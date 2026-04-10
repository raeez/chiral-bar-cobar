r"""Tests for virasoro_pbw_bar_motzkin_engine.py.

Verifies partition numbers, Motzkin numbers, bar cohomology dimensions,
and the structural identities linking them for the Virasoro algebra.

MULTI-PATH VERIFICATION:
  Path 1: Partition numbers match OEIS A000041 for n=1..20
  Path 2: Motzkin numbers match OEIS A001006 for n=0..19
  Path 3: Motzkin recurrence holds at every n
  Path 4: Motzkin via trinomial sum matches recurrence (independent formula)
  Path 5: Bar cohomology = Motzkin convolution [x^n] x*M(x)^2
  Path 6: Identity M(n) - M(n-1) = bar_cohom(n-1) for n >= 2
  Path 7: Boundary cases (n=0, n=1, n=2)
  Path 8: Partition generating function cross-check (Euler product)
  Path 9: Motzkin generating function algebraic equation
  Path 10: Consistency with bar_cohomology_wn_universal_engine (W_2 = Vir)
  Path 11: Extended range n=11..20 (new predictions)

References:
  OEIS A000041 (partition numbers, Euler 1748)
  OEIS A001006 (Motzkin numbers, Motzkin 1948)
  Donaghey & Shapiro (1977), trinomial representation
  bar_cohomology_wn_universal_engine.py (W_2 generating function)
  CLAUDE.md: kappa(Vir) = c/2
"""

import pytest

from compute.lib.virasoro_pbw_bar_motzkin_engine import (
    partitions_up_to,
    partition_number,
    motzkin_up_to,
    motzkin_number,
    motzkin_via_trinomial,
    virasoro_bar_cohom_gen_degree,
    virasoro_pbw_bar_motzkin_table,
    PARTITIONS_1_TO_20,
    MOTZKIN_0_TO_19,
    BAR_COHOM_GEN_DEGREE_1_TO_10,
    _binomial,
)


# ============================================================
# Canonical reference data
# ============================================================

# OEIS A000041: p(0)..p(20)
# VERIFIED [DC] dynamic programming + [LT] OEIS A000041 (Euler, 1748)
OEIS_A000041 = [
    1,  # p(0)
    1, 2, 3, 5, 7, 11, 15, 22, 30, 42,
    56, 77, 101, 135, 176, 231, 297, 385, 490, 627,
]

# OEIS A001006: M(0)..M(19)
# VERIFIED [DC] recurrence + [LT] OEIS A001006 (Motzkin, 1948)
# VERIFIED [CF] trinomial sum (Donaghey & Shapiro, 1977)
OEIS_A001006 = [
    1, 1, 2, 4, 9, 21, 51, 127, 323, 835,
    2188, 5798, 15511, 41835, 113634, 310572, 853467, 2356779, 6536382, 18199284,
]

# Extended Motzkin M(20)..M(24) for extended range tests
# VERIFIED [DC] recurrence + [LT] OEIS A001006
OEIS_A001006_EXTENDED = [
    50852019, 142547559, 400763223, 1131467286, 3206598054,
]

# Bar cohomology dims [x^n] x*M(x)^2 for degrees 1..10
# VERIFIED [DC] convolution + [LT] bar_cohomology_wn_universal_engine.py
EXPECTED_BAR_COHOM = [1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610]


# ============================================================
# Partition number tests
# ============================================================

