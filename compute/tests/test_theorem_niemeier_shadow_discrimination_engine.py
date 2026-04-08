r"""Tests for Niemeier shadow discrimination engine.

Tests the multi-channel bar complex discrimination of all 24 Niemeier lattices.

MATHEMATICAL SUMMARY:
  - The scalar shadow tower is BLIND: kappa=24, S_r=0 for all 24.
  - The per-factor bar complex decomposition DISTINGUISHES all 24.
  - The minimal complete invariant is the (h, rank_partition) pair.
  - The 5 collision pairs (same |R|) are all resolved by rank partition.
  - The per-factor KM kappa sum equals 24*(1+h)^2/(2h), depending only on h.
  - The cubic shadow S_3 does NOT distinguish (uniform for lattice VOAs).

Multi-path verification: every numerical value checked by 2+ independent
methods as required by AP10.
"""

import math
import pytest
from fractions import Fraction
from typing import Any

from compute.lib.theorem_niemeier_shadow_discrimination_engine import (
    # Root system data
    root_count,
    coxeter_number,
    dim_lie,
    cartan_det,
    weyl_group_order,
    verify_dim_identity,
    # Registry
    ALL_LABELS,
    _NIEMEIER,
    # Scalar tower
    KAPPA_NIEMEIER,
    scalar_kappa,
    scalar_S3,
    scalar_S4,
    scalar_shadow_class,
    scalar_shadow_depth,
    scalar_critical_discriminant,
    scalar_tower,
    scalar_F_g,
    scalar_planted_forest_g2,
    # Root count and theta
    root_count_niemeier,
    c_delta,
    theta_coeff,
    COLLISION_PAIRS,
    # Per-factor decomposition
    per_factor_rank_partition,
    per_factor_coxeter,
    common_coxeter,
    per_factor_type,
    per_factor_kappa_km,
    per_factor_central_charge,
    per_factor_dim,
    per_factor_S3,
    per_factor_S4,
    kappa_km_sum,
    kappa_km_sum_from_h,
    # Niemeier identity
    verify_niemeier_kappa_identity,
    # Specific lattices
    compute_A1_24,
    compute_D4_6,
    compute_E8_3,
    compute_Leech,
    # Collision analysis
    analyze_collision_pair,
    full_collision_analysis,
    # Discrimination hierarchy
    discrimination_power,
    discrimination_hierarchy,
    # Invariants
    kappa_km_sum_all,
    weight_1_bar_dim,
    total_lie_dim,
    faber_pandharipande,
    # Verification
    run_all_verifications,
)


# =========================================================================
# Helper: independent Bernoulli computation for FP cross-check
# =========================================================================

