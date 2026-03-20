#!/usr/bin/env python3
"""
Tests for the Verdier-Hecke bridge (Step 3 of the five-step proof strategy).

Verifies that the Verdier involution on self-dual algebras forces
partition functions to decompose into Hecke eigenforms via multiplicity one.

60+ tests across 10 test classes covering:
  1. Modular form q-expansions (theta, Eisenstein, eta, Delta)
  2. Hecke operator action on standard forms
  3. Verdier involution properties (self-duality detection, action)
  4. E_4 = theta_{E_8} eigenform verification
  5. Delta eigenform verification (weight 12)
  6. Leech lattice decomposition
  7. Weight 24 analysis (dim S_24 = 2, Delta^2 NOT an eigenform)
  8. Virasoro self-duality (c=13 vs c != 13)
  9. Verdier-Hecke commutation
  10. Obstruction analysis and the universal mechanism
"""

import pytest
import numpy as np

from compute.lib.verdier_hecke_bridge import (
    # Arithmetic
    sigma_k, sigma_3, sigma_7, sigma_11,
    tau_ramanujan, ramanujan_tau_batch,
    # Modular forms
    theta3_qexp, eta_qexp, eta_power_qexp,
    eisenstein_qexp, delta_qexp,
    theta_Zr_qexp, theta_E8_qexp, theta_Leech_qexp,
    _poly_mul,
    # Verdier
    VerdierInvolution, verdier_involution_lattice,
    # Hecke
    hecke_operator_qexp, hecke_eigenvalue,
    is_hecke_eigenform,
    # Commutation
    verdier_hecke_commutation_check,
    # Multiplicity one
    cusp_form_dimension, modular_form_dimension,
    multiplicity_one_holds, eigenform_decomposition_forced,
    # Weight 24
    weight24_eigenform_basis, weight24_hecke_matrix,
    weight24_hecke_eigenvalues, eta48_is_eigenform,
    # Virasoro
    virasoro_partition_function_weight, virasoro_selfdual_analysis,
    virasoro_c25_analysis,
    # Lattice
    verify_E4_is_eigenform, verify_Delta_is_eigenform,
    verify_Leech_decomposition,
    # Universal mechanism
    self_duality_forces_eigenform, obstruction_catalog,
    # Ising
    ising_level_structure,
    # Summary
    step3_summary,
)


NMAX = 50  # Truncation depth for q-expansions


# ===================================================================
# 1. Modular form q-expansions
# ===================================================================

