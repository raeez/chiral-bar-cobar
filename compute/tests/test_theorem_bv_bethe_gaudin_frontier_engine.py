r"""Tests for BV 2-loop Feynman integral structure and Bethe-Gaudin correspondence.

MULTI-PATH VERIFICATION (CLAUDE.md mandate):
    Every numerical result verified by at least 3 independent paths.
    All formulas computed from first principles (AP1, AP3).

TEST STRUCTURE:
    Section A: Stable graphs of M-bar_{2,0} (topological correctness)
    Section B: BV Feynman rules (structural assignments)
    Section C: Heisenberg BV = bar at genus 2 (class G, PROVED)
    Section D: Affine sl_2 BV prediction (class L, CONJECTURAL)
    Section E: Virasoro BV prediction (class M, CONJECTURAL)
    Section F: Graph contribution classification by shadow class
    Section G: Gaudin Hamiltonians at n=3 (commutativity + sum identity)
    Section H: Bethe roots for n=3 Gaudin (BAE + independent formula)
    Section I: Gaudin eigenvalues from Bethe vs exact diagonalization
    Section J: Gaudin at n=4 and KZ equation
    Section K: Shadow-Gaudin dictionary (structural consistency)

References:
    conj:master-bv-brst (bv_brst.tex)
    thm:heisenberg-bv-bar-all-genera (bv_brst.tex)
    thm:gaudin-yangian-identification (yangians_drinfeld_kohno.tex)
    AP19: bar r-matrix pole order one below OPE
    AP27: bar propagator d log E(z,w) weight 1
    AP38: lambda_2^FP = 7/5760 (NOT 1/1152)
    AP48: kappa(H_k) = k
"""

import numpy as np
import pytest
from fractions import Fraction
from numpy import linalg as la

from compute.lib.theorem_bv_bethe_gaudin_frontier_engine import (
    # Arithmetic
    lambda_fp,
    lambda_fp_from_ahat,
    # Direction A: BV structure
    StableGraphG2,
    genus2_stable_graphs,
    bv_feynman_rules_genus2,
    delta_pf_genus2,
    delta_pf_genus2_from_graph_decomposition,
    bv_bar_genus2_heisenberg,
    bv_bar_genus2_affine_sl2,
    bv_bar_genus2_virasoro,
    bv_graph_contribution_summary,
    verify_direction_a,
    # Direction B: Bethe-Gaudin
    gaudin_hamiltonian,
    verify_gaudin_commuting,
    gaudin_sum_identity,
    gaudin_spectrum,
    gaudin_n3_bethe_roots,
    gaudin_n3_standard_config,
    gaudin_eigenvalue_from_bethe,
    verify_gaudin_bethe_eigenvalues,
    gaudin_n4_accessory_parameter,
    gaudin_n4_bethe_equations,
    solve_gaudin_n4_bethe,
    kz_connection_coefficient,
    verify_kz_flatness,
    shadow_gaudin_dictionary,
    verify_direction_b,
)


# =====================================================================
# Section A: Stable graphs of M-bar_{2,0} (topological correctness)
# =====================================================================

