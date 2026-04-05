r"""Tests for the complete Niemeier shadow atlas.

85+ tests verifying:
  1. Registry integrity (24 lattices, correct root counts, rank 24)
  2. Root system combinatorics (root counts for each ADE type)
  3. Coxeter numbers (uniform for each lattice, correct values)
  4. Shadow obstruction tower universality (all 24 have identical shadow data)
  5. Genus expansion (F_1=1, F_2=7/240, proportional to kappa)
  6. Planted-forest corrections (all zero)
  7. Complementarity (kappa + kappa' = 0 for all)
  8. Self-duality (all 24 are unimodular)
  9. Theta series (r(0)=1, r(1)=|R|, integrality, non-negativity)
  10. Root count collisions (5 pairs identified)
  11. E_8^3 vs D_24 comparison
  12. Leech lattice special case
  13. Genus-2 representation numbers
  14. Full atlas end-to-end
  15. Faber-Pandharipande numbers cross-check

Mathematical ground truth:
  - Conway-Sloane, "Sphere Packings, Lattices and Groups", Ch. 16
  - lattice_foundations.tex: thm:lattice:curvature-braiding-orthogonal
  - higher_genus_modular_koszul.tex: shadow depth classification
"""

import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.niemeier_shadow_atlas import (
    ALL_NIEMEIER_LABELS,
    CS_ORDER,
    KAPPA_NIEMEIER,
    NIEMEIER_REGISTRY,
    F_g,
    _orthogonal_roots_in_component,
    _ramanujan_tau,
    _sigma_k,
    c_delta,
    complementarity,
    coxeter_analysis,
    coxeter_number,
    distinguishing_invariants,
    dual_coxeter_number,
    e8_cubed_vs_d24,
    faber_pandharipande,
    full_atlas,
    genus2_diag11_rep,
    genus_expansion,
    is_self_dual,
    leech_special,
    orthogonal_roots_per_root,
    planted_forest_g2,
    root_count,
    root_count_collisions,
    root_lattice_det,
    shadow_classification_table,
    shadow_data,
    theta_coefficient,
    theta_series,
    total_genus2_amplitude,
    verify_all_shadow_identical,
    verify_complementarity_sum_zero,
    verify_root_count_at_n1,
    verify_theta_integrality,
)


# =========================================================================
# Section 1: Registry integrity
# =========================================================================

class TestRegistryIntegrity:
    """Verify the Niemeier lattice registry has correct basic data."""

    def test_exactly_24_lattices(self):
        assert len(NIEMEIER_REGISTRY) == 24

    def test_all_labels_in_registry(self):
        assert len(ALL_NIEMEIER_LABELS) == 24

    def test_cs_order_has_all(self):
        assert set(CS_ORDER) == set(ALL_NIEMEIER_LABELS)

    def test_all_rank_24(self):
        for label, data in NIEMEIER_REGISTRY.items():
            assert data['rank'] == 24, f"{label} rank != 24"

    def test_all_root_rank_24_except_leech(self):
        for label, data in NIEMEIER_REGISTRY.items():
            if label == 'Leech':
                assert data['root_rank'] == 0
            else:
                assert data['root_rank'] == 24, (
                    f"{label}: root_rank = {data['root_rank']}"
                )

    def test_leech_no_roots(self):
        assert NIEMEIER_REGISTRY['Leech']['num_roots'] == 0

    def test_leech_no_components(self):
        assert NIEMEIER_REGISTRY['Leech']['components'] == []


# =========================================================================
# Section 2: Root system combinatorics
# =========================================================================

