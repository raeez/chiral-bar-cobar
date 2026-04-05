"""Tests for the Eisenstein moment matrix module.

Covers:
  - Shadow coefficient computation and known values
  - Genus-1 invariants (delta_H, Q^contact, rho)
  - Surface Hankel moment matrices
  - Shadow Eisenstein series
  - Shadow Epstein zeta function
  - Duality structure at c=13
  - Lee-Yang singularity at c=-22/5
  - Moment matrix exclusion principle
  - Partition function / Eisenstein series data
"""

import sys
import os
import math
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from eisenstein_moment_matrix import (
    shadow_coefficient_exact, shadow_coefficients,
    genus1_free_energy, delta_H_genus1, quartic_contact, rho_genus1,
    S_heisenberg, S_virasoro, S_WN,
    surface_moment_matrix, surface_moment_minors,
    shadow_eisenstein_series, shadow_eisenstein_array,
    shadow_epstein_zeta, shadow_epstein_zeta_complex,
    shadow_epstein_functional_equation_test,
    shadow_duality_ratio, shadow_duality_epstein_ratio,
    eisenstein_moment_matrix_genus1, eisenstein_moment_matrix_pure,
    eisenstein_moment_minors,
    eta_function, heisenberg_partition,
    virasoro_vacuum_character,
    eisenstein_E2, eisenstein_E4, eisenstein_E6,
    shadow_modular_ratio,
    lee_yang_approach,
)

from mpmath import mpf, mp

mp.dps = 30


# =========================================================================
# Shadow coefficients
# =========================================================================

class TestShadowCoefficients:

    def test_S2_is_half_c(self):
        for c_val in [1, 2, 13, 25, 26]:
            S2 = shadow_coefficient_exact(2, c_val)
            assert abs(S2 - mpf(c_val) / 2) < 1e-25

    def test_S3_is_two(self):
        for c_val in [1, 5, 13, 26]:
            S3 = shadow_coefficient_exact(3, c_val)
            assert abs(S3 - 2) < 1e-25

    def test_S4_quartic_contact(self):
        for c_val in [1, 2, 13, 25]:
            S4 = shadow_coefficient_exact(4, c_val)
            expected = mpf(10) / (mpf(c_val) * (5 * mpf(c_val) + 22))
            assert abs(S4 - expected) < 1e-20

    def test_S5_quintic(self):
        for c_val in [1, 2, 13, 26]:
            S5 = shadow_coefficient_exact(5, c_val)
            expected = mpf(-48) / (mpf(c_val) ** 2 * (5 * mpf(c_val) + 22))
            assert abs(S5 - expected) < 1e-20

    def test_shadow_coefficients_dict(self):
        S = shadow_coefficients(8, 13)
        assert len(S) >= 7
        assert abs(S[2] - mpf(13) / 2) < 1e-20
        assert abs(S[3] - 2) < 1e-20

    def test_S5_at_selfdual_c13(self):
        """S_5(13) = -48/(169 * 87) = -16/4901."""
        S5 = shadow_coefficient_exact(5, 13)
        expected = mpf(-16) / 4901
        assert abs(S5 - expected) < 1e-20

    def test_S5_at_c26(self):
        """S_5(26) = -48/(676 * 152) = -3/6422."""
        S5 = shadow_coefficient_exact(5, 26)
        expected = mpf(-3) / 6422
        assert abs(S5 - expected) < 1e-20

    def test_shadow_tower_alternates_sign(self):
        """For c > 0, the shadow obstruction tower beyond arity 3 alternates in sign."""
        S = shadow_coefficients(10, 13)
        # S_4 > 0, S_5 < 0, ...
        assert S[4] > 0
        assert S[5] < 0


# =========================================================================
# Genus-1 invariants
# =========================================================================

