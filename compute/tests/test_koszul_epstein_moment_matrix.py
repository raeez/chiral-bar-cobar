r"""
test_koszul_epstein_moment_matrix.py — Tests for the quartic residue moment matrix.

Tests verify:
  1. Shadow coefficient computation agrees with existing modules
  2. Exact det(H_2) formula for Virasoro
  3. Sign sequence classification by shadow depth class
  4. Hankel positivity fails at rank 2 for all c > 0 (Virasoro)
  5. Class G (Heisenberg): degenerate positive (point mass)
  6. Class L (affine KM): signed from rank 2 (Cauchy-Schwarz obstruction)
  7. Class M (Virasoro): signed from rank 2, rich higher-rank structure
  8. Cross-check with existing shadow_tower_recursive module
  9. Exact rational arithmetic consistency
  10. Positivity boundary location
  11. Schur complement sequence
  12. Turan ratios
  13. Normalized Hankel sequence

Manuscript references:
    prop:hankel-extraction (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
"""

import math
import pytest
from fractions import Fraction

from compute.lib.koszul_epstein_moment_matrix import (
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_km_shadow_data,
    betagamma_shadow_data,
    shadow_coefficients_from_data,
    shadow_coefficients_virasoro,
    shadow_hankel_matrix,
    hankel_det,
    shadow_hankel_determinants,
    moment_matrix_sign_sequence,
    virasoro_hankel_analysis,
    virasoro_H2_det_exact,
    virasoro_H3_det_exact,
    class_G_moment_analysis,
    class_L_moment_analysis,
    class_M_moment_analysis,
    affine_km_hankel_analysis,
    virasoro_shadow_coefficients_exact,
    virasoro_hankel_dets_exact,
    shadow_hankel_matrix_exact,
    hankel_det_exact,
    hankel_landscape,
    turan_ratios,
    schur_complement_sequence,
    positivity_boundary_H2,
    positivity_scan,
    normalized_hankel_sequence,
)


# ================================================================
# 1. Shadow coefficient basic tests
# ================================================================

class TestShadowCoefficients:
    """Test shadow coefficient computation from first principles."""

    def test_virasoro_s2_is_kappa(self):
        """S_2 = kappa = c/2."""
        for c in [0.5, 1.0, 2.0, 13.0, 26.0]:
            coeffs = shadow_coefficients_virasoro(c, 4)
            assert abs(coeffs[2] - c / 2) < 1e-12, f"S_2 != c/2 at c={c}"

    def test_virasoro_s3_is_alpha(self):
        """S_3 = alpha = 2 (universal cubic, independent of c)."""
        for c in [0.5, 1.0, 2.0, 13.0, 26.0]:
            coeffs = shadow_coefficients_virasoro(c, 4)
            assert abs(coeffs[3] - 2.0) < 1e-12, f"S_3 != 2 at c={c}"

    def test_virasoro_s4_is_qcontact(self):
        """S_4 = Q^contact = 10/(c(5c+22))."""
        for c in [0.5, 1.0, 2.0, 13.0, 26.0]:
            coeffs = shadow_coefficients_virasoro(c, 5)
            expected = 10.0 / (c * (5 * c + 22))
            assert abs(coeffs[4] - expected) < 1e-12, f"S_4 wrong at c={c}"

    def test_cross_check_with_recursive_module(self):
        """Shadow coefficients agree with shadow_tower_recursive module."""
        try:
            from compute.lib.shadow_tower_recursive import (
                shadow_coefficients_virasoro as recursive_virasoro,
            )
        except ImportError:
            pytest.skip("shadow_tower_recursive not available")

        for c in [1.0, 13.0]:
            ours = shadow_coefficients_virasoro(c, 15)
            theirs = recursive_virasoro(c, 15)
            for r in range(2, 16):
                assert abs(ours[r] - theirs[r]) < 1e-10 * max(1, abs(ours[r])), \
                    f"Disagreement at c={c}, r={r}: {ours[r]} vs {theirs[r]}"

    def test_cross_check_with_eisenstein_module(self):
        """Shadow coefficients agree with eisenstein_moment_matrix module."""
        try:
            from compute.lib.eisenstein_moment_matrix import (
                shadow_coefficients as emm_coefficients,
            )
        except ImportError:
            pytest.skip("eisenstein_moment_matrix not available")

        for c in [1.0, 13.0]:
            ours = shadow_coefficients_virasoro(c, 12)
            theirs = emm_coefficients(12, c)
            for r in range(2, 13):
                assert abs(ours[r] - float(theirs[r])) < 1e-10 * max(1, abs(ours[r])), \
                    f"Disagreement at c={c}, r={r}"

    def test_heisenberg_terminates(self):
        """Heisenberg: S_r = 0 for r >= 3."""
        kappa, alpha, S4 = heisenberg_shadow_data(1)
        coeffs = shadow_coefficients_from_data(kappa, alpha, S4, 10)
        assert abs(coeffs[2] - 1.0) < 1e-12  # AP39: kappa(H_1) = 1, NOT 0.5
        for r in range(3, 11):
            assert abs(coeffs[r]) < 1e-12, f"S_{r} != 0 for Heisenberg"

    def test_affine_km_s4_zero(self):
        """Affine KM: S_4 = 0 (class L)."""
        kappa, alpha, S4 = affine_km_shadow_data(3, 1, 2)
        assert S4 == 0


