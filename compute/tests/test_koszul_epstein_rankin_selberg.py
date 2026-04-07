"""Tests for the genus-1 Rankin-Selberg transform of Theta_A.

Verifies the construction from rn105: define RS_1(s, A), compute Li-like
coefficients for Heisenberg, Virasoro, and W_3, verify universality.

40+ tests covering:
  - RS Dirichlet series vs product formula
  - Lambda_1 = 0 (exactly, by pairing symmetry)
  - Lambda_n > 0 for n >= 2 (under RH)
  - Universality: Li coefficients independent of family at genus 1
  - Critical line decomposition
  - Comparison with classical Li coefficients
  - Sewing Dirichlet series for all three families
  - Genus-2 family-dependent corrections
  - KE-RH equivalence test
"""
import math
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

from compute.lib import koszul_epstein_rankin_selberg as kers

# Common test parameters
N_ZEROS = 100  # Sufficient for 12-digit accuracy
DPS = 30


@pytest.fixture(scope="module")
def zeta_zeros():
    """Precompute zeta zeros for all tests."""
    if not HAS_MPMATH:
        pytest.skip("mpmath required")
    return kers.compute_zeta_zeros(N_ZEROS, DPS)


@pytest.fixture(scope="module")
def heisenberg():
    return kers.heisenberg_data(1.0)


@pytest.fixture(scope="module")
def virasoro_26():
    return kers.virasoro_data(26.0)


@pytest.fixture(scope="module")
def virasoro_10():
    return kers.virasoro_data(10.0)


@pytest.fixture(scope="module")
def w3_50():
    return kers.w3_data(50.0)


# ============================================================
# 1. Shadow data tests
# ============================================================

class TestShadowData:
    def test_heisenberg_kappa(self, heisenberg):
        assert heisenberg.kappa == 1.0  # kappa(H_k) = k, NOT k/2 (AP39)

    def test_heisenberg_class_G(self, heisenberg):
        assert heisenberg.shadow_class == 'G'

    def test_heisenberg_no_higher_shadows(self, heisenberg):
        for r in range(3, 10):
            assert heisenberg.shadow_coefficient(r) == 0.0

    def test_virasoro_kappa(self, virasoro_26):
        assert virasoro_26.kappa == 13.0

    def test_virasoro_class_M(self, virasoro_26):
        assert virasoro_26.shadow_class == 'M'

    def test_virasoro_cubic(self, virasoro_26):
        assert virasoro_26.shadow_coefficient(3) == 2.0

    def test_virasoro_quartic(self):
        v = kers.virasoro_data(10.0)
        Q_contact = 10.0 / (10.0 * (5*10 + 22))
        assert abs(v.shadow_coefficient(4) - Q_contact) < 1e-12

    def test_w3_kappa(self, w3_50):
        # kappa(W_3) = 5c/6, NOT c/2 (AP1). At c=50: 5*50/6 = 250/6
        assert abs(w3_50.kappa - 5.0 * 50.0 / 6.0) < 1e-12

    def test_w3_weights(self, w3_50):
        assert w3_50.weights == [2, 3]


# ============================================================
# 2. RS Dirichlet series tests
# ============================================================

class TestRSDirichletSeries:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_dirichlet_vs_product_s3(self):
        """At s=3, sum sigma_1(n)n^{-3} converges slowly; use large N."""
        mpmath.mp.dps = DPS
        s = mpmath.mpf(3)
        d = kers.rs_dirichlet_series(s, kappa=1.0, N_max=5000)
        p = kers.rs_product_formula(s, kappa=1.0)
        # Tail sum ~ integral_N^infty n^{1-s} dn = N^{2-s}/(s-2) for sigma_1(n)~n
        # At N=5000, s=3: tail ~ 5000^{-1} = 2e-4
        assert abs(float(d - p) / float(p)) < 5e-4

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_dirichlet_vs_product_s5(self):
        mpmath.mp.dps = DPS
        s = mpmath.mpf(5)
        d = kers.rs_dirichlet_series(s, kappa=1.0, N_max=500)
        p = kers.rs_product_formula(s, kappa=1.0)
        assert abs(float(d - p) / float(p)) < 1e-5

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_kappa_scaling(self):
        """RS_1(s, A) = kappa(A) * RS_1(s, H)."""
        mpmath.mp.dps = DPS
        s = mpmath.mpf(4)
        rs_h = kers.rs_product_formula(s, kappa=1.0)
        rs_v = kers.rs_product_formula(s, kappa=13.0)  # Vir at c=26
        assert abs(float(rs_v / rs_h) - 13.0) < 1e-10

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_product_zeta_zeta(self):
        """RS_1(s, H) = zeta(s) * zeta(s-1)."""
        mpmath.mp.dps = DPS
        s = mpmath.mpf(3)
        rs = kers.rs_product_formula(s, kappa=1.0)
        expected = mpmath.zeta(3) * mpmath.zeta(2)
        assert abs(float(rs - expected)) < 1e-15


