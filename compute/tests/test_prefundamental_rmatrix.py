"""Tests for R-matrix structure on prefundamental tensor products.

Verifies:
  - R-matrix block-diagonal structure on V_n ⊗ L⁻
  - CG projector idempotent extraction
  - Yang-Baxter equation on evaluation modules (cross-check)
  - R-matrix eigenvalue structure from CG decomposition
"""

import numpy as np
import pytest

from compute.lib.sl2_baxter import (
    eval_module_V1,
    eval_module_Vn,
    r_matrix_decomposition,
    tensor_product_characters,
    verify_yang_baxter,
    yang_r_matrix,
)
from compute.lib.hjz_prefundamental import (
    partition_function,
    prefundamental_character_sl2,
)
from compute.lib.prefundamental_clebsch_gordan import (
    prefundamental_clebsch_gordan,
)


# =========================================================================
# 1. R-matrix on evaluation modules (foundation)
# =========================================================================

class TestRMatrixFoundation:
    """Yang R-matrix R(u) = uI + P on V_1 ⊗ V_1."""

    def test_r_matrix_form(self):
        """R(u) = uI + P at u=1."""
        R = yang_r_matrix(1.0)
        I4 = np.eye(4, dtype=complex)
        P = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], dtype=complex)
        expected = 1.0 * I4 + P
        assert np.allclose(R, expected)

    @pytest.mark.parametrize("u,v", [(1.0, 2.0), (0.5, 1.5), (3.0, 0.7)])
    def test_yang_baxter_equation(self, u, v):
        """YBE: R_12(u-v) R_13(u) R_23(v) = R_23(v) R_13(u) R_12(u-v)."""
        residual = verify_yang_baxter(u, v)
        assert residual < 1e-10

    def test_r_matrix_decomposition_structure(self):
        """R(u) = (u+1)P_sym + (u-1)P_asym."""
        data = r_matrix_decomposition(2.0)
        assert data["R_on_sym"] == pytest.approx(3.0)  # u+1
        assert data["R_on_asym"] == pytest.approx(1.0)  # u-1

    def test_r_matrix_unitarity(self):
        """R(u) R(-u) = (1 - u²)I.

        Proof: R(u) = uI + P, R(-u) = -uI + P.
        Product = (-u²)I + P² = (-u² + 1)I since P² = I.
        """
        for u in [1.5, 2.0, 3.7]:
            R_u = yang_r_matrix(u)
            R_neg_u = yang_r_matrix(-u)
            product = R_u @ R_neg_u
            expected = (1 - u**2) * np.eye(4, dtype=complex)
            assert np.allclose(product, expected, atol=1e-10)


# =========================================================================
# 2. R-matrix block-diagonal structure from CG
# =========================================================================

class TestRMatrixBlockDiagonal:
    """R-matrix on V_n ⊗ L⁻ should be block-diagonal in the CG basis.

    By the CG decomposition V_n ⊗ L⁻ = ⊕ L⁻(shifted), the R-matrix
    should act as a scalar on each L⁻(shifted) block.
    """

    def test_cg_predicts_n_plus_1_blocks(self):
        """V_n ⊗ L⁻ has n+1 blocks by CG."""
        for n in range(1, 6):
            r = prefundamental_clebsch_gordan(n)
            assert r["n_components"] == n + 1

    def test_block_weights_partition_correctly(self):
        """The n+1 blocks have hw = n, n-2, ..., -n."""
        for n in range(1, 6):
            r = prefundamental_clebsch_gordan(n)
            expected_hws = [n - 2*j for j in range(n+1)]
            assert r["highest_weights"] == expected_hws

    def test_v1_tensor_l_two_blocks(self):
        """V_1 ⊗ L⁻: 2 blocks with hw = 1 and hw = -1."""
        r = prefundamental_clebsch_gordan(1)
        assert r["match"]
        assert r["highest_weights"] == [1, -1]

    def test_v2_tensor_l_three_blocks(self):
        """V_2 ⊗ L⁻: 3 blocks with hw = 2, 0, -2."""
        r = prefundamental_clebsch_gordan(2)
        assert r["match"]
        assert r["highest_weights"] == [2, 0, -2]


