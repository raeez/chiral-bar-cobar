"""Tests for DS reduction seed scaffold."""

from collections import Counter

from sympy import Matrix, Rational, Symbol, simplify, zeros

from compute.lib.nonprincipal_ds_reduction import bp_strong_presentation
from compute.lib.nonprincipal_ds_orbits import centralizer_dimension_sl_n

from compute.lib.ds_reduction import (
    DSBRSTBlueprint,
    DSBasisElement,
    DSReducedFieldCandidate,
    CurrentActionTermEntry,
    SurvivorActionTermEntry,
    QuadraticGhostTermEntry,
    DSReductionSeed,
    DSConstraint,
    HookPairDSComplexSeed,
    InternalSurvivorCEBlock,
    LinearConstraintBRSTBlock,
    MixedConstraintGhostBRSTBlock,
    SurvivorCoupledBRSTBlock,
    STATUS_DS_SEED,
    TruncatedBRSTComplex,
    build_character_wedge_complex,
    build_ghost_brst_complex,
    build_mixed_constraint_ghost_brst_block,
    build_linear_constraint_koszul_block,
    character_wedge_differential,
    chain_homology_dimensions,
    complex_has_nilpotent_differential,
    complex_is_acyclic,
    ds_basis_expression_matrix,
    differential_square_blocks,
    exact_matrix_rank,
    exterior_basis_indices,
    first_nonselfdual_hook_pair_ds_seed,
    first_nonselfdual_hook_pair_basis_profiles,
    first_nonselfdual_hook_pair_brst_blueprints,
    hook_pair_ds_seed,
    hook_pair_ds_seed_catalog,
    hook_pair_ghost_profiles,
    hook_pair_linear_constraint_blocks,
    hook_pair_constraint_characters,
    hook_pair_constraints,
    hook_pair_positive_nilpotent_brackets,
    hook_pair_quadratic_ghost_term_support,
    hook_pair_current_action_terms,
    hook_pair_mixed_constraint_ghost_blocks,
    hook_pair_nonlinear_mixed_constraint_ghost_blocks,
    hook_pair_mixed_blocks_match_under_dual_swap,
    hook_pair_nonlinear_blocks_match_under_dual_swap,
    verify_hook_pair_mixed_block_duality_catalog,
    verify_hook_pair_nonlinear_block_duality_catalog,
    hook_pair_surviving_field_candidates,
    hook_pair_reduced_brackets,
    hook_pair_specialized_complexes,
    first_nonselfdual_hook_pair_linear_constraint_blocks,
    first_nonselfdual_hook_pair_mixed_constraint_ghost_blocks,
    first_nonselfdual_hook_pair_nonlinear_mixed_constraint_ghost_blocks,
    first_nonselfdual_hook_pair_ghost_profiles,
    first_nonselfdual_hook_pair_constraint_characters,
    first_nonselfdual_hook_pair_constraints,
    first_nonselfdual_hook_pair_current_action_terms,
    first_nonselfdual_hook_pair_survivor_action_terms,
    first_nonselfdual_hook_pair_positive_nilpotent_brackets,
    first_nonselfdual_hook_pair_quadratic_ghost_term_support,
    first_nonselfdual_hook_pair_ghost_label_map,
    first_nonselfdual_hook_pair_ghost_side_map,
    first_nonselfdual_hook_pair_ghost_complexes_match_under_relabeling,
    first_nonselfdual_hook_pair_reduced_brackets,
    first_nonselfdual_hook_pair_specialized_complexes,
    first_nonselfdual_hook_pair_surviving_field_candidates,
    first_nonselfdual_hook_pair_internal_survivor_ce_blocks,
    first_nonselfdual_hook_pair_mixed_blocks_match_under_relabeling,
    first_nonselfdual_hook_pair_nonlinear_blocks_match_under_relabeling,
    first_nonselfdual_hook_pair_survivor_coupled_blocks,
    ghost_brst_differential,
    brst_ghost_weights,
    homogeneous_monomial_exponents,
    linear_constraint_block_basis,
    linear_constraint_block_has_contracting_homotopy,
    linear_constraint_block_has_square_zero,
    linear_constraint_block_is_positive_acyclic,
    linear_constraint_contracting_homotopy,
    linear_constraint_koszul_differential,
    matrix_commutator,
    mixed_constraint_ghost_block_basis,
    mixed_constraint_ghost_block_has_square_zero,
    mixed_constraint_ghost_block_homology_dimensions,
    mixed_constraint_ghost_block_is_acyclic,
    current_action_differential,
    internal_survivor_action_terms,
    internal_survivor_ce_block_basis,
    internal_survivor_ce_block_homology_dimensions,
    internal_survivor_ce_block_has_square_zero,
    internal_survivor_ce_block_is_acyclic,
    internal_survivor_ce_differential,
    internal_survivor_ghost_labels,
    internal_survivor_quadratic_ghost_terms,
    mixed_constraint_ghost_brst_differential,
    quadratic_ghost_differential,
    survivor_action_differential,
    survivor_coupled_block_basis,
    survivor_coupled_block_has_square_zero,
    survivor_coupled_block_homology_dimensions,
    survivor_coupled_block_is_acyclic,
    relabel_current_action_terms,
    relabel_mixed_constraint_ghost_block,
    relabel_quadratic_ghost_terms,
    relabel_truncated_brst_complex,
    sl3_subregular_ad_e_image_basis,
    sl3_subregular_ad_e_image_witnesses,
    sl3_subregular_basis_grades,
    sl3_subregular_basis_matrices,
    sl3_subregular_basis_profile,
    sl3_subregular_brst_blueprint,
    sl3_subregular_constraint_character,
    sl3_subregular_constraints,
    sl3_subregular_ds_seed,
    sl3_subregular_ghost_profile,
    sl3_subregular_linear_constraint_blocks,
    sl3_subregular_mixed_constraint_ghost_blocks,
    sl3_subregular_nonlinear_mixed_constraint_ghost_blocks,
    sl3_subregular_internal_survivor_ce_blocks,
    sl3_subregular_positive_nilpotent_brackets,
    sl3_subregular_positive_grades,
    sl3_subregular_survivor_action_terms,
    sl3_subregular_survivor_coupled_blocks,
    sl3_subregular_project_basis_label_to_strong_candidates,
    sl3_subregular_project_expression_to_strong_candidates,
    sl3_subregular_projected_strong_brackets,
    sl3_subregular_sl2_triple,
    sl3_subregular_strong_generator_candidates,
    sl3_subregular_truncated_brst_complex,
    specialize_complex_chi,
    truncated_cohomology_dimensions,
    verify_hook_pair_ds_seed_catalog,
    verify_hook_pair_seed_alignment,
    verify_ds_reduction_seed,
)


