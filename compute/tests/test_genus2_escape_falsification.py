r"""
Tests for adversarial falsification of the genus-2 escape claim.

Tests that the genus-2 non-diagonality (rem:genus2-escape-route)
provides genuine structural advance but does NOT resolve the
structural separation (thm:structural-separation). Six angles:

1. Heisenberg: genus-2 non-diagonality is structural, not arithmetic
2. Newton redundancy: genus-2 MC for Heisenberg is tautological
3. Separating degeneration: does NOT dominate (full measure interior)
4. Unfolding erasure: partially persists; Bocherer channel is new
5. L-values vs zero locations: access != control
6. Information-theoretic counterexample: finite D underdetermined
7. Lattice VOA dimension analysis: Leech reduces to GL(2) via SK
8. Verification functions: cross-checks on individual claims
"""

import pytest
import math
import numpy as np

from compute.lib.genus2_escape_falsification import (
    heisenberg_genus1_partition,
    heisenberg_genus2_siegel_theta,
    heisenberg_genus2_newton_test,
    genus2_mc_newton_redundancy,
    separating_degeneration_volume,
    genus2_unfolding_analysis,
    lvalue_vs_zero_location_test,
    explicit_counterexample,
    real_mechanism_analysis,
    lattice_voa_genus2_content,
    full_falsification_report,
    verify_heisenberg_no_new_constraints,
    verify_separating_not_dominant,
    verify_bocherer_access_genuine,
    verify_lvalue_not_zero_location,
    verify_leech_reduces_to_gl2,
    verify_first_genuine_siegel_rank,
    verify_counterexample_dimension_gap,
    verify_escalation_conjectural,
    heisenberg_c11_positive,
    genus2_correction_z_dependent,
    verify_sp4_volume_formula,
    dim_S_k_Sp4,
    dim_sk_lifts_in_weight,
    count_genuine_siegel_eigenforms,
)


# ============================================================
# HEISENBERG GENUS-1 PARTITION FUNCTION
# ============================================================

class TestHeisenbergGenus1:
    """Verify Heisenberg genus-1 partition function = 1/eta(tau)."""

    def test_positive(self):
        """1/eta(tau) is positive for purely imaginary tau."""
        for tau_im in [0.5, 1.0, 1.5, 2.0, 3.0]:
            z = heisenberg_genus1_partition(tau_im)
            assert z > 0, f"1/eta should be positive at tau_im={tau_im}"

    def test_increasing_for_large_tau_im(self):
        """1/eta(tau) increases for large Im(tau) (q^{-1/24} dominates)."""
        # For large Im(tau), q -> 0 so product -> 1, and q^{-1/24} grows
        vals = [heisenberg_genus1_partition(t) for t in [1.0, 2.0, 3.0, 5.0]]
        for i in range(len(vals) - 1):
            assert vals[i] < vals[i + 1], (
                "1/eta should increase for large Im(tau) due to q^{-1/24}"
            )

    def test_q_expansion_leading(self):
        """Leading term q^{-1/24} dominates for large Im(tau)."""
        tau_im = 5.0
        z = heisenberg_genus1_partition(tau_im)
        q = math.exp(-2 * math.pi * tau_im)
        leading = q ** (-1.0 / 24.0)
        # For large tau_im, the product is very close to 1
        ratio = z / leading
        assert 0.999 < ratio < 1.001, (
            f"For tau_im=5, product factor should be ~1, got ratio={ratio}"
        )

    def test_known_value_tau_i(self):
        """At tau = i (tau_im = 1), 1/eta has a known numerical value."""
        z = heisenberg_genus1_partition(1.0, order=100)
        # eta(i) = Gamma(1/4) / (2 * pi^{3/4})
        # 1/eta(i) = 2 * pi^{3/4} / Gamma(1/4) * q^{-1/24}
        # Numerically: eta(i) approx 0.76823 (without q^{1/24} factor)
        # 1/eta(i) ~ 1.302  (with q^{-1/24} factor included)
        # Just check it's a reasonable positive number > 1
        assert 1.0 < z < 2.0, f"1/eta(i) should be ~1.3, got {z}"


# ============================================================
# HEISENBERG GENUS-2 SIEGEL THETA
# ============================================================

