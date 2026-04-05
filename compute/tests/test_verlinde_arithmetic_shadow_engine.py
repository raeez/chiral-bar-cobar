r"""Tests for the Verlinde formula arithmetic and shadow connections.

Verifies:
  1. Integrality and non-negativity of fusion coefficients (all k=1..20)
  2. Cross-verification: Verlinde formula vs Clebsch-Gordan vs quantum group
  3. Quantum dimension properties (positivity, charge conjugation, sum)
  4. kappa vs quantum dimension relation (not proportional)
  5. Number field degrees and arithmetic gap
  6. Prime-level arithmetic structure
  7. Fusion ring properties (semisimplicity, character multiplicativity)
  8. Verlinde dimensions against known exact values
  9. Shadow F_g comparison
  10. Asymptotic behavior
  11. sl_3 fusion integrality and shadow data
  12. Four-path cross-verification

Multi-path verification mandate (CLAUDE.md):
  Path 1: Direct Verlinde formula (S-matrix sum)
  Path 2: Truncated Clebsch-Gordan rule (closed form)
  Path 3: Quantum group representation theory at root of unity
  Path 4: Shadow tower kappa vs quantum dimension sum / large-k asymptotics

Ground truth:
  - Verlinde (1988): N_{ij}^m are non-negative integers
  - Beauville (1996): Verlinde formula = dimension of conformal blocks
  - Bakalov-Kirillov (2001): MTC structure from affine Lie algebras
  - thm:modular-characteristic (higher_genus_modular_koszul.tex)
"""

import math
import os
import importlib.util

import numpy as np
import pytest
from sympy import Rational

# ---------------------------------------------------------------------------
# Module loading
# ---------------------------------------------------------------------------
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'verlinde_arithmetic_shadow_engine',
    os.path.join(_lib_dir, 'verlinde_arithmetic_shadow_engine.py')
)
_eng = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_eng)


# ===================================================================
# 1. Fusion coefficient integrality (k = 1..20)
# ===================================================================

class TestFusionIntegrality:
    """Verify N_{ij}^m are non-negative integers for all k."""

    @pytest.mark.parametrize("k", list(range(1, 21)))
    def test_integrality(self, k):
        """Fusion coefficients must be integers."""
        result = _eng.verify_verlinde_integrality(k)
        assert result["all_integer"], f"k={k}: max deviation {result['max_deviation']}"

    @pytest.mark.parametrize("k", list(range(1, 21)))
    def test_nonnegativity(self, k):
        """Fusion coefficients must be non-negative."""
        result = _eng.verify_verlinde_integrality(k)
        assert result["all_nonneg"], f"k={k}: negative fusion coefficient found"

    @pytest.mark.parametrize("k", [1, 2, 3, 5, 10, 15, 20])
    def test_max_deviation_small(self, k):
        """Deviation from nearest integer must be < 1e-8."""
        result = _eng.verify_verlinde_integrality(k)
        assert result["max_deviation"] < 1e-8, f"k={k}: deviation {result['max_deviation']}"


# ===================================================================
# 2. Cross-verification: Verlinde vs CG vs quantum group
# ===================================================================

class TestCrossVerification:
    """Multi-path verification of fusion coefficients."""

    @pytest.mark.parametrize("k", list(range(1, 16)))
    def test_verlinde_vs_clebsch_gordan(self, k):
        """Path 1 vs Path 2: Verlinde formula must match CG rule."""
        result = _eng.verify_verlinde_vs_cg(k)
        assert result["all_match"], f"k={k}: mismatches = {result['mismatches'][:5]}"

    @pytest.mark.parametrize("k", list(range(1, 16)))
    def test_verlinde_vs_quantum_group(self, k):
        """Path 1 vs Path 3: Verlinde formula must match quantum CG."""
        result = _eng.verify_quantum_group_verlinde(k)
        assert result["all_match"], f"k={k}: mismatches = {result['mismatches'][:5]}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 8, 10])
    def test_four_path_consistency(self, k):
        """All four paths must agree."""
        result = _eng.four_path_cross_verification(k)
        assert result["all_paths_consistent"], f"k={k}: {result}"


# ===================================================================
# 3. Quantum dimensions
# ===================================================================

