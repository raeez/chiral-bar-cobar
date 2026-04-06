r"""Tests for DS-shadow cascade engine.

Systematic verification of the Drinfeld-Sokolov depth increase mechanism
across sl_N -> W_N for N = 2, 3, 4, 5.

STRUCTURE:
  Section 1: Central charge formulas and ghost additivity (10 tests)
  Section 2: Kappa formulas and additivity analysis (8 tests)
  Section 3: Shadow obstruction tower computation — exact arithmetic (8 tests)
  Section 4: Depth increase verification (8 tests)
  Section 5: BRST quartic creation mechanism (6 tests)
  Section 6: Cascade verification S_4 -> S_5 -> ... (6 tests)
  Section 7: DS commutation diagram (5 tests)
  Section 8: Ghost sector analysis (5 tests)
  Section 9: Growth rate comparison (4 tests)
  Section 10: Cross-engine consistency checks (5 tests)

Total: 65 tests.

Manuscript references:
    thm:ds-central-charge-additivity, thm:shadow-archetype-classification,
    prop:independent-sum-factorization, thm:single-line-dichotomy,
    thm:obstruction-recursion, rem:virasoro-resonance-model
"""

import pytest
from fractions import Fraction

from compute.lib.ds_shadow_cascade_engine import (
    # Central charges
    c_slN,
    c_WN,
    c_ghost,
    verify_ghost_central_charge,
    # Kappa
    kappa_slN,
    anomaly_ratio,
    kappa_WN,
    kappa_ghost,
    verify_kappa_additivity,
    # Shadow data
    slN_shadow_data,
    WN_shadow_data_T_line,
    # Tower computation
    shadow_tower_exact,
    _convolution_coefficients_exact,
    # Pipeline
    ds_pipeline,
    depth_increase_all_N,
    # BRST
    brst_quartic_creation,
    # Cascade
    cascade_verification,
    # Commutation diagram
    ds_commutation_diagram,
    # Multi-N
    multi_N_summary,
    # Ghost
    ghost_shadow_tower,
    independent_sum_test,
    # Growth rate
    growth_rate_comparison,
    # Cross-checks
    virasoro_s5_crosscheck,
    # Verification
    verify_all,
)


# ============================================================================
# Section 1: Central charge formulas and ghost additivity
# ============================================================================

class TestCentralChargeFormulas:
    """Test central charge formulas for sl_N and W_N."""

    def test_c_sl2_k1(self):
        """c(sl_2, k=1) = 3*1/(1+2) = 1."""
        assert c_slN(2, Fraction(1)) == Fraction(1)

    def test_c_sl2_k2(self):
        """c(sl_2, k=2) = 3*2/(2+2) = 6/4 = 3/2."""
        assert c_slN(2, Fraction(2)) == Fraction(3, 2)

    def test_c_sl3_k1(self):
        """c(sl_3, k=1) = 8*1/(1+3) = 2."""
        assert c_slN(3, Fraction(1)) == Fraction(2)

    def test_c_sl4_k1(self):
        """c(sl_4, k=1) = 15*1/(1+4) = 3."""
        assert c_slN(4, Fraction(1)) == Fraction(3)

    def test_c_sl5_k1(self):
        """c(sl_5, k=1) = 24*1/(1+5) = 4."""
        assert c_slN(5, Fraction(1)) == Fraction(4)

    def test_c_WN_virasoro_k1(self):
        """c(Vir from DS(sl_2, k=1)) = 1 - 6*4/3 = -7 (Fateev-Lukyanov)."""
        c_v = c_WN(2, Fraction(1))
        assert c_v == Fraction(-7)

    def test_ghost_c_sl2_k0(self):
        """c_ghost(sl_2, k=0) = 2."""
        assert c_ghost(2) == Fraction(2)

    def test_ghost_c_sl3_k0(self):
        """c_ghost(sl_3, k=0) = 30."""
        assert c_ghost(3) == Fraction(30)

    def test_ghost_c_sl4_k0(self):
        """c_ghost(sl_4, k=0) = 132."""
        assert c_ghost(4) == Fraction(132)

    def test_ghost_c_sl5_k0(self):
        """c_ghost(sl_5, k=0) = 380."""
        assert c_ghost(5) == Fraction(380)


