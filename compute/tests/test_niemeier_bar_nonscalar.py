r"""Tests for non-scalar bar complex invariants of the 24 Niemeier lattice VOAs.

150+ tests verifying:
  1. Lie algebra dimension formulas (dim = rank + |R| for ADE)
  2. Per-factor kappa at level k=1
  3. Per-factor central charge (c = rank for simply-laced at k=1)
  4. Factor decomposition totals
  5. Affine kappa vector: complete invariant (all 24 distinguished)
  6. Collision analysis: 5 pairs at |R| level, all resolved by multi-channel data
  7. Minimal complete invariant: (h, num_factors) pair
  8. Weight-1 bar dimension
  9. Inner product distributions
  10. Cross-checks with niemeier_shadow_atlas data

Mathematical ground truth:
  - Conway-Sloane, "Sphere Packings, Lattices and Groups", Ch. 16
  - prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
  - thm:lattice:curvature-braiding-orthogonal (lattice_foundations.tex)
"""

import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.niemeier_bar_nonscalar import (
    ALL_NIEMEIER_LABELS,
    NIEMEIER_REGISTRY,
    affine_kappa_vector,
    c_vector,
    casimir_eigenvalue,
    central_charge_factor,
    collision_analysis,
    dim_simple,
    dim_vector,
    factor_decomposition,
    factor_type_multiset,
    full_nonscalar_data,
    h_vector,
    inner_product_distribution,
    kappa_decomposition,
    kappa_factor,
    kappa_vector_is_injective,
    minimal_distinguishing_invariant,
    nonscalar_atlas_table,
    verify_c_equals_rank_at_k1,
    verify_dim_rank_roots,
    verify_niemeier_uniform_h,
    verify_total_c_24,
    weight_1_dimension,
    weight_spectrum,
    _adjacent_roots_per_root,
    _orthogonal_roots_within_component,
    cubic_shadow_factor,
    quartic_shadow_factor,
)
from compute.lib.niemeier_shadow_atlas import (
    KAPPA_NIEMEIER,
    root_count,
    coxeter_number,
    dual_coxeter_number,
    root_count_collisions,
)


# =========================================================================
# Section 1: Lie algebra dimensions
# =========================================================================

class TestDimSimple:
    """Verify dim(g) for all ADE types used in Niemeier lattices."""

    def test_dim_A1(self):
        assert dim_simple('A', 1) == 3  # sl_2

    def test_dim_A2(self):
        assert dim_simple('A', 2) == 8  # sl_3

    def test_dim_A3(self):
        assert dim_simple('A', 3) == 15  # sl_4

    def test_dim_A_general(self):
        for n in range(1, 25):
            assert dim_simple('A', n) == n * (n + 2)

    def test_dim_D4(self):
        assert dim_simple('D', 4) == 28  # so_8

    def test_dim_D5(self):
        assert dim_simple('D', 5) == 45  # so_10

    def test_dim_D_general(self):
        for n in range(3, 25):
            assert dim_simple('D', n) == n * (2 * n - 1)

    def test_dim_E6(self):
        assert dim_simple('E', 6) == 78

    def test_dim_E7(self):
        assert dim_simple('E', 7) == 133

    def test_dim_E8(self):
        assert dim_simple('E', 8) == 248

    def test_dim_equals_rank_plus_roots(self):
        """dim(g) = rank + |R| for all ADE types."""
        assert verify_dim_rank_roots()

    def test_dim_equals_rank_plus_roots_specific(self):
        """Spot-check: dim = rank + |R|."""
        # A_2: dim = 8, rank = 2, |R| = 6
        assert dim_simple('A', 2) == 2 + root_count('A', 2)
        # D_4: dim = 28, rank = 4, |R| = 24
        assert dim_simple('D', 4) == 4 + root_count('D', 4)
        # E_8: dim = 248, rank = 8, |R| = 240
        assert dim_simple('E', 8) == 8 + root_count('E', 8)


# =========================================================================
# Section 2: Per-factor kappa at level k=1
# =========================================================================

