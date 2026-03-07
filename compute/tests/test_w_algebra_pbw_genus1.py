"""Tests for genus-1 PBW support in principal finite-type W-algebras."""

from compute.lib.w_algebra_pbw_genus1 import (
    d2_target_weight,
    d2_weight_shift,
    has_unique_stress_tensor,
    higher_spin_generators,
    principal_generator_weights,
    verify_principal_w_pbw_genus1,
    verify_principal_weight_argument,
    verify_w3_d2_weight_pattern,
    verify_w3_l0_scalar,
)


class TestPrincipalGeneratorWeights:
    """Principal W-algebra generators are determined by exponents + 1."""

    def test_A1_weights(self):
        assert principal_generator_weights("A", 1) == [2]

    def test_A2_weights(self):
        assert principal_generator_weights("A", 2) == [2, 3]

    def test_A3_weights(self):
        assert principal_generator_weights("A", 3) == [2, 3, 4]

    def test_B2_weights(self):
        assert principal_generator_weights("B", 2) == [2, 4]

    def test_C2_weights(self):
        assert principal_generator_weights("C", 2) == [2, 4]

    def test_G2_weights(self):
        assert principal_generator_weights("G", 2) == [2, 6]

    def test_F4_weights(self):
        assert principal_generator_weights("F", 4) == [2, 6, 8, 12]

    def test_unique_stress_tensor(self):
        for family in [("A", 1), ("A", 2), ("A", 3), ("B", 2), ("C", 2), ("G", 2), ("F", 4)]:
            assert has_unique_stress_tensor(*family)

    def test_higher_spin_generators(self):
        assert higher_spin_generators("A", 2) == [3]
        assert higher_spin_generators("A", 3) == [3, 4]
        assert higher_spin_generators("G", 2) == [6]


class TestD2WeightShifts:
    """Only the stress tensor contributes to the weight-diagonal d_2 block."""

    def test_stress_tensor_shift(self):
        assert d2_weight_shift(2) == 0
        assert d2_target_weight(7, 2) == 7

    def test_higher_spin_shifts_are_positive(self):
        assert d2_weight_shift(3) == 1
        assert d2_weight_shift(4) == 2
        assert d2_weight_shift(6) == 4

    def test_verification_bundle(self):
        for ok in verify_principal_weight_argument(max_weight=8).values():
            assert ok


class TestW3ExplicitChecks:
    """Low-weight W_3 computations realize the abstract triangular pattern."""

    def test_w3_l0_scalar_bundle(self):
        for ok in verify_w3_l0_scalar(max_weight=8).values():
            assert ok

    def test_w3_d2_pattern_bundle(self):
        for ok in verify_w3_d2_weight_pattern(max_weight=8).values():
            assert ok


class TestIntegration:
    """End-to-end support bundle used by the manuscript theorem."""

    def test_all_pass(self):
        for name, ok in verify_principal_w_pbw_genus1(max_weight=8).items():
            assert ok, name
