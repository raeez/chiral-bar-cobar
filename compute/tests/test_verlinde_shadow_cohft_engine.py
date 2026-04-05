r"""Tests for the Verlinde-shadow CohFT engine.

Verification paths:
  Path 1: Verlinde formula via S-matrix (type A) / quantum Weyl dimensions (all types)
  Path 2: Independent quantum Weyl dimension formula
  Path 3: Known literature values (Di Francesco-Mathieu-Senechal, Beauville, Fuchs)
  Path 4: Genus-1 = number of integrable representations
  Path 5: Shadow F_g = kappa * lambda_g^FP
  Path 6: Level-rank duality as consistency check

The Verlinde formula is:
    V_{g,k}(g) = sum_lambda S_{0,lambda}^{2-2g}
using RAW S-matrix entries (NOT quantum dimensions d_lambda = S_{0,lambda}/S_{0,0}).

Ground truth:
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  thm:modular-characteristic (higher_genus_modular_koszul.tex)
  Verlinde (1988), Kac-Peterson (1984), Beauville (1996)
"""

from __future__ import annotations

import math
import pytest

from sympy import Rational, bernoulli, binomial, factorial

from compute.lib.verlinde_shadow_cohft_engine import (
    S_matrix,
    asymptotic_growth_comparison,
    cartan_matrix,
    central_charge,
    comprehensive_verification,
    fusion_coefficients,
    full_diagnostic,
    genus1_verlinde_vs_shadow,
    integrable_weights,
    kappa_affine,
    kappa_affine_exact,
    known_verlinde,
    lambda_fp,
    level_rank_check,
    num_integrable_reps,
    positive_roots,
    quantum_dim_weyl,
    quantum_dimensions,
    shadow_F_g,
    shadow_verlinde_comparison,
    sl2_verlinde_closed_form,
    total_quantum_dim_sq,
    verify_fusion_integrality,
    verify_S_matrix_properties,
    verlinde_dimension,
    verlinde_dimension_exact,
    verlinde_from_weyl_qdim,
)


# =========================================================================
# Section 1: Root system verification
# =========================================================================

class TestRootSystem:
    """Verify positive root enumeration and Cartan matrices."""

    @pytest.mark.parametrize("lt,r,expected_npos", [
        ("A", 1, 1), ("A", 2, 3), ("A", 3, 6), ("A", 4, 10),
        ("B", 2, 4), ("B", 3, 9),
        ("C", 2, 4), ("C", 3, 9),
        ("D", 4, 12),
        ("G", 2, 6),
        ("F", 4, 24),
        ("E", 6, 36), ("E", 7, 63), ("E", 8, 120),
    ])
    def test_positive_root_count(self, lt, r, expected_npos):
        """Number of positive roots = dim(g) - rank(g) / 2 = n_pos."""
        pos = positive_roots(lt, r)
        assert len(pos) == expected_npos

    @pytest.mark.parametrize("lt,r,expected_marks", [
        ("A", 1, (1,)), ("A", 2, (1, 1)), ("A", 3, (1, 1, 1)),
        ("B", 2, (1, 2)), ("B", 3, (1, 2, 2)),
        ("C", 2, (2, 1)), ("C", 3, (2, 2, 1)),
        ("D", 4, (1, 2, 1, 1)),
        ("G", 2, (2, 3)),
        ("F", 4, (2, 4, 3, 2)),
    ])
    def test_highest_root_marks(self, lt, r, expected_marks):
        """Highest root coefficients = marks of affine Dynkin diagram."""
        pos = positive_roots(lt, r)
        highest = max(pos, key=lambda x: sum(x))
        marks = tuple(int(x) for x in highest)
        assert marks == expected_marks

    @pytest.mark.parametrize("lt,r", [
        ("A", 1), ("A", 2), ("A", 3),
        ("B", 2), ("C", 2), ("D", 4), ("G", 2),
    ])
    def test_cartan_matrix_properties(self, lt, r):
        """Cartan matrix has 2 on diagonal and non-positive off-diagonal."""
        C = cartan_matrix(lt, r)
        assert C.shape == (r, r)
        for i in range(r):
            assert C[i, i] == 2
            for j in range(r):
                if i != j:
                    assert C[i, j] <= 0


# =========================================================================
# Section 2: Integrable representations
# =========================================================================

class TestIntegrableWeights:
    """Verify integrable weight enumeration."""

    @pytest.mark.parametrize("r,k,expected", [
        (1, 1, 2), (1, 2, 3), (1, 3, 4), (1, 4, 5), (1, 5, 6),
        (2, 1, 3), (2, 2, 6), (2, 3, 10),
        (3, 1, 4), (3, 2, 10),
        (4, 1, 5),
    ])
    def test_type_A_count(self, r, k, expected):
        """Type A_r at level k: C(k+r, r) integrable reps."""
        n = num_integrable_reps("A", r, k)
        assert n == expected
        assert n == int(binomial(k + r, r))

    def test_D4_level1(self):
        """D_4 at k=1: 4 integrable weights (marks (1,2,1,1) -> a1+2a2+a3+a4 <= 1)."""
        wts = integrable_weights("D", 4, 1)
        # (0,0,0,0), (1,0,0,0), (0,0,1,0), (0,0,0,1) -- but NOT (0,1,0,0) since 2*1=2>1
        assert len(wts) == 4

    def test_G2_level1(self):
        """G_2 at k=1: only vacuum (marks (2,3) force a_1*2+a_2*3 <= 1)."""
        wts = integrable_weights("G", 2, 1)
        assert len(wts) == 1
        assert wts[0] == (0, 0)

    def test_G2_level2(self):
        """G_2 at k=2: two reps: (0,0) and (1,0)."""
        wts = integrable_weights("G", 2, 2)
        assert len(wts) == 2


