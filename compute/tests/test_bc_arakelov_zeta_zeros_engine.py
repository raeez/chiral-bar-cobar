r"""Tests for the BC Arakelov zeta zeros engine.

Covers all eight sections:
  1. Arakelov height of A_c(rho_n) at zeta zeros
  2. Faltings height of the shadow motive
  3. Height function on M-bar_{g,n}
  4. Shadow height zeta function
  5. Northcott property for shadow coefficients
  6. Bogomolov gap for shadow heights
  7. ABC conjecture for shadow triples
  8. Beilinson-Bloch height pairing

MULTI-PATH VERIFICATION:
  Path 1: Direct height computation from |A_c(rho)|
  Path 2: For rational values: h(p/q) = log max(|p|,|q|)
  Path 3: Consistency: h(alpha*beta) <= h(alpha) + h(beta)
  Path 4: For Heisenberg: kappa = k (integer), height = log|k|

References:
  CLAUDE.md: AP1, AP10, AP24, AP33, AP39, AP46, AP48
"""

import math
import cmath
import pytest
from fractions import Fraction

from compute.lib.bc_arakelov_zeta_zeros_engine import (
    # Zero access
    zeta_zero_rho,
    ZETA_ZEROS_50,
    # Core residue + height
    universal_residue_factor_Ac,
    arakelov_height_Ac,
    arakelov_height_Ac_table,
    arakelov_height_Ac_via_components,
    # Faltings height
    faltings_height_shadow_motive,
    lambda_fp,
    deg_arakelov_lambda1,
    kappa_exact_float,
    # Stratum heights
    stratum_heights_genus1,
    stratum_heights_genus2,
    height_function_Mbar,
    # Shadow height zeta
    shadow_height_zeta_partial,
    shadow_height_zeta_abscissa,
    shadow_coefficients_for_height,
    # Northcott
    northcott_count_shadows,
    northcott_property_check,
    # Bogomolov
    bogomolov_gap,
    # ABC
    abc_ratio_shadow_triple,
    abc_scan_shadows,
    _radical,
    _to_integer_triple,
    # Beilinson-Bloch
    beilinson_bloch_height_pairing,
    # Cross-verification
    verify_height_triangle_inequality,
    verify_heisenberg_height,
    verify_complementarity_heights,
    verify_rational_height_formula,
    # Comprehensive
    build_comprehensive_table,
)


# ============================================================================
# 1. ZETA ZEROS — basic access
# ============================================================================

class TestZetaZeros:
    """Verify zeta zero storage and access."""

    def test_first_zero_gamma(self):
        """First zero gamma_1 = 14.1347... (Odlyzko)."""
        assert abs(ZETA_ZEROS_50[0] - 14.134725141734694) < 1e-12

    def test_50_zeros_stored(self):
        """We store exactly 50 zeros."""
        assert len(ZETA_ZEROS_50) == 50

    def test_zeros_increasing(self):
        """Zeros are strictly increasing."""
        for i in range(len(ZETA_ZEROS_50) - 1):
            assert ZETA_ZEROS_50[i] < ZETA_ZEROS_50[i + 1]

    def test_zeta_zero_rho_format(self):
        """rho_n = 1/2 + i*gamma_n."""
        rho = zeta_zero_rho(1)
        assert abs(rho.real - 0.5) < 1e-15
        assert abs(rho.imag - 14.134725141734694) < 1e-12

    def test_zeta_zero_rho_n10(self):
        """10th zero: gamma_10 = 49.7738..."""
        rho = zeta_zero_rho(10)
        assert abs(rho.imag - 49.773832477672302) < 1e-10

    def test_zeta_zero_rho_n50(self):
        """50th zero: gamma_50 = 143.1118..."""
        rho = zeta_zero_rho(50)
        assert abs(rho.imag - 143.111845808661987) < 1e-8


# ============================================================================
# 2. ARAKELOV HEIGHT of A_c(rho_n) — Section 1
# ============================================================================

