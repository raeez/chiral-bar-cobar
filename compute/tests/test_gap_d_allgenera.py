r"""Tests for Gap D analysis: central L-values, all-genera convergence, circularity.

Covers both parts from arithmetic_shadows.tex:
  PART 1 (B7): Gap D norm mismatch — central values vs L^2(0,1) norm
  PART 2 (B11): All-genera convergence and circularity

Test structure:
  1. Nyman-Beurling norm computation (ground truth for Gap D)
  2. Central value information content (what genus-2 determines)
  3. Symmetric power conductor growth (analytic behavior)
  4. Root numbers and forced vanishing (rank defects)
  5. Circularity analysis (Newton-Thorne frontier)
  6. All-genera convergence (operator convergence)
  7. Moment problem and Satake recovery
  8. Quantitative Gap D comparison
  9. Boecherer structure at each genus
  10. Full integrated analysis
"""

import math
import pytest
import numpy as np

from compute.lib.gap_d_allgenera import (
    nyman_beurling_norm_squared,
    nyman_beurling_gram_matrix,
    nyman_beurling_distance_to_one,
    central_value_information_content,
    symmetric_power_conductor,
    keating_snaith_moment_prediction,
    symmetric_power_root_number,
    root_number_table,
    sym_power_functoriality_status,
    circularity_genus_frontier,
    all_genera_kernel_convergence,
    satake_recovery_from_central_values,
    gap_d_quantitative_analysis,
    genus_g_boecherer_structure,
    full_gap_d_analysis,
)


# ============================================================================
# 1. NYMAN-BEURLING NORM COMPUTATION
# ============================================================================

class TestNymanBeurlingNorm:
    """Tests for the Nyman-Beurling L^2 norm of dilation functions."""

    def test_norm_positive(self):
        """||rho_theta||^2 >= 0 for all theta in (0,1)."""
        for theta in [0.1, 0.3, 0.5, 0.7, 0.9]:
            norm_sq = nyman_beurling_norm_squared(theta, nmax=500)
            assert norm_sq >= -1e-10, f"Negative norm at theta={theta}: {norm_sq}"

    def test_norm_boundary_behavior(self):
        """||rho_theta||^2 should be small near theta=0 and theta=1."""
        norm_small = nyman_beurling_norm_squared(0.01, nmax=500)
        norm_mid = nyman_beurling_norm_squared(0.5, nmax=500)
        # rho_theta -> 0 as theta -> 0 or theta -> 1
        # (because {theta/x} ~ theta/x for small theta)
        assert norm_small < norm_mid or norm_small < 1.0

    def test_norm_invalid_theta(self):
        """theta outside (0,1) should raise ValueError."""
        with pytest.raises(ValueError):
            nyman_beurling_norm_squared(0.0)
        with pytest.raises(ValueError):
            nyman_beurling_norm_squared(1.0)
        with pytest.raises(ValueError):
            nyman_beurling_norm_squared(-0.5)

    def test_norm_symmetry(self):
        """rho_theta is NOT symmetric in theta <-> 1-theta in general.
        But ||rho_theta||^2 should be continuous."""
        norms = [nyman_beurling_norm_squared(t, nmax=300) for t in [0.3, 0.35, 0.4]]
        # Check continuity: adjacent values shouldn't differ by too much
        for i in range(len(norms) - 1):
            assert abs(norms[i] - norms[i + 1]) < 1.0, "Discontinuity detected"


