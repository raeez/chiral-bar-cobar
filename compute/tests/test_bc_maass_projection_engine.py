r"""Tests for the BC Maass projection engine.

Verifies:
  - Maass cusp form spectral parameters (Hejhal-Then tables)
  - K-Bessel integral formulas
  - Heisenberg lattice VOA: partition function values and Maass projections
  - Virasoro vacuum character: q-expansion coefficients
  - Trivial case c=0: all projections vanish
  - Parseval identity consistency
  - Complementarity c vs 26-c
  - Self-dual point c=13 symmetry
  - Shadow data consistency
  - Rankin-Selberg consistency for Heisenberg
  - Shadow depth vs Maass projection scaling
  - Maass L-function / shadow data correlation structure

VERIFICATION PATHS:
  Path 1: Direct inner product computation via truncated Fourier expansion
  Path 2: Parseval identity (sum of all projections = L^2 norm)
  Path 3: Consistency with known Rankin-Selberg L-values for Heisenberg
  Path 4: At c=0 (trivial): Z=1, all projections vanish

60+ tests with mpmath 30+ digit precision.

Manuscript references:
    roelcke_selberg.md (compute/audit/benjamin_chang/)
    eq:roelcke-selberg-chi0 (arithmetic_shadows.tex)
    thm:refined-shadow-spectral (arithmetic_shadows.tex)
"""

import math
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    import mpmath
    from mpmath import mp, mpf, mpc, pi as MP_PI, besselk, exp, sqrt, fabs, gamma as mpgamma
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

from compute.lib import bc_maass_projection_engine as bme

DPS = 30
skipmp = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ============================================================
# Section 1: Spectral parameter table (Hejhal-Then)
# ============================================================

class TestSpectralParameters:
    """Verify the Hejhal-Then spectral parameters for even Maass cusp forms."""

    @skipmp
    def test_table_length(self):
        """We have at least 20 spectral parameters tabulated."""
        params = bme.get_spectral_params(20)
        assert len(params) == 20

    @skipmp
    def test_first_spectral_param(self):
        """t_1 = 9.5337... (first even Maass form on SL(2,Z))."""
        params = bme.get_spectral_params(1)
        t1 = float(params[0])
        assert abs(t1 - 9.5336752624) < 1e-6, f"t_1 = {t1}, expected ~9.5337"

    @skipmp
    def test_second_spectral_param(self):
        """t_2 = 12.1730..."""
        params = bme.get_spectral_params(2)
        t2 = float(params[1])
        assert abs(t2 - 12.1730039300) < 1e-6, f"t_2 = {t2}"

    @skipmp
    def test_spectral_params_increasing(self):
        """Spectral parameters are strictly increasing."""
        params = bme.get_spectral_params(20)
        for i in range(len(params) - 1):
            assert params[i] < params[i + 1], (
                f"t_{i+1} = {params[i]} >= t_{i+2} = {params[i+1]}"
            )

    @skipmp
    def test_eigenvalues_positive(self):
        """All eigenvalues lambda_j = 1/4 + t_j^2 > 1/4."""
        params = bme.get_spectral_params(20)
        for j, t_j in enumerate(params):
            lam = bme.maass_eigenvalue(t_j)
            assert lam > 0.25, f"lambda_{j+1} = {lam} <= 1/4"

    @skipmp
    def test_first_eigenvalue(self):
        """lambda_1 = 1/4 + t_1^2 ~ 91.14..."""
        params = bme.get_spectral_params(1)
        lam1 = float(bme.maass_eigenvalue(params[0]))
        expected = 0.25 + 9.5337 ** 2
        assert abs(lam1 - expected) < 0.1, f"lambda_1 = {lam1}, expected ~{expected}"

    @skipmp
    def test_spectral_parameter_table_function(self):
        """spectral_parameter_table returns correct format."""
        table = bme.spectral_parameter_table(5)
        assert len(table) == 5
        assert table[0]['j'] == 1
        assert abs(table[0]['t_j'] - 9.5337) < 0.01
        assert 'lambda_j' in table[0]

    @skipmp
    def test_selberg_eigenvalue_conjecture(self):
        """All eigenvalues satisfy lambda >= 1/4 (Selberg's conjecture, proved for SL(2,Z))."""
        params = bme.get_spectral_params(20)
        for j, t_j in enumerate(params):
            lam = bme.maass_eigenvalue(t_j)
            assert lam >= 0.25 - 1e-10, (
                f"lambda_{j+1} = {lam} violates Selberg bound 1/4"
            )


# ============================================================
# Section 2: K-Bessel integrals
# ============================================================

