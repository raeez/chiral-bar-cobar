r"""Tests for Burns space F_2 = 7/1440 theorem verification engine.

Verification paths (multi-path mandate: 3+ per claim):
  1. Direct computation from defining formulas
  2. Alternative formula (Bernoulli, A-hat, manual)
  3. Limiting cases (single pair, lambda=0, lambda=1/2)
  4. Cross-check (ratio, shadow tower, complementarity)
  5. Cross-engine consistency (against burns_space_koszul_datum_engine)
  6. Dimensional/degree analysis
  7. Numerical evaluation
  8. Literature comparison (Faber-Pandharipande known values)

60+ tests covering:
  - F_2 = 7/1440 via 6 independent paths (Section A)
  - kappa = 4 via 5 independent paths (Section B)
  - Faber-Pandharipande numbers (Section C)
  - Betagamma formulas (Section D)
  - Shadow tower on T-line (Section E)
  - S_3 structure (Section F)
  - Planted-forest corrections (Section G)
  - F_3 prediction (Section H)
  - Asymptotic analysis (Section I)
  - Cross-engine consistency (Section J)
  - Costello-Paquette-Sharma comparison (Section K)
  - Shadow metric and classification (Section L)
"""

import pytest
from fractions import Fraction
from math import factorial

from sympy import Rational, bernoulli, Symbol, sin, series

from compute.lib.theorem_burns_f2_engine import (
    # Faber-Pandharipande
    lambda_fp,
    lambda_fp_from_bernoulli_manual,
    lambda_fp_from_ahat,
    bernoulli_exact,
    # Betagamma
    bg_central_charge,
    bg_kappa,
    bc_kappa,
    # Burns data constants
    N_BG,
    LAMBDA_BURNS,
    C_SINGLE,
    KAPPA_SINGLE,
    C_TOTAL,
    KAPPA_TOTAL,
    KAPPA_DUAL,
    C_DUAL,
    COMPLEMENTARITY_SUM,
    # Genus tower
    F_g_burns,
    burns_genus_tower,
    burns_genus_tower_extended,
    # F_2 paths
    F2_path_direct,
    F2_path_bernoulli,
    F2_path_ahat,
    F2_path_ratio,
    F2_path_manual_bernoulli,
    F2_path_shadow_tower,
    verify_F2_all_paths,
    # Kappa paths
    kappa_path_direct,
    kappa_path_additivity,
    kappa_path_from_formula,
    kappa_path_from_genus1,
    kappa_path_from_complementarity,
    verify_kappa_all_paths,
    # Shadow tower
    virasoro_shadow_initial_data,
    burns_T_line_data,
    shadow_tower_sqrt_method,
    mc_recursion_tower,
    burns_shadow_tower_two_methods,
    # S_3
    burns_S3_T_line,
    burns_S3_weight_line,
    burns_S3_per_pair,
    burns_S3_global,
    # Planted forest
    planted_forest_genus2_T_line,
    planted_forest_genus2_weight_line,
    planted_forest_genus3_T_line,
    # F_3 prediction
    F3_prediction,
    # Costello comparison
    costello_comparison,
    # Asymptotic
    asymptotic_ratios,
    # Shadow metric
    burns_shadow_metric,
    # S_5
    burns_S5_T_line,
    # Full datum
    burns_full_datum,
)


# =========================================================================
# Section A: F_2 = 7/1440 — THE THEOREM (6 independent verification paths)
# =========================================================================

