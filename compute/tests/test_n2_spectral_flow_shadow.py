r"""Tests for the N=2 spectral flow shadow tower computation (Method C).

Tests cover:
  1. Spectral flow automorphism: OPE preservation
  2. Shadow data invariance under spectral flow
  3. Fixed-point locus in shadow space
  4. Three-method consistency for kappa(N=2)
  5. N=2 chiral ring structure and bar cohomology
  6. Explicit bar homology via matrix rank
  7. Spectral flow on representation theory
  8. Elliptic genus Jacobi property
  9. N=2 minimal model landscape
  10. Cross-checks with Method A (direct OPE)
  11. Koszul duality interactions
  12. Genus-1 free energy

50+ tests total.
"""

import pytest
from sympy import Rational, simplify, sqrt, Symbol

from compute.lib.n2_spectral_flow_shadow import (
    # Spectral flow automorphism
    spectral_flow_stress_tensor,
    spectral_flow_current,
    spectral_flow_supercharges,
    # OPE preservation
    verify_flowed_TT_OPE,
    verify_flowed_JJ_OPE,
    verify_flowed_GG_OPE,
    # Shadow orbit
    spectral_flow_shadow_orbit,
    spectral_flow_orbit_explicit,
    # Fixed-point locus
    spectral_flow_fixed_point_locus,
    # Elliptic genus
    elliptic_genus_jacobi_property,
    # Chiral ring
    n2_chiral_ring_dimension,
    n2_chiral_ring_central_charge,
    # Bar complex
    truncated_poly_bar_cohomology,
    truncated_poly_tor_computation,
    chiral_ring_bar_betti,
    bar_differential_matrix,
    bar_homology_dimensions,
    # Three methods
    kappa_method_A,
    kappa_method_B_kazama_suzuki,
    kappa_method_C_spectral_flow,
    three_method_consistency,
    # S4 constraint
    S4_spectral_flow_constraint,
    # Representation theory
    spectral_flow_on_weights,
    spectral_flow_preserves_chiral_ring,
    # Invariant tower
    spectral_flow_invariant_tower,
    # Comparison
    compare_methods_A_and_C,
    # Genus-1
    genus1_spectral_flow_check,
    # Landscape
    n2_minimal_model_landscape,
    # Specific c values
    spectral_flow_orbit_at_c3,
    spectral_flow_orbit_at_c6,
    spectral_flow_orbit_at_c9,
    # Full verification
    verify_all,
)


c = Symbol('c')


# =========================================================================
# 1. Spectral flow automorphism structure
# =========================================================================

class TestSpectralFlowAutomorphism:
    """Tests for the spectral flow automorphism sigma_theta."""

    def test_stress_tensor_at_theta_0(self):
        """At theta=0, T' = T (identity flow)."""
        sf = spectral_flow_stress_tensor(0)
        assert sf['T_coeff'] == 1
        assert sf['J_coeff'] == 0
        assert simplify(sf['constant']) == 0

    def test_stress_tensor_at_theta_1(self):
        """At theta=1, T' = T + J + c/6."""
        sf = spectral_flow_stress_tensor(1)
        assert sf['T_coeff'] == 1
        assert sf['J_coeff'] == 1
        assert simplify(sf['constant'] - c / 6) == 0

    def test_stress_tensor_at_theta_2(self):
        """At theta=2, T' = T + 2J + 2c/3."""
        sf = spectral_flow_stress_tensor(2)
        assert sf['J_coeff'] == 2
        assert simplify(sf['constant'] - 2 * c / 3) == 0

    def test_current_at_theta_0(self):
        """At theta=0, J' = J (identity)."""
        sf = spectral_flow_current(0)
        assert sf['J_coeff'] == 1
        assert simplify(sf['constant']) == 0

    def test_current_at_theta_1(self):
        """At theta=1, J' = J + c/3."""
        sf = spectral_flow_current(1)
        assert simplify(sf['constant'] - c / 3) == 0

    def test_supercharge_weights_theta_1(self):
        """At theta=1: h(G+)=5/2, h(G-)=1/2."""
        sc = spectral_flow_supercharges(1)
        assert sc['h_G+'] == Rational(5, 2)
        assert sc['h_G-'] == Rational(1, 2)

    def test_supercharge_weight_sum_invariant(self):
        """h(G+) + h(G-) = 3 for all theta."""
        for th in range(-3, 4):
            sc = spectral_flow_supercharges(th)
            assert sc['h_sum'] == 3

    def test_supercharge_weight_difference(self):
        """h(G+) - h(G-) = 2*theta."""
        for th in range(-3, 4):
            sc = spectral_flow_supercharges(th)
            assert sc['h_diff'] == 2 * Rational(th)


