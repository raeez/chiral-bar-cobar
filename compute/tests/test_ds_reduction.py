"""Tests for DS reduction seed scaffold."""

from sympy import Rational, Symbol, simplify

from compute.lib.ds_reduction import (
    STATUS_DS_SEED,
    brst_ghost_weights,
    sl3_subregular_ds_seed,
    sl3_subregular_ghost_profile,
    sl3_subregular_positive_grades,
    sl3_subregular_sl2_triple,
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

    def test_positive_grades(self):
        grades = sl3_subregular_positive_grades()
        assert grades == {"alpha1": 2, "alpha1+alpha2": 1}

    def test_seed_record(self):
        k = Symbol("k")
        seed = sl3_subregular_ds_seed(k)
        assert seed.partition == (2, 1)
        assert simplify(seed.dual_level - (-k - 6)) == 0
        assert seed.expected_target == "affine_sl2_seed"
        assert seed.track == "frontier_nonprincipal_ds_orbit"
        assert seed.status == STATUS_DS_SEED


class TestVerificationBundle:
    def test_all_checks(self):
        assert all(verify_ds_reduction_seed().values())
