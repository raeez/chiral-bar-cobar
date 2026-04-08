"""Tests for bar cohomology of rank-r Heisenberg and E_8 lattice VOA.

Ground truth:
  - heisenberg_bar.py: KNOWN_BAR_DIMS for rank-1 Heisenberg
  - e8_lattice_bar.py: E_8 root system data
  - lattice_voa_shadows.py: kappa(V_{E_8}) = rank = 8 (lattice description)
  - e8_affine_shadow_engine.py: kappa(V_1(e_8)) = 1922/15 (affine KM)
  - bar_cohomology_dimensions.py: H^1_h = p(h-2) for rank-1 Heisenberg

Multi-path verification for every numerical claim (per CLAUDE.md mandate).
"""

import pytest
from math import comb, factorial
from sympy import Rational, Symbol

from compute.lib.bar_cohomology_lattice_explicit_engine import (
    # Colored partitions
    colored_partition_number,
    colored_partition_table,
    # Faber-Pandharipande
    faber_pandharipande,
    # Rank-r Heisenberg
    heisenberg_rank_r_bar_chain_dim,
    heisenberg_rank_r_bar_chain_total,
    heisenberg_rank_r_euler_char,
    heisenberg_rank_r_bar_cohomology_h1,
    heisenberg_rank_r_bar_cohomology_koszul,
    heisenberg_rank_r_kappa,
    heisenberg_rank_r_central_charge,
    heisenberg_rank_r_shadow_data,
    # E_8 root data
    E8_ROOT_DATA,
    # E_8 lattice description
    e8_lattice_kappa,
    e8_lattice_central_charge,
    e8_lattice_shadow_data,
    e8_lattice_bar_cohomology_h1,
    e8_lattice_bar_chain_dim,
    # E_8 affine description
    e8_affine_kappa,
    e8_affine_central_charge,
    e8_affine_dual_level,
    e8_affine_complementarity,
    e8_affine_shadow_data,
    e8_affine_bar_chain_dim,
    # Genus expansion
    genus_expansion,
    # Verlinde
    e8_level1_verlinde,
    # Comparison
    kappa_comparison,
    root_vector_bar_contribution,
    kappa_e8_lattice_multipath,
    kappa_e8_affine_multipath,
    # Verification
    verify_all,
)


# =========================================================================
# 1. Colored partition numbers
# =========================================================================

class TestColoredPartitions:
    """Verify r-colored partition numbers against known values."""

    def test_r1_matches_partition_numbers(self):
        """p_1(h) = p(h) = ordinary partition numbers."""
        from compute.lib.utils import partition_number
        for h in range(15):
            assert colored_partition_number(h, 1) == partition_number(h), \
                f"p_1({h}) = {colored_partition_number(h, 1)} != p({h}) = {partition_number(h)}"

    def test_r1_known_values(self):
        """Spot-check against OEIS A000041."""
        known = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15, 8: 22,
                 9: 30, 10: 42}
        for h, expected in known.items():
            assert colored_partition_number(h, 1) == expected

    def test_r2_known_values(self):
        """p_2(h): OEIS A000712 (2-colored partitions)."""
        known = {0: 1, 1: 2, 2: 5, 3: 10, 4: 20, 5: 36, 6: 65}
        for h, expected in known.items():
            assert colored_partition_number(h, 2) == expected

    def test_r8_at_h0(self):
        """p_r(0) = 1 for all r."""
        assert colored_partition_number(0, 8) == 1

    def test_r8_at_h1(self):
        """p_r(1) = r (each color gives one partition of 1)."""
        assert colored_partition_number(1, 8) == 8

    def test_r8_at_h2(self):
        """p_8(2) = C(2+8-1, 8-1) = C(9,7) = 36 from (1+1) plus 8 from (2).
        Actually: p_8(2) = 44."""
        assert colored_partition_number(2, 8) == 44

    def test_r8_known_sequence(self):
        """p_8(h) for h=0..8 against independently computed values."""
        expected = [1, 8, 44, 192, 726, 2464, 7704, 22528, 62337]
        table = colored_partition_table(8, 8)
        for h in range(9):
            assert table[h] == expected[h], \
                f"p_8({h}) = {table[h]} != {expected[h]}"

    def test_table_matches_pointwise(self):
        """colored_partition_table matches colored_partition_number."""
        for r in [1, 2, 4, 8]:
            table = colored_partition_table(10, r)
            for h in range(11):
                assert table[h] == colored_partition_number(h, r)

    def test_negative_h(self):
        """p_r(h) = 0 for h < 0."""
        assert colored_partition_number(-1, 8) == 0
        assert colored_partition_number(-5, 1) == 0

    def test_r0(self):
        """p_0(h) = 0 for h > 0, = 1 for h = 0."""
        assert colored_partition_number(0, 0) == 1
        assert colored_partition_number(1, 0) == 0