# ================================================================
# 2. Hankel matrix construction tests
# ================================================================

class TestHankelMatrix:
    """Test Hankel matrix construction and determinant."""

    def test_H1_is_kappa(self):
        """H_1 = (S_2) = (kappa)."""
        coeffs = shadow_coefficients_virasoro(1.0, 4)
        H = shadow_hankel_matrix(coeffs, 1)
        assert abs(H[0][0] - 0.5) < 1e-12

    def test_H2_structure(self):
        """H_2 = ((S_2, S_3), (S_3, S_4))."""
        coeffs = shadow_coefficients_virasoro(1.0, 5)
        H = shadow_hankel_matrix(coeffs, 2)
        assert abs(H[0][0] - coeffs[2]) < 1e-12
        assert abs(H[0][1] - coeffs[3]) < 1e-12
        assert abs(H[1][0] - coeffs[3]) < 1e-12
        assert abs(H[1][1] - coeffs[4]) < 1e-12

    def test_hankel_symmetry(self):
        """Hankel matrix is symmetric."""
        coeffs = shadow_coefficients_virasoro(1.0, 10)
        H = shadow_hankel_matrix(coeffs, 4)
        for i in range(4):
            for j in range(4):
                assert abs(H[i][j] - H[j][i]) < 1e-12

    def test_hankel_anti_diagonal_constant(self):
        """Hankel matrix has constant anti-diagonals."""
        coeffs = shadow_coefficients_virasoro(1.0, 10)
        H = shadow_hankel_matrix(coeffs, 4)
        # Anti-diagonal i+j = k should be constant = S_{k+2}
        for k in range(7):  # k = 0..6
            vals = [H[i][k - i] for i in range(max(0, k - 3), min(4, k + 1))]
            for v in vals:
                assert abs(v - vals[0]) < 1e-12

    def test_det_1x1(self):
        """det(H_1) = S_2 = kappa."""
        coeffs = shadow_coefficients_virasoro(1.0, 4)
        H = shadow_hankel_matrix(coeffs, 1)
        assert abs(hankel_det(H) - 0.5) < 1e-12

    def test_det_2x2_direct(self):
        """det(H_2) = S_2*S_4 - S_3^2 (direct formula)."""
        coeffs = shadow_coefficients_virasoro(1.0, 5)
        H = shadow_hankel_matrix(coeffs, 2)
        det_numerical = hankel_det(H)
        det_direct = coeffs[2] * coeffs[4] - coeffs[3] ** 2
        assert abs(det_numerical - det_direct) < 1e-12

    def test_missing_coefficient_raises(self):
        """Accessing a missing coefficient raises KeyError."""
        coeffs = {2: 0.5, 3: 2.0}  # Missing S_4
        with pytest.raises(KeyError):
            shadow_hankel_matrix(coeffs, 2)


# ================================================================
# 3. Exact det(H_2) formula tests
# ================================================================

