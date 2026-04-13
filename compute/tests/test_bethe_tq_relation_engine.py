import numpy as np

from compute.lib.bethe_tq_relation_engine import (
    a_factor,
    bae_from_tq,
    baxter_q_polynomial,
    d_factor,
    verify_tq_relation,
)


def test_q_polynomial_vanishes_at_bethe_roots():
    lambdas = np.array([0.3, -0.4])
    assert abs(baxter_q_polynomial(0.3, lambdas)) < 1e-12
    assert abs(baxter_q_polynomial(-0.4, lambdas)) < 1e-12


def test_vacuum_tq_relation_uses_real_gamma_shift():
    result = verify_tq_relation(0.5, np.array([]), 4, np.pi / 4)
    assert result["residual"] < 1e-12
    assert abs(result["lhs"] - result["rhs"]) < 1e-12


def test_a_and_d_factors_at_zero():
    gamma = np.pi / 4
    assert abs(a_factor(0.0, 4, gamma) - np.sin(gamma) ** 4) < 1e-12
    assert abs(d_factor(0.0, 4, gamma)) < 1e-12


def test_empty_root_bae_is_trivially_satisfied():
    result = bae_from_tq(np.array([]), 4, np.pi / 4)
    assert result["all_satisfied"] is True
    assert result["max_residual"] == 0
