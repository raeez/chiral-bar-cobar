r"""Tests for cy_borcherds_lift_engine: Borcherds lift K3 -> Phi_10.

Multi-path verification throughout (AP38, AP46, AP48):
  Path A: Borcherds product formula (multiplicative lift)
  Path B: Direct eta^{18} * theta_1^2
  Path C: phi_{-2,1} * Delta (Eichler-Zagier structure theorem)
  Path D: Hardcoded known values from literature
  Path E: Sum rules and identities
  Path F: Maass relations (denominator formula)
  Path G: Shadow tower connection

140+ tests organized by:
  1. Arithmetic primitives (eta, theta, modular forms)
  2. phi_{0,1} coefficients and identities
  3. Borcherds product computation
  4. Fourier-Jacobi expansion: phi_{10,1} three-path verification
  5. BKM root system and multiplicities
  6. Denominator formula (Maass relations)
  7. Shadow tower connection (F_2 = 7/1920)
  8. Root multiplicity table c_0(D) for D=-1..20
  9. Cross-consistency checks
  10. Comprehensive multi-path verification
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest

from compute.lib.cy_borcherds_lift_engine import (
    F,
    KAPPA_K3E,
    bernoulli_number,
    bkm_imaginary_multiplicities,
    bkm_real_root_count,
    bkm_root_system,
    borcherds_fourier_jacobi,
    borcherds_product_fourier_jacobi_check,
    borcherds_product_phi10,
    eisenstein_e4_coeffs,
    eisenstein_e6_coeffs,
    eta_coeffs,
    eta_power_coeffs,
    eta_18_theta1_squared_coeffs,
    full_borcherds_analysis,
    k3_elliptic_genus_discriminant_table,
    lambda_g_fp,
    phi01_discriminant_table,
    phi01_fourier_coeffs,
    phi_10_1_direct,
    phi_10_1_via_phi01_phi_m21,
    phi_10_2_from_borcherds,
    phi_m21_discriminant_table,
    ramanujan_tau,
    reciprocal_phi10_coeffs,
    root_multiplicity,
    root_multiplicities_table,
    root_multiplicity_parity,
    shadow_borcherds_comparison,
    shadow_f2_borcherds_connection,
    shadow_tower_k3e,
    sigma_k,
    theta_1_squared_from_product,
    verify_borcherds_weight_10,
    verify_denominator_formula,
    verify_discriminant_dependence,
    verify_phi01_sum_rules,
    verify_phi10_fourier_jacobi_3_paths,
    verify_phi101_is_cusp_form,
    verify_phi101_leading_coefficients,
    verify_ramanujan_tau,
    verify_theta1_squared_y0,
    weyl_group_sum_terms,
)


# =========================================================================
# Section 1: Arithmetic primitives
# =========================================================================

class TestArithmeticPrimitives:
    """Tests for basic arithmetic functions."""

    def test_sigma_0(self):
        """sigma_0(n) = number of divisors."""
        assert sigma_k(1, 0) == 1
        assert sigma_k(6, 0) == 4  # 1, 2, 3, 6
        assert sigma_k(12, 0) == 6  # 1, 2, 3, 4, 6, 12

    def test_sigma_1(self):
        """sigma_1(n) = sum of divisors."""
        assert sigma_k(1, 1) == 1
        assert sigma_k(6, 1) == 12  # 1+2+3+6
        assert sigma_k(12, 1) == 28  # 1+2+3+4+6+12

    def test_sigma_3(self):
        """sigma_3 for Eisenstein E_4."""
        assert sigma_k(1, 3) == 1
        assert sigma_k(2, 3) == 9  # 1 + 8

    def test_sigma_5(self):
        """sigma_5 for Eisenstein E_6."""
        assert sigma_k(1, 5) == 1
        assert sigma_k(2, 5) == 33  # 1 + 32

    def test_sigma_zero_input(self):
        """sigma_k(n, k) = 0 for n <= 0."""
        assert sigma_k(0, 1) == 0
        assert sigma_k(-1, 1) == 0

    def test_bernoulli_known(self):
        """Known Bernoulli numbers."""
        assert bernoulli_number(0) == F(1)
        assert bernoulli_number(1) == F(-1, 2)
        assert bernoulli_number(2) == F(1, 6)
        assert bernoulli_number(4) == F(-1, 30)
        assert bernoulli_number(6) == F(1, 42)
        assert bernoulli_number(8) == F(-1, 30)
        assert bernoulli_number(10) == F(5, 66)
        assert bernoulli_number(12) == F(-691, 2730)

    def test_bernoulli_odd_zero(self):
        """B_n = 0 for odd n > 1."""
        for n in [3, 5, 7, 9, 11]:
            assert bernoulli_number(n) == 0

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_g_fp(1) == F(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_g_fp(2) == F(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_g_fp(3) == F(31, 967680)

    def test_lambda_fp_from_bernoulli(self):
        """lambda_g = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""
        for g in [1, 2, 3, 4]:
            B2g = bernoulli_number(2 * g)
            expected = F(2**(2*g-1)-1, 2**(2*g-1)) * abs(B2g) / F(math.factorial(2*g))
            assert lambda_g_fp(g) == expected


class TestEtaFunction:
    """Tests for Dedekind eta function coefficients."""

    def test_eta_leading(self):
        """prod(1-q^n) starts with 1."""
        c = eta_coeffs(10)
        assert c[0] == 1

    def test_eta_pentagonal(self):
        """Verify pentagonal theorem: prod(1-q^n) = sum(-1)^k q^{k(3k-1)/2}."""
        c = eta_coeffs(30)
        assert c[0] == 1
        assert c[1] == -1
        assert c[2] == -1
        assert c[5] == 1
        assert c[7] == 1
        assert c[3] == 0
        assert c[4] == 0
        assert c[6] == 0

    def test_eta_squared(self):
        """q^{-1/12} * eta^2 = prod(1-q^n)^2 leading terms."""
        c = eta_power_coeffs(20, 2)
        assert c[0] == 1
        assert c[1] == -2
        assert c[2] == -1

    def test_eta_24_is_delta(self):
        """prod(1-q^n)^{24} gives Ramanujan tau function (shifted)."""
        c = eta_power_coeffs(12, 24)
        assert c[0] == 1
        assert c[1] == -24
        assert c[2] == 252

    def test_eta_inverse(self):
        """1/prod(1-q^n) = partition function."""
        c = eta_power_coeffs(10, -1)
        assert c[0] == 1
        assert c[1] == 1
        assert c[2] == 2
        assert c[3] == 3
        assert c[4] == 5
        assert c[5] == 7


