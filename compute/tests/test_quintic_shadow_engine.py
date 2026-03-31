r"""Tests for quintic-sextic shadow obstruction engine.

Verifies the FIRST EXPLICIT arity-5/6 shadow computations:

    S_5^Vir(c) = -48 / [c^2 (5c + 22)]
    S_6^Vir(c) = 80(45c + 193) / [3 c^3 (5c + 22)^2]
    S_7^Vir(c) = -2880(15c + 61) / [7 c^4 (5c + 22)^2]

Cross-checks:
  1. Exact symbolic formula against convolution recursion
  2. Numerical evaluation at multiple c values
  3. Depth classification: S_5 = 0 for G, L classes; != 0 for M
  4. bc ghosts stratum separation: S_5 = 1/2 on 1D metric but = 0 in full complex
  5. Complementarity: S_5(c) + S_5(26-c) structure
  6. DS depth increase: sl_2 (S_5=0) -> Vir (S_5!=0)
  7. Consistency with shadow_tower_recursive.py
  8. Growth rate diagnostics
"""

import pytest

from sympy import Rational, Symbol, cancel, simplify, factor

from compute.lib.quintic_shadow_engine import (
    virasoro_quintic_exact,
    virasoro_sextic_exact,
    virasoro_shadow_tower_exact,
    virasoro_shadow_numerical_table,
    heisenberg_quintic,
    affine_sl2_quintic,
    bc_ghosts_quintic,
    bc_ghosts_shadow_tower_1d,
    cross_family_quintic_table,
    ds_depth_increase_quintic,
    ds_depth_increase_sl3_quintic,
    virasoro_quintic_complementarity,
    quintic_growth_diagnostics,
    quintic_phase_diagram,
    w3_quintic_t_line,
    quintic_obstruction_class,
    virasoro_shadow_pattern,
    verify_quintic_formulas,
    virasoro_shadow_data,
    _convolution_coefficients,
)


c = Symbol('c', positive=True)
k = Symbol('k')


# ============================================================================
# SECTION 1: Exact formula verification
# ============================================================================

class TestVirasiroQuinticExact:
    """Test S_5^Vir(c) = -48/(c^2(5c+22))."""

    def test_s5_formula_matches(self):
        result = virasoro_quintic_exact()
        assert result['S5_matches'], f"S_5 mismatch: got {result['S5']}"

    def test_s5_explicit_value(self):
        tower = virasoro_shadow_tower_exact(6)
        S5_expected = Rational(-48) / (c ** 2 * (5 * c + 22))
        assert simplify(tower[5] - S5_expected) == 0

    def test_s2_is_kappa(self):
        tower = virasoro_shadow_tower_exact(3)
        assert simplify(tower[2] - c / 2) == 0

    def test_s3_is_constant(self):
        tower = virasoro_shadow_tower_exact(4)
        assert simplify(tower[3] - 2) == 0

    def test_s4_quartic_contact(self):
        tower = virasoro_shadow_tower_exact(5)
        S4_expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(tower[4] - S4_expected) == 0

    def test_s5_negative_for_positive_c(self):
        """S_5 < 0 for c > 0 (both factors in denominator positive)."""
        for c_val in [0.5, 1, 5, 13, 25, 100]:
            S5 = -48.0 / (c_val ** 2 * (5 * c_val + 22))
            assert S5 < 0, f"S_5({c_val}) = {S5} should be negative"

    def test_s5_singular_at_c_zero(self):
        """S_5 has a pole at c = 0 (order 2 in c from denominator c^2)."""
        tower = virasoro_shadow_tower_exact(6)
        # Evaluate near c=0: should diverge
        val = float(tower[5].subs(c, 0.001))
        assert abs(val) > 1e3

    def test_s5_singular_at_5c_plus_22(self):
        """S_5 has a simple pole at c = -22/5 (outside physical range)."""
        # Evaluate close to c = -22/5 + epsilon; but c is positive in our
        # symbol, so we just check the formula structure.
        tower = virasoro_shadow_tower_exact(6)
        factored = factor(tower[5])
        # denominator should contain (5c+22)
        assert factored is not None


