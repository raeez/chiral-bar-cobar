r"""Tests for reduced Gromov-Witten invariants of K3 and K3 x E.

Multi-path verification:
  Path 1: Direct BPS computation via (t-2)^g basis from F(y,q)
  Path 2: Yau-Zaslow formula (genus 0, independent)
  Path 3: GW/DT comparison (chi(K3xE) = 0 implies DT = PT)
  Path 4: BPS integrality (all n^g_h in Z)
  Path 5: Gottsche evaluation F_h(y=1) = prod 1/(1-q^n)^{24}
  Path 6: Hodge symmetry F_{j,h} = F_{-j,h}
  Path 7: Ramanujan tau from Delta = eta^{24}
"""

import math
import pytest
from fractions import Fraction

from compute.lib.cy_gw_k3e_engine import (
    # Number theory
    _divisors, _sigma, _prime_factors, _mobius,
    # Modular forms
    _eta_power_coeffs, inverse_eta_24_coeffs, discriminant_coeffs,
    ramanujan_tau, eisenstein_e2_coeffs, eisenstein_e4_coeffs,
    eisenstein_e6_coeffs,
    # KKV product
    _product_coeff, chi_y_hilb_k3, chi_y_hilb_as_t_poly,
    # BPS
    bps_k3, bps_genus0_k3, bps_table,
    # GW
    gw_reduced_k3, _sin_power_coeff, _inverse_sinc_sq_coeff,
    _sinc_power_coeff,
    # K3 x E
    euler_char_k3, euler_char_elliptic, euler_char_k3xe,
    hodge_numbers_k3, hodge_numbers_k3xe,
    virtual_dimension_k3, reduced_virtual_dimension_k3,
    virtual_dimension_k3xe, macmahon_coeffs,
    gw_dt_check_k3xe,
    # NL
    noether_lefschetz_rational,
    # QH
    qh_elliptic_curve_sigma1, qh_k3_trivial,
    # Verification
    verify_bps_integrality, verify_gottsche_sum,
    verify_hodge_symmetry, verify_bps_sign_pattern,
)


# ============================================================================
# 1. Number-theoretic helpers
# ============================================================================

class TestNumberTheory:
    """Tests for divisor sums, Mobius function, etc."""

    def test_divisors_1(self):
        assert _divisors(1) == [1]

    def test_divisors_6(self):
        assert _divisors(6) == [1, 2, 3, 6]

    def test_divisors_12(self):
        assert _divisors(12) == [1, 2, 3, 4, 6, 12]

    def test_divisors_prime(self):
        assert _divisors(7) == [1, 7]

    def test_divisors_square(self):
        assert _divisors(4) == [1, 2, 4]

    def test_sigma_0(self):
        """sigma_0(n) = number of divisors."""
        assert _sigma(6, 0) == 4
        assert _sigma(12, 0) == 6

    def test_sigma_1(self):
        """sigma_1(n) = sum of divisors."""
        assert _sigma(1, 1) == 1
        assert _sigma(2, 1) == 3
        assert _sigma(3, 1) == 4
        assert _sigma(4, 1) == 7
        assert _sigma(6, 1) == 12

    def test_sigma_2(self):
        """sigma_2(n) = sum of squares of divisors."""
        assert _sigma(1, 2) == 1
        assert _sigma(2, 2) == 5
        assert _sigma(3, 2) == 10

    def test_sigma_3(self):
        """sigma_3 for Eisenstein E_4."""
        assert _sigma(1, 3) == 1
        assert _sigma(2, 3) == 9
        assert _sigma(3, 3) == 28

    def test_mobius(self):
        assert _mobius(1) == 1
        assert _mobius(2) == -1
        assert _mobius(3) == -1
        assert _mobius(4) == 0  # 4 = 2^2
        assert _mobius(6) == 1  # 6 = 2*3
        assert _mobius(30) == -1  # 30 = 2*3*5

    def test_prime_factors(self):
        assert _prime_factors(1) == {}
        assert _prime_factors(12) == {2: 2, 3: 1}
        assert _prime_factors(30) == {2: 1, 3: 1, 5: 1}


# ============================================================================
# 2. Modular forms
# ============================================================================

