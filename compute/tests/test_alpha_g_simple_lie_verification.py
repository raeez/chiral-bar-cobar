r"""Tests for alpha_g_simple_lie_verification_engine.py.

Verifies alpha_g = 2*rank + 4*dim*h^v for all 31 simple Lie algebras
in types A_1--A_8, B_2--B_8, C_3--C_8, D_4--D_8, G_2, F_4, E_6, E_7, E_8.

MULTI-PATH VERIFICATION:
  Path 1: [DC] Direct computation from formula 2*rank + 4*dim*h^v
  Path 2: [CF] Cross-family consistency (B_n/C_n share dim, differ in h^v)
  Path 3: [LC] Limiting/boundary cases (A_1=sl_2, smallest of each type)
  Path 4: Classical dim/h^v cross-check against rank formulas
  Path 5: Isomorphism checks (B_2=C_2, D_3=A_3)
  Path 6: Decomposition: alpha_g = rank_contribution + curvature_contribution

References:
  Bourbaki, Lie Groups and Lie Algebras, Ch. IV-VI (Tables)
  Humphreys, Introduction to Lie Algebras, Table p. 66
  Kac, Infinite-Dimensional Lie Algebras, Table Aff 1 (dual Coxeter numbers)
"""

import pytest

from compute.lib.alpha_g_simple_lie_verification_engine import (
    LIE_ALGEBRA_TABLE,
    AlphaResult,
    LieAlgebraData,
    alpha_g,
    alpha_g_for_algebra,
    check_b2_c2_isomorphism,
    check_d3_a3_isomorphism,
    compute_all_alpha_g,
    verify_all_classical_data,
    verify_alpha_g_integrality,
    verify_alpha_g_positivity,
    verify_classical_dim,
    verify_classical_dual_coxeter,
)


# ============================================================
# 1. Table completeness
# ============================================================

class TestTableCompleteness:
    """Verify the Lie algebra table has exactly the right entries."""

    def test_total_count(self):
        """8 (A) + 7 (B) + 6 (C) + 5 (D) + 5 (exc) = 31 algebras."""
        assert len(LIE_ALGEBRA_TABLE) == 31

    def test_a_series_count(self):
        a_algebras = [n for n, d in LIE_ALGEBRA_TABLE.items() if d.series == 'A']
        assert len(a_algebras) == 8  # A1--A8

    def test_b_series_count(self):
        b_algebras = [n for n, d in LIE_ALGEBRA_TABLE.items() if d.series == 'B']
        assert len(b_algebras) == 7  # B2--B8

    def test_c_series_count(self):
        c_algebras = [n for n, d in LIE_ALGEBRA_TABLE.items() if d.series == 'C']
        assert len(c_algebras) == 6  # C3--C8

    def test_d_series_count(self):
        d_algebras = [n for n, d in LIE_ALGEBRA_TABLE.items() if d.series == 'D']
        assert len(d_algebras) == 5  # D4--D8

    def test_exceptional_count(self):
        exc = [n for n, d in LIE_ALGEBRA_TABLE.items() if d.series == 'EXC']
        assert len(exc) == 5  # G2, F4, E6, E7, E8

    def test_all_names_present(self):
        expected = set()
        for n in range(1, 9):
            expected.add(f'A{n}')
        for n in range(2, 9):
            expected.add(f'B{n}')
        for n in range(3, 9):
            expected.add(f'C{n}')
        for n in range(4, 9):
            expected.add(f'D{n}')
        expected.update(['G2', 'F4', 'E6', 'E7', 'E8'])
        assert set(LIE_ALGEBRA_TABLE.keys()) == expected


# ============================================================
# 2. Classical data cross-checks
# ============================================================

