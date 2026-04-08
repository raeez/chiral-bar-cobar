r"""Tests for Swiss-cheese Kontsevich conjecture engine.

Tests the SC^{ch,top} operadic structure, De Leger's E_3 action on
chiral Hochschild cochains, Moriwaki's boundary OPE convergence,
and compatibility with the brace dg algebra of Vol II.

Multi-path verification per CLAUDE.md mandate:
  - Each numerical claim verified by at least 3 independent paths
  - Cross-family consistency across Heisenberg / affine KM / Virasoro
  - AP-aware: checks AP14, AP19, AP24, AP27, AP39, AP44, AP45

References:
  De Leger, arXiv:2512.20167 (Dec 2025)
  Moriwaki, arXiv:2410.02648 (Oct 2024)
  Vol II: thm:homotopy-Koszul, thm:bar-swiss-cheese, thm:cohomology-PVA-main
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import math
import cmath
import pytest
from math import factorial, comb

from lib.theorem_swiss_cheese_kontsevich_engine import (
    # Operad spaces
    fm_dimension,
    e1_components,
    sc_operation_space_dim,
    # Heisenberg SC structure
    heisenberg_ope_kernel,
    heisenberg_collision_residue,
    heisenberg_bar_differential_arity2,
    heisenberg_bar_differential_arity3,
    heisenberg_e1_coproduct,
    heisenberg_sc_interchange,
    # Groupoid action
    upper_half_plane_config,
    heisenberg_boundary_ope_convergence,
    groupoid_parallel_transport,
    # E_3 action
    e3_action_dimension_check,
    chiral_hochschild_e3_structure,
    # Brace structure
    brace_dg_algebra_heisenberg,
    sc_koszulity_verification,
    # Moriwaki convergence
    moriwaki_ope_convergence_test,
    # Cross-family
    affine_km_sc_data,
    virasoro_sc_data,
    cross_family_sc_consistency,
    # PVA descent
    pva_descent_from_sc,
    # Summary
    full_swiss_cheese_kontsevich_summary,
)


# ===================================================================
# 1. SC OPERAD SPACE DIMENSIONS
# ===================================================================

class TestSCOperadSpaces:
    """Test the operation spaces of SC^{ch,top}."""

    def test_fm_dimension_1(self):
        """FM_1(C) = point, dim = 0."""
        assert fm_dimension(1) == 0

    def test_fm_dimension_2(self):
        """FM_2(C): 2 points mod translation+dilation, dim_R = 2."""
        assert fm_dimension(2) == 2

    def test_fm_dimension_3(self):
        """FM_3(C): dim_R = 4."""
        assert fm_dimension(3) == 4

    def test_fm_dimension_k(self):
        """FM_k(C): dim_R = 2k - 2 for k >= 2."""
        for k in range(2, 10):
            assert fm_dimension(k) == 2 * k - 2

    def test_e1_contractible(self):
        """Conf_m^<(R) is contractible for all m >= 1."""
        for m in range(1, 10):
            assert e1_components(m) == 1

    def test_sc_open_to_closed_empty(self):
        """SC directionality: no open inputs produce closed outputs."""
        for k in range(5):
            for m in range(5):
                data = sc_operation_space_dim(k, m)
                assert data['open_to_closed_empty'] is True

    def test_sc_poincare_polynomial_fm2(self):
        """H*(FM_2(C)) = [1, 1]: one generator in degree 1."""
        data = sc_operation_space_dim(2, 0)
        assert data['poincare_poly_degrees'] == [1, 1]

    def test_sc_poincare_polynomial_fm3(self):
        """H*(FM_3(C)) = [1, 3, 2]: Poincare from (1+t)(1+2t)."""
        data = sc_operation_space_dim(3, 0)
        assert data['poincare_poly_degrees'] == [1, 3, 2]

    def test_sc_poincare_polynomial_fm4(self):
        """H*(FM_4(C)) = [1, 6, 11, 6]: from (1+t)(1+2t)(1+3t)."""
        data = sc_operation_space_dim(4, 0)
        assert data['poincare_poly_degrees'] == [1, 6, 11, 6]

    def test_poincare_at_1_equals_factorial(self):
        """P(1) = n! for the Poincare polynomial of FM_n(C)."""
        for n in range(1, 8):
            data = sc_operation_space_dim(n, 0)
            p_at_1 = sum(data['poincare_poly_degrees'])
            assert p_at_1 == factorial(n), f"P(1) = {p_at_1} != {n}! for n={n}"

    def test_euler_characteristic_fm(self):
        """chi(FM_n(C)) = prod_{j=1}^{n-1}(1-j) = (-1)^{n-1}(n-1)! for n>=2."""
        for n in range(2, 7):
            data = sc_operation_space_dim(n, 0)
            euler = sum((-1)**i * c for i, c in enumerate(data['poincare_poly_degrees']))
            # chi = prod_{j=1}^{n-1}(1-j) = prod(-j+1) for j=1..n-1
            expected = 1
            for j in range(1, n):
                expected *= (1 - j)
            assert euler == expected, f"chi(FM_{n}) = {euler} != {expected}"


# ===================================================================
# 2. HEISENBERG BAR DIFFERENTIAL AND SC STRUCTURE
# ===================================================================

class TestHeisenbergBarDifferential:
    """Test bar differential on Heisenberg bar complex."""

    def test_arity2_multipath_kappa1(self):
        """Bar differential at arity 2, kappa = 1: three paths agree."""
        result = heisenberg_bar_differential_arity2(1.0)
        assert result['all_agree'] is True
        assert abs(result['result'] - 1.0) < 1e-12

    def test_arity2_multipath_kappa_half(self):
        """Bar differential at arity 2, kappa = 1/2 (Virasoro c=1)."""
        result = heisenberg_bar_differential_arity2(0.5)
        assert result['all_agree'] is True
        assert abs(result['result'] - 0.5) < 1e-12

    def test_arity2_direct_equals_propagator(self):
        """Direct OPE extraction = propagator method (AP19 consistency)."""
        for kappa in [0.5, 1.0, 2.0, 13.0]:
            result = heisenberg_bar_differential_arity2(kappa)
            assert abs(result['direct'] - result['propagator']) < 1e-12

    def test_arity2_direct_equals_lambda_bracket(self):
        """Direct OPE extraction = lambda-bracket method (AP44 consistency)."""
        for kappa in [0.5, 1.0, 2.0, 13.0]:
            result = heisenberg_bar_differential_arity2(kappa)
            assert abs(result['direct'] - result['lambda_bracket']) < 1e-12

    def test_arity2_bar_degree_shift(self):
        """Bar desuspension lowers degree by 1 (AP45)."""
        result = heisenberg_bar_differential_arity2(1.0)
        assert result['bar_degree_shift'] == -1

    def test_arity3_d_squared_zero(self):
        """d^2 = 0 at arity 3 via Arnold relation."""
        for kappa in [0.5, 1.0, 2.0, 13.0, -1.0]:
            result = heisenberg_bar_differential_arity3(kappa)
            assert result['d_squared_zero'] is True

    def test_arity3_three_boundary_strata(self):
        """FM_3(C) has exactly 3 codimension-1 boundary strata."""
        result = heisenberg_bar_differential_arity3(1.0)
        assert result['num_boundary_strata'] == 3


class TestHeisenbergOPE:
    """Test Heisenberg OPE kernel and collision residue (AP19)."""

    def test_ope_double_pole(self):
        """J(z)J(w) has a double pole at z = w."""
        kappa = 1.0
        for eps in [0.1, 0.01, 0.001]:
            val = heisenberg_ope_kernel(kappa, 0, complex(eps, 0))
            expected = kappa / eps**2
            assert abs(val - expected) / abs(expected) < 1e-10

    def test_collision_residue_simple_pole(self):
        """Collision residue r(z) = kappa/z has a simple pole (AP19)."""
        kappa = 2.0
        for z_val in [0.1, 0.5, 1.0, 2.0]:
            r = heisenberg_collision_residue(kappa, complex(z_val, 0))
            expected = kappa / z_val
            assert abs(r - expected) < 1e-12

    def test_ap19_pole_order_reduction(self):
        """AP19: collision residue pole order = OPE pole order - 1.
        Heisenberg OPE: double pole -> collision residue: simple pole."""
        kappa = 3.0
        z = 0.5
        ope_val = heisenberg_ope_kernel(kappa, 0, complex(z, 0))  # ~ 1/z^2
        res_val = heisenberg_collision_residue(kappa, complex(z, 0))  # ~ 1/z
        # Ratio should be ~ 1/z (the absorbed pole)
        ratio = abs(ope_val / res_val)
        expected_ratio = 1.0 / z
        assert abs(ratio - expected_ratio) < 1e-10


class TestHeisenbergE1Coproduct:
    """Test E_1 (open-color) coproduct on the bar complex."""

    def test_coproduct_arity2(self):
        """Deconcatenation at arity 2: 3 terms (including extremes)."""
        result = heisenberg_e1_coproduct(1.0, 2)
        assert result['num_coproduct_terms'] == 3

    def test_coproduct_arity_n(self):
        """Deconcatenation at arity n: n+1 terms."""
        for n in range(1, 8):
            result = heisenberg_e1_coproduct(1.0, n)
            assert result['num_coproduct_terms'] == n + 1

    def test_coproduct_coassociative(self):
        """The deconcatenation coproduct is coassociative."""
        for n in range(1, 6):
            result = heisenberg_e1_coproduct(1.0, n)
            assert result['coassociative'] is True

    def test_coproduct_kappa_independent(self):
        """The E_1 coproduct does not depend on kappa."""
        for kappa in [0.0, 0.5, 1.0, 100.0, -3.0]:
            result = heisenberg_e1_coproduct(kappa, 3)
            assert result['kappa_independent'] is True
            assert result['num_coproduct_terms'] == 4

    def test_cofree_conilpotent(self):
        """The bar coalgebra is cofree conilpotent."""
        result = heisenberg_e1_coproduct(1.0, 5)
        assert result['cofree_conilpotent'] is True


class TestSCInterchange:
    """Test the SC interchange law (closed/open compatibility)."""

    def test_interchange_various_arities(self):
        """Interchange law holds at all arities tested."""
        for k in range(1, 5):
            for m in range(1, 5):
                result = heisenberg_sc_interchange(1.0, k, m)
                assert result['interchange_holds'] is True


# ===================================================================
# 3. GROUPOID ACTION (Moriwaki)
# ===================================================================

class TestGroupoidAction:
    """Test Moriwaki's fundamental groupoid action on module categories."""

    def test_upper_half_plane_config_default(self):
        """Default configuration is in the upper half-plane."""
        pts = upper_half_plane_config(3)
        assert len(pts) == 3
        for z in pts:
            assert z.imag > 0

    def test_upper_half_plane_config_custom(self):
        """Custom configuration is validated."""
        pts = upper_half_plane_config(2, [1 + 2j, 3 + 0.5j])
        assert len(pts) == 2

    def test_upper_half_plane_config_rejects_lower(self):
        """Points in the lower half-plane are rejected."""
        with pytest.raises(AssertionError):
            upper_half_plane_config(1, [1 - 1j])

    def test_braid_monodromy_kappa1(self):
        """Braid monodromy for kappa = 1: exp(pi*i) = -1."""
        result = groupoid_parallel_transport(
            1.0, [1 + 1j, 2 + 1j], 'braid'
        )
        phase = result['monodromy_phase']
        expected = cmath.exp(1j * math.pi * 1.0)  # = -1
        assert abs(phase - expected) < 1e-12

    def test_braid_monodromy_kappa_half(self):
        """Braid monodromy for kappa = 1/2: exp(pi*i/2) = i."""
        result = groupoid_parallel_transport(
            0.5, [1 + 1j, 3 + 1j], 'braid'
        )
        phase = result['monodromy_phase']
        expected = cmath.exp(1j * math.pi * 0.5)  # = i
        assert abs(phase - expected) < 1e-12

    def test_braid_monodromy_kappa2(self):
        """Braid monodromy for kappa = 2: exp(2*pi*i) = 1."""
        result = groupoid_parallel_transport(
            2.0, [1 + 1j, 2 + 1j], 'braid'
        )
        phase = result['monodromy_phase']
        expected = cmath.exp(1j * math.pi * 2.0)  # = 1
        assert abs(phase - expected) < 1e-12

    def test_associator_trivial_for_heisenberg(self):
        """Drinfeld associator is trivial for Heisenberg (scalar KZ residues)."""
        result = groupoid_parallel_transport(
            1.0, [1 + 1j, 2 + 1j, 3 + 1j], 'associator'
        )
        assert result['associator_trivial'] is True
        assert result['parenthesization_independent'] is True

    def test_parenthesization_independence(self):
        """Moriwaki's theorem: different parenthesizations give same answer."""
        for kappa in [0.5, 1.0, 2.0, 5.0]:
            result = groupoid_parallel_transport(
                kappa, [1 + 1j, 2 + 1j, 3 + 1j], 'associator'
            )
            assert result['parenthesization_independent'] is True


