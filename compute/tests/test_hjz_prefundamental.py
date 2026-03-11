"""Tests for HJZ negative prefundamental modules — G5 for MC3.

Tests verify:
  1. Partition function correctness (known values and recurrence).
  2. L^-_a character has correct weight multiplicities (partition function).
  3. Drinfeld data consistency.
  4. Tensor product V_1 tensor L^- has correct character.
  5. TQ relation verified at K_0 level (character-level decomposition).
  6. Higher-spin tensor products V_n tensor L^-.
  7. Thick closure / compact generation evidence.
  8. Shifted Yangian category description.
  9. Integration tests combining multiple aspects.

References:
  - Hernandez-Jimbo (2012), Asymptotic representations
  - Zhang (2024), Shifted Yangians and polynomial R-matrices
  - Hernandez-Jimbo-Zhang (2025) [HJZ25]
  - yangians.tex, conj:shifted-prefundamental-generation
"""

import math

import pytest

from compute.lib.hjz_prefundamental import (
    # Partition function
    partition_function,
    # Prefundamental character
    prefundamental_character_sl2,
    prefundamental_character_generating_function,
    prefundamental_total_dim,
    # Drinfeld data
    prefundamental_drinfeld_data,
    # Tensor products
    prefundamental_tensor_V1,
    prefundamental_tensor_Vn,
    # TQ relation
    verify_prefundamental_tq_k0,
    # Thick closure
    thick_closure_test_sl2,
    # Category structure
    shifted_yangian_category_sl2,
    # Compact generation
    verify_compact_generation_evidence,
    # Full verification
    verify_all,
)
from compute.lib.sl2_baxter import (
    FormalCharacter,
    eval_module_V1,
    eval_module_Vn,
    formal_character_equal,
    sl2_verma_character,
    subtract_characters,
    sum_characters,
    tensor_product_characters,
)


# ============================================================================
# Partition function
# ============================================================================

class TestPartitionFunction:
    """Test the integer partition function p(n)."""

    @pytest.mark.parametrize("n,expected", [
        (0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 7),
        (6, 11), (7, 15), (8, 22), (9, 30), (10, 42),
    ])
    def test_known_values(self, n, expected):
        """p(n) matches known values from OEIS A000041."""
        assert partition_function(n) == expected

    def test_p_negative(self):
        """p(n) = 0 for n < 0."""
        for n in [-1, -5, -100]:
            assert partition_function(n) == 0

    def test_monotonicity(self):
        """p(n) is strictly increasing for n >= 1."""
        for n in range(1, 20):
            assert partition_function(n) >= partition_function(n - 1)
        # Strict after n=1: p(1)=1 = p(0)=1, but p(2)=2 > p(1)=1.
        for n in range(2, 20):
            assert partition_function(n) > partition_function(n - 1)

    def test_p_large(self):
        """p(20) = 627, p(50) = 204226."""
        assert partition_function(20) == 627
        assert partition_function(50) == 204226

    def test_generating_function_product(self):
        """Verify prod_{n>=1} 1/(1-x^n) gives partition numbers.

        We check this numerically: evaluate the truncated product at
        x = 0.1 and compare with the truncated sum.
        """
        x = 0.1
        depth = 30

        # Product form: prod_{n=1}^{depth} 1/(1-x^n)
        product = 1.0
        for n in range(1, depth + 1):
            product /= (1 - x ** n)

        # Sum form: sum_{k=0}^{depth-1} p(k) * x^k
        series_sum = sum(partition_function(k) * x ** k for k in range(depth))

        assert abs(product - series_sum) < 1e-10

    def test_caching(self):
        """Repeated calls return the same value (cache consistency)."""
        for _ in range(3):
            assert partition_function(10) == 42
            assert partition_function(5) == 7


# ============================================================================
# Prefundamental character
# ============================================================================

