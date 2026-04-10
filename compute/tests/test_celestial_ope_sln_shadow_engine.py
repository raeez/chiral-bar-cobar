r"""Tests for celestial_ope_sln_shadow_engine.py.

Verifies celestial OPE coefficients S_2 (leading soft gluon = kappa)
and S_3 (subleading cubic shadow) extracted from the V_k(sl_N) shadow
tower at arity 2 and 3.  All expected values use exact rational
arithmetic (Fraction).

MULTI-PATH VERIFICATION:
  Path 1 [DC]: Direct computation from formulas
  Path 2 [LC]: Limiting cases k=0, k=-N, N=1
  Path 3 [CF]: Cross-family consistency (sl_2 vs sl_3 vs sl_4)
  Path 4 [DA]: Dimensional analysis / large-N scaling
  Path 5 [SY]: Symmetry checks (ratio formula algebraic identity)

References:
  CLAUDE.md C3: kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)
  CLAUDE.md C9: r^KM(z) = k*Omega/z
  CLAUDE.md C13: av(r(z)) = kappa at arity 2
  prop:arity-2-shadow-is-kappa (higher_genus_modular_koszul.tex)

CAUTIONS:
    AP1:   Every kappa from census, never from memory.
    AP10:  Every hardcoded expected value has 2+ independent derivation paths.
    AP126: r-matrix level prefix k mandatory. k=0 -> r=0.
    AP128: Expected values derived independently, NOT from engine output.
"""

import pytest
from fractions import Fraction

from compute.lib.celestial_ope_sln_shadow_engine import (
    dim_sln,
    dual_coxeter_number,
    shadow_s2,
    shadow_s3,
    shadow_ratio,
    verify_abelian_limit,
    verify_critical_level,
    shadow_table,
)

F = Fraction


# ============================================================
# 1. Basic Lie algebra data
# ============================================================

class TestLieAlgebraData:
    """Verify dim(sl_N) and h^v = N."""

    def test_dim_sl2(self):
        # VERIFIED [DC] 2^2 - 1 = 3, [LT] standard
        assert dim_sln(2) == 3

    def test_dim_sl3(self):
        # VERIFIED [DC] 3^2 - 1 = 8, [LT] standard
        assert dim_sln(3) == 8

    def test_dim_sl4(self):
        # VERIFIED [DC] 4^2 - 1 = 15, [LT] standard
        assert dim_sln(4) == 15

    def test_dim_sl5(self):
        # VERIFIED [DC] 5^2 - 1 = 24, [LT] standard
        assert dim_sln(5) == 24

    def test_dim_sl1(self):
        # sl_1 is trivial, dim = 0
        # VERIFIED [DC] 1^2 - 1 = 0, [LT] abelian
        assert dim_sln(1) == 0

    def test_dual_coxeter_sl2(self):
        # VERIFIED [LT] h^v(sl_2) = 2
        assert dual_coxeter_number(2) == 2

    def test_dual_coxeter_sl3(self):
        # VERIFIED [LT] h^v(sl_3) = 3
        assert dual_coxeter_number(3) == 3

    def test_invalid_N(self):
        with pytest.raises(ValueError):
            dim_sln(0)
        with pytest.raises(ValueError):
            dual_coxeter_number(-1)


# ============================================================
# 2. Arity-2 shadow S_2 = kappa
# ============================================================