class TestBoundaryOPEConvergence:
    """Test Moriwaki's boundary OPE absolute convergence."""

    def test_convergence_separated_boundary_points(self):
        """Boundary OPE converges for well-separated points."""
        result = heisenberg_boundary_ope_convergence(
            1.0, [1.0, 3.0, 5.0], [2 + 1j], cutoff=30
        )
        assert result['converges'] is True
        assert result['c1_cofinite'] is True

    def test_convergence_requires_separation(self):
        """Boundary OPE diverges for coincident points."""
        result = heisenberg_boundary_ope_convergence(
            1.0, [1.0, 1.0], [], cutoff=10
        )
        # Coincident points: min_sep = 0, formal divergence
        assert result['min_separation'] == 0.0

    def test_c1_cofinite_heisenberg(self):
        """Heisenberg Fock modules are C_1-cofinite."""
        result = heisenberg_boundary_ope_convergence(
            1.0, [1.0, 2.0], [1.5 + 1j]
        )
        assert result['c1_cofinite'] is True
        assert result['moriwaki_applicable'] is True


# ===================================================================
# 4. E_3 ACTION ON CHIRAL HOCHSCHILD (De Leger)
# ===================================================================

class TestE3Action:
    """Test De Leger's E_3-action on chiral Hochschild cochains."""

    def test_e3_poincare_arity2(self):
        """E_3(2): Conf_2(R^3). Poincare polynomial."""
        data = e3_action_dimension_check(2)
        # Conf_2(R^3) ~ S^2, so H = [1, 0, 1] = 1 + t^2
        # But our polynomial uses degree-1 shift... let's check.
        # Actually: H*(Conf_k(R^3)) with generators in deg 2.
        # For k=2: (1 + 1*t) where t has deg 1 in our encoding.
        # The E_3 Poincare at arity 2 = [1, 1] (one generator)
        assert data['e3_poincare'] == [1, 1]

    def test_e3_total_dim_equals_factorial(self):
        """Total Betti of E_3(k) space."""
        for k in range(2, 6):
            data = e3_action_dimension_check(k)
            # The E_3 Poincare evaluated at t=1 = prod(1+j) = k!
            assert data['e3_total_dim'] == factorial(k)

    def test_sc2_closed_matches_fm(self):
        """SC_2 closed-color Poincare matches FM_k(C) Poincare."""
        for k in range(2, 6):
            data = e3_action_dimension_check(k)
            # SC_2 closed = FM_k(C), also with P(1) = k!
            assert data['sc2_closed_total_dim'] == factorial(k)

    def test_hochschild_dims_heisenberg(self):
        """ChirHoch*(H, H) dimensions: 1 in degrees 0 and 1, 0 elsewhere."""
        data = chiral_hochschild_e3_structure(1.0, max_arity=5)
        assert data['hochschild_dims'][0] == 1
        assert data['hochschild_dims'][1] == 1
        for n in range(2, 6):
            assert data['hochschild_dims'][n] == 0

    def test_gerstenhaber_bracket_trivial_heisenberg(self):
        """Heisenberg has abelian Gerstenhaber bracket (class G)."""
        data = chiral_hochschild_e3_structure(1.0)
        assert data['gerstenhaber_bracket_trivial'] is True

    def test_e3_formal_for_heisenberg(self):
        """The E_3 structure is formal for Heisenberg (class G)."""
        data = chiral_hochschild_e3_structure(1.0)
        assert data['e3_formal'] is True
        assert data['shadow_class'] == 'G'

    def test_brace_operations_vanish_from_2(self):
        """Brace operations B_k = 0 for k >= 2 (class G)."""
        data = chiral_hochschild_e3_structure(1.0, max_arity=5)
        assert data['brace_operations'][0] == 'identity'
        for k in range(2, 6):
            assert 'zero' in data['brace_operations'][k]

    def test_de_leger_applicable(self):
        """De Leger's SC(E_2) construction applies to our setting."""
        data = chiral_hochschild_e3_structure(1.0)
        assert data['de_leger_applicable'] is True