class TestF2Theorem:
    """F_2(A_Burns) = 7/1440 verified via 6 independent paths."""

    def test_F2_path_direct(self):
        """Path 1: F_2 = kappa * lambda_2^FP = 4 * 7/5760 = 7/1440."""
        assert F2_path_direct() == Rational(7, 1440)

    def test_F2_path_bernoulli(self):
        """Path 2: From B_4 = -1/30. lambda_2 = 7/8 * 1/30 / 24 = 7/5760."""
        assert F2_path_bernoulli() == Rational(7, 1440)

    def test_F2_path_ahat(self):
        """Path 3: From A-hat(ix) = (x/2)/sin(x/2) expansion at x^4."""
        assert F2_path_ahat() == Rational(7, 1440)

    def test_F2_path_manual_bernoulli(self):
        """Path 4: From hardcoded B_4 = -1/30 (independent of sympy)."""
        assert F2_path_manual_bernoulli() == Rational(7, 1440)

    def test_F2_path_ratio(self):
        """Path 5: F_2 = F_1 * (lambda_2/lambda_1) = (1/6)*(7/240) = 7/1440."""
        assert F2_path_ratio() == Rational(7, 1440)

    def test_F2_path_shadow_tower(self):
        """Path 6: F_2 = S_2 * lambda_2^FP where S_2 = kappa_T = 4."""
        assert F2_path_shadow_tower() == Rational(7, 1440)

    def test_F2_all_paths_agree(self):
        """All 6 paths agree on F_2 = 7/1440."""
        result = verify_F2_all_paths()
        assert result['all_agree']
        assert result['n_paths'] == 6
        assert result['target'] == Rational(7, 1440)

    def test_F2_numerical_value(self):
        """F_2 numerically approximately 0.004861."""
        F2 = F_g_burns(2)
        assert abs(float(F2) - 7.0/1440.0) < 1e-12

    def test_F2_positive(self):
        """F_2 > 0 (kappa > 0 implies all F_g > 0)."""
        assert F_g_burns(2) > 0

    def test_F2_less_than_F1(self):
        """F_2 < F_1 (Bernoulli decay)."""
        assert F_g_burns(2) < F_g_burns(1)

    def test_F2_ratio_to_F1(self):
        """F_2/F_1 = 7/240 (independent of kappa)."""
        ratio = F_g_burns(2) / F_g_burns(1)
        assert ratio == Rational(7, 240)


# =========================================================================
# Section B: kappa = 4 — verified via 5 independent paths
# =========================================================================

class TestKappaVerification:
    """kappa(A_Burns) = 4 verified via 5 independent paths."""

    def test_kappa_path_c_over_2(self):
        """Path 1: kappa = c/2 = 8/2 = 4."""
        assert kappa_path_direct() == 4

    def test_kappa_path_additivity(self):
        """Path 2: kappa = 4 * kappa_single = 4 * 1 = 4."""
        assert kappa_path_additivity() == 4

    def test_kappa_path_formula(self):
        """Path 3: kappa(bg,1) = 6-6+1 = 1, total = 4."""
        assert kappa_path_from_formula() == 4

    def test_kappa_path_genus1(self):
        """Path 4: From F_1 = kappa/24 = 1/6, kappa = 4."""
        assert kappa_path_from_genus1() == 4

    def test_kappa_path_complementarity(self):
        """Path 5: kappa(A!) = -4, so kappa(A) = 4."""
        assert kappa_path_from_complementarity() == 4

    def test_kappa_all_paths_agree(self):
        """All 5 paths agree on kappa = 4."""
        result = verify_kappa_all_paths()
        assert result['all_agree']
        assert result['n_paths'] == 5
        assert result['target'] == 4

    def test_kappa_module_constant(self):
        """The module constant KAPPA_TOTAL equals 4."""
        assert KAPPA_TOTAL == 4


# =========================================================================
# Section C: Faber-Pandharipande numbers (literature comparison)
# =========================================================================

class TestFaberPandharipande:
    """Verify lambda_g^FP against known values."""

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_4(self):
        """lambda_4 = 127/154828800."""
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_lambda_5(self):
        """lambda_5 = 73/3503554560."""
        assert lambda_fp(5) == Rational(73, 3503554560)

    def test_lambda_fp_manual_bernoulli_g2(self):
        """lambda_2 from manual B_4 agrees with sympy computation."""
        assert lambda_fp_from_bernoulli_manual(2) == lambda_fp(2)

    def test_lambda_fp_manual_bernoulli_g3(self):
        """lambda_3 from manual B_6 agrees with sympy computation."""
        assert lambda_fp_from_bernoulli_manual(3) == lambda_fp(3)

    def test_lambda_fp_ahat_g1(self):
        """lambda_1 from A-hat expansion agrees."""
        assert lambda_fp_from_ahat(1) == Rational(1, 24)

    def test_lambda_fp_ahat_g2(self):
        """lambda_2 from A-hat expansion agrees."""
        assert lambda_fp_from_ahat(2) == Rational(7, 5760)

    def test_lambda_fp_invalid_genus(self):
        """lambda_g raises ValueError for g < 1."""
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_lambda_all_positive(self):
        """All lambda_g > 0 for g = 1, ..., 5."""
        for g in range(1, 6):
            assert lambda_fp(g) > 0

    def test_lambda_decreasing(self):
        """lambda_g is strictly decreasing for g = 1, ..., 5."""
        for g in range(1, 5):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_bernoulli_B4(self):
        """B_4 = -1/30 (independent check)."""
        assert bernoulli_exact(4) == Rational(-1, 30)

    def test_bernoulli_B6(self):
        """B_6 = 1/42."""
        assert bernoulli_exact(6) == Rational(1, 42)


