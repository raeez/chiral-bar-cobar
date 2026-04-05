r"""Tests for arithmetic depth d_arith across the complete standard landscape.

Tests verify:
  1. Cusp form dimension formula for SL(2,Z)
  2. Lattice VOA d_arith = 2 + dim S_{r/2}
  3. Niemeier lattices: d_arith = 3 universally
  4. Affine KM: d_arith values
  5. Virasoro minimal models: multiplicative independence
  6. Ising d_arith = 0 (prop:ising-d-arith)
  7. Betagamma d_arith = 1
  8. First d_arith > 3: rank 48
  9. Monotonicity of d_arith for lattice VOAs
 10. Depth decomposition consistency d = 1 + d_arith + d_alg
 11. Cross-family assertions

Manuscript references:
    thm:depth-decomposition (arithmetic_shadows.tex)
    prop:ising-d-arith (arithmetic_shadows.tex)
    thm:refined-shadow-spectral (arithmetic_shadows.tex)
"""

import sys
sys.path.insert(0, 'compute/lib')

import pytest
from fractions import Fraction
from sympy import Rational

from darith_complete_landscape import (
    cusp_form_dim_sl2z,
    darith_lattice_unimodular,
    darith_all_niemeier,
    darith_heisenberg,
    darith_affine_km,
    darith_virasoro_minimal,
    darith_virasoro_generic,
    darith_w_algebra,
    darith_betagamma,
    complete_landscape_table,
    first_darith_exceeding,
    darith_monotonicity_lattice,
    landscape_summary,
    cusp_form_dim_table,
    darith_vs_rank_table,
    DArithResult,
    _minimal_model_primaries,
    _minimal_model_c,
    _count_critical_lines_minimal,
    _factorize,
    _matrix_rank_Q,
)


# ========================================================================
# 1. Cusp form dimension for SL(2,Z)
# ========================================================================

class TestCuspFormDim:
    """Verify dim S_k(SL(2,Z)) against known values."""

    def test_small_weights_zero(self):
        """dim S_k = 0 for k < 12 even."""
        for k in [2, 4, 6, 8, 10]:
            assert cusp_form_dim_sl2z(k) == 0, f"S_{k} should be 0"

    def test_ramanujan_delta(self):
        """dim S_12 = 1 (the Ramanujan Delta function)."""
        assert cusp_form_dim_sl2z(12) == 1

    def test_dim_S14_to_S22(self):
        """Known values from Diamond-Shurman."""
        assert cusp_form_dim_sl2z(14) == 0
        assert cusp_form_dim_sl2z(16) == 1
        assert cusp_form_dim_sl2z(18) == 1
        assert cusp_form_dim_sl2z(20) == 1
        assert cusp_form_dim_sl2z(22) == 1

    def test_dim_S24(self):
        """dim S_24 = 2 (two independent cusp forms)."""
        assert cusp_form_dim_sl2z(24) == 2

    def test_dim_S26_S28(self):
        """dim S_26 = 1, dim S_28 = 2.

        k=26: 26 mod 12 = 2, dim M_26 = floor(26/12) = 2, dim S_26 = 1.
        k=28: 28 mod 12 = 4, dim M_28 = floor(28/12)+1 = 3, dim S_28 = 2.
        """
        assert cusp_form_dim_sl2z(26) == 1
        assert cusp_form_dim_sl2z(28) == 2

    def test_dim_S36(self):
        """dim S_36 = 3."""
        assert cusp_form_dim_sl2z(36) == 3

    def test_dim_S48(self):
        """dim S_48 = 4."""
        assert cusp_form_dim_sl2z(48) == 4

    def test_odd_weight_zero(self):
        """Odd weight: dim S_k = 0 for SL(2,Z)."""
        for k in [1, 3, 5, 7, 11, 13]:
            assert cusp_form_dim_sl2z(k) == 0

    def test_nondecreasing_at_lattice_weights(self):
        """dim S_k(SL(2,Z)) is non-decreasing at lattice-relevant weights.

        For even unimodular lattices (rank = 8m), the theta weight
        is k = 4m. Since 4m mod 12 is in {0, 4, 8} (never 2), the
        dim S_k formula gives a non-decreasing sequence at these
        weights. The full dim S_k sequence is NOT monotone: it drops
        at k = 2 mod 12 (k = 14, 26, 38, ...).
        """
        prev = 0
        for m in range(1, 25):
            k = 4 * m  # lattice-relevant weight
            d = cusp_form_dim_sl2z(k)
            assert d >= prev, f"dim S_{k} = {d} < dim S_{k-4} = {prev}"
            prev = d

    def test_table_nonempty(self):
        """Cusp form dimension table is well-formed."""
        table = cusp_form_dim_table(60)
        assert len(table) == 30  # weights 2, 4, ..., 60
        for k, d in table:
            assert d >= 0


