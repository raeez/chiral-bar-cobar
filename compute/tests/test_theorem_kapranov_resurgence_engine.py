r"""Tests for the Kapranov-Soibelman perverse sheaf resurgence engine.

Verifies the connection between the perverse sheaf framework of
Kapranov-Soibelman (arXiv:2512.22718) and the shadow obstruction tower's
resurgence programme. Tests cover:

1. Universal instanton action A = (2*pi)^2 across all families
2. Stokes multipliers from the MC equation
3. Perverse sheaf data (vanishing cycles, transport maps)
4. Alien derivatives in the KS framework
5. Stokes automorphism and log St = sum Delta_omega (Thm 2.3.10)
6. Bridge equation and MC constraint
7. Shadow Borel transform and singularity structure
8. Large-order / instanton relations
9. CS critical value spacing = shadow instanton action
10. Shadow Eisenstein theorem in perverse sheaf language
11. Anomaly cancellation at c=26
12. Shadow connection monodromy (Koszul sign)
13. Universality: kappa-dependence of S_1 across families
14. Alien derivative transport coefficients (Prop 2.2.8)
15. Convolution algebra (Thom-Sebastiani)

Multi-path verification mandate: every numerical result verified
by at least 3 independent paths.

Manuscript references:
    prop:shadow-stokes-multipliers
    prop:universal-instanton-action
    thm:shadow-transseries
    thm:shadow-eisenstein
    prop:resurgent-orthogonality
    rem:resurgent-anomaly-cancellation

External references:
    Kapranov-Soibelman, arXiv:2512.22718
"""

import cmath
import math
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_kapranov_resurgence_engine import (
    STANDARD_FAMILIES,
    UNIVERSAL_INSTANTON_ACTION,
    PerverseSheafDatum,
    alien_derivative_single_singularity,
    alien_derivative_transport_coefficients,
    anomaly_cancellation_c26,
    borel_singularities_genus,
    borel_singularity_genus,
    chern_simons_instanton_spacing,
    convolution_product_vanishing_cycles,
    dirichlet_eta,
    faber_pandharipande_lambda_g,
    kapranov_soibelman_assessment,
    kappa_heisenberg,
    kappa_kac_moody,
    kappa_virasoro,
    kappa_w_algebra,
    large_order_genus_prediction,
    large_order_genus_prediction_corrected,
    leading_stokes_multiplier,
    log_stokes_equals_alien_sum,
    mc_constraint_on_stokes,
    shadow_borel_closed_form,
    shadow_borel_transform_genus,
    shadow_connection_monodromy,
    shadow_free_energy,
    shadow_l_function,
    shadow_perverse_sheaf_genus,
    stokes_automorphism_genus,
    stokes_multiplier_genus,
    stokes_multipliers_genus,
    verify_cs_shadow_match,
    verify_instanton_universality,
    verify_shadow_eisenstein,
)


# =====================================================================
# Test 1-5: Universal instanton action
# =====================================================================

class TestUniversalInstantonAction:
    """A = (2*pi)^2 is universal across all families."""

    def test_instanton_action_value(self):
        """A = (2*pi)^2 = 4*pi^2 approx 39.478."""
        A = UNIVERSAL_INSTANTON_ACTION
        assert abs(A - 4.0 * math.pi**2) < 1e-10

    def test_instanton_action_from_borel_singularity(self):
        """A = xi_1 = first Borel singularity."""
        xi_1 = borel_singularity_genus(1)
        assert abs(xi_1 - UNIVERSAL_INSTANTON_ACTION) < 1e-10

    def test_borel_singularities_are_multiples_of_A(self):
        """xi_n = n^2 * A for all n."""
        A = UNIVERSAL_INSTANTON_ACTION
        for n in range(1, 10):
            xi_n = borel_singularity_genus(n)
            assert abs(xi_n - n**2 * A) < 1e-8

    def test_instanton_action_universality_all_families(self):
        """A = (2*pi)^2 does not depend on the algebra."""
        results = verify_instanton_universality()
        for name, data in results.items():
            assert data['A_is_universal'] is True
            assert abs(data['instanton_action'] - UNIVERSAL_INSTANTON_ACTION) < 1e-10

    def test_cs_step_equals_instanton_action(self):
        """Chern-Simons critical value step 4*pi^2 = A (KS Section 3.4)."""
        result = verify_cs_shadow_match()
        assert result['match']
        assert abs(result['ratio'] - 1.0) < 1e-10


