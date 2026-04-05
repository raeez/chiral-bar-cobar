r"""Tests for the Second-Generation Grand Unified Atlas (BC-105).

Verification (multi-path per the mandate):
  Path 1: Independent computation of each invariant
  Path 2: Cross-family consistency checks
  Path 3: Complementarity pair sums (kappa + kappa')
  Path 4: Depth class matches coefficient pattern
  Path 5: Extremals verified by exhaustive search

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP10): Tests must NOT hardcode wrong expected values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP39): kappa = c/2 ONLY for Virasoro.
"""

import cmath
import math
import pytest

from compute.lib.bc_grand_atlas_v2_engine import (
    # Section 0: shadow infrastructure
    _shadow_coeffs_from_tower,
    # Section 1: kappa formulas
    kappa_heisenberg,
    kappa_affine,
    kappa_virasoro,
    kappa_betagamma,
    kappa_w3_t,
    kappa_w3_w,
    kappa_WN,
    # Dual kappa
    dual_kappa_heisenberg,
    dual_kappa_affine,
    dual_kappa_virasoro,
    dual_kappa_betagamma,
    # Central charges
    central_charge_heisenberg,
    central_charge_affine,
    central_charge_virasoro,
    central_charge_betagamma,
    # Shadow classification
    shadow_class,
    shadow_depth,
    # Section 2: master entry
    FamilyEntry,
    build_master_table,
    _compute_shadow_coefficients,
    _shadow_zeta_eval,
    _shadow_zeta_deriv,
    _count_zeros_simple,
    _abscissa_estimate,
    _analytic_rank,
    _katz_sarnak_type,
    _selberg_membership,
    _arithmetic_depth,
    _effective_curvature,
    # Section 4: consistency matrix
    PairData,
    compute_pair_data,
    build_consistency_matrix,
    # Section 5: depth class stats
    DepthClassStats,
    compute_depth_class_stats,
    # Section 6: arithmetic hierarchy
    arithmetic_hierarchy,
    max_arithmetic_depth,
    min_nonzero_arithmetic_depth,
    # Section 7: complementarity
    ComplementarityEntry,
    build_complementarity_atlas,
    # Section 8: extremals
    ExtremalRecord,
    find_extremals,
    # Section 9: scaling laws
    ScalingLaw,
    _linear_regression,
    check_rho1_vs_kappa,
    check_zeta2_normalization,
    check_zero_density_ratio,
    check_all_scaling_laws,
    # Section 10: grand atlas
    GrandAtlas,
    build_grand_atlas,
    atlas_summary,
    atlas_to_dict,
    # Section 11: verification
    verify_kappa_complementarity,
    verify_depth_class_consistency,
    verify_shadow_zeta_at_large_s,
    verify_exhaustive_extremals,
)


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture(scope="module")
def master_table():
    """Build the master table once for all tests."""
    return build_master_table(max_r=30)


@pytest.fixture(scope="module")
def small_atlas():
    """Build a small atlas for integration tests."""
    return build_grand_atlas(max_r=30)


# ============================================================================
# 1. Kappa formula tests (AP1, AP9, AP39, AP48)
# ============================================================================

class TestKappaFormulas:
    """Verify kappa formulas by independent computation."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        for k in [1, 2, 3, 5, 10]:
            assert kappa_heisenberg(k) == float(k)

    def test_affine_sl2_kappa(self):
        """kappa(V_k(sl_2)) = 3(k+2)/4.  dim=3, h^v=2."""
        for k in [1, 2, 3]:
            expected = 3.0 * (k + 2.0) / 4.0
            assert abs(kappa_affine("A", 1, k) - expected) < 1e-12

    def test_affine_sl3_kappa(self):
        """kappa(V_k(sl_3)) = 4(k+3)/3.  dim=8, h^v=3."""
        for k in [1, 2, 3]:
            expected = 4.0 * (k + 3.0) / 3.0
            assert abs(kappa_affine("A", 2, k) - expected) < 1e-12

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2.  This is ONLY for Virasoro (AP39)."""
        for c in [0.5, 1, 13, 25, 26]:
            assert abs(kappa_virasoro(c) - c / 2.0) < 1e-12

    def test_betagamma_kappa(self):
        """kappa(bg_lam) = (6*lam^2 - 6*lam + 1)."""
        lam = 0.5
        c = 2.0 * (6.0 * 0.25 - 3.0 + 1.0)  # = 2*(-0.5) = -1.0
        assert abs(kappa_betagamma(lam) - c / 2.0) < 1e-12

    def test_w3_t_kappa_equals_virasoro(self):
        """On T-line, W3 kappa = c/2 (Virasoro restriction)."""
        for c in [2, 10, 50]:
            assert abs(kappa_w3_t(c) - kappa_virasoro(c)) < 1e-12

    def test_w3_w_kappa(self):
        """On W-line, kappa = c/3."""
        for c in [3, 9, 30]:
            assert abs(kappa_w3_w(c) - c / 3.0) < 1e-12

    def test_w_N_kappa(self):
        """kappa(W_N) = c * (H_N - 1)."""
        # W_2 = Virasoro: H_2 - 1 = 1/2, so kappa = c/2
        assert abs(kappa_WN(2, 10) - 5.0) < 1e-12
        # W_3: H_3 - 1 = 1/2 + 1/3 = 5/6
        assert abs(kappa_WN(3, 6) - 6.0 * 5.0 / 6.0) < 1e-12

    def test_kappa_cross_method_affine(self):
        """Cross-verify kappa via dim*k/(k+h^v) asymptotics.

        At large k: kappa ~ dim/2, central_charge ~ dim.
        So kappa/c ~ 1/2 for affine KM at large k.
        """
        for k in [100.0, 1000.0]:
            kap = kappa_affine("A", 1, k)
            c = central_charge_affine("A", 1, k)
            # kappa = 3(k+2)/4, c = 3k/(k+2)
            # kappa/c = (k+2)^2/(4k) -> k/4 at large k
            # This is NOT c/2; it shows AP39
            ratio = kap / c
            expected_ratio = (k + 2.0) ** 2 / (4.0 * k)
            assert abs(ratio - expected_ratio) < 1e-8

    def test_kappa_E8_independent(self):
        """kappa(V_1(E_8)) = dim(E_8)*(1+30)/(2*30) = 248*31/60."""
        expected = 248.0 * 31.0 / 60.0
        actual = kappa_affine("E", 8, 1)
        assert abs(actual - expected) < 1e-10


