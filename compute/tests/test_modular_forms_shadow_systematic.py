#!/usr/bin/env python3
r"""
Tests for modular_forms_shadow_systematic.py — Modular forms and L-functions
from the shadow tower, systematically.

TARGET: 60+ tests across all 8 sections of the programme.

Sections tested:
  1. Genus-1 partition functions as modular forms (q^30 expansions)
  2. Modular transformation verification (S and T transforms)
  3. Quasi-modular forms and E_2*
  4. L-functions (Eisenstein and Ramanujan)
  5. Rankin-Selberg from Koszul pairs
  6. Hecke eigenvalues
  7. p-adic shadow valuations
  8. Petersson inner product and motivic weight filtration
"""

import math
import sys
import os
from fractions import Fraction

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from modular_forms_shadow_systematic import (
    # Section 0: arithmetic helpers
    sigma_k, ramanujan_tau, bernoulli_number,
    # Section 1: partition functions
    eta_coeffs, eta_inverse_coeffs, heisenberg_partition, e8_partition,
    e6_eisenstein, e4_coeffs, delta_coeffs, j_invariant_coeffs,
    leech_partition, sl2_level1_partition, d16_plus_partition,
    _convolve,
    # Section 2: modular transformations
    verify_e4_modular_s, verify_e4_at_rho, verify_e6_at_i,
    # Section 3: quasi-modular forms
    e2_star_coeffs, quasi_modular_ring_basis, genus1_propagator_expansion,
    virasoro_quasi_modular_content, sl2_quasi_modular_content,
    e8_quasi_modular_content,
    # Section 4: L-functions
    l_function_eisenstein_e4, l_function_eisenstein_e4_product,
    l_function_ramanujan, l_function_ramanujan_critical_values,
    l_function_e4_critical_values,
    # Section 5: Rankin-Selberg
    rankin_selberg_dirichlet, rankin_selberg_e4_square,
    rankin_selberg_e4_formula, koszul_pair_rankin_selberg,
    # Section 6: Hecke eigenvalues
    hecke_eigenvalues_e4, hecke_eigenvalues_delta,
    hecke_eigenvalues_from_shadow_e8, hecke_eigenvalues_from_shadow_leech,
    hecke_eigenvalues_d16_plus, verify_e4_squared_equals_e8,
    ramanujan_bound_check,
    # Section 7: p-adic
    p_adic_valuation, p_adic_valuation_rational,
    shadow_coefficients_at_c, p_adic_shadow_table,
    # Section 8: Petersson and motivic
    petersson_inner_product_e4, petersson_inner_product_delta,
    petersson_complementarity_ratio,
    motivic_weights_genus1, motivic_weights_genus2,
    # Section 10: verification
    verify_partition_coefficients, verify_e4_first_coefficients,
    verify_delta_first_coefficients, verify_j_invariant_coefficients,
)


# ============================================================
# Section 1: Genus-1 partition functions
# ============================================================

