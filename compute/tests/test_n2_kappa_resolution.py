"""Tests for exact N=2 parameter arithmetic and open modular status."""

import pytest
import sympy as sp

from compute.lib.n2_kappa_resolution import (
    F1_values,
    OpenN2InvariantError,
    complementarity_sum,
    coset_decomposition,
    discrepancy,
    discrepancy_symbolic,
    k_from_c,
    kappa_fermion_pair,
    kappa_n2_correct,
    kappa_n2_from_k,
    kappa_n2_wrong,
    kappa_sl2,
    kappa_u1_denominator,
    n2_central_charge,
    n2_koszul_dual_c,
    n2_koszul_dual_level,
    n2_modular_status,
    parameter_reflection_check,
    sigma_n2,
    sl2_naive_vs_correct,
    verify_resolution,
    wrong_duality_check,
)


class TestParameterArithmetic:
    @pytest.mark.parametrize(
        ("level", "central_charge"),
        [(1, 1), (2, sp.Rational(3, 2)), (10, sp.Rational(5, 2))],
    )
    def test_central_charge(self, level, central_charge):
        assert n2_central_charge(level) == central_charge

    @pytest.mark.parametrize("level", [0, 1, 2, 5, sp.Rational(7, 3)])
    def test_inverse(self, level):
        assert sp.simplify(k_from_c(n2_central_charge(level)) - level) == 0

    def test_poles(self):
        with pytest.raises(ValueError):
            n2_central_charge(-2)
        with pytest.raises(ValueError):
            k_from_c(3)

    @pytest.mark.parametrize("level", [0, 1, 2, 5])
    def test_level_reflection(self, level):
        assert n2_koszul_dual_level(n2_koszul_dual_level(level)) == level

    @pytest.mark.parametrize("central_charge", [0, 1, 3, 6])
    def test_central_reflection(self, central_charge):
        assert n2_koszul_dual_c(n2_koszul_dual_c(central_charge)) == central_charge

    @pytest.mark.parametrize("level", [1, 2, 5, sp.Rational(7, 3)])
    def test_reflection_sum(self, level):
        packet = parameter_reflection_check(level)
        assert packet["sum"] == 6
        assert packet["involutive"] is True
        assert packet["interpretation"] == "arithmetic reflection candidate"


class TestOpenModularLane:
    @pytest.mark.parametrize(
        ("function", "args"),
        [
            (kappa_n2_correct, (1,)),
            (kappa_n2_from_k, (1,)),
            (kappa_n2_wrong, (1,)),
            (kappa_sl2, (1,)),
            (kappa_fermion_pair, ()),
            (kappa_u1_denominator, (1,)),
            (complementarity_sum, (1,)),
            (sigma_n2, (1,)),
        ],
    )
    def test_numeric_invariant_calls_fail_loudly(self, function, args):
        with pytest.raises(OpenN2InvariantError):
            function(*args)

    def test_coset_packet(self):
        packet = coset_decomposition(2)
        assert packet["central_charge"] == sp.Rational(3, 2)
        assert packet["kappa_coset"] is None
        assert packet["status"] == "open modular comparison"

    def test_status_packet(self):
        packet = n2_modular_status()
        assert packet["status"] == "open"
        assert packet["kappa"] is None
        assert packet["K_kappa"] is None
        assert packet["anomaly_ratio"] is None

    def test_auxiliary_reports_stop_before_kappa(self):
        for packet in (
            discrepancy(1),
            discrepancy_symbolic(),
            sl2_naive_vs_correct(1),
            wrong_duality_check(1),
        ):
            assert packet.get("kappa", packet.get("kappa_coset")) is None
        assert F1_values()["values"] is None


def test_resolution_report() -> None:
    report = verify_resolution()
    assert report["all_exact_checks_pass"] is True
    assert all(report["exact_parameter_checks"].values())
    assert report["modular_status"]["status"] == "open"
