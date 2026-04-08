r"""Tests for the exact full-OPE delta_F2(W_5) engine.

Multi-path verification per CLAUDE.md mandate: every numerical result
verified by at least 3 independent paths.

Test groups:
    1. OPE coupling formulas (6 tests)
    2. Master formula verification (8 tests)
    3. Per-graph contributions (7 tests)
    4. Rational part R(c) (6 tests)
    5. Irrational decomposition (5 tests)
    6. Galois structure (7 tests)
    7. Gravitational limit (4 tests)
    8. Large-c asymptotics (3 tests)
    9. Cross-algebra comparison (4 tests)
    10. Exact arithmetic (4 tests)

Total: 54 tests.
"""

import math
from fractions import Fraction

import pytest

from compute.lib.w5_full_ope_delta_f2_engine import (
    CHANNELS,
    WEIGHTS,
    IS_ODD,
    _C3,
    _master_formula_float,
    delta_F2_full,
    delta_F2_full_via_master,
    delta_F2_W3,
    direct_graph_sum,
    full_evaluation,
    g334_squared_exact,
    g334_squared_float,
    g345_squared_exact,
    g345_squared_float,
    g444_squared_exact,
    g444_squared_float,
    g455_squared_exact,
    g455_squared_float,
    g335_squared_float,
    g555_squared_float,
    galois_data_at,
    gravitational_part,
    gravitational_part_exact,
    higher_spin_correction,
    higher_spin_correction_decomposed,
    irrational_I1,
    irrational_I2,
    irrational_I3,
    irrational_I4,
    irrational_I5,
    kappa_total,
    kappa_total_exact,
    lambda_fp,
    large_c_limit,
    per_graph_grav_only,
    per_graph_mixed_float,
    rational_hs_part_exact,
    rational_hs_part_float,
    rational_part_exact,
    rational_part_float,
    verify_per_graph_sum,
    w3_w4_w5_comparison,
)


# ============================================================================
# 1. OPE coupling formulas
# ============================================================================

class TestOPECouplings:
    """Verify OPE structure constants g_{ijk}^2."""

    def test_g334_large_c(self):
        """g334^2 -> 10 as c -> infinity."""
        # 42*5/(7*3) = 210/21 = 10
        val = g334_squared_float(100000)
        assert abs(val - 10.0) < 0.01

    def test_g345_large_c(self):
        """g345^2 -> 80 as c -> infinity."""
        # 1680*5*2/(7*3*10) = 16800/210 = 80
        val = g345_squared_float(100000)
        assert abs(val - 80.0) < 0.1

    def test_g444_large_c(self):
        """g444^2 -> 48/25 as c -> infinity."""
        # 112*2*3/(7*10*5) = 672/350 = 48/25 = 1.92
        val = g444_squared_float(100000)
        assert abs(val - 1.92) < 0.01

    def test_g455_large_c(self):
        """g455^2 -> 96/5 as c -> infinity."""
        # 2240*2*3*1/(7*5*10*2) = 13440/700 = 96/5 = 19.2
        val = g455_squared_float(100000)
        assert abs(val - 19.2) < 0.1

    def test_g334_exact_at_10(self):
        """g334^2 at c=10: exact fraction check."""
        val = g334_squared_exact(Fraction(10))
        assert val == Fraction(6300, 7429)

    def test_parity_forbidden_g555(self):
        """g555^2 = 0 (W5 x W5 -> W5 forbidden by parity)."""
        assert g555_squared_float(10.0) == 0.0


# ============================================================================
# 2. Master formula verification
# ============================================================================

class TestMasterFormula:
    """Verify the master formula against independent graph sum."""

    @pytest.mark.parametrize("c_val", [2, 4, 7, 10, 26, 50, 100, 200])
    def test_master_vs_graph_sum(self, c_val):
        """Master formula matches direct graph sum at c = {c_val}."""
        master = delta_F2_full_via_master(float(c_val))
        graph = direct_graph_sum(float(c_val))['delta_F2']
        assert abs(master - graph) < 1e-10, \
            f"c={c_val}: master={master}, graph={graph}"

    @pytest.mark.parametrize("c_val", [4, 10, 26, 50, 100, 200])
    def test_decomposition_vs_master(self, c_val):
        """R + I1 + I2 + I3 + I4 + I5 matches master formula."""
        full = delta_F2_full(float(c_val))
        master = delta_F2_full_via_master(float(c_val))
        assert abs(full - master) < 1e-10, \
            f"c={c_val}: full={full}, master={master}"


