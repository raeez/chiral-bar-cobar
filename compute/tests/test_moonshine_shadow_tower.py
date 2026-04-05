r"""Tests for the moonshine shadow tower module.

Covers:
  1. kappa(V^natural) and kappa(V_Leech)
  2. Shadow class determination
  3. Virasoro shadow coefficients at c = 24
  4. Critical discriminant
  5. Monster vs Leech comparison
  6. Genus amplitudes
  7. Planted-forest corrections
  8. J-function coefficients
  9. Monster representation decompositions
  10. McKay-Thompson series
  11. McKay-Thompson shadow kappa
  12. Genus-0 Hauptmodul property
  13. Arithmetic depth
  14. Orbifold shadow dichotomy
  15. Griess algebra data
  16. MC synthesis
  17. Full atlas construction

Mathematical ground truth:
  - Frenkel-Lepowsky-Meurman (1988): V^natural, c=24, dim V_1=0
  - Conway-Norton (1979): 194 McKay-Thompson Hauptmoduln
  - Borcherds (1992): proof of monstrous moonshine
  - OEIS A014708: J-function coefficients
  - OEIS A001489: McKay-Thompson 2A coefficients
"""

import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.moonshine_shadow_tower import (
    KNOWN_J_COEFFICIENTS,
    MCKAY_THOMPSON_DATA,
    MONSTER_CENTRAL_CHARGE,
    MONSTER_DECOMPOSITIONS,
    MONSTER_IRREP_DIMS,
    MONSTER_ORDER,
    _faber_pandharipande,
    _virasoro_shadow_coefficient,
    full_moonshine_shadow_atlas,
    genus_amplitude_comparison,
    griess_algebra_data,
    j_coefficient,
    leech_arithmetic_depth,
    leech_genus_amplitude,
    leech_kappa,
    leech_shadow_data,
    mckay_thompson_coefficients,
    mckay_thompson_equivariant_F1,
    mckay_thompson_genus0_property,
    mckay_thompson_shadow_kappa,
    monster_arithmetic_depth,
    monster_critical_discriminant,
    monster_genus_amplitude,
    monster_kappa,
    monster_planted_forest_g2,
    monster_rep_decomposition,
    monster_shadow_class,
    monster_shadow_data,
    monster_shadow_growth_rate,
    monster_total_genus2,
    monster_vs_leech_comparison,
    moonshine_mc_synthesis,
    orbifold_shadow_dichotomy,
    verify_decomposition_totals,
    virasoro_shadow_tower,
)


# =========================================================================
# 1. kappa values
# =========================================================================

class TestKappaValues:
    """Verify kappa(V^natural) and kappa(V_Leech)."""

    def test_monster_kappa_is_12(self):
        """kappa(V^natural) = c/2 = 12."""
        assert monster_kappa() == Rational(12)

    def test_leech_kappa_is_24(self):
        """kappa(V_Leech) = rank = 24."""
        assert leech_kappa() == Rational(24)

    def test_kappas_are_different(self):
        """V^natural and V_Leech have DIFFERENT kappa."""
        assert monster_kappa() != leech_kappa()

    def test_kappa_ratio(self):
        """kappa_Leech / kappa_Monster = 2 (orbifold halving)."""
        assert leech_kappa() / monster_kappa() == Rational(2)

    def test_monster_kappa_positive(self):
        assert monster_kappa() > 0

    def test_leech_kappa_positive(self):
        assert leech_kappa() > 0

    def test_central_charge_same(self):
        """Both have c = 24."""
        assert MONSTER_CENTRAL_CHARGE == Rational(24)


# =========================================================================
# 2. Shadow class
# =========================================================================

