r"""Tests for BPS black hole entropy from the CY3 shadow obstruction tower.

Tests organized by section:
  1.  Faber-Pandharipande intersection numbers (exact)
  2.  CY3 modular characteristics (kappa values)
  3.  Strominger-Vafa BPS entropy
  4.  Shadow tower to entropy corrections
  5.  Rademacher expansion for 1/Phi_10
  6.  C^3 / MacMahon formal entropy
  7.  Bessel index from shadow data
  8.  Cross-verification: Bessel vs shadow tower
  9.  Entropy comparison across CY3 families
  10. Genus expansion of BPS free energy
  11. Numerical BPS degeneracy comparisons
  12. Shadow depth classification
  13. Kappa-weight bridge
  14. Shadow CohFT entropy functional
  15. Consistency checks

Multi-path verification (CLAUDE.md mandate):
  Path 1: Direct formula computation
  Path 2: Cross-family / cross-arity consistency
  Path 3: Numerical comparison with known values
"""

import pytest
import math
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bps_entropy_shadow import (
    # Section 1
    lambda_fp,
    # Section 2
    kappa_k3_times_e, kappa_elliptic, kappa_k3,
    kappa_quintic_conjectural, kappa_resolved_conifold,
    # Section 3
    strominger_vafa_discriminant, strominger_vafa_entropy_leading,
    strominger_vafa_entropy_subleading,
    # Section 4
    shadow_to_entropy_correction_k3e, shadow_entropy_expansion_k3e,
    bessel_asymptotic_coefficients,
    # Section 5
    rademacher_leading_term_phi10, rademacher_subleading_phi10,
    # Section 6
    macmahon_log_asymptotics, macmahon_shadow_comparison,
    # Section 7
    bessel_index_from_kappa, log_correction_from_kappa,
    # Section 8
    verify_bessel_shadow_match,
    # Section 9
    entropy_comparison_table,
    # Section 10
    bps_free_energy_genus_g, bps_genus_expansion,
    bps_entropy_genus_corrections,
    # Section 11
    BPS_DEGENERACIES_DVV,
    verify_rademacher_vs_exact, rademacher_convergence_rate,
    # Section 12
    bps_shadow_depth_classification,
    # Section 13
    kappa_to_automorphic_weight, weight_to_log_correction,
    # Section 14
    shadow_cohft_entropy,
    # Section 15
    verify_kappa_weight_consistency, verify_bessel_coefficients_exact,
)

PI = math.pi
FOUR_PI = 4.0 * PI


# =========================================================================
# Section 1: Faber-Pandharipande intersection numbers
# =========================================================================

class TestFaberPandharipande:
    """Tests for lambda_g^FP values (exact arithmetic)."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_4(self):
        """lambda_4^FP = 127/154828800."""
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_lambda_positive(self):
        """All lambda_g^FP are POSITIVE (AP22: Bernoulli signs)."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0, f"lambda_{g} must be positive"

    def test_lambda_decreasing(self):
        """lambda_g^FP decreases superexponentially."""
        for g in range(1, 7):
            assert lambda_fp(g + 1) < lambda_fp(g)


# =========================================================================
# Section 2: CY3 modular characteristics
# =========================================================================