class TestShadowS2:
    """S_2 = kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N)."""

    def test_sl2_k1(self):
        # kappa = 3*(1+2)/(2*2) = 9/4
        # VERIFIED [DC] direct, [LC] k=0 -> 3/2, k=-2 -> 0
        assert shadow_s2(2, 1) == F(9, 4)

    def test_sl3_k1(self):
        # kappa = 8*(1+3)/(2*3) = 32/6 = 16/3
        # VERIFIED [DC] direct, [LC] k=0 -> 4, k=-3 -> 0
        assert shadow_s2(3, 1) == F(16, 3)

    def test_sl4_k1(self):
        # kappa = 15*(1+4)/(2*4) = 75/8
        # VERIFIED [DC] direct, [LC] k=0 -> 15/2
        assert shadow_s2(4, 1) == F(75, 8)

    def test_sl2_k2(self):
        # kappa = 3*(2+2)/(2*2) = 12/4 = 3
        # VERIFIED [DC] direct, [CF] 2*kappa(sl2,k=1) - kappa(sl2,k=0)
        #   = 2*(9/4) - 3/2 = 9/2 - 3/2 = 3. Linear in k: yes.
        assert shadow_s2(2, 2) == F(3)

    def test_sl3_k2(self):
        # kappa = 8*(2+3)/(2*3) = 40/6 = 20/3
        # VERIFIED [DC] direct, [LC] linearity check
        assert shadow_s2(3, 2) == F(20, 3)

    def test_sl2_k0_sugawara_shift(self):
        # kappa(V_0(sl_2)) = 3*(0+2)/(2*2) = 6/4 = 3/2
        # NOT zero: Sugawara shift h^v = 2 contributes.
        # VERIFIED [DC] direct, [LT] CLAUDE.md C3: k=0 -> dim(g)/2
        assert shadow_s2(2, 0) == F(3, 2)

    def test_sl3_k0_sugawara_shift(self):
        # kappa(V_0(sl_3)) = 8*(0+3)/(2*3) = 24/6 = 4
        # VERIFIED [DC] direct, [LT] dim(g)/2 = 8/2 = 4
        assert shadow_s2(3, 0) == F(4)

    def test_linearity_in_k(self):
        """S_2 is linear in k: S_2(N,k) = (N^2-1)/(2N) * k + (N^2-1)/2."""
        # VERIFIED [DA] coefficient of k is dim/(2h^v) = (N^2-1)/(2N)
        for N in [2, 3, 4, 5]:
            slope = F(N * N - 1, 2 * N)
            intercept = F(N * N - 1, 2)
            for k in [0, 1, 2, 3]:
                expected = slope * k + intercept
                assert shadow_s2(N, k) == expected

    def test_sl1_trivial(self):
        # dim(sl_1) = 0, so kappa = 0 for all k.
        # VERIFIED [DC] 0*(k+1)/(2*1) = 0
        for k in [0, 1, 2, -1]:
            assert shadow_s2(1, k) == F(0)


# ============================================================
# 3. Arity-3 shadow S_3
# ============================================================

class TestShadowS3:
    """S_3 = k^2 * (N^2-1) / (4N)."""

    def test_sl2_k1(self):
        # S_3 = 1^2 * 3 / (4*2) = 3/8
        # VERIFIED [DC] direct, [LC] k=0 -> 0
        assert shadow_s3(2, 1) == F(3, 8)

    def test_sl3_k1(self):
        # S_3 = 1^2 * 8 / (4*3) = 8/12 = 2/3
        # VERIFIED [DC] direct, [LC] k=0 -> 0
        assert shadow_s3(3, 1) == F(2, 3)

    def test_sl4_k1(self):
        # S_3 = 1^2 * 15 / (4*4) = 15/16
        # VERIFIED [DC] direct, [LC] k=0 -> 0
        assert shadow_s3(4, 1) == F(15, 16)

    def test_sl2_k2(self):
        # S_3 = 4 * 3 / 8 = 12/8 = 3/2
        # VERIFIED [DC] direct, [SY] quadratic in k: 4 * S_3(2,1) = 4*(3/8)=3/2
        assert shadow_s3(2, 2) == F(3, 2)

    def test_sl3_k2(self):
        # S_3 = 4 * 8 / 12 = 32/12 = 8/3
        # VERIFIED [DC] direct, [SY] 4 * S_3(3,1) = 4*(2/3) = 8/3
        assert shadow_s3(3, 2) == F(8, 3)

    def test_quadratic_in_k(self):
        """S_3 is quadratic in k: S_3(N, 2k) = 4 * S_3(N, k)."""
        # VERIFIED [DA] k^2 scaling
        for N in [2, 3, 4, 5]:
            for k in [1, 2, 3]:
                assert shadow_s3(N, 2 * k) == 4 * shadow_s3(N, k)

    def test_k0_vanishes(self):
        """S_3 = 0 at k = 0 for all N (abelian limit, AP141)."""
        # VERIFIED [LC] k^2 * anything = 0 at k=0
        for N in [1, 2, 3, 4, 5, 10]:
            assert shadow_s3(N, 0) == F(0)

    def test_sl1_trivial(self):
        # dim(sl_1) = 0, so S_3 = 0 for all k.
        # VERIFIED [DC] k^2 * 0 / 4 = 0
        for k in [0, 1, 2, -1, 5]:
            assert shadow_s3(1, k) == F(0)

    def test_negative_k(self):
        # S_3(N, -k) = S_3(N, k) since k enters as k^2.
        # VERIFIED [SY] k^2 = (-k)^2
        for N in [2, 3, 4]:
            for k in [1, 2, 3]:
                assert shadow_s3(N, -k) == shadow_s3(N, k)


# ============================================================
# 4. Shadow ratio S_3 / S_2
# ============================================================

