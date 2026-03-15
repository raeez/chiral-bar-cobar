"""Tests for pro-Weyl convergence of Y(sl_2) — task B7.

Tests verify conj:pro-weyl-recovery (yangians.tex) at the character level:
  M(Psi) ~= R lim_m W_m

  1. Truncated Weyl modules W_m have correct characters
  2. Projective system structure (surjectivity of transition maps)
  3. Coefficientwise convergence W_m -> M(lambda) as m -> infinity
  4. Error character support on weights <= lambda - 2m
  5. Linear convergence rate (one weight space per level)
  6. R^1 lim = 0 (Mittag-Leffler condition from surjectivity)
  7. Finite-dimensional Weyl module structure
  8. Drinfeld polynomial truncation
  9. Multi-lambda verification (lambda = 0, 1, 2, 5, 10)
"""

import pytest

from compute.lib.sl2_baxter import (
    FormalCharacter,
    formal_character_equal,
    sl2_fd_character,
    sl2_verma_character,
    subtract_characters,
)
from compute.lib.pro_weyl_sl2 import (
    # Truncations
    weyl_truncation,
    weyl_tower,
    # Error analysis
    error_character,
    error_support_bound,
    error_dimension,
    # Convergence
    coefficientwise_convergence,
    convergence_rate_data,
    convergence_summary,
    # Projective system
    verify_projective_system,
    verify_inverse_limit,
    # Derived corrections
    r1_lim_vanishing,
    # fd Weyl
    fd_weyl_character,
    fd_weyl_vs_verma,
    # Drinfeld polynomial
    drinfeld_polynomial_truncation,
    # Tail decay
    tail_decay,
    verify_linear_decay,
    # Full suite
    verify_all,
    # Multi-lambda
    verify_pro_weyl_convergence,
)


# ============================================================================
# Weyl truncations
# ============================================================================

class TestWeylTruncation:
    """Test the truncated Weyl module characters W_m."""

    def test_W0_is_empty(self):
        """W_0 (zero weight levels) has empty character."""
        assert weyl_truncation(5, 0) == {}

    def test_W1_is_highest_weight(self):
        """W_1 has only the highest weight space."""
        for lam in [0, 1, 3, 10]:
            W1 = weyl_truncation(lam, 1)
            assert W1 == {lam: 1}

    def test_W2_has_two_weights(self):
        """W_2 has the top two weight spaces."""
        W2 = weyl_truncation(5, 2)
        assert W2 == {5: 1, 3: 1}

    def test_Wm_dimension(self):
        """dim(W_m) = m (each weight space is 1-dimensional for sl_2 Verma)."""
        for lam in [0, 2, 7]:
            for m in range(1, 15):
                W_m = weyl_truncation(lam, m)
                assert sum(W_m.values()) == m

    def test_Wm_highest_weight(self):
        """Highest weight in W_m is lambda."""
        for lam in [0, 1, 5, 10]:
            for m in [1, 5, 10]:
                W_m = weyl_truncation(lam, m)
                assert max(W_m.keys()) == lam

    def test_Wm_lowest_weight(self):
        """Lowest weight in W_m is lambda - 2(m-1)."""
        for lam in [3, 7]:
            for m in [1, 3, 5]:
                W_m = weyl_truncation(lam, m)
                assert min(W_m.keys()) == lam - 2 * (m - 1)

    def test_Wm_all_mults_one(self):
        """All weight multiplicities in W_m are 1."""
        W_m = weyl_truncation(5, 10)
        for mult in W_m.values():
            assert mult == 1

    def test_Wm_weight_spacing(self):
        """Weights in W_m decrease by 2."""
        W_m = weyl_truncation(4, 6)
        weights = sorted(W_m.keys(), reverse=True)
        for i in range(len(weights) - 1):
            assert weights[i] - weights[i + 1] == 2

    def test_Wm_subcharacter_of_verma(self):
        """ch(W_m) is a sub-character of ch(M(lambda))."""
        lam, depth = 5, 50
        verma = sl2_verma_character(lam, depth=depth)
        for m in [1, 5, 10, 20]:
            W_m = weyl_truncation(lam, m)
            for w, mult in W_m.items():
                assert verma.get(w, 0) >= mult

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_Wm_converges_to_verma(self, lam):
        """For large m, W_m agrees with M(lambda) up to depth m."""
        depth = 30
        verma = sl2_verma_character(lam, depth=depth)
        W_m = weyl_truncation(lam, depth)
        assert formal_character_equal(W_m, verma)


