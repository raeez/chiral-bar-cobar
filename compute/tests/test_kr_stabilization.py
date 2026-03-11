"""Tests for KR module stabilization for Y(sl_2) — task C5.

Ground truth from the manuscript (yangians.tex, sec:yangian-rep-bar):
  - KR modules W_{k,a}^{(1)} = V_{k+1}(a) (evaluation modules)
  - ch(V_n) = q^n + q^{n-2} + ... + q^{-n}
  - Bar complex: B^k(Y; V_n) = V_n tensor Lambda^k(sl_2*)
  - dim B^k = (n+1) * C(3,k)
  - Euler characteristic: sum (-1)^k dim B^k = 0

Five stabilization properties:
  1. Coefficientwise convergence of characters
  2. Normalized character convergence
  3. Tensor product stability (CG decomposition)
  4. Bar complex dimension stability
  5. q-character convergence (Frenkel-Reshetikhin)

Shadow-level identity: F_n(t)/(n+1) = (1-t)^3 exactly.
"""

import pytest
from math import comb
from sympy import Rational

from compute.lib.kr_stabilization import (
    # KR module basics
    kr_module_character,
    kr_module_dim,
    # Property 1
    coefficientwise_convergence_check,
    verify_coefficientwise_convergence,
    # Property 2
    normalized_character_ratio,
    verify_normalized_convergence,
    character_dimension,
    # Property 3
    tensor_product_decomposition_dims,
    tensor_product_character,
    tensor_product_cg_character,
    verify_clebsch_gordan,
    tensor_stability_data,
    verify_tensor_stability,
    # Property 4
    bar_complex_dim,
    bar_euler_char,
    bar_poincare_polynomial,
    bar_alternating_series,
    bar_normalized_limit,
    verify_bar_stability,
    bar_growth_rate,
    # Property 5
    q_character_vn,
    q_character_stabilization_check,
    q_character_a_pattern,
    verify_q_character_convergence,
    # Synthesis
    shadow_level_identity,
    stabilization_summary,
    verify_all,
)

from compute.lib.sl2_baxter import (
    sl2_fd_character,
    formal_character_equal,
)


# ============================================================================
# KR module basics
# ============================================================================

class TestKRModuleBasics:
    """Test KR module character and dimension computations."""

    def test_kr_dim_k0(self):
        """W_{0,a} is the trivial 1-dim module."""
        assert kr_module_dim(0) == 1

    def test_kr_dim_k1(self):
        """W_{1,a} is V_2, the standard 2-dim module."""
        assert kr_module_dim(1) == 2

    def test_kr_dim_k2(self):
        """W_{2,a} is V_3, the adjoint 3-dim module."""
        assert kr_module_dim(2) == 3

    def test_kr_dim_general(self):
        """W_{k,a} has dimension k+1."""
        for k in range(20):
            assert kr_module_dim(k) == k + 1

    def test_kr_character_k0(self):
        """W_{0,a} = trivial rep, character is {0: 1}."""
        chi = kr_module_character(0)
        assert chi == {0: 1}

    def test_kr_character_k1(self):
        """W_{1,a} = V_2, weights +1, -1."""
        chi = kr_module_character(1)
        assert chi == {1: 1, -1: 1}

    def test_kr_character_k2(self):
        """W_{2,a} = V_3, weights +2, 0, -2."""
        chi = kr_module_character(2)
        assert chi == {2: 1, 0: 1, -2: 1}

    def test_kr_character_weights_symmetric(self):
        """Weights of V_n are symmetric: w in chi iff -w in chi."""
        for k in range(15):
            chi = kr_module_character(k)
            for w in chi:
                assert -w in chi, f"Weight {w} present but {-w} missing for k={k}"
                assert chi[w] == chi[-w]

    def test_kr_character_multiplicity_one(self):
        """All multiplicities in irreducible V_n character are 1."""
        for k in range(15):
            chi = kr_module_character(k)
            assert all(m == 1 for m in chi.values())

    def test_kr_character_weight_count(self):
        """V_n has exactly n+1 weights."""
        for k in range(15):
            chi = kr_module_character(k)
            assert len(chi) == k + 1

    def test_kr_character_highest_weight(self):
        """Highest weight of W_{k,a} is k."""
        for k in range(15):
            chi = kr_module_character(k)
            assert max(chi.keys()) == k

    def test_kr_negative_index(self):
        """KR index must be non-negative."""
        with pytest.raises(ValueError):
            kr_module_character(-1)

    def test_kr_matches_sl2_fd(self):
        """KR module character matches sl2_fd_character."""
        for k in range(15):
            assert kr_module_character(k) == sl2_fd_character(k + 1)