class TestClassicalDataCrossChecks:
    """Verify dim and h^v from rank formulas for classical types."""

    def test_all_classical_data_pass(self):
        failures = verify_all_classical_data()
        assert failures == [], f'Classical data failures: {failures}'

    @pytest.mark.parametrize('n', range(1, 9))
    def test_a_dim(self, n):
        """A_n: dim = n(n+2)."""
        data = LIE_ALGEBRA_TABLE[f'A{n}']
        assert data.dim == n * (n + 2)

    @pytest.mark.parametrize('n', range(1, 9))
    def test_a_dual_coxeter(self, n):
        """A_n: h^v = n+1."""
        data = LIE_ALGEBRA_TABLE[f'A{n}']
        assert data.dual_coxeter == n + 1

    @pytest.mark.parametrize('n', range(2, 9))
    def test_b_dim(self, n):
        """B_n: dim = n(2n+1)."""
        data = LIE_ALGEBRA_TABLE[f'B{n}']
        assert data.dim == n * (2 * n + 1)

    @pytest.mark.parametrize('n', range(2, 9))
    def test_b_dual_coxeter(self, n):
        """B_n: h^v = 2n-1."""
        data = LIE_ALGEBRA_TABLE[f'B{n}']
        assert data.dual_coxeter == 2 * n - 1

    @pytest.mark.parametrize('n', range(3, 9))
    def test_c_dim(self, n):
        """C_n: dim = n(2n+1)."""
        data = LIE_ALGEBRA_TABLE[f'C{n}']
        assert data.dim == n * (2 * n + 1)

    @pytest.mark.parametrize('n', range(3, 9))
    def test_c_dual_coxeter(self, n):
        """C_n: h^v = n+1."""
        data = LIE_ALGEBRA_TABLE[f'C{n}']
        assert data.dual_coxeter == n + 1

    @pytest.mark.parametrize('n', range(4, 9))
    def test_d_dim(self, n):
        """D_n: dim = n(2n-1)."""
        data = LIE_ALGEBRA_TABLE[f'D{n}']
        assert data.dim == n * (2 * n - 1)

    @pytest.mark.parametrize('n', range(4, 9))
    def test_d_dual_coxeter(self, n):
        """D_n: h^v = 2n-2."""
        data = LIE_ALGEBRA_TABLE[f'D{n}']
        assert data.dual_coxeter == 2 * n - 2


# ============================================================
# 3. Exceptional algebra data
# ============================================================

class TestExceptionalData:
    """Verify exceptional algebra dimensions and dual Coxeter numbers."""

    def test_g2(self):
        # VERIFIED [DC] Bourbaki Table VI + [LT] Humphreys p.66
        d = LIE_ALGEBRA_TABLE['G2']
        assert (d.rank, d.dim, d.dual_coxeter) == (2, 14, 4)

    def test_f4(self):
        # VERIFIED [DC] Bourbaki Table VIII + [LT] Humphreys p.66
        d = LIE_ALGEBRA_TABLE['F4']
        assert (d.rank, d.dim, d.dual_coxeter) == (4, 52, 9)

    def test_e6(self):
        # VERIFIED [DC] Bourbaki Table V + [LT] Kac, Table Aff 1
        d = LIE_ALGEBRA_TABLE['E6']
        assert (d.rank, d.dim, d.dual_coxeter) == (6, 78, 12)

    def test_e7(self):
        # VERIFIED [DC] Bourbaki Table VI + [LT] Kac, Table Aff 1
        d = LIE_ALGEBRA_TABLE['E7']
        assert (d.rank, d.dim, d.dual_coxeter) == (7, 133, 18)

    def test_e8(self):
        # VERIFIED [DC] Bourbaki Table VII + [LT] Kac, Table Aff 1
        d = LIE_ALGEBRA_TABLE['E8']
        assert (d.rank, d.dim, d.dual_coxeter) == (8, 248, 30)


# ============================================================
# 4. Individual alpha_g values -- A series
# ============================================================

class TestAlphaA:
    """alpha_g for A_n = sl_{n+1}, n=1..8."""

    def test_a1(self):
        # A1=sl2: 2*1 + 4*3*2 = 2 + 24 = 26
        # VERIFIED [DC] 2*1+4*3*2=26 + [LC] smallest simple algebra, dim(sl2)=3
        assert alpha_g_for_algebra('A1') == 26

    def test_a2(self):
        # A2=sl3: 2*2 + 4*8*3 = 4 + 96 = 100
        # VERIFIED [DC] 2*2+4*8*3=100 + [CF] dim(sl3)=8=3^2-1 cross-check
        assert alpha_g_for_algebra('A2') == 100

    def test_a3(self):
        # A3=sl4: 2*3 + 4*15*4 = 6 + 240 = 246
        # VERIFIED [DC] 2*3+4*15*4=246 + [CF] dim=15=4^2-1, h^v=4
        assert alpha_g_for_algebra('A3') == 246

    def test_a4(self):
        # A4=sl5: 2*4 + 4*24*5 = 8 + 480 = 488
        # VERIFIED [DC] 2*4+4*24*5=488 + [CF] dim=24=5^2-1
        assert alpha_g_for_algebra('A4') == 488

    def test_a5(self):
        # A5=sl6: 2*5 + 4*35*6 = 10 + 840 = 850
        # VERIFIED [DC] 2*5+4*35*6=850 + [CF] dim=35=6^2-1
        assert alpha_g_for_algebra('A5') == 850

    def test_a6(self):
        # A6=sl7: 2*6 + 4*48*7 = 12 + 1344 = 1356
        # VERIFIED [DC] 2*6+4*48*7=1356 + [CF] dim=48=7^2-1
        assert alpha_g_for_algebra('A6') == 1356

    def test_a7(self):
        # A7=sl8: 2*7 + 4*63*8 = 14 + 2016 = 2030
        # VERIFIED [DC] 2*7+4*63*8=2030 + [CF] dim=63=8^2-1
        assert alpha_g_for_algebra('A7') == 2030

    def test_a8(self):
        # A8=sl9: 2*8 + 4*80*9 = 16 + 2880 = 2896
        # VERIFIED [DC] 2*8+4*80*9=2896 + [CF] dim=80=9^2-1
        assert alpha_g_for_algebra('A8') == 2896