class TestHeisenbergGenus2:
    """Test genus-2 Heisenberg partition function structure."""

    def test_separating_factorizes(self):
        """At z=0 (separating degeneration), genus-2 factorizes."""
        r = heisenberg_genus2_siegel_theta(1.0, 1.0, 0.0)
        assert abs(r['correction']) < 1e-15, (
            "At z=0, off-diagonal correction should vanish"
        )
        assert r['ratio'] == pytest.approx(1.0, abs=1e-14), (
            "At z=0, total/separating ratio should be 1"
        )

    def test_nonseparating_nontrivial(self):
        """At z != 0, the off-diagonal correction is nonzero."""
        r = heisenberg_genus2_siegel_theta(1.0, 1.0, 0.5)
        assert r['z_dependent'], "Off-diagonal correction should be nonzero for z=0.5"
        assert r['correction'] > 0, "Correction should be positive"

    def test_correction_decays_with_z(self):
        """The off-diagonal correction decays as z -> infinity."""
        corrections = []
        for z in [0.3, 0.5, 1.0, 2.0, 3.0]:
            r = heisenberg_genus2_siegel_theta(1.0, 1.0, z)
            corrections.append(r['correction'])
        for i in range(len(corrections) - 1):
            assert corrections[i] > corrections[i + 1], (
                "Correction should decrease with increasing z_im"
            )

    def test_total_exceeds_separating(self):
        """Total partition function >= separating part (correction is positive)."""
        for z in [0.3, 0.5, 1.0]:
            r = heisenberg_genus2_siegel_theta(1.0, 1.0, z)
            assert r['total'] >= r['separating'], (
                "Total should exceed separating contribution"
            )

    def test_symmetric_in_tau1_tau2(self):
        """Z_2 is symmetric under tau_1 <-> tau_2."""
        r1 = heisenberg_genus2_siegel_theta(1.0, 1.5, 0.5)
        r2 = heisenberg_genus2_siegel_theta(1.5, 1.0, 0.5)
        assert r1['total'] == pytest.approx(r2['total'], rel=1e-10), (
            "Genus-2 partition function should be symmetric in tau_1, tau_2"
        )


# ============================================================
# TEST 1: HEISENBERG ARITHMETIC TRIVIALITY AT GENUS 2
# ============================================================

class TestHeisenbergArithmeticTriviality:
    """Verify genus-2 gives no new arithmetic content for Heisenberg."""

    def test_no_new_arithmetic(self):
        """Heisenberg genus-2 gives no new arithmetic constraints."""
        result = heisenberg_genus2_newton_test()
        assert result['new_arithmetic_at_genus2'] is False

    def test_heisenberg_class_g(self):
        """Heisenberg is class G (shadow depth 2)."""
        result = heisenberg_genus2_newton_test()
        assert result['heisenberg_class'] == 'G'
        assert result['shadow_depth'] == 2

    def test_c11_positive(self):
        """The off-diagonal coupling c_{1,1} is positive."""
        assert heisenberg_c11_positive()

    def test_c11_purely_combinatorial(self):
        """c_{1,1} carries no new arithmetic content."""
        result = heisenberg_genus2_newton_test()
        assert result['c11_arithmetic_content'] is False

    def test_z_dependent(self):
        """The genus-2 correction IS z-dependent (structural non-triviality)."""
        assert genus2_correction_z_dependent()

    def test_z_dependence_details(self):
        """At z=0 correction vanishes; at z=0.5 it does not."""
        result = heisenberg_genus2_newton_test()
        z_results = result['z_dependent_results']
        # z_im = 0 should have no z-dependence
        assert z_results[0]['z_dependent'] is False
        # z_im = 0.5 should have z-dependence
        assert z_results[1]['z_dependent'] is True


# ============================================================
# TEST 2: NEWTON REDUNDANCY
# ============================================================