class TestPrefundamentalCharacter:
    """Test the formal character of L^-_a for Y(sl_2)."""

    def test_weight_zero_multiplicity(self):
        """Weight 0 has multiplicity p(0) = 1."""
        chi = prefundamental_character_sl2(0, depth=10)
        assert chi[0] == 1

    def test_weight_minus2_multiplicity(self):
        """Weight -2 has multiplicity p(1) = 1."""
        chi = prefundamental_character_sl2(0, depth=10)
        assert chi[-2] == 1

    def test_weight_minus4_multiplicity(self):
        """Weight -4 has multiplicity p(2) = 2."""
        chi = prefundamental_character_sl2(0, depth=10)
        assert chi[-4] == 2

    @pytest.mark.parametrize("k,expected", [
        (0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 7),
    ])
    def test_weight_multiplicities(self, k, expected):
        """Weight -2k has multiplicity p(k)."""
        chi = prefundamental_character_sl2(0, depth=k + 1)
        assert chi[-2 * k] == expected

    def test_character_independent_of_a(self):
        """The character is the same for different evaluation parameters."""
        chi_0 = prefundamental_character_sl2(0, depth=20)
        chi_1 = prefundamental_character_sl2(1, depth=20)
        chi_neg = prefundamental_character_sl2(-3.5, depth=20)
        assert chi_0 == chi_1
        assert chi_0 == chi_neg

    def test_all_weights_nonpositive_even(self):
        """All weights are nonpositive and even."""
        chi = prefundamental_character_sl2(0, depth=30)
        for w in chi.keys():
            assert w <= 0, f"Weight {w} is positive"
            assert w % 2 == 0, f"Weight {w} is odd"

    def test_all_multiplicities_positive(self):
        """All weight multiplicities are positive."""
        chi = prefundamental_character_sl2(0, depth=30)
        for w, m in chi.items():
            assert m > 0, f"Weight {w} has non-positive mult {m}"

    def test_highest_weight_is_zero(self):
        """The highest weight of L^- is 0."""
        chi = prefundamental_character_sl2(0, depth=10)
        assert max(chi.keys()) == 0

    def test_depth_controls_number_of_weights(self):
        """depth=d gives exactly d weights."""
        for d in [1, 5, 10, 20]:
            chi = prefundamental_character_sl2(0, depth=d)
            assert len(chi) == d


class TestPrefundamentalGeneratingFunction:
    """Test the generating function sequence."""

    def test_sequence_matches_character(self):
        """The GF sequence matches the character multiplicities."""
        depth = 20
        seq = prefundamental_character_generating_function(depth)
        chi = prefundamental_character_sl2(0, depth=depth)
        for k in range(depth):
            assert seq[k] == chi[-2 * k]

    def test_sequence_is_partition_numbers(self):
        """The sequence is exactly the partition numbers."""
        seq = prefundamental_character_generating_function(10)
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30]
        assert seq == expected

    def test_total_dim(self):
        """Total dimension is sum of partition numbers."""
        depth = 15
        total = prefundamental_total_dim(depth)
        expected = sum(partition_function(k) for k in range(depth))
        assert total == expected


# ============================================================================
# Drinfeld data
# ============================================================================

class TestDrinfeldData:
    """Test the Drinfeld polynomial/rational function data for L^-_a."""

    def test_type(self):
        """L^- is labeled as negative prefundamental."""
        data = prefundamental_drinfeld_data(0)
        assert data["type"] == "negative_prefundamental"

    def test_psi_degrees(self):
        """psi(u) = 1/(u-a) has numerator degree 0, denominator degree 1."""
        data = prefundamental_drinfeld_data(0)
        assert data["psi_numerator_degree"] == 0
        assert data["psi_denominator_degree"] == 1

    def test_denominator_roots(self):
        """The denominator root is at u = a."""
        for a in [0, 1, -2, 3.5]:
            data = prefundamental_drinfeld_data(a)
            assert data["psi_denominator_roots"] == [a]

    def test_highest_weight(self):
        """L^- has highest weight 0."""
        data = prefundamental_drinfeld_data(0)
        assert data["highest_weight"] == 0

    def test_infinite_dimensional(self):
        """L^- is infinite-dimensional."""
        data = prefundamental_drinfeld_data(0)
        assert data["is_finite_dimensional"] is False

    def test_is_highest_weight(self):
        """L^- is a highest-weight module."""
        data = prefundamental_drinfeld_data(0)
        assert data["is_highest_weight"] is True

    def test_dual_type(self):
        """The dual of L^- is L^+ with psi(u) = (u-a)."""
        data = prefundamental_drinfeld_data(0)
        dual = data["dual_type"]
        assert dual["type"] == "positive_prefundamental"
        assert dual["psi_numerator_degree"] == 1
        assert dual["psi_denominator_degree"] == 0

    def test_evaluation_parameter(self):
        """The evaluation parameter is stored correctly."""
        for a in [0, 1, -5, 2.7]:
            data = prefundamental_drinfeld_data(a)
            assert data["evaluation_parameter"] == a


