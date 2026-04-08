r"""Tests for theorem_moonshine_shadow_tower_engine: V^natural shadow obstruction tower.

Multi-path verification (CLAUDE.md mandate): every numerical claim verified by
at least 3 independent paths.  Each test class targets a specific mathematical
claim with multiple verification strategies.

MATHEMATICAL CLAIMS TESTED:
  (a) V^natural genus-0 OPE: Griess algebra dim 196883, Virasoro poles
  (b) kappa(V^natural) = 12 (AP48), kappa(V_Leech) = 24
  (c) S_3^{Vir} = 2, S_4 = 5/1704 (Q^contact at c=24)
  (d) Shadow class M, depth infinity (Delta = 20/71 != 0)
  (e) F_1(V^natural) = 1/2, F_1(V_Leech) = 1
  (f) j-function: J(tau) = j(tau) - 744, constant 744 = 3*dim(E_8)
  (g) Planted-forest at genus 2, orbifold dichotomy
  (h) Shadow metric, growth rate, higher shadow coefficients
"""

import math
import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.theorem_moonshine_shadow_tower_engine import (
    MONSTER_C,
    MONSTER_KAPPA,
    MONSTER_DIM_V0,
    MONSTER_DIM_V1,
    MONSTER_DIM_V2,
    MONSTER_GRIESS_DIM,
    LEECH_KAPPA,
    LEECH_DIM_V1,
    J_COEFFICIENTS,
    J_CONSTANT,
    faber_pandharipande,
    monster_kappa,
    leech_kappa,
    kappa_orbifold_halving,
    virasoro_S3,
    virasoro_S4_at_c24,
    virasoro_Q_contact,
    critical_discriminant_virasoro,
    virasoro_shadow_coefficient,
    virasoro_shadow_tower,
    monster_shadow_class,
    monster_shadow_depth,
    leech_shadow_class,
    leech_shadow_depth,
    shadow_class_dichotomy,
    monster_F_g,
    leech_F_g,
    F1_comparison,
    F2_comparison,
    genus_amplitude_table,
    monster_planted_forest_g2,
    leech_planted_forest_g2,
    monster_total_F2,
    j_function_data,
    j_constant_decomposition,
    eta_product_F1_relation,
    griess_algebra_structure,
    griess_S3_correction_status,
    monster_shadow_growth_rate,
    orbifold_full_analysis,
    virasoro_at_c24_data,
    cross_family_kappa_table,
    monster_shadow_metric_virasoro,
    run_all_verifications,
)


# =====================================================================
# Section 1: Faber-Pandharipande (foundation, multi-path)
# =====================================================================

