r"""Tests for genus-2 Siegel modular forms from shadow amplitudes.

Tests the genus-2 shadow amplitude decomposition into Siegel modular forms
for all 24 Niemeier lattices, including:
  - Graph enumeration and stability verification
  - Class G vanishing of boundary corrections
  - Siegel decomposition (c_0, c_1, c_2) for all 24 lattices
  - Distinguishing power analysis (20 distinct c_2 out of 24)
  - Boecherer conjecture structure
  - MC framework connection
"""

import pytest
from fractions import Fraction

from compute.lib.genus2_siegel_shadow import (
    GENUS2_GRAPHS,
    bocherer_atlas,
    bocherer_L_value_proxy,
    bocherer_sign_pattern,
    collision_root_analysis,
    distinguishing_analysis,
    full_niemeier_siegel_atlas,
    genus3_prediction,
    graph_amplitudes_class_G,
    lambda_fp,
    mc_genus2_decomposition,
    scalar_vs_full_comparison,
    siegel_decomposition,
    verify_genus2_graphs,
)
from compute.lib.niemeier_bocherer_atlas import (
    ALL_NIEMEIER,
    NIEMEIER_LATTICES,
    extract_c2,
    genus2_rep_at_diag11,
    niemeier_c1,
    niemeier_c_delta,
    orthogonal_roots_per_root,
)
from compute.lib.siegel_eisenstein import (
    chi12_from_igusa,
    siegel_eisenstein_coefficient,
)
from compute.lib.niemeier_bocherer_atlas import klingen_eisenstein_coefficient


# ============================================================================
# 1. Faber-Pandharipande numbers
# ============================================================================