# ============================================================================
# Tensor product with V_1
# ============================================================================

class TestTensorV1:
    """Test the tensor product V_1(a) tensor L^-_{a_L}."""

    def test_weight_1_multiplicity(self):
        """Weight 1 in V_1 tensor L^- has multiplicity p(0) = 1."""
        tensor = prefundamental_tensor_V1(0, 0, depth=20)
        assert tensor[1] == 1

    def test_weight_minus1_multiplicity(self):
        """Weight -1 in V_1 tensor L^- has multiplicity p(0) + p(1) = 2."""
        tensor = prefundamental_tensor_V1(0, 0, depth=20)
        assert tensor[-1] == 2

    def test_weight_minus3_multiplicity(self):
        """Weight -3 has mult p(1) + p(2) = 1 + 2 = 3."""
        tensor = prefundamental_tensor_V1(0, 0, depth=20)
        assert tensor[-3] == 3

    def test_weight_minus5_multiplicity(self):
        """Weight -5 has mult p(2) + p(3) = 2 + 3 = 5."""
        tensor = prefundamental_tensor_V1(0, 0, depth=20)
        assert tensor[-5] == 5

    @pytest.mark.parametrize("k", range(1, 10))
    def test_weight_pattern(self, k):
        """Weight -(2k-1) has mult p(k-1) + p(k)."""
        tensor = prefundamental_tensor_V1(0, 0, depth=k + 2)
        w = -(2 * k - 1)
        expected = partition_function(k - 1) + partition_function(k)
        assert tensor[w] == expected, (
            f"At weight {w}: got {tensor[w]}, expected {expected}"
        )

    def test_all_weights_odd(self):
        """All weights in V_1 tensor L^- are odd."""
        tensor = prefundamental_tensor_V1(0, 0, depth=30)
        for w in tensor.keys():
            assert w % 2 != 0, f"Weight {w} is even"

    def test_highest_weight(self):
        """Highest weight of V_1 tensor L^- is 1."""
        tensor = prefundamental_tensor_V1(0, 0, depth=20)
        assert max(tensor.keys()) == 1

    def test_independent_of_parameters(self):
        """The character is independent of the evaluation parameters."""
        t1 = prefundamental_tensor_V1(0, 0, depth=15)
        t2 = prefundamental_tensor_V1(1, 2, depth=15)
        t3 = prefundamental_tensor_V1(-3, 5, depth=15)
        assert t1 == t2
        assert t1 == t3


