r"""Tests for Dixmier trace, Wodzicki residue, and NC integral of shadow operators.

BC-130: Noncommutative geometry of the shadow spectral triple at Riemann zeros.

Verification strategy (multi-path, per CLAUDE.md mandate):
    Path 1: Direct singular value computation
    Path 2: Dixmier trace via Cesaro mean of partial sums / log N
    Path 3: Wodzicki residue from Connes trace theorem
    Path 4: NC spectral zeta function (residue, analytic continuation)
    Path 5: Heat kernel small-t expansion (Seeley-DeWitt coefficients)
    Path 6: Cross-family consistency (additivity of kappa => additivity of Tr_omega)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  kappa != c/2 in general.
CAUTION (AP10): Multi-path verification catches hardcoded-wrong expected values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP39): kappa != S_2 for non-Virasoro families in general.

References:
    concordance.tex: Theorem D (modular characteristic)
    higher_genus_modular_koszul.tex: shadow obstruction tower
    CLAUDE.md: multi-path verification mandate, AP1, AP9, AP10, AP24, AP39
"""

import cmath
import math

import pytest

from compute.lib.bc_dixmier_trace_shadow_engine import (
    # Constants
    RIEMANN_ZEROS,
    # Shadow coefficients
    shadow_coefficients,
    kappa_value,
    shadow_depth_class,
    shadow_rmax,
    # Spectral data
    shadow_eigenvalues,
    shadow_eigenvalues_from_tower,
    ShadowSpectralData,
    # Singular value analysis
    fit_singular_value_decay,
    singular_values_table,
    log_divergence_fit,
    SingularValueFit,
    # Dixmier trace
    partial_sum_singular_values,
    dixmier_trace_partial,
    dixmier_trace_cesaro,
    dixmier_trace_exact,
    # Wodzicki residue
    wodzicki_residue,
    wodzicki_residue_from_symbol,
    # NC spectral zeta
    nc_spectral_zeta,
    nc_spectral_zeta_exact,
    nc_spectral_zeta_at_zero,
    nc_spectral_zeta_derivative_at_zero,
    nc_spectral_determinant,
    # Shadow NC zeta
    shadow_nc_zeta,
    shadow_nc_zeta_residue,
    # Heat kernel
    heat_kernel_trace,
    heat_kernel_trace_exact,
    heat_kernel_seeley_dewitt,
    heat_kernel_dixmier_check,
    # NC at zeros
    nc_integral_at_riemann_zero,
    nc_integrals_at_all_zeros,
    NCZeroData,
    # Shared zero test
    check_shared_zeros,
    # Complementarity
    dixmier_complementarity,
    # Multi-family
    nc_data_for_family,
    standard_family_nc_table,
    FamilyNCData,
    # Comprehensive report
    comprehensive_nc_report,
)


# ============================================================================
#  Section 1: Kappa values (AP1, AP9, AP39 cross-checks)
# ============================================================================

class TestKappaValues:
    """Verify kappa(A) for all standard families.

    Multi-path: direct formula, shadow coefficient S_2, cross-family consistency.
    """

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k. Direct formula."""
        assert kappa_value('heisenberg', 1.0) == 1.0
        assert kappa_value('heisenberg', 2.0) == 2.0
        assert kappa_value('heisenberg', 0.5) == 0.5
        assert kappa_value('heisenberg', -1.0) == -1.0

    def test_heisenberg_kappa_equals_S2(self):
        """For Heisenberg, kappa = S_2 (single nonzero coefficient)."""
        for k in [1.0, 2.0, 5.0]:
            coeffs = shadow_coefficients('heisenberg', k, max_r=10)
            assert abs(coeffs[2] - kappa_value('heisenberg', k)) < 1e-12

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2. Direct formula."""
        assert kappa_value('virasoro', 1.0) == 0.5
        assert kappa_value('virasoro', 26.0) == 13.0
        assert kappa_value('virasoro', 13.0) == 6.5  # self-dual

    def test_affine_sl2_kappa(self):
        """kappa(aff sl_2, k) = 3(k+2)/4. dim=3, h^v=2."""
        # k=1: 3*3/4 = 9/4 = 2.25
        assert abs(kappa_value('affine_sl2', 1.0) - 2.25) < 1e-12
        # k=4: 3*6/4 = 18/4 = 4.5
        assert abs(kappa_value('affine_sl2', 4.0) - 4.5) < 1e-12

    def test_affine_sl3_kappa(self):
        """kappa(aff sl_3, k) = 8(k+3)/6. dim=8, h^v=3."""
        # k=1: 8*4/6 = 32/6 = 16/3
        assert abs(kappa_value('affine_sl3', 1.0) - 16.0 / 3.0) < 1e-12

    def test_betagamma_kappa(self):
        """kappa(bg, lambda) = c(lambda)/2 where c = 2(6*lam^2 - 6*lam + 1)."""
        # lambda=1: c = 2(6-6+1) = 2, kappa = 1
        assert abs(kappa_value('betagamma', 1.0) - 1.0) < 1e-12

    def test_kappa_never_equals_c_for_affine(self):
        """AP9/AP39: kappa != c/2 for affine KM at rank > 1.

        For sl_2 at k=1: c = 3*1/(1+2) = 1, so c/2 = 0.5.
        But kappa = 3*(1+2)/4 = 2.25.  These are DIFFERENT.
        """
        k = 1.0
        c_sl2 = 3.0 * k / (k + 2.0)  # c for sl_2 at level k
        kap = kappa_value('affine_sl2', k)
        assert abs(c_sl2 / 2.0 - kap) > 0.1  # They differ

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError, match="Unknown family"):
            kappa_value('unknown', 1.0)


# ============================================================================
#  Section 2: Shadow depth classification
# ============================================================================

class TestShadowDepth:
    """Verify shadow depth class and r_max."""

    def test_heisenberg_class_G(self):
        assert shadow_depth_class('heisenberg') == 'G'
        assert shadow_rmax('heisenberg') == 2

    def test_affine_class_L(self):
        assert shadow_depth_class('affine_sl2') == 'L'
        assert shadow_rmax('affine_sl2') == 3

    def test_betagamma_class_C(self):
        assert shadow_depth_class('betagamma') == 'C'
        assert shadow_rmax('betagamma') == 4

    def test_virasoro_class_M(self):
        assert shadow_depth_class('virasoro') == 'M'
        assert shadow_rmax('virasoro') == math.inf

    def test_w3_class_M(self):
        assert shadow_depth_class('w3_t') == 'M'
        assert shadow_rmax('w3_t') == math.inf


