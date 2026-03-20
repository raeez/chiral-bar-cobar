"""Tests for the Hecke-Newton closure programme."""
import cmath
import math
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from fractions import Fraction
from compute.lib import hecke_newton_closure as hnc
from compute.lib.modular_spectral_rigidity import ramanujan_tau, sigma_k


# ============================================================
# 1. Theta decomposition
# ============================================================

class TestThetaDecomposition:
    """Verify the theta function decomposition into Hecke eigenforms."""

    def test_rank8_is_E4(self):
        """E_8 lattice: Theta_{E_8} = E_4 exactly."""
        decomp = hnc.theta_hecke_decomposition(8, n_max=20)
        assert decomp['weight'] == 4
        assert len(decomp['eigenforms']) == 1
        assert decomp['eigenforms'][0]['label'] == 'E_4'
        assert decomp['eigenforms'][0]['coefficient'] == Fraction(1)
        assert decomp['eigenforms'][0]['type'] == 'eisenstein'

    def test_rank8_constant_term(self):
        """E_4 has constant term 1."""
        decomp = hnc.theta_hecke_decomposition(8, n_max=10)
        assert decomp['fourier_coeffs'][0] == Fraction(1)

    def test_rank8_first_coefficients(self):
        """E_4 Fourier coefficients: 1, 240, 2160, 6720, ..."""
        decomp = hnc.theta_hecke_decomposition(8, n_max=5)
        fc = decomp['fourier_coeffs']
        assert fc[0] == Fraction(1)
        assert fc[1] == Fraction(240)
        assert fc[2] == Fraction(2160)
        assert fc[3] == Fraction(6720)

    def test_rank24_leech_decomposition(self):
        """Leech lattice: Theta = E_{12} - (65520/691) * Delta_12."""
        decomp = hnc.theta_hecke_decomposition(24, n_max=10)
        assert decomp['weight'] == 12
        assert len(decomp['eigenforms']) == 2
        labels = {ef['label'] for ef in decomp['eigenforms']}
        assert labels == {'E_12', 'Delta_12'}

    def test_rank24_delta_coefficient(self):
        """The Delta coefficient is exactly -65520/691."""
        decomp = hnc.theta_hecke_decomposition(24, n_max=5)
        delta_ef = [ef for ef in decomp['eigenforms'] if ef['label'] == 'Delta_12'][0]
        assert delta_ef['coefficient'] == Fraction(-65520, 691)

    def test_rank24_no_roots(self):
        """Leech lattice has no vectors of norm 2, so q^1 coefficient = 0."""
        decomp = hnc.theta_hecke_decomposition(24, n_max=5)
        assert decomp['fourier_coeffs'][1] == Fraction(0)

    def test_rank24_constant_term(self):
        """Constant term is 1 (the zero vector)."""
        decomp = hnc.theta_hecke_decomposition(24, n_max=5)
        assert decomp['fourier_coeffs'][0] == Fraction(1)

    def test_rank16_is_E8(self):
        """Rank 16: Theta = E_8 (no cusp forms of weight 8)."""
        decomp = hnc.theta_hecke_decomposition(16, n_max=10)
        assert decomp['weight'] == 8
        assert len(decomp['eigenforms']) == 1
        assert decomp['eigenforms'][0]['label'] == 'E_8'

    def test_invalid_rank(self):
        """Rank not divisible by 8 should raise."""
        with pytest.raises(ValueError):
            hnc.theta_hecke_decomposition(10, n_max=5)

    def test_rank24_norm4_vectors(self):
        """Leech lattice has 196560 vectors of norm 4, so q^2 coeff = 196560."""
        decomp = hnc.theta_hecke_decomposition(24, n_max=5)
        assert decomp['fourier_coeffs'][2] == Fraction(196560)


# ============================================================
# 2. Hecke eigenvalues
# ============================================================

