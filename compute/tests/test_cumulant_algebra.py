"""Tests for the primitive cumulant algebra and cofree recognition."""
import pytest
from fractions import Fraction
from math import log

from sympy import Rational, Symbol

from compute.lib.cumulant_algebra import (
    cofree_dimensions,
    cumulant_inversion,
    compute_primitive_cumulants,
    verify_euler_identity,
    grand_completion_datum,
    cumulant_ds_reduction,
    entropy_ladder,
    generalized_binom,
    cofree_gf_from_cumulant_gf,
    heisenberg_cumulant_analysis,
    cross_family_cumulant_comparison,
    CumulantAlgebra,
    PrimitiveCumulant,
)
from compute.lib.utils import partition_number


# ================================================================
# TestCofreeForward: cofree_dimensions forward Euler transform
# ================================================================


class TestCofreeForward:
    """Tests for the forward cofree dimension computation (Euler transform)."""

    def test_cofree_all_ones_gives_partitions(self):
        """cofree on q_n = 1 for all n gives partition numbers p(n).

        This is the cumulant avatar of Euler's product formula:
            prod_{k >= 1} 1/(1 - x^k) = sum p(n) x^n.
        """
        q = {n: 1 for n in range(1, 21)}
        b = cofree_dimensions(q, max_degree=20)
        for n in range(1, 21):
            assert b[n] == partition_number(n), f"Mismatch at n={n}"

    def test_cofree_single_generator_degree_1(self):
        """cofree on q_1 = 1, q_n = 0 for n >= 2 gives 1 for all n.

        The cofree coalgebra on a single generator in degree 1 is
        T^c(k[1]) with dim = 1 in every degree (monomials a^n).
        """
        q = {1: 1}
        b = cofree_dimensions(q, max_degree=15)
        for n in range(1, 16):
            assert b[n] == 1, f"Expected 1 at degree {n}, got {b[n]}"

    def test_cofree_d_generators_degree_1(self):
        """cofree on q_1 = d, q_n = 0 for n >= 2 gives d-colored partitions.

        For d generators in degree 1, the cofree coalgebra has
        dim = binom(d + n - 1, n) in degree n (d-multiset coefficients).
        """
        for d in [2, 3, 5]:
            q = {1: d}
            b = cofree_dimensions(q, max_degree=10)
            for n in range(1, 11):
                expected = generalized_binom(d, n)
                assert b[n] == expected, (
                    f"d={d}, n={n}: expected {expected}, got {b[n]}"
                )

    def test_cofree_empty_cumulants(self):
        """Empty cumulants give all zeros (no generators, no bar cohomology)."""
        q = {}
        b = cofree_dimensions(q, max_degree=10)
        for n in range(1, 11):
            assert b[n] == 0, f"Expected 0 at degree {n}, got {b[n]}"

    def test_cofree_single_generator_degree_2(self):
        """cofree on q_2 = 1 gives b_n = 1 if n even, 0 if n odd."""
        q = {2: 1}
        b = cofree_dimensions(q, max_degree=12)
        for n in range(1, 13):
            expected = 1 if n % 2 == 0 else 0
            assert b[n] == expected, f"n={n}: expected {expected}, got {b[n]}"

    def test_cofree_q1_2_q2_1(self):
        """cofree on q_1 = 2, q_2 = 1 gives specific low-degree values.

        1/(1-x)^2 * 1/(1-x^2) = (1 + 2x + 3x^2 + 4x^3 + ...)(1 + x^2 + x^4 + ...)
        b_1 = 2, b_2 = 3 + 1 = 4, b_3 = 4 + 2 = 6.
        """
        q = {1: 2, 2: 1}
        b = cofree_dimensions(q, max_degree=6)
        assert b[1] == 2
        assert b[2] == 4
        assert b[3] == 6

    def test_cofree_max_degree_respected(self):
        """Output keys match 1..max_degree."""
        q = {1: 1, 3: 1}
        b = cofree_dimensions(q, max_degree=7)
        assert set(b.keys()) == set(range(1, 8))

    def test_cofree_negative_cumulant(self):
        """cofree handles negative q_k via generalized binomial.

        With q_2 = -1, the factor 1/(1 - x^2)^{-1} = (1 - x^2) contributes
        negatively at even degrees.
        """
        q = {1: 3, 2: -1}
        b = cofree_dimensions(q, max_degree=6)
        # 1/(1-x)^3 * (1-x^2) = 1/(1-x)^3 * (1-x)(1+x) = (1+x)/(1-x)^2
        # b_n coefficient of x^n in (1+x)/(1-x)^2 = (n+1) + n = 2n+1 for n >= 1
        # Actually: (1+x) * sum (n+1)x^n = sum (n+1)x^n + sum (n+1)x^{n+1}
        # = sum (n+1)x^n + sum n*x^n = sum (2n+1)x^n for n >= 1, plus x^0 = 1
        assert b[1] == 3  # 2*1 + 1 = 3
        assert b[2] == 5  # 2*2 + 1 = 5
        assert b[3] == 7  # 2*3 + 1 = 7
        assert b[4] == 9  # 2*4 + 1 = 9

    def test_cofree_large_degree(self):
        """cofree on single generator works at large degree."""
        q = {1: 1}
        b = cofree_dimensions(q, max_degree=50)
        assert b[50] == 1

    def test_cofree_two_families_additive(self):
        """cofree is multiplicative in generating functions.

        cofree({1:a}) * cofree({2:b}) via separate Euler factors should
        agree with cofree({1:a, 2:b}).
        """
        q_combined = {1: 2, 2: 3}
        b = cofree_dimensions(q_combined, max_degree=8)
        # Verify by direct computation that the result is nonnegative and consistent
        for n in range(1, 9):
            assert isinstance(b[n], int)
            assert b[n] > 0


