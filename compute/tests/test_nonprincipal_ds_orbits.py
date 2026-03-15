"""Tests for the non-principal DS/orbit scaffold (hook + subregular)."""

import pytest

pytestmark = pytest.mark.slow

from sympy import Rational, Symbol, simplify
from sympy import zeros

from compute.lib.nonprincipal_ds_orbits import (
    HookOrbitPairProfile,
    MatrixSl2Triple,
    STATUS_HOOK_EVIDENCE,
    STATUS_PROVED_SUBREGULAR_SL3,
    TRACK_FRONTIER_NONPRINCIPAL,
    ad_h_graded_basis_labels_sl_n,
    ad_h_grade_multiplicities_sl_n,
    centralizer_dimension_sl_n,
    first_nonselfdual_hook_pair_centralizer_bases,
    first_nonselfdual_hook_pair_f_centralizer_bases,
    first_nonselfdual_hook_pair_nilpotent_matrices,
    first_nonselfdual_hook_pair_sl2_triples,
    hook_dual_partition,
    hook_orbit_pair_profile,
    hook_orbit_pair_profile_catalog,
    hook_partition,
    is_hook_partition,
    matrix_centralizer_basis_sl_n,
    matrix_centralizer_dimension_sl_n,
    matrix_to_traceless_basis_expression_sl_n,
    nilpotent_partition_from_matrix,
    nonprincipal_general_cases,
    nonprincipal_hook_case,
    nonprincipal_hook_cases,
    nonprincipal_hook_level_shift_type_a,
    nonprincipal_hook_level_shift_ansatz_type_a,
    nonprincipal_orbit_level_shift_type_a,
    nonprincipal_type_a_case,
    nonprincipal_two_row_case,
    nonprincipal_two_row_cases,
    two_row_nonhook_partition,
    orbit_dimension_sl_n,
    principal_ff_level_shift_type_a,
    standard_traceless_basis_sl_n,
    subregular_partition,
    transpose_partition,
    type_a_hook_pair_sl2_triples,
    type_a_hook_sl2_triple,
    type_a_hook_nilpotent_matrix,
    type_a_nilpotent_matrix,
    type_a_general_nonprincipal_partitions,
    type_a_orbit_class,
    type_a_orbit_level_shift_correction_data,
    type_a_partition_sl2_triple,
    verify_hook_orbit_pair_profile_catalog,
    verify_nonprincipal_general_orbit_scaffold,
    verify_nonprincipal_two_row_orbit_scaffold,
    verify_nonprincipal_ds_orbit_scaffold,
)


class TestPartitionCombinatorics:
    def test_transpose_involution(self):
        partition = (4, 2, 1)
        assert transpose_partition(transpose_partition(partition)) == partition

    def test_hook_constructor(self):
        assert hook_partition(6, 2) == (4, 1, 1)
        assert hook_partition(6, 0) == (6,)
        assert hook_partition(6, 5) == (1, 1, 1, 1, 1, 1)

    def test_subregular_constructor(self):
        assert subregular_partition(3) == (2, 1)
        assert subregular_partition(7) == (6, 1)

    def test_hook_dual_formula(self):
        # (n-r,1^r)^t = (r+1,1^{n-r-1})
        assert hook_dual_partition(6, 2) == (3, 1, 1, 1)
        assert hook_dual_partition(5, 1) == (2, 1, 1, 1)

    def test_hook_detection(self):
        assert is_hook_partition((5, 1, 1))
        assert is_hook_partition((4,))
        assert not is_hook_partition((3, 2, 1))

    def test_two_row_nonhook_constructor(self):
        assert two_row_nonhook_partition(6, 2) == (4, 2)
        assert two_row_nonhook_partition(7, 3) == (4, 3)

    def test_general_partition_catalog(self):
        assert type_a_general_nonprincipal_partitions(6) == (
            (3, 2, 1),
            (2, 2, 2),
            (2, 2, 1, 1),
        )