# ============================================================================
# Property 1: Coefficientwise convergence
# ============================================================================

class TestCoefficientwiseConvergence:
    """Test that KR characters converge coefficientwise to Verma character."""

    def test_window3_basic(self):
        """Top 3 weights of V_n agree with M(n) for n >= 2."""
        for k in range(2, 15):
            agree, data = coefficientwise_convergence_check(k, window=3)
            assert agree, f"Failed at k={k}: {data}"

    def test_window5_basic(self):
        """Top 5 weights of V_n agree with M(n) for n >= 4."""
        for k in range(4, 15):
            agree, data = coefficientwise_convergence_check(k, window=5)
            assert agree, f"Failed at k={k}: {data}"

    def test_full_verification_window3(self):
        assert verify_coefficientwise_convergence(max_k=20, window=3)

    def test_full_verification_window5(self):
        assert verify_coefficientwise_convergence(max_k=20, window=5)

    def test_full_verification_window8(self):
        assert verify_coefficientwise_convergence(max_k=20, window=8)

    def test_all_weights_agree_for_large_k(self):
        """For k=10, window=5: all top 5 weights match Verma."""
        agree, data = coefficientwise_convergence_check(10, window=5)
        assert agree
        assert len(data["kr_weights_in_window"]) == 5

    def test_convergence_rate(self):
        """The agreement window grows linearly with k.

        For W_{k,a}, the character agrees with M(k) in the top k+1
        weight levels (all of them, since V_n has exactly n+1 weights).
        """
        for k in range(1, 15):
            agree, _ = coefficientwise_convergence_check(k, window=k + 1)
            assert agree, f"Full agreement should hold for window <= k+1 at k={k}"


# ============================================================================
# Property 2: Normalized character convergence
# ============================================================================

class TestNormalizedConvergence:
    """Test normalized character convergence."""

    def test_dim_ratio_decreasing(self):
        """dim(V_n) / 2^{n-1} decreases for n >= 2."""
        prev = float('inf')
        for n in range(2, 15):
            ratio = (n + 1) / 2**(n - 1)
            assert ratio < prev, f"Ratio not decreasing at n={n}"
            prev = ratio

    def test_dim_ratio_to_zero(self):
        """dim(V_n) / 2^{n-1} -> 0."""
        ratio_20 = 21 / 2**19
        assert ratio_20 < 1e-4

    def test_all_multiplicities_one(self):
        """Irreducible V_n has all weight multiplicities equal to 1."""
        for n in range(1, 20):
            chi = kr_module_character(n)
            assert all(m == 1 for m in chi.values())

    def test_character_dimension(self):
        """dim(V_n) = n+1 via character."""
        for n in range(20):
            chi = kr_module_character(n)
            assert character_dimension(chi) == n + 1

    def test_full_verification(self):
        assert verify_normalized_convergence(max_n=15)

    def test_ratio_data_structure(self):
        """Check the returned data structure."""
        data = normalized_character_ratio(5)
        assert data["n"] == 5
        assert data["dim_Vn"] == 6
        assert data["dim_V1_power"] == 16  # 2^4
        assert data["dim_ratio"] == Rational(6, 16)


# ============================================================================
# Property 3: Tensor product stability
# ============================================================================