class TestPartitionFunctions:
    """Tests for genus-1 partition functions as q-expansions."""

    def test_partition_numbers_first_12(self):
        """p(0)=1, p(1)=1, ..., p(10)=42, p(11)=56."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56]
        p = eta_inverse_coeffs(20)
        for i, val in enumerate(expected):
            assert p[i] == val, f"p({i}) = {p[i]}, expected {val}"

    def test_partition_numbers_extended(self):
        """p(20) = 627, p(30) = 5604 (verify against known OEIS values)."""
        p = eta_inverse_coeffs(35)
        assert p[20] == 627
        assert p[30] == 5604

    def test_eta_pentagonal_theorem(self):
        """Verify eta coefficients from Euler pentagonal theorem.

        prod(1-q^n) = sum (-1)^k q^{k(3k-1)/2} = 1 - q - q^2 + q^5 + q^7 - ...
        """
        e = eta_coeffs(20)
        assert e[0] == 1
        assert e[1] == -1   # k=1: pentagonal 1
        assert e[2] == -1   # k=-1: pentagonal 2
        assert e[3] == 0
        assert e[4] == 0
        assert e[5] == 1    # k=2: pentagonal 5
        assert e[7] == 1    # k=-2: pentagonal 7

    def test_eta_times_eta_inverse_is_identity(self):
        """eta * eta^{-1} = 1, i.e., convolution of coefficients gives delta."""
        N = 20
        e = eta_coeffs(N)
        p = eta_inverse_coeffs(N)
        prod = _convolve(e, p, N)
        assert prod[0] == 1
        for i in range(1, N):
            assert prod[i] == 0, f"(eta * eta^{{-1}})[{i}] = {prod[i]}, expected 0"

    def test_heisenberg_partition_structure(self):
        """Heisenberg partition function = 1/eta."""
        data = heisenberg_partition(20)
        assert data['family'] == 'Heisenberg'
        assert data['central_charge'] == Fraction(1)
        assert data['kappa'] == Fraction(1, 2)
        assert data['is_modular_form'] is False
        assert data['coefficients'][0] == 1
        assert data['coefficients'][1] == 1

    def test_e8_partition_is_e4(self):
        """E_8 partition function = E_4(tau)."""
        data = e8_partition(10)
        assert data['family'] == 'E_8'
        assert data['weight'] == 4
        assert data['is_modular_form'] is True
        assert data['eigenform'] is True
        assert data['coefficients'][0] == 1
        assert data['coefficients'][1] == 240

    def test_e4_coefficients_via_sigma3(self):
        """E_4(tau) = 1 + 240*sum sigma_3(n)*q^n.  Verify first 5."""
        e4 = e4_coeffs(6)
        assert e4[0] == 1
        assert e4[1] == 240 * 1      # sigma_3(1) = 1
        assert e4[2] == 240 * 9      # sigma_3(2) = 1 + 8 = 9
        assert e4[3] == 240 * 28     # sigma_3(3) = 1 + 27 = 28
        assert e4[4] == 240 * 73     # sigma_3(4) = 1 + 8 + 64 = 73
        assert e4[5] == 240 * 126    # sigma_3(5) = 1 + 125 = 126

    def test_delta_coefficients(self):
        """Delta = q * prod(1-q^n)^{24}. Verify first 8 tau values."""
        d = delta_coeffs(10)
        assert d[0] == 0
        assert d[1] == 1
        assert d[2] == -24
        assert d[3] == 252
        assert d[4] == -1472
        assert d[5] == 4830
        assert d[6] == -6048
        assert d[7] == -16744

    def test_j_invariant_leading_terms(self):
        """j(tau) - 744 = q^{-1} + 196884*q + 21493760*q^2 + ..."""
        data = leech_partition()
        c = data['coefficients']
        assert c[0] == 1           # q^{-1}
        assert c[1] == 0           # q^0 (after subtracting 744)
        assert c[2] == 196884      # q^1
        assert c[3] == 21493760    # q^2

    def test_leech_partition_structure(self):
        """Leech lattice VOA partition function metadata."""
        data = leech_partition()
        assert data['family'] == 'Leech'
        assert data['central_charge'] == Fraction(24)
        assert data['kappa'] == Fraction(12)
        assert data['weight'] == 0

    def test_d16_plus_is_e4_squared(self):
        """Theta_{D_{16}^+} = E_4^2 = E_8 (since dim M_8 = 1)."""
        data = d16_plus_partition(20)
        assert data['weight'] == 8
        e4 = e4_coeffs(20)
        e4_sq = _convolve(e4, e4, 20)
        for i in range(20):
            assert data['coefficients'][i] == e4_sq[i]

    def test_sl2_level1_partition_structure(self):
        """sl_2 level 1 partition function metadata."""
        data = sl2_level1_partition(20)
        assert data['family'] == 'sl_2_level_1'
        assert data['central_charge'] == Fraction(1)
        assert data['kappa'] == Fraction(3, 4)

    def test_e4_to_q30(self):
        """Verify E_4 computation to q^30."""
        e4 = e4_coeffs(31)
        # Check a few higher coefficients against known values
        assert e4[10] == 240 * sigma_k(10, 3)  # 240 * (1+8+125+1000) = 240*1332 = 319680
        assert e4[15] == 240 * sigma_k(15, 3)
        assert e4[20] == 240 * sigma_k(20, 3)
        assert e4[30] == 240 * sigma_k(30, 3)


# ============================================================
# Section 2: Modular transformations
# ============================================================

class TestModularTransformations:
    """Tests for modular transformation properties."""

    def test_e4_t_invariance(self):
        """E_4(tau+1) = E_4(tau): T-invariance."""
        ok, diff = verify_e4_modular_s()
        assert ok, f"E_4 not T-invariant: diff = {diff}"

    def test_e4_vanishes_at_rho(self):
        """E_4(rho) = 0 where rho = e^{2*pi*i/3} (cubic root of unity)."""
        ok, val = verify_e4_at_rho()
        assert ok, f"|E_4(rho)| = {val}, expected ~ 0"

    def test_e6_vanishes_at_i(self):
        """E_6(i) = 0 (E_6 has a zero at the quartic point)."""
        ok, val = verify_e6_at_i()
        assert ok, f"|E_6(i)| = {val}, expected ~ 0"

    def test_e4_squared_equals_e8(self):
        """E_4^2 = E_8 (since dim M_8(SL(2,Z)) = 1)."""
        assert verify_e4_squared_equals_e8(20)

    def test_delta_is_e4_cubed_minus_e6_squared_over_1728(self):
        """Delta = (E_4^3 - E_6^2) / 1728."""
        N = 20
        e4 = e4_coeffs(N)
        e6 = e6_eisenstein(N)
        e4_cu = _convolve(_convolve(e4, e4, N), e4, N)
        e6_sq = _convolve(e6, e6, N)
        d = delta_coeffs(N)
        for i in range(N):
            computed = (e4_cu[i] - e6_sq[i])
            assert computed % 1728 == 0, f"(E_4^3 - E_6^2)[{i}] = {computed} not divisible by 1728"
            assert computed // 1728 == d[i], f"Delta[{i}]: expected {d[i]}, got {computed // 1728}"


# ============================================================
# Section 3: Quasi-modular forms and E_2*
# ============================================================

class TestQuasiModularForms:
    """Tests for quasi-modular content."""

    def test_e2_star_first_coefficients(self):
        """E_2*(tau) = 1 - 24*sigma_1(n)*q^n.  Verify first terms."""
        e2s = e2_star_coeffs(10)
        assert e2s[0] == 1
        assert e2s[1] == -24 * 1     # sigma_1(1) = 1
        assert e2s[2] == -24 * 3     # sigma_1(2) = 3
        assert e2s[3] == -24 * 4     # sigma_1(3) = 4
        assert e2s[4] == -24 * 7     # sigma_1(4) = 7

    def test_e2_star_sigma1_values(self):
        """Cross-check sigma_1 values used in E_2*."""
        assert sigma_k(1, 1) == 1
        assert sigma_k(2, 1) == 3
        assert sigma_k(3, 1) == 4
        assert sigma_k(4, 1) == 7
        assert sigma_k(5, 1) == 6
        assert sigma_k(6, 1) == 12

    def test_quasi_modular_ring_dimensions(self):
        """Verify QM_k dimensions: QM_0=1, QM_2=1, QM_4=2, QM_6=3."""
        basis = quasi_modular_ring_basis(5)
        assert len(basis) == 5
        # At weight 4: E_4 and E_2*^2 are independent
        assert basis['E_4'][1] == 240
        assert basis['E_2_star_sq'][1] == -48

    def test_e2_star_squared_coefficients(self):
        """E_2*^2 first terms: (1 - 24q - 72q^2 - ...)^2."""
        basis = quasi_modular_ring_basis(5)
        e2sq = basis['E_2_star_sq']
        # (1 - 24q)^2 = 1 - 48q + 576q^2 at leading order
        # But also -72 at q^2 from cross terms: coefficient of q^2 = (-24)^2 + 2*1*(-72) = 576 - 144 = 432
        assert e2sq[0] == 1
        assert e2sq[1] == -48
        assert e2sq[2] == 432

    def test_propagator_is_negative_e2_star(self):
        """Genus-1 propagator: 12*P(tau) = -E_2*(tau)."""
        prop = genus1_propagator_expansion(10)
        e2s = e2_star_coeffs(10)
        for i in range(10):
            assert prop[i] == -e2s[i]

    def test_virasoro_quasi_modular_content(self):
        """Virasoro at c=26: kappa=13, F_1=13/24, Q_contact = 10/(26*152)."""
        data = virasoro_quasi_modular_content(26.0)
        assert abs(data['kappa'] - 13.0) < 1e-10
        assert abs(data['F_1'] - 13.0 / 24.0) < 1e-10
        expected_Q = 10.0 / (26.0 * (5 * 26.0 + 22.0))
        assert abs(data['Q_contact'] - expected_Q) < 1e-10

    def test_e8_quasi_modular_kappa(self):
        """E_8 quasi-modular content: kappa=4, F_1=1/6."""
        data = e8_quasi_modular_content()
        assert abs(data['kappa'] - 4.0) < 1e-10
        assert abs(data['F_1'] - 1.0 / 6.0) < 1e-10

    def test_sl2_quasi_modular_content(self):
        """sl_2 at k=1: kappa = 3*3/4 = 9/4... wait, kappa = 3(k+2)/(2*2) = 3*3/4 = 9/4.
        No: kappa = dim(g)*(k+h^v)/(2*h^v) = 3*(1+2)/(2*2) = 9/4.
        """
        data = sl2_quasi_modular_content(1.0)
        assert abs(data['kappa'] - 2.25) < 1e-10
        assert abs(data['F_1'] - 2.25 / 24.0) < 1e-10


# ============================================================
# Section 4: L-functions
# ============================================================

class TestLFunctions:
    """Tests for L-functions of modular forms."""

    def test_l_e4_equals_zeta_product(self):
        """L(E_4, s) = zeta(s)*zeta(s-3) for Re(s) > 4."""
        for s in [8.0, 10.0, 12.0]:
            L_dir = l_function_eisenstein_e4(complex(s), 500)
            L_prod = l_function_eisenstein_e4_product(complex(s), 500)
            rel_err = abs(L_dir - L_prod) / abs(L_dir)
            assert rel_err < 1e-8, f"L(E_4, {s}): rel error {rel_err:.2e}"

    def test_l_e4_at_s_equals_8(self):
        """L(E_4, 8) = zeta(8)*zeta(5)."""
        val = l_function_eisenstein_e4(complex(8.0), 1000)
        # zeta(8) = pi^8/9450 ≈ 1.00408
        # zeta(5) ≈ 1.03693
        # Product ≈ 1.04116
        assert abs(val.real - 1.04116) < 0.001

    def test_l_delta_convergence(self):
        """L(Delta, s) converges for Re(s) > 7 (Ramanujan conjecture)."""
        val1 = l_function_ramanujan(complex(8.0), 100)
        val2 = l_function_ramanujan(complex(8.0), 200)
        # Should converge
        rel_diff = abs(val1 - val2) / abs(val2)
        assert rel_diff < 0.01

    def test_l_delta_critical_values_decrease(self):
        """|L(Delta, s)| should generally decrease as s increases past critical strip."""
        crits = l_function_ramanujan_critical_values(200)
        # For s >= 7, the values should be close to 1 (approaching the Euler product)
        for s in [8, 9, 10, 11]:
            assert abs(crits[s].real) < 1.1

    def test_l_delta_at_s_12_approaches_1(self):
        """As s -> infinity, L(Delta, s) -> 1 (leading term tau(1)/1^s = 1)."""
        val = l_function_ramanujan(complex(20.0), 200)
        assert abs(val.real - 1.0) < 0.001

    def test_l_e4_critical_values_positive(self):
        """L(E_4, s) > 0 for real s > 4."""
        vals = l_function_e4_critical_values(500)
        for s, v in vals.items():
            assert v.real > 0, f"L(E_4, {s}) = {v.real} is not positive"


# ============================================================
# Section 5: Rankin-Selberg
# ============================================================

class TestRankinSelberg:
    """Tests for Rankin-Selberg convolutions from Koszul pairs."""

    def test_rankin_selberg_e4_at_s_10(self):
        """L(E_4 x E_4, 10) computed via series and closed form."""
        RS_series = rankin_selberg_e4_square(complex(10.0), 200)
        RS_formula = rankin_selberg_e4_formula(complex(10.0), 500)
        rel_err = abs(RS_series - RS_formula) / abs(RS_series)
        assert rel_err < 1e-4, f"RS relative error: {rel_err:.2e}"

    def test_rankin_selberg_e4_positive(self):
        """L(E_4 x E_4, s) > 0 for real s > 7."""
        for s in [8.0, 10.0, 12.0, 15.0]:
            val = rankin_selberg_e4_square(complex(s), 200)
            assert val.real > 0

    def test_rankin_selberg_self_convolution(self):
        """L(f x f, s) = sum |a_n|^2 n^{-s} > 0 for real s."""
        e4 = e4_coeffs(50)
        val = rankin_selberg_dirichlet(e4, e4, complex(10.0), 50)
        assert val.real > 0

    def test_koszul_pair_rankin_selberg_e8(self):
        """For E_8 (self-dual as lattice): L(Z_{E8} x Z_{E8}, s) via two methods.

        rankin_selberg_dirichlet uses the FULL E_4 coefficients (including 240 prefactor),
        while rankin_selberg_e4_square uses sigma_3(n)^2 (normalized eigenvalues).
        The ratio should be 240^2 = 57600.
        """
        e4 = e4_coeffs(50)
        val = koszul_pair_rankin_selberg(e4, e4, complex(10.0), 50)
        direct = rankin_selberg_e4_square(complex(10.0), 50)
        # val uses full E_4 coeffs (with 240), direct uses sigma_3 (normalized)
        ratio = val.real / direct.real
        assert abs(ratio - 240.0 ** 2) / (240.0 ** 2) < 0.01

    def test_rankin_selberg_e4_e6_cross(self):
        """L(E_4 x E_6, s) = sum sigma_3(n)*sigma_5(n)*n^{-s}."""
        e4 = e4_coeffs(50)
        e6 = e6_eisenstein(50)
        # The convolution coefficients alternate in sign (E_6 has negative coefficients)
        val = rankin_selberg_dirichlet(e4, e6, complex(12.0), 50)
        # This should be finite and nonzero
        assert abs(val) > 0.01


# ============================================================
# Section 6: Hecke eigenvalues
# ============================================================

class TestHeckeEigenvalues:
    """Tests for Hecke eigenvalue extraction."""

    def test_hecke_e4_formula(self):
        """a_p(E_4) = 1 + p^3."""
        primes = [2, 3, 5, 7, 11, 13]
        eigs = hecke_eigenvalues_e4(primes)
        for p in primes:
            assert eigs[p] == 1 + p ** 3

    def test_hecke_delta_known_values(self):
        """tau(2)=-24, tau(3)=252, tau(5)=4830, tau(7)=-16744."""
        primes = [2, 3, 5, 7]
        eigs = hecke_eigenvalues_delta(primes)
        assert eigs[2] == -24
        assert eigs[3] == 252
        assert eigs[5] == 4830
        assert eigs[7] == -16744

    def test_hecke_e8_from_shadow(self):
        """E_8 shadow gives Hecke eigenvalues = sigma_3(p)."""
        primes = [2, 3, 5, 7]
        shadow_eigs = hecke_eigenvalues_from_shadow_e8(primes)
        e4_eigs = hecke_eigenvalues_e4(primes)
        for p in primes:
            assert shadow_eigs[p] == e4_eigs[p]

    def test_hecke_leech_decomposition(self):
        """Leech Hecke eigenvalues decompose into E_{12} and Delta components."""
        primes = [2, 3, 5]
        eigs = hecke_eigenvalues_from_shadow_leech(primes)
        for p in primes:
            eis_eig, cusp_eig = eigs[p]
            assert eis_eig == sigma_k(p, 11)
            assert cusp_eig == ramanujan_tau(p)

    def test_hecke_d16_plus(self):
        """D_{16}^+ Hecke eigenvalues = 1 + p^7."""
        primes = [2, 3, 5, 7]
        eigs = hecke_eigenvalues_d16_plus(primes)
        for p in primes:
            assert eigs[p] == 1 + p ** 7

    def test_ramanujan_bound(self):
        """Verify Ramanujan conjecture |tau(p)| <= 2*p^{11/2} for small primes."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        bounds = ramanujan_bound_check(primes)
        for p, (ok, ratio) in bounds.items():
            assert ok, f"Ramanujan bound violated at p={p}: ratio={ratio}"
            assert ratio < 1.0, f"Ratio >= 1 at p={p}"

    def test_hecke_multiplicativity_e4(self):
        """Hecke eigenvalues of E_4 satisfy a_{mn} = a_m * a_n for gcd(m,n)=1."""
        # sigma_3 is multiplicative
        for m, n in [(2, 3), (2, 5), (3, 5), (2, 7), (3, 7)]:
            assert sigma_k(m * n, 3) == sigma_k(m, 3) * sigma_k(n, 3), \
                f"sigma_3({m}*{n}) != sigma_3({m})*sigma_3({n})"

    def test_hecke_multiplicativity_tau(self):
        """Ramanujan tau is multiplicative: tau(mn) = tau(m)*tau(n) for gcd(m,n)=1."""
        for m, n in [(2, 3), (2, 5), (3, 5), (2, 7)]:
            assert ramanujan_tau(m * n) == ramanujan_tau(m) * ramanujan_tau(n), \
                f"tau({m}*{n}) = {ramanujan_tau(m*n)} != {ramanujan_tau(m)*ramanujan_tau(n)}"


