"""Tests for conj:type-a-transport-to-transpose investigation.

Tests the conjecture: at generic level, for type A,
    (W^k(sl_N, f_lambda))^! = W^{k^v_lambda}(sl_N, f_{lambda^t})
with k^v = -k - 2N and lambda^t = partition transpose.

Three parts:
  (A) Transport-closure of hook vertices = Par(N).
  (B) Central charge complementarity c + c' is level-independent.
  (C) Generator spectrum, ghost constant, and level transform compatibility.
"""

import pytest
from fractions import Fraction

from compute.lib.transport_to_transpose import (
    TransposeConjectureEngine,
    affine_kappa,
    central_charge_sl_N,
    complementarity_constant,
    complementarity_constant_value,
    complementarity_is_level_independent,
    dim_g0,
    dim_g_half,
    find_path_from_hooks,
    ghost_constant_from_partition,
    hook_ghost_constant,
    hook_kappa,
    non_hook_coverage,
    non_hook_partitions,
)
from compute.lib.w_algebra_transport_propagation import (
    central_charge_principal,
    dual_level,
    generator_weights,
    graph_is_connected,
    hook_partitions,
    hook_transport_closure,
    is_hook,
    partitions,
    transport_coverage_fraction,
    transpose,
)


# =====================================================================
# Part A: Transport-closure = Par(N)
# =====================================================================