# ============================================================
# 5. Individual alpha_g values -- B series
# ============================================================

class TestAlphaB:
    """alpha_g for B_n = so_{2n+1}, n=2..8."""

    def test_b2(self):
        # B2=so5: 2*2 + 4*10*3 = 4 + 120 = 124
        # VERIFIED [DC] 2*2+4*10*3=124 + [LC] B2=C2 isomorphism, dim(so5)=10
        assert alpha_g_for_algebra('B2') == 124

    def test_b3(self):
        # B3=so7: 2*3 + 4*21*5 = 6 + 420 = 426
        # VERIFIED [DC] 2*3+4*21*5=426 + [CF] dim=21=3*7
        assert alpha_g_for_algebra('B3') == 426

    def test_b4(self):
        # B4=so9: 2*4 + 4*36*7 = 8 + 1008 = 1016
        # VERIFIED [DC] 2*4+4*36*7=1016 + [CF] dim=36=4*9
        assert alpha_g_for_algebra('B4') == 1016

    def test_b5(self):
        # B5=so11: 2*5 + 4*55*9 = 10 + 1980 = 1990
        # VERIFIED [DC] 2*5+4*55*9=1990 + [CF] dim=55=5*11
        assert alpha_g_for_algebra('B5') == 1990

    def test_b6(self):
        # B6=so13: 2*6 + 4*78*11 = 12 + 3432 = 3444
        # VERIFIED [DC] 2*6+4*78*11=3444 + [CF] dim=78=6*13
        assert alpha_g_for_algebra('B6') == 3444

    def test_b7(self):
        # B7=so15: 2*7 + 4*105*13 = 14 + 5460 = 5474
        # VERIFIED [DC] 2*7+4*105*13=5474 + [CF] dim=105=7*15
        assert alpha_g_for_algebra('B7') == 5474

    def test_b8(self):
        # B8=so17: 2*8 + 4*136*15 = 16 + 8160 = 8176
        # VERIFIED [DC] 2*8+4*136*15=8176 + [CF] dim=136=8*17
        assert alpha_g_for_algebra('B8') == 8176


# ============================================================
# 6. Individual alpha_g values -- C series
# ============================================================

class TestAlphaC:
    """alpha_g for C_n = sp_{2n}, n=3..8."""

    def test_c3(self):
        # C3=sp6: 2*3 + 4*21*4 = 6 + 336 = 342
        # VERIFIED [DC] 2*3+4*21*4=342 + [CF] dim(C3)=dim(B3)=21, h^v differs
        assert alpha_g_for_algebra('C3') == 342

    def test_c4(self):
        # C4=sp8: 2*4 + 4*36*5 = 8 + 720 = 728
        # VERIFIED [DC] 2*4+4*36*5=728 + [CF] dim(C4)=dim(B4)=36, h^v=5 vs 7
        assert alpha_g_for_algebra('C4') == 728

    def test_c5(self):
        # C5=sp10: 2*5 + 4*55*6 = 10 + 1320 = 1330
        # VERIFIED [DC] 2*5+4*55*6=1330 + [CF] dim(C5)=dim(B5)=55
        assert alpha_g_for_algebra('C5') == 1330

    def test_c6(self):
        # C6=sp12: 2*6 + 4*78*7 = 12 + 2184 = 2196
        # VERIFIED [DC] 2*6+4*78*7=2196 + [CF] dim(C6)=dim(B6)=78
        assert alpha_g_for_algebra('C6') == 2196

    def test_c7(self):
        # C7=sp14: 2*7 + 4*105*8 = 14 + 3360 = 3374
        # VERIFIED [DC] 2*7+4*105*8=3374 + [CF] dim(C7)=dim(B7)=105
        assert alpha_g_for_algebra('C7') == 3374

    def test_c8(self):
        # C8=sp16: 2*8 + 4*136*9 = 16 + 4896 = 4912
        # VERIFIED [DC] 2*8+4*136*9=4912 + [CF] dim(C8)=dim(B8)=136
        assert alpha_g_for_algebra('C8') == 4912


