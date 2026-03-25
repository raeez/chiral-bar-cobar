"""Tests for compute/lib/pbw_propagation_engine.py.

Key result: MK1 (genus-0 Koszulity) implies MK3 (PBW concentration
at all genera) for CFT-type chiral algebras with positive conformal
grading and unique weight-2 stress tensor.

Three-step proof:
  Step 1: d_coll is curve-independent (regular part has zero residue)
  Step 2: core-enrichment decomposition preserved by d_coll
  Step 3: d_2 = h*id on enrichment kills it on E_3
"""

import pytest
import numpy as np

from compute.lib.pbw_propagation_engine import (
    PropagatorDecomposition,
    CoreEnrichmentDecomposition,
    PBWSpectralSequence,
    HeisenbergGenusgVerification,
    AffineSl2GenusgVerification,
    VirasoroGenusgVerification,
    PBWPropagationTheorem,
    verify_collision_differential_independence,
    verify_enrichment_factorization,
)


class TestPropagatorDecomposition:
    """Szego kernel decomposition at genus g."""

    def test_genus0_no_regular_part(self):
        prop = PropagatorDecomposition(0)
        assert prop.dim_h10 == 0
        assert prop.regular_part_matrix() is None

    def test_singular_residue_always_1(self):
        for g in range(4):
            prop = PropagatorDecomposition(g)
            assert prop.singular_part_residue() == 1

    def test_regular_residue_always_0(self):
        """Key fact: R_g(z,w) is holomorphic at z=w, so residue = 0."""
        for g in range(4):
            prop = PropagatorDecomposition(g)
            assert prop.regular_part_residue() == 0

    def test_curve_independence_for_collisions(self):
        """Step 1: d_coll is curve-independent at every genus."""
        for g in range(4):
            prop = PropagatorDecomposition(g)
            assert prop.propagator_is_curve_independent_for_collisions()

    def test_genus1_period_matrix_shape(self):
        prop = PropagatorDecomposition(1)
        assert prop.period_matrix.shape == (1, 1)

    def test_genus2_regular_part_matrix(self):
        prop = PropagatorDecomposition(2)
        M = prop.regular_part_matrix()
        assert M is not None
        assert M.shape == (2, 2)

    def test_negative_genus_raises(self):
        with pytest.raises(ValueError):
            PropagatorDecomposition(-1)


class TestCoreEnrichmentDecomposition:
    """Core-enrichment decomposition of the genus-g bar complex."""

    def test_genus0_no_enrichment(self):
        d = CoreEnrichmentDecomposition(0, "Heisenberg")
        for h in range(1, 6):
            assert d.enrichment_dim_at_weight(h) == 0

    def test_genus1_enrichment_heisenberg(self):
        """Enrichment at genus 1: dim(M_h) * 1 = p(h) for Heisenberg."""
        d = CoreEnrichmentDecomposition(1, "Heisenberg")
        # p(1)=1, p(2)=2, p(3)=3, p(4)=5
        assert d.enrichment_dim_at_weight(1) == 1
        assert d.enrichment_dim_at_weight(2) == 2
        assert d.enrichment_dim_at_weight(3) == 3

    def test_genus2_enrichment_doubles(self):
        """Enrichment scales linearly with genus."""
        d1 = CoreEnrichmentDecomposition(1, "Heisenberg")
        d2 = CoreEnrichmentDecomposition(2, "Heisenberg")
        for h in range(1, 5):
            assert d2.enrichment_dim_at_weight(h) == 2 * d1.enrichment_dim_at_weight(h)

    def test_d_coll_preserves_both(self):
        d = CoreEnrichmentDecomposition(2, "Heisenberg")
        assert d.d_coll_preserves_core()
        assert d.d_coll_preserves_enrichment()
        assert d.no_mixed_terms()