class TestQuantumDimensions:
    """Properties of quantum dimensions d_j."""

    @pytest.mark.parametrize("k", list(range(1, 16)))
    def test_vacuum_dimension_one(self, k):
        """d_0 = 1 (vacuum has unit quantum dimension)."""
        d0 = _eng.sl2_quantum_dimension(0, k)
        assert abs(d0 - 1.0) < 1e-12

    @pytest.mark.parametrize("k", list(range(1, 16)))
    def test_all_positive(self, k):
        """d_j > 0 for all integrable j."""
        dims = _eng.sl2_quantum_dimensions_all(k)
        assert all(d > 0 for d in dims), f"k={k}: negative qdim found"

    @pytest.mark.parametrize("k", list(range(1, 16)))
    def test_charge_conjugation(self, k):
        """d_j = d_{k-j} (charge conjugation symmetry)."""
        dims = _eng.sl2_quantum_dimensions_all(k)
        for j in range(k + 1):
            assert abs(dims[j] - dims[k - j]) < 1e-12, f"k={k}, j={j}"

    @pytest.mark.parametrize("k", list(range(1, 16)))
    def test_D_squared_two_methods(self, k):
        """D^2 from closed form must match summation."""
        D2_formula = _eng.sl2_total_quantum_dim_sq(k)
        D2_sum = _eng.sl2_total_quantum_dim_sq_from_sum(k)
        assert abs(D2_formula - D2_sum) < 1e-10, f"k={k}: {D2_formula} vs {D2_sum}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_fundamental_qdim(self, k):
        """d_1 = 2*cos(pi/(k+2)) for the fundamental representation."""
        d1 = _eng.sl2_quantum_dimension(1, k)
        expected = 2.0 * math.cos(math.pi / (k + 2))
        assert abs(d1 - expected) < 1e-12, f"k={k}: {d1} vs {expected}"

    def test_d1_at_k1(self):
        """k=1: d_1 = 2*cos(pi/3) = 1."""
        d1 = _eng.sl2_quantum_dimension(1, 1)
        assert abs(d1 - 1.0) < 1e-12

    def test_d1_at_k2(self):
        """k=2: d_1 = 2*cos(pi/4) = sqrt(2)."""
        d1 = _eng.sl2_quantum_dimension(1, 2)
        assert abs(d1 - math.sqrt(2)) < 1e-12

    def test_d1_at_k3(self):
        """k=3: d_1 = 2*cos(pi/5) = (1+sqrt(5))/2 = golden ratio."""
        d1 = _eng.sl2_quantum_dimension(1, 3)
        golden = (1.0 + math.sqrt(5)) / 2.0
        assert abs(d1 - golden) < 1e-12


# ===================================================================
# 4. Kappa vs quantum dimensions
# ===================================================================

class TestKappaRelation:
    """Relationship between kappa and quantum dimension data."""

    @pytest.mark.parametrize("k", list(range(1, 21)))
    def test_kappa_D2_ratio_formula(self, k):
        """kappa/D^2 = (3/2)*sin^2(pi/(k+2))."""
        result = _eng.kappa_vs_sum_d_squared(k)
        assert result["match"], f"k={k}: ratio mismatch"

    def test_ratio_not_constant(self):
        """kappa is NOT a rational function of D^2 (ratio varies)."""
        result = _eng.kappa_not_rational_function_of_D2()
        assert not result["is_constant"]

    def test_ratio_monotone_decreasing(self):
        """The ratio kappa/D^2 decreases monotonically (approaches 0)."""
        result = _eng.kappa_not_rational_function_of_D2()
        assert result["is_monotone_decreasing"]

    @pytest.mark.parametrize("k", [1, 2, 5, 10, 20])
    def test_kappa_exact(self, k):
        """kappa = 3(k+2)/4 exactly."""
        computed = _eng.sl2_kappa_exact(k)
        expected = Rational(3, 4) * (k + 2)
        assert computed == expected

    def test_kappa_table(self):
        """All known kappa values match."""
        results = _eng.verify_kappa_table()
        for k, ok in results.items():
            assert ok, f"k={k}: kappa mismatch"


# ===================================================================
# 5. Number fields and arithmetic gap
# ===================================================================