# ============================================================
# 7. Individual alpha_g values -- D series
# ============================================================

class TestAlphaD:
    """alpha_g for D_n = so_{2n}, n=4..8."""

    def test_d4(self):
        # D4=so8: 2*4 + 4*28*6 = 8 + 672 = 680
        # VERIFIED [DC] 2*4+4*28*6=680 + [SY] D4 triality: S3 symmetry on 3 fund reps
        assert alpha_g_for_algebra('D4') == 680

    def test_d5(self):
        # D5=so10: 2*5 + 4*45*8 = 10 + 1440 = 1450
        # VERIFIED [DC] 2*5+4*45*8=1450 + [CF] dim=45=5*9
        assert alpha_g_for_algebra('D5') == 1450

    def test_d6(self):
        # D6=so12: 2*6 + 4*66*10 = 12 + 2640 = 2652
        # VERIFIED [DC] 2*6+4*66*10=2652 + [CF] dim=66=6*11
        assert alpha_g_for_algebra('D6') == 2652

    def test_d7(self):
        # D7=so14: 2*7 + 4*91*12 = 14 + 4368 = 4382
        # VERIFIED [DC] 2*7+4*91*12=4382 + [CF] dim=91=7*13
        assert alpha_g_for_algebra('D7') == 4382

    def test_d8(self):
        # D8=so16: 2*8 + 4*120*14 = 16 + 6720 = 6736
        # VERIFIED [DC] 2*8+4*120*14=6736 + [CF] dim=120=8*15
        assert alpha_g_for_algebra('D8') == 6736


# ============================================================
# 8. Individual alpha_g values -- Exceptionals
# ============================================================

class TestAlphaExceptional:
    """alpha_g for G_2, F_4, E_6, E_7, E_8."""

    def test_g2(self):
        # G2: 2*2 + 4*14*4 = 4 + 224 = 228
        # VERIFIED [DC] 2*2+4*14*4=228 + [LT] dim(G2)=14, h^v=4 (Bourbaki)
        assert alpha_g_for_algebra('G2') == 228

    def test_f4(self):
        # F4: 2*4 + 4*52*9 = 8 + 1872 = 1880
        # VERIFIED [DC] 2*4+4*52*9=1880 + [LT] dim(F4)=52, h^v=9 (Bourbaki)
        assert alpha_g_for_algebra('F4') == 1880

    def test_e6(self):
        # E6: 2*6 + 4*78*12 = 12 + 3744 = 3756
        # VERIFIED [DC] 2*6+4*78*12=3756 + [LT] dim(E6)=78, h^v=12 (Kac)
        assert alpha_g_for_algebra('E6') == 3756

    def test_e7(self):
        # E7: 2*7 + 4*133*18 = 14 + 9576 = 9590
        # VERIFIED [DC] 2*7+4*133*18=9590 + [LT] dim(E7)=133, h^v=18 (Kac)
        assert alpha_g_for_algebra('E7') == 9590

    def test_e8(self):
        # E8: 2*8 + 4*248*30 = 16 + 29760 = 29776
        # VERIFIED [DC] 2*8+4*248*30=29776 + [LT] dim(E8)=248, h^v=30 (Kac)
        assert alpha_g_for_algebra('E8') == 29776


# ============================================================
# 9. Structural properties
# ============================================================

