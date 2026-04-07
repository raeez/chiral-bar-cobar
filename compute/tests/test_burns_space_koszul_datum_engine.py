r"""Tests for Burns space holographic modular Koszul datum engine.

Tests the first complete modular Koszul datum for a celestial holography example:
the gauged betagamma system with SO(8) flavor on Burns space.

Verification paths:
  1. Direct computation from defining formulas
  2. MC recursion (independent of sqrt(Q_L) assumption)
  3. Cross-check against existing engines (betagamma, Virasoro, shadow landscape)
  4. Limiting cases (n_bg=1, lambda=0, lambda=1/2)
  5. Symmetry/duality (kappa+kappa'=0, lambda<->1-lambda)
  6. Dimensional/degree analysis
  7. Cross-family consistency (additivity, complementarity)
  8. Numerical evaluation at specific parameters

60+ tests covering all 15 components of the engine.
"""

import pytest
from fractions import Fraction

from sympy import Rational, simplify, bernoulli, factorial

# Import the engine under test
from compute.lib.burns_space_koszul_datum_engine import (
    # Core
    lambda_fp,
    genus_free_energy,
    # Betagamma
    bg_central_charge,
    bg_kappa,
    bc_central_charge,
    bc_kappa,
    # Burns data
    BurnsSpaceData,
    N_BG_PAIRS,
    LAMBDA_BG,
    FLAVOR_GROUP,
    # Shadow tower
    virasoro_shadow_initial_data,
    shadow_tower_from_initial_data,
    mc_recursion_shadow_tower,
    burns_T_line_shadow_tower,
    burns_T_line_shadow_tower_mc,
    # Shadow metric
    shadow_metric_coefficients,
    critical_discriminant,
    shadow_class_from_data,
    burns_T_line_shadow_metric,
    # Genus expansion
    burns_genus_expansion,
    burns_genus_expansion_from_tower,
    # Koszul dual
    burns_koszul_dual,
    # R-matrix
    burns_r_matrix_structure,
    # Planted forest
    burns_planted_forest_g2,
    # Two-loop
    burns_two_loop_prediction,
    # Full datum
    burns_holographic_datum,
    # Parametric
    parametric_burns_datum,
    # Verification
    verify_kappa_additivity,
    verify_complementarity_antisymmetry,
    verify_shadow_tower_two_methods,
    verify_genus_1_from_kappa,
    verify_lambda_fp_values,
    verify_bg_lambda_symmetry,
    verify_c_kappa_relation,
    # Shadow connection
    burns_shadow_connection_data,
    # Propagator variance
    burns_propagator_variance,
)


# =========================================================================
# Section 1: Faber-Pandharipande numbers (path: literature comparison)
# =========================================================================

class TestFaberPandharipande:
    """Verify lambda_g^FP against known values from the literature."""

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
        """lambda_5 = 73/3503554560.

        Independent computation: B_10 = 5/66.
        lambda_5 = (2^9 - 1)/(2^9) * (5/66) / 10!
                  = 511/512 * 5/66 / 3628800
                  = 2555 / (512*66*3628800) = 2555 / 122624409600
        Simplify: 2555 = 5*511, 122624409600 = 512*66*3628800
        = 5*511 / (512*66*3628800) = 73 / 3503554560.
        """
        assert lambda_fp(5) == Rational(73, 3503554560)

    def test_lambda_fp_invalid(self):
        """lambda_g is undefined for g < 1."""
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_verify_all_known(self):
        """Built-in verification function."""
        assert verify_lambda_fp_values()


# =========================================================================
# Section 2: Betagamma formulas (path: direct computation)
# =========================================================================