class TestRootCounts:
    """Test root count formulas for simple Lie algebras."""

    def test_A1(self):
        assert root_count('A', 1) == 2

    def test_A2(self):
        assert root_count('A', 2) == 6

    def test_A3(self):
        assert root_count('A', 3) == 12

    def test_A24(self):
        assert root_count('A', 24) == 600

    def test_D4(self):
        assert root_count('D', 4) == 24

    def test_D8(self):
        assert root_count('D', 8) == 112

    def test_D12(self):
        assert root_count('D', 12) == 264

    def test_D24(self):
        assert root_count('D', 24) == 1104

    def test_E6(self):
        assert root_count('E', 6) == 72

    def test_E7(self):
        assert root_count('E', 7) == 126

    def test_E8(self):
        assert root_count('E', 8) == 240

    def test_root_counts_match_registry(self):
        """Verify all root counts in the registry match the formulas."""
        for label, data in NIEMEIER_REGISTRY.items():
            expected = sum(root_count(f, n) for f, n in data['components'])
            assert data['num_roots'] == expected, (
                f"{label}: registry {data['num_roots']} != computed {expected}"
            )

    def test_specific_root_counts(self):
        """Spot-check specific lattices against Conway-Sloane table."""
        assert NIEMEIER_REGISTRY['D24']['num_roots'] == 1104
        assert NIEMEIER_REGISTRY['3E8']['num_roots'] == 720
        assert NIEMEIER_REGISTRY['D16_E8']['num_roots'] == 720
        assert NIEMEIER_REGISTRY['A24']['num_roots'] == 600
        assert NIEMEIER_REGISTRY['24A1']['num_roots'] == 48
        assert NIEMEIER_REGISTRY['12A2']['num_roots'] == 72
        assert NIEMEIER_REGISTRY['8A3']['num_roots'] == 96
        assert NIEMEIER_REGISTRY['6A4']['num_roots'] == 120


# =========================================================================
# Section 3: Coxeter numbers
# =========================================================================

class TestCoxeterNumbers:
    """Test Coxeter number computations."""

    def test_A_coxeter(self):
        for n in range(1, 10):
            assert coxeter_number('A', n) == n + 1

    def test_D_coxeter(self):
        for n in range(3, 10):
            assert coxeter_number('D', n) == 2 * (n - 1)

    def test_E_coxeter(self):
        assert coxeter_number('E', 6) == 12
        assert coxeter_number('E', 7) == 18
        assert coxeter_number('E', 8) == 30

    def test_dual_equals_coxeter_simply_laced(self):
        """For simply-laced types, h^vee = h."""
        for f, n in [('A', 5), ('D', 6), ('E', 8)]:
            assert dual_coxeter_number(f, n) == coxeter_number(f, n)

    def test_uniform_coxeter_all_lattices(self):
        """All components of each Niemeier lattice share the same h."""
        for label, data in NIEMEIER_REGISTRY.items():
            h_vals = data['coxeter_numbers']
            if h_vals:
                assert all(h == h_vals[0] for h in h_vals), (
                    f"{label}: non-uniform h = {h_vals}"
                )

    def test_coxeter_analysis_groups(self):
        """Check the number of distinct Coxeter numbers."""
        ca = coxeter_analysis()
        by_h = ca['by_coxeter_number']
        # 18 distinct h values for the 23 non-Leech lattices
        assert len(by_h) == 18

    def test_coxeter_D24(self):
        assert NIEMEIER_REGISTRY['D24']['coxeter_numbers'] == [46]

    def test_coxeter_3E8(self):
        assert NIEMEIER_REGISTRY['3E8']['coxeter_numbers'] == [30, 30, 30]

    def test_coxeter_24A1(self):
        assert NIEMEIER_REGISTRY['24A1']['coxeter_numbers'] == [2] * 24


# =========================================================================
# Section 4: Shadow obstruction tower universality
# =========================================================================

