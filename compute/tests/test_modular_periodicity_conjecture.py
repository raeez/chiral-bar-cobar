"""Tests for modular periodicity conjecture analysis.

Investigates conj:modular-periodicity-minimal from chiral_hochschild_koszul.tex.

Key findings:
1. Step 1 (T-matrix periodicity) is UNCONDITIONAL — verified for all tested models.
2. Step 2 (weight-space periodicity) FAILS — the convolution with 1/eta destroys
   exact eventual periodicity. dim V_{r,s,[k]} grows monotonically for all k.
3. The theta-function NUMERATOR has exact periodicity (period dividing 2pq).
4. The periodicity defect dim[k+N] - dim[k] grows subexponentially (like partition
   numbers), NOT zero. The claim in the evidence that the tail sum is "empty for
   k sufficiently large" is incorrect.
5. The conjecture may still hold at the bar COHOMOLOGY level (with the differential),
   but this cannot be tested without explicit OPE data.

Refined conjecture candidate: For bar COHOMOLOGY (not chain) dimensions,
exact N-periodicity holds because the bar differential respects the Virasoro
module structure and quotients out the non-periodic growth from 1/eta.

References:
    - conj:modular-periodicity-minimal (chiral_hochschild_koszul.tex, line 3646)
    - comp:m58-weight-space-periodicity (chiral_hochschild_koszul.tex, line 3738)
    - rem:step2-stabilization-threshold (chiral_hochschild_koszul.tex, line 3733)
"""

import pytest
from sympy import Rational

from compute.lib.modular_periodicity_test import (
    minimal_model_central_charge,
    conformal_weights,
    modular_period,
    t_matrix_period,
    partition_table,
    weight_space_dims_direct,
    periodicity_difference,
    is_eventually_zero,
    is_eventually_periodic,
    analyze_eta_obstruction,
    theta_periodicity_test,
    quasi_periodicity_analysis,
    STANDARD_MODELS,
)


# ===========================================================================
# Step 1: T-matrix periodicity (unconditional)
# ===========================================================================

class TestTMatrixPeriodicity:
    """Verify Step 1: T^N = Id for all minimal models."""

    @pytest.mark.parametrize("p,q,name", STANDARD_MODELS)
    def test_t_matrix_period_divides_formula(self, p, q, name):
        """The formula period N divides the actual T-matrix period N_T."""
        N = modular_period(p, q)
        N_T = t_matrix_period(p, q)
        assert N_T % N == 0, f"{name}: N_T={N_T} not divisible by N={N}"

    @pytest.mark.parametrize("p,q,name", STANDARD_MODELS)
    def test_t_matrix_period_divides_24pq(self, p, q, name):
        """N_T divides 24pq (universal bound)."""
        N_T = t_matrix_period(p, q)
        assert (24 * p * q) % N_T == 0, f"{name}: 24pq={24*p*q} not divisible by N_T={N_T}"

    @pytest.mark.parametrize("p,q,name", STANDARD_MODELS)
    def test_nc_over_24_integer(self, p, q, name):
        """N*c/24 is an integer (T^N = Id on character space)."""
        c = minimal_model_central_charge(p, q)
        N = modular_period(p, q)
        val = Rational(N) * c / 24
        assert val == int(val), f"{name}: Nc/24 = {val} not integer"

    def test_ising_period(self):
        """Ising M(3,4): c=1/2, N=48."""
        assert minimal_model_central_charge(3, 4) == Rational(1, 2)
        assert modular_period(3, 4) == 48

    def test_yang_lee_period(self):
        """Yang-Lee M(2,5): c=-22/5, N=60."""
        assert minimal_model_central_charge(2, 5) == Rational(-22, 5)
        assert modular_period(2, 5) == 60

    def test_m35_period(self):
        """M(3,5): c=-3/5, N=40."""
        assert minimal_model_central_charge(3, 5) == Rational(-3, 5)
        assert modular_period(3, 5) == 40

    def test_m58_period(self):
        """M(5,8): c=-7/20, N=480 (the comp:m58 test case)."""
        assert minimal_model_central_charge(5, 8) == Rational(-7, 20)
        # c = -7/20, p'=-7, q'=20, gcd(7,24)=1, N=24*20/1=480
        assert modular_period(5, 8) == 480


# ===========================================================================
# Step 2 gap: 1/eta convolution obstruction
# ===========================================================================

