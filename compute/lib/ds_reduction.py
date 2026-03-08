"""Chain-level seed scaffold for non-principal Drinfeld-Sokolov reduction.

Current scope is intentionally narrow: the sl_3 subregular orbit seed used by
the non-principal frontier. This module does not compute BRST cohomology; it
records the structural inputs needed to launch that computation cleanly.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from typing import Dict, Tuple

from sympy import Matrix, Rational, Symbol, simplify, sympify, zeros

from compute.lib.bv_duality import first_nonselfdual_type_a_hook_pair
from compute.lib.nonprincipal_ds_orbits import (
    TRACK_FRONTIER_NONPRINCIPAL,
    ad_h_graded_basis_labels_sl_n,
    centralizer_dimension_sl_n,
    first_nonselfdual_hook_pair_sl2_triples,
    nonprincipal_hook_case,
    nonprincipal_hook_level_shift_ansatz_type_a,
    subregular_partition,
    type_a_orbit_class,
)
from compute.lib.nonprincipal_ds_reduction import (
    bp_current_presentation,
    bp_dual_level,
    bp_strong_presentation,
    nonprincipal_hook_seed_catalog,
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


ConstraintBasisElement = Tuple[Tuple[int, ...], Tuple[int, ...]]
DSBasisExpression = Tuple[Tuple[str, Rational], ...]


@dataclass(frozen=True)
class LinearConstraintBRSTBlock:
    """Finite total-degree block for the linear BRST/Koszul constraint complex."""

    source_tag: str
    shifted_current_labels: Tuple[str, ...]
    ghost_labels: Tuple[str, ...]
    total_degree: int
    basis_by_chain_degree: Dict[int, Tuple[ConstraintBasisElement, ...]]
    differentials: Dict[int, Matrix]


@dataclass(frozen=True)
class DSReducedFieldCandidate:
    """One candidate surviving field in the reduced DS algebra."""

    label: str
    source_terms: DSBasisExpression
    ad_h_grade: Rational
    conformal_weight: Rational
    parity: str


def brst_ghost_weights(ad_h_grade) -> Tuple[Rational, Rational]:
    """Ghost conformal weights from DS grading."""
    grade = sympify(ad_h_grade)
    return (Rational(1) + grade / 2, -grade / 2)


def matrix_commutator(left: Matrix, right: Matrix) -> Matrix:
    """Matrix commutator [left, right]."""
    return left * right - right * left


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
    matrix = zeros(3, 3)
    for label, coefficient in source_terms:
        matrix += sympify(coefficient) * basis_matrices[label]
    return matrix


def _ds_basis_expression_coordinates(
    source_terms: DSBasisExpression,
    basis_order: Tuple[str, ...],
) -> Matrix:
    """Coordinate column of a basis expression in the ordered basis."""
    index = {label: position for position, label in enumerate(basis_order)}
    coordinates = zeros(len(basis_order), 1)
    for label, coefficient in source_terms:
        coordinates[index[label], 0] += sympify(coefficient)
    return coordinates


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


def first_nonselfdual_hook_pair_ghost_profiles() -> Tuple[Tuple[DSGhostWeight, ...], Tuple[DSGhostWeight, ...]]:
    """Positive-grade ghost profiles for the first non-self-dual hook pair."""
    source_triple, target_triple = first_nonselfdual_hook_pair_sl2_triples()
    source_graded_basis = ad_h_graded_basis_labels_sl_n(source_triple.h)
    target_graded_basis = ad_h_graded_basis_labels_sl_n(target_triple.h)
    return (
        _ghost_profile_from_positive_grade_labels(source_graded_basis),
        _ghost_profile_from_positive_grade_labels(target_graded_basis),
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


def exterior_basis_indices(num_generators: int, degree: int) -> Tuple[Tuple[int, ...], ...]:
    """Ordered exterior basis in degree `degree` on `num_generators` symbols."""
    if degree < 0 or degree > num_generators:
        return ()
    return tuple(combinations(range(num_generators), degree))


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
        basis_set = set(basis)
        for ghost_index in range(num_ghosts):
            if ghost_index in basis_set:
                continue
            insertion_position = sum(1 for value in basis if value < ghost_index)
            sign = -1 if insertion_position % 2 else 1
            target = tuple(sorted(basis + (ghost_index,)))
            row = target_index[target]
            matrix[row, col] += sign * sympify(chi_vector[ghost_index])

    return matrix


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
        rank_curr = int(d_curr.rank()) if d_curr is not None else 0
        rank_prev = int(d_prev.rank()) if d_prev is not None else 0
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
    source_num_constraints: int = 2,
    target_num_constraints: int = 2,
) -> HookPairDSComplexSeed:
    """Paired symbolic DS complexes for one non-principal hook/subregular pair.

    This remains a truncated chain-level scaffold: the source/target sectors are
    finite exterior complexes with symbolic character entries.
    """
    if source_num_constraints < 1 or target_num_constraints < 1:
        raise ValueError("source_num_constraints and target_num_constraints must be positive")

    k = sympify(level)
    case = nonprincipal_hook_case(n, r, level=k)
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)

    source_complex = build_character_wedge_complex(
        ghost_labels=tuple(f"c_source_{index}" for index in range(1, source_num_constraints + 1)),
        chi_vector=tuple(
            Symbol(f"chi_source_{index}") for index in range(1, source_num_constraints + 1)
        ),
        source_tag=f"A{n-1}_hook_source_{partition_tag}",
    )
    target_complex = build_character_wedge_complex(
        ghost_labels=tuple(f"c_target_{index}" for index in range(1, target_num_constraints + 1)),
        chi_vector=tuple(
            Symbol(f"chi_target_{index}") for index in range(1, target_num_constraints + 1)
        ),
        source_tag=f"A{n-1}_hook_target_{dual_tag}",
    )

    return HookPairDSComplexSeed(
        n=n,
        r=r,
        source_partition=case.partition,
        target_partition=case.dual_partition,
        source_level=k,
        target_level=case.level_shift,
        source_complex=source_complex,
        target_complex=target_complex,
        track=TRACK_FRONTIER_NONPRINCIPAL,
    )


def hook_pair_specialized_complexes(
    n: int,
    r: int,
    level=Symbol("k"),
    source_chi: Tuple[object, ...] | None = None,
    target_chi: Tuple[object, ...] | None = None,
    source_num_constraints: int = 2,
    target_num_constraints: int = 2,
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
    k = sympify(level)
    n, r, _ = first_nonselfdual_type_a_hook_pair()
    case = nonprincipal_hook_case(n, r, level=k)
    source_profile, target_profile = first_nonselfdual_hook_pair_ghost_profiles()

    source_complex = build_character_wedge_complex(
        ghost_labels=tuple(f"c_source_{item.root_label}" for item in source_profile),
        chi_vector=tuple(Symbol(f"chi_source_{item.root_label}") for item in source_profile),
        source_tag="A3_hook_source_3_1",
    )
    target_complex = build_character_wedge_complex(
        ghost_labels=tuple(f"c_target_{item.root_label}" for item in target_profile),
        chi_vector=tuple(Symbol(f"chi_target_{item.root_label}") for item in target_profile),
        source_tag="A3_hook_target_2_1_1",
    )

    return HookPairDSComplexSeed(
        n=n,
        r=r,
        source_partition=case.partition,
        target_partition=case.dual_partition,
        source_level=k,
        target_level=case.level_shift,
        source_complex=source_complex,
        target_complex=target_complex,
        track=TRACK_FRONTIER_NONPRINCIPAL,
    )


def first_nonselfdual_hook_pair_specialized_complexes(
    level=Symbol("k"),
    source_chi: Tuple[object, ...] | None = None,
    target_chi: Tuple[object, ...] | None = None,
) -> Tuple[TruncatedBRSTComplex, TruncatedBRSTComplex]:
    """Specialize the first hook-pair seed complexes to concrete chi values."""
    seed = first_nonselfdual_hook_pair_ds_seed(level=level)
    if source_chi is None:
        source_chi = _default_nonzero_character(len(seed.source_complex.ghost_labels))
    if target_chi is None:
        target_chi = _default_nonzero_character(len(seed.target_complex.ghost_labels))
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


def hook_pair_ds_seed_catalog(
    max_n: int = 6,
    level=Symbol("k"),
    source_num_constraints: int = 2,
    target_num_constraints: int = 2,
) -> Tuple[HookPairDSComplexSeed, ...]:
    """Enumerate hook/subregular DS pair seeds in type A."""
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
    k = sympify(level)
    results: Dict[str, bool] = {}
    seeds = hook_pair_ds_seed_catalog(max_n=max_n, level=k)

    results["hook DS pair catalog is nonempty"] = bool(seeds)
    results["hook DS pair catalog stays on frontier track"] = all(
        seed.track == TRACK_FRONTIER_NONPRINCIPAL for seed in seeds
    )

    for seed in seeds:
        n = seed.n
        r = seed.r
        case = nonprincipal_hook_case(n, r, level=k)
        key = f"A{n-1} hook r={r}"
        source_spec, target_spec = hook_pair_specialized_complexes(
            n,
            r,
            level=k,
            source_num_constraints=len(seed.source_complex.ghost_labels),
            target_num_constraints=len(seed.target_complex.ghost_labels),
        )

        results[f"{key} partition propagation"] = (
            seed.source_partition == case.partition
            and seed.target_partition == case.dual_partition
        )
        results[f"{key} level shift propagation"] = (
            simplify(seed.target_level - nonprincipal_hook_level_shift_ansatz_type_a(n, k)) == 0
        )
        results[f"{key} class is non-principal hook/subregular"] = (
            type_a_orbit_class(seed.source_partition) in {"subregular", "hook_nonprincipal"}
        )
        results[f"{key} source complex nilpotent"] = (
            complex_has_nilpotent_differential(seed.source_complex)
        )
        results[f"{key} target complex nilpotent"] = (
            complex_has_nilpotent_differential(seed.target_complex)
        )
        results[f"{key} source specialization acyclic"] = complex_is_acyclic(source_spec)
        results[f"{key} target specialization acyclic"] = complex_is_acyclic(target_spec)

    first = first_nonselfdual_hook_pair_ds_seed(level=k)
    results["first hook DS pair remains A3"] = (
        first.n == 4
        and first.r == 1
        and first.source_partition == (3, 1)
        and first.target_partition == (2, 1, 1)
    )
    return results


def verify_hook_pair_seed_alignment(max_n: int = 8, level=Symbol("k")) -> Dict[str, bool]:
    """Cross-check DS pair catalog against non-principal DS seed catalog."""
    k = sympify(level)
    results: Dict[str, bool] = {}
    pair_catalog = hook_pair_ds_seed_catalog(max_n=max_n, level=k)
    seed_catalog = nonprincipal_hook_seed_catalog(max_n=max_n, level=k)

    results["hook pair catalog matches seed catalog size"] = (
        len(pair_catalog) == len(seed_catalog)
    )
    for pair_seed, seed in zip(pair_catalog, seed_catalog):
        key = f"A{pair_seed.n-1} hook r={pair_seed.r}"
        results[f"{key} partition alignment"] = (
            pair_seed.source_partition == seed.partition
            and pair_seed.target_partition == seed.dual_partition
        )
        results[f"{key} level-shift alignment"] = (
            simplify(pair_seed.target_level - seed.level_shift) == 0
        )
        results[f"{key} track alignment"] = (pair_seed.track == seed.track)

    return results


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


def chain_homology_dimensions(block: LinearConstraintBRSTBlock) -> Dict[int, int]:
    """Compute chain homology dimensions for a finite linear constraint block."""
    dims: Dict[int, int] = {}
    max_degree = max(block.basis_by_chain_degree)
    for degree in range(max_degree + 1):
        dim_c = len(block.basis_by_chain_degree[degree])
        d_down = block.differentials.get(degree)
        d_up = block.differentials.get(degree + 1)
        rank_down = int(d_down.rank()) if d_down is not None else 0
        rank_up = int(d_up.rank()) if d_up is not None else 0
        ker_dim = dim_c - rank_down
        dims[degree] = ker_dim - rank_up
    return dims


def linear_constraint_block_has_square_zero(block: LinearConstraintBRSTBlock) -> bool:
    """Check d^2 = 0 for a linear constraint block."""
    for degree, d_k in block.differentials.items():
        d_km1 = block.differentials.get(degree - 1)
        if d_km1 is None:
            continue
        if d_km1 * d_k != zeros(d_km1.rows, d_k.cols):
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
    num_constraints: int = 2,
) -> Tuple[Tuple[LinearConstraintBRSTBlock, ...], Tuple[LinearConstraintBRSTBlock, ...]]:
    """Linear BRST/Koszul blocks for one hook/subregular DS seed pair."""
    if num_constraints < 1:
        raise ValueError("num_constraints must be positive")

    case = nonprincipal_hook_case(n, r)
    partition_tag = "_".join(str(part) for part in case.partition)
    dual_tag = "_".join(str(part) for part in case.dual_partition)

    source_shifted_labels = tuple(f"u_source_{index}" for index in range(1, num_constraints + 1))
    source_ghost_labels = tuple(f"b_source_{index}" for index in range(1, num_constraints + 1))
    source_blocks = tuple(
        build_linear_constraint_koszul_block(
            shifted_current_labels=source_shifted_labels,
            ghost_labels=source_ghost_labels,
            total_degree=total_degree,
            source_tag=f"A{n-1}_hook_source_{partition_tag}_linear_block_deg_{total_degree}",
        )
        for total_degree in range(max_total_degree + 1)
    )

    target_shifted_labels = tuple(f"u_target_{index}" for index in range(1, num_constraints + 1))
    target_ghost_labels = tuple(f"b_target_{index}" for index in range(1, num_constraints + 1))
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
        source_chi=(1, 0, 0, 0, 0),
        target_chi=(1, 0, 0, 0, 0),
    )
    hook_source_profile, hook_target_profile = first_nonselfdual_hook_pair_ghost_profiles()
    basis_matrices = sl3_subregular_basis_matrices()
    e_matrix = basis_matrices["E12"]
    f_matrix = basis_matrices["F12"]
    ad_e_witnesses = sl3_subregular_ad_e_image_witnesses()
    ad_e_basis = sl3_subregular_ad_e_image_basis()
    strong_candidates = sl3_subregular_strong_generator_candidates()
    subregular_blocks = sl3_subregular_linear_constraint_blocks(max_total_degree=3)
    hook_source_blocks, hook_target_blocks = first_nonselfdual_hook_pair_linear_constraint_blocks(
        max_total_degree=3
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
    results["subregular linear positive blocks square to zero"] = all(
        linear_constraint_block_has_square_zero(block) for block in subregular_blocks[1:]
    )
    results["subregular linear positive blocks contractible"] = all(
        linear_constraint_block_has_contracting_homotopy(block) for block in subregular_blocks[1:]
    )
    results["subregular linear positive blocks acyclic"] = all(
        linear_constraint_block_is_positive_acyclic(block) for block in subregular_blocks[1:]
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
    results["first hook source complex d^2 = 0"] = (
        complex_has_nilpotent_differential(hook_pair.source_complex)
    )
    results["first hook target complex d^2 = 0"] = (
        complex_has_nilpotent_differential(hook_pair.target_complex)
    )
    results["first hook source specialized complex acyclic"] = (
        complex_is_acyclic(hook_source_spec)
    )
    results["first hook target specialized complex acyclic"] = (
        complex_is_acyclic(hook_target_spec)
    )
    results["first hook source linear positive blocks acyclic"] = all(
        linear_constraint_block_is_positive_acyclic(block) for block in hook_source_blocks[1:]
    )
    results["first hook source linear positive blocks contractible"] = all(
        linear_constraint_block_has_contracting_homotopy(block) for block in hook_source_blocks[1:]
    )
    results["first hook target linear positive blocks acyclic"] = all(
        linear_constraint_block_is_positive_acyclic(block) for block in hook_target_blocks[1:]
    )
    results["first hook target linear positive blocks contractible"] = all(
        linear_constraint_block_has_contracting_homotopy(block) for block in hook_target_blocks[1:]
    )
    results["hook pair catalog checks"] = all(
        verify_hook_pair_ds_seed_catalog(max_n=8, level=k).values()
    )
    results["hook pair/seed catalog alignment checks"] = all(
        verify_hook_pair_seed_alignment(max_n=8, level=k).values()
    )
    results["seed frontier track"] = (seed.track == TRACK_FRONTIER_NONPRINCIPAL)
    results["first hook pair frontier track"] = (hook_pair.track == TRACK_FRONTIER_NONPRINCIPAL)
    results["seed status tag"] = (seed.status == STATUS_DS_SEED)

    return results