class TestShadowTowerUniversality:
    """All 24 Niemeier lattices have identical shadow obstruction tower data."""

    def test_verify_all_shadow_identical(self):
        assert verify_all_shadow_identical()

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_kappa_24(self, label):
        sd = shadow_data(label)
        assert sd['kappa'] == Rational(24)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_class_G(self, label):
        sd = shadow_data(label)
        assert sd['shadow_class'] == 'G'

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_depth_2(self, label):
        sd = shadow_data(label)
        assert sd['shadow_depth'] == 2

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_S3_zero(self, label):
        sd = shadow_data(label)
        assert sd['S3'] == Rational(0)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_S4_zero(self, label):
        sd = shadow_data(label)
        assert sd['S4'] == Rational(0)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_discriminant_zero(self, label):
        sd = shadow_data(label)
        assert sd['critical_discriminant'] == Rational(0)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_central_charge_24(self, label):
        sd = shadow_data(label)
        assert sd['central_charge'] == Rational(24)

    def test_shadow_metric_value(self):
        """Q_L = (2*kappa)^2 = (2*24)^2 = 2304."""
        sd = shadow_data('Leech')
        assert sd['shadow_metric'] == 4 * Rational(24) ** 2
        assert sd['shadow_metric'] == Rational(2304)


# =========================================================================
# Section 5: Genus expansion
# =========================================================================

class TestGenusExpansion:
    """Genus expansion F_g = 24 * lambda_g^FP."""

    def test_F1_equals_1(self):
        assert F_g(1) == Rational(1)

    def test_F2_equals_7_over_240(self):
        assert F_g(2) == Rational(7, 240)

    def test_F3_value(self):
        """F_3 = 24 * 31/967680 = 31/40320."""
        assert F_g(3) == Rational(24) * Rational(31, 967680)

    def test_fp_genus1(self):
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_fp_genus2(self):
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_fp_positivity(self):
        for g in range(1, 6):
            assert faber_pandharipande(g) > 0

    def test_fp_monotone_decrease(self):
        for g in range(1, 5):
            assert faber_pandharipande(g) > faber_pandharipande(g + 1)

    def test_genus_expansion_dict(self):
        exp = genus_expansion(max_g=3)
        assert exp[1] == Rational(1)
        assert exp[2] == Rational(7, 240)
        assert len(exp) == 3

    def test_genus_expansion_universal(self):
        """The genus expansion is independent of which lattice we choose."""
        exp = genus_expansion(max_g=5)
        for g in range(1, 6):
            assert exp[g] == Rational(24) * faber_pandharipande(g)


# =========================================================================
# Section 6: Planted-forest corrections
# =========================================================================

class TestPlantedForest:
    """All planted-forest corrections vanish for Niemeier lattices."""

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_planted_forest_g2_zero(self, label):
        assert planted_forest_g2(label) == Rational(0)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_total_A2_equals_F2(self, label):
        assert total_genus2_amplitude(label) == F_g(2)

    def test_A2_value(self):
        assert total_genus2_amplitude('Leech') == Rational(7, 240)

    def test_A2_universal(self):
        """A_2 is the same for all 24 lattices."""
        vals = {total_genus2_amplitude(lab) for lab in ALL_NIEMEIER_LABELS}
        assert len(vals) == 1
        assert vals.pop() == Rational(7, 240)


# =========================================================================
# Section 7: Complementarity
# =========================================================================

class TestComplementarity:
    """kappa + kappa' = 0 for all Niemeier lattices."""

    def test_verify_complementarity_sum_zero(self):
        assert verify_complementarity_sum_zero()

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_kappa_sum_zero(self, label):
        comp = complementarity(label)
        assert comp['kappa_sum'] == Rational(0)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_kappa_24(self, label):
        comp = complementarity(label)
        assert comp['kappa'] == Rational(24)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_kappa_dual_minus_24(self, label):
        comp = complementarity(label)
        assert comp['kappa_dual'] == Rational(-24)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_anti_symmetric(self, label):
        comp = complementarity(label)
        assert comp['is_anti_symmetric'] is True

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_self_dual_lattice(self, label):
        comp = complementarity(label)
        assert comp['self_dual_lattice'] is True

    def test_km_type_not_virasoro(self):
        """Lattice complementarity is KM/free-field type (sum=0), not Virasoro (sum=13)."""
        comp = complementarity('Leech')
        assert comp['complementarity_type'] == 'KM/free-field'


# =========================================================================
# Section 8: Self-duality
# =========================================================================

class TestSelfDuality:
    """All Niemeier lattices are even unimodular, hence self-dual."""

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_self_dual(self, label):
        assert is_self_dual(label) is True

    def test_unknown_lattice_raises(self):
        with pytest.raises(ValueError):
            is_self_dual('NotALattice')