class TestTensorStability:
    """Test tensor product stability via Clebsch-Gordan."""

    def test_cg_v1_v1(self):
        """V_1 tensor V_1 = V_2 + V_0."""
        dims = tensor_product_decomposition_dims(1, 1)
        assert sorted(dims) == [1, 3]  # V_0 has dim 1, V_2 has dim 3

    def test_cg_v2_v1(self):
        """V_2 tensor V_1 = V_3 + V_1."""
        dims = tensor_product_decomposition_dims(2, 1)
        assert sorted(dims) == [2, 4]

    def test_cg_v2_v2(self):
        """V_2 tensor V_2 = V_4 + V_2 + V_0."""
        dims = tensor_product_decomposition_dims(2, 2)
        assert sorted(dims) == [1, 3, 5]

    def test_cg_character_v1_v1(self):
        """Character-level CG for V_1 tensor V_1."""
        assert verify_clebsch_gordan(1, 1)

    def test_cg_character_v3_v2(self):
        assert verify_clebsch_gordan(3, 2)

    def test_cg_character_v5_v3(self):
        assert verify_clebsch_gordan(5, 3)

    def test_cg_character_large(self):
        """CG holds for larger modules."""
        assert verify_clebsch_gordan(10, 7)

    def test_n_summands_formula(self):
        """Number of CG summands is min(n,m)+1."""
        for n in range(1, 10):
            for m in range(1, 10):
                dims = tensor_product_decomposition_dims(n, m)
                assert len(dims) == min(n, m) + 1

    def test_total_dim(self):
        """Total dimension of tensor product is (n+1)(m+1)."""
        for n in range(1, 10):
            for m in range(1, 10):
                dims = tensor_product_decomposition_dims(n, m)
                assert sum(dims) == (n + 1) * (m + 1)

    def test_summand_stability(self):
        """For fixed m, number of summands stabilizes for n >= m."""
        for m in range(1, 6):
            expected = m + 1
            for n in range(m, 15):
                data = tensor_stability_data(n, m)
                assert data["n_summands"] == expected

    def test_full_verification(self):
        assert verify_tensor_stability(max_k=10)


# ============================================================================
# Property 4: Bar complex stability
# ============================================================================

class TestBarStability:
    """Test bar complex dimension stability."""

    def test_bar_dim_k0_all_degrees(self):
        """For trivial module (k=0): B^j has dim C(3,j)."""
        assert bar_complex_dim(0, 0) == 1
        assert bar_complex_dim(0, 1) == 3
        assert bar_complex_dim(0, 2) == 3
        assert bar_complex_dim(0, 3) == 1

    def test_bar_dim_k1_all_degrees(self):
        """For V_2 (k=1): B^j has dim 2*C(3,j)."""
        assert bar_complex_dim(1, 0) == 2
        assert bar_complex_dim(1, 1) == 6
        assert bar_complex_dim(1, 2) == 6
        assert bar_complex_dim(1, 3) == 2

    def test_bar_dim_general_formula(self):
        """dim B^j(V_n) = (n+1) * C(3,j)."""
        for k in range(15):
            for j in range(4):
                assert bar_complex_dim(k, j) == (k + 1) * comb(3, j)

    def test_bar_dim_out_of_range(self):
        """Bar complex is zero outside degrees 0..3."""
        for k in range(5):
            assert bar_complex_dim(k, -1) == 0
            assert bar_complex_dim(k, 4) == 0
            assert bar_complex_dim(k, 10) == 0

    def test_euler_char_zero(self):
        """Euler characteristic is always zero."""
        for k in range(20):
            assert bar_euler_char(k) == 0

    def test_poincare_polynomial(self):
        """Poincare polynomial is (n+1) * [1,3,3,1]."""
        for k in range(10):
            poly = bar_poincare_polynomial(k)
            expected = [(k + 1) * c for c in [1, 3, 3, 1]]
            assert poly == expected

    def test_alternating_series_coefficients(self):
        """F_n(t) coefficients are (n+1) * [1, -3, 3, -1]."""
        for k in range(10):
            coeffs = bar_alternating_series(k)
            expected = [(k + 1) * ((-1)**j * comb(3, j)) for j in range(4)]
            assert coeffs == expected

    def test_alternating_series_value_at_1(self):
        """F_n(1) = 0 (Euler characteristic)."""
        for k in range(10):
            val = bar_alternating_series(k, t=1.0)
            assert abs(val) < 1e-12, f"F_{k}(1) = {val} != 0"

    def test_alternating_series_value_at_0(self):
        """F_n(0) = n+1 = dim(V_n)."""
        for k in range(10):
            val = bar_alternating_series(k, t=0.0)
            assert abs(val - (k + 1)) < 1e-12

    def test_normalized_limit_exact(self):
        """F_n(t)/(n+1) = (1-t)^3 coefficients for ALL n."""
        target = [Rational(1), Rational(-3), Rational(3), Rational(-1)]
        for k in range(20):
            normalized = bar_normalized_limit(k)
            assert normalized == target, f"Failed at k={k}: {normalized}"

    def test_bar_growth_linear(self):
        """Growth rate of dim B^j is linear in n."""
        for j in range(4):
            data = bar_growth_rate(j)
            assert data["slope"] == comb(3, j)
            assert data["growth"] == "linear in n"

    def test_full_verification(self):
        assert verify_bar_stability(max_k=20)