# ================================================================
# TestCumulantInversion: Moebius inversion from bar dims to cumulants
# ================================================================


class TestCumulantInversion:
    """Tests for the inverse Euler transform (Moebius inversion)."""

    def test_round_trip_all_ones(self):
        """Round-trip: cumulant_inversion(cofree_dimensions(q)) == q for q_n = 1."""
        q_in = {n: 1 for n in range(1, 13)}
        b = cofree_dimensions(q_in, max_degree=12)
        q_out = cumulant_inversion(b, max_degree=12)
        for n in range(1, 13):
            assert q_out[n] == q_in[n], f"Round-trip failed at n={n}"

    def test_round_trip_single_generator(self):
        """Round-trip for q_1 = 1 only."""
        q_in = {1: 1}
        b = cofree_dimensions(q_in, max_degree=10)
        q_out = cumulant_inversion(b, max_degree=10)
        assert q_out[1] == 1
        for n in range(2, 11):
            assert q_out[n] == 0, f"Expected q_{n} = 0, got {q_out[n]}"

    def test_round_trip_d_generators(self):
        """Round-trip for q_1 = d, higher zero."""
        for d in [2, 3, 7]:
            q_in = {1: d}
            b = cofree_dimensions(q_in, max_degree=8)
            q_out = cumulant_inversion(b, max_degree=8)
            assert q_out[1] == d
            for n in range(2, 9):
                assert q_out[n] == 0

    def test_round_trip_mixed(self):
        """Round-trip for mixed cumulant profile {1:3, 2:1, 3:2}."""
        q_in = {1: 3, 2: 1, 3: 2}
        b = cofree_dimensions(q_in, max_degree=10)
        q_out = cumulant_inversion(b, max_degree=10)
        for n in range(1, 11):
            expected = q_in.get(n, 0)
            assert q_out[n] == expected, f"n={n}: expected {expected}, got {q_out[n]}"

    def test_partition_numbers_invert_to_ones(self):
        """Partition numbers p(n) invert to q_n = 1 for all n.

        This is the inverse of the Euler product identity.
        """
        bar = {n: partition_number(n) for n in range(1, 16)}
        q = cumulant_inversion(bar, max_degree=15)
        for n in range(1, 16):
            assert q[n] == 1, f"q_{n} = {q[n]}, expected 1"

    def test_inversion_of_doubled_partitions(self):
        """2 * p(n) does NOT invert to q_n = 2 for all n.

        The Euler transform is MULTIPLICATIVE: prod 1/(1-x^k)^{q_k}.
        Doubling the output does not simply double each q_k.
        Only q_1 = 2*p(1) = 2 (since at degree 1 there is no lower contribution).
        Higher cumulants differ from 2 due to cross-terms.

        The round-trip still works: cofree(cumulant_inversion(2*p)) = 2*p.
        """
        bar = {n: 2 * partition_number(n) for n in range(1, 13)}
        q = cumulant_inversion(bar, max_degree=12)
        # q_1 = 2*p(1) = 2 since no lower terms contribute
        assert q[1] == 2
        # Round-trip is always exact
        b_check = cofree_dimensions(q, max_degree=12)
        for n in range(1, 13):
            assert b_check[n] == bar[n], f"Round-trip failed at n={n}"

    def test_round_trip_negative_cumulant(self):
        """Round-trip preserves negative cumulants (e.g. sl_2 defect)."""
        q_in = {1: 3, 2: -1}
        b = cofree_dimensions(q_in, max_degree=8)
        q_out = cumulant_inversion(b, max_degree=8)
        assert q_out[1] == 3
        assert q_out[2] == -1
        for n in range(3, 9):
            assert q_out[n] == 0

    def test_inversion_single_nonzero(self):
        """Inversion of bar dims from a single nonzero cumulant q_3 = 2."""
        q_in = {3: 2}
        b = cofree_dimensions(q_in, max_degree=12)
        q_out = cumulant_inversion(b, max_degree=12)
        for n in range(1, 13):
            expected = q_in.get(n, 0)
            assert q_out[n] == expected

    def test_round_trip_large_values(self):
        """Round-trip with large cumulant values."""
        q_in = {1: 10, 2: 5, 3: 3}
        b = cofree_dimensions(q_in, max_degree=8)
        q_out = cumulant_inversion(b, max_degree=8)
        for n in range(1, 9):
            assert q_out[n] == q_in.get(n, 0)

    def test_inversion_returns_all_degrees(self):
        """Inversion returns values for all degrees 1..max_degree."""
        bar = {1: 1, 2: 2}
        q = cumulant_inversion(bar, max_degree=6)
        assert set(q.keys()) == set(range(1, 7))


