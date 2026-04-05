r"""Tests for the Niemeier genus-2 theta decomposition and Bocherer coefficients.

Comprehensive tests covering:
1. Genus-1 equivalence class structure
2. Root-pair genus-2 representation numbers
3. Inner product distribution analysis
4. Bocherer coefficient extraction
5. Genus-2 vs genus-3 distinction
6. MC framework connection
7. Cross-checks with existing engines
8. Classical results verification
"""

import math
import unittest
from fractions import Fraction

from compute.lib.niemeier_genus2_full import (
    genus1_equivalence_classes,
    genus1_indistinguishable_pairs,
    root_pair_r2_table,
    root_pair_genus2_distinction,
    extract_c2_from_rootpairs,
    aggregated_ip_distribution,
    ip_distribution_all_components,
    genus1_equivalent_pairs_analysis,
    why_root_pairs_coincide,
    full_genus2_table,
    siegel_modular_form_dims,
    minimum_genus_for_complete_distinction,
    bocherer_atlas_rootpair,
    mc_shadow_vs_bocherer,
    norm4_vector_counts,
    summary,
)
from compute.lib.niemeier_bocherer_atlas import (
    ALL_NIEMEIER,
    NIEMEIER_LATTICES,
    NIEMEIER_AUT_ORDERS,
    niemeier_c_delta,
    niemeier_c1,
    kissing_number,
    genus2_rep_at_diag11,
    orthogonal_roots_per_root,
    _inner_product_distribution_simple,
    _root_count_for_type,
)


# ====================================================================
# Section 1: Genus-1 equivalence classes
# ====================================================================

class TestGenus1Equivalence(unittest.TestCase):
    """Genus-1 equivalence class structure."""

    def test_24_lattices(self):
        """All 24 Niemeier lattices are present."""
        classes = genus1_equivalence_classes()
        total = sum(len(v) for v in classes.values())
        self.assertEqual(total, 24)

    def test_five_pairs(self):
        """Exactly 5 genus-1 indistinguishable pairs."""
        pairs = genus1_indistinguishable_pairs()
        self.assertEqual(len(pairs), 5)

    def test_pair_root_counts(self):
        """Each pair has the same root count."""
        pairs = genus1_indistinguishable_pairs()
        for n1, n2 in pairs:
            self.assertEqual(
                NIEMEIER_LATTICES[n1]['num_roots'],
                NIEMEIER_LATTICES[n2]['num_roots'],
                f"{n1} vs {n2}"
            )

    def test_specific_pairs(self):
        """The five specific pairs are correct."""
        pairs = genus1_indistinguishable_pairs()
        pair_roots = {(n1, n2): NIEMEIER_LATTICES[n1]['num_roots']
                      for n1, n2 in pairs}
        root_values = set(pair_roots.values())
        self.assertEqual(root_values, {96, 144, 288, 432, 720})

    def test_19_genus1_classes(self):
        """There are 19 genus-1 equivalence classes (24 - 5 pairs)."""
        classes = genus1_equivalence_classes()
        # Number of classes = number of distinct root counts
        self.assertEqual(len(classes), 19)

    def test_leech_unique(self):
        """The Leech lattice (0 roots) is unique at genus 1."""
        classes = genus1_equivalence_classes()
        self.assertEqual(len(classes[0]), 1)
        self.assertEqual(classes[0], ['Leech'])

    def test_d24_unique(self):
        """D_24 (1104 roots) is unique at genus 1."""
        classes = genus1_equivalence_classes()
        self.assertEqual(len(classes[1104]), 1)


# ====================================================================
# Section 2: Root-pair genus-2 representation numbers
# ====================================================================

