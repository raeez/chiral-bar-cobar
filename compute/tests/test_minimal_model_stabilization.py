"""Tests for M(5,8) bar chain stabilization computation.

Verifies:
  - Partition function
  - Kac table conformal weights
  - Rocha-Caridi weight-space dimensions (cross-validated against Ising and Lee-Yang)
  - M(5,8) module data
  - Step 2 gap confirmation: weight-space dims NOT eventually periodic
"""

import pytest
from sympy import Rational

from compute.lib.minimal_model_stabilization import (
    partition,
    kac_weight,
    kac_table,
    n_modules,
    weight_space_dim,
    weight_space_dims,
    modular_period,
    theta_level_period,
    detect_eventual_period,
    find_best_period,
    divisors,
    m58_data,
    lee_yang_vacuum_dims,
    ising_vacuum_dims,
    ising_sigma_dims,
    ising_epsilon_dims,
    minimal_model_c,
)


# ===== Partition function =====

class TestPartition:
    def test_small_values(self):
        assert [partition(k) for k in range(11)] == [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]

    def test_p20(self):
        assert partition(20) == 627

    def test_p50(self):
        assert partition(50) == 204226

    def test_negative(self):
        assert partition(-1) == 0
        assert partition(-100) == 0


# ===== Kac table =====

class TestKacTable:
    def test_ising_modules(self):
        """M(3,4) has 3 modules."""
        assert n_modules(3, 4) == 3
        modules = kac_table(3, 4)
        assert len(modules) == 3

    def test_lee_yang_modules(self):
        """M(2,5) has 2 modules."""
        assert n_modules(2, 5) == 2
        modules = kac_table(2, 5)
        assert len(modules) == 2

    def test_m58_modules(self):
        """M(5,8) has 14 modules."""
        assert n_modules(5, 8) == 14
        modules = kac_table(5, 8)
        assert len(modules) == 14

    def test_tricritical_modules(self):
        """M(4,5) has 6 modules."""
        assert n_modules(4, 5) == 6

    def test_potts_modules(self):
        """M(5,6) has 10 modules."""
        assert n_modules(5, 6) == 10


# ===== Conformal weights =====

class TestConformalWeights:
    def test_ising_vacuum(self):
        """M(3,4) vacuum: h_{1,1} = 0."""
        assert kac_weight(3, 4, 1, 1) == 0

    def test_ising_sigma(self):
        """M(3,4) sigma: h_{1,2} = 1/16."""
        assert kac_weight(3, 4, 1, 2) == Rational(1, 16)

    def test_ising_epsilon(self):
        """M(3,4) epsilon: h_{2,1} = 1/2."""
        assert kac_weight(3, 4, 2, 1) == Rational(1, 2)

    def test_lee_yang_vacuum(self):
        """M(2,5) vacuum: h_{1,1} = 0."""
        assert kac_weight(2, 5, 1, 1) == 0

    def test_lee_yang_phi(self):
        """M(2,5) phi: h_{1,2} = -1/5."""
        assert kac_weight(2, 5, 1, 2) == Rational(-1, 5)

    def test_m58_vacuum(self):
        """M(5,8) vacuum: h_{1,1} = 0."""
        assert kac_weight(5, 8, 1, 1) == 0

    def test_m58_central_charge(self):
        """M(5,8): c = -7/20 (NOT 57/40 as stated in rem:step2-stabilization-threshold)."""
        assert minimal_model_c(5, 8) == Rational(-7, 20)

    def test_m58_nonunitary(self):
        """M(5,8) is non-unitary: some h_{r,s} < 0."""
        h12 = kac_weight(5, 8, 1, 2)
        assert h12 == Rational(-1, 32)
        assert h12 < 0

    def test_m58_weights(self):
        """Spot-check several M(5,8) conformal weights."""
        assert kac_weight(5, 8, 1, 3) == Rational(1, 4)
        assert kac_weight(5, 8, 2, 1) == Rational(7, 10)
        assert kac_weight(5, 8, 2, 3) == Rational(-1, 20)
        assert kac_weight(5, 8, 1, 7) == Rational(9, 2)

    def test_kac_identification(self):
        """h_{r,s} = h_{p-r, q-s} (Kac table symmetry)."""
        for p, q in [(3, 4), (5, 8)]:
            for r in range(1, p):
                for s in range(1, q):
                    assert kac_weight(p, q, r, s) == kac_weight(p, q, p - r, q - s)


# ===== Weight-space dimensions: Ising cross-validation =====