class TestModularFormQExpansions:

    def test_theta3_constant_term(self):
        """theta_3 = 1 + 2q + 2q^4 + 2q^9 + ..., so a_0 = 1."""
        coeffs = theta3_qexp(20)
        assert coeffs[0] == 1

    def test_theta3_first_few(self):
        """theta_3 coefficients: a_1=2, a_2=0, a_3=0, a_4=2."""
        coeffs = theta3_qexp(20)
        assert coeffs[1] == 2
        assert coeffs[2] == 0
        assert coeffs[3] == 0
        assert coeffs[4] == 2

    def test_theta3_representation_count(self):
        """a_n = r_1(n) = number of ways n = m^2 for m in Z (with sign)."""
        coeffs = theta3_qexp(100)
        # a_9 = 2 (from m = +-3)
        assert coeffs[9] == 2
        # a_25 = 2 (from m = +-5)
        assert coeffs[25] == 2
        # a_6 = 0 (6 is not a perfect square)
        assert coeffs[6] == 0

    def test_eta_constant_term(self):
        """eta = q^{1/24} prod(1-q^k), so the product part has a_0 = 1."""
        coeffs = eta_qexp(20)
        assert coeffs[0] == 1

    def test_eta_pentagonal_theorem(self):
        """
        prod(1-q^k) = sum_{n=-inf}^{inf} (-1)^n q^{n(3n-1)/2}
        (Euler's pentagonal number theorem).
        Nonzero at m = k(3k-1)/2: m=0,1,2,5,7,12,...
        """
        coeffs = eta_qexp(20)
        assert coeffs[0] == 1
        assert coeffs[1] == -1
        assert coeffs[2] == -1
        assert coeffs[3] == 0
        assert coeffs[4] == 0
        assert coeffs[5] == 1
        assert coeffs[7] == 1

    def test_eisenstein_E4_constant(self):
        """E_4 = 1 + 240q + 2160q^2 + ..."""
        e4 = eisenstein_qexp(4, 10)
        assert abs(e4[0] - 1.0) < 1e-10

    def test_eisenstein_E4_first_coeff(self):
        """E_4: a_1 = 240."""
        e4 = eisenstein_qexp(4, 10)
        assert abs(e4[1] - 240.0) < 1e-6

    def test_eisenstein_E4_second_coeff(self):
        """E_4: a_2 = 2160 = 240*(1+8) = 240*sigma_3(2)."""
        e4 = eisenstein_qexp(4, 10)
        assert abs(e4[2] - 2160.0) < 1e-6

    def test_eisenstein_E6_first_coeff(self):
        """E_6: a_1 = -504."""
        e6 = eisenstein_qexp(6, 10)
        assert abs(e6[1] - (-504.0)) < 1e-6

    def test_delta_leading_coeff(self):
        """Delta = q - 24q^2 + 252q^3 - ..., so a_0 = 0, a_1 = 1."""
        d = delta_qexp(10)
        assert abs(d[0]) < 1e-10
        assert abs(d[1] - 1.0) < 1e-10

    def test_delta_tau2(self):
        """tau(2) = -24."""
        d = delta_qexp(10)
        assert abs(d[2] - (-24.0)) < 1e-6

    def test_delta_tau3(self):
        """tau(3) = 252."""
        d = delta_qexp(10)
        assert abs(d[3] - 252.0) < 1e-6

    def test_delta_tau4(self):
        """tau(4) = -1472."""
        d = delta_qexp(10)
        assert abs(d[4] - (-1472.0)) < 1e-6

    def test_delta_tau5(self):
        """tau(5) = 4830."""
        d = delta_qexp(10)
        assert abs(d[5] - 4830.0) < 1e-6


# ===================================================================
# 2. Arithmetic functions
# ===================================================================

class TestArithmeticFunctions:

    def test_sigma3_prime(self):
        """sigma_3(2) = 1 + 8 = 9."""
        assert sigma_3(2) == 9

    def test_sigma3_3(self):
        """sigma_3(3) = 1 + 27 = 28."""
        assert sigma_3(3) == 28

    def test_sigma3_4(self):
        """sigma_3(4) = 1 + 8 + 64 = 73."""
        assert sigma_3(4) == 73

    def test_sigma3_5(self):
        """sigma_3(5) = 1 + 125 = 126."""
        assert sigma_3(5) == 126

    def test_sigma7_2(self):
        """sigma_7(2) = 1 + 128 = 129."""
        assert sigma_7(2) == 129

    def test_sigma11_2(self):
        """sigma_11(2) = 1 + 2048 = 2049."""
        assert sigma_11(2) == 2049

    def test_ramanujan_tau_1(self):
        """tau(1) = 1."""
        assert tau_ramanujan(1) == 1

    def test_ramanujan_tau_2(self):
        """tau(2) = -24."""
        assert tau_ramanujan(2) == -24

    def test_ramanujan_tau_3(self):
        """tau(3) = 252."""
        assert tau_ramanujan(3) == 252

    def test_ramanujan_tau_5(self):
        """tau(5) = 4830."""
        assert tau_ramanujan(5) == 4830

    def test_ramanujan_tau_batch(self):
        """Batch computation matches individual."""
        batch = ramanujan_tau_batch(10)
        assert batch[0] == 1      # tau(1)
        assert batch[1] == -24    # tau(2)
        assert batch[2] == 252    # tau(3)

    def test_ramanujan_tau_multiplicative(self):
        """tau is multiplicative: tau(mn) = tau(m)*tau(n) for gcd(m,n)=1."""
        batch = ramanujan_tau_batch(20)
        # tau(6) = tau(2)*tau(3) = -24*252 = -6048
        assert batch[5] == batch[1] * batch[2]  # tau(6) = tau(2)*tau(3)
        # tau(10) = tau(2)*tau(5)
        assert batch[9] == batch[1] * batch[4]  # tau(10) = tau(2)*tau(5)