class TestRootPairR2(unittest.TestCase):
    """Root-pair genus-2 representation number tests."""

    def test_leech_all_zero(self):
        """Leech lattice has no roots, so all root-pair r_2 = 0."""
        table = root_pair_r2_table('Leech')
        for b in range(-2, 3):
            self.assertEqual(table.get(b, 0), 0)

    def test_24A1_diag11(self):
        """24A_1: each root is orthogonal to 46 others (24*2 - 2 = 46)."""
        r2 = genus2_rep_at_diag11('24A1')
        # 48 roots, each orthogonal to 46 others
        self.assertEqual(r2, 48 * 46)

    def test_3E8_diag11(self):
        """3E_8: 720 roots, each orthogonal to 606."""
        r2 = genus2_rep_at_diag11('3E8')
        # In one E8: 126 orthogonal. In other 2 copies: 2*240 = 480.
        # Total orth = 126 + 480 = 606.
        self.assertEqual(r2, 720 * 606)

    def test_D16_E8_diag11(self):
        """D_16+E_8: same r_2 at diag(1,1) as 3E_8."""
        r2_d16e8 = genus2_rep_at_diag11('D16_E8')
        r2_3e8 = genus2_rep_at_diag11('3E8')
        self.assertEqual(r2_d16e8, r2_3e8)

    def test_8A3_vs_4D4_different(self):
        """8A_3 and 4D_4 have different r_2 at diag(1,1)."""
        r2_8a3 = genus2_rep_at_diag11('8A3')
        r2_4d4 = genus2_rep_at_diag11('4D4')
        self.assertNotEqual(r2_8a3, r2_4d4)
        self.assertEqual(r2_8a3, 96 * 86)
        self.assertEqual(r2_4d4, 96 * 78)

    def test_root_pair_symmetry(self):
        """r_2(Lambda, ((1,b/2),(b/2,1))) = r_2(Lambda, ((1,-b/2),(-b/2,1)))."""
        for name in ['24A1', '3E8', 'D24']:
            table = root_pair_r2_table(name)
            for b in [1, 2]:
                self.assertEqual(table.get(b, 0), table.get(-b, 0),
                                 f"{name} at b={b}")

    def test_b2_equals_nroots(self):
        """At b=2, r_2 = N_roots (each root pairs with itself)."""
        for name in ALL_NIEMEIER:
            if name == 'Leech':
                continue
            table = root_pair_r2_table(name)
            self.assertEqual(table.get(2, 0),
                             NIEMEIER_LATTICES[name]['num_roots'],
                             f"{name} at b=2")

    def test_bm2_equals_nroots(self):
        """At b=-2, r_2 = N_roots (each root pairs with its negative)."""
        for name in ALL_NIEMEIER:
            if name == 'Leech':
                continue
            table = root_pair_r2_table(name)
            self.assertEqual(table.get(-2, 0),
                             NIEMEIER_LATTICES[name]['num_roots'],
                             f"{name} at b=-2")


# ====================================================================
# Section 3: Inner product distribution analysis
# ====================================================================

class TestIPDistributions(unittest.TestCase):
    """Aggregated inner product distribution tests."""

    def test_distribution_sums_to_total(self):
        """Aggregated distribution sums to N_roots."""
        for name in ALL_NIEMEIER:
            if name == 'Leech':
                continue
            dist = aggregated_ip_distribution(name)
            total = sum(dist.values())
            self.assertEqual(total, NIEMEIER_LATTICES[name]['num_roots'],
                             f"{name}: sum={total}")

    def test_ip2_is_1(self):
        """ip=2 count is always 1 (the root itself)."""
        for name in ALL_NIEMEIER:
            if name == 'Leech':
                continue
            dist = aggregated_ip_distribution(name)
            self.assertEqual(dist.get(2, 0), 1, f"{name}")

    def test_ipm2_is_1(self):
        """ip=-2 count is always 1 (the negative root)."""
        for name in ALL_NIEMEIER:
            if name == 'Leech':
                continue
            dist = aggregated_ip_distribution(name)
            self.assertEqual(dist.get(-2, 0), 1, f"{name}")

    def test_ip_symmetry(self):
        """ip distribution is symmetric: count(b) = count(-b)."""
        for name in ALL_NIEMEIER:
            if name == 'Leech':
                continue
            dist = aggregated_ip_distribution(name)
            for b in [1, 2]:
                self.assertEqual(dist.get(b, 0), dist.get(-b, 0),
                                 f"{name} at b={b}")

    def test_d16e8_vs_3e8_same_distribution(self):
        """D_16+E_8 and 3E_8 have the same aggregated distribution."""
        d1 = aggregated_ip_distribution('D16_E8')
        d2 = aggregated_ip_distribution('3E8')
        self.assertEqual(d1, d2)

    def test_8a3_vs_4d4_different_distribution(self):
        """8A_3 and 4D_4 have different distributions (ip=1 differs)."""
        d1 = aggregated_ip_distribution('8A3')
        d2 = aggregated_ip_distribution('4D4')
        self.assertNotEqual(d1, d2)
        self.assertEqual(d1[1], 4)   # A3: ip=1 count within = 2*(3-1) = 4
        self.assertEqual(d2[1], 8)   # D4: ip=1 count within = 4*(4-2) = 8