class TestTensorVn:
    """Test the tensor product V_n tensor L^- for higher n."""

    def test_V2_tensor_L_highest_weight(self):
        """Highest weight of V_2 tensor L^- is 2."""
        tensor = prefundamental_tensor_Vn(2, 0, 0, depth=20)
        assert max(tensor.keys()) == 2

    def test_V2_tensor_L_weight_parity(self):
        """V_2 tensor L^- has even weights (since V_2 has even weights)."""
        tensor = prefundamental_tensor_Vn(2, 0, 0, depth=20)
        for w in tensor.keys():
            assert w % 2 == 0, f"Weight {w} is odd in V_2 tensor L^-"

    def test_V3_tensor_L_weight_parity(self):
        """V_3 tensor L^- has odd weights."""
        tensor = prefundamental_tensor_Vn(3, 0, 0, depth=20)
        for w in tensor.keys():
            assert w % 2 != 0, f"Weight {w} is even in V_3 tensor L^-"

    def test_Vn_tensor_L_highest_weight(self):
        """V_n tensor L^- has highest weight n."""
        for n in range(1, 6):
            tensor = prefundamental_tensor_Vn(n, 0, 0, depth=10)
            assert max(tensor.keys()) == n

    def test_V1_tensor_matches(self):
        """V_1 tensor L^- from prefundamental_tensor_Vn matches prefundamental_tensor_V1."""
        t1 = prefundamental_tensor_V1(0, 0, depth=20)
        t2 = prefundamental_tensor_Vn(1, 0, 0, depth=20)
        assert t1 == t2

    def test_V0_tensor_is_L(self):
        """V_0 tensor L^- = L^- (tensoring with trivial rep)."""
        L_char = prefundamental_character_sl2(0, depth=20)
        tensor = prefundamental_tensor_Vn(0, 0, 0, depth=20)
        assert tensor == L_char

    def test_tensor_dimension(self):
        """dim(V_n tensor L^-) = (n+1) * dim(L^-)."""
        depth = 15
        L_dim = prefundamental_total_dim(depth)
        for n in range(5):
            tensor = prefundamental_tensor_Vn(n, 0, 0, depth=depth)
            tensor_dim = sum(tensor.values())
            assert tensor_dim == (n + 1) * L_dim


# ============================================================================
# TQ relation at K_0 level
# ============================================================================

class TestTQRelation:
    """Test the TQ relation for prefundamental modules at the character level."""

    def test_two_term_decomposition(self):
        """V_1 tensor L^- decomposes as sum of two shifted L^- at character level."""
        tq = verify_prefundamental_tq_k0(0, 0, depth=30)
        assert tq["two_term_decomposition_matches"]

    def test_all_weights_odd(self):
        """All weights in the tensor product are odd."""
        tq = verify_prefundamental_tq_k0(0, 0, depth=30)
        assert tq["all_weights_odd"]

    def test_multiplicity_pattern(self):
        """Multiplicities follow the p(k-1) + p(k) pattern."""
        tq = verify_prefundamental_tq_k0(0, 0, depth=30)
        assert tq["multiplicity_pattern_correct"]

    def test_weight_1_is_correct(self):
        """Weight 1 has multiplicity 1."""
        tq = verify_prefundamental_tq_k0(0, 0, depth=20)
        assert tq["weight_1_correct"]

    def test_tq_at_different_parameters(self):
        """TQ relation holds for various evaluation parameters."""
        for a_V, a_L in [(0, 0), (1, 0), (0, 1), (2, -3)]:
            tq = verify_prefundamental_tq_k0(a_V, a_L, depth=20)
            assert tq["two_term_decomposition_matches"], (
                f"TQ failed for a_V={a_V}, a_L={a_L}"
            )

    def test_tq_large_depth(self):
        """TQ relation holds at large depth (stress test)."""
        tq = verify_prefundamental_tq_k0(0, 0, depth=60)
        assert tq["two_term_decomposition_matches"]
        assert tq["multiplicity_pattern_correct"]

    def test_explicit_two_term_decomposition(self):
        """Explicitly construct the two shifted L^- and verify the sum.

        L^-_+(odd): weight 1-2k has mult p(k) for k >= 0.
        L^-_-(odd): weight -1-2k has mult p(k) for k >= 0.
        Sum at weight -(2m-1): p(m) + p(m-1). This should match V_1 tensor L^-.
        """
        depth = 25
        L_plus = {1 - 2 * k: partition_function(k) for k in range(depth)}
        L_minus = {-1 - 2 * k: partition_function(k) for k in range(depth)}
        rhs = sum_characters(L_plus, L_minus)

        lhs = prefundamental_tensor_V1(0, 0, depth=depth)
        assert formal_character_equal(lhs, rhs)


# ============================================================================
# Thick closure / compact generation
# ============================================================================