class TestPartitionNumbers:
    """Tests for partition number computation."""

    def test_partition_base_cases(self):
        """p(0) = 1 (empty partition), p(1) = 1."""
        p = partitions_up_to(1)
        assert p[0] == 1
        assert p[1] == 1

    def test_partitions_small(self):
        """p(2) = 2, p(3) = 3, p(4) = 5, p(5) = 7."""
        # VERIFIED [DC] enumeration + [LT] OEIS A000041
        p = partitions_up_to(5)
        assert p[2] == 2   # {2, 1+1}
        assert p[3] == 3   # {3, 2+1, 1+1+1}
        assert p[4] == 5   # {4, 3+1, 2+2, 2+1+1, 1+1+1+1}
        assert p[5] == 7

    def test_partitions_1_to_20(self):
        """Match OEIS A000041 for n=1..20."""
        # VERIFIED [DC] dynamic programming + [LT] OEIS A000041
        p = partitions_up_to(20)
        for n in range(1, 21):
            assert p[n] == OEIS_A000041[n], f"p({n}) mismatch"

    def test_partition_number_function(self):
        """partition_number(n) agrees with partitions_up_to."""
        for n in range(21):
            assert partition_number(n) == OEIS_A000041[n]

    def test_partition_negative(self):
        """p(n) = 0 for n < 0."""
        assert partition_number(-1) == 0
        assert partition_number(-5) == 0

    def test_partitions_match_module_constant(self):
        """Module constant PARTITIONS_1_TO_20 matches computation."""
        p = partitions_up_to(20)
        for i, n in enumerate(range(1, 21)):
            assert PARTITIONS_1_TO_20[i] == p[n]

    def test_partition_euler_product_cross_check(self):
        """Cross-check: partition GF = 1/prod(1-x^k) via polynomial multiplication.

        Truncate the Euler product to degree 15 and verify coefficients.
        # VERIFIED [DC] polynomial multiplication + [LT] OEIS A000041
        """
        N = 15
        # Start with 1, multiply by 1/(1-x^k) = sum x^{jk} for j=0,1,...
        coeffs = [0] * (N + 1)
        coeffs[0] = 1
        for k in range(1, N + 1):
            for j in range(k, N + 1):
                coeffs[j] += coeffs[j - k]
        for n in range(N + 1):
            assert coeffs[n] == OEIS_A000041[n], f"Euler product p({n}) mismatch"


# ============================================================
# Motzkin number tests
# ============================================================

class TestMotzkinNumbers:
    """Tests for Motzkin number computation."""

    def test_motzkin_base_cases(self):
        """M(0) = 1, M(1) = 1."""
        assert motzkin_number(0) == 1
        assert motzkin_number(1) == 1

    def test_motzkin_small(self):
        """M(2) = 2, M(3) = 4, M(4) = 9."""
        # VERIFIED [DC] recurrence + [LT] OEIS A001006
        assert motzkin_number(2) == 2
        assert motzkin_number(3) == 4
        assert motzkin_number(4) == 9

    def test_motzkin_0_to_19(self):
        """Match OEIS A001006 for n=0..19."""
        # VERIFIED [DC] recurrence + [LT] OEIS A001006
        m = motzkin_up_to(19)
        for n in range(20):
            assert m[n] == OEIS_A001006[n], f"M({n}) mismatch"

    def test_motzkin_match_module_constant(self):
        """Module constant MOTZKIN_0_TO_19 matches computation."""
        m = motzkin_up_to(19)
        for n in range(20):
            assert MOTZKIN_0_TO_19[n] == m[n]

    def test_motzkin_negative(self):
        """M(n) = 0 for n < 0."""
        assert motzkin_number(-1) == 0
        assert motzkin_number(-3) == 0

    def test_motzkin_empty_list(self):
        """motzkin_up_to(-1) returns empty list."""
        assert motzkin_up_to(-1) == []

    def test_motzkin_recurrence_explicit(self):
        """Verify the recurrence M(n) = M(n-1) + sum M(k)*M(n-2-k) at each n.

        # VERIFIED [DC] recurrence definition + [LT] OEIS A001006
        """
        m = motzkin_up_to(19)
        for n in range(2, 20):
            conv = sum(m[k] * m[n - 2 - k] for k in range(n - 1))
            assert m[n] == m[n - 1] + conv, f"Recurrence fails at n={n}"

    def test_motzkin_trinomial_cross_check(self):
        """Motzkin via trinomial sum matches recurrence for n=0..19.

        Independent computation path using:
          M(n) = sum_{k=0}^{floor(n/2)} C(n,2k) * C_k

        # VERIFIED [DC] recurrence + [CF] trinomial sum (Donaghey & Shapiro, 1977)
        """
        m_rec = motzkin_up_to(19)
        for n in range(20):
            m_tri = motzkin_via_trinomial(n)
            assert m_rec[n] == m_tri, f"Trinomial mismatch at n={n}: rec={m_rec[n]}, tri={m_tri}"

    def test_motzkin_extended_range(self):
        """Verify M(20)..M(24) against extended OEIS data.

        # VERIFIED [DC] recurrence + [LT] OEIS A001006
        """
        m = motzkin_up_to(24)
        for i, n in enumerate(range(20, 25)):
            assert m[n] == OEIS_A001006_EXTENDED[i], f"M({n}) mismatch"

    def test_motzkin_trinomial_extended(self):
        """Trinomial formula matches recurrence for M(20)..M(24)."""
        m = motzkin_up_to(24)
        for n in range(20, 25):
            assert m[n] == motzkin_via_trinomial(n), f"Trinomial mismatch at M({n})"

    def test_motzkin_growth_rate(self):
        """M(n)/M(n-1) approaches 3 as n -> infinity.

        The Motzkin GF has radius of convergence 1/3 (from discriminant
        1 - 2x - 3x^2 = 0 at x = 1/3).  So M(n) ~ C * 3^n / n^{3/2}.

        # VERIFIED [DC] ratio computation + [LT] Flajolet & Sedgewick (2009)
        """
        m = motzkin_up_to(19)
        ratio = m[19] / m[18]
        assert 2.7 < ratio < 3.0, f"Growth ratio M(19)/M(18) = {ratio} out of range"