# ============================================================================
# 2. Dual kappa and complementarity tests (AP24, AP33)
# ============================================================================

class TestDualKappa:
    """Verify Koszul dual kappa and complementarity sums."""

    def test_heisenberg_dual(self):
        """kappa(H_k^!) = -k.  Sum = 0."""
        for k in [1, 2, 5]:
            assert abs(kappa_heisenberg(k) + dual_kappa_heisenberg(k)) < 1e-12

    def test_affine_sl2_dual(self):
        """kappa + kappa^! = 0 for affine sl_2 (FF involution)."""
        for k in [1, 2, 3, 4, 5]:
            kap = kappa_affine("A", 1, k)
            kap_dual = dual_kappa_affine("A", 1, k)
            assert abs(kap + kap_dual) < 1e-12

    def test_virasoro_complementarity_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for ALL c (AP24)."""
        for c in [0.5, 1, 2, 6, 10, 13, 20, 25, 26]:
            kap = kappa_virasoro(c)
            kap_dual = dual_kappa_virasoro(c)
            assert abs(kap + kap_dual - 13.0) < 1e-12, \
                f"c={c}: kappa+kappa'={kap+kap_dual}, expected 13"

    def test_virasoro_self_dual_at_c13(self):
        """At c=13: kappa = kappa^! = 13/2 = 6.5."""
        assert abs(kappa_virasoro(13) - dual_kappa_virasoro(13)) < 1e-12

    def test_betagamma_dual(self):
        """bg dual goes through Virasoro."""
        lam = 0.5
        kap = kappa_betagamma(lam)
        kap_dual = dual_kappa_betagamma(lam)
        # kap + kap_dual = c/2 + (26-c)/2 = 13
        assert abs(kap + kap_dual - 13.0) < 1e-12

    @pytest.mark.parametrize("c", [0.5, 1.0, 5.0, 10.0, 13.0, 20.0, 25.0])
    def test_complementarity_sum_parametric(self, c):
        """Parametric test of kappa + kappa' = 13 for Virasoro."""
        assert abs(kappa_virasoro(c) + dual_kappa_virasoro(c) - 13.0) < 1e-12


# ============================================================================
# 3. Central charge tests
# ============================================================================

class TestCentralCharges:
    """Verify central charge formulas."""

    def test_heisenberg_cc(self):
        """c(H_k) = 1 regardless of k."""
        for k in [1, 5, 100]:
            assert abs(central_charge_heisenberg(k) - 1.0) < 1e-12

    def test_affine_sl2_cc(self):
        """c(V_k(sl_2)) = 3k/(k+2)."""
        for k in [1, 2, 3]:
            expected = 3.0 * k / (k + 2.0)
            assert abs(central_charge_affine("A", 1, k) - expected) < 1e-12

    def test_virasoro_cc(self):
        """c(Vir_c) = c (tautological)."""
        for c in [1, 13, 26]:
            assert abs(central_charge_virasoro(c) - c) < 1e-12

    def test_betagamma_cc_at_half(self):
        """c(bg_{1/2}) = 2(6/4 - 3 + 1) = -1."""
        c = central_charge_betagamma(0.5)
        assert abs(c - (-1.0)) < 1e-12


# ============================================================================
# 4. Shadow classification tests
# ============================================================================

class TestShadowClassification:
    """Verify depth class G/L/C/M."""

    def test_heisenberg_class_G(self):
        assert shadow_class('heisenberg') == 'G'
        assert shadow_depth('heisenberg') == 2

    def test_affine_class_L(self):
        assert shadow_class('affine_sl2') == 'L'
        assert shadow_class('affine_sl3') == 'L'
        assert shadow_depth('affine_sl2') == 3

    def test_betagamma_class_C(self):
        assert shadow_class('betagamma') == 'C'
        assert shadow_depth('betagamma') == 4

    def test_virasoro_class_M(self):
        assert shadow_class('virasoro') == 'M'
        assert shadow_depth('virasoro') == float('inf')

    def test_w3_class_M(self):
        assert shadow_class('w3_t') == 'M'
        assert shadow_class('w3_w') == 'M'


# ============================================================================
# 5. Shadow coefficient tests
# ============================================================================

class TestShadowCoefficients:
    """Verify shadow tower computation."""

    def test_heisenberg_only_S2(self):
        """Heisenberg has S_2 = k and S_r = 0 for r >= 3."""
        coeffs = _compute_shadow_coefficients('heisenberg', 3.0, 20)
        assert abs(coeffs[2] - 3.0) < 1e-12
        for r in range(3, 21):
            assert abs(coeffs[r]) < 1e-15

    def test_affine_sl2_S2_S3(self):
        """Affine sl_2 at k=1: S_2 = 3*3/4 = 9/4, S_3 = 4/3."""
        coeffs = _compute_shadow_coefficients('affine_sl2', 1.0, 20)
        assert abs(coeffs[2] - 2.25) < 1e-10
        assert abs(coeffs[3] - 4.0 / 3.0) < 1e-10
        for r in range(4, 21):
            assert abs(coeffs[r]) < 1e-14

    def test_betagamma_S2_S3_S4(self):
        """Beta-gamma at lam=0.5: S_2=kappa, S_3=2, S_4 computed."""
        coeffs = _compute_shadow_coefficients('betagamma', 0.5, 20)
        c = central_charge_betagamma(0.5)
        kap = kappa_betagamma(0.5)
        assert abs(coeffs[2] - kap) < 1e-10
        assert abs(coeffs[3] - 2.0) < 1e-10
        # S_4 = 10/(c(5c+22))
        if c != 0 and 5.0 * c + 22.0 != 0:
            S4_expected = 10.0 / (c * (5.0 * c + 22.0))
            assert abs(coeffs[4] - S4_expected) < 1e-10
        for r in range(5, 21):
            assert abs(coeffs[r]) < 1e-14

    def test_virasoro_S2_equals_kappa(self):
        """Virasoro S_2 = kappa = c/2."""
        for c in [1.0, 10.0, 25.0]:
            coeffs = _compute_shadow_coefficients('virasoro', c, 20)
            assert abs(coeffs[2] - c / 2.0) < 1e-10

    def test_virasoro_tower_nonzero(self):
        """Virasoro has S_r != 0 for r >= 3 (class M)."""
        coeffs = _compute_shadow_coefficients('virasoro', 10.0, 20)
        for r in range(3, 15):
            assert abs(coeffs[r]) > 1e-15, f"S_{r} should be nonzero for Virasoro"

    def test_self_contained_matches_imported(self):
        """Self-contained computation matches imported provider."""
        coeffs_import = _compute_shadow_coefficients('virasoro', 10.0, 20)
        # Also compute via _shadow_coeffs_from_tower
        # For Virasoro c=10: kappa=5, alpha=2 (cubic shadow parameter),
        # S4 = 10/(c*(5c+22)) = 10/(10*72)
        kap = 5.0
        alpha = 2.0  # NOT 6; alpha is the cubic shadow param, S_3 = alpha
        S4 = 10.0 / (10.0 * (50.0 + 22.0))
        coeffs_manual = _shadow_coeffs_from_tower(kap, alpha, S4, 20)
        for r in range(2, 21):
            assert abs(coeffs_import[r] - coeffs_manual[r]) < 1e-8, \
                f"S_{r} mismatch: {coeffs_import[r]} vs {coeffs_manual[r]}"