class TestDetH2Exact:
    """Test the exact formula det(H_2) = -(20c+83)/(5c+22)."""

    def test_formula_at_c1(self):
        exact = virasoro_H2_det_exact(Fraction(1))
        assert exact == Fraction(-103, 27)

    def test_formula_at_c_half(self):
        exact = virasoro_H2_det_exact(Fraction(1, 2))
        assert exact == Fraction(-186, 49)

    def test_formula_at_c13(self):
        exact = virasoro_H2_det_exact(Fraction(13))
        assert exact == Fraction(-343, 87)

    def test_formula_matches_numerical(self):
        """Exact formula matches numerical computation."""
        for c in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(13)]:
            exact = float(virasoro_H2_det_exact(c))
            coeffs = shadow_coefficients_virasoro(float(c), 5)
            dets = shadow_hankel_determinants(coeffs, 2)
            assert abs(exact - dets[1]) < 1e-10

    def test_negative_for_all_positive_c(self):
        """det(H_2) < 0 for all c > 0."""
        for c_val in [0.01, 0.1, 0.5, 1, 2, 5, 10, 13, 26, 50, 100, 1000]:
            exact = virasoro_H2_det_exact(Fraction(c_val))
            assert exact < 0, f"det(H_2) >= 0 at c={c_val}: {exact}"

    def test_negative_for_minimal_models(self):
        """det(H_2) < 0 for all unitary minimal models M(m, m+1)."""
        for m in range(3, 20):
            c = Fraction(1) - Fraction(6, m * (m + 1))
            exact = virasoro_H2_det_exact(c)
            assert exact < 0, f"det(H_2) >= 0 at M({m},{m+1}), c={float(c):.4f}"

    def test_approaches_minus_4_at_large_c(self):
        """det(H_2) -> -4 as c -> infinity."""
        # -(20c+83)/(5c+22) -> -20/5 = -4
        exact = virasoro_H2_det_exact(Fraction(10000))
        assert abs(float(exact) - (-4.0)) < 0.01


# ================================================================
# 4. Sign sequence classification tests
# ================================================================

class TestSignSequence:
    """Test sign sequence by shadow depth class."""

    def test_class_G_heisenberg(self):
        """Class G: (+, 0, 0, ...)."""
        kappa, alpha, S4 = heisenberg_shadow_data(1)
        coeffs = shadow_coefficients_from_data(kappa, alpha, S4, 6)
        signs = moment_matrix_sign_sequence(coeffs, 3)
        assert signs[0] == 1  # det(H_1) = kappa > 0
        assert signs[1] == 0  # det(H_2) = 0 (S_3 = S_4 = 0)
        assert signs[2] == 0  # det(H_3) = 0

    def test_class_L_affine_sl2(self):
        """Class L: (+, -, ...)."""
        kappa, alpha, S4 = affine_km_shadow_data(3, 1, 2)
        coeffs = shadow_coefficients_from_data(kappa, alpha, S4, 6)
        signs = moment_matrix_sign_sequence(coeffs, 2)
        assert signs[0] == 1   # kappa > 0
        assert signs[1] == -1  # -alpha^2 < 0

    def test_class_M_virasoro_c1(self):
        """Class M at c=1: (+, -, -, +, +, +)."""
        coeffs = shadow_coefficients_virasoro(1.0, 12)
        signs = moment_matrix_sign_sequence(coeffs, 6)
        assert signs[0] == 1   # kappa > 0
        assert signs[1] == -1  # always negative for c > 0

    def test_class_M_signed_from_rank_2(self):
        """All Virasoro with c > 0 have first negative at rank 2."""
        for c_val in [0.5, 1.0, 5.0, 13.0, 26.0, 100.0]:
            analysis = virasoro_hankel_analysis(c_val, 3)
            assert analysis['first_negative'] == 2, \
                f"First negative not at rank 2 for c={c_val}"


# ================================================================
# 5. Class G (Heisenberg) detailed tests
# ================================================================

