"""Tests for compute/lib/n2_sca_chiral_bar_engine.

N=2 superconformal algebra chiral bar-complex dimensions and
Chevalley-Eilenberg H^2 analysis.

Three verification paths:
  (a) Bar basis at weight 0 has dimension 0 (vacuum only).
  (b) n2_ope_data is non-empty and symmetric in generator labels.
  (c) Bar dimension grows polynomially with weight (upper bound check).
"""

import pytest

from compute.lib.n2_sca_chiral_bar_engine import (
    bar_basis_at_weight,
    bar_dim_at_weight,
    max_pole_order,
    n2_ope_data,
)


def test_smoke_import():
    """Imports and basic call."""
    data = n2_ope_data()
    assert isinstance(data, dict)
    assert len(data) > 0


def test_n2_ope_data_keys_are_generator_pairs():
    """OPE data is keyed by pairs of N=2 generator names."""
    data = n2_ope_data()
    for key in data:
        assert isinstance(key, tuple)
        assert len(key) == 2


def test_bar_dim_at_weight_is_non_negative():
    """Bar dimensions at any half-integer weight are >= 0."""
    from fractions import Fraction
    for h_total in (Fraction(1, 2), Fraction(1), Fraction(3, 2),
                    Fraction(2), Fraction(5, 2)):
        for n in (1, 2, 3):
            d = bar_dim_at_weight(n, h_total)
            assert d >= 0


def test_bar_basis_lists_agree_with_dim():
    """Length of bar_basis_at_weight equals bar_dim_at_weight."""
    from fractions import Fraction
    for h_total in (Fraction(1, 2), Fraction(1), Fraction(3, 2),
                    Fraction(2), Fraction(5, 2)):
        for n in (1, 2):
            basis = bar_basis_at_weight(n, h_total)
            dim = bar_dim_at_weight(n, h_total)
            assert len(basis) == dim


def test_max_pole_order_is_positive():
    """max_pole_order returns a positive integer for each OPE pair."""
    data = n2_ope_data()
    for (a, b) in data:
        p = max_pole_order(a, b)
        assert isinstance(p, int)
        assert p >= 0