class TestShadowRatio:
    """Ratio S_3/S_2 = k^2 / (2(k+N))."""

    def test_sl2_k1(self):
        # ratio = 1 / (2*(1+2)) = 1/6
        # VERIFIED [DC] direct, [DC] S_3/S_2 = (3/8)/(9/4) = (3/8)*(4/9) = 12/72 = 1/6
        assert shadow_ratio(2, 1) == F(1, 6)

    def test_sl3_k1(self):
        # ratio = 1 / (2*(1+3)) = 1/8
        # VERIFIED [DC] direct, [DC] S_3/S_2 = (2/3)/(16/3) = 2/16 = 1/8
        assert shadow_ratio(3, 1) == F(1, 8)

    def test_sl4_k1(self):
        # ratio = 1 / (2*(1+4)) = 1/10
        # VERIFIED [DC] direct, [DC] S_3/S_2 = (15/16)/(75/8) = (15/16)*(8/75) = 120/1200 = 1/10
        assert shadow_ratio(4, 1) == F(1, 10)

    def test_sl2_k2(self):
        # ratio = 4 / (2*(2+2)) = 4/8 = 1/2
        # VERIFIED [DC] direct, [DC] S_3/S_2 = (3/2)/3 = 1/2
        assert shadow_ratio(2, 2) == F(1, 2)

    def test_sl3_k3(self):
        # ratio = 9 / (2*(3+3)) = 9/12 = 3/4
        # VERIFIED [DC] k^2/(2(k+N)) = 9/12 = 3/4
        assert shadow_ratio(3, 3) == F(3, 4)

    def test_ratio_formula_identity(self):
        """Verify S_3/S_2 = k^2/(2(k+N)) algebraically for a grid."""
        # VERIFIED [DC] algebraic identity from formula simplification
        for N in [2, 3, 4, 5]:
            for k in [1, 2, 3, 4, 5]:
                expected = F(k * k, 2 * (k + N))
                assert shadow_ratio(N, k) == expected

    def test_critical_level_raises(self):
        """Ratio undefined at k = -N (critical level, S_2 = 0)."""
        for N in [2, 3, 4, 5]:
            with pytest.raises(ZeroDivisionError):
                shadow_ratio(N, -N)

    def test_k0_ratio(self):
        """At k = 0: S_3 = 0 but S_2 != 0, so ratio = 0."""
        # VERIFIED [LC] 0^2 / (2*(0+N)) = 0
        for N in [2, 3, 4, 5]:
            assert shadow_ratio(N, 0) == F(0)


# ============================================================
# 5. Abelian limit (k = 0) verification
# ============================================================

class TestAbelianLimit:
    """AP126/AP141: at k=0, r(z) = 0 so S_3 = 0.  S_2 = dim(g)/2."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_s3_vanishes(self, N):
        # VERIFIED [LC] AP141 k=0 -> r=0 -> cubic shadow = 0
        result = verify_abelian_limit(N)
        assert result['S_3_is_zero'] is True

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_s2_equals_dim_over_2(self, N):
        # VERIFIED [DC] (N^2-1)(0+N)/(2N) = (N^2-1)/2, [LT] CLAUDE.md C3
        result = verify_abelian_limit(N)
        assert result['S_2'] == result['S_2_expected']
        assert result['S_2'] == F(N * N - 1, 2)

    @pytest.mark.parametrize("N,expected_s2", [
        (2, F(3, 2)),   # VERIFIED [DC] 3/2
        (3, F(4)),       # VERIFIED [DC] 8/2 = 4
        (4, F(15, 2)),  # VERIFIED [DC] 15/2
        (5, F(12)),      # VERIFIED [DC] 24/2 = 12
    ])
    def test_s2_explicit(self, N, expected_s2):
        assert shadow_s2(N, 0) == expected_s2


# ============================================================
# 6. Critical level (k = -N) verification
# ============================================================

class TestCriticalLevel:
    """At k = -N: S_2 = 0, S_3 = N*dim(g)/4."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_s2_vanishes(self, N):
        # VERIFIED [DC] (N^2-1)*(-N+N)/(2N) = 0, [LT] CLAUDE.md C3: k=-h^v -> 0
        result = verify_critical_level(N)
        assert result['S_2_is_zero'] is True

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_s3_nonzero(self, N):
        # S_3 = N^2 * (N^2-1) / (4N) = N*(N^2-1)/4
        # VERIFIED [DC] (-N)^2 = N^2, [SY] S_3(-k) = S_3(k)
        result = verify_critical_level(N)
        assert result['S_3_matches'] is True
        expected = F(N * (N * N - 1), 4)
        assert result['S_3'] == expected

    @pytest.mark.parametrize("N,expected_s3", [
        (2, F(3, 2)),    # VERIFIED [DC] 2*3/4 = 3/2
        (3, F(6)),        # VERIFIED [DC] 3*8/4 = 6
        (4, F(15)),       # VERIFIED [DC] 4*15/4 = 15
        (5, F(30)),       # VERIFIED [DC] 5*24/4 = 30
    ])
    def test_s3_explicit(self, N, expected_s3):
        result = verify_critical_level(N)
        assert result['S_3'] == expected_s3