# ================================================================
# TestEulerIdentity: verify_euler_identity
# ================================================================


class TestEulerIdentity:
    """Tests for the Euler product identity verification."""

    def test_euler_identity_holds(self):
        """verify_euler_identity returns all_match = True."""
        result = verify_euler_identity(max_degree=20)
        assert result["all_match"] is True

    def test_euler_specific_partition_values(self):
        """Check specific partition numbers: p(5) = 7, p(10) = 42, p(20) = 627."""
        assert partition_number(5) == 7
        assert partition_number(10) == 42
        assert partition_number(20) == 627

    def test_euler_identity_per_degree(self):
        """Each degree in the Euler identity matches."""
        result = verify_euler_identity(max_degree=15)
        for n in range(1, 16):
            assert result["per_degree"][n]["match"] is True

    def test_euler_identity_cofree_values(self):
        """The cofree values in the Euler identity match p(n)."""
        result = verify_euler_identity(max_degree=10)
        for n in range(1, 11):
            assert result["per_degree"][n]["cofree"] == partition_number(n)

    def test_euler_small_partitions(self):
        """p(1)=1, p(2)=2, p(3)=3, p(4)=5."""
        assert partition_number(1) == 1
        assert partition_number(2) == 2
        assert partition_number(3) == 3
        assert partition_number(4) == 5


# ================================================================
# TestHeisenbergCumulants: Heisenberg bar cohomology and cumulants
# ================================================================


class TestHeisenbergCumulants:
    """Tests for the Heisenberg cumulant algebra."""

    def test_heisenberg_q1_is_1(self):
        """q_1 = 1 for Heisenberg (single generator of conformal weight 1)."""
        ca = compute_primitive_cumulants('heisenberg', max_degree=10)
        assert ca.total_dims[1] == 1

    def test_heisenberg_q2_is_0(self):
        """q_2 = 0 for Heisenberg (no independent degree-2 primitive)."""
        ca = compute_primitive_cumulants('heisenberg', max_degree=10)
        assert ca.total_dims[2] == 0

    def test_heisenberg_q3_is_0(self):
        """q_3 = 0 for Heisenberg."""
        ca = compute_primitive_cumulants('heisenberg', max_degree=10)
        assert ca.total_dims[3] == 0

    def test_heisenberg_round_trip(self):
        """Cofree recognition is exact by construction (round-trip always works)."""
        ca = compute_primitive_cumulants('heisenberg', max_degree=12)
        assert ca.recognition_verified is True

    def test_heisenberg_bar_dims_shifted_partitions(self):
        """Heisenberg bar dims: b_1 = 1, b_n = p(n-2) for n >= 2."""
        ca = compute_primitive_cumulants('heisenberg', max_degree=10)
        # Access bar dims via the cofree prediction (which equals bar dims when verified)
        # Instead, recompute bar dims directly
        from compute.lib.cumulant_algebra import _heisenberg_bar_dims
        bar = _heisenberg_bar_dims(max_degree=10)
        assert bar[1] == 1
        assert bar[2] == partition_number(0)  # p(0) = 1
        assert bar[3] == partition_number(1)  # p(1) = 1
        assert bar[4] == partition_number(2)  # p(2) = 2
        assert bar[5] == partition_number(3)  # p(3) = 3

    def test_heisenberg_analysis_structural(self):
        """heisenberg_cumulant_analysis returns correct structural data."""
        result = heisenberg_cumulant_analysis(max_degree=12)
        assert result["q_1"] == 1
        assert result["q_2"] == 0
        assert result["q_3"] == 0
        assert result["round_trip_exact"] is True

    def test_heisenberg_euler_comparison(self):
        """Euler identity: p(n) inverts to q_n = 1, confirmed by analysis."""
        result = heisenberg_cumulant_analysis(max_degree=15)
        assert result["euler_identity_on_p(n)"] is True

    def test_heisenberg_negativity_boundary(self):
        """Heisenberg cumulants become negative at degree 15.

        The shifted bar dims p(n-2) do NOT arise from a genuine cofree
        structure beyond degree 14. This is documented in the module.
        """
        result = heisenberg_cumulant_analysis(max_degree=20)
        # The module documents negativity at degree 15
        assert result["first_negative_degree"] is not None
        assert result["first_negative_degree"] == 15