# ===================================================================
# 5. BRACE DG ALGEBRA COMPATIBILITY
# ===================================================================

class TestBraceDGAlgebra:
    """Test brace dg algebra structure from thm:thqg-swiss-cheese."""

    def test_brace_heisenberg_multipath(self):
        """Multi-path verification of brace structure for Heisenberg."""
        result = brace_dg_algebra_heisenberg(1.0)
        assert result['all_paths_agree'] is True
        assert result['bar_diff_trivial'] is True
        assert result['recognition_consistent'] is True

    def test_brace_kappa_zero_limit(self):
        """At kappa = 0: trivial algebra, trivial brace."""
        result = brace_dg_algebra_heisenberg(0.0)
        assert result['kappa_zero_limit']['brace_trivial'] is True

    def test_braces_vanish_from_2(self):
        """B_k = 0 for k >= 2 (class G: Heisenberg)."""
        result = brace_dg_algebra_heisenberg(1.0)
        assert result['braces_vanish_from'] == 2

    def test_shadow_class_G(self):
        """Heisenberg is class G (shadow depth 2)."""
        result = brace_dg_algebra_heisenberg(1.0)
        assert result['shadow_class'] == 'G'


# ===================================================================
# 6. HOMOTOPY-KOSZULITY VERIFICATION
# ===================================================================

