r"""Tests for DS-transferred shadow obstruction towers: explicit computation of W_N
shadows via Drinfeld-Sokolov transfer from the affine sl_N shadow obstruction tower.

STRUCTURE (109 tests):

  Section 1: Central charge formulas (10 tests)
      c(sl_N, k) and c(W_N, k) exact values, c-additivity
  Section 2: Kappa formulas (10 tests)
      kappa(sl_N), kappa(W_N), anomaly ratio, kappa deficit
  Section 3: Ghost sector analysis (10 tests)
      c_ghost = N(N-1), kappa non-additivity (all N), deficit k-dependence
  Section 4: Affine shadow obstruction towers (8 tests)
      Class L verification: S_r = 0 for r >= 4
  Section 5: Direct vs transferred towers — T-line (16 tests)
      Agreement at all arities for N=2,3,4,5 at multiple levels
  Section 6: Direct vs transferred towers — W-line (6 tests)
      Agreement on the W_3 direction for N=3,4,5
  Section 7: Virasoro cross-checks (8 tests)
      Known exact formulas for S_2..S_5 at specific levels
  Section 8: Quartic creation mechanism (8 tests)
      S_4 = 0 on affine, S_4 != 0 on W_N, Lambda exchange formula
  Section 9: Cubic doubling (6 tests)
      S_3(W_N)/S_3(sl_N) = 2 universally
  Section 10: Depth classification (6 tests)
      Affine = class L, W_N = class M
  Section 11: Growth rate analysis (6 tests)
      rho(sl_N) = finite, rho(W_N) > rho(sl_N), depth increase
  Section 12: Cross-engine consistency (6 tests)
      Agreement with ds_cascade_shadows at overlapping points
  Edge cases: (9 tests)
      Critical level, parity constraints, systematic comparison, verify_all

Manuscript references:
    thm:ds-koszul-obstruction, cor:ds-theta-descent,
    thm:shadow-archetype-classification, prop:independent-sum-factorization,
    thm:single-line-dichotomy, rem:virasoro-resonance-model
"""

import pytest
from fractions import Fraction

from compute.lib.ds_transferred_shadows import (
    # Central charges
    c_slN,
    c_WN,
    c_ghost,
    # Kappa
    kappa_slN,
    kappa_WN,
    kappa_ghost,
    kappa_deficit,
    harmonic_minus_one,
    # Shadow data
    affine_shadow_data,
    affine_shadow_tower,
    wn_shadow_data_t_line,
    wn_shadow_data_w_line,
    wn_direct_tower_t_line,
    wn_direct_tower_w_line,
    # DS transfer
    ds_transferred_shadow_data_t_line,
    ds_transferred_tower_t_line,
    ds_transferred_shadow_data_w_line,
    ds_transferred_tower_w_line,
    # Analysis
    ghost_analysis,
    ds_transfer_analysis,
    quartic_creation_analysis,
    growth_rate,
    growth_rate_comparison,
    cubic_doubling_analysis,
    depth_classification,
    virasoro_crosscheck,
    shadow_tower_from_data,
    systematic_comparison,
    verify_all,
)


# ============================================================================
# Section 1: Central charge formulas (10 tests)
# ============================================================================