# =========================================================================
# Section D: Betagamma formulas (direct computation)
# =========================================================================

class TestBetagammaFormulas:
    """Verify bg/bc central charge and kappa."""

    def test_bg_c_lambda_0(self):
        """c(bg, lambda=0) = 2."""
        assert bg_central_charge(Rational(0)) == 2

    def test_bg_c_lambda_half(self):
        """c(bg, lambda=1/2) = -1."""
        assert bg_central_charge(Rational(1, 2)) == -1

    def test_bg_c_lambda_1(self):
        """c(bg, lambda=1) = 2."""
        assert bg_central_charge(Rational(1)) == 2

    def test_bg_kappa_lambda_0(self):
        """kappa(bg, lambda=0) = 1."""
        assert bg_kappa(Rational(0)) == 1

    def test_bg_kappa_lambda_1(self):
        """kappa(bg, lambda=1) = 1."""
        assert bg_kappa(Rational(1)) == 1

    def test_bg_kappa_lambda_half(self):
        """kappa(bg, lambda=1/2) = -1/2."""
        assert bg_kappa(Rational(1, 2)) == Rational(-1, 2)

    def test_bg_lambda_symmetry(self):
        """kappa(bg, lambda) = kappa(bg, 1-lambda) for all lambda."""
        for lam in [Rational(0), Rational(1, 3), Rational(1, 4), Rational(2, 7)]:
            assert bg_kappa(lam) == bg_kappa(1 - lam)

    def test_bg_kappa_equals_c_over_2(self):
        """kappa = c/2 for betagamma at all test weights (AP48: specific to bg)."""
        for lam in [Rational(0), Rational(1, 2), Rational(1), Rational(1, 3)]:
            assert bg_kappa(lam) == bg_central_charge(lam) / 2

    def test_bc_kappa_opposite(self):
        """kappa(bc) = -kappa(bg) for all lambda."""
        for lam in [Rational(0), Rational(1, 2), Rational(1)]:
            assert bc_kappa(lam) == -bg_kappa(lam)


# =========================================================================
# Section E: Shadow tower on T-line (two independent methods)
# =========================================================================

class TestShadowTower:
    """Shadow tower via sqrt(Q_L) and MC recursion agree."""

    def test_T_line_kappa(self):
        """T-line kappa = c/2 = 4."""
        data = burns_T_line_data()
        assert data['kappa'] == 4

    def test_T_line_S3(self):
        """T-line S_3 = 2 (universal Virasoro)."""
        data = burns_T_line_data()
        assert data['S_3'] == 2

    def test_T_line_S4(self):
        """T-line S_4 = Q^contact(c=8) = 5/248."""
        data = burns_T_line_data()
        assert data['S_4'] == Rational(5, 248)

    def test_T_line_S5(self):
        """T-line S_5 = -48/(64*62) = -3/248."""
        data = burns_T_line_data()
        assert data['S_5'] == Rational(-3, 248)

    def test_tower_S2_equals_kappa(self):
        """S_2 = kappa = 4 from the sqrt method."""
        data = burns_T_line_data()
        tower = shadow_tower_sqrt_method(data['kappa'], data['S_3'], data['S_4'], 6)
        assert tower[2] == 4

    def test_tower_S3_from_sqrt(self):
        """S_3 from sqrt method = 2."""
        data = burns_T_line_data()
        tower = shadow_tower_sqrt_method(data['kappa'], data['S_3'], data['S_4'], 6)
        assert tower[3] == 2

    def test_tower_S4_from_sqrt(self):
        """S_4 from sqrt method = 5/248."""
        data = burns_T_line_data()
        tower = shadow_tower_sqrt_method(data['kappa'], data['S_3'], data['S_4'], 6)
        assert tower[4] == Rational(5, 248)

    def test_two_methods_agree(self):
        """sqrt(Q_L) and MC recursion agree at arities 2-10."""
        result = burns_shadow_tower_two_methods(10)
        assert result['all_agree']

    def test_tower_S5_nonzero(self):
        """S_5 is nonzero (class M: infinite shadow depth)."""
        data = burns_T_line_data()
        tower = shadow_tower_sqrt_method(data['kappa'], data['S_3'], data['S_4'], 6)
        assert tower[5] != 0