# ========================================================================
# 2. Lattice VOA d_arith
# ========================================================================

class TestLatticeDArith:
    """Verify d_arith for even unimodular lattice VOAs."""

    def test_E8_rank8(self):
        """E_8 lattice (rank 8): d_arith = 2, dim S_4 = 0."""
        r = darith_lattice_unimodular(8)
        assert r.d_arith == 2
        assert r.d_alg == 0
        assert r.d_total == 3
        assert r.shadow_class == 'G'

    def test_rank16(self):
        """Rank-16 lattice: d_arith = 2 (dim S_8 = 0)."""
        r = darith_lattice_unimodular(16)
        assert r.d_arith == 2

    def test_Niemeier_rank24(self):
        """Rank-24 (Niemeier): d_arith = 3 (dim S_12 = 1)."""
        r = darith_lattice_unimodular(24)
        assert r.d_arith == 3
        assert r.d_total == 4

    def test_rank32(self):
        """Rank-32: d_arith = 3 (dim S_16 = 1)."""
        r = darith_lattice_unimodular(32)
        assert r.d_arith == 3

    def test_rank48(self):
        """Rank-48: d_arith = 4 (dim S_24 = 2). FIRST d_arith > 3."""
        r = darith_lattice_unimodular(48)
        assert r.d_arith == 4

    def test_rank72(self):
        """Rank-72: d_arith = 5 (dim S_36 = 3)."""
        r = darith_lattice_unimodular(72)
        assert r.d_arith == 5

    def test_rank96(self):
        """Rank-96: d_arith = 6 (dim S_48 = 4)."""
        r = darith_lattice_unimodular(96)
        assert r.d_arith == 6

    def test_depth_decomposition_consistency(self):
        """d_total = 1 + d_arith + d_alg for all lattice VOAs."""
        for rank in [8, 16, 24, 32, 48, 72, 96]:
            r = darith_lattice_unimodular(rank)
            assert r.d_total == 1 + r.d_arith + r.d_alg

    def test_monotonicity(self):
        """d_arith is non-decreasing with rank."""
        data = darith_monotonicity_lattice(200)
        prev_da = 0
        for rank, weight, da in data:
            assert da >= prev_da, f"d_arith decreased at rank {rank}"
            prev_da = da


# ========================================================================
# 3. Niemeier lattices (all 24)
# ========================================================================

class TestNiemeier:
    """Verify d_arith = 3 for all 24 Niemeier lattices."""

    def test_all_niemeier_d_arith_3(self):
        """ALL Niemeier lattices have d_arith = 3."""
        results = darith_all_niemeier()
        assert len(results) >= 24, f"Expected 24 Niemeier, got {len(results)}"
        for name, r in results.items():
            assert r.d_arith == 3, f"{name}: d_arith = {r.d_arith}, expected 3"

    def test_leech_lattice(self):
        """Leech lattice (rank 24, no roots): d_arith = 3."""
        results = darith_all_niemeier()
        assert 'Leech' in results
        assert results['Leech'].d_arith == 3

    def test_e8_cubed(self):
        """E_8^3 (rank 24): d_arith = 3."""
        results = darith_all_niemeier()
        assert 'E8_3' in results
        assert results['E8_3'].d_arith == 3

    def test_niemeier_universality(self):
        """d_arith is INDEPENDENT of the root system for rank 24.

        This is because d_arith = 2 + dim S_12 = 3, and dim S_12
        depends only on the WEIGHT (=12 for all rank-24 lattices),
        not on the specific theta function.
        """
        results = darith_all_niemeier()
        d_arith_values = set(r.d_arith for r in results.values())
        assert d_arith_values == {3}, f"Expected all 3, got {d_arith_values}"


# ========================================================================
# 4. Heisenberg
# ========================================================================