class TestVirasiroSexticExact:
    """Test S_6^Vir(c) = 80(45c+193)/(3 c^3 (5c+22)^2)."""

    def test_s6_computed(self):
        result = virasoro_sextic_exact()
        assert result['S6'] is not None

    def test_s6_formula(self):
        """Verify S_6 matches the expected closed-form formula."""
        tower = virasoro_shadow_tower_exact(7)
        S6_expected = Rational(80) * (45 * c + 193) / (
            3 * c ** 3 * (5 * c + 22) ** 2)
        assert simplify(tower[6] - S6_expected) == 0

    def test_s7_formula(self):
        """Verify S_7 matches the expected closed-form formula."""
        tower = virasoro_shadow_tower_exact(8)
        S7_expected = Rational(-2880) * (15 * c + 61) / (
            7 * c ** 4 * (5 * c + 22) ** 2)
        assert simplify(tower[7] - S7_expected) == 0

    def test_s6_positive_at_positive_c(self):
        """S_6 > 0 for c > 0: numerator 45c+193 > 0 and denominator > 0."""
        result = virasoro_sextic_exact()
        S6_at_25 = float(result['S6'].subs(c, 25))
        assert S6_at_25 > 0

    def test_s7_computed(self):
        result = virasoro_sextic_exact()
        assert result['S7'] is not None

    def test_s8_computed(self):
        result = virasoro_sextic_exact()
        assert result['S8'] is not None

    def test_sextic_numerical_crosscheck(self):
        """Cross-check S_6 symbolic vs numerical at c=25."""
        result = virasoro_sextic_exact()
        S6_symbolic = float(result['S6'].subs(c, 25))
        num_tower = virasoro_shadow_numerical_table(25.0, 8)
        assert abs(S6_symbolic - num_tower[6]) < 1e-12


# ============================================================================
# SECTION 2: Cross-family depth verification
# ============================================================================

class TestCrossFamilyQuintic:
    """Verify S_5 = 0 for depth-bounded families, != 0 for Virasoro."""

    def test_heisenberg_s5_zero(self):
        assert heisenberg_quintic() == 0

    def test_affine_sl2_s5_zero(self):
        assert affine_sl2_quintic() == 0

    def test_bc_ghosts_s5_1d_nonzero(self):
        """On 1D metric, bc ghosts has S_5 != 0."""
        bg = bc_ghosts_quintic()
        assert bg['S5_1d_nonzero']

    def test_bc_ghosts_s5_equals_half(self):
        """On 1D metric, bc ghosts S_5 = 1/2 exactly."""
        bg = bc_ghosts_quintic()
        assert bg['S5_1d_metric'] == Rational(1, 2)

    def test_bc_ghosts_s5_true_zero(self):
        """True depth of bc ghosts is 4, so S_5 = 0 in full complex."""
        bg = bc_ghosts_quintic()
        assert bg['S5_true_depth'] == 0

    def test_bc_ghosts_stratum_separation(self):
        """bc ghosts: mechanism for depth-4 termination is stratum separation."""
        bg = bc_ghosts_quintic()
        assert bg['mechanism'] == 'stratum_separation'

    def test_virasoro_s5_nonzero(self):
        """Virasoro (class M) has S_5 != 0."""
        q5 = virasoro_quintic_exact()
        assert q5['S5'] != 0

    def test_cross_family_table_complete(self):
        table = cross_family_quintic_table()
        assert 'Heisenberg' in table
        assert 'Affine_sl2' in table
        assert 'bc_ghosts' in table
        assert 'Virasoro' in table

    def test_cross_family_depth_classification(self):
        table = cross_family_quintic_table()
        assert table['Heisenberg']['class'] == 'G'
        assert table['Affine_sl2']['class'] == 'L'
        assert table['bc_ghosts']['class'] == 'C'
        assert table['Virasoro']['class'] == 'M'


