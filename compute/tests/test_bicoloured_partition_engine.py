r"""Tests for compute/lib/bicoloured_partition_engine.py -- bicoloured partitions and 1/eta^2.

Validates:
  1. Ordinary partition numbers p(n) against OEIS A000041
  2. Bicoloured partition numbers p_{-2}(n) against OEIS A000712
  3. Cross-check: convolution method vs product expansion method
  4. r-coloured generalisation at r=1 (ordinary) and r=2 (bicoloured)
  5. AP135 regression: coefficients are NOT triangular numbers

References:
  - OEIS A000041: https://oeis.org/A000041 (ordinary partitions)
  - OEIS A000712: https://oeis.org/A000712 (bicoloured partitions)
  - Andrews, "The Theory of Partitions" (1976)
  - CLAUDE.md C22, C23, AP135
"""

import pytest

from compute.lib.bicoloured_partition_engine import (
    partition_number,
    bicoloured_partition_number,
    bicoloured_from_product,
    bicoloured_partitions_table,
    r_coloured_partition_from_product,
    OEIS_A000712,
)


# ============================================================================
# Ordinary partition numbers (OEIS A000041)
# ============================================================================

class TestOrdinaryPartitions:
    """Validate partition_number against OEIS A000041."""

    # VERIFIED:
    # [LT] OEIS A000041: https://oeis.org/A000041
    # [DC] Euler pentagonal recurrence
    OEIS_A000041 = (
        1, 1, 2, 3, 5, 7, 11, 15, 22, 30,     # n=0..9
        42, 56, 77, 101, 135, 176, 231, 297,   # n=10..17
        385, 490, 627, 792, 1002, 1255, 1575,   # n=18..24
        1958, 2436, 3010, 3718, 4565, 5604,     # n=25..30
    )

    def test_partition_numbers_n0_to_30(self):
        """p(n) for n=0..30 matches OEIS A000041."""
        for n, expected in enumerate(self.OEIS_A000041):
            assert partition_number(n) == expected, (
                f"p({n}) = {partition_number(n)}, expected {expected}"
            )

    def test_partition_negative(self):
        """p(n) = 0 for n < 0."""
        for n in [-1, -5, -100]:
            assert partition_number(n) == 0

    def test_partition_base_cases(self):
        """p(0) = 1, p(1) = 1."""
        assert partition_number(0) == 1
        assert partition_number(1) == 1

    def test_partition_p5_equals_7(self):
        """p(5) = 7: {5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1}."""
        # VERIFIED:
        # [DC] Explicit enumeration of partitions of 5
        # [LT] OEIS A000041
        assert partition_number(5) == 7


# ============================================================================
# Bicoloured partition numbers (OEIS A000712)
# ============================================================================

class TestBicolouredPartitions:
    """Validate bicoloured partition numbers against OEIS A000712."""

    def test_bicoloured_n0_to_30_convolution(self):
        """p_{-2}(n) via convolution matches OEIS A000712 for n=0..30."""
        for n in range(31):
            computed = bicoloured_partition_number(n)
            expected = OEIS_A000712[n]
            assert computed == expected, (
                f"p_{{-2}}({n}) convolution = {computed}, expected {expected}"
            )

    def test_bicoloured_n0_to_30_product(self):
        """p_{-2}(n) via product expansion matches OEIS A000712 for n=0..30."""
        prod_coeffs = bicoloured_from_product(30)
        for n in range(31):
            assert prod_coeffs[n] == OEIS_A000712[n], (
                f"p_{{-2}}({n}) product = {prod_coeffs[n]}, expected {OEIS_A000712[n]}"
            )

    def test_convolution_equals_product(self):
        """Cross-check: convolution and product expansion agree for n=0..30."""
        prod_coeffs = bicoloured_from_product(30)
        for n in range(31):
            conv = bicoloured_partition_number(n)
            assert conv == prod_coeffs[n], (
                f"n={n}: convolution={conv}, product={prod_coeffs[n]}"
            )

    def test_bicoloured_partitions_table_consistency(self):
        """bicoloured_partitions_table performs internal cross-check."""
        # This function asserts internally that convolution == product
        table = bicoloured_partitions_table(30)
        assert len(table) == 31
        for n in range(31):
            assert table[n] == OEIS_A000712[n]

    def test_bicoloured_negative(self):
        """p_{-2}(n) = 0 for n < 0."""
        assert bicoloured_partition_number(-1) == 0
        assert bicoloured_partition_number(-10) == 0


# ============================================================================
# AP135 regression: NOT triangular numbers
# ============================================================================