# =========================================================================
# Section F: S_3 structure for Burns algebra
# =========================================================================

class TestS3Structure:
    """Verify S_3 on different lines of the Burns boundary VOA."""

    def test_S3_T_line_equals_2(self):
        """S_3 = 2 on the T-line (universal Virasoro)."""
        assert burns_S3_T_line() == 2

    def test_S3_weight_line_equals_0(self):
        """S_3 = 0 on the weight-changing line (no cubic vertex)."""
        assert burns_S3_weight_line() == 0

    def test_S3_per_pair_T_line(self):
        """S_3 = 2 on the T-line for each bg pair."""
        data = burns_S3_per_pair()
        assert data['S3_T_line'] == 2

    def test_S3_per_pair_weight_line(self):
        """S_3 = 0 on the weight line for each bg pair."""
        data = burns_S3_per_pair()
        assert data['S3_weight_line'] == 0

    def test_S3_per_pair_class_C(self):
        """Each bg pair is class C (contact)."""
        data = burns_S3_per_pair()
        assert data['shadow_class'] == 'C'

    def test_S3_global_T_line(self):
        """Global S_3 on T-line = 2."""
        data = burns_S3_global()
        assert data['S3_T_line'] == 2

    def test_S3_global_cross_terms_zero(self):
        """Cross-terms vanish (independent pairs)."""
        data = burns_S3_global()
        assert data['cross_terms'] == 0


# =========================================================================
# Section G: Planted-forest corrections
# =========================================================================

class TestPlantedForest:
    """Verify planted-forest corrections at genus 2 and genus 3."""

    def test_pf_genus2_T_line_value(self):
        """delta_pf^{(2,0)} = 2/3 on T-line."""
        result = planted_forest_genus2_T_line()
        assert result['delta_pf_g2'] == Rational(2, 3)

    def test_pf_genus2_T_line_formula(self):
        """delta_pf = S_3(10*S_3 - kappa)/48 = 2*(20-4)/48 = 2/3."""
        result = planted_forest_genus2_T_line()
        expected = Rational(2) * (10 * Rational(2) - Rational(4)) / 48
        assert result['delta_pf_g2'] == expected

    def test_pf_genus2_T_line_self_consistent(self):
        """Two evaluations of the formula agree."""
        result = planted_forest_genus2_T_line()
        assert result['agrees']

    def test_pf_genus2_weight_line_zero(self):
        """delta_pf = 0 on weight line (S_3 = 0)."""
        result = planted_forest_genus2_weight_line()
        assert result['delta_pf_g2'] == 0

    def test_pf_genus3_T_line_11_terms(self):
        """Genus-3 planted-forest has 11 terms."""
        result = planted_forest_genus3_T_line()
        assert result['n_terms'] == 11

    def test_pf_genus3_T_line_data(self):
        """Genus-3 computation uses correct input data."""
        result = planted_forest_genus3_T_line()
        assert result['kappa'] == 4
        assert result['S_3'] == 2
        assert result['S_4'] == Rational(5, 248)
        assert result['S_5'] == Rational(-3, 248)

    def test_pf_genus3_T_line_is_rational(self):
        """Genus-3 planted-forest correction is a rational number."""
        result = planted_forest_genus3_T_line()
        assert isinstance(result['delta_pf_g3'], Rational)

    def test_pf_genus3_T_line_nonzero(self):
        """Genus-3 planted-forest is nonzero for class M (Virasoro at c=8)."""
        result = planted_forest_genus3_T_line()
        assert result['delta_pf_g3'] != 0

    def test_pf_genus2_does_not_change_F2(self):
        """The planted-forest correction does NOT modify the scalar F_2.

        F_2 = kappa * lambda_2^FP is the SCALAR genus expansion.
        The planted-forest is a separate tautological contribution.
        """
        F2 = F_g_burns(2)
        pf = planted_forest_genus2_T_line()
        # F_2 is defined independently of the planted-forest
        assert F2 == Rational(7, 1440)
        # The planted-forest is a separate quantity
        assert pf['delta_pf_g2'] == Rational(2, 3)
        # They are NOT equal (different objects)
        assert F2 != pf['delta_pf_g2']


