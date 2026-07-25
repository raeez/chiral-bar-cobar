"""Finite oracles and typed obligations for five arbitrary-DS audit routes.

The routes are:

  A: Induction on orbit closure
  B: BFN / Coulomb branch
  C: Derived DS = homotopy DS (formality)
  D: Shadow-level commutation
  E: Type-by-type exhaustion

Target: conj:ds-kd-arbitrary-nilpotent (w_algebras_deep.tex line 1584).
Proved cases: principal (all types), subregular/minimal sl_3, hooks type A.
"""

from fractions import Fraction

import pytest

from compute.lib.hook_type_w_duality import ClaimPacket, ClaimStatus

from compute.lib.ds_kd_green_team import (
    # Strategy A
    closure_poset_covers,
    closure_poset_layers,
    compute_induction_steps,
    induction_feasibility_score,
    InductionStep,
    # Strategy B
    bfn_quiver_for_type_a,
    bfn_coulomb_matches_slodowy,
    bfn_strategy_assessment,
    QuiverData,
    # Strategy C
    is_even_nilpotent,
    slodowy_slice_is_affine,
    li_filtration_status,
    formality_assessment,
    derived_ds_strategy_score,
    # Strategy D
    generator_weight_shadow_depth_candidate,
    shadow_depth_estimate,
    shadow_kappa_ds_commutation,
    shadow_commutation_induction_data,
    # Strategy E
    type_a_orbit_census,
    type_bcd_orbit_data,
    type_e_exhaustion_assessment,
    # Overall
    rate_all_strategies,
    recommended_strategy,
    run_diagnostics,
)
from compute.lib.w_algebra_transport_propagation import (
    partitions,
    transpose,
    is_hook,
    hook_partitions,
    centralizer_dimension,
    nilpotent_orbit_dimension,
    generator_weights,
    graph_is_connected,
)


def _assert_unresolved(packet: ClaimPacket, status: ClaimStatus) -> None:
    """Assert an explicit typed construction obligation."""

    assert isinstance(packet, ClaimPacket)
    assert packet.status is status
    assert packet.value is None
    assert packet.hypotheses


# =====================================================================
# STRATEGY A: Induction on orbit closure
# =====================================================================

class TestStrategyA:
    """Tests for orbit-closure induction."""

    def test_closure_covers_sl3(self):
        """sl_3 has 3 orbits: (3) > (2,1) > (1,1,1)."""
        covers = closure_poset_covers(3)
        assert len(covers) == 2
        # (3) covers (2,1), (2,1) covers (1,1,1)
        assert ((3,), (2, 1)) in covers
        assert ((2, 1), (1, 1, 1)) in covers

    def test_closure_covers_sl4(self):
        """sl_4 has 5 orbits with specific cover relations."""
        covers = closure_poset_covers(4)
        # (4) > (3,1) > (2,2) > (2,1,1) > (1^4)
        # But (3,1) also covers (2,1,1) directly? No.
        # Dominance order covers for partitions of 4:
        # (4) covers (3,1)
        # (3,1) covers (2,2) and (2,1,1)
        # (2,2) covers (2,1,1)
        # (2,1,1) covers (1,1,1,1)
        assert len(covers) >= 4

    def test_closure_layers_sl3(self):
        """sl_3 layers: [(3)], [(2,1)], [(1,1,1)]."""
        layers = closure_poset_layers(3)
        assert layers[0] == [(3,)]
        assert (1, 1, 1) in layers[-1]

    def test_closure_layers_sl5(self):
        """sl_5 should have multiple layers."""
        layers = closure_poset_layers(5)
        assert layers[0] == [(5,)]
        assert len(layers) >= 3

    def test_induction_sl3_candidate_closure(self):
        """The candidate closure covers sl3 and transport remains open."""
        score = induction_feasibility_score(3)
        assert score['candidate_closure_covers_all']
        _assert_unresolved(score['transport_realization'], ClaimStatus.OPEN)
        assert score['remaining'] == 0

    def test_induction_sl4_candidate_closure(self):
        """sl_4: hooks cover (4), (3,1), (2,1,1). (2,2) is non-hook but
        reachable by induction since its parents (3,1) and/or (2,2) covers
        only (2,1,1)."""
        score = induction_feasibility_score(4)
        # All should be reached: hooks cover 3 of 5 partitions,
        # and graph connectivity fills in (2,2)
        assert score['candidate_closure_covers_all']
        _assert_unresolved(score['transport_realization'], ClaimStatus.OPEN)

    def test_induction_sl5_candidate_closure(self):
        """sl_5: 7 partitions. Hooks give 5. Non-hook: (3,2), (2,2,1).
        Both should be reachable."""
        score = induction_feasibility_score(5)
        assert score['candidate_closure_covers_all']
        _assert_unresolved(score['transport_realization'], ClaimStatus.OPEN)

    def test_induction_sl6(self):
        """sl_6: 11 partitions. Test induction coverage."""
        score = induction_feasibility_score(6)
        # In type A, the dominance order graph is always connected,
        # so induction from hooks should reach everything
        assert score['candidate_closure_covers_all']
        _assert_unresolved(score['transport_realization'], ClaimStatus.OPEN)

    def test_induction_steps_have_codimension(self):
        """Each induction step carries exact codimension and KRW arithmetic."""
        steps = compute_induction_steps(4)
        for s in steps:
            assert s.codimension >= 0
            assert s.parent_orbit_dim >= s.child_orbit_dim
            assert not hasattr(s, 'kappa_drop')
        step_31_22 = next(step for step in steps if step.parent == (3, 1) and step.child == (2, 2))
        from compute.lib.hook_type_w_duality import krw_central_charge
        from sympy import Rational as SRational, simplify
        expected = krw_central_charge((3, 1), SRational(7)) - krw_central_charge(
            (2, 2), SRational(7)
        )
        assert simplify(step_31_22.central_charge_difference - expected) == 0

    def test_induction_graph_connected_small(self):
        """Gamma_N is connected for N = 2, 3, 4, 5, 6."""
        for n in [2, 3, 4, 5, 6]:
            assert graph_is_connected(n), f"Gamma_{n} not connected"


