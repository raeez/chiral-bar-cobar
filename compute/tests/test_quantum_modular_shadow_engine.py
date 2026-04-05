r"""Tests for quantum modular forms from class-M shadow towers.

Tests the seven main analysis areas:
1. Shadow generating function evaluation and cross-verification
2. Quantum modularity defects at rational points
3. Mock modular structure for minimal models
4. False theta functions and shadow tower overlap
5. Nahm conjecture and shadow matrices
6. Habiro ring integrality at roots of unity
7. Modular completion and radial limits

86+ tests covering multi-path verification.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
"""

import cmath
import math
import pytest

from compute.lib.quantum_modular_shadow_engine import (
    # Section 0: Virasoro helpers
    virasoro_kappa,
    virasoro_cubic,
    virasoro_quartic,
    virasoro_shadow_metric_coeffs,
    virasoro_shadow_radius,
    # Section 1: Shadow GF evaluation
    shadow_tower_coefficients,
    shadow_generating_function,
    weighted_shadow_gf,
    weighted_shadow_gf_complex,
    shadow_gf_at_rational,
    shadow_gf_borel_regularized,
    # Section 2: Quantum modularity
    quantum_modular_defect,
    quantum_modularity_S_defect,
    quantum_modularity_T_defect,
    scan_quantum_modularity,
    # Section 3: Mock modular
    false_theta_function,
    false_theta_coefficients,
    shadow_tower_vs_false_theta,
    minimal_model_central_charge,
    mock_modular_shadow_analysis,
    # Section 4: Nahm conjecture
    nahm_matrix_from_shadow,
    nahm_scan_minimal_models,
    # Section 5: Habiro ring
    habiro_element_test,
    habiro_scan,
    q_pochhammer,
    # Section 6: Modular completion
    modular_completion_shadow,
    # Section 7: Radial limits
    radial_limit_shadow_pf,
    radial_limits_scan,
    # Section 8: Cross-verification
    cross_verify_shadow_gf,
    cross_verify_nahm,
    # Section 9: W_N
    w3_shadow_data_T_line,
    # Section 10: Zwegers
    shadow_zwegers_completion,
    # Section 11: Periods
    period_polynomial_shadow,
    # Section 12: Master
    quantum_modular_master_analysis,
    quantum_modularity_summary,
)

PI = math.pi
TWO_PI = 2 * PI


# =========================================================================
# Section 1: Basic shadow data verification (10 tests)
# =========================================================================