class TestThickClosure:
    """Test thick closure properties for conj:shifted-prefundamental-generation."""

    def test_fd_modules_in_closure(self):
        """Finite-dimensional modules are in the thick closure (trivially)."""
        result = thick_closure_test_sl2(max_dim=6)
        assert result["fd_modules_in_closure"]

    def test_prefundamental_in_closure(self):
        """Prefundamental is in the thick closure (trivially)."""
        result = thick_closure_test_sl2(max_dim=6)
        assert result["prefundamental_in_closure"]

    def test_tq_relation_match(self):
        """The TQ relation at the character level matches."""
        result = thick_closure_test_sl2(max_dim=6)
        assert result["tq_relation_character_match"]

    def test_exact_triangle_evidence(self):
        """The exact triangle evidence is positive."""
        result = thick_closure_test_sl2(max_dim=6)
        assert result["exact_triangle_evidence"]

    def test_excess_starts_at_k2(self):
        """The excess of L^- over Verma starts at weight level k=2."""
        result = thick_closure_test_sl2(max_dim=6)
        for lam, analysis in result["verma_analysis"].items():
            assert analysis["excess_starts_at_k"] == 2

    def test_first_excess_is_1(self):
        """At k=2, the excess is p(2)-1 = 1."""
        result = thick_closure_test_sl2(max_dim=6)
        for lam, analysis in result["verma_analysis"].items():
            assert analysis["first_excess"] == 1

    def test_dimension_comparison(self):
        """Partition function exceeds Verma multiplicity starting at k=2."""
        result = thick_closure_test_sl2(max_dim=6)
        dim_comp = result["dimension_comparison"]
        assert dim_comp["excess_first_nonzero_k"] == 2
        # Check that excess dims match p(k) - 1 for k >= 2
        excess = dim_comp["excess_dims_first_10"]
        partition = dim_comp["partition_dims_first_10"]
        for k in range(2, 10):
            assert excess[k] == partition[k] - 1


class TestCompactGeneration:
    """Test compact generation evidence."""

    def test_layer1_tq(self):
        """Layer 1: TQ character match."""
        ev = verify_compact_generation_evidence(max_weight=15)
        assert ev["layer1_tq_character_match"]
        assert ev["layer1_tq_all_odd"]
        assert ev["layer1_tq_pattern_correct"]

    def test_layer2_verma(self):
        """Layer 2: All tested Verma modules are K_0-expressible."""
        ev = verify_compact_generation_evidence(max_weight=15)
        for lam, data in ev["layer2_verma_data"].items():
            assert data["excess_expressible"]

    def test_layer3_iterated_tensor(self):
        """Layer 3: V_1^2 tensor L^- has even weights."""
        ev = verify_compact_generation_evidence(max_weight=15)
        assert ev["layer3_V1_V1_L_even_weights"]

    def test_layer3_weight_0_mult(self):
        """Layer 3: V_1^2 tensor L^- at weight 0 has predicted multiplicity.

        V_1^2 tensor L^- at weight 0:
        V_1 has weights +1, -1. V_1^2 has weights +2(1), 0(2), -2(1).
        Convolving with L^-:
          weight 0: (+2 x -2)[p(1)] + (0 x 0)[2*p(0)] + (-2 x +2)[impossible, no +2 in L^-]
          Actually L^- has weight 0 and below. So:
            weight 0 of V_1^2 tensor L^-:
              = (weight 2 of V_1^2) * (weight -2 of L^-)
                + (weight 0 of V_1^2) * (weight 0 of L^-)
              = 1 * p(1) + 2 * p(0)
              = 1 + 2 = 3
        Wait, we also need:
              + (weight -2 of V_1^2) * (weight +2 of L^-)
            But L^- has no positive weights. So total = 1*1 + 2*1 = 3.

        But V_1^2 also has weight -2 with mult 1. And L^- has weight +2? No.
        L^- has weights 0, -2, -4, ... So weight +2 doesn't exist in L^-.

        Total at weight 0: 1*p(1) + 2*p(0) = 1 + 2 = 3.
        """
        ev = verify_compact_generation_evidence(max_weight=15)
        assert ev["layer3_V1_V1_L_weight_0"] == 3

    def test_layer4_growth(self):
        """Layer 4: Hardy-Ramanujan asymptotic is approached."""
        ev = verify_compact_generation_evidence(max_weight=15)
        assert ev["layer4_hr_asymptotic_convergence"]

    def test_summary_positive(self):
        """Overall summary is positive evidence."""
        ev = verify_compact_generation_evidence(max_weight=15)
        summary = ev["summary"]
        assert summary["tq_verified"]
        assert summary["verma_expressible"]
        assert summary["iterated_tensor_consistent"]


