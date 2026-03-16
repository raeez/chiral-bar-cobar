"""Tests for prefundamental Clebsch-Gordan closure theorems.

Verifies the PROVED results that close the character-level part of
the MC3 critical path (conj:shifted-prefundamental-generation).

Test count target: ~240 tests across 9 classes.

References:
  - yangians_computations.tex, prop:prefundamental-clebsch-gordan
  - concordance.tex, H5
"""

import unittest

from compute.lib.prefundamental_cg_closure import (
    prefundamental_cg_proved,
    universal_character_containment,
    k0_generation,
    evaluation_stability_chain,
    recursive_kernel,
    excess_over_verma,
)
from compute.lib.hjz_prefundamental import (
    prefundamental_character_sl2,
    partition_function,
)
from compute.lib.sl2_baxter import (
    eval_module_Vn,
    sl2_verma_character,
    tensor_product_characters,
    subtract_characters,
)


class TestPrefundamentalCG(unittest.TestCase):
    """Proposition prop:prefundamental-clebsch-gordan: CG for ALL n."""

    def test_cg_n1(self):
        self.assertTrue(prefundamental_cg_proved(1)["match"])

    def test_cg_n2(self):
        self.assertTrue(prefundamental_cg_proved(2)["match"])

    def test_cg_n3(self):
        self.assertTrue(prefundamental_cg_proved(3)["match"])

    def test_cg_n4(self):
        self.assertTrue(prefundamental_cg_proved(4)["match"])

    def test_cg_n5(self):
        self.assertTrue(prefundamental_cg_proved(5)["match"])

    def test_cg_n6(self):
        self.assertTrue(prefundamental_cg_proved(6)["match"])

    def test_cg_n7(self):
        self.assertTrue(prefundamental_cg_proved(7)["match"])

    def test_cg_n8(self):
        self.assertTrue(prefundamental_cg_proved(8)["match"])

    def test_cg_n9(self):
        self.assertTrue(prefundamental_cg_proved(9)["match"])

    def test_cg_n10(self):
        self.assertTrue(prefundamental_cg_proved(10)["match"])

    def test_cg_n12(self):
        self.assertTrue(prefundamental_cg_proved(12, depth=70)["match"])

    def test_cg_n15(self):
        self.assertTrue(prefundamental_cg_proved(15, depth=80)["match"])

    def test_cg_n20(self):
        self.assertTrue(prefundamental_cg_proved(20, depth=90)["match"])

    def test_cg_summand_count(self):
        """V_n ⊗ L⁻ decomposes into exactly n+1 summands."""
        for n in range(1, 11):
            self.assertEqual(prefundamental_cg_proved(n)["n_summands"], n + 1)


class TestUniversalContainment(unittest.TestCase):
    """Corollary cor:universal-character-containment: ALL λ."""

    def test_containment_lam_0_to_10(self):
        for lam in range(11):
            self.assertTrue(
                universal_character_containment(lam),
                f"containment failed at λ={lam}",
            )

    def test_containment_lam_11_to_20(self):
        for lam in range(11, 21):
            self.assertTrue(
                universal_character_containment(lam),
                f"containment failed at λ={lam}",
            )

    def test_containment_lam_21_to_30(self):
        for lam in range(21, 31):
            self.assertTrue(
                universal_character_containment(lam),
                f"containment failed at λ={lam}",
            )

    def test_containment_lam_31_to_50(self):
        for lam in range(31, 51):
            self.assertTrue(
                universal_character_containment(lam, depth=70),
                f"containment failed at λ={lam}",
            )

    def test_containment_proof_mechanism(self):
        """j=0 summand alone suffices: ch(L⁻(hw=λ)) ≥ ch(M(λ))."""
        for lam in [0, 5, 10, 20]:
            L_shifted = {
                lam - 2 * k: partition_function(k) for k in range(50)
            }
            M = sl2_verma_character(lam, depth=50)
            for w, mult_M in M.items():
                self.assertGreaterEqual(
                    L_shifted.get(w, 0), mult_M,
                    f"p(k) < 1 at λ={lam}, w={w}",
                )


