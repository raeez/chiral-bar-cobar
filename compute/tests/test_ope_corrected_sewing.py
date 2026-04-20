"""Tests for compute/lib/ope_corrected_sewing.py -- OPE-level Virasoro sewing.

Non-trivial identities tested:
  (i)   Virasoro OPE: <L_{-2}|L_2 L_{-2}|0> structure const = c/2.
  (ii)  Virasoro quartic contact invariant: Q_Vir = 10/[c(5c+22)]
        (Zamolodchikov Lambda-norm denominator c(5c+22)/10 inverted).
  (iii) Character partition function positivity for Heisenberg weights [1].
"""

from __future__ import annotations

from mpmath import mpc, mpf

from compute.lib.ope_corrected_sewing import (
    character_free_energy,
    character_partition_function,
    ope_correction_quartic_virasoro,
    virasoro_ope_L2L2,
    virasoro_ope_L2L2L2,
)


def test_smoke_virasoro_l2l2():
    """Smoke: <L_{-2}|L_2 L_{-2}|0> = c/2 identity at sample central charge."""
    c = mpf(1)
    assert virasoro_ope_L2L2(c) == c / 2


def test_virasoro_l2l2_at_c_eq_2():
    """At c=2 (2D free boson rank 2): <L_{-2}|L_2 L_{-2}|0> = 1."""
    c = mpf(2)
    assert virasoro_ope_L2L2(c) == mpf(1)


def test_quartic_contact_zamolodchikov():
    """Virasoro quartic contact Q = 10/[c(5c+22)]. At c=1: Q = 10/27."""
    Q = virasoro_ope_L2L2L2(mpf(1))
    expected = mpf(10) / (mpf(1) * (mpf(5) + mpf(22)))
    # 5*1 + 22 = 27
    assert abs(float(Q) - 10.0 / 27.0) < 1e-10


def test_quartic_contact_at_c_critical_26():
    """At c=26 (critical bosonic string): Q = 10/[26*152] = 5/1976."""
    Q = virasoro_ope_L2L2L2(mpf(26))
    expected = 10.0 / (26.0 * (5 * 26 + 22))
    assert abs(float(Q) - expected) < 1e-12


def test_ope_correction_scalar():
    """ope_correction_quartic_virasoro returns Q_contact as scalar prefactor."""
    q = mpf('0.1')
    corr = ope_correction_quartic_virasoro(mpf(1), q, N_terms=20)
    assert abs(float(corr) - 10.0 / 27.0) < 1e-10


def test_character_partition_function_positive():
    """Character Z_A(q) for single weight-1 generator is positive at q<1."""
    q = mpf('0.3')
    Z = character_partition_function([1], q, N_terms=20)
    assert float(Z) > 1.0  # Product of (1-q^m)^{-1} > 1 for 0 < q < 1


def test_character_free_energy_zero_at_q_zero():
    """log Z(q=0) = log(1) = 0 (free energy vanishes at zero nome)."""
    q = mpf('0.001')
    F = character_free_energy([1], q, N_terms=10)
    # Should be small positive (log of something just above 1)
    assert float(F) < 0.01
    assert float(F) > 0