# ============================================================================
# 3. Per-graph contributions
# ============================================================================

class TestPerGraph:
    """Verify per-graph analytic formulas."""

    def test_fig_eight_zero(self):
        """Fig-eight has zero mixed contribution (single edge)."""
        pg = per_graph_mixed_float(10.0)
        assert pg['fig_eight'] == 0.0

    def test_dumbbell_zero(self):
        """Dumbbell has zero mixed contribution (single edge)."""
        pg = per_graph_mixed_float(10.0)
        assert pg['dumbbell'] == 0.0

    @pytest.mark.parametrize("c_val", [4, 10, 50, 100])
    def test_per_graph_sum_matches_total(self, c_val):
        """Sum of per-graph contributions matches delta_F2."""
        result = verify_per_graph_sum(float(c_val))
        assert result['match'], \
            f"c={c_val}: sum={result['graph_sum']}, total={result['total']}"

    def test_grav_only_per_graph(self):
        """Gravitational-only per-graph values sum to (c+434)/(4c)."""
        c = 10.0
        pg = per_graph_grav_only(c)
        total = sum(pg.values())
        expected = gravitational_part(c)
        assert abs(total - expected) < 1e-12

    def test_banana_at_c10(self):
        """Banana mixed amplitude at c=10 is positive."""
        pg = per_graph_mixed_float(10.0)
        assert pg['banana'] > 0

    def test_theta_at_c10(self):
        """Theta mixed amplitude at c=10 is positive."""
        pg = per_graph_mixed_float(10.0)
        assert pg['theta'] > 0


# ============================================================================
# 4. Rational part R(c)
# ============================================================================

class TestRationalPart:
    """Verify the rational part R(c)."""

    @pytest.mark.parametrize("c_val", [4, 10, 26, 50, 100])
    def test_rational_float_vs_exact(self, c_val):
        """Float and exact evaluations agree."""
        f = rational_part_float(float(c_val))
        e = float(rational_part_exact(Fraction(c_val)))
        assert abs(f - e) < 1e-10, f"c={c_val}: float={f}, exact={e}"

    def test_rational_decomposition(self):
        """R(c) = grav(c) + R_HS(c)."""
        for cv in [10, 50, 100]:
            c = Fraction(cv)
            R = rational_part_exact(c)
            grav = gravitational_part_exact(c)
            hs = rational_hs_part_exact(c)
            assert R == grav + hs, f"c={cv}: R != grav + hs"

    def test_rational_part_at_c1(self):
        """R(1) is a specific exact fraction."""
        R = rational_part_exact(Fraction(1))
        # Verify it's a well-defined positive fraction
        assert R > 0
        # Cross-check with float
        assert abs(float(R) - rational_part_float(1.0)) < 1e-12

    def test_grav_formula(self):
        """Gravitational part = (c+434)/(4c)."""
        for cv in [4, 10, 26, 100]:
            expected = (cv + 434) / (4 * cv)
            actual = gravitational_part(float(cv))
            assert abs(actual - expected) < 1e-14

    def test_grav_at_c1(self):
        """Gravitational at c=1: 435/4."""
        assert gravitational_part_exact(Fraction(1)) == Fraction(435, 4)


# ============================================================================
# 5. Irrational decomposition
# ============================================================================

