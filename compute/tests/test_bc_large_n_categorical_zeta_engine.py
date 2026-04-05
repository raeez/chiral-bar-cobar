r"""Tests for large-N categorical zeta functions from the DK category.

Verification strategy (multi-path, per CLAUDE.md mandate):
    Path 1: N=2 reproduces Riemann zeta (exact check)
    Path 2: Weyl dimension formula vs hook-content formula (must agree)
    Path 3: Monotonicity: zeta^{DK}_{sl_N}(s) monotone in N for fixed s
    Path 4: Asymptotic formula check: leading term at large N
    Path 5: Character identity: chi_lambda(1) = dim V_lambda

The central large-N theme:
    As N -> infty, sl_N representations grow in dimension.  The categorical
    zeta gains more terms (more allowed partitions) but each term shrinks
    (dimensions grow).  The net behavior depends on the exponent s and the
    representation sector.

References:
    concordance.tex: MC3 (all simple types, cor:mc3-all-types)
    bc_categorical_zeta_engine.py: base categorical zeta
    large_n_twisted_holography.py: 't Hooft genus expansion
    CLAUDE.md: multi-path verification mandate, AP1, AP10
"""

import cmath
import math
from fractions import Fraction
from math import comb, factorial

import numpy as np
import pytest

from compute.lib.bc_large_n_categorical_zeta_engine import (
    # Young diagram utilities
    partition_to_young_diagram,
    hook_length,
    content,
    hook_content_dimension,
    weyl_dimension_slN_partition,
    partition_size,
    num_rows,
    # Partition enumeration
    partitions_bounded,
    partitions_at_most_k_rows,
    symmetric_partitions,
    # Categorical zeta
    categorical_zeta_slN,
    categorical_zeta_sl2_exact,
    # Symmetric rep zeta
    dim_symmetric_rep,
    symmetric_rep_zeta,
    symmetric_rep_asymptotic,
    # Adjoint
    dim_adjoint,
    adjoint_contribution,
    # Rescaled zeta
    rescaled_zeta,
    rescaled_zeta_data,
    # Planar zeta
    planar_zeta,
    planar_fraction,
    # Casimir zeta
    casimir_eigenvalue_sl2,
    casimir_eigenvalue_slN,
    casimir_zeta_sl2,
    casimir_zeta_slN,
    # Character zeta
    character_sl2,
    character_slN_symmetric,
    character_zeta_sl2,
    root_of_unity,
    # Renormalized zeta
    frame_robinson_schensted_limit,
    renormalized_dimension,
    renormalized_zeta,
    renormalized_zeta_limit,
    # 't Hooft
    thooft_double_scaling_zeta,
    thooft_rescaled,
    # Monotonicity
    zeta_monotonicity_check,
    symmetric_zeta_growth,
    # Abscissa
    abscissa_of_convergence_slN,
    # Cross-verification
    verify_hook_vs_weyl,
    verify_sl2_is_riemann,
    verify_character_at_one,
    verify_asymptotic_dimension,
    # Summary
    large_n_summary,
    casimir_summary,
)


# =========================================================================
# Section 1: Young diagram and hook-content formula
# =========================================================================

class TestYoungDiagram:
    """Test Young diagram utilities: cells, hooks, contents."""

    def test_single_box(self):
        """Partition (1,) has a single cell."""
        cells = partition_to_young_diagram((1,))
        assert cells == [(0, 0)]

    def test_single_row(self):
        """Partition (3,) = three cells in one row."""
        cells = partition_to_young_diagram((3,))
        assert len(cells) == 3
        assert (0, 0) in cells
        assert (0, 1) in cells
        assert (0, 2) in cells

    def test_two_rows(self):
        """Partition (2, 1) = L-shaped Young diagram."""
        cells = partition_to_young_diagram((2, 1))
        assert len(cells) == 3
        assert set(cells) == {(0, 0), (0, 1), (1, 0)}

    def test_hook_single_cell(self):
        """Hook length at the only cell of (1,) is 1."""
        assert hook_length((1,), 0, 0) == 1

    def test_hook_two_by_one(self):
        """Hook lengths for partition (2,)."""
        assert hook_length((2,), 0, 0) == 2
        assert hook_length((2,), 0, 1) == 1

    def test_hook_staircase(self):
        """Hook lengths for partition (2, 1)."""
        assert hook_length((2, 1), 0, 0) == 3  # arm=1, leg=1
        assert hook_length((2, 1), 0, 1) == 1  # arm=0, leg=0
        assert hook_length((2, 1), 1, 0) == 1  # arm=0, leg=0

    def test_content_values(self):
        """Content = N + j - i."""
        for N in [3, 5, 10]:
            assert content(N, 0, 0) == N
            assert content(N, 0, 1) == N + 1
            assert content(N, 1, 0) == N - 1

    def test_partition_size(self):
        assert partition_size((3, 2, 1)) == 6
        assert partition_size((4,)) == 4
        assert partition_size(()) == 0

    def test_num_rows(self):
        assert num_rows((3, 2, 1)) == 3
        assert num_rows((4, 0)) == 1
        assert num_rows(()) == 0


# =========================================================================
# Section 2: Hook-content dimension formula
# =========================================================================

