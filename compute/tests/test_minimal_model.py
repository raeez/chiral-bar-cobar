"""Tests for minimal model bar complexes."""

import pytest
from sympy import Rational

from compute.lib.minimal_model_bar import (
    minimal_model_c,
    MINIMAL_MODELS,
    ising_bar_data,
    ising_genus1_bar,
    tricritical_ising_data,
    three_state_potts_data,
    minimal_model_complementarity,
    verify_minimal_models,
)


class TestCentralCharges:
    def test_trivial(self):
        assert minimal_model_c(3, 2) == 0

    def test_ising(self):
        assert minimal_model_c(4, 3) == Rational(1, 2)

    def test_tricritical_ising(self):
        assert minimal_model_c(5, 4) == Rational(7, 10)

    def test_three_state_potts(self):
        assert minimal_model_c(6, 5) == Rational(4, 5)

    def test_lee_yang(self):
        """Lee-Yang M(5,2): c = 1 - 6*9/10 = 1 - 54/10 = -22/5."""
        assert minimal_model_c(5, 2) == Rational(-22, 5)

    def test_registry(self):
        assert MINIMAL_MODELS["Ising"]["c"] == Rational(1, 2)


class TestIsingBar:
    def test_curvature(self):
        data = ising_bar_data()
        assert data["kappa"] == Rational(1, 4)

    def test_obs_1(self):
        data = ising_bar_data()
        assert data["obs_1"] == Rational(1, 96)

    def test_modules(self):
        data = ising_bar_data()
        assert data["n_modules"] == 3
        assert set(data["modules"]) == {"I", "sigma", "epsilon"}

    def test_conformal_weights(self):
        data = ising_bar_data()
        assert data["conformal_weights"]["sigma"] == Rational(1, 16)
        assert data["conformal_weights"]["epsilon"] == Rational(1, 2)

    def test_fusion_sigma_sigma(self):
        data = ising_bar_data()
        assert set(data["fusion_rules"][("sigma", "sigma")]) == {"I", "epsilon"}


class TestIsingGenus1:
    def test_vacuum(self):
        g1 = ising_genus1_bar()
        assert g1["B_{g=1}(I, I)"]["dim"] == 1

    def test_sigma_sigma(self):
        g1 = ising_genus1_bar()
        assert g1["B_{g=1}(sigma, sigma)"]["dim"] == 2

    def test_sigma_epsilon(self):
        g1 = ising_genus1_bar()
        assert g1["B_{g=1}(sigma, epsilon)"]["dim"] == 1


class TestTricriticalIsing:
    def test_c(self):
        data = tricritical_ising_data()
        assert data["c"] == Rational(7, 10)

    def test_modules(self):
        data = tricritical_ising_data()
        assert data["n_modules"] == 6


class TestComplementarity:
    def test_all_26(self):
        """All minimal models have c + c' = 26."""
        for p, q in [(4, 3), (5, 4), (6, 5)]:
            assert minimal_model_complementarity(p, q) == 26


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_minimal_models().items():
            assert ok, f"Failed: {name}"
