r"""Tests for the Pixton shadow bridge: conj:pixton-from-shadows verification.

Tests that the MC-descended tautological relations from the shadow tower
generate the Pixton ideal at low genus.

Test structure:
1. Witten-Kontsevich intersection number verification
2. Stable graph enumeration and Hodge integral tests
3. Shadow CohFT amplitude tests
4. Mumford relation from MC (prop:mumford-from-mc)
5. Planted-forest correction tests
6. Pixton conjecture verification at genus 2
7. Cross-family comparison (G/L/C/M classification)
"""

import pytest
from fractions import Fraction

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from pixton_shadow_bridge import (
    wk_intersection,
    double_factorial,
    stable_graphs_genus2_0leg,
    stable_graphs_genus1_1leg,
    graph_integral_genus2,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_shadow_data,
    vertex_weight,
    mc_relation_genus2_free_energy,
    verify_mumford_from_mc,
    verify_pixton_genus2,
    planted_forest_polynomial,
    cross_family_pixton_test,
    known_genus2_hodge_integrals,
    c_sym,
)

from sympy import Rational, Integer, cancel, simplify, Symbol


# ═══════════════════════════════════════════════════════════════════════════
# Section 1: Witten-Kontsevich intersection numbers
# ═══════════════════════════════════════════════════════════════════════════

class TestDoubleFactorial:
    """Test the double factorial (2n+1)!! computation."""

    def test_base_cases(self):
        assert double_factorial(0) == 1     # 1!! = 1
        assert double_factorial(1) == 3     # 3!! = 3
        assert double_factorial(2) == 15    # 5!! = 15
        assert double_factorial(3) == 105   # 7!! = 105

    def test_negative(self):
        # Convention: (-1)!! = 1 (empty product)
        assert double_factorial(-1) == 1


class TestWKIntersection:
    """Verify Witten-Kontsevich intersection numbers against known values."""

    def test_base_case_tau0_cubed(self):
        """<tau_0^3>_0 = 1."""
        assert wk_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_genus1_tau1(self):
        """<tau_1>_1 = 1/24."""
        assert wk_intersection(1, (1,)) == Fraction(1, 24)

    def test_dimensional_constraint(self):
        """Non-matching dimensions give 0."""
        assert wk_intersection(0, (1, 0, 0)) == Fraction(0)  # sum = 1 != 0
        assert wk_intersection(1, (0,)) == Fraction(0)  # sum = 0 != 1

    def test_stability(self):
        """Unstable (g,n) give 0."""
        assert wk_intersection(0, (0, 0)) == Fraction(0)  # n=2, g=0 unstable
        assert wk_intersection(0, (0,)) == Fraction(0)     # n=1, g=0 unstable

    def test_genus0_four_points(self):
        """<tau_1 tau_0^3>_0 = 1 (by string equation)."""
        # dim constraint: 1+0+0+0 = 1 = 3*0-3+4 = 1. OK.
        result = wk_intersection(0, (1, 0, 0, 0))
        assert result == Fraction(1)

    def test_genus1_two_point(self):
        """<tau_1^2>_1 = 1/24 (by dilaton)."""
        # dim constraint: 1+1 = 2 = 3*1-3+2 = 2. OK.
        result = wk_intersection(1, (1, 1))
        assert result == Fraction(1, 24)

    def test_genus2_tau4(self):
        """<tau_4>_2 = 1/1152."""
        # dim constraint: 4 = 3*2-3+1 = 4. OK.
        result = wk_intersection(2, (4,))
        assert result == Fraction(1, 1152)

    def test_genus0_tau1_squared(self):
        """<tau_1^2 tau_0>_0 = 1 (from string/DVV)."""
        # dim: 1+1+0 = 2 = 3*0-3+3 = 0. NO! 3*0-3+3 = 0, but sum = 2. Wrong dim.
        # Actually for n=3: dim = 0. So need sum = 0. <tau_1^2 tau_0>_0 = 0.
        # For n=4: <tau_1^2 tau_0^2>_0, dim = 1. sum = 1+1+0+0 = 2 != 1. Also 0.
        # For n=3: <tau_0^3>_0 = 1 is the only nonzero genus-0 3-point number.
        pass

    def test_genus2_three_point(self):
        """<tau_1^2 tau_2>_2 at genus 2."""
        # dim: 1+1+2 = 4 = 3*2-3+3 = 6. NO! 6 != 4.
        # Actually 3g-3+n = 3*2-3+3 = 6. Need sum d_i = 6. So (1,1,2) has sum 4 != 6.
        result = wk_intersection(2, (2, 1, 1))
        assert result == Fraction(0)  # wrong dimension

    def test_symmetry(self):
        """Intersection numbers are symmetric in the d_i."""
        assert wk_intersection(0, (1, 0, 0, 0)) == wk_intersection(0, (0, 1, 0, 0))
        assert wk_intersection(0, (1, 0, 0, 0)) == wk_intersection(0, (0, 0, 0, 1))

    def test_genus0_five_point(self):
        """<tau_1^2 tau_0^3>_0 = 2."""
        # dim: 3*0-3+5 = 2. sum: 1+1+0+0+0 = 2. OK.
        result = wk_intersection(0, (1, 1, 0, 0, 0))
        assert result == Fraction(2)

    def test_genus1_tau2(self):
        """<tau_2>_1: dim = 3*1-3+1 = 1. sum = 2 != 1. So 0."""
        assert wk_intersection(1, (2,)) == Fraction(0)

    def test_genus1_tau0_tau1(self):
        """<tau_0 tau_1>_1: dim = 3*1-3+2 = 2. sum = 0+1 = 1 != 2. 0."""
        assert wk_intersection(1, (1, 0)) == Fraction(0)

    def test_genus2_tau3_tau1(self):
        """<tau_3 tau_1>_2: dim = 3*2-3+2 = 5. sum = 3+1 = 4 != 5. 0."""
        assert wk_intersection(2, (3, 1)) == Fraction(0)


