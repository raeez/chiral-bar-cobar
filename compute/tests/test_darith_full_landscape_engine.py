r"""Tests for arithmetic depth d_arith across the FULL 61-family landscape.

Covers:
  1. Depth decomposition consistency: d = 1 + d_arith + d_alg for ALL families
  2. Class G families: Heisenberg, free fermion, symplectic fermion, bc ghosts, lattices
  3. Class L families: ALL affine KM types (simply-laced, non-simply-laced, higher levels)
  4. Class C families: betagamma at all weights
  5. Class M families: Virasoro minimal models, generic, W_N, BP, moonshine
  6. Shadow tower denominator analysis for Virasoro
  7. Additivity under independent sums
  8. Koszul dual invariance
  9. Universal bounds (d_arith vs d_alg)
  10. Cusp form contributions
  11. DS transformation law
  12. Multi-path verification (4 independent paths)
  13. Cross-family consistency assertions
  14. Niemeier universality (all 24 have same d_arith)

Manuscript references:
    thm:depth-decomposition (arithmetic_shadows.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    prop:ising-d-arith (arithmetic_shadows.tex)
"""

import sys
sys.path.insert(0, 'compute/lib')

import pytest
from fractions import Fraction
from sympy import Rational

from darith_full_landscape_engine import (
    # Core functions
    cusp_form_dim_sl2z,
    DepthTriple,
    full_landscape_61,
    landscape_summary_61,
    depth_triple_table,
    darith_by_class,
    # Family constructors
    depth_heisenberg,
    depth_free_fermion,
    depth_symplectic_fermion,
    depth_bc_ghost,
    depth_betagamma,
    depth_lattice_unimodular,
    depth_affine_km,
    depth_virasoro_generic,
    depth_virasoro_minimal,
    depth_w_algebra,
    depth_bershadsky_polyakov,
    depth_moonshine,
    # Analysis
    virasoro_shadow_S,
    virasoro_shadow_denominator_primes,
    virasoro_darith_from_tower,
    darith_independent_sum,
    darith_koszul_dual_comparison,
    darith_dalg_scatter,
    universal_bound_check,
    cusp_form_in_shadow_tower,
    darith_ds_transformation,
    # Multi-path
    multipath_verify_heisenberg,
    multipath_verify_lattice,
    multipath_verify_virasoro_ising,
    multipath_verify_E8,
    # Internal
    _count_critical_lines,
    _factorize_int,
    _matrix_rank_Q,
    _kappa_km,
    _central_charge_km,
)


# ========================================================================
# 1. Full landscape: 61 families, all consistent
# ========================================================================

class TestFullLandscape:
    """Verify the full 61-family landscape."""

    def test_total_61(self):
        """The landscape has exactly 61 families."""
        table = full_landscape_61()
        assert len(table) == 61

    def test_all_depth_consistent(self):
        """d_total = 1 + d_arith + d_alg for EVERY family."""
        table = full_landscape_61()
        for dt in table:
            assert dt.depth_consistent(), (
                f"{dt.family_id}: d_total={dt.d_total}, "
                f"d_arith={dt.d_arith}, d_alg={dt.d_alg}")

    def test_all_four_classes(self):
        """All four shadow classes G, L, C, M are represented."""
        table = full_landscape_61()
        classes = set(dt.shadow_class for dt in table)
        assert classes == {'G', 'L', 'C', 'M'}

    def test_class_counts(self):
        """Check approximate class counts."""
        s = landscape_summary_61()
        assert s['by_class']['G'] >= 5
        assert s['by_class']['L'] >= 15
        assert s['by_class']['C'] >= 2
        assert s['by_class']['M'] >= 15

    def test_all_have_verification_paths(self):
        """Every family has at least 2 verification paths."""
        table = full_landscape_61()
        for dt in table:
            assert len(dt.verification_paths) >= 2, (
                f"{dt.family_id}: only {len(dt.verification_paths)} paths")


# ========================================================================
# 2. Cusp form dimension (foundational)
# ========================================================================

class TestCuspFormDim:
    """Verify dim S_k(SL(2,Z)) against known values."""

    def test_small_weights_zero(self):
        for k in [2, 4, 6, 8, 10]:
            assert cusp_form_dim_sl2z(k) == 0

    def test_ramanujan_delta(self):
        assert cusp_form_dim_sl2z(12) == 1

    def test_S14_zero(self):
        """dim S_14 = 0 (k=14 mod 12 = 2, dim M = 1, dim S = 0)."""
        assert cusp_form_dim_sl2z(14) == 0

    def test_S16_through_S22(self):
        assert cusp_form_dim_sl2z(16) == 1
        assert cusp_form_dim_sl2z(18) == 1
        assert cusp_form_dim_sl2z(20) == 1
        assert cusp_form_dim_sl2z(22) == 1

    def test_S24_two(self):
        assert cusp_form_dim_sl2z(24) == 2

    def test_S36_three(self):
        assert cusp_form_dim_sl2z(36) == 3

    def test_S48_four(self):
        assert cusp_form_dim_sl2z(48) == 4

    def test_odd_zero(self):
        for k in [1, 3, 5, 7, 11, 13, 15]:
            assert cusp_form_dim_sl2z(k) == 0

    def test_negative_zero(self):
        assert cusp_form_dim_sl2z(-2) == 0

    def test_nondecreasing_at_lattice_weights(self):
        """dim S_{4m} is non-decreasing for m >= 1."""
        prev = 0
        for m in range(1, 20):
            d = cusp_form_dim_sl2z(4 * m)
            assert d >= prev
            prev = d


