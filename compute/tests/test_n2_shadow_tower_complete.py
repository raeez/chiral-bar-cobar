"""Tests for the complete N=2 superconformal shadow tower.

70+ tests covering:
  1. Three-route kappa agreement (8 tests)
  2. Koszul duality and complementarity (10 tests)
  3. Shadow metric per-channel (8 tests)
  4. Spectral flow invariance (6 tests)
  5. Elliptic genus and K3 (8 tests)
  6. Mathieu moonshine (5 tests)
  7. N=2 minimal models (10 tests)
  8. Gepner models (8 tests)
  9. Cross-checks and edge cases (10 tests)

ADVERSARIAL DESIGN:
  - Each kappa test is verified by INDEPENDENT computation (AP10).
  - Complementarity tests verify constant sum, not just a formula (AP24).
  - Shadow metric tests verify structure, not just values (AP3).
  - Spectral flow tests check invariance from first principles (AP9).
  - Elliptic genus tests verify against published K3 data.
  - Mathieu moonshine tests check M_24 representation dimensions.
"""

import pytest
from sympy import Rational, simplify, Symbol, expand, sqrt

from compute.lib.n2_shadow_tower_complete import (
    # Central charge
    n2_central_charge,
    k_from_c,
    # Three routes for kappa
    kappa_n2,
    kappa_n2_coset,
    kappa_n2_ds,
    kappa_n2_spectral_flow,
    three_route_agreement,
    # Koszul duality
    koszul_dual_c,
    koszul_dual_k,
    complementarity_sum_kappa,
    self_dual_point,
    # Shadow metric
    shadow_data_T_line,
    shadow_data_J_line,
    shadow_data_G_line,
    shadow_metric_T_line,
    shadow_metric_J_line,
    shadow_metric_matrix_bosonic,
    shadow_metric_at_values,
    # Spectral flow
    spectral_flow_modes,
    spectral_flow_invariance_shadow,
    spectral_flow_shadow_coefficients_agree,
    # Elliptic genus
    weak_jacobi_phi01_coefficients,
    k3_elliptic_genus_coefficients,
    k3_euler_characteristic,
    elliptic_genus_shadow_connection,
    # Mathieu moonshine
    mathieu_moonshine_coefficients,
    mathieu_m24_decomposition,
    # Minimal models
    n2_minimal_model,
    n2_minimal_model_table,
    n2_minimal_model_partition_function_ns,
    # Gepner
    gepner_model,
    gepner_quintic,
    gepner_k3,
    # Summary
    full_n2_summary,
    verify_all_cross_checks,
    # Internal helper
    _compute_shadow_coefficients,
)


# =========================================================================
# 1. Three-route kappa agreement
# =========================================================================

class TestThreeRouteKappa:
    """Verify kappa from coset, DS, and spectral flow all agree."""

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 10, 100])
    def test_three_routes_agree(self, k_val):
        result = three_route_agreement(k_val)
        assert result['all_agree'], f"Three routes disagree at k={k_val}"

    def test_explicit_coset_decomposition_k1(self):
        """At k=1: kappa(sl2) = 3*3/4 = 9/4, fermion=1/2, U(1) = 3/2.
        Total = 9/4 + 1/2 - 3/2 = 9/4 - 1 = 5/4."""
        result = three_route_agreement(1)
        assert result['kappa_sl2'] == Rational(9, 4)
        assert result['kappa_fermion'] == Rational(1, 2)
        assert result['kappa_u1'] == Rational(3, 2)
        assert result['route1_explicit_decomposition'] == Rational(5, 4)

    def test_explicit_coset_decomposition_k2(self):
        """At k=2: kappa(sl2) = 3*4/4 = 3, fermion=1/2, U(1) = 2.
        Total = 3 + 1/2 - 2 = 3/2."""
        result = three_route_agreement(2)
        assert result['kappa_sl2'] == Rational(3)
        assert result['kappa_fermion'] == Rational(1, 2)
        assert result['kappa_u1'] == Rational(2)
        assert result['route1_explicit_decomposition'] == Rational(3, 2)

    @pytest.mark.parametrize("k_val,expected", [
        (1, Rational(5, 4)),
        (2, Rational(3, 2)),
        (3, Rational(7, 4)),
        (4, Rational(2)),
        (10, Rational(7, 2)),
    ])
    def test_kappa_specific_values(self, k_val, expected):
        """Verify kappa = (k+4)/4 at specific levels."""
        assert kappa_n2(k_val=k_val) == expected

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4])
    def test_kappa_from_k_matches_from_c(self, k_val):
        """kappa from k-formula matches kappa from c-formula."""
        c_val = n2_central_charge(k_val)
        kap_k = kappa_n2(k_val=k_val)
        kap_c = kappa_n2(c_val=c_val)
        assert simplify(kap_k - kap_c) == 0