class TestOrbitClassification:
    def test_classes(self):
        assert type_a_orbit_class((5,)) == "principal"
        assert type_a_orbit_class((1, 1, 1, 1, 1)) == "trivial"
        assert type_a_orbit_class((4, 1)) == "subregular"
        assert type_a_orbit_class((3, 1, 1)) == "hook_nonprincipal"
        assert type_a_orbit_class((3, 2, 1)) == "general_nonprincipal"


class TestDimensions:
    def test_subregular_sl3_dimensions(self):
        # sl_3 subregular (2,1): orbit dim 4, centralizer dim 4.
        partition = (2, 1)
        assert orbit_dimension_sl_n(partition) == 4
        assert centralizer_dimension_sl_n(partition) == 4
        assert orbit_dimension_sl_n(partition) + centralizer_dimension_sl_n(partition) == 8

    def test_subregular_sl4_dimensions(self):
        # n=4: orbit dim = n^2 - (n+2) = 10 for (3,1).
        partition = (3, 1)
        assert orbit_dimension_sl_n(partition) == 10
        assert centralizer_dimension_sl_n(partition) == 5
        assert orbit_dimension_sl_n(partition) + centralizer_dimension_sl_n(partition) == 15

    def test_matrix_representatives_recover_partitions(self):
        assert nilpotent_partition_from_matrix(type_a_nilpotent_matrix((3, 1))) == (3, 1)
        assert nilpotent_partition_from_matrix(type_a_hook_nilpotent_matrix(6, 2)) == (4, 1, 1)

    def test_standard_basis_and_reexpansion(self):
        basis = standard_traceless_basis_sl_n(4)
        assert len(basis) == 15
        expression = matrix_to_traceless_basis_expression_sl_n(
            basis[0][1] + 2 * basis[-1][1]
        )
        assert expression == ((basis[0][0], 1), (basis[-1][0], 2))

    def test_standard_basis_uses_unambiguous_labels_at_rank_10_and_above(self):
        basis = standard_traceless_basis_sl_n(11)
        labels = tuple(label for label, _ in basis)
        assert len(labels) == len(set(labels))
        assert "E1_11" in labels
        assert "E11_1" in labels
        expression = matrix_to_traceless_basis_expression_sl_n(
            dict(basis)["E1_11"] + 2 * dict(basis)["E11_1"]
        )
        assert expression == (("E1_11", 1), ("E11_1", 2))

    def test_matrix_centralizer_dimensions_match_partition_formula(self):
        hook_matrix = type_a_hook_nilpotent_matrix(4, 1)
        dual_matrix = type_a_nilpotent_matrix((2, 1, 1))
        assert matrix_centralizer_dimension_sl_n(hook_matrix) == centralizer_dimension_sl_n((3, 1))
        assert matrix_centralizer_dimension_sl_n(dual_matrix) == centralizer_dimension_sl_n((2, 1, 1))

    def test_first_nonselfdual_hook_pair_matrices(self):
        source, target = first_nonselfdual_hook_pair_nilpotent_matrices()
        assert nilpotent_partition_from_matrix(source) == (3, 1)
        assert nilpotent_partition_from_matrix(target) == (2, 1, 1)

    def test_matrix_centralizer_basis(self):
        matrix = type_a_hook_nilpotent_matrix(4, 1)
        basis = matrix_centralizer_basis_sl_n(matrix)
        assert len(basis) == centralizer_dimension_sl_n((3, 1))
        assert all(candidate.trace() == 0 for candidate in basis)
        assert all(matrix * candidate - candidate * matrix == zeros(4, 4) for candidate in basis)

    def test_first_nonselfdual_hook_pair_centralizer_bases(self):
        source, target = first_nonselfdual_hook_pair_nilpotent_matrices()
        source_basis, target_basis = first_nonselfdual_hook_pair_centralizer_bases()
        assert len(source_basis) == centralizer_dimension_sl_n((3, 1))
        assert len(target_basis) == centralizer_dimension_sl_n((2, 1, 1))
        assert all(source * candidate - candidate * source == zeros(4, 4) for candidate in source_basis)
        assert all(target * candidate - candidate * target == zeros(4, 4) for candidate in target_basis)

    def test_first_nonselfdual_hook_pair_sl2_triples(self):
        source, target = first_nonselfdual_hook_pair_sl2_triples()
        assert isinstance(source, MatrixSl2Triple)
        assert isinstance(target, MatrixSl2Triple)
        assert source.h * source.e - source.e * source.h == 2 * source.e
        assert source.h * source.f - source.f * source.h == -2 * source.f
        assert source.e * source.f - source.f * source.e == source.h
        assert target.h * target.e - target.e * target.h == 2 * target.e
        assert target.h * target.f - target.f * target.h == -2 * target.f
        assert target.e * target.f - target.f * target.e == target.h

    def test_first_nonselfdual_hook_pair_grading_multiplicities(self):
        source, target = first_nonselfdual_hook_pair_sl2_triples()
        assert ad_h_grade_multiplicities_sl_n(source.h) == {4: 1, 2: 4, 0: 5, -2: 4, -4: 1}
        assert ad_h_grade_multiplicities_sl_n(target.h) == {2: 1, 1: 4, 0: 5, -1: 4, -2: 1}

    def test_first_nonselfdual_hook_pair_graded_basis_labels(self):
        source, target = first_nonselfdual_hook_pair_sl2_triples()
        source_labels = ad_h_graded_basis_labels_sl_n(source.h)
        target_labels = ad_h_graded_basis_labels_sl_n(target.h)
        assert source_labels[4] == ("E13",)
        assert source_labels[2] == ("E12", "E14", "E23", "E43")
        assert target_labels[2] == ("E12",)
        assert target_labels[1] == ("E13", "E14", "E32", "E42")

    def test_first_nonselfdual_hook_pair_f_centralizer_bases(self):
        source_basis, target_basis = first_nonselfdual_hook_pair_f_centralizer_bases()
        assert tuple(sorted(source_basis, reverse=True)) == (0, -2, -4)
        assert tuple(sorted(target_basis, reverse=True)) == (0, -1, -2)
        assert sum(len(items) for items in source_basis.values()) == 5
        assert sum(len(items) for items in target_basis.values()) == 9
        assert source_basis[0][0] == (
            ("H1", Rational(1, 3)),
            ("H2", Rational(2, 3)),
            ("H3", Rational(1)),
        )

    def test_partition_hook_triple_builders(self):
        partition_triple = type_a_partition_sl2_triple((3, 1))
        hook_triple = type_a_hook_sl2_triple(4, 1)
        source, target = type_a_hook_pair_sl2_triples(4, 1)
        first_source, first_target = first_nonselfdual_hook_pair_sl2_triples()

        assert partition_triple.e == hook_triple.e
        assert source.e == first_source.e
        assert target.e == first_target.e
        assert source.h * source.e - source.e * source.h == 2 * source.e
        assert source.h * source.f - source.f * source.h == -2 * source.f
        assert source.e * source.f - source.f * source.e == source.h
        assert nilpotent_partition_from_matrix(source.e) == (3, 1)
        assert nilpotent_partition_from_matrix(target.e) == (2, 1, 1)


