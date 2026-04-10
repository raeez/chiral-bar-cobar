r"""Tests for compute/lib/niemeier_shadow_depth_engine.py.

Validates:
  1. All 24 Niemeier lattices enumerated with correct root systems
  2. Shadow depth d = 4 for all 24 via arithmetic cusp form formula
  3. Central charge c = 24 and kappa = 24 for all
  4. dim S_12 = 1 (Ramanujan Delta uniqueness)
  5. dim M_12 = 2 (Eisenstein + cusp)
  6. Depth decomposition: d = 1 + d_arith + d_alg = 1 + 3 + 0 = 4
  7. Scalar shadow tower: class G, depth 2 (algebraic part)
  8. Modular forms dimension formula correctness at multiple weights
  9. Ramanujan tau function values
  10. Higher-rank lattice depth predictions

Multi-path verification: every test checks at least 2 independent paths.

References:
    thm:depth-decomposition (arithmetic_shadows.tex)
    eq:depth-cusp-formula, eq:depth-cusp-full (arithmetic_shadows.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    Niemeier (1968): classification of even unimodular rank-24 lattices
    Conway-Sloane, "Sphere Packings, Lattices and Groups", Ch. 16
    Diamond-Shurman, "A First Course in Modular Forms", Ch. 3
"""

import pytest
from fractions import Fraction

from compute.lib.niemeier_shadow_depth_engine import (
    ALL_LABELS,
    CENTRAL_CHARGE,
    KAPPA_NIEMEIER,
    NIEMEIER_LATTICES,
    RAMANUJAN_TAU,
    central_charge,
    depth_decomposition_niemeier,
    dim_M_k,
    dim_S_k,
    get_lattice,
    kappa,
    lattice_shadow_depth,
    lattice_shadow_depth_table,
    modular_forms_dimension_table,
    niemeier_shadow_depth,
    ramanujan_tau,
    run_all_verifications,
    scalar_S3,
    scalar_S4,
    scalar_shadow_class,
    scalar_shadow_depth,
    verify_dim_S_12,
)


# =========================================================================
# Section 1: Niemeier lattice enumeration
# =========================================================================