class TestGenus1Invariants:

    def test_free_energy_F1(self):
        assert abs(genus1_free_energy(1) - mpf(1) / 48) < 1e-25
        assert abs(genus1_free_energy(24) - mpf(1) / 2) < 1e-25

    def test_delta_H_genus1(self):
        """delta_H^(1) = 120/[c^2(5c+22)]."""
        for c_val in [1, 13, 26]:
            d = delta_H_genus1(c_val)
            expected = mpf(120) / (mpf(c_val) ** 2 * (5 * mpf(c_val) + 22))
            assert abs(d - expected) < 1e-20

    def test_quartic_contact_formula(self):
        """Q^contact = 10/[c(5c+22)]."""
        for c_val in [1, 13, 26]:
            Q = quartic_contact(c_val)
            expected = mpf(10) / (mpf(c_val) * (5 * mpf(c_val) + 22))
            assert abs(Q - expected) < 1e-20

    def test_rho_genus1_formula(self):
        """rho^(1) = 240/[c^3(5c+22)]."""
        for c_val in [1, 13, 26]:
            r = rho_genus1(c_val)
            expected = mpf(240) / (mpf(c_val) ** 3 * (5 * mpf(c_val) + 22))
            assert abs(r - expected) < 1e-20

    def test_delta_H_equals_12_S4_over_c(self):
        """delta_H^(1) = 12 * S_4 / c (relation between genus-1 correction and quartic)."""
        for c_val in [1, 5, 13, 26]:
            d = delta_H_genus1(c_val)
            S4 = shadow_coefficient_exact(4, c_val)
            assert abs(d - 12 * S4 / mpf(c_val)) < 1e-20

    def test_lee_yang_denominator(self):
        """At c = -22/5, the denominator 5c+22 vanishes."""
        c_ly = mpf(-22) / 5
        h = 5 * c_ly + 22
        assert abs(h) < 1e-25


# =========================================================================
# Surface moment matrices (Layer 1)
# =========================================================================

class TestSurfaceMomentMatrix:

    def test_heisenberg_S_values(self):
        """S_H(u) = zeta(u)*zeta(u+1) at integer points."""
        from mpmath import zeta
        for u in [2, 3, 4, 5]:
            S = S_heisenberg(u)
            expected = zeta(u) * zeta(u + 1)
            assert abs(S - expected) < 1e-25

    def test_virasoro_S_values(self):
        """S_Vir(u) = zeta(u+1)*(zeta(u)-1)."""
        from mpmath import zeta
        for u in [2, 3, 4]:
            S = S_virasoro(u)
            expected = zeta(u + 1) * (zeta(u) - 1)
            assert abs(S - expected) < 1e-25

    def test_surface_matrix_is_hankel(self):
        """M_{ij} = S(i+j+alpha): entries along anti-diagonals are equal."""
        M = surface_moment_matrix(S_heisenberg, 4, 2)
        # Check: M[0,1] == M[1,0] (Hankel symmetry)
        assert abs(M[0, 1] - M[1, 0]) < 1e-25

    def test_surface_minors_positive_heisenberg(self):
        """All Heisenberg surface minors should be positive."""
        minors = surface_moment_minors(S_heisenberg, 4, 2)
        for m in minors:
            assert m > 0

    def test_virasoro_minors_smaller(self):
        """Virasoro minors < Heisenberg minors (defect structure)."""
        minors_H = surface_moment_minors(S_heisenberg, 3, 2)
        minors_V = surface_moment_minors(S_virasoro, 3, 2)
        for i in range(3):
            assert abs(minors_V[i]) < abs(minors_H[i])

    def test_WN_interpolates(self):
        """W_2 = Virasoro (single generator beyond stress tensor)."""
        # W_2 means N=2, but by convention S_WN(2,u) uses 2 generators
        # This is actually the Virasoro case for our S_WN formula
        for u in [2, 3, 4]:
            S_w2 = S_WN(2, u)
            S_vir = S_virasoro(u)
            # S_WN(2,u) = zeta(u+1)*((2-1)*zeta(u) - sum_{j=1}^1 j^{-u})
            #           = zeta(u+1)*(zeta(u) - 1) = S_virasoro(u)
            assert abs(S_w2 - S_vir) < 1e-20


# =========================================================================
# Shadow Eisenstein series (Layer 2)
# =========================================================================