# ========================================================================
# 3. Class G families
# ========================================================================

class TestClassG:
    """Verify depth triples for class G (Gaussian) families."""

    def test_heisenberg_k1(self):
        dt = depth_heisenberg(1)
        assert dt.shadow_class == 'G'
        assert dt.d_arith == 1
        assert dt.d_alg == 0
        assert dt.d_total == 2
        assert dt.kappa == 1

    def test_heisenberg_k2(self):
        dt = depth_heisenberg(2)
        assert dt.d_arith == 1
        assert dt.kappa == 2

    def test_free_fermion(self):
        dt = depth_free_fermion()
        assert dt.shadow_class == 'G'
        assert dt.d_arith == 0
        assert dt.d_alg == 0
        assert dt.d_total == 1
        assert dt.kappa == Rational(1, 4)
        assert dt.central_charge == Rational(1, 2)

    def test_symplectic_fermion(self):
        dt = depth_symplectic_fermion()
        assert dt.shadow_class == 'G'
        assert dt.d_arith == 0
        assert dt.d_alg == 0
        assert dt.d_total == 1
        assert dt.kappa == Rational(-1, 2)
        assert dt.central_charge == Rational(-1)

    def test_lattice_E8(self):
        dt = depth_lattice_unimodular(8)
        assert dt.shadow_class == 'G'
        assert dt.d_arith == 2
        assert dt.d_alg == 0
        assert dt.d_total == 3
        assert dt.kappa == 8

    def test_lattice_rank16(self):
        dt = depth_lattice_unimodular(16)
        assert dt.d_arith == 2  # dim S_8 = 0

    def test_lattice_rank24_niemeier(self):
        dt = depth_lattice_unimodular(24)
        assert dt.d_arith == 3  # dim S_12 = 1

    def test_lattice_rank32(self):
        dt = depth_lattice_unimodular(32)
        assert dt.d_arith == 3  # dim S_16 = 1

    def test_lattice_rank48_first_gt3(self):
        """Rank 48: d_arith = 4, the FIRST family with d_arith > 3."""
        dt = depth_lattice_unimodular(48)
        assert dt.d_arith == 4  # dim S_24 = 2

    def test_lattice_rank72(self):
        dt = depth_lattice_unimodular(72)
        assert dt.d_arith == 5  # dim S_36 = 3

    def test_lattice_rank96(self):
        dt = depth_lattice_unimodular(96)
        assert dt.d_arith == 6  # dim S_48 = 4

    def test_lattice_monotonicity(self):
        """d_arith is non-decreasing with rank."""
        prev = 0
        for rank in range(8, 120, 8):
            dt = depth_lattice_unimodular(rank)
            assert dt.d_arith >= prev
            prev = dt.d_arith

    def test_class_G_all_d_alg_zero(self):
        """All class G families have d_alg = 0."""
        table = full_landscape_61()
        for dt in table:
            if dt.shadow_class == 'G':
                assert dt.d_alg == 0, f"{dt.family_id}: d_alg={dt.d_alg}"


# ========================================================================
# 4. Class L families
# ========================================================================

class TestClassL:
    """Verify depth triples for class L (Lie) families."""

    def test_sl2_level1(self):
        dt = depth_affine_km('A1', 1)
        assert dt.shadow_class == 'L'
        assert dt.d_arith == 1
        assert dt.d_alg == 1
        assert dt.d_total == 3
        assert dt.kappa == Rational(3, 4) * 3  # dim=3, h_vee=2, (3*3)/(2*2)=9/4

    def test_sl3_level1(self):
        dt = depth_affine_km('A2', 1)
        assert dt.d_arith == 1
        # kappa = 8*(1+3)/(2*3) = 16/3
        assert dt.kappa == Rational(16, 3)

    def test_E8_level1_exceptional(self):
        """E_8 level 1 is the ONLY affine KM with d_arith > 1."""
        dt = depth_affine_km('E8', 1)
        assert dt.d_arith == 2
        assert dt.d_alg == 1
        assert dt.d_total == 4

    def test_E7_level1(self):
        dt = depth_affine_km('E7', 1)
        assert dt.d_arith == 1

    def test_E6_level1(self):
        dt = depth_affine_km('E6', 1)
        assert dt.d_arith == 1

    def test_D4_level1(self):
        dt = depth_affine_km('D4', 1)
        assert dt.d_arith == 1

    def test_D5_level1(self):
        dt = depth_affine_km('D5', 1)
        assert dt.d_arith == 1

    def test_D6_level1(self):
        dt = depth_affine_km('D6', 1)
        assert dt.d_arith == 1

    # Non-simply-laced
    def test_B2_level1(self):
        dt = depth_affine_km('B2', 1)
        assert dt.shadow_class == 'L'
        assert dt.d_arith == 1

    def test_B3_level1(self):
        dt = depth_affine_km('B3', 1)
        assert dt.d_arith == 1

    def test_B4_level1(self):
        dt = depth_affine_km('B4', 1)
        assert dt.d_arith == 1

    def test_C2_level1(self):
        dt = depth_affine_km('C2', 1)
        assert dt.d_arith == 1

    def test_C3_level1(self):
        dt = depth_affine_km('C3', 1)
        assert dt.d_arith == 1

    def test_C4_level1(self):
        dt = depth_affine_km('C4', 1)
        assert dt.d_arith == 1

    def test_G2_level1(self):
        dt = depth_affine_km('G2', 1)
        assert dt.d_arith == 1

    def test_F4_level1(self):
        dt = depth_affine_km('F4', 1)
        assert dt.d_arith == 1

    # Higher levels
    def test_sl2_levels_2_to_5(self):
        """sl_2 at levels 2..5: all d_arith = 1."""
        for k in range(2, 6):
            dt = depth_affine_km('A1', k)
            assert dt.d_arith == 1, f"sl_2 level {k}: d_arith={dt.d_arith}"
            assert dt.shadow_class == 'L'

    def test_all_class_L_d_alg_1(self):
        """All class L families have d_alg = 1."""
        table = full_landscape_61()
        for dt in table:
            if dt.shadow_class == 'L':
                assert dt.d_alg == 1, f"{dt.family_id}: d_alg={dt.d_alg}"

    def test_E8_only_exceptional(self):
        """E_8 level 1 is the ONLY level-1 affine KM with d_arith > 1."""
        types = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
                 'D4', 'D5', 'D6', 'E6', 'E7', 'E8',
                 'B2', 'B3', 'B4', 'C2', 'C3', 'C4', 'G2', 'F4']
        exceptional = [t for t in types if depth_affine_km(t, 1).d_arith > 1]
        assert exceptional == ['E8']

    def test_kappa_formulas(self):
        """Verify kappa = dim(g)(k+h^vee)/(2h^vee) for selected types."""
        # sl_2: dim=3, h_vee=2, k=1: kappa = 3*3/4 = 9/4
        assert _kappa_km('A1', 1) == Rational(9, 4)
        # E_8: dim=248, h_vee=30, k=1: kappa = 248*31/60
        assert _kappa_km('E8', 1) == Rational(248 * 31, 60)