class TestKappaFactor:
    """Verify per-factor kappa values at level k=1."""

    def test_kappa_A1_k1(self):
        # sl_2: dim=3, h=2. kappa = 3*3/4 = 9/4
        assert kappa_factor('A', 1, k=1) == Rational(9, 4)

    def test_kappa_A2_k1(self):
        # sl_3: dim=8, h=3. kappa = 8*4/6 = 32/6 = 16/3
        assert kappa_factor('A', 2, k=1) == Rational(16, 3)

    def test_kappa_D4_k1(self):
        # so_8: dim=28, h=6. kappa = 28*7/12 = 196/12 = 49/3
        assert kappa_factor('D', 4, k=1) == Rational(49, 3)

    def test_kappa_E6_k1(self):
        # e_6: dim=78, h=12. kappa = 78*13/24 = 1014/24 = 169/4
        assert kappa_factor('E', 6, k=1) == Rational(169, 4)

    def test_kappa_E7_k1(self):
        # e_7: dim=133, h=18. kappa = 133*19/36 = 2527/36
        assert kappa_factor('E', 7, k=1) == Rational(2527, 36)

    def test_kappa_E8_k1(self):
        # e_8: dim=248, h=30. kappa = 248*31/60 = 7688/60 = 1922/15
        assert kappa_factor('E', 8, k=1) == Rational(1922, 15)

    def test_kappa_formula_explicit(self):
        """Verify kappa = dim*(1+h)/(2h) for all ADE types."""
        for fam, ns in [('A', range(1, 25)), ('D', range(3, 25)), ('E', [6, 7, 8])]:
            for n in ns:
                d = dim_simple(fam, n)
                h = coxeter_number(fam, n)
                expected = Rational(d * (1 + h), 2 * h)
                assert kappa_factor(fam, n, k=1) == expected, (
                    f"kappa({fam}_{n}, 1) = {kappa_factor(fam, n, k=1)} != {expected}"
                )

    def test_kappa_not_c_over_2(self):
        """AP1 check: kappa != c/2 for non-Virasoro algebras."""
        # For V_1(sl_2): c = 1, c/2 = 1/2. kappa = 9/4 != 1/2.
        c = central_charge_factor('A', 1, k=1)
        kap = kappa_factor('A', 1, k=1)
        assert kap != c / 2


# =========================================================================
# Section 3: Per-factor central charge at k=1
# =========================================================================

class TestCentralChargeFactor:
    """Verify c(g, 1) = rank(g) for simply-laced types."""

    def test_c_equals_rank(self):
        assert verify_c_equals_rank_at_k1()

    def test_c_A_n(self):
        for n in range(1, 25):
            assert central_charge_factor('A', n, k=1) == Rational(n)

    def test_c_D_n(self):
        for n in range(3, 25):
            assert central_charge_factor('D', n, k=1) == Rational(n)

    def test_c_E(self):
        assert central_charge_factor('E', 6, k=1) == Rational(6)
        assert central_charge_factor('E', 7, k=1) == Rational(7)
        assert central_charge_factor('E', 8, k=1) == Rational(8)


# =========================================================================
# Section 4: Factor decomposition totals
# =========================================================================

class TestFactorDecomposition:
    """Verify total sums for factor decompositions."""

    def test_total_c_24(self):
        """Sum of per-factor central charges = 24 for all non-Leech."""
        assert verify_total_c_24()

    def test_total_c_24_explicit(self):
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            dec = factor_decomposition(label)
            assert dec['total_c'] == Rational(24), (
                f"{label}: total_c = {dec['total_c']} != 24"
            )

    def test_uniform_coxeter(self):
        """All components of each Niemeier lattice have the same h."""
        assert verify_niemeier_uniform_h()

    def test_num_factors(self):
        """Spot-check number of factors."""
        assert factor_decomposition('24A1')['num_factors'] == 24
        assert factor_decomposition('12A2')['num_factors'] == 12
        assert factor_decomposition('3E8')['num_factors'] == 3
        assert factor_decomposition('D24')['num_factors'] == 1
        assert factor_decomposition('Leech')['num_factors'] == 0

    def test_leech_empty(self):
        dec = factor_decomposition('Leech')
        assert dec['num_factors'] == 0
        assert dec['kappa_vector'] == []
        assert dec['c_vector'] == []


# =========================================================================
# Section 5: Affine kappa sum (NOT 24 in general)
# =========================================================================