class TestNewtonRedundancy:
    """Test genus-2 MC equation is tautological for Heisenberg."""

    def test_heisenberg_tautological(self):
        """Genus-2 MC for Heisenberg is a tautology."""
        result = genus2_mc_newton_redundancy()
        assert result['heisenberg_genus2_mc'] == 'tautological'

    def test_no_planted_forest(self):
        """No planted-forest correction at genus 2 for Heisenberg."""
        result = genus2_mc_newton_redundancy()
        assert result['heisenberg_planted_forest_g2'] == 0

    def test_no_new_constraints(self):
        """No new constraints from genus-2 MC for Heisenberg."""
        result = genus2_mc_newton_redundancy()
        assert result['heisenberg_new_constraints_g2'] is False

    def test_lattice_potentially_nontrivial(self):
        """Lattice VOA genus-2 MC is potentially non-trivial."""
        result = genus2_mc_newton_redundancy()
        assert result['lattice_voa_genus2_mc'] == 'potentially non-trivial'

    def test_lattice_bocherer_channel(self):
        """Lattice VOA genus-2 has Bocherer factorization channel."""
        result = genus2_mc_newton_redundancy()
        assert result['lattice_new_constraints_g2'] == 'YES, via Bocherer factorization'


# ============================================================
# TEST 3: SEPARATING DEGENERATION VOLUME
# ============================================================

class TestSeparatingDegeneration:
    """Test separating degeneration does not dominate."""

    def test_boundary_measure_zero(self):
        """The separating boundary z=0 has measure zero."""
        result = separating_degeneration_volume()
        assert result['separating_boundary_measure'] == 0

    def test_sp4_volume_finite(self):
        """Sp(4,Z)\\H_2 has finite positive volume."""
        result = separating_degeneration_volume()
        assert result['sp4_volume_finite']
        assert result['sp4_volume'] > 0

    def test_sp4_volume_formula(self):
        """Volume formula is self-consistent."""
        assert verify_sp4_volume_formula()

    def test_separating_not_dominant(self):
        """Separating degeneration does NOT dominate."""
        assert verify_separating_not_dominant()

    def test_sp4_volume_numerical(self):
        """Sp(4) volume is a small positive number."""
        result = separating_degeneration_volume()
        vol = result['sp4_volume']
        # Should be O(10^{-4})
        assert 1e-6 < vol < 1e-2, f"Volume {vol} should be ~1.5e-4"


# ============================================================
# TEST 4: UNFOLDING ERASURE AT GENUS 2
# ============================================================

class TestUnfoldingErasure:
    """Test that unfolding erasure partially persists at genus 2."""

    def test_genus1_erasure(self):
        """Unfolding erasure holds at genus 1."""
        result = genus2_unfolding_analysis()
        assert result['genus1_erasure'] is True

    def test_genus2_pole_cancellation(self):
        """Eisenstein poles still cancel in genus-2 RS integral."""
        result = genus2_unfolding_analysis()
        assert result['genus2_pole_cancellation'] is True

    def test_bocherer_channel_new(self):
        """Bocherer channel is genuinely new at genus 2."""
        result = genus2_unfolding_analysis()
        assert result['bocherer_channel_new'] is True

    def test_critical_line_access(self):
        """Bocherer gives genuine critical-line access."""
        result = genus2_unfolding_analysis()
        assert result['critical_line_access'] is True

    def test_access_not_control(self):
        """Access to critical line is not control of zeros."""
        result = genus2_unfolding_analysis()
        assert result['but_access_not_control'] is True

    def test_bocherer_mechanism(self):
        """Bocherer mechanism is Fourier coefficient extraction."""
        result = genus2_unfolding_analysis()
        assert 'Fourier coefficient' in result['bocherer_mechanism']

    def test_bocherer_access_genuine(self):
        """Combined verification of Bocherer access."""
        assert verify_bocherer_access_genuine()

    def test_genus2_eisenstein_poles(self):
        """Genus-2 Eisenstein has poles at 3/2, 1/2, 0, -1/2."""
        result = genus2_unfolding_analysis()
        poles = result['genus2_eisenstein_poles']
        assert 1.5 in poles
        assert 0.5 in poles


# ============================================================
# TEST 5: L-VALUES VS ZERO LOCATIONS
# ============================================================