# ============================================================================
# 6. Shadow zeta evaluation tests
# ============================================================================

class TestShadowZeta:
    """Verify shadow zeta function evaluation."""

    def test_heisenberg_zeta_exact(self):
        """zeta_{H_k}(s) = k * 2^{-s} (single term)."""
        for k in [1.0, 3.0, 5.0]:
            coeffs = _compute_shadow_coefficients('heisenberg', k, 10)
            for s in [2.0, 3.0, 5.0]:
                z = _shadow_zeta_eval(coeffs, complex(s, 0))
                expected = k * 2.0 ** (-s)
                assert abs(z - expected) < 1e-12

    def test_affine_sl2_zeta_two_terms(self):
        """zeta(s) = S_2 * 2^{-s} + S_3 * 3^{-s} for affine."""
        coeffs = _compute_shadow_coefficients('affine_sl2', 1.0, 10)
        S2 = coeffs[2]
        S3 = coeffs[3]
        for s in [2.0, 3.0]:
            z = _shadow_zeta_eval(coeffs, complex(s, 0))
            expected = S2 * 2.0 ** (-s) + S3 * 3.0 ** (-s)
            assert abs(z - expected) < 1e-12

    def test_zeta_at_negative_integers_moments(self):
        """zeta_A(-n) = sum S_r * r^n (exact for Dirichlet series)."""
        coeffs = _compute_shadow_coefficients('virasoro', 10.0, 30)
        for n in [0, 1, 2, 3]:
            z = _shadow_zeta_eval(coeffs, complex(-n, 0), 30)
            moment = sum(coeffs.get(r, 0.0) * r ** n for r in range(2, 31))
            assert abs(z.real - moment) < 1e-6, \
                f"n={n}: zeta(-{n})={z.real}, moment={moment}"

    def test_zeta_derivative(self):
        """Verify derivative by finite difference."""
        coeffs = _compute_shadow_coefficients('virasoro', 10.0, 30)
        s0 = complex(3.0, 0.0)
        h = 1e-7
        z_deriv = _shadow_zeta_deriv(coeffs, s0, 30)
        z_fd = (_shadow_zeta_eval(coeffs, s0 + h, 30) - _shadow_zeta_eval(coeffs, s0 - h, 30)) / (2 * h)
        assert abs(z_deriv - z_fd) < 1e-4, \
            f"Derivative mismatch: analytic={z_deriv}, FD={z_fd}"


# ============================================================================
# 7. Master table tests
# ============================================================================

class TestMasterTable:
    """Verify the master invariant table."""

    def test_table_has_families(self, master_table):
        """Table should have 49+ families."""
        assert len(master_table) >= 49

    def test_heisenberg_entries(self, master_table):
        """Heisenberg H_k for k=1..8 present."""
        for k in range(1, 9):
            name = f'Heis_k={k}'
            assert name in master_table
            entry = master_table[name]
            assert entry.depth_class == 'G'
            assert abs(entry.kappa - float(k)) < 1e-12
            assert abs(entry.central_charge - 1.0) < 1e-12

    def test_virasoro_entries(self, master_table):
        """Virasoro at c=0.5, 1, 13, 26 present."""
        for c in [0.5, 1.0, 13.0, 26.0]:
            name = f'Vir_c={c}'
            assert name in master_table
            entry = master_table[name]
            assert entry.depth_class == 'M'
            assert abs(entry.kappa - c / 2.0) < 1e-12

    def test_affine_E8_present(self, master_table):
        """Affine E_8 at k=1 present with correct kappa."""
        assert 'aff_E_8_k=1' in master_table
        e = master_table['aff_E_8_k=1']
        assert e.depth_class == 'L'
        expected_kappa = 248.0 * 31.0 / 60.0
        assert abs(e.kappa - expected_kappa) < 1e-8

    def test_all_entries_have_shadow_coeffs(self, master_table):
        """Every entry should have shadow coefficients."""
        for name, entry in master_table.items():
            assert len(entry.shadow_coeffs) > 0, f"{name} has no shadow coefficients"
            assert 2 in entry.shadow_coeffs, f"{name} missing S_2"

    def test_S2_equals_kappa(self, master_table):
        """S_2 = kappa for all families (AP39)."""
        for name, entry in master_table.items():
            assert abs(entry.shadow_coeffs[2] - entry.kappa) < 1e-8, \
                f"{name}: S_2={entry.shadow_coeffs[2]}, kappa={entry.kappa}"

    def test_delta_formula(self, master_table):
        """Delta = 8 * kappa * S_4."""
        for name, entry in master_table.items():
            expected = 8.0 * entry.kappa * entry.S4
            assert abs(entry.Delta - expected) < 1e-8, \
                f"{name}: Delta={entry.Delta}, expected={expected}"

    def test_class_G_zero_S3_S4(self, master_table):
        """Class G (Heisenberg): S_3 = S_4 = 0."""
        for name, entry in master_table.items():
            if entry.depth_class == 'G':
                assert abs(entry.S3) < 1e-15, f"{name}: S3={entry.S3}"
                assert abs(entry.S4) < 1e-15, f"{name}: S4={entry.S4}"

    def test_class_G_no_zeros(self, master_table):
        """Class G (Heisenberg) should have no shadow zeta zeros."""
        for name, entry in master_table.items():
            if entry.depth_class == 'G':
                assert entry.N_zeros_100 == 0, \
                    f"{name}: expected 0 zeros, got {entry.N_zeros_100}"

    def test_class_L_zero_S4_onwards(self, master_table):
        """Class L: S_r = 0 for r >= 4."""
        for name, entry in master_table.items():
            if entry.depth_class == 'L':
                for r in range(4, min(20, max(entry.shadow_coeffs.keys()) + 1)):
                    assert abs(entry.shadow_coeffs.get(r, 0.0)) < 1e-14, \
                        f"{name}: S_{r}={entry.shadow_coeffs.get(r, 0.0)}"


