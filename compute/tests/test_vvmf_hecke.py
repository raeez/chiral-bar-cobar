"""Tests for vector-valued modular forms and Hecke operators on Virasoro characters.

50+ tests covering:
  - Minimal model construction and central charges
  - Character q-series against known values
  - S-matrix unitarity and symmetry
  - T-matrix eigenvalues
  - Hecke operator computation
  - Rankin-Selberg integral and L-functions
  - Cross-model consistency
"""

import pytest
from fractions import Fraction
from math import gcd

import mpmath
from mpmath import mp, mpf, mpc, pi, exp, fabs, sqrt, power

from compute.lib.vvmf_hecke import (
    MinimalModel,
    MinimalModelLabel,
    ising_model,
    tricritical_ising_model,
    three_state_potts_model,
    character_qseries,
    character_value,
    character_vector,
    s_matrix,
    t_matrix,
    verify_s_matrix_unitarity,
    verify_s_matrix_symmetry,
    hecke_operator_on_qseries,
    hecke_eigenvalues,
    rankin_selberg_dirichlet_coeffs,
    rankin_selberg_lfunction,
    character_lfunction,
    compute_spectral_data,
    _inverse_eta_coeffs,
    _eta_coeffs,
)

DPS = 30


# ===================================================================
# Model construction
# ===================================================================

class TestMinimalModelConstruction:

    def test_ising_central_charge(self):
        m = ising_model()
        assert m.central_charge == Fraction(1, 2)

    def test_tricritical_ising_central_charge(self):
        m = tricritical_ising_model()
        assert m.central_charge == Fraction(7, 10)

    def test_three_state_potts_central_charge(self):
        m = three_state_potts_model()
        assert m.central_charge == Fraction(4, 5)

    def test_ising_num_primaries(self):
        m = ising_model()
        assert m.num_primaries() == 3

    def test_tricritical_ising_num_primaries(self):
        m = tricritical_ising_model()
        assert m.num_primaries() == 6

    def test_three_state_potts_num_primaries(self):
        m = three_state_potts_model()
        assert m.num_primaries() == 10

    def test_coprimality_check(self):
        with pytest.raises(ValueError):
            MinimalModel(p=6, q=4)  # gcd = 2

    def test_p_greater_than_q(self):
        with pytest.raises(ValueError):
            MinimalModel(p=3, q=4)

    def test_q_at_least_2(self):
        with pytest.raises(ValueError):
            MinimalModel(p=3, q=1)

    def test_general_central_charge_formula(self):
        """c = 1 - 6(p-q)^2/(pq) for M(7,5)."""
        m = MinimalModel(p=7, q=5)
        assert m.central_charge == Fraction(1) - Fraction(6 * 4, 35)
        assert m.central_charge == Fraction(11, 35)


# ===================================================================
# Conformal weights
# ===================================================================

class TestConformalWeights:

    def test_ising_vacuum(self):
        """h_{1,1} = 0 for Ising."""
        m = ising_model()
        assert m.conformal_weight(1, 1) == Fraction(0)

    def test_ising_spin_field(self):
        """h_{2,1} = 1/16 for Ising (sigma field)."""
        m = ising_model()
        assert m.conformal_weight(2, 1) == Fraction(1, 16)

    def test_ising_energy_field(self):
        """h_{3,1} = 1/2 for Ising (epsilon field). But (3,1)~(1,2)."""
        m = ising_model()
        assert m.conformal_weight(1, 2) == Fraction(1, 2)

    def test_tricritical_ising_vacuum(self):
        m = tricritical_ising_model()
        assert m.conformal_weight(1, 1) == Fraction(0)

    def test_tricritical_ising_h21(self):
        """h_{2,1} for M(5,4): ((2*4-1*5)^2 - 1)/(4*20) = (9-1)/80 = 1/10."""
        m = tricritical_ising_model()
        assert m.conformal_weight(2, 1) == Fraction(1, 10)

    def test_potts_vacuum(self):
        m = three_state_potts_model()
        assert m.conformal_weight(1, 1) == Fraction(0)

    def test_identification_symmetry(self):
        """h_{r,s} = h_{p-r,q-s}."""
        m = ising_model()
        assert m.conformal_weight(1, 1) == m.conformal_weight(3, 2)
        assert m.conformal_weight(2, 1) == m.conformal_weight(2, 2)

    def test_weight_non_negative(self):
        """All conformal weights of primaries are non-negative."""
        for model in [ising_model(), tricritical_ising_model(), three_state_potts_model()]:
            for lab in model.primary_labels():
                assert model.conformal_weight(lab.r, lab.s) >= 0