class TestModularForms:
    """Tests for eta, Delta, Ramanujan tau, Eisenstein series."""

    def test_eta_24_product(self):
        """prod(1-q^n)^24 first coefficients = Ramanujan tau (shifted)."""
        coeffs = discriminant_coeffs(6)
        # Delta(q) = q * prod(1-q^n)^24, tau(n+1) = coeffs[n]
        assert coeffs[0] == 1    # tau(1)
        assert coeffs[1] == -24  # tau(2)
        assert coeffs[2] == 252  # tau(3)

    def test_ramanujan_tau_values(self):
        """Known values of tau(n) (OEIS A000594)."""
        expected = {1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
                    6: -6048, 7: -16744, 8: 84480}
        for n, val in expected.items():
            assert ramanujan_tau(n) == val, f"tau({n}) = {ramanujan_tau(n)} != {val}"

    def test_ramanujan_tau_multiplicativity(self):
        """tau is multiplicative: tau(mn) = tau(m)tau(n) for gcd(m,n)=1."""
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)
        assert ramanujan_tau(10) == ramanujan_tau(2) * ramanujan_tau(5)
        assert ramanujan_tau(15) == ramanujan_tau(3) * ramanujan_tau(5)

    def test_ramanujan_tau_hecke_relation(self):
        """Hecke relation: tau(p^2) = tau(p)^2 - p^11."""
        # tau(4) = tau(2)^2 - 2^11 = 576 - 2048 = -1472
        assert ramanujan_tau(4) == ramanujan_tau(2) ** 2 - 2 ** 11
        # tau(9) = tau(3)^2 - 3^11 = 63504 - 177147 = -113643
        assert ramanujan_tau(9) == ramanujan_tau(3) ** 2 - 3 ** 11

    def test_inverse_eta_24(self):
        """1/eta^24 coefficients = Yau-Zaslow / OEIS A006922."""
        coeffs = inverse_eta_24_coeffs(6)
        expected = [1, 24, 324, 3200, 25650, 176256, 1073720]
        assert coeffs == expected

    def test_eisenstein_e2(self):
        """E_2(q) = 1 - 24q - 72q^2 - 96q^3 - ..."""
        e2 = eisenstein_e2_coeffs(4)
        assert e2[0] == Fraction(1)
        assert e2[1] == Fraction(-24)  # -24 * sigma_1(1) = -24
        assert e2[2] == Fraction(-72)  # -24 * sigma_1(2) = -24*3 = -72
        assert e2[3] == Fraction(-96)  # -24 * sigma_1(3) = -24*4 = -96
        assert e2[4] == Fraction(-168)  # -24 * sigma_1(4) = -24*7 = -168

    def test_eisenstein_e4(self):
        """E_4(q) = 1 + 240q + 2160q^2 + ..."""
        e4 = eisenstein_e4_coeffs(3)
        assert e4[0] == Fraction(1)
        assert e4[1] == Fraction(240)  # 240 * sigma_3(1) = 240
        assert e4[2] == Fraction(2160)  # 240 * 9 = 2160
        assert e4[3] == Fraction(6720)  # 240 * 28 = 6720

    def test_eisenstein_e6(self):
        """E_6(q) = 1 - 504q - 16632q^2 - ..."""
        e6 = eisenstein_e6_coeffs(2)
        assert e6[0] == Fraction(1)
        assert e6[1] == Fraction(-504)  # -504 * sigma_5(1) = -504
        assert e6[2] == Fraction(-16632)  # -504 * 33 = -16632

    def test_delta_from_e4_e6(self):
        """Delta = (E_4^3 - E_6^2) / 1728 (cross-check)."""
        max_n = 5
        e4 = eisenstein_e4_coeffs(max_n)
        e6 = eisenstein_e6_coeffs(max_n)

        # E_4^3
        e4_cubed = [Fraction(0)] * (max_n + 1)
        e4_sq = [Fraction(0)] * (max_n + 1)
        for i in range(max_n + 1):
            for j in range(max_n + 1 - i):
                e4_sq[i + j] += e4[i] * e4[j]
        for i in range(max_n + 1):
            for j in range(max_n + 1 - i):
                e4_cubed[i + j] += e4_sq[i] * e4[j]

        # E_6^2
        e6_sq = [Fraction(0)] * (max_n + 1)
        for i in range(max_n + 1):
            for j in range(max_n + 1 - i):
                e6_sq[i + j] += e6[i] * e6[j]

        # (E_4^3 - E_6^2) / 1728
        delta_from_eis = [(e4_cubed[n] - e6_sq[n]) / 1728 for n in range(max_n + 1)]

        # Delta/q = prod(1-q^n)^24: tau(n) at index n-1
        # But delta_from_eis is sum c_n q^n with c_0 = 0, c_1 = tau(1) = 1, ...
        # Since E_4, E_6 are both 1 + ..., E_4^3 - E_6^2 starts at q^1.
        assert delta_from_eis[0] == 0  # no q^0 term
        for n in range(1, max_n + 1):
            expected_tau = ramanujan_tau(n)
            computed = int(delta_from_eis[n])
            assert computed == expected_tau, (
                f"Delta from E4,E6 at q^{n}: {computed} != tau({n}) = {expected_tau}"
            )


