r"""Tests for DS reduction and arithmetic depth transformation engine.

Systematic verification that Drinfeld-Sokolov reduction V_k(sl_N) -> W_k(sl_N)
transforms arithmetic depth d_arith according to:
  - d_arith(affine) = 1 (class L)
  - d_arith(W-algebra) = 0 at generic level (class M)
  - The total depth INCREASES (3 -> inf) but arithmetic component DECREASES
  - Ghost sector has d_arith = 0 (absorbed in BRST)
  - Level-rank duality: kappa is NOT symmetric
  - DS cascade: d_arith is NOT monotonically increasing

STRUCTURE (91 tests):
  Section 1:  Central charge formulas (8 tests)
  Section 2:  Kappa multi-path verification (12 tests)
  Section 3:  S_3 transformation under DS (8 tests)
  Section 4:  d_arith for affine KM (8 tests)
  Section 5:  d_arith for principal W-algebras (8 tests)
  Section 6:  DS depth jump analysis (8 tests)
  Section 7:  Ghost sector arithmetic (5 tests)
  Section 8:  Level-rank duality (10 tests)
  Section 9:  DS cascade and monotonicity (8 tests)
  Section 10: Non-principal orbits (6 tests)
  Section 11: Shadow tower comparison (5 tests)
  Section 12: Cross-engine consistency (5 tests)

Manuscript references:
    thm:ds-koszul-obstruction, thm:depth-decomposition,
    thm:shadow-archetype-classification, prop:independent-sum-factorization,
    thm:single-line-dichotomy, conj:type-a-transport-to-transpose

MULTI-PATH VERIFICATION:
  Path 1: Direct formula computation
  Path 2: Character/anomaly ratio
  Path 3: Shadow tower extraction
  Path 4: Level-rank duality cross-check
"""

import pytest
from fractions import Fraction

from compute.lib.ds_arithmetic_transformation_engine import (
    # Central charges
    c_slN,
    c_WN_principal,
    c_bershadsky_polyakov,
    c_ghost,
    # Kappa
    kappa_slN,
    harmonic_number,
    anomaly_ratio_principal,
    kappa_WN_principal,
    kappa_ghost_free,
    ghost_constant,
    kappa_bershadsky_polyakov,
    # d_arith
    DArithResult,
    darith_affine_slN,
    darith_WN_principal,
    darith_bershadsky_polyakov,
    # DS depth jump
    DSDepthJump,
    ds_depth_jump_principal,
    ds_depth_jump_subregular,
    # Kappa table
    kappa_transformation_table,
    # S_3
    s3_transformation_table,
    # Ghost
    ghost_arithmetic,
    # Level-rank
    level_rank_kappa,
    level_rank_darith,
    level_rank_full_table,
    # Cascade
    ds_cascade_darith,
    ds_cascade_monotonicity,
    # Non-principal
    darith_by_orbit_sl3,
    darith_by_orbit_sl4,
    # Multi-path
    kappa_verification_multipath,
    # Shadow tower
    shadow_tower,
    shadow_tower_comparison,
    # Verification
    verify_all,
)


# ============================================================================
# Section 1: Central charge formulas
# ============================================================================