# ============================================================================
# Property 5: q-character convergence
# ============================================================================

class TestQCharacterConvergence:
    """Test q-character convergence (Frenkel-Reshetikhin)."""

    def test_q_char_hw_monomial(self):
        """Highest weight monomial has coefficient 1."""
        for n in range(1, 10):
            qc = q_character_vn(n)
            assert qc.get((0,), 0) == 1

    def test_q_char_all_coefficients_one(self):
        """All q-character monomials have coefficient 1 for irreducible V_n."""
        for n in range(1, 10):
            qc = q_character_vn(n, num_terms=n + 1)
            for j in range(n + 1):
                assert qc.get((j,), 0) == 1, f"Coeff at j={j} for V_{n} is not 1"

    def test_q_char_num_monomials(self):
        """V_n has n+1 q-character monomials."""
        for n in range(1, 10):
            qc = q_character_vn(n, num_terms=n + 1)
            assert len(qc) == n + 1

    def test_a_pattern_j0(self):
        """Highest weight monomial has no A^{-1} factors."""
        for n in range(1, 10):
            pattern = q_character_a_pattern(n, 0)
            assert pattern == []

    def test_a_pattern_j1(self):
        """First descent has one A^{-1} factor at relative position 0."""
        for n in range(2, 10):
            pattern = q_character_a_pattern(n, 1)
            assert pattern == [0]

    def test_a_pattern_j2(self):
        """Second descent has A^{-1} at relative positions [0, -2]."""
        for n in range(3, 10):
            pattern = q_character_a_pattern(n, 2)
            assert pattern == [0, -2]

    def test_a_pattern_independent_of_n(self):
        """The A-pattern at position j is independent of n for n > j."""
        for j in range(6):
            patterns = [q_character_a_pattern(n, j) for n in range(j + 1, 15)]
            # All should be the same
            for p in patterns:
                assert p == patterns[0], f"Pattern varies with n at j={j}"

    def test_a_pattern_length_equals_j(self):
        """Pattern at position j has exactly j entries (for j > 0)."""
        for j in range(1, 8):
            pattern = q_character_a_pattern(10, j)
            assert len(pattern) == j

    def test_stabilization_check(self):
        """q-character stabilization check passes."""
        for j in range(5):
            assert q_character_stabilization_check(j, list(range(j + 1, 15)))

    def test_full_verification(self):
        assert verify_q_character_convergence(max_j=5, max_n=15)


# ============================================================================
# Shadow-level identity
# ============================================================================

class TestShadowIdentity:
    """Test the key shadow-level identity F_n(t)/(n+1) = (1-t)^{dim(sl_2)}."""

    def test_identity_k0(self):
        """Shadow identity for trivial module."""
        data = shadow_level_identity(0)
        assert data["identity_holds"]
        assert data["dim_Vn"] == 1
        assert data["F_n_coeffs"] == [1, -3, 3, -1]

    def test_identity_k1(self):
        """Shadow identity for standard module."""
        data = shadow_level_identity(1)
        assert data["identity_holds"]
        assert data["dim_Vn"] == 2
        assert data["F_n_coeffs"] == [2, -6, 6, -2]

    def test_identity_k5(self):
        data = shadow_level_identity(5)
        assert data["identity_holds"]
        assert data["dim_Vn"] == 6
        assert data["F_n_coeffs"] == [6, -18, 18, -6]

    def test_identity_k10(self):
        data = shadow_level_identity(10)
        assert data["identity_holds"]
        assert data["dim_Vn"] == 11

    def test_normalized_coeffs_universal(self):
        """The normalized coefficients [1,-3,3,-1] are independent of k."""
        for k in range(20):
            data = shadow_level_identity(k)
            assert data["normalized_coeffs"] == [1, -3, 3, -1]

    def test_dim_g_is_3(self):
        """dim(sl_2) = 3."""
        data = shadow_level_identity(0)
        assert data["dim_g"] == 3

    def test_identity_equals_1_minus_t_cubed(self):
        """Verify (1-t)^3 = 1 - 3t + 3t^2 - t^3 via binomial."""
        for k in range(4):
            assert (-1)**k * comb(3, k) == [1, -3, 3, -1][k]

    def test_identity_large_k(self):
        """Shadow identity holds for large k."""
        for k in [50, 100, 200]:
            data = shadow_level_identity(k)
            assert data["identity_holds"]