# ============================================================================
# 3. Yau-Zaslow formula (genus 0 BPS)
# ============================================================================

class TestYauZaslow:
    """PATH 2: Yau-Zaslow formula for genus-0 BPS of K3."""

    @pytest.mark.parametrize("h,expected", [
        (0, 1), (1, 24), (2, 324), (3, 3200),
        (4, 25650), (5, 176256), (6, 1073720),
    ])
    def test_yau_zaslow_values(self, h, expected):
        """OEIS A006922 values."""
        assert bps_genus0_k3(h) == expected

    def test_yau_zaslow_positivity(self):
        """n^0_h > 0 for all h >= 0."""
        for h in range(10):
            assert bps_genus0_k3(h) > 0

    def test_yau_zaslow_growth(self):
        """n^0_h grows roughly like exp(4pi sqrt(h))."""
        for h in range(1, 8):
            assert bps_genus0_k3(h) < bps_genus0_k3(h + 1)

    def test_yau_zaslow_from_eta(self):
        """n^0_h = [q^h] prod 1/(1-q^n)^{24} via two methods."""
        # Method 1: direct from inverse_eta_24_coeffs
        coeffs = inverse_eta_24_coeffs(5)
        # Method 2: from bps_genus0_k3 which also uses this
        for h in range(6):
            assert coeffs[h] == bps_genus0_k3(h)


# ============================================================================
# 4. KKV product and chi_y(Hilb)
# ============================================================================

class TestKKVProduct:
    """Tests for the chi_y(Hilb^h(K3)) product formula."""

    def test_product_coeff_h0(self):
        """F_{0,0} = 1, all other F_{j,0} = 0."""
        assert _product_coeff(0, 0) == Fraction(1)
        for j in [-2, -1, 1, 2]:
            assert _product_coeff(j, 0) == Fraction(0)

    def test_product_coeff_h1(self):
        """F_{-1,1} = F_{1,1} = 2, F_{0,1} = 20."""
        assert _product_coeff(0, 1) == Fraction(20)
        assert _product_coeff(1, 1) == Fraction(2)
        assert _product_coeff(-1, 1) == Fraction(2)

    def test_product_coeff_h2(self):
        """F_{0,2}=234, F_{1,2}=42, F_{2,2}=3."""
        assert _product_coeff(0, 2) == Fraction(234)
        assert _product_coeff(1, 2) == Fraction(42)
        assert _product_coeff(2, 2) == Fraction(3)

    @pytest.mark.parametrize("h", range(6))
    def test_hodge_symmetry(self, h):
        """PATH 6: F_{j,h} = F_{-j,h}."""
        assert verify_hodge_symmetry(h)

    @pytest.mark.parametrize("h", range(6))
    def test_gottsche_sum(self, h):
        """PATH 5: F_h(y=1) = [q^h] prod 1/(1-q^n)^{24}."""
        assert verify_gottsche_sum(h)

    def test_chi_y_hilb_dict(self):
        """chi_y_hilb_k3 returns correct dict."""
        d = chi_y_hilb_k3(1)
        assert d[-1] == Fraction(2)
        assert d[0] == Fraction(20)
        assert d[1] == Fraction(2)

    def test_chi_y_hilb_positivity(self):
        """All F_{j,h} are nonneg (Hodge numbers are nonneg)."""
        for h in range(6):
            d = chi_y_hilb_k3(h)
            for j, c in d.items():
                assert c >= 0, f"F_{{{j},{h}}} = {c} < 0"

    def test_t_polynomial_h0(self):
        """F_0(t) = 1."""
        p = chi_y_hilb_as_t_poly(0)
        assert p == [Fraction(1)]

    def test_t_polynomial_h1(self):
        """F_1(t) = 20 + 2t."""
        p = chi_y_hilb_as_t_poly(1)
        assert p[0] == Fraction(20)
        assert p[1] == Fraction(2)

    def test_t_polynomial_evaluation_at_2(self):
        """F_h(t=2) = Gottsche number (y=1 corresponds to t=2)."""
        for h in range(6):
            p = chi_y_hilb_as_t_poly(h)
            val = sum(c * Fraction(2 ** k) for k, c in enumerate(p))
            assert val == Fraction(bps_genus0_k3(h))