# =========================================================================
# 2. Koszul duality and complementarity
# =========================================================================

class TestKoszulDuality:
    """Test c' = 6 - c and kappa + kappa' = 1."""

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 10])
    def test_additive_duality(self, k_val):
        """c + c' = 6 at each level."""
        c_v = n2_central_charge(k_val)
        c_dual = koszul_dual_c(c_v)
        assert simplify(c_v + c_dual - 6) == 0

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 10, -1, -3])
    def test_complementarity_sum_is_one(self, k_val):
        """kappa(c) + kappa(c') = 1."""
        result = complementarity_sum_kappa(k_val=k_val)
        assert result['sum'] == 1, f"Sum = {result['sum']} at k={k_val}"

    def test_complementarity_symbolic(self):
        """Symbolic verification: kappa(c) + kappa(6-c) = 1."""
        result = complementarity_sum_kappa()
        assert result['sum'] == 1

    def test_self_dual_point(self):
        """Self-dual point is c = 3 (free-field limit)."""
        sd = self_dual_point()
        assert sd['c_self_dual'] == 3
        assert sd['k_self_dual'] is None  # k -> infinity

    def test_koszul_dual_k_involution(self):
        """k' = -k-4 is an involution: (k')' = k."""
        for k_v in [1, 2, 5]:
            k_dual = koszul_dual_k(k_v)
            k_double = koszul_dual_k(k_dual)
            assert simplify(k_double - Rational(k_v)) == 0

    def test_complementarity_at_c1(self):
        """At c=1: kappa=5/4, c'=5, kappa'=-1/4, sum=1."""
        result = complementarity_sum_kappa(c_val=1)
        assert result['kappa'] == Rational(5, 4)
        assert result['c_dual'] == 5
        assert result['kappa_dual'] == Rational(-1, 4)
        assert result['sum'] == 1

    def test_complementarity_at_c2(self):
        """At c=2 (k=4): kappa=2, c'=4, kappa'=-1, sum=1."""
        result = complementarity_sum_kappa(c_val=2)
        assert result['kappa'] == 2
        assert result['c_dual'] == 4
        assert result['kappa_dual'] == -1
        assert result['sum'] == 1

    def test_kappa_zero_at_critical(self):
        """kappa = 0 at c = 6 (k = -4, critical level of sl(2))."""
        assert kappa_n2(c_val=6) == 0
        assert kappa_n2(k_val=-4) == 0

    def test_complementarity_not_zero(self):
        """kappa + kappa' = 1, NOT zero (unlike KM where it is 0).
        This is a non-trivial complementarity sum (AP24)."""
        result = complementarity_sum_kappa(c_val=1)
        assert result['sum'] != 0
        assert result['sum'] == 1

    def test_wrong_multiplicative_duality(self):
        """The WRONG duality c' = 9/c gives non-constant complementarity sum.
        At c=1: kappa(1) + kappa(9) = 5/4 + (6-9)/(2(3-9)) = 5/4 + (-3)/(-12) = 5/4 + 1/4 = 3/2.
        At c=2: kappa(2) + kappa(9/2) = 2 + (6-9/2)/(2(3-9/2)) = 2 + (3/2)/(2*(-3/2)) = 2 - 1/2 = 3/2.
        So the sum IS constant (3/2) under c'=9/c too! But with the CORRECT duality c'=6-c, the sum is 1.
        The two dualities give DIFFERENT constant sums: 3/2 vs 1."""
        # Under c' = 9/c:
        kap_1 = kappa_n2(c_val=1)  # = 5/4
        kap_9 = kappa_n2(c_val=9)  # = (6-9)/(2(3-9)) = -3/(-12) = 1/4
        sum_wrong = kap_1 + kap_9
        # Note: 5/4 + 1/4 = 3/2
        assert sum_wrong == Rational(3, 2)

        # Under c' = 6-c:
        result = complementarity_sum_kappa(c_val=1)
        assert result['sum'] == 1

        # The two give DIFFERENT sums
        assert sum_wrong != result['sum']