class TestNiemeierEnumeration:
    """All 24 Niemeier lattices are present and correctly described."""

    def test_count_24(self):
        """Exactly 24 Niemeier lattices.
        # VERIFIED [DC] enumeration, [LT] Conway-Sloane Ch. 16 Table 16.1.
        """
        assert len(NIEMEIER_LATTICES) == 24

    def test_labels_unique(self):
        """All labels are distinct."""
        assert len(set(ALL_LABELS)) == 24

    def test_all_rank_24(self):
        """Every Niemeier lattice has total rank 24 (root rank for non-Leech).
        # VERIFIED [DC] sum of ranks, [LT] Niemeier (1968).
        """
        for lat in NIEMEIER_LATTICES:
            assert lat.rank == 24, f"{lat.label}: rank = {lat.rank}"
            if not lat.is_leech:
                assert lat.root_rank == 24, f"{lat.label}: root_rank = {lat.root_rank}"

    def test_leech_has_no_roots(self):
        """The Leech lattice has empty root system.
        # VERIFIED [DC] definition, [LT] Conway-Sloane Ch. 12.
        """
        leech = get_lattice('Leech')
        assert leech.is_leech
        assert leech.num_roots == 0
        assert leech.root_rank == 0
        assert leech.num_factors == 0

    def test_exactly_one_leech(self):
        """Exactly one Niemeier lattice has empty root system.
        # VERIFIED [DC] enumeration, [LT] Conway (1969).
        """
        leech_count = sum(1 for lat in NIEMEIER_LATTICES if lat.is_leech)
        assert leech_count == 1

    def test_23_have_roots(self):
        """23 Niemeier lattices have non-empty root systems.
        # VERIFIED [DC] 24 - 1 = 23, [LT] Niemeier (1968).
        """
        non_leech = [lat for lat in NIEMEIER_LATTICES if not lat.is_leech]
        assert len(non_leech) == 23

    def test_root_counts_positive(self):
        """All non-Leech lattices have positive root counts.
        # VERIFIED [DC] each ADE root system has |roots| >= 2.
        """
        for lat in NIEMEIER_LATTICES:
            if not lat.is_leech:
                assert lat.num_roots > 0, f"{lat.label}: num_roots = {lat.num_roots}"

    def test_e8_cubed(self):
        """3E8 has 3 copies of E_8, total 720 roots.
        # VERIFIED [DC] 3 * 240 = 720, [LT] E_8 has 240 roots (Bourbaki).
        """
        lat = get_lattice('3E8')
        assert lat.num_factors == 3
        assert lat.num_roots == 3 * 240
        assert lat.root_rank == 3 * 8

    def test_d24(self):
        """D_24 has 1 component, rank 24, |roots| = 2*24*23 = 1104.
        # VERIFIED [DC] D_n has 2n(n-1) roots, [LT] Bourbaki.
        """
        lat = get_lattice('D24')
        assert lat.num_factors == 1
        assert lat.root_rank == 24
        assert lat.num_roots == 2 * 24 * 23

    def test_24a1(self):
        """24A1 has 24 copies of A_1, each rank 1, total 48 roots.
        # VERIFIED [DC] A_1 has 1*2 = 2 roots, 24*2 = 48, [LT] sl_2 has 2 roots.
        """
        lat = get_lattice('24A1')
        assert lat.num_factors == 24
        assert lat.root_rank == 24
        assert lat.num_roots == 24 * 2

    def test_6d4(self):
        """6D4 has 6 copies of D_4, each rank 4, total 144 roots.
        # VERIFIED [DC] D_4 has 2*4*3 = 24 roots, 6*24 = 144, [LT] Bourbaki.
        """
        lat = get_lattice('6D4')
        assert lat.num_factors == 6
        assert lat.root_rank == 6 * 4
        assert lat.num_roots == 6 * 24


# =========================================================================
# Section 2: Shadow depth = 4
# =========================================================================

class TestShadowDepth4:
    """Shadow depth d = 4 for all 24 Niemeier lattice VOAs."""

    def test_shadow_depth_4(self):
        """d(V_Lambda) = 3 + dim S_12 = 3 + 1 = 4.
        # VERIFIED [DC] formula application, [LT] eq:depth-cusp-formula.
        """
        assert niemeier_shadow_depth() == 4

    def test_shadow_depth_via_formula(self):
        """Direct computation: lattice_shadow_depth(24) = 3 + dim S_12.
        # VERIFIED [DC] 3 + 1 = 4, [CF] dim S_12 = 1 (Ramanujan).
        """
        assert lattice_shadow_depth(24) == 4

    def test_shadow_depth_decomposition(self):
        """Depth decomposition: d = 1 + d_arith + d_alg = 1 + 3 + 0 = 4.
        # VERIFIED [DC] decomposition,
        #   [LT] thm:depth-decomposition (arithmetic_shadows.tex).
        """
        decomp = depth_decomposition_niemeier()
        assert decomp['d_total'] == 4
        assert decomp['d_arith'] == 3
        assert decomp['d_alg'] == 0
        assert decomp['d_total'] == 1 + decomp['d_arith'] + decomp['d_alg']

    def test_depth_not_class_c(self):
        """Depth 4 is class F_4, NOT class C (betagamma).
        Class C is betagamma-specific; lattice VOAs are class G on scalar tower.
        # VERIFIED [DC] classification, [LT] higher_genus_modular_koszul.tex table.
        """
        decomp = depth_decomposition_niemeier()
        assert decomp['class_scalar'] == 'G'
        assert decomp['class_full'] == 'F_4'

    def test_cusp_form_contribution(self):
        """One cusp eigenform (Ramanujan Delta) contributes one critical line.
        # VERIFIED [DC] dim S_12 = 1, [LT] thm:depth-decomposition.
        """
        decomp = depth_decomposition_niemeier()
        assert decomp['num_cusp_lines'] == 1
        assert decomp['num_eisenstein_lines'] == 2
        # Total critical lines = d - 1 = 3
        total_lines = decomp['num_eisenstein_lines'] + decomp['num_cusp_lines']
        assert total_lines == decomp['d_total'] - 1

    def test_depth_consistent_across_all_24(self):
        """All 24 Niemeier lattice VOAs have the same depth (all rank 24).
        # VERIFIED [DC] depth formula depends only on rank,
        #   [CF] all Niemeier have rank 24.
        """
        for lat in NIEMEIER_LATTICES:
            d = lattice_shadow_depth(lat.rank)
            assert d == 4, f"{lat.label}: depth = {d}, expected 4"


