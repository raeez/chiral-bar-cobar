r"""Tests for the finite scalar Faber-Pandharipande generating function.

Verifies:
  1. λ_g^FP table through genus 15
  2. Â-genus identity: (x/2)/sin(x/2) = Σ λ_g^FP x^{2g}
  3. Free energy closed form: F(ℏ) = κ/ℏ² · [(ℏ/2)/sin(ℏ/2) - 1]
  4. Universal ratios F_{g+1}/F_g
  5. Sign resolution: (x/2)/sin(x/2) vs (x/2)/sinh(x/2)
  6. Conditional Virasoro genus-2 contact pairing
  7. Scalar infinite-product window
  8. KdV/tau firewall for missing descendant CohFT data
"""

from sympy import (
    Rational, Symbol, bernoulli, factorial, Abs, simplify, series,
    sin, sinh, pi, log, oo,
)

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.utils import lambda_fp
from lib.genus_generating_function import (
    lambda_fp_table,
    lambda_fp_extended,
    A_hat_coefficients,
    verify_A_hat_equals_FP,
    scalar_free_energy_series,
    scalar_free_energy_closed_form,
    verify_closed_form,
    free_energy_sign_resolution,
    universal_ratios,
    virasoro_Q_contact,
    genus2_shadow_correction_virasoro,
    free_energy_tau_function_check,
    shadow_corrected_structure,
    numerical_verification,
)


# ═══════════════════════════════════════════════════════════════════════
# FP number table
# ═══════════════════════════════════════════════════════════════════════

class TestFPNumbers:
    """Verify Faber-Pandharipande intersection numbers."""

    def test_lambda_1_fp(self):
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_2_fp(self):
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_3_fp(self):
        """λ_3^FP = (2^5-1)/2^5 · |B_6|/6! = 31/32 · (1/42)/720."""
        expected = Rational(31, 32) * Rational(1, 42) / factorial(6)
        assert lambda_fp(3) == expected

    def test_fp_table_length(self):
        table = lambda_fp_table(15)
        assert len(table) == 15

    def test_fp_all_positive(self):
        """λ_g^FP > 0 for all g ≥ 1."""
        for g in range(1, 16):
            assert lambda_fp(g) > 0

    def test_lambda_0_extended(self):
        assert lambda_fp_extended(0) == 1

    def test_fp_formula(self):
        """Verify formula λ_g^FP = (2^{2g-1}-1)/2^{2g-1} · |B_{2g}|/(2g)!."""
        for g in range(1, 11):
            power = 2**(2*g - 1)
            expected = Rational(power - 1, power) * Abs(bernoulli(2*g)) / factorial(2*g)
            assert lambda_fp(g) == expected


# ═══════════════════════════════════════════════════════════════════════
# Â-genus generating function identity
# ═══════════════════════════════════════════════════════════════════════

class TestAHatGenus:
    """Verify (x/2)/sin(x/2) = Σ λ_g^FP x^{2g}."""

    def test_generating_function_g10(self):
        """Finite exact verification through genus 10."""
        result = numerical_verification(10)
        assert result['all_match']

    def test_generating_function_g15(self):
        """Finite exact verification through genus 15."""
        result = numerical_verification(15)
        assert result['all_match']

    def test_sinh_version_alternating(self):
        """Verify (x/2)/sinh(x/2) = Σ (-1)^g λ_g^FP x^{2g}."""
        result = verify_A_hat_equals_FP(10)
        assert result['all_match']

    def test_sin_vs_sinh(self):
        """(x/2)/sin(x/2) = Â(ix), sign resolution."""
        x = Symbol('x')
        s_sin = series(x/2/sin(x/2), x, 0, 12)
        s_sinh = series(x/2/sinh(x/2), x, 0, 12)
        # Check coefficient relation: sin version has all positive,
        # sinh version alternates
        for g in range(6):
            c_sin = Rational(s_sin.coeff(x, 2*g))
            c_sinh = Rational(s_sinh.coeff(x, 2*g))
            assert c_sin == (-1)**g * c_sinh

    def test_odd_coefficients_zero(self):
        """Only even powers appear in (x/2)/sin(x/2)."""
        x = Symbol('x')
        s = series(x/2/sin(x/2), x, 0, 22)
        for k in range(1, 21, 2):  # odd powers
            assert s.coeff(x, k) == 0