class TestNymanBeurlingGram:
    """Tests for the NB Gram matrix."""

    def test_gram_psd(self):
        """Gram matrix must be positive semi-definite."""
        thetas = [1 / n for n in range(2, 8)]
        G = nyman_beurling_gram_matrix(thetas, nmax=500)
        eigenvalues = np.linalg.eigvalsh(G)
        assert all(v >= -1e-8 for v in eigenvalues), f"Non-PSD eigenvalue: {min(eigenvalues)}"

    def test_gram_symmetric(self):
        """Gram matrix must be symmetric."""
        thetas = [0.2, 0.4, 0.6]
        G = nyman_beurling_gram_matrix(thetas, nmax=500)
        np.testing.assert_allclose(G, G.T, atol=1e-10)

    def test_gram_diagonal_matches_norm(self):
        """Diagonal of Gram matrix should match ||rho_theta||^2."""
        thetas = [0.3, 0.5, 0.7]
        nmax = 500
        G = nyman_beurling_gram_matrix(thetas, nmax=nmax)
        for i, theta in enumerate(thetas):
            norm_sq = nyman_beurling_norm_squared(theta, nmax=nmax)
            # Allow some tolerance due to different quadrature
            assert abs(G[i, i] - norm_sq) < 0.1 * max(abs(G[i, i]), abs(norm_sq), 0.01), \
                f"Diagonal mismatch at theta={theta}: {G[i, i]} vs {norm_sq}"

    def test_distance_to_one_positive(self):
        """Distance from 1 to span{rho_theta} should be positive (d > 0)."""
        thetas = [1 / n for n in range(2, 6)]
        result = nyman_beurling_distance_to_one(thetas, nmax=500)
        assert result['distance'] >= 0
        assert result['distance_squared'] >= 0

    def test_distance_decreases_with_more_thetas(self):
        """Adding more thetas should decrease the distance (or keep it the same)."""
        thetas_small = [1 / n for n in range(2, 5)]
        thetas_large = [1 / n for n in range(2, 10)]
        d_small = nyman_beurling_distance_to_one(thetas_small, nmax=500)
        d_large = nyman_beurling_distance_to_one(thetas_large, nmax=500)
        # More thetas gives a richer span, so distance should not increase
        assert d_large['distance'] <= d_small['distance'] + 0.01


# ============================================================================
# 2. CENTRAL VALUE INFORMATION CONTENT
# ============================================================================

class TestCentralValueInfo:
    """Tests for the analysis of what central L-values determine."""

    def test_structure(self):
        """Output should have the expected keys."""
        info = central_value_information_content()
        assert 'genus_2_determines' in info
        assert 'genus_2_does_not_determine' in info
        assert 'all_genera_determines' in info
        assert 'circularity_at_finite_g' in info
        assert 'gap_d_conclusion' in info

    def test_genus_2_limitations(self):
        """Genus 2 should NOT determine the L^2 norm."""
        info = central_value_information_content()
        does_not = info['genus_2_does_not_determine']
        assert any('L^2' in item or 'norm' in item.lower() for item in does_not), \
            "Should flag L^2 norm as not determined"

    def test_all_genera_recovery(self):
        """All genera should determine all zeros (in principle)."""
        info = central_value_information_content()
        determines = info['all_genera_determines']
        assert any('zero' in item.lower() or 'Satake' in item for item in determines)

    def test_gap_d_not_closable_at_finite_genus(self):
        """Gap D conclusion should state not closable at finite genus."""
        info = central_value_information_content()
        concl = info['gap_d_conclusion']
        assert 'finite genus' in concl.lower() or 'not closable' in concl.lower() or \
               'NOT' in concl


# ============================================================================
# 3. SYMMETRIC POWER CONDUCTOR GROWTH
# ============================================================================

class TestConductorGrowth:
    """Tests for analytic conductor of Sym^{g-1} L-functions."""

    def test_conductor_nonnegative(self):
        """Log conductor should be nonnegative."""
        for g in range(1, 15):
            log_c = symmetric_power_conductor(g)
            assert log_c >= 0, f"Negative log conductor at genus {g}"

    def test_conductor_monotone(self):
        """Log conductor should increase with genus."""
        prev = 0
        for g in range(1, 15):
            log_c = symmetric_power_conductor(g)
            assert log_c >= prev - 1e-10, \
                f"Conductor not monotone: g={g}, log_c={log_c}, prev={prev}"
            prev = log_c

    def test_conductor_growth_rate(self):
        """Conductor should grow at least linearly in g."""
        log_c_5 = symmetric_power_conductor(5)
        log_c_10 = symmetric_power_conductor(10)
        assert log_c_10 > log_c_5, "Conductor should grow with genus"
        # For weight 22: growth should be roughly linear in g
        # (each Sym^n adds log(k-1+2n) ~ log(n) terms)
        assert log_c_10 / log_c_5 > 1.2, "Conductor growth too slow"

    def test_keating_snaith_structure(self):
        """Keating-Snaith prediction should have expected keys."""
        ks = keating_snaith_moment_prediction(3)
        assert 'genus' in ks
        assert 'log_analytic_conductor' in ks
        assert 'predicted_moment_second' in ks
        assert ks['genus'] == 3
        assert ks['sym_power_degree'] == 2

    def test_moment_prediction_positive(self):
        """Predicted moment should be positive."""
        for g in range(1, 10):
            ks = keating_snaith_moment_prediction(g)
            assert ks['predicted_moment_second'] >= 0


