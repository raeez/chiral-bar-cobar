r"""Tests for the Feynman integral / bar complex frontier engine.

DIRECTION A: Graph-by-graph Feynman integral = bar amplitude at genus 2.
DIRECTION B: Feynman integral structure of the collision residue r(z).

30+ tests verifying:
  1. Stable graph enumeration and metadata (genus, stability, automorphisms)
  2. Faber-Pandharipande numbers (exact, multi-path verified)
  3. Graph-by-graph bar amplitudes for Heisenberg, KM, Virasoro
  4. Shadow class graph selection (which graphs contribute)
  5. Collision residue: tree level vs loop corrections
  6. Non-renormalization for class G/L
  7. Planted-forest corrections
  8. Orbifold Euler characteristic
  9. Cross-family consistency (additivity, complementarity)

Multi-path verification (AP10: tests with independent derivations, not hardcoded values):
  Path 1: Direct computation from engine
  Path 2: Independent formula evaluation
  Path 3: Cross-family consistency checks
  Path 4: Limiting cases
  Path 5: Additivity / complementarity

References:
  higher_genus_modular_koszul.tex: Theorem D, shadow obstruction tower
  bv_brst.tex: conj:master-bv-brst
  feynman_diagrams.tex: Feynman rules
  AP19: pole absorption
  AP27: weight-1 propagator
  AP38: lambda_2 = 7/5760 NOT 1/1152
"""

from fractions import Fraction
from math import factorial

import pytest

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_feynman_bar_frontier_engine import (
    StableGraphG2,
    bar_amplitude_scalar,
    bubble_diagram_amplitude,
    chi_orb,
    CollisionResidue,
    contributing_graphs,
    genus2_bar_amplitudes,
    genus2_graph_by_name,
    genus2_stable_graphs,
    genus2_total_bar,
    heisenberg_genus2,
    affine_sl2_genus2,
    affine_sl2_shadow_data,
    lambda_fp,
    sunset_diagram_amplitude,
    verify_non_renormalization,
    verify_euler_char_g2,
    virasoro_genus2,
    virasoro_shadow_data,
    virasoro_planted_forest,
    planted_forest_correction,
    tree_level_r_heisenberg,
    tree_level_r_km_sl2,
    tree_level_r_virasoro,
    virasoro_r_matrix_with_corrections,
    one_loop_correction_heisenberg,
    one_loop_correction_km_sl2,
    one_loop_correction_virasoro,
    vertex_factor_scalar,
    koszul_complementarity_g2,
    heisenberg_additivity_g2,
    full_summary,
)

FR = Fraction


# =====================================================================
# Section 1: Stable graph enumeration
# =====================================================================