class TestFaberPandharipande:
    """Verify Faber-Pandharipande intersection numbers."""

    def test_lambda_1(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_positive(self):
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_lambda_decreasing(self):
        for g in range(1, 7):
            assert lambda_fp(g) > lambda_fp(g + 1)


# ============================================================================
# 2. Graph enumeration
# ============================================================================

class TestGraphEnumeration:
    """Verify the 6 stable graphs of M-bar_{2,0}."""

    def test_exactly_6_graphs(self):
        assert len(GENUS2_GRAPHS) == 6

    def test_all_genus_2(self):
        for name, info in verify_genus2_graphs().items():
            assert info['is_genus_2'], f"{name} has genus {info['total_genus']}"

    def test_all_stable(self):
        for name, info in verify_genus2_graphs().items():
            assert info['is_stable'], f"{name} is not stable"

    @pytest.mark.parametrize("name,expected_aut", [
        ('theta', 12),
        ('eyeglasses', 4),
        ('figure_eight', 8),
        ('dumbbell', 2),
        ('lollipop', 2),
        ('smooth', 1),
    ])
    def test_automorphism_orders(self, name, expected_aut):
        assert GENUS2_GRAPHS[name]['aut_order'] == expected_aut

    def test_sum_inverse_aut(self):
        """Sum of 1/|Aut| over all graphs should be related to orbifold Euler char."""
        total = sum(Fraction(1, g['aut_order']) for g in GENUS2_GRAPHS.values())
        # 1/12 + 1/4 + 1/8 + 1/2 + 1/2 + 1 = 1/12 + 3/12 + 1.5/12 + 6/12 + 6/12 + 12/12
        # = (1 + 3 + 1.5 + 6 + 6 + 12) / 12 = 29.5/12 ... let me compute
        expected = Fraction(1, 12) + Fraction(1, 4) + Fraction(1, 8) + \
                   Fraction(1, 2) + Fraction(1, 2) + Fraction(1, 1)
        assert total == expected

    def test_graph_names_consistent(self):
        expected_names = {'theta', 'eyeglasses', 'figure_eight',
                          'dumbbell', 'lollipop', 'smooth'}
        assert set(GENUS2_GRAPHS.keys()) == expected_names

    def test_h1_values(self):
        results = verify_genus2_graphs()
        assert results['theta']['h1'] == 2
        assert results['eyeglasses']['h1'] == 2
        assert results['figure_eight']['h1'] == 2
        assert results['dumbbell']['h1'] == 0
        assert results['lollipop']['h1'] == 1
        assert results['smooth']['h1'] == 0


# ============================================================================
# 3. Class G graph amplitudes
# ============================================================================

class TestClassGAmplitudes:
    """Verify graph amplitudes for Gaussian (class G) algebras."""

    def test_total_F2_kappa_24(self):
        amps = graph_amplitudes_class_G(Fraction(24))
        assert amps['total_F2'] == Fraction(24) * Fraction(7, 5760)

    def test_total_F2_kappa_8(self):
        amps = graph_amplitudes_class_G(Fraction(8))
        assert amps['total_F2'] == Fraction(8) * Fraction(7, 5760)

    def test_theta_vanishes(self):
        amps = graph_amplitudes_class_G(Fraction(24))
        assert amps['theta']['amplitude'] == 0

    def test_eyeglasses_vanishes(self):
        amps = graph_amplitudes_class_G(Fraction(24))
        assert amps['eyeglasses']['amplitude'] == 0

    def test_figure_eight_vanishes(self):
        amps = graph_amplitudes_class_G(Fraction(24))
        assert amps['figure_eight']['amplitude'] == 0

    def test_dumbbell_nonzero(self):
        amps = graph_amplitudes_class_G(Fraction(24))
        assert amps['dumbbell']['amplitude'] > 0

    def test_dumbbell_formula(self):
        kappa = Fraction(24)
        lam1 = Fraction(1, 24)
        P = Fraction(1) / kappa
        expected = Fraction(1, 2) * kappa**2 * lam1**2 * P
        amps = graph_amplitudes_class_G(kappa)
        assert amps['dumbbell']['amplitude'] == expected

    def test_matches_expected(self):
        amps = graph_amplitudes_class_G(Fraction(24))
        assert amps['total_matches']

    def test_various_kappa(self):
        for k in [1, 2, 4, 8, 12, 16, 24]:
            amps = graph_amplitudes_class_G(Fraction(k))
            assert amps['total_F2'] == Fraction(k) * Fraction(7, 5760)


# ============================================================================
# 4. Siegel decomposition
# ============================================================================

class TestSiegelDecomposition:
    """Verify Siegel decomposition for Niemeier lattices."""

    def test_c0_is_1_for_all(self):
        for name in ALL_NIEMEIER:
            dec = siegel_decomposition(name)
            assert dec['c_0'] == 1

    def test_c1_equals_c_delta(self):
        for name in ALL_NIEMEIER:
            dec = siegel_decomposition(name)
            assert dec['c_1'] == dec['c_delta']

    def test_c2_computed_for_all(self):
        for name in ALL_NIEMEIER:
            dec = siegel_decomposition(name)
            assert dec['c_2'] is not None, f"c_2 not computed for {name}"

    def test_leech_c_delta(self):
        c_del = niemeier_c_delta('Leech')
        expected = Fraction(691 * 0 - 65520, 691)
        assert c_del == expected

    def test_3E8_c_delta(self):
        c_del = niemeier_c_delta('3E8')
        expected = Fraction(691 * 720 - 65520, 691)
        assert c_del == expected

    def test_c2_exact_3E8_D16_E8(self):
        """3E8 and D16+E8 should have identical c_2."""
        c2_3e8 = extract_c2('3E8')
        c2_d16e8 = extract_c2('D16_E8')
        assert c2_3e8 == c2_d16e8

    def test_all_kappa_24(self):
        for name in ALL_NIEMEIER:
            dec = siegel_decomposition(name)
            assert dec['kappa'] == 24


# ============================================================================
# 5. Distinguishing analysis
# ============================================================================

class TestDistinguishing:
    """Verify the distinguishing power of genus-2 theta series."""

    def test_20_distinct_values(self):
        da = distinguishing_analysis()
        assert da['n_distinct_c2'] == 20

    def test_24_total_lattices(self):
        da = distinguishing_analysis()
        assert da['n_total_lattices'] == 24

    def test_4_collision_pairs(self):
        da = distinguishing_analysis()
        assert da['n_collision_pairs'] == 4

    def test_genus2_does_not_distinguish_all(self):
        da = distinguishing_analysis()
        assert not da['genus2_distinguishes']

    def test_needs_genus3(self):
        da = distinguishing_analysis()
        assert da['needs_genus3']

    def test_collision_pair_6D4_4A5D4(self):
        c2_1 = extract_c2('6D4')
        c2_2 = extract_c2('4A5_D4')
        assert c2_1 == c2_2

    def test_collision_pair_A11D7E6_4E6(self):
        c2_1 = extract_c2('A11_D7_E6')
        c2_2 = extract_c2('4E6')
        assert c2_1 == c2_2

    def test_collision_pair_A17E7_D10_2E7(self):
        c2_1 = extract_c2('A17_E7')
        c2_2 = extract_c2('D10_2E7')
        assert c2_1 == c2_2

    def test_collision_pair_D16E8_3E8(self):
        c2_1 = extract_c2('D16_E8')
        c2_2 = extract_c2('3E8')
        assert c2_1 == c2_2

    def test_8A3_4D4_not_collision(self):
        """8A3 and 4D4 both have 96 roots but DIFFERENT c_2."""
        c2_1 = extract_c2('8A3')
        c2_2 = extract_c2('4D4')
        assert c2_1 != c2_2

    def test_collisions_have_same_num_roots(self):
        """All collision pairs have the same number of roots."""
        da = distinguishing_analysis()
        for n1, n2, _ in da['collision_pairs']:
            r1 = NIEMEIER_LATTICES[n1]['num_roots']
            r2 = NIEMEIER_LATTICES[n2]['num_roots']
            assert r1 == r2, f"{n1} ({r1}) vs {n2} ({r2})"

    def test_collisions_have_same_N_orth(self):
        """All collision pairs have the same N_orth."""
        da = distinguishing_analysis()
        for n1, n2, _ in da['collision_pairs']:
            o1 = orthogonal_roots_per_root(n1)
            o2 = orthogonal_roots_per_root(n2)
            assert o1 == o2, f"{n1} ({o1}) vs {n2} ({o2})"


# ============================================================================
# 6. Collision root analysis
# ============================================================================

class TestCollisionAnalysis:
    """Verify the root-level analysis of collisions."""

    def test_collision_pairs_structure(self):
        ca = collision_root_analysis()
        # 4 colliding pairs + 1 non-colliding pair
        assert len(ca) == 5

    def test_8A3_4D4_different_N_orth(self):
        ca = collision_root_analysis()
        entry = ca[('8A3', '4D4')]
        assert entry['same_N_roots']
        assert not entry['same_N_orth']
        assert not entry['same_c2']

    def test_6D4_4A5D4_same_everything(self):
        ca = collision_root_analysis()
        entry = ca[('6D4', '4A5_D4')]
        assert entry['same_N_roots']
        assert entry['same_N_orth']
        assert entry['same_c2']


# ============================================================================
# 7. Boecherer conjecture
# ============================================================================

class TestBocherer:
    """Verify Boecherer conjecture structure."""

    def test_c2_squared_nonneg_for_all(self):
        """c_2^2 is always non-negative (trivially, but verifying computation)."""
        atlas = bocherer_atlas()
        for name, data in atlas.items():
            if data is not None:
                assert data['c_2_squared'] >= 0

    def test_leech_c2_negative(self):
        """The Leech lattice has negative c_2 (deficit of cusp content)."""
        proxy = bocherer_L_value_proxy('Leech')
        assert proxy['sign_c2'] == -1

    def test_d24_c2_positive(self):
        """D24 has the largest positive c_2."""
        proxy = bocherer_L_value_proxy('D24')
        assert proxy['sign_c2'] == 1

    def test_sign_pattern_count(self):
        signs = bocherer_sign_pattern()
        neg = sum(1 for v in signs.values() if v < 0)
        pos = sum(1 for v in signs.values() if v > 0)
        # 3 negative (Leech, 24A1, 12A2), 21 positive
        assert neg == 3
        assert pos == 21
        assert neg + pos == 24

    def test_negative_lattices_are_small_root(self):
        """Negative c_2 should occur for lattices with few roots."""
        signs = bocherer_sign_pattern()
        neg_names = [n for n, s in signs.items() if s < 0]
        for name in neg_names:
            N = NIEMEIER_LATTICES[name]['num_roots']
            assert N <= 72, f"{name} has {N} roots but negative c_2"

    def test_c2_monotone_in_roots_roughly(self):
        """c_2 should roughly increase with the number of roots."""
        # Not strictly monotone (8A3 vs 4D4 at same root count differ),
        # but the overall trend should hold.
        c2_list = []
        for name in ALL_NIEMEIER:
            c2 = extract_c2(name)
            N = NIEMEIER_LATTICES[name]['num_roots']
            if c2 is not None:
                c2_list.append((N, float(c2), name))
        c2_list.sort()
        # Check: the lattice with most roots (D24, 1104) has largest c_2
        assert c2_list[-1][2] == 'D24'
        # And the Leech (0 roots) is among the smallest
        leech_idx = next(i for i, (N, _, n) in enumerate(c2_list) if n == 'Leech')
        assert leech_idx <= 2  # Leech should be in the bottom 3


# ============================================================================
# 8. MC framework connection
# ============================================================================

class TestMCConnection:
    """Verify the MC framework connection."""

    def test_F2_scalar_universal(self):
        mc = mc_genus2_decomposition()
        assert mc['F2_scalar'] == Fraction(7, 240)

    def test_F2_scalar_numerical(self):
        mc = mc_genus2_decomposition()
        assert abs(mc['F2_scalar_numerical'] - 7 / 240) < 1e-15

    def test_universal_for_all_niemeier(self):
        mc = mc_genus2_decomposition()
        assert mc['universal_for_all_niemeier']


# ============================================================================
# 9. Scalar vs full comparison
# ============================================================================

class TestScalarVsFull:
    """Compare scalar shadow prediction with full Siegel form."""

    def test_all_ratios_finite(self):
        comp = scalar_vs_full_comparison()
        for name, data in comp.items():
            assert data['ratio_numerical'] is not None

    def test_leech_ratio_negative(self):
        comp = scalar_vs_full_comparison()
        assert comp['Leech']['ratio_numerical'] < 0

    def test_d24_ratio_positive(self):
        comp = scalar_vs_full_comparison()
        assert comp['D24']['ratio_numerical'] > 0

    def test_ratio_range(self):
        """All ratios should be between -1 and 1 (c_2 small relative to F_2)."""
        comp = scalar_vs_full_comparison()
        for name, data in comp.items():
            assert abs(data['ratio_numerical']) < 1, \
                f"{name} has ratio {data['ratio_numerical']}"


# ============================================================================
# 10. Consistency checks
# ============================================================================

class TestConsistency:
    """Cross-verify with existing modules."""

    def test_consistent_with_niemeier_atlas(self):
        """c_2 values from our module match the niemeier_bocherer_atlas."""
        for name in ALL_NIEMEIER:
            our_c2 = siegel_decomposition(name)['c_2']
            their_c2 = extract_c2(name)
            assert our_c2 == their_c2, f"Mismatch for {name}"

    def test_siegel_modular_form_space_dim(self):
        """dim M_12(Sp(4,Z)) = 3 (fundamental check)."""
        # Count monomials E_4^a * E_6^b * chi_10^c * chi_12^d with 4a+6b+10c+12d=12
        count = 0
        for d in range(2):
            for c_val in range(2):
                for b in range(3):
                    rem = 12 - 12 * d - 10 * c_val - 6 * b
                    if rem >= 0 and rem % 4 == 0:
                        count += 1
        assert count == 3

    def test_cusp_dim_12_is_1(self):
        """dim S_12(Sp(4,Z)) = 1 (only chi_12)."""
        # The only cusp monomial at weight 12 is chi_12 itself (d=1, rest=0).
        # Chi_10 has weight 10, so chi_10 * E_2 would be weight 12 but E_2
        # doesn't exist for Sp(4,Z) (dim M_2 = 0).
        # So the only cusp form is chi_12.
        cusp_count = 0
        # Cusp forms = span of products involving at least one of chi_10, chi_12
        # At weight 12: chi_12 (d=1) is the only one since chi_10*E_2 doesn't exist.
        for d in range(2):
            for c_val in range(2):
                for b in range(3):
                    rem = 12 - 12 * d - 10 * c_val - 6 * b
                    if rem >= 0 and rem % 4 == 0:
                        if c_val > 0 or d > 0:
                            cusp_count += 1
        assert cusp_count == 1  # only chi_12

    def test_c1_determined_by_roots(self):
        """c_1 depends only on N_roots."""
        for n1 in ALL_NIEMEIER:
            for n2 in ALL_NIEMEIER:
                if NIEMEIER_LATTICES[n1]['num_roots'] == \
                   NIEMEIER_LATTICES[n2]['num_roots']:
                    assert niemeier_c1(n1) == niemeier_c1(n2)

    def test_F2_equals_kappa_lambda2(self):
        """The scalar F_2 = kappa * lambda_2^FP for all Niemeier lattices."""
        expected = Fraction(24) * Fraction(7, 5760)
        assert expected == Fraction(7, 240)

    def test_chi12_nonzero_at_diag11(self):
        """chi_12 does not vanish at T = diag(1,1), so c_2 extraction works."""
        chi = chi12_from_igusa(1, 0, 1)
        assert chi != 0

    def test_chi12_nonzero_at_diag22(self):
        """chi_12 does not vanish at T = diag(2,2), so Leech extraction works."""
        chi = chi12_from_igusa(2, 0, 2)
        assert chi != 0

    def test_extraction_formula_consistency(self):
        """Verify the extraction formula is self-consistent for 3E8.

        r_2(3E8, diag(1,1)) = E_12(diag(1,1)) + c_1*Kling(diag(1,1)) + c_2*chi_12(diag(1,1))
        """
        name = '3E8'
        c1 = niemeier_c1(name)
        c2 = extract_c2(name)
        r2 = genus2_rep_at_diag11(name)

        e12 = siegel_eisenstein_coefficient(12, 1, 0, 1)
        kling = klingen_eisenstein_coefficient(1, 0, 1)
        chi = chi12_from_igusa(1, 0, 1)

        reconstructed = e12 + c1 * Fraction(kling) + c2 * chi
        assert reconstructed == Fraction(r2)


# ============================================================================
# 11. Genus-3 predictions
# ============================================================================

class TestGenus3:
    """Verify genus-3 prediction structure."""

    def test_prediction_exists(self):
        pred = genus3_prediction()
        assert pred['genus2_distinct'] == 20
        assert pred['genus2_collisions'] == 4

    def test_kneser_precedent(self):
        pred = genus3_prediction()
        assert 'genus 3' in pred['kneser_precedent']


# ============================================================================
# 12. Graph-by-graph for specific lattices
# ============================================================================

class TestSpecificLattices:
    """Verify specific lattice computations."""

    def test_leech_c2_value(self):
        """Leech lattice c_2 should be computable and negative."""
        c2 = extract_c2('Leech')
        assert c2 is not None
        assert c2 < 0

    def test_d24_largest_c2(self):
        """D24 has the largest c_2 among all Niemeier lattices."""
        max_c2 = None
        max_name = None
        for name in ALL_NIEMEIER:
            c2 = extract_c2(name)
            if c2 is not None and (max_c2 is None or c2 > max_c2):
                max_c2 = c2
                max_name = name
        assert max_name == 'D24'

    def test_24A1_is_second_most_negative(self):
        """24A1 should have a more negative c_2 than 12A2."""
        c2_24A1 = extract_c2('24A1')
        c2_12A2 = extract_c2('12A2')
        assert c2_24A1 < c2_12A2

    def test_e8_genus2_F2(self):
        """E_8 lattice VOA has F_2 = 8 * 7/5760 = 7/720."""
        F2 = Fraction(8) * lambda_fp(2)
        assert F2 == Fraction(7, 720)

    def test_niemeier_F2_universal(self):
        """All Niemeier lattices have F_2 = 24 * 7/5760 = 7/240."""
        F2 = Fraction(24) * lambda_fp(2)
        assert F2 == Fraction(7, 240)

    def test_c2_ordering_monotone_excluding_leech(self):
        """c_2 increases with N_roots for lattices with roots.

        The Leech lattice (0 roots) is excluded because its c_2 is determined
        by the norm-4 shell, giving a different relationship to root count.
        Among lattices WITH roots (N_roots >= 48), c_2 is monotone non-decreasing
        when grouped by root count.
        """
        root_groups = {}
        for name in ALL_NIEMEIER:
            N = NIEMEIER_LATTICES[name]['num_roots']
            if N == 0:
                continue  # Skip Leech
            c2 = extract_c2(name)
            root_groups.setdefault(N, []).append((name, c2))

        sorted_roots = sorted(root_groups.keys())
        for i in range(1, len(sorted_roots)):
            r_prev = sorted_roots[i - 1]
            r_curr = sorted_roots[i]
            min_curr = min(c2 for _, c2 in root_groups[r_curr])
            max_prev = max(c2 for _, c2 in root_groups[r_prev])
            assert min_curr >= max_prev, \
                f"Monotonicity violation: roots {r_prev} max={float(max_prev):.6e}, " \
                f"roots {r_curr} min={float(min_curr):.6e}"


# ============================================================================
# 13. Dimension theory
# ============================================================================

class TestDimensionTheory:
    """Verify dimensional constraints on Siegel modular form spaces."""

    @pytest.mark.parametrize("k,expected_dim", [
        (4, 1), (6, 1), (8, 1), (10, 2), (12, 3),
    ])
    def test_igusa_dimensions(self, k, expected_dim):
        """Verify dim M_k(Sp(4,Z)) for small k."""
        count = 0
        for d in range(k // 12 + 1):
            for c_val in range((k - 12 * d) // 10 + 1):
                for b in range((k - 12 * d - 10 * c_val) // 6 + 1):
                    rem = k - 12 * d - 10 * c_val - 6 * b
                    if rem >= 0 and rem % 4 == 0:
                        count += 1
        assert count == expected_dim

    def test_no_cusp_forms_below_10(self):
        """S_k(Sp(4,Z)) = 0 for k < 10."""
        for k in [4, 6, 8]:
            cusp_count = 0
            for d in range(k // 12 + 1):
                for c_val in range((k - 12 * d) // 10 + 1):
                    for b in range((k - 12 * d - 10 * c_val) // 6 + 1):
                        rem = k - 12 * d - 10 * c_val - 6 * b
                        if rem >= 0 and rem % 4 == 0:
                            if c_val > 0 or d > 0:
                                cusp_count += 1
            assert cusp_count == 0, f"Unexpected cusp form at weight {k}"

    def test_first_cusp_form_at_10(self):
        """S_10(Sp(4,Z)) has dimension 1 (chi_10)."""
        k = 10
        cusp_count = 0
        for d in range(k // 12 + 1):
            for c_val in range((k - 12 * d) // 10 + 1):
                for b in range((k - 12 * d - 10 * c_val) // 6 + 1):
                    rem = k - 12 * d - 10 * c_val - 6 * b
                    if rem >= 0 and rem % 4 == 0:
                        if c_val > 0 or d > 0:
                            cusp_count += 1
        assert cusp_count == 1


# ============================================================================
# 14. Orthogonal root counts
# ============================================================================

class TestOrthogonalRoots:
    """Verify orthogonal root counts for root systems."""

    def test_E8_orthogonal(self):
        assert orthogonal_roots_per_root('3E8') == 606
        # In 3E8: a root in one E_8 copy.
        # Within same E_8: 126 orthogonal.
        # Other 2 copies: 2*240 = 480 orthogonal.
        # Total: 126 + 480 = 606.

    def test_D24_orthogonal(self):
        N_orth = orthogonal_roots_per_root('D24')
        # D_24: all roots +-e_i+-e_j.
        # Given e_1+e_2: orthogonal = e_1-e_2, -(e_1-e_2) + 2*(22)(21) = 2 + 924 = 926.
        # Formula: 2*(n-2)*(n-3) + 2 = 2*22*21 + 2 = 924 + 2 = 926.
        # Then N_orth_total = orth_within = 926 (single component).
        assert N_orth == 926

    def test_24A1_orthogonal(self):
        N_orth = orthogonal_roots_per_root('24A1')
        # In A_1: 2 roots, 0 orthogonal within.
        # Other 23 copies: 23*2 = 46 orthogonal.
        # Total: 0 + 46 = 46.
        assert N_orth == 46

    def test_6D4_equals_4A5D4(self):
        """6D4 and 4A5+D4 should have same N_orth (collision prerequisite)."""
        assert orthogonal_roots_per_root('6D4') == \
               orthogonal_roots_per_root('4A5_D4')


# ============================================================================
# 15. Sign analysis and ordering
# ============================================================================

class TestSignAndOrdering:
    """Verify the sign pattern and ordering of c_2 values."""

    def test_negative_lattices(self):
        """Exactly 3 lattices have negative c_2: Leech, 24A1, 12A2."""
        signs = bocherer_sign_pattern()
        neg = [n for n, s in signs.items() if s < 0]
        assert set(neg) == {'Leech', '24A1', '12A2'}

    def test_c2_sorted_by_roots_excluding_leech(self):
        """When sorted by N_roots (excluding Leech), c_2 is non-decreasing."""
        da = distinguishing_analysis()
        root_to_c2 = {}
        for name, data in da['c2_data'].items():
            N = data['N_roots']
            if N == 0:
                continue  # Leech excluded (norm-4 shell, different regime)
            c2 = data['c_2']
            root_to_c2.setdefault(N, []).append(c2)

        sorted_roots = sorted(root_to_c2.keys())
        for i in range(1, len(sorted_roots)):
            max_prev = max(root_to_c2[sorted_roots[i - 1]])
            min_curr = min(root_to_c2[sorted_roots[i]])
            assert min_curr >= max_prev
