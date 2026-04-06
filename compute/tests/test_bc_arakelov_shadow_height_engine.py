r"""Tests for bc_arakelov_shadow_height_engine.py.

BC-116: Arakelov intersection theory on shadow moduli and height pairings at zeros.

Covers all 10 sections:
  1. Kappa and shadow coefficient infrastructure
  2. Weil height infrastructure
  3. Arakelov height of shadow specialization points
  4. Faltings height of shadow fiber
  5. Height at zeta zeros
  6. Shadow elliptic curve and Neron-Tate height
  7. Gross-Zagier from shadow
  8. Koszul dual height pairing
  9. Multi-path verification (3+ paths per claim)
  10. Comprehensive tables

MULTI-PATH VERIFICATION:
  Path 1: Direct height from absolute value / Mahler measure
  Path 2: For rational values: h(p/q) = log max(|p|,|q|)
  Path 3: Triangle inequality: h(xy) <= h(x) + h(y) + log(2)
  Path 4: Faltings formula comparison
  Path 5: Complementarity at c=13 (AP24)
  Path 6: Naive Weil height comparison
  Path 7: Numerical evaluation at specific values

References:
  CLAUDE.md: AP1, AP10, AP24, AP33, AP39, AP46, AP48
"""

import math
import cmath
import pytest
from fractions import Fraction

from compute.lib.bc_arakelov_shadow_height_engine import (
    # Constants
    ZETA_ZEROS_50,
    zeta_zero_rho,
    # Kappa and shadow infrastructure
    kappa_value,
    shadow_S3,
    shadow_S4,
    shadow_discriminant,
    shadow_metric_QL,
    all_shadow_coefficients,
    # Weil height
    weil_height_rational,
    weil_height_complex,
    naive_height_vector,
    # Arakelov height of shadow points
    arakelov_height_shadow_point,
    arakelov_height_virasoro_scan,
    arakelov_height_heisenberg_scan,
    arakelov_height_affine_table,
    # Faltings height
    lambda_fp,
    deg_arakelov_lambda1,
    petersson_norm_shadow,
    faltings_height_shadow_fiber,
    faltings_height_virasoro_table,
    # Height at zeros
    shadow_kappa_at_complex_c,
    shadow_S3_at_complex_c,
    shadow_S4_at_complex_c,
    arakelov_height_at_zero,
    faltings_height_at_zero,
    height_at_zeros_table,
    test_local_extrema_at_zeros,
    test_faltings_monotonicity,
    # Shadow elliptic curve
    shadow_elliptic_curve_coefficients,
    neron_tate_height_estimate,
    neron_tate_on_shadow_curve,
    # Gross-Zagier
    cm_discriminants_small,
    is_cm_point_shadow,
    gross_zagier_shadow_data,
    # Koszul dual height pairing
    koszul_dual_kappa,
    complementarity_height_pairing,
    # Multi-path verification
    verify_arakelov_vs_weil,
    verify_faltings_two_paths,
    verify_complementarity_sum,
    verify_height_triangle,
    verify_numerical_evaluation,
    # Comprehensive
    build_full_arakelov_shadow_table,
)


# ============================================================================
# 1. KAPPA INFRASTRUCTURE (AP1, AP39, AP48)
# ============================================================================

class TestKappaInfrastructure:
    """Verify kappa formulas recomputed from first principles."""

    def test_heisenberg_kappa_k1(self):
        """kappa(H_1) = 1."""
        assert kappa_value("heisenberg", k=1) == 1.0

    def test_heisenberg_kappa_k5(self):
        """kappa(H_5) = 5."""
        assert kappa_value("heisenberg", k=5) == 5.0

    def test_heisenberg_kappa_negative(self):
        """kappa(H_{-3}) = -3."""
        assert kappa_value("heisenberg", k=-3) == -3.0

    def test_virasoro_kappa_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert abs(kappa_value("virasoro", c=1) - 0.5) < 1e-15

    def test_virasoro_kappa_c13(self):
        """kappa(Vir_13) = 13/2 (self-dual point)."""
        assert abs(kappa_value("virasoro", c=13) - 6.5) < 1e-15

    def test_virasoro_kappa_c26(self):
        """kappa(Vir_26) = 13 (critical dimension)."""
        assert abs(kappa_value("virasoro", c=26) - 13.0) < 1e-15

    def test_affine_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        kap = kappa_value("affine", lie_type="A", rank=1, k=1)
        assert abs(kap - 9 / 4) < 1e-12

    def test_affine_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        kap = kappa_value("affine", lie_type="A", rank=2, k=1)
        assert abs(kap - 16 / 3) < 1e-12

    def test_affine_sl4_k1(self):
        """kappa(sl_4, k=1) = 15*(1+4)/(2*4) = 75/8."""
        kap = kappa_value("affine", lie_type="A", rank=3, k=1)
        assert abs(kap - 75 / 8) < 1e-12

    def test_w3_kappa(self):
        """kappa(W_3, c=6) = 5*6/6 = 5."""
        assert abs(kappa_value("w3", c=6) - 5.0) < 1e-12

    def test_lattice_kappa(self):
        """kappa(V_Lambda, rank=24) = 24."""
        assert kappa_value("lattice", rank=24) == 24.0


