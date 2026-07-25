r"""Exact BCD root arithmetic with typed principal-W comparison claims.

The scalar lane records the dimensions, dual Coxeter numbers, exponents,
principal generator weights, Weyl-vector norms, and nilpotent-partition
combinatorics of the classical root systems.  The principal-W lane records
central charge, the genus-one anomaly ratio, modular characteristic,
reflected level, modular conductor, full shadow, and Koszul duality as
``ClaimPacket`` objects imported from the canonical Creutzig landscape
engine.  Each unresolved packet names the comparison theorem required to
promote root arithmetic to a modular or chiral statement.

The distinction is forced by the accidental isomorphism ``D_3=A_3``.  The
rank-minus-pole expression formerly used for the BCD central charge differs
from the Kac--Roan--Wakimoto type-A value by ``60*k+120``.  Thus the exact
root isomorphism survives, while its principal-W central-charge realization
remains open until the complete non-simply-laced KRW convention is supplied.

The exact root-system normalization has long roots of squared length two:

``B_n``: ``||rho||^2 = n(2n-1)(2n+1)/12``;
``C_n``: ``||rho||^2 = n(n+1)(2n+1)/12``;
``D_n``: ``||rho||^2 = n(n-1)(2n-1)/6``.

Manuscript anchors: ``conj:w-orbit-duality`` and
``thm:w-algebra-koszul-main`` in ``chapters/examples/w_algebras.tex``.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.non_principal_w_bar_engine import ClaimPacket, ClaimStatus
from compute.lib.theorem_creutzig_w_landscape_engine import (
    building_block_bcd_data,
    d3_a3_incomplete_ansatz_discrepancy,
    minimal_w_so_data,
)


k_sym = Symbol('k')


# =====================================================================
# 1.  Lie algebra data (with verified ||rho||^2)
# =====================================================================

def _lie_data(lie_type: str, rank: int) -> Dict[str, Any]:
    """Lie algebra data for types B, C, D.

    Returns rank, dimension, dual Coxeter number, exponents,
    generator weights (exponents + 1), and ||rho||^2 in the
    long-root-normalized invariant form.
    """
    if lie_type == 'B':
        if rank < 2:
            raise ValueError(f"B_n requires n >= 2, got {rank}")
        n = rank
        N = 2 * n + 1
        return {
            'type': f'B_{n}',
            'lie_algebra': f'so_{N}',
            'rank': n,
            'dim': n * (2 * n + 1),
            'h_dual': 2 * n - 1,
            'exponents': tuple(2 * i + 1 for i in range(n)),
            'generator_weights': tuple(2 * (i + 1) for i in range(n)),
            # rho = ((2n-1)/2, ..., 1/2), (e_i, e_j) = delta_{ij}
            'rho_squared': Rational(n * (2 * n - 1) * (2 * n + 1), 12),
        }
    elif lie_type == 'C':
        if rank < 2:
            raise ValueError(f"C_n requires n >= 2, got {rank}")
        n = rank
        return {
            'type': f'C_{n}',
            'lie_algebra': f'sp_{2 * n}',
            'rank': n,
            'dim': n * (2 * n + 1),
            'h_dual': n + 1,
            'exponents': tuple(2 * i + 1 for i in range(n)),
            'generator_weights': tuple(2 * (i + 1) for i in range(n)),
            # rho = (n, n-1, ..., 1), but (e_i,e_j) = delta_{ij}/2
            # since long roots 2e_i have ||2e_i||^2 = 2.
            'rho_squared': Rational(n * (n + 1) * (2 * n + 1), 12),
        }
    elif lie_type == 'D':
        if rank < 3:
            raise ValueError(f"D_n requires n >= 3, got {rank}")
        n = rank
        N = 2 * n
        exps = list(2 * i + 1 for i in range(n - 1))
        exps.append(n - 1)
        exps.sort()
        return {
            'type': f'D_{n}',
            'lie_algebra': f'so_{N}',
            'rank': n,
            'dim': n * (2 * n - 1),
            'h_dual': 2 * n - 2,
            'exponents': tuple(exps),
            'generator_weights': tuple(e + 1 for e in exps),
            # rho = (n-1, n-2, ..., 1, 0), (e_i,e_j) = delta_{ij}
            'rho_squared': Rational(n * (n - 1) * (2 * n - 1), 6),
        }
    else:
        raise ValueError(f"Unsupported type: {lie_type}")


def _langlands_dual_type(lie_type: str) -> str:
    """Langlands dual: B_n^L = C_n, C_n^L = B_n, D_n^L = D_n."""
    if lie_type == 'B':
        return 'C'
    elif lie_type == 'C':
        return 'B'
    elif lie_type == 'D':
        return 'D'
    raise ValueError(f"Unsupported: {lie_type}")


def _open_claim(
    statement: str,
    *hypotheses: str,
    evidence: Tuple[str, ...] = (),
) -> ClaimPacket:
    """Return an unresolved comparison with its exact obligations."""

    return ClaimPacket(
        statement=statement,
        status=ClaimStatus.OPEN,
        value=None,
        evidence=evidence,
        hypotheses=tuple(dict.fromkeys(hypotheses)),
    )


def _conditional_claim(
    statement: str,
    *hypotheses: str,
    evidence: Tuple[str, ...] = (),
) -> ClaimPacket:
    """Return a conditional consequence of named comparison data."""

    return ClaimPacket(
        statement=statement,
        status=ClaimStatus.CONDITIONAL,
        value=None,
        evidence=evidence,
        hypotheses=tuple(dict.fromkeys(hypotheses)),
    )


# =====================================================================
# 2.  Principal W-algebra invariants
# =====================================================================

def reciprocal_weight_diagnostic(lie_type: str, rank: int) -> Rational:
    """Return the exact reciprocal sum of principal generator weights."""

    data = _lie_data(lie_type, rank)
    return sum(Rational(1, weight) for weight in data['generator_weights'])


def anomaly_ratio(lie_type: str, rank: int) -> ClaimPacket:
    """Return the open genus-one realization of the weight diagnostic."""

    return building_block_bcd_data(lie_type, rank).anomaly_ratio


def central_charge(lie_type: str, rank: int, level=k_sym) -> ClaimPacket:
    """Return the canonical open principal-W central-charge packet."""

    return building_block_bcd_data(lie_type, rank, level).central_charge


def kappa(lie_type: str, rank: int, level=k_sym) -> ClaimPacket:
    """Return the conditional principal-W modular characteristic."""

    return building_block_bcd_data(lie_type, rank, level).kappa


def ff_dual_level(lie_type: str, rank: int, level=k_sym) -> ClaimPacket:
    """Return the open fixed-convention Langlands-dual level relation."""

    return building_block_bcd_data(lie_type, rank, level).langlands_dual_level


# =====================================================================
# 3.  Kappa complementarity
# =====================================================================

@dataclass(frozen=True)
class KappaComplementarityData:
    """Typed modular-conductor data for a principal BCD W-algebra."""

    lie_type: str
    rank: int
    kappa_k: ClaimPacket
    kappa_kprime: ClaimPacket
    kappa_sum: ClaimPacket
    kappa_sum_is_constant: ClaimPacket
    anomaly_ratio: ClaimPacket
    rho_squared: Rational
    h_dual: int


def kappa_complementarity(lie_type: str, rank: int, level=k_sym) -> KappaComplementarityData:
    """Return the open modular conductor without symbolic packet arithmetic."""

    data = _lie_data(lie_type, rank)
    canonical = building_block_bcd_data(lie_type, rank, level)
    dual_type = _langlands_dual_type(lie_type)
    dual = building_block_bcd_data(dual_type, rank, level)
    dual_kappa = _conditional_claim(
        f"kappa of principal {dual.lie_type} at the dual level of {canonical.lie_type}",
        *dual.kappa.hypotheses,
        *canonical.langlands_dual_level.hypotheses,
        evidence=(
            f"exact Langlands-dual root type {canonical.lie_type}^L={dual.lie_type}",
        ),
    )
    level_independence = _open_claim(
        f"level-independence of K^kappa for principal {canonical.lie_type}",
        *canonical.modular_conductor.hypotheses,
        "a proof that the represented trace sum is constant in the dual-level parameter",
        evidence=(
            f"exact generator diagnostic {reciprocal_weight_diagnostic(lie_type, rank)}",
        ),
    )

    return KappaComplementarityData(
        lie_type=data['type'],
        rank=rank,
        kappa_k=canonical.kappa,
        kappa_kprime=dual_kappa,
        kappa_sum=canonical.modular_conductor,
        kappa_sum_is_constant=level_independence,
        anomaly_ratio=canonical.anomaly_ratio,
        rho_squared=data['rho_squared'],
        h_dual=data['h_dual'],
    )


# =====================================================================
# 4.  Accidental isomorphism verification
# =====================================================================

@dataclass(frozen=True)
class IsomorphismCheckData:
    """Exact root oracle and typed modular comparisons for an isomorphism."""

    type_1: str
    rank_1: int
    type_2: str
    rank_2: int
    dim_1: int
    dim_2: int
    h_dual_1: int
    h_dual_2: int
    exponents_1: Tuple[int, ...]
    exponents_2: Tuple[int, ...]
    generator_weights_1: Tuple[int, ...]
    generator_weights_2: Tuple[int, ...]
    rho_squared_1: Rational
    rho_squared_2: Rational
    root_data_match: bool
    c_match: ClaimPacket
    kappa_match: ClaimPacket
    rho_match: ClaimPacket
    incomplete_central_ansatz_discrepancy: object


def check_b2_c2_isomorphism(level=k_sym) -> IsomorphismCheckData:
    """Return the exact ``B_2=C_2`` root oracle and modular obligations."""

    b = _lie_data('B', 2)
    c = _lie_data('C', 2)
    b_claims = building_block_bcd_data('B', 2, level)
    c_claims = building_block_bcd_data('C', 2, level)
    evidence = (
        "B_2 and C_2 have dimension 10, h^vee=3, exponents (1,3), "
        "generator weights (2,4), and ||rho||^2=5/2",
    )

    return IsomorphismCheckData(
        type_1='B_2', rank_1=2,
        type_2='C_2', rank_2=2,
        dim_1=b['dim'], dim_2=c['dim'],
        h_dual_1=b['h_dual'], h_dual_2=c['h_dual'],
        exponents_1=b['exponents'], exponents_2=c['exponents'],
        generator_weights_1=b['generator_weights'],
        generator_weights_2=c['generator_weights'],
        rho_squared_1=b['rho_squared'], rho_squared_2=c['rho_squared'],
        root_data_match=all(
            b[key] == c[key]
            for key in ('dim', 'h_dual', 'exponents', 'generator_weights', 'rho_squared')
        ),
        c_match=_open_claim(
            "principal-W central charges agree under B_2=C_2",
            *b_claims.central_charge.hypotheses,
            *c_claims.central_charge.hypotheses,
            "a fixed-convention identification of the two DS reductions",
            evidence=evidence,
        ),
        kappa_match=_conditional_claim(
            "principal-W modular characteristics agree under B_2=C_2",
            *b_claims.kappa.hypotheses,
            *c_claims.kappa.hypotheses,
            "the central-charge and genus-one trace identifications under B_2=C_2",
            evidence=evidence,
        ),
        rho_match=_open_claim(
            "principal-W anomaly ratios agree under B_2=C_2",
            *b_claims.anomaly_ratio.hypotheses,
            *c_claims.anomaly_ratio.hypotheses,
            evidence=(
                *evidence,
                "both reciprocal-weight diagnostics equal 3/4",
            ),
        ),
        incomplete_central_ansatz_discrepancy=None,
    )


def check_d3_a3_isomorphism(level=k_sym) -> IsomorphismCheckData:
    """Return the exact ``D_3=A_3`` root oracle and the failed-ansatz gap."""

    d = _lie_data('D', 3)
    a = {
        'dim': 15,
        'h_dual': 4,
        'exponents': (1, 2, 3),
        'generator_weights': (2, 3, 4),
        'rho_squared': Rational(5),
    }
    d_claims = building_block_bcd_data('D', 3, level)
    discrepancy = d3_a3_incomplete_ansatz_discrepancy(level)
    evidence = (
        "D_3 and A_3 have dimension 15, h^vee=4, exponents (1,2,3), "
        "generator weights (2,3,4), and ||rho||^2=5",
        f"the incomplete rank-minus-pole central ansatz has discrepancy {discrepancy}",
    )

    return IsomorphismCheckData(
        type_1='D_3', rank_1=3,
        type_2='A_3', rank_2=3,
        dim_1=d['dim'], dim_2=a['dim'],
        h_dual_1=d['h_dual'], h_dual_2=a['h_dual'],
        exponents_1=d['exponents'], exponents_2=a['exponents'],
        generator_weights_1=d['generator_weights'],
        generator_weights_2=a['generator_weights'],
        rho_squared_1=d['rho_squared'], rho_squared_2=a['rho_squared'],
        root_data_match=all(
            d[key] == a[key]
            for key in ('dim', 'h_dual', 'exponents', 'generator_weights', 'rho_squared')
        ),
        c_match=_open_claim(
            "principal-W central charges agree under D_3=A_3",
            *d_claims.central_charge.hypotheses,
            "the complete KRW formula in the D_3 convention and its transport through D_3=A_3",
            evidence=evidence,
        ),
        kappa_match=_conditional_claim(
            "principal-W modular characteristics agree under D_3=A_3",
            *d_claims.kappa.hypotheses,
            "the central-charge and genus-one trace identifications under D_3=A_3",
            evidence=evidence,
        ),
        rho_match=_open_claim(
            "principal-W anomaly ratios agree under D_3=A_3",
            *d_claims.anomaly_ratio.hypotheses,
            evidence=(
                *evidence,
                "both reciprocal-weight diagnostics equal 13/12",
            ),
        ),
        incomplete_central_ansatz_discrepancy=discrepancy,
    )


# =====================================================================
# 5.  Langlands duality data
# =====================================================================

@dataclass(frozen=True)
class LanglandsDualityData:
    """Exact root comparison and typed claims for ``(g,g^L)``."""

    type_g: str
    rank: int
    type_gL: str
    # g data
    h_dual_g: int
    dim_g: int
    rho_sq_g: Rational
    rho_g: ClaimPacket
    c_g: ClaimPacket
    kappa_g: ClaimPacket
    # g^L data
    h_dual_gL: int
    dim_gL: int
    rho_sq_gL: Rational
    rho_gL: ClaimPacket
    c_gL: ClaimPacket
    kappa_gL: ClaimPacket
    # Comparisons
    same_exponents: bool
    same_anomaly_ratio: ClaimPacket
    same_central_charge: ClaimPacket
    kappa_sum_g: ClaimPacket
    kappa_sum_gL: ClaimPacket
    same_kappa_sum: ClaimPacket


def langlands_duality_data(lie_type: str, rank: int, level=k_sym) -> LanglandsDualityData:
    """Return exact Langlands root data and unresolved modular comparisons."""

    dual_type = _langlands_dual_type(lie_type)
    data_g = _lie_data(lie_type, rank)
    data_gL = _lie_data(dual_type, rank)
    claims_g = building_block_bcd_data(lie_type, rank, level)
    claims_gL = building_block_bcd_data(dual_type, rank, level)
    same_exponents = data_g['exponents'] == data_gL['exponents']
    root_evidence = (
        f"exact exponent ledgers {data_g['type']}:{data_g['exponents']} and "
        f"{data_gL['type']}:{data_gL['exponents']}",
        f"exact reciprocal-weight diagnostics "
        f"{reciprocal_weight_diagnostic(lie_type, rank)} and "
        f"{reciprocal_weight_diagnostic(dual_type, rank)}",
    )

    return LanglandsDualityData(
        type_g=data_g['type'],
        rank=rank,
        type_gL=data_gL['type'],
        h_dual_g=data_g['h_dual'],
        dim_g=data_g['dim'],
        rho_sq_g=data_g['rho_squared'],
        rho_g=claims_g.anomaly_ratio,
        c_g=claims_g.central_charge,
        kappa_g=claims_g.kappa,
        h_dual_gL=data_gL['h_dual'],
        dim_gL=data_gL['dim'],
        rho_sq_gL=data_gL['rho_squared'],
        rho_gL=claims_gL.anomaly_ratio,
        c_gL=claims_gL.central_charge,
        kappa_gL=claims_gL.kappa,
        same_exponents=same_exponents,
        same_anomaly_ratio=_open_claim(
            f"rho agrees for the Langlands pair {data_g['type']},{data_gL['type']}",
            *claims_g.anomaly_ratio.hypotheses,
            *claims_gL.anomaly_ratio.hypotheses,
            evidence=root_evidence,
        ),
        same_central_charge=_open_claim(
            f"principal central charges compare for {data_g['type']},{data_gL['type']}",
            *claims_g.central_charge.hypotheses,
            *claims_gL.central_charge.hypotheses,
            "a common invariant-form and DS-reduction convention",
            evidence=root_evidence,
        ),
        kappa_sum_g=claims_g.modular_conductor,
        kappa_sum_gL=claims_gL.modular_conductor,
        same_kappa_sum=_open_claim(
            f"modular conductors agree for {data_g['type']},{data_gL['type']}",
            *claims_g.modular_conductor.hypotheses,
            *claims_gL.modular_conductor.hypotheses,
            evidence=root_evidence,
        ),
    )


# =====================================================================
# 6.  Nilpotent orbit combinatorics for BCD types
# =====================================================================

def _is_valid_bcd_partition(lie_type: str, partition: Tuple[int, ...]) -> bool:
    """Check if a partition parameterizes a nilpotent orbit.

    Type B_n (so_{2n+1}): partition of 2n+1, even parts have even multiplicity.
    Type C_n (sp_{2n}):   partition of 2n, odd parts have even multiplicity.
    Type D_n (so_{2n}):   partition of 2n, even parts have even multiplicity.
    """
    parts = tuple(sorted(partition, reverse=True))
    n_total = sum(parts)

    # Count multiplicities
    mult = Counter(parts)

    if lie_type == 'B':
        # Even parts must have even multiplicity
        return all(mult[p] % 2 == 0 for p in mult if p % 2 == 0)
    elif lie_type == 'C':
        # Odd parts must have even multiplicity
        return all(mult[p] % 2 == 0 for p in mult if p % 2 == 1)
    elif lie_type == 'D':
        # Even parts must have even multiplicity
        return all(mult[p] % 2 == 0 for p in mult if p % 2 == 0)
    return False


def bcd_nilpotent_partitions(lie_type: str, rank: int) -> List[Tuple[int, ...]]:
    """Return the admissible partition labels for the given classical type.

    The labels occur in decreasing dominance order.  In type ``D``, a
    very-even label represents the familiar pair of nilpotent orbits; this
    routine enumerates partition labels and therefore records that label
    once.
    """
    if lie_type == 'B':
        N = 2 * rank + 1
    elif lie_type == 'C':
        N = 2 * rank
    elif lie_type == 'D':
        N = 2 * rank
    else:
        raise ValueError(f"Unsupported: {lie_type}")

    # Generate all partitions of N
    def _partitions(n, max_part=None):
        if max_part is None:
            max_part = n
        if n == 0:
            yield ()
            return
        for first in range(min(n, max_part), 0, -1):
            for rest in _partitions(n - first, first):
                yield (first,) + rest

    result = []
    for p in _partitions(N):
        if _is_valid_bcd_partition(lie_type, p):
            result.append(p)
    return result


def _transpose_partition(partition: Tuple[int, ...]) -> Tuple[int, ...]:
    """Transpose (conjugate) a partition."""
    parts = tuple(sorted(partition, reverse=True))
    if not parts:
        return ()
    cols = []
    for i in range(parts[0]):
        cols.append(sum(1 for p in parts if p > i))
    return tuple(cols)


def _transpose_parity_repair_candidate(
    partition: Tuple[int, ...], target_type: str
) -> Tuple[int, ...]:
    """Return the deterministic transpose-lane parity-repair candidate.

    This exact combinatorial routine decreases a parity-violating part until
    the target parity condition holds.  It can change the size of the
    partition.  Consequently it is an audit candidate, rather than the
    Barbasch--Vogan ``B/C/D`` collapse: the latter requires the source-backed
    size-changing ``+/-`` operation and the genuine dominance-maximal
    collapse convention.
    """
    result = list(sorted(partition, reverse=True))
    max_iterations = 2 * sum(result) + 10  # safety bound

    for _ in range(max_iterations):
        result = [x for x in result if x > 0]
        if not result:
            break
        result.sort(reverse=True)
        mult = Counter(result)

        violation_found = False
        if target_type in ('B', 'D'):
            # Even parts must have even multiplicity
            for p in sorted(mult.keys(), reverse=True):
                if p > 0 and p % 2 == 0 and mult[p] % 2 == 1:
                    # Decrease LAST occurrence of p by 1
                    for i in range(len(result) - 1, -1, -1):
                        if result[i] == p:
                            result[i] -= 1
                            break
                    violation_found = True
                    break
        elif target_type == 'C':
            # Odd parts must have even multiplicity
            for p in sorted(mult.keys(), reverse=True):
                if p > 0 and p % 2 == 1 and mult[p] % 2 == 1:
                    for i in range(len(result) - 1, -1, -1):
                        if result[i] == p:
                            result[i] -= 1
                            break
                    violation_found = True
                    break

        if not violation_found:
            break

    result = [x for x in result if x > 0]
    result.sort(reverse=True)
    return tuple(result) if result else (0,)


def bv_dual_partition(
    lie_type: str, rank: int, partition: Tuple[int, ...]
) -> ClaimPacket:
    """Return the open Barbasch--Vogan orbit-identification claim.

    Transposition and the local parity repair are computed as evidence.
    They do not identify the dual orbit: a valid target label has the
    target algebra's natural partition size, and the classical ``B/C/D``
    formulas insert type-dependent ``+/-`` operations before the genuine
    collapse.  A source-backed convention is therefore a proof obligation.
    """
    parts = tuple(sorted(partition, reverse=True))
    if lie_type == 'B':
        source_size = 2 * rank + 1
        target_size = 2 * rank
    elif lie_type == 'C':
        source_size = 2 * rank
        target_size = 2 * rank + 1
    elif lie_type == 'D':
        source_size = target_size = 2 * rank
    else:
        raise ValueError(f"Unsupported: {lie_type}")
    if sum(parts) != source_size:
        raise ValueError(f"Partition {parts} does not sum to {source_size}")
    if not _is_valid_bcd_partition(lie_type, parts):
        raise ValueError(f"Partition {parts} violates the type-{lie_type} parity condition")

    tr = _transpose_partition(parts)
    dual_type = _langlands_dual_type(lie_type)
    candidate = _transpose_parity_repair_candidate(tr, dual_type)
    return _open_claim(
        f"Barbasch--Vogan dual of the type-{lie_type}_{rank} orbit {parts}",
        "a source-backed type-dependent +/- operation",
        "the dominance-maximal B/C/D collapse in a fixed partition convention",
        "resolution of very-even type-D orbit labels when applicable",
        evidence=(
            f"transpose {tr}",
            f"parity-repair candidate {candidate}",
            f"target type {dual_type}_{rank} has partition size {target_size}",
        ),
    )


# =====================================================================
# 7.  Complete duality data for a BCD principal W-algebra
# =====================================================================

@dataclass(frozen=True)
class BCDPrincipalDualityData:
    """Exact root data and typed principal-W duality claims."""

    lie_type: str
    rank: int
    dim_g: int
    h_dual: int
    rho_squared: Rational
    exponents: Tuple[int, ...]
    generator_weights: Tuple[int, ...]
    reciprocal_weight_diagnostic: Rational
    anomaly_ratio: ClaimPacket
    central_charge: ClaimPacket
    kappa: ClaimPacket
    langlands_dual_level: ClaimPacket
    dual_central_charge: ClaimPacket
    dual_kappa: ClaimPacket
    central_charge_complementarity: ClaimPacket
    modular_conductor: ClaimPacket
    conductor_level_independence: ClaimPacket
    shadow_class: ClaimPacket
    shadow_depth: ClaimPacket
    langlands_dual_type: str
    koszul_status: ClaimPacket


def principal_duality_data(
    lie_type: str, rank: int, level=k_sym
) -> BCDPrincipalDualityData:
    """Return the canonical packets together with their exact root ledger."""

    data = _lie_data(lie_type, rank)
    canonical = building_block_bcd_data(lie_type, rank, level)
    dual_family = _langlands_dual_type(lie_type)
    dual = building_block_bcd_data(dual_family, rank, level)
    complementarity = kappa_complementarity(lie_type, rank, level)
    dual_central = _conditional_claim(
        f"principal central charge of {dual.lie_type} at the dual level of {canonical.lie_type}",
        *dual.central_charge.hypotheses,
        *canonical.langlands_dual_level.hypotheses,
        evidence=(
            f"exact Langlands-dual root type {canonical.lie_type}^L={dual.lie_type}",
        ),
    )

    return BCDPrincipalDualityData(
        lie_type=data['type'],
        rank=rank,
        dim_g=data['dim'],
        h_dual=data['h_dual'],
        rho_squared=data['rho_squared'],
        exponents=data['exponents'],
        generator_weights=data['generator_weights'],
        reciprocal_weight_diagnostic=reciprocal_weight_diagnostic(lie_type, rank),
        anomaly_ratio=canonical.anomaly_ratio,
        central_charge=canonical.central_charge,
        kappa=canonical.kappa,
        langlands_dual_level=canonical.langlands_dual_level,
        dual_central_charge=dual_central,
        dual_kappa=complementarity.kappa_kprime,
        central_charge_complementarity=canonical.c_complementarity,
        modular_conductor=canonical.modular_conductor,
        conductor_level_independence=complementarity.kappa_sum_is_constant,
        shadow_class=canonical.shadow_class,
        shadow_depth=canonical.shadow_depth,
        langlands_dual_type=canonical.langlands_dual_type,
        koszul_status=canonical.koszul_status,
    )


# =====================================================================
# 8.  Affine vertex algebra (pre-DS) central charge
# =====================================================================

def affine_central_charge(lie_type: str, rank: int, level=k_sym) -> ClaimPacket:
    """Return the typed Sugawara central-charge surface."""

    building_block_bcd_data(lie_type, rank, level)
    data = _lie_data(lie_type, rank)
    kk = sympify(level)
    formula = simplify(kk * data['dim'] / (kk + data['h_dual']))
    return _conditional_claim(
        f"Sugawara central charge of V_{kk}({data['type']})",
        "a fixed invariant-form normalization",
        f"the noncritical-level hypothesis {kk} != -{data['h_dual']}",
        "the chosen Sugawara conformal vector",
        evidence=(f"the Sugawara expression in this convention is {formula}",),
    )


def affine_kappa(lie_type: str, rank: int, level=k_sym) -> ClaimPacket:
    """Return the typed affine modular-characteristic surface."""

    building_block_bcd_data(lie_type, rank, level)
    data = _lie_data(lie_type, rank)
    kk = sympify(level)
    formula = simplify(Rational(data['dim'], 2 * data['h_dual']) * (kk + data['h_dual']))
    return _conditional_claim(
        f"affine modular characteristic of V_{kk}({data['type']})",
        "the affine genus-one Hodge trace calculation",
        "normalization of the invariant bilinear form and Hodge line",
        evidence=(f"the candidate affine trace expression is {formula}",),
    )


# =====================================================================
# 9.  DS reduction kappa deficit
# =====================================================================

def ds_kappa_deficit(lie_type: str, rank: int, level=k_sym) -> ClaimPacket:
    """Return the conditional DS trace-defect comparison."""

    affine = affine_kappa(lie_type, rank, level)
    principal = kappa(lie_type, rank, level)
    return _conditional_claim(
        f"DS modular-characteristic defect for principal {lie_type}_{rank}",
        *affine.hypotheses,
        *principal.hypotheses,
        "a chain-level BRST trace comparison identifying the ghost contribution",
        evidence=(*affine.evidence, *principal.evidence),
    )


# =====================================================================
# 10.  Minimal W-algebra kappa for so_N
# =====================================================================

def minimal_so_kappa(N: int, level=k_sym) -> ClaimPacket:
    """Return the canonical conditional minimal-orthogonal kappa packet."""

    return minimal_w_so_data(N, level).kappa


def minimal_so_complementarity(N: int, level=k_sym) -> ClaimPacket:
    """Return the canonical open minimal-orthogonal modular conductor."""

    return minimal_w_so_data(N, level).modular_conductor


# =====================================================================
# 11.  Transport-to-BV question: what replaces transpose for BCD?
# =====================================================================

@dataclass(frozen=True)
class BCDTransportQuestion:
    """Analysis of the transport-to-BV question for a BCD nilpotent orbit."""

    lie_type: str
    rank: int
    partition: Tuple[int, ...]
    transpose_parity_candidate: Tuple[int, ...]
    bv_duality: ClaimPacket
    bv_dual_type: str        # Langlands dual type
    is_principal: bool
    is_minimal: bool
    is_zero: bool
    self_duality: ClaimPacket


def transport_question(
    lie_type: str, rank: int, partition: Tuple[int, ...]
) -> BCDTransportQuestion:
    """Analyze the transport-to-BV question for a given nilpotent orbit."""
    parts = tuple(sorted(partition, reverse=True))

    if lie_type == 'B':
        N = 2 * rank + 1
    elif lie_type == 'C':
        N = 2 * rank
    elif lie_type == 'D':
        N = 2 * rank
    else:
        raise ValueError(f"Unsupported: {lie_type}")

    if sum(parts) != N:
        raise ValueError(f"Partition {parts} does not sum to {N}")

    dual_type = _langlands_dual_type(lie_type)
    transposed = _transpose_partition(parts)
    candidate = _transpose_parity_repair_candidate(transposed, dual_type)
    bv = bv_dual_partition(lie_type, rank, parts)

    is_principal = (parts == (N,)) if lie_type == 'B' else (parts == (N,) if N > 0 else True)
    # For type B: principal partition is (2n+1)
    # For type C: principal partition is (2n)
    # For type D: principal partition is (2n-1, 1) ... no.
    # Actually, for so_N and sp_N, the principal nilpotent has a single Jordan block:
    # Type B_n (so_{2n+1}): partition (2n+1)
    # Type C_n (sp_{2n}): partition (2n)
    # Type D_n (so_{2n}): partition (2n-1, 1)
    if lie_type == 'B':
        is_principal = (parts == (2 * rank + 1,))
    elif lie_type == 'C':
        is_principal = (parts == (2 * rank,))
    elif lie_type == 'D':
        is_principal = (parts == (2 * rank - 1, 1))

    is_minimal = all(p <= 3 for p in parts) and max(parts) >= 2
    # Minimal nilpotent: partition (3, 1^{N-3}) for types B, D
    # and (2^2, 1^{N-4}) for type C
    if lie_type in ('B', 'D'):
        is_minimal = (parts == tuple(sorted([3] + [1] * (N - 3), reverse=True)))
    elif lie_type == 'C':
        is_minimal = (parts == tuple(sorted([2, 2] + [1] * (N - 4), reverse=True)))

    is_zero = all(p == 1 for p in parts)

    return BCDTransportQuestion(
        lie_type=lie_type,
        rank=rank,
        partition=parts,
        transpose_parity_candidate=candidate,
        bv_duality=bv,
        bv_dual_type=dual_type,
        is_principal=is_principal,
        is_minimal=is_minimal,
        is_zero=is_zero,
        self_duality=_open_claim(
            f"the type-{lie_type}_{rank} orbit {parts} is Barbasch--Vogan self-dual",
            "identification of the Barbasch--Vogan dual orbit",
            evidence=(*bv.evidence,),
        ),
    )


# =====================================================================
# 12.  Summary table
# =====================================================================

def bcd_duality_summary(max_rank: int = 5) -> List[Dict[str, Any]]:
    """Return exact root rows and statuses of every geometric claim."""
    rows = []
    for lie_type in ['B', 'C', 'D']:
        min_rank = 2 if lie_type != 'D' else 3
        for rank in range(min_rank, max_rank + 1):
            d = principal_duality_data(lie_type, rank)
            rows.append({
                'type': d.lie_type,
                'rank': rank,
                'dim': d.dim_g,
                'h_dual': d.h_dual,
                'rho_sq': d.rho_squared,
                'exponents': d.exponents,
                'generator_weights': d.generator_weights,
                'reciprocal_weight_diagnostic': d.reciprocal_weight_diagnostic,
                'rho_status': d.anomaly_ratio.status,
                'central_charge_status': d.central_charge.status,
                'kappa_status': d.kappa.status,
                'modular_conductor_status': d.modular_conductor.status,
                'shadow_status': d.shadow_class.status,
                'langlands_dual': d.langlands_dual_type,
            })
    return rows