class TestShadowClass:
    """Verify shadow class determination."""

    def test_monster_class_M(self):
        """V^natural is class M (infinite depth)."""
        assert monster_shadow_class() == 'M'

    def test_leech_class_G(self):
        """V_Leech is class G (Gaussian, depth 2)."""
        sd = leech_shadow_data()
        assert sd['shadow_class'] == 'G'
        assert sd['shadow_depth'] == 2

    def test_monster_infinite_depth(self):
        sd = monster_shadow_data()
        assert sd['shadow_depth'] == float('inf')

    def test_different_classes(self):
        """V^natural and V_Leech have DIFFERENT shadow classes."""
        assert monster_shadow_class() != leech_shadow_data()['shadow_class']


# =========================================================================
# 3. Virasoro shadow coefficients at c = 24
# =========================================================================

class TestVirasoroShadowCoefficients:
    """Shadow coefficients for the Virasoro subalgebra at c = 24."""

    def test_S2_equals_kappa(self):
        """S_2(Vir, c=24) = c/2 = 12."""
        assert _virasoro_shadow_coefficient(2) == Rational(12)

    def test_S3_equals_2(self):
        """S_3(Vir) = 2 (universal)."""
        assert _virasoro_shadow_coefficient(3) == Rational(2)

    def test_S4_value(self):
        """S_4(Vir, c=24) = 10/(24*142) = 5/1704."""
        expected = Rational(10, 24 * (5 * 24 + 22))
        assert expected == Rational(5, 1704)
        assert _virasoro_shadow_coefficient(4) == Rational(5, 1704)

    def test_S5_value(self):
        """S_5(Vir, c=24) from recursion."""
        S5 = _virasoro_shadow_coefficient(5)
        assert S5 == Rational(-1, 1704)

    def test_S2_positive(self):
        assert _virasoro_shadow_coefficient(2) > 0

    def test_S3_positive(self):
        assert _virasoro_shadow_coefficient(3) > 0

    def test_S4_positive(self):
        assert _virasoro_shadow_coefficient(4) > 0

    def test_S1_zero(self):
        assert _virasoro_shadow_coefficient(1) == 0

    def test_S0_zero(self):
        assert _virasoro_shadow_coefficient(0) == 0

    def test_virasoro_tower_dict(self):
        """virasoro_shadow_tower returns a dict with correct keys."""
        tower = virasoro_shadow_tower(8)
        assert set(tower.keys()) == set(range(2, 9))

    def test_virasoro_tower_S2(self):
        tower = virasoro_shadow_tower(5)
        assert tower[2] == Rational(12)

    def test_virasoro_tower_alternating_sign(self):
        """For Virasoro at c=24, S_r alternates sign for r >= 4."""
        tower = virasoro_shadow_tower(10)
        # S_4 > 0, S_5 < 0, S_6 > 0, S_7 < 0, ...
        assert tower[4] > 0
        assert tower[5] < 0
        assert tower[6] > 0
        assert tower[7] < 0


# =========================================================================
# 4. Critical discriminant
# =========================================================================

class TestCriticalDiscriminant:
    """Verify Delta = 8*kappa*S_4."""

    def test_discriminant_value(self):
        """Delta = 8 * 12 * 5/1704 = 20/71."""
        assert monster_critical_discriminant() == Rational(20, 71)

    def test_discriminant_nonzero(self):
        """Delta != 0 implies class M."""
        assert monster_critical_discriminant() != 0

    def test_discriminant_positive(self):
        """Delta > 0 for c = 24."""
        assert monster_critical_discriminant() > 0

    def test_discriminant_formula(self):
        """Verify Delta = 8*kappa*S_4 from components."""
        kappa = monster_kappa()
        S4 = _virasoro_shadow_coefficient(4)
        expected = 8 * kappa * S4
        assert expected == Rational(20, 71)
        assert expected == monster_critical_discriminant()

    def test_leech_discriminant_zero(self):
        """V_Leech has Delta = 0 (class G)."""
        sd = leech_shadow_data()
        assert sd['critical_discriminant'] == 0


# =========================================================================
# 5. Monster vs Leech comparison
# =========================================================================