class TestIsingDims:
    def test_vacuum_low(self):
        """Ising vacuum: d = [1,0,1,1,2,2,3,3,5,5,7,8]."""
        dims = ising_vacuum_dims(11)
        assert dims == [1, 0, 1, 1, 2, 2, 3, 3, 5, 5, 7, 8]

    def test_vacuum_null_at_1(self):
        """Level 1 is null (L_{-1}|0> = 0): d(1) = 0."""
        assert weight_space_dim(3, 4, 1, 1, 1) == 0

    def test_vacuum_null_at_6(self):
        """Second null at level 6: d(6) = p(6)-p(5)-p(0) = 3."""
        assert weight_space_dim(3, 4, 1, 1, 6) == 3

    def test_sigma_is_partitions_into_distinct_parts(self):
        """Ising sigma matches OEIS A000009 (partitions into distinct parts).

        This reflects the free fermion realization at c = 1/2.
        """
        a000009 = [1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22, 27, 32, 38, 46, 54, 64]
        assert ising_sigma_dims(20) == a000009

    def test_epsilon_low(self):
        """Ising epsilon: d = [1,1,1,1,2,2,3,4,5,6]."""
        dims = ising_epsilon_dims(9)
        assert dims == [1, 1, 1, 1, 2, 2, 3, 4, 5, 6]


# ===== Weight-space dimensions: Lee-Yang cross-validation =====

class TestLeeYangDims:
    def test_vacuum_low(self):
        """Lee-Yang vacuum: d = [1,0,1,1,1,1,2,2,3,3,4]."""
        dims = lee_yang_vacuum_dims(10)
        assert dims == [1, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4]

    def test_vacuum_null_structure(self):
        """Lee-Yang M(2,5) vacuum: nulls at levels 1 and 4."""
        # Level 1: d(1) = p(1)-p(0) = 0
        assert weight_space_dim(2, 5, 1, 1, 1) == 0
        # Level 4: second null kicks in
        # d(4) = p(4)-p(3)-p(0) = 5-3-1 = 1
        assert weight_space_dim(2, 5, 1, 1, 4) == 1


# ===== Weight-space dimensions: M(5,8) =====

class TestM58Dims:
    def test_vacuum_low(self):
        """M(5,8) vacuum: d(k) = p(k) - p(k-1) for k < 28."""
        dims = weight_space_dims(5, 8, 1, 1, 27)
        expected = [partition(0)] + [partition(k) - partition(k - 1) for k in range(1, 28)]
        assert dims == expected

    def test_vacuum_d0(self):
        assert weight_space_dim(5, 8, 1, 1, 0) == 1

    def test_vacuum_d1(self):
        """Level 1 is null."""
        assert weight_space_dim(5, 8, 1, 1, 1) == 0

    def test_vacuum_d28(self):
        """Second null at level 28: first correction from delta_-(-1) = 28."""
        # d(28) = p(28) - p(27) - p(0) = 3718 - 3010 - 1 = 707
        assert weight_space_dim(5, 8, 1, 1, 28) == 707

    def test_all_dims_nonneg(self):
        """All weight-space dims are non-negative (they're dimensions)."""
        for r, s in kac_table(5, 8):
            dims = weight_space_dims(5, 8, r, s, 40)
            for k, d in enumerate(dims):
                assert d >= 0, f"V_({r},{s}) has d({k}) = {d} < 0"

    def test_d0_always_1(self):
        """d(0) = 1 for all modules (highest weight state)."""
        for r, s in kac_table(5, 8):
            assert weight_space_dim(5, 8, r, s, 0) == 1


# ===== Period and modular data =====

class TestPeriodData:
    def test_m58_modular_period(self):
        """T-matrix period for M(5,8): N = 480."""
        assert modular_period(5, 8) == 480

    def test_m58_theta_period(self):
        """Theta function level for M(5,8): pq = 40."""
        assert theta_level_period(5, 8) == 40

    def test_ising_modular_period(self):
        """T-matrix period for M(3,4): N = 48."""
        assert modular_period(3, 4) == 48

    def test_lee_yang_modular_period(self):
        """T-matrix period for M(2,5)."""
        # c = -22/5, p'=-22, q'=5, gcd(22,24)=2, N=24*5/2=60
        assert modular_period(2, 5) == 60


# ===== Periodicity detection =====