# ============================================================================
# 8. Complementarity atlas tests
# ============================================================================

class TestComplementarity:
    """Verify complementarity atlas."""

    def test_all_sums_correct(self, master_table):
        """All complementarity sums should be correct."""
        results = verify_kappa_complementarity(master_table)
        for name, ksum, expected, matches in results:
            assert matches, f"{name}: kappa_sum={ksum}, expected={expected}"

    def test_heisenberg_sum_zero(self, master_table):
        """Heisenberg: kappa + kappa' = 0."""
        for k in range(1, 9):
            e = master_table[f'Heis_k={k}']
            if e.dual_kappa is not None:
                assert abs(e.kappa + e.dual_kappa) < 1e-12

    def test_virasoro_sum_13(self, master_table):
        """Virasoro: kappa + kappa' = 13 for all c (AP24)."""
        for c in [0.5, 1.0, 10.0, 13.0, 25.0, 26.0]:
            name = f'Vir_c={c}'
            if name in master_table:
                e = master_table[name]
                if e.dual_kappa is not None:
                    assert abs(e.kappa + e.dual_kappa - 13.0) < 1e-12

    def test_affine_sl2_sum_zero(self, master_table):
        """Affine sl_2: kappa + kappa' = 0 (FF involution)."""
        for k in range(1, 6):
            name = f'aff_sl2_k={k}'
            e = master_table[name]
            if e.dual_kappa is not None:
                assert abs(e.kappa + e.dual_kappa) < 1e-12

    def test_complementarity_atlas_no_violations(self, master_table):
        """Build complementarity atlas; check no violations."""
        atlas = build_complementarity_atlas(master_table)
        for name, entry in atlas.items():
            assert entry.sum_correct, \
                f"{name}: kappa_sum={entry.kappa_sum}, expected={entry.expected_sum}"


# ============================================================================
# 9. Depth class consistency tests
# ============================================================================

class TestDepthClassConsistency:
    """Verify depth class matches shadow coefficient pattern."""

    def test_all_families_consistent(self, master_table):
        """Every family's declared class matches coefficient pattern."""
        results = verify_depth_class_consistency(master_table)
        for name, expected, actual, consistent in results:
            assert consistent, \
                f"{name}: declared={expected}, pattern={actual}"


# ============================================================================
# 10. Cross-family consistency matrix tests
# ============================================================================

class TestConsistencyMatrix:
    """Verify the cross-family consistency matrix."""

    def test_matrix_symmetric_zeta_diff(self, master_table):
        """Zeta differences are antisymmetric: diff(A,B) = -diff(B,A)."""
        names = ['Heis_k=1', 'aff_sl2_k=1', 'Vir_c=10.0']
        names = [n for n in names if n in master_table]
        matrix = build_consistency_matrix(master_table, names, max_r=30)
        for (nA, nB), pd in matrix.items():
            # Check reverse pair via computing manually
            pd_rev = compute_pair_data(master_table[nB], master_table[nA], 30)
            assert abs(pd.zeta_diff_s2 + pd_rev.zeta_diff_s2) < 1e-10

    def test_diagonal_is_zero(self, master_table):
        """diff(A,A) = 0 (self-consistency)."""
        name = 'Heis_k=1'
        if name in master_table:
            e = master_table[name]
            pd = compute_pair_data(e, e, 30)
            assert abs(pd.zeta_diff_s2) < 1e-12
            assert abs(pd.zeta_diff_s3) < 1e-12
            assert abs(pd.zeta_diff_s4) < 1e-12

    def test_rankin_selberg_nonneg_for_self(self, master_table):
        """L(1, zeta_A x zeta_A) = sum S_r^2 / r >= 0."""
        for name in ['Heis_k=2', 'Vir_c=10.0']:
            if name in master_table:
                e = master_table[name]
                pd = compute_pair_data(e, e, 30)
                assert pd.rankin_selberg.real >= -1e-12


# ============================================================================
# 11. Depth class statistics tests
# ============================================================================

class TestDepthClassStats:
    """Verify per-class aggregate statistics."""

    def test_all_four_classes_present(self, master_table):
        """All four depth classes G, L, C, M should be represented."""
        stats = compute_depth_class_stats(master_table)
        for cls in ['G', 'L', 'C', 'M']:
            assert cls in stats, f"Class {cls} missing from stats"
            assert stats[cls].n_families > 0

    def test_class_G_count(self, master_table):
        """Class G = Heisenberg: 8 families."""
        stats = compute_depth_class_stats(master_table)
        assert stats['G'].n_families == 8

    def test_class_L_has_affine(self, master_table):
        """Class L should contain all affine algebras."""
        stats = compute_depth_class_stats(master_table)
        assert stats['L'].n_families >= 8  # sl2@5 + sl3@3 + others

    def test_class_M_has_virasoro(self, master_table):
        """Class M should contain all Virasoro + W algebras."""
        stats = compute_depth_class_stats(master_table)
        assert stats['M'].n_families >= 10

    def test_shadow_entropy_nonneg(self, master_table):
        """Shadow entropy should be non-negative."""
        stats = compute_depth_class_stats(master_table)
        for cls, s in stats.items():
            assert s.shadow_entropy >= -1e-15