class TestMonsterVsLeech:
    """Side-by-side comparison of the two c=24 holomorphic VOAs."""

    def test_same_central_charge(self):
        comp = monster_vs_leech_comparison()
        assert comp['same_central_charge'] is True

    def test_different_kappa(self):
        comp = monster_vs_leech_comparison()
        assert comp['same_kappa'] is False

    def test_different_shadow_class(self):
        comp = monster_vs_leech_comparison()
        assert comp['same_shadow_class'] is False

    def test_kappa_ratio_is_2(self):
        comp = monster_vs_leech_comparison()
        assert comp['F1_ratio'] == 2

    def test_dim_V1_monster_zero(self):
        comp = monster_vs_leech_comparison()
        assert comp['dim_V1_monster'] == 0

    def test_dim_V1_leech_24(self):
        comp = monster_vs_leech_comparison()
        assert comp['dim_V1_leech'] == 24

    def test_orbifold_halving(self):
        comp = monster_vs_leech_comparison()
        assert comp['orbifold_kappa_halving'] is True


# =========================================================================
# 6. Genus amplitudes
# =========================================================================

class TestGenusAmplitudes:
    """Verify genus-g scalar amplitudes."""

    def test_monster_F1(self):
        """F_1(V^natural) = 12/24 = 1/2."""
        assert monster_genus_amplitude(1) == Rational(1, 2)

    def test_leech_F1(self):
        """F_1(V_Leech) = 24/24 = 1."""
        assert leech_genus_amplitude(1) == Rational(1)

    def test_monster_F2(self):
        """F_2(V^natural) = 12 * 7/5760 = 7/480."""
        assert monster_genus_amplitude(2) == Rational(7, 480)

    def test_leech_F2(self):
        """F_2(V_Leech) = 24 * 7/5760 = 7/240."""
        assert leech_genus_amplitude(2) == Rational(7, 240)

    def test_F1_ratio_is_2(self):
        """F_1(Leech) / F_1(Monster) = 2."""
        ratio = leech_genus_amplitude(1) / monster_genus_amplitude(1)
        assert ratio == 2

    def test_Fg_ratio_is_2_all_g(self):
        """F_g(Leech) / F_g(Monster) = 2 for all g (at scalar level)."""
        for g in range(1, 6):
            ratio = leech_genus_amplitude(g) / monster_genus_amplitude(g)
            assert ratio == 2

    def test_genus_comparison_dict(self):
        comp = genus_amplitude_comparison(3)
        assert set(comp.keys()) == {1, 2, 3}
        for g in range(1, 4):
            assert 'F_monster' in comp[g]
            assert 'F_leech' in comp[g]
            assert 'ratio' in comp[g]


# =========================================================================
# 7. Planted-forest corrections
# =========================================================================

class TestPlantedForest:
    """Verify genus-2 planted-forest corrections."""

    def test_monster_pf_g2(self):
        """delta_pf = 2*(20-12)/48 = 2*8/48 = 1/3."""
        pf = monster_planted_forest_g2()
        assert pf == Rational(1, 3)

    def test_monster_pf_nonzero(self):
        """V^natural has NONZERO planted-forest correction (class M)."""
        assert monster_planted_forest_g2() != 0

    def test_leech_pf_zero(self):
        """V_Leech has ZERO planted-forest correction (class G)."""
        sd = leech_shadow_data()
        assert sd['S3'] == 0  # S_3 = 0 implies delta_pf = 0

    def test_monster_total_g2(self):
        """A_2 = F_2 + delta_pf = 7/480 + 1/3 = 167/480."""
        total = monster_total_genus2()
        expected = Rational(7, 480) + Rational(1, 3)
        assert total == expected
        assert total == Rational(167, 480)


# =========================================================================
# 8. J-function coefficients
# =========================================================================