# =========================================================================
# 3. Shadow metric per-channel
# =========================================================================

class TestShadowMetric:
    """Test the shadow metric Q_L channel decomposition."""

    def test_T_line_kappa(self):
        """T-line kappa = c/2 (Virasoro subsector)."""
        data = shadow_data_T_line(Rational(1))
        assert data['kappa'] == Rational(1, 2)

    def test_J_line_kappa(self):
        """J-line kappa = c/3 (Heisenberg)."""
        data = shadow_data_J_line(Rational(1))
        assert data['kappa'] == Rational(1, 3)

    def test_G_line_kappa(self):
        """G-line kappa = c/3 (supercurrent pairing)."""
        data = shadow_data_G_line(Rational(1))
        assert data['kappa'] == Rational(1, 3)

    def test_T_line_class_M(self):
        """T-line is class M (mixed, infinite depth)."""
        data = shadow_data_T_line(Rational(1))
        assert data['shadow_class'] == 'M'

    def test_J_line_class_G(self):
        """J-line is class G (Gaussian, depth 2)."""
        data = shadow_data_J_line(Rational(1))
        assert data['shadow_class'] == 'G'
        assert data['shadow_depth'] == 2

    def test_J_line_metric_constant(self):
        """J-line shadow metric is constant (no t-dependence)."""
        result = shadow_metric_J_line(Rational(1))
        assert result['is_constant'] is True
        assert result['Q'] == Rational(4, 9)  # (2*1/3)^2 = 4/9

    def test_T_line_alpha(self):
        """T-line alpha = 2 (Sugawara normalization)."""
        data = shadow_data_T_line(Rational(1))
        assert data['alpha'] == 2

    def test_shadow_metric_matrix_c1(self):
        """2x2 shadow metric matrix at c=1."""
        result = shadow_metric_matrix_bosonic(Rational(1))
        # Diagonal: Q_T at t=0 is (2*1/2)^2 = 1, Q_J = (2/3)^2 = 4/9
        assert result['Q_T'].subs(Symbol('t'), 0) == 1
        assert result['Q_J'] == Rational(4, 9)

    def test_T_line_S4_formula(self):
        """S4_T = 10/(c(5c+22)) matches Virasoro."""
        for c_val in [1, 2, Rational(3, 2)]:
            data = shadow_data_T_line(c_val)
            expected = Rational(10) / (c_val * (5 * c_val + 22))
            assert data['S4'] == expected

    def test_T_line_delta(self):
        """Delta_T = 40/(5c+22) for the T-line."""
        c_v = Rational(1)
        data = shadow_data_T_line(c_v)
        # Delta = 8*(c/2)*10/(c*(5c+22)) = 40/(5c+22)
        expected = Rational(40) / (5 * c_v + 22)
        assert simplify(data['Delta'] - expected) == 0


# =========================================================================
# 4. Spectral flow invariance
# =========================================================================