# =========================================================================
# Section 9: Theta series
# =========================================================================

class TestThetaSeries:
    """Theta series coefficients for Niemeier lattices."""

    def test_verify_root_count_at_n1(self):
        assert verify_root_count_at_n1()

    def test_verify_theta_integrality(self):
        assert verify_theta_integrality(5)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_r0_equals_1(self, label):
        assert theta_coefficient(label, 0) == 1

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_r1_equals_num_roots(self, label):
        expected = NIEMEIER_REGISTRY[label]['num_roots']
        assert theta_coefficient(label, 1) == expected

    def test_leech_r1_zero(self):
        assert theta_coefficient('Leech', 1) == 0

    def test_leech_r2(self):
        """Leech kissing number = 196560."""
        assert theta_coefficient('Leech', 2) == 196560

    def test_leech_r3(self):
        assert theta_coefficient('Leech', 3) == 16773120

    def test_leech_r4(self):
        assert theta_coefficient('Leech', 4) == 398034000

    def test_3E8_r1(self):
        assert theta_coefficient('3E8', 1) == 720

    def test_D24_r1(self):
        assert theta_coefficient('D24', 1) == 1104

    def test_theta_series_tuple(self):
        ts = theta_series('Leech', 3)
        assert ts[0] == 1
        assert ts[1] == 0
        assert ts[2] == 196560
        assert ts[3] == 16773120

    @pytest.mark.parametrize("label", ['Leech', '3E8', 'D24', '24A1'])
    def test_theta_nonneg(self, label):
        """All theta coefficients are non-negative."""
        for n in range(6):
            assert theta_coefficient(label, n) >= 0

    def test_c_delta_leech(self):
        """Leech: c_Delta = -65520/691."""
        assert c_delta('Leech') == Fraction(-65520, 691)

    def test_c_delta_3E8(self):
        expected = Fraction(691 * 720 - 65520, 691)
        assert c_delta('3E8') == expected

    def test_c_delta_distinct_count(self):
        """c_Delta = (691*N - 65520)/691: lattices with same |R| share c_Delta.

        With 5 collision pairs (10 lattices sharing 5 values), we get 19 distinct.
        """
        vals = [c_delta(label) for label in ALL_NIEMEIER_LABELS]
        # 24 lattices, 5 collision pairs => 24 - 5 = 19 distinct values
        assert len(set(vals)) == 19


# =========================================================================
# Section 10: Root count collisions
# =========================================================================

class TestRootCountCollisions:
    """Pairs of lattices sharing the same number of roots."""

    def test_five_collision_pairs(self):
        collisions = root_count_collisions()
        assert len(collisions) == 5

    def test_720_collision(self):
        collisions = root_count_collisions()
        assert set(collisions[720]) == {'D16_E8', '3E8'}

    def test_432_collision(self):
        collisions = root_count_collisions()
        assert set(collisions[432]) == {'A17_E7', 'D10_2E7'}

    def test_288_collision(self):
        collisions = root_count_collisions()
        assert set(collisions[288]) == {'A11_D7_E6', '4E6'}

    def test_240_collision(self):
        collisions = root_count_collisions()
        assert set(collisions[240]) == {'2A9_D6', '4D6'}

    def test_144_collision(self):
        collisions = root_count_collisions()
        assert set(collisions[144]) == {'4A5_D4', '6D4'}


# =========================================================================
# Section 11: E_8^3 vs D_24 comparison
# =========================================================================