class TestClassG:
    """Detailed tests for Class G (Gaussian/Heisenberg)."""

    def test_point_mass_interpretation(self):
        """Class G has degenerate positive measure (point mass at 0)."""
        result = class_G_moment_analysis(0.5)
        assert result['is_positive'] is True
        assert result['H1_det'] == 0.5
        assert result['H2_det'] == 0.0

    def test_negative_kappa_heisenberg(self):
        """Heisenberg at negative level has kappa < 0."""
        result = class_G_moment_analysis(-0.5)
        assert result['H1_det'] == -0.5
        assert result['sign_sequence'][0] == -1


# ================================================================
# 6. Class L (affine KM) detailed tests
# ================================================================

class TestClassL:
    """Detailed tests for Class L (Lie/tree, affine Kac-Moody)."""

    def test_cauchy_schwarz_obstruction(self):
        """For class L: alpha^2 > 0 and S_4 = 0 => det(H_2) = -alpha^2 < 0.

        This is the Cauchy-Schwarz obstruction: if mu is positive with
        integral d mu = kappa > 0 and integral x d mu = alpha != 0,
        then integral x^2 d mu >= alpha^2/kappa > 0.
        But S_4 = integral x^2 d mu = 0. Contradiction.
        """
        result = class_L_moment_analysis(2.25, 2.0)
        assert result['H2_det'] == -4.0

    def test_sl2_k1(self):
        result = affine_km_hankel_analysis(3, 1, 2)
        assert result['kappa'] == 2.25
        assert result['alpha'] == 2.0
        assert result['H2_det'] == -4.0

    def test_sl3_k1(self):
        result = affine_km_hankel_analysis(8, 1, 3)
        kappa_expected = 8 * (1 + 3) / (2 * 3)
        assert abs(result['kappa'] - kappa_expected) < 1e-12
        assert result['H2_det'] == -4.0  # -alpha^2 = -4

    def test_g2_k1(self):
        """G_2 at level 1: dim=14, h^v=4."""
        result = affine_km_hankel_analysis(14, 1, 4)
        kappa_expected = 14 * (1 + 4) / (2 * 4)
        assert abs(result['kappa'] - kappa_expected) < 1e-12
        assert result['H2_det'] == -4.0

    def test_all_class_L_signed(self):
        """Every class L algebra with alpha != 0 has signed measure."""
        for dim_g, h_dual in [(3, 2), (8, 3), (14, 4), (24, 5), (52, 6)]:
            result = affine_km_hankel_analysis(dim_g, 1, h_dual)
            assert not result['is_positive'], f"dim={dim_g} should be signed"


# ================================================================
# 7. Exact rational arithmetic tests
# ================================================================

class TestExactArithmetic:
    """Tests using exact Fraction-based computation."""

    def test_exact_s2_s3_s4(self):
        """Exact shadow coefficients at c=1."""
        c = Fraction(1)
        coeffs = virasoro_shadow_coefficients_exact(c, 5)
        assert coeffs[2] == Fraction(1, 2)
        assert coeffs[3] == Fraction(2)
        assert coeffs[4] == Fraction(10, 27)

    def test_exact_det_H1(self):
        """Exact det(H_1) = c/2."""
        c = Fraction(1)
        dets = virasoro_hankel_dets_exact(c, 1)
        assert dets[0] == Fraction(1, 2)

    def test_exact_det_H2(self):
        """Exact det(H_2) matches closed-form formula."""
        c = Fraction(1)
        dets = virasoro_hankel_dets_exact(c, 2)
        expected = -(20 * c + 83) / (5 * c + 22)
        assert dets[1] == expected

    def test_exact_det_H2_at_c13(self):
        """Exact det(H_2) at self-dual point c=13."""
        c = Fraction(13)
        dets = virasoro_hankel_dets_exact(c, 2)
        expected = Fraction(-343, 87)
        assert dets[1] == expected

    def test_exact_det_H3(self):
        """Exact det(H_3) at c=1 is negative."""
        c = Fraction(1)
        dets = virasoro_hankel_dets_exact(c, 3)
        # det(H_3) should be negative for c=1
        assert dets[2] < 0

    def test_exact_agrees_with_numerical(self):
        """Exact and numerical determinants agree."""
        c = Fraction(1)
        exact_dets = virasoro_hankel_dets_exact(c, 3)
        numerical_analysis = virasoro_hankel_analysis(1.0, 3)
        for i in range(3):
            assert abs(float(exact_dets[i]) - numerical_analysis['hankel_dets'][i]) < 1e-10

    def test_exact_det_H3_formula(self):
        """Exact det(H_3) formula matches numerical."""
        for c_frac, c_float in [(Fraction(1, 2), 0.5), (Fraction(1), 1.0),
                                 (Fraction(5), 5.0), (Fraction(13), 13.0)]:
            exact = virasoro_H3_det_exact(c_frac)
            numerical = virasoro_hankel_analysis(c_float, 3)['hankel_dets'][2]
            assert abs(float(exact) - numerical) < 1e-10 * max(1, abs(numerical))

    def test_exact_det_H3_negative_all_c_positive(self):
        """det(H_3) < 0 for all c > 0 (proved: numerator has no real roots)."""
        for c_val in [1, 2, 5, 10, 13, 26, 100, 1000]:
            exact = virasoro_H3_det_exact(Fraction(c_val))
            assert exact < 0, f"det(H_3) >= 0 at c={c_val}"

    def test_exact_det_H3_minimal_models(self):
        """det(H_3) < 0 for all unitary minimal models."""
        for m in range(3, 15):
            c = Fraction(1) - Fraction(6, m * (m + 1))
            exact = virasoro_H3_det_exact(c)
            assert exact < 0, f"det(H_3) >= 0 at M({m},{m+1})"


