"""Tests for G/L/C/M depth classification and total depth decomposition.

Verifies:
    1. G/L/C/M classification for all 20 algebras
    2. Total depth formula d = 1 + d_arith + d_alg
    3. Kappa formulas computed from first principles (AP1)
    4. Delta = 8*kappa*S4 where applicable
    5. Cusp form dimension formula for SL(2,Z)
    6. Cross-checks against shadow_metric_census.py
    7. Lattice depth formula d = 3 + dim S_{r/2}
    8. Degenerate cases (kappa=0, weight-0 generators)
    9. Virasoro/W_N specific data
   10. Additivity and consistency cross-checks

Mathematical references:
    thm:depth-decomposition (arithmetic_shadows.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    def:shadow-depth-classification (higher_genus_modular_koszul.tex)
    eq:depth-cusp-formula (arithmetic_shadows.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import pytest

from sympy import Rational, oo, simplify

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from depth_classification import (
    DepthClassification,
    LIE_DATA,
    build_20_algebra_classification,
    classify_affine,
    classify_betagamma,
    classify_free_fermion,
    classify_glcm,
    classify_heisenberg_generic,
    classify_heisenberg_zero,
    classify_lattice,
    classify_virasoro,
    classify_w_infinity,
    classify_wN,
    dim_cusp_forms_sl2z,
    dim_modular_forms_sl2z,
    harmonic_number,
    kappa_affine,
    kappa_betagamma,
    kappa_free_fermion,
    kappa_heisenberg,
    kappa_lattice,
    kappa_virasoro,
    kappa_wN,
    summary_table,
    verify_all_class_consistency,
    verify_all_deltas,
    verify_all_depth_formulas,
)


# ========================================================================
# Fixture: build the 20-algebra list once
# ========================================================================

@pytest.fixture(scope='module')
def algebras():
    return build_20_algebra_classification()


# ========================================================================
# 1. G/L/C/M classification
# ========================================================================

class TestGLCMClassification:
    """Verify the G/L/C/M class assignment for each algebra."""

    def test_classify_G(self):
        """G: alpha = 0, Delta = 0."""
        cls, r, d = classify_glcm(0, 0)
        assert cls == 'G'
        assert r == 2
        assert d == 0

    def test_classify_L(self):
        """L: alpha != 0, Delta = 0."""
        cls, r, d = classify_glcm(1, 0)
        assert cls == 'L'
        assert r == 3
        assert d == 1

    def test_classify_C(self):
        """C: alpha = 0, Delta != 0."""
        cls, r, d = classify_glcm(0, 1)
        assert cls == 'C'
        assert r == 4
        assert d == 2

    def test_classify_M(self):
        """M: alpha != 0, Delta != 0."""
        cls, r, d = classify_glcm(1, 1)
        assert cls == 'M'
        assert r is None
        assert d is None

    def test_heisenberg_is_G(self):
        a = classify_heisenberg_generic(1)
        assert a.depth_class == 'G'
        assert a.r_max == 2

    def test_free_fermion_is_G(self):
        a = classify_free_fermion()
        assert a.depth_class == 'G'
        assert a.r_max == 2

    def test_affine_sl2_is_L(self):
        a = classify_affine('sl2', 1)
        assert a.depth_class == 'L'
        assert a.r_max == 3

    def test_affine_sl3_is_L(self):
        a = classify_affine('sl3', 1)
        assert a.depth_class == 'L'
        assert a.r_max == 3

    def test_affine_G2_is_L(self):
        a = classify_affine('G2', 1)
        assert a.depth_class == 'L'
        assert a.r_max == 3

    def test_affine_E8_is_L(self):
        a = classify_affine('E8', 1)
        assert a.depth_class == 'L'
        assert a.r_max == 3

    def test_lattice_D4_is_G(self):
        a = classify_lattice(4, 'D_4')
        assert a.depth_class == 'G'
        assert a.r_max == 2

    def test_lattice_E8_is_G(self):
        a = classify_lattice(8, 'E_8')
        assert a.depth_class == 'G'
        assert a.r_max == 2

    def test_lattice_Leech_is_G(self):
        a = classify_lattice(24, 'Leech')
        assert a.depth_class == 'G'
        assert a.r_max == 2

    def test_betagamma_lam1_is_C(self):
        a = classify_betagamma(1)
        assert a.depth_class == 'C'
        assert a.r_max == 4

    def test_betagamma_lam_half_is_C(self):
        a = classify_betagamma(Rational(1, 2))
        assert a.depth_class == 'C'
        assert a.r_max == 4

    def test_betagamma_lam0_is_class_C_but_flagged(self):
        a = classify_betagamma(0)
        assert a.depth_class == 'C'
        assert a.r_max == 4
        assert a.d_alg == 2
        assert a.degenerate

    def test_virasoro_is_M(self):
        a = classify_virasoro(1)
        assert a.depth_class == 'M'
        assert a.r_max is None

    def test_virasoro_c0_is_M(self):
        """Virasoro at c=0 is still class M (alpha=2, Delta!=0)."""
        a = classify_virasoro(0)
        assert a.depth_class == 'M'
        assert a.degenerate

    def test_virasoro_c26_is_M(self):
        a = classify_virasoro(26)
        assert a.depth_class == 'M'
        assert a.r_max is None

    def test_w3_is_M(self):
        a = classify_wN(3, 50)
        assert a.depth_class == 'M'
        assert a.r_max is None

    def test_w4_is_M(self):
        a = classify_wN(4, 50)
        assert a.depth_class == 'M'
        assert a.r_max is None

    def test_w_infinity_is_M(self):
        a = classify_w_infinity()
        assert a.depth_class == 'M'

    def test_all_class_consistency(self, algebras):
        results = verify_all_class_consistency(algebras)
        for name, ok in results.items():
            assert ok, f"Class inconsistency for {name}"


# ========================================================================
# 2. Depth formula d = 1 + d_arith + d_alg
# ========================================================================

class TestDepthFormula:
    """Verify d = 1 + d_arith + d_alg for each algebra."""

    def test_all_depth_formulas(self, algebras):
        results = verify_all_depth_formulas(algebras)
        for name, ok in results.items():
            assert ok, f"Depth formula fails for {name}"

    def test_heisenberg_depth(self):
        a = classify_heisenberg_generic(1)
        assert a.d_total == 2
        assert a.d_alg == 0
        assert a.d_arith == 1
        assert a.d_total == 1 + a.d_arith + a.d_alg

    def test_heisenberg_zero_depth(self):
        a = classify_heisenberg_zero()
        assert a.d_total == 1
        assert a.d_alg == 0
        assert a.d_arith == 0

    def test_free_fermion_depth(self):
        a = classify_free_fermion()
        assert a.d_total == 2
        assert a.d_alg == 0
        assert a.d_arith == 1

    def test_affine_depth(self):
        for lie_type in ['sl2', 'sl3', 'G2', 'E8']:
            a = classify_affine(lie_type, 1)
            assert a.d_total == 3, f"depth({lie_type}) should be 3"
            assert a.d_alg == 1
            assert a.d_arith == 1

    def test_lattice_E8_depth(self):
        """E_8 lattice (rank 8, even unimodular): d = 3 + dim S_4 = 3 + 0 = 3."""
        a = classify_lattice(8, 'E_8')
        assert a.d_total == 3
        assert a.d_arith == 2
        assert a.d_alg == 0

    def test_lattice_Leech_depth(self):
        """Leech lattice (rank 24): d = 3 + dim S_12 = 3 + 1 = 4."""
        a = classify_lattice(24, 'Leech')
        assert a.d_total == 4
        assert a.d_arith == 3
        assert a.d_alg == 0

    def test_lattice_rank48_depth(self):
        """Rank-48 lattice: d = 3 + dim S_24 = 3 + 2 = 5."""
        a = classify_lattice(48, 'rank-48')
        assert a.d_total == 5
        assert a.d_arith == 4
        assert a.d_alg == 0

    def test_lattice_rank72_depth(self):
        """Rank-72 lattice: d = 3 + dim S_36 = 3 + 3 = 6."""
        a = classify_lattice(72, 'rank-72')
        assert a.d_total == 6
        assert a.d_arith == 5
        assert a.d_alg == 0

    def test_lattice_rank96_depth(self):
        """Rank-96 lattice: d = 3 + dim S_48 = 3 + 4 = 7."""
        a = classify_lattice(96, 'rank-96')
        assert a.d_total == 7
        assert a.d_arith == 6
        assert a.d_alg == 0

    def test_betagamma_depth(self):
        a = classify_betagamma(1)
        assert a.d_total == 4
        assert a.d_alg == 2
        assert a.d_arith == 1

    def test_virasoro_infinite_depth(self):
        a = classify_virasoro(1)
        assert a.d_total is None  # infinity
        assert a.d_alg is None   # infinity

    def test_wN_infinite_depth(self):
        a = classify_wN(3, 50)
        assert a.d_total is None
        assert a.d_alg is None

    def test_class_G_has_dalg_0(self, algebras):
        for a in algebras:
            if a.depth_class == 'G':
                assert a.d_alg == 0, f"{a.name}: class G should have d_alg=0"

    def test_class_L_has_dalg_1(self, algebras):
        for a in algebras:
            if a.depth_class == 'L':
                assert a.d_alg == 1, f"{a.name}: class L should have d_alg=1"

    def test_class_C_has_dalg_2(self, algebras):
        for a in algebras:
            if a.depth_class == 'C':
                assert a.d_alg == 2, f"{a.name}: class C should have d_alg=2"

    def test_class_M_has_dalg_infinity(self, algebras):
        for a in algebras:
            if a.depth_class == 'M':
                assert a.d_alg is None, f"{a.name}: class M should have d_alg=None (infinity)"


# ========================================================================
# 3. Kappa formulas (AP1: verify from first principles)
# ========================================================================

class TestKappaFormulas:
    """Verify kappa computed from first principles for each family."""

    def test_kappa_heisenberg(self):
        assert kappa_heisenberg(1) == 1
        assert kappa_heisenberg(2) == 2
        assert kappa_heisenberg(Rational(1, 2)) == Rational(1, 2)

    def test_kappa_free_fermion(self):
        """kappa(free fermion) = c/2 = 1/4. NOT kappa = k."""
        assert kappa_free_fermion() == Rational(1, 4)

    def test_kappa_lattice(self):
        assert kappa_lattice(4) == 4
        assert kappa_lattice(8) == 8
        assert kappa_lattice(24) == 24

    def test_kappa_affine_sl2(self):
        """kappa(sl_2, k) = 3(k+2)/4. dim=3, h^v=2."""
        assert kappa_affine(3, 2, 1) == Rational(9, 4)
        assert kappa_affine(3, 2, 2) == 3
        assert kappa_affine(3, 2, 0) == Rational(3, 2)

    def test_kappa_affine_sl3(self):
        """kappa(sl_3, k) = 8(k+3)/6 = 4(k+3)/3. dim=8, h^v=3."""
        assert kappa_affine(8, 3, 1) == Rational(32, 6)
        assert simplify(kappa_affine(8, 3, 1) - Rational(16, 3)) == 0

    def test_kappa_affine_G2(self):
        """kappa(G_2, k) = 14(k+4)/8 = 7(k+4)/4. dim=14, h^v=4."""
        assert kappa_affine(14, 4, 1) == Rational(35, 4)

    def test_kappa_affine_E8(self):
        """kappa(E_8, k) = 248(k+30)/60. dim=248, h^v=30."""
        kap = kappa_affine(248, 30, 1)
        assert kap == Rational(248 * 31, 60)
        assert kap == Rational(7688, 60)
        assert simplify(kap - Rational(1922, 15)) == 0

    def test_kappa_virasoro(self):
        assert kappa_virasoro(1) == Rational(1, 2)
        assert kappa_virasoro(26) == 13
        assert kappa_virasoro(0) == 0

    def test_kappa_betagamma_standard(self):
        """Standard betagamma (lambda=0 or 1): kappa = 1."""
        assert kappa_betagamma(0) == 1
        assert kappa_betagamma(1) == 1

    def test_kappa_betagamma_symplectic(self):
        """Symplectic (lambda=1/2): kappa = -1/2."""
        assert kappa_betagamma(Rational(1, 2)) == Rational(-1, 2)

    def test_kappa_w3(self):
        """kappa(W_3, c) = (H_3 - 1)*c = (1/2 + 1/3)*c = 5c/6."""
        assert kappa_wN(3, 6) == 5
        assert kappa_wN(3, 12) == 10

    def test_kappa_w4(self):
        """kappa(W_4, c) = (H_4 - 1)*c = (1/2 + 1/3 + 1/4)*c = 13c/12."""
        assert kappa_wN(4, 12) == 13

    def test_kappa_cross_check_with_census(self):
        """Cross-check: kappa(Vir, c) = c/2 should NOT equal kappa(KM, level)
        at the same level. These are DIFFERENT formulas (AP1)."""
        kap_vir = kappa_virasoro(1)
        kap_sl2 = kappa_affine(3, 2, 1)
        assert kap_vir != kap_sl2  # c/2 != 3(k+2)/4 at k=1, c=1

    def test_kappa_not_c_over_2_for_km(self):
        """AP1: kappa(KM) != c/2 in general. Only Virasoro uses kappa = c/2."""
        c_sl2_k1 = Rational(3) * 1 / (1 + 2)  # c = dim*k/(k+h^v) = 3*1/3 = 1
        kap_correct = kappa_affine(3, 2, 1)  # 9/4
        kap_wrong = c_sl2_k1 / 2  # 1/2
        assert kap_correct != kap_wrong

    def test_kappa_heisenberg_not_c_over_2(self):
        """AP1: kappa(Heis, k) = k, NOT c/2. For Heisenberg, c = k, so
        kappa = k = c. kappa = c/2 is WRONG for Heisenberg."""
        # Heisenberg at k=1: c = 1, kappa = 1. NOT kappa = 1/2.
        assert kappa_heisenberg(1) == 1
        assert kappa_heisenberg(1) != Rational(1, 2)


# ========================================================================
# 4. Delta = 8*kappa*S4
# ========================================================================

class TestDeltaIdentity:

    def test_all_deltas(self, algebras):
        results = verify_all_deltas(algebras)
        for name, ok in results.items():
            assert ok, f"Delta identity fails for {name}"

    def test_virasoro_delta(self):
        """Delta = 40/(5c+22) for Virasoro."""
        a = classify_virasoro(1)
        assert a.delta == Rational(40, 27)
        expected = 8 * Rational(1, 2) * Rational(10, 27)
        assert simplify(a.delta - expected) == 0

    def test_virasoro_delta_c26(self):
        """Delta = 40/(5*26+22) = 40/152 = 5/19."""
        a = classify_virasoro(26)
        assert a.delta == Rational(40, 152)
        assert simplify(a.delta - Rational(5, 19)) == 0

    def test_affine_delta_zero(self):
        """All affine KM have Delta = 0 (Jacobi kills quartic)."""
        for lie_type in ['sl2', 'sl3', 'G2', 'E8']:
            a = classify_affine(lie_type, 1)
            assert a.delta == 0

    def test_heisenberg_delta_zero(self):
        a = classify_heisenberg_generic(1)
        assert a.delta == 0

    def test_lattice_delta_zero(self):
        for rank in [4, 8, 24]:
            a = classify_lattice(rank)
            assert a.delta == 0


# ========================================================================
# 5. Cusp form dimensions
# ========================================================================

class TestCuspFormDimensions:
    """Verify dim S_k(SL(2,Z)) against known values."""

    def test_small_weights(self):
        """dim S_k = 0 for k < 12."""
        for k in range(0, 12, 2):
            assert dim_cusp_forms_sl2z(k) == 0, f"dim S_{k} should be 0"

    def test_k12(self):
        """dim S_12 = 1 (Ramanujan Delta)."""
        assert dim_cusp_forms_sl2z(12) == 1

    def test_k24(self):
        """dim S_24 = 2."""
        assert dim_cusp_forms_sl2z(24) == 2

    def test_k36(self):
        """dim S_36 = 3."""
        assert dim_cusp_forms_sl2z(36) == 3

    def test_k48(self):
        """dim S_48 = 4."""
        assert dim_cusp_forms_sl2z(48) == 4

    def test_k14(self):
        """dim S_14 = 0 (14 % 12 = 2, dim M_14 = 1)."""
        assert dim_cusp_forms_sl2z(14) == 0

    def test_k16(self):
        """dim S_16 = 1."""
        assert dim_cusp_forms_sl2z(16) == 1

    def test_k18(self):
        """dim S_18 = 1."""
        assert dim_cusp_forms_sl2z(18) == 1

    def test_k20(self):
        """dim S_20 = 1."""
        assert dim_cusp_forms_sl2z(20) == 1

    def test_k22(self):
        """dim S_22 = 1."""
        assert dim_cusp_forms_sl2z(22) == 1

    def test_odd_weights_zero(self):
        """dim S_k = 0 for k odd."""
        for k in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]:
            assert dim_cusp_forms_sl2z(k) == 0

    def test_dim_M_k(self):
        """Verify dim M_k agrees with known values."""
        known = {
            0: 1, 2: 0, 4: 1, 6: 1, 8: 1, 10: 1,
            12: 2, 14: 1, 16: 2, 18: 2, 20: 2, 22: 2,
            24: 3, 26: 2, 28: 3, 30: 3, 32: 3, 34: 3,
            36: 4, 48: 5,
        }
        for k, expected in known.items():
            assert dim_modular_forms_sl2z(k) == expected, \
                f"dim M_{k} should be {expected}, got {dim_modular_forms_sl2z(k)}"

    def test_dim_S_equals_dim_M_minus_1(self):
        """For k >= 4, k even: dim S_k = dim M_k - 1."""
        for k in range(4, 100, 2):
            assert dim_cusp_forms_sl2z(k) == dim_modular_forms_sl2z(k) - 1


# ========================================================================
# 6. Cross-checks against shadow_metric_census.py
# ========================================================================

class TestCrossCheckCensus:
    """Cross-check against existing shadow_metric_census.py data."""

    def test_virasoro_S4(self):
        """Q^contact_Vir = 10/[c(5c+22)]."""
        a = classify_virasoro(1)
        assert a.S4 == Rational(10, 27)

    def test_virasoro_alpha(self):
        """Virasoro cubic alpha = 2."""
        a = classify_virasoro(1)
        assert a.alpha == 2

    def test_heisenberg_all_zero(self):
        """Heisenberg: alpha=0, S4=0, Delta=0."""
        a = classify_heisenberg_generic(1)
        assert a.alpha == 0
        assert a.S4 == 0
        assert a.delta == 0

    def test_affine_S4_zero(self):
        """All affine: S_4 = 0 (Jacobi identity)."""
        for lie_type in ['sl2', 'sl3', 'G2', 'E8']:
            a = classify_affine(lie_type, 1)
            assert a.S4 == 0


# ========================================================================
# 7. Lattice depth formula
# ========================================================================

class TestLatticeDepthFormula:
    """Verify d(V_Lambda) = 3 + dim S_{r/2} for even unimodular lattices."""

    @pytest.mark.parametrize("rank,expected_depth", [
        (8, 3),    # dim S_4 = 0, d = 3
        (16, 3),   # dim S_8 = 0, d = 3
        (24, 4),   # dim S_12 = 1, d = 4
        (32, 4),   # dim S_16 = 1, d = 4
        (48, 5),   # dim S_24 = 2, d = 5
        (72, 6),   # dim S_36 = 3, d = 6
        (96, 7),   # dim S_48 = 4, d = 7
    ])
    def test_lattice_depth_by_rank(self, rank, expected_depth):
        a = classify_lattice(rank)
        assert a.d_total == expected_depth, \
            f"rank {rank}: d should be {expected_depth}, got {a.d_total}"

    @pytest.mark.parametrize("rank,expected_darith", [
        (8, 2),    # 2 + dim S_4 = 2 + 0
        (16, 2),   # 2 + dim S_8 = 2 + 0
        (24, 3),   # 2 + dim S_12 = 2 + 1
        (48, 4),   # 2 + dim S_24 = 2 + 2
        (72, 5),   # 2 + dim S_36 = 2 + 3
    ])
    def test_lattice_darith_by_rank(self, rank, expected_darith):
        a = classify_lattice(rank)
        assert a.d_arith == expected_darith

    def test_all_lattice_dalg_zero(self):
        """All lattice VOAs have d_alg = 0 (abelian primary line)."""
        for rank in [4, 8, 16, 24, 32, 48, 72, 96]:
            a = classify_lattice(rank)
            assert a.d_alg == 0

    def test_lattice_depth_formula_identity(self):
        """Verify d = 3 + dim S_{r/2} matches d = 1 + d_arith + d_alg."""
        for rank in [8, 16, 24, 32, 48, 72, 96]:
            a = classify_lattice(rank)
            k = rank // 2
            dim_S = dim_cusp_forms_sl2z(k)
            assert a.d_total == 3 + dim_S
            assert a.d_total == 1 + a.d_arith + a.d_alg


# ========================================================================
# 8. Degenerate cases
# ========================================================================

class TestDegenerateCases:
    """Test degenerate algebras (kappa=0, weight-0 generators)."""

    def test_heisenberg_zero_is_degenerate(self):
        a = classify_heisenberg_zero()
        assert a.degenerate
        assert a.kappa == 0

    def test_virasoro_c0_is_degenerate(self):
        """Virasoro c=0: kappa=0, uncurved. Still class M."""
        a = classify_virasoro(0)
        assert a.degenerate
        assert a.kappa == 0
        assert a.depth_class == 'M'

    def test_betagamma_lam0_degenerate(self):
        """betagamma lambda=0: weight-0 generator (AP18)."""
        a = classify_betagamma(0)
        assert a.degenerate
        assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
        assert a.depth_class == 'C'
        assert a.d_alg == 2

    def test_ap31_kappa_zero_not_theta_zero(self):
        """AP31: kappa = 0 does NOT imply Theta_A = 0.

        For Virasoro c=0: kappa=0, alpha=2, Delta=40/22. The tower
        is still infinite (class M). Higher-arity shadows may be nonzero.
        """
        a = classify_virasoro(0)
        assert a.kappa == 0
        assert a.depth_class == 'M'  # NOT class G!
        assert a.r_max is None  # infinite tower


# ========================================================================
# 9. Virasoro/W_N specific data
# ========================================================================

class TestVirasoroWN:

    def test_virasoro_koszul_dual(self):
        """Virasoro: Vir_c^! = Vir_{26-c}. kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        kap_c1 = kappa_virasoro(1)
        kap_c25 = kappa_virasoro(25)
        assert kap_c1 + kap_c25 == 13

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro is self-dual at c=13 (AP8)."""
        kap = kappa_virasoro(13)
        assert kap == Rational(13, 2)
        # Self-duality: kappa(Vir_13) + kappa(Vir_{26-13}) = kappa(Vir_13) + kappa(Vir_13) = 13.
        assert 2 * kap == 13

    def test_virasoro_delta_nonzero_generic(self):
        """Delta = 40/(5c+22) != 0 for c != -22/5."""
        for c_val in [1, 2, 10, 13, 26]:
            a = classify_virasoro(c_val)
            assert a.delta != 0

    def test_w3_kappa_formula(self):
        """kappa(W_3, c) = 5c/6."""
        a = classify_wN(3, 6)
        assert a.kappa == 5

    def test_w4_kappa_formula(self):
        """kappa(W_4, c) = 13c/12."""
        a = classify_wN(4, 12)
        assert a.kappa == 13

    def test_wN_t_line_autonomous(self):
        """W_N T-line data = Virasoro data (autonomous)."""
        c_val = 50
        vir = classify_virasoro(c_val)
        for n in [3, 4, 5]:
            wn = classify_wN(n, c_val)
            assert wn.alpha == vir.alpha
            assert wn.S4 == vir.S4
            assert wn.delta == vir.delta

    def test_wN_kappa_increases_with_N(self):
        """kappa(W_N) = (H_N - 1)*c increases with N."""
        c_val = 10
        kappas = [classify_wN(n, c_val).kappa for n in range(3, 8)]
        for i in range(len(kappas) - 1):
            assert kappas[i] < kappas[i + 1]

    def test_harmonic_number(self):
        assert harmonic_number(1) == 1
        assert harmonic_number(2) == Rational(3, 2)
        assert harmonic_number(3) == Rational(11, 6)
        assert harmonic_number(4) == Rational(25, 12)

    def test_w_infinity_kappa_diverges(self):
        a = classify_w_infinity()
        assert a.kappa == oo


# ========================================================================
# 10. Additivity and consistency cross-checks
# ========================================================================

class TestConsistency:
    """Cross-family consistency tests (AP10: multi-path verification)."""

    def test_20_algebras_complete(self, algebras):
        """Verify we have exactly 20 algebras."""
        assert len(algebras) == 20

    def test_class_distribution(self, algebras):
        """Count class distribution."""
        counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
        for a in algebras:
            counts[a.depth_class] += 1
        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
        #           L=4 (sl2, sl3, G2, E8 affine)
        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
        #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
        assert counts['G'] == 6
        assert counts['L'] == 4
        assert counts['C'] == 3
        assert counts['M'] == 7

    def test_no_class_G_has_infinite_depth(self, algebras):
        for a in algebras:
            if a.depth_class == 'G':
                assert a.d_total is not None, f"{a.name}: class G should have finite depth"

    def test_no_class_L_has_infinite_depth(self, algebras):
        for a in algebras:
            if a.depth_class == 'L':
                assert a.d_total is not None

    def test_all_class_M_have_infinite_depth(self, algebras):
        for a in algebras:
            if a.depth_class == 'M':
                assert a.d_total is None, f"{a.name}: class M should have infinite depth"

    def test_r_max_consistent_with_class(self, algebras):
        expected = {'G': 2, 'L': 3, 'C': 4, 'M': None}
        for a in algebras:
            assert a.r_max == expected[a.depth_class], \
                f"{a.name}: r_max should be {expected[a.depth_class]}, got {a.r_max}"

    def test_kappa_additivity_heisenberg(self):
        """kappa(H_{k1} x H_{k2}) = kappa(H_{k1}) + kappa(H_{k2}) = k1 + k2."""
        k1, k2 = 3, 5
        assert kappa_heisenberg(k1) + kappa_heisenberg(k2) == kappa_heisenberg(k1 + k2)

    def test_kappa_lattice_is_rank(self):
        """kappa(V_Lambda) = rank(Lambda), not c/2."""
        # E_8 lattice: rank=8, c=8. kappa = rank = 8. kappa = c/2 would give 4.
        assert kappa_lattice(8) == 8
        assert kappa_lattice(8) != Rational(8, 2)  # NOT c/2

    def test_depth_monotonic_in_lattice_rank(self):
        """Total depth is non-decreasing in lattice rank (for even unimodular)."""
        ranks = [8, 16, 24, 32, 48, 72, 96]
        depths = [classify_lattice(r).d_total for r in ranks]
        for i in range(len(depths) - 1):
            assert depths[i] <= depths[i + 1], \
                f"depth at rank {ranks[i]} = {depths[i]} > depth at rank {ranks[i+1]} = {depths[i+1]}"

    def test_betagamma_kappa_formula_quadratic(self):
        """kappa(bg, lambda) = 6*lambda^2 - 6*lambda + 1 is a quadratic.

        Verify at several points to catch AP1-type copy errors.
        """
        test_points = {
            0: 1,
            1: 1,
            Rational(1, 2): Rational(-1, 2),
            Rational(1, 3): Rational(-1, 3),
            2: 13,
            -1: 13,
        }
        for lam, expected in test_points.items():
            assert kappa_betagamma(lam) == expected, \
                f"kappa(bg, {lam}) should be {expected}"

    def test_summary_table_printable(self, algebras):
        """Verify the summary table doesn't crash."""
        table = summary_table(algebras)
        assert len(table) > 0
        assert 'Heisenberg' in table
        assert 'Virasoro' in table