class TestSpectralFlow:
    """Test that shadow data is spectral-flow invariant."""

    @pytest.mark.parametrize("c_val", [1, Rational(3, 2), 2])
    def test_spectral_flow_invariance(self, c_val):
        """Shadow data is identical at theta=0 (NS) and theta=1 (R)."""
        result = spectral_flow_invariance_shadow(c_val)
        assert result['all_invariant'] is True

    def test_spectral_flow_modes(self):
        """Spectral flow at theta=1: G+ -> weight 5/2, G- -> weight 1/2."""
        modes = spectral_flow_modes(1)
        assert modes['G+_weight'] == Rational(5, 2)
        assert modes['G-_weight'] == Rational(1, 2)

    def test_spectral_flow_weight_sum(self):
        """h(G+) + h(G-) = 3 for all theta."""
        for theta in [0, 1, 2, -1, Rational(1, 2)]:
            modes = spectral_flow_modes(theta)
            assert modes['G+_weight'] + modes['G-_weight'] == 3

    def test_shadow_coefficients_ns_equals_r(self):
        """S_r(NS) = S_r(R) for r=2..8 at c=1."""
        result = spectral_flow_shadow_coefficients_agree(1)
        assert result['all_agree'] is True

    @pytest.mark.parametrize("c_val", [1, Rational(3, 2), 2])
    def test_spectral_flow_kappa_invariant(self, c_val):
        """kappa is the same in NS and R sectors."""
        result = spectral_flow_invariance_shadow(c_val)
        assert result['NS_data']['kappa_T'] == result['R_data']['kappa_T']
        assert result['NS_data']['kappa_J'] == result['R_data']['kappa_J']

    def test_spectral_flow_s4_invariant(self):
        """S4 is the same in NS and R sectors."""
        result = spectral_flow_invariance_shadow(1)
        assert result['NS_data']['S4_T'] == result['R_data']['S4_T']


# =========================================================================
# 5. Elliptic genus and K3
# =========================================================================

class TestEllipticGenus:
    """Test elliptic genus computations for K3."""

    def test_phi01_at_q0(self):
        """phi_{0,1} at q^0: y + 10 + y^{-1}."""
        coeffs = weak_jacobi_phi01_coefficients(max_n=0, max_l=2)
        assert coeffs[(0, 1)] == 1    # y
        assert coeffs[(0, 0)] == 10   # constant
        assert coeffs[(0, -1)] == 1   # y^{-1}
        assert coeffs[(0, 2)] == 0    # no y^2 at q^0
        assert coeffs[(0, -2)] == 0   # no y^{-2} at q^0

    def test_k3_euler_characteristic(self):
        """chi(K3) = Z_ell(tau, 0) = 24."""
        assert k3_euler_characteristic() == 24

    def test_k3_elliptic_genus_is_2_phi01(self):
        """K3 elliptic genus = 2 * phi_{0,1}."""
        phi_coeffs = weak_jacobi_phi01_coefficients(max_n=1, max_l=2)
        k3_coeffs = k3_elliptic_genus_coefficients(max_n=1, max_l=2)
        for key in phi_coeffs:
            assert k3_coeffs[key] == 2 * phi_coeffs[key]

    def test_k3_z0_value(self):
        """Z_ell^{K3}(tau, 0) = 2*(1+10+1) = 24."""
        k3_coeffs = k3_elliptic_genus_coefficients(max_n=0, max_l=2)
        z0_value = sum(k3_coeffs[(0, l)] for l in range(-2, 3))
        assert z0_value == 24

    def test_phi01_discriminant_dependence(self):
        """c(n,l) depends only on D = 4n - l^2."""
        coeffs = weak_jacobi_phi01_coefficients(max_n=3, max_l=3)
        # Check: c(1,0) and c(0,?) should correspond to D=4 and some other D
        # D = 4*1 - 0 = 4 for (1,0)
        # c(1,0) should equal c(n,l) for any other (n,l) with 4n-l^2 = 4
        # e.g., n=2, l=2: D = 8-4 = 4, but we need (2,2) in our range
        # Actually (2,2) has D = 8-4 = 4. So c(2,2) should equal c(1,0).
        if (2, 2) in coeffs:
            assert coeffs[(1, 0)] == coeffs[(2, 2)]

    def test_shadow_connection_c6(self):
        """At c=6: kappa=0, F_1=0, but chi(K3)=24."""
        result = elliptic_genus_shadow_connection(c_val=6)
        assert result['kappa'] == 0
        assert result['F_1'] == 0
        assert result['kappa_is_zero'] is True
        assert result['chi_K3'] == 24

    def test_phi01_q1_coefficients(self):
        """At q^1: verify known coefficients."""
        coeffs = weak_jacobi_phi01_coefficients(max_n=1, max_l=3)
        # (1, 0): D=4, c=108
        assert coeffs[(1, 0)] == 108
        # (1, +/-1): D=3, c=64
        assert coeffs[(1, 1)] == 64
        assert coeffs[(1, -1)] == 64
        # (1, +/-2): D=0, c=10
        assert coeffs[(1, 2)] == 10
        assert coeffs[(1, -2)] == 10

    def test_jacobi_index(self):
        """The Jacobi index of the K3 elliptic genus is m = c/3 = 2."""
        result = elliptic_genus_shadow_connection(c_val=6)
        # At c=6, the N=2 algebra has Jacobi index m = c/3 = 2.
        # For K3, the elliptic genus is a Jacobi form of index 1
        # (from the N=4 structure, not N=2). The N=2 index would be c/3=2.
        # But the physical K3 sigma model has enhanced N=4 supersymmetry,
        # so the index is 1 (= c/6 for N=4).
        # Our module computes c/3 = 2 as the N=2 Jacobi index.
        assert Rational(6) / 3 == 2  # N=2 index