# ====================================================================
# Section 4: Genus-1 pair analysis
# ====================================================================

class TestGenus1PairsAnalysis(unittest.TestCase):
    """Analysis of the 5 genus-1 indistinguishable pairs."""

    def test_8a3_4d4_distinguished_by_root_pairs(self):
        """8A_3 vs 4D_4 is distinguished by root-pair data."""
        result = root_pair_genus2_distinction('8A3', '4D4')
        self.assertTrue(result['distinguished_by_root_pairs'])

    def test_d16e8_3e8_not_distinguished_by_root_pairs(self):
        """D_16+E_8 vs 3E_8 is NOT distinguished by root-pair data."""
        result = root_pair_genus2_distinction('D16_E8', '3E8')
        self.assertFalse(result['distinguished_by_root_pairs'])

    def test_6d4_4a5d4_not_distinguished_by_root_pairs(self):
        """6D_4 vs 4A_5+D_4 is NOT distinguished by root-pair data."""
        result = root_pair_genus2_distinction('6D4', '4A5_D4')
        self.assertFalse(result['distinguished_by_root_pairs'])

    def test_a11d7e6_4e6_not_distinguished_by_root_pairs(self):
        """A_11+D_7+E_6 vs 4E_6 is NOT distinguished by root-pair data."""
        result = root_pair_genus2_distinction('A11_D7_E6', '4E6')
        self.assertFalse(result['distinguished_by_root_pairs'])

    def test_a17e7_d10_2e7_not_distinguished_by_root_pairs(self):
        """A_17+E_7 vs D_10+2E_7 is NOT distinguished by root-pair data."""
        result = root_pair_genus2_distinction('A17_E7', 'D10_2E7')
        self.assertFalse(result['distinguished_by_root_pairs'])

    def test_exactly_one_pair_distinguished_by_root_pairs(self):
        """Exactly 1 of 5 pairs is root-pair distinguished."""
        results = genus1_equivalent_pairs_analysis()
        n_dist = sum(1 for r in results if r['root_pair_distinguished'])
        self.assertEqual(n_dist, 1)

    def test_four_pairs_have_matching_signatures(self):
        """4 of 5 pairs have matching ip signatures."""
        results = genus1_equivalent_pairs_analysis()
        n_same = sum(1 for r in results if r['same_aggregated_distribution'])
        self.assertEqual(n_same, 4)


# ====================================================================
# Section 5: Why root pairs coincide
# ====================================================================

class TestWhyRootPairsCoincide(unittest.TestCase):
    """Verify the signature-matching explanation."""

    def test_d16e8_3e8_same_signatures(self):
        """D_16+E_8 and 3E_8 have matching ip signatures."""
        result = why_root_pairs_coincide('D16_E8', '3E8')
        self.assertTrue(result['signatures_match'])
        # Both should have signature (56, 56, 606)
        self.assertIn((56, 56, 606), result['ip_signatures_1'])
        self.assertIn((56, 56, 606), result['ip_signatures_2'])

    def test_6d4_4a5d4_same_signatures(self):
        result = why_root_pairs_coincide('6D4', '4A5_D4')
        self.assertTrue(result['signatures_match'])

    def test_a11d7e6_4e6_same_signatures(self):
        result = why_root_pairs_coincide('A11_D7_E6', '4E6')
        self.assertTrue(result['signatures_match'])

    def test_a17e7_d10_2e7_same_signatures(self):
        result = why_root_pairs_coincide('A17_E7', 'D10_2E7')
        self.assertTrue(result['signatures_match'])

    def test_8a3_4d4_different_signatures(self):
        result = why_root_pairs_coincide('8A3', '4D4')
        self.assertFalse(result['signatures_match'])


# ====================================================================
# Section 6: Bocherer coefficient extraction
# ====================================================================