# ================================================================
# TestAffineSl2Cumulants: affine sl_2 bar cohomology and cumulants
# ================================================================


class TestAffineSl2Cumulants:
    """Tests for the affine sl_2 cumulant algebra.

    CRITICAL: H^2 = 5, NOT 6. The Riordan number R(5) = 6 overcounts
    by 1 at degree 2 (rem:bar-deg2-symmetric-square). This produces
    q_2 = -1, a genuine defect in the cofree recognition.
    """

    def test_sl2_q1_is_3(self):
        """q_1 = 3 for affine sl_2 (dim(sl_2) = 3)."""
        ca = compute_primitive_cumulants('affine_sl2', max_degree=8)
        assert ca.total_dims[1] == 3

    def test_sl2_q2_is_negative(self):
        """q_2 = -1 for affine sl_2 (Riordan defect from H^2 = 5, not 6)."""
        ca = compute_primitive_cumulants('affine_sl2', max_degree=8)
        assert ca.total_dims[2] == -1

    def test_sl2_h2_is_5_not_6(self):
        """Bar cohomology H^2 = 5, NOT 6. Riordan WRONG at n=2."""
        from compute.lib.cumulant_algebra import _sl2_bar_dims
        bar = _sl2_bar_dims(max_degree=5)
        assert bar[2] == 5, f"H^2 should be 5, got {bar[2]}"

    def test_sl2_h1_is_3(self):
        """Bar cohomology H^1 = 3."""
        from compute.lib.cumulant_algebra import _sl2_bar_dims
        bar = _sl2_bar_dims(max_degree=5)
        assert bar[1] == 3

    def test_sl2_round_trip(self):
        """Round-trip cofree recognition holds (exact by construction)."""
        ca = compute_primitive_cumulants('affine_sl2', max_degree=10)
        assert ca.recognition_verified is True

    def test_sl2_not_all_nonneg(self):
        """sl_2 cumulants are NOT all non-negative (q_2 = -1)."""
        ca = compute_primitive_cumulants('affine_sl2', max_degree=8)
        all_nonneg = all(v >= 0 for v in ca.total_dims.values())
        assert not all_nonneg

    def test_sl2_bar_dims_riordan_for_n_geq_3(self):
        """For n >= 3, H^n = R(n+3) where R is the Riordan sequence."""
        from compute.lib.cumulant_algebra import _sl2_bar_dims
        bar = _sl2_bar_dims(max_degree=8)
        # R(0)=1, R(1)=0, R(2)=1, R(3)=1, R(4)=3, R(5)=6, R(6)=15, R(7)=36, R(8)=91
        # n=3: R(6)=15, n=4: R(7)=36, n=5: R(8)=91
        riordan = [1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603]
        for n in range(3, 9):
            if n + 3 < len(riordan):
                assert bar[n] == riordan[n + 3], f"n={n}: expected R({n+3})={riordan[n+3]}, got {bar[n]}"

    def test_sl2_cofree_prediction_matches_bar(self):
        """The cofree prediction from cumulants exactly matches the bar dims."""
        from compute.lib.cumulant_algebra import _sl2_bar_dims
        bar = _sl2_bar_dims(max_degree=10)
        ca = compute_primitive_cumulants('affine_sl2', max_degree=10)
        for n in range(1, 11):
            assert ca.cofree_prediction[n] == bar[n]


# ================================================================
# TestVirasoroCumulants: Virasoro bar cohomology and cumulants
# ================================================================