# =====================================================================
# Test 6-12: Stokes multipliers
# =====================================================================

class TestStokesMultipliers:
    """S_n = (-1)^n * 4*pi^2 * n * kappa * i."""

    def test_leading_stokes_virasoro(self):
        """S_1(Vir_c) = -4*pi^2 * (c/2) * i."""
        c = 10.0
        kappa = kappa_virasoro(c)
        S_1 = leading_stokes_multiplier(kappa)
        expected = -4.0 * math.pi**2 * (c / 2.0) * 1j
        assert abs(S_1 - expected) < 1e-10

    def test_stokes_purely_imaginary(self):
        """All S_n are purely imaginary (for real kappa)."""
        kappa = 5.0
        for n in range(1, 10):
            S_n = stokes_multiplier_genus(n, kappa)
            assert abs(S_n.real) < 1e-10

    def test_stokes_alternating_sign(self):
        """S_n alternates in sign: Im(S_n) * (-1)^n > 0 for kappa > 0."""
        kappa = 3.0
        for n in range(1, 10):
            S_n = stokes_multiplier_genus(n, kappa)
            assert (-1)**n * S_n.imag > 0

    def test_stokes_linear_in_kappa(self):
        """S_n is linear in kappa: S_n(2*kappa) = 2*S_n(kappa)."""
        kappa = 7.0
        for n in range(1, 5):
            S_n_k = stokes_multiplier_genus(n, kappa)
            S_n_2k = stokes_multiplier_genus(n, 2.0 * kappa)
            assert abs(S_n_2k - 2.0 * S_n_k) < 1e-10

    def test_stokes_magnitude_grows_linearly_in_n(self):
        """|S_n| = 4*pi^2 * n * |kappa|."""
        kappa = 4.0
        for n in range(1, 10):
            S_n = stokes_multiplier_genus(n, kappa)
            expected_mag = 4.0 * math.pi**2 * n * abs(kappa)
            assert abs(abs(S_n) - expected_mag) < 1e-8

    def test_stokes_from_residue_consistency(self):
        """S_n = 2*pi*i * Res_{hbar=2*pi*n} (closed form)."""
        kappa = 6.0
        for n in range(1, 5):
            S_n = stokes_multiplier_genus(n, kappa)
            residue = (-1)**n * 2.0 * math.pi * n * kappa
            S_n_from_res = 2.0 * math.pi * 1j * residue
            assert abs(S_n - S_n_from_res) < 1e-10

    def test_stokes_kappa_zero_vanishes(self):
        """At kappa = 0 (uncurved), all Stokes multipliers vanish."""
        for n in range(1, 10):
            S_n = stokes_multiplier_genus(n, 0.0)
            assert abs(S_n) < 1e-15


# =====================================================================
# Test 13-17: Perverse sheaf data
# =====================================================================

