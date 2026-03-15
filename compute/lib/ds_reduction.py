"""Chain-level seed scaffold for non-principal Drinfeld-Sokolov reduction.

Current scope covers the concrete finite ghost-sector BRST complexes attached
to the live non-principal frontier. The module still stops short of the full
current-plus-ghost BRST cohomology, but it now computes the exterior ghost
complex with both character and quadratic ghost terms.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations
from typing import Callable, Dict, Iterable, Tuple

from sympy import Matrix, Rational, SparseMatrix, Symbol, simplify, sympify, zeros
from sympy.polys.matrices import DomainMatrix

from compute.lib.bv_duality import first_nonselfdual_type_a_hook_pair
from compute.lib.nonprincipal_ds_orbits import (
    TRACK_FRONTIER_NONPRINCIPAL,
    ad_h_graded_basis_labels_sl_n,
    centralizer_dimension_sl_n,
    first_nonselfdual_hook_pair_sl2_triples,
    homogeneous_f_centralizer_basis_sl_n,
    matrix_to_traceless_basis_expression_sl_n,
    nonprincipal_general_cases,
    nonprincipal_hook_case,
    nonprincipal_hook_level_shift_type_a,
    nonprincipal_two_row_cases,
    nonprincipal_type_a_case,
    normalize_partition,
    partition_size,
    standard_traceless_basis_sl_n,
    subregular_partition,
    two_row_nonhook_partition,
    type_a_partition_sl2_triple,
    type_a_hook_pair_sl2_triples,
    type_a_orbit_class,
)
from compute.lib.nonprincipal_ds_reduction import (
    bp_current_presentation,
    bp_dual_level,
    bp_strong_presentation,
    hook_pair_constraint_counts_ansatz_type_a,
    nonprincipal_hook_seed_catalog,
    verify_nonprincipal_general_seed_catalog,
    verify_nonprincipal_two_row_seed_catalog,
    sl3_subregular_good_grading_multiplicities,
)


@dataclass(frozen=True)
class Sl2TripleSeed:
    """Symbolic sl_2-triple data inside a Lie algebra."""

    e: str
    h: str
    f: str


@dataclass(frozen=True)
class DSGhostWeight:
    """BRST ghost conformal-weight data for one graded root direction."""

    root_label: str
    ad_h_grade: Rational
    b_weight: Rational
    c_weight: Rational


@dataclass(frozen=True)
class DSReductionSeed:
    """Frontier DS reduction seed record."""

    lie_type: str
    rank: int
    partition: Tuple[int, ...]
    sl2_triple: Sl2TripleSeed
    positive_grades: Tuple[DSGhostWeight, ...]
    dual_level: object
    expected_target: str
    track: str
    status: str


STATUS_DS_SEED = "nonprincipal_ds_seed"


@dataclass(frozen=True)
class DSBasisElement:
    """One affine current direction together with its good-grading degree."""

    label: str
    ad_h_grade: Rational
    sector: str


@dataclass(frozen=True)
class DSConstraint:
    """Linear DS constraint attached to one positive-graded root direction."""

    root_label: str
    current_label: str
    character_value: Rational
    b_ghost: str
    c_ghost: str


@dataclass(frozen=True)
class DSBRSTBlueprint:
    """Symbolic BRST-input package for a DS reduction seed."""

    seed: DSReductionSeed
    basis: Tuple[DSBasisElement, ...]
    constraints: Tuple[DSConstraint, ...]
    positive_nilpotent_is_abelian: bool
    quadratic_ghost_term_present: bool
    expected_current_presentation: Tuple[Tuple[str, object, str], ...]
    expected_strong_presentation: Tuple[Tuple[str, object, str], ...]


@dataclass(frozen=True)
class TruncatedBRSTComplex:
    """Finite cochain complex built from a character-wedge BRST seed."""

    source_tag: str
    ghost_labels: Tuple[str, ...]
    chi_vector: Tuple[object, ...]
    basis_by_degree: Dict[int, Tuple[Tuple[int, ...], ...]]
    differentials: Dict[int, Matrix]
    quadratic_ghost_terms: Tuple[QuadraticGhostTermEntry, ...] = ()


@dataclass(frozen=True)
class HookPairDSComplexSeed:
    """Paired DS seed complexes for one non-principal type-A hook orbit pair."""

    n: int
    r: int
    source_partition: Tuple[int, ...]
    target_partition: Tuple[int, ...]
    source_level: object
    target_level: object
    source_complex: TruncatedBRSTComplex
    target_complex: TruncatedBRSTComplex
    track: str
    status: str


ConstraintBasisElement = Tuple[Tuple[int, ...], Tuple[int, ...]]
DSBasisExpression = Tuple[Tuple[str, Rational], ...]
LabeledLinearCombination = Tuple[Tuple[str, Rational], ...]


@dataclass(frozen=True)
class LinearConstraintBRSTBlock:
    """Finite total-degree block for the linear BRST/Koszul constraint complex."""

    source_tag: str
    shifted_current_labels: Tuple[str, ...]
    ghost_labels: Tuple[str, ...]
    total_degree: int
    basis_by_chain_degree: Dict[int, Tuple[ConstraintBasisElement, ...]]
    differentials: Dict[int, Matrix]


FullConstraintGhostBasisElement = Tuple[Tuple[int, ...], Tuple[int, ...], Tuple[int, ...]]


@dataclass(frozen=True)
class MixedConstraintGhostBRSTBlock:
    """Finite fixed-constraint-degree BRST block on u-variables, c-ghosts, and b-ghosts."""

    source_tag: str
    shifted_current_labels: Tuple[str, ...]
    c_ghost_labels: Tuple[str, ...]
    b_ghost_labels: Tuple[str, ...]
    chi_vector: Tuple[object, ...]
    quadratic_ghost_terms: Tuple[QuadraticGhostTermEntry, ...]
    current_action_terms: Tuple[CurrentActionTermEntry, ...]
    constraint_total_degree: int
    basis_by_brst_degree: Dict[int, Tuple[FullConstraintGhostBasisElement, ...]]
    differentials: Dict[int, Matrix]


SurvivorCoupledBasisElement = Tuple[
    Tuple[int, ...],
    Tuple[int, ...],
    Tuple[int, ...],
    Tuple[int, ...],
]

InternalSurvivorBasisElement = Tuple[
    Tuple[int, ...],
    Tuple[int, ...],
]

SemidirectSurvivorBasisElement = Tuple[
    Tuple[int, ...],
    Tuple[int, ...],
    Tuple[int, ...],
    Tuple[int, ...],
    Tuple[int, ...],
]


@dataclass(frozen=True)
class SurvivorCoupledBRSTBlock:
    """Finite BRST block with shifted currents, linear survivor variables, c- and b-ghosts."""

    source_tag: str
    shifted_current_labels: Tuple[str, ...]
    survivor_labels: Tuple[str, ...]
    c_ghost_labels: Tuple[str, ...]
    b_ghost_labels: Tuple[str, ...]
    chi_vector: Tuple[object, ...]
    quadratic_ghost_terms: Tuple[QuadraticGhostTermEntry, ...]
    current_action_terms: Tuple[CurrentActionTermEntry, ...]
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...]
    constraint_total_degree: int
    survivor_total_degree: int
    basis_by_brst_degree: Dict[int, Tuple[SurvivorCoupledBasisElement, ...]]
    differentials: Dict[int, Matrix]


@dataclass(frozen=True)
class InternalSurvivorCEBlock:
    """Finite CE block for the reduced survivor current algebra."""

    source_tag: str
    survivor_labels: Tuple[str, ...]
    c_ghost_labels: Tuple[str, ...]
    b_ghost_labels: Tuple[str, ...]
    quadratic_ghost_terms: Tuple[QuadraticGhostTermEntry, ...]
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...]
    survivor_polynomial_degree: int
    basis_by_ce_degree: Dict[int, Tuple[InternalSurvivorBasisElement, ...]]
    differentials: Dict[int, Matrix]


@dataclass(frozen=True)
class SemidirectSurvivorBRSTBlock:
    """Naive quotient-level BRST block coupling the positive sector to the internal survivor CE sector."""

    source_tag: str
    shifted_current_labels: Tuple[str, ...]
    survivor_labels: Tuple[str, ...]
    c_ghost_labels: Tuple[str, ...]
    b_ghost_labels: Tuple[str, ...]
    internal_c_ghost_labels: Tuple[str, ...]
    internal_b_ghost_labels: Tuple[str, ...]
    chi_vector: Tuple[object, ...]
    quadratic_ghost_terms: Tuple[QuadraticGhostTermEntry, ...]
    current_action_terms: Tuple[CurrentActionTermEntry, ...]
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...]
    internal_quadratic_ghost_terms: Tuple[QuadraticGhostTermEntry, ...]
    internal_survivor_action_terms: Tuple[SurvivorActionTermEntry, ...]
    constraint_total_degree: int
    survivor_total_degree: int
    max_internal_ce_degree: int
    basis_by_brst_degree: Dict[int, Tuple[SemidirectSurvivorBasisElement, ...]]
    differentials: Dict[int, Matrix]


@dataclass(frozen=True)
class DSReducedFieldCandidate:
    """One candidate surviving field in the reduced DS algebra."""

    label: str
    source_terms: DSBasisExpression
    ad_h_grade: Rational
    conformal_weight: Rational
    parity: str


@dataclass(frozen=True)
class QuadraticGhostTermEntry:
    """One nonzero support entry in the quadratic ghost term."""

    left_c_ghost: str
    right_c_ghost: str
    target_b_ghost: str
    coefficient: Rational


@dataclass(frozen=True)
class CurrentActionTermEntry:
    """One current-action term c_i . rho_i on shifted currents and b-ghosts."""

    c_ghost: str
    source_root_label: str
    target_root_label: str
    coefficient: Rational


@dataclass(frozen=True)
class SurvivorActionTermEntry:
    """One induced action term of the positive sector on a survivor variable."""

    c_ghost: str
    source_survivor_label: str
    target_survivor_label: str
    coefficient: Rational


@dataclass(frozen=True)
class SurvivorActionLiftWitness:
    """One decomposition of a positive commutator into survivor and [e,g] pieces."""

    c_ghost: str
    source_survivor_label: str
    projected_terms: LabeledLinearCombination
    ad_e_image_terms: DSBasisExpression
    ad_e_witness_preimage: DSBasisExpression


@dataclass(frozen=True)
class SurvivorDerivationDefectWitness:
    """Unreduced witness expression for one quotient-level derivation defect."""

    c_ghost: str
    left_survivor_label: str
    right_survivor_label: str
    left_action_witness_preimage: DSBasisExpression
    right_action_witness_preimage: DSBasisExpression
    unreduced_expression: DSBasisExpression
    projected_defect_terms: LabeledLinearCombination


@dataclass(frozen=True)
class FirstTransferCorrectionWitness:
    """Explicit first transferred correction built from exact current and action witnesses."""

    c_ghost: str
    current_label: str
    current_witness_preimage: DSBasisExpression
    source_survivor_label: str
    projected_action_terms: LabeledLinearCombination
    action_witness_preimage: DSBasisExpression
    correction_terms: LabeledLinearCombination


def brst_ghost_weights(ad_h_grade) -> Tuple[Rational, Rational]:
    """Ghost conformal weights from DS grading."""
    grade = sympify(ad_h_grade)
    return (Rational(1) + grade / 2, -grade / 2)


def matrix_commutator(left: Matrix, right: Matrix) -> Matrix:
    """Matrix commutator [left, right]."""
    return left * right - right * left


def _matrix_signature(matrix: Matrix | None) -> Tuple[str, int, int, Tuple[object, ...]] | None:
    """Immutable signature for caching exact matrix invariants."""
    if matrix is None or not matrix.rows or not matrix.cols:
        return None
    if isinstance(matrix, SparseMatrix):
        return ("sparse", matrix.rows, matrix.cols, tuple(sorted(matrix.todok().items())))
    # `Matrix.__iter__` goes through per-entry `__getitem__`, which is a major
    # hotspot on the larger survivor-coupled blocks. `flat()` traverses the
    # same dense data far more cheaply while preserving row-major order.
    return ("dense", matrix.rows, matrix.cols, tuple(matrix.flat()))


def _matrix_from_signature(
    kind: str,
    rows: int,
    cols: int,
    entries: Tuple[object, ...],
) -> Matrix:
    """Reconstruct a matrix from its cached dense or sparse signature."""
    if kind == "sparse":
        return SparseMatrix(rows, cols, dict(entries))
    return Matrix(rows, cols, entries)


def _matrix_product_cache_size(matrix: Matrix) -> int:
    """Approximate signature size used to decide whether cache hashing is worth it."""
    if isinstance(matrix, SparseMatrix):
        return matrix.nnz()
    return matrix.rows * matrix.cols


def _matrix_is_zero(matrix: Matrix) -> bool:
    """Check whether a concrete matrix is zero without forcing an extra dense reconstruction."""
    if isinstance(matrix, SparseMatrix):
        return matrix.nnz() == 0
    zero_flag = matrix.is_zero_matrix
    if zero_flag is not None:
        return bool(zero_flag)
    return matrix == zeros(matrix.rows, matrix.cols)


@lru_cache(maxsize=256)
def _exact_matrix_rank_from_signature(
    kind: str,
    rows: int,
    cols: int,
    entries: Tuple[object, ...],
) -> int:
    """Exact matrix rank cached by immutable matrix data."""
    matrix = _matrix_from_signature(kind, rows, cols, entries)
    try:
        return int(DomainMatrix.from_Matrix(matrix).rank())
    except Exception:
        return int(matrix.rank())


def exact_matrix_rank(matrix: Matrix | None) -> int:
    """Exact matrix rank via DomainMatrix, with a dense fallback when needed."""
    signature = _matrix_signature(matrix)
    if signature is None:
        return 0
    return _exact_matrix_rank_from_signature(*signature)


@lru_cache(maxsize=256)
def _matrix_product_is_zero_from_signatures(
    left_kind: str,
    left_rows: int,
    left_cols: int,
    left_entries: Tuple[object, ...],
    right_kind: str,
    right_rows: int,
    right_cols: int,
    right_entries: Tuple[object, ...],
) -> bool:
    """Whether the product of two cached matrices is the zero matrix."""
    left = _matrix_from_signature(left_kind, left_rows, left_cols, left_entries)
    right = _matrix_from_signature(right_kind, right_rows, right_cols, right_entries)
    return _matrix_is_zero(left * right)


def _matrix_product_is_zero(left: Matrix | None, right: Matrix | None) -> bool:
    """Whether two compatible differentials compose to zero."""
    if left is None or right is None or not left.rows or not left.cols or not right.rows or not right.cols:
        return True
    # Large square-zero checks are faster to compute directly than to hash and
    # reconstruct through the signature cache. Keep caching only for the small
    # matrices that are actually reused cheaply.
    if _matrix_product_cache_size(left) + _matrix_product_cache_size(right) > 100_000:
        return _matrix_is_zero(left * right)
    left_signature = _matrix_signature(left)
    right_signature = _matrix_signature(right)
    if left_signature is None or right_signature is None:
        return True
    return _matrix_product_is_zero_from_signatures(*left_signature, *right_signature)


@dataclass(frozen=True)
class FiniteBlockInvariantSummary:
    """One-pass finite-block invariant summary used by the DS verifier hotspots."""

    homology_dimensions: Tuple[Tuple[int, int], ...]
    has_square_zero: bool

    @property
    def is_acyclic(self) -> bool:
        """Whether the recorded block homology vanishes in every degree."""
        return all(value == 0 for _, value in self.homology_dimensions)


def _cochain_block_invariant_summary(
    basis_by_degree: Dict[int, Tuple[object, ...]],
    differentials: Dict[int, Matrix],
) -> FiniteBlockInvariantSummary:
    """Compute cochain homology dimensions and d^2 = 0 in one pass."""
    homology_dimensions = []
    has_square_zero = True
    for degree in sorted(basis_by_degree):
        dim_c = len(basis_by_degree[degree])
        d_curr = differentials.get(degree)
        d_prev = differentials.get(degree - 1)
        rank_curr = exact_matrix_rank(d_curr)
        rank_prev = exact_matrix_rank(d_prev)
        homology_dimensions.append((degree, (dim_c - rank_curr) - rank_prev))
        if has_square_zero and d_curr is not None:
            d_next = differentials.get(degree + 1)
            if d_next is not None and not _matrix_product_is_zero(d_next, d_curr):
                has_square_zero = False
    return FiniteBlockInvariantSummary(tuple(homology_dimensions), has_square_zero)


def _chain_block_invariant_summary(
    basis_by_degree: Dict[int, Tuple[object, ...]],
    differentials: Dict[int, Matrix],
) -> FiniteBlockInvariantSummary:
    """Compute chain homology dimensions and d^2 = 0 in one pass."""
    homology_dimensions = []
    has_square_zero = True
    max_degree = max(basis_by_degree)
    for degree in range(max_degree + 1):
        dim_c = len(basis_by_degree[degree])
        d_down = differentials.get(degree)
        d_up = differentials.get(degree + 1)
        rank_down = exact_matrix_rank(d_down)
        rank_up = exact_matrix_rank(d_up)
        homology_dimensions.append((degree, (dim_c - rank_down) - rank_up))
        if has_square_zero and d_down is not None:
            d_prev = differentials.get(degree - 1)
            if d_prev is not None and not _matrix_product_is_zero(d_prev, d_down):
                has_square_zero = False
    return FiniteBlockInvariantSummary(tuple(homology_dimensions), has_square_zero)


def mixed_constraint_ghost_block_invariant_summary(
    block: MixedConstraintGhostBRSTBlock,
) -> FiniteBlockInvariantSummary:
    """One-pass homology and square-zero summary for a mixed BRST block."""
    return _cochain_block_invariant_summary(block.basis_by_brst_degree, block.differentials)


def survivor_coupled_block_invariant_summary(
    block: SurvivorCoupledBRSTBlock,
) -> FiniteBlockInvariantSummary:
    """One-pass homology and square-zero summary for a survivor-coupled BRST block."""
    return _cochain_block_invariant_summary(block.basis_by_brst_degree, block.differentials)


def semidirect_survivor_block_invariant_summary(
    block: SemidirectSurvivorBRSTBlock,
) -> FiniteBlockInvariantSummary:
    """One-pass homology and square-zero summary for a semidirect survivor BRST block."""
    return _cochain_block_invariant_summary(block.basis_by_brst_degree, block.differentials)


def linear_constraint_block_invariant_summary(
    block: LinearConstraintBRSTBlock,
) -> FiniteBlockInvariantSummary:
    """One-pass homology and square-zero summary for a linear constraint block."""
    return _chain_block_invariant_summary(block.basis_by_chain_degree, block.differentials)


def _block_invariant_summaries(
    blocks: Iterable[object],
    summary_fn: Callable[[object], FiniteBlockInvariantSummary],
) -> Tuple[FiniteBlockInvariantSummary, ...]:
    """Materialize block summaries once when multiple invariant predicates are needed."""
    return tuple(summary_fn(block) for block in blocks)


def _all_block_summaries_have_square_zero(
    summaries: Iterable[FiniteBlockInvariantSummary],
) -> bool:
    """Whether every block summary satisfies d^2 = 0."""
    return all(summary.has_square_zero for summary in summaries)


def _all_block_summaries_are_acyclic(
    summaries: Iterable[FiniteBlockInvariantSummary],
) -> bool:
    """Whether every block summary has zero homology."""
    return all(summary.is_acyclic for summary in summaries)


def _all_blocks_have_square_zero_and_are_acyclic(
    blocks: Iterable[object],
    summary_fn: Callable[[object], FiniteBlockInvariantSummary],
) -> bool:
    """Hot-path combined invariant check that avoids a second rank pass."""
    for block in blocks:
        summary = summary_fn(block)
        if not summary.has_square_zero or not summary.is_acyclic:
            return False
    return True


def _basis_expression_from_coefficients(
    coefficients: Dict[str, object],
    label_order: Tuple[str, ...],
) -> DSBasisExpression:
    """Ordered basis expression from a sparse coefficient dictionary."""
    return tuple(
        (label, simplify(coefficients[label]))
        for label in label_order
        if simplify(coefficients.get(label, 0)) != 0
    )


def _labeled_linear_combination(
    coefficients: Dict[str, object],
    label_order: Tuple[str, ...],
) -> LabeledLinearCombination:
    """Ordered labeled linear combination from a sparse coefficient dictionary."""
    return tuple(
        (label, simplify(coefficients[label]))
        for label in label_order
        if simplify(coefficients.get(label, 0)) != 0
    )


def _sl3_matrix_unit(i: int, j: int) -> Matrix:
    """Standard elementary 3x3 matrix."""
    matrix = zeros(3, 3)
    matrix[i - 1, j - 1] = 1
    return matrix


def sl3_subregular_basis_matrices() -> Dict[str, Matrix]:
    """Matrix realization of the ordered sl_3 basis used in the DS seed."""
    e11 = _sl3_matrix_unit(1, 1)
    e22 = _sl3_matrix_unit(2, 2)
    e33 = _sl3_matrix_unit(3, 3)
    return {
        "E12": _sl3_matrix_unit(1, 2),
        "E13": _sl3_matrix_unit(1, 3),
        "F23": _sl3_matrix_unit(3, 2),
        "H1": e11 - e22,
        "H2": e22 - e33,
        "E23": _sl3_matrix_unit(2, 3),
        "F13": _sl3_matrix_unit(3, 1),
        "F12": _sl3_matrix_unit(2, 1),
    }


def ds_basis_expression_matrix(
    source_terms: DSBasisExpression,
    basis_matrices: Dict[str, Matrix],
) -> Matrix:
    """Evaluate a linear combination of basis labels in a matrix model."""
    if not basis_matrices:
        raise ValueError("basis_matrices must be nonempty")
    nrows = next(iter(basis_matrices.values())).rows
    matrix = zeros(nrows, nrows)
    for label, coefficient in source_terms:
        matrix += sympify(coefficient) * basis_matrices[label]
    return matrix


def _ds_basis_expression_coordinates(
    source_terms: DSBasisExpression,
    basis_order: Tuple[str, ...],
) -> Matrix:
    """Coordinate column of a basis expression in the ordered basis."""
    index = _basis_order_index_map(basis_order)
    coordinates = zeros(len(basis_order), 1)
    for label, coefficient in source_terms:
        coordinates[index[label], 0] += sympify(coefficient)
    return coordinates


@lru_cache(maxsize=256)
def _basis_order_index_map(basis_order: Tuple[str, ...]) -> Dict[str, int]:
    """Index lookup for a fixed basis order."""
    return {label: position for position, label in enumerate(basis_order)}


def _basis_expression_ad_h_grade(
    source_terms: DSBasisExpression,
    basis_grades: Dict[str, Rational],
) -> Rational:
    """Return the homogeneous ad(h)-grade of a basis expression."""
    grades = {basis_grades[label] for label, coefficient in source_terms if coefficient != 0}
    if len(grades) != 1:
        raise ValueError("basis expression must be homogeneous in ad(h)-grade")
    return next(iter(grades))


def sl3_subregular_sl2_triple() -> Sl2TripleSeed:
    """Standard symbolic triple for the sl_3 subregular seed."""
    return Sl2TripleSeed(e="E12", h="H1", f="F12")


def sl3_subregular_positive_grades() -> Dict[str, Rational]:
    """Positive ad(h)-grades used by the subregular DS seed."""
    # For h = H1: alpha1 has grade 2, alpha1+alpha2 has grade 1.
    return {
        "alpha1": Rational(2),
        "alpha1+alpha2": Rational(1),
    }


def sl3_subregular_basis_grades() -> Dict[str, Rational]:
    """Full good-grading profile for the standard sl_3 subregular seed."""
    return {
        "E12": Rational(2),
        "E13": Rational(1),
        "F23": Rational(1),
        "H1": Rational(0),
        "H2": Rational(0),
        "E23": Rational(-1),
        "F13": Rational(-1),
        "F12": Rational(-2),
    }


def sl3_subregular_basis_profile() -> Tuple[DSBasisElement, ...]:
    """Ordered affine-current basis profile for the subregular good grading."""
    sectors = {
        "E12": "positive_root",
        "E13": "positive_root",
        "F23": "positive_root",
        "H1": "cartan",
        "H2": "cartan",
        "E23": "negative_root",
        "F13": "negative_root",
        "F12": "negative_root",
    }
    order = ("E12", "E13", "F23", "H1", "H2", "E23", "F13", "F12")
    grades = sl3_subregular_basis_grades()
    return tuple(
        DSBasisElement(
            label=label,
            ad_h_grade=grades[label],
            sector=sectors[label],
        )
        for label in order
    )


def sl3_subregular_ad_e_image_witnesses() -> Dict[str, DSBasisExpression]:
    """Witness preimages for a basis of [e, sl_3] in the subregular triple."""
    return {
        "H1": (("F12", Rational(1)),),
        "E12": (("H1", Rational(-1, 2)),),
        "E13": (("E23", Rational(1)),),
        "F23": (("F13", Rational(-1)),),
    }


def sl3_subregular_ad_e_image_basis() -> Tuple[DSBasisElement, ...]:
    """Explicit basis of [e, sl_3] for the subregular sl_3 triple."""
    grades = sl3_subregular_basis_grades()
    order = ("H1", "E12", "E13", "F23")
    return tuple(
        DSBasisElement(
            label=label,
            ad_h_grade=grades[label],
            sector="image_ad_e",
        )
        for label in order
    )


def sl3_subregular_strong_generator_candidates() -> Tuple[DSReducedFieldCandidate, ...]:
    """Strong generator candidates from the subregular centralizer g^f."""
    basis_grades = sl3_subregular_basis_grades()
    specs = (
        ("J", (("H1", Rational(1, 2)), ("H2", Rational(1))), "bosonic"),
        ("G+", (("E23", Rational(1)),), "fermionic"),
        ("G-", (("F13", Rational(1)),), "fermionic"),
        ("T", (("F12", Rational(1)),), "bosonic"),
    )
    candidates = []
    for label, source_terms, parity in specs:
        grade = _basis_expression_ad_h_grade(source_terms, basis_grades)
        candidates.append(
            DSReducedFieldCandidate(
                label=label,
                source_terms=source_terms,
                ad_h_grade=grade,
                conformal_weight=Rational(1) - grade / 2,
                parity=parity,
            )
        )
    return tuple(candidates)


def _sl3_subregular_split_basis_matrix() -> Matrix:
    """Change-of-basis matrix for sl_3 = [e,sl_3] ⊕ g^f in the ordered basis."""
    basis_order = tuple(item.label for item in sl3_subregular_basis_profile())
    columns = [
        _ds_basis_expression_coordinates(((item.label, Rational(1)),), basis_order)
        for item in sl3_subregular_ad_e_image_basis()
    ] + [
        _ds_basis_expression_coordinates(candidate.source_terms, basis_order)
        for candidate in sl3_subregular_strong_generator_candidates()
    ]
    return Matrix.hstack(*columns)


def sl3_subregular_split_expression(
    source_terms: DSBasisExpression,
) -> Tuple[DSBasisExpression, LabeledLinearCombination]:
    """Split one sl_3 expression into [e,sl_3] and survivor components."""
    basis_order = tuple(item.label for item in sl3_subregular_basis_profile())
    ad_e_basis = sl3_subregular_ad_e_image_basis()
    strong_candidates = sl3_subregular_strong_generator_candidates()
    coefficients = _sl3_subregular_split_basis_matrix().LUsolve(
        _ds_basis_expression_coordinates(source_terms, basis_order)
    )
    ad_e_terms = tuple(
        (item.label, simplify(coefficients[index, 0]))
        for index, item in enumerate(ad_e_basis)
        if simplify(coefficients[index, 0]) != 0
    )
    offset = len(ad_e_basis)
    projected_terms = tuple(
        (candidate.label, simplify(coefficients[offset + index, 0]))
        for index, candidate in enumerate(strong_candidates)
        if simplify(coefficients[offset + index, 0]) != 0
    )
    return ad_e_terms, projected_terms


def sl3_subregular_expand_ad_e_terms_to_witness_preimage(
    ad_e_terms: DSBasisExpression,
) -> DSBasisExpression:
    """Expand one [e,sl_3]-expression to chosen explicit preimages."""
    witness_map = sl3_subregular_ad_e_image_witnesses()
    basis_order = tuple(item.label for item in sl3_subregular_basis_profile())
    coefficients: Dict[str, object] = {}
    for label, coefficient in ad_e_terms:
        for witness_label, witness_coefficient in witness_map[label]:
            coefficients[witness_label] = simplify(
                coefficients.get(witness_label, 0)
                + sympify(coefficient) * sympify(witness_coefficient)
            )
    return _basis_expression_from_coefficients(coefficients, basis_order)


def sl3_subregular_project_expression_to_strong_candidates(
    source_terms: DSBasisExpression,
) -> Dict[str, Rational]:
    """Project a basis expression to g^f along the splitting [e,sl_3] ⊕ g^f."""
    basis_order = tuple(item.label for item in sl3_subregular_basis_profile())
    coefficients = _sl3_subregular_split_basis_matrix().LUsolve(
        _ds_basis_expression_coordinates(source_terms, basis_order)
    )
    strong_candidates = sl3_subregular_strong_generator_candidates()
    offset = len(sl3_subregular_ad_e_image_basis())
    projection: Dict[str, Rational] = {}
    for index, candidate in enumerate(strong_candidates):
        coefficient = simplify(coefficients[offset + index, 0])
        if coefficient != 0:
            projection[candidate.label] = coefficient
    return projection


def sl3_subregular_project_basis_label_to_strong_candidates(label: str) -> Dict[str, Rational]:
    """Project one ordered sl_3 basis label to the surviving strong candidates."""
    return sl3_subregular_project_expression_to_strong_candidates(((label, Rational(1)),))


def _sl3_subregular_matrix_to_basis_expression(matrix: Matrix) -> DSBasisExpression:
    """Re-expand a traceless 3x3 matrix in the ordered sl_3 basis."""
    basis_order = tuple(item.label for item in sl3_subregular_basis_profile())
    basis_matrices = sl3_subregular_basis_matrices()
    basis_columns = Matrix.hstack(*[basis_matrices[label].reshape(9, 1) for label in basis_order])
    coefficients = basis_columns.gauss_jordan_solve(matrix.reshape(9, 1))[0]
    return tuple(
        (label, simplify(coefficients[index, 0]))
        for index, label in enumerate(basis_order)
        if simplify(coefficients[index, 0]) != 0
    )


def sl3_subregular_projected_strong_brackets() -> Dict[Tuple[str, str], Dict[str, Rational]]:
    """Projected commutators on the surviving strong-candidate sector."""
    basis_matrices = sl3_subregular_basis_matrices()
    candidates = sl3_subregular_strong_generator_candidates()
    projected: Dict[Tuple[str, str], Dict[str, Rational]] = {}
    for left in candidates:
        for right in candidates:
            commutator = matrix_commutator(
                ds_basis_expression_matrix(left.source_terms, basis_matrices),
                ds_basis_expression_matrix(right.source_terms, basis_matrices),
            )
            source_terms = _sl3_subregular_matrix_to_basis_expression(commutator)
            projected[(left.label, right.label)] = (
                sl3_subregular_project_expression_to_strong_candidates(source_terms)
                if source_terms
                else {}
            )
    return projected


def sl3_subregular_ghost_profile() -> Tuple[DSGhostWeight, ...]:
    """Ghost profile for the positive-graded root directions."""
    profile = []
    for root, grade in sl3_subregular_positive_grades().items():
        b_weight, c_weight = brst_ghost_weights(grade)
        profile.append(
            DSGhostWeight(
                root_label=root,
                ad_h_grade=grade,
                b_weight=b_weight,
                c_weight=c_weight,
            )
        )
    return tuple(profile)


def _ghost_profile_from_positive_grade_labels(
    graded_basis_labels: Dict[int, Tuple[str, ...]],
) -> Tuple[DSGhostWeight, ...]:
    """Ghost profile from positive ad(h)-graded basis labels."""
    profile = []
    for grade in sorted(graded_basis_labels, reverse=True):
        if grade <= 0:
            continue
        for label in graded_basis_labels[grade]:
            b_weight, c_weight = brst_ghost_weights(Rational(grade))
            profile.append(
                DSGhostWeight(
                    root_label=label,
                    ad_h_grade=Rational(grade),
                    b_weight=b_weight,
                    c_weight=c_weight,
                )
            )
    return tuple(profile)


def hook_pair_ghost_profiles(n: int, r: int) -> Tuple[Tuple[DSGhostWeight, ...], Tuple[DSGhostWeight, ...]]:
    """Positive-grade ghost profiles for a hook orbit and its transpose-dual hook."""
    source_triple, target_triple = type_a_hook_pair_sl2_triples(n, r)
    source_graded_basis = ad_h_graded_basis_labels_sl_n(source_triple.h)
    target_graded_basis = ad_h_graded_basis_labels_sl_n(target_triple.h)
    return (
        _ghost_profile_from_positive_grade_labels(source_graded_basis),
        _ghost_profile_from_positive_grade_labels(target_graded_basis),
    )


def _positive_simple_root_count_from_h(h: Matrix) -> int:
    """Count positive ad(h)-grades on simple roots alpha_i (i=1,...,n-1)."""
    return sum(1 for index in range(h.rows - 1) if h[index, index] - h[index + 1, index + 1] > 0)


def partition_pair_ghost_profiles(
    partition: Tuple[int, ...],
) -> Tuple[Tuple[DSGhostWeight, ...], Tuple[DSGhostWeight, ...]]:
    """Positive-grade ghost profiles for one type-A partition and its transpose dual."""
    case = nonprincipal_type_a_case(partition)
    source_triple = type_a_partition_sl2_triple(case.partition)
    target_triple = type_a_partition_sl2_triple(case.dual_partition)
    source_graded_basis = ad_h_graded_basis_labels_sl_n(source_triple.h)
    target_graded_basis = ad_h_graded_basis_labels_sl_n(target_triple.h)
    return (
        _ghost_profile_from_positive_grade_labels(source_graded_basis),
        _ghost_profile_from_positive_grade_labels(target_graded_basis),
    )


@lru_cache(maxsize=64)
def _partition_pair_default_constraint_counts(partition: Tuple[int, ...]) -> Tuple[int, int]:
    """Default source/target truncation counts for one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    source_triple = type_a_partition_sl2_triple(case.partition)
    target_triple = type_a_partition_sl2_triple(case.dual_partition)
    return (
        max(1, _positive_simple_root_count_from_h(source_triple.h)),
        max(1, _positive_simple_root_count_from_h(target_triple.h)),
    )


@lru_cache(maxsize=64)
def _partition_pair_truncated_profiles(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[DSGhostWeight, ...], Tuple[DSGhostWeight, ...]]:
    """Truncated source/target ghost profiles for one type-A non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    default_source, default_target = _partition_pair_default_constraint_counts(case.partition)
    source_count = default_source if source_num_constraints is None else source_num_constraints
    target_count = default_target if target_num_constraints is None else target_num_constraints
    source_profile, target_profile = partition_pair_ghost_profiles(case.partition)
    return (
        _truncate_ghost_profile(source_profile, source_count, "source"),
        _truncate_ghost_profile(target_profile, target_count, "target"),
    )


def _truncate_ghost_profile(
    profile: Tuple[DSGhostWeight, ...],
    count: int,
    side: str,
) -> Tuple[DSGhostWeight, ...]:
    """Take a deterministic prefix of a ghost profile for finite truncations."""
    if count < 1:
        raise ValueError(f"{side} ghost count must be positive")
    if count > len(profile):
        raise ValueError(
            f"{side} ghost count {count} exceeds available positive directions {len(profile)}"
        )
    return profile[:count]


def first_nonselfdual_hook_pair_ghost_profiles() -> Tuple[Tuple[DSGhostWeight, ...], Tuple[DSGhostWeight, ...]]:
    """Positive-grade ghost profiles for the first non-self-dual hook pair."""
    return hook_pair_ghost_profiles(4, 1)


def first_nonselfdual_hook_pair_constraint_characters() -> Tuple[Dict[str, Rational], Dict[str, Rational]]:
    """Default DS character data on the positive directions of the first hook pair."""
    source_profile, target_profile = first_nonselfdual_hook_pair_ghost_profiles()
    source_positive_brackets, target_positive_brackets = (
        first_nonselfdual_hook_pair_positive_nilpotent_brackets()
    )
    source_commutator_targets = {target for _, _, target in source_positive_brackets}
    target_commutator_targets = {target for _, _, target in target_positive_brackets}
    source_character = {}
    source_assigned = False
    for item in source_profile:
        value = Rational(0)
        if (not source_assigned) and item.root_label not in source_commutator_targets:
            value = Rational(1)
            source_assigned = True
        source_character[item.root_label] = value
    target_character = {}
    target_assigned = False
    for item in target_profile:
        value = Rational(0)
        if (not target_assigned) and item.root_label not in target_commutator_targets:
            value = Rational(1)
            target_assigned = True
        target_character[item.root_label] = value
    return source_character, target_character


def _constraints_from_ghost_profile(
    profile: Tuple[DSGhostWeight, ...],
    character: Dict[str, Rational],
    side: str,
) -> Tuple[DSConstraint, ...]:
    """Build DS constraints from a ghost profile and character assignment."""
    return tuple(
        DSConstraint(
            root_label=item.root_label,
            current_label=item.root_label,
            character_value=character[item.root_label],
            b_ghost=f"b_{side}_{item.root_label}",
            c_ghost=f"c_{side}_{item.root_label}",
        )
        for item in profile
    )


def first_nonselfdual_hook_pair_constraints() -> Tuple[Tuple[DSConstraint, ...], Tuple[DSConstraint, ...]]:
    """Explicit DS constraints on the first non-self-dual hook pair."""
    source_profile, target_profile = first_nonselfdual_hook_pair_ghost_profiles()
    source_character, target_character = first_nonselfdual_hook_pair_constraint_characters()
    return (
        _constraints_from_ghost_profile(source_profile, source_character, "source"),
        _constraints_from_ghost_profile(target_profile, target_character, "target"),
    )


def _current_action_terms_from_constraints_and_brackets(
    constraints: Tuple[DSConstraint, ...],
    brackets: Tuple[Tuple[str, str, str], ...],
) -> Tuple[CurrentActionTermEntry, ...]:
    """Current-action terms induced by adjoint brackets on the positive sector."""
    constraint_map = {item.root_label: item for item in constraints}
    terms = []
    for left, right, target in brackets:
        terms.append(
            CurrentActionTermEntry(
                c_ghost=constraint_map[left].c_ghost,
                source_root_label=right,
                target_root_label=target,
                coefficient=Rational(1),
            )
        )
        terms.append(
            CurrentActionTermEntry(
                c_ghost=constraint_map[right].c_ghost,
                source_root_label=left,
                target_root_label=target,
                coefficient=Rational(-1),
            )
        )
    return tuple(terms)


def first_nonselfdual_hook_pair_current_action_terms(
) -> Tuple[Tuple[CurrentActionTermEntry, ...], Tuple[CurrentActionTermEntry, ...]]:
    """Current-action terms c.rho for the first non-self-dual hook pair."""
    source_constraints, target_constraints = first_nonselfdual_hook_pair_constraints()
    source_brackets, target_brackets = first_nonselfdual_hook_pair_positive_nilpotent_brackets()
    return (
        _current_action_terms_from_constraints_and_brackets(source_constraints, source_brackets),
        _current_action_terms_from_constraints_and_brackets(target_constraints, target_brackets),
    )


def _positive_nilpotent_brackets_from_labels(
    labels: Tuple[str, ...],
    n: int,
) -> Tuple[Tuple[str, str, str], ...]:
    """Nonzero brackets among positively graded standard basis labels."""
    basis_matrices = dict(standard_traceless_basis_sl_n(n))
    label_set = set(labels)
    brackets = []
    for index, left in enumerate(labels):
        for right in labels[index + 1 :]:
            commutator = matrix_commutator(basis_matrices[left], basis_matrices[right])
            if commutator == zeros(n, n):
                continue
            expression = matrix_to_traceless_basis_expression_sl_n(commutator)
            if len(expression) != 1:
                continue
            target_label, coefficient = expression[0]
            if target_label not in label_set:
                continue
            if coefficient == 1:
                brackets.append((left, right, target_label))
            elif coefficient == -1:
                brackets.append((right, left, target_label))
    return tuple(brackets)


def first_nonselfdual_hook_pair_positive_nilpotent_brackets(
) -> Tuple[Tuple[Tuple[str, str, str], ...], Tuple[Tuple[str, str, str], ...]]:
    """Nonzero positive-nilpotent brackets for the first hook pair."""
    source_profile, target_profile = first_nonselfdual_hook_pair_ghost_profiles()
    source_labels = tuple(item.root_label for item in source_profile)
    target_labels = tuple(item.root_label for item in target_profile)
    return (
        _positive_nilpotent_brackets_from_labels(source_labels, n=4),
        _positive_nilpotent_brackets_from_labels(target_labels, n=4),
    )


def first_nonselfdual_hook_pair_quadratic_ghost_term_support(
) -> Tuple[Tuple[QuadraticGhostTermEntry, ...], Tuple[QuadraticGhostTermEntry, ...]]:
    """Quadratic ghost support induced by the first hook-pair positive brackets."""
    source_constraints, target_constraints = first_nonselfdual_hook_pair_constraints()
    source_constraint_map = {item.root_label: item for item in source_constraints}
    target_constraint_map = {item.root_label: item for item in target_constraints}
    source_brackets, target_brackets = first_nonselfdual_hook_pair_positive_nilpotent_brackets()
    return (
        tuple(
            QuadraticGhostTermEntry(
                left_c_ghost=source_constraint_map[left].c_ghost,
                right_c_ghost=source_constraint_map[right].c_ghost,
                target_b_ghost=source_constraint_map[target].b_ghost,
                coefficient=Rational(1),
            )
            for left, right, target in source_brackets
        ),
        tuple(
            QuadraticGhostTermEntry(
                left_c_ghost=target_constraint_map[left].c_ghost,
                right_c_ghost=target_constraint_map[right].c_ghost,
                target_b_ghost=target_constraint_map[target].b_ghost,
                coefficient=Rational(1),
            )
            for left, right, target in target_brackets
        ),
    )


@lru_cache(maxsize=64)
def _hook_pair_truncated_profiles(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[DSGhostWeight, ...], Tuple[DSGhostWeight, ...]]:
    """Truncated source/target ghost profiles for one hook pair."""
    default_source, default_target = hook_pair_constraint_counts_ansatz_type_a(n, r)
    source_count = default_source if source_num_constraints is None else source_num_constraints
    target_count = default_target if target_num_constraints is None else target_num_constraints
    source_profile, target_profile = hook_pair_ghost_profiles(n, r)
    return (
        _truncate_ghost_profile(source_profile, source_count, "source"),
        _truncate_ghost_profile(target_profile, target_count, "target"),
    )


def _default_constraint_character_from_brackets(
    profile: Tuple[DSGhostWeight, ...],
    brackets: Tuple[Tuple[str, str, str], ...],
) -> Dict[str, Rational]:
    """Default character assignment: first non-commutator-target gets value 1."""
    commutator_targets = {target for _, _, target in brackets}
    character: Dict[str, Rational] = {}
    assigned = False
    for item in profile:
        value = Rational(0)
        if (not assigned) and item.root_label not in commutator_targets:
            value = Rational(1)
            assigned = True
        character[item.root_label] = value
    if profile and not assigned:
        character[profile[0].root_label] = Rational(1)
    return character


@lru_cache(maxsize=64)
def hook_pair_positive_nilpotent_brackets(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[Tuple[str, str, str], ...], Tuple[Tuple[str, str, str], ...]]:
    """Nonzero positive-nilpotent brackets for one hook pair (possibly truncated)."""
    source_profile, target_profile = _hook_pair_truncated_profiles(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_labels = tuple(item.root_label for item in source_profile)
    target_labels = tuple(item.root_label for item in target_profile)
    return (
        _positive_nilpotent_brackets_from_labels(source_labels, n=n),
        _positive_nilpotent_brackets_from_labels(target_labels, n=n),
    )


@lru_cache(maxsize=64)
def hook_pair_constraint_characters(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Dict[str, Rational], Dict[str, Rational]]:
    """Default DS character data for one hook pair (possibly truncated)."""
    source_profile, target_profile = _hook_pair_truncated_profiles(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_brackets, target_brackets = hook_pair_positive_nilpotent_brackets(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        _default_constraint_character_from_brackets(source_profile, source_brackets),
        _default_constraint_character_from_brackets(target_profile, target_brackets),
    )


@lru_cache(maxsize=64)
def hook_pair_constraints(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[DSConstraint, ...], Tuple[DSConstraint, ...]]:
    """DS constraint package for one hook pair (possibly truncated)."""
    source_profile, target_profile = _hook_pair_truncated_profiles(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_character, target_character = hook_pair_constraint_characters(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        _constraints_from_ghost_profile(source_profile, source_character, "source"),
        _constraints_from_ghost_profile(target_profile, target_character, "target"),
    )


@lru_cache(maxsize=64)
def hook_pair_quadratic_ghost_term_support(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[QuadraticGhostTermEntry, ...], Tuple[QuadraticGhostTermEntry, ...]]:
    """Quadratic ghost support induced by positive brackets for one hook pair."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_constraint_map = {item.root_label: item for item in source_constraints}
    target_constraint_map = {item.root_label: item for item in target_constraints}
    source_brackets, target_brackets = hook_pair_positive_nilpotent_brackets(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        tuple(
            QuadraticGhostTermEntry(
                left_c_ghost=source_constraint_map[left].c_ghost,
                right_c_ghost=source_constraint_map[right].c_ghost,
                target_b_ghost=source_constraint_map[target].b_ghost,
                coefficient=Rational(1),
            )
            for left, right, target in source_brackets
        ),
        tuple(
            QuadraticGhostTermEntry(
                left_c_ghost=target_constraint_map[left].c_ghost,
                right_c_ghost=target_constraint_map[right].c_ghost,
                target_b_ghost=target_constraint_map[target].b_ghost,
                coefficient=Rational(1),
            )
            for left, right, target in target_brackets
        ),
    )


@lru_cache(maxsize=64)
def hook_pair_current_action_terms(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[CurrentActionTermEntry, ...], Tuple[CurrentActionTermEntry, ...]]:
    """Current-action terms induced by positive brackets for one hook pair."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_brackets, target_brackets = hook_pair_positive_nilpotent_brackets(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        _current_action_terms_from_constraints_and_brackets(source_constraints, source_brackets),
        _current_action_terms_from_constraints_and_brackets(target_constraints, target_brackets),
    )


@lru_cache(maxsize=64)
def partition_pair_positive_nilpotent_brackets(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[Tuple[str, str, str], ...], Tuple[Tuple[str, str, str], ...]]:
    """Nonzero positive-nilpotent brackets for one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_profile, target_profile = _partition_pair_truncated_profiles(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_labels = tuple(item.root_label for item in source_profile)
    target_labels = tuple(item.root_label for item in target_profile)
    return (
        _positive_nilpotent_brackets_from_labels(source_labels, n=n),
        _positive_nilpotent_brackets_from_labels(target_labels, n=n),
    )


@lru_cache(maxsize=64)
def partition_pair_constraint_characters(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Dict[str, Rational], Dict[str, Rational]]:
    """Default DS character data for one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    source_profile, target_profile = _partition_pair_truncated_profiles(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_brackets, target_brackets = partition_pair_positive_nilpotent_brackets(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        _default_constraint_character_from_brackets(source_profile, source_brackets),
        _default_constraint_character_from_brackets(target_profile, target_brackets),
    )


@lru_cache(maxsize=64)
def partition_pair_constraints(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[DSConstraint, ...], Tuple[DSConstraint, ...]]:
    """DS constraint package for one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    source_profile, target_profile = _partition_pair_truncated_profiles(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_character, target_character = partition_pair_constraint_characters(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        _constraints_from_ghost_profile(source_profile, source_character, "source"),
        _constraints_from_ghost_profile(target_profile, target_character, "target"),
    )


@lru_cache(maxsize=64)
def partition_pair_quadratic_ghost_term_support(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[QuadraticGhostTermEntry, ...], Tuple[QuadraticGhostTermEntry, ...]]:
    """Quadratic ghost support induced by positive brackets for one partition pair."""
    case = nonprincipal_type_a_case(partition)
    source_constraints, target_constraints = partition_pair_constraints(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_constraint_map = {item.root_label: item for item in source_constraints}
    target_constraint_map = {item.root_label: item for item in target_constraints}
    source_brackets, target_brackets = partition_pair_positive_nilpotent_brackets(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        tuple(
            QuadraticGhostTermEntry(
                left_c_ghost=source_constraint_map[left].c_ghost,
                right_c_ghost=source_constraint_map[right].c_ghost,
                target_b_ghost=source_constraint_map[target].b_ghost,
                coefficient=Rational(1),
            )
            for left, right, target in source_brackets
        ),
        tuple(
            QuadraticGhostTermEntry(
                left_c_ghost=target_constraint_map[left].c_ghost,
                right_c_ghost=target_constraint_map[right].c_ghost,
                target_b_ghost=target_constraint_map[target].b_ghost,
                coefficient=Rational(1),
            )
            for left, right, target in target_brackets
        ),
    )


@lru_cache(maxsize=64)
def partition_pair_current_action_terms(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[CurrentActionTermEntry, ...], Tuple[CurrentActionTermEntry, ...]]:
    """Current-action terms induced by positive brackets for one partition pair."""
    case = nonprincipal_type_a_case(partition)
    source_constraints, target_constraints = partition_pair_constraints(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_brackets, target_brackets = partition_pair_positive_nilpotent_brackets(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        _current_action_terms_from_constraints_and_brackets(source_constraints, source_brackets),
        _current_action_terms_from_constraints_and_brackets(target_constraints, target_brackets),
    )


def _reduced_candidates_from_homogeneous_basis(
    prefix: str,
    homogeneous_basis: Dict[int, Tuple[DSBasisExpression, ...]],
) -> Tuple[DSReducedFieldCandidate, ...]:
    """Build reduced-field candidates from a homogeneous g^f basis."""
    candidates = []
    for grade in sorted(homogeneous_basis, reverse=True):
        grade_tag = f"m{abs(grade)}" if grade < 0 else str(grade)
        for index, expression in enumerate(homogeneous_basis[grade], start=1):
            candidates.append(
                DSReducedFieldCandidate(
                    label=f"{prefix}_g{grade_tag}_{index}",
                    source_terms=tuple((label, sympify(coefficient)) for label, coefficient in expression),
                    ad_h_grade=Rational(grade),
                    conformal_weight=Rational(1) - Rational(grade, 2),
                    parity="bosonic",
                )
            )
    return tuple(candidates)


@lru_cache(maxsize=64)
def hook_pair_surviving_field_candidates(
    n: int,
    r: int,
) -> Tuple[Tuple[DSReducedFieldCandidate, ...], Tuple[DSReducedFieldCandidate, ...]]:
    """Homogeneous surviving-field candidates for one hook pair."""
    source_triple, target_triple = type_a_hook_pair_sl2_triples(n, r)
    source_basis = homogeneous_f_centralizer_basis_sl_n(source_triple.f, source_triple.h)
    target_basis = homogeneous_f_centralizer_basis_sl_n(target_triple.f, target_triple.h)
    return (
        _reduced_candidates_from_homogeneous_basis("source", source_basis),
        _reduced_candidates_from_homogeneous_basis("target", target_basis),
    )


@lru_cache(maxsize=64)
def partition_pair_surviving_field_candidates(
    partition: Tuple[int, ...],
) -> Tuple[Tuple[DSReducedFieldCandidate, ...], Tuple[DSReducedFieldCandidate, ...]]:
    """Homogeneous surviving-field candidates for one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    source_triple = type_a_partition_sl2_triple(case.partition)
    target_triple = type_a_partition_sl2_triple(case.dual_partition)
    source_basis = homogeneous_f_centralizer_basis_sl_n(source_triple.f, source_triple.h)
    target_basis = homogeneous_f_centralizer_basis_sl_n(target_triple.f, target_triple.h)
    return (
        _reduced_candidates_from_homogeneous_basis("source", source_basis),
        _reduced_candidates_from_homogeneous_basis("target", target_basis),
    )


def first_nonselfdual_hook_pair_surviving_field_candidates(
) -> Tuple[Tuple[DSReducedFieldCandidate, ...], Tuple[DSReducedFieldCandidate, ...]]:
    """Homogeneous surviving-field candidates for the first non-self-dual hook pair."""
    return hook_pair_surviving_field_candidates(4, 1)


def _reduced_candidate_bracket_table(
    candidates: Tuple[DSReducedFieldCandidate, ...],
    basis_matrices: Dict[str, Matrix],
) -> Dict[Tuple[str, str], Dict[str, object]]:
    """Bracket table on a reduced-field basis that is already closed under commutator."""
    candidate_matrices = {
        candidate.label: ds_basis_expression_matrix(candidate.source_terms, basis_matrices)
        for candidate in candidates
    }
    candidate_columns = Matrix.hstack(
        *[candidate_matrices[candidate.label].reshape(next(iter(basis_matrices.values())).rows ** 2, 1) for candidate in candidates]
    )
    pivot_rows = tuple(int(index) for index in candidate_columns.T.rref()[1])
    reduced_solver = candidate_columns.extract(pivot_rows, list(range(candidate_columns.cols))).inv()
    brackets: Dict[Tuple[str, str], Dict[str, object]] = {}
    labels = [candidate.label for candidate in candidates]
    n = next(iter(basis_matrices.values())).rows
    for left in labels:
        for right in labels:
            commutator = matrix_commutator(candidate_matrices[left], candidate_matrices[right])
            if commutator == zeros(n, n):
                brackets[(left, right)] = {}
                continue
            coefficients = reduced_solver * commutator.reshape(n * n, 1).extract(pivot_rows, [0])
            brackets[(left, right)] = {
                labels[index]: simplify(coefficients[index, 0])
                for index in range(len(labels))
                if simplify(coefficients[index, 0]) != 0
            }
    return brackets


def first_nonselfdual_hook_pair_reduced_brackets(
) -> Tuple[Dict[Tuple[str, str], Dict[str, object]], Dict[Tuple[str, str], Dict[str, object]]]:
    """Closed reduced brackets on the first non-self-dual hook pair survivor sectors."""
    source_candidates, target_candidates = hook_pair_surviving_field_candidates(4, 1)
    basis_matrices = dict(standard_traceless_basis_sl_n(4))
    return (
        _reduced_candidate_bracket_table(source_candidates, basis_matrices),
        _reduced_candidate_bracket_table(target_candidates, basis_matrices),
    )


@lru_cache(maxsize=64)
def hook_pair_reduced_brackets(
    n: int,
    r: int,
) -> Tuple[Dict[Tuple[str, str], Dict[str, object]], Dict[Tuple[str, str], Dict[str, object]]]:
    """Closed reduced brackets on hook-pair survivor sectors."""
    source_candidates, target_candidates = hook_pair_surviving_field_candidates(n, r)
    basis_matrices = dict(standard_traceless_basis_sl_n(n))
    return (
        _reduced_candidate_bracket_table(source_candidates, basis_matrices),
        _reduced_candidate_bracket_table(target_candidates, basis_matrices),
    )


@lru_cache(maxsize=64)
def partition_pair_reduced_brackets(
    partition: Tuple[int, ...],
) -> Tuple[Dict[Tuple[str, str], Dict[str, object]], Dict[Tuple[str, str], Dict[str, object]]]:
    """Closed reduced brackets on one non-principal partition pair survivor sector."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_candidates, target_candidates = partition_pair_surviving_field_candidates(case.partition)
    basis_matrices = dict(standard_traceless_basis_sl_n(n))
    return (
        _reduced_candidate_bracket_table(source_candidates, basis_matrices),
        _reduced_candidate_bracket_table(target_candidates, basis_matrices),
    )


def _independent_matrix_basis(matrices: Tuple[Matrix, ...]) -> Tuple[Matrix, ...]:
    """Extract a linearly independent ordered matrix basis from a tuple of matrices."""
    if not matrices:
        return ()
    n = matrices[0].rows
    filtered = tuple(
        (matrix, matrix.reshape(n * n, 1))
        for matrix in matrices
        if matrix != zeros(n, n)
    )
    if not filtered:
        return ()
    if len(filtered) == 1:
        return (filtered[0][0],)
    pivot_columns = Matrix.hstack(*[column for _, column in filtered]).rref()[1]
    return tuple(filtered[index][0] for index in pivot_columns)


def _ad_e_image_basis_matrices(
    e_matrix: Matrix,
    basis_matrices: Dict[str, Matrix],
) -> Tuple[Matrix, ...]:
    """Independent basis of [e,g] from a fixed ordered basis of g."""
    return _independent_matrix_basis(
        tuple(
            matrix_commutator(e_matrix, basis_matrices[label])
            for label, _ in standard_traceless_basis_sl_n(e_matrix.rows)
        )
    )


def _ad_e_image_basis_matrices_with_witness_preimages(
    e_matrix: Matrix,
    basis_matrices: Dict[str, Matrix],
) -> Tuple[Tuple[Matrix, ...], Tuple[DSBasisExpression, ...]]:
    """Independent [e,g] basis together with chosen standard-basis preimages."""
    n = e_matrix.rows
    filtered = []
    for label, _ in standard_traceless_basis_sl_n(n):
        image = matrix_commutator(e_matrix, basis_matrices[label])
        if image == zeros(n, n):
            continue
        filtered.append((label, image, image.reshape(n * n, 1)))
    if not filtered:
        return (), ()
    if len(filtered) == 1:
        label, image, _ = filtered[0]
        return (image,), (((label, Rational(1)),),)
    pivot_columns = Matrix.hstack(*[column for _, _, column in filtered]).rref()[1]
    return (
        tuple(filtered[index][1] for index in pivot_columns),
        tuple(((filtered[index][0], Rational(1)),) for index in pivot_columns),
    )


def _project_matrix_to_candidate_basis(
    matrix: Matrix,
    candidate_labels: Tuple[str, ...],
    candidate_matrices: Tuple[Matrix, ...],
    complement_matrices: Tuple[Matrix, ...],
    decomposition_inverse: Matrix | None = None,
    basis_order: Tuple[str, ...] | None = None,
) -> Dict[str, Rational]:
    """Project a matrix to a candidate basis along a chosen complement."""
    n = matrix.rows
    if decomposition_inverse is None:
        combined = Matrix.hstack(
            *[
                entry.reshape(n * n, 1)
                for entry in complement_matrices + candidate_matrices
            ]
        )
        coefficients = combined.LUsolve(matrix.reshape(n * n, 1))
    else:
        if basis_order is None:
            raise ValueError("basis_order is required when decomposition_inverse is provided")
        coefficients = decomposition_inverse * _matrix_coordinate_column(matrix, basis_order)
    offset = len(complement_matrices)
    projection: Dict[str, Rational] = {}
    for index, label in enumerate(candidate_labels):
        value = simplify(coefficients[offset + index, 0])
        if value != 0:
            projection[label] = value
    return projection


def _sum_scaled_basis_expressions(
    expressions: Tuple[DSBasisExpression, ...],
    coefficients: Tuple[object, ...],
    basis_order: Tuple[str, ...],
) -> DSBasisExpression:
    """Linear combination of basis expressions collected in a fixed order."""
    accumulated: Dict[str, object] = {}
    for expression, coefficient in zip(expressions, coefficients):
        scalar = sympify(coefficient)
        if scalar == 0:
            continue
        for label, entry_coefficient in expression:
            accumulated[label] = simplify(
                accumulated.get(label, 0)
                + scalar * sympify(entry_coefficient)
            )
    return _basis_expression_from_coefficients(accumulated, basis_order)


def _basis_expression_coordinate_column(
    expression: DSBasisExpression,
    basis_order: Tuple[str, ...],
) -> Matrix:
    """Column vector of coefficients in a fixed traceless-basis order."""
    index = _basis_order_index_map(basis_order)
    coordinates = zeros(len(basis_order), 1)
    for label, coefficient in expression:
        coordinates[index[label], 0] += sympify(coefficient)
    return coordinates


def _matrix_coordinate_column(
    matrix: Matrix,
    basis_order: Tuple[str, ...],
) -> Matrix:
    """Column vector of a traceless matrix in the fixed standard traceless basis."""
    return _basis_expression_coordinate_column(
        tuple(
            (label, sympify(coefficient))
            for label, coefficient in matrix_to_traceless_basis_expression_sl_n(matrix)
        ),
        basis_order,
    )


def _split_matrix_to_candidate_basis_with_witnesses(
    matrix: Matrix,
    candidate_labels: Tuple[str, ...],
    candidate_matrices: Tuple[Matrix, ...],
    complement_matrices: Tuple[Matrix, ...],
    complement_witness_preimages: Tuple[DSBasisExpression, ...],
    basis_order: Tuple[str, ...],
    decomposition_inverse: Matrix | None = None,
) -> Tuple[DSBasisExpression, LabeledLinearCombination, DSBasisExpression]:
    """Split a matrix into complement and survivor parts with a chosen witness lift."""
    n = matrix.rows
    if decomposition_inverse is None:
        combined = Matrix.hstack(
            *[
                entry.reshape(n * n, 1)
                for entry in complement_matrices + candidate_matrices
            ]
        )
        coefficients = combined.LUsolve(matrix.reshape(n * n, 1))
    else:
        coefficients = decomposition_inverse * _matrix_coordinate_column(matrix, basis_order)
    complement_coefficients = tuple(
        simplify(coefficients[index, 0])
        for index in range(len(complement_matrices))
    )
    projected_terms = tuple(
        (label, simplify(coefficients[len(complement_matrices) + index, 0]))
        for index, label in enumerate(candidate_labels)
        if simplify(coefficients[len(complement_matrices) + index, 0]) != 0
    )
    complement_matrix = zeros(n, n)
    for coefficient, entry in zip(complement_coefficients, complement_matrices):
        complement_matrix += sympify(coefficient) * entry
    return (
        tuple(
            (label, sympify(coefficient))
            for label, coefficient in matrix_to_traceless_basis_expression_sl_n(
                complement_matrix
            )
        ),
        projected_terms,
        _sum_scaled_basis_expressions(
            complement_witness_preimages,
            complement_coefficients,
            basis_order,
        ),
    )


@lru_cache(maxsize=64)
def _first_nonselfdual_hook_pair_projection_data(
    side: str,
) -> Tuple[Tuple[str, ...], Tuple[Matrix, ...], Tuple[Matrix, ...], Dict[str, Matrix], Matrix, Matrix]:
    """Projection data g = [e,g] ⊕ g^f for one side of the first hook pair."""
    if side not in {"source", "target"}:
        raise ValueError("side must be 'source' or 'target'")
    source_triple, target_triple = first_nonselfdual_hook_pair_sl2_triples()
    source_candidates, target_candidates = first_nonselfdual_hook_pair_surviving_field_candidates()
    triple = source_triple if side == "source" else target_triple
    candidates = source_candidates if side == "source" else target_candidates
    basis_matrices = dict(standard_traceless_basis_sl_n(4))
    basis_order = tuple(label for label, _ in standard_traceless_basis_sl_n(4))
    candidate_labels = tuple(candidate.label for candidate in candidates)
    candidate_matrices = tuple(
        ds_basis_expression_matrix(candidate.source_terms, basis_matrices)
        for candidate in candidates
    )
    ad_e_basis = _ad_e_image_basis_matrices(triple.e, basis_matrices)
    decomposition_matrix = Matrix.hstack(
        *[_matrix_coordinate_column(entry, basis_order) for entry in ad_e_basis + candidate_matrices]
    )
    decomposition_inverse = decomposition_matrix.inv()
    return (
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        basis_matrices,
        decomposition_matrix,
        decomposition_inverse,
    )


def _project_hook_pair_matrix_to_survivors(
    side: str,
    matrix: Matrix,
    n: int = 4,
    r: int = 1,
) -> Dict[str, Rational]:
    """Project a hook-pair matrix to the survivor basis along [e,g]."""
    if side not in {"source", "target"}:
        raise ValueError("side must be 'source' or 'target'")
    if n == 4 and r == 1:
        candidate_labels, candidate_matrices, ad_e_basis, _, _, decomposition_inverse = (
            _first_nonselfdual_hook_pair_projection_data(side)
        )
        basis_order = tuple(label for label, _ in standard_traceless_basis_sl_n(4))
    else:
        candidate_labels, candidate_matrices, ad_e_basis, _, _, decomposition_inverse = (
            _hook_pair_projection_data(n, r, side)
        )
        basis_order = tuple(label for label, _ in standard_traceless_basis_sl_n(n))
    return _project_matrix_to_candidate_basis(
        matrix,
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        decomposition_inverse=decomposition_inverse,
        basis_order=basis_order,
    )


@lru_cache(maxsize=64)
def _hook_pair_projection_witness_data(
    n: int,
    r: int,
    side: str,
) -> Tuple[
    Tuple[str, ...],
    Tuple[Matrix, ...],
    Tuple[Matrix, ...],
    Tuple[DSBasisExpression, ...],
    Dict[str, Matrix],
    Matrix,
    Matrix,
]:
    """Projection data with chosen [e,g]-witness preimages for one hook-pair side."""
    if side not in {"source", "target"}:
        raise ValueError("side must be 'source' or 'target'")
    source_triple, target_triple = type_a_hook_pair_sl2_triples(n, r)
    source_candidates, target_candidates = hook_pair_surviving_field_candidates(n, r)
    triple = source_triple if side == "source" else target_triple
    candidates = source_candidates if side == "source" else target_candidates
    basis_matrices = dict(standard_traceless_basis_sl_n(n))
    basis_order = tuple(label for label, _ in standard_traceless_basis_sl_n(n))
    candidate_labels = tuple(candidate.label for candidate in candidates)
    candidate_matrices = tuple(
        ds_basis_expression_matrix(candidate.source_terms, basis_matrices)
        for candidate in candidates
    )
    ad_e_basis, ad_e_witness_preimages = _ad_e_image_basis_matrices_with_witness_preimages(
        triple.e,
        basis_matrices,
    )
    decomposition_matrix = Matrix.hstack(
        *[_matrix_coordinate_column(entry, basis_order) for entry in ad_e_basis + candidate_matrices]
    )
    decomposition_inverse = decomposition_matrix.inv()
    return (
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        ad_e_witness_preimages,
        basis_matrices,
        decomposition_matrix,
        decomposition_inverse,
    )


def _split_hook_pair_matrix_to_survivors_with_witnesses(
    side: str,
    matrix: Matrix,
    n: int = 4,
    r: int = 1,
) -> Tuple[DSBasisExpression, LabeledLinearCombination, DSBasisExpression]:
    """Split a hook-pair matrix into survivor and [e,g]-witness pieces."""
    (
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        ad_e_witness_preimages,
        _basis_matrices,
        _decomposition_matrix,
        decomposition_inverse,
    ) = _hook_pair_projection_witness_data(n, r, side)
    basis_order = tuple(label for label, _ in standard_traceless_basis_sl_n(n))
    return _split_matrix_to_candidate_basis_with_witnesses(
        matrix,
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        ad_e_witness_preimages,
        basis_order,
        decomposition_inverse=decomposition_inverse,
    )


@lru_cache(maxsize=64)
def _hook_pair_projection_data(
    n: int,
    r: int,
    side: str,
) -> Tuple[Tuple[str, ...], Tuple[Matrix, ...], Tuple[Matrix, ...], Dict[str, Matrix], Matrix, Matrix]:
    """Projection data g = [e,g] ⊕ g^f for one side of a hook pair."""
    if side not in {"source", "target"}:
        raise ValueError("side must be 'source' or 'target'")
    source_triple, target_triple = type_a_hook_pair_sl2_triples(n, r)
    source_candidates, target_candidates = hook_pair_surviving_field_candidates(n, r)
    triple = source_triple if side == "source" else target_triple
    candidates = source_candidates if side == "source" else target_candidates
    basis_matrices = dict(standard_traceless_basis_sl_n(n))
    basis_order = tuple(label for label, _ in standard_traceless_basis_sl_n(n))
    candidate_labels = tuple(candidate.label for candidate in candidates)
    candidate_matrices = tuple(
        ds_basis_expression_matrix(candidate.source_terms, basis_matrices)
        for candidate in candidates
    )
    ad_e_basis = _ad_e_image_basis_matrices(triple.e, basis_matrices)
    decomposition_matrix = Matrix.hstack(
        *[_matrix_coordinate_column(entry, basis_order) for entry in ad_e_basis + candidate_matrices]
    )
    decomposition_inverse = decomposition_matrix.inv()
    return (
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        basis_matrices,
        decomposition_matrix,
        decomposition_inverse,
    )


@lru_cache(maxsize=64)
def _partition_pair_projection_data(
    partition: Tuple[int, ...],
    side: str,
) -> Tuple[Tuple[str, ...], Tuple[Matrix, ...], Tuple[Matrix, ...], Dict[str, Matrix], Matrix, Matrix]:
    """Projection data g = [e,g] ⊕ g^f for one side of a non-principal partition pair."""
    if side not in {"source", "target"}:
        raise ValueError("side must be 'source' or 'target'")
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_triple = type_a_partition_sl2_triple(case.partition)
    target_triple = type_a_partition_sl2_triple(case.dual_partition)
    source_candidates, target_candidates = partition_pair_surviving_field_candidates(case.partition)
    triple = source_triple if side == "source" else target_triple
    candidates = source_candidates if side == "source" else target_candidates
    basis_matrices = dict(standard_traceless_basis_sl_n(n))
    basis_order = tuple(label for label, _ in standard_traceless_basis_sl_n(n))
    candidate_labels = tuple(candidate.label for candidate in candidates)
    candidate_matrices = tuple(
        ds_basis_expression_matrix(candidate.source_terms, basis_matrices)
        for candidate in candidates
    )
    ad_e_basis = _ad_e_image_basis_matrices(triple.e, basis_matrices)
    decomposition_matrix = Matrix.hstack(
        *[_matrix_coordinate_column(entry, basis_order) for entry in ad_e_basis + candidate_matrices]
    )
    decomposition_inverse = decomposition_matrix.inv()
    return (
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        basis_matrices,
        decomposition_matrix,
        decomposition_inverse,
    )


@lru_cache(maxsize=64)
def _partition_pair_projection_witness_data(
    partition: Tuple[int, ...],
    side: str,
) -> Tuple[
    Tuple[str, ...],
    Tuple[Matrix, ...],
    Tuple[Matrix, ...],
    Tuple[DSBasisExpression, ...],
    Dict[str, Matrix],
    Matrix,
    Matrix,
]:
    """Projection data with chosen [e,g]-witness preimages for one partition-pair side."""
    if side not in {"source", "target"}:
        raise ValueError("side must be 'source' or 'target'")
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_triple = type_a_partition_sl2_triple(case.partition)
    target_triple = type_a_partition_sl2_triple(case.dual_partition)
    source_candidates, target_candidates = partition_pair_surviving_field_candidates(case.partition)
    triple = source_triple if side == "source" else target_triple
    candidates = source_candidates if side == "source" else target_candidates
    basis_matrices = dict(standard_traceless_basis_sl_n(n))
    basis_order = tuple(label for label, _ in standard_traceless_basis_sl_n(n))
    candidate_labels = tuple(candidate.label for candidate in candidates)
    candidate_matrices = tuple(
        ds_basis_expression_matrix(candidate.source_terms, basis_matrices)
        for candidate in candidates
    )
    ad_e_basis, ad_e_witness_preimages = _ad_e_image_basis_matrices_with_witness_preimages(
        triple.e,
        basis_matrices,
    )
    decomposition_matrix = Matrix.hstack(
        *[_matrix_coordinate_column(entry, basis_order) for entry in ad_e_basis + candidate_matrices]
    )
    decomposition_inverse = decomposition_matrix.inv()
    return (
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        ad_e_witness_preimages,
        basis_matrices,
        decomposition_matrix,
        decomposition_inverse,
    )


def _split_partition_pair_matrix_to_survivors_with_witnesses(
    partition: Tuple[int, ...],
    side: str,
    matrix: Matrix,
) -> Tuple[DSBasisExpression, LabeledLinearCombination, DSBasisExpression]:
    """Split a partition-pair matrix into survivor and [e,g]-witness pieces."""
    normalized_partition = normalize_partition(partition)
    (
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        ad_e_witness_preimages,
        _basis_matrices,
        _decomposition_matrix,
        decomposition_inverse,
    ) = _partition_pair_projection_witness_data(normalized_partition, side)
    n = partition_size(normalized_partition)
    basis_order = tuple(label for label, _ in standard_traceless_basis_sl_n(n))
    return _split_matrix_to_candidate_basis_with_witnesses(
        matrix,
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        ad_e_witness_preimages,
        basis_order,
        decomposition_inverse=decomposition_inverse,
    )


def _project_partition_pair_matrix_to_survivors(
    partition: Tuple[int, ...],
    side: str,
    matrix: Matrix,
) -> Dict[str, Rational]:
    """Project a partition-pair matrix to the survivor basis along [e,g]."""
    if side not in {"source", "target"}:
        raise ValueError("side must be 'source' or 'target'")
    normalized_partition = normalize_partition(partition)
    candidate_labels, candidate_matrices, ad_e_basis, _, _, decomposition_inverse = _partition_pair_projection_data(
        normalized_partition,
        side,
    )
    basis_order = tuple(label for label, _ in standard_traceless_basis_sl_n(partition_size(normalized_partition)))
    return _project_matrix_to_candidate_basis(
        matrix,
        candidate_labels,
        candidate_matrices,
        ad_e_basis,
        decomposition_inverse=decomposition_inverse,
        basis_order=basis_order,
    )


def _survivor_action_terms_from_projected_commutators(
    constraints: Tuple[DSConstraint, ...],
    candidates: Tuple[DSReducedFieldCandidate, ...],
    basis_matrices: Dict[str, Matrix],
    projector,
) -> Tuple[SurvivorActionTermEntry, ...]:
    """Induced c.rho action terms on survivor variables."""
    terms = []
    for constraint in constraints:
        positive_matrix = basis_matrices[constraint.current_label]
        for candidate in candidates:
            commutator = matrix_commutator(
                positive_matrix,
                ds_basis_expression_matrix(candidate.source_terms, basis_matrices),
            )
            for target_label, coefficient in projector(commutator).items():
                terms.append(
                    SurvivorActionTermEntry(
                        c_ghost=constraint.c_ghost,
                        source_survivor_label=candidate.label,
                        target_survivor_label=target_label,
                        coefficient=coefficient,
                    )
                )
    return tuple(terms)


def sl3_subregular_survivor_action_terms() -> Tuple[SurvivorActionTermEntry, ...]:
    """Induced c.rho action terms on the subregular survivor sector."""
    constraints = sl3_subregular_constraints()
    candidates = sl3_subregular_strong_generator_candidates()
    basis_matrices = sl3_subregular_basis_matrices()
    return _survivor_action_terms_from_projected_commutators(
        constraints,
        candidates,
        basis_matrices,
        lambda matrix: sl3_subregular_project_expression_to_strong_candidates(
            _sl3_subregular_matrix_to_basis_expression(matrix)
        ),
    )


def sl3_subregular_survivor_action_lift_witnesses(
) -> Tuple[SurvivorActionLiftWitness, ...]:
    """Explicit survivor-action lifts into projected and [e,sl_3]-witness parts."""
    constraints = sl3_subregular_constraints()
    candidates = sl3_subregular_strong_generator_candidates()
    basis_matrices = sl3_subregular_basis_matrices()
    entries = []
    for constraint in constraints:
        positive_matrix = basis_matrices[constraint.current_label]
        for candidate in candidates:
            commutator = matrix_commutator(
                positive_matrix,
                ds_basis_expression_matrix(candidate.source_terms, basis_matrices),
            )
            if commutator == zeros(3, 3):
                continue
            ad_e_terms, projected_terms = sl3_subregular_split_expression(
                _sl3_subregular_matrix_to_basis_expression(commutator)
            )
            entries.append(
                SurvivorActionLiftWitness(
                    c_ghost=constraint.c_ghost,
                    source_survivor_label=candidate.label,
                    projected_terms=projected_terms,
                    ad_e_image_terms=ad_e_terms,
                    ad_e_witness_preimage=sl3_subregular_expand_ad_e_terms_to_witness_preimage(
                        ad_e_terms
                    ),
                )
            )
    return tuple(entries)


@lru_cache(maxsize=64)
def hook_pair_survivor_action_terms(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorActionTermEntry, ...], Tuple[SurvivorActionTermEntry, ...]]:
    """Induced c.rho action terms on reduced survivor sectors for one hook pair."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_candidates, target_candidates = hook_pair_surviving_field_candidates(n, r)
    basis_matrices = dict(standard_traceless_basis_sl_n(n))
    return (
        _survivor_action_terms_from_projected_commutators(
            source_constraints,
            source_candidates,
            basis_matrices,
            lambda matrix: _project_hook_pair_matrix_to_survivors(
                "source",
                matrix,
                n=n,
                r=r,
            ),
        ),
        _survivor_action_terms_from_projected_commutators(
            target_constraints,
            target_candidates,
            basis_matrices,
            lambda matrix: _project_hook_pair_matrix_to_survivors(
                "target",
                matrix,
                n=n,
                r=r,
            ),
        ),
    )


@lru_cache(maxsize=64)
def partition_pair_survivor_action_terms(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorActionTermEntry, ...], Tuple[SurvivorActionTermEntry, ...]]:
    """Induced c.rho action terms on reduced survivor sectors for one partition pair."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_constraints, target_constraints = partition_pair_constraints(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_candidates, target_candidates = partition_pair_surviving_field_candidates(case.partition)
    basis_matrices = dict(standard_traceless_basis_sl_n(n))
    return (
        _survivor_action_terms_from_projected_commutators(
            source_constraints,
            source_candidates,
            basis_matrices,
            lambda matrix: _project_partition_pair_matrix_to_survivors(
                case.partition,
                "source",
                matrix,
            ),
        ),
        _survivor_action_terms_from_projected_commutators(
            target_constraints,
            target_candidates,
            basis_matrices,
            lambda matrix: _project_partition_pair_matrix_to_survivors(
                case.partition,
                "target",
                matrix,
            ),
        ),
    )


@lru_cache(maxsize=64)
def partition_pair_survivor_action_lift_witnesses(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorActionLiftWitness, ...], Tuple[SurvivorActionLiftWitness, ...]]:
    """Explicit survivor-action lifts for one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_constraints, target_constraints = partition_pair_constraints(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_candidates, target_candidates = partition_pair_surviving_field_candidates(case.partition)
    basis_matrices = dict(standard_traceless_basis_sl_n(n))

    def build_side(
        side: str,
        constraints: Tuple[DSConstraint, ...],
        candidates: Tuple[DSReducedFieldCandidate, ...],
    ) -> Tuple[SurvivorActionLiftWitness, ...]:
        entries = []
        for constraint in constraints:
            positive_matrix = basis_matrices[constraint.current_label]
            for candidate in candidates:
                commutator = matrix_commutator(
                    positive_matrix,
                    ds_basis_expression_matrix(candidate.source_terms, basis_matrices),
                )
                if commutator == zeros(n, n):
                    continue
                ad_e_terms, projected_terms, witness_preimage = (
                    _split_partition_pair_matrix_to_survivors_with_witnesses(
                        case.partition,
                        side,
                        commutator,
                    )
                )
                entries.append(
                    SurvivorActionLiftWitness(
                        c_ghost=constraint.c_ghost,
                        source_survivor_label=candidate.label,
                        projected_terms=projected_terms,
                        ad_e_image_terms=ad_e_terms,
                        ad_e_witness_preimage=witness_preimage,
                    )
                )
        return tuple(entries)

    return (
        build_side("source", source_constraints, source_candidates),
        build_side("target", target_constraints, target_candidates),
    )


@lru_cache(maxsize=64)
def partition_pair_constraint_current_witnesses(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Dict[str, DSBasisExpression], Dict[str, DSBasisExpression]]:
    """Chosen witness preimages for exact constrained currents in one partition pair."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_constraints, target_constraints = partition_pair_constraints(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    basis_matrices = dict(standard_traceless_basis_sl_n(n))

    def build_side(
        side: str,
        constraints: Tuple[DSConstraint, ...],
    ) -> Dict[str, DSBasisExpression]:
        witnesses: Dict[str, DSBasisExpression] = {}
        for constraint in constraints:
            _ad_e_terms, projected_terms, witness_preimage = (
                _split_partition_pair_matrix_to_survivors_with_witnesses(
                    case.partition,
                    side,
                    basis_matrices[constraint.current_label],
                )
            )
            if not projected_terms:
                witnesses[constraint.current_label] = witness_preimage
        return witnesses

    return (
        build_side("source", source_constraints),
        build_side("target", target_constraints),
    )


def first_nonselfdual_hook_pair_survivor_action_terms(
) -> Tuple[Tuple[SurvivorActionTermEntry, ...], Tuple[SurvivorActionTermEntry, ...]]:
    """Induced c.rho action terms on the reduced survivor sectors of the first hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_survivor_action_terms(
        4,
        1,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


@lru_cache(maxsize=64)
def hook_pair_survivor_action_lift_witnesses(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorActionLiftWitness, ...], Tuple[SurvivorActionLiftWitness, ...]]:
    """Explicit survivor-action lifts into projected and [e,g]-witness pieces for one hook pair."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_candidates, target_candidates = hook_pair_surviving_field_candidates(n, r)
    basis_matrices = dict(standard_traceless_basis_sl_n(n))

    def build_side(
        side: str,
        constraints: Tuple[DSConstraint, ...],
        candidates: Tuple[DSReducedFieldCandidate, ...],
    ) -> Tuple[SurvivorActionLiftWitness, ...]:
        entries = []
        for constraint in constraints:
            positive_matrix = basis_matrices[constraint.current_label]
            for candidate in candidates:
                commutator = matrix_commutator(
                    positive_matrix,
                    ds_basis_expression_matrix(candidate.source_terms, basis_matrices),
                )
                if commutator == zeros(n, n):
                    continue
                ad_e_terms, projected_terms, witness_preimage = (
                    _split_hook_pair_matrix_to_survivors_with_witnesses(
                        side,
                        commutator,
                        n=n,
                        r=r,
                    )
                )
                entries.append(
                    SurvivorActionLiftWitness(
                        c_ghost=constraint.c_ghost,
                        source_survivor_label=candidate.label,
                        projected_terms=projected_terms,
                        ad_e_image_terms=ad_e_terms,
                        ad_e_witness_preimage=witness_preimage,
                    )
                )
        return tuple(entries)

    return (
        build_side("source", source_constraints, source_candidates),
        build_side("target", target_constraints, target_candidates),
    )


def first_nonselfdual_hook_pair_survivor_action_lift_witnesses(
) -> Tuple[Tuple[SurvivorActionLiftWitness, ...], Tuple[SurvivorActionLiftWitness, ...]]:
    """Explicit survivor-action lifts for the first non-self-dual hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_survivor_action_lift_witnesses(
        4,
        1,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


@lru_cache(maxsize=64)
def hook_pair_constraint_current_witnesses(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Dict[str, DSBasisExpression], Dict[str, DSBasisExpression]]:
    """Chosen witness preimages for constrained hook-pair currents in [e,g]."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    basis_matrices = dict(standard_traceless_basis_sl_n(n))

    def build_side(
        side: str,
        constraints: Tuple[DSConstraint, ...],
    ) -> Dict[str, DSBasisExpression]:
        witnesses: Dict[str, DSBasisExpression] = {}
        for constraint in constraints:
            _ad_e_terms, projected_terms, witness_preimage = (
                _split_hook_pair_matrix_to_survivors_with_witnesses(
                    side,
                    basis_matrices[constraint.current_label],
                    n=n,
                    r=r,
                )
            )
            if projected_terms:
                raise ValueError(
                    f"{constraint.current_label} is not purely ad_e-exact on the {side} side"
                )
            witnesses[constraint.current_label] = witness_preimage
        return witnesses

    return (
        build_side("source", source_constraints),
        build_side("target", target_constraints),
    )


def first_nonselfdual_hook_pair_constraint_current_witnesses(
) -> Tuple[Dict[str, DSBasisExpression], Dict[str, DSBasisExpression]]:
    """Chosen witness preimages for the constrained currents of the first hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_constraint_current_witnesses(
        4,
        1,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def internal_survivor_ghost_labels(
    survivor_labels: Tuple[str, ...],
) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    """Ghost labels for the internal reduced-survivor CE sector."""
    return (
        tuple(f"c_survivor_{label}" for label in survivor_labels),
        tuple(f"b_survivor_{label}" for label in survivor_labels),
    )


def internal_survivor_quadratic_ghost_terms(
    survivor_labels: Tuple[str, ...],
    reduced_brackets: Dict[Tuple[str, str], Dict[str, object]],
) -> Tuple[QuadraticGhostTermEntry, ...]:
    """Quadratic CE ghost terms induced by the reduced survivor bracket."""
    c_ghost_labels, b_ghost_labels = internal_survivor_ghost_labels(survivor_labels)
    c_ghost_by_label = dict(zip(survivor_labels, c_ghost_labels))
    b_ghost_by_label = dict(zip(survivor_labels, b_ghost_labels))
    terms = []
    for left_index, left in enumerate(survivor_labels):
        for right in survivor_labels[left_index + 1 :]:
            for target, coefficient in reduced_brackets.get((left, right), {}).items():
                terms.append(
                    QuadraticGhostTermEntry(
                        left_c_ghost=c_ghost_by_label[left],
                        right_c_ghost=c_ghost_by_label[right],
                        target_b_ghost=b_ghost_by_label[target],
                        coefficient=sympify(coefficient),
                    )
                )
    return tuple(terms)


def internal_survivor_action_terms(
    survivor_labels: Tuple[str, ...],
    reduced_brackets: Dict[Tuple[str, str], Dict[str, object]],
) -> Tuple[SurvivorActionTermEntry, ...]:
    """Adjoint-action terms of the reduced survivor algebra on itself."""
    c_ghost_labels, _ = internal_survivor_ghost_labels(survivor_labels)
    c_ghost_by_label = dict(zip(survivor_labels, c_ghost_labels))
    terms = []
    for left in survivor_labels:
        for right in survivor_labels:
            for target, coefficient in reduced_brackets.get((left, right), {}).items():
                terms.append(
                    SurvivorActionTermEntry(
                        c_ghost=c_ghost_by_label[left],
                        source_survivor_label=right,
                        target_survivor_label=target,
                        coefficient=sympify(coefficient),
                    )
                )
    return tuple(terms)


def _add_linear_combination(
    target: Dict[str, object],
    source: Dict[str, object],
    scale=1,
) -> None:
    """Accumulate one labeled linear combination into another."""
    scalar = sympify(scale)
    for label, coefficient in source.items():
        updated = simplify(target.get(label, 0) + scalar * sympify(coefficient))
        if updated == 0:
            target.pop(label, None)
        else:
            target[label] = updated


def _survivor_action_by_c_ghost(
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
) -> Dict[str, Dict[str, Dict[str, object]]]:
    """Action maps grouped by external c-ghost and source survivor label."""
    action: Dict[str, Dict[str, Dict[str, object]]] = {}
    for item in survivor_action_terms:
        ghost_action = action.setdefault(item.c_ghost, {})
        image = ghost_action.setdefault(item.source_survivor_label, {})
        image[item.target_survivor_label] = simplify(
            image.get(item.target_survivor_label, 0) + sympify(item.coefficient)
        )
    return action


@lru_cache(maxsize=256)
def _indexed_survivor_action_by_source_and_c_ghost(
    survivor_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
) -> Dict[int, Dict[int, Tuple[Tuple[int, object], ...]]]:
    """Grouped survivor action with source/ghost/target labels resolved to indices."""
    survivor_index = {label: index for index, label in enumerate(survivor_labels)}
    c_index = _ghost_label_index_map(c_ghost_labels)
    grouped: Dict[int, Dict[int, Dict[int, object]]] = {}
    for item in survivor_action_terms:
        source = survivor_index[item.source_survivor_label]
        ghost = c_index[item.c_ghost]
        target = survivor_index[item.target_survivor_label]
        source_group = grouped.setdefault(source, {})
        target_group = source_group.setdefault(ghost, {})
        target_group[target] = simplify(
            target_group.get(target, 0) + sympify(item.coefficient)
        )
    return {
        source: {
            ghost: tuple(
                (target, coefficient)
                for target, coefficient in sorted(target_group.items())
                if coefficient != 0
            )
            for ghost, target_group in ghost_groups.items()
        }
        for source, ghost_groups in grouped.items()
    }


@lru_cache(maxsize=256)
def _indexed_current_action_terms(
    shifted_current_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    b_ghost_labels: Tuple[str, ...],
    current_action_terms: Tuple[CurrentActionTermEntry, ...],
) -> Dict[int, Tuple[Tuple[int, int, int, int, object], ...]]:
    """Current-action terms grouped by c-ghost with root labels resolved to indices."""
    c_index = _ghost_label_index_map(c_ghost_labels)
    u_index = {_label_root(label): index for index, label in enumerate(shifted_current_labels)}
    b_index = {_label_root(label): index for index, label in enumerate(b_ghost_labels)}
    grouped: Dict[int, Dict[Tuple[int, int, int, int], object]] = {}
    for item in current_action_terms:
        ghost = c_index[item.c_ghost]
        key = (
            u_index[item.source_root_label],
            u_index[item.target_root_label],
            b_index[item.source_root_label],
            b_index[item.target_root_label],
        )
        ghost_group = grouped.setdefault(ghost, {})
        ghost_group[key] = simplify(ghost_group.get(key, 0) + sympify(item.coefficient))
    return {
        ghost: tuple(
            (source_u, target_u, source_b, target_b, coefficient)
            for (source_u, target_u, source_b, target_b), coefficient in sorted(action_group.items())
            if coefficient != 0
        )
        for ghost, action_group in grouped.items()
    }


@lru_cache(maxsize=512)
def _monomial_nonzero_entries(monomial: Tuple[int, ...]) -> Tuple[Tuple[int, int], ...]:
    """Indices and exponents of nonzero monomial entries."""
    return tuple((index, exponent) for index, exponent in enumerate(monomial) if exponent)


@lru_cache(maxsize=512)
def _retarget_monomial(
    monomial: Tuple[int, ...],
    source_index: int,
    target_index: int,
) -> Tuple[int, ...]:
    """Move one unit of monomial weight from source to target."""
    target = list(monomial)
    target[source_index] -= 1
    target[target_index] += 1
    return tuple(target)


def _apply_survivor_action_to_linear_combination(
    action_by_source: Dict[str, Dict[str, object]],
    combination: Dict[str, object],
) -> Dict[str, object]:
    """Apply a grouped survivor action to a labeled linear combination."""
    result: Dict[str, object] = {}
    for source_label, source_coefficient in combination.items():
        _add_linear_combination(
            result,
            action_by_source.get(source_label, {}),
            scale=source_coefficient,
        )
    return result


def combine_survivor_action_terms(
    *term_sets: Tuple[SurvivorActionTermEntry, ...],
) -> Tuple[SurvivorActionTermEntry, ...]:
    """Combine survivor-action terms with coefficient collection."""
    coefficients: Dict[Tuple[str, str, str], object] = {}
    ordered_keys: list[Tuple[str, str, str]] = []
    for term_set in term_sets:
        for item in term_set:
            key = (
                item.c_ghost,
                item.source_survivor_label,
                item.target_survivor_label,
            )
            if key not in coefficients:
                ordered_keys.append(key)
            coefficients[key] = simplify(
                coefficients.get(key, 0) + sympify(item.coefficient)
            )
    return tuple(
        SurvivorActionTermEntry(
            c_ghost=c_ghost,
            source_survivor_label=source_survivor_label,
            target_survivor_label=target_survivor_label,
            coefficient=simplify(coefficients[(c_ghost, source_survivor_label, target_survivor_label)]),
        )
        for c_ghost, source_survivor_label, target_survivor_label in ordered_keys
        if simplify(coefficients[(c_ghost, source_survivor_label, target_survivor_label)]) != 0
    )


def first_transfer_correction_witnesses_from_exact_constraints(
    constraints: Tuple[DSConstraint, ...],
    survivor_action_lift_witnesses: Tuple[SurvivorActionLiftWitness, ...],
    exact_current_witnesses: Dict[str, DSBasisExpression],
) -> Tuple[FirstTransferCorrectionWitness, ...]:
    """First-transfer witness package for action terms induced by ad_e-exact currents."""
    current_label_by_ghost = {
        item.c_ghost: item.current_label
        for item in constraints
        if item.current_label in exact_current_witnesses
    }
    return tuple(
        FirstTransferCorrectionWitness(
            c_ghost=item.c_ghost,
            current_label=current_label_by_ghost[item.c_ghost],
            current_witness_preimage=exact_current_witnesses[
                current_label_by_ghost[item.c_ghost]
            ],
            source_survivor_label=item.source_survivor_label,
            projected_action_terms=item.projected_terms,
            action_witness_preimage=item.ad_e_witness_preimage,
            correction_terms=tuple(
                (label, simplify(-sympify(coefficient)))
                for label, coefficient in item.projected_terms
            ),
        )
        for item in survivor_action_lift_witnesses
        if item.c_ghost in current_label_by_ghost and item.projected_terms
    )


def first_transfer_correction_terms_from_witnesses(
    correction_witnesses: Tuple[FirstTransferCorrectionWitness, ...],
) -> Tuple[SurvivorActionTermEntry, ...]:
    """Flatten first-transfer witness data back to survivor-action correction terms."""
    return tuple(
        SurvivorActionTermEntry(
            c_ghost=item.c_ghost,
            source_survivor_label=item.source_survivor_label,
            target_survivor_label=target_survivor_label,
            coefficient=simplify(coefficient),
        )
        for item in correction_witnesses
        for target_survivor_label, coefficient in item.correction_terms
    )


def _linear_combination_bracket(
    left: Dict[str, object],
    right: Dict[str, object],
    reduced_brackets: Dict[Tuple[str, str], Dict[str, object]],
) -> Dict[str, object]:
    """Bracket of two labeled linear combinations in the reduced survivor algebra."""
    result: Dict[str, object] = {}
    for left_label, left_coefficient in left.items():
        for right_label, right_coefficient in right.items():
            _add_linear_combination(
                result,
                reduced_brackets.get((left_label, right_label), {}),
                scale=sympify(left_coefficient) * sympify(right_coefficient),
            )
    return result


def survivor_action_derivation_defects(
    survivor_labels: Tuple[str, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    reduced_brackets: Dict[Tuple[str, str], Dict[str, object]],
) -> Dict[str, Dict[Tuple[str, str], Dict[str, object]]]:
    """Defect of the positive-sector survivor action from being a derivation of the reduced bracket."""
    action_by_ghost = _survivor_action_by_c_ghost(survivor_action_terms)
    defects: Dict[str, Dict[Tuple[str, str], Dict[str, object]]] = {}
    for c_ghost, action_by_source in action_by_ghost.items():
        ghost_defects: Dict[Tuple[str, str], Dict[str, object]] = {}
        for left in survivor_labels:
            for right in survivor_labels:
                rho_bracket = _apply_survivor_action_to_linear_combination(
                    action_by_source,
                    reduced_brackets.get((left, right), {}),
                )
                derivation_term: Dict[str, object] = {}
                _add_linear_combination(
                    derivation_term,
                    _linear_combination_bracket(
                        action_by_source.get(left, {}),
                        {right: 1},
                        reduced_brackets,
                    ),
                )
                _add_linear_combination(
                    derivation_term,
                    _linear_combination_bracket(
                        {left: 1},
                        action_by_source.get(right, {}),
                        reduced_brackets,
                    ),
                )
                defect = dict(rho_bracket)
                _add_linear_combination(defect, derivation_term, scale=-1)
                if defect:
                    ghost_defects[(left, right)] = defect
        if ghost_defects:
            defects[c_ghost] = ghost_defects
    return defects


def sl3_subregular_derivation_defect_witnesses(
) -> Tuple[SurvivorDerivationDefectWitness, ...]:
    """Explicit unreduced witness formulas for the subregular derivation defects."""
    basis_matrices = sl3_subregular_basis_matrices()
    e_matrix = basis_matrices[sl3_subregular_sl2_triple().e]
    candidates = sl3_subregular_strong_generator_candidates()
    candidate_order = tuple(item.label for item in candidates)
    candidate_matrices = {
        item.label: ds_basis_expression_matrix(item.source_terms, basis_matrices)
        for item in candidates
    }
    witness_by_ghost: Dict[str, Dict[str, DSBasisExpression]] = {}
    for item in sl3_subregular_survivor_action_lift_witnesses():
        ghost_map = witness_by_ghost.setdefault(item.c_ghost, {})
        ghost_map[item.source_survivor_label] = item.ad_e_witness_preimage

    entries = []
    for c_ghost, ghost_defects in sl3_subregular_survivor_derivation_defects().items():
        ghost_witnesses = witness_by_ghost.get(c_ghost, {})
        for (left_label, right_label), defect_terms in ghost_defects.items():
            left_witness = ghost_witnesses.get(left_label, ())
            right_witness = ghost_witnesses.get(right_label, ())
            unreduced = -matrix_commutator(
                ds_basis_expression_matrix(left_witness, basis_matrices),
                matrix_commutator(e_matrix, candidate_matrices[right_label]),
            ) - matrix_commutator(
                matrix_commutator(e_matrix, candidate_matrices[left_label]),
                ds_basis_expression_matrix(right_witness, basis_matrices),
            )
            unreduced_expression = _sl3_subregular_matrix_to_basis_expression(unreduced)
            projected_terms = _labeled_linear_combination(
                sl3_subregular_project_expression_to_strong_candidates(
                    unreduced_expression
                ),
                candidate_order,
            )
            entries.append(
                SurvivorDerivationDefectWitness(
                    c_ghost=c_ghost,
                    left_survivor_label=left_label,
                    right_survivor_label=right_label,
                    left_action_witness_preimage=left_witness,
                    right_action_witness_preimage=right_witness,
                    unreduced_expression=unreduced_expression,
                    projected_defect_terms=projected_terms,
                )
            )
    return tuple(entries)


def sl3_subregular_survivor_derivation_defects(
) -> Dict[str, Dict[Tuple[str, str], Dict[str, object]]]:
    """Derivation defects for the subregular sl_3 positive action on the reduced survivor bracket."""
    survivors = sl3_subregular_strong_generator_candidates()
    return survivor_action_derivation_defects(
        tuple(item.label for item in survivors),
        sl3_subregular_survivor_action_terms(),
        sl3_subregular_projected_strong_brackets(),
    )


def sl3_subregular_first_transfer_correction_terms(
) -> Tuple[SurvivorActionTermEntry, ...]:
    """First transferred correction from the ad_e-exact positive generators."""
    return first_transfer_correction_terms_from_witnesses(
        sl3_subregular_first_transfer_correction_witnesses()
    )


def sl3_subregular_first_transfer_correction_witnesses(
) -> Tuple[FirstTransferCorrectionWitness, ...]:
    """Explicit first-transfer witnesses for the subregular control case."""
    return first_transfer_correction_witnesses_from_exact_constraints(
        sl3_subregular_constraints(),
        sl3_subregular_survivor_action_lift_witnesses(),
        sl3_subregular_ad_e_image_witnesses(),
    )


def sl3_subregular_corrected_survivor_action_terms(
) -> Tuple[SurvivorActionTermEntry, ...]:
    """Naive subregular action plus the first transferred correction."""
    return combine_survivor_action_terms(
        sl3_subregular_survivor_action_terms(),
        sl3_subregular_first_transfer_correction_terms(),
    )


def sl3_subregular_corrected_survivor_derivation_defects(
) -> Dict[str, Dict[Tuple[str, str], Dict[str, object]]]:
    """Derivation defects after the first transferred subregular correction."""
    survivors = sl3_subregular_strong_generator_candidates()
    return survivor_action_derivation_defects(
        tuple(item.label for item in survivors),
        sl3_subregular_corrected_survivor_action_terms(),
        sl3_subregular_projected_strong_brackets(),
    )


def solve_survivor_derivation_correction_for_ghost(
    c_ghost: str,
    survivor_labels: Tuple[str, ...],
    reduced_brackets: Dict[Tuple[str, str], Dict[str, object]],
    ghost_defects: Dict[Tuple[str, str], Dict[str, object]],
) -> Tuple[SurvivorActionTermEntry, ...]:
    """Solve the first-order derivation-coboundary equation for one ghost."""
    unknown_keys = [
        (source_label, target_label)
        for source_label in survivor_labels
        for target_label in survivor_labels
    ]
    rows = []
    rhs = []
    for left_label in survivor_labels:
        for right_label in survivor_labels:
            for target_label in survivor_labels:
                row = []
                for source_label, image_label in unknown_keys:
                    coefficient = Rational(0)
                    for bracket_label, bracket_coefficient in reduced_brackets[
                        (left_label, right_label)
                    ].items():
                        if bracket_label == source_label and image_label == target_label:
                            coefficient += sympify(bracket_coefficient)
                    if source_label == left_label:
                        for bracket_label, bracket_coefficient in reduced_brackets[
                            (image_label, right_label)
                        ].items():
                            if bracket_label == target_label:
                                coefficient -= sympify(bracket_coefficient)
                    if source_label == right_label:
                        for bracket_label, bracket_coefficient in reduced_brackets[
                            (left_label, image_label)
                        ].items():
                            if bracket_label == target_label:
                                coefficient -= sympify(bracket_coefficient)
                    row.append(simplify(coefficient))
                constant_term = -sympify(
                    ghost_defects.get((left_label, right_label), {}).get(target_label, 0)
                )
                if any(entry != 0 for entry in row) or constant_term != 0:
                    rows.append(row)
                    rhs.append(constant_term)
    if not rows:
        return ()

    matrix = Matrix(rows)
    vector = Matrix(rhs)
    if matrix.rank() != matrix.row_join(vector).rank():
        raise ValueError(f"no derivation correction exists for {c_ghost}")
    solution, parameters = matrix.gauss_jordan_solve(vector)
    parameter_substitution = {parameter: 0 for parameter in parameters}
    return tuple(
        SurvivorActionTermEntry(
            c_ghost=c_ghost,
            source_survivor_label=source_label,
            target_survivor_label=target_label,
            coefficient=simplify(solution[index, 0].subs(parameter_substitution)),
        )
        for index, (source_label, target_label) in enumerate(unknown_keys)
        if simplify(solution[index, 0].subs(parameter_substitution)) != 0
    )


def solve_survivor_derivation_correction_terms(
    survivor_labels: Tuple[str, ...],
    reduced_brackets: Dict[Tuple[str, str], Dict[str, object]],
    derivation_defects: Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
) -> Tuple[SurvivorActionTermEntry, ...]:
    """Solve the first transferred survivor correction for every active ghost."""
    return tuple(
        item
        for c_ghost, ghost_defects in derivation_defects.items()
        for item in solve_survivor_derivation_correction_for_ghost(
            c_ghost,
            survivor_labels,
            reduced_brackets,
            ghost_defects,
        )
    )


def hook_pair_survivor_derivation_defects(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
]:
    """Derivation defects for the reduced survivor actions on one hook pair."""
    source_survivors, target_survivors = hook_pair_surviving_field_candidates(n, r)
    source_actions, target_actions = hook_pair_survivor_action_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_brackets, target_brackets = hook_pair_reduced_brackets(n, r)
    return (
        survivor_action_derivation_defects(
            tuple(item.label for item in source_survivors),
            source_actions,
            source_brackets,
        ),
        survivor_action_derivation_defects(
            tuple(item.label for item in target_survivors),
            target_actions,
            target_brackets,
        ),
    )


@lru_cache(maxsize=64)
def partition_pair_survivor_derivation_defects(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
]:
    """Derivation defects for reduced survivor actions on one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    source_survivors, target_survivors = partition_pair_surviving_field_candidates(case.partition)
    source_actions, target_actions = partition_pair_survivor_action_terms(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_brackets, target_brackets = partition_pair_reduced_brackets(case.partition)
    return (
        survivor_action_derivation_defects(
            tuple(item.label for item in source_survivors),
            source_actions,
            source_brackets,
        ),
        survivor_action_derivation_defects(
            tuple(item.label for item in target_survivors),
            target_actions,
            target_brackets,
        ),
    )


@lru_cache(maxsize=64)
def partition_pair_first_transfer_correction_terms(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorActionTermEntry, ...], Tuple[SurvivorActionTermEntry, ...]]:
    """First transferred survivor corrections for one partition pair."""
    source_witnesses, target_witnesses = partition_pair_first_transfer_correction_witnesses(
        partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        first_transfer_correction_terms_from_witnesses(source_witnesses),
        first_transfer_correction_terms_from_witnesses(target_witnesses),
    )


@lru_cache(maxsize=64)
def partition_pair_first_transfer_correction_witnesses(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[
    Tuple[FirstTransferCorrectionWitness, ...],
    Tuple[FirstTransferCorrectionWitness, ...],
]:
    """Explicit first-transfer witnesses for one partition pair."""
    case = nonprincipal_type_a_case(partition)
    source_constraints, target_constraints = partition_pair_constraints(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_action_lifts, target_action_lifts = partition_pair_survivor_action_lift_witnesses(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_current_witnesses, target_current_witnesses = (
        partition_pair_constraint_current_witnesses(
            case.partition,
            source_num_constraints=source_num_constraints,
            target_num_constraints=target_num_constraints,
        )
    )
    return (
        first_transfer_correction_witnesses_from_exact_constraints(
            source_constraints,
            source_action_lifts,
            source_current_witnesses,
        ),
        first_transfer_correction_witnesses_from_exact_constraints(
            target_constraints,
            target_action_lifts,
            target_current_witnesses,
        ),
    )


@lru_cache(maxsize=64)
def partition_pair_corrected_survivor_action_terms(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorActionTermEntry, ...], Tuple[SurvivorActionTermEntry, ...]]:
    """Naive partition-pair survivor actions plus the first transferred correction."""
    source_naive, target_naive = partition_pair_survivor_action_terms(
        partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_correction, target_correction = partition_pair_first_transfer_correction_terms(
        partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        combine_survivor_action_terms(source_naive, source_correction),
        combine_survivor_action_terms(target_naive, target_correction),
    )


@lru_cache(maxsize=64)
def partition_pair_corrected_survivor_derivation_defects(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
]:
    """Derivation defects after the first transferred correction on one partition pair."""
    case = nonprincipal_type_a_case(partition)
    source_survivors, target_survivors = partition_pair_surviving_field_candidates(case.partition)
    source_brackets, target_brackets = partition_pair_reduced_brackets(case.partition)
    source_corrected, target_corrected = partition_pair_corrected_survivor_action_terms(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        survivor_action_derivation_defects(
            tuple(item.label for item in source_survivors),
            source_corrected,
            source_brackets,
        ),
        survivor_action_derivation_defects(
            tuple(item.label for item in target_survivors),
            target_corrected,
            target_brackets,
        ),
    )


def first_nonselfdual_hook_pair_survivor_derivation_defects(
) -> Tuple[
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
]:
    """Derivation defects for the first non-self-dual hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_survivor_derivation_defects(
        4,
        1,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def hook_pair_derivation_defect_witnesses(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[
    Tuple[SurvivorDerivationDefectWitness, ...],
    Tuple[SurvivorDerivationDefectWitness, ...],
]:
    """Explicit unreduced witness formulas for hook-pair derivation defects."""
    source_triple, target_triple = type_a_hook_pair_sl2_triples(n, r)
    source_candidates, target_candidates = hook_pair_surviving_field_candidates(n, r)
    source_brackets, target_brackets = hook_pair_reduced_brackets(n, r)
    source_lifts, target_lifts = hook_pair_survivor_action_lift_witnesses(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_defects, target_defects = hook_pair_survivor_derivation_defects(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    basis_matrices = dict(standard_traceless_basis_sl_n(n))

    def build_side(
        side: str,
        e_matrix: Matrix,
        candidates: Tuple[DSReducedFieldCandidate, ...],
        reduced_brackets: Dict[Tuple[str, str], Dict[str, object]],
        action_lifts: Tuple[SurvivorActionLiftWitness, ...],
        derivation_defects: Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
    ) -> Tuple[SurvivorDerivationDefectWitness, ...]:
        candidate_order = tuple(item.label for item in candidates)
        candidate_matrices = {
            item.label: ds_basis_expression_matrix(item.source_terms, basis_matrices)
            for item in candidates
        }
        witness_by_ghost: Dict[str, Dict[str, DSBasisExpression]] = {}
        for item in action_lifts:
            ghost_map = witness_by_ghost.setdefault(item.c_ghost, {})
            ghost_map[item.source_survivor_label] = item.ad_e_witness_preimage
        entries = []
        for c_ghost, ghost_defects in derivation_defects.items():
            ghost_witnesses = witness_by_ghost.get(c_ghost, {})
            for (left_label, right_label), _defect_terms in ghost_defects.items():
                left_witness = ghost_witnesses.get(left_label, ())
                right_witness = ghost_witnesses.get(right_label, ())
                unreduced = -matrix_commutator(
                    ds_basis_expression_matrix(left_witness, basis_matrices),
                    matrix_commutator(e_matrix, candidate_matrices[right_label]),
                ) - matrix_commutator(
                    matrix_commutator(e_matrix, candidate_matrices[left_label]),
                    ds_basis_expression_matrix(right_witness, basis_matrices),
                )
                unreduced_expression = tuple(
                    (label, sympify(coefficient))
                    for label, coefficient in matrix_to_traceless_basis_expression_sl_n(
                        unreduced
                    )
                )
                projected_defect_terms = _labeled_linear_combination(
                    _project_hook_pair_matrix_to_survivors(
                        side,
                        unreduced,
                        n=n,
                        r=r,
                    ),
                    candidate_order,
                )
                entries.append(
                    SurvivorDerivationDefectWitness(
                        c_ghost=c_ghost,
                        left_survivor_label=left_label,
                        right_survivor_label=right_label,
                        left_action_witness_preimage=left_witness,
                        right_action_witness_preimage=right_witness,
                        unreduced_expression=unreduced_expression,
                        projected_defect_terms=projected_defect_terms,
                    )
                )
        return tuple(entries)

    return (
        build_side(
            "source",
            source_triple.e,
            source_candidates,
            source_brackets,
            source_lifts,
            source_defects,
        ),
        build_side(
            "target",
            target_triple.e,
            target_candidates,
            target_brackets,
            target_lifts,
            target_defects,
        ),
    )


def first_nonselfdual_hook_pair_derivation_defect_witnesses(
) -> Tuple[
    Tuple[SurvivorDerivationDefectWitness, ...],
    Tuple[SurvivorDerivationDefectWitness, ...],
]:
    """Explicit unreduced witness formulas for the first non-self-dual hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_derivation_defect_witnesses(
        4,
        1,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


@lru_cache(maxsize=64)
def hook_pair_first_transfer_correction_terms(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorActionTermEntry, ...], Tuple[SurvivorActionTermEntry, ...]]:
    """First transferred survivor corrections for one hook pair."""
    source_witnesses, target_witnesses = hook_pair_first_transfer_correction_witnesses(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        first_transfer_correction_terms_from_witnesses(source_witnesses),
        first_transfer_correction_terms_from_witnesses(target_witnesses),
    )


@lru_cache(maxsize=64)
def hook_pair_first_transfer_correction_witnesses(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[
    Tuple[FirstTransferCorrectionWitness, ...],
    Tuple[FirstTransferCorrectionWitness, ...],
]:
    """Explicit first-transfer witnesses for one hook pair."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_action_lifts, target_action_lifts = hook_pair_survivor_action_lift_witnesses(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_current_witnesses, target_current_witnesses = (
        hook_pair_constraint_current_witnesses(
            n,
            r,
            source_num_constraints=source_num_constraints,
            target_num_constraints=target_num_constraints,
        )
    )
    return (
        first_transfer_correction_witnesses_from_exact_constraints(
            source_constraints,
            source_action_lifts,
            source_current_witnesses,
        ),
        first_transfer_correction_witnesses_from_exact_constraints(
            target_constraints,
            target_action_lifts,
            target_current_witnesses,
        ),
    )


@lru_cache(maxsize=64)
def hook_pair_corrected_survivor_action_terms(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorActionTermEntry, ...], Tuple[SurvivorActionTermEntry, ...]]:
    """Naive hook-pair survivor actions plus the first transferred correction."""
    source_naive, target_naive = hook_pair_survivor_action_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_correction, target_correction = hook_pair_first_transfer_correction_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        combine_survivor_action_terms(source_naive, source_correction),
        combine_survivor_action_terms(target_naive, target_correction),
    )


def hook_pair_corrected_survivor_derivation_defects(
    n: int,
    r: int,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
]:
    """Derivation defects after the first transferred hook-pair correction."""
    source_survivors, target_survivors = hook_pair_surviving_field_candidates(n, r)
    source_brackets, target_brackets = hook_pair_reduced_brackets(n, r)
    source_corrected, target_corrected = hook_pair_corrected_survivor_action_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        survivor_action_derivation_defects(
            tuple(item.label for item in source_survivors),
            source_corrected,
            source_brackets,
        ),
        survivor_action_derivation_defects(
            tuple(item.label for item in target_survivors),
            target_corrected,
            target_brackets,
        ),
    )


def first_nonselfdual_hook_pair_first_transfer_correction_terms(
) -> Tuple[Tuple[SurvivorActionTermEntry, ...], Tuple[SurvivorActionTermEntry, ...]]:
    """First transferred survivor corrections for the first non-self-dual hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_first_transfer_correction_terms(
        4,
        1,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def first_nonselfdual_hook_pair_first_transfer_correction_witnesses(
) -> Tuple[
    Tuple[FirstTransferCorrectionWitness, ...],
    Tuple[FirstTransferCorrectionWitness, ...],
]:
    """Explicit first-transfer witnesses for the first non-self-dual hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_first_transfer_correction_witnesses(
        4,
        1,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def first_nonselfdual_hook_pair_corrected_survivor_action_terms(
) -> Tuple[Tuple[SurvivorActionTermEntry, ...], Tuple[SurvivorActionTermEntry, ...]]:
    """Corrected survivor actions for the first non-self-dual hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_corrected_survivor_action_terms(
        4,
        1,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def first_nonselfdual_hook_pair_corrected_survivor_derivation_defects(
) -> Tuple[
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
    Dict[str, Dict[Tuple[str, str], Dict[str, object]]],
]:
    """Derivation defects after the first transferred correction on the first hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_corrected_survivor_derivation_defects(
        4,
        1,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def sl3_subregular_constraint_character() -> Dict[str, Rational]:
    """DS character values on the constrained positive-graded roots."""
    return {
        "alpha1": Rational(1),
        "alpha1+alpha2": Rational(0),
    }


def sl3_subregular_constraints() -> Tuple[DSConstraint, ...]:
    """Linear constraints defining the sl_3 subregular DS seed."""
    character = sl3_subregular_constraint_character()
    return (
        DSConstraint(
            root_label="alpha1",
            current_label="E12",
            character_value=character["alpha1"],
            b_ghost="b_alpha1",
            c_ghost="c_alpha1",
        ),
        DSConstraint(
            root_label="alpha1+alpha2",
            current_label="E13",
            character_value=character["alpha1+alpha2"],
            b_ghost="b_alpha1+alpha2",
            c_ghost="c_alpha1+alpha2",
        ),
    )


def sl3_subregular_positive_nilpotent_brackets() -> Tuple[Tuple[str, str, str], ...]:
    """Nonzero brackets among constrained positive root directions.

    For the standard subregular grading, the constrained directions are
    `E12` and `E13`, and their bracket vanishes because `2*alpha1+alpha2`
    is not a root of `sl_3`.
    """
    return ()


def sl3_subregular_ds_seed(level=Symbol("k")) -> DSReductionSeed:
    """Seed DS record for the non-principal sl_3 subregular case."""
    k = sympify(level)
    return DSReductionSeed(
        lie_type="A",
        rank=2,
        partition=subregular_partition(3),
        sl2_triple=sl3_subregular_sl2_triple(),
        positive_grades=sl3_subregular_ghost_profile(),
        dual_level=bp_dual_level(k),
        expected_target="affine_sl2_seed",
        track=TRACK_FRONTIER_NONPRINCIPAL,
        status=STATUS_DS_SEED,
    )


def sl3_subregular_brst_blueprint(level=Symbol("k")) -> DSBRSTBlueprint:
    """Symbolic BRST-input package for the sl_3 subregular seed."""
    return DSBRSTBlueprint(
        seed=sl3_subregular_ds_seed(level),
        basis=sl3_subregular_basis_profile(),
        constraints=sl3_subregular_constraints(),
        positive_nilpotent_is_abelian=(sl3_subregular_positive_nilpotent_brackets() == ()),
        quadratic_ghost_term_present=False,
        expected_current_presentation=bp_current_presentation(),
        expected_strong_presentation=bp_strong_presentation(),
    )


def _basis_profile_from_h_matrix(h: Matrix) -> Tuple[DSBasisElement, ...]:
    """Standard traceless basis profile organized by ad(h)-grade."""
    graded_basis = ad_h_graded_basis_labels_sl_n(h)
    inverse_grades = {
        label: Rational(grade)
        for grade, labels in graded_basis.items()
        for label in labels
    }
    profile = []
    for label, _ in standard_traceless_basis_sl_n(h.rows):
        grade = inverse_grades[label]
        sector = "positive_grade" if grade > 0 else ("negative_grade" if grade < 0 else "neutral")
        profile.append(
            DSBasisElement(
                label=label,
                ad_h_grade=grade,
                sector=sector,
            )
        )
    return tuple(profile)


def first_nonselfdual_hook_pair_basis_profiles() -> Tuple[Tuple[DSBasisElement, ...], Tuple[DSBasisElement, ...]]:
    """Standard traceless basis profiles for the first non-self-dual hook pair."""
    source_triple, target_triple = first_nonselfdual_hook_pair_sl2_triples()
    return (
        _basis_profile_from_h_matrix(source_triple.h),
        _basis_profile_from_h_matrix(target_triple.h),
    )


def first_nonselfdual_hook_pair_brst_blueprints(
    level=Symbol("k"),
) -> Tuple[DSBRSTBlueprint, DSBRSTBlueprint]:
    """Symbolic BRST blueprints for the first non-self-dual hook pair."""
    seed = first_nonselfdual_hook_pair_ds_seed(level)
    source_constraints, target_constraints = first_nonselfdual_hook_pair_constraints()
    source_basis, target_basis = first_nonselfdual_hook_pair_basis_profiles()
    source_positive_brackets, target_positive_brackets = (
        first_nonselfdual_hook_pair_positive_nilpotent_brackets()
    )
    source_candidates, target_candidates = first_nonselfdual_hook_pair_surviving_field_candidates()
    source_blueprint = DSBRSTBlueprint(
        seed=DSReductionSeed(
            lie_type="A",
            rank=3,
            partition=seed.source_partition,
            sl2_triple=Sl2TripleSeed(e="source_e", h="source_h", f="source_f"),
            positive_grades=first_nonselfdual_hook_pair_ghost_profiles()[0],
            dual_level=seed.target_level,
            expected_target="hook_pair_source_survivor_seed",
            track=TRACK_FRONTIER_NONPRINCIPAL,
            status=STATUS_DS_SEED,
        ),
        basis=source_basis,
        constraints=source_constraints,
        positive_nilpotent_is_abelian=(source_positive_brackets == ()),
        quadratic_ghost_term_present=(source_positive_brackets != ()),
        expected_current_presentation=(),
        expected_strong_presentation=tuple(
            (candidate.label, candidate.conformal_weight, candidate.parity)
            for candidate in source_candidates
        ),
    )
    target_blueprint = DSBRSTBlueprint(
        seed=DSReductionSeed(
            lie_type="A",
            rank=3,
            partition=seed.target_partition,
            sl2_triple=Sl2TripleSeed(e="target_e", h="target_h", f="target_f"),
            positive_grades=first_nonselfdual_hook_pair_ghost_profiles()[1],
            dual_level=seed.source_level,
            expected_target="hook_pair_target_survivor_seed",
            track=TRACK_FRONTIER_NONPRINCIPAL,
            status=STATUS_DS_SEED,
        ),
        basis=target_basis,
        constraints=target_constraints,
        positive_nilpotent_is_abelian=(target_positive_brackets == ()),
        quadratic_ghost_term_present=(target_positive_brackets != ()),
        expected_current_presentation=(),
        expected_strong_presentation=tuple(
            (candidate.label, candidate.conformal_weight, candidate.parity)
            for candidate in target_candidates
        ),
    )
    return source_blueprint, target_blueprint


@lru_cache(maxsize=512)
def exterior_basis_indices(num_generators: int, degree: int) -> Tuple[Tuple[int, ...], ...]:
    """Ordered exterior basis in degree `degree` on `num_generators` symbols."""
    if degree < 0 or degree > num_generators:
        return ()
    return tuple(combinations(range(num_generators), degree))


@lru_cache(maxsize=512)
def _insert_ghost_index(
    basis: Tuple[int, ...],
    ghost_index: int,
) -> Tuple[int, Tuple[int, ...]] | None:
    """Insert one ghost index into a sorted exterior basis with the wedge sign."""
    if ghost_index in basis:
        return None
    insertion_position = sum(1 for value in basis if value < ghost_index)
    sign = -1 if insertion_position % 2 else 1
    return sign, tuple(sorted(basis + (ghost_index,)))


@lru_cache(maxsize=512)
def _remove_ghost_index(
    basis: Tuple[int, ...],
    ghost_index: int,
) -> Tuple[int, Tuple[int, ...]] | None:
    """Contract one ghost index from a sorted exterior basis with the Koszul sign."""
    if ghost_index not in basis:
        return None
    position = basis.index(ghost_index)
    sign = -1 if position % 2 else 1
    return sign, basis[:position] + basis[position + 1 :]


@lru_cache(maxsize=256)
def character_wedge_differential(
    num_ghosts: int,
    chi_vector: Tuple[object, ...],
    degree: int,
) -> Matrix:
    """Matrix of d = (sum chi_i c_i) wedge - on exterior degree `degree`."""
    source_basis = exterior_basis_indices(num_ghosts, degree)
    target_basis = exterior_basis_indices(num_ghosts, degree + 1)
    matrix = zeros(len(target_basis), len(source_basis))
    if not source_basis or not target_basis:
        return matrix

    target_index = {basis: row for row, basis in enumerate(target_basis)}

    for col, basis in enumerate(source_basis):
        for ghost_index in range(num_ghosts):
            inserted = _insert_ghost_index(basis, ghost_index)
            if inserted is None:
                continue
            sign, target = inserted
            row = target_index[target]
            matrix[row, col] += sign * sympify(chi_vector[ghost_index])

    return matrix


def _dual_c_ghost_label(target_b_ghost: str) -> str:
    """Map a BRST b-ghost label to the dual c-ghost label."""
    if not target_b_ghost.startswith("b_"):
        raise ValueError("target_b_ghost must begin with 'b_'")
    return "c_" + target_b_ghost[2:]


def _relabel_ghost_label(label: str, label_map: Dict[str, str]) -> str:
    """Relabel a c- or b-ghost by its root-label suffix."""
    return _relabel_ghost_label_with_side_map(label, label_map)


def _relabel_ghost_label_with_side_map(
    label: str,
    label_map: Dict[str, str],
    side_map: Dict[str, str] | None = None,
) -> str:
    """Relabel a c- or b-ghost by root label and, optionally, side tag."""
    parts = label.split("_", 2)
    if parts[0] not in {"b", "c"} or len(parts) < 2:
        raise ValueError("ghost label must begin with 'c_' or 'b_'")
    if len(parts) == 2:
        prefix, root_label = parts
        return f"{prefix}_{label_map[root_label]}"
    prefix, side, root_label = parts
    mapped_side = side_map.get(side, side) if side_map is not None else side
    return f"{prefix}_{mapped_side}_{label_map[root_label]}"


def relabel_quadratic_ghost_terms(
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    label_map: Dict[str, str],
    side_map: Dict[str, str] | None = None,
) -> Tuple[QuadraticGhostTermEntry, ...]:
    """Relabel the ghost fields appearing in quadratic BRST support."""
    return tuple(
        QuadraticGhostTermEntry(
            left_c_ghost=_relabel_ghost_label_with_side_map(
                item.left_c_ghost, label_map, side_map
            ),
            right_c_ghost=_relabel_ghost_label_with_side_map(
                item.right_c_ghost, label_map, side_map
            ),
            target_b_ghost=_relabel_ghost_label_with_side_map(
                item.target_b_ghost, label_map, side_map
            ),
            coefficient=item.coefficient,
        )
        for item in quadratic_terms
    )


def relabel_current_action_terms(
    current_action_terms: Tuple[CurrentActionTermEntry, ...],
    label_map: Dict[str, str],
    side_map: Dict[str, str] | None = None,
) -> Tuple[CurrentActionTermEntry, ...]:
    """Relabel current-action terms by root label and optional side tag."""
    return tuple(
        CurrentActionTermEntry(
            c_ghost=_relabel_ghost_label_with_side_map(item.c_ghost, label_map, side_map),
            source_root_label=label_map[item.source_root_label],
            target_root_label=label_map[item.target_root_label],
            coefficient=item.coefficient,
        )
        for item in current_action_terms
    )


def relabel_truncated_brst_complex(
    complex_seed: TruncatedBRSTComplex,
    label_map: Dict[str, str],
    side_map: Dict[str, str] | None = None,
    source_tag: str | None = None,
) -> TruncatedBRSTComplex:
    """Relabel a truncated ghost BRST complex by a root-label bijection."""
    tag = source_tag if source_tag is not None else f"{complex_seed.source_tag}_relabeled"
    mapped_ghost_labels = tuple(
        _relabel_ghost_label_with_side_map(label, label_map, side_map)
        for label in complex_seed.ghost_labels
    )
    mapped_quadratic_terms = relabel_quadratic_ghost_terms(
        complex_seed.quadratic_ghost_terms,
        label_map,
        side_map=side_map,
    )
    if mapped_quadratic_terms:
        return build_ghost_brst_complex(
            ghost_labels=mapped_ghost_labels,
            chi_vector=complex_seed.chi_vector,
            quadratic_terms=mapped_quadratic_terms,
            source_tag=tag,
        )
    return build_character_wedge_complex(
        ghost_labels=mapped_ghost_labels,
        chi_vector=complex_seed.chi_vector,
        source_tag=tag,
    )


def _relabel_shifted_current_label(
    label: str,
    label_map: Dict[str, str],
    side_map: Dict[str, str] | None = None,
) -> str:
    """Relabel a shifted-current label by root label and, optionally, side tag."""
    parts = label.split("_", 2)
    if parts[0] != "u" or len(parts) < 2:
        raise ValueError("shifted current label must begin with 'u_'")
    if len(parts) == 2:
        prefix, root_label = parts
        return f"{prefix}_{label_map[root_label]}"
    prefix, side, root_label = parts
    mapped_side = side_map.get(side, side) if side_map is not None else side
    return f"{prefix}_{mapped_side}_{label_map[root_label]}"


def relabel_mixed_constraint_ghost_block(
    block: MixedConstraintGhostBRSTBlock,
    label_map: Dict[str, str],
    side_map: Dict[str, str] | None = None,
    source_tag: str | None = None,
) -> MixedConstraintGhostBRSTBlock:
    """Relabel one mixed current-plus-ghost BRST block."""
    tag = source_tag if source_tag is not None else f"{block.source_tag}_relabeled"
    mapped_shifted_current_labels = tuple(
        _relabel_shifted_current_label(label, label_map, side_map)
        for label in block.shifted_current_labels
    )
    mapped_c_ghost_labels = tuple(
        _relabel_ghost_label_with_side_map(label, label_map, side_map)
        for label in block.c_ghost_labels
    )
    mapped_b_ghost_labels = tuple(
        _relabel_ghost_label_with_side_map(label, label_map, side_map)
        for label in block.b_ghost_labels
    )
    return build_mixed_constraint_ghost_brst_block(
        shifted_current_labels=mapped_shifted_current_labels,
        c_ghost_labels=mapped_c_ghost_labels,
        b_ghost_labels=mapped_b_ghost_labels,
        chi_vector=block.chi_vector,
        quadratic_terms=relabel_quadratic_ghost_terms(
            block.quadratic_ghost_terms,
            label_map,
            side_map=side_map,
        ),
        current_action_terms=relabel_current_action_terms(
            block.current_action_terms,
            label_map,
            side_map=side_map,
        ),
        constraint_total_degree=block.constraint_total_degree,
        source_tag=tag,
    )


def _relabel_survivor_label_with_side_map(
    label: str,
    side_map: Dict[str, str] | None = None,
) -> str:
    """Relabel a survivor label by side tag when present."""
    if "_" not in label:
        return label
    side, remainder = label.split("_", 1)
    mapped_side = side_map.get(side, side) if side_map is not None else side
    return f"{mapped_side}_{remainder}"


def _relabel_survivor_action_terms(
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    label_map: Dict[str, str],
    side_map: Dict[str, str] | None = None,
) -> Tuple[SurvivorActionTermEntry, ...]:
    """Relabel survivor-action terms by root label and optional side tag."""
    return tuple(
        SurvivorActionTermEntry(
            c_ghost=_relabel_ghost_label_with_side_map(item.c_ghost, label_map, side_map),
            source_survivor_label=_relabel_survivor_label_with_side_map(
                item.source_survivor_label,
                side_map=side_map,
            ),
            target_survivor_label=_relabel_survivor_label_with_side_map(
                item.target_survivor_label,
                side_map=side_map,
            ),
            coefficient=item.coefficient,
        )
        for item in survivor_action_terms
    )


def _relabel_internal_survivor_ghost_label(
    label: str,
    side_map: Dict[str, str] | None = None,
) -> str:
    """Relabel an internal survivor ghost label by survivor side tag."""
    parts = label.split("_", 2)
    if len(parts) != 3 or parts[0] not in {"b", "c"} or parts[1] != "survivor":
        raise ValueError("internal survivor ghost label must have form c_survivor_* or b_survivor_*")
    prefix, marker, survivor_label = parts
    mapped_survivor = _relabel_survivor_label_with_side_map(
        survivor_label,
        side_map=side_map,
    )
    return f"{prefix}_{marker}_{mapped_survivor}"


def _relabel_internal_quadratic_ghost_terms(
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    side_map: Dict[str, str] | None = None,
) -> Tuple[QuadraticGhostTermEntry, ...]:
    """Relabel internal CE quadratic ghost terms by survivor side tag."""
    return tuple(
        QuadraticGhostTermEntry(
            left_c_ghost=_relabel_internal_survivor_ghost_label(
                item.left_c_ghost,
                side_map=side_map,
            ),
            right_c_ghost=_relabel_internal_survivor_ghost_label(
                item.right_c_ghost,
                side_map=side_map,
            ),
            target_b_ghost=_relabel_internal_survivor_ghost_label(
                item.target_b_ghost,
                side_map=side_map,
            ),
            coefficient=item.coefficient,
        )
        for item in quadratic_terms
    )


def _relabel_internal_survivor_action_terms(
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    side_map: Dict[str, str] | None = None,
) -> Tuple[SurvivorActionTermEntry, ...]:
    """Relabel internal survivor-action terms by survivor side tag."""
    return tuple(
        SurvivorActionTermEntry(
            c_ghost=_relabel_internal_survivor_ghost_label(
                item.c_ghost,
                side_map=side_map,
            ),
            source_survivor_label=_relabel_survivor_label_with_side_map(
                item.source_survivor_label,
                side_map=side_map,
            ),
            target_survivor_label=_relabel_survivor_label_with_side_map(
                item.target_survivor_label,
                side_map=side_map,
            ),
            coefficient=item.coefficient,
        )
        for item in survivor_action_terms
    )


def _relabel_survivor_coupled_block(
    block: SurvivorCoupledBRSTBlock,
    label_map: Dict[str, str],
    side_map: Dict[str, str] | None = None,
    source_tag: str | None = None,
) -> SurvivorCoupledBRSTBlock:
    """Relabel one survivor-coupled BRST block."""
    tag = source_tag if source_tag is not None else f"{block.source_tag}_relabeled"
    mapped_shifted_current_labels = tuple(
        _relabel_shifted_current_label(label, label_map, side_map)
        for label in block.shifted_current_labels
    )
    mapped_survivor_labels = tuple(
        _relabel_survivor_label_with_side_map(label, side_map=side_map)
        for label in block.survivor_labels
    )
    mapped_c_ghost_labels = tuple(
        _relabel_ghost_label_with_side_map(label, label_map, side_map)
        for label in block.c_ghost_labels
    )
    mapped_b_ghost_labels = tuple(
        _relabel_ghost_label_with_side_map(label, label_map, side_map)
        for label in block.b_ghost_labels
    )
    return build_survivor_coupled_brst_block(
        shifted_current_labels=mapped_shifted_current_labels,
        survivor_labels=mapped_survivor_labels,
        c_ghost_labels=mapped_c_ghost_labels,
        b_ghost_labels=mapped_b_ghost_labels,
        chi_vector=block.chi_vector,
        quadratic_terms=relabel_quadratic_ghost_terms(
            block.quadratic_ghost_terms,
            label_map,
            side_map=side_map,
        ),
        current_action_terms=relabel_current_action_terms(
            block.current_action_terms,
            label_map,
            side_map=side_map,
        ),
        survivor_action_terms=_relabel_survivor_action_terms(
            block.survivor_action_terms,
            label_map,
            side_map=side_map,
        ),
        constraint_total_degree=block.constraint_total_degree,
        survivor_total_degree=block.survivor_total_degree,
        source_tag=tag,
    )


def _relabel_semidirect_survivor_block(
    block: SemidirectSurvivorBRSTBlock,
    label_map: Dict[str, str],
    side_map: Dict[str, str] | None = None,
    source_tag: str | None = None,
) -> SemidirectSurvivorBRSTBlock:
    """Relabel one semidirect survivor BRST block."""
    tag = source_tag if source_tag is not None else f"{block.source_tag}_relabeled"
    mapped_shifted_current_labels = tuple(
        _relabel_shifted_current_label(label, label_map, side_map)
        for label in block.shifted_current_labels
    )
    mapped_survivor_labels = tuple(
        _relabel_survivor_label_with_side_map(label, side_map=side_map)
        for label in block.survivor_labels
    )
    mapped_c_ghost_labels = tuple(
        _relabel_ghost_label_with_side_map(label, label_map, side_map)
        for label in block.c_ghost_labels
    )
    mapped_b_ghost_labels = tuple(
        _relabel_ghost_label_with_side_map(label, label_map, side_map)
        for label in block.b_ghost_labels
    )
    mapped_internal_c_ghost_labels = tuple(
        _relabel_internal_survivor_ghost_label(label, side_map=side_map)
        for label in block.internal_c_ghost_labels
    )
    mapped_internal_b_ghost_labels = tuple(
        _relabel_internal_survivor_ghost_label(label, side_map=side_map)
        for label in block.internal_b_ghost_labels
    )
    return build_semidirect_survivor_brst_block(
        shifted_current_labels=mapped_shifted_current_labels,
        survivor_labels=mapped_survivor_labels,
        c_ghost_labels=mapped_c_ghost_labels,
        b_ghost_labels=mapped_b_ghost_labels,
        internal_c_ghost_labels=mapped_internal_c_ghost_labels,
        internal_b_ghost_labels=mapped_internal_b_ghost_labels,
        chi_vector=block.chi_vector,
        quadratic_terms=relabel_quadratic_ghost_terms(
            block.quadratic_ghost_terms,
            label_map,
            side_map=side_map,
        ),
        current_action_terms=relabel_current_action_terms(
            block.current_action_terms,
            label_map,
            side_map=side_map,
        ),
        survivor_action_terms=_relabel_survivor_action_terms(
            block.survivor_action_terms,
            label_map,
            side_map=side_map,
        ),
        internal_quadratic_terms=_relabel_internal_quadratic_ghost_terms(
            block.internal_quadratic_ghost_terms,
            side_map=side_map,
        ),
        internal_survivor_action_terms=_relabel_internal_survivor_action_terms(
            block.internal_survivor_action_terms,
            side_map=side_map,
        ),
        constraint_total_degree=block.constraint_total_degree,
        survivor_total_degree=block.survivor_total_degree,
        max_internal_ce_degree=block.max_internal_ce_degree,
        source_tag=tag,
    )


def quadratic_ghost_differential(
    ghost_labels: Tuple[str, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    degree: int,
) -> Matrix:
    """Matrix of the quadratic ghost differential on exterior degree `degree`."""
    source_basis = exterior_basis_indices(len(ghost_labels), degree)
    target_basis = exterior_basis_indices(len(ghost_labels), degree + 1)
    matrix = zeros(len(target_basis), len(source_basis))
    if not source_basis or not target_basis or not quadratic_terms:
        return matrix

    ghost_index = {label: index for index, label in enumerate(ghost_labels)}
    target_index = {basis: row for row, basis in enumerate(target_basis)}

    for col, basis in enumerate(source_basis):
        for item in quadratic_terms:
            contraction = _remove_ghost_index(
                basis,
                ghost_index[_dual_c_ghost_label(item.target_b_ghost)],
            )
            if contraction is None:
                continue
            sign_remove, reduced_basis = contraction
            inserted_left = _insert_ghost_index(reduced_basis, ghost_index[item.left_c_ghost])
            if inserted_left is None:
                continue
            sign_left, left_basis = inserted_left
            inserted_right = _insert_ghost_index(left_basis, ghost_index[item.right_c_ghost])
            if inserted_right is None:
                continue
            sign_right, target = inserted_right
            row = target_index[target]
            matrix[row, col] += (
                -sympify(item.coefficient) * sign_remove * sign_left * sign_right
            )

    return matrix


def ghost_brst_differential(
    ghost_labels: Tuple[str, ...],
    chi_vector: Tuple[object, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    degree: int,
) -> Matrix:
    """Matrix of the ghost-sector BRST differential on one exterior degree."""
    return character_wedge_differential(len(ghost_labels), chi_vector, degree) + (
        quadratic_ghost_differential(ghost_labels, quadratic_terms, degree)
    )


def build_character_wedge_complex(
    ghost_labels: Tuple[str, ...],
    chi_vector: Tuple[object, ...],
    source_tag: str,
) -> TruncatedBRSTComplex:
    """Build the finite exterior complex with d = chi wedge."""
    if len(ghost_labels) != len(chi_vector):
        raise ValueError("ghost_labels and chi_vector must have the same length")

    num_ghosts = len(ghost_labels)
    basis_by_degree = {
        degree: exterior_basis_indices(num_ghosts, degree)
        for degree in range(num_ghosts + 1)
    }
    differentials = {
        degree: character_wedge_differential(num_ghosts, chi_vector, degree)
        for degree in range(num_ghosts)
    }

    return TruncatedBRSTComplex(
        source_tag=source_tag,
        ghost_labels=ghost_labels,
        chi_vector=chi_vector,
        basis_by_degree=basis_by_degree,
        differentials=differentials,
    )


def build_ghost_brst_complex(
    ghost_labels: Tuple[str, ...],
    chi_vector: Tuple[object, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    source_tag: str,
) -> TruncatedBRSTComplex:
    """Build the finite ghost-sector BRST complex with character and cc b terms."""
    if len(ghost_labels) != len(chi_vector):
        raise ValueError("ghost_labels and chi_vector must have the same length")

    num_ghosts = len(ghost_labels)
    basis_by_degree = {
        degree: exterior_basis_indices(num_ghosts, degree)
        for degree in range(num_ghosts + 1)
    }
    differentials = {
        degree: ghost_brst_differential(ghost_labels, chi_vector, quadratic_terms, degree)
        for degree in range(num_ghosts)
    }

    return TruncatedBRSTComplex(
        source_tag=source_tag,
        ghost_labels=ghost_labels,
        chi_vector=chi_vector,
        basis_by_degree=basis_by_degree,
        differentials=differentials,
        quadratic_ghost_terms=quadratic_terms,
    )


def differential_square_blocks(complex_seed: TruncatedBRSTComplex) -> Dict[int, Matrix]:
    """Return d_{k+1} d_k blocks for the complex."""
    blocks: Dict[int, Matrix] = {}
    degrees = sorted(complex_seed.differentials)
    for degree in degrees:
        d_k = complex_seed.differentials[degree]
        d_k1 = complex_seed.differentials.get(degree + 1)
        if d_k1 is None:
            continue
        blocks[degree] = d_k1 * d_k
    return blocks


def complex_has_nilpotent_differential(complex_seed: TruncatedBRSTComplex) -> bool:
    """Check d^2 = 0 on all available blocks."""
    for block in differential_square_blocks(complex_seed).values():
        if block != zeros(block.rows, block.cols):
            return False
    return True


def specialize_complex_chi(
    complex_seed: TruncatedBRSTComplex,
    chi_vector: Tuple[object, ...],
    source_tag: str | None = None,
) -> TruncatedBRSTComplex:
    """Rebuild a complex with the same ghost labels and a new chi vector."""
    tag = source_tag if source_tag is not None else f"{complex_seed.source_tag}_specialized"
    if complex_seed.quadratic_ghost_terms:
        return build_ghost_brst_complex(
            ghost_labels=complex_seed.ghost_labels,
            chi_vector=chi_vector,
            quadratic_terms=complex_seed.quadratic_ghost_terms,
            source_tag=tag,
        )
    return build_character_wedge_complex(
        ghost_labels=complex_seed.ghost_labels,
        chi_vector=chi_vector,
        source_tag=tag,
    )


def truncated_cohomology_dimensions(complex_seed: TruncatedBRSTComplex) -> Dict[int, int]:
    """Compute cohomology dimensions H^k of a finite truncated complex."""
    dims: Dict[int, int] = {}
    max_degree = max(complex_seed.basis_by_degree)
    for degree in range(max_degree + 1):
        dim_c = len(complex_seed.basis_by_degree[degree])
        d_curr = complex_seed.differentials.get(degree)
        d_prev = complex_seed.differentials.get(degree - 1)
        rank_curr = exact_matrix_rank(d_curr)
        rank_prev = exact_matrix_rank(d_prev)
        ker_dim = dim_c - rank_curr
        dims[degree] = ker_dim - rank_prev
    return dims


def complex_is_acyclic(complex_seed: TruncatedBRSTComplex) -> bool:
    """Check whether all cohomology groups of the truncated complex vanish."""
    return all(value == 0 for value in truncated_cohomology_dimensions(complex_seed).values())


def sl3_subregular_truncated_brst_complex(level=Symbol("k")) -> TruncatedBRSTComplex:
    """Explicit truncated BRST seed complex for sl_3 subregular DS reduction."""
    _ = sympify(level)  # reserved for future level-dependent corrections
    constraints = sl3_subregular_constraints()
    character = sl3_subregular_constraint_character()
    root_order = tuple(constraint.root_label for constraint in constraints)
    ghost_labels = tuple(constraint.c_ghost for constraint in constraints)
    chi_vector = tuple(character[root] for root in root_order)
    return build_character_wedge_complex(
        ghost_labels=ghost_labels,
        chi_vector=chi_vector,
        source_tag="A2_subregular_seed",
    )


def _default_nonzero_character(num_constraints: int) -> Tuple[int, ...]:
    """Default nonzero character vector used for acyclicity specializations."""
    if num_constraints < 1:
        raise ValueError("num_constraints must be positive")
    return (1,) + (0,) * (num_constraints - 1)


def hook_pair_ds_seed(
    n: int,
    r: int,
    level=Symbol("k"),
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> HookPairDSComplexSeed:
    """Paired symbolic DS complexes for one non-principal hook/subregular pair.

    This remains a truncated chain-level scaffold: the source/target sectors are
    finite exterior complexes with symbolic character entries.
    """
    return _hook_pair_ds_seed_cached(
        n,
        r,
        sympify(level),
        source_num_constraints,
        target_num_constraints,
    )


@lru_cache(maxsize=64)
def _hook_pair_ds_seed_cached(
    n: int,
    r: int,
    level,
    source_num_constraints: int | None,
    target_num_constraints: int | None,
) -> HookPairDSComplexSeed:
    """Cached paired symbolic DS complexes keyed by normalized level and truncation counts."""
    default_source, default_target = hook_pair_constraint_counts_ansatz_type_a(n, r)
    if source_num_constraints is None:
        source_num_constraints = default_source
    if target_num_constraints is None:
        target_num_constraints = default_target
    source_profile, target_profile = hook_pair_ghost_profiles(n, r)
    source_profile = _truncate_ghost_profile(source_profile, source_num_constraints, "source")
    target_profile = _truncate_ghost_profile(target_profile, target_num_constraints, "target")

    case = nonprincipal_hook_case(n, r, level=level)
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)

    source_complex = build_character_wedge_complex(
        ghost_labels=tuple(f"c_source_{item.root_label}" for item in source_profile),
        chi_vector=tuple(Symbol(f"chi_source_{item.root_label}") for item in source_profile),
        source_tag=f"A{n-1}_hook_source_{partition_tag}",
    )
    target_complex = build_character_wedge_complex(
        ghost_labels=tuple(f"c_target_{item.root_label}" for item in target_profile),
        chi_vector=tuple(Symbol(f"chi_target_{item.root_label}") for item in target_profile),
        source_tag=f"A{n-1}_hook_target_{dual_tag}",
    )

    return HookPairDSComplexSeed(
        n=n,
        r=r,
        source_partition=case.partition,
        target_partition=case.dual_partition,
        source_level=level,
        target_level=case.level_shift,
        source_complex=source_complex,
        target_complex=target_complex,
        track=TRACK_FRONTIER_NONPRINCIPAL,
        status=STATUS_DS_SEED,
    )


def hook_pair_specialized_complexes(
    n: int,
    r: int,
    level=Symbol("k"),
    source_chi: Tuple[object, ...] | None = None,
    target_chi: Tuple[object, ...] | None = None,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[TruncatedBRSTComplex, TruncatedBRSTComplex]:
    """Specialize one hook-pair DS seed to concrete character values."""
    seed = hook_pair_ds_seed(
        n,
        r,
        level=level,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    if source_chi is None:
        source_chi = _default_nonzero_character(len(seed.source_complex.ghost_labels))
    if target_chi is None:
        target_chi = _default_nonzero_character(len(seed.target_complex.ghost_labels))
    if len(source_chi) != len(seed.source_complex.ghost_labels):
        raise ValueError("source_chi length must match source ghost count")
    if len(target_chi) != len(seed.target_complex.ghost_labels):
        raise ValueError("target_chi length must match target ghost count")

    source = specialize_complex_chi(
        seed.source_complex,
        source_chi,
        source_tag=f"{seed.source_complex.source_tag}_specialized",
    )
    target = specialize_complex_chi(
        seed.target_complex,
        target_chi,
        source_tag=f"{seed.target_complex.source_tag}_specialized",
    )
    return source, target


def first_nonselfdual_hook_pair_ds_seed(level=Symbol("k")) -> HookPairDSComplexSeed:
    """Paired DS seed complexes for the first non-self-dual type-A hook pair."""
    return _first_nonselfdual_hook_pair_ds_seed_cached(sympify(level))


@lru_cache(maxsize=64)
def _first_nonselfdual_hook_pair_ds_seed_cached(level) -> HookPairDSComplexSeed:
    """Cached first hook-pair DS seed keyed by normalized level."""
    n, r, _ = first_nonselfdual_type_a_hook_pair()
    case = nonprincipal_hook_case(n, r, level=level)
    source_constraints, target_constraints = first_nonselfdual_hook_pair_constraints()
    source_character, target_character = first_nonselfdual_hook_pair_constraint_characters()
    source_quadratic, target_quadratic = first_nonselfdual_hook_pair_quadratic_ghost_term_support()

    source_complex = build_ghost_brst_complex(
        ghost_labels=tuple(item.c_ghost for item in source_constraints),
        chi_vector=tuple(source_character[item.root_label] for item in source_constraints),
        quadratic_terms=source_quadratic,
        source_tag="A3_hook_source_3_1",
    )
    target_complex = build_ghost_brst_complex(
        ghost_labels=tuple(item.c_ghost for item in target_constraints),
        chi_vector=tuple(target_character[item.root_label] for item in target_constraints),
        quadratic_terms=target_quadratic,
        source_tag="A3_hook_target_2_1_1",
    )

    return HookPairDSComplexSeed(
        n=n,
        r=r,
        source_partition=case.partition,
        target_partition=case.dual_partition,
        source_level=level,
        target_level=case.level_shift,
        source_complex=source_complex,
        target_complex=target_complex,
        track=TRACK_FRONTIER_NONPRINCIPAL,
        status=STATUS_DS_SEED,
    )


def first_nonselfdual_hook_pair_specialized_complexes(
    level=Symbol("k"),
    source_chi: Tuple[object, ...] | None = None,
    target_chi: Tuple[object, ...] | None = None,
) -> Tuple[TruncatedBRSTComplex, TruncatedBRSTComplex]:
    """Specialize the first hook-pair seed complexes to concrete chi values."""
    seed = first_nonselfdual_hook_pair_ds_seed(level=level)
    source_constraints, target_constraints = first_nonselfdual_hook_pair_constraints()
    if source_chi is None:
        source_character, _ = first_nonselfdual_hook_pair_constraint_characters()
        source_chi = tuple(source_character[item.root_label] for item in source_constraints)
    if target_chi is None:
        _, target_character = first_nonselfdual_hook_pair_constraint_characters()
        target_chi = tuple(target_character[item.root_label] for item in target_constraints)
    if len(source_chi) != len(seed.source_complex.ghost_labels):
        raise ValueError("source_chi length must match source ghost count")
    if len(target_chi) != len(seed.target_complex.ghost_labels):
        raise ValueError("target_chi length must match target ghost count")

    return (
        specialize_complex_chi(
            seed.source_complex,
            source_chi,
            source_tag=f"{seed.source_complex.source_tag}_specialized",
        ),
        specialize_complex_chi(
            seed.target_complex,
            target_chi,
            source_tag=f"{seed.target_complex.source_tag}_specialized",
        ),
    )


def first_nonselfdual_hook_pair_ghost_label_map() -> Dict[str, str]:
    """Canonical source-to-target positive-root relabeling for the first hook pair."""
    return {
        "E13": "E12",
        "E12": "E13",
        "E14": "E14",
        "E23": "E32",
        "E43": "E42",
    }


def first_nonselfdual_hook_pair_ghost_side_map() -> Dict[str, str]:
    """Canonical side relabeling from the hook-pair source ghost sector to the target."""
    return {"source": "target"}


def first_nonselfdual_hook_pair_ghost_complexes_match_under_relabeling(
    level=Symbol("k"),
) -> bool:
    """Check source/target ghost BRST complexes coincide after the canonical relabeling."""
    seed = first_nonselfdual_hook_pair_ds_seed(level=sympify(level))
    relabeled_source = relabel_truncated_brst_complex(
        seed.source_complex,
        first_nonselfdual_hook_pair_ghost_label_map(),
        side_map=first_nonselfdual_hook_pair_ghost_side_map(),
        source_tag=seed.target_complex.source_tag,
    )
    return (
        relabeled_source.ghost_labels == seed.target_complex.ghost_labels
        and relabeled_source.chi_vector == seed.target_complex.chi_vector
        and relabeled_source.quadratic_ghost_terms == seed.target_complex.quadratic_ghost_terms
        and relabeled_source.differentials == seed.target_complex.differentials
    )


def hook_pair_ds_seed_catalog(
    max_n: int = 6,
    level=Symbol("k"),
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[HookPairDSComplexSeed, ...]:
    """Enumerate hook/subregular DS pair seeds in type A."""
    return _hook_pair_ds_seed_catalog_cached(
        max_n,
        sympify(level),
        source_num_constraints,
        target_num_constraints,
    )


@lru_cache(maxsize=64)
def _hook_pair_ds_seed_catalog_cached(
    max_n: int,
    level,
    source_num_constraints: int | None,
    target_num_constraints: int | None,
) -> Tuple[HookPairDSComplexSeed, ...]:
    """Cached hook/subregular DS pair seed catalog keyed by normalized level."""
    if max_n < 3:
        return ()
    return tuple(
        hook_pair_ds_seed(
            n,
            r,
            level=level,
            source_num_constraints=source_num_constraints,
            target_num_constraints=target_num_constraints,
        )
        for n in range(3, max_n + 1)
        for r in range(1, n - 1)
    )


def verify_hook_pair_ds_seed_catalog(max_n: int = 8, level=Symbol("k")) -> Dict[str, bool]:
    """Sanity checks for the hook/subregular DS pair complex catalog."""
    return dict(_verify_hook_pair_ds_seed_catalog_items(max_n, sympify(level)))


@lru_cache(maxsize=64)
def _verify_hook_pair_ds_seed_catalog_items(
    max_n: int,
    level,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for hook/subregular DS pair catalog verification."""
    results: Dict[str, bool] = {}
    seeds = hook_pair_ds_seed_catalog(max_n=max_n, level=level)

    results["hook DS pair catalog is nonempty"] = bool(seeds)
    results["hook DS pair catalog stays on frontier track"] = all(
        seed.track == TRACK_FRONTIER_NONPRINCIPAL for seed in seeds
    )
    results["hook DS pair catalog keeps explicit seed status"] = all(
        seed.status == STATUS_DS_SEED for seed in seeds
    )

    for seed in seeds:
        n = seed.n
        r = seed.r
        case = nonprincipal_hook_case(n, r, level=level)
        expected_source_count, expected_target_count = hook_pair_constraint_counts_ansatz_type_a(n, r)
        key = f"A{n-1} hook r={r}"
        source_spec, target_spec = hook_pair_specialized_complexes(
            n,
            r,
            level=level,
            source_num_constraints=len(seed.source_complex.ghost_labels),
            target_num_constraints=len(seed.target_complex.ghost_labels),
        )

        results[f"{key} partition propagation"] = (
            seed.source_partition == case.partition
            and seed.target_partition == case.dual_partition
        )
        results[f"{key} level shift propagation"] = (
            simplify(seed.target_level - nonprincipal_hook_level_shift_type_a(n, r, level)) == 0
        )
        results[f"{key} ansatz ghost-count propagation"] = (
            len(seed.source_complex.ghost_labels) == expected_source_count
            and len(seed.target_complex.ghost_labels) == expected_target_count
        )
        results[f"{key} class is non-principal hook/subregular"] = (
            type_a_orbit_class(seed.source_partition) in {"subregular", "hook_nonprincipal"}
        )
        results[f"{key} explicit seed status tag"] = (seed.status == STATUS_DS_SEED)
        results[f"{key} source complex nilpotent"] = (
            complex_has_nilpotent_differential(seed.source_complex)
        )
        results[f"{key} target complex nilpotent"] = (
            complex_has_nilpotent_differential(seed.target_complex)
        )
        results[f"{key} source specialization acyclic"] = complex_is_acyclic(source_spec)
        results[f"{key} target specialization acyclic"] = complex_is_acyclic(target_spec)

    first = first_nonselfdual_hook_pair_ds_seed(level=level)
    results["first hook DS pair remains A3"] = (
        first.n == 4
        and first.r == 1
        and first.source_partition == (3, 1)
        and first.target_partition == (2, 1, 1)
    )
    return tuple(results.items())


def verify_hook_pair_seed_alignment(max_n: int = 8, level=Symbol("k")) -> Dict[str, bool]:
    """Cross-check DS pair catalog against non-principal DS seed catalog."""
    return dict(_verify_hook_pair_seed_alignment_items(max_n, sympify(level)))


@lru_cache(maxsize=64)
def _verify_hook_pair_seed_alignment_items(
    max_n: int,
    level,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for hook DS seed alignment checks."""
    results: Dict[str, bool] = {}
    pair_catalog = hook_pair_ds_seed_catalog(max_n=max_n, level=level)
    seed_catalog = nonprincipal_hook_seed_catalog(max_n=max_n, level=level)

    results["hook pair catalog matches seed catalog size"] = (
        len(pair_catalog) == len(seed_catalog)
    )
    for pair_seed, seed in zip(pair_catalog, seed_catalog):
        key = f"A{pair_seed.n-1} hook r={pair_seed.r}"
        expected_source_count, expected_target_count = hook_pair_constraint_counts_ansatz_type_a(
            pair_seed.n,
            pair_seed.r,
        )
        results[f"{key} partition alignment"] = (
            pair_seed.source_partition == seed.partition
            and pair_seed.target_partition == seed.dual_partition
        )
        results[f"{key} level-shift alignment"] = (
            simplify(pair_seed.target_level - seed.level_shift) == 0
        )
        results[f"{key} track alignment"] = (pair_seed.track == seed.track)
        results[f"{key} status alignment"] = (pair_seed.status == STATUS_DS_SEED)
        results[f"{key} ghost-count ansatz alignment"] = (
            len(pair_seed.source_complex.ghost_labels) == expected_source_count
            and len(pair_seed.target_complex.ghost_labels) == expected_target_count
        )

    return tuple(results.items())


def verify_hook_pair_first_transfer_correction_catalog(
    max_n: int = 6,
) -> Dict[str, bool]:
    """Low-rank catalog checks for witness-driven first transfer on hook pairs."""
    results: Dict[str, bool] = {}
    if max_n < 3:
        results["hook first-transfer catalog is empty below rank three"] = True
        return results
    for n in range(3, max_n + 1):
        for r in range(1, n - 1):
            source_action, target_action = hook_pair_survivor_action_terms(n, r)
            source_correction, target_correction = hook_pair_first_transfer_correction_terms(n, r)
            source_corrected, target_corrected = (
                combine_survivor_action_terms(source_action, source_correction),
                combine_survivor_action_terms(target_action, target_correction),
            )
            key = f"A{n-1} hook r={r}"
            results[f"{key} first transfer cancels reduced survivor action"] = (
                len(source_action) == len(source_correction)
                and len(target_action) == len(target_correction)
                and source_corrected == ()
                and target_corrected == ()
            )
    return results


def verify_hook_pair_corrected_semidirect_catalog(
    max_n: int = 6,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Dict[str, bool]:
    """Low-rank catalog checks for the corrected semidirect hook truncation."""
    results: Dict[str, bool] = {}
    if max_n < 3:
        results["hook corrected semidirect catalog is empty below rank three"] = True
        return results
    for n in range(3, max_n + 1):
        for r in range(1, n - 1):
            key = f"A{n-1} hook r={r}"
            results[f"{key} corrected semidirect blocks square to zero"] = all(
                _hook_pair_corrected_semidirect_square_zero_flags(
                    n,
                    r,
                    max_constraint_total_degree=max_constraint_total_degree,
                    survivor_total_degree=survivor_total_degree,
                    max_internal_ce_degree=max_internal_ce_degree,
                )
            )
    return results


def verify_hook_pair_corrected_semidirect_duality_catalog(
    max_n: int = 6,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of corrected semidirect hook blocks."""
    results: Dict[str, bool] = {}
    if max_n < 3:
        results["hook corrected semidirect duality catalog is empty below rank three"] = True
        return results
    for n in range(3, max_n + 1):
        for r in range(1, n - 1):
            key = f"A{n-1} hook r={r}"
            results[f"{key} corrected semidirect dual-swap match"] = (
                hook_pair_corrected_semidirect_blocks_match_under_dual_swap(
                    n,
                    r,
                    max_constraint_total_degree=max_constraint_total_degree,
                    survivor_total_degree=survivor_total_degree,
                    max_internal_ce_degree=max_internal_ce_degree,
                )
            )
    return results


@lru_cache(maxsize=64)
def hook_pair_corrected_semidirect_family_holds_via_duality(
    n: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> bool:
    """Check one hook family using direct half-catalog square-zero plus transpose duality."""
    if n < 3:
        return True
    for r in _hook_family_representative_rs(n):
        if not hook_pair_corrected_semidirect_representative_holds_via_duality(
            n,
            r,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
        ):
            return False
    return True


def verify_hook_pair_corrected_semidirect_family_via_duality_catalog(
    max_n: int = 7,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks that recover each hook family from a half-catalog plus duality."""
    return dict(
        _hook_pair_corrected_semidirect_family_via_duality_catalog_items(
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
        )
    )


@lru_cache(maxsize=64)
def _hook_pair_corrected_semidirect_family_via_duality_catalog_items(
    max_n: int = 7,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for hook corrected family-via-duality checks."""
    if max_n < 3:
        return (("hook corrected semidirect family-via-duality catalog is empty below rank three", True),)
    return tuple(
        (
            f"A{n-1} hook family corrected semidirect square-zero follows by duality",
            hook_pair_corrected_semidirect_family_holds_via_duality(
                n,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
            ),
        )
        for n in range(3, max_n + 1)
    )


@lru_cache(maxsize=128)
def hook_pair_corrected_semidirect_representative_holds_via_duality(
    n: int,
    r: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> bool:
    """Check one corrected semidirect hook representative plus transpose duality."""
    if not all(
        _hook_pair_corrected_semidirect_source_square_zero_flags(
            n,
            r,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
        )
    ):
        return False
    if not hook_pair_corrected_semidirect_blocks_match_under_dual_swap(
        n,
        r,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
    ):
        return False
    return True


@lru_cache(maxsize=512)
def homogeneous_monomial_exponents(num_variables: int, degree: int) -> Tuple[Tuple[int, ...], ...]:
    """Exponent tuples of total degree `degree` in `num_variables` commuting variables."""
    if num_variables < 0:
        raise ValueError("num_variables must be nonnegative")
    if degree < 0:
        return ()
    if num_variables == 0:
        return ((),) if degree == 0 else ()
    if num_variables == 1:
        return ((degree,),)

    exponents = []
    for first in range(degree, -1, -1):
        for rest in homogeneous_monomial_exponents(num_variables - 1, degree - first):
            exponents.append((first,) + rest)
    return tuple(exponents)


@lru_cache(maxsize=512)
def linear_constraint_block_basis(
    num_constraints: int,
    total_degree: int,
    chain_degree: int,
) -> Tuple[ConstraintBasisElement, ...]:
    """Basis of monomials times exterior `b`-ghosts in fixed total degree."""
    polynomial_degree = total_degree - chain_degree
    if polynomial_degree < 0 or chain_degree < 0 or chain_degree > num_constraints:
        return ()

    monomials = homogeneous_monomial_exponents(num_constraints, polynomial_degree)
    ghosts = exterior_basis_indices(num_constraints, chain_degree)
    return tuple((monomial, ghost) for monomial in monomials for ghost in ghosts)


def linear_constraint_koszul_differential(
    num_constraints: int,
    total_degree: int,
    chain_degree: int,
) -> Matrix:
    """Koszul differential on one fixed total-degree block.

    This is the linear BRST differential for the shifted constraints
    `u_i = J_i - chi_i`, acting by `d = sum u_i * iota_{b_i}`.
    """
    source_basis = linear_constraint_block_basis(num_constraints, total_degree, chain_degree)
    target_basis = linear_constraint_block_basis(num_constraints, total_degree, chain_degree - 1)
    matrix = zeros(len(target_basis), len(source_basis))
    if not source_basis or not target_basis:
        return matrix

    target_index = {basis: row for row, basis in enumerate(target_basis)}

    for col, (monomial, ghost_subset) in enumerate(source_basis):
        for position, ghost_index in enumerate(ghost_subset):
            target_monomial = list(monomial)
            target_monomial[ghost_index] += 1
            target = (tuple(target_monomial), ghost_subset[:position] + ghost_subset[position + 1 :])
            row = target_index[target]
            sign = -1 if position % 2 else 1
            matrix[row, col] += sign

    return matrix


def linear_constraint_contracting_homotopy(
    num_constraints: int,
    total_degree: int,
    chain_degree: int,
) -> Matrix:
    """Standard contracting homotopy on one fixed positive total-degree block."""
    source_basis = linear_constraint_block_basis(num_constraints, total_degree, chain_degree)
    target_basis = linear_constraint_block_basis(num_constraints, total_degree, chain_degree + 1)
    matrix = zeros(len(target_basis), len(source_basis))
    if total_degree <= 0 or not source_basis or not target_basis:
        return matrix

    target_index = {basis: row for row, basis in enumerate(target_basis)}

    for col, (monomial, ghost_subset) in enumerate(source_basis):
        ghost_set = set(ghost_subset)
        for ghost_index in range(num_constraints):
            exponent = monomial[ghost_index]
            if exponent == 0 or ghost_index in ghost_set:
                continue
            target_monomial = list(monomial)
            target_monomial[ghost_index] -= 1
            insertion_position = sum(1 for value in ghost_subset if value < ghost_index)
            sign = -1 if insertion_position % 2 else 1
            target_ghost = tuple(sorted(ghost_subset + (ghost_index,)))
            target = (tuple(target_monomial), target_ghost)
            row = target_index[target]
            matrix[row, col] += sign * Rational(exponent, total_degree)

    return matrix


def build_linear_constraint_koszul_block(
    shifted_current_labels: Tuple[str, ...],
    ghost_labels: Tuple[str, ...],
    total_degree: int,
    source_tag: str,
) -> LinearConstraintBRSTBlock:
    """Build one finite current-plus-ghost block for the linear constraint differential."""
    if len(shifted_current_labels) != len(ghost_labels):
        raise ValueError("shifted_current_labels and ghost_labels must have the same length")

    num_constraints = len(ghost_labels)
    basis_by_chain_degree = {
        degree: linear_constraint_block_basis(num_constraints, total_degree, degree)
        for degree in range(min(num_constraints, total_degree) + 1)
    }
    differentials = {
        degree: linear_constraint_koszul_differential(num_constraints, total_degree, degree)
        for degree in range(1, min(num_constraints, total_degree) + 1)
    }
    return LinearConstraintBRSTBlock(
        source_tag=source_tag,
        shifted_current_labels=shifted_current_labels,
        ghost_labels=ghost_labels,
        total_degree=total_degree,
        basis_by_chain_degree=basis_by_chain_degree,
        differentials=differentials,
    )


@lru_cache(maxsize=512)
def _ghost_brst_images_on_basis_element(
    basis: Tuple[int, ...],
    ghost_labels: Tuple[str, ...],
    chi_vector: Tuple[object, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
) -> Dict[Tuple[int, ...], object]:
    """Image of one c-ghost exterior basis element under the ghost BRST differential."""
    coefficients: Dict[Tuple[int, ...], object] = {}
    ghost_index = _ghost_label_index_map(ghost_labels)
    indexed_quadratic_terms = _indexed_quadratic_ghost_terms(ghost_labels, quadratic_terms)

    for ghost_idx, chi_value in enumerate(chi_vector):
        inserted = _insert_ghost_index(basis, ghost_idx)
        if inserted is None:
            continue
        sign, target = inserted
        coefficients[target] = coefficients.get(target, 0) + sign * sympify(chi_value)

    for target_c_idx, left_c_idx, right_c_idx, coefficient in indexed_quadratic_terms:
        contraction = _remove_ghost_index(
            basis,
            target_c_idx,
        )
        if contraction is None:
            continue
        sign_remove, reduced_basis = contraction
        inserted_left = _insert_ghost_index(reduced_basis, left_c_idx)
        if inserted_left is None:
            continue
        sign_left, left_basis = inserted_left
        inserted_right = _insert_ghost_index(left_basis, right_c_idx)
        if inserted_right is None:
            continue
        sign_right, target = inserted_right
        coefficients[target] = coefficients.get(target, 0) - (
            sympify(coefficient) * sign_remove * sign_left * sign_right
        )

    return {target: simplify(value) for target, value in coefficients.items() if value != 0}


@lru_cache(maxsize=256)
def _ghost_label_index_map(ghost_labels: Tuple[str, ...]) -> Dict[str, int]:
    """Index lookup for a fixed ordered ghost basis."""
    return {label: index for index, label in enumerate(ghost_labels)}


@lru_cache(maxsize=256)
def _indexed_quadratic_ghost_terms(
    ghost_labels: Tuple[str, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
) -> Tuple[Tuple[int, int, int, object], ...]:
    """Quadratic ghost terms with labels resolved to fixed ghost indices."""
    ghost_index = _ghost_label_index_map(ghost_labels)
    return tuple(
        (
            ghost_index[_dual_c_ghost_label(item.target_b_ghost)],
            ghost_index[item.left_c_ghost],
            ghost_index[item.right_c_ghost],
            item.coefficient,
        )
        for item in quadratic_terms
    )


@lru_cache(maxsize=512)
def _replace_exterior_index(
    basis: Tuple[int, ...],
    source_index: int,
    target_index: int,
) -> Tuple[int, Tuple[int, ...]] | None:
    """Replace one exterior basis index and return the induced reordering sign."""
    if source_index not in basis:
        return None
    if target_index == source_index:
        return 1, basis
    if target_index in basis:
        return None
    position = basis.index(source_index)
    updated = list(basis)
    updated[position] = target_index
    sorted_updated = sorted(updated)
    sign = -1 if abs(sorted_updated.index(target_index) - position) % 2 else 1
    return sign, tuple(sorted_updated)


def _label_root(label: str) -> str:
    """Root-label suffix of a shifted-current or ghost label."""
    parts = label.split("_", 2)
    if len(parts) < 2:
        raise ValueError("label must contain an underscore")
    return parts[-1]


@lru_cache(maxsize=256)
def current_action_differential(
    shifted_current_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    b_ghost_labels: Tuple[str, ...],
    current_action_terms: Tuple[CurrentActionTermEntry, ...],
    constraint_total_degree: int,
    brst_degree: int,
) -> Matrix:
    """Current-action term c.rho on one fixed mixed current-plus-ghost block."""
    num_constraints = len(c_ghost_labels)
    source_basis = mixed_constraint_ghost_block_basis(
        num_constraints,
        constraint_total_degree,
        brst_degree,
    )
    target_basis = mixed_constraint_ghost_block_basis(
        num_constraints,
        constraint_total_degree,
        brst_degree + 1,
    )
    matrix = zeros(len(target_basis), len(source_basis))
    if not source_basis or not target_basis or not current_action_terms:
        return matrix

    target_index = {basis: row for row, basis in enumerate(target_basis)}
    indexed_current_actions = _indexed_current_action_terms(
        shifted_current_labels,
        c_ghost_labels,
        b_ghost_labels,
        current_action_terms,
    )

    for col, (monomial, c_subset, b_subset) in enumerate(source_basis):
        for c_ghost_index, action_terms in indexed_current_actions.items():
            inserted = _insert_ghost_index(c_subset, c_ghost_index)
            if inserted is None:
                continue
            c_sign, target_c_subset = inserted

            for source_u, target_u, source_b, target_b, coefficient in action_terms:
                exponent = monomial[source_u]
                if exponent:
                    target_monomial = list(monomial)
                    target_monomial[source_u] -= 1
                    target_monomial[target_u] += 1
                    target = (tuple(target_monomial), target_c_subset, b_subset)
                    row = target_index[target]
                    matrix[row, col] += c_sign * exponent * coefficient

                replaced = _replace_exterior_index(b_subset, source_b, target_b)
                if replaced is None:
                    continue
                b_sign, target_b_subset = replaced
                target = (monomial, target_c_subset, target_b_subset)
                row = target_index[target]
                matrix[row, col] += c_sign * b_sign * coefficient

    return matrix


@lru_cache(maxsize=512)
def mixed_constraint_ghost_block_basis(
    num_constraints: int,
    constraint_total_degree: int,
    brst_degree: int,
) -> Tuple[FullConstraintGhostBasisElement, ...]:
    """Basis in fixed constraint-total degree and BRST degree.

    The constraint-total degree is polynomial degree plus b-ghost degree.
    The BRST degree is c-degree minus b-degree.
    """
    if num_constraints < 0:
        raise ValueError("num_constraints must be nonnegative")
    basis: list[FullConstraintGhostBasisElement] = []
    max_b_degree = min(num_constraints, constraint_total_degree)
    for b_degree in range(max_b_degree + 1):
        polynomial_degree = constraint_total_degree - b_degree
        c_degree = brst_degree + b_degree
        if c_degree < 0 or c_degree > num_constraints:
            continue
        monomials = homogeneous_monomial_exponents(num_constraints, polynomial_degree)
        c_basis = exterior_basis_indices(num_constraints, c_degree)
        b_basis = exterior_basis_indices(num_constraints, b_degree)
        basis.extend((monomial, c_subset, b_subset) for monomial in monomials for c_subset in c_basis for b_subset in b_basis)
    return tuple(basis)


def mixed_constraint_ghost_brst_differential(
    shifted_current_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    b_ghost_labels: Tuple[str, ...],
    chi_vector: Tuple[object, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    constraint_total_degree: int,
    brst_degree: int,
    current_action_terms: Tuple[CurrentActionTermEntry, ...] = (),
) -> Matrix:
    """BRST differential on one fixed mixed current-plus-ghost block."""
    if not (
        len(shifted_current_labels) == len(c_ghost_labels) == len(b_ghost_labels) == len(chi_vector)
    ):
        raise ValueError("shifted currents, c-ghosts, b-ghosts, and chi entries must align")

    num_constraints = len(c_ghost_labels)
    source_basis = mixed_constraint_ghost_block_basis(
        num_constraints, constraint_total_degree, brst_degree
    )
    target_basis = mixed_constraint_ghost_block_basis(
        num_constraints, constraint_total_degree, brst_degree + 1
    )
    matrix = zeros(len(target_basis), len(source_basis))
    if not source_basis or not target_basis:
        return matrix

    target_index = {basis: row for row, basis in enumerate(target_basis)}

    for col, (monomial, c_subset, b_subset) in enumerate(source_basis):
        # Ghost-sector term: acts only on c-subset.
        for target_c_subset, coefficient in _ghost_brst_images_on_basis_element(
            c_subset,
            c_ghost_labels,
            chi_vector,
            quadratic_terms,
        ).items():
            target = (monomial, target_c_subset, b_subset)
            row = target_index[target]
            matrix[row, col] += coefficient

        # Linear Koszul term: d(b_i) = u_i, with a Koszul sign past the c-sector.
        c_sign = -1 if len(c_subset) % 2 else 1
        for position, b_index in enumerate(b_subset):
            target_monomial = list(monomial)
            target_monomial[b_index] += 1
            target = (
                tuple(target_monomial),
                c_subset,
                b_subset[:position] + b_subset[position + 1 :],
            )
            row = target_index[target]
            matrix[row, col] += c_sign * (-1 if position % 2 else 1)

    matrix += current_action_differential(
        shifted_current_labels,
        c_ghost_labels,
        b_ghost_labels,
        current_action_terms,
        constraint_total_degree,
        brst_degree,
    )
    return matrix


def build_mixed_constraint_ghost_brst_block(
    shifted_current_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    b_ghost_labels: Tuple[str, ...],
    chi_vector: Tuple[object, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    constraint_total_degree: int,
    source_tag: str,
    current_action_terms: Tuple[CurrentActionTermEntry, ...] = (),
) -> MixedConstraintGhostBRSTBlock:
    """Build one finite mixed BRST block at fixed constraint-total degree."""
    if not (
        len(shifted_current_labels) == len(c_ghost_labels) == len(b_ghost_labels) == len(chi_vector)
    ):
        raise ValueError("shifted currents, c-ghosts, b-ghosts, and chi entries must align")

    num_constraints = len(c_ghost_labels)
    basis_by_brst_degree: Dict[int, Tuple[FullConstraintGhostBasisElement, ...]] = {}
    for brst_degree in range(-min(num_constraints, constraint_total_degree), num_constraints + 1):
        basis = mixed_constraint_ghost_block_basis(
            num_constraints,
            constraint_total_degree,
            brst_degree,
        )
        if basis:
            basis_by_brst_degree[brst_degree] = basis

    differentials = {
        degree: mixed_constraint_ghost_brst_differential(
            shifted_current_labels,
            c_ghost_labels,
            b_ghost_labels,
            chi_vector,
            quadratic_terms,
            constraint_total_degree,
            degree,
            current_action_terms=current_action_terms,
        )
        for degree in basis_by_brst_degree
        if mixed_constraint_ghost_block_basis(
            num_constraints,
            constraint_total_degree,
            degree + 1,
        )
    }

    return MixedConstraintGhostBRSTBlock(
        source_tag=source_tag,
        shifted_current_labels=shifted_current_labels,
        c_ghost_labels=c_ghost_labels,
        b_ghost_labels=b_ghost_labels,
        chi_vector=chi_vector,
        quadratic_ghost_terms=quadratic_terms,
        current_action_terms=current_action_terms,
        constraint_total_degree=constraint_total_degree,
        basis_by_brst_degree=basis_by_brst_degree,
        differentials=differentials,
    )


@lru_cache(maxsize=512)
def survivor_coupled_block_basis(
    num_constraints: int,
    num_survivors: int,
    constraint_total_degree: int,
    survivor_total_degree: int,
    brst_degree: int,
) -> Tuple[SurvivorCoupledBasisElement, ...]:
    """Basis in fixed constraint degree, survivor degree, and BRST degree."""
    if num_constraints < 0 or num_survivors < 0:
        raise ValueError("constraint and survivor counts must be nonnegative")
    basis: list[SurvivorCoupledBasisElement] = []
    max_b_degree = min(num_constraints, constraint_total_degree)
    survivor_monomials = homogeneous_monomial_exponents(num_survivors, survivor_total_degree)
    for b_degree in range(max_b_degree + 1):
        polynomial_degree = constraint_total_degree - b_degree
        c_degree = brst_degree + b_degree
        if c_degree < 0 or c_degree > num_constraints:
            continue
        u_monomials = homogeneous_monomial_exponents(num_constraints, polynomial_degree)
        c_basis = exterior_basis_indices(num_constraints, c_degree)
        b_basis = exterior_basis_indices(num_constraints, b_degree)
        basis.extend(
            (u_monomial, survivor_monomial, c_subset, b_subset)
            for u_monomial in u_monomials
            for survivor_monomial in survivor_monomials
            for c_subset in c_basis
            for b_subset in b_basis
        )
    return tuple(basis)


@lru_cache(maxsize=256)
def survivor_action_differential(
    survivor_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    b_ghost_labels: Tuple[str, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    constraint_total_degree: int,
    survivor_total_degree: int,
    brst_degree: int,
) -> Matrix:
    """Induced action of the positive sector on survivor variables."""
    num_constraints = len(c_ghost_labels)
    num_survivors = len(survivor_labels)
    source_basis = survivor_coupled_block_basis(
        num_constraints,
        num_survivors,
        constraint_total_degree,
        survivor_total_degree,
        brst_degree,
    )
    target_basis = survivor_coupled_block_basis(
        num_constraints,
        num_survivors,
        constraint_total_degree,
        survivor_total_degree,
        brst_degree + 1,
    )
    matrix = zeros(len(target_basis), len(source_basis))
    if not source_basis or not target_basis or not survivor_action_terms:
        return matrix

    target_index = {basis: row for row, basis in enumerate(target_basis)}
    indexed_survivor_actions = _indexed_survivor_action_by_source_and_c_ghost(
        survivor_labels,
        c_ghost_labels,
        survivor_action_terms,
    )

    for col, (u_monomial, survivor_monomial, c_subset, b_subset) in enumerate(source_basis):
        for source_survivor, exponent in _monomial_nonzero_entries(survivor_monomial):
            for c_ghost_index, target_images in indexed_survivor_actions.get(source_survivor, {}).items():
                inserted = _insert_ghost_index(c_subset, c_ghost_index)
                if inserted is None:
                    continue
                c_sign, target_c_subset = inserted
                for target_survivor, coefficient in target_images:
                    target_survivor_monomial = list(survivor_monomial)
                    target_survivor_monomial[source_survivor] -= 1
                    target_survivor_monomial[target_survivor] += 1
                    target = (
                        u_monomial,
                        tuple(target_survivor_monomial),
                        target_c_subset,
                        b_subset,
                    )
                    row = target_index[target]
                    matrix[row, col] += c_sign * exponent * sympify(coefficient)

    return matrix


@lru_cache(maxsize=512)
def internal_survivor_ce_block_basis(
    num_survivors: int,
    survivor_polynomial_degree: int,
    ce_degree: int,
) -> Tuple[InternalSurvivorBasisElement, ...]:
    """Basis in fixed survivor polynomial degree and CE ghost degree."""
    if num_survivors < 0:
        raise ValueError("num_survivors must be nonnegative")
    if ce_degree < 0 or ce_degree > num_survivors:
        return ()
    monomials = homogeneous_monomial_exponents(num_survivors, survivor_polynomial_degree)
    c_basis = exterior_basis_indices(num_survivors, ce_degree)
    return tuple((monomial, c_subset) for monomial in monomials for c_subset in c_basis)


@lru_cache(maxsize=256)
def internal_survivor_action_differential(
    survivor_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    survivor_polynomial_degree: int,
    ce_degree: int,
) -> Matrix:
    """Adjoint action of survivor ghosts on survivor polynomial variables."""
    num_survivors = len(survivor_labels)
    source_basis = internal_survivor_ce_block_basis(
        num_survivors,
        survivor_polynomial_degree,
        ce_degree,
    )
    target_basis = internal_survivor_ce_block_basis(
        num_survivors,
        survivor_polynomial_degree,
        ce_degree + 1,
    )
    matrix = zeros(len(target_basis), len(source_basis))
    if not source_basis or not target_basis or not survivor_action_terms:
        return matrix

    target_index = {basis: row for row, basis in enumerate(target_basis)}
    indexed_survivor_actions = _indexed_survivor_action_by_source_and_c_ghost(
        survivor_labels,
        c_ghost_labels,
        survivor_action_terms,
    )

    for col, (survivor_monomial, c_subset) in enumerate(source_basis):
        for source_survivor, exponent in _monomial_nonzero_entries(survivor_monomial):
            for c_ghost_index, target_images in indexed_survivor_actions.get(source_survivor, {}).items():
                inserted = _insert_ghost_index(c_subset, c_ghost_index)
                if inserted is None:
                    continue
                c_sign, target_c_subset = inserted
                for target_survivor, coefficient in target_images:
                    target_survivor_monomial = list(survivor_monomial)
                    target_survivor_monomial[source_survivor] -= 1
                    target_survivor_monomial[target_survivor] += 1
                    target = (
                        tuple(target_survivor_monomial),
                        target_c_subset,
                    )
                    row = target_index[target]
                    matrix[row, col] += -c_sign * exponent * sympify(coefficient)

    return matrix


@lru_cache(maxsize=256)
def internal_survivor_ce_differential(
    survivor_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    survivor_polynomial_degree: int,
    ce_degree: int,
) -> Matrix:
    """CE differential for the reduced survivor algebra on one fixed polynomial degree."""
    if len(survivor_labels) != len(c_ghost_labels):
        raise ValueError("survivor labels and ghost labels must align")

    num_survivors = len(survivor_labels)
    source_basis = internal_survivor_ce_block_basis(
        num_survivors,
        survivor_polynomial_degree,
        ce_degree,
    )
    target_basis = internal_survivor_ce_block_basis(
        num_survivors,
        survivor_polynomial_degree,
        ce_degree + 1,
    )
    matrix = zeros(len(target_basis), len(source_basis))
    if not source_basis or not target_basis:
        return matrix

    target_index = {basis: row for row, basis in enumerate(target_basis)}
    zero_character = (Rational(0),) * num_survivors
    for col, (survivor_monomial, c_subset) in enumerate(source_basis):
        for target_c_subset, coefficient in _ghost_brst_images_on_basis_element(
            c_subset,
            c_ghost_labels,
            zero_character,
            quadratic_terms,
        ).items():
            target = (survivor_monomial, target_c_subset)
            row = target_index[target]
            matrix[row, col] += coefficient

    matrix += internal_survivor_action_differential(
        survivor_labels,
        c_ghost_labels,
        survivor_action_terms,
        survivor_polynomial_degree,
        ce_degree,
    )
    return matrix


@lru_cache(maxsize=512)
def semidirect_survivor_block_basis(
    num_constraints: int,
    num_survivors: int,
    constraint_total_degree: int,
    survivor_total_degree: int,
    max_internal_ce_degree: int,
    brst_degree: int,
) -> Tuple[SemidirectSurvivorBasisElement, ...]:
    """Basis in fixed constraint degree, survivor degree, bounded internal CE degree, and BRST degree."""
    if num_constraints < 0 or num_survivors < 0:
        raise ValueError("constraint and survivor counts must be nonnegative")
    if max_internal_ce_degree < 0:
        raise ValueError("max_internal_ce_degree must be nonnegative")
    basis: list[SemidirectSurvivorBasisElement] = []
    max_b_degree = min(num_constraints, constraint_total_degree)
    max_int_degree = min(num_survivors, max_internal_ce_degree)
    survivor_monomials = homogeneous_monomial_exponents(num_survivors, survivor_total_degree)
    internal_c_bases = {
        degree: exterior_basis_indices(num_survivors, degree)
        for degree in range(max_int_degree + 1)
    }
    for b_degree in range(max_b_degree + 1):
        polynomial_degree = constraint_total_degree - b_degree
        u_monomials = homogeneous_monomial_exponents(num_constraints, polynomial_degree)
        b_basis = exterior_basis_indices(num_constraints, b_degree)
        for internal_degree in range(max_int_degree + 1):
            c_degree = brst_degree + b_degree - internal_degree
            if c_degree < 0 or c_degree > num_constraints:
                continue
            c_basis = exterior_basis_indices(num_constraints, c_degree)
            basis.extend(
                (u_monomial, survivor_monomial, c_subset, b_subset, internal_c_subset)
                for u_monomial in u_monomials
                for survivor_monomial in survivor_monomials
                for c_subset in c_basis
                for b_subset in b_basis
                for internal_c_subset in internal_c_bases[internal_degree]
            )
    return tuple(basis)


def external_survivor_action_on_internal_ghosts_differential(
    survivor_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    constraint_total_degree: int,
    survivor_total_degree: int,
    max_internal_ce_degree: int,
    brst_degree: int,
) -> Matrix:
    """Cross term: positive-sector action on the internal survivor ghosts."""
    num_constraints = len(c_ghost_labels)
    num_survivors = len(survivor_labels)
    source_basis = semidirect_survivor_block_basis(
        num_constraints,
        num_survivors,
        constraint_total_degree,
        survivor_total_degree,
        max_internal_ce_degree,
        brst_degree,
    )
    target_basis = semidirect_survivor_block_basis(
        num_constraints,
        num_survivors,
        constraint_total_degree,
        survivor_total_degree,
        max_internal_ce_degree,
        brst_degree + 1,
    )
    matrix = zeros(len(target_basis), len(source_basis))
    if not source_basis or not target_basis or not survivor_action_terms:
        return matrix

    target_index = {basis: row for row, basis in enumerate(target_basis)}
    c_index = {label: index for index, label in enumerate(c_ghost_labels)}
    internal_c_ghost_labels, _ = internal_survivor_ghost_labels(survivor_labels)
    internal_index = {label: index for index, label in enumerate(internal_c_ghost_labels)}

    for col, (u_monomial, survivor_monomial, c_subset, b_subset, internal_c_subset) in enumerate(source_basis):
        _ = survivor_monomial
        for item in survivor_action_terms:
            inserted_ext = _insert_ghost_index(c_subset, c_index[item.c_ghost])
            if inserted_ext is None:
                continue
            ext_sign, target_c_subset = inserted_ext
            target_internal_ghost = internal_index[f"c_survivor_{item.target_survivor_label}"]
            removed = _remove_ghost_index(internal_c_subset, target_internal_ghost)
            if removed is None:
                continue
            remove_sign, reduced_internal_subset = removed
            source_internal_ghost = internal_index[f"c_survivor_{item.source_survivor_label}"]
            inserted_internal = _insert_ghost_index(reduced_internal_subset, source_internal_ghost)
            if inserted_internal is None:
                continue
            internal_sign, target_internal_subset = inserted_internal
            target = (
                u_monomial,
                survivor_monomial,
                target_c_subset,
                b_subset,
                target_internal_subset,
            )
            row = target_index[target]
            matrix[row, col] += (
                -ext_sign * remove_sign * internal_sign * sympify(item.coefficient)
            )

    return matrix


@lru_cache(maxsize=256)
def semidirect_survivor_brst_differential(
    shifted_current_labels: Tuple[str, ...],
    survivor_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    b_ghost_labels: Tuple[str, ...],
    internal_c_ghost_labels: Tuple[str, ...],
    chi_vector: Tuple[object, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    current_action_terms: Tuple[CurrentActionTermEntry, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    internal_quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    internal_survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    constraint_total_degree: int,
    survivor_total_degree: int,
    max_internal_ce_degree: int,
    brst_degree: int,
) -> Matrix:
    """Naive semidirect BRST differential with both external and internal survivor sectors.

    This is the direct quotient-level coupling attempt. It need not square to
    zero when the projected positive action fails to act by derivations on the
    reduced survivor bracket.
    """
    if not (
        len(shifted_current_labels) == len(c_ghost_labels) == len(b_ghost_labels) == len(chi_vector)
    ):
        raise ValueError("constraint labels and chi data must align")
    if len(survivor_labels) != len(internal_c_ghost_labels):
        raise ValueError("survivor labels and internal c-ghost labels must align")

    num_constraints = len(c_ghost_labels)
    num_survivors = len(survivor_labels)
    source_basis = semidirect_survivor_block_basis(
        num_constraints,
        num_survivors,
        constraint_total_degree,
        survivor_total_degree,
        max_internal_ce_degree,
        brst_degree,
    )
    target_basis = semidirect_survivor_block_basis(
        num_constraints,
        num_survivors,
        constraint_total_degree,
        survivor_total_degree,
        max_internal_ce_degree,
        brst_degree + 1,
    )
    if not source_basis or not target_basis:
        return zeros(len(target_basis), len(source_basis))

    target_index = {basis: row for row, basis in enumerate(target_basis)}
    indexed_current_actions = _indexed_current_action_terms(
        shifted_current_labels,
        c_ghost_labels,
        b_ghost_labels,
        current_action_terms,
    )
    internal_zero_character = (Rational(0),) * num_survivors
    indexed_survivor_actions = _indexed_survivor_action_by_source_and_c_ghost(
        survivor_labels,
        c_ghost_labels,
        survivor_action_terms,
    )
    indexed_internal_survivor_actions = _indexed_survivor_action_by_source_and_c_ghost(
        survivor_labels,
        internal_c_ghost_labels,
        internal_survivor_action_terms,
    )
    external_ghost_images = {
        c_subset: _ghost_brst_images_on_basis_element(
            c_subset,
            c_ghost_labels,
            chi_vector,
            quadratic_terms,
        )
        for c_subset in {basis[2] for basis in source_basis}
    }
    internal_ghost_images = {
        internal_c_subset: _ghost_brst_images_on_basis_element(
            internal_c_subset,
            internal_c_ghost_labels,
            internal_zero_character,
            internal_quadratic_terms,
        )
        for internal_c_subset in {basis[4] for basis in source_basis}
        if len(internal_c_subset) < max_internal_ce_degree
    }
    entries: Dict[Tuple[int, int], object] = {}

    def add_entry(row: int, col: int, value: object) -> None:
        if value == 0:
            return
        key = (row, col)
        updated = entries.get(key, 0) + value
        if updated == 0:
            entries.pop(key, None)
            return
        entries[key] = updated

    for col, (u_monomial, survivor_monomial, c_subset, b_subset, internal_c_subset) in enumerate(source_basis):
        internal_degree = len(internal_c_subset)
        for target_c_subset, coefficient in external_ghost_images[c_subset].items():
            target = (
                u_monomial,
                survivor_monomial,
                target_c_subset,
                b_subset,
                internal_c_subset,
            )
            row = target_index[target]
            add_entry(row, col, coefficient)

        c_sign = -1 if len(c_subset) % 2 else 1
        for position, b_var_index in enumerate(b_subset):
            target_u_monomial = list(u_monomial)
            target_u_monomial[b_var_index] += 1
            target = (
                tuple(target_u_monomial),
                survivor_monomial,
                c_subset,
                b_subset[:position] + b_subset[position + 1 :],
                internal_c_subset,
            )
            row = target_index[target]
            add_entry(row, col, c_sign * (-1 if position % 2 else 1))

        for c_ghost_index, action_terms in indexed_current_actions.items():
            inserted = _insert_ghost_index(c_subset, c_ghost_index)
            if inserted is None:
                continue
            insert_sign, target_c_subset = inserted

            for source_u, target_u, source_b, target_b, coefficient in action_terms:
                exponent = u_monomial[source_u]
                if exponent:
                    target_u_monomial = list(u_monomial)
                    target_u_monomial[source_u] -= 1
                    target_u_monomial[target_u] += 1
                    target = (
                        tuple(target_u_monomial),
                        survivor_monomial,
                        target_c_subset,
                        b_subset,
                        internal_c_subset,
                    )
                    row = target_index[target]
                    add_entry(row, col, insert_sign * exponent * coefficient)

                replaced = _replace_exterior_index(b_subset, source_b, target_b)
                if replaced is None:
                    continue
                b_sign, target_b_subset = replaced
                target = (
                    u_monomial,
                    survivor_monomial,
                    target_c_subset,
                    target_b_subset,
                    internal_c_subset,
                )
                row = target_index[target]
                add_entry(row, col, insert_sign * b_sign * coefficient)

        for source_survivor, exponent in _monomial_nonzero_entries(survivor_monomial):
            for c_ghost_index, target_images in indexed_survivor_actions.get(source_survivor, {}).items():
                inserted = _insert_ghost_index(c_subset, c_ghost_index)
                if inserted is None:
                    continue
                insert_sign, target_c_subset = inserted
                for target_survivor, coefficient in target_images:
                    target = (
                        u_monomial,
                        _retarget_monomial(
                            survivor_monomial,
                            source_survivor,
                            target_survivor,
                        ),
                        target_c_subset,
                        b_subset,
                        internal_c_subset,
                    )
                    row = target_index[target]
                    add_entry(row, col, insert_sign * exponent * sympify(coefficient))

                    removed = _remove_ghost_index(internal_c_subset, target_survivor)
                    if removed is None:
                        continue
                    remove_sign, reduced_internal_subset = removed
                    inserted_internal = _insert_ghost_index(
                        reduced_internal_subset,
                        source_survivor,
                    )
                    if inserted_internal is None:
                        continue
                    internal_sign, target_internal_subset = inserted_internal
                    target = (
                        u_monomial,
                        survivor_monomial,
                        target_c_subset,
                        b_subset,
                        target_internal_subset,
                    )
                    row = target_index[target]
                    add_entry(
                        row,
                        col,
                        -insert_sign
                        * remove_sign
                        * internal_sign
                        * sympify(coefficient)
                    )

        internal_prefix = -1 if (len(c_subset) + len(b_subset)) % 2 else 1
        if internal_degree < max_internal_ce_degree:
            for target_internal_subset, coefficient in internal_ghost_images.get(
                internal_c_subset, {}
            ).items():
                target = (
                    u_monomial,
                    survivor_monomial,
                    c_subset,
                    b_subset,
                    target_internal_subset,
                )
                row = target_index.get(target)
                if row is None:
                    continue
                add_entry(row, col, internal_prefix * coefficient)

            for source_survivor, exponent in _monomial_nonzero_entries(survivor_monomial):
                for c_ghost_index, target_images in indexed_internal_survivor_actions.get(
                    source_survivor, {}
                ).items():
                    inserted_internal = _insert_ghost_index(
                        internal_c_subset,
                        c_ghost_index,
                    )
                    if inserted_internal is None:
                        continue
                    internal_sign, target_internal_subset = inserted_internal
                    for target_survivor, coefficient in target_images:
                        target = (
                            u_monomial,
                            _retarget_monomial(
                                survivor_monomial,
                                source_survivor,
                                target_survivor,
                            ),
                            c_subset,
                            b_subset,
                            target_internal_subset,
                        )
                        row = target_index.get(target)
                        if row is None:
                            continue
                        add_entry(
                            row,
                            col,
                            -internal_prefix
                            * internal_sign
                            * exponent
                            * sympify(coefficient)
                        )

    return SparseMatrix(
        len(target_basis),
        len(source_basis),
        {(row, col): value for (row, col), value in entries.items() if value != 0},
    )


def build_semidirect_survivor_brst_block(
    shifted_current_labels: Tuple[str, ...],
    survivor_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    b_ghost_labels: Tuple[str, ...],
    internal_c_ghost_labels: Tuple[str, ...],
    internal_b_ghost_labels: Tuple[str, ...],
    chi_vector: Tuple[object, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    current_action_terms: Tuple[CurrentActionTermEntry, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    internal_quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    internal_survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    constraint_total_degree: int,
    survivor_total_degree: int,
    max_internal_ce_degree: int,
    source_tag: str,
) -> SemidirectSurvivorBRSTBlock:
    """Build one finite naive semidirect survivor BRST block."""
    if not (
        len(shifted_current_labels) == len(c_ghost_labels) == len(b_ghost_labels) == len(chi_vector)
    ):
        raise ValueError("constraint labels and chi data must align")
    if not (
        len(survivor_labels) == len(internal_c_ghost_labels) == len(internal_b_ghost_labels)
    ):
        raise ValueError("survivor labels and internal ghost labels must align")

    num_constraints = len(c_ghost_labels)
    num_survivors = len(survivor_labels)
    basis_by_brst_degree: Dict[int, Tuple[SemidirectSurvivorBasisElement, ...]] = {}
    for brst_degree in range(
        -min(num_constraints, constraint_total_degree),
        num_constraints + min(num_survivors, max_internal_ce_degree) + 1,
    ):
        basis = semidirect_survivor_block_basis(
            num_constraints,
            num_survivors,
            constraint_total_degree,
            survivor_total_degree,
            max_internal_ce_degree,
            brst_degree,
        )
        if basis:
            basis_by_brst_degree[brst_degree] = basis

    differentials = {
        degree: semidirect_survivor_brst_differential(
            shifted_current_labels,
            survivor_labels,
            c_ghost_labels,
            b_ghost_labels,
            internal_c_ghost_labels,
            chi_vector,
            quadratic_terms,
            current_action_terms,
            survivor_action_terms,
            internal_quadratic_terms,
            internal_survivor_action_terms,
            constraint_total_degree,
            survivor_total_degree,
            max_internal_ce_degree,
            degree,
        )
        for degree in basis_by_brst_degree
        if semidirect_survivor_block_basis(
            num_constraints,
            num_survivors,
            constraint_total_degree,
            survivor_total_degree,
            max_internal_ce_degree,
            degree + 1,
        )
    }

    return SemidirectSurvivorBRSTBlock(
        source_tag=source_tag,
        shifted_current_labels=shifted_current_labels,
        survivor_labels=survivor_labels,
        c_ghost_labels=c_ghost_labels,
        b_ghost_labels=b_ghost_labels,
        internal_c_ghost_labels=internal_c_ghost_labels,
        internal_b_ghost_labels=internal_b_ghost_labels,
        chi_vector=chi_vector,
        quadratic_ghost_terms=quadratic_terms,
        current_action_terms=current_action_terms,
        survivor_action_terms=survivor_action_terms,
        internal_quadratic_ghost_terms=internal_quadratic_terms,
        internal_survivor_action_terms=internal_survivor_action_terms,
        constraint_total_degree=constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        basis_by_brst_degree=basis_by_brst_degree,
        differentials=differentials,
    )


def semidirect_survivor_block_homology_dimensions(
    block: SemidirectSurvivorBRSTBlock,
) -> Dict[int, int]:
    """Cohomology dimensions for one semidirect survivor BRST block."""
    return dict(semidirect_survivor_block_invariant_summary(block).homology_dimensions)


def semidirect_survivor_block_has_square_zero(block: SemidirectSurvivorBRSTBlock) -> bool:
    """Check d^2 = 0 on a semidirect survivor BRST block."""
    for degree, d_k in block.differentials.items():
        d_k1 = block.differentials.get(degree + 1)
        if d_k1 is None:
            continue
        if not _matrix_product_is_zero(d_k1, d_k):
            return False
    return True


def semidirect_survivor_block_is_acyclic(block: SemidirectSurvivorBRSTBlock) -> bool:
    """Check whether a semidirect survivor BRST block has zero cohomology."""
    return semidirect_survivor_block_invariant_summary(block).is_acyclic


def survivor_coupled_brst_differential(
    shifted_current_labels: Tuple[str, ...],
    survivor_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    b_ghost_labels: Tuple[str, ...],
    chi_vector: Tuple[object, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    current_action_terms: Tuple[CurrentActionTermEntry, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    constraint_total_degree: int,
    survivor_total_degree: int,
    brst_degree: int,
) -> Matrix:
    """BRST differential on a survivor-coupled finite block."""
    if not (
        len(shifted_current_labels) == len(c_ghost_labels) == len(b_ghost_labels) == len(chi_vector)
    ):
        raise ValueError("constraint labels and chi data must align")

    num_constraints = len(c_ghost_labels)
    num_survivors = len(survivor_labels)
    source_basis = survivor_coupled_block_basis(
        num_constraints,
        num_survivors,
        constraint_total_degree,
        survivor_total_degree,
        brst_degree,
    )
    target_basis = survivor_coupled_block_basis(
        num_constraints,
        num_survivors,
        constraint_total_degree,
        survivor_total_degree,
        brst_degree + 1,
    )
    matrix = zeros(len(target_basis), len(source_basis))
    if not source_basis or not target_basis:
        return matrix

    target_index = {basis: row for row, basis in enumerate(target_basis)}
    indexed_current_actions = _indexed_current_action_terms(
        shifted_current_labels,
        c_ghost_labels,
        b_ghost_labels,
        current_action_terms,
    )

    for col, (u_monomial, survivor_monomial, c_subset, b_subset) in enumerate(source_basis):
        for target_c_subset, coefficient in _ghost_brst_images_on_basis_element(
            c_subset,
            c_ghost_labels,
            chi_vector,
            quadratic_terms,
        ).items():
            target = (u_monomial, survivor_monomial, target_c_subset, b_subset)
            row = target_index[target]
            matrix[row, col] += coefficient

        c_sign = -1 if len(c_subset) % 2 else 1
        for position, b_var_index in enumerate(b_subset):
            target_u_monomial = list(u_monomial)
            target_u_monomial[b_var_index] += 1
            target = (
                tuple(target_u_monomial),
                survivor_monomial,
                c_subset,
                b_subset[:position] + b_subset[position + 1 :],
            )
            row = target_index[target]
            matrix[row, col] += c_sign * (-1 if position % 2 else 1)

        for c_ghost_index, action_terms in indexed_current_actions.items():
            inserted = _insert_ghost_index(c_subset, c_ghost_index)
            if inserted is None:
                continue
            insert_sign, target_c_subset = inserted

            for source_u, target_u, source_b, target_b, coefficient in action_terms:
                exponent = u_monomial[source_u]
                if exponent:
                    target_u_monomial = list(u_monomial)
                    target_u_monomial[source_u] -= 1
                    target_u_monomial[target_u] += 1
                    target = (
                        tuple(target_u_monomial),
                        survivor_monomial,
                        target_c_subset,
                        b_subset,
                    )
                    row = target_index[target]
                    matrix[row, col] += insert_sign * exponent * coefficient

                replaced = _replace_exterior_index(b_subset, source_b, target_b)
                if replaced is None:
                    continue
                b_sign, target_b_subset = replaced
                target = (u_monomial, survivor_monomial, target_c_subset, target_b_subset)
                row = target_index[target]
                matrix[row, col] += insert_sign * b_sign * coefficient

    matrix += survivor_action_differential(
        survivor_labels,
        c_ghost_labels,
        b_ghost_labels,
        survivor_action_terms,
        constraint_total_degree,
        survivor_total_degree,
        brst_degree,
    )
    return matrix


def build_survivor_coupled_brst_block(
    shifted_current_labels: Tuple[str, ...],
    survivor_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    b_ghost_labels: Tuple[str, ...],
    chi_vector: Tuple[object, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    current_action_terms: Tuple[CurrentActionTermEntry, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    constraint_total_degree: int,
    survivor_total_degree: int,
    source_tag: str,
) -> SurvivorCoupledBRSTBlock:
    """Build one finite survivor-coupled BRST block."""
    if not (
        len(shifted_current_labels) == len(c_ghost_labels) == len(b_ghost_labels) == len(chi_vector)
    ):
        raise ValueError("constraint labels and chi data must align")

    num_constraints = len(c_ghost_labels)
    num_survivors = len(survivor_labels)
    basis_by_brst_degree: Dict[int, Tuple[SurvivorCoupledBasisElement, ...]] = {}
    for brst_degree in range(-min(num_constraints, constraint_total_degree), num_constraints + 1):
        basis = survivor_coupled_block_basis(
            num_constraints,
            num_survivors,
            constraint_total_degree,
            survivor_total_degree,
            brst_degree,
        )
        if basis:
            basis_by_brst_degree[brst_degree] = basis

    differentials: Dict[int, Matrix] = {}
    for degree in basis_by_brst_degree:
        if degree + 1 not in basis_by_brst_degree:
            continue
        differentials[degree] = survivor_coupled_brst_differential(
            shifted_current_labels,
            survivor_labels,
            c_ghost_labels,
            b_ghost_labels,
            chi_vector,
            quadratic_terms,
            current_action_terms,
            survivor_action_terms,
            constraint_total_degree,
            survivor_total_degree,
            degree,
        )

    return SurvivorCoupledBRSTBlock(
        source_tag=source_tag,
        shifted_current_labels=shifted_current_labels,
        survivor_labels=survivor_labels,
        c_ghost_labels=c_ghost_labels,
        b_ghost_labels=b_ghost_labels,
        chi_vector=chi_vector,
        quadratic_ghost_terms=quadratic_terms,
        current_action_terms=current_action_terms,
        survivor_action_terms=survivor_action_terms,
        constraint_total_degree=constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        basis_by_brst_degree=basis_by_brst_degree,
        differentials=differentials,
    )


def build_internal_survivor_ce_block(
    survivor_labels: Tuple[str, ...],
    c_ghost_labels: Tuple[str, ...],
    b_ghost_labels: Tuple[str, ...],
    quadratic_terms: Tuple[QuadraticGhostTermEntry, ...],
    survivor_action_terms: Tuple[SurvivorActionTermEntry, ...],
    survivor_polynomial_degree: int,
    source_tag: str,
) -> InternalSurvivorCEBlock:
    """Build one finite internal CE block for the reduced survivor algebra."""
    if not (len(survivor_labels) == len(c_ghost_labels) == len(b_ghost_labels)):
        raise ValueError("survivor labels and internal ghost labels must align")

    num_survivors = len(survivor_labels)
    basis_by_ce_degree: Dict[int, Tuple[InternalSurvivorBasisElement, ...]] = {}
    for ce_degree in range(num_survivors + 1):
        basis = internal_survivor_ce_block_basis(
            num_survivors,
            survivor_polynomial_degree,
            ce_degree,
        )
        if basis:
            basis_by_ce_degree[ce_degree] = basis

    differentials = {
        degree: internal_survivor_ce_differential(
            survivor_labels,
            c_ghost_labels,
            quadratic_terms,
            survivor_action_terms,
            survivor_polynomial_degree,
            degree,
        )
        for degree in basis_by_ce_degree
        if internal_survivor_ce_block_basis(
            num_survivors,
            survivor_polynomial_degree,
            degree + 1,
        )
    }

    return InternalSurvivorCEBlock(
        source_tag=source_tag,
        survivor_labels=survivor_labels,
        c_ghost_labels=c_ghost_labels,
        b_ghost_labels=b_ghost_labels,
        quadratic_ghost_terms=quadratic_terms,
        survivor_action_terms=survivor_action_terms,
        survivor_polynomial_degree=survivor_polynomial_degree,
        basis_by_ce_degree=basis_by_ce_degree,
        differentials=differentials,
    )


def internal_survivor_ce_block_homology_dimensions(
    block: InternalSurvivorCEBlock,
) -> Dict[int, int]:
    """Cohomology dimensions for one internal reduced-survivor CE block."""
    dims: Dict[int, int] = {}
    for degree in sorted(block.basis_by_ce_degree):
        dim_c = len(block.basis_by_ce_degree[degree])
        d_curr = block.differentials.get(degree)
        d_prev = block.differentials.get(degree - 1)
        rank_curr = exact_matrix_rank(d_curr)
        rank_prev = exact_matrix_rank(d_prev)
        dims[degree] = (dim_c - rank_curr) - rank_prev
    return dims


def internal_survivor_ce_h0_basis(
    block: InternalSurvivorCEBlock,
) -> Tuple[Tuple[Tuple[Tuple[int, ...], object], ...], ...]:
    """Basis of H^0 represented on the CE degree-zero survivor monomials."""
    basis = block.basis_by_ce_degree.get(0, ())
    if not basis:
        return ()
    d0 = block.differentials.get(0)
    if d0 is None:
        return tuple((((basis_element[0], sympify(1)),),) for basis_element in basis)
    return tuple(
        tuple(
            (basis[index][0], simplify(vector[index, 0]))
            for index in range(vector.rows)
            if simplify(vector[index, 0]) != 0
        )
        for vector in d0.nullspace()
    )


def _survivor_monomial_label(
    survivor_labels: Tuple[str, ...],
    monomial: Tuple[int, ...],
) -> Tuple[Tuple[str, int], ...]:
    """Labeled survivor monomial from an exponent vector."""
    return tuple(
        (label, exponent)
        for label, exponent in zip(survivor_labels, monomial)
        if exponent
    )


def internal_survivor_h0_monomial_labels(
    block: InternalSurvivorCEBlock,
) -> Tuple[Tuple[Tuple[Tuple[Tuple[str, int], ...], object], ...], ...]:
    """H^0 basis with survivor monomials written in the labeled basis."""
    return tuple(
        tuple(
            (_survivor_monomial_label(block.survivor_labels, monomial), coefficient)
            for monomial, coefficient in vector
        )
        for vector in internal_survivor_ce_h0_basis(block)
    )


def internal_survivor_linear_h0_labels(
    block: InternalSurvivorCEBlock,
) -> Tuple[Tuple[Tuple[str, object], ...], ...]:
    """Linear H^0 representatives, when the survivor polynomial degree is one."""
    if block.survivor_polynomial_degree != 1:
        raise ValueError("linear H^0 labels are only defined at survivor polynomial degree 1")
    labels = []
    for vector in internal_survivor_ce_h0_basis(block):
        labels.append(
            tuple(
                (block.survivor_labels[monomial.index(1)], coefficient)
                for monomial, coefficient in vector
                if sum(monomial) == 1 and max(monomial) == 1
            )
        )
    return tuple(labels)


def internal_survivor_ce_block_has_square_zero(block: InternalSurvivorCEBlock) -> bool:
    """Check d^2 = 0 on an internal reduced-survivor CE block."""
    for degree, d_k in block.differentials.items():
        d_k1 = block.differentials.get(degree + 1)
        if d_k1 is None:
            continue
        if not _matrix_product_is_zero(d_k1, d_k):
            return False
    return True


def internal_survivor_ce_block_is_acyclic(block: InternalSurvivorCEBlock) -> bool:
    """Check whether an internal reduced-survivor CE block has zero cohomology."""
    return all(value == 0 for value in internal_survivor_ce_block_homology_dimensions(block).values())


def survivor_coupled_block_homology_dimensions(
    block: SurvivorCoupledBRSTBlock,
) -> Dict[int, int]:
    """Cohomology dimensions for one survivor-coupled BRST block."""
    return dict(survivor_coupled_block_invariant_summary(block).homology_dimensions)


def survivor_coupled_block_has_square_zero(block: SurvivorCoupledBRSTBlock) -> bool:
    """Check d^2 = 0 on a survivor-coupled block."""
    for degree, d_k in block.differentials.items():
        d_k1 = block.differentials.get(degree + 1)
        if d_k1 is None:
            continue
        if not _matrix_product_is_zero(d_k1, d_k):
            return False
    return True


def survivor_coupled_block_is_acyclic(block: SurvivorCoupledBRSTBlock) -> bool:
    """Check whether a survivor-coupled block has zero cohomology."""
    return all(value == 0 for value in survivor_coupled_block_homology_dimensions(block).values())


def mixed_constraint_ghost_block_homology_dimensions(
    block: MixedConstraintGhostBRSTBlock,
) -> Dict[int, int]:
    """Cohomology dimensions for one fixed mixed current-plus-ghost block."""
    return dict(mixed_constraint_ghost_block_invariant_summary(block).homology_dimensions)


def mixed_constraint_ghost_block_has_square_zero(block: MixedConstraintGhostBRSTBlock) -> bool:
    """Check d^2 = 0 on one mixed current-plus-ghost block."""
    for degree, d_k in block.differentials.items():
        d_k1 = block.differentials.get(degree + 1)
        if d_k1 is None:
            continue
        if not _matrix_product_is_zero(d_k1, d_k):
            return False
    return True


def mixed_constraint_ghost_block_is_acyclic(block: MixedConstraintGhostBRSTBlock) -> bool:
    """Check whether one mixed current-plus-ghost block has zero cohomology."""
    return all(value == 0 for value in mixed_constraint_ghost_block_homology_dimensions(block).values())


def chain_homology_dimensions(block: LinearConstraintBRSTBlock) -> Dict[int, int]:
    """Compute chain homology dimensions for a finite linear constraint block."""
    return dict(linear_constraint_block_invariant_summary(block).homology_dimensions)


def linear_constraint_block_has_square_zero(block: LinearConstraintBRSTBlock) -> bool:
    """Check d^2 = 0 for a linear constraint block."""
    for degree, d_k in block.differentials.items():
        d_km1 = block.differentials.get(degree - 1)
        if d_km1 is None:
            continue
        if not _matrix_product_is_zero(d_km1, d_k):
            return False
    return True


def linear_constraint_block_is_positive_acyclic(block: LinearConstraintBRSTBlock) -> bool:
    """Positive-total-degree Koszul blocks should be acyclic."""
    if block.total_degree == 0:
        return False
    return all(value == 0 for value in chain_homology_dimensions(block).values())


def linear_constraint_block_has_contracting_homotopy(block: LinearConstraintBRSTBlock) -> bool:
    """Check d h + h d = id on each positive-total-degree chain group."""
    if block.total_degree <= 0:
        return False

    num_constraints = len(block.ghost_labels)
    max_degree = max(block.basis_by_chain_degree)
    for degree in range(max_degree + 1):
        dim_c = len(block.basis_by_chain_degree[degree])
        identity = Matrix.eye(dim_c)
        d = block.differentials.get(degree)
        d_up = block.differentials.get(degree + 1)
        h = linear_constraint_contracting_homotopy(num_constraints, block.total_degree, degree)
        h_down = linear_constraint_contracting_homotopy(
            num_constraints, block.total_degree, degree - 1
        )

        lhs = zeros(dim_c, dim_c)
        if d_up is not None:
            lhs += d_up * h
        if d is not None:
            lhs += h_down * d
        if lhs != identity:
            return False

    return True


def sl3_subregular_linear_constraint_blocks(
    max_total_degree: int = 3,
) -> Tuple[LinearConstraintBRSTBlock, ...]:
    """Linear BRST/Koszul blocks for the subregular sl_3 constraint sector."""
    constraints = sl3_subregular_constraints()
    shifted_current_labels = tuple(f"u_{constraint.current_label}" for constraint in constraints)
    ghost_labels = tuple(constraint.b_ghost for constraint in constraints)
    return tuple(
        build_linear_constraint_koszul_block(
            shifted_current_labels=shifted_current_labels,
            ghost_labels=ghost_labels,
            total_degree=total_degree,
            source_tag=f"A2_subregular_linear_block_deg_{total_degree}",
        )
        for total_degree in range(max_total_degree + 1)
    )


def hook_pair_linear_constraint_blocks(
    n: int,
    r: int,
    max_total_degree: int = 3,
    num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[LinearConstraintBRSTBlock, ...], Tuple[LinearConstraintBRSTBlock, ...]]:
    """Linear BRST/Koszul blocks for one hook/subregular DS seed pair."""
    default_source_count, default_target_count = hook_pair_constraint_counts_ansatz_type_a(n, r)
    source_count = default_source_count if num_constraints is None else num_constraints
    if target_num_constraints is None:
        target_count = source_count if num_constraints is not None else default_target_count
    else:
        target_count = target_num_constraints
    if source_count < 1 or target_count < 1:
        raise ValueError("source/target constraint counts must be positive")

    case = nonprincipal_hook_case(n, r)
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    source_profile, target_profile = hook_pair_ghost_profiles(n, r)
    source_labels = tuple(
        item.root_label for item in _truncate_ghost_profile(source_profile, source_count, "source")
    )
    target_labels = tuple(
        item.root_label for item in _truncate_ghost_profile(target_profile, target_count, "target")
    )

    source_shifted_labels = tuple(f"u_source_{label}" for label in source_labels)
    source_ghost_labels = tuple(f"b_source_{label}" for label in source_labels)
    source_blocks = tuple(
        build_linear_constraint_koszul_block(
            shifted_current_labels=source_shifted_labels,
            ghost_labels=source_ghost_labels,
            total_degree=total_degree,
            source_tag=f"A{n-1}_hook_source_{partition_tag}_linear_block_deg_{total_degree}",
        )
        for total_degree in range(max_total_degree + 1)
    )

    target_shifted_labels = tuple(f"u_target_{label}" for label in target_labels)
    target_ghost_labels = tuple(f"b_target_{label}" for label in target_labels)
    target_blocks = tuple(
        build_linear_constraint_koszul_block(
            shifted_current_labels=target_shifted_labels,
            ghost_labels=target_ghost_labels,
            total_degree=total_degree,
            source_tag=f"A{n-1}_hook_target_{dual_tag}_linear_block_deg_{total_degree}",
        )
        for total_degree in range(max_total_degree + 1)
    )
    return source_blocks, target_blocks


def first_nonselfdual_hook_pair_linear_constraint_blocks(
    max_total_degree: int = 3,
) -> Tuple[Tuple[LinearConstraintBRSTBlock, ...], Tuple[LinearConstraintBRSTBlock, ...]]:
    """Linear BRST/Koszul blocks for the first non-self-dual hook-pair seed."""
    source_profile, target_profile = first_nonselfdual_hook_pair_ghost_profiles()
    source_labels = tuple(item.root_label for item in source_profile)
    target_labels = tuple(item.root_label for item in target_profile)
    source_blocks = tuple(
        build_linear_constraint_koszul_block(
            shifted_current_labels=tuple(f"u_source_{label}" for label in source_labels),
            ghost_labels=tuple(f"b_source_{label}" for label in source_labels),
            total_degree=total_degree,
            source_tag=f"A3_hook_source_3_1_linear_block_deg_{total_degree}",
        )
        for total_degree in range(max_total_degree + 1)
    )
    target_blocks = tuple(
        build_linear_constraint_koszul_block(
            shifted_current_labels=tuple(f"u_target_{label}" for label in target_labels),
            ghost_labels=tuple(f"b_target_{label}" for label in target_labels),
            total_degree=total_degree,
            source_tag=f"A3_hook_target_2_1_1_linear_block_deg_{total_degree}",
        )
        for total_degree in range(max_total_degree + 1)
    )
    return source_blocks, target_blocks


def nonprincipal_partition_pair_mixed_constraint_ghost_blocks(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[MixedConstraintGhostBRSTBlock, ...], Tuple[MixedConstraintGhostBRSTBlock, ...]]:
    """Mixed current-plus-ghost BRST blocks for one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_constraints, target_constraints = partition_pair_constraints(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_character, target_character = partition_pair_constraint_characters(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_quadratic, target_quadratic = partition_pair_quadratic_ghost_term_support(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    family_tag = case.family
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_mixed_constraint_ghost_brst_block(
                shifted_current_labels=tuple(f"u_source_{item.root_label}" for item in source_constraints),
                c_ghost_labels=tuple(item.c_ghost for item in source_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in source_constraints),
                chi_vector=tuple(source_character[item.root_label] for item in source_constraints),
                quadratic_terms=source_quadratic,
                constraint_total_degree=total_degree,
                source_tag=f"A{n-1}_{family_tag}_source_{partition_tag}_mixed_{total_degree}",
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
        tuple(
            build_mixed_constraint_ghost_brst_block(
                shifted_current_labels=tuple(f"u_target_{item.root_label}" for item in target_constraints),
                c_ghost_labels=tuple(item.c_ghost for item in target_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in target_constraints),
                chi_vector=tuple(target_character[item.root_label] for item in target_constraints),
                quadratic_terms=target_quadratic,
                constraint_total_degree=total_degree,
                source_tag=f"A{n-1}_{family_tag}_target_{dual_tag}_mixed_{total_degree}",
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
    )


def nonprincipal_partition_pair_nonlinear_mixed_constraint_ghost_blocks(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[MixedConstraintGhostBRSTBlock, ...], Tuple[MixedConstraintGhostBRSTBlock, ...]]:
    """Mixed blocks with nonlinear current-action terms for one partition pair."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_constraints, target_constraints = partition_pair_constraints(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_character, target_character = partition_pair_constraint_characters(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_quadratic, target_quadratic = partition_pair_quadratic_ghost_term_support(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_action, target_action = partition_pair_current_action_terms(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    family_tag = case.family
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_mixed_constraint_ghost_brst_block(
                shifted_current_labels=tuple(f"u_source_{item.root_label}" for item in source_constraints),
                c_ghost_labels=tuple(item.c_ghost for item in source_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in source_constraints),
                chi_vector=tuple(source_character[item.root_label] for item in source_constraints),
                quadratic_terms=source_quadratic,
                current_action_terms=source_action,
                constraint_total_degree=total_degree,
                source_tag=f"A{n-1}_{family_tag}_source_{partition_tag}_nonlinear_{total_degree}",
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
        tuple(
            build_mixed_constraint_ghost_brst_block(
                shifted_current_labels=tuple(f"u_target_{item.root_label}" for item in target_constraints),
                c_ghost_labels=tuple(item.c_ghost for item in target_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in target_constraints),
                chi_vector=tuple(target_character[item.root_label] for item in target_constraints),
                quadratic_terms=target_quadratic,
                current_action_terms=target_action,
                constraint_total_degree=total_degree,
                source_tag=f"A{n-1}_{family_tag}_target_{dual_tag}_nonlinear_{total_degree}",
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
    )


@lru_cache(maxsize=64)
def _partition_pair_external_constraint_data(
    partition: Tuple[int, ...],
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[
    Tuple[
        Tuple[str, ...],
        Tuple[str, ...],
        Tuple[str, ...],
        Tuple[object, ...],
        Tuple[QuadraticGhostTermEntry, ...],
        Tuple[CurrentActionTermEntry, ...],
    ],
    Tuple[
        Tuple[str, ...],
        Tuple[str, ...],
        Tuple[str, ...],
        Tuple[object, ...],
        Tuple[QuadraticGhostTermEntry, ...],
        Tuple[CurrentActionTermEntry, ...],
    ],
]:
    """Shared external constraint-sector data for one non-principal partition pair."""
    source_constraints, target_constraints = partition_pair_constraints(
        partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_character, target_character = partition_pair_constraint_characters(
        partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_quadratic, target_quadratic = partition_pair_quadratic_ghost_term_support(
        partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_current_action, target_current_action = partition_pair_current_action_terms(
        partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return (
        (
            tuple(f"u_source_{item.root_label}" for item in source_constraints),
            tuple(item.c_ghost for item in source_constraints),
            tuple(item.b_ghost for item in source_constraints),
            tuple(source_character[item.root_label] for item in source_constraints),
            source_quadratic,
            source_current_action,
        ),
        (
            tuple(f"u_target_{item.root_label}" for item in target_constraints),
            tuple(item.c_ghost for item in target_constraints),
            tuple(item.b_ghost for item in target_constraints),
            tuple(target_character[item.root_label] for item in target_constraints),
            target_quadratic,
            target_current_action,
        ),
    )


@lru_cache(maxsize=64)
def _partition_pair_survivor_labels(
    partition: Tuple[int, ...],
) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    """Survivor labels for one non-principal partition pair."""
    source_survivors, target_survivors = partition_pair_surviving_field_candidates(partition)
    return (
        tuple(item.label for item in source_survivors),
        tuple(item.label for item in target_survivors),
    )


@lru_cache(maxsize=64)
def _partition_pair_internal_survivor_data(
    partition: Tuple[int, ...],
) -> Tuple[
    Tuple[
        Tuple[str, ...],
        Tuple[str, ...],
        Tuple[QuadraticGhostTermEntry, ...],
        Tuple[SurvivorActionTermEntry, ...],
    ],
    Tuple[
        Tuple[str, ...],
        Tuple[str, ...],
        Tuple[QuadraticGhostTermEntry, ...],
        Tuple[SurvivorActionTermEntry, ...],
    ],
]:
    """Shared internal survivor CE-sector data for one non-principal partition pair."""
    source_survivor_labels, target_survivor_labels = _partition_pair_survivor_labels(partition)
    source_internal_c_ghosts, source_internal_b_ghosts = internal_survivor_ghost_labels(
        source_survivor_labels
    )
    target_internal_c_ghosts, target_internal_b_ghosts = internal_survivor_ghost_labels(
        target_survivor_labels
    )
    source_reduced_brackets, target_reduced_brackets = partition_pair_reduced_brackets(partition)
    source_internal_quadratic = internal_survivor_quadratic_ghost_terms(
        source_survivor_labels,
        source_reduced_brackets,
    )
    target_internal_quadratic = internal_survivor_quadratic_ghost_terms(
        target_survivor_labels,
        target_reduced_brackets,
    )
    source_internal_action = internal_survivor_action_terms(
        source_survivor_labels,
        source_reduced_brackets,
    )
    target_internal_action = internal_survivor_action_terms(
        target_survivor_labels,
        target_reduced_brackets,
    )
    return (
        (
            source_internal_c_ghosts,
            source_internal_b_ghosts,
            source_internal_quadratic,
            source_internal_action,
        ),
        (
            target_internal_c_ghosts,
            target_internal_b_ghosts,
            target_internal_quadratic,
            target_internal_action,
        ),
    )


@lru_cache(maxsize=64)
def nonprincipal_partition_pair_survivor_coupled_blocks(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorCoupledBRSTBlock, ...], Tuple[SurvivorCoupledBRSTBlock, ...]]:
    """Survivor-coupled BRST blocks for one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    (source_data, target_data) = _partition_pair_external_constraint_data(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivor_action, target_survivor_action = partition_pair_survivor_action_terms(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivor_labels, target_survivor_labels = _partition_pair_survivor_labels(case.partition)
    family_tag = case.family
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_survivor_coupled_brst_block(
                shifted_current_labels=source_data[0],
                survivor_labels=source_survivor_labels,
                c_ghost_labels=source_data[1],
                b_ghost_labels=source_data[2],
                chi_vector=source_data[3],
                quadratic_terms=source_data[4],
                current_action_terms=source_data[5],
                survivor_action_terms=source_survivor_action,
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                source_tag=(
                    f"A{n-1}_{family_tag}_source_{partition_tag}_survivor_coupled_"
                    f"{total_degree}_{survivor_total_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
        tuple(
            build_survivor_coupled_brst_block(
                shifted_current_labels=target_data[0],
                survivor_labels=target_survivor_labels,
                c_ghost_labels=target_data[1],
                b_ghost_labels=target_data[2],
                chi_vector=target_data[3],
                quadratic_terms=target_data[4],
                current_action_terms=target_data[5],
                survivor_action_terms=target_survivor_action,
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                source_tag=(
                    f"A{n-1}_{family_tag}_target_{dual_tag}_survivor_coupled_"
                    f"{total_degree}_{survivor_total_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
    )


@lru_cache(maxsize=64)
def partition_pair_internal_survivor_ce_blocks(
    partition: Tuple[int, ...],
    max_survivor_polynomial_degree: int = 2,
) -> Tuple[Tuple[InternalSurvivorCEBlock, ...], Tuple[InternalSurvivorCEBlock, ...]]:
    """Internal reduced-survivor CE blocks for one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_labels, target_labels = _partition_pair_survivor_labels(case.partition)
    source_data, target_data = _partition_pair_internal_survivor_data(case.partition)
    family_tag = case.family
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_internal_survivor_ce_block(
                survivor_labels=source_labels,
                c_ghost_labels=source_data[0],
                b_ghost_labels=source_data[1],
                quadratic_terms=source_data[2],
                survivor_action_terms=source_data[3],
                survivor_polynomial_degree=degree,
                source_tag=f"A{n-1}_{family_tag}_source_{partition_tag}_internal_survivor_{degree}",
            )
            for degree in range(max_survivor_polynomial_degree + 1)
        ),
        tuple(
            build_internal_survivor_ce_block(
                survivor_labels=target_labels,
                c_ghost_labels=target_data[0],
                b_ghost_labels=target_data[1],
                quadratic_terms=target_data[2],
                survivor_action_terms=target_data[3],
                survivor_polynomial_degree=degree,
                source_tag=f"A{n-1}_{family_tag}_target_{dual_tag}_internal_survivor_{degree}",
            )
            for degree in range(max_survivor_polynomial_degree + 1)
        ),
    )


@lru_cache(maxsize=64)
def nonprincipal_partition_pair_semidirect_survivor_blocks(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SemidirectSurvivorBRSTBlock, ...], Tuple[SemidirectSurvivorBRSTBlock, ...]]:
    """Naive semidirect survivor BRST blocks for one non-principal partition pair."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_data, target_data = _partition_pair_external_constraint_data(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivor_action, target_survivor_action = partition_pair_survivor_action_terms(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivor_labels, target_survivor_labels = _partition_pair_survivor_labels(case.partition)
    source_internal_data, target_internal_data = _partition_pair_internal_survivor_data(
        case.partition
    )
    family_tag = case.family
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_semidirect_survivor_brst_block(
                shifted_current_labels=source_data[0],
                survivor_labels=source_survivor_labels,
                c_ghost_labels=source_data[1],
                b_ghost_labels=source_data[2],
                internal_c_ghost_labels=source_internal_data[0],
                internal_b_ghost_labels=source_internal_data[1],
                chi_vector=source_data[3],
                quadratic_terms=source_data[4],
                current_action_terms=source_data[5],
                survivor_action_terms=source_survivor_action,
                internal_quadratic_terms=source_internal_data[2],
                internal_survivor_action_terms=source_internal_data[3],
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
                source_tag=(
                    f"A{n-1}_{family_tag}_source_{partition_tag}_semidirect_survivor_"
                    f"{total_degree}_{survivor_total_degree}_{max_internal_ce_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
        tuple(
            build_semidirect_survivor_brst_block(
                shifted_current_labels=target_data[0],
                survivor_labels=target_survivor_labels,
                c_ghost_labels=target_data[1],
                b_ghost_labels=target_data[2],
                internal_c_ghost_labels=target_internal_data[0],
                internal_b_ghost_labels=target_internal_data[1],
                chi_vector=target_data[3],
                quadratic_terms=target_data[4],
                current_action_terms=target_data[5],
                survivor_action_terms=target_survivor_action,
                internal_quadratic_terms=target_internal_data[2],
                internal_survivor_action_terms=target_internal_data[3],
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
                source_tag=(
                    f"A{n-1}_{family_tag}_target_{dual_tag}_semidirect_survivor_"
                    f"{total_degree}_{survivor_total_degree}_{max_internal_ce_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
    )


@lru_cache(maxsize=64)
def nonprincipal_partition_pair_corrected_semidirect_survivor_blocks(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SemidirectSurvivorBRSTBlock, ...], Tuple[SemidirectSurvivorBRSTBlock, ...]]:
    """Semidirect survivor blocks after the first transferred correction on one partition pair."""
    case = nonprincipal_type_a_case(partition)
    n = partition_size(case.partition)
    source_data, target_data = _partition_pair_external_constraint_data(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivor_action, target_survivor_action = partition_pair_corrected_survivor_action_terms(
        case.partition,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivor_labels, target_survivor_labels = _partition_pair_survivor_labels(case.partition)
    source_internal_data, target_internal_data = _partition_pair_internal_survivor_data(
        case.partition
    )
    family_tag = case.family
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_semidirect_survivor_brst_block(
                shifted_current_labels=source_data[0],
                survivor_labels=source_survivor_labels,
                c_ghost_labels=source_data[1],
                b_ghost_labels=source_data[2],
                internal_c_ghost_labels=source_internal_data[0],
                internal_b_ghost_labels=source_internal_data[1],
                chi_vector=source_data[3],
                quadratic_terms=source_data[4],
                current_action_terms=source_data[5],
                survivor_action_terms=source_survivor_action,
                internal_quadratic_terms=source_internal_data[2],
                internal_survivor_action_terms=source_internal_data[3],
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
                source_tag=(
                    f"A{n-1}_{family_tag}_source_{partition_tag}_corrected_semidirect_"
                    f"{total_degree}_{survivor_total_degree}_{max_internal_ce_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
        tuple(
            build_semidirect_survivor_brst_block(
                shifted_current_labels=target_data[0],
                survivor_labels=target_survivor_labels,
                c_ghost_labels=target_data[1],
                b_ghost_labels=target_data[2],
                internal_c_ghost_labels=target_internal_data[0],
                internal_b_ghost_labels=target_internal_data[1],
                chi_vector=target_data[3],
                quadratic_terms=target_data[4],
                current_action_terms=target_data[5],
                survivor_action_terms=target_survivor_action,
                internal_quadratic_terms=target_internal_data[2],
                internal_survivor_action_terms=target_internal_data[3],
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
                source_tag=(
                    f"A{n-1}_{family_tag}_target_{dual_tag}_corrected_semidirect_"
                    f"{total_degree}_{survivor_total_degree}_{max_internal_ce_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
    )


def nonprincipal_two_row_mixed_constraint_ghost_blocks(
    n: int,
    s: int,
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[MixedConstraintGhostBRSTBlock, ...], Tuple[MixedConstraintGhostBRSTBlock, ...]]:
    """Mixed current-plus-ghost BRST blocks for one type-A two-row non-hook orbit."""
    return nonprincipal_partition_pair_mixed_constraint_ghost_blocks(
        two_row_nonhook_partition(n, s),
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )


def nonprincipal_two_row_nonlinear_mixed_constraint_ghost_blocks(
    n: int,
    s: int,
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[MixedConstraintGhostBRSTBlock, ...], Tuple[MixedConstraintGhostBRSTBlock, ...]]:
    """Mixed blocks with nonlinear current terms for one type-A two-row non-hook orbit."""
    return nonprincipal_partition_pair_nonlinear_mixed_constraint_ghost_blocks(
        two_row_nonhook_partition(n, s),
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )


def nonprincipal_two_row_survivor_coupled_blocks(
    n: int,
    s: int,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorCoupledBRSTBlock, ...], Tuple[SurvivorCoupledBRSTBlock, ...]]:
    """Survivor-coupled BRST blocks for one type-A two-row non-hook orbit."""
    return nonprincipal_partition_pair_survivor_coupled_blocks(
        two_row_nonhook_partition(n, s),
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )


def nonprincipal_two_row_internal_survivor_ce_blocks(
    n: int,
    s: int,
    max_survivor_polynomial_degree: int = 2,
) -> Tuple[Tuple[InternalSurvivorCEBlock, ...], Tuple[InternalSurvivorCEBlock, ...]]:
    """Internal reduced-survivor CE blocks for one type-A two-row non-hook orbit."""
    return partition_pair_internal_survivor_ce_blocks(
        two_row_nonhook_partition(n, s),
        max_survivor_polynomial_degree=max_survivor_polynomial_degree,
    )


def nonprincipal_two_row_semidirect_survivor_blocks(
    n: int,
    s: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SemidirectSurvivorBRSTBlock, ...], Tuple[SemidirectSurvivorBRSTBlock, ...]]:
    """Naive semidirect survivor BRST blocks for one type-A two-row non-hook orbit."""
    return nonprincipal_partition_pair_semidirect_survivor_blocks(
        two_row_nonhook_partition(n, s),
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )


def nonprincipal_two_row_corrected_semidirect_survivor_blocks(
    n: int,
    s: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SemidirectSurvivorBRSTBlock, ...], Tuple[SemidirectSurvivorBRSTBlock, ...]]:
    """Corrected semidirect survivor BRST blocks for one type-A two-row non-hook orbit."""
    return nonprincipal_partition_pair_corrected_semidirect_survivor_blocks(
        two_row_nonhook_partition(n, s),
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )


def hook_pair_mixed_constraint_ghost_blocks(
    n: int,
    r: int,
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[MixedConstraintGhostBRSTBlock, ...], Tuple[MixedConstraintGhostBRSTBlock, ...]]:
    """Mixed current-plus-ghost BRST blocks for one hook/subregular pair."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_character, target_character = hook_pair_constraint_characters(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_quadratic, target_quadratic = hook_pair_quadratic_ghost_term_support(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    case = nonprincipal_hook_case(n, r)
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_mixed_constraint_ghost_brst_block(
                shifted_current_labels=tuple(f"u_source_{item.root_label}" for item in source_constraints),
                c_ghost_labels=tuple(item.c_ghost for item in source_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in source_constraints),
                chi_vector=tuple(source_character[item.root_label] for item in source_constraints),
                quadratic_terms=source_quadratic,
                constraint_total_degree=total_degree,
                source_tag=f"A{n-1}_hook_source_{partition_tag}_mixed_{total_degree}",
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
        tuple(
            build_mixed_constraint_ghost_brst_block(
                shifted_current_labels=tuple(f"u_target_{item.root_label}" for item in target_constraints),
                c_ghost_labels=tuple(item.c_ghost for item in target_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in target_constraints),
                chi_vector=tuple(target_character[item.root_label] for item in target_constraints),
                quadratic_terms=target_quadratic,
                constraint_total_degree=total_degree,
                source_tag=f"A{n-1}_hook_target_{dual_tag}_mixed_{total_degree}",
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
    )


def hook_pair_nonlinear_mixed_constraint_ghost_blocks(
    n: int,
    r: int,
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[MixedConstraintGhostBRSTBlock, ...], Tuple[MixedConstraintGhostBRSTBlock, ...]]:
    """Mixed blocks with nonlinear current-action terms for one hook/subregular pair."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_character, target_character = hook_pair_constraint_characters(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_quadratic, target_quadratic = hook_pair_quadratic_ghost_term_support(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_action, target_action = hook_pair_current_action_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    case = nonprincipal_hook_case(n, r)
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_mixed_constraint_ghost_brst_block(
                shifted_current_labels=tuple(f"u_source_{item.root_label}" for item in source_constraints),
                c_ghost_labels=tuple(item.c_ghost for item in source_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in source_constraints),
                chi_vector=tuple(source_character[item.root_label] for item in source_constraints),
                quadratic_terms=source_quadratic,
                current_action_terms=source_action,
                constraint_total_degree=total_degree,
                source_tag=f"A{n-1}_hook_source_{partition_tag}_nonlinear_{total_degree}",
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
        tuple(
            build_mixed_constraint_ghost_brst_block(
                shifted_current_labels=tuple(f"u_target_{item.root_label}" for item in target_constraints),
                c_ghost_labels=tuple(item.c_ghost for item in target_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in target_constraints),
                chi_vector=tuple(target_character[item.root_label] for item in target_constraints),
                quadratic_terms=target_quadratic,
                current_action_terms=target_action,
                constraint_total_degree=total_degree,
                source_tag=f"A{n-1}_hook_target_{dual_tag}_nonlinear_{total_degree}",
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
    )


@lru_cache(maxsize=64)
def hook_pair_survivor_coupled_blocks(
    n: int,
    r: int,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SurvivorCoupledBRSTBlock, ...], Tuple[SurvivorCoupledBRSTBlock, ...]]:
    """Survivor-coupled BRST blocks for one hook pair."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_character, target_character = hook_pair_constraint_characters(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_quadratic, target_quadratic = hook_pair_quadratic_ghost_term_support(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_current_action, target_current_action = hook_pair_current_action_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivor_action, target_survivor_action = hook_pair_survivor_action_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivors, target_survivors = hook_pair_surviving_field_candidates(n, r)
    case = nonprincipal_hook_case(n, r)
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_survivor_coupled_brst_block(
                shifted_current_labels=tuple(
                    f"u_source_{item.root_label}" for item in source_constraints
                ),
                survivor_labels=tuple(item.label for item in source_survivors),
                c_ghost_labels=tuple(item.c_ghost for item in source_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in source_constraints),
                chi_vector=tuple(source_character[item.root_label] for item in source_constraints),
                quadratic_terms=source_quadratic,
                current_action_terms=source_current_action,
                survivor_action_terms=source_survivor_action,
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                source_tag=(
                    f"A{n-1}_hook_source_{partition_tag}_survivor_coupled_"
                    f"{total_degree}_{survivor_total_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
        tuple(
            build_survivor_coupled_brst_block(
                shifted_current_labels=tuple(
                    f"u_target_{item.root_label}" for item in target_constraints
                ),
                survivor_labels=tuple(item.label for item in target_survivors),
                c_ghost_labels=tuple(item.c_ghost for item in target_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in target_constraints),
                chi_vector=tuple(target_character[item.root_label] for item in target_constraints),
                quadratic_terms=target_quadratic,
                current_action_terms=target_current_action,
                survivor_action_terms=target_survivor_action,
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                source_tag=(
                    f"A{n-1}_hook_target_{dual_tag}_survivor_coupled_"
                    f"{total_degree}_{survivor_total_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
    )


def hook_pair_semidirect_survivor_blocks(
    n: int,
    r: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SemidirectSurvivorBRSTBlock, ...], Tuple[SemidirectSurvivorBRSTBlock, ...]]:
    """Naive semidirect survivor BRST blocks for one hook pair."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_character, target_character = hook_pair_constraint_characters(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_quadratic, target_quadratic = hook_pair_quadratic_ghost_term_support(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_current_action, target_current_action = hook_pair_current_action_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivor_action, target_survivor_action = hook_pair_survivor_action_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivors, target_survivors = hook_pair_surviving_field_candidates(n, r)
    source_survivor_labels = tuple(item.label for item in source_survivors)
    target_survivor_labels = tuple(item.label for item in target_survivors)
    source_internal_c_ghosts, source_internal_b_ghosts = internal_survivor_ghost_labels(
        source_survivor_labels
    )
    target_internal_c_ghosts, target_internal_b_ghosts = internal_survivor_ghost_labels(
        target_survivor_labels
    )
    source_reduced_brackets, target_reduced_brackets = hook_pair_reduced_brackets(n, r)
    source_internal_quadratic = internal_survivor_quadratic_ghost_terms(
        source_survivor_labels,
        source_reduced_brackets,
    )
    target_internal_quadratic = internal_survivor_quadratic_ghost_terms(
        target_survivor_labels,
        target_reduced_brackets,
    )
    source_internal_action = internal_survivor_action_terms(
        source_survivor_labels,
        source_reduced_brackets,
    )
    target_internal_action = internal_survivor_action_terms(
        target_survivor_labels,
        target_reduced_brackets,
    )
    case = nonprincipal_hook_case(n, r)
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_semidirect_survivor_brst_block(
                shifted_current_labels=tuple(
                    f"u_source_{item.root_label}" for item in source_constraints
                ),
                survivor_labels=source_survivor_labels,
                c_ghost_labels=tuple(item.c_ghost for item in source_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in source_constraints),
                internal_c_ghost_labels=source_internal_c_ghosts,
                internal_b_ghost_labels=source_internal_b_ghosts,
                chi_vector=tuple(source_character[item.root_label] for item in source_constraints),
                quadratic_terms=source_quadratic,
                current_action_terms=source_current_action,
                survivor_action_terms=source_survivor_action,
                internal_quadratic_terms=source_internal_quadratic,
                internal_survivor_action_terms=source_internal_action,
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
                source_tag=(
                    f"A{n-1}_hook_source_{partition_tag}_semidirect_survivor_"
                    f"{total_degree}_{survivor_total_degree}_{max_internal_ce_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
        tuple(
            build_semidirect_survivor_brst_block(
                shifted_current_labels=tuple(
                    f"u_target_{item.root_label}" for item in target_constraints
                ),
                survivor_labels=target_survivor_labels,
                c_ghost_labels=tuple(item.c_ghost for item in target_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in target_constraints),
                internal_c_ghost_labels=target_internal_c_ghosts,
                internal_b_ghost_labels=target_internal_b_ghosts,
                chi_vector=tuple(target_character[item.root_label] for item in target_constraints),
                quadratic_terms=target_quadratic,
                current_action_terms=target_current_action,
                survivor_action_terms=target_survivor_action,
                internal_quadratic_terms=target_internal_quadratic,
                internal_survivor_action_terms=target_internal_action,
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
                source_tag=(
                    f"A{n-1}_hook_target_{dual_tag}_semidirect_survivor_"
                    f"{total_degree}_{survivor_total_degree}_{max_internal_ce_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
    )


@lru_cache(maxsize=64)
def hook_pair_corrected_semidirect_survivor_blocks(
    n: int,
    r: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[Tuple[SemidirectSurvivorBRSTBlock, ...], Tuple[SemidirectSurvivorBRSTBlock, ...]]:
    """Hook-pair semidirect survivor blocks after the first transferred correction."""
    source_constraints, target_constraints = hook_pair_constraints(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_character, target_character = hook_pair_constraint_characters(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_quadratic, target_quadratic = hook_pair_quadratic_ghost_term_support(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_current_action, target_current_action = hook_pair_current_action_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivor_action, target_survivor_action = hook_pair_corrected_survivor_action_terms(
        n,
        r,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    source_survivors, target_survivors = hook_pair_surviving_field_candidates(n, r)
    source_survivor_labels = tuple(item.label for item in source_survivors)
    target_survivor_labels = tuple(item.label for item in target_survivors)
    source_internal_c_ghosts, source_internal_b_ghosts = internal_survivor_ghost_labels(
        source_survivor_labels
    )
    target_internal_c_ghosts, target_internal_b_ghosts = internal_survivor_ghost_labels(
        target_survivor_labels
    )
    source_reduced_brackets, target_reduced_brackets = hook_pair_reduced_brackets(n, r)
    source_internal_quadratic = internal_survivor_quadratic_ghost_terms(
        source_survivor_labels,
        source_reduced_brackets,
    )
    target_internal_quadratic = internal_survivor_quadratic_ghost_terms(
        target_survivor_labels,
        target_reduced_brackets,
    )
    source_internal_action = internal_survivor_action_terms(
        source_survivor_labels,
        source_reduced_brackets,
    )
    target_internal_action = internal_survivor_action_terms(
        target_survivor_labels,
        target_reduced_brackets,
    )
    case = nonprincipal_hook_case(n, r)
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)
    return (
        tuple(
            build_semidirect_survivor_brst_block(
                shifted_current_labels=tuple(
                    f"u_source_{item.root_label}" for item in source_constraints
                ),
                survivor_labels=source_survivor_labels,
                c_ghost_labels=tuple(item.c_ghost for item in source_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in source_constraints),
                internal_c_ghost_labels=source_internal_c_ghosts,
                internal_b_ghost_labels=source_internal_b_ghosts,
                chi_vector=tuple(source_character[item.root_label] for item in source_constraints),
                quadratic_terms=source_quadratic,
                current_action_terms=source_current_action,
                survivor_action_terms=source_survivor_action,
                internal_quadratic_terms=source_internal_quadratic,
                internal_survivor_action_terms=source_internal_action,
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
                source_tag=(
                    f"A{n-1}_hook_source_{partition_tag}_corrected_semidirect_"
                    f"{total_degree}_{survivor_total_degree}_{max_internal_ce_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
        tuple(
            build_semidirect_survivor_brst_block(
                shifted_current_labels=tuple(
                    f"u_target_{item.root_label}" for item in target_constraints
                ),
                survivor_labels=target_survivor_labels,
                c_ghost_labels=tuple(item.c_ghost for item in target_constraints),
                b_ghost_labels=tuple(item.b_ghost for item in target_constraints),
                internal_c_ghost_labels=target_internal_c_ghosts,
                internal_b_ghost_labels=target_internal_b_ghosts,
                chi_vector=tuple(target_character[item.root_label] for item in target_constraints),
                quadratic_terms=target_quadratic,
                current_action_terms=target_current_action,
                survivor_action_terms=target_survivor_action,
                internal_quadratic_terms=target_internal_quadratic,
                internal_survivor_action_terms=target_internal_action,
                constraint_total_degree=total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
                source_tag=(
                    f"A{n-1}_hook_target_{dual_tag}_corrected_semidirect_"
                    f"{total_degree}_{survivor_total_degree}_{max_internal_ce_degree}"
                ),
            )
            for total_degree in range(max_constraint_total_degree + 1)
        ),
    )


@lru_cache(maxsize=64)
def _partition_pair_semidirect_square_zero_flags(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[bool, ...]:
    """Cached square-zero profile for one naive non-principal semidirect family."""
    source_blocks, target_blocks = nonprincipal_partition_pair_semidirect_survivor_blocks(
        partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return tuple(
        semidirect_survivor_block_has_square_zero(block)
        for block in source_blocks + target_blocks
    )


@lru_cache(maxsize=64)
def _partition_pair_corrected_semidirect_square_zero_flags(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[bool, ...]:
    """Cached square-zero profile for one corrected non-principal semidirect family."""
    source_blocks, target_blocks = nonprincipal_partition_pair_corrected_semidirect_survivor_blocks(
        partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return tuple(
        semidirect_survivor_block_has_square_zero(block)
        for block in source_blocks + target_blocks
    )


@lru_cache(maxsize=64)
def _partition_pair_survivor_coupled_square_zero_flags(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[bool, ...]:
    """Cached square-zero profile for one non-principal survivor-coupled family."""
    source_blocks, target_blocks = nonprincipal_partition_pair_survivor_coupled_blocks(
        partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return tuple(
        survivor_coupled_block_has_square_zero(block)
        for block in source_blocks + target_blocks
    )


@lru_cache(maxsize=64)
def _partition_pair_survivor_coupled_source_square_zero_flags(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[bool, ...]:
    """Cached square-zero profile for the source side of one survivor-coupled family."""
    source_blocks, _ = nonprincipal_partition_pair_survivor_coupled_blocks(
        partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return tuple(
        survivor_coupled_block_has_square_zero(block)
        for block in source_blocks
    )


@lru_cache(maxsize=64)
def _partition_pair_corrected_semidirect_source_square_zero_flags(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[bool, ...]:
    """Cached square-zero profile for the source side of one corrected semidirect family."""
    source_blocks, _ = nonprincipal_partition_pair_corrected_semidirect_survivor_blocks(
        partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return tuple(
        semidirect_survivor_block_has_square_zero(block)
        for block in source_blocks
    )


@lru_cache(maxsize=64)
def _hook_pair_semidirect_square_zero_flags(
    n: int,
    r: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[bool, ...]:
    """Cached square-zero profile for one hook-pair naive semidirect family."""
    source_blocks, target_blocks = hook_pair_semidirect_survivor_blocks(
        n,
        r,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return tuple(
        semidirect_survivor_block_has_square_zero(block)
        for block in source_blocks + target_blocks
    )


@lru_cache(maxsize=64)
def _hook_pair_corrected_semidirect_square_zero_flags(
    n: int,
    r: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[bool, ...]:
    """Cached square-zero profile for one hook-pair corrected semidirect family."""
    source_blocks, target_blocks = hook_pair_corrected_semidirect_survivor_blocks(
        n,
        r,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return tuple(
        semidirect_survivor_block_has_square_zero(block)
        for block in source_blocks + target_blocks
    )


@lru_cache(maxsize=64)
def _hook_pair_corrected_semidirect_source_square_zero_flags(
    n: int,
    r: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> Tuple[bool, ...]:
    """Cached source-side square-zero profile for one corrected hook-pair representative."""
    source_blocks, _ = hook_pair_corrected_semidirect_survivor_blocks(
        n,
        r,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )
    return tuple(
        semidirect_survivor_block_has_square_zero(block)
        for block in source_blocks
    )


def _mixed_blocks_match_under_relabeling(
    source_blocks: Tuple[MixedConstraintGhostBRSTBlock, ...],
    target_blocks: Tuple[MixedConstraintGhostBRSTBlock, ...],
    label_map: Dict[str, str],
    side_map: Dict[str, str],
) -> bool:
    """Check equality of mixed-block tuples after canonical relabeling."""
    if len(source_blocks) != len(target_blocks):
        return False
    for source_block, target_block in zip(source_blocks, target_blocks):
        effective_label_map = dict(label_map)
        if not effective_label_map:
            for label in (
                source_block.shifted_current_labels
                + source_block.c_ghost_labels
                + source_block.b_ghost_labels
            ):
                root = _label_root(label)
                effective_label_map[root] = root
        relabeled_source = relabel_mixed_constraint_ghost_block(
            source_block,
            effective_label_map,
            side_map=side_map,
            source_tag=target_block.source_tag,
        )
        if relabeled_source != target_block:
            return False
    return True


def _survivor_coupled_blocks_match_under_relabeling(
    source_blocks: Tuple[SurvivorCoupledBRSTBlock, ...],
    target_blocks: Tuple[SurvivorCoupledBRSTBlock, ...],
    label_map: Dict[str, str],
    side_map: Dict[str, str],
) -> bool:
    """Check equality of survivor-coupled block tuples after canonical relabeling."""
    if len(source_blocks) != len(target_blocks):
        return False
    for source_block, target_block in zip(source_blocks, target_blocks):
        effective_label_map = dict(label_map)
        if not effective_label_map:
            for label in (
                source_block.shifted_current_labels
                + source_block.c_ghost_labels
                + source_block.b_ghost_labels
            ):
                root = _label_root(label)
                effective_label_map[root] = root
        relabeled_source = _relabel_survivor_coupled_block(
            source_block,
            effective_label_map,
            side_map=side_map,
            source_tag=target_block.source_tag,
        )
        if relabeled_source != target_block:
            return False
    return True


def _semidirect_survivor_blocks_match_under_relabeling(
    source_blocks: Tuple[SemidirectSurvivorBRSTBlock, ...],
    target_blocks: Tuple[SemidirectSurvivorBRSTBlock, ...],
    label_map: Dict[str, str],
    side_map: Dict[str, str],
) -> bool:
    """Check semidirect survivor block equality after relabeling without rebuilding matrices."""
    if len(source_blocks) != len(target_blocks):
        return False
    for source_block, target_block in zip(source_blocks, target_blocks):
        effective_label_map = dict(label_map)
        if not effective_label_map:
            for label in (
                source_block.shifted_current_labels
                + source_block.c_ghost_labels
                + source_block.b_ghost_labels
            ):
                root = _label_root(label)
                effective_label_map[root] = root
        mapped_shifted_current_labels = tuple(
            _relabel_shifted_current_label(label, effective_label_map, side_map)
            for label in source_block.shifted_current_labels
        )
        mapped_survivor_labels = tuple(
            _relabel_survivor_label_with_side_map(label, side_map=side_map)
            for label in source_block.survivor_labels
        )
        mapped_c_ghost_labels = tuple(
            _relabel_ghost_label_with_side_map(label, effective_label_map, side_map)
            for label in source_block.c_ghost_labels
        )
        mapped_b_ghost_labels = tuple(
            _relabel_ghost_label_with_side_map(label, effective_label_map, side_map)
            for label in source_block.b_ghost_labels
        )
        mapped_internal_c_ghost_labels = tuple(
            _relabel_internal_survivor_ghost_label(label, side_map=side_map)
            for label in source_block.internal_c_ghost_labels
        )
        mapped_internal_b_ghost_labels = tuple(
            _relabel_internal_survivor_ghost_label(label, side_map=side_map)
            for label in source_block.internal_b_ghost_labels
        )
        if (
            mapped_shifted_current_labels != target_block.shifted_current_labels
            or mapped_survivor_labels != target_block.survivor_labels
            or mapped_c_ghost_labels != target_block.c_ghost_labels
            or mapped_b_ghost_labels != target_block.b_ghost_labels
            or mapped_internal_c_ghost_labels != target_block.internal_c_ghost_labels
            or mapped_internal_b_ghost_labels != target_block.internal_b_ghost_labels
            or source_block.chi_vector != target_block.chi_vector
            or relabel_quadratic_ghost_terms(
                source_block.quadratic_ghost_terms,
                effective_label_map,
                side_map=side_map,
            )
            != target_block.quadratic_ghost_terms
            or relabel_current_action_terms(
                source_block.current_action_terms,
                effective_label_map,
                side_map=side_map,
            )
            != target_block.current_action_terms
            or _relabel_survivor_action_terms(
                source_block.survivor_action_terms,
                effective_label_map,
                side_map=side_map,
            )
            != target_block.survivor_action_terms
            or _relabel_internal_quadratic_ghost_terms(
                source_block.internal_quadratic_ghost_terms,
                side_map=side_map,
            )
            != target_block.internal_quadratic_ghost_terms
            or _relabel_internal_survivor_action_terms(
                source_block.internal_survivor_action_terms,
                side_map=side_map,
            )
            != target_block.internal_survivor_action_terms
            or source_block.constraint_total_degree != target_block.constraint_total_degree
            or source_block.survivor_total_degree != target_block.survivor_total_degree
            or source_block.max_internal_ce_degree != target_block.max_internal_ce_degree
        ):
            return False
    return True


def nonprincipal_partition_pair_mixed_blocks_match_under_dual_swap(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check mixed blocks for one partition against the transpose-dual case."""
    case = nonprincipal_type_a_case(partition)
    default_source, default_target = _partition_pair_default_constraint_counts(case.partition)
    source_count = default_source if source_num_constraints is None else source_num_constraints
    target_count = default_target if target_num_constraints is None else target_num_constraints
    source_blocks, target_blocks = nonprincipal_partition_pair_mixed_constraint_ghost_blocks(
        case.partition,
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )
    dual_source_blocks, dual_target_blocks = nonprincipal_partition_pair_mixed_constraint_ghost_blocks(
        case.dual_partition,
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=target_count,
        target_num_constraints=source_count,
    )
    return _mixed_blocks_match_under_relabeling(
        source_blocks,
        dual_target_blocks,
        label_map={},
        side_map={"source": "target"},
    ) and _mixed_blocks_match_under_relabeling(
        target_blocks,
        dual_source_blocks,
        label_map={},
        side_map={"target": "source"},
    )


def nonprincipal_partition_pair_nonlinear_blocks_match_under_dual_swap(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check nonlinear mixed blocks for one partition against the dual case."""
    case = nonprincipal_type_a_case(partition)
    default_source, default_target = _partition_pair_default_constraint_counts(case.partition)
    source_count = default_source if source_num_constraints is None else source_num_constraints
    target_count = default_target if target_num_constraints is None else target_num_constraints
    source_blocks, target_blocks = nonprincipal_partition_pair_nonlinear_mixed_constraint_ghost_blocks(
        case.partition,
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )
    dual_source_blocks, dual_target_blocks = (
        nonprincipal_partition_pair_nonlinear_mixed_constraint_ghost_blocks(
            case.dual_partition,
            max_constraint_total_degree=max_constraint_total_degree,
            source_num_constraints=target_count,
            target_num_constraints=source_count,
        )
    )
    return _mixed_blocks_match_under_relabeling(
        source_blocks,
        dual_target_blocks,
        label_map={},
        side_map={"source": "target"},
    ) and _mixed_blocks_match_under_relabeling(
        target_blocks,
        dual_source_blocks,
        label_map={},
        side_map={"target": "source"},
    )


@lru_cache(maxsize=64)
def nonprincipal_partition_pair_survivor_coupled_blocks_match_under_dual_swap(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check survivor-coupled blocks for one partition against the dual case."""
    case = nonprincipal_type_a_case(partition)
    default_source, default_target = _partition_pair_default_constraint_counts(case.partition)
    source_count = default_source if source_num_constraints is None else source_num_constraints
    target_count = default_target if target_num_constraints is None else target_num_constraints
    source_blocks, target_blocks = nonprincipal_partition_pair_survivor_coupled_blocks(
        case.partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )
    dual_source_blocks, dual_target_blocks = nonprincipal_partition_pair_survivor_coupled_blocks(
        case.dual_partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=target_count,
        target_num_constraints=source_count,
    )
    return _survivor_coupled_blocks_match_under_relabeling(
        source_blocks,
        dual_target_blocks,
        label_map={},
        side_map={"source": "target"},
    ) and _survivor_coupled_blocks_match_under_relabeling(
        target_blocks,
        dual_source_blocks,
        label_map={},
        side_map={"target": "source"},
    )


@lru_cache(maxsize=64)
def nonprincipal_partition_pair_corrected_semidirect_blocks_match_under_dual_swap(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check corrected semidirect blocks for one partition against the dual case."""
    case = nonprincipal_type_a_case(partition)
    default_source, default_target = _partition_pair_default_constraint_counts(case.partition)
    source_count = default_source if source_num_constraints is None else source_num_constraints
    target_count = default_target if target_num_constraints is None else target_num_constraints
    source_blocks, target_blocks = nonprincipal_partition_pair_corrected_semidirect_survivor_blocks(
        case.partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )
    dual_source_blocks, dual_target_blocks = (
        nonprincipal_partition_pair_corrected_semidirect_survivor_blocks(
            case.dual_partition,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
            source_num_constraints=target_count,
            target_num_constraints=source_count,
        )
    )
    return _semidirect_survivor_blocks_match_under_relabeling(
        source_blocks,
        dual_target_blocks,
        label_map={},
        side_map={"source": "target"},
    ) and _semidirect_survivor_blocks_match_under_relabeling(
        target_blocks,
        dual_source_blocks,
        label_map={},
        side_map={"target": "source"},
    )


def nonprincipal_two_row_mixed_blocks_match_under_dual_swap(
    n: int,
    s: int,
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check mixed two-row non-hook blocks against their transpose-dual case."""
    return nonprincipal_partition_pair_mixed_blocks_match_under_dual_swap(
        two_row_nonhook_partition(n, s),
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )


def nonprincipal_two_row_nonlinear_blocks_match_under_dual_swap(
    n: int,
    s: int,
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check nonlinear two-row non-hook blocks against their transpose-dual case."""
    return nonprincipal_partition_pair_nonlinear_blocks_match_under_dual_swap(
        two_row_nonhook_partition(n, s),
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )


def nonprincipal_two_row_survivor_coupled_blocks_match_under_dual_swap(
    n: int,
    s: int,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check survivor-coupled two-row non-hook blocks against transpose duality."""
    return nonprincipal_partition_pair_survivor_coupled_blocks_match_under_dual_swap(
        two_row_nonhook_partition(n, s),
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )


def nonprincipal_two_row_corrected_semidirect_blocks_match_under_dual_swap(
    n: int,
    s: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check corrected semidirect two-row non-hook blocks against transpose duality."""
    return nonprincipal_partition_pair_corrected_semidirect_blocks_match_under_dual_swap(
        two_row_nonhook_partition(n, s),
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_num_constraints,
        target_num_constraints=target_num_constraints,
    )


def hook_pair_mixed_blocks_match_under_dual_swap(
    n: int,
    r: int,
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check mixed blocks for (n,r) against the transpose-dual case under side swap."""
    default_source, default_target = hook_pair_constraint_counts_ansatz_type_a(n, r)
    source_count = default_source if source_num_constraints is None else source_num_constraints
    target_count = default_target if target_num_constraints is None else target_num_constraints
    dual_r = n - r - 1
    source_blocks, target_blocks = hook_pair_mixed_constraint_ghost_blocks(
        n,
        r,
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )
    dual_source_blocks, dual_target_blocks = hook_pair_mixed_constraint_ghost_blocks(
        n,
        dual_r,
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=target_count,
        target_num_constraints=source_count,
    )
    return _mixed_blocks_match_under_relabeling(
        source_blocks,
        dual_target_blocks,
        label_map={},
        side_map={"source": "target"},
    ) and _mixed_blocks_match_under_relabeling(
        target_blocks,
        dual_source_blocks,
        label_map={},
        side_map={"target": "source"},
    )


def hook_pair_nonlinear_blocks_match_under_dual_swap(
    n: int,
    r: int,
    max_constraint_total_degree: int = 2,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check nonlinear mixed blocks for (n,r) against the transpose-dual case."""
    default_source, default_target = hook_pair_constraint_counts_ansatz_type_a(n, r)
    source_count = default_source if source_num_constraints is None else source_num_constraints
    target_count = default_target if target_num_constraints is None else target_num_constraints
    dual_r = n - r - 1
    source_blocks, target_blocks = hook_pair_nonlinear_mixed_constraint_ghost_blocks(
        n,
        r,
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )
    dual_source_blocks, dual_target_blocks = hook_pair_nonlinear_mixed_constraint_ghost_blocks(
        n,
        dual_r,
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=target_count,
        target_num_constraints=source_count,
    )
    return _mixed_blocks_match_under_relabeling(
        source_blocks,
        dual_target_blocks,
        label_map={},
        side_map={"source": "target"},
    ) and _mixed_blocks_match_under_relabeling(
        target_blocks,
        dual_source_blocks,
        label_map={},
        side_map={"target": "source"},
    )


def hook_pair_survivor_coupled_blocks_match_under_dual_swap(
    n: int,
    r: int,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check survivor-coupled blocks for (n,r) against the transpose-dual case."""
    default_source, default_target = hook_pair_constraint_counts_ansatz_type_a(n, r)
    source_count = default_source if source_num_constraints is None else source_num_constraints
    target_count = default_target if target_num_constraints is None else target_num_constraints
    dual_r = n - r - 1
    source_blocks, target_blocks = hook_pair_survivor_coupled_blocks(
        n,
        r,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )
    dual_source_blocks, dual_target_blocks = hook_pair_survivor_coupled_blocks(
        n,
        dual_r,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=target_count,
        target_num_constraints=source_count,
    )
    return _survivor_coupled_blocks_match_under_relabeling(
        source_blocks,
        dual_target_blocks,
        label_map={},
        side_map={"source": "target"},
    ) and _survivor_coupled_blocks_match_under_relabeling(
        target_blocks,
        dual_source_blocks,
        label_map={},
        side_map={"target": "source"},
    )


def hook_pair_corrected_semidirect_blocks_match_under_dual_swap(
    n: int,
    r: int,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
    source_num_constraints: int | None = None,
    target_num_constraints: int | None = None,
) -> bool:
    """Check corrected semidirect hook blocks for (n,r) against the transpose-dual case."""
    default_source, default_target = hook_pair_constraint_counts_ansatz_type_a(n, r)
    source_count = default_source if source_num_constraints is None else source_num_constraints
    target_count = default_target if target_num_constraints is None else target_num_constraints
    dual_r = n - r - 1
    source_blocks, target_blocks = hook_pair_corrected_semidirect_survivor_blocks(
        n,
        r,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )
    dual_source_blocks, dual_target_blocks = hook_pair_corrected_semidirect_survivor_blocks(
        n,
        dual_r,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=target_count,
        target_num_constraints=source_count,
    )
    return _semidirect_survivor_blocks_match_under_relabeling(
        source_blocks,
        dual_target_blocks,
        label_map={},
        side_map={"source": "target"},
    ) and _semidirect_survivor_blocks_match_under_relabeling(
        target_blocks,
        dual_source_blocks,
        label_map={},
        side_map={"target": "source"},
    )


def verify_hook_pair_mixed_block_duality_catalog(
    max_n: int = 7,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of mixed hook-pair BRST blocks."""
    results: Dict[str, bool] = {}
    if max_n < 3:
        return results
    for n in range(3, max_n + 1):
        for r in range(1, n - 1):
            key = f"A{n-1} hook r={r}"
            results[f"{key} mixed dual-swap symmetry"] = hook_pair_mixed_blocks_match_under_dual_swap(
                n,
                r,
                max_constraint_total_degree=max_constraint_total_degree,
            )
    return results


@lru_cache(maxsize=64)
def _hook_family_representative_rs(n: int) -> Tuple[int, ...]:
    """Canonical hook representatives for one rank, reduced by transpose duality."""
    if n < 3:
        return ()
    return tuple(r for r in range(1, n - 1) if r <= n - r - 1)


@lru_cache(maxsize=128)
def hook_pair_survivor_coupled_representative_holds_via_duality(
    n: int,
    r: int,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> bool:
    """Check one hook representative by survivor invariants plus transpose duality."""
    dual_r = n - r - 1
    source_blocks, target_blocks = hook_pair_survivor_coupled_blocks(
        n,
        r,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
    )
    if not _all_blocks_have_square_zero_and_are_acyclic(
        source_blocks + target_blocks,
        survivor_coupled_block_invariant_summary,
    ):
        return False
    if r < dual_r and not hook_pair_survivor_coupled_blocks_match_under_dual_swap(
        n,
        r,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
    ):
        return False
    return True


@lru_cache(maxsize=64)
def hook_pair_mixed_family_holds_via_duality(
    n: int,
    max_constraint_total_degree: int = 1,
) -> bool:
    """Check one hook mixed family using direct half-catalog acyclicity plus transpose duality."""
    if n < 3:
        return True
    for r in _hook_family_representative_rs(n):
        dual_r = n - r - 1
        source_blocks, target_blocks = hook_pair_mixed_constraint_ghost_blocks(
            n,
            r,
            max_constraint_total_degree=max_constraint_total_degree,
        )
        if not _all_blocks_have_square_zero_and_are_acyclic(
            source_blocks + target_blocks,
            mixed_constraint_ghost_block_invariant_summary,
        ):
            return False
        if r < dual_r and not hook_pair_mixed_blocks_match_under_dual_swap(
            n,
            r,
            max_constraint_total_degree=max_constraint_total_degree,
        ):
            return False
    return True


def verify_hook_pair_mixed_family_via_duality_catalog(
    max_n: int = 7,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks that recover each hook mixed family from a half-catalog plus duality."""
    return dict(
        _hook_pair_mixed_family_via_duality_catalog_items(
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
        )
    )


@lru_cache(maxsize=64)
def _hook_pair_mixed_family_via_duality_catalog_items(
    max_n: int = 7,
    max_constraint_total_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for hook mixed family-via-duality catalog checks."""
    if max_n < 3:
        return (("hook mixed family-via-duality catalog is empty below rank three", True),)
    return tuple(
        (
            f"A{n-1} hook family mixed acyclicity follows by duality",
            hook_pair_mixed_family_holds_via_duality(
                n,
                max_constraint_total_degree=max_constraint_total_degree,
            ),
        )
        for n in range(3, max_n + 1)
    )


def verify_hook_pair_nonlinear_block_duality_catalog(
    max_n: int = 7,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of nonlinear mixed hook-pair blocks."""
    results: Dict[str, bool] = {}
    if max_n < 3:
        return results
    for n in range(3, max_n + 1):
        for r in range(1, n - 1):
            key = f"A{n-1} hook r={r}"
            results[f"{key} nonlinear dual-swap symmetry"] = (
                hook_pair_nonlinear_blocks_match_under_dual_swap(
                    n,
                    r,
                    max_constraint_total_degree=max_constraint_total_degree,
            )
        )
    return results


@lru_cache(maxsize=64)
def hook_pair_nonlinear_family_holds_via_duality(
    n: int,
    max_constraint_total_degree: int = 1,
) -> bool:
    """Check one hook nonlinear family using direct half-catalog acyclicity plus transpose duality."""
    if n < 3:
        return True
    for r in _hook_family_representative_rs(n):
        dual_r = n - r - 1
        source_blocks, target_blocks = hook_pair_nonlinear_mixed_constraint_ghost_blocks(
            n,
            r,
            max_constraint_total_degree=max_constraint_total_degree,
        )
        if not _all_blocks_have_square_zero_and_are_acyclic(
            source_blocks + target_blocks,
            mixed_constraint_ghost_block_invariant_summary,
        ):
            return False
        if r < dual_r and not hook_pair_nonlinear_blocks_match_under_dual_swap(
            n,
            r,
            max_constraint_total_degree=max_constraint_total_degree,
        ):
            return False
    return True


def verify_hook_pair_nonlinear_family_via_duality_catalog(
    max_n: int = 7,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks that recover each hook nonlinear family from a half-catalog plus duality."""
    return dict(
        _hook_pair_nonlinear_family_via_duality_catalog_items(
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
        )
    )


@lru_cache(maxsize=64)
def _hook_pair_nonlinear_family_via_duality_catalog_items(
    max_n: int = 7,
    max_constraint_total_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for hook nonlinear family-via-duality catalog checks."""
    if max_n < 3:
        return (("hook nonlinear family-via-duality catalog is empty below rank three", True),)
    return tuple(
        (
            f"A{n-1} hook family nonlinear acyclicity follows by duality",
            hook_pair_nonlinear_family_holds_via_duality(
                n,
                max_constraint_total_degree=max_constraint_total_degree,
            ),
        )
        for n in range(3, max_n + 1)
    )


def verify_hook_pair_survivor_coupled_block_duality_catalog(
    max_n: int = 5,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of survivor-coupled hook-pair blocks."""
    results: Dict[str, bool] = {}
    if max_n < 3:
        return results
    for n in range(3, max_n + 1):
        for r in range(1, n - 1):
            key = f"A{n-1} hook r={r}"
            results[f"{key} survivor-coupled dual-swap symmetry"] = (
                hook_pair_survivor_coupled_blocks_match_under_dual_swap(
                    n,
                    r,
                    max_constraint_total_degree=max_constraint_total_degree,
                    survivor_total_degree=survivor_total_degree,
                )
            )
    return results


@lru_cache(maxsize=64)
def hook_pair_survivor_coupled_family_holds_via_duality(
    n: int,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> bool:
    """Check one hook family by direct half-catalog acyclicity plus transpose duality."""
    if n < 3:
        return True
    for r in _hook_family_representative_rs(n):
        if not hook_pair_survivor_coupled_representative_holds_via_duality(
            n,
            r,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
        ):
            return False
    return True


def verify_hook_pair_survivor_coupled_family_via_duality_catalog(
    max_n: int = 6,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks recovering hook survivor families from half-catalog data."""
    return dict(
        _hook_pair_survivor_coupled_family_via_duality_catalog_items(
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
        )
    )


@lru_cache(maxsize=64)
def _hook_pair_survivor_coupled_family_via_duality_catalog_items(
    max_n: int = 6,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for hook survivor family-via-duality catalog checks."""
    if max_n < 3:
        return (("hook survivor-coupled family-via-duality catalog is empty below rank three", True),)
    return tuple(
        (
            f"A{n-1} hook family survivor-coupled checks follow by duality",
            hook_pair_survivor_coupled_family_holds_via_duality(
                n,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
            ),
        )
        for n in range(3, max_n + 1)
    )


def verify_nonprincipal_two_row_mixed_block_duality_catalog(
    max_n: int = 8,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of mixed non-hook two-row blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_two_row_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} two-row {case.partition}"
        results[f"{key} mixed dual-swap symmetry"] = (
            nonprincipal_partition_pair_mixed_blocks_match_under_dual_swap(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
            )
        )
    return results


@lru_cache(maxsize=64)
def _nonprincipal_two_row_family_representative_items(
    max_n: int = 9,
) -> Tuple[Tuple[Tuple[int, ...], str], ...]:
    """Cached canonical two-row family representatives with stable catalog labels."""
    results: list[Tuple[Tuple[int, ...], str]] = []
    seen_pairs: set[Tuple[Tuple[int, ...], Tuple[int, ...]]] = set()
    for case in nonprincipal_two_row_cases(max_n=max_n):
        canonical_pair = tuple(sorted((case.partition, case.dual_partition)))
        if canonical_pair in seen_pairs:
            continue
        seen_pairs.add(canonical_pair)
        n = partition_size(case.partition)
        if case.partition == case.dual_partition:
            key = f"A{n-1} two-row {case.partition}"
        else:
            key = f"A{n-1} two-row {canonical_pair[0]}<->{canonical_pair[1]}"
        results.append((case.partition, key))
    return tuple(results)


@lru_cache(maxsize=64)
def nonprincipal_two_row_mixed_family_holds_via_duality(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> bool:
    """Recover two-row mixed checks from one representative in each transpose pair."""
    for partition, _ in _nonprincipal_two_row_family_representative_items(max_n=max_n):
        if not _nonprincipal_partition_pair_mixed_holds_via_duality(
            partition,
            max_constraint_total_degree=max_constraint_total_degree,
        ):
            return False
    return True


def verify_nonprincipal_two_row_mixed_family_via_duality_catalog(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Seeded two-row mixed checks reduced by transpose duality."""
    return dict(
        _nonprincipal_two_row_mixed_family_via_duality_catalog_items(
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
        )
    )


@lru_cache(maxsize=64)
def _nonprincipal_two_row_mixed_family_via_duality_catalog_items(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for two-row mixed family-via-duality checks."""
    return tuple(
        (
            f"{key} mixed checks follow by duality",
            _nonprincipal_partition_pair_mixed_holds_via_duality(
                partition,
                max_constraint_total_degree=max_constraint_total_degree,
            ),
        )
        for partition, key in _nonprincipal_two_row_family_representative_items(max_n=max_n)
    )


def verify_nonprincipal_two_row_nonlinear_block_duality_catalog(
    max_n: int = 8,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of nonlinear non-hook two-row blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_two_row_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} two-row {case.partition}"
        results[f"{key} nonlinear dual-swap symmetry"] = (
            nonprincipal_partition_pair_nonlinear_blocks_match_under_dual_swap(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
            )
        )
    return results


@lru_cache(maxsize=64)
def nonprincipal_two_row_nonlinear_family_holds_via_duality(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> bool:
    """Recover two-row nonlinear checks from one representative in each transpose pair."""
    for partition, _ in _nonprincipal_two_row_family_representative_items(max_n=max_n):
        if not _nonprincipal_partition_pair_nonlinear_holds_via_duality(
            partition,
            max_constraint_total_degree=max_constraint_total_degree,
        ):
            return False
    return True


def verify_nonprincipal_two_row_nonlinear_family_via_duality_catalog(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Seeded two-row nonlinear checks reduced by transpose duality."""
    return dict(
        _nonprincipal_two_row_nonlinear_family_via_duality_catalog_items(
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
        )
    )


@lru_cache(maxsize=64)
def _nonprincipal_two_row_nonlinear_family_via_duality_catalog_items(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for two-row nonlinear family-via-duality checks."""
    return tuple(
        (
            f"{key} nonlinear checks follow by duality",
            _nonprincipal_partition_pair_nonlinear_holds_via_duality(
                partition,
                max_constraint_total_degree=max_constraint_total_degree,
            ),
        )
        for partition, key in _nonprincipal_two_row_family_representative_items(max_n=max_n)
    )


def verify_nonprincipal_two_row_survivor_coupled_block_duality_catalog(
    max_n: int = 8,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of survivor-coupled two-row blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_two_row_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} two-row {case.partition}"
        results[f"{key} survivor-coupled dual-swap symmetry"] = (
            nonprincipal_partition_pair_survivor_coupled_blocks_match_under_dual_swap(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
            )
        )
    return results


def verify_nonprincipal_two_row_survivor_coupled_bundle(
    max_n: int = 8,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Dict[str, bool]:
    """One-pass square-zero and dual-swap checks for survivor-coupled two-row blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_two_row_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} two-row {case.partition}"
        default_source, default_target = _partition_pair_default_constraint_counts(case.partition)
        source_blocks, target_blocks = nonprincipal_partition_pair_survivor_coupled_blocks(
            case.partition,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            source_num_constraints=default_source,
            target_num_constraints=default_target,
        )
        dual_source_blocks, dual_target_blocks = nonprincipal_partition_pair_survivor_coupled_blocks(
            case.dual_partition,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            source_num_constraints=default_target,
            target_num_constraints=default_source,
        )
        results[f"{key} survivor-coupled blocks square to zero"] = all(
            survivor_coupled_block_has_square_zero(block)
            for block in source_blocks + target_blocks
        )
        results[f"{key} survivor-coupled dual-swap symmetry"] = (
            _survivor_coupled_blocks_match_under_relabeling(
                source_blocks,
                dual_target_blocks,
                label_map={},
                side_map={"source": "target"},
            )
            and _survivor_coupled_blocks_match_under_relabeling(
                target_blocks,
                dual_source_blocks,
                label_map={},
                side_map={"target": "source"},
            )
        )
    return results


@lru_cache(maxsize=64)
def nonprincipal_two_row_survivor_coupled_family_holds_via_duality(
    max_n: int = 8,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> bool:
    """Recover two-row survivor checks from one representative in each transpose pair."""
    for partition, _ in _nonprincipal_two_row_family_representative_items(max_n=max_n):
        if not _nonprincipal_partition_pair_survivor_coupled_holds_via_duality(
            partition,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
        ):
            return False
    return True


def verify_nonprincipal_two_row_survivor_coupled_family_via_duality_catalog(
    max_n: int = 8,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Dict[str, bool]:
    """Seeded two-row survivor checks reduced by transpose duality."""
    return dict(
        _nonprincipal_two_row_survivor_coupled_family_via_duality_catalog_items(
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
        )
    )


@lru_cache(maxsize=64)
def _nonprincipal_two_row_survivor_coupled_family_via_duality_catalog_items(
    max_n: int = 8,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for two-row survivor family-via-duality checks."""
    return tuple(
        (
            f"{key} survivor-coupled checks follow by duality",
            _nonprincipal_partition_pair_survivor_coupled_holds_via_duality(
                partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
            ),
        )
        for partition, key in _nonprincipal_two_row_family_representative_items(max_n=max_n)
    )


@lru_cache(maxsize=64)
def _nonprincipal_partition_pair_survivor_coupled_holds_via_duality(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> bool:
    """Check one non-principal partition pair by square-zero plus transpose duality."""
    case = nonprincipal_type_a_case(partition)
    default_source, default_target = _partition_pair_default_constraint_counts(case.partition)
    if not all(
        _partition_pair_survivor_coupled_source_square_zero_flags(
            case.partition,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            source_num_constraints=default_source,
            target_num_constraints=default_target,
        )
    ):
        return False
    return nonprincipal_partition_pair_survivor_coupled_blocks_match_under_dual_swap(
        case.partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=default_source,
        target_num_constraints=default_target,
    )


@lru_cache(maxsize=64)
def nonprincipal_partition_pair_survivor_coupled_representative_holds_via_duality(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> bool:
    """Public representative check for one non-principal survivor-coupled partition pair."""
    return _nonprincipal_partition_pair_survivor_coupled_holds_via_duality(
        partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
    )


@lru_cache(maxsize=64)
def general_nonprincipal_survivor_coupled_family_holds_via_duality(
    min_n: int = 5,
    max_n: int = 11,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> bool:
    """Recover seeded general survivor-coupled checks from square-zero plus transpose symmetry."""
    for partition, _ in _nonprincipal_general_family_representative_items_in_range(
        min_n=min_n,
        max_n=max_n,
    ):
        if not _nonprincipal_partition_pair_survivor_coupled_holds_via_duality(
            partition,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
        ):
            return False
    return True


def verify_nonprincipal_general_survivor_coupled_family_via_duality_catalog(
    min_n: int = 5,
    max_n: int = 11,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Dict[str, bool]:
    """Seeded general survivor-coupled checks reduced by transpose duality."""
    return dict(
        _nonprincipal_general_survivor_coupled_family_via_duality_catalog_items(
            min_n=min_n,
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
        )
    )


@lru_cache(maxsize=64)
def _nonprincipal_general_survivor_coupled_family_via_duality_catalog_items(
    min_n: int = 5,
    max_n: int = 11,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for general survivor family-via-duality checks."""
    return tuple(
        (
            f"{key} survivor-coupled checks follow by duality",
            _nonprincipal_partition_pair_survivor_coupled_holds_via_duality(
                partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
            ),
        )
        for partition, key in _nonprincipal_general_family_representative_items_in_range(
            min_n=min_n,
            max_n=max_n,
        )
    )


def verify_nonprincipal_general_mixed_block_duality_catalog(
    max_n: int = 7,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of general non-principal mixed blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_general_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} general {case.partition}"
        results[f"{key} mixed dual-swap symmetry"] = (
            nonprincipal_partition_pair_mixed_blocks_match_under_dual_swap(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
            )
        )
    return results


@lru_cache(maxsize=64)
def _nonprincipal_general_family_representative_items(
    max_n: int = 9,
) -> Tuple[Tuple[Tuple[int, ...], str], ...]:
    """Cached canonical general-family representatives with stable catalog labels."""
    results: list[Tuple[Tuple[int, ...], str]] = []
    seen_pairs: set[Tuple[Tuple[int, ...], Tuple[int, ...]]] = set()
    for case in nonprincipal_general_cases(max_n=max_n):
        canonical_pair = tuple(sorted((case.partition, case.dual_partition)))
        if canonical_pair in seen_pairs:
            continue
        seen_pairs.add(canonical_pair)
        n = partition_size(case.partition)
        if case.partition == case.dual_partition:
            key = f"A{n-1} general {case.partition}"
        else:
            key = f"A{n-1} general {canonical_pair[0]}<->{canonical_pair[1]}"
        results.append((case.partition, key))
    return tuple(results)


@lru_cache(maxsize=64)
def _nonprincipal_general_family_representative_items_in_range(
    min_n: int = 5,
    max_n: int = 11,
) -> Tuple[Tuple[Tuple[int, ...], str], ...]:
    """Cached general-family representatives filtered to an inclusive rank window."""
    return tuple(
        (partition, key)
        for partition, key in _nonprincipal_general_family_representative_items(max_n=max_n)
        if min_n <= partition_size(partition) <= max_n
    )


@lru_cache(maxsize=64)
def _nonprincipal_partition_pair_mixed_holds_via_duality(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 1,
) -> bool:
    """Check one seeded general mixed block representative against its transpose dual."""
    return nonprincipal_partition_pair_mixed_blocks_match_under_dual_swap(
        partition,
        max_constraint_total_degree=max_constraint_total_degree,
    )


@lru_cache(maxsize=64)
def general_nonprincipal_mixed_family_holds_via_duality(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> bool:
    """Recover seeded general mixed checks from one representative in each transpose pair."""
    for partition, _ in _nonprincipal_general_family_representative_items(max_n=max_n):
        if not _nonprincipal_partition_pair_mixed_holds_via_duality(
            partition,
            max_constraint_total_degree=max_constraint_total_degree,
        ):
            return False
    return True


def verify_nonprincipal_general_mixed_family_via_duality_catalog(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Seeded general mixed checks reduced by transpose symmetry."""
    return dict(
        _nonprincipal_general_mixed_family_via_duality_catalog_items(
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
        )
    )


@lru_cache(maxsize=64)
def _nonprincipal_general_mixed_family_via_duality_catalog_items(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for general mixed family-via-duality checks."""
    return tuple(
        (
            f"{key} mixed checks follow by duality",
            _nonprincipal_partition_pair_mixed_holds_via_duality(
                partition,
                max_constraint_total_degree=max_constraint_total_degree,
            ),
        )
        for partition, key in _nonprincipal_general_family_representative_items(max_n=max_n)
    )


def verify_nonprincipal_general_nonlinear_block_duality_catalog(
    max_n: int = 7,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of general non-principal nonlinear blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_general_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} general {case.partition}"
        results[f"{key} nonlinear dual-swap symmetry"] = (
            nonprincipal_partition_pair_nonlinear_blocks_match_under_dual_swap(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
            )
        )
    return results


@lru_cache(maxsize=64)
def _nonprincipal_partition_pair_nonlinear_holds_via_duality(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 1,
) -> bool:
    """Check one seeded general nonlinear block representative against its transpose dual."""
    return nonprincipal_partition_pair_nonlinear_blocks_match_under_dual_swap(
        partition,
        max_constraint_total_degree=max_constraint_total_degree,
    )


@lru_cache(maxsize=64)
def general_nonprincipal_nonlinear_family_holds_via_duality(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> bool:
    """Recover seeded general nonlinear checks from one representative in each transpose pair."""
    for partition, _ in _nonprincipal_general_family_representative_items(max_n=max_n):
        if not _nonprincipal_partition_pair_nonlinear_holds_via_duality(
            partition,
            max_constraint_total_degree=max_constraint_total_degree,
        ):
            return False
    return True


def verify_nonprincipal_general_nonlinear_family_via_duality_catalog(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> Dict[str, bool]:
    """Seeded general nonlinear checks reduced by transpose symmetry."""
    return dict(
        _nonprincipal_general_nonlinear_family_via_duality_catalog_items(
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
        )
    )


@lru_cache(maxsize=64)
def _nonprincipal_general_nonlinear_family_via_duality_catalog_items(
    max_n: int = 9,
    max_constraint_total_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for general nonlinear family-via-duality checks."""
    return tuple(
        (
            f"{key} nonlinear checks follow by duality",
            _nonprincipal_partition_pair_nonlinear_holds_via_duality(
                partition,
                max_constraint_total_degree=max_constraint_total_degree,
            ),
        )
        for partition, key in _nonprincipal_general_family_representative_items(max_n=max_n)
    )


def verify_nonprincipal_general_survivor_coupled_block_duality_catalog(
    max_n: int = 7,
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of general non-principal survivor blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_general_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} general {case.partition}"
        results[f"{key} survivor-coupled dual-swap symmetry"] = (
            nonprincipal_partition_pair_survivor_coupled_blocks_match_under_dual_swap(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
            )
        )
    return results


def verify_nonprincipal_two_row_corrected_semidirect_catalog(
    max_n: int = 6,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for square-zero corrected semidirect two-row blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_two_row_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} two-row {case.partition}"
        results[f"{key} corrected semidirect blocks square to zero"] = all(
            _partition_pair_corrected_semidirect_square_zero_flags(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
            )
        )
    return results


def verify_nonprincipal_two_row_corrected_semidirect_duality_catalog(
    max_n: int = 6,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of corrected semidirect two-row blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_two_row_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} two-row {case.partition}"
        results[f"{key} corrected semidirect dual-swap symmetry"] = (
            nonprincipal_partition_pair_corrected_semidirect_blocks_match_under_dual_swap(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
            )
        )
    return results


def verify_nonprincipal_two_row_corrected_semidirect_bundle(
    max_n: int = 7,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Dict[str, bool]:
    """One-pass square-zero and dual-swap checks for corrected semidirect two-row blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_two_row_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} two-row {case.partition}"
        default_source, default_target = _partition_pair_default_constraint_counts(case.partition)
        source_blocks, target_blocks = nonprincipal_partition_pair_corrected_semidirect_survivor_blocks(
            case.partition,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
            source_num_constraints=default_source,
            target_num_constraints=default_target,
        )
        dual_source_blocks, dual_target_blocks = (
            nonprincipal_partition_pair_corrected_semidirect_survivor_blocks(
                case.dual_partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
                source_num_constraints=default_target,
                target_num_constraints=default_source,
            )
        )
        results[f"{key} corrected semidirect blocks square to zero"] = all(
            _partition_pair_corrected_semidirect_square_zero_flags(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
                source_num_constraints=default_source,
                target_num_constraints=default_target,
            )
        )
        results[f"{key} corrected semidirect dual-swap symmetry"] = (
            _semidirect_survivor_blocks_match_under_relabeling(
                source_blocks,
                dual_target_blocks,
                label_map={},
                side_map={"source": "target"},
            )
            and _semidirect_survivor_blocks_match_under_relabeling(
                target_blocks,
                dual_source_blocks,
                label_map={},
                side_map={"target": "source"},
            )
        )
    return results


@lru_cache(maxsize=64)
def nonprincipal_two_row_corrected_semidirect_family_holds_via_duality(
    max_n: int = 8,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> bool:
    """Recover two-row corrected checks from one representative in each transpose pair."""
    for partition, _ in _nonprincipal_two_row_family_representative_items(max_n=max_n):
        if not _nonprincipal_partition_pair_corrected_semidirect_holds_via_duality(
            partition,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
        ):
            return False
    return True


def verify_nonprincipal_two_row_corrected_semidirect_family_via_duality_catalog(
    max_n: int = 8,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Dict[str, bool]:
    """Seeded two-row corrected checks reduced by transpose duality."""
    return dict(
        _nonprincipal_two_row_corrected_semidirect_family_via_duality_catalog_items(
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
        )
    )


@lru_cache(maxsize=64)
def _nonprincipal_two_row_corrected_semidirect_family_via_duality_catalog_items(
    max_n: int = 8,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for two-row corrected family-via-duality checks."""
    return tuple(
        (
            f"{key} corrected semidirect checks follow by duality",
            _nonprincipal_partition_pair_corrected_semidirect_holds_via_duality(
                partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
            ),
        )
        for partition, key in _nonprincipal_two_row_family_representative_items(max_n=max_n)
    )


def verify_nonprincipal_general_corrected_semidirect_catalog(
    max_n: int = 5,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for square-zero corrected semidirect general non-principal blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_general_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} general {case.partition}"
        results[f"{key} corrected semidirect blocks square to zero"] = all(
            _partition_pair_corrected_semidirect_square_zero_flags(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
            )
        )
    return results


def verify_nonprincipal_general_corrected_semidirect_duality_catalog(
    max_n: int = 5,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Dict[str, bool]:
    """Catalog checks for dual-swap symmetry of corrected semidirect general blocks."""
    results: Dict[str, bool] = {}
    for case in nonprincipal_general_cases(max_n=max_n):
        n = partition_size(case.partition)
        key = f"A{n-1} general {case.partition}"
        results[f"{key} corrected semidirect dual-swap symmetry"] = (
            nonprincipal_partition_pair_corrected_semidirect_blocks_match_under_dual_swap(
                case.partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
            )
        )
    return results


@lru_cache(maxsize=64)
def _nonprincipal_partition_pair_corrected_semidirect_holds_via_duality(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> bool:
    """Check one partition pair by direct square-zero on one side plus transpose duality."""
    case = nonprincipal_type_a_case(partition)
    default_source, default_target = _partition_pair_default_constraint_counts(case.partition)
    if not all(
        _partition_pair_corrected_semidirect_source_square_zero_flags(
            case.partition,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
            source_num_constraints=default_source,
            target_num_constraints=default_target,
        )
    ):
        return False
    return nonprincipal_partition_pair_corrected_semidirect_blocks_match_under_dual_swap(
        case.partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=default_source,
        target_num_constraints=default_target,
    )


@lru_cache(maxsize=64)
def nonprincipal_partition_pair_corrected_semidirect_representative_holds_via_duality(
    partition: Tuple[int, ...],
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> bool:
    """Public representative check for one corrected non-principal partition pair."""
    return _nonprincipal_partition_pair_corrected_semidirect_holds_via_duality(
        partition,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
    )


@lru_cache(maxsize=64)
def general_nonprincipal_corrected_semidirect_family_holds_via_duality(
    min_n: int = 5,
    max_n: int = 14,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> bool:
    """Recover seeded general non-principal corrected semidirect checks from square-zero plus transpose duality."""
    for partition, _ in _nonprincipal_general_family_representative_items_in_range(
        min_n=min_n,
        max_n=max_n,
    ):
        if not _nonprincipal_partition_pair_corrected_semidirect_holds_via_duality(
            partition,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
        ):
            return False
    return True


def verify_nonprincipal_general_corrected_semidirect_family_via_duality_catalog(
    min_n: int = 5,
    max_n: int = 14,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Dict[str, bool]:
    """Seeded general-family corrected semidirect checks reduced by transpose duality."""
    return dict(
        _nonprincipal_general_corrected_semidirect_family_via_duality_catalog_items(
            min_n=min_n,
            max_n=max_n,
            max_constraint_total_degree=max_constraint_total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
        )
    )


@lru_cache(maxsize=64)
def _nonprincipal_general_corrected_semidirect_family_via_duality_catalog_items(
    min_n: int = 5,
    max_n: int = 14,
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for general corrected family-via-duality checks."""
    return tuple(
        (
            f"{key} corrected semidirect checks follow by duality",
            _nonprincipal_partition_pair_corrected_semidirect_holds_via_duality(
                partition,
                max_constraint_total_degree=max_constraint_total_degree,
                survivor_total_degree=survivor_total_degree,
                max_internal_ce_degree=max_internal_ce_degree,
            ),
        )
        for partition, key in _nonprincipal_general_family_representative_items_in_range(
            min_n=min_n,
            max_n=max_n,
        )
    )


def _first_nonselfdual_full_constraint_counts() -> Tuple[int, int]:
    """Full positive-sector counts for the first non-self-dual hook pair."""
    source_profile, target_profile = first_nonselfdual_hook_pair_ghost_profiles()
    return len(source_profile), len(target_profile)


def first_nonselfdual_hook_pair_mixed_constraint_ghost_blocks(
    max_constraint_total_degree: int = 2,
) -> Tuple[Tuple[MixedConstraintGhostBRSTBlock, ...], Tuple[MixedConstraintGhostBRSTBlock, ...]]:
    """Mixed current-plus-ghost BRST blocks for the first non-self-dual hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_mixed_constraint_ghost_blocks(
        4,
        1,
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def first_nonselfdual_hook_pair_nonlinear_mixed_constraint_ghost_blocks(
    max_constraint_total_degree: int = 2,
) -> Tuple[Tuple[MixedConstraintGhostBRSTBlock, ...], Tuple[MixedConstraintGhostBRSTBlock, ...]]:
    """Mixed blocks with the nonlinear current-action term for the first hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_nonlinear_mixed_constraint_ghost_blocks(
        4,
        1,
        max_constraint_total_degree=max_constraint_total_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def first_nonselfdual_hook_pair_mixed_blocks_match_under_relabeling(
    max_constraint_total_degree: int = 2,
) -> bool:
    """Check the first hook-pair mixed BRST blocks match under the canonical relabeling."""
    source_blocks, target_blocks = first_nonselfdual_hook_pair_mixed_constraint_ghost_blocks(
        max_constraint_total_degree=max_constraint_total_degree
    )
    return _mixed_blocks_match_under_relabeling(
        source_blocks,
        target_blocks,
        label_map=first_nonselfdual_hook_pair_ghost_label_map(),
        side_map=first_nonselfdual_hook_pair_ghost_side_map(),
    )


def first_nonselfdual_hook_pair_nonlinear_blocks_match_under_relabeling(
    max_constraint_total_degree: int = 2,
) -> bool:
    """Check nonlinear first hook-pair mixed blocks match under canonical relabeling."""
    source_blocks, target_blocks = first_nonselfdual_hook_pair_nonlinear_mixed_constraint_ghost_blocks(
        max_constraint_total_degree=max_constraint_total_degree
    )
    return _mixed_blocks_match_under_relabeling(
        source_blocks,
        target_blocks,
        label_map=first_nonselfdual_hook_pair_ghost_label_map(),
        side_map=first_nonselfdual_hook_pair_ghost_side_map(),
    )


def first_nonselfdual_hook_pair_survivor_coupled_blocks_match_under_relabeling(
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> bool:
    """Check first hook-pair survivor-coupled blocks against the transpose-dual case."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_survivor_coupled_blocks_match_under_dual_swap(
        4,
        1,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def first_nonselfdual_hook_pair_corrected_semidirect_blocks_match_under_relabeling(
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> bool:
    """Check first hook-pair corrected semidirect blocks against the transpose-dual case."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_corrected_semidirect_blocks_match_under_dual_swap(
        4,
        1,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def sl3_subregular_mixed_constraint_ghost_blocks(
    max_constraint_total_degree: int = 3,
) -> Tuple[MixedConstraintGhostBRSTBlock, ...]:
    """Mixed current-plus-ghost BRST blocks for the subregular sl_3 seed."""
    constraints = sl3_subregular_constraints()
    character = sl3_subregular_constraint_character()
    return tuple(
        build_mixed_constraint_ghost_brst_block(
            shifted_current_labels=tuple(f"u_{item.root_label}" for item in constraints),
            c_ghost_labels=tuple(item.c_ghost for item in constraints),
            b_ghost_labels=tuple(item.b_ghost for item in constraints),
            chi_vector=tuple(character[item.root_label] for item in constraints),
            quadratic_terms=(),
            constraint_total_degree=total_degree,
            source_tag=f"A2_subregular_mixed_{total_degree}",
        )
        for total_degree in range(max_constraint_total_degree + 1)
    )


def sl3_subregular_nonlinear_mixed_constraint_ghost_blocks(
    max_constraint_total_degree: int = 3,
) -> Tuple[MixedConstraintGhostBRSTBlock, ...]:
    """Mixed blocks with nonlinear current-action term for the subregular sl_3 seed."""
    return sl3_subregular_mixed_constraint_ghost_blocks(
        max_constraint_total_degree=max_constraint_total_degree
    )


def sl3_subregular_internal_survivor_ce_blocks(
    max_survivor_polynomial_degree: int = 2,
) -> Tuple[InternalSurvivorCEBlock, ...]:
    """Internal reduced-survivor CE blocks for the subregular sl_3 seed."""
    survivors = sl3_subregular_strong_generator_candidates()
    survivor_labels = tuple(item.label for item in survivors)
    c_ghost_labels, b_ghost_labels = internal_survivor_ghost_labels(survivor_labels)
    reduced_brackets = sl3_subregular_projected_strong_brackets()
    quadratic_terms = internal_survivor_quadratic_ghost_terms(
        survivor_labels,
        reduced_brackets,
    )
    action_terms = internal_survivor_action_terms(survivor_labels, reduced_brackets)
    return tuple(
        build_internal_survivor_ce_block(
            survivor_labels=survivor_labels,
            c_ghost_labels=c_ghost_labels,
            b_ghost_labels=b_ghost_labels,
            quadratic_terms=quadratic_terms,
            survivor_action_terms=action_terms,
            survivor_polynomial_degree=degree,
            source_tag=f"A2_subregular_internal_survivor_{degree}",
        )
        for degree in range(max_survivor_polynomial_degree + 1)
    )


def sl3_subregular_semidirect_survivor_blocks(
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 2,
) -> Tuple[SemidirectSurvivorBRSTBlock, ...]:
    """Naive semidirect survivor BRST blocks for the subregular sl_3 seed."""
    constraints = sl3_subregular_constraints()
    character = sl3_subregular_constraint_character()
    survivors = sl3_subregular_strong_generator_candidates()
    survivor_labels = tuple(item.label for item in survivors)
    survivor_action = sl3_subregular_survivor_action_terms()
    internal_c_ghosts, internal_b_ghosts = internal_survivor_ghost_labels(survivor_labels)
    reduced_brackets = sl3_subregular_projected_strong_brackets()
    internal_quadratic = internal_survivor_quadratic_ghost_terms(
        survivor_labels,
        reduced_brackets,
    )
    internal_action = internal_survivor_action_terms(
        survivor_labels,
        reduced_brackets,
    )
    return tuple(
        build_semidirect_survivor_brst_block(
            shifted_current_labels=tuple(f"u_{item.root_label}" for item in constraints),
            survivor_labels=survivor_labels,
            c_ghost_labels=tuple(item.c_ghost for item in constraints),
            b_ghost_labels=tuple(item.b_ghost for item in constraints),
            internal_c_ghost_labels=internal_c_ghosts,
            internal_b_ghost_labels=internal_b_ghosts,
            chi_vector=tuple(character[item.root_label] for item in constraints),
            quadratic_terms=(),
            current_action_terms=(),
            survivor_action_terms=survivor_action,
            internal_quadratic_terms=internal_quadratic,
            internal_survivor_action_terms=internal_action,
            constraint_total_degree=total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
            source_tag=(
                f"A2_subregular_semidirect_survivor_"
                f"{total_degree}_{survivor_total_degree}_{max_internal_ce_degree}"
            ),
        )
        for total_degree in range(max_constraint_total_degree + 1)
    )


def sl3_subregular_corrected_semidirect_survivor_blocks(
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 2,
) -> Tuple[SemidirectSurvivorBRSTBlock, ...]:
    """Subregular semidirect blocks after the first transferred survivor correction."""
    constraints = sl3_subregular_constraints()
    character = sl3_subregular_constraint_character()
    survivors = sl3_subregular_strong_generator_candidates()
    survivor_labels = tuple(item.label for item in survivors)
    corrected_survivor_action = sl3_subregular_corrected_survivor_action_terms()
    internal_c_ghosts, internal_b_ghosts = internal_survivor_ghost_labels(survivor_labels)
    reduced_brackets = sl3_subregular_projected_strong_brackets()
    internal_quadratic = internal_survivor_quadratic_ghost_terms(
        survivor_labels,
        reduced_brackets,
    )
    internal_action = internal_survivor_action_terms(
        survivor_labels,
        reduced_brackets,
    )
    return tuple(
        build_semidirect_survivor_brst_block(
            shifted_current_labels=tuple(f"u_{item.root_label}" for item in constraints),
            survivor_labels=survivor_labels,
            c_ghost_labels=tuple(item.c_ghost for item in constraints),
            b_ghost_labels=tuple(item.b_ghost for item in constraints),
            internal_c_ghost_labels=internal_c_ghosts,
            internal_b_ghost_labels=internal_b_ghosts,
            chi_vector=tuple(character[item.root_label] for item in constraints),
            quadratic_terms=(),
            current_action_terms=(),
            survivor_action_terms=corrected_survivor_action,
            internal_quadratic_terms=internal_quadratic,
            internal_survivor_action_terms=internal_action,
            constraint_total_degree=total_degree,
            survivor_total_degree=survivor_total_degree,
            max_internal_ce_degree=max_internal_ce_degree,
            source_tag=(
                f"A2_subregular_corrected_semidirect_survivor_"
                f"{total_degree}_{survivor_total_degree}_{max_internal_ce_degree}"
            ),
        )
        for total_degree in range(max_constraint_total_degree + 1)
    )


def sl3_subregular_survivor_coupled_blocks(
    max_constraint_total_degree: int = 2,
    survivor_total_degree: int = 1,
) -> Tuple[SurvivorCoupledBRSTBlock, ...]:
    """Survivor-coupled BRST blocks for the subregular sl_3 seed."""
    constraints = sl3_subregular_constraints()
    character = sl3_subregular_constraint_character()
    survivors = sl3_subregular_strong_generator_candidates()
    survivor_action = sl3_subregular_survivor_action_terms()
    return tuple(
        build_survivor_coupled_brst_block(
            shifted_current_labels=tuple(f"u_{item.root_label}" for item in constraints),
            survivor_labels=tuple(item.label for item in survivors),
            c_ghost_labels=tuple(item.c_ghost for item in constraints),
            b_ghost_labels=tuple(item.b_ghost for item in constraints),
            chi_vector=tuple(character[item.root_label] for item in constraints),
            quadratic_terms=(),
            current_action_terms=(),
            survivor_action_terms=survivor_action,
            constraint_total_degree=total_degree,
            survivor_total_degree=survivor_total_degree,
            source_tag=f"A2_subregular_survivor_coupled_{total_degree}_{survivor_total_degree}",
        )
        for total_degree in range(max_constraint_total_degree + 1)
    )


def first_nonselfdual_hook_pair_internal_survivor_ce_blocks(
    max_survivor_polynomial_degree: int = 2,
) -> Tuple[Tuple[InternalSurvivorCEBlock, ...], Tuple[InternalSurvivorCEBlock, ...]]:
    """Internal reduced-survivor CE blocks for the first non-self-dual hook pair."""
    source_survivors, target_survivors = first_nonselfdual_hook_pair_surviving_field_candidates()
    source_labels = tuple(item.label for item in source_survivors)
    target_labels = tuple(item.label for item in target_survivors)
    source_c_ghosts, source_b_ghosts = internal_survivor_ghost_labels(source_labels)
    target_c_ghosts, target_b_ghosts = internal_survivor_ghost_labels(target_labels)
    source_brackets, target_brackets = first_nonselfdual_hook_pair_reduced_brackets()
    source_quadratic = internal_survivor_quadratic_ghost_terms(source_labels, source_brackets)
    target_quadratic = internal_survivor_quadratic_ghost_terms(target_labels, target_brackets)
    source_action = internal_survivor_action_terms(source_labels, source_brackets)
    target_action = internal_survivor_action_terms(target_labels, target_brackets)
    return (
        tuple(
            build_internal_survivor_ce_block(
                survivor_labels=source_labels,
                c_ghost_labels=source_c_ghosts,
                b_ghost_labels=source_b_ghosts,
                quadratic_terms=source_quadratic,
                survivor_action_terms=source_action,
                survivor_polynomial_degree=degree,
                source_tag=f"A3_hook_source_internal_survivor_{degree}",
            )
            for degree in range(max_survivor_polynomial_degree + 1)
        ),
        tuple(
            build_internal_survivor_ce_block(
                survivor_labels=target_labels,
                c_ghost_labels=target_c_ghosts,
                b_ghost_labels=target_b_ghosts,
                quadratic_terms=target_quadratic,
                survivor_action_terms=target_action,
                survivor_polynomial_degree=degree,
                source_tag=f"A3_hook_target_internal_survivor_{degree}",
            )
            for degree in range(max_survivor_polynomial_degree + 1)
        ),
    )


def first_nonselfdual_hook_pair_semidirect_survivor_blocks(
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Tuple[Tuple[SemidirectSurvivorBRSTBlock, ...], Tuple[SemidirectSurvivorBRSTBlock, ...]]:
    """Naive semidirect survivor BRST blocks for the first non-self-dual hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_semidirect_survivor_blocks(
        4,
        1,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def first_nonselfdual_hook_pair_corrected_semidirect_survivor_blocks(
    max_constraint_total_degree: int = 0,
    survivor_total_degree: int = 1,
    max_internal_ce_degree: int = 1,
) -> Tuple[Tuple[SemidirectSurvivorBRSTBlock, ...], Tuple[SemidirectSurvivorBRSTBlock, ...]]:
    """Corrected semidirect survivor blocks for the first non-self-dual hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_corrected_semidirect_survivor_blocks(
        4,
        1,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        max_internal_ce_degree=max_internal_ce_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def first_nonselfdual_hook_pair_survivor_coupled_blocks(
    max_constraint_total_degree: int = 1,
    survivor_total_degree: int = 1,
) -> Tuple[Tuple[SurvivorCoupledBRSTBlock, ...], Tuple[SurvivorCoupledBRSTBlock, ...]]:
    """Survivor-coupled BRST blocks for the first non-self-dual hook pair."""
    source_count, target_count = _first_nonselfdual_full_constraint_counts()
    return hook_pair_survivor_coupled_blocks(
        4,
        1,
        max_constraint_total_degree=max_constraint_total_degree,
        survivor_total_degree=survivor_total_degree,
        source_num_constraints=source_count,
        target_num_constraints=target_count,
    )


def verify_ds_reduction_seed(level=Symbol("k")) -> Dict[str, bool]:
    """Consistency checks for the DS seed scaffold."""
    k = sympify(level)
    seed = sl3_subregular_ds_seed(k)
    basis = sl3_subregular_basis_profile()
    grading_counts = Counter(item.ad_h_grade for item in basis)
    constraints = sl3_subregular_constraints()
    blueprint = sl3_subregular_brst_blueprint(k)
    truncated = sl3_subregular_truncated_brst_complex(k)
    hook_pair = first_nonselfdual_hook_pair_ds_seed(k)
    hook_source_spec, hook_target_spec = first_nonselfdual_hook_pair_specialized_complexes(
        k,
        source_chi=(0, 1, 0, 0, 0),
        target_chi=(0, 1, 0, 0, 0),
    )
    hook_source_blueprint, hook_target_blueprint = first_nonselfdual_hook_pair_brst_blueprints(k)
    hook_source_profile, hook_target_profile = first_nonselfdual_hook_pair_ghost_profiles()
    hook_source_character, hook_target_character = first_nonselfdual_hook_pair_constraint_characters()
    hook_source_constraints, hook_target_constraints = first_nonselfdual_hook_pair_constraints()
    hook_source_candidates, hook_target_candidates = first_nonselfdual_hook_pair_surviving_field_candidates()
    hook_source_brackets, hook_target_brackets = first_nonselfdual_hook_pair_reduced_brackets()
    hook_source_quadratic, hook_target_quadratic = (
        first_nonselfdual_hook_pair_quadratic_ghost_term_support()
    )
    hook_source_action, hook_target_action = first_nonselfdual_hook_pair_current_action_terms()
    subregular_survivor_action = sl3_subregular_survivor_action_terms()
    subregular_action_lifts = sl3_subregular_survivor_action_lift_witnesses()
    subregular_derivation_defects = sl3_subregular_survivor_derivation_defects()
    subregular_defect_witnesses = sl3_subregular_derivation_defect_witnesses()
    subregular_first_correction_witnesses = (
        sl3_subregular_first_transfer_correction_witnesses()
    )
    subregular_first_correction = sl3_subregular_first_transfer_correction_terms()
    subregular_corrected_survivor_action = sl3_subregular_corrected_survivor_action_terms()
    subregular_corrected_derivation_defects = (
        sl3_subregular_corrected_survivor_derivation_defects()
    )
    hook_source_survivor_action, hook_target_survivor_action = (
        first_nonselfdual_hook_pair_survivor_action_terms()
    )
    hook_source_action_lifts, hook_target_action_lifts = (
        first_nonselfdual_hook_pair_survivor_action_lift_witnesses()
    )
    hook_source_current_witnesses, hook_target_current_witnesses = (
        first_nonselfdual_hook_pair_constraint_current_witnesses()
    )
    hook_source_derivation_defects, hook_target_derivation_defects = (
        first_nonselfdual_hook_pair_survivor_derivation_defects()
    )
    hook_source_defect_witnesses, hook_target_defect_witnesses = (
        first_nonselfdual_hook_pair_derivation_defect_witnesses()
    )
    hook_source_first_correction_witnesses, hook_target_first_correction_witnesses = (
        first_nonselfdual_hook_pair_first_transfer_correction_witnesses()
    )
    hook_source_first_correction, hook_target_first_correction = (
        first_nonselfdual_hook_pair_first_transfer_correction_terms()
    )
    hook_source_corrected_action, hook_target_corrected_action = (
        first_nonselfdual_hook_pair_corrected_survivor_action_terms()
    )
    hook_source_corrected_defects, hook_target_corrected_defects = (
        first_nonselfdual_hook_pair_corrected_survivor_derivation_defects()
    )
    basis_matrices = sl3_subregular_basis_matrices()
    e_matrix = basis_matrices["E12"]
    f_matrix = basis_matrices["F12"]
    ad_e_witnesses = sl3_subregular_ad_e_image_witnesses()
    ad_e_basis = sl3_subregular_ad_e_image_basis()
    strong_candidates = sl3_subregular_strong_generator_candidates()
    subregular_blocks = sl3_subregular_linear_constraint_blocks(max_total_degree=3)
    subregular_mixed_blocks = sl3_subregular_mixed_constraint_ghost_blocks(
        max_constraint_total_degree=3
    )
    subregular_nonlinear_blocks = sl3_subregular_nonlinear_mixed_constraint_ghost_blocks(
        max_constraint_total_degree=3
    )
    subregular_survivor_blocks = sl3_subregular_survivor_coupled_blocks(
        max_constraint_total_degree=2,
        survivor_total_degree=1,
    )
    subregular_internal_survivor_blocks = sl3_subregular_internal_survivor_ce_blocks(
        max_survivor_polynomial_degree=2
    )
    hook_source_blocks, hook_target_blocks = first_nonselfdual_hook_pair_linear_constraint_blocks(
        max_total_degree=3
    )
    hook_source_mixed_blocks, hook_target_mixed_blocks = (
        first_nonselfdual_hook_pair_mixed_constraint_ghost_blocks(max_constraint_total_degree=2)
    )
    hook_source_nonlinear_blocks, hook_target_nonlinear_blocks = (
        first_nonselfdual_hook_pair_nonlinear_mixed_constraint_ghost_blocks(
            max_constraint_total_degree=2
        )
    )
    hook_source_survivor_blocks, hook_target_survivor_blocks = (
        first_nonselfdual_hook_pair_survivor_coupled_blocks(
            max_constraint_total_degree=1,
            survivor_total_degree=1,
        )
    )
    hook_source_internal_survivor_blocks, hook_target_internal_survivor_blocks = (
        first_nonselfdual_hook_pair_internal_survivor_ce_blocks(
            max_survivor_polynomial_degree=2
        )
    )
    hook_source_survivor_blocks_deg2, hook_target_survivor_blocks_deg2 = (
        first_nonselfdual_hook_pair_survivor_coupled_blocks(
            max_constraint_total_degree=1,
            survivor_total_degree=2,
        )
    )
    subregular_linear_positive_summaries = _block_invariant_summaries(
        subregular_blocks[1:],
        linear_constraint_block_invariant_summary,
    )
    subregular_mixed_summaries = _block_invariant_summaries(
        subregular_mixed_blocks,
        mixed_constraint_ghost_block_invariant_summary,
    )
    subregular_nonlinear_summaries = _block_invariant_summaries(
        subregular_nonlinear_blocks,
        mixed_constraint_ghost_block_invariant_summary,
    )
    subregular_survivor_summaries = _block_invariant_summaries(
        subregular_survivor_blocks,
        survivor_coupled_block_invariant_summary,
    )
    hook_source_linear_positive_summaries = _block_invariant_summaries(
        hook_source_blocks[1:],
        linear_constraint_block_invariant_summary,
    )
    hook_target_linear_positive_summaries = _block_invariant_summaries(
        hook_target_blocks[1:],
        linear_constraint_block_invariant_summary,
    )
    hook_mixed_summaries = _block_invariant_summaries(
        hook_source_mixed_blocks + hook_target_mixed_blocks,
        mixed_constraint_ghost_block_invariant_summary,
    )
    hook_nonlinear_summaries = _block_invariant_summaries(
        hook_source_nonlinear_blocks + hook_target_nonlinear_blocks,
        mixed_constraint_ghost_block_invariant_summary,
    )
    hook_survivor_summaries = _block_invariant_summaries(
        hook_source_survivor_blocks + hook_target_survivor_blocks,
        survivor_coupled_block_invariant_summary,
    )
    # For the first non-self-dual hook pair, the degree-two target survivor
    # block is the dominant DS verifier hotspot. We only summarize the source
    # side here and recover the target side from the explicit relabeling check
    # recorded below.
    hook_source_survivor_deg2_summaries = _block_invariant_summaries(
        hook_source_survivor_blocks_deg2,
        survivor_coupled_block_invariant_summary,
    )
    results: Dict[str, bool] = {}

    results["seed orbit is subregular"] = (type_a_orbit_class(seed.partition) == "subregular")
    results["seed sl2 triple labels"] = (
        seed.sl2_triple.e == "E12"
        and seed.sl2_triple.h == "H1"
        and seed.sl2_triple.f == "F12"
    )
    results["seed dual level formula"] = (seed.dual_level == -k - 6)
    results["seed has positive grades only"] = all(item.ad_h_grade > 0 for item in seed.positive_grades)
    results["ghost weight balance b+c=1"] = all(
        (item.b_weight + item.c_weight) == 1 for item in seed.positive_grades
    )
    results["ghost profile roots expected"] = (
        {item.root_label for item in seed.positive_grades} == {"alpha1", "alpha1+alpha2"}
    )
    results["full basis grading matches sl3 multiplicities"] = (
        grading_counts == sl3_subregular_good_grading_multiplicities()
    )
    results["constraint roots match ghost profile"] = (
        {item.root_label for item in constraints} == {item.root_label for item in seed.positive_grades}
    )
    results["constraint character concentrated on alpha1"] = (
        sl3_subregular_constraint_character() == {"alpha1": 1, "alpha1+alpha2": 0}
    )
    results["positive nilpotent is abelian"] = (sl3_subregular_positive_nilpotent_brackets() == ())
    results["quadratic ghost term absent"] = (not blueprint.quadratic_ghost_term_present)
    results["bp current target is 5-field"] = (len(blueprint.expected_current_presentation) == 5)
    results["bp strong target is 4-field"] = (len(blueprint.expected_strong_presentation) == 4)
    results["subregular strong candidates match centralizer dimension"] = (
        len(strong_candidates) == centralizer_dimension_sl_n(seed.partition)
    )
    results["subregular ad_e-image basis has dimension four"] = (len(ad_e_basis) == 4)
    results["subregular ad_e-image witnesses are correct"] = all(
        matrix_commutator(
            e_matrix,
            ds_basis_expression_matrix(source_terms, basis_matrices),
        )
        == basis_matrices[label]
        for label, source_terms in ad_e_witnesses.items()
    )
    results["subregular strong candidates centralize f"] = all(
        matrix_commutator(
            f_matrix,
            ds_basis_expression_matrix(candidate.source_terms, basis_matrices),
        )
        == zeros(3, 3)
        for candidate in strong_candidates
    )
    results["subregular sl2 splitting spans sl3"] = (
        _sl3_subregular_split_basis_matrix().rank()
        == len(sl3_subregular_basis_profile())
    )
    results["subregular projection kills ad_e-image"] = all(
        sl3_subregular_project_basis_label_to_strong_candidates(item.label) == {}
        for item in ad_e_basis
    )
    results["subregular projection recovers BP fields"] = (
        sl3_subregular_project_basis_label_to_strong_candidates("H2") == {"J": 1}
        and sl3_subregular_project_basis_label_to_strong_candidates("E23") == {"G+": 1}
        and sl3_subregular_project_basis_label_to_strong_candidates("F13") == {"G-": 1}
        and sl3_subregular_project_basis_label_to_strong_candidates("F12") == {"T": 1}
    )
    projected_brackets = sl3_subregular_projected_strong_brackets()
    results["subregular projected strong brackets match seed"] = (
        projected_brackets[("J", "G+")] == {"G+": Rational(3, 2)}
        and projected_brackets[("J", "G-")] == {"G-": Rational(-3, 2)}
        and projected_brackets[("G+", "G-")] == {"T": 1}
        and projected_brackets[("T", "J")] == {}
        and projected_brackets[("T", "G+")] == {}
        and projected_brackets[("T", "G-")] == {}
    )
    results["subregular strong candidate profile matches BP"] = (
        tuple(
            (candidate.label, candidate.conformal_weight, candidate.parity)
            for candidate in strong_candidates
        )
        == blueprint.expected_strong_presentation
    )
    results["subregular truncated cochain dimensions 1-2-1"] = (
        tuple(len(truncated.basis_by_degree[d]) for d in (0, 1, 2)) == (1, 2, 1)
    )
    results["subregular truncated d0 nonzero"] = (
        truncated.differentials[0].rank() == 1
    )
    results["subregular truncated d1 nonzero"] = (
        truncated.differentials[1].rank() == 1
    )
    results["subregular truncated d^2 = 0"] = complex_has_nilpotent_differential(truncated)
    results["subregular truncated cohomology is zero"] = (
        truncated_cohomology_dimensions(truncated) == {0: 0, 1: 0, 2: 0}
    )
    results["subregular linear block degree-0 homology is vacuum line"] = (
        chain_homology_dimensions(subregular_blocks[0]) == {0: 1}
    )
    results["subregular linear positive blocks square to zero"] = (
        _all_block_summaries_have_square_zero(subregular_linear_positive_summaries)
    )
    results["subregular linear positive blocks contractible"] = all(
        linear_constraint_block_has_contracting_homotopy(block) for block in subregular_blocks[1:]
    )
    results["subregular linear positive blocks acyclic"] = (
        _all_block_summaries_are_acyclic(subregular_linear_positive_summaries)
    )
    results["subregular mixed blocks square to zero"] = (
        _all_block_summaries_have_square_zero(subregular_mixed_summaries)
    )
    results["subregular mixed blocks acyclic"] = (
        _all_block_summaries_are_acyclic(subregular_mixed_summaries)
    )
    results["subregular nonlinear mixed blocks square to zero"] = (
        _all_block_summaries_have_square_zero(subregular_nonlinear_summaries)
    )
    results["subregular nonlinear mixed blocks acyclic"] = (
        _all_block_summaries_are_acyclic(subregular_nonlinear_summaries)
    )
    results["subregular survivor action is explicit"] = (
        tuple(
            (item.c_ghost, item.source_survivor_label, item.target_survivor_label, item.coefficient)
            for item in subregular_survivor_action
        )
        == (
            ("c_alpha1+alpha2", "G-", "J", 1),
            ("c_alpha1+alpha2", "T", "G+", -1),
        )
    )
    results["subregular survivor-coupled blocks square to zero"] = (
        _all_block_summaries_have_square_zero(subregular_survivor_summaries)
    )
    results["subregular survivor-coupled blocks acyclic"] = (
        _all_block_summaries_are_acyclic(subregular_survivor_summaries)
    )
    results["subregular internal survivor CE blocks square to zero"] = all(
        internal_survivor_ce_block_has_square_zero(block)
        for block in subregular_internal_survivor_blocks
    )
    results["subregular internal survivor CE cohomology is nontrivial"] = (
        internal_survivor_ce_block_homology_dimensions(subregular_internal_survivor_blocks[1])
        == {0: 1, 1: 2, 2: 2, 3: 2, 4: 1}
    )
    results["subregular internal survivor linear invariant is T"] = (
        internal_survivor_linear_h0_labels(subregular_internal_survivor_blocks[1])
        == ((("T", 1),),)
    )
    results["subregular survivor action has derivation defects"] = (
        len(subregular_derivation_defects["c_alpha1+alpha2"]) == 8
        and subregular_derivation_defects["c_alpha1+alpha2"][("G+", "G-")]
        == {"G+": Rational(1, 2)}
    )
    results["subregular action lifts expose explicit ad_e witnesses"] = (
        any(
            item.c_ghost == "c_alpha1+alpha2"
            and item.source_survivor_label == "G-"
            and item.projected_terms == (("J", 1),)
            and item.ad_e_image_terms == (("H1", Rational(1, 2)),)
            and item.ad_e_witness_preimage == (("F12", Rational(1, 2)),)
            for item in subregular_action_lifts
        )
        and any(
            item.c_ghost == "c_alpha1+alpha2"
            and item.source_survivor_label == "J"
            and item.projected_terms == ()
            and item.ad_e_image_terms == (("E13", Rational(-3, 2)),)
            and item.ad_e_witness_preimage == (("E23", Rational(-3, 2)),)
            for item in subregular_action_lifts
        )
    )
    results["subregular defect witnesses recover the projected defect"] = all(
        dict(item.projected_defect_terms)
        == subregular_derivation_defects[item.c_ghost][
            (item.left_survivor_label, item.right_survivor_label)
        ]
        for item in subregular_defect_witnesses
    )
    results["subregular first transfer correction kills the naive survivor action"] = (
        first_transfer_correction_terms_from_witnesses(subregular_first_correction_witnesses)
        == subregular_first_correction
        and all(
            tuple(
                (target_survivor_label, simplify(-sympify(coefficient)))
                for target_survivor_label, coefficient in item.projected_action_terms
            )
            == item.correction_terms
            for item in subregular_first_correction_witnesses
        )
        and
        tuple(
            (item.c_ghost, item.source_survivor_label, item.target_survivor_label, item.coefficient)
            for item in subregular_first_correction
        )
        == (
            ("c_alpha1+alpha2", "G-", "J", -1),
            ("c_alpha1+alpha2", "T", "G+", 1),
        )
        and subregular_corrected_survivor_action == ()
        and subregular_corrected_derivation_defects == {}
    )
    results["subregular naive semidirect coupling fails square zero"] = (
        not any(
            semidirect_survivor_block_has_square_zero(block)
            for block in sl3_subregular_semidirect_survivor_blocks(
                max_constraint_total_degree=1,
                survivor_total_degree=1,
                max_internal_ce_degree=2,
            )
        )
    )
    results["subregular corrected semidirect coupling restores square zero"] = all(
        _partition_pair_corrected_semidirect_square_zero_flags(
            seed.partition,
            max_constraint_total_degree=1,
            survivor_total_degree=1,
            max_internal_ce_degree=2,
        )
    )
    results["first non-self-dual hook pair partitions"] = (
        hook_pair.source_partition == (3, 1)
        and hook_pair.target_partition == (2, 1, 1)
    )
    results["first non-self-dual hook pair level shift"] = (
        hook_pair.target_level == -k - 8
    )
    results["first hook pair positive ghost profiles use five directions"] = (
        len(hook_source_profile) == 5
        and len(hook_target_profile) == 5
        and hook_source_profile[0].root_label == "E13"
        and hook_source_profile[0].b_weight == 3
        and hook_target_profile[0].root_label == "E12"
        and hook_target_profile[0].b_weight == 2
    )
    results["first hook pair constraint characters factor through abelianization"] = (
        hook_source_character == {"E13": 0, "E12": 1, "E14": 0, "E23": 0, "E43": 0}
        and hook_target_character == {"E12": 0, "E13": 1, "E14": 0, "E32": 0, "E42": 0}
    )
    results["first hook pair constraints match ghost profiles"] = (
        tuple(item.root_label for item in hook_source_constraints)
        == tuple(item.root_label for item in hook_source_profile)
        and tuple(item.root_label for item in hook_target_constraints)
        == tuple(item.root_label for item in hook_target_profile)
        and tuple(item.character_value for item in hook_source_constraints) == (0, 1, 0, 0, 0)
        and tuple(item.character_value for item in hook_target_constraints) == (0, 1, 0, 0, 0)
    )
    hook_source_positive_brackets, hook_target_positive_brackets = (
        first_nonselfdual_hook_pair_positive_nilpotent_brackets()
    )
    results["first hook pair positive sectors are non-abelian"] = (
        hook_source_positive_brackets == (("E12", "E23", "E13"), ("E14", "E43", "E13"))
        and hook_target_positive_brackets == (("E13", "E32", "E12"), ("E14", "E42", "E12"))
    )
    results["first hook pair quadratic ghost support is explicit"] = (
        tuple(
            (item.left_c_ghost, item.right_c_ghost, item.target_b_ghost, item.coefficient)
            for item in hook_source_quadratic
        )
        == (
            ("c_source_E12", "c_source_E23", "b_source_E13", 1),
            ("c_source_E14", "c_source_E43", "b_source_E13", 1),
        )
        and tuple(
            (item.left_c_ghost, item.right_c_ghost, item.target_b_ghost, item.coefficient)
            for item in hook_target_quadratic
        )
        == (
            ("c_target_E13", "c_target_E32", "b_target_E12", 1),
            ("c_target_E14", "c_target_E42", "b_target_E12", 1),
        )
    )
    results["first hook pair current action is explicit"] = (
        tuple(
            (item.c_ghost, item.source_root_label, item.target_root_label, item.coefficient)
            for item in hook_source_action
        )
        == (
            ("c_source_E12", "E23", "E13", 1),
            ("c_source_E23", "E12", "E13", -1),
            ("c_source_E14", "E43", "E13", 1),
            ("c_source_E43", "E14", "E13", -1),
        )
        and tuple(
            (item.c_ghost, item.source_root_label, item.target_root_label, item.coefficient)
            for item in hook_target_action
        )
        == (
            ("c_target_E13", "E32", "E12", 1),
            ("c_target_E32", "E13", "E12", -1),
            ("c_target_E14", "E42", "E12", 1),
            ("c_target_E42", "E14", "E12", -1),
        )
    )
    results["first hook pair survivor action is explicit"] = (
        len(hook_source_survivor_action) == 6
        and len(hook_target_survivor_action) == 14
        and hook_source_survivor_action[0]
        == SurvivorActionTermEntry(
            c_ghost="c_source_E12",
            source_survivor_label="source_gm4_1",
            target_survivor_label="source_gm2_1",
            coefficient=Rational(-1, 2),
        )
        and hook_target_survivor_action[-1]
        == SurvivorActionTermEntry(
            c_ghost="c_target_E42",
            source_survivor_label="target_gm2_1",
            target_survivor_label="target_gm1_4",
            coefficient=1,
        )
    )
    results["first hook pair blueprints carry quadratic ghost term"] = (
        (not hook_source_blueprint.positive_nilpotent_is_abelian)
        and hook_source_blueprint.quadratic_ghost_term_present
        and (not hook_target_blueprint.positive_nilpotent_is_abelian)
        and hook_target_blueprint.quadratic_ghost_term_present
        and len(hook_source_blueprint.basis) == 15
        and len(hook_target_blueprint.basis) == 15
    )
    results["first hook pair surviving field counts"] = (
        len(hook_source_candidates) == 5
        and len(hook_target_candidates) == 9
    )
    results["first hook pair surviving weight profiles"] = (
        tuple(candidate.conformal_weight for candidate in hook_source_candidates)
        == (1, 2, 2, 2, 3)
        and tuple(candidate.conformal_weight for candidate in hook_target_candidates)
        == (1, 1, 1, 1, Rational(3, 2), Rational(3, 2), Rational(3, 2), Rational(3, 2), 2)
    )
    results["first hook source complex d^2 = 0"] = (
        complex_has_nilpotent_differential(hook_pair.source_complex)
    )
    results["first hook target complex d^2 = 0"] = (
        complex_has_nilpotent_differential(hook_pair.target_complex)
    )
    results["first hook source seed ghost cohomology vanishes"] = (
        truncated_cohomology_dimensions(hook_pair.source_complex)
        == {degree: 0 for degree in range(6)}
    )
    results["first hook target seed ghost cohomology vanishes"] = (
        truncated_cohomology_dimensions(hook_pair.target_complex)
        == {degree: 0 for degree in range(6)}
    )
    results["first hook source/target ghost complexes match under relabeling"] = (
        first_nonselfdual_hook_pair_ghost_complexes_match_under_relabeling(level=k)
    )
    results["first hook source specialized complex acyclic"] = (
        complex_is_acyclic(hook_source_spec)
    )
    results["first hook target specialized complex acyclic"] = (
        complex_is_acyclic(hook_target_spec)
    )
    results["first hook source linear positive blocks acyclic"] = (
        _all_block_summaries_are_acyclic(hook_source_linear_positive_summaries)
    )
    results["first hook source linear positive blocks contractible"] = all(
        linear_constraint_block_has_contracting_homotopy(block) for block in hook_source_blocks[1:]
    )
    results["first hook target linear positive blocks acyclic"] = (
        _all_block_summaries_are_acyclic(hook_target_linear_positive_summaries)
    )
    results["first hook target linear positive blocks contractible"] = all(
        linear_constraint_block_has_contracting_homotopy(block) for block in hook_target_blocks[1:]
    )
    results["first hook mixed blocks square to zero"] = (
        _all_block_summaries_have_square_zero(hook_mixed_summaries)
    )
    results["first hook mixed blocks are acyclic through constraint degree two"] = (
        _all_block_summaries_are_acyclic(hook_mixed_summaries)
    )
    results["first hook mixed blocks match under relabeling"] = (
        first_nonselfdual_hook_pair_mixed_blocks_match_under_relabeling(
            max_constraint_total_degree=2
        )
    )
    results["first hook nonlinear mixed blocks square to zero"] = (
        _all_block_summaries_have_square_zero(hook_nonlinear_summaries)
    )
    results["first hook nonlinear mixed blocks are acyclic through constraint degree two"] = (
        _all_block_summaries_are_acyclic(hook_nonlinear_summaries)
    )
    results["first hook nonlinear mixed blocks match under relabeling"] = (
        first_nonselfdual_hook_pair_nonlinear_blocks_match_under_relabeling(
            max_constraint_total_degree=2
        )
    )
    results["first hook nonlinear current term is nontrivial"] = (
        any(
            hook_source_nonlinear_blocks[1].differentials[degree]
            != hook_source_mixed_blocks[1].differentials[degree]
            for degree in hook_source_nonlinear_blocks[1].differentials
        )
        and any(
            hook_target_nonlinear_blocks[1].differentials[degree]
            != hook_target_mixed_blocks[1].differentials[degree]
            for degree in hook_target_nonlinear_blocks[1].differentials
        )
    )
    results["first hook survivor-coupled blocks square to zero"] = (
        _all_block_summaries_have_square_zero(hook_survivor_summaries)
    )
    results["first hook survivor-coupled blocks acyclic"] = (
        _all_block_summaries_are_acyclic(hook_survivor_summaries)
    )
    results["first hook survivor-coupled blocks match under dual swap"] = (
        first_nonselfdual_hook_pair_survivor_coupled_blocks_match_under_relabeling(
            max_constraint_total_degree=1,
            survivor_total_degree=1,
        )
    )
    results["first hook survivor-coupled blocks square to zero in survivor degree two"] = (
        _all_block_summaries_have_square_zero(hook_source_survivor_deg2_summaries)
    )
    results["first hook survivor-coupled blocks acyclic in survivor degree two"] = (
        _all_block_summaries_are_acyclic(hook_source_survivor_deg2_summaries)
    )
    results["first hook survivor-coupled blocks match under dual swap in survivor degree two"] = (
        first_nonselfdual_hook_pair_survivor_coupled_blocks_match_under_relabeling(
            max_constraint_total_degree=1,
            survivor_total_degree=2,
        )
    )
    results["first hook survivor feedback is nontrivial"] = (
        any(
            hook_source_survivor_blocks[1].differentials[degree]
            != hook_source_nonlinear_blocks[1].differentials[degree]
            for degree in hook_source_survivor_blocks[1].differentials
        )
        and any(
            hook_target_survivor_blocks[1].differentials[degree]
            != hook_target_nonlinear_blocks[1].differentials[degree]
            for degree in hook_target_survivor_blocks[1].differentials
        )
    )
    results["first hook internal survivor CE blocks square to zero"] = all(
        internal_survivor_ce_block_has_square_zero(block)
        for block in hook_source_internal_survivor_blocks + hook_target_internal_survivor_blocks
    )
    results["first hook internal survivor CE cohomology is nontrivial"] = (
        internal_survivor_ce_block_homology_dimensions(hook_source_internal_survivor_blocks[1])
        == {0: 2, 1: 5, 2: 5, 3: 5, 4: 5, 5: 2}
        and internal_survivor_ce_block_homology_dimensions(hook_target_internal_survivor_blocks[1])
        == {0: 1, 1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
    )
    results["first hook internal survivor linear invariants are explicit"] = (
        internal_survivor_linear_h0_labels(hook_source_internal_survivor_blocks[1])
        == ((("source_gm2_1", 1),), (("source_gm4_1", 1),))
        and internal_survivor_linear_h0_labels(hook_target_internal_survivor_blocks[1])
        == ((("target_gm2_1", 1),),)
    )
    results["first hook survivor action has derivation defects"] = (
        {ghost: len(items) for ghost, items in hook_source_derivation_defects.items()}
        == {
            "c_source_E12": 2,
            "c_source_E14": 8,
            "c_source_E23": 2,
            "c_source_E43": 8,
        }
        and {ghost: len(items) for ghost, items in hook_target_derivation_defects.items()}
        == {
            "c_target_E13": 26,
            "c_target_E14": 26,
            "c_target_E32": 26,
            "c_target_E42": 26,
        }
    )
    results["first hook action lifts expose explicit ad_e witnesses"] = (
        any(
            item.c_ghost == "c_source_E12"
            and item.source_survivor_label == "source_gm4_1"
            and item.projected_terms == (("source_gm2_1", Rational(-1, 2)),)
            and item.ad_e_witness_preimage == (("E31", Rational(1, 2)),)
            for item in hook_source_action_lifts
        )
        and any(
            item.c_ghost == "c_target_E13"
            and item.source_survivor_label == "target_gm1_3"
            and item.projected_terms == (("target_g0_3", 1),)
            and item.ad_e_witness_preimage == (("E21", Rational(1, 2)),)
            for item in hook_target_action_lifts
        )
    )
    results["first hook constrained currents are ad_e-exact with chosen witnesses"] = (
        hook_source_current_witnesses["E12"]
        == (("H1", Rational(-2, 3)), ("H2", Rational(-1, 3)))
        and hook_source_current_witnesses["E14"] == (("E24", 1),)
        and hook_target_current_witnesses["E13"] == (("E23", 1),)
        and hook_target_current_witnesses["E42"] == (("E41", -1),)
    )
    results["first hook defect witnesses recover the projected defect"] = (
        all(
            dict(item.projected_defect_terms)
            == hook_source_derivation_defects[item.c_ghost][
                (item.left_survivor_label, item.right_survivor_label)
            ]
            for item in hook_source_defect_witnesses
        )
        and all(
            dict(item.projected_defect_terms)
            == hook_target_derivation_defects[item.c_ghost][
                (item.left_survivor_label, item.right_survivor_label)
            ]
            for item in hook_target_defect_witnesses
        )
    )
    results["first hook naive semidirect coupling fails square zero"] = (
        not any(
            semidirect_survivor_block_has_square_zero(block)
            for blocks in first_nonselfdual_hook_pair_semidirect_survivor_blocks(
                max_constraint_total_degree=0,
                survivor_total_degree=1,
                max_internal_ce_degree=1,
            )
            for block in blocks
        )
    )
    results["first hook first transfer correction kills the naive survivor action"] = (
        first_transfer_correction_terms_from_witnesses(
            hook_source_first_correction_witnesses
        )
        == hook_source_first_correction
        and first_transfer_correction_terms_from_witnesses(
            hook_target_first_correction_witnesses
        )
        == hook_target_first_correction
        and
        hook_source_corrected_action == ()
        and hook_target_corrected_action == ()
        and hook_source_corrected_defects == {}
        and hook_target_corrected_defects == {}
        and len(hook_source_first_correction) == len(hook_source_survivor_action)
        and len(hook_target_first_correction) == len(hook_target_survivor_action)
        and hook_source_first_correction
        == tuple(
            SurvivorActionTermEntry(
                c_ghost=item.c_ghost,
                source_survivor_label=item.source_survivor_label,
                target_survivor_label=item.target_survivor_label,
                coefficient=simplify(-item.coefficient),
            )
            for item in hook_source_survivor_action
        )
        and hook_target_first_correction
        == tuple(
            SurvivorActionTermEntry(
                c_ghost=item.c_ghost,
                source_survivor_label=item.source_survivor_label,
                target_survivor_label=item.target_survivor_label,
                coefficient=simplify(-item.coefficient),
            )
            for item in hook_target_survivor_action
        )
    )
    results["first hook corrected semidirect coupling restores square zero"] = all(
        _hook_pair_corrected_semidirect_square_zero_flags(
            4,
            1,
            max_constraint_total_degree=0,
            survivor_total_degree=1,
            max_internal_ce_degree=1,
        )
    )
    results["first hook corrected semidirect coupling restores square zero in survivor degree two"] = all(
        _hook_pair_corrected_semidirect_square_zero_flags(
            4,
            1,
            max_constraint_total_degree=0,
            survivor_total_degree=2,
            max_internal_ce_degree=1,
        )
    )
    results["first hook reduced brackets close on survivors"] = (
        hook_source_brackets[("source_gm2_2", "source_gm2_3")] == {"source_gm4_1": 1}
        and hook_source_brackets[("source_g0_1", "source_gm2_2")] == {"source_gm2_2": Rational(4, 3)}
        and hook_target_brackets[("target_gm1_1", "target_gm1_3")] == {"target_gm2_1": 1}
        and hook_target_brackets[("target_g0_1", "target_g0_2")] == {"target_g0_4": 1}
    )
    generic_case = nonprincipal_hook_case(5, 2, level=k)
    generic_source_candidates, generic_target_candidates = hook_pair_surviving_field_candidates(5, 2)
    generic_source_brackets, generic_target_brackets = hook_pair_reduced_brackets(5, 2)
    results["A4 self-dual hook survivor counts match centralizer dimensions"] = (
        len(generic_source_candidates) == centralizer_dimension_sl_n(generic_case.partition)
        and len(generic_target_candidates) == centralizer_dimension_sl_n(generic_case.dual_partition)
    )
    results["A4 self-dual hook reduced brackets are nontrivial"] = (
        bool(generic_source_brackets)
        and bool(generic_target_brackets)
    )
    # Representative two-row and general non-principal family checks are covered
    # by the dedicated family-catalog tests. Keep this verifier concentrated on
    # the subregular and first-hook seed scaffold plus catalog-level seed data.
    # Family-wide duality catalogs are exercised by dedicated DS tests. Keep
    # this verifier focused on the seed scaffold and a handful of local
    # representative families so smoke runs do not duplicate the full catalog
    # sweep.
    results["hook pair catalog checks"] = all(
        verify_hook_pair_ds_seed_catalog(max_n=8, level=k).values()
    )
    results["hook pair/seed catalog alignment checks"] = all(
        verify_hook_pair_seed_alignment(max_n=8, level=k).values()
    )
    results["two-row non-hook seed catalog checks"] = all(
        verify_nonprincipal_two_row_seed_catalog(max_n=8, level=k).values()
    )
    results["general nonprincipal seed catalog checks"] = all(
        verify_nonprincipal_general_seed_catalog(max_n=7, level=k).values()
    )
    results["seed frontier track"] = (seed.track == TRACK_FRONTIER_NONPRINCIPAL)
    results["first hook pair frontier track"] = (hook_pair.track == TRACK_FRONTIER_NONPRINCIPAL)
    results["seed status tag"] = (seed.status == STATUS_DS_SEED)
    results["first hook pair seed status tag"] = (hook_pair.status == STATUS_DS_SEED)

    return results
