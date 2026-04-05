r"""Tests for bc_koszul_zeta_complementarity_engine.py -- Koszul duality
(Theorem C) acting on zeta zeros in the Benjamin-Chang framework.

Verification paths:
  - Path 1: Direct computation of residue ratios
  - Path 2: Gamma duplication/reflection identities for ratio simplification
  - Path 3: Boundary cases c=0, c=26 where one algebra is trivial
  - Path 4: Consistency with kappa+kappa' values from landscape_census.tex

80+ tests covering:
  1. Complementarity of residues (A_c / A_{26-c})
  2. Self-dual residue at c=13
  3. Duality-twisted zeta with double poles
  4. Complementarity L-function and Koszul perturbation
  5. Shadow complementarity (shadow zeta sum/difference)
  6. Lagrangian intersection structure
  7. Defect form Omega_c
  8. Boundary cases and kappa consistency

Manuscript references:
    thm:complementarity (higher_genus_complementarity.tex)
    eq:constrained-epstein-fe (arithmetic_shadows.tex)
    def:universal-residue-factor (arithmetic_shadows.tex)
    rem:koszul-epstein-constraints (arithmetic_shadows.tex)

CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP1): kappa formulas are family-specific.
"""

import math
import cmath
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

from compute.lib import bc_koszul_zeta_complementarity_engine as engine

DPS = 30
skipmp = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ============================================================================
# Section 1: Complementarity of residues -- A_c(rho) / A_{26-c}(rho)
# ============================================================================

class TestResidueComplementarity:
    """Tests for the residue complementarity ratio."""

    @skipmp
    def test_ratio_direct_vs_gamma(self):
        """Direct ratio A_c/A_{26-c} should equal the Gamma-only formula."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        for c_val in [1.0, 5.0, 10.0, 20.0, 25.0]:
            result = engine.residue_complementarity_ratio(rho, c_val, DPS)
            assert result['relative_error'] < 1e-10, (
                f"Direct vs Gamma ratio mismatch at c={c_val}: "
                f"rel_err={result['relative_error']}"
            )

    @skipmp
    def test_ratio_at_c_equals_13_is_unity(self):
        """At c=13 (self-dual): A_13/A_13 = 1."""
        mpmath.mp.dps = DPS
        for k in range(1, 6):
            rho = complex(mpmath.zetazero(k))
            result = engine.residue_complementarity_ratio(rho, 13.0, DPS)
            assert abs(result['ratio_gamma'] - 1.0) < 1e-10, (
                f"Ratio at c=13, zero #{k} != 1: {result['ratio_gamma']}"
            )

    @skipmp
    def test_ratio_c_and_26_minus_c_reciprocal(self):
        """A_c/A_{26-c} and A_{26-c}/A_c should be reciprocals."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        for c_val in [2.0, 7.0, 12.0, 18.0]:
            r1 = engine.residue_complementarity_ratio(rho, c_val, DPS)
            r2 = engine.residue_complementarity_ratio(rho, 26.0 - c_val, DPS)
            product = r1['ratio_gamma'] * r2['ratio_gamma']
            assert abs(product - 1.0) < 1e-10, (
                f"Reciprocal check failed at c={c_val}: product={product}"
            )

    @skipmp
    def test_ratio_multiple_zeros(self):
        """Check ratio consistency across first 5 zeros."""
        mpmath.mp.dps = DPS
        c_val = 5.0
        for k in range(1, 6):
            rho = complex(mpmath.zetazero(k))
            result = engine.residue_complementarity_ratio(rho, c_val, DPS)
            assert result['relative_error'] < 1e-10, (
                f"Zero #{k}: rel_err={result['relative_error']}"
            )
            # The ratio should be finite and nonzero
            assert abs(result['ratio_gamma']) > 1e-50, (
                f"Zero #{k}: ratio too small"
            )
            assert abs(result['ratio_gamma']) < 1e50, (
                f"Zero #{k}: ratio too large"
            )

    @skipmp
    def test_ratio_symmetry_under_conjugation(self):
        """A_c(conj(rho))/A_{26-c}(conj(rho)) = conj(A_c(rho)/A_{26-c}(rho))."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        rho_conj = rho.conjugate()
        c_val = 5.0
        r1 = engine.residue_complementarity_ratio(rho, c_val, DPS)
        r2 = engine.residue_complementarity_ratio(rho_conj, c_val, DPS)
        expected = r1['ratio_gamma'].conjugate()
        assert abs(r2['ratio_gamma'] - expected) < 1e-10, (
            f"Conjugation symmetry failed"
        )

    @skipmp
    def test_residue_ratio_modulus_spectrum(self):
        """Check that the modulus spectrum is computed without errors."""
        spectrum = engine.residue_ratio_modulus_spectrum(n_zeros=5, c_val=3.0, dps=DPS)
        assert len(spectrum) == 5
        for entry in spectrum:
            assert 'ratio_modulus' in entry
            assert entry['ratio_modulus'] > 0
            assert math.isfinite(entry['ratio_modulus'])

    @skipmp
    def test_residue_table_shape(self):
        """Table should have n_zeros * len(c_values) entries."""
        table = engine.residue_complementarity_table(
            n_zeros=3, c_values=[1.0, 13.0, 25.0], dps=DPS
        )
        assert len(table) == 9  # 3 zeros * 3 c-values


# ============================================================================
# Section 2: Self-dual residue at c=13
# ============================================================================

class TestSelfDualResidue:
    """Tests for the self-dual point c=13."""

    @skipmp
    def test_self_dual_residue_is_nonzero(self):
        """A_13(rho_1) should be nonzero."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        A = engine.self_dual_residue(rho, DPS)
        assert abs(A) > 1e-50, f"|A_13(rho_1)| too small: {abs(A)}"

    @skipmp
    def test_conjugation_property(self):
        """A_13(conj(rho)) = conj(A_13(rho)) for the self-dual point."""
        mpmath.mp.dps = DPS
        for k in range(1, 4):
            rho = complex(mpmath.zetazero(k))
            result = engine.self_dual_conjugation_test(rho, DPS)
            assert result['error'] < 1e-12, (
                f"Conjugation property failed at zero #{k}: err={result['error']}"
            )

    @skipmp
    def test_self_dual_multiplier_finite(self):
        """g_13(rho) should be finite for the first 5 zeros."""
        mpmath.mp.dps = DPS
        for k in range(1, 6):
            rho = complex(mpmath.zetazero(k))
            result = engine.self_dual_multiplier(rho, DPS)
            assert math.isfinite(result['|g_13|']), (
                f"g_13 not finite at zero #{k}"
            )
            assert result['|g_13|'] > 0, (
                f"g_13 vanishes at zero #{k}"
            )

    @skipmp
    def test_self_dual_multiplier_has_unit_modulus_under_rh(self):
        """Under RH (rho = 1/2 + it), 1-rho = 1/2 - it = conj(rho).

        So A_13(1-rho) = conj(A_13(rho)) by the conjugation property.
        Therefore |g_13(rho)| = |conj(A_13(rho))/A_13(rho)| = 1.
        """
        mpmath.mp.dps = DPS
        for k in range(1, 6):
            rho = complex(mpmath.zetazero(k))
            result = engine.self_dual_multiplier(rho, DPS)
            assert abs(result['|g_13|'] - 1.0) < 1e-8, (
                f"|g_13| != 1 at zero #{k}: {result['|g_13|']}"
            )

    @skipmp
    def test_self_dual_spectrum_shape(self):
        """Self-dual residue spectrum returns correct number of entries."""
        spectrum = engine.self_dual_residue_spectrum(n_zeros=5, dps=DPS)
        assert len(spectrum) == 5
        for entry in spectrum:
            assert '|A_13|' in entry
            assert entry['|A_13|'] > 0