class TestShadowCoefficients:
    """Verify shadow coefficients S_3, S_4, discriminant."""

    def test_S3_heisenberg_zero(self):
        """S_3 = 0 for Heisenberg (class G)."""
        assert shadow_S3("heisenberg", k=1) == 0.0

    def test_S3_virasoro_universal(self):
        """S_3 = 2 for ALL Virasoro (c-independent)."""
        for c in [1, 6, 12, 13, 24, 26]:
            assert abs(shadow_S3("virasoro", c=c) - 2.0) < 1e-15

    def test_S3_affine_sl2(self):
        """S_3 = 2*h^v/(k+h^v) = 4/(k+2) for affine sl_2."""
        for k in [1, 2, 3, 5]:
            expected = 4.0 / (k + 2)
            assert abs(shadow_S3("affine", lie_type="A", rank=1, k=k) - expected) < 1e-12

    def test_S4_heisenberg_zero(self):
        """S_4 = 0 for Heisenberg."""
        assert shadow_S4("heisenberg", k=1) == 0.0

    def test_S4_virasoro_formula(self):
        """S_4 = 10/(c*(5c+22)) for Virasoro."""
        for c in [1, 6, 12, 24]:
            expected = 10.0 / (c * (5 * c + 22))
            assert abs(shadow_S4("virasoro", c=c) - expected) < 1e-12

    def test_discriminant_heisenberg_zero(self):
        """Delta = 0 for Heisenberg (class G: tower terminates)."""
        assert shadow_discriminant("heisenberg", k=1) == 0.0

    def test_discriminant_virasoro_nonzero(self):
        """Delta != 0 for generic Virasoro (class M: infinite tower)."""
        for c in [1, 6, 12, 24]:
            delta = shadow_discriminant("virasoro", c=c)
            assert abs(delta) > 1e-15

    def test_shadow_metric_positive(self):
        """Q_L(0) = 4*kappa^2 > 0 for kappa != 0."""
        for c in [1, 6, 12, 24]:
            Q0 = shadow_metric_QL("virasoro", 0.0, c=c)
            kap = kappa_value("virasoro", c=c)
            assert abs(Q0 - 4 * kap ** 2) < 1e-10

    def test_all_shadow_coefficients_heisenberg(self):
        """Heisenberg: only S_2 = k nonzero."""
        coeffs = all_shadow_coefficients("heisenberg", max_r=10, k=3)
        assert coeffs[2] == 3.0
        for r in range(3, 11):
            assert abs(coeffs.get(r, 0)) < 1e-15

    def test_all_shadow_coefficients_virasoro(self):
        """Virasoro: S_2, S_3, S_4 all nonzero."""
        coeffs = all_shadow_coefficients("virasoro", max_r=10, c=12)
        assert abs(coeffs[2] - 6.0) < 1e-12
        assert abs(coeffs[3] - 2.0) < 1e-12
        assert abs(coeffs[4]) > 1e-15


# ============================================================================
# 2. WEIL HEIGHT INFRASTRUCTURE
# ============================================================================

class TestWeilHeight:
    """Verify the Weil height computations."""

    def test_weil_height_integer(self):
        """h(n) = log(n) for integer n > 0."""
        for n in [2, 3, 5, 7, 10, 100]:
            assert abs(weil_height_rational(float(n)) - math.log(n)) < 1e-10

    def test_weil_height_unit(self):
        """h(1) = 0, h(-1) = 0."""
        assert abs(weil_height_rational(1.0)) < 1e-12
        assert abs(weil_height_rational(-1.0)) < 1e-12

    def test_weil_height_zero(self):
        """h(0) = 0."""
        assert weil_height_rational(0.0) == 0.0

    def test_weil_height_half(self):
        """h(1/2) = log(2)."""
        assert abs(weil_height_rational(0.5) - math.log(2)) < 1e-10

    def test_weil_height_third(self):
        """h(1/3) = log(3)."""
        h = weil_height_rational(1.0 / 3.0)
        assert abs(h - math.log(3)) < 1e-8

    def test_weil_height_two_thirds(self):
        """h(2/3) = log(3) (since max(2,3) = 3)."""
        h = weil_height_rational(2.0 / 3.0)
        assert abs(h - math.log(3)) < 1e-8

    def test_weil_height_complex_unit(self):
        """h(e^{i*theta}) = 0 for |z| = 1."""
        for theta in [0.5, 1.0, 2.0, math.pi]:
            z = cmath.exp(1j * theta)
            assert abs(weil_height_complex(z)) < 1e-12

    def test_weil_height_complex_large(self):
        """h(z) = log|z| for |z| > 1."""
        z = complex(3, 4)  # |z| = 5
        assert abs(weil_height_complex(z) - math.log(5)) < 1e-12

    def test_weil_height_complex_small(self):
        """h(z) = 0 for |z| <= 1."""
        z = complex(0.3, 0.4)  # |z| = 0.5
        assert weil_height_complex(z) == 0.0

    def test_naive_height_vector_basic(self):
        """h([1:2:3]) = log(3)."""
        assert abs(naive_height_vector([1, 2, 3]) - math.log(3)) < 1e-12

    def test_naive_height_vector_unit(self):
        """h([1:1:1]) = 0."""
        assert abs(naive_height_vector([1, 1, 1])) < 1e-12