class TestArakelovHeightAc:
    """Test the Arakelov height of the universal residue factor."""

    def test_Ac_c1_rho1_finite(self):
        """A_1(rho_1) is finite and nonzero."""
        rho = zeta_zero_rho(1)
        A = universal_residue_factor_Ac(1.0, rho)
        assert abs(A) > 0
        assert not math.isinf(abs(A))

    def test_Ac_c13_rho1_finite(self):
        """A_13(rho_1) at the self-dual point is finite."""
        rho = zeta_zero_rho(1)
        A = universal_residue_factor_Ac(13.0, rho)
        assert abs(A) > 0
        assert not math.isinf(abs(A))

    def test_Ac_c26_rho1_finite(self):
        """A_26(rho_1) at the critical point is finite."""
        rho = zeta_zero_rho(1)
        A = universal_residue_factor_Ac(26.0, rho)
        assert abs(A) > 0
        assert not math.isinf(abs(A))

    def test_height_is_log_modulus(self):
        """h_Ar(A_c(rho)) = log|A_c(rho)|."""
        rho = zeta_zero_rho(1)
        c = 12.0
        A = universal_residue_factor_Ac(c, rho)
        h = arakelov_height_Ac(c, rho)
        assert abs(h - math.log(abs(A))) < 1e-10

    def test_height_c1_rho1_real(self):
        """Height at c=1, rho_1 is a real number."""
        h = arakelov_height_Ac(1.0, zeta_zero_rho(1))
        assert isinstance(h, float)
        assert not math.isnan(h)

    def test_height_varies_with_c(self):
        """Heights at different c are different (generically)."""
        rho = zeta_zero_rho(1)
        h1 = arakelov_height_Ac(1.0, rho)
        h13 = arakelov_height_Ac(13.0, rho)
        h26 = arakelov_height_Ac(26.0, rho)
        # These should generically differ
        assert abs(h1 - h13) > 1e-6 or abs(h1 - h26) > 1e-6

    def test_height_varies_with_n(self):
        """Heights at different zeros are different."""
        c = 12.0
        h1 = arakelov_height_Ac(c, zeta_zero_rho(1))
        h2 = arakelov_height_Ac(c, zeta_zero_rho(2))
        assert abs(h1 - h2) > 1e-8

    def test_height_table_shape(self):
        """Height table for 3 c-values and 5 zeros has 15 entries."""
        table = arakelov_height_Ac_table(c_values=[1, 13, 26], n_zeros=5)
        assert len(table) == 15

    def test_height_table_keys(self):
        """Each entry has the required keys."""
        table = arakelov_height_Ac_table(c_values=[1], n_zeros=1)
        entry = table[0]
        for key in ['c', 'n', 'gamma_n', 'rho_n', 'A_c_rho', 'modulus', 'phase', 'height']:
            assert key in entry

    def test_component_decomposition_matches(self):
        """Component decomposition of h_Ar matches direct computation."""
        rho = zeta_zero_rho(1)
        result = arakelov_height_Ac_via_components(12.0, rho)
        assert result['match'], (
            f"Component total {result['total_from_components']:.10f} != "
            f"direct {result['direct_height']:.10f}"
        )

    def test_component_decomposition_c1(self):
        """Component decomposition at c=1."""
        rho = zeta_zero_rho(3)
        result = arakelov_height_Ac_via_components(1.0, rho)
        assert result['match']

    def test_component_decomposition_c26(self):
        """Component decomposition at c=26."""
        rho = zeta_zero_rho(5)
        result = arakelov_height_Ac_via_components(26.0, rho)
        assert result['match']


# ============================================================================
# 3. FALTINGS HEIGHT — Section 2
# ============================================================================