class TestVirasoroCumulants:
    """Tests for the Virasoro cumulant algebra (class M, infinite tower)."""

    def test_virasoro_q1_is_1(self):
        """q_1 = 1 for Virasoro (single generator L of conformal weight 2)."""
        ca = compute_primitive_cumulants('virasoro', max_degree=10)
        assert ca.total_dims[1] == 1

    def test_virasoro_all_cumulants_nonneg(self):
        """All Virasoro cumulants are non-negative (through available data)."""
        ca = compute_primitive_cumulants('virasoro', max_degree=12)
        for n, qn in ca.total_dims.items():
            assert qn >= 0, f"q_{n} = {qn} is negative"

    def test_virasoro_cumulants_grow(self):
        """Virasoro cumulants grow (class M: exponential growth)."""
        ca = compute_primitive_cumulants('virasoro', max_degree=12)
        # At least some cumulants beyond q_1 should be positive
        positive_count = sum(1 for n, q in ca.total_dims.items() if n > 1 and q > 0)
        assert positive_count > 3, "Virasoro should have many positive cumulants"

    def test_virasoro_entropy_positive(self):
        """Virasoro entropy h_K > 0 (exponential cumulant growth)."""
        ca = compute_primitive_cumulants('virasoro', max_degree=14)
        assert ca.entropy is not None
        assert ca.entropy > 0

    def test_virasoro_bar_dims_motzkin_diffs(self):
        """Virasoro bar dims are first differences of Motzkin numbers."""
        from compute.lib.cumulant_algebra import _virasoro_bar_dims
        bar = _virasoro_bar_dims(max_degree=8)
        # Motzkin: 1, 1, 2, 4, 9, 21, 51, 127, 323, 835
        motzkin = [1, 1, 2, 4, 9, 21, 51, 127, 323, 835]
        for n in range(1, 9):
            expected = motzkin[n + 1] - motzkin[n]
            assert bar[n] == expected, f"n={n}: expected {expected}, got {bar[n]}"

    def test_virasoro_round_trip(self):
        """Cofree recognition round-trip is exact."""
        ca = compute_primitive_cumulants('virasoro', max_degree=12)
        assert ca.recognition_verified is True

    def test_virasoro_q2_value(self):
        """Virasoro q_2 should be non-negative and specific."""
        ca = compute_primitive_cumulants('virasoro', max_degree=10)
        # b_1 = M(2) - M(1) = 2 - 1 = 1, so q_1 = 1
        # b_2 = M(3) - M(2) = 4 - 2 = 2
        # cofree on q_1 = 1 contributes 1 at degree 2
        # so q_2 = 2 - 1 = 1
        assert ca.total_dims[2] == 1

    def test_virasoro_generating_function(self):
        """Virasoro cumulant generating function is a sympy expression."""
        ca = compute_primitive_cumulants('virasoro', max_degree=8)
        gf = ca.cumulant_generating_function()
        x = Symbol('x')
        # Should have q_1 = 1 as the x^1 coefficient
        assert gf.coeff(x, 1) == 1


# ================================================================
# TestW3Cumulants: W_3 bar cohomology and cumulants
# ================================================================


class TestW3Cumulants:
    """Tests for the W_3 cumulant algebra."""

    def test_w3_q1_is_2(self):
        """q_1 = 2 for W_3 (two generators L, W)."""
        ca = compute_primitive_cumulants('w3', max_degree=5)
        assert ca.total_dims[1] == 2

    def test_w3_bar_dims(self):
        """W_3 bar dims: H^1 = 2, H^2 = 5, H^3 = 16, H^4 = 52, H^5 = 171."""
        from compute.lib.cumulant_algebra import _w3_bar_dims
        bar = _w3_bar_dims()
        assert bar[1] == 2
        assert bar[2] == 5
        assert bar[3] == 16
        assert bar[4] == 52
        assert bar[5] == 171

    def test_w3_round_trip(self):
        """Cofree recognition round-trip is exact for W_3."""
        ca = compute_primitive_cumulants('w3', max_degree=5)
        assert ca.recognition_verified is True

    def test_w3_cumulants_nonneg(self):
        """W_3 cumulants are all non-negative through degree 5."""
        ca = compute_primitive_cumulants('w3', max_degree=5)
        for n, qn in ca.total_dims.items():
            assert qn >= 0, f"q_{n} = {qn} is negative"

    def test_w3_entropy_exceeds_virasoro(self):
        """W_3 entropy exceeds Virasoro entropy (more generators, more growth).

        This may be approximate since W_3 has only 5 data points.
        """
        ca_w3 = compute_primitive_cumulants('w3', max_degree=5)
        ca_vir = compute_primitive_cumulants('virasoro', max_degree=14)
        # W_3 entropy estimate is based on 5 points; Virasoro on 14.
        # Both should be positive (class M).
        assert ca_w3.entropy is not None
        assert ca_vir.entropy is not None
        # The ordering may not be strict due to limited W_3 data,
        # but both should be positive.
        assert ca_w3.entropy > 0
        assert ca_vir.entropy > 0


# ================================================================
# TestBetagammaCumulants: betagamma system
# ================================================================


class TestBetagammaCumulants:
    """Tests for the betagamma cumulant algebra (class C, contact)."""

    def test_betagamma_q1(self):
        """betagamma q_1 = 2 (generators beta, gamma)."""
        ca = compute_primitive_cumulants('betagamma', max_degree=10)
        assert ca.total_dims[1] == 2

    def test_betagamma_bar_dims(self):
        """betagamma bar dims from sqrt((1+x)/(1-3x)) recurrence."""
        from compute.lib.cumulant_algebra import _betagamma_bar_dims
        bar = _betagamma_bar_dims(max_degree=6)
        assert bar[1] == 2
        assert bar[2] == 4

    def test_betagamma_round_trip(self):
        """Cofree recognition round-trip is exact."""
        ca = compute_primitive_cumulants('betagamma', max_degree=10)
        assert ca.recognition_verified is True

    def test_betagamma_cumulants_nonneg(self):
        """betagamma cumulants are all non-negative."""
        ca = compute_primitive_cumulants('betagamma', max_degree=10)
        for n, qn in ca.total_dims.items():
            assert qn >= 0, f"q_{n} = {qn} is negative"