class TestGhostWeights:
    def test_formula(self):
        b, c = brst_ghost_weights(Rational(2))
        assert b == 2
        assert c == -1
        assert b + c == 1

    def test_profile_values(self):
        profile = {item.root_label: item for item in sl3_subregular_ghost_profile()}
        assert profile["alpha1"].ad_h_grade == 2
        assert profile["alpha1"].b_weight == 2
        assert profile["alpha1"].c_weight == -1
        assert profile["alpha1+alpha2"].ad_h_grade == 1
        assert profile["alpha1+alpha2"].b_weight == Rational(3, 2)
        assert profile["alpha1+alpha2"].c_weight == Rational(-1, 2)


class TestSl3SubregularSeed:
    def test_triple(self):
        triple = sl3_subregular_sl2_triple()
        assert (triple.e, triple.h, triple.f) == ("E12", "H1", "F12")

    def test_basis_grading(self):
        grades = sl3_subregular_basis_grades()
        assert grades == {
            "E12": 2,
            "E13": 1,
            "F23": 1,
            "H1": 0,
            "H2": 0,
            "E23": -1,
            "F13": -1,
            "F12": -2,
        }

        profile = sl3_subregular_basis_profile()
        assert all(isinstance(item, DSBasisElement) for item in profile)
        assert Counter(item.ad_h_grade for item in profile) == {
            -2: 1,
            -1: 2,
            0: 2,
            1: 2,
            2: 1,
        }

    def test_positive_grades(self):
        grades = sl3_subregular_positive_grades()
        assert grades == {"alpha1": 2, "alpha1+alpha2": 1}

    def test_constraints_and_brackets(self):
        assert sl3_subregular_constraint_character() == {
            "alpha1": 1,
            "alpha1+alpha2": 0,
        }

        constraints = {item.root_label: item for item in sl3_subregular_constraints()}
        assert all(isinstance(item, DSConstraint) for item in constraints.values())
        assert constraints["alpha1"].current_label == "E12"
        assert constraints["alpha1"].character_value == 1
        assert constraints["alpha1"].b_ghost == "b_alpha1"
        assert constraints["alpha1"].c_ghost == "c_alpha1"
        assert constraints["alpha1+alpha2"].current_label == "E13"
        assert constraints["alpha1+alpha2"].character_value == 0
        assert sl3_subregular_positive_nilpotent_brackets() == ()

    def test_seed_record(self):
        k = Symbol("k")
        seed = sl3_subregular_ds_seed(k)
        assert isinstance(seed, DSReductionSeed)
        assert seed.partition == (2, 1)
        assert simplify(seed.dual_level - (-k - 6)) == 0
        assert seed.expected_target == "affine_sl2_seed"
        assert seed.track == "frontier_nonprincipal_ds_orbit"
        assert seed.status == STATUS_DS_SEED

    def test_brst_blueprint(self):
        blueprint = sl3_subregular_brst_blueprint()
        assert isinstance(blueprint, DSBRSTBlueprint)
        assert blueprint.seed.partition == (2, 1)
        assert blueprint.positive_nilpotent_is_abelian
        assert not blueprint.quadratic_ghost_term_present
        assert len(blueprint.constraints) == 2
        assert blueprint.expected_current_presentation[0][0] == "J1"
        assert blueprint.expected_strong_presentation[-1][0] == "T"

    def test_strong_generator_candidates(self):
        candidates = sl3_subregular_strong_generator_candidates()
        assert all(isinstance(item, DSReducedFieldCandidate) for item in candidates)
        assert tuple((item.label, item.conformal_weight, item.parity) for item in candidates) == (
            bp_strong_presentation()
        )
        assert Counter(item.ad_h_grade for item in candidates) == {0: 1, -1: 2, -2: 1}

    def test_strong_generator_candidates_centralize_f(self):
        basis_matrices = sl3_subregular_basis_matrices()
        f_matrix = basis_matrices["F12"]
        for candidate in sl3_subregular_strong_generator_candidates():
            matrix = ds_basis_expression_matrix(candidate.source_terms, basis_matrices)
            assert matrix_commutator(f_matrix, matrix) == zeros(3, 3)

    def test_ad_e_image_witnesses_and_splitting(self):
        basis_matrices = sl3_subregular_basis_matrices()
        e_matrix = basis_matrices["E12"]
        image_basis = sl3_subregular_ad_e_image_basis()
        image_witnesses = sl3_subregular_ad_e_image_witnesses()
        assert [item.label for item in image_basis] == ["H1", "E12", "E13", "F23"]
        assert Counter(item.ad_h_grade for item in image_basis) == {0: 1, 1: 2, 2: 1}
        for label, witness in image_witnesses.items():
            matrix = ds_basis_expression_matrix(witness, basis_matrices)
            assert matrix_commutator(e_matrix, matrix) == basis_matrices[label]

        spanning_columns = [
            basis_matrices[item.label].reshape(9, 1) for item in image_basis
        ] + [
            ds_basis_expression_matrix(candidate.source_terms, basis_matrices).reshape(9, 1)
            for candidate in sl3_subregular_strong_generator_candidates()
        ]
        assert simplify(Matrix.hstack(*spanning_columns).rank() - 8) == 0

    def test_projection_to_strong_candidates(self):
        assert sl3_subregular_project_basis_label_to_strong_candidates("H1") == {}
        assert sl3_subregular_project_basis_label_to_strong_candidates("E12") == {}
        assert sl3_subregular_project_basis_label_to_strong_candidates("E13") == {}
        assert sl3_subregular_project_basis_label_to_strong_candidates("F23") == {}
        assert sl3_subregular_project_basis_label_to_strong_candidates("H2") == {"J": 1}
        assert sl3_subregular_project_basis_label_to_strong_candidates("E23") == {"G+": 1}
        assert sl3_subregular_project_basis_label_to_strong_candidates("F13") == {"G-": 1}
        assert sl3_subregular_project_basis_label_to_strong_candidates("F12") == {"T": 1}
        assert sl3_subregular_project_expression_to_strong_candidates(
            (("H1", Rational(1)), ("H2", Rational(1)))
        ) == {"J": 1}

    def test_projected_strong_brackets(self):
        brackets = sl3_subregular_projected_strong_brackets()
        assert brackets[("J", "G+")] == {"G+": Rational(3, 2)}
        assert brackets[("J", "G-")] == {"G-": Rational(-3, 2)}
        assert brackets[("G+", "J")] == {"G+": Rational(-3, 2)}
        assert brackets[("G-", "J")] == {"G-": Rational(3, 2)}
        assert brackets[("G+", "G-")] == {"T": 1}
        assert brackets[("G-", "G+")] == {"T": -1}
        assert brackets[("T", "J")] == {}
        assert brackets[("T", "G+")] == {}
        assert brackets[("T", "G-")] == {}