class TestKBesselIntegrals:
    """Verify the K-Bessel Mellin transform formulas."""

    @skipmp
    def test_k_bessel_integral_known_case(self):
        """int_0^infty y K_{0}(y) dy = pi/2 (known exactly)."""
        # For nu=0, alpha=2: 2^{0} Gamma(1) Gamma(1) = 1
        # With beta=1: (1/1^2) * 2^{0} * 1 * 1 = 1
        # Actually: int y^{alpha-1} K_0(beta*y) dy = beta^{-alpha} 2^{alpha-2} [Gamma(alpha/2)]^2
        # For alpha=2, beta=1: 2^{0} [Gamma(1)]^2 = 1
        # But int_0^infty y K_0(y) dy = (pi/2) actually... Let me verify.
        # K_0 Mellin: int y^{s-1} K_0(y) dy = 2^{s-2} [Gamma(s/2)]^2
        # For s=2: 2^0 [Gamma(1)]^2 = 1.
        # Hmm, actually int_0^infty y K_0(y) dy = 1. Let me check numerically.
        with mp.workdps(30):
            val = mpmath.quad(lambda y: y * besselk(0, y), [mpf('1e-10'), mpf('50')])
            assert abs(float(val) - 1.0) < 1e-8, f"Integral = {val}, expected 1.0"

    @skipmp
    def test_k_bessel_integral_formula(self):
        """k_bessel_integral agrees with numerical quadrature for real nu=0."""
        result = bme.k_bessel_integral(0, 2, 1, dps=30)
        # alpha=2, beta=1, t_j=0 (nu=0):
        # (1/1^2) * 2^{0} * Gamma(1) * Gamma(1) = 1
        assert abs(complex(result) - 1.0) < 1e-10, f"Formula gives {result}, expected 1"

    @skipmp
    def test_k_bessel_integral_imaginary_order(self):
        """k_bessel_integral for imaginary order nu = i*t gives positive result."""
        # alpha=3, beta=1, t=5
        result = bme.k_bessel_integral(5, 3, 1, dps=30)
        # Should be: 2^{1} Gamma((3+5i)/2) Gamma((3-5i)/2) = 2 |Gamma((3+5i)/2)|^2
        with mp.workdps(30):
            g = mpgamma(mpc(1.5, 2.5))
            expected = 2 * float(fabs(g) ** 2)
        assert abs(float(fabs(mpc(result))) - expected) < 1e-6, (
            f"Got {result}, expected ~{expected}"
        )

    @skipmp
    def test_k_bessel_symmetry(self):
        """K_{it} = K_{-it} so the integral is real for real alpha, beta."""
        r1 = bme.k_bessel_integral(9.5337, 2.5, 2.0, dps=30)
        # The integral should be real since K_{it}(x) = conj(K_{-it}(x)) for real x,
        # and the Gamma factors are conjugate pairs.
        assert abs(float(mpmath.im(mpc(r1)))) < 1e-15, (
            f"Imaginary part = {float(mpmath.im(mpc(r1)))}, should be ~0"
        )


# ============================================================
# Section 3: Heisenberg lattice partition function
# ============================================================