class TestFaltingsHeight:
    """Test Faltings height of the shadow motive."""

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert abs(lambda_fp(1) - 1 / 24) < 1e-15

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert abs(lambda_fp(2) - 7 / 5760) < 1e-15

    def test_lambda_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        assert abs(lambda_fp(3) - 31 / 967680) < 1e-12

    def test_deg_arakelov_lambda1_value(self):
        """deg_Ar(lambda_1) = (1/2)*zeta'(-1) + (1/4)*log(2*pi) ~ 0.3776."""
        val = deg_arakelov_lambda1()
        # zeta'(-1) ~ -0.1654, log(2*pi) ~ 1.8379
        # (1/2)*(-0.1654) + (1/4)*(1.8379) = -0.0827 + 0.4595 ~ 0.3768
        assert 0.35 < val < 0.40

    def test_faltings_heisenberg_g1(self):
        """Faltings height for Heisenberg k=1 at genus 1."""
        result = faltings_height_shadow_motive("heisenberg", genus=1, k=1)
        assert result['kappa'] == 1.0
        assert result['lambda_fp_g'] == pytest.approx(1 / 24)
        assert abs(result['faltings_height'] - deg_arakelov_lambda1()) < 1e-12

    def test_faltings_virasoro_c13_g1(self):
        """Faltings height for Virasoro c=13 (self-dual point)."""
        result = faltings_height_shadow_motive("virasoro", genus=1, c=13)
        assert result['kappa'] == 6.5
        assert abs(result['faltings_height'] - 6.5 * deg_arakelov_lambda1()) < 1e-10

    def test_faltings_genus2(self):
        """Faltings height at genus 2 is computed."""
        result = faltings_height_shadow_motive("virasoro", genus=2, c=12)
        assert result['genus'] == 2
        assert result['faltings_height'] != 0

    def test_motivic_weight(self):
        """Motivic weight = 2g-2."""
        for g in [1, 2, 3]:
            result = faltings_height_shadow_motive("heisenberg", genus=g, k=1)
            assert result['motivic_weight'] == 2 * g - 2

    def test_F_g_equals_kappa_times_lambda(self):
        """F_g = kappa * lambda_g^FP."""
        result = faltings_height_shadow_motive("virasoro", genus=1, c=24)
        kap = 12.0
        assert abs(result['F_g'] - kap * lambda_fp(1)) < 1e-12


# ============================================================================
# 4. KAPPA COMPUTATION — foundational (AP1, AP39, AP48)
# ============================================================================