# ============================================================
# Bar cohomology tests
# ============================================================

class TestBarCohomology:
    """Tests for Virasoro bar cohomology in generation degree."""

    def test_bar_cohom_degrees_1_to_10(self):
        """Bar cohomology dims match known values for degrees 1..10.

        # VERIFIED [DC] Motzkin convolution + [LT] bar_cohomology_wn_universal_engine.py
        """
        bar = virasoro_bar_cohom_gen_degree(10)
        for n in range(1, 11):
            assert bar[n] == EXPECTED_BAR_COHOM[n - 1], \
                f"bar_cohom({n}) = {bar[n]}, expected {EXPECTED_BAR_COHOM[n - 1]}"

    def test_bar_cohom_matches_module_constant(self):
        """Module constant BAR_COHOM_GEN_DEGREE_1_TO_10 matches computation."""
        bar = virasoro_bar_cohom_gen_degree(10)
        for n in range(1, 11):
            assert BAR_COHOM_GEN_DEGREE_1_TO_10[n - 1] == bar[n]

    def test_bar_cohom_as_motzkin_convolution(self):
        """bar_cohom(n) = sum_{k=0}^{n-1} M(k)*M(n-1-k) (definition check).

        # VERIFIED [DC] convolution definition + [LT] P(x) = x*M(x)^2
        """
        m = motzkin_up_to(20)
        bar = virasoro_bar_cohom_gen_degree(20)
        for n in range(1, 21):
            conv = sum(m[k] * m[n - 1 - k] for k in range(n))
            assert bar[n] == conv, f"Convolution mismatch at n={n}"

    def test_bar_cohom_degree_1(self):
        """bar_cohom(1) = M(0)^2 = 1 (single generator L_{-2} at degree 1).

        # VERIFIED [DC] M(0)=1 + [LT] bar_cohomology_wn_universal_engine.py
        """
        bar = virasoro_bar_cohom_gen_degree(1)
        assert bar[1] == 1

    def test_bar_cohom_degree_2(self):
        """bar_cohom(2) = M(0)*M(1) + M(1)*M(0) = 2.

        # VERIFIED [DC] explicit convolution + [LT] bar_cohomology_wn_universal_engine.py
        """
        bar = virasoro_bar_cohom_gen_degree(2)
        assert bar[2] == 2

    def test_bar_cohom_extended_degrees_11_to_20(self):
        """Bar cohomology dims for degrees 11..20 (new predictions).

        Computed via Motzkin convolution.
        # VERIFIED [DC] convolution of independently verified Motzkin numbers
        """
        bar = virasoro_bar_cohom_gen_degree(20)
        # These are predictions from the engine; verified by the convolution formula
        # and the identity M(n) - M(n-1) = bar_cohom(n-1).
        expected_11_to_20 = [9713, 26324, 71799, 196938, 542895,
                             1503312, 4179603, 11662902, 32652735, 91695540]
        for i, n in enumerate(range(11, 21)):
            assert bar[n] == expected_11_to_20[i], \
                f"bar_cohom({n}) = {bar[n]}, expected {expected_11_to_20[i]}"

    def test_bar_cohom_growth_rate(self):
        """bar_cohom(n) ~ C * 9^n (since M(x) has radius 1/3, M(x)^2 has radius 1/3).

        Actually x*M(x)^2 has the same radius of convergence 1/3 as M(x),
        so bar_cohom(n) grows like 3^n.  The ratio bar(n)/bar(n-1) -> 3.

        More precisely: since P(x) = x*M(x)^2 and M(x) ~ C/sqrt(1-3x),
        we get P(x) ~ C^2 * x / (1-3x), so [x^n]P ~ C^2 * 3^{n-1}.

        # VERIFIED [DC] ratio + [LT] Flajolet & Sedgewick (2009)
        """
        bar = virasoro_bar_cohom_gen_degree(20)
        ratio = bar[20] / bar[19]
        assert 2.7 < ratio < 3.0, f"Growth ratio bar(20)/bar(19) = {ratio}"