# ===================================================================
# 3. Hecke operators
# ===================================================================

class TestHeckeOperators:

    def test_T2_on_E4(self):
        """T_2(E_4) = sigma_3(2) * E_4 = 9 * E_4."""
        e4 = eisenstein_qexp(4, NMAX)
        T2_e4 = hecke_operator_qexp(e4, 2, 4, NMAX)
        # Check proportionality: T2_e4[i] / e4[i] = 9 for all nonzero e4[i]
        for i in [0, 1, 2, 3]:
            if abs(e4[i]) > 1e-10:
                ratio = T2_e4[i] / e4[i]
                assert abs(ratio - 9.0) < 1e-6, f"At i={i}: ratio={ratio}, expected 9"

    def test_T3_on_E4(self):
        """T_3(E_4) = sigma_3(3) * E_4 = 28 * E_4."""
        e4 = eisenstein_qexp(4, NMAX)
        T3_e4 = hecke_operator_qexp(e4, 3, 4, NMAX)
        for i in [0, 1, 2]:
            if abs(e4[i]) > 1e-10:
                ratio = T3_e4[i] / e4[i]
                assert abs(ratio - 28.0) < 1e-6, f"At i={i}: ratio={ratio}, expected 28"

    def test_T5_on_E4(self):
        """T_5(E_4) = sigma_3(5) * E_4 = 126 * E_4."""
        e4 = eisenstein_qexp(4, NMAX)
        T5_e4 = hecke_operator_qexp(e4, 5, 4, NMAX)
        for i in [0, 1]:
            if abs(e4[i]) > 1e-10:
                ratio = T5_e4[i] / e4[i]
                assert abs(ratio - 126.0) < 1e-6

    def test_T2_on_Delta(self):
        """T_2(Delta) = tau(2) * Delta = -24 * Delta."""
        d = delta_qexp(NMAX)
        T2_d = hecke_operator_qexp(d, 2, 12, NMAX)
        # Delta has a_1 = 1, so T_2(Delta)[1] / Delta[1] = tau(2) = -24
        ratio = T2_d[1] / d[1]
        assert abs(ratio - (-24.0)) < 1e-6

    def test_T3_on_Delta(self):
        """T_3(Delta) = tau(3) * Delta = 252 * Delta."""
        d = delta_qexp(NMAX)
        T3_d = hecke_operator_qexp(d, 3, 12, NMAX)
        ratio = T3_d[1] / d[1]
        assert abs(ratio - 252.0) < 1e-6

    def test_T5_on_Delta(self):
        """T_5(Delta) = tau(5) * Delta = 4830 * Delta."""
        d = delta_qexp(NMAX)
        T5_d = hecke_operator_qexp(d, 5, 12, NMAX)
        ratio = T5_d[1] / d[1]
        assert abs(ratio - 4830.0) < 1e-4

    def test_E4_is_eigenform(self):
        """E_4 is a Hecke eigenform for all T_p."""
        e4 = eisenstein_qexp(4, NMAX)
        is_eigen, eigenvals = is_hecke_eigenform(e4, 4, [2, 3, 5, 7], NMAX)
        assert is_eigen
        assert abs(eigenvals[2] - sigma_3(2)) < 1e-6
        assert abs(eigenvals[3] - sigma_3(3)) < 1e-6

    def test_Delta_is_eigenform(self):
        """Delta is a Hecke eigenform for all T_p."""
        d = delta_qexp(NMAX)
        is_eigen, eigenvals = is_hecke_eigenform(d, 12, [2, 3, 5], NMAX)
        assert is_eigen
        assert abs(eigenvals[2] - (-24.0)) < 1e-6
        assert abs(eigenvals[3] - 252.0) < 1e-6


# ===================================================================
# 4. Verdier involution
# ===================================================================