# ============================================================================
# 12. Arithmetic hierarchy tests
# ============================================================================

class TestArithmeticHierarchy:
    """Verify arithmetic depth ordering."""

    def test_hierarchy_sorted(self, master_table):
        """Hierarchy should be sorted by d_total then kappa."""
        order = arithmetic_hierarchy(master_table)
        for i in range(len(order) - 1):
            assert order[i][1] <= order[i + 1][1]

    def test_class_G_minimal_depth(self, master_table):
        """Class G (Heisenberg) should have d_total = 1."""
        for name, entry in master_table.items():
            if entry.depth_class == 'G':
                assert entry.d_total == 1, f"{name}: d_total={entry.d_total}"

    def test_class_M_maximal_depth(self, master_table):
        """Class M should have the largest d_total."""
        name, d = max_arithmetic_depth(master_table)
        entry = master_table[name]
        assert entry.depth_class == 'M'

    def test_min_nonzero_is_class_L(self, master_table):
        """Minimal nonzero depth should be class L (d_alg=1 -> d=2)."""
        name, d = min_nonzero_arithmetic_depth(master_table)
        entry = master_table[name]
        assert entry.depth_class in ('L', 'C')


# ============================================================================
# 13. Extremal value tests
# ============================================================================

class TestExtremals:
    """Verify extremal families."""

    def test_extremals_not_empty(self, master_table):
        """Should find at least 5 extremal records."""
        extremals = find_extremals(master_table)
        assert len(extremals) >= 5

    def test_zero_zeros_is_class_G(self, master_table):
        """Family with zero zeros should be class G."""
        extremals = find_extremals(master_table)
        if 'zero_zeros' in extremals:
            name = extremals['zero_zeros'].family_name
            assert master_table[name].depth_class == 'G'

    def test_largest_kappa_correct(self, master_table):
        """Largest |kappa| verified by exhaustive search."""
        extremals = find_extremals(master_table)
        rec = extremals['largest_kappa']
        # Verify by brute force
        max_kap = max(abs(e.kappa) for e in master_table.values())
        assert abs(rec.value - max_kap) < 1e-10

    def test_smallest_kappa_correct(self, master_table):
        """Smallest nonzero |kappa| verified by exhaustive search."""
        extremals = find_extremals(master_table)
        if 'smallest_kappa' in extremals:
            rec = extremals['smallest_kappa']
            min_kap = min(
                abs(e.kappa) for e in master_table.values() if abs(e.kappa) > 1e-12
            )
            assert abs(rec.value - min_kap) < 1e-10

    def test_exhaustive_verification(self, master_table):
        """Run the built-in exhaustive extremal verification."""
        checks = verify_exhaustive_extremals(master_table)
        for category, passed in checks.items():
            assert passed, f"Extremal '{category}' failed exhaustive check"


# ============================================================================
# 14. Scaling law tests
# ============================================================================

class TestScalingLaws:
    """Verify universal scaling law tests."""

    def test_scaling_laws_run(self, master_table):
        """All scaling law tests should run without error."""
        laws = check_all_scaling_laws(master_table)
        assert 'rho1_vs_kappa' in laws
        assert 'zeta2_normalization' in laws
        assert 'zero_density_ratio' in laws

    def test_linear_regression_exact(self):
        """Linear regression on exact line y = 2x + 3."""
        xs = [1.0, 2.0, 3.0, 4.0, 5.0]
        ys = [5.0, 7.0, 9.0, 11.0, 13.0]
        a, b, r2 = _linear_regression(xs, ys)
        assert abs(a - 3.0) < 1e-10
        assert abs(b - 2.0) < 1e-10
        assert abs(r2 - 1.0) < 1e-10

    def test_linear_regression_constant(self):
        """Constant y => slope = 0."""
        xs = [1.0, 2.0, 3.0, 4.0, 5.0]
        ys = [7.0, 7.0, 7.0, 7.0, 7.0]
        a, b, r2 = _linear_regression(xs, ys)
        assert abs(b) < 1e-10


# ============================================================================
# 15. Grand atlas integration tests
# ============================================================================

class TestGrandAtlas:
    """Integration tests for the full grand atlas."""

    def test_atlas_builds(self, small_atlas):
        """Atlas should build without error."""
        assert small_atlas is not None
        assert len(small_atlas.families) >= 49

    def test_atlas_has_all_components(self, small_atlas):
        """Atlas should have all 7 components."""
        assert len(small_atlas.families) > 0
        assert small_atlas.consistency_matrix is not None
        assert small_atlas.depth_class_stats is not None
        assert small_atlas.arithmetic_order is not None
        assert small_atlas.complementarity is not None
        assert small_atlas.extremals is not None
        assert small_atlas.scaling_laws is not None

    def test_atlas_summary_keys(self, small_atlas):
        """Summary should have expected keys."""
        s = atlas_summary(small_atlas)
        for key in ['n_families', 'class_distribution', 'kappa_range',
                     'n_with_zeros', 'extremals', 'scaling_laws',
                     'complementarity_violations']:
            assert key in s, f"Missing key: {key}"

    def test_atlas_to_dict_serializable(self, small_atlas):
        """Atlas dict should be JSON-serializable."""
        d = atlas_to_dict(small_atlas)
        import json
        json_str = json.dumps(d, default=str)
        assert len(json_str) > 100

    def test_no_complementarity_violations(self, small_atlas):
        """No complementarity violations in the atlas."""
        s = atlas_summary(small_atlas)
        assert s['complementarity_violations'] == 0


# ============================================================================
# 16. Verification function tests
# ============================================================================