class TestTruncatedComplex:
    def test_exterior_basis(self):
        assert exterior_basis_indices(2, 0) == ((),)
        assert exterior_basis_indices(2, 1) == ((0,), (1,))
        assert exterior_basis_indices(2, 2) == ((0, 1),)

    def test_character_wedge_matrices(self):
        d0 = character_wedge_differential(2, (1, 0), 0)
        d1 = character_wedge_differential(2, (1, 0), 1)
        assert d0.shape == (2, 1)
        assert d1.shape == (1, 2)
        # d(1) = c_1
        assert d0[0, 0] == 1
        assert d0[1, 0] == 0
        # d(c_1)=0, d(c_2)=c_1^c_2
        assert d1[0, 0] == 0
        assert d1[0, 1] == 1
        assert d1 * d0 == d1.zeros(1, 1)

    def test_manual_complex_builder(self):
        complex_seed = build_character_wedge_complex(
            ghost_labels=("c1", "c2"),
            chi_vector=(1, 0),
            source_tag="manual",
        )
        assert isinstance(complex_seed, TruncatedBRSTComplex)
        assert complex_seed.source_tag == "manual"
        assert tuple(len(complex_seed.basis_by_degree[d]) for d in (0, 1, 2)) == (1, 2, 1)
        assert complex_has_nilpotent_differential(complex_seed)
        for block in differential_square_blocks(complex_seed).values():
            assert block == block.zeros(block.rows, block.cols)
        assert truncated_cohomology_dimensions(complex_seed) == {0: 0, 1: 0, 2: 0}
        assert complex_is_acyclic(complex_seed)

    def test_subregular_complex(self):
        complex_seed = sl3_subregular_truncated_brst_complex()
        assert complex_seed.source_tag == "A2_subregular_seed"
        assert complex_seed.ghost_labels == ("c_alpha1", "c_alpha1+alpha2")
        assert complex_seed.chi_vector == (1, 0)
        assert complex_seed.differentials[0].rank() == 1
        assert complex_seed.differentials[1].rank() == 1
        assert complex_has_nilpotent_differential(complex_seed)
        assert truncated_cohomology_dimensions(complex_seed) == {0: 0, 1: 0, 2: 0}

    def test_specialize_complex(self):
        symbolic = build_character_wedge_complex(
            ghost_labels=("c1", "c2"),
            chi_vector=(Symbol("x"), Symbol("y")),
            source_tag="symbolic",
        )
        specialized = specialize_complex_chi(symbolic, (1, 0), source_tag="specialized")
        assert specialized.source_tag == "specialized"
        assert specialized.chi_vector == (1, 0)
        assert truncated_cohomology_dimensions(specialized) == {0: 0, 1: 0, 2: 0}
        assert complex_is_acyclic(specialized)

        zero = specialize_complex_chi(symbolic, (0, 0), source_tag="zero")
        assert truncated_cohomology_dimensions(zero) == {0: 1, 1: 2, 2: 1}
        assert not complex_is_acyclic(zero)

    def test_quadratic_ghost_differential_on_hook_generator(self):
        source_constraints, _ = first_nonselfdual_hook_pair_constraints()
        source_support, _ = first_nonselfdual_hook_pair_quadratic_ghost_term_support()
        ghost_labels = tuple(item.c_ghost for item in source_constraints)
        d1 = quadratic_ghost_differential(ghost_labels, source_support, 1)
        source_basis = exterior_basis_indices(5, 1)
        target_basis = exterior_basis_indices(5, 2)
        col = source_basis.index((0,))
        assert d1[target_basis.index((1, 3)), col] == 1
        assert d1[target_basis.index((2, 4)), col] == 1
        assert sum(abs(d1[row, col]) for row in range(d1.rows)) == 2

    def test_build_full_ghost_brst_complex(self):
        source_constraints, _ = first_nonselfdual_hook_pair_constraints()
        source_support, _ = first_nonselfdual_hook_pair_quadratic_ghost_term_support()
        complex_seed = build_ghost_brst_complex(
            ghost_labels=tuple(item.c_ghost for item in source_constraints),
            chi_vector=(0, 1, 0, 0, 0),
            quadratic_terms=source_support,
            source_tag="hook_source_full",
        )
        assert complex_seed.quadratic_ghost_terms == source_support
        assert complex_has_nilpotent_differential(complex_seed)
        assert truncated_cohomology_dimensions(complex_seed) == {degree: 0 for degree in range(6)}
        assert complex_is_acyclic(complex_seed)

    def test_ghost_brst_differential_matches_seed_block(self):
        pair_seed = first_nonselfdual_hook_pair_ds_seed()
        d1 = ghost_brst_differential(
            pair_seed.source_complex.ghost_labels,
            pair_seed.source_complex.chi_vector,
            pair_seed.source_complex.quadratic_ghost_terms,
            1,
        )
        assert d1 == pair_seed.source_complex.differentials[1]
        assert complex_has_nilpotent_differential(pair_seed.source_complex)

    def test_first_hook_pair_relabeling_matches_target_complex(self):
        pair_seed = first_nonselfdual_hook_pair_ds_seed()
        label_map = first_nonselfdual_hook_pair_ghost_label_map()
        side_map = first_nonselfdual_hook_pair_ghost_side_map()
        relabeled_source = relabel_truncated_brst_complex(
            pair_seed.source_complex,
            label_map,
            side_map=side_map,
            source_tag=pair_seed.target_complex.source_tag,
        )
        relabeled_support = relabel_quadratic_ghost_terms(
            pair_seed.source_complex.quadratic_ghost_terms,
            label_map,
            side_map=side_map,
        )
        assert relabeled_source.ghost_labels == pair_seed.target_complex.ghost_labels
        assert relabeled_source.chi_vector == pair_seed.target_complex.chi_vector
        assert relabeled_support == pair_seed.target_complex.quadratic_ghost_terms
        assert relabeled_source.differentials == pair_seed.target_complex.differentials
        assert first_nonselfdual_hook_pair_ghost_complexes_match_under_relabeling()


class TestExactRank:
    def test_symbolic_rank(self):
        x = Symbol("x")
        assert exact_matrix_rank(Matrix([[x, 1], [0, 0]])) == 1
        assert exact_matrix_rank(Matrix([[x, 0], [0, x]])) == 2
        assert exact_matrix_rank(None) == 0


