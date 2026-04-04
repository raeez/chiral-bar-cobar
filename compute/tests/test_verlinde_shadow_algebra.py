r"""Tests for the Verlinde algebra, fusion rules, and MTC data engine.

Verifies:
  1. Modular S-matrix: symmetry, unitarity, S^2=I for sl_2 at k=1..10.
  2. Verlinde formula: all fusion coefficients for sl_2 at k=1..6,
     orthogonality, vacuum identity, non-negativity, integrality.
  3. Shadow tower: S,T extraction from genus-1 data, consistency.
  4. Full MTC data for sl_2 at k=2,3,4: braiding, twist, RT trefoil.
  5. Higher rank: sl_3 at k=1,2,3 -- S-matrix, fusion, Verlinde formula.
  6. Quantum dimensions: d_j = S_{0j}/S_{00}, D^2, k=1..20.
  7. Verlinde ring: recursion, truncation, vacuum identity for k=2,3,4.
  8. Genus-g Verlinde: Z_g for g=0..4, k=1..5, cross-check with shadow F_g.

Mathematical references:
  Verlinde (1988), Nuclear Phys. B 300, 115--138
  Kac-Peterson (1984), Adv. Math. 53, 125--264
  Bakalov-Kirillov (2001), Lectures on tensor categories and modular functors
  thm:modular-characteristic (higher_genus_modular_koszul.tex)
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
"""

import math

import numpy as np
import pytest

from compute.lib.verlinde_shadow_algebra import (
    sl2_S_matrix,
    sl2_S_matrix_exact,
    sl2_T_matrix,
    sl2_charge_conjugation,
    sl2_fusion_coefficients,
    sl2_fusion_rules_explicit,
    sl2_quantum_dimensions,
    sl2_quantum_dimension_formula,
    sl2_total_quantum_dimension_sq,
    sl2_total_quantum_dimension_sq_formula,
    sl2_conformal_weights,
    sl2_central_charge,
    sl2_kappa,
    shadow_S_T_from_genus1,
    sl2_twist,
    sl2_braiding_eigenvalues,
    sl2_RT_trefoil,
    sl2_RT_unknot,
    sl3_integrable_weights,
    sl3_S_matrix,
    sl3_quantum_dimensions,
    sl3_fusion_coefficients,
    sl2_verlinde_ring_multiplication,
    sl2_generator_powers,
    sl2_verlinde_ring_relation,
    sl2_verlinde_genus_g,
    sl2_verlinde_genus_g_exact,
    sl2_verlinde_genus_g_formula,
    sl2_shadow_F_g,
    SL2_VERLINDE_TABLE,
    verify_verlinde_table,
)


# ===========================================================================
# I. MODULAR S-MATRIX FOR sl_2 (k=1..10)
# ===========================================================================

class TestSl2SMatrix:
    """S-matrix properties: symmetric, unitary, S^2 = I."""

    @pytest.mark.parametrize("k", range(1, 11))
    def test_S_symmetric(self, k):
        """S is symmetric: S = S^T."""
        S = sl2_S_matrix(k)
        assert np.allclose(S, S.T, atol=1e-12), (
            f"S-matrix not symmetric at k={k}"
        )

    @pytest.mark.parametrize("k", range(1, 11))
    def test_S_unitary(self, k):
        """S is unitary: S * S^T = I (S is real for sl_2)."""
        S = sl2_S_matrix(k)
        I = np.eye(k + 1)
        assert np.allclose(S @ S.T, I, atol=1e-12), (
            f"S-matrix not unitary at k={k}"
        )

    @pytest.mark.parametrize("k", range(1, 11))
    def test_S_squared_is_identity(self, k):
        """S^2 = I for real symmetric unitary S."""
        S = sl2_S_matrix(k)
        I = np.eye(k + 1)
        assert np.allclose(S @ S, I, atol=1e-12), (
            f"S^2 != I at k={k}"
        )

    @pytest.mark.parametrize("k", range(1, 11))
    def test_S_00_positive(self, k):
        """S_{00} > 0 (positive normalization convention)."""
        S = sl2_S_matrix(k)
        assert S[0, 0] > 0, f"S_00 = {S[0, 0]} not positive at k={k}"

    @pytest.mark.parametrize("k", range(1, 11))
    def test_S_entries_real(self, k):
        """All S-matrix entries are real for sl_2."""
        S = sl2_S_matrix(k)
        assert S.dtype in [np.float64, np.float32], (
            f"S-matrix has non-real dtype at k={k}"
        )

    @pytest.mark.parametrize("k", range(1, 7))
    def test_S_charge_conjugation_symmetry(self, k):
        """S_{j, k-l} = (-1)^j * S_{j,l} for all j, l."""
        S = sl2_S_matrix(k)
        for j in range(k + 1):
            for l in range(k + 1):
                expected = (-1) ** j * S[j, l]
                actual = S[j, k - l]
                assert abs(actual - expected) < 1e-12, (
                    f"Charge conjugation symmetry fails at k={k}, j={j}, l={l}: "
                    f"S[{j},{k-l}]={actual} vs (-1)^{j}*S[{j},{l}]={expected}"
                )