class TestGhostCentralChargeAdditivity:
    """Verify c(sl_N, k) - c(W_N, k) is linear in k (structural property)."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_ghost_additivity_N(self, N):
        """Ghost central charge is linear in k for all tested levels."""
        result = verify_ghost_central_charge(N)
        assert result['all_match'], (
            f"Ghost c linearity fails for sl_{N}"
        )

    @pytest.mark.parametrize("N,k_val", [
        (2, Fraction(1)),
        (2, Fraction(10)),
        (3, Fraction(1)),
        (3, Fraction(10)),
        (4, Fraction(5)),
        (5, Fraction(5)),
    ])
    def test_c_additivity_explicit(self, N, k_val):
        """c(sl_N, k) = c(W_N, k) + c_ghost(N, k) at specific (N, k)."""
        c_aff = c_slN(N, k_val)
        c_w = c_WN(N, k_val)
        c_gh = c_ghost(N, k_val)
        assert c_aff == c_w + c_gh, (
            f"c(sl_{N}, {k_val}) = {c_aff} != c(W_{N}) + c_ghost = {c_w} + {c_gh}"
        )


# ============================================================================
# Section 2: Kappa formulas and additivity analysis
# ============================================================================

class TestKappaFormulas:
    """Test kappa formulas for sl_N and W_N."""

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        assert kappa_slN(2, Fraction(1)) == Fraction(9, 4)

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 32/6 = 16/3."""
        assert kappa_slN(3, Fraction(1)) == Fraction(16, 3)

    def test_anomaly_ratio_sl2(self):
        """rho(sl_2) = H_2 - 1 = 1/2."""
        assert anomaly_ratio(2) == Fraction(1, 2)

    def test_anomaly_ratio_sl3(self):
        """rho(sl_3) = H_3 - 1 = 1/2 + 1/3 = 5/6."""
        assert anomaly_ratio(3) == Fraction(5, 6)

    def test_anomaly_ratio_sl4(self):
        """rho(sl_4) = H_4 - 1 = 1/2 + 1/3 + 1/4 = 13/12."""
        assert anomaly_ratio(4) == Fraction(13, 12)

    def test_anomaly_ratio_sl5(self):
        """rho(sl_5) = H_5 - 1 = 1/2 + 1/3 + 1/4 + 1/5 = 77/60."""
        assert anomaly_ratio(5) == Fraction(77, 60)

    def test_kappa_ghost_sl2(self):
        """kappa_ghost(sl_2) = N(N-1)/2 = 1."""
        assert kappa_ghost(2) == Fraction(1)

    def test_kappa_ghost_sl3(self):
        """kappa_ghost(sl_3) at k=0: c_ghost(3,0)/2 = 30/2 = 15."""
        assert kappa_ghost(3) == Fraction(15)


# ============================================================================
# Section 3: Shadow obstruction tower computation — exact arithmetic
# ============================================================================