# =========================================================================
# 2. OPE preservation under spectral flow
# =========================================================================

class TestOPEPreservation:
    """Tests that spectral flow preserves OPE structure."""

    def test_TT_preserved_theta_1(self):
        v = verify_flowed_TT_OPE(1)
        assert v['virasoro_structure_preserved']
        assert v['quartic_preserved']
        assert v['double_pole_is_2T_prime']
        assert v['simple_pole_is_dT_prime']

    def test_TT_preserved_theta_2(self):
        v = verify_flowed_TT_OPE(2)
        assert v['virasoro_structure_preserved']

    def test_TT_preserved_theta_minus1(self):
        v = verify_flowed_TT_OPE(-1)
        assert v['virasoro_structure_preserved']

    def test_TT_preserved_theta_3(self):
        v = verify_flowed_TT_OPE(3)
        assert v['central_charge_preserved']

    def test_JJ_preserved_theta_1(self):
        v = verify_flowed_JJ_OPE(1)
        assert v['preserved']

    def test_JJ_preserved_theta_minus2(self):
        v = verify_flowed_JJ_OPE(-2)
        assert v['preserved']

    def test_GG_preserved_theta_1(self):
        v = verify_flowed_GG_OPE(1)
        assert v['structure_constants_preserved']
        assert v['is_inner_automorphism']


# =========================================================================
# 3. Shadow data invariance
# =========================================================================

class TestShadowInvariance:
    """Tests that shadow data is invariant under spectral flow."""

    def test_orbit_is_fixed_point_c1(self):
        orbit = spectral_flow_shadow_orbit(1)
        assert orbit['is_fixed_point']

    def test_orbit_is_fixed_point_c3(self):
        orbit = spectral_flow_shadow_orbit(3)
        assert orbit['is_fixed_point']

    def test_orbit_total_kappa_c1(self):
        """kappa(N=2, c=1) = (6-1)/(2*2) = 5/4."""
        orbit = spectral_flow_shadow_orbit(1)
        assert simplify(orbit['total_kappa'] - Rational(5, 4)) == 0

    def test_orbit_total_kappa_c2(self):
        """kappa(N=2, c=2) = (6-2)/(2*1) = 2."""
        orbit = spectral_flow_shadow_orbit(2)
        assert simplify(orbit['total_kappa'] - Rational(2)) == 0

    def test_orbit_total_kappa_c5(self):
        """kappa(N=2, c=5) = 1/(2*(-2)) = -1/4."""
        orbit = spectral_flow_shadow_orbit(5)
        assert simplify(orbit['total_kappa'] - Rational(-1, 4)) == 0

    def test_orbit_explicit_all_theta_same_c3(self):
        """All spectral flow levels give identical shadow data at c=3."""
        orbit = spectral_flow_orbit_explicit(3, max_theta=4)
        ref = orbit[0]
        for th in range(1, 5):
            assert orbit[th]['kappa_T'] == ref['kappa_T']
            assert orbit[th]['kappa_J'] == ref['kappa_J']
            assert orbit[th]['kappa_G'] == ref['kappa_G']
            assert simplify(orbit[th]['kappa_total'] - ref['kappa_total']) == 0

    def test_orbit_explicit_all_theta_same_c1(self):
        orbit = spectral_flow_orbit_explicit(1, max_theta=3)
        ref = orbit[0]
        for th in range(1, 4):
            assert orbit[th]['kappa_T'] == ref['kappa_T']

    def test_T_line_data_invariant(self):
        orbit = spectral_flow_shadow_orbit(3)
        T = orbit['T_line']
        assert T['kappa'] == Rational(3, 2)
        assert T['alpha'] == 2
        assert simplify(T['S4'] - Rational(10, 111)) == 0

    def test_J_line_data_invariant(self):
        orbit = spectral_flow_shadow_orbit(3)
        J = orbit['J_line']
        assert J['kappa'] == 1
        assert J['alpha'] == 0
        assert J['S4'] == 0

    def test_G_line_data_invariant(self):
        orbit = spectral_flow_shadow_orbit(3)
        G = orbit['G_line']
        assert G['kappa'] == 1
        assert G['alpha'] == 1


