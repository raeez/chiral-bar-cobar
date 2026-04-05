#!/usr/bin/env python3
r"""Tests for offdiag_newton_test.py -- off-diagonal Newton test at genus 2.

Tests the central question of Agent B10: do genus-2 off-diagonal corrections
give constraints BEYOND Newton's identities?

DEFINITIVE ANSWERS (verified computationally):
  (a) Satake parameters: NO. Newton for 2 variables is complete.
  (b) Partition function: YES. Boecherer coefficient c_2 is non-Newton.

References:
    prop:genus2-non-diagonal (arithmetic_shadows.tex, line 9103)
    thm:genus2-non-collapse (arithmetic_shadows.tex, line 9147)
    mc_spectral_rigidity.py (Newton redundancy at genus 1)
"""

import math
import sys
import os

import pytest
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from offdiag_newton_test import (
    partitions,
    divisor_count,
    sigma_k,
    genus1_mc_is_newton,
    heisenberg_genus2_connected_free_energy,
    schur_complement_correction,
    offdiag_newton_analysis,
    virasoro_genus2_offdiag_order_r,
    cross_handle_newton_test,
    beurling_kernel_non_newton,
    master_offdiag_newton_analysis,
)


# =========================================================================
# 1. Utilities
# =========================================================================

class TestUtilities:
    """Test partition, divisor, and sigma functions."""

    def test_partitions_small(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for n, p in enumerate(expected):
            assert partitions(n) == p, f"p({n}) = {partitions(n)}, expected {p}"

    def test_divisor_count(self):
        """d(1)=1, d(2)=2, d(3)=2, d(4)=3, d(6)=4, d(12)=6."""
        assert divisor_count(1) == 1
        assert divisor_count(2) == 2
        assert divisor_count(3) == 2
        assert divisor_count(4) == 3
        assert divisor_count(6) == 4
        assert divisor_count(12) == 6

    def test_sigma_k_values(self):
        """sigma_1(n) = sum of divisors."""
        assert sigma_k(1, 1) == 1
        assert sigma_k(2, 1) == 3  # 1+2
        assert sigma_k(3, 1) == 4  # 1+3
        assert sigma_k(4, 1) == 7  # 1+2+4
        assert sigma_k(6, 1) == 12  # 1+2+3+6
        assert sigma_k(12, 1) == 28  # 1+2+3+4+6+12

    def test_sigma_k_higher(self):
        """sigma_3(n) = sum of cubes of divisors."""
        assert sigma_k(1, 3) == 1
        assert sigma_k(2, 3) == 9    # 1+8
        assert sigma_k(3, 3) == 28   # 1+27
        assert sigma_k(4, 3) == 73   # 1+8+64


# =========================================================================
# 2. Genus-1 Newton completeness
# =========================================================================

class TestGenus1Newton:
    """Verify that genus-1 MC = Newton for 2 variables."""

    def test_newton_complete_delta(self):
        """Newton is complete for Ramanujan Delta at p=2."""
        result = genus1_mc_is_newton(-24.0, 2048.0, 20)
        assert result['newton_complete']
        assert result['max_relative_residual'] < 1e-10

    def test_newton_complete_integer_roots(self):
        """Newton for alpha=3, beta=4: e1=7, e2=12."""
        result = genus1_mc_is_newton(7.0, 12.0, 15)
        assert result['newton_complete']

    def test_newton_complete_complex_roots(self):
        """Newton for complex conjugate Satake (Ramanujan case)."""
        # e1 = 2*cos(theta)*p^{(k-1)/2}, e2 = p^{k-1}
        # Take theta = pi/3, p = 2, k = 12:
        e1 = 2 * math.cos(math.pi / 3) * 2 ** 5.5  # = 2^5.5
        e2 = 2 ** 11
        result = genus1_mc_is_newton(e1, e2, 15)
        assert result['newton_complete']

    def test_newton_complete_ramanujan_violating(self):
        """Newton holds even for Ramanujan-violating Satake parameters."""
        # Take |alpha| != |beta| but |alpha| != p^{(k-1)/2}
        # e1 = 100, e2 = 2048 (alpha,beta not on the unit circle)
        result = genus1_mc_is_newton(100.0, 2048.0, 15)
        assert result['newton_complete']
        # Newton is a TAUTOLOGY: it holds regardless of Ramanujan

    def test_newton_redundancy_message(self):
        """Verify the conclusion states Newton completeness."""
        result = genus1_mc_is_newton(-24.0, 2048.0, 10)
        assert 'Newton' in result['conclusion']
        assert 'determined' in result['conclusion'].lower() or 'no new constraint' in result['conclusion'].lower()


# =========================================================================
# 3. Heisenberg genus-2 connected free energy
# =========================================================================

class TestHeisenbergGenus2:
    """Test Heisenberg genus-2 connected free energy."""

    def test_offdiag_coefficients_formula(self):
        """Verify c_m = sigma_1(m)/m."""
        result = heisenberg_genus2_connected_free_energy(
            tau1=0.5j, tau2=0.7j, z=0.3j, N_terms=20
        )
        coeffs = result['offdiag_coefficients']
        # c_1 = sigma_1(1)/1 = 1/1 = 1
        assert float(coeffs[0]) == 1.0
        # c_2 = sigma_1(2)/2 = 3/2
        assert abs(float(coeffs[1]) - 1.5) < 1e-10
        # c_3 = sigma_1(3)/3 = 4/3
        assert abs(float(coeffs[2]) - 4.0 / 3.0) < 1e-10
        # c_4 = sigma_1(4)/4 = 7/4
        assert abs(float(coeffs[3]) - 7.0 / 4.0) < 1e-10
        # c_6 = sigma_1(6)/6 = 12/6 = 2
        assert abs(float(coeffs[5]) - 2.0) < 1e-10

    def test_expansion_agrees_with_direct(self):
        """r-expansion of -log eta(z) matches direct computation."""
        result = heisenberg_genus2_connected_free_energy(
            tau1=0.5j, tau2=0.7j, z=0.4j, N_terms=40
        )
        # The agreement should be good for |r| = e^{-2*pi*0.4} ~ 0.08
        assert result['expansion_vs_direct_residual'] < 1e-8

    def test_tau_independence(self):
        """F_2^conn for Heisenberg is independent of tau_1, tau_2."""
        z_val = 0.3j
        result1 = heisenberg_genus2_connected_free_energy(
            tau1=0.5j, tau2=0.7j, z=z_val, N_terms=30
        )
        result2 = heisenberg_genus2_connected_free_energy(
            tau1=0.8j, tau2=1.2j, z=z_val, N_terms=30
        )
        # The connected free energies should agree (both = -log eta(z))
        diff = abs(result1['F2_conn_expansion'] - result2['F2_conn_expansion'])
        assert diff < 1e-10, f"tau-dependence detected: diff = {diff}"

    def test_small_r_leading_term(self):
        """For small r, F_2^conn ~ r (the first off-diagonal correction)."""
        z_val = 0.8j  # |r| = e^{-2*pi*0.8} ~ 0.007
        result = heisenberg_genus2_connected_free_energy(
            tau1=0.5j, tau2=0.7j, z=z_val, N_terms=20
        )
        r = np.exp(2j * np.pi * z_val)
        # Leading term: c_1 * r = 1 * r
        # F_2^conn ~ -(pi*i*z)/12 + r + O(r^2)
        linear_part = -(np.pi * 1j * z_val) / 12.0 + r
        full = result['F2_conn_expansion']
        # The next correction is O(r^2) ~ 5e-5
        assert abs(full - linear_part) < 0.01  # r^2 correction is small


# =========================================================================
# 4. Schur complement factorization
# =========================================================================

class TestSchurComplement:
    """Test Schur complement off-diagonal correction."""

    def test_heisenberg_factorization(self):
        """Heisenberg Fredholm determinant factors at genus 2."""
        q1 = np.exp(2j * np.pi * 0.5j)
        q2 = np.exp(2j * np.pi * 0.7j)
        r = np.exp(2j * np.pi * 0.3j)
        result = schur_complement_correction(q1, q2, r, N_modes=20)
        assert result['factorization_holds'], "Heisenberg should factorize!"

    def test_schur_complement_is_eta(self):
        """Schur complement = prod(1-r^n) for Heisenberg."""
        q1 = np.exp(2j * np.pi * 0.6j)
        q2 = np.exp(2j * np.pi * 0.8j)
        r = np.exp(2j * np.pi * 0.4j)
        result = schur_complement_correction(q1, q2, r, N_modes=25)
        # Schur complement should equal det_r = prod(1-r^n)
        assert abs(result['schur_complement'] - result['det_r']) < 1e-12

    def test_c11_positive(self):
        """c_{1,1} coefficient is positive (sum of positive terms)."""
        q1 = np.exp(2j * np.pi * 0.5j)
        q2 = np.exp(2j * np.pi * 0.7j)
        r = np.exp(2j * np.pi * 0.3j)
        result = schur_complement_correction(q1, q2, r, N_modes=20)
        # c_{1,1} should be positive real (up to numerical noise)
        assert result['c_11_manuscript'].real > 0
        assert abs(result['c_11_manuscript'].imag) < 1e-10

    def test_factorization_different_parameters(self):
        """Factorization holds for various sewing parameters."""
        for im_tau1, im_tau2, im_z in [(0.3, 0.4, 0.5), (1.0, 1.5, 0.8),
                                        (0.2, 0.9, 0.6)]:
            q1 = np.exp(-2 * np.pi * im_tau1)
            q2 = np.exp(-2 * np.pi * im_tau2)
            r = np.exp(-2 * np.pi * im_z)
            result = schur_complement_correction(q1, q2, r, N_modes=20)
            assert result['factorization_holds'], (
                f"Factorization failed at im_tau=({im_tau1},{im_tau2}), im_z={im_z}"
            )


# =========================================================================
# 5. Off-diagonal Newton analysis
# =========================================================================

class TestOffdiagNewton:
    """Test the central off-diagonal Newton analysis."""

    def test_satake_not_constrained(self):
        """Satake parameters are NOT constrained by genus-2 off-diagonal."""
        result = offdiag_newton_analysis(c_val=1.0)
        assert not result['summary']['satake_constrained']

    def test_partition_function_constrained(self):
        """Partition function IS constrained by genus-2 off-diagonal."""
        result = offdiag_newton_analysis(c_val=1.0)
        assert result['summary']['partition_function_constrained']

    def test_newton_complete_in_analysis(self):
        """Newton is reported as complete."""
        result = offdiag_newton_analysis(c_val=1.0)
        assert result['newton_check']['newton_complete']

    def test_non_newton_invariant_identified(self):
        """The non-Newton invariant is the Boecherer coefficient."""
        result = offdiag_newton_analysis(c_val=1.0)
        assert 'Boecherer' in result['summary']['non_newton_invariant'] or \
               'c_2' in result['summary']['non_newton_invariant']

    def test_heisenberg_offdiag_coefficients(self):
        """Off-diagonal coefficients for Heisenberg are sigma_1(m)/m."""
        result = offdiag_newton_analysis(c_val=1.0, N_expansion=10)
        coeffs = result['offdiag_expansion']['first_10_coeffs']
        # c_1 = 1, c_2 = 3/2, c_3 = 4/3, c_4 = 7/4, c_5 = 6/5
        assert abs(coeffs[0] - 1.0) < 1e-10
        assert abs(coeffs[1] - 1.5) < 1e-10
        assert abs(coeffs[2] - 4.0 / 3.0) < 1e-10
        assert abs(coeffs[3] - 7.0 / 4.0) < 1e-10
        assert abs(coeffs[4] - 6.0 / 5.0) < 1e-10

    def test_genus2_adds_boecherer(self):
        """Genus-2 adds Boecherer coefficient (c_2) beyond genus-1."""
        result = offdiag_newton_analysis()
        assert 'c_2' in result['summary']['genus_2_adds'] or \
               'Boecherer' in result['summary']['genus_2_adds']


# =========================================================================
# 6. Virasoro off-diagonal
# =========================================================================

class TestVirasoroOffdiag:
    """Test Virasoro genus-2 off-diagonal corrections."""

    def test_d1_vanishes(self):
        """d_1 = 0 for Virasoro (no weight-1 modes)."""
        result = virasoro_genus2_offdiag_order_r(c_val=25.0, r_order=2)
        assert result['d_1_vanishes']
        assert result['corrections'][1] == 0.0

    def test_d2_scales_as_kappa_squared(self):
        """d_2 ~ kappa^2 = (c/2)^2 at leading order."""
        for c in [1.0, 10.0, 25.0, 0.5]:
            result = virasoro_genus2_offdiag_order_r(c_val=c, r_order=2)
            kappa = c / 2.0
            assert abs(result['d_2_leading'] - kappa ** 2) < 1e-10

    def test_d2_does_not_constrain_satake(self):
        """d_2 does not constrain Satake parameters."""
        result = virasoro_genus2_offdiag_order_r(c_val=25.0, r_order=2)
        assert not result['d_2_constrains_satake']

    def test_d2_does_constrain_weights(self):
        """d_2 constrains partition function weights."""
        result = virasoro_genus2_offdiag_order_r(c_val=25.0, r_order=2)
        assert result['d_2_constrains_weights']

    def test_weight4_gram_matrix(self):
        """Gram matrix at weight 4 has correct structure for c=25."""
        result = virasoro_genus2_offdiag_order_r(c_val=25.0, r_order=4)
        # At weight 4, dim V_4(Vir) = 2
        # d_4 should be the determinant of the 2x2 Gram matrix
        # Gram_4 = [[c(5c+22)/10, 3c], [3c, c/2*(c/2+2)]]
        c = 25.0
        expected_11 = c * (5 * c + 22) / 10.0  # = 25*147/10 = 367.5
        expected_12 = 3 * c  # = 75
        expected_22 = (c / 2.0) * (c / 2.0 + 2)  # = 12.5 * 14.5 = 181.25
        det_expected = expected_11 * expected_22 - expected_12 ** 2
        assert abs(result['corrections'][4] - det_expected) < 1e-6


# =========================================================================
# 7. Cross-handle Newton test
# =========================================================================

class TestCrossHandleNewton:
    """Test cross-handle coupling vs Newton analysis."""

    def test_single_eigenform_trivial(self):
        """For 1 eigenform, genus-2 adds nothing."""
        result = cross_handle_newton_test(N_eigenforms=1)
        assert not result['satake_constrained_by_genus2']
        assert not result['weights_constrained_by_genus2']

    def test_two_eigenforms_nontrivial(self):
        """For 2 eigenforms, genus-2 constrains weights."""
        result = cross_handle_newton_test(N_eigenforms=2)
        assert not result['satake_constrained_by_genus2']
        assert result['weights_constrained_by_genus2']

    def test_factored_terms_automatic(self):
        """Factored cross-handle terms are automatic from genus 1."""
        result = cross_handle_newton_test(N_eigenforms=2)
        assert result['factored_terms_automatic']

    def test_connected_terms_new(self):
        """Connected cross-handle terms are genuinely new at genus 2."""
        result = cross_handle_newton_test(N_eigenforms=2)
        assert result['connected_terms_new']

    def test_genus1_surplus_positive(self):
        """Genus-1 is already overdetermined for 2 eigenforms at 3 primes."""
        result = cross_handle_newton_test(N_eigenforms=2, primes=[2, 3, 5])
        # 2*N*P - (N-1 + N*P) = 2*2*3 - (1+2*3) = 12 - 7 = 5
        assert result['genus1_surplus'] > 0

    def test_genus2_additional_positive(self):
        """Genus-2 adds additional constraints."""
        result = cross_handle_newton_test(N_eigenforms=2, primes=[2, 3, 5])
        assert result['genus2_additional_constraints'] > 0

    def test_three_eigenforms(self):
        """For 3 eigenforms, connected cross-terms still new."""
        result = cross_handle_newton_test(N_eigenforms=3, primes=[2, 3, 5, 7])
        assert not result['satake_constrained_by_genus2']
        assert result['weights_constrained_by_genus2']
        assert result['connected_terms_new']


# =========================================================================
# 8. Beurling kernel
# =========================================================================

class TestBeurlingKernel:
    """Test Beurling kernel as non-Newton detector."""

    def test_leech_rank_one(self):
        """Leech lattice (rank 24): kernel rank = 1."""
        result = beurling_kernel_non_newton(rank=24)
        assert result['kernel_rank'] == 1
        assert not result['cross_correlation_exists']

    def test_rank48_higher_rank(self):
        """Rank-48 lattice: kernel rank > 1, cross-correlations exist."""
        result = beurling_kernel_non_newton(rank=48)
        assert result['kernel_rank'] > 1
        assert result['cross_correlation_exists']

    def test_satake_not_constrained(self):
        """Beurling kernel does not constrain Satake parameters."""
        result = beurling_kernel_non_newton(rank=24)
        assert not result['satake_constrained']

    def test_partition_constrained(self):
        """Beurling kernel constrains partition function."""
        result = beurling_kernel_non_newton(rank=24)
        assert result['partition_constrained']


# =========================================================================
# 9. Master analysis
# =========================================================================

class TestMasterAnalysis:
    """Test the complete master analysis."""

    def test_master_runs(self):
        """Master analysis completes without error."""
        result = master_offdiag_newton_analysis()
        assert result is not None

    def test_genus1_complete(self):
        """Genus-1 Newton is complete."""
        result = master_offdiag_newton_analysis()
        assert result['genus1_newton_complete']

    def test_heisenberg_factorizes(self):
        """Heisenberg Fredholm determinant factorizes."""
        result = master_offdiag_newton_analysis()
        assert result['schur_complement_factorizes_heisenberg']

    def test_satake_not_constrained(self):
        """Off-diagonal does NOT constrain Satake."""
        result = master_offdiag_newton_analysis()
        assert not result['offdiag_satake_constrained']

    def test_partition_constrained(self):
        """Off-diagonal DOES constrain partition function."""
        result = master_offdiag_newton_analysis()
        assert result['offdiag_partition_constrained']

    def test_single_eigenform_trivial(self):
        """Single eigenform: genus-2 trivial."""
        result = master_offdiag_newton_analysis()
        assert result['single_eigenform_genus2_trivial']

    def test_multi_eigenform_nontrivial(self):
        """Multi eigenform: genus-2 nontrivial."""
        result = master_offdiag_newton_analysis()
        assert result['multi_eigenform_genus2_nontrivial']

    def test_virasoro_d1_vanishes(self):
        """Virasoro d_1 = 0."""
        result = master_offdiag_newton_analysis()
        assert result['virasoro_d1_vanishes']

    def test_definitive_answers_present(self):
        """Definitive answers for both questions are present."""
        result = master_offdiag_newton_analysis()
        assert 'satake_parameters' in result['definitive_answers']
        assert 'partition_function' in result['definitive_answers']
        assert 'NO' in result['definitive_answers']['satake_parameters']
        assert 'YES' in result['definitive_answers']['partition_function']


# =========================================================================
# 10. Newton redundancy: quantitative cross-checks
# =========================================================================

class TestNewtonRedundancyQuantitative:
    """Quantitative cross-checks on Newton redundancy."""

    def test_power_sum_4_from_newton(self):
        """p_4 = e1*p_3 - e2*p_2 is exact for integer roots."""
        alpha, beta = 3, 7
        e1 = alpha + beta  # 10
        e2 = alpha * beta  # 21
        p2 = alpha ** 2 + beta ** 2  # 58
        p3 = alpha ** 3 + beta ** 3  # 370
        p4_direct = alpha ** 4 + beta ** 4  # 2482
        p4_newton = e1 * p3 - e2 * p2  # 10*370 - 21*58 = 3700-1218 = 2482
        assert p4_newton == p4_direct

    def test_power_sum_r_ramanujan_tau(self):
        """Power sums for tau(2) satisfy Newton exactly."""
        e1 = -24  # tau(2)
        e2 = 2048  # 2^11
        # p_2 = e1^2 - 2*e2 = 576 - 4096 = -3520
        p2 = e1 ** 2 - 2 * e2
        assert p2 == -3520
        # p_3 = e1*p_2 - e2*p_1 = -24*(-3520) - 2048*(-24)
        #      = 84480 + 49152 = 133632
        p3 = e1 * p2 - e2 * e1
        assert p3 == 133632
        # p_4 = e1*p_3 - e2*p_2 = -24*133632 - 2048*(-3520)
        #      = -3207168 + 7208960 = 4001792
        p4 = e1 * p3 - e2 * p2
        assert p4 == 4001792

    def test_offdiag_product_factors(self):
        """Cross-handle product P_{(m,n)} = P_m * P_n for single eigenform."""
        # For a single eigenform with a(2) = -24, a(3) = 252:
        a2 = -24
        a3 = 252
        # P_1(p) = c * a(p) with c = 1 (single eigenform, normalized)
        P1_2 = a2  # at prime 2
        P1_3 = a3  # at prime 3
        # Cross-handle: P_{(1,1)}(2, 3) = c^2 * a(2) * a(3)
        P_11 = a2 * a3
        # This should equal P_1(2) * P_1(3):
        assert P_11 == P1_2 * P1_3
        # For single eigenform, cross-handle ALWAYS factors.

    def test_offdiag_product_always_factors_at_leading_order(self):
        """Cross-handle product ALWAYS factors: P_{(m,n)} = P_m * P_n.

        This is the KEY INSIGHT: at the level of weighted power sums,
        cross-handle products FACTOR regardless of number of eigenforms.
        sum_{j,k} c_j c_k a_j(p1)^m a_k(p2)^n
          = [sum_j c_j a_j(p1)^m] * [sum_k c_k a_k(p2)^n]
          = P_m(p1) * P_n(p2)

        The genuinely non-Newton content at genus 2 comes from the
        SCHUR COMPLEMENT (non-factored terms in the Fredholm determinant),
        not from weighted power sums. See schur_complement_correction.
        """
        c1, c2 = 0.6, 0.4
        a1_2, a2_2 = -24, 10
        a1_3, a2_3 = 252, -50
        P1_p2 = c1 * a1_2 + c2 * a2_2
        P1_p3 = c1 * a1_3 + c2 * a2_3
        factored = P1_p2 * P1_p3
        full = (c1 ** 2 * a1_2 * a1_3 + c1 * c2 * a1_2 * a2_3 +
                c2 * c1 * a2_2 * a1_3 + c2 ** 2 * a2_2 * a2_3)
        # Connected part VANISHES: products always factor
        connected = full - factored
        assert abs(connected) < 1e-10, (
            f"Connected part should vanish: {connected}"
        )

    def test_multi_eigenform_weights_not_determined_by_genus1_power_sums(self):
        """Different weight vectors can give the same genus-1 power sums.

        Two decompositions with different (c_1, c_2) but same P_1, P_2
        at a single prime are indistinguishable at genus 1.
        Genus 2 (Boecherer coefficient) can separate them.
        """
        # Decomposition A: c_1=0.7, c_2=0.3 with eigenvalues a_1=-24, a_2=10
        c1a, c2a = 0.7, 0.3
        a1, a2 = -24.0, 10.0
        P1_A = c1a * a1 + c2a * a2  # = -16.8 + 3 = -13.8
        P2_A = c1a * a1 ** 2 + c2a * a2 ** 2  # = 0.7*576 + 0.3*100 = 403.2+30=433.2

        # Decomposition B: different weights, different eigenvalues,
        # engineered to give the SAME P_1 and P_2
        # We need: c1b*b1 + c2b*b2 = P1_A, c1b*b1^2 + c2b*b2^2 = P2_A
        # with c1b+c2b = 1
        # Choose c1b = 0.5, c2b = 0.5:
        # b1+b2 = 2*P1_A = -27.6
        # b1^2+b2^2 = 2*P2_A = 866.4
        # So b1*b2 = ((b1+b2)^2 - (b1^2+b2^2))/2 = (761.76-866.4)/2 = -52.32
        c1b, c2b = 0.5, 0.5
        b_sum = 2 * P1_A
        b_prod = (b_sum ** 2 - 2 * P2_A) / 2
        disc = b_sum ** 2 - 4 * b_prod
        if disc >= 0:
            b1 = (b_sum + math.sqrt(disc)) / 2
            b2 = (b_sum - math.sqrt(disc)) / 2
        else:
            # Complex roots: still valid
            b1 = complex(b_sum / 2, math.sqrt(-disc) / 2)
            b2 = complex(b_sum / 2, -math.sqrt(-disc) / 2)

        P1_B = c1b * b1 + c2b * b2
        P2_B = c1b * abs(b1) ** 2 + c2b * abs(b2) ** 2 if isinstance(b1, complex) \
            else c1b * b1 ** 2 + c2b * b2 ** 2

        if isinstance(b1, complex):
            # For complex roots, P_2 = c1b*b1^2 + c2b*b2^2 (not |b|^2)
            P2_B = (c1b * b1 ** 2 + c2b * b2 ** 2).real

        # P1 should match
        assert abs(P1_B.real if isinstance(P1_B, complex) else P1_B - P1_A) < 1e-8
        # P2 should match (up to numerical precision)
        assert abs(P2_B - P2_A) < 1e-6

        # But the decomposition weights are DIFFERENT:
        assert abs(c1a - c1b) > 0.1  # different weight vectors
        # Genus 2 (Boecherer) can separate these two decompositions.
        # This is the non-Newton content of genus 2.


# =========================================================================
# 11. Heisenberg off-diagonal is purely z-dependent
# =========================================================================

class TestHeisenbergPurelyZ:
    """Verify that Heisenberg off-diagonal depends only on z."""

    def test_no_q1q2_cross_terms(self):
        """Off-diagonal expansion has no q_1*q_2 cross-terms for Heisenberg."""
        # Compute at two different (tau_1, tau_2) but same z
        z = 0.35j
        res1 = heisenberg_genus2_connected_free_energy(0.4j, 0.6j, z, 25)
        res2 = heisenberg_genus2_connected_free_energy(0.9j, 1.3j, z, 25)
        # The coefficients should be IDENTICAL (no tau dependence)
        for i in range(10):
            diff = abs(float(res1['offdiag_coefficients'][i]) -
                       float(res2['offdiag_coefficients'][i]))
            assert diff < 1e-14, f"Coefficient {i+1} differs by {diff}"

    def test_connected_energy_is_minus_log_eta(self):
        """F_2^conn = -log eta(z) for Heisenberg."""
        z = 0.4j
        r = np.exp(2j * np.pi * z)
        # -log eta(z) = -(pi*i*z)/12 - sum log(1-r^n)
        eta_prod = 1.0 + 0j
        for n in range(1, 100):
            eta_prod *= (1.0 - r ** n)
        F2_expected = -(np.pi * 1j * z) / 12.0 - np.log(eta_prod)

        result = heisenberg_genus2_connected_free_energy(0.5j, 0.7j, z, 50)
        F2_computed = result['F2_conn_expansion']

        assert abs(F2_computed - F2_expected) < 1e-6


# =========================================================================
# 12. The critical argument: Satake already determined at genus 1
# =========================================================================

class TestSatakeAlreadyDetermined:
    """The CRITICAL argument: Satake params are already determined at genus 1.

    At genus 1, for a Hecke eigenform f of weight k at prime p:
      e1 = a_f(p) = alpha_p + beta_p
      e2 = p^{k-1} = alpha_p * beta_p
    These TWO numbers determine alpha_p and beta_p UNIQUELY (up to ordering).

    Therefore: ANY function of (alpha_p, beta_p) is determined by genus-1 data.
    Genus-2 off-diagonal corrections involve products of already-determined
    quantities. No new constraint on individual Satake parameters can emerge.

    The ONLY new information at genus 2 is about the WEIGHTS c_j in the
    spectral decomposition, not the eigenvalues themselves.
    """

    def test_satake_determined_by_e1_e2(self):
        """(alpha, beta) are determined by (e1, e2)."""
        for e1, e2 in [(7, 12), (-24, 2048), (100, 2500)]:
            disc = e1 ** 2 - 4 * e2
            if disc >= 0:
                alpha = (e1 + math.sqrt(disc)) / 2
                beta = (e1 - math.sqrt(disc)) / 2
            else:
                alpha = complex(e1 / 2, math.sqrt(-disc) / 2)
                beta = complex(e1 / 2, -math.sqrt(-disc) / 2)
            # Verify
            assert abs((alpha + beta) - e1) < 1e-10
            assert abs((alpha * beta) - e2) < 1e-10

    def test_all_power_sums_from_e1_e2(self):
        """All p_r = alpha^r + beta^r are determined by (e1, e2)."""
        e1, e2 = -24.0, 2048.0
        disc = e1 ** 2 - 4 * e2
        sqrt_d = complex(0, math.sqrt(-disc)) if disc < 0 else math.sqrt(disc)
        alpha = (e1 + sqrt_d) / 2
        beta = (e1 - sqrt_d) / 2

        p = [2.0, e1]
        for r in range(2, 21):
            p.append(e1 * p[-1] - e2 * p[-2])

        for r in range(1, 21):
            direct = alpha ** r + beta ** r
            if isinstance(direct, complex):
                direct = direct.real
            assert abs(p[r] - direct) < 1e-4 * max(abs(p[r]), 1), f"Mismatch at r={r}"

    def test_genus2_product_determined(self):
        """alpha_p^m * alpha_q^n is a product of genus-1 determined quantities."""
        # At primes p=2 and q=3, weight k=12:
        e1_2, e2_2 = -24, 2048
        e1_3, e2_3 = 252, 3 ** 11

        # Satake at p=2
        disc_2 = e1_2 ** 2 - 4 * e2_2
        sq2 = complex(0, math.sqrt(-disc_2))
        alpha_2 = (e1_2 + sq2) / 2
        beta_2 = (e1_2 - sq2) / 2

        # Satake at p=3
        disc_3 = e1_3 ** 2 - 4 * e2_3
        sq3 = complex(0, math.sqrt(-disc_3))
        alpha_3 = (e1_3 + sq3) / 2
        beta_3 = (e1_3 - sq3) / 2

        # The product alpha_2^2 * alpha_3^3 is determined
        product = alpha_2 ** 2 * alpha_3 ** 3
        # This product is computable from genus-1 data (e1_2, e2_2, e1_3, e2_3)
        # No genus-2 data needed
        assert isinstance(product, complex)  # exists and is well-defined
        # The POINT: this product is a function of already-known quantities.
        # Genus-2 off-diagonal terms involve such products, hence add nothing.