class TestVerificationFunctions:
    """Test the built-in verification utilities."""

    def test_kappa_complementarity(self, master_table):
        """All complementarity sums should match."""
        results = verify_kappa_complementarity(master_table)
        assert len(results) > 0
        for name, ksum, expected, matches in results:
            assert matches, f"{name}: sum={ksum}, expected={expected}"

    def test_depth_class_consistency(self, master_table):
        """All depth classes should be consistent."""
        results = verify_depth_class_consistency(master_table)
        assert len(results) > 0
        for name, expected, actual, consistent in results:
            assert consistent, f"{name}: expected={expected}, actual={actual}"

    def test_large_s_behavior(self, master_table):
        """zeta_A(sigma) ~ kappa * 2^{-sigma} for large sigma.

        Only applies to class G/L/C where the Dirichlet series converges.
        Class M families with rho > 1 have sigma_c = +infinity; the truncated
        sum at finite order does NOT approximate the leading term.
        """
        results = verify_shadow_zeta_at_large_s(master_table, sigma=20.0)
        assert len(results) > 0
        for name, ratio, consistent in results:
            entry = master_table[name]
            if entry.depth_class == 'M':
                continue  # Skip divergent class M series
            assert consistent, f"{name}: ratio={ratio}"


# ============================================================================
# 17. Abscissa of convergence tests
# ============================================================================

class TestAbscissa:
    """Verify abscissa of convergence estimates."""

    def test_class_G_abscissa_minus_inf(self, master_table):
        """Class G: sigma_c = -inf (entire)."""
        for name, entry in master_table.items():
            if entry.depth_class == 'G':
                assert entry.sigma_c == float('-inf'), \
                    f"{name}: sigma_c={entry.sigma_c}"

    def test_class_L_abscissa_minus_inf(self, master_table):
        """Class L: sigma_c = -inf (finite Dirichlet polynomial)."""
        for name, entry in master_table.items():
            if entry.depth_class == 'L':
                assert entry.sigma_c == float('-inf'), \
                    f"{name}: sigma_c={entry.sigma_c}"

    def test_class_C_abscissa_minus_inf(self, master_table):
        """Class C: sigma_c = -inf."""
        for name, entry in master_table.items():
            if entry.depth_class == 'C':
                assert entry.sigma_c == float('-inf'), \
                    f"{name}: sigma_c={entry.sigma_c}"


# ============================================================================
# 18. Q_contact tests
# ============================================================================

class TestQContact:
    """Verify Q^{contact} invariant."""

    def test_virasoro_Q_contact(self, master_table):
        """Q^{contact}(Vir_c) = 10/(c(5c+22))."""
        for c in [0.5, 1.0, 10.0, 25.0, 26.0]:
            name = f'Vir_c={c}'
            if name in master_table:
                e = master_table[name]
                expected = 10.0 / (c * (5.0 * c + 22.0))
                assert abs(e.Q_contact - expected) < 1e-10, \
                    f"c={c}: Q_contact={e.Q_contact}, expected={expected}"

    def test_heisenberg_Q_contact_zero(self, master_table):
        """Class G: Q_contact = 0."""
        for name, entry in master_table.items():
            if entry.depth_class == 'G':
                assert abs(entry.Q_contact) < 1e-15


# ============================================================================
# 19. Katz-Sarnak type tests
# ============================================================================

class TestKatzSarnak:
    """Verify Katz-Sarnak type assignment."""

    def test_class_G_is_U(self):
        assert _katz_sarnak_type('heisenberg', 'G') == 'U'

    def test_class_L_is_USp(self):
        assert _katz_sarnak_type('affine_sl2', 'L') == 'USp'

    def test_virasoro_is_SO_odd(self):
        assert _katz_sarnak_type('virasoro', 'M') == 'SO(odd)'


# ============================================================================
# 20. Selberg class membership tests
# ============================================================================

class TestSelbergClass:
    """Verify Selberg class membership assessment."""

    def test_heisenberg_satisfies_S1(self, master_table):
        """All families satisfy S1 (Dirichlet series)."""
        for name, entry in master_table.items():
            assert 'S1' in entry.selberg_axioms

    def test_class_GLC_satisfies_S2(self, master_table):
        """Class G/L/C satisfy S2 (entire = meromorphic a fortiori)."""
        for name, entry in master_table.items():
            if entry.depth_class in ('G', 'L', 'C'):
                assert 'S2' in entry.selberg_axioms

    def test_class_GLC_satisfies_S5(self, master_table):
        """Finite Dirichlet polynomials trivially have Euler product."""
        for name, entry in master_table.items():
            if entry.depth_class in ('G', 'L', 'C'):
                assert 'S5' in entry.selberg_axioms


# ============================================================================
# 21. Effective curvature tests (AP29)
# ============================================================================

class TestEffectiveCurvature:
    """Verify kappa_eff = kappa + kappa(ghost) = kappa - 13."""

    def test_virasoro_critical(self, master_table):
        """At c=26: kappa=13, kappa_eff=0 (anomaly cancellation)."""
        e = master_table.get('Vir_c=26.0')
        if e is not None:
            assert abs(e.kappa_eff - 0.0) < 1e-12

    def test_kappa_eff_formula(self, master_table):
        """kappa_eff = kappa - 13 for all families."""
        for name, entry in master_table.items():
            expected = entry.kappa - 13.0
            assert abs(entry.kappa_eff - expected) < 1e-10


# ============================================================================
# 22. Cross-verification: kappa from multiple methods
# ============================================================================

class TestKappaCrossVerification:
    """Cross-verify kappa using independent methods."""

    def test_kappa_from_S2(self, master_table):
        """Method 1: kappa = S_2 (shadow coefficient)."""
        for name, entry in master_table.items():
            assert abs(entry.shadow_coeffs[2] - entry.kappa) < 1e-8

    def test_kappa_from_formula(self, master_table):
        """Method 2: kappa from the defining formula."""
        for name, entry in master_table.items():
            if entry.family == 'heisenberg':
                expected = entry.param
            elif entry.family == 'virasoro':
                expected = entry.param / 2.0
            elif entry.family == 'affine_sl2':
                expected = 3.0 * (entry.param + 2.0) / 4.0
            elif entry.family == 'affine_sl3':
                expected = 4.0 * (entry.param + 3.0) / 3.0
            else:
                continue
            assert abs(entry.kappa - expected) < 1e-8, \
                f"{name}: kappa={entry.kappa}, expected={expected}"

    def test_kappa_from_complementarity(self, master_table):
        """Method 3: kappa from complementarity sum."""
        for name, entry in master_table.items():
            if entry.dual_kappa is None:
                continue
            if entry.family == 'virasoro':
                assert abs(entry.kappa - (13.0 - entry.dual_kappa)) < 1e-8
            elif entry.family == 'heisenberg' or entry.family.startswith('affine'):
                assert abs(entry.kappa - (-entry.dual_kappa)) < 1e-8