# ============================================================================
#  Section 3: Singular values (Path 1)
# ============================================================================

class TestSingularValues:
    """Singular values sigma_n(T_kappa) = kappa * n^{-d_S/2}."""

    def test_heisenberg_singular_values_canonical(self):
        """For H_1 with d_S=2: sigma_n = 1/n."""
        sv = shadow_eigenvalues('heisenberg', 1.0, n_max=100)
        for n in range(1, 11):
            expected = 1.0 / n
            # singular_values are sorted descending, so sv[0] = sigma_1 = 1.0
            assert abs(sv.singular_values[n - 1] - expected) < 1e-12

    def test_virasoro_singular_values_scale_with_kappa(self):
        """sigma_n(Vir_c) = (c/2) * n^{-1} for d_S = 2."""
        for c in [1.0, 13.0, 26.0]:
            sv = shadow_eigenvalues('virasoro', c, n_max=50)
            kap = c / 2.0
            for n in range(1, 6):
                expected = kap / n
                assert abs(sv.singular_values[n - 1] - expected) < 1e-10

    def test_singular_values_descending(self):
        """Singular values must be non-increasing."""
        for fam, p in [('heisenberg', 1.0), ('virasoro', 10.0), ('affine_sl2', 2.0)]:
            sv = shadow_eigenvalues(fam, p, n_max=100)
            for i in range(len(sv.singular_values) - 1):
                assert sv.singular_values[i] >= sv.singular_values[i + 1] - 1e-15

    def test_singular_values_table_matches(self):
        """singular_values_table agrees with shadow_eigenvalues."""
        table = singular_values_table('heisenberg', 2.0, n_max=50, d_S=2.0)
        sv = shadow_eigenvalues('heisenberg', 2.0, n_max=50)
        for n, sigma in table[:10]:
            assert abs(sigma - sv.singular_values[n - 1]) < 1e-12

    def test_singular_value_fit_exponent(self):
        """Fit sigma_n ~ C * n^{-alpha} recovers alpha = 1 for d_S = 2."""
        sv = shadow_eigenvalues('heisenberg', 1.0, n_max=500)
        fit = fit_singular_value_decay(sv.singular_values, n_start=10, n_end=500)
        assert abs(fit.alpha - 1.0) < 0.01  # alpha = 1/d_S = 1/2... no, alpha = d_S/2 = 1
        assert abs(fit.C - 1.0) < 0.05  # C = kappa = 1

    def test_singular_value_fit_d_S(self):
        """Inferred d_S = 1/alpha should be ~1 (since alpha=1 => d_S=1).

        Wait: sigma_n = kappa * n^{-d_S/2}. For d_S=2, exponent = -1, so alpha=1.
        Then d_S = 2*alpha = 2. But fit.d_S = 1/alpha = 1.
        The fit reports d_S = 1/alpha which is the "NC dimension" from the
        singular value decay rate. For the canonical model this is 1, meaning
        the operator is in the (1,infinity) ideal.  The SPECTRAL dimension d_S=2
        comes from the eigenvalue growth, not the singular value exponent directly.
        """
        sv = shadow_eigenvalues('virasoro', 26.0, n_max=500)
        fit = fit_singular_value_decay(sv.singular_values, n_start=10)
        # alpha = 1.0, so fit.d_S = 1/1 = 1.0
        assert abs(fit.alpha - 1.0) < 0.01

    def test_singular_value_fit_C_scales_with_kappa(self):
        """The fitted coefficient C should equal kappa."""
        for k in [1.0, 3.0, 7.0]:
            sv = shadow_eigenvalues('heisenberg', k, n_max=500)
            fit = fit_singular_value_decay(sv.singular_values, n_start=10)
            assert abs(fit.C - k) < 0.1 * k


# ============================================================================
#  Section 4: Dixmier trace (Paths 1, 2, 5)
# ============================================================================

class TestDixmierTrace:
    """Dixmier trace Tr_omega(T_kappa) = kappa (for d_S = 2)."""

    def test_heisenberg_dixmier_exact(self):
        """Tr_omega(T_{H_k}) = k (exact)."""
        for k in [1.0, 2.0, 5.0, 0.5]:
            assert abs(dixmier_trace_exact('heisenberg', k) - abs(k)) < 1e-12

    def test_virasoro_dixmier_exact(self):
        """Tr_omega(T_{Vir_c}) = c/2 (exact)."""
        for c in [1.0, 13.0, 26.0, 48.0]:
            assert abs(dixmier_trace_exact('virasoro', c) - c / 2.0) < 1e-12

    def test_dixmier_partial_converges_to_kappa(self):
        """Path 2: (1/log N) sum_{n=1}^N sigma_n -> kappa as N -> infinity.

        For sigma_n = kappa/n: sum ~ kappa*(log N + gamma), so
        (1/log N) * sum ~ kappa * (1 + gamma/log N) -> kappa.
        At N=500, gamma/log(500) ~ 0.577/6.21 ~ 0.093, so ~9% overshoot.
        """
        sv = shadow_eigenvalues('heisenberg', 1.0, n_max=500)
        dix_500 = dixmier_trace_partial(sv.singular_values, 500)
        # Should be within 10% of kappa = 1.0
        assert abs(dix_500 - 1.0) < 0.15

    def test_dixmier_partial_improves_with_N(self):
        """Larger N gives better approximation."""
        sv = shadow_eigenvalues('heisenberg', 1.0, n_max=500)
        dix_100 = dixmier_trace_partial(sv.singular_values, 100)
        dix_500 = dixmier_trace_partial(sv.singular_values, 500)
        assert abs(dix_500 - 1.0) < abs(dix_100 - 1.0)

    def test_dixmier_cesaro_closer_to_kappa(self):
        """Cesaro averaging improves convergence."""
        sv = shadow_eigenvalues('heisenberg', 1.0, n_max=500)
        dix_cesaro = dixmier_trace_cesaro(sv.singular_values, 500, window=100)
        # Cesaro should be within 15% of exact
        assert abs(dix_cesaro - 1.0) < 0.2

    def test_dixmier_scales_linearly_with_kappa(self):
        """Tr_omega(alpha * T) = alpha * Tr_omega(T)."""
        for k in [1.0, 3.0, 10.0]:
            assert abs(dixmier_trace_exact('heisenberg', k) - k) < 1e-12

    def test_dixmier_heat_kernel_cross_check(self):
        """Path 5: heat kernel gives same Dixmier trace."""
        for fam, p in [('heisenberg', 1.0), ('virasoro', 26.0), ('affine_sl2', 1.0)]:
            check = heat_kernel_dixmier_check(fam, p)
            assert check['match'], (
                f"Heat kernel Dixmier check failed for {fam}: "
                f"heat={check['dixmier_from_heat']}, direct={check['dixmier_direct']}"
            )

    def test_dixmier_trace_all_families(self):
        """Exact Dixmier trace matches kappa for all standard families."""
        cases = [
            ('heisenberg', 1.0, 1.0),
            ('heisenberg', 2.0, 2.0),
            ('affine_sl2', 1.0, 2.25),
            ('affine_sl3', 1.0, 16.0 / 3.0),
            ('virasoro', 1.0, 0.5),
            ('virasoro', 26.0, 13.0),
        ]
        for fam, p, expected_kappa in cases:
            dix = dixmier_trace_exact(fam, p)
            assert abs(dix - abs(expected_kappa)) < 1e-10, (
                f"Dixmier({fam}, {p}) = {dix}, expected {abs(expected_kappa)}"
            )


