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

from sympy import Matrix, Rational, Symbol, sympify, zeros

from compute.lib.bv_duality import first_nonselfdual_type_a_hook_pair
from compute.lib.nonprincipal_ds_orbits import (
    TRACK_FRONTIER_NONPRINCIPAL,
    nonprincipal_hook_level_shift_ansatz_type_a,
    subregular_partition,
    type_a_orbit_class,
)
from compute.lib.nonprincipal_ds_reduction import (
    bp_current_presentation,
    bp_dual_level,
    bp_strong_presentation,
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
    """Paired DS seed complexes for the first non-self-dual hook orbit pair."""

    n: int
    r: int
    source_partition: Tuple[int, ...]
    target_partition: Tuple[int, ...]
    source_level: object
    target_level: object
    source_complex: TruncatedBRSTComplex
    target_complex: TruncatedBRSTComplex
    track: str


def brst_ghost_weights(ad_h_grade) -> Tuple[Rational, Rational]:
    """Ghost conformal weights from DS grading."""
    grade = sympify(ad_h_grade)
    return (Rational(1) + grade / 2, -grade / 2)


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


def first_nonselfdual_hook_pair_ds_seed(level=Symbol("k")) -> HookPairDSComplexSeed:
    """Paired DS seed complexes for the first non-self-dual type-A hook pair."""
    k = sympify(level)
    n, r, pair = first_nonselfdual_type_a_hook_pair()
    k_target = nonprincipal_hook_level_shift_ansatz_type_a(n, k)

    source_complex = build_character_wedge_complex(
        ghost_labels=("c_source_1", "c_source_2"),
        chi_vector=(Symbol("chi_source_1"), Symbol("chi_source_2")),
        source_tag="A3_hook_source_(3,1)",
    )
    target_complex = build_character_wedge_complex(
        ghost_labels=("c_target_1", "c_target_2"),
        chi_vector=(Symbol("chi_target_1"), Symbol("chi_target_2")),
        source_tag="A3_hook_target_(2,1,1)",
    )

    return HookPairDSComplexSeed(
        n=n,
        r=r,
        source_partition=pair.source_orbit,
        target_partition=pair.target_orbit,
        source_level=k,
        target_level=k_target,
        source_complex=source_complex,
        target_complex=target_complex,
        track=TRACK_FRONTIER_NONPRINCIPAL,
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
    results["first non-self-dual hook pair partitions"] = (
        hook_pair.source_partition == (3, 1)
        and hook_pair.target_partition == (2, 1, 1)
    )
    results["first non-self-dual hook pair level shift"] = (
        hook_pair.target_level == -k - 8
    )
    results["first hook source complex d^2 = 0"] = (
        complex_has_nilpotent_differential(hook_pair.source_complex)
    )
    results["first hook target complex d^2 = 0"] = (
        complex_has_nilpotent_differential(hook_pair.target_complex)
    )
    results["seed frontier track"] = (seed.track == TRACK_FRONTIER_NONPRINCIPAL)
    results["first hook pair frontier track"] = (hook_pair.track == TRACK_FRONTIER_NONPRINCIPAL)
    results["seed status tag"] = (seed.status == STATUS_DS_SEED)

    return results