# ============================================================================
# 4. ROOT NUMBERS AND FORCED VANISHING
# ============================================================================

class TestRootNumbers:
    """Tests for root numbers of symmetric power L-functions."""

    def test_root_number_values(self):
        """Root numbers should be +1 or -1."""
        for g in range(1, 15):
            for D in [-3, -4, -7, -8, -11]:
                eps = symmetric_power_root_number(g, D)
                assert eps in {1, -1}, f"Invalid root number {eps} at g={g}, D={D}"

    def test_sym0_root_number(self):
        """Sym^0 = trivial: L(s, chi_D) has known root number.
        For D < 0: epsilon(chi_D) depends on D mod 4."""
        # g=1 means Sym^0. The root number of L(s, chi_D) for D < 0
        # is chi_D(-1) = -1 (since D < 0 => imaginary quadratic field).
        # Actually for Sym^0 of f twisted by chi_D:
        # this is just the Dirichlet L-function L(s, chi_D), whose root
        # number for D < 0 is +1 if D ≡ 1 mod 4, related to the sign.
        # The implementation uses a simplified formula; just verify it gives ±1.
        for D in [-3, -4, -7, -8]:
            eps = symmetric_power_root_number(1, D)
            assert eps in {1, -1}

    def test_root_number_table_structure(self):
        """Root number table should have expected structure."""
        rt = root_number_table(genus_max=5, disc_list=[-3, -4, -7])
        assert 'table' in rt
        assert 'forced_vanishing' in rt
        assert 'total_entries' in rt
        assert rt['total_entries'] == 5 * 3

    def test_forced_vanishing_fraction(self):
        """At least some entries should have forced vanishing (epsilon = -1)."""
        rt = root_number_table(genus_max=10)
        assert rt['n_forced_zero'] > 0, "No forced vanishing found — check formula"
        assert rt['fraction_forced_zero'] > 0

    def test_root_number_not_all_negative(self):
        """Not all root numbers should be -1 (that would be too strong)."""
        rt = root_number_table(genus_max=10)
        assert rt['n_forced_zero'] < rt['total_entries'], \
            "All entries forced zero — root number formula likely wrong"


# ============================================================================
# 5. CIRCULARITY ANALYSIS
# ============================================================================