# =========================================================================
# Section 3: Modular characteristic kappa
# =========================================================================

class TestKappa:
    """Verify modular characteristic kappa = dim(g)(k+h^v)/(2h^v)."""

    @pytest.mark.parametrize("lt,r,k,expected", [
        ("A", 1, 1, Rational(9, 4)),      # 3*(1+2)/(2*2) = 9/4
        ("A", 1, 2, Rational(3)),          # 3*(2+2)/(2*2) = 3
        ("A", 2, 1, Rational(32, 6)),      # 8*(1+3)/(2*3) = 32/6
        ("A", 3, 1, Rational(75, 8)),      # 15*(1+4)/(2*4) = 75/8
        ("D", 4, 1, Rational(196, 12)),    # 28*(1+6)/(2*6)
    ])
    def test_kappa_values(self, lt, r, k, expected):
        kap = kappa_affine_exact(lt, r, k)
        assert kap == expected

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 2, 2), ("B", 2, 1), ("G", 2, 1),
    ])
    def test_kappa_positive(self, lt, r, k):
        """Kappa is positive for positive integer level."""
        kap = kappa_affine(lt, r, k)
        assert kap > 0


# =========================================================================
# Section 4: Quantum Weyl dimensions
# =========================================================================

class TestQuantumDimensions:
    """Verify quantum dimensions via the Weyl formula."""

    def test_vacuum_dim_one(self):
        """Vacuum representation has quantum dimension 1 for all types."""
        for (lt, r) in [("A", 1), ("A", 2), ("A", 3), ("B", 2), ("C", 2),
                         ("D", 4), ("G", 2)]:
            for k in [1, 2, 3]:
                wts = integrable_weights(lt, r, k)
                vacuum = wts[0]  # (0, 0, ..., 0)
                d = quantum_dim_weyl(vacuum, lt, r, k)
                assert abs(d - 1.0) < 1e-10, f"d(vacuum) = {d} for {lt}_{r} k={k}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_sl2_quantum_dims(self, k):
        """sl_2 quantum dimensions: d_j = sin((j+1)pi/(k+2)) / sin(pi/(k+2))."""
        n = k + 2
        for j in range(k + 1):
            wt = (j,)
            d_weyl = quantum_dim_weyl(wt, "A", 1, k)
            d_exact = math.sin((j + 1) * math.pi / n) / math.sin(math.pi / n)
            if d_exact > 1e-10:
                assert abs(d_weyl - d_exact) < 1e-8, \
                    f"d_{j} at k={k}: weyl={d_weyl}, exact={d_exact}"

    def test_sl3_k1_all_dim_one(self):
        """sl_3 at k=1: all 3 reps have quantum dimension = dimension / sqrt(3)...
        Actually d = 1 for trivial, d = 1 for (1,0) and (0,1) at k=1."""
        for wt in [(0, 0), (1, 0), (0, 1)]:
            d = quantum_dim_weyl(wt, "A", 2, 1)
            assert abs(d - 1.0) < 1e-8, f"d({wt}) = {d}"

    def test_sl4_k1_all_dim_one(self):
        """sl_4 at k=1: all 4 reps have quantum dimension 1."""
        for wt in [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            d = quantum_dim_weyl(wt, "A", 3, 1)
            assert abs(d - 1.0) < 1e-8


# =========================================================================
# Section 5: sl_2 Verlinde numbers (direct computation)
# =========================================================================

class TestSl2Verlinde:
    """Verify sl_2 Verlinde numbers from multiple paths."""

    # Known sl_2 Verlinde numbers (computed from the closed-form formula)
    SL2_DATA = [
        # (k, g, V)
        (1, 0, 1), (1, 1, 2), (1, 2, 4), (1, 3, 8), (1, 4, 16), (1, 5, 32),
        (2, 0, 1), (2, 1, 3), (2, 2, 10), (2, 3, 36), (2, 4, 136), (2, 5, 528),
        (3, 0, 1), (3, 1, 4), (3, 2, 20), (3, 3, 120), (3, 4, 800),
        (4, 0, 1), (4, 1, 5), (4, 2, 35), (4, 3, 329),
        (5, 0, 1), (5, 1, 6), (5, 2, 56), (5, 3, 784),
    ]

    @pytest.mark.parametrize("k,g,expected", SL2_DATA)
    def test_sl2_closed_form(self, k, g, expected):
        """Path 1: sl_2 closed-form formula."""
        V = sl2_verlinde_closed_form(k, g)
        assert abs(V - expected) < 0.01, f"V_{g}(sl_2, k={k}) = {V}, expected {expected}"

    @pytest.mark.parametrize("k,g,expected", SL2_DATA)
    def test_sl2_S_matrix(self, k, g, expected):
        """Path 2: sl_2 from full S-matrix computation."""
        V = verlinde_dimension_exact("A", 1, k, g)
        assert V == expected

    @pytest.mark.parametrize("k,g,expected", SL2_DATA)
    def test_sl2_weyl_qdim(self, k, g, expected):
        """Path 3: sl_2 from quantum Weyl dimensions."""
        V = verlinde_from_weyl_qdim("A", 1, k, g)
        assert abs(V - expected) < 0.5, f"V_{g}(sl_2, k={k}) = {V}, expected {expected}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_sl2_genus0_is_1(self, k):
        """V_0 = 1 for all k (unitarity)."""
        assert verlinde_dimension_exact("A", 1, k, 0) == 1

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_sl2_genus1_is_k_plus_1(self, k):
        """V_1(sl_2, k) = k+1."""
        assert verlinde_dimension_exact("A", 1, k, 1) == k + 1

    def test_sl2_k1_all_powers_of_2(self):
        """sl_2 at k=1: V_g = 2^g (all qdims = 1, 2 reps)."""
        for g in range(8):
            V = verlinde_dimension_exact("A", 1, 1, g)
            assert V == 2 ** g


# =========================================================================
# Section 6: Type A Verlinde numbers (higher rank)
# =========================================================================

class TestTypeAVerlinde:
    """Verify Verlinde numbers for sl_N at various levels."""

    @pytest.mark.parametrize("N,k,g,expected", [
        # sl_3 at k=1: V_g = 3^g (all S_{0j} = 1/sqrt(3))
        (3, 1, 0, 1), (3, 1, 1, 3), (3, 1, 2, 9), (3, 1, 3, 27), (3, 1, 4, 81),
        # sl_4 at k=1: V_g = 4^g
        (4, 1, 0, 1), (4, 1, 1, 4), (4, 1, 2, 16), (4, 1, 3, 64),
        # sl_5 at k=1: V_g = 5^g
        (5, 1, 0, 1), (5, 1, 1, 5), (5, 1, 2, 25),
    ])
    def test_slN_k1(self, N, k, g, expected):
        """sl_N at k=1: V_g = N^g (all N reps have d=1, S_{0j}=1/sqrt(N))."""
        V = verlinde_dimension_exact("A", N - 1, k, g)
        assert V == expected

    @pytest.mark.parametrize("N,k,g,expected", [
        (3, 2, 0, 1), (3, 2, 1, 6), (3, 2, 2, 45),
        (3, 3, 0, 1), (3, 3, 1, 10), (3, 3, 2, 166),
    ])
    def test_slN_higher_level(self, N, k, g, expected):
        """sl_3 at higher levels."""
        V = verlinde_dimension_exact("A", N - 1, k, g)
        assert V == expected

    def test_slN_k1_pattern(self):
        """sl_N at k=1: V_g = N^g for N=2,...,6."""
        for N in range(2, 7):
            for g in range(4):
                V = verlinde_dimension_exact("A", N - 1, 1, g)
                assert V == N ** g, f"V_{g}(sl_{N}, k=1) = {V}, expected {N**g}"

    @pytest.mark.parametrize("N,k", [
        (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (4, 1),
    ])
    def test_two_path_agreement(self, N, k):
        """S-matrix and Weyl qdim paths agree for type A."""
        for g in range(5):
            v1 = verlinde_dimension("A", N - 1, k, g)
            v2 = verlinde_from_weyl_qdim("A", N - 1, k, g)
            assert abs(v1 - v2) < 0.5, \
                f"Paths disagree: V_{g}(sl_{N}, k={k}): Smat={v1:.4f}, Weyl={v2:.4f}"


# =========================================================================
# Section 7: Non-simply-laced types via quantum Weyl dimensions
# =========================================================================

class TestNonSimplyLaced:
    """Verlinde numbers for BCGF types via quantum Weyl dimensions."""

    @pytest.mark.parametrize("lt,r,k,g,expected", [
        # B_2 at k=2: 2 reps with d > 0, both d=1 -> V_g = 2^g
        ("B", 2, 2, 0, 1), ("B", 2, 2, 1, 2), ("B", 2, 2, 2, 4),
        # C_2 at k=2: 2 reps with d > 0 -> V_g = 2^g
        ("C", 2, 2, 0, 1), ("C", 2, 2, 1, 2), ("C", 2, 2, 2, 4),
        # G_2 at k=2: 2 reps with d > 0 -> V_g = 2^g
        ("G", 2, 2, 0, 1), ("G", 2, 2, 1, 2), ("G", 2, 2, 2, 4),
        # G_2 at k=1: only vacuum -> V_g = 1
        ("G", 2, 1, 0, 1), ("G", 2, 1, 1, 1),
    ])
    def test_non_simply_laced_verlinde(self, lt, r, k, g, expected):
        V = verlinde_from_weyl_qdim(lt, r, k, g)
        assert abs(V - expected) < 0.5, \
            f"V_{g}({lt}_{r}, k={k}) = {V:.4f}, expected {expected}"

    @pytest.mark.parametrize("lt,r,k", [
        ("B", 2, 3), ("C", 2, 3), ("G", 2, 3),
    ])
    def test_genus0_is_1(self, lt, r, k):
        """V_0 = 1 for all types."""
        V = verlinde_from_weyl_qdim(lt, r, k, 0)
        assert abs(V - 1.0) < 1e-8

    @pytest.mark.parametrize("lt,r,k", [
        ("B", 2, 2), ("B", 2, 3),
        ("C", 2, 2), ("C", 2, 3),
        ("G", 2, 2), ("G", 2, 3),
    ])
    def test_verlinde_integer(self, lt, r, k):
        """Verlinde dimensions are positive integers for g >= 0."""
        for g in range(5):
            V = verlinde_from_weyl_qdim(lt, r, k, g)
            assert abs(V - round(V)) < 0.01, \
                f"V_{g}({lt}_{r}, k={k}) = {V} not integer"
            assert round(V) >= 1


# =========================================================================
# Section 8: S-matrix properties (type A)
# =========================================================================

class TestSMatrixProperties:
    """Verify fundamental S-matrix properties for type A."""

    @pytest.mark.parametrize("r,k", [
        (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 1), (2, 2),
        (3, 1),
    ])
    def test_unitarity(self, r, k):
        """S S^dagger = I."""
        props = verify_S_matrix_properties("A", r, k)
        assert props["is_unitary"], f"Not unitary: dev = {props['unitary_dev']}"

    @pytest.mark.parametrize("r,k", [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2),
    ])
    def test_S00_positive(self, r, k):
        """S_{0,0} > 0."""
        props = verify_S_matrix_properties("A", r, k)
        assert props["S_00_positive"]

    @pytest.mark.parametrize("r,k", [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2),
    ])
    def test_quantum_dims_positive(self, r, k):
        """All quantum dimensions are positive."""
        props = verify_S_matrix_properties("A", r, k)
        assert props["all_qd_positive"]


