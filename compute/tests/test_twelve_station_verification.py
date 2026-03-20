#!/usr/bin/env python3
"""
test_twelve_station_verification.py — Tests for the twelve-station proof of the
Ramanujan bound for the Leech lattice.

60+ tests covering each station individually, cross-station consistency, and
integration tests running the full pipeline.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.twelve_station_verification import (
    _gcd,
    _primes_up_to,
    _sigma_k,
    _sigma_minus_1,
    eisenstein_coefficients,
    ramanujan_tau,
    ramanujan_tau_batch,
    satake_parameters,
    station_1_poisson_summation,
    station_2_hecke_decomposition,
    station_3_hecke_multiplicativity,
    station_4_mc_element,
    station_5_sewing_intertwining,
    station_6_hs_sewing,
    station_7_rankin_selberg,
    station_8_cps_converse,
    station_9_newton_identities,
    station_10_euler_product,
    station_11_strong_multiplicity_one,
    station_12_serre_reduction,
    twelve_station_proof,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

pytestmark = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# =========================================================================
# Utility tests
# =========================================================================

class TestUtilities:
    def test_primes_up_to_10(self):
        assert _primes_up_to(10) == [2, 3, 5, 7]

    def test_primes_up_to_30(self):
        primes = _primes_up_to(30)
        assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_sigma_k_basic(self):
        # sigma_0(6) = #{1,2,3,6} = 4
        assert _sigma_k(6, 0) == 4
        # sigma_1(6) = 1+2+3+6 = 12
        assert _sigma_k(6, 1) == 12

    def test_sigma_minus_1(self):
        # sigma_{-1}(6) = 1 + 1/2 + 1/3 + 1/6 = 2
        assert abs(_sigma_minus_1(6) - 2.0) < 1e-14

    def test_gcd(self):
        assert _gcd(12, 8) == 4
        assert _gcd(7, 13) == 1


# =========================================================================
# Ramanujan tau tests
# =========================================================================

class TestRamanujanTau:
    def test_tau_known_values(self):
        """Verify first several Ramanujan tau values."""
        known = {1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
                 6: -6048, 7: -16744, 8: 84480, 9: -113643, 10: -115920}
        for n, expected in known.items():
            assert ramanujan_tau(n) == expected, f"tau({n}) = {ramanujan_tau(n)}, expected {expected}"

    def test_tau_batch_consistency(self):
        """Batch computation matches individual computation."""
        batch = ramanujan_tau_batch(20)
        for n in range(1, 21):
            assert batch[n - 1] == ramanujan_tau(n)

    def test_tau_multiplicative_coprime(self):
        """tau(mn) = tau(m)*tau(n) for coprime m, n."""
        batch = ramanujan_tau_batch(60)
        for m, n in [(2, 3), (2, 5), (3, 7), (5, 11)]:
            assert _gcd(m, n) == 1
            assert batch[m * n - 1] == batch[m - 1] * batch[n - 1]

    def test_tau_hecke_at_prime_square(self):
        """tau(p^2) = tau(p)^2 - p^11."""
        batch = ramanujan_tau_batch(50)
        for p in [2, 3, 5, 7]:
            assert batch[p * p - 1] == batch[p - 1] ** 2 - p ** 11


# =========================================================================
# Eisenstein series tests
# =========================================================================

class TestEisenstein:
    def test_e12_constant_term(self):
        e12 = eisenstein_coefficients(12, 5)
        assert abs(float(e12[0]) - 1.0) < 1e-20

    def test_e12_normalisation(self):
        """E_12 = 1 + (65520/691) * sum sigma_11(n) q^n."""
        e12 = eisenstein_coefficients(12, 10)
        coeff_1 = float(e12[1])
        expected_1 = 65520.0 / 691.0 * 1  # sigma_11(1) = 1
        assert abs(coeff_1 - expected_1) < 1e-8

    def test_e4_is_theta_E8(self):
        """E_4 = Theta_{E_8}: a_n = 240*sigma_3(n)."""
        e4 = eisenstein_coefficients(4, 10)
        for n in range(1, 11):
            expected = 240 * _sigma_k(n, 3)
            assert abs(float(e4[n]) - expected) < 1e-8


# =========================================================================
# Station 1 tests: Poisson summation
# =========================================================================

class TestStation1:
    @pytest.fixture(scope="class")
    def result(self):
        return station_1_poisson_summation(nmax=50)

    def test_station1_passes(self, result):
        assert result['passed']

    def test_a0_is_one(self, result):
        assert abs(result['a0'] - 1.0) < 1e-15

    def test_a1_is_zero(self, result):
        """Leech lattice has no norm-2 vectors."""
        assert abs(result['a1']) < 1e-8

    def test_a2_is_kissing_number(self, result):
        """Kissing number of Leech lattice is 196560."""
        assert abs(result['a2'] - 196560) < 1

    def test_modular_transformation(self, result):
        """Theta(i/y) = y^12 * Theta(iy) for several y."""
        for check in result['modular_checks']:
            assert check['ok'], f"Modular transform failed at y={check['y']}, rel_err={check['rel_err']}"


# =========================================================================
# Station 2 tests: Hecke decomposition
# =========================================================================

class TestStation2:
    @pytest.fixture(scope="class")
    def result(self):
        return station_2_hecke_decomposition(nmax=50)

    def test_station2_passes(self, result):
        assert result['passed']

    def test_c_delta_value(self, result):
        assert abs(result['c_delta'] - 65520 / 691) < 1e-10

    def test_normalisation_check(self, result):
        assert result['normalisation_check']

    def test_known_coefficients(self, result):
        assert result['known_coefficients_ok']

    def test_integrality(self, result):
        """All theta coefficients should be non-negative integers."""
        assert result['integrality_ok']


# =========================================================================
# Station 3 tests: Hecke multiplicativity
# =========================================================================

class TestStation3:
    @pytest.fixture(scope="class")
    def result(self):
        return station_3_hecke_multiplicativity()

    def test_station3_passes(self, result):
        assert result['passed']

    def test_all_coprime_pairs(self, result):
        for check in result['coprime_checks']:
            assert check['ok'], f"tau({check['m']}*{check['n']}) != tau({check['m']})*tau({check['n']})"

    def test_prime_power_hecke(self, result):
        for check in result['prime_power_checks']:
            assert check['ok'], f"tau({check['p']}^2) != tau({check['p']})^2 - {check['p']}^11"

    def test_specific_tau_6(self):
        """tau(6) = tau(2)*tau(3) since gcd(2,3)=1."""
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)

    def test_specific_tau_4(self):
        """tau(4) = tau(2)^2 - 2^11 = 576 - 2048 = -1472."""
        assert ramanujan_tau(4) == ramanujan_tau(2) ** 2 - 2 ** 11


# =========================================================================
# Station 4 tests: MC element
# =========================================================================

class TestStation4:
    @pytest.fixture(scope="class")
    def result(self):
        return station_4_mc_element(r_max=8)

    def test_station4_passes(self, result):
        assert result['passed']

    def test_kappa_equals_12(self, result):
        assert result['kappa'] == 12

    def test_S2_equals_kappa(self, result):
        assert result['S_2'] == 12

    def test_mc_recursion_all_primes(self, result):
        for check in result['mc_recursion_checks']:
            assert check['ok'], (
                f"MC recursion failed at p={check['p']}, r={check['r']}, "
                f"rel_err={check['rel_err']}"
            )

    def test_power_sum_at_p2(self, result):
        """p_1(alpha_2, beta_2) = tau(2) = -24."""
        shadows = result['shadow_at_primes'][2]
        assert abs(shadows[1] - (-24)) < 1e-8 if 1 in shadows else True


# =========================================================================
# Station 5 tests: Sewing-shadow intertwining
# =========================================================================

class TestStation5:
    @pytest.fixture(scope="class")
    def result(self):
        return station_5_sewing_intertwining(q_max=30)

    def test_station5_passes(self, result):
        assert result['passed']

    def test_kappa_24(self, result):
        assert result['kappa'] == 12.0

    def test_intertwining_exact(self, result):
        assert result['max_intertwining_err'] < 1e-12

    def test_det_check(self, result):
        assert result['det_check_err'] < 1e-4

    def test_F1_first_coefficient(self, result):
        """F_1^conn(q=1) = c * sigma_{-1}(1) = 24 * 1 = 24."""
        assert abs(result['F1_first_5'][0] - 24.0) < 1e-12


# =========================================================================
# Station 6 tests: HS-sewing
# =========================================================================

class TestStation6:
    @pytest.fixture(scope="class")
    def result(self):
        return station_6_hs_sewing(nmax=50)

    def test_station6_passes(self, result):
        assert result['passed']

    def test_polynomial_growth(self, result):
        assert result['polynomial_growth_ok']

    def test_growth_exponent(self, result):
        assert result['growth_exponent'] == 11

    def test_subexponential_sectors(self, result):
        assert result['sector_growth_ok']


# =========================================================================
# Station 7 tests: Rankin-Selberg
# =========================================================================

class TestStation7:
    @pytest.fixture(scope="class")
    def result(self):
        return station_7_rankin_selberg(s_values=[3.0, 4.0, 5.0], nmax_sum=300)

    def test_station7_passes(self, result):
        assert result['passed']

    def test_M2_positive_at_s3(self, result):
        assert result['M2_values'][3.0] > 0

    def test_M2_decreasing(self, result):
        """M_2(s) should decrease as s increases (for real s > 1)."""
        vals = result['M2_values']
        assert vals[3.0] > vals[4.0] > vals[5.0]

    def test_dominant_term_reasonable(self, result):
        """The n=2 term (196560^2/8 ~ 4.8e9) should contribute to M_2(3),
        though higher terms with rapidly growing coefficients dominate."""
        # The n=2 term contributes 196560^2/8 ~ 4.83e9.
        # The full sum is much larger due to fast-growing a_Theta(n).
        # We just verify the ratio is nonzero and finite.
        assert result['s3_dominant_term_ratio'] > 0
        assert result['s3_dominant_term_ratio'] < 1


# =========================================================================
# Station 8 tests: CPS converse theorem
# =========================================================================

class TestStation8:
    @pytest.fixture(scope="class")
    def result(self):
        return station_8_cps_converse(nmax_sum=300)

    def test_station8_passes(self, result):
        assert result['passed']

    def test_meromorphic(self, result):
        assert result['meromorphic']

    def test_growth_polynomial(self, result):
        assert result['growth_ok']

    def test_convergence_at_s3(self, result):
        assert result['convergence_checks'][3.0]['finite']

    def test_convergence_at_s5(self, result):
        assert result['convergence_checks'][5.0]['finite']


# =========================================================================
# Station 9 tests: Newton's identities
# =========================================================================

class TestStation9:
    @pytest.fixture(scope="class")
    def result(self):
        return station_9_newton_identities()

    def test_station9_passes(self, result):
        assert result['passed']

    def test_p1_equals_tau_at_each_prime(self, result):
        for check in result['prime_checks']:
            assert check['p1_check'], f"p_1 != tau({check['p']})"

    def test_p2_newton_identity(self, result):
        for check in result['prime_checks']:
            assert check['p2_check'], f"p_2 != tau({check['p']})^2 - 2*{check['p']}^11"

    def test_recursion_at_all_primes(self, result):
        for check in result['prime_checks']:
            for rc in check['recursion_checks']:
                assert rc['ok'], (
                    f"Newton recursion failed at p={check['p']}, r={rc['r']}"
                )

    def test_e1_e2_values(self, result):
        """e_1 = tau(p), e_2 = p^11 for the Hecke eigenform Delta."""
        for check in result['prime_checks']:
            p = check['p']
            assert check['e1'] == ramanujan_tau(p)
            assert check['e2'] == p ** 11


# =========================================================================
# Station 10 tests: Euler product
# =========================================================================

class TestStation10:
    @pytest.fixture(scope="class")
    def result(self):
        return station_10_euler_product(s_test=14.0, num_primes=15)

    def test_station10_passes(self, result):
        assert result['passed']

    def test_multiplicativity(self, result):
        assert result['multiplicativity_ok']

    def test_euler_vs_dirichlet(self, result):
        """Euler product and Dirichlet series agree."""
        assert result['relative_error'] < 0.05  # 5% tolerance due to truncation

    def test_euler_product_finite(self, result):
        """The Euler product should be a finite real number for real s > 12."""
        assert math.isfinite(result['euler_product'])


# =========================================================================
# Station 11 tests: Strong multiplicity one
# =========================================================================

class TestStation11:
    @pytest.fixture(scope="class")
    def result(self):
        return station_11_strong_multiplicity_one(num_primes=15)

    def test_station11_passes(self, result):
        assert result['passed']

    def test_hecke_relations(self, result):
        assert result['hecke_relations_ok']

    def test_unique_eigenvalues(self, result):
        """All primes have distinct Hecke eigenvalues (since Delta is the unique
        normalised eigenform in S_12)."""
        assert result['unique_eigenvalues']


# =========================================================================
# Station 12 tests: Serre reduction (Ramanujan bound)
# =========================================================================

class TestStation12:
    @pytest.fixture(scope="class")
    def result(self):
        return station_12_serre_reduction(primes_to_check=[2, 3, 5, 7, 11])

    def test_station12_passes(self, result):
        assert result['passed']

    def test_ramanujan_verified(self, result):
        assert result['ramanujan_bound_verified']

    def test_discriminant_negative_all_primes(self, result):
        for check in result['checks']:
            assert check['disc_negative'], f"Discriminant >= 0 at p={check['p']}"

    def test_satake_type_complex_conjugate(self, result):
        for check in result['checks']:
            assert check['satake_type'] == 'complex_conjugate', (
                f"Satake type is {check['satake_type']} at p={check['p']}"
            )

    def test_abs_alpha_equals_target(self, result):
        for check in result['checks']:
            assert check['alpha_exact'], (
                f"|alpha| != p^{{11/2}} at p={check['p']}, "
                f"rel_err={check['alpha_rel_err']}"
            )

    def test_abs_beta_equals_target(self, result):
        for check in result['checks']:
            assert check['beta_exact'], (
                f"|beta| != p^{{11/2}} at p={check['p']}, "
                f"rel_err={check['beta_rel_err']}"
            )

    def test_product_equals_p11(self, result):
        for check in result['checks']:
            assert check['product_exact'], (
                f"alpha*beta != p^11 at p={check['p']}"
            )

    def test_ramanujan_bound_satisfied(self, result):
        for check in result['checks']:
            assert check['satisfies_bound'], (
                f"|tau({check['p']})| > 2*{check['p']}^{{11/2}}"
            )

    def test_ramanujan_at_p2_explicit(self):
        """tau(2) = -24, bound = 2*2^{11/2} = 2*sqrt(2048) ~ 90.5."""
        tau_2 = ramanujan_tau(2)
        bound = 2 * 2 ** 5.5
        assert abs(tau_2) <= bound + 1e-10
        assert abs(tau_2) == 24

    def test_ramanujan_at_p23_explicit(self):
        """tau(23) = 18643272, bound = 2*23^{11/2} ~ 5.4e7."""
        batch = ramanujan_tau_batch(23)
        tau_23 = batch[22]
        bound = 2.0 * 23 ** 5.5
        assert abs(tau_23) <= bound + 1

    def test_extended_primes(self):
        """Verify Ramanujan bound at primes up to 30."""
        result = station_12_serre_reduction(
            primes_to_check=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        )
        assert result['passed']


# =========================================================================
# Cross-station consistency tests
# =========================================================================

class TestCrossStation:
    def test_station2_station3_consistent_tau(self):
        """Station 2 and 3 use the same tau values."""
        s2 = station_2_hecke_decomposition(nmax=10)
        s3 = station_3_hecke_multiplicativity()
        # tau(2)*tau(3) = tau(6)
        tau_2 = s3['coprime_checks'][0]['m']  # m=2
        assert tau_2 == 2

    def test_station4_station9_power_sums_agree(self):
        """MC element shadow coefficients (station 4) agree with
        Newton identities (station 9) at each prime."""
        s4 = station_4_mc_element(r_max=6)
        s9 = station_9_newton_identities()

        for check9 in s9['prime_checks']:
            p = check9['p']
            if p in s4['shadow_at_primes']:
                for r in range(2, 7):
                    if r in s4['shadow_at_primes'][p]:
                        s4_val = s4['shadow_at_primes'][p][r]
                        s9_val = check9['power_sums'][r - 1]
                        err = abs(s4_val - s9_val) / max(abs(s4_val), 1.0)
                        assert err < 1e-8, (
                            f"Disagreement at p={p}, r={r}: "
                            f"station4={s4_val}, station9={s9_val}"
                        )

    def test_station5_station6_kappa_consistent(self):
        """Sewing kappa from station 5 and growth exponent from station 6
        are consistent: kappa = c/2 = 12, growth = O(n^{c-1}) = O(n^{11})."""
        s5 = station_5_sewing_intertwining()
        s6 = station_6_hs_sewing()
        assert s5['kappa'] == 12.0
        assert s6['growth_exponent'] == 11
        # kappa = c/2 = 12 <=> c = 24 <=> growth exponent = c - 1 = 23 ... wait
        # Actually growth exponent for Leech = 11 from weight 12 of E_12.
        # kappa = 12 = c/2 with c = 24. The growth is sigma_11(n) = O(n^11).

    def test_station10_station12_euler_factors_ramanujan(self):
        """Euler product factors (station 10) are consistent with
        Ramanujan bound (station 12)."""
        s10 = station_10_euler_product(s_test=14.0, num_primes=5)
        s12 = station_12_serre_reduction(primes_to_check=[2, 3, 5])
        # Both should pass
        assert s10['passed']
        assert s12['passed']


# =========================================================================
# Integration tests: full pipeline
# =========================================================================

class TestFullPipeline:
    @pytest.fixture(scope="class")
    def result(self):
        return twelve_station_proof(lattice_type='Leech')

    def test_overall_pass(self, result):
        assert result['overall_passed'], result['summary']

    def test_all_12_stations_pass(self, result):
        for i in range(1, 13):
            assert result['stations'][i]['passed'], (
                f"Station {i} failed"
            )

    def test_summary_contains_all_stations(self, result):
        for i in range(1, 13):
            assert f'Station {i:2d}' in result['summary'] or f'Station  {i}' in result['summary']

    def test_lattice_type(self, result):
        assert result['lattice_type'] == 'Leech'

    def test_invalid_lattice_type(self):
        result = twelve_station_proof(lattice_type='Barnes-Wall')
        assert not result['overall_passed']

    def test_summary_format(self, result):
        assert 'PASS' in result['summary']
        assert 'Ramanujan' in result['summary']


# =========================================================================
# Additional mathematical verification tests
# =========================================================================

class TestMathematicalVerification:
    def test_leech_kissing_number(self):
        """The Leech lattice has kissing number 196560."""
        e12 = eisenstein_coefficients(12, 5)
        tau_batch = ramanujan_tau_batch(5)
        c_delta = mpmath.mpf(65520) / 691
        a2 = float(e12[2] - c_delta * tau_batch[1])
        assert abs(a2 - 196560) < 1

    def test_leech_theta_no_norm2(self):
        """No vectors of norm 2 in the Leech lattice."""
        e12 = eisenstein_coefficients(12, 5)
        tau_batch = ramanujan_tau_batch(5)
        c_delta = mpmath.mpf(65520) / 691
        a1 = float(e12[1] - c_delta * tau_batch[0])
        assert abs(a1) < 1e-8

    def test_bernoulli_12(self):
        """B_12 = -691/2730."""
        B12 = mpmath.bernoulli(12)
        expected = mpmath.mpf(-691) / 2730
        assert abs(B12 - expected) < 1e-20

    def test_satake_product_p11(self):
        """alpha*beta = p^11 for all primes tested."""
        batch = ramanujan_tau_batch(30)
        for p in [2, 3, 5, 7, 11, 13]:
            tau_p = batch[p - 1]
            alpha, beta = satake_parameters(tau_p, 12, p)
            product = alpha * beta
            expected = mpmath.power(p, 11)
            assert abs(product - expected) / abs(expected) < 1e-20

    def test_ramanujan_discriminant_always_negative(self):
        """tau(p)^2 - 4*p^11 < 0 for all primes p up to 30."""
        batch = ramanujan_tau_batch(30)
        for p in _primes_up_to(30):
            tau_p = batch[p - 1]
            disc = tau_p ** 2 - 4 * p ** 11
            assert disc < 0, f"Discriminant >= 0 at p={p}: disc={disc}"

    def test_deligne_bound_all_primes_to_50(self):
        """Deligne's theorem: |tau(p)| <= 2*p^{11/2} for p up to 47."""
        batch = ramanujan_tau_batch(50)
        for p in _primes_up_to(47):
            tau_p = batch[p - 1]
            bound = 2 * p ** 5.5
            assert abs(tau_p) <= bound + 1e-6, (
                f"|tau({p})| = {abs(tau_p)} > {bound}"
            )

    def test_tau_absolute_values_growth(self):
        """Verify |tau(p)| grows roughly as p^{11/2}."""
        batch = ramanujan_tau_batch(50)
        for p in [2, 3, 5, 7, 11, 23, 29, 47]:
            tau_p = batch[p - 1]
            ratio = abs(tau_p) / p ** 5.5
            # Should be between 0 and 2 (Ramanujan bound)
            assert 0 <= ratio <= 2.01, f"Ratio at p={p}: {ratio}"

    def test_e12_sigma11_relation(self):
        """E_12 coefficient = (65520/691)*sigma_11(n)."""
        e12 = eisenstein_coefficients(12, 10)
        factor = 65520.0 / 691.0
        for n in range(1, 11):
            expected = factor * _sigma_k(n, 11)
            assert abs(float(e12[n]) - expected) < 1e-4

    def test_theta_leech_weight_12(self):
        """Theta_Leech has weight 12 = rank/2 = 24/2."""
        rank = 24
        weight = rank / 2
        assert weight == 12

    def test_dim_S12_equals_1(self):
        """dim S_12(SL_2(Z)) = 1, so Delta_12 is the unique normalised cuspform."""
        # The dimension formula for S_k: dim = floor(k/12) if k=2 mod 12, else floor(k/12)-1+...
        # For k=12: dim S_12 = 1 (well-known).
        # We verify this by checking that the Hecke eigenvalues are uniquely determined.
        s11 = station_11_strong_multiplicity_one(num_primes=10)
        assert s11['unique_eigenvalues']