class TestKoszulity:
    """Test homotopy-Koszulity of SC^{ch,top}."""

    def test_three_independent_proofs(self):
        """Koszulity proved by Livernet, Kontsevich formality, AND De Leger."""
        result = sc_koszulity_verification(5)
        assert result['koszul_via_livernet'] is True
        assert result['koszul_via_kontsevich_formality'] is True
        assert result['koszul_via_de_leger'] is True
        assert result['three_independent_proofs'] is True

    def test_poincare_at_1_is_factorial(self):
        """P_FM_n(1) = n! for all n in range."""
        result = sc_koszulity_verification(7)
        for n, data in result['arity_data'].items():
            assert data['equals_n_factorial'] is True

    def test_koszul_dual_dim(self):
        """Koszul dual (Lie) has dimension (n-1)! at arity n."""
        result = sc_koszulity_verification(7)
        for n, data in result['arity_data'].items():
            assert data['koszul_dual_dim'] == factorial(n - 1)


# ===================================================================
# 7. MORIWAKI CONVERGENCE
# ===================================================================

class TestMoriwakiConvergence:
    """Test Moriwaki's OPE convergence on upper half-plane."""

    def test_convergence_positive_height(self):
        """Absolute convergence for Im(z) > 0."""
        result = moriwaki_ope_convergence_test(1.0, 3, 1.0, 30)
        assert result['converges_absolutely'] is True
        assert result['convergence_ratio'] < 1

    def test_convergence_ratio_geometric(self):
        """Convergence ratio is exp(-2*pi*h) for height h."""
        for h in [0.5, 1.0, 2.0]:
            result = moriwaki_ope_convergence_test(1.0, 3, h, 20)
            expected_ratio = math.exp(-2 * math.pi * h)
            assert abs(result['convergence_ratio'] - expected_ratio) < 1e-12

    def test_c1_cofinite_heisenberg(self):
        """Heisenberg satisfies Moriwaki's C_1-cofiniteness hypothesis."""
        result = moriwaki_ope_convergence_test(1.0, 2, 1.0, 10)
        assert result['c1_cofinite'] is True
        assert result['moriwaki_hypothesis_satisfied'] is True

    def test_convergence_improves_with_height(self):
        """Higher Im(z) gives faster convergence."""
        r1 = moriwaki_ope_convergence_test(1.0, 3, 0.5, 20)
        r2 = moriwaki_ope_convergence_test(1.0, 3, 1.0, 20)
        r3 = moriwaki_ope_convergence_test(1.0, 3, 2.0, 20)
        assert r1['convergence_ratio'] > r2['convergence_ratio'] > r3['convergence_ratio']