# ===================================================================
# Eta function / partition numbers
# ===================================================================

class TestEtaPartitions:

    def test_partition_numbers_small(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        inv = _inverse_eta_coeffs(10)
        assert inv[0] == 1
        assert inv[1] == 1
        assert inv[2] == 2
        assert inv[3] == 3
        assert inv[4] == 5
        assert inv[5] == 7

    def test_partition_number_10(self):
        """p(10) = 42."""
        inv = _inverse_eta_coeffs(15)
        assert inv[10] == 42

    def test_eta_product_inverse(self):
        """eta * (1/eta) should give delta_{n,0}."""
        N = 50
        eta = _eta_coeffs(N)
        inv = _inverse_eta_coeffs(N)
        for n in range(N):
            conv = sum(eta[k] * inv[n - k] for k in range(n + 1))
            expected = 1 if n == 0 else 0
            assert conv == expected, f"Convolution at n={n}: got {conv}, expected {expected}"


# ===================================================================
# Character q-series
# ===================================================================

class TestCharacterQSeries:

    def test_vacuum_leading_coeff(self):
        """d_0 = 1 for all vacuum characters."""
        for model in [ising_model(), tricritical_ising_model(), three_state_potts_model()]:
            coeffs = character_qseries(model, 1, 1, num_terms=10, dps=DPS)
            assert abs(coeffs[0] - 1) < mpf(1e-20)

    def test_ising_vacuum_first_terms(self):
        """Ising vacuum chi_{1,1}: Rocha-Caridi for M(4,3), h=0."""
        m = ising_model()
        coeffs = character_qseries(m, 1, 1, num_terms=10, dps=DPS)
        expected = [1, 0, 1, 1, 2, 2, 3, 3, 5]
        for i, e in enumerate(expected):
            assert abs(coeffs[i] - e) < mpf(1e-15), \
                f"Ising vacuum d_{i}: got {coeffs[i]}, expected {e}"

    def test_ising_spin_first_terms(self):
        """Ising spin field chi_{2,1} (h=1/16)."""
        m = ising_model()
        coeffs = character_qseries(m, 2, 1, num_terms=10, dps=DPS)
        expected = [1, 1, 1, 2, 2, 3, 4, 5, 6, 8]
        for i, e in enumerate(expected):
            assert abs(coeffs[i] - e) < mpf(1e-15), \
                f"Ising spin d_{i}: got {coeffs[i]}, expected {e}"

    def test_ising_energy_first_terms(self):
        """Ising energy chi_{1,2} (h=1/2)."""
        m = ising_model()
        coeffs = character_qseries(m, 1, 2, num_terms=10, dps=DPS)
        expected = [1, 1, 1, 1, 2, 2, 3, 4, 5, 6]
        for i, e in enumerate(expected):
            assert abs(coeffs[i] - e) < mpf(1e-15), \
                f"Ising energy d_{i}: got {coeffs[i]}, expected {e}"

    def test_all_degeneracies_nonneg_integer(self):
        """All character degeneracies must be non-negative integers."""
        for model in [ising_model(), tricritical_ising_model(), three_state_potts_model()]:
            for lab in model.primary_labels():
                coeffs = character_qseries(model, lab.r, lab.s, num_terms=20, dps=DPS)
                for n, c in enumerate(coeffs):
                    rounded = round(float(c))
                    assert abs(c - rounded) < mpf(1e-10), \
                        f"Non-integer coeff d_{n}={c} for ({lab.r},{lab.s}) in M({model.p},{model.q})"
                    assert rounded >= 0, \
                        f"Negative coeff d_{n}={rounded} for ({lab.r},{lab.s})"

    def test_tricritical_ising_vacuum(self):
        """Tricritical Ising vacuum: 1, 0, 1, 1, 1, 2, 3, ..."""
        m = tricritical_ising_model()
        coeffs = character_qseries(m, 1, 1, num_terms=10, dps=DPS)
        assert abs(coeffs[0] - 1) < mpf(1e-15)
        assert abs(coeffs[1] - 0) < mpf(1e-15)
        assert abs(coeffs[2] - 1) < mpf(1e-15)

    def test_potts_vacuum_leading(self):
        m = three_state_potts_model()
        coeffs = character_qseries(m, 1, 1, num_terms=5, dps=DPS)
        assert abs(coeffs[0] - 1) < mpf(1e-15)


# ===================================================================
# S-matrix
# ===================================================================

class TestSMatrix:

    def test_ising_s_unitarity(self):
        err = verify_s_matrix_unitarity(ising_model(), dps=DPS)
        assert err < mpf(1e-25)

    def test_tricritical_s_unitarity(self):
        err = verify_s_matrix_unitarity(tricritical_ising_model(), dps=DPS)
        assert err < mpf(1e-25)

    def test_potts_s_unitarity(self):
        err = verify_s_matrix_unitarity(three_state_potts_model(), dps=DPS)
        assert err < mpf(1e-25)

    def test_ising_s_symmetry(self):
        err = verify_s_matrix_symmetry(ising_model(), dps=DPS)
        assert err < mpf(1e-25)

    def test_tricritical_s_symmetry(self):
        err = verify_s_matrix_symmetry(tricritical_ising_model(), dps=DPS)
        assert err < mpf(1e-25)

    def test_potts_s_symmetry(self):
        err = verify_s_matrix_symmetry(three_state_potts_model(), dps=DPS)
        assert err < mpf(1e-25)

    def test_ising_s_size(self):
        S = s_matrix(ising_model(), dps=DPS)
        assert S.rows == 3
        assert S.cols == 3

    def test_s_squared_is_charge_conjugation(self):
        """S^2 = C (charge conjugation) for minimal models.
        For Ising, S^2 = I since all reps are self-conjugate."""
        m = ising_model()
        S = s_matrix(m, dps=DPS)
        S2 = S * S
        n = S.rows
        # S^2 should be identity (all Ising reps are self-conjugate)
        for i in range(n):
            for j in range(n):
                expected = mpf(1) if i == j else mpf(0)
                assert fabs(S2[i, j] - expected) < mpf(1e-20)

    def test_verlinde_formula_ising(self):
        """Verlinde formula: N_{ij}^k = sum_m S_{im} S_{jm} S_{km}^* / S_{0m}.
        For Ising, check N_{sigma,sigma}^{epsilon} = 1 (fusion sigma x sigma = 1 + epsilon)."""
        m = ising_model()
        S = s_matrix(m, dps=DPS)
        labels = m.primary_labels()
        # Find indices
        idx_1 = None  # vacuum (1,1)
        idx_sigma = None  # (2,1), h=1/16
        idx_eps = None  # (1,2), h=1/2
        for k, lab in enumerate(labels):
            h = m.conformal_weight(lab.r, lab.s)
            if h == 0:
                idx_1 = k
            elif h == Fraction(1, 16):
                idx_sigma = k
            elif h == Fraction(1, 2):
                idx_eps = k
        assert idx_1 is not None and idx_sigma is not None and idx_eps is not None

        # N_{sigma, sigma}^{eps}
        n_val = mpf(0)
        for l in range(3):
            n_val += S[idx_sigma, l] * S[idx_sigma, l] * S[idx_eps, l] / S[idx_1, l]
        # Should be integer (0 or 1)
        assert fabs(n_val - round(float(n_val))) < mpf(1e-20)
        assert round(float(n_val)) == 1


# ===================================================================
# T-matrix
# ===================================================================

class TestTMatrix:

    def test_ising_t_diagonal(self):
        T = t_matrix(ising_model(), dps=DPS)
        for i in range(T.rows):
            for j in range(T.cols):
                if i != j:
                    assert fabs(T[i, j]) < mpf(1e-25)

    def test_ising_t_eigenvalues_magnitude(self):
        """All T eigenvalues have |T_ii| = 1."""
        T = t_matrix(ising_model(), dps=DPS)
        for i in range(T.rows):
            assert fabs(fabs(T[i, i]) - 1) < mpf(1e-25)

    def test_ising_vacuum_t_eigenvalue(self):
        """T_{00} = exp(2 pi i (0 - c/24)) = exp(-2 pi i / 48) = exp(-pi i/24)."""
        mp.dps = DPS
        m = ising_model()
        T = t_matrix(m, dps=DPS)
        labels = m.primary_labels()
        idx_vac = None
        for k, lab in enumerate(labels):
            if m.conformal_weight(lab.r, lab.s) == 0:
                idx_vac = k
        expected = exp(2 * pi * mpc(0, 1) * (mpf(0) - m.central_charge_mpf / 24))
        assert fabs(T[idx_vac, idx_vac] - expected) < mpf(1e-25)

    def test_tricritical_t_magnitude(self):
        T = t_matrix(tricritical_ising_model(), dps=DPS)
        for i in range(T.rows):
            assert fabs(fabs(T[i, i]) - 1) < mpf(1e-25)

    def test_st_relation_order(self):
        """(ST)^3 = S^2 for modular group."""
        mp.dps = DPS
        m = ising_model()
        S = s_matrix(m, dps=DPS)
        T = t_matrix(m, dps=DPS)
        ST = S * T
        ST3 = ST * ST * ST
        S2 = S * S
        n = S.rows
        for i in range(n):
            for j in range(n):
                assert fabs(ST3[i, j] - S2[i, j]) < mpf(1e-20), \
                    f"(ST)^3 != S^2 at ({i},{j})"


# ===================================================================
# Hecke operators
# ===================================================================

class TestHeckeOperators:

    def test_hecke_t2_ising_output_shape(self):
        result = hecke_operator_on_qseries(ising_model(), 2, num_terms=20, dps=DPS)
        assert len(result) == 3  # 3 primaries
        assert len(result[0]) == 20

    def test_hecke_preserves_integrality(self):
        """Hecke image of integer q-series should have rational coefficients."""
        result = hecke_operator_on_qseries(ising_model(), 2, num_terms=20, dps=DPS)
        for coeffs in result:
            for c in coeffs:
                # Should be close to a half-integer (weight 0 Hecke involves 1/p)
                val = float(c) * 2  # multiply by 2 to check
                assert abs(val - round(val)) < 1e-10

    def test_hecke_eigenvalues_ising(self):
        """Hecke eigenvalues for Ising at small primes."""
        result = hecke_eigenvalues(ising_model(), [2, 3, 5], num_terms=50, dps=DPS)
        assert 2 in result
        assert 3 in result
        assert 5 in result
        # Each should have 3 eigenvalues (one per primary)
        assert len(result[2]) == 3


# ===================================================================
# Rankin-Selberg
# ===================================================================

class TestRankinSelberg:

    def test_rs_coeffs_positive(self):
        """Rankin-Selberg coefficients |a(n)|^2 are non-negative."""
        for model in [ising_model(), tricritical_ising_model()]:
            coeffs = rankin_selberg_dirichlet_coeffs(model, num_terms=30, dps=DPS)
            for n, c in enumerate(coeffs):
                assert c >= -mpf(1e-20), f"Negative RS coeff at n={n}: {c}"

    def test_rs_vacuum_contribution(self):
        """The n=0 coefficient should be num_primaries (each has d_0=1)."""
        m = ising_model()
        coeffs = rankin_selberg_dirichlet_coeffs(m, num_terms=10, dps=DPS)
        # |a_0|^2 summed over primaries = num_primaries * 1^2
        assert fabs(coeffs[0] - m.num_primaries()) < mpf(1e-15)

    def test_rs_lfunction_convergence(self):
        """L(s) converges for large Re(s) (degeneracies grow sub-exponentially)."""
        mp.dps = DPS
        m = ising_model()
        # Degeneracies grow like exp(C*sqrt(n)), so n^{-s} series converges for all s.
        # But convergence is slow for small s; use s=10 for quick test.
        val1 = rankin_selberg_lfunction(m, mpc(10, 0), num_terms=100, dps=DPS)
        val2 = rankin_selberg_lfunction(m, mpc(10, 0), num_terms=200, dps=DPS)
        # Convergence check: relative change decreases with more terms
        assert fabs(val1 - val2) / max(fabs(val1), mpf(1e-30)) < mpf(0.5)

    def test_rs_lfunction_positive_real_axis(self):
        """L(s) should be real for real s."""
        mp.dps = DPS
        m = ising_model()
        val = rankin_selberg_lfunction(m, mpc(10, 0), num_terms=200, dps=DPS)
        assert fabs(val.imag) < mpf(1e-15)

    def test_character_lfunction_convergence(self):
        """Individual character L-function converges."""
        mp.dps = DPS
        m = ising_model()
        v1 = character_lfunction(m, 1, 1, mpc(10, 0), num_terms=200, dps=DPS)
        v2 = character_lfunction(m, 1, 1, mpc(10, 0), num_terms=400, dps=DPS)
        assert fabs(v1 - v2) / fabs(v2) < mpf(0.1)


# ===================================================================
# Spectral data
# ===================================================================

class TestSpectralData:

    def test_compute_spectral_data_ising(self):
        data = compute_spectral_data(ising_model(), primes=[2, 3], num_terms=30, dps=DPS)
        assert data.num_primaries == 3
        assert data.central_charge == Fraction(1, 2)
        assert data.s_matrix_val.rows == 3
        assert 2 in data.hecke_coeffs
        assert len(data.rs_dirichlet_coeffs) == 30

    def test_compute_spectral_data_tricritical(self):
        data = compute_spectral_data(
            tricritical_ising_model(), primes=[2], num_terms=20, dps=DPS
        )
        assert data.num_primaries == 6

    def test_compute_spectral_data_potts(self):
        data = compute_spectral_data(
            three_state_potts_model(), primes=[2], num_terms=20, dps=DPS
        )
        assert data.num_primaries == 10


# ===================================================================
# Cross-model consistency
# ===================================================================

class TestCrossModel:

    def test_ising_character_sum_at_tau(self):
        """Sum of characters with S_{0,i} weights gives Z(tau) ~ partition function.
        Z = sum_i |chi_i|^2 should be modular invariant (diagonal invariant)."""
        mp.dps = DPS
        m = ising_model()
        tau = mpc(0.1, 1.5)
        chi = character_vector(m, tau, num_terms=100, dps=DPS)
        Z = fabs(sum(abs(c) ** 2 for c in chi))
        assert Z > 0  # basic sanity

    def test_s_transform_characters(self):
        """chi_i(-1/tau) = sum_j S_{ij} chi_j(tau) (approximately, via q-series)."""
        mp.dps = DPS
        m = ising_model()
        tau = mpc(0.0, 2.0)
        tau_transformed = -1 / tau  # = i/2

        chi_tau = character_vector(m, tau, num_terms=300, dps=DPS)
        chi_minv = character_vector(m, tau_transformed, num_terms=300, dps=DPS)
        S = s_matrix(m, dps=DPS)

        labels = m.primary_labels()
        for i in range(len(labels)):
            predicted = mpc(0)
            for j in range(len(labels)):
                predicted += S[i, j] * chi_tau[j]
            # Check agreement (may need many terms for convergence)
            rel_err = fabs(predicted - chi_minv[i]) / max(fabs(chi_minv[i]), mpf(1e-30))
            assert rel_err < mpf(0.01), \
                f"S-transform failed for character {i}: rel_err = {float(rel_err)}"

    def test_central_charge_ordering(self):
        """c(Ising) < c(TCI) < c(Potts) as expected for the unitary series."""
        c1 = ising_model().central_charge
        c2 = tricritical_ising_model().central_charge
        c3 = three_state_potts_model().central_charge
        assert c1 < c2 < c3 < 1

    def test_num_primaries_formula(self):
        """Number of primaries = (p-1)(q-1)/2."""
        for m in [ising_model(), tricritical_ising_model(), three_state_potts_model()]:
            expected = (m.p - 1) * (m.q - 1) // 2
            assert m.num_primaries() == expected