class TestVerdierInvolution:

    def test_lattice_E8_self_dual(self):
        """E_8 lattice is self-dual."""
        sigma = verdier_involution_lattice('E8')
        assert sigma.is_self_dual()

    def test_lattice_Leech_self_dual(self):
        """Leech lattice is self-dual."""
        sigma = verdier_involution_lattice('Leech')
        assert sigma.is_self_dual()

    def test_lattice_Z_selfdual(self):
        """Z at R=1 is self-dual."""
        sigma = verdier_involution_lattice('Z_selfdual')
        assert sigma.is_self_dual()

    def test_virasoro_c13_self_dual(self):
        """Vir_{c=13} is self-dual: Vir_c^! = Vir_{26-c} = Vir_13."""
        sigma = VerdierInvolution('virasoro', c=13)
        assert sigma.is_self_dual()

    def test_virasoro_c1_not_self_dual(self):
        """Vir_{c=1} is NOT self-dual: Vir_1^! = Vir_25."""
        sigma = VerdierInvolution('virasoro', c=1)
        assert not sigma.is_self_dual()

    def test_virasoro_c25_not_self_dual(self):
        """Vir_{c=25} is NOT self-dual: Vir_25^! = Vir_1."""
        sigma = VerdierInvolution('virasoro', c=25)
        assert not sigma.is_self_dual()

    def test_virasoro_c26_not_self_dual(self):
        """Vir_{c=26} has Vir_26^! = Vir_0, not self-dual."""
        sigma = VerdierInvolution('virasoro', c=26)
        assert not sigma.is_self_dual()

    def test_free_boson_R1_self_dual(self):
        """Free boson at R=1 is self-dual (T-duality)."""
        sigma = VerdierInvolution('free_boson', R=1.0)
        assert sigma.is_self_dual()

    def test_free_boson_R2_not_self_dual(self):
        """Free boson at R=2 is not self-dual (T-dual is R=1/2)."""
        sigma = VerdierInvolution('free_boson', R=2.0)
        assert not sigma.is_self_dual()

    def test_sigma_fixes_Z_when_selfdual(self):
        """For self-dual A, sigma(Z_A) = Z_A."""
        sigma = verdier_involution_lattice('E8')
        e4 = eisenstein_qexp(4, 20)
        result = sigma.acts_on_partition_function(e4)
        assert result is not None
        for i in range(len(e4)):
            assert abs(result[i] - e4[i]) < 1e-10

    def test_sigma_is_none_when_not_selfdual(self):
        """For non-self-dual A, sigma maps Z_A to Z_{A!} (cannot compute from Z_A alone)."""
        sigma = VerdierInvolution('virasoro', c=25)
        d = delta_qexp(20)
        result = sigma.acts_on_partition_function(d)
        assert result is None

    def test_dual_central_charge_virasoro(self):
        """Vir_c^! = Vir_{26-c}."""
        sigma = VerdierInvolution('virasoro', c=7)
        assert sigma.dual_central_charge() == 19


# ===================================================================
# 5. E_4 = theta_{E_8} eigenform verification
# ===================================================================

class TestE4Eigenform:

    def test_theta_E8_equals_E4(self):
        """theta_{E_8} = E_4 (identity of modular forms)."""
        theta = theta_E8_qexp(NMAX)
        e4 = eisenstein_qexp(4, NMAX)
        for i in range(NMAX + 1):
            assert abs(theta[i] - e4[i]) < 1e-6, f"At q^{i}: theta={theta[i]}, E_4={e4[i]}"

    def test_E4_eigenvalue_T2(self):
        """T_2(E_4) = sigma_3(2)*E_4 = 9*E_4."""
        results = verify_E4_is_eigenform(NMAX)
        assert results[2]['match']
        assert abs(results[2]['expected'] - 9) < 1e-10

    def test_E4_eigenvalue_T3(self):
        """T_3(E_4) = sigma_3(3)*E_4 = 28*E_4."""
        results = verify_E4_is_eigenform(NMAX)
        assert results[3]['match']
        assert abs(results[3]['expected'] - 28) < 1e-10

    def test_E4_eigenvalue_T5(self):
        """T_5(E_4) = sigma_3(5)*E_4 = 126*E_4."""
        results = verify_E4_is_eigenform(NMAX)
        assert results[5]['match']
        assert abs(results[5]['expected'] - 126) < 1e-10

    def test_E4_eigenvalue_T7(self):
        """T_7(E_4) = sigma_3(7)*E_4 = 344*E_4."""
        results = verify_E4_is_eigenform(NMAX)
        assert results[7]['match']
        assert abs(results[7]['expected'] - 344) < 1e-10