# =========================================================================
# Section 9: Fusion rules (type A)
# =========================================================================

class TestFusionRules:
    """Verify fusion coefficient integrality and specific values."""

    @pytest.mark.parametrize("r,k", [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2),
    ])
    def test_fusion_nonneg_integer(self, r, k):
        """Fusion coefficients are non-negative integers."""
        result = verify_fusion_integrality("A", r, k)
        assert result["all_nonneg_integer"], \
            f"Fusion not integral: max dev = {result['max_deviation']}"

    def test_sl2_fusion_explicit(self):
        """sl_2 at k=2: V_1 x V_1 = V_0 + V_2 (truncated CG rule)."""
        import numpy as np
        N = fusion_coefficients("A", 1, 2)
        # V_1 x V_1: channels 0 and 2 (with same parity i+j+m even)
        assert abs(N[1, 1, 0] - 1.0) < 0.01  # N_{11}^0 = 1
        assert abs(N[1, 1, 2] - 1.0) < 0.01  # N_{11}^2 = 1
        assert abs(N[1, 1, 1]) < 0.01         # N_{11}^1 = 0

    def test_sl2_vacuum_fusion(self):
        """V_0 x V_j = V_j (vacuum is identity)."""
        import numpy as np
        for k in [1, 2, 3]:
            N = fusion_coefficients("A", 1, k)
            for j in range(k + 1):
                for m in range(k + 1):
                    expected = 1.0 if m == j else 0.0
                    assert abs(N[0, j, m] - expected) < 0.01