# ============================================================================
# Category structure
# ============================================================================

class TestShiftedYangianCategory:
    """Test the shifted Yangian category description."""

    def test_category_name(self):
        """Category has the correct name."""
        cat = shifted_yangian_category_sl2()
        assert "sl_2" in cat["name"] or "sl(2)" in cat["name"]

    def test_rank(self):
        """sl_2 has rank 1."""
        cat = shifted_yangian_category_sl2()
        assert cat["rank"] == 1

    def test_simple_objects(self):
        """Simple objects include V_n, L^+, L^-."""
        cat = shifted_yangian_category_sl2()
        simples = cat["simple_objects"]
        assert len(simples) == 3
        assert any("V_n" in s for s in simples)
        assert any("L^+" in s for s in simples)
        assert any("L^-" in s for s in simples)

    def test_standard_objects(self):
        """Standard objects include Verma modules."""
        cat = shifted_yangian_category_sl2()
        standards = cat["standard_objects"]
        assert any("Verma" in s or "M(" in s for s in standards)

    def test_conjecture_reference(self):
        """The conjecture reference is present."""
        cat = shifted_yangian_category_sl2()
        conjecture_str = cat["generators_for_thick_closure"]["conjecture"]
        assert "shifted-prefundamental-generation" in conjecture_str

    def test_exact_sequences(self):
        """Key exact sequences are listed."""
        cat = shifted_yangian_category_sl2()
        ses_list = cat["key_exact_sequences"]
        assert len(ses_list) >= 2
        # Baxter TQ for Verma
        assert any("M(lam" in s for s in ses_list)
        # Baxter TQ for prefundamentals
        assert any("L^-" in s for s in ses_list)


# ============================================================================
# Comparison with Verma module TQ
# ============================================================================

class TestPrefundamentalVsVerma:
    """Compare prefundamental TQ with the Verma module TQ relation."""

    def test_verma_tq_mults_are_one(self):
        """For Verma modules, V_1 tensor M(lam) has mults 1 or 2 only.

        At weight lam+1: mult 1. At lower weights: mult 2 (from two summands).
        """
        from compute.lib.sl2_baxter import baxter_tq_k0
        lhs, rhs = baxter_tq_k0(3, depth=20)
        # Top weight 4: mult 1
        assert lhs[4] == 1
        # Weight 2: mult 2
        assert lhs[2] == 2
        # Weight 0: mult 2
        assert lhs[0] == 2

    def test_prefundamental_tq_mults_grow(self):
        """For prefundamentals, V_1 tensor L^- has growing multiplicities.

        This is the key difference: Verma mults are bounded by 2,
        but prefundamental tensor mults grow as p(k) + p(k-1).
        """
        tensor = prefundamental_tensor_V1(0, 0, depth=20)
        mults = [tensor.get(-(2 * k - 1), 0) for k in range(1, 15)]
        # Should be 2, 3, 5, 8, 12, 18, 26, 37, 52, 72, ...
        expected = [partition_function(k - 1) + partition_function(k) for k in range(1, 15)]
        assert mults == expected

        # Verify growth: multiplicities strictly increase after the first
        for i in range(1, len(mults)):
            assert mults[i] > mults[i - 1]

    def test_different_weight_parities(self):
        """Verma tensor has weights of same parity as lam+1;
        prefundamental tensor has only odd weights."""
        # Verma M(3) tensor V_1: weights 4, 2, 0, -2, ... (even)
        from compute.lib.sl2_baxter import baxter_tq_k0
        lhs_verma, _ = baxter_tq_k0(3, depth=20)
        assert all(w % 2 == 0 for w in lhs_verma.keys())

        # L^- tensor V_1: all odd
        tensor_prefund = prefundamental_tensor_V1(0, 0, depth=20)
        assert all(w % 2 != 0 for w in tensor_prefund.keys())


# ============================================================================
# Integration / comprehensive
# ============================================================================