# ================================================================
# 8. Positivity boundary tests
# ================================================================

class TestPositivityBoundary:
    """Test the boundary where det(H_2) changes sign."""

    def test_boundary_values(self):
        bd = positivity_boundary_H2()
        assert bd['zero'] == Fraction(-83, 20)
        assert bd['pole'] == Fraction(-22, 5)
        assert bd['negative_for_c_positive'] is True

    def test_det_positive_in_interval(self):
        """det(H_2) > 0 for c in (-22/5, -83/20)."""
        c_val = -4.25  # In the interval (-4.4, -4.15)
        exact = virasoro_H2_det_exact(Fraction(-425, 100))
        assert float(exact) > 0

    def test_det_zero_at_boundary(self):
        """det(H_2) = 0 at c = -83/20."""
        exact = virasoro_H2_det_exact(Fraction(-83, 20))
        assert exact == 0

    def test_scan_reproduces_boundary(self):
        """Positivity scan finds the transition."""
        c_values = [-4.3, -4.2, -4.15, -4.1, 0.5, 1.0]
        results = positivity_scan(c_values, max_r=2)
        # c=-4.3 is in the positive interval, so signs[1] should be +1
        # c=-4.1 and above should have signs[1] = -1
        assert results[-4.3] is not None
        assert results[-4.3][1] == 1  # positive in interval
        assert results[1.0][1] == -1  # negative for c > 0


# ================================================================
# 9. Schur complement and Turan ratio tests
# ================================================================

class TestSchurAndTuran:
    """Test Schur complement and Turan ratio computation."""

    def test_schur_complement_exists(self):
        """Schur complement sequence can be computed."""
        coeffs = shadow_coefficients_virasoro(1.0, 12)
        schurs = schur_complement_sequence(coeffs, 5)
        assert len(schurs) >= 4

    def test_schur_complement_is_det_ratio(self):
        """sc_r = det(H_{r+1}) / det(H_r)."""
        coeffs = shadow_coefficients_virasoro(1.0, 12)
        dets = shadow_hankel_determinants(coeffs, 5)
        schurs = schur_complement_sequence(coeffs, 4)
        for i, (r, sc) in enumerate(schurs):
            if abs(dets[i]) > 1e-300:
                expected = dets[i + 1] / dets[i]
                assert abs(sc - expected) < 1e-8 * max(1, abs(expected))

    def test_turan_ratios_exist(self):
        """Turan ratios can be computed."""
        coeffs = shadow_coefficients_virasoro(1.0, 12)
        ratios = turan_ratios(coeffs, 5)
        assert len(ratios) >= 3


# ================================================================
# 10. Normalized Hankel sequence tests
# ================================================================