class TestHeckeEigenvalues:
    """Verify Hecke eigenvalues for Eisenstein and cusp forms."""

    def test_E4_at_p2(self):
        """E_4 eigenvalue at p=2 is sigma_3(2) = 1 + 8 = 9."""
        evs = hnc.hecke_eigenvalue_at_prime(2, 8)
        assert len(evs) == 1
        assert evs[0]['label'] == 'E_4'
        assert evs[0]['eigenvalue'] == sigma_k(2, 3)
        assert evs[0]['eigenvalue'] == 9

    def test_E4_at_p3(self):
        """E_4 eigenvalue at p=3 is sigma_3(3) = 1 + 27 = 28."""
        evs = hnc.hecke_eigenvalue_at_prime(3, 8)
        assert evs[0]['eigenvalue'] == 28

    def test_E4_at_p5(self):
        """E_4 eigenvalue at p=5 is sigma_3(5) = 1 + 125 = 126."""
        evs = hnc.hecke_eigenvalue_at_prime(5, 8)
        assert evs[0]['eigenvalue'] == 126

    def test_delta_at_p2(self):
        """Delta_12 eigenvalue at p=2 is tau(2) = -24."""
        evs = hnc.hecke_eigenvalue_at_prime(2, 24)
        delta_ev = [e for e in evs if e['label'] == 'Delta_12'][0]
        assert delta_ev['eigenvalue'] == -24
        assert delta_ev['eigenvalue'] == ramanujan_tau(2)

    def test_delta_at_p3(self):
        """Delta_12 eigenvalue at p=3 is tau(3) = 252."""
        evs = hnc.hecke_eigenvalue_at_prime(3, 24)
        delta_ev = [e for e in evs if e['label'] == 'Delta_12'][0]
        assert delta_ev['eigenvalue'] == 252

    def test_delta_at_p5(self):
        """Delta_12 eigenvalue at p=5 is tau(5) = 4830."""
        evs = hnc.hecke_eigenvalue_at_prime(5, 24)
        delta_ev = [e for e in evs if e['label'] == 'Delta_12'][0]
        assert delta_ev['eigenvalue'] == 4830

    def test_not_prime_raises(self):
        """Non-prime input should raise."""
        with pytest.raises(ValueError):
            hnc.hecke_eigenvalue_at_prime(4, 8)

    def test_E12_at_p2(self):
        """E_12 eigenvalue at p=2 is sigma_11(2) = 1 + 2048 = 2049."""
        evs = hnc.hecke_eigenvalue_at_prime(2, 24)
        e12_ev = [e for e in evs if e['label'] == 'E_12'][0]
        assert e12_ev['eigenvalue'] == 1 + 2 ** 11


# ============================================================
# 3. Satake parameters and Ramanujan bound
# ============================================================