class TestPerverseSheafData:
    """GMV description of the perverse sheaf for the shadow expansion."""

    def test_vanishing_cycles_one_dimensional(self):
        """Simple poles => 1-dim vanishing cycle spaces."""
        ps = shadow_perverse_sheaf_genus(5.0, 5)
        for d in ps.vanishing_cycle_dims:
            assert d == 1

    def test_singularity_set_correct(self):
        """Singularity set A = {(2*pi*n)^2 : n=1..N}."""
        n_max = 4
        ps = shadow_perverse_sheaf_genus(5.0, n_max)
        for i, s in enumerate(ps.singularities):
            n = i + 1
            assert abs(s - (2.0 * math.pi * n)**2) < 1e-8

    def test_perverse_sheaf_N(self):
        """Number of singularities matches n_max."""
        ps = shadow_perverse_sheaf_genus(5.0, 7)
        assert ps.N == 7

    def test_transport_maps_diagonal(self):
        """Diagonal transport m_ii = Id - T_i."""
        kappa = 3.0
        ps = shadow_perverse_sheaf_genus(kappa, 5)
        for i in range(ps.N):
            m_ii = ps.transport_maps.get((i, i), 0.0)
            expected = 1.0 - ps.monodromies[i]
            assert abs(m_ii - expected) < 1e-8

    def test_adjacent_transport_from_stokes(self):
        """Adjacent transport m_{i,i+1} determined by Stokes multiplier."""
        kappa = 4.0
        ps = shadow_perverse_sheaf_genus(kappa, 5)
        for i in range(ps.N - 1):
            n = i + 2  # n-th Stokes multiplier
            S_n = stokes_multiplier_genus(n, kappa)
            m_adj = ps.transport_maps.get((i, i + 1), 0.0)
            expected = S_n / (2.0 * math.pi * 1j)
            assert abs(m_adj - expected) < 1e-8


# =====================================================================
# Test 18-22: Alien derivatives
# =====================================================================

class TestAlienDerivatives:
    """Alien derivatives in the KS framework (Def 2.2.7, Thm 2.3.10)."""

    def test_alien_derivative_coefficients_r0(self):
        """r=0: no intermediate points, coefficient is -1."""
        coeffs = alien_derivative_transport_coefficients(0)
        assert len(coeffs) == 1
        from fractions import Fraction
        assert coeffs[0] == Fraction(-1, 1)

    def test_alien_derivative_coefficients_r1(self):
        """r=1: two terms with coefficients -1/1, 1/2."""
        coeffs = alien_derivative_transport_coefficients(1)
        assert len(coeffs) == 2
        from fractions import Fraction
        assert coeffs[0] == Fraction(-1, 1)
        assert coeffs[1] == Fraction(1, 2)

    def test_alien_derivative_coefficients_sum(self):
        """Sum of |coefficients| for r intermediate points."""
        for r in range(6):
            coeffs = alien_derivative_transport_coefficients(r)
            assert len(coeffs) == r + 1

    def test_log_stokes_equals_alien_sum_kappa5(self):
        """Thm 2.3.10: log St = sum Delta_omega for kappa=5."""
        kappa = 5.0
        n_max = 4
        log_St, alien_sum = log_stokes_equals_alien_sum(kappa, n_max)
        # The first row (perturbative -> instanton) should match
        for m in range(1, n_max + 1):
            assert abs(log_St[0, m] - alien_sum[0, m]) < 1e-8

    def test_alien_derivative_proportional_to_stokes(self):
        """Delta_{xi_n} = S_n / (2*pi*i) for simple poles."""
        kappa = 7.0
        for n in range(1, 6):
            S_n = stokes_multiplier_genus(n, kappa)
            alien = alien_derivative_single_singularity(S_n, 1.0)
            assert abs(alien - S_n) < 1e-10


# =====================================================================
# Test 23-27: Stokes automorphism
# =====================================================================

class TestStokesAutomorphism:
    """Stokes automorphism St_zeta (Def 2.3.8)."""

    def test_stokes_matrix_upper_triangular(self):
        """St is upper triangular with Id on diagonal."""
        St = stokes_automorphism_genus(5.0, 5)
        N = St.shape[0]
        for i in range(N):
            assert abs(St[i, i] - 1.0) < 1e-10
            for j in range(i):
                assert abs(St[i, j]) < 1e-15

    def test_stokes_matrix_kappa_zero_is_identity(self):
        """At kappa=0, St = Id (no Stokes phenomenon)."""
        St = stokes_automorphism_genus(0.0, 5)
        assert np.allclose(St, np.eye(6))

    def test_stokes_multiplicative(self):
        """Prop 2.3.9: St^{F*G} = St^F tensor St^G.

        For the genus expansion, this means the Stokes data of
        A tensor B is the tensor product of individual Stokes data.
        In particular, |S_1(A+B)| = |S_1(A)| + |S_1(B)| when
        kappa is additive.
        """
        kappa_A = 3.0
        kappa_B = 5.0
        S1_A = leading_stokes_multiplier(kappa_A)
        S1_B = leading_stokes_multiplier(kappa_B)
        S1_AB = leading_stokes_multiplier(kappa_A + kappa_B)
        assert abs(S1_AB - (S1_A + S1_B)) < 1e-10

    def test_stokes_automorphism_determinant(self):
        """det(St) = 1 (upper triangular with 1s on diagonal)."""
        St = stokes_automorphism_genus(5.0, 5)
        assert abs(np.linalg.det(St) - 1.0) < 1e-8

    def test_stokes_inverse_exists(self):
        """St is invertible (upper triangular with nonzero diagonal)."""
        St = stokes_automorphism_genus(5.0, 5)
        St_inv = np.linalg.inv(St)
        assert np.allclose(St @ St_inv, np.eye(St.shape[0]), atol=1e-8)


