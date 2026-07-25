r"""Exact type-A DS data with typed DS--bar and duality claims.

The ``sl_3`` subregular reduction is the Bershadsky--Polyakov algebra in the
Fehily--Kawasetsu--Ridout normalization.  Its strong generators
``J,G^+,G^-,L`` are even, with weights ``1,3/2,3/2,2`` and standard central
charge

``c_BP(k)=-(2k+3)(3k+1)/(k+3)``.

This engine imports that OPE packet once from the canonical non-principal
module.  It also computes exact affine arithmetic, good-grading BRST
dimensions, KRW central charges, partition transpose, and formal level
reflection.  DS--bar comparison, PBW collapse, chiral Koszulness,
categorical transport, transpose duality, and KSDual membership return typed
claim packets under named hypothesis packages.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.hook_type_w_duality import (
    ClaimPacket,
    ClaimStatus,
    OpenInvariantError,
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    ghost_constant,
    hook_dual_level_sl_n,
    kappa_complementarity_sum,
    krw_central_charge,
    reciprocal_weight_diagnostic_from_partition,
    w_algebra_generator_data,
)
from compute.lib.non_principal_beyond_hook_engine import (
    BRSTComplexData,
    brst_complex_analysis,
)
from compute.lib.non_principal_w_bar_engine import (
    BershadskyPolyakovOPEData,
    bershadsky_polyakov_central_charge,
    bershadsky_polyakov_ope_data,
)
from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    normalize_partition,
    partition_size,
    transpose_partition,
)
from compute.lib.theorem_butson_inverse_reduction_engine import (
    verify_transport_to_transpose,
)


k = Symbol("k")
BP_OPE_SOURCE = (
    "Fehily--Kawasetsu--Ridout (2021), Definition 2.1, equations (2.1)--(2.2)"
)
KRW_SOURCE = "Kac--Roan--Wakimoto (2003), Theorem 2.1(a), equation (2.6)"

H_DS_BAR = (
    "H_DS-bar: a filtered chain map between DS(B(V_k(sl_N))) and "
    "B(W^k(sl_N,f)), strict convergence, and completion compatibility"
)
H_PBW_BAR = (
    "H_PBW-bar: collapse and extension control for the PBW-to-chiral-bar "
    "spectral sequence with a compatible twisting morphism"
)
H_BP_BAR = (
    "H_BP-bar: a direct completed chiral-bar computation for the standard "
    "Bershadsky--Polyakov OPE packet"
)
H_MODULAR = (
    "H_DS-modular: direct genus-one characteristics before and after DS in "
    "one normalization, with charged, neutral, and improvement channels"
)
H_TRANSPORT = (
    "H_DS-transport: realized inverse-reduction functors along the finite "
    "Hasse path, compatible with DS, bar, and Verdier completion"
)
H_KOSZUL = (
    "H_DS-Koszul: DS--bar comparison, PBW/bar collapse, and a perfect "
    "twisting comparison for source and target"
)
H_DUALITY = (
    "H_transpose-duality: an object-level Koszul equivalence at formal "
    "reflected level with explicit hypothesis package"
)
H_KSDUAL = (
    "H_KSDual: fixed-point equivalence compatible with DS/bar and transpose "
    "transport"
)


def _open(statement: str, *hypotheses: str, evidence: Tuple[str, ...] = ()) -> ClaimPacket:
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


def _ope_coefficient(
    ope: BershadskyPolyakovOPEData,
    left: str,
    right: str,
    pole: int,
):
    for source, target, terms in ope.singular_products:
        if source == left and target == right:
            for term in terms:
                if term.pole_order == pole:
                    return term.coefficient
    raise KeyError((left, right, pole))


@dataclass(frozen=True)
class N2SCAData:
    r"""Compatibility record carrying the standard BP OPE data.

    The historical class name remains for import stability; the mathematical
    object represented here is the Bershadsky--Polyakov algebra.
    """

    level: object
    central_charge: object
    generators: Tuple[Tuple[str, object, str], ...]
    ope_data: BershadskyPolyakovOPEData
    formal_reflected_level: object
    formal_central_sum: object
    source: str

    @property
    def exact_pole_orders(self) -> Tuple[Tuple[str, str, int], ...]:
        return tuple(
            (left, right, max((term.pole_order for term in terms), default=0))
            for left, right, terms in self.ope_data.singular_products
        )

    @property
    def jj_pole2(self):
        return _ope_coefficient(self.ope_data, "J", "J", 2)

    @property
    def jg_charge(self):
        coefficient = _ope_coefficient(self.ope_data, "J", "G+", 1)
        return simplify(coefficient / Symbol("G_plus"))

    @property
    def jg_minus_charge(self):
        coefficient = _ope_coefficient(self.ope_data, "J", "G-", 1)
        return simplify(coefficient / Symbol("G_minus"))

    @property
    def gg_pole3(self):
        return _ope_coefficient(self.ope_data, "G+", "G-", 3)

    @property
    def gg_pole2_coeff(self):
        coefficient = _ope_coefficient(self.ope_data, "G+", "G-", 2)
        return simplify(coefficient / Symbol("J"))

    @property
    def gg_pole1(self):
        return _ope_coefficient(self.ope_data, "G+", "G-", 1)

    @property
    def tt_pole4(self):
        return _ope_coefficient(self.ope_data, "L", "L", 4)


BershadskyPolyakovData = N2SCAData


def bershadsky_polyakov_data(level=k) -> BershadskyPolyakovData:
    r"""Return the canonical BP generator, OPE, and reflection packet."""

    level = sympify(level)
    ope = bershadsky_polyakov_ope_data(level)
    reflected = hook_dual_level_sl_n(3, level)
    central_charge = bershadsky_polyakov_central_charge(level)
    return BershadskyPolyakovData(
        level=level,
        central_charge=central_charge,
        generators=tuple(
            (generator.label, generator.conformal_weight, generator.parity)
            for generator in ope.generators
        ),
        ope_data=ope,
        formal_reflected_level=reflected,
        formal_central_sum=simplify(
            central_charge + bershadsky_polyakov_central_charge(reflected)
        ),
        source=ope.source,
    )


def n2_sca_data(level=k) -> N2SCAData:
    r"""Compatibility entry point for :func:`bershadsky_polyakov_data`."""

    return bershadsky_polyakov_data(level)


@dataclass(frozen=True)
class BarComplexData:
    r"""Exact BP bar input and typed higher-bar consequences."""

    partition: Partition
    level: object
    chain_degree_zero_dimension: int
    chain_degree_one_generators: Tuple[Tuple[str, object, str], ...]
    singular_ope_channels: Tuple[Tuple[str, str, int], ...]
    ope_data: BershadskyPolyakovOPEData
    higher_bar_cohomology: ClaimPacket
    pbw_collapse: ClaimPacket
    koszulness: ClaimPacket

    @property
    def h0_dim(self) -> int:
        return self.chain_degree_zero_dimension

    @property
    def h1_generators(self) -> Tuple[Tuple[str, object, str], ...]:
        return self.chain_degree_one_generators

    @property
    def h1_dim(self) -> int:
        return len(self.chain_degree_one_generators)

    @property
    def is_koszul(self) -> ClaimPacket:
        return self.koszulness


def bar_complex_n2_sca(level=k) -> BarComplexData:
    r"""Return the exact BP bar input and unresolved higher cohomology."""

    bp = bershadsky_polyakov_data(level)
    return BarComplexData(
        partition=(2, 1),
        level=bp.level,
        chain_degree_zero_dimension=1,
        chain_degree_one_generators=bp.generators,
        singular_ope_channels=bp.exact_pole_orders,
        ope_data=bp.ope_data,
        higher_bar_cohomology=_open(
            "completed higher chiral-bar cohomology of the BP algebra",
            H_BP_BAR,
            evidence=(BP_OPE_SOURCE,),
        ),
        pbw_collapse=_conditional(
            "PBW-to-bar collapse for the BP algebra",
            H_BP_BAR,
            H_PBW_BAR,
            evidence=(BP_OPE_SOURCE,),
        ),
        koszulness=_conditional(
            "chiral Koszulness of the BP algebra",
            H_BP_BAR,
            H_PBW_BAR,
            H_KOSZUL,
        ),
    )


def dim_sl_n(N: int) -> int:
    r"""Return ``dim sl_N=N^2-1``."""

    if N < 2:
        raise ValueError("N must be at least 2")
    return N * N - 1


def affine_kappa_sl_n(N: int, level=k):
    r"""Return the canonical affine class-L characteristic convention."""

    level = sympify(level)
    return Rational(dim_sl_n(N), 2 * N) * (level + N)


def affine_central_charge_sl_n(N: int, level=k):
    r"""Return the Sugawara central charge of ``V^k(sl_N)``."""

    level = sympify(level)
    return simplify(level * dim_sl_n(N) / (level + N))


def ds_good_grading_data(partition: Partition) -> BRSTComplexData:
    r"""Return the canonical exact type-A good-grading packet."""

    return brst_complex_analysis(normalize_partition(partition))


def ds_nilpotent_plus_dim(partition: Partition) -> int:
    r"""Return ``dim n_+`` for the good grading."""

    return ds_good_grading_data(partition).n_plus_dim


def ds_nilpotent_half_dim(partition: Partition) -> int:
    r"""Return ``dim g_{1/2}`` for the good grading."""

    return ds_good_grading_data(partition).g_half_dim


@dataclass(frozen=True)
class DSBarCommutationData:
    r"""Exact DS input data and typed comparison claims."""

    lie_algebra: str
    rank: int
    partition: Partition
    level: object
    affine_generators: int
    affine_kappa: object
    affine_central_charge: object
    w_generators: int
    w_generator_weights: Tuple[Rational, ...]
    w_num_even: int
    w_num_odd: int
    w_central_charge: object
    positive_grade_multiplicities: Dict[Rational, int]
    positive_subalgebra_is_abelian: bool
    ghost_dim: int
    neutral_half_dimension: int
    ghost_constant_value: object
    reciprocal_weight_diagnostic: Rational
    rho: ClaimPacket
    w_kappa: ClaimPacket
    pbw_collapse: ClaimPacket
    ds_bar_commutation: ClaimPacket
    koszulness: ClaimPacket
    categorical_transport: ClaimPacket

    @property
    def kappa_commutes(self) -> ClaimPacket:
        return self.ds_bar_commutation


def ds_bar_commutation_check(
    partition: Partition,
    level=k,
) -> DSBarCommutationData:
    r"""Return exact DS arithmetic and the chain-level comparison packet."""

    lam = normalize_partition(partition)
    N = partition_size(lam)
    level = sympify(level)
    generators = w_algebra_generator_data(lam)
    grading = ds_good_grading_data(lam)
    transpose_profile = verify_transport_to_transpose(lam, level)
    weights = tuple(
        sorted(Rational(weight) for _, weight, _ in generators.strong_generators)
    )
    return DSBarCommutationData(
        lie_algebra=f"sl_{N}",
        rank=N - 1,
        partition=lam,
        level=level,
        affine_generators=dim_sl_n(N),
        affine_kappa=affine_kappa_sl_n(N, level),
        affine_central_charge=affine_central_charge_sl_n(N, level),
        w_generators=generators.f_centralizer_dimension,
        w_generator_weights=weights,
        w_num_even=generators.n_even,
        w_num_odd=generators.n_odd,
        w_central_charge=krw_central_charge(lam, level),
        positive_grade_multiplicities=grading.n_plus_grades,
        positive_subalgebra_is_abelian=grading.n_plus_is_abelian,
        ghost_dim=grading.n_plus_dim,
        neutral_half_dimension=grading.g_half_dim,
        ghost_constant_value=ghost_constant(lam),
        reciprocal_weight_diagnostic=reciprocal_weight_diagnostic_from_partition(lam),
        rho=anomaly_ratio_from_partition(lam),
        w_kappa=ds_kappa_from_affine(lam, level),
        pbw_collapse=_conditional(
            f"PBW-to-bar collapse after DS reduction at partition {lam}",
            H_PBW_BAR,
        ),
        ds_bar_commutation=_conditional(
            f"DS--bar comparison for W^{level}(sl_{N},f_{lam})",
            H_DS_BAR,
        ),
        koszulness=_conditional(
            f"chiral Koszulness for W^{level}(sl_{N},f_{lam})",
            H_DS_BAR,
            H_PBW_BAR,
            H_KOSZUL,
        ),
        categorical_transport=transpose_profile.categorical_transport,
    )


def _critical_pole_for_bp() -> bool:
    numerator_after_clearing = simplify(
        (k + 3) * bershadsky_polyakov_central_charge(k)
    )
    return simplify(numerator_after_clearing.subs(k, -3)) != 0


def sl3_minimal_data(level=k) -> Dict[str, object]:
    r"""Return the exact BP seed packet and typed homological claims."""

    level = sympify(level)
    lam = (2, 1)
    generators = w_algebra_generator_data(lam)
    reflected = hook_dual_level_sl_n(3, level)
    bp = bershadsky_polyakov_data(level)
    return {
        "partition": lam,
        "transpose": transpose_partition(lam),
        "is_self_transpose": transpose_partition(lam) == lam,
        "N": 3,
        "generators": generators,
        "n_generators": generators.f_centralizer_dimension,
        "n_even": generators.n_even,
        "n_odd": generators.n_odd,
        "n_bosonic": generators.n_even,
        "n_fermionic": generators.n_odd,
        "central_charge": bp.central_charge,
        "formal_reflected_level": reflected,
        "formal_central_sum": bp.formal_central_sum,
        "formal_fixed_level": Rational(-3),
        "central_charge_has_pole_at_fixed_level": _critical_pole_for_bp(),
        "reciprocal_weight_diagnostic": reciprocal_weight_diagnostic_from_partition(lam),
        "rho": anomaly_ratio_from_partition(lam),
        "kappa": ds_kappa_from_affine(lam, level),
        "reflected_kappa": ds_kappa_from_affine(lam, reflected),
        "modular_conductor": kappa_complementarity_sum(lam, level),
        "ghost_constant": ghost_constant(lam),
        "bar_complex": bar_complex_n2_sca(level),
        "ds_bar_check": ds_bar_commutation_check(lam, level),
    }


def sl4_hook_ds_bar_data(level=k) -> Dict[str, object]:
    r"""Return exact data for the ``(2,1,1)`` and ``(3,1)`` hook pair."""

    level = sympify(level)
    source = (2, 1, 1)
    target = (3, 1)
    reflected = hook_dual_level_sl_n(4, level)
    duality = koszul_dual_identification(source, level)
    return {
        "minimal_check": ds_bar_commutation_check(source, level),
        "subregular_check": ds_bar_commutation_check(target, level),
        "source_partition": source,
        "transpose_partition": target,
        "formal_reflected_level": reflected,
        "formal_central_sum": simplify(
            krw_central_charge(source, level)
            + krw_central_charge(target, reflected)
        ),
        "source_kappa": ds_kappa_from_affine(source, level),
        "transpose_kappa": ds_kappa_from_affine(target, reflected),
        "modular_conductor": kappa_complementarity_sum(source, level),
        "duality": duality,
    }


@dataclass(frozen=True)
class KoszulDualIdentification:
    r"""Exact formal transpose data and typed object-level duality."""

    source_partition: Partition
    source_level: object
    dual_partition: Partition
    dual_level: object
    N: int
    source_central_charge: object
    dual_central_charge: object
    formal_central_sum: object
    formal_central_sum_k_independent: Optional[bool]
    source_reciprocal_weight_diagnostic: Rational
    dual_reciprocal_weight_diagnostic: Rational
    source_rho: ClaimPacket
    dual_rho: ClaimPacket
    source_kappa: ClaimPacket
    dual_kappa: ClaimPacket
    modular_conductor: ClaimPacket
    is_self_transpose: bool
    formal_fixed_level: object
    self_dual_level: Optional[object]
    hasse_path_to_transpose: Tuple[Partition, ...]
    categorical_transport: ClaimPacket
    bar_compatibility: ClaimPacket
    koszul_duality: ClaimPacket
    ksdual_membership: ClaimPacket

    @property
    def source_c(self):
        return self.source_central_charge

    @property
    def dual_c(self):
        return self.dual_central_charge

    @property
    def c_sum(self):
        return self.formal_central_sum


def koszul_dual_identification(
    partition: Partition,
    level=k,
) -> KoszulDualIdentification:
    r"""Return formal transpose arithmetic and the duality obligation."""

    lam = normalize_partition(partition)
    N = partition_size(lam)
    level = sympify(level)
    profile = verify_transport_to_transpose(lam, level)
    fixed_level = Rational(-N)
    return KoszulDualIdentification(
        source_partition=lam,
        source_level=level,
        dual_partition=profile.transpose,
        dual_level=profile.formal_reflected_level,
        N=N,
        source_central_charge=profile.source_central_charge,
        dual_central_charge=profile.transpose_reflected_central_charge,
        formal_central_sum=profile.formal_central_sum,
        formal_central_sum_k_independent=profile.formal_central_sum_k_independent,
        source_reciprocal_weight_diagnostic=profile.source_reciprocal_weight_diagnostic,
        dual_reciprocal_weight_diagnostic=profile.transpose_reciprocal_weight_diagnostic,
        source_rho=profile.source_rho,
        dual_rho=profile.transpose_rho,
        source_kappa=profile.source_kappa,
        dual_kappa=profile.transpose_kappa,
        modular_conductor=profile.modular_conductor,
        is_self_transpose=profile.is_self_transpose,
        formal_fixed_level=fixed_level,
        self_dual_level=fixed_level if profile.is_self_transpose else None,
        hasse_path_to_transpose=profile.hasse_path_to_transpose,
        categorical_transport=profile.categorical_transport,
        bar_compatibility=_conditional(
            f"DS--bar compatibility along transpose path for {lam}",
            H_DS_BAR,
            H_TRANSPORT,
        ),
        koszul_duality=_conditional(
            f"object-level Koszul duality between {lam} and {profile.transpose}",
            H_KOSZUL,
            H_DUALITY,
        ),
        ksdual_membership=_conditional(
            f"KSDual membership for partition {lam}",
            H_KSDUAL,
        ),
    )


@dataclass(frozen=True)
class DSBarAudit:
    r"""Exact regression checks and typed theorem-level claims."""

    exact_checks: Tuple[Tuple[str, bool], ...]
    claims: Tuple[ClaimPacket, ...]

    @property
    def all_exact_checks_pass(self) -> bool:
        return all(value for _, value in self.exact_checks)

    @property
    def exact_check_count(self) -> int:
        return len(self.exact_checks)


def verify_ds_bar_commutation() -> DSBarAudit:
    r"""Audit exact DS input data and expose the open comparison surface."""

    bp = bershadsky_polyakov_data(k)
    bp_ds = ds_bar_commutation_check((2, 1), k)
    hook_min = ds_bar_commutation_check((2, 1, 1), k)
    hook_sub = ds_bar_commutation_check((3, 1), k)
    bp_duality = koszul_dual_identification((2, 1), k)
    hook_duality = koszul_dual_identification((2, 1, 1), k)
    exact_checks = (
        ("BP partition is self-transpose", transpose_partition((2, 1)) == (2, 1)),
        ("BP has four strong generators", bp_ds.w_generators == 4),
        ("BP strong generators are even", bp_ds.w_num_even == 4 and bp_ds.w_num_odd == 0),
        (
            "BP weights are 1,3/2,3/2,2",
            bp_ds.w_generator_weights == (1, Rational(3, 2), Rational(3, 2), 2),
        ),
        (
            "BP central charge uses the FKR convention",
            simplify(
                bp.central_charge + (2 * k + 3) * (3 * k + 1) / (k + 3)
            ) == 0,
        ),
        ("BP formal reflected central sum is 50", simplify(bp.formal_central_sum - 50) == 0),
        ("BP n_plus dimension is 3", bp_ds.ghost_dim == 3),
        ("BP g_half dimension is 2", bp_ds.neutral_half_dimension == 2),
        ("BP positive subalgebra is nonabelian", bp_ds.positive_subalgebra_is_abelian is False),
        ("BP ghost constant is 2", bp_ds.ghost_constant_value == 2),
        ("sl4 hook partitions transpose", transpose_partition((2, 1, 1)) == (3, 1)),
        ("sl4 minimal generators are even", hook_min.w_num_even == 9 and hook_min.w_num_odd == 0),
        ("sl4 subregular generators are even", hook_sub.w_num_even == 5 and hook_sub.w_num_odd == 0),
        ("BP formal fixed level is -3", bp_duality.formal_fixed_level == -3),
        ("sl4 formal reflected level is -k-8", simplify(hook_duality.dual_level + k + 8) == 0),
    )
    claims = (
        bar_complex_n2_sca(k).higher_bar_cohomology,
        bar_complex_n2_sca(k).pbw_collapse,
        bp_ds.ds_bar_commutation,
        bp_ds.koszulness,
        bp_duality.categorical_transport,
        bp_duality.koszul_duality,
        hook_min.ds_bar_commutation,
        hook_sub.ds_bar_commutation,
        hook_duality.bar_compatibility,
        hook_duality.koszul_duality,
    )
    return DSBarAudit(exact_checks=exact_checks, claims=claims)


__all__ = [
    "ClaimPacket",
    "ClaimStatus",
    "OpenInvariantError",
    "N2SCAData",
    "BershadskyPolyakovData",
    "BarComplexData",
    "DSBarCommutationData",
    "KoszulDualIdentification",
    "DSBarAudit",
    "bershadsky_polyakov_data",
    "n2_sca_data",
    "bar_complex_n2_sca",
    "dim_sl_n",
    "affine_kappa_sl_n",
    "affine_central_charge_sl_n",
    "ds_good_grading_data",
    "ds_nilpotent_plus_dim",
    "ds_nilpotent_half_dim",
    "ds_bar_commutation_check",
    "sl3_minimal_data",
    "sl4_hook_ds_bar_data",
    "koszul_dual_identification",
    "verify_ds_bar_commutation",
]