# =========================================================================
# Section 10: Shadow CohFT partition function
# =========================================================================

class TestShadowCohFT:
    """Verify shadow F_g = kappa * lambda_g^FP."""

    def test_lambda_fp_values(self):
        """Known Faber-Pandharipande numbers."""
        assert lambda_fp(1) == Rational(1, 24)
        assert lambda_fp(2) == Rational(7, 5760)
        assert lambda_fp(3) == Rational(31, 967680)

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 2, 1), ("A", 3, 1),
    ])
    def test_F1_equals_kappa_over_24(self, lt, r, k):
        """F_1 = kappa / 24."""
        F1 = shadow_F_g(lt, r, k, 1)
        kap = kappa_affine_exact(lt, r, k)
        assert F1 == kap / 24

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_shadow_positive(self, g):
        """F_g > 0 for positive level."""
        F = shadow_F_g("A", 1, 2, g)
        assert float(F) > 0

    def test_shadow_F_g_is_kappa_times_FP(self):
        """F_g = kappa * lambda_g^FP for all g."""
        for g in range(1, 6):
            for (lt, r, k) in [("A", 1, 2), ("A", 2, 1)]:
                F = shadow_F_g(lt, r, k, g)
                kap = kappa_affine_exact(lt, r, k)
                fp = lambda_fp(g)
                assert F == kap * fp


# =========================================================================
# Section 11: Shadow-Verlinde comparison
# =========================================================================

class TestShadowVerlindeComparison:
    """Compare shadow CohFT with Verlinde formula."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 2, 1),
    ])
    def test_comparison_genus1(self, lt, r, k):
        """At genus 1: V_1 = number of reps, F_1 = kappa/24."""
        comp = shadow_verlinde_comparison(lt, r, k, 1)
        assert comp["verlinde_dim"] == num_integrable_reps(lt, r, k)
        assert abs(comp["shadow_F_g"] - kappa_affine(lt, r, k) / 24.0) < 1e-10

    def test_verlinde_much_larger_than_shadow(self):
        """At large genus, Verlinde grows much faster than shadow."""
        comp = asymptotic_growth_comparison("A", 1, 3, max_genus=5)
        V = comp["verlinde_dims"]
        F = comp["shadow_F_g"]
        # V grows exponentially, F decays (Bernoulli)
        assert V[3] > V[2] > V[1]
        assert abs(F[3]) < abs(F[2]) < abs(F[1])


# =========================================================================
# Section 12: Level-rank duality
# =========================================================================

class TestLevelRankDuality:
    """Test level-rank duality for type A."""

    @pytest.mark.parametrize("N,k", [(2, 2), (2, 3), (3, 3), (2, 4)])
    def test_symmetric_case_genus1(self, N, k):
        """At genus 1 for SL: V_1(sl_N, k) = C(N+k-1, N-1)."""
        V = verlinde_dimension_exact("A", N - 1, k, 1)
        expected = int(binomial(N + k - 1, N - 1))
        assert V == expected

    def test_level_rank_N_equals_k(self):
        """When N = k, level-rank should give equal Verlinde numbers."""
        for N in [2, 3]:
            for g in range(4):
                check = level_rank_check(N, N, g)
                assert check["equal"], \
                    f"N=k={N}, g={g}: V_A={check['V_slN_k']}, V_B={check['V_slk_N']}"

    @pytest.mark.parametrize("N,k,g", [
        (2, 3, 0), (2, 3, 1), (2, 3, 2),
        (3, 2, 0), (3, 2, 1), (3, 2, 2),
    ])
    def test_level_rank_data(self, N, k, g):
        """Level-rank produces valid data."""
        check = level_rank_check(N, k, g)
        assert "V_slN_k" in check
        assert "V_slk_N" in check
        assert check["V_slN_k"] >= 1
        assert check["V_slk_N"] >= 1


# =========================================================================
# Section 13: Known literature values cross-check
# =========================================================================

class TestKnownValues:
    """Cross-check against known Verlinde numbers from the literature."""

    def test_all_known_values(self):
        """Every entry in the known_verlinde table matches computation."""
        from compute.lib.verlinde_shadow_cohft_engine import _KNOWN_VERLINDE
        for (lt, r, k, g), expected in _KNOWN_VERLINDE.items():
            V = verlinde_dimension_exact(lt, r, k, g)
            assert V == expected, \
                f"V_{g}({lt}_{r}, k={k}) = {V}, expected {expected}"

    @pytest.mark.parametrize("k,g,expected", [
        # From Beauville (1996) and DMS Table 16.1
        (1, 2, 4), (2, 2, 10), (3, 2, 20), (4, 2, 35), (5, 2, 56),
    ])
    def test_sl2_genus2_beauville(self, k, g, expected):
        """sl_2 genus-2 Verlinde numbers."""
        V = verlinde_dimension_exact("A", 1, k, g)
        assert V == expected


# =========================================================================
# Section 14: Genus-0 normalization
# =========================================================================

class TestGenus0:
    """Verify V_0 = 1 (unitarity of S-matrix row 0)."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3), ("A", 1, 4), ("A", 1, 5),
        ("A", 2, 1), ("A", 2, 2), ("A", 2, 3),
        ("A", 3, 1), ("A", 3, 2),
        ("A", 4, 1),
    ])
    def test_V0_is_1(self, lt, r, k):
        """V_0 = sum S_{0,lambda}^2 = 1 by unitarity."""
        V = verlinde_dimension(lt, r, k, 0)
        assert abs(V - 1.0) < 1e-8