# ============================================================
# 7. Large-N scaling
# ============================================================

class TestLargeNScaling:
    """Asymptotic behaviour as N -> infinity at fixed k."""

    def test_s2_large_n(self):
        """S_2 ~ N*k/2 + N/2 for large N (leading: N^2*k/(2N) = Nk/2)."""
        # VERIFIED [DA] leading term of (N^2-1)(k+N)/(2N) at large N
        #   = N^2*(k+N)/(2N) = N(k+N)/2 ~ Nk/2 for k fixed, N large.
        # Actually: (N^2-1)(k+N)/(2N). For large N:
        #   ~ N^2(k+N)/(2N) = N(k+N)/2 = Nk/2 + N^2/2.
        # Ratio S_2 / (N^2/2) -> 1 as N -> inf for fixed k.
        k = 1
        for N in [50, 100, 200]:
            s2 = shadow_s2(N, k)
            leading = F(N * N, 2)  # N^2/2 (not Nk/2; N^2/2 dominates)
            ratio = s2 / leading
            # ratio = (N^2-1)(k+N)/(2N) / (N^2/2)
            #       = (N^2-1)(k+N) / (N^3)
            #       ~ (k+N)/N -> 1 for large N
            assert abs(float(ratio) - 1.0) < 0.05

    def test_ratio_large_n(self):
        """S_3/S_2 = k^2/(2(k+N)) -> 0 as N -> inf for fixed k."""
        # VERIFIED [DA] k^2/(2(k+N)) -> 0
        k = 1
        for N in [100, 1000]:
            r = shadow_ratio(N, k)
            assert r < F(1, 100)


# ============================================================
# 8. Shadow table
# ============================================================

class TestShadowTable:
    """Test the bulk table computation."""

    def test_table_structure(self):
        table = shadow_table(range(2, 4), range(1, 3))
        # 2 values of N * 2 values of k = 4 rows
        assert len(table) == 4

    def test_table_values(self):
        table = shadow_table(range(2, 3), range(1, 2))
        row = table[0]
        assert row['N'] == 2
        assert row['k'] == 1
        assert row['S_2'] == F(9, 4)
        assert row['S_3'] == F(3, 8)
        assert row['ratio'] == F(1, 6)

    def test_table_critical_level(self):
        """Table at critical level has ratio = None."""
        table = shadow_table(range(2, 3), range(-2, -1))
        row = table[0]
        assert row['N'] == 2
        assert row['k'] == -2
        assert row['S_2'] == F(0)
        assert row['ratio'] is None


# ============================================================
# 9. Cross-consistency checks
# ============================================================

class TestCrossConsistency:
    """Relations between S_2, S_3, and the ratio."""

    def test_s3_equals_ratio_times_s2(self):
        """S_3 = ratio * S_2 by definition."""
        # VERIFIED [DC] tautological consistency
        for N in [2, 3, 4, 5]:
            for k in [1, 2, 3]:
                s2 = shadow_s2(N, k)
                s3 = shadow_s3(N, k)
                r = shadow_ratio(N, k)
                assert s3 == r * s2

    def test_s2_times_2n_is_integer_poly(self):
        """2N * S_2 = (N^2-1)(k+N) is always integer for integer k."""
        # VERIFIED [DA] clearing denominator
        for N in [2, 3, 4, 5]:
            for k in range(-5, 6):
                val = shadow_s2(N, k) * 2 * N
                assert val.denominator == 1

    def test_s3_times_4n_is_integer_poly(self):
        """4N * S_3 = k^2 * (N^2-1) is always integer for integer k."""
        # VERIFIED [DA] clearing denominator
        for N in [2, 3, 4, 5]:
            for k in range(-5, 6):
                val = shadow_s3(N, k) * 4 * N
                assert val.denominator == 1

    def test_fractional_level(self):
        """Engine handles fractional k (e.g. admissible levels)."""
        # k = -1/2 for sl_2: admissible level
        k = F(-1, 2)
        s2 = shadow_s2(2, k)
        # (3)*(-1/2 + 2)/(4) = 3*(3/2)/4 = 9/8
        # VERIFIED [DC] direct
        assert s2 == F(9, 8)
        s3 = shadow_s3(2, k)
        # (1/4)*3/8 = 3/32
        # VERIFIED [DC] (-1/2)^2 * 3 / 8 = (1/4)*3/8 = 3/32
        assert s3 == F(3, 32)