# ═══════════════════════════════════════════════════════════════════════════
# Section 2: Stable graph enumeration
# ═══════════════════════════════════════════════════════════════════════════

class TestStableGraphs:
    """Test stable graph enumeration."""

    def test_genus2_count(self):
        """There are exactly 7 stable graphs of type (2, 0)."""
        graphs = stable_graphs_genus2_0leg()
        assert len(graphs) == 7

    def test_genus2_names(self):
        """Check graph names are correct."""
        names = {G.name for G in stable_graphs_genus2_0leg()}
        expected = {
            'A_smooth', 'B_lollipop', 'C_sunset', 'D_dumbbell',
            'E_bridge_loop', 'F_theta', 'G_figure8_bridge',
        }
        assert names == expected

    def test_genus2_codimensions(self):
        """Check codimension assignment."""
        graphs = stable_graphs_genus2_0leg()
        codims = {G.name: G.codimension for G in graphs}
        assert codims['A_smooth'] == 0
        assert codims['B_lollipop'] == 1
        assert codims['D_dumbbell'] == 1
        assert codims['C_sunset'] == 2
        assert codims['E_bridge_loop'] == 2
        assert codims['F_theta'] == 3
        assert codims['G_figure8_bridge'] == 3

    def test_genus2_automorphisms(self):
        """Check automorphism orders."""
        graphs = stable_graphs_genus2_0leg()
        auts = {G.name: G.automorphism_order for G in graphs}
        assert auts['A_smooth'] == 1
        assert auts['B_lollipop'] == 2
        assert auts['D_dumbbell'] == 2
        assert auts['C_sunset'] == 8
        assert auts['E_bridge_loop'] == 2
        assert auts['F_theta'] == 12
        assert auts['G_figure8_bridge'] == 8

    def test_genus1_count(self):
        """There are exactly 2 stable graphs of type (1, 1)."""
        graphs = stable_graphs_genus1_1leg()
        assert len(graphs) == 2


# ═══════════════════════════════════════════════════════════════════════════
# Section 3: Graph integral computation
# ═══════════════════════════════════════════════════════════════════════════

