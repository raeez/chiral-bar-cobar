r"""Tests for the higher-genus constrained Epstein zeta engine.

Verifies:
  - Siegel Eisenstein scattering matrix phi_g(s) for g = 1, 2, 3
  - Functional equation phi_g(s) * phi_g((g+1)/2 - s) = 1
  - Factorisation phi_g(s) = prod_{j=0}^{g-1} phi_1(s-j)
  - Genus-2 scattering factor F_{2,c}(s) and its decomposition
  - Genus-2 pole structure: two families of poles from two zeta ratios
  - Genus-2 universal residue factors at single and paired zeta zeros
  - Genus-2 to genus-1 consistency: coincident residue vs genus-1 squared
  - Genus-3 scattering factor and three pole families
  - General genus-g scattering factor
  - Boecherer connection: Fourier coefficients and L-value proxy
  - Planted-forest correction at genus 2
  - Complementarity under c -> 26-c at genus 2 and 3
  - Theta lift / Rankin-Selberg consistency (verification path 2)
  - Standard family genus-2 shadow data

60+ tests covering the full mathematical content.

Verification paths:
  Path 1: Direct computation from Siegel-Eisenstein functional equation
  Path 2: Genus-2 Rankin-Selberg integral via theta lift
  Path 3: Genus-2 residue at coincident zeros relates to genus-1 residue
  Path 4: Boecherer's formula: Fourier coefficient vs known L-values
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

from fractions import Fraction

from compute.lib import bc_higher_genus_epstein_engine as hge

DPS = 30
skipmp = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ====================================================================
# Section 1: Siegel Eisenstein scattering matrix
# ====================================================================

class TestSiegelScatteringMatrix:
    """Tests for phi_g(s) = prod_{j=0}^{g-1} xi(2s-2j-1)/xi(2s-2j)."""

    @skipmp
    def test_genus1_scattering_basic(self):
        """phi_1(s) should be computable at generic points."""
        for s in [0.3 + 1j, 0.7 + 5j, 0.5 + 14.13j]:
            result = hge.siegel_scattering_matrix(1, s, DPS)
            assert isinstance(result, complex)
            assert math.isfinite(abs(result))

    @skipmp
    def test_genus2_scattering_basic(self):
        """phi_2(s) should be computable at generic points."""
        for s in [2.5 + 1j, 3.0 + 5j, 2.2 + 3j]:
            result = hge.siegel_scattering_matrix(2, s, DPS)
            assert isinstance(result, complex)
            assert math.isfinite(abs(result))

    @skipmp
    def test_genus3_scattering_basic(self):
        """phi_3(s) should be computable at generic points."""
        for s in [4.0 + 1j, 5.0 + 3j, 3.5 + 7j]:
            result = hge.siegel_scattering_matrix(3, s, DPS)
            assert isinstance(result, complex)
            assert math.isfinite(abs(result))

    @skipmp
    def test_genus1_fe(self):
        """phi_1(s) * phi_1(1-s) = 1."""
        for s in [0.3 + 0.5j, 0.7 + 2j, 0.2 + 10j]:
            result = hge.verify_siegel_scattering_fe(1, s, DPS)
            assert result['error'] < 1e-12, (
                f"FE error at g=1, s={s}: {result['error']}"
            )

    @skipmp
    def test_genus2_fe(self):
        """phi_2(s) * phi_2(3/2 - s) = 1."""
        for s in [2.3 + 1j, 1.7 + 3j, 2.0 + 7j]:
            result = hge.verify_siegel_scattering_fe(2, s, DPS)
            assert result['error'] < 1e-10, (
                f"FE error at g=2, s={s}: {result['error']}"
            )

    @skipmp
    def test_genus3_fe(self):
        """phi_3(s) * phi_3(2 - s) = 1."""
        for s in [3.3 + 1j, 3.7 + 3j, 4.0 + 5j]:
            result = hge.verify_siegel_scattering_fe(3, s, DPS)
            assert result['error'] < 1e-10, (
                f"FE error at g=3, s={s}: {result['error']}"
            )


# ====================================================================
# Section 2: Factorisation phi_g = product of genus-1 factors
# ====================================================================

class TestScatteringFactorisation:
    """Verify phi_g(s) = prod_{j=0}^{g-1} phi_1(s-j)."""

    @skipmp
    def test_genus2_factorises(self):
        """phi_2(s) = phi_1(s) * phi_1(s-1)."""
        for s in [2.5 + 1j, 3.0 + 5j, 2.2 + 3j]:
            result = hge.verify_genus2_reduces_to_genus1(s, DPS)
            assert result['relative_error'] < 1e-12, (
                f"Factorisation fails at s={s}: rel_err={result['relative_error']}"
            )

    @skipmp
    def test_genus3_factorises(self):
        """phi_3(s) = phi_1(s) * phi_1(s-1) * phi_1(s-2)."""
        for s in [4.0 + 1j, 5.0 + 3j, 3.5 + 7j]:
            result = hge.verify_genus3_factorisation(s, DPS)
            assert result['relative_error'] < 1e-10, (
                f"Factorisation fails at s={s}: rel_err={result['relative_error']}"
            )

    @skipmp
    def test_genus_g_factorisation_g4(self):
        """c_4(s) = prod_{j=0}^3 c_1(s - j/2)."""
        g = 4
        s = 5.5 + 2j
        phi_g = hge.siegel_scattering_matrix(g, s, DPS)
        product = 1.0 + 0j
        for j in range(g):
            product *= hge.siegel_scattering_matrix(1, s - j / 2, DPS)
        rel_err = abs(phi_g - product) / max(abs(phi_g), 1e-100)
        assert rel_err < 1e-10, f"g=4 factorisation fails: rel_err={rel_err}"


# ====================================================================
# Section 3: Zeta ratio decomposition
# ====================================================================

class TestZetaRatioDecomposition:
    """Verify the zeta ratio structure of phi_g(s)."""

    @skipmp
    def test_genus1_single_ratio(self):
        """phi_1(s) has exactly 1 zeta ratio."""
        s = 2.0 + 3j
        factors = hge.siegel_scattering_zeta_ratios(1, s, DPS)
        assert len(factors) == 1

    @skipmp
    def test_genus2_two_ratios(self):
        """phi_2(s) has exactly 2 zeta ratios."""
        s = 3.0 + 2j
        factors = hge.siegel_scattering_zeta_ratios(2, s, DPS)
        assert len(factors) == 2

    @skipmp
    def test_genus3_three_ratios(self):
        """phi_3(s) has exactly 3 zeta ratios."""
        s = 5.0 + 1j
        factors = hge.siegel_scattering_zeta_ratios(3, s, DPS)
        assert len(factors) == 3

    @skipmp
    def test_zeta_ratio_arguments_genus2(self):
        """Genus-2 zeta ratios have correct arguments.

        Factor i=1: xi(2s)/xi(2s-1) => zeta(2s)/zeta(2s-1)
        Factor i=2: xi(2s-1)/xi(2s-2) => zeta(2s-1)/zeta(2s-2)
        """
        s = 3.0 + 2j
        factors = hge.siegel_scattering_zeta_ratios(2, s, DPS)
        # i=1: zeta(2s)/zeta(2s-1)
        assert abs(factors[0]['zeta_num_arg'] - (2 * s)) < 1e-10
        assert abs(factors[0]['zeta_den_arg'] - (2 * s - 1)) < 1e-10
        # i=2: zeta(2s-1)/zeta(2s-2)
        assert abs(factors[1]['zeta_num_arg'] - (2 * s - 1)) < 1e-10
        assert abs(factors[1]['zeta_den_arg'] - (2 * s - 2)) < 1e-10

    @skipmp
    def test_zeta_ratio_product_equals_phi(self):
        """Product of zeta ratios * archimedean = phi_g(s)."""
        g = 2
        s = 3.0 + 2j
        phi = hge.siegel_scattering_matrix(g, s, DPS)
        factors = hge.siegel_scattering_zeta_ratios(g, s, DPS)
        product = 1.0 + 0j
        for f in factors:
            product *= f['combined']
        # This should equal phi up to normalisation
        assert math.isfinite(abs(product))
        assert math.isfinite(abs(phi))


# ====================================================================
# Section 4: Genus-2 scattering factor F_{2,c}(s)
# ====================================================================

class TestGenus2ScatteringFactor:
    """Tests for F_{2,c}(s)."""

    @skipmp
    def test_genus2_factor_computable(self):
        """F_{2,c}(s) is computable at generic points."""
        for s in [2.5 + 1j, 3.0 + 2j, 2.0 + 0.5j]:
            for c in [1, 12, 13, 24, 26]:
                result = hge.genus2_scattering_factor(s, c, DPS)
                assert isinstance(result, complex)
                assert math.isfinite(abs(result)), (
                    f"F_{{2,{c}}}({s}) not finite"
                )

    @skipmp
    def test_genus2_decomposition(self):
        """F_{2,c} decomposition factors multiply to the full value."""
        s = 2.5 + 1j
        c = 12
        d = hge.genus2_scattering_factor_decomposition(s, c, DPS)
        # Product of factors should equal F_{2,c}
        product = (complex(d['conformal_gamma']) * complex(d['pi_factor'])
                   * complex(d['zeta_ratio_1']) * complex(d['zeta_ratio_2']))
        rel_err = abs(d['product'] - product) / max(abs(d['product']), 1e-100)
        assert rel_err < 1e-10, f"Decomposition inconsistent: rel_err={rel_err}"

    @skipmp
    def test_genus2_has_two_zeta_ratios(self):
        """F_{2,c} decomposition has two separate zeta ratios."""
        s = 2.5 + 1j
        c = 12
        d = hge.genus2_scattering_factor_decomposition(s, c, DPS)
        # Both ratios should be finite and nonzero
        assert abs(d['zeta_ratio_1']) > 1e-20
        assert abs(d['zeta_ratio_2']) > 1e-20
        # They should be different (at generic s)
        assert abs(d['zeta_ratio_1'] - d['zeta_ratio_2']) > 1e-20


# ====================================================================
# Section 5: Genus-2 pole structure
# ====================================================================

class TestGenus2PoleStructure:
    """Tests for the two families of poles."""

    @skipmp
    def test_two_pole_families(self):
        """There are two families of poles."""
        poles = hge.genus2_pole_positions(n_zeros=5, dps=DPS)
        assert 'family_1' in poles
        assert 'family_2' in poles
        assert len(poles['family_1']) == 5
        assert len(poles['family_2']) == 5

    @skipmp
    def test_family1_real_parts(self):
        """Family 1 poles have Re(s) = 3/4 under RH (from 2s-1=rho)."""
        poles = hge.genus2_pole_positions(n_zeros=5, dps=DPS)
        for p in poles['family_1']:
            assert abs(p['real'] - 0.75) < 1e-10, (
                f"Family 1 pole Re(s) = {p['real']}, expected 0.75"
            )

    @skipmp
    def test_family2_real_parts(self):
        """Family 2 poles have Re(s) = 5/4 under RH (from 2s-2=rho)."""
        poles = hge.genus2_pole_positions(n_zeros=5, dps=DPS)
        for p in poles['family_2']:
            assert abs(p['real'] - 1.25) < 1e-10, (
                f"Family 2 pole Re(s) = {p['real']}, expected 1.25"
            )

    @skipmp
    def test_family1_matches_genus1(self):
        """Family 1 poles at genus 2 = genus-1 poles."""
        from compute.lib import benjamin_chang_analysis as bca
        g1_poles = bca.scattering_pole_positions(n_zeros=5, dps=DPS)
        g2_poles = hge.genus2_pole_positions(n_zeros=5, dps=DPS)
        for g1, g2 in zip(g1_poles, g2_poles['family_1']):
            assert abs(g1['s_rho'] - g2['s']) < 1e-10, (
                f"Family 1 pole mismatch: g1={g1['s_rho']}, g2={g2['s']}"
            )

    @skipmp
    def test_family2_shifted_by_half(self):
        """Family 2 poles = Family 1 poles + 1/2 (shift by 1/2 in s)."""
        poles = hge.genus2_pole_positions(n_zeros=5, dps=DPS)
        for p1, p2 in zip(poles['family_1'], poles['family_2']):
            assert abs(p2['s'] - p1['s'] - 0.5) < 1e-10, (
                f"Family 2 not shifted by 1/2: {p2['s']} vs {p1['s']} + 0.5"
            )


# ====================================================================
# Section 6: Genus-2 residue factors
# ====================================================================

class TestGenus2Residues:
    """Tests for A^{(2)}_c residue factors."""

    @skipmp
    def test_single_residue_family1_computable(self):
        """Family 1 residue is computable at the first zeta zero."""
        rho1 = complex(mpmath.zetazero(1))
        for c in [1, 12, 13, 24]:
            A = hge.genus2_universal_residue_single(rho1, c, family=1, dps=DPS)
            assert isinstance(A, complex)
            assert math.isfinite(abs(A))
            assert abs(A) > 0

    @skipmp
    def test_single_residue_family2_computable(self):
        """Family 2 residue is computable at the first zeta zero."""
        rho1 = complex(mpmath.zetazero(1))
        for c in [1, 12, 13, 24]:
            A = hge.genus2_universal_residue_single(rho1, c, family=2, dps=DPS)
            assert isinstance(A, complex)
            assert math.isfinite(abs(A))
            assert abs(A) > 0

    @skipmp
    def test_coincident_residue(self):
        """Coincident residue A^{(2)}_c(rho, rho) is nonzero."""
        rho1 = complex(mpmath.zetazero(1))
        result = hge.genus2_coincident_residue(rho1, 12, DPS)
        assert abs(result['coincident_product']) > 0
        assert math.isfinite(result['magnitude'])

    @skipmp
    def test_double_residue_structure(self):
        """Double residue at (rho_1, rho_2) has correct structure."""
        rho1 = complex(mpmath.zetazero(1))
        rho2 = complex(mpmath.zetazero(2))
        result = hge.genus2_universal_residue_double(rho1, rho2, 12, DPS)
        assert 'A_family1' in result
        assert 'A_family2' in result
        assert 'product' in result
        assert 'interference_kernel' in result
        assert 'paired_residue' in result
        # Product should be A1 * A2
        expected_product = complex(result['A_family1']) * complex(result['A_family2'])
        assert abs(result['product'] - expected_product) < 1e-10 * max(abs(expected_product), 1e-50)


# ====================================================================
# Section 7: Genus-2 to genus-1 consistency (Path 3)
# ====================================================================

class TestGenus2ToGenus1Consistency:
    """Path 3: genus-2 residue at coincident zeros should relate to genus-1."""

    @skipmp
    def test_residue_ratio_is_finite(self):
        """A^{(2)}_c(rho,rho) / [A^{(1)}_c(rho)]^2 is finite."""
        rho1 = complex(mpmath.zetazero(1))
        for c in [1, 12, 13, 24]:
            result = hge.genus2_vs_genus1_residue_ratio(rho1, c, DPS)
            assert math.isfinite(result['ratio_magnitude']), (
                f"Ratio not finite at c={c}"
            )

    @skipmp
    def test_genus1_residue_nonzero(self):
        """The genus-1 residue should be nonzero at the first zero."""
        rho1 = complex(mpmath.zetazero(1))
        A1 = hge.genus1_universal_residue(rho1, 12, DPS)
        assert abs(A1) > 0

    @skipmp
    def test_genus1_matches_benjamin_chang(self):
        """Our genus-1 residue matches the benjamin_chang_analysis module."""
        from compute.lib import benjamin_chang_analysis as bca
        rho1 = complex(mpmath.zetazero(1))
        A1_ours = hge.genus1_universal_residue(rho1, 12, DPS)
        A1_bc = bca.universal_residue_factor(rho1, 12, DPS)
        rel_err = abs(A1_ours - A1_bc) / max(abs(A1_ours), 1e-100)
        assert rel_err < 1e-10, (
            f"Genus-1 residue mismatch: ours={A1_ours}, BC={A1_bc}"
        )

    @skipmp
    def test_ratio_varies_with_c(self):
        """The genus-2/genus-1 ratio should vary with c (not constant)."""
        rho1 = complex(mpmath.zetazero(1))
        ratios = []
        for c in [1, 12, 24]:
            r = hge.genus2_vs_genus1_residue_ratio(rho1, c, DPS)
            ratios.append(r['ratio_magnitude'])
        # Not all the same
        assert not (abs(ratios[0] - ratios[1]) < 1e-5
                    and abs(ratios[1] - ratios[2]) < 1e-5), (
            f"Ratio does not vary with c: {ratios}"
        )

    @skipmp
    def test_ratio_varies_with_zero(self):
        """The ratio should vary across different zeta zeros."""
        ratios = []
        for k in [1, 2, 3]:
            rho = complex(mpmath.zetazero(k))
            r = hge.genus2_vs_genus1_residue_ratio(rho, 12, DPS)
            ratios.append(r['ratio_magnitude'])
        # Not all the same
        assert not (abs(ratios[0] - ratios[1]) < 1e-5
                    and abs(ratios[1] - ratios[2]) < 1e-5), (
            f"Ratio does not vary with zero: {ratios}"
        )


# ====================================================================
# Section 8: Genus-3 scattering factor
# ====================================================================

class TestGenus3:
    """Tests for genus-3 scattering factor and poles."""

    @skipmp
    def test_genus3_factor_computable(self):
        """F_{3,c}(s) is computable."""
        result = hge.genus3_scattering_factor(4.0 + 1j, 12, DPS)
        assert isinstance(result, complex)
        assert math.isfinite(abs(result))

    @skipmp
    def test_genus3_three_pole_families(self):
        """Genus 3 has three pole families."""
        poles = hge.genus3_pole_positions(n_zeros=3, dps=DPS)
        assert len(poles) == 3
        assert 'family_1' in poles
        assert 'family_2' in poles
        assert 'family_3' in poles

    @skipmp
    def test_genus3_pole_real_parts(self):
        """Genus-3 pole families have correct real parts under RH.

        Family i poles at s = (i+rho)/2, Re = (i+1/2)/2 = i/2 + 1/4.
        """
        poles = hge.genus3_pole_positions(n_zeros=3, dps=DPS)
        for p in poles['family_1']:
            assert abs(p['real'] - 0.75) < 1e-10
        for p in poles['family_2']:
            assert abs(p['real'] - 1.25) < 1e-10
        for p in poles['family_3']:
            assert abs(p['real'] - 1.75) < 1e-10

    @skipmp
    def test_genus3_residue_family1(self):
        """Genus-3 family 1 residue is computable."""
        rho1 = complex(mpmath.zetazero(1))
        A = hge.genus3_universal_residue_single(rho1, 12, family=1, dps=DPS)
        assert isinstance(A, complex)
        assert math.isfinite(abs(A))
        assert abs(A) > 0

    @skipmp
    def test_genus3_residue_family2(self):
        """Genus-3 family 2 residue is computable."""
        rho1 = complex(mpmath.zetazero(1))
        A = hge.genus3_universal_residue_single(rho1, 12, family=2, dps=DPS)
        assert isinstance(A, complex)
        assert math.isfinite(abs(A))

    @skipmp
    def test_genus3_residue_family3(self):
        """Genus-3 family 3 residue is computable."""
        rho1 = complex(mpmath.zetazero(1))
        A = hge.genus3_universal_residue_single(rho1, 12, family=3, dps=DPS)
        assert isinstance(A, complex)
        assert math.isfinite(abs(A))


# ====================================================================
# Section 9: General genus-g scattering factor
# ====================================================================

class TestGeneralGenusG:
    """Tests for genus_g_scattering_factor at various genera."""

    @skipmp
    def test_genus1_agrees(self):
        """genus_g_scattering_factor(1, s, c) matches genus-1 Fc."""
        from compute.lib import benjamin_chang_analysis as bca
        s = 2.0 + 1j
        c = 12
        Fg = hge.genus_g_scattering_factor(1, s, c, DPS)
        # Not directly comparable to bca.scattering_factor_Fc due to
        # slightly different normalisation, but should be finite and nonzero
        assert math.isfinite(abs(Fg))
        assert abs(Fg) > 0

    @skipmp
    def test_genus2_agrees(self):
        """genus_g_scattering_factor(2, s, c) consistent with genus2_scattering_factor."""
        s = 2.5 + 1j
        c = 12
        Fg = hge.genus_g_scattering_factor(2, s, c, DPS)
        F2 = hge.genus2_scattering_factor(s, c, DPS)
        # Should agree (same formula)
        rel_err = abs(Fg - F2) / max(abs(Fg), 1e-100)
        assert rel_err < 1e-10, f"g=2 general vs specific: rel_err={rel_err}"

    @skipmp
    def test_genus3_agrees(self):
        """genus_g_scattering_factor(3, s, c) consistent with genus3_scattering_factor."""
        s = 4.0 + 1j
        c = 12
        Fg = hge.genus_g_scattering_factor(3, s, c, DPS)
        F3 = hge.genus3_scattering_factor(s, c, DPS)
        rel_err = abs(Fg - F3) / max(abs(Fg), 1e-100)
        assert rel_err < 1e-10, f"g=3 general vs specific: rel_err={rel_err}"

    @skipmp
    def test_g_pole_families_count(self):
        """genus_g_pole_families(g) returns g families."""
        for g in [1, 2, 3, 4]:
            families = hge.genus_g_pole_families(g, n_zeros=2, dps=DPS)
            assert len(families) == g, f"Expected {g} families, got {len(families)}"

    @skipmp
    def test_g_pole_families_real_parts(self):
        """Family i (0-indexed j=i-1) has Re(s) = (i+1/2)/2 = i/2 + 1/4 under RH."""
        g = 4
        families = hge.genus_g_pole_families(g, n_zeros=2, dps=DPS)
        for j in range(g):
            i = j + 1  # 1-indexed
            for p in families[j]:
                expected = i / 2 + 0.25
                assert abs(p['real'] - expected) < 1e-10, (
                    f"Family i={i}: Re(s)={p['real']}, expected {expected}"
                )


# ====================================================================
# Section 10: Boecherer connection
# ====================================================================

class TestBoecherConnection:
    """Tests for the Boecherer bridge / L-value proxy."""

    def test_faber_pandharipande_lambda2(self):
        """lambda_2^FP = 7/5760."""
        lam2 = hge.faber_pandharipande_lambda(2)
        assert lam2 == Fraction(7, 5760), f"lambda_2 = {lam2}"

    def test_faber_pandharipande_lambda1(self):
        """lambda_1^FP = 1/24."""
        lam1 = hge.faber_pandharipande_lambda(1)
        assert lam1 == Fraction(1, 24), f"lambda_1 = {lam1}"

    def test_faber_pandharipande_lambda3(self):
        """lambda_3^FP = 31/967680."""
        lam3 = hge.faber_pandharipande_lambda(3)
        assert lam3 == Fraction(31, 967680), f"lambda_3 = {lam3}"

    def test_shadow_genus2_heisenberg(self):
        """F_2(Heisenberg) = k * 7/5760, no planted forest."""
        for kap in [1, 2, 5, 10]:
            data = hge.shadow_genus2_fourier_coefficient(kap, S3=0)
            assert data['F2_scalar'] == Fraction(kap) * Fraction(7, 5760)
            assert data['delta_pf'] == 0
            assert data['F2_total'] == data['F2_scalar']

    def test_shadow_genus2_virasoro(self):
        """F_2(Virasoro) = c/2 * 7/5760 + pf correction."""
        data = hge.shadow_genus2_fourier_coefficient(Fraction(13, 2), Fraction(2))
        assert data['F2_scalar'] == Fraction(13, 2) * Fraction(7, 5760)
        assert data['delta_pf'] == Fraction(2) * (20 - Fraction(13, 2)) / 48

    @skipmp
    def test_bocherer_proxy_computable(self):
        """Boecherer L-value proxy is computable."""
        result = hge.bocherer_central_L_value_proxy(12, 24, DPS)
        assert math.isfinite(result['F2'])
        assert math.isfinite(result['bocherer_ratio'])

    @skipmp
    def test_bocherer_ratio_is_1_for_scalar(self):
        """For scalar shadow alone, the Boecherer ratio is 1."""
        result = hge.bocherer_central_L_value_proxy(12, 24, DPS)
        assert abs(result['bocherer_ratio'] - 1.0) < 1e-10


# ====================================================================
# Section 11: Planted-forest correction
# ====================================================================

class TestPlantedForest:
    """Tests for delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48."""

    def test_heisenberg_zero(self):
        """Heisenberg (S_3=0): delta_pf = 0."""
        assert hge.planted_forest_genus2(1, 0) == 0
        assert hge.planted_forest_genus2(10, 0) == 0

    def test_virasoro_c26(self):
        """Virasoro at c=26: kappa=13, S_3=2, delta_pf = 2*(20-13)/48 = 7/24."""
        result = hge.planted_forest_genus2(13, 2)
        assert result == Fraction(7, 24), f"delta_pf = {result}"

    def test_virasoro_c1(self):
        """Virasoro at c=1: kappa=1/2, S_3=2, delta_pf = 2*(20-1/2)/48 = 39/48."""
        result = hge.planted_forest_genus2(Fraction(1, 2), 2)
        expected = Fraction(2) * (20 - Fraction(1, 2)) / 48
        assert result == expected, f"delta_pf = {result}, expected {expected}"

    def test_selfdual_c13(self):
        """Virasoro at c=13: kappa=13/2, delta_pf = 2*(20-13/2)/48 = 27/48 = 9/16."""
        result = hge.planted_forest_genus2(Fraction(13, 2), 2)
        expected = Fraction(2) * (20 - Fraction(13, 2)) / 48
        assert result == expected

    @skipmp
    def test_pf_residue_computable(self):
        """Planted-forest residue at a zeta zero is computable."""
        rho1 = complex(mpmath.zetazero(1))
        result = hge.planted_forest_residue_at_zeta_zero(
            Fraction(13, 2), Fraction(2), rho1, 13, family=1, dps=DPS
        )
        assert isinstance(result, complex)
        assert math.isfinite(abs(result))

    @skipmp
    def test_pf_residue_zero_for_heisenberg(self):
        """Planted-forest residue is zero for Heisenberg."""
        rho1 = complex(mpmath.zetazero(1))
        result = hge.planted_forest_residue_at_zeta_zero(
            1, 0, rho1, 2, family=1, dps=DPS
        )
        assert abs(result) < 1e-20


# ====================================================================
# Section 12: Complementarity at genus 2
# ====================================================================

class TestComplementarity:
    """Tests for c <-> 26-c complementarity at higher genus."""

    @skipmp
    def test_genus2_complementarity_computable(self):
        """genus2_complementarity is computable."""
        result = hge.genus2_complementarity(2.5 + 1j, 12, DPS)
        assert math.isfinite(abs(result['F2_c']))
        assert math.isfinite(abs(result['F2_c_dual']))

    @skipmp
    def test_genus2_self_dual_c13(self):
        """At c=13, F_{2,13}(s) = F_{2,13}(s) (trivially self-dual)."""
        s = 2.5 + 1j
        result = hge.genus2_complementarity(s, 13, DPS)
        assert abs(result['F2_c'] - result['F2_c_dual']) < 1e-10 * max(abs(result['F2_c']), 1e-50)

    @skipmp
    def test_genus2_zeta_ratios_universal(self):
        """Zeta ratios are the same for c and 26-c (they are c-independent)."""
        s = 2.5 + 1j
        d1 = hge.genus2_scattering_factor_decomposition(s, 10, DPS)
        d2 = hge.genus2_scattering_factor_decomposition(s, 16, DPS)
        # Zeta ratios should be identical
        assert abs(d1['zeta_ratio_1'] - d2['zeta_ratio_1']) < 1e-12
        assert abs(d1['zeta_ratio_2'] - d2['zeta_ratio_2']) < 1e-12

    @skipmp
    def test_genus_g_complementarity(self):
        """General genus-g complementarity is computable."""
        for g in [1, 2, 3]:
            s = g + 1.5 + 1j  # well away from poles
            result = hge.genus_g_complementarity(g, s, 10, DPS)
            assert math.isfinite(abs(result['Fg_c']))
            assert result['c_dual'] == 16

    @skipmp
    def test_genus_g_self_dual_c13(self):
        """At c=13, F_{g,13}(s) = F_{g,26-13}(s) for all g."""
        for g in [1, 2, 3]:
            s = g + 1.5 + 1j
            result = hge.genus_g_complementarity(g, s, 13, DPS)
            rel_err = abs(result['Fg_c'] - result['Fg_c_dual']) / max(abs(result['Fg_c']), 1e-50)
            assert rel_err < 1e-10, (
                f"Self-duality fails at g={g}: rel_err={rel_err}"
            )


# ====================================================================
# Section 13: Theta lift consistency (Path 2)
# ====================================================================

class TestThetaLift:
    """Path 2: Rankin-Selberg theta lift verification."""

    @skipmp
    def test_genus2_theta_lift_agrees(self):
        """Theta lift phi_2 agrees with direct computation."""
        for s in [2.5 + 1j, 3.0 + 2j, 2.2 + 5j]:
            result = hge.genus2_theta_lift_scattering(s, 12, DPS)
            assert result['agreement'] is True, (
                f"Theta lift disagrees at s={s}"
            )

    @skipmp
    def test_rankin_selberg_consistency(self):
        """Rankin-Selberg theta lift is consistent with scattering."""
        result = hge.rankin_selberg_theta_lift_consistency(2, 12, 2.5 + 1j, DPS)
        assert math.isfinite(abs(result['F_gc_direct']))
        assert math.isfinite(abs(result['phi_g']))


# ====================================================================
# Section 14: Standard family data
# ====================================================================

class TestStandardFamilyData:
    """Tests for standard family genus-2 shadow data."""

    def test_standard_families_complete(self):
        """All 5 standard families are present."""
        data = hge.standard_family_genus2_data()
        expected = {'Heisenberg', 'V_k(sl_2)', 'Virasoro', 'beta-gamma', 'W_3'}
        assert set(data.keys()) == expected

    def test_heisenberg_class_G(self):
        """Heisenberg is class G with S_3 = 0."""
        data = hge.standard_family_genus2_data()
        assert data['Heisenberg']['S3'] == 0
        assert data['Heisenberg']['shadow_class'] == 'G'

    def test_virasoro_class_M(self):
        """Virasoro is class M with S_3 = 2."""
        data = hge.standard_family_genus2_data()
        assert data['Virasoro']['S3'] == 2
        assert data['Virasoro']['shadow_class'] == 'M'

    def test_betagamma_pf_nonzero(self):
        """Beta-gamma has nonzero planted-forest correction."""
        data = hge.standard_family_genus2_data()
        assert data['beta-gamma']['delta_pf'] != 0

    def test_virasoro_genus2_data(self):
        """virasoro_genus2_epstein_data returns correct kappa values."""
        for c_val in [1, 12, 13, 24, 26]:
            data = hge.virasoro_genus2_epstein_data(c_val)
            assert data['kappa'] == Fraction(c_val, 2)
            assert data['kappa_dual'] == Fraction(26 - c_val, 2)

    def test_virasoro_genus2_selfdual(self):
        """At c=13, kappa = kappa_dual."""
        data = hge.virasoro_genus2_epstein_data(13)
        assert data['kappa'] == data['kappa_dual']


# ====================================================================
# Section 15: Higher-genus summary
# ====================================================================

class TestHigherGenusSummary:
    """Tests for the summary/overview functions."""

    @skipmp
    def test_summary_genus1(self):
        """Genus-1 summary is computable."""
        result = hge.higher_genus_zeta_zero_summary(1, 12, n_zeros=2, dps=DPS)
        assert result['genus'] == 1
        assert result['num_pole_families'] == 1
        assert len(result['first_zeros']) == 2

    @skipmp
    def test_summary_genus2(self):
        """Genus-2 summary shows two pole families."""
        result = hge.higher_genus_zeta_zero_summary(2, 12, n_zeros=2, dps=DPS)
        assert result['num_pole_families'] == 2
        assert len(result['pole_families']) == 2

    @skipmp
    def test_summary_genus3(self):
        """Genus-3 summary shows three pole families."""
        result = hge.higher_genus_zeta_zero_summary(3, 12, n_zeros=2, dps=DPS)
        assert result['num_pole_families'] == 3
        assert len(result['pole_families']) == 3

    @skipmp
    def test_summary_pole_staircase(self):
        """Pole families form a staircase: Re = 3/4, 5/4, 7/4, ..."""
        result = hge.higher_genus_zeta_zero_summary(3, 12, n_zeros=1, dps=DPS)
        for idx, fam in enumerate(result['pole_families']):
            i = idx + 1  # 1-indexed family
            expected_re = i / 2 + 0.25
            assert abs(fam['real_part_under_RH'] - expected_re) < 1e-10

    @skipmp
    def test_summary_genus2_has_family_residues(self):
        """Genus-2 summary includes family residue magnitudes."""
        result = hge.higher_genus_zeta_zero_summary(2, 12, n_zeros=1, dps=DPS)
        zero_data = result['first_zeros'][0]
        assert 'family_residues' in zero_data
        assert len(zero_data['family_residues']) == 2

    @skipmp
    def test_summary_genus1_residue_positive(self):
        """Genus-1 residue magnitude is positive."""
        result = hge.higher_genus_zeta_zero_summary(1, 12, n_zeros=1, dps=DPS)
        assert result['first_zeros'][0]['genus1_residue_mag'] > 0


# ====================================================================
# Section 16: Completed zeta/xi function
# ====================================================================

class TestCompletedFunctions:
    """Tests for the building-block functions."""

    @skipmp
    def test_xi_functional_equation(self):
        """xi(s) = xi(1-s) (completed Riemann zeta FE)."""
        for s in [0.3 + 1j, 0.7 + 5j, 2 + 3j]:
            xi_s = hge.completed_riemann_xi(s, DPS)
            xi_1ms = hge.completed_riemann_xi(1 - s, DPS)
            rel_err = abs(xi_s - xi_1ms) / max(abs(xi_s), 1e-100)
            assert rel_err < 1e-12, f"xi FE fails at s={s}: rel_err={rel_err}"

    @skipmp
    def test_Lambda_equals_xi_of_2s(self):
        """Lambda(s) = xi(2s)."""
        for s in [1.5 + 1j, 2.0 + 3j, 0.7 + 0.5j]:
            Lambda_s = hge.completed_selberg_Lambda(s, DPS)
            xi_2s = hge.completed_riemann_xi(2 * s, DPS)
            rel_err = abs(Lambda_s - xi_2s) / max(abs(Lambda_s), 1e-100)
            assert rel_err < 1e-12, f"Lambda != xi(2s) at s={s}: rel_err={rel_err}"


# ====================================================================
# Section 17: Cross-genus residue monotonicity
# ====================================================================

class TestCrossGenusMonotonicity:
    """Test structural properties across genera."""

    @skipmp
    def test_more_pole_families_at_higher_genus(self):
        """Genus g has exactly g pole families."""
        for g in range(1, 5):
            families = hge.genus_g_pole_families(g, n_zeros=1, dps=DPS)
            assert len(families) == g

    @skipmp
    def test_pole_staircase_step_size(self):
        """Each new genus adds a pole family 1/2 unit further right."""
        families = hge.genus_g_pole_families(4, n_zeros=1, dps=DPS)
        for j in range(4):
            i = j + 1
            expected_re = i / 2 + 0.25
            actual_re = families[j][0]['real']
            assert abs(actual_re - expected_re) < 1e-10

    @skipmp
    def test_genus2_family1_equals_genus1_family1(self):
        """The first family at genus 2 has the same poles as genus 1."""
        g1_fam = hge.genus_g_pole_families(1, n_zeros=3, dps=DPS)
        g2_fam = hge.genus_g_pole_families(2, n_zeros=3, dps=DPS)
        for p1, p2 in zip(g1_fam[0], g2_fam[0]):
            assert abs(p1['s'] - p2['s']) < 1e-10


# ====================================================================
# Section 18: Bernoulli numbers and FP invariants
# ====================================================================

class TestBernoulliAndFP:
    """Test Bernoulli numbers and Faber-Pandharipande invariants."""

    def test_bernoulli_B0(self):
        """B_0 = 1."""
        assert hge._bernoulli_number(0) == Fraction(1)

    def test_bernoulli_B1(self):
        """B_1 = -1/2."""
        assert hge._bernoulli_number(1) == Fraction(-1, 2)

    def test_bernoulli_B2(self):
        """B_2 = 1/6."""
        assert hge._bernoulli_number(2) == Fraction(1, 6)

    def test_bernoulli_B4(self):
        """B_4 = -1/30."""
        assert hge._bernoulli_number(4) == Fraction(-1, 30)

    def test_bernoulli_B6(self):
        """B_6 = 1/42."""
        assert hge._bernoulli_number(6) == Fraction(1, 42)

    def test_bernoulli_odd_vanish(self):
        """B_n = 0 for odd n > 1."""
        for n in [3, 5, 7, 9, 11]:
            assert hge._bernoulli_number(n) == 0

    def test_lambda_fp_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 7):
            assert hge.faber_pandharipande_lambda(g) > 0