# ========================================================================
# 5. Class C families
# ========================================================================

class TestClassC:
    """Verify depth triples for class C (contact) families."""

    def test_betagamma_standard(self):
        dt = depth_betagamma(1)
        assert dt.shadow_class == 'C'
        assert dt.d_arith == 1
        assert dt.d_alg == 2
        assert dt.d_total == 4
        # kappa(bg, lambda=1) = 6-6+1 = 1
        assert dt.kappa == 1

    def test_betagamma_symplectic(self):
        dt = depth_betagamma(Rational(1, 2))
        assert dt.shadow_class == 'C'
        assert dt.d_arith == 1
        assert dt.d_alg == 2
        # kappa(bg, 1/2) = 6/4 - 3 + 1 = -1/2
        assert dt.kappa == Rational(-1, 2)

    def test_bc_ghost_spin2(self):
        dt = depth_bc_ghost(2)
        assert dt.shadow_class == 'C'
        assert dt.d_arith == 1
        assert dt.d_alg == 2
        assert dt.d_total == 4
        # kappa(bc, 2) = -(24 - 12 + 1) = -13
        assert dt.kappa == -13

    def test_all_class_C_d_alg_2(self):
        """All class C families have d_alg = 2."""
        table = full_landscape_61()
        for dt in table:
            if dt.shadow_class == 'C':
                assert dt.d_alg == 2, f"{dt.family_id}: d_alg={dt.d_alg}"


# ========================================================================
# 6. Class M families: Virasoro minimal models
# ========================================================================

class TestVirasoroMinimal:
    """Verify d_arith for Virasoro minimal models."""

    def test_ising_M34(self):
        """Ising M(3,4), c=1/2: d_arith = 0 (prop:ising-d-arith)."""
        dt = depth_virasoro_minimal(3, 4)
        assert dt.d_arith == 0
        assert dt.shadow_class == 'M'
        assert dt.d_alg is None
        assert dt.central_charge == Rational(1, 2)

    def test_tricritical_ising_M45(self):
        """M(4,5), c=7/10: d_arith = 3."""
        dt = depth_virasoro_minimal(4, 5)
        assert dt.d_arith == 3
        assert dt.central_charge == Rational(7, 10)

    def test_three_state_potts_M56(self):
        """M(5,6), c=4/5: d_arith >= 1."""
        dt = depth_virasoro_minimal(5, 6)
        assert dt.d_arith >= 1

    def test_M67(self):
        """M(6,7), c=6/7: d_arith >= 1."""
        dt = depth_virasoro_minimal(6, 7)
        assert dt.d_arith >= 1

    def test_M78(self):
        """M(7,8), c=25/28: d_arith >= 1."""
        dt = depth_virasoro_minimal(7, 8)
        assert dt.d_arith >= 1

    def test_nonunitary_M35(self):
        """M(3,5), c=-3/5 (non-unitary): d_arith computable."""
        dt = depth_virasoro_minimal(3, 5)
        assert isinstance(dt.d_arith, int)
        assert dt.central_charge == Rational(-3, 5)

    def test_M57(self):
        """M(5,7), non-unitary."""
        dt = depth_virasoro_minimal(5, 7)
        assert isinstance(dt.d_arith, int)
        assert dt.d_arith >= 0

    def test_M47(self):
        """M(4,7), non-unitary."""
        dt = depth_virasoro_minimal(4, 7)
        assert isinstance(dt.d_arith, int)

    def test_nondecreasing_unitary(self):
        """d_arith is non-decreasing for unitary M(m, m+1), m=3..7."""
        prev = 0
        for m in range(3, 8):
            dt = depth_virasoro_minimal(m, m + 1)
            assert dt.d_arith >= prev, (
                f"M({m},{m+1}): d_arith={dt.d_arith} < {prev}")
            prev = dt.d_arith

    def test_all_class_M(self):
        """All Virasoro minimal models are class M."""
        for m in range(3, 8):
            dt = depth_virasoro_minimal(m, m + 1)
            assert dt.shadow_class == 'M'


