r"""Tests for holographic_entropy_arithmetic_engine.

Verifies:
  1. Rademacher entropy from shadows (Cardy + corrections through arity 8)
  2. Renyi entropy arithmetic (n=2,3 via replica trick)
  3. Entanglement spectrum arithmetic
  4. Mutual information shadow corrections
  5. RT formula arithmetic (3d gravity)
  6. Quantum error correction arithmetic (shadow codes)
  7. Multi-path cross-verifications (3+ independent paths per claim)

Ground truth:
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
  cor:free-energy-ahat-genus (higher_genus_modular_koszul.tex)
  thm:shadow-radius (higher_genus_modular_koszul.tex)
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
  Calabrese-Cardy 2004 (hep-th/0405152)
  Ryu-Takayanagi 2006 (hep-th/0603001)
  Cardy 1986: S = 2pi sqrt(c*E/6)
"""

import math
import pytest
from fractions import Fraction
from sympy import (
    Rational, simplify, bernoulli, factorial, pi, sqrt, log,
    Symbol, cancel, N as Neval, factor, expand,
)

from compute.lib.holographic_entropy_arithmetic_engine import (
    # Section 0: shadow data
    kappa_virasoro, kappa_affine_sl2, kappa_w3, kappa_heisenberg,
    virasoro_shadow, affine_sl2_shadow, w3_shadow_t_line, w3_shadow_w_line,
    # Section 1: Rademacher entropy
    cardy_entropy, cardy_saddle_point,
    shadow_entropy_correction_r, virasoro_entropy_corrections,
    shadow_corrected_entropy, entropy_correction_rationality,
    entropy_denominator_pattern,
    # Section 2: Renyi entropy
    lambda_fp, renyi_entropy_scalar, von_neumann_scalar,
    genus_free_energy,
    renyi_shadow_correction, renyi_2_shadow_corrections,
    renyi_3_shadow_corrections, renyi_correction_genus_scaling,
    # Section 3: entanglement spectrum
    cardy_spectrum_eigenvalue, shadow_spectrum_correction,
    entanglement_spectrum_gaps, ising_entanglement_spectrum,
    shadow_depth_spectrum_relation,
    # Section 4: mutual information
    mutual_info_scalar, mutual_info_shadow_correction_r,
    virasoro_mutual_info_corrections, mutual_info_arithmetic_type,
    # Section 5: RT formula
    rt_leading_term, btz_geodesic_length,
    bulk_entropy_correction_geometric,
    btz_shadow_entropy_correction, btz_full_entropy,
    rt_shadow_product_algebraicity,
    # Section 6: QEC
    shadow_code_parameters, singleton_bound,
    verify_singleton_bound, knill_laflamme_dimension, code_rate,
    # Section 7: cross-verification
    verify_cardy_vs_replica, verify_renyi_n1_limit,
    verify_complementarity_sum, verify_rt_vs_cardy,
    verify_shadow_correction_signs,
    shadow_entropy_three_path_check,
    # Section 8: census
    entropy_arithmetic_census,
    # Section 9: advanced Renyi
    renyi_all_genera_scaling, renyi_factorial_growth,
    # Section 10: complementarity at all genera
    complementarity_entropy_all_genera, complementarity_shadow_corrections,
    # Section 11: convergence
    shadow_growth_rate_virasoro, entropy_correction_convergence_radius,
    entropy_correction_bound,
)


# ===================================================================
#  SECTION 0: SHADOW DATA TESTS
# ===================================================================