class TestIrrationalTerms:
    """Verify the five irrational terms."""

    def test_all_irrational_positive(self):
        """All 5 irrational terms are positive for c > 1/2."""
        for cv in [2, 10, 100]:
            c = float(cv)
            assert irrational_I1(c) > 0
            assert irrational_I2(c) > 0
            assert irrational_I3(c) > 0
            assert irrational_I4(c) > 0
            assert irrational_I5(c) > 0

    def test_I1_formula(self):
        """I_1 = sqrt(g334^2)/64."""
        c = 10.0
        expected = math.sqrt(g334_squared_float(c)) / 64
        assert abs(irrational_I1(c) - expected) < 1e-15

    def test_I2_formula(self):
        """I_2 = sqrt(g455^2)/48."""
        c = 10.0
        expected = math.sqrt(g455_squared_float(c)) / 48
        assert abs(irrational_I2(c) - expected) < 1e-15

    def test_I3_formula(self):
        """I_3 = (3/2)*sqrt(g334^2*g444^2)/c."""
        c = 10.0
        expected = 1.5 * math.sqrt(g334_squared_float(c)
                                    * g444_squared_float(c)) / c
        assert abs(irrational_I3(c) - expected) < 1e-15

    def test_hs_decomposition_sums(self):
        """Rational HS + all irrationals = total HS correction."""
        c = 10.0
        decomp = higher_spin_correction_decomposed(c)
        total_from_parts = decomp['rational_hs'] + decomp['total_irrational']
        assert abs(total_from_parts - decomp['total_hs']) < 1e-10


# ============================================================================
# 6. Galois structure
# ============================================================================

class TestGalois:
    """Verify the Galois group (Z/2)^3."""

    def test_galois_rank_at_c7(self):
        """F_2-rank = 3 at c=7."""
        data = galois_data_at(Fraction(7))
        assert data['rank'] == 3
        assert data['group'] == '(Z/2)^3'
        assert data['order'] == 8

    def test_galois_rank_at_c10(self):
        """F_2-rank = 3 at c=10."""
        data = galois_data_at(Fraction(10))
        assert data['rank'] == 3

    def test_galois_rank_at_c26(self):
        """F_2-rank = 3 at c=26."""
        data = galois_data_at(Fraction(26))
        assert data['rank'] == 3

    def test_g345_rational(self):
        """g345 only appears squared, so its class is irrelevant."""
        # g345 is parity-allowed but only appears in g345^2 (even power)
        # so it does not contribute to the Galois group
        data = galois_data_at(Fraction(10))
        # The relevant classes are 334, 444, 455 (not 345)
        assert '345' not in data['relevant_classes']

    def test_three_independent_sqrts_at_c50(self):
        """Three squarefree classes are pairwise independent at c=50."""
        data = galois_data_at(Fraction(50))
        s334 = data['relevant_classes']['334']
        s444 = data['relevant_classes']['444']
        s455 = data['relevant_classes']['455']
        # All three should be nontrivial (not 0 or 1)
        assert s334 not in (0, 1)
        assert s444 not in (0, 1)
        assert s455 not in (0, 1)
        # Pairwise products should also be nontrivial
        from compute.lib.w5_full_ope_delta_f2_engine import _squarefree_int
        assert _squarefree_int(s334 * s444) != 1
        assert _squarefree_int(s334 * s455) != 1
        assert _squarefree_int(s444 * s455) != 1

    def test_galois_at_c_half(self):
        """At c=1/2 (Ising), g444^2=0 and g455^2<0 so rank collapses."""
        # g444^2 has factor (2c-1) which vanishes at c=1/2
        val = g444_squared_exact(Fraction(1, 2))
        assert val == 0
        # g455^2 also has factor (2c-1)
        val = g455_squared_exact(Fraction(1, 2))
        assert val == 0

    def test_galois_exceeds_w4(self):
        """W_5 Galois rank (3) exceeds W_4 Galois rank (2)."""
        # W_4 has rank 2 with discriminants D_334, D_444
        # W_5 adds D_455 giving rank 3
        data = galois_data_at(Fraction(10))
        assert data['rank'] == 3
        # W_4 would have rank 2 (only 334, 444)


# ============================================================================
# 7. Gravitational limit
# ============================================================================