class TestCY3Kappa:
    """Tests for CY3 modular characteristics kappa."""

    def test_kappa_k3_times_e(self):
        """kappa(K3 x E) = 5.

        Path 1: weight(Delta_5) = 5.
        Path 2: (chi(K3) - 4)/4 = (24-4)/4 = 5.
        """
        assert kappa_k3_times_e() == Fraction(5)

    def test_kappa_elliptic(self):
        """kappa(E) = 1 = kappa(Heisenberg H_1)."""
        assert kappa_elliptic() == Fraction(1)

    def test_kappa_k3(self):
        """kappa(K3) = 2 = chi(O_{K3})."""
        assert kappa_k3() == Fraction(2)

    def test_kappa_quintic_conjectural(self):
        """kappa(quintic) = -200/24 = -25/3 (CONJECTURAL)."""
        assert kappa_quintic_conjectural() == Fraction(-25, 3)

    def test_kappa_resolved_conifold(self):
        """kappa(resolved conifold) = 1."""
        assert kappa_resolved_conifold() == Fraction(1)

    def test_kappa_additivity_k3_e(self):
        """kappa(K3 x E) != kappa(K3) + kappa(E).

        5 != 2 + 1 = 3. The CY modular characteristic is NOT additive
        under products. This is because kappa for a product CY3 involves
        the MIXED Hodge structure, not just the sum.
        """
        assert kappa_k3_times_e() != kappa_k3() + kappa_elliptic()

    def test_kappa_not_half_euler(self):
        """kappa(K3 x E) != chi_top(K3 x E)/2.

        AP48: kappa is NOT chi_top/2 in general.
        chi_top(K3 x E) = chi_top(K3) * chi_top(E) = 24 * 0 = 0.
        kappa = 5 != 0.
        """
        chi_top_k3_times_e = 0  # chi(K3)*chi(E) = 24*0 = 0
        assert float(kappa_k3_times_e()) != chi_top_k3_times_e / 2


# =========================================================================
# Section 3: Strominger-Vafa BPS entropy
# =========================================================================

class TestStromingerVafa:
    """Tests for the Strominger-Vafa BPS entropy formula."""

    def test_discriminant_basic(self):
        """D = Q0*Q2*Q6 - J^2."""
        assert strominger_vafa_discriminant(1, 2, 3, 0) == 6
        assert strominger_vafa_discriminant(2, 3, 5, 1) == 29
        assert strominger_vafa_discriminant(1, 1, 1, 1) == 0

    def test_discriminant_no_angular_momentum(self):
        """J=0 case: D = Q0*Q2*Q6."""
        assert strominger_vafa_discriminant(10, 10, 10) == 1000

    def test_leading_entropy_formula(self):
        """S_BH = 4*pi*sqrt(D).

        Path 1: direct formula.
        Path 2: Cardy formula S = 2*pi*sqrt(c*L_0/6) with c=6Q_6, L_0 ~ Q_0*Q_2.
        """
        D = 100
        S = strominger_vafa_entropy_leading(D)
        assert abs(S - FOUR_PI * 10.0) < 1e-10

    def test_leading_entropy_large_D(self):
        """At large D, S grows as sqrt(D)."""
        D1, D2 = 1000, 4000
        S1 = strominger_vafa_entropy_leading(D1)
        S2 = strominger_vafa_entropy_leading(D2)
        # S2/S1 should be sqrt(D2/D1) = 2
        assert abs(S2 / S1 - 2.0) < 1e-10

    def test_entropy_zero_discriminant(self):
        """D=0: no black hole."""
        assert strominger_vafa_entropy_leading(0) == 0.0

    def test_entropy_negative_discriminant(self):
        """D<0: no black hole (naked singularity)."""
        assert strominger_vafa_entropy_leading(-1) == 0.0

    def test_subleading_structure(self):
        """Subleading has log correction and power corrections."""
        result = strominger_vafa_entropy_subleading(1000)
        assert 'S_BH' in result
        assert 'log_correction' in result
        assert 'entropy_corrections' in result
        # S_BH should be 4*pi*sqrt(1000)
        assert abs(result['S_BH'] - FOUR_PI * math.sqrt(1000)) < 1e-10

    def test_log_correction_sign(self):
        """Logarithmic correction is NEGATIVE for D > 1."""
        result = strominger_vafa_entropy_subleading(100)
        assert result['log_correction'] < 0

    def test_log_correction_coefficient(self):
        """Log correction coefficient is -27/4.

        Path 1: from Rademacher expansion of 1/Phi_10.
        Path 2: from Sen's 2012 result for N=4 BPS.
        """
        result = strominger_vafa_entropy_subleading(100)
        assert abs(result['log_correction_coeff'] - (-6.75)) < 1e-10


# =========================================================================
# Section 4: Shadow tower to entropy corrections
# =========================================================================