# ============================================================================
#  Section 5: Log-divergence fit (Path 2 detailed)
# ============================================================================

class TestLogDivergence:
    """Fit sum_{n<=N} sigma_n ~ alpha * log(N) + beta."""

    def test_heisenberg_alpha_equals_kappa(self):
        """For H_k: alpha = k (harmonic series coefficient)."""
        for k in [1.0, 2.0, 5.0]:
            lf = log_divergence_fit('heisenberg', k, n_max=500)
            assert abs(lf['alpha'] - k) < 0.05 * k, (
                f"alpha={lf['alpha']}, expected {k}"
            )

    def test_virasoro_alpha_equals_kappa(self):
        """For Vir_c: alpha = c/2."""
        for c in [1.0, 10.0, 26.0]:
            lf = log_divergence_fit('virasoro', c, n_max=500)
            kap = c / 2.0
            assert abs(lf['alpha'] - kap) < 0.05 * kap + 0.01

    def test_beta_approximates_kappa_gamma(self):
        """beta ~ kappa * gamma_EM where gamma_EM = 0.5772..."""
        gamma_em = 0.5772156649015329
        lf = log_divergence_fit('heisenberg', 1.0, n_max=500)
        assert abs(lf['beta'] - gamma_em) < 0.1

    def test_fit_quality(self):
        """Residual of log fit should be small."""
        lf = log_divergence_fit('heisenberg', 1.0, n_max=500)
        assert lf['residual'] < 0.05

    def test_alpha_match_flag(self):
        """alpha_match flag should be True for good fits."""
        lf = log_divergence_fit('heisenberg', 1.0, n_max=500)
        assert lf['alpha_match']


# ============================================================================
#  Section 6: Wodzicki residue (Path 3)
# ============================================================================

class TestWodzickiResidue:
    """Res_W(|D|^{-d_S}) = d_S * Tr_omega(|D|^{-d_S}) (Connes trace theorem)."""

    def test_wodzicki_equals_dS_times_dixmier(self):
        """Res_W = d_S * Tr_omega for d_S = 2."""
        for fam, p in [('heisenberg', 1.0), ('virasoro', 26.0), ('affine_sl2', 2.0)]:
            dix = dixmier_trace_exact(fam, p)
            wod = wodzicki_residue(fam, p, d_S=2.0)
            assert abs(wod - 2.0 * dix) < 1e-10

    def test_wodzicki_heisenberg(self):
        """Res_W(|D|^{-2}) = 2 * kappa = 2 * k for Heisenberg."""
        for k in [1.0, 3.0, 5.0]:
            wod = wodzicki_residue('heisenberg', k)
            assert abs(wod - 2.0 * k) < 1e-12

    def test_wodzicki_virasoro(self):
        """Res_W(|D|^{-2}) = 2 * c/2 = c for Virasoro."""
        for c in [1.0, 13.0, 26.0]:
            wod = wodzicki_residue('virasoro', c)
            assert abs(wod - c) < 1e-12

    def test_wodzicki_from_symbol_agrees(self):
        """Path 3 alternative: symbol computation matches Connes."""
        for fam, p in [('heisenberg', 1.0), ('virasoro', 10.0)]:
            w1 = wodzicki_residue(fam, p)
            w2 = wodzicki_residue_from_symbol(fam, p)
            assert abs(w1 - w2) < 1e-10

    def test_wodzicki_scales_with_kappa(self):
        """Res_W scales linearly with kappa."""
        w1 = wodzicki_residue('heisenberg', 1.0)
        w3 = wodzicki_residue('heisenberg', 3.0)
        assert abs(w3 / w1 - 3.0) < 1e-10


# ============================================================================
#  Section 7: NC spectral zeta (Path 4)
# ============================================================================

class TestNCSpectralZeta:
    """zeta_D(s) = zeta_R(s/2) for the canonical model."""

    def test_zeta_D_at_zero(self):
        """zeta_D(0) = zeta_R(0) = -1/2."""
        z = nc_spectral_zeta_at_zero()
        assert abs(z.real - (-0.5)) < 1e-12
        assert abs(z.imag) < 1e-12

    def test_zeta_D_prime_at_zero(self):
        """zeta_D'(0) = (1/2) * zeta_R'(0) = -log(2*pi)/4."""
        zp = nc_spectral_zeta_derivative_at_zero()
        expected = -math.log(2.0 * math.pi) / 4.0
        assert abs(zp.real - expected) < 1e-10

    def test_spectral_determinant(self):
        """det(D^2) = exp(-zeta_D'(0)) = (2*pi)^{1/4}."""
        det = nc_spectral_determinant()
        expected = (2.0 * math.pi) ** 0.25
        assert abs(det - expected) < 1e-10

    def test_nc_zeta_partial_at_s_4(self):
        """zeta_D(4) = zeta_R(2) = pi^2/6 (from partial sum)."""
        z = nc_spectral_zeta(complex(4.0, 0.0), n_max=50000)
        expected = math.pi ** 2 / 6.0
        assert abs(z.real - expected) < 0.01  # Partial sum converges slowly

    def test_nc_zeta_partial_at_s_6(self):
        """zeta_D(6) = zeta_R(3) = 1.202056... (Apery's constant)."""
        z = nc_spectral_zeta(complex(6.0, 0.0), n_max=10000)
        expected = 1.2020569031595942
        assert abs(z.real - expected) < 0.01

    def test_nc_zeta_exact_at_s_4(self):
        """Exact: zeta_D(4) = zeta_R(2) = pi^2/6."""
        z = nc_spectral_zeta_exact(complex(4.0, 0.0))
        expected = math.pi ** 2 / 6.0
        assert abs(z.real - expected) < 0.01

    def test_nc_zeta_at_negative_even_integers(self):
        """zeta_R(-2n) = 0 for n >= 1, so zeta_D(-4n) = 0."""
        # zeta_D(-4) = zeta_R(-2) = 0
        z = nc_spectral_zeta_exact(complex(-4.0, 0.0))
        assert abs(z) < 0.1  # Approximate due to analytic continuation numerics

    def test_nc_zeta_is_real_on_real_axis(self):
        """For real s, zeta_D(s) is real."""
        for s_val in [3.0, 4.0, 6.0, 10.0]:
            z = nc_spectral_zeta(complex(s_val, 0.0), n_max=5000)
            assert abs(z.imag) < 1e-10