class TestStructuralProperties:
    """Global properties of alpha_g across all algebras."""

    def test_all_positive(self):
        failures = verify_alpha_g_positivity()
        assert failures == [], f'Positivity failures: {failures}'

    def test_all_integer(self):
        failures = verify_alpha_g_integrality()
        assert failures == [], f'Integrality failures: {failures}'

    def test_all_even(self):
        """alpha_g = 2*rank + 4*dim*h^v is always even (both terms even)."""
        results = compute_all_alpha_g()
        for name, r in results.items():
            assert r.alpha_g % 2 == 0, f'{name}: alpha_g={r.alpha_g} is odd'

    def test_decomposition(self):
        """alpha_g = rank_contribution + curvature_contribution."""
        results = compute_all_alpha_g()
        for name, r in results.items():
            assert r.alpha_g == r.rank_contribution + r.curvature_contribution, (
                f'{name}: {r.alpha_g} != {r.rank_contribution} + {r.curvature_contribution}')

    def test_curvature_dominates(self):
        """4*dim*h^v >> 2*rank for all algebras (curvature term dominates)."""
        results = compute_all_alpha_g()
        for name, r in results.items():
            assert r.curvature_contribution > r.rank_contribution, (
                f'{name}: curvature {r.curvature_contribution} <= rank {r.rank_contribution}')

    def test_monotone_in_rank_within_a(self):
        """Within A-series, alpha_g is strictly increasing in rank."""
        prev = 0
        for n in range(1, 9):
            val = alpha_g_for_algebra(f'A{n}')
            assert val > prev, f'A{n}: alpha_g={val} not > {prev}'
            prev = val

    def test_monotone_in_rank_within_b(self):
        """Within B-series, alpha_g is strictly increasing in rank."""
        prev = 0
        for n in range(2, 9):
            val = alpha_g_for_algebra(f'B{n}')
            assert val > prev, f'B{n}: alpha_g={val} not > {prev}'
            prev = val

    def test_monotone_in_rank_within_d(self):
        """Within D-series, alpha_g is strictly increasing in rank."""
        prev = 0
        for n in range(4, 9):
            val = alpha_g_for_algebra(f'D{n}')
            assert val > prev, f'D{n}: alpha_g={val} not > {prev}'
            prev = val


# ============================================================
# 10. Cross-family comparisons
# ============================================================

class TestCrossFamilyComparisons:
    """Cross-family consistency checks."""

    def test_bc_same_dim_different_alpha(self):
        """B_n and C_n share dim = n(2n+1) but have different h^v, hence different alpha_g.

        For n=3: B3 has h^v=5, C3 has h^v=4. Same dim=21.
        alpha(B3) = 6 + 4*21*5 = 426
        alpha(C3) = 6 + 4*21*4 = 342
        """
        # VERIFIED [CF] B_n/C_n dim identity + [DC] direct comparison
        for n in range(3, 9):
            b_data = LIE_ALGEBRA_TABLE[f'B{n}']
            c_data = LIE_ALGEBRA_TABLE[f'C{n}']
            assert b_data.dim == c_data.dim, f'n={n}: dims should match'
            alpha_b = alpha_g_for_algebra(f'B{n}')
            alpha_c = alpha_g_for_algebra(f'C{n}')
            assert alpha_b > alpha_c, (
                f'n={n}: alpha(B{n})={alpha_b} should exceed alpha(C{n})={alpha_c} '
                f'since h^v(B{n})=2n-1={2*n-1} > h^v(C{n})=n+1={n+1}')

    def test_a1_is_smallest(self):
        """A_1 = sl_2 has the smallest alpha_g among all simple Lie algebras."""
        # VERIFIED [DC] alpha(A1)=26 + [LC] rank=1, dim=3 are minimal
        results = compute_all_alpha_g()
        a1_val = results['A1'].alpha_g
        for name, r in results.items():
            assert r.alpha_g >= a1_val, f'{name}: alpha_g={r.alpha_g} < A1={a1_val}'

    def test_e8_is_largest(self):
        """E_8 has the largest alpha_g among the 31 algebras in our table."""
        # VERIFIED [DC] alpha(E8)=29776 + [CF] dim*h^v = 248*30 = 7440 dominates
        results = compute_all_alpha_g()
        e8_val = results['E8'].alpha_g
        for name, r in results.items():
            assert r.alpha_g <= e8_val, f'{name}: alpha_g={r.alpha_g} > E8={e8_val}'


# ============================================================
# 11. Isomorphism checks
# ============================================================