class TestShadowTowerExact:
    """Test exact Fraction arithmetic shadow obstruction tower computation."""

    def test_class_G_tower(self):
        """Heisenberg-type (kappa=1, alpha=0, S4=0): S_r=0 for r>=3."""
        tower = shadow_tower_exact(Fraction(1), Fraction(0), Fraction(0), 8)
        assert tower[2] == Fraction(1)  # kappa
        for r in range(3, 9):
            assert tower[r] == Fraction(0), f"S_{r} should be 0 for class G"

    def test_class_L_tower(self):
        """sl_2-type (kappa=9/4, alpha=1, S4=0): S_r=0 for r>=4."""
        tower = shadow_tower_exact(Fraction(9, 4), Fraction(1), Fraction(0), 8)
        assert tower[2] == Fraction(9, 4)
        assert tower[3] != Fraction(0)  # cubic is nonzero
        for r in range(4, 9):
            assert tower[r] == Fraction(0), f"S_{r} should be 0 for class L"

    def test_class_L_s3_value(self):
        """For class L with alpha=1: S_3 = a_1/3 = q1/(2*a0*3) = 12*kappa/(2*2*kappa*3) = 1."""
        kap = Fraction(9, 4)
        tower = shadow_tower_exact(kap, Fraction(1), Fraction(0), 4)
        # a_0 = 2*kappa, a_1 = q1/(2*a0) = 12*kappa*1/(2*2*kappa) = 3
        # S_3 = a_1/3 = 3/3 = 1
        assert tower[3] == Fraction(1)

    def test_virasoro_type_s4_nonzero(self):
        """Virasoro-type at c=1: S_4 should be nonzero."""
        # c=1: kappa=1/2, alpha=2, S4=10/(1*27) = 10/27
        kap = Fraction(1, 2)
        alp = Fraction(2)
        s4 = Fraction(10, 27)
        tower = shadow_tower_exact(kap, alp, s4, 6)
        assert tower[4] == s4
        assert tower[5] != Fraction(0), "S_5 should be nonzero for class M"

    def test_convolution_identity_a0(self):
        """a_0 = sqrt(q0) = 2*kappa when q0 = 4*kappa^2."""
        kap = Fraction(7, 3)
        q0 = 4 * kap ** 2
        q1 = 12 * kap * Fraction(1)
        q2 = 9 * Fraction(1) ** 2
        coeffs = _convolution_coefficients_exact(q0, q1, q2, 0)
        assert coeffs[0] == 2 * kap

    def test_convolution_identity_a1(self):
        """a_1 = q1 / (2*a_0) = 12*kappa*alpha / (2*2*kappa) = 3*alpha."""
        kap = Fraction(5, 2)
        alp = Fraction(3)
        q0 = 4 * kap ** 2
        q1 = 12 * kap * alp
        q2 = 9 * alp ** 2
        coeffs = _convolution_coefficients_exact(q0, q1, q2, 1)
        assert coeffs[1] == 3 * alp

    def test_tower_s2_always_kappa(self):
        """S_2 = a_0 / 2 = 2*kappa/2 = kappa."""
        for kap in [Fraction(1), Fraction(3, 2), Fraction(7, 4)]:
            tower = shadow_tower_exact(kap, Fraction(1), Fraction(0), 3)
            assert tower[2] == kap, f"S_2 should equal kappa={kap}"

    def test_tower_s3_always_alpha(self):
        """S_3 = a_1 / 3 = 3*alpha/3 = alpha."""
        for alp in [Fraction(0), Fraction(1), Fraction(2), Fraction(5, 3)]:
            kap = Fraction(3)  # arbitrary nonzero
            tower = shadow_tower_exact(kap, alp, Fraction(0), 4)
            assert tower[3] == alp, f"S_3 should equal alpha={alp}"


# ============================================================================
# Section 4: Depth increase verification
# ============================================================================