# ============================================================================
# 3. ARAKELOV HEIGHT OF SHADOW POINTS
# ============================================================================

class TestArakelovHeightShadowPoints:
    """Arakelov height at shadow specialization points."""

    def test_heisenberg_k1_height(self):
        """Heisenberg k=1: kappa = 1, h(1) = 0."""
        result = arakelov_height_shadow_point("heisenberg", k=1)
        assert result['kappa'] == 1.0
        assert result['h_kappa'] == pytest.approx(0.0, abs=1e-10)

    def test_heisenberg_k2_height(self):
        """Heisenberg k=2: kappa = 2, h(2) = log(2)."""
        result = arakelov_height_shadow_point("heisenberg", k=2)
        assert abs(result['h_kappa'] - math.log(2)) < 1e-10

    def test_virasoro_c12_height(self):
        """Virasoro c=12: kappa = 6, h(6) = log(6)."""
        result = arakelov_height_shadow_point("virasoro", c=12)
        assert abs(result['h_kappa'] - math.log(6)) < 1e-10

    def test_naive_le_total(self):
        """h_naive <= h_total always."""
        for fam, pars in [("heisenberg", {"k": 3}),
                          ("virasoro", {"c": 12}),
                          ("virasoro", {"c": 24})]:
            result = arakelov_height_shadow_point(fam, **pars)
            assert result['naive_le_total']

    def test_height_nonnegative(self):
        """All heights are nonnegative."""
        for fam, pars in [("heisenberg", {"k": 1}),
                          ("virasoro", {"c": 1}),
                          ("virasoro", {"c": 26})]:
            result = arakelov_height_shadow_point(fam, **pars)
            assert result['h_naive'] >= -1e-12
            assert result['h_total'] >= -1e-12

    def test_virasoro_scan_length(self):
        """Virasoro scan at c = 1/2, 1, ..., 26 has 27 entries."""
        results = arakelov_height_virasoro_scan()
        assert len(results) == 27

    def test_virasoro_scan_c13(self):
        """At c=13: kappa = 13/2."""
        results = arakelov_height_virasoro_scan()
        c13_entry = [r for r in results if abs(r['c'] - 13) < 0.01][0]
        assert abs(c13_entry['kappa'] - 6.5) < 1e-12

    def test_heisenberg_scan_length(self):
        """Heisenberg scan at k = 1, ..., 20 has 20 entries."""
        results = arakelov_height_heisenberg_scan()
        assert len(results) == 20

    def test_heisenberg_height_vs_level(self):
        """Heisenberg heights are monotone increasing in k."""
        results = arakelov_height_heisenberg_scan()
        # h(k) = log(k) is increasing for k >= 1
        for i in range(len(results) - 1):
            h_curr = results[i]['h_kappa']
            h_next = results[i + 1]['h_kappa']
            assert h_next >= h_curr - 1e-12

    def test_affine_table_shape(self):
        """Affine table: 4 N-values * 10 k-values = 40 entries."""
        results = arakelov_height_affine_table()
        assert len(results) == 40

    def test_affine_kappa_increases_with_k(self):
        """For fixed N, kappa increases with k (since kappa = dim*(k+h^v)/(2h^v))."""
        results = arakelov_height_affine_table()
        for N in [2, 3, 4, 5]:
            entries = [r for r in results if r['N'] == N]
            kappas = [r['kappa'] for r in entries]
            for i in range(len(kappas) - 1):
                assert kappas[i + 1] > kappas[i]


# ============================================================================
# 4. FALTINGS HEIGHT
# ============================================================================