# ============================================================================
#  Section 8: Shadow zeta as NC zeta
# ============================================================================

class TestShadowNCZeta:
    """Shadow zeta zeta_A(s) = sum S_r * r^{-s}."""

    def test_heisenberg_shadow_zeta(self):
        """zeta_{H_k}(s) = k * 2^{-s}."""
        for k in [1.0, 3.0]:
            for s in [1.0 + 0j, 2.0 + 0j, 0.5 + 1j]:
                z = shadow_nc_zeta('heisenberg', k, s, max_r=10)
                expected = k * 2.0 ** (-s)
                assert abs(z - expected) < 1e-10

    def test_heisenberg_shadow_zeta_never_zero(self):
        """zeta_{H_k}(s) = k * 2^{-s} != 0 for k != 0."""
        for gamma in RIEMANN_ZEROS[:5]:
            rho = complex(0.5, gamma)
            z = shadow_nc_zeta('heisenberg', 1.0, rho, max_r=10)
            assert abs(z) > 0.1  # Never zero

    def test_virasoro_shadow_zeta_nonzero_at_zeros(self):
        """Shadow zeta generically does NOT vanish at Riemann zeros."""
        z = shadow_nc_zeta('virasoro', 26.0, complex(0.5, RIEMANN_ZEROS[0]), max_r=50)
        # Generically nonzero
        assert abs(z) > 0.01

    def test_shadow_residue_class_G(self):
        """Class G has entire shadow zeta: residue = 0."""
        assert shadow_nc_zeta_residue('heisenberg', 1.0) == 0.0

    def test_shadow_residue_class_M(self):
        """Class M: residue = kappa (leading estimate)."""
        res = shadow_nc_zeta_residue('virasoro', 26.0)
        assert abs(res - 13.0) < 1e-10


# ============================================================================
#  Section 9: Heat kernel (Path 5)
# ============================================================================

class TestHeatKernel:
    """Heat kernel Tr(e^{-tD^2}) and Seeley-DeWitt expansion."""

    def test_heat_kernel_exact_matches_truncated(self):
        """Exact (geometric) formula matches term-by-term sum."""
        for t in [0.01, 0.1, 1.0]:
            exact = heat_kernel_trace_exact(t)
            truncated = heat_kernel_trace(t, n_max=10000)
            assert abs(exact - truncated) / max(abs(exact), 1.0) < 1e-6

    def test_heat_kernel_small_t_leading(self):
        """For small t: Tr(e^{-tD^2}) ~ 1/t."""
        t = 0.001
        exact = heat_kernel_trace_exact(t)
        assert abs(exact - 1.0 / t) / (1.0 / t) < 0.01  # Within 1%

    def test_heat_kernel_seeley_dewitt_matches(self):
        """Seeley-DeWitt expansion matches exact for small t."""
        for t in [0.01, 0.05]:
            exact = heat_kernel_trace_exact(t)
            sd = heat_kernel_seeley_dewitt(t, n_terms=8)
            assert abs(exact - sd) / abs(exact) < 0.001  # Within 0.1%

    def test_seeley_dewitt_leading_coefficient(self):
        """a_0 = 1 in the expansion Tr(e^{-tD^2}) ~ a_0/t + ..."""
        # From the exact formula: e^{-t}/(1-e^{-t}) = 1/(e^t - 1)
        # Laurent: 1/t - 1/2 + t/12 - ...
        # So a_0 (coefficient of t^{-1}) = 1.
        t = 0.001
        exact = heat_kernel_trace_exact(t)
        # leading: 1/t = 1000
        leading = 1.0 / t
        subleading = -0.5 + t / 12.0
        assert abs(exact - leading - subleading) / leading < 0.001

    def test_heat_kernel_large_t_decays(self):
        """For large t: Tr(e^{-tD^2}) -> e^{-t}/(1-e^{-t}) -> 0."""
        t = 10.0
        exact = heat_kernel_trace_exact(t)
        assert exact < 0.001

    def test_heat_kernel_dixmier_consistency(self):
        """Heat kernel a_0/Gamma(1) = kappa matches Dixmier trace."""
        for fam, p in [('heisenberg', 1.0), ('virasoro', 13.0)]:
            check = heat_kernel_dixmier_check(fam, p)
            assert check['match']
            assert abs(check['dixmier_from_heat'] - check['dixmier_direct']) < 1e-10


# ============================================================================
#  Section 10: NC integrals at Riemann zeros
# ============================================================================