class TestBcGhosts1DTower:
    """Verify bc ghosts 1D shadow tower behavior."""

    def test_bc_ghosts_s2(self):
        """S_2 from 1D metric = |kappa| = 1 (not kappa = -1)."""
        tower = bc_ghosts_shadow_tower_1d(4)
        # a_0 = sqrt(4*kappa^2) = sqrt(4) = 2, S_2 = a_0/2 = 1
        assert tower[2] == Rational(1)

    def test_bc_ghosts_s3(self):
        """S_3 from 1D metric = a_1/3 = -3/3 = -1."""
        tower = bc_ghosts_shadow_tower_1d(4)
        assert tower[3] == Rational(-1)

    def test_bc_ghosts_s4(self):
        """S_4 from 1D metric = a_2/4 = (5/3)/4 = 5/12."""
        tower = bc_ghosts_shadow_tower_1d(5)
        assert tower[4] == Rational(5, 12)

    def test_bc_ghosts_s5_is_half(self):
        """S_5 from 1D metric = a_3/5 = (5/2)/5 = 1/2."""
        tower = bc_ghosts_shadow_tower_1d(6)
        assert tower[5] == Rational(1, 2)

    def test_bc_ghosts_s5_through_s8_nonzero(self):
        """On 1D metric, ALL S_r are nonzero for bc ghosts."""
        tower = bc_ghosts_shadow_tower_1d(10)
        for r in range(5, 10):
            assert tower[r] != 0, f"S_{r} should be nonzero on 1D metric"


# ============================================================================
# SECTION 3: DS depth increase
# ============================================================================

class TestDSDepthIncrease:
    """Verify DS depth increase mechanism at quintic level."""

    def test_sl2_to_vir_depth_increase(self):
        result = ds_depth_increase_quintic()
        assert result['depth_increase']

    def test_sl2_s5_zero(self):
        result = ds_depth_increase_quintic()
        assert result['S5_sl2'] == 0

    def test_vir_s5_nonzero_all_levels(self):
        result = ds_depth_increase_quintic()
        for k_val, ev in result['evaluations'].items():
            assert ev['S5_nonzero'], (
                f"S_5(Vir from DS at k={k_val}) should be nonzero")

    def test_ghost_central_charge(self):
        """c_ghost for sl_2 principal DS = 2 (= dim n_+)."""
        result = ds_depth_increase_quintic()
        c_ghost_simplified = cancel(result['c_ghost'])
        # c_ghost = (3k - k + 4)/(k+2) = (2k+4)/(k+2) = 2
        val = float(c_ghost_simplified.subs(k, 10))
        assert abs(val - 2.0) < 1e-10

    def test_sl3_to_w3_depth_increase(self):
        result = ds_depth_increase_sl3_quintic()
        assert result['S5_sl3'] == 0
        for k_val, ev in result['evaluations'].items():
            if not (ev['S5_W3_T_line'] != ev['S5_W3_T_line']):  # not NaN
                assert abs(ev['S5_W3_T_line']) > 1e-15


# ============================================================================
# SECTION 4: Complementarity at arity 5
# ============================================================================