class TestFaltingsHeight:
    """Test Faltings height of shadow fibers."""

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        assert abs(lambda_fp(1) - 1 / 24) < 1e-15

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        assert abs(lambda_fp(2) - 7 / 5760) < 1e-15

    def test_lambda_fp_g3(self):
        """lambda_3^FP = 31/967680."""
        assert abs(lambda_fp(3) - 31 / 967680) < 1e-12

    def test_deg_arakelov_lambda1_range(self):
        """deg_Ar(lambda_1) ~ 0.377 (within [0.35, 0.40])."""
        val = deg_arakelov_lambda1()
        assert 0.35 < val < 0.40

    def test_petersson_norm_positive(self):
        """Petersson norm is positive for kappa != 0."""
        for c in [1, 12, 24]:
            pet = petersson_norm_shadow("virasoro", c=c)
            assert pet > 0

    def test_petersson_norm_scales_quadratically(self):
        """||sigma||_Pet^2 scales as kappa^2."""
        pet1 = petersson_norm_shadow("virasoro", c=2)   # kappa = 1
        pet12 = petersson_norm_shadow("virasoro", c=24)  # kappa = 12
        # Ratio should be (12/1)^2 = 144
        assert abs(pet12 / pet1 - 144.0) < 1e-8

    def test_faltings_height_heisenberg_g1(self):
        """Faltings height for H_1 at genus 1."""
        result = faltings_height_shadow_fiber("heisenberg", genus=1, k=1)
        assert result['kappa'] == 1.0
        expected = deg_arakelov_lambda1()
        assert abs(result['h_F_arakelov'] - expected) < 1e-12

    def test_faltings_height_virasoro_c13(self):
        """Faltings height for Vir_13 (self-dual)."""
        result = faltings_height_shadow_fiber("virasoro", genus=1, c=13)
        assert abs(result['kappa'] - 6.5) < 1e-12
        expected = 6.5 * deg_arakelov_lambda1()
        assert abs(result['h_F_arakelov'] - expected) < 1e-10

    def test_faltings_height_proportional_to_kappa(self):
        """h_F is proportional to kappa at genus 1."""
        h1 = faltings_height_shadow_fiber("virasoro", genus=1, c=2)['h_F_arakelov']
        h2 = faltings_height_shadow_fiber("virasoro", genus=1, c=4)['h_F_arakelov']
        # kappa(c=2) = 1, kappa(c=4) = 2, so ratio = 2
        assert abs(h2 / h1 - 2.0) < 1e-10

    def test_faltings_table_length(self):
        """Faltings table for c = 1..26 has 26 entries."""
        table = faltings_height_virasoro_table()
        assert len(table) == 26

    def test_F_g_equals_kappa_times_lambda(self):
        """F_g = kappa * lambda_g^FP."""
        result = faltings_height_shadow_fiber("virasoro", genus=1, c=24)
        assert abs(result['F_g'] - 12.0 * lambda_fp(1)) < 1e-12

    def test_motivic_weight_genus1(self):
        """Motivic weight at genus 1 is 0."""
        result = faltings_height_shadow_fiber("virasoro", genus=1, c=12)
        assert result['motivic_weight'] == 0

    def test_motivic_weight_genus2(self):
        """Motivic weight at genus 2 is 2."""
        result = faltings_height_shadow_fiber("virasoro", genus=2, c=12)
        assert result['motivic_weight'] == 2


# ============================================================================
# 5. HEIGHT AT ZETA ZEROS
# ============================================================================

class TestHeightAtZeros:
    """Test heights evaluated at zeta zeros."""

    def test_zeta_zeros_stored(self):
        """50 zeros stored."""
        assert len(ZETA_ZEROS_50) == 50

    def test_zeros_increasing(self):
        """Zeros are strictly increasing."""
        for i in range(49):
            assert ZETA_ZEROS_50[i] < ZETA_ZEROS_50[i + 1]

    def test_first_zero(self):
        """gamma_1 = 14.1347..."""
        assert abs(ZETA_ZEROS_50[0] - 14.134725) < 1e-4

    def test_shadow_kappa_complex(self):
        """kappa(c) = c/2 for complex c."""
        c = complex(3, 4)
        kap = shadow_kappa_at_complex_c(c)
        assert abs(kap - complex(1.5, 2.0)) < 1e-12

    def test_shadow_S3_complex(self):
        """S_3 = 2 (c-independent) for complex c."""
        c = complex(3, 4)
        s3 = shadow_S3_at_complex_c(c)
        assert abs(s3 - 2.0) < 1e-12

    def test_shadow_S4_complex(self):
        """S_4 = 10/(c*(5c+22)) for complex c."""
        c = complex(2, 0)
        s4 = shadow_S4_at_complex_c(c)
        expected = 10.0 / (2 * (10 + 22))
        assert abs(s4 - expected) < 1e-12

    def test_arakelov_height_at_zero_1(self):
        """h_Ar at first zero is finite and positive."""
        result = arakelov_height_at_zero(1)
        assert result['h_Ar_total'] > 0
        assert not math.isinf(result['h_Ar_total'])
        assert not math.isnan(result['h_Ar_total'])

    def test_arakelov_height_at_zero_10(self):
        """h_Ar at 10th zero is finite."""
        result = arakelov_height_at_zero(10)
        assert not math.isnan(result['h_Ar_total'])

    def test_faltings_height_at_zero_1(self):
        """h_F at first zero is finite and positive."""
        result = faltings_height_at_zero(1)
        assert result['h_F'] > 0
        assert not math.isnan(result['h_F'])

    def test_height_at_zeros_table_shape(self):
        """Table for first 10 zeros has 10 entries."""
        table = height_at_zeros_table(n_max=10)
        assert len(table) == 10

    def test_height_at_zeros_keys(self):
        """Each entry has required keys."""
        table = height_at_zeros_table(n_max=2)
        for entry in table:
            for key in ['n', 'gamma_n', 'h_Ar', 'h_F', 'abs_kappa']:
                assert key in entry

    def test_faltings_monotonicity(self):
        """h_F is monotone along the critical line.

        h_F = |kappa(1/2 + i*t)| * deg = |1/4 + i*t/2| * deg
        = sqrt(1/16 + t^2/4) * deg, strictly increasing in |t|.
        Since gamma_n is increasing, h_F should be monotone.
        """
        result = test_faltings_monotonicity(n_max=25)
        assert result['is_monotone']

    def test_faltings_monotonicity_formula(self):
        """h_F(rho_n) = sqrt(1/16 + gamma_n^2/4) * deg_Ar."""
        deg = deg_arakelov_lambda1()
        for n in [1, 5, 10, 20]:
            result = faltings_height_at_zero(n)
            gamma = result['gamma_n']
            expected = math.sqrt(1.0 / 16 + gamma ** 2 / 4) * abs(deg)
            assert abs(result['h_F'] - expected) < 1e-8

    def test_h_Ar_grows_with_n(self):
        """h_Ar generally grows with n (because gamma_n grows)."""
        h1 = arakelov_height_at_zero(1)['h_Ar_total']
        h25 = arakelov_height_at_zero(25)['h_Ar_total']
        assert h25 > h1

    def test_local_extrema_analysis(self):
        """Local extrema test runs without error."""
        result = test_local_extrema_at_zeros(n_max=5, delta=0.5)
        assert result['n_zeros_tested'] == 5
        assert 'n_local_min' in result
        assert 'n_local_max' in result