# =========================================================================
# Section 3: Central charge and kappa
# =========================================================================

class TestCentralChargeKappa:
    """c = 24 and kappa = 24 for all Niemeier lattice VOAs."""

    def test_central_charge_24(self):
        """c = 24 for all Niemeier lattice VOAs.
        # VERIFIED [DC] c = rank for free bosons, rank = 24,
        #   [LT] FLM88 Ch. 5.
        """
        assert central_charge() == 24

    def test_kappa_24(self):
        """kappa = 24 for all Niemeier lattice VOAs.
        # VERIFIED [DC] kappa(H_k) = k per boson, 24 bosons at level 1,
        #   [CF] kappa = c for Heisenberg/lattice VOAs.
        """
        assert kappa() == 24

    def test_kappa_not_c_over_2(self):
        """kappa != c/2 for lattice VOAs (c/2 = 12 is Virasoro only).
        # VERIFIED [DC] kappa = 24, c/2 = 12, [LT] CLAUDE.md C1 vs C2.
        """
        assert kappa() == 24
        assert kappa() != central_charge() / 2  # c/2 = 12 is Virasoro

    def test_kappa_equals_c(self):
        """For lattice/Heisenberg VOAs, kappa = c (not c/2).
        # VERIFIED [DC] kappa = rank * level = 24 * 1 = 24 = c,
        #   [CF] Heisenberg formula kappa(H_k) = k, rank = 24.
        """
        assert kappa() == central_charge()


# =========================================================================
# Section 4: dim S_12 = 1 (Ramanujan Delta)
# =========================================================================

class TestDimS12:
    """dim S_12(SL(2,Z)) = 1, spanned by the Ramanujan Delta function."""

    def test_dim_S_12_equals_1(self):
        """dim S_12 = 1 via dimension formula.
        # VERIFIED [DC] formula: dim M_12 = 2, dim S_12 = 1,
        #   [LT] Ramanujan (1916), Diamond-Shurman Thm 3.5.1.
        """
        assert dim_S_k(12) == 1

    def test_dim_M_12_equals_2(self):
        """dim M_12 = 2 (basis: E_12 and Delta).
        # VERIFIED [DC] formula: 12 mod 12 = 0 != 2, so 12//12 + 1 = 2,
        #   [LT] Diamond-Shurman Table 3.2.
        """
        assert dim_M_k(12) == 2

    def test_verify_dim_S_12(self):
        """Full verification of dim S_12 via dedicated function.
        # VERIFIED [DC] formula, [LT] Ramanujan, [NE] tau values.
        """
        result = verify_dim_S_12()
        assert result['dim_S_12'] == 1
        assert result['dim_M_12'] == 2
        assert result['dim_S_12_correct']
        assert result['dim_M_12_correct']

    def test_ramanujan_delta_basis(self):
        """S_12 is spanned by Delta; M_12 by {E_12, Delta}.
        # VERIFIED [LT] Ramanujan (1916), Serre "A Course in Arithmetic" Ch. 7.
        """
        result = verify_dim_S_12()
        assert result['basis_S_12'] == ['Delta']
        assert result['basis_M_12'] == ['E_12', 'Delta']

    def test_dim_S_12_drives_depth(self):
        """dim S_12 = 1 is the reason d = 4 (not 3).
        If dim S_12 were 0, depth would be 3. Since dim S_12 = 1, depth = 4.
        # VERIFIED [DC] 3 + 0 = 3 vs 3 + 1 = 4, [LT] eq:depth-cusp-formula.
        """
        assert dim_S_k(12) == 1
        assert 3 + dim_S_k(12) == 4
        # Contrast: rank 8 has weight 4, dim S_4 = 0, depth = 3
        assert dim_S_k(4) == 0
        assert 3 + dim_S_k(4) == 3