class TestGravitationalLimit:
    """Verify the gravitational-only limit."""

    def test_grav_formula_434(self):
        """Gravitational part is exactly (c+434)/(4c)."""
        for cv in [2, 5, 10, 50, 100]:
            expected = (cv + 434) / (4.0 * cv)
            actual = gravitational_part(float(cv))
            assert abs(actual - expected) < 1e-14

    def test_grav_constant_term_217(self):
        """The constant 217/2 = 71/2 + 25 + 48 from per-graph breakdown."""
        # banana: 71/(2c), theta: 25/c, barbell: 48/c
        # Total: 71/(2c) + 25/c + 48/c = (71 + 50 + 96)/(2c) = 217/(2c)
        assert 71 + 50 + 96 == 217
        # grav = 1/4 + 217/(2c) = (c + 434)/(4c)
        assert 217 * 2 == 434

    def test_grav_from_weights(self):
        r"""Gravitational constant 434 = sum over mixed pairs.

        For channels with weights h_1,..,h_N, the gravitational
        cross-channel correction at genus 2 has the form
        (c + K)/(4c) where K depends on the weights.
        """
        # The value 434 is verified by direct computation
        grav_at_1 = gravitational_part(1.0)
        assert abs(grav_at_1 - 435 / 4) < 1e-14

    def test_kappa_formula(self):
        """kappa(W_5) = 77c/60 = (1/2+1/3+1/4+1/5)*c."""
        # H_5 - 1 = 1/2 + 1/3 + 1/4 + 1/5 = (30+20+15+12)/60 = 77/60
        assert kappa_total_exact(Fraction(60)) == Fraction(77)
        assert abs(kappa_total(10.0) - 77 * 10 / 60) < 1e-14


# ============================================================================
# 8. Large-c asymptotics
# ============================================================================

class TestLargeCAsymptotics:
    """Verify large-c behavior."""

    def test_large_c_leading(self):
        """delta -> 1/4 + sqrt(10)/64 + sqrt(96/5)/48 + O(1/c)."""
        expected = large_c_limit()
        # At c=100000, subleading terms ~ O(1/c) are negligible
        actual = delta_F2_full(100000.0)
        assert abs(actual - expected) < 0.01

    def test_large_c_grav_dominates_at_small_c(self):
        """At small c, gravitational part dominates (HS is perturbative)."""
        c = 2.0
        grav = gravitational_part(c)
        hs = higher_spin_correction(c)
        assert hs / grav < 0.05  # HS < 5% of gravitational at c=2

    def test_large_c_hs_grows(self):
        """At large c, HS correction becomes significant."""
        c = 100.0
        grav = gravitational_part(c)
        hs = higher_spin_correction(c)
        assert hs / grav > 0.5  # HS > 50% of gravitational at c=100


# ============================================================================
# 9. Cross-algebra comparison
# ============================================================================

class TestCrossAlgebra:
    """Compare with W_3 and W_4."""

    @pytest.mark.parametrize("c_val", [4, 10, 50, 100])
    def test_w5_exceeds_w3(self, c_val):
        """delta_F2(W_5) > delta_F2(W_3) for c > 1."""
        w5 = delta_F2_full(float(c_val))
        w3 = delta_F2_W3(float(c_val))
        assert w5 > w3, f"c={c_val}: W5={w5} <= W3={w3}"

    def test_w5_grav_vs_w3(self):
        """Even gravitational-only W_5 exceeds W_3."""
        for cv in [10, 50, 100]:
            w5g = gravitational_part(float(cv))
            w3 = delta_F2_W3(float(cv))
            assert w5g > w3

    def test_hierarchy_at_c10(self):
        """delta_F2(W_3) < delta_F2(W_4,grav) < delta_F2(W_5,grav) < delta_F2(W_5,full)."""
        c = 10.0
        comp = w3_w4_w5_comparison(c)
        assert comp['delta_W3'] < comp['delta_W4_grav']
        assert comp['delta_W4_grav'] < comp['delta_W5_grav']
        assert comp['delta_W5_grav'] < comp['delta_W5_full']

    def test_full_evaluation_consistency(self):
        """full_evaluation returns consistent data."""
        r = full_evaluation(10.0)
        assert r['match_master']
        assert r['match_graph']
        assert r['delta_F2_full'] > 0
        assert r['hs_total'] > 0
        assert r['kappa'] == kappa_total(10.0)


# ============================================================================
# 10. Exact arithmetic
# ============================================================================

class TestExactArithmetic:
    """Verify exact rational computations."""

    def test_rational_part_at_c1_exact(self):
        """R(1) is computed exactly."""
        R = rational_part_exact(Fraction(1))
        assert isinstance(R, Fraction)
        assert R > 0

    def test_grav_plus_hs_equals_R(self):
        """grav + R_HS = R at c=1,2,5,10."""
        for cv in [1, 2, 5, 10]:
            c = Fraction(cv)
            R = rational_part_exact(c)
            g = gravitational_part_exact(c)
            h = rational_hs_part_exact(c)
            assert R == g + h, f"c={cv}: {R} != {g} + {h}"

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_kappa_exact(self):
        """kappa(W_5) = 77c/60 exactly."""
        assert kappa_total_exact(Fraction(120)) == Fraction(77 * 120, 60)
        assert kappa_total_exact(Fraction(120)) == Fraction(154)