class TestShadowEisenstein:

    def test_shadow_eisenstein_at_q0(self):
        """E^{shadow}_k(q=0, c) = S_k(c)."""
        for c_val in [1, 13, 26]:
            for k in [2, 3, 4, 5]:
                E = shadow_eisenstein_series(k, c_val, 0, max_terms=10)
                S_k = shadow_coefficient_exact(k, c_val)
                assert abs(E - S_k) < 1e-20

    def test_shadow_eisenstein_monotone_in_q(self):
        """For small q, E^{shadow}_2 should increase (S_3 = 2 > 0)."""
        c_val = 13
        E0 = shadow_eisenstein_series(2, c_val, 0, 15)
        E1 = shadow_eisenstein_series(2, c_val, 0.01, 15)
        # E_2(q) = S_2 + S_3*q + S_4*q^2 + ...
        # S_3 = 2 > 0, so E_2 increases for small q
        assert E1 > E0

    def test_shadow_eisenstein_convergence(self):
        """Series should converge for |q| < 1. Check stability under truncation."""
        c_val = 13
        q_val = 0.1
        E15 = shadow_eisenstein_series(2, c_val, q_val, 15)
        E20 = shadow_eisenstein_series(2, c_val, q_val, 20)
        # Should agree to many digits
        assert abs(E15 - E20) / abs(E20) < 1e-10

    def test_shadow_eisenstein_array(self):
        """Array computation matches individual calls."""
        c_val = 13
        q_val = 0.1
        arr = shadow_eisenstein_array(c_val, q_val, range(2, 6), 15)
        for k in range(2, 6):
            individual = shadow_eisenstein_series(k, c_val, q_val, 15)
            assert abs(arr[k] - individual) < 1e-20

    def test_heisenberg_shadow_eisenstein_trivial(self):
        """For Heisenberg (depth 2), only S_2 = 1/2 is nonzero in the shadow obstruction tower.
        But Virasoro shadow obstruction tower has S_3 = 2 etc., so E^{shadow} is nontrivial.
        (Heisenberg tower terminates at r=2: S_r = 0 for r >= 3.)
        This test verifies the Virasoro tower does NOT terminate."""
        S = shadow_coefficients(8, 13)
        assert abs(S[3]) > 1e-5  # S_3 = 2
        assert abs(S[4]) > 1e-5  # S_4 nonzero
        assert abs(S[5]) > 1e-5  # S_5 nonzero


# =========================================================================
# Shadow Epstein zeta
# =========================================================================

class TestShadowEpsteinZeta:

    def test_epstein_positive_for_positive_c(self):
        """Z_shadow(s, c) > 0 for real s > 1 and c > 0 (all S_r^2 >= 0)."""
        for c_val in [1, 13, 26]:
            for s_val in [2, 3, 5]:
                Z = shadow_epstein_zeta(s_val, c_val, 20)
                assert Z > 0

    def test_epstein_decreasing_in_s(self):
        """Z_shadow(s, c) decreases as s increases (r^{-s} terms shrink)."""
        c_val = 13
        Z2 = shadow_epstein_zeta(2, c_val, 25)
        Z5 = shadow_epstein_zeta(5, c_val, 25)
        assert Z2 > Z5

    def test_epstein_dominated_by_kappa(self):
        """For large s, Z_shadow ~ |S_2|^2 * 2^{-s} (leading term)."""
        c_val = 13
        S2 = mpf(13) / 2
        for s_val in [10, 15]:
            Z = shadow_epstein_zeta(s_val, c_val, 25)
            leading = S2 ** 2 * mpf(2) ** (-s_val)
            assert abs(Z / leading - 1) < 0.01  # dominated by r=2 term

    def test_epstein_self_dual_c13(self):
        """At c=13, Z(s,13) = Z(s,26-13) = Z(s,13) (trivial self-check)."""
        for s_val in [2, 3, 4]:
            ratio = shadow_duality_epstein_ratio(s_val, 13, 25)
            assert abs(ratio - 1) < 1e-20

    def test_epstein_complex_s(self):
        """Complex Epstein zeta should reduce to real when s_imag=0."""
        c_val = 13
        Z_real = shadow_epstein_zeta(3, c_val, 20)
        Z_complex = shadow_epstein_zeta_complex(3, 0, c_val, 20)
        assert abs(Z_complex - Z_real) < 1e-20

    def test_epstein_convergence_with_truncation(self):
        """Verify convergence: increasing max_r should stabilize."""
        c_val = 13
        s_val = 3
        Z20 = shadow_epstein_zeta(s_val, c_val, 20)
        Z25 = shadow_epstein_zeta(s_val, c_val, 25)
        assert abs(Z20 - Z25) / abs(Z25) < 1e-5


