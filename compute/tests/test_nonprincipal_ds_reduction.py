"""Tests for the non-principal DS reduction seed layer."""

from sympy import Rational, Symbol, simplify

from compute.lib.nonprincipal_ds_reduction import (
    STATUS_HOOK_EVIDENCE,
    STATUS_PROGRAMME,
    STATUS_PROVED_SUBREGULAR_SL3,
    bp_central_charge,
    bp_complementarity_constant,
    bp_complementarity_sum,
    bp_current_presentation,
    bp_dual_level,
    bp_residual_sl2_dual_relation,
    bp_residual_sl2_level,
    bp_strong_presentation,
    first_nonselfdual_hook_seed,
    nonprincipal_hook_seed,
    nonprincipal_hook_seed_catalog,
    sl3_subregular_bp_seed,
    sl3_subregular_good_grading_multiplicities,
    verify_nonprincipal_hook_seed_catalog,
    verify_nonprincipal_ds_reduction_seed,
)


class TestBershadskyPolyakovSeed:
    def test_dual_level(self):
        k = Symbol("k")
        assert simplify(bp_dual_level(k) - (-k - 6)) == 0

    def test_central_charge_bundle(self):
        k = Symbol("k")
        assert simplify(bp_complementarity_sum(k) - bp_complementarity_constant()) == 0
        assert simplify(bp_complementarity_constant() - 76) == 0
        assert bp_central_charge(0) == -7

    def test_residual_sl2_level(self):
        k = Symbol("k")
        assert simplify(bp_residual_sl2_level(k) - (k + Rational(1, 2))) == 0
        assert bp_residual_sl2_dual_relation(k) == 0

    def test_good_grading_multiplicities(self):
        grading = sl3_subregular_good_grading_multiplicities()
        assert grading == {-2: 1, -1: 2, 0: 2, 1: 2, 2: 1}
        assert sum(grading.values()) == 8

    def test_presentations(self):
        assert bp_current_presentation() == (
            ("J1", 1, "bosonic"),
            ("J2", 1, "bosonic"),
            ("J3", 1, "bosonic"),
            ("G+", Rational(3, 2), "fermionic"),
            ("G-", Rational(3, 2), "fermionic"),
        )
        assert bp_strong_presentation() == (
            ("J", 1, "bosonic"),
            ("G+", Rational(3, 2), "fermionic"),
            ("G-", Rational(3, 2), "fermionic"),
            ("T", 2, "bosonic"),
        )

    def test_seed_record(self):
        seed = sl3_subregular_bp_seed()
        assert seed.partition == (2, 1)
        assert seed.dual_partition == (2, 1)
        assert seed.status == STATUS_PROVED_SUBREGULAR_SL3


class TestFirstNonselfdualHookSeed:
    def test_seed(self):
        seed = first_nonselfdual_hook_seed()
        assert seed.partition == (3, 1)
        assert seed.dual_partition == (2, 1, 1)
        assert seed.status == STATUS_HOOK_EVIDENCE


class TestHookSeedFamily:
    def test_generic_seed(self):
        k = Symbol("k")
        seed = nonprincipal_hook_seed(6, 2, level=k)
        assert seed.partition == (4, 1, 1)
        assert seed.dual_partition == (3, 1, 1, 1)
        assert simplify(seed.level_shift - (-k - 12)) == 0
        assert seed.status == STATUS_HOOK_EVIDENCE

    def test_programme_status_propagation(self):
        seed = nonprincipal_hook_seed(8, 3)
        assert seed.status == STATUS_PROGRAMME

    def test_catalog(self):
        seeds = nonprincipal_hook_seed_catalog(max_n=5)
        assert len(seeds) == 6
        assert seeds[0].partition == (2, 1)
        assert seeds[-1].partition == (2, 1, 1, 1)

    def test_catalog_verification(self):
        assert all(verify_nonprincipal_hook_seed_catalog(max_n=8).values())


class TestVerificationBundle:
    def test_all_checks(self):
        assert all(verify_nonprincipal_ds_reduction_seed().values())