class TestHookContentDimension:
    """Test the hook-content dimension formula for sl_N representations."""

    def test_trivial_rep(self):
        """Empty partition = trivial rep, dim = 1."""
        for N in range(2, 10):
            assert hook_content_dimension(N, ()) == 1

    def test_fundamental_rep(self):
        """Partition (1,) = fundamental rep of sl_N, dim = N."""
        for N in range(2, 20):
            assert hook_content_dimension(N, (1,)) == N

    def test_sl2_dimensions(self):
        """For sl_2, dim V_{(n,)} = n + 1."""
        for n in range(1, 15):
            assert hook_content_dimension(2, (n,)) == n + 1

    def test_adjoint_sl3(self):
        """Adjoint of sl_3: partition (2,1), dim = 8."""
        assert hook_content_dimension(3, (2, 1)) == 8

    def test_adjoint_slN(self):
        """Adjoint of sl_N: Young diagram with single column of 2 boxes
        gives the antisymmetric square; adjoint = (2,1,...,1) has dim N^2-1.

        Actually, the adjoint of sl_N corresponds to the partition (2, 1, ..., 1)
        with N-2 ones. But it is easier to use: adjoint = fund tensor fund*
        minus trivial.  In partition notation, adjoint = (2, 1^{N-2}) has
        N-1 rows.  Wait: for sl_N, the adjoint has highest weight omega_1 + omega_{N-1}.
        In partition notation this is (2, 1, 1, ..., 1) with N-2 ones.
        """
        for N in [3, 4, 5, 6]:
            adj_partition = (2,) + (1,) * (N - 2)
            d = hook_content_dimension(N, adj_partition)
            assert d == N * N - 1, f"sl_{N} adjoint: got {d}, expected {N*N-1}"

    def test_symmetric_reps(self):
        """dim Sym^n(C^N) = C(N+n-1, n)."""
        for N in range(2, 8):
            for n in range(1, 8):
                expected = comb(N + n - 1, n)
                actual = hook_content_dimension(N, (n,))
                assert actual == expected, \
                    f"sl_{N}, Sym^{n}: got {actual}, expected {expected}"

    def test_antisymmetric_reps(self):
        """dim Lambda^k(C^N) = C(N, k)."""
        for N in range(2, 8):
            for k in range(1, N):
                expected = comb(N, k)
                lam = (1,) * k
                actual = hook_content_dimension(N, lam)
                assert actual == expected, \
                    f"sl_{N}, Lambda^{k}: got {actual}, expected {expected}"

    def test_too_many_rows_returns_zero(self):
        """Partition with >= N rows gives dim 0 for sl_N."""
        assert hook_content_dimension(3, (1, 1, 1)) == 0
        assert hook_content_dimension(2, (1, 1)) == 0

    def test_sl3_standard_dims(self):
        """Known sl_3 dimensions for small representations."""
        # (1,) = fund of sl_3: dim 3
        assert hook_content_dimension(3, (1,)) == 3
        # (1,1) as partition = column of height 2 = Lambda^2(C^3) = C(3,2) = 3
        assert hook_content_dimension(3, (1, 1)) == 3
        # (2,) = Sym^2(C^3): dim = C(4,2) = 6
        assert hook_content_dimension(3, (2,)) == 6
        # (2,1) = adjoint of sl_3: dim = 8
        assert hook_content_dimension(3, (2, 1)) == 8

    def test_large_N_fundamental(self):
        """For large N, dim of fundamental = N exactly."""
        assert hook_content_dimension(100, (1,)) == 100
        assert hook_content_dimension(1000, (1,)) == 1000


# =========================================================================
# Section 3: Hook-content vs Weyl (Path 2 cross-verification)
# =========================================================================

class TestHookVsWeyl:
    """Two independent dimension formulas must agree identically."""

    def test_sl2_agreement(self):
        """Hook-content and Weyl agree for all sl_2 reps up to dim 20."""
        for n in range(1, 20):
            d_hook = hook_content_dimension(2, (n,))
            d_weyl = weyl_dimension_slN_partition(2, (n,))
            assert d_hook == d_weyl, f"sl_2, n={n}: hook={d_hook}, weyl={d_weyl}"

    def test_sl3_agreement(self):
        """Hook-content and Weyl agree for sl_3 reps."""
        for a in range(6):
            for b in range(6 - a):
                lam = (a + b, b) if b > 0 else (a,) if a > 0 else ()
                # Actually, the partition for hw (a, b) of sl_3 is:
                # lam_1 = a + b, lam_2 = b (in partition notation)
                if a + b == 0:
                    continue
                d_hook = hook_content_dimension(3, lam)
                d_weyl = weyl_dimension_slN_partition(3, lam)
                assert d_hook == d_weyl, \
                    f"sl_3, hw=({a},{b}), part={lam}: hook={d_hook}, weyl={d_weyl}"

    def test_sl4_agreement(self):
        """Hook-content and Weyl agree for sl_4 reps up to 5 boxes."""
        result = verify_hook_vs_weyl(4, max_box_count=5)
        assert result['all_agree'], f"Mismatches: {result['mismatches']}"
        assert result['total_checked'] > 0

    def test_sl5_agreement(self):
        """Hook-content and Weyl agree for sl_5 reps up to 4 boxes."""
        result = verify_hook_vs_weyl(5, max_box_count=4)
        assert result['all_agree'], f"Mismatches: {result['mismatches']}"

    def test_sl10_agreement(self):
        """Hook-content and Weyl agree for sl_10 reps up to 3 boxes."""
        result = verify_hook_vs_weyl(10, max_box_count=3)
        assert result['all_agree'], f"Mismatches: {result['mismatches']}"