# ========================================================================
# 11. Lie algebra data consistency
# ========================================================================

class TestLieData:
    """Verify Lie algebra data for kappa computation."""

    def test_sl2_data(self):
        assert LIE_DATA['sl2']['dim'] == 3
        assert LIE_DATA['sl2']['h_dual'] == 2

    def test_sl3_data(self):
        assert LIE_DATA['sl3']['dim'] == 8
        assert LIE_DATA['sl3']['h_dual'] == 3

    def test_G2_data(self):
        assert LIE_DATA['G2']['dim'] == 14
        assert LIE_DATA['G2']['h_dual'] == 4

    def test_E8_data(self):
        assert LIE_DATA['E8']['dim'] == 248
        assert LIE_DATA['E8']['h_dual'] == 30

    def test_D4_data(self):
        assert LIE_DATA['D4']['dim'] == 28
        assert LIE_DATA['D4']['h_dual'] == 6

    def test_kappa_affine_formula_consistency(self):
        """Verify kappa = dim*(k+h^v)/(2*h^v) for several families."""
        for name, data in LIE_DATA.items():
            d, h = data['dim'], data['h_dual']
            for k in [1, 2, 3]:
                kap = kappa_affine(d, h, k)
                expected = Rational(d) * (Rational(k) + Rational(h)) / (2 * Rational(h))
                assert simplify(kap - expected) == 0, \
                    f"kappa({name}, k={k}) mismatch"