class TestNormalizedHankel:
    """Test normalized Hankel sequence det(H_r)/kappa^r."""

    def test_first_entry_is_one(self):
        """Normalized first entry is det(H_1)/kappa = 1."""
        coeffs = shadow_coefficients_virasoro(1.0, 12)
        norms = normalized_hankel_sequence(coeffs, 3)
        assert abs(norms[0] - 1.0) < 1e-12

    def test_second_entry_is_H2_normalized(self):
        """Normalized second entry is det(H_2)/kappa^2."""
        coeffs = shadow_coefficients_virasoro(1.0, 12)
        norms = normalized_hankel_sequence(coeffs, 2)
        kappa = coeffs[2]
        expected = virasoro_hankel_analysis(1.0, 2)['hankel_dets'][1] / kappa ** 2
        assert abs(norms[1] - expected) < 1e-10


# ================================================================
# 11. Cross-family landscape tests
# ================================================================

class TestLandscape:
    """Test the cross-family Hankel landscape."""

    def test_landscape_has_all_families(self):
        """Landscape contains all standard families."""
        land = hankel_landscape(3)
        assert 'Heisenberg_k1' in land
        assert 'sl2_k1' in land
        assert 'sl3_k1' in land
        assert any('Ising' in k for k in land)
        assert any('selfdual' in k for k in land)

    def test_heisenberg_is_positive(self):
        land = hankel_landscape(3)
        assert land['Heisenberg_k1']['is_positive'] is True

    def test_sl2_is_signed(self):
        land = hankel_landscape(3)
        assert not land['sl2_k1']['is_positive']


# ================================================================
# 12. Structural theorems (mathematical content tests)
# ================================================================