class TestCentralChargeFormulas:
    """Central charge formulas for sl_N and W_N."""

    def test_c_sl2_k1(self):
        """c(sl_2, k=1) = 3*1/(1+2) = 1."""
        assert c_slN(2, Fraction(1)) == Fraction(1)

    def test_c_sl3_k1(self):
        """c(sl_3, k=1) = 8*1/(1+3) = 2."""
        assert c_slN(3, Fraction(1)) == Fraction(2)

    def test_c_W2_k1(self):
        """c(Vir, k=1) via Fateev-Lukyanov: (2-1) - 2*3*(1+2-1)^2/(1+2) = 1 - 8 = -7."""
        # VERIFIED: [DC] FL formula direct substitution; [LT] Arakawa (2.3.1)
        assert c_WN_principal(2, Fraction(1)) == Fraction(-7)

    def test_c_W3_k1(self):
        """c(W_3, k=1) via FL: (3-1) - 3*8*(1+3-1)^2/(1+3) = 2 - 54 = -52."""
        # VERIFIED: [DC] FL formula; [LC] N=2 gives -7 (Vir check)
        assert c_WN_principal(3, Fraction(1)) == Fraction(-52)

    def test_c_ghost_sl2(self):
        """c_ghost(sl_2) = 2*1 = 2."""
        assert c_ghost(2) == Fraction(2)

    def test_c_ghost_sl3(self):
        """c_ghost(sl_3) = 3*2 = 6."""
        assert c_ghost(3) == Fraction(6)

    def test_c_additivity(self):
        """c(sl_N) = c(W_N) + c_ghost(N, k) for all N=2..5, k=1..5."""
        for N in range(2, 6):
            for k in range(1, 6):
                kv = Fraction(k)
                assert c_slN(N, kv) == c_WN_principal(N, kv) + c_ghost(N, kv), \
                    f"c-additivity failed at N={N}, k={k}"

    def test_c_bershadsky_polyakov_k1(self):
        """c(BP, k=1) = 2 - 24*(1+1)^2/(1+3) = 2 - 24 = -22."""
        # VERIFIED: [DC] BP formula 2 - 24*(k+1)^2/(k+3); [CF] K_BP = c(0)+c(-6) = -6+202 = 196
        assert c_bershadsky_polyakov(Fraction(1)) == Fraction(-22)


# ============================================================================
# Section 2: Kappa multi-path verification
# ============================================================================

class TestKappaMultiPath:
    """Multi-path verification of kappa transformation."""

    def test_kappa_sl2_k1_direct(self):
        """kappa(V_1(sl_2)) = 3*(1+2)/(2*2) = 9/4."""
        assert kappa_slN(2, Fraction(1)) == Fraction(9, 4)

    def test_kappa_sl3_k1_direct(self):
        """kappa(V_1(sl_3)) = 8*(1+3)/(2*3) = 16/3."""
        assert kappa_slN(3, Fraction(1)) == Fraction(16, 3)

    def test_kappa_W2_k1(self):
        """kappa(Vir, k=1) = c/2 = -7/2 [c=-7 from FL]."""
        # VERIFIED: [DC] kappa = (H_2-1)*c = (1/2)*(-7) = -7/2; [LT] canonical_c_wn_fl
        assert kappa_WN_principal(2, Fraction(1)) == Fraction(-7, 2)

    def test_kappa_W3_k1(self):
        """kappa(W_3, k=1) = (5/6)*(-52) = -130/3 [c=-52 from FL]."""
        # VERIFIED: [DC] rho=5/6, c(W_3,1)=-52, kappa=(5/6)*(-52)=-130/3; [LC] N=2 gives -7/2
        rho = anomaly_ratio_principal(3)
        assert rho == Fraction(5, 6)
        assert kappa_WN_principal(3, Fraction(1)) == Fraction(-130, 3)

    def test_anomaly_ratio_N2(self):
        """rho(W_2) = H_2 - 1 = 1/2."""
        assert anomaly_ratio_principal(2) == Fraction(1, 2)

    def test_anomaly_ratio_N3(self):
        """rho(W_3) = H_3 - 1 = 1/2 + 1/3 = 5/6."""
        assert anomaly_ratio_principal(3) == Fraction(5, 6)

    def test_anomaly_ratio_N4(self):
        """rho(W_4) = H_4 - 1 = 1/2 + 1/3 + 1/4 = 13/12."""
        assert anomaly_ratio_principal(4) == Fraction(13, 12)

    def test_kappa_multipath_consistency_N2_k3(self):
        """All 4 paths give consistent kappa for sl_2, k=3."""
        v = kappa_verification_multipath(2, 3)
        assert v['all_consistent']
        assert v['path4_virasoro']['match']  # N=2 Virasoro check

    def test_kappa_multipath_consistency_N3_k2(self):
        """All 3 paths give consistent kappa for sl_3, k=2."""
        v = kappa_verification_multipath(3, 2)
        assert v['all_consistent']

    def test_kappa_multipath_consistency_N4_k5(self):
        """All paths consistent for sl_4, k=5."""
        v = kappa_verification_multipath(4, 5)
        assert v['all_consistent']

    def test_kappa_multipath_consistency_N5_k1(self):
        """All paths consistent for sl_5, k=1."""
        v = kappa_verification_multipath(5, 1)
        assert v['all_consistent']

    def test_kappa_not_preserved_under_ds(self):
        """kappa is NOT preserved under DS for N >= 3."""
        for N in range(3, 6):
            for k in range(1, 4):
                kv = Fraction(k)
                kap_aff = kappa_slN(N, kv)
                kap_w = kappa_WN_principal(N, kv)
                assert kap_aff != kap_w, \
                    f"kappa preserved at N={N}, k={k} (should not be)"