class TestAP135Regression:
    """Verify that bicoloured partitions are NOT confused with triangular numbers.

    AP135: 1/eta^2 coefficients are bicoloured partitions (1,2,5,10,20,...),
    NOT triangular numbers (1,3,6,10,...). This confusion was a documented
    repeat offender across multiple waves.
    """

    TRIANGULAR = [n * (n + 1) // 2 for n in range(1, 32)]  # 1,3,6,10,15,...

    def test_not_triangular_at_n1(self):
        """p_{-2}(1) = 2, not T_1 = 1."""
        assert OEIS_A000712[1] == 2
        assert self.TRIANGULAR[0] == 1
        assert OEIS_A000712[1] != self.TRIANGULAR[0]

    def test_not_triangular_at_n2(self):
        """p_{-2}(2) = 5, not T_2 = 3."""
        assert OEIS_A000712[2] == 5
        assert self.TRIANGULAR[1] == 3
        assert OEIS_A000712[2] != self.TRIANGULAR[1]

    def test_not_triangular_at_n4(self):
        """p_{-2}(4) = 20, not T_4 = 10. Note p_{-2}(3)=10=T_4 is a coincidence."""
        assert OEIS_A000712[4] == 20
        assert self.TRIANGULAR[3] == 10
        assert OEIS_A000712[4] != self.TRIANGULAR[3]

    def test_first_10_differ_from_triangular(self):
        """At least 8 of the first 10 bicoloured numbers differ from triangular."""
        diffs = sum(
            1 for i in range(10)
            if OEIS_A000712[i] != self.TRIANGULAR[i]
        )
        assert diffs >= 8, f"Only {diffs} of first 10 differ from triangular"


# ============================================================================
# r-coloured partitions (generalisation)
# ============================================================================

class TestRColouredPartitions:
    """Validate the r-coloured generalisation."""

    def test_r1_equals_ordinary(self):
        """r=1 coloured partitions are ordinary partitions (OEIS A000041)."""
        r1 = r_coloured_partition_from_product(30, r=1)
        for n in range(31):
            assert r1[n] == partition_number(n), (
                f"r=1 at n={n}: {r1[n]} vs p({n})={partition_number(n)}"
            )

    def test_r2_equals_bicoloured(self):
        """r=2 coloured partitions are bicoloured partitions (OEIS A000712)."""
        r2 = r_coloured_partition_from_product(30, r=2)
        for n in range(31):
            assert r2[n] == OEIS_A000712[n], (
                f"r=2 at n={n}: {r2[n]} vs A000712={OEIS_A000712[n]}"
            )

    def test_r3_first_few(self):
        """r=3 coloured partitions: first few values (OEIS A000716).

        # VERIFIED:
        # [LT] OEIS A000716: 1, 3, 9, 22, 51, 108, 221, 429, ...
        # [DC] Product expansion prod 1/(1-q^n)^3
        """
        # OEIS A000716 first 8 terms
        expected_r3 = [1, 3, 9, 22, 51, 108, 221, 429]
        r3 = r_coloured_partition_from_product(7, r=3)
        for n, exp in enumerate(expected_r3):
            assert r3[n] == exp, f"r=3 at n={n}: {r3[n]} vs {exp}"


# ============================================================================
# Specific value checks with multiple verification paths
# ============================================================================

class TestSpecificValues:
    """Individual value checks with multi-path verification."""

    def test_p2_0_equals_1(self):
        """p_{-2}(0) = 1: the empty partition (unique).

        # VERIFIED:
        # [DC] Convolution: p(0)*p(0) = 1*1 = 1
        # [DC] Product: constant term of prod 1/(1-q^n)^2 = 1
        # [LT] OEIS A000712
        """
        assert bicoloured_partition_number(0) == 1

    def test_p2_1_equals_2(self):
        """p_{-2}(1) = 2: partition 1 in colour A or colour B.

        # VERIFIED:
        # [DC] Convolution: p(0)*p(1) + p(1)*p(0) = 1*1 + 1*1 = 2
        # [DC] Enumeration: {1_A, 1_B}
        # [LT] OEIS A000712
        """
        assert bicoloured_partition_number(1) == 2

    def test_p2_2_equals_5(self):
        """p_{-2}(2) = 5.

        # VERIFIED:
        # [DC] Convolution: p(0)*p(2) + p(1)*p(1) + p(2)*p(0) = 2 + 1 + 2 = 5
        # [DC] Enumeration: {2_A, 2_B, 1_A+1_A, 1_B+1_B, 1_A+1_B}
        # [LT] OEIS A000712
        """
        assert bicoloured_partition_number(2) == 5

    def test_p2_3_equals_10(self):
        """p_{-2}(3) = 10.

        # VERIFIED:
        # [DC] Convolution: p(0)*p(3)+p(1)*p(2)+p(2)*p(1)+p(3)*p(0) = 3+2+2+3 = 10
        # [LT] OEIS A000712
        # [SY] Coincides with T_4=10, but this is accidental (AP135)
        """
        assert bicoloured_partition_number(3) == 10

    def test_p2_5_equals_36(self):
        """p_{-2}(5) = 36.

        # VERIFIED:
        # [DC] Convolution: sum_{k=0}^{5} p(k)*p(5-k)
        #   = 1*7 + 1*5 + 2*3 + 3*2 + 5*1 + 7*1 = 7+5+6+6+5+7 = 36
        # [LT] OEIS A000712
        """
        assert bicoloured_partition_number(5) == 36

    def test_p2_10_equals_481(self):
        """p_{-2}(10) = 481.

        # VERIFIED:
        # [DC] Convolution of A000041 with itself at n=10
        # [DC] Product expansion
        # [LT] OEIS A000712
        """
        assert bicoloured_partition_number(10) == 481

    def test_p2_20_equals_24842(self):
        """p_{-2}(20) = 24842.

        # VERIFIED:
        # [DC] Convolution
        # [DC] Product expansion
        # [LT] OEIS A000712
        """
        assert bicoloured_partition_number(20) == 24842

    def test_p2_30_equals_595910(self):
        """p_{-2}(30) = 595910.

        # VERIFIED:
        # [DC] Convolution
        # [DC] Product expansion
        # [LT] OEIS A000712
        """
        assert bicoloured_partition_number(30) == 595910


# ============================================================================
# Generating function identity: p_{-2}(n) = sum p(k)*p(n-k)
# ============================================================================

class TestConvolutionIdentity:
    """Verify the Cauchy convolution identity directly."""

    def test_convolution_identity_n0_to_20(self):
        """p_{-2}(n) = sum_{k=0}^{n} p(k)*p(n-k) for n=0..20."""
        for n in range(21):
            conv_sum = sum(
                partition_number(k) * partition_number(n - k)
                for k in range(n + 1)
            )
            assert conv_sum == OEIS_A000712[n], (
                f"Convolution at n={n}: {conv_sum} vs {OEIS_A000712[n]}"
            )
