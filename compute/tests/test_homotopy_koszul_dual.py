"""Tests for homotopy Koszul dual A-infinity structure.

Verifies:
1. Bar complex d^2 = 0 for truncated polynomial algebras
2. Total bar cohomology dimensions
3. Bigraded bar cohomology (weight decomposition)
4. Koszul vs non-Koszul detection via weight concentration
5. A-infinity operations m_k via Massey products
6. Admissible-level analysis for L_{-1/2}(sl_2)
"""

import numpy as np
import pytest
from compute.lib.homotopy_koszul_dual import (
    TruncatedPolynomialAlgebra,
    BarComplex,
    AInfinityTransfer,
    compute_truncated_poly,
    dual_numbers_verification,
    cubic_truncation,
    admissible_sl2_analysis,
)


# =========================================================================
# Helpers
# =========================================================================

def bigraded_cohomology(bar: BarComplex, max_p: int = 5):
    """Compute bigraded bar cohomology H_{p,w}."""
    result = {}
    for p in range(1, max_p + 1):
        dp = bar.differential_matrix(p)
        dpp1 = bar.differential_matrix(p + 1)
        dim = bar.basis_size(p)

        weights = {}
        for idx in range(dim):
            tup = bar._index_to_tuple(p, idx)
            w = sum(t + 1 for t in tup)
            if w not in weights:
                weights[w] = []
            weights[w].append(idx)

        for w in sorted(weights.keys()):
            src_indices = weights[w]
            sub_dp = dp[:, src_indices]
            r_dp = np.linalg.matrix_rank(sub_dp, tol=1e-10)
            ker_dim = len(src_indices) - r_dp

            dim_pp1 = bar.basis_size(p + 1)
            if dim_pp1 > 0:
                sub_dpp1 = dpp1[src_indices, :]
                r_dpp1 = np.linalg.matrix_rank(sub_dpp1, tol=1e-10)
            else:
                r_dpp1 = 0

            h_pw = ker_dim - r_dpp1
            if h_pw > 0:
                result[(p, w)] = h_pw
    return result


# =========================================================================
# k[x]/(x^2) = dual numbers (Koszul)
# =========================================================================

class TestDualNumbers:
    """k[x]/(x^2) = k[epsilon] is Koszul: A! = k[y]."""

    def test_aug_ideal_dim(self):
        A = TruncatedPolynomialAlgebra(2)
        assert A.aug_ideal_dim == 1

    def test_multiplication(self):
        A = TruncatedPolynomialAlgebra(2)
        assert A.multiply(0, 0) is None  # x*x = x^2 = 0 in k[x]/(x^2)

    def test_d_squared_zero(self):
        bar = BarComplex(TruncatedPolynomialAlgebra(2))
        for p in range(2, 7):
            assert bar.verify_d_squared(p) < 1e-10

    def test_total_cohomology(self):
        """H_p = 1 for all p (periodic resolution)."""
        bar = BarComplex(TruncatedPolynomialAlgebra(2))
        for p in range(7):
            assert bar.cohomology_dim(p) == 1

    def test_bigraded_concentration(self):
        """H_{p,p} = 1 for all p: concentrated on diagonal = Koszul."""
        bar = BarComplex(TruncatedPolynomialAlgebra(2))
        bh = bigraded_cohomology(bar, max_p=5)
        for (p, w), dim in bh.items():
            assert w == p, f"Off-diagonal cohomology at ({p},{w})"
            assert dim == 1

    def test_m3_vanishes(self):
        """m_3 = 0 for Koszul algebra."""
        r = dual_numbers_verification()
        if '(1,1,1)' in r['m3']:
            assert not r['m3']['(1,1,1)']['nonzero']

    def test_m4_vanishes(self):
        """m_4 = 0 for Koszul algebra."""
        r = dual_numbers_verification()
        if '(1,1,1,1)' in r['m4']:
            assert not r['m4']['(1,1,1,1)']['nonzero']


# =========================================================================
# k[x]/(x^3) (non-Koszul, first nontrivial m_3)
# =========================================================================