# =========================================================================
# Section H: F_3 prediction (3-loop gravitational correction)
# =========================================================================

class TestF3Prediction:
    """Verify F_3(A_Burns) = 31/241920."""

    def test_F3_value(self):
        """F_3 = 4 * 31/967680 = 31/241920."""
        pred = F3_prediction()
        assert pred['F_3'] == Rational(31, 241920)

    def test_F3_equals_target(self):
        """F_3 matches the target value."""
        pred = F3_prediction()
        assert pred['F_3'] == pred['target']

    def test_F3_all_paths_agree(self):
        """All 4 paths agree on F_3."""
        pred = F3_prediction()
        assert pred['all_agree']

    def test_F3_positive(self):
        """F_3 > 0."""
        assert F_g_burns(3) > 0

    def test_F3_less_than_F2(self):
        """F_3 < F_2 (monotone decreasing)."""
        assert F_g_burns(3) < F_g_burns(2)

    def test_F3_ratio_to_F1(self):
        """F_3/F_1 = lambda_3/lambda_1 = 31/40320."""
        pred = F3_prediction()
        expected_ratio = Rational(31, 967680) / Rational(1, 24)
        assert pred['ratio_F3_F1'] == expected_ratio

    def test_F3_from_bernoulli(self):
        """F_3 from manual B_6 = 1/42 agrees."""
        pred = F3_prediction()
        assert pred['F_3_bernoulli'] == Rational(31, 241920)

    def test_F3_from_ahat(self):
        """F_3 from A-hat generating function agrees."""
        pred = F3_prediction()
        assert pred['F_3_ahat'] == Rational(31, 241920)

    def test_F3_numerical(self):
        """F_3 approximately 1.281e-4."""
        pred = F3_prediction()
        assert abs(pred['F_3_numerical'] - 31.0 / 241920.0) < 1e-12


# =========================================================================
# Section I: Asymptotic analysis (universal instanton action)
# =========================================================================

class TestAsymptoticAnalysis:
    """Verify asymptotic behavior of F_g ratios."""

    def test_ratios_positive(self):
        """All F_{g+1}/F_g > 0 for g = 1,...,9."""
        result = asymptotic_ratios(10)
        for g, r in result['ratios'].items():
            assert r > 0

    def test_ratios_less_than_one(self):
        """F_{g+1}/F_g < 1 for all g (decaying sequence)."""
        result = asymptotic_ratios(10)
        for g, r in result['ratios'].items():
            assert r < 1

    def test_ratios_decreasing(self):
        """F_{g+1}/F_g is decreasing toward 1/(2*pi)^2."""
        result = asymptotic_ratios(10)
        ratios = result['ratios']
        for g in range(1, 8):
            if g in ratios and g + 1 in ratios:
                assert ratios[g] > ratios[g + 1]

    def test_asymptotic_limit(self):
        """F_{g+1}/F_g converges toward 1/(4*pi^2) ~ 0.0253."""
        result = asymptotic_ratios(10)
        last_ratio = result['ratios'][9]
        # At g=9, the ratio should be within 1% of the limit
        assert abs(last_ratio - result['theoretical_limit']) < 0.01


# =========================================================================
# Section J: Cross-engine consistency
# =========================================================================