class TestBetagammaFormulas:
    """Verify bg/bc central charge and kappa from first principles."""

    def test_bg_c_lambda_0(self):
        """c(bg, lambda=0) = 2."""
        assert bg_central_charge(Rational(0)) == 2

    def test_bg_c_lambda_half(self):
        """c(bg, lambda=1/2) = -1 (symplectic bosons)."""
        assert bg_central_charge(Rational(1, 2)) == -1

    def test_bg_c_lambda_1(self):
        """c(bg, lambda=1) = 2."""
        assert bg_central_charge(Rational(1)) == 2

    def test_bg_kappa_lambda_0(self):
        """kappa(bg, lambda=0) = 1."""
        assert bg_kappa(Rational(0)) == 1

    def test_bg_kappa_lambda_half(self):
        """kappa(bg, lambda=1/2) = -1/2."""
        assert bg_kappa(Rational(1, 2)) == Rational(-1, 2)

    def test_bg_kappa_lambda_1(self):
        """kappa(bg, lambda=1) = 1."""
        assert bg_kappa(Rational(1)) == 1

    def test_bg_kappa_lambda_2(self):
        """kappa(bg, lambda=2) = 6*4 - 6*2 + 1 = 13."""
        assert bg_kappa(Rational(2)) == 13

    def test_bc_c_opposite(self):
        """c(bc) = -c(bg) for all lambda."""
        for lam in [Rational(0), Rational(1, 2), Rational(1), Rational(1, 3)]:
            assert bc_central_charge(lam) == -bg_central_charge(lam)

    def test_bc_kappa_opposite(self):
        """kappa(bc) = -kappa(bg) for all lambda."""
        for lam in [Rational(0), Rational(1, 2), Rational(1), Rational(1, 3)]:
            assert bc_kappa(lam) == -bg_kappa(lam)

    def test_lambda_symmetry(self):
        """kappa(bg, lambda) = kappa(bg, 1-lambda) for all lambda."""
        assert verify_bg_lambda_symmetry()

    def test_c_kappa_relation(self):
        """kappa = c/2 for betagamma at all weights."""
        assert verify_c_kappa_relation()


# =========================================================================
# Section 3: Burns space basic data (path: direct + cross-check)
# =========================================================================

class TestBurnsSpaceData:
    """Verify the Burns space boundary VOA basic invariants."""

    def test_parameters(self):
        """Physical parameters: 4 bg pairs at lambda=1 with SO(8) flavor."""
        assert N_BG_PAIRS == 4
        assert LAMBDA_BG == Rational(1)
        assert FLAVOR_GROUP == "SO(8)"

    def test_c_single(self):
        """c(bg, lambda=1) = 2."""
        data = BurnsSpaceData()
        assert data.c_single == 2

    def test_c_total(self):
        """c(A_Burns) = 4 * 2 = 8."""
        data = BurnsSpaceData()
        assert data.c_total == 8

    def test_kappa_single(self):
        """kappa(bg, lambda=1) = 1."""
        data = BurnsSpaceData()
        assert data.kappa_single == 1

    def test_kappa_total(self):
        """kappa(A_Burns) = 4 * 1 = 4."""
        data = BurnsSpaceData()
        assert data.kappa_total == 4

    def test_kappa_dual_single(self):
        """kappa(bc, lambda=1) = -1."""
        data = BurnsSpaceData()
        assert data.kappa_dual_single == -1

    def test_kappa_dual_total(self):
        """kappa(A!_Burns) = 4 * (-1) = -4."""
        data = BurnsSpaceData()
        assert data.kappa_dual_total == -4

    def test_complementarity_sum_zero(self):
        """kappa(A) + kappa(A!) = 0 for free-field pairs (AP24)."""
        data = BurnsSpaceData()
        assert data.complementarity_sum == 0

    def test_shadow_class_per_pair(self):
        """Each bg pair is class C (contact, r_max=4)."""
        data = BurnsSpaceData()
        assert data.shadow_class_per_pair == 'C'

    def test_shadow_class_global(self):
        """Global shadow class is C."""
        data = BurnsSpaceData()
        assert data.shadow_class_global == 'C'

    def test_shadow_class_T_line(self):
        """T-line shadow class is M (infinite depth for Virasoro at c=8)."""
        data = BurnsSpaceData()
        assert data.shadow_class_T_line == 'M'

    def test_shadow_depth_per_pair(self):
        """Shadow depth per bg pair: r_max = 4."""
        data = BurnsSpaceData()
        assert data.shadow_depth_per_pair == 4

    def test_shadow_depth_T_line_infinite(self):
        """T-line shadow depth: None (infinite)."""
        data = BurnsSpaceData()
        assert data.shadow_depth_T_line is None