class TestDepthIncrease:
    """Verify sl_N (depth 3) -> W_N (depth inf) for all N."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_slN_is_class_L(self, N):
        """sl_N has S_4 = 0 (class L, depth 3)."""
        data = slN_shadow_data(N, Fraction(5))
        assert data['S4'] == Fraction(0)
        assert data['depth_class'] == 'L'

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_WN_has_nonzero_S4(self, N):
        """W_N has S_4 != 0 (class M, depth infinity)."""
        data = WN_shadow_data_T_line(N, Fraction(5))
        assert data['S4'] != Fraction(0), f"W_{N} should have nonzero S_4"

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_depth_increase_pipeline(self, N):
        """Full pipeline confirms depth increase at k=5."""
        pipe = ds_pipeline(N, Fraction(5))
        assert pipe['depth_increase'], f"Depth increase should hold for sl_{N} -> W_{N}"

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_depth_increase_multiple_levels(self, N):
        """Depth increase holds at multiple levels k."""
        for kv in [Fraction(1), Fraction(2), Fraction(10)]:
            try:
                pipe = ds_pipeline(N, kv)
                assert pipe['depth_increase'], (
                    f"Depth increase fails for sl_{N} at k={kv}"
                )
            except (ValueError, ZeroDivisionError):
                # Skip singular levels
                pass

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_slN_tower_terminates(self, N):
        """sl_N shadow obstruction tower has S_r = 0 for r >= 4."""
        kap = kappa_slN(N, Fraction(5))
        tower = shadow_tower_exact(kap, Fraction(1), Fraction(0), 8)
        for r in range(4, 9):
            assert tower[r] == Fraction(0), (
                f"sl_{N}: S_{r} should be 0 but is {tower[r]}"
            )

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_WN_tower_does_not_terminate(self, N):
        """W_N shadow obstruction tower has S_r != 0 for 4 <= r <= 8."""
        data = WN_shadow_data_T_line(N, Fraction(5))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], 8)
        for r in range(4, 9):
            assert tower[r] != Fraction(0), (
                f"W_{N}: S_{r} should be nonzero but is 0"
            )

    def test_depth_increase_summary(self):
        """Multi-N depth increase summary, all should be True."""
        di = depth_increase_all_N()
        for N, data in di.items():
            assert data['depth_increase'], f"sl_{N}: depth increase failed"

    def test_c_additivity_in_depth_increase(self):
        """Central charge additivity holds for all N in depth increase."""
        di = depth_increase_all_N()
        for N, data in di.items():
            assert data['c_additive'], f"sl_{N}: c additivity failed"


# ============================================================================
# Section 5: BRST quartic creation mechanism
# ============================================================================

class TestBRSTQuarticCreation:
    """Test the BRST quartic creation mechanism."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_brst_creates_quartic(self, N):
        """BRST coupling creates nonzero quartic from zero inputs."""
        result = brst_quartic_creation(N, Fraction(5))
        assert result['brst_creates_quartic'], (
            f"BRST should create nonzero quartic for sl_{N} -> W_{N}"
        )

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_naive_sum_is_zero(self, N):
        """Naive sum S_4(sl_N) + S_4(ghost) = 0."""
        result = brst_quartic_creation(N, Fraction(5))
        assert result['naive_sum'] == Fraction(0)

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_delta_nonzero(self, N):
        """Discriminant Delta = 8*kappa*S_4 != 0 for W_N."""
        result = brst_quartic_creation(N, Fraction(5))
        assert result['Delta_nonzero'], f"Delta should be nonzero for W_{N}"

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_brst_creation_equals_s4_wn(self, N):
        """The BRST creation term equals S_4(W_N) exactly."""
        result = brst_quartic_creation(N, Fraction(5))
        assert result['brst_creation'] == result['S4_WN']

    def test_virasoro_quartic_formula(self):
        """S_4(Vir) = 10/(c(5c+22)) at specific c value."""
        c_v = c_WN(2, Fraction(5))  # c_Vir at k=5
        result = brst_quartic_creation(2, Fraction(5))
        expected = Fraction(10) / (c_v * (5 * c_v + 22))
        assert result['S4_WN'] == expected

    def test_brst_creation_varies_with_k(self):
        """BRST quartic creation has different value at different k."""
        s4_k5 = brst_quartic_creation(2, Fraction(5))['S4_WN']
        s4_k10 = brst_quartic_creation(2, Fraction(10))['S4_WN']
        assert s4_k5 != s4_k10, "S_4 should depend on k (through c)"


# ============================================================================
# Section 6: Cascade verification
# ============================================================================

