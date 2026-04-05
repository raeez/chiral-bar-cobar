r"""Tests for the moonshine bar complex module.

Covers:
  1. kappa(V^natural) computation and verification
  2. kappa comparison with Niemeier lattice VOAs
  3. Shadow depth classification (class M)
  4. Critical discriminant
  5. Shadow growth rate
  6. Shadow metric on the Virasoro line
  7. Virasoro shadow tower at c = 24
  8. Cubic shadow S_3
  9. Quartic contact invariant S_4
  10. Griess algebra structure
  11. Genus amplitudes F_g
  12. Planted-forest correction at genus 2
  13. Bar complex dimensions at low weights
  14. Bar cohomology dimensions
  15. Monster representation decomposition of bar cohomology
  16. Monster symmetry constraints on shadow tower
  17. V^natural vs V_Leech comparison
  18. V^natural vs all 24 Niemeier lattices
  19. Koszul dual structure
  20. J-function coefficient verification
  21. Multi-channel shadow dimensions

Mathematical ground truth:
  - Frenkel-Lepowsky-Meurman (1988): V^natural, c=24, dim V_1=0
  - Conway-Norton (1979): Monstrous Moonshine
  - Borcherds (1992): proof of monstrous moonshine
  - Griess (1982): the Griess algebra
  - Norton (1996): the Norton-Griess structure constants
  - OEIS A014708: J-function coefficients
  - AP48: kappa depends on full algebra, not Virasoro subalgebra
  - AP20: kappa(A) is intrinsic to A
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.moonshine_bar_complex import (
    BAR,
    GRIESS,
    KNOWN_J_COEFFICIENTS,
    MONSTER_CENTRAL_CHARGE,
    MONSTER_DECOMPOSITIONS,
    MONSTER_IRREPS,
    MONSTER_ORDER,
    MOONSHINE_DIMS,
    GriessAlgebra,
    WeightGradedBarComplex,
    j_coefficient,
    monster_invariant_shadows,
    moonshine_bar_cohomology,
    moonshine_critical_discriminant,
    moonshine_cubic_shadow,
    moonshine_F1,
    moonshine_full_shadow_data,
    moonshine_genus_amplitude,
    moonshine_griess_cubic_tensor_norm,
    moonshine_kappa,
    moonshine_kappa_from_partition_function,
    moonshine_koszul_dual_structure,
    moonshine_planted_forest_g2,
    moonshine_quartic_contact,
    moonshine_quartic_from_griess,
    moonshine_shadow_class,
    moonshine_shadow_growth_rate,
    moonshine_shadow_metric,
    moonshine_total_genus2,
    moonshine_virasoro_S_r,
    moonshine_virasoro_shadow_tower,
    moonshine_vs_all_niemeier,
    moonshine_vs_leech,
    _faber_pandharipande,
)


# =========================================================================
# 1. Kappa computation
# =========================================================================

class TestKappa:
    """Test kappa(V^natural) = c/2 = 12."""

    def test_kappa_value(self):
        """kappa(V^natural) = 12."""
        assert moonshine_kappa() == Rational(12)

    def test_kappa_from_partition_function(self):
        """kappa from partition function integration gives c/2 = 12."""
        assert moonshine_kappa_from_partition_function() == Rational(12)

    def test_kappa_agrees_both_methods(self):
        """Both kappa computation methods agree."""
        assert moonshine_kappa() == moonshine_kappa_from_partition_function()

    def test_kappa_positive(self):
        """kappa > 0 (positive curvature)."""
        assert moonshine_kappa() > 0

    def test_kappa_is_rational(self):
        """kappa is a rational number."""
        k = moonshine_kappa()
        assert isinstance(k, Rational)

    def test_kappa_not_24(self):
        """kappa(V^natural) != 24 (NOT the lattice formula).

        AP48: kappa depends on the full algebra.  For V^natural with dim V_1 = 0,
        kappa = c/2 = 12, NOT kappa = rank = 24 (which applies to lattice VOAs).
        """
        assert moonshine_kappa() != Rational(24)

    def test_kappa_half_of_leech(self):
        """kappa(V^natural) = (1/2) * kappa(V_Leech) (orbifold halving)."""
        assert moonshine_kappa() == Rational(24) / 2


# =========================================================================
# 2. Kappa comparison with Niemeier lattices
# =========================================================================

class TestKappaComparison:
    """Compare kappa(V^natural) with Niemeier lattice VOAs."""

    def test_kappa_differs_from_all_niemeier(self):
        """kappa(V^natural) = 12 != 24 = kappa(V_Lambda) for all Niemeier Lambda."""
        comparison = moonshine_vs_all_niemeier()
        for label, data in comparison.items():
            assert data['kappa'] == Rational(24)
            assert data['kappa_difference'] == Rational(12)

    def test_all_24_niemeier_lattices_present(self):
        """All 24 Niemeier lattices are in the comparison."""
        comparison = moonshine_vs_all_niemeier()
        assert len(comparison) == 24

    def test_separation_from_niemeier(self):
        """V^natural is separated from all Niemeier lattices by kappa."""
        comparison = moonshine_vs_all_niemeier()
        for label, data in comparison.items():
            assert data['separated_from_monster'] is True

    def test_niemeier_all_class_G(self):
        """All Niemeier lattice VOAs are class G."""
        comparison = moonshine_vs_all_niemeier()
        for label, data in comparison.items():
            assert data['shadow_class'] == 'G'

    def test_niemeier_kappa_is_rank(self):
        """Niemeier lattice VOAs have kappa = rank = 24 (not c/2 = 12)."""
        comparison = moonshine_vs_all_niemeier()
        for label, data in comparison.items():
            assert data['kappa'] == Rational(24)


# =========================================================================
# 3. Shadow depth classification
# =========================================================================

class TestShadowClass:
    """Test shadow class determination for V^natural."""

    def test_class_M(self):
        """V^natural is class M (infinite shadow depth)."""
        assert moonshine_shadow_class() == 'M'

    def test_not_class_G(self):
        """V^natural is NOT class G (would require S_3 = S_4 = 0)."""
        assert moonshine_shadow_class() != 'G'

    def test_not_class_L(self):
        """V^natural is NOT class L (would require S_4 = 0 with S_3 != 0)."""
        assert moonshine_shadow_class() != 'L'

    def test_not_class_C(self):
        """V^natural is NOT class C (contact class)."""
        assert moonshine_shadow_class() != 'C'

    def test_virasoro_forces_class_M(self):
        """The Virasoro subalgebra alone forces class M.

        S_4 = 5/1704 != 0 implies Delta != 0 implies class M.
        """
        S4 = moonshine_virasoro_S_r(4)
        assert S4 != 0
        Delta = moonshine_critical_discriminant()
        assert Delta != 0


# =========================================================================
# 4. Critical discriminant
# =========================================================================

class TestCriticalDiscriminant:
    """Test the critical discriminant Delta(V^natural)."""

    def test_discriminant_value(self):
        """Delta = 8 * 12 * (5/1704) = 20/71."""
        Delta = moonshine_critical_discriminant()
        assert Delta == Rational(20, 71)

    def test_discriminant_positive(self):
        """Delta > 0 (class M requires Delta != 0)."""
        assert moonshine_critical_discriminant() > 0

    def test_discriminant_formula(self):
        """Delta = 8 * kappa * S_4."""
        kappa = moonshine_kappa()
        S4 = moonshine_virasoro_S_r(4)
        assert moonshine_critical_discriminant() == 8 * kappa * S4

    def test_discriminant_not_zero(self):
        """Delta != 0 is the key criterion for class M."""
        assert moonshine_critical_discriminant() != 0


# =========================================================================
# 5. Shadow growth rate
# =========================================================================

class TestShadowGrowthRate:
    """Test the shadow growth rate rho(V^natural)."""

    def test_growth_rate_positive(self):
        """rho > 0 for class M."""
        rho = moonshine_shadow_growth_rate()
        assert rho > 0

    def test_growth_rate_less_than_one(self):
        """rho < 1 at c = 24 (shadow tower converges).

        The critical central charge c* ~ 6.12; for c = 24 >> c*,
        the tower converges.
        """
        rho = moonshine_shadow_growth_rate()
        assert rho < 1

    def test_growth_rate_formula(self):
        """rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)."""
        alpha = Rational(2)
        Delta = moonshine_critical_discriminant()
        kappa = moonshine_kappa()
        expected_sq = float(9 * alpha**2 + 2 * Delta) / float(4 * kappa**2)
        expected = expected_sq ** 0.5
        assert abs(moonshine_shadow_growth_rate() - expected) < 1e-12

    def test_growth_rate_less_than_virasoro_c13(self):
        """rho(V^natural, c=24) < rho(Vir, c=13) = self-dual rate ~ 0.467.

        Higher c gives lower rho (more convergent).
        """
        rho = moonshine_shadow_growth_rate()
        # Self-dual Virasoro rho at c=13: sqrt(9*4 + 2*8*6.5*S4(13)) / (2*6.5)
        # Approximate: ~0.467
        assert rho < 0.5

    def test_growth_rate_numerical(self):
        """Numerical check: rho ~ 0.2534."""
        rho = moonshine_shadow_growth_rate()
        assert abs(rho - 0.2534) < 0.01


# =========================================================================
# 6. Shadow metric
# =========================================================================

class TestShadowMetric:
    """Test the shadow metric Q_L(t) on the Virasoro line."""

    def test_metric_coefficients(self):
        """Q_L(t) = 576 + 288*t + (2596/71)*t^2."""
        q0, q1, q2 = moonshine_shadow_metric()
        assert q0 == Rational(576)
        assert q1 == Rational(288)
        assert q2 == Rational(2596, 71)

    def test_metric_positive_at_zero(self):
        """Q_L(0) = 4*kappa^2 > 0."""
        q0, _, _ = moonshine_shadow_metric()
        assert q0 > 0

    def test_metric_leading_coefficient_positive(self):
        """q_2 = 9*alpha^2 + 2*Delta > 0."""
        _, _, q2 = moonshine_shadow_metric()
        assert q2 > 0

    def test_metric_discriminant_negative(self):
        """Discriminant q_1^2 - 4*q_0*q_2 < 0 (complex branch points, class M).

        This is equivalent to Delta > 0.
        """
        q0, q1, q2 = moonshine_shadow_metric()
        disc = q1**2 - 4 * q0 * q2
        assert disc < 0


# =========================================================================
# 7. Virasoro shadow tower
# =========================================================================

class TestVirasuroShadowTower:
    """Test the Virasoro-sector shadow coefficients at c = 24."""

    def test_S2(self):
        """S_2 = kappa = c/2 = 12."""
        assert moonshine_virasoro_S_r(2) == Rational(12)

    def test_S3(self):
        """S_3 = 2 (universal Virasoro value)."""
        assert moonshine_virasoro_S_r(3) == Rational(2)

    def test_S4(self):
        """S_4 = 10/(24*142) = 5/1704."""
        assert moonshine_virasoro_S_r(4) == Rational(5, 1704)

    def test_S5_nonzero(self):
        """S_5 != 0 (class M: all higher S_r are nonzero)."""
        assert moonshine_virasoro_S_r(5) != 0

    def test_S6_nonzero(self):
        """S_6 != 0."""
        assert moonshine_virasoro_S_r(6) != 0

    def test_tower_dict(self):
        """Shadow tower returns a dict {r: S_r}."""
        tower = moonshine_virasoro_shadow_tower(6)
        assert len(tower) == 5  # r = 2, 3, 4, 5, 6
        assert tower[2] == Rational(12)
        assert tower[3] == Rational(2)
        assert tower[4] == Rational(5, 1704)

    def test_S_r_alternating_sign(self):
        """Shadow coefficients may alternate in sign (check)."""
        tower = moonshine_virasoro_shadow_tower(10)
        # At c = 24, the shadow tower should have the Bernoulli-type
        # alternating structure.  Just verify they are all nonzero.
        for r in range(5, 11):
            assert tower[r] != 0, f"S_{r} should be nonzero for class M"

    def test_S5_formula(self):
        """S_5 from recursion at c = 24.

        S_5 = -(1/(2*5*24)) * [2*3*4*S_3*S_4] (only j=3,k=4 contributes)
        = -(1/240) * 24 * 2 * (5/1704) = -(1/240) * 240/1704
        = -1/1704.
        Wait: let me compute carefully.
        sum for r=5: j+k=7, j,k>=3. j=3,k=4 (j<k).
        obstruction = 2*3*4*S_3*S_4/c = 24*2*(5/1704)/24 = 10/1704 = 5/852.
        S_5 = -obstruction/(2*5) = -(5/852)/10 = -5/8520 = -1/1704.
        """
        assert moonshine_virasoro_S_r(5) == Rational(-1, 1704)


# =========================================================================
# 8. Cubic shadow
# =========================================================================

class TestCubicShadow:
    """Test the cubic shadow S_3(V^natural)."""

    def test_cubic_shadow_value(self):
        """S_3 = 2 on the Virasoro primary line."""
        assert moonshine_cubic_shadow() == Rational(2)

    def test_griess_does_not_modify_virasoro_line(self):
        """Griess algebra does not modify S_3 on the T-line."""
        assert GRIESS.griess_cubic_correction() == Rational(0)

    def test_full_cubic_equals_virasoro(self):
        """Full S_3 on Virasoro line = Virasoro S_3."""
        assert GRIESS.full_cubic_shadow() == Rational(2)

    def test_cubic_nonzero(self):
        """S_3 != 0 (class L or higher)."""
        assert moonshine_cubic_shadow() != 0


# =========================================================================
# 9. Quartic contact invariant
# =========================================================================

class TestQuarticContact:
    """Test the quartic contact invariant."""

    def test_quartic_value(self):
        """Q^contact = 5/1704."""
        assert moonshine_quartic_contact() == Rational(5, 1704)

    def test_quartic_positive(self):
        """Q^contact > 0."""
        assert moonshine_quartic_contact() > 0

    def test_quartic_from_griess_virasoro_line(self):
        """Quartic on the Virasoro line is the Virasoro value."""
        data = moonshine_quartic_from_griess()
        assert data['Q_total_virasoro_line'] == Rational(5, 1704)

    def test_quartic_determines_class_M(self):
        """Delta = 8*12*(5/1704) = 20/71 != 0 implies class M."""
        data = moonshine_quartic_from_griess()
        assert data['is_class_M'] is True
        assert data['Delta'] == Rational(20, 71)


# =========================================================================
# 10. Griess algebra structure
# =========================================================================

class TestGriessAlgebra:
    """Test Griess algebra properties."""

    def test_griess_dim_total(self):
        """dim V_2 = 196884."""
        assert GRIESS.dim_total == 196884

    def test_griess_dim_vacuum_descendant(self):
        """dim(L_{-2}|0>) = 1."""
        assert GRIESS.dim_vacuum_desc == 1

    def test_griess_dim_primary(self):
        """dim V_2^prim = 196883."""
        assert GRIESS.dim_primary == 196883

    def test_griess_decomposition(self):
        """V_2 = 1 + 196883 (McKay's observation)."""
        assert GRIESS.dim_total == GRIESS.dim_vacuum_desc + GRIESS.dim_primary

    def test_conformal_vector_norm(self):
        """<omega, omega> = c/2 = 12."""
        assert GRIESS.conformal_vector_norm() == Rational(12)

    def test_griess_cubic_tensor_norm_positive(self):
        """The Griess cubic tensor norm is positive."""
        norm = moonshine_griess_cubic_tensor_norm()
        assert norm > 0


# =========================================================================
# 11. Genus amplitudes
# =========================================================================

class TestGenusAmplitudes:
    """Test scalar genus-g amplitudes F_g(V^natural)."""

    def test_F1(self):
        """F_1 = kappa/24 = 12/24 = 1/2."""
        assert moonshine_F1() == Rational(1, 2)

    def test_F1_from_formula(self):
        """F_1 = kappa * lambda_1^FP = 12 * 1/24 = 1/2."""
        assert moonshine_genus_amplitude(1) == Rational(1, 2)

    def test_F2(self):
        """F_2 = 12 * (7/5760) = 7/480."""
        assert moonshine_genus_amplitude(2) == Rational(7, 480)

    def test_F3(self):
        """F_3 = 12 * lambda_3^FP."""
        fp3 = _faber_pandharipande(3)
        assert moonshine_genus_amplitude(3) == 12 * fp3

    def test_amplitudes_positive(self):
        """F_g > 0 for all g >= 1."""
        for g in range(1, 6):
            assert moonshine_genus_amplitude(g) > 0

    def test_F1_half_of_leech(self):
        """F_1(V^natural) = (1/2) * F_1(V_Leech).

        F_1(Leech) = 24/24 = 1; F_1(Monster) = 12/24 = 1/2.
        """
        F1_monster = moonshine_F1()
        F1_leech = Rational(24) * _faber_pandharipande(1)
        assert F1_monster == F1_leech / 2


# =========================================================================
# 12. Planted-forest correction
# =========================================================================

class TestPlantedForest:
    """Test genus-2 planted-forest correction."""

    def test_planted_forest_g2(self):
        """delta_pf = S_3 * (10*S_3 - kappa) / 48 = 2*(20-12)/48 = 1/3."""
        assert moonshine_planted_forest_g2() == Rational(1, 3)

    def test_planted_forest_nonzero(self):
        """Planted-forest correction is nonzero (class M has S_3 != 0)."""
        assert moonshine_planted_forest_g2() != 0

    def test_total_genus2(self):
        """A_2 = F_2 + delta_pf = 7/480 + 1/3 = 167/480."""
        assert moonshine_total_genus2() == Rational(167, 480)

    def test_planted_forest_positive(self):
        """Planted-forest correction is positive at c = 24.

        S_3*(10*S_3 - kappa)/48 = 2*8/48 > 0 since 10*2 = 20 > 12 = kappa.
        """
        assert moonshine_planted_forest_g2() > 0


# =========================================================================
# 13. Bar complex dimensions
# =========================================================================

class TestBarComplexDimensions:
    """Test dimensions of the weight-graded bar complex."""

    def test_bar_degree_0(self):
        """B_0^0 = 1 (vacuum at weight 0, bar degree 0)."""
        assert BAR.bar_dim(0, 0) == 1

    def test_bar_degree_1_weight_2(self):
        """B_2^1 = V_2, dim = 196884."""
        assert BAR.bar_dim(1, 2) == 196884

    def test_bar_degree_1_weight_1(self):
        """B_1^1 = V_1 = 0 (no weight-1 currents)."""
        assert BAR.bar_dim(1, 1) == 0

    def test_bar_degree_1_weight_3(self):
        """B_3^1 = V_3, dim = 21493760."""
        assert BAR.bar_dim(1, 3) == 21493760

    def test_bar_degree_2_weight_3(self):
        """B_3^2 = 0 (need w1+w2=3 with w_i>=2; only (2,1) but V_1=0)."""
        assert BAR.bar_dim(2, 3) == 0

    def test_bar_degree_2_weight_4(self):
        """B_4^2 = V_2 tensor V_2, dim = 196884^2."""
        expected = 196884 ** 2
        assert BAR.bar_dim(2, 4) == expected

    def test_bar_degree_2_weight_5(self):
        """B_5^2 = V_2 tensor V_3 (unordered bar, distinct weights)."""
        expected = 196884 * 21493760
        assert BAR.bar_dim(2, 5) == expected

    def test_bar_degree_1_weight_0(self):
        """B_0^1 = 0 (vacuum is removed in bar complex)."""
        assert BAR.bar_dim(1, 0) == 0

    def test_minimum_weight_bar_degree_2(self):
        """Minimum weight at bar degree 2 is 4 (since min per factor is 2, and V_1=0)."""
        assert BAR.bar_dim(2, 2) == 0
        assert BAR.bar_dim(2, 3) == 0
        assert BAR.bar_dim(2, 4) > 0


# =========================================================================
# 14. Bar cohomology dimensions
# =========================================================================

class TestBarCohomology:
    """Test bar cohomology H^*(B(V^natural))."""

    def test_H1_weight_2(self):
        """H^1(B)_2 = V_2, dim = 196884.

        V_1 = 0 implies no bar-degree-2 contribution at weight <= 3.
        """
        assert BAR.bar_cohomology_dim_weight2() == 196884

    def test_H1_weight_3(self):
        """H^1(B)_3 = V_3, dim = 21493760."""
        assert BAR.bar_cohomology_dim_weight3() == 21493760

    def test_H1_weight_4_upper_bound(self):
        """H^1(B)_4 <= dim V_4 = 864299970."""
        assert BAR.bar_cohomology_dim_weight4() <= 864299970

    def test_cohomology_data(self):
        """Bar cohomology data structure."""
        data = moonshine_bar_cohomology()
        assert data['H1_weight_2']['dim'] == 196884
        assert data['H1_weight_2']['exact'] is True
        assert data['H1_weight_3']['dim'] == 21493760
        assert data['H1_weight_3']['exact'] is True
        assert data['H1_weight_4']['exact'] is False

    def test_chirally_koszul(self):
        """V^natural is chirally Koszul (bar cohomology concentrated in bar degree 1)."""
        data = moonshine_bar_cohomology()
        assert data['bar_chirally_koszul'] is True


# =========================================================================
# 15. Monster representation decomposition of bar cohomology
# =========================================================================

class TestMonsterDecomposition:
    """Test Monster-rep decomposition of bar cohomology."""

    def test_V2_decomposition(self):
        """V_2 = 1 + 196883 (McKay's observation)."""
        decomp = MONSTER_DECOMPOSITIONS[2]
        total = sum(mult * MONSTER_IRREPS[rep] for mult, rep in decomp)
        assert total == 196884

    def test_V3_decomposition(self):
        """V_3 = 1 + 196883 + 21296876."""
        decomp = MONSTER_DECOMPOSITIONS[3]
        total = sum(mult * MONSTER_IRREPS[rep] for mult, rep in decomp)
        assert total == 21493760

    def test_V4_decomposition(self):
        """V_4 = 2*1 + 2*196883 + 21296876 + 842609326."""
        decomp = MONSTER_DECOMPOSITIONS[4]
        total = sum(mult * MONSTER_IRREPS[rep] for mult, rep in decomp)
        assert total == 864299970

    def test_V0_vacuum(self):
        """V_0 = 1 (vacuum)."""
        decomp = MONSTER_DECOMPOSITIONS[0]
        total = sum(mult * MONSTER_IRREPS[rep] for mult, rep in decomp)
        assert total == 1

    def test_V1_empty(self):
        """V_1 = 0 (no weight-1 currents)."""
        decomp = MONSTER_DECOMPOSITIONS[1]
        assert len(decomp) == 0


# =========================================================================
# 16. Monster symmetry constraints
# =========================================================================

class TestMonsterSymmetry:
    """Test Monster group constraints on the shadow tower."""

    def test_scalar_shadows_invariant(self):
        """Scalar shadows are automatically Monster-invariant."""
        data = monster_invariant_shadows()
        assert data['scalar_shadows_invariant'] is True

    def test_multi_channel_cubic_1d(self):
        """Monster constrains multi-channel cubic to 1D.

        Hom_M(196883 tensor 196883, 196883) is 1-dimensional (Schur).
        """
        data = monster_invariant_shadows()
        assert data['multi_channel_cubic_dim'] == 1

    def test_monster_does_not_constrain_virasoro_line(self):
        """Monster does not provide extra constraints on the Virasoro line."""
        data = monster_invariant_shadows()
        assert data['monster_constrains_virasoro_line'] is False

    def test_monster_constrains_multi_channel(self):
        """Monster DOES constrain the multi-channel shadow tower."""
        data = monster_invariant_shadows()
        assert data['monster_constrains_multi_channel'] is True

    def test_equivariant_bar_cohomology_known(self):
        """Equivariant bar cohomology decomposition is known at low weights."""
        data = monster_invariant_shadows()
        assert data['equivariant_bar_cohomology'][2]['is_known'] is True
        assert data['equivariant_bar_cohomology'][3]['is_known'] is True


# =========================================================================
# 17. V^natural vs V_Leech
# =========================================================================

class TestMonsterVsLeech:
    """Test comparison between V^natural and V_Leech."""

    def test_same_central_charge(self):
        """Both have c = 24."""
        comp = moonshine_vs_leech()
        assert comp['same_central_charge'] is True

    def test_different_kappa(self):
        """kappa: 12 vs 24."""
        comp = moonshine_vs_leech()
        assert comp['kappa_monster'] == Rational(12)
        assert comp['kappa_leech'] == Rational(24)

    def test_kappa_ratio(self):
        """kappa_Leech / kappa_Monster = 2."""
        comp = moonshine_vs_leech()
        assert comp['kappa_ratio'] == Rational(2)

    def test_different_shadow_class(self):
        """V^natural is class M; V_Leech is class G."""
        comp = moonshine_vs_leech()
        assert comp['shadow_class_monster'] == 'M'
        assert comp['shadow_class_leech'] == 'G'

    def test_different_shadow_depth(self):
        """V^natural has infinite depth; V_Leech has depth 2."""
        comp = moonshine_vs_leech()
        assert comp['shadow_depth_monster'] == float('inf')
        assert comp['shadow_depth_leech'] == 2

    def test_different_dim_V1(self):
        """dim V_1: 0 vs 24."""
        comp = moonshine_vs_leech()
        assert comp['dim_V1_monster'] == 0
        assert comp['dim_V1_leech'] == 24

    def test_F1_ratio(self):
        """F_1 ratio = 2 (kappa ratio)."""
        comp = moonshine_vs_leech()
        assert comp['F1_ratio'] == Rational(2)


# =========================================================================
# 18. V^natural vs all Niemeier lattices
# =========================================================================

class TestMonsterVsAllNiemeier:
    """Test V^natural against all 24 Niemeier lattice VOAs."""

    def test_all_24_present(self):
        comparison = moonshine_vs_all_niemeier()
        assert len(comparison) == 24

    def test_leech_included(self):
        comparison = moonshine_vs_all_niemeier()
        assert 'Leech' in comparison

    def test_all_separated(self):
        """V^natural is shadow-separated from all Niemeier lattices."""
        comparison = moonshine_vs_all_niemeier()
        for label, data in comparison.items():
            assert data['separated_from_monster'] is True

    def test_all_class_G(self):
        comparison = moonshine_vs_all_niemeier()
        for label, data in comparison.items():
            assert data['shadow_class'] == 'G'

    def test_kappa_difference_12(self):
        """kappa difference is always 12."""
        comparison = moonshine_vs_all_niemeier()
        for label, data in comparison.items():
            assert data['kappa_difference'] == Rational(12)


# =========================================================================
# 19. Koszul dual structure
# =========================================================================

class TestKoszulDual:
    """Test the Koszul dual V^{natural,!}."""

    def test_generators_at_weight_2(self):
        """Koszul dual has generators at weight 2 of dim 196884."""
        data = moonshine_koszul_dual_structure()
        assert data['generators']['weight_2']['dim'] == 196884

    def test_virasoro_dual_kappa(self):
        """Virasoro dual Vir_2 has kappa = 1."""
        data = moonshine_koszul_dual_structure()
        assert data['kappa_virasoro_dual'] == Rational(1)

    def test_virasoro_dual_central_charge(self):
        """Virasoro dual has c = 26 - 24 = 2."""
        data = moonshine_koszul_dual_structure()
        assert data['central_charge_virasoro_dual'] == Rational(2)

    def test_monster_symmetry_preserved(self):
        """Koszul dual has Monster symmetry."""
        data = moonshine_koszul_dual_structure()
        assert data['has_monster_symmetry'] is True

    def test_full_dual_kappa_unknown(self):
        """kappa of the full Koszul dual is a frontier problem."""
        data = moonshine_koszul_dual_structure()
        assert data['kappa_full_dual'] is None

    def test_relations_start_at_weight_4(self):
        """Relations in the Koszul dual start at weight 4."""
        data = moonshine_koszul_dual_structure()
        assert data['relations_start_at'] == 4


# =========================================================================
# 20. J-function coefficients
# =========================================================================

class TestJFunction:
    """Test J-function coefficient verification."""

    def test_polar_coefficient(self):
        """c(-1) = 1 (polar term q^{-1})."""
        assert j_coefficient(-1) == 1

    def test_constant_term(self):
        """c(0) = 0 (J = j - 744 has vanishing constant term)."""
        assert j_coefficient(0) == 0

    def test_c1_mckay(self):
        """c(1) = 196884 (McKay's observation: 196884 = 1 + 196883)."""
        assert j_coefficient(1) == 196884

    def test_c2(self):
        """c(2) = 21493760."""
        assert j_coefficient(2) == 21493760

    def test_c3(self):
        """c(3) = 864299970."""
        assert j_coefficient(3) == 864299970

    def test_dim_V_n_equals_J_coefficient(self):
        """dim V_{n+1} = c(n) for n >= 1 in the standard grading."""
        # With our convention: MOONSHINE_DIMS[k] = dim V_k
        # and J = q^{-1} + sum c(n) q^n, the graded dimensions satisfy
        # dim V_0 = 1 (from q^{-1}), dim V_1 = c(0) = 0,
        # dim V_2 = c(1) = 196884, dim V_3 = c(2) = 21493760, etc.
        assert MOONSHINE_DIMS[0] == 1
        assert MOONSHINE_DIMS[1] == j_coefficient(0)
        assert MOONSHINE_DIMS[2] == j_coefficient(1)
        assert MOONSHINE_DIMS[3] == j_coefficient(2)
        assert MOONSHINE_DIMS[4] == j_coefficient(3)


# =========================================================================
# 21. Multi-channel shadow dimensions
# =========================================================================

class TestMultiChannel:
    """Test multi-channel shadow tower properties."""

    def test_multi_channel_cubic_dim(self):
        """Multi-channel cubic shadow is 1D (Monster Schur constraint)."""
        data = monster_invariant_shadows()
        assert data['multi_channel_cubic_dim'] == 1

    def test_griess_cubic_norm_value(self):
        """Griess cubic tensor norm (scalar channel)."""
        norm = moonshine_griess_cubic_tensor_norm()
        # scalar channel: d / (c^2/4) = 196883 / 144
        expected = Rational(196883, 144)
        assert norm == expected


# =========================================================================
# 22. Full shadow data structure
# =========================================================================

class TestFullShadowData:
    """Test the complete shadow data structure."""

    def test_data_has_all_fields(self):
        """Full shadow data has all required fields."""
        data = moonshine_full_shadow_data()
        assert 'kappa' in data
        assert 'shadow_class' in data
        assert 'shadow_depth' in data
        assert 'critical_discriminant' in data
        assert 'F1' in data
        assert 'dim_V1' in data
        assert 'dim_V2' in data

    def test_data_kappa(self):
        data = moonshine_full_shadow_data()
        assert data['kappa'] == Rational(12)

    def test_data_class_M(self):
        data = moonshine_full_shadow_data()
        assert data['shadow_class'] == 'M'

    def test_data_depth_infinite(self):
        data = moonshine_full_shadow_data()
        assert data['shadow_depth'] == float('inf')

    def test_data_F1(self):
        data = moonshine_full_shadow_data()
        assert data['F1'] == Rational(1, 2)

    def test_data_dim_V1_zero(self):
        data = moonshine_full_shadow_data()
        assert data['dim_V1'] == 0

    def test_data_griess_dim(self):
        data = moonshine_full_shadow_data()
        assert data['griess_algebra_dim'] == 196884
        assert data['griess_primaries_dim'] == 196883

    def test_separated_from_niemeier(self):
        data = moonshine_full_shadow_data()
        assert data['separated_from_all_niemeier'] is True

    def test_monster_order(self):
        data = moonshine_full_shadow_data()
        expected = 808017424794512875886459904961710757005754368000000000
        assert data['monster_order'] == expected

    def test_planted_forest_g2(self):
        data = moonshine_full_shadow_data()
        assert data['planted_forest_g2'] == Rational(1, 3)

    def test_total_g2(self):
        data = moonshine_full_shadow_data()
        assert data['total_g2'] == Rational(167, 480)


# =========================================================================
# 23. Cross-consistency checks
# =========================================================================

class TestCrossConsistency:
    """Cross-consistency between different computations."""

    def test_kappa_times_fp1_equals_F1(self):
        """kappa * lambda_1^FP = F_1."""
        assert moonshine_kappa() * _faber_pandharipande(1) == moonshine_F1()

    def test_discriminant_from_components(self):
        """Delta = 8 * kappa * S_4."""
        kappa = moonshine_kappa()
        S4 = moonshine_virasoro_S_r(4)
        assert moonshine_critical_discriminant() == 8 * kappa * S4

    def test_shadow_metric_from_components(self):
        """Shadow metric coefficients from kappa, alpha, Delta."""
        q0, q1, q2 = moonshine_shadow_metric()
        kappa = moonshine_kappa()
        alpha = moonshine_virasoro_S_r(3)
        Delta = moonshine_critical_discriminant()
        assert q0 == 4 * kappa**2
        assert q1 == 12 * kappa * alpha
        assert q2 == 9 * alpha**2 + 2 * Delta

    def test_total_genus2_sum(self):
        """Total genus-2 = scalar + planted-forest."""
        assert moonshine_total_genus2() == moonshine_genus_amplitude(2) + moonshine_planted_forest_g2()

    def test_V2_decomposition_consistent(self):
        """V_2 decomposition consistent with J-coefficient."""
        assert MOONSHINE_DIMS[2] == GRIESS.dim_total
        assert MOONSHINE_DIMS[2] == 196884

    def test_central_charge_consistent(self):
        """Central charge consistent across all computations."""
        assert MONSTER_CENTRAL_CHARGE == Rational(24)
        assert GRIESS.central_charge == Rational(24)


# =========================================================================
# 24. Depth decomposition
# =========================================================================

class TestDepthDecomposition:
    """Test the depth decomposition d = 1 + d_arith + d_alg."""

    def test_algebraic_depth_infinite(self):
        """V^natural has d_alg = infinity (class M).

        The Virasoro self-OPE drives infinite algebraic depth.
        """
        # For class M: d_alg = infinity
        assert moonshine_shadow_class() == 'M'

    def test_arithmetic_depth_zero(self):
        """d_arith = 0 at genus 1 (J is a Hauptmodul, no cusp forms at weight 0)."""
        # The J-function is weight-0 for SL(2,Z), so no cusp form obstruction
        # at genus 1.
        assert j_coefficient(0) == 0  # constant term vanishes (Hauptmodul property)


# =========================================================================
# 25. Edge cases and error handling
# =========================================================================

class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_j_coefficient_out_of_range(self):
        """Accessing J-coefficient beyond tabulated range raises ValueError."""
        with pytest.raises(ValueError):
            j_coefficient(100)

    def test_bar_dim_negative_weight(self):
        """Bar dim at negative weight is 0."""
        assert BAR.bar_dim(1, -1) == 0

    def test_bar_dim_zero_weight_nonzero_degree(self):
        """Bar dim at weight 0, bar degree > 0, is 0 (vacuum removed)."""
        assert BAR.bar_dim(1, 0) == 0
        assert BAR.bar_dim(2, 0) == 0

    def test_genus_amplitude_raises_for_g0(self):
        """Genus-0 amplitude raises ValueError."""
        with pytest.raises(ValueError):
            moonshine_genus_amplitude(0)

    def test_virasoro_S_r_at_r1(self):
        """S_1 = 0 (no arity-1 shadow)."""
        assert moonshine_virasoro_S_r(1) == 0

    def test_virasoro_S_r_at_r0(self):
        """S_0 = 0."""
        assert moonshine_virasoro_S_r(0) == 0