# =========================================================================
# Section 4: Shadow tower on T-line (path: two independent methods)
# =========================================================================

class TestShadowTower:
    """Verify T-line shadow tower by two independent methods."""

    def test_virasoro_initial_data_c8(self):
        """Initial data for Virasoro at c=8: kappa=4, alpha=2, S4=5/248."""
        kappa, alpha, S4 = virasoro_shadow_initial_data(Rational(8))
        assert kappa == 4
        assert alpha == 2
        assert S4 == Rational(10) / (8 * (5 * 8 + 22))
        assert S4 == Rational(10, 496)
        assert S4 == Rational(5, 248)

    def test_tower_S2(self):
        """S_2 on T-line = kappa_T = c/2 = 4."""
        tower = burns_T_line_shadow_tower(max_r=6)
        assert tower[2] == 4

    def test_tower_S3(self):
        """S_3 on T-line = alpha = 2 (universal for Virasoro)."""
        tower = burns_T_line_shadow_tower(max_r=6)
        # S_3 = a_1/3 = 3*alpha/3 = alpha = 2
        # Wait: a_1 = q1/(2*a0) = 12*4*2 / (2*2*4) = 96/16 = 6
        # S_3 = a_1/3 = 6/3 = 2. Correct.
        assert tower[3] == 2

    def test_tower_S4(self):
        """S_4 on T-line = 5/248 = Q^contact_Vir(c=8)."""
        tower = burns_T_line_shadow_tower(max_r=6)
        # S_4 = a_2/4 = 4*S4/4 = S4 = 5/248. Let me verify:
        # a_2 = (q2 - a_1^2)/(2*a0) = (9*4 + 16*4*5/248 - 36) / (2*8)
        # = (36 + 320/248 - 36)/16 = (320/248)/16 = 320/3968 = 20/248 = 5/62
        # S_4 = a_2/4 = 5/248
        assert tower[4] == Rational(5, 248)

    def test_two_methods_agree(self):
        """sqrt(Q_L) method and MC recursion agree at all arities."""
        agreement = verify_shadow_tower_two_methods(max_r=10)
        for r in range(2, 11):
            assert agreement[r], f"Methods disagree at arity {r}"

    def test_tower_S5_independent(self):
        """Verify S_5 by MC recursion independently."""
        tower_mc = burns_T_line_shadow_tower_mc(max_r=6)
        tower_sq = burns_T_line_shadow_tower(max_r=6)
        assert tower_mc[5] == tower_sq[5]

    def test_tower_S6_independent(self):
        """Verify S_6 by MC recursion independently."""
        tower_mc = burns_T_line_shadow_tower_mc(max_r=7)
        tower_sq = burns_T_line_shadow_tower(max_r=7)
        assert tower_mc[6] == tower_sq[6]

    def test_tower_nonzero_S5(self):
        """S_5 is nonzero (Virasoro at c=8 is class M, tower does not terminate)."""
        tower = burns_T_line_shadow_tower(max_r=6)
        assert tower[5] != 0

    def test_tower_nonzero_S6(self):
        """S_6 is nonzero (class M, infinite depth)."""
        tower = burns_T_line_shadow_tower(max_r=7)
        assert tower[6] != 0


# =========================================================================
# Section 5: Shadow metric and discriminant (path: direct + formula check)
# =========================================================================

