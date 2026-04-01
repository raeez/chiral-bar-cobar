r"""Tests for DS cascade shadows: V_k(sl_N) -> W_N for N = 2..6.

Systematic verification of the five computations:
  1. kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N)
  2. kappa(W_N) = c(W_N) * (H_N - 1)
  3. Ghost constant C(N,k) = kappa(V_k) - kappa(W_N), k-dependent
  4. c(W_N) = (N-1)(1 - N(N+1)/(k+N)) verified
  5. Shadow tower transformation: DS does NOT commute with shadows

STRUCTURE (149 tests total):
  Section 1: Central charge formulas and additivity (18 tests)
  Section 2: Kappa formulas — affine and W_N (19 tests)
  Section 3: Ghost constant C(N,k) (17 tests)
  Section 4: Shadow tower exact computation (22 tests)
  Section 5: S_3 transformation under DS (8 tests)
  Section 6: Depth increase L -> M (16 tests)
  Section 7: Cascade from quartic seed (18 tests)
  Section 8: Growth rate (13 tests)
  Section 9: Commutation failure analysis (8 tests)
  Section 10: Cross-engine consistency (10 tests)

Manuscript references:
    thm:ds-koszul-obstruction, thm:shadow-archetype-classification,
    prop:independent-sum-factorization, thm:single-line-dichotomy,
    cor:ds-theta-descent
"""

import pytest
from fractions import Fraction

from compute.lib.ds_cascade_shadows import (
    # Central charges
    c_slN,
    c_WN,
    c_ghost,
    # Kappa
    kappa_slN,
    harmonic_number,
    anomaly_ratio,
    kappa_WN,
    kappa_ghost_free,
    ghost_constant,
    # Shadow data
    slN_shadow_data,
    WN_shadow_data,
    # Tower
    shadow_tower,
    shadow_growth_rate,
    # Pipeline
    ds_cascade,
    # Analysis
    s3_transformation,
    depth_increase_table,
    ghost_constant_analysis,
    full_cascade_all_N,
    commutation_failure_arity,
    virasoro_quintic_crosscheck,
    # Verification
    verify_all,
)


# ============================================================================
# Section 1: Central charge formulas and additivity
# ============================================================================

class TestCentralChargeFormulas:
    """Test c(sl_N, k) and c(W_N, k) formulas for N = 2..6."""

    def test_c_sl2_k1(self):
        """c(sl_2, k=1) = 3*1/(1+2) = 1."""
        assert c_slN(2, Fraction(1)) == Fraction(1)

    def test_c_sl3_k1(self):
        """c(sl_3, k=1) = 8*1/(1+3) = 2."""
        assert c_slN(3, Fraction(1)) == Fraction(2)

    def test_c_sl6_k1(self):
        """c(sl_6, k=1) = 35*1/(1+6) = 5."""
        assert c_slN(6, Fraction(1)) == Fraction(5)

    def test_c_sl6_k5(self):
        """c(sl_6, k=5) = 35*5/(5+6) = 175/11."""
        assert c_slN(6, Fraction(5)) == Fraction(175, 11)

    def test_c_WN_virasoro(self):
        """c(Vir from sl_2, k=1) = 1 - 6/3 = -1."""
        assert c_WN(2, Fraction(1)) == Fraction(-1)

    def test_c_W3_k1(self):
        """c(W_3, k=1) = 2(1 - 12/4) = 2(-2) = -4."""
        assert c_WN(3, Fraction(1)) == Fraction(-4)

    def test_c_W6_k1(self):
        """c(W_6, k=1) = 5(1 - 42/7) = 5(-5) = -25."""
        assert c_WN(6, Fraction(1)) == Fraction(-25)

    def test_c_W6_k5(self):
        """c(W_6, k=5) = 5(1 - 42/11) = 5*(11-42)/11 = 5*(-31)/11 = -155/11."""
        assert c_WN(6, Fraction(5)) == Fraction(-155, 11)

    def test_c_ghost_N2(self):
        """c_ghost(sl_2) = 2*1 = 2."""
        assert c_ghost(2) == Fraction(2)

    def test_c_ghost_N6(self):
        """c_ghost(sl_6) = 6*5 = 30."""
        assert c_ghost(6) == Fraction(30)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_c_additivity(self, N):
        """c(sl_N, k) = c(W_N, k) + c_ghost(N) for all N and k."""
        for kv in [1, 2, 5, 10, 50]:
            k = Fraction(kv)
            assert c_slN(N, k) == c_WN(N, k) + c_ghost(N), \
                f"c-additivity fails for N={N}, k={kv}"

    def test_c_ghost_k_independent(self):
        """Ghost central charge N(N-1) is independent of k."""
        for N in [2, 3, 4, 5, 6]:
            diffs = []
            for kv in [1, 5, 10, 50]:
                k = Fraction(kv)
                diffs.append(c_slN(N, k) - c_WN(N, k))
            assert all(d == diffs[0] for d in diffs), \
                f"c_ghost depends on k for N={N}"

    def test_critical_level_raises(self):
        """c(sl_N, k=-N) should raise ValueError."""
        for N in [2, 3, 4, 5, 6]:
            with pytest.raises(ValueError):
                c_slN(N, Fraction(-N))