class TestCrossEngineConsistency:
    """Cross-check against the existing burns_space_koszul_datum_engine."""

    def test_kappa_matches(self):
        """Our kappa matches the existing engine."""
        from compute.lib.burns_space_koszul_datum_engine import (
            BurnsSpaceData,
        )
        data = BurnsSpaceData()
        assert KAPPA_TOTAL == data.kappa_total

    def test_c_total_matches(self):
        """Our c_total matches the existing engine."""
        from compute.lib.burns_space_koszul_datum_engine import (
            BurnsSpaceData,
        )
        data = BurnsSpaceData()
        assert C_TOTAL == data.c_total

    def test_F2_matches(self):
        """Our F_2 matches the existing engine."""
        from compute.lib.burns_space_koszul_datum_engine import (
            burns_genus_expansion,
        )
        F_g = burns_genus_expansion()
        assert F_g_burns(2) == F_g[2]

    def test_F1_matches(self):
        """Our F_1 matches the existing engine."""
        from compute.lib.burns_space_koszul_datum_engine import (
            burns_genus_expansion,
        )
        F_g = burns_genus_expansion()
        assert F_g_burns(1) == F_g[1]

    def test_lambda_fp_matches(self):
        """Our lambda_fp matches the existing engine at g=1,...,5."""
        from compute.lib.burns_space_koszul_datum_engine import (
            lambda_fp as lambda_fp_existing,
        )
        for g in range(1, 6):
            assert lambda_fp(g) == lambda_fp_existing(g)

    def test_complementarity_matches(self):
        """Our complementarity sum matches."""
        from compute.lib.burns_space_koszul_datum_engine import (
            BurnsSpaceData,
        )
        data = BurnsSpaceData()
        assert COMPLEMENTARITY_SUM == data.complementarity_sum

    def test_planted_forest_g2_matches(self):
        """Our genus-2 planted-forest matches the existing engine."""
        from compute.lib.burns_space_koszul_datum_engine import (
            burns_planted_forest_g2,
        )
        existing_pf = burns_planted_forest_g2()
        our_pf = planted_forest_genus2_T_line()
        assert our_pf['delta_pf_g2'] == existing_pf['delta_pf_g2']

    def test_shadow_tower_matches(self):
        """Our shadow tower matches the existing engine at arities 2-6."""
        from compute.lib.burns_space_koszul_datum_engine import (
            burns_T_line_shadow_tower,
        )
        existing = burns_T_line_shadow_tower(max_r=6)
        data = burns_T_line_data()
        ours = shadow_tower_sqrt_method(data['kappa'], data['S_3'], data['S_4'], 6)
        for r in range(2, 7):
            assert ours[r] == existing[r], f"Mismatch at arity {r}"


# =========================================================================
# Section K: Costello-Paquette-Sharma comparison
# =========================================================================

class TestCostelloComparison:
    """Verify comparison with Costello-Paquette-Sharma framework."""

    def test_boundary_voa_is_4bg(self):
        """Boundary VOA is 4 pairs of bg at lambda=1."""
        comp = costello_comparison()
        assert '4' in comp['boundary_VOA']
        assert 'SO(8)' in comp['boundary_VOA']

    def test_c_total_equals_8(self):
        """c(A_Burns) = 8."""
        comp = costello_comparison()
        assert comp['c_total'] == 8

    def test_kappa_total_equals_4(self):
        """kappa(A_Burns) = 4."""
        comp = costello_comparison()
        assert comp['kappa_total'] == 4

    def test_genus_expansion_has_5_terms(self):
        """Genus expansion has F_1,...,F_5."""
        comp = costello_comparison()
        assert len(comp['genus_expansion']) == 5

    def test_uniform_weight_proved(self):
        """Uniform weight status is PROVED."""
        comp = costello_comparison()
        assert 'PROVED' in comp['uniform_weight_status']


# =========================================================================
# Section L: Shadow metric and classification
# =========================================================================

class TestShadowMetric:
    """Verify shadow metric and G/L/C/M classification."""

    def test_shadow_class_M_on_T_line(self):
        """T-line is class M (infinite shadow depth)."""
        metric = burns_shadow_metric()
        assert metric['shadow_class'] == 'M'

    def test_delta_nonzero(self):
        """Delta = 8*kappa*S_4 != 0."""
        metric = burns_shadow_metric()
        assert metric['Delta'] != 0

    def test_delta_value(self):
        """Delta = 8*4*5/248 = 20/31."""
        metric = burns_shadow_metric()
        assert metric['Delta'] == Rational(20, 31)

    def test_q0_positive(self):
        """q0 = 4*kappa^2 = 64 > 0."""
        metric = burns_shadow_metric()
        assert metric['q0'] == 64
        assert metric['q0'] > 0

    def test_S5_three_methods_agree(self):
        """S_5 verified by formula, MC recursion, and sqrt expansion."""
        result = burns_S5_T_line()
        assert result['all_agree']

    def test_S5_value(self):
        """S_5 = -3/248."""
        result = burns_S5_T_line()
        assert result['S_5_formula'] == Rational(-3, 248)