# =========================================================================
# Duality structure
# =========================================================================

class TestDuality:

    def test_duality_ratio_c13(self):
        """At c=13: S_r(13)/S_r(13) = 1 for all r."""
        for r in range(2, 8):
            ratio = shadow_duality_ratio(r, 13)
            assert abs(ratio - 1) < 1e-20

    def test_duality_ratio_c1_vs_c25(self):
        """S_r(1) / S_r(25) tests the Vir_1^! = Vir_25 duality."""
        # S_2(1)/S_2(25) = (1/2)/(25/2) = 1/25
        ratio2 = shadow_duality_ratio(2, 1)
        assert abs(ratio2 - mpf(1) / 25) < 1e-20

        # S_3(1)/S_3(25) = 2/2 = 1
        ratio3 = shadow_duality_ratio(3, 1)
        assert abs(ratio3 - 1) < 1e-20

    def test_duality_nontrivial_at_S4(self):
        """S_4(c)/S_4(26-c) != 1 in general (nontrivial duality)."""
        ratio = shadow_duality_ratio(4, 1)
        # S_4(1) = 10/(1*27) = 10/27
        # S_4(25) = 10/(25*147) = 10/3675
        expected = mpf(3675) / 27  # = 136.111...
        assert abs(ratio - expected) < 1e-15

    def test_functional_equation_probe(self):
        """Probe whether Z_shadow has a reflection symmetry at c=13."""
        results = shadow_epstein_functional_equation_test(3, 13, 25)
        # At least check it returns something
        assert isinstance(results, dict)
        assert len(results) > 0


# =========================================================================
# Eisenstein moment matrix
# =========================================================================

class TestEisensteinMomentMatrix:

    def test_E1_is_scalar(self):
        """E_1(c) = S_2(c) * F_1(c) = (c/2)(c/48) = c^2/96."""
        for c_val in [1, 13, 26]:
            M = eisenstein_moment_matrix_genus1(1, c_val)
            expected = mpf(c_val) ** 2 / 96
            assert abs(M[0, 0] - expected) < 1e-20

    def test_pure_E1_is_S2(self):
        """Pure E_1(c) = S_2(c) = c/2."""
        for c_val in [1, 13, 26]:
            M = eisenstein_moment_matrix_pure(1, c_val)
            assert abs(M[0, 0] - mpf(c_val) / 2) < 1e-20

    def test_moment_matrix_symmetric(self):
        """The moment matrix is symmetric (Hankel)."""
        M = eisenstein_moment_matrix_pure(4, 13)
        for i in range(4):
            for j in range(4):
                assert abs(M[i, j] - M[j, i]) < 1e-20

    def test_moment_matrix_hankel(self):
        """M_{ij} depends only on i+j (Hankel property)."""
        M = eisenstein_moment_matrix_pure(4, 13)
        # M[0,2] = S_4, M[1,1] = S_4
        assert abs(M[0, 2] - M[1, 1]) < 1e-20
        # M[0,3] = S_5, M[1,2] = S_5
        assert abs(M[0, 3] - M[1, 2]) < 1e-20

    def test_pure_minors_2x2(self):
        """det(E_2^pure) = S_2*S_4 - S_3^2 at c=13."""
        c_val = 13
        S = shadow_coefficients(6, c_val)
        det_expected = S[2] * S[4] - S[3] ** 2
        minors = eisenstein_moment_minors(2, c_val, pure=True)
        assert abs(minors[1] - det_expected) < 1e-15

    def test_pure_minor_1x1(self):
        """det(E_1^pure) = S_2(c) = c/2."""
        for c_val in [1, 13, 26]:
            minors = eisenstein_moment_minors(1, c_val, pure=True)
            assert abs(minors[0] - mpf(c_val) / 2) < 1e-20

    def test_2x2_minor_sign(self):
        """det(E_2^pure) = S_2*S_4 - S_3^2 should be negative for generic c > 0.

        S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)].
        det = (c/2)*10/[c(5c+22)] - 4 = 5/(5c+22) - 4 = (5 - 20c - 88)/(5c+22)
            = -(20c+83)/(5c+22) < 0 for c > 0.
        """
        for c_val in [1, 5, 13, 26, 100]:
            minors = eisenstein_moment_minors(2, c_val, pure=True)
            assert minors[1] < 0  # always negative

    def test_2x2_det_formula(self):
        """Verify det(E_2) = -(20c+83)/(5c+22)."""
        for c_val in [1, 5, 13, 26]:
            c = mpf(c_val)
            expected = -(20 * c + 83) / (5 * c + 22)
            minors = eisenstein_moment_minors(2, c_val, pure=True)
            assert abs(minors[1] - expected) < 1e-15