# ============================================================================
# Section 2: Kappa formulas
# ============================================================================

class TestKappaFormulas:
    """Test kappa formulas for affine sl_N and W_N."""

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*3/(2*2) = 9/4."""
        assert kappa_slN(2, Fraction(1)) == Fraction(9, 4)

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*4/(2*3) = 16/3."""
        assert kappa_slN(3, Fraction(1)) == Fraction(16, 3)

    def test_kappa_sl6_k1(self):
        """kappa(sl_6, k=1) = 35*7/(2*6) = 245/12."""
        assert kappa_slN(6, Fraction(1)) == Fraction(245, 12)

    def test_kappa_denominator_is_2N(self):
        """The correct formula has 2N in denominator, NOT 2.

        kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N), not (N^2-1)(k+N)/2.
        This tests AP1: the user's original formula was wrong by factor N.
        """
        for N in [2, 3, 4, 5, 6]:
            k = Fraction(5)
            correct = Fraction(N * N - 1) * (k + Fraction(N)) / (2 * Fraction(N))
            wrong = Fraction(N * N - 1) * (k + Fraction(N)) / 2
            assert kappa_slN(N, k) == correct
            assert kappa_slN(N, k) != wrong or N == 1  # only equal when N=1

    def test_harmonic_numbers(self):
        """H_2 = 3/2, H_3 = 11/6, H_4 = 25/12, H_5 = 137/60, H_6 = 49/20."""
        assert harmonic_number(2) == Fraction(3, 2)
        assert harmonic_number(3) == Fraction(11, 6)
        assert harmonic_number(4) == Fraction(25, 12)
        assert harmonic_number(5) == Fraction(137, 60)
        assert harmonic_number(6) == Fraction(49, 20)

    def test_anomaly_ratios(self):
        """H_N - 1: 1/2, 5/6, 13/12, 77/60, 29/20."""
        assert anomaly_ratio(2) == Fraction(1, 2)
        assert anomaly_ratio(3) == Fraction(5, 6)
        assert anomaly_ratio(4) == Fraction(13, 12)
        assert anomaly_ratio(5) == Fraction(77, 60)
        assert anomaly_ratio(6) == Fraction(29, 20)

    def test_kappa_virasoro_is_c_over_2(self):
        """For N=2 (Virasoro): kappa = c/2. This is the c/2 formula."""
        for kv in [1, 2, 5, 10]:
            k = Fraction(kv)
            c_v = c_WN(2, k)
            kap = kappa_WN(2, k)
            assert kap == c_v / 2, f"kappa(Vir) != c/2 at k={kv}"

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_kappa_WN_equals_rho_times_c(self, N):
        """kappa(W_N) = (H_N - 1) * c(W_N) for all N."""
        rho = anomaly_ratio(N)
        for kv in [1, 5, 10]:
            k = Fraction(kv)
            assert kappa_WN(N, k) == rho * c_WN(N, k)

    def test_kappa_ghost_free_values(self):
        """kappa_ghost_free = N(N-1)/2."""
        assert kappa_ghost_free(2) == Fraction(1)
        assert kappa_ghost_free(3) == Fraction(3)
        assert kappa_ghost_free(4) == Fraction(6)
        assert kappa_ghost_free(5) == Fraction(10)
        assert kappa_ghost_free(6) == Fraction(15)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_kappa_NOT_additive(self, N):
        """kappa(sl_N) != kappa(W_N) + kappa_ghost_free for N >= 2.

        This is the fundamental non-additivity under DS.
        """
        k = Fraction(5)
        lhs = kappa_slN(N, k)
        rhs = kappa_WN(N, k) + kappa_ghost_free(N)
        assert lhs != rhs, \
            f"kappa appears additive for N={N} — this should NOT happen"