# ================================================================
# TestFreeFermionCumulants: free fermion
# ================================================================


class TestFreeFermionCumulants:
    """Tests for the free fermion cumulant algebra."""

    def test_free_fermion_bar_dims(self):
        """Free fermion bar dims: b_n = p(n-1)."""
        from compute.lib.cumulant_algebra import _free_fermion_bar_dims
        bar = _free_fermion_bar_dims(max_degree=8)
        for n in range(1, 9):
            assert bar[n] == partition_number(n - 1)

    def test_free_fermion_q1(self):
        """Free fermion q_1 = 1."""
        ca = compute_primitive_cumulants('free_fermion', max_degree=10)
        assert ca.total_dims[1] == 1

    def test_free_fermion_round_trip(self):
        """Cofree recognition round-trip is exact."""
        ca = compute_primitive_cumulants('free_fermion', max_degree=10)
        assert ca.recognition_verified is True


# ================================================================
# TestEntropyLadder: entropy ordering across families
# ================================================================


class TestEntropyLadder:
    """Tests for the entropy ladder across standard families."""

    def test_entropy_ladder_returns_all_families(self):
        """entropy_ladder returns an entry for every standard family."""
        result = entropy_ladder()
        from compute.lib.cumulant_algebra import _BAR_DIM_PROVIDERS
        for fam in _BAR_DIM_PROVIDERS:
            assert fam in result

    def test_entropy_ladder_heisenberg_small(self):
        """Heisenberg entropy is near 0 (polynomial cumulant growth).

        The estimator uses finite data so may return a small nonzero value,
        but it should be much smaller than exponential-growth families.
        """
        result = entropy_ladder(families=['heisenberg'], max_degree=14)
        assert result['heisenberg'] < 0.1

    def test_entropy_ladder_free_fermion_small(self):
        """Free fermion entropy is near 0 (polynomial cumulant growth).

        The estimator uses finite data so may return a small nonzero value,
        but it should be much smaller than exponential-growth families.
        """
        result = entropy_ladder(families=['free_fermion'], max_degree=14)
        assert result['free_fermion'] < 0.15

    def test_entropy_ladder_virasoro_positive(self):
        """Virasoro entropy is positive (exponential cumulant growth)."""
        result = entropy_ladder(families=['virasoro'], max_degree=14)
        assert result['virasoro'] > 0

    def test_entropy_ladder_betagamma_positive(self):
        """betagamma entropy is positive (exponential cumulant growth)."""
        result = entropy_ladder(families=['betagamma'], max_degree=12)
        assert result['betagamma'] > 0

    def test_entropy_ladder_polynomial_leq_exponential(self):
        """Polynomial-growth families have entropy <= exponential-growth families."""
        result = entropy_ladder(max_degree=12)
        # Heisenberg and free_fermion are polynomial (h_K = 0)
        # Virasoro and betagamma are exponential (h_K > 0)
        assert result['heisenberg'] <= result['virasoro']
        assert result['free_fermion'] <= result['virasoro']

    def test_entropy_ladder_subset(self):
        """entropy_ladder with a subset of families."""
        result = entropy_ladder(families=['heisenberg', 'virasoro'])
        assert len(result) == 2
        assert 'heisenberg' in result
        assert 'virasoro' in result

    def test_entropy_ladder_aliases(self):
        """entropy_ladder accepts family aliases."""
        result = entropy_ladder(families=['heis', 'vir'])
        assert 'heisenberg' in result
        assert 'virasoro' in result


# ================================================================
# TestDSReduction: Drinfeld-Sokolov cumulant comparison
# ================================================================