class TestBochererCoefficients(unittest.TestCase):
    """Bocherer coefficient c_2 extraction tests."""

    def test_c2_leech_nonzero(self):
        """Leech lattice c_2 is nonzero (cusp form content)."""
        c2 = extract_c2_from_rootpairs('Leech')
        self.assertIsNotNone(c2)
        self.assertNotEqual(c2, 0)

    def test_c2_all_computable(self):
        """c_2 is computable for all 24 lattices."""
        for name in ALL_NIEMEIER:
            c2 = extract_c2_from_rootpairs(name)
            self.assertIsNotNone(c2, f"c_2 not computable for {name}")

    def test_c2_leech_negative(self):
        """Leech c_2 is negative (fewer norm-2 pairs than Eisenstein predicts)."""
        c2 = extract_c2_from_rootpairs('Leech')
        self.assertLess(float(c2), 0)

    def test_c2_d24_largest(self):
        """D_24 (most roots) has the largest c_2."""
        c2s = {name: float(extract_c2_from_rootpairs(name))
               for name in ALL_NIEMEIER}
        max_name = max(c2s, key=c2s.get)
        self.assertEqual(max_name, 'D24')

    def test_c2_monotonic_with_roots_for_rooted_singletons(self):
        """For rooted lattices NOT in genus-1 pairs, c_2 increases with |R|.

        The Leech lattice is excluded because its c_2 comes from a different
        shell (norm-4 vs norm-2) and uses a different extraction point.
        """
        pairs = genus1_indistinguishable_pairs()
        in_pair = set()
        for a, b in pairs:
            in_pair.add(a)
            in_pair.add(b)

        singletons = [(name, NIEMEIER_LATTICES[name]['num_roots'])
                       for name in ALL_NIEMEIER
                       if name not in in_pair and name != 'Leech']
        singletons.sort(key=lambda x: x[1])

        c2_values = [float(extract_c2_from_rootpairs(name))
                     for name, _ in singletons]
        for i in range(len(c2_values) - 1):
            self.assertLess(c2_values[i], c2_values[i + 1],
                            f"{singletons[i][0]} vs {singletons[i+1][0]}")

    def test_c2_genus1_pairs_equal_from_rootpairs(self):
        """For the 4 non-root-pair-distinguishable pairs, c_2 from root
        pairs gives the same value (because root-pair data is identical)."""
        non_dist_pairs = [
            ('6D4', '4A5_D4'),
            ('A11_D7_E6', '4E6'),
            ('A17_E7', 'D10_2E7'),
            ('D16_E8', '3E8'),
        ]
        for n1, n2 in non_dist_pairs:
            c2_1 = extract_c2_from_rootpairs(n1)
            c2_2 = extract_c2_from_rootpairs(n2)
            self.assertEqual(c2_1, c2_2, f"{n1} vs {n2}")

    def test_c2_8a3_4d4_differ(self):
        """8A_3 and 4D_4 have different c_2 values."""
        c2_8a3 = extract_c2_from_rootpairs('8A3')
        c2_4d4 = extract_c2_from_rootpairs('4D4')
        self.assertNotEqual(c2_8a3, c2_4d4)


# ====================================================================
# Section 7: Siegel modular form dimensions
# ====================================================================

class TestSiegelDimensions(unittest.TestCase):
    """Siegel modular form dimension tests."""

    def test_genus1_dim(self):
        dims = siegel_modular_form_dims()
        self.assertEqual(dims['genus_1']['dim_M'], 2)
        self.assertEqual(dims['genus_1']['dim_S'], 1)

    def test_genus2_dim(self):
        dims = siegel_modular_form_dims()
        self.assertEqual(dims['genus_2']['dim_M'], 3)
        self.assertEqual(dims['genus_2']['dim_S'], 1)

    def test_genus3_dim(self):
        dims = siegel_modular_form_dims()
        self.assertEqual(dims['genus_3']['dim_M'], 5)
        self.assertEqual(dims['genus_3']['dim_S'], 2)

    def test_cumulative_invariants(self):
        dims = siegel_modular_form_dims()
        self.assertEqual(dims['cumulative_invariants'][1], 1)
        self.assertEqual(dims['cumulative_invariants'][2], 2)
        self.assertEqual(dims['cumulative_invariants'][3], 4)


# ====================================================================
# Section 8: Minimum genus for distinction
# ====================================================================

class TestMinimumGenus(unittest.TestCase):
    """Minimum genus for complete distinction."""

    def test_minimum_is_2(self):
        mg = minimum_genus_for_complete_distinction()
        self.assertEqual(mg['result'], 2)

    def test_rank16_needs_genus3(self):
        """E_8 x E_8 vs D_16^+ requires genus 3."""
        mg = minimum_genus_for_complete_distinction()
        self.assertFalse(mg['rank_16_comparison']['genus_2_distinguished'])
        self.assertTrue(mg['rank_16_comparison']['genus_3_distinguished'])