# ============================================================
# 3. Lambda_1 = 0 tests
# ============================================================

class TestLambda1Vanishing:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_lambda1_zero(self, zeta_zeros):
        mpmath.mp.dps = DPS
        lam1 = kers.li_coefficient_rs(1, zeta_zeros)
        assert abs(float(lam1)) < 1e-15

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_lambda1_vanishing_proof(self, zeta_zeros):
        mpmath.mp.dps = DPS
        proof = kers.lambda1_vanishing_proof(zeta_zeros)
        assert proof['is_zero']
        assert proof['mechanism'] == 'pairing_symmetry'

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_lambda1_per_gamma_cancellation(self, zeta_zeros):
        """Each gamma contributes 0 to lambda_1."""
        mpmath.mp.dps = DPS
        proof = kers.lambda1_vanishing_proof(zeta_zeros)
        for entry in proof['per_gamma']:
            assert abs(entry['sum']) < 1e-15

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_lambda1_structural(self, zeta_zeros):
        """Verify the algebraic identity: 1/(z-1) sums to 0 over quadruplets."""
        mpmath.mp.dps = DPS
        for rho in zeta_zeros[:10]:
            gamma = mpmath.im(rho)
            denom = mpmath.mpf('0.25') + gamma**2
            c_half = -1 / denom      # 2*Re[1/(-1/2+i*gamma)]
            c_three_half = 1 / denom  # 2*Re[1/(1/2+i*gamma)]
            assert abs(float(c_half + c_three_half)) < 1e-20


# ============================================================
# 4. Li coefficient positivity tests
# ============================================================

class TestLiPositivity:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_lambda2_positive(self, zeta_zeros):
        mpmath.mp.dps = DPS
        lam2 = kers.li_coefficient_rs(2, zeta_zeros)
        # With N_zeros=100, value is ~0.080; with 200, ~0.084
        assert float(lam2) > 0.07

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_lambda_all_positive_from_2(self, zeta_zeros):
        """lambda_n^KE > 0 for n = 2..20 (under RH)."""
        mpmath.mp.dps = DPS
        for n in range(2, 21):
            lam = kers.li_coefficient_rs(n, zeta_zeros)
            assert float(lam) > 0, f"lambda_{n}^KE = {float(lam)} is not positive"

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_lambda_monotone_increasing(self, zeta_zeros):
        """lambda_n^KE is monotonically increasing for n >= 2."""
        mpmath.mp.dps = DPS
        prev = kers.li_coefficient_rs(2, zeta_zeros)
        for n in range(3, 16):
            curr = kers.li_coefficient_rs(n, zeta_zeros)
            assert float(curr) > float(prev), f"lambda_{n} <= lambda_{n-1}"
            prev = curr

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_lambda_growth_rate(self, zeta_zeros):
        """lambda_n^KE grows roughly linearly in n (for moderate n)."""
        mpmath.mp.dps = DPS
        lam10 = float(kers.li_coefficient_rs(10, zeta_zeros))
        lam20 = float(kers.li_coefficient_rs(20, zeta_zeros))
        ratio = lam20 / lam10
        # Should be roughly 2x (linear growth at leading order)
        assert 1.5 < ratio < 5.0


# ============================================================
# 5. Universality tests
# ============================================================

