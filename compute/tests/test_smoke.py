"""Cross-module smoke tests.

Verify that every public function in compute.lib can be called
with minimal valid inputs and produces non-trivial results.
"""

import pytest
from sympy import zeros


class TestCoreTypes:
    def test_graded_vector_space(self):
        from compute.lib import GradedVectorSpace
        V = GradedVectorSpace({0: 1, 1: 3, 2: 5})
        assert V.dim(0) == 1
        assert V.dim(1) == 3

    def test_chain_complex(self):
        from compute.lib import GradedVectorSpace, ChainComplex
        spaces = GradedVectorSpace({0: 1, 1: 3, 2: 5})
        cc = ChainComplex(spaces)
        assert cc.spaces.dim(1) == 3

    def test_ope_algebra(self):
        from compute.lib import OPEAlgebra, Generator
        T = Generator("T", 2, 0)
        alg = OPEAlgebra([T], {}, name="test")
        assert len(alg.generators) == 1


class TestAlgebraConstructors:
    def test_heisenberg(self):
        from compute.lib import heisenberg_algebra
        H = heisenberg_algebra()
        assert len(H.generators) == 1

    def test_sl2(self):
        from compute.lib import sl2_algebra
        g = sl2_algebra()
        assert len(g.generators) == 3

    def test_virasoro(self):
        from compute.lib import virasoro_algebra
        V = virasoro_algebra()
        assert len(V.generators) == 1

    def test_free_fermion(self):
        from compute.lib import free_fermion_algebra
        F = free_fermion_algebra()
        assert len(F.generators) >= 1


class TestLieAlgebra:
    def test_cartan_data(self):
        from compute.lib import cartan_data
        cd = cartan_data("A", 1)
        assert cd.dim == 3
        assert cd.h_dual == 2

    def test_sugawara_c(self):
        from compute.lib import sugawara_c
        from sympy import Symbol
        k = Symbol('k')
        c = sugawara_c("A", 1, k)
        assert c.subs(k, 1) == 1

    def test_ff_dual_level(self):
        from compute.lib import ff_dual_level
        from sympy import Symbol, simplify
        k = Symbol('k')
        kp = ff_dual_level("A", 1, k)
        assert simplify(kp - (-k - 4)) == 0

    def test_kappa_km(self):
        from compute.lib import kappa_km
        from sympy import Symbol
        k = Symbol('k')
        kap = kappa_km("A", 1, k)
        assert kap is not None


class TestRegistries:
    def test_algebra_registry(self):
        from compute.lib import ALGEBRA_REGISTRY
        assert len(ALGEBRA_REGISTRY) == 11

    def test_known_bar_dims(self):
        from compute.lib import KNOWN_BAR_DIMS
        assert "sl2" in KNOWN_BAR_DIMS
        assert KNOWN_BAR_DIMS["sl2"][1] == 3

    def test_verify_bar_dim(self):
        from compute.lib import verify_bar_dim
        ok, msg = verify_bar_dim("sl2", 1, 3)
        assert ok


class TestKoszulHilbert:
    def test_riordan(self):
        from compute.lib import riordan
        # R(0)=1, R(1)=0, R(2)=1, R(3)=1, R(4)=3, R(5)=6
        assert riordan(4) == 3
        assert riordan(5) == 6
        assert riordan(6) == 15

    def test_motzkin(self):
        from compute.lib import motzkin
        assert motzkin(0) == 1
        assert motzkin(3) == 4
        assert motzkin(4) == 9

    def test_verify_koszul_sym_ext(self):
        from compute.lib import verify_koszul
        from math import comb
        h_sym = [comb(k + 2, k) for k in range(5)]
        h_ext = [comb(3, k) for k in range(4)] + [0]
        assert verify_koszul(h_sym, h_ext)


class TestOrlikSolomon:
    def test_os_dimension(self):
        from compute.lib import os_dimension
        assert os_dimension(2, 1) == 1
        assert os_dimension(3, 2) == 2

    def test_os_basis(self):
        from compute.lib import os_basis
        b = os_basis(3, 2)
        assert len(b) == 2

    def test_residue_map(self):
        from compute.lib import residue_map
        r = residue_map(3, 2, 0, 1)
        assert r is not None


class TestUtilities:
    def test_partition_number(self):
        from compute.lib import partition_number
        assert partition_number(0) == 1
        assert partition_number(5) == 7

    def test_lambda_fp(self):
        from compute.lib import lambda_fp
        from fractions import Fraction
        lam1 = lambda_fp(1)
        assert lam1 == Fraction(1, 24)

    def test_F_g(self):
        from compute.lib import F_g
        from fractions import Fraction
        f1 = F_g(1, 1)
        assert f1 == Fraction(1, 24)