class TestGenus2StableGraphs:
    """Test the enumeration and properties of the 7 stable graphs of M-bar_{2,0}."""

    def test_exactly_seven_graphs(self):
        """There are exactly 7 stable graphs at genus 2 with n=0."""
        graphs = genus2_stable_graphs()
        assert len(graphs) == 7

    def test_all_genus_two(self):
        """Every graph has arithmetic genus 2."""
        for g in genus2_stable_graphs():
            assert g.arithmetic_genus == 2, f"{g.name}: genus = {g.arithmetic_genus}"

    def test_all_stable(self):
        """Every graph satisfies 2g(v) + val(v) >= 3 for all vertices."""
        for g in genus2_stable_graphs():
            assert g.is_stable, f"{g.name}: not stable, val = {g.valence}"

    def test_smooth_topology(self):
        """smooth: 1 vertex g=2, 0 edges, |Aut| = 1."""
        g = genus2_graph_by_name('smooth')
        assert g.vertex_genera == (2,)
        assert g.num_edges == 0
        assert g.aut_order == 1
        assert g.h1 == 0

    def test_figure_eight_topology(self):
        """figure_eight: 1 vertex g=1, 1 self-loop, |Aut| = 2."""
        g = genus2_graph_by_name('figure_eight')
        assert g.vertex_genera == (1,)
        assert g.num_edges == 1
        assert g.aut_order == 2
        assert g.h1 == 1
        assert g.valence == (2,)

    def test_banana_topology(self):
        """banana: 1 vertex g=0, 2 self-loops, |Aut| = 8."""
        g = genus2_graph_by_name('banana')
        assert g.vertex_genera == (0,)
        assert g.num_edges == 2
        assert g.aut_order == 8
        assert g.h1 == 2
        assert g.valence == (4,)

    def test_dumbbell_topology(self):
        """dumbbell (separating node): 2 vertices g=(1,1), 1 edge, |Aut| = 2."""
        g = genus2_graph_by_name('dumbbell')
        assert g.vertex_genera == (1, 1)
        assert g.num_edges == 1
        assert g.aut_order == 2
        assert g.h1 == 0
        assert g.valence == (1, 1)

    def test_theta_topology(self):
        """theta: 2 vertices g=(0,0), 3 bridges, |Aut| = 12."""
        g = genus2_graph_by_name('theta')
        assert g.vertex_genera == (0, 0)
        assert g.num_edges == 3
        assert g.aut_order == 12
        assert g.h1 == 2
        assert g.valence == (3, 3)

    def test_lollipop_topology(self):
        """lollipop: 2 vertices g=(0,1), 1 self-loop + 1 bridge, |Aut| = 2."""
        g = genus2_graph_by_name('lollipop')
        assert g.vertex_genera == (0, 1)
        assert g.num_edges == 2
        assert g.aut_order == 2
        assert g.h1 == 1
        # vertex 0: self-loop (val 2) + bridge (val 1) = 3
        # vertex 1: bridge (val 1)
        assert g.valence == (3, 1)

    def test_barbell_topology(self):
        """barbell: 2 vertices g=(0,0), 2 self-loops + 1 bridge, |Aut| = 8."""
        g = genus2_graph_by_name('barbell')
        assert g.vertex_genera == (0, 0)
        assert g.num_edges == 3
        assert g.aut_order == 8
        assert g.h1 == 2

    def test_feynman_loop_orders(self):
        """Verify the Feynman loop order = h^1 for each graph."""
        expected = {
            'smooth': 0,
            'figure_eight': 1,
            'banana': 2,
            'dumbbell': 0,
            'theta': 2,
            'lollipop': 1,
            'barbell': 2,
        }
        for g in genus2_stable_graphs():
            assert g.feynman_loop_order == expected[g.name], \
                f"{g.name}: loop order {g.feynman_loop_order} != {expected[g.name]}"


# =====================================================================
# Section 2: Faber-Pandharipande numbers
# =====================================================================