# ===========================================================================
# II. VERLINDE FORMULA: FUSION COEFFICIENTS FOR sl_2 (k=1..6)
# ===========================================================================

class TestSl2FusionCoefficients:
    """Fusion coefficients from Verlinde formula."""

    @pytest.mark.parametrize("k", range(1, 7))
    def test_fusion_integer(self, k):
        """All N_{ij}^m are integers."""
        N = sl2_fusion_coefficients(k)
        for i in range(k + 1):
            for j in range(k + 1):
                for m in range(k + 1):
                    assert abs(N[i, j, m] - round(N[i, j, m])) < 1e-10, (
                        f"Non-integer fusion at k={k}: N_{{{i},{j}}}^{m} = {N[i,j,m]}"
                    )

    @pytest.mark.parametrize("k", range(1, 7))
    def test_fusion_nonnegative(self, k):
        """All N_{ij}^m >= 0."""
        N = sl2_fusion_coefficients(k)
        for i in range(k + 1):
            for j in range(k + 1):
                for m in range(k + 1):
                    assert round(N[i, j, m]) >= 0, (
                        f"Negative fusion at k={k}: N_{{{i},{j}}}^{m} = {N[i,j,m]}"
                    )

    @pytest.mark.parametrize("k", range(1, 7))
    def test_vacuum_fusion(self, k):
        """V_0 is the identity: N_{0,j}^m = delta_{j,m}."""
        N = sl2_fusion_coefficients(k)
        for j in range(k + 1):
            for m in range(k + 1):
                expected = 1.0 if j == m else 0.0
                assert abs(N[0, j, m] - expected) < 1e-10, (
                    f"Vacuum fusion fails at k={k}: N_{{0,{j}}}^{m} = {N[0,j,m]}"
                )

    @pytest.mark.parametrize("k", range(1, 7))
    def test_fusion_commutative(self, k):
        """Fusion is commutative: N_{ij}^m = N_{ji}^m."""
        N = sl2_fusion_coefficients(k)
        for i in range(k + 1):
            for j in range(k + 1):
                for m in range(k + 1):
                    assert abs(N[i, j, m] - N[j, i, m]) < 1e-10, (
                        f"Non-commutative fusion at k={k}: "
                        f"N_{{{i},{j}}}^{m} = {N[i,j,m]} vs N_{{{j},{i}}}^{m} = {N[j,i,m]}"
                    )

    @pytest.mark.parametrize("k", range(1, 7))
    def test_fusion_associative(self, k):
        """Fusion is associative: sum_p N_{ij}^p N_{pm}^n = sum_p N_{jm}^p N_{ip}^n."""
        N = sl2_fusion_coefficients(k)
        size = k + 1
        for i in range(size):
            for j in range(size):
                for m in range(size):
                    for n in range(size):
                        lhs = sum(round(N[i, j, p]) * round(N[p, m, n]) for p in range(size))
                        rhs = sum(round(N[j, m, p]) * round(N[i, p, n]) for p in range(size))
                        assert lhs == rhs, (
                            f"Associativity fails at k={k}, (i,j,m,n)=({i},{j},{m},{n}): "
                            f"lhs={lhs} vs rhs={rhs}"
                        )

    @pytest.mark.parametrize("k", range(1, 7))
    def test_fusion_matches_explicit(self, k):
        """Verlinde formula matches the explicit truncated CG rules."""
        N = sl2_fusion_coefficients(k)
        rules = sl2_fusion_rules_explicit(k)
        size = k + 1
        for i in range(size):
            for j in range(size):
                for m in range(size):
                    expected = rules.get((i, j, m), 0)
                    computed = round(N[i, j, m])
                    assert computed == expected, (
                        f"Mismatch at k={k}: N_{{{i},{j}}}^{m}: "
                        f"Verlinde={computed}, explicit={expected}"
                    )

    @pytest.mark.parametrize("k", range(1, 7))
    def test_fusion_orthogonality(self, k):
        """Orthogonality: sum_m N_{ij}^m * d_m = d_i * d_j (quantum dim product)."""
        N = sl2_fusion_coefficients(k)
        d = sl2_quantum_dimensions(k)
        size = k + 1
        for i in range(size):
            for j in range(size):
                lhs = sum(round(N[i, j, m]) * d[m] for m in range(size))
                rhs = d[i] * d[j]
                assert abs(lhs - rhs) < 1e-10, (
                    f"Orthogonality fails at k={k}, (i,j)=({i},{j}): "
                    f"sum N*d={lhs} vs d_i*d_j={rhs}"
                )