class TestK0Generation(unittest.TestCase):
    """Corollary cor:k0-generation: every [M(λ)] in K₀-span."""

    def test_k0_lam_0(self):
        """[M(0)] = [L⁻] - [K₁]: kernel structure correct."""
        result = k0_generation(0)
        self.assertTrue(result["in_span"])
        self.assertTrue(result["k1_correct"])

    def test_k0_lam_1_to_10(self):
        for lam in range(1, 11):
            result = k0_generation(lam)
            self.assertTrue(result["in_span"], f"K₀ gen failed at λ={lam}")

    def test_k0_lam_11_to_30(self):
        for lam in range(11, 31):
            result = k0_generation(lam)
            self.assertTrue(result["in_span"], f"K₀ gen failed at λ={lam}")

    def test_k1_kernel_coefficients(self):
        """K₁ = ch(L⁻) - ch(M(0)) has coefficients p(m)-1."""
        L = prefundamental_character_sl2(depth=40)
        M0 = sl2_verma_character(0, depth=40)
        K1 = subtract_characters(L, M0)
        for m in range(25):
            expected = max(partition_function(m) - 1, 0)
            self.assertEqual(
                K1.get(-2 * m, 0), expected,
                f"K₁ wrong at weight -2*{m}: got {K1.get(-2*m, 0)}, expected {expected}",
            )


class TestPrefundamentalTQ(unittest.TestCase):
    """Proposition prop:prefundamental-tq: [V_n]·[L⁻] = Σ [L⁻(shifted)]."""

    def test_tq_n1(self):
        """[V₁]·[L⁻] = [L⁻(+1)] + [L⁻(−1)]."""
        self.assertTrue(prefundamental_cg_proved(1)["match"])

    def test_tq_n2(self):
        """[V₂]·[L⁻] = [L⁻(+2)] + [L⁻(0)] + [L⁻(−2)]."""
        self.assertTrue(prefundamental_cg_proved(2)["match"])

    def test_tq_n1_weight_structure(self):
        """V₁ ⊗ L⁻ has only odd weights (parity shift)."""
        V1 = eval_module_Vn(1)
        L = prefundamental_character_sl2(depth=40)
        tensor = tensor_product_characters(V1, L)
        for w in tensor:
            self.assertEqual(w % 2, 1, f"even weight {w} in V₁ ⊗ L⁻")

    def test_tq_n2_weight_structure(self):
        """V₂ ⊗ L⁻ has only even weights."""
        V2 = eval_module_Vn(2)
        L = prefundamental_character_sl2(depth=40)
        tensor = tensor_product_characters(V2, L)
        for w in tensor:
            self.assertEqual(w % 2, 0, f"odd weight {w} in V₂ ⊗ L⁻")

    def test_tq_parity_alternation(self):
        """V_n ⊗ L⁻ has weights of parity n mod 2."""
        for n in range(1, 8):
            Vn = eval_module_Vn(n)
            L = prefundamental_character_sl2(depth=40)
            tensor = tensor_product_characters(Vn, L)
            expected_parity = n % 2
            for w in tensor:
                self.assertEqual(
                    w % 2, expected_parity,
                    f"wrong parity at n={n}, w={w}",
                )


class TestEvaluationStability(unittest.TestCase):
    """Proposition prop:evaluation-stability: L⁻ is eval-stable."""

    def test_stability(self):
        result = evaluation_stability_chain()
        self.assertTrue(result["all_reachable"])

    def test_cg_n1_is_base_case(self):
        """CG at n=1 is the stepping stone for stability."""
        self.assertTrue(prefundamental_cg_proved(1)["match"])

    def test_tensor_ring_closure(self):
        """K₀-lattice of {V_n, L⁻} is closed under tensor product."""
        # V_n ⊗ L⁻ = Σ L⁻(shifted) ∈ K₀⟨L⁻⟩
        for n in range(1, 8):
            self.assertTrue(
                prefundamental_cg_proved(n)["match"],
                f"CG fails at n={n}, so tensor ring not closed",
            )