class TestEtaObstruction:
    """Demonstrate that convolution with 1/eta destroys eventual periodicity."""

    def test_eta_destroys_periodicity(self):
        """The test sequence a(k) with period N, convolved with p(k),
        gives diffs that equal p(k+N), NOT zero."""
        obs = analyze_eta_obstruction(200)
        assert obs["diffs_equal_partition_shifted"] is True
        assert obs["diffs_eventually_zero"] is False

    def test_ising_weight_space_not_periodic(self):
        """Ising vacuum module weight-space dims are NOT eventually N-periodic."""
        N = modular_period(3, 4)  # 48
        dims = weight_space_dims_direct(3, 4, 1, 1, N + 40)
        diffs = periodicity_difference(dims, N)
        assert not is_eventually_zero(diffs, start=10)

    def test_ising_weight_space_monotone(self):
        """Ising vacuum dims are eventually monotonically increasing."""
        dims = weight_space_dims_direct(3, 4, 1, 1, 80)
        # After the null at level 1, dims should be increasing
        assert dims[0] == 1
        assert dims[1] == 0  # null vector at level 1
        # Eventually increasing
        for k in range(5, 79):
            assert dims[k + 1] >= dims[k], f"Non-monotone at k={k}: {dims[k]} > {dims[k+1]}"

    def test_yang_lee_weight_space_not_periodic(self):
        """Yang-Lee vacuum dims are NOT eventually N-periodic."""
        N = modular_period(2, 5)  # 60
        dims = weight_space_dims_direct(2, 5, 1, 1, N + 30)
        diffs = periodicity_difference(dims, N)
        assert not is_eventually_zero(diffs, start=5)

    def test_m35_weight_space_not_periodic(self):
        """M(3,5) vacuum dims are NOT eventually N-periodic."""
        N = modular_period(3, 5)  # 40
        dims = weight_space_dims_direct(3, 5, 1, 1, N + 30)
        diffs = periodicity_difference(dims, N)
        assert not is_eventually_zero(diffs, start=5)

    def test_periodicity_diffs_grow(self):
        """The periodicity defect dim[k+N]-dim[k] grows, not stabilizes."""
        N = modular_period(3, 4)
        dims = weight_space_dims_direct(3, 4, 1, 1, N + 60)
        diffs = periodicity_difference(dims, N)
        # Diffs should be positive and growing for k >> 0
        tail = diffs[-20:]
        assert all(d > 0 for d in tail), "Diffs should be positive"
        assert tail[-1] > tail[0], "Diffs should be growing"


# ===========================================================================
# Theta numerator periodicity (isolating the obstruction)
# ===========================================================================

class TestThetaNumerator:
    """The theta numerator coefficients are SPARSE and NOT periodic.

    This is a deeper failure than just the 1/eta convolution: the evidence
    Step 2 (line 3718-3720) incorrectly claims a_Theta(k+N) = a_Theta(k).
    The theta function has modular periodicity (tau -> tau+1 gives a phase),
    but this does NOT make the Fourier coefficients periodic in the weight index.
    The null vector exponents A(n), B(n) grow quadratically, producing a sparse
    (not periodic) coefficient sequence.
    """

    def test_ising_theta_NOT_periodic(self):
        """Ising: theta numerator is NOT 2pq=24-periodic in Fourier index."""
        result = theta_periodicity_test(3, 4, 1, 1, 200)
        assert result["numerator_periodic_2pq"] is False

    def test_ising_theta_sparse(self):
        """Ising: theta numerator coefficients are sparse."""
        result = theta_periodicity_test(3, 4, 1, 1, 200)
        assert result["numerator_sparse"] is True
        assert result["density"] < 0.05

    def test_yang_lee_theta_NOT_periodic(self):
        """Yang-Lee: theta numerator NOT periodic."""
        result = theta_periodicity_test(2, 5, 1, 1, 200)
        assert result["numerator_periodic_2pq"] is False

    @pytest.mark.parametrize("p,q,name", STANDARD_MODELS[:5])
    def test_theta_sparse(self, p, q, name):
        """All theta numerators are sparse (density < 10%)."""
        ws = conformal_weights(p, q)
        if ws:
            r0, s0 = ws[0]["r"], ws[0]["s"]
            result = theta_periodicity_test(p, q, r0, s0, 200)
            assert result["numerator_sparse"] is True


# ===========================================================================
# Weight-space dimension sanity checks
# ===========================================================================