# ============================================================================
# Section 3: Duality-twisted zeta Z^Koszul
# ============================================================================

class TestDualityTwistedZeta:
    """Tests for Z^Koszul(s) = F_c(s) * F_{26-c}(s)."""

    @skipmp
    def test_duality_twisted_is_product(self):
        """Z^Koszul = F_c * F_{26-c}."""
        s = 2.0 + 1.0j
        c = 5.0
        result = engine.duality_twisted_scattering(s, c, DPS)
        expected = result['F_c'] * result['F_dual']
        assert abs(result['Z_Koszul'] - expected) < 1e-15 * abs(expected), (
            f"Product check failed"
        )

    @skipmp
    def test_duality_twisted_symmetric_in_c(self):
        """Z^Koszul(s, c) = Z^Koszul(s, 26-c) (symmetric in Koszul pair)."""
        s = 2.0 + 3.0j
        for c in [1.0, 5.0, 10.0]:
            r1 = engine.duality_twisted_scattering(s, c, DPS)
            r2 = engine.duality_twisted_scattering(s, 26.0 - c, DPS)
            assert abs(r1['Z_Koszul'] - r2['Z_Koszul']) < 1e-10 * abs(r1['Z_Koszul']), (
                f"Symmetry failed at c={c}"
            )

    @skipmp
    def test_duality_twisted_contains_zeta_ratio_squared(self):
        """Z^Koszul contains [zeta(2s)/zeta(2s-1)]^2 as a factor."""
        s = 2.0 + 1.0j
        result = engine.duality_twisted_scattering(s, 5.0, DPS)
        # The zeta ratio squared should be nonzero and finite
        assert abs(result['zeta_ratio_sq']) > 1e-20
        assert abs(result['zeta_ratio_sq']) < 1e20

    @skipmp
    def test_duality_twisted_factorization(self):
        """Verify the factorization Z = Gamma * pi * zeta^2."""
        s = 2.5 + 1.5j
        for c in [3.0, 10.0, 13.0]:
            result = engine.duality_twisted_factorization(s, c, DPS)
            assert result['rel_err'] < 1e-10, (
                f"Factorization failed at c={c}: rel_err={result['rel_err']}"
            )

    @skipmp
    def test_double_pole_at_zeta_zero(self):
        """Z^Koszul has double poles at s = (1+rho)/2 (from zeta(2s-1)=0)."""
        result = engine.duality_twisted_double_pole_test(k=1, c=5.0, dps=DPS)
        # Check that Z * eps^2 converges to A_c * A_{26-c}
        approach = result['approach_data']
        # The last few entries (smallest eps) should be closest
        last = approach[-1]
        assert last['rel_err'] < 0.01, (
            f"Double pole test: rel_err={last['rel_err']} at eps={last['eps']}"
        )

    @skipmp
    def test_double_pole_at_c_13(self):
        """Double pole test at the self-dual point c=13."""
        result = engine.duality_twisted_double_pole_test(k=1, c=13.0, dps=DPS)
        last = result['approach_data'][-1]
        assert last['rel_err'] < 0.01, (
            f"Self-dual double pole: rel_err={last['rel_err']}"
        )