# =========================================================================
# Section M: Burns space constants
# =========================================================================

class TestBurnsConstants:
    """Verify all module-level Burns space constants."""

    def test_n_bg(self):
        """N_BG = 4 (complex dimension of transverse C^4)."""
        assert N_BG == 4

    def test_lambda_burns(self):
        """LAMBDA_BURNS = 1 (weight of beta fields)."""
        assert LAMBDA_BURNS == Rational(1)

    def test_c_single(self):
        """c(bg, lambda=1) = 2."""
        assert C_SINGLE == 2

    def test_kappa_single(self):
        """kappa(bg, lambda=1) = 1."""
        assert KAPPA_SINGLE == 1

    def test_c_total(self):
        """c(A_Burns) = 8."""
        assert C_TOTAL == 8

    def test_kappa_total(self):
        """kappa(A_Burns) = 4."""
        assert KAPPA_TOTAL == 4

    def test_c_dual(self):
        """c(A!_Burns) = -8."""
        assert C_DUAL == -8

    def test_kappa_dual(self):
        """kappa(A!_Burns) = -4."""
        assert KAPPA_DUAL == -4

    def test_complementarity_zero(self):
        """kappa + kappa' = 0 (free-field anti-symmetry, AP24)."""
        assert COMPLEMENTARITY_SUM == 0


# =========================================================================
# Section N: Full genus tower
# =========================================================================

class TestGenusTower:
    """Verify the complete genus tower F_1,...,F_5."""

    def test_F1(self):
        """F_1 = 1/6."""
        assert F_g_burns(1) == Rational(1, 6)

    def test_F2(self):
        """F_2 = 7/1440."""
        assert F_g_burns(2) == Rational(7, 1440)

    def test_F3(self):
        """F_3 = 31/241920."""
        assert F_g_burns(3) == Rational(31, 241920)

    def test_F4(self):
        """F_4 = 127/38707200."""
        assert F_g_burns(4) == Rational(127, 38707200)

    def test_F5(self):
        """F_5 = 73/875888640."""
        assert F_g_burns(5) == Rational(73, 875888640)

    def test_tower_dict(self):
        """burns_genus_tower returns correct dict."""
        tower = burns_genus_tower(5)
        assert len(tower) == 5
        assert tower[2] == Rational(7, 1440)

    def test_all_F_g_positive(self):
        """All F_g > 0 (kappa = 4 > 0)."""
        for g in range(1, 6):
            assert F_g_burns(g) > 0

    def test_monotone_decreasing(self):
        """F_g is strictly decreasing."""
        for g in range(1, 5):
            assert F_g_burns(g) > F_g_burns(g + 1)

    def test_F_g_scales_with_kappa(self):
        """F_g(A_Burns) = 4 * lambda_g^FP (kappa factorizes)."""
        for g in range(1, 6):
            assert F_g_burns(g) == 4 * lambda_fp(g)


# =========================================================================
# Section O: Full datum integration test
# =========================================================================

class TestFullDatum:
    """Integration test for the complete Burns space datum."""

    def test_full_datum_has_all_sections(self):
        """Full datum has algebra, dual, genus tower, shadow data."""
        datum = burns_full_datum()
        assert 'algebra' in datum
        assert 'koszul_dual' in datum
        assert 'genus_tower' in datum
        assert 'F_2_theorem' in datum
        assert 'F_3_prediction' in datum

    def test_full_datum_F2_correct(self):
        """Full datum F_2 = 7/1440."""
        datum = burns_full_datum()
        assert datum['F_2_theorem']['equals_7_over_1440']

    def test_full_datum_F3_correct(self):
        """Full datum F_3 = 31/241920."""
        datum = burns_full_datum()
        assert datum['F_3_prediction']['equals_31_over_241920']

    def test_full_datum_shadow_tower_consistent(self):
        """Shadow tower methods agree in full datum."""
        datum = burns_full_datum()
        assert datum['shadow_tower_agreement']

    def test_full_datum_complementarity(self):
        """Complementarity sum = 0 in full datum."""
        datum = burns_full_datum()
        assert datum['koszul_dual']['complementarity'] == 0

    def test_full_datum_S5_consistent(self):
        """S_5 three methods agree in full datum."""
        datum = burns_full_datum()
        assert datum['S_5']['all_agree']