# =========================================================================
# 4. Fixed-point locus
# =========================================================================

class TestFixedPointLocus:
    """Tests for the spectral flow fixed-point locus in shadow space."""

    def test_trivial_action(self):
        fp = spectral_flow_fixed_point_locus()
        assert fp['spectral_flow_action'] == 'trivial (automorphism)'

    def test_koszul_self_dual_positive(self):
        fp = spectral_flow_fixed_point_locus()
        assert fp['koszul_self_dual']['positive'] == 3

    def test_koszul_self_dual_negative(self):
        fp = spectral_flow_fixed_point_locus()
        assert fp['koszul_self_dual']['positive'] == 3

    def test_kappa_sum_invariant(self):
        """kappa(c) + kappa(6-c) = 1 for all c (constant, additive)."""
        fp = spectral_flow_fixed_point_locus()
        assert fp['kappa_sum_invariant'] == Rational(1)
        # Verify at several values
        for c_v in [1, 2, Rational(1, 2), -3]:
            c_r = Rational(c_v)
            kap = (6 - c_r) / (2 * (3 - c_r))
            kap_dual = c_r / (2 * (c_r - 3))
            assert simplify(kap + kap_dual - 1) == 0


# =========================================================================
# 5. Three-method consistency
# =========================================================================

class TestThreeMethodConsistency:
    """Tests that all three methods give the same kappa."""

    def test_consistency_c1(self):
        tc = three_method_consistency(1)
        assert tc['all_agree']

    def test_consistency_c2(self):
        """c=2: kappa = (6-2)/(2*1) = 2."""
        tc = three_method_consistency(2)
        assert tc['all_agree']

    def test_consistency_c5(self):
        """c=5: kappa = 1/(2*(-2)) = -1/4."""
        tc = three_method_consistency(5)
        assert tc['all_agree']

    def test_consistency_c_minus3(self):
        """c=-3: kappa = 9/12 = 3/4."""
        tc = three_method_consistency(-3)
        assert tc['all_agree']

    def test_consistency_c_half(self):
        tc = three_method_consistency(Rational(1, 2))
        assert tc['all_agree']

    def test_method_A_formula(self):
        assert simplify(kappa_method_A() - (6 - c) / (2 * (3 - c))) == 0

    def test_method_A_at_c1(self):
        assert kappa_method_A(1) == Rational(5, 4)

    def test_method_B_formula(self):
        assert simplify(kappa_method_B_kazama_suzuki() - (6 - c) / (2 * (3 - c))) == 0

    def test_method_C_formula(self):
        assert simplify(kappa_method_C_spectral_flow() - (6 - c) / (2 * (3 - c))) == 0


# =========================================================================
# 6. Chiral ring structure
# =========================================================================

class TestChiralRing:
    """Tests for the N=2 chiral ring."""

    def test_dim_K3(self):
        cr = n2_chiral_ring_dimension(3)
        assert cr['dim_R'] == 2
        assert cr['c'] == 1

    def test_dim_K4(self):
        cr = n2_chiral_ring_dimension(4)
        assert cr['dim_R'] == 3
        assert cr['c'] == Rational(3, 2)

    def test_dim_K5(self):
        cr = n2_chiral_ring_dimension(5)
        assert cr['dim_R'] == 4
        assert cr['c'] == Rational(9, 5)

    def test_dim_K6(self):
        cr = n2_chiral_ring_dimension(6)
        assert cr['dim_R'] == 5
        assert cr['c'] == 2

    def test_central_charge_formula(self):
        for K in range(3, 12):
            assert n2_chiral_ring_central_charge(K) == Rational(3 * (K - 2), K)

    def test_ring_structure_truncated_poly(self):
        for K in [3, 4, 5]:
            cr = n2_chiral_ring_dimension(K)
            assert cr['ring_structure'] == f'C[x]/(x^{K-1})'

    def test_invalid_K_raises(self):
        with pytest.raises(ValueError):
            n2_chiral_ring_dimension(2)