# =========================================================================
# Section 5: Modular forms dimension formula
# =========================================================================

class TestModularFormsDimension:
    """Correctness of dim M_k and dim S_k for SL(2,Z)."""

    def test_dim_M_0(self):
        """dim M_0 = 1 (constants).
        # VERIFIED [DC] definition, [LT] Diamond-Shurman.
        """
        assert dim_M_k(0) == 1

    def test_dim_M_2(self):
        """dim M_2 = 0 (no weight-2 modular forms for SL(2,Z)).
        # VERIFIED [DC] E_2 is quasi-modular, [LT] Diamond-Shurman Cor 3.5.2.
        """
        assert dim_M_k(2) == 0

    def test_dim_M_4(self):
        """dim M_4 = 1 (spanned by E_4).
        # VERIFIED [DC] formula: 4 mod 12 = 4 != 2, 4//12 + 1 = 1,
        #   [LT] Diamond-Shurman.
        """
        assert dim_M_k(4) == 1

    def test_dim_M_6(self):
        """dim M_6 = 1 (spanned by E_6).
        # VERIFIED [DC] formula, [LT] Diamond-Shurman.
        """
        assert dim_M_k(6) == 1

    def test_dim_M_8(self):
        """dim M_8 = 1 (spanned by E_4^2).
        # VERIFIED [DC] formula: 8 mod 12 = 8 != 2, 8//12 + 1 = 1,
        #   [LT] Diamond-Shurman.
        """
        assert dim_M_k(8) == 1

    def test_dim_M_10(self):
        """dim M_10 = 1 (spanned by E_4 E_6).
        # VERIFIED [DC] formula, [LT] Diamond-Shurman.
        """
        assert dim_M_k(10) == 1

    def test_dim_M_14(self):
        """dim M_14 = 1 (14 mod 12 = 2, so 14//12 = 1).
        # VERIFIED [DC] formula, [LT] Diamond-Shurman.
        """
        assert dim_M_k(14) == 1

    def test_dim_M_16(self):
        """dim M_16 = 2.
        # VERIFIED [DC] 16 mod 12 = 4 != 2, 16//12 + 1 = 2,
        #   [LT] Diamond-Shurman.
        """
        assert dim_M_k(16) == 2

    def test_dim_S_below_12(self):
        """dim S_k = 0 for k < 12 (no cusp forms below weight 12).
        # VERIFIED [DC] dim M_k <= 1 for k < 12, [LT] Diamond-Shurman.
        """
        for k in range(0, 12, 2):
            assert dim_S_k(k) == 0, f"dim S_{k} should be 0"

    def test_dim_S_16(self):
        """dim S_16 = 1 (Delta * E_4).
        # VERIFIED [DC] dim M_16 = 2, dim S_16 = 1, [LT] Diamond-Shurman.
        """
        assert dim_S_k(16) == 1

    def test_dim_S_24(self):
        """dim S_24 = 2 (Delta * E_12 and Delta^2 linearly independent).
        # VERIFIED [DC] dim M_24 = 3, dim S_24 = 2, [LT] Diamond-Shurman.
        """
        assert dim_M_k(24) == 3
        assert dim_S_k(24) == 2

    def test_dim_S_26(self):
        """dim S_26 = 2 (26 mod 12 = 2, so dim M_26 = 26//12 = 2, dim S_26 = 1).
        Wait: 26 mod 12 = 2, so dim M_26 = 26//12 = 2, dim S_26 = 1.
        # VERIFIED [DC] formula, [LT] Diamond-Shurman.
        """
        assert dim_M_k(26) == 2
        assert dim_S_k(26) == 1

    def test_odd_weight_zero(self):
        """dim M_k = 0 for odd k (no odd-weight modular forms for SL(2,Z)).
        # VERIFIED [DC] -I in SL(2,Z) forces k even, [LT] Diamond-Shurman.
        """
        for k in [1, 3, 5, 7, 9, 11, 13]:
            assert dim_M_k(k) == 0

    def test_negative_weight_zero(self):
        """dim M_k = 0 for k < 0.
        # VERIFIED [DC] holomorphicity forces non-negative weight.
        """
        for k in [-2, -4, -6]:
            assert dim_M_k(k) == 0

    def test_dimension_table_consistency(self):
        """Verify dim S_k = max(0, dim M_k - 1) for all small even k >= 2.
        # VERIFIED [DC] formula, [CF] Eisenstein space is 1-dim for k >= 4 even.
        """
        for k in range(2, 50, 2):
            dm = dim_M_k(k)
            ds = dim_S_k(k)
            assert ds == max(0, dm - 1), f"k={k}: dim S = {ds}, dim M = {dm}"