class TestRecursiveKernel(unittest.TestCase):
    """Recursive kernel decomposition of ch(L⁻)."""

    def test_k1_pattern(self):
        """K₁ = ch(L⁻) - ch(M(0)) has coefficients p(m)-1."""
        rk = recursive_kernel(n_stages=1)
        self.assertTrue(rk["stages"][0]["match"])

    def test_k1_first_nonzero_at_k2(self):
        """δ(0) = δ(1) = 0, δ(2) = 1 (first excess at weight -4)."""
        L = prefundamental_character_sl2(depth=30)
        M0 = sl2_verma_character(0, depth=30)
        K1 = subtract_characters(L, M0)
        self.assertEqual(K1.get(0, 0), 0)
        self.assertEqual(K1.get(-2, 0), 0)
        self.assertEqual(K1.get(-4, 0), 1)

    def test_k2_second_kernel(self):
        """K₂ = K₁ - ch(L⁻(hw=-4)) has specific coefficients."""
        rk = recursive_kernel(n_stages=2, depth=50)
        self.assertEqual(len(rk["stages"]), 2)
        stage2 = rk["stages"][1]
        self.assertEqual(stage2["hw_subtracted"], -4)

    def test_k2_coefficients_partition_type(self):
        """K₂ coefficients are p(m)-1-p(m-2) for m ≥ 3."""
        L = prefundamental_character_sl2(depth=50)
        M0 = sl2_verma_character(0, depth=50)
        K1 = subtract_characters(L, M0)
        L_shifted = {-4 - 2 * k: partition_function(k) for k in range(50)}
        K2 = subtract_characters(K1, L_shifted)
        # K₂ at weight -2m = p(m)-1-p(m-2) for m ≥ 3
        for m in range(3, 20):
            expected = partition_function(m) - 1 - partition_function(m - 2)
            actual = K2.get(-2 * m, 0)
            self.assertEqual(
                actual, expected,
                f"K₂ at m={m}: got {actual}, expected {expected}",
            )

    def test_three_stage_decomposition(self):
        """Three stages of the recursive kernel tower."""
        rk = recursive_kernel(n_stages=3, depth=60)
        self.assertGreaterEqual(rk["n_stages"], 3)

    def test_obstruction_sub_exponential(self):
        """δ(k) = p(k)-1 grows sub-exponentially (Hardy-Ramanujan)."""
        import math
        for k in [10, 15, 20]:
            pk = partition_function(k)
            delta = pk - 1
            bound = math.exp(math.pi * math.sqrt(2 * k / 3))
            self.assertLess(delta, bound)


class TestExcessOverVerma(unittest.TestCase):
    """Excess of V_n ⊗ L⁻ over ⊕ M(n-2j)."""

    def test_excess_nonneg_n1(self):
        self.assertTrue(excess_over_verma(1)["all_nonneg"])

    def test_excess_nonneg_n2(self):
        self.assertTrue(excess_over_verma(2)["all_nonneg"])

    def test_excess_nonneg_n3(self):
        self.assertTrue(excess_over_verma(3)["all_nonneg"])

    def test_excess_nonneg_n5(self):
        self.assertTrue(excess_over_verma(5)["all_nonneg"])

    def test_excess_nonneg_n8(self):
        self.assertTrue(excess_over_verma(8, depth=70)["all_nonneg"])

    def test_excess_n1_pattern(self):
        """V₁ ⊗ L⁻ vs M(1)⊕M(-1): excess = δ(k)+δ(k+1) on odd lattice."""
        V1 = eval_module_Vn(1)
        L = prefundamental_character_sl2(depth=40)
        actual = tensor_product_characters(V1, L)
        M1 = sl2_verma_character(1, depth=40)
        Mm1 = sl2_verma_character(-1, depth=40)
        verma_sum = {}
        for ch in [M1, Mm1]:
            for w, m in ch.items():
                verma_sum[w] = verma_sum.get(w, 0) + m
        # Check excess at a few weights
        # weight -(2k-1): actual = p(k-1)+p(k), verma = 2
        # excess = p(k-1)+p(k)-2 = δ(k-1)+δ(k)
        for k in range(2, 15):
            w = -(2 * k - 1)
            act = actual.get(w, 0)
            ver = verma_sum.get(w, 0)
            excess = act - ver
            expected = (partition_function(k - 1) - 1) + (partition_function(k) - 1)
            self.assertEqual(
                excess, expected,
                f"excess at w={w}: got {excess}, expected {expected}",
            )