class TestWeylTower:
    """Test the Weyl tower construction."""

    def test_tower_length(self):
        """Tower has the requested number of levels."""
        tower = weyl_tower(5, 10)
        assert len(tower) == 10

    def test_tower_increasing_dimension(self):
        """Each level in the tower has one more weight space."""
        tower = weyl_tower(3, 15)
        for i in range(len(tower) - 1):
            dim_curr = sum(tower[i].values())
            dim_next = sum(tower[i + 1].values())
            assert dim_next == dim_curr + 1

    def test_tower_nesting(self):
        """W_m is a sub-character of W_{m+1}."""
        tower = weyl_tower(5, 10)
        for i in range(len(tower) - 1):
            for w, mult in tower[i].items():
                assert tower[i + 1].get(w, 0) >= mult


# ============================================================================
# Error characters
# ============================================================================

class TestErrorCharacter:
    """Test the error character ch(M(lambda)) - ch(W_m)."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_error_nonnegative(self, lam):
        """Error character has nonneg multiplicities (W_m is a sub-character)."""
        for m in [1, 3, 5, 10]:
            err = error_character(lam, m)
            for mult in err.values():
                assert mult >= 0

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_error_plus_Wm_equals_verma(self, lam):
        """ch(W_m) + error(m) = ch(M(lambda))."""
        depth = 50
        for m in [1, 5, 10]:
            W_m = weyl_truncation(lam, m)
            err = error_character(lam, m, depth=depth)
            # Reconstruct verma
            reconstructed: FormalCharacter = {}
            for w, mult in W_m.items():
                reconstructed[w] = reconstructed.get(w, 0) + mult
            for w, mult in err.items():
                reconstructed[w] = reconstructed.get(w, 0) + mult
            verma = sl2_verma_character(lam, depth=depth)
            assert formal_character_equal(reconstructed, verma)

    def test_error_decreases(self):
        """dim(error(m+1)) = dim(error(m)) - 1."""
        lam, depth = 5, 50
        for m in range(1, 30):
            d1 = error_dimension(lam, m, depth=depth)
            d2 = error_dimension(lam, m + 1, depth=depth)
            assert d2 == d1 - 1

    def test_error_empty_at_full_depth(self):
        """Error is empty when m >= depth."""
        lam, depth = 3, 20
        err = error_character(lam, depth, depth=depth)
        assert err == {}


class TestErrorSupportBound:
    """Test that error is supported on weights <= lambda - 2m."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    @pytest.mark.parametrize("m", [1, 2, 3, 5, 8])
    def test_error_top_weight(self, lam, m):
        """Highest weight in error(m) is exactly lambda - 2m."""
        bound = error_support_bound(lam, m)
        assert bound == lam - 2 * m

    def test_error_support_none_at_full_depth(self):
        """error_support_bound returns None when error is empty."""
        assert error_support_bound(3, 50, depth=50) is None

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_all_error_weights_below_bound(self, lam):
        """Every weight in error(m) is <= lambda - 2m."""
        for m in [1, 3, 7]:
            err = error_character(lam, m)
            bound = lam - 2 * m
            for w in err.keys():
                assert w <= bound