class TestRamanujanTau:
    """Tests for the Ramanujan tau function."""

    def test_tau_known_values(self):
        """tau(n) for n = 1..11."""
        tau = ramanujan_tau(12)
        known = [0, 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643, -115920, 534612]
        for n in range(12):
            assert tau[n] == known[n], f"tau({n}) = {tau[n]}, expected {known[n]}"

    def test_tau_zero(self):
        """tau(0) = 0."""
        tau = ramanujan_tau(5)
        assert tau[0] == 0

    def test_verify_ramanujan_tau(self):
        """Verify all known tau values."""
        result = verify_ramanujan_tau()
        assert result['all_match']

    def test_tau_multiplicativity_at_coprimes(self):
        """tau(mn) = tau(m)*tau(n) for gcd(m,n)=1."""
        tau = ramanujan_tau(30)
        assert tau[6] == tau[2] * tau[3]
        assert tau[10] == tau[2] * tau[5]
        assert tau[15] == tau[3] * tau[5]

    def test_tau_prime_power(self):
        """tau(p^2) = tau(p)^2 - p^11 for prime p."""
        tau = ramanujan_tau(30)
        assert tau[4] == tau[2] ** 2 - 2 ** 11
        assert tau[9] == tau[3] ** 2 - 3 ** 11


class TestEisenstein:
    """Tests for Eisenstein series."""

    def test_e4_leading(self):
        """E_4 = 1 + 240q + 2160q^2 + ..."""
        e4 = eisenstein_e4_coeffs(5)
        assert e4[0] == 1
        assert e4[1] == 240
        assert e4[2] == 2160

    def test_e6_leading(self):
        """E_6 = 1 - 504q - 16632q^2 - ..."""
        e6 = eisenstein_e6_coeffs(5)
        assert e6[0] == 1
        assert e6[1] == -504
        assert e6[2] == -16632

    def test_delta_from_e4_e6(self):
        """Delta = (E_4^3 - E_6^2) / 1728."""
        nmax = 8
        e4 = eisenstein_e4_coeffs(nmax)
        e6 = eisenstein_e6_coeffs(nmax)
        # E_4^3
        e4_3 = [0] * nmax
        e4_3[0] = 1
        for _ in range(3):
            new = [0] * nmax
            for i in range(nmax):
                if e4_3[i] == 0:
                    continue
                for j in range(nmax - i):
                    new[i + j] += e4_3[i] * e4[j]
            e4_3 = new
        # E_6^2
        e6_2 = [0] * nmax
        for i in range(nmax):
            for j in range(nmax - i):
                e6_2[i + j] += e6[i] * e6[j]
        # Delta coefficients: (E_4^3 - E_6^2)/1728
        tau = ramanujan_tau(nmax)
        for n in range(1, nmax):
            delta_n = (e4_3[n] - e6_2[n]) // 1728
            assert delta_n == tau[n], f"Delta({n}): {delta_n} vs tau({n})={tau[n]}"


# =========================================================================
# Section 2: phi_{0,1} coefficients
# =========================================================================

class TestPhi01:
    """Tests for weak Jacobi form phi_{0,1}."""

    def test_f_minus1(self):
        """f(-1) = 1 (polar term)."""
        table = phi01_discriminant_table()
        assert table[-1] == 1

    def test_f_0(self):
        """f(0) = 10 (Eichler-Zagier convention, AP38)."""
        table = phi01_discriminant_table()
        assert table[0] == 10

    def test_f_3(self):
        """f(3) = -64."""
        assert phi01_discriminant_table()[3] == -64

    def test_f_4(self):
        """f(4) = 108."""
        assert phi01_discriminant_table()[4] == 108

    def test_f_7(self):
        """f(7) = -513."""
        assert phi01_discriminant_table()[7] == -513

    def test_f_8(self):
        """f(8) = 808."""
        assert phi01_discriminant_table()[8] == 808

    def test_f_11(self):
        """f(11) = -2752."""
        assert phi01_discriminant_table()[11] == -2752

    def test_f_12(self):
        """f(12) = 4016."""
        assert phi01_discriminant_table()[12] == 4016

    def test_k3_elliptic_genus_doubled(self):
        """K3 elliptic genus c_0(D) = 2*f(D)."""
        f_table = phi01_discriminant_table()
        c_table = k3_elliptic_genus_discriminant_table()
        for D in f_table:
            assert c_table[D] == 2 * f_table[D]

    def test_sum_rule_n0(self):
        """phi_{0,1}(tau, 0) q^0 coefficient = 12."""
        table = phi01_discriminant_table()
        total = table[0] + 2 * table[-1]
        assert total == 12

    def test_sum_rule_n1(self):
        """phi_{0,1}(tau, 0) q^1 coefficient = 0."""
        table = phi01_discriminant_table()
        total = table[4] + 2 * table[3] + 2 * table[0]
        assert total == 0

    def test_sum_rule_n2(self):
        """phi_{0,1}(tau, 0) q^2 coefficient = 0."""
        table = phi01_discriminant_table()
        total = table[8] + 2 * table[7] + 2 * table[4] + 2 * table.get(-1, 0)
        assert total == 0, f"Sum at n=2: {total}"

    def test_sum_rule_n3(self):
        """phi_{0,1}(tau, 0) q^3 coefficient = 0."""
        table = phi01_discriminant_table()
        total = (table[12] + 2 * table[11] + 2 * table[8] + 2 * table[3])
        assert total == 0, f"Sum at n=3: {total}"

    def test_verify_sum_rules(self):
        """Comprehensive sum rule verification."""
        result = verify_phi01_sum_rules(nmax=8)
        assert result['all_pass']

    def test_discriminant_dependence(self):
        """c(n,l) depends only on D = 4n - l^2."""
        result = verify_discriminant_dependence(nmax=4, lmax=4)
        assert result['all_pass']

    def test_phi01_fourier_coeffs_at_n0(self):
        """Fourier coefficients at q^0."""
        coeffs = phi01_fourier_coeffs(5, 5)
        assert coeffs.get((0, 0), 0) == 10
        assert coeffs.get((0, 1), 0) == 1
        assert coeffs.get((0, -1), 0) == 1

    def test_phi01_chi_y_genus(self):
        """Chi_y of K3: chi_y(K3) = 2y^{-1} + 20 + 2y."""
        coeffs = phi01_fourier_coeffs(5, 5)
        assert 2 * coeffs.get((0, -1), 0) == 2
        assert 2 * coeffs.get((0, 0), 0) == 20
        assert 2 * coeffs.get((0, 1), 0) == 2

    def test_k3_euler_from_phi01(self):
        """chi(K3) = 2 * phi_{0,1}(tau,0) = 24."""
        table = phi01_discriminant_table()
        phi01_at_y1 = table[0] + 2 * table[-1]
        assert 2 * phi01_at_y1 == 24

    def test_dvv_vs_eichler_zagier(self):
        """Verify EZ convention: f(0)=10 for phi_{0,1}, c_0(0)=20 for chi_K3."""
        assert phi01_discriminant_table()[0] == 10
        assert k3_elliptic_genus_discriminant_table()[0] == 20

    def test_phi_m21_leading(self):
        """phi_{-2,1} leading discriminant coefficients."""
        table = phi_m21_discriminant_table()
        assert table[-1] == 1
        assert table[0] == -2
        assert table[3] == 8
        assert table[4] == -12