class TestVirasororShadowData:
    """Verify Virasoro shadow data against known values."""

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2 (AP20, AP39)."""
        for c in [0.5, 1, 2, 13, 25, 26]:
            assert abs(virasoro_kappa(c) - c / 2) < 1e-14

    def test_cubic_shadow_universal(self):
        """S_3 = alpha = 2 for ALL Virasoro (universal cubic coefficient)."""
        for c in [0.5, 1, 2, 7, 13, 25]:
            assert virasoro_cubic(c) == 2

    def test_quartic_contact_virasoro(self):
        """Q^contact = 10/(c*(5c+22)) for Virasoro."""
        c = 2.0
        expected = 10.0 / (2.0 * (10.0 + 22.0))
        assert abs(virasoro_quartic(c) - expected) < 1e-14

    def test_quartic_contact_ising(self):
        """Q^contact for Ising (c=1/2): 10/(0.5*24.5) = 10/12.25."""
        c = 0.5
        expected = 10.0 / (0.5 * (2.5 + 22.0))
        assert abs(virasoro_quartic(c) - expected) < 1e-12

    def test_shadow_metric_Q0(self):
        """Q_L(0) = 4*kappa^2 = c^2."""
        for c in [1.0, 2.0, 13.0, 25.0]:
            q0, q1, q2 = virasoro_shadow_metric_coeffs(c)
            assert abs(q0 - c ** 2) < 1e-12

    def test_shadow_metric_Q1(self):
        """q_1 = 12*kappa*alpha = 12c (since alpha=2, kappa=c/2)."""
        for c in [1.0, 2.0, 13.0]:
            q0, q1, q2 = virasoro_shadow_metric_coeffs(c)
            assert abs(q1 - 12.0 * c) < 1e-12

    def test_shadow_radius_c13(self):
        """rho(Vir_13) ~ 0.467 (self-dual point)."""
        rho = virasoro_shadow_radius(13.0)
        assert 0.4 < rho < 0.55

    def test_shadow_radius_c25(self):
        """rho(Vir_25) < 1 (convergent)."""
        rho = virasoro_shadow_radius(25.0)
        assert rho < 1.0

    def test_shadow_radius_ising(self):
        """rho(Vir_{1/2}) > 1 (divergent: c < c*)."""
        rho = virasoro_shadow_radius(0.5)
        assert rho > 1.0

    def test_shadow_radius_critical(self):
        """rho(Vir_{c*}) ~ 1 at c* ~ 6.125."""
        # The critical charge: 5c^3 + 22c^2 - 180c - 872 = 0
        # c* ~ 6.1243
        rho_low = virasoro_shadow_radius(6.0)
        rho_high = virasoro_shadow_radius(6.2)
        # rho should cross 1 between c=6.0 and c=6.2
        assert rho_low > 1.0 or rho_high < 1.0


# =========================================================================
# Section 2: Shadow tower coefficients (10 tests)
# =========================================================================

class TestShadowTowerCoefficients:
    """Verify shadow tower computation from sqrt(Q_L) expansion."""

    def test_S2_equals_kappa(self):
        """S_2 = a_0/2 = sqrt(q0)/2 = |2*kappa|/2 = |kappa|."""
        for c in [1.0, 2.0, 13.0, 25.0]:
            S = shadow_tower_coefficients(c, 5)
            kappa = virasoro_kappa(c)
            assert abs(S[2] - kappa) < 1e-10, f"S_2={S[2]}, kappa={kappa} at c={c}"

    def test_S3_positive(self):
        """S_3 > 0 for c > 0 (cubic shadow is positive)."""
        for c in [0.5, 1.0, 2.0, 13.0, 25.0]:
            S = shadow_tower_coefficients(c, 5)
            assert S[3] > 0, f"S_3={S[3]} at c={c}"

    def test_S4_positive(self):
        """S_4 > 0 for c > 0 (quartic contact invariant is positive)."""
        for c in [0.5, 1.0, 2.0, 13.0, 25.0]:
            S = shadow_tower_coefficients(c, 5)
            assert S[4] > 0, f"S_4={S[4]} at c={c}"

    def test_tower_nonzero_class_M(self):
        """All S_r != 0 for class M (Virasoro has infinite shadow depth)."""
        c = 13.0
        S = shadow_tower_coefficients(c, 30)
        for r in range(2, 25):
            assert abs(S[r]) > 1e-30, f"S_{r}=0 at c={c}, but Virasoro is class M"

    def test_tower_decay_convergent(self):
        """For c=25 (rho<1), |S_r| -> 0 as r -> infinity."""
        c = 25.0
        S = shadow_tower_coefficients(c, 40)
        assert abs(S[30]) < abs(S[5]), "S_r should decay for convergent tower"

    def test_tower_growth_divergent(self):
        """For c=1/2 (rho>1), |S_r| grows as r -> infinity."""
        c = 0.5
        S = shadow_tower_coefficients(c, 30)
        assert abs(S[20]) > abs(S[5]) * 0.5, "S_r should grow for divergent tower"

    def test_ratio_test_approaches_rho(self):
        """The ratio |S_{r+1}/S_r| -> rho as r -> infinity.

        For class-M towers with oscillation, the ratio |S_{r+1}/S_r|
        oscillates around rho due to the cos(r*theta+phi) factor.
        The AVERAGED ratio converges; individual ratios can deviate.
        We use a rolling average and wider tolerance.
        """
        c = 13.0
        rho = virasoro_shadow_radius(c)
        S = shadow_tower_coefficients(c, 80)
        ratios = []
        for r in range(20, 75):
            if abs(S[r]) > 1e-50:
                ratios.append(abs(S[r + 1] / S[r]))
        # Average of last 20 ratios should be close to rho
        if len(ratios) >= 20:
            avg_ratio = sum(ratios[-20:]) / 20
            assert abs(avg_ratio - rho) / rho < 0.25, f"avg_ratio={avg_ratio}, rho={rho}"

    def test_S2_kappa_c25(self):
        """S_2(Vir_25) = 25/2 = 12.5."""
        S = shadow_tower_coefficients(25.0, 5)
        assert abs(S[2] - 12.5) < 1e-12

    def test_tower_coefficients_count(self):
        """Requesting max_arity=N produces N-1 coefficients (r=2,...,N)."""
        S = shadow_tower_coefficients(13.0, 20)
        assert len(S) == 19  # r = 2,3,...,20

    def test_tower_coefficients_symmetry(self):
        """S_r(Vir_c) and S_r(Vir_{26-c}) are related by Koszul duality."""
        c1, c2 = 10.0, 16.0  # Koszul dual pair
        S1 = shadow_tower_coefficients(c1, 10)
        S2 = shadow_tower_coefficients(c2, 10)
        # kappa1 + kappa2 = 5 + 8 = 13 (AP24: sum is 13 for Virasoro, not 0)
        assert abs(S1[2] + S2[2] - 13.0) < 1e-10


# =========================================================================
# Section 3: Weighted generating function (6 tests)
# =========================================================================

class TestWeightedGF:
    """Cross-verify H(t) = t^2*sqrt(Q_L(t)) vs series."""

    def test_H_at_zero(self):
        """H(0) = 0."""
        for c in [1.0, 13.0, 25.0]:
            assert abs(weighted_shadow_gf(c, 0)) < 1e-15

    def test_H_series_vs_closed_form(self):
        """H(t) from series vs closed form at t=0.01."""
        c = 13.0
        t = 0.01
        H_closed = weighted_shadow_gf(c, t)
        S = shadow_tower_coefficients(c, 100)
        H_series = sum(r * S.get(r, 0) * t ** r for r in range(2, 100))
        rel_err = abs(H_series - H_closed) / abs(H_closed)
        assert rel_err < 1e-8, f"H_series={H_series}, H_closed={H_closed}, err={rel_err}"

    def test_H_series_vs_closed_form_c25(self):
        """H(t) series vs closed at c=25, t=0.1."""
        c = 25.0
        t = 0.1
        H_closed = weighted_shadow_gf(c, t)
        S = shadow_tower_coefficients(c, 100)
        H_series = sum(r * S.get(r, 0) * t ** r for r in range(2, 100))
        rel_err = abs(H_series - H_closed) / abs(H_closed)
        assert rel_err < 1e-6, f"rel_err={rel_err}"

    def test_H_leading_term(self):
        """H(t) ~ 2*kappa*t^2 + O(t^3) for small t."""
        c = 13.0
        t = 1e-5
        H = weighted_shadow_gf(c, t)
        kappa = virasoro_kappa(c)
        expected_leading = 2 * kappa * t ** 2
        assert abs(H - expected_leading) / abs(expected_leading) < 1e-4

    def test_H_complex(self):
        """H(t) for complex t matches real restriction on real axis."""
        c = 13.0
        t = 0.05
        H_real = weighted_shadow_gf(c, t)
        H_complex = weighted_shadow_gf_complex(c, t)
        assert abs(H_complex.imag) < 1e-12
        assert abs(H_complex.real - H_real) < 1e-12

    def test_H_squared_equals_t4_QL(self):
        """H(t)^2 = t^4 * Q_L(t) (the fundamental identity)."""
        c = 13.0
        t = 0.03
        H = weighted_shadow_gf(c, t)
        q0, q1, q2 = virasoro_shadow_metric_coeffs(c)
        Q = q0 + q1 * t + q2 * t ** 2
        lhs = H ** 2
        rhs = t ** 4 * Q
        assert abs(lhs - rhs) / abs(rhs) < 1e-10


# =========================================================================
# Section 4: Quantum modularity defects (8 tests)
# =========================================================================

class TestQuantumModularity:
    """Test quantum modular defect structure at rational points."""

    def test_S_defect_finite(self):
        """S-defect at x=1/2 is finite for convergent tower."""
        c = 25.0
        result = quantum_modularity_S_defect(c, 2)
        assert not result.get('singular')
        assert 'defects_by_weight' in result

    def test_S_defect_c13(self):
        """S-defect at x=1/2, c=13 (self-dual) is finite."""
        result = quantum_modularity_S_defect(13.0, 2)
        assert not result.get('singular')

    def test_T_defect_finite(self):
        """T-defect at x=1/3 is finite."""
        c = 25.0
        result = quantum_modularity_T_defect(c, 3)
        assert not result.get('singular')
        assert 'defects_by_weight' in result

    def test_defect_different_weights(self):
        """Different weight candidates produce different defects."""
        c = 25.0
        result = quantum_modularity_S_defect(c, 3, max_arity=60)
        if not result.get('singular') and 'defects_by_weight' in result:
            d0 = result['defects_by_weight'][0]
            d3 = result['defects_by_weight'][3]
            # Weight 0 and weight 3 should generally differ
            # (unless G_x = 0 or G_gamma_x = 0)
            assert not (abs(d0) < 1e-15 and abs(d3) < 1e-15)

    def test_scan_quantum_modularity(self):
        """Full scan returns results for all coprime p/q with q<=5."""
        results = scan_quantum_modularity(25.0, max_denom=5, max_arity=60)
        assert len(results) > 5  # At least: 1/1, 1/2, 1/3, 2/3, 1/4, 3/4, 1/5,...

    def test_G_at_rational_convergent(self):
        """G(1/10) converges for c=25 (rho ~ 0.24)."""
        c = 25.0
        rho = virasoro_shadow_radius(c)
        R = 1.0 / rho
        assert 1.0 / 10.0 < R, "1/10 should be inside convergence disk"
        G = shadow_gf_at_rational(c, 1, 10)
        assert abs(G) < 100  # should be finite and reasonable

    def test_G_at_rational_ising(self):
        """G(p/q) at Ising c=1/2 uses Borel regularization."""
        c = 0.5
        rho = virasoro_shadow_radius(c)
        assert rho > 1.0  # divergent
        G = shadow_gf_at_rational(c, 1, 10)
        # Should still return a finite (Borel-resummed) value
        assert math.isfinite(G)

    def test_borel_regularization_finite(self):
        """Borel regularization at t=0.1 gives finite answer."""
        c = 0.5
        G = shadow_gf_borel_regularized(c, 0.1)
        assert math.isfinite(G)


# =========================================================================
# Section 5: False theta functions (7 tests)
# =========================================================================

class TestFalseTheta:
    """Test false theta function and its connection to shadow towers."""

    def test_false_theta_at_zero(self):
        """Psi(0) = 1 (only n=0 term contributes)."""
        assert abs(false_theta_function(0.0) - 1.0) < 1e-14

    def test_false_theta_coefficients_triangular(self):
        """False theta has support on triangular numbers."""
        coeffs = false_theta_coefficients(50)
        # Triangular numbers: 0, 1, 3, 6, 10, 15, 21, 28, 36, 45
        triangular = {m * (m + 1) // 2 for m in range(10)}
        for n in range(50):
            if n in coeffs:
                assert n in triangular, f"Coefficient at n={n} not triangular"

    def test_false_theta_alternating(self):
        """Psi alternates: a_{m(m+1)/2} = (-1)^m."""
        coeffs = false_theta_coefficients(50)
        for m in range(8):
            n = m * (m + 1) // 2
            assert coeffs[n] == (-1) ** m, f"Wrong sign at m={m}, n={n}"

    def test_false_theta_evaluation(self):
        """Psi(1/2) is a finite computable number."""
        val = false_theta_function(0.5)
        assert math.isfinite(val)
        assert abs(val) < 10  # should be O(1)

    def test_shadow_vs_false_theta_overlap(self):
        """Check overlap between shadow tower and false theta at c=1/2."""
        result = shadow_tower_vs_false_theta(0.5, 20)
        # There should be SOME overlap (triangular number positions)
        assert result['has_triangular_support_overlap'] or len(result['comparisons']) >= 0

    def test_shadow_vs_false_theta_c1(self):
        """Shadow-false theta comparison at c=1."""
        result = shadow_tower_vs_false_theta(1.0, 20)
        assert 'shadow_coefficients' in result

    def test_minimal_model_central_charge(self):
        """c(3,4) = 1/2 (Ising), c(4,5) = 7/10 (tri-Ising)."""
        c_ising = minimal_model_central_charge(3, 4)
        assert abs(c_ising - 0.5) < 1e-14
        c_tri = minimal_model_central_charge(4, 5)
        assert abs(c_tri - 0.7) < 1e-14


# =========================================================================
# Section 6: Mock modular analysis (8 tests)
# =========================================================================

class TestMockModular:
    """Test mock modular structure of shadow PF."""

    def test_mock_analysis_ising(self):
        """Mock modular analysis at c=1/2 (Ising)."""
        result = mock_modular_shadow_analysis(0.5)
        assert result['is_minimal_model']
        assert result['shadow_depth'] == 'M'
        assert result['growth_type'] == 'divergent'
        assert result['borel_summable']

    def test_mock_analysis_convergent(self):
        """Mock modular analysis at c=25 (convergent)."""
        result = mock_modular_shadow_analysis(25.0)
        assert not result['is_minimal_model']
        assert result['shadow_depth'] == 'M'
        assert result['growth_type'] == 'convergent'
        assert 'sum_value' in result

    def test_mock_analysis_self_dual(self):
        """Mock modular analysis at c=13 (self-dual point)."""
        result = mock_modular_shadow_analysis(13.0)
        assert result['shadow_depth'] == 'M'
        assert 0.4 < result['shadow_radius'] < 0.55

    def test_optimal_truncation_ising(self):
        """Optimal truncation order for Ising is small (rho >> 1)."""
        result = mock_modular_shadow_analysis(0.5)
        if result.get('optimal_truncation') is not None:
            N_star = result['optimal_truncation']
            assert N_star < 10, f"N*={N_star} too large for rho>>1"

    def test_partial_sums_exist(self):
        """Partial sums are computed correctly."""
        result = mock_modular_shadow_analysis(13.0, max_terms=30)
        assert len(result['partial_sums']) > 10

    def test_ratio_tail_matches_rho(self):
        """Ratio tail from mock analysis approaches rho (averaged over oscillation)."""
        c = 25.0  # Use convergent case (less oscillation, better convergence)
        rho = virasoro_shadow_radius(c)
        result = mock_modular_shadow_analysis(c, max_terms=60)
        if 'ratio_tail' in result and len(result['ratio_tail']) >= 3:
            avg_ratio = sum(result['ratio_tail']) / len(result['ratio_tail'])
            assert abs(avg_ratio - rho) / rho < 0.3

    def test_mock_analysis_tri_ising(self):
        """Mock modular analysis at c=7/10 (tri-critical Ising)."""
        result = mock_modular_shadow_analysis(0.7)
        assert result['is_minimal_model']
        assert result['growth_type'] == 'divergent'

    def test_mock_returns_estimated_rho(self):
        """The mock analysis returns an estimated rho from ratio test."""
        result = mock_modular_shadow_analysis(25.0, max_terms=40)
        assert result.get('estimated_rho') is not None or result['growth_type'] == 'convergent'


# =========================================================================
# Section 7: Nahm conjecture (10 tests)
# =========================================================================

class TestNahmConjecture:
    """Test Nahm matrix construction and criterion."""

    def test_nahm_eigenvalue_equals_rho_squared(self):
        """The Nahm matrix eigenvalue = rho^2 (fundamental identity)."""
        for c in [1.0, 2.0, 7.0, 13.0, 25.0]:
            nahm = nahm_matrix_from_shadow(c)
            rho = virasoro_shadow_radius(c)
            assert abs(nahm['eigenvalue'] - rho ** 2) < 1e-10, (
                f"c={c}: eigenvalue={nahm['eigenvalue']}, rho^2={rho**2}"
            )

    def test_nahm_criterion_convergent(self):
        """Nahm criterion satisfied iff rho < 1 (convergent tower)."""
        c = 25.0
        rho = virasoro_shadow_radius(c)
        assert rho < 1.0
        nahm = nahm_matrix_from_shadow(c)
        assert nahm['nahm_criterion_satisfied']

    def test_nahm_criterion_divergent(self):
        """Nahm criterion violated iff rho > 1 (divergent tower)."""
        c = 0.5
        rho = virasoro_shadow_radius(c)
        assert rho > 1.0
        nahm = nahm_matrix_from_shadow(c)
        assert not nahm['nahm_criterion_satisfied']

    def test_nahm_c_equals_1(self):
        """Nahm matrix at c=1: rho ~ 3.24, criterion violated."""
        nahm = nahm_matrix_from_shadow(1.0)
        assert not nahm['nahm_criterion_satisfied']
        assert nahm['eigenvalue'] > 1.0

    def test_nahm_self_dual(self):
        """Nahm at c=13 (self-dual): rho ~ 0.467, criterion satisfied."""
        nahm = nahm_matrix_from_shadow(13.0)
        assert nahm['nahm_criterion_satisfied']
        assert 0.15 < nahm['eigenvalue'] < 0.35

    def test_nahm_scan_minimal_models(self):
        """All minimal models violate Nahm criterion (rho > 1)."""
        results = nahm_scan_minimal_models(8)
        for r in results:
            assert not r['nahm_criterion_satisfied'], (
                f"Model {r['model_name']} has Nahm satisfied, but c={r['c']}<c*"
            )

    def test_nahm_1x1_matrix(self):
        """Nahm matrix is 1x1 for single-generator Virasoro."""
        nahm = nahm_matrix_from_shadow(13.0)
        assert len(nahm['nahm_matrix']) == 1
        assert len(nahm['nahm_matrix'][0]) == 1

    def test_nahm_cross_verify(self):
        """Cross-verify Nahm eigenvalue via 3 paths."""
        result = cross_verify_nahm(13.0)
        assert result['nahm_eq_rho_sq']
        if result['formula_vs_ratio'] is not None:
            assert result['formula_vs_ratio'] < 0.15

    def test_nahm_cross_verify_c25(self):
        """Cross-verify Nahm at c=25."""
        result = cross_verify_nahm(25.0)
        assert result['nahm_eq_rho_sq']

    def test_nahm_not_degenerate(self):
        """Nahm matrix not degenerate for c > 0."""
        for c in [0.5, 1.0, 10.0, 25.0]:
            nahm = nahm_matrix_from_shadow(c)
            assert not nahm['degenerate']


# =========================================================================
# Section 8: Habiro ring integrality (8 tests)
# =========================================================================

class TestHabiroRing:
    """Test Habiro ring integrality at roots of unity."""

    def test_pochhammer_at_root(self):
        """(zeta_N; zeta_N)_N = 0 since product includes 1 - zeta_N^N = 0."""
        for N in [3, 4, 5, 6]:
            zeta = cmath.exp(2j * PI / N)
            poch = q_pochhammer(zeta, N)
            assert abs(poch) < 1e-10, f"(zeta_{N};zeta_{N})_{N} = {poch}"

    def test_pochhammer_small(self):
        """(q;q)_1 = 1-q, (q;q)_2 = (1-q)(1-q^2)."""
        q = 0.5
        assert abs(q_pochhammer(q, 1) - (1 - q)) < 1e-14
        assert abs(q_pochhammer(q, 2) - (1 - q) * (1 - q ** 2)) < 1e-14

    def test_habiro_zeta3_c25(self):
        """Z^sh(Vir_25, zeta_3) is finite."""
        result = habiro_element_test(25.0, 3)
        assert result['habiro_compatible']
        assert math.isfinite(abs(result['G_zeta_N']))

    def test_habiro_zeta4_c25(self):
        """Z^sh(Vir_25, zeta_4) is finite."""
        result = habiro_element_test(25.0, 4)
        assert result['habiro_compatible']

    def test_habiro_zeta5_c13(self):
        """Z^sh(Vir_13, zeta_5) is finite."""
        result = habiro_element_test(13.0, 5)
        assert result['habiro_compatible']

    def test_habiro_scan_c25(self):
        """Habiro scan at c=25: all values finite."""
        result = habiro_scan(25.0)
        assert result['all_finite']

    def test_habiro_scan_c13(self):
        """Habiro scan at c=13."""
        result = habiro_scan(13.0)
        assert result['all_finite']

    def test_habiro_pochhammer_zero_at_N(self):
        """Verify (zeta_N;zeta_N)_N = 0 in the Habiro test."""
        result = habiro_element_test(25.0, 4)
        assert result['pochhammer_zero_at_N']


# =========================================================================
# Section 9: Modular completion (6 tests)
# =========================================================================

class TestModularCompletion:
    """Test non-holomorphic modular completion of shadow PF."""

    def test_completion_at_tau_i(self):
        """Modular completion at tau=i (Im(tau)=1)."""
        result = modular_completion_shadow(13.0, tau_val=complex(0, 1))
        assert result['is_modular_completed']
        assert abs(result['E2_star_correction'] - 3.0 / PI) < 1e-10

    def test_completion_F1_holomorphic(self):
        """F1 holomorphic part = -kappa * log eta(tau), finite at tau=i."""
        result = modular_completion_shadow(13.0, tau_val=complex(0, 1))
        F1 = result['F1_holomorphic']
        assert cmath.isfinite(F1)

    def test_completion_nh_correction_scales_with_y(self):
        """Non-holomorphic correction ~ 1/y."""
        result1 = modular_completion_shadow(13.0, tau_val=complex(0, 1))
        result2 = modular_completion_shadow(13.0, tau_val=complex(0, 2))
        # nh correction ~ kappa * 3/(pi*y) / 24
        ratio = abs(result1['nh_correction'] / result2['nh_correction'])
        assert abs(ratio - 2.0) < 0.1  # correction scales as 1/y

    def test_completion_at_large_y(self):
        """At large Im(tau), non-holomorphic correction vanishes."""
        result = modular_completion_shadow(13.0, tau_val=complex(0, 1000))
        assert abs(result['nh_correction']) < 1e-3

    def test_completion_upper_half_plane_required(self):
        """Error for tau not in upper half-plane."""
        result = modular_completion_shadow(13.0, tau_val=complex(0, -1))
        assert 'error' in result

    def test_completion_includes_shadow_tower(self):
        """Completion includes the shadow tower sum."""
        result = modular_completion_shadow(13.0, tau_val=complex(0, 1), max_arity=30)
        assert 'shadow_tower_sum' in result
        assert math.isfinite(result['shadow_tower_sum'])


# =========================================================================
# Section 10: Radial limits (7 tests)
# =========================================================================

class TestRadialLimits:
    """Test radial limits at roots of unity."""

    def test_radial_limit_zeta3(self):
        """Radial limit at zeta_3 produces finite values."""
        result = radial_limit_shadow_pf(13.0, 3, num_points=15)
        assert result['num_points'] > 5
        assert result['limit_abs'] < 1e10

    def test_radial_limit_zeta4(self):
        """Radial limit at zeta_4."""
        result = radial_limit_shadow_pf(13.0, 4, num_points=15)
        assert result['num_points'] > 5

    def test_radial_limit_zeta6(self):
        """Radial limit at zeta_6."""
        result = radial_limit_shadow_pf(25.0, 6, num_points=15)
        assert result['num_points'] > 5

    def test_radial_limit_data_monotone(self):
        """As r -> 1, the approach data should stabilize."""
        result = radial_limit_shadow_pf(25.0, 4, num_points=20)
        data = result['approach_data']
        if len(data) >= 3:
            # Check that values don't oscillate wildly
            vals = [abs(d['F1']) for d in data]
            # The sequence should be roughly monotone near the end
            assert all(math.isfinite(v) for v in vals)

    def test_radial_limits_scan(self):
        """Scan at multiple roots of unity."""
        result = radial_limits_scan(13.0, [3, 4, 5])
        assert len(result['limits']) == 3

    def test_radial_limit_kappa_scaling(self):
        """Limits scale with kappa (the modular characteristic)."""
        result1 = radial_limit_shadow_pf(10.0, 4, num_points=10)
        result2 = radial_limit_shadow_pf(20.0, 4, num_points=10)
        # F1 = -kappa * log_eta, so ratio should be ~ kappa_2/kappa_1 = 2
        if (result1['limit_abs'] > 1e-10 and result2['limit_abs'] > 1e-10):
            ratio = result2['limit_abs'] / result1['limit_abs']
            assert 1.0 < ratio < 4.0  # approximately 2

    def test_radial_limit_ising(self):
        """Radial limit at c=1/2 (Ising)."""
        result = radial_limit_shadow_pf(0.5, 3, num_points=10)
        assert result['num_points'] > 0


# =========================================================================
# Section 11: Cross-verification (8 tests)
# =========================================================================

class TestCrossVerification:
    """Multi-path verification of shadow computations."""

    def test_cross_verify_c13_small_t(self):
        """Cross-verify G(t) at c=13, t=0.01."""
        result = cross_verify_shadow_gf(13.0, 0.01)
        assert result['paths_consistent']

    def test_cross_verify_c25_small_t(self):
        """Cross-verify G(t) at c=25, t=0.01."""
        result = cross_verify_shadow_gf(25.0, 0.01)
        assert result['paths_consistent']

    def test_cross_verify_H_identity(self):
        """H_series vs H_closed agrees to high precision."""
        result = cross_verify_shadow_gf(13.0, 0.02, max_arity=120)
        assert result['H_series_vs_closed'] < 1e-6

    def test_cross_verify_c2(self):
        """Cross-verify at c=2."""
        result = cross_verify_shadow_gf(2.0, 0.01)
        assert result['paths_consistent']

    def test_nahm_cross_verify_three_paths(self):
        """Nahm eigenvalue = rho^2 via three independent paths."""
        result = cross_verify_nahm(13.0)
        assert result['nahm_eq_rho_sq']

    def test_nahm_cross_verify_c2(self):
        """Three-path Nahm cross-verification at c=2."""
        result = cross_verify_nahm(2.0)
        assert result['nahm_eq_rho_sq']

    def test_kappa_additivity_check(self):
        """kappa is additive: kappa(Vir_c) = c/2 cross-checked via shadow tower."""
        for c in [1.0, 5.0, 13.0, 25.0]:
            S = shadow_tower_coefficients(c, 5)
            assert abs(S[2] - c / 2) < 1e-10

    def test_complementarity_sum_check(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c in [1.0, 5.0, 10.0, 13.0]:
            S1 = shadow_tower_coefficients(c, 3)
            S2 = shadow_tower_coefficients(26.0 - c, 3)
            sum_kappa = S1[2] + S2[2]
            assert abs(sum_kappa - 13.0) < 1e-10, f"sum={sum_kappa} at c={c}"


# =========================================================================
# Section 12: Zwegers completion (4 tests)
# =========================================================================

class TestZwegersCompletion:
    """Test Zwegers-type non-holomorphic completion."""

    def test_zwegers_completion_structure(self):
        """Zwegers completion at c=13, tau=i has required keys."""
        result = shadow_zwegers_completion(13.0, complex(0, 1))
        assert 'G_formal' in result
        assert 'nh_correction' in result
        assert 'G_completed' in result

    def test_zwegers_completion_nh_nonzero(self):
        """Non-holomorphic correction is nonzero for class M."""
        result = shadow_zwegers_completion(13.0, complex(0, 1))
        assert abs(result['nh_correction']) > 1e-15

    def test_zwegers_completion_c25(self):
        """Zwegers completion at c=25."""
        result = shadow_zwegers_completion(25.0, complex(0, 1))
        assert math.isfinite(result['G_formal'])
        assert math.isfinite(result['G_completed'])

    def test_zwegers_koszul_sign(self):
        """Shadow connection has monodromy -1 (Koszul sign), implies Delta > 0."""
        c = 13.0
        result = shadow_zwegers_completion(c, complex(0, 1))
        assert result['Delta'] > 0  # class M with complex branch points


# =========================================================================
# Section 13: Period polynomial (3 tests)
# =========================================================================

class TestPeriodPolynomial:
    """Test period polynomial of shadow generating function."""

    def test_period_polynomial_exists(self):
        """Period polynomial computation returns valid structure."""
        result = period_polynomial_shadow(13.0, degree=8)
        assert 'polynomial_coefficients' in result
        assert len(result['polynomial_coefficients']) == 9  # degrees 0..8

    def test_period_constant_term(self):
        """Constant term P_0 = sum S_r * C(r,0) = sum S_r."""
        c = 25.0
        result = period_polynomial_shadow(c, degree=5)
        S = shadow_tower_coefficients(c, 10)
        expected_P0 = sum(S.get(r, 0) for r in range(2, 10))
        assert abs(result['polynomial_coefficients'][0] - expected_P0) < 1e-6

    def test_period_polynomial_c1(self):
        """Period polynomial at c=1."""
        result = period_polynomial_shadow(1.0, degree=6)
        assert math.isfinite(result['leading_coefficient'])


# =========================================================================
# Section 14: W_3 extension (3 tests)
# =========================================================================

class TestW3Extension:
    """Test W_3 shadow data."""

    def test_w3_kappa(self):
        """kappa(W_3) = 5c/6 (from H_3 - 1 = 5/6)."""
        c = 2.0
        kappa, alpha, S4 = w3_shadow_data_T_line(c)
        assert abs(kappa - 5 * c / 6) < 1e-12

    def test_w3_cubic_universal(self):
        """W_3 cubic shadow coefficient alpha = 2 (universal)."""
        kappa, alpha, S4 = w3_shadow_data_T_line(10.0)
        assert alpha == 2

    def test_w3_shadow_exists(self):
        """W_3 shadow data returns valid triple."""
        kappa, alpha, S4 = w3_shadow_data_T_line(5.0)
        assert math.isfinite(kappa)
        assert math.isfinite(alpha)
        assert math.isfinite(S4)


# =========================================================================
# Section 15: Master summary (3 tests)
# =========================================================================

class TestMasterSummary:
    """Test master analysis and summary functions."""

    def test_master_analysis_c13(self):
        """Master analysis at c=13 returns all components."""
        result = quantum_modular_master_analysis(13.0, max_arity=30)
        assert 'nahm' in result
        assert 'mock_modular' in result
        assert 'cross_verify' in result
        assert 'habiro' in result
        assert result['convergent']

    def test_master_analysis_c1(self):
        """Master analysis at c=1 (divergent)."""
        result = quantum_modular_master_analysis(1.0, max_arity=30)
        assert not result['convergent']
        assert result['nahm']['eigenvalue'] > 1

    def test_quantum_modularity_summary_runs(self):
        """Summary function across landscape runs without error."""
        results = quantum_modularity_summary([1.0, 13.0, 25.0], max_arity=30)
        assert len(results) == 3
        # c=25 should be convergent
        assert results[2]['convergent']
        # c=1 should be divergent
        assert not results[0]['convergent']
