"""Tests for the DS complementarity defect.

Verifies:
1. δ_K = K_N · (H_N - 1) for all N
2. Factorization δ_K = K_N · ρ(sl_N)
3. K(ĝ_k) = 0 for all affine
4. K(Vir_c) = 13 for all c
5. Cubic conductor C + C' = -26 for Virasoro
6. Quartic conductor Q + Q' depends on c (NOT level-independent)
7. Genus-g defect δ_{Q_g} = K · λ_g^FP
8. Large-N asymptotics δ_K ~ (4/3)N³ log N
9. Affine tower vanishes at all arities/genera
10. Hook-type defects for non-principal reductions
"""

from fractions import Fraction
import pytest

from compute.lib.ds_complementarity_defect import (
    DSComplementarityDefect,
    K_affine,
    K_virasoro,
    K_wn,
    asymptotic_ratio,
    complementarity_constant_hook,
    conformal_weights,
    cubic_conductor_virasoro,
    defect_summary_table,
    ds_complementarity_defect,
    ds_defect_hook,
    exponent_sum,
    full_tower,
    genus_g_defect,
    genus_g_defect_affine,
    ghost_constant_hook,
    koszul_conductor,
    lie_exponents,
    quartic_conductor_virasoro,
    quartic_conductor_virasoro_numerator,
    self_dual_central_charge,
    tower_arity2,
    tower_arity3_virasoro,
    verify_factorization,
    verify_genus_defect_vanishes_affine,
    verify_large_N_convergence,
    verify_virasoro_conductors,
    affine_tower_vanishes,
)
from compute.lib.stable_graph_enumeration import _lambda_fp_exact


# ===========================================================================
# Root datum invariants
# ===========================================================================

class TestRootDatum:
    def test_exponent_sum_sl2(self):
        assert exponent_sum(2) == Fraction(1, 2)

    def test_exponent_sum_sl3(self):
        assert exponent_sum(3) == Fraction(5, 6)

    def test_exponent_sum_sl4(self):
        assert exponent_sum(4) == Fraction(13, 12)

    def test_koszul_conductor_sl2(self):
        assert koszul_conductor(2) == Fraction(26)

    def test_koszul_conductor_sl3(self):
        assert koszul_conductor(3) == Fraction(100)

    def test_koszul_conductor_sl4(self):
        assert koszul_conductor(4) == Fraction(246)

    def test_koszul_conductor_sl5(self):
        assert koszul_conductor(5) == Fraction(488)

    def test_koszul_conductor_sl6(self):
        assert koszul_conductor(6) == Fraction(850)

    def test_self_dual_c_sl2(self):
        assert self_dual_central_charge(2) == Fraction(13)

    def test_self_dual_c_sl3(self):
        assert self_dual_central_charge(3) == Fraction(50)

    def test_lie_exponents_sl4(self):
        assert lie_exponents(4) == [1, 2, 3]

    def test_conformal_weights_sl4(self):
        assert conformal_weights(4) == [2, 3, 4]


# ===========================================================================
# Complementarity constants
# ===========================================================================

class TestComplementarityConstants:
    def test_K_affine_is_zero(self):
        for N in range(2, 8):
            for k in [1, 2, 3, 5, 10]:
                assert K_affine(N, Fraction(k)) == 0

    def test_K_virasoro_is_13(self):
        for c in [1, 13, 25, Fraction(1, 2), Fraction(-22, 5) + 1]:
            assert K_virasoro(c) == 13

    def test_K_wn_sl2(self):
        assert K_wn(2) == 26 * Fraction(1, 2)  # = 13

    def test_K_wn_sl3(self):
        assert K_wn(3) == 100 * Fraction(5, 6)  # = 250/3

    def test_K_wn_sl4(self):
        assert K_wn(4) == 246 * Fraction(13, 12)  # = 1599/6 = 266.5

    def test_K_wn_matches_virasoro_at_N2(self):
        """W_2 = Virasoro. K(W_2) = K(Vir) = 13."""
        assert K_wn(2) == Fraction(13)


# ===========================================================================
# DS complementarity defect
# ===========================================================================

class TestDSDefect:
    def test_defect_sl2(self):
        d = ds_complementarity_defect(2)
        assert d.delta_K == Fraction(13)
        assert d.K_affine == 0
        assert d.factored is True

    def test_defect_sl3(self):
        d = ds_complementarity_defect(3)
        assert d.delta_K == Fraction(250, 3)
        assert d.factored is True

    def test_defect_all_factored(self):
        for N in range(2, 12):
            d = ds_complementarity_defect(N)
            assert d.factored, f"Factorization failed at N={N}"

    def test_defect_nonzero(self):
        for N in range(2, 12):
            d = ds_complementarity_defect(N)
            assert d.delta_K > 0, f"Defect should be positive at N={N}"

    def test_defect_growth(self):
        """δ_K is strictly increasing in N."""
        prev = Fraction(0)
        for N in range(2, 12):
            d = ds_complementarity_defect(N)
            assert d.delta_K > prev
            prev = d.delta_K


# ===========================================================================
# DS complementarity tower
# ===========================================================================