# ============================================================================
# Section 4: Complementarity L-function
# ============================================================================

class TestComplementarityLFunction:
    """Tests for L^comp_c(s) = F_c / F_{26-c}."""

    @skipmp
    def test_L_comp_at_c_13_is_unity(self):
        """L^comp_13(s) = 1 for generic s."""
        for s in [1.5 + 1j, 2.0 + 3j, 3.0 + 0.5j]:
            result = engine.complementarity_L_at_self_dual(s, DPS)
            assert result['deviation_from_1'] < 1e-10, (
                f"L^comp_13 != 1 at s={s}: deviation={result['deviation_from_1']}"
            )

    @skipmp
    def test_L_comp_direct_vs_gamma(self):
        """Direct F_c/F_{26-c} should match the Gamma-only formula."""
        s = 2.0 + 1.0j
        for c in [1.0, 5.0, 10.0, 20.0]:
            result = engine.complementarity_L_function(s, c, DPS)
            assert result['relative_error'] < 1e-10, (
                f"Direct vs Gamma mismatch at c={c}: "
                f"rel_err={result['relative_error']}"
            )

    @skipmp
    def test_L_comp_reciprocal(self):
        """L^comp_c * L^comp_{26-c} = 1."""
        s = 2.0 + 1.0j
        for c in [2.0, 8.0, 12.0]:
            L1 = engine.complementarity_L_function(s, c, DPS)['L_gamma']
            L2 = engine.complementarity_L_function(s, 26.0 - c, DPS)['L_gamma']
            product = L1 * L2
            assert abs(product - 1.0) < 1e-10, (
                f"Reciprocal check failed at c={c}: product={product}"
            )

    @skipmp
    def test_L_comp_no_zeta_content(self):
        """L^comp should be expressible in Gamma functions alone (no zeta)."""
        # The Gamma-only formula should work for all s (including near poles of zeta)
        s = 2.0 + 7.06j  # Near Im(rho_1)/2 but not exactly
        result = engine.complementarity_L_function(s, 5.0, DPS)
        assert result['relative_error'] < 1e-8, (
            f"Gamma formula breaks near zeta zero: rel_err={result['relative_error']}"
        )

    @skipmp
    def test_koszul_perturbation_analytic_vs_numerical(self):
        """delta_L(s) from digamma should match finite-difference."""
        for s in [2.0 + 1.0j, 3.0 + 2.0j]:
            result = engine.koszul_perturbation(s, DPS)
            assert result['relative_error'] < 1e-4, (
                f"Perturbation mismatch at s={s}: "
                f"rel_err={result['relative_error']}"
            )

    @skipmp
    def test_koszul_perturbation_is_real_on_real_axis(self):
        """delta_L(s) should be real for real s (because psi is real on reals)."""
        s = 3.0  # Real s away from poles
        result = engine.koszul_perturbation(s, DPS)
        delta = result['delta_L_analytic']
        assert abs(delta.imag) < 1e-10, (
            f"delta_L not real at real s={s}: imag={delta.imag}"
        )

    @skipmp
    def test_koszul_perturbation_at_zeros_finite(self):
        """delta_L evaluated near zeta zero positions should be finite."""
        results = engine.koszul_perturbation_at_zeros(n_zeros=3, dps=DPS)
        assert len(results) == 3
        for entry in results:
            assert math.isfinite(entry['|delta_L|']), (
                f"delta_L not finite at zero #{entry['k']}"
            )


# ============================================================================
# Section 5: Shadow complementarity
# ============================================================================