class TestHeisenberg:
    """Verify d_arith for Heisenberg algebra."""

    def test_level_1(self):
        """H_1: d_arith = 1."""
        r = darith_heisenberg(1)
        assert r.d_arith == 1
        assert r.d_alg == 0
        assert r.d_total == 2

    def test_class_G(self):
        """Heisenberg is class G."""
        r = darith_heisenberg(1)
        assert r.shadow_class == 'G'


# ========================================================================
# 5. Affine Kac-Moody
# ========================================================================

class TestAffineKM:
    """Verify d_arith for affine Kac-Moody algebras."""

    def test_E8_level1_lattice_type(self):
        """V_1(E_8) ~ V_{E_8}: d_arith = 2 (lattice-type)."""
        r = darith_affine_km('E8', 1)
        assert r.d_arith == 2
        assert r.shadow_class == 'L'

    def test_sl2_level1(self):
        """V_1(sl_2): d_arith = 1."""
        r = darith_affine_km('sl2', 1)
        assert r.d_arith == 1

    def test_sl3_level1(self):
        """V_1(sl_3): d_arith = 1."""
        r = darith_affine_km('sl3', 1)
        assert r.d_arith == 1

    def test_E7_level1(self):
        """V_1(E_7): d_arith = 1."""
        r = darith_affine_km('E7', 1)
        assert r.d_arith == 1

    def test_G2_level1(self):
        """V_1(G_2): d_arith = 1."""
        r = darith_affine_km('G2', 1)
        assert r.d_arith == 1

    def test_sl2_higher_levels(self):
        """V_k(sl_2) at k=2..10: d_arith = 1 (VVMF suppression)."""
        for k in range(2, 11):
            r = darith_affine_km('sl2', k)
            assert r.d_arith == 1, f"sl_2 level {k}: d_arith = {r.d_arith}"

    def test_all_class_L(self):
        """All affine KM are class L."""
        for t in ['sl2', 'sl3', 'E8', 'G2']:
            r = darith_affine_km(t, 1)
            assert r.shadow_class == 'L'

    def test_E8_exceptional(self):
        """E_8 at level 1 is the ONLY affine KM with d_arith = 2."""
        exceptional = []
        for t in _test_types():
            r = darith_affine_km(t, 1)
            if r.d_arith > 1:
                exceptional.append(t)
        assert exceptional == ['E8'], f"Expected only E_8, got {exceptional}"

    def test_depth_decomposition(self):
        """d_total = 1 + d_arith + d_alg for all affine KM."""
        for t in _test_types():
            r = darith_affine_km(t, 1)
            assert r.d_total == 1 + r.d_arith + r.d_alg


def _test_types():
    return ['sl2', 'sl3', 'sl4', 'E6', 'E7', 'E8', 'D4', 'G2', 'F4', 'so5']


# ========================================================================
# 6. Virasoro minimal models
# ========================================================================

class TestVirasoroMinimal:
    """Verify d_arith for Virasoro minimal models."""

    def test_ising_d_arith_zero(self):
        """M(3,4) [Ising, c=1/2]: d_arith = 0 (prop:ising-d-arith).

        This is the manuscript's proved result. The primaries are
        h = 1/16, 1/2, giving lambda = 1/8, 1. These are
        multiplicatively dependent (both powers of 2): 1 = 2^0,
        1/8 = 2^{-3}. So rank = 1, d_arith = 0.
        """
        r = darith_virasoro_minimal(3, 4)
        assert r.d_arith == 0
        assert r.shadow_class == 'M'

    def test_ising_central_charge(self):
        """Ising has c = 1/2."""
        assert _minimal_model_c(3, 4) == Rational(1, 2)

    def test_tricritical_ising(self):
        """M(4,5) [tri-critical Ising, c=7/10]: d_arith = 3.

        Primaries: h = 3/80, 1/10, 7/16, 3/5, 3/2
        Lambda: 3/40, 1/5, 7/8, 6/5, 3
        Prime factors: {2, 3, 5, 7}
        Multiplicative rank: 4
        d_arith = 3.
        """
        r = darith_virasoro_minimal(4, 5)
        assert r.d_arith == 3
        assert _minimal_model_c(4, 5) == Rational(7, 10)

    def test_three_state_potts(self):
        """M(5,6) [3-state Potts, c=4/5]: d_arith > 0.

        More primaries => more multiplicatively independent lambdas.
        """
        r = darith_virasoro_minimal(5, 6)
        assert r.d_arith >= 1
        assert _minimal_model_c(5, 6) == Rational(4, 5)

    def test_d_arith_nondecreasing_with_complexity(self):
        """d_arith grows with unitary minimal model complexity.

        For unitary M(m, m+1), the number of primaries grows as
        m(m-1)/2 - 1, and the number of distinct primes dividing
        their denominators grows, so d_arith is non-decreasing.
        """
        prev_da = 0
        for m in range(3, 8):
            r = darith_virasoro_minimal(m, m + 1)
            assert r.d_arith >= prev_da, (
                f"M({m},{m+1}): d_arith = {r.d_arith} < {prev_da}")
            prev_da = r.d_arith

    def test_non_unitary_M35(self):
        """M(3,5) is NON-UNITARY (c = -3/5). d_arith still computable."""
        r = darith_virasoro_minimal(3, 5)
        assert isinstance(r.d_arith, int)
        assert _minimal_model_c(3, 5) == Rational(-3, 5)

    def test_M43_equals_M34(self):
        """M(4,3) should give same c and d_arith as M(3,4) (Ising).

        Convention: we require p > q, but M(4,3) with c = 1/2 should work.
        """
        # c(4,3) = 1 - 6*(1)^2/(12) = 1 - 1/2 = 1/2
        assert _minimal_model_c(4, 3) == Rational(1, 2)
        r = darith_virasoro_minimal(4, 3)
        assert r.d_arith == 0  # same as Ising


