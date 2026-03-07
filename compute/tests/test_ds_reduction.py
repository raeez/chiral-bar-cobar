"""Tests for DS reduction seed scaffold."""

from collections import Counter

from sympy import Rational, Symbol, simplify

from compute.lib.ds_reduction import (
    DSBRSTBlueprint,
    DSBasisElement,
    DSReductionSeed,
    DSConstraint,
    HookPairDSComplexSeed,
    STATUS_DS_SEED,
    TruncatedBRSTComplex,
    build_character_wedge_complex,
    character_wedge_differential,
    complex_has_nilpotent_differential,
    differential_square_blocks,
    exterior_basis_indices,
    first_nonselfdual_hook_pair_ds_seed,
    brst_ghost_weights,
    sl3_subregular_basis_grades,
    sl3_subregular_basis_profile,
    sl3_subregular_brst_blueprint,
    sl3_subregular_constraint_character,
    sl3_subregular_constraints,
    sl3_subregular_ds_seed,
    sl3_subregular_ghost_profile,
    sl3_subregular_positive_nilpotent_brackets,
    sl3_subregular_positive_grades,
    sl3_subregular_sl2_triple,
    sl3_subregular_truncated_brst_complex,
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

    def test_subregular_complex(self):
        complex_seed = sl3_subregular_truncated_brst_complex()
        assert complex_seed.source_tag == "A2_subregular_seed"
        assert complex_seed.ghost_labels == ("c_alpha1", "c_alpha1+alpha2")
        assert complex_seed.chi_vector == (1, 0)
        assert complex_seed.differentials[0].rank() == 1
        assert complex_seed.differentials[1].rank() == 1
        assert complex_has_nilpotent_differential(complex_seed)


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
        assert complex_has_nilpotent_differential(pair_seed.source_complex)
        assert complex_has_nilpotent_differential(pair_seed.target_complex)


class TestVerificationBundle:
    def test_all_checks(self):
        assert all(verify_ds_reduction_seed().values())