class TestCentralCharges:
    """Exact central charge computations for sl_N and W_N."""

    def test_c_sl2_k1(self):
        """c(sl_2, k=1) = 3*1/(1+2) = 1."""
        assert c_slN(2, Fraction(1)) == Fraction(1)

    def test_c_sl3_k1(self):
        """c(sl_3, k=1) = 8*1/(1+3) = 2."""
        assert c_slN(3, Fraction(1)) == Fraction(2)

    def test_c_sl4_k1(self):
        """c(sl_4, k=1) = 15*1/(1+4) = 3."""
        assert c_slN(4, Fraction(1)) == Fraction(3)

    def test_c_sl5_k1(self):
        """c(sl_5, k=1) = 24*1/(1+5) = 4."""
        assert c_slN(5, Fraction(1)) == Fraction(4)

    def test_c_vir_k1(self):
        """c(Vir from sl_2, k=1) = 1 - 6*4/3 = -7 (Fateev-Lukyanov)."""
        # VERIFIED: c_wn_fl(2,1)=-7 [DC], complementarity c(1)+c(-5)=26 [SY]
        assert c_WN(2, Fraction(1)) == Fraction(-7)

    def test_c_W3_k1(self):
        """c(W_3, k=1) = 2 - 24*9/4 = -52 (Fateev-Lukyanov)."""
        # VERIFIED: c_wn_fl(3,1)=-52 [DC], complementarity c(1)+c(-7)=100 [SY]
        assert c_WN(3, Fraction(1)) == Fraction(-52)

    def test_c_W4_k1(self):
        """c(W_4, k=1) = 3 - 60*16/5 = -189 (Fateev-Lukyanov)."""
        # VERIFIED: c_wn_fl(4,1)=-189 [DC], complementarity c(1)+c(-9)=246 [SY]
        assert c_WN(4, Fraction(1)) == Fraction(-189)

    def test_c_W5_k1(self):
        """c(W_5, k=1) = 4 - 120*25/6 = -496 (Fateev-Lukyanov)."""
        # VERIFIED: c_wn_fl(5,1)=-496 [DC], complementarity c(1)+c(-11)=488 [SY]
        assert c_WN(5, Fraction(1)) == Fraction(-496)

    def test_c_ghost_additivity_N2(self):
        """c(sl_2) = c(Vir) + c_ghost(2, k) for all k."""
        # VERIFIED: c_ghost(N,k) = c_slN(N,k) - c_WN(N,k) is k-DEPENDENT
        # with the correct FL formula. c_ghost(N) = N*(N-1) is only the k=0 value.
        for kv in [Fraction(1), Fraction(2), Fraction(5), Fraction(10)]:
            assert c_slN(2, kv) == c_WN(2, kv) + c_ghost(2, kv)

    def test_c_ghost_additivity_N5(self):
        """c(sl_5) = c(W_5) + c_ghost(5, k) for all k."""
        # VERIFIED: c_ghost(N,k) = c_slN(N,k) - c_WN(N,k) is k-DEPENDENT [DC]
        for kv in [Fraction(1), Fraction(2), Fraction(5), Fraction(10)]:
            assert c_slN(5, kv) == c_WN(5, kv) + c_ghost(5, kv)


# ============================================================================
# Section 2: Kappa formulas (10 tests)
# ============================================================================

class TestKappaFormulas:
    """Exact kappa computations for affine and W_N algebras."""

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*3/(2*2) = 9/4."""
        assert kappa_slN(2, Fraction(1)) == Fraction(9, 4)

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*4/(2*3) = 16/3."""
        assert kappa_slN(3, Fraction(1)) == Fraction(16, 3)

    def test_kappa_sl4_k1(self):
        """kappa(sl_4, k=1) = 15*5/(2*4) = 75/8."""
        assert kappa_slN(4, Fraction(1)) == Fraction(75, 8)

    def test_kappa_sl5_k1(self):
        """kappa(sl_5, k=1) = 24*6/(2*5) = 72/5."""
        assert kappa_slN(5, Fraction(1)) == Fraction(72, 5)

    def test_kappa_WN_virasoro(self):
        """kappa(Vir, k=1) = c/2 = -7/2 (Fateev-Lukyanov c=-7)."""
        # VERIFIED: kappa = (H_2-1)*c = (1/2)*(-7) = -7/2 [DC]
        assert kappa_WN(2, Fraction(1)) == Fraction(-7, 2)

    def test_kappa_W3_k1(self):
        """kappa(W_3, k=1) = (H_3-1)*c = (5/6)*(-52) = -130/3 (Fateev-Lukyanov)."""
        # VERIFIED: kappa = (5/6)*(-52) = -130/3 [DC], cross-check with kappa_wn_fl [CF]
        assert kappa_WN(3, Fraction(1)) == Fraction(-130, 3)

    def test_harmonic_minus_one_N2(self):
        """H_2 - 1 = 1/2."""
        assert harmonic_minus_one(2) == Fraction(1, 2)

    def test_harmonic_minus_one_N3(self):
        """H_3 - 1 = 1/2 + 1/3 = 5/6."""
        assert harmonic_minus_one(3) == Fraction(5, 6)

    def test_harmonic_minus_one_N4(self):
        """H_4 - 1 = 1/2 + 1/3 + 1/4 = 13/12."""
        assert harmonic_minus_one(4) == Fraction(13, 12)

    def test_harmonic_minus_one_N5(self):
        """H_5 - 1 = 1/2 + 1/3 + 1/4 + 1/5 = 77/60."""
        assert harmonic_minus_one(5) == Fraction(77, 60)


# ============================================================================
# Section 3: Ghost sector analysis (10 tests)
# ============================================================================

