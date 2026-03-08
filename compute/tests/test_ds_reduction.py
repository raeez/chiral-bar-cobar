"""Tests for DS reduction seed scaffold."""

from collections import Counter

from sympy import Matrix, Rational, Symbol, simplify, zeros

from compute.lib.nonprincipal_ds_reduction import bp_strong_presentation

from compute.lib.ds_reduction import (
    DSBRSTBlueprint,
    DSBasisElement,
    DSReducedFieldCandidate,
    DSReductionSeed,
    DSConstraint,
    HookPairDSComplexSeed,
    LinearConstraintBRSTBlock,
    STATUS_DS_SEED,
    TruncatedBRSTComplex,
    build_character_wedge_complex,
    build_linear_constraint_koszul_block,
    character_wedge_differential,
    chain_homology_dimensions,
    complex_has_nilpotent_differential,
    complex_is_acyclic,
    ds_basis_expression_matrix,
    differential_square_blocks,
    exterior_basis_indices,
    first_nonselfdual_hook_pair_ds_seed,
    hook_pair_ds_seed,
    hook_pair_ds_seed_catalog,
    hook_pair_linear_constraint_blocks,
    hook_pair_specialized_complexes,
    first_nonselfdual_hook_pair_linear_constraint_blocks,
    first_nonselfdual_hook_pair_ghost_profiles,
    first_nonselfdual_hook_pair_specialized_complexes,
    brst_ghost_weights,
    homogeneous_monomial_exponents,
    linear_constraint_block_basis,
    linear_constraint_block_has_contracting_homotopy,
    linear_constraint_block_has_square_zero,
    linear_constraint_block_is_positive_acyclic,
    linear_constraint_contracting_homotopy,
    linear_constraint_koszul_differential,
    matrix_commutator,
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
    sl3_subregular_positive_nilpotent_brackets,
    sl3_subregular_positive_grades,
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
        assert complex_has_nilpotent_differential(pair_seed.source_complex)
        assert complex_has_nilpotent_differential(pair_seed.target_complex)

    def test_pair_specialization(self):
        source, target = first_nonselfdual_hook_pair_specialized_complexes(
            source_chi=(1, 0, 0, 0, 0),
            target_chi=(1, 0, 0, 0, 0),
        )
        assert source.chi_vector == (1, 0, 0, 0, 0)
        assert target.chi_vector == (1, 0, 0, 0, 0)
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
        assert seed.source_complex.ghost_labels == ("c_source_1", "c_source_2", "c_source_3")
        assert seed.target_complex.ghost_labels == ("c_target_1", "c_target_2")
        assert simplify(seed.target_level - (-k - 12)) == 0
        assert complex_has_nilpotent_differential(seed.source_complex)
        assert complex_has_nilpotent_differential(seed.target_complex)

    def test_generic_specialization_defaults(self):
        source, target = hook_pair_specialized_complexes(
            6,
            2,
            source_num_constraints=3,
            target_num_constraints=3,
        )
        assert source.chi_vector == (1, 0, 0)
        assert target.chi_vector == (1, 0, 0)
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

    def test_catalog(self):
        seeds = hook_pair_ds_seed_catalog(max_n=5)
        assert len(seeds) == 6
        assert seeds[0].source_partition == (2, 1)
        assert seeds[-1].source_partition == (2, 1, 1, 1)

    def test_catalog_verification(self):
        assert all(verify_hook_pair_ds_seed_catalog(max_n=8).values())
        assert all(verify_hook_pair_seed_alignment(max_n=8).values())


class TestVerificationBundle:
    def test_all_checks(self):
        assert all(verify_ds_reduction_seed().values())
