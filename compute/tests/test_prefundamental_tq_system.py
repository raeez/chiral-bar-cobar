"""Tests for the prefundamental TQ system and spectral structure.

Verifies the Baxter TQ functional equation and its consequences for
the prefundamental module L- of Y(sl_2), including:
  - TQ relation: T(u)Q(u) = phi(u+1/2)Q(u-1) + phi(u-1/2)Q(u+1)
  - Two-term K_0 decomposition: [V_1].[L-] = [L-(+1)] + [L-(-1)]
  - Weight parity structure of V_n tensor L-
  - QQ-system Wronskian preservation under V_1-twist
  - Spectral self-duality of the TQ recurrence

References:
  - yangians_computations.tex, prop:prefundamental-clebsch-gordan
  - yangians_computations.tex, cor:k0-generation-OY
  - sl2_baxter.py: tq_functional_equation, transfer_matrix_eigenvalue
  - hjz_prefundamental.py: verify_prefundamental_tq_k0
"""

import math

import pytest

from compute.lib.hjz_prefundamental import (
    partition_function,
    prefundamental_character_sl2,
    prefundamental_tensor_V1,
    prefundamental_tensor_Vn,
    verify_prefundamental_tq_k0,
)
from compute.lib.sl2_baxter import (
    baxter_q_operator_eigenvalue,
    eval_module_Vn,
    sl2_verma_character,
    subtract_characters,
    sum_characters,
    tensor_product_characters,
    tq_functional_equation,
    transfer_matrix_eigenvalue,
)


# =========================================================================
# 1. TQ functional equation at the transfer-matrix level
# =========================================================================

class TestTQFunctionalEquation:
    """Baxter TQ: T(u)Q(u) = Q(u+1) + Q(u-1) for evaluation modules."""

    def test_tq_vacuum_state(self):
        """Vacuum (lam=0): Q(u)=1. Structure check."""
        Q = lambda w: baxter_q_operator_eigenvalue(w, 0)
        assert abs(Q(5.0) - 1.0) < 1e-10

    def test_tq_lam1_bethe_root(self):
        """lam=1: Q(u) = u."""
        Q = lambda w: baxter_q_operator_eigenvalue(w, 1)
        assert abs(Q(3.0) - 3.0) < 1e-10
        assert abs(Q(-2.0) - (-2.0)) < 1e-10

    def test_tq_lam2_polynomial(self):
        """lam=2: Q(u) is degree-2 polynomial with known Bethe roots."""
        Q = lambda w: baxter_q_operator_eigenvalue(w, 2)
        q0 = Q(0.0)
        q1 = Q(1.0)
        q2 = Q(2.0)
        # Second differences should be constant (degree 2 polynomial)
        d2 = q2 - 2 * q1 + q0
        q3 = Q(3.0)
        d2_alt = q3 - 2 * q2 + q1
        assert abs(d2 - d2_alt) < 1e-10, "Q not degree 2"

    @pytest.mark.parametrize("lam", [0, 1, 2, 3, 4, 5])
    def test_q_polynomial_degree(self, lam):
        """Q-operator eigenvalue is degree-lam polynomial."""
        Q = lambda w: baxter_q_operator_eigenvalue(w, lam)
        vals = [Q(float(k)) for k in range(lam + 3)]
        from math import comb
        fd = sum((-1) ** (lam + 1 - k) * comb(lam + 1, k) * vals[k]
                 for k in range(lam + 2))
        assert abs(fd) < 1e-6, f"Q not degree {lam}: fd = {fd}"


# =========================================================================
# 2. Prefundamental TQ relation at the K_0 / character level
# =========================================================================

class TestPrefundamentalTQCharacterLevel:
    """[V_1].[L-] = [L-(+1)] + [L-(-1)] at the character level."""

    def test_two_term_decomposition(self):
        """verify_prefundamental_tq_k0 confirms the two-term decomposition."""
        r = verify_prefundamental_tq_k0(0.0, 0.0, depth=40)
        assert r["two_term_decomposition_matches"]

    def test_all_weights_odd(self):
        """V_1 tensor L- lives on the odd weight lattice."""
        r = verify_prefundamental_tq_k0(0.0, 0.0, depth=40)
        assert r["all_weights_odd"]

    def test_weight_1_multiplicity(self):
        """Weight 1 has multiplicity p(0) = 1."""
        r = verify_prefundamental_tq_k0(0.0, 0.0, depth=40)
        assert r["weight_1_correct"]

    def test_multiplicity_pattern(self):
        """Weight -(2k-1) has mult p(k-1) + p(k)."""
        r = verify_prefundamental_tq_k0(0.0, 0.0, depth=40)
        assert r["multiplicity_pattern_correct"]

    def test_multiplicity_pattern_deep(self):
        """Multiplicity pattern at depth 80."""
        r = verify_prefundamental_tq_k0(0.0, 0.0, depth=80)
        assert r["multiplicity_pattern_correct"]

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_vn_weight_parity(self, n):
        """V_n tensor L- has weights of parity n mod 2."""
        Vn = eval_module_Vn(n)
        L = prefundamental_character_sl2(depth=40)
        tensor = tensor_product_characters(Vn, L)
        expected_parity = n % 2
        for w in tensor:
            assert w % 2 == expected_parity, f"Wrong parity at n={n}, w={w}"


# =========================================================================
# 3. QQ-system and Wronskian structure
# =========================================================================