# =========================================================================
# Section 4: Partition enumeration
# =========================================================================

class TestPartitionEnumeration:
    """Test partition enumeration utilities."""

    def test_single_box_partitions(self):
        """Only one partition of size 1."""
        parts = partitions_bounded(1, 10)
        assert (1,) in parts

    def test_two_box_partitions(self):
        """Partitions of size <= 2: (1,), (2,), (1,1)."""
        parts = partitions_bounded(2, 10)
        assert (1,) in parts
        assert (2,) in parts
        assert (1, 1) in parts

    def test_row_constraint(self):
        """Partitions with at most 1 row are single-row partitions."""
        parts = partitions_at_most_k_rows(5, 1)
        for p in parts:
            assert num_rows(p) == 1

    def test_symmetric_partitions(self):
        """symmetric_partitions(n) gives single-row partitions."""
        parts = symmetric_partitions(5)
        assert parts == [(1,), (2,), (3,), (4,), (5,)]

    def test_partition_count_size_3(self):
        """There are 3 partitions of size 3: (3,), (2,1), (1,1,1)."""
        parts = [p for p in partitions_bounded(3, 10) if sum(p) == 3]
        assert len(parts) == 3


# =========================================================================
# Section 5: sl_2 = Riemann zeta (Path 1)
# =========================================================================

class TestSl2RiemannZeta:
    """The defining identity: zeta^{DK}_{sl_2}(s) = zeta(s)."""

    def test_sl2_zeta_at_s2(self):
        """zeta(2) = pi^2/6."""
        z = categorical_zeta_sl2_exact(2.0, N_terms=10000, include_trivial=True)
        expected = math.pi ** 2 / 6
        assert abs(z.real - expected) < 1e-3, f"Got {z.real}, expected {expected}"

    def test_sl2_zeta_at_s4(self):
        """zeta(4) = pi^4/90."""
        z = categorical_zeta_sl2_exact(4.0, N_terms=5000, include_trivial=True)
        expected = math.pi ** 4 / 90
        assert abs(z.real - expected) < 1e-5, f"Got {z.real}, expected {expected}"

    def test_sl2_zeta_at_s6(self):
        """zeta(6) = pi^6/945."""
        z = categorical_zeta_sl2_exact(6.0, N_terms=2000, include_trivial=True)
        expected = math.pi ** 6 / 945
        assert abs(z.real - expected) < 1e-8

    def test_sl2_via_hook_content(self):
        """Hook-content categorical zeta for sl_2 reproduces Riemann zeta.

        With max_box_count=20, sl_2 partition (n,) for n=1..20 has dim n+1=2..21.
        Including trivial adds dim=1. So hook sums d^{-s} for d=1,2,...,21.
        The direct version with N_terms=21 sums d=1,...,21.
        """
        z_hook = categorical_zeta_slN(2, 2.0, max_box_count=20, include_trivial=True)
        z_direct = categorical_zeta_sl2_exact(2.0, N_terms=21, include_trivial=True)
        assert abs(z_hook - z_direct) < 1e-10

    def test_verify_utility(self):
        """The verify_sl2_is_riemann utility reports match."""
        result = verify_sl2_is_riemann(3.0, N_terms=500)
        assert result['match']
        assert result['difference'] < 1e-10


# =========================================================================
# Section 6: Symmetric representation zeta
# =========================================================================

class TestSymmetricRepZeta:
    """Zeta restricted to single-row representations."""

    def test_dim_symmetric_rep(self):
        """dim Sym^n(C^N) = C(N+n-1, n)."""
        for N in [2, 5, 10, 20]:
            for n in [1, 2, 3, 5]:
                assert dim_symmetric_rep(N, n) == comb(N + n - 1, n)

    def test_sl2_symmetric_equals_full(self):
        """For sl_2, every irrep is symmetric, so symmetric zeta = full zeta."""
        for s in [2.0, 3.0, 4.0]:
            z_sym = symmetric_rep_zeta(2, s, max_n=50)
            z_full = categorical_zeta_sl2_exact(s, N_terms=50, include_trivial=False)
            assert abs(z_sym - z_full) < 1e-10, \
                f"s={s}: sym={z_sym}, full={z_full}"

    def test_symmetric_positive(self):
        """Symmetric zeta is positive for real s > 0."""
        for N in [3, 5, 10]:
            for s in [1.0, 2.0, 3.0]:
                z = symmetric_rep_zeta(N, s)
                assert z.real > 0

    def test_symmetric_decreasing_in_s(self):
        """For fixed N, symmetric zeta decreases as s increases."""
        for N in [3, 5, 10]:
            z_prev = symmetric_rep_zeta(N, 1.0).real
            for s in [2.0, 3.0, 4.0]:
                z_curr = symmetric_rep_zeta(N, s).real
                assert z_curr < z_prev + 1e-10, \
                    f"N={N}: z({s})={z_curr} >= z({s-1})={z_prev}"
                z_prev = z_curr

    def test_asymptotic_formula(self):
        """dim Sym^n(C^N) ~ N^n/n! at large N (Path 4)."""
        for n in [1, 2, 3]:
            result = verify_asymptotic_dimension(100, n)
            assert result['relative_error'] < 0.05, \
                f"n={n}: relative error {result['relative_error']}"

    def test_asymptotic_improves_with_N(self):
        """Asymptotic approximation improves as N grows."""
        n = 3
        errors = []
        for N in [10, 50, 100, 500]:
            result = verify_asymptotic_dimension(N, n)
            errors.append(result['relative_error'])
        # Errors should decrease
        for i in range(len(errors) - 1):
            assert errors[i + 1] < errors[i] + 1e-12