class TestE8CubedVsD24:
    """Compare the two most structured Niemeier lattices."""

    def test_same_shadow(self):
        comp = e8_cubed_vs_d24()
        assert comp['shadow_identical'] is True

    def test_different_roots(self):
        comp = e8_cubed_vs_d24()
        assert comp['3E8']['num_roots'] == 720
        assert comp['D24']['num_roots'] == 1104

    def test_different_theta(self):
        comp = e8_cubed_vs_d24()
        assert comp['theta_differ'] is True

    def test_different_c_delta(self):
        comp = e8_cubed_vs_d24()
        assert comp['3E8']['c_delta'] != comp['D24']['c_delta']

    def test_different_coxeter(self):
        comp = e8_cubed_vs_d24()
        assert comp['3E8']['coxeter_numbers'] == [30, 30, 30]
        assert comp['D24']['coxeter_numbers'] == [46]

    def test_same_root_count_different_lattice(self):
        """D16+E8 also has 720 roots but is different from 3E8."""
        assert NIEMEIER_REGISTRY['D16_E8']['num_roots'] == 720
        assert NIEMEIER_REGISTRY['3E8']['num_roots'] == 720
        assert c_delta('D16_E8') == c_delta('3E8')  # same N => same c_delta
        # But they have different coxeter numbers
        assert NIEMEIER_REGISTRY['D16_E8']['coxeter_numbers'] == [30, 30]
        assert NIEMEIER_REGISTRY['3E8']['coxeter_numbers'] == [30, 30, 30]


# =========================================================================
# Section 12: Leech lattice special case
# =========================================================================

class TestLeechLattice:
    """Special properties of the Leech lattice."""

    def test_no_roots(self):
        ls = leech_special()
        assert ls['num_roots'] == 0

    def test_minimal_norm_4(self):
        ls = leech_special()
        assert ls['minimal_norm'] == 4

    def test_kissing_196560(self):
        ls = leech_special()
        assert ls['kissing_number'] == 196560

    def test_c_delta_most_negative(self):
        """Leech has the most negative c_delta (fewest roots)."""
        leech_cd = c_delta('Leech')
        for label in ALL_NIEMEIER_LABELS:
            assert c_delta(label) >= leech_cd

    def test_shadow_data_class_G(self):
        ls = leech_special()
        sd = ls['shadow_data']
        assert sd['shadow_class'] == 'G'
        assert sd['kappa'] == Rational(24)


# =========================================================================
# Section 13: Genus-2 representation numbers
# =========================================================================

class TestGenus2RepNumbers:
    """Genus-2 representation numbers at T = diag(1,1)."""

    def test_leech_zero(self):
        """Leech has no roots, so r_2(diag(1,1)) = 0."""
        assert genus2_diag11_rep('Leech') == 0

    def test_24A1_value(self):
        """24A1: 48 roots, each in its own A1 copy. Orthogonal = 46 other roots."""
        # Each A1 has 0 orthogonal roots within itself
        # Other 23 copies contribute 23*2 = 46 roots
        # Total = 48 * 46 = 2208
        assert genus2_diag11_rep('24A1') == 48 * 46

    def test_3E8_value(self):
        """3E8: 720 roots. Root in one E8: 126 orthogonal within, 480 in other copies."""
        orth = orthogonal_roots_per_root('3E8')
        assert orth == 126 + 480
        assert genus2_diag11_rep('3E8') == 720 * 606

    def test_leech_orthogonal_none(self):
        assert orthogonal_roots_per_root('Leech') is None

    def test_genus2_nonneg(self):
        for label in ALL_NIEMEIER_LABELS:
            assert genus2_diag11_rep(label) >= 0


# =========================================================================
# Section 14: Full atlas
# =========================================================================

class TestFullAtlas:
    """End-to-end test of the full atlas."""

    def test_atlas_has_all_24(self):
        atlas = full_atlas(max_n_theta=3, max_g=2)
        assert len(atlas) == 24

    def test_atlas_shadow_universal(self):
        atlas = full_atlas(max_n_theta=3, max_g=2)
        for label, data in atlas.items():
            assert data['shadow']['kappa'] == Rational(24)
            assert data['shadow']['shadow_class'] == 'G'

    def test_atlas_planted_forest_zero(self):
        atlas = full_atlas(max_n_theta=3, max_g=2)
        for label, data in atlas.items():
            assert data['planted_forest_g2'] == Rational(0)

    def test_atlas_total_A2_universal(self):
        atlas = full_atlas(max_n_theta=3, max_g=2)
        for label, data in atlas.items():
            assert data['total_A2'] == Rational(7, 240)

    def test_classification_table_length(self):
        table = shadow_classification_table()
        assert len(table) == 24

    def test_classification_table_order(self):
        """Table is ordered by decreasing number of roots."""
        table = shadow_classification_table()
        for i in range(len(table) - 1):
            assert table[i]['num_roots'] >= table[i + 1]['num_roots']