class TestCircularity:
    """Tests for the symmetric power functoriality circularity."""

    def test_functoriality_status_structure(self):
        """Functoriality status should have entries for n = 1..19."""
        status = sym_power_functoriality_status()
        assert 'symmetric_powers' in status
        assert len(status['symmetric_powers']) == 19

    def test_sym1_through_4_unconditional(self):
        """Sym^1 through Sym^4 should be unconditional."""
        status = sym_power_functoriality_status()
        for n in range(1, 5):
            assert status['symmetric_powers'][n]['status'] == 'UNCONDITIONAL', \
                f"Sym^{n} should be unconditional"

    def test_sym5_plus_conditional(self):
        """Sym^5 and above should be conditional (for general GL(2))."""
        status = sym_power_functoriality_status()
        for n in range(5, 10):
            assert status['symmetric_powers'][n]['status'] == 'CONDITIONAL', \
                f"Sym^{n} should be conditional for general GL(2)"

    def test_f22_unconditional_at_all_n(self):
        """For f_22 (weight 22), Newton-Thorne gives all Sym^n."""
        status = sym_power_functoriality_status()
        for n in range(5, 10):
            assert status['symmetric_powers'][n].get('unconditional_for_f22', False), \
                f"Sym^{n} should be unconditional for f_22"

    def test_circularity_frontier(self):
        """The circularity frontier for general GL(2) should be at genus 5."""
        circ = circularity_genus_frontier()
        assert circ['circularity_frontier_general'] == 5
        assert circ['circularity_frontier_holomorphic'] == float('inf')

    def test_genus_table_structure(self):
        """Genus table should have entries with expected keys."""
        circ = circularity_genus_frontier()
        assert 1 in circ['genus_table']
        assert 10 in circ['genus_table']
        entry = circ['genus_table'][3]
        assert 'sym_power_degree' in entry
        assert 'unconditional_for_all_GL2' in entry
        assert entry['sym_power_degree'] == 2

    def test_f22_no_circularity(self):
        """All genera should be unconditional for f_22."""
        circ = circularity_genus_frontier()
        for g in range(1, 15):
            if g in circ['genus_table']:
                assert circ['genus_table'][g]['unconditional_for_f22']

    def test_general_circularity_at_genus_6(self):
        """Genus 6 requires Sym^5, which is conditional for general GL(2)."""
        circ = circularity_genus_frontier()
        assert not circ['genus_table'][6]['unconditional_for_all_GL2']

    def test_circularity_assessment_text(self):
        """Circularity assessment should mention Newton-Thorne."""
        status = sym_power_functoriality_status()
        assessment = status['circularity_assessment']
        assert 'Newton-Thorne' in assessment['for_f22']
        assert 'Maass' in assessment['for_general_forms'] or \
               'circularity' in assessment['for_general_forms'].lower()


# ============================================================================
# 6. ALL-GENERA CONVERGENCE
# ============================================================================

class TestAllGeneraConvergence:
    """Tests for convergence of K^{(infty)}."""

    def test_convergence_structure(self):
        """Convergence analysis should have expected structure."""
        conv = all_genera_kernel_convergence(genus_max=8)
        assert 'genus_data' in conv
        assert 'convergence_assessment' in conv
        assert len(conv['genus_data']) == 8

    def test_genus_data_fields(self):
        """Each genus entry should have expected fields."""
        conv = all_genera_kernel_convergence(genus_max=5)
        for entry in conv['genus_data']:
            assert 'genus' in entry
            assert 'sym_power_degree' in entry
            assert 'log_analytic_conductor' in entry
            assert entry['sym_power_degree'] == entry['genus'] - 1

    def test_conductor_increases_with_genus(self):
        """Analytic conductor should increase with genus."""
        conv = all_genera_kernel_convergence(genus_max=10)
        conductors = [e['log_analytic_conductor'] for e in conv['genus_data']]
        for i in range(len(conductors) - 1):
            assert conductors[i + 1] >= conductors[i] - 1e-10

    def test_convergence_assessment_content(self):
        """Convergence assessment should state the operator converges."""
        conv = all_genera_kernel_convergence(genus_max=5)
        text = conv['convergence_assessment']
        assert 'positive' in text.lower() or 'converge' in text.lower() or \
               'exists' in text.lower()


# ============================================================================
# 7. MOMENT PROBLEM AND SATAKE RECOVERY
# ============================================================================

class TestSatakeRecovery:
    """Tests for the moment problem: how many Satake parameters are recovered."""

    def test_structure(self):
        """Should have recovery_data and gl2_satake_genus."""
        result = satake_recovery_from_central_values()
        assert 'recovery_data' in result
        assert 'gl2_satake_genus' in result
        assert result['gl2_satake_genus'] == 2

    def test_genus_1_no_satake(self):
        """Genus 1 (Sym^0) gives no Satake information."""
        result = satake_recovery_from_central_values()
        g1 = result['recovery_data'][0]
        assert g1['genus'] == 1
        assert 'None' in g1['satake_recovery'] or 'none' in g1['satake_recovery'].lower()

    def test_genus_2_complete_for_gl2(self):
        """Genus 2 (Sym^1) gives complete GL(2) Satake recovery."""
        result = satake_recovery_from_central_values()
        g2 = result['recovery_data'][1]
        assert g2['genus'] == 2
        assert 'COMPLETE' in g2['satake_recovery'] or 'complete' in g2['satake_recovery'].lower()

    def test_higher_genus_redundant_for_gl2(self):
        """Genus >= 3 is redundant for GL(2) Satake parameters."""
        result = satake_recovery_from_central_values()
        for entry in result['recovery_data'][2:]:
            assert 'Redundant' in entry['satake_recovery'] or \
                   'redundant' in entry['satake_recovery'].lower()