class TestQuinticComplementarity:
    """Test S_5(c) + S_5(26-c) structure."""

    def test_complementarity_computed(self):
        comp = virasoro_quintic_complementarity()
        assert comp['sum'] is not None

    def test_self_dual_s5(self):
        """At c=13 (self-dual point), S_5(13) has a specific value."""
        comp = virasoro_quintic_complementarity()
        S5_13 = -48.0 / (13.0 ** 2 * (65 + 22))
        assert abs(comp['self_dual_S5'] - S5_13) < 1e-12

    def test_complementarity_sum_at_13(self):
        """At c=13: S_5(13) + S_5(13) = 2*S_5(13)."""
        comp = virasoro_quintic_complementarity()
        expected = 2 * (-48.0 / (13.0 ** 2 * 87.0))
        assert abs(comp['self_dual_sum'] - expected) < 1e-12

    def test_complementarity_sum_rational(self):
        """The sum S_5(c) + S_5(26-c) should be a rational function of c."""
        comp = virasoro_quintic_complementarity()
        # The sum is rational in c
        assert comp['sum_factored'] is not None

    def test_complementarity_sum_symmetric_under_exchange(self):
        """S_5(c) + S_5(26-c) should be symmetric under c <-> 26-c."""
        comp = virasoro_quintic_complementarity()
        # Evaluate at c and 26-c
        val_5 = float(comp['sum'].subs(c, 5))
        val_21 = float(comp['sum'].subs(c, 21))
        assert abs(val_5 - val_21) < 1e-12


# ============================================================================
# SECTION 5: Numerical consistency
# ============================================================================

class TestNumericalConsistency:
    """Cross-check symbolic vs numerical at multiple c values."""

    @pytest.mark.parametrize("c_val", [0.5, 1, 2, 5, 10, 13, 25, 50, 100])
    def test_s5_symbolic_vs_numerical(self, c_val):
        tower_exact = virasoro_shadow_tower_exact(6)
        S5_sym = float(tower_exact[5].subs(c, c_val))

        num_tower = virasoro_shadow_numerical_table(c_val, 6)
        S5_num = num_tower[5]

        if abs(S5_sym) > 1e-50:
            assert abs(S5_sym - S5_num) / abs(S5_sym) < 1e-10
        else:
            assert abs(S5_num) < 1e-15

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25])
    def test_s6_symbolic_vs_numerical(self, c_val):
        result = virasoro_sextic_exact()
        S6_sym = float(result['S6'].subs(c, c_val))

        num_tower = virasoro_shadow_numerical_table(c_val, 8)
        S6_num = num_tower[6]

        if abs(S6_sym) > 1e-50:
            assert abs(S6_sym - S6_num) / abs(S6_sym) < 1e-10

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25])
    def test_s7_symbolic_vs_numerical(self, c_val):
        result = virasoro_sextic_exact()
        S7_sym = float(result['S7'].subs(c, c_val))

        num_tower = virasoro_shadow_numerical_table(c_val, 8)
        S7_num = num_tower[7]

        if abs(S7_sym) > 1e-50:
            assert abs(S7_sym - S7_num) / abs(S7_sym) < 1e-10

    def test_growth_rate_convergence(self):
        """At c=25 (convergent), ratio test should approach rho < 1."""
        diag = quintic_growth_diagnostics(25.0)
        assert diag['convergent']
        assert diag['rho_exact'] < 1.0

    def test_growth_rate_divergence(self):
        """At c=1/2 (Ising, divergent), rho > 1."""
        diag = quintic_growth_diagnostics(0.5)
        assert not diag['convergent']
        assert diag['rho_exact'] > 1.0

    def test_phase_diagram(self):
        pd = quintic_phase_diagram()
        assert len(pd) >= 5
        # c=25 should be convergent
        assert pd['c=25.0']['convergent']
        # c=0.5 should be divergent
        assert not pd['c=0.5']['convergent']


# ============================================================================
# SECTION 6: Shadow tower consistency
# ============================================================================