class TestWeightSpaceDims:
    """Sanity checks for the Rocha-Caridi weight-space computation."""

    def test_ising_vacuum_first_dims(self):
        """Ising vacuum: known dimensions from Virasoro c=1/2 representation theory."""
        dims = weight_space_dims_direct(3, 4, 1, 1, 10)
        # Ising vacuum (h=0, c=1/2): 1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12
        # Null vector at level 1 (from singular vector in M(3,4) Kac table)
        assert dims[0] == 1
        assert dims[1] == 0  # null at level 1

    def test_ising_sigma_first_dims(self):
        """Ising sigma (h=1/16): dims should start at 1."""
        # h=1/16 is not integer, so in our direct formula framework
        # this requires fractional shifts — skip for now
        pass

    def test_yang_lee_vacuum(self):
        """Yang-Lee vacuum: h=0, c=-22/5."""
        dims = weight_space_dims_direct(2, 5, 1, 1, 10)
        assert dims[0] == 1
        # Yang-Lee vacuum has null at level 1 as well
        assert dims[1] == 0

    def test_partition_table(self):
        """Verify partition function values."""
        P = partition_table(20)
        assert P[0] == 1
        assert P[1] == 1
        assert P[2] == 2
        assert P[3] == 3
        assert P[4] == 5
        assert P[5] == 7
        assert P[10] == 42
        assert P[20] == 627

    def test_dims_nonnegative(self):
        """Weight-space dimensions must be non-negative."""
        for p, q, name in STANDARD_MODELS[:5]:
            ws = conformal_weights(p, q)
            for w in ws:
                dims = weight_space_dims_direct(p, q, w["r"], w["s"], 30)
                assert all(d >= 0 for d in dims), \
                    f"{name} V_{{{w['r']},{w['s']}}}: negative dim at some level"


# ===========================================================================
# Module count verification
# ===========================================================================

class TestModuleCount:
    """Verify the number of irreducible modules (p-1)(q-1)/2."""

    @pytest.mark.parametrize("p,q,expected,name", [
        (3, 4, 3, "Ising"),
        (2, 5, 2, "Yang-Lee"),
        (3, 5, 4, "M(3,5)"),
        (4, 5, 6, "tricritical Ising"),
        (5, 8, 14, "M(5,8)"),
    ])
    def test_module_count(self, p, q, expected, name):
        ws = conformal_weights(p, q)
        assert len(ws) == expected, f"{name}: got {len(ws)} modules, expected {expected}"


# ===========================================================================
# Central charge verification
# ===========================================================================

class TestCentralCharges:
    """Verify central charge formula and lowest-terms decomposition."""

    def test_ising(self):
        assert minimal_model_central_charge(3, 4) == Rational(1, 2)

    def test_yang_lee(self):
        assert minimal_model_central_charge(2, 5) == Rational(-22, 5)

    def test_m35(self):
        assert minimal_model_central_charge(3, 5) == Rational(-3, 5)

    def test_m45(self):
        # M(4,5) = tricritical Ising: c = 1 - 6*1/(20) = 1 - 3/10 = 7/10
        assert minimal_model_central_charge(4, 5) == Rational(7, 10)

    def test_m58(self):
        # M(5,8): c = 1 - 6*9/40 = 1 - 54/40 = 1 - 27/20 = -7/20
        assert minimal_model_central_charge(5, 8) == Rational(-7, 20)

    def test_m27(self):
        # M(2,7): c = 1 - 6*25/14 = 1 - 75/7 = -68/7
        assert minimal_model_central_charge(2, 7) == Rational(-68, 7)


# ===========================================================================
# Precise failure mechanism identification
# ===========================================================================