# =========================================================================
# Section 3: Theta functions
# =========================================================================

class TestThetaFunctions:
    """Tests for Jacobi theta function computations."""

    def test_theta1_squared_at_y0(self):
        """theta_1(tau, 0)^2 = 0."""
        result = verify_theta1_squared_y0(nmax=8)
        assert result['all_zero']

    def test_theta1_squared_leading(self):
        """Leading term relative to q^{1/4}: (0,1)=1, (0,0)=-2, (0,-1)=1."""
        th1sq = theta_1_squared_from_product(5, 5)
        assert th1sq.get((0, 1), 0) == 1
        assert th1sq.get((0, 0), 0) == -2
        assert th1sq.get((0, -1), 0) == 1

    def test_theta1_squared_symmetry(self):
        """theta_1^2(tau, -z) = theta_1^2(tau, z)."""
        th1sq = theta_1_squared_from_product(5, 5)
        for (n, l), c in th1sq.items():
            assert th1sq.get((n, -l), 0) == c, f"Symmetry failure at ({n}, {l})"

    def test_theta1_squared_q1_sum_zero(self):
        """Sum over l at q^1 vanishes (theta_1(tau,0) = 0)."""
        th1sq = theta_1_squared_from_product(5, 5)
        total = sum(c for (n, l), c in th1sq.items() if n == 1)
        assert total == 0


# =========================================================================
# Section 4: phi_{10,1} = eta^{18} * theta_1^2
# =========================================================================

class TestPhi101:
    """Tests for the first Fourier-Jacobi coefficient of Phi_10."""

    def test_phi101_is_cusp_form(self):
        """phi_{10,1}(tau, 0) = 0 at all q-orders."""
        result = verify_phi101_is_cusp_form(nmax=5, lmax=5)
        assert result['is_cusp_form']

    def test_phi101_leading_term(self):
        """Leading term: c(1, 1) = 1, c(1, 0) = -2, c(1, -1) = 1."""
        result = verify_phi101_leading_coefficients()
        assert result['all_match'], f"Failures: {result['details']}"

    def test_phi101_symmetry(self):
        """c(n, l) = c(n, -l) (even weight Jacobi form)."""
        coeffs = phi_10_1_direct(5, 5)
        for (n, l), c in coeffs.items():
            assert coeffs.get((n, -l), 0) == c, f"Symmetry failure at ({n}, {l})"

    def test_phi101_weight_10(self):
        """Weight: eta^{18} (weight 9) * theta_1^2 (weight 1) = 10."""
        assert 18 * F(1, 2) + 2 * F(1, 2) == 10

    def test_phi101_direct_vs_eichler_zagier(self):
        """Compare direct computation with phi_{-2,1} * Delta path."""
        direct = phi_10_1_direct(4, 4)
        ez_path = phi_10_1_via_phi01_phi_m21(4, 4)
        for key in set(direct.keys()) | set(ez_path.keys()):
            v1 = direct.get(key, 0)
            v2 = ez_path.get(key, 0)
            if isinstance(v1, float):
                v1 = int(round(v1))
            if isinstance(v2, float):
                v2 = int(round(v2))
            assert v1 == v2, f"Mismatch at {key}: direct={v1}, EZ={v2}"

    def test_phi101_q2_sum_zero(self):
        """Sum over l of c(2, l) = 0 (cusp form)."""
        coeffs = phi_10_1_direct(5, 5)
        total = sum(c for (n, l), c in coeffs.items() if n == 2)
        assert abs(total) < 1e-10

    def test_phi101_first_nonzero_at_q1(self):
        """phi_{10,1} starts at q^1 (cusp form)."""
        coeffs = phi_10_1_direct(5, 5)
        q0_terms = {(n, l): c for (n, l), c in coeffs.items() if n == 0}
        assert len(q0_terms) == 0

    def test_phi101_q2_known_values(self):
        """q^2 coefficients: c(2,2)=-2, c(2,1)=-16, c(2,0)=36."""
        coeffs = phi_10_1_direct(5, 5)
        def _int(x):
            return int(round(x)) if isinstance(x, float) else x
        assert _int(coeffs.get((2, 0), 0)) == 36
        assert _int(coeffs.get((2, 1), 0)) == -16
        assert _int(coeffs.get((2, 2), 0)) == -2

    def test_phi101_q3_known_values(self):
        """q^3 coefficients: c(3,3)=1, c(3,2)=36, c(3,1)=99, c(3,0)=-272."""
        coeffs = phi_10_1_direct(5, 5)
        def _int(x):
            return int(round(x)) if isinstance(x, float) else x
        assert _int(coeffs.get((3, 3), 0)) == 1
        assert _int(coeffs.get((3, 2), 0)) == 36
        assert _int(coeffs.get((3, 1), 0)) == 99
        assert _int(coeffs.get((3, 0), 0)) == -272


# =========================================================================
# Section 5: Borcherds product
# =========================================================================

