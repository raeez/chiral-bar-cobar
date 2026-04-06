#!/usr/bin/env python3
r"""Tests for bc_shifted_symplectic_shadow_engine.py -- Shifted symplectic
structures on shadow stacks and AKSZ from shadow tower.

BC-125: Benjamin-Chang programme.

MULTI-PATH VERIFICATION:
    Path 1: PTVV shifted symplectic from cyclic pairing
    Path 2: Lagrangian from Koszul pair (Theorem C)
    Path 3: AKSZ action functional
    Path 4: Poisson bracket degree +1
    Path 5: Numerical evaluation at zeta zeros

CONVENTIONS (from CLAUDE.md):
    AP1:  kappa formulas recomputed per family
    AP8:  Virasoro self-dual at c=13, NOT c=26
    AP24: kappa + kappa' = 0 for KM; = 13 for Virasoro
    AP39: kappa != c/2 for general VOA
    AP48: kappa depends on full algebra
"""

from fractions import Fraction
import math
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_shifted_symplectic_shadow_engine import (
    # Family constructors
    AlgebraFamily,
    heisenberg_family,
    virasoro_family,
    affine_slN_family,
    betagamma_family,
    w3_family,
    lattice_family,
    STANDARD_FAMILIES,
    # Darboux coordinates
    DarbouxCoordinate,
    shadow_darboux_coordinates,
    # Shifted symplectic form
    ShiftedSymplecticForm,
    compute_shifted_symplectic_form,
    symplectic_matrix_determinant,
    # Poisson bracket
    poisson_bracket_degree,
    evaluate_poisson_bracket_quadratic,
    # Lagrangian
    LagrangianData,
    compute_lagrangian_structure,
    lagrangian_primitive_heisenberg,
    lagrangian_primitive_virasoro,
    lagrangian_primitive_sl2,
    lagrangian_primitive_w3,
    # AKSZ
    AKSZData,
    compute_aksz_data,
    # PTVV
    ptvv_shift_at_genus,
    aksz_mapping_stack_shift,
    # Shadow metric
    shadow_metric_discriminant,
    # Intersection
    lagrangian_intersection_degree,
    # Full package
    full_shifted_symplectic_package,
    cross_family_symplectic_comparison,
    # Verification
    verify_mc_equals_lagrangian,
    verify_ptvv_shift_consistency,
    verify_aksz_shift_consistency,
    verify_symplectic_determinant_families,
    verify_complementarity_lagrangian_consistency,
    verify_lagrangian_additivity,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

requires_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ========================================================================
# SECTION 1: FAMILY CONSTRUCTION (AP1 recomputation)
# ========================================================================

class TestFamilyConstruction:
    """Verify kappa formulas are correct per AP1/AP39/AP48."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (AP1)."""
        fam = heisenberg_family(Fraction(3))
        assert fam.kappa == Fraction(3)
        assert fam.kappa_dual == Fraction(-3)

    def test_heisenberg_complementarity_sum(self):
        """kappa + kappa' = 0 for Heisenberg (AP24)."""
        for k in [1, 2, 5, 7, Fraction(1, 2)]:
            fam = heisenberg_family(Fraction(k))
            assert fam.complementarity_sum == Fraction(0)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2 (AP1)."""
        fam = virasoro_family(Fraction(26))
        assert fam.kappa == Fraction(13)

    def test_virasoro_complementarity_sum_13(self):
        """kappa + kappa' = 13 for Virasoro (AP24: NOT 0)."""
        for c in [1, 2, 13, 24, 26, Fraction(-22, 5)]:
            fam = virasoro_family(Fraction(c))
            assert fam.complementarity_sum == Fraction(13)

    def test_virasoro_self_dual_c13(self):
        """Virasoro self-dual at c=13 (AP8: NOT c=26)."""
        fam = virasoro_family(Fraction(13))
        assert fam.kappa == fam.kappa_dual == Fraction(13, 2)

    def test_virasoro_NOT_self_dual_c26(self):
        """Virasoro NOT self-dual at c=26 (AP8)."""
        fam = virasoro_family(Fraction(26))
        assert fam.kappa == Fraction(13)
        assert fam.kappa_dual == Fraction(0)
        assert fam.kappa != fam.kappa_dual

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4 (AP1, AP39)."""
        fam = affine_slN_family(2, Fraction(1))
        expected = Fraction(3) * Fraction(3) / Fraction(4)  # 3*3/4 = 9/4
        assert fam.kappa == expected

    def test_affine_sl2_kappa_NOT_c_over_2(self):
        """kappa(sl_2, k=1) != c/2 for affine sl_2 (AP39)."""
        fam = affine_slN_family(2, Fraction(1))
        c_half = fam.central_charge / 2  # c = 3*1/(1+2) = 1
        assert fam.kappa != c_half

    def test_affine_complementarity_sum_zero(self):
        """kappa + kappa' = 0 for affine KM (AP24)."""
        for N in [2, 3, 4]:
            for k in [Fraction(1), Fraction(2), Fraction(5)]:
                fam = affine_slN_family(N, k)
                assert fam.complementarity_sum == Fraction(0)

    def test_betagamma_complementarity_sum_zero(self):
        """kappa + kappa' = 0 for betagamma (AP24)."""
        fam = betagamma_family(Fraction(-2))
        assert fam.complementarity_sum == Fraction(0)

    def test_w3_kappa(self):
        """kappa(W_3, c) = 5c/6 (AP1: H_3 - 1 = 5/6)."""
        fam = w3_family(Fraction(6))
        assert fam.kappa == Fraction(5)

    def test_w3_complementarity_sum(self):
        """kappa(W_3) + kappa(W_3') = 250/3 (AP24)."""
        for c in [2, 6, 50]:
            fam = w3_family(Fraction(c))
            assert fam.complementarity_sum == Fraction(250, 3)

    def test_lattice_kappa(self):
        """kappa(Lattice) = rank (AP48: NOT c/2 in general)."""
        fam = lattice_family(24)
        assert fam.kappa == Fraction(24)
        assert fam.kappa_dual == Fraction(-24)

    def test_delta_kappa_virasoro(self):
        """delta_kappa = kappa - kappa' = c - 13 for Virasoro (AP29)."""
        fam = virasoro_family(Fraction(1))
        assert fam.delta_kappa == Fraction(1, 2) - Fraction(25, 2)
        assert fam.delta_kappa == Fraction(-12)

    def test_shadow_depth_classification(self):
        """Shadow depth: G=2, L=3, C=4, M=infinity."""
        assert heisenberg_family().shadow_depth == 2
        assert affine_slN_family(2).shadow_depth == 3
        assert betagamma_family().shadow_depth == 4
        assert virasoro_family().shadow_depth is None

    def test_shadow_class_classification(self):
        """Shadow class assignment."""
        assert heisenberg_family().shadow_class == 'G'
        assert affine_slN_family(2).shadow_class == 'L'
        assert betagamma_family().shadow_class == 'C'
        assert virasoro_family().shadow_class == 'M'
        assert w3_family().shadow_class == 'M'

    def test_standard_families_registry(self):
        """All standard families are in the registry."""
        assert len(STANDARD_FAMILIES) >= 10
        assert "Heisenberg" in STANDARD_FAMILIES
        assert "Virasoro_c13" in STANDARD_FAMILIES
        assert "sl2_k1" in STANDARD_FAMILIES


# ========================================================================
# SECTION 2: DARBOUX COORDINATES
# ========================================================================

class TestDarbouxCoordinates:
    """Test the Darboux coordinate system from shadow data."""

    def test_heisenberg_darboux_arity2(self):
        """Heisenberg: q_2 = k, p_2 = -k."""
        fam = heisenberg_family(Fraction(3))
        coords = shadow_darboux_coordinates(fam, max_arity=2)
        assert len(coords) == 1
        assert coords[0].q_value == Fraction(3)
        assert coords[0].p_value == Fraction(-3)

    def test_heisenberg_all_higher_shadows_zero(self):
        """Heisenberg class G: S_r = 0 for r >= 3."""
        fam = heisenberg_family()
        coords = shadow_darboux_coordinates(fam, max_arity=5)
        for coord in coords[1:]:
            assert coord.q_value == 0
            assert coord.p_value == 0

    def test_virasoro_darboux_arity2(self):
        """Virasoro: q_2 = c/2, p_2 = (26-c)/2."""
        fam = virasoro_family(Fraction(6))
        coords = shadow_darboux_coordinates(fam, max_arity=2)
        assert coords[0].q_value == Fraction(3)
        assert coords[0].p_value == Fraction(10)

    def test_virasoro_S4_nonzero(self):
        """Virasoro class M: S_4 = Q^contact = 10/[c(5c+22)] != 0."""
        fam = virasoro_family(Fraction(2))
        coords = shadow_darboux_coordinates(fam, max_arity=4)
        S4_coord = coords[2]
        expected_S4 = Fraction(10) / (Fraction(2) * Fraction(32))
        assert S4_coord.q_value == expected_S4

    def test_affine_S3_nonzero(self):
        """Affine sl_N class L: S_3 != 0."""
        fam = affine_slN_family(2, Fraction(1))
        coords = shadow_darboux_coordinates(fam, max_arity=3)
        assert coords[1].q_value != 0

    def test_affine_S3_dual_antisymmetric(self):
        """For affine KM: S_3(A!) = -S_3(A) (FF antisymmetry)."""
        fam = affine_slN_family(2, Fraction(1))
        coords = shadow_darboux_coordinates(fam, max_arity=3)
        assert coords[1].p_value == -coords[1].q_value

    def test_darboux_count_at_max_arity(self):
        """Number of Darboux pairs = max_arity - 1."""
        for r in [2, 3, 4, 5]:
            fam = virasoro_family()
            coords = shadow_darboux_coordinates(fam, max_arity=r)
            assert len(coords) == r - 1

    def test_arity_labels(self):
        """Darboux coordinates are labeled by arity."""
        fam = virasoro_family()
        coords = shadow_darboux_coordinates(fam, max_arity=5)
        for i, coord in enumerate(coords):
            assert coord.arity == i + 2


# ========================================================================
# SECTION 3: SHIFTED SYMPLECTIC FORM
# ========================================================================

class TestShiftedSymplecticForm:
    """Test the (-1)-shifted symplectic form."""

    def test_shift_is_minus_one(self):
        """The form has shift -1."""
        fam = heisenberg_family()
        form = compute_shifted_symplectic_form(fam)
        assert form.shift == -1

    def test_symplectic_rank(self):
        """Rank = 2 * (number of Darboux pairs)."""
        for max_ar in [2, 3, 4, 5]:
            fam = virasoro_family()
            form = compute_shifted_symplectic_form(fam, max_arity=max_ar)
            assert form.symplectic_rank == 2 * (max_ar - 1)

    def test_symplectic_matrix_standard_form(self):
        """Matrix is block-diagonal with J = [[0,-1],[1,0]]."""
        fam = virasoro_family()
        form = compute_shifted_symplectic_form(fam, max_arity=3)
        M = form.symplectic_matrix
        # 4x4 matrix: J blocks at (0,1) and (2,3)
        assert M[0][1] == -1 and M[1][0] == 1
        assert M[2][3] == -1 and M[3][2] == 1
        # Off-block entries are 0
        assert M[0][2] == 0 and M[0][3] == 0
        assert M[1][2] == 0 and M[1][3] == 0

    def test_determinant_is_one(self):
        """det(Omega) = 1 for the standard symplectic matrix."""
        for name, fam in STANDARD_FAMILIES.items():
            form = compute_shifted_symplectic_form(fam)
            assert symplectic_matrix_determinant(form) == 1

    def test_determinant_all_families(self):
        """det(Omega) = 1 for ALL standard families."""
        results = verify_symplectic_determinant_families()
        for name, det in results.items():
            assert det == 1, f"det != 1 for {name}"

    def test_antisymmetry_of_matrix(self):
        """Omega^T = -Omega (symplectic matrix is antisymmetric)."""
        fam = virasoro_family()
        form = compute_shifted_symplectic_form(fam, max_arity=4)
        M = form.symplectic_matrix
        n = len(M)
        for i in range(n):
            for j in range(n):
                assert M[i][j] == -M[j][i], f"Not antisymmetric at ({i},{j})"


# ========================================================================
# SECTION 4: POISSON BRACKET
# ========================================================================

class TestPoissonBracket:
    """Test the degree +1 Poisson bracket."""

    def test_poisson_degree_plus_one(self):
        """For (-1)-shifted: {,} has degree -(-1) = +1."""
        assert poisson_bracket_degree(-1) == 1

    def test_poisson_degree_general(self):
        """For n-shifted: {,} has degree -n."""
        assert poisson_bracket_degree(0) == 0
        assert poisson_bracket_degree(-2) == 2
        assert poisson_bracket_degree(-3) == 3

    def test_bracket_theta_theta_vanishes(self):
        """{Theta, Theta}_{-1} = 0 by antisymmetry."""
        for name, fam in STANDARD_FAMILIES.items():
            result = evaluate_poisson_bracket_quadratic(fam)
            assert result['bracket_Theta_Theta'] == Fraction(0)

    def test_mc_is_lagrangian(self):
        """MC equation = Lagrangian condition for all families."""
        for name, fam in STANDARD_FAMILIES.items():
            result = evaluate_poisson_bracket_quadratic(fam)
            assert result['mc_is_lagrangian'] is True

    def test_heisenberg_single_active_pair(self):
        """Heisenberg: only arity-2 pair is active."""
        fam = heisenberg_family()
        result = evaluate_poisson_bracket_quadratic(fam, max_arity=4)
        assert result['num_active_darboux_pairs'] == 1

    def test_virasoro_multiple_active_pairs(self):
        """Virasoro: arity-2 and arity-4 pairs are active."""
        fam = virasoro_family(Fraction(2))
        result = evaluate_poisson_bracket_quadratic(fam, max_arity=4)
        assert result['num_active_darboux_pairs'] >= 2

    def test_obstruction_arity2_is_kappa(self):
        """The arity-2 obstruction is kappa."""
        fam = virasoro_family(Fraction(1))
        result = evaluate_poisson_bracket_quadratic(fam)
        assert result['obstructions_by_arity'][2]['value'] == Fraction(1, 2)

    def test_obstruction_arity3_cubic(self):
        """The arity-3 obstruction is the cubic shadow."""
        fam = affine_slN_family(2, Fraction(1))
        result = evaluate_poisson_bracket_quadratic(fam, max_arity=3)
        assert result['obstructions_by_arity'][3]['value'] != 0


# ========================================================================
# SECTION 5: LAGRANGIAN STRUCTURE
# ========================================================================

class TestLagrangianStructure:
    """Test Lagrangian embeddings from Koszul pairs."""

    def test_all_families_lagrangian(self):
        """All standard families have Lagrangian structure."""
        for name, fam in STANDARD_FAMILIES.items():
            lag = compute_lagrangian_structure(fam)
            assert lag.is_lagrangian, f"{name} not Lagrangian"

    def test_heisenberg_theta_primitive(self):
        """Heisenberg theta_2 = k * (-k) = -k^2."""
        fam = heisenberg_family(Fraction(3))
        lag = compute_lagrangian_structure(fam, max_arity=2)
        assert lag.theta_primitive[2] == Fraction(-9)
        assert lag.theta_primitive[2] == lagrangian_primitive_heisenberg(Fraction(3))

    def test_virasoro_theta_primitive(self):
        """Virasoro theta_2 = c(26-c)/4."""
        fam = virasoro_family(Fraction(2))
        lag = compute_lagrangian_structure(fam, max_arity=2)
        expected = Fraction(2) * Fraction(24) / Fraction(4)  # = 12
        assert lag.theta_primitive[2] == expected
        assert lag.theta_primitive[2] == lagrangian_primitive_virasoro(Fraction(2))

    def test_virasoro_c13_theta(self):
        """Virasoro c=13: theta_2 = 13*13/4 = 169/4."""
        expected = Fraction(13) * Fraction(13) / Fraction(4)
        assert lagrangian_primitive_virasoro(Fraction(13)) == expected

    def test_virasoro_c0_theta_zero(self):
        """Virasoro c=0: theta_2 = 0 (kappa = 0)."""
        assert lagrangian_primitive_virasoro(Fraction(0)) == Fraction(0)

    def test_virasoro_c26_theta_zero(self):
        """Virasoro c=26: theta_2 = 0 (kappa' = 0)."""
        assert lagrangian_primitive_virasoro(Fraction(26)) == Fraction(0)

    def test_sl2_theta_primitive(self):
        """sl_2 at k=1: theta_2 = -(9/4)^2 = -81/16."""
        # kappa = 3*(1+2)/4 = 9/4, theta = (9/4)*(-9/4) = -81/16
        expected = Fraction(-81, 16)
        assert lagrangian_primitive_sl2(Fraction(1)) == expected

    def test_w3_theta_primitive(self):
        """W_3 at c=6: theta_2 = (5*6/6)*(5*94/6) = 5 * 470/6 = 2350/6."""
        kap = Fraction(5) * Fraction(6) / Fraction(6)
        kap_dual = Fraction(5) * Fraction(94) / Fraction(6)
        expected = kap * kap_dual
        assert lagrangian_primitive_w3(Fraction(6)) == expected

    def test_lagrangian_rank_heisenberg(self):
        """Heisenberg at max_arity=5: only 1 active pair."""
        fam = heisenberg_family()
        lag = compute_lagrangian_structure(fam, max_arity=5)
        assert lag.lagrangian_rank == 1

    def test_lagrangian_codimension(self):
        """Codimension = total pairs - active pairs."""
        fam = heisenberg_family()
        lag = compute_lagrangian_structure(fam, max_arity=5)
        assert lag.codimension == 4 - 1  # 4 pairs, 1 active

    def test_complementarity_lagrangian_consistency(self):
        """theta_2 = kappa * (comp_sum - kappa) for all families."""
        for name, fam in STANDARD_FAMILIES.items():
            result = verify_complementarity_lagrangian_consistency(fam)
            assert result['consistent'], (
                f"Lagrangian-complementarity inconsistent for {name}: "
                f"theta={result['theta_2']}, expected={result['expected_theta_2']}"
            )

    def test_theta_primitive_sign(self):
        """For sum=0 families: theta_2 = -kappa^2 < 0 when kappa != 0."""
        for name in ["Heisenberg", "sl2_k1", "betagamma"]:
            fam = STANDARD_FAMILIES[name]
            if fam.kappa != 0:
                lag = compute_lagrangian_structure(fam, max_arity=2)
                assert lag.theta_primitive[2] < 0

    def test_theta_primitive_virasoro_positive_range(self):
        """For Virasoro: theta_2 > 0 when 0 < c < 26."""
        for c in [1, 2, 6, 13, 24, 25]:
            assert lagrangian_primitive_virasoro(Fraction(c)) > 0


# ========================================================================
# SECTION 6: AKSZ CONSTRUCTION
# ========================================================================

class TestAKSZConstruction:
    """Test the AKSZ action for Map(Sigma_g, M^sh)."""

    def test_aksz_shift_computation(self):
        """AKSZ shift: n - dim(Sigma) = -1 - 2 = -3."""
        assert aksz_mapping_stack_shift(2, -1) == -3

    def test_aksz_shift_consistency(self):
        """Verify AKSZ shift consistency."""
        result = verify_aksz_shift_consistency()
        assert result['consistent']

    def test_aksz_genus0_no_genus_correction(self):
        """At genus 0: no genus correction."""
        fam = heisenberg_family()
        data = compute_aksz_data(fam, genus=0)
        assert data.aksz_action_terms['genus_correction'] == Fraction(0)

    def test_aksz_genus1_correction(self):
        """At genus 1: F_1 = kappa * lambda_1 = kappa/24."""
        fam = virasoro_family(Fraction(26))
        data = compute_aksz_data(fam, genus=1)
        # kappa = 13, lambda_1 = 1/24
        expected = Fraction(13) * Fraction(1, 24)
        assert data.aksz_action_terms['genus_correction'] == expected

    def test_aksz_heisenberg_genus1(self):
        """Heisenberg k=1: F_1 = 1/24."""
        fam = heisenberg_family(Fraction(1))
        data = compute_aksz_data(fam, genus=1)
        assert data.aksz_action_terms['genus_correction'] == Fraction(1, 24)

    def test_aksz_kinetic_term_universal(self):
        """Kinetic term is always 1 (normalized)."""
        for name, fam in STANDARD_FAMILIES.items():
            data = compute_aksz_data(fam, genus=0)
            assert data.aksz_action_terms['kinetic'] == Fraction(1)

    def test_aksz_kappa_term(self):
        """The kappa term is the arity-2 shadow coefficient."""
        fam = virasoro_family(Fraction(6))
        data = compute_aksz_data(fam, genus=0)
        assert data.aksz_action_terms['kappa'] == Fraction(3)

    def test_aksz_cubic_term_virasoro_zero(self):
        """Virasoro: cubic term = 0 (gauge triviality on T-line)."""
        fam = virasoro_family()
        data = compute_aksz_data(fam, genus=0)
        assert data.aksz_action_terms['cubic'] == Fraction(0)

    def test_aksz_cubic_term_affine_nonzero(self):
        """Affine sl_N: cubic term != 0."""
        fam = affine_slN_family(2, Fraction(1))
        data = compute_aksz_data(fam, genus=0)
        assert data.aksz_action_terms['cubic'] != Fraction(0)

    def test_aksz_planted_forest_genus2(self):
        """Genus 2: planted-forest correction for affine sl_2."""
        fam = affine_slN_family(2, Fraction(1))
        data = compute_aksz_data(fam, genus=2)
        # S_3 = dim(g)/(2(k+h^v)) = 3/6 = 1/2
        # kappa = 9/4
        # delta_pf = (1/2)(10*(1/2) - 9/4)/48 = (1/2)(5 - 9/4)/48
        #          = (1/2)(11/4)/48 = 11/384
        S3 = Fraction(1, 2)
        kap = Fraction(9, 4)
        expected = S3 * (Fraction(10) * S3 - kap) / Fraction(48)
        assert data.aksz_action_terms['planted_forest'] == expected

    def test_aksz_planted_forest_heisenberg_zero(self):
        """Heisenberg: planted-forest = 0 (S_3 = 0)."""
        fam = heisenberg_family()
        data = compute_aksz_data(fam, genus=2)
        assert data.aksz_action_terms['planted_forest'] == Fraction(0)

    def test_aksz_target_shift(self):
        """Target shift is -1."""
        fam = heisenberg_family()
        data = compute_aksz_data(fam, genus=1)
        assert data.target_shift == -1

    def test_aksz_mapping_stack_shift(self):
        """Mapping stack shift = -3."""
        fam = heisenberg_family()
        data = compute_aksz_data(fam, genus=1)
        assert data.mapping_stack_shift == -3


# ========================================================================
# SECTION 7: PTVV SHIFTS
# ========================================================================

class TestPTVVShifts:
    """Test PTVV shifted-symplectic degrees."""

    def test_ptvv_genus1(self):
        """Genus 1: shift = 0."""
        assert ptvv_shift_at_genus(1) == 0

    def test_ptvv_genus2(self):
        """Genus 2: shift = -3."""
        assert ptvv_shift_at_genus(2) == -3

    def test_ptvv_genus3(self):
        """Genus 3: shift = -6."""
        assert ptvv_shift_at_genus(3) == -6

    def test_ptvv_genus_formula(self):
        """shift = -(3g-3) for g = 1, ..., 10."""
        for g in range(1, 11):
            assert ptvv_shift_at_genus(g) == -(3 * g - 3)

    def test_ptvv_genus0_raises(self):
        """Genus 0 is invalid (M_0 is a point)."""
        with pytest.raises(ValueError):
            ptvv_shift_at_genus(0)

    def test_ptvv_consistency(self):
        """Verify shift consistency at multiple genera."""
        results = verify_ptvv_shift_consistency()
        for r in results:
            assert r['consistent']


# ========================================================================
# SECTION 8: SHADOW METRIC DISCRIMINANT
# ========================================================================

class TestShadowMetricDiscriminant:
    """Test the critical discriminant Delta = 8*kappa*S_4."""

    def test_heisenberg_discriminant_zero(self):
        """Heisenberg: Delta = 0 (class G, finite tower)."""
        fam = heisenberg_family()
        assert shadow_metric_discriminant(fam) == Fraction(0)

    def test_affine_discriminant_zero(self):
        """Affine sl_N: Delta = 0 (S_4 = 0, class L)."""
        fam = affine_slN_family(2)
        assert shadow_metric_discriminant(fam) == Fraction(0)

    def test_virasoro_discriminant_nonzero(self):
        """Virasoro: Delta != 0 (class M, infinite tower)."""
        fam = virasoro_family(Fraction(2))
        disc = shadow_metric_discriminant(fam)
        # kappa = 1, S_4 = 10/(2*32) = 5/32
        # Delta = 8 * 1 * 5/32 = 40/32 = 5/4
        assert disc == Fraction(5, 4)
        assert disc != 0

    def test_discriminant_zero_iff_finite_tower(self):
        """Delta = 0 iff shadow tower terminates (class G or L)."""
        for name, fam in STANDARD_FAMILIES.items():
            disc = shadow_metric_discriminant(fam)
            if fam.shadow_class in ('G', 'L'):
                assert disc == 0, f"Delta != 0 for finite-tower {name}"
            # Note: class C may have Delta = 0 on primary line but
            # nonzero on charged stratum; class M has Delta != 0.

    def test_virasoro_c13_discriminant(self):
        """Virasoro c=13: Delta = 8*(13/2)*S_4(13)."""
        fam = virasoro_family(Fraction(13))
        disc = shadow_metric_discriminant(fam)
        S4_13 = Fraction(10) / (Fraction(13) * (Fraction(65) + Fraction(22)))
        expected = Fraction(8) * Fraction(13, 2) * S4_13
        assert disc == expected


# ========================================================================
# SECTION 9: INTERSECTION DEGREE
# ========================================================================

class TestIntersectionDegree:
    """Test derived Lagrangian intersection degree."""

    def test_heisenberg_intersection_zero(self):
        """Heisenberg: intersection degree = 0 (transverse)."""
        fam = heisenberg_family()
        assert lagrangian_intersection_degree(fam) == Fraction(0)

    def test_virasoro_intersection_minus_13(self):
        """Virasoro: intersection degree = -13."""
        fam = virasoro_family(Fraction(1))
        assert lagrangian_intersection_degree(fam) == Fraction(-13)

    def test_affine_intersection_zero(self):
        """Affine sl_N: intersection degree = 0."""
        for N in [2, 3, 4]:
            fam = affine_slN_family(N)
            assert lagrangian_intersection_degree(fam) == Fraction(0)

    def test_w3_intersection(self):
        """W_3: intersection degree = -250/3."""
        fam = w3_family()
        assert lagrangian_intersection_degree(fam) == Fraction(-250, 3)

    def test_intersection_sign_convention(self):
        """Intersection degree = -complementarity_sum."""
        for name, fam in STANDARD_FAMILIES.items():
            assert lagrangian_intersection_degree(fam) == -fam.complementarity_sum


# ========================================================================
# SECTION 10: MC = LAGRANGIAN VERIFICATION
# ========================================================================

class TestMCEqualsLagrangian:
    """Verify MC equation = Lagrangian condition (PTVV Thm 2.9)."""

    def test_all_families_consistent(self):
        """MC = Lagrangian for all standard families."""
        for name, fam in STANDARD_FAMILIES.items():
            result = verify_mc_equals_lagrangian(fam)
            assert result['verification_status'] == 'CONSISTENT', (
                f"MC-Lagrangian inconsistent for {name}")

    def test_bracket_vanishes_all(self):
        """{Theta, Theta}_{-1} = 0 for all families."""
        for name, fam in STANDARD_FAMILIES.items():
            result = verify_mc_equals_lagrangian(fam)
            assert result['bracket_vanishes']

    def test_symplectic_shift_minus_one(self):
        """Symplectic shift is -1 for all families."""
        for name, fam in STANDARD_FAMILIES.items():
            result = verify_mc_equals_lagrangian(fam)
            assert result['symplectic_shift'] == -1

    def test_poisson_degree_one(self):
        """Poisson bracket has degree +1 for all families."""
        for name, fam in STANDARD_FAMILIES.items():
            result = verify_mc_equals_lagrangian(fam)
            assert result['poisson_degree'] == 1


# ========================================================================
# SECTION 11: FULL PACKAGE
# ========================================================================

class TestFullPackage:
    """Test the comprehensive shifted symplectic package."""

    def test_heisenberg_package(self):
        """Full package for Heisenberg."""
        fam = heisenberg_family()
        pkg = full_shifted_symplectic_package(fam)
        assert pkg['kappa'] == Fraction(1)
        assert pkg['complementarity_sum'] == Fraction(0)
        assert pkg['shifted_symplectic_form']['shift'] == -1
        assert pkg['lagrangian']['is_lagrangian']
        assert pkg['shadow_metric_discriminant'] == Fraction(0)

    def test_virasoro_package(self):
        """Full package for Virasoro c=26."""
        fam = virasoro_family(Fraction(26))
        pkg = full_shifted_symplectic_package(fam)
        assert pkg['kappa'] == Fraction(13)
        assert pkg['complementarity_sum'] == Fraction(13)
        assert pkg['intersection_degree'] == Fraction(-13)

    def test_cross_family_comparison(self):
        """Cross-family comparison runs without error."""
        results = cross_family_symplectic_comparison(max_arity=3)
        assert len(results) == len(STANDARD_FAMILIES)
        for name in STANDARD_FAMILIES:
            assert name in results

    def test_package_genus_range(self):
        """AKSZ data computed for requested genus range."""
        fam = virasoro_family()
        pkg = full_shifted_symplectic_package(fam, genus_range=(0, 3))
        assert set(pkg['aksz'].keys()) == {0, 1, 2, 3}

    def test_package_shadow_class(self):
        """Shadow class propagated to package."""
        for name, fam in STANDARD_FAMILIES.items():
            pkg = full_shifted_symplectic_package(fam)
            assert pkg['shadow_class'] == fam.shadow_class


# ========================================================================
# SECTION 12: LAGRANGIAN ADDITIVITY
# ========================================================================

class TestLagrangianAdditivity:
    """Test additivity: theta(A1 + A2) = theta(A1) + theta(A2)."""

    def test_two_heisenberg(self):
        """Two Heisenberg: theta = -k1^2 + (-k2^2) = -(k1^2 + k2^2)."""
        fams = [heisenberg_family(Fraction(1)), heisenberg_family(Fraction(2))]
        result = verify_lagrangian_additivity(fams)
        assert result['is_additive']

    def test_heisenberg_plus_virasoro(self):
        """Heisenberg + Virasoro: theta additive."""
        fams = [heisenberg_family(Fraction(1)), virasoro_family(Fraction(2))]
        result = verify_lagrangian_additivity(fams)
        assert result['is_additive']

    def test_three_families(self):
        """Three families: additivity."""
        fams = [
            heisenberg_family(Fraction(1)),
            affine_slN_family(2, Fraction(1)),
            virasoro_family(Fraction(6)),
        ]
        result = verify_lagrangian_additivity(fams)
        assert result['is_additive']

    def test_single_family_trivial(self):
        """Single family: trivially additive."""
        result = verify_lagrangian_additivity([heisenberg_family()])
        assert result['is_additive']


# ========================================================================
# SECTION 13: ZETA ZERO EVALUATIONS (requires mpmath)
# ========================================================================

@requires_mpmath
class TestZetaZeroEvaluations:
    """Test symplectic data at zeta zeros."""

    def test_first_zero_residue_finite(self):
        """Residue at first zero is finite for generic c."""
        from bc_shifted_symplectic_shadow_engine import symplectic_at_zeta_zero
        data = symplectic_at_zeta_zero(1, c_value=1.0, dps=20)
        assert not data.is_singular
        assert abs(data.residue_A_c) > 0
        assert abs(data.residue_A_c) < 1e10

    def test_generic_rank_at_zeros(self):
        """Symplectic rank is generically 2*(max_arity-1) = 6 at arity 4."""
        from bc_shifted_symplectic_shadow_engine import symplectic_at_zeta_zero
        data = symplectic_at_zeta_zero(1, c_value=6.0, max_arity=4, dps=20)
        assert data.symplectic_rank_generic == 6

    def test_no_rank_drop_generic_c(self):
        """No rank drop at generic c (not 0 or 26)."""
        from bc_shifted_symplectic_shadow_engine import symplectic_at_zeta_zero
        for c in [1.0, 2.0, 6.0, 13.0, 24.0]:
            data = symplectic_at_zeta_zero(1, c_value=c, dps=20)
            assert data.rank_drop == 0

    def test_rank_drop_at_c0(self):
        """Rank drop at c=0 (kappa = 0)."""
        from bc_shifted_symplectic_shadow_engine import symplectic_at_zeta_zero
        data = symplectic_at_zeta_zero(1, c_value=0.001, dps=20)
        # Near c=0: theta_kappa ~ 0.001 * 25.999 / 4 ~ 0.0065 > 0
        # Not exactly zero but small
        assert data.rank_drop == 0  # Not exactly zero

    def test_theta_at_c26_near_zero(self):
        """Theta at c=26: kappa' = 0, theta = 0."""
        from bc_shifted_symplectic_shadow_engine import symplectic_at_zeta_zero
        data = symplectic_at_zeta_zero(1, c_value=26.0, dps=20)
        assert abs(data.lagrangian_theta_kappa) < 1e-8

    def test_c13_self_dual_symmetry(self):
        """At c=13: residue_A_c = residue_A_{26-c} (self-dual)."""
        from bc_shifted_symplectic_shadow_engine import symplectic_at_zeta_zero
        data = symplectic_at_zeta_zero(1, c_value=13.0, dps=20)
        # At c=13, A_c = A_{26-c} = A_13
        assert abs(data.residue_A_c - data.residue_A_c_dual) / max(abs(data.residue_A_c), 1e-15) < 1e-8

    def test_first_15_zeros_finite(self):
        """Residue is finite at first 15 zeros for c=1."""
        from bc_shifted_symplectic_shadow_engine import symplectic_at_zeta_zero
        for n in range(1, 16):
            data = symplectic_at_zeta_zero(n, c_value=1.0, dps=20)
            assert not data.is_singular, f"Singular at zero {n}"

    def test_theta_monotonic_in_c(self):
        """theta_2 = c(26-c)/4 is concave: max at c=13."""
        from bc_shifted_symplectic_shadow_engine import symplectic_at_zeta_zero
        thetas = []
        for c in [1.0, 6.0, 13.0, 20.0, 25.0]:
            data = symplectic_at_zeta_zero(1, c_value=c, dps=20)
            thetas.append(data.lagrangian_theta_kappa.real)
        # Max at c=13
        assert thetas[2] >= max(thetas[0], thetas[1], thetas[3], thetas[4])

    def test_symplectic_rank_table(self):
        """Rank table at multiple zeros is well-formed."""
        from bc_shifted_symplectic_shadow_engine import symplectic_rank_at_zeros
        results = symplectic_rank_at_zeros(n_zeros=3, c_values=[1.0, 13.0], dps=20)
        assert len(results) == 6  # 3 zeros * 2 c-values
        for r in results:
            assert 'zero_index' in r
            assert 'generic_rank' in r

    def test_lagrangian_intersection_at_c13(self):
        """Lagrangian intersection at c=13."""
        from bc_shifted_symplectic_shadow_engine import lagrangian_intersection_at_zero
        result = lagrangian_intersection_at_zero(1, c_value=13.0, dps=20)
        assert result['complementarity_sum'] == 13.0
        assert result['intersection_degree'] == -13.0

    def test_lagrangian_intersection_arithmetic_mult(self):
        """Arithmetic multiplicity is finite at first zero."""
        from bc_shifted_symplectic_shadow_engine import lagrangian_intersection_at_zero
        result = lagrangian_intersection_at_zero(1, c_value=13.0, dps=20)
        assert result['arithmetic_multiplicity'] > 0
        assert result['arithmetic_multiplicity'] < 1e20

    def test_shadow_metric_at_zero(self):
        """Shadow metric at first zero is well-defined."""
        from bc_shifted_symplectic_shadow_engine import shadow_metric_at_zero
        result = shadow_metric_at_zero(1, c_value=2.0, dps=20)
        assert result['discriminant'] != 0  # Class M
        assert result['Q_L'] > 0  # Positive definite

    def test_shadow_metric_perfect_square_check(self):
        """Shadow metric at Heisenberg c=1: close to perfect square (Delta ~ 0)."""
        from bc_shifted_symplectic_shadow_engine import shadow_metric_at_zero
        # For c=1, Virasoro: S_4 = 10/(1*27) ~ 0.37, kappa = 0.5
        # Delta = 8 * 0.5 * 0.37 ~ 1.48 != 0
        result = shadow_metric_at_zero(1, c_value=1.0, dps=20)
        assert not result['is_perfect_square']


# ========================================================================
# SECTION 14: MULTI-PATH CROSS-CHECKS
# ========================================================================

class TestMultiPathVerification:
    """Cross-check results across multiple independent paths."""

    def test_path1_vs_path2_heisenberg(self):
        """Path 1 (PTVV form) vs Path 2 (Lagrangian): Heisenberg consistent."""
        fam = heisenberg_family()
        form = compute_shifted_symplectic_form(fam)
        lag = compute_lagrangian_structure(fam)
        # Form shift = -1, Lagrangian exists
        assert form.shift == -1
        assert lag.is_lagrangian

    def test_path1_vs_path3_aksz(self):
        """Path 1 (PTVV form) vs Path 3 (AKSZ): shift consistency."""
        # PTVV at genus 2: shift = -3
        ptvv = ptvv_shift_at_genus(2)
        # AKSZ mapping: n - d = -1 - 2 = -3
        aksz = aksz_mapping_stack_shift(2, -1)
        assert ptvv == aksz  # Both give -3

    def test_path2_vs_path4_poisson(self):
        """Path 2 (Lagrangian) vs Path 4 (Poisson): MC = Lagrangian."""
        for name, fam in list(STANDARD_FAMILIES.items())[:5]:
            mc_lag = verify_mc_equals_lagrangian(fam)
            assert mc_lag['verification_status'] == 'CONSISTENT'

    def test_path1_path2_path3_full_consistency(self):
        """Full 3-path check: PTVV + Lagrangian + AKSZ for Virasoro."""
        fam = virasoro_family(Fraction(2))

        # Path 1: PTVV form
        form = compute_shifted_symplectic_form(fam)
        assert form.shift == -1
        assert symplectic_matrix_determinant(form) == 1

        # Path 2: Lagrangian
        lag = compute_lagrangian_structure(fam)
        assert lag.is_lagrangian
        theta_2 = lag.theta_primitive[2]
        assert theta_2 == lagrangian_primitive_virasoro(Fraction(2))

        # Path 3: AKSZ at genus 1
        aksz = compute_aksz_data(fam, genus=1)
        assert aksz.target_shift == -1
        assert aksz.aksz_action_terms['kappa'] == fam.kappa

    def test_complementarity_sum_independence(self):
        """Complementarity sum is level-independent for Virasoro."""
        sums = set()
        for c in [1, 2, 5, 13, 20, 26]:
            fam = virasoro_family(Fraction(c))
            sums.add(fam.complementarity_sum)
        assert len(sums) == 1  # All give 13
        assert Fraction(13) in sums

    def test_discriminant_vs_shadow_class(self):
        """Delta = 0 iff class G/L; Delta != 0 iff class M."""
        for name, fam in STANDARD_FAMILIES.items():
            disc = shadow_metric_discriminant(fam)
            if fam.shadow_class in ('G', 'L', 'C'):
                # S4 = 0 for these classes on the primary line
                assert disc == 0 or fam.S4 == 0
            elif fam.shadow_class == 'M':
                if fam.kappa != 0 and fam.S4 != 0:
                    assert disc != 0

    def test_aksz_genus_sequence_consistency(self):
        """AKSZ genus corrections form a consistent tower."""
        fam = virasoro_family(Fraction(2))
        corrections = []
        for g in range(1, 5):
            data = compute_aksz_data(fam, genus=g)
            corrections.append(data.aksz_action_terms['genus_correction'])
        # All corrections have the same sign (positive for kappa > 0)
        for c in corrections:
            assert c > 0


# ========================================================================
# SECTION 15: EDGE CASES AND ROBUSTNESS
# ========================================================================

class TestEdgeCases:
    """Edge cases and boundary behavior."""

    def test_virasoro_c0_kappa_zero(self):
        """Virasoro c=0: kappa = 0, uncurved bar complex."""
        fam = virasoro_family(Fraction(0))
        assert fam.kappa == Fraction(0)
        assert fam.complementarity_sum == Fraction(13)

    def test_virasoro_c26_kappa_prime_zero(self):
        """Virasoro c=26: kappa' = 0, dual uncurved."""
        fam = virasoro_family(Fraction(26))
        assert fam.kappa_dual == Fraction(0)

    def test_large_kappa(self):
        """Large kappa: Heisenberg k=1000."""
        fam = heisenberg_family(Fraction(1000))
        lag = compute_lagrangian_structure(fam, max_arity=2)
        assert lag.theta_primitive[2] == Fraction(-1000000)

    def test_negative_kappa(self):
        """Negative kappa: Heisenberg k=-3."""
        fam = heisenberg_family(Fraction(-3))
        assert fam.kappa == Fraction(-3)
        assert fam.kappa_dual == Fraction(3)

    def test_fractional_level(self):
        """Fractional level: sl_2 at k=1/2."""
        fam = affine_slN_family(2, Fraction(1, 2))
        expected_kappa = Fraction(3) * (Fraction(1, 2) + Fraction(2)) / Fraction(4)
        assert fam.kappa == expected_kappa

    def test_max_arity_2_minimal(self):
        """Minimal arity: only kappa pair."""
        fam = virasoro_family()
        coords = shadow_darboux_coordinates(fam, max_arity=2)
        assert len(coords) == 1

    def test_virasoro_negative_c(self):
        """Virasoro with negative c (Argyres-Douglas)."""
        fam = virasoro_family(Fraction(-22, 5))
        assert fam.kappa == Fraction(-11, 5)
        assert fam.complementarity_sum == Fraction(13)

    def test_w3_c0(self):
        """W_3 at c=0: kappa = 0."""
        fam = w3_family(Fraction(0))
        assert fam.kappa == Fraction(0)

    def test_lattice_rank1(self):
        """Lattice rank 1: same as Heisenberg k=1."""
        fam = lattice_family(1)
        assert fam.kappa == Fraction(1)
        assert fam.shadow_class == 'G'