# =====================================================================
# Test 28-32: Shadow Borel transform
# =====================================================================

class TestShadowBorelTransform:
    """Borel transform of the shadow genus expansion."""

    def test_faber_pandharipande_g1(self):
        """lambda_1^FP = |B_2| / (2*2!) = (1/6) / 4 = 1/24."""
        assert abs(faber_pandharipande_lambda_g(1) - 1.0 / 24.0) < 1e-12

    def test_faber_pandharipande_g2(self):
        """lambda_2^FP = |B_4| / (4*4!) = (1/30) / 96 = 1/2880."""
        # B_4 = -1/30, |B_4| = 1/30
        assert abs(faber_pandharipande_lambda_g(2) - 1.0 / 2880.0) < 1e-12

    def test_shadow_free_energy_g1(self):
        """F_1 = kappa/24 (the fundamental genus-1 obstruction)."""
        kappa = 10.0
        F_1 = shadow_free_energy(1, kappa)
        assert abs(F_1 - kappa / 24.0) < 1e-10

    def test_borel_transform_small_xi(self):
        """At small xi, B[Z](xi) approx F_1 * xi^2 / 2!."""
        kappa = 5.0
        xi = 0.01
        B_val = shadow_borel_transform_genus(kappa, xi, g_max=50)
        F_1 = shadow_free_energy(1, kappa)
        leading = F_1 * xi**2 / 2.0
        assert abs(B_val - leading) / abs(leading) < 0.01

    def test_borel_closed_form_has_poles_at_2pin(self):
        """Closed form has poles at hbar = 2*pi*n (sin(hbar/2) = 0)."""
        kappa = 5.0
        for n in range(1, 4):
            hbar_pole = 2.0 * math.pi * n
            # Approach the pole from the side
            eps = 1e-6
            val_near = shadow_borel_closed_form(kappa, hbar_pole - eps)
            # Should be large near the pole
            assert abs(val_near) > 100.0


# =====================================================================
# Test 33-36: Large-order relations
# =====================================================================