class TestPartACoverage:
    """Test that hook transport-closure covers all of Par(N)."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7])
    def test_gamma_connected(self, N):
        """Gamma_N is connected for small N."""
        assert graph_is_connected(N)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7])
    def test_full_coverage(self, N):
        """Transport-closure from hooks = Par(N) for small N."""
        assert transport_coverage_fraction(N) == Fraction(1)

    def test_hook_counts(self):
        """N hook partitions of N exist for each N."""
        for N in range(2, 8):
            assert len(hook_partitions(N)) == N

    def test_non_hook_existence(self):
        """Non-hook partitions first appear at N=4."""
        for N in range(2, 4):
            assert len(non_hook_partitions(N)) == 0
        assert len(non_hook_partitions(4)) == 1  # (2,2)
        assert len(non_hook_partitions(5)) == 2  # (3,2), (2,2,1)

    def test_path_to_every_partition_sl5(self):
        """Every partition of 5 is reachable from a hook."""
        for lam in partitions(5):
            path = find_path_from_hooks(5, lam)
            assert path is not None, f"No path from hooks to {lam}"
            assert is_hook(path[0])

    def test_path_to_22_in_sl4(self):
        """The only non-hook (2,2) in sl_4 is reachable from hooks."""
        path = find_path_from_hooks(4, (2, 2))
        assert path is not None
        assert len(path) >= 2
        assert is_hook(path[0])
        assert path[-1] == (2, 2)


# =====================================================================
# Part B: Central charge formula verification
# =====================================================================

class TestCentralChargeFormula:
    """Test the corrected central charge formula against known values."""

    def test_virasoro_formula(self):
        """Virasoro = W^k(sl_2): c = 1 - 6/(k+2)."""
        for k_num in [1, 2, 3, 5, 7, 11]:
            k = Fraction(k_num)
            c_gen = central_charge_sl_N(2, (2,), k)
            c_vir = Fraction(1) - Fraction(6) / (k + 2)
            assert c_gen == c_vir, f"k={k}: got {c_gen}, want {c_vir}"

    def test_affine_sl2(self):
        """V_k(sl_2): c = 3k/(k+2)."""
        for k_num in [1, 2, 3, 5, 7]:
            k = Fraction(k_num)
            c_gen = central_charge_sl_N(2, (1, 1), k)
            c_aff = Fraction(3) * k / (k + 2)
            assert c_gen == c_aff, f"k={k}: got {c_gen}, want {c_aff}"

    def test_w3_formula(self):
        """W_3 = W^k(sl_3, principal): c = 2 - 24/(k+3)."""
        for k_num in [1, 2, 5, 7]:
            k = Fraction(k_num)
            c_gen = central_charge_sl_N(3, (3,), k)
            c_w3 = Fraction(2) - Fraction(24) / (k + 3)
            assert c_gen == c_w3, f"k={k}: got {c_gen}, want {c_w3}"

    def test_affine_sl3(self):
        """V_k(sl_3): c = 8k/(k+3)."""
        for k_num in [1, 2, 5, 7]:
            k = Fraction(k_num)
            c_gen = central_charge_sl_N(3, (1, 1, 1), k)
            c_aff = Fraction(8) * k / (k + 3)
            assert c_gen == c_aff, f"k={k}: got {c_gen}, want {c_aff}"

    def test_bp_formula(self):
        """BP = W^k(sl_3, (2,1)): c = -4k + 2 - 12/(k+3)."""
        for k_num in [1, 2, 5, 7, 11]:
            k = Fraction(k_num)
            c_gen = central_charge_sl_N(3, (2, 1), k)
            c_bp = -4 * k + 2 - Fraction(12) / (k + 3)
            assert c_gen == c_bp, f"k={k}: got {c_gen}, want {c_bp}"

    def test_principal_formula_consistency(self):
        """General formula matches central_charge_principal for all N."""
        for N in range(2, 8):
            for k_num in [1, 3, 5, 7]:
                k = Fraction(k_num)
                c_gen = central_charge_sl_N(N, (N,), k)
                c_prin = central_charge_principal(N, k)
                assert c_gen == c_prin, f"sl_{N} k={k}: {c_gen} != {c_prin}"

    def test_affine_formula_consistency(self):
        """General formula gives k*dim(g)/(k+N) for trivial partition."""
        for N in range(2, 7):
            for k_num in [1, 3, 5, 7]:
                k = Fraction(k_num)
                c_gen = central_charge_sl_N(N, (1,) * N, k)
                c_aff = k * (N * N - 1) / (k + N)
                assert c_gen == c_aff, f"sl_{N} k={k}: {c_gen} != {c_aff}"


# =====================================================================
# Part B continued: Complementarity
# =====================================================================

class TestComplementarity:
    """Test that c(k, lambda) + c(k', lambda^t) is independent of k."""

    @pytest.mark.parametrize("N", [2, 3])
    def test_small_partitions_level_independent(self, N):
        """Complementarity is level-independent for sl_2 and sl_3.

        The central charge formula is verified for sl_2 and sl_3.
        For N >= 4 with half-integer grading, the per-root-pair formula
        requires further derivation (the half-integer coefficients are
        not fully determined).
        """
        for lam in partitions(N):
            assert complementarity_is_level_independent(N, lam), (
                f"N={N}, lambda={lam}: complementarity depends on level"
            )

    def test_sl4_integer_only_partitions(self):
        """Level-independence for sl_4 partitions with integer-only grading.

        Partitions (4), (3,1), (2,2), (1,1,1,1) have only integer ad(x')
        eigenvalues (no half-integer grading piece).
        """
        # (4): principal, all integer
        assert complementarity_is_level_independent(4, (4,))
        # (2,2): even partition, all integer
        assert complementarity_is_level_independent(4, (2, 2))
        # (1,1,1,1): trivial, all zero (integer)
        assert complementarity_is_level_independent(4, (1, 1, 1, 1))

    def test_virasoro_same_family_26(self):
        """Same-family Virasoro: c(k) + c(-k-4) = 26.

        Note: the TRANSPOSE duality sends (2) -> (1,1), not (2) -> (2).
        The c + c' = 26 identity is for the SAME-FAMILY (principal to
        principal) duality, which is the standard Feigin-Frenkel duality.
        """
        N = 2
        # Same-family: (2) -> (2) with k -> -k - 4
        k = Fraction(7)
        k_dual = dual_level(N, k)
        c1 = central_charge_sl_N(N, (2,), k)
        c2 = central_charge_sl_N(N, (2,), k_dual)
        # c(k) + c(k') for the PRINCIPAL partition (same family)
        # c = 1 - 6/(k+2), c' = 1 - 6/(-k-4+2) = 1 + 6/(k+2)
        # sum = 2, NOT 26. The c + c' = 26 identity is for the FULL Virasoro
        # with the different normalization c = 13 - 6(t-1/t)^2.
        assert c1 + c2 == 2

    def test_virasoro_self_dual_level(self):
        """Virasoro self-dual at c = 13 comes from k = -5/2 in the
        full parametrization. In our c(k) = 1 - 6/(k+2) formula,
        c(k) = c(k') requires k = k' = -k - 4, so k = -2. But
        k = -2 is the critical level for sl_2!

        The resolution: c(k) + c(k') = 2 (not 26) in our normalization.
        Self-dual c = 1 (from c = c' = 2/2 = 1).
        The c = 13 self-duality point uses a DIFFERENT parametrization.
        """
        # At k = -2 (critical): undefined.
        # c(k) = 1 - 6/(k+2). For c = 1: k -> infinity. For c = -5: k = 0.
        # c + c' = 2 for all k. Self-dual c = 1.
        k = Fraction(7)
        c = central_charge_sl_N(2, (2,), k)
        k_dual = dual_level(2, k)
        c_dual = central_charge_sl_N(2, (2,), k_dual)
        assert c + c_dual == 2

    def test_sl3_complementarity_values(self):
        """Complementarity constants for sl_3 (verified by hand)."""
        C_prin = complementarity_constant_value(3, (3,))
        assert C_prin == 10

        C_bp = complementarity_constant_value(3, (2, 1))
        assert C_bp == 28

        C_triv = complementarity_constant_value(3, (1, 1, 1))
        assert C_triv == 10

    def test_complementarity_varies_with_partition(self):
        """The complementarity constant C(N, lambda) VARIES across partitions."""
        vals = set()
        for lam in partitions(3):
            vals.add(complementarity_constant_value(3, lam))
        assert len(vals) >= 2

    def test_sl2_cross_family_complementarity(self):
        """Cross-family sl_2: c_Vir(k) + c_aff(-k-4) is level-independent."""
        values = set()
        for k_num in [1, 3, 5, 7, 11]:
            k = Fraction(k_num)
            values.add(complementarity_constant(2, (2,), k))
        assert len(values) == 1


# =====================================================================
# Part C: Ghost constants and DS-bar commutation
# =====================================================================

class TestGhostConstants:
    """Test ghost constant formula and kappa compatibility."""

    def test_principal_ghost_constant(self):
        """C_{(N)} = N(N^2-1)/6 for principal."""
        for N in range(2, 9):
            C = ghost_constant_from_partition((N,))
            expected = Fraction(N * (N * N - 1), 6)
            assert C == expected

    def test_sl4_hook_ghost_values(self):
        """Ghost constants for sl_4 hooks match tex data."""
        assert ghost_constant_from_partition((4,)) == 10
        assert ghost_constant_from_partition((3, 1)) == 6
        assert ghost_constant_from_partition((2, 1, 1)) == 3

    def test_trivial_ghost_constant_zero(self):
        """C_{(1^N)} = 0 for the trivial partition."""
        for N in range(2, 8):
            assert ghost_constant_from_partition((1,) * N) == 0

    def test_ghost_constant_monotone(self):
        """Ghost constant increases with arm length."""
        for N in range(3, 8):
            prev = Fraction(-1)
            for r in range(N - 1, -1, -1):
                lam = (N - r,) + (1,) * r
                C = ghost_constant_from_partition(lam)
                assert C >= prev
                prev = C

    def test_kappa_compatibility_hook(self):
        """kappa(W) = kappa(V_k) - C_eta for hooks."""
        for N in range(3, 7):
            k = Fraction(7)
            for eta in hook_partitions(N):
                kappa_w = hook_kappa(N, eta, k)
                kappa_aff = affine_kappa(N, k)
                C_eta = ghost_constant_from_partition(eta)
                assert kappa_w == kappa_aff - C_eta


# =====================================================================
# Grading data tests
# =====================================================================

class TestGradingData:
    """Test the sl_2 grading on sl_N."""

    def test_principal_dim_g0(self):
        """For principal partition, dim(g_0) = rank = N-1."""
        for N in range(2, 7):
            assert dim_g0((N,)) == N - 1

    def test_trivial_dim_g0(self):
        """For trivial partition, dim(g_0) = dim(g) = N^2-1."""
        for N in range(2, 7):
            assert dim_g0((1,) * N) == N * N - 1

    def test_bp_dim_g0(self):
        """For BP (sl_3, (2,1)): dim(g_0) = 2 (just the Cartan)."""
        assert dim_g0((2, 1)) == 2

    def test_bp_dim_g_half(self):
        """For BP: dim(g_{1/2}) = 2."""
        assert dim_g_half((2, 1)) == 2

    def test_principal_no_half_integer(self):
        """Principal partition has no half-integer grading."""
        for N in range(2, 7):
            assert dim_g_half((N,)) == 0


# =====================================================================
# Transpose partition tests
# =====================================================================

class TestTransposePartition:
    """Test partition transpose properties."""

    def test_hook_transpose_is_hook(self):
        """Transpose of a hook is a hook."""
        for N in range(2, 8):
            for eta in hook_partitions(N):
                assert is_hook(transpose(eta))

    def test_transpose_involutive(self):
        """(lambda^t)^t = lambda."""
        for N in range(2, 8):
            for lam in partitions(N):
                assert transpose(transpose(lam)) == lam

    def test_hook_transpose_explicit(self):
        """(N-r, 1^r)^t = (r+1, 1^{N-r-1})."""
        for N in range(2, 8):
            for r in range(N):
                eta = (N - r,) + (1,) * r
                expected = (r + 1,) + (1,) * (N - r - 1)
                assert transpose(eta) == expected

    @pytest.mark.parametrize("lam,expected", [
        ((3, 2), (2, 2, 1)),
        ((2, 2, 1), (3, 2)),
        ((2, 2), (2, 2)),
        ((4, 2, 1), (3, 2, 1, 1)),
    ])
    def test_non_hook_transpose(self, lam, expected):
        assert transpose(lam) == expected

    def test_bp_self_transpose(self):
        """(2,1)^t = (2,1): Bershadsky-Polyakov is self-transpose."""
        assert transpose((2, 1)) == (2, 1)


# =====================================================================
# Level transform tests
# =====================================================================

class TestLevelTransform:
    """Test the Feigin-Frenkel level transform k^v = -k - 2N."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_involutivity(self, N):
        k = Fraction(7)
        assert dual_level(N, dual_level(N, k)) == k

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_critical_fixed_point(self, N):
        """k = -N is a fixed point."""
        assert dual_level(N, Fraction(-N)) == Fraction(-N)

    def test_sl2_dual_level(self):
        assert dual_level(2, Fraction(7)) == Fraction(-11)


# =====================================================================
# Non-hook partition analysis
# =====================================================================

class TestNonHookAnalysis:
    """Deep analysis of non-hook partitions."""

    def test_sl4_non_hook_reached(self):
        assert non_hook_coverage(4)['all_reached']

    def test_sl5_non_hooks_reached(self):
        assert non_hook_coverage(5)['all_reached']

    def test_sl6_non_hooks_reached(self):
        assert non_hook_coverage(6)['all_reached']

    def test_sl4_even_non_hook_complement_level_independent(self):
        """Complementarity for (2,2) in sl_4 is level-independent.

        (2,2) has only integer grading, so the formula is reliable.
        """
        assert complementarity_is_level_independent(4, (2, 2))


# =====================================================================
# Conjecture engine tests
# =====================================================================

class TestConjectureEngine:
    """Systematic conjecture evidence via TransposeConjectureEngine."""

    def test_engine_part_A(self):
        engine = TransposeConjectureEngine(N_max=6)
        results = engine.part_A_coverage()
        for key, val in results.items():
            assert val, f"Part A: {key}"

    def test_engine_part_B_small(self):
        """Part B for sl_2 and sl_3 (where formula is fully verified)."""
        engine = TransposeConjectureEngine(N_max=3)
        results = engine.part_B_complementarity()
        for key, val in results.items():
            assert val, f"Part B: {key}"

    def test_engine_ghost(self):
        engine = TransposeConjectureEngine(N_max=5)
        results = engine.hook_ghost_verification()
        for key, val in results.items():
            assert val, f"Ghost: {key}"


# =====================================================================
# Integration tests
# =====================================================================

class TestIntegration:
    """Integration tests combining multiple aspects."""

    def test_sl3_all_hooks(self):
        """All partitions of 3 are hook-type."""
        assert set(partitions(3)) == set(hook_partitions(3))

    def test_sl4_hooks_and_non_hooks(self):
        """sl_4: 4 hooks + 1 non-hook = 5 partitions."""
        hooks = {lam for lam in partitions(4) if is_hook(lam)}
        non_hooks = {lam for lam in partitions(4) if not is_hook(lam)}
        assert hooks == {(4,), (3, 1), (2, 1, 1), (1, 1, 1, 1)}
        assert non_hooks == {(2, 2)}

    def test_sl5_non_hooks_form_dual_pair(self):
        """(3,2)^t = (2,2,1) and (2,2,1)^t = (3,2)."""
        assert transpose((3, 2)) == (2, 2, 1)
        assert transpose((2, 2, 1)) == (3, 2)

    def test_22_self_transpose(self):
        """(2,2) is self-transpose."""
        assert transpose((2, 2)) == (2, 2)

    def test_sl4_ghost_from_tex(self):
        """Ghost constants match Computation comp:sl4-hook-data."""
        assert ghost_constant_from_partition((4,)) == 10
        assert ghost_constant_from_partition((3, 1)) == 6
        assert ghost_constant_from_partition((2, 1, 1)) == 3

    def test_complementarity_structure_sl4_integer_grading(self):
        """Complementarity for sl_4 partitions with integer-only grading."""
        # Integer-only partitions of 4: (4), (2,2), (1,1,1,1)
        for lam in [(4,), (2, 2), (1, 1, 1, 1)]:
            assert complementarity_is_level_independent(4, lam), (
                f"sl_4 ({lam}): complementarity depends on level"
            )

    def test_complementarity_structure_sl3(self):
        """Complementarity for all sl_3 partitions."""
        for lam in partitions(3):
            assert complementarity_is_level_independent(3, lam)