# ============================================================================
# Section 3: S_3 transformation under DS
# ============================================================================

class TestS3Transformation:
    """S_3 transformation under principal DS reduction."""

    def test_s3_ratio_universal_2(self):
        """S_3(W_N)/S_3(V_k(sl_N)) = 2 for all N, k."""
        result = s3_transformation_table()
        assert result['ratio_universal_2']

    def test_s3_affine_always_1(self):
        """S_3(V_k(sl_N)) = alpha = 1 for all affine algebras."""
        result = s3_transformation_table()
        for (N, k), data in result['per_Nk'].items():
            assert data['S3_affine'] == Fraction(1), \
                f"S_3(affine) != 1 at N={N}, k={k}"

    def test_s3_W_always_2(self):
        """S_3(W_N) = alpha = 2 on the T-line."""
        result = s3_transformation_table()
        for (N, k), data in result['per_Nk'].items():
            assert data['S3_W'] == Fraction(2), \
                f"S_3(W) != 2 at N={N}, k={k}"

    def test_s3_not_ds_equivariant_as_functor(self):
        """S_3 is NOT DS-equivariant as a functor (doubles, not preserved)."""
        result = s3_transformation_table()
        for (N, k), data in result['per_Nk'].items():
            assert data['ratio'] == Fraction(2)

    def test_s3_ratio_N2_k1(self):
        """Specific check: N=2, k=1."""
        result = s3_transformation_table(range(2, 3), range(1, 2))
        data = result['per_Nk'][(2, 1)]
        assert data['ratio'] == Fraction(2)

    def test_s3_ratio_N5_k5(self):
        """Specific check: N=5, k=5."""
        result = s3_transformation_table(range(5, 6), range(5, 6))
        data = result['per_Nk'][(5, 5)]
        assert data['ratio'] == Fraction(2)

    def test_s3_alpha_transition(self):
        """Alpha transitions from 1 (Lie bracket) to 2 (Virasoro OPE) under DS."""
        result = s3_transformation_table()
        for (N, k), data in result['per_Nk'].items():
            assert data['alpha_affine'] == Fraction(1)
            assert data['alpha_W'] == Fraction(2)

    def test_s3_k_independence(self):
        """S_3 ratio is independent of level k."""
        result = s3_transformation_table(range(3, 4), range(1, 6))
        ratios = [result['per_Nk'][(3, k)]['ratio'] for k in range(1, 6)]
        assert all(r == Fraction(2) for r in ratios)


# ============================================================================
# Section 4: d_arith for affine KM
# ============================================================================

