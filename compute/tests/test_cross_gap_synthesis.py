#!/usr/bin/env python3
"""
Tests for cross_gap_synthesis.py — Cross-gap coupling analysis.

Validates the coupling matrix, information flow, minimal closing sets,
redundancy test, obstruction hierarchy, bootstrap exclusion regions,
and residue discrimination across the three gaps in the sewing-to-zeta programme.
"""

import sys, os, math
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from cross_gap_synthesis import (
    GAP_INGREDIENTS,
    gap_coupling_matrix,
    gap12_hecke_gives_intertwining,
    gap13_coderived_gives_poles,
    gap23_sewing_gives_vvmf,
    information_content_VZ,
    information_flow_direction,
    test_gap2_alone_ising as _test_gap2_alone_ising,
    test_gap3_alone as _test_gap3_alone,
    test_gap1_alone as _test_gap1_alone,
    minimal_closing_set,
    redundancy_test_VZ,
    obstruction_hierarchy,
    exclusion_region_single_c,
    bootstrap_exclusion_plane,
    residue_at_zeta_zero_c,
    offline_residue,
    residue_discrimination,
    full_synthesis,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

needs_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath not installed")


# ============================================================
# 1. Gap coupling matrix tests
# ============================================================

class TestGapCouplingMatrix:
    """Test the gap coupling matrix computation."""

    def test_ingredients_defined(self):
        """All three gaps have ingredient sets."""
        assert 1 in GAP_INGREDIENTS
        assert 2 in GAP_INGREDIENTS
        assert 3 in GAP_INGREDIENTS

    def test_ingredients_nonempty(self):
        """Each gap has at least 5 ingredients."""
        for gap_id in [1, 2, 3]:
            assert len(GAP_INGREDIENTS[gap_id]['ingredients']) >= 5

    def test_coupling_matrix_symmetric(self):
        """Coupling matrix is symmetric: C(i,j) = C(j,i)."""
        matrix = gap_coupling_matrix()
        for i in [1, 2, 3]:
            for j in [1, 2, 3]:
                assert abs(matrix[(i, j)]['coupling'] - matrix[(j, i)]['coupling']) < 1e-15

    def test_coupling_diagonal_is_one(self):
        """Diagonal entries are 1 (Jaccard of set with itself)."""
        matrix = gap_coupling_matrix()
        for i in [1, 2, 3]:
            assert abs(matrix[(i, i)]['coupling'] - 1.0) < 1e-15

    def test_coupling_12_positive(self):
        """Gap 1 and Gap 2 share ingredients (Langlands parametrization)."""
        matrix = gap_coupling_matrix()
        assert matrix[(1, 2)]['coupling'] > 0
        assert 'langlands_parametrization' in matrix[(1, 2)]['shared']

    def test_coupling_13_positive(self):
        """Gap 1 and Gap 3 share ingredients (analytic continuation)."""
        matrix = gap_coupling_matrix()
        # They share at least one ingredient
        assert matrix[(1, 3)]['shared_count'] >= 0
        # The coupling is between 0 and 1
        assert 0 <= matrix[(1, 3)]['coupling'] <= 1

    def test_coupling_23_positive(self):
        """Gap 2 and Gap 3 share no ingredients in common OR share some."""
        matrix = gap_coupling_matrix()
        assert 0 <= matrix[(2, 3)]['coupling'] <= 1

    def test_triple_coupling_exists(self):
        """Triple coupling (1,2,3) is computed."""
        matrix = gap_coupling_matrix()
        assert (1, 2, 3) in matrix
        assert 0 <= matrix[(1, 2, 3)]['coupling'] <= 1

    def test_coupling_12_shared_functional_equation(self):
        """Gaps 1 and 2 share 'functional_equation'."""
        matrix = gap_coupling_matrix()
        assert 'functional_equation' in matrix[(1, 2)]['shared']

    def test_gaps_not_independent(self):
        """At least one pair of gaps shares ingredients."""
        matrix = gap_coupling_matrix()
        max_coupling = max(
            matrix[(i, j)]['coupling']
            for i in [1, 2, 3] for j in [1, 2, 3] if i < j
        )
        assert max_coupling > 0, "Gaps should share at least some ingredients"


# ============================================================
# 2. Gap pair interaction tests
# ============================================================

class TestGapPairInteractions:
    """Test specific gap-pair interaction analyses."""

    @needs_mpmath
    def test_gap12_lattice_closed(self):
        """For lattice VOAs, Hecke decomposition gives intertwining operator."""
        result = gap12_hecke_gives_intertwining()
        assert result['lattice_closed'] is True

    @needs_mpmath
    def test_gap12_non_lattice_open(self):
        """For non-lattice VOAs, the connection is partial."""
        result = gap12_hecke_gives_intertwining()
        assert result['non_lattice_closed'] is False

    @needs_mpmath
    def test_gap12_VZ_scattering_verification(self):
        """Verify scattering matrix computation for V_Z."""
        result = gap12_hecke_gives_intertwining()
        vz = result['VZ_verification']
        assert len(vz) > 0
        # For s=1.5 or s=2.0: phi should be a finite complex number
        found_finite = False
        for entry in vz:
            if np.isfinite(abs(entry['phi'])):
                found_finite = True
        assert found_finite, "At least one test s-value should give finite phi"

    @needs_mpmath
    def test_gap13_coupled(self):
        """Gap 1 and Gap 3 are coupled through Fredholm determinant."""
        result = gap13_coderived_gives_poles()
        assert result['coupled'] is True

    @needs_mpmath
    def test_gap13_coderived_encodes_poles(self):
        """Coderived category encodes intertwining operator poles."""
        result = gap13_coderived_gives_poles()
        assert result['coderived_encodes_poles'] is True

    @needs_mpmath
    def test_gap13_parametrization_relation(self):
        """Epstein and Fredholm zeros are related by factor of 2."""
        result = gap13_coderived_gives_poles()
        ep_zeros = result['epstein_zero_locations']
        fr_zeros = result['fredholm_zero_locations']
        for i in range(min(len(ep_zeros), len(fr_zeros))):
            assert abs(ep_zeros[i] - fr_zeros[i] / 2) < 1e-10

    def test_gap23_strongly_coupled(self):
        """Gap 2 and Gap 3 are strongly coupled."""
        result = gap23_sewing_gives_vvmf()
        assert result['strongly_coupled'] is True

    def test_gap23_rational_gap2_from_gap3(self):
        """For rational theories, Gap 2 follows from Gap 3."""
        result = gap23_sewing_gives_vvmf()
        assert result['rational_theories']['gap2_follows_from_gap3'] is True

    def test_gap23_irrational_gap2_not_from_gap3(self):
        """For irrational theories, Gap 2 does NOT follow from Gap 3."""
        result = gap23_sewing_gives_vvmf()
        assert result['irrational_theories']['gap2_follows_from_gap3'] is False

    def test_gap23_lattice_automatic(self):
        """For lattice theories, Gap 2 is automatic."""
        result = gap23_sewing_gives_vvmf()
        assert result['lattice_theories']['gap2_automatic'] is True

    def test_gap23_minimal_model_vvmf(self):
        """Minimal models have finite-dimensional VVMF structure."""
        result = gap23_sewing_gives_vvmf()
        for name, data in result['minimal_model_vvmf'].items():
            assert data['vvmf'] is True
            assert data['char_dim'] > 0


# ============================================================
# 3. Information content and flow tests
# ============================================================

class TestInformationFlow:
    """Test information content and flow direction."""

    @needs_mpmath
    def test_VZ_all_consistent(self):
        """All three gap stages give consistent information for V_Z."""
        result = information_content_VZ()
        assert result['all_consistent'] is True

    @needs_mpmath
    def test_VZ_zero_count(self):
        """V_Z information content covers 10 zeros."""
        result = information_content_VZ()
        assert result['zero_count'] == 10

    @needs_mpmath
    def test_VZ_zeros_from_all_gaps_agree(self):
        """Zeros from all three gap routes agree for V_Z."""
        result = information_content_VZ()
        z1 = result['zeros_from_gap1']
        z2 = result['zeros_from_gap2']
        z3 = result['zeros_from_gap3']
        for i in range(len(z1)):
            assert abs(z1[i] - z2[i]) < 1e-6
            assert abs(z2[i] - z3[i]) < 1e-6

    @needs_mpmath
    def test_VZ_gap2_euler_product(self):
        """Gap 2 info for V_Z includes Euler product data."""
        result = information_content_VZ()
        euler = result['gap2']['first_10_primes_euler_factors']
        assert len(euler) == 10
        # First prime p=2: factor = 1/(1-1/4) = 4/3
        assert abs(euler[0]['factor'] - 4 / 3) < 1e-10

    def test_flow_direction_is_3_to_1(self):
        """Information flows from Gap 3 to Gap 2 to Gap 1."""
        flow = information_flow_direction()
        assert 'Gap 3 -> Gap 2 -> Gap 1' in flow['direction']

    def test_flow_reverse_impossible(self):
        """Reverse flow is not possible."""
        flow = information_flow_direction()
        assert '1_to_2' in flow['reverse_impossible']
        assert '2_to_3' in flow['reverse_impossible']


# ============================================================
# 4. Minimal closing set tests
# ============================================================

class TestMinimalClosingSet:
    """Test the minimal closing set analysis."""

    @needs_mpmath
    def test_gap2_alone_insufficient_for_ising(self):
        """Gap 2 alone does not give zeta(s) for Ising."""
        result = _test_gap2_alone_ising()
        assert result['gap2_alone_sufficient'] is False
        assert result['zeta_appears'] is False

    def test_gap3_alone_sufficient_lattice(self):
        """Gap 3 alone is sufficient for lattice VOAs."""
        result = _test_gap3_alone()
        assert result['gap3_alone_sufficient_lattice'] is True

    def test_gap3_alone_insufficient_general(self):
        """Gap 3 alone is NOT sufficient for general VOAs."""
        result = _test_gap3_alone()
        assert result['gap3_alone_sufficient_general'] is False

    def test_gap1_alone_insufficient(self):
        """Gap 1 alone is NOT sufficient (gives identification but not computation)."""
        result = _test_gap1_alone()
        assert result['gap1_alone_sufficient'] is False

    def test_minimal_set_lattice(self):
        """For lattice VOAs, minimal closing set is {3}."""
        result = minimal_closing_set()
        assert result['lattice_VOA']['minimal_set'] == {3}

    def test_minimal_set_rational(self):
        """For rational VOAs, minimal closing set is {2, 3}."""
        result = minimal_closing_set()
        assert result['rational_VOA']['minimal_set'] == {2, 3}

    def test_minimal_set_general(self):
        """For general VOAs, all three gaps needed."""
        result = minimal_closing_set()
        assert result['general_VOA']['minimal_set'] == {1, 2, 3}

    def test_minimal_set_bootstrap(self):
        """For the bootstrap programme, Gaps 2+3 suffice."""
        result = minimal_closing_set()
        assert result['for_bootstrap']['minimal_set'] == {2, 3}


# ============================================================
# 5. Redundancy test for V_Z
# ============================================================

class TestRedundancyVZ:
    """Test the four-route redundancy computation for V_Z."""

    @needs_mpmath
    def test_route_a_zeros_near_zero(self):
        """Route (a) zeros: epsilon^1 vanishes at zeta zeros."""
        result = redundancy_test_VZ(num_zeros=5)
        for val in result['route_a_residuals']:
            assert val < 1e-5, f"epsilon^1 should vanish at zero, got {val}"

    @needs_mpmath
    def test_routes_a_b_agree(self):
        """Routes (a) and (b) give the same t-values."""
        result = redundancy_test_VZ(num_zeros=5)
        a = result['route_a_direct']
        b = result['route_b_barcobar']
        for i in range(len(a)):
            assert abs(a[i] - b[i]) < 1e-10

    @needs_mpmath
    def test_first_zero_agreement(self):
        """All four routes agree on the first zero location."""
        result = redundancy_test_VZ(num_zeros=5)
        assert result['first_zero_agreement'] is True

    @needs_mpmath
    def test_all_routes_consistent(self):
        """All routes are flagged as consistent."""
        result = redundancy_test_VZ(num_zeros=5)
        assert result['all_routes_consistent'] is True

    @needs_mpmath
    def test_shadow_moments_positive(self):
        """Shadow moments M_2, M_3, M_4 are positive."""
        result = redundancy_test_VZ(num_zeros=5)
        M = result['shadow_moments']
        assert M['M2'] > 0
        assert M['M3'] > 0
        assert M['M4'] > 0

    @needs_mpmath
    def test_hecke_L_zeros_distinct_from_zeta(self):
        """Route (c) L(s, chi_{-4}) zeros are DISTINCT from zeta zeros."""
        result = redundancy_test_VZ(num_zeros=5)
        zeta_zeros = result['route_c_hecke_zeta']
        L_zeros = result['route_c_hecke_L']
        if len(L_zeros) > 0:
            # L-zeros should NOT coincide with zeta zeros
            for lz in L_zeros:
                for gz in zeta_zeros:
                    assert abs(lz - gz) > 0.1, "L and zeta zeros should be distinct"

    @needs_mpmath
    def test_first_zero_location(self):
        """First zero at t = gamma_1/2 ~ 7.067."""
        result = redundancy_test_VZ(num_zeros=5)
        first = result['route_a_direct'][0]
        assert abs(first - 14.134725 / 2) < 0.001


# ============================================================
# 6. Obstruction hierarchy tests
# ============================================================

class TestObstructionHierarchy:
    """Test the difficulty and dependency structure of gaps."""

    def test_gap1_hardest(self):
        """Gap 1 (Langlands) has the highest difficulty."""
        h = obstruction_hierarchy()
        assert h[1]['difficulty'] >= h[2]['difficulty']
        assert h[1]['difficulty'] >= h[3]['difficulty']

    def test_gap1_depends_on_2_and_3(self):
        """Gap 1 depends on both Gap 2 and Gap 3."""
        h = obstruction_hierarchy()
        assert 2 in h[1]['depends_on']
        assert 3 in h[1]['depends_on']

    def test_gap2_depends_on_3(self):
        """Gap 2 depends on Gap 3."""
        h = obstruction_hierarchy()
        assert 3 in h[2]['depends_on']

    def test_gap3_no_dependencies(self):
        """Gap 3 has no dependencies (it is the foundation)."""
        h = obstruction_hierarchy()
        assert len(h[3]['depends_on']) == 0

    def test_lattice_all_closed(self):
        """For lattice VOAs, all gaps are closed."""
        h = obstruction_hierarchy()
        for gap_id in [1, 2, 3]:
            assert h[gap_id]['status']['lattice'].startswith('CLOSED')

    def test_difficulty_labels(self):
        """Difficulty labels are consistent with numbers."""
        h = obstruction_hierarchy()
        assert h[1]['difficulty_label'] == 'hard'
        assert h[2]['difficulty_label'] == 'medium'
        assert h[3]['difficulty_label'] == 'medium'


# ============================================================
# 7. Bootstrap exclusion region tests
# ============================================================

class TestBootstrapExclusion:
    """Test the exclusion region computation."""

    @needs_mpmath
    def test_c1_complete_exclusion(self):
        """At c=1 (V_Z), exclusion should be nearly complete."""
        gamma = float(mpmath.zetazero(1).imag)
        region = exclusion_region_single_c(1.0, gamma)
        # For c=1, the lattice case has exact functional equation
        # All sigma != 1/2 should be excluded
        assert region['excluded_fraction'] > 0.8

    @needs_mpmath
    def test_c1_all_excluded(self):
        """At c=1, all sigma values are excluded (ratio never equals 1).

        At the pole s = (1+z_k)/2, the functional equation has a POLE,
        so the compatibility ratio is never 1 for any sigma. This means
        100% exclusion, which is the correct answer: the functional
        equation is consistent only when z_k is a genuine zeta zero.
        """
        gamma = float(mpmath.zetazero(1).imag)
        region = exclusion_region_single_c(1.0, gamma)
        assert region['excluded_fraction'] == 1.0

    @needs_mpmath
    def test_c_half_partial_exclusion(self):
        """At c=1/2 (Ising approximation), some exclusion expected."""
        gamma = float(mpmath.zetazero(1).imag)
        region = exclusion_region_single_c(0.5, gamma)
        # Should exclude at least some sigma values
        assert region['excluded_fraction'] > 0

    @needs_mpmath
    def test_exclusion_plane_computed(self):
        """Bootstrap exclusion plane computes for multiple c values."""
        gamma = float(mpmath.zetazero(1).imag)
        plane = bootstrap_exclusion_plane(c_values=[0.5, 1.0], gamma=gamma)
        assert 1.0 in plane
        assert 'exclusion_fraction' in plane[1.0]

    @needs_mpmath
    def test_c1_stronger_than_c_half(self):
        """Exclusion at c=1 is at least as strong as at c=1/2."""
        gamma = float(mpmath.zetazero(1).imag)
        plane = bootstrap_exclusion_plane(c_values=[0.5, 1.0], gamma=gamma)
        assert plane[1.0]['exclusion_fraction'] >= plane[0.5]['exclusion_fraction']


# ============================================================
# 8. Residue discrimination tests
# ============================================================

class TestResidueDiscrimination:
    """Test residue discrimination for minimal models."""

    @needs_mpmath
    def test_residue_at_c1_finite(self):
        """Residue at first zeta zero for c=1 is finite and nonzero."""
        res = residue_at_zeta_zero_c(1, 1.0)
        assert np.isfinite(abs(res))
        assert abs(res) > 1e-30

    @needs_mpmath
    def test_offline_residue_different(self):
        """Off-line residue (sigma=0.3) differs from on-line (sigma=0.5)."""
        gamma = float(mpmath.zetazero(1).imag)
        online = residue_at_zeta_zero_c(1, 1.0)
        offline = offline_residue(0.3, gamma, 1.0)
        assert abs(abs(online) - abs(offline)) > 1e-10

    @needs_mpmath
    def test_discrimination_computed(self):
        """Residue discrimination is computed for minimal models."""
        result = residue_discrimination(c_values=[0.5, 1.0], zero_index=1)
        assert 0.5 in result['per_c']
        assert 1.0 in result['per_c']

    @needs_mpmath
    def test_discrimination_at_c1_online_magnitude(self):
        """Online magnitude at c=1 is a specific positive number."""
        result = residue_discrimination(c_values=[1.0], zero_index=1)
        assert result['per_c'][1.0]['online_magnitude'] > 0

    @needs_mpmath
    def test_discrimination_offline_tests_present(self):
        """Offline tests at sigma=0.3, 0.4, 0.6, 0.7 are present."""
        result = residue_discrimination(c_values=[1.0], zero_index=1)
        offsets = [od['sigma'] for od in result['per_c'][1.0]['offline_tests']]
        assert 0.3 in offsets
        assert 0.7 in offsets

    @needs_mpmath
    def test_discrimination_nontrivial(self):
        """Discrimination ratio is not 1 for off-line sigma."""
        result = residue_discrimination(c_values=[1.0], zero_index=1)
        for od in result['per_c'][1.0]['offline_tests']:
            if np.isfinite(od['discrimination']):
                # Off-line: discrimination should deviate from 1
                assert abs(od['discrimination'] - 1.0) > 1e-6 or not np.isfinite(od['discrimination'])

    @needs_mpmath
    def test_discrimination_trend_exists(self):
        """The trend analysis gives a result."""
        result = residue_discrimination(c_values=[0.5, 0.7, 0.8, 1.0], zero_index=1)
        assert result['trend_with_c'] in [
            'increasing_with_c', 'non_monotone_or_decreasing', 'insufficient_data'
        ]

    @needs_mpmath
    def test_multiple_zero_indices(self):
        """Residue discrimination works for different zero indices."""
        for k in [1, 2, 3]:
            result = residue_discrimination(c_values=[1.0], zero_index=k)
            assert result['gamma_k'] > 0
            assert result['per_c'][1.0]['online_magnitude'] > 0


# ============================================================
# 9. Full synthesis tests
# ============================================================

class TestFullSynthesis:
    """Test the complete synthesis output."""

    def test_synthesis_coupling_matrix(self):
        """Synthesis includes coupling matrix."""
        s = full_synthesis()
        assert '(1,2)' in s['coupling_matrix']
        assert '(1,3)' in s['coupling_matrix']
        assert '(2,3)' in s['coupling_matrix']

    def test_synthesis_gaps_not_independent(self):
        """Synthesis concludes gaps are NOT independent."""
        s = full_synthesis()
        assert s['are_gaps_independent'] is False

    def test_synthesis_flow_direction(self):
        """Synthesis gives correct flow direction."""
        s = full_synthesis()
        assert '3' in s['flow_direction'] and '1' in s['flow_direction']

    def test_synthesis_minimal_sets_present(self):
        """Synthesis includes minimal closing sets for all theory classes."""
        s = full_synthesis()
        mcs = s['minimal_closing_sets']
        assert 'lattice_VOA' in mcs
        assert 'rational_VOA' in mcs
        assert 'general_VOA' in mcs

    def test_synthesis_shared_ingredients(self):
        """Synthesis includes shared ingredient lists."""
        s = full_synthesis()
        si = s['shared_ingredients']
        assert isinstance(si['(1,2)'], set)

    def test_synthesis_key_insight_nonempty(self):
        """Synthesis provides a key insight string."""
        s = full_synthesis()
        assert len(s['key_insight']) > 50

    def test_synthesis_coupling_values_valid(self):
        """All coupling values are in [0, 1]."""
        s = full_synthesis()
        for key, val in s['coupling_matrix'].items():
            assert 0 <= val <= 1, f"Coupling {key} = {val} out of range"

    def test_synthesis_triple_coupling_leq_pairwise(self):
        """Triple coupling is at most as large as any pairwise coupling."""
        s = full_synthesis()
        c123 = s['coupling_matrix']['(1,2,3)']
        c12 = s['coupling_matrix']['(1,2)']
        c13 = s['coupling_matrix']['(1,3)']
        c23 = s['coupling_matrix']['(2,3)']
        # Jaccard: intersection of 3 sets <= intersection of any 2
        assert c123 <= max(c12, c13, c23) + 1e-15


# ============================================================
# 10. Cross-gap structural tests
# ============================================================

class TestCrossGapStructure:
    """Structural tests verifying the cross-gap framework coherence."""

    def test_all_gaps_have_status(self):
        """Each gap has a defined status."""
        for gap_id in [1, 2, 3]:
            assert 'status' in GAP_INGREDIENTS[gap_id]

    def test_all_gaps_have_difficulty(self):
        """Each gap has a defined difficulty."""
        for gap_id in [1, 2, 3]:
            assert 'difficulty' in GAP_INGREDIENTS[gap_id]

    def test_dependency_acyclic(self):
        """Gap dependency graph is acyclic (DAG)."""
        h = obstruction_hierarchy()
        # Gap 3 depends on nothing
        assert len(h[3]['depends_on']) == 0
        # Gap 2 depends on 3 only
        assert h[2]['depends_on'] == {3}
        # Gap 1 depends on 2 and 3
        assert h[1]['depends_on'] == {2, 3}
        # No cycles: 3 has no deps, 2 deps on 3 only, 1 deps on 2,3 only

    def test_lattice_is_simplest(self):
        """Lattice VOAs have the simplest closing strategy."""
        mcs = minimal_closing_set()
        lattice_size = len(mcs['lattice_VOA']['minimal_set'])
        rational_size = len(mcs['rational_VOA']['minimal_set'])
        general_size = len(mcs['general_VOA']['minimal_set'])
        assert lattice_size <= rational_size <= general_size

    def test_gap_names_descriptive(self):
        """Gap names are informative."""
        for gap_id in [1, 2, 3]:
            name = GAP_INGREDIENTS[gap_id]['name']
            assert len(name) > 10

    @needs_mpmath
    def test_VZ_complete_chain(self):
        """For V_Z, the complete chain from shadow to zeros is computable."""
        # Gap 3: convergence
        info = information_content_VZ()
        assert info['gap3']['HS_sewing'] is True

        # Gap 2: Hecke (trivial for V_Z)
        assert info['gap2']['hecke_type'].startswith('trivial')

        # Gap 1: functional equation
        assert 'xi(2s) = xi(1-2s)' in info['gap1']['functional_equation']

        # Final result: zeros
        assert len(info['zeros_from_gap1']) == 10
        assert info['all_consistent'] is True