class TestFrontierCases:
    def test_single_case_status_and_track(self):
        subregular = nonprincipal_hook_case(3, 1)
        assert subregular.family == "subregular"
        assert subregular.status == STATUS_PROVED_SUBREGULAR_SL3
        assert subregular.track == TRACK_FRONTIER_NONPRINCIPAL

        hook = nonprincipal_hook_case(5, 2)
        assert hook.family == "hook"
        assert hook.status == STATUS_HOOK_EVIDENCE
        assert hook.track == TRACK_FRONTIER_NONPRINCIPAL

    def test_frontier_catalog_excludes_principal_and_trivial(self):
        cases = nonprincipal_hook_cases(max_n=6)
        assert cases
        assert all(type_a_orbit_class(case.partition) != "principal" for case in cases)
        assert all(type_a_orbit_class(case.partition) != "trivial" for case in cases)

    def test_two_row_frontier_cases(self):
        case = nonprincipal_two_row_case(6, 2)
        assert case.family == "two_row_nonhook"
        assert case.partition == (4, 2)
        assert case.dual_partition == (2, 2, 1, 1)
        cases = nonprincipal_two_row_cases(max_n=7)
        assert cases
        assert all(type_a_orbit_class(entry.partition) == "two_row_nonhook" for entry in cases)

    def test_general_frontier_cases(self):
        cases = nonprincipal_general_cases(max_n=6)
        assert cases
        assert cases[0].partition == (2, 2, 1)
        assert all(type_a_orbit_class(entry.partition) == "general_nonprincipal" for entry in cases)

    def test_frontier_case_builders_normalize_and_cache(self):
        tuple_case = nonprincipal_type_a_case((4, 2))
        list_case = nonprincipal_type_a_case([4, 2])
        assert tuple_case is list_case
        assert nonprincipal_two_row_case(6, 2) is nonprincipal_two_row_case(6, 2)

    def test_frontier_catalogs_reuse_cached_tuples(self):
        assert nonprincipal_hook_cases(max_n=6) is nonprincipal_hook_cases(max_n=6)
        assert nonprincipal_two_row_cases(max_n=7) is nonprincipal_two_row_cases(max_n=7)
        assert nonprincipal_general_cases(max_n=6) is nonprincipal_general_cases(max_n=6)