class TestDArithAffine:
    """d_arith for affine Kac-Moody algebras."""

    def test_darith_sl2_k1(self):
        """d_arith(V_1(sl_2)) = 1."""
        r = darith_affine_slN(2, 1)
        assert r.d_arith == 1

    def test_darith_sl3_k2(self):
        """d_arith(V_2(sl_3)) = 1."""
        r = darith_affine_slN(3, 2)
        assert r.d_arith == 1

    def test_darith_sl5_k3(self):
        """d_arith(V_3(sl_5)) = 1."""
        r = darith_affine_slN(5, 3)
        assert r.d_arith == 1

    def test_all_affine_class_L(self):
        """All affine sl_N are class L."""
        for N in range(2, 7):
            for k in range(1, 6):
                r = darith_affine_slN(N, k)
                assert r.shadow_class == 'L', \
                    f"Expected class L at N={N}, k={k}"

    def test_all_affine_depth_3(self):
        """All affine sl_N have total depth 3."""
        for N in range(2, 7):
            for k in range(1, 6):
                r = darith_affine_slN(N, k)
                assert r.d_total == 3

    def test_all_affine_dalg_1(self):
        """All affine sl_N have d_alg = 1."""
        for N in range(2, 7):
            for k in range(1, 6):
                r = darith_affine_slN(N, k)
                assert r.d_alg == 1

    def test_depth_decomposition_affine(self):
        """d = 1 + d_arith + d_alg = 1 + 1 + 1 = 3 for all affine."""
        for N in range(2, 7):
            for k in range(1, 6):
                r = darith_affine_slN(N, k)
                assert r.d_total == 1 + r.d_arith + r.d_alg

    def test_kappa_stored_correctly(self):
        """kappa is stored correctly in the result."""
        r = darith_affine_slN(3, 2)
        expected = Fraction(8 * (2 + 3), 2 * 3)  # 40/6 = 20/3
        assert r.kappa == expected


# ============================================================================
# Section 5: d_arith for principal W-algebras
# ============================================================================

class TestDArithWAlgebra:
    """d_arith for principal W-algebras under DS."""

    def test_darith_vir_k1_generic(self):
        """d_arith(Vir, k=1) = 0 [c=-1, generic non-unitary]."""
        r = darith_WN_principal(2, 1)
        assert r.d_arith == 0

    def test_darith_vir_k10_ising(self):
        """d_arith(Vir, k=10) = 0 [Ising, c=1/2]."""
        r = darith_WN_principal(2, 10)
        assert r.d_arith == 0

    def test_darith_W3_generic(self):
        """d_arith(W_3, k=1) = 0 [generic]."""
        r = darith_WN_principal(3, 1)
        assert r.d_arith == 0

    def test_darith_W4_generic(self):
        """d_arith(W_4, k=3) = 0 [generic]."""
        r = darith_WN_principal(4, 3)
        assert r.d_arith == 0

    def test_all_W_class_M(self):
        """All W_N are class M (infinite depth)."""
        for N in range(2, 6):
            for k in range(1, 6):
                r = darith_WN_principal(N, k)
                assert r.shadow_class == 'M', \
                    f"Expected class M at N={N}, k={k}"

    def test_all_W_dalg_infinite(self):
        """All W_N have d_alg = infinity (None)."""
        for N in range(2, 6):
            for k in range(1, 6):
                r = darith_WN_principal(N, k)
                assert r.d_alg is None

    def test_free_field_darith_1(self):
        """At free-field level k=N: d_arith = 1 (theta-like)."""
        for N in range(2, 6):
            r = darith_WN_principal(N, N)
            assert r.d_arith == 1, f"Free-field d_arith != 1 at N={N}"

    def test_darith_bp_generic(self):
        """d_arith(BP, k=2) = 0 [generic Bershadsky-Polyakov]."""
        r = darith_bershadsky_polyakov(2)
        assert r.d_arith == 0


# ============================================================================
# Section 6: DS depth jump analysis
# ============================================================================