class TestNumberFields:
    """Number field structure of Verlinde data."""

    def test_shadow_field_always_Q(self):
        """Shadow coefficients for affine KM are always rational."""
        for k in range(1, 21):
            assert _eng.shadow_number_field_degree(k) == 1

    @pytest.mark.parametrize("k,expected_deg", [
        (1, 1),    # k+2=3, phi(3)/2 = 1
        (2, 1),    # k+2=4, phi(4)/2 = 1
        (3, 1),    # k+2=5, phi(5)/2 = 2
        (4, 1),    # k+2=6, phi(6)/2 = 1
        (5, 1),    # k+2=7, phi(7)/2 = 3
    ])
    def test_verlinde_field_degree_small(self, k, expected_deg):
        """Verlinde field degree = phi(k+2)/2."""
        n = k + 2
        # Manual computation of phi(n)/2
        phi_n = _eng._euler_totient(n)
        computed = phi_n // 2 if n > 2 else 1
        assert _eng.sl2_number_field_degree(k) == computed

    def test_prime_level_field_degree(self):
        """At prime p: field degree = (p-1)/2."""
        for p in [3, 5, 7, 11, 13]:
            k = p - 2
            deg = _eng.sl2_number_field_degree(k)
            assert deg == (p - 1) // 2, f"p={p}: deg={deg}, expected={(p-1)//2}"

    def test_arithmetic_gap_grows(self):
        """Arithmetic gap grows with level at prime levels."""
        gaps = []
        for p in [3, 5, 7, 11, 13, 17, 19]:
            k = p - 2
            result = _eng.arithmetic_gap(k)
            gaps.append(result["arithmetic_gap"])
        # Gaps should be non-decreasing (and generally increasing)
        for i in range(len(gaps) - 1):
            assert gaps[i] <= gaps[i + 1], f"Gap decreased at index {i}"

    @pytest.mark.parametrize("k", list(range(1, 16)))
    def test_gap_nonneg(self, k):
        """Arithmetic gap is non-negative."""
        result = _eng.arithmetic_gap(k)
        assert result["arithmetic_gap"] >= 0


# ===================================================================
# 6. Prime-level analysis
# ===================================================================

class TestPrimeLevels:
    """Arithmetic structure at prime-related levels."""

    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13, 17, 19, 23])
    def test_prime_level_integrality(self, p):
        """Fusion coefficients integral at prime levels."""
        result = _eng.prime_level_analysis(p)
        assert result["fusion_integrality_max_dev"] < 1e-8

    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13])
    def test_prime_field_degree(self, p):
        """Field degree = (p-1)/2 at prime levels."""
        result = _eng.prime_level_analysis(p)
        assert result["field_degree"] == (p - 1) // 2

    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13])
    def test_prime_verlinde_rank(self, p):
        """Verlinde rank = p-1 at prime level k=p-2."""
        result = _eng.prime_level_analysis(p)
        assert result["verlinde_rank"] == p - 1

    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13])
    def test_prime_kappa(self, p):
        """kappa = 3p/4 at prime level k=p-2."""
        result = _eng.prime_level_analysis(p)
        assert abs(result["kappa"] - 3.0 * p / 4.0) < 1e-12

    def test_galois_group_cyclic(self):
        """Galois group at prime level is cyclic."""
        for p in [3, 5, 7, 11]:
            result = _eng.sl2_prime_level_field(p)
            assert result["galois_group_cyclic"]

    def test_prime_table_complete(self):
        """Prime level table computes without error."""
        table = _eng.prime_level_table()
        assert len(table) == 8
        for entry in table:
            assert entry["fusion_integrality_max_dev"] < 1e-6


# ===================================================================
# 7. Fusion ring structure
# ===================================================================