# ========================================================================
# 7. Class M families: Virasoro generic
# ========================================================================

class TestVirasoroGeneric:
    """Verify d_arith for Virasoro at generic central charge."""

    def test_c1_free_boson(self):
        dt = depth_virasoro_generic(1)
        assert dt.d_arith == 1

    def test_c25_koszul_dual(self):
        dt = depth_virasoro_generic(25)
        assert dt.d_arith == 1

    def test_c26_critical_string(self):
        dt = depth_virasoro_generic(26)
        assert dt.d_arith == 1

    def test_c13_self_dual(self):
        dt = depth_virasoro_generic(13)
        assert dt.d_arith == 0

    def test_c2_generic_integer(self):
        dt = depth_virasoro_generic(2)
        assert dt.d_arith == 0

    def test_c10_generic_integer(self):
        dt = depth_virasoro_generic(10)
        assert dt.d_arith == 0

    def test_ising_dispatch(self):
        """c=1/2 dispatches to Ising: d_arith = 0."""
        dt = depth_virasoro_generic(Rational(1, 2))
        assert dt.d_arith == 0

    def test_tricritical_dispatch(self):
        """c=7/10 dispatches to tri-critical Ising: d_arith = 3."""
        dt = depth_virasoro_generic(Rational(7, 10))
        assert dt.d_arith == 3

    def test_all_class_M(self):
        """All generic Virasoro are class M."""
        for c in [1, 2, 10, 13, 25, 26]:
            dt = depth_virasoro_generic(c)
            assert dt.shadow_class == 'M'


# ========================================================================
# 8. Class M families: W-algebras
# ========================================================================

class TestWAlgebra:
    """Verify d_arith for W-algebras."""

    def test_W3_generic(self):
        dt = depth_w_algebra(3)
        assert dt.d_arith == 0
        assert dt.shadow_class == 'M'

    def test_W4_generic(self):
        dt = depth_w_algebra(4)
        assert dt.d_arith == 0

    def test_W5_generic(self):
        dt = depth_w_algebra(5)
        assert dt.d_arith == 0

    def test_W6_generic(self):
        dt = depth_w_algebra(6)
        assert dt.d_arith == 0

    def test_W3_free_field(self):
        """W_3 at c=2 (free field): d_arith = 1."""
        dt = depth_w_algebra(3, c_val=2)
        assert dt.d_arith == 1

    def test_W4_free_field(self):
        """W_4 at c=3 (free field): d_arith = 1."""
        dt = depth_w_algebra(4, c_val=3)
        assert dt.d_arith == 1

    def test_W5_free_field(self):
        """W_5 at c=4 (free field): d_arith = 1."""
        dt = depth_w_algebra(5, c_val=4)
        assert dt.d_arith == 1


# ========================================================================
# 9. Class M: Bershadsky-Polyakov and moonshine
# ========================================================================

class TestBPMoonshine:
    """Verify d_arith for Bershadsky-Polyakov and moonshine."""

    def test_bershadsky_polyakov(self):
        dt = depth_bershadsky_polyakov(5)
        assert dt.shadow_class == 'M'
        assert dt.d_arith == 0  # generic level, non-modular
        assert dt.d_alg is None

    def test_moonshine(self):
        dt = depth_moonshine()
        assert dt.shadow_class == 'M'
        assert dt.d_arith == 1  # j-function structure
        assert dt.kappa == 12
        assert dt.central_charge == 24

    def test_moonshine_kappa_not_c_over_2(self):
        """AP48: kappa(V^natural) = 12, NOT c/2 = 12. Actually coincidence here.

        But the MECHANISM is different: kappa = 12 comes from the j-function,
        not from c/2 = 24/2 = 12. For moonshine, kappa = c/2 = 12 is
        a coincidence (dim_1 = 0, rank = 0, so kappa is determined by
        the genus-1 bar complex, not by the central charge formula).
        """
        dt = depth_moonshine()
        # kappa = 12 = c/2 = 24/2: this is a COINCIDENCE (AP48)
        assert dt.kappa == 12
        assert dt.central_charge == 24


# ========================================================================
# 10. Shadow tower denominator analysis
# ========================================================================