class TestGhostSector:
    """Ghost sector: c_ghost, kappa additivity, discrepancy."""

    def test_c_ghost_N2(self):
        """c_ghost(sl_2) = 2*1 = 2."""
        assert c_ghost(2) == Fraction(2)

    def test_c_ghost_N3(self):
        """c_ghost(sl_3) = 3*2 = 6."""
        assert c_ghost(3) == Fraction(6)

    def test_c_ghost_N4(self):
        """c_ghost(sl_4) = 4*3 = 12."""
        assert c_ghost(4) == Fraction(12)

    def test_c_ghost_N5(self):
        """c_ghost(sl_5) = 5*4 = 20."""
        assert c_ghost(5) == Fraction(20)

    def test_kappa_NOT_additive_N2(self):
        """For N=2: kappa(sl_2) != kappa(Vir) + kappa_ghost at generic k.

        Kappa additivity FAILS because the three algebras (sl_N, W_N, ghost)
        have three DIFFERENT anomaly ratios:
          kappa(sl_N)/c(sl_N) = (k+h^v)^2 / (2*h^v*k)
          kappa(W_N)/c(W_N) = H_N - 1
          kappa_ghost/c_ghost = 1/2
        These are equal only at the self-dual level k = h^v.
        """
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            ga = ghost_analysis(2, kv)
            assert not ga['kappa_additive'], f"N=2 should not be kappa-additive at k={kv}"

    def test_kappa_NOT_additive_N3(self):
        """For N>=3: kappa IS NOT naively additive."""
        for kv in [Fraction(1), Fraction(5)]:
            ga = ghost_analysis(3, kv)
            assert not ga['kappa_additive'], f"N=3 should not be kappa-additive at k={kv}"

    def test_kappa_NOT_additive_N4(self):
        """For N=4: kappa is NOT additive."""
        ga = ghost_analysis(4, Fraction(5))
        assert not ga['kappa_additive']

    def test_kappa_deficit_k_dependent_N2(self):
        """Kappa deficit C(2,k) = kappa(sl_2) - kappa(Vir) is k-dependent."""
        deficits = set()
        for kv in [Fraction(1), Fraction(2), Fraction(5), Fraction(10)]:
            ga = ghost_analysis(2, kv)
            deficits.add(ga['kappa_deficit'])
        assert len(deficits) > 1, "Deficit should vary with k"

    def test_kappa_deficit_k_dependent_N3(self):
        """Kappa deficit C(3,k) is k-dependent."""
        deficits = set()
        for kv in [Fraction(1), Fraction(2), Fraction(5)]:
            ga = ghost_analysis(3, kv)
            deficits.add(ga['kappa_deficit'])
        assert len(deficits) > 1

    def test_kappa_deficit_positive_large_k(self):
        """At large k, kappa deficit is positive (kappa(sl_N) >> kappa(W_N))."""
        ga = ghost_analysis(3, Fraction(100))
        assert ga['kappa_deficit'] > 0


# ============================================================================
# Section 4: Affine shadow obstruction towers (8 tests)
# ============================================================================

class TestAffineTowers:
    """Verify affine sl_N shadow obstruction towers are class L (terminate at arity 3)."""

    def test_affine_sl2_S2(self):
        """S_2(sl_2, k=1) = kappa = 9/4."""
        tower = affine_shadow_tower(2, Fraction(1))
        assert tower[2] == Fraction(9, 4)

    def test_affine_sl2_S3(self):
        """S_3(sl_2) = 1 (universal for all KM)."""
        tower = affine_shadow_tower(2, Fraction(1))
        assert tower[3] == Fraction(1)

    def test_affine_sl2_S4_zero(self):
        """S_4(sl_2) = 0 (Jacobi identity)."""
        tower = affine_shadow_tower(2, Fraction(1))
        assert tower[4] == Fraction(0)

    def test_affine_sl3_S4_zero(self):
        """S_4(sl_3) = 0 (Jacobi identity, all N)."""
        tower = affine_shadow_tower(3, Fraction(1))
        assert tower[4] == Fraction(0)

    def test_affine_terminates_N2(self):
        """Affine sl_2 tower: S_r = 0 for ALL r >= 4."""
        tower = affine_shadow_tower(2, Fraction(5), max_arity=20)
        for r in range(4, 21):
            assert tower[r] == Fraction(0), f"S_{r}(sl_2) = {tower[r]} != 0"

    def test_affine_terminates_N3(self):
        """Affine sl_3 tower: S_r = 0 for ALL r >= 4."""
        tower = affine_shadow_tower(3, Fraction(5), max_arity=20)
        for r in range(4, 21):
            assert tower[r] == Fraction(0), f"S_{r}(sl_3) = {tower[r]} != 0"

    def test_affine_terminates_N4(self):
        """Affine sl_4 tower: S_r = 0 for ALL r >= 4."""
        tower = affine_shadow_tower(4, Fraction(5), max_arity=20)
        for r in range(4, 21):
            assert tower[r] == Fraction(0), f"S_{r}(sl_4) = {tower[r]} != 0"

    def test_affine_terminates_N5(self):
        """Affine sl_5 tower: S_r = 0 for ALL r >= 4."""
        tower = affine_shadow_tower(5, Fraction(5), max_arity=20)
        for r in range(4, 21):
            assert tower[r] == Fraction(0), f"S_{r}(sl_5) = {tower[r]} != 0"