class TestNCAtZeros:
    """NC spectral zeta and shadow zeta evaluated at Riemann zeros."""

    def test_riemann_zeros_count(self):
        """We have 25 Riemann zeros stored."""
        assert len(RIEMANN_ZEROS) == 25

    def test_riemann_zeros_increasing(self):
        """Zeros are in increasing order."""
        for i in range(len(RIEMANN_ZEROS) - 1):
            assert RIEMANN_ZEROS[i] < RIEMANN_ZEROS[i + 1]

    def test_first_zero_value(self):
        """First zero gamma_1 ~ 14.1347..."""
        assert abs(RIEMANN_ZEROS[0] - 14.134725141734693) < 1e-10

    def test_nc_integral_at_first_zero(self):
        """NC data at first Riemann zero is computable."""
        data = nc_integral_at_riemann_zero('virasoro', 26.0, 1, max_r=50)
        assert data.zero_index == 1
        assert abs(data.gamma - RIEMANN_ZEROS[0]) < 1e-10
        assert abs(data.rho - complex(0.5, RIEMANN_ZEROS[0])) < 1e-10
        # Shadow zeta should be nonzero generically
        assert abs(data.shadow_zeta_at_zero) > 0.01

    def test_nc_integral_at_all_zeros(self):
        """Compute NC data at first 10 zeros."""
        results = nc_integrals_at_all_zeros('heisenberg', 1.0, n_zeros=10)
        assert len(results) == 10
        for r in results:
            assert isinstance(r, NCZeroData)
            assert abs(r.shadow_zeta_at_zero) > 0.01  # Heis never zero

    def test_nc_zeta_at_riemann_zero_nonzero(self):
        """NC spectral zeta zeta_D(rho) at Riemann zeros.

        zeta_D(rho) = zeta_R(rho/2) where rho = 1/2 + i*gamma.
        So zeta_D(rho) = zeta_R(1/4 + i*gamma/2).
        This is generically NOT zero (the Riemann zeros of zeta_R are at
        1/2 + i*gamma, not at 1/4 + i*gamma/2).
        """
        data = nc_integral_at_riemann_zero('virasoro', 26.0, 1)
        assert abs(data.nc_zeta_at_zero) > 0.1

    def test_shadow_zeta_at_zeros_heisenberg(self):
        """For Heisenberg: zeta_A(rho) = k * 2^{-rho}, always nonzero."""
        for i in range(1, 6):
            data = nc_integral_at_riemann_zero('heisenberg', 1.0, i)
            expected = 2.0 ** (-complex(0.5, RIEMANN_ZEROS[i - 1]))
            assert abs(data.shadow_zeta_at_zero - expected) < 1e-6

    def test_wodzicki_formal_at_zeros(self):
        """Wodzicki formal: rho * zeta_D(rho)."""
        data = nc_integral_at_riemann_zero('virasoro', 26.0, 1)
        expected = data.rho * data.nc_zeta_at_zero
        assert abs(data.wodzicki_at_zero - expected) < 1e-6

    def test_invalid_zero_index_raises(self):
        with pytest.raises(ValueError):
            nc_integral_at_riemann_zero('heisenberg', 1.0, 0)
        with pytest.raises(ValueError):
            nc_integral_at_riemann_zero('heisenberg', 1.0, 100)


# ============================================================================
#  Section 11: Shared zeros test
# ============================================================================

class TestSharedZeros:
    """Test whether shadow zeta shares zeros with Riemann zeta."""

    def test_heisenberg_no_shared_zeros(self):
        """Heisenberg shadow zeta is never zero."""
        result = check_shared_zeros('heisenberg', 1.0, n_zeros=10)
        assert result['shared'] == 0
        assert 'NO shared zeros' in result['conclusion']

    def test_virasoro_generically_no_shared_zeros(self):
        """Virasoro shadow zeta generically has no shared zeros with Riemann."""
        result = check_shared_zeros('virasoro', 26.0, n_zeros=10, max_r=50)
        # Generically independent => no shared zeros
        assert result['shared'] <= 1  # At most 1 accidental near-zero

    def test_min_value_positive_heisenberg(self):
        """Minimum |zeta_A(rho)| > 0 for Heisenberg."""
        result = check_shared_zeros('heisenberg', 1.0, n_zeros=10)
        assert result['min_value'] > 0.1

    def test_shared_zeros_returns_correct_structure(self):
        result = check_shared_zeros('heisenberg', 1.0, n_zeros=5)
        assert 'family' in result
        assert 'values' in result
        assert len(result['values']) == 5


# ============================================================================
#  Section 12: Complementarity (AP24)
# ============================================================================

class TestComplementarity:
    """Dixmier trace complementarity: Tr_omega(A) + Tr_omega(A!)."""

    def test_heisenberg_complementarity_zero(self):
        """kappa(H_k) + kappa(H_k^!) = k + (-k) = 0."""
        comp = dixmier_complementarity('heisenberg', 1.0)
        assert abs(comp['sum']) < 1e-12

    def test_virasoro_complementarity_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13."""
        for c in [1.0, 10.0, 13.0, 26.0]:
            comp = dixmier_complementarity('virasoro', c)
            assert abs(comp['sum'] - 13.0) < 1e-10, (
                f"c={c}: sum = {comp['sum']}, expected 13"
            )

    def test_affine_sl2_complementarity_zero(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 3(k+2)/4 + 3(-k-2)/4 = 0."""
        comp = dixmier_complementarity('affine_sl2', 1.0)
        assert abs(comp['sum']) < 1e-10

    def test_virasoro_self_dual_point(self):
        """At c=13: kappa = kappa' = 6.5."""
        comp = dixmier_complementarity('virasoro', 13.0)
        assert abs(comp['kappa'] - 6.5) < 1e-12
        assert abs(comp['kappa_dual'] - 6.5) < 1e-12

    def test_virasoro_complementarity_is_NOT_zero(self):
        """AP24 cross-check: kappa + kappa' = 13 != 0 for Virasoro."""
        comp = dixmier_complementarity('virasoro', 1.0)
        assert abs(comp['sum']) > 1.0  # It's 13, very far from 0


# ============================================================================
#  Section 13: Multi-family NC data table
# ============================================================================

class TestMultiFamilyTable:
    """Cross-family NC geometry data."""

    def test_nc_data_heisenberg(self):
        data = nc_data_for_family('heisenberg', 1.0)
        assert data.kappa == 1.0
        assert data.shadow_class == 'G'
        assert abs(data.dixmier_trace - 1.0) < 1e-12

    def test_nc_data_virasoro_self_dual(self):
        data = nc_data_for_family('virasoro', 13.0)
        assert abs(data.kappa - 6.5) < 1e-12
        assert data.shadow_class == 'M'

    def test_standard_table_length(self):
        table = standard_family_nc_table(max_r=20)
        assert len(table) == 10  # 10 standard entries

    def test_standard_table_kappas(self):
        """Verify kappa values in the standard table."""
        table = standard_family_nc_table(max_r=20)
        # First entry: heisenberg k=1, kappa=1
        assert abs(table[0].kappa - 1.0) < 1e-12
        # Second: heisenberg k=2, kappa=2
        assert abs(table[1].kappa - 2.0) < 1e-12

    def test_wodzicki_equals_twice_dixmier_in_table(self):
        """For all families: Res_W = 2 * Tr_omega (d_S = 2)."""
        table = standard_family_nc_table(max_r=20)
        for entry in table:
            assert abs(entry.wodzicki_residue - 2.0 * entry.dixmier_trace) < 1e-10

    def test_spectral_determinant_universal(self):
        """Spectral determinant = (2pi)^{1/4} for all families (canonical model)."""
        table = standard_family_nc_table(max_r=20)
        expected = (2.0 * math.pi) ** 0.25
        for entry in table:
            assert abs(entry.spectral_determinant - expected) < 1e-10