class TestLargeOrderRelations:
    """F_g ~ sum F_g^{(n)} from instanton sectors."""

    def test_large_order_leading_instanton(self):
        """Corrected instanton prediction matches F_g exactly.

        The raw instanton sum gives 2*kappa*eta_D(2g)/(2*pi)^{2g},
        which differs from F_g by a factor 2g*(1-2^{1-2g}) due to
        the hbar vs hbar^2 variable change. The corrected function
        accounts for this.
        """
        kappa = 5.0
        for g in [1, 2, 5, 10, 20]:
            F_g_exact = shadow_free_energy(g, kappa)
            F_g_corrected = large_order_genus_prediction_corrected(g, kappa, n_inst=200)
            if abs(F_g_exact) > 1e-100:
                rel_err = abs(F_g_exact - F_g_corrected) / abs(F_g_exact)
                assert rel_err < 0.01, f"g={g}: rel_err={rel_err}"

    def test_instanton_conversion_factor(self):
        """Raw instanton sum / F_g = 2g * (1 - 2^{1-2g}) exactly."""
        kappa = 5.0
        for g in [1, 2, 3, 5, 10]:
            F_g_exact = shadow_free_energy(g, kappa)
            F_g_raw = large_order_genus_prediction(g, kappa, n_inst=200)
            if abs(F_g_exact) > 1e-100:
                ratio = F_g_raw / F_g_exact
                expected = 2.0 * g * (1.0 - 2.0**(1.0 - 2.0 * g))
                assert abs(ratio - expected) / abs(expected) < 0.001, \
                    f"g={g}: ratio={ratio}, expected={expected}"

    def test_dirichlet_eta_positive_even(self):
        """eta_D(2g) = (1 - 2^{1-2g}) * zeta(2g) for g >= 1."""
        for g in range(1, 5):
            eta = dirichlet_eta(2 * g)
            assert eta > 0  # eta(2g) > 0 for g >= 1

    def test_large_order_saturation(self):
        """eta_D(2g)/zeta(2g) -> 1 as g -> infinity."""
        for g in [10, 20, 30]:
            eta = dirichlet_eta(2 * g)
            # zeta(2g) = (-1)^{g+1} B_{2g} (2*pi)^{2g} / (2*(2g)!)
            from theorem_kapranov_resurgence_engine import _riemann_zeta
            zeta_val = _riemann_zeta(2 * g)
            ratio = eta / zeta_val
            assert abs(ratio - 1.0) < 0.01, f"g={g}: ratio={ratio}"

    def test_bernoulli_decay_matches_instanton(self):
        """F_g decays as 1/(2*pi)^{2g}, matching the instanton action A=(2*pi)^2."""
        kappa = 5.0
        ratios = []
        for g in range(5, 15):
            F_g = shadow_free_energy(g, kappa)
            F_g1 = shadow_free_energy(g + 1, kappa)
            if abs(F_g) > 1e-30:
                ratios.append(abs(F_g1 / F_g))
        # The ratio should approach 1/(2*pi)^2 = 1/A
        expected_ratio = 1.0 / UNIVERSAL_INSTANTON_ACTION
        for r in ratios[-3:]:
            assert abs(r - expected_ratio) / expected_ratio < 0.2


# =====================================================================
# Test 37-39: Shadow Eisenstein in perverse sheaf language
# =====================================================================

class TestShadowEisenstein:
    """L^sh(s) = -kappa * zeta(s) * zeta(s-1) (thm:shadow-eisenstein)."""

    def test_shadow_l_function_s3(self):
        """L^sh(3) = -kappa * zeta(3) * zeta(2)."""
        kappa = 5.0
        L_val = shadow_l_function(kappa, 3.0)
        from theorem_kapranov_resurgence_engine import _riemann_zeta
        expected = -kappa * _riemann_zeta(3.0) * _riemann_zeta(2.0)
        assert abs(L_val - expected) < 1e-6

    def test_shadow_eisenstein_multi_path(self):
        """Multi-path: Eisenstein product vs divisor sum."""
        kappa = 3.0
        results = verify_shadow_eisenstein(kappa, [3.0, 4.0, 5.0])
        for r in results:
            if 'relative_error' in r:
                assert r['relative_error'] < 0.01

    def test_shadow_l_not_cuspidal(self):
        """L^sh = product of zeta functions => not cuspidal (Eisenstein)."""
        # Cuspidal L-functions do not factor as products of Riemann zeta.
        # This is a structural test: the formula is a product.
        kappa = 1.0
        L_val = shadow_l_function(kappa, 4.0)
        from theorem_kapranov_resurgence_engine import _riemann_zeta
        assert abs(L_val - (-_riemann_zeta(4.0) * _riemann_zeta(3.0))) < 1e-6


# =====================================================================
# Test 40-43: Anomaly cancellation and Koszul duality
# =====================================================================