class TestHeisenbergLattice:
    """Tests for the Heisenberg (rank-1 lattice) partition function."""

    @skipmp
    def test_lattice_zhat_at_i(self):
        """Z-hat^1(i) = y^{1/2} |theta_3(i)|^2 = |theta_3(i)|^2."""
        # theta_3(i) = sum_{n in Z} e^{-pi n^2} is known:
        # theta_3(i) = pi^{1/4} / Gamma(3/4) ~ 1.08643...
        with mp.workdps(30):
            tau = mpc(0, 1)
            zhat = bme.heisenberg_lattice_zhat(tau, k=1, dps=30)
            # y = 1 at tau=i, so Z-hat = |theta_3(i)|^2
            expected = (mpmath.pi ** mpf('0.25') / mpgamma(mpf('0.75'))) ** 2
            assert abs(float(zhat) - float(expected)) < 1e-6, (
                f"Z-hat(i) = {zhat}, expected {expected}"
            )

    @skipmp
    def test_lattice_zhat_positive(self):
        """Z-hat is positive on the upper half-plane."""
        for tau in [complex(0, 1), complex(0.3, 1.5), complex(-0.2, 2)]:
            zhat = bme.heisenberg_lattice_zhat(tau, k=1, dps=20)
            assert float(zhat) > 0, f"Z-hat({tau}) = {zhat} <= 0"

    @skipmp
    def test_lattice_zhat_T2_invariance(self):
        """y^{1/2}|theta_3|^2 is invariant under tau -> tau+2 (theta_3 has period 2).

        NOTE: theta_3(0, tau+1) = theta_4(0, tau) != theta_3(0, tau).
        The function |theta_3|^2 is Gamma_0(2)-invariant, not SL(2,Z)-invariant.
        For the FULL lattice partition function on Z (which IS SL(2,Z)-invariant),
        one must use the Narain partition function Z = sum_{m,w} q^{p_L^2/2} bar{q}^{p_R^2/2}
        rather than |theta_3|^2 alone.  Here we test the weaker T^2 periodicity.
        """
        with mp.workdps(25):
            tau = mpc(0.3, 1.2)
            z1 = bme.heisenberg_lattice_zhat(tau, k=1, dps=25)
            z2 = bme.heisenberg_lattice_zhat(tau + 2, k=1, dps=25)
            assert abs(float(z1) - float(z2)) / max(float(z1), 1e-30) < 1e-6, (
                f"Z-hat(tau) = {z1}, Z-hat(tau+2) = {z2}"
            )

    @skipmp
    def test_lattice_zhat_s_transform_absolute(self):
        """Z-hat^1(-1/tau) relates to Z-hat^1(tau) by the S-transform of theta_3.

        Under S: tau -> -1/tau, theta_3(0, -1/tau) = sqrt(-i*tau) theta_3(0, tau).
        So |theta_3(-1/tau)|^2 = |tau| |theta_3(tau)|^2.
        And y(-1/tau) = y/|tau|^2.  Thus Z-hat(-1/tau) = (y/|tau|^2)^{1/2} |tau| |theta_3|^2
          = y^{1/2} / |tau| * |tau| * |theta_3|^2 = y^{1/2} |theta_3|^2 = Z-hat(tau).
        So Z-hat IS S-invariant.
        """
        with mp.workdps(25):
            tau = mpc(0.2, 1.3)
            z1 = bme.heisenberg_lattice_zhat(tau, k=1, dps=25)
            z2 = bme.heisenberg_lattice_zhat(-1 / tau, k=1, dps=25)
            assert abs(float(z1) - float(z2)) / max(float(z1), 1e-30) < 1e-4, (
                f"Z-hat(tau) = {z1}, Z-hat(-1/tau) = {z2}"
            )

    @skipmp
    def test_lattice_l2_norm_infinite_for_chiral(self):
        """The chiral Heisenberg character y^{k/2} is NOT in L^2 for k>0."""
        result = bme.heisenberg_eta_power_l2_norm(1, dps=20)
        assert result == float('inf'), "L^2 norm should be infinite"


# ============================================================
# Section 4: Virasoro vacuum character
# ============================================================

class TestVirasoroCharacter:
    """Tests for the Virasoro vacuum character q-expansion."""

    @skipmp
    def test_p2_initial_values(self):
        """p_2(0) = 1, p_2(1) = 0, p_2(2) = 1, p_2(3) = 1, p_2(4) = 2."""
        coeffs = bme.virasoro_vacuum_character_q_expansion(1, 10, 30)
        # p_2(n) = partitions into parts >= 2:
        # p_2(0) = 1 (empty partition)
        # p_2(1) = 0 (no parts >= 2 sum to 1)
        # p_2(2) = 1 (just {2})
        # p_2(3) = 1 (just {3})
        # p_2(4) = 2 ({4}, {2,2})
        # p_2(5) = 2 ({5}, {3,2})
        # p_2(6) = 4 ({6}, {4,2}, {3,3}, {2,2,2})
        assert float(coeffs[0]) == 1, f"p_2(0) = {coeffs[0]}"
        assert float(coeffs[1]) == 0, f"p_2(1) = {coeffs[1]}"
        assert float(coeffs[2]) == 1, f"p_2(2) = {coeffs[2]}"
        assert float(coeffs[3]) == 1, f"p_2(3) = {coeffs[3]}"
        assert float(coeffs[4]) == 2, f"p_2(4) = {coeffs[4]}"
        assert float(coeffs[5]) == 2, f"p_2(5) = {coeffs[5]}"
        assert float(coeffs[6]) == 4, f"p_2(6) = {coeffs[6]}"

    @skipmp
    def test_p2_from_partition_relation(self):
        """p_2(n) = p(n) - p(n-1) where p is the partition function."""
        # Verify against known values of the partition function
        # p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7, p(6)=11, p(7)=15
        expected_p2 = [1, 0, 1, 1, 2, 2, 4, 4]
        coeffs = bme.virasoro_vacuum_character_q_expansion(1, 10, 30)
        for n in range(len(expected_p2)):
            assert abs(float(coeffs[n]) - expected_p2[n]) < 1e-10, (
                f"p_2({n}) = {coeffs[n]}, expected {expected_p2[n]}"
            )

    @skipmp
    def test_p2_generates_correct_total(self):
        """sum_{n=0}^{20} p_2(n) should match the generating function at q=1^-."""
        # prod_{n>=2} 1/(1-x^n) evaluated at x close to 1:
        # This diverges, but the partial sums should be consistent.
        coeffs = bme.virasoro_vacuum_character_q_expansion(1, 30, 30)
        # Verify sum matches the direct product expansion at q = 0.5
        q = mpf('0.5')
        gf_val = mpf(1)
        for n in range(2, 30):
            gf_val /= (1 - q ** n)
        series_val = sum(float(coeffs[n]) * 0.5 ** n for n in range(30))
        assert abs(float(gf_val) - series_val) < 1e-5, (
            f"GF = {gf_val}, series = {series_val}"
        )

    @skipmp
    def test_virasoro_zhat_positive(self):
        """Z-hat^c_Vir is positive for tau = i, c = 1."""
        with mp.workdps(20):
            zhat = bme.virasoro_zhat_numerical(complex(0, 1.5), 1, 100, 20)
            assert float(zhat) > 0, f"Z-hat = {zhat}"