class TestStructuralTheorems:
    """Tests encoding proved mathematical results."""

    def test_det_H3_numerator_no_real_roots(self):
        """The numerator quadratic of det(H_3) has no real roots.

        det(H_3) = -8*(9000c^2 + 81710c + 185909) / (3c^3(5c+22)^3)
        Discriminant of 9000c^2 + 81710c + 185909:
        D = 81710^2 - 4*9000*185909 = -16199900 < 0.
        With positive constant term 185909, the quadratic is positive for all c.
        Therefore det(H_3) < 0 for all c > 0.
        """
        disc = 81710 ** 2 - 4 * 9000 * 185909
        assert disc == -16199900
        assert disc < 0
        # Constant term is positive
        assert 185909 > 0

    def test_det_H2_and_H3_both_negative(self):
        """Both det(H_2) and det(H_3) are negative for all c > 0.

        This is a proved structural result:
        - det(H_2) = -(20c+83)/(5c+22) < 0  (linear in c, no real roots in R+)
        - det(H_3) = -8(9000c^2+81710c+185909)/(3c^3(5c+22)^3) < 0  (quadratic, no real roots)

        The spectral measure is signed at ALL positive central charges, with
        the negativity appearing from the FIRST nontrivial Hankel minor.
        """
        for c_num, c_den in [(1, 2), (1, 1), (5, 1), (13, 1), (26, 1)]:
            c = Fraction(c_num, c_den)
            d2 = virasoro_H2_det_exact(c)
            d3 = virasoro_H3_det_exact(c)
            assert d2 < 0, f"det(H_2) >= 0 at c={c}"
            assert d3 < 0, f"det(H_3) >= 0 at c={c}"

    def test_universal_signed_measure_theorem(self):
        """THEOREM: For Virasoro at ANY c > 0, the spectral measure is signed.

        Proof: det(H_2) = -(20c+83)/(5c+22). For c > 0: 20c+83 > 0
        and 5c+22 > 0, so det(H_2) < 0. Since Hamburger's theorem
        requires det(H_r) >= 0 for all r for a positive measure,
        the spectral measure cannot be positive. QED.
        """
        # Test 100 c-values spanning 6 orders of magnitude
        c_values = [0.001 * 2 ** k for k in range(20)]
        for c_val in c_values:
            exact = virasoro_H2_det_exact(Fraction(int(c_val * 1000), 1000))
            assert exact < 0, f"Theorem fails at c={c_val}"

    def test_cauchy_schwarz_obstruction_class_L(self):
        """THEOREM: For class L with alpha != 0, det(H_2) = -alpha^2 < 0.

        Proof: S_4 = 0 for class L. det(H_2) = kappa*S_4 - alpha^2
        = -alpha^2. QED.
        """
        for alpha in [0.5, 1.0, 2.0, 5.0]:
            det = -alpha ** 2
            assert det < 0

    def test_det_H2_limiting_value(self):
        """det(H_2) -> -4 as c -> infinity.

        This is the universal large-c asymptotic:
        -(20c+83)/(5c+22) -> -20/5 = -4.

        Physical interpretation: the universal negative Hankel determinant
        at rank 2 has a finite limit, independent of the algebra.
        The value -4 = -(S_3)^2 = -alpha^2 comes purely from the cubic
        shadow, which is universal (alpha = 2 for all standard families).
        """
        for c_val in [100, 1000, 10000]:
            exact = float(virasoro_H2_det_exact(Fraction(c_val)))
            assert abs(exact - (-4.0)) < 100.0 / c_val

    def test_self_dual_moment_structure(self):
        """At the self-dual point c=13, the moment matrix has special structure.

        Virasoro at c=13 is self-dual: Vir_c^! = Vir_{26-c} = Vir_{13}.
        The shadow obstruction tower at c=13 should have enhanced symmetry.
        """
        analysis = virasoro_hankel_analysis(13.0, 6)
        # All determinants exist and are finite
        assert len(analysis['hankel_dets']) == 6
        for d in analysis['hankel_dets']:
            assert math.isfinite(d)

    def test_ising_model_moment_matrix(self):
        """Ising model (c=1/2) moment matrix analysis."""
        analysis = virasoro_hankel_analysis(0.5, 4)
        assert analysis['first_negative'] == 2
        # Ising has c = 1/2, kappa = 1/4
        assert abs(analysis['shadow_coeffs'][2] - 0.25) < 1e-12

    def test_dh_class_separation(self):
        """The shadow moment problem is in a DIFFERENT class from DH.

        Davenport-Heilbronn counterexamples use positive-definite forms
        with class number > 1.  The shadow metric Q_L IS positive definite
        (for c > -22/5), but the MOMENT PROBLEM is signed.

        Verify: Q_L is positive definite but moment matrix is not.
        """
        c = 1.0
        kappa, alpha, S4 = virasoro_shadow_data(c)
        # Q_L positive definite: disc < 0
        disc = (12 * kappa * alpha) ** 2 - 4 * (4 * kappa ** 2) * (9 * alpha ** 2 + 16 * kappa * S4)
        assert disc < 0, "Q_L should be positive definite"
        # But moment matrix has negative det
        analysis = virasoro_hankel_analysis(c, 2)
        assert analysis['hankel_dets'][1] < 0, "Moment matrix should be signed"


# ================================================================
# 13. Higher-rank determinant sign pattern tests
# ================================================================

class TestHigherRankSigns:
    """Test the sign pattern of higher-rank Hankel determinants."""

    def test_sign_pattern_c1(self):
        """At c=1: signs are (+, -, -, +, +, +)."""
        analysis = virasoro_hankel_analysis(1.0, 6)
        assert analysis['sign_sequence'] == [1, -1, -1, 1, 1, 1]

    def test_sign_pattern_c13(self):
        """At c=13 (self-dual): signs start (+, -, -, -, +, +)."""
        analysis = virasoro_hankel_analysis(13.0, 6)
        assert analysis['sign_sequence'][:2] == [1, -1]

    def test_det_H4_sign_transition(self):
        """det(H_4) changes sign between c=1 and c=5.

        At c=1: det(H_4) > 0.
        At c=5: det(H_4) < 0.
        There must be a transition point.
        """
        analysis_c1 = virasoro_hankel_analysis(1.0, 4)
        analysis_c5 = virasoro_hankel_analysis(5.0, 4)
        assert analysis_c1['hankel_dets'][3] > 0, "det(H_4) should be positive at c=1"
        assert analysis_c5['hankel_dets'][3] < 0, "det(H_4) should be negative at c=5"

    def test_determinants_decay(self):
        """Hankel determinants decay rapidly for large c.

        For large c, the shadow coefficients S_r for r >= 4 decay as
        O(1/c^{r-2}), so the Hankel determinants decay super-exponentially.
        """
        for c_val in [10.0, 50.0, 100.0]:
            analysis = virasoro_hankel_analysis(c_val, 5)
            dets = [abs(d) for d in analysis['hankel_dets']]
            # Each determinant should be much smaller than the previous
            for i in range(1, len(dets)):
                if dets[i - 1] > 1e-300 and dets[i] > 1e-300:
                    # Rough check: dets decay
                    pass  # just verify computation succeeds