class TestSatakeRamanujan:
    """Verify Satake parameters satisfy |alpha|=|beta|=p^{(k-1)/2}."""

    def test_delta_p2_ramanujan(self):
        """Delta at p=2: |alpha| = |beta| = 2^{11/2}."""
        sat = hnc.satake_parameters_at_prime(2, 12, float(ramanujan_tau(2)))
        bound = 2 ** (11.0 / 2.0)
        assert abs(sat['abs_alpha'] - bound) < 1e-6 * bound
        assert abs(sat['abs_beta'] - bound) < 1e-6 * bound
        assert sat['ramanujan_satisfied']

    def test_delta_p3_ramanujan(self):
        """Delta at p=3: |alpha| = |beta| = 3^{11/2}."""
        sat = hnc.satake_parameters_at_prime(3, 12, float(ramanujan_tau(3)))
        bound = 3 ** (11.0 / 2.0)
        assert abs(sat['abs_alpha'] - bound) < 1e-6 * bound
        assert abs(sat['abs_beta'] - bound) < 1e-6 * bound
        assert sat['ramanujan_satisfied']

    def test_delta_p5_ramanujan(self):
        """Delta at p=5: |alpha| = |beta| = 5^{11/2}."""
        sat = hnc.satake_parameters_at_prime(5, 12, float(ramanujan_tau(5)))
        bound = 5 ** (11.0 / 2.0)
        assert abs(sat['abs_alpha'] - bound) < 1e-6 * bound
        assert abs(sat['abs_beta'] - bound) < 1e-6 * bound
        assert sat['ramanujan_satisfied']

    def test_delta_p7_ramanujan(self):
        """Delta at p=7: |alpha| = |beta| = 7^{11/2}."""
        sat = hnc.satake_parameters_at_prime(7, 12, float(ramanujan_tau(7)))
        bound = 7 ** (11.0 / 2.0)
        assert abs(sat['abs_alpha'] - bound) < 1e-6 * bound
        assert abs(sat['abs_beta'] - bound) < 1e-6 * bound
        assert sat['ramanujan_satisfied']

    def test_delta_p2_complex_roots(self):
        """Delta at p=2: discriminant < 0, roots are complex conjugates."""
        sat = hnc.satake_parameters_at_prime(2, 12, float(ramanujan_tau(2)))
        # tau(2) = -24, disc = 576 - 4*2048 = 576 - 8192 = -7616 < 0
        assert sat['discriminant'] < 0
        # Complex conjugate pair
        assert abs(sat['alpha'] - sat['beta'].conjugate()) < 1e-10

    def test_delta_product(self):
        """alpha * beta = p^{k-1} = p^11."""
        for p in [2, 3, 5, 7]:
            sat = hnc.satake_parameters_at_prime(p, 12, float(ramanujan_tau(p)))
            expected = p ** 11
            assert abs(sat['product'].real - expected) < 1e-4
            assert abs(sat['product'].imag) < 1e-4

    def test_delta_sum(self):
        """alpha + beta = tau(p)."""
        for p in [2, 3, 5]:
            tau_p = float(ramanujan_tau(p))
            sat = hnc.satake_parameters_at_prime(p, 12, tau_p)
            assert abs(sat['sum'].real - tau_p) < 1e-6
            assert abs(sat['sum'].imag) < 1e-6

    def test_eisenstein_satake(self):
        """E_4 at p=2: eigenvalue = 9, product = 2^3 = 8."""
        sat = hnc.satake_parameters_at_prime(2, 4, 9.0)
        assert abs(sat['product'].real - 8.0) < 1e-6
        assert abs(sat['sum'].real - 9.0) < 1e-6
        # For Eisenstein, discriminant = 81 - 32 = 49 > 0 (real roots)
        assert sat['discriminant'] > 0

    def test_eisenstein_not_ramanujan(self):
        """Eisenstein series do NOT satisfy Ramanujan (alpha=p^{k-1}, beta=1)."""
        sat = hnc.satake_parameters_at_prime(2, 4, 9.0)
        # alpha = (9+7)/2 = 8, beta = (9-7)/2 = 1
        # |alpha| = 8 != 2^{3/2} = 2.828..., so Ramanujan fails
        assert not sat['ramanujan_satisfied']


# ============================================================
# 4. Newton's identities at a prime
# ============================================================

class TestNewtonAtPrime:
    """Verify Newton's identities p_r = e1*p_{r-1} - e2*p_{r-2}."""

    def _make_moments(self, alpha, beta, r_max):
        return {r: hnc.power_sum(alpha, beta, r) for r in range(1, r_max + 1)}

    def test_delta_p2_newton(self):
        """Newton's identities for Delta Satake parameters at p=2."""
        sat = hnc.satake_parameters_at_prime(2, 12, float(ramanujan_tau(2)))
        moments = self._make_moments(sat['alpha'], sat['beta'], 10)
        newton = hnc.newton_identity_at_prime(2, moments, 10)
        for r, info in newton.items():
            assert info['passes'], f"Newton failed at r={r}, defect={info['defect']}"

    def test_delta_p3_newton(self):
        """Newton's identities for Delta Satake parameters at p=3."""
        sat = hnc.satake_parameters_at_prime(3, 12, float(ramanujan_tau(3)))
        moments = self._make_moments(sat['alpha'], sat['beta'], 10)
        newton = hnc.newton_identity_at_prime(3, moments, 10)
        for r, info in newton.items():
            assert info['passes'], f"Newton failed at r={r}, defect={info['defect']}"

    def test_delta_p5_newton(self):
        """Newton's identities for Delta Satake parameters at p=5."""
        sat = hnc.satake_parameters_at_prime(5, 12, float(ramanujan_tau(5)))
        moments = self._make_moments(sat['alpha'], sat['beta'], 10)
        newton = hnc.newton_identity_at_prime(5, moments, 10)
        for r, info in newton.items():
            assert info['passes'], f"Newton failed at r={r}, defect={info['defect']}"

    def test_eisenstein_p2_newton(self):
        """Newton's identities for E_4 Satake parameters at p=2."""
        sat = hnc.satake_parameters_at_prime(2, 4, 9.0)
        moments = self._make_moments(sat['alpha'], sat['beta'], 10)
        newton = hnc.newton_identity_at_prime(2, moments, 10)
        for r, info in newton.items():
            assert info['passes'], f"Newton failed at r={r}, defect={info['defect']}"

    def test_e1_e2_values_delta(self):
        """For Delta at p=2: e1 = tau(2) = -24, e2 = 2^11 = 2048."""
        sat = hnc.satake_parameters_at_prime(2, 12, float(ramanujan_tau(2)))
        moments = self._make_moments(sat['alpha'], sat['beta'], 5)
        newton = hnc.newton_identity_at_prime(2, moments, 5)
        # e1 = alpha + beta = tau(2) = -24
        # e2 = alpha * beta = 2^11 = 2048
        e1 = newton[3]['e1']
        e2 = newton[3]['e2']
        assert abs(e1.real - (-24.0)) < 1e-6
        assert abs(e1.imag) < 1e-6
        assert abs(e2.real - 2048.0) < 1e-4
        assert abs(e2.imag) < 1e-4

    def test_power_sum_basic(self):
        """p_1(a,b) = a+b, p_2(a,b) = a^2+b^2."""
        alpha = complex(3, 4)
        beta = complex(3, -4)
        assert abs(hnc.power_sum(alpha, beta, 1) - (alpha + beta)) < 1e-12
        assert abs(hnc.power_sum(alpha, beta, 2) - (alpha**2 + beta**2)) < 1e-12