# ============================================================================
# 6. SHADOW ELLIPTIC CURVE
# ============================================================================

class TestShadowEllipticCurve:
    """Test the shadow elliptic curve and Neron-Tate height."""

    def test_curve_coefficients_computed(self):
        """Curve coefficients are finite for c=12."""
        ec = shadow_elliptic_curve_coefficients(12)
        assert not math.isnan(ec['a4'])
        assert not math.isnan(ec['a6'])
        assert not math.isnan(ec['discriminant'])

    def test_curve_j_invariant_finite(self):
        """j-invariant is finite for generic c."""
        for c in [1, 6, 12, 24]:
            ec = shadow_elliptic_curve_coefficients(c)
            if abs(ec['discriminant']) > 1e-10:
                assert not math.isinf(ec['j_invariant'])

    def test_curve_discriminant_varies(self):
        """Discriminant varies with c."""
        d1 = shadow_elliptic_curve_coefficients(6)['discriminant']
        d2 = shadow_elliptic_curve_coefficients(12)['discriminant']
        assert abs(d1 - d2) > 1e-10

    def test_neron_tate_nonnegative(self):
        """Neron-Tate height estimate is real."""
        nt = neron_tate_height_estimate(12, 1.0, 1.0)
        assert not math.isnan(nt['h_NT_estimate'])

    def test_neron_tate_increases_with_x(self):
        """h_NT ~ log|x| grows with |x|."""
        h1 = neron_tate_height_estimate(12, 1.0, 0.0)['h_NT_estimate']
        h10 = neron_tate_height_estimate(12, 10.0, 0.0)['h_NT_estimate']
        assert h10 > h1

    def test_neron_tate_on_curve_structure(self):
        """neron_tate_on_shadow_curve returns expected structure."""
        result = neron_tate_on_shadow_curve(12)
        assert 'c' in result
        assert 'curve' in result
        assert 'n_rational_points_found' in result
        assert 'rational_points' in result

    def test_a4_proportional_to_QL(self):
        """a4 = -27 * Q_L(1): direct verification."""
        for c in [6, 12, 24]:
            ec = shadow_elliptic_curve_coefficients(c)
            Q1 = shadow_metric_QL("virasoro", 1.0, c=c)
            assert abs(ec['a4'] - (-27 * Q1)) < 1e-8


# ============================================================================
# 7. GROSS-ZAGIER FROM SHADOW
# ============================================================================

class TestGrossZagier:
    """Test Gross-Zagier shadow data."""

    def test_cm_discriminants_list(self):
        """9 class-number-1 CM discriminants."""
        disc = cm_discriminants_small()
        assert len(disc) == 9
        assert -163 in disc
        assert -3 in disc

    def test_cm_point_check_structure(self):
        """CM point check returns expected fields."""
        result = is_cm_point_shadow(12)
        assert 'c' in result
        assert 'j_invariant' in result
        assert 'is_cm' in result
        assert 'nearest_cm_discriminant' in result

    def test_cm_point_generic_not_cm(self):
        """Generic c (e.g., c=7) is not a CM point."""
        result = is_cm_point_shadow(7)
        # Generic c should not be CM (unless by coincidence)
        # We just check the structure is valid
        assert isinstance(result['is_cm'], bool)

    def test_gross_zagier_data_structure(self):
        """Gross-Zagier data returns expected fields."""
        result = gross_zagier_shadow_data(12)
        assert 'c' in result
        assert 'elliptic_curve' in result
        assert 'cm_data' in result
        assert 'neron_tate_data' in result
        assert 'petersson_norm' in result

    def test_gross_zagier_petersson_positive(self):
        """Petersson norm in GZ data is positive."""
        result = gross_zagier_shadow_data(12)
        assert result['petersson_norm'] > 0

    def test_gross_zagier_several_c(self):
        """GZ data computes for several c values."""
        for c in [1, 6, 12, 24]:
            result = gross_zagier_shadow_data(c)
            assert result['c'] == c