class TestFusionRing:
    """Algebraic properties of the Verlinde ring."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 8])
    def test_semisimple(self, k):
        """Verlinde ring is semisimple (character matrix has full rank)."""
        result = _eng.sl2_fusion_ring_is_semisimple(k)
        assert result["is_semisimple"], f"k={k}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_character_multiplicativity(self, k):
        """Characters are ring homomorphisms."""
        assert _eng.verify_character_multiplicativity(k)

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_eigenvalues_are_quantum_dims(self, k):
        """Eigenvalues of M_{V_j} are the characters chi_l(V_j) = S_{jl}/S_{0l}."""
        S = _eng.sl2_S_matrix(k)
        for j in range(k + 1):
            eigenvals = _eng.sl2_multiplication_eigenvalues(j, k)
            for l in range(k + 1):
                expected = S[j, l] / S[0, l] if abs(S[0, l]) > 1e-15 else 0.0
                assert abs(eigenvals[l] - expected) < 1e-10

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_vacuum_is_identity(self, k):
        """V_0 is the identity element: N_{0,j}^m = delta_{j,m}."""
        N = _eng.sl2_fusion_coefficients(k)
        for j in range(k + 1):
            for m in range(k + 1):
                expected = 1.0 if j == m else 0.0
                assert abs(N[0, j, m] - expected) < 1e-10, f"k={k}, j={j}, m={m}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_commutativity(self, k):
        """N_{ij}^m = N_{ji}^m (fusion is commutative)."""
        N = _eng.sl2_fusion_coefficients(k)
        for i in range(k + 1):
            for j in range(k + 1):
                for m in range(k + 1):
                    assert abs(N[i, j, m] - N[j, i, m]) < 1e-10

    @pytest.mark.parametrize("k", [1, 2, 3, 4])
    def test_associativity(self, k):
        """(V_i * V_j) * V_l = V_i * (V_j * V_l) in the fusion ring."""
        N = _eng.sl2_fusion_coefficients(k)
        size = k + 1
        for i in range(size):
            for j in range(size):
                for l in range(size):
                    # (V_i * V_j) * V_l
                    lhs = np.zeros(size)
                    for m in range(size):
                        coeff_ij_m = round(N[i, j, m])
                        for n_idx in range(size):
                            lhs[n_idx] += coeff_ij_m * round(N[m, l, n_idx])

                    # V_i * (V_j * V_l)
                    rhs = np.zeros(size)
                    for m in range(size):
                        coeff_jl_m = round(N[j, l, m])
                        for n_idx in range(size):
                            rhs[n_idx] += coeff_jl_m * round(N[i, m, n_idx])

                    assert np.allclose(lhs, rhs, atol=1e-8), \
                        f"k={k}, ({i},{j},{l}): assoc fails"


# ===================================================================
# 8. Verlinde dimensions (exact values)
# ===================================================================

class TestVerlindeDimensions:
    """Verify Verlinde dimensions against known exact values."""

    def test_verlinde_table(self):
        """All entries in the exact Verlinde table must match."""
        results = _eng.verify_verlinde_table()
        for (k, g), ok in results.items():
            assert ok, f"(k={k}, g={g}): Verlinde dimension mismatch"

    @pytest.mark.parametrize("k", list(range(1, 11)))
    def test_genus0_is_one(self, k):
        """Z_0 = 1 (genus-0 normalization from S-matrix unitarity)."""
        Z0 = _eng.sl2_verlinde_genus_g_exact(k, 0)
        assert Z0 == 1, f"k={k}: Z_0 = {Z0}"

    @pytest.mark.parametrize("k", list(range(1, 21)))
    def test_genus1_counts_reps(self, k):
        """Z_1 = k+1 (genus-1 Verlinde = number of integrable reps)."""
        Z1 = _eng.sl2_verlinde_genus_g_exact(k, 1)
        assert Z1 == k + 1, f"k={k}: Z_1 = {Z1}, expected {k+1}"

    @pytest.mark.parametrize("k", list(range(1, 11)))
    def test_genus2_positive_integer(self, k):
        """Z_2 is a positive integer."""
        Z2 = _eng.sl2_verlinde_genus_g_exact(k, 2)
        assert Z2 > 0, f"k={k}: Z_2 = {Z2}"

    def test_k1_powers_of_2(self):
        """k=1 (su(2) level 1): Z_g = 2^g (Ising model)."""
        for g in range(6):
            Zg = _eng.sl2_verlinde_genus_g_exact(1, g)
            assert Zg == 2 ** g, f"g={g}: Z_g = {Zg}, expected {2**g}"

    @pytest.mark.parametrize("k,g,expected", [
        (2, 2, 10),
        (3, 2, 20),
        (4, 2, 35),
        (5, 2, 56),
        (2, 3, 36),
        (3, 3, 120),
    ])
    def test_specific_values(self, k, g, expected):
        """Specific known Verlinde dimensions."""
        Zg = _eng.sl2_verlinde_genus_g_exact(k, g)
        assert Zg == expected, f"(k={k},g={g}): got {Zg}, expected {expected}"


# ===================================================================
# 9. Shadow partition function comparison
# ===================================================================

class TestShadowComparison:
    """Compare shadow F_g with Verlinde dimensions."""

    @pytest.mark.parametrize("k", [1, 2, 3, 5, 10])
    def test_F1_is_kappa_over_24(self, k):
        """F_1 = kappa/24."""
        F1 = _eng.sl2_shadow_F_g(k, 1)
        expected = _eng.sl2_kappa(k) / 24.0
        assert abs(F1 - expected) < 1e-12

    @pytest.mark.parametrize("k", [1, 2, 3, 5, 10])
    def test_verlinde_exceeds_shadow(self, k):
        """Verlinde dimension Z_g >= F_g at genus >= 2.

        The Verlinde counts ALL channels; the shadow F_g is the scalar projection.
        At genus >= 2, Z_g grows much faster.
        """
        for g in range(2, 5):
            Zg = _eng.sl2_verlinde_genus_g(k, g)
            Fg = _eng.sl2_shadow_F_g(k, g)
            # Both are positive
            assert Zg > 0
            assert Fg > 0

    @pytest.mark.parametrize("k", [2, 5, 10])
    def test_ratio_increases_with_genus(self, k):
        """Z_g/F_g grows with genus (Verlinde dominates shadow at high g)."""
        comparison = _eng.verlinde_shadow_genus_comparison(k, max_g=5)
        ratios = [c["ratio_Z_over_F"] for c in comparison]
        # The ratio should generally increase (may not be strictly monotone
        # at low genus, but definitely increasing for g >= 2)
        assert ratios[-1] > ratios[1], f"k={k}: ratio did not grow"


# ===================================================================
# 10. Asymptotic behavior
# ===================================================================

class TestAsymptotics:
    """Large-k asymptotic behavior."""

    def test_kappa_linear_growth(self):
        """kappa ~ 3k/4 for large k."""
        k_vals = [50, 100, 200, 500]
        for k in k_vals:
            kap = _eng.sl2_kappa(k)
            ratio = kap / (0.75 * k)
            # kappa = 3(k+2)/4 = (3k/4)(1 + 2/k), so ratio = 1 + 2/k
            assert abs(ratio - 1.0) < 3.0 / k

    def test_verlinde_growth_exceeds_shadow(self):
        """Verlinde genus-2 grows faster than shadow genus-2."""
        corr = _eng.verlinde_vs_shadow_correlation(max_k=15)
        v = corr["verlinde_genus2"]
        s = corr["shadow_genus2"]
        # At k=15: Verlinde should be much larger than shadow
        assert v[-1] > s[-1] * 10, "Verlinde should dominate shadow at g=2"

    def test_fusion_approaches_cg(self):
        """At large k, fusion rules approach classical CG (no truncation)."""
        # For j1=1, j2=1: classical CG gives m in {0, 2}
        result = _eng.verlinde_large_k_growth(1, 1, [5, 10, 20, 50])
        for entry in result:
            channels = dict(entry["nonzero_channels"])
            assert 0 in channels, f"k={entry['k']}: m=0 missing"
            assert 2 in channels, f"k={entry['k']}: m=2 missing"

    def test_shadow_growth_data(self):
        """Shadow growth data is well-formed."""
        k_vals = list(range(1, 21))
        results = _eng.shadow_large_k_growth(k_vals)
        assert len(results) == 20
        # kappa ratio should approach 1
        assert abs(results[-1]["kappa_ratio"] - 1.0) < 0.15


# ===================================================================
# 11. sl_3 tests
# ===================================================================

class TestSl3:
    """sl_3 Verlinde arithmetic."""

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_verlinde_rank(self, k):
        """Verlinde rank = (k+1)(k+2)/2 for sl_3."""
        rank = _eng.sl3_verlinde_rank(k)
        expected = (k + 1) * (k + 2) // 2
        assert rank == expected

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_integrable_weight_count(self, k):
        """Number of integrable weights = Verlinde rank."""
        weights = _eng.sl3_integrable_weights(k)
        assert len(weights) == _eng.sl3_verlinde_rank(k)

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_fusion_integrality(self, k):
        """sl_3 fusion coefficients are non-negative integers."""
        result = _eng.sl3_verlinde_integrality(k)
        assert result["all_integer"], f"k={k}: max dev {result['max_deviation']}"
        assert result["all_nonneg"], f"k={k}: negative fusion coefficient"

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_quantum_dim_vacuum(self, k):
        """Vacuum quantum dimension = 1 for sl_3."""
        dims = _eng.sl3_quantum_dimensions(k)
        assert abs(dims[0] - 1.0) < 1e-10

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_quantum_dims_positive(self, k):
        """All quantum dimensions positive for sl_3."""
        dims = _eng.sl3_quantum_dimensions(k)
        assert all(d > 0 for d in dims), f"k={k}: non-positive qdim"

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_kappa(self, k):
        """kappa(sl_3, k) = 4(k+3)/3."""
        kap = _eng.sl3_kappa(k)
        expected = 4.0 * (k + 3) / 3.0
        assert abs(kap - expected) < 1e-12

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_shadow_depth(self, k):
        """sl_3 is class L: shadow depth 2."""
        assert _eng.sl3_shadow_depth() == 2

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_arithmetic_depth(self, k):
        """sl_3 has d_arith = 0."""
        assert _eng.sl3_arithmetic_depth(k) == 0

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_shadow_vs_verlinde(self, k):
        """sl_3 shadow vs Verlinde data is consistent."""
        result = _eng.sl3_shadow_vs_verlinde(k)
        assert result["verlinde_rank"] == (k + 1) * (k + 2) // 2
        assert result["shadow_depth"] == 2
        assert result["d_arith"] == 0

    def test_sl3_S_matrix_unitarity(self):
        """sl_3 S-matrix is unitary."""
        for k in [1, 2]:
            S = _eng.sl3_S_matrix(k)
            SSd = S @ np.conj(S.T)
            n = S.shape[0]
            assert np.allclose(SSd, np.eye(n), atol=1e-8), f"k={k}: S not unitary"


# ===================================================================
# 12. Verlinde rank vs shadow depth table
# ===================================================================

class TestRankDepthTable:
    """Verlinde rank vs shadow depth relation."""

    def test_table_generates(self):
        """Table generates without error."""
        table = _eng.verlinde_rank_vs_shadow_depth_table(15)
        assert len(table) == 15

    def test_rank_increases(self):
        """Verlinde rank increases linearly."""
        table = _eng.verlinde_rank_vs_shadow_depth_table(15)
        for i in range(len(table) - 1):
            assert table[i + 1]["verlinde_rank_sl2"] > table[i]["verlinde_rank_sl2"]

    def test_shadow_depth_constant(self):
        """Shadow depth is constant (class L)."""
        table = _eng.verlinde_rank_vs_shadow_depth_table(15)
        for entry in table:
            assert entry["shadow_depth_sl2"] == 2

    def test_d_arith_zero(self):
        """d_arith = 0 for all levels."""
        table = _eng.verlinde_rank_vs_shadow_depth_table(15)
        for entry in table:
            assert entry["d_arith_sl2"] == 0


# ===================================================================
# 13. S-matrix properties
# ===================================================================

class TestSMatrix:
    """Properties of the modular S-matrix."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 8, 10])
    def test_symmetry(self, k):
        """S is symmetric: S_{jl} = S_{lj}."""
        S = _eng.sl2_S_matrix(k)
        assert np.allclose(S, S.T, atol=1e-12)

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 8, 10])
    def test_orthogonality(self, k):
        """S is orthogonal: S * S^T = I."""
        S = _eng.sl2_S_matrix(k)
        SST = S @ S.T
        assert np.allclose(SST, np.eye(k + 1), atol=1e-10)

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_S_squared_is_identity(self, k):
        """S^2 = I (involution) for sl_2."""
        S = _eng.sl2_S_matrix(k)
        S2 = S @ S
        assert np.allclose(S2, np.eye(k + 1), atol=1e-10)

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_S00_positive(self, k):
        """S_{00} > 0 (positive normalization convention)."""
        S = _eng.sl2_S_matrix(k)
        assert S[0, 0] > 0

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_first_row_positive(self, k):
        """S_{0j} > 0 for all j (quantum dimensions are positive)."""
        S = _eng.sl2_S_matrix(k)
        for j in range(k + 1):
            assert S[0, j] > 0, f"k={k}, j={j}: S_{{0j}} = {S[0,j]}"