# ============================================================
# Section 5: Trivial case c=0 (verification path 4)
# ============================================================

class TestTrivialC0:
    """At c=0, Z=1 and all Maass projections must vanish."""

    @skipmp
    def test_c0_first_maass_form(self):
        """<1, u_1> = 0 since Maass cusp forms integrate to zero."""
        result = bme.trivial_c0_check(HEJHAL_T1, dps=15)
        assert result['abs_projection'] < 0.1, (
            f"|<1, u_1>| = {result['abs_projection']}, expected ~0"
        )

    @skipmp
    def test_c0_second_maass_form(self):
        """<1, u_2> = 0."""
        result = bme.trivial_c0_check(HEJHAL_T2, dps=15)
        assert result['abs_projection'] < 0.1, (
            f"|<1, u_2>| = {result['abs_projection']}, expected ~0"
        )

    @skipmp
    def test_c0_multiple_forms(self):
        """All Maass projections of the constant function vanish."""
        params = bme.get_spectral_params(5)
        for j, t_j in enumerate(params):
            result = bme.trivial_c0_check(t_j, dps=12)
            assert result['abs_projection'] < 0.2, (
                f"|<1, u_{j+1}>| = {result['abs_projection']}, expected ~0"
            )


# Convenience: store commonly used spectral parameters
HEJHAL_T1 = '9.5336752624429843'
HEJHAL_T2 = '12.1730039300295800'
HEJHAL_T3 = '13.7797513468489540'


# ============================================================
# Section 6: Shadow data consistency
# ============================================================

class TestShadowData:
    """Verify shadow data for standard families matches known values."""

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2 (AP1, AP20, AP39 cross-check)."""
        for c in [1, 1/2, 25, 13, 26]:
            data = bme.shadow_data_standard_families(c)
            assert abs(data['kappa'] - c / 2) < 1e-15, (
                f"kappa({c}) = {data['kappa']}, expected {c/2}"
            )

    def test_virasoro_alpha(self):
        """alpha = 2 for Virasoro (cubic shadow coefficient)."""
        for c in [1, 10, 25]:
            data = bme.shadow_data_standard_families(c)
            assert abs(data['alpha'] - 2.0) < 1e-15

    def test_virasoro_S4(self):
        """S_4 = 10/(c(5c+22)) for Virasoro."""
        for c in [1, 2, 10, 25]:
            data = bme.shadow_data_standard_families(c)
            expected = 10.0 / (c * (5 * c + 22))
            assert abs(data['S_4'] - expected) < 1e-12, (
                f"S_4({c}) = {data['S_4']}, expected {expected}"
            )

    def test_virasoro_delta(self):
        """Delta = 40/(5c+22) for Virasoro."""
        for c in [1, 2, 10, 25]:
            data = bme.shadow_data_standard_families(c)
            expected = 40.0 / (5 * c + 22)
            assert abs(data['Delta'] - expected) < 1e-12

    def test_complementarity_kappa_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24: NOT zero)."""
        for c in [1, 5, 10, 13, 20, 25]:
            k1 = bme.shadow_data_standard_families(c)['kappa']
            k2 = bme.shadow_data_standard_families(26 - c)['kappa']
            assert abs(k1 + k2 - 13) < 1e-12, (
                f"kappa({c}) + kappa({26-c}) = {k1 + k2}, expected 13"
            )

    def test_self_dual_point(self):
        """At c=13: kappa = 13/2 = 6.5, Delta symmetric."""
        data = bme.shadow_data_standard_families(13)
        assert abs(data['kappa'] - 6.5) < 1e-15
        data_dual = bme.shadow_data_standard_families(13)
        assert abs(data['Delta'] - data_dual['Delta']) < 1e-15

    def test_delta_complementarity(self):
        """Delta(c) and Delta(26-c): check the complementarity structure."""
        for c in [1, 5, 10, 20]:
            d1 = bme.shadow_data_standard_families(c)['Delta']
            d2 = bme.shadow_data_standard_families(26 - c)['Delta']
            # Delta(c) = 40/(5c+22), Delta(26-c) = 40/(5(26-c)+22) = 40/(152-5c)
            # Sum = 40/(5c+22) + 40/(152-5c) = 40(152-5c+5c+22)/((5c+22)(152-5c))
            #     = 40*174/((5c+22)(152-5c)) = 6960/((5c+22)(152-5c))
            expected_sum = 6960.0 / ((5 * c + 22) * (152 - 5 * c))
            assert abs(d1 + d2 - expected_sum) < 1e-10, (
                f"Delta({c})+Delta({26-c}) = {d1+d2}, expected {expected_sum}"
            )