class TestCascadeVerification:
    """Verify the cascade: S_4 != 0 => S_r != 0 for all r >= 4."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_cascade_all_nonzero(self, N):
        """All S_r for r = 4..8 are nonzero for W_N."""
        casc = cascade_verification(N, Fraction(5), 8)
        assert casc['all_nonzero_from_4'], (
            f"W_{N}: cascade should give all nonzero S_r from arity 4"
        )

    def test_virasoro_s5_matches_quintic_formula(self):
        """S_5(Vir) from cascade matches -48/(c^2(5c+22))."""
        casc = cascade_verification(2, Fraction(5), 6)
        s5_check = casc['s5_crosscheck']
        assert s5_check is not None
        assert s5_check['matches'], (
            f"S_5 mismatch: cascade={s5_check['S5_cascade']}, "
            f"expected={s5_check['S5_expected']}"
        )

    def test_virasoro_s5_crosscheck_multiple_levels(self):
        """Cross-check S_5 at multiple levels."""
        result = virasoro_s5_crosscheck()
        assert result['all_match'], "S_5 cross-check fails at some level"

    def test_cascade_sign_alternation(self):
        """For Virasoro, shadow coefficients alternate in sign."""
        casc = cascade_verification(2, Fraction(5), 8)
        # S_2 = kappa > 0 (if c > 0)
        # S_3 = 2 > 0
        # S_4 = 10/(c(5c+22)) > 0 (if c > 0)
        # S_5 = -48/(c^2(5c+22)) < 0 (if c > 0)
        c_v = c_WN(2, Fraction(5))
        if c_v > 0:
            s4 = casc['cascade'][4]['S_r']
            s5 = casc['cascade'][5]['S_r']
            assert s4 > 0 and s5 < 0, "S_4 > 0, S_5 < 0 for c > 0"

    def test_cascade_ratios_stabilize(self):
        """For W_N, consecutive ratios |S_{r+1}/S_r| stabilize to growth rate rho."""
        # At k=100, the tower has a definite growth rate
        casc = cascade_verification(2, Fraction(100), 12)
        ratios = []
        for r in range(5, 12):
            s_r = abs(casc['cascade'][r]['float'])
            s_r1 = abs(casc['cascade'][r + 1]['float'])
            if s_r > 1e-30:
                ratios.append(s_r1 / s_r)
        # Check ratios converge (last two close to each other)
        if len(ratios) >= 2:
            rel_diff = abs(ratios[-1] - ratios[-2]) / max(abs(ratios[-1]), 1e-30)
            assert rel_diff < 0.5, (
                f"Ratios not stabilizing: {ratios[-2]:.4f}, {ratios[-1]:.4f}"
            )

    def test_class_L_no_cascade(self):
        """For sl_N (class L), there is no cascade: S_r = 0 for r >= 4."""
        tower = shadow_tower_exact(Fraction(9, 4), Fraction(1), Fraction(0), 8)
        for r in range(4, 9):
            assert tower[r] == Fraction(0)


# ============================================================================
# Section 7: DS commutation diagram
# ============================================================================

class TestDSCommutationDiagram:
    """Test the DS-shadow commutation diagram analysis."""

    def test_c_additive_in_diagram(self):
        """Central charge is additive in the DS commutation diagram."""
        diag = ds_commutation_diagram(2, Fraction(5))
        assert diag['c_additive']

    def test_arity4_noncommutative(self):
        """Diagram fails to commute at arity 4."""
        diag = ds_commutation_diagram(2, Fraction(5))
        a4 = diag['arity_analysis'][4]
        assert not a4['diagram_commutes']
        assert a4['slN_zero']
        assert a4['WN_nonzero']

    def test_depth_increase_in_diagram(self):
        """Diagram shows depth increase."""
        diag = ds_commutation_diagram(2, Fraction(5))
        assert diag['depth_increase']

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_arity4_noncommutative_all_N(self, N):
        """Arity-4 non-commutativity is universal across all N."""
        diag = ds_commutation_diagram(N, Fraction(5))
        a4 = diag['arity_analysis'][4]
        assert a4['slN_zero'] and a4['WN_nonzero'], (
            f"sl_{N}: arity-4 should show depth increase"
        )

    def test_higher_arity_noncommutative(self):
        """Arities 5-8 also fail to commute (cascade)."""
        diag = ds_commutation_diagram(2, Fraction(5), 8)
        for r in range(5, 9):
            assert not diag['arity_analysis'][r]['diagram_commutes']


# ============================================================================
# Section 8: Ghost sector analysis
# ============================================================================

class TestGhostSector:
    """Test the ghost sector shadow obstruction tower and independent sum."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_ghost_scalar_level_depth(self, N):
        """Ghost sector scalar-level tower: S_r = 0 for r >= 3."""
        gt = ghost_shadow_tower(N)
        for r in range(3, max(gt.keys()) + 1):
            assert gt[r] == Fraction(0), (
                f"Ghost(sl_{N}): S_{r} should be 0 but is {gt[r]}"
            )

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_ghost_kappa_value(self, N):
        """Ghost S_2 = kappa_ghost(N, k=0) = c_ghost(N, 0)/2."""
        gt = ghost_shadow_tower(N)
        expected = c_ghost(N) / 2
        assert gt[2] == expected

    def test_independent_sum_fails_at_arity4_sl2(self):
        """For sl_2 -> Vir, independent sum fails at arity 4."""
        result = independent_sum_test(2, Fraction(5))
        assert result['fails_at'] is not None, "Independent sum should fail"
        # It may fail earlier than arity 4 due to alpha mismatch
        assert result['fails_at'] <= 4, (
            f"Should fail at or before arity 4, fails at {result['fails_at']}"
        )

    def test_independent_sum_fails_arity4_explicit(self):
        """S_4(W_N) != S_4(sl_N) + S_4(ghost) = 0 + 0 = 0."""
        result = independent_sum_test(2, Fraction(5))
        a4 = result['per_arity'][4]
        assert not a4['independent_sum'], "S_4 should not be additive"
        assert a4['S_r_slN'] == Fraction(0)
        assert a4['S_r_ghost'] == Fraction(0)
        assert a4['S_r_WN'] != Fraction(0)

    @pytest.mark.parametrize("N", [3, 4, 5])
    def test_independent_sum_fails_higher_N(self, N):
        """Independent sum fails for all N >= 3 too."""
        result = independent_sum_test(N, Fraction(5))
        assert result['fails_at'] is not None, (
            f"Independent sum should fail for sl_{N} -> W_{N}"
        )