class TestErrorDimension:
    """Test error dimension = depth - m."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_error_dim_formula(self, lam):
        """dim(error(m)) = depth - m for m <= depth."""
        depth = 50
        for m in [1, 5, 10, 20, 40]:
            expected = depth - m
            actual = error_dimension(lam, m, depth=depth)
            assert actual == expected

    def test_error_dim_zero_beyond_depth(self):
        """dim(error(m)) = 0 for m >= depth."""
        lam, depth = 3, 20
        assert error_dimension(lam, depth + 5, depth=depth) == 0


# ============================================================================
# Convergence analysis
# ============================================================================

class TestCoefficientwiseConvergence:
    """Test that each weight stabilizes at a finite truncation level."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_stabilization_levels(self, lam):
        """Weight lambda - 2k stabilizes at m = k+1."""
        data = coefficientwise_convergence(lam, max_m=20)
        for k in range(min(20, len(data))):
            weight = lam - 2 * k
            if weight in data:
                assert data[weight] == k + 1

    def test_highest_weight_stabilizes_at_m1(self):
        """The highest weight is captured at m=1."""
        for lam in [0, 1, 5, 10]:
            data = coefficientwise_convergence(lam, max_m=10)
            assert data[lam] == 1

    def test_second_weight_stabilizes_at_m2(self):
        """The second weight lambda-2 is captured at m=2."""
        for lam in [1, 3, 7]:
            data = coefficientwise_convergence(lam, max_m=10)
            assert data[lam - 2] == 2


class TestConvergenceRateData:
    """Test the convergence rate data structure."""

    def test_data_length(self):
        """Rate data has max_m entries."""
        data = convergence_rate_data(5, max_m=15)
        assert len(data) == 15

    def test_dim_Wm_is_m(self):
        """dim(W_m) = m."""
        data = convergence_rate_data(5, max_m=10, depth=50)
        for entry in data:
            assert entry["dim_Wm"] == entry["m"]

    def test_error_dim_decreasing(self):
        """Error dimension is strictly decreasing."""
        data = convergence_rate_data(5, max_m=20, depth=50)
        for i in range(len(data) - 1):
            assert data[i + 1]["dim_error"] < data[i]["dim_error"]

    def test_fraction_increasing(self):
        """Fraction captured is strictly increasing."""
        data = convergence_rate_data(5, max_m=20, depth=50)
        for i in range(len(data) - 1):
            assert data[i + 1]["fraction_captured"] > data[i]["fraction_captured"]

    def test_error_top_weight_decreasing(self):
        """Error top weight decreases by 2 at each step."""
        data = convergence_rate_data(5, max_m=20, depth=50)
        for i in range(len(data) - 1):
            w_curr = data[i]["error_top_weight"]
            w_next = data[i + 1]["error_top_weight"]
            if w_curr is not None and w_next is not None:
                assert w_curr - w_next == 2


# ============================================================================
# Projective system
# ============================================================================

class TestProjectiveSystem:
    """Test the projective system structure of the Weyl tower."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_projective_system_valid(self, lam):
        """Projective system holds for various lambda."""
        assert verify_projective_system(lam, max_m=20)

    def test_transition_maps_surjective(self):
        """Each W_{m+1} -> W_m is surjective (removes one weight space)."""
        lam = 5
        tower = weyl_tower(lam, 15)
        for i in range(len(tower) - 1):
            diff = subtract_characters(tower[i + 1], tower[i])
            # Exactly one new weight space
            assert sum(diff.values()) == 1


class TestInverseLimit:
    """Test that lim_m W_m = M(lambda) as formal characters."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_inverse_limit_converges(self, lam):
        """Inverse limit converges for various lambda."""
        assert verify_inverse_limit(lam, max_m=50, depth=30)

    def test_inverse_limit_large_depth(self):
        """Convergence holds at larger depth."""
        assert verify_inverse_limit(3, max_m=100, depth=80)


# ============================================================================
# Derived corrections (R^1 lim)
# ============================================================================