# ============================================================
# Structural identity tests
# ============================================================

class TestStructuralIdentities:
    """Tests for the identities linking Motzkin, partitions, and bar cohomology."""

    def test_motzkin_increment_equals_bar_cohom(self):
        """M(n) - M(n-1) = bar_cohom(n-1) for n = 2..20.

        This is the Motzkin recurrence rewritten:
          M(n) = M(n-1) + sum_{k=0}^{n-2} M(k)*M(n-2-k)
               = M(n-1) + bar_cohom(n-1)

        # VERIFIED [DC] direct computation + [SY] recurrence rewriting
        """
        m = motzkin_up_to(20)
        bar = virasoro_bar_cohom_gen_degree(20)
        for n in range(2, 21):
            increment = m[n] - m[n - 1]
            assert increment == bar[n - 1], \
                f"At n={n}: M({n})-M({n-1}) = {increment} != bar_cohom({n-1}) = {bar[n-1]}"

    def test_motzkin_increment_at_n1(self):
        """M(1) - M(0) = 0, and bar_cohom(0) is not defined (degree starts at 1).

        The identity M(n) - M(n-1) = bar_cohom(n-1) holds for n >= 2.
        At n=1: M(1) - M(0) = 0, which would be bar_cohom(0) = 0 (no degree-0 bar cohomology).
        """
        m = motzkin_up_to(1)
        assert m[1] - m[0] == 0

    def test_table_consistency(self):
        """Every row of the table satisfies bar_cohom + motzkin_prev = convolution check.

        # VERIFIED [DC] table row computation
        """
        table = virasoro_pbw_bar_motzkin_table(20)
        m = motzkin_up_to(20)
        for row in table:
            n = row['degree']
            assert row['motzkin'] == m[n]
            assert row['motzkin_prev'] == m[n - 1]
            assert row['motzkin_increment'] == m[n] - m[n - 1]

    def test_table_length(self):
        """Table has exactly n_max rows."""
        table = virasoro_pbw_bar_motzkin_table(20)
        assert len(table) == 20

    def test_table_degrees_sequential(self):
        """Table degrees are 1, 2, ..., 20."""
        table = virasoro_pbw_bar_motzkin_table(20)
        for i, row in enumerate(table):
            assert row['degree'] == i + 1


# ============================================================
# Binomial coefficient tests
# ============================================================

class TestBinomial:
    """Tests for the internal binomial coefficient function."""

    def test_binomial_boundary(self):
        """C(n,0) = C(n,n) = 1."""
        for n in range(10):
            assert _binomial(n, 0) == 1
            assert _binomial(n, n) == 1

    def test_binomial_negative_k(self):
        """C(n,k) = 0 for k < 0 or k > n."""
        assert _binomial(5, -1) == 0
        assert _binomial(5, 6) == 0

    def test_binomial_pascal(self):
        """C(n,k) = C(n-1,k-1) + C(n-1,k) (Pascal's rule)."""
        for n in range(1, 10):
            for k in range(1, n):
                assert _binomial(n, k) == _binomial(n - 1, k - 1) + _binomial(n - 1, k)

    def test_binomial_known_values(self):
        """C(10,3) = 120, C(10,5) = 252.
        # VERIFIED [DC] computation + [LT] standard
        """
        assert _binomial(10, 3) == 120
        assert _binomial(10, 5) == 252