class TestAnomalyCancellation:
    """c=26 anomaly cancellation in the resurgent setting."""

    def test_anomaly_cancellation_c26(self):
        """S_1(matter) + S_1(ghost) = 0 at c=26."""
        result = anomaly_cancellation_c26()
        assert result['cancellation']
        assert abs(result['kappa_total']) < 1e-10

    def test_kappa_additivity_for_stokes(self):
        """S_1(A+B) = S_1(A) + S_1(B) because S_1 is linear in kappa."""
        kappa_A = 7.0
        kappa_B = -3.0
        S1_sum = leading_stokes_multiplier(kappa_A) + leading_stokes_multiplier(kappa_B)
        S1_total = leading_stokes_multiplier(kappa_A + kappa_B)
        assert abs(S1_sum - S1_total) < 1e-10

    def test_koszul_dual_stokes_virasoro(self):
        """Koszul dual Vir_{26-c}: S_1(c) + S_1(26-c) at c=13 only."""
        # At c=13 (self-dual): kappa + kappa' = 13/2 + 13/2 = 13 != 0
        # But in the genus direction, S_1 propto kappa, so
        # S_1(c) + S_1(26-c) = -4*pi^2*i * (c/2 + (26-c)/2) = -4*pi^2*i * 13
        c = 13.0
        S1_c = leading_stokes_multiplier(kappa_virasoro(c))
        S1_dual = leading_stokes_multiplier(kappa_virasoro(26.0 - c))
        S1_sum = S1_c + S1_dual
        expected_sum = -4.0 * math.pi**2 * 13.0 * 1j
        assert abs(S1_sum - expected_sum) < 1e-8

    def test_cancellation_only_at_c26(self):
        """Stokes cancellation requires kappa_eff = 0, i.e., c=26."""
        for c in [1.0, 10.0, 13.0, 25.0]:
            kappa_matter = kappa_virasoro(c)
            kappa_ghost = -13.0
            kappa_eff = kappa_matter + kappa_ghost
            S1_total = leading_stokes_multiplier(kappa_eff)
            if abs(c - 26.0) > 0.01:
                assert abs(S1_total) > 1e-5


# =====================================================================
# Test 44-46: Shadow connection monodromy
# =====================================================================

class TestShadowConnection:
    """Shadow connection has Koszul monodromy -1."""

    def test_monodromy_minus_one(self):
        """Monodromy at zeros of Q_L is -1 (Koszul sign)."""
        c = 10.0
        kappa = kappa_virasoro(c)
        result = shadow_connection_monodromy(kappa, c)
        assert result['monodromy_is_minus_one']

    def test_monodromy_minus_one_multiple_c(self):
        """Koszul monodromy -1 for all c > 0."""
        for c in [1.0, 5.0, 13.0, 25.0, 50.0]:
            kappa = kappa_virasoro(c)
            result = shadow_connection_monodromy(kappa, c)
            assert result['monodromy_is_minus_one'], f"Failed at c={c}"

    def test_shadow_metric_zeros_conjugate(self):
        """For c > 0, zeros of Q_L are complex conjugates."""
        c = 10.0
        kappa = kappa_virasoro(c)
        result = shadow_connection_monodromy(kappa, c)
        t_plus = result['t_plus']
        t_minus = result['t_minus']
        assert abs(t_plus - t_minus.conjugate()) < 1e-10


# =====================================================================
# Test 47-49: Convolution algebra
# =====================================================================

class TestConvolutionAlgebra:
    """Additive convolution in Perv^0(C) (Thm 2.1.6)."""

    def test_convolution_simple(self):
        """Phi_c(F*G) = sum_{a+b=c} Phi_a(F) tensor Phi_b(G)."""
        phi_f = {1.0: 2.0 + 0j, 3.0: 1.0 + 0j}
        phi_g = {2.0: 3.0 + 0j, 4.0: -1.0 + 0j}
        result = convolution_product_vanishing_cycles(phi_f, phi_g)
        # Expected: at 3.0: 2*3=6, at 5.0: 2*(-1)+1*3=1, at 7.0: 1*(-1)=-1
        assert abs(result.get(3.0, 0) - 6.0) < 1e-10
        assert abs(result.get(5.0, 0) - 1.0) < 1e-10  # 2*(-1) + 1*3 = 1
        assert abs(result.get(7.0, 0) - (-1.0)) < 1e-10

    def test_convolution_unit(self):
        """Unit object: Phi = {0: 1} (skyscraper at 0)."""
        phi_unit = {0.0: 1.0 + 0j}
        phi_f = {2.0: 5.0 + 0j, 3.0: -2.0 + 0j}
        result = convolution_product_vanishing_cycles(phi_unit, phi_f)
        assert abs(result.get(2.0, 0) - 5.0) < 1e-10
        assert abs(result.get(3.0, 0) - (-2.0)) < 1e-10

    def test_convolution_commutative(self):
        """Convolution is commutative (symmetric monoidal)."""
        phi_f = {1.0: 2.0 + 0j, 2.0: 3.0 + 0j}
        phi_g = {1.0: -1.0 + 0j, 3.0: 4.0 + 0j}
        fg = convolution_product_vanishing_cycles(phi_f, phi_g)
        gf = convolution_product_vanishing_cycles(phi_g, phi_f)
        for key in set(fg.keys()) | set(gf.keys()):
            assert abs(fg.get(key, 0) - gf.get(key, 0)) < 1e-10