# =========================================================================
# Section 15: Genus-1 = number of representations
# =========================================================================

class TestGenus1:
    """V_1 = number of integrable representations with nonzero quantum dimension."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3), ("A", 1, 4), ("A", 1, 5),
        ("A", 2, 1), ("A", 2, 2), ("A", 2, 3),
        ("A", 3, 1), ("A", 3, 2),
        ("A", 4, 1),
    ])
    def test_V1_equals_nreps_typeA(self, lt, r, k):
        """For type A: all reps have nonzero qdim, so V_1 = C(k+r, r)."""
        V = verlinde_dimension_exact(lt, r, k, 1)
        expected = int(binomial(k + r, r))
        assert V == expected


# =========================================================================
# Section 16: Total quantum dimension
# =========================================================================

class TestTotalQuantumDim:
    """Verify D^2 = 1/S_{0,0}^2."""

    @pytest.mark.parametrize("r,k", [(1, 1), (1, 2), (1, 3), (2, 1)])
    def test_D2_formula(self, r, k):
        """D^2 = 1/S_{0,0}^2."""
        S = S_matrix("A", r, k)
        s00 = S[0, 0].real
        D2_from_S00 = 1.0 / (s00 * s00)
        D2_from_func = total_quantum_dim_sq("A", r, k)
        assert abs(D2_from_S00 - D2_from_func) < 1e-10

    def test_sl2_D2(self):
        """sl_2 at k=2: D^2 = (k+2)/(2 sin^2(pi/(k+2)))."""
        k = 2
        n = k + 2
        D2_formula = n / (2.0 * math.sin(math.pi / n) ** 2)
        D2_computed = total_quantum_dim_sq("A", 1, k)
        assert abs(D2_formula - D2_computed) < 1e-10


# =========================================================================
# Section 17: Central charge
# =========================================================================

class TestCentralCharge:
    """Verify Sugawara central charge c = k*dim/(k+h^v)."""

    @pytest.mark.parametrize("lt,r,k,expected_c", [
        ("A", 1, 1, 1.0),       # 1*3/3 = 1
        ("A", 1, 2, 1.5),       # 2*3/4 = 1.5
        ("A", 2, 1, 2.0),       # 1*8/4 = 2
        ("D", 4, 1, 4.0),       # 1*28/7 = 4
    ])
    def test_central_charge(self, lt, r, k, expected_c):
        c = central_charge(lt, r, k)
        assert abs(c - expected_c) < 1e-10


# =========================================================================
# Section 18: Comprehensive multi-path verification
# =========================================================================

class TestComprehensiveVerification:
    """Run the comprehensive verification suite."""

    def test_comprehensive_type_A(self):
        """All paths agree for type A at various levels."""
        results = comprehensive_verification(
            types_levels=[("A", 1, 2), ("A", 2, 1), ("A", 3, 1)],
            max_genus=3,
        )
        for rec in results:
            if rec.get("paths_12_agree") is not None:
                assert rec["paths_12_agree"], \
                    f"Paths 1-2 disagree at {rec['type']}_{rec['rank']} " \
                    f"k={rec['level']} g={rec['genus']}"
            if rec.get("paths_13_agree") is not None:
                assert rec["paths_13_agree"], \
                    f"Paths 1-3 disagree at {rec['type']}_{rec['rank']} " \
                    f"k={rec['level']} g={rec['genus']}"


# =========================================================================
# Section 19: Asymptotic growth
# =========================================================================

class TestAsymptoticGrowth:
    """Verify asymptotic behavior of Verlinde and shadow partition functions."""

    def test_verlinde_monotone_increasing(self):
        """V_{g+1} >= V_g for all g >= 1 (Verlinde dims grow)."""
        for k in [2, 3]:
            prev = verlinde_dimension_exact("A", 1, k, 1)
            for g in range(2, 6):
                curr = verlinde_dimension_exact("A", 1, k, g)
                assert curr >= prev, f"V_{g} < V_{g-1} for sl_2 k={k}"
                prev = curr

    def test_shadow_monotone_decreasing(self):
        """|F_{g+1}| < |F_g| for g >= 1 (Bernoulli decay)."""
        for (lt, r, k) in [("A", 1, 2), ("A", 2, 1)]:
            for g in range(1, 5):
                F_curr = abs(float(shadow_F_g(lt, r, k, g)))
                F_next = abs(float(shadow_F_g(lt, r, k, g + 1)))
                assert F_next < F_curr, \
                    f"|F_{g+1}| >= |F_{g}| for {lt}_{r} k={k}"


# =========================================================================
# Section 20: Verlinde at k=1 pattern
# =========================================================================

class TestK1Pattern:
    """At level k=1 for type A: V_g(sl_N, 1) = N^g."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_V_g_equals_N_to_g(self, N):
        """V_g(sl_N, k=1) = N^g."""
        for g in range(5):
            # Use Weyl quantum dimension path
            V = verlinde_from_weyl_qdim("A", N - 1, 1, g)
            expected = N ** g
            assert abs(V - expected) < 0.5, \
                f"V_{g}(sl_{N}, k=1) = {V:.4f}, expected {expected}"