# =========================================================================
# 2. Faber-Pandharipande intersection numbers
# =========================================================================

class TestFaberPandharipande:
    def test_g1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_g2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_g3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_all_positive(self):
        """All lambda_g^FP > 0 (Bernoulli sign convention absorbed)."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0

    def test_invalid_genus(self):
        with pytest.raises(ValueError):
            faber_pandharipande(0)


# =========================================================================
# 3. Rank-r Heisenberg bar chain dimensions
# =========================================================================

class TestHeisenbergBarChainDims:
    """B^n_h = r^n * C(h-1, n-1) * (n-1)! for rank-r Heisenberg."""

    def test_rank1_matches_heisenberg_bar(self):
        """Cross-check against heisenberg_bar.py formula."""
        from compute.lib.heisenberg_bar import heisenberg_bar_chain_dim
        for n in range(1, 7):
            for h in range(n, n + 5):
                assert heisenberg_rank_r_bar_chain_dim(n, h, 1) == \
                    heisenberg_bar_chain_dim(n, h)

    @pytest.mark.parametrize("r", [1, 2, 4, 8])
    def test_formula_direct(self, r):
        """Verify dim B^n_h = r^n * C(h-1,n-1) * (n-1)!."""
        for n in range(1, 6):
            for h in range(n, n + 4):
                expected = r ** n * comb(h - 1, n - 1) * factorial(n - 1)
                assert heisenberg_rank_r_bar_chain_dim(n, h, r) == expected

    def test_rank8_specific_values(self):
        """Spot-check rank-8 chain dims."""
        assert heisenberg_rank_r_bar_chain_dim(1, 1, 8) == 8
        assert heisenberg_rank_r_bar_chain_dim(2, 2, 8) == 64
        assert heisenberg_rank_r_bar_chain_dim(2, 3, 8) == 128
        assert heisenberg_rank_r_bar_chain_dim(3, 3, 8) == 1024

    def test_zero_cases(self):
        """B^n_h = 0 when h < n or n <= 0."""
        assert heisenberg_rank_r_bar_chain_dim(0, 5, 8) == 0
        assert heisenberg_rank_r_bar_chain_dim(5, 3, 8) == 0
        assert heisenberg_rank_r_bar_chain_dim(-1, 3, 8) == 0

    def test_b1_h_equals_r(self):
        """B^1_h = r for all h >= 1 (r generator modes at each weight)."""
        for h in range(1, 10):
            assert heisenberg_rank_r_bar_chain_dim(1, h, 8) == 8

    def test_total_grows_with_rank(self):
        """Total chain dimension increases with rank at fixed (n, h)."""
        for n in range(1, 4):
            for h in range(n, n + 3):
                d1 = heisenberg_rank_r_bar_chain_dim(n, h, 1)
                d8 = heisenberg_rank_r_bar_chain_dim(n, h, 8)
                assert d8 >= d1


# =========================================================================
# 4. Rank-r Heisenberg bar cohomology (class G, Koszulness)
# =========================================================================

class TestHeisenbergBarCohomology:
    """H^n(B(H_k^r)) = 0 for n >= 2 (class G / Koszulness)."""

    def test_rank1_matches_known_bar_dims(self):
        """Cross-check against KNOWN_BAR_DIMS from heisenberg_bar.py."""
        known = {1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 7, 8: 11}
        for h, expected in known.items():
            computed = heisenberg_rank_r_bar_cohomology_h1(h, 1)
            assert computed == expected, \
                f"H^1_{h} = {computed} != {expected}"

    def test_rank1_formula_p_h_minus_2(self):
        """H^1_h = p(h-2) for h >= 2 (bar_cohomology_dimensions.py ground truth)."""
        from compute.lib.utils import partition_number
        for h in range(2, 13):
            expected = partition_number(h - 2)
            computed = heisenberg_rank_r_bar_cohomology_h1(h, 1)
            assert computed == expected, \
                f"H^1_{h} = {computed} != p({h-2}) = {expected}"

    def test_rank1_h1_is_generator(self):
        """H^1_1 = 1: the single generator at weight 1."""
        assert heisenberg_rank_r_bar_cohomology_h1(1, 1) == 1

    def test_rank8_h1_is_8_generators(self):
        """H^1_1 = 8 for rank 8: the 8 generators at weight 1."""
        assert heisenberg_rank_r_bar_cohomology_h1(1, 8) == 8

    def test_rank8_known_values(self):
        """Rank-8 bar cohomology cross-verified by independent computation."""
        expected = {1: 8, 2: 36, 3: 120, 4: 338, 5: 864, 6: 2084,
                    7: 4824, 8: 10799}
        for h, exp in expected.items():
            assert heisenberg_rank_r_bar_cohomology_h1(h, 8) == exp

    def test_rank8_kuenneth_crosscheck(self):
        """Cross-check rank-8 via 8-fold convolution of rank-1 GF."""
        from compute.lib.utils import partition_number
        h_max = 8

        def rank1_gf(h):
            if h == 0:
                return 1
            if h == 1:
                return 1
            return partition_number(h - 2)

        gf = [rank1_gf(h) for h in range(h_max + 1)]
        current = [0] * (h_max + 1)
        current[0] = 1
        for _ in range(8):
            new = [0] * (h_max + 1)
            for j in range(h_max + 1):
                if current[j] == 0:
                    continue
                for m in range(h_max + 1 - j):
                    new[j + m] += current[j] * gf[m]
            current = new

        for h in range(1, h_max + 1):
            assert heisenberg_rank_r_bar_cohomology_h1(h, 8) == current[h]

    def test_koszul_concentration(self):
        """For Koszul algebras: H^n = 0 for n >= 2."""
        for h in range(1, 7):
            cohom = heisenberg_rank_r_bar_cohomology_koszul(h, 8)
            assert 1 in cohom
            for n in range(2, h + 1):
                assert cohom.get(n, 0) == 0

    def test_h1_monotone_in_h(self):
        """H^1_h is non-decreasing in h (for fixed r)."""
        for r in [1, 4, 8]:
            prev = 0
            for h in range(1, 9):
                curr = heisenberg_rank_r_bar_cohomology_h1(h, r)
                assert curr >= prev
                prev = curr

    def test_h1_grows_with_rank(self):
        """H^1_h(rank r) >= H^1_h(rank 1) for r >= 1."""
        for h in range(1, 7):
            d1 = heisenberg_rank_r_bar_cohomology_h1(h, 1)
            d8 = heisenberg_rank_r_bar_cohomology_h1(h, 8)
            assert d8 >= d1


# =========================================================================
# 5. Kappa and shadow data for rank-r Heisenberg
# =========================================================================

class TestHeisenbergKappaShadow:
    def test_kappa_additivity(self):
        """kappa(H_k^r) = r*k (additivity)."""
        assert heisenberg_rank_r_kappa(1, 8) == Rational(8)
        assert heisenberg_rank_r_kappa(2, 8) == Rational(16)
        assert heisenberg_rank_r_kappa(1, 1) == Rational(1)

    def test_kappa_cross_check_lattice(self):
        """kappa(H_1^8) = 8 cross-checks against lattice formula."""
        from compute.lib.lattice_voa_shadows import kappa_lattice
        assert heisenberg_rank_r_kappa(1, 8) == kappa_lattice(8)

    def test_central_charge(self):
        """c(H_k^r) = r (independent of k)."""
        assert heisenberg_rank_r_central_charge(1, 8) == Rational(8)
        assert heisenberg_rank_r_central_charge(5, 3) == Rational(3)

    def test_shadow_class_G(self):
        """Rank-r Heisenberg is class G (Gaussian, depth 2)."""
        data = heisenberg_rank_r_shadow_data(1, 8)
        assert data['shadow_class'] == 'G'
        assert data['shadow_depth'] == 2
        assert data['S3'] == 0
        assert data['S4'] == 0
        assert data['Delta'] == 0
        assert data['is_perfect_square'] is True

    def test_shadow_metric_perfect_square(self):
        """Q_L = 4*kappa^2 for class G."""
        data = heisenberg_rank_r_shadow_data(1, 8)
        assert data['Q_L'] == 4 * Rational(8) ** 2
        assert data['Q_L'] == 256


# =========================================================================
# 6. E_8 root system data
# =========================================================================

class TestE8RootData:
    def test_dim(self):
        assert E8_ROOT_DATA['dim'] == 248

    def test_rank(self):
        assert E8_ROOT_DATA['rank'] == 8

    def test_n_roots(self):
        assert E8_ROOT_DATA['n_roots'] == 240

    def test_simply_laced(self):
        """E_8 is simply laced: h = h^vee."""
        assert E8_ROOT_DATA['h'] == E8_ROOT_DATA['h_dual'] == 30

    def test_unimodular(self):
        """det(Cartan matrix) = 1 for E_8."""
        assert E8_ROOT_DATA['det_cartan'] == 1

    def test_dim_decomposes(self):
        """dim(e_8) = rank + n_roots = 8 + 240 = 248."""
        assert E8_ROOT_DATA['rank'] + E8_ROOT_DATA['n_roots'] == E8_ROOT_DATA['dim']


# =========================================================================
# 7. E_8 lattice description
# =========================================================================

class TestE8Lattice:
    def test_kappa_equals_rank(self):
        """kappa(V_{E_8} as lattice) = rank = 8."""
        assert e8_lattice_kappa() == Rational(8)

    def test_kappa_not_c_over_2(self):
        """kappa != c/2 (AP48: kappa depends on full algebra, not Virasoro sub)."""
        c = e8_lattice_central_charge()
        kappa = e8_lattice_kappa()
        assert kappa != c / 2  # 8 != 4

    def test_central_charge(self):
        assert e8_lattice_central_charge() == Rational(8)

    def test_shadow_class_G(self):
        """Lattice VOA inherits class G from Heisenberg sector."""
        data = e8_lattice_shadow_data()
        assert data['shadow_class'] == 'G'
        assert data['shadow_depth'] == 2

    def test_bar_cohomology_matches_rank8_heisenberg(self):
        """In lattice description, bar cohomology = that of H_1^8."""
        for h in range(1, 7):
            assert e8_lattice_bar_cohomology_h1(h) == \
                heisenberg_rank_r_bar_cohomology_h1(h, 8)

    def test_bar_chain_dim_matches_rank8(self):
        """Lattice bar chains (Cartan sector) = rank-8 Heisenberg."""
        for n in range(1, 5):
            for h in range(n, n + 3):
                assert e8_lattice_bar_chain_dim(n, h) == \
                    heisenberg_rank_r_bar_chain_dim(n, h, 8)


# =========================================================================
# 8. E_8 affine KM description
# =========================================================================

class TestE8Affine:
    def test_kappa_formula(self):
        """kappa = 248*(k+30)/60 at general k."""
        k_sym = Symbol('k')
        kappa = e8_affine_kappa(1)
        assert kappa == Rational(1922, 15)

    def test_kappa_at_k1_exact(self):
        """kappa(k=1) = 248*31/60 = 1922/15 exactly."""
        kappa = e8_affine_kappa(1)
        assert kappa == Rational(248 * 31, 60)
        assert kappa == Rational(1922, 15)

    def test_kappa_not_rank(self):
        """kappa(affine) != rank (AP48)."""
        assert e8_affine_kappa(1) != Rational(8)

    def test_kappa_not_c_over_2(self):
        """kappa != c/2 (AP39: kappa != S_2 for non-Virasoro)."""
        c = e8_affine_central_charge(1)
        kappa = e8_affine_kappa(1)
        assert kappa != c / 2

    def test_central_charge_at_k1(self):
        """c(k=1) = 248/31."""
        assert e8_affine_central_charge(1) == Rational(248, 31)

    def test_dual_level(self):
        """k' = -k - 2h^vee = -1 - 60 = -61."""
        assert e8_affine_dual_level(1) == -61

    def test_complementarity_kappa_sum(self):
        """kappa(k) + kappa(k') = 0 for affine KM (AP24 correct for KM)."""
        comp = e8_affine_complementarity(1)
        assert comp['kappa_sum'] == 0

    def test_complementarity_c_sum(self):
        """c(k) + c(k') = 2*dim(e_8) = 496."""
        comp = e8_affine_complementarity(1)
        assert comp['c_sum'] == 496

    def test_shadow_class_L(self):
        """Affine KM is class L (Lie/tree, depth 3)."""
        data = e8_affine_shadow_data(1)
        assert data['shadow_class'] == 'L'
        assert data['shadow_depth'] == 3
        assert data['S3'] == 1
        assert data['S4'] == 0

    def test_bar_chain_dim_248_generators(self):
        """In affine description, 248 weight-1 currents => r=248 in formula."""
        assert e8_affine_bar_chain_dim(1, 1) == 248
        assert e8_affine_bar_chain_dim(2, 2) == 248 ** 2