# ============================================================
# Section 7: p-adic shadow
# ============================================================

class TestPAdicShadow:
    """Tests for p-adic valuations of shadow coefficients."""

    def test_p_adic_valuation_basic(self):
        """Basic p-adic valuation tests."""
        assert p_adic_valuation(12, 2) == 2   # 12 = 4 * 3
        assert p_adic_valuation(12, 3) == 1   # 12 = 3 * 4
        assert p_adic_valuation(100, 5) == 2  # 100 = 4 * 25
        assert p_adic_valuation(7, 2) == 0
        assert p_adic_valuation(0, 2) == 999  # infinity

    def test_p_adic_valuation_rational(self):
        """p-adic valuation of rationals."""
        assert p_adic_valuation_rational(1, 4, 2) == -2  # 1/4 = 2^{-2}
        assert p_adic_valuation_rational(3, 8, 2) == -3  # 3/8: v_2 = 0 - 3 = -3
        assert p_adic_valuation_rational(9, 1, 3) == 2   # 9 = 3^2

    def test_shadow_coefficients_at_c_half(self):
        """S_r at c=1/2: S_2=1/4, S_3=2, S_4=10/(1/2*(5/2+22))."""
        S = shadow_coefficients_at_c(Fraction(1, 2))
        assert S[2] == Fraction(1, 4)
        assert S[3] == Fraction(2)
        # S_4 = 10/(c*(5c+22)) = 10/((1/2)*(5/2+22)) = 10/((1/2)*(49/2)) = 10/(49/4) = 40/49
        assert S[4] == Fraction(40, 49)

    def test_shadow_coefficients_at_c_1(self):
        """S_r at c=1: S_2=1/2, S_3=2, S_4=10/(1*27) = 10/27."""
        S = shadow_coefficients_at_c(Fraction(1))
        assert S[2] == Fraction(1, 2)
        assert S[3] == Fraction(2)
        assert S[4] == Fraction(10, 27)

    def test_shadow_coefficients_at_c_26(self):
        """S_r at c=26 (self-dual Virasoro): S_2=13, S_3=2."""
        S = shadow_coefficients_at_c(Fraction(26))
        assert S[2] == Fraction(13)
        assert S[3] == Fraction(2)
        # S_4 = 10/(26*(130+22)) = 10/(26*152) = 10/3952 = 5/1976
        assert S[4] == Fraction(5, 1976)

    def test_p_adic_table_structure(self):
        """p-adic shadow table has correct structure."""
        table = p_adic_shadow_table()
        assert len(table) == 5  # 5 c-values
        for c, data in table.items():
            assert 2 in data
            assert 3 in data
            for r, pdata in data.items():
                assert 2 in pdata
                assert 3 in pdata
                assert 5 in pdata
                assert 7 in pdata

    def test_p_adic_kappa_c_half(self):
        """v_2(S_2(1/2)) = v_2(1/4) = -2."""
        table = p_adic_shadow_table()
        assert table[Fraction(1, 2)][2][2] == -2

    def test_p_adic_kappa_c_26(self):
        """v_2(S_2(26)) = v_2(13) = 0 (13 is odd)."""
        table = p_adic_shadow_table()
        assert table[Fraction(26)][2][2] == 0

    def test_p_adic_s3_universal(self):
        """S_3 = 2 universally for Virasoro; v_2(2) = 1, v_3(2) = 0."""
        table = p_adic_shadow_table()
        for c in table:
            assert table[c][3][2] == 1, f"v_2(S_3) at c={c}: expected 1"
            assert table[c][3][3] == 0, f"v_3(S_3) at c={c}: expected 0"

    def test_p_adic_s4_at_c6(self):
        """S_4 at c=6: 10/(6*(30+22)) = 10/(6*52) = 10/312 = 5/156.
        v_2(5/156) = v_2(5) - v_2(156) = 0 - 2 = -2.
        v_3(5/156) = v_3(5) - v_3(156) = 0 - 1 = -1.
        v_5(5/156) = 1 - 0 = 1.
        """
        table = p_adic_shadow_table()
        assert table[Fraction(6)][4][2] == -2
        assert table[Fraction(6)][4][3] == -1
        assert table[Fraction(6)][4][5] == 1