# ====================================================================
# Section 9: MC framework connection
# ====================================================================

class TestMCConnection(unittest.TestCase):
    """MC shadow tower vs Bocherer coefficient."""

    def test_shadow_universal(self):
        mc = mc_shadow_vs_bocherer()
        self.assertEqual(mc['kappa_all_niemeier'], 24)
        self.assertEqual(mc['F2_shadow_universal'], Fraction(7, 240))

    def test_c2_beyond_shadow(self):
        mc = mc_shadow_vs_bocherer()
        self.assertIn('beyond', mc['bocherer_captures'].lower())


# ====================================================================
# Section 10: Full table consistency
# ====================================================================

class TestFullTable(unittest.TestCase):
    """Full genus-2 table consistency checks."""

    def test_all_24_present(self):
        table = full_genus2_table()
        self.assertEqual(len(table), 24)

    def test_c1_equals_c_delta(self):
        """c_1 = c_Delta for all lattices."""
        table = full_genus2_table()
        for name, entry in table.items():
            c1_expected = niemeier_c1(name)
            c_delta = niemeier_c_delta(name)
            self.assertEqual(c1_expected, c_delta, f"{name}")
            # Float values should also match
            self.assertAlmostEqual(entry['c_delta_float'],
                                   float(c1_expected), places=4,
                                   msg=f"{name}")

    def test_leech_r2_zero(self):
        table = full_genus2_table()
        self.assertEqual(table['Leech']['r2_diag11'], 0)

    def test_reliable_flags(self):
        """Reliability flags are correct."""
        table = full_genus2_table()
        # Leech: reliable (has dedicated computation)
        self.assertTrue(table['Leech']['c2_reliable'])
        # 24A1: not in a pair, so reliable
        self.assertTrue(table['24A1']['c2_reliable'])
        # D16_E8: in a pair, not reliable from root data alone
        self.assertFalse(table['D16_E8']['c2_reliable'])
        # 3E8: in a pair, not reliable
        self.assertFalse(table['3E8']['c2_reliable'])


# ====================================================================
# Section 11: Bocherer atlas
# ====================================================================

class TestBochererAtlas(unittest.TestCase):
    """Bocherer atlas output tests."""

    def test_atlas_completeness(self):
        atlas = bocherer_atlas_rootpair()
        self.assertEqual(len(atlas), 24)

    def test_atlas_has_c2(self):
        atlas = bocherer_atlas_rootpair()
        for name, entry in atlas.items():
            self.assertIn('c2', entry)
            self.assertIsNotNone(entry['c2'], f"{name} has None c2")


# ====================================================================
# Section 12: Summary
# ====================================================================

class TestSummary(unittest.TestCase):
    """Summary tests."""

    def test_summary_counts(self):
        s = summary()
        self.assertEqual(s['total_lattices'], 24)
        self.assertEqual(s['genus1_pairs'], 5)
        self.assertEqual(s['pairs_root_pair_distinguished'], 1)
        self.assertEqual(s['pairs_needing_full_lattice'], 4)
        self.assertEqual(s['minimum_genus_for_distinction'], 2)


# ====================================================================
# Section 13: Cross-checks with existing engines
# ====================================================================

class TestCrossChecks(unittest.TestCase):
    """Cross-checks with existing niemeier_bocherer_atlas and genus2_bocherer_bridge."""

    def test_c_delta_consistency(self):
        """c_Delta values match the existing atlas."""
        for name in ALL_NIEMEIER:
            c_del_new = float(niemeier_c_delta(name))
            nr = NIEMEIER_LATTICES[name]['num_roots']
            c_del_expected = nr - 65520.0 / 691.0
            self.assertAlmostEqual(c_del_new, c_del_expected, places=6,
                                   msg=f"{name}")

    def test_orthogonal_roots_cross_check(self):
        """Orthogonal root counts are consistent between engines."""
        # E8 as a standalone: 126 orthogonal roots per root
        from compute.lib.genus2_bocherer_bridge import e8_inner_product_distribution
        dist = e8_inner_product_distribution()
        self.assertEqual(dist[0], 126)

    def test_leech_minimal_shell(self):
        """Leech lattice minimal shell has 196560 vectors."""
        from compute.lib.genus2_bocherer_bridge import LEECH_KISSING
        self.assertEqual(LEECH_KISSING, 196560)
        self.assertEqual(kissing_number('Leech'), 196560)

    def test_e8_root_count(self):
        from compute.lib.genus2_bocherer_bridge import e8_roots
        roots = e8_roots()
        self.assertEqual(len(roots), 240)