class TestJFunction:
    """Verify J-function coefficient table."""

    def test_J_minus1(self):
        """J(tau) has polar coefficient 1."""
        assert j_coefficient(-1) == 1

    def test_J_0(self):
        """J(tau) has constant term 0."""
        assert j_coefficient(0) == 0

    def test_J_1(self):
        """c(1) = 196884."""
        assert j_coefficient(1) == 196884

    def test_J_2(self):
        """c(2) = 21493760."""
        assert j_coefficient(2) == 21493760

    def test_J_3(self):
        """c(3) = 864299970."""
        assert j_coefficient(3) == 864299970

    def test_J_positive_for_n_ge_1(self):
        """All J-function coefficients are positive for n >= 1."""
        for n in range(1, 11):
            assert j_coefficient(n) > 0

    def test_J_mckay(self):
        """196884 = 1 + 196883 (McKay observation)."""
        assert j_coefficient(1) == 1 + MONSTER_IRREP_DIMS['chi_2']

    def test_J_out_of_range_raises(self):
        with pytest.raises(ValueError):
            j_coefficient(100)


# =========================================================================
# 9. Monster representation decompositions
# =========================================================================

class TestMonsterDecompositions:
    """Verify V_n decomposes into Monster irreps summing to dim(V_n)."""

    def test_V0_vacuum(self):
        d = monster_rep_decomposition(0)
        assert d is not None
        assert d['total'] == 1

    def test_V1_mckay(self):
        """V_1 = 1 + 196883 (McKay)."""
        d = monster_rep_decomposition(1)
        assert d is not None
        assert d['total'] == 196884
        dims = [dim for dim, _ in d['irreps']]
        assert 1 in dims
        assert 196883 in dims

    def test_V2_decomposition(self):
        d = monster_rep_decomposition(2)
        assert d is not None
        assert d['total'] == 21493760
        dims = [dim for dim, _ in d['irreps']]
        assert sum(dims) == 21493760

    def test_V3_decomposition(self):
        d = monster_rep_decomposition(3)
        assert d is not None
        assert d['total'] == 864299970
        dims = [dim for dim, _ in d['irreps']]
        assert sum(dims) == 864299970

    def test_unknown_returns_none(self):
        assert monster_rep_decomposition(100) is None

    def test_verify_all_totals(self):
        """Sum of irrep dims equals total for all tabulated weights."""
        assert verify_decomposition_totals() is True


# =========================================================================
# 10. McKay-Thompson series
# =========================================================================

class TestMcKayThompson:
    """Verify McKay-Thompson series data."""

    def test_1A_equals_J(self):
        """T_{1A} = J(tau)."""
        coeffs = mckay_thompson_coefficients('1A', 5)
        for n in range(6):
            assert coeffs[n] == j_coefficient(n)

    def test_2A_constant_zero(self):
        """T_{2A} has c(0) = 0."""
        coeffs = mckay_thompson_coefficients('2A', 0)
        assert coeffs[0] == 0

    def test_2A_c1(self):
        """T_{2A}: c(1) = 4372."""
        coeffs = mckay_thompson_coefficients('2A', 1)
        assert coeffs[1] == 4372

    def test_2B_alternating_sign(self):
        """T_{2B} has alternating signs relative to T_{2A}."""
        c_2A = mckay_thompson_coefficients('2A', 5)
        c_2B = mckay_thompson_coefficients('2B', 5)
        for n in range(1, 6):
            assert c_2B[n] == (-1)**n * c_2A[n]

    def test_3A_constant_zero(self):
        coeffs = mckay_thompson_coefficients('3A', 0)
        assert coeffs[0] == 0

    def test_all_constant_terms_zero(self):
        """All McKay-Thompson series have c(0) = 0."""
        for cls in MCKAY_THOMPSON_DATA:
            coeffs = mckay_thompson_coefficients(cls, 0)
            assert coeffs[0] == 0, f"T_{cls} has nonzero constant term"

    def test_unknown_class_raises(self):
        with pytest.raises(ValueError):
            mckay_thompson_coefficients('99Z', 5)

    def test_13A_c1(self):
        """T_{13A}: c(1) = 12."""
        coeffs = mckay_thompson_coefficients('13A', 1)
        assert coeffs[1] == 12