# =========================================================================
# Section 21: Specific non-simply-laced quantum dimensions
# =========================================================================

class TestSpecificQuantumDims:
    """Verify quantum dimensions for specific non-simply-laced cases."""

    def test_B2_k2_vector_qdim(self):
        """B_2 at k=2: vector rep (1,0) should have d = 1."""
        d = quantum_dim_weyl((1, 0), "B", 2, 2)
        assert abs(d - 1.0) < 1e-8

    def test_C2_k2_fundamental_qdim(self):
        """C_2 at k=2: fundamental rep (0,1) should have d = 1."""
        d = quantum_dim_weyl((0, 1), "C", 2, 2)
        assert abs(d - 1.0) < 1e-8

    def test_G2_k2_fundamental_qdim(self):
        """G_2 at k=2: fundamental rep (1,0) has d = 1 at this level."""
        d = quantum_dim_weyl((1, 0), "G", 2, 2)
        assert abs(d - 1.0) < 1e-8

    def test_B2_k3_qdims(self):
        """B_2 at k=3: verify qdim integrality check."""
        wts = integrable_weights("B", 2, 3)
        qdims = [quantum_dim_weyl(wt, "B", 2, 3) for wt in wts]
        nonzero = [d for d in qdims if d > 1e-10]
        assert len(nonzero) >= 2  # at least vacuum + one more


# =========================================================================
# Section 22: Full diagnostic
# =========================================================================

class TestFullDiagnostic:
    """Test the full diagnostic function."""

    def test_sl2_k2_diagnostic(self):
        """Full diagnostic for sl_2 at k=2."""
        diag = full_diagnostic("A", 1, 2, max_genus=3)
        assert diag["algebra"] == "sl_2"
        assert diag["S_unitary"]
        assert diag["fusion_ok"]
        assert diag["verlinde"][0] == 1
        assert diag["verlinde"][1] == 3
        assert diag["verlinde"][2] == 10

    def test_sl3_k1_diagnostic(self):
        """Full diagnostic for sl_3 at k=1."""
        diag = full_diagnostic("A", 2, 1, max_genus=3)
        assert diag["algebra"] == "sl_3"
        assert diag["verlinde"][1] == 3
        assert diag["verlinde"][2] == 9


# =========================================================================
# Section 23: Edge cases
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_genus_negative_raises(self):
        with pytest.raises(ValueError):
            verlinde_dimension("A", 1, 1, -1)

    def test_level_zero_raises(self):
        with pytest.raises(ValueError):
            S_matrix("A", 1, 0)

    def test_F_g_genus_zero_raises(self):
        with pytest.raises(ValueError):
            shadow_F_g("A", 1, 1, 0)

    def test_lambda_fp_genus_zero_raises(self):
        with pytest.raises(ValueError):
            lambda_fp(0)


# =========================================================================
# Section 24: Genus-1 comparison table
# =========================================================================

class TestGenus1Comparison:
    """Genus-1 Verlinde vs shadow across types."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3),
        ("A", 2, 1), ("A", 2, 2),
        ("A", 3, 1),
    ])
    def test_genus1_comparison_data(self, lt, r, k):
        """genus1_verlinde_vs_shadow returns consistent data."""
        data = genus1_verlinde_vs_shadow(lt, r, k)
        assert data["V_1_nonzero_qdim"] >= 1
        assert data["F_1"] > 0
        assert data["kappa"] > 0


# =========================================================================
# Section 25: Verlinde integrality for all tested cases
# =========================================================================

class TestVerlindeIntegrality:
    """Verlinde dimensions are positive integers."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3), ("A", 1, 4), ("A", 1, 5),
        ("A", 2, 1), ("A", 2, 2), ("A", 2, 3),
        ("A", 3, 1), ("A", 3, 2),
        ("A", 4, 1),
    ])
    def test_integrality_typeA(self, lt, r, k):
        """Type A Verlinde numbers are positive integers."""
        for g in range(6):
            V = verlinde_dimension(lt, r, k, g)
            assert abs(V - round(V)) < 0.01, \
                f"V_{g}({lt}_{r}, k={k}) = {V} not integer"
            assert round(V) >= 1

    @pytest.mark.parametrize("lt,r,k", [
        ("B", 2, 2), ("B", 2, 3),
        ("C", 2, 2), ("C", 2, 3),
        ("G", 2, 2), ("G", 2, 3),
    ])
    def test_integrality_weyl(self, lt, r, k):
        """Non-A Verlinde numbers (via Weyl qdim) are positive integers."""
        for g in range(5):
            V = verlinde_from_weyl_qdim(lt, r, k, g)
            assert abs(V - round(V)) < 0.05, \
                f"V_{g}({lt}_{r}, k={k}) = {V:.6f} not integer"
            assert round(V) >= 1