# ===========================================================================
# III. SHADOW TOWER: GENUS-1 S,T EXTRACTION
# ===========================================================================

class TestShadowST:
    """S,T extraction from genus-1 shadow transformation properties."""

    @pytest.mark.parametrize("k", range(1, 7))
    def test_T_consistency(self, k):
        """T diagonal matches exp(2*pi*i*(h_j - c/24))."""
        data = shadow_S_T_from_genus1(k)
        assert data["T_consistency"], f"T matrix inconsistent at k={k}"

    @pytest.mark.parametrize("k", range(1, 7))
    def test_SL2Z_relation(self, k):
        """|(ST)^3| = I (since S^2 = I in our convention)."""
        data = shadow_S_T_from_genus1(k)
        assert data["SL2Z_relation_abs"], f"SL(2,Z) relation fails at k={k}"

    @pytest.mark.parametrize("k", range(1, 7))
    def test_central_charge_formula(self, k):
        """c = 3k/(k+2)."""
        c = sl2_central_charge(k)
        expected = 3.0 * k / (k + 2)
        assert abs(c - expected) < 1e-12

    @pytest.mark.parametrize("k", range(1, 7))
    def test_conformal_weight_vacuum(self, k):
        """h_0 = 0 (vacuum has zero conformal weight)."""
        h = sl2_conformal_weights(k)
        assert abs(h[0]) < 1e-15

    @pytest.mark.parametrize("k", range(1, 7))
    def test_kappa_formula(self, k):
        """kappa(sl_2, k) = 3(k+2)/4."""
        kap = sl2_kappa(k)
        expected = 3.0 * (k + 2) / 4.0
        assert abs(kap - expected) < 1e-12


# ===========================================================================
# IV. MTC DATA FOR sl_2: BRAIDING, TWIST, RT TREFOIL
# ===========================================================================