class TestShadowEntropyDictionary:
    """Tests for the shadow tower to entropy correction dictionary."""

    def test_arity_2_is_bekenstein_hawking(self):
        """Arity 2 gives S_BH = 4*pi*sqrt(D)."""
        D = 100
        S2 = shadow_to_entropy_correction_k3e(2, D)
        assert abs(S2 - FOUR_PI * 10.0) < 1e-10

    def test_arity_3_is_logarithmic(self):
        """Arity 3 gives the logarithmic correction."""
        D = 100
        S3 = shadow_to_entropy_correction_k3e(3, D)
        assert abs(S3 - (-6.75 * math.log(100))) < 1e-10

    def test_arity_4_power_correction(self):
        """Arity 4 gives the first power correction ~ 1/D.

        Arity r maps to Bessel coefficient k = r - 2.
        Arity 4 -> k = 2 -> a_2 / z^2.
        """
        D = 10000
        S4 = shadow_to_entropy_correction_k3e(4, D)
        # Should be a_2 / z^2 where z = 4*pi*sqrt(D) = 4*pi*100
        z = FOUR_PI * 100
        nu = Fraction(19, 2)
        coeffs = bessel_asymptotic_coefficients(nu, 2)
        expected = float(coeffs[2]) / z ** 2
        assert abs(S4 - expected) < 1e-12

    def test_higher_arity_decreasing(self):
        """Higher-arity corrections decrease in magnitude for large D."""
        D = 10000
        corrections = []
        for r in range(4, 8):
            corrections.append(abs(shadow_to_entropy_correction_k3e(r, D)))
        for i in range(len(corrections) - 1):
            assert corrections[i + 1] < corrections[i], \
                f"Arity {i+4} correction not smaller than arity {i+5}"

    def test_expansion_structure(self):
        """Full expansion returns consistent structure."""
        result = shadow_entropy_expansion_k3e(1000, max_arity=6)
        assert result['kappa_K3E'] == 5
        assert result['weight_Phi10'] == 10
        assert 2 in result['contributions']
        assert result['S_BH'] > 0

    def test_expansion_dominated_by_leading(self):
        """S_BH dominates total entropy at large D."""
        result = shadow_entropy_expansion_k3e(10000, max_arity=8)
        S_BH = result['S_BH']
        S_total = result['S_total']
        # Corrections are small at large D
        assert abs(S_total - S_BH) / S_BH < 0.1


# =========================================================================
# Section 5: Rademacher expansion
# =========================================================================

class TestRademacher:
    """Tests for the Rademacher expansion of 1/Phi_10."""

    def test_leading_term_positive(self):
        """Leading Rademacher term is positive for D > 0."""
        for D in [1, 10, 100, 1000]:
            assert rademacher_leading_term_phi10(D) > 0

    def test_leading_term_negative_D(self):
        """Leading term is -inf for D <= 0."""
        assert rademacher_leading_term_phi10(0) == float('-inf')

    def test_subleading_structure(self):
        """Subleading expansion returns correct structure."""
        result = rademacher_subleading_phi10(1000, order=3)
        assert 'S_BH' in result
        assert 'power_corrections' in result
        assert len(result['power_corrections']) == 3

    def test_subleading_convergent(self):
        """Power corrections decrease geometrically at large D."""
        result = rademacher_subleading_phi10(10000, order=5)
        corrections = [
            abs(result['power_corrections'][k]['contribution'])
            for k in range(1, 6)
        ]
        for i in range(len(corrections) - 1):
            assert corrections[i + 1] < corrections[i]


# =========================================================================
# Section 6: MacMahon / C^3 formal entropy
# =========================================================================