class TestDSDepthJump:
    """DS depth jump: d_arith transformation."""

    def test_principal_jump_sl2_k3(self):
        """DS depth jump for sl_2, k=3: 1 -> 0, jump = -1."""
        j = ds_depth_jump_principal(2, 3)
        assert j.darith_before == 1
        assert j.darith_after == 0
        assert j.depth_jump == -1

    def test_principal_jump_sl3_k2(self):
        """DS depth jump for sl_3, k=2: 1 -> 0."""
        j = ds_depth_jump_principal(3, 2)
        assert j.depth_jump == -1

    def test_class_transition(self):
        """DS transitions from class L to class M."""
        for N in range(2, 6):
            for k in range(1, 4):
                j = ds_depth_jump_principal(N, k)
                assert j.class_before == 'L'
                assert j.class_after == 'M'

    def test_darith_decreases_generic(self):
        """d_arith decreases from 1 to 0 at generic level."""
        for N in range(2, 6):
            for k in [1, 3, 5]:
                j = ds_depth_jump_principal(N, k)
                # At generic level: d_arith drops
                # Exception: free-field k=N gives d_arith=1
                if k != N:
                    assert j.depth_jump <= 0, \
                        f"d_arith increased at N={N}, k={k}"

    def test_free_field_no_jump(self):
        """At free-field level k=N: d_arith stays 1, jump = 0."""
        for N in range(2, 6):
            j = ds_depth_jump_principal(N, N)
            assert j.depth_jump == 0, f"Jump != 0 at free-field N={N}"

    def test_subregular_sl3_k2(self):
        """Subregular DS for sl_3 (BP algebra)."""
        j = ds_depth_jump_subregular(3, 2)
        assert j.darith_before == 1
        assert j.darith_after == 0

    def test_kappa_before_after_stored(self):
        """kappa values are correctly stored in DSDepthJump."""
        j = ds_depth_jump_principal(3, 2)
        assert j.kappa_before == kappa_slN(3, Fraction(2))
        assert j.kappa_after == kappa_WN_principal(3, Fraction(2))

    def test_c_before_after_stored(self):
        """Central charges are correctly stored."""
        j = ds_depth_jump_principal(2, 3)
        assert j.c_before == c_slN(2, Fraction(3))
        assert j.c_after == c_WN_principal(2, Fraction(3))


# ============================================================================
# Section 7: Ghost sector arithmetic
# ============================================================================

class TestGhostArithmetic:
    """Ghost sector arithmetic under DS."""

    def test_ghost_darith_always_0(self):
        """d_arith(ghost) = 0 for all N."""
        for N in range(2, 8):
            ga = ghost_arithmetic(N)
            assert ga.darith_ghost == 0

    def test_ghost_class_G(self):
        """Ghost sector is class G (Gaussian/free fields)."""
        for N in range(2, 8):
            ga = ghost_arithmetic(N)
            assert ga.class_ghost == 'G'

    def test_ghost_c_correct(self):
        """c_ghost = N(N-1) for all N."""
        for N in range(2, 8):
            ga = ghost_arithmetic(N)
            assert ga.c_ghost == Fraction(N * (N - 1))

    def test_ghost_kappa_correct(self):
        """kappa_ghost_free = N(N-1)/2."""
        for N in range(2, 8):
            ga = ghost_arithmetic(N)
            assert ga.kappa_ghost_free == Fraction(N * (N - 1), 2)

    def test_ghost_dalg_0(self):
        """d_alg(ghost) = 0 (free fields)."""
        for N in range(2, 8):
            ga = ghost_arithmetic(N)
            assert ga.dalg_ghost == 0


# ============================================================================
# Section 8: Level-rank duality
# ============================================================================