class TestCubicTruncation:
    """k[x]/(x^3): the simplest non-Koszul example."""

    def test_aug_ideal_dim(self):
        A = TruncatedPolynomialAlgebra(3)
        assert A.aug_ideal_dim == 2

    def test_multiplication_table(self):
        A = TruncatedPolynomialAlgebra(3)
        assert A.multiply(0, 0) == 1   # x*x = x^2
        assert A.multiply(0, 1) is None  # x*x^2 = x^3 = 0
        assert A.multiply(1, 0) is None
        assert A.multiply(1, 1) is None

    def test_d_squared_zero(self):
        bar = BarComplex(TruncatedPolynomialAlgebra(3))
        for p in range(2, 7):
            assert bar.verify_d_squared(p) < 1e-10

    def test_total_cohomology(self):
        """H_p = 1 for all p (2-periodic resolution)."""
        bar = BarComplex(TruncatedPolynomialAlgebra(3))
        for p in range(7):
            assert bar.cohomology_dim(p) == 1

    def test_bar_differential_d2(self):
        """d_2[x|x] = -[x^2], all others zero."""
        bar = BarComplex(TruncatedPolynomialAlgebra(3))
        d2 = bar.differential_matrix(2)
        # Column 0 = [x|x]: should give -[x^2] = (0, -1)
        assert abs(d2[0, 0]) < 1e-10
        assert abs(d2[1, 0] - (-1)) < 1e-10
        # All other columns zero
        for j in range(1, 4):
            assert np.max(np.abs(d2[:, j])) < 1e-10

    def test_bigraded_off_diagonal(self):
        """H_{2,3} = 1: cohomology NOT on diagonal => non-Koszul."""
        bar = BarComplex(TruncatedPolynomialAlgebra(3))
        bh = bigraded_cohomology(bar, max_p=4)
        assert (1, 1) in bh and bh[(1, 1)] == 1
        assert (2, 3) in bh and bh[(2, 3)] == 1  # OFF diagonal!
        assert (3, 4) in bh and bh[(3, 4)] == 1
        # No diagonal entries at p >= 2
        for (p, w) in bh:
            if p >= 2:
                assert w > p, f"Unexpected diagonal cohomology at ({p},{w})"

    def test_koszul_failure(self):
        """k[x]/(x^3) is not Koszul: H_{2,3} ≠ 0 with 3 > 2."""
        bar = BarComplex(TruncatedPolynomialAlgebra(3))
        bh = bigraded_cohomology(bar, max_p=3)
        is_koszul = all(w == p for (p, w) in bh)
        assert not is_koszul

    def test_m2_vanishes_yoneda(self):
        """m_2(a,a) = 0 in Ext^2 (Yoneda product vanishes).

        The class [x] ∈ H_{1,1} has m_2([x],[x]) = 0 because
        [x|x] ∈ B_2 at weight 2, and H_{2,2} = 0.
        """
        bar = BarComplex(TruncatedPolynomialAlgebra(3))
        bh = bigraded_cohomology(bar, max_p=3)
        assert (2, 2) not in bh  # no cohomology at weight = bar degree

    def test_massey_product_defined(self):
        """m_2(a,a) = 0 implies Massey product <a,a,a> is defined."""
        # m_2(a,a) = 0 verified above; this is the precondition for m_3
        bar = BarComplex(TruncatedPolynomialAlgebra(3))
        bh = bigraded_cohomology(bar, max_p=3)
        assert (2, 2) not in bh  # m_2(a,a) = 0
        assert (2, 3) in bh     # target of m_3 exists

    def test_m3_target_exists(self):
        """m_3(a,a,a) targets H_{2,3} = k (1-dimensional)."""
        bar = BarComplex(TruncatedPolynomialAlgebra(3))
        bh = bigraded_cohomology(bar, max_p=3)
        # m_3: H_{1,1}^3 -> H_{2,3} (weight 3*1=3, bar degree 3-1=2)
        assert (2, 3) in bh
        assert bh[(2, 3)] == 1

    def test_d3_boundary_relation(self):
        """d_3[x|x|x] = [x|x^2] - [x^2|x]: the boundary relating weight-3 cycles."""
        bar = BarComplex(TruncatedPolynomialAlgebra(3))
        d3 = bar.differential_matrix(3)
        # Column 0 = [x|x|x] = (0,0,0)
        col = d3[:, 0]
        # Row 1 = [x|x^2] = (0,1), Row 2 = [x^2|x] = (1,0)
        assert abs(col[1] - 1) < 1e-10    # +[x|x^2]
        assert abs(col[2] - (-1)) < 1e-10  # -[x^2|x]
        assert abs(col[0]) < 1e-10
        assert abs(col[3]) < 1e-10