class TestIsomorphisms:
    """Verify alpha_g is consistent across Lie algebra isomorphisms."""

    def test_b2_c2_isomorphism(self):
        """B_2 = C_2 (so_5 = sp_4): same rank, dim, h^v, hence same alpha_g."""
        # VERIFIED [DC] B2 data + [SY] isomorphism so(5)=sp(4)
        ok, msg = check_b2_c2_isomorphism()
        assert ok, f'B2/C2 isomorphism check failed: {msg}'

    def test_d3_a3_isomorphism(self):
        """D_3 = A_3 (so_6 = sl_4): same rank, dim, h^v, hence same alpha_g."""
        # VERIFIED [DC] A3 data + [SY] isomorphism so(6)=sl(4)
        ok, msg = check_d3_a3_isomorphism()
        assert ok, f'D3/A3 isomorphism check failed: {msg}'

    def test_d4_triality(self):
        """D_4 = so_8 has S_3 triality symmetry; alpha_g is a single number."""
        # VERIFIED [DC] alpha(D4)=680 + [SY] S3 triality preserves dim and h^v
        d4 = LIE_ALGEBRA_TABLE['D4']
        assert d4.rank == 4
        assert d4.dim == 28
        assert d4.dual_coxeter == 6
        assert alpha_g_for_algebra('D4') == 680


# ============================================================
# 12. Formula unit tests
# ============================================================

class TestFormulaUnit:
    """Direct unit tests of the alpha_g function."""

    def test_alpha_g_direct(self):
        assert alpha_g(1, 3, 2) == 26   # sl_2
        assert alpha_g(2, 8, 3) == 100  # sl_3 -- wait, A2 has rank 2 not dim 8
        # Actually: A2: rank=2, dim=2*(2+2)=8, h^v=3. alpha = 4+96 = 100

    def test_alpha_g_zero_inputs(self):
        """alpha_g with rank=0 and/or h^v=0 (degenerate, not physical)."""
        assert alpha_g(0, 10, 5) == 200  # pure curvature
        assert alpha_g(5, 10, 0) == 10   # pure rank
        assert alpha_g(0, 0, 0) == 0     # trivial

    def test_alpha_g_additivity_in_rank(self):
        """2*rank term is linear in rank."""
        for r in range(1, 10):
            assert alpha_g(r, 0, 0) == 2 * r

    def test_alpha_g_multiplicativity_in_dim_hv(self):
        """4*dim*h^v term is bilinear."""
        for d in [3, 10, 78, 248]:
            for hv in [2, 4, 12, 30]:
                assert alpha_g(0, d, hv) == 4 * d * hv


# ============================================================
# 13. Parametric verification (closed-form for classical types)
# ============================================================

class TestParametricFormulas:
    """Verify alpha_g against closed-form expressions for each classical series."""

    @pytest.mark.parametrize('n', range(1, 9))
    def test_a_series_closed_form(self, n):
        """A_n: alpha = 2n + 4*n(n+2)*(n+1) = 2n + 4n(n+1)(n+2)."""
        # VERIFIED [DC] formula expansion + [CF] matches individual tests
        expected = 2 * n + 4 * n * (n + 2) * (n + 1)
        assert alpha_g_for_algebra(f'A{n}') == expected

    @pytest.mark.parametrize('n', range(2, 9))
    def test_b_series_closed_form(self, n):
        """B_n: alpha = 2n + 4*n(2n+1)*(2n-1) = 2n + 4n(2n+1)(2n-1)."""
        # VERIFIED [DC] formula expansion + [CF] dim*h^v = n(2n+1)(2n-1)
        expected = 2 * n + 4 * n * (2 * n + 1) * (2 * n - 1)
        assert alpha_g_for_algebra(f'B{n}') == expected

    @pytest.mark.parametrize('n', range(3, 9))
    def test_c_series_closed_form(self, n):
        """C_n: alpha = 2n + 4*n(2n+1)*(n+1)."""
        # VERIFIED [DC] formula expansion + [CF] dim*h^v = n(2n+1)(n+1)
        expected = 2 * n + 4 * n * (2 * n + 1) * (n + 1)
        assert alpha_g_for_algebra(f'C{n}') == expected

    @pytest.mark.parametrize('n', range(4, 9))
    def test_d_series_closed_form(self, n):
        """D_n: alpha = 2n + 4*n(2n-1)*(2n-2) = 2n + 8n(2n-1)(n-1)."""
        # VERIFIED [DC] formula expansion + [CF] h^v=2(n-1)
        expected = 2 * n + 4 * n * (2 * n - 1) * (2 * n - 2)
        assert alpha_g_for_algebra(f'D{n}') == expected