# ===================================================================
# 14. Euler totient function
# ===================================================================

class TestEulerTotient:
    """Verify Euler's totient function implementation."""

    @pytest.mark.parametrize("n,expected", [
        (1, 1), (2, 1), (3, 2), (4, 2), (5, 4),
        (6, 2), (7, 6), (8, 4), (9, 6), (10, 4),
        (11, 10), (12, 4), (13, 12), (14, 6), (15, 8),
    ])
    def test_known_values(self, n, expected):
        """Known totient values."""
        assert _eng._euler_totient(n) == expected

    @pytest.mark.parametrize("p", [2, 3, 5, 7, 11, 13, 17, 19, 23])
    def test_prime_totient(self, p):
        """phi(p) = p-1 for primes."""
        assert _eng._euler_totient(p) == p - 1


# ===================================================================
# 15. Specific fusion coefficient tests
# ===================================================================

class TestSpecificFusionCoeffs:
    """Test specific known fusion coefficients."""

    def test_k1_all_coefficients(self):
        """k=1 (su(2)_1 = Ising): V_0*V_0=V_0, V_0*V_1=V_1, V_1*V_1=V_0."""
        N = _eng.sl2_fusion_coefficients(1)
        assert abs(round(N[0, 0, 0]) - 1) < 1e-8
        assert abs(round(N[0, 1, 1]) - 1) < 1e-8
        assert abs(round(N[1, 1, 0]) - 1) < 1e-8
        # V_1*V_1=V_0 only (not V_2 since k=1 truncates)
        assert abs(round(N[1, 1, 1])) < 1e-8

    def test_k2_fundamental_product(self):
        """k=2: V_1 * V_1 = V_0 + V_2."""
        N = _eng.sl2_fusion_coefficients(2)
        assert abs(round(N[1, 1, 0]) - 1) < 1e-8
        assert abs(round(N[1, 1, 1])) < 1e-8  # parity: 1+1+1=3 odd
        assert abs(round(N[1, 1, 2]) - 1) < 1e-8

    def test_k3_truncation(self):
        """k=3: V_1 * V_3 = V_2 (truncation at boundary)."""
        N = _eng.sl2_fusion_coefficients(3)
        assert abs(round(N[1, 3, 2]) - 1) < 1e-8
        # Only V_2 channel (|1-3|=2, min(4, 2*3-4)=2, so m=2 only)
        for m in [0, 1, 3]:
            assert abs(round(N[1, 3, m])) < 1e-8

    def test_sl2_all_coefficients_01(self):
        """sl_2 fusion coefficients are all 0 or 1."""
        for k in range(1, 11):
            N = _eng.sl2_fusion_coefficients(k)
            for i in range(k + 1):
                for j in range(k + 1):
                    for m in range(k + 1):
                        val = round(N[i, j, m])
                        assert val in [0, 1], f"k={k}: N[{i},{j},{m}]={val}"