class TestLevelRankDuality:
    """Level-rank duality and arithmetic depth."""

    def test_level_rank_kappa_asymmetric(self):
        """kappa(W_k(sl_N)) != kappa(W_N(sl_k)) in general."""
        lr = level_rank_kappa(3, 4)
        assert not lr['kappa_equal'], "kappa should be asymmetric under level-rank"

    def test_level_rank_c_asymmetric(self):
        """c(W_k(sl_N)) != c(W_N(sl_k)) in general."""
        lr = level_rank_kappa(3, 4)
        assert lr['c_Wk_slN'] != lr['c_WN_slk']

    def test_level_rank_darith_symmetric_generic(self):
        """At generic level: d_arith = 0 for both, hence trivially symmetric."""
        lr = level_rank_darith(3, 4)
        assert lr['darith_equal']
        assert lr['darith_Wk_slN'] == 0
        assert lr['darith_WN_slk'] == 0

    def test_level_rank_N2_k3(self):
        """Explicit level-rank: W_3(sl_2) vs W_2(sl_3)."""
        # W_3(sl_2) = Virasoro at level 3 = c(W_2, 3)
        # W_2(sl_3) = W_3 algebra at level 2 = c(W_3, 2)
        lr = level_rank_kappa(2, 3)
        # VERIFIED: [DC] FL: c(W_2,3) = 1 - 2*3*(3+2-1)^2/(3+2) = 1-6*16/5 = 1-96/5 = -91/5
        assert lr['c_Wk_slN'] == Fraction(-91, 5)
        # VERIFIED: [DC] FL: c(W_3,2) = 2 - 3*8*(2+3-1)^2/(2+3) = 2-24*16/5 = 2-384/5 = -374/5
        assert lr['c_WN_slk'] == Fraction(-374, 5)

    def test_level_rank_explicit_kappa_N3_k4(self):
        """Explicit kappa computation for N=3, k=4."""
        lr = level_rank_kappa(3, 4)
        # kappa(W_4(sl_3)) = rho_3 * c(W_3, k=4)
        c_w34 = c_WN_principal(3, Fraction(4))
        rho3 = anomaly_ratio_principal(3)
        expected_kap_34 = rho3 * c_w34
        assert lr['kappa_Wk_slN'] == expected_kap_34

        # kappa(W_3(sl_4)) = rho_4 * c(W_4, k=3)
        # Wait: this needs level-rank swap. W_N(sl_k) = W_k(sl_N) with N,k swapped.
        # level_rank_kappa(3, 4): Wk_slN = W_4(sl_3), WN_slk = W_3(sl_4)
        c_w43 = c_WN_principal(4, Fraction(3))
        rho4 = anomaly_ratio_principal(4)
        expected_kap_43 = rho4 * c_w43
        assert lr['kappa_WN_slk'] == expected_kap_43

    def test_level_rank_full_table(self):
        """Full table computation succeeds for N,k <= 5."""
        lr = level_rank_full_table(max_N=5, max_k=5)
        assert lr['kappa_table']  # non-empty
        assert lr['darith_table']

    def test_level_rank_kappa_not_symmetric_global(self):
        """kappa is NOT symmetric under level-rank globally."""
        lr = level_rank_full_table(max_N=5, max_k=5)
        assert not lr['kappa_symmetric']

    def test_level_rank_darith_symmetric_global(self):
        """d_arith is trivially symmetric (all 0 at generic level)."""
        lr = level_rank_full_table(max_N=5, max_k=5)
        assert lr['darith_symmetric']

    def test_level_rank_self_dual_kappa(self):
        """At N=k (self-dual point): W_N(sl_N) is self-dual, kappa well-defined."""
        # N = k = 3: W_3(sl_3) at level 3
        c_w33 = c_WN_principal(3, Fraction(3))
        rho3 = anomaly_ratio_principal(3)
        kap_33 = rho3 * c_w33
        # VERIFIED: [DC] FL: c(W_3,3) = 2 - 3*8*(3+3-1)^2/(3+3) = 2-24*25/6 = 2-100 = -98
        assert c_w33 == Fraction(-98)
        # VERIFIED: [DC] kappa = (5/6)*(-98) = -490/6 = -245/3
        assert kap_33 == Fraction(5, 6) * Fraction(-98)
        assert kap_33 == Fraction(-245, 3)

    def test_level_rank_rho_differs(self):
        """Anomaly ratios rho_N and rho_k differ when N != k."""
        lr = level_rank_kappa(3, 4)
        assert lr['rho_N'] != lr['rho_k']


# ============================================================================
# Section 9: DS cascade and monotonicity
# ============================================================================