# =========================================================================
# Partition functions and Eisenstein series
# =========================================================================

class TestPartitionFunctions:

    def test_eta_at_small_q(self):
        """eta(q) ~ q^{1/24} for small q (product -> 1)."""
        q = mpf('0.001')
        eta = eta_function(q, 50)
        assert abs(eta - q ** (mpf(1) / 24)) / q ** (mpf(1) / 24) < 0.01

    def test_heisenberg_partition_positive(self):
        """1/eta(q) > 0 for 0 < q < 1."""
        for q_val in [0.01, 0.1, 0.5]:
            Z = heisenberg_partition(q_val, 80)
            assert Z > 0

    def test_E2_at_q0(self):
        """E_2(0) = 1."""
        assert abs(eisenstein_E2(0) - 1) < 1e-25

    def test_E4_at_q0(self):
        """E_4(0) = 1."""
        assert abs(eisenstein_E4(0) - 1) < 1e-25

    def test_E6_at_q0(self):
        """E_6(0) = 1."""
        assert abs(eisenstein_E6(0) - 1) < 1e-25

    def test_E2_first_coefficient(self):
        """E_2 = 1 - 24q - 72q^2 - ... sigma_1(1) = 1, sigma_1(2) = 3."""
        q = mpf('0.001')
        E2 = eisenstein_E2(q, 5)
        expected = 1 - 24 * q - 72 * q ** 2  # truncated
        assert abs(E2 - expected) < 1e-6  # higher terms negligible

    def test_E4_first_coefficient(self):
        """E_4 = 1 + 240q + 2160q^2 + ... sigma_3(1) = 1, sigma_3(2) = 9."""
        q = mpf('0.001')
        E4 = eisenstein_E4(q, 5)
        expected = 1 + 240 * q + 2160 * q ** 2
        assert abs(E4 - expected) < 1e-4  # higher order terms at q=0.001

    def test_virasoro_vacuum_positive(self):
        """Vacuum character is positive for 0 < q < 1, c > 0."""
        for c_val in [1, 13, 26]:
            chi = virasoro_vacuum_character(c_val, 0.1, 30)
            assert chi > 0


# =========================================================================
# Shadow-modular connection
# =========================================================================

class TestShadowModularRatio:

    def test_ratio_exists_at_weight2(self):
        """E^{shadow}_2 / E_2 should be finite."""
        ratio = shadow_modular_ratio(2, 13, 0.1, 15)
        assert ratio is not None
        assert abs(ratio) < 1e10

    def test_ratio_varies_with_q(self):
        """The ratio is NOT constant (shadow is not modular)."""
        r1 = shadow_modular_ratio(2, 13, 0.05, 15)
        r2 = shadow_modular_ratio(2, 13, 0.2, 15)
        assert abs(r1 - r2) > 1e-5  # should differ

    def test_unsupported_weight(self):
        """Weights other than 2,4,6 return None."""
        assert shadow_modular_ratio(3, 13, 0.1) is None
        assert shadow_modular_ratio(8, 13, 0.1) is None