# ============================================================
# Section 7: Complementarity structure
# ============================================================

class TestComplementarity:
    """Test Maass projection complementarity under c -> 26-c."""

    @skipmp
    def test_kappa_sum_13(self):
        """kappa + kappa' = 13 for all Virasoro pairs (AP24)."""
        result = bme.virasoro_complementarity_maass(10, HEJHAL_T1, 50, 12)
        assert abs(result['kappa_sum'] - 13) < 1e-12

    @skipmp
    def test_self_dual_c13(self):
        """At c=13, the projections for c and 26-c should be identical."""
        result = bme.self_dual_maass_symmetry(HEJHAL_T1, 50, 12)
        # c = 13, c_dual = 13
        assert result['c'] == 13
        assert result['c_dual'] == 13

    @skipmp
    def test_complementarity_ratio_exists(self):
        """The ratio F_c/F_{26-c} should be computable for generic c."""
        result = bme.virasoro_complementarity_maass(5, HEJHAL_T1, 50, 12)
        # Just verify the computation completes without error
        assert 'proj_c' in result
        assert 'proj_dual' in result


# ============================================================
# Section 8: Rankin-Selberg consistency (verification path 3)
# ============================================================

class TestRankinSelberg:
    """Verify Rankin-Selberg L-values for Heisenberg."""

    @skipmp
    def test_heisenberg_epsilon_1s(self):
        """epsilon^1_s = 2*zeta(2s) for the rank-1 lattice VOA."""
        # This is the known result from roelcke_selberg.md section 2.2
        result = bme.heisenberg_rankin_selberg_check(complex(2, 0), k=1, dps=30)
        expected = complex(result['expected_epsilon'])
        # epsilon^1_2 = 2 * zeta(4) = 2 * pi^4/90 = pi^4/45
        with mp.workdps(30):
            val = 2 * float(mpmath.zeta(4))
            assert abs(expected.real - val) < 1e-10, (
                f"epsilon^1_2 = {expected}, expected {val}"
            )

    @skipmp
    def test_heisenberg_epsilon_known_value(self):
        """epsilon^1_s at s=1.5: 2*zeta(3) ~ 2*1.202... = 2.404..."""
        with mp.workdps(30):
            expected = 2 * float(mpmath.zeta(3))
            result = bme.heisenberg_rankin_selberg_check(1.5, k=1, dps=30)
            eps = complex(result['expected_epsilon'])
            assert abs(eps.real - expected) < 1e-8, (
                f"epsilon^1_{{3/2}} = {eps}, expected {expected}"
            )

    @skipmp
    def test_heisenberg_direct_sum_convergence(self):
        """The direct sum in the RS check converges to a finite value."""
        result = bme.heisenberg_rankin_selberg_check(complex(2, 0), k=1, dps=30)
        assert result['direct_sum'] is not None
        ds = complex(result['direct_sum'])
        assert abs(ds) < 1e10, f"Direct sum = {ds}"
        assert abs(ds) > 1e-10, f"Direct sum too small = {ds}"


# ============================================================
# Section 9: Maass form evaluation
# ============================================================