# ============================================================
# 5. MC preserves Euler structure
# ============================================================

class TestMCPreservesEuler:
    """Verify MC recursion preserves Newton at each prime."""

    def test_rank8_p2(self):
        """Rank 8 (E_8) at p=2: pure Eisenstein, MC trivially preserves."""
        result = hnc.mc_preserves_euler_at_prime(2, 8.0, 8, r_max=8)
        assert result['all_pass']

    def test_rank8_p3(self):
        result = hnc.mc_preserves_euler_at_prime(3, 8.0, 8, r_max=8)
        assert result['all_pass']

    def test_rank8_p5(self):
        result = hnc.mc_preserves_euler_at_prime(5, 8.0, 8, r_max=8)
        assert result['all_pass']

    def test_rank24_p2(self):
        """Rank 24 (Leech) at p=2: E_12 + Delta, both must pass Newton."""
        result = hnc.mc_preserves_euler_at_prime(2, 24.0, 24, r_max=8)
        assert result['all_pass']
        assert 'E_12' in result['eigenforms']
        assert 'Delta_12' in result['eigenforms']

    def test_rank24_p3(self):
        result = hnc.mc_preserves_euler_at_prime(3, 24.0, 24, r_max=8)
        assert result['all_pass']

    def test_rank24_p5(self):
        result = hnc.mc_preserves_euler_at_prime(5, 24.0, 24, r_max=8)
        assert result['all_pass']

    def test_rank24_delta_satake_ramanujan(self):
        """At each prime, Delta's Satake parameters satisfy Ramanujan."""
        for p in [2, 3, 5, 7, 11]:
            result = hnc.mc_preserves_euler_at_prime(p, 24.0, 24, r_max=6)
            delta_info = result['eigenforms']['Delta_12']
            assert delta_info['satake']['ramanujan_satisfied'], \
                f"Ramanujan failed at p={p}"

    def test_rank24_e12_not_ramanujan(self):
        """Eisenstein E_12 does NOT satisfy Ramanujan."""
        result = hnc.mc_preserves_euler_at_prime(2, 24.0, 24, r_max=6)
        e12_info = result['eigenforms']['E_12']
        assert not e12_info['satake']['ramanujan_satisfied']


# ============================================================
# 6. Full closure verification
# ============================================================

class TestFullClosure:
    """Run the full Hecke-Newton closure verification."""

    def test_rank8_full(self):
        """Full closure for E_8 lattice (rank 8)."""
        result = hnc.full_hecke_newton_closure(8, p_max=20, r_max=8)
        assert result['all_pass']
        assert result['summary']['n_primes'] == 8  # primes up to 20: 2,3,5,7,11,13,17,19

    def test_rank24_full(self):
        """Full closure for Leech lattice (rank 24)."""
        result = hnc.full_hecke_newton_closure(24, p_max=13, r_max=6)
        assert result['all_pass']

    def test_rank16_full(self):
        """Full closure for rank 16 (D_16^+ or E_8+E_8)."""
        result = hnc.full_hecke_newton_closure(16, p_max=10, r_max=6)
        assert result['all_pass']

    def test_rank8_many_primes(self):
        """E_8 with many primes."""
        result = hnc.full_hecke_newton_closure(8, p_max=50, r_max=6)
        assert result['all_pass']
        assert result['summary']['n_primes'] == 15  # primes up to 50

    def test_rank24_high_arity(self):
        """Leech lattice at high arity."""
        result = hnc.full_hecke_newton_closure(24, p_max=7, r_max=10)
        assert result['all_pass']