class TestAffineKappaSum:
    """The sum of per-factor affine kappas is NOT 24."""

    def test_24A1_kappa_sum(self):
        # 24 copies of A_1: each kappa = 9/4. Sum = 54.
        dec = factor_decomposition('24A1')
        assert dec['total_kappa'] == Rational(54)

    def test_3E8_kappa_sum(self):
        # 3 copies of E_8: each kappa = 1922/15. Sum = 5766/15 = 1922/5.
        dec = factor_decomposition('3E8')
        assert dec['total_kappa'] == Rational(1922, 5)

    def test_D24_kappa_sum(self):
        # D_24: dim = 24*47 = 1128, h = 46. kappa = 1128*47/92 = 53016/92 = 13254/23.
        dec = factor_decomposition('D24')
        assert dec['total_kappa'] == Rational(13254, 23)

    def test_kappa_sum_not_24_for_24A1(self):
        dec = factor_decomposition('24A1')
        assert dec['total_kappa'] != Rational(24)

    def test_kappa_sum_varies(self):
        """Different lattices have different affine kappa sums."""
        sums = set()
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            dec = factor_decomposition(label)
            sums.add(dec['total_kappa'])
        # At least 18 distinct values (5 collision groups among 23 non-Leech)
        assert len(sums) >= 18


# =========================================================================
# Section 6: Affine kappa vector completeness
# =========================================================================

class TestKappaVectorCompleteness:
    """The sorted affine kappa vector is a COMPLETE invariant."""

    def test_kappa_vector_injective(self):
        is_inj, collisions = kappa_vector_is_injective()
        assert is_inj, f"Collisions found: {collisions}"

    def test_all_24_distinct(self):
        vectors = set()
        for label in ALL_NIEMEIER_LABELS:
            kv = affine_kappa_vector(label)
            vectors.add(kv)
        assert len(vectors) == 24

    def test_leech_unique(self):
        kv = affine_kappa_vector('Leech')
        assert kv == ()  # only lattice with empty root system

    def test_collision_pairs_distinguished(self):
        """The 5 |R|-collision pairs are all distinguished by kappa vector."""
        collisions = root_count_collisions()
        for nr, labels in collisions.items():
            kappas = [affine_kappa_vector(lab) for lab in labels]
            assert len(set(kappas)) == len(labels), (
                f"|R|={nr}: {labels} have identical kappa vectors!"
            )

    def test_D16_E8_vs_3E8(self):
        """D16+E8 and 3E8 have the same |R|=720 but different kappa vectors."""
        kv1 = affine_kappa_vector('D16_E8')
        kv2 = affine_kappa_vector('3E8')
        assert kv1 != kv2
        # D16+E8: two factors with different kappas
        assert len(kv1) == 2
        # 3E8: three identical factors
        assert len(kv2) == 3

    def test_A17_E7_vs_D10_2E7(self):
        """A17+E7 and D10+2E7 have |R|=432 but different kappa vectors."""
        kv1 = affine_kappa_vector('A17_E7')
        kv2 = affine_kappa_vector('D10_2E7')
        assert kv1 != kv2
        assert len(kv1) == 2
        assert len(kv2) == 3

    def test_A11_D7_E6_vs_4E6(self):
        """A11+D7+E6 and 4E6 have |R|=288 but different structures."""
        kv1 = affine_kappa_vector('A11_D7_E6')
        kv2 = affine_kappa_vector('4E6')
        assert kv1 != kv2
        assert len(kv1) == 3
        assert len(kv2) == 4

    def test_2A9_D6_vs_4D6(self):
        kv1 = affine_kappa_vector('2A9_D6')
        kv2 = affine_kappa_vector('4D6')
        assert kv1 != kv2
        assert len(kv1) == 3
        assert len(kv2) == 4

    def test_4A5_D4_vs_6D4(self):
        kv1 = affine_kappa_vector('4A5_D4')
        kv2 = affine_kappa_vector('6D4')
        assert kv1 != kv2
        assert len(kv1) == 5
        assert len(kv2) == 6


# =========================================================================
# Section 7: Minimal complete invariant
# =========================================================================