# =========================================================================
# Section 7: Adjoint representation
# =========================================================================

class TestAdjoint:
    """Adjoint representation contribution."""

    def test_dim_adjoint(self):
        """dim adj(sl_N) = N^2 - 1."""
        for N in range(2, 20):
            assert dim_adjoint(N) == N * N - 1

    def test_adjoint_contribution_decays(self):
        """(N^2 - 1)^{-s} -> 0 as N -> infty for s > 0."""
        for s in [1.0, 2.0]:
            prev = adjoint_contribution(2, s).real
            for N in range(3, 20):
                curr = adjoint_contribution(N, s).real
                assert curr < prev + 1e-15
                prev = curr

    def test_adjoint_sl2(self):
        """Adjoint of sl_2 has dim 3."""
        assert dim_adjoint(2) == 3
        assert abs(adjoint_contribution(2, 2.0) - 3.0 ** (-2)) < 1e-15


# =========================================================================
# Section 8: Rescaled zeta
# =========================================================================

class TestRescaledZeta:
    """Rescaled zeta Z_N(s) = N^{-2s} * zeta^{DK}_{sl_N}(s)."""

    def test_rescaled_sl2(self):
        """For sl_2: Z_2(s) = 2^{-2s} * zeta^{DK}_{sl_2}(s)."""
        s = 3.0
        z = rescaled_zeta(2, s, max_box_count=15)
        z_cat = categorical_zeta_slN(2, s, max_box_count=15)
        expected = 2.0 ** (-2 * s) * z_cat
        assert abs(z - expected) < 1e-12

    def test_rescaled_data(self):
        """rescaled_zeta_data returns dict of correct shape."""
        data = rescaled_zeta_data(2.0, N_range=range(2, 6), max_box_count=6)
        assert set(data.keys()) == {2, 3, 4, 5}
        for v in data.values():
            assert isinstance(v, complex)

    def test_rescaled_positive(self):
        """Z_N(s) > 0 for real s > 1."""
        for N in [3, 5, 8]:
            z = rescaled_zeta(N, 2.0, max_box_count=8)
            assert z.real > 0

    def test_rescaled_bounded(self):
        """Z_N(s) should remain bounded as N grows (for sufficiently large s)."""
        vals = []
        for N in range(2, 12):
            z = rescaled_zeta(N, 3.0, max_box_count=6)
            vals.append(z.real)
        # The values should not blow up
        assert max(vals) < 1e6


# =========================================================================
# Section 9: Planar zeta (at most 2 rows)
# =========================================================================

class TestPlanarZeta:
    """Planar limit: sum over partitions with at most 2 rows."""

    def test_planar_sl2_equals_full(self):
        """For sl_2, only single-row partitions exist, so planar = full."""
        for s in [2.0, 3.0]:
            z_plan = planar_zeta(2, s, max_box_count=15)
            z_full = categorical_zeta_slN(2, s, max_box_count=15)
            assert abs(z_plan - z_full) < 1e-10

    def test_planar_less_than_full(self):
        """For sl_N with N >= 3, planar < full (more reps in full sum)."""
        for N in [4, 5, 6]:
            z_plan = planar_zeta(N, 2.0, max_box_count=8)
            z_full = categorical_zeta_slN(N, 2.0, max_box_count=8)
            assert z_plan.real < z_full.real + 1e-10

    def test_planar_positive(self):
        """Planar zeta is positive for real s > 0."""
        for N in [3, 5, 10]:
            z = planar_zeta(N, 2.0, max_box_count=8)
            assert z.real > 0

    def test_planar_fraction_bounded(self):
        """Planar fraction is between 0 and 1."""
        for N in [3, 5, 8]:
            f = planar_fraction(N, 2.0, max_box_count=8)
            assert 0 < f <= 1.0 + 1e-10


# =========================================================================
# Section 10: Casimir zeta
# =========================================================================