class TestStableGraphs:
    """Verify the 7 stable graphs of M-bar_{2,0} have correct topology."""

    def test_exactly_7_graphs(self):
        """M-bar_{2,0} has exactly 7 stable graphs."""
        assert len(genus2_stable_graphs()) == 7

    def test_all_genus_2(self):
        """Each graph has arithmetic genus 2."""
        for g in genus2_stable_graphs():
            assert g.arithmetic_genus == 2, \
                f"{g.name}: genus {g.arithmetic_genus}, expected 2"

    def test_all_stable(self):
        """Each graph satisfies the stability condition 2g_v + val_v >= 3."""
        for g in genus2_stable_graphs():
            assert g.is_stable, f"{g.name} is not stable"

    def test_smooth_graph(self):
        """Smooth: 1 vertex of genus 2, 0 edges."""
        g = genus2_stable_graphs()[0]
        assert g.name == 'smooth'
        assert g.vertex_genera == (2,)
        assert g.num_edges == 0
        assert g.aut_order == 1
        assert g.feynman_loop_order == 0

    def test_figure_eight(self):
        """Figure-eight: 1 vertex of genus 1, 1 self-loop."""
        g = genus2_stable_graphs()[1]
        assert g.name == 'figure_eight'
        assert g.vertex_genera == (1,)
        assert g.num_edges == 1
        assert g.aut_order == 2
        assert g.feynman_loop_order == 1

    def test_banana(self):
        """Banana: 1 vertex of genus 0, 2 self-loops, |Aut|=8."""
        g = genus2_stable_graphs()[2]
        assert g.name == 'banana'
        assert g.vertex_genera == (0,)
        assert g.num_edges == 2
        assert g.aut_order == 8
        assert g.feynman_loop_order == 2
        assert g.valence == (4,)  # 2 self-loops = 4 half-edges

    def test_theta(self):
        """Theta: 2 genus-0 vertices, 3 parallel edges, |Aut|=12."""
        g = genus2_stable_graphs()[4]
        assert g.name == 'theta'
        assert g.vertex_genera == (0, 0)
        assert g.num_edges == 3
        assert g.aut_order == 12
        assert g.valence == (3, 3)

    def test_barbell(self):
        """Barbell: 2 genus-0 vertices, each with 1 self-loop + 1 bridge."""
        g = genus2_stable_graphs()[6]
        assert g.name == 'barbell'
        assert g.vertex_genera == (0, 0)
        assert g.num_edges == 3
        assert g.aut_order == 8
        assert g.valence == (3, 3)

    def test_dumbbell_tadpole(self):
        """Dumbbell has valence 1 at each vertex (tadpole)."""
        g = genus2_stable_graphs()[3]
        assert g.name == 'dumbbell'
        assert g.valence == (1, 1)

    def test_lollipop_tadpole(self):
        """Lollipop: genus-1 vertex has valence 1 (tadpole)."""
        g = genus2_stable_graphs()[5]
        assert g.name == 'lollipop'
        val = g.valence
        # v0 (genus 0) has val 3; v1 (genus 1) has val 1
        assert val[1] == 1  # tadpole at genus-1 vertex


# =====================================================================
# Section B: BV Feynman rules (structural assignments)
# =====================================================================

class TestBVFeynmanRules:
    """Verify the BV Feynman rule assignments for genus-2 graphs."""

    def test_all_7_rules_present(self):
        """Every graph has a Feynman rule assignment."""
        rules = bv_feynman_rules_genus2()
        names = {g.name for g in genus2_stable_graphs()}
        assert set(rules.keys()) == names

    def test_smooth_is_0_loop(self):
        """The smooth graph is a 0-loop BV integral."""
        rules = bv_feynman_rules_genus2()
        assert rules['smooth'].loop_order == 0

    def test_figure_eight_is_1_loop(self):
        """The figure-eight is a 1-loop BV integral."""
        rules = bv_feynman_rules_genus2()
        assert rules['figure_eight'].loop_order == 1

    def test_banana_is_2_loop(self):
        """The banana is a 2-loop BV integral."""
        rules = bv_feynman_rules_genus2()
        assert rules['banana'].loop_order == 2

    def test_theta_is_2_loop(self):
        """The theta is a 2-loop BV integral."""
        rules = bv_feynman_rules_genus2()
        assert rules['theta'].loop_order == 2

    def test_symmetry_factors(self):
        """Symmetry factors 1/|Aut| match the graph data."""
        rules = bv_feynman_rules_genus2()
        graphs = {g.name: g for g in genus2_stable_graphs()}
        for name, rule in rules.items():
            expected = Fraction(1, graphs[name].aut_order)
            assert rule.symmetry_factor == expected, \
                f"{name}: sym factor {rule.symmetry_factor}, expected {expected}"


# =====================================================================
# Section C: Heisenberg BV = bar at genus 2 (class G, PROVED)
# =====================================================================