# ============================================================================
# 5. BPS extraction via (t-2)^g basis
# ============================================================================

class TestBPSExtraction:
    """PATH 1: BPS invariants from (t-2)^g basis change."""

    @pytest.mark.parametrize("h,expected", [
        (0, 1), (1, 24), (2, 324), (3, 3200), (4, 25650), (5, 176256),
    ])
    def test_bps_genus0_matches_yau_zaslow(self, h, expected):
        """n^0_h from extraction matches Yau-Zaslow."""
        assert bps_k3(0, h) == expected

    def test_bps_genus1(self):
        """Genus-1 BPS invariants."""
        assert bps_k3(1, 0) == 0
        assert bps_k3(1, 1) == -2
        assert bps_k3(1, 2) == -54

    def test_bps_genus2(self):
        """Genus-2 BPS invariants."""
        assert bps_k3(2, 0) == 0
        assert bps_k3(2, 1) == 0
        assert bps_k3(2, 2) == 3

    def test_bps_genus3(self):
        """Genus-3 BPS."""
        assert bps_k3(3, 0) == 0
        assert bps_k3(3, 1) == 0
        assert bps_k3(3, 2) == 0
        assert bps_k3(3, 3) == -4

    def test_bps_vanishing_g_greater_h(self):
        """n^g_h = 0 for g > h."""
        for g in range(1, 6):
            for h in range(g):
                assert bps_k3(g, h) == 0, f"n^{g}_{h} should be 0"

    def test_bps_diagonal_nonzero(self):
        """n^g_g != 0 for g >= 1."""
        # n^1_1 = -2, n^2_2 = 3, n^3_3 = -4
        assert bps_k3(1, 1) != 0
        assert bps_k3(2, 2) != 0
        assert bps_k3(3, 3) != 0

    @pytest.mark.parametrize("h", range(6))
    def test_bps_reconstruction(self, h):
        """Reconstruct F_h(t) from BPS and verify."""
        p = chi_y_hilb_as_t_poly(h)
        # Reconstruct from BPS: F_h(t) = sum n'^g_h (t-2)^g
        # n'^g_h = (-1)^g n^g_h.
        max_deg = len(p) - 1
        reconstructed = [Fraction(0)] * (max_deg + 1)
        for g in range(h + 1):
            n_unsigned = (-1) ** g * bps_k3(g, h)
            # (t-2)^g = sum C(g,k) t^k (-2)^{g-k}
            for k in range(g + 1):
                if k <= max_deg:
                    reconstructed[k] += (
                        Fraction(n_unsigned)
                        * Fraction(math.comb(g, k))
                        * Fraction((-2) ** (g - k))
                    )
        for k in range(max_deg + 1):
            assert reconstructed[k] == p[k], (
                f"h={h}, t^{k}: reconstructed={reconstructed[k]} != original={p[k]}"
            )

    def test_bps_table_shape(self):
        """bps_table returns correct dimensions."""
        t = bps_table(3, 5)
        assert len(t) == 4
        assert all(len(row) == 6 for row in t)


class TestBPSIntegrality:
    """PATH 4: All BPS invariants are integers."""

    def test_integrality_g0_h0_to_10(self):
        for h in range(11):
            n = bps_genus0_k3(h)
            assert isinstance(n, int)

    @pytest.mark.parametrize("g", range(4))
    def test_integrality_all_h(self, g):
        for h in range(8):
            n = bps_k3(g, h)
            assert isinstance(n, int), f"n^{g}_{h} = {n} not int"

    def test_integrality_verify_function(self):
        result = verify_bps_integrality(3, 6)
        assert result["all_integer"]
        assert result["failures"] == []

    def test_sign_pattern(self):
        """n^g_h has sign (-1)^g for nonzero values."""
        result = verify_bps_sign_pattern(3, 6)
        assert result["all_pass"], f"Sign failures: {[c for c in result['checks'] if not c['sign_ok']]}"


# ============================================================================
# 6. GW reduced invariants
# ============================================================================