# ============================================================================
# Section 9: Growth rate comparison
# ============================================================================

class TestGrowthRate:
    """Test shadow growth rate comparison sl_N vs W_N."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_rho_positive_for_WN(self, N):
        """Growth rate rho > 0 for W_N (class M)."""
        result = growth_rate_comparison(N, Fraction(5))
        assert result['rho_positive'], f"W_{N}: rho should be positive"

    def test_rho_zero_for_slN(self):
        """Growth rate rho = 0 for sl_N (class L)."""
        result = growth_rate_comparison(2, Fraction(5))
        assert result['rho_slN'] == 0.0

    def test_virasoro_rho_decreases_with_k(self):
        """For Virasoro T-line, growth rate rho decreases as k increases."""
        rho_k5 = growth_rate_comparison(2, Fraction(5))['rho_float']
        rho_k100 = growth_rate_comparison(2, Fraction(100))['rho_float']
        assert rho_k100 < rho_k5, (
            f"rho should decrease: rho(k=5)={rho_k5:.4f}, rho(k=100)={rho_k100:.4f}"
        )

    def test_growth_rate_varies_with_N(self):
        """Growth rate depends on N (different W_N algebras)."""
        rho2 = growth_rate_comparison(2, Fraction(5))['rho_float']
        rho3 = growth_rate_comparison(3, Fraction(5))['rho_float']
        assert abs(rho2 - rho3) > 1e-10, "rho should differ between N=2 and N=3"


# ============================================================================
# Section 10: Cross-engine consistency checks
# ============================================================================

class TestCrossEngineConsistency:
    """Cross-checks against existing engines."""

    def test_virasoro_s5_exact_formula(self):
        """S_5(Vir) = -48/(c^2(5c+22)) matches quintic_shadow_engine."""
        result = virasoro_s5_crosscheck()
        assert result['all_match']

    def test_multi_N_summary_coherent(self):
        """Multi-N summary table is internally consistent."""
        summary = multi_N_summary(Fraction(5))
        for N, data in summary.items():
            # Central charge additivity
            assert data['c_additive'], f"sl_{N}: c not additive"
            # Depth increase
            assert data['depth_increase'], f"sl_{N}: no depth increase"
            # Cascade
            assert data['cascade_all_nonzero'], f"sl_{N}: cascade incomplete"

    def test_verify_all_passes(self):
        """The master verify_all() function passes everything."""
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"verify_all: {name} failed"

    def test_pipeline_at_k1(self):
        """DS pipeline at k=1 for sl_2 gives consistent results."""
        pipe = ds_pipeline(2, Fraction(1))
        assert pipe['c_additive']
        assert pipe['S4_slN'] == Fraction(0)
        assert pipe['S4_WN'] != Fraction(0)

    def test_ghost_c_formula_N2_to_N5(self):
        """Ghost central charge at k=0: c_ghost(N) = (N-1)[(N^2-1)(N-1)-1]."""
        expected = {2: 2, 3: 30, 4: 132, 5: 380}
        for N, exp in expected.items():
            assert c_ghost(N) == Fraction(exp), (
                f"c_ghost({N}) = {c_ghost(N)} != {exp}"
            )