class TestLinearConstraintBlocks:
    def test_monomial_exponents(self):
        assert homogeneous_monomial_exponents(2, 0) == ((0, 0),)
        assert homogeneous_monomial_exponents(2, 1) == ((1, 0), (0, 1))
        assert homogeneous_monomial_exponents(2, 2) == ((2, 0), (1, 1), (0, 2))

    def test_block_basis(self):
        assert linear_constraint_block_basis(2, 1, 1) == (
            ((0, 0), (0,)),
            ((0, 0), (1,)),
        )
        assert linear_constraint_block_basis(2, 2, 1) == (
            ((1, 0), (0,)),
            ((1, 0), (1,)),
            ((0, 1), (0,)),
            ((0, 1), (1,)),
        )

    def test_linear_differential_degree_one(self):
        d1 = linear_constraint_koszul_differential(2, 1, 1)
        assert d1.shape == (2, 2)
        assert d1 == d1.eye(2)

    def test_manual_linear_block(self):
        block = build_linear_constraint_koszul_block(
            shifted_current_labels=("u1", "u2"),
            ghost_labels=("b1", "b2"),
            total_degree=2,
            source_tag="manual_linear",
        )
        assert isinstance(block, LinearConstraintBRSTBlock)
        assert tuple(len(block.basis_by_chain_degree[d]) for d in (0, 1, 2)) == (3, 4, 1)
        assert linear_constraint_block_has_square_zero(block)
        assert linear_constraint_block_has_contracting_homotopy(block)
        assert linear_constraint_block_is_positive_acyclic(block)
        assert chain_homology_dimensions(block) == {0: 0, 1: 0, 2: 0}

    def test_linear_contracting_homotopy_degree_one(self):
        h0 = linear_constraint_contracting_homotopy(2, 1, 0)
        assert h0.shape == (2, 2)
        assert h0 == h0.eye(2)

    def test_subregular_linear_blocks(self):
        blocks = sl3_subregular_linear_constraint_blocks(3)
        assert [block.total_degree for block in blocks] == [0, 1, 2, 3]
        assert chain_homology_dimensions(blocks[0]) == {0: 1}
        assert all(linear_constraint_block_has_square_zero(block) for block in blocks[1:])
        assert all(linear_constraint_block_has_contracting_homotopy(block) for block in blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in blocks[1:])


class TestMixedConstraintGhostBlocks:
    def test_basis_count(self):
        basis = mixed_constraint_ghost_block_basis(2, 1, 0)
        assert len(basis) == 6
        assert ((1, 0), (), ()) in basis
        assert ((0, 0), (0,), (0,)) in basis

    def test_manual_block(self):
        block = build_mixed_constraint_ghost_brst_block(
            shifted_current_labels=("u1", "u2"),
            c_ghost_labels=("c1", "c2"),
            b_ghost_labels=("b1", "b2"),
            chi_vector=(1, 0),
            quadratic_terms=(),
            constraint_total_degree=1,
            source_tag="manual_mixed",
        )
        assert isinstance(block, MixedConstraintGhostBRSTBlock)
        assert mixed_constraint_ghost_brst_differential(
            ("u1", "u2"),
            ("c1", "c2"),
            ("b1", "b2"),
            (1, 0),
            (),
            1,
            0,
        ) == block.differentials[0]
        assert mixed_constraint_ghost_block_has_square_zero(block)
        assert mixed_constraint_ghost_block_homology_dimensions(block) == {-1: 0, 0: 0, 1: 0, 2: 0}
        assert mixed_constraint_ghost_block_is_acyclic(block)

    def test_first_hook_pair_mixed_blocks(self):
        source_blocks, target_blocks = first_nonselfdual_hook_pair_mixed_constraint_ghost_blocks(2)
        assert [block.constraint_total_degree for block in source_blocks] == [0, 1, 2]
        assert [block.constraint_total_degree for block in target_blocks] == [0, 1, 2]
        assert all(mixed_constraint_ghost_block_has_square_zero(block) for block in source_blocks)
        assert all(mixed_constraint_ghost_block_has_square_zero(block) for block in target_blocks)
        assert all(mixed_constraint_ghost_block_is_acyclic(block) for block in source_blocks)
        assert all(mixed_constraint_ghost_block_is_acyclic(block) for block in target_blocks)
        assert mixed_constraint_ghost_block_homology_dimensions(source_blocks[1]) == {
            -1: 0,
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
        }
        label_map = first_nonselfdual_hook_pair_ghost_label_map()
        side_map = first_nonselfdual_hook_pair_ghost_side_map()
        relabeled_source = relabel_mixed_constraint_ghost_block(
            source_blocks[1],
            label_map,
            side_map=side_map,
            source_tag=target_blocks[1].source_tag,
        )
        assert relabeled_source.differentials == target_blocks[1].differentials
        assert first_nonselfdual_hook_pair_mixed_blocks_match_under_relabeling(2)

    def test_first_hook_pair_current_action(self):
        source_action, target_action = first_nonselfdual_hook_pair_current_action_terms()
        assert all(isinstance(item, CurrentActionTermEntry) for item in source_action)
        assert all(isinstance(item, CurrentActionTermEntry) for item in target_action)
        assert [
            (item.c_ghost, item.source_root_label, item.target_root_label, item.coefficient)
            for item in source_action
        ] == [
            ("c_source_E12", "E23", "E13", 1),
            ("c_source_E23", "E12", "E13", -1),
            ("c_source_E14", "E43", "E13", 1),
            ("c_source_E43", "E14", "E13", -1),
        ]
        assert [
            (item.c_ghost, item.source_root_label, item.target_root_label, item.coefficient)
            for item in target_action
        ] == [
            ("c_target_E13", "E32", "E12", 1),
            ("c_target_E32", "E13", "E12", -1),
            ("c_target_E14", "E42", "E12", 1),
            ("c_target_E42", "E14", "E12", -1),
        ]

    def test_current_action_differential_on_hook_pair(self):
        source_constraints, _ = first_nonselfdual_hook_pair_constraints()
        source_action, _ = first_nonselfdual_hook_pair_current_action_terms()
        shifted = tuple(f"u_source_{item.root_label}" for item in source_constraints)
        c_ghosts = tuple(item.c_ghost for item in source_constraints)
        b_ghosts = tuple(item.b_ghost for item in source_constraints)
        d = current_action_differential(
            shifted,
            c_ghosts,
            b_ghosts,
            source_action,
            1,
            0,
        )
        source_basis = mixed_constraint_ghost_block_basis(5, 1, 0)
        target_basis = mixed_constraint_ghost_block_basis(5, 1, 1)
        assert d[target_basis.index(((1, 0, 0, 0, 0), (1,), ())), source_basis.index(((0, 0, 0, 1, 0), (), ()))] == 1
        assert d[target_basis.index(((1, 0, 0, 0, 0), (3,), ())), source_basis.index(((0, 1, 0, 0, 0), (), ()))] == -1

    def test_first_hook_pair_nonlinear_mixed_blocks(self):
        linear_source, linear_target = first_nonselfdual_hook_pair_mixed_constraint_ghost_blocks(2)
        nonlinear_source, nonlinear_target = first_nonselfdual_hook_pair_nonlinear_mixed_constraint_ghost_blocks(2)
        assert [block.constraint_total_degree for block in nonlinear_source] == [0, 1, 2]
        assert [block.constraint_total_degree for block in nonlinear_target] == [0, 1, 2]
        assert all(mixed_constraint_ghost_block_has_square_zero(block) for block in nonlinear_source)
        assert all(mixed_constraint_ghost_block_has_square_zero(block) for block in nonlinear_target)
        assert all(mixed_constraint_ghost_block_is_acyclic(block) for block in nonlinear_source)
        assert all(mixed_constraint_ghost_block_is_acyclic(block) for block in nonlinear_target)
        assert nonlinear_source[1].current_action_terms == first_nonselfdual_hook_pair_current_action_terms()[0]
        assert nonlinear_target[1].current_action_terms == first_nonselfdual_hook_pair_current_action_terms()[1]
        assert any(
            nonlinear_source[1].differentials[degree] != linear_source[1].differentials[degree]
            for degree in nonlinear_source[1].differentials
        )
        assert any(
            nonlinear_target[1].differentials[degree] != linear_target[1].differentials[degree]
            for degree in nonlinear_target[1].differentials
        )
        label_map = first_nonselfdual_hook_pair_ghost_label_map()
        side_map = first_nonselfdual_hook_pair_ghost_side_map()
        relabeled_action = relabel_current_action_terms(
            nonlinear_source[1].current_action_terms,
            label_map,
            side_map=side_map,
        )
        relabeled_source = relabel_mixed_constraint_ghost_block(
            nonlinear_source[1],
            label_map,
            side_map=side_map,
            source_tag=nonlinear_target[1].source_tag,
        )
        assert relabeled_action == nonlinear_target[1].current_action_terms
        assert relabeled_source.differentials == nonlinear_target[1].differentials
        assert first_nonselfdual_hook_pair_nonlinear_blocks_match_under_relabeling(2)

    def test_subregular_mixed_blocks(self):
        blocks = sl3_subregular_mixed_constraint_ghost_blocks(3)
        assert [block.constraint_total_degree for block in blocks] == [0, 1, 2, 3]
        assert all(mixed_constraint_ghost_block_has_square_zero(block) for block in blocks)
        assert all(mixed_constraint_ghost_block_is_acyclic(block) for block in blocks)
        assert mixed_constraint_ghost_block_homology_dimensions(blocks[0]) == {0: 0, 1: 0, 2: 0}

    def test_subregular_nonlinear_mixed_blocks(self):
        linear_blocks = sl3_subregular_mixed_constraint_ghost_blocks(3)
        nonlinear_blocks = sl3_subregular_nonlinear_mixed_constraint_ghost_blocks(3)
        assert [block.constraint_total_degree for block in nonlinear_blocks] == [0, 1, 2, 3]
        assert all(mixed_constraint_ghost_block_has_square_zero(block) for block in nonlinear_blocks)
        assert all(mixed_constraint_ghost_block_is_acyclic(block) for block in nonlinear_blocks)
        assert all(block.current_action_terms == () for block in nonlinear_blocks)
        assert [
            mixed_constraint_ghost_block_homology_dimensions(block) for block in nonlinear_blocks
        ] == [
            mixed_constraint_ghost_block_homology_dimensions(block) for block in linear_blocks
        ]