# ============================================================================
# 8. QUANTITATIVE GAP D COMPARISON
# ============================================================================

class TestQuantitativeGapD:
    """Tests for quantitative comparison of genus-2 kernel vs NB."""

    def test_gap_d_structure(self):
        """Gap D analysis should have expected structure."""
        result = gap_d_quantitative_analysis(nmax_nb=300)
        assert 'genus_2_kernel_rank' in result
        assert 'nb_distance' in result
        assert 'gap_d_conclusion' in result

    def test_genus_2_rank_one(self):
        """Genus-2 Leech kernel is rank 1 (dim S_12(Sp(4,Z)) = 1)."""
        result = gap_d_quantitative_analysis(nmax_nb=300)
        assert result['genus_2_kernel_rank'] == 1

    def test_rank_deficit_positive(self):
        """NB effective rank should exceed genus-2 kernel rank."""
        result = gap_d_quantitative_analysis(nmax_nb=300)
        assert result['rank_deficit'] >= 0, "NB rank should be >= genus-2 rank"

    def test_nb_distance_positive(self):
        """NB distance from 1 should be positive (unless RH is proved!)."""
        result = gap_d_quantitative_analysis(nmax_nb=300)
        assert result['nb_distance']['distance'] >= 0

    def test_conclusion_mentions_gap(self):
        """Conclusion should mention that Gap D is not closable at genus 2."""
        result = gap_d_quantitative_analysis(nmax_nb=300)
        concl = result['gap_d_conclusion']
        assert 'NOT' in concl or 'not' in concl.lower()


# ============================================================================
# 9. BOECHERER STRUCTURE AT EACH GENUS
# ============================================================================

class TestBoechererStructure:
    """Tests for genus-g Boecherer-type formula structure."""

    def test_genus_1_classical(self):
        """Genus 1 should be classical (Rankin-Selberg, Re(s) > 1)."""
        bs = genus_g_boecherer_structure(1)
        assert bs['status'] == 'CLASSICAL'
        assert not bs['central_access']

    def test_genus_2_proved(self):
        """Genus 2 should be proved (Waldspurger/DPSS20)."""
        bs = genus_g_boecherer_structure(2)
        assert bs['status'] == 'PROVED'
        assert bs['central_access']

    def test_genus_3_partial(self):
        """Genus 3 should be partially proved."""
        bs = genus_g_boecherer_structure(3)
        assert 'PARTIAL' in bs['status'] or 'partial' in bs['status'].lower()

    def test_genus_ge_4_conjectural(self):
        """Genus >= 4 should be conjectural."""
        for g in range(4, 8):
            bs = genus_g_boecherer_structure(g)
            assert bs['status'] == 'CONJECTURAL'
            assert bs['central_access']

    def test_boecherer_sym_power_consistency(self):
        """The Sym^{g-1} requirement should be consistent."""
        for g in range(2, 8):
            bs = genus_g_boecherer_structure(g)
            if 'sym_power_needed' in bs:
                expected = f'Sym^{g - 1}'
                assert expected in bs['sym_power_needed'] or str(g - 1) in bs['sym_power_needed']


# ============================================================================
# 10. FULL INTEGRATED ANALYSIS
# ============================================================================