# ═══════════════════════════════════════════════════════════════════════
# Free energy closed form
# ═══════════════════════════════════════════════════════════════════════

class TestFreeEnergy:
    """Verify closed form F(ℏ) = κ/ℏ² · [(ℏ/2)/sin(ℏ/2) - 1]."""

    def test_series_matches_closed_form(self):
        """Term-by-term comparison through genus 10."""
        x = Symbol('x')
        g_max = 10

        # Closed form: 1/hbar^2 * [(hbar/2)/sin(hbar/2) - 1]
        closed_inner = series(x/2/sin(x/2) - 1, x, 0, 2*g_max + 2)
        # closed_inner / x^2 = Σ λ_g^FP x^{2g-2}
        for g in range(1, g_max + 1):
            coeff_closed = Rational(closed_inner.coeff(x, 2*g))
            assert coeff_closed == lambda_fp(g), f"Mismatch at genus {g}"

    def test_closed_form_function_uses_sin_branch(self):
        """The public closed-form helper returns the positive FP branch."""
        kappa = Symbol('kappa')
        hbar = Symbol('hbar')
        closed = scalar_free_energy_closed_form(kappa, hbar)
        expanded = series(closed, hbar, 0, 8).removeO()
        for g in range(1, 4):
            coeff = expanded.coeff(hbar, 2*g - 2)
            assert simplify(coeff - kappa * lambda_fp(g)) == 0

    def test_verify_closed_form_reports_finite_window(self):
        result = verify_closed_form(10)
        assert result['all_match']
        assert result['scope'] == 'finite exact rational window 1 <= g <= 10'

    def test_genus_1_term(self):
        """F_1 = κ/24 (the leading term as ℏ → 0)."""
        kappa = Symbol('kappa')
        hbar = Symbol('hbar')
        F = scalar_free_energy_series(kappa, hbar, g_max=1)
        assert F == kappa * Rational(1, 24)

    def test_universal_ratio_F2_F1(self):
        """F_2/F_1 = λ_2^FP/λ_1^FP = (7/5760)/(1/24) = 7/240."""
        ratio = lambda_fp(2) / lambda_fp(1)
        assert ratio == Rational(7, 240)


# ═══════════════════════════════════════════════════════════════════════
# Universal ratios
# ═══════════════════════════════════════════════════════════════════════

class TestUniversalRatios:
    """F_{g+1}/F_g = λ_{g+1}^FP/λ_g^FP are universal (κ-independent)."""

    def test_ratio_21(self):
        assert lambda_fp(2) / lambda_fp(1) == Rational(7, 240)

    def test_ratio_32(self):
        r = lambda_fp(3) / lambda_fp(2)
        assert r == Rational(r.p, r.q)  # exact rational
        assert r > 0

    def test_ratios_decreasing(self):
        """Ratios approach the scalar Bernoulli value 1/(2π)^2."""
        for g in range(1, 10):
            r = lambda_fp(g+1) / lambda_fp(g)
            assert 0 < r < 1, f"Ratio at g={g} is {r}, expected < 1"

    def test_ratios_table(self):
        ratios = universal_ratios(10)
        assert len(ratios) == 9
        for key, val in ratios.items():
            assert val > 0


# ═══════════════════════════════════════════════════════════════════════
# Sign resolution
# ═══════════════════════════════════════════════════════════════════════

class TestSignResolution:
    """The free energy uses (x/2)/sin(x/2), not (x/2)/sinh(x/2)."""

    def test_sign_resolution(self):
        result = free_energy_sign_resolution()
        assert result['real_equals_FP']
        assert result['standard_equals_(-1)^g_FP']

    def test_all_positive_coefficients(self):
        """(x/2)/sin(x/2) has all positive coefficients."""
        x = Symbol('x')
        s = series(x/2/sin(x/2), x, 0, 32)
        for g in range(16):
            assert Rational(s.coeff(x, 2*g)) > 0


# ═══════════════════════════════════════════════════════════════════════
# Virasoro shadow corrections
# ═══════════════════════════════════════════════════════════════════════

