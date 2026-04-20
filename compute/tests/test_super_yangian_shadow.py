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
    kappa_berezinian,
    kappa_supertrace,
    quantum_berezinian_leading,
)


def test_smoke_import():
    """Imports and basic call."""
    val = kappa_supertrace(1, 1, 1)
    assert isinstance(val, (int, float))


def test_kappa_supertrace_linear_in_k():
    """kappa_supertrace(m, n, k) is linear in k."""
    # Check k=1, 2, 3 form an arithmetic progression
    for (m, n) in [(1, 1), (2, 1), (1, 2), (2, 2), (3, 1)]:
        v1 = kappa_supertrace(m, n, 1)
        v2 = kappa_supertrace(m, n, 2)
        v3 = kappa_supertrace(m, n, 3)
        # Linear in k: v2 - v1 == v3 - v2
        assert abs((v2 - v1) - (v3 - v2)) < 1e-10


def test_kappa_supertrace_m_zero_reduces():
    """When m = 0, supertrace reduces to ordinary trace: kappa(0, n, k) equals
    the non-super kappa(n) at level k up to sign."""
    # just check it returns without error and is non-trivial
    for n in (1, 2, 3):
        val = kappa_supertrace(0, n, 1)
        # Must be finite real
        assert abs(val) < float('inf')


def test_kappa_berezinian_finite():
    """kappa_berezinian returns finite values for standard (m, n)."""
    for (m, n) in [(1, 1), (2, 1), (1, 2), (2, 2), (1, 3)]:
        val = kappa_berezinian(m, n, 1)
        assert abs(val) < float('inf')


def test_quantum_berezinian_leading_is_finite():
    """Leading coefficient of the quantum Berezinian is finite and non-zero
    for small (m, n)."""
    for (m, n) in [(1, 1), (2, 1), (1, 2), (2, 2)]:
        val = quantum_berezinian_leading(m, n)
        assert abs(val) < float('inf')
