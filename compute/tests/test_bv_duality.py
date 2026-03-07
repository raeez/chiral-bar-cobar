"""Tests for the BV duality scaffold."""

from compute.lib.bv_duality import (
    first_nonselfdual_type_a_hook_pair,
    is_type_a_self_dual_orbit,
    type_a_bv_dual,
    type_a_bv_pair,
    type_a_hook_bv_pair,
    verify_bv_duality_scaffold,
)


class TestTypeADuality:
    def test_transpose_duality(self):
        assert type_a_bv_dual((3, 1, 1)) == (3, 1, 1)
        assert type_a_bv_dual((4, 1)) == (2, 1, 1, 1)

    def test_self_dual_detection(self):
        assert is_type_a_self_dual_orbit((2, 1))
        assert not is_type_a_self_dual_orbit((3, 1))

    def test_pair_record(self):
        pair = type_a_bv_pair(4, (3, 1))
        assert pair.source_type == "A"
        assert pair.source_rank == 3
        assert pair.source_orbit == (3, 1)
        assert pair.target_orbit == (2, 1, 1)
        assert not pair.is_self_dual


class TestHooks:
    def test_hook_pair(self):
        pair = type_a_hook_bv_pair(6, 2)
        assert pair.source_orbit == (4, 1, 1)
        assert pair.target_orbit == (3, 1, 1, 1)

    def test_first_nonselfdual(self):
        n, r, pair = first_nonselfdual_type_a_hook_pair()
        assert n == 4
        assert r == 1
        assert pair.source_orbit == (3, 1)
        assert pair.target_orbit == (2, 1, 1)


class TestVerificationBundle:
    def test_all_checks(self):
        assert all(verify_bv_duality_scaffold(max_n=9).values())