# ====================================================================
# Section 14: Specific computations
# ====================================================================

class TestSpecificComputations(unittest.TestCase):
    """Verify specific computed values."""

    def test_a3_orth(self):
        """A_3: (3-1)*(3-2) = 2 orthogonal roots within."""
        dist = _inner_product_distribution_simple('A', 3)
        self.assertEqual(dist[0], 2)

    def test_d4_orth(self):
        """D_4: 2*(4-2)*(4-3) + 2 = 6 orthogonal roots within."""
        dist = _inner_product_distribution_simple('D', 4)
        self.assertEqual(dist[0], 6)

    def test_e8_orth(self):
        """E_8: 126 orthogonal roots within."""
        dist = _inner_product_distribution_simple('E', 8)
        self.assertEqual(dist[0], 126)

    def test_d16_orth(self):
        """D_16: 2*(16-2)*(16-3) + 2 = 366 orthogonal within."""
        dist = _inner_product_distribution_simple('D', 16)
        self.assertEqual(dist[0], 2 * 14 * 13 + 2)

    def test_r2_b2_is_nroots(self):
        """At b=2, r_2(Lambda, ((1,1),(1,1))) counts root-selfpairs."""
        for name in ['24A1', '12A2', '3E8', 'D24']:
            table = root_pair_r2_table(name)
            nr = NIEMEIER_LATTICES[name]['num_roots']
            self.assertEqual(table[2], nr, f"{name}")

    def test_aggregated_d16e8(self):
        """D_16+E_8 aggregated distribution: ip1=56, ip0=606."""
        dist = aggregated_ip_distribution('D16_E8')
        self.assertEqual(dist[1], 56)
        self.assertEqual(dist[0], 606)

    def test_aggregated_3e8(self):
        """3E_8 aggregated distribution: ip1=56, ip0=606."""
        dist = aggregated_ip_distribution('3E8')
        self.assertEqual(dist[1], 56)
        self.assertEqual(dist[0], 606)


# ====================================================================
# Section 15: Deeper algebraic tests for ip distributions
# ====================================================================

class TestIPDistributionAlgebra(unittest.TestCase):
    """Algebraic consistency of inner product distributions."""

    def test_ip_distribution_sum(self):
        """Distribution sums to total roots for all simple types."""
        test_cases = [
            ('A', 1, 2), ('A', 2, 6), ('A', 3, 12), ('A', 5, 30),
            ('D', 4, 24), ('D', 7, 84), ('D', 10, 180),
            ('E', 6, 72), ('E', 7, 126), ('E', 8, 240),
        ]
        for fam, n, expected_total in test_cases:
            dist = _inner_product_distribution_simple(fam, n)
            total = sum(dist.values())
            self.assertEqual(total, expected_total,
                             f"{fam}_{n}: sum={total}, expected {expected_total}")

    def test_ip1_formula_A(self):
        """For A_n, ip=1 count = 2*(n-1)."""
        for n in range(2, 10):
            dist = _inner_product_distribution_simple('A', n)
            self.assertEqual(dist[1], 2 * (n - 1),
                             f"A_{n}")

    def test_ip1_formula_D(self):
        """For D_n, ip=1 count = 4*(n-2)."""
        for n in range(4, 10):
            dist = _inner_product_distribution_simple('D', n)
            self.assertEqual(dist[1], 4 * (n - 2),
                             f"D_{n}")

    def test_ip0_formula_A(self):
        """For A_n, ip=0 count = (n-1)*(n-2)."""
        for n in range(2, 10):
            dist = _inner_product_distribution_simple('A', n)
            self.assertEqual(dist[0], (n - 1) * (n - 2),
                             f"A_{n}")

    def test_ip0_formula_D(self):
        """For D_n, ip=0 count = 2*(n-2)*(n-3) + 2."""
        for n in range(4, 10):
            dist = _inner_product_distribution_simple('D', n)
            self.assertEqual(dist[0], 2 * (n - 2) * (n - 3) + 2,
                             f"D_{n}")


# ====================================================================
# Section 16: D16+E8 vs 3E8 specific investigation
# ====================================================================