class TestHookOrbitProfiles:
    def test_single_profile(self):
        profile = hook_orbit_pair_profile(6, 2)
        assert isinstance(profile, HookOrbitPairProfile)
        assert profile.source_partition == (4, 1, 1)
        assert profile.target_partition == (3, 1, 1, 1)
        assert profile.source_orbit_dimension + profile.source_centralizer_dimension == 35
        assert profile.target_orbit_dimension + profile.target_centralizer_dimension == 35
        assert profile.source_positive_simple_root_count == 3
        assert profile.target_positive_simple_root_count == 2
        assert profile.source_positive_basis_labels[:3] == ("E14", "E13", "E24")
        assert profile.target_positive_basis_labels[0] == "E13"

    def test_profile_catalog(self):
        catalog = hook_orbit_pair_profile_catalog(max_n=5)
        assert len(catalog) == 6
        assert catalog[0].source_partition == (2, 1)
        assert catalog[-1].source_partition == (2, 1, 1, 1)


class TestLevelShiftScaffold:
    def test_hook_ansatz_matches_principal_ff_shift(self):
        k = Symbol("k")
        lhs = nonprincipal_hook_level_shift_ansatz_type_a(6, k)
        rhs = principal_ff_level_shift_type_a(6, k)
        assert simplify(lhs - rhs) == 0
        assert simplify(lhs - (-k - 12)) == 0

    def test_data_driven_hook_shift(self):
        k = Symbol("k")
        assert simplify(nonprincipal_hook_level_shift_type_a(6, 2, k) - (-k - 12)) == 0
        assert type_a_orbit_level_shift_correction_data((4, 2)) == 1
        assert simplify(nonprincipal_orbit_level_shift_type_a((4, 2), k) - (-k - 13)) == 0
        assert type_a_orbit_level_shift_correction_data((3, 2, 1)) == 1
        assert simplify(nonprincipal_orbit_level_shift_type_a((3, 2, 1), k) - (-k - 13)) == 0

    def test_general_seed_correction_is_dual_symmetric(self):
        assert type_a_orbit_level_shift_correction_data((4, 2, 1)) == 1
        assert type_a_orbit_level_shift_correction_data((3, 2, 1, 1)) == 1
        assert type_a_orbit_level_shift_correction_data((3, 3, 1)) == 2
        assert type_a_orbit_level_shift_correction_data((3, 2, 2)) == 2


class TestVerificationBundle:
    def test_all_checks(self):
        assert all(verify_nonprincipal_ds_orbit_scaffold(max_n=8).values())
        assert all(verify_hook_orbit_pair_profile_catalog(max_n=8).values())
        assert all(verify_nonprincipal_general_orbit_scaffold(max_n=7).values())
        assert all(verify_nonprincipal_two_row_orbit_scaffold(max_n=8).values())