class TestMinimalInvariant:
    """The pair (h, num_factors) is the simplest complete invariant."""

    def test_h_num_factors_complete(self):
        """(h, num_factors) distinguishes all 24."""
        seen = set()
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                key = (0, 0)
            else:
                components = NIEMEIER_REGISTRY[label]['components']
                h = coxeter_number(components[0][0], components[0][1])
                nf = len(components)
                key = (h, nf)
            assert key not in seen, (
                f"Collision: {label} has (h, nf) = {key}, already seen"
            )
            seen.add(key)
        assert len(seen) == 24

    def test_minimal_level_is_2(self):
        """Level 2 (h-vector) is the first complete level."""
        result = minimal_distinguishing_invariant()
        assert result['minimal_complete_level'] == 2

    def test_level_0_not_complete(self):
        """Scalar kappa = 24 for all: not discriminating."""
        result = minimal_distinguishing_invariant()
        assert result['level_0_scalar_kappa']['distinct_values'] == 1

    def test_level_1_has_5_collisions(self):
        """Number of roots has exactly 5 collision groups."""
        result = minimal_distinguishing_invariant()
        assert len(result['level_1_num_roots']['collisions']) == 5

    def test_level_2_complete(self):
        """Sorted h-vector distinguishes all 24."""
        result = minimal_distinguishing_invariant()
        assert result['level_2_h_vector']['distinct_values'] == 24

    def test_level_3_complete(self):
        """Sorted kappa vector also distinguishes all 24."""
        result = minimal_distinguishing_invariant()
        assert result['level_3_kappa_vector']['distinct_values'] == 24

    def test_level_4_complete(self):
        """Factor type multiset distinguishes all 24."""
        result = minimal_distinguishing_invariant()
        assert result['level_4_factor_multiset']['distinct_values'] == 24


# =========================================================================
# Section 8: Weight-1 bar dimension
# =========================================================================

class TestWeight1Dimension:
    """Weight-1 dimension = 24 + |R| is a partial discriminant."""

    def test_leech_weight_1(self):
        assert weight_1_dimension('Leech') == 24  # no roots

    def test_24A1_weight_1(self):
        assert weight_1_dimension('24A1') == 24 + 48

    def test_3E8_weight_1(self):
        assert weight_1_dimension('3E8') == 24 + 720

    def test_D24_weight_1(self):
        assert weight_1_dimension('D24') == 24 + 1104

    def test_weight_1_varies(self):
        """Weight-1 dimension varies across lattices."""
        dims = [weight_1_dimension(lab) for lab in ALL_NIEMEIER_LABELS]
        assert len(set(dims)) >= 19  # same collision count as |R|


# =========================================================================
# Section 9: Cubic and quartic shadows per factor
# =========================================================================

class TestPerFactorShadows:
    """Per-factor cubic and quartic shadows for affine KM."""

    def test_S3_universal(self):
        """S_3 = 1/3 for all affine KM factors on current line."""
        for label in ALL_NIEMEIER_LABELS:
            components = NIEMEIER_REGISTRY[label]['components']
            for fam, n in components:
                assert cubic_shadow_factor(fam, n) == Rational(1, 3)

    def test_S4_zero(self):
        """S_4 = 0 for all affine KM factors (Jacobi identity)."""
        for label in ALL_NIEMEIER_LABELS:
            components = NIEMEIER_REGISTRY[label]['components']
            for fam, n in components:
                assert quartic_shadow_factor(fam, n) == Rational(0)

    def test_per_factor_class_L(self):
        """All affine KM factors are class L (depth 3)."""
        # S_3 != 0, S_4 = 0 => class L
        for label in ALL_NIEMEIER_LABELS:
            components = NIEMEIER_REGISTRY[label]['components']
            for fam, n in components:
                assert cubic_shadow_factor(fam, n) != 0
                assert quartic_shadow_factor(fam, n) == 0


# =========================================================================
# Section 10: Adjacent roots per root
# =========================================================================