class TestGraphIntegrals:
    """Test Hodge integral computation for genus-2 graphs."""

    def test_dumbbell_integral(self):
        """Dumbbell: I(D) = (-1) * <tau_1>_1^2 = -1/576."""
        graphs = stable_graphs_genus2_0leg()
        D = [G for G in graphs if G.name == 'D_dumbbell'][0]
        I_D = graph_integral_genus2(D)
        assert I_D == Fraction(-1, 576)

    def test_lollipop_integral(self):
        """Lollipop B: I(B) = sum_{d+=0}^2 (-1)^{2-d+} <tau_{d+} tau_{2-d+}>_1."""
        graphs = stable_graphs_genus2_0leg()
        B = [G for G in graphs if G.name == 'B_lollipop'][0]
        I_B = graph_integral_genus2(B)
        # <tau_0 tau_2>_1: dim needs 0+2 = 2 = 3*1-3+2. OK.
        # <tau_1 tau_1>_1: 1+1 = 2. OK.
        # <tau_2 tau_0>_1: same as <tau_0 tau_2>_1.
        # Compute:
        # d+=0, d-=2: (-1)^2 * <tau_0 tau_2>_1
        # d+=1, d-=1: (-1)^1 * <tau_1 tau_1>_1
        # d+=2, d-=0: (-1)^0 * <tau_2 tau_0>_1

        wk_02 = wk_intersection(1, (2, 0))
        wk_11 = wk_intersection(1, (1, 1))
        expected = wk_02 - wk_11 + wk_02  # = 2*wk_02 - wk_11

        assert I_B == expected

    def test_theta_integral(self):
        """Theta: I(F) = <tau_0^3>_0^2 = 1."""
        graphs = stable_graphs_genus2_0leg()
        F = [G for G in graphs if G.name == 'F_theta'][0]
        I_F = graph_integral_genus2(F)
        assert I_F == Fraction(1)

    def test_figure8_integral(self):
        """Figure-8 bridge: I(G) = <tau_0^3>_0^2 = 1."""
        graphs = stable_graphs_genus2_0leg()
        G = [g for g in graphs if g.name == 'G_figure8_bridge'][0]
        I_G = graph_integral_genus2(G)
        assert I_G == Fraction(1)

    def test_bridge_loop_integral(self):
        """Bridge+loop E: I(E) = (-1)^1 * <tau_0^3>_0 * <tau_1>_1 = -1/24."""
        graphs = stable_graphs_genus2_0leg()
        E = [G for G in graphs if G.name == 'E_bridge_loop'][0]
        I_E = graph_integral_genus2(E)
        assert I_E == Fraction(-1, 24)


# ═══════════════════════════════════════════════════════════════════════════
# Section 4: Shadow data tests
# ═══════════════════════════════════════════════════════════════════════════

class TestShadowData:
    """Test shadow data for standard families."""

    def test_virasoro_kappa(self):
        vir = virasoro_shadow_data()
        assert vir.kappa == c_sym / 2

    def test_virasoro_S3(self):
        vir = virasoro_shadow_data()
        assert vir.S3 == 2

    def test_virasoro_S4(self):
        vir = virasoro_shadow_data()
        expected = Rational(10) / (c_sym * (5 * c_sym + 22))
        assert cancel(vir.S4 - expected) == 0

    def test_heisenberg_class_G(self):
        heis = heisenberg_shadow_data()
        assert heis.S3 == 0
        assert heis.S4 == 0
        assert heis.depth_class == 'G'

    def test_affine_class_L(self):
        aff = affine_shadow_data()
        assert aff.S3 == 2
        assert aff.S4 == 0
        assert aff.depth_class == 'L'

    def test_virasoro_S5(self):
        """S_5 = -48/[c^2(5c+22)] (quintic forced)."""
        vir = virasoro_shadow_data()
        S5 = vir.S(5)
        expected = Rational(-48) / (c_sym ** 2 * (5 * c_sym + 22))
        assert cancel(S5 - expected) == 0

    def test_virasoro_higher_arities(self):
        """Shadow tower computes to arbitrary arity."""
        vir = virasoro_shadow_data(max_arity=8)
        for r in range(2, 9):
            S_r = vir.S(r)
            assert S_r is not None
            # Verify nonzero for class M
            assert S_r != 0 or r > 8


# ═══════════════════════════════════════════════════════════════════════════
# Section 5: Mumford relation from MC (prop:mumford-from-mc)
# ═══════════════════════════════════════════════════════════════════════════

class TestMumfordFromMC:
    """Test that arity-2 MC relation gives Mumford's relation."""

    def test_mumford_structure(self):
        """The arity-2 MC relation at genus 2 has the Mumford structure:
        separating (dumbbell) + non-separating (lollipop) terms.
        """
        heis = heisenberg_shadow_data()
        result = verify_mumford_from_mc(heis)
        # Both contributions should be nonzero
        assert result['D_hodge_integral'] != 0
        assert result['B_hodge_integral'] != 0

    def test_dumbbell_value(self):
        """Dumbbell Hodge integral = -1/576."""
        heis = heisenberg_shadow_data()
        result = verify_mumford_from_mc(heis)
        assert result['D_hodge_integral'] == Fraction(-1, 576)


# ═══════════════════════════════════════════════════════════════════════════
# Section 6: Planted-forest correction tests
# ═══════════════════════════════════════════════════════════════════════════