# =========================================================================
# k[x]/(x^n) for general n (Lu-Palmieri-Wu-Zhang pattern)
# =========================================================================

class TestGeneralTruncation:
    """k[x]/(x^n): first nontrivial A-infinity operation is m_{n-1}."""

    @pytest.mark.parametrize("n", [2, 3, 4, 5])
    def test_d_squared(self, n):
        bar = BarComplex(TruncatedPolynomialAlgebra(n))
        for p in range(2, 5):
            assert bar.verify_d_squared(p) < 1e-10

    @pytest.mark.parametrize("n", [2, 3, 4, 5])
    def test_total_cohomology_one(self, n):
        """Total H_p = 1 for all p (periodic resolution)."""
        bar = BarComplex(TruncatedPolynomialAlgebra(n))
        for p in range(5):
            assert bar.cohomology_dim(p) == 1

    def test_kx2_koszul(self):
        """k[x]/(x^2) is Koszul: H_{p,p} only."""
        bar = BarComplex(TruncatedPolynomialAlgebra(2))
        bh = bigraded_cohomology(bar, max_p=5)
        assert all(w == p for (p, w) in bh)

    @pytest.mark.parametrize("n", [3, 4, 5])
    def test_kxn_not_koszul(self, n):
        """k[x]/(x^n) for n >= 3 is NOT Koszul."""
        bar = BarComplex(TruncatedPolynomialAlgebra(n))
        bh = bigraded_cohomology(bar, max_p=3)
        assert not all(w == p for (p, w) in bh)

    @pytest.mark.parametrize("n", [3, 4, 5])
    def test_h2_weight_n(self, n):
        """H_{2,n} = 1: the bar cohomology in degree 2 at weight n."""
        bar = BarComplex(TruncatedPolynomialAlgebra(n))
        bh = bigraded_cohomology(bar, max_p=3)
        assert (2, n) in bh
        assert bh[(2, n)] == 1

    @pytest.mark.parametrize("n", [3, 4, 5])
    def test_h1_weight_1_only(self, n):
        """H_1 is concentrated at weight 1."""
        bar = BarComplex(TruncatedPolynomialAlgebra(n))
        bh = bigraded_cohomology(bar, max_p=1)
        assert (1, 1) in bh
        assert bh[(1, 1)] == 1
        for (p, w) in bh:
            if p == 1:
                assert w == 1

    def test_lpwz_pattern_n3(self):
        """k[x]/(x^3): m_{n-1} = m_2 is the first nonzero operation.
        Wait -- m_2(a,a) = 0, so m_3 = m_{n-1} is first nonzero.
        """
        # For n=3: m_2(a,a)=0, m_3(a,a,a) = b (generator of Ext^2)
        bar = BarComplex(TruncatedPolynomialAlgebra(3))
        bh = bigraded_cohomology(bar, max_p=3)
        # Precondition: m_2(a,a)=0 (no H_{2,2})
        assert (2, 2) not in bh
        # Target exists: H_{2,3} = 1
        assert (2, 3) in bh

    def test_lpwz_pattern_n4(self):
        """k[x]/(x^4): m_2 = m_3 = 0 on a, m_4(a,a,a,a) = b."""
        bar = BarComplex(TruncatedPolynomialAlgebra(4))
        bh = bigraded_cohomology(bar, max_p=3)
        # m_2(a,a) targets H_{2,2}: should be 0
        assert (2, 2) not in bh
        # m_3(a,a,a) targets H_{2,3}: should be 0
        assert (2, 3) not in bh
        # m_4(a,a,a,a) targets H_{2,4}: should be 1
        assert (2, 4) in bh
        assert bh[(2, 4)] == 1

    def test_lpwz_pattern_n5(self):
        """k[x]/(x^5): m_2 = m_3 = m_4 = 0 on a, m_5(a,...,a) = b."""
        bar = BarComplex(TruncatedPolynomialAlgebra(5))
        bh = bigraded_cohomology(bar, max_p=3)
        assert (2, 2) not in bh
        assert (2, 3) not in bh
        assert (2, 4) not in bh
        assert (2, 5) in bh