class TestInfiniteGeneratorFrontier:
    def test_pronilpotent_completion_exports(self):
        from compute.lib import (
            w_infinity_weight_sector,
            verify_w_infinity_completion,
        )
        assert (2, 2) in w_infinity_weight_sector(4)[2]
        assert all(verify_w_infinity_completion(6).values())

    def test_w_infinity_ope_exports(self):
        from compute.lib import (
            TruncatedWinfinityOPE,
            TruncatedWinfinitySupportComplex,
            verify_truncated_w_infinity_ope,
            verify_w_infinity_support_complex,
        )
        model = TruncatedWinfinityOPE(max_spin=5)
        support = TruncatedWinfinitySupportComplex(max_spin=5)
        assert model.generator_spins == (2, 3, 4, 5)
        assert support.weight_sector_basis(4) == ((4,), (2, 2))
        assert all(verify_truncated_w_infinity_ope(5, 7).values())
        assert all(verify_w_infinity_support_complex(5, 7).values())


class TestNonprincipalFrontier:
    def test_nonprincipal_exports(self):
        from compute.lib import (
            hook_partition,
            subregular_partition,
            type_a_bv_dual,
            nonprincipal_hook_cases,
            verify_nonprincipal_ds_orbit_scaffold,
        )
        assert hook_partition(5, 2) == (3, 1, 1)
        assert subregular_partition(4) == (3, 1)
        assert type_a_bv_dual((3, 1)) == (2, 1, 1)
        assert nonprincipal_hook_cases(5)
        assert all(verify_nonprincipal_ds_orbit_scaffold(7).values())

    def test_nonprincipal_ds_seed_exports(self):
        from sympy import Rational
        from compute.lib import (
            bp_dual_level,
            bp_residual_sl2_level,
            bp_complementarity_constant,
            sl3_subregular_good_grading_multiplicities,
            bp_current_presentation,
            bp_strong_presentation,
            first_nonselfdual_hook_pair_nilpotent_matrices,
            first_nonselfdual_hook_pair_centralizer_bases,
            first_nonselfdual_hook_pair_sl2_triples,
            ad_h_graded_basis_labels_sl_n,
            ad_h_grade_multiplicities_sl_n,
            matrix_centralizer_basis_sl_n,
            nilpotent_partition_from_matrix,
            type_a_hook_nilpotent_matrix,
            nonprincipal_hook_seed_catalog,
            verify_nonprincipal_hook_seed_catalog,
            verify_nonprincipal_ds_reduction_seed,
        )
        assert bp_dual_level(0) == -6
        assert bp_residual_sl2_level(0) == Rational(1, 2)
        assert bp_complementarity_constant() == 76
        assert sl3_subregular_good_grading_multiplicities()[0] == 2
        assert len(bp_current_presentation()) == 5
        assert len(bp_strong_presentation()) == 4
        assert nilpotent_partition_from_matrix(type_a_hook_nilpotent_matrix(4, 1)) == (3, 1)
        first_source, first_target = first_nonselfdual_hook_pair_nilpotent_matrices()
        assert len(matrix_centralizer_basis_sl_n(first_source)) == 5
        source_centralizer, target_centralizer = first_nonselfdual_hook_pair_centralizer_bases()
        source_triple, target_triple = first_nonselfdual_hook_pair_sl2_triples()
        assert nilpotent_partition_from_matrix(first_source) == (3, 1)
        assert nilpotent_partition_from_matrix(first_target) == (2, 1, 1)
        assert len(source_centralizer) == 5
        assert len(target_centralizer) == 9
        assert ad_h_graded_basis_labels_sl_n(source_triple.h)[4] == ("E13",)
        assert ad_h_grade_multiplicities_sl_n(source_triple.h)[4] == 1
        assert ad_h_grade_multiplicities_sl_n(target_triple.h)[1] == 4
        assert len(nonprincipal_hook_seed_catalog(5)) == 6
        assert all(verify_nonprincipal_hook_seed_catalog(7).values())
        assert all(verify_nonprincipal_ds_reduction_seed().values())

    def test_bv_and_ds_seed_exports(self):
        from compute.lib import (
            first_nonselfdual_type_a_hook_pair,
            verify_bv_duality_scaffold,
            sl3_subregular_bp_seed,
            verify_nonprincipal_ds_reduction_seed,
            bp_shift_to_target_sum,
            verify_nonprincipal_ds_normalization,
            sl3_subregular_ad_e_image_basis,
            sl3_subregular_ad_e_image_witnesses,
            sl3_subregular_basis_matrices,
            sl3_subregular_basis_profile,
            sl3_subregular_constraints,
            sl3_subregular_brst_blueprint,
            sl3_subregular_truncated_brst_complex,
            sl3_subregular_linear_constraint_blocks,
            sl3_subregular_project_basis_label_to_strong_candidates,
            sl3_subregular_projected_strong_brackets,
            sl3_subregular_strong_generator_candidates,
            ds_basis_expression_matrix,
            matrix_commutator,
            hook_pair_ds_seed_catalog,
            first_nonselfdual_hook_pair_ds_seed,
            verify_hook_pair_ds_seed_catalog,
            verify_hook_pair_seed_alignment,
            first_nonselfdual_hook_pair_ghost_profiles,
            first_nonselfdual_hook_pair_linear_constraint_blocks,
            complex_has_nilpotent_differential,
            chain_homology_dimensions,
            linear_constraint_block_has_contracting_homotopy,
            linear_constraint_block_is_positive_acyclic,
            first_nonselfdual_hook_pair_specialized_complexes,
            truncated_cohomology_dimensions,
            complex_is_acyclic,
            sl3_subregular_ds_seed,
            verify_ds_reduction_seed,
        )
        n, r, pair = first_nonselfdual_type_a_hook_pair()
        seed = sl3_subregular_bp_seed()
        ad_e_basis = sl3_subregular_ad_e_image_basis()
        ad_e_witnesses = sl3_subregular_ad_e_image_witnesses()
        basis_matrices = sl3_subregular_basis_matrices()
        basis = sl3_subregular_basis_profile()
        constraints = sl3_subregular_constraints()
        blueprint = sl3_subregular_brst_blueprint()
        strong_candidates = sl3_subregular_strong_generator_candidates()
        subregular_complex = sl3_subregular_truncated_brst_complex()
        subregular_blocks = sl3_subregular_linear_constraint_blocks(2)
        hook_catalog = hook_pair_ds_seed_catalog(5)
        hook_pair_seed = first_nonselfdual_hook_pair_ds_seed()
        hook_source_profile, hook_target_profile = first_nonselfdual_hook_pair_ghost_profiles()
        hook_source_blocks, hook_target_blocks = first_nonselfdual_hook_pair_linear_constraint_blocks(2)
        ds_seed = sl3_subregular_ds_seed()
        assert n == 4 and r == 1
        assert pair.source_orbit == (3, 1) and pair.target_orbit == (2, 1, 1)
        assert seed.partition == (2, 1) and seed.dual_partition == (2, 1)
        assert len(basis) == 8
        assert len(ad_e_basis) == 4
        assert sorted(ad_e_witnesses) == ["E12", "E13", "F23", "H1"]
        assert len(constraints) == 2
        assert blueprint.positive_nilpotent_is_abelian
        assert len(strong_candidates) == 4
        assert matrix_commutator(
            basis_matrices["F12"],
            ds_basis_expression_matrix(strong_candidates[0].source_terms, basis_matrices),
        ) == zeros(3, 3)
        assert sl3_subregular_project_basis_label_to_strong_candidates("H2") == {"J": 1}
        assert sl3_subregular_projected_strong_brackets()[("G+", "G-")] == {"T": 1}
        assert subregular_complex.source_tag == "A2_subregular_seed"
        assert chain_homology_dimensions(subregular_blocks[0]) == {0: 1}
        assert all(linear_constraint_block_has_contracting_homotopy(block) for block in subregular_blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in subregular_blocks[1:])
        assert hook_pair_seed.source_partition == (3, 1)
        assert hook_pair_seed.target_partition == (2, 1, 1)
        assert len(hook_source_profile) == 5
        assert len(hook_target_profile) == 5
        assert len(hook_catalog) == 6
        assert complex_has_nilpotent_differential(subregular_complex)
        assert complex_has_nilpotent_differential(hook_pair_seed.source_complex)
        assert complex_has_nilpotent_differential(hook_pair_seed.target_complex)
        assert all(linear_constraint_block_has_contracting_homotopy(block) for block in hook_source_blocks[1:])
        assert all(linear_constraint_block_has_contracting_homotopy(block) for block in hook_target_blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in hook_source_blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in hook_target_blocks[1:])
        assert len(hook_source_blocks[0].ghost_labels) == 5
        assert len(hook_target_blocks[0].ghost_labels) == 5
        assert truncated_cohomology_dimensions(subregular_complex) == {0: 0, 1: 0, 2: 0}
        assert complex_is_acyclic(subregular_complex)
        source_spec, target_spec = first_nonselfdual_hook_pair_specialized_complexes(
            source_chi=(1, 0, 0, 0, 0),
            target_chi=(1, 0, 0, 0, 0),
        )
        assert complex_is_acyclic(source_spec)
        assert complex_is_acyclic(target_spec)
        assert ds_seed.partition == (2, 1)
        assert bp_shift_to_target_sum(22) == -27
        assert all(verify_bv_duality_scaffold(7).values())
        assert all(verify_nonprincipal_ds_reduction_seed().values())
        assert all(verify_nonprincipal_ds_normalization().values())
        assert all(verify_hook_pair_ds_seed_catalog(7).values())
        assert all(verify_hook_pair_seed_alignment(7).values())
        assert all(verify_ds_reduction_seed().values())