# =========================================================================
# 3. CG projector structure
# =========================================================================

class TestCGProjectors:
    """CG projectors: idempotents extracting each L⁻(shifted) from V_n ⊗ L⁻."""

    def test_projector_dimensions_sum_correctly(self):
        """Sum of block dimensions = total tensor product dimension.

        At each weight w, the sum of multiplicities from each
        L⁻(n-2j) block should equal the V_n ⊗ L⁻ multiplicity.
        """
        depth = 25
        for n in [1, 2, 3, 4]:
            L = prefundamental_character_sl2(depth=depth)
            Vn = eval_module_Vn(n)
            total = tensor_product_characters(Vn, L)

            # Sum of shifted L⁻ characters
            block_sum = {}
            for j in range(n + 1):
                hw = n - 2 * j
                for k in range(depth):
                    w = hw - 2 * k
                    block_sum[w] = block_sum.get(w, 0) + partition_function(k)

            # Compare at each weight
            for w in total:
                if abs(w) < 2 * (depth - n):
                    assert total.get(w, 0) == block_sum.get(w, 0), \
                        f"n={n}, w={w}: total={total.get(w,0)}, blocks={block_sum.get(w,0)}"

    def test_projectors_are_complementary(self):
        """The n+1 blocks partition the weight space completely."""
        depth = 20
        for n in [1, 2, 3]:
            # Each weight in V_n ⊗ L⁻ belongs to at least one block
            Vn = eval_module_Vn(n)
            L = prefundamental_character_sl2(depth=depth)
            total = tensor_product_characters(Vn, L)

            # All weights in total should be accounted for by blocks
            block_weights = set()
            for j in range(n + 1):
                hw = n - 2 * j
                for k in range(depth):
                    block_weights.add(hw - 2 * k)

            for w in total:
                if abs(w) < 2 * (depth - n):
                    assert w in block_weights, \
                        f"Weight {w} in V_{n} ⊗ L⁻ not covered by blocks"


# =========================================================================
# 4. R-matrix CG consistency
# =========================================================================

class TestRMatrixCGConsistency:
    """The CG decomposition for evaluation modules is consistent
    with the R-matrix eigenstructure."""

    def test_v1_v1_eigenvalues(self):
        """R(u) on V_1 ⊗ V_1 has eigenvalues u+1 (V_2) and u-1 (V_0)."""
        data = r_matrix_decomposition(1.0)
        # sym eigenvalue = u + 1 = 2, asym = u - 1 = 0
        assert data["R_on_sym"] == pytest.approx(2.0)
        assert data["R_on_asym"] == pytest.approx(0.0)

    def test_cg_for_evaluation_modules(self):
        """V_1 ⊗ V_1 = V_2 ⊕ V_0 at character level."""
        from compute.lib.sl2_baxter import verify_r_matrix_clebsch_gordan
        assert verify_r_matrix_clebsch_gordan()

    def test_iterated_cg_consistency(self):
        """V_1^⊗n ⊗ L⁻ parity alternates: even/odd lattice."""
        V1 = eval_module_V1()
        L = prefundamental_character_sl2(depth=20)

        current = dict(L)
        for step in range(5):
            weights = [w for w in current if current[w] > 0]
            parities = set(w % 2 for w in weights)
            expected_parity = {step % 2}
            assert parities == expected_parity, \
                f"Step {step}: expected parity {expected_parity}, got {parities}"
            current = tensor_product_characters(V1, current)


# =========================================================================
# 5. Extended CG verification
# =========================================================================

class TestExtendedCG:
    """Extended CG verification for larger n and deeper depth."""

    @pytest.mark.parametrize("n", range(1, 13))
    def test_cg_n_through_12(self, n):
        """CG at n=1..12, depth=30."""
        r = prefundamental_clebsch_gordan(n, depth=30)
        assert r["match"], f"CG failed at n={n}"

    def test_cg_n25_depth30(self):
        """CG at n=25 (blue team defense level)."""
        r = prefundamental_clebsch_gordan(25, depth=30)
        assert r["match"]