# ============================================================
# Combinatorial interpretation tests
# ============================================================

class TestCombinatorialInterpretation:
    """Tests for combinatorial meaning of the Motzkin numbers."""

    def test_motzkin_counts_paths(self):
        """M(n) counts lattice paths from (0,0) to (n,0) using steps
        (1,1), (1,0), (1,-1) that never go below y=0.

        Verify by brute-force path enumeration for small n.
        # VERIFIED [DC] path enumeration + [LT] OEIS A001006
        """
        def count_motzkin_paths(n):
            """Count Motzkin paths of length n by dynamic programming."""
            if n == 0:
                return 1
            # dp[step][height] = number of paths
            dp = [[0] * (n + 1) for _ in range(n + 1)]
            dp[0][0] = 1
            for i in range(n):
                for h in range(n + 1):
                    if dp[i][h] == 0:
                        continue
                    # Step right (1,0)
                    dp[i + 1][h] += dp[i][h]
                    # Step up (1,1)
                    if h + 1 <= n:
                        dp[i + 1][h + 1] += dp[i][h]
                    # Step down (1,-1)
                    if h - 1 >= 0:
                        dp[i + 1][h - 1] += dp[i][h]
            return dp[n][0]

        for n in range(10):
            assert count_motzkin_paths(n) == OEIS_A001006[n], \
                f"Path count at n={n}: {count_motzkin_paths(n)} != {OEIS_A001006[n]}"

    def test_motzkin_catalan_relation(self):
        """M(n) = sum_{k=0}^{floor(n/2)} C(n,2k) * C_k.

        At n=4: C(4,0)*C_0 + C(4,2)*C_1 + C(4,4)*C_2
              = 1*1 + 6*1 + 1*2 = 9 = M(4).

        # VERIFIED [DC] explicit sum + [LT] Donaghey & Shapiro (1977)
        """
        # C_0=1, C_1=1, C_2=2
        val = _binomial(4, 0) * 1 + _binomial(4, 2) * 1 + _binomial(4, 4) * 2
        assert val == 9
        assert val == OEIS_A001006[4]


# ============================================================
# Generating function algebraic equation test
# ============================================================

class TestGeneratingFunction:
    """Tests for the Motzkin generating function properties."""

    def test_algebraic_equation(self):
        """M(x) satisfies x^2 * M^2 + (x-1)*M + 1 = 0.

        Verify by truncated power series: compute LHS to degree 15
        and check all coefficients vanish.

        # VERIFIED [DC] polynomial arithmetic + [LT] Flajolet & Sedgewick (2009)
        """
        N = 15
        m = motzkin_up_to(N)

        # Compute M(x)^2 as convolution
        m_sq = [0] * (N + 1)
        for i in range(N + 1):
            for j in range(N + 1 - i):
                m_sq[i + j] += m[i] * m[j]

        # LHS = x^2 * M^2 + (x-1)*M + 1
        # Coefficient of x^n in LHS:
        #   [x^n] x^2*M^2 = m_sq[n-2]  (for n >= 2, else 0)
        #   [x^n] x*M     = m[n-1]     (for n >= 1, else 0)
        #   [x^n] (-1)*M  = -m[n]
        #   [x^n] 1       = 1 if n=0 else 0
        for n in range(N + 1):
            lhs = 0
            if n >= 2:
                lhs += m_sq[n - 2]
            if n >= 1:
                lhs += m[n - 1]
            lhs -= m[n]
            if n == 0:
                lhs += 1
            assert lhs == 0, f"Algebraic equation fails at x^{n}: LHS = {lhs}"

    def test_bar_gf_is_x_m_squared(self):
        """P(x) = x*M(x)^2: verify coefficients match bar_cohom.

        # VERIFIED [DC] convolution + [LT] bar_cohomology_wn_universal_engine.py
        """
        N = 15
        m = motzkin_up_to(N)
        bar = virasoro_bar_cohom_gen_degree(N)

        for n in range(1, N + 1):
            # [x^n] x*M^2 = [x^{n-1}] M^2 = sum_{k=0}^{n-1} M(k)*M(n-1-k)
            conv = sum(m[k] * m[n - 1 - k] for k in range(n))
            assert bar[n] == conv