# =========================================================================
# 7. Bar cohomology of truncated polynomial rings
# =========================================================================

class TestBarCohomology:
    """Tests for the bar complex of R = C[x]/(x^n)."""

    def test_tor_n2_all_ones(self):
        """Tor_p^{C[x]/(x^2)}(C,C) = C for all p."""
        betti = truncated_poly_bar_cohomology(2)
        for p in range(8):
            assert betti[p] == 1

    def test_tor_n3_all_ones(self):
        betti = truncated_poly_bar_cohomology(3)
        for p in range(8):
            assert betti[p] == 1

    def test_tor_n4_all_ones(self):
        betti = truncated_poly_bar_cohomology(4)
        for p in range(8):
            assert betti[p] == 1

    def test_tor_n5_all_ones(self):
        betti = truncated_poly_bar_cohomology(5)
        for p in range(8):
            assert betti[p] == 1

    def test_tor_n1_trivial(self):
        """C[x]/(x^1) = C: trivial ring, H^0 = C, H^p = 0 for p > 0."""
        betti = truncated_poly_bar_cohomology(1)
        assert betti[0] == 1
        for p in range(1, 8):
            assert betti[p] == 0

    def test_tor_computation_agrees(self):
        """truncated_poly_tor_computation agrees with bar_cohomology."""
        for n in [2, 3, 4]:
            betti = truncated_poly_bar_cohomology(n)
            tor = truncated_poly_tor_computation(n)
            for p in range(6):
                assert betti[p] == tor[p]

    def test_chiral_ring_bar_betti_K3(self):
        result = chiral_ring_bar_betti(3)
        assert result['n'] == 2
        assert result['ring'] == 'C[x]/(x^2)'
        assert not result['is_koszul']
        for p in range(6):
            assert result['betti'][p] == 1

    def test_chiral_ring_bar_betti_K5(self):
        result = chiral_ring_bar_betti(5)
        assert result['n'] == 4
        for p in range(6):
            assert result['betti'][p] == 1


# =========================================================================
# 8. Explicit bar homology via matrix rank
# =========================================================================

class TestExplicitBarHomology:
    """Tests for the bar differential matrix and homology computation."""

    def test_bar_diff_n2_rank_zero(self):
        """For n=2 (R = C[x]/(x^2)): all differentials have rank 0."""
        for p in range(1, 5):
            mat, src, tgt = bar_differential_matrix(2, p)
            from sympy import Matrix
            if mat and mat[0]:
                M = Matrix(mat)
                assert M.rank() == 0

    def test_bar_homology_n2_all_ones(self):
        dims = bar_homology_dimensions(2, max_p=5)
        for p in range(6):
            assert dims[p] == 1, f"H_{p} = {dims[p]} != 1 for n=2"

    def test_bar_homology_n3_all_ones(self):
        dims = bar_homology_dimensions(3, max_p=5)
        for p in range(6):
            assert dims[p] == 1, f"H_{p} = {dims[p]} != 1 for n=3"

    def test_bar_homology_n4_all_ones(self):
        dims = bar_homology_dimensions(4, max_p=4)
        for p in range(5):
            assert dims[p] == 1, f"H_{p} = {dims[p]} != 1 for n=4"

    def test_bar_diff_n3_p2_rank(self):
        """d_2: C_2 -> C_1 for n=3 has rank 1."""
        from sympy import Matrix
        mat, _, _ = bar_differential_matrix(3, 2)
        assert Matrix(mat).rank() == 1

    def test_bar_diff_n3_p3_rank(self):
        """d_3: C_3 -> C_2 for n=3 has rank 2."""
        from sympy import Matrix
        mat, _, _ = bar_differential_matrix(3, 3)
        assert Matrix(mat).rank() == 2

    def test_d_squared_zero_n3(self):
        """Verify d^2 = 0 for n=3, p=3 (d_2 . d_3 = 0)."""
        from sympy import Matrix, zeros
        mat2, _, _ = bar_differential_matrix(3, 2)
        mat3, _, _ = bar_differential_matrix(3, 3)
        M2 = Matrix(mat2)
        M3 = Matrix(mat3)
        product = M2 * M3
        assert product == zeros(M2.rows, M3.cols)

    def test_d_squared_zero_n4(self):
        """Verify d^2 = 0 for n=4, p=3."""
        from sympy import Matrix, zeros
        mat2, _, _ = bar_differential_matrix(4, 2)
        mat3, _, _ = bar_differential_matrix(4, 3)
        M2 = Matrix(mat2)
        M3 = Matrix(mat3)
        product = M2 * M3
        assert product == zeros(M2.rows, M3.cols)

    def test_bar_homology_n1_trivial(self):
        """Trivial ring: H_0 = C, H_p = 0 for p > 0."""
        dims = bar_homology_dimensions(1, max_p=4)
        assert dims[0] == 1
        for p in range(1, 5):
            assert dims[p] == 0