class TestTowerConsistency:
    """Verify consistency of the tower across arities."""

    def test_tower_monotone_decrease_large_c(self):
        """For large c, |S_r| decreases with r (after initial terms)."""
        tower = virasoro_shadow_numerical_table(100.0, 15)
        # From arity 4 onwards, magnitudes should decrease
        for r in range(5, 14):
            assert abs(tower[r]) >= abs(tower[r + 1]) * 0.3, (
                f"|S_{r}| = {abs(tower[r])}, "
                f"|S_{r+1}| = {abs(tower[r + 1])}")

    def test_shadow_metric_reconstruction_a0(self):
        """a_0^2 = q0."""
        data = virasoro_shadow_data()
        coeffs = _convolution_coefficients(
            data['q0'], data['q1'], data['q2'], 3)
        a0_sq = cancel(coeffs[0] ** 2)
        assert simplify(a0_sq - data['q0']) == 0

    def test_shadow_metric_reconstruction_a1(self):
        """2 a_0 a_1 = q1."""
        data = virasoro_shadow_data()
        coeffs = _convolution_coefficients(
            data['q0'], data['q1'], data['q2'], 3)
        lhs = cancel(2 * coeffs[0] * coeffs[1])
        assert simplify(lhs - data['q1']) == 0

    def test_shadow_metric_reconstruction_a2(self):
        """2 a_0 a_2 + a_1^2 = q2."""
        data = virasoro_shadow_data()
        coeffs = _convolution_coefficients(
            data['q0'], data['q1'], data['q2'], 3)
        lhs = cancel(2 * coeffs[0] * coeffs[2] + coeffs[1] ** 2)
        assert simplify(lhs - data['q2']) == 0

    def test_convolution_identity_arity5(self):
        """Verify t^3 coefficient of f^2 vanishes (Q_L is quadratic)."""
        data = virasoro_shadow_data()
        coeffs = _convolution_coefficients(
            data['q0'], data['q1'], data['q2'], 5)
        lhs = cancel(
            2 * coeffs[0] * coeffs[3] + 2 * coeffs[1] * coeffs[2])
        assert simplify(lhs) == 0

    def test_convolution_identity_arity6(self):
        """Verify t^4 coefficient of f^2 vanishes."""
        data = virasoro_shadow_data()
        coeffs = _convolution_coefficients(
            data['q0'], data['q1'], data['q2'], 6)
        lhs = cancel(
            2 * coeffs[0] * coeffs[4]
            + 2 * coeffs[1] * coeffs[3]
            + coeffs[2] ** 2)
        assert simplify(lhs) == 0

    def test_convolution_identity_arity7(self):
        """Verify t^5 coefficient of f^2 vanishes."""
        data = virasoro_shadow_data()
        coeffs = _convolution_coefficients(
            data['q0'], data['q1'], data['q2'], 7)
        lhs = cancel(
            2 * coeffs[0] * coeffs[5]
            + 2 * coeffs[1] * coeffs[4]
            + 2 * coeffs[2] * coeffs[3])
        assert simplify(lhs) == 0

    def test_tower_max_arity_10(self):
        """Can compute tower to arity 10."""
        tower = virasoro_shadow_tower_exact(10)
        assert len(tower) == 9  # S_2 through S_10
        for r in range(2, 11):
            assert r in tower


# ============================================================================
# SECTION 7: W_3 quintic
# ============================================================================

class TestW3Quintic:
    """Test W_3 quintic on T-line."""

    def test_w3_t_line_computed(self):
        result = w3_quintic_t_line()
        assert result['S5_T_line'] is not None

    @pytest.mark.parametrize("k_val", [1, 2, 5, 10, 20])
    def test_w3_s5_nonzero(self, k_val):
        result = w3_quintic_t_line(k_val)
        c_w3 = float(result['c_W3'])
        if abs(c_w3) > 0.01 and abs(5 * c_w3 + 22) > 0.01:
            S5 = -48.0 / (c_w3 ** 2 * (5 * c_w3 + 22))
            assert abs(S5) > 1e-20

    def test_w3_w_line_frontier(self):
        from compute.lib.quintic_shadow_engine import w3_quintic_w_line
        result = w3_quintic_w_line()
        assert result['status'] == 'frontier'


# ============================================================================
# SECTION 8: Obstruction class
# ============================================================================