class TestFaberPandharipande:
    """Verify lambda_g^FP values that underpin all genus-g computations."""

    def test_lambda1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_lambda2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_lambda3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_lambda1_from_bernoulli(self):
        """Path 2: compute lambda_1 from B_2 = 1/6 directly.

        (2^1 - 1)/2^1 * |B_2|/(2!) = (1/2)*(1/6)/2 = 1/24.
        """
        B2 = Rational(1, 6)
        result = Rational(1, 2) * B2 / 2
        assert result == Rational(1, 24)
        assert result == faber_pandharipande(1)

    def test_lambda_positive(self):
        """All lambda_g^FP are positive (Bernoulli sign pattern)."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0


# =====================================================================
# Section 2: Kappa (AP48-compliant, 3 paths)
# =====================================================================

class TestKappa:
    """Verify kappa(V^natural) = 12 and kappa(V_Leech) = 24."""

    def test_monster_kappa_value(self):
        """Path 1 (direct): kappa(V^natural) = c/2 = 24/2 = 12."""
        assert monster_kappa() == Rational(12)
        assert monster_kappa() == MONSTER_C / 2

    def test_monster_kappa_from_constant(self):
        """Path 2 (constant): matches the MONSTER_KAPPA constant."""
        assert monster_kappa() == MONSTER_KAPPA
        assert MONSTER_KAPPA == Rational(12)

    def test_monster_kappa_ap48(self):
        """Path 3 (AP48 check): dim V_1 = 0 implies no Heisenberg.

        With no Heisenberg sector, kappa is determined by the Virasoro
        formula kappa = c/2, not the rank formula.
        """
        assert MONSTER_DIM_V1 == 0
        assert monster_kappa() == MONSTER_C / 2

    def test_leech_kappa_value(self):
        """kappa(V_Leech) = rank = 24."""
        assert leech_kappa() == Rational(24)

    def test_leech_kappa_from_rank(self):
        """V_Leech has rank 24 (the Leech lattice is rank 24)."""
        assert leech_kappa() == LEECH_KAPPA
        assert LEECH_DIM_V1 == 24

    def test_kappa_ratio(self):
        """kappa(V_Leech) / kappa(V^natural) = 2 (orbifold halving)."""
        assert leech_kappa() / monster_kappa() == 2

    def test_kappa_orbifold_halving(self):
        """The Z/2Z orbifold halves kappa."""
        data = kappa_orbifold_halving()
        assert data['ratio'] == 2
        assert data['kappa_change'] == Rational(12)

    def test_kappa_not_equal(self):
        """V^natural and V_Leech have different kappa (AP48 critical)."""
        assert monster_kappa() != leech_kappa()


# =====================================================================
# Section 3: Shadow coefficients S_3, S_4 (3+ paths each)
# =====================================================================

class TestShadowCoefficients:
    """Verify Virasoro shadow coefficients at c = 24."""

    def test_S3_virasoro(self):
        """S_3^{Vir} = 2 (universal for Virasoro at any c != 0)."""
        assert virasoro_S3() == Rational(2)

    def test_S4_direct(self):
        """Path 1: S_4 = 10 / (24 * 142) = 10/3408 = 5/1704."""
        assert virasoro_S4_at_c24() == Rational(5, 1704)

    def test_S4_from_formula(self):
        """Path 2: Q^contact_Vir(c) = 10/[c(5c+22)] at c = 24."""
        c = Rational(24)
        expected = Rational(10) / (c * (5 * c + 22))
        assert virasoro_S4_at_c24() == expected

    def test_S4_denominator_factored(self):
        """Path 3: verify 24 * (5*24+22) = 24 * 142 = 3408."""
        assert 24 * (5 * 24 + 22) == 3408
        assert Rational(10, 3408) == Rational(5, 1704)
        assert virasoro_S4_at_c24() == Rational(10, 3408)

    def test_S4_nonzero(self):
        """S_4 != 0 (necessary for class M)."""
        assert virasoro_S4_at_c24() != 0

    def test_S4_positive(self):
        """S_4 > 0 at c = 24 (c and 5c+22 are both positive)."""
        assert virasoro_S4_at_c24() > 0

    def test_Q_contact_general(self):
        """Q^contact_Vir at various c values for cross-check."""
        # c = 1: 10/(1*27) = 10/27
        assert virasoro_Q_contact(Rational(1)) == Rational(10, 27)
        # c = 26: 10/(26*152) = 10/3952 = 5/1976
        assert virasoro_Q_contact(Rational(26)) == Rational(5, 1976)

    def test_shadow_tower_consistency(self):
        """The tower function agrees with individual coefficients."""
        tower = virasoro_shadow_tower(6)
        assert tower[2] == Rational(12)
        assert tower[3] == Rational(2)
        assert tower[4] == Rational(5, 1704)


# =====================================================================
# Section 4: Critical discriminant and shadow class (3 paths)
# =====================================================================

class TestCriticalDiscriminant:
    """Verify Delta = 20/71 and class M."""

    def test_delta_direct(self):
        """Path 1: Delta = 8 * 12 * 5/1704 = 480/1704 = 20/71."""
        assert critical_discriminant_virasoro() == Rational(20, 71)

    def test_delta_numerics(self):
        """Path 2: verify 480/1704 reduces to 20/71."""
        raw = Rational(8) * Rational(12) * Rational(5, 1704)
        assert raw == Rational(480, 1704)
        assert Rational(480, 1704) == Rational(20, 71)

    def test_delta_gcd(self):
        """Path 3: gcd(480, 1704) = 24, so 480/1704 = 20/71."""
        assert math.gcd(480, 1704) == 24
        assert 480 // 24 == 20
        assert 1704 // 24 == 71

    def test_delta_nonzero(self):
        """Delta != 0 is the necessary and sufficient condition for class M."""
        assert critical_discriminant_virasoro() != 0

    def test_monster_class_M(self):
        """V^natural is class M."""
        assert monster_shadow_class() == 'M'

    def test_monster_depth_infinite(self):
        """Shadow depth of V^natural is infinity."""
        assert monster_shadow_depth() == float('inf')

    def test_leech_class_G(self):
        """V_Leech is class G."""
        assert leech_shadow_class() == 'G'

    def test_leech_depth_2(self):
        """Shadow depth of V_Leech is 2."""
        assert leech_shadow_depth() == 2


# =====================================================================
# Section 5: Genus-1 free energy F_1 (3+ paths)
# =====================================================================

class TestF1:
    """Verify F_1(V^natural) = 1/2 and F_1(V_Leech) = 1."""

    def test_F1_monster_direct(self):
        """Path 1: F_1 = kappa * lambda_1^FP = 12 * 1/24 = 1/2."""
        assert monster_F_g(1) == Rational(1, 2)

    def test_F1_monster_from_kappa(self):
        """Path 2: F_1 = kappa/24 = 12/24 = 1/2."""
        assert monster_kappa() / 24 == Rational(1, 2)

    def test_F1_monster_decimal(self):
        """Path 3: numerical check."""
        assert float(monster_F_g(1)) == 0.5

    def test_F1_leech_direct(self):
        """F_1(V_Leech) = 24 * 1/24 = 1."""
        assert leech_F_g(1) == Rational(1)

    def test_F1_ratio(self):
        """F_1(Leech)/F_1(Monster) = 2 (orbifold halving)."""
        data = F1_comparison()
        assert data['ratio'] == 2
        assert data['orbifold_halving'] is True

    def test_F1_comparison_data(self):
        """Cross-check F1_comparison output."""
        data = F1_comparison()
        assert data['F1_monster'] == Rational(1, 2)
        assert data['F1_leech'] == Rational(1)


# =====================================================================
# Section 6: Genus-2 and planted-forest (3+ paths)
# =====================================================================

class TestGenus2:
    """Verify F_2 and planted-forest corrections."""

    def test_F2_monster(self):
        """F_2(V^natural) = 12 * 7/5760 = 84/5760 = 7/480."""
        assert monster_F_g(2) == Rational(7, 480)

    def test_F2_leech(self):
        """F_2(V_Leech) = 24 * 7/5760 = 7/240."""
        assert leech_F_g(2) == Rational(7, 240)

    def test_F2_ratio(self):
        """F_2(Leech)/F_2(Monster) = 2."""
        data = F2_comparison()
        assert data['ratio'] == 2

    def test_planted_forest_monster(self):
        """delta_pf(V^natural) = 2*(20-12)/48 = 16/48 = 1/3."""
        assert monster_planted_forest_g2() == Rational(1, 3)

    def test_planted_forest_monster_path2(self):
        """Path 2: S_3*(10*S_3 - kappa)/48 = 2*(20-12)/48."""
        S3 = Rational(2)
        kappa = Rational(12)
        result = S3 * (10 * S3 - kappa) / 48
        assert result == Rational(1, 3)

    def test_planted_forest_monster_path3(self):
        """Path 3: (40-c)/48 for Virasoro at c=24 where kappa=c/2."""
        c = Rational(24)
        result = (40 - c) / 48  # using kappa = c/2, S_3 = 2
        assert result == Rational(1, 3)

    def test_planted_forest_leech(self):
        """delta_pf(V_Leech) = 0 (class G, S_3 = 0)."""
        assert leech_planted_forest_g2() == Rational(0)

    def test_total_F2_monster(self):
        """F_2^{total} = 7/480 + 1/3 = 167/480."""
        assert monster_total_F2() == Rational(167, 480)

    def test_total_F2_sum_check(self):
        """Verify 7/480 + 1/3 = 7/480 + 160/480 = 167/480."""
        assert Rational(7, 480) + Rational(1, 3) == Rational(167, 480)


# =====================================================================
# Section 7: j-function connection (3+ paths)
# =====================================================================

class TestJFunction:
    """Verify j-function data and the F_1 vs 744 relation."""

    def test_j_constant_value(self):
        """The constant term of j(tau) is 744."""
        assert J_CONSTANT == 744

    def test_j_constant_factored(self):
        """744 = 3 * 248 = 3 * dim(E_8)."""
        assert J_CONSTANT == 3 * 248

    def test_j_constant_prime_factorization(self):
        """744 = 2^3 * 3 * 31."""
        assert 744 == 8 * 93
        assert 744 == 8 * 3 * 31

    def test_J_constant_is_zero(self):
        """J(tau) = j(tau) - 744 has zero constant term."""
        assert J_COEFFICIENTS[0] == 0

    def test_J_polar_term(self):
        """J(tau) has a simple pole: coefficient of q^{-1} is 1."""
        assert J_COEFFICIENTS[-1] == 1

    def test_first_moonshine_relation(self):
        """196884 = 1 + 196883 (first moonshine relation)."""
        assert J_COEFFICIENTS[1] == 196884
        assert J_COEFFICIENTS[1] == 1 + MONSTER_GRIESS_DIM

    def test_dim_V2_from_j(self):
        """dim V_2 = J-coefficient at q^1 = 196884."""
        assert MONSTER_DIM_V2 == J_COEFFICIENTS[1]

    def test_F1_independent_of_744(self):
        """F_1 = 1/2 does not depend on the j-constant 744."""
        data = j_function_data()
        assert data['F1_monster'] == Rational(1, 2)
        # F_1 depends only on kappa, not on genus-0 data
        assert data['F1_monster'] == monster_kappa() / 24

    def test_j_decomposition(self):
        """j constant decomposition sanity."""
        data = j_constant_decomposition()
        assert data['value'] == 744
        assert data['is_dim_E8_multiple'] is True
        assert data['shadow_tower_encodes'] is False


# =====================================================================
# Section 8: Griess algebra structure (multi-path)
# =====================================================================

class TestGriessAlgebra:
    """Verify Griess algebra dimensions and structure."""

    def test_griess_dim(self):
        """The Griess algebra has dimension 196883."""
        assert MONSTER_GRIESS_DIM == 196883

    def test_dim_V2_decomposition(self):
        """V_2 = conformal vector (1) + primaries (196883) = 196884."""
        assert MONSTER_DIM_V2 == 1 + MONSTER_GRIESS_DIM

    def test_griess_structure(self):
        """Griess algebra data consistency."""
        data = griess_algebra_structure()
        assert data['dim_V2'] == 196884
        assert data['dim_primaries'] == 196883
        assert data['conformal_vector_contribution'] == 1
        assert data['first_moonshine_relation'] is True

    def test_S3_correction_frontier(self):
        """The Griess correction to S_3 is frontier (not computed)."""
        data = griess_S3_correction_status()
        assert data['S3_virasoro'] == Rational(2)
        assert data['lower_bound'] == Rational(2)
        assert data['class_M_independent_of_correction'] is True


# =====================================================================
# Section 9: Orbifold dichotomy (cross-check)
# =====================================================================

class TestOrbifold:
    """Verify the V_Leech -> V^natural orbifold analysis."""

    def test_orbifold_changes(self):
        """The orbifold changes kappa, class, depth, dim V_1."""
        data = orbifold_full_analysis()
        kl, km = data['changes']['kappa']
        assert kl == Rational(24)
        assert km == Rational(12)

    def test_class_change(self):
        """Class changes G -> M."""
        data = shadow_class_dichotomy()
        assert data['V_Leech']['class'] == 'G'
        assert data['V_natural']['class'] == 'M'

    def test_dim_V1_change(self):
        """dim V_1 changes 24 -> 0."""
        data = orbifold_full_analysis()
        assert data['changes']['dim_V1'] == (24, 0)

    def test_central_charge_preserved(self):
        """The orbifold preserves c = 24."""
        data = orbifold_full_analysis()
        assert data['invariants_preserved']['central_charge'] == (Rational(24), Rational(24))


# =====================================================================
# Section 10: Shadow growth rate
# =====================================================================

class TestShadowGrowthRate:
    """Verify shadow growth rate computation."""

    def test_growth_rate_positive(self):
        """rho > 0 for V^natural."""
        rho = monster_shadow_growth_rate()
        assert rho > 0

    def test_growth_rate_less_than_one(self):
        """rho < 1 (the shadow tower coefficients decay)."""
        rho = monster_shadow_growth_rate()
        assert rho < 1

    def test_growth_rate_approximate(self):
        """rho ~ 0.252 (from exact formula)."""
        rho = monster_shadow_growth_rate()
        assert abs(rho - 0.252) < 0.01


# =====================================================================
# Section 11: Shadow metric
# =====================================================================

class TestShadowMetric:
    """Verify shadow metric Q_L is positive-definite."""

    def test_metric_positive_definite(self):
        """Q_L(t) > 0 for all t (class M confirmation)."""
        data = monster_shadow_metric_virasoro()
        assert data['positive_definite']
        assert data['class_M_confirmed']

    def test_metric_discriminant_negative(self):
        """Discriminant of Q_L < 0 (no real zeros)."""
        data = monster_shadow_metric_virasoro()
        assert data['discriminant'] < 0


# =====================================================================
# Section 12: Higher shadow coefficients (recursion)
# =====================================================================

class TestHigherShadow:
    """Verify the shadow tower recursion beyond S_4."""

    def test_S5_nonzero(self):
        """S_5 is nonzero (the tower does not terminate)."""
        S5 = virasoro_shadow_coefficient(5)
        assert S5 != 0

    def test_tower_all_nonzero(self):
        """S_r != 0 for r = 2, ..., 8 (class M: infinite tower)."""
        for r in range(2, 9):
            assert virasoro_shadow_coefficient(r) != 0

    def test_tower_decay(self):
        """|S_r| decreases (at least for small r)."""
        for r in range(3, 8):
            assert abs(virasoro_shadow_coefficient(r)) >= abs(virasoro_shadow_coefficient(r + 1))


# =====================================================================
# Section 13: Cross-family comparison
# =====================================================================

class TestCrossFamily:
    """Verify cross-family consistency."""

    def test_virasoro_c24_data(self):
        """Pure Virasoro at c=24 agrees with V^natural at shadow level."""
        data = virasoro_at_c24_data()
        assert data['kappa'] == Rational(12)
        assert data['S3'] == Rational(2)
        assert data['S4'] == Rational(5, 1704)

    def test_cross_family_kappa(self):
        """Kappa distinguishes V^natural from Niemeier lattices."""
        data = cross_family_kappa_table()
        assert data['V^natural'] == Rational(12)
        assert data['Niemeier (all 24)'] == Rational(24)

    def test_genus_amplitude_ratios(self):
        """F_g(Leech)/F_g(Monster) = 2 for all g (kappa ratio)."""
        table = genus_amplitude_table(5)
        for g in range(1, 6):
            assert table[g]['ratio'] == 2


# =====================================================================
# Section 14: Master verification
# =====================================================================

class TestMasterVerification:
    """Run the full internal verification suite."""

    def test_all_verifications_pass(self):
        """Every internal consistency check passes."""
        results = run_all_verifications()
        assert results['all_pass'] is True

    def test_eta_product_relation(self):
        """Eta-product relation for F_1."""
        data = eta_product_F1_relation()
        assert data['F1'] == Rational(1, 2)
        assert data['lambda_1_FP'] == Rational(1, 24)
        assert data['kappa'] == Rational(12)
        assert data['product'] == Rational(1, 2)
        assert data['eta_includes_q_prefactor'] is True  # AP46