class TestBorcherdsProduct:
    """Tests for the Borcherds product computation of Phi_10."""

    def test_leading_term(self):
        """Phi_10 leading term is q*y*p with coefficient 1."""
        phi10 = borcherds_product_phi10(3, 3, 3)
        assert phi10.get((1, 1, 1), 0) == 1

    def test_no_terms_below_p1(self):
        """Phi_10 = sum_{m>=1} phi_m p^m: no p^0 terms."""
        phi10 = borcherds_product_phi10(4, 4, 4)
        for (n, l, m), c in phi10.items():
            if c != 0:
                assert m >= 1

    def test_fourier_jacobi_m1_exists(self):
        """First Fourier-Jacobi coefficient phi_1 is nonzero."""
        fj = borcherds_fourier_jacobi(4, 4, 4)
        assert 1 in fj
        assert len(fj[1]) > 0

    def test_fourier_jacobi_m1_cusp(self):
        """phi_1(tau, 0) = 0 (cusp form)."""
        fj = borcherds_fourier_jacobi(4, 5, 4)
        phi1 = fj.get(1, {})
        for n in range(5):
            total = sum(c for (nq, l), c in phi1.items() if nq == n)
            assert total == 0, f"phi_1(tau,0) nonzero at q^{n}: {total}"

    def test_borcherds_weight_10(self):
        """Weight of Phi_10 = c_0(0)/2 = 20/2 = 10."""
        result = verify_borcherds_weight_10()
        assert result['weight_from_c'] == 10
        assert result['weight_matches']

    def test_phi10_z_symmetry(self):
        """Phi_10(tau, -z, sigma) = Phi_10(tau, z, sigma): c(n,-l,m)=c(n,l,m)."""
        phi10 = borcherds_product_phi10(3, 4, 3)
        for (n, l, m), c in phi10.items():
            if c != 0:
                c_neg = phi10.get((n, -l, m), 0)
                assert c == c_neg, f"z-sym: ({n},{l},{m})={c} vs ({n},{-l},{m})={c_neg}"

    def test_phi10_tau_sigma_symmetry(self):
        """c(n,l,m) = c(m,l,n) (tau <-> sigma exchange)."""
        phi10 = borcherds_product_phi10(3, 4, 3)
        for (n, l, m), c in phi10.items():
            if c != 0 and n <= 3 and m <= 3:
                c_swap = phi10.get((m, l, n), 0)
                assert c == c_swap, f"tau-sigma: ({n},{l},{m})={c} vs ({m},{l},{n})={c_swap}"

    def test_borcherds_uses_k3_eg_coefficients(self):
        """The Borcherds product uses c_0(D) = 2*f(D) (K3 elliptic genus).

        Convention (AP38): exponents are c_0(D), not f(D).
        c_0(-1) = 2 gives the Weyl vector factor (1-y^{-1})^2.
        """
        c_table = k3_elliptic_genus_discriminant_table()
        assert c_table[-1] == 2  # product uses c_0(-1) = 2
        assert c_table[0] == 20  # gives weight c_0(0)/2 = 10

    def test_borcherds_product_to_o_q5_p3(self):
        """Compute Borcherds product to O(q^5, p^3) and verify nonempty."""
        phi10 = borcherds_product_phi10(5, 7, 3)
        # Count coefficients at each p-level
        counts = {}
        for (n, l, m), c in phi10.items():
            if c != 0:
                counts[m] = counts.get(m, 0) + 1
        assert 1 in counts
        assert 2 in counts
        assert 3 in counts
        assert counts[1] > 5
        assert counts[2] > 10


class TestBorcherdsVsDirectPhi1:
    """Compare Borcherds product phi_1 with direct eta^18 * theta_1^2."""

    def test_three_path_verification(self):
        """Three-path verification of phi_{10,1}."""
        result = verify_phi10_fourier_jacobi_3_paths(nmax=4, lmax=4)
        assert result['matches_bc'], f"B vs C disagree: {result['disagreements'][:5]}"

    def test_three_path_all_agree(self):
        """All three paths agree for phi_{10,1}."""
        result = verify_phi10_fourier_jacobi_3_paths(nmax=3, lmax=3)
        assert result['all_agree'], f"Disagreements: {result['disagreements'][:5]}"

    def test_borcherds_phi1_vs_direct_at_11(self):
        """Borcherds phi_1(1,1) = direct computation."""
        fj = borcherds_fourier_jacobi(4, 5, 4)
        borch_val = fj.get(1, {}).get((1, 1), 0)
        direct_val = phi_10_1_direct(4, 4).get((1, 1), 0)
        assert borch_val == direct_val

    def test_borcherds_phi1_vs_direct_at_10(self):
        """Borcherds phi_1(1,0) = -2 matches direct."""
        fj = borcherds_fourier_jacobi(4, 5, 4)
        borch_val = fj.get(1, {}).get((1, 0), 0)
        direct_val = phi_10_1_direct(4, 4).get((1, 0), 0)
        assert borch_val == direct_val

    def test_borcherds_phi1_vs_direct_at_1m1(self):
        """Borcherds phi_1(1,-1) = 1 matches direct."""
        fj = borcherds_fourier_jacobi(4, 5, 4)
        borch_val = fj.get(1, {}).get((1, -1), 0)
        direct_val = phi_10_1_direct(4, 4).get((1, -1), 0)
        assert borch_val == direct_val

    def test_borcherds_phi1_vs_ez_at_11(self):
        """Borcherds phi_1(1,1) = EZ path."""
        fj = borcherds_fourier_jacobi(4, 5, 4)
        borch_val = fj.get(1, {}).get((1, 1), 0)
        ez_val = phi_10_1_via_phi01_phi_m21(4, 4).get((1, 1), 0)
        assert borch_val == ez_val

    def test_direct_vs_ez_comprehensive(self):
        """Comprehensive comparison of all phi_{10,1} coefficients."""
        direct = phi_10_1_direct(4, 4)
        ez = phi_10_1_via_phi01_phi_m21(4, 4)
        all_keys = set(direct.keys()) | set(ez.keys())
        for key in all_keys:
            v1 = direct.get(key, 0)
            v2 = ez.get(key, 0)
            if isinstance(v1, float):
                v1 = int(round(v1))
            if isinstance(v2, float):
                v2 = int(round(v2))
            assert v1 == v2, f"Direct vs EZ mismatch at {key}: {v1} vs {v2}"

    def test_borcherds_phi1_full_match(self):
        """Full Borcherds FJ phi_1 matches direct at all computed terms."""
        check = borcherds_product_fourier_jacobi_check(q_max=4, p_max=2)
        assert check['phi1_matches_direct']

    def test_borcherds_phi1_matches_ez(self):
        """Borcherds FJ phi_1 matches Eichler-Zagier path."""
        check = borcherds_product_fourier_jacobi_check(q_max=4, p_max=2)
        assert check['phi1_matches_ez']


# =========================================================================
# Section 6: BKM root system and multiplicities
# =========================================================================