# ===================================================================
# 6. Delta eigenform verification (weight 12)
# ===================================================================

class TestDeltaEigenform:

    def test_Delta_eigenvalue_T2(self):
        """T_2(Delta) = tau(2)*Delta = -24*Delta."""
        results = verify_Delta_is_eigenform(NMAX)
        assert results[2]['match']
        assert abs(results[2]['expected'] - (-24)) < 1e-6

    def test_Delta_eigenvalue_T3(self):
        """T_3(Delta) = tau(3)*Delta = 252*Delta."""
        results = verify_Delta_is_eigenform(NMAX)
        assert results[3]['match']
        assert abs(results[3]['expected'] - 252) < 1e-6

    def test_S12_dim_1(self):
        """dim S_12(SL(2,Z)) = 1, so any cusp form of weight 12 is a multiple of Delta."""
        assert cusp_form_dimension(12) == 1

    def test_M12_dim_2(self):
        """dim M_12(SL(2,Z)) = 2: {E_12, Delta}."""
        assert modular_form_dimension(12) == 2

    def test_weight12_multiplicity_one(self):
        """Multiplicity one trivially holds for S_12 (1-dimensional)."""
        # Any sigma-invariant function in S_12 is a scalar multiple of Delta
        assert cusp_form_dimension(12) == 1
        assert multiplicity_one_holds(1, 12)


# ===================================================================
# 7. Leech lattice decomposition
# ===================================================================

class TestLeechDecomposition:

    def test_theta_Leech_constant_term(self):
        """theta_{Leech}(q^0) = 1 (the zero vector)."""
        theta = theta_Leech_qexp(NMAX)
        assert abs(theta[0] - 1.0) < 1e-6

    def test_theta_Leech_no_roots(self):
        """Leech lattice has no roots: theta_{Leech} at q^1 = 0."""
        theta = theta_Leech_qexp(NMAX)
        assert abs(theta[1]) < 1e-6

    def test_theta_Leech_q2(self):
        """
        theta_{Leech} at q^2 = 196560 (kissing number of Leech lattice).
        E_4^3 at q^2 = (1+240+2160+...)^3 evaluated at q^2.
        Actually E_4^3: q^0=1, q^1=720, q^2=179280, ...
        720*Delta at q^2 = 720*(-24) = -17280.
        So theta_Leech at q^2 = 179280 - (-17280) = ... wait, let me just check.
        """
        theta = theta_Leech_qexp(NMAX)
        # theta_{Leech} at q^2: known to be 196560
        assert abs(theta[2] - 196560.0) < 1.0

    def test_Leech_decomposition_into_eigenforms(self):
        """theta_{Leech} = E_12 - (65520/691)*Delta: both components are eigenforms."""
        result = verify_Leech_decomposition(NMAX)
        assert result['both_eigenforms']
        assert abs(result['E12_coeff'] - 1.0) < 1e-10

    def test_Leech_E4_cubed_decomposition_error(self):
        """E_4^3 = E_12 + (432000/691)*Delta with small numerical error."""
        result = verify_Leech_decomposition(NMAX)
        assert result['e4_cubed_decomp_error'] < 1e-3

    def test_Leech_Delta_coefficient(self):
        """theta_{Leech} has Delta coefficient -65520/691."""
        result = verify_Leech_decomposition(NMAX)
        expected = -65520.0 / 691.0
        assert abs(result['Delta_coeff'] - expected) < 1e-6


# ===================================================================
# 8. Weight 24: the critical case
# ===================================================================