class TestPBWSpectralSequence:
    """PBW spectral sequence: d_2 = h*id kills enrichment."""

    def test_d2_eigenvalue_equals_weight(self):
        ss = PBWSpectralSequence(1, "Heisenberg")
        for h in range(1, 8):
            assert ss.d2_eigenvalue_on_enrichment(h) == h

    def test_d2_is_isomorphism_for_positive_weight(self):
        ss = PBWSpectralSequence(1, "Heisenberg")
        for h in range(1, 8):
            assert ss.d2_is_isomorphism_on_enrichment(h)

    def test_e3_enrichment_zero(self):
        """E_3(enrichment) = 0 because d_2 is an isomorphism."""
        ss = PBWSpectralSequence(2, "Heisenberg")
        for h in range(1, 8):
            assert ss.e3_enrichment_dim(h) == 0

    def test_e_infinity_equals_genus0(self):
        """E_infty(g) = E_infty(0) for all g."""
        for g in range(3):
            ss = PBWSpectralSequence(g, "Heisenberg")
            assert ss.e_infinity_genus_g_equals_genus_0(max_weight=6)


class TestHeisenbergVerification:
    """Explicit PBW propagation for Heisenberg at various genera."""

    def test_core_matches_genus0(self):
        v = HeisenbergGenusgVerification(2)
        for deg in range(1, 5):
            ok, core, g0 = v.verify_core_dimension(deg)
            assert ok, f"Core mismatch at degree {deg}: {core} vs {g0}"

    def test_enrichment_dimension(self):
        v = HeisenbergGenusgVerification(1)
        ok, actual, m_h, expected = v.verify_enrichment_dimension(3)
        assert ok

    def test_d2_kills_enrichment(self):
        v = HeisenbergGenusgVerification(1)
        for h in range(1, 5):
            ok, eigenval, ker = v.verify_d2_kills_enrichment(h)
            assert ok

    def test_e_infinity_equality(self):
        v = HeisenbergGenusgVerification(2)
        assert v.verify_e_infinity_equality(max_degree=6)


class TestPBWPropagationTheorem:
    """Full theorem: MK1 + positive grading + stress tensor => MK3."""

    @pytest.mark.parametrize("algebra", ["Heisenberg", "sl2", "Virasoro"])
    def test_mk1_implies_mk3(self, algebra):
        """KEY RESULT: MK1 implies MK3 for all standard families."""
        thm = PBWPropagationTheorem(algebra, max_genus=2)
        assert thm.verify_mk1_implies_mk3(max_weight=6)

    def test_step1_all_genera(self):
        thm = PBWPropagationTheorem("Heisenberg", max_genus=3)
        results = thm.verify_step1()
        assert all(results.values())

    def test_step2_decomposition(self):
        thm = PBWPropagationTheorem("Heisenberg", max_genus=2)
        results = thm.verify_step2()
        for g, props in results.items():
            for prop_name, ok in props.items():
                assert ok, f"Step 2 failed at genus {g}: {prop_name}"

    def test_step3_enrichment_killing(self):
        thm = PBWPropagationTheorem("Heisenberg", max_genus=2)
        results = thm.verify_step3()
        for g, ok in results.items():
            if g > 0:
                assert ok, f"Step 3 failed at genus {g}"


class TestCollisionDifferentialIndependence:
    """d_coll is the same operator at all genera."""

    def test_independence_up_to_genus3(self):
        results = verify_collision_differential_independence(max_genus=3)
        assert all(results.values())


class TestEnrichmentFactorization:
    """dim(B-bar_enr^{*,h}) = dim(M_h) * g."""

    @pytest.mark.parametrize("algebra", ["Heisenberg", "sl2", "Virasoro"])
    def test_factorization_genus1(self, algebra):
        results = verify_enrichment_factorization(1, algebra, max_weight=5)
        for h, (ok, actual, expected) in results.items():
            assert ok, f"{algebra} g=1 h={h}: {actual} != {expected}"