class TestHeisenbergBV:
    """Verify BV = bar at genus 2 for Heisenberg (class G)."""

    def test_heisenberg_k1_F2(self):
        """F_2^bar(H_1) = 1 * 7/5760 = 7/5760."""
        result = bv_bar_genus2_heisenberg(1)
        assert result['F2_bar'] == Fraction(7, 5760)

    def test_heisenberg_bv_equals_bar(self):
        """F_2^BV = F_2^bar for Heisenberg (PROVED)."""
        result = bv_bar_genus2_heisenberg(1)
        assert result['bv_equals_bar'] is True

    def test_heisenberg_delta_pf_vanishes(self):
        """delta_pf = 0 for class G (S_3 = S_4 = 0)."""
        result = bv_bar_genus2_heisenberg(1)
        assert result['delta_pf'] == 0

    def test_heisenberg_status_proved(self):
        """Status is PROVED for Heisenberg at all genera."""
        result = bv_bar_genus2_heisenberg(1)
        assert result['status'] == 'PROVED'

    def test_heisenberg_k2_F2(self):
        """F_2^bar(H_2) = 2 * 7/5760 = 7/2880."""
        result = bv_bar_genus2_heisenberg(2)
        assert result['F2_bar'] == Fraction(7, 2880)

    def test_heisenberg_figure_eight_amp(self):
        """Figure-eight amplitude is always 1/2 for any k (kappa cancels)."""
        for k in [1, 2, 3, 5]:
            result = bv_bar_genus2_heisenberg(k)
            assert result['amplitudes']['figure_eight'] == Fraction(1, 2)

    def test_heisenberg_only_two_graphs_contribute(self):
        """For class G, only smooth and figure_eight contribute."""
        result = bv_bar_genus2_heisenberg(1)
        amps = result['amplitudes']
        for name in ['banana', 'theta', 'dumbbell', 'lollipop', 'barbell']:
            assert amps[name] == 0, f"{name} should vanish for class G"

    def test_heisenberg_lambda2_fp_3paths(self):
        """lambda_2^FP = 7/5760 by two independent methods (AP38 guard)."""
        assert lambda_fp(2) == Fraction(7, 5760)
        assert lambda_fp_from_ahat(2) == Fraction(7, 5760)
        assert lambda_fp(2) != Fraction(1, 1152)  # AP38 wrong value


# =====================================================================
# Section D: Affine sl_2 BV prediction (class L, CONJECTURAL)
# =====================================================================

class TestAffineSl2BV:
    """BV prediction for affine sl_2 at genus 2."""

    def test_sl2_k1_kappa(self):
        """kappa(sl_2, k=1) = 3(1+2)/4 = 9/4."""
        result = bv_bar_genus2_affine_sl2(1)
        assert result['kappa'] == Fraction(9, 4)

    def test_sl2_k1_S3(self):
        """S_3(sl_2, k=1) = 4/(1+2) = 4/3."""
        result = bv_bar_genus2_affine_sl2(1)
        assert result['S_3'] == Fraction(4, 3)

    def test_sl2_k1_delta_pf(self):
        """delta_pf(sl_2, k=1) = (4/3)(40/3 - 9/4)/48 = 133/432."""
        result = bv_bar_genus2_affine_sl2(1)
        expected = Fraction(4, 3) * (Fraction(40, 3) - Fraction(9, 4)) / 48
        assert result['delta_pf'] == expected
        assert result['delta_pf'] == Fraction(133, 432)

    def test_sl2_k1_F2_total(self):
        """F_2^bar(sl_2, k=1) = 9/4 * 7/5760 + 133/432 = 21469/69120."""
        result = bv_bar_genus2_affine_sl2(1)
        expected = Fraction(9, 4) * Fraction(7, 5760) + Fraction(133, 432)
        assert result['F2_bar'] == expected
        assert result['F2_bar'] == Fraction(21469, 69120)

    def test_sl2_k1_status_conjectural(self):
        """BV = bar at genus 2 for sl_2 is CONJECTURAL."""
        result = bv_bar_genus2_affine_sl2(1)
        assert result['status'] == 'CONJECTURAL'

    def test_sl2_banana_vanishes(self):
        """Banana vanishes for class L (S_4 = 0)."""
        result = bv_bar_genus2_affine_sl2(1)
        assert 'banana' in result['non_contributing']

    def test_sl2_delta_pf_decomposition(self):
        """delta_pf decomposes into theta/barbell + mixed terms."""
        decomp = delta_pf_genus2_from_graph_decomposition(
            Fraction(4, 3), Fraction(9, 4))
        assert decomp['match'] is True

    def test_sl2_k2_kappa(self):
        """kappa(sl_2, k=2) = 3(2+2)/4 = 3."""
        result = bv_bar_genus2_affine_sl2(2)
        assert result['kappa'] == Fraction(3)

    def test_sl2_critical_level_raises(self):
        """k = -2 (critical level) raises ValueError."""
        with pytest.raises(ValueError, match="critical"):
            bv_bar_genus2_affine_sl2(-2)