class TestSl2MTC:
    """Full MTC data for sl_2 at k=2,3,4."""

    @pytest.mark.parametrize("k", [2, 3, 4])
    def test_twist_vacuum(self, k):
        """theta_0 = 1 (vacuum twist is trivial)."""
        theta = sl2_twist(k)
        assert abs(theta[0] - 1.0) < 1e-12

    @pytest.mark.parametrize("k", [2, 3, 4])
    def test_twist_unit_modulus(self, k):
        """All twist values have |theta_j| = 1."""
        theta = sl2_twist(k)
        for j in range(k + 1):
            assert abs(abs(theta[j]) - 1.0) < 1e-12, (
                f"|theta_{j}| = {abs(theta[j])} != 1 at k={k}"
            )

    @pytest.mark.parametrize("k", [2, 3, 4])
    def test_braiding_vacuum_channel(self, k):
        """Braiding eigenvalue on vacuum channel V_0 in V_j x V_j is exp(-2*pi*i*h_j)."""
        for j in range(1, k + 1):
            eigs, channels = sl2_braiding_eigenvalues(j, j, k)
            if 0 in channels:
                idx = channels.index(0)
                h_j = j * (j + 2) / (4.0 * (k + 2))
                expected = np.exp(-2.0j * math.pi * h_j)
                assert abs(eigs[idx] - expected) < 1e-10, (
                    f"Braiding eigenvalue on V_0 channel wrong for V_{j}xV_{j} at k={k}"
                )

    @pytest.mark.parametrize("k", [2, 3, 4])
    def test_braiding_eigenvalue_modulus(self, k):
        """All braiding eigenvalues have modulus 1."""
        for j1 in range(k + 1):
            for j2 in range(k + 1):
                eigs, _ = sl2_braiding_eigenvalues(j1, j2, k)
                for e in eigs:
                    assert abs(abs(e) - 1.0) < 1e-12

    @pytest.mark.parametrize("k", [2, 3, 4])
    def test_RT_unknot_equals_quantum_dim(self, k):
        """RT(unknot, V_j) = d_j for all j."""
        d = sl2_quantum_dimensions(k)
        for j in range(k + 1):
            rt = sl2_RT_unknot(k, j)
            assert abs(rt - d[j]) < 1e-10, (
                f"RT(unknot, V_{j}) = {rt} != d_{j} = {d[j]} at k={k}"
            )

    def test_RT_trefoil_k2(self):
        """RT(trefoil, V_1) = 2*sqrt(2) at k=2 (manual computation)."""
        rt = sl2_RT_trefoil(2)
        expected = 2.0 * math.sqrt(2)
        assert abs(rt.real - expected) < 1e-10 and abs(rt.imag) < 1e-10, (
            f"RT(trefoil) = {rt}, expected {expected} at k=2"
        )

    def test_RT_trefoil_k2_normalized(self):
        """Normalized RT(trefoil) / d_1 = 2 at k=2."""
        rt = sl2_RT_trefoil(2)
        d1 = sl2_quantum_dimensions(2)[1]
        norm = rt / d1
        assert abs(norm.real - 2.0) < 1e-10 and abs(norm.imag) < 1e-10

    @pytest.mark.parametrize("k", range(1, 8))
    def test_RT_trefoil_nonzero(self, k):
        """RT(trefoil) is nonzero for all k >= 1."""
        rt = sl2_RT_trefoil(k)
        assert abs(rt) > 1e-10, f"RT(trefoil) = 0 at k={k}"


# ===========================================================================
# V. HIGHER RANK: sl_3 AT k=1,2,3
# ===========================================================================