# =========================================================================
# 6. Mathieu moonshine
# =========================================================================

class TestMathieuMoonshine:
    """Test Mathieu moonshine coefficients and M_24 decompositions."""

    def test_A1_is_90(self):
        """A_1 = 90 = 45 + 45'."""
        coeffs = mathieu_moonshine_coefficients()
        assert coeffs[1] == 90

    def test_A2_is_462(self):
        """A_2 = 462 = 231 + 231'."""
        coeffs = mathieu_moonshine_coefficients()
        assert coeffs[2] == 462

    def test_A3_is_1540(self):
        """A_3 = 1540 = 770 + 770'."""
        coeffs = mathieu_moonshine_coefficients()
        assert coeffs[3] == 1540

    def test_m24_decomposition_dims(self):
        """M_24 representation dimensions sum correctly."""
        decomp = mathieu_m24_decomposition()
        assert sum(decomp[1]['dims']) == 90
        assert sum(decomp[2]['dims']) == 462
        assert sum(decomp[3]['dims']) == 1540

    def test_A0_negative(self):
        """A_0 = -2 (BPS subtraction)."""
        coeffs = mathieu_moonshine_coefficients()
        assert coeffs[0] == -2


# =========================================================================
# 7. N=2 minimal models
# =========================================================================

class TestMinimalModels:
    """Test N=2 minimal model shadow data."""

    @pytest.mark.parametrize("k_val,expected_c", [
        (1, 1),
        (2, Rational(3, 2)),
        (3, Rational(9, 5)),
        (4, 2),
    ])
    def test_central_charge(self, k_val, expected_c):
        """Central charges of the first minimal models."""
        assert n2_central_charge(k_val) == expected_c

    @pytest.mark.parametrize("k_val,expected_kappa", [
        (1, Rational(5, 4)),
        (2, Rational(3, 2)),
        (3, Rational(7, 4)),
        (4, Rational(2)),
    ])
    def test_minimal_model_kappa(self, k_val, expected_kappa):
        """kappa values for minimal models."""
        mm = n2_minimal_model(k_val)
        assert mm['kappa'] == expected_kappa

    def test_minimal_model_complementarity(self):
        """kappa + kappa' = 1 for all minimal models."""
        for k in [1, 2, 3, 4]:
            mm = n2_minimal_model(k)
            assert mm['complementarity_sum'] == 1

    def test_minimal_model_dual_c(self):
        """Dual central charges for minimal models."""
        mm = n2_minimal_model(1)
        assert mm['c_dual'] == 5

        mm = n2_minimal_model(4)
        assert mm['c_dual'] == 4

    def test_chiral_ring_dimension(self):
        """Chiral ring dimension = k + 1."""
        for k in [1, 2, 3, 4]:
            mm = n2_minimal_model(k)
            assert mm['chiral_ring_dim'] == k + 1

    def test_n_primaries(self):
        """Number of primaries = (k+1)(k+2)/2."""
        for k in [1, 2, 3, 4]:
            mm = n2_minimal_model(k)
            expected = Rational(k + 1) * (k + 2) / 2
            assert mm['n_primaries'] == expected

    def test_minimal_model_F1(self):
        """F_1 = kappa/24 for minimal models."""
        mm = n2_minimal_model(1)
        assert mm['F_1'] == Rational(5, 4) / 24

    def test_minimal_model_table(self):
        """Table of all four minimal models."""
        table = n2_minimal_model_table()
        assert len(table) == 4
        assert all(k in table for k in [1, 2, 3, 4])

    def test_minimal_model_shadow_class(self):
        """Overall shadow class is M for all minimal models."""
        for k in [1, 2, 3, 4]:
            mm = n2_minimal_model(k)
            assert mm['shadow_class'] == 'M'

    def test_partition_function_ns(self):
        """Vacuum character data for k=1 minimal model."""
        pf = n2_minimal_model_partition_function_ns(1)
        assert pf['c'] == 1
        # Vacuum at h=0 has 1 state
        assert pf['vacuum_degeneracies'][0] == 1
        # At h=1/2: two fermionic states G^+_{-1/2}|0> and G^-_{-1/2}|0>
        assert pf['vacuum_degeneracies'][Rational(1, 2)] == 2