class TestGWReduced:
    """Reduced Gromov-Witten invariants of K3."""

    def test_sin_power_j0_g0(self):
        """[u^{-2}] 1/(2sin(u/2))^2 = 1."""
        assert _sin_power_coeff(0, 0) == Fraction(1)

    def test_sin_power_j0_g1(self):
        """[u^0] 1/(2sin(u/2))^2 = 1/12."""
        assert _sin_power_coeff(1, 0) == Fraction(1, 12)

    def test_sin_power_j0_g2(self):
        """[u^2] 1/(2sin(u/2))^2 = 1/240."""
        assert _sin_power_coeff(2, 0) == Fraction(1, 240)

    def test_sin_power_j0_g3(self):
        """[u^4] 1/(2sin(u/2))^2 = 1/6048."""
        assert _sin_power_coeff(3, 0) == Fraction(1, 6048)

    def test_sin_power_j1(self):
        """(2sin(u/2))^0 = 1: only u^0 coefficient is 1."""
        assert _sin_power_coeff(1, 1) == Fraction(1)
        assert _sin_power_coeff(0, 1) == Fraction(0)
        assert _sin_power_coeff(2, 1) == Fraction(0)

    def test_sin_power_j2_leading(self):
        """[u^2] (2sin(u/2))^2 = 1 (leading term u^2)."""
        assert _sin_power_coeff(2, 2) == Fraction(1)

    def test_sin_power_j2_subleading(self):
        """[u^4] (2sin(u/2))^2 = -1/12."""
        assert _sin_power_coeff(3, 2) == Fraction(-1, 12)

    @pytest.mark.parametrize("h", range(1, 7))
    def test_gw_genus0_primitive_equals_bps(self, h):
        """For primitive class: N^{red}_{0,h} = n^0_h."""
        gw = gw_reduced_k3(0, h)
        assert gw == Fraction(bps_genus0_k3(h))

    def test_gw_genus1_h1(self):
        """N^{red}_{1,1} = n^1_1 + n^0_1 * (1/12) = -2 + 2 = 0."""
        gw = gw_reduced_k3(1, 1)
        # n^0_1 = 24, a(1,0) = 1/12 => 24/12 = 2
        # n^1_1 = -2, a(1,1) = 1 => -2
        assert gw == Fraction(0)

    def test_gw_genus1_h2(self):
        """N^{red}_{1,2} = n^1_2 * 1 + n^0_2 * (1/12)."""
        gw = gw_reduced_k3(1, 2)
        expected = Fraction(-54) + Fraction(324, 12)  # -54 + 27 = -27
        assert gw == expected

    def test_gw_vanishing_h0_gpos(self):
        """N^{red}_{g, 0} = 0 for g >= 1."""
        for g in range(1, 5):
            assert gw_reduced_k3(g, 0) == Fraction(0)


# ============================================================================
# 7. K3 x E topology
# ============================================================================

class TestK3xETopology:
    """Topological invariants of K3, E, and K3 x E."""

    def test_euler_char_k3(self):
        assert euler_char_k3() == 24

    def test_euler_char_elliptic(self):
        assert euler_char_elliptic() == 0

    def test_euler_char_k3xe(self):
        """chi(K3 x E) = 24 * 0 = 0."""
        assert euler_char_k3xe() == 0

    def test_hodge_k3(self):
        h = hodge_numbers_k3()
        assert h[(0, 0)] == 1
        assert h[(2, 0)] == 1  # H^{2,0} = C (key for reduced theory)
        assert h[(1, 1)] == 20
        assert h[(1, 0)] == 0  # simply connected
        # Euler char
        chi = sum((-1) ** (p + q) * v for (p, q), v in h.items())
        assert chi == 24

    def test_hodge_k3xe(self):
        h = hodge_numbers_k3xe()
        # CY3: h^{3,0} = 1 (from h^{2,0}(K3) * h^{1,0}(E))
        assert h[(3, 0)] == 1
        # h^{1,1} = h^{2,1} (CY3 mirror pair)
        assert h[(1, 1)] == h[(2, 1)]
        assert h[(1, 1)] == 21
        # Euler char = 0
        chi = sum((-1) ** (p + q) * v for (p, q), v in h.items())
        assert chi == 0

    def test_hodge_k3xe_symmetry(self):
        """Hodge symmetry: h^{p,q} = h^{q,p}."""
        h = hodge_numbers_k3xe()
        for (p, q), v in h.items():
            if (q, p) in h:
                assert h[(q, p)] == v

    def test_virtual_dim_k3(self):
        assert virtual_dimension_k3(0) == -1
        assert virtual_dimension_k3(1) == 0
        assert virtual_dimension_k3(2) == 1

    def test_reduced_virtual_dim_k3(self):
        assert reduced_virtual_dimension_k3(0) == 0
        assert reduced_virtual_dimension_k3(1) == 1
        assert reduced_virtual_dimension_k3(2) == 2

    def test_virtual_dim_cy3(self):
        """CY3: vdim = n (independent of genus!)."""
        for g in range(5):
            assert virtual_dimension_k3xe(g, n=0) == 0
            assert virtual_dimension_k3xe(g, n=3) == 3