class TestR1Vanishing:
    """Test R^1 lim = 0 (Mittag-Leffler from surjectivity)."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_mittag_leffler(self, lam):
        """Mittag-Leffler condition holds (all transition maps surjective)."""
        assert r1_lim_vanishing(lam, max_m=20)

    def test_transition_increment_structure(self):
        """Each transition adds exactly the weight lambda - 2m at level m."""
        lam = 7
        tower = weyl_tower(lam, 15)
        for i in range(len(tower) - 1):
            diff = subtract_characters(tower[i + 1], tower[i])
            expected_weight = lam - 2 * (i + 1)
            assert diff == {expected_weight: 1}


# ============================================================================
# Finite-dimensional Weyl modules
# ============================================================================

class TestFdWeylModule:
    """Test finite-dimensional Weyl module structure."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 3, 5])
    def test_fd_weyl_is_irreducible(self, lam):
        """For Y(sl_2), W(lambda) = V_lambda (irreducible of dim lambda+1)."""
        weyl = fd_weyl_character(lam)
        irred = sl2_fd_character(lam + 1)
        assert formal_character_equal(weyl, irred)

    def test_fd_weyl_dimension(self):
        """dim W(lambda) = lambda + 1."""
        for lam in range(10):
            weyl = fd_weyl_character(lam)
            assert sum(weyl.values()) == lam + 1

    def test_fd_weyl_negative_raises(self):
        """fd Weyl module requires lambda >= 0."""
        with pytest.raises(ValueError):
            fd_weyl_character(-1)

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_kernel_structure(self, lam):
        """Kernel of M(lambda) -> W(lambda) = M(-lambda-2) for dominant lambda."""
        data = fd_weyl_vs_verma(lam)
        assert data["kernel_matches_subverma"]
        assert data["dim_weyl"] == lam + 1
        if lam >= 0:
            assert data["expected_kernel_hw"] == -lam - 2


class TestFdWeylVsVerma:
    """Comparison of fd Weyl module with Verma module."""

    def test_weyl_is_quotient_of_verma(self):
        """The Verma character dominates the Weyl character at every weight."""
        for lam in [0, 1, 3, 5]:
            verma = sl2_verma_character(lam, depth=50)
            weyl = fd_weyl_character(lam)
            for w, mult in weyl.items():
                assert verma.get(w, 0) >= mult

    def test_weyl_truncation_agrees_with_fd_weyl(self):
        """W_{lambda+1} restricted to dominant weights matches fd Weyl character.

        For sl_2, the fd Weyl module has lambda+1 weight spaces:
        lambda, lambda-2, ..., -lambda.
        The truncation W_{lambda+1} also has lambda+1 weight spaces:
        lambda, lambda-2, ..., lambda - 2*lambda = -lambda.
        They agree!
        """
        for lam in [0, 1, 2, 5]:
            trunc = weyl_truncation(lam, lam + 1)
            fd_weyl = fd_weyl_character(lam)
            assert formal_character_equal(trunc, fd_weyl)


# ============================================================================
# Drinfeld polynomial truncation
# ============================================================================

class TestDrinfeldTruncation:
    """Test Drinfeld polynomial truncation Psi_{<=m}."""

    def test_exact_at_full_level(self):
        """Truncation is exact when m >= lambda."""
        for lam in [1, 3, 5]:
            data = drinfeld_polynomial_truncation(lam, lam)
            assert data["is_exact"]
            data2 = drinfeld_polynomial_truncation(lam, lam + 5)
            assert data2["is_exact"]

    def test_not_exact_below(self):
        """Truncation is not exact when m < lambda."""
        for lam in [2, 5, 10]:
            data = drinfeld_polynomial_truncation(lam, lam - 1)
            assert not data["is_exact"]

    def test_truncated_degree(self):
        """Truncated degree = min(m, lambda)."""
        assert drinfeld_polynomial_truncation(5, 3)["truncated_degree"] == 3
        assert drinfeld_polynomial_truncation(5, 5)["truncated_degree"] == 5
        assert drinfeld_polynomial_truncation(5, 8)["truncated_degree"] == 5

    def test_weyl_dim(self):
        """Weyl module of truncation has dim = min(m, lambda) + 1."""
        assert drinfeld_polynomial_truncation(5, 3)["weyl_dim"] == 4
        assert drinfeld_polynomial_truncation(5, 5)["weyl_dim"] == 6