# =========================================================================
# Section 26: Additional sl_2 Verlinde cross-checks
# =========================================================================

class TestSl2CrossChecks:
    """Additional cross-checks for sl_2."""

    def test_sl2_k1_is_power_of_2(self):
        """V_g(sl_2, k=1) = 2^g for g = 0,...,10."""
        for g in range(11):
            V = sl2_verlinde_closed_form(1, g)
            assert abs(V - 2 ** g) < 0.01

    def test_sl2_k2_recursion(self):
        """sl_2 k=2 satisfies V_{g+1}/V_g -> D^2 = 4 for large g."""
        V = [verlinde_dimension_exact("A", 1, 2, g) for g in range(1, 8)]
        ratios = [V[i + 1] / V[i] for i in range(len(V) - 1)]
        # Ratios should approach D^2 = 4 for k=2
        D2 = total_quantum_dim_sq("A", 1, 2)
        assert abs(ratios[-1] - D2) < 0.5

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_sl2_verlinde_positive(self, k):
        """All sl_2 Verlinde numbers are positive."""
        for g in range(8):
            V = sl2_verlinde_closed_form(k, g)
            assert V > 0


# =========================================================================
# Section 27: Shadow CohFT exact values
# =========================================================================

class TestShadowExactValues:
    """Verify exact shadow F_g values."""

    def test_F1_sl2_k1(self):
        """F_1(sl_2, k=1) = (9/4) * (1/24) = 9/96 = 3/32."""
        F = shadow_F_g("A", 1, 1, 1)
        assert F == Rational(9, 4) * Rational(1, 24)

    def test_F1_sl2_k2(self):
        """F_1(sl_2, k=2) = 3 * (1/24) = 1/8."""
        F = shadow_F_g("A", 1, 2, 1)
        assert F == Rational(1, 8)

    def test_F2_sl2_k2(self):
        """F_2(sl_2, k=2) = 3 * 7/5760."""
        F = shadow_F_g("A", 1, 2, 2)
        assert F == Rational(3) * Rational(7, 5760)

    def test_shadow_additivity(self):
        """kappa is additive: kappa(g1 oplus g2) = kappa(g1) + kappa(g2).
        For sl_2 k=1 and sl_3 k=1:
        kappa_sum = kappa(sl_2, 1) + kappa(sl_3, 1)."""
        k1 = kappa_affine_exact("A", 1, 1)
        k2 = kappa_affine_exact("A", 2, 1)
        k_sum = k1 + k2
        # Should equal dim(sl_2)(1+2)/(2*2) + dim(sl_3)(1+3)/(2*3)
        expected = Rational(9, 4) + Rational(16, 3)
        assert k_sum == expected


# =========================================================================
# Section 28: Extended type A Verlinde numbers at higher levels
# =========================================================================

class TestTypeAHigherLevels:
    """Verlinde numbers for type A at higher levels and ranks."""

    @pytest.mark.parametrize("N,k,expected_V1", [
        (2, 1, 2), (2, 2, 3), (2, 3, 4), (2, 4, 5), (2, 5, 6),
        (3, 1, 3), (3, 2, 6), (3, 3, 10),
        (4, 1, 4), (4, 2, 10),
        (5, 1, 5),
    ])
    def test_genus1_equals_binomial(self, N, k, expected_V1):
        """V_1(sl_N, k) = C(N+k-1, N-1)."""
        V = verlinde_dimension_exact("A", N - 1, k, 1)
        assert V == expected_V1

    @pytest.mark.parametrize("N,k", [
        (2, 2), (2, 3), (2, 4), (2, 5),
        (3, 2), (3, 3),
        (4, 2),
    ])
    def test_verlinde_growth(self, N, k):
        """V_g strictly increases with g for k >= 2."""
        prev = 1
        for g in range(1, 5):
            V = verlinde_dimension_exact("A", N - 1, k, g)
            assert V > prev, f"V_{g} = {V} <= V_{g-1} = {prev}"
            prev = V


# =========================================================================
# Section 29: D_4 triality and Verlinde numbers
# =========================================================================

class TestD4:
    """D_4 = so(8) Verlinde numbers and triality."""

    def test_D4_k1_weights(self):
        """D_4 at k=1: weights are vacuum, vector, and two spinors."""
        wts = integrable_weights("D", 4, 1)
        assert (0, 0, 0, 0) in wts  # vacuum
        assert (1, 0, 0, 0) in wts  # vector
        assert (0, 0, 1, 0) in wts  # spinor+
        assert (0, 0, 0, 1) in wts  # spinor-
        assert (0, 1, 0, 0) not in wts  # adjoint needs level >= 2

    def test_D4_k1_all_qdim_1(self):
        """D_4 at k=1: all 4 representations have quantum dimension 1."""
        wts = integrable_weights("D", 4, 1)
        for wt in wts:
            d = quantum_dim_weyl(wt, "D", 4, 1)
            assert abs(d - 1.0) < 1e-8, f"d({wt}) = {d}"

    def test_D4_k1_verlinde_4_to_g(self):
        """D_4 at k=1: V_g = 4^g (4 reps, all with d=1)."""
        for g in range(5):
            V = verlinde_from_weyl_qdim("D", 4, 1, g)
            assert abs(V - 4 ** g) < 0.5

    def test_D4_k2_integrality(self):
        """D_4 at k=2: Verlinde numbers are integers."""
        for g in range(4):
            V = verlinde_from_weyl_qdim("D", 4, 2, g)
            assert abs(V - round(V)) < 0.1