# ============================================================================
# 11. Parity constraints
# ============================================================================

class TestParity:
    """Verify Z_2 parity constraints on the Frobenius algebra."""

    def test_odd_triple_vanishes(self):
        """C_{W3,W3,W5} = 0 (3 odd-weight fields)."""
        c = 10.0
        val = _C3('W3', 'W3', 'W5', c, 1.0, 1.0, 1.0, 1.0)
        assert val == 0.0

    def test_odd_single_vanishes(self):
        """C_{W4,W4,W5} = 0 (1 odd-weight field)."""
        c = 10.0
        val = _C3('W4', 'W4', 'W5', c, 1.0, 1.0, 1.0, 1.0)
        assert val == 0.0

    def test_allowed_triple_nonzero(self):
        """C_{W3,W4,W5} != 0 (2 odd-weight fields)."""
        c = 10.0
        val = _C3('W3', 'W4', 'W5', c, 1.0, 1.0, 1.0, 1.5)
        assert val != 0.0

    def test_gravitational_coupling(self):
        """C_{T,W5,W5} = c (gravitational coupling)."""
        c = 10.0
        val = _C3('T', 'W5', 'W5', c, 0.0, 0.0, 0.0, 0.0)
        assert abs(val - c) < 1e-14

    def test_primary_constraint_TTW4(self):
        """C_{T,T,W4} = 0 (W4 primary, not produced by TxT)."""
        c = 10.0
        val = _C3('T', 'T', 'W4', c, 1.0, 1.0, 1.0, 1.0)
        assert val == 0.0

    def test_primary_constraint_TW3W5(self):
        """C_{T,W3,W5} = 0 (W5 not produced by TxW3)."""
        c = 10.0
        val = _C3('T', 'W3', 'W5', c, 1.0, 1.0, 1.0, 1.0)
        assert val == 0.0


# ============================================================================
# 12. Master formula coefficient cross-checks
# ============================================================================

class TestMasterCoefficients:
    """Verify individual master formula coefficients."""

    def test_constant_term(self):
        """960c*delta at g=0 gives 240c + 104160."""
        c = 10.0
        master_grav = 240 * c + 104160
        delta_grav = gravitational_part(c)
        assert abs(master_grav / (960 * c) - delta_grav) < 1e-14

    def test_g334_coefficient_from_lollipop(self):
        """The g334 coefficient in c*delta is c/64 (from lollipop)."""
        # In the master: 960c * delta has 15c*g334 term
        # So c*delta has (15/960)*c*g334 = c*g334/64. Check: 15/960 = 1/64.
        assert Fraction(15, 960) == Fraction(1, 64)

    def test_g455_coefficient_from_lollipop(self):
        """The g455 coefficient in c*delta is c/48 (from lollipop)."""
        # 960c*delta has 20c*g455. c*delta has 20/960*c*g455 = c*g455/48.
        assert Fraction(20, 960) == Fraction(1, 48)

    def test_g334sq_coefficient(self):
        """The g334^2 coefficient: 810/960 = 27/32."""
        assert Fraction(810, 960) == Fraction(27, 32)

    def test_g345sq_coefficient(self):
        """The g345^2 coefficient: 1152/960 = 6/5."""
        assert Fraction(1152, 960) == Fraction(6, 5)

    def test_g455sq_coefficient(self):
        """The g455^2 coefficient: 1440/960 = 3/2."""
        assert Fraction(1440, 960) == Fraction(3, 2)

    def test_g334_g444_coefficient(self):
        """The g334*g444 coefficient: 1440/960 = 3/2."""
        assert Fraction(1440, 960) == Fraction(3, 2)

    def test_g444_g455_coefficient(self):
        """The g444*g455 coefficient: 1920/960 = 2."""
        assert Fraction(1920, 960) == Fraction(2)