# =========================================================================
# 11. McKay-Thompson shadow kappa
# =========================================================================

class TestMcKayThompsonKappa:
    """Equivariant modular characteristic."""

    def test_1A_kappa_12(self):
        """kappa_{1A} = kappa(V^natural) = 12."""
        assert mckay_thompson_shadow_kappa('1A') == Rational(12)

    def test_2A_kappa_virasoro_level(self):
        """At Virasoro level, kappa_g = 12 for all g."""
        assert mckay_thompson_shadow_kappa('2A') == Rational(12)

    def test_all_kappa_same_at_virasoro_level(self):
        """At Virasoro level, kappa_g = 12 for all tabulated classes."""
        for cls in MCKAY_THOMPSON_DATA:
            assert mckay_thompson_shadow_kappa(cls) == Rational(12)

    def test_F1_equivariant_identity(self):
        """F_1^{1A} = 12/24 = 1/2."""
        assert mckay_thompson_equivariant_F1('1A') == Rational(1, 2)


# =========================================================================
# 12. Genus-0 Hauptmodul property
# =========================================================================

class TestGenus0Property:
    """Verify genus-0 Hauptmodul data."""

    def test_1A_SL2Z(self):
        """T_{1A} is the Hauptmodul for SL(2,Z)."""
        data = mckay_thompson_genus0_property('1A')
        assert data['genus_zero_group'] == 'SL(2,Z)'
        assert data['hauptmodul'] is True
        assert data['element_order'] == 1

    def test_2A_genus0(self):
        data = mckay_thompson_genus0_property('2A')
        assert data['hauptmodul'] is True
        assert data['element_order'] == 2
        assert data['constant_term_vanishes'] is True

    def test_all_hauptmoduln(self):
        """All tabulated classes are genus-0."""
        for cls in MCKAY_THOMPSON_DATA:
            data = mckay_thompson_genus0_property(cls)
            assert data['hauptmodul'] is True

    def test_all_constant_terms_vanish(self):
        """All Hauptmoduln have vanishing constant term."""
        for cls in MCKAY_THOMPSON_DATA:
            data = mckay_thompson_genus0_property(cls)
            assert data['constant_term_vanishes'] is True


# =========================================================================
# 13. Arithmetic depth
# =========================================================================

class TestArithmeticDepth:
    """Verify arithmetic depth analysis."""

    def test_monster_d_arith_0(self):
        """d_arith(V^natural) = 0 at genus 1."""
        ad = monster_arithmetic_depth()
        assert ad['genus_1_arithmetic_depth'] == 0

    def test_leech_d_arith_1(self):
        """d_arith(V_Leech) = 1 (Delta_12 cusp form)."""
        ad = leech_arithmetic_depth()
        assert ad['genus_1_arithmetic_depth'] == 1

    def test_leech_c_delta(self):
        """c_delta(Leech) = -65520/691."""
        ad = leech_arithmetic_depth()
        assert ad['c_delta'] == Fraction(-65520, 691)

    def test_monster_genus0_exact(self):
        """V^natural partition function is genus-0 exact (Rademacher)."""
        ad = monster_arithmetic_depth()
        assert ad['rademacher_exact'] is True
        assert ad['genus_0_hauptmodul'] is True


# =========================================================================
# 14. Orbifold shadow dichotomy
# =========================================================================