class TestWeight24:

    def test_S24_dimension_2(self):
        """dim S_24(SL(2,Z)) = 2."""
        assert cusp_form_dimension(24) == 2

    def test_M24_dimension_3(self):
        """dim M_24(SL(2,Z)) = 3."""
        assert modular_form_dimension(24) == 3

    def test_eta48_not_eigenform(self):
        """
        Delta^2 = eta^{48} is NOT a single Hecke eigenform (dim S_24 = 2).
        This corresponds to c=24, which is NOT self-dual (Vir_24^! = Vir_2).
        """
        is_eigen, eigenvals = eta48_is_eigenform(80)
        assert not is_eigen

    def test_weight24_two_eigenvalues_for_T2(self):
        """
        S_24 has two distinct T_2 eigenvalues.
        They are the roots of the Hecke polynomial for T_2 on S_24.
        """
        eigenvals = weight24_hecke_eigenvalues(2, 80)
        assert len(eigenvals) == 2
        # The two eigenvalues should be distinct
        assert abs(eigenvals[0] - eigenvals[1]) > 1.0

    def test_c24_not_self_dual(self):
        """c=24: Vir_24^! = Vir_2, NOT self-dual."""
        sigma = VerdierInvolution('virasoro', c=24)
        assert not sigma.is_self_dual()
        assert sigma.dual_central_charge() == 2

    def test_c25_not_self_dual(self):
        """c=25: Vir_25^! = Vir_1, NOT self-dual."""
        analysis = virasoro_c25_analysis(80)
        assert not analysis['is_self_dual']
        assert analysis['dual_c'] == 1


# ===================================================================
# 9. Virasoro self-duality
# ===================================================================

class TestVirasoroSelfDuality:

    def test_virasoro_self_dual_c13(self):
        """Vir_c^! = Vir_{26-c}. Self-dual iff c = 13."""
        analysis = virasoro_selfdual_analysis()
        assert analysis['c'] == 13
        assert analysis['is_self_dual']

    def test_virasoro_weight_equals_c(self):
        """The partition function eta^{2c} has weight c."""
        for c in [1, 7, 13, 24, 25]:
            assert virasoro_partition_function_weight(c) == c

    def test_virasoro_c13_odd_weight(self):
        """At c=13, eta^{26} has weight 13 (odd). Not a classical modular form."""
        analysis = virasoro_selfdual_analysis()
        assert analysis['weight'] == 13

    def test_virasoro_c13_eigenform_forced(self):
        """At c=13 (self-dual), eigenform decomposition is forced."""
        analysis = virasoro_selfdual_analysis()
        assert analysis['eigenform_forced']

    def test_verdier_maps_Z_to_Z_dual(self):
        """For Vir_c with c != 13: sigma maps Z_c to Z_{26-c}."""
        for c in [1, 7, 12, 25]:
            sigma = VerdierInvolution('virasoro', c=c)
            assert sigma.dual_central_charge() == 26 - c


# ===================================================================
# 10. Verdier-Hecke commutation
# ===================================================================

class TestVerdierHeckeCommutation:

    def test_commutation_E8(self):
        """sigma and T_2 commute on V_{E_8} (trivially: sigma = id)."""
        sigma = verdier_involution_lattice('E8')
        e4 = eisenstein_qexp(4, NMAX)
        commutes, _, _ = verdier_hecke_commutation_check(sigma, e4, 2, 4, NMAX)
        assert commutes

    def test_commutation_E8_T3(self):
        """sigma and T_3 commute on V_{E_8}."""
        sigma = verdier_involution_lattice('E8')
        e4 = eisenstein_qexp(4, NMAX)
        commutes, _, _ = verdier_hecke_commutation_check(sigma, e4, 3, 4, NMAX)
        assert commutes

    def test_commutation_E8_T5(self):
        """sigma and T_5 commute on V_{E_8}."""
        sigma = verdier_involution_lattice('E8')
        e4 = eisenstein_qexp(4, NMAX)
        commutes, _, _ = verdier_hecke_commutation_check(sigma, e4, 5, 4, NMAX)
        assert commutes

    def test_commutation_Leech(self):
        """sigma and T_2 commute on V_{Leech}."""
        sigma = verdier_involution_lattice('Leech')
        theta = theta_Leech_qexp(NMAX)
        commutes, _, _ = verdier_hecke_commutation_check(sigma, theta, 2, 12, NMAX)
        assert commutes

    def test_commutation_Leech_T3(self):
        """sigma and T_3 commute on V_{Leech}."""
        sigma = verdier_involution_lattice('Leech')
        theta = theta_Leech_qexp(NMAX)
        commutes, _, _ = verdier_hecke_commutation_check(sigma, theta, 3, 12, NMAX)
        assert commutes

    def test_commutation_non_selfdual_returns_none(self):
        """For non-self-dual, commutation check returns None."""
        sigma = VerdierInvolution('virasoro', c=25)
        d = delta_qexp(20)
        result = verdier_hecke_commutation_check(sigma, d, 2, 12, 20)
        assert result[0] is None