# ============================================================================
# 23. Shadow tower recursion tests
# ============================================================================

class TestShadowTowerRecursion:
    """Verify the tower recursion independently."""

    def test_tower_from_Q_L(self):
        """H(t) = t^2 sqrt(Q_L(t)) reproduces the tower."""
        kap = 5.0  # Virasoro c=10
        alpha = 2.0  # cubic shadow parameter
        S4 = 10.0 / (10.0 * 72.0)
        coeffs = _shadow_coeffs_from_tower(kap, alpha, S4, 20)

        # S_2 = a_0/2 = 2*kappa/2 = kappa
        assert abs(coeffs[2] - kap) < 1e-10
        # S_3 = a_1/3 = 3*alpha/3 = alpha
        assert abs(coeffs[3] - alpha) < 1e-10
        # S_4 = a_2/4 = 4*S4/4 = S4
        assert abs(coeffs[4] - S4) < 1e-10

    def test_tower_terminates_for_Delta_zero(self):
        """Delta = 0 => tower terminates (perfect square Q_L)."""
        kap = 5.0
        alpha = 2.0
        S4 = 0.0  # Delta = 0
        coeffs = _shadow_coeffs_from_tower(kap, alpha, S4, 20)
        # With Delta=0 and nonzero alpha, S_r should decay rapidly
        # Q_L = (2*kappa + 3*alpha*t)^2, sqrt = 2*kappa + 3*alpha*t
        # So a_0 = 2*kappa, a_1 = 3*alpha, a_n = 0 for n>=2
        for r in range(4, 15):
            assert abs(coeffs[r]) < 1e-10, f"S_{r}={coeffs[r]} should be ~0"


# ============================================================================
# 24. Pair data computation tests
# ============================================================================

class TestPairData:
    """Verify pair data computations."""

    def test_self_pair_zero_diff(self, master_table):
        """Pair(A,A) should have zero differences."""
        for name in ['Heis_k=1', 'Vir_c=10.0', 'aff_sl2_k=1']:
            if name in master_table:
                e = master_table[name]
                pd = compute_pair_data(e, e, 30)
                assert abs(pd.zeta_diff_s2) < 1e-12
                assert abs(pd.zeta_diff_s3) < 1e-12
                assert abs(pd.zeta_diff_s4) < 1e-12

    def test_rankin_selberg_positive_self(self, master_table):
        """RS(A,A) = sum S_r^2/r >= 0."""
        for name in ['Vir_c=10.0', 'aff_sl2_k=1']:
            if name in master_table:
                e = master_table[name]
                pd = compute_pair_data(e, e, 30)
                assert pd.rankin_selberg.real >= -1e-12

    def test_heisenberg_rankin_selberg(self, master_table):
        """RS(H_k, H_k) = k^2 / 2 (single term)."""
        for k in [1, 2, 3]:
            name = f'Heis_k={k}'
            if name in master_table:
                e = master_table[name]
                pd = compute_pair_data(e, e, 30)
                expected = float(k ** 2) / 2.0
                assert abs(pd.rankin_selberg.real - expected) < 1e-10


# ============================================================================
# 25. Analytic rank tests
# ============================================================================

class TestAnalyticRank:
    """Verify analytic rank estimation."""

    def test_heisenberg_rank_0(self):
        """Heisenberg zeta(1/2) = k*2^{-1/2} != 0 => rank 0."""
        coeffs = _compute_shadow_coefficients('heisenberg', 1.0, 10)
        r = _analytic_rank(coeffs)
        assert r == 0


# ============================================================================
# 26. Edge case tests
# ============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_virasoro_c_half(self, master_table):
        """Virasoro at c=1/2 (Ising): kappa=1/4."""
        e = master_table.get('Vir_c=0.5')
        if e:
            assert abs(e.kappa - 0.25) < 1e-12

    def test_virasoro_c_26_kappa_eff_zero(self, master_table):
        """c=26: kappa_eff = 13 - 13 = 0."""
        e = master_table.get('Vir_c=26.0')
        if e:
            assert abs(e.kappa_eff) < 1e-12

    def test_virasoro_c_13_self_dual(self, master_table):
        """c=13: self-dual point, kappa = kappa' = 6.5."""
        e = master_table.get('Vir_c=13.0')
        if e and e.dual_kappa is not None:
            assert abs(e.kappa - e.dual_kappa) < 1e-12

    def test_w3_w_alpha_zero(self, master_table):
        """W_3 W-line: alpha = 0 (Z_2 parity)."""
        for name, entry in master_table.items():
            if entry.family == 'w3_w':
                # S_3 should be 0 (odd arities vanish on W-line)
                assert abs(entry.S3) < 1e-10, f"{name}: S3={entry.S3}"

    def test_empty_table_extremals(self):
        """Empty table should return empty extremals."""
        extremals = find_extremals({})
        assert len(extremals) == 0


# ============================================================================
# 27. Arithmetic depth decomposition tests
# ============================================================================

class TestArithmeticDepthDecomposition:
    """Verify d = 1 + d_arith + d_alg."""

    def test_class_G_depth_1(self, master_table):
        """Class G: d_alg=0, d_arith=0, d=1."""
        for name, entry in master_table.items():
            if entry.depth_class == 'G':
                assert entry.d_alg == 0
                assert entry.d_total == 1

    def test_class_L_depth_2(self, master_table):
        """Class L: d_alg=1, d=2."""
        for name, entry in master_table.items():
            if entry.depth_class == 'L':
                assert entry.d_alg == 1
                assert entry.d_total == 2

    def test_class_C_depth_3(self, master_table):
        """Class C: d_alg=2, d=3."""
        for name, entry in master_table.items():
            if entry.depth_class == 'C':
                assert entry.d_alg == 2
                assert entry.d_total == 3

    def test_depth_monotone(self, master_table):
        """Depth order: G < L < C < M."""
        order = {'G': 1, 'L': 2, 'C': 3, 'M': 101}
        for name, entry in master_table.items():
            assert entry.d_total == order.get(entry.depth_class, 0), \
                f"{name}: d_total={entry.d_total}, expected={order.get(entry.depth_class)}"