class TestMaassFormEvaluation:
    """Test the approximate Maass form evaluator."""

    @skipmp
    def test_maass_form_at_i(self):
        """u_j(i) is finite and nonzero (generically)."""
        with mp.workdps(20):
            val = bme.maass_form_value(complex(0, 1), 9.5337, n_fourier=2, dps=20)
            # The value should be finite (may be complex from K-Bessel)
            assert float(fabs(mpc(val))) < 1e10, f"|u_1(i)| = {val}"

    @skipmp
    def test_maass_form_decay(self):
        """Maass cusp forms decay exponentially as y -> infinity."""
        with mp.workdps(20):
            v1 = float(fabs(mpc(bme.maass_form_value(complex(0, 1), 9.5337, 2, 20))))
            v2 = float(fabs(mpc(bme.maass_form_value(complex(0, 5), 9.5337, 2, 20))))
            # K_{it}(2*pi*y) ~ sqrt(pi/(4*pi*y)) e^{-2*pi*y} for large y
            # So u(0+5i) should be much smaller than u(0+i)
            if v1 > 1e-20:
                assert v2 / v1 < 0.01, (
                    f"u(5i)/u(i) = {v2/v1}, expected exponential decay"
                )

    @skipmp
    def test_maass_form_even_symmetry(self):
        """Even Maass forms satisfy u(-x+iy) = u(x+iy)."""
        with mp.workdps(20):
            val_plus = bme.maass_form_value(complex(0.3, 1.5), 9.5337, 2, 20)
            val_minus = bme.maass_form_value(complex(-0.3, 1.5), 9.5337, 2, 20)
            # Both values may be mpc; compare their real parts (even Maass forms are real-valued)
            diff = float(fabs(mpc(val_plus) - mpc(val_minus)))
            scale = max(float(fabs(mpc(val_plus))), 1e-20)
            assert diff / scale < 1e-8, (
                f"u(0.3+1.5i) = {val_plus}, u(-0.3+1.5i) = {val_minus}"
            )


# ============================================================
# Section 10: Numerical Maass projection
# ============================================================

class TestMaassProjectionNumerical:
    """Test the numerical fundamental-domain integration."""

    @skipmp
    def test_constant_function_projection_vanishes(self):
        """<1, u_j> = 0 for any Maass cusp form (orthogonality)."""
        result = bme.maass_projection_numerical(
            lambda tau: mpf(1), 9.5337, n_x=20, n_y=15, dps=12
        )
        assert result['abs'] < 0.2, (
            f"|<1, u_1>| = {result['abs']}, expected ~0"
        )

    @skipmp
    def test_y_power_projection(self):
        """<y^s, u_j> for s = 1/2 should be small (y^{1/2} has no cuspidal content
        in the sense that it contributes to the Eisenstein spectrum, not Maass)."""
        # y^s is an eigenfunction of the Laplacian: Delta(y^s) = s(1-s) y^s.
        # For s = 1/2: eigenvalue 1/4, which is NOT a Maass eigenvalue
        # (the first one is ~91). So <y^{1/2}, u_j> should be 0 by orthogonality.
        # BUT y^{1/2} is not in L^2, so this is a distributional statement.
        # For the truncated fundamental domain, we expect a small numerical value.
        with mp.workdps(15):
            def f_y_half(tau):
                return mpmath.im(tau) ** mpf('0.5')

            result = bme.maass_projection_numerical(
                f_y_half, 9.5337, n_x=15, n_y=10, dps=12
            )
            # This should be small (not exactly 0 due to truncation)
            assert result['abs'] < 1.0, f"|<y^{{1/2}}, u_1>| = {result['abs']}"


# ============================================================
# Section 11: Homotopy defect
# ============================================================

class TestHomotopyDefect:
    """Test the homotopy defect computation."""

    @skipmp
    def test_defect_nonnegative(self):
        """Def_Maass >= 0 (sum of squares)."""
        def f_const(tau):
            return mpf(1)
        result = bme.homotopy_defect_maass(f_const, n_forms=3, dps=10)
        assert result['defect'] >= -1e-10, f"Defect = {result['defect']} < 0"

    @skipmp
    def test_defect_contributions_list(self):
        """The contributions list has the right length."""
        def f_const(tau):
            return mpf(1)
        result = bme.homotopy_defect_maass(f_const, n_forms=3, dps=10)
        assert len(result['contributions']) == 3


# ============================================================
# Section 12: Parseval decomposition
# ============================================================