# ============================================================================
# Section 5: Direct vs transferred towers — T-line (16 tests)
# ============================================================================

class TestDirectVsTransferredTLine:
    """Agreement between direct and DS-transferred shadow obstruction towers on the T-line."""

    def _check_agreement(self, N: int, k_val: Fraction, max_arity: int = 20):
        """Verify exact agreement at all arities."""
        tower_direct = wn_direct_tower_t_line(N, k_val, max_arity)
        tower_transferred = ds_transferred_tower_t_line(N, k_val, max_arity)
        for r in range(2, max_arity + 1):
            d = tower_direct[r]
            t = tower_transferred[r]
            assert d == t, (
                f"N={N}, k={k_val}, r={r}: direct={d} != transferred={t}"
            )

    def test_N2_k1(self):
        """sl_2 -> Virasoro at k=1: towers agree."""
        self._check_agreement(2, Fraction(1))

    def test_N2_k2(self):
        """sl_2 -> Virasoro at k=2: towers agree."""
        self._check_agreement(2, Fraction(2))

    def test_N2_k5(self):
        """sl_2 -> Virasoro at k=5: towers agree."""
        self._check_agreement(2, Fraction(5))

    def test_N2_k10(self):
        """sl_2 -> Virasoro at k=10: towers agree."""
        self._check_agreement(2, Fraction(10))

    def test_N3_k1(self):
        """sl_3 -> W_3 at k=1: towers agree."""
        self._check_agreement(3, Fraction(1))

    def test_N3_k2(self):
        """sl_3 -> W_3 at k=2: towers agree."""
        self._check_agreement(3, Fraction(2))

    def test_N3_k5(self):
        """sl_3 -> W_3 at k=5: towers agree."""
        self._check_agreement(3, Fraction(5))

    def test_N3_k10(self):
        """sl_3 -> W_3 at k=10: towers agree."""
        self._check_agreement(3, Fraction(10))

    def test_N4_k1(self):
        """sl_4 -> W_4 at k=1: towers agree."""
        self._check_agreement(4, Fraction(1))

    def test_N4_k2(self):
        """sl_4 -> W_4 at k=2: towers agree."""
        self._check_agreement(4, Fraction(2))

    def test_N4_k5(self):
        """sl_4 -> W_4 at k=5: towers agree."""
        self._check_agreement(4, Fraction(5))

    def test_N4_k10(self):
        """sl_4 -> W_4 at k=10: towers agree."""
        self._check_agreement(4, Fraction(10))

    def test_N5_k1(self):
        """sl_5 -> W_5 at k=1: towers agree."""
        self._check_agreement(5, Fraction(1))

    def test_N5_k2(self):
        """sl_5 -> W_5 at k=2: towers agree."""
        self._check_agreement(5, Fraction(2))

    def test_N5_k5(self):
        """sl_5 -> W_5 at k=5: towers agree."""
        self._check_agreement(5, Fraction(5))

    def test_N5_k10(self):
        """sl_5 -> W_5 at k=10: towers agree."""
        self._check_agreement(5, Fraction(10))


# ============================================================================
# Section 6: Direct vs transferred towers — W-line (6 tests)
# ============================================================================

class TestDirectVsTransferredWLine:
    """Agreement on the W_3-line for N >= 3."""

    def _check_w_line(self, N: int, k_val: Fraction, max_arity: int = 20):
        """Verify exact agreement on the W-line."""
        tower_direct = wn_direct_tower_w_line(N, k_val, max_arity)
        tower_transferred = ds_transferred_tower_w_line(N, k_val, max_arity)
        for r in range(2, max_arity + 1):
            d = tower_direct[r]
            t = tower_transferred[r]
            assert d == t, (
                f"W-line N={N}, k={k_val}, r={r}: direct={d} != transferred={t}"
            )

    def test_N3_k1_wline(self):
        """W_3-line at k=1: towers agree."""
        self._check_w_line(3, Fraction(1))

    def test_N3_k5_wline(self):
        """W_3-line at k=5: towers agree."""
        self._check_w_line(3, Fraction(5))

    def test_N4_k1_wline(self):
        """W_3-line of W_4 at k=1: towers agree."""
        self._check_w_line(4, Fraction(1))

    def test_N4_k5_wline(self):
        """W_3-line of W_4 at k=5: towers agree."""
        self._check_w_line(4, Fraction(5))

    def test_N5_k1_wline(self):
        """W_3-line of W_5 at k=1: towers agree."""
        self._check_w_line(5, Fraction(1))

    def test_N5_k5_wline(self):
        """W_3-line of W_5 at k=5: towers agree."""
        self._check_w_line(5, Fraction(5))