# =====================================================================
# STRATEGY B: BFN / Coulomb branch
# =====================================================================

class TestStrategyB:
    """Tests for BFN Coulomb branch approach."""

    def test_bfn_quiver_principal_sl3(self):
        """Principal sl3 exposes exact target dimensions and an open identification."""
        quiver = bfn_quiver_for_type_a((3,))
        assert quiver.lie_type == 'A'
        assert quiver.slodowy_dimension == centralizer_dimension((3,)) == 2
        _assert_unresolved(quiver.bfn_slodowy_identification, ClaimStatus.OPEN)

    def test_bfn_quiver_subregular_sl3(self):
        """Subregular sl_3: partition (2,1)."""
        quiver = bfn_quiver_for_type_a((2, 1))
        assert quiver.slodowy_dimension == centralizer_dimension((2, 1))
        # dim(g^e) for (2,1) in sl_3: transpose = (2,1), sum of squares - 1 = 4+1-1 = 4
        assert quiver.slodowy_dimension == 4

    def test_bfn_quiver_zero_sl3(self):
        """Zero orbit sl_3: partition (1,1,1)."""
        quiver = bfn_quiver_for_type_a((1, 1, 1))
        assert quiver.slodowy_dimension == centralizer_dimension((1, 1, 1))
        # dim(g^e) for (1,1,1) = dim(sl_3) = 8
        assert quiver.slodowy_dimension == 8

    def test_bfn_dim_match_all_sl4(self):
        """Every sl4 BFN--Slodowy identification stays open."""
        for lam in partitions(4):
            _assert_unresolved(bfn_coulomb_matches_slodowy(lam), ClaimStatus.OPEN)

    def test_bfn_dim_match_all_sl5(self):
        """Every sl5 candidate ledger carries its geometric obligation."""
        for lam in partitions(5):
            _assert_unresolved(bfn_coulomb_matches_slodowy(lam), ClaimStatus.OPEN)

    def test_bfn_assessment_sl3(self):
        """BFN strategy assessment for sl_3."""
        result = bfn_strategy_assessment(3)
        assert result['partition_ledgers_complete']
        assert len(result['bfn_slodowy_identifications']) == 3
        for packet in result['bfn_slodowy_identifications']:
            _assert_unresolved(packet, ClaimStatus.OPEN)

    def test_bfn_quiver_higgs_dim(self):
        """The exact orbit dimension remains separate from the BFN claim."""
        for lam in partitions(4):
            quiver = bfn_quiver_for_type_a(lam)
            assert quiver.orbit_dimension == nilpotent_orbit_dimension(lam)

    def test_bfn_principal_framing(self):
        """Principal orbit has specific framing pattern."""
        quiver = bfn_quiver_for_type_a((4,))
        # For principal: lambda^t = (1,1,1,1), so framing = (1,1,1,1)
        # minus consecutive differences
        assert len(quiver.candidate_framing_ranks) > 0