class TestTower:
    def test_arity2_genus1(self):
        entry = tower_arity2(2, 1)
        # Δ^(2,1) = K · λ_1^FP = 13 · 1/24 = 13/24
        assert entry.value == Fraction(13) * _lambda_fp_exact(1)
        assert entry.level_independent is True

    def test_arity2_genus2(self):
        entry = tower_arity2(3, 2)
        expected = K_wn(3) * _lambda_fp_exact(2)
        assert entry.value == expected

    def test_arity3_virasoro(self):
        entry = tower_arity3_virasoro()
        assert entry.value == Fraction(-26)
        assert entry.level_independent is True

    def test_cubic_conductor_virasoro_constant(self):
        """C + C' = -26 regardless of c."""
        for c in [Fraction(1), Fraction(13), Fraction(25), Fraction(1, 3)]:
            assert cubic_conductor_virasoro(c) == Fraction(-26)

    def test_quartic_conductor_virasoro_depends_on_c(self):
        """Q + Q' is NOT constant in c (unlike arity 2 and 3)."""
        Q1 = quartic_conductor_virasoro(Fraction(1))
        Q13 = quartic_conductor_virasoro(Fraction(13))
        assert Q1 is not None
        assert Q13 is not None
        assert Q1 != Q13  # Level-dependent!

    def test_quartic_conductor_numerator_quadratic(self):
        """Numerator 10c² - 260c + 3952 is quadratic in c."""
        # Check at c = 0, 1, 2
        assert quartic_conductor_virasoro_numerator(Fraction(0)) == 3952
        assert quartic_conductor_virasoro_numerator(Fraction(1)) == 10 - 260 + 3952  # = 3702
        assert quartic_conductor_virasoro_numerator(Fraction(13)) == (
            10 * 169 - 260 * 13 + 3952
        )  # = 1690 - 3380 + 3952 = 2262

    def test_full_tower_sl2(self):
        tower = full_tower(2, max_genus=3)
        assert (2, 1) in tower
        assert (2, 2) in tower
        assert (2, 3) in tower
        assert (3, 0) in tower  # Virasoro cubic conductor

    def test_full_tower_sl3_no_arity3(self):
        tower = full_tower(3, max_genus=3)
        assert (2, 1) in tower
        assert (3, 0) not in tower  # Only for N=2 (Virasoro)


# ===========================================================================
# Genus-g defect
# ===========================================================================

class TestGenusDefect:
    def test_genus_defect_affine_vanishes(self):
        for N in range(2, 6):
            for g in range(1, 4):
                assert genus_g_defect_affine(N, g) == 0

    def test_genus_defect_wn_nonzero(self):
        for N in range(2, 6):
            for g in range(1, 4):
                assert genus_g_defect(N, g) != 0

    def test_genus_defect_factorization(self):
        """δ_{Q_g} = K · λ_g^FP."""
        for N in range(2, 6):
            K = K_wn(N)
            for g in range(1, 4):
                assert genus_g_defect(N, g) == K * _lambda_fp_exact(g)


# ===========================================================================
# Large-N asymptotics
# ===========================================================================

class TestLargeN:
    def test_ratio_approaches_1(self):
        """δ_K / (4N³ log N) → 1 (logarithmically slow)."""
        r100 = asymptotic_ratio(100)
        r1000 = asymptotic_ratio(1000)
        # At N=100: ratio ≈ 0.91 (subleading correction ~ (γ-1)/ln N)
        assert abs(r100 - 1.0) < 0.15
        assert abs(r1000 - 1.0) < 0.08

    def test_ratio_improves_with_N(self):
        """Ratio gets closer to 1 as N increases."""
        r100 = asymptotic_ratio(100)
        r1000 = asymptotic_ratio(1000)
        assert abs(r1000 - 1.0) < abs(r100 - 1.0)


# ===========================================================================
# Affine tower vanishing
# ===========================================================================

class TestAffineTowerVanishing:
    def test_affine_tower_vanishes(self):
        for N in range(2, 6):
            assert affine_tower_vanishes(N)


# ===========================================================================
# Hook-type defects
# ===========================================================================

class TestHookDefect:
    def test_ghost_constant_principal(self):
        """For principal (N, 0): C = N(N²-1)/6."""
        for N in range(2, 6):
            C = ghost_constant_hook(N, 0)
            assert C == Fraction(N * (N * N - 1), 6)

    def test_ghost_constant_subregular_sl3(self):
        """For sl₃ subregular (2,1): C_{(2,1)} = 2(4-1)/6 + 1·(4//2)/2 = 1 + 1 = 2."""
        C = ghost_constant_hook(2, 1)
        assert C == Fraction(2)

    def test_complementarity_sl3_subregular(self):
        """K for sl₃ (2,1): self-transpose, so K = -2C_{(2,1)}."""
        K = complementarity_constant_hook(2, 1)
        C = ghost_constant_hook(2, 1)
        assert K == -2 * C  # self-dual partition


# ===========================================================================
# Verification suites
# ===========================================================================

class TestVerificationSuites:
    def test_factorization_all(self):
        results = verify_factorization(10)
        assert all(results.values())

    def test_virasoro_conductors(self):
        v = verify_virasoro_conductors()
        assert v["K_arity2"] == 13
        assert v["cubic_conductor"] == -26
        assert v["cubic_c13"] == -26
        assert v["cubic_c25"] == -26

    def test_genus_defect_vanishes_affine(self):
        results = verify_genus_defect_vanishes_affine()
        assert all(results.values())

    def test_large_N_convergence(self):
        results = verify_large_N_convergence([100, 1000])
        assert abs(results[1000] - 1.0) < 0.08

    def test_summary_table_nonempty(self):
        table = defect_summary_table(6)
        assert len(table) == 5  # N = 2, 3, 4, 5, 6
        assert all(row["factored"] for row in table)

    def test_summary_table_growth(self):
        table = defect_summary_table(6)
        deltas = [row["delta_K"] for row in table]
        for i in range(1, len(deltas)):
            assert deltas[i] > deltas[i - 1]