class TestD16E8vs3E8(unittest.TestCase):
    """Detailed investigation of the D_16+E_8 vs 3E_8 pair.

    This is the most interesting pair: both have 720 roots, both have
    the same root-pair representation numbers at ALL T = ((1,b/2),(b/2,1)),
    and they are the rank-24 analogue of the E_8xE_8 vs D_16^+ pair at rank 16.
    """

    def test_same_root_count(self):
        self.assertEqual(
            NIEMEIER_LATTICES['D16_E8']['num_roots'],
            NIEMEIER_LATTICES['3E8']['num_roots']
        )
        self.assertEqual(NIEMEIER_LATTICES['D16_E8']['num_roots'], 720)

    def test_same_r2_all_b(self):
        """Same root-pair r_2 at all b values."""
        t1 = root_pair_r2_table('D16_E8')
        t2 = root_pair_r2_table('3E8')
        self.assertEqual(t1, t2)

    def test_same_aggregated_distribution(self):
        d1 = aggregated_ip_distribution('D16_E8')
        d2 = aggregated_ip_distribution('3E8')
        self.assertEqual(d1, d2)

    def test_same_c2_from_root_pairs(self):
        """Root-pair c_2 extraction gives same value (inherent limitation)."""
        c2_1 = extract_c2_from_rootpairs('D16_E8')
        c2_2 = extract_c2_from_rootpairs('3E8')
        self.assertEqual(c2_1, c2_2)

    def test_different_components(self):
        """But the lattice structures are genuinely different."""
        comp1 = NIEMEIER_LATTICES['D16_E8']['components']
        comp2 = NIEMEIER_LATTICES['3E8']['components']
        self.assertNotEqual(comp1, comp2)

    def test_genus2_distinguishes_in_theory(self):
        """Classical result: genus-2 theta distinguishes them."""
        mg = minimum_genus_for_complete_distinction()
        self.assertTrue(mg['genus_2_distinguishes_all'])

    def test_ip_from_different_components(self):
        """The two lattices have different COMPONENT ip distributions,
        but the same AGGREGATED distributions."""
        dists1 = ip_distribution_all_components('D16_E8')
        dists2 = ip_distribution_all_components('3E8')
        # D16+E8 has TWO distinct component types
        self.assertEqual(len(dists1), 2)
        # 3E8 has ONE component type
        self.assertEqual(len(dists2), 1)
        # But both aggregate to the same signature
        sigs1 = {(d['distribution'][1], d['distribution'][0])
                 for d in dists1}
        sigs2 = {(d['distribution'][1], d['distribution'][0])
                 for d in dists2}
        # D16: ip1=56, ip0=366+240=606
        # E8 in D16+E8: ip1=56, ip0=126+480=606
        # E8 in 3E8: ip1=56, ip0=126+480=606
        # All give (56, 606)
        self.assertEqual(sigs1, {(56, 606)})
        self.assertEqual(sigs2, {(56, 606)})


# ====================================================================
# Section 17: Numerical consistency
# ====================================================================

class TestNumericalConsistency(unittest.TestCase):
    """Numerical consistency checks."""

    def test_c2_ordering_rooted(self):
        """c_2 values increase with |R| for rooted singletons.

        Excludes Leech (no roots, different extraction shell).
        """
        pairs = genus1_indistinguishable_pairs()
        in_pair = set()
        for a, b in pairs:
            in_pair.add(a)
            in_pair.add(b)

        singletons = sorted(
            [(name, NIEMEIER_LATTICES[name]['num_roots'])
             for name in ALL_NIEMEIER
             if name not in in_pair and name != 'Leech'],
            key=lambda x: x[1]
        )

        c2_prev = float('-inf')
        for name, nr in singletons:
            c2 = float(extract_c2_from_rootpairs(name))
            self.assertGreater(c2, c2_prev, f"c_2({name}) not > previous")
            c2_prev = c2

    def test_c_delta_range(self):
        """c_Delta ranges from -94.8... (Leech) to 1009.18... (D_24)."""
        c_deltas = {name: float(niemeier_c_delta(name))
                    for name in ALL_NIEMEIER}
        self.assertAlmostEqual(min(c_deltas.values()), -65520 / 691, places=2)
        self.assertAlmostEqual(max(c_deltas.values()),
                               1104 - 65520 / 691, places=2)


if __name__ == '__main__':
    unittest.main()