# ========================================================================
# 7. Virasoro generic
# ========================================================================

class TestVirasoroGeneric:
    """Verify d_arith for Virasoro at generic central charge."""

    def test_c1_free_boson(self):
        """Virasoro c = 1: d_arith = 1."""
        r = darith_virasoro_generic(1)
        assert r.d_arith == 1

    def test_c25_koszul_dual(self):
        """Virasoro c = 25: d_arith = 1 (Koszul dual of c=1)."""
        r = darith_virasoro_generic(25)
        assert r.d_arith == 1

    def test_c26_critical_string(self):
        """Virasoro c = 26: d_arith = 1."""
        r = darith_virasoro_generic(26)
        assert r.d_arith == 1

    def test_c13_self_dual(self):
        """Virasoro c = 13 (self-dual): d_arith = 0 (generic)."""
        r = darith_virasoro_generic(13)
        assert r.d_arith == 0

    def test_c_half_is_ising(self):
        """c = 1/2 dispatches to Ising minimal model."""
        r = darith_virasoro_generic(Rational(1, 2))
        assert r.d_arith == 0

    def test_c_7_10_is_tricritical(self):
        """c = 7/10 dispatches to tri-critical Ising."""
        r = darith_virasoro_generic(Rational(7, 10))
        assert r.d_arith == 3


# ========================================================================
# 8. Betagamma
# ========================================================================

class TestBetagamma:
    """Verify d_arith for betagamma system."""

    def test_standard_betagamma(self):
        """betagamma (lambda=1): d_arith = 1, d_alg = 2, d_total = 4."""
        r = darith_betagamma(1)
        assert r.d_arith == 1
        assert r.d_alg == 2
        assert r.d_total == 4
        assert r.shadow_class == 'C'

    def test_symplectic_betagamma(self):
        """betagamma (lambda=1/2): d_arith = 1."""
        r = darith_betagamma(Rational(1, 2))
        assert r.d_arith == 1

    def test_depth_decomposition(self):
        """d_total = 1 + 1 + 2 = 4 for all betagamma."""
        for w in [1, Rational(1, 2), Rational(1, 3)]:
            r = darith_betagamma(w)
            assert r.d_total == 1 + r.d_arith + r.d_alg


# ========================================================================
# 9. W-algebras
# ========================================================================

class TestWAlgebra:
    """Verify d_arith for W-algebras."""

    def test_W3_free_field(self):
        """W_3 at c = 2 (free field): d_arith = 1."""
        r = darith_w_algebra(3, c_val=2)
        assert r.d_arith == 1

    def test_W3_generic(self):
        """W_3 at generic c: d_arith = 0."""
        r = darith_w_algebra(3)
        assert r.d_arith == 0

    def test_W4_free_field(self):
        """W_4 at c = 3 (free field): d_arith = 1."""
        r = darith_w_algebra(4, c_val=3)
        assert r.d_arith == 1

    def test_W4_generic(self):
        """W_4 at generic c: d_arith = 0."""
        r = darith_w_algebra(4)
        assert r.d_arith == 0

    def test_class_M(self):
        """All W-algebras are class M."""
        for N in [3, 4, 5]:
            r = darith_w_algebra(N)
            assert r.shadow_class == 'M'