class TestSurvivorCoupledBlocks:
    def test_basis_count(self):
        basis = survivor_coupled_block_basis(2, 3, 1, 1, 0)
        assert len(basis) == 18
        assert ((1, 0), (1, 0, 0), (), ()) in basis
        assert ((0, 0), (0, 1, 0), (0,), (0,)) in basis

    def test_subregular_survivor_action(self):
        action = sl3_subregular_survivor_action_terms()
        assert all(isinstance(item, SurvivorActionTermEntry) for item in action)
        assert [
            (item.c_ghost, item.source_survivor_label, item.target_survivor_label, item.coefficient)
            for item in action
        ] == [
            ("c_alpha1+alpha2", "G-", "J", 1),
            ("c_alpha1+alpha2", "T", "G+", -1),
        ]

    def test_subregular_survivor_coupled_blocks(self):
        blocks = sl3_subregular_survivor_coupled_blocks(2, 1)
        assert all(isinstance(block, SurvivorCoupledBRSTBlock) for block in blocks)
        assert [block.constraint_total_degree for block in blocks] == [0, 1, 2]
        assert all(block.survivor_total_degree == 1 for block in blocks)
        assert all(survivor_coupled_block_has_square_zero(block) for block in blocks)
        assert all(survivor_coupled_block_is_acyclic(block) for block in blocks)
        assert survivor_coupled_block_homology_dimensions(blocks[1]) == {
            -1: 0,
            0: 0,
            1: 0,
            2: 0,
        }

    def test_first_hook_pair_survivor_action(self):
        source_action, target_action = first_nonselfdual_hook_pair_survivor_action_terms()
        assert len(source_action) == 6
        assert len(target_action) == 14
        assert source_action[0] == SurvivorActionTermEntry(
            c_ghost="c_source_E12",
            source_survivor_label="source_gm4_1",
            target_survivor_label="source_gm2_1",
            coefficient=Rational(-1, 2),
        )
        assert target_action[-1] == SurvivorActionTermEntry(
            c_ghost="c_target_E42",
            source_survivor_label="target_gm2_1",
            target_survivor_label="target_gm1_4",
            coefficient=1,
        )

    def test_survivor_action_differential_on_subregular(self):
        constraints = sl3_subregular_constraints()
        survivors = sl3_subregular_strong_generator_candidates()
        action = sl3_subregular_survivor_action_terms()
        d = survivor_action_differential(
            tuple(item.label for item in survivors),
            tuple(item.c_ghost for item in constraints),
            tuple(item.b_ghost for item in constraints),
            action,
            0,
            1,
            0,
        )
        source_basis = survivor_coupled_block_basis(2, 4, 0, 1, 0)
        target_basis = survivor_coupled_block_basis(2, 4, 0, 1, 1)
        assert d[target_basis.index(((0, 0), (1, 0, 0, 0), (1,), ())), source_basis.index(((0, 0), (0, 0, 1, 0), (), ()))] == 1
        assert d[target_basis.index(((0, 0), (0, 1, 0, 0), (1,), ())), source_basis.index(((0, 0), (0, 0, 0, 1), (), ()))] == -1

    def test_first_hook_pair_survivor_coupled_blocks(self):
        source_blocks, target_blocks = first_nonselfdual_hook_pair_survivor_coupled_blocks(1, 1)
        assert [block.constraint_total_degree for block in source_blocks] == [0, 1]
        assert [block.constraint_total_degree for block in target_blocks] == [0, 1]
        assert all(survivor_coupled_block_has_square_zero(block) for block in source_blocks)
        assert all(survivor_coupled_block_has_square_zero(block) for block in target_blocks)
        assert all(survivor_coupled_block_is_acyclic(block) for block in source_blocks)
        assert all(survivor_coupled_block_is_acyclic(block) for block in target_blocks)
        assert survivor_coupled_block_homology_dimensions(source_blocks[1]) == {
            -1: 0,
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
        }
        assert survivor_coupled_block_homology_dimensions(target_blocks[1]) == {
            -1: 0,
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
        }