class TestComprehensive:
    """Integration tests combining multiple aspects."""

    def test_verify_all(self):
        """All verification checks pass."""
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_character_sum_rule(self):
        """The total dimension of V_n tensor L^- equals (n+1) * dim(L^-).

        This is a basic check that tensor product characters are computed
        correctly: dim(A tensor B) = dim(A) * dim(B).
        """
        depth = 20
        L_dim = prefundamental_total_dim(depth)
        for n in range(5):
            tensor = prefundamental_tensor_Vn(n, 0, 0, depth=depth)
            assert sum(tensor.values()) == (n + 1) * L_dim

    def test_prefundamental_vs_verma_at_k0_and_k1(self):
        """At weight levels k=0 and k=1, L^- and M(0) agree.

        Both have mult 1 at weight 0 and mult 1 at weight -2.
        They diverge at weight -4 (L^- has 2, M(0) has 1).
        """
        L_char = prefundamental_character_sl2(0, depth=10)
        M_char = sl2_verma_character(0, depth=10)

        # Agreement at k=0, k=1
        assert L_char[0] == M_char[0] == 1
        assert L_char[-2] == M_char[-2] == 1

        # Divergence at k=2
        assert L_char[-4] == 2
        assert M_char[-4] == 1

    def test_tq_prefundamental_generalizes_verma_tq(self):
        """The prefundamental TQ relation is a generalization of the Verma TQ.

        For Verma modules: [V_1]*[M(lam)] = [M(lam+1)] + [M(lam-1)]
        For prefundamentals: [V_1]*[L^-] decomposes as shifted L^- sum.

        Both are instances of the Baxter TQ relation in K_0(O).
        We verify both hold simultaneously.
        """
        from compute.lib.sl2_baxter import verify_baxter_tq_k0

        # Verma TQ
        for lam in range(6):
            assert verify_baxter_tq_k0(lam)

        # Prefundamental TQ
        tq = verify_prefundamental_tq_k0(0, 0, depth=30)
        assert tq["two_term_decomposition_matches"]

    def test_iterated_tq_builds_lattice(self):
        """Iterated application of V_1-tensoring builds the weight lattice.

        Starting from L^- (even weights), one V_1-tensor gives odd weights,
        two gives even again. This alternation covers the full weight lattice.
        """
        L_char = prefundamental_character_sl2(0, depth=20)
        V1 = eval_module_V1()

        T1 = tensor_product_characters(V1, L_char)
        T2 = tensor_product_characters(V1, T1)

        # T1 on odd lattice, T2 on even lattice
        assert all(w % 2 != 0 for w in T1.keys())
        assert all(w % 2 == 0 for w in T2.keys())

        # T2 at weight 0 has multiplicity >= 1 (the lattice point is covered)
        assert T2.get(0, 0) >= 1


# ============================================================================
# Edge cases
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary tests."""

    def test_depth_1(self):
        """depth=1 gives just the weight-0 space."""
        chi = prefundamental_character_sl2(0, depth=1)
        assert chi == {0: 1}

    def test_depth_0(self):
        """depth=0 gives empty character."""
        chi = prefundamental_character_sl2(0, depth=0)
        assert chi == {}

    def test_tensor_depth_1(self):
        """V_1 tensor L^-(depth=1) = V_1 (just the weight-0 part of L^-)."""
        tensor = prefundamental_tensor_V1(0, 0, depth=1)
        # L^- at depth 1 has only weight 0 with mult 1.
        # V_1 tensor {0: 1} = {1: 1, -1: 1}.
        assert tensor == {1: 1, -1: 1}

    def test_large_partition(self):
        """Partition function at large values is positive and large."""
        p100 = partition_function(100)
        assert p100 > 0
        assert p100 == 190569292  # known value

    def test_prefundamental_not_verma(self):
        """L^- is NOT a Verma module (multiplicities differ at k >= 2)."""
        L_char = prefundamental_character_sl2(0, depth=20)
        M_char = sl2_verma_character(0, depth=20)
        # They agree at k=0,1 but differ at k=2
        assert L_char[-4] != M_char[-4]
        assert L_char[-4] == 2
        assert M_char[-4] == 1