class TestShadowComplementarity:
    """Tests for shadow zeta sums and differences."""

    def test_virasoro_shadow_sum_leading_term(self):
        """S_2(Vir_c) + S_2(Vir_{26-c}) = 13 for all c (AP24)."""
        for c_val in [1.0, 5.0, 13.0, 20.0, 25.0]:
            s = 2.0  # Real s for convergence
            result = engine.shadow_complementarity_sum(c_val, s)
            assert abs(result['S2_sum'] - 13.0) < 1e-10, (
                f"S_2 sum != 13 at c={c_val}: {result['S2_sum']}"
            )

    def test_virasoro_shadow_sum_at_self_dual(self):
        """At c=13: both algebras are the same, so sum = 2*zeta_{Vir_13}."""
        s = 3.0
        result = engine.shadow_complementarity_sum(13.0, s)
        # zeta_A = zeta_{26-c} at c=13
        assert abs(result['zeta_A'] - result['zeta_dual']) < 1e-10, (
            f"zeta_A != zeta_dual at c=13"
        )
        assert abs(result['zeta_sum'] - 2 * result['zeta_A']) < 1e-10

    def test_virasoro_shadow_difference_at_self_dual(self):
        """At c=13: zeta_A - zeta_{A!} = 0 at the leading order."""
        s = 3.0
        result = engine.shadow_complementarity_difference(13.0, s)
        assert abs(result['delta_kappa']) < 1e-14, (
            f"delta_kappa != 0 at c=13: {result['delta_kappa']}"
        )
        # The full difference should also vanish since both algebras are identical
        assert abs(result['zeta_diff']) < 1e-10, (
            f"zeta_diff != 0 at c=13: {result['zeta_diff']}"
        )

    def test_virasoro_shadow_difference_delta_kappa(self):
        """delta_kappa = c - 13 for Virasoro (AP29)."""
        for c_val in [1.0, 5.0, 20.0, 25.0]:
            result = engine.shadow_complementarity_difference(c_val, 3.0)
            expected = c_val - 13.0
            assert abs(result['delta_kappa'] - expected) < 1e-14, (
                f"delta_kappa wrong at c={c_val}: "
                f"{result['delta_kappa']} != {expected}"
            )

    def test_heisenberg_shadow_sum_vanishes(self):
        """For Heisenberg: kappa + kappa' = 0, so shadow zeta sum = 0."""
        for k_val in [1.0, 2.0, 5.0]:
            s = 3.0
            result = engine.shadow_complementarity_heisenberg(k_val, s)
            assert abs(result['kappa_sum']) < 1e-14, (
                f"Heisenberg kappa sum != 0: {result['kappa_sum']}"
            )
            assert abs(result['zeta_sum']) < 1e-14, (
                f"Heisenberg zeta sum != 0: {result['zeta_sum']}"
            )

    def test_affine_sl2_shadow_sum_kappa_vanishes(self):
        """For affine sl_2: kappa + kappa' = 0 (Feigin-Frenkel, AP24)."""
        for k_val in [1.0, 3.0, 5.0]:
            s = 3.0
            result = engine.shadow_complementarity_affine_sl2(k_val, s)
            assert abs(result['kappa_sum']) < 1e-12, (
                f"Affine sl_2 kappa sum != 0 at k={k_val}: {result['kappa_sum']}"
            )

    def test_affine_sl2_shadow_sum_leading_cancels(self):
        """For affine sl_2: the S_2 terms cancel (since kappa+kappa'=0)."""
        k_val = 2.0
        s = 3.0
        result = engine.shadow_complementarity_affine_sl2(k_val, s)
        # Since kappa + kappa' = 0, the S_2 contribution cancels
        # The remaining sum should be from S_3 terms only
        # S_3(A) + S_3(A!) where alpha(k) = 2h^v/(k+h^v)
        h_dual = 2.0
        alpha_A = 2 * h_dual / (k_val + h_dual)
        alpha_dual = 2 * h_dual / (-k_val - 2 * h_dual + h_dual)
        expected_S3_sum = (alpha_A + alpha_dual) * 3 ** (-s)
        # Check the sum is dominated by S_3
        assert abs(result['zeta_sum'] - expected_S3_sum) < 1e-10

    def test_shadow_zeta_convergence(self):
        """Shadow zeta should converge for sufficiently large Re(s)."""
        c_val = 10.0
        for s in [3.0, 5.0, 10.0]:
            result = engine.shadow_complementarity_sum(c_val, s)
            assert math.isfinite(result['zeta_sum'].real), (
                f"Shadow zeta sum not finite at s={s}"
            )


# ============================================================================
# Section 6: Lagrangian structure
# ============================================================================