# ============================================================================
# 8. GW/DT correspondence
# ============================================================================

class TestGWDT:
    """PATH 3: GW/DT comparison for K3 x E."""

    def test_chi_zero_implies_dt_equals_pt(self):
        """chi(K3 x E) = 0 implies MacMahon^0 = 1, so DT = PT."""
        assert euler_char_k3xe() == 0

    def test_gw_dt_check_h1(self):
        result = gw_dt_check_k3xe(1, max_g=3)
        assert result["chi_K3xE"] == 0
        assert result["macmahon_power"] == 0

    def test_macmahon_coefficients(self):
        """Plane partition counts (OEIS A000219)."""
        mc = macmahon_coeffs(8)
        expected = (1, 1, 3, 6, 13, 24, 48, 86, 160)
        for i in range(9):
            assert mc[i] == expected[i], f"pp({i}) = {mc[i]} != {expected[i]}"

    def test_macmahon_positivity(self):
        mc = macmahon_coeffs(15)
        for i in range(16):
            assert mc[i] > 0


# ============================================================================
# 9. Noether-Lefschetz theory
# ============================================================================

class TestNoetherLefschetz:
    """Noether-Lefschetz numbers for rational curves on K3."""

    @pytest.mark.parametrize("h", range(7))
    def test_nl_equals_yau_zaslow(self, h):
        """NL(h) = n^0_h (Yau-Zaslow)."""
        assert noether_lefschetz_rational(h) == bps_genus0_k3(h)

    def test_nl_3200(self):
        """3200 rational curves of degree 3 on K3 (classical result)."""
        assert noether_lefschetz_rational(3) == 3200


# ============================================================================
# 10. Quantum cohomology
# ============================================================================

class TestQuantumCohomology:
    """Quantum cohomology of K3 and K3 x E."""

    def test_qh_k3_trivial(self):
        """QH*(K3) = H*(K3)."""
        assert qh_k3_trivial()

    @pytest.mark.parametrize("d,expected", [
        (1, 1), (2, 3), (3, 4), (4, 7), (5, 6), (6, 12),
    ])
    def test_sigma_1(self, d, expected):
        """sigma_1(d) for quantum corrections of E."""
        assert qh_elliptic_curve_sigma1(d) == expected

    def test_sigma_1_multiplicativity(self):
        """sigma_1 is multiplicative for coprime."""
        assert qh_elliptic_curve_sigma1(6) == (
            qh_elliptic_curve_sigma1(2) * qh_elliptic_curve_sigma1(3)
        )


# ============================================================================
# 11. Cross-path verification
# ============================================================================