class TestVirasoro:
    """Scalar Virasoro term and conditional contact pairing."""

    def test_Q_contact(self):
        c = Symbol('c')
        Q = virasoro_Q_contact(c)
        assert simplify(Q - 10/(c*(5*c + 22))) == 0

    def test_Q_contact_c26(self):
        """At c = 26: Q^contact = 10/(26 · 152) = 5/1976."""
        Q = virasoro_Q_contact(26)
        assert Q == Rational(10, 26 * 152)

    def test_genus2_scalar(self):
        """F_2^scalar(Vir_c) = c/2 · 7/5760 = 7c/11520."""
        c = Symbol('c')
        data = genus2_shadow_correction_virasoro(c)
        assert simplify(data['F_2_scalar'] - c * Rational(7, 11520)) == 0

    def test_genus2_contact_pairing_conditional(self):
        """Q_contact times 1/1152 is conditional descendant data."""
        c = Symbol('c')
        data = genus2_shadow_correction_virasoro(c)
        assert data['boundary_wk_pairing'] == Rational(1, 1152)
        assert simplify(
            data['conditional_delta_F_2']
            - virasoro_Q_contact(c) * Rational(1, 1152)
        ) == 0
        assert data['unconditional_full_genus2_correction'] is None

    def test_conditional_contact_ratio_subleading(self):
        """The conditional contact/scalar ratio vanishes at large c."""
        c = Symbol('c')
        data = genus2_shadow_correction_virasoro(c)
        ratio = simplify(data['conditional_ratio_if_pairing_applies'])
        from sympy import limit
        assert limit(ratio, c, oo) == 0

    def test_contact_scope_blocks_unconditional_correction_claim(self):
        data = genus2_shadow_correction_virasoro(26)
        assert data['claim_scope'].startswith('conditional:')


# ═══════════════════════════════════════════════════════════════════════
# Scalar infinite product
# ═══════════════════════════════════════════════════════════════════════

class TestScalarInfiniteProduct:
    """(ℏ/2)/sin(ℏ/2) = Π_{n≥1} (1 - ℏ²/(2nπ)²)^{-1}."""

    def test_product_matches_series(self):
        """The Euler product gives the x^2 logarithmic coefficient."""
        x = Symbol('x')
        # sin(x/2) = (x/2) Π_{n≥1} (1 - x²/(2nπ)²)
        # So (x/2)/sin(x/2) = Π_{n≥1} (1 - x²/(2nπ)²)^{-1}
        # log[(x/2)/sin(x/2)] = -Σ_{n≥1} log(1 - x²/(2nπ)²)
        #                     = Σ_{n≥1} Σ_{m≥1} x^{2m} / (m · (2nπ)^{2m})
        from sympy import zeta
        product_coeff = simplify(zeta(2) / (2*pi)**2)
        log_series = series(log(x/2/sin(x/2)), x, 0, 4)
        assert product_coeff == Rational(1, 24)
        assert Rational(log_series.coeff(x, 2)) == Rational(1, 24)

    def test_scalar_meromorphic_radius(self):
        """The scalar sin closed form has first pole at |ℏ| = 2π."""
        # The ratio test: λ_{g+1}/λ_g → 1/(2π)² as g → ∞
        # (from Bernoulli number asymptotics: |B_{2g}| ~ 2(2g)!/(2π)^{2g})
        ratios = []
        for g in range(5, 15):
            r = float(lambda_fp(g+1) / lambda_fp(g))
            ratios.append(r)
        # Should converge to 1/(2π)² ≈ 0.02533
        target = 1 / (2 * 3.14159265)**2
        assert abs(ratios[-1] - target) < 0.001


# ═══════════════════════════════════════════════════════════════════════
# Descendant CohFT firewall
# ═══════════════════════════════════════════════════════════════════════