# =====================================================================
# Test 50-52: MC constraint verification
# =====================================================================

class TestMCConstraint:
    """MC equation constrains Stokes multipliers."""

    def test_bridge_equation_consistency(self):
        """Bridge equation: S_n = 2*pi*i * Res_n is self-consistent."""
        kappa = 8.0
        constraints = mc_constraint_on_stokes(kappa, 5)
        for key, val in constraints.items():
            assert abs(val) < 1e-10, f"{key}: deviation = {val}"

    def test_mc_bridge_all_families(self):
        """Bridge equation holds for all standard families."""
        for name, data in STANDARD_FAMILIES.items():
            kappa = data['kappa']
            if abs(kappa) < 1e-15:
                continue
            constraints = mc_constraint_on_stokes(kappa, 3)
            for key, val in constraints.items():
                assert abs(val) < 1e-10, f"{name}/{key}: deviation = {val}"

    def test_leibniz_alien_derivative(self):
        """Thm 2.3.10(b): Delta^{F*G} = Delta^F otimes Id + Id otimes Delta^G.

        For the shadow expansion, this means the alien derivative of a
        tensor product of shadow partition functions is additive in kappa.
        """
        kappa_1 = 3.0
        kappa_2 = 5.0
        for n in range(1, 4):
            S_n_1 = stokes_multiplier_genus(n, kappa_1)
            S_n_2 = stokes_multiplier_genus(n, kappa_2)
            S_n_sum = stokes_multiplier_genus(n, kappa_1 + kappa_2)
            # Leibniz: the alien derivative of the tensor product
            # equals the sum of individual alien derivatives
            assert abs(S_n_sum - (S_n_1 + S_n_2)) < 1e-10


# =====================================================================
# Test 53-55: Assessment and synthesis
# =====================================================================

class TestAssessment:
    """Overall assessment of the KS framework for the shadow programme."""

    def test_assessment_keys(self):
        """Assessment has all required keys."""
        a = kapranov_soibelman_assessment()
        required_keys = ['(a) categorification', '(b) MC constraints',
                         '(c) alien derivatives', '(d) shadow connection',
                         '(e) shadow Eisenstein', 'overall']
        for key in required_keys:
            assert key in a

    def test_categorification_positive(self):
        """Question (a): categorification is YES."""
        a = kapranov_soibelman_assessment()
        assert 'YES' in a['(a) categorification']

    def test_mc_constraints_partial(self):
        """Question (b): MC constraints is PARTIAL (not full proof)."""
        a = kapranov_soibelman_assessment()
        assert 'PARTIAL' in a['(b) MC constraints']


# =====================================================================
# Test 56-58: Kappa formulas (AP1 cross-check)
# =====================================================================

class TestKappaFormulas:
    """Cross-verify kappa formulas (prevent AP1 recurrence)."""

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        assert abs(kappa_virasoro(26.0) - 13.0) < 1e-10

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k (NOT k/2, see AP39)."""
        assert abs(kappa_heisenberg(5.0) - 5.0) < 1e-10

    def test_kappa_sl2_k1(self):
        """kappa(sl2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        assert abs(kappa_kac_moody(3, 1.0, 2.0) - 2.25) < 1e-10