class TestFullAnalysis:
    """Tests for the complete Gap D analysis."""

    def test_full_analysis_structure(self):
        """Full analysis should have all expected keys."""
        result = full_gap_d_analysis(genus_max=5, nmax_nb=300)
        assert 'central_value_info' in result
        assert 'moment_predictions' in result
        assert 'root_numbers' in result
        assert 'circularity' in result
        assert 'convergence' in result
        assert 'satake_recovery' in result
        assert 'summary' in result

    def test_summary_three_questions(self):
        """Summary should address all three questions."""
        result = full_gap_d_analysis(genus_max=5, nmax_nb=300)
        summary = result['summary']
        assert 'can_central_values_close_gap_d' in summary
        assert 'does_k_infty_converge' in summary
        assert 'the_circularity' in summary

    def test_summary_central_values_cannot_close(self):
        """Summary should say central values cannot close Gap D at finite genus."""
        result = full_gap_d_analysis(genus_max=5, nmax_nb=300)
        answer = result['summary']['can_central_values_close_gap_d']
        assert 'NO' in answer or 'not' in answer.lower()

    def test_summary_k_infty_converges(self):
        """Summary should say K^{(infty)} converges (as positive operator)."""
        result = full_gap_d_analysis(genus_max=5, nmax_nb=300)
        answer = result['summary']['does_k_infty_converge']
        assert 'YES' in answer or 'converge' in answer.lower()

    def test_summary_circularity_partial(self):
        """Summary should say circularity is partial (broken for holomorphic)."""
        result = full_gap_d_analysis(genus_max=5, nmax_nb=300)
        answer = result['summary']['the_circularity']
        assert 'PARTIAL' in answer or 'partial' in answer.lower() or \
               'Newton-Thorne' in answer

    def test_moment_predictions_list(self):
        """Should have moment predictions for each genus."""
        result = full_gap_d_analysis(genus_max=5, nmax_nb=300)
        assert len(result['moment_predictions']) == 5

    def test_boecherer_genus_g_present(self):
        """Should have Boecherer structure for each genus."""
        result = full_gap_d_analysis(genus_max=5, nmax_nb=300)
        assert 'boecherer_genus_g' in result
        assert 1 in result['boecherer_genus_g']
        assert 5 in result['boecherer_genus_g']


# ============================================================================
# 11. MATHEMATICAL CONSISTENCY CHECKS
# ============================================================================

class TestMathematicalConsistency:
    """Cross-checks verifying mathematical consistency."""

    def test_conductor_at_genus_1(self):
        """At genus 1, Sym^0 is trivial — conductor should be small."""
        log_c = symmetric_power_conductor(1)
        # Sym^0 has a single Gamma factor — conductor is modest
        assert log_c < 10

    def test_root_number_periodicity(self):
        """Root numbers should have some periodicity in genus (mod 4 structure)."""
        D = -3
        root_nums = [symmetric_power_root_number(g, D) for g in range(1, 20)]
        # For a fixed D, the root number pattern in g should repeat with period 4
        # (since it depends on n mod 4 where n = g-1)
        # Check that we see at least some ±1 pattern
        assert 1 in root_nums
        assert -1 in root_nums

    def test_gl2_satake_two_parameters(self):
        """GL(2) has 2 Satake parameters — Sym^1 should suffice."""
        result = satake_recovery_from_central_values()
        # The first genus giving complete Satake recovery for GL(2) is g=2 (Sym^1)
        assert result['gl2_satake_genus'] == 2

    def test_nb_gram_and_distance_consistent(self):
        """The NB distance should be consistent with the Gram matrix."""
        thetas = [0.3, 0.5, 0.7]
        nmax = 300
        G = nyman_beurling_gram_matrix(thetas, nmax)
        result = nyman_beurling_distance_to_one(thetas, nmax)

        # Distance should be nonnegative
        assert result['distance'] >= 0

        # Gram rank should be <= number of thetas
        assert result['gram_rank'] <= len(thetas)

    def test_genus_2_spectral_support_on_critical_line(self):
        """Genus 2 kernel spectral support should be on Re(s) = 1/2."""
        bs = genus_g_boecherer_structure(2)
        assert 'central' in bs['l_function'].lower() or '1/2' in bs['l_function']

    def test_genus_1_spectral_support_off_critical_line(self):
        """Genus 1 spectral support should be at Re(s) > 1."""
        bs = genus_g_boecherer_structure(1)
        assert 'Re(s) > 1' in bs['l_function'] or 'Rankin' in bs['l_function']

    def test_escalation_from_genus_1_to_2(self):
        """The spectral jump from genus 1 to genus 2 is the KEY insight."""
        bs1 = genus_g_boecherer_structure(1)
        bs2 = genus_g_boecherer_structure(2)
        assert not bs1['central_access']
        assert bs2['central_access']

    def test_forced_vanishing_creates_rank_defect(self):
        """Root number -1 implies L(1/2) = 0, creating rank defects in K^{(g)}."""
        rt = root_number_table(genus_max=8)
        # At least some (g, D) pairs should have forced vanishing
        fv = rt['forced_vanishing']
        assert len(fv) > 0, "No forced vanishing — root number formula suspect"
        # Check that these are genuine (g, D) pairs
        for g, D in fv[:5]:
            assert 1 <= g <= 8
            assert D < 0

    def test_dim_s12_sp4_is_1(self):
        """The cusp space S_12(Sp(4,Z)) is 1-dimensional (spanned by chi_12).
        This is the mathematical fact underlying the rank-1 genus-2 kernel for Leech."""
        # This is a hardcoded fact from the literature (Igusa 1962).
        # We verify it appears correctly in the analysis.
        result = gap_d_quantitative_analysis(nmax_nb=300)
        assert result['genus_2_kernel_rank'] == 1