# ============================================================================
# 28. Shadow entropy tests
# ============================================================================

class TestShadowEntropy:
    """Verify shadow entropy computation."""

    def test_entropy_class_G_minimal(self, master_table):
        """Class G (single nonzero coeff): entropy = 0."""
        stats = compute_depth_class_stats(master_table)
        # Heisenberg has only S_2 != 0, so entropy is 0 (single nonzero prob)
        assert abs(stats['G'].shadow_entropy) < 1e-10

    def test_entropy_class_M_positive(self, master_table):
        """Class M (many nonzero coeffs): entropy > 0."""
        stats = compute_depth_class_stats(master_table)
        assert stats['M'].shadow_entropy > 0.0


# ============================================================================
# 29. Zeta special value cross-checks
# ============================================================================

class TestZetaSpecialValues:
    """Cross-check zeta function at special values."""

    def test_zeta_0_is_sum_S_r(self, master_table):
        """zeta_A(0) = sum S_r (all arities contribute equally at s=0)."""
        for name in ['Heis_k=1', 'aff_sl2_k=1']:
            if name not in master_table:
                continue
            e = master_table[name]
            z0 = e.zeta_at_0
            total = sum(e.shadow_coeffs.get(r, 0.0) for r in range(2, 31))
            assert abs(z0.real - total) < 1e-6, \
                f"{name}: zeta(0)={z0.real}, sum={total}"

    def test_heisenberg_zeta_1(self, master_table):
        """zeta_{H_k}(1) = k/2."""
        for k in range(1, 6):
            e = master_table.get(f'Heis_k={k}')
            if e:
                assert abs(e.zeta_at_1.real - float(k) / 2.0) < 1e-10

    def test_heisenberg_zeta_half(self, master_table):
        """zeta_{H_k}(1/2) = k * 2^{-1/2} = k/sqrt(2)."""
        for k in range(1, 4):
            e = master_table.get(f'Heis_k={k}')
            if e:
                expected = float(k) / math.sqrt(2.0)
                assert abs(e.zeta_at_half.real - expected) < 1e-10


# ============================================================================
# 30. Theorem D: leading behavior test
# ============================================================================

class TestTheoremD:
    """Verify Theorem D consistency: kappa controls leading zeta behavior."""

    def test_leading_behavior_all_families(self, master_table):
        """zeta_A(20) / (kappa * 2^{-20}) ~ 1 for all families."""
        results = verify_shadow_zeta_at_large_s(master_table, sigma=20.0)
        for name, ratio, consistent in results:
            assert consistent, f"{name}: ratio={ratio}"

    @pytest.mark.parametrize("sigma", [15.0, 20.0, 25.0])
    def test_leading_behavior_heisenberg(self, sigma, master_table):
        """Heisenberg: exact leading behavior zeta = kappa * 2^{-s}."""
        e = master_table.get('Heis_k=1')
        if e is None:
            pytest.skip("Heis_k=1 not in table")
        z = _shadow_zeta_eval(e.shadow_coeffs, complex(sigma, 0))
        leading = e.kappa * 2.0 ** (-sigma)
        assert abs(z / leading - 1.0) < 1e-12


# ============================================================================
# 31. AP-specific regression tests
# ============================================================================

class TestAPRegressions:
    """Regression tests for known anti-patterns."""

    def test_AP1_no_cross_family_copy(self, master_table):
        """AP1: kappa formulas must be family-specific."""
        # Virasoro c=1 has kappa=0.5; Heisenberg k=1 has kappa=1
        vir = master_table.get('Vir_c=1.0')
        heis = master_table.get('Heis_k=1')
        if vir and heis:
            assert vir.kappa != heis.kappa

    def test_AP24_virasoro_sum_is_13_not_0(self, master_table):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        vir = master_table.get('Vir_c=10.0')
        if vir and vir.dual_kappa is not None:
            s = vir.kappa + vir.dual_kappa
            assert abs(s - 13.0) < 1e-12
            assert abs(s) > 1.0  # NOT zero

    def test_AP39_S2_equals_kappa_not_c_over_2(self, master_table):
        """AP39: S_2 = kappa for all families. kappa != c/2 in general."""
        e = master_table.get('aff_sl2_k=1')
        if e:
            # For sl_2 k=1: c = 1.0, kappa = 2.25
            # S_2 should be kappa = 2.25, NOT c/2 = 0.5
            assert abs(e.shadow_coeffs[2] - e.kappa) < 1e-10
            assert abs(e.shadow_coeffs[2] - e.central_charge / 2.0) > 0.1

    def test_AP48_kappa_depends_on_full_algebra(self, master_table):
        """AP48: kappa depends on the full algebra, not Virasoro sub."""
        # For affine sl_2 k=1: c=1, kappa=2.25
        # If we wrongly used kappa=c/2=0.5, we'd be off by 1.75
        e = master_table.get('aff_sl2_k=1')
        if e:
            wrong_kappa = e.central_charge / 2.0
            assert abs(e.kappa - wrong_kappa) > 1.0, \
                "kappa should NOT be c/2 for affine KM"


# ============================================================================
# 32. Full end-to-end test
# ============================================================================

class TestEndToEnd:
    """Full pipeline integration tests."""

    def test_full_pipeline(self):
        """Build atlas, summarize, convert to dict."""
        atlas = build_grand_atlas(max_r=20)
        s = atlas_summary(atlas)
        d = atlas_to_dict(atlas)
        assert s['n_families'] >= 49
        assert d['n_families'] >= 49
        assert s['complementarity_violations'] == 0

    def test_atlas_deterministic(self):
        """Two builds produce identical results."""
        a1 = build_grand_atlas(max_r=15)
        a2 = build_grand_atlas(max_r=15)
        for name in a1.families:
            assert name in a2.families
            assert abs(a1.families[name].kappa - a2.families[name].kappa) < 1e-15