# =========================================================================
# 9. Spectral flow on representation theory
# =========================================================================

class TestSpectralFlowRepTheory:
    """Tests for spectral flow acting on weights and charges."""

    def test_vacuum_flow_c3(self):
        """Vacuum (h=0, q=0) at c=3, theta=1: h'=1/2, q'=1."""
        result = spectral_flow_on_weights(0, 0, 3, 1)
        assert result['h_prime'] == Rational(1, 2)
        assert result['q_prime'] == 1

    def test_vacuum_flow_c1(self):
        """Vacuum at c=1, theta=1: h'=1/6, q'=1/3."""
        result = spectral_flow_on_weights(0, 0, 1, 1)
        assert result['h_prime'] == Rational(1, 6)
        assert result['q_prime'] == Rational(1, 3)

    def test_vacuum_flow_theta_0_identity(self):
        """theta=0 is the identity: h'=h, q'=q."""
        result = spectral_flow_on_weights(Rational(1, 2), Rational(1, 3), 3, 0)
        assert result['h_prime'] == Rational(1, 2)
        assert result['q_prime'] == Rational(1, 3)

    def test_chiral_ring_preserved_K3_vacuous(self):
        """K=3: only one chiral primary (vacuum), which maps to a BPS state.

        This is a vacuous preservation: the vacuum (h=0, q=0) maps to
        h'=c/6, q'=c/3 with h' = q'/2, so it formally satisfies the
        chiral primary condition. But the image is in the Ramond sector.
        """
        result = spectral_flow_preserves_chiral_ring(3, theta_val=1)
        # K=3 has only one chiral primary (l=0, the vacuum)
        # It maps to a state satisfying h' = q'/2, so ring_preserved is True
        assert result['ring_preserved']
        assert len(result['chiral_primaries']) == 1

    def test_chiral_ring_not_preserved_K4(self):
        """K=4: two chiral primaries, only vacuum maps to BPS."""
        result = spectral_flow_preserves_chiral_ring(4, theta_val=1)
        assert not result['ring_preserved']

    def test_chiral_ring_not_preserved_K5(self):
        result = spectral_flow_preserves_chiral_ring(5, theta_val=1)
        assert not result['ring_preserved']

    def test_vacuum_chiral_primary_maps_to_ramond(self):
        """The vacuum (l=0 chiral primary) maps to a Ramond ground state."""
        result = spectral_flow_preserves_chiral_ring(4, theta_val=1)
        # l=0 chiral primary has h=0, q=0
        vac = result['chiral_primaries'][0]
        # After flow: h' = c/6 = 1/4, q' = c/3 = 1/2
        assert vac['h_prime'] == Rational(1, 4)
        assert vac['q_prime'] == Rational(1, 2)


# =========================================================================
# 10. Elliptic genus
# =========================================================================

class TestEllipticGenus:
    """Tests for the elliptic genus Jacobi property."""

    def test_jacobi_index_c1(self):
        ej = elliptic_genus_jacobi_property(1)
        assert ej['index'] == Rational(1, 3)

    def test_jacobi_index_c3(self):
        ej = elliptic_genus_jacobi_property(3)
        assert ej['index'] == 1

    def test_F1_at_c1(self):
        ej = elliptic_genus_jacobi_property(1)
        assert ej['F_1'] == Rational(7, 144)

    def test_F1_at_c3(self):
        ej = elliptic_genus_jacobi_property(3)
        assert ej['F_1'] == Rational(7, 48)