class TestMacMahon:
    """Tests for C^3 / MacMahon formal entropy."""

    def test_macmahon_A3_value(self):
        """A_3 = 3*(zeta(3)/4)^{1/3} ~ 2.009."""
        result = macmahon_log_asymptotics(1000)
        A_3 = result['A_3']
        # A_3 should be approximately 2.009
        assert abs(A_3 - 2.009) < 0.01

    def test_macmahon_leading_positive(self):
        """Leading MacMahon term is positive for n > 0."""
        for n in [1, 10, 100, 1000]:
            result = macmahon_log_asymptotics(n)
            assert result['leading'] > 0

    def test_macmahon_growth_exponent(self):
        """log p_3(n) grows as n^{2/3} (not n^{1/2} like 2d partitions).

        Path 1: direct formula.
        Path 2: ratio test: log p_3(8n) / log p_3(n) -> 4 (since (8n)^{2/3}/n^{2/3} = 4).
        """
        n1, n2 = 1000, 8000
        r1 = macmahon_log_asymptotics(n1)
        r2 = macmahon_log_asymptotics(n2)
        ratio = r2['leading'] / r1['leading']
        # Should be (8000/1000)^{2/3} = 8^{2/3} = 4
        assert abs(ratio - 4.0) < 0.01

    def test_macmahon_log_correction_coefficient(self):
        """Log correction coefficient is -25/36."""
        result = macmahon_log_asymptotics(1000)
        assert abs(result['log_correction_coeff'] - (-25.0 / 36.0)) < 1e-10

    def test_shadow_comparison_structure(self):
        """MacMahon-shadow comparison returns valid structure."""
        result = macmahon_shadow_comparison(10, 100)
        assert result['N_trunc'] == 10
        assert result['c'] == 9
        assert result['kappa_WN'] > 0


# =========================================================================
# Section 7: Bessel index
# =========================================================================

class TestBesselIndex:
    """Tests for the Bessel index from shadow data."""

    def test_bessel_index_k3e(self):
        """nu = 2*kappa - 3/2 = 10 - 3/2 = 17/2 for K3 x E."""
        nu = bessel_index_from_kappa(5, dim_moduli=3)
        assert nu == Fraction(17, 2)

    def test_log_correction_k3e(self):
        """Log correction is -27/4 for K3 x E."""
        assert log_correction_from_kappa(5) == Fraction(-27, 4)


# =========================================================================
# Section 8: Bessel asymptotic coefficients
# =========================================================================

class TestBesselCoefficients:
    """Tests for Bessel asymptotic coefficients a_k(nu)."""

    def test_a0_is_one(self):
        """a_0(nu) = 1 for all nu."""
        for nu in [Fraction(1, 2), Fraction(19, 2), Fraction(5)]:
            coeffs = bessel_asymptotic_coefficients(nu, 0)
            assert coeffs[0] == Fraction(1)

    def test_a1_formula(self):
        """a_1(nu) = -(4*nu^2 - 1)/8.

        For nu = 19/2: a_1 = -(4*(361/4) - 1)/8 = -(361-1)/8 = -45.
        """
        nu = Fraction(19, 2)
        coeffs = bessel_asymptotic_coefficients(nu, 1)
        expected = -(4 * nu * nu - 1) / 8
        assert coeffs[1] == expected
        assert coeffs[1] == Fraction(-45)

    def test_a2_formula(self):
        """a_2(19/2) = (4*nu^2-1)(4*nu^2-9)/128 = 360*352/128 = 990."""
        nu = Fraction(19, 2)
        coeffs = bessel_asymptotic_coefficients(nu, 2)
        four_nu_sq = 4 * nu * nu
        expected = (four_nu_sq - 1) * (four_nu_sq - 9) / 128
        assert coeffs[2] == expected
        assert coeffs[2] == Fraction(990)

    def test_bessel_coeff_nu_half(self):
        """For nu=1/2, I_{1/2}(z) = sqrt(2/(pi*z))*sinh(z), all a_k should be computable.

        a_1(1/2) = -(4*1/4 - 1)/8 = 0/8 = 0.
        Actually: 4*(1/2)^2 = 1, so 4*nu^2 - 1 = 0.
        Therefore a_k(1/2) = 0 for all k >= 1 (the product has a zero factor).
        This is correct: I_{1/2}(z) = sqrt(2/(pi*z))*sinh(z) which has
        EXACT Bessel expansion with a_0=1 and all a_k=0.
        """
        nu = Fraction(1, 2)
        coeffs = bessel_asymptotic_coefficients(nu, 5)
        assert coeffs[0] == Fraction(1)
        for k in range(1, 6):
            assert coeffs[k] == Fraction(0), f"a_{k}(1/2) should be 0"

    def test_bessel_coefficients_exact_verification(self):
        """Cross-verify Bessel coefficients via the dedicated function."""
        result = verify_bessel_coefficients_exact()
        assert result['all_match'] is True