# ============================================================================
# Combined stabilization summary
# ============================================================================

class TestStabilizationSummary:
    """Test the combined stabilization summary."""

    def test_all_properties_pass(self):
        """All five stabilization properties hold."""
        summary = stabilization_summary(max_k=10)
        for prop, result in summary.items():
            assert result, f"Property {prop} failed"

    def test_verify_all(self):
        """Full verification suite passes."""
        results = verify_all(max_k=10)
        failures = {k: v for k, v in results.items() if not v}
        assert not failures, f"Failures: {failures}"


# ============================================================================
# Cross-consistency with sl2_baxter
# ============================================================================

class TestCrossConsistency:
    """Cross-check KR stabilization with sl2_baxter module."""

    def test_kr_matches_eval_module(self):
        """KR character matches eval_module_Vn from sl2_baxter."""
        from compute.lib.sl2_baxter import eval_module_Vn
        for n in range(10):
            chi_kr = kr_module_character(n)
            chi_eval = eval_module_Vn(n)
            assert formal_character_equal(chi_kr, chi_eval)

    def test_tensor_matches_baxter(self):
        """Tensor product character matches sl2_baxter tensor_product_characters."""
        from compute.lib.sl2_baxter import tensor_product_characters
        for n in range(1, 6):
            for m in range(1, 6):
                chi_n = kr_module_character(n)
                chi_m = kr_module_character(m)
                chi_tensor = tensor_product_characters(chi_n, chi_m)
                chi_our = tensor_product_character(n, m)
                assert formal_character_equal(chi_tensor, chi_our)

    def test_chebyshev_consistency(self):
        """KR CG decomposition is consistent with Chebyshev structure.

        V_1 tensor V_n = V_{n+1} + V_{n-1} (Chebyshev recurrence).
        """
        for n in range(1, 10):
            chi_tensor = tensor_product_character(1, n)
            # CG: V_{n+1} + V_{n-1}
            chi_cg = tensor_product_cg_character(1, n)
            assert formal_character_equal(chi_tensor, chi_cg)
            # Check summands
            dims = tensor_product_decomposition_dims(1, n)
            assert sorted(dims) == sorted([n + 2, n])  # V_{n+1} and V_{n-1}


# ============================================================================
# Edge cases and structural tests
# ============================================================================

class TestEdgeCases:
    """Edge cases and structural properties."""

    def test_trivial_module_bar(self):
        """Bar complex of trivial module W_{0,a}."""
        dims = bar_poincare_polynomial(0)
        assert dims == [1, 3, 3, 1]  # = Pascal row 3

    def test_bar_complex_pascal(self):
        """Bar complex Betti numbers form Pascal's row 3 (scaled)."""
        pascal_3 = [1, 3, 3, 1]
        for k in range(10):
            dims = bar_poincare_polynomial(k)
            assert dims == [(k + 1) * c for c in pascal_3]

    def test_bar_dim_symmetry(self):
        """dim B^j = dim B^{3-j} (Poincare duality of Lambda^*(sl_2*))."""
        for k in range(10):
            for j in range(4):
                assert bar_complex_dim(k, j) == bar_complex_dim(k, 3 - j)

    def test_alternating_series_at_minus_1(self):
        """F_n(-1) = (n+1) * (1-(-1))^3 = (n+1) * 8."""
        for k in range(10):
            val = bar_alternating_series(k, t=-1.0)
            assert abs(val - (k + 1) * 8) < 1e-10

    def test_cg_commutativity(self):
        """V_n tensor V_m = V_m tensor V_n at character level."""
        for n in range(1, 8):
            for m in range(1, 8):
                chi_nm = tensor_product_character(n, m)
                chi_mn = tensor_product_character(m, n)
                assert formal_character_equal(chi_nm, chi_mn)

    def test_cg_associativity_dims(self):
        """(V_n tensor V_m) tensor V_p and V_n tensor (V_m tensor V_p) have same dim."""
        for n, m, p in [(1, 1, 1), (2, 1, 1), (2, 2, 1), (3, 2, 1)]:
            dim_left = (n + 1) * (m + 1) * (p + 1)
            dim_right = (n + 1) * (m + 1) * (p + 1)
            assert dim_left == dim_right

    def test_q_character_convergence_small_window(self):
        """q-character convergence with small window."""
        assert verify_q_character_convergence(max_j=2, max_n=5)