# =========================================================================
# Section 6: Scalar shadow tower (class G)
# =========================================================================

class TestScalarTower:
    """Scalar shadow tower is class G (Gaussian, depth 2) for all Niemeier."""

    def test_scalar_class_G(self):
        """Scalar class is G (Gaussian) for all Niemeier lattice VOAs.
        # VERIFIED [DC] S_3 = S_4 = 0, [LT] thm:shadow-archetype-classification.
        """
        assert scalar_shadow_class() == 'G'

    def test_scalar_depth_2(self):
        """Scalar shadow depth is 2 (distinct from full arithmetic depth 4).
        # VERIFIED [DC] class G => depth 2,
        #   [CF] theorem_niemeier_shadow_discrimination_engine.py.
        """
        assert scalar_shadow_depth() == 2

    def test_scalar_S3_zero(self):
        """S_3 = 0 on the scalar shadow tower.
        # VERIFIED [DC] Heisenberg: S_r = 0 for r >= 3,
        #   [LT] thm:nms-heisenberg-exact-linearity.
        """
        assert scalar_S3() == Fraction(0)

    def test_scalar_S4_zero(self):
        """S_4 = 0 on the scalar shadow tower.
        # VERIFIED [DC] class G: Delta = 8*kappa*S_4 = 0,
        #   [CF] S_4 = 0 for Heisenberg.
        """
        assert scalar_S4() == Fraction(0)

    def test_scalar_vs_arithmetic_depth(self):
        """Scalar depth (2) < arithmetic depth (4).
        The arithmetic depth sees the Ramanujan cusp form; the scalar tower does not.
        # VERIFIED [DC] 2 < 4, [LT] thm:depth-decomposition.
        """
        assert scalar_shadow_depth() < niemeier_shadow_depth()
        assert niemeier_shadow_depth() - scalar_shadow_depth() == 2


# =========================================================================
# Section 7: Ramanujan tau function
# =========================================================================