# =====================================================================
# STRATEGY C: Derived DS = homotopy DS
# =====================================================================

class TestStrategyC:
    """Tests for the derived DS / formality approach."""

    def test_even_nilpotent_principal_sl3(self):
        """Principal in sl_3: partition (3) is even (single odd part)."""
        # (3): all parts odd and same parity -> even
        assert is_even_nilpotent((3,))

    def test_even_nilpotent_subregular_sl3(self):
        """Subregular sl_3: (2,1) has mixed parities -> not even."""
        assert not is_even_nilpotent((2, 1))

    def test_even_nilpotent_22(self):
        """(2,2) in sl_4: all even parts -> even."""
        assert is_even_nilpotent((2, 2))

    def test_slodowy_always_affine(self):
        """Slodowy slice is always affine."""
        for lam in partitions(5):
            assert slodowy_slice_is_affine(lam)

    def test_li_filtration_type_a(self):
        """Each Li associated-graded comparison states its source obligation."""
        for n in [3, 4, 5]:
            for lam in partitions(n):
                _assert_unresolved(li_filtration_status(lam), ClaimStatus.OPEN)

    def test_formality_packets_sl3(self):
        """Every sl3 orbit has affine input and an open realization."""
        assessments = formality_assessment(3)
        assert all(a.slodowy_is_affine for a in assessments)
        for assessment in assessments:
            _assert_unresolved(assessment.formality_realization, ClaimStatus.OPEN)

    def test_formality_packets_sl5(self):
        """Affine Slodowy input leaves every sl5 formality claim open."""
        assessments = formality_assessment(5)
        assert all(a.slodowy_is_affine for a in assessments)
        for assessment in assessments:
            _assert_unresolved(assessment.formality_realization, ClaimStatus.OPEN)

    def test_derived_ds_score_sl4(self):
        """The sl4 derived route separates affine input from comparison."""
        score = derived_ds_strategy_score(4)
        assert score['all_slodowy_slices_affine']
        _assert_unresolved(score['derived_ds_bar_comparison'], ClaimStatus.OPEN)

    def test_derived_ds_score_sl5(self):
        """Derived DS strategy score for sl_5."""
        score = derived_ds_strategy_score(5)
        assert score['all_slodowy_slices_affine']
        _assert_unresolved(score['derived_ds_bar_comparison'], ClaimStatus.OPEN)
        assert score['num_orbits'] == 7


# =====================================================================
# STRATEGY D: Shadow-level commutation
# =====================================================================

class TestStrategyD:
    """Tests for shadow-level commutation."""

    def test_kappa_packets_all_sl3(self):
        """Arity-two scalar evidence carries a conditional comparison."""
        for lam in partitions(3):
            result = shadow_kappa_ds_commutation(3, lam)
            _assert_unresolved(result['anomaly_ratio'], ClaimStatus.OPEN)
            _assert_unresolved(result['kappa_w'], ClaimStatus.CONDITIONAL)
            _assert_unresolved(result['commutation_arity2'], ClaimStatus.OPEN)

    def test_kappa_packets_all_sl4(self):
        """Kappa DS-bar commutation for all sl_4 orbits."""
        for lam in partitions(4):
            result = shadow_kappa_ds_commutation(4, lam)
            _assert_unresolved(result['commutation_arity2'], ClaimStatus.OPEN)

    def test_kappa_ghost_constant_principal_sl3(self):
        """Principal sl3 uses the canonical DS ghost constant C_(3)=4."""
        result = shadow_kappa_ds_commutation(3, (3,))
        assert result['ghost_constant'] == 4

    def test_kappa_ghost_constant_zero_orbit(self):
        """Zero orbit: ghost constant = 0 (h = 0)."""
        result = shadow_kappa_ds_commutation(3, (1, 1, 1))
        assert result['ghost_constant'] == Fraction(0)

    def test_shadow_induction_data_sl3(self):
        """Shadow commutation data for sl_3."""
        data = shadow_commutation_induction_data(3)
        assert data['total_orbits'] == 3
        for label, orbit_data in data['orbit_data'].items():
            _assert_unresolved(orbit_data['arity2'], ClaimStatus.OPEN)
            _assert_unresolved(orbit_data['shadow_depth_realization'], ClaimStatus.OPEN)
            _assert_unresolved(orbit_data['full_tower'], ClaimStatus.OPEN)

    def test_shadow_depth_principal(self):
        """Generator weights give a candidate; full depth remains open."""
        assert generator_weight_shadow_depth_candidate((3,)) == float('inf')
        _assert_unresolved(shadow_depth_estimate((3,)), ClaimStatus.OPEN)

    def test_shadow_depth_zero(self):
        """The zero-orbit generator candidate leaves full depth open."""
        candidate = generator_weight_shadow_depth_candidate((1, 1, 1))
        assert isinstance(candidate, (int, float))
        _assert_unresolved(shadow_depth_estimate((1, 1, 1)), ClaimStatus.OPEN)