class TestSl3:
    """sl_3 S-matrix, fusion, Verlinde formula."""

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_integrable_weight_count(self, k):
        """Number of integrable weights = C(k+2, 2) for sl_3."""
        w = sl3_integrable_weights(k)
        expected = (k + 1) * (k + 2) // 2
        assert len(w) == expected

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_S_matrix_unitary(self, k):
        """S * S^dag = I for sl_3."""
        S = sl3_S_matrix(k)
        n = S.shape[0]
        I = np.eye(n)
        SSd = S @ np.conj(S.T)
        assert np.allclose(SSd, I, atol=1e-10), (
            f"sl_3 S-matrix not unitary at k={k}, max deviation={np.max(np.abs(SSd - I))}"
        )

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_S_matrix_symmetric(self, k):
        """S = S^T for sl_3."""
        S = sl3_S_matrix(k)
        assert np.allclose(S, S.T, atol=1e-10)

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_S_00_positive(self, k):
        """S_{00} > 0."""
        S = sl3_S_matrix(k)
        assert S[0, 0].real > 0

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_quantum_dim_vacuum(self, k):
        """d_0 = 1 (vacuum quantum dimension)."""
        d = sl3_quantum_dimensions(k)
        assert abs(d[0] - 1.0) < 1e-10

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_quantum_dim_positive(self, k):
        """All quantum dimensions are positive."""
        d = sl3_quantum_dimensions(k)
        for idx, val in enumerate(d):
            assert val > 0, (
                f"Non-positive quantum dim at k={k}, idx={idx}: d={val}"
            )

    def test_sl3_k1_Z3_fusion(self):
        """sl_3 at k=1 has Z_3 fusion ring (all dims 1, cyclic)."""
        d = sl3_quantum_dimensions(1)
        assert np.allclose(d, [1.0, 1.0, 1.0], atol=1e-10)
        N = sl3_fusion_coefficients(1)
        # V_(0,1) x V_(0,1) = V_(1,0), V_(0,1) x V_(1,0) = V_(0,0), etc.
        assert round(N[1, 1, 2]) == 1  # (0,1)x(0,1) = (1,0)
        assert round(N[1, 2, 0]) == 1  # (0,1)x(1,0) = (0,0)
        assert round(N[2, 2, 1]) == 1  # (1,0)x(1,0) = (0,1)

    def test_sl3_k2_golden_ratio(self):
        """sl_3 at k=2: fundamental has quantum dim phi = (1+sqrt(5))/2."""
        d = sl3_quantum_dimensions(2)
        phi = (1 + math.sqrt(5)) / 2
        w = sl3_integrable_weights(2)
        idx_01 = w.index((0, 1))
        idx_10 = w.index((1, 0))
        assert abs(d[idx_01] - phi) < 1e-10, f"d_(0,1) = {d[idx_01]}, expected phi"
        assert abs(d[idx_10] - phi) < 1e-10, f"d_(1,0) = {d[idx_10]}, expected phi"

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_fusion_integer_nonneg(self, k):
        """All sl_3 fusion coefficients are non-negative integers."""
        N = sl3_fusion_coefficients(k)
        num = N.shape[0]
        for i in range(num):
            for j in range(num):
                for m in range(num):
                    val = N[i, j, m]
                    assert abs(val - round(val)) < 1e-8, (
                        f"Non-integer fusion at k={k}: N[{i},{j},{m}]={val}"
                    )
                    assert round(val) >= 0, (
                        f"Negative fusion at k={k}: N[{i},{j},{m}]={val}"
                    )

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_vacuum_fusion(self, k):
        """V_0 is identity in sl_3 fusion."""
        N = sl3_fusion_coefficients(k)
        num = N.shape[0]
        for j in range(num):
            for m in range(num):
                expected = 1.0 if j == m else 0.0
                assert abs(N[0, j, m] - expected) < 1e-8

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_fusion_orthogonality(self, k):
        """sum_m N_{ij}^m * d_m = d_i * d_j for sl_3."""
        N = sl3_fusion_coefficients(k)
        d = sl3_quantum_dimensions(k)
        num = N.shape[0]
        for i in range(num):
            for j in range(num):
                lhs = sum(round(N[i, j, m]) * d[m] for m in range(num))
                rhs = d[i] * d[j]
                assert abs(lhs - rhs) < 1e-8, (
                    f"sl_3 orthogonality fails: k={k}, i={i}, j={j}, "
                    f"sum={lhs}, product={rhs}"
                )

    def test_sl3_k3_adjoint_dim(self):
        """sl_3 at k=3: adjoint rep (1,1) has quantum dim 3."""
        d = sl3_quantum_dimensions(3)
        w = sl3_integrable_weights(3)
        idx_11 = w.index((1, 1))
        assert abs(d[idx_11] - 3.0) < 1e-10, (
            f"d_(1,1) at k=3 = {d[idx_11]}, expected 3.0"
        )


# ===========================================================================
# VI. QUANTUM DIMENSIONS: d_j, D^2, k=1..20
# ===========================================================================