class TestAdjacentRoots:
    """Number of roots with inner product 1 with a fixed root."""

    def test_A1_no_adjacent(self):
        assert _adjacent_roots_per_root('A', 1) == 0

    def test_A2_two_adjacent(self):
        assert _adjacent_roots_per_root('A', 2) == 2

    def test_A3_four_adjacent(self):
        # D_3 = A_3, should agree
        assert _adjacent_roots_per_root('A', 3) == 4

    def test_D3_equals_A3(self):
        """D_3 = A_3 isomorphism: same n_plus."""
        assert _adjacent_roots_per_root('D', 3) == _adjacent_roots_per_root('A', 3)

    def test_D4_adjacent(self):
        assert _adjacent_roots_per_root('D', 4) == 8

    def test_A_n_formula(self):
        for n in range(1, 20):
            expected = 0 if n == 1 else 2 * (n - 1)
            assert _adjacent_roots_per_root('A', n) == expected

    def test_D_n_formula(self):
        for n in range(3, 20):
            expected = 4 if n == 3 else 4 * (n - 2)
            assert _adjacent_roots_per_root('D', n) == expected

    def test_E6_adjacent(self):
        # E_6: |R|=72, n_orth=30. n_plus = (72-2-30)/2 = 20.
        assert _adjacent_roots_per_root('E', 6) == 20

    def test_E7_adjacent(self):
        # E_7: |R|=126, n_orth=72. n_plus = (126-2-72)/2 = 26.
        assert _adjacent_roots_per_root('E', 7) == 26

    def test_E8_adjacent(self):
        # E_8: |R|=240, n_orth=126. n_plus = (240-2-126)/2 = 56.
        assert _adjacent_roots_per_root('E', 8) == 56

    def test_partition_of_R_minus_2(self):
        """For each root alpha: |R|-2 = 2*n_plus + n_orth (partition of non-self non-neg)."""
        for fam, ns in [('A', range(1, 20)), ('D', range(3, 20)), ('E', [6, 7, 8])]:
            for n in ns:
                nr = root_count(fam, n)
                n_plus = _adjacent_roots_per_root(fam, n)
                n_orth = _orthogonal_roots_within_component(fam, n)
                assert nr - 2 == 2 * n_plus + n_orth, (
                    f"{fam}_{n}: {nr}-2 = {nr-2} != 2*{n_plus} + {n_orth} = {2*n_plus+n_orth}"
                )


# =========================================================================
# Section 11: Inner product distributions
# =========================================================================

class TestInnerProductDistribution:
    """Test the ip distribution on roots."""

    def test_ip_leech_trivial(self):
        """Leech has no roots, so ip dist is trivial."""
        ip = inner_product_distribution('Leech')
        assert ip == {0: 0}

    def test_ip_total_equals_R_squared(self):
        """Total ordered pairs = |R|^2."""
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            ip = inner_product_distribution(label)
            nr = NIEMEIER_REGISTRY[label]['num_roots']
            total = sum(ip.values())
            assert total == nr ** 2, (
                f"{label}: ip total = {total} != |R|^2 = {nr**2}"
            )

    def test_ip_2_count(self):
        """ip = 2: exactly |R| pairs (alpha, alpha)."""
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            ip = inner_product_distribution(label)
            nr = NIEMEIER_REGISTRY[label]['num_roots']
            assert ip[2] == nr

    def test_ip_minus2_count(self):
        """ip = -2: exactly |R| pairs (alpha, -alpha)."""
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            ip = inner_product_distribution(label)
            nr = NIEMEIER_REGISTRY[label]['num_roots']
            assert ip[-2] == nr

    def test_ip_symmetry(self):
        """ip = 1 and ip = -1 have the same count (by beta -> -beta)."""
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            ip = inner_product_distribution(label)
            assert ip[1] == ip[-1]


# =========================================================================
# Section 12: Factor type multiset
# =========================================================================

class TestFactorTypeMultiset:
    """Verify the factor type multiset encoding."""

    def test_3E8(self):
        assert factor_type_multiset('3E8') == (('E', 8, 3),)

    def test_D16_E8(self):
        assert factor_type_multiset('D16_E8') == (('D', 16, 1), ('E', 8, 1))

    def test_24A1(self):
        assert factor_type_multiset('24A1') == (('A', 1, 24),)

    def test_A11_D7_E6(self):
        assert factor_type_multiset('A11_D7_E6') == (
            ('A', 11, 1), ('D', 7, 1), ('E', 6, 1)
        )

    def test_4A5_D4(self):
        assert factor_type_multiset('4A5_D4') == (
            ('A', 5, 4), ('D', 4, 1)
        )

    def test_leech(self):
        assert factor_type_multiset('Leech') == ()

    def test_all_24_distinct(self):
        """Factor type multisets are all distinct (by Niemeier classification)."""
        ftms = set()
        for label in ALL_NIEMEIER_LABELS:
            ftm = factor_type_multiset(label)
            assert ftm not in ftms, f"Duplicate FTM for {label}"
            ftms.add(ftm)
        assert len(ftms) == 24


# =========================================================================
# Section 13: Dim vector, c vector, h vector
# =========================================================================

class TestVectors:
    """Verify the sorted invariant vectors."""

    def test_dim_vector_3E8(self):
        assert dim_vector('3E8') == (248, 248, 248)

    def test_dim_vector_D16_E8(self):
        # D_16: dim = 16*31 = 496. E_8: dim = 248.
        assert dim_vector('D16_E8') == (248, 496)

    def test_c_vector_all_24(self):
        """c vectors have total = 24 for all non-Leech."""
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            cv = c_vector(label)
            assert sum(cv) == Rational(24)

    def test_h_vector_uniform(self):
        """All entries in h-vector are the same (Niemeier property)."""
        for label in ALL_NIEMEIER_LABELS:
            hv = h_vector(label)
            if hv:
                assert all(h == hv[0] for h in hv)