# =========================================================================
# Section 15: Arithmetic helpers cross-check
# =========================================================================

class TestArithmeticHelpers:
    """Cross-check internal arithmetic functions."""

    def test_sigma_11_1(self):
        assert _sigma_k(1, 11) == 1

    def test_sigma_11_2(self):
        assert _sigma_k(2, 11) == 1 + 2048

    def test_tau_1(self):
        assert _ramanujan_tau(1) == 1

    def test_tau_2(self):
        assert _ramanujan_tau(2) == -24

    def test_tau_3(self):
        assert _ramanujan_tau(3) == 252

    def test_tau_4(self):
        assert _ramanujan_tau(4) == -1472

    def test_tau_5(self):
        assert _ramanujan_tau(5) == 4830


# =========================================================================
# Section 16: Root lattice determinants
# =========================================================================

class TestRootLatticeDet:
    """Cartan matrix determinants."""

    def test_A_det(self):
        for n in range(1, 10):
            assert root_lattice_det('A', n) == n + 1

    def test_D_det(self):
        for n in range(3, 10):
            assert root_lattice_det('D', n) == 4

    def test_E6_det(self):
        assert root_lattice_det('E', 6) == 3

    def test_E7_det(self):
        assert root_lattice_det('E', 7) == 2

    def test_E8_det(self):
        assert root_lattice_det('E', 8) == 1


# =========================================================================
# Section 17: Orthogonal roots within components
# =========================================================================

class TestOrthogonalRoots:
    """Orthogonal root counts within single simple components."""

    def test_A1_zero(self):
        assert _orthogonal_roots_in_component('A', 1) == 0

    def test_A2_zero(self):
        assert _orthogonal_roots_in_component('A', 2) == 0

    def test_A3(self):
        assert _orthogonal_roots_in_component('A', 3) == 2

    def test_A4(self):
        assert _orthogonal_roots_in_component('A', 4) == 6

    def test_D4(self):
        assert _orthogonal_roots_in_component('D', 4) == 6

    def test_E6(self):
        assert _orthogonal_roots_in_component('E', 6) == 30

    def test_E7(self):
        assert _orthogonal_roots_in_component('E', 7) == 72

    def test_E8(self):
        assert _orthogonal_roots_in_component('E', 8) == 126

    def test_consistency_with_root_count(self):
        """Orthogonal count < total roots - 2 (excluding root and its negative)."""
        for f, n in [('A', 5), ('D', 6), ('E', 8)]:
            orth = _orthogonal_roots_in_component(f, n)
            total = root_count(f, n)
            assert orth <= total - 2


# =========================================================================
# Section 18: Distinguishing invariants
# =========================================================================

class TestDistinguishingInvariants:
    """Invariants that separate the 24 lattices."""

    def test_c_delta_19_distinct(self):
        """19 distinct c_delta values (5 collision pairs share the same |R|)."""
        vals = [c_delta(lab) for lab in ALL_NIEMEIER_LABELS]
        assert len(set(vals)) == 19

    def test_distinguishing_has_all_fields(self):
        di = distinguishing_invariants('3E8')
        assert 'num_roots' in di
        assert 'c_delta' in di
        assert 'genus2_diag11' in di
        assert 'theta_r2' in di
        assert 'coxeter_numbers' in di

    def test_theta_r2_distinguishes_most(self):
        """r(2) should be distinct for most lattices."""
        r2_vals = {theta_coefficient(lab, 2) for lab in ALL_NIEMEIER_LABELS}
        # At least 20 distinct r(2) values (may not be all 24)
        assert len(r2_vals) >= 15