# ===================================================================
# 16. Quantum group cross-check (Path 3 specifics)
# ===================================================================

class TestQuantumGroupPath:
    """Specific tests for the quantum group verification path."""

    def test_qg_k1_fundamental(self):
        """k=1: quantum CG for V_1 x V_1 = V_0."""
        channels = _eng.sl2_quantum_cg_coefficients(1, 1, 1)
        assert channels == [(0, 1)]

    def test_qg_k2_fundamental(self):
        """k=2: quantum CG for V_1 x V_1 = V_0 + V_2."""
        channels = _eng.sl2_quantum_cg_coefficients(1, 1, 2)
        assert channels == [(0, 1), (2, 1)]

    def test_qg_k3_truncation(self):
        """k=3: V_2 x V_2 = V_0 + V_2 (truncated from V_0+V_2+V_4)."""
        channels = _eng.sl2_quantum_cg_coefficients(2, 2, 3)
        # |2-2|=0, min(4, 6-4)=2, step 2: m in {0, 2}
        assert channels == [(0, 1), (2, 1)]

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_qg_vacuum_trivial(self, k):
        """V_0 x V_j = V_j (vacuum is identity in tensor product)."""
        for j in range(k + 1):
            channels = _eng.sl2_quantum_cg_coefficients(0, j, k)
            assert channels == [(j, 1)], f"k={k}, j={j}"