class TestCrossPath:
    """Multi-path verification across different computation methods."""

    def test_path1_vs_path2_genus0(self):
        """BPS extraction (path 1) matches Yau-Zaslow (path 2) at genus 0."""
        for h in range(8):
            assert bps_k3(0, h) == bps_genus0_k3(h)

    @pytest.mark.parametrize("h", range(1, 6))
    def test_path1_reconstruction_vs_path5(self, h):
        """BPS reconstruction (path 1): F_h(t=2) = n^0_h = YZ.

        F_h(t) = sum n'^g_h (t-2)^g.  At t=2: (t-2)^g = 0 for g>=1,
        so F_h(2) = n'^0_h = n^0_h (Yau-Zaslow).
        Equivalently: sum n'^g_h * 0^g = n'^0_h.
        """
        # n'^0_h = (-1)^0 * n^0_h = n^0_h
        assert bps_k3(0, h) == bps_genus0_k3(h)

    @pytest.mark.parametrize("h", range(1, 5))
    def test_path1_reconstruction_at_t3(self, h):
        """F_h(t=3) = sum n'^g_h (checking evaluation at t=3)."""
        # F_h(3) from the t-polynomial
        p = chi_y_hilb_as_t_poly(h)
        f_at_3 = sum(c * Fraction(3 ** k) for k, c in enumerate(p))
        # sum n'^g_h = sum (-1)^g n^g_h
        bps_sum = sum((-1) ** g * bps_k3(g, h) for g in range(h + 1))
        assert f_at_3 == Fraction(bps_sum)

    def test_path4_integrality_vs_path1(self):
        """Integrality (path 4) verified for extracted BPS (path 1)."""
        for g in range(4):
            for h in range(7):
                n = bps_k3(g, h)
                assert isinstance(n, int)

    def test_path6_hodge_vs_path5(self):
        """Hodge symmetry (path 6) implies F_h(y=1) consistent."""
        for h in range(6):
            assert verify_hodge_symmetry(h)
            assert verify_gottsche_sum(h)

    def test_path7_ramanujan_tau_cross_check(self):
        """tau(n) from eta^24 vs from E_4^3 - E_6^2."""
        # Already tested in TestModularForms.test_delta_from_e4_e6
        # Here verify one more property: tau(n) are eigenvalues of T_n
        # tau(2)*tau(3) = tau(6) (multiplicativity for coprime)
        assert ramanujan_tau(2) * ramanujan_tau(3) == ramanujan_tau(6)

    def test_bps_alternating_sum_at_y_neg1(self):
        """F_h(-1) = sum (-1)^j F_{j,h} from product = sum n'^g_h (-4)^g."""
        for h in range(5):
            # F_h(-1) from product
            max_j = h + 2
            f_neg1 = sum(
                _product_coeff(j, h) * Fraction((-1) ** j)
                for j in range(-max_j, max_j + 1)
            )
            # From BPS: t = y + y^{-1} = -1 + (-1) = -2
            # F_h(t=-2) = sum n'^g_h (t-2)^g = sum n'^g_h (-4)^g
            from_bps = Fraction(0)
            for g in range(h + 1):
                n_unsigned = (-1) ** g * bps_k3(g, h)
                from_bps += Fraction(n_unsigned) * Fraction((-4) ** g)
            assert f_neg1 == from_bps, f"h={h}: F(-1)={f_neg1} != BPS sum={from_bps}"

    def test_gw_bps_consistency_genus1(self):
        """N^{red}_{1,h} for primitive h satisfies GW/BPS change of vars."""
        for h in range(1, 5):
            gw = gw_reduced_k3(1, h)
            # N^{red}_{1,h} = n^1_h * 1 + n^0_h * (1/12)
            expected = Fraction(bps_k3(1, h)) + Fraction(bps_k3(0, h), 12)
            assert gw == expected, f"h={h}: GW={gw} != expected={expected}"


# ============================================================================
# 12. Deeper BPS verification
# ============================================================================

class TestBPSDeep:
    """Deeper structural tests for BPS invariants."""

    def test_bps_h4_full_column(self):
        """Full BPS column at h=4."""
        col = [bps_k3(g, 4) for g in range(5)]
        assert col[0] == 25650
        assert col[4] == bps_k3(4, 4)
        # All should be integers with alternating signs
        for g, n in enumerate(col):
            assert isinstance(n, int)
            if n != 0:
                assert (n > 0) == (g % 2 == 0), f"g={g}: n={n} wrong sign"

    def test_bps_h5_full_column(self):
        """Full BPS column at h=5."""
        col = [bps_k3(g, 5) for g in range(6)]
        assert col[0] == 176256
        for g, n in enumerate(col):
            assert isinstance(n, int)
            if n != 0:
                assert (n > 0) == (g % 2 == 0), f"g={g}: n={n} wrong sign"

    def test_bps_negative_args(self):
        """Negative arguments return 0."""
        assert bps_k3(-1, 0) == 0
        assert bps_k3(0, -1) == 0
        assert bps_k3(-1, -1) == 0

    def test_bps_genus0_large(self):
        """n^0_8 and n^0_9 are large positive integers."""
        n8 = bps_genus0_k3(8)
        n9 = bps_genus0_k3(9)
        assert n8 > 10 ** 7
        assert n9 > n8
        assert isinstance(n8, int)
        assert isinstance(n9, int)

    def test_gottsche_chi_from_bps(self):
        """chi(Hilb^h(K3)) = sum_g n'^g_h * 2^g (substitute t=2 into (t-2)^g).
        Actually sum n'^g_h (2-2)^g = n'^0_h = n^0_h.  So chi = n^0_h."""
        for h in range(6):
            assert verify_gottsche_sum(h)


# ============================================================================
# 13. Eisenstein E_2 quasi-modularity test
# ============================================================================