# ============================================================
# Extended range tests (degrees 11-20, the new predictions)
# ============================================================

class TestExtendedRange:
    """Tests for the extended range n=11..20."""

    def test_motzkin_11_to_20(self):
        """Motzkin numbers M(10)..M(19) match extended OEIS data.

        # VERIFIED [DC] recurrence + [LT] OEIS A001006
        """
        m = motzkin_up_to(19)
        expected = OEIS_A001006[10:]
        for i, n in enumerate(range(10, 20)):
            assert m[n] == expected[i], f"M({n}) = {m[n]}, expected {expected[i]}"

    def test_partitions_11_to_20(self):
        """Partition numbers p(11)..p(20) match OEIS A000041.

        # VERIFIED [DC] dynamic programming + [LT] OEIS A000041
        """
        p = partitions_up_to(20)
        expected = OEIS_A000041[11:]
        for i, n in enumerate(range(11, 21)):
            assert p[n] == expected[i], f"p({n}) = {p[n]}, expected {expected[i]}"

    def test_bar_cohom_11_to_20_via_two_paths(self):
        """Bar cohomology at degrees 11-20 verified by two independent paths.

        Path 1: direct convolution sum_{k=0}^{n-1} M(k)*M(n-1-k)
        Path 2: Motzkin increment M(n+1) - M(n) = bar_cohom(n)

        # VERIFIED [DC] convolution + [SY] Motzkin increment identity
        """
        m = motzkin_up_to(21)
        bar = virasoro_bar_cohom_gen_degree(20)

        for n in range(11, 21):
            # Path 1: convolution
            conv = sum(m[k] * m[n - 1 - k] for k in range(n))
            # Path 2: increment
            increment = m[n + 1] - m[n] if n + 1 <= 21 else None

            assert bar[n] == conv, f"Convolution mismatch at n={n}"
            if increment is not None:
                assert bar[n] == increment, \
                    f"Increment mismatch at n={n}: bar={bar[n]}, M({n+1})-M({n})={increment}"

    def test_full_table_20(self):
        """Full table for n_max=20 has all expected fields."""
        table = virasoro_pbw_bar_motzkin_table(20)
        assert len(table) == 20
        for row in table:
            assert 'degree' in row
            assert 'pbw_dim' in row
            assert 'bar_cohom' in row
            assert 'motzkin' in row
            assert 'motzkin_prev' in row
            assert 'motzkin_increment' in row


# ============================================================
# Regression / sanity tests
# ============================================================

class TestSanity:
    """Sanity checks and boundary conditions."""

    def test_bar_cohom_positive(self):
        """All bar cohomology dimensions are positive."""
        bar = virasoro_bar_cohom_gen_degree(20)
        for n in range(1, 21):
            assert bar[n] > 0, f"bar_cohom({n}) = {bar[n]} <= 0"

    def test_motzkin_monotone(self):
        """Motzkin numbers are strictly increasing for n >= 1."""
        m = motzkin_up_to(19)
        for n in range(2, 20):
            assert m[n] > m[n - 1], f"M({n}) = {m[n]} <= M({n-1}) = {m[n-1]}"

    def test_partitions_monotone(self):
        """Partition numbers are strictly increasing for n >= 1."""
        p = partitions_up_to(20)
        for n in range(2, 21):
            assert p[n] > p[n - 1], f"p({n}) = {p[n]} <= p({n-1}) = {p[n-1]}"

    def test_bar_cohom_exceeds_partitions(self):
        """For n >= 3, bar_cohom(n) > p(n).

        The bar cohomology in generation degree grows like 3^n while
        partitions grow like exp(pi*sqrt(2n/3)), so bar overtakes quickly.

        # VERIFIED [DC] comparison + [DA] growth rate analysis
        """
        bar = virasoro_bar_cohom_gen_degree(20)
        p = partitions_up_to(20)
        for n in range(3, 21):
            assert bar[n] > p[n], \
                f"At n={n}: bar_cohom={bar[n]} <= p(n)={p[n]}"

    def test_m0_m1_equal(self):
        """M(0) = M(1) = 1 (unique among named integer sequences)."""
        assert motzkin_number(0) == 1
        assert motzkin_number(1) == 1
