"""Tests for the infinite-generator completed bar scaffold."""

from compute.lib.pronilpotent_bar import (
    degree_sector_dimension_formula,
    effective_generator_weights,
    max_bar_degree,
    ordered_weight_monomials,
    total_sector_dimension_formula,
    verify_w_infinity_completion,
    w_infinity_generator_weights,
    w_infinity_weight_sector,
    weight_sector_profile,
)


class TestPronilpotentBar:
    def test_effective_generator_truncation(self):
        assert effective_generator_weights(5, [2, 3, 4, 5, 6, 8]) == (2, 3, 4, 5)

    def test_w_infinity_effective_weights(self):
        assert w_infinity_generator_weights(6) == (2, 3, 4, 5, 6)

    def test_max_bar_degree(self):
        assert max_bar_degree(1) == 0
        assert max_bar_degree(6) == 3
        assert max_bar_degree(9) == 4

    def test_weight_six_degree_two_basis(self):
        basis = ordered_weight_monomials(6, w_infinity_generator_weights(6), 2)
        assert basis == ((2, 4), (3, 3), (4, 2))

    def test_degree_dimension_formula(self):
        for total_weight in range(2, 10):
            weights = w_infinity_generator_weights(total_weight)
            for degree in range(1, max_bar_degree(total_weight) + 1):
                basis = ordered_weight_monomials(total_weight, weights, degree)
                assert len(basis) == degree_sector_dimension_formula(total_weight, degree)

    def test_total_dimension_formula(self):
        expected = {
            2: 1,
            3: 1,
            4: 2,
            5: 3,
            6: 5,
            7: 8,
            8: 13,
        }
        for total_weight, dimension in expected.items():
            profile = w_infinity_weight_sector(total_weight)
            total = sum(len(basis) for basis in profile.values())
            assert total == dimension
            assert total == total_sector_dimension_formula(total_weight)

    def test_truncation_stability(self):
        for total_weight in range(2, 10):
            profile = w_infinity_weight_sector(total_weight)
            larger = weight_sector_profile(total_weight, range(2, total_weight + 6))
            assert profile == larger

    def test_verification_bundle(self):
        assert all(verify_w_infinity_completion(8).values())