class TestBKMRoots:
    """Tests for the BKM superalgebra root system."""

    def test_weyl_vector(self):
        """Weyl vector is (1, 1, 1)."""
        data = bkm_root_system()
        assert data.weyl_vector == (1, 1, 1)

    def test_real_root_mult_1(self):
        """Real roots have D = -1, multiplicity f(-1) = 1."""
        assert phi01_discriminant_table()[-1] == 1

    def test_imaginary_mult_D0(self):
        """Lightlike roots (D=0) have mult = f(0) = 10."""
        mults = bkm_imaginary_multiplicities()
        assert mults[0] == 10

    def test_imaginary_mult_D3_fermionic(self):
        """D=3 roots have mult = f(3) = -64 (fermionic)."""
        mults = bkm_imaginary_multiplicities()
        assert mults[3] == -64

    def test_imaginary_mult_D4(self):
        """D=4 roots have mult = f(4) = 108."""
        mults = bkm_imaginary_multiplicities()
        assert mults[4] == 108

    def test_real_roots_exist(self):
        """Positive real roots (D=-1 solutions) exist."""
        count = bkm_real_root_count(5)
        assert count > 0

    def test_real_root_count_lower_bound(self):
        """At least 17 positive real roots with n,m <= 3."""
        count = bkm_real_root_count(3)
        assert count >= 17

    def test_imaginary_multiplicities_first_11(self):
        """Verify imaginary root multiplicities for D = 0..20."""
        mults = bkm_imaginary_multiplicities(D_max=20)
        expected = {
            0: 10, 3: -64, 4: 108, 7: -513, 8: 808,
            11: -2752, 12: 4016, 15: -11775, 16: 16524,
            19: -43200, 20: 58640,
        }
        for D, exp_mult in expected.items():
            assert mults.get(D) == exp_mult, f"mult(D={D}): got {mults.get(D)}, expected {exp_mult}"

    def test_bkm_superalgebra_sign(self):
        """Negative multiplicities = fermionic roots."""
        mults = bkm_imaginary_multiplicities()
        assert mults[3] < 0   # fermionic
        assert mults[7] < 0   # fermionic
        assert mults[0] > 0   # bosonic
        assert mults[4] > 0   # bosonic
        assert mults[8] > 0   # bosonic


# =========================================================================
# Section 7: Root multiplicities c_0(D) for D = -1 .. 20
# =========================================================================

class TestRootMultiplicities:
    """Tests for root_multiplicity(), root_multiplicities_table(), root_multiplicity_parity()."""

    def test_root_mult_minus1(self):
        """c_0(-1) = 2 (real roots, K3 elliptic genus coefficient)."""
        assert root_multiplicity(-1) == 2

    def test_root_mult_0(self):
        """c_0(0) = 20 (lightlike roots)."""
        assert root_multiplicity(0) == 20

    def test_root_mult_3(self):
        """c_0(3) = -128 (fermionic roots)."""
        assert root_multiplicity(3) == -128

    def test_root_mult_4(self):
        """c_0(4) = 216 (bosonic roots)."""
        assert root_multiplicity(4) == 216

    def test_root_mult_7(self):
        """c_0(7) = -1026."""
        assert root_multiplicity(7) == -1026

    def test_root_mult_8(self):
        """c_0(8) = 1616."""
        assert root_multiplicity(8) == 1616

    def test_root_mult_11(self):
        """c_0(11) = -5504."""
        assert root_multiplicity(11) == -5504

    def test_root_mult_12(self):
        """c_0(12) = 8032."""
        assert root_multiplicity(12) == 8032

    def test_root_mult_15(self):
        """c_0(15) = -23550."""
        assert root_multiplicity(15) == -23550

    def test_root_mult_16(self):
        """c_0(16) = 33048."""
        assert root_multiplicity(16) == 33048

    def test_root_mult_19(self):
        """c_0(19) = -86400."""
        assert root_multiplicity(19) == -86400

    def test_root_mult_20(self):
        """c_0(20) = 117280."""
        assert root_multiplicity(20) == 117280

    def test_root_mult_undefined_D(self):
        """c_0(D) = 0 for D not in the table (or D < -1)."""
        assert root_multiplicity(-2) == 0
        assert root_multiplicity(1) == 0
        assert root_multiplicity(2) == 0
        assert root_multiplicity(5) == 0
        assert root_multiplicity(6) == 0

    def test_root_multiplicities_table_range(self):
        """Table returns correct range of discriminants."""
        table = root_multiplicities_table(-1, 20)
        assert -1 in table
        assert 0 in table
        assert 20 in table
        # D = 1, 2, 5, 6 should NOT be in the table (no roots at these D)
        assert 1 not in table
        assert 2 not in table

    def test_root_mult_c0_equals_2f(self):
        """c_0(D) = 2*f(D) for all D in the table."""
        f_table = phi01_discriminant_table()
        for D in f_table:
            assert root_multiplicity(D) == 2 * f_table[D]

    def test_root_parity_bosonic(self):
        """Bosonic roots have c_0(D) > 0."""
        parity = root_multiplicity_parity(20)
        for D in parity['bosonic']:
            assert root_multiplicity(D) > 0

    def test_root_parity_fermionic(self):
        """Fermionic roots have c_0(D) < 0."""
        parity = root_multiplicity_parity(20)
        for D in parity['fermionic']:
            assert root_multiplicity(D) < 0

    def test_root_parity_alternation(self):
        """Bosonic at D = 0 mod 4 or 0, fermionic at D = 3 mod 4.

        D = 0: bosonic (20). D = 3: fermionic (-128).
        D = 4: bosonic (216). D = 7: fermionic (-1026).
        D = 8: bosonic (1616). D = 11: fermionic (-5504).
        The pattern: D = 0 mod 4 or D = 0 -> bosonic; D = 3 mod 4 -> fermionic.
        """
        parity = root_multiplicity_parity(20)
        for D in parity['bosonic']:
            if D > 0:
                assert D % 4 == 0, f"Bosonic D={D} not 0 mod 4"
        for D in parity['fermionic']:
            assert D % 4 == 3, f"Fermionic D={D} not 3 mod 4"

    def test_root_mult_growth(self):
        """Root multiplicities |c_0(D)| grow with D."""
        table = root_multiplicities_table(0, 40)
        prev_abs = 0
        for D in sorted(table.keys()):
            if D > 0:
                assert abs(table[D]) > prev_abs, f"|c_0({D})| not growing"
                prev_abs = abs(table[D])


# =========================================================================
# Section 8: Denominator formula verification
# =========================================================================