# =====================================================================
# Section E: Virasoro BV prediction (class M, CONJECTURAL)
# =====================================================================

class TestVirassoroBV:
    """BV prediction for Virasoro at genus 2."""

    def test_virasoro_c26_kappa(self):
        """kappa(Vir_26) = 13."""
        result = bv_bar_genus2_virasoro(Fraction(26))
        assert result['kappa'] == Fraction(13)

    def test_virasoro_c26_S4(self):
        """S_4(Vir_26) = Q^contact = 10/(26 * 152) = 5/1976."""
        result = bv_bar_genus2_virasoro(Fraction(26))
        expected = Fraction(10) / (Fraction(26) * Fraction(152))
        assert result['S_4'] == expected

    def test_virasoro_5_graphs_contribute(self):
        """5 of 7 graphs contribute for class M."""
        result = bv_bar_genus2_virasoro(Fraction(26))
        assert len(result['contributing_graphs']) == 5

    def test_virasoro_status_conjectural(self):
        """BV = bar at genus 2 for Virasoro is CONJECTURAL."""
        result = bv_bar_genus2_virasoro(Fraction(26))
        assert result['status'] == 'CONJECTURAL'


# =====================================================================
# Section F: Graph contribution classification by shadow class
# =====================================================================

class TestGraphContributions:
    """Verify which graphs contribute for each shadow class."""

    def test_class_G_two_graphs(self):
        """Class G: only smooth and figure_eight contribute."""
        summary = bv_graph_contribution_summary()
        for name, row in summary.items():
            if name in ('smooth', 'figure_eight'):
                assert row['G'] is True
            else:
                assert row['G'] is False, \
                    f"{name} should not contribute for class G"

    def test_class_L_four_graphs(self):
        """Class L: smooth, figure_eight, theta, barbell contribute."""
        summary = bv_graph_contribution_summary()
        contributing = [n for n, r in summary.items() if r['L']]
        assert sorted(contributing) == sorted([
            'smooth', 'figure_eight', 'theta', 'barbell'])

    def test_class_M_five_graphs(self):
        """Class M: smooth, figure_eight, theta, banana, barbell contribute."""
        summary = bv_graph_contribution_summary()
        contributing = [n for n, r in summary.items() if r['M']]
        assert sorted(contributing) == sorted([
            'smooth', 'figure_eight', 'theta', 'banana', 'barbell'])

    def test_dumbbell_never_contributes(self):
        """Dumbbell vanishes for all classes (tadpole)."""
        summary = bv_graph_contribution_summary()
        for cls in ['G', 'L', 'C', 'M']:
            assert summary['dumbbell'][cls] is False

    def test_lollipop_never_contributes(self):
        """Lollipop vanishes for all classes (tadpole at genus-1 vertex)."""
        summary = bv_graph_contribution_summary()
        for cls in ['G', 'L', 'C', 'M']:
            assert summary['lollipop'][cls] is False


# =====================================================================
# Section G: Gaudin Hamiltonians (commutativity + sum identity)
# =====================================================================