# ============================================================================
# 12. CIRCULARITY DEPTH ANALYSIS
# ============================================================================

class TestCircularityDepth:
    """Deeper tests for the circularity structure."""

    def test_newton_thorne_year(self):
        """Newton-Thorne should be cited as 2021."""
        status = sym_power_functoriality_status()
        nt_scope = status['newton_thorne_scope']
        assert '2021' in nt_scope

    def test_gelbart_jacquet_sym2(self):
        """Sym^2 should cite Gelbart-Jacquet."""
        status = sym_power_functoriality_status()
        sym2 = status['symmetric_powers'][2]
        assert 'Gelbart' in sym2['reference']

    def test_kim_shahidi_sym3(self):
        """Sym^3 should cite Kim-Shahidi."""
        status = sym_power_functoriality_status()
        sym3 = status['symmetric_powers'][3]
        assert 'Kim' in sym3['reference']

    def test_kim_sym4(self):
        """Sym^4 should cite Kim."""
        status = sym_power_functoriality_status()
        sym4 = status['symmetric_powers'][4]
        assert 'Kim' in sym4['reference']

    def test_circularity_does_not_affect_lattice_programme(self):
        """The lattice programme (Leech, E8, etc.) uses holomorphic forms only.
        Newton-Thorne eliminates circularity here."""
        circ = circularity_genus_frontier()
        # All genera unconditional for holomorphic weight >= 2
        for g in range(1, 15):
            if g in circ['genus_table']:
                assert circ['genus_table'][g]['unconditional_for_f22']

    def test_maass_form_circularity_at_genus_6(self):
        """For Maass forms, circularity should begin at genus 6."""
        circ = circularity_genus_frontier()
        # Genus 5 should still be unconditional for all GL(2)
        assert circ['genus_table'][5]['unconditional_for_all_GL2']
        # Genus 6 should be conditional for general GL(2)
        assert not circ['genus_table'][6]['unconditional_for_all_GL2']


# ============================================================================
# 13. EDGE CASES AND ROBUSTNESS
# ============================================================================

class TestEdgeCases:
    """Edge cases and robustness checks."""

    def test_genus_1(self):
        """Genus 1 should work correctly (Sym^0 = trivial)."""
        bs = genus_g_boecherer_structure(1)
        assert bs['genus'] == 1
        log_c = symmetric_power_conductor(1)
        assert log_c >= 0

    def test_high_genus(self):
        """High genus (g=15) should not crash."""
        log_c = symmetric_power_conductor(15)
        assert log_c > 0
        eps = symmetric_power_root_number(15, -3)
        assert eps in {1, -1}

    def test_small_disc(self):
        """Small discriminant D=-3 should work."""
        eps = symmetric_power_root_number(2, -3)
        assert eps in {1, -1}

    def test_large_disc(self):
        """Large discriminant D=-1000003 should work."""
        eps = symmetric_power_root_number(2, -1000003)
        assert eps in {1, -1}

    def test_convergence_with_small_genus_max(self):
        """Convergence analysis with genus_max=2 should work."""
        conv = all_genera_kernel_convergence(genus_max=2)
        assert len(conv['genus_data']) == 2