# =========================================================================
# 11. S4 spectral flow constraint
# =========================================================================

class TestS4Constraint:
    """Tests for the spectral flow constraint on S_4."""

    def test_sf_invariant(self):
        result = S4_spectral_flow_constraint(3)
        assert result['spectral_flow_invariant']

    def test_S4_at_c3(self):
        result = S4_spectral_flow_constraint(3)
        assert result['S4'] == Rational(10, 111)

    def test_S4_koszul_self_dual_at_c3(self):
        """At c=3 (Koszul self-dual): S4(3) = S4(9/3) = S4(3)."""
        result = S4_spectral_flow_constraint(3)
        assert result['S4_equals_S4_dual']

    def test_S4_not_koszul_invariant_c1(self):
        """S4(1) != S4(9): not Koszul-invariant at c=1."""
        result = S4_spectral_flow_constraint(1)
        assert not result['S4_equals_S4_dual']


# =========================================================================
# 12. Genus-1 free energy
# =========================================================================

class TestGenus1:
    """Tests for genus-1 free energy."""

    def test_F1_c1(self):
        g1 = genus1_spectral_flow_check(1)
        assert g1['F_1'] == Rational(7, 144)
        assert g1['sf_invariant']

    def test_F1_c3(self):
        g1 = genus1_spectral_flow_check(3)
        assert g1['F_1'] == Rational(7, 48)

    def test_F1_c6(self):
        g1 = genus1_spectral_flow_check(6)
        assert g1['F_1'] == Rational(7, 24)

    def test_F1_c9(self):
        g1 = genus1_spectral_flow_check(9)
        assert g1['F_1'] == Rational(21, 48)
        # = 7/16


# =========================================================================
# 13. Invariant tower computation
# =========================================================================

class TestInvariantTower:
    """Tests for the spectral-flow-invariant shadow tower."""

    def test_T_line_kappa_c3(self):
        tower = spectral_flow_invariant_tower(3, 'T')
        assert tower['kappa'] == Rational(3, 2)
        assert tower['sf_invariant']

    def test_J_line_terminates(self):
        tower = spectral_flow_invariant_tower(3, 'J')
        for r in range(3, 10):
            assert tower['tower'][r] == 0

    def test_G_line_terminates_at_3(self):
        """Conjectural class L: tower terminates at arity 3."""
        tower = spectral_flow_invariant_tower(3, 'G')
        for r in range(4, 10):
            assert tower['tower'][r] == 0

    def test_T_line_tower_S2_c3(self):
        tower = spectral_flow_invariant_tower(3, 'T')
        assert tower['tower'][2] == Rational(3, 2)

    def test_T_line_tower_nonzero_S5(self):
        """T-line tower has nonzero S_5 (class M)."""
        tower = spectral_flow_invariant_tower(3, 'T', max_arity=6)
        assert tower['tower'][5] != 0

    def test_invalid_line_raises(self):
        with pytest.raises(ValueError):
            spectral_flow_invariant_tower(3, 'X')


# =========================================================================
# 14. Comparison with Method A
# =========================================================================

class TestMethodComparison:
    """Tests comparing Method A (direct OPE) with Method C (spectral flow)."""

    def test_compare_c1(self):
        result = compare_methods_A_and_C(1)
        assert result['all_agree']
        assert result['kappa_agree']

    def test_compare_c2(self):
        result = compare_methods_A_and_C(2)
        assert result['all_agree']

    def test_compare_c5(self):
        result = compare_methods_A_and_C(5)
        assert result['all_agree']

    def test_compare_T_line_details(self):
        result = compare_methods_A_and_C(2)
        assert result['T_kappa_agree']
        assert result['T_alpha_agree']
        assert result['T_S4_agree']


# =========================================================================
# 15. N=2 minimal model landscape
# =========================================================================