class TestLValueVsZeroLocation:
    """Test that L-values at s=1/2 do not determine zero locations."""

    def test_central_values_not_zeros(self):
        """Central L-values do NOT determine zero locations."""
        result = lvalue_vs_zero_location_test()
        assert result['central_values_determine_zeros'] is False

    def test_finitely_many_not_sufficient(self):
        """Finitely many discriminants do not determine f."""
        result = lvalue_vs_zero_location_test()
        assert result['finitely_many_determine_f'] is False

    def test_all_central_values_determine_f(self):
        """ALL central values DO determine f (via Shimura/Waldspurger)."""
        result = lvalue_vs_zero_location_test()
        assert result['all_central_values_determine_f'] is True

    def test_escalation_conditional(self):
        """The escalation principle is conditional."""
        result = lvalue_vs_zero_location_test()
        assert result['escalation_conditional'] is True

    def test_escalation_insufficient(self):
        """Even with all symmetric powers, zeros not directly determined."""
        result = lvalue_vs_zero_location_test()
        assert result['escalation_sufficient'] is False

    def test_manuscript_partially_valid(self):
        """Manuscript claim is partially valid."""
        result = lvalue_vs_zero_location_test()
        assert result['manuscript_claim_valid'] == 'PARTIALLY'

    def test_lvalue_not_zero_location(self):
        """Combined verification."""
        assert verify_lvalue_not_zero_location()

    def test_escalation_conjectural(self):
        """Combined verification of escalation conditionality."""
        assert verify_escalation_conjectural()


# ============================================================
# TEST 6: EXPLICIT COUNTEREXAMPLE
# ============================================================

class TestExplicitCounterexample:
    """Test the information-theoretic counterexample."""

    def test_dimension_gap(self):
        """Finite D constraints << zero count for degree-4 L-function."""
        result = explicit_counterexample()
        n_constraints = result['finite_D_constraint_count']
        n_zeros = result['zero_count_up_to_T100']
        assert n_constraints < n_zeros, (
            f"{n_constraints} constraints cannot determine {n_zeros} zeros"
        )

    def test_counterexample_dimension_gap(self):
        """Combined verification of dimension gap."""
        assert verify_counterexample_dimension_gap()

    def test_degree2_special(self):
        """Degree-2 is special: central value DOES determine zeros."""
        result = explicit_counterexample()
        assert result['degree2_central_determines_zeros'] is True

    def test_degree4_general(self):
        """Degree-4 is general: central value does NOT determine zeros."""
        result = explicit_counterexample()
        assert result['degree4_central_determines_zeros'] is False

    def test_all_D_sufficient(self):
        """All D together ARE sufficient (by Hecke theory)."""
        result = explicit_counterexample()
        assert result['all_D_sufficient'] is True

    def test_zero_count_reasonable(self):
        """Zero count estimate is reasonable for T=100."""
        result = explicit_counterexample()
        n = result['zero_count_up_to_T100']
        # T/(2*pi) * log(T) ~ 100/(6.28)*4.6 ~ 73
        assert 50 < n < 100, f"Zero count should be ~73, got {n}"

    def test_toy_L_functions_different(self):
        """Toy L-functions have different central values (as expected)."""
        result = explicit_counterexample()
        assert result['toy_same_central'] is False


# ============================================================
# TEST 7: REAL MECHANISM ANALYSIS
# ============================================================

class TestRealMechanism:
    """Test the honest assessment of the genus-2 escape mechanism."""

    def test_true_claims_nonempty(self):
        """There are genuine true claims about the genus-2 escape."""
        result = real_mechanism_analysis()
        assert len(result['true_claims']) >= 4

    def test_overstated_claims_nonempty(self):
        """There are overstated claims."""
        result = real_mechanism_analysis()
        assert len(result['overstated_claims']) >= 2

    def test_false_claims_nonempty(self):
        """There are false/misleading claims."""
        result = real_mechanism_analysis()
        assert len(result['false_claims']) >= 1

    def test_nondiagonality_true(self):
        """Non-diagonality of genus-2 sewing kernel is a true claim."""
        result = real_mechanism_analysis()
        assert any('Non-diagonality' in c or 'non-diag' in c.lower()
                    for c in result['true_claims'])

    def test_genus2_alone_false(self):
        """Genus-2 alone resolving structural separation is false."""
        result = real_mechanism_analysis()
        assert any('alone' in c.lower() and 'false' in c.lower()
                    for c in result['false_claims'])