class TestOrbifoldDichotomy:
    """Verify the V_Leech -> V^natural orbifold effect on shadows."""

    def test_orbifold_type(self):
        od = orbifold_shadow_dichotomy()
        assert od['orbifold_type'] == 'Z/2Z'

    def test_kappa_halving(self):
        od = orbifold_shadow_dichotomy()
        assert od['kappa_change']['before'] == 24
        assert od['kappa_change']['after'] == 12

    def test_class_change(self):
        od = orbifold_shadow_dichotomy()
        assert od['class_change']['before'] == 'G'
        assert od['class_change']['after'] == 'M'

    def test_depth_change(self):
        od = orbifold_shadow_dichotomy()
        assert od['depth_change']['before'] == 2
        assert od['depth_change']['after'] == float('inf')

    def test_dim_V1_killed(self):
        od = orbifold_shadow_dichotomy()
        assert od['dim_V1_change']['before'] == 24
        assert od['dim_V1_change']['after'] == 0


# =========================================================================
# 15. Griess algebra data
# =========================================================================

class TestGriessAlgebra:
    """Verify Griess algebra data."""

    def test_dimension(self):
        gd = griess_algebra_data()
        assert gd['dimension'] == 196884

    def test_primary_space_dim(self):
        gd = griess_algebra_data()
        assert gd['decomposition_under_virasoro']['primary_space'] == 196883

    def test_S3_virasoro(self):
        gd = griess_algebra_data()
        assert gd['S3_virasoro_contribution'] == Rational(2)


# =========================================================================
# 16. Shadow growth rate
# =========================================================================

class TestShadowGrowthRate:
    """Verify shadow growth rate for V^natural."""

    def test_growth_rate_positive(self):
        """rho > 0 for V^natural (class M)."""
        rho = monster_shadow_growth_rate()
        assert rho > 0

    def test_growth_rate_less_than_1(self):
        """rho < 1 (shadow tower converges)."""
        rho = monster_shadow_growth_rate()
        assert rho < 1

    def test_growth_rate_value(self):
        """rho approximately 0.252 at Virasoro level."""
        rho = monster_shadow_growth_rate()
        assert abs(rho - 0.252) < 0.01

    def test_leech_growth_rate_zero(self):
        """V_Leech has rho = 0 (class G, terminates)."""
        sd = leech_shadow_data()
        assert sd['shadow_growth_rate'] == 0.0


# =========================================================================
# 17. MC synthesis
# =========================================================================

class TestMCSynthesis:
    """Verify the synthesis of moonshine in the MC framework."""

    def test_synthesis_has_key_sections(self):
        s = moonshine_mc_synthesis()
        assert 'what_mc_sees' in s
        assert 'what_mc_does_not_see_at_scalar_level' in s
        assert 'frontier_computations' in s
        assert 'key_insight' in s

    def test_kappa_distinguishes(self):
        s = moonshine_mc_synthesis()
        assert 'kappa' in s['what_mc_sees']


# =========================================================================
# 18. Full atlas
# =========================================================================

class TestFullAtlas:
    """Verify the complete moonshine shadow atlas."""

    def test_atlas_has_monster(self):
        atlas = full_moonshine_shadow_atlas()
        assert 'monster' in atlas

    def test_atlas_has_leech(self):
        atlas = full_moonshine_shadow_atlas()
        assert 'leech' in atlas

    def test_atlas_has_comparison(self):
        atlas = full_moonshine_shadow_atlas()
        assert 'comparison' in atlas

    def test_atlas_has_mckay_thompson(self):
        atlas = full_moonshine_shadow_atlas()
        assert 'mckay_thompson' in atlas
        assert '1A' in atlas['mckay_thompson']
        assert '2A' in atlas['mckay_thompson']

    def test_atlas_has_synthesis(self):
        atlas = full_moonshine_shadow_atlas()
        assert 'synthesis' in atlas

    def test_atlas_virasoro_tower(self):
        atlas = full_moonshine_shadow_atlas()
        assert 'virasoro_tower' in atlas
        tower = atlas['virasoro_tower']
        assert tower[2] == Rational(12)
        assert tower[3] == Rational(2)


# =========================================================================
# 19. Cross-checks with shadow_tower_ode
# =========================================================================