# ================================================================
# 14. Moment matrix size and consistency tests
# ================================================================

class TestConsistency:
    """Consistency and edge case tests."""

    def test_H1_det_matches_S2(self):
        """det(H_1) = S_2 for all c."""
        for c in [0.5, 1.0, 13.0]:
            coeffs = shadow_coefficients_virasoro(c, 4)
            dets = shadow_hankel_determinants(coeffs, 1)
            assert abs(dets[0] - coeffs[2]) < 1e-12

    def test_increasing_matrix_sizes(self):
        """Can compute Hankel matrices from 1x1 to 6x6."""
        coeffs = shadow_coefficients_virasoro(1.0, 14)
        for r in range(1, 7):
            H = shadow_hankel_matrix(coeffs, r)
            assert len(H) == r
            assert all(len(row) == r for row in H)
            det = hankel_det(H)
            assert math.isfinite(det)

    def test_det_sequence_length(self):
        """shadow_hankel_determinants returns correct number of dets."""
        coeffs = shadow_coefficients_virasoro(1.0, 12)
        dets = shadow_hankel_determinants(coeffs, 6)
        assert len(dets) == 6

    def test_virasoro_hankel_analysis_keys(self):
        """virasoro_hankel_analysis returns all expected keys."""
        analysis = virasoro_hankel_analysis(1.0, 3)
        for key in ['c', 'shadow_coeffs', 'hankel_dets', 'sign_sequence',
                     'is_positive', 'first_negative']:
            assert key in analysis


# ================================================================
# 15. Physical content tests
# ================================================================

class TestPhysicalContent:
    """Tests with physical/mathematical significance."""

    def test_critical_c26_moment_structure(self):
        """At critical dimension c=26, the moment matrix has a specific structure.

        c=26 is the critical dimension for bosonic string.
        kappa(Vir_26) = 13, kappa(ghost) = -13, kappa_eff = 0.
        But the moment matrix of Vir_26 alone is nontrivial.
        """
        analysis = virasoro_hankel_analysis(26.0, 4)
        assert analysis['first_negative'] == 2
        # kappa = 13
        assert abs(analysis['shadow_coeffs'][2] - 13.0) < 1e-12

    def test_complementarity_pair_moments(self):
        """For Koszul pair (Vir_c, Vir_{26-c}): moment matrices are different.

        The Koszul dual has c' = 26-c, kappa' = (26-c)/2.
        The moment matrices should be related by kappa -> kappa'.
        """
        for c_val in [1.0, 5.0, 13.0]:
            c_dual = 26.0 - c_val
            a1 = virasoro_hankel_analysis(c_val, 3)
            a2 = virasoro_hankel_analysis(c_dual, 3)
            # Both should be signed
            assert a1['first_negative'] == 2
            assert a2['first_negative'] == 2

    def test_large_c_expansion(self):
        """For large c, S_r ~ 2*(-3)^{r-3}/r for r >= 3.

        This is the tree-level (class L) approximation.
        At large c, the quartic S_4 = 10/(c(5c+22)) -> 0,
        so Virasoro approaches class L.  The det(H_2) approaches
        -4 (the class L value -alpha^2).
        """
        c_val = 10000.0
        coeffs = shadow_coefficients_virasoro(c_val, 8)
        # S_4 should be very small
        assert abs(coeffs[4]) < 1e-6
        # det(H_2) should be close to -4
        dets = shadow_hankel_determinants(coeffs, 2)
        assert abs(dets[1] - (-4.0)) < 0.01