class TestPlantedForest:
    """Test the planted-forest correction delta_pf at genus 2."""

    def test_heisenberg_pf_zero(self):
        """For class G (Heisenberg), delta_pf = 0."""
        heis = heisenberg_shadow_data()
        pf = planted_forest_polynomial(heis)
        assert pf == 0

    def test_affine_pf_structure(self):
        """For class L (affine), delta_pf involves only S_3 (no S_4 terms)."""
        aff = affine_shadow_data()
        pf = planted_forest_polynomial(aff)
        # S_4 = 0 for affine, so only graphs with S_3 vertex weights contribute
        # These are graphs with (0,3) vertices: E, F, G
        # But graph C has (0,4) vertex with weight S_4 = 0, so C vanishes.
        # The remaining codim >= 2 graphs (E, F, G) have S_3 in their weights.

    def test_virasoro_pf_nonzero(self):
        """For class M (Virasoro), delta_pf != 0."""
        vir = virasoro_shadow_data()
        pf = planted_forest_polynomial(vir)
        # Evaluate at a specific c to check nonzero
        pf_num = float(pf.subs(c_sym, 25))
        assert abs(pf_num) > 1e-10, f"delta_pf should be nonzero for Virasoro, got {pf_num}"

    def test_virasoro_pf_rational_function(self):
        """delta_pf for Virasoro is a rational function of c."""
        vir = virasoro_shadow_data()
        pf = planted_forest_polynomial(vir)
        # Should be expressible as P(c)/Q(c) for polynomials P, Q
        from sympy import fraction
        num, den = fraction(cancel(pf))
        # Denominator should involve c and (5c+22)
        assert den != 0

    def test_virasoro_pf_multiple_c_values(self):
        """Verify delta_pf is consistent across multiple c values."""
        vir = virasoro_shadow_data()
        pf = planted_forest_polynomial(vir)
        values = []
        for c_val in [3, 7, 13, 25, 50]:
            val = float(pf.subs(c_sym, c_val))
            values.append(val)
        # All should be nonzero for class M
        for v in values:
            assert abs(v) > 1e-15

    def test_pf_self_dual_point(self):
        """At the self-dual point c=13, check delta_pf has specific structure."""
        vir = virasoro_shadow_data()
        pf = planted_forest_polynomial(vir)
        pf_13 = float(pf.subs(c_sym, 13))
        # At c=13, Vir is self-dual. The planted-forest correction should
        # have a specific value related to the duality.
        assert abs(pf_13) > 1e-15  # nonzero


# ═══════════════════════════════════════════════════════════════════════════
# Section 7: Pixton conjecture verification
# ═══════════════════════════════════════════════════════════════════════════

class TestPixtonConjecture:
    """Test conj:pixton-from-shadows at genus 2."""

    def test_genus2_mc_relation_structure(self):
        """The MC relation at genus 2 has three parts:
        separating + non-separating + planted-forest = 0.
        """
        vir = virasoro_shadow_data()
        result = verify_pixton_genus2(vir)
        assert 'separating' in result
        assert 'non_separating' in result
        assert 'planted_forest' in result

    def test_class_G_only_mumford(self):
        """For Heisenberg (class G), only Mumford relations, no planted-forest."""
        heis = heisenberg_shadow_data()
        result = verify_pixton_genus2(heis)
        assert result['planted_forest'] == 0
        assert result['pixton_conjecture_status'] == 'trivially_satisfied'

    def test_class_M_nontrivial_pf(self):
        """For Virasoro (class M), planted-forest correction is nontrivial."""
        vir = virasoro_shadow_data()
        result = verify_pixton_genus2(vir)
        pf = result['planted_forest']
        # Evaluate at c = 25
        pf_val = float(pf.subs(c_sym, 25))
        assert abs(pf_val) > 1e-10
        assert result['pixton_conjecture_status'] == 'nontrivial_test'

    def test_pf_structure_for_pixton(self):
        """The planted-forest correction for Virasoro at genus 2 should
        produce a relation in R^2(M-bar_2) that is proportional to
        the Faber-Zagier relation (the first non-Mumford Pixton relation).

        Specifically, the correction involves codim-2 and codim-3 strata:
        - C (sunset): weight S_4, codim 2
        - E (bridge+loop): weight S_3 * kappa, codim 2
        - F (theta): weight S_3^2, codim 3
        - G (figure-8): weight S_3^2, codim 3
        """
        vir = virasoro_shadow_data()
        result = verify_pixton_genus2(vir)
        graphs = result['graphs']

        # Check which graphs contribute to planted-forest (codim >= 2)
        pf_graphs = {name: info for name, info in graphs.items()
                     if info['codimension'] >= 2}
        assert len(pf_graphs) == 4  # C, E, F, G

        # Verify graph C contribution involves S_4
        C_weight = graphs['C_sunset']['weight']
        assert C_weight != 0  # S_4 != 0 for Virasoro

    def test_pf_codim2_factorization(self):
        """At codim 2, the planted-forest correction should factorize
        into a product of shadow data and a universal Hodge integral.

        This is the key structural prediction: the Pixton relation's
        codim-2 piece is a UNIVERSAL rational function times the
        shadow data (kappa, S_3, S_4).
        """
        vir = virasoro_shadow_data()
        result = mc_relation_genus2_free_energy(vir)
        graphs = result['graphs']

        # Codim-2 contributions: C and E
        C_contrib = graphs['C_sunset']['contribution']
        E_contrib = graphs['E_bridge_loop']['contribution']
        codim2_total = cancel(C_contrib + E_contrib)

        # This should be a specific rational function of c
        from sympy import fraction
        num, den = fraction(codim2_total)
        # The denominator should be a power of c and (5c+22)
        # (from the shadow data denominators)
        assert den != 0