# ===================================================================
# 11. Multiplicity one and dimension formulas
# ===================================================================

class TestMultiplicityOne:

    def test_cusp_dim_k_less_12(self):
        """No cusp forms of weight < 12 for SL(2,Z)."""
        for k in range(2, 12, 2):
            assert cusp_form_dimension(k) == 0

    def test_cusp_dim_12(self):
        assert cusp_form_dimension(12) == 1

    def test_cusp_dim_16(self):
        """dim S_16 = 1."""
        assert cusp_form_dimension(16) == 1

    def test_cusp_dim_20(self):
        """dim S_20 = 1."""
        assert cusp_form_dimension(20) == 1

    def test_cusp_dim_22(self):
        """dim S_22 = 1."""
        assert cusp_form_dimension(22) == 1

    def test_cusp_dim_24(self):
        """dim S_24 = 2."""
        assert cusp_form_dimension(24) == 2

    def test_cusp_dim_26(self):
        """dim S_26 = 1 (only one monomial E_4^a E_6^b Delta gives weight 26 cusp form)."""
        assert cusp_form_dimension(26) == 1

    def test_cusp_dim_36(self):
        """dim S_36 = 3."""
        assert cusp_form_dimension(36) == 3

    def test_modular_dim_0(self):
        """dim M_0 = 1 (just constants)."""
        assert modular_form_dimension(0) == 1

    def test_modular_dim_2(self):
        """dim M_2 = 0 (no nonzero forms of weight 2)."""
        assert modular_form_dimension(2) == 0

    def test_modular_dim_4(self):
        """dim M_4 = 1 (just E_4)."""
        assert modular_form_dimension(4) == 1

    def test_multiplicity_one_SL2Z(self):
        """Multiplicity one holds for SL(2,Z) at any weight."""
        assert multiplicity_one_holds(1, 12)
        assert multiplicity_one_holds(1, 24)


# ===================================================================
# 12. Universal mechanism and obstructions
# ===================================================================

class TestUniversalMechanism:

    def test_selfdual_lattice_forced(self):
        """Self-dual lattice: eigenform decomposition is forced."""
        result = self_duality_forces_eigenform('lattice', self_dual=True, rank=8)
        assert result['is_self_dual']
        assert result['eigenform_forced']

    def test_non_selfdual_not_forced(self):
        """Non-self-dual algebra: eigenform decomposition is NOT forced."""
        result = self_duality_forces_eigenform('virasoro', c=25)
        assert not result['is_self_dual']
        assert not result['eigenform_forced']

    def test_virasoro_c13_forced(self):
        """Virasoro at c=13: self-dual, eigenform decomposition forced."""
        result = self_duality_forces_eigenform('virasoro', c=13)
        assert result['is_self_dual']
        assert result['eigenform_forced']

    def test_obstruction_catalog_nonempty(self):
        """The obstruction catalog has at least 4 entries."""
        obstructions = obstruction_catalog()
        assert len(obstructions) >= 4

    def test_obstruction_severity_levels(self):
        """Obstruction catalog contains both fatal and non-fatal entries."""
        obstructions = obstruction_catalog()
        severities = {o['severity'] for o in obstructions}
        assert 'fatal' in severities
        assert 'moderate' in severities or 'serious' in severities

    def test_eigenform_decomposition_selfdual(self):
        """eigenform_decomposition_forced returns True for self-dual + SL(2,Z)."""
        result = eigenform_decomposition_forced(True, 1, 12)
        assert result['forced']
        assert result['obstruction'] is None

    def test_eigenform_decomposition_not_selfdual(self):
        """eigenform_decomposition_forced returns False for non-self-dual."""
        result = eigenform_decomposition_forced(False, 1, 12)
        assert not result['forced']


