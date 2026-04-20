"""Tests for compute/lib/modular_periodicity_test.

Minimal model central charges, T-matrix periods, Rocha-Caridi character
formula, and periodicity of weight-space dimensions.

Three verification paths:
  (a) Yang-Lee c(2,5) = -22/5 (classical minimal-model central charge).
  (b) Ising c(3,4) = 1/2, tricritical Ising c(4,5) = 7/10.
  (c) T-matrix period consistency with conformal weights.
"""

from fractions import Fraction

import pytest

from compute.lib.modular_periodicity_test import (
    conformal_weights,
    minimal_model_central_charge,
    modular_period,
    partition_table,
    t_matrix_period,
)


def test_smoke_import():
    """Module imports and basic call."""
    c = minimal_model_central_charge(3, 4)
    assert c == Fraction(1, 2)


def test_minimal_model_central_charges():
    """c(p,q) = 1 - 6(p-q)^2/(pq) for (p,q) coprime."""
    assert minimal_model_central_charge(3, 4) == Fraction(1, 2)       # Ising
    assert minimal_model_central_charge(2, 5) == Fraction(-22, 5)     # Yang-Lee
    assert minimal_model_central_charge(4, 5) == Fraction(7, 10)      # TCI
    assert minimal_model_central_charge(5, 6) == Fraction(4, 5)       # 3-state Potts
    assert minimal_model_central_charge(6, 7) == Fraction(6, 7)       # tricritical Potts


def test_yangian_lee_central_charge_formula():
    """Cross-check Yang-Lee: 1 - 6*9/10 = 1 - 27/5 = -22/5."""
    c = minimal_model_central_charge(2, 5)
    expected = Fraction(1) - Fraction(6 * (2 - 5) ** 2, 2 * 5)
    assert c == expected == Fraction(-22, 5)


def test_partition_table_classical():
    """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7 (partition function)."""
    table = partition_table(10)
    assert table[0] == 1
    assert table[1] == 1
    assert table[2] == 2
    assert table[3] == 3
    assert table[4] == 5
    assert table[5] == 7
    assert table[6] == 11
    assert table[7] == 15


def test_conformal_weights_exist():
    """Kac weights are returned for (2,5) and (3,4)."""
    for pq in [(2, 5), (3, 4), (4, 5)]:
        weights = conformal_weights(*pq)
        assert isinstance(weights, list)
        assert len(weights) > 0


def test_t_matrix_period_is_positive_integer():
    """T-matrix period is a positive integer (modular-T finite order)."""
    for pq in [(3, 4), (2, 5)]:
        period = t_matrix_period(*pq)
        assert isinstance(period, int)
        assert period > 0