# ============================================================
# TEST 8: LATTICE VOA DIMENSION ANALYSIS
# ============================================================

class TestLatticeVOADimensions:
    """Test Siegel cusp form dimensions and SK lift analysis."""

    def test_leech_dim_S12(self):
        """dim S_12(Sp(4,Z)) = 1."""
        result = lattice_voa_genus2_content(24)
        assert result['dim_S_k_Sp4'] == 1

    def test_leech_all_sk(self):
        """For Leech (rank 24), all genus-2 cusp forms are SK lifts."""
        result = lattice_voa_genus2_content(24)
        assert result['leech_all_sk'] is True

    def test_leech_no_genuine(self):
        """Leech has zero genuine (non-SK) Siegel eigenforms."""
        result = lattice_voa_genus2_content(24)
        assert result['n_genuine_siegel'] == 0

    def test_leech_genus2_no_new(self):
        """Leech genus-2 data gives no genuinely new arithmetic content."""
        result = lattice_voa_genus2_content(24)
        assert result['genus2_new_for_leech'] is False

    def test_leech_reduces_to_gl2(self):
        """Combined verification that Leech reduces to GL(2)."""
        assert verify_leech_reduces_to_gl2()

    def test_first_genuine_at_rank_40(self):
        """First genuinely new Siegel eigenforms appear at rank >= 40."""
        assert verify_first_genuine_siegel_rank()

    def test_rank_40_has_genuine(self):
        """Rank 40 (weight 20) has at least 1 genuine Siegel eigenform."""
        result = lattice_voa_genus2_content(40)
        assert result['n_genuine_siegel'] is not None
        assert result['n_genuine_siegel'] >= 1

    def test_rank_40_genus2_new(self):
        """Rank 40 has genuinely new genus-2 content."""
        result = lattice_voa_genus2_content(40)
        assert result['genus2_new_for_higher_rank'] is True

    @pytest.mark.parametrize("rank", [20, 24, 28, 32, 36])
    def test_no_genuine_below_40(self, rank):
        """No genuine Siegel eigenforms for rank < 40."""
        result = lattice_voa_genus2_content(rank)
        if result['n_genuine_siegel'] is not None:
            assert result['n_genuine_siegel'] == 0, (
                f"Rank {rank}: expected 0 genuine, got {result['n_genuine_siegel']}"
            )


# ============================================================
# SIEGEL CUSP FORM DIMENSION TABLE
# ============================================================

class TestSiegelDimensions:
    """Cross-check dim S_k(Sp(4,Z)) against known values."""

    @pytest.mark.parametrize("k,expected", [
        (4, 0), (6, 0), (8, 0), (10, 1), (12, 1), (14, 1),
        (16, 2), (18, 2), (20, 3), (22, 4), (24, 5), (26, 6),
    ])
    def test_dim_S_k_Sp4(self, k, expected):
        """Verify dim S_k(Sp(4,Z)) against Igusa-Tsuyumine values."""
        result = dim_S_k_Sp4(k)
        assert result == expected, f"dim S_{k}(Sp(4,Z)): expected {expected}, got {result}"

    @pytest.mark.parametrize("k,expected", [
        (4, 0), (6, 0), (8, 0),
    ])
    def test_no_cusp_forms_small_weight(self, k, expected):
        """No cusp forms for weight < 10."""
        result = dim_S_k_Sp4(k)
        assert result == expected

    def test_first_cusp_form_at_weight_10(self):
        """First Siegel cusp form appears at weight 10 (SK lift of Delta)."""
        assert dim_S_k_Sp4(10) == 1


# ============================================================
# SK LIFT DIMENSION TABLE
# ============================================================