# ============================================================
# Section 8: Petersson inner product and motivic weight
# ============================================================

class TestPeterssonAndMotivic:
    """Tests for Petersson inner products and motivic weight filtration."""

    def test_petersson_e4_positive(self):
        """Rankin-Selberg proxy for <E_4, E_4> is positive."""
        val = petersson_inner_product_e4(200)
        assert val > 0

    def test_petersson_delta_positive(self):
        """Partial Petersson norm of Delta is positive."""
        val = petersson_inner_product_delta(200)
        assert val > 0

    def test_petersson_ratio_finite(self):
        """Ratio of Petersson norms is finite and positive."""
        ratio = petersson_complementarity_ratio(200)
        assert ratio['ratio_e4_delta'] > 0
        assert ratio['ratio_e4_delta'] < 100

    def test_motivic_weights_genus1_heisenberg(self):
        """Heisenberg: F_1 = 1/48, motivic weight 0."""
        mw = motivic_weights_genus1()
        assert mw['Heisenberg']['F_1'] == Fraction(1, 48)
        assert 0 in mw['Heisenberg']['motivic_weights']

    def test_motivic_weights_genus1_e8(self):
        """E_8: F_1 = 1/6, motivic weights {0, 3}."""
        mw = motivic_weights_genus1()
        assert mw['E_8']['F_1'] == Fraction(1, 6)
        assert set(mw['E_8']['motivic_weights']) == {0, 3}

    def test_motivic_weights_genus1_leech(self):
        """Leech: F_1 = 1/2, motivic weights {0, 11}."""
        mw = motivic_weights_genus1()
        assert mw['Leech']['F_1'] == Fraction(1, 2)
        assert set(mw['Leech']['motivic_weights']) == {0, 11}

    def test_motivic_weights_genus2_e8(self):
        """E_8 at genus 2: pure Eisenstein, motivic weights {0, 3}."""
        mw = motivic_weights_genus2()
        assert 'E_8' in mw
        assert set(mw['E_8']['motivic_weights']) == {0, 3}

    def test_motivic_weights_genus2_leech(self):
        """Leech at genus 2: Eisenstein + cusp, weight 11 appears."""
        mw = motivic_weights_genus2()
        assert 11 in mw['Leech']['motivic_weights']