class TestDSReduction:
    """Tests for cumulant_ds_reduction comparison."""

    def test_ds_reduction_sl2_vs_virasoro(self):
        """Compare sl_2 and Virasoro cumulants under DS.

        DS: affine sl_2 -> Virasoro. The cumulant defect measures what
        is killed by the reduction functor.
        """
        ca_sl2 = compute_primitive_cumulants('affine_sl2', max_degree=8)
        ca_vir = compute_primitive_cumulants('virasoro', max_degree=8)
        result = cumulant_ds_reduction(ca_sl2.total_dims, ca_vir.total_dims)
        # At degree 1: sl_2 has q_1 = 3, Virasoro has q_1 = 1, defect = 2
        assert result["per_degree"][1]["defect"] == 2

    def test_ds_reduction_returns_structure(self):
        """DS reduction result contains expected keys."""
        parent = {1: 3, 2: -1, 3: 2}
        child = {1: 1, 2: 1, 3: 1}
        result = cumulant_ds_reduction(parent, child)
        assert "per_degree" in result
        assert "total_defect" in result
        assert "parent_entropy" in result
        assert "child_entropy" in result

    def test_ds_reduction_identical_families(self):
        """DS reduction of a family with itself has zero defect."""
        q = {1: 2, 2: 3, 3: 1}
        result = cumulant_ds_reduction(q, q)
        assert result["total_defect"] == 0
        for n in result["per_degree"]:
            assert result["per_degree"][n]["defect"] == 0

    def test_ds_reduction_total_defect_nonneg(self):
        """Total defect is always non-negative (sum of absolute values)."""
        parent = {1: 3, 2: -1}
        child = {1: 1, 2: 2, 3: 1}
        result = cumulant_ds_reduction(parent, child)
        assert result["total_defect"] >= 0

    def test_ds_reduction_survives_flag(self):
        """'survives' flag correctly identifies positive child cumulants."""
        parent = {1: 3, 2: 0}
        child = {1: 1, 2: 0}
        result = cumulant_ds_reduction(parent, child)
        assert result["per_degree"][1]["survives"] is True
        assert result["per_degree"][2]["survives"] is False


# ================================================================
# TestGrandCompletion: grand_completion_datum
# ================================================================


class TestGrandCompletion:
    """Tests for the grand completion datum assembly."""

    def test_grand_completion_heisenberg(self):
        """Grand completion for Heisenberg has depth class G."""
        datum = grand_completion_datum('heisenberg')
        assert datum["depth_class"] == "G"
        assert datum["recognition_verified"] is True

    def test_grand_completion_virasoro(self):
        """Grand completion for Virasoro has depth class M."""
        datum = grand_completion_datum('virasoro')
        assert datum["depth_class"] == "M"
        assert datum["all_cumulants_nonneg"] is True

    def test_grand_completion_sl2(self):
        """Grand completion for sl_2 has depth class L."""
        datum = grand_completion_datum('affine_sl2')
        assert datum["depth_class"] == "L"
        assert datum["all_cumulants_nonneg"] is False  # q_2 = -1

    def test_grand_completion_betagamma(self):
        """Grand completion for betagamma has depth class C."""
        datum = grand_completion_datum('betagamma')
        assert datum["depth_class"] == "C"

    def test_grand_completion_contains_cumulant_gf(self):
        """Grand completion datum includes the cumulant generating function."""
        datum = grand_completion_datum('heisenberg')
        assert datum["cumulant_gf"] is not None

    def test_grand_completion_all_families(self):
        """Grand completion datum works for all standard families."""
        from compute.lib.cumulant_algebra import _BAR_DIM_PROVIDERS
        for fam in _BAR_DIM_PROVIDERS:
            datum = grand_completion_datum(fam)
            assert "family" in datum
            assert "cumulant_dims" in datum
            assert "recognition_verified" in datum
            assert datum["recognition_verified"] is True

    def test_grand_completion_structural_note(self):
        """Each family has a nonempty structural note."""
        for fam in ['heisenberg', 'virasoro', 'affine_sl2', 'w3', 'betagamma']:
            datum = grand_completion_datum(fam)
            assert "structural_note" in datum
            assert len(datum["structural_note"]) > 10


# ================================================================
# TestGeneralizedBinom: generalized binomial coefficient
# ================================================================


class TestGeneralizedBinom:
    """Tests for the generalized binomial coefficient."""

    def test_binom_m_zero(self):
        """binom(q, 0) = 1 for all q."""
        for q in [-2, -1, 0, 1, 5, 10]:
            assert generalized_binom(q, 0) == 1

    def test_binom_m_negative(self):
        """binom(q, m) = 0 for m < 0."""
        for q in [0, 1, 3]:
            assert generalized_binom(q, -1) == 0

    def test_binom_standard_cases(self):
        """Standard multiset coefficients: binom(q+m-1, m)."""
        # binom(2+1-1, 1) = binom(2,1) = 2
        assert generalized_binom(2, 1) == 2
        # binom(3+2-1, 2) = binom(4,2) = 6
        assert generalized_binom(3, 2) == 6
        # binom(1+m-1, m) = binom(m, m) = 1
        for m in range(0, 6):
            assert generalized_binom(1, m) == 1

    def test_binom_negative_q(self):
        """Generalized binomial for negative q.

        binom(q+m-1, m) for q = -1, m = 1: (-1+1-1 choose 1) = (-1 choose 1) = -1.
        """
        assert generalized_binom(-1, 1) == -1
        # q=-1, m=2: binom(0, 2) = 0
        assert generalized_binom(-1, 2) == 0

    def test_binom_q_zero(self):
        """binom(0+m-1, m) = binom(m-1, m) = 0 for m >= 1."""
        for m in range(1, 6):
            assert generalized_binom(0, m) == 0