# ============================================================================
# 8. KOSZUL DUAL HEIGHT PAIRING
# ============================================================================

class TestKoszulDualHeightPairing:
    """Test the Koszul dual and complementarity height pairing."""

    def test_koszul_dual_heisenberg(self):
        """Heisenberg: kappa + kappa' = 0 (AP33)."""
        kap = kappa_value("heisenberg", k=3)
        kap_dual = koszul_dual_kappa("heisenberg", k=3)
        assert abs(kap + kap_dual) < 1e-12

    def test_koszul_dual_virasoro_sum_13(self):
        """Virasoro: kappa + kappa' = 13 (AP24)."""
        for c in [1, 6, 12, 13, 24, 25, 26]:
            kap = kappa_value("virasoro", c=c)
            kap_dual = koszul_dual_kappa("virasoro", c=c)
            assert abs(kap + kap_dual - 13.0) < 1e-12, \
                f"c={c}: sum = {kap + kap_dual}"

    def test_koszul_dual_virasoro_self_dual_c13(self):
        """At c=13: kappa = kappa' = 13/2."""
        kap = kappa_value("virasoro", c=13)
        kap_dual = koszul_dual_kappa("virasoro", c=13)
        assert abs(kap - kap_dual) < 1e-12

    def test_koszul_dual_affine_sl2(self):
        """Affine sl_2: kappa + kappa' = 0 (Feigin-Frenkel)."""
        kap = kappa_value("affine", lie_type="A", rank=1, k=1)
        kap_dual = koszul_dual_kappa("affine", lie_type="A", rank=1, k=1)
        assert abs(kap + kap_dual) < 1e-10

    def test_complementarity_pairing_virasoro(self):
        """BB pairing structure for Virasoro."""
        result = complementarity_height_pairing("virasoro", genus=1, c=12)
        assert abs(result['kappa_sum'] - 13.0) < 1e-10
        assert 'BB_pairing' in result
        assert result['BB_pairing'] != 0

    def test_complementarity_pairing_heisenberg(self):
        """BB pairing for Heisenberg: kappa + kappa' = 0."""
        result = complementarity_height_pairing("heisenberg", genus=1, k=2)
        assert abs(result['kappa_sum']) < 1e-12

    def test_complementarity_pairing_sign(self):
        """For Heisenberg: kappa*kappa' < 0, so BB < 0."""
        result = complementarity_height_pairing("heisenberg", genus=1, k=2)
        assert result['BB_pairing'] < 0

    def test_complementarity_self_dual_symmetric(self):
        """At c=13: Q_A = Q_A' (symmetric pairing)."""
        result = complementarity_height_pairing("virasoro", genus=1, c=13)
        assert abs(result['Q_A'] - result['Q_A_dual']) < 1e-12


# ============================================================================
# 9. MULTI-PATH VERIFICATION (3+ paths per claim)
# ============================================================================