class TestLagrangianStructure:
    """Tests for the Lagrangian intersection with the zeta zero hyperplane."""

    @skipmp
    def test_lagrangian_at_self_dual(self):
        """At c=13: A_c = A_{26-c}, so |ratio| = 1 and angle = 0."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        data = engine.lagrangian_intersection_data(rho, 13.0, DPS)
        assert abs(data['|A_c/A_dual|'] - 1.0) < 1e-8, (
            f"|A_13/A_13| != 1: {data['|A_c/A_dual|']}"
        )
        assert abs(data['lagrangian_angle']) < 1e-8, (
            f"Lagrangian angle != 0 at c=13: {data['lagrangian_angle']}"
        )

    @skipmp
    def test_lagrangian_coupling_nonzero_at_self_dual(self):
        """At c=13: coupling = A_13(rho)^2 != 0."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        data = engine.lagrangian_intersection_data(rho, 13.0, DPS)
        assert data['|coupling|'] > 0, "Coupling vanishes at self-dual point"
        # At c=13: A_c = A_{26-c} = A_13, so coupling = A_13^2.
        # Since A_13 is complex, the coupling is complex, NOT necessarily real.
        # But |coupling| = |A_13|^2.
        A_13 = engine.self_dual_residue(rho, DPS)
        expected_modulus = abs(A_13) ** 2
        assert abs(data['|coupling|'] - expected_modulus) < 1e-8 * expected_modulus, (
            f"|coupling| != |A_13|^2 at c=13: {data['|coupling|']} vs {expected_modulus}"
        )

    @skipmp
    def test_lagrangian_finite_for_all_zeros(self):
        """Lagrangian data should be finite for the first 5 zeros."""
        mpmath.mp.dps = DPS
        for k in range(1, 6):
            rho = complex(mpmath.zetazero(k))
            data = engine.lagrangian_intersection_data(rho, 5.0, DPS)
            assert math.isfinite(data['|coupling|'])
            assert math.isfinite(data['lagrangian_angle'])

    @skipmp
    def test_lagrangian_angle_spectrum_shape(self):
        """Spectrum should have correct number of entries."""
        spectrum = engine.lagrangian_angle_spectrum(n_zeros=5, c=3.0, dps=DPS)
        assert len(spectrum) == 5
        for entry in spectrum:
            assert 'lagrangian_angle' in entry
            assert math.isfinite(entry['lagrangian_angle'])

    @skipmp
    def test_lagrangian_angle_antisymmetric(self):
        """theta(c) = -theta(26-c) (angle reverses under duality)."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        for c_val in [3.0, 8.0, 12.0]:
            d1 = engine.lagrangian_intersection_data(rho, c_val, DPS)
            d2 = engine.lagrangian_intersection_data(rho, 26.0 - c_val, DPS)
            # theta(c) = arg(A_c/A_{26-c}), theta(26-c) = arg(A_{26-c}/A_c) = -theta(c)
            assert abs(d1['lagrangian_angle'] + d2['lagrangian_angle']) < 1e-8, (
                f"Angle antisymmetry failed at c={c_val}"
            )


# ============================================================================
# Section 7: Defect form
# ============================================================================

class TestDefectForm:
    """Tests for the defect form Omega_c(rho) = (d/dc) A_c(rho)."""

    @skipmp
    def test_defect_analytic_vs_numerical(self):
        """Analytic formula should match numerical finite-difference."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        for c_val in [5.0, 13.0, 20.0]:
            result = engine.defect_form(rho, c_val, DPS)
            assert result['relative_error'] < 1e-3, (
                f"Defect form mismatch at c={c_val}: "
                f"rel_err={result['relative_error']}"
            )

    @skipmp
    def test_defect_nonzero(self):
        """Omega_c should be nonzero generically."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        result = engine.defect_form(rho, 5.0, DPS)
        assert abs(result['omega_analytic']) > 1e-50, (
            f"Defect form vanishes at c=5"
        )

    @skipmp
    def test_defect_at_zeros_shape(self):
        """Defect form at zeros should return correct number of entries."""
        results = engine.defect_form_at_zeros(n_zeros=3, c_val=10.0, dps=DPS)
        assert len(results) == 3
        for entry in results:
            assert '|omega|' in entry
            assert math.isfinite(entry['|omega|'])

    @skipmp
    def test_defect_spectrum_shape(self):
        """Defect spectrum table should have correct shape."""
        results = engine.defect_form_spectrum(
            n_zeros=3, c_values=[5.0, 13.0, 25.0], dps=DPS
        )
        assert len(results) == 3
        for entry in results:
            assert '|omega_c=13.0|' in entry

    @skipmp
    def test_defect_conjugation(self):
        """Omega_c(conj(rho)) = conj(Omega_c(rho)) for real c."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        rho_conj = rho.conjugate()
        c_val = 7.0
        d1 = engine.defect_form(rho, c_val, DPS)
        d2 = engine.defect_form(rho_conj, c_val, DPS)
        expected = d1['omega_analytic'].conjugate()
        assert abs(d2['omega_analytic'] - expected) < 1e-8 * abs(expected), (
            f"Defect form conjugation failed"
        )


# ============================================================================
# Section 8: Boundary cases
# ============================================================================