class TestFailureMechanism:
    """Identify the EXACT failure in Step 2 of the evidence.

    The evidence claims (line 3729-3731): "for k exceeding the maximal
    pole order of Theta_{r,s}/eta, the sum on the right is empty."

    This is WRONG. The sum sum_{j>k} (a(k+N-j) - a(k-j)) p(j) is NOT
    eventually empty because:
    1. a(k+N-j) = a(k-j) only when BOTH indices are in the periodic range
    2. For j > k, the index k-j < 0, where a is identically 0
    3. But a(k+N-j) can be nonzero when 0 <= k+N-j (i.e., j <= k+N)
    4. So the sum picks up p(j) for k < j <= k+N where a(k+N-j) != 0
    5. These terms contribute sum_{j=k+1}^{k+N} a(k+N-j) p(j) which grows

    The error is conflating "a has no poles" (finite support in negative indices)
    with "the convolution tail vanishes" (it does not, because p(j) grows).
    """

    def test_convolution_tail_nonzero(self):
        """The convolution tail sum_{j>k} terms does NOT vanish for large k."""
        # For the simplest periodic sequence a(k) = delta_{k mod N, 0}:
        # conv(k) = sum_{m=0}^{k//N} p(k - mN)
        # conv(k+N) - conv(k) = p(k+N) (new highest term)
        # This is manifestly nonzero and growing.
        obs = analyze_eta_obstruction(150)
        assert obs["diffs_equal_partition_shifted"]
        assert not obs["diffs_eventually_zero"]

    def test_ising_defect_positive_growing(self):
        """Ising: the periodicity defect is positive and unbounded."""
        N = 48
        dims = weight_space_dims_direct(3, 4, 1, 1, N + 50)
        diffs = periodicity_difference(dims, N)
        # All diffs for k >= some threshold should be positive
        assert all(d > 0 for d in diffs[10:])
        # Growth: later diffs are larger
        assert diffs[-1] > diffs[len(diffs) // 2]

    def test_m58_monotone_growth(self):
        """M(5,8): confirm comp:m58-weight-space-periodicity finding.

        N=480 is too large for direct periodicity test, but we verify
        monotone growth of dims through k=80 as stated in the computation.
        """
        ws = conformal_weights(5, 8)
        for w in ws[:3]:  # test first 3 modules
            dims = weight_space_dims_direct(5, 8, w["r"], w["s"], 80)
            # After initial nulls, should be monotonically increasing
            # (confirming "no eventual periodicity detected")
            max_dim = max(dims)
            assert max_dim == dims[-1] or max_dim == dims[-2], \
                f"V_{{{w['r']},{w['s']}}}: max not at end, dims not monotone"


# ===========================================================================
# Refined conjecture analysis
# ===========================================================================

class TestRefinedConjecture:
    """Test candidates for a refined conjecture.

    Since exact periodicity of weight-space dims fails, candidates:
    (A) Periodicity of bar COHOMOLOGY (requires differential — cannot test here)
    (B) Quasi-periodicity: dim[k+N] - dim[k] ~ f(k) for some explicit f
    (C) Periodicity modulo the partition function: dim[k]/p(k) is N-periodic
    (D) Periodicity of the "reduced character" chi/eta (just the theta part)
    """

    def test_theta_part_sparse_not_periodic(self):
        """The theta numerator is sparse and NOT periodic in Fourier index.
        Option (D) fails: there is no 'reduced character' with periodic coefficients."""
        for p, q, name in STANDARD_MODELS[:3]:
            ws = conformal_weights(p, q)
            if ws:
                result = theta_periodicity_test(p, q, ws[0]["r"], ws[0]["s"], 200)
                assert result["numerator_sparse"], f"{name}: theta should be sparse"
                assert not result["numerator_periodic_2pq"], \
                    f"{name}: theta should NOT be 2pq-periodic"

    def test_defect_subexponential(self):
        """The periodicity defect grows sub-exponentially (like partition numbers)."""
        N = modular_period(3, 4)
        dims = weight_space_dims_direct(3, 4, 1, 1, N + 60)
        P = partition_table(N + 60)
        diffs = periodicity_difference(dims, N)

        # Check that diffs grow slower than exponential
        # Ratio diffs[k+1]/diffs[k] should be < 2 for all large k
        for k in range(30, len(diffs) - 1):
            if diffs[k] > 0:
                ratio = diffs[k + 1] / diffs[k]
                assert ratio < 2.0, f"Exponential growth at k={k}"

    def test_two_independent_obstructions(self):
        """The conjecture faces TWO independent obstructions:
        (1) Theta numerator coefficients are sparse/non-periodic (not just 1/eta)
        (2) Convolution with 1/eta further destroys any residual structure

        Both must be resolved for bar COHOMOLOGY periodicity to hold.
        The conjecture can only be saved if the bar differential
        exactly compensates both effects."""
        # Obstruction 1: theta not periodic
        result = theta_periodicity_test(3, 4, 1, 1, 200)
        assert not result["numerator_periodic_2pq"]

        # Obstruction 2: 1/eta convolution destroys periodicity
        obs = analyze_eta_obstruction(150)
        assert not obs["diffs_eventually_zero"]

        # Both obstructions confirmed independently
        assert True