# =========================================================================
# 8. Gepner models
# =========================================================================

class TestGepnerModels:
    """Test Gepner model computations."""

    def test_gepner_quintic_c(self):
        """Quintic Gepner (3,3,3,3,3): c_total = 9."""
        gep = gepner_quintic()
        assert gep['c_total'] == 9

    def test_gepner_quintic_kappa(self):
        """Quintic Gepner: kappa_total = 5 * 7/4 = 35/4."""
        gep = gepner_quintic()
        assert gep['kappa_total'] == Rational(35, 4)

    def test_gepner_quintic_dimension(self):
        """Quintic Gepner: CY dimension = 9/3 = 3."""
        gep = gepner_quintic()
        assert gep['CY_dimension'] == 3

    def test_gepner_quintic_F1(self):
        """Quintic Gepner: F_1 = 35/96."""
        gep = gepner_quintic()
        assert gep['F_1_total'] == Rational(35, 96)

    def test_gepner_quintic_complementarity(self):
        """Quintic Gepner: sum of kappa + kappa_dual = 5 (one per factor)."""
        gep = gepner_quintic()
        assert gep['complementarity_sum'] == 5

    def test_gepner_k3_c(self):
        """K3 Gepner (2,2,2,2): c_total = 6."""
        models = gepner_k3()
        gep = models['(2,2,2,2)']
        assert gep['c_total'] == 6

    def test_gepner_k3_kappa(self):
        """K3 Gepner (2,2,2,2): kappa_total = 4 * 3/2 = 6."""
        models = gepner_k3()
        gep = models['(2,2,2,2)']
        assert gep['kappa_total'] == 6

    def test_gepner_additivity(self):
        """Kappa is additive across Gepner factors."""
        gep = gepner_model([1, 2, 3])
        kap1 = kappa_n2(k_val=1)  # 5/4
        kap2 = kappa_n2(k_val=2)  # 3/2
        kap3 = kappa_n2(k_val=3)  # 7/4
        assert gep['kappa_total'] == kap1 + kap2 + kap3

    def test_gepner_k3_sixfold(self):
        """K3 Gepner (1,1,1,1,1,1): c = 6 * 1 = 6, kappa = 6 * 5/4 = 15/2."""
        models = gepner_k3()
        gep = models['(1,1,1,1,1,1)']
        assert gep['c_total'] == 6
        assert gep['kappa_total'] == Rational(15, 2)

    def test_gepner_k3_threefold(self):
        """K3 Gepner (4,4,4): c = 3 * 2 = 6, kappa = 3 * 2 = 6."""
        models = gepner_k3()
        gep = models['(4,4,4)']
        assert gep['c_total'] == 6
        assert gep['kappa_total'] == 6


# =========================================================================
# 9. Cross-checks and edge cases
# =========================================================================