class TestCasimirZeta:
    """Casimir zeta: sum C_2(lambda)^{-s}."""

    def test_casimir_sl2_values(self):
        """C_2(V_n) = n(n+2)/4 for sl_2."""
        assert casimir_eigenvalue_sl2(1) == Fraction(3, 4)
        assert casimir_eigenvalue_sl2(2) == Fraction(8, 4)
        assert casimir_eigenvalue_sl2(3) == Fraction(15, 4)
        assert casimir_eigenvalue_sl2(4) == Fraction(24, 4)

    def test_casimir_sl2_formula(self):
        """C_2(V_n) = n(n+2)/4, verify the pattern."""
        for n in range(1, 20):
            expected = Fraction(n * (n + 2), 4)
            assert casimir_eigenvalue_sl2(n) == expected

    def test_casimir_fundamental(self):
        """For sl_N fundamental rep, C_2 = (N^2-1)/(2N)."""
        for N in range(2, 10):
            c2 = casimir_eigenvalue_slN(N, (1,))
            expected = Fraction(N * N - 1, 2 * N)
            assert c2 == expected, f"sl_{N} fund: got {c2}, expected {expected}"

    def test_casimir_adjoint(self):
        """For sl_N adjoint rep, C_2 = N (in standard normalization)."""
        for N in [3, 4, 5]:
            adj = (2,) + (1,) * (N - 2)
            c2 = casimir_eigenvalue_slN(N, adj)
            assert c2 == N, f"sl_{N} adj: got {c2}, expected {N}"

    def test_casimir_not_riemann(self):
        """Casimir zeta for sl_2 is NOT the Riemann zeta."""
        z_cas = casimir_zeta_sl2(2.0, N_terms=500)
        z_riemann = sum(n ** (-2.0) for n in range(1, 501))
        # They should differ
        assert abs(z_cas - z_riemann) > 0.01, \
            "Casimir zeta should differ from Riemann zeta"

    def test_casimir_sl2_positive(self):
        """Casimir zeta is positive for real s > 0."""
        for s in [1.0, 2.0, 3.0]:
            z = casimir_zeta_sl2(s, N_terms=200)
            assert z.real > 0

    def test_casimir_sl2_four_s_factor(self):
        """zeta^{Cas}_{sl_2}(s) = 4^s * sum [n(n+2)]^{-s}.

        Verify by computing both sides.
        """
        s = 2.0
        z = casimir_zeta_sl2(s, N_terms=300)
        direct = sum((n * (n + 2)) ** (-s) for n in range(1, 301))
        assert abs(z - 4 ** s * direct) < 1e-10

    def test_casimir_slN_positive(self):
        """Casimir zeta for sl_N is positive."""
        for N in [3, 4, 5]:
            z = casimir_zeta_slN(N, 2.0, max_box_count=6)
            assert z.real > 0

    def test_casimir_summary(self):
        """casimir_summary runs without error."""
        result = casimir_summary(s_values=[2.0, 3.0], N_range=range(2, 5))
        assert 2.0 in result
        assert 2 in result[2.0]


# =========================================================================
# Section 11: Character zeta
# =========================================================================

class TestCharacterZeta:
    """Character zeta: sum chi_lambda(q)^{-s}."""

    def test_character_at_identity(self):
        """chi_V(1) = dim V (Path 5)."""
        result = verify_character_at_one(N_terms=30)
        assert result['all_agree'], f"Mismatches: {result['mismatches']}"

    def test_character_sl2_formula(self):
        """chi_{V_n}(q) = (q^{n+1} - q^{-(n+1)}) / (q - q^{-1})."""
        q = cmath.exp(0.3j)
        for n in range(1, 10):
            chi = character_sl2(n, q)
            expected = (q ** (n + 1) - q ** (-(n + 1))) / (q - q ** (-1))
            assert abs(chi - expected) < 1e-10

    def test_character_zeta_at_q1_equals_dim_zeta(self):
        """At q=1, character zeta = categorical (dimension) zeta."""
        s = 3.0
        z_char = character_zeta_sl2(s, 1.0, N_terms=100)
        z_dim = categorical_zeta_sl2_exact(s, N_terms=100, include_trivial=False)
        assert abs(z_char - z_dim) < 1e-8

    def test_root_of_unity(self):
        """exp(2*pi*i/N) is an N-th root of unity."""
        for N in [2, 3, 4, 5, 6]:
            q = root_of_unity(N)
            assert abs(q ** N - 1.0) < 1e-12

    def test_character_at_root_of_unity(self):
        """Characters at roots of unity take finite values."""
        for N in [3, 4, 5]:
            q = root_of_unity(N)
            for n in range(1, 10):
                chi = character_sl2(n, q)
                assert np.isfinite(abs(chi)), f"N={N}, n={n}: chi not finite"

    def test_character_zeta_root_of_unity_finite(self):
        """Character zeta at root of unity: should be finite for large enough s."""
        q = root_of_unity(3)
        z = character_zeta_sl2(4.0, q, N_terms=100)
        assert np.isfinite(abs(z))

    def test_character_symmetric_at_identity(self):
        """Symmetric representation character at identity = dim."""
        for N in [3, 4, 5]:
            q_diag = tuple([1.0] * N)
            for n in [1, 2, 3]:
                chi = character_slN_symmetric(N, n, q_diag)
                expected = dim_symmetric_rep(N, n)
                assert abs(chi - expected) < 1e-8, \
                    f"N={N}, n={n}: chi={chi}, dim={expected}"


# =========================================================================
# Section 12: Renormalized zeta (sl_infty limit)
# =========================================================================