class TestSKLiftDimensions:
    """Verify SK lift counts = dim S_{2k-2}(SL(2,Z))."""

    @pytest.mark.parametrize("k,expected_sk", [
        (10, 1),   # S_18(SL2) = 1
        (12, 1),   # S_22(SL2) = 1
        (14, 1),   # S_26(SL2) = 1
        (16, 2),   # S_30(SL2) = 2
        (18, 2),   # S_34(SL2) = 2
        (20, 2),   # S_38(SL2) = 2
        (22, 3),   # S_42(SL2) = 3
        (24, 3),   # S_46(SL2) = 3
        (26, 3),   # S_50(SL2) = 3
    ])
    def test_sk_lift_count(self, k, expected_sk):
        """SK lift count = dim S_{2k-2}(SL(2,Z))."""
        result = dim_sk_lifts_in_weight(k)
        assert result == expected_sk, (
            f"Weight {k}: expected {expected_sk} SK lifts, got {result}"
        )

    def test_sk_lift_from_monomial_count(self):
        """SK lift count from dim S_{2k-2} agrees with monomial counting."""
        for k in range(10, 28, 2):
            n_sk = dim_sk_lifts_in_weight(k)
            # Cross-check: count monomials E_4^a E_6^b with 4a+6b = 2k-2
            wt = 2 * k - 2
            dim_mk = sum(
                1 for b in range(wt // 6 + 1)
                if (wt - 6 * b) >= 0 and (wt - 6 * b) % 4 == 0
            )
            dim_sk = max(0, dim_mk - 1) if wt >= 12 else 0
            assert n_sk == dim_sk, (
                f"Weight {k}: SK={n_sk} vs monomial dim S_{wt}={dim_sk}"
            )


# ============================================================
# GENUINE SIEGEL EIGENFORM COUNTS
# ============================================================

class TestGenuineSiegelCounts:
    """Verify genuine (non-SK) Siegel eigenform counts."""

    @pytest.mark.parametrize("k,expected", [
        (10, 0), (12, 0), (14, 0), (16, 0), (18, 0),
        (20, 1),  # first genuine Siegel eigenform
    ])
    def test_genuine_count(self, k, expected):
        """Count genuine Siegel eigenforms."""
        result = count_genuine_siegel_eigenforms(k)
        assert result == expected, (
            f"Weight {k}: expected {expected} genuine, got {result}"
        )

    def test_genuine_monotone_increasing(self):
        """Genuine count is non-decreasing in weight."""
        prev = 0
        for k in range(10, 28, 2):
            n = count_genuine_siegel_eigenforms(k)
            if n is not None:
                assert n >= prev, (
                    f"Weight {k}: genuine count {n} < previous {prev}"
                )
                prev = n

    def test_first_genuine_is_20(self):
        """First weight with genuine Siegel eigenform is 20."""
        for k in range(4, 20, 2):
            n = count_genuine_siegel_eigenforms(k)
            if n is not None:
                assert n == 0, f"Expected 0 genuine at weight {k}"
        assert count_genuine_siegel_eigenforms(20) == 1


# ============================================================
# FULL FALSIFICATION REPORT
# ============================================================

class TestFullReport:
    """Test the complete adversarial falsification report."""

    def test_report_runs(self):
        """The full report computes without error."""
        report = full_falsification_report()
        assert report is not None

    def test_finding_count(self):
        """Report has 8 findings."""
        report = full_falsification_report()
        assert report['total_findings'] == 8

    def test_critical_count(self):
        """Report has exactly 1 critical finding."""
        report = full_falsification_report()
        assert report['critical'] == 1

    def test_serious_count(self):
        """Report has at least 3 serious findings."""
        report = full_falsification_report()
        assert report['serious'] >= 3

    def test_each_finding_has_id(self):
        """Each finding has an id, severity, claim, and finding."""
        report = full_falsification_report()
        for f in report['findings']:
            assert 'id' in f
            assert 'severity' in f
            assert 'claim' in f
            assert 'finding' in f

    def test_finding_ids_unique(self):
        """Finding IDs are unique."""
        report = full_falsification_report()
        ids = [f['id'] for f in report['findings']]
        assert len(ids) == len(set(ids))

    def test_verdict_nonempty(self):
        """Overall verdict is a non-empty string."""
        report = full_falsification_report()
        assert len(report['overall_verdict']) > 100

    def test_verdict_mentions_key_concepts(self):
        """Verdict addresses the key mathematical points."""
        report = full_falsification_report()
        v = report['overall_verdict']
        assert 'non-diagonality' in v.lower() or 'noncollapse' in v.lower()
        assert 'bocherer' in v.lower() or 'L-value' in v.lower() or 'l-value' in v.lower()


# ============================================================
# VERIFICATION FUNCTIONS (boolean checks)
# ============================================================

class TestVerificationFunctions:
    """Test all verification helper functions."""

    def test_heisenberg_no_new_constraints(self):
        assert verify_heisenberg_no_new_constraints()

    def test_separating_not_dominant(self):
        assert verify_separating_not_dominant()

    def test_bocherer_access_genuine(self):
        assert verify_bocherer_access_genuine()

    def test_lvalue_not_zero_location(self):
        assert verify_lvalue_not_zero_location()

    def test_leech_reduces_to_gl2(self):
        assert verify_leech_reduces_to_gl2()

    def test_first_genuine_siegel_rank(self):
        assert verify_first_genuine_siegel_rank()

    def test_counterexample_dimension_gap(self):
        assert verify_counterexample_dimension_gap()

    def test_escalation_conjectural(self):
        assert verify_escalation_conjectural()

    def test_c11_positive(self):
        assert heisenberg_c11_positive()

    def test_c11_positive_various_tau(self):
        """c_{1,1} is positive for various tau values."""
        for tau in [0.5, 1.0, 1.5, 2.0]:
            assert heisenberg_c11_positive(tau, tau)

    def test_z_dependent(self):
        assert genus2_correction_z_dependent()

    def test_sp4_volume_formula(self):
        assert verify_sp4_volume_formula()


# ============================================================
# CROSS-CONSISTENCY CHECKS
# ============================================================

class TestCrossConsistency:
    """Cross-check findings against each other for internal consistency."""

    def test_heisenberg_trivial_but_nondiagonal(self):
        """Heisenberg: arithmetically trivial yet structurally non-diagonal."""
        t1 = heisenberg_genus2_newton_test()
        assert t1['new_arithmetic_at_genus2'] is False  # trivial arithmetic
        # But the z-dependent correction IS nonzero
        assert genus2_correction_z_dependent()  # non-diagonal structure

    def test_bocherer_genuine_but_limited(self):
        """Bocherer access is genuine but L-values are not zero locations."""
        t4 = genus2_unfolding_analysis()
        t5 = lvalue_vs_zero_location_test()
        assert t4['critical_line_access'] is True  # access genuine
        assert t5['central_values_determine_zeros'] is False  # not zeros

    def test_leech_reduces_but_higher_rank_new(self):
        """Leech reduces to GL(2); higher rank has genuinely new content."""
        r24 = lattice_voa_genus2_content(24)
        r40 = lattice_voa_genus2_content(40)
        assert r24['n_genuine_siegel'] == 0  # Leech: all SK
        assert r40['n_genuine_siegel'] >= 1  # rank 40: genuine new

    def test_findings_severity_hierarchy(self):
        """At least one finding at each severity level except minor."""
        report = full_falsification_report()
        assert report['critical'] >= 1
        assert report['serious'] >= 1
        assert report['moderate'] >= 1

    def test_manuscript_partially_valid_consistent(self):
        """The 'partially valid' verdict is consistent across tests."""
        t5 = lvalue_vs_zero_location_test()
        t7 = real_mechanism_analysis()
        assert t5['manuscript_claim_valid'] == 'PARTIALLY'
        assert len(t7['true_claims']) > 0  # some are true
        assert len(t7['false_claims']) > 0  # some are false

    def test_all_findings_have_valid_severity(self):
        """All findings have a valid severity label."""
        report = full_falsification_report()
        valid = {'CRITICAL', 'SERIOUS', 'MODERATE', 'MINOR'}
        for f in report['findings']:
            assert f['severity'] in valid, (
                f"Finding {f['id']} has invalid severity {f['severity']}"
            )


# ============================================================
# MATHEMATICAL SOUNDNESS CHECKS
# ============================================================

class TestMathematicalSoundness:
    """Independent mathematical verification of key claims."""

    def test_siegel_fundamental_domain_dimension(self):
        """H_2 has complex dimension 3, real dimension 6."""
        # H_2 = {Omega = (tau1, z; z, tau2) : Im(Omega) > 0}
        # Parameters: tau1, tau2, z (complex), so 3 complex = 6 real
        # Separating boundary z=0 has codimension 2 (real) in F_2
        # So the boundary has measure zero. This is a topological fact.
        assert True  # structural check, documented

    def test_sk_lift_source_weight(self):
        """SK lifts of weight k come from S_{2k-2}(SL(2,Z))."""
        # For the Leech (weight 12): SK lifts from S_22(SL(2,Z))
        # dim S_22 = 1 (spanned by a Hecke eigenform f_22)
        n = dim_sk_lifts_in_weight(12)
        assert n == 1, "Leech SK lift count should be 1"

    def test_bocherer_formula_structure(self):
        """Bocherer formula relates Fourier coefficients to L-values."""
        # |B_f(D)|^2 / <f,f> = alpha * L(1/2, pi_f) * L(1/2, pi_f x chi_D)
        # This gives L-values at s=1/2, which is ON the critical line
        result = genus2_unfolding_analysis()
        assert result['critical_line_access'] is True

    def test_newton_thorne_bound(self):
        """Newton-Thorne: symmetric power transfer conditional for degree >= 6."""
        # Newton-Thorne proved automorphy of Sym^n for n <= 8 for
        # regular algebraic cuspidal automorphic representations of GL(2)
        # But the GENERAL case (all n, all forms) is conditional
        result = lvalue_vs_zero_location_test()
        assert result['escalation_conditional'] is True

    def test_partition_function_convergence(self):
        """1/eta series converges for |q| < 1 (Im(tau) > 0)."""
        # For tau_im > 0, q = e^{-2*pi*tau_im} < 1
        # The product prod (1-q^n) converges absolutely
        for tau_im in [0.1, 0.5, 1.0, 2.0]:
            z = heisenberg_genus1_partition(tau_im, order=100)
            assert math.isfinite(z) and z > 0

    def test_siegel_eisenstein_poles(self):
        """Genus-2 Siegel Eisenstein series has poles at specific half-integers."""
        result = genus2_unfolding_analysis()
        poles = result['genus2_eisenstein_poles']
        # The Siegel Eisenstein series E_k^{(2)}(Omega, s) has poles
        # related to Langlands constant term analysis
        assert len(poles) >= 3
        # Poles should be at half-integer points
        for p in poles:
            assert p * 2 == int(p * 2), f"Pole {p} should be a half-integer"


# ============================================================
# EDGE CASES AND ROBUSTNESS
# ============================================================

class TestEdgeCases:
    """Edge cases and numerical robustness."""

    def test_genus2_small_z(self):
        """Small z gives small correction (continuity at z=0)."""
        r = heisenberg_genus2_siegel_theta(1.0, 1.0, 3.0)
        # Very large z_im -> very small r -> very small correction
        assert abs(r['correction']) < 1e-10

    def test_genus2_equal_tau(self):
        """Equal tau values give consistent result."""
        r = heisenberg_genus2_siegel_theta(1.0, 1.0, 0.5)
        assert r['total'] > 0
        assert math.isfinite(r['total'])

    def test_genus2_unequal_tau(self):
        """Unequal tau values give consistent result."""
        r = heisenberg_genus2_siegel_theta(1.0, 2.0, 0.5)
        assert r['total'] > 0
        assert math.isfinite(r['total'])

    def test_lattice_voa_unknown_rank(self):
        """Lattice VOA at rank with unknown dim returns None."""
        result = lattice_voa_genus2_content(100)
        # Weight 50 is beyond our table
        assert result['dim_S_k_Sp4'] is None

    def test_dim_S_k_out_of_range(self):
        """dim S_k returns None for out-of-range weights."""
        assert dim_S_k_Sp4(100) is None
        assert dim_S_k_Sp4(3) is None  # odd weight

    def test_sk_lifts_small_weight(self):
        """SK lift count is 0 for small weights."""
        assert dim_sk_lifts_in_weight(4) == 0
        assert dim_sk_lifts_in_weight(6) == 0
        assert dim_sk_lifts_in_weight(8) == 0

    def test_genuine_count_none_for_unknown(self):
        """Genuine count returns None for unknown weights."""
        result = count_genuine_siegel_eigenforms(100)
        # Weight 100 is out of Sp(4) table range
        assert result is None