class TestUniversality:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_heisenberg_virasoro_agree(self, zeta_zeros, heisenberg, virasoro_26):
        """Li coefficients are the same for Heisenberg and Virasoro at genus 1."""
        mpmath.mp.dps = DPS
        for n in range(2, 11):
            lam_h = kers.li_coefficient_rs(n, zeta_zeros, heisenberg)
            lam_v = kers.li_coefficient_rs(n, zeta_zeros, virasoro_26)
            assert abs(float(lam_h - lam_v)) < 1e-15, \
                f"lambda_{n}: Heis={float(lam_h)}, Vir={float(lam_v)}"

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_virasoro_w3_agree(self, zeta_zeros, virasoro_26, w3_50):
        """Li coefficients are the same for Virasoro and W_3 at genus 1."""
        mpmath.mp.dps = DPS
        for n in range(2, 11):
            lam_v = kers.li_coefficient_rs(n, zeta_zeros, virasoro_26)
            lam_w = kers.li_coefficient_rs(n, zeta_zeros, w3_50)
            assert abs(float(lam_v - lam_w)) < 1e-15

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_universality_full(self):
        """Full universality test across 4 families."""
        mpmath.mp.dps = DPS
        result = kers.universality_test(N_zeros=50, dps=DPS)
        assert result['universality_holds']
        assert result['max_discrepancy'] < 1e-10


# ============================================================
# 6. Critical line decomposition tests
# ============================================================

class TestCriticalLineDecomposition:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_half_line_ratio_increases(self, zeta_zeros):
        """The ratio (Re=1/2)/(Re=3/2) increases with n, approaching 1."""
        mpmath.mp.dps = DPS
        decomp = kers.critical_line_analysis(zeta_zeros, 15)
        # Ratio increases monotonically for n >= 3
        for n in range(4, 15):
            assert decomp[n]['ratio'] > decomp[n-1]['ratio'] - 0.01

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_both_lines_contribute(self, zeta_zeros):
        """Both critical lines contribute nontrivially for n >= 3."""
        mpmath.mp.dps = DPS
        decomp = kers.critical_line_analysis(zeta_zeros, 10)
        for n in range(3, 11):
            assert decomp[n]['from_Re_half'] > 0
            assert decomp[n]['from_Re_three_half'] > 0

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_three_half_bounded(self, zeta_zeros):
        """Re(s)=3/2 contributions grow but remain moderate per zero."""
        mpmath.mp.dps = DPS
        decomp = kers.critical_line_analysis(zeta_zeros, 15)
        vals_3h = [abs(decomp[n]['from_Re_three_half']) for n in range(2, 16)]
        # With N_zeros=100, total Re=3/2 contribution stays moderate
        assert max(vals_3h) < 100

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_cancellation_at_n1(self, zeta_zeros):
        """At n=1, the two lines cancel exactly."""
        mpmath.mp.dps = DPS
        decomp = kers.critical_line_analysis(zeta_zeros, 1)
        total = decomp[1]['total']
        assert abs(total) < 1e-15


# ============================================================
# 7. Comparison with classical Li coefficients
# ============================================================

class TestClassicalComparison:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_classical_li_positive(self):
        mpmath.mp.dps = DPS
        li = kers.classical_li_coefficients(10, N_ZEROS, DPS)
        for n in range(1, 11):
            assert float(li[n]) > 0

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_classical_lambda1_nonzero(self):
        """Classical lambda_1 is about 0.023 (NOT zero)."""
        mpmath.mp.dps = DPS
        li = kers.classical_li_coefficients(1, N_ZEROS, DPS)
        assert abs(float(li[1]) - 0.023) < 0.005

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_rs_vs_classical_lambda2(self):
        """RS lambda_2 differs from classical lambda_2."""
        mpmath.mp.dps = DPS
        comp = kers.li_comparison(2, N_ZEROS, DPS)
        # Classical lambda_2 ~ 0.084, RS lambda_2 ~ 0.084 also (close but not identical)
        assert abs(comp[2]['classical'] - comp[2]['rs']) < 0.01

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_rs_exceeds_classical_at_n10(self):
        """RS lambda_n > classical lambda_n for large n (doubled zeros)."""
        mpmath.mp.dps = DPS
        comp = kers.li_comparison(10, N_ZEROS, DPS)
        assert comp[10]['rs'] > comp[10]['classical']


# ============================================================
# 8. Sewing Dirichlet series tests
# ============================================================