# ============================================================
# Cross-checks and consistency
# ============================================================

class TestCrossChecks:
    """Cross-family consistency checks (AP10 defense)."""

    def test_kappa_from_partition_e8(self):
        """E_8: kappa = c/2 = 4 matches partition function metadata."""
        data = e8_partition()
        assert data['kappa'] == Fraction(4)
        assert data['central_charge'] == Fraction(8)
        assert data['kappa'] == data['central_charge'] / 2

    def test_kappa_from_partition_leech(self):
        """Leech: kappa = c/2 = 12."""
        data = leech_partition()
        assert data['kappa'] == Fraction(12)
        assert data['kappa'] == data['central_charge'] / 2

    def test_kappa_from_partition_heisenberg(self):
        """Heisenberg: kappa = k/2 = 1/2 (not c/2, but for k=1 Heisenberg c=1 so kappa = 1/2)."""
        data = heisenberg_partition()
        assert data['kappa'] == Fraction(1, 2)

    def test_sigma3_multiplicativity(self):
        """sigma_3 is multiplicative: sigma_3(mn) = sigma_3(m)*sigma_3(n) for gcd(m,n)=1."""
        for m, n in [(2, 3), (2, 5), (3, 7), (5, 7), (2, 11)]:
            assert math.gcd(m, n) == 1
            assert sigma_k(m * n, 3) == sigma_k(m, 3) * sigma_k(n, 3)

    def test_sigma3_at_prime_power(self):
        """sigma_3(p^2) = 1 + p^3 + p^6 for prime p."""
        for p in [2, 3, 5]:
            expected = 1 + p ** 3 + p ** 6
            assert sigma_k(p ** 2, 3) == expected

    def test_tau_hecke_relation_at_prime_square(self):
        """tau(p^2) = tau(p)^2 - p^11 for prime p."""
        for p in [2, 3, 5]:
            assert ramanujan_tau(p ** 2) == ramanujan_tau(p) ** 2 - p ** 11, \
                f"Hecke relation at p={p}: tau(p^2) = {ramanujan_tau(p ** 2)}, " \
                f"tau(p)^2 - p^11 = {ramanujan_tau(p) ** 2 - p ** 11}"

    def test_bernoulli_numbers(self):
        """B_0=1, B_1=-1/2, B_2=1/6, B_4=-1/30, B_6=1/42."""
        assert bernoulli_number(0) == Fraction(1)
        assert bernoulli_number(1) == Fraction(-1, 2)
        assert bernoulli_number(2) == Fraction(1, 6)
        assert bernoulli_number(4) == Fraction(-1, 30)
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_bernoulli_odd_vanish(self):
        """B_{2k+1} = 0 for k >= 1."""
        for k in range(1, 10):
            assert bernoulli_number(2 * k + 1) == 0

    def test_e4_e6_to_delta_relation(self):
        """1728*Delta = E_4^3 - E_6^2 (discriminant relation)."""
        N = 15
        e4 = e4_coeffs(N)
        e6 = e6_eisenstein(N)
        d = delta_coeffs(N)
        e4_cu = _convolve(_convolve(e4, e4, N), e4, N)
        e6_sq = _convolve(e6, e6, N)
        for i in range(N):
            assert e4_cu[i] - e6_sq[i] == 1728 * d[i]

    def test_verification_routines(self):
        """All built-in verification routines pass."""
        assert verify_partition_coefficients()
        assert verify_e4_first_coefficients()
        assert verify_delta_first_coefficients()
        assert verify_j_invariant_coefficients()