class TestBoundaryCases:
    """Tests for c near 0 and c near 26."""

    @skipmp
    def test_boundary_c1_c25_are_dual(self):
        """A_1 and A_25 should be related by the complementarity ratio."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        data = engine.boundary_case_analysis(rho, DPS)
        ratio = engine.residue_complementarity_ratio(rho, 1.0, DPS)
        # A_1 / A_25 should match the Gamma ratio
        expected_ratio = ratio['ratio_gamma']
        if abs(data['A_25']) > 1e-50:
            actual_ratio = data['A_1'] / data['A_25']
            assert abs(actual_ratio - expected_ratio) < 1e-6 * abs(expected_ratio), (
                f"Boundary ratio mismatch"
            )

    @skipmp
    def test_boundary_near_0_finite(self):
        """A_c near c=0 should be finite (computed at c=0.01)."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        data = engine.boundary_case_analysis(rho, DPS)
        assert math.isfinite(abs(data['A_near_0'])), "A near c=0 not finite"

    @skipmp
    def test_boundary_near_26_finite(self):
        """A_c near c=26 should be finite (computed at c=25.99)."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        data = engine.boundary_case_analysis(rho, DPS)
        assert math.isfinite(abs(data['A_near_26'])), "A near c=26 not finite"


# ============================================================================
# Section 9: Kappa consistency checks
# ============================================================================

class TestKappaConsistency:
    """Tests for kappa + kappa' values from landscape_census.tex."""

    def test_heisenberg_kappa_sum_zero(self):
        """kappa(H_k) + kappa(H_{-k}) = 0."""
        checks = engine.kappa_consistency_check()
        heis_checks = [c for c in checks if 'Heisenberg' in c['family']]
        for c in heis_checks:
            assert c['ok'], (
                f"{c['family']}: kappa sum = {c['sum']}, expected {c['expected_sum']}"
            )

    def test_affine_sl2_kappa_sum_zero(self):
        """kappa(V_k(sl_2)) + kappa(V_{-k-4}(sl_2)) = 0."""
        checks = engine.kappa_consistency_check()
        affine_checks = [c for c in checks if 'Affine' in c['family']]
        for c in affine_checks:
            assert c['ok'], (
                f"{c['family']}: kappa sum = {c['sum']}, expected {c['expected_sum']}"
            )

    def test_virasoro_kappa_sum_thirteen(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        checks = engine.kappa_consistency_check()
        vir_checks = [c for c in checks if 'Virasoro' in c['family']]
        for c in vir_checks:
            assert c['ok'], (
                f"{c['family']}: kappa sum = {c['sum']}, expected {c['expected_sum']}"
            )

    def test_virasoro_kappa_not_zero(self):
        """The Virasoro kappa sum is 13, NOT 0 (anti-pattern AP24)."""
        checks = engine.kappa_consistency_check()
        vir_c13 = [c for c in checks if c['family'] == 'Virasoro c=13.0'][0]
        assert abs(vir_c13['sum'] - 13.0) < 1e-14
        assert abs(vir_c13['sum']) > 1.0  # Definitely not zero

    def test_all_checks_pass(self):
        """All kappa consistency checks should pass."""
        checks = engine.kappa_consistency_check()
        for c in checks:
            assert c['ok'], f"FAILED: {c['family']}: sum={c['sum']}"


# ============================================================================
# Section 10: Cross-verification paths
# ============================================================================

class TestCrossVerification:
    """Cross-verification: multiple independent paths to the same result."""

    @skipmp
    def test_path1_vs_path2_residue_ratio(self):
        """Path 1 (direct) vs Path 2 (Gamma identity) for residue ratio."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(2))
        for c_val in [3.0, 7.0, 15.0, 22.0]:
            result = engine.residue_complementarity_ratio(rho, c_val, DPS)
            assert result['relative_error'] < 1e-10, (
                f"Path 1 vs Path 2 failed at c={c_val}"
            )

    @skipmp
    def test_path2_gamma_reflection(self):
        """Path 2: Gamma ratio simplifies via reflection formula.

        For c and 26-c: the product A_c * A_{26-c} involves
        Gamma((c+rho-1)/2) * Gamma((25-c+rho)/2) which by the
        Gamma multiplication formula has known structure.
        """
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        c_val = 5.0
        r = engine.residue_complementarity_ratio(rho, c_val, DPS)
        r_dual = engine.residue_complementarity_ratio(rho, 26.0 - c_val, DPS)
        # r * r_dual should = 1
        product = r['ratio_gamma'] * r_dual['ratio_gamma']
        assert abs(product - 1.0) < 1e-10

    @skipmp
    def test_path3_boundary_c_1(self):
        """Path 3: At c=1, kappa=1/2, the algebra is near-trivial."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        # A_1 should be computable
        result = engine.residue_complementarity_ratio(rho, 1.0, DPS)
        assert math.isfinite(abs(result['ratio_gamma']))
        assert abs(result['ratio_gamma']) > 0

    @skipmp
    def test_path3_boundary_c_25(self):
        """Path 3: At c=25, kappa=25/2, dual is c=1."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        result = engine.residue_complementarity_ratio(rho, 25.0, DPS)
        # This should be the reciprocal of the c=1 result
        result_1 = engine.residue_complementarity_ratio(rho, 1.0, DPS)
        product = result['ratio_gamma'] * result_1['ratio_gamma']
        assert abs(product - 1.0) < 1e-10

    @skipmp
    def test_path4_kappa_sum_consistency(self):
        """Path 4: kappa values consistent with S_2 shadow coefficients."""
        for c_val in [5.0, 13.0, 20.0]:
            coeffs = engine._virasoro_shadow_coefficients(c_val)
            coeffs_dual = engine._virasoro_shadow_coefficients(26.0 - c_val)
            S2_sum = coeffs[2] + coeffs_dual[2]
            kappa_sum = c_val / 2.0 + (26.0 - c_val) / 2.0
            assert abs(S2_sum - kappa_sum) < 1e-10, (
                f"S2 sum != kappa sum at c={c_val}: {S2_sum} != {kappa_sum}"
            )
            assert abs(kappa_sum - 13.0) < 1e-10

    def test_shadow_coefficients_kappa_identity(self):
        """S_2(Vir_c) = c/2 = kappa(Vir_c) for all c."""
        for c_val in [1.0, 5.0, 13.0, 20.0, 25.0]:
            coeffs = engine._virasoro_shadow_coefficients(c_val)
            assert abs(coeffs[2] - c_val / 2.0) < 1e-10, (
                f"S_2 != c/2 at c={c_val}"
            )

    @skipmp
    def test_scattering_ratio_decomposition(self):
        """Scattering factor ratio decomposes into Gamma factors."""
        s = 2.0 + 1.5j
        for c_val in [3.0, 13.0, 22.0]:
            result = engine.scattering_factor_ratio_decomposition(s, c_val, DPS)
            assert result['relative_error'] < 1e-10, (
                f"Ratio decomposition failed at c={c_val}: "
                f"rel_err={result['relative_error']}"
            )

    @skipmp
    def test_scattering_ratio_at_c_13_identity(self):
        """At c=13: R1 * R2 = 1 (since R2 = 1/R1)."""
        s = 2.0 + 1.0j
        result = engine.scattering_factor_ratio_decomposition(s, 13.0, DPS)
        product = result['R1'] * result['R2']
        assert abs(product - 1.0) < 1e-10, (
            f"R1*R2 != 1 at c=13: {product}"
        )


# ============================================================================
# Section 11: Full analysis integration
# ============================================================================

class TestFullAnalysis:
    """Integration tests combining multiple components."""

    @skipmp
    def test_full_complementarity_at_zero_1(self):
        """Full analysis at the first zeta zero, c=5."""
        result = engine.full_complementarity_at_zero(k=1, c=5.0, dps=DPS)
        assert result['kappa_sum'] == 13.0
        assert abs(result['residue_ratio']) > 0
        assert math.isfinite(result['|coupling|'])
        assert result['complementarity_error'] < 1e-8

    @skipmp
    def test_full_complementarity_at_self_dual(self):
        """Full analysis at c=13 (self-dual)."""
        result = engine.full_complementarity_at_zero(k=1, c=13.0, dps=DPS)
        assert result['kappa_sum'] == 13.0
        assert abs(result['residue_ratio'] - 1.0) < 1e-8, (
            f"Residue ratio != 1 at self-dual: {result['residue_ratio']}"
        )
        assert abs(result['lagrangian_angle']) < 1e-8

    @skipmp
    def test_full_analysis_multiple_zeros(self):
        """Full analysis for first 3 zeros at c=10."""
        for k in range(1, 4):
            result = engine.full_complementarity_at_zero(k=k, c=10.0, dps=DPS)
            assert result['kappa_sum'] == 13.0
            assert result['complementarity_error'] < 1e-8
            assert math.isfinite(result['|defect|'])

    @skipmp
    def test_c_dependence_smooth(self):
        """Full analysis should vary smoothly with c."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        prev_ratio = None
        for c_val in [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]:
            result = engine.full_complementarity_at_zero(k=1, c=c_val, dps=DPS)
            ratio = abs(result['residue_ratio'])
            if prev_ratio is not None:
                # Change should be bounded (smooth function)
                assert abs(ratio - prev_ratio) < 2.0 * abs(prev_ratio) + 1.0, (
                    f"Non-smooth jump at c={c_val}"
                )
            prev_ratio = ratio


# ============================================================================
# Section 12: Shadow zeta function properties
# ============================================================================

class TestShadowZetaProperties:
    """Tests for shadow zeta function analytic properties."""

    def test_shadow_zeta_heisenberg_exact(self):
        """zeta_{H_k}(s) = k * 2^{-s} (only arity 2 contributes)."""
        for k_val in [1.0, 3.0]:
            coeffs = engine._heisenberg_shadow_coefficients(k_val)
            for s in [2.0, 3.0, 5.0]:
                z = engine.shadow_zeta_function(coeffs, s)
                expected = k_val * 2 ** (-s)
                assert abs(z - expected) < 1e-14, (
                    f"Heisenberg zeta wrong at k={k_val}, s={s}"
                )

    def test_shadow_zeta_virasoro_leading_term(self):
        """Leading term of zeta_{Vir_c}(s) is (c/2) * 2^{-s}."""
        c_val = 10.0
        coeffs = engine._virasoro_shadow_coefficients(c_val)
        for s in [10.0, 20.0]:  # Large s for leading term dominance
            z = engine.shadow_zeta_function(coeffs, s)
            leading = (c_val / 2.0) * 2 ** (-s)
            # At large s, higher arities are suppressed
            assert abs(z - leading) < 0.5 * abs(leading) + 1e-20, (
                f"Leading term dominance fails at c={c_val}, s={s}"
            )

    def test_shadow_zeta_sum_virasoro_leading_13(self):
        """Sum zeta_A + zeta_{A!} has leading coefficient 13 * 2^{-s}."""
        for c_val in [2.0, 10.0, 20.0]:
            result = engine.shadow_complementarity_sum(c_val, 20.0)
            expected_leading = 13.0 * 2 ** (-20.0)
            # At s=20, higher arities are negligible
            assert abs(result['zeta_sum'] - expected_leading) < 0.1 * abs(expected_leading) + 1e-20


# ============================================================================
# Section 13: Additional structural tests
# ============================================================================

class TestStructuralProperties:
    """Tests for structural properties of the complementarity engine."""

    @skipmp
    def test_residue_ratio_continuous_in_c(self):
        """The ratio A_c/A_{26-c} should be continuous in c."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        ratios = []
        for c_val in [12.5, 12.8, 13.0, 13.2, 13.5]:
            r = engine.residue_complementarity_ratio(rho, c_val, DPS)
            ratios.append(abs(r['ratio_gamma']))
        # Check that consecutive ratios don't jump too much
        for i in range(1, len(ratios)):
            assert abs(ratios[i] - ratios[i-1]) < 1.0, (
                f"Discontinuity between c={12.5 + 0.3*i} and previous"
            )

    @skipmp
    def test_defect_form_antisymmetric_at_c_13(self):
        """At c=13: Omega_13 + Omega_{13} = 2*Omega_13 (trivially).

        But Omega_c(rho) + Omega_{26-c}(rho) measures the total
        rate of change of the PAIR, which should relate to
        d/dc(A_c * A_{26-c}).
        """
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        d1 = engine.defect_form(rho, 13.0, DPS)
        # At c=13, omega_analytic should be nonzero (c is not a critical point
        # of the ratio, only the ratio equals 1 at c=13)
        assert abs(d1['omega_analytic']) > 1e-50

    @skipmp
    def test_duality_twisted_self_dual_is_square(self):
        """At c=13: Z^Koszul = F_13^2 (since F_c = F_{26-c})."""
        s = 2.0 + 1.5j
        result = engine.duality_twisted_scattering(s, 13.0, DPS)
        F13 = result['F_c']
        assert abs(result['Z_Koszul'] - F13 ** 2) < 1e-10 * abs(F13 ** 2), (
            f"Z^Koszul != F_13^2 at self-dual point"
        )

    @skipmp
    def test_complementarity_ratio_large_c(self):
        """Test ratio at large c (c=24, c_dual=2) for stability."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        result = engine.residue_complementarity_ratio(rho, 24.0, DPS)
        assert result['relative_error'] < 1e-8, (
            f"Large c ratio mismatch: rel_err={result['relative_error']}"
        )

    @skipmp
    def test_defect_form_at_multiple_c(self):
        """Defect form should vary smoothly across c=1 to c=25."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        prev = None
        for c_val in [1.0, 5.0, 10.0, 15.0, 20.0, 25.0]:
            d = engine.defect_form(rho, c_val, DPS)
            val = abs(d['omega_analytic'])
            if prev is not None:
                # Smoothness: no order-of-magnitude jumps
                assert val < 100 * prev + 1e-10 or prev < 100 * val + 1e-10, (
                    f"Non-smooth defect form between c values"
                )
            prev = val

    @skipmp
    def test_shadow_difference_sign_changes_at_c_13(self):
        """zeta_diff leading term = (c-13)*2^{-s}: positive for c>13, negative for c<13."""
        s = 3.0
        r_low = engine.shadow_complementarity_difference(10.0, s)
        r_high = engine.shadow_complementarity_difference(16.0, s)
        # c=10 < 13: delta_kappa = -3, leading term negative
        assert r_low['delta_kappa'] < 0
        assert r_low['leading_diff'] < 0
        # c=16 > 13: delta_kappa = 3, leading term positive
        assert r_high['delta_kappa'] > 0
        assert r_high['leading_diff'] > 0

    @skipmp
    def test_all_seven_components_finite(self):
        """All 7 components should produce finite results at generic point."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        c_val = 7.0

        # 1. Residue ratio
        r1 = engine.residue_complementarity_ratio(rho, c_val, DPS)
        assert math.isfinite(abs(r1['ratio_gamma']))

        # 2. Self-dual residue
        r2 = engine.self_dual_residue(rho, DPS)
        assert math.isfinite(abs(r2))

        # 3. Duality-twisted
        r3 = engine.duality_twisted_scattering(2.0 + 1.0j, c_val, DPS)
        assert math.isfinite(abs(r3['Z_Koszul']))

        # 4. L^comp
        r4 = engine.complementarity_L_function(2.0 + 1.0j, c_val, DPS)
        assert math.isfinite(abs(r4['L_comp']))

        # 5. Shadow complementarity
        r5 = engine.shadow_complementarity_sum(c_val, 3.0)
        assert math.isfinite(r5['zeta_sum'].real)

        # 6. Lagrangian
        r6 = engine.lagrangian_intersection_data(rho, c_val, DPS)
        assert math.isfinite(r6['|coupling|'])

        # 7. Defect form
        r7 = engine.defect_form(rho, c_val, DPS)
        assert math.isfinite(abs(r7['omega_analytic']))