# ========================================================================
# 10. First family with d_arith > threshold
# ========================================================================

class TestFirstDArith:
    """Verify the first families where d_arith exceeds given thresholds."""

    def test_first_gt_2(self):
        """First d_arith > 2: rank-24 lattice (Niemeier/Leech)."""
        r = first_darith_exceeding(2)
        assert r['rank'] == 24
        assert r['dim_cusp'] == 1  # dim S_12 = 1

    def test_first_gt_3(self):
        """First d_arith > 3: rank-48 lattice."""
        r = first_darith_exceeding(3)
        assert r['rank'] == 48
        assert r['dim_cusp'] == 2  # dim S_24 = 2

    def test_first_gt_4(self):
        """First d_arith > 4: rank-72 lattice."""
        r = first_darith_exceeding(4)
        assert r['rank'] == 72
        assert r['dim_cusp'] == 3  # dim S_36 = 3

    def test_first_gt_5(self):
        """First d_arith > 5: rank-96 lattice."""
        r = first_darith_exceeding(5)
        assert r['rank'] == 96
        assert r['dim_cusp'] == 4  # dim S_48 = 4


# ========================================================================
# 11. Cross-family consistency
# ========================================================================

class TestCrossFamilyConsistency:
    """Cross-family assertions from the depth decomposition theorem."""

    def test_d_arith_bounded_by_class(self):
        """d_arith + d_alg + 1 = d_total is consistent.

        For class G: d_alg = 0
        For class L: d_alg = 1
        For class C: d_alg = 2
        For class M: d_alg = infinity
        """
        table = complete_landscape_table()
        for r in table:
            if r.shadow_class == 'G':
                assert r.d_alg == 0
            elif r.shadow_class == 'L':
                assert r.d_alg == 1
            elif r.shadow_class == 'C':
                assert r.d_alg == 2
            elif r.shadow_class == 'M':
                assert r.d_alg is None  # infinity

    def test_finite_d_arith_for_lattice(self):
        """Lattice VOAs always have finite d_arith."""
        for rank in [8, 16, 24, 32, 48]:
            r = darith_lattice_unimodular(rank)
            assert isinstance(r.d_arith, int)
            assert r.d_arith >= 2

    def test_lattice_d_arith_at_least_2(self):
        """Even unimodular lattice: d_arith >= 2 (Eisenstein contribution)."""
        for rank in [8, 16, 24, 32, 48, 72, 96]:
            r = darith_lattice_unimodular(rank)
            assert r.d_arith >= 2

    def test_E8_level1_vs_E8_lattice(self):
        """V_1(E_8) and V_{E_8} should have same d_arith = 2.

        V_1(E_8) ~ V_{E_8} (the lattice VOA for the E_8 root lattice).
        """
        r_km = darith_affine_km('E8', 1)
        r_lat = darith_lattice_unimodular(8)
        assert r_km.d_arith == r_lat.d_arith == 2

    def test_complete_table_has_all_classes(self):
        """The complete table covers all four shadow classes."""
        table = complete_landscape_table()
        classes = set(r.shadow_class for r in table)
        assert classes == {'G', 'L', 'C', 'M'}

    def test_class_M_all_infinite_d_total(self):
        """Class M algebras have infinite d_total (from d_alg = infinity)."""
        table = complete_landscape_table()
        for r in table:
            if r.shadow_class == 'M':
                assert r.d_total is None  # infinity

    def test_heisenberg_less_than_lattice(self):
        """Heisenberg (rank 1) has d_arith < lattice (rank 8)."""
        r_h = darith_heisenberg(1)
        r_l = darith_lattice_unimodular(8)
        assert r_h.d_arith < r_l.d_arith


# ========================================================================
# 12. Multiplicative independence (internal helper tests)
# ========================================================================