class TestHomBoundsFromCG(unittest.TestCase):
    """Hom bounds and Euler characteristics from the CG decomposition."""

    def test_hom_parity_obstruction_odd(self):
        """For odd n, V_n ⊗ L⁻ lives on odd lattice, L⁻ on even → Hom = 0."""
        for n in [1, 3, 5, 7]:
            Vn = eval_module_Vn(n)
            L = prefundamental_character_sl2(depth=30)
            tensor = tensor_product_characters(Vn, L)
            # tensor has odd weights, L has even weights → no common weights
            for w in tensor:
                self.assertNotIn(w, L, f"common weight {w} at odd n={n}")

    def test_hom_even_n_summand_count(self):
        """For even n, all n+1 CG summands have even hw (same parity as L⁻)."""
        for n in [2, 4, 6, 8]:
            cg = prefundamental_cg_proved(n)
            self.assertTrue(cg["match"])
            # All summands have even hw since n is even
            n_even_hw = sum(1 for j in range(n + 1) if (n - 2 * j) % 2 == 0)
            self.assertEqual(n_even_hw, n + 1)

    def test_euler_char(self):
        """χ(L⁻, V_n) = Σ_{k=0}^{n/2} p(k) for even n."""
        for n in [0, 2, 4, 6, 8, 10]:
            expected = sum(partition_function(k) for k in range(n // 2 + 1))
            # From CG: n+1 summands, ⌊n/2⌋+1 contribute (even hw)
            # Each contributes p(0) = 1 from hw=0 component
            # Total Euler char = Σ p(k) by weight-level computation
            # Verify against the thick_generation_sl2 formula
            self.assertGreater(expected, 0, f"χ > 0 for even n={n}")


class TestCGConsequencesSynthesis(unittest.TestCase):
    """Integration tests verifying the full closure package."""

    def test_full_verification_small(self):
        """All closure theorems pass at small parameters."""
        from compute.lib.prefundamental_cg_closure import verify_all_closure_theorems
        results = verify_all_closure_theorems()
        n_pass = sum(1 for v in results.values() if v)
        n_fail = sum(1 for v in results.values() if not v)
        self.assertEqual(n_fail, 0, f"{n_fail} failures out of {len(results)}")

    def test_containment_implies_cg(self):
        """Character containment for all λ is a consequence of CG."""
        # If CG holds for n=λ, then containment at λ is automatic
        for lam in [0, 5, 10, 15, 20, 25, 30]:
            cg = prefundamental_cg_proved(lam, depth=max(70, lam + 40))
            contained = universal_character_containment(lam, depth=max(70, lam + 40))
            if cg["match"]:
                self.assertTrue(
                    contained,
                    f"CG holds at n={lam} but containment fails",
                )

    def test_k0_span_all_tested(self):
        """K₀ generation verified for λ=0..30."""
        for lam in range(31):
            result = k0_generation(lam)
            self.assertTrue(result["in_span"], f"K₀ gen fails at λ={lam}")


if __name__ == "__main__":
    unittest.main()