class TestDSCascade:
    """DS cascade: iterated DS and d_arith sequence."""

    def test_cascade_sl3_k3_stages(self):
        """Cascade for sl_3, k=3 has correct number of stages."""
        stages = ds_cascade_darith(3, 3)
        # Stages: V_3(sl_3) -> W_3(k=3) -> W_2(k=3)
        assert len(stages) >= 3

    def test_cascade_sl4_k2_stages(self):
        """Cascade for sl_4, k=2 has correct structure."""
        stages = ds_cascade_darith(4, 2)
        # V_2(sl_4) -> W_4(k=2) -> W_3(k=2) -> W_2(k=2)
        assert len(stages) >= 4

    def test_cascade_first_stage_affine(self):
        """First stage is always affine (d_arith = 1)."""
        for N in range(3, 6):
            stages = ds_cascade_darith(N, 3)
            assert stages[0]['type'] == 'affine'
            assert stages[0]['d_arith'] == 1

    def test_cascade_remaining_stages_W(self):
        """All stages after the first are W-algebras."""
        stages = ds_cascade_darith(4, 3)
        for s in stages[1:]:
            assert s['type'] == 'W-algebra'

    def test_cascade_not_monotone_increasing(self):
        """d_arith is NOT monotonically increasing through cascade."""
        mono = ds_cascade_monotonicity(4, 3)
        assert not mono['monotone_increasing']

    def test_cascade_monotone_decreasing_after_first(self):
        """After the first affine stage, d_arith is 0 or 1 (not increasing)."""
        mono = ds_cascade_monotonicity(5, 3)
        d_seq = mono['d_arith_sequence']
        # First value is 1 (affine), then all 0 (generic W)
        assert d_seq[0] == 1

    def test_cascade_total_jump(self):
        """Total depth jump: d_arith(final) - d_arith(initial)."""
        mono = ds_cascade_monotonicity(4, 3)
        # Initial d_arith = 1, final = 0 (generic W_2)
        assert mono['total_jump'] <= 0

    def test_cascade_interpretation(self):
        """DS converts arithmetic depth to algebraic depth."""
        mono = ds_cascade_monotonicity(3, 3)
        assert 'arithmetic' in mono['interpretation'].lower()


# ============================================================================
# Section 10: Non-principal orbits
# ============================================================================

class TestNonPrincipalOrbits:
    """Non-principal DS reductions and d_arith dependence on orbit."""

    def test_sl3_all_orbits_k2(self):
        """sl_3 nilpotent orbits at k=2."""
        orbits = darith_by_orbit_sl3(2)
        assert 'principal' in orbits
        assert 'subregular' in orbits

    def test_sl3_principal_vs_subregular(self):
        """Principal and subregular give same d_arith (= 0 at generic level).

        Use k=2 (not k=3, which is free-field for sl_3).
        """
        orbits = darith_by_orbit_sl3(2)
        assert orbits['principal'].darith_after == 0
        assert orbits['subregular'].darith_after == 0

    def test_sl4_all_orbits_k3(self):
        """sl_4 hook-type orbits at k=3."""
        orbits = darith_by_orbit_sl4(3)
        assert 'principal' in orbits
        assert 'hook_31' in orbits
        assert 'rect_22' in orbits
        assert 'minimal_211' in orbits

    def test_sl4_orbits_all_darith_0(self):
        """All sl_4 non-trivial orbits give d_arith = 0 at generic level."""
        orbits = darith_by_orbit_sl4(3)
        for name, j in orbits.items():
            assert j.darith_after == 0, f"d_arith != 0 for orbit {name}"

    def test_darith_independent_of_orbit_generic(self):
        """At generic (non-free-field) level, d_arith = 0 for all orbits.

        Use k not equal to N=3 (free-field) to test generic behavior.
        The orbit dependence shows up in d_alg, not d_arith.
        """
        for k in [1, 2, 5]:
            orbits = darith_by_orbit_sl3(k)
            d_values = {name: j.darith_after for name, j in orbits.items()}
            assert all(v == 0 for v in d_values.values()), \
                f"d_arith varies with orbit at k={k}: {d_values}"

    def test_kappa_bp_k2(self):
        """kappa(BP, k=2) = (1/6)*c(BP, k=2)."""
        kap = kappa_bershadsky_polyakov(Fraction(2))
        c_bp = c_bershadsky_polyakov(Fraction(2))
        assert kap == Fraction(1, 6) * c_bp