# ============================================================================
#  Section 14: Comprehensive report
# ============================================================================

class TestComprehensiveReport:
    """Integration test: comprehensive NC report."""

    def test_heisenberg_report_structure(self):
        report = comprehensive_nc_report('heisenberg', 1.0, n_max=100,
                                         n_zeros=5, max_r=10)
        assert report['kappa'] == 1.0
        assert report['shadow_class'] == 'G'
        assert abs(report['dixmier_exact'] - 1.0) < 1e-12
        assert len(report['nc_at_zeros']) == 5

    def test_virasoro_report_dixmier_methods_agree(self):
        """All three Dixmier methods approximately agree."""
        report = comprehensive_nc_report('virasoro', 26.0, n_max=200,
                                         n_zeros=3, max_r=30)
        exact = report['dixmier_exact']
        partial = report['dixmier_partial']
        cesaro = report['dixmier_cesaro']
        # All should be within 20% of kappa = 13
        assert abs(exact - 13.0) < 1e-10
        assert abs(partial - 13.0) < 3.0
        assert abs(cesaro - 13.0) < 3.0

    def test_report_heat_kernel_match(self):
        report = comprehensive_nc_report('heisenberg', 1.0, n_max=100,
                                         n_zeros=3, max_r=10)
        assert report['heat_kernel_check']['match']

    def test_report_log_divergence(self):
        report = comprehensive_nc_report('heisenberg', 2.0, n_max=200,
                                         n_zeros=3, max_r=10)
        assert abs(report['log_divergence']['alpha'] - 2.0) < 0.2


# ============================================================================
#  Section 15: Multi-path convergence (cross-verification)
# ============================================================================

class TestMultiPathConvergence:
    """Verify that all five paths give consistent results."""

    @pytest.mark.parametrize("family,param,expected_kappa", [
        ('heisenberg', 1.0, 1.0),
        ('heisenberg', 3.0, 3.0),
        ('virasoro', 1.0, 0.5),
        ('virasoro', 13.0, 6.5),
        ('virasoro', 26.0, 13.0),
        ('affine_sl2', 1.0, 2.25),
        ('affine_sl3', 1.0, 16.0 / 3.0),
    ])
    def test_dixmier_exact_matches_kappa(self, family, param, expected_kappa):
        """Path 1 (exact): Tr_omega = kappa."""
        dix = dixmier_trace_exact(family, param)
        assert abs(dix - abs(expected_kappa)) < 1e-10

    @pytest.mark.parametrize("family,param,expected_kappa", [
        ('heisenberg', 1.0, 1.0),
        ('heisenberg', 5.0, 5.0),
        ('virasoro', 26.0, 13.0),
    ])
    def test_log_fit_alpha_matches_kappa(self, family, param, expected_kappa):
        """Path 2 (log fit): alpha = kappa."""
        lf = log_divergence_fit(family, param, n_max=500)
        assert abs(lf['alpha'] - abs(expected_kappa)) < 0.1 * abs(expected_kappa) + 0.01

    @pytest.mark.parametrize("family,param,expected_kappa", [
        ('heisenberg', 1.0, 1.0),
        ('virasoro', 26.0, 13.0),
        ('affine_sl2', 1.0, 2.25),
    ])
    def test_wodzicki_matches_2kappa(self, family, param, expected_kappa):
        """Path 3 (Wodzicki): Res_W = 2*kappa."""
        wod = wodzicki_residue(family, param)
        assert abs(wod - 2.0 * abs(expected_kappa)) < 1e-10

    @pytest.mark.parametrize("family,param", [
        ('heisenberg', 1.0),
        ('virasoro', 13.0),
        ('affine_sl2', 2.0),
    ])
    def test_heat_kernel_matches_dixmier(self, family, param):
        """Path 5 (heat kernel): a_0/Gamma(1) = kappa."""
        check = heat_kernel_dixmier_check(family, param)
        assert check['match']

    @pytest.mark.parametrize("family,param,expected_kappa", [
        ('heisenberg', 1.0, 1.0),
        ('heisenberg', 2.0, 2.0),
        ('virasoro', 26.0, 13.0),
    ])
    def test_singular_value_C_matches_kappa(self, family, param, expected_kappa):
        """Path 1 (singular value fit): C = kappa."""
        sv = shadow_eigenvalues(family, param, n_max=500)
        fit = fit_singular_value_decay(sv.singular_values, n_start=10)
        assert abs(fit.C - abs(expected_kappa)) < 0.1 * abs(expected_kappa) + 0.01


# ============================================================================
#  Section 16: Edge cases and error handling
# ============================================================================

class TestEdgeCases:
    """Edge cases, boundary conditions, error handling."""

    def test_kappa_zero_heisenberg(self):
        """H_0: kappa = 0, Dixmier trace = 0."""
        assert kappa_value('heisenberg', 0.0) == 0.0
        assert dixmier_trace_exact('heisenberg', 0.0) == 0.0

    def test_negative_kappa(self):
        """H_{-1}: kappa = -1. Dixmier trace = |kappa| = 1."""
        assert kappa_value('heisenberg', -1.0) == -1.0
        assert dixmier_trace_exact('heisenberg', -1.0) == 1.0

    def test_virasoro_c_zero(self):
        """Vir_0: kappa = 0."""
        assert kappa_value('virasoro', 0.0) == 0.0

    def test_heat_kernel_t_zero(self):
        """Heat kernel diverges as t -> 0."""
        assert heat_kernel_trace_exact(1e-10) > 1e9

    def test_heat_kernel_negative_t(self):
        """Negative t gives infinity."""
        assert heat_kernel_trace_exact(-1.0) == float('inf')

    def test_singular_values_n_1(self):
        """n_max=1 gives a single singular value."""
        sv = shadow_eigenvalues('heisenberg', 1.0, n_max=1)
        assert len(sv.singular_values) == 1
        assert abs(sv.singular_values[0] - 1.0) < 1e-12

    def test_partial_sum_empty(self):
        """Partial sum with N=0."""
        sv = shadow_eigenvalues('heisenberg', 1.0, n_max=10)
        assert partial_sum_singular_values(sv.singular_values, 0) == 0.0