# ============================================================================
# Section 3: Ghost constant C(N,k)
# ============================================================================

class TestGhostConstant:
    """Test the ghost constant C(N,k) = kappa(V_k) - kappa(W_N)."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_ghost_constant_k_dependent(self, N):
        """C(N,k) is k-dependent: C(N,1) != C(N,5)."""
        C1 = ghost_constant(N, Fraction(1))
        C5 = ghost_constant(N, Fraction(5))
        assert C1 != C5, f"Ghost constant is k-independent for N={N}"

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_ghost_constant_neq_free(self, N):
        """C(N,k) != N(N-1)/2 (the free-ghost kappa)."""
        C = ghost_constant(N, Fraction(5))
        kgf = kappa_ghost_free(N)
        assert C != kgf, f"C(N,k) equals free ghost kappa for N={N}"

    def test_ghost_constant_positive_at_large_k(self):
        """At large k, C(N,k) should be positive (both kappas are positive)."""
        for N in [2, 3, 4, 5, 6]:
            C = ghost_constant(N, Fraction(100))
            assert C > 0, f"C({N},100) = {C} is not positive"

    def test_ghost_constant_grows_with_k(self):
        """C(N,k) grows with k (at large k, linear growth)."""
        for N in [2, 3, 4, 5, 6]:
            C10 = ghost_constant(N, Fraction(10))
            C100 = ghost_constant(N, Fraction(100))
            assert C100 > C10, f"C({N},k) does not grow: C(10)={C10}, C(100)={C100}"

    def test_ghost_constant_grows_with_N(self):
        """C(N,k) grows with N at fixed k."""
        k = Fraction(5)
        Cs = [ghost_constant(N, k) for N in [2, 3, 4, 5, 6]]
        for i in range(len(Cs) - 1):
            assert Cs[i + 1] > Cs[i], \
                f"C does not grow: C({i+2})={Cs[i]}, C({i+3})={Cs[i+1]}"

    def test_ghost_constant_definition(self):
        """C(N,k) = kappa(V_k(sl_N)) - kappa(W_N) by definition."""
        for N in [2, 3, 4, 5, 6]:
            for kv in [1, 5, 10]:
                k = Fraction(kv)
                C = ghost_constant(N, k)
                expected = kappa_slN(N, k) - kappa_WN(N, k)
                assert C == expected

    def test_ghost_constant_analysis_structure(self):
        """ghost_constant_analysis returns expected structure."""
        result = ghost_constant_analysis()
        for N in [2, 3, 4, 5, 6]:
            assert N in result
            assert result[N]['C_k_dependent']
            assert not result[N]['C_equals_free_ever']


# ============================================================================
# Section 4: Shadow tower computation
# ============================================================================

class TestShadowTower:
    """Test exact shadow tower computation."""

    def test_class_G_terminates_at_2(self):
        """Class G (alpha=0, S4=0): S_r = 0 for r >= 3."""
        tower = shadow_tower(Fraction(5), Fraction(0), Fraction(0), 8)
        assert tower[2] == Fraction(5)  # S_2 = kappa
        for r in range(3, 9):
            assert tower[r] == Fraction(0), f"S_{r} != 0 for class G"

    def test_class_L_terminates_at_3(self):
        """Class L (alpha=1, S4=0): S_r = 0 for r >= 4."""
        tower = shadow_tower(Fraction(5), Fraction(1), Fraction(0), 8)
        assert tower[2] == Fraction(5)  # S_2 = kappa
        assert tower[3] == Fraction(1)  # S_3 = alpha
        for r in range(4, 9):
            assert tower[r] == Fraction(0), f"S_{r} != 0 for class L"

    def test_class_M_infinite(self):
        """Class M (S4 != 0): S_r != 0 for all r >= 4."""
        # Virasoro at c = 25 (k=300, so c = 1 - 6/302)
        # Use simple values instead
        tower = shadow_tower(Fraction(1), Fraction(2), Fraction(1, 10), 10)
        for r in range(4, 11):
            assert tower[r] != Fraction(0), f"S_{r} = 0 for class M"

    def test_S2_equals_kappa(self):
        """S_2 = kappa for all families."""
        for kap in [Fraction(1), Fraction(5), Fraction(-3, 2)]:
            tower = shadow_tower(kap, Fraction(1), Fraction(0), 3)
            assert tower[2] == kap

    def test_S3_equals_alpha(self):
        """S_3 = alpha for all families."""
        for alpha in [Fraction(0), Fraction(1), Fraction(2), Fraction(-1)]:
            tower = shadow_tower(Fraction(5), alpha, Fraction(0), 4)
            assert tower[3] == alpha

    def test_slN_shadow_data_class_L(self):
        """sl_N shadow data is class L with alpha=1, S4=0."""
        for N in [2, 3, 4, 5, 6]:
            sd = slN_shadow_data(N, Fraction(5))
            assert sd['alpha'] == Fraction(1)
            assert sd['S4'] == Fraction(0)
            assert sd['depth_class'] == 'L'
            assert sd['shadow_depth'] == 3

    def test_WN_shadow_data_class_M(self):
        """W_N shadow data is class M with alpha=2, S4 != 0."""
        for N in [2, 3, 4, 5, 6]:
            sd = WN_shadow_data(N, Fraction(5))
            assert sd['alpha'] == Fraction(2)
            assert sd['S4'] != Fraction(0)
            assert sd['depth_class'] == 'M'

    def test_virasoro_S4_formula(self):
        """S_4(Vir, c) = 10/(c(5c+22)) cross-checked at multiple levels."""
        for kv in [1, 2, 5, 10, 50]:
            k = Fraction(kv)
            c_v = c_WN(2, k)
            if c_v == 0 or 5 * c_v + 22 == 0:
                continue
            sd = WN_shadow_data(2, k)
            expected = Fraction(10) / (c_v * (5 * c_v + 22))
            assert sd['S4'] == expected

    def test_kappa_zero_gives_zero_tower(self):
        """kappa = 0 gives S_r = 0 for all r."""
        tower = shadow_tower(Fraction(0), Fraction(1), Fraction(1), 8)
        for r in range(2, 9):
            assert tower[r] == Fraction(0)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_slN_tower_terminates(self, N):
        """sl_N shadow tower terminates at arity 3."""
        sd = slN_shadow_data(N, Fraction(5))
        tower = shadow_tower(sd['kappa'], sd['alpha'], sd['S4'], 10)
        for r in range(4, 11):
            assert tower[r] == Fraction(0)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_WN_tower_infinite(self, N):
        """W_N shadow tower is infinite (all S_r != 0 for r >= 4)."""
        sd = WN_shadow_data(N, Fraction(5))
        tower = shadow_tower(sd['kappa'], sd['alpha'], sd['S4'], 10)
        for r in range(4, 11):
            assert tower[r] != Fraction(0), \
                f"S_{r}(W_{N}) = 0 but should be nonzero"


# ============================================================================
# Section 5: S_3 transformation under DS
# ============================================================================

class TestS3Transformation:
    """Test the cubic shadow transformation under DS."""

    def test_s3_slN_always_1(self):
        """S_3(sl_N) = alpha = 1 for all N and k."""
        for N in [2, 3, 4, 5, 6]:
            for kv in [1, 5, 10]:
                sd = slN_shadow_data(N, Fraction(kv))
                tower = shadow_tower(sd['kappa'], sd['alpha'], sd['S4'], 4)
                assert tower[3] == Fraction(1)

    def test_s3_WN_always_2(self):
        """S_3(W_N) = alpha = 2 on T-line for all N and k."""
        for N in [2, 3, 4, 5, 6]:
            for kv in [1, 5, 10]:
                sd = WN_shadow_data(N, Fraction(kv))
                tower = shadow_tower(sd['kappa'], sd['alpha'], sd['S4'], 4)
                assert tower[3] == Fraction(2)

    def test_s3_ratio_is_2(self):
        """S_3(W_N)/S_3(sl_N) = 2 universally."""
        result = s3_transformation()
        assert result['ratio_universal']
        assert result['ratio_value'] == Fraction(2)

    def test_s3_does_not_commute(self):
        """DS does NOT commute with S_3: S_3(W_N) != S_3(sl_N)."""
        for N in [2, 3, 4, 5, 6]:
            sd_aff = slN_shadow_data(N, Fraction(5))
            sd_w = WN_shadow_data(N, Fraction(5))
            t_aff = shadow_tower(sd_aff['kappa'], sd_aff['alpha'], sd_aff['S4'], 4)
            t_w = shadow_tower(sd_w['kappa'], sd_w['alpha'], sd_w['S4'], 4)
            assert t_aff[3] != t_w[3], f"S_3 commutes for N={N}"

    def test_s3_doubling_mechanism(self):
        """The doubling S_3: 1 -> 2 reflects Lie bracket -> Virasoro OPE.

        sl_N: alpha = 1 (Lie bracket structure constants f^{abc}).
        W_N T-line: alpha = 2 (stress-tensor OPE: 2T at z^{-2}).
        """
        for N in [2, 3, 4, 5, 6]:
            assert slN_shadow_data(N, Fraction(5))['alpha'] == Fraction(1)
            assert WN_shadow_data(N, Fraction(5))['alpha'] == Fraction(2)

    def test_s3_transformation_all_k(self):
        """S_3 ratio = 2 at many levels, not just k=5."""
        result = s3_transformation(
            k_values=[Fraction(n) for n in [1, 2, 3, 5, 10, 50, 100]]
        )
        assert result['ratio_universal']

    def test_s3_ratio_independent_of_N(self):
        """The ratio 2 does not depend on N."""
        for N in [2, 3, 4, 5, 6]:
            result = s3_transformation(N_values=[N])
            assert result['ratio_universal']

    def test_s3_ratio_independent_of_k(self):
        """The ratio 2 does not depend on k."""
        for kv in [1, 2, 3, 5, 10, 50]:
            result = s3_transformation(k_values=[Fraction(kv)])
            assert result['ratio_universal']


# ============================================================================
# Section 6: Depth increase L -> M
# ============================================================================

class TestDepthIncrease:
    """Test the universal depth increase from class L to class M."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_depth_increase_at_k5(self, N):
        """sl_N (class L, depth 3) -> W_N (class M, depth inf) at k=5."""
        cascade = ds_cascade(N, Fraction(5))
        assert cascade['depth_increase']
        assert cascade['depth_class_slN'] == 'L'
        assert cascade['depth_class_WN'] == 'M'

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_depth_increase_at_k1(self, N):
        """Depth increase at k=1."""
        cascade = ds_cascade(N, Fraction(1))
        assert cascade['depth_increase']

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_S4_zero_for_slN(self, N):
        """S_4(sl_N) = 0 for all N (Jacobi identity kills quartic)."""
        sd = slN_shadow_data(N, Fraction(5))
        tower = shadow_tower(sd['kappa'], sd['alpha'], sd['S4'], 5)
        assert tower[4] == Fraction(0)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_S4_nonzero_for_WN(self, N):
        """S_4(W_N) != 0 for all N (BRST creates quartic)."""
        sd = WN_shadow_data(N, Fraction(5))
        tower = shadow_tower(sd['kappa'], sd['alpha'], sd['S4'], 5)
        assert tower[4] != Fraction(0)

    def test_depth_increase_table_N2_through_6(self):
        """Depth increase table covers N=2..6."""
        table = depth_increase_table()
        assert len(table) == 5
        for row in table:
            assert row['depth_slN'] == 3
            assert row['depth_WN'] == 'inf'
            assert row['rho_slN'] == 0.0
            assert row['rho_WN'] > 0

    def test_depth_increase_universal(self):
        """Depth increase sl_N -> W_N is universal for all N >= 2."""
        for N in [2, 3, 4, 5, 6]:
            for kv in [1, 2, 5, 10, 50]:
                cascade = ds_cascade(N, Fraction(kv))
                assert cascade['depth_increase'], \
                    f"No depth increase for N={N}, k={kv}"