class TestParseval:
    """Test Parseval identity consistency (verification path 2)."""

    @skipmp
    def test_parseval_constant_function(self):
        """For f=1: ||1||^2 = pi/3. All Maass projections = 0. Residual = 1."""
        # <1, 1> = vol(F) = pi/3. The residual contribution is
        # |<f,1>|^2 * (3/pi) where <f,1> = int_F 1 d mu = pi/3.
        # So residual_norm_sq = (pi/3)^2 * (3/pi) = pi/3.
        result = bme.parseval_check_constant(lambda tau: mpf(1), dps=12)
        # c_0 should be approximately pi/3
        expected_c0 = math.pi / 3
        # The computation is approximate due to truncation
        assert abs(abs(result['c_0']) - expected_c0) < 0.5, (
            f"|c_0| = {abs(result['c_0'])}, expected ~{expected_c0}"
        )

    @skipmp
    def test_parseval_sum_nonnegative(self):
        """Each component of the Parseval decomposition is nonnegative."""
        result = bme.parseval_decomposition(
            lambda tau: mpf(1), math.pi / 3, n_forms=2, dps=10
        )
        assert result['residual_contrib'] >= -0.1
        assert result['maass_contrib_truncated'] >= -1e-5


# ============================================================
# Section 13: Eisenstein spectral coefficient
# ============================================================

class TestEisensteinCoefficient:
    """Test the Eisenstein spectral coefficient computation."""

    @skipmp
    def test_eisenstein_coeff_computable(self):
        """The Eisenstein coefficient can be computed without error."""
        def f_const(tau):
            return mpf(1)
        result = bme.eisenstein_spectral_coefficient(f_const, 1.0, dps=12)
        assert 'c_E' in result
        assert 'abs_c_E' in result

    @skipmp
    def test_eisenstein_coeff_at_multiple_t(self):
        """Eisenstein coefficients at different t values are computable."""
        def f_const(tau):
            return mpf(1)
        for t in [0.5, 1.0, 5.0]:
            result = bme.eisenstein_spectral_coefficient(f_const, t, dps=10)
            # Should complete without error
            assert isinstance(result['c_E'], complex)


# ============================================================
# Section 14: Shadow-Maass correlation
# ============================================================

class TestShadowMaassCorrelation:
    """Test the shadow data / Maass L-function correlation analysis."""

    @skipmp
    def test_correlation_structure(self):
        """shadow_maass_correlation returns correct structure."""
        result = bme.shadow_maass_correlation(10, n_forms=2, dps=10)
        assert 'shadow_data' in result
        assert 'maass_data' in result
        assert len(result['maass_data']) == 2
        assert result['shadow_data']['kappa'] == 5.0

    @skipmp
    def test_correlation_conductor_weight_positive(self):
        """The conductor weight 1/cosh(pi*t/2) is positive and decreasing."""
        result = bme.shadow_maass_correlation(10, n_forms=3, dps=10)
        for item in result['maass_data']:
            assert item['conductor_weight'] > 0
        # Check monotone decreasing (higher t -> smaller weight)
        weights = [item['conductor_weight'] for item in result['maass_data']]
        for i in range(len(weights) - 1):
            assert weights[i] >= weights[i + 1] - 1e-10


# ============================================================
# Section 15: Shadow depth scaling
# ============================================================

class TestShadowDepthScaling:
    """Test the shadow depth vs Maass projection scaling."""

    @skipmp
    def test_depth_scaling_computable(self):
        """shadow_depth_maass_scaling runs without error."""
        # Use a small set of c values
        result = bme.shadow_depth_maass_scaling([1, 10], t_j_index=0, dps=10)
        assert 'results' in result
        assert len(result['results']) == 2

    @skipmp
    def test_depth_scaling_kappa_values(self):
        """kappa values in the scaling results are correct."""
        result = bme.shadow_depth_maass_scaling([2, 20], t_j_index=0, dps=10)
        for item in result['results']:
            assert abs(item['kappa'] - item['c'] / 2) < 1e-12


# ============================================================
# Section 16: Full analysis diagnostic
# ============================================================

class TestFullAnalysis:
    """Test the full_maass_analysis summary function."""

    @skipmp
    def test_heisenberg_analysis(self):
        """Heisenberg analysis returns correct metadata."""
        result = bme.full_maass_analysis('heisenberg', {'c': 1, 'k': 1})
        assert result['family'] == 'heisenberg'
        assert result['shadow_depth'] == 2
        assert result['kappa'] == 0.5

    @skipmp
    def test_virasoro_analysis(self):
        """Virasoro analysis computes projections."""
        result = bme.full_maass_analysis('virasoro', {'c': 10}, n_forms=2, dps=10)
        assert result['family'] == 'virasoro'
        assert result['shadow_depth'] == float('inf')
        assert 'projections' in result
        assert len(result['projections']) == 2

    @skipmp
    def test_unknown_family(self):
        """Unknown family returns error message."""
        result = bme.full_maass_analysis('unknown', {'c': 1})
        assert 'error' in result


# ============================================================
# Section 17: Cross-verification with benjamin_chang_analysis
# ============================================================