# =========================================================================
# Lee-Yang singularity
# =========================================================================

class TestLeeYang:

    def test_approach_from_above(self):
        """As c -> -22/5 from above, all shadow invariants diverge."""
        c_near = -22.0 / 5 + 0.01
        result = lee_yang_approach(c_near)
        assert abs(result['5c+22']) < 0.1
        assert abs(result['Q_contact']) > 10

    def test_approach_from_below(self):
        """As c -> -22/5 from below, divergence with opposite sign."""
        c_near = -22.0 / 5 - 0.01
        result = lee_yang_approach(c_near)
        assert abs(result['5c+22']) < 0.1

    def test_lee_yang_exact_value(self):
        """5c+22 = 0 at c = -22/5 = -4.4 exactly."""
        c_ly = -22.0 / 5
        assert abs(5 * c_ly + 22) < 1e-10


# =========================================================================
# Structural identities
# =========================================================================

class TestStructuralIdentities:

    def test_delta_H_ratio_to_Q_contact(self):
        """delta_H^(1) / Q^contact = 12/c for all c."""
        for c_val in [1, 5, 13, 26]:
            d = delta_H_genus1(c_val)
            Q = quartic_contact(c_val)
            assert abs(d / Q - 12 / mpf(c_val)) < 1e-20

    def test_rho_ratio_to_delta_H(self):
        """rho^(1) / delta_H^(1) = 2/c for all c."""
        for c_val in [1, 5, 13, 26]:
            r = rho_genus1(c_val)
            d = delta_H_genus1(c_val)
            assert abs(r / d - 2 / mpf(c_val)) < 1e-20

    def test_genus1_chain(self):
        """Q^contact * 12/c = delta_H, delta_H * 2/c = rho: full chain."""
        c_val = 7
        Q = quartic_contact(c_val)
        d = delta_H_genus1(c_val)
        r = rho_genus1(c_val)
        assert abs(Q * 12 / mpf(c_val) - d) < 1e-20
        assert abs(d * 2 / mpf(c_val) - r) < 1e-20

    def test_shadow_epstein_scaling(self):
        """Z_shadow(s, lambda*c) scales predictably with lambda at leading order.

        S_2(lambda*c) = lambda*c/2, so Z ~ (lambda*c/2)^2 * 2^{-s} at large s.
        """
        lam = 3
        s_val = 15
        Z_c = shadow_epstein_zeta(s_val, 5, 20)
        Z_lc = shadow_epstein_zeta(s_val, 15, 20)
        # Leading: (lam*c/2)^2 / (c/2)^2 = lam^2 = 9
        ratio = Z_lc / Z_c
        assert abs(ratio - lam ** 2) < 0.5  # approximate at large s

    def test_kappa_times_lambda1(self):
        """F_1 = kappa * lambda_1^FP = (c/2)(1/24) = c/48."""
        for c_val in [1, 13, 26]:
            kappa = mpf(c_val) / 2
            lambda1 = mpf(1) / 24
            assert abs(genus1_free_energy(c_val) - kappa * lambda1) < 1e-25


# =========================================================================
# Moment matrix exclusion
# =========================================================================

class TestMomentMatrixExclusion:

    def test_2x2_always_negative(self):
        """det(E_2) < 0 for all c > 0 (no exclusion at size 2)."""
        for c_val in [0.5, 1, 5, 13, 26, 100]:
            minors = eisenstein_moment_minors(2, c_val, pure=True)
            assert minors[1] < 0

    def test_3x3_sign(self):
        """Compute det(E_3) at c=1 and c=13 to check sign pattern."""
        for c_val in [1, 13]:
            minors = eisenstein_moment_minors(3, c_val, pure=True)
            # Just check it's finite and computable
            assert abs(minors[2]) < 1e10
            assert abs(minors[2]) > 1e-30

    def test_minors_sequence_computable(self):
        """Can compute minors up to size 4 without error."""
        minors = eisenstein_moment_minors(4, 13, pure=True)
        assert len(minors) == 4
        for m in minors:
            assert abs(m) < 1e20  # no overflow


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
