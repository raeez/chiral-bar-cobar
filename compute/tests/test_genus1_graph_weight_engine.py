r"""
Tests for genus1_graph_weight_engine.py — weight bounds for shadow weight bound.

GRADING: Cohomological, |d| = +1.
"""

import pytest
from compute.lib.genus1_graph_weight_engine import (
    enumerate_genus1_graphs,
    weight_bound_analysis,
    shadow_multiplicativity_theorem_data,
    cusp_form_dimension,
    modular_form_dimension,
)


class TestStableGraphEnumeration:
    """Verify stable graph enumeration at genus 1."""

    def test_no_graphs_at_r0(self):
        """No stable graphs at (1, 0)."""
        graphs = enumerate_genus1_graphs(0)
        assert len(graphs) == 0

    def test_two_graphs_at_r1(self):
        """Two stable graphs at (1, 1)."""
        graphs = enumerate_genus1_graphs(1)
        assert len(graphs) == 2

    def test_all_stable(self):
        """All enumerated graphs are stable."""
        for r in range(0, 7):
            for g in enumerate_genus1_graphs(r):
                assert g.is_stable, f"Unstable graph at r={r}: {g.description}"

    def test_all_genus_correct(self):
        """All enumerated graphs satisfy the genus formula."""
        for r in range(0, 7):
            for g in enumerate_genus1_graphs(r):
                assert g.genus_check, f"Genus check failed at r={r}: {g.description}"

    def test_graph_count_increases(self):
        """Graph count increases with arity (structural)."""
        counts = [len(enumerate_genus1_graphs(r)) for r in range(1, 7)]
        for i in range(len(counts) - 1):
            assert counts[i] <= counts[i + 1]


class TestWeightBound:
    """Verify the weight bound 2|E| <= 2r."""

    def test_weight_bound_all_arities(self):
        """Weight <= 2r for all stable graphs at (1, r) for r <= 7."""
        wb = weight_bound_analysis(max_legs=7)
        for r in range(1, 8):
            assert wb[r]['weight_bound_2r'], f"Weight bound fails at r={r}"

    def test_max_weight_at_r5(self):
        """Maximum weight at r=5 is 10."""
        wb = weight_bound_analysis(max_legs=5)
        assert wb[5]['max_weight'] == 10

    def test_max_weight_at_r6(self):
        """Maximum weight at r=6 is 12 (critical arity)."""
        wb = weight_bound_analysis(max_legs=6)
        assert wb[6]['max_weight'] == 12

    def test_weights_are_even(self):
        """All modular weights are even (weight-2 propagators)."""
        wb = weight_bound_analysis(max_legs=7)
        for r in range(1, 8):
            for w in wb[r]['weights']:
                assert w % 2 == 0, f"Odd weight {w} at r={r}"


class TestCuspFormDimension:
    """Verify cusp form dimensions for SL(2,Z)."""

    def test_no_cusp_forms_below_12(self):
        """dim S_k = 0 for k < 12."""
        for k in range(0, 12, 2):
            assert cusp_form_dimension(k) == 0, f"S_{k} should be 0"

    def test_delta_at_weight_12(self):
        """dim S_12 = 1 (Ramanujan Delta)."""
        assert cusp_form_dimension(12) == 1

    def test_no_cusp_at_weight_14(self):
        """dim S_14 = 0."""
        assert cusp_form_dimension(14) == 0

    def test_cusp_at_weight_16(self):
        """dim S_16 = 1."""
        assert cusp_form_dimension(16) == 1

    def test_cusp_at_weight_24(self):
        """dim S_24 = 2."""
        assert cusp_form_dimension(24) == 2

    def test_odd_weight_zero(self):
        """dim S_k = 0 for all odd k."""
        for k in range(1, 30, 2):
            assert cusp_form_dimension(k) == 0


class TestModularFormDimension:
    """Verify modular form dimensions."""

    def test_m0(self):
        assert modular_form_dimension(0) == 1

    def test_m2(self):
        """No holomorphic weight-2 forms for SL(2,Z)."""
        assert modular_form_dimension(2) == 0

    def test_m4(self):
        assert modular_form_dimension(4) == 1

    def test_m12(self):
        """M_12 = span{E_12, Delta}: dim = 2."""
        assert modular_form_dimension(12) == 2


class TestShadowWeightBound:
    """Verify the shadow weight bound data."""

    def test_automatic_range(self):
        """Automatic multiplicativity at arities 1-5."""
        data = shadow_multiplicativity_theorem_data(max_arity=7)
        assert data['automatic_multiplicativity_range'] == [1, 2, 3, 4, 5]

    def test_critical_arity_is_6(self):
        """First cusp forms at arity 6."""
        data = shadow_multiplicativity_theorem_data(max_arity=7)
        assert data['critical_arity'] == 6

    def test_no_cusp_forms_below_critical(self):
        """All arities below critical have no cusp forms."""
        data = shadow_multiplicativity_theorem_data(max_arity=7)
        for r in range(1, 6):
            assert data['arity_data'][r]['cusp_form_dim'] == 0

    def test_cusp_forms_at_critical(self):
        """Cusp forms appear at critical arity."""
        data = shadow_multiplicativity_theorem_data(max_arity=7)
        assert data['arity_data'][6]['cusp_form_dim'] == 1

    def test_weight_bound_verified_all(self):
        """Weight bound 2r verified at all arities."""
        data = shadow_multiplicativity_theorem_data(max_arity=7)
        for r, entry in data['arity_data'].items():
            if entry['num_graphs'] > 0:
                assert entry['max_weight'] <= 2 * r


class TestCrossFamilyConsistency:
    """Cross-check: weight bounds are structural, not family-specific (AP10)."""

    def test_weight_independent_of_shadow_data(self):
        """Modular weight depends only on graph topology, not shadow coefficients.
        This is structural: the weight is 2|E|, independent of S_j values."""
        # The weight bound is 2|E| = 2|V| (for h^1=1) or 2(|V|-1) (for h^1=0).
        # Both are determined by graph topology alone.
        wb = weight_bound_analysis(max_legs=5)
        for r in range(1, 6):
            for g in wb[r].get('graphs', []):
                assert g.modular_weight == 2 * g.num_edges

    def test_cusp_threshold_universal(self):
        """The cusp form threshold weight 12 is universal (SL(2,Z) structure)."""
        # This verifies that the Ramanujan Delta is the first cusp form
        # for ALL representations of SL(2,Z), not just for specific families.
        for k in range(2, 12, 2):
            assert cusp_form_dimension(k) == 0
        assert cusp_form_dimension(12) == 1