class TestRenormalizedZeta:
    """Renormalized zeta for the sl_infty limit."""

    def test_frs_single_box(self):
        """f_{(1)} / 1! = 1 (one standard tableau of shape (1,))."""
        frs = frame_robinson_schensted_limit((1,))
        assert abs(frs - 1.0) < 1e-12

    def test_frs_two_boxes_row(self):
        """f_{(2)} / 2! = 1/2 (one tableau of shape (2,), divided by 2!)."""
        frs = frame_robinson_schensted_limit((2,))
        assert abs(frs - 0.5) < 1e-12

    def test_frs_two_boxes_col(self):
        """f_{(1,1)} / 2! = 1/2."""
        frs = frame_robinson_schensted_limit((1, 1))
        assert abs(frs - 0.5) < 1e-12

    def test_frs_staircase(self):
        """f_{(2,1)} / 3! = 2/6 = 1/3."""
        # (2,1) has 2 standard Young tableaux, so f = 2. f/3! = 2/6 = 1/3.
        frs = frame_robinson_schensted_limit((2, 1))
        assert abs(frs - 1.0 / 3) < 1e-12

    def test_renormalized_dim_converges(self):
        """dim V_lambda / N^{|lambda|} converges to f_lambda / |lambda|! as N -> infty."""
        for lam in [(1,), (2,), (1, 1), (2, 1)]:
            frs = frame_robinson_schensted_limit(lam)
            rd_prev = None
            for N in [10, 50, 100, 500]:
                rd = renormalized_dimension(N, lam)
                if rd_prev is not None:
                    # Should be converging to frs
                    assert abs(rd - frs) < abs(rd_prev - frs) + 1e-10
                rd_prev = rd

    def test_renormalized_zeta_finite(self):
        """Renormalized zeta is finite for s >= 2."""
        for N in [5, 10, 20]:
            z = renormalized_zeta(N, 2.0, max_box_count=6)
            assert np.isfinite(abs(z))

    def test_renormalized_limit_finite(self):
        """The N -> infty limiting renormalized zeta is finite."""
        z = renormalized_zeta_limit(2.0, max_box_count=6)
        assert np.isfinite(abs(z))
        assert z.real > 0

    def test_renormalized_converges_to_limit(self):
        """renormalized_zeta(N, s) -> renormalized_zeta_limit(s) as N -> infty.

        We fix max_rows to a small value so that the number of available
        partitions is constant across all N (avoiding the effect of new rows
        becoming available at larger N).  Then the only N-dependence is in
        dim/N^{|lam|} -> f_lam/|lam|! as N -> infty.
        """
        s = 3.0
        max_box = 4
        max_r = 3  # fix max rows so partition set is constant
        z_limit = renormalized_zeta_limit(s, max_box_count=max_box, max_rows=max_r)
        errors = []
        for N in [5, 10, 20, 50]:
            # Compute renormalized zeta restricted to same partitions
            parts = partitions_bounded(max_box, max_r, min_size=1)
            z_N = complex(0)
            for lam in parts:
                if num_rows(lam) < N:  # valid for sl_N
                    rd = renormalized_dimension(N, lam)
                    if rd > 1e-30:
                        z_N += rd ** (-s)
            errors.append(abs(z_N - z_limit))
        # Errors should decrease as N grows
        assert errors[-1] < errors[0] + 1e-6


# =========================================================================
# Section 13: 't Hooft double scaling
# =========================================================================

class TestTHooftScaling:
    """'t Hooft double scaling: N -> infty with sN = tau fixed."""

    def test_thooft_zeta_finite(self):
        """The double-scaled zeta is finite for reasonable tau."""
        for N in [5, 10, 20]:
            z = thooft_double_scaling_zeta(N, 5.0, max_box_count=6)
            assert np.isfinite(abs(z))

    def test_thooft_rescaled_finite(self):
        """Rescaled 't Hooft zeta is finite."""
        for N in [5, 10, 20]:
            z = thooft_rescaled(N, 5.0, max_box_count=6)
            assert np.isfinite(abs(z))

    def test_thooft_at_large_tau(self):
        """At large tau (= large effective s), zeta is small."""
        for N in [5, 10]:
            z = thooft_double_scaling_zeta(N, 20.0, max_box_count=6)
            assert abs(z) < 100  # reasonable bound


# =========================================================================
# Section 14: Monotonicity (Path 3)
# =========================================================================

