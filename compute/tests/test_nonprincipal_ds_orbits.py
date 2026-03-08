"""Tests for the non-principal DS/orbit scaffold (hook + subregular)."""

from sympy import Symbol, simplify
from sympy import zeros

from compute.lib.nonprincipal_ds_orbits import (
    MatrixSl2Triple,
    STATUS_HOOK_EVIDENCE,
    STATUS_PROVED_SUBREGULAR_SL3,
    TRACK_FRONTIER_NONPRINCIPAL,
    ad_h_graded_basis_labels_sl_n,
    ad_h_grade_multiplicities_sl_n,
    centralizer_dimension_sl_n,
    first_nonselfdual_hook_pair_centralizer_bases,
    first_nonselfdual_hook_pair_nilpotent_matrices,
    first_nonselfdual_hook_pair_sl2_triples,
    hook_dual_partition,
    hook_partition,
    is_hook_partition,
    matrix_centralizer_basis_sl_n,
    matrix_centralizer_dimension_sl_n,
    nilpotent_partition_from_matrix,
    nonprincipal_hook_case,
    nonprincipal_hook_cases,
    nonprincipal_hook_level_shift_ansatz_type_a,
    orbit_dimension_sl_n,
    principal_ff_level_shift_type_a,
    subregular_partition,
    transpose_partition,
    type_a_hook_nilpotent_matrix,
    type_a_nilpotent_matrix,
    type_a_orbit_class,
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


class TestLevelShiftScaffold:
    def test_hook_ansatz_matches_principal_ff_shift(self):
        k = Symbol("k")
        lhs = nonprincipal_hook_level_shift_ansatz_type_a(6, k)
        rhs = principal_ff_level_shift_type_a(6, k)
        assert simplify(lhs - rhs) == 0
        assert simplify(lhs - (-k - 12)) == 0


class TestVerificationBundle:
    def test_all_checks(self):
        assert all(verify_nonprincipal_ds_orbit_scaffold(max_n=8).values())
