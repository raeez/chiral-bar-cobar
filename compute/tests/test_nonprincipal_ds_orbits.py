"""Tests for the non-principal DS/orbit scaffold (hook + subregular)."""

from sympy import Symbol, simplify

from compute.lib.nonprincipal_ds_orbits import (
    STATUS_HOOK_EVIDENCE,
    STATUS_PROVED_SUBREGULAR_SL3,
    TRACK_FRONTIER_NONPRINCIPAL,
    centralizer_dimension_sl_n,
    hook_dual_partition,
    hook_partition,
    is_hook_partition,
    nonprincipal_hook_case,
    nonprincipal_hook_cases,
    nonprincipal_hook_level_shift_ansatz_type_a,
    orbit_dimension_sl_n,
    principal_ff_level_shift_type_a,
    subregular_partition,
    transpose_partition,
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