# ========================================================================
# 12. Depth decomposition edge cases
# ========================================================================

class TestEdgeCases:
    """Test edge cases and boundary behavior."""

    def test_d_total_at_least_1(self, algebras):
        """d >= 1 for all algebras (from the +1 offset)."""
        for a in algebras:
            if a.d_total is not None:
                assert a.d_total >= 1, f"{a.name}: d should be >= 1"

    def test_d_arith_non_negative(self, algebras):
        for a in algebras:
            assert a.d_arith >= 0, f"{a.name}: d_arith should be >= 0"

    def test_d_alg_values(self, algebras):
        """d_alg in {0, 1, 2, None (infinity)}."""
        valid = {0, 1, 2, None}
        for a in algebras:
            assert a.d_alg in valid, f"{a.name}: d_alg = {a.d_alg} not in {valid}"

    def test_infinite_depth_iff_class_M(self, algebras):
        for a in algebras:
            if a.depth_class == 'M':
                assert a.d_total is None
            else:
                assert a.d_total is not None

    def test_cusp_dim_0_for_rank_8_and_16(self):
        """No cusp forms in weights 4 and 8 for SL(2,Z)."""
        assert dim_cusp_forms_sl2z(4) == 0
        assert dim_cusp_forms_sl2z(8) == 0

    def test_first_cusp_form_at_weight_12(self):
        """Ramanujan Delta is the first cusp form, at weight 12."""
        for k in range(0, 12, 2):
            assert dim_cusp_forms_sl2z(k) == 0
        assert dim_cusp_forms_sl2z(12) == 1

    def test_betagamma_symplectic_negative_kappa(self):
        """betagamma at lambda=1/2 has negative kappa = -1/2."""
        a = classify_betagamma(Rational(1, 2))
        assert a.kappa < 0
        assert a.kappa == Rational(-1, 2)