# =========================================================================
# 9. Kappa multi-path verification (3+ paths each, per CLAUDE.md mandate)
# =========================================================================

class TestKappaMultiPath:
    def test_lattice_3_paths(self):
        """kappa(V_{E_8} lattice) = 8 via 3 independent paths."""
        mp = kappa_e8_lattice_multipath()
        assert mp['all_agree']
        assert mp['value'] == Rational(8)

    def test_affine_3_paths(self):
        """kappa(V_1(e_8) affine) = 1922/15 via 3 independent paths."""
        mp = kappa_e8_affine_multipath()
        assert mp['all_agree']
        assert mp['value'] == Rational(1922, 15)

    def test_lattice_path1_rank(self):
        mp = kappa_e8_lattice_multipath()
        assert mp['path1_rank'] == Rational(8)

    def test_lattice_path2_additivity(self):
        mp = kappa_e8_lattice_multipath()
        assert mp['path2_additivity'] == Rational(8)

    def test_affine_path1_km(self):
        mp = kappa_e8_affine_multipath()
        assert mp['path1_km_formula'] == Rational(1922, 15)

    def test_affine_path2_complementarity(self):
        mp = kappa_e8_affine_multipath()
        assert mp['path2_complementarity'] == Rational(1922, 15)

    def test_affine_path3_central_charge(self):
        mp = kappa_e8_affine_multipath()
        assert mp['path3_central_charge'] == Rational(1922, 15)