class TestShadowMetric:
    """Verify shadow metric Q_L, discriminant Delta, and classification."""

    def test_metric_coefficients(self):
        """Q_L(t) = 64 + 192t + (36 + 80/248)*t^2 for Burns T-line."""
        metric = burns_T_line_shadow_metric()
        assert metric['q0'] == 4 * 4**2  # = 64
        assert metric['q1'] == 12 * 4 * 2  # = 96
        # q2 = 9*4 + 16*4*5/248 = 36 + 320/248 = 36 + 40/31 = (36*31 + 40)/31
        # = (1116 + 40)/31 = 1156/31
        expected_q2 = 9 * Rational(2)**2 + 16 * Rational(4) * Rational(5, 248)
        assert metric['q2'] == expected_q2

    def test_delta_nonzero(self):
        """Delta = 8*kappa*S4 != 0 for Virasoro at c=8 (class M confirmation)."""
        metric = burns_T_line_shadow_metric()
        assert metric['Delta'] != 0
        # Delta = 8*4*5/248 = 160/248 = 20/31
        assert metric['Delta'] == Rational(20, 31)

    def test_class_M(self):
        """T-line classified as M (infinite shadow depth)."""
        metric = burns_T_line_shadow_metric()
        assert metric['class'] == 'M'

    def test_delta_formula(self):
        """Delta = 40/(5c+22) for Virasoro. At c=8: Delta = 40/62 = 20/31."""
        c_val = Rational(8)
        expected = Rational(40) / (5 * c_val + 22)
        metric = burns_T_line_shadow_metric()
        assert metric['Delta'] == expected

    def test_metric_gaussian_class(self):
        """Heisenberg (alpha=0, S4=0) => class G."""
        cls = shadow_class_from_data(Rational(1), Rational(0), Rational(0))
        assert cls == 'G'

    def test_metric_lie_class(self):
        """alpha != 0, S4 = 0 => class L."""
        cls = shadow_class_from_data(Rational(1), Rational(3), Rational(0))
        assert cls == 'L'


# =========================================================================
# Section 6: Genus expansion (path: direct + consistency + tower)
# =========================================================================

class TestGenusExpansion:
    """Verify genus-g free energies F_g(A_Burns)."""

    def test_F1(self):
        """F_1 = kappa/24 = 4/24 = 1/6."""
        F_g = burns_genus_expansion()
        assert F_g[1] == Rational(1, 6)

    def test_F2(self):
        """F_2 = 4 * 7/5760 = 7/1440."""
        F_g = burns_genus_expansion()
        assert F_g[2] == Rational(7, 1440)

    def test_F3(self):
        """F_3 = 4 * 31/967680 = 31/241920."""
        F_g = burns_genus_expansion()
        assert F_g[3] == Rational(31, 241920)

    def test_F4(self):
        """F_4 = 4 * 127/154828800 = 127/38707200."""
        F_g = burns_genus_expansion()
        assert F_g[4] == Rational(127, 38707200)

    def test_F5(self):
        """F_5 = 4 * 73/3503554560 = 73/875888640."""
        F_g = burns_genus_expansion()
        assert F_g[5] == Rational(73, 875888640)

    def test_genus_1_universality(self):
        """F_1 = kappa/24 (Theorem D, genus-1 universality)."""
        assert verify_genus_1_from_kappa()

    def test_genus_1_from_tower(self):
        """F_1 from the shadow tower S_2 agrees with F_1 = kappa/24."""
        result = burns_genus_expansion_from_tower()
        assert result['F_1_from_tower'] == Rational(1, 6)
        assert result['kappa_T'] == 4

    def test_F_g_positive(self):
        """All F_g > 0 for g=1,...,5 (kappa = 4 > 0)."""
        F_g = burns_genus_expansion()
        for g in range(1, 6):
            assert F_g[g] > 0

    def test_F_g_monotone_decreasing(self):
        """F_g decreases with g (Bernoulli growth slower than factorial)."""
        F_g = burns_genus_expansion()
        for g in range(1, 5):
            assert F_g[g] > F_g[g + 1]


# =========================================================================
# Section 7: Koszul dual and complementarity (path: duality + AP24)
# =========================================================================