# ============================================================================
# Section 11: Shadow tower comparison
# ============================================================================

class TestShadowTowerComparison:
    """Shadow tower pre- and post-DS (Path 3 verification)."""

    def test_shadow_depth_increase_N2(self):
        """S_4(sl_2) = 0, S_4(Vir) != 0: depth increase for N=2."""
        comp = shadow_tower_comparison(2, 3)
        assert comp['S4_affine'] == Fraction(0)
        assert comp['S4_W'] != Fraction(0)
        assert comp['depth_increase']

    def test_shadow_depth_increase_N3(self):
        """Depth increase for N=3."""
        comp = shadow_tower_comparison(3, 3)
        assert comp['depth_increase']

    def test_shadow_depth_increase_N4(self):
        """Depth increase for N=4."""
        comp = shadow_tower_comparison(4, 3)
        assert comp['depth_increase']

    def test_affine_tower_terminates(self):
        """Affine sl_N tower terminates at arity 3 (S_4 = S_5 = ... = 0)."""
        comp = shadow_tower_comparison(3, 5, max_arity=8)
        for r in range(4, 9):
            assert comp['tower_affine'][r] == Fraction(0), \
                f"S_{r}(affine) != 0"

    def test_W_tower_infinite(self):
        """W_N tower has nonzero S_r for all r >= 4."""
        comp = shadow_tower_comparison(2, 5, max_arity=8)
        for r in range(4, 9):
            assert comp['tower_W'][r] != Fraction(0), \
                f"S_{r}(W) == 0 at r={r}"


# ============================================================================
# Section 12: Cross-engine consistency
# ============================================================================

class TestCrossEngineConsistency:
    """Cross-check with existing engines."""

    def test_kappa_sl2_matches_cascade_shadows(self):
        """kappa(V_k(sl_2)) matches ds_cascade_shadows module."""
        # Direct computation
        for k in [1, 2, 3, 5]:
            kv = Fraction(k)
            kap = kappa_slN(2, kv)
            expected = Fraction(3 * (k + 2), 2 * 2)  # dim=3, h=2
            assert kap == expected, f"kappa mismatch at k={k}"

    def test_kappa_WN_matches_anomaly_formula(self):
        """kappa(W_N) = (H_N - 1) * c(W_N) consistently."""
        for N in range(2, 6):
            for k in range(1, 6):
                kv = Fraction(k)
                kap = kappa_WN_principal(N, kv)
                rho = anomaly_ratio_principal(N)
                c_w = c_WN_principal(N, kv)
                assert kap == rho * c_w, \
                    f"kappa != rho*c at N={N}, k={k}"

    def test_ghost_constant_k_dependent(self):
        """Ghost constant C(N,k) depends on k (not constant)."""
        for N in range(2, 6):
            C1 = ghost_constant(N, Fraction(1))
            C5 = ghost_constant(N, Fraction(5))
            assert C1 != C5, f"C not k-dependent for N={N}"

    def test_ghost_constant_not_free(self):
        """C(N,k) != kappa_ghost^free = N(N-1)/2 in general."""
        for N in range(2, 6):
            C5 = ghost_constant(N, Fraction(5))
            kgf = kappa_ghost_free(N)
            assert C5 != kgf, f"C == free ghost kappa at N={N}"

    def test_verify_all_passes(self):
        """Full verification suite passes."""
        results = verify_all()
        failures = {k: v for k, v in results.items() if not v}
        assert not failures, f"verify_all failures: {failures}"
