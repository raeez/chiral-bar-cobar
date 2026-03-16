"""Tests for R-matrix structure on V_n tensor L- and CG projectors.

Verifies block-diagonal structure of the R-matrix action, CG projector
idempotency, and the relation between R-matrix eigenvalues and the
prefundamental CG decomposition.

References:
  - yangians_computations.tex, prop:prefundamental-clebsch-gordan
  - yangians_foundations.tex, prop:yangian-module-koszul
  - sl2_baxter.py: yang_r_matrix, r_matrix_decomposition
"""

import numpy as np
import pytest

from compute.lib.sl2_baxter import (
    eval_module_Vn,
    r_matrix_decomposition,
    tensor_product_characters,
    verify_r_matrix_clebsch_gordan,
    verify_yang_baxter,
    yang_r_matrix,
    yang_r_matrix_normalized,
)
from compute.lib.hjz_prefundamental import (
    partition_function,
    prefundamental_character_sl2,
)
from compute.lib.prefundamental_clebsch_gordan import (
    prefundamental_clebsch_gordan,
)


# =========================================================================
# 1. Yang-Baxter equation verification
# =========================================================================

class TestYangBaxterEquation:
    """R12(u-v) R13(u) R23(v) = R23(v) R13(u) R12(u-v)."""

    @pytest.mark.parametrize("u,v", [
        (1.0, 0.5), (2.0, 1.0), (3.5, 1.7), (0.1, 5.0), (-1.0, 2.0),
    ])
    def test_yang_baxter(self, u, v):
        residual = verify_yang_baxter(u, v)
        assert residual < 1e-10

    def test_yang_baxter_equal_params(self):
        residual = verify_yang_baxter(1.0, 1.0)
        assert residual < 1e-10


# =========================================================================
# 2. R-matrix block-diagonal structure on V1 tensor V1
# =========================================================================

class TestRMatrixBlockDiagonal:
    """R(u) is block-diagonal in the CG basis V2 + V0."""

    def test_decomposition_eigenvalues(self):
        for u in [1.0, 2.5, 5.0]:
            d = r_matrix_decomposition(u)
            assert abs(d["eigenvalues"]["symmetric"] - (u + 1)) < 1e-10
            assert abs(d["eigenvalues"]["antisymmetric"] - (u - 1)) < 1e-10

    def test_projectors_idempotent(self):
        d = r_matrix_decomposition(1.0)
        assert np.allclose(d["P_sym"] @ d["P_sym"], d["P_sym"])
        assert np.allclose(d["P_asym"] @ d["P_asym"], d["P_asym"])

    def test_projectors_orthogonal(self):
        d = r_matrix_decomposition(1.0)
        assert np.allclose(d["P_sym"] @ d["P_asym"], 0)

    def test_projectors_complete(self):
        d = r_matrix_decomposition(1.0)
        assert np.allclose(d["P_sym"] + d["P_asym"], np.eye(4))

    def test_projector_ranks(self):
        d = r_matrix_decomposition(1.0)
        assert np.linalg.matrix_rank(d["P_sym"]) == 3
        assert np.linalg.matrix_rank(d["P_asym"]) == 1

    def test_r_matrix_from_projectors(self):
        for u in [0.0, 1.0, 3.0, -2.0]:
            d = r_matrix_decomposition(u)
            R_from_proj = (u + 1) * d["P_sym"] + (u - 1) * d["P_asym"]
            R_direct = yang_r_matrix(u)
            assert np.allclose(R_from_proj, R_direct)


# =========================================================================
# 3. CG decomposition: V1 tensor V1 = V2 + V0
# =========================================================================

class TestEvaluationCG:
    """Classical CG for evaluation modules verified via R-matrix."""

    def test_cg_v1_v1(self):
        assert verify_r_matrix_clebsch_gordan()

    def test_cg_character_v1_v1(self):
        V1 = eval_module_Vn(1)
        V2 = eval_module_Vn(2)
        V0 = eval_module_Vn(0)
        lhs = tensor_product_characters(V1, V1)
        rhs = {}
        for ch in [V2, V0]:
            for w, m in ch.items():
                rhs[w] = rhs.get(w, 0) + m
        for w in set(list(lhs.keys()) + list(rhs.keys())):
            assert lhs.get(w, 0) == rhs.get(w, 0)

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_cg_character_v1_vn(self, n):
        """ch(V1 tensor Vn) = ch(V_{n+1}) + ch(V_{n-1})."""
        V1 = eval_module_Vn(1)
        Vn = eval_module_Vn(n)
        lhs = tensor_product_characters(V1, Vn)
        rhs = {}
        for ch in [eval_module_Vn(n + 1), eval_module_Vn(n - 1)]:
            for w, m in ch.items():
                rhs[w] = rhs.get(w, 0) + m
        for w in set(list(lhs.keys()) + list(rhs.keys())):
            assert lhs.get(w, 0) == rhs.get(w, 0)


# =========================================================================
# 4. R-matrix structure predictions for V_n tensor L-
# =========================================================================