class TestDescendantCohFTFirewall:
    """Scalar FP windows do not construct descendant hierarchies."""

    def test_scalar_window_does_not_construct_kdv(self):
        result = free_energy_tau_function_check()
        assert 'scalar_free_energy' in result
        assert 'infinite_product' in result
        assert result['constructs_full_kdv_hierarchy'] is False
        assert result['constructs_analytic_tau_function'] is False
        assert result['claims_all_genus_shadow_convergence'] is False
        assert result['requires_witten_kontsevich_descendants'] is True
        assert 'all-genus shadow convergence requires separate analytic input' in result['analytic_scope']

    def test_shadow_corrected_structure(self):
        result = shadow_corrected_structure()
        assert result['mc_equation_controls_corrections']
        assert result['closed_shadow_generating_function'] is None
        assert result['requires_descendant_cohft_data'] is True

    def test_gaussian_no_correction(self):
        """Gaussian archetype (Heisenberg): no shadow correction."""
        result = shadow_corrected_structure()
        assert 'δF = 0' in result['gaussian_correction']


# ═══════════════════════════════════════════════════════════════════════
# Specific FP numbers (high genus, exact values)
# ═══════════════════════════════════════════════════════════════════════

class TestHighGenusFP:
    """Exact FP numbers at high genus."""

    def test_lambda_4(self):
        """λ_4^FP from Bernoulli B_8 = -1/30."""
        g = 4
        B8 = bernoulli(8)  # = -1/30
        power = 2**(2*g-1)  # = 128
        expected = Rational(power-1, power) * Abs(B8) / factorial(8)
        assert lambda_fp(4) == expected

    def test_lambda_5(self):
        g = 5
        B10 = bernoulli(10)  # = 5/66
        power = 2**(2*g-1)
        expected = Rational(power-1, power) * Abs(B10) / factorial(10)
        assert lambda_fp(5) == expected

    def test_lambda_10(self):
        """Verify λ_10^FP is computable and positive."""
        val = lambda_fp(10)
        assert val > 0
        assert isinstance(val, Rational)

    def test_lambda_15(self):
        """Verify λ_15^FP is computable and positive."""
        val = lambda_fp(15)
        assert val > 0
        assert isinstance(val, Rational)


# ═══════════════════════════════════════════════════════════════════════
# Scalar coefficient surface
# ═══════════════════════════════════════════════════════════════════════

class TestScalarCoefficientSurface:
    r"""Finite-window scalar free-energy identity.

    Scalar coefficient identity:

      F(ℏ) = κ/ℏ² · [(ℏ/2)/sin(ℏ/2) - 1]

    where (ℏ/2)/sin(ℏ/2) is the positive FP generating function,
    formally obtained from the A-hat series by x -> i*x.

    Equivalently:
      F^total(ℏ) = κ · (ℏ/2)/(ℏ² sin(ℏ/2))
                 = κ · (2ℏ sin(ℏ/2))^{-1}

    with genus-g projection:
      F_g = κ · λ_g^FP,  λ_g^FP = (2^{2g-1}-1)/2^{2g-1} · |B_{2g}|/(2g)!

    Conditional shadow-corrected version:
      F^corr(ℏ) = F^scalar(ℏ) + δF^shadow(ℏ)
    where δF^shadow requires the MC element Θ_A and descendant graph data.
    """

    def test_finite_scalar_statement(self):
        """Verify the scalar coefficient identity through genus 15."""
        result = numerical_verification(15)
        assert result['all_match'], "A-hat companion identity failed"

    def test_closed_form_series_agreement(self):
        """Closed form and series agree through genus 10."""
        x = Symbol('x')
        g_max = 10
        # (x/2)/sin(x/2) - 1 = Σ_{g≥1} λ_g^FP x^{2g}
        s = series(x/2/sin(x/2) - 1, x, 0, 2*g_max + 2)
        for g in range(1, g_max + 1):
            assert Rational(s.coeff(x, 2*g)) == lambda_fp(g)

    def test_log_product_first_coefficient(self):
        """The scalar Euler product gives the first logarithmic coefficient."""
        # Verify: log[(x/2)/sin(x/2)] at x^2 gives 1/24
        x = Symbol('x')
        s = series(log(x/2/sin(x/2)), x, 0, 6)
        assert Rational(s.coeff(x, 2)) == Rational(1, 24)

    def test_scalar_meromorphic_window_at_hbar_1(self):
        """The scalar sin series is inside its first-pole window at ℏ = 1."""
        # Evaluate at ℏ = 1
        val = float(sum(lambda_fp(g) for g in range(1, 20)))
        exact = float(Rational(1, 2) / sin(Rational(1, 2))) - 1
        assert abs(val - exact) < 1e-10