class TestInternalSurvivorCEBlocks:
    def test_basis_count(self):
        basis = internal_survivor_ce_block_basis(4, 1, 1)
        assert len(basis) == 16
        assert ((1, 0, 0, 0), (0,)) in basis
        assert ((0, 0, 1, 0), (3,)) in basis

    def test_subregular_internal_terms(self):
        survivor_labels = tuple(
            item.label for item in sl3_subregular_strong_generator_candidates()
        )
        ghost_labels, _ = internal_survivor_ghost_labels(survivor_labels)
        brackets = sl3_subregular_projected_strong_brackets()
        assert ghost_labels == (
            "c_survivor_J",
            "c_survivor_G+",
            "c_survivor_G-",
            "c_survivor_T",
        )
        assert internal_survivor_quadratic_ghost_terms(survivor_labels, brackets) == (
            QuadraticGhostTermEntry(
                left_c_ghost="c_survivor_J",
                right_c_ghost="c_survivor_G+",
                target_b_ghost="b_survivor_G+",
                coefficient=Rational(3, 2),
            ),
            QuadraticGhostTermEntry(
                left_c_ghost="c_survivor_J",
                right_c_ghost="c_survivor_G-",
                target_b_ghost="b_survivor_G-",
                coefficient=Rational(-3, 2),
            ),
            QuadraticGhostTermEntry(
                left_c_ghost="c_survivor_G+",
                right_c_ghost="c_survivor_G-",
                target_b_ghost="b_survivor_T",
                coefficient=1,
            ),
        )
        assert internal_survivor_action_terms(survivor_labels, brackets) == (
            SurvivorActionTermEntry("c_survivor_J", "G+", "G+", Rational(3, 2)),
            SurvivorActionTermEntry("c_survivor_J", "G-", "G-", Rational(-3, 2)),
            SurvivorActionTermEntry("c_survivor_G+", "J", "G+", Rational(-3, 2)),
            SurvivorActionTermEntry("c_survivor_G+", "G-", "T", 1),
            SurvivorActionTermEntry("c_survivor_G-", "J", "G-", Rational(3, 2)),
            SurvivorActionTermEntry("c_survivor_G-", "G+", "T", -1),
        )

    def test_subregular_internal_ce_differential(self):
        survivor_labels = tuple(
            item.label for item in sl3_subregular_strong_generator_candidates()
        )
        c_ghosts, _ = internal_survivor_ghost_labels(survivor_labels)
        brackets = sl3_subregular_projected_strong_brackets()
        d = internal_survivor_ce_differential(
            survivor_labels,
            c_ghosts,
            internal_survivor_quadratic_ghost_terms(survivor_labels, brackets),
            internal_survivor_action_terms(survivor_labels, brackets),
            1,
            0,
        )
        source_basis = internal_survivor_ce_block_basis(4, 1, 0)
        target_basis = internal_survivor_ce_block_basis(4, 1, 1)
        assert d[
            target_basis.index(((0, 1, 0, 0), (0,))),
            source_basis.index(((0, 1, 0, 0), ())),
        ] == Rational(-3, 2)
        assert d[
            target_basis.index(((0, 0, 0, 1), (2,))),
            source_basis.index(((0, 1, 0, 0), ())),
        ] == 1

    def test_subregular_internal_survivor_ce_blocks(self):
        blocks = sl3_subregular_internal_survivor_ce_blocks(2)
        assert all(isinstance(block, InternalSurvivorCEBlock) for block in blocks)
        assert [block.survivor_polynomial_degree for block in blocks] == [0, 1, 2]
        assert all(internal_survivor_ce_block_has_square_zero(block) for block in blocks)
        assert not all(internal_survivor_ce_block_is_acyclic(block) for block in blocks)
        assert internal_survivor_ce_block_homology_dimensions(blocks[0]) == {
            0: 1,
            1: 1,
            2: 0,
            3: 1,
            4: 1,
        }
        assert internal_survivor_ce_block_homology_dimensions(blocks[1]) == {
            0: 1,
            1: 2,
            2: 2,
            3: 2,
            4: 1,
        }
        assert internal_survivor_ce_block_homology_dimensions(blocks[2]) == {
            0: 2,
            1: 3,
            2: 2,
            3: 3,
            4: 2,
        }

    def test_first_hook_pair_internal_survivor_ce_blocks(self):
        source_blocks, target_blocks = first_nonselfdual_hook_pair_internal_survivor_ce_blocks(1)
        assert [block.survivor_polynomial_degree for block in source_blocks] == [0, 1]
        assert [block.survivor_polynomial_degree for block in target_blocks] == [0, 1]
        assert all(internal_survivor_ce_block_has_square_zero(block) for block in source_blocks)
        assert all(internal_survivor_ce_block_has_square_zero(block) for block in target_blocks)
        assert internal_survivor_ce_block_homology_dimensions(source_blocks[0]) == {
            0: 1,
            1: 2,
            2: 1,
            3: 1,
            4: 2,
            5: 1,
        }
        assert internal_survivor_ce_block_homology_dimensions(source_blocks[1]) == {
            0: 2,
            1: 5,
            2: 5,
            3: 5,
            4: 5,
            5: 2,
        }
        assert internal_survivor_ce_block_homology_dimensions(target_blocks[0]) == {
            0: 1,
            1: 1,
            2: 0,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 0,
            8: 1,
            9: 1,
        }
        assert internal_survivor_ce_block_homology_dimensions(target_blocks[1]) == {
            0: 1,
            1: 2,
            2: 2,
            3: 2,
            4: 2,
            5: 3,
            6: 2,
            7: 0,
            8: 1,
            9: 1,
        }