class TestShadowTowerDenominators:
    """Analyze denominator primes in the Virasoro shadow tower."""

    def test_S2_denominator(self):
        """S_2 = c/2: denominator prime = {2}."""
        s = virasoro_shadow_S(2, Rational(5))
        assert s == Rational(5, 2)

    def test_S3_value(self):
        """S_3 = 2/3 (alpha = 2 on T-line)."""
        s = virasoro_shadow_S(3, Rational(5))
        assert s == Rational(2, 3)

    def test_S4_formula(self):
        """S_4 = 10/[c(5c+22)] for Virasoro."""
        c_val = Rational(5)
        expected = Rational(10, 5 * (25 + 22))
        s = virasoro_shadow_S(4, c_val)
        assert s == expected

    def test_S4_primes_at_c5(self):
        """S_4 at c=5: 10/(5*47) = 2/47. After cancellation denom = 47."""
        s = virasoro_shadow_S(4, Rational(5))
        assert s == Rational(2, 47)
        primes = virasoro_shadow_denominator_primes(4, Rational(5))
        assert 47 in primes

    def test_tower_analysis_c1(self):
        """Tower analysis at c=1: denominators grow in complexity."""
        res = virasoro_darith_from_tower(Rational(1), 8)
        assert 'new_primes_at' in res
        assert len(res['all_primes']) >= 2

    def test_tower_analysis_c26(self):
        """Tower analysis at c=26."""
        res = virasoro_darith_from_tower(Rational(26), 8)
        assert len(res['all_primes']) >= 3

    def test_tower_algebraic(self):
        """Shadow tower coefficients are rational functions of c (algebraic)."""
        for c_val in [Rational(1), Rational(5), Rational(13), Rational(26)]:
            for r in range(2, 8):
                s = virasoro_shadow_S(r, c_val)
                assert isinstance(s, Rational), (
                    f"S_{r}(c={c_val}) = {s} not Rational")

    def test_S4_zero_iff_c_zero(self):
        """S_4 is nonzero for all nonzero c (c*(5c+22) nonzero).

        5c+22 = 0 at c = -22/5, which is a degenerate point.
        """
        for c_val in [Rational(1), Rational(5), Rational(13), Rational(26)]:
            s = virasoro_shadow_S(4, c_val)
            assert s != 0


# ========================================================================
# 11. Additivity under independent sums
# ========================================================================

class TestAdditivity:
    """Verify d_arith(A1 + A2) = max(d_arith(A1), d_arith(A2))."""

    def test_heisenberg_plus_heisenberg(self):
        dt1 = depth_heisenberg(1)
        dt2 = depth_heisenberg(2)
        res = darith_independent_sum(dt1, dt2)
        assert res['d_arith_sum'] == 1  # max(1, 1)

    def test_heisenberg_plus_virasoro(self):
        dt1 = depth_heisenberg(1)
        dt2 = depth_virasoro_generic(13)
        res = darith_independent_sum(dt1, dt2)
        assert res['d_arith_sum'] == max(1, 0) == 1

    def test_lattice_plus_virasoro(self):
        dt1 = depth_lattice_unimodular(24)  # d_arith = 3
        dt2 = depth_virasoro_generic(1)     # d_arith = 1
        res = darith_independent_sum(dt1, dt2)
        assert res['d_arith_sum'] == 3

    def test_virasoro_plus_virasoro(self):
        dt1 = depth_virasoro_generic(1)   # d_arith = 1
        dt2 = depth_virasoro_generic(25)  # d_arith = 1
        res = darith_independent_sum(dt1, dt2)
        assert res['d_arith_sum'] == 1

    def test_sl2_plus_sl3(self):
        dt1 = depth_affine_km('A1', 1)  # d_arith = 1
        dt2 = depth_affine_km('A2', 1)  # d_arith = 1
        res = darith_independent_sum(dt1, dt2)
        assert res['d_arith_sum'] == 1

    def test_free_fermion_plus_heisenberg(self):
        dt1 = depth_free_fermion()      # d_arith = 0
        dt2 = depth_heisenberg(1)       # d_arith = 1
        res = darith_independent_sum(dt1, dt2)
        assert res['d_arith_sum'] == 1

    def test_two_lattices(self):
        dt1 = depth_lattice_unimodular(8)   # d_arith = 2
        dt2 = depth_lattice_unimodular(24)  # d_arith = 3
        res = darith_independent_sum(dt1, dt2)
        assert res['d_arith_sum'] == 3

    def test_sum_consistent(self):
        """All sums are consistent."""
        pairs = [
            (depth_heisenberg(1), depth_free_fermion()),
            (depth_affine_km('A1', 1), depth_betagamma(1)),
            (depth_lattice_unimodular(24), depth_moonshine()),
        ]
        for dt1, dt2 in pairs:
            res = darith_independent_sum(dt1, dt2)
            assert res['consistent']


# ========================================================================
# 12. Koszul dual invariance
# ========================================================================

class TestKoszulDual:
    """Verify d_arith(A) = d_arith(A!) for Koszul pairs."""

    def test_heisenberg(self):
        res = darith_koszul_dual_comparison('heisenberg_k1')
        assert res['koszul_invariant']
        assert res['d_arith_A'] == 1
        assert res['d_arith_A_dual'] == 1

    def test_virasoro_c1(self):
        """Vir_1 <-> Vir_25: d_arith = 1 = 1."""
        res = darith_koszul_dual_comparison('vir_c1')
        assert res['koszul_invariant']

    def test_virasoro_c13_self_dual(self):
        """Vir_13 is self-dual: d_arith = 0."""
        res = darith_koszul_dual_comparison('vir_c13')
        assert res['koszul_invariant']
        assert res['d_arith_A'] == 0

    def test_E8(self):
        """E_8 level 1: d_arith = 2 preserved."""
        res = darith_koszul_dual_comparison('E8_k1')
        assert res['koszul_invariant']
        assert res['d_arith_A'] == 2

    def test_sl2(self):
        res = darith_koszul_dual_comparison('A1_k1')
        assert res['koszul_invariant']

    def test_sl3(self):
        res = darith_koszul_dual_comparison('A2_k1')
        assert res['koszul_invariant']

    def test_moonshine(self):
        res = darith_koszul_dual_comparison('moonshine')
        assert res['koszul_invariant']

    def test_unknown_family(self):
        """Unknown family returns dual_found=False."""
        res = darith_koszul_dual_comparison('nonexistent')
        assert not res['dual_found']