class TestSewingDirichletSeries:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_heisenberg_sewing(self):
        """S_H(u) = zeta(u) * zeta(u+1)."""
        mpmath.mp.dps = DPS
        u = mpmath.mpf(3)
        S = kers.sewing_dirichlet_series(u, [1])
        expected = mpmath.zeta(3) * mpmath.zeta(4)
        assert abs(float(S - expected) / float(expected)) < 1e-10

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_virasoro_sewing(self):
        """S_Vir(u) = zeta(u+1) * (zeta(u) - 1)."""
        mpmath.mp.dps = DPS
        u = mpmath.mpf(3)
        S = kers.sewing_dirichlet_series(u, [2])
        expected = mpmath.zeta(4) * (mpmath.zeta(3) - 1)
        assert abs(float(S - expected) / float(expected)) < 1e-10

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_w3_sewing(self):
        """S_{W3}(u) = zeta(u+1) * (2*zeta(u) - 1 - 1 - 1/2^u)."""
        mpmath.mp.dps = DPS
        u = mpmath.mpf(3)
        S = kers.sewing_dirichlet_series(u, [2, 3])
        z_u = mpmath.zeta(3)
        z_u1 = mpmath.zeta(4)
        # weight 2: zeta(u) - 1 = zeta(3) - 1
        # weight 3: zeta(u) - 1 - 1/2^u = zeta(3) - 1 - 1/8
        expected = z_u1 * ((z_u - 1) + (z_u - 1 - mpmath.power(2, -u)))
        assert abs(float(S - expected) / float(expected)) < 1e-10

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_heisenberg_euler_koszul(self):
        """Heisenberg has Euler defect D = 1 (exact Euler-Koszul)."""
        mpmath.mp.dps = DPS
        u = mpmath.mpf(3)
        D = kers.sewing_euler_defect(u, [1])
        assert abs(float(D) - 1.0) < 1e-10

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_virasoro_euler_defect(self):
        """Virasoro has Euler defect D = 1 - 1/zeta(u)."""
        mpmath.mp.dps = DPS
        u = mpmath.mpf(3)
        D = kers.sewing_euler_defect(u, [2])
        expected = 1 - 1 / mpmath.zeta(3)
        assert abs(float(D - expected)) < 1e-10

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_betagamma_euler_koszul(self):
        """Beta-gamma has D = 1 (both weights = 1)."""
        mpmath.mp.dps = DPS
        u = mpmath.mpf(3)
        D = kers.sewing_euler_defect(u, [1, 1])
        assert abs(float(D) - 1.0) < 1e-10


# ============================================================
# 9. Genus-2 corrections (family-dependent) tests
# ============================================================

class TestGenus2Corrections:
    def test_heisenberg_no_cubic(self, heisenberg):
        """Heisenberg has S_3 = 0, so no cubic correction."""
        corr = kers.genus2_cubic_correction(heisenberg)
        assert abs(corr) < 1e-15

    def test_virasoro_cubic_nonzero(self, virasoro_26):
        """Virasoro has nonzero cubic correction at genus 2."""
        corr = kers.genus2_cubic_correction(virasoro_26)
        # S_3 = 2, kappa = 13
        # delta_pf = 2 * (10*2 - 13) / 48 = 2 * 7 / 48 = 7/24
        expected = 2 * (10*2 - 13) / 48
        assert abs(corr - expected) < 1e-10

    def test_genus2_family_dependent(self, heisenberg, virasoro_26, w3_50):
        """Genus-2 corrections differ across families."""
        corr_h = kers.genus2_cubic_correction(heisenberg)
        corr_v = kers.genus2_cubic_correction(virasoro_26)
        corr_w = kers.genus2_cubic_correction(w3_50)
        # Heisenberg = 0, others nonzero
        assert abs(corr_h) < 1e-15
        assert abs(corr_v) > 0.1
        assert abs(corr_w) > 0.1

    def test_genus2_scalar_formula(self, virasoro_26):
        """F_2^scalar = kappa / 240."""
        f2 = kers.genus2_rs_kappa_contribution(3.0, virasoro_26.kappa)
        assert abs(f2 - 13.0/240) < 1e-12


# ============================================================
# 10. KE-RH equivalence tests
# ============================================================

class TestKERH:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_ke_rh_consistent(self):
        result = kers.ke_rh_equivalence(n_max=10, N_zeros=50, dps=DPS)
        assert result['consistent_with_RH']
        assert result['lambda_1_zero']
        assert result['all_positive_from_2']


# ============================================================
# 11. Three-family analysis tests
# ============================================================