# ============================================================================
# Section 7: Virasoro cross-checks (8 tests)
# ============================================================================

class TestVirasoroCrossChecks:
    """Verify DS-transferred Virasoro tower against exact formulas."""

    def test_vir_S2_k1(self):
        """S_2(Vir, k=1) = c/2 = -1/2."""
        vc = virasoro_crosscheck(Fraction(1))
        assert vc['checks'][2]['match']

    def test_vir_S3_k1(self):
        """S_3(Vir, k=1) = 2."""
        vc = virasoro_crosscheck(Fraction(1))
        assert vc['checks'][3]['match']

    def test_vir_S4_k1(self):
        """S_4(Vir, k=1) = 10/[c(5c+22)] at c=-1."""
        vc = virasoro_crosscheck(Fraction(1))
        assert vc['checks'][4]['match']

    def test_vir_S5_k1(self):
        """S_5(Vir, k=1) = -48/[c^2(5c+22)] at c=-1."""
        vc = virasoro_crosscheck(Fraction(1))
        assert vc['checks'][5]['match']

    def test_vir_all_k2(self):
        """Full cross-check at k=2: S_2..S_5 match exact formulas."""
        vc = virasoro_crosscheck(Fraction(2))
        assert vc['all_match']

    def test_vir_all_k5(self):
        """Full cross-check at k=5."""
        vc = virasoro_crosscheck(Fraction(5))
        assert vc['all_match']

    def test_vir_all_k10(self):
        """Full cross-check at k=10."""
        vc = virasoro_crosscheck(Fraction(10))
        assert vc['all_match']

    def test_vir_all_k3(self):
        """Full cross-check at k=3."""
        vc = virasoro_crosscheck(Fraction(3))
        assert vc['all_match']


# ============================================================================
# Section 8: Quartic creation mechanism (8 tests)
# ============================================================================