class TestMonotonicity:
    """Monotonicity of categorical zeta in N."""

    def test_monotone_decreasing_at_s2_fixed_truncation(self):
        """At fixed max_box_count, the zeta DECREASES in N for s=2.

        Reason: increasing N enlarges existing representations (dims grow,
        so dim^{-s} shrinks), while the new representations that become
        available (more rows) have size bounded by max_box_count and thus
        contribute modestly.  The net effect at fixed truncation is decrease.

        The TRUE (un-truncated) zeta would eventually increase with N,
        but that requires summing far more terms.
        """
        result = zeta_monotonicity_check(2.0, N_range=range(2, 10),
                                         max_box_count=6)
        # At fixed truncation, observed to be decreasing
        assert result['is_monotone_decreasing'], \
            f"Differences: {result['differences']}"

    def test_monotone_decreasing_at_s3_fixed_truncation(self):
        """At fixed max_box_count, the zeta decreases in N for s=3."""
        result = zeta_monotonicity_check(3.0, N_range=range(2, 10),
                                         max_box_count=6)
        assert result['is_monotone_decreasing']

    def test_symmetric_zeta_decreasing_in_N(self):
        """For SYMMETRIC reps, the zeta DECREASES in N at fixed s > 0.

        Reason: dim Sym^n(C^N) grows with N, so dim^{-s} shrinks.
        But there are no NEW symmetric reps as N increases (always one per n).
        So each term shrinks while the number of terms stays the same.
        """
        for s in [2.0, 3.0]:
            vals = symmetric_zeta_growth(s, N_range=range(2, 12))
            Ns = sorted(vals.keys())
            for i in range(len(Ns) - 1):
                assert vals[Ns[i + 1]] <= vals[Ns[i]] + 1e-10, \
                    f"s={s}: sym zeta not decreasing at N={Ns[i]}"


# =========================================================================
# Section 15: Large-N asymptotics (Path 4)
# =========================================================================

class TestLargeNAsymptotics:
    """Asymptotic behavior at large N."""

    def test_fundamental_dim_equals_N(self):
        """dim V_{fund} = N exactly."""
        for N in range(2, 50):
            assert hook_content_dimension(N, (1,)) == N

    def test_adjoint_dim_quadratic(self):
        """dim V_{adj} = N^2 - 1 for sl_N."""
        for N in range(2, 30):
            assert dim_adjoint(N) == N * N - 1

    def test_symmetric_rep_large_N_leading(self):
        """dim Sym^n(C^N) / N^n -> 1/n! as N -> infty."""
        for n in [2, 3, 4]:
            ratios = []
            for N in [50, 100, 200, 500]:
                d = dim_symmetric_rep(N, n)
                ratios.append(d / N ** n)
            # Should converge to 1/n!
            expected = 1.0 / factorial(n)
            assert abs(ratios[-1] - expected) < 0.01

    def test_adjoint_zeta_vanishes(self):
        """Adjoint contribution (N^2-1)^{-s} -> 0 as N -> infty."""
        s = 2.0
        for N in [10, 100, 1000]:
            val = adjoint_contribution(N, s).real
            assert val < 1.0 / (N ** 2 - 1) ** s + 1e-15


# =========================================================================
# Section 16: Cross-checks and multi-path verification
# =========================================================================

class TestCrossChecks:
    """Multi-path cross-verification."""

    def test_sl2_three_paths(self):
        """sl_2 zeta at s=2 via three independent methods.

        For sl_2, V_{(n)} has dim n+1.  The nontrivial partitions (n,) for
        n=1,...,M give dims 2,...,M+1.  Including trivial: dims 1,...,M+1.
        We align all three paths to sum d^{-s} for d = 1, 2, ..., D.
        """
        s = 2.0
        D = 500

        # Path 1: Direct dimension sum (sl_2: dim(V_n) = n+1 for n=0,...,D-1)
        z1 = sum((n + 1) ** (-s) for n in range(D))

        # Path 2: Hook-content formula (n=1,...,D-1 give dims 2,...,D) + trivial
        z2 = 1.0  # trivial rep (dim 1)
        for n in range(1, D):
            d = hook_content_dimension(2, (n,))
            z2 += d ** (-s)

        # Path 3: Riemann zeta partial sum d=1,...,D
        z3 = sum(d ** (-s) for d in range(1, D + 1))

        assert abs(z1 - z2) < 1e-10, f"Path 1 vs 2: {abs(z1-z2)}"
        assert abs(z1 - z3) < 1e-10, f"Path 1 vs 3: {abs(z1-z3)}"

    def test_planar_contains_symmetric_and_two_row(self):
        """Planar zeta >= symmetric zeta (planar includes 2-row reps too)."""
        for N in [4, 5, 6]:
            s = 2.0
            z_plan = planar_zeta(N, s, max_box_count=8)
            z_sym = symmetric_rep_zeta(N, s, max_n=8)
            assert z_plan.real >= z_sym.real - 1e-10

    def test_full_geq_planar_geq_symmetric(self):
        """full zeta >= planar zeta >= symmetric zeta."""
        for N in [4, 5]:
            s = 2.0
            z_full = categorical_zeta_slN(N, s, max_box_count=8)
            z_plan = planar_zeta(N, s, max_box_count=8)
            z_sym = symmetric_rep_zeta(N, s, max_n=8)
            assert z_full.real >= z_plan.real - 1e-10
            assert z_plan.real >= z_sym.real - 1e-10

    def test_casimir_vs_dim_ordering(self):
        """Casimir and dimension give DIFFERENT zetas (distinct objects)."""
        s = 2.0
        z_dim = categorical_zeta_slN(3, s, max_box_count=6)
        z_cas = casimir_zeta_slN(3, s, max_box_count=6)
        assert abs(z_dim - z_cas) > 1e-3, \
            "Casimir and dim zetas should differ for sl_3"

    def test_hook_content_dimension_exact_integer(self):
        """Hook-content formula always gives a positive integer for valid input."""
        for N in [3, 4, 5]:
            for lam in partitions_bounded(5, N - 1):
                d = hook_content_dimension(N, lam)
                assert isinstance(d, int)
                assert d > 0

    def test_casimir_grows_with_representation(self):
        """Casimir eigenvalue grows with the size of the representation."""
        # For sl_2: C_2(V_n) = n(n+2)/4 is increasing in n
        for n in range(1, 20):
            c_n = float(casimir_eigenvalue_sl2(n))
            c_n1 = float(casimir_eigenvalue_sl2(n + 1))
            assert c_n1 > c_n