class TestQuantumDimensions:
    """Quantum dimensions d_j and total D^2."""

    @pytest.mark.parametrize("k", range(1, 21))
    def test_vacuum_dim_one(self, k):
        """d_0 = 1."""
        d = sl2_quantum_dimensions(k)
        assert abs(d[0] - 1.0) < 1e-12

    @pytest.mark.parametrize("k", range(1, 21))
    def test_all_positive(self, k):
        """All quantum dimensions are positive."""
        d = sl2_quantum_dimensions(k)
        for j in range(k + 1):
            assert d[j] > 0, f"d_{j} = {d[j]} not positive at k={k}"

    @pytest.mark.parametrize("k", range(1, 21))
    def test_charge_conjugation_symmetry(self, k):
        """d_j = d_{k-j}."""
        d = sl2_quantum_dimensions(k)
        for j in range(k + 1):
            assert abs(d[j] - d[k - j]) < 1e-12, (
                f"d_{j} = {d[j]} != d_{k-j} = {d[k-j]} at k={k}"
            )

    @pytest.mark.parametrize("k", range(1, 21))
    def test_D_squared_formula(self, k):
        """D^2 = sum d_j^2 = 1/S_{00}^2."""
        D2_sum = sl2_total_quantum_dimension_sq(k)
        D2_formula = sl2_total_quantum_dimension_sq_formula(k)
        assert abs(D2_sum - D2_formula) < 1e-10, (
            f"D^2 mismatch at k={k}: sum={D2_sum}, formula={D2_formula}"
        )

    @pytest.mark.parametrize("k", range(1, 21))
    def test_quantum_dim_agrees_with_formula(self, k):
        """d_j from S-matrix agrees with sin formula."""
        d_S = sl2_quantum_dimensions(k)
        for j in range(k + 1):
            d_formula = sl2_quantum_dimension_formula(j, k)
            assert abs(d_S[j] - d_formula) < 1e-12, (
                f"d_{j} mismatch at k={k}: S-matrix={d_S[j]}, formula={d_formula}"
            )

    def test_D_squared_k1(self):
        """D^2 = 2 at k=1."""
        assert abs(sl2_total_quantum_dimension_sq(1) - 2.0) < 1e-12

    def test_D_squared_k2(self):
        """D^2 = 4 at k=2."""
        assert abs(sl2_total_quantum_dimension_sq(2) - 4.0) < 1e-12

    def test_D_squared_k4(self):
        """D^2 = 12 at k=4."""
        assert abs(sl2_total_quantum_dimension_sq(4) - 12.0) < 1e-12

    def test_fundamental_dim_k1(self):
        """d_1 = 1 at k=1."""
        d = sl2_quantum_dimensions(1)
        assert abs(d[1] - 1.0) < 1e-12

    def test_fundamental_dim_k2(self):
        """d_1 = sqrt(2) at k=2."""
        d = sl2_quantum_dimensions(2)
        assert abs(d[1] - math.sqrt(2)) < 1e-12

    def test_fundamental_dim_k3(self):
        """d_1 = golden ratio phi at k=3."""
        d = sl2_quantum_dimensions(3)
        phi = (1 + math.sqrt(5)) / 2
        assert abs(d[1] - phi) < 1e-12

    def test_fundamental_dim_k4(self):
        """d_1 = sqrt(3) at k=4."""
        d = sl2_quantum_dimensions(4)
        assert abs(d[1] - math.sqrt(3)) < 1e-12


# ===========================================================================
# VII. VERLINDE RING: RECURSION, TRUNCATION, VACUUM FOR k=2,3,4
# ===========================================================================

class TestVerlindeRing:
    """Verlinde ring structure V_k(sl_2)."""

    @pytest.mark.parametrize("k", [2, 3, 4])
    def test_chebyshev_recursion(self, k):
        """V_1 * V_j = V_{j-1} + V_{j+1} for 0 < j < k."""
        rel = sl2_verlinde_ring_relation(k)
        assert rel["chebyshev_recursion_holds"], (
            f"Chebyshev recursion fails at k={k}"
        )

    @pytest.mark.parametrize("k", [2, 3, 4])
    def test_truncation(self, k):
        """V_1 * V_k = V_{k-1} (truncation, i.e., V_{k+1} = 0)."""
        rel = sl2_verlinde_ring_relation(k)
        assert rel["truncation_holds"], f"Truncation fails at k={k}"

    @pytest.mark.parametrize("k", [2, 3, 4])
    def test_vacuum_identity(self, k):
        """V_0 * V_j = V_j for all j."""
        rel = sl2_verlinde_ring_relation(k)
        assert rel["vacuum_identity_holds"], (
            f"Vacuum identity fails at k={k}"
        )

    def test_k2_V1_cubed(self):
        """At k=2: [V_1]^3 = 2*[V_1] (Chebyshev: U_3(x/2) = x^3 - 2x)."""
        powers = sl2_generator_powers(2)
        assert np.allclose(powers[3], [0, 2, 0], atol=1e-10)

    def test_k3_V1_fourth(self):
        """At k=3: [V_1]^4 = 2*[V_0] + 3*[V_2]."""
        powers = sl2_generator_powers(3)
        assert np.allclose(powers[4], [2, 0, 3, 0], atol=1e-10)

    def test_k4_V1_squared(self):
        """At k=4: [V_1]^2 = [V_0] + [V_2]."""
        powers = sl2_generator_powers(4)
        assert np.allclose(powers[2], [1, 0, 1, 0, 0], atol=1e-10)

    @pytest.mark.parametrize("k", [2, 3, 4])
    def test_ring_multiplication_agrees(self, k):
        """Ring multiplication table equals fusion coefficients."""
        M = sl2_verlinde_ring_multiplication(k)
        N = sl2_fusion_coefficients(k)
        assert np.allclose(M, N, atol=1e-10)