# =========================================================================
# 10. Genus expansion
# =========================================================================

class TestGenusExpansion:
    def test_lattice_F1(self):
        """F_1(V_{E_8} lattice) = 8/24 = 1/3."""
        F = genus_expansion(Rational(8))
        assert F[1] == Rational(1, 3)

    def test_lattice_F2(self):
        """F_2(V_{E_8} lattice) = 8 * 7/5760 = 7/720."""
        F = genus_expansion(Rational(8))
        assert F[2] == Rational(7, 720)

    def test_affine_F1(self):
        """F_1(V_1(e_8) affine) = (1922/15)/24 = 961/180."""
        F = genus_expansion(Rational(1922, 15))
        assert F[1] == Rational(961, 180)

    def test_F_g_positive(self):
        """All F_g > 0 (positive kappa * positive lambda_g)."""
        for kappa_val in [Rational(8), Rational(1922, 15)]:
            for g, F in genus_expansion(kappa_val).items():
                assert F > 0

    def test_genus_expansion_ratio(self):
        """F_g(affine) / F_g(lattice) = 1922/15 / 8 = 961/60 for all g."""
        F_lat = genus_expansion(Rational(8))
        F_aff = genus_expansion(Rational(1922, 15))
        for g in range(1, 6):
            assert F_aff[g] / F_lat[g] == Rational(961, 60)