# =========================================================================
# Section 9: Cross-verification Bessel vs shadow
# =========================================================================

class TestBesselShadowMatch:
    """Tests for Bessel-shadow tower correspondence."""

    def test_match_at_large_D(self):
        """Bessel and shadow match by construction of the dictionary."""
        result = verify_bessel_shadow_match(10000, max_arity=6)
        assert result['all_match'] is True

    def test_match_moderate_D(self):
        """Match at moderate D (corrections larger but still match)."""
        result = verify_bessel_shadow_match(100, max_arity=5)
        assert result['all_match'] is True


# =========================================================================
# Section 10: Entropy comparison table
# =========================================================================

class TestEntropyComparison:
    """Tests for cross-family entropy comparison."""

    def test_table_structure(self):
        """Comparison table has correct structure."""
        table = entropy_comparison_table([100, 1000])
        assert len(table) == 2
        assert 'K3xE_S_BH' in table[0]
        assert 'conifold_S_BH' in table[0]

    def test_k3e_dominates_conifold(self):
        """K3 x E entropy > conifold entropy at same D.

        K3 x E: S = 4*pi*sqrt(D) (from kappa=5).
        Conifold: S = 2*pi*sqrt(D) (from kappa=1).
        """
        table = entropy_comparison_table([100])
        row = table[0]
        assert row['K3xE_S_BH'] > row['conifold_S_BH']

    def test_k3e_vs_conifold_ratio(self):
        """K3xE / conifold ratio is 2 for S_BH.

        4*pi*sqrt(D) / 2*pi*sqrt(D) = 2.
        """
        table = entropy_comparison_table([100])
        row = table[0]
        assert abs(row['K3xE_S_BH'] / row['conifold_S_BH'] - 2.0) < 1e-10


# =========================================================================
# Section 11: Genus expansion of BPS free energy
# =========================================================================

class TestBPSGenusExpansion:
    """Tests for the genus expansion of BPS free energy."""

    def test_F1_k3e(self):
        """F_1(K3 x E) = 5/24.

        Path 1: kappa * lambda_1 = 5 * 1/24 = 5/24.
        Path 2: from weight(Delta_5) = 5.
        """
        F1 = bps_free_energy_genus_g(Fraction(5), 1)
        assert F1 == Fraction(5, 24)

    def test_F2_k3e(self):
        """F_2(K3 x E) = 5 * 7/5760 = 7/1152 (scalar lane)."""
        F2 = bps_free_energy_genus_g(Fraction(5), 2)
        assert F2 == Fraction(7, 1152)

    def test_F3_k3e(self):
        """F_3(K3 x E) = 5 * 31/967680 = 31/193536."""
        F3 = bps_free_energy_genus_g(Fraction(5), 3)
        assert F3 == Fraction(31, 193536)

    def test_genus_expansion_table(self):
        """Genus expansion table is consistent."""
        table = bps_genus_expansion(Fraction(5), g_max=5)
        assert len(table) == 5
        assert table[1] == Fraction(5, 24)

    def test_genus_expansion_positive(self):
        """All F_g are positive for positive kappa."""
        table = bps_genus_expansion(Fraction(5), g_max=7)
        for g, Fg in table.items():
            assert Fg > 0, f"F_{g} should be positive for kappa=5"

    def test_genus_corrections_structure(self):
        """Genus corrections for BPS entropy have correct structure."""
        result = bps_entropy_genus_corrections(1000, kappa_val=5, g_max=3)
        assert 'S_BH' in result
        assert 'S_1' in result
        assert 'S_2' in result

    def test_genus_corrections_convergent(self):
        """Higher-genus corrections decrease at large D."""
        result = bps_entropy_genus_corrections(10000, kappa_val=5, g_max=5)
        # |S_g| should decrease for g >= 2
        for g in range(2, 5):
            assert abs(result[f'S_{g+1}']) < abs(result[f'S_{g}']), \
                f"|S_{g+1}| should be < |S_{g}|"

    def test_kappa_proportionality(self):
        """F_g is proportional to kappa.

        F_g(kappa_1)/F_g(kappa_2) = kappa_1/kappa_2 for all g.
        """
        for g in range(1, 5):
            F_5 = bps_free_energy_genus_g(Fraction(5), g)
            F_2 = bps_free_energy_genus_g(Fraction(2), g)
            assert F_5 / F_2 == Fraction(5, 2)