class TestRMatrixPrefundamental:
    """R-matrix eigenvalue predictions on V_n tensor L- from the CG rule."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 6])
    def test_cg_summand_count(self, n):
        r = prefundamental_clebsch_gordan(n, depth=40)
        assert r["match"]
        assert r["n_components"] == n + 1

    def test_cg_block_diagonal_character_evidence(self):
        """Character splits cleanly into n+1 shifted copies."""
        for n in range(1, 7):
            r = prefundamental_clebsch_gordan(n, depth=40)
            assert r["match"]
            assert r["n_mismatches"] == 0

    def test_r_eigenvalue_shift_pattern(self):
        """Eigenvalue gap between V2 and V0 blocks is 2."""
        d = r_matrix_decomposition(0.0)
        gap = abs(d["eigenvalues"]["symmetric"] - d["eigenvalues"]["antisymmetric"])
        assert abs(gap - 2) < 1e-10

    @pytest.mark.parametrize("n", [1, 2, 3, 4])
    def test_highest_weight_arithmetic_progression(self, n):
        """CG highest weights form AP with common difference -2."""
        r = prefundamental_clebsch_gordan(n, depth=40)
        hws = r["highest_weights"]
        for i in range(1, len(hws)):
            assert hws[i] - hws[i - 1] == -2


# =========================================================================
# 5. CG projector structure
# =========================================================================

class TestCGProjectors:
    """CG projector idempotent extraction from the R-matrix."""

    def test_v1v1_projectors_from_r_matrix(self):
        R0 = yang_r_matrix(0.0)
        I4 = np.eye(4, dtype=complex)
        P_sym = (I4 + R0) / 2
        P_asym = (I4 - R0) / 2
        assert np.allclose(P_sym @ P_sym, P_sym)
        assert np.allclose(P_asym @ P_asym, P_asym)

    def test_projectors_from_two_r_values(self):
        """Extract projectors from R(u1), R(u2) by solving linear system."""
        u1, u2 = 1.0, 3.0
        R1 = yang_r_matrix(u1)
        R2 = yang_r_matrix(u2)
        denom = (u1 + 1) * (u2 - 1) - (u2 + 1) * (u1 - 1)
        P_sym = ((u2 - 1) * R1 - (u1 - 1) * R2) / denom
        d = r_matrix_decomposition(0.0)
        assert np.allclose(P_sym, d["P_sym"])

    def test_trace_matches_dimension(self):
        d = r_matrix_decomposition(0.0)
        assert abs(np.trace(d["P_sym"]) - 3) < 1e-10
        assert abs(np.trace(d["P_asym"]) - 1) < 1e-10

    def test_prefundamental_cg_projector_character_prediction(self):
        """CG projectors predict multiplicity in each L- summand."""
        L = prefundamental_character_sl2(depth=30)
        for n in [1, 2, 3]:
            Vn = eval_module_Vn(n)
            total = tensor_product_characters(Vn, L)
            reconstructed = {}
            for j in range(n + 1):
                hw = n - 2 * j
                for k in range(30):
                    w = hw - 2 * k
                    reconstructed[w] = reconstructed.get(w, 0) + partition_function(k)
            for w in total:
                if abs(w) <= 50:
                    assert total.get(w, 0) == reconstructed.get(w, 0)


# =========================================================================
# 6. Compatibility with evaluation CG
# =========================================================================

class TestCGCompatibility:
    """Prefundamental CG is compatible with evaluation CG."""

    def test_v1_tensor_commutes(self):
        """(V1 tensor V2) tensor L- = V1 tensor (V2 tensor L-)."""
        L = prefundamental_character_sl2(depth=30)
        V1 = eval_module_Vn(1)
        V2 = eval_module_Vn(2)
        V3 = eval_module_Vn(3)

        v3L = tensor_product_characters(V3, L)
        v1L = tensor_product_characters(V1, L)
        lhs = {}
        for ch in [v3L, v1L]:
            for w, m in ch.items():
                lhs[w] = lhs.get(w, 0) + m

        v2L = tensor_product_characters(V2, L)
        rhs = tensor_product_characters(V1, v2L)

        for w in set(list(lhs.keys()) + list(rhs.keys())):
            if abs(w) <= 50:
                assert lhs.get(w, 0) == rhs.get(w, 0)

    def test_associativity_v2_v2_L(self):
        """(V2 tensor V2) tensor L- = V2 tensor (V2 tensor L-)."""
        L = prefundamental_character_sl2(depth=30)
        V2 = eval_module_Vn(2)
        V4 = eval_module_Vn(4)
        V0 = eval_module_Vn(0)

        lhs = {}
        for Vk in [V4, V2, V0]:
            ch = tensor_product_characters(Vk, L)
            for w, m in ch.items():
                lhs[w] = lhs.get(w, 0) + m

        v2L = tensor_product_characters(V2, L)
        rhs = tensor_product_characters(V2, v2L)

        for w in set(list(lhs.keys()) + list(rhs.keys())):
            if abs(w) <= 50:
                assert lhs.get(w, 0) == rhs.get(w, 0)
