r"""Arithmetic and chain-map scope for Drinfeld--Sokolov reduction.

This module computes three kinds of data.

* The root decomposition of :math:`\mathfrak{sl}_N`.
* The principal :math:`\mathfrak{sl}_2` DS central charge and the two
  scalar :math:`\kappa` formulae used by the census.
* The nilpotent-orbit arithmetic attached to a partition of :math:`N`.

A map on chiral Hochschild cohomology requires a cochain map between the
source derivation complex and the DS BRST complex, followed by passage to
the reduced algebra.  The present engine records this construction as an
open obligation.  Accordingly, BRST, Cartan, and screening images carry
``None`` until explicit cochains and homotopies are supplied.

The mode convention is load-bearing.  If ``omega`` is the conformal
vector, then

    omega_(0) = L_(-1),       omega_(1) = L_0,

and

    [L_0, Y(a,z)] = Y(L_0 a,z) + z d_z Y(a,z).

Thus the conformal vector supplies the translation zero mode.  A proposed
Cartan-to-``L_0`` comparison must also account for the coordinate Euler
term.  Screening operators belong naturally to a chosen free-field
extension; an inner representative in the reduced W-algebra is further
data.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Optional, Tuple


DIM_SL2 = 3
RANK_SL2 = 1
NUM_POS_ROOTS_SL2 = 1
NUM_NEG_ROOTS_SL2 = 1


@dataclass(frozen=True)
class DSChainMapObligation:
    """A candidate DS image together with the data that would define it."""

    sector: str
    candidate_source: str
    multiplicity: int
    natural_ambient: str
    required_data: Tuple[str, ...]
    induced_chain_map: Optional[str] = None
    target_cocycle: Optional[str] = None
    null_homotopy: Optional[str] = None
    inner_witness: Optional[str] = None
    epistemic_status: str = "open_chain_map_obligation"


@dataclass(frozen=True)
class NilpotentOrbitArithmetic:
    """Type-A nilpotent-orbit invariants determined by a partition."""

    N: int
    partition: Tuple[int, ...]
    transpose_partition: Tuple[int, ...]
    block_multiplicities: Tuple[Tuple[int, int], ...]
    dim_sl_n: int
    dim_nilpotent_centralizer_sl_n: int
    dim_orbit: int
    half_orbit_dimension: int
    dim_reductive_triple_centralizer_sl_n: int
    dim_center_reductive_triple_centralizer: int


def sl_n_data(N: int) -> Dict[str, int]:
    r"""Return the root-space dimensions of :math:`\mathfrak{sl}_N`.

    The decomposition

    .. math::

       \mathfrak{sl}_N=\mathfrak n_-\oplus\mathfrak h\oplus\mathfrak n_+

    has dimensions ``N(N-1)/2``, ``N-1``, and ``N(N-1)/2``.
    """

    if not isinstance(N, int) or isinstance(N, bool) or N < 2:
        raise ValueError(f"N must be an integer at least 2, got {N!r}")
    rank = N - 1
    positive_roots = N * (N - 1) // 2
    dimension = N * N - 1
    return {
        "N": N,
        "dim": dimension,
        "rank": rank,
        "pos_roots": positive_roots,
        "neg_roots": positive_roots,
    }


def virasoro_mode_convention() -> Dict[str, Optional[str]]:
    r"""Return the two conformal-vector modes relevant to the Cartan lane."""

    return {
        "conformal_vector_zero_mode": "omega_(0) = L_(-1)",
        "conformal_vector_grading_mode": "omega_(1) = L_0",
        "grading_commutator": (
            "[L_0, Y(a,z)] = Y(L_0 a,z) + z d_z Y(a,z)"
        ),
        "cartan_to_target_chain_map": None,
        "inner_witness_for_l0": None,
    }


def principal_ds_obligations_sl2() -> Tuple[DSChainMapObligation, ...]:
    r"""Return the three candidate zero-mode directions for principal DS.

    Their :math:`h`-weights ``2, 0, -2`` are elementary
    :math:`\mathfrak{sl}_2` arithmetic.  Their DS images require the
    cochain data listed in ``required_data``.
    """

    return (
        DSChainMapObligation(
            sector="positive_root_h_weight_2",
            candidate_source="the e zero-mode direction",
            multiplicity=1,
            natural_ambient="DS BRST complex C_DS(V_k(sl_2))",
            required_data=(
                "a degree-zero cochain Delta_e on the DS BRST complex",
                "the identity [Q_DS, Delta_e] = 0",
                "a degree-minus-one H_e with [Q_DS, H_e] = Delta_e",
            ),
        ),
        DSChainMapObligation(
            sector="cartan_h_weight_0",
            candidate_source="the h zero-mode direction",
            multiplicity=1,
            natural_ambient="DS BRST complex and the Virasoro derivation complex",
            required_data=(
                "a Q_DS-closed lift of the Cartan action",
                "a target derivation cocycle on Vir_c",
                "a comparison accounting for the z d_z term in the L_0 commutator",
                "an element a in Vir_c with a_(0) equal to the target cocycle, if inner",
            ),
        ),
        DSChainMapObligation(
            sector="negative_root_h_weight_minus_2",
            candidate_source="the f zero-mode direction",
            multiplicity=1,
            natural_ambient="a chosen Wakimoto or free-field extension containing Vir_c",
            required_data=(
                "a specified free-field extension and Vir_c embedding",
                "a screening operator on that extension",
                "a cochain map from the source derivation complex to the DS complex",
                "an element of Vir_c realizing the target zero mode, if inner",
            ),
        ),
    )


def principal_ds_obligations_sl_n(N: int) -> Tuple[DSChainMapObligation, ...]:
    r"""Return the three root sectors and their open DS image obligations."""

    data = sl_n_data(N)
    return (
        DSChainMapObligation(
            sector="positive_roots",
            candidate_source="positive-root zero-mode directions",
            multiplicity=data["pos_roots"],
            natural_ambient=f"principal DS BRST complex C_DS(V_k(sl_{N}))",
            required_data=(
                "Q_DS-closed derivation cochains for the positive-root directions",
                "degree-minus-one BRST homotopies for the proposed exact images",
            ),
        ),
        DSChainMapObligation(
            sector="cartan",
            candidate_source="Cartan zero-mode directions",
            multiplicity=data["rank"],
            natural_ambient=f"DS BRST complex and derivations of W_k(sl_{N})",
            required_data=(
                "Q_DS-compatible Cartan lifts",
                "target derivation cocycles on the principal W-algebra",
                "zero-mode inner witnesses inside the W-algebra, when applicable",
            ),
        ),
        DSChainMapObligation(
            sector="negative_roots",
            candidate_source="negative-root zero-mode directions",
            multiplicity=data["neg_roots"],
            natural_ambient="a specified Miura or Wakimoto free-field extension",
            required_data=(
                "screening operators on the chosen extension",
                "descent of the source derivation cochains through DS reduction",
                "zero-mode inner witnesses inside the W-algebra, when applicable",
            ),
        ),
    )


def principal_ds_scope_report(N: int) -> Dict[str, object]:
    r"""Separate proved root arithmetic from the open cohomological map."""

    root_data = sl_n_data(N)
    obligations = principal_ds_obligations_sl_n(N)
    sector_total = sum(item.multiplicity for item in obligations)
    return {
        "N": N,
        "epistemic_status": "root_arithmetic_proved_chain_map_open",
        "root_data": root_data,
        "root_decomposition_total": sector_total,
        "root_decomposition_identity": sector_total == root_data["dim"],
        "obligations": obligations,
        "source_chirhoch1_dimension": None,
        "target_chirhoch1_dimension": None,
        "induced_chirhoch1_map": None,
        "brst_image": None,
        "cartan_image": None,
        "screening_image": None,
    }


def c_ds_sl2(k: Fraction) -> Fraction:
    r"""Central charge of principal DS reduction of :math:`V_k(sl_2)`.

    .. math:: c(k)=1-6(k+1)^2/(k+2)=13-6((k+2)+(k+2)^{-1}).
    """

    k = Fraction(k)
    if k == -2:
        raise ValueError("The principal sl_2 formula has a pole at k = -2")
    return Fraction(1) - Fraction(6) * (k + 1) ** 2 / (k + 2)


def kappa_km_sl2(k: Fraction) -> Fraction:
    r"""Return :math:`\kappa(V_k(sl_2))=3(k+2)/4`."""

    return Fraction(3) * (Fraction(k) + 2) / 4


def kappa_vir(c: Fraction) -> Fraction:
    r"""Return :math:`\kappa(\mathrm{Vir}_c)=c/2`."""

    return Fraction(c) / 2


def ds_scalar_data_sl2(k: Fraction) -> Dict[str, Fraction]:
    r"""Evaluate the proved scalar formulas at one noncritical level."""

    k = Fraction(k)
    c = c_ds_sl2(k)
    return {
        "k": k,
        "c": c,
        "kappa_km": kappa_km_sl2(k),
        "kappa_vir": kappa_vir(c),
    }


def ft4_scope_report() -> Dict[str, object]:
    r"""Return the mathematical scope of the proposed FT-4 comparison.

    The report proves the :math:`\mathfrak{sl}_2` root count and evaluates
    the scalar formulas at regular levels.  Its cohomological outcome is
    ``None`` until the three chain-map obligations are constructed.
    """

    levels = tuple(Fraction(k) for k in (1, 2, 3, 5, 10, -3))
    return {
        "epistemic_status": "arithmetic_proved_chain_map_open",
        "root_arithmetic": sl_n_data(2),
        "mode_convention": virasoro_mode_convention(),
        "obligations": principal_ds_obligations_sl2(),
        "scalar_data": {k: ds_scalar_data_sl2(k) for k in levels},
        "chirhoch_source": None,
        "chirhoch_target": None,
        "induced_map": None,
        "ft4_outcome": None,
    }


def _validate_partition(N: int, partition: Tuple[int, ...]) -> None:
    sl_n_data(N)
    if not partition:
        raise ValueError("partition must contain at least one positive part")
    if any(not isinstance(part, int) or isinstance(part, bool) or part <= 0 for part in partition):
        raise ValueError(f"partition parts must be positive integers, got {partition!r}")
    if tuple(sorted(partition, reverse=True)) != partition:
        raise ValueError(f"partition must be weakly decreasing, got {partition!r}")
    if sum(partition) != N:
        raise ValueError(f"partition {partition!r} must sum to N={N}")


def transpose_partition(partition: Tuple[int, ...]) -> Tuple[int, ...]:
    r"""Return the conjugate Young partition."""

    if not partition:
        raise ValueError("partition must contain at least one positive part")
    if any(not isinstance(part, int) or isinstance(part, bool) or part <= 0 for part in partition):
        raise ValueError(f"partition parts must be positive integers, got {partition!r}")
    if tuple(sorted(partition, reverse=True)) != partition:
        raise ValueError(f"partition must be weakly decreasing, got {partition!r}")
    return tuple(
        sum(part >= column for part in partition)
        for column in range(1, partition[0] + 1)
    )


def nilpotent_orbit_arithmetic_sl_n(
    N: int, partition: Tuple[int, ...]
) -> NilpotentOrbitArithmetic:
    r"""Compute exact type-A orbit and triple-centralizer dimensions.

    For Jordan type :math:`\lambda` with transpose :math:`\lambda'`,

    .. math::

       \dim Z_{\mathfrak{sl}_N}(f)=\sum_j(\lambda'_j)^2-1,
       \qquad
       \dim\mathcal O_\lambda=N^2-\sum_j(\lambda'_j)^2.

    If ``m_d`` is the multiplicity of a block of size ``d``, the
    reductive centralizer of the associated :math:`\mathfrak{sl}_2`
    triple has dimension ``sum_d m_d^2 - 1`` in
    :math:`\mathfrak{sl}_N`, and its center has dimension one less than
    the number of distinct block sizes.
    """

    partition = tuple(partition)
    _validate_partition(N, partition)
    transpose = transpose_partition(partition)
    multiplicities = tuple(sorted(Counter(partition).items(), reverse=True))
    centralizer_gl = sum(column * column for column in transpose)
    centralizer_sl = centralizer_gl - 1
    dim_g = N * N - 1
    orbit_dimension = dim_g - centralizer_sl
    if orbit_dimension % 2:
        raise ArithmeticError(
            f"nilpotent orbit dimension must be even, got {orbit_dimension}"
        )
    reductive_dimension = (
        sum(multiplicity * multiplicity for _, multiplicity in multiplicities) - 1
    )
    reductive_center_dimension = len(multiplicities) - 1
    return NilpotentOrbitArithmetic(
        N=N,
        partition=partition,
        transpose_partition=transpose,
        block_multiplicities=multiplicities,
        dim_sl_n=dim_g,
        dim_nilpotent_centralizer_sl_n=centralizer_sl,
        dim_orbit=orbit_dimension,
        half_orbit_dimension=orbit_dimension // 2,
        dim_reductive_triple_centralizer_sl_n=reductive_dimension,
        dim_center_reductive_triple_centralizer=reductive_center_dimension,
    )


def nonprincipal_ds_scope_report(
    N: int, partition: Tuple[int, ...]
) -> Dict[str, object]:
    r"""Return nilpotent-orbit arithmetic and the open DS comparison data."""

    arithmetic = nilpotent_orbit_arithmetic_sl_n(N, partition)
    return {
        "epistemic_status": "orbit_arithmetic_proved_chain_map_open",
        "arithmetic": arithmetic,
        "source_chirhoch1_dimension": None,
        "target_chirhoch1_dimension": None,
        "induced_chirhoch1_map": None,
        "conditional_target_formula": None,
        "required_data": (
            "the DS BRST derivation complex for the chosen good grading",
            "a cochain map from affine derivations to BRST derivations",
            "target cocycle representatives in ChirHoch of the reduced W-algebra",
            "homotopies or inner zero-mode witnesses for every claimed vanishing",
        ),
    }