# ===========================================================================
# VIII. GENUS-g VERLINDE: Z_g FOR g=0..4, k=1..5
# ===========================================================================

class TestGenusGVerlinde:
    """Genus-g Verlinde dimensions and shadow F_g."""

    @pytest.mark.parametrize("k", range(1, 6))
    def test_genus_0_is_one(self, k):
        """Z_0 = 1 for all k (by unitarity)."""
        Z0 = sl2_verlinde_genus_g_exact(k, 0)
        assert Z0 == 1, f"Z_0 = {Z0} at k={k}, expected 1"

    @pytest.mark.parametrize("k", range(1, 6))
    def test_genus_1_is_k_plus_1(self, k):
        """Z_1 = k+1 (number of integrable reps)."""
        Z1 = sl2_verlinde_genus_g_exact(k, 1)
        assert Z1 == k + 1, f"Z_1 = {Z1} at k={k}, expected {k+1}"

    @pytest.mark.parametrize("k,g,expected", [
        (k, g, SL2_VERLINDE_TABLE[(k, g)])
        for (k, g) in SL2_VERLINDE_TABLE
    ])
    def test_verlinde_table(self, k, g, expected):
        """Verify against the Verlinde dimension table."""
        computed = sl2_verlinde_genus_g_exact(k, g)
        assert computed == expected, (
            f"Verlinde dim mismatch at k={k}, g={g}: computed={computed}, expected={expected}"
        )

    @pytest.mark.parametrize("k", range(1, 6))
    def test_genus_g_positive(self, k):
        """Z_g > 0 for all g >= 0."""
        for g in range(5):
            Z = sl2_verlinde_genus_g(k, g)
            assert Z > 0, f"Z_{g} = {Z} not positive at k={k}"

    @pytest.mark.parametrize("k", range(1, 6))
    def test_genus_g_integer(self, k):
        """Z_g is always an integer."""
        for g in range(5):
            Z = sl2_verlinde_genus_g(k, g)
            assert abs(Z - round(Z)) < 1e-8, (
                f"Z_{g} = {Z} not integer at k={k}"
            )

    @pytest.mark.parametrize("k", range(1, 6))
    def test_alternative_formula_agrees(self, k):
        """Z_g via quantum dimensions agrees with direct formula."""
        for g in range(5):
            Z1 = sl2_verlinde_genus_g(k, g)
            Z2 = sl2_verlinde_genus_g_formula(k, g)
            assert abs(Z1 - Z2) < 1e-10, (
                f"Alternative formula disagrees at k={k}, g={g}: {Z1} vs {Z2}"
            )

    def test_k1_genus_g_powers_of_2(self):
        """At k=1: Z_g = 2^g for g >= 0."""
        for g in range(8):
            Z = sl2_verlinde_genus_g_exact(1, g)
            assert Z == 2 ** g, f"Z_{g}(k=1) = {Z}, expected {2**g}"

    def test_shadow_F_1(self):
        """F_1 = kappa/24."""
        for k in range(1, 6):
            F1 = sl2_shadow_F_g(k, 1)
            kap = sl2_kappa(k)
            assert abs(F1 - kap / 24.0) < 1e-12, (
                f"F_1 = {F1} != kappa/24 = {kap/24} at k={k}"
            )

    def test_shadow_F_g_positive(self):
        """F_g > 0 for all g >= 1 (kappa > 0 for positive level)."""
        for k in range(1, 6):
            for g in range(1, 5):
                F = sl2_shadow_F_g(k, g)
                assert F > 0, f"F_{g} = {F} not positive at k={k}"

    def test_shadow_F_g_proportional_to_kappa(self):
        """F_g is proportional to kappa: F_g(k1)/kappa(k1) = F_g(k2)/kappa(k2)."""
        for g in range(1, 5):
            ratios = []
            for k in range(1, 6):
                F = sl2_shadow_F_g(k, g)
                kap = sl2_kappa(k)
                ratios.append(F / kap)
            for r in ratios:
                assert abs(r - ratios[0]) < 1e-12, (
                    f"F_{g}/kappa not constant: ratios={ratios}"
                )