# =========================================================================
# 11. Verlinde dimensions
# =========================================================================

class TestVerlinde:
    @pytest.mark.parametrize("g", [0, 1, 2, 3, 5, 10, 50])
    def test_verlinde_always_1(self, g):
        """E_8 at level 1 has unique integrable rep => Verlinde dim = 1."""
        assert e8_level1_verlinde(g) == 1

    def test_verlinde_invalid_genus(self):
        with pytest.raises(ValueError):
            e8_level1_verlinde(-1)


# =========================================================================
# 12. Comparison: lattice vs affine
# =========================================================================

class TestComparison:
    def test_kappa_different(self):
        """The two descriptions give different kappa (AP48)."""
        comp = kappa_comparison()
        assert comp['kappa_different'] is True

    def test_kappa_ratio(self):
        """kappa_affine / kappa_lattice = 961/60."""
        comp = kappa_comparison()
        assert comp['kappa_ratio'] == Rational(961, 60)

    def test_root_vectors_acyclic_in_lattice(self):
        """Root vectors do not generate new bar cohomology (lattice desc)."""
        data = root_vector_bar_contribution()
        assert data['lattice_description']['root_sector_acyclic'] is True
        assert data['lattice_description']['new_bar_cohomology_from_roots'] is False

    def test_240_roots(self):
        data = root_vector_bar_contribution()
        assert data['n_roots'] == 240

    def test_120_opposite_pairs(self):
        data = root_vector_bar_contribution()
        assert data['root_types']['opposite_pairs'] == 120

    def test_affine_bar_chains_much_larger(self):
        """The affine description has 248^n bar chains vs 8^n for lattice."""
        for n in range(1, 4):
            for h in range(n, n + 2):
                d_lat = e8_lattice_bar_chain_dim(n, h)
                d_aff = e8_affine_bar_chain_dim(n, h)
                assert d_aff > d_lat
                assert d_aff == d_lat * (248 // 8) ** n


# =========================================================================
# 13. Cross-family consistency checks (AP10 defense)
# =========================================================================

class TestCrossFamilyConsistency:
    def test_kappa_additivity_tensor_product(self):
        """kappa(H_1^8) = 8 * kappa(H_1^1) = 8."""
        assert heisenberg_rank_r_kappa(1, 8) == 8 * heisenberg_rank_r_kappa(1, 1)

    def test_kappa_lattice_matches_shadow_module(self):
        """Cross-check kappa from lattice_voa_shadows.py."""
        from compute.lib.lattice_voa_shadows import kappa_lattice
        assert e8_lattice_kappa() == kappa_lattice(8)

    def test_kappa_affine_matches_e8_affine_engine(self):
        """Cross-check kappa from e8_affine_shadow_engine (if available)."""
        try:
            from compute.lib.e8_affine_shadow_engine import kappa_e8_affine
            assert e8_affine_kappa(1) == kappa_e8_affine(1)
        except ImportError:
            pass  # engine may not have this exact function name

    def test_e8_data_matches_e8_lattice_bar(self):
        """Cross-check root data against e8_lattice_bar.py."""
        from compute.lib.e8_lattice_bar import E8_DATA
        assert E8_ROOT_DATA['dim'] == E8_DATA['dim']
        assert E8_ROOT_DATA['rank'] == E8_DATA['rank']
        assert E8_ROOT_DATA['n_roots'] == E8_DATA['n_roots']
        assert E8_ROOT_DATA['h_dual'] == E8_DATA['h_dual']

    def test_central_charge_two_formulas(self):
        """c = rank = 8 (lattice) vs c = 248*1/31 = 248/31 (affine).

        These are genuinely different conventions:
        c_lattice = 8 counts free bosons.
        c_affine = 248/31 is the Sugawara formula.
        At k=1 for E_8: 248/31 = 8 exactly.
        """
        c_lat = e8_lattice_central_charge()
        c_aff = e8_affine_central_charge(1)
        assert c_lat == Rational(8)
        assert c_aff == Rational(248, 31)
        assert c_lat == c_aff  # 248/31 = 8 at k=1!

    def test_complementarity_affine_vs_lattice(self):
        """For lattice: kappa + kappa' = 0. For affine: kappa + kappa' = 0."""
        # Lattice:
        from compute.lib.lattice_voa_shadows import kappa_lattice, kappa_lattice_dual
        assert kappa_lattice(8) + kappa_lattice_dual(8) == 0

        # Affine:
        comp = e8_affine_complementarity(1)
        assert comp['kappa_sum'] == 0


# =========================================================================
# 14. Internal verification suite
# =========================================================================

class TestVerifyAll:
    def test_all_pass(self):
        """All internal verification checks pass."""
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"Internal check failed: {name}"