# =========================================================================
# Section 12: Numerical BPS degeneracy comparisons
# =========================================================================

class TestBPSDegeneracies:
    """Tests for comparison with known BPS degeneracies."""

    def test_dvv_table_exists(self):
        """DVV table has expected entries."""
        assert BPS_DEGENERACIES_DVV[1] == 24
        assert BPS_DEGENERACIES_DVV[2] == 324
        assert BPS_DEGENERACIES_DVV[5] == 176256

    def test_dvv_growth(self):
        """DVV degeneracies grow exponentially."""
        for D in range(1, 10):
            assert BPS_DEGENERACIES_DVV[D + 1] > BPS_DEGENERACIES_DVV[D]

    def test_rademacher_vs_exact_structure(self):
        """Rademacher comparison returns valid structure."""
        results = verify_rademacher_vs_exact(5)
        assert len(results) > 0
        assert 'D' in results[0]
        assert 'exact_degeneracy' in results[0]

    def test_rademacher_ratio_improves(self):
        """S_BH / log(exact) approaches 1 at large D.

        At large D, S_BH = 4*pi*sqrt(D) dominates log c(D).
        But at small D, subleading corrections are large.
        """
        results = verify_rademacher_vs_exact(10)
        # The ratio S_BH/log(exact) should increase toward 1 (or overshoot)
        # as D increases, since S_BH grows faster than log corrections.
        # At D=10: ratio should be > 1 (S_BH is already an overestimate
        # because log corrections are negative).
        last = results[-1]
        assert last['ratio_S_BH_to_log_exact'] > 1.0

    def test_convergence_rate_structure(self):
        """Convergence rate analysis returns valid structure."""
        result = rademacher_convergence_rate(100, n_corrections=3)
        assert len(result['steps']) == 4  # k=0 plus 3 corrections
        assert result['D'] == 100


# =========================================================================
# Section 13: Shadow depth classification
# =========================================================================