# ============================================================================
# Section 7: Cascade from quartic seed
# ============================================================================

class TestCascade:
    """Test that nonzero S_4 cascades to all higher arities."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_cascade_all_nonzero(self, N):
        """Once S_4(W_N) != 0, all S_r != 0 for r = 4..10."""
        cascade = ds_cascade(N, Fraction(5), max_arity=10)
        for r in range(4, 11):
            assert cascade['tower_WN'][r] != Fraction(0), \
                f"S_{r}(W_{N}) = 0 but cascade requires nonzero"

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_slN_tower_zero_from_4(self, N):
        """sl_N tower is zero from arity 4 onward."""
        cascade = ds_cascade(N, Fraction(5), max_arity=10)
        for r in range(4, 11):
            assert cascade['tower_slN'][r] == Fraction(0)

    def test_virasoro_s5_crosscheck(self):
        """S_5(Vir) = -48/(c^2(5c+22)) cross-checked at many levels."""
        result = virasoro_quintic_crosscheck()
        assert result['all_match']

    def test_s5_nonzero_all_N(self):
        """S_5(W_N) != 0 for N = 2..6 at k=5."""
        for N in [2, 3, 4, 5, 6]:
            cascade = ds_cascade(N, Fraction(5), max_arity=6)
            assert cascade['tower_WN'][5] != Fraction(0)

    def test_cascade_signs_virasoro(self):
        """For Virasoro at k=5 (c=1/7): S_4 > 0, S_5 < 0 (alternating signs)."""
        cascade = ds_cascade(2, Fraction(5), max_arity=6)
        assert cascade['tower_WN'][4] > 0  # S_4 = 10/(c(5c+22)) > 0 for c > 0
        assert cascade['tower_WN'][5] < 0  # S_5 = -48/(c^2(5c+22)) < 0

    def test_virasoro_s5_exact_k1(self):
        """S_5(Vir, k=1) = -48/((-1)^2 * (5*(-1)+22)) = -48/17."""
        c_v = c_WN(2, Fraction(1))
        assert c_v == Fraction(-1)
        cascade = ds_cascade(2, Fraction(1), max_arity=6)
        expected = Fraction(-48) / (c_v ** 2 * (5 * c_v + 22))
        assert expected == Fraction(-48, 17)
        assert cascade['tower_WN'][5] == expected

    def test_cascade_at_large_k(self):
        """Cascade persists at large k (asymptotic regime)."""
        for N in [2, 3, 4, 5, 6]:
            cascade = ds_cascade(N, Fraction(100), max_arity=8)
            for r in range(4, 9):
                assert cascade['tower_WN'][r] != Fraction(0)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_deficit_nonzero_at_arity_4(self, N):
        """The ghost deficit S_4(sl_N) - S_4(W_N) = -S_4(W_N) != 0."""
        cascade = ds_cascade(N, Fraction(5))
        comp = cascade['arity_comparison'][4]
        assert comp['deficit'] != Fraction(0)
        assert comp['deficit'] == -cascade['tower_WN'][4]  # since S_4(sl_N)=0


# ============================================================================
# Section 8: Growth rate
# ============================================================================

class TestGrowthRate:
    """Test shadow growth rate computation."""

    def test_class_G_rho_zero(self):
        """Class G (alpha=0, S4=0): rho = 0."""
        assert shadow_growth_rate(Fraction(5), Fraction(0), Fraction(0)) == 0.0

    def test_class_L_rho_zero(self):
        """Class L (alpha=1, S4=0): rho = 0 (finite tower)."""
        assert shadow_growth_rate(Fraction(5), Fraction(1), Fraction(0)) == 0.0

    def test_class_M_rho_positive(self):
        """Class M (S4 != 0): rho > 0."""
        rho = shadow_growth_rate(Fraction(1), Fraction(2), Fraction(1, 10))
        assert rho > 0

    def test_kappa_zero_rho_zero(self):
        """kappa = 0: rho = 0."""
        assert shadow_growth_rate(Fraction(0), Fraction(1), Fraction(1)) == 0.0

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_rho_increase_under_DS(self, N):
        """DS takes rho from 0 (class L) to > 0 (class M)."""
        cascade = ds_cascade(N, Fraction(5))
        assert cascade['rho_slN'] == 0.0
        assert cascade['rho_WN'] > 0
        assert cascade['rho_increase'] > 0

    def test_rho_WN_decreases_with_N(self):
        """At fixed k=5, rho(W_N) decreases with N for N >= 3.

        This is because larger N gives more negative c(W_N), hence
        larger |kappa(W_N)|, hence smaller rho.
        """
        rhos = []
        for N in [3, 4, 5, 6]:
            cascade = ds_cascade(N, Fraction(5))
            rhos.append(cascade['rho_WN'])
        for i in range(len(rhos) - 1):
            assert rhos[i + 1] < rhos[i], \
                f"rho does not decrease: rho(W_{i+3})={rhos[i]}, rho(W_{i+4})={rhos[i+1]}"

    def test_virasoro_rho_large_at_small_c(self):
        """Virasoro rho is large when c is small (near zero)."""
        # k=5: c = 1/7, very small, so rho should be large
        cascade = ds_cascade(2, Fraction(5))
        assert cascade['rho_WN'] > 10

    def test_rho_convergent_at_large_N(self):
        """For large N at k=5, the W_N tower converges (rho < 1)."""
        for N in [5, 6]:
            cascade = ds_cascade(N, Fraction(5))
            assert cascade['rho_WN'] < 1, \
                f"Tower diverges for N={N}: rho={cascade['rho_WN']}"


# ============================================================================
# Section 9: Commutation failure analysis
# ============================================================================

class TestCommutationFailure:
    """Test where the DS-shadow diagram fails to commute."""

    def test_first_failure_arity_2(self):
        """DS-shadow diagram first fails at arity 2 (kappa not additive).

        S_2 = kappa, and kappa(sl_N) != kappa(W_N), so the diagram
        fails at the very first arity. At the c level it commutes
        (c is additive), but S_2 is kappa, not c.
        """
        failures = commutation_failure_arity()
        for N in [2, 3, 4, 5, 6]:
            assert failures[N]['first_failure_arity'] == 2

    def test_s3_ratio_in_failure_analysis(self):
        """The S_3 ratio is 2 in the commutation failure analysis."""
        failures = commutation_failure_arity()
        for N in [2, 3, 4, 5, 6]:
            assert failures[N]['S3_ratio'] == Fraction(2)

    def test_s4_creation_in_failure_analysis(self):
        """S_4(sl_N) = 0 but S_4(W_N) != 0 in the failure analysis."""
        failures = commutation_failure_arity()
        for N in [2, 3, 4, 5, 6]:
            assert failures[N]['S4_slN'] == Fraction(0)
            assert failures[N]['S4_WN'] != Fraction(0)

    def test_c_level_does_commute(self):
        """At the central charge level, the diagram DOES commute."""
        for N in [2, 3, 4, 5, 6]:
            cascade = ds_cascade(N, Fraction(5))
            assert cascade['c_additive']

    def test_kappa_level_does_not_commute(self):
        """At the kappa level, the diagram does NOT commute (kappa not additive)."""
        for N in [2, 3, 4, 5, 6]:
            cascade = ds_cascade(N, Fraction(5))
            assert not cascade['kappa_additive']

    def test_arity_2_commutes_for_c_not_kappa(self):
        """Arity 2: c additive (commutes) but kappa not additive (fails)."""
        for N in [2, 3, 4, 5, 6]:
            cascade = ds_cascade(N, Fraction(5))
            # S_2 = kappa, so if kappa differs, the diagram fails at arity 2 too
            # But at the c level it commutes
            assert cascade['c_additive']
            comp2 = cascade['arity_comparison'][2]
            # S_2(sl_N) = kappa(sl_N) != S_2(W_N) = kappa(W_N) in general
            assert comp2['S_r_slN'] != comp2['S_r_WN']

    def test_all_arities_4plus_fail(self):
        """All arities 4+ fail (cascade from quartic creation)."""
        for N in [2, 3, 4, 5, 6]:
            cascade = ds_cascade(N, Fraction(5), max_arity=8)
            for r in range(4, 9):
                comp = cascade['arity_comparison'][r]
                assert not comp['ds_commutes']

    def test_full_cascade_all_N(self):
        """full_cascade_all_N returns results for all N = 2..6."""
        results = full_cascade_all_N()
        assert set(results.keys()) == {2, 3, 4, 5, 6}
        for N, data in results.items():
            assert data['depth_increase']
            assert data['c_additive']


# ============================================================================
# Section 10: Cross-engine consistency
# ============================================================================

class TestCrossEngineConsistency:
    """Cross-check against ds_shadow_cascade_engine and other modules."""

    def test_c_slN_matches_cascade_engine(self):
        """c_slN matches the existing ds_shadow_cascade_engine."""
        from compute.lib.ds_shadow_cascade_engine import (
            c_slN as c_slN_old,
        )
        for N in [2, 3, 4, 5]:
            for kv in [1, 5, 10]:
                assert c_slN(N, Fraction(kv)) == c_slN_old(N, Fraction(kv))

    def test_c_WN_matches_cascade_engine(self):
        """c_WN matches the existing ds_shadow_cascade_engine."""
        from compute.lib.ds_shadow_cascade_engine import (
            c_WN as c_WN_old,
        )
        for N in [2, 3, 4, 5]:
            for kv in [1, 5, 10]:
                assert c_WN(N, Fraction(kv)) == c_WN_old(N, Fraction(kv))

    def test_kappa_slN_matches_cascade_engine(self):
        """kappa_slN matches the existing ds_shadow_cascade_engine."""
        from compute.lib.ds_shadow_cascade_engine import (
            kappa_slN as kappa_slN_old,
        )
        for N in [2, 3, 4, 5]:
            for kv in [1, 5, 10]:
                assert kappa_slN(N, Fraction(kv)) == kappa_slN_old(N, Fraction(kv))

    def test_kappa_WN_matches_cascade_engine(self):
        """kappa_WN matches the existing ds_shadow_cascade_engine."""
        from compute.lib.ds_shadow_cascade_engine import (
            kappa_WN as kappa_WN_old,
        )
        for N in [2, 3, 4, 5]:
            for kv in [1, 5, 10]:
                assert kappa_WN(N, Fraction(kv)) == kappa_WN_old(N, Fraction(kv))

    def test_shadow_tower_matches_cascade_engine(self):
        """Shadow tower values match the existing engine for N=2..5."""
        from compute.lib.ds_shadow_cascade_engine import (
            shadow_tower_exact,
            WN_shadow_data_T_line,
        )
        for N in [2, 3, 4, 5]:
            sd_old = WN_shadow_data_T_line(N, Fraction(5))
            tower_old = shadow_tower_exact(
                sd_old['kappa'], sd_old['alpha'], sd_old['S4'], 8)
            sd_new = WN_shadow_data(N, Fraction(5))
            tower_new = shadow_tower(
                sd_new['kappa'], sd_new['alpha'], sd_new['S4'], 8)
            for r in range(2, 9):
                assert tower_new[r] == tower_old[r], \
                    f"Tower mismatch at r={r} for N={N}"

    def test_N6_not_in_old_engine(self):
        """N=6 is new in this module (old engine only does N=2..5).

        Verify N=6 data is self-consistent.
        """
        cascade = ds_cascade(6, Fraction(5))
        assert cascade['c_additive']
        assert cascade['depth_increase']
        assert cascade['rho_slN'] == 0.0
        assert cascade['rho_WN'] > 0
        # N=6: c_ghost = 30
        assert c_ghost(6) == Fraction(30)
        # N=6: anomaly ratio = H_6 - 1 = 29/20
        assert anomaly_ratio(6) == Fraction(29, 20)

    def test_virasoro_c_crosscheck_with_shadow_functor(self):
        """Cross-check c(Vir) with ds_shadow_functor module."""
        from compute.lib.ds_shadow_functor import (
            ds_level_to_central_charge,
        )
        from sympy import Rational
        for kv in [1, 5, 10]:
            c_ours = c_WN(2, Fraction(kv))
            # ds_level_to_central_charge(n, level) gives c(W_n) from level
            c_theirs = ds_level_to_central_charge(2, Rational(kv))
            assert float(c_ours) == pytest.approx(float(c_theirs), abs=1e-12)

    def test_depth_increase_matches_cascade_engine(self):
        """Depth increase results match the existing engine."""
        from compute.lib.ds_shadow_cascade_engine import (
            depth_increase_all_N,
        )
        old = depth_increase_all_N()
        for N in [2, 3, 4, 5]:
            new_cascade = ds_cascade(N, Fraction(5))
            assert new_cascade['depth_increase'] == old[N]['depth_increase']

    def test_verify_all_passes(self):
        """All internal verification checks pass."""
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"Internal check failed: {name}"

    def test_anomaly_ratio_matches_landscape(self):
        """Anomaly ratio matches landscape_census values.

        For Virasoro: rho = 1/2 (kappa = c/2).
        For W_3: rho = 5/6.
        """
        assert anomaly_ratio(2) == Fraction(1, 2)
        assert anomaly_ratio(3) == Fraction(5, 6)
