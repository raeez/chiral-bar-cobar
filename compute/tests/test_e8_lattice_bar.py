"""Tests for compute/lib/e8_lattice_bar.py -- E_8 lattice bar complex.

Non-trivial identities tested:
  (i)   c_{E_8}(k=1) = 248/31 -- central charge of V_{E_8}.
  (ii)  complementarity sum c + c' = 2*dim(E_8) = 496 for Koszul dual KM.
  (iii) nonzero differential count at degree 2 = 15600
        = 1920 (Cartan-root) + 13440 (root-root inner product -1) + 240 (opposites).
  (iv)  E_8 root system data: 240 roots, 8-rank, Coxeter h = h^vee = 30.
"""

from __future__ import annotations

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.e8_lattice_bar import (
    e8_central_charge,
    e8_complementarity_sum,
    e8_curvature,
    e8_dual_level,
    e8_generator_count,
    e8_koszul_acyclic,
    e8_lattice_self_dual,
    e8_nonzero_diff_count,
    E8_DATA,
)


def test_smoke_imports_and_data():
    """Smoke: E_8 data constants are as stated (dim=248, rank=8, 240 roots, h=30)."""
    assert E8_DATA["dim"] == 248
    assert E8_DATA["rank"] == 8
    assert E8_DATA["n_roots"] == 240
    assert E8_DATA["h"] == 30
    assert E8_DATA["h_dual"] == 30


def test_central_charge_at_level_one():
    """c(V_{E_8}, k=1) = 248/31."""
    c = e8_central_charge(k=1)
    assert c == Rational(248, 31)


def test_central_charge_symbolic_formula():
    """c(V_{E_8}, k) = 248k/(k+30) as symbolic function of k."""
    k = Symbol('k')
    c = e8_central_charge(k)
    # c should simplify to 248k/(k+30)
    target = Rational(248) * k / (k + 30)
    assert simplify(c - target) == 0


def test_complementarity_sum_equals_2_dim():
    """c + c' = 2*dim(E_8) = 496 for KM Koszul dual pair."""
    assert e8_complementarity_sum() == 496
    assert e8_complementarity_sum() == 2 * E8_DATA["dim"]


def test_dual_level_at_k_one():
    """k' = -k - 2h^vee. At k=1: k' = -1 - 60 = -61."""
    assert e8_dual_level(k=1) == -61


def test_nonzero_diff_count_deg2():
    """Total nonzero differential count at degree 2 is 15600 = 1920+13440+240."""
    assert e8_nonzero_diff_count() == 1920 + 13440 + 240
    assert e8_nonzero_diff_count() == 15600


def test_generator_count_sums_to_dim():
    """Cartan + vertex ops = dim(E_8) = 248."""
    g = e8_generator_count()
    assert g["cartan"] + g["vertex_operators"] == g["total"]
    assert g["total"] == 248


def test_curvature_at_level_one():
    """m_0 = (k+h^vee)/(2h^vee) * kappa. At k=1: 31/60."""
    m = e8_curvature(k=1)
    assert m == Rational(31, 60)


def test_lattice_self_dual_and_koszul_acyclic():
    """E_8 lattice is Koszul self-dual (unimodular) and the complex is acyclic."""
    assert e8_lattice_self_dual() is True
    ka = e8_koszul_acyclic()
    assert ka["acyclic"] is True