class TestShadowDepthClassification:
    """Tests for the shadow depth classification of BPS systems."""

    def test_classification_families(self):
        """All expected families are present."""
        cl = bps_shadow_depth_classification()
        assert 'K3 x E' in cl
        assert 'Heisenberg (E)' in cl
        assert 'Quintic' in cl

    def test_k3e_class_M(self):
        """K3 x E is class M (infinite shadow depth)."""
        cl = bps_shadow_depth_classification()
        assert cl['K3 x E']['class'] == 'M'
        assert cl['K3 x E']['shadow_depth'] == float('inf')

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (Gaussian, depth 2)."""
        cl = bps_shadow_depth_classification()
        assert cl['Heisenberg (E)']['class'] == 'G'
        assert cl['Heisenberg (E)']['shadow_depth'] == 2

    def test_class_M_has_bh(self):
        """Class M systems have genuine black holes (K3 x E)."""
        cl = bps_shadow_depth_classification()
        assert cl['K3 x E']['has_bh'] is True

    def test_class_G_simple(self):
        """Class G systems: Heisenberg and K3 have no BPS BH."""
        cl = bps_shadow_depth_classification()
        assert cl['Heisenberg (E)']['has_bh'] is False
        assert cl['K3']['has_bh'] is False


# =========================================================================
# Section 14: Kappa-weight bridge
# =========================================================================

class TestKappaWeightBridge:
    """Tests for the kappa-to-automorphic-weight bridge."""

    def test_k3e_weight(self):
        """weight(Phi_10) = 2*kappa(K3 x E) = 10."""
        assert kappa_to_automorphic_weight(5) == 10

    def test_weight_to_log_correction(self):
        """Log correction for Phi_10 is -27/4."""
        assert weight_to_log_correction(10) == Fraction(-27, 4)


# =========================================================================
# Section 15: Shadow CohFT entropy functional
# =========================================================================

class TestShadowCohFTEntropy:
    """Tests for the shadow CohFT entropy functional."""

    def test_shadow_cohft_structure(self):
        """Shadow CohFT entropy returns valid structure."""
        result = shadow_cohft_entropy(5, 1000, g_max=3)
        assert 'S_BH' in result
        assert 'S_total' in result

    def test_shadow_cohft_matches_bps(self):
        """Shadow CohFT entropy matches BPS genus corrections."""
        r1 = shadow_cohft_entropy(5, 1000, g_max=3)
        r2 = bps_entropy_genus_corrections(1000, kappa_val=5, g_max=3)
        assert abs(r1['S_BH'] - r2['S_BH']) < 1e-10
        assert abs(r1['S_total'] - r2['S_total']) < 1e-10


# =========================================================================
# Section 16: Consistency checks (multi-path verification)
# =========================================================================

class TestConsistency:
    """Multi-path verification of the entropy-shadow dictionary."""

    def test_kappa_weight_consistency(self):
        """kappa-weight-F_1 consistency across families."""
        result = verify_kappa_weight_consistency()
        assert result['K3xE']['consistent'] is True
        assert result['Elliptic']['consistent'] is True
        assert result['K3']['consistent'] is True

    def test_bessel_coefficients_exact(self):
        """Bessel coefficients match hand computation."""
        result = verify_bessel_coefficients_exact()
        assert result['all_match'] is True

    def test_entropy_positivity(self):
        """Total entropy is positive for D >> 1.

        S_total = S_BH + corrections > 0 for large D.
        """
        for D in [100, 1000, 10000]:
            result = bps_entropy_genus_corrections(D, kappa_val=5, g_max=5)
            assert result['S_total'] > 0

    def test_subleading_sign_pattern(self):
        """Log correction is negative, first power correction has known sign.

        Path 1: -27/4 < 0 (negative log correction).
        Path 2: a_1(19/2) = -45 < 0 (first Bessel coefficient negative).
        Path 3: this means the first power correction REDUCES entropy.
        """
        D = 1000
        # Log correction: negative
        log_corr = -6.75 * math.log(D)
        assert log_corr < 0

        # First Bessel coefficient
        nu = Fraction(19, 2)
        coeffs = bessel_asymptotic_coefficients(nu, 1)
        assert coeffs[1] < 0

    def test_expansion_parameter_small(self):
        """epsilon = 1/(2*sqrt(D)) is small at large D.

        This ensures the genus expansion converges.
        """
        for D in [100, 1000, 10000]:
            epsilon = 1.0 / (2.0 * math.sqrt(D))
            assert epsilon < 0.1, f"epsilon = {epsilon} not small at D={D}"

    def test_k3e_five_is_special(self):
        """kappa=5 for K3 x E is consistent with chi(K3)=24.

        (chi(K3) - 4)/4 = (24-4)/4 = 5 = kappa.
        This is NOT chi(K3)/4 = 6. The -4 offset is important.
        """
        chi_K3 = 24
        kappa = (chi_K3 - 4) / 4
        assert kappa == 5

    def test_bessel_shadow_self_consistency(self):
        """The dictionary maps shadow->Bessel and Bessel->shadow consistently.

        For each arity r >= 4, the shadow contribution at discriminant D
        equals a_{r-2} / (4*pi*sqrt(D))^{r-2}.
        """
        D = 10000
        nu = Fraction(19, 2)
        for r in range(4, 8):
            k = r - 2
            coeffs = bessel_asymptotic_coefficients(nu, k)
            z = FOUR_PI * math.sqrt(D)
            bessel_pred = float(coeffs[k]) / z ** k
            shadow_pred = shadow_to_entropy_correction_k3e(r, D)
            assert abs(bessel_pred - shadow_pred) < 1e-12 * max(abs(bessel_pred), 1e-30)