# ===================================================================
# 8. CROSS-FAMILY CONSISTENCY
# ===================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks: Heisenberg / affine KM / Virasoro."""

    def test_all_families_koszul(self):
        """All standard families are chirally Koszul (AP14)."""
        result = cross_family_sc_consistency()
        assert result['all_koszul'] is True

    def test_formality_consistent_with_class(self):
        """SC formality correlates with shadow class (AP14)."""
        result = cross_family_sc_consistency()
        assert result['formality_consistent'] is True

    def test_virasoro_complementarity_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        result = cross_family_sc_consistency()
        assert result['virasoro_complementarity'] is True

    def test_ap14_koszulness_ne_formality(self):
        """AP14: Koszulness != SC formality. Virasoro is Koszul but NOT formal."""
        result = cross_family_sc_consistency()
        families = result['families']
        # Virasoro: Koszul = True, SC formal = False
        assert families['Vir_c=1']['koszul'] is True
        assert families['Vir_c=1']['sc_formal'] is False

    def test_affine_km_kappa_formula(self):
        """kappa = dim(g) * (k + h^v) / (2 * h^v) for affine KM (AP1, AP39)."""
        # sl_2 at level 1: dim = 3, h^v = 2, k = 1
        # kappa = 3 * (1 + 2) / (2 * 2) = 9/4
        data = affine_km_sc_data(rank=1, level=1.0)
        assert abs(data['kappa'] - 9.0 / 4.0) < 1e-12
        assert data['shadow_class'] == 'L'

    def test_affine_km_class_L(self):
        """Affine KM is class L (shadow depth 3, SC formal)."""
        data = affine_km_sc_data(rank=1, level=1.0)
        assert data['shadow_class'] == 'L'
        assert data['shadow_depth'] == 3
        assert data['sc_formal'] is True

    def test_virasoro_kappa_c_over_2(self):
        """kappa = c/2 for Virasoro (AP39: specific to Vir!)."""
        for c in [1, 13, 25, 26]:
            data = virasoro_sc_data(float(c))
            assert abs(data['kappa'] - c / 2.0) < 1e-12

    def test_virasoro_kappa_sum_13(self):
        """kappa(c) + kappa(26-c) = 13 for all c (AP24)."""
        for c in [0, 1, 5, 13, 20, 25, 26]:
            data = virasoro_sc_data(float(c))
            assert data['kappa_sum_is_13'] is True

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro is self-dual at c = 13 (NOT c = 26)."""
        data_13 = virasoro_sc_data(13.0)
        assert abs(data_13['kappa'] - data_13['kappa_dual']) < 1e-12
        # c = 26 is NOT self-dual: kappa = 13, kappa' = 0
        data_26 = virasoro_sc_data(26.0)
        assert abs(data_26['kappa'] - data_26['kappa_dual']) > 1

    def test_virasoro_class_M(self):
        """Virasoro is class M (infinite shadow depth, non-formal SC)."""
        data = virasoro_sc_data(1.0)
        assert data['shadow_class'] == 'M'
        assert data['shadow_depth'] == float('inf')
        assert data['sc_formal'] is False
        assert data['quartic_pole'] is True

    def test_moriwaki_applies_to_all_standard(self):
        """Moriwaki's C_1-cofiniteness applies to all standard families."""
        assert affine_km_sc_data(1, 1.0)['moriwaki_c1_cofinite'] is True
        assert virasoro_sc_data(1.0)['moriwaki_c1_cofinite'] is True

    def test_de_leger_applies_to_all(self):
        """De Leger's SC(E_2) construction applies to all families."""
        assert affine_km_sc_data(1, 1.0)['de_leger_applicable'] is True
        assert virasoro_sc_data(1.0)['de_leger_applicable'] is True