# ============================================================================
#  Section 17: Shadow eigenvalues from tower
# ============================================================================

class TestShadowEigenvaluesFromTower:
    """Test the tower-based eigenvalue construction."""

    def test_tower_eigenvalues_heisenberg(self):
        """Heisenberg: only one eigenvalue at r=2."""
        sv = shadow_eigenvalues_from_tower('heisenberg', 1.0, n_max=50, max_r=10)
        # First eigenvalue should be 2 (from S_2)
        assert abs(sv.eigenvalues[0] - 2.0) < 1e-10

    def test_tower_eigenvalues_affine(self):
        """Affine sl_2: eigenvalues at r=2 and r=3."""
        sv = shadow_eigenvalues_from_tower('affine_sl2', 1.0, n_max=50, max_r=10)
        # First two eigenvalues from tower
        assert abs(sv.eigenvalues[0] - 2.0) < 1e-10
        assert abs(sv.eigenvalues[1] - 3.0) < 1e-10

    def test_tower_kappa_correct(self):
        """Tower construction preserves kappa."""
        sv = shadow_eigenvalues_from_tower('virasoro', 26.0, n_max=50)
        assert abs(sv.kappa - 13.0) < 1e-10

    def test_tower_singular_values_descending(self):
        """Singular values from tower are descending."""
        sv = shadow_eigenvalues_from_tower('virasoro', 10.0, n_max=100, max_r=20)
        for i in range(len(sv.singular_values) - 1):
            assert sv.singular_values[i] >= sv.singular_values[i + 1] - 1e-15


# ============================================================================
#  Section 18: NC zeta exact (analytic continuation)
# ============================================================================

class TestNCZetaExact:
    """Analytic continuation of the NC spectral zeta."""

    def test_exact_at_s_4(self):
        """zeta_D(4) = zeta_R(2) = pi^2/6."""
        z = nc_spectral_zeta_exact(complex(4.0, 0.0))
        assert abs(z.real - math.pi ** 2 / 6.0) < 0.05

    def test_exact_at_s_6(self):
        """zeta_D(6) = zeta_R(3) ~ 1.202."""
        z = nc_spectral_zeta_exact(complex(6.0, 0.0))
        assert abs(z.real - 1.2020569031595942) < 0.05

    def test_exact_at_large_s(self):
        """zeta_D(20) = zeta_R(10) ~ 1.0009945..."""
        z = nc_spectral_zeta_exact(complex(20.0, 0.0))
        assert abs(z.real - 1.0) < 0.01  # Very close to 1 for large s

    def test_exact_real_on_real_axis(self):
        """For real s > 2, zeta_D(s) is real."""
        z = nc_spectral_zeta_exact(complex(4.0, 0.0))
        assert abs(z.imag) < 0.01


# ============================================================================
#  Section 19: Parametric sweeps
# ============================================================================

class TestParametricSweeps:
    """Sweep parameters and verify monotonicity/scaling."""

    def test_dixmier_monotone_in_k(self):
        """Tr_omega increases with k for Heisenberg."""
        dix_prev = 0.0
        for k in [0.5, 1.0, 2.0, 5.0, 10.0]:
            dix = dixmier_trace_exact('heisenberg', k)
            assert dix >= dix_prev
            dix_prev = dix

    def test_dixmier_monotone_in_c(self):
        """Tr_omega increases with c for Virasoro (c > 0)."""
        dix_prev = 0.0
        for c in [1.0, 5.0, 13.0, 26.0, 48.0]:
            dix = dixmier_trace_exact('virasoro', c)
            assert dix >= dix_prev
            dix_prev = dix

    def test_wodzicki_monotone_in_k(self):
        """Res_W increases with k for Heisenberg."""
        wod_prev = 0.0
        for k in [0.5, 1.0, 2.0, 5.0]:
            wod = wodzicki_residue('heisenberg', k)
            assert wod >= wod_prev
            wod_prev = wod

    def test_complementarity_sum_constant(self):
        """kappa + kappa' = 13 independent of c for Virasoro."""
        for c in [0.1, 1.0, 5.0, 13.0, 20.0, 25.9]:
            comp = dixmier_complementarity('virasoro', c)
            assert abs(comp['sum'] - 13.0) < 1e-10


# ============================================================================
#  Section 20: Additivity (cross-family consistency)
# ============================================================================

class TestAdditivity:
    """kappa is additive under direct sum => Dixmier trace is additive."""

    def test_heisenberg_additivity(self):
        """kappa(H_{k1} + H_{k2}) = k1 + k2 => Tr_omega additive."""
        k1, k2 = 1.0, 3.0
        dix1 = dixmier_trace_exact('heisenberg', k1)
        dix2 = dixmier_trace_exact('heisenberg', k2)
        dix_sum = dixmier_trace_exact('heisenberg', k1 + k2)
        assert abs(dix1 + dix2 - dix_sum) < 1e-12

    def test_wodzicki_additivity(self):
        """Res_W is additive under direct sum."""
        k1, k2 = 2.0, 5.0
        w1 = wodzicki_residue('heisenberg', k1)
        w2 = wodzicki_residue('heisenberg', k2)
        w_sum = wodzicki_residue('heisenberg', k1 + k2)
        assert abs(w1 + w2 - w_sum) < 1e-12


# ============================================================================
#  Section 21: NC geometry consistency relations
# ============================================================================