class TestFirstNonSelfDualHookPair:
    def test_pair_seed(self):
        k = Symbol("k")
        pair_seed = first_nonselfdual_hook_pair_ds_seed(k)
        assert isinstance(pair_seed, HookPairDSComplexSeed)
        assert pair_seed.n == 4
        assert pair_seed.r == 1
        assert pair_seed.source_partition == (3, 1)
        assert pair_seed.target_partition == (2, 1, 1)
        assert simplify(pair_seed.target_level - (-k - 8)) == 0
        assert pair_seed.track == "frontier_nonprincipal_ds_orbit"
        assert len(pair_seed.source_complex.ghost_labels) == 5
        assert len(pair_seed.target_complex.ghost_labels) == 5
        assert pair_seed.source_complex.chi_vector == (0, 1, 0, 0, 0)
        assert pair_seed.target_complex.chi_vector == (0, 1, 0, 0, 0)
        assert len(pair_seed.source_complex.quadratic_ghost_terms) == 2
        assert len(pair_seed.target_complex.quadratic_ghost_terms) == 2
        assert complex_has_nilpotent_differential(pair_seed.source_complex)
        assert complex_has_nilpotent_differential(pair_seed.target_complex)
        assert truncated_cohomology_dimensions(pair_seed.source_complex) == {
            degree: 0 for degree in range(6)
        }
        assert truncated_cohomology_dimensions(pair_seed.target_complex) == {
            degree: 0 for degree in range(6)
        }

    def test_pair_specialization(self):
        source, target = first_nonselfdual_hook_pair_specialized_complexes(
            source_chi=(0, 1, 0, 0, 0),
            target_chi=(0, 1, 0, 0, 0),
        )
        assert source.chi_vector == (0, 1, 0, 0, 0)
        assert target.chi_vector == (0, 1, 0, 0, 0)
        assert truncated_cohomology_dimensions(source) == {degree: 0 for degree in range(6)}
        assert truncated_cohomology_dimensions(target) == {degree: 0 for degree in range(6)}
        assert complex_is_acyclic(source)
        assert complex_is_acyclic(target)

    def test_pair_ghost_profiles(self):
        source_profile, target_profile = first_nonselfdual_hook_pair_ghost_profiles()
        assert len(source_profile) == 5
        assert len(target_profile) == 5
        assert source_profile[0].root_label == "E13"
        assert source_profile[0].b_weight == 3
        assert source_profile[0].c_weight == -2
        assert target_profile[0].root_label == "E12"
        assert target_profile[0].b_weight == 2
        assert target_profile[1].b_weight == Rational(3, 2)

    def test_pair_constraint_characters_and_constraints(self):
        source_character, target_character = first_nonselfdual_hook_pair_constraint_characters()
        source_constraints, target_constraints = first_nonselfdual_hook_pair_constraints()
        assert source_character == {"E13": 0, "E12": 1, "E14": 0, "E23": 0, "E43": 0}
        assert target_character == {"E12": 0, "E13": 1, "E14": 0, "E32": 0, "E42": 0}
        assert [item.root_label for item in source_constraints] == ["E13", "E12", "E14", "E23", "E43"]
        assert [item.root_label for item in target_constraints] == ["E12", "E13", "E14", "E32", "E42"]
        assert source_constraints[0].character_value == 0
        assert source_constraints[1].character_value == 1
        assert target_constraints[0].character_value == 0
        assert target_constraints[1].character_value == 1

    def test_pair_positive_nilpotent_brackets(self):
        source_brackets, target_brackets = first_nonselfdual_hook_pair_positive_nilpotent_brackets()
        assert source_brackets == (("E12", "E23", "E13"), ("E14", "E43", "E13"))
        assert target_brackets == (("E13", "E32", "E12"), ("E14", "E42", "E12"))

    def test_pair_quadratic_ghost_term_support(self):
        source_support, target_support = first_nonselfdual_hook_pair_quadratic_ghost_term_support()
        assert all(isinstance(item, QuadraticGhostTermEntry) for item in source_support)
        assert all(isinstance(item, QuadraticGhostTermEntry) for item in target_support)
        assert [
            (item.left_c_ghost, item.right_c_ghost, item.target_b_ghost, item.coefficient)
            for item in source_support
        ] == [
            ("c_source_E12", "c_source_E23", "b_source_E13", 1),
            ("c_source_E14", "c_source_E43", "b_source_E13", 1),
        ]
        assert [
            (item.left_c_ghost, item.right_c_ghost, item.target_b_ghost, item.coefficient)
            for item in target_support
        ] == [
            ("c_target_E13", "c_target_E32", "b_target_E12", 1),
            ("c_target_E14", "c_target_E42", "b_target_E12", 1),
        ]

    def test_pair_basis_profiles_and_blueprints(self):
        source_basis, target_basis = first_nonselfdual_hook_pair_basis_profiles()
        source_blueprint, target_blueprint = first_nonselfdual_hook_pair_brst_blueprints()
        assert len(source_basis) == 15
        assert len(target_basis) == 15
        assert not source_blueprint.positive_nilpotent_is_abelian
        assert not target_blueprint.positive_nilpotent_is_abelian
        assert source_blueprint.quadratic_ghost_term_present
        assert target_blueprint.quadratic_ghost_term_present
        assert len(source_blueprint.expected_strong_presentation) == 5
        assert len(target_blueprint.expected_strong_presentation) == 9

    def test_pair_surviving_field_candidates(self):
        source_candidates, target_candidates = first_nonselfdual_hook_pair_surviving_field_candidates()
        assert [candidate.conformal_weight for candidate in source_candidates] == [1, 2, 2, 2, 3]
        assert [candidate.conformal_weight for candidate in target_candidates] == [
            1,
            1,
            1,
            1,
            Rational(3, 2),
            Rational(3, 2),
            Rational(3, 2),
            Rational(3, 2),
            2,
        ]

    def test_pair_reduced_brackets(self):
        source_brackets, target_brackets = first_nonselfdual_hook_pair_reduced_brackets()
        assert source_brackets[("source_gm2_2", "source_gm2_3")] == {"source_gm4_1": 1}
        assert source_brackets[("source_g0_1", "source_gm2_2")] == {"source_gm2_2": Rational(4, 3)}
        assert target_brackets[("target_gm1_1", "target_gm1_3")] == {"target_gm2_1": 1}
        assert target_brackets[("target_g0_1", "target_g0_2")] == {"target_g0_4": 1}

    def test_pair_linear_blocks(self):
        source_blocks, target_blocks = first_nonselfdual_hook_pair_linear_constraint_blocks(3)
        assert [block.total_degree for block in source_blocks] == [0, 1, 2, 3]
        assert [block.total_degree for block in target_blocks] == [0, 1, 2, 3]
        assert len(source_blocks[0].ghost_labels) == 5
        assert len(target_blocks[0].ghost_labels) == 5
        assert chain_homology_dimensions(source_blocks[0]) == {0: 1}
        assert chain_homology_dimensions(target_blocks[0]) == {0: 1}
        assert all(linear_constraint_block_has_contracting_homotopy(block) for block in source_blocks[1:])
        assert all(linear_constraint_block_has_contracting_homotopy(block) for block in target_blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in source_blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in target_blocks[1:])