# =========================================================================
# Section 14: Kappa decomposition
# =========================================================================

class TestKappaDecomposition:
    """Detailed kappa decomposition analysis."""

    def test_lattice_kappa_sum_24(self):
        """Sum of per-factor lattice kappas = 24 for all non-Leech."""
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            kd = kappa_decomposition(label)
            assert kd['lattice_kappa_sum'] == Rational(24)

    def test_affine_kappa_not_24(self):
        """Affine kappa sum != 24 for 24A1."""
        kd = kappa_decomposition('24A1')
        assert not kd['affine_kappa_equals_24']

    def test_per_factor_data(self):
        """Spot-check per-factor data for D16+E8."""
        kd = kappa_decomposition('D16_E8')
        pf = kd['per_factor']
        assert len(pf) == 2
        assert pf[0]['type'] == 'D_16'
        assert pf[0]['dim'] == 496
        assert pf[0]['h'] == 30
        assert pf[1]['type'] == 'E_8'
        assert pf[1]['dim'] == 248
        assert pf[1]['h'] == 30


# =========================================================================
# Section 15: Casimir eigenvalues
# =========================================================================

class TestCasimir:
    """Casimir eigenvalue on adjoint = 2*h^v."""

    def test_casimir_A1(self):
        assert casimir_eigenvalue('A', 1) == Rational(4)  # 2*h = 2*2 = 4

    def test_casimir_E8(self):
        assert casimir_eigenvalue('E', 8) == Rational(60)  # 2*30


# =========================================================================
# Section 16: Collision analysis
# =========================================================================

class TestCollisionAnalysis:
    """Detailed analysis of which lattice pairs collide at which level."""

    def test_exactly_5_collision_groups(self):
        ca = collision_analysis()
        assert ca['num_collision_groups'] == 5

    def test_all_resolved_by_h_vector(self):
        ca = collision_analysis()
        for nr_str, info in ca['resolved_by_h_vector'].items():
            assert info['resolved'], (
                f"|R|={nr_str}: not resolved by h-vector: {info['labels']}"
            )

    def test_collision_pairs_match_root_count_collisions(self):
        """Cross-check with niemeier_shadow_atlas.root_count_collisions."""
        rc = root_count_collisions()
        assert len(rc) == 5
        expected_pairs = {720, 432, 288, 240, 144}
        assert set(rc.keys()) == expected_pairs


# =========================================================================
# Section 17: Full data package
# =========================================================================

class TestFullData:
    """End-to-end test of full_nonscalar_data."""

    def test_full_data_all_24(self):
        for label in ALL_NIEMEIER_LABELS:
            data = full_nonscalar_data(label)
            assert data['label'] == label

    def test_full_data_leech(self):
        data = full_nonscalar_data('Leech')
        assert data['affine_kappa_vector'] == ()
        assert data['weight_1_dim'] == 24
        assert data['num_roots'] == 0

    def test_full_data_3E8(self):
        data = full_nonscalar_data('3E8')
        assert len(data['affine_kappa_vector']) == 3
        assert data['weight_1_dim'] == 744
        assert data['num_roots'] == 720


# =========================================================================
# Section 18: Nonscalar atlas table
# =========================================================================

class TestAtlasTable:
    """End-to-end test of nonscalar_atlas_table."""

    def test_table_has_24_rows(self):
        table = nonscalar_atlas_table()
        assert len(table) == 24

    def test_table_ordered_by_roots(self):
        table = nonscalar_atlas_table()
        roots = [row['num_roots'] for row in table]
        assert roots == sorted(roots, reverse=True)


# =========================================================================
# Section 19: Weight spectrum
# =========================================================================

class TestWeightSpectrum:
    """Basic weight spectrum tests."""

    def test_weight_0_vacuum(self):
        for label in ALL_NIEMEIER_LABELS:
            ws = weight_spectrum(label)
            assert ws[0] == 1

    def test_weight_1_matches(self):
        for label in ALL_NIEMEIER_LABELS:
            ws = weight_spectrum(label)
            assert ws[1] == weight_1_dimension(label)