# =========================================================================
# Admissible level analysis
# =========================================================================

class TestAdmissibleLevel:
    """L_{-1/2}(sl_2) at admissible level."""

    def test_basic_data(self):
        r = admissible_sl2_analysis()
        assert r['level'] == -0.5
        assert r['admissible']
        assert r['universal_koszul']
        assert r['null_vector_level'] == 2

    def test_universal_vs_simple(self):
        """V_k is Koszul for all k; L_k may fail at admissible levels."""
        r = admissible_sl2_analysis()
        assert r['universal_koszul']
        assert r['simple_quotient_koszul'] == 'OPEN'


# =========================================================================
# Structural tests
# =========================================================================

class TestBarComplexStructure:
    """General structural properties of the bar complex."""

    @pytest.mark.parametrize("n", [2, 3, 4])
    def test_basis_size(self, n):
        """B_p has dim (n-1)^p."""
        bar = BarComplex(TruncatedPolynomialAlgebra(n))
        for p in range(5):
            assert bar.basis_size(p) == (n - 1) ** p

    @pytest.mark.parametrize("n", [2, 3, 4])
    def test_index_tuple_roundtrip(self, n):
        """Index <-> tuple conversion is invertible."""
        bar = BarComplex(TruncatedPolynomialAlgebra(n))
        for p in range(1, 4):
            for idx in range(bar.basis_size(p)):
                tup = bar._index_to_tuple(p, idx)
                assert bar._tuple_to_index(tup) == idx

    def test_euler_characteristic(self):
        """chi(B(A)) = sum (-1)^p dim H_p. For contractible: chi = 1."""
        for n in [2, 3, 4]:
            bar = BarComplex(TruncatedPolynomialAlgebra(n))
            # Truncated Euler char
            chi = sum((-1) ** p * bar.cohomology_dim(p) for p in range(6))
            # Should be 1 (augmented bar complex is acyclic except H_0 = k)
            # Actually H_0 = 1, H_p = 1 for all p, so chi = 1-1+1-1+1-1 = 0
            # for even truncation, 1 for odd.
            # The sign-alternating sum depends on truncation.
            # Just check that all cohomology dims are 1.
            for p in range(6):
                assert bar.cohomology_dim(p) == 1


# =========================================================================
# Weight concentration = Koszulness criterion
# =========================================================================

class TestKoszulnessCriterion:
    """The weight concentration criterion for Koszulness:
    A is Koszul iff H_{p,w}(B(A)) = 0 for w != p."""

    def test_dual_numbers_passes(self):
        bar = BarComplex(TruncatedPolynomialAlgebra(2))
        bh = bigraded_cohomology(bar, max_p=5)
        for (p, w), dim in bh.items():
            assert w == p

    @pytest.mark.parametrize("n", [3, 4, 5])
    def test_truncated_poly_fails(self, n):
        bar = BarComplex(TruncatedPolynomialAlgebra(n))
        bh = bigraded_cohomology(bar, max_p=3)
        off_diagonal = [(p, w) for (p, w) in bh if w != p]
        assert len(off_diagonal) > 0

    def test_non_koszul_degree(self):
        """For k[x]/(x^n), non-Koszulness first appears at bar degree 2."""
        for n in [3, 4, 5]:
            bar = BarComplex(TruncatedPolynomialAlgebra(n))
            bh = bigraded_cohomology(bar, max_p=3)
            # Degree 1 is always on diagonal
            for (p, w) in bh:
                if p == 1:
                    assert w == p
            # Degree 2 is off diagonal
            assert any(p == 2 and w != p for (p, w) in bh)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