class TestHookFamilyCatalog:
    def test_generic_seed(self):
        k = Symbol("k")
        seed = hook_pair_ds_seed(
            6,
            2,
            level=k,
            source_num_constraints=3,
            target_num_constraints=2,
        )
        assert seed.source_partition == (4, 1, 1)
        assert seed.target_partition == (3, 1, 1, 1)
        assert len(seed.source_complex.ghost_labels) == 3
        assert len(seed.target_complex.ghost_labels) == 2
        assert all(label.startswith("c_source_E") for label in seed.source_complex.ghost_labels)
        assert all(label.startswith("c_target_E") for label in seed.target_complex.ghost_labels)
        assert simplify(seed.target_level - (-k - 12)) == 0
        assert complex_has_nilpotent_differential(seed.source_complex)
        assert complex_has_nilpotent_differential(seed.target_complex)

    def test_generic_seed_uses_ansatz_by_default(self):
        seed = hook_pair_ds_seed(7, 2)
        assert len(seed.source_complex.ghost_labels) == 4
        assert len(seed.target_complex.ghost_labels) == 2

    def test_generic_specialization_defaults(self):
        source, target = hook_pair_specialized_complexes(
            6,
            2,
        )
        assert source.chi_vector == (1, 0, 0)
        assert target.chi_vector == (1, 0)
        assert complex_is_acyclic(source)
        assert complex_is_acyclic(target)

    def test_generic_linear_blocks(self):
        source_blocks, target_blocks = hook_pair_linear_constraint_blocks(
            6,
            2,
            max_total_degree=3,
            num_constraints=3,
        )
        assert chain_homology_dimensions(source_blocks[0]) == {0: 1}
        assert chain_homology_dimensions(target_blocks[0]) == {0: 1}
        assert all(linear_constraint_block_has_square_zero(block) for block in source_blocks[1:])
        assert all(linear_constraint_block_has_square_zero(block) for block in target_blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in source_blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in target_blocks[1:])

    def test_generic_linear_blocks_default_ansatz(self):
        source_blocks, target_blocks = hook_pair_linear_constraint_blocks(
            6,
            2,
            max_total_degree=2,
        )
        assert len(source_blocks[0].ghost_labels) == 3
        assert len(target_blocks[0].ghost_labels) == 2

    def test_generic_constraint_data_and_nonlinearity(self):
        source_constraints, target_constraints = hook_pair_constraints(6, 2)
        source_character, target_character = hook_pair_constraint_characters(6, 2)
        source_brackets, target_brackets = hook_pair_positive_nilpotent_brackets(6, 2)
        source_quadratic, target_quadratic = hook_pair_quadratic_ghost_term_support(6, 2)
        source_action, target_action = hook_pair_current_action_terms(6, 2)

        assert len(source_constraints) == 3
        assert len(target_constraints) == 2
        assert sum(source_character.values()) == 1
        assert sum(target_character.values()) == 1
        assert source_brackets == ()
        assert target_brackets == ()
        assert len(source_quadratic) == len(source_brackets)
        assert len(target_quadratic) == len(target_brackets)
        assert len(source_action) == 2 * len(source_brackets)
        assert len(target_action) == 2 * len(target_brackets)

        source_profile, target_profile = hook_pair_ghost_profiles(6, 2)
        full_source_brackets, full_target_brackets = hook_pair_positive_nilpotent_brackets(
            6,
            2,
            source_num_constraints=len(source_profile),
            target_num_constraints=len(target_profile),
        )
        full_source_action, full_target_action = hook_pair_current_action_terms(
            6,
            2,
            source_num_constraints=len(source_profile),
            target_num_constraints=len(target_profile),
        )
        assert full_source_brackets
        assert full_target_brackets
        assert len(full_source_action) == 2 * len(full_source_brackets)
        assert len(full_target_action) == 2 * len(full_target_brackets)

    def test_generic_mixed_and_nonlinear_blocks(self):
        source_blocks, target_blocks = hook_pair_mixed_constraint_ghost_blocks(
            6,
            2,
            max_constraint_total_degree=2,
        )
        nonlinear_source, nonlinear_target = hook_pair_nonlinear_mixed_constraint_ghost_blocks(
            6,
            2,
            max_constraint_total_degree=2,
        )
        assert [block.constraint_total_degree for block in source_blocks] == [0, 1, 2]
        assert [block.constraint_total_degree for block in target_blocks] == [0, 1, 2]
        assert len(source_blocks[0].c_ghost_labels) == 3
        assert len(target_blocks[0].c_ghost_labels) == 2
        assert len(nonlinear_source[1].current_action_terms) >= len(source_blocks[1].current_action_terms)
        assert all(
            mixed_constraint_ghost_block_has_square_zero(block)
            for block in source_blocks + target_blocks + nonlinear_source + nonlinear_target
        )
        assert all(
            mixed_constraint_ghost_block_is_acyclic(block)
            for block in source_blocks + target_blocks + nonlinear_source + nonlinear_target
        )

    def test_generic_dual_swap_block_symmetry(self):
        assert hook_pair_mixed_blocks_match_under_dual_swap(6, 2, max_constraint_total_degree=1)
        assert hook_pair_nonlinear_blocks_match_under_dual_swap(6, 2, max_constraint_total_degree=1)
        assert all(
            verify_hook_pair_mixed_block_duality_catalog(
                max_n=7,
                max_constraint_total_degree=1,
            ).values()
        )
        assert all(
            verify_hook_pair_nonlinear_block_duality_catalog(
                max_n=7,
                max_constraint_total_degree=1,
            ).values()
        )

    def test_generic_survivor_family_scaffold(self):
        source_candidates, target_candidates = hook_pair_surviving_field_candidates(5, 2)
        source_brackets, target_brackets = hook_pair_reduced_brackets(5, 2)
        assert len(source_candidates) == centralizer_dimension_sl_n((3, 1, 1))
        assert len(target_candidates) == centralizer_dimension_sl_n((3, 1, 1))
        assert source_brackets
        assert target_brackets

    def test_catalog(self):
        seeds = hook_pair_ds_seed_catalog(max_n=5)
        assert len(seeds) == 6
        assert seeds[0].source_partition == (2, 1)
        assert seeds[-1].source_partition == (2, 1, 1, 1)
        assert len(seeds[0].source_complex.ghost_labels) == 2
        assert len(seeds[-1].source_complex.ghost_labels) == 1

    def test_catalog_verification(self):
        assert all(verify_hook_pair_ds_seed_catalog(max_n=8).values())
        assert all(verify_hook_pair_seed_alignment(max_n=8).values())


class TestVerificationBundle:
    def test_all_checks(self):
        assert all(verify_ds_reduction_seed().values())