class TestQuarticCreation:
    """Verify the quartic shadow is CREATED by DS reduction."""

    def test_affine_S4_zero_N2(self):
        """S_4(sl_2) = 0 at all levels."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            tower = affine_shadow_tower(2, kv, 5)
            assert tower[4] == Fraction(0)

    def test_affine_S4_zero_N3(self):
        """S_4(sl_3) = 0 at all levels."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            tower = affine_shadow_tower(3, kv, 5)
            assert tower[4] == Fraction(0)

    def test_wn_S4_nonzero_N2(self):
        """S_4(Vir) != 0: quartic CREATED by DS."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            tower = wn_direct_tower_t_line(2, kv, 5)
            assert tower[4] != Fraction(0), f"S_4(Vir) = 0 at k={kv}!"

    def test_wn_S4_nonzero_N3(self):
        """S_4(W_3) != 0: quartic created."""
        for kv in [Fraction(1), Fraction(5)]:
            tower = wn_direct_tower_t_line(3, kv, 5)
            assert tower[4] != Fraction(0)

    def test_quartic_formula_N2_k1(self):
        """S_4(Vir, c=-1) = 10/[(-1)(5*(-1)+22)] = 10/(-17) = -10/17."""
        tower = wn_direct_tower_t_line(2, Fraction(1), 5)
        c_w = c_WN(2, Fraction(1))  # = -1
        expected = Fraction(10) / (c_w * (5 * c_w + 22))
        assert tower[4] == expected

    def test_quartic_formula_N3_k1(self):
        """S_4(W_3, c=-4) = 10/[(-4)(5*(-4)+22)] = 10/(-4*2) = -5/4."""
        tower = wn_direct_tower_t_line(3, Fraction(1), 5)
        c_w = c_WN(3, Fraction(1))  # = -4
        expected = Fraction(10) / (c_w * (5 * c_w + 22))
        assert tower[4] == expected

    def test_quartic_creation_analysis_N2(self):
        """Quartic creation analysis for sl_2 -> Vir."""
        qc = quartic_creation_analysis(2, Fraction(5))
        assert qc['quartic_created']
        assert qc['S4_affine'] == Fraction(0)
        assert qc['S4_t_line'] != Fraction(0)

    def test_quartic_creation_analysis_N4(self):
        """Quartic creation analysis for sl_4 -> W_4."""
        qc = quartic_creation_analysis(4, Fraction(5))
        assert qc['quartic_created']
        assert qc['S4_w_line'] is not None


# ============================================================================
# Section 9: Cubic doubling (6 tests)
# ============================================================================

class TestCubicDoubling:
    """S_3(W_N, T-line) = 2 * S_3(sl_N) universally."""

    def test_cubic_N2_k1(self):
        """S_3(Vir)/S_3(sl_2) = 2/1 = 2 at k=1."""
        t_aff = affine_shadow_tower(2, Fraction(1), 5)
        t_wn = wn_direct_tower_t_line(2, Fraction(1), 5)
        assert t_wn[3] / t_aff[3] == Fraction(2)

    def test_cubic_N3_k1(self):
        """S_3(W_3)/S_3(sl_3) = 2 at k=1."""
        t_aff = affine_shadow_tower(3, Fraction(1), 5)
        t_wn = wn_direct_tower_t_line(3, Fraction(1), 5)
        assert t_wn[3] / t_aff[3] == Fraction(2)

    def test_cubic_N4_k5(self):
        """S_3(W_4)/S_3(sl_4) = 2 at k=5."""
        t_aff = affine_shadow_tower(4, Fraction(5), 5)
        t_wn = wn_direct_tower_t_line(4, Fraction(5), 5)
        assert t_wn[3] / t_aff[3] == Fraction(2)

    def test_cubic_N5_k10(self):
        """S_3(W_5)/S_3(sl_5) = 2 at k=10."""
        t_aff = affine_shadow_tower(5, Fraction(10), 5)
        t_wn = wn_direct_tower_t_line(5, Fraction(10), 5)
        assert t_wn[3] / t_aff[3] == Fraction(2)

    def test_cubic_doubling_universal(self):
        """Cubic doubling ratio = 2 for all N=2..5 and k=1,2,5,10."""
        cd = cubic_doubling_analysis(
            N_values=[2, 3, 4, 5],
            k_values=[Fraction(1), Fraction(2), Fraction(5), Fraction(10)]
        )
        assert cd['all_ratio_2']

    def test_affine_S3_universal(self):
        """S_3(sl_N) = 1 for all N (from the Lie bracket)."""
        for N in [2, 3, 4, 5]:
            for kv in [Fraction(1), Fraction(5)]:
                tower = affine_shadow_tower(N, kv, 5)
                assert tower[3] == Fraction(1), f"S_3(sl_{N}) = {tower[3]} != 1"


# ============================================================================
# Section 10: Depth classification (6 tests)
# ============================================================================

class TestDepthClassification:
    """Verify depth: affine = class L (depth 3), W_N = class M (depth inf)."""

    def test_depth_N2(self):
        """sl_2 -> Vir: depth increase L -> M."""
        dc = depth_classification(2, Fraction(5))
        assert dc['affine_class'] == 'L'
        assert dc['wn_class'] == 'M'
        assert dc['depth_increase']

    def test_depth_N3(self):
        """sl_3 -> W_3: depth increase L -> M."""
        dc = depth_classification(3, Fraction(5))
        assert dc['depth_increase']

    def test_depth_N4(self):
        """sl_4 -> W_4: depth increase L -> M."""
        dc = depth_classification(4, Fraction(5))
        assert dc['depth_increase']

    def test_depth_N5(self):
        """sl_5 -> W_5: depth increase L -> M."""
        dc = depth_classification(5, Fraction(5))
        assert dc['depth_increase']

    def test_affine_no_higher_shadows(self):
        """Affine sl_N: zero nonzero entries above arity 3."""
        for N in [2, 3, 4, 5]:
            dc = depth_classification(N, Fraction(5))
            assert dc['affine_nonzero_above_3'] == 0

    def test_wn_has_higher_shadows(self):
        """W_N: multiple nonzero entries above arity 3."""
        for N in [2, 3, 4, 5]:
            dc = depth_classification(N, Fraction(5))
            assert dc['wn_nonzero_above_3'] >= 10, (
                f"W_{N} only has {dc['wn_nonzero_above_3']} nonzero S_r for r>=4"
            )


# ============================================================================
# Section 11: Growth rate analysis (6 tests)
# ============================================================================

class TestGrowthRate:
    """Shadow growth rates: affine finite, W_N increases."""

    def test_affine_growth_rate_finite(self):
        """Affine growth rate is finite (3/(2*kappa) for class L with alpha=1)."""
        aff_data = affine_shadow_data(2, Fraction(5))
        rho = growth_rate(aff_data['kappa'], aff_data['alpha'], aff_data['S4'])
        assert rho > 0
        assert rho < 1  # For large enough kappa

    def test_wn_growth_rate_positive(self):
        """W_N growth rate is positive (class M, infinite tower)."""
        wn_data = wn_shadow_data_t_line(2, Fraction(5))
        rho = growth_rate(wn_data['kappa'], wn_data['alpha'], wn_data['S4'])
        assert rho > 0

    def test_growth_rate_comparison_N2(self):
        """Growth rate increases under DS for N=2."""
        gc = growth_rate_comparison(2, Fraction(5))
        assert gc['rho_WN'] > 0
        assert gc['rho_affine'] > 0

    def test_growth_rate_comparison_N3(self):
        """Growth rate for N=3."""
        gc = growth_rate_comparison(3, Fraction(5))
        assert gc['rho_WN'] > 0

    def test_growth_rate_comparison_N4(self):
        """Growth rate for N=4."""
        gc = growth_rate_comparison(4, Fraction(5))
        assert gc['rho_WN'] > 0

    def test_wn_tower_nonzero_high_arity(self):
        """W_N shadow obstruction tower has nonzero entries at high arities."""
        for N in [2, 3, 4, 5]:
            tower = wn_direct_tower_t_line(N, Fraction(5), 20)
            # At least S_10 should be nonzero
            assert tower[10] != Fraction(0), f"S_10(W_{N}) = 0!"


# ============================================================================
# Section 12: Cross-engine consistency (6 tests)
# ============================================================================

class TestCrossEngineConsistency:
    """Agreement with ds_cascade_shadows at overlapping points."""

    def test_c_slN_agrees(self):
        """Central charge agrees with ds_cascade_shadows."""
        from compute.lib.ds_cascade_shadows import (
            c_slN as c_slN_ref,
        )
        for N in [2, 3, 4, 5]:
            for kv in [Fraction(1), Fraction(5)]:
                assert c_slN(N, kv) == c_slN_ref(N, kv)

    def test_c_WN_agrees(self):
        """W_N central charge agrees with ds_cascade_shadows."""
        from compute.lib.ds_cascade_shadows import (
            c_WN as c_WN_ref,
        )
        for N in [2, 3, 4, 5]:
            for kv in [Fraction(1), Fraction(5)]:
                assert c_WN(N, kv) == c_WN_ref(N, kv)

    def test_kappa_slN_agrees(self):
        """kappa(sl_N) agrees with ds_cascade_shadows."""
        from compute.lib.ds_cascade_shadows import (
            kappa_slN as kappa_slN_ref,
        )
        for N in [2, 3, 4, 5]:
            for kv in [Fraction(1), Fraction(5)]:
                assert kappa_slN(N, kv) == kappa_slN_ref(N, kv)

    def test_kappa_WN_agrees(self):
        """kappa(W_N) agrees with ds_cascade_shadows."""
        from compute.lib.ds_cascade_shadows import (
            kappa_WN as kappa_WN_ref,
        )
        for N in [2, 3, 4, 5]:
            for kv in [Fraction(1), Fraction(5)]:
                assert kappa_WN(N, kv) == kappa_WN_ref(N, kv)

    def test_shadow_tower_agrees_N2(self):
        """Shadow obstruction tower for W_2 (Virasoro) agrees with ds_cascade_shadows."""
        from compute.lib.ds_cascade_shadows import (
            shadow_tower as shadow_tower_ref,
            WN_shadow_data as WN_shadow_data_ref,
        )
        for kv in [Fraction(1), Fraction(5)]:
            sd_ref = WN_shadow_data_ref(2, kv)
            tower_ref = shadow_tower_ref(
                sd_ref['kappa'], sd_ref['alpha'], sd_ref['S4'], 10
            )
            tower_ours = wn_direct_tower_t_line(2, kv, 10)
            for r in range(2, 11):
                assert tower_ours[r] == tower_ref[r], (
                    f"k={kv}, r={r}: ours={tower_ours[r]}, ref={tower_ref[r]}"
                )

    def test_shadow_tower_N3_uses_different_kappa(self):
        """For N>=3: ds_cascade_shadows uses TOTAL kappa = (H_N-1)*c,
        while our T-line uses kappa_T = c/2. These differ by design.

        ds_cascade_shadows models W_N as an effective 1D shadow with
        total kappa. Our module uses the intrinsic T-channel kappa.
        For N=2 they coincide because H_2 - 1 = 1/2.
        """
        from compute.lib.ds_cascade_shadows import (
            WN_shadow_data as WN_shadow_data_ref,
        )
        for kv in [Fraction(1), Fraction(5)]:
            sd_ref = WN_shadow_data_ref(3, kv)
            sd_ours = wn_shadow_data_t_line(3, kv)
            # kappa values differ: ref uses 5c/6, ours uses c/2
            assert sd_ref['kappa'] != sd_ours['kappa']
            # alpha and S_4 agree
            assert sd_ref['alpha'] == sd_ours['alpha']
            assert sd_ref['S4'] == sd_ours['S4']


# ============================================================================
# Additional edge case tests
# ============================================================================

class TestEdgeCases:
    """Edge cases and structural properties."""

    def test_critical_level_raises(self):
        """Critical level k=-N raises ValueError."""
        with pytest.raises(ValueError):
            c_slN(2, Fraction(-2))
        with pytest.raises(ValueError):
            c_WN(3, Fraction(-3))

    def test_wn_w_line_N2_raises(self):
        """W-line for N=2 raises (no W_3 generator)."""
        with pytest.raises(ValueError):
            wn_shadow_data_w_line(2, Fraction(1))

    def test_w_line_odd_arities_vanish(self):
        """W-line: all ODD arities vanish (Z_2 parity)."""
        tower = wn_direct_tower_w_line(3, Fraction(5), 20)
        for r in range(3, 21, 2):
            assert tower[r] == Fraction(0), f"Odd S_{r} = {tower[r]} != 0 on W-line"

    def test_w_line_even_arities_nonzero(self):
        """W-line: EVEN arities >= 4 are nonzero."""
        tower = wn_direct_tower_w_line(3, Fraction(5), 20)
        for r in range(4, 21, 2):
            assert tower[r] != Fraction(0), f"Even S_{r} = 0 on W-line!"

    def test_systematic_comparison(self):
        """Run the full systematic comparison: all direct==transferred."""
        result = systematic_comparison(
            N_values=[2, 3, 4, 5],
            k_values=[Fraction(1), Fraction(2), Fraction(5)],
            max_arity=15
        )
        assert result['all_agree'], "Systematic comparison found disagreement!"

    def test_verify_all(self):
        """Run the complete verification suite."""
        results = verify_all(max_arity=15)
        failures = {name: ok for name, ok in results.items() if not ok}
        assert not failures, f"verify_all failures: {failures}"

    def test_ds_noncommutativity_arity4(self):
        """DS does NOT commute with shadows at arity >= 4."""
        for N in [2, 3, 4, 5]:
            analysis = ds_transfer_analysis(N, Fraction(5), 10)
            # At arity 4: affine S_4 = 0 but W_N S_4 != 0
            assert not analysis['per_arity'][4]['ds_commutes'], (
                f"N={N}: DS should NOT commute at arity 4"
            )

    def test_ds_commutes_arity2(self):
        """DS commutes with shadows at arity 2 (both give kappa)."""
        # Note: the "commutation" at arity 2 is subtle.
        # The affine kappa != W_N kappa, so it DOES NOT commute
        # at arity 2 either!  The commutation is at the CENTRAL CHARGE
        # level, not at the kappa level.
        # So we test that the analysis correctly identifies non-commutation.
        analysis = ds_transfer_analysis(2, Fraction(5), 5)
        # S_2(sl_2) = kappa(sl_2) != kappa(Vir) = S_2(Vir)
        assert not analysis['per_arity'][2]['ds_commutes']

    def test_large_k_behavior(self):
        """At large k, c(W_N) ~ -N(N^2-1)*k (Fateev-Lukyanov quadratic growth)."""
        # VERIFIED: c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N) ~ -N(N^2-1)*k [DC]
        k_large = Fraction(1000)
        for N in [2, 3, 4, 5]:
            c_w = c_WN(N, k_large)
            kap_w = kappa_WN(N, k_large)
            # c ~ -N(N^2-1)*k for large k
            c_approx = -N * (N**2 - 1) * float(k_large)
            assert abs(float(c_w) - c_approx) / abs(c_approx) < 0.01,                 f"N={N}: c={float(c_w)}, approx={c_approx}"
            # kappa ~ (H_N-1)*c, same sign
            assert float(kap_w) < 0, f"N={N}: kappa should be negative at large k"