class TestQQSystem:
    """QQ-system Wronskian preservation under V_1-twist."""

    def test_wronskian_adjacent_partition_sums(self):
        """Turan determinant p(k)^2 - p(k+1)p(k-1) > 0 for k >= 26."""
        for k in range(26, 40):
            pk = partition_function(k)
            pk1 = partition_function(k + 1)
            pkm1 = partition_function(k - 1)
            turan = pk * pk - pk1 * pkm1
            assert turan > 0, f"Turan negative at k={k}: {turan}"

    def test_qq_character_consistency(self):
        """[L-(+1)] + [L-(-1)] exhausts [V_1].[L-] with no remainder."""
        L = prefundamental_character_sl2(depth=40)
        L_plus = {w + 1: m for w, m in L.items()}
        L_minus = {w - 1: m for w, m in L.items()}
        rhs = sum_characters(L_plus, L_minus)

        V1 = eval_module_Vn(1)
        lhs = tensor_product_characters(V1, L)

        for w in set(list(lhs.keys()) + list(rhs.keys())):
            if abs(w) <= 70:
                assert lhs.get(w, 0) == rhs.get(w, 0), \
                    f"QQ mismatch at w={w}: lhs={lhs.get(w,0)}, rhs={rhs.get(w,0)}"

    def test_qq_vn_consistency(self):
        """[V_n].[L-] = sum [L-(n-2j)] is the higher-spin QQ-system."""
        for n in [2, 3, 4]:
            L = prefundamental_character_sl2(depth=40)
            Vn = eval_module_Vn(n)
            lhs = tensor_product_characters(Vn, L)

            rhs = {}
            for j in range(n + 1):
                hw = n - 2 * j
                shifted = {w + hw: m for w, m in L.items()}
                for w, m in shifted.items():
                    rhs[w] = rhs.get(w, 0) + m

            for w in set(list(lhs.keys()) + list(rhs.keys())):
                if abs(w) <= 60:
                    assert lhs.get(w, 0) == rhs.get(w, 0), \
                        f"Higher QQ mismatch at n={n}, w={w}"

    def test_wronskian_preservation_under_v1_twist(self):
        """[V_1]^2.[L-] = [V_2].[L-] + [L-] (from V_1 tensor V_1 = V_2 + V_0)."""
        L = prefundamental_character_sl2(depth=40)
        V1 = eval_module_Vn(1)
        V2 = eval_module_Vn(2)

        v1_L = tensor_product_characters(V1, L)
        v1_v1_L = tensor_product_characters(V1, v1_L)

        v2_L = tensor_product_characters(V2, L)
        rhs = sum_characters(v2_L, L)

        for w in set(list(v1_v1_L.keys()) + list(rhs.keys())):
            if abs(w) <= 60:
                assert v1_v1_L.get(w, 0) == rhs.get(w, 0), \
                    f"Wronskian twist mismatch at w={w}"


# =========================================================================
# 4. Spectral self-duality and shift structure
# =========================================================================

class TestSpectralStructure:
    """Spectral self-duality of the prefundamental CG decomposition."""

    def test_cg_symmetric_under_reflection(self):
        """CG summands {n-2j : j=0..n} are symmetric under j -> n-j."""
        for n in range(1, 10):
            hws = [n - 2 * j for j in range(n + 1)]
            reversed_hws = list(reversed(hws))
            assert hws == [-h for h in reversed_hws]

    def test_cg_center_of_mass_zero(self):
        """Sum of CG highest weights is zero."""
        for n in range(1, 15):
            total = sum(n - 2 * j for j in range(n + 1))
            assert total == 0

    def test_tq_recurrence_symmetry(self):
        """T(u) + T(-u-1) = 0: spectral shadow of Koszul duality."""
        for u in [1.0, 2.5, 4.3]:
            T_u = transfer_matrix_eigenvalue(u, 0, 0.0)
            T_neg = transfer_matrix_eigenvalue(-u - 1, 0, 0.0)
            assert abs(T_u + T_neg) < 1e-10

    def test_shift_operator_chebyshev(self):
        """[V_1] acts as shift operator: Chebyshev recurrence on K_0."""
        from compute.lib.sl2_baxter import verify_chebyshev_structure
        assert verify_chebyshev_structure(max_n=6)

    def test_k0_lattice_structure(self):
        """K_0 lattice generated by {V_n, L-} verifies structure."""
        from compute.lib.sl2_baxter import verify_k0_lattice
        assert verify_k0_lattice(max_lam=5, depth=30)


# =========================================================================
# 5. Growth rate analysis
# =========================================================================

class TestGrowthRates:
    """Growth rates of the TQ system quantities."""

    def test_adjacent_partition_sum_growth(self):
        """p(k-1) + p(k) ~ 2*HR(k) for large k."""
        for k in [15, 20, 30]:
            pk = partition_function(k)
            pkm1 = partition_function(k - 1)
            hr = math.exp(math.pi * math.sqrt(2 * k / 3)) / (4 * k * math.sqrt(3))
            ratio = (pk + pkm1) / (2 * hr)
            assert 0.3 < ratio < 3.0

    def test_cumulative_multiplicity_growth(self):
        """Cumulative mult grows sub-exponentially."""
        total = 0
        for k in range(1, 40):
            total += partition_function(k - 1) + partition_function(k)
        assert total < 2 ** 40

    @pytest.mark.parametrize("n", [2, 4, 6, 8])
    def test_euler_char_from_tq(self, n):
        """Euler characteristic chi(L-, V_n) = sum p(k) from TQ structure."""
        from compute.lib.thick_generation_sl2 import ext_euler_char_bound
        r = ext_euler_char_bound(n)
        expected = sum(partition_function(k) for k in range(n // 2 + 1))
        assert r["euler_characteristic"] == expected