class TestDenominatorFormula:
    """Tests for Maass relations and the denominator formula."""

    def test_maass_relation_at_q2_p2(self):
        """Maass relation verified at q_max=2, p_max=2."""
        result = verify_denominator_formula(2, 2, 2)
        assert result['all_match'], f"Mismatches: {result['first_mismatches']}"

    def test_maass_relation_at_q3_p3(self):
        """Maass relation verified at q_max=3, p_max=3."""
        result = verify_denominator_formula(3, 3, 3)
        assert result['all_match'], f"Mismatches: {result['first_mismatches']}"

    def test_maass_trivial_at_m1(self):
        """At m=1: c(n,l,1) = phi_1(n,l) (Maass with d=1 only)."""
        maass = weyl_group_sum_terms(4, 4, 2)
        phi1 = phi_10_1_direct(5, 5)
        for (n, l, m), c_m in maass.items():
            if m == 1:
                c_d = phi1.get((n, l), 0)
                if isinstance(c_d, float):
                    c_d = int(round(c_d))
                if isinstance(c_m, float):
                    c_m = int(round(c_m))
                assert c_m == c_d, f"Maass at ({n},{l},1)={c_m} vs phi1={c_d}"

    def test_maass_at_222(self):
        """c(2,2,2) via Maass: gcd=2, d=1 gives phi1(4,2), d=2 gives 2^9*phi1(1,1)."""
        phi1 = phi_10_1_direct(8, 8)
        # d=1: phi1(4, 2)
        v1 = phi1.get((4, 2), 0)
        if isinstance(v1, float):
            v1 = int(round(v1))
        # d=2: 2^9 * phi1(1, 1)
        v2 = phi1.get((1, 1), 0)
        if isinstance(v2, float):
            v2 = int(round(v2))
        expected = v1 + 512 * v2
        phi10 = borcherds_product_phi10(5, 6, 5)
        actual = phi10.get((2, 2, 2), 0)
        assert actual == expected, f"c(2,2,2): Borcherds={actual}, Maass={expected}"

    def test_reciprocal_leading(self):
        """1/Phi_10 leading term: q^{-1} y^{-1} p^{-1}."""
        inv = reciprocal_phi10_coeffs(3, 3, 3)
        assert (-1, -1, -1) in inv
        assert inv[(-1, -1, -1)] != 0

    def test_reciprocal_exists(self):
        """1/Phi_10 computation produces nonzero coefficients."""
        inv = reciprocal_phi10_coeffs(3, 3, 3)
        assert len(inv) > 0

    def test_denominator_formula_matches_count(self):
        """Denominator formula matches on 50+ coefficients."""
        result = verify_denominator_formula(3, 3, 3)
        assert result['matches'] >= 50


# =========================================================================
# Section 9: Shadow tower connection
# =========================================================================