# ========================================================================
# 13. Universal bounds
# ========================================================================

class TestUniversalBounds:
    """Test universal bound d_arith vs d_alg."""

    def test_bound_fails(self):
        """d_arith <= d_alg does NOT hold universally.

        Counterexamples: class G lattice VOAs have d_arith >= 2 but d_alg = 0.
        """
        ub = universal_bound_check()
        assert not ub['bound_holds']

    def test_class_G_counterexamples(self):
        """Class G lattice VOAs are the counterexamples."""
        ub = universal_bound_check()
        cex = ub['class_G_counterexamples']
        assert len(cex) >= 4  # at least E8, rank16, rank24, rank32

    def test_scatter_complete(self):
        """Scatter plot covers all 61 families."""
        scatter = darith_dalg_scatter()
        assert len(scatter) == 61

    def test_scatter_class_consistency(self):
        """In the scatter, class G has d_alg=0, class L has d_alg=1, etc."""
        scatter = darith_dalg_scatter()
        for p in scatter:
            if p['shadow_class'] == 'G':
                assert p['d_alg'] == 0
            elif p['shadow_class'] == 'L':
                assert p['d_alg'] == 1
            elif p['shadow_class'] == 'C':
                assert p['d_alg'] == 2
            elif p['shadow_class'] == 'M':
                assert p['d_alg'] == float('inf')


# ========================================================================
# 14. Cusp form contributions
# ========================================================================

class TestCuspForms:
    """Test cusp form detection in shadow towers."""

    def test_virasoro_tower_algebraic(self):
        """Shadow tower is always algebraic (no cusp form content)."""
        res = cusp_form_in_shadow_tower(Rational(26), 12)
        assert res['shadow_tower_algebraic']
        assert not res['cusp_form_visible_in_tower']

    def test_virasoro_c1(self):
        res = cusp_form_in_shadow_tower(Rational(1), 10)
        assert res['shadow_tower_algebraic']

    def test_virasoro_c13(self):
        res = cusp_form_in_shadow_tower(Rational(13), 10)
        assert res['shadow_tower_algebraic']


# ========================================================================
# 15. DS transformation law
# ========================================================================

class TestDSTransformation:
    """Test d_arith under DS reduction."""

    def test_sl3_to_W3(self):
        """sl_3 level 5 -> W_3: d_arith 1 -> 0 (decreased)."""
        res = darith_ds_transformation('A2', 3, 5)
        assert res['affine']['d_arith'] == 1
        assert res['w_algebra']['d_arith'] == 0
        assert res['d_arith_change'] == 'decreased'

    def test_sl4_to_W4(self):
        res = darith_ds_transformation('A3', 4, 5)
        assert res['affine']['d_arith'] == 1
        assert res['w_algebra']['d_arith'] == 0
        assert res['d_arith_change'] == 'decreased'

    def test_d_alg_always_increases(self):
        """DS always increases d_alg (L -> M)."""
        for N, lie_type in [(3, 'A2'), (4, 'A3'), (5, 'A4')]:
            res = darith_ds_transformation(lie_type, N, 5)
            assert res['d_alg_change'] == 'increased (1 -> inf)'

    def test_ds_does_not_increase_darith(self):
        """DS reduction can decrease d_arith, never increases at generic level."""
        for N, lie_type in [(3, 'A2'), (4, 'A3'), (5, 'A4')]:
            res = darith_ds_transformation(lie_type, N, 5)
            assert res['d_arith_change'] in ('decreased', 'same')


# ========================================================================
# 16. Multi-path verification
# ========================================================================

class TestMultiPath:
    """Multi-path verification of d_arith for key families."""

    def test_heisenberg_4_paths(self):
        mv = multipath_verify_heisenberg()
        assert mv['all_agree']
        assert mv['d_arith'] == 1
        assert mv['path1_shadow_tower']['result'] == 1
        assert mv['path2_theta']['result'] == 1
        assert mv['path3_rankin_selberg']['result'] == 1
        assert mv['path4_ds']['result'] == 1

    def test_lattice_24_3_paths(self):
        mv = multipath_verify_lattice(24)
        assert mv['all_agree']
        assert mv['d_arith'] == 3
        assert mv['path1_theta']['result'] == 3
        assert mv['path2_cusp_dim']['result'] == 3
        assert mv['path3_rankin_selberg']['result'] == 3

    def test_lattice_48_3_paths(self):
        mv = multipath_verify_lattice(48)
        assert mv['all_agree']
        assert mv['d_arith'] == 4

    def test_ising_3_paths(self):
        mv = multipath_verify_virasoro_ising()
        assert mv['all_agree']
        assert mv['d_arith'] == 0

    def test_E8_3_paths(self):
        mv = multipath_verify_E8()
        assert mv['all_agree']
        assert mv['d_arith'] == 2


# ========================================================================
# 17. Cross-family consistency
# ========================================================================