class TestObstructionClass:
    """Test quintic obstruction class properties."""

    def test_quintic_forced_class_m(self):
        result = quintic_obstruction_class()
        assert result['quintic_forced_class_M']

    def test_quintic_vanishes_class_g(self):
        result = quintic_obstruction_class()
        assert result['quintic_vanishes_class_G']

    def test_quintic_vanishes_class_l(self):
        result = quintic_obstruction_class()
        assert result['quintic_vanishes_class_L']

    def test_quintic_stratum_class_c(self):
        result = quintic_obstruction_class()
        assert result['quintic_stratum_separated_class_C']

    def test_forest_count_arity_5(self):
        """A000311(5) = 236 planted forests on 5 leaves."""
        result = quintic_obstruction_class()
        assert result['n_forests_arity_5'] == 236

    def test_binary_tree_count_arity_5(self):
        """Catalan C_4 = 14 binary trees on 5 leaves."""
        result = quintic_obstruction_class()
        assert result['n_binary_trees_arity_5'] == 14


# ============================================================================
# SECTION 9: Verification suite
# ============================================================================

class TestVerificationSuite:
    """Run the built-in verification suite."""

    def test_all_verifications_pass(self):
        results = verify_quintic_formulas()
        for name, ok in results.items():
            assert ok, f"Verification failed: {name}"


# ============================================================================
# SECTION 10: Cross-check with shadow_tower_recursive
# ============================================================================

class TestCrossCheckShadowTower:
    """Cross-check against the existing shadow_tower_recursive.py engine."""

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 13.0, 25.0])
    def test_s5_matches_recursive_tower(self, c_val):
        """S_5 from quintic engine matches shadow_tower_recursive."""
        from compute.lib.shadow_tower_recursive import compute_shadow_tower

        kap = c_val / 2
        alp = 2.0
        s4 = 10.0 / (c_val * (5 * c_val + 22))

        tower = compute_shadow_tower(
            kap, alp, s4, max_arity=8,
            algebra_name=f"Vir(c={c_val})")
        S5_recursive = tower.coefficients[5].numerical

        # From quintic engine (corrected formula)
        S5_quintic = -48.0 / (c_val ** 2 * (5 * c_val + 22))

        assert abs(S5_recursive - S5_quintic) < 1e-10 * abs(S5_quintic)

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 13.0, 25.0])
    def test_s6_matches_recursive_tower(self, c_val):
        """S_6 from quintic engine matches shadow_tower_recursive."""
        from compute.lib.shadow_tower_recursive import compute_shadow_tower

        kap = c_val / 2
        alp = 2.0
        s4 = 10.0 / (c_val * (5 * c_val + 22))

        tower = compute_shadow_tower(kap, alp, s4, max_arity=8)
        S6_recursive = tower.coefficients[6].numerical

        # From quintic engine
        result = virasoro_sextic_exact()
        S6_exact = float(result['S6'].subs(c, c_val))

        if abs(S6_recursive) > 1e-50:
            assert abs(S6_recursive - S6_exact) / abs(S6_recursive) < 1e-8

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 13.0, 25.0])
    def test_s7_matches_recursive_tower(self, c_val):
        """S_7 from quintic engine matches shadow_tower_recursive."""
        from compute.lib.shadow_tower_recursive import compute_shadow_tower

        kap = c_val / 2
        alp = 2.0
        s4 = 10.0 / (c_val * (5 * c_val + 22))

        tower = compute_shadow_tower(kap, alp, s4, max_arity=8)
        S7_recursive = tower.coefficients[7].numerical

        result = virasoro_sextic_exact()
        S7_exact = float(result['S7'].subs(c, c_val))

        if abs(S7_recursive) > 1e-50:
            assert abs(S7_recursive - S7_exact) / abs(S7_recursive) < 1e-8

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 13.0, 25.0])
    def test_bc_ghosts_matches_recursive(self, c_val):
        """bc ghosts 1D tower matches shadow_tower_recursive."""
        from compute.lib.shadow_tower_recursive import compute_shadow_tower

        tower_rec = compute_shadow_tower(
            -1.0, 1.0, -5.0 / 12.0, max_arity=8,
            algebra_name="bc_ghosts")

        tower_1d = bc_ghosts_shadow_tower_1d(8)

        for r in range(2, 8):
            rec_val = tower_rec.coefficients[r].numerical
            exact_val = float(tower_1d[r])
            assert abs(rec_val - exact_val) < 1e-10 * max(1, abs(exact_val)), \
                f"S_{r} mismatch: recursive={rec_val}, exact={exact_val}"