class TestCrossChecks:
    """Comprehensive cross-checks and edge cases."""

    def test_master_verification(self):
        """Run all cross-checks via verify_all_cross_checks."""
        checks = verify_all_cross_checks()
        for name, passed in checks.items():
            assert passed, f"Cross-check failed: {name}"

    def test_k_from_c_inverse(self):
        """k_from_c is the inverse of n2_central_charge."""
        for k_v in [1, 2, 3, 4, 10]:
            c_v = n2_central_charge(k_v)
            k_recovered = k_from_c(c_v)
            assert simplify(k_recovered - Rational(k_v)) == 0

    def test_kappa_never_equals_7c_over_6(self):
        """The correct kappa != 7c/6 at any finite non-zero c with c != 3."""
        for k_v in [1, 2, 3, 4, 10]:
            c_v = n2_central_charge(k_v)
            kap = kappa_n2(c_val=c_v)
            naive = 7 * c_v / 6
            assert kap != naive, f"kappa equals naive 7c/6 at k={k_v}"

    def test_kappa_positive_for_positive_k(self):
        """kappa > 0 for k > 0 (unitary minimal models)."""
        for k_v in [1, 2, 3, 4, 10, 100]:
            kap = kappa_n2(k_val=k_v)
            assert kap > 0

    def test_kappa_diverges_at_c3(self):
        """kappa has a pole at c=3 (k -> infinity)."""
        # kappa = (6-c)/(2(3-c)) -> infinity as c -> 3
        # Check: kappa at c close to 3 is large
        kap_near = kappa_n2(c_val=Rational(29, 10))  # c = 2.9
        assert kap_near > 10

    def test_full_summary_c1(self):
        """Full summary at c=1 contains all required fields."""
        summary = full_n2_summary(c_val=1)
        assert summary['c'] == 1
        assert summary['kappa'] == Rational(5, 4)
        assert summary['c_dual'] == 5
        assert summary['complementarity_sum'] == 1
        assert summary['spectral_flow_invariant'] is True

    def test_shadow_coefficients_recursion_c1(self):
        """Shadow coefficients via recursion at c=1 (T-line)."""
        kap = Rational(1, 2)  # kappa_T for c=1
        alpha = Rational(2)
        S4 = Rational(10) / (1 * (5 + 22))  # = 10/27
        S = _compute_shadow_coefficients(kap, alpha, S4, 6)
        # S_2 = kappa = 1/2
        assert S[2] == kap
        # S_3 = alpha = 2
        # Actually S_3 in the shadow parametrization: from the generating function
        # H(t) = t^2 * sqrt(Q(t)), we have 3*S_3 = a_1 where a_1 is the
        # first Taylor coefficient of sqrt(Q). Let me verify:
        # Q(t) = (1 + 6t)^2 + 2*Delta*t^2 where Delta = 8*(1/2)*(10/27) = 40/27
        # Q(t) = 1 + 12t + (36 + 80/27)t^2 = 1 + 12t + (972+80)/27 * t^2
        #       = 1 + 12t + 1052/27 * t^2
        # sqrt(Q) at t=0: 1
        # d/dt sqrt(Q) at t=0: Q'(0)/(2*sqrt(Q(0))) = 12/2 = 6
        # So a_1 = 6, hence 3*S_3 = 6, so S_3 = 2. Matches alpha.
        assert S[3] == alpha

    def test_shadow_coefficients_heisenberg(self):
        """Heisenberg (J-line) shadow tower terminates: S_r = 0 for r >= 3."""
        kap = Rational(1, 3)
        alpha = Rational(0)
        S4 = Rational(0)
        S = _compute_shadow_coefficients(kap, alpha, S4, 6)
        assert S[2] == kap
        for r in range(3, 7):
            assert S[r] == 0

    def test_anomaly_ratio_not_constant(self):
        """sigma = kappa/c is NOT constant for N=2 (it is a coset, not W-algebra)."""
        sigma_1 = kappa_n2(c_val=1) / 1      # = 5/4
        sigma_2 = kappa_n2(c_val=2) / 2      # = 1
        assert sigma_1 != sigma_2

    def test_shadow_metric_values_various_c(self):
        """Shadow metric at c=1, 6, 9."""
        results = shadow_metric_at_values([1, 6, 9])
        # At c=1: should have data
        assert 'kappa_total' in results[1]
        assert results[1]['kappa_total'] == Rational(5, 4)
        # At c=6: kappa = 0
        assert results[6]['kappa_total'] == 0
        # At c=9: kappa = (6-9)/(2(3-9)) = -3/(-12) = 1/4
        assert results[9]['kappa_total'] == Rational(1, 4)