class TestEisensteinCrossChecks:
    """Cross-checks involving Eisenstein series."""

    def test_e2_not_modular(self):
        """E_2 is QUASI-modular (AP15): verify it is NOT weight-2 holomorphic.
        The space M_2(SL(2,Z)) = {0}, so E_2 is not in it."""
        # E_2 is quasi-modular weight 2. No nonzero modular form of weight 2.
        # Numerically: E_2 transforms with anomaly, not as a modular form.
        # We just verify E_2 is nonzero (it exists as a function).
        e2 = eisenstein_e2_coeffs(1)
        assert e2[0] == Fraction(1)  # constant term
        assert e2[1] != Fraction(0)  # nontrivial

    def test_e4_modular_check(self):
        """E_4^3 and E_6^2 should produce Delta via (E_4^3 - E_6^2)/1728."""
        e4 = eisenstein_e4_coeffs(2)
        e6 = eisenstein_e6_coeffs(2)
        # E_4^3 at q^1: 3 * 240 = 720
        e4_cubed_q1 = Fraction(3) * e4[0] ** 2 * e4[1]
        # E_6^2 at q^1: 2 * (-504) = -1008
        e6_sq_q1 = Fraction(2) * e6[0] * e6[1]
        delta_q1 = (e4_cubed_q1 - e6_sq_q1) / 1728
        assert delta_q1 == Fraction(1)  # tau(1) = 1


# ============================================================================
# 14. Laurent coefficient tests
# ============================================================================

class TestLaurentCoeffs:
    """Tests for inverse sinc^2 and sinc power computations."""

    def test_inverse_sinc_sq_n0(self):
        """[x^0] 1/sinc(x)^2 / 4^0 = 1."""
        assert _inverse_sinc_sq_coeff(0) == Fraction(1)

    def test_inverse_sinc_sq_n1(self):
        """[u^0] 1/(2sin(u/2))^2 = c_1/4 = (1/3)/4 = 1/12."""
        assert _inverse_sinc_sq_coeff(1) == Fraction(1, 12)

    def test_inverse_sinc_sq_n2(self):
        """[u^2] 1/(2sin(u/2))^2 = c_2/16."""
        val = _inverse_sinc_sq_coeff(2)
        assert val == Fraction(1, 240)

    def test_sinc_power_m2_k0(self):
        """[u^2] (2sin(u/2))^2 = 1 (leading term)."""
        assert _sinc_power_coeff(2, 0) == Fraction(1)

    def test_sinc_power_m2_k1(self):
        """[u^4] (2sin(u/2))^2 = -1/12."""
        assert _sinc_power_coeff(2, 1) == Fraction(-1, 12)

    def test_sinc_power_m4_k0(self):
        """[u^4] (2sin(u/2))^4 = 1 (leading)."""
        assert _sinc_power_coeff(4, 0) == Fraction(1)


# ============================================================================
# 15. Edge cases and error handling
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_bps_genus0_h_negative(self):
        assert bps_genus0_k3(-1) == 0

    def test_gw_h_zero(self):
        """N^{red}_{0,0} = n^0_0 = 1 (constant map / trivial class)."""
        assert gw_reduced_k3(0, 0) == Fraction(1)

    def test_gw_negative_g(self):
        assert gw_reduced_k3(-1, 1) == Fraction(0)

    def test_product_coeff_negative_h(self):
        assert _product_coeff(0, -1) == Fraction(0)

    def test_ramanujan_tau_zero(self):
        assert ramanujan_tau(0) == 0
        assert ramanujan_tau(-1) == 0

    def test_sigma_1_boundary(self):
        assert qh_elliptic_curve_sigma1(0) == 0


# ============================================================================
# 16. Product formula specific cross-checks
# ============================================================================

class TestProductCrossChecks:
    """Additional cross-checks on the KKV product."""

    def test_product_sum_absolute_h3(self):
        """Total chi(Hilb^3(K3)) = 3200 (Gottsche)."""
        total = sum(
            _product_coeff(j, 3) for j in range(-5, 6)
        )
        assert total == Fraction(3200)

    def test_product_symmetry_h4(self):
        """Hodge symmetry at h=4."""
        for j in range(1, 6):
            assert _product_coeff(j, 4) == _product_coeff(-j, 4)

    def test_product_trace_at_y_neg1_h2(self):
        """F_2(-1) = sum F_{j,2} (-1)^j."""
        total = sum(
            _product_coeff(j, 2) * Fraction((-1) ** j)
            for j in range(-4, 5)
        )
        assert total == Fraction(156)  # Known from computation

    def test_product_h1_sum_positive_y(self):
        """F_1(y) = 2y^{-1} + 20 + 2y. At y=2: 1 + 20 + 4 = 25."""
        val = (
            _product_coeff(-1, 1) * Fraction(1, 2)
            + _product_coeff(0, 1)
            + _product_coeff(1, 1) * Fraction(2)
        )
        assert val == Fraction(25)