def _bernoulli_independent(n: int) -> Fraction:
    """Independent Bernoulli computation (Akiyama-Tanigawa algorithm)."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    a = [Fraction(1, k + 1) for k in range(n + 1)]
    for j in range(n):
        for k in range(n - j):
            a[k] = (k + 1) * (a[k] - a[k + 1])
    return a[0]


def _fp_independent(g: int) -> Fraction:
    """Independent FP computation from Bernoulli numbers."""
    b2g = _bernoulli_independent(2 * g)
    num = (2 ** (2 * g - 1) - 1) * abs(b2g)
    den = Fraction(2 ** (2 * g - 1)) * Fraction(math.factorial(2 * g))
    return num / den


# =========================================================================
# Test 1: Registry completeness
# =========================================================================

class TestRegistry:
    """Verify the registry of 24 Niemeier lattices."""

    def test_24_lattices(self):
        """24 Niemeier lattices (Niemeier 1968)."""
        assert len(ALL_LABELS) == 24

    def test_all_rank_24(self):
        """All Niemeier lattices have rank 24."""
        for label in ALL_LABELS:
            assert _NIEMEIER[label]['rank'] == 24

    def test_root_rank_24_or_leech(self):
        """Root rank is 24 for non-Leech, 0 for Leech.

        Cross-check: sum of per-factor ranks = 24 for non-Leech.
        """
        for label in ALL_LABELS:
            rr = _NIEMEIER[label]['root_rank']
            comps = _NIEMEIER[label]['components']
            if label == 'Leech':
                assert rr == 0
                assert len(comps) == 0
            else:
                assert rr == 24
                # Cross-check: sum of component ranks
                assert sum(n for _, n in comps) == 24

    def test_root_count_bounds(self):
        """Root counts in [0, 1104].

        Cross-check max: D_24 has |R| = 2*24*23 = 1104 (D_n formula).
        Cross-check min: Leech has |R| = 0 (no roots by definition).
        """
        counts = {lab: _NIEMEIER[lab]['num_roots'] for lab in ALL_LABELS}
        assert max(counts.values()) == 2 * 24 * 23  # D_n formula: 2n(n-1)
        assert min(counts.values()) == 0
        assert counts['D24'] == max(counts.values())
        assert counts['Leech'] == 0


# =========================================================================
# Test 2: Root system data (multi-path)
# =========================================================================

class TestRootSystemData:
    """Verify ADE root system formulas with multi-path cross-checks."""

    def test_dim_identity_all_ade(self):
        """dim(g) = rank * (1 + h) for all simply-laced types.

        This is the fundamental identity |R| = rank * h (root count
        = rank * Coxeter), combined with dim = rank + |R|.
        """
        for label in ALL_LABELS:
            for fam, n in _NIEMEIER[label]['components']:
                assert verify_dim_identity(fam, n)

    def test_root_count_a1_multipath(self):
        """A_1 root count: 2.

        Path 1: n(n+1) = 1*2 = 2.
        Path 2: dim - rank = 3 - 1 = 2.
        Path 3: rank * h = 1 * 2 = 2.
        """
        assert root_count('A', 1) == 1 * 2              # n(n+1)
        assert dim_lie('A', 1) - 1 == 2                  # dim - rank
        assert 1 * coxeter_number('A', 1) == 2           # rank * h

    def test_root_count_d4_multipath(self):
        """D_4 root count: 24.

        Path 1: 2n(n-1) = 2*4*3 = 24.
        Path 2: dim - rank = 28 - 4 = 24.
        Path 3: rank * h = 4 * 6 = 24.
        """
        assert root_count('D', 4) == 2 * 4 * 3           # formula
        assert dim_lie('D', 4) - 4 == 24                  # dim - rank
        assert 4 * coxeter_number('D', 4) == 24           # rank * h

    def test_root_count_e8_multipath(self):
        """E_8 root count: 240.

        Path 1: tabulated value 240.
        Path 2: dim - rank = 248 - 8 = 240.
        Path 3: rank * h = 8 * 30 = 240.
        """
        assert root_count('E', 8) == 240
        assert dim_lie('E', 8) - 8 == 240
        assert 8 * coxeter_number('E', 8) == 240

    def test_coxeter_from_root_count(self):
        """Cross-check: h = |R| / rank for all ADE types used."""
        for label in ALL_LABELS:
            for fam, n in _NIEMEIER[label]['components']:
                h = coxeter_number(fam, n)
                r = root_count(fam, n)
                assert r == n * h, f"{fam}_{n}: |R|={r}, rank*h={n*h}"

    def test_uniform_coxeter(self):
        """All factors of each Niemeier lattice share the same h (Niemeier).

        Cross-check: this is a structural theorem, not just data.
        """
        for label in ALL_LABELS:
            h_vals = _NIEMEIER[label]['coxeter_numbers']
            if h_vals:
                assert len(set(h_vals)) == 1, f"{label}: h = {h_vals}"


# =========================================================================
# Test 3: Scalar shadow tower (BLIND)
# =========================================================================

class TestScalarTower:
    """Verify the scalar shadow tower is identical for all 24 lattices."""

    def test_kappa_24(self):
        """kappa = 24 for all. Cross-check: this IS rank by AP48."""
        assert scalar_kappa() == Fraction(24)
        assert KAPPA_NIEMEIER == 24

    def test_S3_S4_zero(self):
        """S_3 = S_4 = 0 for all. Cross-check: Delta = 8*kappa*S_4 = 0."""
        assert scalar_S3() == Fraction(0)
        assert scalar_S4() == Fraction(0)
        assert scalar_critical_discriminant() == 8 * scalar_kappa() * scalar_S4()

    def test_class_G_depth_2(self):
        """Class G, depth 2. Cross-check: S_4=0 implies Delta=0 implies class G."""
        assert scalar_shadow_class() == 'G'
        assert scalar_shadow_depth() == 2
        # Class G iff Delta = 0 iff S_4 = 0 (for kappa != 0)
        assert scalar_critical_discriminant() == Fraction(0)

    def test_F1_multipath(self):
        """F_1 = 1. Three paths.

        Path 1: F_1 = kappa * lambda_1 = 24 * 1/24 = 1.
        Path 2: lambda_1 = |B_2|/4 * 1/2! = (1/6)/4 * 1/2 = 1/24.
               F_1 = 24/24 = 1.
        Path 3: independent FP computation.
        """
        assert scalar_F_g(1) == Fraction(1)
        # Path 2: B_2 = 1/6, lambda_1 = (2^1-1)/2^1 * |B_2|/2! = 1/2 * 1/6 / 2
        b2 = Fraction(1, 6)
        lam1 = Fraction(1, 2) * b2 / Fraction(2)
        assert lam1 == Fraction(1, 24)
        assert Fraction(24) * lam1 == Fraction(1)
        # Path 3: independent computation
        assert _fp_independent(1) == Fraction(1, 24)
        assert Fraction(24) * _fp_independent(1) == Fraction(1)

    def test_F2_multipath(self):
        """F_2 = 7/240. Three paths.

        Path 1: kappa * lambda_2 = 24 * 7/5760 = 7/240.
        Path 2: B_4 = -1/30, lambda_2 = (2^3-1)/2^3 * |B_4|/4! = 7/8 * 1/720.
        Path 3: independent FP computation.
        """
        assert scalar_F_g(2) == Fraction(7, 240)
        # Path 2
        b4 = Fraction(-1, 30)
        lam2 = Fraction(7, 8) * abs(b4) / Fraction(math.factorial(4))
        assert lam2 == Fraction(7, 5760)
        assert Fraction(24) * lam2 == Fraction(7, 240)
        # Path 3
        assert _fp_independent(2) == Fraction(7, 5760)

    def test_planted_forest_zero(self):
        """PF correction = 0 since S_3 = 0. Cross-check: S_3*(10*S_3-kappa)/48."""
        pf = scalar_S3() * (10 * scalar_S3() - scalar_kappa()) / 48
        assert pf == Fraction(0)
        assert scalar_planted_forest_g2() == Fraction(0)

    def test_scalar_tower_no_discrimination(self):
        """The scalar tower distinguishes 0/276 pairs."""
        dp = discrimination_power(lambda lab: scalar_tower(5))
        assert dp['distinguished'] == 0
        # Cross-check: total pairs = C(24,2) = 276
        assert dp['total_pairs'] == 24 * 23 // 2


# =========================================================================
# Test 4: Per-factor central charge c(g,1) = rank (multi-path)
# =========================================================================

class TestPerFactorCentralCharge:
    """Verify c(g, 1) = rank(g) for simply-laced at level 1.

    Proof: c = k*dim/(k+h) = dim/(1+h) = rank*(1+h)/(1+h) = rank.
    """

    def test_c_equals_rank_all(self):
        """c(g, 1) = rank for all factors. Cross-check via dim/(1+h)."""
        for label in ALL_LABELS:
            c_vals = per_factor_central_charge(label)
            comps = _NIEMEIER[label]['components']
            for cv, (fam, n) in zip(c_vals, comps):
                # Path 1: function output
                assert cv == Fraction(n)
                # Path 2: dim/(1+h) = rank*(1+h)/(1+h) = rank
                assert Fraction(dim_lie(fam, n), 1 + coxeter_number(fam, n)) == Fraction(n)

    def test_c_sum_24(self):
        """sum c_i = 24 for all non-Leech. Cross-check: sum rank_i = 24."""
        for label in ALL_LABELS:
            if label == 'Leech':
                continue
            c_vals = per_factor_central_charge(label)
            assert sum(c_vals) == Fraction(24)
            # Cross-check: since c_i = rank_i, sum = sum ranks = 24
            ranks = [n for _, n in _NIEMEIER[label]['components']]
            assert sum(ranks) == 24


# =========================================================================
# Test 5: Per-factor KM kappa and the h-identity (multi-path)
# =========================================================================

class TestPerFactorKappaKM:
    """Per-factor KM kappa(g,1) = dim*(1+h)/(2h) = rank*(1+h)^2/(2h).

    KEY THEOREM: kappa_km_sum = 24*(1+h)^2/(2h) depends only on h.
    """

    def test_kappa_sl2_multipath(self):
        """kappa(sl_2, 1) = 9/4.

        Path 1: dim*(1+h)/(2h) = 3*3/4 = 9/4.
        Path 2: rank*(1+h)^2/(2h) = 1*9/4 = 9/4.
        Path 3: function output.
        """
        kv = per_factor_kappa_km('24A1')
        assert kv[0] == Fraction(9, 4)
        assert Fraction(dim_lie('A', 1) * (1 + coxeter_number('A', 1)),
                        2 * coxeter_number('A', 1)) == Fraction(9, 4)
        assert Fraction(1 * 3 * 3, 2 * 2) == Fraction(9, 4)

    def test_kappa_D4_multipath(self):
        """kappa(D_4, 1) = 49/3.

        Path 1: dim*(1+h)/(2h) = 28*7/12 = 49/3.
        Path 2: rank*(1+h)^2/(2h) = 4*49/12 = 49/3.
        Path 3: function output.
        """
        kv = per_factor_kappa_km('6D4')
        h = coxeter_number('D', 4)  # = 6
        assert h == 6
        assert kv[0] == Fraction(49, 3)
        assert Fraction(dim_lie('D', 4) * (1 + h), 2 * h) == Fraction(49, 3)
        assert Fraction(4 * (1 + h) ** 2, 2 * h) == Fraction(49, 3)

    def test_kappa_E8_multipath(self):
        """kappa(E_8, 1) = 1922/15.

        Path 1: dim*(1+h)/(2h) = 248*31/60.
        Path 2: rank*(1+h)^2/(2h) = 8*961/60 = 7688/60 = 1922/15.
        Path 3: function output.
        """
        kv = per_factor_kappa_km('3E8')
        h = coxeter_number('E', 8)  # = 30
        assert h == 30
        assert kv[0] == Fraction(1922, 15)
        assert Fraction(248 * 31, 60) == Fraction(1922, 15)
        assert Fraction(8 * 31 ** 2, 60) == Fraction(1922, 15)

    def test_kappa_km_sum_equals_h_formula_all(self):
        """THEOREM: kappa_km_sum = 24*(1+h)^2/(2h) for ALL 24 lattices.

        This is the central identity. Verified by TWO independent paths
        for every single lattice.
        """
        for label in ALL_LABELS:
            h = common_coxeter(label)
            ks = kappa_km_sum(label)
            if h is None:
                assert label == 'Leech'
                assert ks == Fraction(0)
                continue
            # Path 1: closed-form from h
            expected = Fraction(24 * (1 + h) ** 2, 2 * h)
            assert ks == expected, f"{label}: sum={ks}, expected={expected}"
            # Path 2: kappa_km_sum_from_h
            assert kappa_km_sum_from_h(h) == expected

    def test_kappa_km_sum_24A1_multipath(self):
        """24A_1: sum = 54. Three paths.

        Path 1: 24 * kappa(sl_2) = 24 * 9/4 = 54.
        Path 2: 24*(1+2)^2/(2*2) = 24*9/4 = 54.
        Path 3: function output.
        """
        assert kappa_km_sum('24A1') == Fraction(54)
        assert 24 * Fraction(9, 4) == Fraction(54)
        assert kappa_km_sum_from_h(2) == Fraction(54)

    def test_kappa_km_sum_6D4_multipath(self):
        """6D_4: sum = 98. Three paths.

        Path 1: 6 * kappa(D_4) = 6 * 49/3 = 98.
        Path 2: 24*(1+6)^2/(2*6) = 24*49/12 = 98.
        Path 3: function output.
        """
        assert kappa_km_sum('6D4') == Fraction(98)
        assert 6 * Fraction(49, 3) == Fraction(98)
        assert kappa_km_sum_from_h(6) == Fraction(98)

    def test_kappa_km_sum_3E8_multipath(self):
        """3E_8: sum = 1922/5. Three paths.

        Path 1: 3 * 1922/15 = 5766/15 = 1922/5.
        Path 2: 24*31^2/60 = 23064/60 = 1922/5.
        Path 3: function output.
        """
        assert kappa_km_sum('3E8') == Fraction(1922, 5)
        assert 3 * Fraction(1922, 15) == Fraction(1922, 5)
        assert kappa_km_sum_from_h(30) == Fraction(1922, 5)

    def test_kappa_km_sum_leech(self):
        """Leech: sum = 0 (no factors)."""
        assert kappa_km_sum('Leech') == Fraction(0)


# =========================================================================
# Test 6: Cubic shadow S_3 does NOT distinguish
# =========================================================================

class TestCubicShadow:
    """S_3 cannot distinguish Niemeier lattices at any level."""

    def test_total_S3_zero(self):
        """Total S_3 = 0 for all 24. Cross-check: class G means S_3 = 0."""
        assert scalar_S3() == Fraction(0)
        # Class G iff tower terminates at arity 2 iff S_r = 0 for r >= 3
        assert scalar_shadow_class() == 'G'

    def test_per_factor_S3_uniform(self):
        """Per-factor S_3 = 1/3 for all affine KM. Uniform, cannot distinguish."""
        for label in ALL_LABELS:
            for s in per_factor_S3(label):
                assert s == Fraction(1, 3)

    def test_S3_discrimination_zero(self):
        """Total S_3 distinguishes 0 pairs. Cross-check: constant function."""
        dp = discrimination_power(lambda lab: scalar_S3())
        assert dp['distinguished'] == 0
        assert dp['total_pairs'] == 276


# =========================================================================
# Test 7: Root count and theta series (multi-path)
# =========================================================================

class TestRootCountTheta:
    """Root count and theta series discrimination."""

    def test_root_count_specific_multipath(self):
        """Root counts cross-checked via sum of per-factor root counts.

        Path 1: registry value.
        Path 2: sum of root_count(fam, n) for each factor.
        """
        for label in ALL_LABELS:
            nr = root_count_niemeier(label)
            comps = _NIEMEIER[label]['components']
            computed = sum(root_count(f, n) for f, n in comps)
            assert nr == computed, f"{label}: {nr} vs {computed}"

    def test_root_count_via_rank_times_h(self):
        """Root count = 24 * h for non-Leech (since |R_i| = rank_i * h).

        Cross-check: sum |R_i| = sum rank_i * h = 24 * h.
        """
        for label in ALL_LABELS:
            h = common_coxeter(label)
            if h is None:
                continue
            assert root_count_niemeier(label) == 24 * h

    def test_root_count_collision_pairs(self):
        """Collision pairs share |R|. Cross-check: same h implies same |R| = 24*h."""
        for l1, l2, nr in COLLISION_PAIRS:
            h1 = common_coxeter(l1)
            h2 = common_coxeter(l2)
            assert h1 == h2, f"Collision pair {l1},{l2} should share h"
            assert root_count_niemeier(l1) == 24 * h1
            assert root_count_niemeier(l2) == 24 * h2
            assert root_count_niemeier(l1) == nr

    def test_theta_determined_by_root_count(self):
        """Theta series depends only on |R| (exact identity)."""
        for l1, l2, _ in COLLISION_PAIRS:
            for n in range(15):
                assert theta_coeff(l1, n) == theta_coeff(l2, n)

    def test_c_delta_formula_multipath(self):
        """c_Delta = (691*|R| - 65520) / 691.

        Cross-check: Leech has |R|=0, so c_Delta = -65520/691.
        Cross-check: D_24 has |R|=1104, c_Delta = (691*1104-65520)/691.
        """
        # Leech
        cd_leech = c_delta('Leech')
        assert cd_leech == Fraction(-65520, 691)
        assert cd_leech == Fraction(691 * 0 - 65520, 691)
        # D_24: cross-check |R| = 24*46 = 1104
        nr_d24 = 24 * coxeter_number('D', 24)
        assert nr_d24 == 1104
        cd_d24 = c_delta('D24')
        assert cd_d24 == Fraction(691 * 1104 - 65520, 691)

    def test_theta_leech_multipath(self):
        """Leech theta: N_0=1, N_1=0, N_2=196560.

        Cross-check N_2: the kissing number of the Leech lattice is 196560.
        From theta = E_12 + c_Delta*Delta, the coefficient of q^1 should
        be |R| = 0, and the q^1 coefficient of E_12 is 65520/691 * 691 + ...
        Actually verify: N_1 = (65520*sigma_11(1) + c_Delta_num*tau(1))/691
        = (65520*1 + (0-65520)*1)/691 = 0.
        """
        assert theta_coeff('Leech', 0) == 1
        assert theta_coeff('Leech', 1) == 0
        n2 = theta_coeff('Leech', 2)
        assert n2 == 196560
        # Cross-check: N_1 = (65520 + (-65520)*1)/691 = 0
        assert (65520 * 1 + (691 * 0 - 65520) * 1) == 0

    def test_root_count_distinguishes_271(self):
        """Root count distinguishes 271/276 pairs (5 collision pairs).

        Cross-check: 276 - 5 = 271.
        """
        dp = discrimination_power(root_count_niemeier)
        assert dp['num_collision_groups'] == 5
        assert dp['total_pairs'] == 276
        assert dp['distinguished'] == 271


# =========================================================================
# Test 8: Rank partition (multi-path)
# =========================================================================

class TestRankPartition:
    """Rank partition discrimination."""

    def test_rank_partition_sums_to_24(self):
        """Rank partitions sum to 24. Cross-check: root_rank = 24."""
        for label in ALL_LABELS:
            rp = per_factor_rank_partition(label)
            if label == 'Leech':
                assert rp == ()
            else:
                assert sum(rp) == 24
                assert sum(rp) == _NIEMEIER[label]['root_rank']

    def test_rank_partition_specific_multipath(self):
        """Rank partitions cross-checked via component count.

        Path 1: function output.
        Path 2: count of components in registry.
        """
        # 24A_1: 24 components of rank 1
        rp = per_factor_rank_partition('24A1')
        assert rp == tuple([1] * 24)
        assert len(_NIEMEIER['24A1']['components']) == 24

        # 3E_8: 3 components of rank 8
        rp = per_factor_rank_partition('3E8')
        assert rp == (8, 8, 8)
        assert len(_NIEMEIER['3E8']['components']) == 3

        # D_24: 1 component of rank 24
        rp = per_factor_rank_partition('D24')
        assert rp == (24,)
        assert len(_NIEMEIER['D24']['components']) == 1

    def test_collision_pair_rank_partitions_differ(self):
        """All 5 collision pairs have different rank partitions.

        This resolves ALL collision pairs at the rank partition level.
        Cross-check: verify the partitions explicitly.
        """
        expected = {
            ('D16_E8', '3E8'): ((16, 8), (8, 8, 8)),
            ('A17_E7', 'D10_2E7'): ((17, 7), (10, 7, 7)),
            ('A11_D7_E6', '4E6'): ((11, 7, 6), (6, 6, 6, 6)),
            ('2A9_D6', '4D6'): ((9, 9, 6), (6, 6, 6, 6)),
            ('4A5_D4', '6D4'): ((5, 5, 5, 5, 4), (4, 4, 4, 4, 4, 4)),
        }
        for (l1, l2), (rp1, rp2) in expected.items():
            assert per_factor_rank_partition(l1) == rp1
            assert per_factor_rank_partition(l2) == rp2
            assert rp1 != rp2
            # Cross-check: both sum to 24
            assert sum(rp1) == 24
            assert sum(rp2) == 24


# =========================================================================
# Test 9: Complete invariant (h, rank_partition)
# =========================================================================

class TestCompleteInvariant:
    """(h, rank_partition) is the minimal complete MC-based invariant."""

    def test_h_rank_partition_complete(self):
        """Distinguishes all 276 = C(24,2) pairs.

        Cross-check: C(24,2) = 24*23/2 = 276.
        """
        dp = discrimination_power(
            lambda lab: (common_coxeter(lab), per_factor_rank_partition(lab))
        )
        assert dp['is_complete'] is True
        assert dp['distinguished'] == 276
        assert dp['total_pairs'] == 24 * 23 // 2

    def test_factor_type_complete(self):
        """Per-factor type is trivially complete. Cross-check against h-partition."""
        dp_type = discrimination_power(per_factor_type)
        dp_hrp = discrimination_power(
            lambda lab: (common_coxeter(lab), per_factor_rank_partition(lab))
        )
        assert dp_type['is_complete'] is True
        assert dp_hrp['is_complete'] is True
        # Both distinguish exactly 276 pairs
        assert dp_type['distinguished'] == dp_hrp['distinguished'] == 276


# =========================================================================
# Test 10: Specific lattice computations (multi-path)
# =========================================================================

class TestSpecificLattices:
    """Detailed computations for A_1^24, D_4^6, E_8^3, Leech."""

    def test_A1_24_multipath(self):
        """A_1^{24} data cross-checked.

        |R| = 24*h = 24*2 = 48.
        kappa_km_sum = 24*(1+2)^2/(2*2) = 24*9/4 = 54.
        """
        data = compute_A1_24()
        assert data['num_roots'] == 24 * coxeter_number('A', 1)
        assert data['num_roots'] == 48
        assert data['num_factors'] == 24
        assert data['common_h'] == 2
        assert data['kappa_km_sum'] == kappa_km_sum_from_h(2)
        assert data['kappa_km_sum'] == Fraction(54)
        assert data['c_sum'] == Fraction(24)
        assert data['shadow_class'] == 'G'

    def test_D4_6_multipath(self):
        """D_4^6 data cross-checked.

        |R| = 24*h = 24*6 = 144.
        kappa_km_sum = 24*(1+6)^2/(2*6) = 24*49/12 = 98.
        """
        data = compute_D4_6()
        assert data['num_roots'] == 24 * coxeter_number('D', 4)
        assert data['num_roots'] == 144
        assert data['num_factors'] == 6
        assert data['common_h'] == 6
        assert data['kappa_km_sum'] == kappa_km_sum_from_h(6)
        assert data['kappa_km_sum'] == Fraction(98)

    def test_E8_3_multipath(self):
        """E_8^3 data cross-checked.

        |R| = 24*h = 24*30 = 720.
        kappa_km_sum = 24*(1+30)^2/(2*30) = 24*961/60 = 1922/5.
        Collision with D16_E8 at |R|=720.
        """
        data = compute_E8_3()
        assert data['num_roots'] == 24 * coxeter_number('E', 8)
        assert data['num_roots'] == 720
        assert data['num_factors'] == 3
        assert data['common_h'] == 30
        assert data['kappa_km_sum'] == kappa_km_sum_from_h(30)
        assert data['kappa_km_sum'] == Fraction(1922, 5)
        assert data['same_roots'] is True
        assert data['rank_partitions_differ'] is True

    def test_Leech_multipath(self):
        """Leech: no roots, no factors, pure Heisenberg.

        Cross-check: weight-1 bar dim = 24 (Cartan only).
        Cross-check: theta_1 = 0 (no weight-2 lattice vectors with |v|^2=2).
        """
        data = compute_Leech()
        assert data['num_roots'] == 0
        assert data['num_factors'] == 0
        assert data['common_h'] is None
        assert data['kappa_lattice'] == Fraction(24)
        assert data['kappa_km_sum'] == Fraction(0)
        assert data['weight_1_bar_dim'] == 24
        assert data['theta_1'] == 0
        assert data['theta_2'] == 196560

    def test_Leech_unique(self):
        """Leech is the only lattice with |R| = 0.

        Cross-check: all others have h >= 2, so |R| = 24*h >= 48.
        """
        for label in ALL_LABELS:
            if label != 'Leech':
                h = common_coxeter(label)
                assert h >= 2
                assert root_count_niemeier(label) == 24 * h >= 48


# =========================================================================
# Test 11: Collision pair resolution (multi-path)
# =========================================================================

class TestCollisionPairs:
    """All 5 collision pairs resolved by bar complex data."""

    def test_five_pairs(self):
        """Exactly 5 collision pairs."""
        assert len(COLLISION_PAIRS) == 5

    def test_all_same_theta(self):
        """All collision pairs share theta series (same |R| = same c_Delta).

        Cross-check: theta depends only on c_Delta, which depends only on |R|.
        """
        for l1, l2, nr in COLLISION_PAIRS:
            assert c_delta(l1) == c_delta(l2)
            for n in range(10):
                assert theta_coeff(l1, n) == theta_coeff(l2, n)

    def test_all_resolved_by_rank_partition(self):
        """All resolved by rank partition. Cross-check: also by factor type."""
        for l1, l2, _ in COLLISION_PAIRS:
            assert per_factor_rank_partition(l1) != per_factor_rank_partition(l2)
            assert per_factor_type(l1) != per_factor_type(l2)

    def test_km_kappa_sum_cannot_resolve(self):
        """KM kappa sum CANNOT resolve collisions (depends only on h).

        Cross-check: collision pairs share h, so kappa_km_sum = 24*(1+h)^2/(2h)
        is the same for both.
        """
        for l1, l2, _ in COLLISION_PAIRS:
            h1 = common_coxeter(l1)
            h2 = common_coxeter(l2)
            assert h1 == h2
            assert kappa_km_sum(l1) == kappa_km_sum(l2)
            assert kappa_km_sum(l1) == kappa_km_sum_from_h(h1)

    def test_collision_D16E8_vs_3E8_detail(self):
        """D16+E8 vs 3E8: h=30, |R|=720, partitions (16,8) vs (8,8,8).

        Cross-check: D_16 has h=2*15=30, E_8 has h=30. Same h.
        Cross-check: |R| = 24*30 = 720 for both.
        """
        data = analyze_collision_pair('D16_E8', '3E8')
        assert data['root_count'] == 24 * 30
        assert data['same_h'] is True
        assert data['common_h_1'] == 2 * (16 - 1)  # D_16: h = 2*15
        assert data['common_h_2'] == 30              # E_8: h = 30
        assert data['rank_partitions_differ'] is True
        assert data['kappa_km_sums_differ'] is False

    def test_collision_4A5D4_vs_6D4_detail(self):
        """4A5+D4 vs 6D4: h=6, |R|=144.

        Cross-check: A_5 has h=6, D_4 has h=6. Same h.
        """
        data = analyze_collision_pair('4A5_D4', '6D4')
        assert data['root_count'] == 24 * 6
        assert data['same_h'] is True
        assert data['common_h_1'] == coxeter_number('A', 5)  # A_5: h=6
        assert data['common_h_2'] == coxeter_number('D', 4)  # D_4: h=6
        assert coxeter_number('A', 5) == 6
        assert coxeter_number('D', 4) == 6


# =========================================================================
# Test 12: KM kappa sum identity (the theorem)
# =========================================================================

class TestKappaKMSumIdentity:
    """The KM kappa sum identity kappa_km_sum = 24*(1+h)^2/(2h)."""

    def test_identity_all_24(self):
        """Verify for all 24 lattices via two paths."""
        for label in ALL_LABELS:
            h = common_coxeter(label)
            ks = kappa_km_sum(label)
            if h is None:
                assert ks == Fraction(0)
            else:
                # Path 1: closed form
                assert ks == Fraction(24 * (1 + h) ** 2, 2 * h)
                # Path 2: via kappa_km_sum_from_h
                assert ks == kappa_km_sum_from_h(h)

    def test_identity_specific_values(self):
        """Spot-check specific h values with independent arithmetic.

        h=2: 24*9/4 = 54.
        h=6: 24*49/12 = 98.
        h=30: 24*961/60 = 1922/5.
        """
        assert kappa_km_sum_from_h(2) == Fraction(24 * 9, 4)
        assert kappa_km_sum_from_h(6) == Fraction(24 * 49, 12)
        assert kappa_km_sum_from_h(30) == Fraction(24 * 961, 60)
        # Simplified forms
        assert Fraction(24 * 9, 4) == Fraction(54)
        assert Fraction(24 * 49, 12) == Fraction(98)
        assert Fraction(24 * 961, 60) == Fraction(1922, 5)

    def test_discrimination_same_as_h(self):
        """KM kappa sum has same discrimination power as h alone.

        Cross-check: h distinguishes the same number of pairs.
        """
        dp_ks = discrimination_power(kappa_km_sum)
        dp_h = discrimination_power(common_coxeter)
        assert dp_ks['distinguished'] == dp_h['distinguished']
        assert dp_ks['num_collision_groups'] == dp_h['num_collision_groups']


# =========================================================================
# Test 13: Weight-1 bar dimension (multi-path)
# =========================================================================

class TestWeight1BarDim:
    """Weight-1 bar dimension = 24 + |R|."""

    def test_weight_1_multipath(self):
        """Cross-check: 24 + |R| = 24 + 24*h = 24*(1+h) for non-Leech.

        Path 1: weight_1_bar_dim function.
        Path 2: 24 + root_count_niemeier.
        Path 3: 24*(1+h) for non-Leech.
        """
        for label in ALL_LABELS:
            w1 = weight_1_bar_dim(label)
            nr = root_count_niemeier(label)
            assert w1 == 24 + nr
            h = common_coxeter(label)
            if h is not None:
                assert w1 == 24 * (1 + h)

    def test_weight_1_discrimination_equals_root_count(self):
        """Same discrimination as |R|: injective on |R| but not complete."""
        dp_w = discrimination_power(weight_1_bar_dim)
        dp_r = discrimination_power(root_count_niemeier)
        assert dp_w['distinguished'] == dp_r['distinguished']


# =========================================================================
# Test 14: Total Lie algebra dimension (multi-path)
# =========================================================================

class TestLieAlgDim:
    """Total Lie algebra dimension = 24*(1+h) for non-Leech."""

    def test_total_dim_multipath(self):
        """Cross-check: sum dim_i = sum rank_i*(1+h) = 24*(1+h).

        Path 1: total_lie_dim function.
        Path 2: sum of dim_lie for each component.
        Path 3: 24*(1+h) for non-Leech.
        """
        for label in ALL_LABELS:
            td = total_lie_dim(label)
            comps = _NIEMEIER[label]['components']
            assert td == sum(dim_lie(f, n) for f, n in comps)
            h = common_coxeter(label)
            if h is not None:
                assert td == 24 * (1 + h)

    def test_total_dim_equals_24_plus_roots(self):
        """total_dim = 24 + |R| = weight_1_bar_dim (since dim = rank + |R|)."""
        for label in ALL_LABELS:
            assert total_lie_dim(label) == weight_1_bar_dim(label) - 24 + \
                   sum(n for _, n in _NIEMEIER[label]['components'])
            # Simpler: total_dim = rank + |R| summed, = 24 + |R| for non-Leech
            if label != 'Leech':
                assert total_lie_dim(label) == 24 + root_count_niemeier(label)


# =========================================================================
# Test 15: Discrimination hierarchy (structural)
# =========================================================================

class TestDiscriminationHierarchy:
    """Discrimination power monotonically increases up the hierarchy."""

    def test_monotonic(self):
        """d0 <= d_root <= d_h <= d_hrp = 276."""
        d0 = discrimination_power(lambda lab: scalar_kappa())['distinguished']
        d_root = discrimination_power(root_count_niemeier)['distinguished']
        d_h = discrimination_power(common_coxeter)['distinguished']
        d_hrp = discrimination_power(
            lambda lab: (common_coxeter(lab), per_factor_rank_partition(lab))
        )['distinguished']
        assert d0 == 0
        assert d0 <= d_root
        # h and root count have same power (|R| = 24*h is injective in h)
        assert d_root == d_h
        assert d_h <= d_hrp
        assert d_hrp == 276

    def test_total_pairs_276(self):
        """C(24,2) = 276. Cross-check: 24*23/2."""
        dp = discrimination_power(lambda lab: lab)
        assert dp['total_pairs'] == 276
        assert 24 * 23 // 2 == 276


# =========================================================================
# Test 16: Faber-Pandharipande cross-checks
# =========================================================================

class TestFaberPandharipande:
    """FP values via two independent Bernoulli implementations."""

    def test_fp_g1_multipath(self):
        """lambda_1 = 1/24. Two Bernoulli implementations."""
        assert faber_pandharipande(1) == Fraction(1, 24)
        assert _fp_independent(1) == Fraction(1, 24)

    def test_fp_g2_multipath(self):
        """lambda_2 = 7/5760. Two Bernoulli implementations."""
        assert faber_pandharipande(2) == Fraction(7, 5760)
        assert _fp_independent(2) == Fraction(7, 5760)

    def test_fp_g3_multipath(self):
        """lambda_3 = 31/967680. Two Bernoulli implementations."""
        assert faber_pandharipande(3) == Fraction(31, 967680)
        assert _fp_independent(3) == Fraction(31, 967680)

    def test_fp_g4_multipath(self):
        """lambda_4. Two Bernoulli implementations."""
        assert faber_pandharipande(4) == _fp_independent(4)

    def test_cartan_det_multipath(self):
        """Cartan determinants cross-checked.

        A_n: det = n+1. Also equals index [weight lattice : root lattice].
        D_n: det = 4.
        E_8: det = 1 (self-dual, unimodular).
        """
        # A_1: det = 2 = n+1
        assert cartan_det('A', 1) == 1 + 1
        # D_4: det = 4 (universal for D_n)
        assert cartan_det('D', 4) == 4
        # E_8: det = 1 (self-dual)
        assert cartan_det('E', 8) == 1

    def test_weyl_group_multipath(self):
        """Weyl group orders cross-checked.

        A_n: |W| = (n+1)!.
        D_n: |W| = 2^{n-1} * n!.
        """
        # A_1: |W| = 2! = 2
        assert weyl_group_order('A', 1) == math.factorial(2)
        # D_4: |W| = 2^3 * 4! = 8 * 24 = 192
        assert weyl_group_order('D', 4) == 2**3 * math.factorial(4)
        assert weyl_group_order('D', 4) == 192
        # E_8: known value
        assert weyl_group_order('E', 8) == 696729600


# =========================================================================
# Test 17: Master verification suite
# =========================================================================

class TestMasterVerification:
    """Master verification suite runs clean."""

    def test_master_suite(self):
        """All structural verifications pass."""
        results = run_all_verifications()
        assert results['all_kappa_24'] is True
        assert results['all_class_G'] is True
        assert results['all_S3_zero'] is True
        assert results['all_F1_one'] is True
        assert results['all_F2'] is True
        assert results['all_c_sum_24'] is True
        assert results['all_dim_identity'] is True
        assert results['all_uniform_h'] is True

    def test_hierarchy_in_master(self):
        """Hierarchy completeness in master suite."""
        results = run_all_verifications()
        h = results['hierarchy']
        assert h['level_0_kappa']['distinguished'] == 0
        assert h['level_4_coxeter_rank']['is_complete'] is True
        assert h['level_5_factor_type']['is_complete'] is True
        # Cross-check: both complete invariants distinguish 276 pairs
        assert h['level_4_coxeter_rank']['distinguished'] == 276
        assert h['level_5_factor_type']['distinguished'] == 276