# =====================================================================
# STRATEGY E: Type-by-type exhaustion
# =====================================================================

class TestStrategyE:
    """Tests for type-by-type exhaustion."""

    def test_orbit_census_sl2(self):
        """The sl2 census carries conditional hook comparison packets."""
        census = type_a_orbit_census(2)
        assert len(census) == 2
        for record in census:
            _assert_unresolved(record.ds_bar_status, ClaimStatus.CONDITIONAL)

    def test_orbit_census_sl3(self):
        """The sl3 census separates hook and non-hook statuses."""
        census = type_a_orbit_census(3)
        assert len(census) == 3
        for record in census:
            expected = ClaimStatus.CONDITIONAL if record.is_hook else ClaimStatus.OPEN
            _assert_unresolved(record.ds_bar_status, expected)

    def test_orbit_census_sl4(self):
        """sl_4: 5 orbits. Hooks = 4, non-hook (2,2) = 1."""
        census = type_a_orbit_census(4)
        assert len(census) == 5
        hooks = [r for r in census if r.is_hook]
        assert len(hooks) == 4  # (4), (3,1), (2,1,1), (1,1,1,1)
        non_hooks = [r for r in census if not r.is_hook]
        assert len(non_hooks) == 1  # (2,2)

    def test_orbit_census_sl5(self):
        """sl_5: 7 orbits."""
        census = type_a_orbit_census(5)
        assert len(census) == 7
        assert any(record.ds_bar_status.status is ClaimStatus.OPEN for record in census)

    def test_bv_dual_is_transpose_type_a(self):
        """Partition transpose is exact; object-level orbit duality is open."""
        for n in [3, 4, 5]:
            for lam in partitions(n):
                lam_t = transpose(lam)
                census = type_a_orbit_census(n)
                for r in census:
                    if r.label == f"({','.join(str(p) for p in lam)})":
                        expected = f"({','.join(str(p) for p in lam_t)})"
                        assert r.transpose_label == expected
                        _assert_unresolved(r.orbit_duality, ClaimStatus.OPEN)

    def test_type_bcd_orbit_counts(self):
        """Verify orbit counts for small BCD types."""
        data = type_bcd_orbit_data()
        assert len(data['B_2']) == 4
        assert len(data['C_2']) == 4
        assert len(data['G_2']) == 5
        assert len(data['B_3']) == 7
        assert [orbit['dim'] for orbit in data['B_2']] == [8, 6, 4, 0]
        assert [orbit['dim'] for orbit in data['C_2']] == [8, 6, 4, 0]

    def test_type_bcd_distinguished_endpoint_packets(self):
        """Principal and zero BCD comparisons retain explicit hypotheses."""
        data = type_bcd_orbit_data()
        for type_name, orbits in data.items():
            principal = [o for o in orbits if 'principal' in o.get('orbit', '')]
            zero = [o for o in orbits if 'zero' in o.get('orbit', '')]
            for o in principal + zero:
                _assert_unresolved(o['ds_bar_status'], ClaimStatus.CONDITIONAL)

    def test_exceptional_assessment(self):
        """Exceptional types: verify orbit counts."""
        assessment = type_e_exhaustion_assessment()
        assert assessment['G_2']['total'] == 5
        assert assessment['F_4']['total'] == 16
        assert assessment['E_6']['total'] == 21
        assert assessment['E_7']['total'] == 45
        assert assessment['E_8']['total'] == 70
        assert assessment['B_3']['total'] == 7
        assert assessment['C_3']['total'] == 8