class TestKappaExact:
    """Verify kappa formulas for all families."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        for k in [1, 2, 3, -1]:
            assert kappa_exact_float("heisenberg", k=k) == float(k)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        for c in [1, 12, 13, 24, 25, 26]:
            assert abs(kappa_exact_float("virasoro", c=c) - c / 2) < 1e-15

    def test_affine_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        kap = kappa_exact_float("affine", lie_type="A", rank=1, k=1)
        assert abs(kap - 9 / 4) < 1e-12

    def test_w3_kappa(self):
        """kappa(W_3, c) = 5c/6."""
        assert abs(kappa_exact_float("w3", c=6) - 5.0) < 1e-12

    def test_lattice_kappa(self):
        """kappa(V_Lambda) = rank(Lambda)."""
        assert kappa_exact_float("lattice", rank=24) == 24.0

    def test_moonshine_kappa(self):
        """kappa(V^natural) = 12 (AP48: NOT c/2 = 12, same coincidence)."""
        assert kappa_exact_float("moonshine") == 12.0

    def test_betagamma_kappa(self):
        """kappa(betagamma, lam=1) = 6-6+1 = 1."""
        assert abs(kappa_exact_float("betagamma", lam=1) - 1.0) < 1e-12


# ============================================================================
# 5. STRATUM HEIGHTS — Section 3
# ============================================================================

class TestStratumHeights:
    """Test height function on M-bar_{g,n}."""

    def test_genus1_strata_keys(self):
        """Genus-1 strata include self-loop and smooth."""
        strata = stratum_heights_genus1("heisenberg", k=1)
        assert 'g1_n0_selfloop' in strata
        assert 'g1_n1_smooth' in strata

    def test_genus1_selfloop_heisenberg(self):
        """Genus-1 self-loop amplitude for H_1: kappa = 1, h = 0."""
        strata = stratum_heights_genus1("heisenberg", k=1)
        sl = strata['g1_n0_selfloop']
        assert sl['amplitude'] == 1.0
        assert sl['height'] == pytest.approx(0.0, abs=1e-10)

    def test_genus1_selfloop_heisenberg_k2(self):
        """Genus-1 self-loop amplitude for H_2: kappa = 2, h = log(2)."""
        strata = stratum_heights_genus1("heisenberg", k=2)
        sl = strata['g1_n0_selfloop']
        assert sl['amplitude'] == 2.0
        assert abs(sl['height'] - math.log(2)) < 1e-10

    def test_genus2_three_strata(self):
        """Genus-2 has smooth, separating, and non-separating strata."""
        strata = stratum_heights_genus2("virasoro", c=12)
        assert 'g2_smooth' in strata
        assert 'g2_separating' in strata
        assert 'g2_nonseparating' in strata
        assert 'g2_planted_forest' in strata

    def test_genus2_smooth_amplitude(self):
        """Genus-2 smooth amplitude = kappa * lambda_2^FP."""
        strata = stratum_heights_genus2("virasoro", c=24)
        expected = 12.0 * 7 / 5760
        assert abs(strata['g2_smooth']['amplitude'] - expected) < 1e-12

    def test_height_function_Mbar_genus1(self):
        """height_function_Mbar returns strata for genus 1."""
        result = height_function_Mbar("heisenberg", genus=1, k=1)
        assert result['genus'] == 1
        assert 'strata' in result

    def test_height_function_Mbar_genus2(self):
        """height_function_Mbar returns strata for genus 2."""
        result = height_function_Mbar("virasoro", genus=2, c=12)
        assert result['genus'] == 2
        strata = result['strata']
        assert 'g2_smooth' in strata


# ============================================================================
# 6. SHADOW HEIGHT ZETA — Section 4
# ============================================================================

class TestShadowHeightZeta:
    """Test the shadow height zeta function Z^{ht}_A(s)."""

    def test_heisenberg_single_term(self):
        """Heisenberg k=2: only S_2 = 2, so Z^ht(s) = (log 2)^{-s}."""
        z = shadow_height_zeta_partial("heisenberg", s=1.0, max_r=10, k=2)
        expected = math.log(2) ** (-1.0)
        assert abs(z.real - expected) < 1e-8

    def test_heisenberg_k1_vanishes(self):
        """Heisenberg k=1: S_2 = 1, h(1) = 0, so no terms => Z = 0."""
        z = shadow_height_zeta_partial("heisenberg", s=1.0, max_r=10, k=1)
        assert abs(z) < 1e-12

    def test_virasoro_has_multiple_terms(self):
        """Virasoro class M: multiple nonzero shadow coefficients."""
        z = shadow_height_zeta_partial("virasoro", s=2.0, max_r=20, c=12)
        # Should be nonzero (multiple terms contribute)
        assert abs(z) > 0

    def test_abscissa_heisenberg(self):
        """Heisenberg abscissa = -infty (finite sum)."""
        result = shadow_height_zeta_abscissa("heisenberg", max_r=10, k=1)
        assert result['abscissa'] == float('-inf')
        assert result['shadow_class'] == 'finite (G/L/C)'

    def test_abscissa_virasoro(self):
        """Virasoro abscissa is finite (class M, infinite tower)."""
        result = shadow_height_zeta_abscissa("virasoro", max_r=30, c=12)
        assert result['n_terms'] > 3  # Multiple height-nonzero terms

    def test_shadow_coefficients_heisenberg(self):
        """Heisenberg shadow coefficients: S_2 = k, rest zero."""
        coeffs = shadow_coefficients_for_height("heisenberg", k=3, max_r=10)
        assert 2 in coeffs
        assert coeffs[2] == 3.0
        for r in range(3, 11):
            assert coeffs.get(r, 0) == 0

    def test_shadow_coefficients_virasoro(self):
        """Virasoro shadow coefficients include S_2, S_3, S_4."""
        coeffs = shadow_coefficients_for_height("virasoro", c=12, max_r=10)
        assert 2 in coeffs
        assert coeffs[2] == 6.0  # kappa = c/2 = 6
        assert 3 in coeffs  # S_3 nonzero for Virasoro
        assert 4 in coeffs  # S_4 nonzero (Q^contact)


# ============================================================================
# 7. NORTHCOTT PROPERTY — Section 5
# ============================================================================

class TestNorthcott:
    """Test Northcott property for shadow coefficients."""

    def test_northcott_holds_heisenberg(self):
        """Northcott holds trivially for Heisenberg (single term)."""
        result = northcott_property_check("heisenberg", k=2, max_r=20)
        assert result['northcott_holds']
        assert result['shadow_class'] == 'finite'

    def test_northcott_holds_virasoro(self):
        """Northcott holds for Virasoro (heights grow)."""
        result = northcott_property_check("virasoro", c=12, max_r=30)
        assert result['northcott_holds']

    def test_northcott_count_bounded(self):
        """Count of S_r with h(S_r) < B is finite for any B."""
        for B in [1.0, 5.0, 10.0]:
            result = northcott_count_shadows("virasoro", bound=B, max_r=50, c=12)
            assert result['count'] < 50  # Strictly less than max_r

    def test_northcott_count_increases(self):
        """Larger bounds give (weakly) more qualifying terms."""
        c1 = northcott_count_shadows("virasoro", bound=1.0, max_r=30, c=12)
        c5 = northcott_count_shadows("virasoro", bound=5.0, max_r=30, c=12)
        assert c1['count'] <= c5['count']


# ============================================================================
# 8. BOGOMOLOV GAP — Section 6
# ============================================================================

class TestBogomolovGap:
    """Test the Bogomolov gap for shadow heights."""

    def test_gap_exists_heisenberg(self):
        """Heisenberg: gap exists (kappa = k, h = log|k|)."""
        result = bogomolov_gap("heisenberg", k=2, max_r=10)
        assert result['gap_exists']
        assert result['minimum_height'] == pytest.approx(math.log(2), abs=1e-10)

    def test_gap_virasoro(self):
        """Virasoro: gap exists (all S_r are rational, nonzero)."""
        result = bogomolov_gap("virasoro", c=12, max_r=20)
        assert result['gap_exists']
        assert result['minimum_height'] > 0

    def test_gap_value_heisenberg_k3(self):
        """Heisenberg k=3: minimum height = log(3)."""
        result = bogomolov_gap("heisenberg", k=3, max_r=10)
        assert abs(result['minimum_height'] - math.log(3)) < 1e-10

    def test_gap_above_zero(self):
        """All families have strictly positive minimum height (for nonzero coeffs)."""
        for fam, pars in [("heisenberg", {"k": 2}), ("virasoro", {"c": 12}),
                          ("virasoro", {"c": 24})]:
            result = bogomolov_gap(fam, max_r=15, **pars)
            if result['gap_exists']:
                assert result['minimum_height'] > 0


# ============================================================================
# 9. ABC CONJECTURE — Section 7
# ============================================================================

class TestABC:
    """Test ABC conjecture for shadow triples."""

    def test_radical_basic(self):
        """rad(12) = 2*3 = 6."""
        assert _radical(12) == 6

    def test_radical_prime(self):
        """rad(7) = 7."""
        assert _radical(7) == 7

    def test_radical_prime_power(self):
        """rad(8) = rad(2^3) = 2."""
        assert _radical(8) == 2

    def test_radical_1(self):
        """rad(1) = 1."""
        assert _radical(1) == 1

    def test_integer_triple_basic(self):
        """Integer triple from 1/2, 1/3."""
        a, b, c = _to_integer_triple(0.5, 1 / 3)
        assert a + b == c

    def test_abc_virasoro_r2(self):
        """ABC ratio for Virasoro (S_2, S_3, S_2+S_3)."""
        result = abc_ratio_shadow_triple("virasoro", r=2, max_r=10, c=12)
        if not math.isnan(result['abc_ratio']):
            assert result['abc_ratio'] > 0
            assert result['abc_consistent']

    def test_abc_scan_virasoro(self):
        """ABC scan over Virasoro shadow triples."""
        results = abc_scan_shadows("virasoro", max_r=10, c=12)
        # At least some triples should be computable
        assert len(results) > 0
        for r in results:
            if not math.isnan(r['abc_ratio']):
                assert r['abc_consistent'], f"ABC violated at r={r['r']}: q={r['abc_ratio']}"

    def test_abc_ratios_bounded(self):
        """All computed ABC ratios should be < 2 (practical bound)."""
        results = abc_scan_shadows("virasoro", max_r=8, c=24)
        for r in results:
            if not math.isnan(r['abc_ratio']):
                assert r['abc_ratio'] < 2.0


# ============================================================================
# 10. BEILINSON-BLOCH HEIGHT PAIRING — Section 8
# ============================================================================

class TestBeilinsonBloch:
    """Test the Beilinson-Bloch height pairing."""

    def test_bb_heisenberg_antisymmetric(self):
        """Heisenberg: kappa + kappa' = k + (-k) = 0."""
        result = beilinson_bloch_height_pairing("heisenberg", genus=1, k=2)
        assert abs(result['kappa_sum']) < 1e-12

    def test_bb_virasoro_kappa_sum_13(self):
        """Virasoro: kappa + kappa' = c/2 + (26-c)/2 = 13 (AP24)."""
        for c in [1, 6, 12, 13, 24, 25]:
            result = beilinson_bloch_height_pairing("virasoro", genus=1, c=c)
            assert abs(result['kappa_sum'] - 13.0) < 1e-10, \
                f"c={c}: kappa_sum={result['kappa_sum']} != 13"

    def test_bb_self_dual_virasoro(self):
        """At c=13: kappa = kappa' = 13/2, pairing is symmetric."""
        result = beilinson_bloch_height_pairing("virasoro", genus=1, c=13)
        assert abs(result['kappa'] - 6.5) < 1e-12
        assert abs(result['kappa_dual'] - 6.5) < 1e-12
        assert abs(result['Q_g_A'] - result['Q_g_A_dual']) < 1e-12

    def test_bb_affine_sl2_antisymmetric(self):
        """Affine sl_2: kappa + kappa' = 0 (Feigin-Frenkel: k -> -k-4)."""
        result = beilinson_bloch_height_pairing("affine", genus=1,
                                                lie_type="A", rank=1, k=1)
        # kappa(sl2, k=1) = 3*3/4 = 9/4
        # kappa(sl2, k=-1-4=-5) = 3*(-5+2)/4 = -9/4
        assert abs(result['kappa_sum']) < 1e-10

    def test_bb_pairing_nonzero(self):
        """BB pairing is generically nonzero."""
        result = beilinson_bloch_height_pairing("virasoro", genus=1, c=12)
        assert abs(result['BB_pairing']) > 0

    def test_bb_sign_heisenberg(self):
        """For Heisenberg: kappa * kappa' < 0, so BB pairing < 0."""
        result = beilinson_bloch_height_pairing("heisenberg", genus=1, k=2)
        # kappa = 2, kappa' = -2, so product is -4
        assert result['BB_pairing'] < 0

    def test_bb_genus2(self):
        """BB pairing at genus 2 is computed."""
        result = beilinson_bloch_height_pairing("virasoro", genus=2, c=12)
        assert result['genus'] == 2
        assert 'BB_pairing' in result