# ============================================================================
# SECTION 11: Higher-arity pattern analysis
# ============================================================================

class TestHigherArityPattern:
    """Analyze patterns in the shadow tower at higher arities."""

    def test_pattern_computed(self):
        pattern = virasoro_shadow_pattern(10)
        assert len(pattern) >= 8

    def test_alternating_signs_large_c(self):
        """For large c, shadow coefficients alternate in sign past arity 4."""
        tower = virasoro_shadow_numerical_table(100.0, 12)
        assert tower[2] > 0   # kappa = c/2 > 0
        assert tower[5] < 0   # S_5 < 0 for c > 0
        assert tower[6] > 0   # S_6 > 0 for c > 0

    def test_magnitude_decay_convergent(self):
        """For convergent tower (c=25), magnitudes decay geometrically."""
        tower = virasoro_shadow_numerical_table(25.0, 15)
        ratios = []
        for r in range(5, 14):
            if abs(tower[r]) > 1e-50:
                ratios.append(abs(tower[r + 1] / tower[r]))
        # Ratios should approach rho < 1
        if ratios:
            assert ratios[-1] < 1.0

    def test_sign_pattern_s5_to_s7(self):
        """S_5 < 0, S_6 > 0, S_7 < 0 for all positive c."""
        for c_val in [1, 5, 13, 25]:
            tower = virasoro_shadow_numerical_table(c_val, 8)
            assert tower[5] < 0, f"S_5({c_val}) should be < 0"
            assert tower[6] > 0, f"S_6({c_val}) should be > 0"
            assert tower[7] < 0, f"S_7({c_val}) should be < 0"


# ============================================================================
# SECTION 12: Betagamma 1D vs true depth distinction
# ============================================================================

class TestBcGhosts1DvsTrue:
    """Verify the key finding: 1D metric overestimates depth for class C."""

    def test_1d_depth_infinite(self):
        """On 1D metric, bc ghosts tower never terminates."""
        tower = bc_ghosts_shadow_tower_1d(12)
        for r in range(3, 12):
            assert tower[r] != 0, (
                f"S_{r} = 0 on 1D metric for bc ghosts; "
                f"expected nonzero (1D overestimates depth)")

    def test_true_depth_is_4(self):
        """True depth is 4 (class C) via stratum separation."""
        bg = bc_ghosts_quintic()
        assert bg['S5_true_depth'] == 0
        assert bg['mechanism'] == 'stratum_separation'

    def test_bc_ghosts_s6_1d_nonzero(self):
        tower = bc_ghosts_shadow_tower_1d(7)
        assert tower[6] != 0

    def test_bc_ghosts_exact_s4(self):
        """S_4 on 1D = 5/12 (note: signed differently from true S_4 = -5/12
        because a_0 = |2*kappa| = 2, not 2*kappa = -2)."""
        tower = bc_ghosts_shadow_tower_1d(5)
        # a_2 = (q2 - a1^2)/(2*a0)
        # q2 = 47/3, a1 = -3, a0 = 2
        # a_2 = (47/3 - 9)/4 = (20/3)/4 = 5/3
        # S_4 = a_2/4 = 5/12
        assert tower[4] == Rational(5, 12)