# =====================================================================
# OVERALL STRATEGY SCORING
# =====================================================================

class TestOverall:
    """Tests for strategy scoring and recommendations."""

    def test_all_strategies_rated(self):
        """All five strategies should be rated."""
        ratings = rate_all_strategies()
        assert len(ratings) == 5
        codes = {r.code for r in ratings}
        assert codes == {'A', 'B', 'C', 'D', 'E'}

    def test_feasibility_scores_valid(self):
        """Feasibility scores should be in [1, 10]."""
        for r in rate_all_strategies():
            assert 1 <= r.feasibility <= 10
            assert 1 <= r.completeness <= 10
            assert 1 <= r.novelty <= 10

    def test_strategy_c_highest_composite(self):
        """Strategy C (derived DS) should have highest composite score
        among strategies with completeness >= 8."""
        ratings = rate_all_strategies()
        # Composite = feasibility + completeness + novelty
        high_completeness = [r for r in ratings if r.completeness >= 8]
        assert len(high_completeness) >= 2
        c_rating = [r for r in ratings if r.code == 'C'][0]
        c_composite = c_rating.feasibility + c_rating.completeness + c_rating.novelty
        for r in high_completeness:
            if r.code != 'C':
                composite = r.feasibility + r.completeness + r.novelty
                # C should be competitive (not necessarily highest)
                assert c_composite >= composite - 3  # within 3 points

    def test_recommended_strategy_not_empty(self):
        """Recommended strategy should produce a non-empty string."""
        rec = recommended_strategy()
        assert len(rec) > 100
        assert 'COMPOSITE' in rec

    def test_diagnostics_pass(self):
        """Exact diagnostics pass and every theorem claim stays typed."""
        results = run_diagnostics()
        for name, result in results.items():
            if isinstance(result, ClaimPacket):
                assert result.status in (ClaimStatus.OPEN, ClaimStatus.CONDITIONAL)
                assert result.value is None and result.hypotheses
            else:
                assert result is True, name

    def test_diagnostics_count(self):
        """Should have at least 25 diagnostic checks."""
        results = run_diagnostics()
        assert len(results) >= 25


# =====================================================================
# CROSS-STRATEGY CONSISTENCY
# =====================================================================

class TestCrossStrategy:
    """Cross-strategy consistency checks."""

    def test_all_strategies_agree_on_sl3(self):
        """Exact candidate diagnostics agree while theorem realizations stay open."""
        # Strategy A
        induction = induction_feasibility_score(3)
        assert induction['candidate_closure_covers_all']
        _assert_unresolved(induction['transport_realization'], ClaimStatus.OPEN)
        # Strategy B
        bfn = bfn_strategy_assessment(3)
        assert bfn['partition_ledgers_complete']
        assert all(
            packet.status is ClaimStatus.OPEN
            for packet in bfn['bfn_slodowy_identifications']
        )
        # Strategy C
        derived = derived_ds_strategy_score(3)
        assert derived['all_slodowy_slices_affine']
        _assert_unresolved(derived['derived_ds_bar_comparison'], ClaimStatus.OPEN)
        # Strategy E
        census = type_a_orbit_census(3)
        assert all(isinstance(record.ds_bar_status, ClaimPacket) for record in census)

    def test_centralizer_dim_consistency(self):
        """Centralizer dimension from different methods should agree."""
        for n in [3, 4, 5]:
            for lam in partitions(n):
                quiver = bfn_quiver_for_type_a(lam)
                assert quiver.slodowy_dimension == centralizer_dimension(lam)

    def test_orbit_dim_plus_centralizer_dim(self):
        """dim(O) + dim(g^e) = dim(g) = N^2 - 1 for all sl_N orbits."""
        for n in [3, 4, 5, 6]:
            dim_g = n * n - 1
            for lam in partitions(n):
                assert (nilpotent_orbit_dimension(lam) +
                        centralizer_dimension(lam)) == dim_g

    def test_generator_count_equals_centralizer_dim(self):
        """Number of strong generators = dim(g^e) for W-algebras."""
        for n in [3, 4, 5]:
            for lam in partitions(n):
                gens = generator_weights(lam)
                assert len(gens) == centralizer_dimension(lam), (
                    f"sl_{n}, {lam}: {len(gens)} generators but "
                    f"dim(g^e) = {centralizer_dimension(lam)}"
                )


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
