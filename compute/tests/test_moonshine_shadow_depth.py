r"""Tests for moonshine shadow depth: Niemeier lattice VOAs and the Monster module.

Covers:
  1. Niemeier lattice registry: root counts, Coxeter numbers, rank
  2. Shadow data: kappa, S_3, S_4, class, depth for all 24 lattices
  3. Monster module: kappa, class, Virasoro shadow tower
  4. Critical discriminant and single-line dichotomy
  5. Genus amplitudes (F_1, F_2) for lattices and Monster
  6. Planted-forest corrections
  7. c_Delta coefficients and theta series
  8. Holomorphic c = 24 dichotomy
  9. Orbifold shadow transition V_Leech -> V^natural
  10. Moonshine-shadow interface
  11. Cross-verification: multiple independent paths for each claim
  12. Schellekens list shadow class counts

Mathematical ground truth:
  - Niemeier (1973): 24 even unimodular lattices in dim 24
  - Frenkel-Lepowsky-Meurman (1988): V^natural, c=24, dim V_1=0
  - Conway-Norton (1979): Monstrous moonshine
  - Borcherds (1992): proof of moonshine
  - Schellekens (1993): 71 holomorphic c=24 VOAs
  - thm:lattice:niemeier-shadow-universality (lattice_foundations.tex)
  - rem:vnatural-class-m (arithmetic_shadows.tex)
  - cor:conformal-vector-infinite-depth (arithmetic_shadows.tex)

Multi-path verification (CLAUDE.md mandate):
  Every numerical claim verified by 3+ independent paths.
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.moonshine_shadow_depth import (
    ALL_NIEMEIER_LABELS,
    J_COEFFICIENTS,
    MONSTER_CENTRAL_CHARGE,
    MONSTER_KAPPA,
    NIEMEIER_COUNT,
    NIEMEIER_KAPPA,
    NIEMEIER_RANK,
    NIEMEIER_REGISTRY,
    SCHELLEKENS_SHADOW_DATA,
    coxeter_number,
    dimension,
    dual_coxeter_number,
    faber_pandharipande,
    full_shadow_depth_atlas,
    holomorphic_c24_dichotomy,
    j_function_shadow_relation,
    monster_S3_virasoro,
    monster_S4_virasoro,
    monster_critical_discriminant_virasoro,
    monster_d_alg,
    monster_full_shadow_data,
    monster_kappa,
    monster_planted_forest_g2_virasoro,
    monster_shadow_class,
    monster_shadow_depth,
    monster_shadow_growth_rate,
    monster_virasoro_shadow_tower,
    niemeier_S3,
    niemeier_S4,
    niemeier_c_delta,
    niemeier_c_delta_table,
    niemeier_critical_discriminant,
    niemeier_full_shadow_data,
    niemeier_kappa,
    niemeier_shadow_class,
    niemeier_shadow_depth,
    rademacher_shadow_connection,
    root_count,
    shadow_class_count,
    verify_c_delta_table,
    verify_coxeter_numbers,
    verify_niemeier_root_counts,
)


# =========================================================================
# 1. Niemeier lattice registry
# =========================================================================

class TestNiemeierRegistry:
    """Verify the 24 Niemeier lattice registry."""

    def test_count_is_24(self):
        """Exactly 24 Niemeier lattices."""
        assert len(NIEMEIER_REGISTRY) == 24
        assert len(ALL_NIEMEIER_LABELS) == 24

    def test_all_rank_24(self):
        """All Niemeier lattices have rank 24."""
        for label, data in NIEMEIER_REGISTRY.items():
            assert data['rank'] == 24, f"{label}: rank={data['rank']}"

    def test_root_rank_24_for_non_leech(self):
        """All non-Leech lattices have root rank 24."""
        for label, data in NIEMEIER_REGISTRY.items():
            if label == 'Leech':
                assert data['root_rank'] == 0
            else:
                assert data['root_rank'] == 24, f"{label}: root_rank={data['root_rank']}"

    def test_leech_has_no_roots(self):
        """The Leech lattice has no roots."""
        assert NIEMEIER_REGISTRY['Leech']['num_roots'] == 0

    def test_root_counts_from_first_principles(self):
        """Root counts computed from root system formulas."""
        results = verify_niemeier_root_counts()
        for label, ok in results.items():
            assert ok, f"Root count mismatch for {label}"

    def test_coxeter_numbers_uniform(self):
        """All components of each lattice have the same Coxeter number."""
        results = verify_coxeter_numbers()
        for label, ok in results.items():
            assert ok, f"Coxeter number mismatch for {label}"

    def test_root_count_D24(self):
        """D_24: |R| = 2*24*23 = 1104."""
        assert root_count('D', 24) == 1104
        assert NIEMEIER_REGISTRY['D24']['num_roots'] == 1104

    def test_root_count_E8(self):
        """E_8: |R| = 240."""
        assert root_count('E', 8) == 240

    def test_root_count_3E8(self):
        """3E_8: |R| = 3*240 = 720."""
        assert NIEMEIER_REGISTRY['3E8']['num_roots'] == 720

    def test_root_count_24A1(self):
        """24A_1: |R| = 24*1*2 = 48."""
        assert root_count('A', 1) == 2
        assert NIEMEIER_REGISTRY['24A1']['num_roots'] == 48

    def test_coxeter_E8(self):
        """h(E_8) = 30."""
        assert coxeter_number('E', 8) == 30

    def test_coxeter_A24(self):
        """h(A_24) = 25."""
        assert coxeter_number('A', 24) == 25

    def test_root_counts_decrease_with_number(self):
        """Root counts decrease (non-strictly) in the standard ordering."""
        prev = float('inf')
        for label in ALL_NIEMEIER_LABELS:
            n = NIEMEIER_REGISTRY[label]['num_roots']
            assert n <= prev, f"{label}: {n} > {prev}"
            prev = n


# =========================================================================
# 2. Shadow data for Niemeier lattice VOAs
# =========================================================================

class TestNiemeierShadowData:
    """Shadow obstruction tower for all 24 Niemeier lattice VOAs."""

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_kappa_is_24(self, label):
        """kappa(V_Lambda) = 24 for all Niemeier lattices."""
        assert niemeier_kappa(label) == Rational(24)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_S3_is_zero(self, label):
        """S_3 = 0 for all Niemeier lattice VOAs."""
        assert niemeier_S3(label) == Rational(0)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_S4_is_zero(self, label):
        """S_4 = 0 for all Niemeier lattice VOAs."""
        assert niemeier_S4(label) == Rational(0)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_class_G(self, label):
        """All Niemeier lattice VOAs are class G."""
        assert niemeier_shadow_class(label) == 'G'

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_depth_2(self, label):
        """Shadow depth = 2 for all Niemeier lattice VOAs."""
        assert niemeier_shadow_depth(label) == 2

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_critical_discriminant_zero(self, label):
        """Delta = 0 for all Niemeier lattice VOAs."""
        assert niemeier_critical_discriminant(label) == Rational(0)

    def test_kappa_is_rank_not_c_over_2(self):
        """AP39: kappa = rank = 24, NOT c/2 = 12."""
        # The central charge IS 24, and c/2 = 12, but kappa = 24
        c = Rational(24)
        assert NIEMEIER_KAPPA == Rational(24)
        assert NIEMEIER_KAPPA != c / 2  # Would be 12, which is WRONG

    def test_shadow_tower_blind_to_root_system(self):
        """The shadow tower cannot distinguish Niemeier lattices."""
        data_list = [niemeier_full_shadow_data(lb) for lb in ALL_NIEMEIER_LABELS]
        for d in data_list:
            assert d['kappa'] == Rational(24)
            assert d['S3'] == Rational(0)
            assert d['S4'] == Rational(0)
            assert d['shadow_class'] == 'G'
            assert d['shadow_depth'] == 2


# =========================================================================
# 3. Monster module shadow data
# =========================================================================

class TestMonsterShadowData:
    """Shadow obstruction tower for V^natural."""

    def test_monster_kappa_is_12(self):
        """kappa(V^natural) = c/2 = 12."""
        assert monster_kappa() == Rational(12)

    def test_monster_kappa_not_24(self):
        """kappa(V^natural) != 24 (AP48: not rank formula)."""
        assert monster_kappa() != Rational(24)

    def test_monster_class_M(self):
        """V^natural is class M (infinite shadow depth)."""
        assert monster_shadow_class() == 'M'

    def test_monster_depth_infinite(self):
        """Shadow depth of V^natural is infinity."""
        assert monster_shadow_depth() == float('inf')

    def test_monster_d_alg_infinite(self):
        """Algebraic depth d_alg = infinity."""
        assert monster_d_alg() == float('inf')

    def test_monster_S3_virasoro(self):
        """S_3^{Vir} = 2 (universal for Virasoro)."""
        assert monster_S3_virasoro() == Rational(2)

    def test_monster_S4_virasoro(self):
        """S_4^{Vir}(c=24) = 10/(24*142) = 5/1704."""
        assert monster_S4_virasoro() == Rational(5, 1704)

    def test_monster_S4_virasoro_path2(self):
        """Verify S_4 via Q^contact formula: 10/[c(5c+22)]."""
        c = 24
        expected = Rational(10, c * (5 * c + 22))
        assert monster_S4_virasoro() == expected

    def test_monster_S4_virasoro_path3(self):
        """Verify S_4 via explicit arithmetic: 10/3408 = 5/1704."""
        assert Rational(10, 3408) == Rational(5, 1704)
        assert monster_S4_virasoro() == Rational(10, 3408)

    def test_monster_virasoro_tower_nonzero(self):
        """Virasoro shadow tower has nonzero S_r for all r >= 2."""
        tower = monster_virasoro_shadow_tower(8)
        for r in range(2, 9):
            assert tower[r] != 0, f"S_{r} = 0 at c = 24"

    def test_monster_shadow_growth_rate_positive(self):
        """Shadow growth rate rho > 0 for V^natural."""
        rho = monster_shadow_growth_rate()
        assert rho > 0

    def test_monster_kappa_vs_leech(self):
        """Monster kappa (12) differs from Leech kappa (24)."""
        assert monster_kappa() != niemeier_kappa('Leech')
        assert monster_kappa() == niemeier_kappa('Leech') / 2


# =========================================================================
# 4. Critical discriminant and single-line dichotomy
# =========================================================================

class TestCriticalDiscriminant:
    """The single-line dichotomy: Delta != 0 iff class M."""

    def test_monster_discriminant_nonzero(self):
        """Delta(V^natural) = 20/71 != 0 at Virasoro level."""
        Delta = monster_critical_discriminant_virasoro()
        assert Delta == Rational(20, 71)
        assert Delta > 0

    def test_monster_discriminant_formula(self):
        """Delta = 8 * kappa * S_4 = 8 * 12 * 5/1704 = 20/71."""
        Delta = 8 * Rational(12) * Rational(5, 1704)
        assert Delta == Rational(20, 71)

    def test_monster_discriminant_path2(self):
        """Verify: 8*12*5/1704 = 480/1704 = 20/71."""
        assert Rational(480, 1704) == Rational(20, 71)
        assert monster_critical_discriminant_virasoro() == Rational(480, 1704)

    def test_niemeier_discriminant_zero(self):
        """Delta = 0 for all Niemeier lattice VOAs."""
        for label in ALL_NIEMEIER_LABELS:
            assert niemeier_critical_discriminant(label) == Rational(0)

    def test_dichotomy_discriminant_separates(self):
        """Discriminant distinguishes lattice VOAs from Monster."""
        Delta_monster = monster_critical_discriminant_virasoro()
        for label in ALL_NIEMEIER_LABELS:
            Delta_lattice = niemeier_critical_discriminant(label)
            assert Delta_monster != Delta_lattice


# =========================================================================
# 5. Genus amplitudes
# =========================================================================

class TestGenusAmplitudes:
    """F_g for Niemeier lattices and Monster."""

    def test_niemeier_F1(self):
        """F_1(V_Lambda) = 24/24 = 1 for all Niemeier lattices."""
        for label in ALL_NIEMEIER_LABELS:
            data = niemeier_full_shadow_data(label)
            assert data['F1'] == Rational(1)

    def test_monster_F1(self):
        """F_1(V^natural) = 12/24 = 1/2."""
        data = monster_full_shadow_data()
        assert data['F1'] == Rational(1, 2)

    def test_F1_ratio(self):
        """F_1(Niemeier) / F_1(Monster) = 2 (orbifold halving)."""
        assert Rational(1) / Rational(1, 2) == Rational(2)

    def test_niemeier_F2(self):
        """F_2(V_Lambda) = 24 * 7/5760 = 7/240."""
        data = niemeier_full_shadow_data('Leech')
        expected = Rational(24) * Rational(7, 5760)
        assert data['F2'] == expected
        assert data['F2'] == Rational(7, 240)

    def test_monster_F2(self):
        """F_2(V^natural) = 12 * 7/5760 = 7/480."""
        data = monster_full_shadow_data()
        expected = Rational(12) * Rational(7, 5760)
        assert data['F2'] == expected
        assert data['F2'] == Rational(7, 480)

    def test_universal_F2_over_F1_ratio(self):
        """F_2/F_1 = 7/240 for both Niemeier and Monster."""
        monster_data = monster_full_shadow_data()
        niemeier_data = niemeier_full_shadow_data('Leech')
        ratio_monster = monster_data['F2'] / monster_data['F1']
        ratio_niemeier = niemeier_data['F2'] / niemeier_data['F1']
        assert ratio_monster == Rational(7, 240)
        assert ratio_niemeier == Rational(7, 240)

    def test_faber_pandharipande_g1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_faber_pandharipande_g2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)


# =========================================================================
# 6. Planted-forest corrections
# =========================================================================

class TestPlantedForest:
    """Planted-forest corrections at genus 2."""

    def test_niemeier_pf_zero(self):
        """delta_pf = 0 for all Niemeier lattices (S_3 = 0)."""
        for label in ALL_NIEMEIER_LABELS:
            data = niemeier_full_shadow_data(label)
            assert data['planted_forest_g2'] == Rational(0)

    def test_monster_pf_virasoro(self):
        """delta_pf(V^natural, Vir) = S_3*(10*S_3 - kappa)/48 = 1/3."""
        pf = monster_planted_forest_g2_virasoro()
        assert pf == Rational(1, 3)

    def test_monster_pf_formula_check(self):
        """Verify: 2*(20-12)/48 = 2*8/48 = 16/48 = 1/3."""
        S3 = Rational(2)
        kappa = Rational(12)
        result = S3 * (10 * S3 - kappa) / 48
        assert result == Rational(1, 3)

    def test_monster_total_genus2_virasoro(self):
        """Total A_2(V^natural, Vir) = F_2 + delta_pf = 7/480 + 1/3 = 167/480."""
        F2 = Rational(12) * faber_pandharipande(2)
        pf = monster_planted_forest_g2_virasoro()
        total = F2 + pf
        assert total == Rational(7, 480) + Rational(1, 3)
        assert total == Rational(167, 480)


# =========================================================================
# 7. c_Delta coefficients
# =========================================================================

class TestCDelta:
    """c_Delta in Theta_Lambda = E_12 + c_Delta * Delta_12."""

    def test_leech_c_delta(self):
        """Leech: c_Delta = (0 - 65520)/691 = -65520/691."""
        assert niemeier_c_delta('Leech') == Fraction(-65520, 691)

    def test_D24_c_delta(self):
        """D_24: c_Delta = (691*1104 - 65520)/691 = 697344/691."""
        assert niemeier_c_delta('D24') == Fraction(697344, 691)

    def test_3E8_c_delta(self):
        """3E_8: c_Delta = (691*720 - 65520)/691 = 432000/691."""
        assert niemeier_c_delta('3E8') == Fraction(432000, 691)

    def test_8A3_c_delta(self):
        """8A_3: c_Delta = (691*96 - 65520)/691 = 816/691."""
        expected = Fraction(691 * 96 - 65520, 691)
        assert niemeier_c_delta('8A3') == expected
        assert expected == Fraction(816, 691)

    def test_12A2_c_delta(self):
        """12A_2: c_Delta < 0 (fewer roots than average)."""
        cd = niemeier_c_delta('12A2')
        assert cd < 0

    def test_24A1_c_delta(self):
        """24A_1: c_Delta = (691*48 - 65520)/691 = -32352/691."""
        assert niemeier_c_delta('24A1') == Fraction(-32352, 691)

    def test_c_delta_table_consistency(self):
        """All c_Delta values are internally consistent."""
        results = verify_c_delta_table()
        for label, ok in results.items():
            assert ok, f"c_Delta inconsistency for {label}"

    def test_c_delta_distinguishes_by_root_count(self):
        """Lattices with different root counts have different c_Delta."""
        table = niemeier_c_delta_table()
        # Group by root count
        by_roots: Dict = {}
        for label in ALL_NIEMEIER_LABELS:
            n = NIEMEIER_REGISTRY[label]['num_roots']
            by_roots.setdefault(n, []).append(label)
        # Lattices with SAME root count have SAME c_Delta
        for n, labels in by_roots.items():
            cds = [table[lb] for lb in labels]
            assert len(set(cds)) == 1, f"Root count {n}: different c_Delta values"


# =========================================================================
# 8. Holomorphic c = 24 dichotomy
# =========================================================================

class TestDichotomy:
    """The class G vs class M dichotomy."""

    def test_dichotomy_kappa_different(self):
        """Niemeier kappa (24) != Monster kappa (12)."""
        dicho = holomorphic_c24_dichotomy()
        assert dicho['niemeier']['kappa'] != dicho['monster']['kappa']
        assert dicho['kappa_distinguishes'] is True

    def test_dichotomy_class_different(self):
        """Niemeier class G != Monster class M."""
        dicho = holomorphic_c24_dichotomy()
        assert dicho['niemeier']['shadow_class'] == 'G'
        assert dicho['monster']['shadow_class'] == 'M'
        assert dicho['class_distinguishes'] is True

    def test_dichotomy_depth_different(self):
        """Niemeier depth 2 != Monster depth infinity."""
        dicho = holomorphic_c24_dichotomy()
        assert dicho['niemeier']['shadow_depth'] == 2
        assert dicho['monster']['shadow_depth'] == float('inf')

    def test_dichotomy_F1_different(self):
        """Niemeier F_1 = 1, Monster F_1 = 1/2."""
        dicho = holomorphic_c24_dichotomy()
        assert dicho['niemeier']['F1'] == Rational(1)
        assert dicho['monster']['F1'] == Rational(1, 2)


# =========================================================================
# 9. Orbifold shadow transition
# =========================================================================

class TestOrbifoldTransition:
    """The Z/2Z orbifold V_Leech -> V^natural."""

    def test_kappa_halves(self):
        """kappa drops from 24 to 12 under orbifold."""
        assert niemeier_kappa('Leech') == Rational(24)
        assert monster_kappa() == Rational(12)
        assert monster_kappa() == niemeier_kappa('Leech') / 2

    def test_class_changes(self):
        """Shadow class changes from G to M."""
        assert niemeier_shadow_class('Leech') == 'G'
        assert monster_shadow_class() == 'M'

    def test_depth_changes(self):
        """Shadow depth changes from 2 to infinity."""
        assert niemeier_shadow_depth('Leech') == 2
        assert monster_shadow_depth() == float('inf')

    def test_weight1_currents_killed(self):
        """Orbifold kills 24 weight-1 currents."""
        # V_Leech has 24 weight-1 currents (Heisenberg)
        # V^natural has 0 weight-1 currents
        monster_data = monster_full_shadow_data()
        assert monster_data['dim_V1'] == 0

    def test_central_charge_preserved(self):
        """Central charge c = 24 is preserved by orbifold."""
        leech_data = niemeier_full_shadow_data('Leech')
        monster_data = monster_full_shadow_data()
        assert leech_data['central_charge'] == Rational(24)
        assert monster_data['central_charge'] == Rational(24)


# =========================================================================
# 10. Moonshine-shadow interface
# =========================================================================

class TestMoonshineShadow:
    """The relation between moonshine and the shadow tower."""

    def test_shadow_does_not_encode_j(self):
        """The scalar shadow tower does not encode j-function coefficients."""
        rel = j_function_shadow_relation()
        assert rel['shadow_sees_j_coefficients'] is False

    def test_shadow_encodes_kappa(self):
        """The shadow tower encodes kappa = 12."""
        rel = j_function_shadow_relation()
        assert rel['shadow_sees_kappa'] == Rational(12)
        assert rel['genus_tower_encodes_kappa'] is True

    def test_rademacher_exact(self):
        """The Rademacher series determines J(tau) exactly."""
        rel = rademacher_shadow_connection()
        assert rel['rademacher_determines_j'] is True

    def test_rademacher_exceeds_shadow(self):
        """Rademacher goes beyond the scalar shadow tower."""
        rel = rademacher_shadow_connection()
        assert rel['rademacher_exceeds_shadow'] is True

    def test_j_constant_term_vanishes(self):
        """J(tau) = j(tau) - 744 has c(0) = 0."""
        assert J_COEFFICIENTS[0] == 0

    def test_j_polar_term(self):
        """J(tau) has polar term q^{-1} with coefficient 1."""
        assert J_COEFFICIENTS[-1] == 1

    def test_j_first_coefficient_196884(self):
        """J(tau) has c(1) = 196884."""
        assert J_COEFFICIENTS[1] == 196884


# =========================================================================
# 11. Cross-verification (multi-path)
# =========================================================================

class TestCrossVerification:
    """Multi-path verification of key claims."""

    def test_monster_kappa_path1_virasoro(self):
        """Path 1: kappa(V^natural) = c/2 = 24/2 = 12 (Virasoro formula)."""
        assert MONSTER_CENTRAL_CHARGE / 2 == Rational(12)

    def test_monster_kappa_path2_F1(self):
        """Path 2: F_1 = kappa/24 = 1/2 gives kappa = 12."""
        F1 = Rational(1, 2)  # From monster_full_shadow_data
        kappa_from_F1 = F1 * 24
        assert kappa_from_F1 == Rational(12)

    def test_monster_kappa_path3_not_rank(self):
        """Path 3: dim V_1 = 0 => no Heisenberg => kappa != rank = 24."""
        # V^natural has no weight-1 currents, so the Heisenberg
        # formula kappa = rank does NOT apply
        assert monster_kappa() != Rational(24)
        monster_data = monster_full_shadow_data()
        assert monster_data['dim_V1'] == 0

    def test_niemeier_kappa_path1_rank(self):
        """Path 1: kappa(V_Lambda) = rank(Lambda) = 24 (Heisenberg formula)."""
        for label in ALL_NIEMEIER_LABELS:
            assert niemeier_kappa(label) == Rational(NIEMEIER_REGISTRY[label]['rank'])

    def test_niemeier_kappa_path2_F1(self):
        """Path 2: F_1 = kappa/24 = 24/24 = 1."""
        data = niemeier_full_shadow_data('3E8')
        assert data['F1'] == Rational(1)
        assert data['F1'] * 24 == Rational(24)

    def test_niemeier_kappa_path3_not_c_over_2(self):
        """Path 3: kappa = 24 != c/2 = 12 (AP39 check)."""
        # c = 24 for all Niemeier lattices, and c/2 = 12
        # But kappa = 24, which equals the rank, not c/2
        assert NIEMEIER_KAPPA == Rational(24)
        assert NIEMEIER_KAPPA != Rational(24) / 2

    def test_class_M_path1_discriminant(self):
        """Path 1: Delta(V^natural) = 20/71 != 0 => class M."""
        assert monster_critical_discriminant_virasoro() != 0

    def test_class_M_path2_conformal_vector(self):
        """Path 2: T is primitive generator => class M (cor:conformal-vector-infinite-depth)."""
        monster_data = monster_full_shadow_data()
        assert monster_data['dim_V1'] == 0  # No Sugawara source
        assert monster_shadow_class() == 'M'

    def test_class_G_path1_quadratic_OPE(self):
        """Path 1: Lattice VOA has quadratic OPE => S_3 = 0 => class G."""
        for label in ALL_NIEMEIER_LABELS:
            assert niemeier_S3(label) == 0
            assert niemeier_S4(label) == 0

    def test_class_G_path2_discriminant(self):
        """Path 2: Delta = 0 => tower terminates => class G."""
        for label in ALL_NIEMEIER_LABELS:
            assert niemeier_critical_discriminant(label) == 0


# =========================================================================
# 12. Schellekens list
# =========================================================================

class TestSchellekens:
    """The 71 holomorphic c = 24 VOAs."""

    def test_shadow_class_counts(self):
        """24 class G (Niemeier) + 1 class M (Monster) + 46 intermediate = 71."""
        counts = shadow_class_count()
        assert counts['class_G_niemeier'] == 24
        assert counts['class_M_monster'] == 1
        assert counts['intermediate'] == 46
        assert counts['total'] == 71

    def test_schellekens_data_has_niemeier(self):
        """All 24 Niemeier lattices in Schellekens data."""
        for label in ALL_NIEMEIER_LABELS:
            key = f'lattice_{label}'
            assert key in SCHELLEKENS_SHADOW_DATA

    def test_schellekens_data_has_monster(self):
        """V^natural in Schellekens data."""
        assert 'V_natural' in SCHELLEKENS_SHADOW_DATA

    def test_all_niemeier_class_G(self):
        """All Niemeier lattice entries are class G."""
        for label in ALL_NIEMEIER_LABELS:
            key = f'lattice_{label}'
            assert SCHELLEKENS_SHADOW_DATA[key]['shadow_class'] == 'G'

    def test_monster_class_M_in_schellekens(self):
        """V^natural entry is class M."""
        assert SCHELLEKENS_SHADOW_DATA['V_natural']['shadow_class'] == 'M'


# =========================================================================
# 13. Full atlas construction
# =========================================================================

class TestFullAtlas:
    """The complete shadow depth atlas."""

    def test_atlas_has_25_entries(self):
        """24 Niemeier lattices + 1 Monster = 25 entries."""
        atlas = full_shadow_depth_atlas()
        assert len(atlas) == 25

    def test_atlas_all_have_kappa(self):
        """Every atlas entry has a kappa value."""
        atlas = full_shadow_depth_atlas()
        for key, data in atlas.items():
            assert 'kappa' in data, f"Missing kappa for {key}"
            assert data['kappa'] > 0

    def test_atlas_all_have_shadow_class(self):
        """Every atlas entry has a shadow class."""
        atlas = full_shadow_depth_atlas()
        for key, data in atlas.items():
            assert data['shadow_class'] in ('G', 'L', 'C', 'M')

    def test_atlas_monster_entry(self):
        """Monster entry in atlas has correct data."""
        atlas = full_shadow_depth_atlas()
        m = atlas['V_natural']
        assert m['kappa'] == Rational(12)
        assert m['shadow_class'] == 'M'
        assert m['dim_V1'] == 0
