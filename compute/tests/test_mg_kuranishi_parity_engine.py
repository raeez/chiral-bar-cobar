"""Tests for compute/lib/mg_kuranishi_parity_engine.py -- cyclic cohomology at g=0,1,2.

Non-trivial identities tested:
  (i)   dim H^2_cyc(W_3) = 1 at genus 0, 1, 2 (algebraic-family-rigidity).
  (ii)  Z_2 parity W -> -W is INTACT at genera 0, 1 but BROKEN at genus 2 for
        mixed-channel contributions.
  (iii) Heisenberg (single generator, weight 1): parity intact all genera.
  (iv)  Virasoro (single generator, weight 2): parity intact all genera.
"""

from __future__ import annotations

from compute.lib.mg_kuranishi_parity_engine import (
    heisenberg_cyclic_cohomology_genus2,
    virasoro_cyclic_cohomology_genus2,
    w3_cyclic_cohomology_genus0,
    w3_cyclic_cohomology_genus1,
    w3_cyclic_cohomology_genus2,
)


def test_smoke_w3_genus0():
    """Smoke: W_3 at genus 0 -- H^2_cyc = 1."""
    data = w3_cyclic_cohomology_genus0()
    assert data.algebra_name == "W_3"
    assert data.h2 == 1
    assert data.parity_grading_intact is True


def test_w3_genus1_still_rigid():
    """At genus 1: dim H^2_cyc = 1 (algebraic-family-rigidity, genus-independent)."""
    data = w3_cyclic_cohomology_genus1()
    assert data.h2 == 1
    assert data.h1 == 1
    assert data.parity_grading_intact is True


def test_w3_genus2_parity_broken():
    """At genus 2: dim H^2 = 1 still, BUT Z_2 parity broken for cross-channel terms."""
    data = w3_cyclic_cohomology_genus2()
    assert data.h2 == 1
    # Parity BROKEN at genus 2 (multi-edge graphs admit even-W-count mixed channels)
    assert data.parity_grading_intact is False


def test_heisenberg_single_generator_parity_all_genera():
    """Heisenberg (single weight-1 generator): no mixed channels at any genus."""
    data = heisenberg_cyclic_cohomology_genus2()
    assert data.algebra_name == "Heisenberg"
    assert data.h2 == 1
    assert data.parity_grading_intact is True


def test_virasoro_single_generator_parity_all_genera():
    """Virasoro (single weight-2 generator): uniform-weight lane, no mixed channels."""
    data = virasoro_cyclic_cohomology_genus2()
    assert data.algebra_name == "Virasoro"
    assert data.h2 == 1
    assert data.parity_grading_intact is True


def test_w3_generator_weights_are_2_and_3():
    """W_3 has generators at weights 2 (T) and 3 (W)."""
    g0 = w3_cyclic_cohomology_genus0()
    assert g0.generator_weights == (2, 3)
    g2 = w3_cyclic_cohomology_genus2()
    assert g2.generator_weights == (2, 3)


def test_lie_symmetry_consistency():
    """W_3 has sl_3 Lie symmetry; Heisenberg has u(1); Virasoro has no Lie factor."""
    assert w3_cyclic_cohomology_genus0().lie_symmetry == "sl_3"
    assert heisenberg_cyclic_cohomology_genus2().lie_symmetry == "u(1)"
    assert virasoro_cyclic_cohomology_genus2().lie_symmetry is None