# ============================================================================
# Tail decay and convergence rate
# ============================================================================

class TestTailDecay:
    """Test tail (error) decay rate."""

    def test_tail_decay_values(self):
        """tail_dim(m) = depth - m for m <= depth, 0 for m > depth."""
        depth = 30
        data = tail_decay(5, max_m=35, depth=depth)
        for m, tail_dim in data:
            expected = max(depth - m, 0)
            assert tail_dim == expected

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_linear_decay(self, lam):
        """Error dimension decreases linearly."""
        assert verify_linear_decay(lam, max_m=40, depth=50)

    def test_decay_rate_one_per_level(self):
        """Each truncation level reduces error by exactly 1."""
        lam, depth = 5, 50
        prev = error_dimension(lam, 1, depth=depth)
        for m in range(2, 30):
            curr = error_dimension(lam, m, depth=depth)
            assert prev - curr == 1
            prev = curr


# ============================================================================
# Convergence summary
# ============================================================================

class TestConvergenceSummary:
    """Test the convergence summary report."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_summary_all_pass(self, lam):
        """All convergence diagnostics pass."""
        summary = convergence_summary(lam, max_m=30, depth=50)
        assert summary["projective_system_valid"]
        assert summary["inverse_limit_converges"]
        assert summary["mittag_leffler_holds"]

    def test_summary_milestones(self):
        """Milestones are computed correctly."""
        summary = convergence_summary(5, max_m=100, depth=100)
        # 50% of 100 = 50 weight spaces captured at m=50
        assert summary["milestones"]["50%"] == 50
        # 90% at m=90
        assert summary["milestones"]["90%"] == 90
        # 99% at m=99
        assert summary["milestones"]["99%"] == 99

    def test_summary_final_fraction(self):
        """Final fraction is max_m / depth."""
        summary = convergence_summary(5, max_m=20, depth=100)
        assert abs(summary["final_fraction"] - 0.20) < 1e-10


# ============================================================================
# Multi-lambda verification
# ============================================================================

class TestMultiLambda:
    """Test pro-Weyl convergence across multiple values of lambda."""

    def test_default_lambdas(self):
        """Default lambda values [0, 1, 2, 5, 10] all converge."""
        results = verify_pro_weyl_convergence(max_m=30, depth=50)
        for lam, summary in results.items():
            assert summary["projective_system_valid"], f"Failed at lam={lam}"
            assert summary["inverse_limit_converges"], f"Failed at lam={lam}"
            assert summary["mittag_leffler_holds"], f"Failed at lam={lam}"

    def test_negative_lambda(self):
        """Convergence holds for negative lambda (non-dominant Verma)."""
        results = verify_pro_weyl_convergence(
            lambdas=[-1, -3, -5], max_m=30, depth=50
        )
        for lam, summary in results.items():
            assert summary["projective_system_valid"], f"Failed at lam={lam}"
            assert summary["inverse_limit_converges"], f"Failed at lam={lam}"

    def test_large_lambda(self):
        """Convergence holds for large lambda."""
        results = verify_pro_weyl_convergence(
            lambdas=[20, 50], max_m=60, depth=80
        )
        for lam, summary in results.items():
            assert summary["inverse_limit_converges"], f"Failed at lam={lam}"


# ============================================================================
# Integration tests
# ============================================================================

class TestIntegration:
    """Integration tests combining multiple aspects."""

    def test_verify_all(self):
        """Complete verification suite passes."""
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_full_convergence_pipeline(self):
        """Full pipeline: build tower, check errors, verify limit.

        For lambda=3, depth=20:
          - Build W_1, ..., W_20
          - At each level, error is supported below lambda - 2m
          - dim(error) = 20 - m
          - lim_m W_m = M(3) up to depth 20
        """
        lam, depth = 3, 20
        tower = weyl_tower(lam, depth)

        # Tower has correct structure
        for i, W_m in enumerate(tower, start=1):
            # Dimension
            assert sum(W_m.values()) == i
            # Highest weight
            assert max(W_m.keys()) == lam

        # Error analysis
        for m in range(1, depth):
            err = error_character(lam, m, depth=depth)
            # Error nonneg
            for mult in err.values():
                assert mult >= 0
            # Error support
            if err:
                assert max(err.keys()) == lam - 2 * m
            # Error dimension
            assert sum(err.values()) == depth - m

        # Full convergence
        assert verify_inverse_limit(lam, max_m=depth, depth=depth)
        assert r1_lim_vanishing(lam, max_m=depth)

    def test_fd_weyl_embeds_in_tower(self):
        """The fd Weyl module V_lambda appears as W_{lambda+1} in the tower.

        This connects the Drinfeld polynomial picture (fd Weyl modules)
        to the pro-Weyl tower (truncations of the Verma).
        """
        for lam in [1, 2, 5]:
            fd = fd_weyl_character(lam)
            trunc = weyl_truncation(lam, lam + 1)
            assert formal_character_equal(fd, trunc)

    def test_consistency_with_baxter(self):
        """The Verma character used here matches sl2_baxter.py.

        Ensures our pro-Weyl machinery is consistent with the Baxter
        TQ computation framework.
        """
        for lam in [0, 1, 3, 5, 10]:
            # Large m truncation should match the Verma character
            depth = 30
            verma = sl2_verma_character(lam, depth=depth)
            W_full = weyl_truncation(lam, depth)
            assert formal_character_equal(W_full, verma)

    def test_error_monotonicity_across_lambda(self):
        """For fixed m and depth, error dimension is independent of lambda.

        This is because all sl_2 Verma modules have the same weight
        multiplicity pattern (all multiplicities 1), so the error
        dim(error(m)) = depth - m regardless of lambda.
        """
        depth = 50
        for m in [1, 5, 10, 20]:
            dims = set()
            for lam in [0, 1, 3, 7, 10]:
                dims.add(error_dimension(lam, m, depth=depth))
            assert len(dims) == 1, f"Error dims differ at m={m}: {dims}"
            assert dims.pop() == depth - m


# ============================================================================
# Edge cases
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary behavior."""

    def test_lam_zero(self):
        """lambda=0: Verma has weights 0, -2, -4, ...
        W_1 = {0:1}, the trivial module."""
        W1 = weyl_truncation(0, 1)
        assert W1 == {0: 1}

    def test_negative_m(self):
        """m <= 0 gives empty character."""
        assert weyl_truncation(5, -1) == {}
        assert weyl_truncation(5, 0) == {}

    def test_large_m(self):
        """Very large m still works."""
        W = weyl_truncation(0, 1000)
        assert sum(W.values()) == 1000
        assert max(W.keys()) == 0
        assert min(W.keys()) == 0 - 2 * 999

    def test_error_m_equals_one(self):
        """At m=1, error is M(lambda) minus the hw vector."""
        lam, depth = 5, 30
        err = error_character(lam, 1, depth=depth)
        assert max(err.keys()) == lam - 2
        assert sum(err.values()) == depth - 1

    def test_error_m_equals_depth(self):
        """At m = depth, error is empty."""
        lam, depth = 5, 20
        err = error_character(lam, depth, depth=depth)
        assert err == {}

    def test_tower_single_level(self):
        """Tower with max_m=1 has one entry."""
        tower = weyl_tower(5, 1)
        assert len(tower) == 1
        assert tower[0] == {5: 1}