# ============================================================
# 7. Moment L-function Euler product
# ============================================================

class TestMomentLFunction:
    """Test the moment L-function Euler product computation."""

    def test_rank8_r2_converges(self):
        """M_2(s) for rank 8 should converge for Re(s) large."""
        result = hnc.moment_l_euler_product_lattice(2, complex(5.0, 0.0), 8, p_max=20)
        assert abs(result['value']) > 0
        assert len(result['eigenform_contributions']) == 1

    def test_rank24_r2_two_contributions(self):
        """M_2(s) for rank 24 has two eigenform contributions."""
        result = hnc.moment_l_euler_product_lattice(2, complex(15.0, 0.0), 24, p_max=10)
        assert len(result['eigenform_contributions']) == 2
        labels = {c['label'] for c in result['eigenform_contributions']}
        assert labels == {'E_12', 'Delta_12'}

    def test_rank8_r3(self):
        """M_3(s) for rank 8."""
        result = hnc.moment_l_euler_product_lattice(3, complex(6.0, 0.0), 8, p_max=10)
        assert abs(result['value']) > 0

    def test_invalid_arity(self):
        """Arity < 2 should raise."""
        with pytest.raises(ValueError):
            hnc.moment_l_euler_product_lattice(1, complex(5.0, 0.0), 8)


# ============================================================
# 8. Edge cases and consistency
# ============================================================

class TestEdgeCases:
    """Edge cases and cross-consistency checks."""

    def test_tau_values_match(self):
        """Verify tau values used in tests match ramanujan_tau."""
        assert ramanujan_tau(1) == 1
        assert ramanujan_tau(2) == -24
        assert ramanujan_tau(3) == 252
        assert ramanujan_tau(4) == -1472
        assert ramanujan_tau(5) == 4830

    def test_sigma3_values(self):
        """sigma_3(p) for small primes."""
        assert sigma_k(2, 3) == 1 + 8  # = 9
        assert sigma_k(3, 3) == 1 + 27  # = 28
        assert sigma_k(5, 3) == 1 + 125  # = 126

    def test_leech_q2_coefficient(self):
        """Cross-check: E_12(q^2 coeff) - (65520/691)*tau(2) = 196560."""
        e12_2 = Fraction(-24, 1) * Fraction(-691, 12)  # = 24*691/12 = 2*691 = 1382? No.
        # Direct: E_12 = 1 + (-24/B_12) * sum sigma_11(n) q^n
        # B_12 = -691/2730
        # -24/B_12 = -24 / (-691/2730) = 24*2730/691 = 65520/691
        # E_12 q^2 coeff = (65520/691) * sigma_11(2) = (65520/691) * (1 + 2048) = (65520/691) * 2049
        from compute.lib.modular_spectral_rigidity import eisenstein_coefficient
        e12_2 = eisenstein_coefficient(12, 2)
        tau_2 = ramanujan_tau(2)
        c_delta = Fraction(-65520, 691)
        leech_2 = e12_2 + c_delta * Fraction(tau_2)
        assert leech_2 == Fraction(196560)

    def test_satake_p2_delta_disc_negative(self):
        """At p=2 for Delta_12, discriminant is negative (complex Satake)."""
        tau_2 = -24.0
        disc = tau_2**2 - 4 * (2**11)
        # 576 - 8192 = -7616
        assert disc < 0
        assert disc == 576 - 8192

    def test_newton_identity_algebraic(self):
        """Direct algebraic verification of Newton's identity."""
        # alpha = 3+4j, beta = 3-4j
        alpha = complex(3, 4)
        beta = complex(3, -4)
        e1 = alpha + beta  # 6
        e2 = alpha * beta  # 9 + 16 = 25
        for r in range(3, 10):
            p_r = alpha**r + beta**r
            p_r1 = alpha**(r-1) + beta**(r-1)
            p_r2 = alpha**(r-2) + beta**(r-2)
            assert abs(p_r - (e1 * p_r1 - e2 * p_r2)) < 1e-6