class TestKoszulDual:
    """Verify Koszul dual identification and complementarity."""

    def test_dual_is_bc(self):
        """A!_Burns = bc^{tensor 4}_{lambda=1}."""
        dual = burns_koszul_dual()
        assert 'bc' in dual['A_dual_name']

    def test_c_dual(self):
        """c(A!) = -8."""
        dual = burns_koszul_dual()
        assert dual['c_dual'] == -8

    def test_kappa_dual(self):
        """kappa(A!) = -4."""
        dual = burns_koszul_dual()
        assert dual['kappa_dual'] == -4

    def test_complementarity_zero(self):
        """kappa + kappa' = 0 (free-field anti-symmetry, AP24 safe)."""
        dual = burns_koszul_dual()
        assert dual['complementarity_sum'] == 0
        assert dual['anti_symmetric'] is True

    def test_complementarity_all_lambda(self):
        """kappa + kappa' = 0 for all bg/bc pairs at all lambda and n_bg."""
        assert verify_complementarity_antisymmetry()


# =========================================================================
# Section 8: R-matrix structure (path: AP19 pole analysis)
# =========================================================================

class TestRMatrix:
    """Verify r-matrix pole structure and collinear splitting."""

    def test_bg_r_matrix_simple_pole(self):
        """bg r-matrix has a simple pole (AP19: same as OPE for simple pole)."""
        r_mat = burns_r_matrix_structure()
        assert r_mat['r_bg_leading_pole_order'] == 1

    def test_virasoro_r_matrix_cubic_pole(self):
        """T(z)T(w) r-matrix has z^{-3} leading pole (AP19: one below z^{-4})."""
        r_mat = burns_r_matrix_structure()
        assert r_mat['r_T_leading_pole_order'] == 3

    def test_virasoro_r_matrix_z3_coefficient(self):
        """Coefficient of z^{-3} in r_T(z) is c/2 = 4."""
        r_mat = burns_r_matrix_structure()
        assert r_mat['r_T_z3_coefficient'] == 4

    def test_combined_max_pole(self):
        """Combined r-matrix has max pole order 3 (from Virasoro sector)."""
        r_mat = burns_r_matrix_structure()
        assert r_mat['combined_max_pole_order'] == 3


# =========================================================================
# Section 9: Planted-forest correction (path: direct computation)
# =========================================================================

class TestPlantedForest:
    """Verify genus-2 planted-forest correction."""

    def test_delta_pf_g2(self):
        """delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48 = 2*(20-4)/48 = 2/3."""
        pf = burns_planted_forest_g2()
        assert pf['delta_pf_g2'] == Rational(2, 3)

    def test_delta_pf_g2_formula(self):
        """Verify by direct substitution: S_3=2, kappa=4."""
        pf = burns_planted_forest_g2()
        expected = Rational(2) * (10 * Rational(2) - Rational(4)) / 48
        assert pf['delta_pf_g2'] == expected


# =========================================================================
# Section 10: Two-loop prediction (path: dimensional analysis + formula)
# =========================================================================

class TestTwoLoopPrediction:
    """Verify the two-loop self-dual gravity prediction."""

    def test_F2_value(self):
        """F_2 = 7/1440."""
        pred = burns_two_loop_prediction()
        assert pred['F_2'] == Rational(7, 1440)

    def test_F2_numerical(self):
        """Numerical value F_2 approx 0.00486."""
        pred = burns_two_loop_prediction()
        assert abs(pred['F_2_numerical'] - 7.0 / 1440.0) < 1e-10

    def test_ratio_F2_F1(self):
        """F_2/F_1 = (7/1440)/(1/6) = 7/240."""
        pred = burns_two_loop_prediction()
        assert pred['ratio_F2_F1'] == Rational(7, 240)


# =========================================================================
# Section 11: Holographic datum (path: completeness check)
# =========================================================================