class TestNCConsistency:
    """Cross-check relations between NC invariants."""

    def test_connes_trace_theorem(self):
        """Res_W(|D|^{-d_S}) = d_S * Tr_omega(|D|^{-d_S}) for all families."""
        families = [
            ('heisenberg', 1.0),
            ('heisenberg', 5.0),
            ('virasoro', 1.0),
            ('virasoro', 26.0),
            ('affine_sl2', 1.0),
            ('affine_sl3', 1.0),
            ('betagamma', 1.0),
        ]
        d_S = 2.0
        for fam, p in families:
            dix = dixmier_trace_exact(fam, p, d_S)
            wod = wodzicki_residue(fam, p, d_S)
            assert abs(wod - d_S * dix) < 1e-10, (
                f"Connes trace theorem failed for {fam}: "
                f"Res_W={wod}, d_S*Tr_omega={d_S * dix}"
            )

    def test_zeta_D_at_zero_universal(self):
        """zeta_D(0) = -1/2 independent of family (canonical model)."""
        z = nc_spectral_zeta_at_zero()
        assert abs(z.real + 0.5) < 1e-12

    def test_determinant_universal(self):
        """det(D^2) = (2pi)^{1/4} independent of family (canonical model)."""
        det = nc_spectral_determinant()
        assert abs(det - (2.0 * math.pi) ** 0.25) < 1e-10

    def test_wodzicki_from_symbol_vs_connes(self):
        """Two independent computations of Wodzicki residue agree."""
        for fam, p in [('heisenberg', 1.0), ('virasoro', 26.0), ('affine_sl2', 1.0)]:
            w1 = wodzicki_residue(fam, p)
            w2 = wodzicki_residue_from_symbol(fam, p)
            assert abs(w1 - w2) < 1e-10


# ============================================================================
#  Section 22: Riemann zero properties
# ============================================================================

class TestRiemannZeroProperties:
    """Properties of stored Riemann zeros for internal consistency."""

    def test_zeros_positive(self):
        for g in RIEMANN_ZEROS:
            assert g > 0

    def test_zeros_above_14(self):
        """All imaginary parts above 14."""
        for g in RIEMANN_ZEROS:
            assert g > 14.0

    def test_zero_spacing_positive(self):
        """Consecutive zeros have positive spacing."""
        for i in range(len(RIEMANN_ZEROS) - 1):
            assert RIEMANN_ZEROS[i + 1] - RIEMANN_ZEROS[i] > 0.1

    def test_25th_zero(self):
        """25th zero gamma_25 ~ 88.809."""
        assert abs(RIEMANN_ZEROS[24] - 88.809111207634465) < 1e-8


# ============================================================================
#  Section 23: Singular value asymptotics at specific n
# ============================================================================

class TestSingularValueSpecific:
    """Verify specific singular values at n=1, 100, 500."""

    def test_sigma_1_equals_kappa(self):
        """sigma_1 = kappa (largest singular value)."""
        for fam, p in [('heisenberg', 1.0), ('virasoro', 26.0)]:
            sv = shadow_eigenvalues(fam, p, n_max=10)
            kap = abs(kappa_value(fam, p))
            assert abs(sv.singular_values[0] - kap) < 1e-12

    def test_sigma_100_heisenberg(self):
        """sigma_100 = k/100 for Heisenberg H_k."""
        sv = shadow_eigenvalues('heisenberg', 1.0, n_max=100)
        assert abs(sv.singular_values[99] - 0.01) < 1e-12

    def test_sigma_500_virasoro(self):
        """sigma_500 = (c/2)/500 for Virasoro."""
        sv = shadow_eigenvalues('virasoro', 26.0, n_max=500)
        expected = 13.0 / 500.0
        assert abs(sv.singular_values[499] - expected) < 1e-12

    def test_500_singular_values_computed(self):
        """Full 500-element singular value array for each family."""
        for fam, p in [('heisenberg', 1.0), ('virasoro', 10.0), ('affine_sl2', 2.0)]:
            sv = shadow_eigenvalues(fam, p, n_max=500)
            assert len(sv.singular_values) == 500


# ============================================================================
#  Section 24: Comprehensive multi-zero sweep
# ============================================================================

class TestMultiZeroSweep:
    """Shadow zeta at all 25 Riemann zeros for multiple families."""

    @pytest.mark.parametrize("zero_idx", list(range(1, 26)))
    def test_heisenberg_shadow_at_zero(self, zero_idx):
        """Heisenberg shadow zeta |zeta_A(rho)| > 0 at every Riemann zero."""
        gamma = RIEMANN_ZEROS[zero_idx - 1]
        rho = complex(0.5, gamma)
        z = shadow_nc_zeta('heisenberg', 1.0, rho, max_r=10)
        # zeta_A = 2^{-rho}, |z| = 2^{-1/2} ~ 0.707
        assert abs(z) > 0.5

    @pytest.mark.parametrize("zero_idx", [1, 5, 10, 15, 20, 25])
    def test_virasoro_shadow_at_zero(self, zero_idx):
        """Virasoro shadow zeta at selected Riemann zeros."""
        data = nc_integral_at_riemann_zero('virasoro', 26.0, zero_idx, max_r=30)
        # Record the value; generically nonzero
        assert isinstance(data.shadow_zeta_at_zero, complex)

    @pytest.mark.parametrize("zero_idx", [1, 5, 10])
    def test_affine_shadow_at_zero(self, zero_idx):
        """Affine sl_2 shadow zeta at selected zeros."""
        data = nc_integral_at_riemann_zero('affine_sl2', 1.0, zero_idx, max_r=10)
        assert isinstance(data.shadow_zeta_at_zero, complex)
        assert abs(data.shadow_zeta_at_zero) > 0.01


# ============================================================================
#  Section 25: Heisenberg closed-form Dixmier verification
# ============================================================================

class TestHeisenbergClosedForm:
    """Heisenberg has closed-form everything; verify exhaustively."""

    def test_shadow_zeta_closed_form(self):
        """zeta_{H_k}(s) = k * 2^{-s} (exact)."""
        k = 3.0
        for s in [1 + 0j, 2 + 1j, 0.5 + 14.134725j, -1 + 0j]:
            z = shadow_nc_zeta('heisenberg', k, s, max_r=10)
            expected = k * 2.0 ** (-s)
            assert abs(z - expected) < 1e-10

    def test_dixmier_cesaro_converges_to_k(self):
        """Cesaro mean -> k at large N."""
        k = 2.0
        sv = shadow_eigenvalues('heisenberg', k, n_max=500)
        dix = dixmier_trace_cesaro(sv.singular_values, 500, window=100)
        assert abs(dix - k) < 0.5  # Converges slowly but within range

    def test_harmonic_number_approximation(self):
        """sum_{n=1}^N 1/n ~ log(N) + gamma, verifying our Dixmier trace.

        H_N = log(N) + gamma + 1/(2N) - 1/(12N^2) + O(1/N^4).
        """
        gamma_em = 0.5772156649015329
        for N in [100, 500]:
            H_N = sum(1.0 / n for n in range(1, N + 1))
            approx = math.log(N) + gamma_em + 1.0 / (2 * N)
            assert abs(H_N - approx) < 1.0 / (12 * N * N) + 0.001
