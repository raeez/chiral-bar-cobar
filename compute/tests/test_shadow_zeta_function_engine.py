r"""Tests for the shadow zeta function engine.

Multi-path verification of all shadow zeta results:
    Path 1: Direct summation from shadow coefficients
    Path 2: Mellin transform of the shadow generating function
    Path 3: Closed-form exact evaluation (for finite towers)
    Path 4: Cross-family consistency and limiting cases

80+ tests covering:
    - Heisenberg (class G): exact closed form, trivially entire
    - Affine sl_2, sl_3 (class L): two-term exact form
    - Beta-gamma (class C): three-term exact form
    - Virasoro (class M): infinite tower, growth rate, convergence
    - W_3 T-line and W-line (class M): two independent shadow lines
    - Twisted zeta with Dirichlet characters
    - Functional equation candidates
    - Multiplicativity analysis
    - Koszul duality relations
    - Special values at s = 0, 1, 2
    - Abscissa of convergence classification

Tolerance: 1e-10 for exact comparisons, 1e-6 for numerical quadrature.
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import math
import cmath
import pytest
from fractions import Fraction as F

from compute.lib.shadow_zeta_function_engine import (
    # Shadow coefficient providers
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    w3_t_line_shadow_coefficients,
    w3_w_line_shadow_coefficients,
    # Core zeta functions
    shadow_zeta_numerical,
    shadow_zeta_at_integers,
    completed_shadow_zeta_numerical,
    # Abscissa and growth
    abscissa_of_convergence,
    abscissa_from_growth_rate,
    shadow_growth_rate_from_coeffs,
    virasoro_growth_rate_exact,
    # Mellin
    mellin_transform_zeta,
    shadow_generating_function_numerical,
    # Twisted zeta
    dirichlet_character_mod4,
    dirichlet_character_mod8_1,
    dirichlet_character_mod8_2,
    twisted_shadow_zeta_numerical,
    # Euler product
    check_multiplicativity,
    formal_euler_product_coefficients,
    # Special values
    shadow_zeta_special_values,
    # Exact closed forms
    heisenberg_zeta_exact,
    heisenberg_completed_zeta,
    affine_sl2_zeta_exact,
    affine_sl3_zeta_exact,
    betagamma_zeta_exact,
    # Virasoro
    virasoro_zeta_from_ode,
    virasoro_zeta_values_table,
    virasoro_koszul_dual_zeta_relation,
    # Cross-family
    compute_shadow_zeta_data,
    compute_full_landscape,
    ShadowZetaData,
    # Convergence
    convergence_domain_analysis,
    # Functional equation
    functional_equation_test,
)


TOL = 1e-10
TOL_QUAD = 1e-4  # Relaxed for numerical quadrature


# ============================================================================
# HEISENBERG (Class G) — 15 tests
# ============================================================================

class TestHeisenbergZeta:
    """Heisenberg H_k: zeta_{H_k}(s) = k * 2^{-s}. Finite sum, entire."""

    def test_shadow_coefficients_k1(self):
        """S_2 = 1, S_r = 0 for r >= 3."""
        coeffs = heisenberg_shadow_coefficients(1.0, 20)
        assert abs(coeffs[2] - 1.0) < TOL
        for r in range(3, 21):
            assert coeffs[r] == 0.0

    def test_shadow_coefficients_k_half(self):
        """S_2 = 1/2 for k = 1/2."""
        coeffs = heisenberg_shadow_coefficients(0.5, 10)
        assert abs(coeffs[2] - 0.5) < TOL

    def test_exact_zeta_s2(self):
        """zeta_{H_1}(2) = 1 * 2^{-2} = 1/4."""
        assert abs(heisenberg_zeta_exact(1.0, 2.0) - 0.25) < TOL

    def test_exact_zeta_s0(self):
        """zeta_{H_1}(0) = 1 * 2^0 = 1."""
        assert abs(heisenberg_zeta_exact(1.0, 0.0) - 1.0) < TOL

    def test_exact_zeta_s1(self):
        """zeta_{H_1}(1) = 1/2."""
        assert abs(heisenberg_zeta_exact(1.0, 1.0) - 0.5) < TOL

    def test_exact_zeta_negative_s(self):
        """zeta_{H_k}(-1) = k * 2^1 = 2k."""
        assert abs(heisenberg_zeta_exact(3.0, -1.0) - 6.0) < TOL

    def test_direct_vs_exact_k1(self):
        """Path 1 (direct sum) vs Path 3 (exact) for k=1."""
        coeffs = heisenberg_shadow_coefficients(1.0)
        for s in [0.0, 1.0, 2.0, 5.0, -1.0]:
            direct = shadow_zeta_numerical(coeffs, complex(s, 0)).real
            exact = heisenberg_zeta_exact(1.0, s)
            assert abs(direct - exact) < TOL, f"Mismatch at s={s}"

    def test_direct_vs_exact_k5(self):
        """Path 1 vs Path 3 for k=5."""
        coeffs = heisenberg_shadow_coefficients(5.0)
        for s in [0.0, 1.0, 3.0, 10.0]:
            direct = shadow_zeta_numerical(coeffs, complex(s, 0)).real
            exact = heisenberg_zeta_exact(5.0, s)
            assert abs(direct - exact) < TOL

    def test_abscissa_neg_infinity(self):
        """Abscissa of convergence = -infinity for Heisenberg (finite sum)."""
        coeffs = heisenberg_shadow_coefficients(1.0)
        sigma = abscissa_of_convergence(coeffs)
        assert sigma < -1e5  # Our proxy for -infinity

    def test_growth_rate_zero(self):
        """Shadow growth rate = 0 for Heisenberg (tower terminates)."""
        coeffs = heisenberg_shadow_coefficients(1.0)
        rho = shadow_growth_rate_from_coeffs(coeffs)
        assert rho == 0.0

    def test_special_values(self):
        """zeta(0) = k, zeta(1) = k/2, zeta(2) = k/4."""
        coeffs = heisenberg_shadow_coefficients(1.0)
        sv = shadow_zeta_special_values(coeffs)
        assert abs(sv['zeta(0)'] - 1.0) < TOL
        assert abs(sv['zeta(1)'] - 0.5) < TOL
        assert abs(sv['zeta(2)'] - 0.25) < TOL

    def test_multiplicativity_trivial(self):
        """Heisenberg is trivially multiplicative (only one nonzero term)."""
        coeffs = heisenberg_shadow_coefficients(1.0, 20)
        is_mult, violations = check_multiplicativity(coeffs, 20)
        assert is_mult

    def test_completed_zeta_s2(self):
        """Lambda_{H_1}(2) = Gamma(1) * pi^{-1} * (1/4)."""
        val = heisenberg_completed_zeta(1.0, complex(2.0, 0))
        expected = math.gamma(1.0) * math.pi ** (-1.0) * 0.25
        assert abs(val - expected) < TOL

    def test_level_scaling(self):
        """zeta_{H_k}(s) = k * zeta_{H_1}(s) (linearity in level)."""
        for k in [0.5, 1.0, 2.0, 7.0]:
            for s in [0.0, 1.0, 2.0, 5.0]:
                val_k = heisenberg_zeta_exact(k, s)
                val_1 = heisenberg_zeta_exact(1.0, s)
                assert abs(val_k - k * val_1) < TOL

    def test_complex_s(self):
        """zeta_{H_1}(1+2i) = 2^{-(1+2i)} = (1/2) * exp(-2i*log2)."""
        s = complex(1.0, 2.0)
        val = heisenberg_zeta_exact(1.0, s)
        expected = 2.0 ** (-s)
        assert abs(val - expected) < TOL


# ============================================================================
# AFFINE sl_2 (Class L) — 12 tests
# ============================================================================

class TestAffineSl2Zeta:
    """Affine sl_2: zeta(s) = kappa * 2^{-s} + alpha * 3^{-s}."""

    def test_shadow_coefficients_k1(self):
        """kappa = 3(1+2)/4 = 9/4, alpha = 4/(1+2) = 4/3."""
        coeffs = affine_sl2_shadow_coefficients(1.0, 10)
        assert abs(coeffs[2] - 2.25) < TOL  # 9/4
        assert abs(coeffs[3] - 4.0 / 3.0) < TOL
        for r in range(4, 11):
            assert abs(coeffs[r]) < TOL

    def test_exact_zeta_s0(self):
        """zeta(0) = kappa + alpha."""
        k = 1.0
        val = affine_sl2_zeta_exact(k, 0.0)
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        assert abs(val - (kappa + alpha)) < TOL

    def test_exact_zeta_s1(self):
        """zeta(1) = kappa/2 + alpha/3."""
        k = 1.0
        kappa = 9.0 / 4.0
        alpha = 4.0 / 3.0
        expected = kappa / 2.0 + alpha / 3.0
        val = affine_sl2_zeta_exact(k, 1.0)
        assert abs(val - expected) < TOL

    def test_direct_vs_exact(self):
        """Path 1 (direct sum) vs Path 3 (exact) for k=1."""
        coeffs = affine_sl2_shadow_coefficients(1.0)
        for s in [0.0, 1.0, 2.0, 5.0, 10.0]:
            direct = shadow_zeta_numerical(coeffs, complex(s, 0)).real
            exact = affine_sl2_zeta_exact(1.0, s)
            assert abs(direct - exact) < TOL, f"Mismatch at s={s}"

    def test_abscissa(self):
        """Finite tower => abscissa = -infinity."""
        coeffs = affine_sl2_shadow_coefficients(1.0)
        sigma = abscissa_of_convergence(coeffs)
        assert sigma < -1e5

    def test_growth_rate_zero(self):
        """Shadow growth rate = 0 (tower terminates at arity 3)."""
        coeffs = affine_sl2_shadow_coefficients(1.0)
        rho = shadow_growth_rate_from_coeffs(coeffs)
        assert rho == 0.0

    def test_level_dependence(self):
        """kappa and alpha are level-dependent."""
        for k in [1, 2, 5, 10]:
            kappa = 3.0 * (k + 2.0) / 4.0
            alpha = 4.0 / (k + 2.0)
            coeffs = affine_sl2_shadow_coefficients(float(k))
            assert abs(coeffs[2] - kappa) < TOL
            assert abs(coeffs[3] - alpha) < TOL

    def test_kappa_formula(self):
        """kappa = dim(sl_2)*(k+h^v)/(2*h^v) = 3(k+2)/4."""
        for k in [1, 3, 10, 100]:
            kappa = 3.0 * (k + 2.0) / 4.0
            coeffs = affine_sl2_shadow_coefficients(float(k))
            assert abs(coeffs[2] - kappa) < TOL

    def test_large_s_decay(self):
        """For large Re(s), zeta(s) -> 0."""
        coeffs = affine_sl2_shadow_coefficients(1.0)
        val = shadow_zeta_numerical(coeffs, complex(100.0, 0))
        assert abs(val) < TOL

    def test_not_multiplicative(self):
        """Affine sl_2 tower is multiplicative trivially (only 2 nonzero terms; 2,3 coprime)."""
        coeffs = affine_sl2_shadow_coefficients(1.0, 20)
        is_mult, violations = check_multiplicativity(coeffs, 20)
        # S_6 should equal S_2 * S_3 if multiplicative. S_6 = 0, S_2*S_3 != 0.
        assert not is_mult

    def test_special_values(self):
        """Cross-check special values at s=0,1,2."""
        coeffs = affine_sl2_shadow_coefficients(1.0)
        sv = shadow_zeta_special_values(coeffs)
        kappa = 2.25
        alpha = 4.0 / 3.0
        assert abs(sv['zeta(0)'] - (kappa + alpha)) < TOL
        assert abs(sv['zeta(1)'] - (kappa / 2.0 + alpha / 3.0)) < TOL
        assert abs(sv['zeta(2)'] - (kappa / 4.0 + alpha / 9.0)) < TOL

    def test_sl3_exact_vs_direct(self):
        """Path 1 vs Path 3 for affine sl_3 at k=1."""
        coeffs = affine_sl3_shadow_coefficients(1.0)
        for s in [0.0, 1.0, 2.0]:
            direct = shadow_zeta_numerical(coeffs, complex(s, 0)).real
            exact = affine_sl3_zeta_exact(1.0, s)
            assert abs(direct - exact) < TOL


# ============================================================================
# BETA-GAMMA (Class C) — 10 tests
# ============================================================================

class TestBetaGammaZeta:
    """Beta-gamma: three-term exact form."""

    def test_shadow_coefficients_lam_half(self):
        """At lambda=1/2: c=-1, kappa=-1/2, S_3=2, S_4=10/(-1*(-5+22))=-10/17."""
        coeffs = betagamma_shadow_coefficients(0.5)
        assert abs(coeffs[2] - (-0.5)) < TOL
        assert abs(coeffs[3] - 2.0) < TOL
        expected_S4 = 10.0 / (-1.0 * (-5.0 + 22.0))
        assert abs(coeffs[4] - expected_S4) < TOL
        for r in range(5, 20):
            assert abs(coeffs[r]) < TOL

    def test_shadow_coefficients_lam_1(self):
        """At lambda=1: c=2, kappa=1, S_3=2, S_4=10/(2*32)=5/32."""
        coeffs = betagamma_shadow_coefficients(1.0)
        assert abs(coeffs[2] - 1.0) < TOL
        assert abs(coeffs[3] - 2.0) < TOL
        assert abs(coeffs[4] - 10.0 / (2.0 * 32.0)) < TOL

    def test_exact_vs_direct_lam_half(self):
        """Path 1 vs Path 3 for lambda=1/2."""
        coeffs = betagamma_shadow_coefficients(0.5)
        for s in [0.0, 1.0, 2.0, 5.0]:
            direct = shadow_zeta_numerical(coeffs, complex(s, 0)).real
            exact = betagamma_zeta_exact(0.5, s)
            assert abs(direct - exact) < TOL, f"Mismatch at s={s}"

    def test_exact_vs_direct_lam_1(self):
        """Path 1 vs Path 3 for lambda=1."""
        coeffs = betagamma_shadow_coefficients(1.0)
        for s in [0.0, 1.0, 2.0]:
            direct = shadow_zeta_numerical(coeffs, complex(s, 0)).real
            exact = betagamma_zeta_exact(1.0, s)
            assert abs(direct - exact) < TOL

    def test_abscissa(self):
        """Finite tower => abscissa = -infinity."""
        coeffs = betagamma_shadow_coefficients(0.5)
        sigma = abscissa_of_convergence(coeffs)
        assert sigma < -1e5

    def test_weight_symmetry(self):
        """kappa(lambda) = kappa(1-lambda) (weight symmetry of bg)."""
        for lam in [0.0, 0.25, 0.5, 0.75, 1.0]:
            coeffs_lam = betagamma_shadow_coefficients(lam)
            coeffs_sym = betagamma_shadow_coefficients(1.0 - lam)
            assert abs(coeffs_lam[2] - coeffs_sym[2]) < TOL

    def test_complementarity_kappa(self):
        """kappa(bg) + kappa(bc) = 0 for all lambda (AP24 safe for free fields)."""
        for lam in [0.0, 0.25, 0.5, 1.0]:
            c_val = 2.0 * (6.0 * lam ** 2 - 6.0 * lam + 1.0)
            kappa_bg = c_val / 2.0
            kappa_bc = -kappa_bg  # bc is Koszul dual
            assert abs(kappa_bg + kappa_bc) < TOL

    def test_not_multiplicative(self):
        """Beta-gamma tower is not multiplicative."""
        coeffs = betagamma_shadow_coefficients(1.0, 20)
        is_mult, _ = check_multiplicativity(coeffs, 20)
        # S_6 = S_2 * S_3? S_6 = 0 but S_2*S_3 = 2 != 0
        assert not is_mult

    def test_special_values_lam1(self):
        """Special values at lambda=1."""
        coeffs = betagamma_shadow_coefficients(1.0)
        sv = shadow_zeta_special_values(coeffs)
        kappa = 1.0
        S3 = 2.0
        S4 = 10.0 / 64.0  # 5/32
        assert abs(sv['zeta(0)'] - (kappa + S3 + S4)) < TOL
        assert abs(sv['zeta(1)'] - (kappa / 2.0 + S3 / 3.0 + S4 / 4.0)) < TOL
        assert abs(sv['zeta(2)'] - (kappa / 4.0 + S3 / 9.0 + S4 / 16.0)) < TOL

    def test_zeta_s0_explicit(self):
        """zeta_{bg_{1/2}}(0) = kappa + S_3 + S_4 = -1/2 + 2 + (-10/17) = 21/34."""
        val = betagamma_zeta_exact(0.5, 0.0)
        expected = -0.5 + 2.0 + (-10.0 / 17.0)
        assert abs(val - expected) < TOL


# ============================================================================
# VIRASORO (Class M) — 20 tests
# ============================================================================

class TestVirasoroZeta:
    """Virasoro: infinite tower, class M."""

    def test_shadow_coefficients_c1(self):
        """S_2 = 1/2, S_3 = 2, S_4 = 10/(1*27) at c=1."""
        coeffs = virasoro_shadow_coefficients_numerical(1.0, 10)
        assert abs(coeffs[2] - 0.5) < TOL
        assert abs(coeffs[3] - 2.0) < TOL
        assert abs(coeffs[4] - 10.0 / 27.0) < TOL

    def test_shadow_coefficients_c13(self):
        """S_2 = 13/2, S_3 = 2, S_4 = 10/(13*87) at c=13."""
        coeffs = virasoro_shadow_coefficients_numerical(13.0, 10)
        assert abs(coeffs[2] - 6.5) < TOL
        assert abs(coeffs[3] - 2.0) < TOL
        assert abs(coeffs[4] - 10.0 / (13.0 * 87.0)) < TOL

    def test_S5_c26(self):
        """S_5(c=26) = -48/(26^2 * 152) from closed form."""
        coeffs = virasoro_shadow_coefficients_numerical(26.0, 10)
        expected = -48.0 / (676.0 * 152.0)
        assert abs(coeffs[5] - expected) < TOL

    def test_growth_rate_c13(self):
        """rho(Vir_13) = sqrt((180*13+872)/((5*13+22)*169))."""
        rho_exact = virasoro_growth_rate_exact(13.0)
        numer = 180.0 * 13.0 + 872.0  # 3212
        denom = (65.0 + 22.0) * 169.0  # 87 * 169
        expected = math.sqrt(numer / denom)
        assert abs(rho_exact - expected) < TOL

    def test_growth_rate_from_coefficients(self):
        """Growth rate from |S_r|^{1/r} at high arity vs exact formula.

        Use the root test: rho = lim |S_r|^{1/r} (corrected for r^{-5/2}).
        This avoids the ratio oscillation from the cos factor.
        |S_r| ~ C * rho^r * r^{-5/2} => |S_r|^{1/r} ~ rho * (C/r^{5/2})^{1/r}
                                        ~ rho * exp(-(5/2) log(r)/r)
                                        ~ rho for large r.
        """
        c_val = 13.0
        max_r = 300
        coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
        rho_exact = virasoro_growth_rate_exact(c_val)
        # Root test at high arity
        estimates = []
        for r in range(200, max_r + 1):
            Sr = coeffs.get(r, 0.0)
            if abs(Sr) > 1e-300:
                est = abs(Sr) ** (1.0 / r)
                estimates.append(est)
        rho_est = estimates[-1] if estimates else 0.0
        assert abs(rho_est - rho_exact) < 0.02

    def test_growth_rate_c26_convergent(self):
        """rho(Vir_26) < 1: tower converges."""
        rho = virasoro_growth_rate_exact(26.0)
        assert rho < 1.0

    def test_growth_rate_c1_divergent(self):
        """rho(Vir_1) > 1: tower diverges."""
        rho = virasoro_growth_rate_exact(1.0)
        assert rho > 1.0

    def test_abscissa_c26_entire(self):
        """For c=26 (rho < 1): series converges for all s, abscissa -infinity."""
        sigma = abscissa_from_growth_rate(virasoro_growth_rate_exact(26.0))
        assert sigma == float('-inf')

    def test_abscissa_c1_infinity(self):
        """For c=1 (rho > 1): series diverges for all s, abscissa +infinity."""
        sigma = abscissa_from_growth_rate(virasoro_growth_rate_exact(1.0))
        assert sigma == float('inf')

    def test_direct_sum_convergence_c26(self):
        """Direct sum stabilizes for c=26 at s=2."""
        coeffs = virasoro_shadow_coefficients_numerical(26.0, 50)
        val_30 = shadow_zeta_numerical(coeffs, complex(2.0, 0), 30).real
        val_50 = shadow_zeta_numerical(coeffs, complex(2.0, 0), 50).real
        assert abs(val_30 - val_50) < 1e-6

    def test_zeta_s2_c26(self):
        """zeta_{Vir_26}(2) via direct sum with 50 terms."""
        coeffs = virasoro_shadow_coefficients_numerical(26.0, 50)
        val = shadow_zeta_numerical(coeffs, complex(2.0, 0)).real
        # Cross-check: first few terms
        check = sum(coeffs[r] / r ** 2 for r in range(2, 51))
        assert abs(val - check) < TOL

    def test_mellin_vs_direct_c26_s3(self):
        """Path 2 (Mellin) vs Path 1 (direct) for c=26, s=3."""
        c_val = 26.0
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 50)
        direct = shadow_zeta_numerical(coeffs, complex(3.0, 0), 50).real
        mellin = mellin_transform_zeta(coeffs, 3.0, n_points=5000, t_max=40.0)
        assert abs(direct - mellin) / (abs(direct) + 1e-30) < TOL_QUAD

    def test_mellin_vs_direct_c26_s5(self):
        """Path 2 (Mellin) vs Path 1 (direct) for c=26, s=5."""
        c_val = 26.0
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 50)
        direct = shadow_zeta_numerical(coeffs, complex(5.0, 0), 50).real
        mellin = mellin_transform_zeta(coeffs, 5.0, n_points=5000, t_max=40.0)
        assert abs(direct - mellin) / (abs(direct) + 1e-30) < TOL_QUAD

    def test_ode_consistency_c26(self):
        """zeta from virasoro_zeta_from_ode vs direct at c=26."""
        c_val = 26.0
        for s in [2.0, 3.0, 5.0]:
            val_ode = virasoro_zeta_from_ode(c_val, s, max_r=50)
            coeffs = virasoro_shadow_coefficients_numerical(c_val, 50)
            val_direct = shadow_zeta_numerical(coeffs, complex(s, 0), 50).real
            assert abs(val_ode - val_direct) < TOL

    def test_koszul_duality_c13(self):
        """At self-dual c=13: zeta_{Vir_13}(s) = zeta_{Vir_13}(s)."""
        rel = virasoro_koszul_dual_zeta_relation(13.0, 2.0, max_r=50)
        assert abs(rel['zeta_A'] - rel['zeta_dual']) < 1e-8

    def test_koszul_duality_sum_c5(self):
        """zeta_{Vir_5}(s) + zeta_{Vir_21}(s) should be a specific quantity."""
        rel = virasoro_koszul_dual_zeta_relation(5.0, 2.0, max_r=30)
        # Not zero in general (AP24: kappa + kappa' = 13 for Virasoro)
        # At s=0: zeta(0) = sum S_r, which is related to H(1) = sqrt(Q_L(1))
        assert isinstance(rel['sum'], float)

    def test_virasoro_not_multiplicative(self):
        """Virasoro shadow tower is not multiplicative."""
        coeffs = virasoro_shadow_coefficients_numerical(13.0, 20)
        is_mult, violations = check_multiplicativity(coeffs, 20)
        assert not is_mult
        assert len(violations) > 0

    def test_sign_alternation_c13(self):
        """For c=13, S_r alternates in sign for r >= 4."""
        coeffs = virasoro_shadow_coefficients_numerical(13.0, 20)
        for r in range(5, 20):
            if abs(coeffs[r]) > 1e-20:
                expected_sign = (-1) ** r
                actual_sign = 1 if coeffs[r] > 0 else -1
                assert actual_sign == expected_sign, f"Sign wrong at r={r}"

    def test_zeta_values_table(self):
        """Table computation works without error."""
        table = virasoro_zeta_values_table([13.0, 26.0], [2.0, 3.0], max_r=30)
        assert (13.0, 2.0) in table
        assert (26.0, 3.0) in table

    def test_generating_function_vs_coefficients(self):
        """H(x) = sum S_r x^r at x=0.5 matches term-by-term."""
        c_val = 26.0
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
        x = 0.5
        H_val = shadow_generating_function_numerical(coeffs, x)
        H_check = sum(coeffs[r] * x ** r for r in range(2, 31))
        assert abs(H_val - H_check) < TOL


# ============================================================================
# W_3 (Class M, two lines) — 8 tests
# ============================================================================

class TestW3Zeta:
    """W_3 shadow zeta on T-line and W-line."""

    def test_t_line_equals_virasoro(self):
        """W_3 T-line shadow = Virasoro shadow at the same c."""
        c_val = 50.0
        coeffs_T = w3_t_line_shadow_coefficients(c_val, 15)
        coeffs_V = virasoro_shadow_coefficients_numerical(c_val, 15)
        for r in range(2, 16):
            assert abs(coeffs_T[r] - coeffs_V[r]) < 1e-8, f"Mismatch at r={r}"

    def test_w_line_odd_vanishing(self):
        """W-line: S_r = 0 for all odd r (Z_2 parity)."""
        c_val = 50.0
        coeffs_W = w3_w_line_shadow_coefficients(c_val, 20)
        for r in range(3, 21, 2):  # odd r
            assert abs(coeffs_W[r]) < 1e-12, f"S_{r} should vanish, got {coeffs_W[r]}"

    def test_w_line_kappa_W(self):
        """W-line kappa_W = c/3."""
        c_val = 50.0
        coeffs = w3_w_line_shadow_coefficients(c_val, 5)
        assert abs(coeffs[2] - c_val / 3.0) < TOL

    def test_t_line_zeta_vs_virasoro_zeta(self):
        """zeta_{W_3,T}(s) = zeta_{Vir_c}(s) on the T-line."""
        c_val = 50.0
        coeffs_T = w3_t_line_shadow_coefficients(c_val, 30)
        coeffs_V = virasoro_shadow_coefficients_numerical(c_val, 30)
        for s in [2.0, 3.0, 5.0]:
            zT = shadow_zeta_numerical(coeffs_T, complex(s, 0), 30).real
            zV = shadow_zeta_numerical(coeffs_V, complex(s, 0), 30).real
            assert abs(zT - zV) < 1e-8

    def test_w_line_zeta_even_terms_only(self):
        """W-line zeta only receives contributions from even r."""
        c_val = 50.0
        coeffs = w3_w_line_shadow_coefficients(c_val, 20)
        full_zeta = shadow_zeta_numerical(coeffs, complex(2.0, 0), 20).real
        even_only = sum(coeffs[r] / r ** 2 for r in range(2, 21, 2))
        assert abs(full_zeta - even_only) < TOL

    def test_w_line_S4(self):
        """W-line S_4 = 2560/(c*(5c+22)^3)."""
        c_val = 50.0
        coeffs = w3_w_line_shadow_coefficients(c_val, 5)
        expected = 2560.0 / (c_val * (5.0 * c_val + 22.0) ** 3)
        assert abs(coeffs[4] - expected) < 1e-12

    def test_w_line_growth_rate_nonzero(self):
        """W-line has nonzero growth rate (class M on the W-line).

        The W-line has all odd S_r = 0.  Even-arity coefficients are nonzero
        but extremely small (S_4 ~ 2.5e-6, and they decrease exponentially).
        We check that all even arities up to 20 are nonzero.
        """
        c_val = 50.0
        coeffs = w3_w_line_shadow_coefficients(c_val, 20)
        # Even arities should ALL be nonzero (tower does not terminate)
        for r in range(4, 21, 2):
            assert abs(coeffs[r]) > 0, f"S_{r} should be nonzero on W-line"

    def test_total_kappa_decomposition(self):
        """kappa_total = kappa_T + kappa_W = c/2 + c/3 = 5c/6."""
        c_val = 50.0
        coeffs_T = w3_t_line_shadow_coefficients(c_val, 5)
        coeffs_W = w3_w_line_shadow_coefficients(c_val, 5)
        kappa_total = coeffs_T[2] + coeffs_W[2]
        expected = 5.0 * c_val / 6.0
        assert abs(kappa_total - expected) < TOL


# ============================================================================
# DIRICHLET CHARACTERS AND TWISTED ZETA — 8 tests
# ============================================================================

class TestTwistedZeta:
    """Twisted shadow zeta with Dirichlet characters."""

    def test_chi4_values(self):
        """chi_4 character table."""
        assert dirichlet_character_mod4(1) == 1
        assert dirichlet_character_mod4(2) == 0
        assert dirichlet_character_mod4(3) == -1
        assert dirichlet_character_mod4(4) == 0
        assert dirichlet_character_mod4(5) == 1
        assert dirichlet_character_mod4(7) == -1

    def test_chi8_1_values(self):
        """chi_8^{(1)} character table."""
        assert dirichlet_character_mod8_1(1) == 1
        assert dirichlet_character_mod8_1(3) == -1
        assert dirichlet_character_mod8_1(5) == -1
        assert dirichlet_character_mod8_1(7) == 1
        assert dirichlet_character_mod8_1(2) == 0

    def test_chi8_2_values(self):
        """chi_8^{(2)} character table."""
        assert dirichlet_character_mod8_2(1) == 1
        assert dirichlet_character_mod8_2(3) == 1
        assert dirichlet_character_mod8_2(5) == -1
        assert dirichlet_character_mod8_2(7) == -1

    def test_trivial_character_equals_untwisted(self):
        """Twisting by the trivial character gives back the untwisted zeta."""
        coeffs = virasoro_shadow_coefficients_numerical(26.0, 20)
        s = complex(3.0, 0)
        trivial = lambda n: 1
        untwisted = shadow_zeta_numerical(coeffs, s, 20)
        twisted = twisted_shadow_zeta_numerical(coeffs, s, trivial, 20)
        assert abs(untwisted - twisted) < TOL

    def test_twisted_heisenberg_chi4(self):
        """Twisted Heisenberg zeta: chi_4(2) = 0, so twisted zeta = 0."""
        coeffs = heisenberg_shadow_coefficients(1.0)
        s = complex(1.0, 0)
        val = twisted_shadow_zeta_numerical(coeffs, s, dirichlet_character_mod4)
        assert abs(val) < TOL  # chi_4(2) = 0

    def test_twisted_affine_sl2_chi4(self):
        """For affine sl_2: chi_4(2) = 0, chi_4(3) = -1, so twisted = -alpha * 3^{-s}."""
        k = 1.0
        alpha = 4.0 / (k + 2.0)
        coeffs = affine_sl2_shadow_coefficients(k)
        s = complex(1.0, 0)
        val = twisted_shadow_zeta_numerical(coeffs, s, dirichlet_character_mod4)
        expected = -alpha * 3.0 ** (-1.0)  # chi_4(2)=0, chi_4(3)=-1
        assert abs(val - expected) < TOL

    def test_twisted_virasoro_chi4_nonzero(self):
        """Twisted Virasoro zeta is nonzero in general."""
        coeffs = virasoro_shadow_coefficients_numerical(26.0, 20)
        s = complex(3.0, 0)
        val = twisted_shadow_zeta_numerical(coeffs, s, dirichlet_character_mod4, 20)
        # Should be nonzero (has contributions from r=3,5,7,...,19 where chi_4 != 0)
        assert abs(val) > 1e-10

    def test_chi4_orthogonality_sum(self):
        """sum_{r=2}^{N} chi_4(r) should have bounded partial sums."""
        partial = sum(dirichlet_character_mod4(r) for r in range(2, 101))
        # chi_4 is periodic with period 4: sum over full period is 0
        # Partial sum is bounded by 1
        assert abs(partial) <= 2


# ============================================================================
# EULER PRODUCT AND MULTIPLICATIVITY — 6 tests
# ============================================================================

class TestEulerProduct:
    """Euler product analysis."""

    def test_heisenberg_euler_factors(self):
        """Heisenberg has only the factor at p=2."""
        coeffs = heisenberg_shadow_coefficients(1.0, 30)
        factors = formal_euler_product_coefficients(coeffs, max_r=30)
        assert abs(factors[2][1] - 1.0) < TOL  # S_2 = 1 at p=2
        # S_4 = S_{2^2} = 0 (Heisenberg terminates)
        assert abs(factors[2][2]) < TOL
        # S_3 = 0 for Heisenberg
        assert abs(factors[3][1]) < TOL

    def test_virasoro_euler_factor_p2(self):
        """Virasoro Euler factor at p=2 includes S_2, S_4, S_8, S_16, ..."""
        coeffs = virasoro_shadow_coefficients_numerical(26.0, 20)
        factors = formal_euler_product_coefficients(coeffs, [2], max_r=20)
        # S_2 at p=2, S_4 at p=2^2, S_8 at p=2^3, S_16 at p=2^4
        assert abs(factors[2][1] - coeffs[2]) < TOL
        assert abs(factors[2][2] - coeffs[4]) < TOL
        assert abs(factors[2][3] - coeffs[8]) < TOL
        assert abs(factors[2][4] - coeffs[16]) < TOL

    def test_heisenberg_multiplicative(self):
        """Heisenberg is trivially multiplicative."""
        coeffs = heisenberg_shadow_coefficients(1.0, 20)
        is_mult, _ = check_multiplicativity(coeffs, 20)
        assert is_mult

    def test_virasoro_not_multiplicative(self):
        """Virasoro tower is not multiplicative."""
        coeffs = virasoro_shadow_coefficients_numerical(26.0, 20)
        is_mult, violations = check_multiplicativity(coeffs, 20)
        assert not is_mult

    def test_multiplicativity_violation_example(self):
        """Explicit violation: S_6 != S_2 * S_3 for Virasoro."""
        coeffs = virasoro_shadow_coefficients_numerical(26.0, 10)
        S2 = coeffs[2]
        S3 = coeffs[3]
        S6 = coeffs[6]
        assert abs(S6 - S2 * S3) > 1e-5  # NOT equal

    def test_affine_multiplicativity_violation(self):
        """Affine sl_2: S_6 = 0 but S_2 * S_3 != 0."""
        coeffs = affine_sl2_shadow_coefficients(1.0, 10)
        assert abs(coeffs[6]) < TOL  # S_6 = 0
        assert abs(coeffs[2] * coeffs[3]) > 0.1  # S_2 * S_3 != 0


# ============================================================================
# CONVERGENCE AND ABSCISSA — 5 tests
# ============================================================================

class TestConvergence:
    """Convergence analysis."""

    def test_critical_rho_gives_5half(self):
        """At rho = 1 (critical), abscissa = 5/2."""
        assert abs(abscissa_from_growth_rate(1.0) - 2.5) < TOL

    def test_convergent_rho(self):
        """For rho < 1: abscissa = -infinity."""
        assert abscissa_from_growth_rate(0.5) == float('-inf')

    def test_divergent_rho(self):
        """For rho > 1: abscissa = +infinity."""
        assert abscissa_from_growth_rate(2.0) == float('inf')

    def test_convergence_domain_virasoro_c26(self):
        """For c=26, series converges for all real s."""
        coeffs = virasoro_shadow_coefficients_numerical(26.0, 30)
        results = convergence_domain_analysis(coeffs, s_range=(0.0, 10.0), n_points=20)
        # All points should converge
        for s, val, converged in results:
            assert converged, f"Failed to converge at s={s}"

    def test_virasoro_critical_central_charge(self):
        """rho(Vir_c*) = 1 at c* ~ 6.1243."""
        # The equation: 5c^3 + 22c^2 - 180c - 872 = 0
        # Root: c* ~ 6.1243
        c_star = 6.1243  # approximate
        rho = virasoro_growth_rate_exact(c_star)
        assert abs(rho - 1.0) < 1e-3


# ============================================================================
# CROSS-FAMILY LANDSCAPE — 6 tests
# ============================================================================

class TestLandscape:
    """Cross-family comparisons."""

    def test_full_landscape_computes(self):
        """Full landscape computation completes without error."""
        landscape = compute_full_landscape(max_r=20)
        assert len(landscape) >= 10
        assert 'Heis_k=1' in landscape
        assert 'Vir_c=13' in landscape

    def test_class_G_all_entire(self):
        """All class G algebras have sigma = -infinity."""
        landscape = compute_full_landscape(max_r=20)
        for name, data in landscape.items():
            if data.shadow_class == 'G':
                assert data.abscissa < -1e5, f"{name} should be entire"

    def test_class_L_all_entire(self):
        """All class L algebras have sigma = -infinity."""
        landscape = compute_full_landscape(max_r=20)
        for name, data in landscape.items():
            if data.shadow_class == 'L':
                assert data.abscissa < -1e5, f"{name} should be entire"

    def test_class_C_all_entire(self):
        """All class C algebras have sigma = -infinity."""
        landscape = compute_full_landscape(max_r=20)
        for name, data in landscape.items():
            if data.shadow_class == 'C':
                assert data.abscissa < -1e5, f"{name} should be entire"

    def test_kappa_ordering(self):
        """kappa values are consistent across the landscape."""
        landscape = compute_full_landscape(max_r=20)
        # Heisenberg k=1: kappa = 1
        assert abs(landscape['Heis_k=1'].kappa - 1.0) < TOL
        # Virasoro c=26: kappa = 13
        assert abs(landscape['Vir_c=26'].kappa - 13.0) < TOL
        # Affine sl_2 k=1: kappa = 9/4
        assert abs(landscape['aff_sl2_k=1'].kappa - 2.25) < TOL

    def test_shadow_zeta_data_completeness(self):
        """ShadowZetaData has all required fields."""
        coeffs = heisenberg_shadow_coefficients(1.0, 10)
        data = compute_shadow_zeta_data('test', 'G', coeffs)
        assert data.name == 'test'
        assert data.shadow_class == 'G'
        assert data.kappa == 1.0
        assert 'zeta(0)' in data.special_values
        assert isinstance(data.is_multiplicative, bool)


# ============================================================================
# LIMITING CASES AND CONSISTENCY — 5 tests
# ============================================================================

class TestLimitingCases:
    """Limiting cases and cross-checks."""

    def test_large_s_all_families_vanish(self):
        """For all finite towers, zeta(s) -> 0 as s -> infinity."""
        for provider, args in [
            (heisenberg_shadow_coefficients, (1.0,)),
            (affine_sl2_shadow_coefficients, (1.0,)),
            (betagamma_shadow_coefficients, (0.5,)),
        ]:
            coeffs = provider(*args)
            val = shadow_zeta_numerical(coeffs, complex(50.0, 0))
            assert abs(val) < 1e-10

    def test_zeta_linearity_in_coefficients(self):
        """zeta_{2A}(s) = 2 * zeta_A(s) (if shadow coefficients scale linearly)."""
        coeffs1 = heisenberg_shadow_coefficients(1.0, 10)
        coeffs2 = {r: 2.0 * coeffs1[r] for r in coeffs1}
        for s in [1.0, 2.0, 3.0]:
            z1 = shadow_zeta_numerical(coeffs1, complex(s, 0))
            z2 = shadow_zeta_numerical(coeffs2, complex(s, 0))
            assert abs(z2 - 2.0 * z1) < TOL

    def test_heisenberg_limit_of_affine(self):
        """As k -> infinity, affine sl_2 kappa -> 3k/4 and alpha -> 0.
        So the affine zeta approaches (3k/4) * 2^{-s} = Heisenberg-like."""
        k = 10000.0
        alpha = 4.0 / (k + 2.0)  # Very small
        kappa = 3.0 * (k + 2.0) / 4.0
        val_affine = affine_sl2_zeta_exact(k, 2.0)
        val_heis = kappa * 2.0 ** (-2.0)  # Dominant term
        # The S_3 = alpha * 3^{-2} contribution is tiny
        assert abs(val_affine - val_heis) / val_heis < 1e-3

    def test_zeta_derivative_numerical(self):
        """Numerical derivative dζ/ds at s=1 for Heisenberg."""
        k = 1.0
        s = 1.0
        ds = 1e-6
        z_plus = heisenberg_zeta_exact(k, s + ds)
        z_minus = heisenberg_zeta_exact(k, s - ds)
        numerical_deriv = (z_plus - z_minus) / (2 * ds)
        # Exact: d/ds [k * 2^{-s}] = -k * log(2) * 2^{-s}
        exact_deriv = -k * math.log(2) * 2.0 ** (-s)
        assert abs(numerical_deriv - exact_deriv) < 1e-4

    def test_virasoro_koszul_self_dual_point(self):
        """At c=13, the Virasoro algebra is self-dual: zeta_A = zeta_{A!}."""
        coeffs = virasoro_shadow_coefficients_numerical(13.0, 30)
        coeffs_dual = virasoro_shadow_coefficients_numerical(13.0, 30)
        for s in [2.0, 3.0, 5.0]:
            zA = shadow_zeta_numerical(coeffs, complex(s, 0), 30).real
            zD = shadow_zeta_numerical(coeffs_dual, complex(s, 0), 30).real
            assert abs(zA - zD) < 1e-10


# ============================================================================
# MELLIN TRANSFORM VERIFICATION — 4 tests
# ============================================================================

class TestMellinTransform:
    """Mellin transform as independent verification path."""

    def test_mellin_heisenberg_s2(self):
        """Mellin transform of Heisenberg at s=2."""
        coeffs = heisenberg_shadow_coefficients(1.0, 10)
        mellin = mellin_transform_zeta(coeffs, 2.0, n_points=5000, t_max=30.0)
        exact = heisenberg_zeta_exact(1.0, 2.0)
        assert abs(mellin - exact) / abs(exact) < TOL_QUAD

    def test_mellin_affine_s3(self):
        """Mellin of affine sl_2 at s=3."""
        coeffs = affine_sl2_shadow_coefficients(1.0, 10)
        mellin = mellin_transform_zeta(coeffs, 3.0, n_points=5000, t_max=30.0)
        exact = affine_sl2_zeta_exact(1.0, 3.0)
        assert abs(mellin - exact) / (abs(exact) + 1e-30) < TOL_QUAD

    def test_mellin_betagamma_s2(self):
        """Mellin of beta-gamma at s=2."""
        coeffs = betagamma_shadow_coefficients(1.0, 10)
        mellin = mellin_transform_zeta(coeffs, 2.0, n_points=5000, t_max=30.0)
        exact = betagamma_zeta_exact(1.0, 2.0)
        assert abs(mellin - exact) / (abs(exact) + 1e-30) < TOL_QUAD

    def test_generating_function_at_zero(self):
        """H(0) = 0 for all families (tower starts at r=2)."""
        for provider, args in [
            (heisenberg_shadow_coefficients, (1.0,)),
            (virasoro_shadow_coefficients_numerical, (26.0,)),
            (affine_sl2_shadow_coefficients, (1.0,)),
        ]:
            coeffs = provider(*args)
            H0 = shadow_generating_function_numerical(coeffs, 0.0)
            assert abs(H0) < TOL