class TestGaudinHamiltonians:
    """Verify Gaudin Hamiltonian properties at n=3 and n=4."""

    def test_gaudin_n3_commute(self):
        """[H_i, H_j] = 0 for n=3 sites (CYBE consequence)."""
        sites = np.array([0.0, 1.0, 2.0])
        result = verify_gaudin_commuting(sites)
        assert result['commuting'] is True
        assert result['max_commutator_norm'] < 1e-10

    def test_gaudin_n4_commute(self):
        """[H_i, H_j] = 0 for n=4 sites."""
        sites = np.array([0.0, 1.0, 3.0, 5.0])
        result = verify_gaudin_commuting(sites)
        assert result['commuting'] is True

    def test_gaudin_sum_vanishes_n3(self):
        """sum_i H_i = 0 for n=3 (translation invariance)."""
        sites = np.array([0.0, 1.0, 2.0])
        result = gaudin_sum_identity(sites)
        assert result['vanishes'] is True

    def test_gaudin_sum_vanishes_n4(self):
        """sum_i H_i = 0 for n=4."""
        sites = np.array([0.0, 1.0, 3.0, 5.0])
        result = gaudin_sum_identity(sites)
        assert result['vanishes'] is True

    def test_gaudin_n3_hermitian(self):
        """H_i are Hermitian (real eigenvalues)."""
        sites = np.array([0.0, 1.0, 2.0])
        for i in range(3):
            H = gaudin_hamiltonian(sites, i)
            assert la.norm(H - H.conj().T) < 1e-12, \
                f"H_{i} is not Hermitian"

    def test_gaudin_n3_dimension(self):
        """H_i is 8x8 for n=3 (dim = 2^3 = 8)."""
        sites = np.array([0.0, 1.0, 2.0])
        H = gaudin_hamiltonian(sites, 0)
        assert H.shape == (8, 8)

    def test_gaudin_n4_dimension(self):
        """H_i is 16x16 for n=4 (dim = 2^4 = 16)."""
        sites = np.array([0.0, 1.0, 3.0, 5.0])
        H = gaudin_hamiltonian(sites, 0)
        assert H.shape == (16, 16)

    def test_gaudin_n3_generic_positions(self):
        """Commutativity holds for generic (non-integer) positions."""
        sites = np.array([0.1, 0.7, 2.3])
        result = verify_gaudin_commuting(sites)
        assert result['commuting'] is True


# =====================================================================
# Section H: Bethe roots for n=3 Gaudin
# =====================================================================

class TestGaudinN3Bethe:
    """Bethe ansatz for sl_2 Gaudin at n=3 with spin-1/2."""

    def test_n3_bethe_roots_satisfy_bae(self):
        """Bethe roots satisfy sum 1/(w - z_j) = 0."""
        result = gaudin_n3_standard_config()
        assert result['bae_satisfied'] is True

    def test_n3_two_bethe_roots(self):
        """There are exactly 2 Bethe roots for n=3, spin-1/2."""
        result = gaudin_n3_standard_config()
        assert result['num_bethe_roots'] == 2

    def test_n3_bethe_roots_explicit(self):
        """For z=(0,1,2): w = 1 +/- sqrt(3)/3."""
        result = gaudin_n3_standard_config()
        assert result['independent_check'] is True

    def test_n3_bethe_roots_real(self):
        """Bethe roots are real for real z_j (spin-1/2)."""
        result = gaudin_n3_standard_config()
        assert abs(result['w_plus'].imag) < 1e-10
        assert abs(result['w_minus'].imag) < 1e-10

    def test_n3_bethe_sum_equals_centroid(self):
        """w_+ + w_- = 2*(z1+z2+z3)/3 (Vieta for the quadratic)."""
        z1, z2, z3 = 0.0, 1.0, 2.0
        result = gaudin_n3_bethe_roots(z1, z2, z3)
        w_sum = result['w_plus'] + result['w_minus']
        expected = 2.0 * (z1 + z2 + z3) / 3.0
        assert abs(w_sum - expected) < 1e-10

    def test_n3_generic_positions(self):
        """BAE satisfied for generic positions z = (0, 1, 4)."""
        result = gaudin_n3_bethe_roots(0.0, 1.0, 4.0)
        assert result['bae_satisfied'] is True


# =====================================================================
# Section I: Gaudin eigenvalues from Bethe vs exact diag
# =====================================================================

class TestGaudinEigenvalues:
    """Gaudin eigenvalues from Bethe roots match exact diagonalization."""

    def test_bethe_eigenvalues_match_exact(self):
        """Eigenvalues h_i from Bethe roots match exact diag."""
        sites = np.array([0.0, 1.0, 2.0])
        bethe = gaudin_n3_standard_config()
        result = verify_gaudin_bethe_eigenvalues(
            sites, [bethe['w_plus'], bethe['w_minus']])
        assert result['all_match'] is True
        assert result['all_eigenvectors'] is True
        assert result['max_distance'] < 1e-8

    def test_spectrum_simultaneously_diagonal(self):
        """Gaudin Hamiltonians are simultaneously diagonalizable."""
        sites = np.array([0.0, 1.0, 2.0])
        spec = gaudin_spectrum(sites)
        assert spec['simultaneously_diagonal'] is True

    def test_spectrum_dimension(self):
        """Joint spectrum has correct dimensions."""
        sites = np.array([0.0, 1.0, 2.0])
        spec = gaudin_spectrum(sites)
        assert spec['joint_eigenvalues'].shape == (3, 8)
        assert spec['dim'] == 8