class TestMultiplicativeIndependence:
    """Test the prime factorization and matrix rank computation."""

    def test_factorize_small(self):
        """Factorize small integers."""
        assert _factorize(1) == {}
        assert _factorize(2) == {2: 1}
        assert _factorize(12) == {2: 2, 3: 1}
        assert _factorize(360) == {2: 3, 3: 2, 5: 1}

    def test_matrix_rank_identity(self):
        """Rank of identity matrix."""
        assert _matrix_rank_Q([[1, 0], [0, 1]]) == 2

    def test_matrix_rank_dependent(self):
        """Rank of matrix with dependent rows."""
        assert _matrix_rank_Q([[1, 2], [2, 4]]) == 1

    def test_matrix_rank_empty(self):
        """Rank of empty/zero matrix."""
        assert _matrix_rank_Q([]) == 0
        assert _matrix_rank_Q([[0]]) == 0

    def test_ising_multiplicative_dependence(self):
        """Ising: lambda = {1/8, 1}. Both powers of 2. Rank 1."""
        # 1/8 = 2^{-3}, 1 = 2^0
        # Over prime {2}: vectors [-3] and [0]
        rank = _matrix_rank_Q([[-3], [0]])
        assert rank == 1  # => d_arith = 0

    def test_tricritical_four_primes(self):
        """Tri-critical Ising: 4 primes {2,3,5,7}. Rank 4."""
        # Lambdas: 3/40, 1/5, 7/8, 6/5, 3
        # Factorizations over {2,3,5,7}:
        matrix = [
            [-3, 1, -1, 0],   # 3/40 = 2^{-3} 3^1 5^{-1}
            [0, 0, -1, 0],    # 1/5 = 5^{-1}
            [-3, 0, 0, 1],    # 7/8 = 2^{-3} 7^1
            [1, 1, -1, 0],    # 6/5 = 2^1 3^1 5^{-1}
            [0, 1, 0, 0],     # 3 = 3^1
        ]
        assert _matrix_rank_Q(matrix) == 4


# ========================================================================
# 13. Minimal model primaries
# ========================================================================

class TestMinimalModelPrimaries:
    """Test minimal model primary field computation."""

    def test_ising_primaries(self):
        """M(3,4): h = {0, 1/16, 1/2}."""
        primaries = _minimal_model_primaries(3, 4)
        assert Rational(0) in primaries
        assert Rational(1, 16) in primaries
        assert Rational(1, 2) in primaries
        assert len(primaries) == 3

    def test_tricritical_ising_primaries(self):
        """M(4,5): 6 primary fields."""
        primaries = _minimal_model_primaries(4, 5)
        assert Rational(0) in primaries
        assert len(primaries) == 6

    def test_ising_central_charge(self):
        """c(3,4) = 1/2."""
        assert _minimal_model_c(3, 4) == Rational(1, 2)

    def test_tricritical_central_charge(self):
        """c(4,5) = 7/10."""
        assert _minimal_model_c(4, 5) == Rational(7, 10)

    def test_three_state_potts_central_charge(self):
        """c(5,6) = 4/5."""
        assert _minimal_model_c(5, 6) == Rational(4, 5)


# ========================================================================
# 14. darith_vs_rank_table
# ========================================================================

class TestDArithVsRank:
    """Test the d_arith vs rank table."""

    def test_table_nonempty(self):
        """Table has entries."""
        table = darith_vs_rank_table()
        assert len(table) >= 10

    def test_table_monotone(self):
        """d_arith is non-decreasing with rank."""
        table = darith_vs_rank_table()
        prev = 0
        for row in table:
            assert row['d_arith'] >= prev
            prev = row['d_arith']

    def test_table_consistency(self):
        """d_total = 1 + d_arith for class G."""
        for row in darith_vs_rank_table():
            assert row['d_total'] == 1 + row['d_arith']


# ========================================================================
# 15. Landscape summary
# ========================================================================

class TestLandscapeSummary:
    """Test landscape summary statistics."""

    def test_summary_format(self):
        """Summary has expected keys."""
        s = landscape_summary()
        assert 'total' in s
        assert 'by_class' in s
        assert 'max_darith' in s

    def test_summary_total(self):
        """Total families matches table length."""
        s = landscape_summary()
        table = complete_landscape_table()
        assert s['total'] == len(table)

    def test_max_darith_among_lattices(self):
        """Among lattice VOAs (class G), max d_arith = rank 96 with d_arith = 6.

        The overall max finite d_arith can come from minimal models
        (class M) which have many multiplicatively independent primaries.
        E.g. M(7,8) has d_arith = 7, exceeding rank-96 lattice's d_arith = 6.
        """
        table = complete_landscape_table()
        lattice = [r for r in table if r.shadow_class == 'G' and isinstance(r.d_arith, int)]
        max_lat = max(lattice, key=lambda r: r.d_arith)
        assert max_lat.d_arith == 6  # rank-96
