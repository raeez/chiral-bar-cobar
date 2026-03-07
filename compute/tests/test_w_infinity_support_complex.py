"""Tests for the truncated W_infinity support skeleton."""

from compute.lib.w_infinity_support_complex import (
    TruncatedWinfinitySupportComplex,
    verify_w_infinity_support_complex,
)


class TestTruncatedWinfinitySupportComplex:
    def test_weight_sector_basis(self):
        complex_ = TruncatedWinfinitySupportComplex(max_spin=6)
        assert complex_.weight_sector_basis(4) == ((4,), (2, 2))
        assert complex_.weight_sector_basis(6) == (
            (6,),
            (2, 4),
            (3, 3),
            (4, 2),
            (2, 2, 2),
        )

    def test_lower_weight_target_basis_starts_with_vacuum(self):
        complex_ = TruncatedWinfinitySupportComplex(max_spin=6)
        basis = complex_.lower_weight_target_basis(5)
        assert basis[0] == ()
        assert (2,) in basis
        assert (3,) in basis
        assert (2, 2) in basis

    def test_support_targets_for_tt(self):
        complex_ = TruncatedWinfinitySupportComplex(max_spin=6)
        assert complex_.support_targets((2, 2)) == ((), (2,), (3,))

    def test_support_matrix_weight_four(self):
        complex_ = TruncatedWinfinitySupportComplex(max_spin=6)
        source_basis, target_basis, matrix = complex_.support_matrix_at_weight(4)
        assert source_basis == ((4,), (2, 2))
        assert source_basis[1] == (2, 2)
        source_col = 1
        actual = {
            target_basis[row]
            for row in range(matrix.rows)
            if matrix[row, source_col] != 0
        }
        assert actual == {(), (2,), (3,)}

    def test_profile_is_finite(self):
        complex_ = TruncatedWinfinitySupportComplex(max_spin=6)
        profile = complex_.support_profile(7)
        assert profile["source_size"] > 0
        assert profile["target_size"] > 0
        assert profile["edge_count"] > 0

    def test_verification_bundle(self):
        assert all(verify_w_infinity_support_complex(max_spin=6, max_total_weight=8).values())