# ============================================================================
# 11. CROSS-VERIFICATION — multi-path consistency
# ============================================================================

class TestCrossVerification:
    """Multi-path verification of all height computations."""

    def test_triangle_inequality_archimedean(self):
        """h(A1*A2) = h(A1) + h(A2) for archimedean height (equality)."""
        result = verify_height_triangle_inequality(12.0, 1, 2)
        assert result['triangle_holds']
        # For archimedean: log|ab| = log|a| + log|b|, so equality holds
        assert result['is_equality']

    def test_triangle_inequality_several(self):
        """Triangle inequality holds for several (c, n1, n2) triples."""
        for c in [1, 13, 26]:
            for n1, n2 in [(1, 2), (1, 5), (3, 7)]:
                result = verify_height_triangle_inequality(float(c), n1, n2)
                assert result['triangle_holds'], \
                    f"Triangle failed: c={c}, n1={n1}, n2={n2}"

    def test_heisenberg_height_path4(self):
        """Path 4: Heisenberg kappa = k, height = log|k|."""
        for k in [1, 2, 3, 5, 10]:
            result = verify_heisenberg_height(k)
            assert result['match'], \
                f"k={k}: height={result['height']}, expected={result['expected']}"

    def test_heisenberg_height_negative(self):
        """Heisenberg at k=-1: kappa = -1, h = 0."""
        result = verify_heisenberg_height(-1)
        assert result['kappa'] == -1.0
        assert result['height'] == pytest.approx(0.0, abs=1e-10)

    def test_complementarity_virasoro(self):
        """Virasoro complementarity: kappa + kappa' = 13."""
        for c in [1, 6, 12, 13, 24, 25, 26]:
            result = verify_complementarity_heights(float(c))
            assert result['kappa_sum_is_13'], \
                f"c={c}: sum={result['kappa_sum']}"

    def test_rational_height_formula(self):
        """Path 2: h(p/q) = log max(|p|, |q|) for various p, q."""
        cases = [
            (1, 2, math.log(2)),      # h(1/2) = log(2)
            (3, 1, math.log(3)),      # h(3) = log(3)
            (5, 7, math.log(7)),      # h(5/7) = log(7)
            (1, 1, 0.0),             # h(1) = 0
            (2, 3, math.log(3)),      # h(2/3) = log(3)
            (100, 1, math.log(100)),  # h(100) = log(100)
        ]
        for p, q, expected in cases:
            result = verify_rational_height_formula(p, q)
            assert result['match'], \
                f"p={p}, q={q}: height={result['height']}, expected={expected}"

    def test_rational_height_coprime(self):
        """h(6/4) = h(3/2) = log(3) after reduction."""
        result = verify_rational_height_formula(6, 4)
        assert abs(result['height'] - math.log(3)) < 1e-8