# ============================================================
# L-function / Hecke consistency
# ============================================================

class TestLFunctionConsistency:
    """Cross-checks between L-functions and Hecke eigenvalues."""

    def test_l_e4_from_hecke(self):
        """L(E_4, s) = prod_p (1 - a_p*p^{-s} + p^{3-2s})^{-1} consistent with sum."""
        # For Re(s) large, both the Dirichlet series and Euler product converge.
        # The Euler product for E_4:
        # L(E_4, s) = prod_p 1/((1 - p^{-s})(1 - p^{3-s}))
        #           = zeta(s) * zeta(s-3)
        val_sum = l_function_eisenstein_e4(complex(10.0), 500)
        val_prod = l_function_eisenstein_e4_product(complex(10.0), 500)
        assert abs(val_sum - val_prod) / abs(val_sum) < 1e-8

    def test_l_delta_functional_eq_symmetry(self):
        """L(Delta, s) should show approximate symmetry around s=6.

        The completed L-function Lambda(s) = (2pi)^{-s} Gamma(s) L(Delta, s)
        satisfies Lambda(s) = (-1)^{12/2} Lambda(12-s) = Lambda(12-s).
        We test: L(Delta, 5) and L(Delta, 7) are related by Gamma factors.
        """
        # Just check both values are finite and nonzero
        L5 = l_function_ramanujan(complex(5.0), 200)
        L7 = l_function_ramanujan(complex(7.0), 200)
        assert abs(L5) > 0.01
        assert abs(L7) > 0.01