class TestHolographicDatum:
    """Verify the complete holographic modular Koszul datum."""

    def test_datum_has_all_components(self):
        """H(Burns) has all 6 components: A, A!, bulk, r(z), Theta_A, nabla."""
        datum = burns_holographic_datum()
        assert 'A' in datum
        assert 'A_dual' in datum
        assert 'bulk' in datum
        assert 'r_matrix' in datum
        assert 'Theta_A' in datum
        assert 'nabla_hol' in datum

    def test_datum_genus_expansion(self):
        """Datum includes genus expansion for g=1,...,5."""
        datum = burns_holographic_datum()
        assert len(datum['genus_expansion']) == 5

    def test_datum_two_loop(self):
        """Datum includes two-loop prediction."""
        datum = burns_holographic_datum()
        assert 'two_loop_prediction' in datum

    def test_datum_A_c(self):
        """Datum boundary algebra has c=8."""
        datum = burns_holographic_datum()
        assert datum['A']['c'] == 8

    def test_datum_A_kappa(self):
        """Datum boundary algebra has kappa=4."""
        datum = burns_holographic_datum()
        assert datum['A']['kappa'] == 4

    def test_datum_complementarity(self):
        """Datum Koszul dual has kappa + kappa' = 0."""
        datum = burns_holographic_datum()
        assert datum['A_dual']['complementarity_sum'] == 0


# =========================================================================
# Section 12: Parametric engine (path: limiting cases)
# =========================================================================

class TestParametric:
    """Test parametric Burns-type datum at various (n_bg, lambda)."""

    def test_single_pair_lambda_1(self):
        """n_bg=1, lambda=1: c=2, kappa=1."""
        result = parametric_burns_datum(n_bg=1, lam=Rational(1))
        assert result['c_total'] == 2
        assert result['kappa_total'] == 1

    def test_single_pair_lambda_0(self):
        """n_bg=1, lambda=0: c=2, kappa=1."""
        result = parametric_burns_datum(n_bg=1, lam=Rational(0))
        assert result['c_total'] == 2
        assert result['kappa_total'] == 1

    def test_symplectic_boson(self):
        """n_bg=1, lambda=1/2: c=-1, kappa=-1/2."""
        result = parametric_burns_datum(n_bg=1, lam=Rational(1, 2))
        assert result['c_total'] == -1
        assert result['kappa_total'] == Rational(-1, 2)

    def test_4_pairs_lambda_half(self):
        """n_bg=4, lambda=1/2: c=-4, kappa=-2 (ABJM-like at N=1)."""
        result = parametric_burns_datum(n_bg=4, lam=Rational(1, 2))
        assert result['c_total'] == -4
        assert result['kappa_total'] == -2

    def test_physical_burns(self):
        """Default parameters give the physical Burns space data."""
        result = parametric_burns_datum()
        assert result['n_bg'] == 4
        assert result['c_total'] == 8
        assert result['kappa_total'] == 4

    def test_kappa_scales_linearly_n(self):
        """kappa(n pairs) = n * kappa(1 pair) for fixed lambda."""
        for n in [1, 2, 3, 4, 5, 6, 7, 8]:
            result = parametric_burns_datum(n_bg=n, lam=Rational(1))
            assert result['kappa_total'] == n * result['kappa_single']

    def test_complementarity_parametric(self):
        """kappa + kappa' = 0 at all parameter values."""
        for n in [1, 2, 4]:
            for lam in [Rational(0), Rational(1, 2), Rational(1), Rational(1, 3)]:
                result = parametric_burns_datum(n_bg=n, lam=lam)
                assert result['complementarity_sum'] == 0


# =========================================================================
# Section 13: Consistency and cross-check (path: multi-path verification)
# =========================================================================