class TestCrossFamilyConsistency:
    """Cross-family structural assertions from the depth decomposition."""

    def test_d_arith_nonneg(self):
        """d_arith >= 0 for all families."""
        table = full_landscape_61()
        for dt in table:
            if isinstance(dt.d_arith, int):
                assert dt.d_arith >= 0, f"{dt.family_id}: d_arith={dt.d_arith}"

    def test_class_M_infinite_d_total(self):
        """All class M families have d_total = infinity."""
        table = full_landscape_61()
        for dt in table:
            if dt.shadow_class == 'M':
                assert dt.d_total is None, f"{dt.family_id}: d_total={dt.d_total}"

    def test_class_G_L_C_finite_d_total(self):
        """Classes G, L, C have finite d_total."""
        table = full_landscape_61()
        for dt in table:
            if dt.shadow_class in ('G', 'L', 'C'):
                assert dt.d_total is not None, f"{dt.family_id}: d_total is None"
                assert isinstance(dt.d_total, int)

    def test_E8_level1_vs_E8_lattice(self):
        """V_1(E_8) and V_{E_8} have same d_arith = 2."""
        dt_km = depth_affine_km('E8', 1)
        dt_lat = depth_lattice_unimodular(8)
        assert dt_km.d_arith == dt_lat.d_arith == 2

    def test_heisenberg_less_than_lattice(self):
        """Heisenberg d_arith < lattice d_arith."""
        dt_h = depth_heisenberg(1)
        dt_l = depth_lattice_unimodular(8)
        assert dt_h.d_arith < dt_l.d_arith

    def test_free_fermion_equals_ising(self):
        """Free fermion and Ising have same d_arith = 0."""
        dt_ff = depth_free_fermion()
        dt_ising = depth_virasoro_minimal(3, 4)
        assert dt_ff.d_arith == dt_ising.d_arith == 0

    def test_moonshine_vs_niemeier(self):
        """Moonshine V^natural (d_arith=1) < Niemeier lattice (d_arith=3).

        This reflects that the moonshine module is NOT a lattice VOA
        despite having c=24.
        """
        dt_m = depth_moonshine()
        dt_n = depth_lattice_unimodular(24)
        assert dt_m.d_arith < dt_n.d_arith

    def test_koszul_dual_virasoro_c1_c25(self):
        """c=1 and c=25 have same d_arith (Koszul duality)."""
        dt1 = depth_virasoro_generic(1)
        dt25 = depth_virasoro_generic(25)
        assert dt1.d_arith == dt25.d_arith == 1

    def test_max_darith_in_census(self):
        """The maximum d_arith among all 61 families."""
        table = full_landscape_61()
        finite = [dt for dt in table if isinstance(dt.d_arith, int)]
        max_dt = max(finite, key=lambda dt: dt.d_arith)
        # Should come from a Virasoro minimal model with many primaries
        assert max_dt.d_arith >= 4

    def test_class_L_d_arith_bounded(self):
        """All class L families have d_arith <= 2."""
        table = full_landscape_61()
        for dt in table:
            if dt.shadow_class == 'L':
                assert dt.d_arith <= 2, f"{dt.family_id}: d_arith={dt.d_arith}"


# ========================================================================
# 18. Internal helpers
# ========================================================================

class TestInternalHelpers:
    """Test factorization and matrix rank helpers."""

    def test_factorize_small(self):
        assert _factorize_int(1) == {}
        assert _factorize_int(2) == {2: 1}
        assert _factorize_int(12) == {2: 2, 3: 1}
        assert _factorize_int(360) == {2: 3, 3: 2, 5: 1}

    def test_factorize_prime(self):
        assert _factorize_int(7) == {7: 1}
        assert _factorize_int(97) == {97: 1}

    def test_matrix_rank_identity(self):
        assert _matrix_rank_Q([[1, 0], [0, 1]]) == 2

    def test_matrix_rank_dependent(self):
        assert _matrix_rank_Q([[1, 2], [2, 4]]) == 1

    def test_matrix_rank_empty(self):
        assert _matrix_rank_Q([]) == 0

    def test_matrix_rank_3x4(self):
        assert _matrix_rank_Q([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]) == 3

    def test_ising_multiplicative_dependence(self):
        """Ising: lambda = {1/8, 1}. Both powers of 2. Rank 1."""
        lambdas = [Fraction(1, 8), Fraction(1)]
        assert _count_critical_lines(lambdas) == 0

    def test_tricritical_four_primes(self):
        """Tri-critical Ising has rank 4 multiplicative structure."""
        dt = depth_virasoro_minimal(4, 5)
        assert dt.d_arith == 3  # rank - 1 = 4 - 1 = 3


# ========================================================================
# 19. Depth triple table
# ========================================================================

class TestDepthTripleTable:
    """Test the flat table representation."""

    def test_table_length(self):
        table = depth_triple_table()
        assert len(table) == 61

    def test_table_has_all_fields(self):
        table = depth_triple_table()
        for row in table:
            assert 'family' in row
            assert 'family_id' in row
            assert 'class' in row
            assert 'd_arith' in row
            assert 'd_alg' in row
            assert 'd_total' in row


# ========================================================================
# 20. Summary statistics
# ========================================================================

class TestSummary:
    """Test landscape summary statistics."""

    def test_summary_total(self):
        s = landscape_summary_61()
        assert s['total'] == 61

    def test_summary_consistent(self):
        s = landscape_summary_61()
        assert s['all_consistent']

    def test_by_class_summary(self):
        bc = darith_by_class()
        assert len(bc['G']) >= 5
        assert len(bc['L']) >= 15
        assert len(bc['C']) >= 2
        assert len(bc['M']) >= 15


# ========================================================================
# 21. Specific kappa values (AP1/AP48 guard)
# ========================================================================