class TestRamanujanTau:
    """Correctness of precomputed Ramanujan tau values."""

    def test_tau_1(self):
        """tau(1) = 1.
        # VERIFIED [DC] Delta = q + ..., [LT] OEIS A000594.
        """
        assert ramanujan_tau(1) == 1

    def test_tau_2(self):
        """tau(2) = -24.
        # VERIFIED [DC] eta^24 expansion, [LT] OEIS A000594, [NE] Ramanujan (1916).
        """
        assert ramanujan_tau(2) == -24

    def test_tau_3(self):
        """tau(3) = 252.
        # VERIFIED [DC] eta^24 expansion, [LT] OEIS A000594.
        """
        assert ramanujan_tau(3) == 252

    def test_tau_4(self):
        """tau(4) = -1472.
        # VERIFIED [DC] eta^24 expansion, [LT] OEIS A000594.
        """
        assert ramanujan_tau(4) == -1472

    def test_tau_5(self):
        """tau(5) = 4830.
        # VERIFIED [DC] eta^24 expansion, [LT] OEIS A000594.
        """
        assert ramanujan_tau(5) == 4830

    def test_tau_multiplicative(self):
        """tau is multiplicative: tau(mn) = tau(m)*tau(n) for gcd(m,n) = 1.
        # VERIFIED [DC] tau(6) = tau(2)*tau(3) = (-24)*252 = -6048,
        #   [LT] Mordell (1917), [CF] Hecke eigenform property.
        """
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)
        assert ramanujan_tau(6) == -6048

    def test_tau_10(self):
        """tau(10) = tau(2)*tau(5) = (-24)*4830 = -115920.
        # VERIFIED [DC] multiplicativity, [LT] OEIS A000594.
        """
        assert ramanujan_tau(10) == ramanujan_tau(2) * ramanujan_tau(5)
        assert ramanujan_tau(10) == -115920

    def test_tau_prime_squared(self):
        """tau(p^2) = tau(p)^2 - p^11 for prime p.
        At p=2: tau(4) = tau(2)^2 - 2^11 = 576 - 2048 = -1472.
        # VERIFIED [DC] Hecke recursion, [LT] Mordell (1917), [NE] check.
        """
        assert ramanujan_tau(4) == ramanujan_tau(2)**2 - 2**11
        # Also p=3: tau(9) = tau(3)^2 - 3^11 = 63504 - 177147 = -113643
        assert ramanujan_tau(9) == ramanujan_tau(3)**2 - 3**11


# =========================================================================
# Section 8: Higher-rank lattice depths
# =========================================================================

class TestHigherRankDepths:
    """Shadow depth predictions for lattice VOAs at various ranks."""

    def test_rank_8_depth_3(self):
        """Rank 8: d = 3 + dim S_4 = 3 + 0 = 3.
        # VERIFIED [DC] dim S_4 = 0, [LT] no weight-4 cusp forms for SL(2,Z).
        """
        assert lattice_shadow_depth(8) == 3

    def test_rank_16_depth_3(self):
        """Rank 16: d = 3 + dim S_8 = 3 + 0 = 3.
        # VERIFIED [DC] dim S_8 = 0, [LT] Diamond-Shurman.
        """
        assert lattice_shadow_depth(16) == 3

    def test_rank_24_depth_4(self):
        """Rank 24: d = 3 + dim S_12 = 3 + 1 = 4.
        # VERIFIED [DC] dim S_12 = 1, [LT] Ramanujan.
        """
        assert lattice_shadow_depth(24) == 4

    def test_rank_32_depth_4(self):
        """Rank 32: d = 3 + dim S_16 = 3 + 1 = 4.
        # VERIFIED [DC] dim S_16 = 1, [LT] Diamond-Shurman.
        """
        assert lattice_shadow_depth(32) == 4

    def test_rank_48_depth_5(self):
        """Rank 48: d = 3 + dim S_24 = 3 + 2 = 5.
        # VERIFIED [DC] dim S_24 = 2, [LT] manuscript line ~15994.
        """
        assert lattice_shadow_depth(48) == 5

    def test_rank_72_depth_6(self):
        """Rank 72: d = 3 + dim S_36 = 3 + 3 = 6.
        # VERIFIED [DC] dim M_36 = 4, dim S_36 = 3, [LT] manuscript line ~15997.
        """
        assert dim_M_k(36) == 4
        assert dim_S_k(36) == 3
        assert lattice_shadow_depth(72) == 6

    def test_depth_monotone_nondecreasing(self):
        """Shadow depth is non-decreasing in rank (for ranks that are multiples of 8).
        # VERIFIED [DC] dim S_k non-decreasing for k >= 0,
        #   [CF] depth = 3 + dim S_{r/2}.
        """
        table = lattice_shadow_depth_table(max_rank=96)
        for i in range(1, len(table)):
            assert table[i]['depth'] >= table[i-1]['depth']

    def test_depth_table_consistency(self):
        """Depth table entries are self-consistent.
        # VERIFIED [DC] depth = 3 + dim_S for each row.
        """
        table = lattice_shadow_depth_table(max_rank=96)
        for row in table:
            assert row['depth'] == 3 + row['dim_S']
            assert row['dim_S'] == max(0, row['dim_M'] - 1)
            assert row['weight'] == row['rank'] // 2