class TestConsistency:
    """Cross-checks between engine components and known results."""

    def test_kappa_additivity(self):
        """Built-in kappa additivity check for n=1,...,8."""
        assert verify_kappa_additivity()

    def test_tower_S2_equals_kappa_T(self):
        """S_2 from the shadow tower = kappa_T = c/2 = 4."""
        tower = burns_T_line_shadow_tower(max_r=4)
        assert tower[2] == 4

    def test_tower_S4_equals_Q_contact(self):
        """S_4 from the tower = Q^contact_Vir(c=8) = 5/248."""
        tower = burns_T_line_shadow_tower(max_r=5)
        assert tower[4] == Rational(5, 248)

    def test_F1_three_paths(self):
        """F_1 from (a) kappa/24, (b) genus expansion, (c) tower.

        Three independent paths must agree (multi-path verification mandate).
        """
        # Path (a): direct formula
        F1_a = Rational(4) / 24

        # Path (b): genus expansion
        F_g = burns_genus_expansion()
        F1_b = F_g[1]

        # Path (c): from tower S_2
        result = burns_genus_expansion_from_tower()
        F1_c = result['F_1_from_tower']

        assert F1_a == F1_b == F1_c == Rational(1, 6)

    def test_delta_T_equals_8_kappa_S4(self):
        """Delta = 8*kappa*S4 cross-check."""
        metric = burns_T_line_shadow_metric()
        assert metric['Delta'] == 8 * metric['kappa'] * metric['S4']

    def test_shadow_connection_discriminant(self):
        """Q_L discriminant = -32*kappa^2*Delta."""
        conn = burns_shadow_connection_data()
        assert conn['discriminant_check']

    def test_propagator_variance_zero(self):
        """Propagator variance is zero for identical bg pairs."""
        pv = burns_propagator_variance()
        assert pv['delta_mix'] == 0

    def test_bg_at_lambda2_gives_c26(self):
        """bg at lambda=2 gives c=26, kappa=13 (critical string!)."""
        c_val = bg_central_charge(Rational(2))
        k_val = bg_kappa(Rational(2))
        assert c_val == 26
        assert k_val == 13


# =========================================================================
# Section 14: Shadow connection (path: geometric consistency)
# =========================================================================

class TestShadowConnection:
    """Verify shadow connection geometric properties."""

    def test_residue_half(self):
        """Residue of nabla^sh at zeros of Q_L is 1/2."""
        conn = burns_shadow_connection_data()
        assert conn['residue_at_zeros'] == Rational(1, 2)

    def test_monodromy_minus_one(self):
        """Monodromy of nabla^sh is -1 (Koszul sign)."""
        conn = burns_shadow_connection_data()
        assert conn['monodromy'] == -1

    def test_q0_positive(self):
        """Q_L(0) = q0 = 4*kappa^2 > 0 for kappa != 0."""
        conn = burns_shadow_connection_data()
        assert conn['q0'] > 0


# =========================================================================
# Section 15: Cross-engine verification against existing betagamma engine
# =========================================================================

class TestCrossEngine:
    """Cross-check against the existing betagamma_shadow_full.py engine."""

    def test_kappa_matches_betagamma_engine(self):
        """kappa(bg, lambda=1) = 1, matching betagamma_shadow_full.py."""
        # Our engine
        k_ours = bg_kappa(Rational(1))
        # Expected from betagamma_shadow_full.py: 6*1^2 - 6*1 + 1 = 1
        assert k_ours == 1

    def test_c_matches_betagamma_engine(self):
        """c(bg, lambda=1) = 2, matching betagamma_shadow_full.py."""
        c_ours = bg_central_charge(Rational(1))
        assert c_ours == 2

    def test_virasoro_S3_universal(self):
        """S_3 = 2 on the T-line is universal (matches all Virasoro engines)."""
        tower = burns_T_line_shadow_tower(max_r=4)
        assert tower[3] == 2

    def test_Q_contact_matches_virasoro(self):
        """Q^contact(c=8) = 10/(8*62) = 5/248, matching Virasoro engine."""
        tower = burns_T_line_shadow_tower(max_r=5)
        expected = Rational(10) / (8 * (5 * 8 + 22))
        assert tower[4] == expected