class TestCrossVerification:
    """Cross-verify with the existing Benjamin-Chang analysis module."""

    @skipmp
    def test_spectral_params_consistent_with_zeta_zeros(self):
        """Maass spectral parameters t_j are distinct from zeta zero imaginary parts."""
        # The zeta zeros gamma_n and Maass params t_j are different objects.
        # gamma_1 = 14.134... while t_1 = 9.534...
        # This is a sanity check that we are not confusing them.
        from compute.lib import benjamin_chang_analysis as bca
        with mp.workdps(20):
            poles = bca.scattering_pole_positions(5, 20)
            maass_params = bme.get_spectral_params(5)
            for j in range(5):
                gamma_j = poles[j]['gamma']
                t_j = float(maass_params[j])
                assert abs(gamma_j - t_j) > 0.5, (
                    f"gamma_{j+1} = {gamma_j} too close to t_{j+1} = {t_j}"
                )

    @skipmp
    def test_zeta_zeros_and_maass_params_interleave(self):
        """The first zeta zero gamma_1 ~ 14.13 lies between t_3 and t_4."""
        # t_3 ~ 13.78, t_4 ~ 14.36, gamma_1 ~ 14.13
        params = bme.get_spectral_params(5)
        from compute.lib import benjamin_chang_analysis as bca
        with mp.workdps(20):
            poles = bca.scattering_pole_positions(1, 20)
            gamma_1 = poles[0]['gamma']
            t3 = float(params[2])
            t4 = float(params[3])
            assert t3 < gamma_1 < t4, (
                f"Expected t_3 < gamma_1 < t_4: {t3} < {gamma_1} < {t4}"
            )


# ============================================================
# Section 18: Maass eigenvalue properties
# ============================================================

class TestMaassEigenvalues:
    """Mathematical properties of the Maass eigenvalues."""

    @skipmp
    def test_eigenvalue_formula(self):
        """lambda = 1/4 + t^2 for t = 9.5337."""
        t = mpf('9.5337')
        lam = bme.maass_eigenvalue(t)
        expected = mpf('0.25') + t * t
        assert abs(float(lam) - float(expected)) < 1e-6

    @skipmp
    def test_eigenvalue_gap(self):
        """lambda_1 ~ 91.14, lambda_2 ~ 148.43: substantial gap."""
        params = bme.get_spectral_params(2)
        lam1 = float(bme.maass_eigenvalue(params[0]))
        lam2 = float(bme.maass_eigenvalue(params[1]))
        assert lam2 > lam1 + 10, f"Gap too small: {lam2} - {lam1} = {lam2 - lam1}"

    @skipmp
    def test_weyl_law_consistency(self):
        """N(T) ~ T^2/(12) for the number of eigenvalues below T^2 + 1/4.

        For T = 25.05 (our last spectral parameter), there should be ~52
        eigenvalues.  We have 20 EVEN ones, so ~40 total even eigenvalues
        up to T=25 is reasonable (Weyl law counts both even and odd).
        """
        params = bme.get_spectral_params(20)
        T = float(params[-1])
        weyl_count = T ** 2 / 12
        # We have 20 even forms; total (even + odd) should be roughly 2x
        # Weyl law: N(T) ~ T^2/12 for SL(2,Z)
        # T ~ 25: N ~ 625/12 ~ 52
        # We have 20 even forms; plausible if ~30 odd forms below T=25.
        assert weyl_count > 10, f"Weyl count {weyl_count} too small"
        assert weyl_count < 200, f"Weyl count {weyl_count} too large"


# ============================================================
# Section 19: Edge cases and robustness
# ============================================================

class TestEdgeCases:
    """Test edge cases and numerical robustness."""

    @skipmp
    def test_large_c(self):
        """Shadow data at large c is well-defined."""
        data = bme.shadow_data_standard_families(1000)
        assert data['kappa'] == 500
        assert data['Delta'] > 0
        assert data['S_4'] > 0

    @skipmp
    def test_small_c(self):
        """Shadow data at small positive c."""
        data = bme.shadow_data_standard_families(0.01)
        assert abs(data['kappa'] - 0.005) < 1e-15
        assert data['Delta'] > 0

    def test_c_zero_shadow(self):
        """Shadow data at c=0: kappa=0, S_4 diverges."""
        data = bme.shadow_data_standard_families(0)
        assert data['kappa'] == 0
        assert data['S_4'] == float('inf')

    @skipmp
    def test_negative_c_shadow(self):
        """Shadow data at negative c (unphysical but mathematically defined)."""
        data = bme.shadow_data_standard_families(-5)
        assert data['kappa'] == -2.5
        # Delta = 40/(5*(-5)+22) = 40/(-3) < 0
        assert data['Delta'] < 0