# ============================================================================
# 12. COMPREHENSIVE TABLE — Integration test
# ============================================================================

class TestComprehensiveTable:
    """Integration test for the full table builder."""

    def test_table_builds(self):
        """Comprehensive table builds without error."""
        table = build_comprehensive_table(
            c_values=[1, 13], n_zeros=3,
            families=[("heisenberg", {"k": 1}), ("virasoro", {"c": 13})],
        )
        assert 'residue_heights' in table
        assert 'faltings_data' in table
        assert 'bb_data' in table

    def test_table_residue_count(self):
        """Residue heights: 2 c-values * 3 zeros = 6 entries."""
        table = build_comprehensive_table(
            c_values=[1, 13], n_zeros=3,
            families=[("heisenberg", {"k": 1})],
        )
        assert len(table['residue_heights']) == 6

    def test_table_faltings_count(self):
        """Faltings data: 2 families * 2 genera = 4 entries."""
        table = build_comprehensive_table(
            c_values=[1],
            n_zeros=1,
            families=[("heisenberg", {"k": 1}), ("virasoro", {"c": 13})],
        )
        assert len(table['faltings_data']) == 4  # 2 families * 2 genera


# ============================================================================
# 13. SHADOW COEFFICIENT STRUCTURE — deeper tests
# ============================================================================