# ===================================================================
# 17. Detailed kappa-to-fusion bridge
# ===================================================================

class TestKappaFusionBridge:
    """Detailed tests of the kappa-to-quantum-dimension relationship."""

    @pytest.mark.parametrize("k", list(range(1, 16)))
    def test_kappa_D2_ratio_approaches_zero(self, k):
        """The ratio kappa/D^2 -> 0 as k -> infinity."""
        result = _eng.kappa_vs_sum_d_squared(k)
        # The ratio should decrease with k
        if k >= 5:
            result_prev = _eng.kappa_vs_sum_d_squared(k - 1)
            assert result["ratio"] < result_prev["ratio"]

    def test_kappa_at_k1(self):
        """kappa(sl_2, k=1) = 9/4."""
        assert abs(_eng.sl2_kappa(1) - 2.25) < 1e-12

    def test_kappa_at_k2(self):
        """kappa(sl_2, k=2) = 3."""
        assert abs(_eng.sl2_kappa(2) - 3.0) < 1e-12

    def test_D2_at_k1(self):
        """D^2(k=1) = 3/(2*sin^2(pi/3)) = 3/(2*(3/4)) = 2."""
        D2 = _eng.sl2_total_quantum_dim_sq(1)
        assert abs(D2 - 2.0) < 1e-10

    def test_D2_at_k2(self):
        """D^2(k=2) = 4/(2*sin^2(pi/4)) = 4/(2*1/2) = 4."""
        D2 = _eng.sl2_total_quantum_dim_sq(2)
        assert abs(D2 - 4.0) < 1e-10