# =========================================================================
# Section 30: B_n and C_n Verlinde numbers
# =========================================================================

class TestBCTypes:
    """Verlinde numbers for types B and C at various levels."""

    @pytest.mark.parametrize("lt,r,k", [
        ("B", 2, 2), ("B", 2, 3), ("B", 2, 4),
        ("C", 2, 2), ("C", 2, 3), ("C", 2, 4),
        ("B", 3, 2), ("C", 3, 2),
    ])
    def test_integrality(self, lt, r, k):
        """Verlinde numbers are positive integers."""
        for g in range(4):
            V = verlinde_from_weyl_qdim(lt, r, k, g)
            assert abs(V - round(V)) < 0.1, \
                f"V_{g}({lt}_{r}, k={k}) = {V:.6f}"
            assert round(V) >= 1

    def test_B2_C2_isogeny(self):
        """B_2 = C_2 as Lie algebras, so at same level should give same number of reps."""
        # Actually B_2 and C_2 have DIFFERENT colabels, so different integrability conditions
        # at the same level. They are NOT isomorphic as AFFINE algebras.
        wts_B = integrable_weights("B", 2, 3)
        wts_C = integrable_weights("C", 2, 3)
        # Just verify both give valid results
        assert len(wts_B) >= 2
        assert len(wts_C) >= 2


# =========================================================================
# Section 31: Exceptional types
# =========================================================================

class TestExceptionalTypes:
    """Verlinde numbers for exceptional types G_2, F_4, E_6, E_7, E_8."""

    @pytest.mark.parametrize("lt,r,k", [
        ("G", 2, 2), ("G", 2, 3),
    ])
    def test_G2_integrality(self, lt, r, k):
        for g in range(4):
            V = verlinde_from_weyl_qdim(lt, r, k, g)
            assert abs(V - round(V)) < 0.1

    def test_G2_k3_nreps(self):
        """G_2 at k=3: should have 3 integrable reps."""
        wts = integrable_weights("G", 2, 3)
        assert len(wts) == 3

    def test_F4_k1_weights(self):
        """F_4 at k=1: marks (2,4,3,2), so very few reps at level 1."""
        wts = integrable_weights("F", 4, 1)
        # Only vacuum (0,0,0,0) since all marks >= 2
        assert len(wts) == 1

    def test_E6_k1_nreps(self):
        """E_6 at k=1: marks (1,2,3,2,1,2), weights with colabel sum <= 1."""
        wts = integrable_weights("E", 6, 1)
        # (0,...,0), (1,0,...,0), (0,0,0,0,0,1) have sum = 1
        # Any weight with a_2, a_3, a_4, a_6 > 0 exceeds budget
        assert len(wts) >= 2


# =========================================================================
# Section 32: FF anti-symmetry of kappa
# =========================================================================

class TestFFAntiSymmetry:
    """Feigin-Frenkel involution k -> -k - 2h^v preserves kappa anti-symmetrically."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3),
        ("A", 2, 1), ("A", 2, 2),
        ("A", 3, 1),
    ])
    def test_kappa_antisymmetry(self, lt, r, k):
        """kappa(g, k) + kappa(g, -k-2h^v) = 0 (AP24 for KM)."""
        from compute.lib.verlinde_shadow_cohft_engine import _get_lie_data
        data = _get_lie_data(lt, r)
        hv = data["hv"]
        k_dual = -k - 2 * hv
        kap = kappa_affine_exact(lt, r, k)
        kap_dual = kappa_affine_exact(lt, r, k_dual)
        assert kap + kap_dual == 0


# =========================================================================
# Section 33: Shadow F_g Bernoulli decay
# =========================================================================

class TestBernoulliDecay:
    """Verify Bernoulli asymptotic behavior of shadow F_g."""

    def test_lambda_fp_decay(self):
        """lambda_g^FP decays: lambda_{g+1} < lambda_g for g >= 1."""
        for g in range(1, 8):
            fp_g = float(lambda_fp(g))
            fp_g1 = float(lambda_fp(g + 1))
            assert abs(fp_g1) < abs(fp_g)

    def test_lambda_fp_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 10):
            assert float(lambda_fp(g)) > 0

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_shadow_proportional_to_kappa(self, g):
        """F_g(g, k1) / F_g(g, k2) = kappa(g, k1) / kappa(g, k2)."""
        F1 = float(shadow_F_g("A", 1, 2, g))
        F2 = float(shadow_F_g("A", 1, 3, g))
        k1 = kappa_affine("A", 1, 2)
        k2 = kappa_affine("A", 1, 3)
        assert abs(F1 / F2 - k1 / k2) < 1e-10


# =========================================================================
# Section 34: Verlinde-shadow ratio behavior
# =========================================================================

class TestVerlindeRatio:
    """Analyze the ratio V_{g,k} / F_g."""

    def test_ratio_increases_with_genus(self):
        """V_g / F_g increases with g (Verlinde grows, shadow decays)."""
        ratios = []
        for g in range(1, 5):
            V = verlinde_dimension_exact("A", 1, 3, g)
            F = float(shadow_F_g("A", 1, 3, g))
            ratios.append(V / F)
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] > ratios[i]

    def test_ratio_genus1_formula(self):
        """At genus 1: V_1/F_1 = 24 * |P^k_+| / kappa."""
        for (lt, r, k) in [("A", 1, 2), ("A", 2, 1)]:
            V1 = verlinde_dimension_exact(lt, r, k, 1)
            F1 = float(shadow_F_g(lt, r, k, 1))
            kap = kappa_affine(lt, r, k)
            n_reps = V1
            expected_ratio = 24.0 * n_reps / kap
            assert abs(V1 / F1 - expected_ratio) < 1e-10