# ===================================================================
# 13. Ising model
# ===================================================================

class TestIsingModel:

    def test_ising_central_charge(self):
        """Ising model has c = 1/2."""
        info = ising_level_structure()
        assert abs(info['c'] - 0.5) < 1e-10

    def test_ising_num_primaries(self):
        """Ising model has 3 primary fields."""
        info = ising_level_structure()
        assert info['num_primaries'] == 3

    def test_ising_not_chirally_self_dual(self):
        """Ising model is NOT chirally self-dual."""
        info = ising_level_structure()
        assert not info['self_dual_chiral']

    def test_ising_has_diagonal_invariant(self):
        """Ising model has a diagonal modular invariant."""
        info = ising_level_structure()
        assert info['diagonal_invariant']


# ===================================================================
# 14. Step 3 summary
# ===================================================================

class TestStep3Summary:

    def test_summary_step_number(self):
        s = step3_summary()
        assert s['step'] == 3

    def test_summary_has_verified_examples(self):
        s = step3_summary()
        assert len(s['key_examples_verified']) >= 3

    def test_summary_has_counterexamples(self):
        s = step3_summary()
        assert len(s['key_counterexamples']) >= 1

    def test_summary_lattice_complete(self):
        s = step3_summary()
        assert 'COMPLETE' in s['lattice_VOAs']

    def test_summary_virasoro_restricted(self):
        """Virasoro: step 3 only applies at c=13."""
        s = step3_summary()
        assert 'c=13' in s['virasoro']


# ===================================================================
# 15. Theta function identities
# ===================================================================

class TestThetaIdentities:

    def test_theta_Z1_equals_theta3(self):
        """theta_{Z^1} = theta_3."""
        t1 = theta_Zr_qexp(1, NMAX)
        t3 = theta3_qexp(NMAX)
        for i in range(NMAX + 1):
            assert abs(t1[i] - t3[i]) < 1e-10

    def test_theta_Z2(self):
        """theta_{Z^2} = theta_3^2. Check a few coefficients."""
        t2 = theta_Zr_qexp(2, NMAX)
        t3 = theta3_qexp(NMAX)
        t3_sq = _poly_mul(t3, t3, NMAX)
        for i in range(min(20, NMAX + 1)):
            assert abs(t2[i] - t3_sq[i]) < 1e-6

    def test_theta_Z8_vs_E4_squared(self):
        """
        theta_{Z^8} = (theta_3)^8. This is NOT E_4 (which is theta_{E_8}).
        Check that they differ.
        """
        t8 = theta_Zr_qexp(8, 10)
        e4 = eisenstein_qexp(4, 10)
        # They should differ at q^1: theta_3^8 has r_8(1) = 16,
        # while E_4 has a_1 = 240.
        assert abs(t8[1] - 16) < 1e-6
        assert abs(e4[1] - 240) < 1e-6
        assert abs(t8[1] - e4[1]) > 100  # Clearly different

    def test_eta_power_24_matches_delta(self):
        """eta^{24} = Delta (up to the q-shift convention)."""
        # eta^24 coefficients correspond to prod(1-q^k)^24
        # Delta = q * prod(1-q^k)^24, so delta_qexp shifts by 1
        eta24 = eta_power_qexp(24, NMAX)
        d = delta_qexp(NMAX)
        # d[n] = eta24[n-1] for n >= 1
        for n in range(1, min(20, NMAX)):
            assert abs(d[n] - eta24[n - 1]) < 1e-6, \
                f"Mismatch at n={n}: delta[{n}]={d[n]}, eta24[{n - 1}]={eta24[n - 1]}"