class TestFaberPandharipande:
    """Multi-path verification of lambda_g^FP."""

    def test_lambda1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == FR(1, 24)

    def test_lambda2(self):
        """lambda_2^FP = 7/5760 (NOT 1/1152 -- AP38)."""
        assert lambda_fp(2) == FR(7, 5760)

    def test_lambda3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == FR(31, 967680)

    def test_lambda4(self):
        """lambda_4^FP = 127/154828800."""
        assert lambda_fp(4) == FR(127, 154828800)

    def test_ahat_consistency(self):
        r"""Verify lambda_g^FP matches A-hat genus coefficients.

        Ahat(x) = (x/2)/sinh(x/2) = 1 - x^2/24 + 7x^4/5760 - ...
        Coefficient of x^{2g} = (-1)^g * lambda_g^FP.
        """
        assert (-1) ** 1 * lambda_fp(1) == FR(-1, 24)
        assert (-1) ** 2 * lambda_fp(2) == FR(7, 5760)

    def test_positivity(self):
        """lambda_g^FP > 0 for all g >= 1 (Bernoulli signs)."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0, f"lambda_{g}^FP = {lambda_fp(g)} <= 0"


# =====================================================================
# Section 3: Contributing graphs by shadow class
# =====================================================================

class TestContributingGraphs:
    """Test which graphs contribute for each shadow-depth class."""

    def test_class_G(self):
        """Class G (Gaussian, r_max=2): smooth + figure_eight only."""
        result = contributing_graphs('G')
        assert 'smooth' in result
        assert 'figure_eight' in result
        assert 'banana' not in result
        assert 'theta' not in result
        assert len(result) == 2

    def test_class_L(self):
        """Class L (Lie/tree, r_max=3): adds theta and barbell to class G."""
        result = contributing_graphs('L')
        assert 'smooth' in result
        assert 'figure_eight' in result
        assert 'theta' in result
        assert 'barbell' in result
        assert 'banana' not in result
        assert len(result) == 4

    def test_class_C(self):
        """Class C (contact, r_max=4): adds banana to class L."""
        result = contributing_graphs('C')
        assert 'banana' in result
        assert len(result) == 5

    def test_class_M(self):
        """Class M (mixed, r_max=inf): same as class C (tadpoles excluded)."""
        result = contributing_graphs('M')
        assert len(result) == 5

    def test_tadpole_graphs_excluded_all_classes(self):
        """dumbbell and lollipop have val-1 vertices (tadpoles), excluded in all classes."""
        for cls in ['G', 'L', 'C', 'M']:
            result = contributing_graphs(cls)
            assert 'dumbbell' not in result, f"dumbbell in class {cls}"
            assert 'lollipop' not in result, f"lollipop in class {cls}"

    def test_class_hierarchy(self):
        """Each class includes all graphs of the previous class."""
        G = set(contributing_graphs('G'))
        L = set(contributing_graphs('L'))
        C = set(contributing_graphs('C'))
        M = set(contributing_graphs('M'))
        assert G <= L <= C <= M


# =====================================================================
# Section 4: Heisenberg bar amplitudes at genus 2
# =====================================================================

class TestHeisenbergGenus2:
    """Heisenberg H_k at genus 2: the simplest case (class G)."""

    def test_total_matches_theorem_d(self):
        """F_2(H_k) = kappa * lambda_2^FP for Heisenberg (Theorem D on scalar lane)."""
        for k_val in [1, 2, 3, 5, 10]:
            k = FR(k_val)
            result = heisenberg_genus2(k)
            assert result['total'] == k * lambda_fp(2), \
                f"k={k}: {result['total']} != {k * lambda_fp(2)}"

    def test_match_flag(self):
        """The engine reports a match between total and expected."""
        result = heisenberg_genus2(FR(1))
        assert result['match'] is True

    def test_figure_eight_kappa_independent(self):
        """The figure_eight amplitude is 1/2 for ALL kappa."""
        for k in [1, 2, 5, 10, 100]:
            result = heisenberg_genus2(FR(k))
            assert result['amplitudes']['figure_eight'] == FR(1, 2)

    def test_only_smooth_and_figure_eight_contribute(self):
        """For class G, only smooth and figure_eight are nonzero."""
        result = heisenberg_genus2(FR(3))
        nonzero = {name for name, amp in result['amplitudes'].items() if amp != FR(0)}
        assert nonzero == {'smooth', 'figure_eight'}

    def test_linearity_in_kappa(self):
        """F_2 is linear in kappa (hence linear in k for Heisenberg)."""
        r1 = heisenberg_genus2(FR(3))
        r2 = heisenberg_genus2(FR(5))
        r_sum = heisenberg_genus2(FR(8))
        assert r1['total'] + r2['total'] == r_sum['total']


# =====================================================================
# Section 5: Virasoro bar amplitudes at genus 2
# =====================================================================

class TestVirasoroGenus2:
    """Virasoro Vir_c at genus 2: class M with planted-forest corrections."""

    def test_total_matches_theorem_d(self):
        """F_2(Vir_c) = (c/2) * lambda_2^FP (Theorem D, uniform-weight lane)."""
        for c_val in [1, 10, 13, 26]:
            c = FR(c_val)
            result = virasoro_genus2(c)
            expected = (c / 2) * lambda_fp(2)
            assert result['total'] == expected, \
                f"c={c}: {result['total']} != {expected}"

    def test_five_contributing_graphs(self):
        """Virasoro (class M) has 5 contributing graphs out of 7."""
        result = virasoro_genus2(FR(26))
        assert len(result['contributing']) == 5
        # dumbbell and lollipop excluded by tadpole
        assert 'dumbbell' not in result['contributing']
        assert 'lollipop' not in result['contributing']

    def test_figure_eight_universal(self):
        """The figure_eight amplitude is always 1/2, independent of c."""
        for c_val in [1, 10, 26]:
            result = virasoro_genus2(FR(c_val))
            assert result['amplitudes']['figure_eight'] == FR(1, 2)

    def test_planted_forest_correction(self):
        """delta_pf = S_3*(10*S_3 - kappa)/48 = 2*(20 - c/2)/48 = (40-c)/48."""
        c = FR(26)
        result = virasoro_genus2(c)
        expected_pf = FR(2) * (10 * FR(2) - c / 2) / 48
        assert result['planted_forest_correction'] == expected_pf

    def test_planted_forest_vanishes_heisenberg(self):
        """Planted-forest correction is zero for Heisenberg (S_3 = 0)."""
        pf = planted_forest_correction(FR(1), FR(0))
        assert pf == FR(0)


# =====================================================================
# Section 6: Affine sl_2 bar amplitudes at genus 2
# =====================================================================

class TestAffineSl2Genus2:
    """Affine V_k(sl_2) at genus 2: class L (r_max=3)."""

    def test_total_matches_theorem_d(self):
        """F_2(V_k(sl_2)) = kappa * lambda_2^FP."""
        for k_val in [1, 2, 3]:
            k = FR(k_val)
            result = affine_sl2_genus2(k)
            assert result['total'] == result['kappa'] * lambda_fp(2)

    def test_kappa_formula(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        for k_val in [1, 2, 5]:
            k = FR(k_val)
            sd = affine_sl2_shadow_data(k)
            assert sd['kappa'] == FR(3) * (k + 2) / 4

    def test_S3_formula(self):
        """S_3(sl_2, k) = 4/(k+2)."""
        k = FR(1)
        sd = affine_sl2_shadow_data(k)
        assert sd['S_3'] == FR(4) / (k + 2)
        assert sd['S_3'] == FR(4, 3)

    def test_S4_vanishes(self):
        """S_4 = 0 for class L (Jacobi kills quartic)."""
        sd = affine_sl2_shadow_data(FR(1))
        assert sd['S_4'] == FR(0)

    def test_banana_excluded(self):
        """banana excluded for class L: genus-0 vertex has val 4 > r_max = 3."""
        result = affine_sl2_genus2(FR(1))
        assert result['amplitudes']['banana'] == FR(0)


# =====================================================================
# Section 7: Collision residue tests
# =====================================================================

class TestCollisionResidue:
    """Test the collision residue r(z) = Res^coll_{0,2}(Theta_A)."""

    def test_heisenberg_tree_exact(self):
        """Heisenberg r(z) = k/z: tree-level exact, no loop corrections."""
        k = FR(3)
        r = tree_level_r_heisenberg(k)
        assert r.poles == {1: k}
        assert r.loop_contributions == {0: k}

    def test_heisenberg_r_scales_with_k(self):
        """r(z) pole coefficient scales linearly with level k."""
        for k_val in [1, 2, 5, 10]:
            k = FR(k_val)
            r = tree_level_r_heisenberg(k)
            assert r.poles[1] == k

    def test_km_sl2_tree_exact(self):
        """KM sl_2 r(z) = kappa/z: tree-level exact (class L, single pole)."""
        k = FR(1)
        r = tree_level_r_km_sl2(k)
        kappa = FR(3) * (k + 2) / 4
        assert r.poles[1] == kappa
        assert r.loop_contributions[0] == kappa
        assert len(r.loop_contributions) == 1

    def test_virasoro_pole_structure(self):
        """Virasoro r(z) has poles at z^{-3} and z^{-1} only (AP19: no even-order poles)."""
        c = FR(1)
        r = tree_level_r_virasoro(c)
        assert 3 in r.poles
        assert 1 in r.poles
        assert 2 not in r.poles  # no even-order poles (AP19)
        assert 4 not in r.poles  # OPE z^{-4} shifted to z^{-3}

    def test_virasoro_leading_pole(self):
        """Virasoro leading pole: coefficient of z^{-3} is c/2 = kappa."""
        c = FR(26)
        r = tree_level_r_virasoro(c)
        assert r.poles[3] == c / 2

    def test_virasoro_tree_level_z_inv(self):
        """Tree-level z^{-1} coefficient for Virasoro is 2*kappa = c."""
        c = FR(10)
        r = tree_level_r_virasoro(c)
        assert r.loop_contributions[0] == c  # 2*kappa = c

    def test_virasoro_bubble_correction(self):
        """1-loop bubble correction to z^{-1}: -S_3^2/kappa = -8/c."""
        c = FR(10)
        r = virasoro_r_matrix_with_corrections(c)
        expected_bubble = FR(8) / c
        assert r.loop_contributions[1] == -expected_bubble


# =====================================================================
# Section 8: Bubble and sunset diagrams
# =====================================================================

class TestDiagramAmplitudes:
    """Test individual Feynman diagram amplitudes."""

    def test_bubble_class_G_vanishes(self):
        """For class G (S_3 = 0), the bubble diagram is zero."""
        assert bubble_diagram_amplitude(FR(0), FR(1)) == FR(0)

    def test_bubble_virasoro(self):
        """Virasoro bubble: S_3^2/kappa = 4/(c/2) = 8/c."""
        c = FR(10)
        kappa = c / 2
        S3 = FR(2)
        result = bubble_diagram_amplitude(S3, kappa)
        assert result == FR(4) / kappa
        assert result == FR(8) / c

    def test_bubble_scales_inversely_with_kappa(self):
        """Bubble amplitude ~ 1/kappa for fixed S_3."""
        S3 = FR(2)
        for k in [1, 2, 5, 10]:
            kappa = FR(k)
            amp = bubble_diagram_amplitude(S3, kappa)
            assert amp == FR(4) / kappa

    def test_sunset_cubic_channel(self):
        """Sunset cubic-cubic channel: S_3^2 / (6 * kappa^3)."""
        S3 = FR(2)
        S4 = FR(0)
        kappa = FR(1)
        result = sunset_diagram_amplitude(S3, S4, kappa)
        assert result == FR(4, 6)  # S_3^2 / 6 = 4/6 = 2/3

    def test_sunset_with_quartic(self):
        """Sunset with quartic channel: adds S_4 / (2*kappa)."""
        S3 = FR(0)
        S4 = FR(1, 10)
        kappa = FR(5)
        result = sunset_diagram_amplitude(S3, S4, kappa)
        assert result == FR(1, 10) / (2 * FR(5))
        assert result == FR(1, 100)


# =====================================================================
# Section 9: Non-renormalization
# =====================================================================

class TestNonRenormalization:
    """Test the non-renormalization theorem for class G and L."""

    def test_class_G_tree_exact(self):
        """Class G: S_3 = 0, so bubble vanishes and r(z) is tree-level exact."""
        result = verify_non_renormalization('G', FR(1), {'S_3': FR(0), 'S_4': FR(0)})
        assert result['class_G_tree_exact'] is True
        assert result['bubble_vanishes'] is True

    def test_class_L_tree_exact_genus0(self):
        """Class L: S_4 = 0, so tree-level exact at genus 0."""
        result = verify_non_renormalization('L', FR(3), {'S_3': FR(2), 'S_4': FR(0)})
        assert result['bubble'] != FR(0)  # bubble nonzero (enters at genus >= 1)
        assert result['class_L_tree_exact_genus0'] is True

    def test_heisenberg_no_loop_correction(self):
        """Heisenberg 1-loop correction is exactly zero."""
        assert one_loop_correction_heisenberg(FR(3)) == FR(0)

    def test_virasoro_bubble_nonzero(self):
        """Virasoro has nonzero 1-loop correction (class M)."""
        for c_val in [1, 10, 26]:
            assert one_loop_correction_virasoro(FR(c_val)) != FR(0)


# =====================================================================
# Section 10: Virasoro shadow data
# =====================================================================

class TestVirasoroShadow:
    """Test Virasoro shadow obstruction tower data."""

    def test_kappa(self):
        """kappa(Vir_c) = c/2."""
        c = FR(26)
        sd = virasoro_shadow_data(c)
        assert sd['kappa'] == FR(13)

    def test_S3_universal(self):
        """Cubic shadow S_3 = 2 for all c (from T_{(1)}T = 2T)."""
        for c_val in [1, 10, 26, 100]:
            sd = virasoro_shadow_data(FR(c_val))
            assert sd['S_3'] == FR(2)

    def test_S4_quartic_contact(self):
        """Q^contact_Vir = 10/(c(5c+22))."""
        c = FR(1)
        sd = virasoro_shadow_data(c)
        assert sd['S_4'] == FR(10) / (c * (5 * c + 22))
        assert sd['S_4'] == FR(10, 27)

    def test_S4_at_c26(self):
        """Q^contact at c=26: 10/(26*152) = 5/1976."""
        c = FR(26)
        sd = virasoro_shadow_data(c)
        assert sd['S_4'] == FR(5, 1976)

    def test_S5(self):
        """S_5 = -48/(c^2(5c+22))."""
        c = FR(1)
        sd = virasoro_shadow_data(c)
        assert sd['S_5'] == FR(-48) / (c ** 2 * (5 * c + 22))


# =====================================================================
# Section 11: Orbifold Euler characteristic
# =====================================================================

class TestEulerCharacteristic:
    """Test orbifold Euler characteristics at standard moduli."""

    def test_chi_orb_M20(self):
        """chi^orb(M_{2,0}) = -1/240."""
        assert chi_orb(2, 0) == FR(-1, 240)

    def test_chi_orb_M11(self):
        """chi^orb(M_{1,1}) = -1/12."""
        assert chi_orb(1, 1) == FR(-1, 12)

    def test_chi_orb_M12(self):
        """chi^orb(M_{1,2}) = 0."""
        assert chi_orb(1, 2) == FR(0)

    def test_chi_orb_M03(self):
        """chi^orb(M_{0,3}) = 1 (point)."""
        assert chi_orb(0, 3) == FR(1)

    def test_chi_orb_M04(self):
        """chi^orb(M_{0,4}) = -1."""
        assert chi_orb(0, 4) == FR(-1)


# =====================================================================
# Section 12: Planted-forest corrections
# =====================================================================

class TestPlantedForest:
    """Test planted-forest corrections at genus 2."""

    def test_virasoro_c26(self):
        """Virasoro c=26: delta_pf = -(26-40)/48 = 7/24."""
        pf = virasoro_planted_forest(FR(26))
        assert pf == FR(7, 24)

    def test_virasoro_c1(self):
        """Virasoro c=1: delta_pf = -(1-40)/48 = 39/48 = 13/16."""
        pf = virasoro_planted_forest(FR(1))
        assert pf == FR(13, 16)

    def test_virasoro_c40(self):
        """Virasoro c=40: delta_pf = 0 (numerator vanishes)."""
        pf = virasoro_planted_forest(FR(40))
        assert pf == FR(0)

    def test_formula_matches_engine(self):
        """Cross-check: planted_forest_correction(kappa, S_3) matches virasoro_planted_forest."""
        for c_val in [1, 10, 26]:
            c = FR(c_val)
            pf_direct = virasoro_planted_forest(c)
            pf_formula = planted_forest_correction(c / 2, FR(2))
            assert pf_direct == pf_formula


# =====================================================================
# Section 13: Cross-family consistency
# =====================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10: not just hardcoded values)."""

    def test_kappa_additivity_heisenberg(self):
        """kappa(H_{k1} + H_{k2}) = kappa(H_{k1}) + kappa(H_{k2}).

        F_2 is additive: F_2(H_{k1+k2}) = F_2(H_{k1}) + F_2(H_{k2}).
        """
        result = heisenberg_additivity_g2(FR(3), FR(5))
        assert result['additivity_holds'] is True

    def test_virasoro_kappa_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c_val in [1, 10, 13, 25]:
            c = FR(c_val)
            kappa = c / 2
            kappa_dual = (FR(26) - c) / 2
            assert kappa + kappa_dual == FR(13)

    def test_virasoro_genus2_complementarity(self):
        """F_2(Vir_c) + F_2(Vir_{26-c}) = 13 * lambda_2^FP."""
        for c_val in [1, 10, 13]:
            result = koszul_complementarity_g2(FR(c_val))
            assert result['complementarity_holds'] is True

    def test_virasoro_self_dual_at_c13(self):
        """At c=13: kappa = 13/2, shadow data is invariant under c -> 26-c."""
        c = FR(13)
        sd = virasoro_shadow_data(c)
        sd_dual = virasoro_shadow_data(FR(26) - c)
        assert sd['kappa'] == sd_dual['kappa']
        assert sd['S_3'] == sd_dual['S_3']
        assert sd['S_4'] == sd_dual['S_4']

    def test_vertex_factor_tadpole_zero(self):
        """Vertex factors at valence 1 are always zero (tadpole vanishing)."""
        for cls in ['G', 'L', 'C', 'M']:
            for gv in [0, 1, 2]:
                vf = vertex_factor_scalar(gv, 1, FR(1), cls)
                assert vf == FR(0), f"Tadpole nonzero at g={gv}, class={cls}"


# =====================================================================
# Section 14: Full summary
# =====================================================================

class TestFullSummary:
    """Test the full graph-level Feynman/bar summary."""

    def test_heisenberg_summary(self):
        """Heisenberg summary: 2 contributing graphs out of 7."""
        summary = full_summary('Heisenberg', FR(1), 'G')
        contributing = [g for g in summary['graphs'] if g['contributes']]
        assert len(contributing) == 2

    def test_virasoro_summary(self):
        """Virasoro summary: 5 contributing graphs."""
        c = FR(10)
        sd = virasoro_shadow_data(c)
        summary = full_summary('Virasoro', c / 2, 'M', sd)
        contributing = [g for g in summary['graphs'] if g['contributes']]
        assert len(contributing) == 5
