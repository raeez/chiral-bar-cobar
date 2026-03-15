"""Tests for the truncated W_infinity structural OPE scaffold."""

from sympy import Symbol

from compute.lib.w_infinity_ope import (
    TruncatedWinfinityOPE,
    verify_truncated_w_infinity_ope,
)


class TestTruncatedWinfinityOPE:
    def test_generator_spins(self):
        model = TruncatedWinfinityOPE(max_spin=5)
        assert model.generator_spins == (2, 3, 4, 5)
        assert [generator.name for generator in model.generators] == [
            "W_2",
            "W_3",
            "W_4",
            "W_5",
        ]

    def test_stress_tensor_ope_on_primary(self):
        model = TruncatedWinfinityOPE(max_spin=5)
        ope = model.stress_tensor_ope(3)
        assert ope == {
            2: {"W_3": 3},
            1: {"dW_3": 1},
        }

    def test_stress_tensor_ope_on_itself(self):
        c = Symbol("c")
        model = TruncatedWinfinityOPE(max_spin=5, central_charge=c)
        ope = model.stress_tensor_ope(2)
        assert ope[4]["1"] == c / 2
        assert ope[2]["W_2"] == 2
        assert ope[1]["dW_2"] == 1

    def test_exact_stress_tensor_output_weights(self):
        model = TruncatedWinfinityOPE(max_spin=6)
        assert model.truncated_singular_output_weights(2, 2) == (0, 2, 3)
        assert model.truncated_singular_output_weights(2, 4) == (4, 5)
        assert model.truncated_singular_output_weights(4, 2) == (4, 5)

    def test_higher_spin_coarse_support(self):
        model = TruncatedWinfinityOPE(max_spin=6)
        assert model.truncated_singular_output_weights(3, 4) == (2, 3, 4, 5, 6)

    def test_adjacent_outputs(self):
        model = TruncatedWinfinityOPE(max_spin=5)
        assert model.adjacent_truncated_singular_outputs((2, 2), 0) == (
            (),
            (2,),
            (3,),
        )
        assert model.adjacent_truncated_singular_outputs((2, 3, 2), 0) == (
            (3, 2),
            (4, 2),
        )

    def test_degree_two_weight_profile(self):
        model = TruncatedWinfinityOPE(max_spin=6)
        profile = model.degree_two_output_profile(6)
        assert set(profile) == {(2, 4), (3, 3), (4, 2)}
        for source, outputs in profile.items():
            assert outputs
            assert all(sum(out) <= sum(source) - 1 for out in outputs)

    def test_verification_bundle(self):
        assert all(verify_truncated_w_infinity_ope(max_spin=6, max_total_weight=8).values())