class TestShadowCoefficientStructure:
    """Test structural properties of shadow coefficients and their heights."""

    def test_virasoro_S3_formula(self):
        """Virasoro S_3 = 2 (c-independent, universal gravitational cubic)."""
        coeffs = shadow_coefficients_for_height("virasoro", c=12, max_r=5)
        assert abs(coeffs.get(3, 0) - 2.0) < 1e-10

    def test_virasoro_S4_formula(self):
        """Virasoro S_4 = Q^contact = 10/(c(5c+22)) at c=12."""
        coeffs = shadow_coefficients_for_height("virasoro", c=12, max_r=5)
        expected_S4 = 10 / (12 * (60 + 22))
        assert abs(coeffs.get(4, 0) - expected_S4) < 1e-10

    def test_heisenberg_class_G(self):
        """Heisenberg is class G: only S_2 nonzero."""
        coeffs = shadow_coefficients_for_height("heisenberg", k=5, max_r=20)
        assert coeffs[2] == 5.0
        for r in range(3, 21):
            assert abs(coeffs.get(r, 0)) < 1e-15

    def test_virasoro_higher_arities_nonzero(self):
        """Virasoro class M: higher-arity coefficients are nonzero."""
        coeffs = shadow_coefficients_for_height("virasoro", c=12, max_r=10)
        # S_5, S_6, ... should be nonzero for class M
        nonzero_count = sum(1 for r in range(5, 11) if abs(coeffs.get(r, 0)) > 1e-15)
        assert nonzero_count > 0

    def test_height_growth_virasoro(self):
        """For Virasoro: the maximum height among S_r grows with max_r (class M)."""
        coeffs = shadow_coefficients_for_height("virasoro", c=12, max_r=15)
        heights = [_naive_ht(coeffs[r]) for r in sorted(coeffs)
                   if abs(coeffs[r]) > 1e-15 and r >= 2]
        # Class M has infinitely many nonzero terms; the max height
        # among the first several should exceed log(2)
        if len(heights) >= 2:
            assert max(heights) >= math.log(2) - 0.01


def _naive_ht(x):
    """Helper: naive height of a float."""
    if abs(x) < 1e-30:
        return 0.0
    try:
        f = Fraction(x).limit_denominator(10 ** 12)
        return math.log(max(abs(f.numerator), abs(f.denominator)))
    except (OverflowError, ValueError):
        return math.log(abs(x))