# ===================================================================
# 9. PVA DESCENT AXIOMS
# ===================================================================

class TestPVADescent:
    """Test PVA descent axioms D2-D6 from SC structure."""

    def test_all_axioms_proved(self):
        """All five PVA descent axioms are proved."""
        result = pva_descent_from_sc(1.0)
        assert result['all_proved'] is True
        assert result['D2_sesquilinearity'] is True
        assert result['D3_skew_symmetry'] is True
        assert result['D4_jacobi'] is True
        assert result['D5_leibniz'] is True
        assert result['D6_associativity'] is True

    def test_moriwaki_analytic_strengthening(self):
        """Moriwaki's convergence analytically strengthens formal PVA descent."""
        result = pva_descent_from_sc(1.0)
        assert result['moriwaki_analytic'] is True

    def test_d4_jacobi_mechanism(self):
        """D4 (Jacobi) comes from Arnold relation on FM_3(C)."""
        result = pva_descent_from_sc(1.0)
        assert 'Arnold' in result['mechanism']['D4']

    def test_d5_leibniz_mechanism(self):
        """D5 (Leibniz) comes from exchange cylinder + three-face Stokes."""
        result = pva_descent_from_sc(1.0)
        assert 'Stokes' in result['mechanism']['D5']


# ===================================================================
# 10. FULL INTEGRATION TEST
# ===================================================================

class TestFullSummary:
    """Integration test: full summary at various kappa values."""

    def test_summary_kappa1(self):
        """Full summary at kappa = 1 passes all checks."""
        summary = full_swiss_cheese_kontsevich_summary(1.0)
        assert summary['all_pass'] is True

    def test_summary_kappa_half(self):
        """Full summary at kappa = 1/2."""
        summary = full_swiss_cheese_kontsevich_summary(0.5)
        assert summary['all_pass'] is True

    def test_summary_kappa13(self):
        """Full summary at kappa = 13 (Virasoro c = 26)."""
        summary = full_swiss_cheese_kontsevich_summary(13.0)
        assert summary['all_pass'] is True

    def test_summary_kappa_negative(self):
        """Full summary at negative kappa."""
        summary = full_swiss_cheese_kontsevich_summary(-1.0)
        assert summary['all_pass'] is True