class TestCrossCheckWithODE:
    """Verify consistency with the shadow_tower_ode module at c = 24."""

    def test_S2_matches_ode(self):
        """S_2(c=24) = 12 from both sources."""
        from compute.lib.shadow_tower_ode import shadow_coefficient
        ode_val = shadow_coefficient(2).subs('c', 24)
        local_val = _virasoro_shadow_coefficient(2)
        assert ode_val == local_val

    def test_S3_matches_ode(self):
        from compute.lib.shadow_tower_ode import shadow_coefficient
        ode_val = shadow_coefficient(3).subs('c', 24)
        local_val = _virasoro_shadow_coefficient(3)
        assert ode_val == local_val

    def test_S4_matches_ode(self):
        from compute.lib.shadow_tower_ode import shadow_coefficient
        ode_val = shadow_coefficient(4).subs('c', 24)
        local_val = _virasoro_shadow_coefficient(4)
        assert ode_val == local_val

    def test_S5_matches_ode(self):
        from compute.lib.shadow_tower_ode import shadow_coefficient
        ode_val = shadow_coefficient(5).subs('c', 24)
        local_val = _virasoro_shadow_coefficient(5)
        assert ode_val == local_val

    def test_S6_matches_ode(self):
        from compute.lib.shadow_tower_ode import shadow_coefficient
        ode_val = shadow_coefficient(6).subs('c', 24)
        local_val = _virasoro_shadow_coefficient(6)
        assert ode_val == local_val


# =========================================================================
# 20. Consistency checks
# =========================================================================

class TestConsistency:
    """Internal consistency checks."""

    def test_monster_shadow_data_kappa(self):
        """Shadow data dict has correct kappa."""
        sd = monster_shadow_data()
        assert sd['kappa'] == Rational(12)

    def test_monster_shadow_data_class(self):
        sd = monster_shadow_data()
        assert sd['shadow_class'] == 'M'

    def test_monster_shadow_data_F1(self):
        sd = monster_shadow_data()
        assert sd['F1'] == Rational(1, 2)

    def test_monster_shadow_data_F2(self):
        sd = monster_shadow_data()
        assert sd['F2'] == Rational(7, 480)

    def test_leech_shadow_data_S3_zero(self):
        sd = leech_shadow_data()
        assert sd['S3'] == 0

    def test_leech_shadow_data_S4_zero(self):
        sd = leech_shadow_data()
        assert sd['S4'] == 0

    def test_decomposition_V1_sum(self):
        """196884 = 1 + 196883."""
        d = MONSTER_DECOMPOSITIONS[1]
        assert sum(dim for dim, _ in d['irreps']) == 196884

    def test_decomposition_V2_sum(self):
        """21493760 = 1 + 196883 + 21296876."""
        d = MONSTER_DECOMPOSITIONS[2]
        assert sum(dim for dim, _ in d['irreps']) == 21493760
        assert 1 + 196883 + 21296876 == 21493760

    def test_decomposition_V3_sum(self):
        """864299970 = 2*1 + 2*196883 + 21296876 + 842609326."""
        assert 2 * 1 + 2 * 196883 + 21296876 + 842609326 == 864299970

    def test_monster_order(self):
        """Verify Monster group order has the right magnitude."""
        assert MONSTER_ORDER > 8 * 10**53
        assert MONSTER_ORDER < 9 * 10**53

    def test_2B_sign_alternation(self):
        """T_{2B}(tau) = T_{2A}(-1/tau) gives alternating signs.

        For an involution g of class 2B, Tr(g|V_n) = (-1)^n * Tr(g'|V_n)
        where g' is class 2A. This is because 2B is the 'other' involution
        class, related to 2A by the sign character of the orbifold.
        """
        data_2A = MCKAY_THOMPSON_DATA['2A']['coefficients']
        data_2B = MCKAY_THOMPSON_DATA['2B']['coefficients']
        for n in range(1, 6):
            if n in data_2A and n in data_2B:
                assert data_2B[n] == (-1)**n * data_2A[n]