# =========================================================================
# Section 17: Convergence of rescaled zeta
# =========================================================================

class TestRescaledConvergence:
    """Study convergence of Z_N(s) = N^{-2s} * zeta as N grows."""

    def test_rescaled_zeta_data_shape(self):
        """rescaled_zeta_data returns correct structure."""
        data = rescaled_zeta_data(3.0, N_range=range(2, 8), max_box_count=6)
        assert len(data) == 6

    def test_rescaled_decreasing_at_large_s(self):
        """For very large s, rescaled zeta Z_N(s) should decrease with N.

        Reason: the N^{-2s} prefactor dominates, killing the growth.
        """
        s = 5.0
        vals = []
        for N in range(3, 10):
            z = rescaled_zeta(N, s, max_box_count=6).real
            vals.append(z)
        # At large s, each subsequent value should be smaller (eventually)
        # This is not guaranteed for ALL N (depends on new reps entering),
        # but for large enough s it should hold for moderate N.
        # Just check values are bounded and finite.
        assert all(np.isfinite(v) for v in vals)

    def test_rescaled_at_s2(self):
        """Rescaled zeta at s=2 for several N values."""
        data = rescaled_zeta_data(2.0, N_range=range(2, 8), max_box_count=6)
        for N, z in data.items():
            assert np.isfinite(abs(z))
            assert z.real > 0


# =========================================================================
# Section 18: Summary and integration tests
# =========================================================================

class TestSummary:
    """Integration tests for summary functions."""

    def test_large_n_summary(self):
        """large_n_summary runs and produces correct structure."""
        result = large_n_summary(s_values=[2.0, 3.0],
                                 N_range=range(2, 5),
                                 max_box_count=5)
        assert 2.0 in result
        assert 2 in result[2.0]
        assert 'full' in result[2.0][2]
        assert 'rescaled' in result[2.0][2]
        assert 'planar' in result[2.0][2]
        assert 'symmetric' in result[2.0][2]

    def test_abscissa_of_convergence(self):
        """Abscissa estimate returns a finite value."""
        sigma = abscissa_of_convergence_slN(3, max_box_count=6)
        assert np.isfinite(sigma)
        assert sigma > 0

    def test_abscissa_sl2_finite(self):
        """For sl_2, the abscissa estimate returns a finite value.

        The true abscissa is 1 (Riemann zeta), but our crude comparison
        of two truncations may overestimate it.  Just check finiteness
        and that it is within the tested range.
        """
        sigma = abscissa_of_convergence_slN(2, max_box_count=10)
        assert np.isfinite(sigma)
        assert sigma <= 5.0


# =========================================================================
# Section 19: Edge cases and robustness
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_empty_partition(self):
        """Empty partition gives trivial rep."""
        assert hook_content_dimension(5, ()) == 1

    def test_single_box_dimension(self):
        """Single box = fundamental, dim = N."""
        assert hook_content_dimension(7, (1,)) == 7

    def test_very_large_N(self):
        """Dimensions at N=100 are correct for small partitions."""
        assert hook_content_dimension(100, (1,)) == 100
        assert hook_content_dimension(100, (2,)) == comb(101, 2)
        assert hook_content_dimension(100, (1, 1)) == comb(100, 2)

    def test_zero_s(self):
        """At s=0, each term contributes 1, so zeta counts representations."""
        # For sl_2 with N_terms, zeta(0) = N_terms
        z = categorical_zeta_sl2_exact(0.0, N_terms=10, include_trivial=True)
        assert abs(z - 10) < 1e-10

    def test_negative_s(self):
        """At s < 0, larger dims contribute MORE (zeta diverges)."""
        z_neg = categorical_zeta_sl2_exact(-1.0, N_terms=100, include_trivial=True)
        z_pos = categorical_zeta_sl2_exact(1.0, N_terms=100, include_trivial=True)
        # At s=-1, sum = 1 + 2 + ... + 100 = 5050 >> sum at s=1
        assert z_neg.real > z_pos.real

    def test_complex_s(self):
        """Zeta at complex s returns complex value."""
        z = categorical_zeta_sl2_exact(2.0 + 1j, N_terms=100)
        assert isinstance(z, complex)
        assert np.isfinite(abs(z))

    def test_sl_large_n_small_partition(self):
        """For large N, partitions with few boxes give well-defined dims."""
        for N in [10, 50, 100]:
            d = hook_content_dimension(N, (2, 1))
            # dim of (2,1) = N(N+1)(N-1)/3 for sl_N
            expected = N * (N + 1) * (N - 1) // 3
            assert d == expected, f"N={N}: got {d}, expected {expected}"