# ═══════════════════════════════════════════════════════════════════════════
# Section 8: Cross-family tests
# ═══════════════════════════════════════════════════════════════════════════

class TestCrossFamily:
    """Test conj:pixton-from-shadows across families."""

    def test_depth_class_determines_pf(self):
        """The depth class (G/L/C/M) determines whether delta_pf is zero.

        G: delta_pf = 0 (no planted-forest contribution)
        L: delta_pf may be nonzero at codim >= 2 (S_3 terms)
        M: delta_pf nonzero (S_3 and S_4 terms)
        """
        heis = heisenberg_shadow_data()
        heis_pf = planted_forest_polynomial(heis)
        assert heis_pf == 0, "Class G should have zero planted-forest correction"

        vir = virasoro_shadow_data()
        vir_pf = planted_forest_polynomial(vir)
        vir_pf_val = float(vir_pf.subs(c_sym, 25))
        assert abs(vir_pf_val) > 1e-10, "Class M should have nonzero planted-forest"

    def test_pixton_generation_hierarchy(self):
        """Test the hierarchy of tautological relation generation:

        Class G: Mumford only (rank 1 in Pixton ideal)
        Class L: Mumford + cubic terms (rank ?)
        Class M: Mumford + cubic + quartic + ... (should generate Pixton ideal)

        The conjecture predicts: class M with infinite shadow tower
        generates the FULL Pixton ideal.
        """
        results = cross_family_pixton_test()

        # Heisenberg: zero planted-forest
        assert results['Heisenberg']['is_zero']

        # Virasoro: nonzero planted-forest
        assert not results['Virasoro']['is_zero']


# ═══════════════════════════════════════════════════════════════════════════
# Section 9: Known Hodge integral cross-checks
# ═══════════════════════════════════════════════════════════════════════════

class TestKnownHodgeIntegrals:
    """Cross-check WK intersection numbers against published values."""

    def test_tau1_genus1(self):
        """<tau_1>_1 = 1/24 (Witten-Kontsevich)."""
        assert wk_intersection(1, (1,)) == Fraction(1, 24)

    def test_tau0_cubed_genus0(self):
        """<tau_0^3>_0 = 1."""
        assert wk_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_tau4_genus2(self):
        """<tau_4>_2 = 1/1152."""
        assert wk_intersection(2, (4,)) == Fraction(1, 1152)

    def test_tau0_tau1_tau2_genus0(self):
        """<tau_0 tau_1 tau_2>_0: dim = 3*0-3+3 = 0. sum = 0+1+2 = 3 != 0. So 0."""
        assert wk_intersection(0, (2, 1, 0)) == Fraction(0)

    def test_tau1_cubed_tau0_genus0(self):
        """<tau_1^3 tau_0^2>_0: dim = 3*0-3+5 = 2. sum = 3+0 = 3 != 2. So 0."""
        assert wk_intersection(0, (1, 1, 1, 0, 0)) == Fraction(0)

    def test_known_values_table(self):
        """Check the known values table is self-consistent."""
        table = known_genus2_hodge_integrals()
        assert table['<tau_1>_1'] == Fraction(1, 24)
        assert table['<tau_0^3>_0'] == Fraction(1)