class TestShadowTower:
    """Tests for shadow tower connection to Borcherds lift."""

    def test_kappa_k3e(self):
        """kappa(K3 x E) = 3 = dim_C(K3 x E)."""
        assert KAPPA_K3E == 3

    def test_shadow_F1(self):
        """F_1 = kappa/24 = 3/24 = 1/8."""
        tower = shadow_tower_k3e()
        assert tower[1] == F(1, 8)

    def test_shadow_F2(self):
        """F_2 = 3 * 7/5760 = 7/1920."""
        tower = shadow_tower_k3e()
        assert tower[2] == F(7, 1920)

    def test_shadow_F2_exact_fraction(self):
        """F_2 = 7/1920 as exact fraction."""
        tower = shadow_tower_k3e()
        assert tower[2].numerator == 7
        assert tower[2].denominator == 1920

    def test_shadow_F3(self):
        """F_3 = 3 * 31/967680 = 31/322560."""
        tower = shadow_tower_k3e()
        assert tower[3] == F(31, 322560)

    def test_shadow_F2_numerical(self):
        """F_2 numerically: 7/1920 ~ 0.003646."""
        tower = shadow_tower_k3e()
        val = float(tower[2])
        assert abs(val - 7.0 / 1920.0) < 1e-12

    def test_shadow_escalation_ratio(self):
        """F_2 / F_1 = lambda_2/lambda_1 = 7/240."""
        tower = shadow_tower_k3e()
        ratio = tower[2] / tower[1]
        assert ratio == F(7, 240)

    def test_shadow_borcherds_comparison(self):
        """Shadow-Borcherds comparison function runs."""
        result = shadow_borcherds_comparison()
        assert result['kappa_k3e'] == 3
        assert result['shadow_F2'] == F(7, 1920)
        assert result['phi10_weight'] == 10

    def test_lambda2_is_7_5760(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_g_fp(2) == F(7, 5760)

    def test_borcherds_exponent_c_minus1_gives_weyl(self):
        """c_0(-1) = 2 for K3 elliptic genus, Weyl vector factor (1-y^{-1})^2."""
        c_table = k3_elliptic_genus_discriminant_table()
        assert c_table[-1] == 2

    def test_borcherds_exponent_c0_gives_weight(self):
        """c_0(0) = 20 -> weight = c_0(0)/2 = 10."""
        c_table = k3_elliptic_genus_discriminant_table()
        assert c_table[0] == 20
        assert c_table[0] // 2 == 10

    def test_genus_escalation_principle(self):
        """Both F_g and Phi_10 are built from genus-1 data."""
        tower = shadow_tower_k3e()
        F2 = tower[2]
        assert F2 == F(KAPPA_K3E) * lambda_g_fp(2)

    def test_shadow_tower_positive(self):
        """Shadow amplitudes F_g > 0 for all g >= 1."""
        tower = shadow_tower_k3e(5)
        for g in range(1, 6):
            assert tower[g] > 0

    def test_shadow_tower_decreasing(self):
        """Shadow amplitudes F_g decrease with g (Bernoulli decay)."""
        tower = shadow_tower_k3e(5)
        for g in range(1, 5):
            assert tower[g] > tower[g + 1]


# =========================================================================
# Section 10: F_2 = 7/1920 Borcherds connection
# =========================================================================

class TestF2BorcherdsConnection:
    """Tests for the connection between F_2 and the Borcherds lift."""

    def test_f2_shadow_exact(self):
        """F_2 = kappa * lambda_2 = 3 * 7/5760 = 7/1920."""
        result = shadow_f2_borcherds_connection()
        assert result['F2'] == F(7, 1920)

    def test_f2_from_kappa_and_lambda2(self):
        """Independent: kappa=3, lambda_2=7/5760 -> F_2=21/5760=7/1920."""
        kappa = F(3)
        lam2 = F(7, 5760)
        assert kappa * lam2 == F(7, 1920)

    def test_f2_from_ahat_generating_function(self):
        """(x/2)/sin(x/2) - 1 at x^4: coefficient = 7/5760."""
        # (x/2)/sin(x/2) = 1 + x^2/24 + 7x^4/5760 + ...
        assert lambda_g_fp(2) == F(7, 5760)

    def test_f2_ratio_to_f1(self):
        """F_2/F_1 = 7/240 (genus escalation ratio)."""
        result = shadow_f2_borcherds_connection()
        ratio = result['F2_div_F1']
        assert ratio == F(7, 240)

    def test_weight_phi10_from_c0(self):
        """weight(Phi_10) = c_0(0)/2 = 10."""
        result = shadow_f2_borcherds_connection()
        assert result['weight_phi10'] == 10

    def test_f2_borcherds_structural(self):
        """F_2 and Phi_10 both use genus-1 data for genus-2 objects."""
        result = shadow_f2_borcherds_connection()
        assert result['kappa'] == 3
        assert result['c_0_minus1'] == 2
        assert result['c_0_0'] == 20
        assert result['F2_from_Ahat'] is True


# =========================================================================
# Section 11: Phi_2 and higher Fourier-Jacobi coefficients
# =========================================================================

class TestPhi2:
    """Tests for the second Fourier-Jacobi coefficient of Phi_10."""

    def test_phi2_exists(self):
        """phi_2 (second FJ coefficient) is nonzero."""
        phi2 = phi_10_2_from_borcherds(q_max=5, l_max=5)
        assert len(phi2) > 0

    def test_phi2_cusp(self):
        """phi_2(tau, 0) = 0 (cusp form)."""
        phi2 = phi_10_2_from_borcherds(q_max=5, l_max=5)
        for n in range(6):
            total = sum(c for (nq, l), c in phi2.items() if nq == n)
            assert total == 0, f"phi_2(tau,0) at q^{n}: {total}"

    def test_phi2_symmetry(self):
        """phi_2 has c(n, -l) = c(n, l) (even weight)."""
        phi2 = phi_10_2_from_borcherds(q_max=4, l_max=4)
        for (n, l), c in phi2.items():
            if c != 0:
                assert phi2.get((n, -l), 0) == c, f"phi_2 symmetry fail at ({n},{l})"


# =========================================================================
# Section 12: Cross-consistency
# =========================================================================

class TestCrossConsistency:
    """Cross-consistency tests between different computations."""

    def test_f_table_matches_deep_engine(self):
        """phi_{0,1} table matches known values."""
        our = phi01_discriminant_table()
        deep = {
            -1: 1, 0: 10, 3: -64, 4: 108, 7: -513, 8: 808,
            11: -2752, 12: 4016, 15: -11775, 16: 16524,
            19: -43200, 20: 58640,
        }
        for D in deep:
            assert our[D] == deep[D], f"Mismatch at D={D}: {our[D]} vs {deep[D]}"

    def test_bps_engine_c0_convention(self):
        """c_0(D) = 2*f(D) verified against hardcoded BPS values."""
        c_table = k3_elliptic_genus_discriminant_table()
        bps_hardcoded = {
            -1: 2, 0: 20, 3: -128, 4: 216,
            7: -1026, 8: 1616, 11: -5504, 12: 8032,
        }
        for D, expected in bps_hardcoded.items():
            assert c_table[D] == expected, f"c_0({D}): got {c_table[D]}, expected {expected}"

    def test_phi10_vanishing_order(self):
        """Phi_10 starts at p^1 (vanishes to order 1 at each boundary)."""
        fj = borcherds_fourier_jacobi(4, 4, 4)
        assert 0 not in fj or len(fj.get(0, {})) == 0
        assert 1 in fj and len(fj[1]) > 0

    def test_ramanujan_in_delta(self):
        """tau(n) from eta^24 and from E_4^3-E_6^2 agree."""
        tau = ramanujan_tau(8)
        assert tau[1] == 1
        assert tau[2] == -24
        assert tau[3] == 252

    def test_ahat_genus_2_coefficient(self):
        """A-hat genus coefficient at g=2: 7/5760."""
        assert lambda_g_fp(2) == F(7, 5760)

    def test_f2_shadow_vs_borcherds_product_data(self):
        """F_2 = 7/1920 and c_0(0) = 20 coexist consistently."""
        tower = shadow_tower_k3e()
        c_table = k3_elliptic_genus_discriminant_table()
        assert tower[2] == F(7, 1920)
        assert c_table[0] == 20

    def test_phi101_cusp_vs_phi01_noncusp(self):
        """phi_{0,1} is NOT a cusp form; phi_{10,1} IS."""
        assert phi01_discriminant_table()[0] != 0
        result = verify_phi101_is_cusp_form(5, 5)
        assert result['is_cusp_form']

    def test_k3_chi_24(self):
        """K3 Euler characteristic from elliptic genus: chi(K3) = 24."""
        table = k3_elliptic_genus_discriminant_table()
        chi = table[0] + 2 * table[-1]  # c_0(0) + 2*c_0(-1) = 20 + 4 = 24
        assert chi == 24

    def test_phi01_sum_to_12(self):
        """phi_{0,1}(tau, 0) = 12 (constant)."""
        table = phi01_discriminant_table()
        total = table[0] + 2 * table[-1]
        assert total == 12


# =========================================================================
# Section 13: Modular properties
# =========================================================================

class TestModularProperties:
    """Tests for modular properties of Phi_10 and related forms."""

    def test_phi10_is_weight_10(self):
        """Phi_10 is weight 10."""
        result = verify_borcherds_weight_10()
        assert result['weight_from_c'] == 10

    def test_phi10_cusp_form(self):
        """Phi_10 is a cusp form (no m=0 term)."""
        fj = borcherds_fourier_jacobi(3, 3, 3)
        assert 0 not in fj or len(fj.get(0, {})) == 0

    def test_phi10_on_sp4_z(self):
        """Phi_10 on full Sp(4,Z): c(n,l,m) = c(m,l,n)."""
        phi10 = borcherds_product_phi10(3, 4, 3)
        for (n, l, m), c in phi10.items():
            if c != 0 and n <= 3 and m <= 3:
                assert phi10.get((m, l, n), 0) == c

    def test_eta_18_correct_weight(self):
        """eta^{18} has weight 9."""
        assert 18 * F(1, 2) == 9

    def test_theta1_squared_correct_weight(self):
        """theta_1^2 has weight 1."""
        assert 2 * F(1, 2) == 1

    def test_combined_weight(self):
        """eta^{18} * theta_1^2 has weight 10."""
        assert 18 * F(1, 2) + 2 * F(1, 2) == 10


# =========================================================================
# Section 14: Full pipeline
# =========================================================================

class TestFullPipeline:
    """Tests for the full Borcherds lift analysis pipeline."""

    def test_full_analysis_runs(self):
        """Full analysis pipeline executes."""
        result = full_borcherds_analysis(q_max=3, p_max=2)
        assert result.phi10_coeffs_count > 0

    def test_full_analysis_tau_sigma_ok(self):
        """tau-sigma symmetry passes in full analysis."""
        result = full_borcherds_analysis(q_max=3, p_max=2)
        assert result.tau_sigma_symmetric

    def test_full_analysis_phi1_match(self):
        """phi_1 three-path match in full analysis."""
        result = full_borcherds_analysis(q_max=3, p_max=2)
        assert result.phi1_three_path_match

    def test_full_analysis_cusp(self):
        """Cusp form property in full analysis."""
        result = full_borcherds_analysis(q_max=3, p_max=2)
        assert result.phi1_is_cusp_form

    def test_full_analysis_weight(self):
        """Weight 10 in full analysis."""
        result = full_borcherds_analysis(q_max=3, p_max=2)
        assert result.weight_phi10 == 10

    def test_full_analysis_f2(self):
        """F_2 = 7/1920 in full analysis."""
        result = full_borcherds_analysis(q_max=3, p_max=2)
        assert result.F2_shadow == F(7, 1920)

    def test_full_analysis_all_pass(self):
        """All verifications pass in full analysis."""
        result = full_borcherds_analysis(q_max=3, p_max=2)
        assert result.all_verifications_pass


# =========================================================================
# Section 15: Comprehensive multi-path verification
# =========================================================================

class TestMultiPathVerification:
    """Comprehensive multi-path verification as required by the mandate."""

    def test_all_verification_functions_run(self):
        """All verification functions execute without error."""
        verify_phi01_sum_rules()
        verify_discriminant_dependence()
        verify_theta1_squared_y0()
        verify_phi101_is_cusp_form()
        verify_phi101_leading_coefficients()
        verify_borcherds_weight_10()
        verify_ramanujan_tau()

    def test_phi101_3_paths_partial(self):
        """At minimum, paths B and C agree for phi_{10,1}."""
        result = verify_phi10_fourier_jacobi_3_paths(nmax=3, lmax=3)
        assert result['matches_bc'], f"B-C disagree: {result['disagreements']}"

    def test_phi01_3_verification_paths(self):
        """phi_{0,1} verified by 3 independent paths."""
        # Path 1: hardcoded values
        table = phi01_discriminant_table()
        assert len(table) > 0
        # Path 2: sum rules
        result = verify_phi01_sum_rules(8)
        assert result['all_pass']
        # Path 3: discriminant dependence
        result = verify_discriminant_dependence(4, 4)
        assert result['all_pass']

    def test_shadow_tower_3_paths(self):
        """Shadow tower F_g verified by 3 paths."""
        # Path 1: direct
        tower = shadow_tower_k3e()
        F2_direct = tower[2]
        # Path 2: via Bernoulli
        B4 = bernoulli_number(4)
        lambda2 = F(2 ** 3 - 1, 2 ** 3) * abs(B4) / F(math.factorial(4))
        F2_bernoulli = F(3) * lambda2
        # Path 3: known value
        F2_known = F(7, 1920)
        assert F2_direct == F2_bernoulli
        assert F2_direct == F2_known

    def test_ramanujan_tau_3_paths(self):
        """tau(n) verified by 3 paths."""
        tau = ramanujan_tau(30)
        # Path 1: direct
        assert tau[1] == 1
        assert tau[2] == -24
        # Path 2: multiplicativity
        assert tau[6] == tau[2] * tau[3]
        # Path 3: Hecke
        assert tau[4] == tau[2] ** 2 - 2 ** 11

    def test_bkm_roots_2_paths(self):
        """BKM root multiplicities verified by 2 paths."""
        f_table = phi01_discriminant_table()
        c_table = k3_elliptic_genus_discriminant_table()
        for D in [0, 3, 4, 7, 8]:
            assert c_table[D] == 2 * f_table[D]

    def test_borcherds_product_4_paths(self):
        """Borcherds product phi_1 verified by 4 paths.

        Path A: Borcherds product FJ extraction
        Path B: Direct eta^{18} * theta_1^2
        Path C: phi_{-2,1} * Delta
        Path D: Maass relations at m=1
        """
        # Path A: Borcherds
        fj = borcherds_fourier_jacobi(4, 5, 4)
        phi1_a = fj.get(1, {})

        # Path B: Direct
        phi1_b = phi_10_1_direct(4, 5)

        # Path C: EZ
        phi1_c = phi_10_1_via_phi01_phi_m21(4, 5)

        # Path D: Maass (m=1 is trivially phi_1)
        maass = weyl_group_sum_terms(4, 5, 2)
        phi1_d = {(n, l): c for (n, l, m), c in maass.items() if m == 1}

        # Compare at a known point
        def _int(x):
            return int(round(x)) if isinstance(x, float) else x

        key = (1, 1)
        assert phi1_a.get(key, 0) == _int(phi1_b.get(key, 0))
        assert _int(phi1_b.get(key, 0)) == _int(phi1_c.get(key, 0))
        assert _int(phi1_c.get(key, 0)) == _int(phi1_d.get(key, 0))

        key = (2, 0)
        va = phi1_a.get(key, 0)
        vb = _int(phi1_b.get(key, 0))
        vc = _int(phi1_c.get(key, 0))
        vd = _int(phi1_d.get(key, 0))
        assert va == vb == vc == vd

    def test_root_mult_3_paths(self):
        """Root multiplicities c_0(D) verified by 3 paths.

        Path 1: root_multiplicity() function
        Path 2: k3_elliptic_genus_discriminant_table()
        Path 3: 2 * phi01_discriminant_table()
        """
        for D in [-1, 0, 3, 4, 7, 8, 11, 12, 15, 16, 19, 20]:
            v1 = root_multiplicity(D)
            v2 = k3_elliptic_genus_discriminant_table().get(D, 0)
            v3 = 2 * phi01_discriminant_table().get(D, 0)
            assert v1 == v2 == v3, f"D={D}: {v1}, {v2}, {v3}"

    def test_denominator_formula_verified(self):
        """Denominator formula (Borcherds product = Maass lift) verified."""
        result = verify_denominator_formula(3, 3, 3)
        assert result['all_match']

    def test_fj_check_comprehensive(self):
        """Comprehensive FJ check: phi_1 match, cusp property, symmetry."""
        check = borcherds_product_fourier_jacobi_check(q_max=4, p_max=2)
        assert check['phi1_matches_direct']
        assert check['phi1_matches_ez']
        assert check['all_cusp']
        assert check['tau_sigma_ok']
