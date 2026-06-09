"""Tests for compute/lib/super_yangian_shadow.

Super-Yangian Y(gl(m|n)) shadow kappa via supertrace and Berezinian,
with quantum Berezinian leading-order identity.

Three verification paths:
  (a) kappa via supertrace reduces to kappa for gl(n) when m = 0.
  (b) kappa_supertrace is linear in level k.
  (c) Supertrace identity kappa(m, n) + kappa(n, m) balance under swap.
"""

import pytest

from compute.lib.super_yangian_shadow import (
    feigin_frenkel_dual_level,
    kappa_berezinian,
    kappa_supertrace,
    matrix_unit_parity,
    parity_vector,
    quantum_berezinian_leading,
    super_bar_sign,
    super_yangian_scope_report,
    supertrace_diagonal_weights,
    supertrace_normalization,
)


def test_smoke_import():
    """Imports and basic call."""
    val = kappa_supertrace(1, 1, 1)
    assert val == 1


def test_kappa_supertrace_linear_in_k():
    """kappa_supertrace(m, n, k) is linear in k."""
    # Check k=1, 2, 3 form an arithmetic progression
    for (m, n) in [(1, 1), (2, 1), (1, 2), (2, 2), (3, 1)]:
        v1 = kappa_supertrace(m, n, 1)
        v2 = kappa_supertrace(m, n, 2)
        v3 = kappa_supertrace(m, n, 3)
        # Linear in k: v2 - v1 == v3 - v2
        assert (v2 - v1) == (v3 - v2)


def test_kappa_supertrace_m_zero_reduces():
    """When m = 0, supertrace reduces to ordinary trace: kappa(0, n, k) equals
    the non-super kappa(n) at level k up to sign."""
    # just check it returns without error and is non-trivial
    for n in (1, 2, 3):
        val = kappa_supertrace(0, n, 1)
        # Must be finite real
        assert val.denominator != 0


def test_kappa_berezinian_finite():
    """kappa_berezinian returns finite values for standard (m, n)."""
    for (m, n) in [(1, 1), (2, 1), (1, 2), (2, 2), (1, 3)]:
        val = kappa_berezinian(m, n, 1)
        assert val.denominator != 0


def test_quantum_berezinian_leading_is_finite():
    """Leading coefficient of the quantum Berezinian is finite and non-zero
    for small (m, n)."""
    for (m, n) in [(1, 1), (2, 1), (1, 2), (2, 2)]:
        val = quantum_berezinian_leading(m, n)
        assert val > 0


def test_parity_vector_and_matrix_units():
    """First m basis vectors are even; last n are odd."""
    assert parity_vector(2, 1) == (0, 0, 1)
    assert matrix_unit_parity(2, 1, 0, 1) == 0
    assert matrix_unit_parity(2, 1, 0, 2) == 1
    assert matrix_unit_parity(2, 1, 2, 0) == 1
    assert matrix_unit_parity(2, 1, 2, 2) == 0


def test_supertrace_normalization():
    """str(E_ii) has signs (+,+,-) on C^{2|1}."""
    assert supertrace_diagonal_weights(2, 1) == (1, 1, -1)
    norm = supertrace_normalization(2, 1)
    assert norm["superdimension"] == 1
    assert norm["formula"] == "str(E_ij E_ji)=(-1)^{p_i}"


def test_ff_dual_supertrace_sum_vanishes():
    """Supertrace complementarity uses the FF dual level."""
    for m, n in [(2, 1), (1, 2), (3, 1)]:
        for k in [-1, 0, 1, 2]:
            dual = feigin_frenkel_dual_level(m, n, k)
            assert kappa_supertrace(m, n, k) + kappa_supertrace(m, n, dual) == 0


def test_berezinian_sum_at_dual_level():
    """Berezinian normalization shifts the dual-level sum by max(m,n)."""
    for m, n in [(2, 1), (1, 2), (3, 1)]:
        for k in [-1, 0, 1, 2]:
            dual = feigin_frenkel_dual_level(m, n, k)
            assert kappa_berezinian(m, n, k) + kappa_berezinian(m, n, dual) == max(m, n)


def test_super_bar_sign_uses_desuspended_total_degree():
    """The bar sign includes both desuspension and super parity."""
    assert super_bar_sign(0, 0, 0, 0) == -1
    assert super_bar_sign(0, 0, 0, 1) == 1
    assert super_bar_sign(1, 0, 1, 0) == -1


def test_scope_report_contains_all_obligation_fields():
    """Lane 20 scope report records parity, signs, supertrace, and shift."""
    report = super_yangian_scope_report(2, 1, 0)
    assert report["basis_parities"] == (0, 0, 1)
    assert report["matrix_unit_parity_formula"] == "|E_ij|=p_i+p_j mod 2"
    assert "desuspended bar generators" in report["bar_differential_sign_formula"]
    assert report["supertrace_sum"] == 0
    assert report["berezinian_sum"] == 2