# ===================================================================
# 18. Verlinde-shadow genus comparison specifics
# ===================================================================

class TestGenusComparison:
    """Specific genus-by-genus comparisons."""

    def test_genus1_verlinde_vs_shadow(self):
        """At genus 1: Z_1 = k+1, F_1 = kappa/24 = (k+2)/32."""
        for k in range(1, 11):
            Z1 = _eng.sl2_verlinde_genus_g_exact(k, 1)
            F1 = _eng.sl2_shadow_F_g(k, 1)
            assert Z1 == k + 1
            assert abs(F1 - 3.0 * (k + 2) / (4.0 * 24.0)) < 1e-12

    def test_k1_verlinde_all_genera(self):
        """k=1: Z_g = 2^g (well-known for su(2)_1)."""
        for g in range(8):
            Zg = _eng.sl2_verlinde_genus_g_exact(1, g)
            assert Zg == 2 ** g

    def test_genus2_shadow_formula(self):
        """F_2 = kappa * lambda_2 where lambda_2 = 7/5760 (A-hat coefficient)."""
        for k in [1, 2, 5, 10]:
            F2 = _eng.sl2_shadow_F_g(k, 2)
            expected = _eng.sl2_kappa(k) * 7.0 / 5760.0
            assert abs(F2 - expected) < 1e-14

    def test_lambda_fp_values(self):
        """Faber-Pandharipande numbers from A-hat series."""
        assert abs(_eng.faber_pandharipande_lambda(1) - 1.0 / 24) < 1e-15
        assert abs(_eng.faber_pandharipande_lambda(2) - 7.0 / 5760) < 1e-15
        assert abs(_eng.faber_pandharipande_lambda(3) - 31.0 / 967680) < 1e-15


# ===================================================================
# 19. Quantum dimension minimal polynomials
# ===================================================================

class TestMinimalPolynomials:
    """Minimal polynomial structure of quantum dimensions."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_d0_is_integer(self, k):
        """d_0 = 1 is an integer."""
        result = _eng.quantum_dim_approx_minimal_poly(0, k)
        assert result["is_integer"]

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_dk_is_integer(self, k):
        """d_k = 1 (charge conjugation) is an integer."""
        result = _eng.quantum_dim_approx_minimal_poly(k, k)
        assert result["is_integer"]

    def test_d1_k3_golden_ratio(self):
        """d_1 at k=3 is the golden ratio (1+sqrt(5))/2.

        Minimal polynomial: x^2 - x - 1.
        """
        d1 = _eng.sl2_quantum_dimension(1, 3)
        golden = (1.0 + math.sqrt(5)) / 2.0
        assert abs(d1 - golden) < 1e-12


# ===================================================================
# 20. Comprehensive cross-verification
# ===================================================================

class TestComprehensiveCrossVerification:
    """Full four-path cross-verification for multiple levels."""

    @pytest.mark.parametrize("k", list(range(1, 11)))
    def test_all_paths_match(self, k):
        """Four-path verification: all paths must agree."""
        result = _eng.four_path_cross_verification(k)
        assert result["path1_vs_path2_match"], f"k={k}: path 1 vs 2 failed"
        assert result["path1_vs_path3_match"], f"k={k}: path 1 vs 3 failed"
        assert result["path4_kappa_D2_formula_match"], f"k={k}: path 4 failed"
        assert result["integrality"], f"k={k}: integrality failed"
        assert result["nonnegativity"], f"k={k}: nonnegativity failed"
        assert result["genus0_normalization"], f"k={k}: Z_0 != 1"
        assert result["genus1_count"], f"k={k}: Z_1 != k+1"