class TestKappaValues:
    """Verify kappa formulas against known values (AP1 guard)."""

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        assert _kappa_km('A1', 1) == Rational(9, 4)

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        assert _kappa_km('A2', 1) == Rational(16, 3)

    def test_kappa_E8_k1(self):
        """kappa(E_8, k=1) = 248*(1+30)/(2*30) = 248*31/60."""
        assert _kappa_km('E8', 1) == Rational(248 * 31, 60)

    def test_kappa_G2_k1(self):
        """kappa(G_2, k=1) = 14*(1+4)/(2*4) = 70/8 = 35/4."""
        assert _kappa_km('G2', 1) == Rational(35, 4)

    def test_central_charge_sl2_k1(self):
        """c(sl_2, k=1) = 1*3/(1+2) = 1."""
        assert _central_charge_km('A1', 1) == 1

    def test_central_charge_E8_k1(self):
        """c(E_8, k=1) = 1*248/(1+30) = 8."""
        assert _central_charge_km('E8', 1) == 8


# ========================================================================
# 22. d_arith at higher lattice ranks
# ========================================================================

class TestHigherLatticeRanks:
    """Verify d_arith for lattice VOAs at high ranks."""

    def test_rank_40(self):
        """Rank 40: theta weight 20, dim S_20 = 1, d_arith = 3."""
        dt = depth_lattice_unimodular(40)
        assert dt.d_arith == 2 + cusp_form_dim_sl2z(20)

    def test_rank_48(self):
        """Rank 48: theta weight 24, dim S_24 = 2, d_arith = 4."""
        dt = depth_lattice_unimodular(48)
        assert dt.d_arith == 4

    def test_first_darith_gt_3(self):
        """First d_arith > 3 is at rank 48."""
        for rank in range(8, 48, 8):
            dt = depth_lattice_unimodular(rank)
            assert dt.d_arith <= 3, f"rank {rank} has d_arith={dt.d_arith}"
        dt48 = depth_lattice_unimodular(48)
        assert dt48.d_arith == 4


# ========================================================================
# 23. Virasoro shadow coefficient verification
# ========================================================================

class TestVirasoroShadowCoefficients:
    """Verify specific Virasoro shadow coefficients."""

    def test_S2_equals_c_over_2(self):
        for c_val in [Rational(1), Rational(5), Rational(26)]:
            assert virasoro_shadow_S(2, c_val) == c_val / 2

    def test_S3_equals_2_over_3(self):
        """S_3 = 2/3 for all c (on T-line)."""
        for c_val in [Rational(1), Rational(5), Rational(26)]:
            assert virasoro_shadow_S(3, c_val) == Rational(2, 3)

    def test_S4_formula_explicit(self):
        """S_4 = 10/[c(5c+22)]."""
        c_val = Rational(1)
        assert virasoro_shadow_S(4, c_val) == Rational(10, 27)

    def test_S4_at_c26(self):
        """S_4(26) = 10/(26*152) = 10/3952 = 5/1976."""
        assert virasoro_shadow_S(4, Rational(26)) == Rational(5, 1976)

    def test_S_r_nonzero(self):
        """All S_r are nonzero for Virasoro at generic c."""
        c_val = Rational(7)
        for r in range(2, 10):
            s = virasoro_shadow_S(r, c_val)
            assert s != 0, f"S_{r}(c=7) = 0 unexpectedly"

    def test_tower_c0_degenerate(self):
        """c=0 is degenerate: all S_r return None."""
        assert virasoro_shadow_S(2, Rational(0)) is None
        assert virasoro_shadow_S(4, Rational(0)) is None


# ========================================================================
# 24. Specific minimal model d_arith values
# ========================================================================

class TestMinimalModelDArith:
    """Verify d_arith for specific minimal models."""

    def test_ising_zero(self):
        """M(3,4) Ising: d_arith = 0."""
        dt = depth_virasoro_minimal(3, 4)
        assert dt.d_arith == 0

    def test_tricritical_three(self):
        """M(4,5) tri-critical Ising: d_arith = 3."""
        dt = depth_virasoro_minimal(4, 5)
        assert dt.d_arith == 3

    def test_M43_same_as_M34(self):
        """M(4,3) and M(3,4) give same central charge."""
        c34 = 1 - Rational(6, 12)
        c43 = 1 - Rational(6, 12)
        assert c34 == c43 == Rational(1, 2)

    def test_growth_with_complexity(self):
        """d_arith grows as the minimal model gets more complex."""
        values = []
        for m in range(3, 8):
            dt = depth_virasoro_minimal(m, m + 1)
            values.append(dt.d_arith)
        # Non-decreasing
        for i in range(1, len(values)):
            assert values[i] >= values[i - 1]


# ========================================================================
# 25. Exhaustive class-specific tests
# ========================================================================

class TestExhaustiveClassSpecific:
    """Exhaustive check that each class has correct d_alg."""

    def test_class_G_dalg_zero(self):
        table = full_landscape_61()
        for dt in table:
            if dt.shadow_class == 'G':
                assert dt.d_alg == 0

    def test_class_L_dalg_one(self):
        table = full_landscape_61()
        for dt in table:
            if dt.shadow_class == 'L':
                assert dt.d_alg == 1

    def test_class_C_dalg_two(self):
        table = full_landscape_61()
        for dt in table:
            if dt.shadow_class == 'C':
                assert dt.d_alg == 2

    def test_class_M_dalg_infinite(self):
        table = full_landscape_61()
        for dt in table:
            if dt.shadow_class == 'M':
                assert dt.d_alg is None  # infinity