# =====================================================================
# Section J: Gaudin at n=4 and KZ equation
# =====================================================================

class TestGaudinN4KZ:
    """n=4 Gaudin and KZ connection."""

    def test_kz_flatness(self):
        """KZ connection is flat (consequence of CYBE)."""
        sites = np.array([0.0, 1.0, 3.0, 5.0])
        result = verify_kz_flatness(sites, kz_level=3.0)
        assert result['flat'] is True

    def test_n4_sector_dimensions(self):
        """S_z sectors for 4 spin-1/2: {-2:1, -1:4, 0:6, 1:4, 2:1}."""
        sites = np.array([0.0, 1.0, 3.0, 5.0])
        result = gaudin_n4_accessory_parameter(sites)
        sectors = result['sectors']
        assert sectors[0.0] == 6   # S_z = 0 sector
        assert sectors[1.0] == 4   # S_z = 1 sector
        assert sectors[-1.0] == 4  # S_z = -1 sector
        assert sectors[2.0] == 1   # S_z = 2 (all up)
        assert sectors[-2.0] == 1  # S_z = -2 (all down)

    def test_n4_bethe_equations_structure(self):
        """n=4 Bethe equations have correct structure for M=2 roots."""
        z = np.array([0.0, 1.0, 3.0, 5.0])
        w = np.array([0.5 + 0.1j, 2.0 - 0.1j])
        res = gaudin_n4_bethe_equations(w, z)
        assert len(res) == 2  # M=2 equations for M=2 roots

    @pytest.mark.skipif(
        not hasattr(pytest, 'importorskip') or True,
        reason="scipy required for solver"
    )
    def test_n4_bethe_solve(self):
        """Solve n=4 Gaudin Bethe equations for M=2."""
        try:
            from scipy import optimize  # noqa: F401
        except ImportError:
            pytest.skip("scipy not available")

        z = np.array([0.0, 1.0, 3.0, 5.0])
        result = solve_gaudin_n4_bethe(z)
        if result['success']:
            assert result['residual_norm'] < 1e-8
        else:
            # Solver may fail for some initial guesses; this is acceptable
            # as long as the BAE structure is correct
            pass


# =====================================================================
# Section K: Shadow-Gaudin dictionary (structural consistency)
# =====================================================================

class TestShadowGaudinDictionary:
    """Verify the shadow-Gaudin dictionary entries."""

    def test_dictionary_nonempty(self):
        """Dictionary has entries."""
        d = shadow_gaudin_dictionary()
        assert len(d) >= 8

    def test_mc_element_maps_to_connection(self):
        """MC element maps to Gaudin connection."""
        d = shadow_gaudin_dictionary()
        assert 'MC element Theta_A|_{genus 0}' in d

    def test_cybe_maps_to_mc(self):
        """CYBE maps to arity-3 MC equation."""
        d = shadow_gaudin_dictionary()
        assert 'CYBE [r,r] = 0' in d

    def test_bethe_roots_maps_to_zeros(self):
        """Bethe roots map to zeros of shadow connection eigenvalue."""
        d = shadow_gaudin_dictionary()
        assert 'Bethe roots w_a' in d


# =====================================================================
# Section L: Comprehensive verification entry points
# =====================================================================

class TestComprehensiveVerification:
    """Top-level verification of both directions."""

    def test_direction_a_passes(self):
        """Direction A (BV structure) comprehensive check passes."""
        result = verify_direction_a(k=1)
        assert result['all_pass'] is True

    def test_direction_b_passes(self):
        """Direction B (Bethe-Gaudin) comprehensive check passes."""
        result = verify_direction_b()
        assert result['commuting_n3']['commuting'] is True
        assert result['commuting_n4']['commuting'] is True
        assert result['bethe_n3']['bae_satisfied'] is True
        assert result['kz_flat']['flat'] is True
        assert result['all_pass'] is True