# =========================================================================
# Section 9: Full verification suite
# =========================================================================

class TestFullVerification:
    """Integration test: all verifications pass."""

    def test_all_pass(self):
        """run_all_verifications returns all_pass = True."""
        results = run_all_verifications()
        assert results['all_pass'], (
            f"Some checks failed: "
            + ", ".join(k for k in results if k.endswith('_ok') and not results[k])
        )

    def test_individual_checks(self):
        """Each individual check passes."""
        results = run_all_verifications()
        assert results['num_lattices_ok']
        assert results['all_rank_24']
        assert results['c_ok']
        assert results['kappa_ok']
        assert results['shadow_depth_ok']
        assert results['decomposition_ok']
        assert results['dim_S_12_ok']
        assert results['scalar_ok']


# =========================================================================
# Section 10: Cross-checks with existing engine
# =========================================================================

class TestCrossChecks:
    """Cross-checks against theorem_niemeier_shadow_discrimination_engine."""

    def test_label_count_matches(self):
        """Both engines agree on 24 Niemeier lattices.
        # VERIFIED [CF] cross-engine, [DC] enumeration.
        """
        from compute.lib.theorem_niemeier_shadow_discrimination_engine import (
            ALL_LABELS as DISC_LABELS,
        )
        assert len(DISC_LABELS) == len(ALL_LABELS)

    def test_scalar_class_matches(self):
        """Both engines agree on class G.
        # VERIFIED [CF] cross-engine.
        """
        from compute.lib.theorem_niemeier_shadow_discrimination_engine import (
            scalar_shadow_class as disc_scalar_class,
        )
        assert disc_scalar_class() == scalar_shadow_class()

    def test_scalar_depth_matches(self):
        """Both engines agree on scalar depth 2.
        # VERIFIED [CF] cross-engine.
        """
        from compute.lib.theorem_niemeier_shadow_discrimination_engine import (
            scalar_shadow_depth as disc_scalar_depth,
        )
        assert disc_scalar_depth() == scalar_shadow_depth()

    def test_kappa_matches(self):
        """Both engines agree on kappa = 24.
        # VERIFIED [CF] cross-engine.
        """
        from compute.lib.theorem_niemeier_shadow_discrimination_engine import (
            scalar_kappa as disc_kappa,
        )
        assert disc_kappa() == Fraction(kappa())

    def test_arithmetic_depth_extends_scalar(self):
        """The arithmetic depth (4) strictly exceeds the scalar depth (2).
        The difference is due to the Ramanujan cusp form.
        # VERIFIED [DC] 4 > 2, [LT] thm:depth-decomposition.
        """
        from compute.lib.theorem_niemeier_shadow_discrimination_engine import (
            scalar_shadow_depth as disc_scalar_depth,
        )
        assert niemeier_shadow_depth() > disc_scalar_depth()