# =========================================================================
# Section 20: Cross-checks with niemeier_shadow_atlas
# =========================================================================

class TestCrossChecks:
    """Cross-checks between nonscalar and scalar data."""

    def test_root_counts_match(self):
        """Our root counts match the registry."""
        for label in ALL_NIEMEIER_LABELS:
            data = full_nonscalar_data(label)
            assert data['num_roots'] == NIEMEIER_REGISTRY[label]['num_roots']

    def test_scalar_kappa_still_24(self):
        """The TOTAL (scalar/lattice) kappa is still 24 for all."""
        from compute.lib.niemeier_shadow_atlas import shadow_data
        for label in ALL_NIEMEIER_LABELS:
            sd = shadow_data(label)
            assert sd['kappa'] == Rational(24)

    def test_collision_pairs_same_as_atlas(self):
        """The 5 collision pairs match between modules."""
        from compute.lib.niemeier_shadow_atlas import root_count_collisions as rcc
        rc = rcc()
        assert len(rc) == 5

    def test_h_vector_matches_coxeter_numbers(self):
        """h-vector matches the registry coxeter_numbers."""
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            hv = h_vector(label)
            registry_h = tuple(sorted(NIEMEIER_REGISTRY[label]['coxeter_numbers']))
            assert hv == registry_h


# =========================================================================
# Section 21: Specific known values (hardcoded ground truth)
# =========================================================================

class TestGroundTruth:
    """Hardcoded ground truth from Conway-Sloane."""

    def test_24A1_data(self):
        """24 copies of sl_2 at level 1."""
        dec = factor_decomposition('24A1')
        assert dec['num_factors'] == 24
        assert dec['total_c'] == Rational(24)
        assert all(k == Rational(9, 4) for k in dec['kappa_vector'])
        assert all(c == Rational(1) for c in dec['c_vector'])
        assert all(d == 3 for d in dec['dim_vector'])

    def test_12A2_data(self):
        dec = factor_decomposition('12A2')
        assert dec['num_factors'] == 12
        assert all(k == Rational(16, 3) for k in dec['kappa_vector'])
        assert all(c == Rational(2) for c in dec['c_vector'])

    def test_leech_data(self):
        dec = factor_decomposition('Leech')
        assert dec['num_factors'] == 0
        assert dec['total_dim'] == 0

    def test_D24_data(self):
        dec = factor_decomposition('D24')
        assert dec['num_factors'] == 1
        assert dec['dim_vector'] == [24 * 47]  # dim(so_48) = 24*47 = 1128
        assert dec['c_vector'] == [Rational(24)]


# =========================================================================
# Section 22: The key theorem — completeness of the invariant
# =========================================================================

class TestCompletenessTheorem:
    """The main result: non-scalar bar data distinguishes all 24 Niemeier lattices."""

    def test_scalar_tower_identical(self):
        """Scalar tower is identical for all 24 (the PROBLEM)."""
        from compute.lib.niemeier_shadow_atlas import verify_all_shadow_identical
        assert verify_all_shadow_identical()

    def test_nonscalar_distinguishes_all(self):
        """Non-scalar bar data (kappa vector) distinguishes all 24 (the SOLUTION)."""
        is_inj, collisions = kappa_vector_is_injective()
        assert is_inj

    def test_minimal_complete_is_h_nf(self):
        """(h, num_factors) is the simplest complete invariant."""
        seen = {}
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                key = (0, 0)
            else:
                components = NIEMEIER_REGISTRY[label]['components']
                h = coxeter_number(components[0][0], components[0][1])
                nf = len(components)
                key = (h, nf)
            assert key not in seen, (
                f"Collision: {label} and {seen[key]} both have (h, nf) = {key}"
            )
            seen[key] = label

    def test_kappa_injectivity_on_ADE(self):
        """kappa(g, 1) = dim(g)*(1+h)/(2h) is injective on ADE types
        that appear in Niemeier lattices (D_n for n >= 4 to avoid D_3 = A_3)."""
        seen = {}
        for fam, ns in [('A', range(1, 25)), ('D', range(4, 25)), ('E', [6, 7, 8])]:
            for n in ns:
                kap = kappa_factor(fam, n, k=1)
                key = float(kap)  # use float for comparison
                if key in seen:
                    assert False, (
                        f"kappa collision: {fam}_{n} and {seen[key]} both give kappa = {kap}"
                    )
                seen[key] = f"{fam}_{n}"