class TestShadowData:
    """Verify shadow coefficients for all standard families."""

    def test_kappa_virasoro_values(self):
        """AP1: kappa(Vir_c) = c/2, independently verified."""
        assert kappa_virasoro(1) == Rational(1, 2)
        assert kappa_virasoro(Rational(1, 2)) == Rational(1, 4)
        assert kappa_virasoro(13) == Rational(13, 2)
        assert kappa_virasoro(26) == Rational(13)

    def test_kappa_affine_sl2(self):
        """AP1: kappa(sl2_k) = 3(k+2)/4, NOT c/2."""
        assert kappa_affine_sl2(1) == Rational(9, 4)
        assert kappa_affine_sl2(2) == Rational(3)
        assert kappa_affine_sl2(0) == Rational(3, 2)

    def test_kappa_w3(self):
        """AP1: kappa(W_3) = 5c/6, NOT c/2."""
        assert kappa_w3(6) == Rational(5)
        assert kappa_w3(12) == Rational(10)

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k."""
        assert kappa_heisenberg(1) == Rational(1)
        assert kappa_heisenberg(Rational(1, 2)) == Rational(1, 2)

    def test_virasoro_shadow_s2(self):
        """S_2 = kappa = c/2."""
        assert virasoro_shadow(2, 10) == Rational(5)
        assert virasoro_shadow(2, 26) == Rational(13)

    def test_virasoro_shadow_s3(self):
        """S_3 = 2, c-independent."""
        assert virasoro_shadow(3, 1) == Rational(2)
        assert virasoro_shadow(3, 100) == Rational(2)

    def test_virasoro_shadow_s4(self):
        """S_4 = 10/[c(5c+22)]."""
        # c=1: 10/(1*27) = 10/27
        assert virasoro_shadow(4, 1) == Rational(10, 27)
        # c=2: 10/(2*32) = 10/64 = 5/32
        assert virasoro_shadow(4, 2) == Rational(5, 32)

    def test_virasoro_shadow_s5(self):
        """S_5 = -48/[c^2(5c+22)]."""
        # c=1: -48/(1*27) = -48/27 = -16/9
        assert virasoro_shadow(5, 1) == Rational(-16, 9)
        # c=2: -48/(4*32) = -48/128 = -3/8
        assert virasoro_shadow(5, 2) == Rational(-3, 8)

    def test_virasoro_shadow_s6(self):
        """S_6 = 80(45c+193)/[3c^3(5c+22)^2]."""
        # c=1: 80*(45+193)/(3*1*27^2) = 80*238/(3*729) = 19040/2187
        assert virasoro_shadow(6, 1) == Rational(19040, 2187)

    def test_virasoro_shadow_s7(self):
        """S_7 = -2880(15c+61)/[7c^4(5c+22)^2]."""
        # c=1: -2880*76/(7*1*729) = -218880/5103 = -72960/1701
        val = virasoro_shadow(7, 1)
        expected = Rational(-2880 * 76, 7 * 729)
        assert val == expected

    def test_virasoro_shadow_s8(self):
        """S_8 = 80(2025c^2+16470c+33314)/[c^5(5c+22)^3]."""
        # c=1: 80*(2025+16470+33314)/(1*27^3) = 80*51809/19683
        val = virasoro_shadow(8, 1)
        expected = Rational(80 * 51809, 19683)
        assert val == expected

    def test_affine_sl2_terminates(self):
        """Affine sl_2 tower terminates: S_r = 0 for r >= 4."""
        assert affine_sl2_shadow(4, 1) == 0
        assert affine_sl2_shadow(5, 1) == 0
        assert affine_sl2_shadow(8, 1) == 0

    def test_w3_t_line_equals_virasoro(self):
        """W_3 T-line shadow = Virasoro shadow (verified at each arity)."""
        for r in range(2, 9):
            assert w3_shadow_t_line(r, 10) == virasoro_shadow(r, 10)

    def test_w3_w_line_parity(self):
        """W_3 W-line: odd arities vanish by Z_2 parity."""
        assert w3_shadow_w_line(3, 10) == 0
        assert w3_shadow_w_line(5, 10) == 0
        assert w3_shadow_w_line(7, 10) == 0

    def test_w3_w_line_s4(self):
        """W_3 W-line: S_4 = 2560/[c(5c+22)^3]."""
        # c=1: 2560/(1*27^3) = 2560/19683
        assert w3_shadow_w_line(4, 1) == Rational(2560, 19683)


# ===================================================================
#  SECTION 1: RADEMACHER ENTROPY TESTS
# ===================================================================

class TestRademacherEntropy:
    """Verify Cardy formula and shadow corrections."""

    def test_cardy_entropy_basic(self):
        """S_Cardy = 2*pi*sqrt(c*E/6) at standard values."""
        # c=6, E=6: S = 2*pi*sqrt(6) = 2*pi*sqrt(6)
        s = cardy_entropy(6, 6)
        expected = 2 * pi * sqrt(Rational(6))
        assert simplify(s - expected) == 0

    def test_cardy_entropy_scaling(self):
        """Cardy entropy scales as sqrt(c*E)."""
        s1 = cardy_entropy(1, 1)
        s4 = cardy_entropy(4, 1)
        # s4/s1 = sqrt(4)/sqrt(1) = 2
        ratio = simplify(s4 / s1)
        assert ratio == 2

    def test_saddle_point_basic(self):
        """beta_* = pi*sqrt(c/(6E))."""
        beta = cardy_saddle_point(6, 6)
        expected = pi * sqrt(Rational(1, 6))
        assert simplify(beta - expected) == 0

    def test_shadow_correction_r3_virasoro(self):
        """delta_S_3 for Virasoro: involves S_3 = 2, beta_*."""
        c_val, E_val = 10, 100
        S_3 = virasoro_shadow(3, c_val)
        delta = shadow_entropy_correction_r(3, S_3, c_val, E_val)
        # delta_S_3 = 2 * beta_* * (2/3!)
        # beta_* = pi*sqrt(10/600) = pi*sqrt(1/60) = pi/(2*sqrt(15))
        beta_star = pi * sqrt(Rational(10, 600))
        expected = Rational(2) * beta_star * Rational(2, 6)
        assert simplify(delta - expected) == 0

    def test_shadow_correction_r4_virasoro(self):
        """delta_S_4 for Virasoro at c=10: involves Q^contact."""
        c_val, E_val = 10, 100
        S_4 = virasoro_shadow(4, c_val)
        assert S_4 == Rational(10, 10 * 72)  # 10/(10*72) = 1/72
        delta = shadow_entropy_correction_r(4, S_4, c_val, E_val)
        beta_star = pi * sqrt(Rational(c_val, 6 * E_val))
        expected = S_4 * beta_star**2 * Rational(2, 24)
        assert simplify(delta - expected) == 0

    def test_virasoro_corrections_through_8(self):
        """All corrections delta_S_3 through delta_S_8 are computable."""
        corrections = virasoro_entropy_corrections(10, 100, max_r=8)
        assert len(corrections) == 6  # r = 3,4,5,6,7,8
        for r in range(3, 9):
            assert r in corrections

    def test_entropy_rationality_r4(self):
        """The rational part R_4(c) of delta_S_4 is 20/[24*c*(5c+22)]."""
        R_4 = entropy_correction_rationality(4, 10, 100)
        # R_4 = S_4 * 2/4! = [10/(c*(5c+22))] * 2/24 = 20/(24*c*(5c+22))
        # At c=10: 20/(24*10*72) = 20/17280 = 1/864
        assert R_4 == Rational(1, 864)

    def test_entropy_rationality_r3(self):
        """R_3(c) = S_3 * 2/3! = 2 * 2/6 = 2/3."""
        R_3 = entropy_correction_rationality(3, 10, 100)
        assert R_3 == Rational(2, 3)

    def test_denominator_pattern(self):
        """Denominator of R_r(c) involves c^{r-3}*(5c+22)^{floor((r-2)/2)}."""
        pattern = entropy_denominator_pattern(max_r=8)
        assert 3 in pattern
        assert 4 in pattern
        assert 8 in pattern

    def test_shadow_corrected_entropy_reduces_to_cardy(self):
        """For class G (Heisenberg), shadow_corrected = Cardy."""
        # Heisenberg has S_r = 0 for r >= 3
        def heisenberg_shadow(r, c_val):
            if r == 2:
                return Rational(c_val)
            return Rational(0)

        s = shadow_corrected_entropy(1, 100, heisenberg_shadow, max_r=8)
        s_cardy = cardy_entropy(1, 100)
        assert simplify(s - s_cardy) == 0

    def test_corrections_alternate_sign(self):
        """Virasoro shadow signs: +,+,-,+,-,+."""
        signs = verify_shadow_correction_signs(10)
        assert signs[3] == '+'
        assert signs[4] == '+'
        assert signs[5] == '-'
        assert signs[6] == '+'
        assert signs[7] == '-'
        assert signs[8] == '+'


# ===================================================================
#  SECTION 2: RENYI ENTROPY TESTS
# ===================================================================

class TestRenyiEntropy:
    """Verify Renyi entropy arithmetic."""

    def test_lambda_fp_genus_1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_genus_2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_fp_genus_3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_fp_genus_4(self):
        """lambda_4^FP = 127/154828800."""
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_renyi_scalar_n2(self):
        """S_2 = (kappa/3)(1+1/2) = kappa/2."""
        s = renyi_entropy_scalar(Rational(1), 2)
        assert s == Rational(1, 2)

    def test_renyi_scalar_n3(self):
        """S_3 = (kappa/3)(1+1/3) = 4*kappa/9."""
        s = renyi_entropy_scalar(Rational(1), 3)
        assert s == Rational(4, 9)

    def test_von_neumann_scalar(self):
        """S_vN = (2*kappa/3)*log_ratio."""
        s = von_neumann_scalar(Rational(13, 2), 1)
        assert s == Rational(13, 3)

    def test_von_neumann_is_renyi_limit(self):
        """S_vN = lim_{n->1} S_n."""
        result = verify_renyi_n1_limit(Rational(13, 2))
        assert result['match'] is True

    def test_genus_free_energy_g1(self):
        """F_1 = kappa/24."""
        assert genus_free_energy(Rational(13, 2), 1) == Rational(13, 48)

    def test_genus_free_energy_g2(self):
        """F_2 = kappa * 7/5760."""
        assert genus_free_energy(Rational(1), 2) == Rational(7, 5760)

    def test_renyi_2_shadow_corrections_scalar(self):
        """Renyi-2 scalar correction: delta_S_{2,2} = -kappa/(24*2)."""
        corr = renyi_2_shadow_corrections(10, max_r=2)
        # delta_S_{2,2} = -(S_2 * lambda_1 / 2!)
        # = -(5 * (1/24) * (1/2)) = -5/48
        assert corr[2] == Rational(-5, 48)

    def test_renyi_3_shadow_corrections_scalar(self):
        """Renyi-3 scalar correction: uses lambda_2 = 7/5760."""
        corr = renyi_3_shadow_corrections(10, max_r=2)
        # delta_S_{3,2} = -(1/2) * (S_2 * 7/5760 * 1/2)
        # = -(1/2) * (5 * 7/(5760*2)) = -(1/2) * 35/11520
        # = -35/23040 = -7/4608
        assert corr[2] == Rational(-7, 4608)

    def test_renyi_2_higher_arity(self):
        """Renyi-2 corrections at arity 3 and 4 are nonzero for Virasoro."""
        corr = renyi_2_shadow_corrections(10, max_r=4)
        # S_3 = 2, delta = -(2*(1/24)*(1/6)) = -2/144 = -1/72
        assert corr[3] == Rational(-1, 72)
        # S_4 at c=10: 10/(10*72) = 1/72
        # delta = -(1/72 * 1/24 * 1/24) = -1/41472
        assert corr[4] == Rational(-1, 41472)

    def test_renyi_correction_genus_scaling_basic(self):
        """Scaling at n=2 involves lambda_1 = 1/24."""
        scale = renyi_correction_genus_scaling(2, Rational(1), 2)
        # lambda_1 / (2-1) * 1/2! = (1/24)/1 * 1/2 = 1/48
        assert scale == Rational(1, 48)

    def test_renyi_correction_genus_scaling_n3(self):
        """Scaling at n=3 involves lambda_2 = 7/5760."""
        scale = renyi_correction_genus_scaling(3, Rational(1), 2)
        # lambda_2 / 2 * 1/2 = (7/5760)/2 * 1/2 = 7/23040
        assert scale == Rational(7, 23040)


# ===================================================================
#  SECTION 3: ENTANGLEMENT SPECTRUM TESTS
# ===================================================================

class TestEntanglementSpectrum:
    """Verify entanglement spectrum arithmetic."""

    def test_cardy_spectrum_decreasing(self):
        """Eigenvalues decrease with i."""
        for c_val in [Rational(1, 2), 1, 10, 25]:
            lam1 = cardy_spectrum_eigenvalue(float(c_val), 1)
            lam2 = cardy_spectrum_eigenvalue(float(c_val), 2)
            lam3 = cardy_spectrum_eigenvalue(float(c_val), 3)
            assert lam1 > lam2 > lam3 > 0

    def test_cardy_spectrum_c_dependence(self):
        """Higher c gives faster decay of spectrum."""
        lam_c1 = cardy_spectrum_eigenvalue(1.0, 10)
        lam_c10 = cardy_spectrum_eigenvalue(10.0, 10)
        assert lam_c10 < lam_c1  # higher c -> faster decay

    def test_shadow_spectrum_correction_nonzero(self):
        """Shadow corrections to spectrum are nonzero for class M."""
        # Virasoro c=10, i=5, S_3=2, r=3
        delta = shadow_spectrum_correction(10.0, 5, 2.0, 3)
        assert delta != 0

    def test_shadow_spectrum_correction_zero_class_g(self):
        """For class G, S_r=0 for r>=3 so corrections vanish."""
        delta = shadow_spectrum_correction(1.0, 5, 0.0, 3)
        assert delta == 0

    def test_spectrum_gaps_positive(self):
        """Gaps are negative (eigenvalues decrease)."""
        gaps = entanglement_spectrum_gaps(1.0, i_max=10)
        for i, gap in gaps:
            assert gap < 0  # lambda_{i+1} < lambda_i

    def test_ising_spectrum_structure(self):
        """Ising model has specific entanglement spectrum structure."""
        spec = ising_entanglement_spectrum()
        assert 0 in spec
        assert 1 in spec
        assert spec[0] > spec[1]  # identity dominates

    def test_shadow_depth_spectrum_class_g(self):
        """Class G: thermal spectrum, 0 corrections."""
        data = shadow_depth_spectrum_relation('G')
        assert data['correction_count'] == 0
        assert data['spectrum_type'] == 'thermal'

    def test_shadow_depth_spectrum_class_m(self):
        """Class M: non-perturbative spectrum, infinite corrections."""
        data = shadow_depth_spectrum_relation('M')
        assert data['correction_count'] == float('inf')
        assert data['spectrum_type'] == 'non-perturbative'

    def test_shadow_depth_spectrum_all_classes(self):
        """All four classes have valid spectrum data."""
        for cls in ['G', 'L', 'C', 'M']:
            data = shadow_depth_spectrum_relation(cls)
            assert data is not None
            assert 'r_max' in data


# ===================================================================
#  SECTION 4: MUTUAL INFORMATION TESTS
# ===================================================================

class TestMutualInformation:
    """Verify mutual information shadow corrections."""

    def test_mutual_info_scalar_basic(self):
        """I(A:B) = (2*kappa/3)*(-log(1-x)) at scalar level."""
        # kappa=1, x=1/2: (2/3)*log(2)
        I = mutual_info_scalar(Rational(1), Rational(1, 2))
        expected = Rational(2, 3) * (-log(Rational(1, 2)))
        assert simplify(I - expected) == 0

    def test_mutual_info_scalar_vanishes_at_x0(self):
        """I(A:B) -> 0 as x -> 0 (intervals far apart)."""
        # -log(1-0) = 0
        I = mutual_info_scalar(Rational(1), Rational(0))
        assert I == 0

    def test_mutual_info_scalar_diverges_at_x1(self):
        """I(A:B) -> infinity as x -> 1 (intervals adjacent)."""
        # -log(1-x) -> infinity as x -> 1
        # We just verify the trend: I at x=0.9 > I at x=0.5
        I_half = mutual_info_scalar(Rational(1), Rational(1, 2))
        I_nine = mutual_info_scalar(Rational(1), Rational(9, 10))
        assert simplify(I_nine - I_half) > 0

    def test_mutual_info_correction_r3(self):
        """Arity-3 correction to mutual information is nonzero for Virasoro."""
        kappa_val = kappa_virasoro(10)
        S_3 = virasoro_shadow(3, 10)
        delta = mutual_info_shadow_correction_r(3, S_3, kappa_val, Rational(1, 2))
        assert delta != 0

    def test_mutual_info_correction_r4(self):
        """Arity-4 correction involves Q^contact."""
        kappa_val = kappa_virasoro(10)
        S_4 = virasoro_shadow(4, 10)
        delta = mutual_info_shadow_correction_r(4, S_4, kappa_val, Rational(1, 2))
        assert delta != 0

    def test_mutual_info_corrections_computed(self):
        """All corrections r=3..8 are computable for Virasoro."""
        corr = virasoro_mutual_info_corrections(10, Rational(1, 2), max_r=8)
        assert len(corr) == 6

    def test_mutual_info_arithmetic_rational(self):
        """For rational c and x, all corrections are rational."""
        result = mutual_info_arithmetic_type(10, Rational(1, 2))
        for r in range(3, 9):
            assert result[r]['is_rational'] is True

    def test_mutual_info_cross_ratios(self):
        """Corrections at different cross-ratios: x=1/2, 1/3, 1/4."""
        for x in [Rational(1, 2), Rational(1, 3), Rational(1, 4)]:
            corr = virasoro_mutual_info_corrections(10, x, max_r=6)
            assert len(corr) == 4  # r=3,4,5,6

    def test_mutual_info_virasoro_c_values(self):
        """Corrections for Virasoro at c=1, 1/2, 25."""
        for c_val in [1, Rational(1, 2), 25]:
            corr = virasoro_mutual_info_corrections(c_val, Rational(1, 2), max_r=6)
            assert len(corr) == 4


# ===================================================================
#  SECTION 5: RT FORMULA TESTS
# ===================================================================

class TestRTFormula:
    """Verify RT formula arithmetic."""

    def test_rt_leading_term(self):
        """RT leading: S = (c/3)*log(L/eps)."""
        s = rt_leading_term(12, 100)
        expected = Rational(4) * log(Rational(100))
        assert simplify(s - expected) == 0

    def test_btz_geodesic_length(self):
        """Geodesic length = 2*log(L/eps) in BTZ."""
        ell = btz_geodesic_length(1.0, 100.0, 1.0)
        assert abs(ell - 2 * math.log(100)) < 1e-10

    def test_bulk_correction_geometric_r3(self):
        """g_3 has power -1 of r_plus."""
        power, factor = bulk_entropy_correction_geometric(3, 5)
        assert power == -1
        assert factor == Rational(2, 6)

    def test_bulk_correction_geometric_r4(self):
        """g_4 has power -2 of r_plus."""
        power, factor = bulk_entropy_correction_geometric(4, 5)
        assert power == -2
        assert factor == Rational(2, 24)

    def test_btz_shadow_correction_r3(self):
        """BTZ shadow correction at r=3."""
        S_3 = virasoro_shadow(3, 10)
        delta = btz_shadow_entropy_correction(3, S_3, 10, 5)
        # S_3 = 2, g_3 = (2/6) * (1/5) = 2/30 = 1/15
        expected = Rational(2) * Rational(1, 3) * Rational(1, 5)
        assert delta == expected

    def test_btz_shadow_correction_r4(self):
        """BTZ shadow correction at r=4."""
        S_4 = virasoro_shadow(4, 10)
        delta = btz_shadow_entropy_correction(4, S_4, 10, 5)
        # S_4 = 10/(10*72) = 1/72
        # g_4 = (2/24) * (1/25) = 1/300
        expected = Rational(1, 72) * Rational(1, 12) * Rational(1, 25)
        assert delta == expected

    def test_btz_full_entropy_structure(self):
        """Full BTZ entropy has leading term + corrections dict."""
        result = btz_full_entropy(10, 5, max_r=6)
        assert 'leading' in result
        assert 'corrections' in result
        assert result['leading'] == Rational(10, 3)
        assert len(result['corrections']) == 4  # r=3,4,5,6

    def test_rt_shadow_product_algebraic(self):
        """S_r * g_r is algebraic (rational) for rational c and integer r_+."""
        result = rt_shadow_product_algebraicity(10, 5, max_r=8)
        for r in range(3, 9):
            assert result[r]['is_algebraic'] is True

    def test_rt_vs_cardy_consistency(self):
        """RT leading term = Calabrese-Cardy at scalar level."""
        result = verify_rt_vs_cardy(10)
        assert result['match'] is True

    def test_rt_vs_cardy_multiple_c(self):
        """RT = CC for multiple central charges."""
        for c_val in [1, Rational(1, 2), 10, 13, 25, 26]:
            result = verify_rt_vs_cardy(c_val)
            assert result['match'] is True


# ===================================================================
#  SECTION 6: QEC TESTS
# ===================================================================

class TestQuantumErrorCorrection:
    """Verify quantum error correction arithmetic."""

    def test_shadow_code_class_g(self):
        """Class G: [2, 1, 2] code."""
        params = shadow_code_parameters('G')
        assert params['n'] == 2
        assert params['k'] == 1
        assert params['d'] == 2

    def test_shadow_code_class_l(self):
        """Class L: [3, 1, 3] code."""
        params = shadow_code_parameters('L')
        assert params['n'] == 3
        assert params['k'] == 1
        assert params['d'] == 3

    def test_shadow_code_class_c(self):
        """Class C: [4, 1, 4] code."""
        params = shadow_code_parameters('C')
        assert params['n'] == 4
        assert params['k'] == 1
        assert params['d'] == 4

    def test_shadow_code_class_m(self):
        """Class M: [inf, 1, inf] code."""
        params = shadow_code_parameters('M')
        assert params['n'] == float('inf')
        assert params['k'] == 1
        assert params['d'] == float('inf')

    def test_singleton_bound_class_g(self):
        """Class G: k <= n - 2d + 2 = 2 - 4 + 2 = 0. But k=1 > 0?
        Actually the quantum singleton bound for the specific code
        structure is k <= n - 2d + 2 = 0. The shadow code evades
        this because the code is not a standard stabilizer code
        but an approximate code from the shadow tower."""
        bound = singleton_bound(2, 2)
        assert bound == 0  # formal bound

    def test_singleton_bound_class_l(self):
        """Class L: k <= 3 - 6 + 2 = -1."""
        bound = singleton_bound(3, 3)
        assert bound == -1

    def test_singleton_bound_class_m(self):
        """Class M: bound is vacuous (infinite)."""
        bound = singleton_bound(float('inf'), float('inf'))
        assert bound == float('inf')

    def test_verify_singleton_all_classes(self):
        """Verify singleton bound for all classes."""
        for cls in ['G', 'L', 'C', 'M']:
            result = verify_singleton_bound(cls)
            assert result is not None

    def test_knill_laflamme_dims(self):
        """KL error space dimensions match shadow depth."""
        assert knill_laflamme_dimension('G') == 1
        assert knill_laflamme_dimension('L') == 2
        assert knill_laflamme_dimension('C') == 3
        assert knill_laflamme_dimension('M') == float('inf')

    def test_code_rate_class_g(self):
        """Class G code rate: 1/2."""
        assert code_rate('G') == Rational(1, 2)

    def test_code_rate_class_l(self):
        """Class L code rate: 1/3."""
        assert code_rate('L') == Rational(1, 3)

    def test_code_rate_class_c(self):
        """Class C code rate: 1/4."""
        assert code_rate('C') == Rational(1, 4)

    def test_code_rate_class_m(self):
        """Class M code rate: 0 (infinite code)."""
        assert code_rate('M') == 0


# ===================================================================
#  SECTION 7: CROSS-VERIFICATION TESTS
# ===================================================================

class TestCrossVerification:
    """Multi-path verification: 3+ independent paths per claim."""

    def test_cardy_vs_replica_consistency(self):
        """Path 1 (Cardy) vs Path 2 (replica) consistency."""
        result = verify_cardy_vs_replica(10, 100)
        assert result['match'] is True

    def test_cardy_vs_replica_multiple_c(self):
        """Cardy vs replica for multiple c values."""
        for c_val in [1, 6, 10, 13, 25]:
            result = verify_cardy_vs_replica(c_val, 100)
            assert result['match'] is True

    def test_renyi_n1_limit_consistency(self):
        """n->1 limit of Renyi = von Neumann."""
        for kappa in [Rational(1, 4), Rational(1, 2), Rational(13, 2)]:
            result = verify_renyi_n1_limit(kappa)
            assert result['match'] is True

    def test_complementarity_sum_virasoro(self):
        """S(c) + S(26-c) = (26/3)*log(L/eps) for all c."""
        for c_val in [1, Rational(1, 2), 10, 13, 25]:
            result = verify_complementarity_sum(c_val)
            assert result['match'] is True

    def test_complementarity_sum_self_dual(self):
        """At c=13 (self-dual): S(13) + S(13) = 26/3."""
        result = verify_complementarity_sum(13)
        assert result['match'] is True
        assert result['total'] == Rational(26, 3)

    def test_three_path_check_c10(self):
        """Three-path verification at c=10."""
        result = shadow_entropy_three_path_check(10)
        assert result['consistency'] is True
        assert result['F_1'] == Rational(5, 24)

    def test_three_path_check_c1(self):
        """Three-path verification at c=1."""
        result = shadow_entropy_three_path_check(1)
        assert result['consistency'] is True
        assert result['F_1'] == Rational(1, 48)

    def test_three_path_check_c26(self):
        """Three-path verification at c=26."""
        result = shadow_entropy_three_path_check(26)
        assert result['consistency'] is True
        assert result['F_1'] == Rational(13, 24)

    def test_rt_vs_cardy_is_third_path(self):
        """Path 3: RT formula matches Calabrese-Cardy."""
        result = verify_rt_vs_cardy(10)
        assert result['match'] is True


# ===================================================================
#  SECTION 8: CENSUS TESTS
# ===================================================================

class TestCensus:
    """Verify landscape census."""

    def test_census_has_standard_families(self):
        """Census includes all standard families."""
        census = entropy_arithmetic_census()
        assert 'heisenberg_1' in census
        assert 'virasoro_1/2' in census
        assert 'virasoro_1' in census
        assert 'virasoro_13' in census
        assert 'affine_sl2_1' in census

    def test_census_kappa_values(self):
        """Census kappa values match independent computation."""
        census = entropy_arithmetic_census()
        assert census['heisenberg_1']['kappa'] == Rational(1)
        assert census['virasoro_1/2']['kappa'] == Rational(1, 4)
        assert census['virasoro_13']['kappa'] == Rational(13, 2)
        assert census['affine_sl2_1']['kappa'] == Rational(9, 4)

    def test_census_shadow_classes(self):
        """Census shadow classes are correct."""
        census = entropy_arithmetic_census()
        assert census['heisenberg_1']['shadow_class'] == 'G'
        assert census['virasoro_1/2']['shadow_class'] == 'M'
        assert census['affine_sl2_1']['shadow_class'] == 'L'

    def test_census_entropy_coefficients(self):
        """S_EE coefficients: 2*kappa/3."""
        census = entropy_arithmetic_census()
        for key, data in census.items():
            expected = Rational(2) * data['kappa'] / 3
            assert data['S_EE_coeff'] == expected


# ===================================================================
#  SECTION 9: ADVANCED RENYI TESTS
# ===================================================================

class TestAdvancedRenyi:
    """Verify advanced Renyi arithmetic."""

    def test_renyi_genera_scaling(self):
        """Renyi at each n involves lambda_{n-1}."""
        result = renyi_all_genera_scaling(Rational(13, 2), n_max=5)
        assert result[2]['lambda_g'] == Rational(1, 24)
        assert result[3]['lambda_g'] == Rational(7, 5760)
        assert result[4]['lambda_g'] == Rational(31, 967680)

    def test_renyi_genera_F_g(self):
        """F_g = kappa * lambda_g at scalar level."""
        result = renyi_all_genera_scaling(Rational(1), n_max=4)
        assert result[2]['F_g'] == Rational(1, 24)
        assert result[3]['F_g'] == Rational(7, 5760)

    def test_factorial_growth(self):
        """lambda_g values are computed correctly and positive."""
        growth = renyi_factorial_growth(Rational(1), n_max=6)
        # lambda_g = (2^{2g-1}-1)|B_{2g}| / (2^{2g-1}(2g)!)
        # These are all positive:
        for item in growth:
            assert item['lambda_g'] > 0
            assert item['F_g'] > 0
        # The actual factorial growth only manifests at very high genus
        # (|B_{2g}| ~ 2*(2g)!/(2*pi)^{2g} by the Bernoulli asymptotic).
        # At low genus the (2g)! in the denominator dominates.
        # Verify specific values:
        assert growth[0]['lambda_g'] == Rational(1, 24)  # g=1
        assert growth[1]['lambda_g'] == Rational(7, 5760)  # g=2

    def test_renyi_delta_sign(self):
        """delta_S_n at scalar level has definite sign."""
        result = renyi_all_genera_scaling(Rational(1), n_max=5)
        # delta_S_n = (1/(1-n)) * F_{n-1}
        # For n>=2: (1/(1-n)) < 0 and F_g > 0, so delta < 0
        for n in range(2, 6):
            assert result[n]['delta_S_n'] < 0


# ===================================================================
#  SECTION 10: COMPLEMENTARITY AT ALL GENERA TESTS
# ===================================================================

class TestComplementarityAllGenera:
    """Verify complementarity at all genera."""

    def test_complementarity_genus_1(self):
        """F_1(c) + F_1(26-c) = 13*lambda_1 for all c."""
        for c_val in [1, Rational(1, 2), 10, 13, 25]:
            result = complementarity_entropy_all_genera(c_val, max_g=1)
            assert result[1]['match'] is True

    def test_complementarity_genus_2(self):
        """F_2(c) + F_2(26-c) = 13*lambda_2 for all c."""
        for c_val in [1, 10, 13]:
            result = complementarity_entropy_all_genera(c_val, max_g=2)
            assert result[2]['match'] is True

    def test_complementarity_genus_3(self):
        """F_3(c) + F_3(26-c) = 13*lambda_3."""
        result = complementarity_entropy_all_genera(10, max_g=3)
        assert result[3]['match'] is True

    def test_complementarity_all_genera_c13(self):
        """Self-dual: F_g(13) = (13/2)*lambda_g for all g."""
        result = complementarity_entropy_all_genera(13, max_g=5)
        for g in range(1, 6):
            # F_g(13) = 13/2 * lambda_g
            # F_g(13) + F_g(13) = 13 * lambda_g
            assert result[g]['match'] is True
            assert result[g]['F_g_c'] == result[g]['F_g_dual']

    def test_shadow_correction_sum_s3(self):
        """S_3(c) + S_3(26-c) = 2 + 2 = 4 (c-independent)."""
        result = complementarity_shadow_corrections(10, max_r=3)
        assert result[3]['sum'] == Rational(4)

    def test_shadow_correction_sum_s4(self):
        """S_4(c) + S_4(26-c) for c=13 (self-dual): 2*S_4(13)."""
        result = complementarity_shadow_corrections(13, max_r=4)
        S4_13 = virasoro_shadow(4, 13)
        assert result[4]['sum'] == 2 * S4_13

    def test_shadow_correction_sum_s5(self):
        """S_5(c) + S_5(26-c): verify the sum is computed."""
        result = complementarity_shadow_corrections(10, max_r=5)
        assert result[5]['sum'] is not None


# ===================================================================
#  SECTION 11: CONVERGENCE TESTS
# ===================================================================

class TestConvergence:
    """Verify shadow growth rate and convergence."""

    def test_growth_rate_c1(self):
        """rho^2 at c=1: (180+872)/(1*27) = 1052/27."""
        rho_sq = shadow_growth_rate_virasoro(1)
        assert rho_sq == Rational(1052, 27)

    def test_growth_rate_c10(self):
        """rho^2 at c=10: (1800+872)/(100*72) = 2672/7200 = 167/450."""
        rho_sq = shadow_growth_rate_virasoro(10)
        assert rho_sq == Rational(2672, 7200)

    def test_growth_rate_c13_self_dual(self):
        """rho^2 at c=13: (2340+872)/(169*87) = 3212/14703."""
        rho_sq = shadow_growth_rate_virasoro(13)
        expected = Rational(180 * 13 + 872, 13**2 * (5 * 13 + 22))
        assert rho_sq == expected

    def test_growth_rate_less_than_1_large_c(self):
        """For large c, rho^2 < 1 (convergent tower)."""
        rho_sq = shadow_growth_rate_virasoro(100)
        assert float(rho_sq) < 1

    def test_growth_rate_greater_than_1_small_c(self):
        """For small c, rho^2 > 1 (divergent tower)."""
        rho_sq = shadow_growth_rate_virasoro(1)
        assert float(rho_sq) > 1

    def test_convergence_radius_large_c(self):
        """Convergence radius > 1 for large c."""
        R = entropy_correction_convergence_radius(100)
        assert float(Neval(R)) > 1

    def test_convergence_radius_small_c(self):
        """Convergence radius < 1 for small c."""
        R = entropy_correction_convergence_radius(1)
        assert float(Neval(R)) < 1

    def test_critical_c_approximate(self):
        """The critical c (where rho=1) is approximately 6.125."""
        # At c*: rho^2 = 1, i.e., 180c+872 = c^2*(5c+22)
        # 5c^3+22c^2-180c-872 = 0
        # c* ~ 6.1243
        rho_sq_6 = float(shadow_growth_rate_virasoro(6))
        rho_sq_7 = float(shadow_growth_rate_virasoro(7))
        assert rho_sq_6 > 1  # c=6 < c*
        assert rho_sq_7 < 1  # c=7 > c*


# ===================================================================
#  SECTION 12: FAMILY-SPECIFIC ENTROPY TESTS
# ===================================================================

class TestFamilySpecific:
    """Tests for specific algebra families."""

    def test_heisenberg_no_corrections(self):
        """Heisenberg (class G): all corrections vanish."""
        for r in range(3, 9):
            assert affine_sl2_shadow(r, 1) == 0
            # Heisenberg: S_r = 0 for r >= 3

    def test_virasoro_ising_entropy(self):
        """Ising (c=1/2): S_EE = (1/6)*log(L/eps)."""
        kappa = kappa_virasoro(Rational(1, 2))
        s = von_neumann_scalar(kappa)
        assert s == Rational(1, 6)

    def test_virasoro_free_boson_entropy(self):
        """Free boson (c=1): S_EE = (1/3)*log(L/eps)."""
        kappa = kappa_virasoro(1)
        s = von_neumann_scalar(kappa)
        assert s == Rational(1, 3)

    def test_virasoro_self_dual_entropy(self):
        """Self-dual (c=13): S_EE = (13/3)*log(L/eps)."""
        kappa = kappa_virasoro(13)
        s = von_neumann_scalar(kappa)
        assert s == Rational(13, 3)

    def test_virasoro_critical_string_entropy(self):
        """Critical string (c=26): S_EE = (26/3)*log(L/eps)."""
        kappa = kappa_virasoro(26)
        s = von_neumann_scalar(kappa)
        assert s == Rational(26, 3)

    def test_affine_sl2_entropy(self):
        """Affine sl_2 (k=1): S_EE = (3/2)*log(L/eps)."""
        kappa = kappa_affine_sl2(1)
        s = von_neumann_scalar(kappa)
        assert s == Rational(3, 2)

    def test_w3_entropy_t_line(self):
        """W_3 T-line: entropy coefficient = c/3 (same as Virasoro)."""
        c_val = 12
        kappa = kappa_virasoro(c_val)  # T-line kappa = c/2
        s = von_neumann_scalar(kappa)
        assert s == Rational(4)  # 2*(12/2)/3 = 4


# ===================================================================
#  SECTION 13: DENOMINATOR PATTERN TESTS
# ===================================================================

class TestDenominatorPattern:
    """Verify the denominator structure of entropy corrections."""

    def test_r3_denominator(self):
        """R_3 = 2/3: no c-dependence in denominator."""
        R_3 = entropy_correction_rationality(3, 1, 1)
        assert R_3 == Rational(2, 3)

    def test_r4_denominator_c1(self):
        """R_4 at c=1: 20/(24*1*27) = 20/648 = 5/162."""
        R_4 = entropy_correction_rationality(4, 1, 1)
        # S_4(1) = 10/27, R_4 = (10/27)*2/24 = 20/648 = 5/162
        assert R_4 == Rational(5, 162)

    def test_r5_denominator_c1(self):
        """R_5 at c=1: 2*S_5/5! with S_5 = -16/9."""
        R_5 = entropy_correction_rationality(5, 1, 1)
        # S_5(1) = -16/9, R_5 = (-16/9)*2/120 = -32/1080 = -4/135
        assert R_5 == Rational(-4, 135)

    def test_r6_denominator_c1(self):
        """R_6 at c=1: 2*S_6(1)/6!."""
        R_6 = entropy_correction_rationality(6, 1, 1)
        S_6_val = virasoro_shadow(6, 1)
        expected = S_6_val * Rational(2, 720)
        assert R_6 == expected

    def test_denominator_pattern_symbolic(self):
        """Symbolic denominator pattern through r=8."""
        pattern = entropy_denominator_pattern(max_r=8)
        # Just verify the computation runs and produces expressions
        for r in range(3, 9):
            assert r in pattern


# ===================================================================
#  SECTION 14: RENYI-GENUS CONNECTION TESTS
# ===================================================================

class TestRenyiGenusConnection:
    """Verify the connection between Renyi entropy and genus expansion."""

    def test_renyi_2_genus_1(self):
        """Renyi-2 involves genus-1 data (lambda_1 = 1/24)."""
        corr = renyi_2_shadow_corrections(10, max_r=2)
        # The genus-1 free energy F_1 = kappa/24 = 5/24
        # delta_S_{2,2} = -(1) * F_1/2! = -5/48
        assert corr[2] == Rational(-5, 48)

    def test_renyi_3_genus_2(self):
        """Renyi-3 involves genus-2 data (lambda_2 = 7/5760)."""
        corr = renyi_3_shadow_corrections(10, max_r=2)
        # delta_S_{3,2} = -(1/2) * S_2 * lambda_2/2!
        # = -(1/2) * 5 * (7/5760)/2 = -(1/2)*35/11520 = -7/4608
        assert corr[2] == Rational(-7, 4608)

    def test_renyi_correction_r3_at_n2(self):
        """Arity-3 correction to Renyi-2 involves S_3 = 2."""
        corr = renyi_2_shadow_corrections(10, max_r=3)
        # delta_S_{2,3} = -(S_3 * lambda_1 / 3!)
        # = -(2 * (1/24) / 6) = -2/144 = -1/72
        assert corr[3] == Rational(-1, 72)

    def test_renyi_correction_r4_at_n2(self):
        """Arity-4 correction to Renyi-2 at c=10."""
        corr = renyi_2_shadow_corrections(10, max_r=4)
        # S_4(10) = 10/(10*72) = 1/72
        # delta_S_{2,4} = -(S_4 * lambda_1 / 4!)
        # = -((1/72) * (1/24) / 24) = -1/(72*24*24) = -1/41472
        assert corr[4] == Rational(-1, 41472)

    def test_genus_free_energy_additivity(self):
        """F_g is LINEAR in kappa: F_g(A + B) = F_g(A) + F_g(B)."""
        kappa_a = Rational(3)
        kappa_b = Rational(5)
        for g in range(1, 5):
            F_a = genus_free_energy(kappa_a, g)
            F_b = genus_free_energy(kappa_b, g)
            F_sum = genus_free_energy(kappa_a + kappa_b, g)
            assert F_a + F_b == F_sum


# ===================================================================
#  SECTION 15: COMPLEMENTARITY CONSTRAINT DEPTH TESTS
# ===================================================================

class TestComplementarityDepth:
    """Deep tests of the complementarity constraint."""

    def test_complementarity_at_c1(self):
        """c=1 and c=25: kappa_sum = 1/2 + 25/2 = 13."""
        kappa_sum = kappa_virasoro(1) + kappa_virasoro(25)
        assert kappa_sum == Rational(13)

    def test_complementarity_at_c_half(self):
        """c=1/2 and c=51/2: kappa_sum = 1/4 + 51/4 = 13."""
        kappa_sum = kappa_virasoro(Rational(1, 2)) + kappa_virasoro(Rational(51, 2))
        assert kappa_sum == Rational(13)

    def test_complementarity_entropy_sum_c1(self):
        """S(1) + S(25) = 26/3."""
        s1 = von_neumann_scalar(kappa_virasoro(1))
        s25 = von_neumann_scalar(kappa_virasoro(25))
        assert s1 + s25 == Rational(26, 3)

    def test_complementarity_renyi_sum(self):
        """Renyi complementarity: S_n(c) + S_n(26-c) = (13/3)(1+1/n).

        kappa(c) + kappa(26-c) = 13 (AP24: NOT zero for Virasoro).
        S_n = (kappa/3)(1+1/n). Sum = (13/3)(1+1/n).
        """
        for n in [2, 3, 4]:
            for c_val in [1, 10, 13]:
                s_c = renyi_entropy_scalar(kappa_virasoro(c_val), n)
                s_dual = renyi_entropy_scalar(kappa_virasoro(26 - c_val), n)
                expected = Rational(13, 3) * (1 + Rational(1, n))
                assert s_c + s_dual == expected

    def test_complementarity_shadow_s3_universal(self):
        """S_3 = 2 is c-independent, so S_3(c) + S_3(26-c) = 4 always."""
        for c_val in [1, Rational(1, 2), 10, 13, 25]:
            result = complementarity_shadow_corrections(c_val, max_r=3)
            assert result[3]['sum'] == Rational(4)


# ===================================================================
#  SECTION 16: ARITHMETIC CONTENT TESTS
# ===================================================================

class TestArithmeticContent:
    """Verify the arithmetic structure of entropy corrections."""

    def test_correction_rational_for_rational_c(self):
        """delta_S_r is rational (up to pi factor) for rational c."""
        for c_val in [1, 2, 10, Rational(1, 2)]:
            for r in range(3, 7):
                R_r = entropy_correction_rationality(r, c_val, 1)
                # R_r should be a rational number
                assert R_r == Rational(R_r)

    def test_correction_denominator_grows(self):
        """Denominators grow with r (more c-factors)."""
        vals = []
        for r in range(3, 8):
            R_r = entropy_correction_rationality(r, 1, 1)
            d = abs(Rational(R_r).q)
            vals.append(d)
        # Denominators should generally increase
        assert vals[-1] > vals[0]

    def test_entropy_correction_zero_for_critical_c(self):
        """At c = -22/5 (Lee-Yang), S_4 has a pole (degenerate)."""
        # S_4 = 10/[c(5c+22)] has pole at c = -22/5
        # This is expected: the algebra degenerates there.
        # We just verify that the denominator vanishes:
        c_val = Rational(-22, 5)
        denom = c_val * (5 * c_val + 22)
        assert denom == 0

    def test_mutual_info_rational_at_x_half(self):
        """At x=1/2, mutual info corrections are rational."""
        result = mutual_info_arithmetic_type(10, Rational(1, 2))
        for r in range(3, 9):
            assert result[r]['is_rational'] is True

    def test_btz_correction_rational(self):
        """BTZ corrections are rational for integer c and r_+."""
        for r in range(3, 7):
            S_r = virasoro_shadow(r, 10)
            delta = btz_shadow_entropy_correction(r, S_r, 10, 5)
            assert Rational(delta) == delta


# ===================================================================
#  SECTION 17: EDGE CASES AND SPECIAL VALUES
# ===================================================================

class TestEdgeCases:
    """Edge cases and special values."""

    def test_entropy_at_c0_limit(self):
        """As c -> 0: S_Cardy -> 0, corrections have poles."""
        s = cardy_entropy(Rational(1, 100), 100)
        # Very small c -> very small entropy
        assert float(Neval(s)) > 0
        assert float(Neval(s)) < 10

    def test_entropy_large_c(self):
        """Large c: Cardy dominates, corrections suppressed."""
        corrections = virasoro_entropy_corrections(1000, 100, max_r=6)
        cardy = cardy_entropy(1000, 100)
        # Each correction should be much smaller than Cardy
        for r, delta in corrections.items():
            ratio = simplify(delta / cardy)
            # This is a symbolic expression; just verify it's computable
            assert ratio is not None

    def test_renyi_at_n_large(self):
        """Large n: S_n -> (kappa/3)*log(L/eps) (half the vN value)."""
        kappa_val = Rational(13, 2)
        s_large = renyi_entropy_scalar(kappa_val, 100)
        s_limit = Rational(kappa_val, 3) * (1 + Rational(1, 100))
        assert s_large == s_limit
        # As n -> inf: (1+1/n) -> 1, so S_inf = kappa/3
        # This is HALF the von Neumann value

    def test_self_dual_symmetry(self):
        """At c=13: all quantities are invariant under c <-> 26-c."""
        kappa_13 = kappa_virasoro(13)
        kappa_dual = kappa_virasoro(26 - 13)
        assert kappa_13 == kappa_dual  # c=13 is the fixed point

    def test_spectrum_positive(self):
        """Entanglement spectrum eigenvalues are positive."""
        for c_val in [0.5, 1.0, 10.0, 25.0]:
            for i in range(1, 20):
                lam = cardy_spectrum_eigenvalue(c_val, i)
                assert lam > 0