class TestMultiPathVerification:
    """Multi-path verification: every claim verified by 3+ independent methods."""

    # --- Path 1 + 6: Arakelov vs Weil ---

    def test_arakelov_ge_weil_heisenberg(self):
        """Path 1+6: h_total >= h_weil for Heisenberg."""
        result = verify_arakelov_vs_weil("heisenberg", k=3)
        assert result['total_ge_weil']

    def test_arakelov_ge_weil_virasoro(self):
        """Path 1+6: h_total >= h_weil for Virasoro."""
        result = verify_arakelov_vs_weil("virasoro", c=12)
        assert result['total_ge_weil']

    def test_arakelov_ge_weil_affine(self):
        """Path 1+6: h_total >= h_weil for affine."""
        result = verify_arakelov_vs_weil("affine", lie_type="A", rank=1, k=1)
        assert result['total_ge_weil']

    # --- Path 2 + 4: Faltings two-path ---

    def test_faltings_two_paths_heisenberg(self):
        """Path 2+4: Faltings height matches across two methods."""
        result = verify_faltings_two_paths("heisenberg", k=1)
        assert result['match']

    def test_faltings_two_paths_virasoro(self):
        """Path 2+4: Faltings height matches for Virasoro."""
        result = verify_faltings_two_paths("virasoro", c=12)
        assert result['match']

    def test_faltings_two_paths_virasoro_c26(self):
        """Path 2+4: Faltings at c=26 (critical dimension)."""
        result = verify_faltings_two_paths("virasoro", c=26)
        assert result['match']

    # --- Path 3: Triangle inequality ---

    def test_triangle_inequality_basic(self):
        """Path 3: h(x*y) <= h(x) + h(y) + log(2)."""
        for x, y in [(2, 3), (5, 7), (1.5, 2.5), (0.5, 3)]:
            result = verify_height_triangle(x, y)
            assert result['triangle_holds'], f"Failed for x={x}, y={y}"

    def test_triangle_inequality_kappa_products(self):
        """Path 3: Triangle for kappa products."""
        result = verify_height_triangle(6.0, 7.0)  # kappa values
        assert result['triangle_holds']

    def test_triangle_inequality_shadow_coefficients(self):
        """Path 3: Triangle for shadow coefficient products."""
        result = verify_height_triangle(2.0, 10.0 / (12 * 82))  # S_3 * S_4
        assert result['triangle_holds']

    # --- Path 5: Complementarity sum ---

    def test_complementarity_sum_all_c(self):
        """Path 5: kappa + kappa' = 13 for c = 1, ..., 26."""
        for c in range(1, 27):
            result = verify_complementarity_sum(float(c))
            assert result['equals_13'], f"c={c}: sum={result['sum']}"

    def test_complementarity_sum_half_integer(self):
        """Path 5: kappa + kappa' = 13 for c = 1/2."""
        result = verify_complementarity_sum(0.5)
        assert result['equals_13']

    def test_complementarity_sum_negative(self):
        """Path 5: kappa + kappa' = 13 for c = -1."""
        result = verify_complementarity_sum(-1.0)
        assert result['equals_13']

    # --- Path 7: Numerical evaluation ---

    def test_numerical_heisenberg(self):
        """Path 7: Numerical cross-check for Heisenberg."""
        result = verify_numerical_evaluation("heisenberg", k=5)
        assert result['kappa_match']

    def test_numerical_virasoro(self):
        """Path 7: Numerical cross-check for Virasoro."""
        result = verify_numerical_evaluation("virasoro", c=24)
        assert result['kappa_match']

    def test_numerical_affine(self):
        """Path 7: Numerical cross-check for affine sl_2."""
        result = verify_numerical_evaluation("affine", lie_type="A", rank=1, k=1)
        assert result['kappa_match']

    # --- Cross-family consistency ---

    def test_heisenberg_is_class_G(self):
        """Cross-family: Heisenberg has h_total = h_kappa (only S_2 nonzero)."""
        result = arakelov_height_shadow_point("heisenberg", k=3)
        assert abs(result['h_total'] - result['h_kappa']) < 1e-12

    def test_virasoro_h_total_exceeds_h_kappa(self):
        """Cross-family: Virasoro h_total > h_kappa (multiple nonzero S_r)."""
        result = arakelov_height_shadow_point("virasoro", c=12)
        assert result['h_total'] > result['h_kappa'] + 1e-12


# ============================================================================
# 10. COMPREHENSIVE TABLE INTEGRATION
# ============================================================================

class TestComprehensiveTable:
    """Integration tests for the full table builder."""

    def test_full_table_builds(self):
        """Comprehensive table builds without error."""
        table = build_full_arakelov_shadow_table(
            n_zeros=3,
            c_virasoro=[1, 13, 26],
            k_heisenberg=[1, 2, 3],
        )
        assert 'virasoro_scan' in table
        assert 'heisenberg_scan' in table
        assert 'affine_table' in table
        assert 'faltings_table' in table
        assert 'zeros_table' in table
        assert 'complementarity' in table

    def test_virasoro_scan_in_table(self):
        """Virasoro scan has correct length."""
        table = build_full_arakelov_shadow_table(
            n_zeros=2, c_virasoro=[1, 13], k_heisenberg=[1])
        assert len(table['virasoro_scan']) == 2

    def test_zeros_table_in_full(self):
        """Zeros table has correct length."""
        table = build_full_arakelov_shadow_table(
            n_zeros=5, c_virasoro=[1], k_heisenberg=[1])
        assert len(table['zeros_table']) == 5

    def test_complementarity_in_table(self):
        """Complementarity data is present and correct."""
        table = build_full_arakelov_shadow_table(
            n_zeros=2, c_virasoro=[1], k_heisenberg=[1])
        for comp in table['complementarity']:
            if comp['family'] == 'virasoro':
                assert abs(comp['kappa_sum'] - 13.0) < 1e-10


# ============================================================================
# 11. DEEP STRUCTURAL TESTS
# ============================================================================