# ===========================================================================
# IX. CROSS-CHECKS AND CONSISTENCY
# ===========================================================================

class TestCrossChecks:
    """Cross-checks between different computational methods."""

    def test_verify_verlinde_table_all(self):
        """All entries in the Verlinde table are correct."""
        results = verify_verlinde_table()
        for (k, g), ok in results.items():
            assert ok, f"Verlinde table entry ({k},{g}) incorrect"

    @pytest.mark.parametrize("k", range(1, 6))
    def test_exact_vs_float_S_matrix(self, k):
        """Symbolic and numerical S-matrices agree."""
        S_num = sl2_S_matrix(k)
        S_sym = sl2_S_matrix_exact(k)
        for j in range(k + 1):
            for l in range(k + 1):
                sym_val = float(S_sym[j, l].evalf())
                assert abs(S_num[j, l] - sym_val) < 1e-12, (
                    f"S[{j},{l}] disagrees: num={S_num[j,l]}, sym={sym_val} at k={k}"
                )

    @pytest.mark.parametrize("k", range(1, 11))
    def test_kappa_and_central_charge_correct(self, k):
        """kappa = 3(k+2)/4 and c = 3k/(k+2)."""
        kap = sl2_kappa(k)
        c = sl2_central_charge(k)
        assert abs(kap - 3.0 * (k + 2) / 4.0) < 1e-12
        assert abs(c - 3.0 * k / (k + 2)) < 1e-12

    def test_sl3_weight_count(self):
        """Number of sl_3 weights: k=1 -> 3, k=2 -> 6, k=3 -> 10."""
        assert len(sl3_integrable_weights(1)) == 3
        assert len(sl3_integrable_weights(2)) == 6
        assert len(sl3_integrable_weights(3)) == 10

    def test_sl3_quantum_dim_matches_S_matrix(self):
        """sl_3 quantum dims from Weyl formula agree with S-matrix ratio."""
        for k in [1, 2, 3]:
            d_weyl = sl3_quantum_dimensions(k)
            S = sl3_S_matrix(k)
            s00 = S[0, 0]
            for j in range(len(d_weyl)):
                d_S = abs(S[0, j]) / abs(s00)
                assert abs(d_weyl[j] - d_S) < 1e-8, (
                    f"sl_3 k={k}, j={j}: Weyl dim={d_weyl[j]}, S-matrix dim={d_S}"
                )

    @pytest.mark.parametrize("k", range(1, 6))
    def test_fusion_sum_equals_D_squared(self, k):
        """sum_{i,j} N_{ij}^0 * d_i * d_j = D^2."""
        N = sl2_fusion_coefficients(k)
        d = sl2_quantum_dimensions(k)
        D2 = sl2_total_quantum_dimension_sq(k)
        size = k + 1
        total = sum(round(N[i, j, 0]) * d[i] * d[j]
                     for i in range(size) for j in range(size))
        assert abs(total - D2) < 1e-10

    @pytest.mark.parametrize("k", range(2, 6))
    def test_genus_g_nondecreasing(self, k):
        """For k >= 2: Z_g is non-decreasing in g (for g >= 1)."""
        for g in range(1, 4):
            Z_g = sl2_verlinde_genus_g(k, g)
            Z_g1 = sl2_verlinde_genus_g(k, g + 1)
            assert Z_g1 >= Z_g - 1e-10, (
                f"Z_{g+1} < Z_{g} at k={k}: {Z_g1} < {Z_g}"
            )