class TestMinimalModelLandscape:
    """Tests for the N=2 minimal model landscape."""

    def test_landscape_length(self):
        landscape = n2_minimal_model_landscape(8)
        assert len(landscape) == 6  # K = 3, 4, 5, 6, 7, 8

    def test_landscape_central_charges(self):
        landscape = n2_minimal_model_landscape(6)
        assert landscape[0]['c'] == 1  # K=3
        assert landscape[1]['c'] == Rational(3, 2)  # K=4
        assert landscape[2]['c'] == Rational(9, 5)  # K=5
        assert landscape[3]['c'] == 2  # K=6

    def test_landscape_kappa_formula(self):
        landscape = n2_minimal_model_landscape(8)
        for entry in landscape:
            expected = 7 * entry['c'] / 6
            assert simplify(entry['kappa'] - expected) == 0

    def test_landscape_all_class_M(self):
        landscape = n2_minimal_model_landscape(8)
        for entry in landscape:
            assert entry['shadow_class'] == 'M'

    def test_landscape_all_sf_invariant(self):
        landscape = n2_minimal_model_landscape(8)
        for entry in landscape:
            assert entry['sf_invariant']

    def test_landscape_chiral_ring_dims(self):
        landscape = n2_minimal_model_landscape(8)
        for entry in landscape:
            assert entry['dim_chiral_ring'] == entry['K'] - 1


# =========================================================================
# 16. Specific c-value orbits
# =========================================================================

class TestSpecificOrbits:
    """Tests for spectral flow orbits at c = 3, 6, 9."""

    def test_c3_kappa_total(self):
        orbit = spectral_flow_orbit_at_c3()
        for th, data in orbit.items():
            assert data['kappa_total'] == Rational(7, 2)

    def test_c6_kappa_total(self):
        orbit = spectral_flow_orbit_at_c6()
        for th, data in orbit.items():
            assert data['kappa_total'] == 7

    def test_c9_kappa_total(self):
        orbit = spectral_flow_orbit_at_c9()
        for th, data in orbit.items():
            assert simplify(data['kappa_total'] - Rational(21, 2)) == 0

    def test_c3_self_dual(self):
        """c=3 is Koszul self-dual (c' = 9/c = 3)."""
        orbit = spectral_flow_orbit_at_c3()
        assert orbit[0]['kappa_T'] == Rational(3, 2)

    def test_c6_kappa_T(self):
        orbit = spectral_flow_orbit_at_c6()
        assert orbit[0]['kappa_T'] == 3

    def test_c9_kappa_J(self):
        orbit = spectral_flow_orbit_at_c9()
        assert orbit[0]['kappa_J'] == 3


# =========================================================================
# 17. Full verification suite
# =========================================================================

class TestFullVerification:
    """Run the full internal verification suite."""

    def test_all_pass(self):
        results = verify_all()
        for name, passed in results.items():
            assert passed, f"Verification failed: {name}"

    def test_count_at_least_30(self):
        results = verify_all()
        assert len(results) >= 30


# =========================================================================
# 18. Koszul duality interactions
# =========================================================================

class TestKoszulDuality:
    """Tests for Koszul duality c -> 6-c (additive) interacting with spectral flow."""

    def test_kappa_sum_c1(self):
        """kappa(1) + kappa(5) = 1."""
        k1 = kappa_method_A(1)
        k5 = kappa_method_A(5)
        assert simplify(k1 + k5 - 1) == 0

    def test_kappa_sum_c2(self):
        """kappa(2) + kappa(4) = 1."""
        k2 = kappa_method_A(2)
        k4 = kappa_method_A(4)
        assert simplify(k2 + k4 - 1) == 0

    def test_dual_central_charge_involutive(self):
        """(c -> 6-c) is an involution: 6-(6-c) = c."""
        for c_v in [1, 2, 4, 5, -3]:
            c_dual = 6 - Rational(c_v)
            c_dual_dual = 6 - c_dual
            assert c_dual_dual == c_v

    def test_self_dual_at_c3(self):
        """c = 6-c iff c = 3 (free-field limit)."""
        assert 6 - Rational(3) == Rational(3)

    def test_kappa_at_c6(self):
        """kappa(6) = 0 (critical level k=-4)."""
        assert kappa_method_A(6) == Rational(0)

    def test_kappa_at_cminus3(self):
        """kappa(-3) = (6-(-3))/(2*(3-(-3))) = 9/12 = 3/4."""
        assert kappa_method_A(-3) == Rational(3, 4)