class TestPeriodicityDetection:
    def test_constant_sequence(self):
        """Constant sequence has period 1."""
        seq = [3] * 20
        assert detect_eventual_period(seq, 1) == 0

    def test_periodic_sequence(self):
        """[1,2,3,1,2,3,...] has period 3."""
        seq = [1, 2, 3] * 10
        assert detect_eventual_period(seq, 3) == 0

    def test_eventually_periodic(self):
        """[0,0,0,1,2,1,2,1,2,...] is eventually periodic with period 2."""
        seq = [0, 0, 0] + [1, 2] * 10
        assert detect_eventual_period(seq, 2) == 3

    def test_not_periodic(self):
        """Growing sequence is not periodic."""
        seq = list(range(20))
        assert detect_eventual_period(seq, 3) is None

    def test_divisors(self):
        assert divisors(12) == [1, 2, 3, 4, 6, 12]
        assert divisors(40) == [1, 2, 4, 5, 8, 10, 20, 40]


# ===== Step 2 gap confirmation =====

class TestStep2Gap:
    """Confirm the Step 2 gap: weight-space dims are NOT eventually periodic."""

    def test_vacuum_not_periodic_5(self):
        """M(5,8) vacuum dims are NOT 5-periodic."""
        dims = weight_space_dims(5, 8, 1, 1, 50)
        assert detect_eventual_period(dims, 5) is None

    def test_vacuum_not_periodic_40(self):
        """M(5,8) vacuum dims are NOT 40-periodic (= pq)."""
        dims = weight_space_dims(5, 8, 1, 1, 120)
        assert detect_eventual_period(dims, 40) is None

    def test_vacuum_monotone_growth(self):
        """Vacuum dims grow monotonically for k >= 2."""
        dims = weight_space_dims(5, 8, 1, 1, 60)
        for k in range(3, len(dims)):
            assert dims[k] >= dims[k - 1], f"Non-monotone at k={k}"

    def test_differences_grow(self):
        """d(k+N) - d(k) grows for all tested N, confirming no periodicity."""
        dims = weight_space_dims(5, 8, 1, 1, 60)
        for N in [5, 8, 10, 20, 40]:
            diffs = [dims[k + N] - dims[k] for k in range(10, len(dims) - N)]
            # All positive (dims grow)
            assert all(d > 0 for d in diffs), f"Non-positive diff for N={N}"
            # Diffs themselves grow (last > first by significant margin)
            assert diffs[-1] > 2 * diffs[0], f"Diffs don't grow for N={N}"

    def test_no_module_periodic(self):
        """No M(5,8) module has eventually periodic weight-space dims."""
        for r, s in kac_table(5, 8):
            dims = weight_space_dims(5, 8, r, s, 50)
            for N in [5, 8, 10, 20, 40]:
                result = detect_eventual_period(dims, N)
                assert result is None, \
                    f"V_({r},{s}) falsely detected as {N}-periodic at k={result}"

    def test_gap_quantification(self):
        """Quantify the gap: d(k+40)/d(k) remains large (>> 1) for all k.

        If dims were 40-periodic, this ratio would be 1.
        """
        dims = weight_space_dims(5, 8, 1, 1, 80)
        for k in range(20, 40):
            ratio = dims[k + 40] / dims[k]
            assert ratio > 50, f"Ratio d({k+40})/d({k}) = {ratio:.1f} unexpectedly small"


# ===== M(5,8) data =====

class TestM58Data:
    def test_central_charge(self):
        data = m58_data()
        assert data["c"] == Rational(-7, 20)

    def test_module_count(self):
        data = m58_data()
        assert data["n_modules"] == 14

    def test_modular_period(self):
        data = m58_data()
        assert data["modular_period"] == 480

    def test_weights_include_negative(self):
        """Non-unitary: at least one h_{r,s} < 0."""
        data = m58_data()
        neg = [h for h in data["conformal_weights"].values() if h < 0]
        assert len(neg) >= 2  # h_{1,2} = -1/32 and h_{2,3} = -1/20


# ===== Asymptotic structure =====

class TestAsymptotics:
    def test_ratio_to_partition(self):
        """d(k)/p(k) decreases slowly but stays bounded away from 0.

        For the vacuum module, d(k) ~ C * p(k) with 0 < C < 1.
        """
        dims = weight_space_dims(5, 8, 1, 1, 60)
        for k in range(40, 60):
            ratio = dims[k] / partition(k)
            assert 0.1 < ratio < 0.5, f"Ratio d({k})/p({k}) = {ratio:.4f} out of range"

    def test_all_modules_grow_subexponentially(self):
        """All module dims grow at most as fast as p(k)."""
        for r, s in kac_table(5, 8):
            dims = weight_space_dims(5, 8, r, s, 50)
            for k in range(10, 50):
                if partition(k) > 0:
                    assert dims[k] <= partition(k), \
                        f"V_({r},{s}) at k={k}: d={dims[k]} > p(k)={partition(k)}"
