"""Tests for non-principal DS normalization bridge."""

from sympy import Symbol, simplify

from compute.lib.nonprincipal_ds_normalization import (
    CHAPTER_BP_SUM_CONVENTION,
    RAW_BP_CONVENTION,
    bp_dual_sum_under_convention,
    bp_shift_to_target_sum,
    bp_shifted_convention_for_target,
    verify_nonprincipal_ds_normalization,
)


class TestNormalizationBridge:
    def test_raw_sum(self):
        k = Symbol("k")
        assert simplify(bp_dual_sum_under_convention(RAW_BP_CONVENTION, k) - 196) == 0

    def test_shift_to_22(self):
        assert simplify(bp_shift_to_target_sum(22) + 87) == 0

    def test_shifted_sum(self):
        k = Symbol("k")
        conv = bp_shifted_convention_for_target(22)
        assert simplify(bp_dual_sum_under_convention(conv, k) - 22) == 0

    def test_explicit_bridge_constant(self):
        k = Symbol("k")
        assert simplify(bp_dual_sum_under_convention(CHAPTER_BP_SUM_CONVENTION, k) - 22) == 0


class TestVerificationBundle:
    def test_all_checks(self):
        assert all(verify_nonprincipal_ds_normalization().values())