# ========================================================================
# 13. W_N Delta consistency
# ========================================================================

class TestWNDeltaConsistency:
    """Verify that W_N Delta is computed from T-line kappa, not full kappa."""

    def test_wN_delta_equals_virasoro_delta(self):
        """W_N Delta on T-line = Virasoro Delta (autonomous)."""
        for c_val in [1, 2, 10, 26, 50]:
            vir = classify_virasoro(c_val)
            for n in [3, 4, 5]:
                wn = classify_wN(n, c_val)
                assert wn.delta == vir.delta, \
                    f"W_{n} at c={c_val}: Delta should match Virasoro"

    def test_wN_delta_is_40_over_5c_plus_22(self):
        """Explicit check: Delta = 40/(5c+22)."""
        for c_val in [1, 10, 50]:
            c = Rational(c_val)
            expected = Rational(40) / (5 * c + 22)
            wn = classify_wN(3, c_val)
            assert wn.delta == expected

    def test_wN_kappa_differs_from_virasoro_kappa(self):
        """W_N full kappa != Virasoro kappa (unless N=2, i.e. Virasoro itself)."""
        c_val = 10
        vir_kap = kappa_virasoro(c_val)  # 5
        for n in [3, 4, 5]:
            wn_kap = classify_wN(n, c_val).kappa
            assert wn_kap != vir_kap, \
                f"W_{n} kappa should differ from Virasoro kappa"