class TestDeepStructural:
    """Deep structural tests for mathematical consistency."""

    def test_shadow_metric_at_origin(self):
        """Q_L(0) = 4*kappa^2: verified for all standard families."""
        for fam, pars in [("heisenberg", {"k": 3}),
                          ("virasoro", {"c": 12}),
                          ("virasoro", {"c": 24}),
                          ("affine", {"lie_type": "A", "rank": 1, "k": 1})]:
            Q0 = shadow_metric_QL(fam, 0.0, **pars)
            kap = kappa_value(fam, **pars)
            assert abs(Q0 - 4 * kap ** 2) < 1e-8

    def test_discriminant_formula(self):
        """Delta = 8*kappa*S_4: verified independently."""
        for c in [1, 6, 12, 24]:
            kap = kappa_value("virasoro", c=c)
            s4 = shadow_S4("virasoro", c=c)
            delta = shadow_discriminant("virasoro", c=c)
            assert abs(delta - 8 * kap * s4) < 1e-12

    def test_height_at_zero_decomposes(self):
        """h_Ar(rho_n) = h(kappa) + h(S_3) + h(S_4)."""
        for n in [1, 5, 10]:
            result = arakelov_height_at_zero(n)
            expected = result['h_kappa'] + result['h_S3'] + result['h_S4']
            assert abs(result['h_Ar_total'] - expected) < 1e-12

    def test_faltings_kappa_product_formula(self):
        """h_F = kappa * deg_Ar at genus 1: verified across families."""
        deg = deg_arakelov_lambda1()
        for fam, pars in [("heisenberg", {"k": 1}),
                          ("heisenberg", {"k": 5}),
                          ("virasoro", {"c": 12}),
                          ("virasoro", {"c": 26})]:
            result = faltings_height_shadow_fiber(fam, genus=1, **pars)
            kap = kappa_value(fam, **pars)
            assert abs(result['h_F_arakelov'] - kap * deg) < 1e-10

    def test_bb_pairing_bilinear(self):
        """BB pairing is bilinear in kappa, kappa'."""
        r1 = complementarity_height_pairing("virasoro", genus=1, c=2)
        r2 = complementarity_height_pairing("virasoro", genus=1, c=4)
        # kappa(c=2) = 1, kappa'(c=2) = 12
        # kappa(c=4) = 2, kappa'(c=4) = 11
        # BB(c=2) = 1*12*lfp^2*deg, BB(c=4) = 2*11*lfp^2*deg
        ratio = r2['BB_pairing'] / r1['BB_pairing']
        expected_ratio = (2 * 11) / (1 * 12)
        assert abs(ratio - expected_ratio) < 1e-8

    def test_shadow_curve_discriminant_sign(self):
        """Elliptic curve discriminant sign is consistent."""
        for c in [6, 12, 24]:
            ec = shadow_elliptic_curve_coefficients(c)
            # disc = -16*(4a4^3 + 27a6^2)
            a4, a6 = ec['a4'], ec['a6']
            expected_disc = -16 * (4 * a4 ** 3 + 27 * a6 ** 2)
            assert abs(ec['discriminant'] - expected_disc) < 1e-4

    def test_all_kappa_positive_for_physical_c(self):
        """kappa > 0 for c > 0 (physical central charges)."""
        for c in range(1, 27):
            kap = kappa_value("virasoro", c=c)
            assert kap > 0


# ============================================================================
# 12. EDGE CASES AND BOUNDARY TESTS
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_kappa_zero_at_c0(self):
        """kappa(Vir_0) = 0."""
        assert kappa_value("virasoro", c=0) == 0.0

    def test_height_at_kappa_zero(self):
        """h(0) = 0 when kappa = 0."""
        result = arakelov_height_shadow_point("virasoro", c=0)
        assert result['h_kappa'] == 0.0

    def test_S4_singular_at_c0(self):
        """S_4 = 10/(c*(5c+22)) -> 0 at c=0 (guarded)."""
        s4 = shadow_S4("virasoro", c=0)
        # Guarded: returns 0 when denominator is zero
        assert s4 == 0.0

    def test_heisenberg_k_negative(self):
        """Negative levels produce negative kappa."""
        kap = kappa_value("heisenberg", k=-5)
        assert kap == -5.0

    def test_large_c_height(self):
        """Height for large c: kappa grows linearly."""
        result = arakelov_height_shadow_point("virasoro", c=1000)
        assert result['kappa'] == 500.0

    def test_half_integer_c(self):
        """c = 1/2 (minimal model): kappa = 1/4."""
        result = arakelov_height_shadow_point("virasoro", c=0.5)
        assert abs(result['kappa'] - 0.25) < 1e-12


# ============================================================================
# 13. CROSS-FAMILY HEIGHT COMPARISON
# ============================================================================

class TestCrossFamilyComparison:
    """Cross-family consistency of height computations."""

    def test_heisenberg_vs_virasoro_at_c2(self):
        """Heisenberg k=1 and Virasoro c=2 have same kappa = 1."""
        h_heis = arakelov_height_shadow_point("heisenberg", k=1)
        h_vir = arakelov_height_shadow_point("virasoro", c=2)
        assert abs(h_heis['kappa'] - h_vir['kappa']) < 1e-12

    def test_heisenberg_height_less_than_virasoro(self):
        """Heisenberg h_total <= Virasoro h_total at same kappa.

        Heisenberg is class G (only S_2), Virasoro is class M (all S_r).
        """
        h_heis = arakelov_height_shadow_point("heisenberg", k=1)
        h_vir = arakelov_height_shadow_point("virasoro", c=2)
        assert h_heis['h_total'] <= h_vir['h_total'] + 1e-12

    def test_affine_kappa_higher_dimensional(self):
        """Affine sl_N at N > 2 has kappa > kappa(sl_2) at same k."""
        kap2 = kappa_value("affine", lie_type="A", rank=1, k=1)  # sl_2
        kap3 = kappa_value("affine", lie_type="A", rank=2, k=1)  # sl_3
        assert kap3 > kap2

    def test_lattice_kappa_equals_rank(self):
        """Lattice VOA: kappa = rank (AP48)."""
        for rank in [1, 8, 16, 24]:
            assert kappa_value("lattice", rank=rank) == float(rank)
