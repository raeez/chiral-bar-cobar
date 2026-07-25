r"""Exact type-A non-principal W-algebra data with typed frontier claims.

The engine has three computational lanes.

* Partition and nilpotent-orbit combinatorics are exact.
* Strong-generator weights follow from the ``sl_2`` decomposition of
  ``End(C^N)`` and every generator is even for ``sl_N``.
* Central charges use Kac--Roan--Wakimoto (2003), Theorem 2.1(a),
  equation (2.6).

The modular characteristic, its coefficient ``rho``, the modular conductor,
full shadow depth, bar collapse, DS--bar comparison, and object-level Koszul
duality are frontier quantities.  Their APIs return :class:`ClaimPacket`
objects with ``value=None`` and an explicit status.  This prevents a formal
partition symmetry or a Virasoro subalgebra calculation from becoming a
numeric theorem by type coercion.

For the Bershadsky--Polyakov algebra the primary normalization is the one in
Fehily--Kawasetsu--Ridout (2021), Definition 2.1 and equations (2.1)--(2.2):

    c_BP(k) = -(2k+3)(3k+1)/(k+3).

Its formal reflection ``k -> -k-6`` gives the central scalar sum ``50``.
The shifted expression ``2-24(k+1)^2/(k+3)`` belongs to a separate comparison
surface and gives ``196`` under the same formal reflection.  The unsigned
reciprocal-weight diagnostic is ``17/6``.  Each scalar remains separate from
``kappa``, ``rho``, ``K^kappa``, bar duality, and KSDual membership.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple

from sympy import Rational, Symbol, cancel, simplify, sympify

from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    _partitions_of_n,
    hook_partition,
    normalize_partition,
    partition_size,
    transpose_partition,
    type_a_orbit_class,
    type_a_partition_sl2_triple,
)


k = Symbol("k")


class ClaimStatus(str, Enum):
    """Epistemic status carried by every derived claim surface."""

    PROVED_HERE = "proved_here"
    PROVED_ELSEWHERE = "proved_elsewhere"
    COMPUTED = "computed"
    CONDITIONAL = "conditional"
    OPEN = "open"


class OpenInvariantError(RuntimeError):
    """Raised when a caller requests a numeric value from an open packet."""


@dataclass(frozen=True)
class ClaimPacket:
    """A value together with its mathematical status and proof obligations."""

    statement: str
    status: ClaimStatus
    value: Optional[object]
    evidence: Tuple[str, ...] = ()
    hypotheses: Tuple[str, ...] = ()

    @property
    def resolved(self) -> bool:
        """Whether this packet carries a value available to computation."""

        return self.value is not None

    def require_value(self):
        """Return the value or raise with the outstanding proof obligation."""

        if self.value is None:
            obligations = "; ".join(self.hypotheses) or "a proof or direct computation"
            raise OpenInvariantError(
                f"{self.statement} has status {self.status.value}; resolution requires {obligations}."
            )
        return self.value


@dataclass(frozen=True)
class GeneratorSpec:
    """One strong generator in the PBW generator ledger."""

    label: str
    conformal_weight: object
    parity: str = "even"


@dataclass(frozen=True)
class KRWCentralChargeData:
    """Ingredients of the KRW central-charge formula in type A."""

    partition: Partition
    N: int
    x_diagonal: Tuple[object, ...]
    x_norm_squared: object
    positive_root_grades: Tuple[object, ...]
    dim_g_half: int
    charged_ghost_term: object
    central_charge: object
    source: str


@dataclass(frozen=True)
class WAlgebraBarProfile:
    """Exact algebraic data and typed derived claims for ``W^k(sl_N,f_lambda)``."""

    partition: Partition
    N: int
    transpose: Partition
    orbit_class: str
    is_self_transpose: bool
    generators: Tuple[GeneratorSpec, ...]
    central_charge: ClaimPacket
    rho: ClaimPacket
    modular_characteristic: ClaimPacket
    modular_conductor: ClaimPacket
    full_shadow_depth: ClaimPacket
    bar_collapse: ClaimPacket
    ds_bar_commutation: ClaimPacket
    koszul_duality_candidate: ClaimPacket
    ksdual_membership: ClaimPacket

    @property
    def num_generators(self) -> int:
        return len(self.generators)

    @property
    def num_even(self) -> int:
        return sum(generator.parity == "even" for generator in self.generators)

    @property
    def num_odd(self) -> int:
        return sum(generator.parity == "odd" for generator in self.generators)

    @property
    def generator_weights(self) -> Tuple[Tuple[str, object, str], ...]:
        """Compatibility view of the exact generator ledger."""

        return tuple(
            (generator.label, generator.conformal_weight, generator.parity)
            for generator in self.generators
        )

    @property
    def num_bosonic(self) -> int:
        """Compatibility alias for the even-generator count."""

        return self.num_even

    @property
    def num_fermionic(self) -> int:
        """Compatibility alias for the odd-generator count."""

        return self.num_odd

    @property
    def kappa(self) -> ClaimPacket:
        """Compatibility alias with a typed open value."""

        return self.modular_characteristic

    @property
    def anomaly_ratio(self) -> ClaimPacket:
        """Compatibility alias with a typed open value."""

        return self.rho


@dataclass(frozen=True)
class OPETerm:
    """One pole coefficient in a singular OPE."""

    pole_order: int
    coefficient: object


@dataclass(frozen=True)
class BershadskyPolyakovOPEData:
    """The exact singular OPE surface of the universal BP algebra."""

    level: object
    generators: Tuple[GeneratorSpec, ...]
    singular_products: Tuple[Tuple[str, str, Tuple[OPETerm, ...]], ...]
    source: str

    def terms(self, left: str, right: str) -> Tuple[OPETerm, ...]:
        for lhs, rhs, terms in self.singular_products:
            if lhs == left and rhs == right:
                return terms
        return ()

    def coefficient(self, left: str, right: str, pole_order: int):
        for term in self.terms(left, right):
            if term.pole_order == pole_order:
                return term.coefficient
        return sympify(0)


@dataclass(frozen=True)
class BPScalarAudit:
    """Convention-separated scalar identities for the BP family."""

    level: object
    reflected_level: object
    standard_central_charge: object
    reflected_standard_central_charge: object
    standard_sum: object
    shifted_central_charge: object
    reflected_shifted_central_charge: object
    shifted_sum: object
    reciprocal_weight_diagnostic: Rational
    modular_characteristic: ClaimPacket
    rho: ClaimPacket
    modular_conductor: ClaimPacket


def _open_packet(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(
        statement=statement,
        status=ClaimStatus.OPEN,
        value=None,
        hypotheses=tuple(hypotheses),
    )


def _conditional_packet(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(
        statement=statement,
        status=ClaimStatus.CONDITIONAL,
        value=None,
        hypotheses=tuple(hypotheses),
    )


def all_partitions_of(N: int) -> Tuple[Partition, ...]:
    """Return all partitions of ``N`` in decreasing lexicographic order."""

    if N < 1:
        raise ValueError("N must be a positive integer")
    return _partitions_of_n(N)


def type_a_generator_weight_multiplicities(
    partition: Partition,
) -> Tuple[Tuple[object, int], ...]:
    r"""Compute the strong-generator weights from the ``sl_2`` decomposition.

    If ``V = direct_sum_i V_{lambda_i-1}``, then each ordered pair of blocks
    contributes

    ``V_{lambda_i-1} tensor V_{lambda_j-1}``
    ``= direct_sum_{r=0}^{min(lambda_i,lambda_j)-1}``
    ``V_{lambda_i+lambda_j-2-2r}``.

    The lowest-weight line in each summand gives a centralizer generator of
    conformal weight ``(lambda_i+lambda_j)/2-r``.  Removing the scalar line
    passes from ``gl_N`` to ``sl_N``.
    """

    lam = normalize_partition(partition)
    multiplicities: Counter = Counter()
    for left in lam:
        for right in lam:
            for r in range(min(left, right)):
                weight = Rational(left + right, 2) - r
                multiplicities[weight] += 1

    multiplicities[Rational(1)] -= 1
    if multiplicities[Rational(1)] == 0:
        del multiplicities[Rational(1)]
    return tuple(sorted(multiplicities.items(), key=lambda item: item[0]))


def type_a_strong_generators(partition: Partition) -> Tuple[GeneratorSpec, ...]:
    """Return the PBW strong-generator ledger; every type-A generator is even."""

    lam = normalize_partition(partition)
    if lam == (2, 1):
        return (
            GeneratorSpec("J", Rational(1)),
            GeneratorSpec("G+", Rational(3, 2)),
            GeneratorSpec("G-", Rational(3, 2)),
            GeneratorSpec("L", Rational(2)),
        )

    generators: List[GeneratorSpec] = []
    for weight, multiplicity in type_a_generator_weight_multiplicities(lam):
        for index in range(1, multiplicity + 1):
            generators.append(GeneratorSpec(f"W[{weight}]_{index}", weight))
    return tuple(generators)


def type_a_krw_central_charge_data(
    partition: Partition,
    level=k,
) -> KRWCentralChargeData:
    r"""Evaluate KRW (2003), Theorem 2.1(a), equation (2.6), for ``sl_N``.

    With ``x=h/2`` and trace-form normalization,

    ``c = k dim(g)/(k+N) - 12 k (x|x)``
    ``    - sum_{alpha(x)>0}(12m_alpha^2-12m_alpha+2)``
    ``    - dim(g_{1/2})/2``.
    """

    lam = normalize_partition(partition)
    N = partition_size(lam)
    kk = sympify(level)
    triple = type_a_partition_sl2_triple(lam)
    x_diagonal = tuple(Rational(triple.h[i, i], 2) for i in range(N))
    x_norm_squared = sum(value * value for value in x_diagonal)

    positive_root_grades = tuple(
        x_diagonal[i] - x_diagonal[j]
        for i in range(N)
        for j in range(N)
        if x_diagonal[i] - x_diagonal[j] > 0
    )
    dim_g_half = sum(grade == Rational(1, 2) for grade in positive_root_grades)
    charged_ghost_term = sum(
        12 * grade**2 - 12 * grade + 2 for grade in positive_root_grades
    )
    central_charge = cancel(
        kk * (N * N - 1) / (kk + N)
        - 12 * kk * x_norm_squared
        - charged_ghost_term
        - Rational(dim_g_half, 2)
    )
    return KRWCentralChargeData(
        partition=lam,
        N=N,
        x_diagonal=x_diagonal,
        x_norm_squared=x_norm_squared,
        positive_root_grades=positive_root_grades,
        dim_g_half=dim_g_half,
        charged_ghost_term=charged_ghost_term,
        central_charge=central_charge,
        source="Kac--Roan--Wakimoto (2003), Theorem 2.1(a), equation (2.6)",
    )


def type_a_krw_central_charge(partition: Partition, level=k):
    """Return the exact KRW central charge in the standard level convention."""

    return type_a_krw_central_charge_data(partition, level).central_charge


def formal_level_reflection(N: int, level=k):
    """Return the algebraic involution ``k -> -k-2N``."""

    if N < 1:
        raise ValueError("N must be a positive integer")
    return -sympify(level) - 2 * N


def bershadsky_polyakov_central_charge(level=k):
    r"""Return ``c_BP(k)=-(2k+3)(3k+1)/(k+3)`` in the FKR convention."""

    kk = sympify(level)
    return cancel(-((2 * kk + 3) * (3 * kk + 1)) / (kk + 3))


def bershadsky_polyakov_shifted_central_charge(level=k):
    """Return the convention-disjoint shifted BP comparison scalar."""

    kk = sympify(level)
    return cancel(2 - 24 * (kk + 1) ** 2 / (kk + 3))


def bershadsky_polyakov_reciprocal_weight_diagnostic() -> Rational:
    """Return the unsigned reciprocal-weight diagnostic ``1+2(2/3)+1/2``."""

    return Rational(1) + 2 * Rational(2, 3) + Rational(1, 2)


def bershadsky_polyakov_ope_data(level=k) -> BershadskyPolyakovOPEData:
    """Return the singular OPE coefficients of FKR (2021), equation (2.1)."""

    kk = sympify(level)
    J = Symbol("J")
    G_plus = Symbol("G_plus")
    G_minus = Symbol("G_minus")
    L = Symbol("L")
    dJ = Symbol("dJ")
    dG_plus = Symbol("dG_plus")
    dG_minus = Symbol("dG_minus")
    dL = Symbol("dL")
    normal_JJ = Symbol("normal_JJ")
    products = (
        ("L", "L", (
            OPETerm(4, bershadsky_polyakov_central_charge(kk) / 2),
            OPETerm(2, 2 * L),
            OPETerm(1, dL),
        )),
        ("L", "J", (OPETerm(2, J), OPETerm(1, dJ))),
        ("L", "G+", (OPETerm(2, Rational(3, 2) * G_plus), OPETerm(1, dG_plus))),
        ("L", "G-", (OPETerm(2, Rational(3, 2) * G_minus), OPETerm(1, dG_minus))),
        ("J", "J", (OPETerm(2, (2 * kk + 3) / 3),)),
        ("J", "G+", (OPETerm(1, G_plus),)),
        ("J", "G-", (OPETerm(1, -G_minus),)),
        ("G+", "G+", ()),
        ("G-", "G-", ()),
        ("G+", "G-", (
            OPETerm(3, (kk + 1) * (2 * kk + 3)),
            OPETerm(2, 3 * (kk + 1) * J),
            OPETerm(
                1,
                3 * normal_JJ + Rational(3, 2) * (kk + 1) * dJ - (kk + 3) * L,
            ),
        )),
    )
    return BershadskyPolyakovOPEData(
        level=kk,
        generators=type_a_strong_generators((2, 1)),
        singular_products=products,
        source="Fehily--Kawasetsu--Ridout (2021), Definition 2.1, equations (2.1)--(2.2)",
    )


def bershadsky_polyakov_kappa(level=k) -> ClaimPacket:
    """Return the typed open modular characteristic packet for BP."""

    return _open_packet(
        f"kappa_BP({sympify(level)})",
        "a nonseparating genus-one calculation with charged ghosts, neutral fields, improvement, and mixed channels",
    )


def bershadsky_polyakov_anomaly_ratio() -> ClaimPacket:
    """Return the typed open ``rho_BP`` packet."""

    return _open_packet(
        "rho_BP in kappa_BP=rho_BP c_BP",
        "a theorem identifying the modular characteristic with a central-charge multiple",
    )


def bershadsky_polyakov_scalar_audit(level=k) -> BPScalarAudit:
    """Compute the two central scalar identities while preserving conventions."""

    kk = sympify(level)
    reflected = formal_level_reflection(3, kk)
    standard = bershadsky_polyakov_central_charge(kk)
    standard_reflected = bershadsky_polyakov_central_charge(reflected)
    shifted = bershadsky_polyakov_shifted_central_charge(kk)
    shifted_reflected = bershadsky_polyakov_shifted_central_charge(reflected)
    return BPScalarAudit(
        level=kk,
        reflected_level=reflected,
        standard_central_charge=standard,
        reflected_standard_central_charge=standard_reflected,
        standard_sum=simplify(standard + standard_reflected),
        shifted_central_charge=shifted,
        reflected_shifted_central_charge=shifted_reflected,
        shifted_sum=simplify(shifted + shifted_reflected),
        reciprocal_weight_diagnostic=bershadsky_polyakov_reciprocal_weight_diagnostic(),
        modular_characteristic=bershadsky_polyakov_kappa(kk),
        rho=bershadsky_polyakov_anomaly_ratio(),
        modular_conductor=_open_packet(
            "K_BP^kappa",
            "values of kappa_BP in a common convention at both reflected levels",
        ),
    )


def _profile_claims(partition: Partition) -> Dict[str, ClaimPacket]:
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    package = "H_nonprincipal^{DS/bar}: filtered BRST comparison, strict completion, and Verdier pairing"
    return {
        "rho": _open_packet(
            f"rho for W(sl_{partition_size(lam)}, f_{lam})",
            "a genus-one modular calculation",
        ),
        "modular_characteristic": _open_packet(
            f"kappa for W(sl_{partition_size(lam)}, f_{lam})",
            "a nonseparating genus-one calculation",
        ),
        "modular_conductor": _open_packet(
            f"K^kappa for W(sl_{partition_size(lam)}, f_{lam})",
            "modular characteristics at both comparison levels",
        ),
        "full_shadow_depth": _open_packet(
            f"full shadow depth for W(sl_{partition_size(lam)}, f_{lam})",
            "Maurer--Cartan coefficients beyond the Virasoro line",
        ),
        "bar_collapse": _open_packet(
            f"completed chiral bar collapse for W(sl_{partition_size(lam)}, f_{lam})",
            "a filtered chiral bar comparison and convergence proof",
        ),
        "ds_bar_commutation": _conditional_packet(
            f"DS--bar comparison for W(sl_{partition_size(lam)}, f_{lam})",
            package,
        ),
        "koszul_duality_candidate": _conditional_packet(
            f"candidate comparison with transpose partition {lam_t}",
            package,
            "a finite or continuously perfect Verdier pairing",
        ),
        "ksdual_membership": _open_packet(
            f"KSDual membership for W(sl_{partition_size(lam)}, f_{lam})",
            "an object-level fixed-point equivalence",
        ),
    }


def w_algebra_bar_profile(partition: Partition, level=k) -> WAlgebraBarProfile:
    """Return exact orbit data and typed frontier claims for one type-A reduction."""

    lam = normalize_partition(partition)
    N = partition_size(lam)
    lam_t = transpose_partition(lam)
    c_data = type_a_krw_central_charge_data(lam, level)
    claims = _profile_claims(lam)
    central_charge = ClaimPacket(
        statement=f"KRW central charge of W^{sympify(level)}(sl_{N}, f_{lam})",
        status=ClaimStatus.PROVED_ELSEWHERE,
        value=c_data.central_charge,
        evidence=(c_data.source,),
    )
    return WAlgebraBarProfile(
        partition=lam,
        N=N,
        transpose=lam_t,
        orbit_class=type_a_orbit_class(lam),
        is_self_transpose=lam == lam_t,
        generators=type_a_strong_generators(lam),
        central_charge=central_charge,
        rho=claims["rho"],
        modular_characteristic=claims["modular_characteristic"],
        modular_conductor=claims["modular_conductor"],
        full_shadow_depth=claims["full_shadow_depth"],
        bar_collapse=claims["bar_collapse"],
        ds_bar_commutation=claims["ds_bar_commutation"],
        koszul_duality_candidate=claims["koszul_duality_candidate"],
        ksdual_membership=claims["ksdual_membership"],
    )


def bershadsky_polyakov_profile() -> WAlgebraBarProfile:
    """Return the standard-convention BP profile."""

    return w_algebra_bar_profile((2, 1))


def sl4_hook_211_profile() -> WAlgebraBarProfile:
    """Return the exact profile for the ``(2,1,1)`` reduction of ``sl_4``."""

    return w_algebra_bar_profile((2, 1, 1))


def sl4_subregular_31_profile() -> WAlgebraBarProfile:
    """Return the exact profile for the ``(3,1)`` reduction of ``sl_4``."""

    return w_algebra_bar_profile((3, 1))


def principal_w_n_profile(N: int) -> WAlgebraBarProfile:
    """Return the exact profile for the principal partition ``(N)``."""

    return w_algebra_bar_profile((N,))


def ds_kappa_additivity_check(partition: Partition, test_levels=None) -> ClaimPacket:
    """Return the open DS/modular comparison packet.

    Subtracting an expression from itself produces an algebraic identity.  A
    DS--bar theorem instead requires the filtered BRST and modular comparison
    named in the packet.
    """

    lam = normalize_partition(partition)
    return _conditional_packet(
        f"DS compatibility of kappa for partition {lam}",
        "H_nonprincipal^{DS/bar}",
        "a direct genus-one calculation on both sides",
    )


def kappa_multi_path_verification(partition: Partition, test_levels=None) -> ClaimPacket:
    """Return one open modular-verification obligation.

    The packet records three genuinely independent evidence routes: a
    genus-one computation, a categorical comparison, and a specialization.
    """

    lam = normalize_partition(partition)
    return _open_packet(
        f"independent verification of kappa for partition {lam}",
        "a genus-one calculation",
        "a categorical comparison theorem",
        "an independent specialization or literature value",
    )


def ds_depth_comparison(partition: Partition) -> ClaimPacket:
    """Return the open full-shadow comparison across DS reduction."""

    lam = normalize_partition(partition)
    return _open_packet(
        f"full shadow-depth comparison across DS for partition {lam}",
        "the full Maurer--Cartan tower on source and target",
        "a DS compatibility theorem for that tower",
    )


def ds_depth_increase_all_nilpotents(N: int) -> List[ClaimPacket]:
    """Return one typed shadow-depth obligation for each nonzero orbit."""

    return [
        ds_depth_comparison(lam)
        for lam in all_partitions_of(N)
        if lam != (1,) * N
    ]


def sl4_hook_duality_check() -> Dict[str, object]:
    """Return exact transpose data and a conditional object-level comparison."""

    source = (2, 1, 1)
    target = (3, 1)
    return {
        "source_partition": source,
        "target_partition": target,
        "are_transposes": transpose_partition(source) == target,
        "formal_level_reflection": formal_level_reflection(4, k),
        "koszul_duality": _conditional_packet(
            "object-level comparison of the sl_4 hook pair",
            "H_nonprincipal^{DS/bar}",
            "a finite or continuously perfect Verdier pairing",
        ),
    }


def hook_type_edge_compatibility(N: int) -> List[Dict[str, object]]:
    """Return exact hook/transpose combinatorics and typed transport claims."""

    results: List[Dict[str, object]] = []
    for r in range(1, N - 1):
        lam = hook_partition(N, r)
        lam_t = transpose_partition(lam)
        results.append({
            "r": r,
            "partition": lam,
            "transpose": lam_t,
            "transpose_involution": transpose_partition(lam_t) == lam,
            "duality_candidate": _conditional_packet(
                f"hook transport from {lam} to {lam_t}",
                "H_nonprincipal^{DS/bar}",
            ),
        })
    return results


def transport_propagation_summary(max_N: int = 8) -> List[Dict[str, object]]:
    """Return the exact hook census and one typed transport obligation per rank."""

    summaries: List[Dict[str, object]] = []
    for N in range(3, max_N + 1):
        hooks = hook_type_edge_compatibility(N)
        summaries.append({
            "N": N,
            "num_partitions": len(all_partitions_of(N)),
            "num_hooks": len(hooks),
            "hook_edge_data": hooks,
            "transport": _conditional_packet(
                f"transport propagation across the sl_{N} hook corridor",
                "explicit reduction functors on every edge",
                "H_nonprincipal^{DS/bar}",
            ),
        })
    return summaries


def nilpotent_classification_table(N: int) -> List[Dict[str, object]]:
    """Return the exact partition/generator/KRW census with typed derived fields."""

    table: List[Dict[str, object]] = []
    for lam in all_partitions_of(N):
        profile = w_algebra_bar_profile(lam)
        table.append({
            "partition": lam,
            "transpose": profile.transpose,
            "orbit_class": profile.orbit_class,
            "num_generators": profile.num_generators,
            "num_even": profile.num_even,
            "num_odd": profile.num_odd,
            "generator_weights": tuple(
                generator.conformal_weight for generator in profile.generators
            ),
            "central_charge": profile.central_charge,
            "rho": profile.rho,
            "kappa": profile.modular_characteristic,
            "K_kappa": profile.modular_conductor,
            "full_shadow_depth": profile.full_shadow_depth,
            "bar_collapse": profile.bar_collapse,
            "ds_bar_commutation": profile.ds_bar_commutation,
            "koszul_duality_candidate": profile.koszul_duality_candidate,
            "ksdual_membership": profile.ksdual_membership,
            "is_self_transpose": profile.is_self_transpose,
        })
    return table


def sl6_full_classification() -> List[Dict[str, object]]:
    """Return the exact partition/generator/KRW census for ``sl_6``."""

    return nilpotent_classification_table(6)


def transpose_partition_pairs(N: int) -> List[Dict[str, object]]:
    """Partition the Young diagrams of ``N`` into transpose orbits."""

    seen = set()
    pairs: List[Dict[str, object]] = []
    for lam in all_partitions_of(N):
        if lam in seen:
            continue
        lam_t = transpose_partition(lam)
        seen.add(lam)
        seen.add(lam_t)
        pairs.append({
            "type": "self-transpose" if lam == lam_t else "transpose-pair",
            "partition": lam,
            "transpose": lam_t,
        })
    return pairs


def koszul_dual_pairs(N: int) -> List[Dict[str, object]]:
    """Compatibility API exposing transpose orbits and typed duality claims."""

    results: List[Dict[str, object]] = []
    for pair in transpose_partition_pairs(N):
        lam = pair["partition"]
        lam_t = pair["transpose"]
        results.append({
            **pair,
            "koszul_duality": _conditional_packet(
                f"object-level Koszul comparison between {lam} and {lam_t}",
                "H_nonprincipal^{DS/bar}",
                "a finite or continuously perfect Verdier pairing",
            ),
        })
    return results


def principal_vs_nonprincipal_comparison(N: int) -> List[Dict[str, object]]:
    """Return exact orbit, generator, and KRW data across all partitions."""

    results: List[Dict[str, object]] = []
    for lam in all_partitions_of(N):
        profile = w_algebra_bar_profile(lam)
        results.append({
            "partition": lam,
            "orbit_class": profile.orbit_class,
            "is_principal": lam == (N,),
            "num_generators": profile.num_generators,
            "central_charge": profile.central_charge,
            "derived_invariants": _open_packet(
                f"modular and bar comparison data for partition {lam}",
                "genus-one and filtered bar calculations",
            ),
        })
    return results