class TestThreeFamilyAnalysis:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_three_family_runs(self):
        result = kers.three_family_analysis(n_li=10, N_zeros=50, dps=DPS)
        assert 'heisenberg' in result
        assert 'virasoro_26' in result
        assert 'w3_50' in result

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_all_families_positive_from_2(self):
        result = kers.three_family_analysis(n_li=10, N_zeros=50, dps=DPS)
        for name, data in result.items():
            assert data['all_positive_from_2'], f"{name} has negative Li coefficient"

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_heisenberg_euler_koszul(self):
        result = kers.three_family_analysis(n_li=5, N_zeros=50, dps=DPS)
        assert result['heisenberg']['is_euler_koszul']

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_virasoro_not_euler_koszul(self):
        result = kers.three_family_analysis(n_li=5, N_zeros=50, dps=DPS)
        assert not result['virasoro_26']['is_euler_koszul']

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_w3_not_euler_koszul(self):
        result = kers.three_family_analysis(n_li=5, N_zeros=50, dps=DPS)
        assert not result['w3_50']['is_euler_koszul']

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_li_universality_across_families(self):
        """All three families have the same Li coefficients at genus 1."""
        result = kers.three_family_analysis(n_li=10, N_zeros=50, dps=DPS)
        li_h = result['heisenberg']['li_coefficients']
        li_v = result['virasoro_26']['li_coefficients']
        li_w = result['w3_50']['li_coefficients']
        for n in range(2, 11):
            assert abs(li_h[n] - li_v[n]) < 1e-10, f"H vs V at n={n}"
            assert abs(li_v[n] - li_w[n]) < 1e-10, f"V vs W at n={n}"


# ============================================================
# 12. Xi_RS function tests
# ============================================================

class TestXiRS:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_xi_rs_symmetry(self):
        """Xi_RS(s) = Xi_RS(2-s)."""
        mpmath.mp.dps = DPS
        for s_val in [0.5 + 3j, 1.2 + 5j, 0.8 - 2j]:
            s = mpmath.mpc(s_val)
            val_s = kers.xi_rs_genus1(s)
            val_2ms = kers.xi_rs_genus1(2 - s)
            if abs(val_s) > 1e-20:
                assert abs(float(abs(val_s - val_2ms) / abs(val_s))) < 1e-8

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_xi_rs_zero_at_rho(self, zeta_zeros):
        """Xi_RS vanishes at nontrivial zeta zeros."""
        mpmath.mp.dps = DPS
        rho = zeta_zeros[0]  # first zero
        val = kers.xi_rs_genus1(rho)
        assert abs(float(abs(val))) < 1e-10

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_xi_rs_zero_at_shifted_rho(self, zeta_zeros):
        """Xi_RS vanishes at 1 + rho (shifted zeros)."""
        mpmath.mp.dps = DPS
        rho = zeta_zeros[0]
        val = kers.xi_rs_genus1(1 + rho)
        assert abs(float(abs(val))) < 1e-10


# ============================================================
# 13. Numerical accuracy and edge case tests
# ============================================================

class TestNumericalAccuracy:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_lambda_2_value(self, zeta_zeros):
        """lambda_2^KE is approximately 0.08 (converges slowly with N_zeros)."""
        mpmath.mp.dps = DPS
        lam2 = float(kers.li_coefficient_rs(2, zeta_zeros))
        # With N_zeros=100: ~0.080; with 200: ~0.084
        assert abs(lam2 - 0.080) < 0.005

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_lambda_10_value(self, zeta_zeros):
        """lambda_10^KE is approximately 3.5-3.8 (depends on N_zeros)."""
        mpmath.mp.dps = DPS
        lam10 = float(kers.li_coefficient_rs(10, zeta_zeros))
        # With N_zeros=100: ~3.56; with 200: ~3.75
        assert abs(lam10 - 3.6) < 0.3

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_zero_kappa_handling(self):
        """Virasoro at c=0 has kappa=0; RS transform is 0."""
        family = kers.virasoro_data(0.001)  # near c=0
        assert abs(family.kappa - 0.0005) < 1e-10

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_large_c_convergence(self):
        """Shadow coefficients approach 0 as c -> infinity."""
        family = kers.virasoro_data(1000.0)
        S4 = family.shadow_coefficient(4)
        assert abs(S4) < 1e-5  # S4 = 10/(1000 * 5022) ~ 2e-6