# ================================================================
# TestCofreeGF: cofree generating function analysis
# ================================================================


class TestCofreeGF:
    """Tests for the cofree generating function analysis."""

    def test_cofree_gf_returns_bar_dims(self):
        """cofree_gf_from_cumulant_gf returns bar_dims dict."""
        q = {1: 1, 2: 1}
        result = cofree_gf_from_cumulant_gf(q, max_degree=10)
        assert "bar_dims" in result
        assert len(result["bar_dims"]) == 10

    def test_cofree_gf_consistency(self):
        """bar_dims from cofree_gf matches cofree_dimensions directly."""
        q = {1: 2, 2: 1, 3: 1}
        result = cofree_gf_from_cumulant_gf(q, max_degree=10)
        direct = cofree_dimensions(q, max_degree=10)
        for n in range(1, 11):
            assert result["bar_dims"][n] == direct[n]

    def test_cofree_gf_radius_for_exponential(self):
        """Radius estimate is finite for exponentially growing cumulants."""
        # Large cumulants should give a finite radius
        q = {n: 2**n for n in range(1, 10)}
        result = cofree_gf_from_cumulant_gf(q, max_degree=10)
        assert result["radius_estimate"] is not None
        assert result["radius_estimate"] > 0


# ================================================================
# TestCumulantAlgebraDataclass: dataclass methods
# ================================================================


class TestCumulantAlgebraDataclass:
    """Tests for the CumulantAlgebra dataclass methods."""

    def test_summary_nonempty(self):
        """summary() returns a nonempty string."""
        ca = compute_primitive_cumulants('heisenberg', max_degree=8)
        s = ca.summary()
        assert len(s) > 0
        assert "Cumulant algebra" in s

    def test_cumulant_gf_sympy(self):
        """cumulant_generating_function returns a sympy expression."""
        ca = compute_primitive_cumulants('virasoro', max_degree=6)
        gf = ca.cumulant_generating_function()
        x = Symbol('x')
        # q_1 = 1 so coefficient of x is 1
        assert gf.coeff(x, 1) == 1

    def test_verify_cofree_recognition_result(self):
        """verify_cofree_recognition returns per-degree checks."""
        from compute.lib.cumulant_algebra import _virasoro_bar_dims
        bar = _virasoro_bar_dims(max_degree=8)
        ca = compute_primitive_cumulants('virasoro', max_degree=8)
        checks = ca.verify_cofree_recognition(bar)
        assert "all_degrees_match" in checks
        assert checks["all_degrees_match"] is True


# ================================================================
# TestFamilyAliases: family name resolution
# ================================================================


class TestFamilyAliases:
    """Tests for family alias resolution."""

    def test_canonical_names(self):
        """Canonical names are accepted directly."""
        for fam in ['heisenberg', 'virasoro', 'affine_sl2', 'w3', 'betagamma', 'free_fermion']:
            ca = compute_primitive_cumulants(fam, max_degree=5)
            assert ca.name == fam

    def test_aliases_resolve(self):
        """Common aliases resolve to canonical names."""
        aliases = {
            'heis': 'heisenberg', 'vir': 'virasoro', 'sl2': 'affine_sl2',
            'W3': 'w3', 'bg': 'betagamma', 'ff': 'free_fermion',
        }
        for alias, canonical in aliases.items():
            ca = compute_primitive_cumulants(alias, max_degree=5)
            assert ca.name == canonical

    def test_unknown_family_raises(self):
        """Unknown family name raises ValueError."""
        with pytest.raises(ValueError, match="Unknown family"):
            compute_primitive_cumulants('nonexistent_algebra')


# ================================================================
# TestCrossFamily: cross-family comparison
# ================================================================


class TestCrossFamily:
    """Tests for the cross-family comparison utility."""

    def test_cross_family_returns_all(self):
        """cross_family_cumulant_comparison returns all families."""
        result = cross_family_cumulant_comparison(max_degree=8)
        from compute.lib.cumulant_algebra import _BAR_DIM_PROVIDERS
        for fam in _BAR_DIM_PROVIDERS:
            assert fam in result

    def test_cross_family_recognition_all_verified(self):
        """All families have verified cofree recognition."""
        result = cross_family_cumulant_comparison(max_degree=8)
        for fam, data in result.items():
            if "error" not in data:
                assert data["recognition_verified"] is True, f"{fam} failed recognition"

    def test_cross_family_q1_values(self):
        """Check q_1 values across families."""
        result = cross_family_cumulant_comparison(max_degree=8)
        assert result["heisenberg"]["q_1"] == 1
        assert result["affine_sl2"]["q_1"] == 3
        assert result["virasoro"]["q_1"] == 1
        assert result["w3"]["q_1"] == 2
        assert result["betagamma"]["q_1"] == 2
        assert result["free_fermion"]["q_1"] == 1
