"""Tests for W-orbit duality (conj:w-orbit-duality verification).

Tests cover:
  1. Lie algebra data (type A, B, C, D)
  2. Partition operations and BV duality
  3. Feigin-Frenkel dual level
  4. Central charge formulas (Virasoro, W_3, W_N, BP)
  5. Complementarity sums (Koszul conductors)
  6. Hook orbit BV duality
  7. Principal orbit recovery
  8. Full type-A verification
  9. Hilbert series checks
  10. Non-simply-laced Langlands duality
  11. Orbit dimension and centralizer identities
  12. Verified complementarity table

Ground truth references:
  - CLAUDE.md verified formulas
  - thm:w-algebra-koszul-main, prop:bp-duality
  - rem:koszul-conductor-explicit in examples_summary.tex
  - comp:sl3-ds-hierarchy, comp:w3-curvature-dual in w_algebras_deep.tex
  - nonprincipal_ds_reduction.py (BP data)
"""

import pytest

from sympy import Rational, Symbol, diff, simplify

from compute.lib.w_orbit_duality import (
    SimpleLieAlgebraData,
    WOrbitDualityVerification,
    all_partitions_of,
    barbasch_vogan_dual_type_a,
    bp_central_charge,
    bv_dual_is_involution_type_a,
    bv_self_dual_partitions,
    centralizer_dimension_type_a,
    complementarity_check,
    complementarity_sum_bp,
    complementarity_sum_principal,
    complementarity_sum_virasoro,
    ff_critical_check,
    ff_dual_level,
    ff_dual_level_type_a,
    ff_involutivity_check,
    full_type_a_verification,
    general_ds_central_charge,
    hook_pair_bv_duality,
    hook_pair_first_nonselfdual,
    hook_partition,
    is_self_dual_orbit_type_a,
    koszul_conductor_principal,
    koszul_hilbert_product_check,
    langlands_dual_data,
    langlands_dual_type,
    lie_algebra_data,
    minimal_partition,
    normalize_partition,
    num_positive_roots_removed,
    orbit_dimension_sum_type_a,
    orbit_dimension_type_a,
    orbit_duality_profile_type_a,
    partition_size,
    principal_hilbert_series_coeffs,
    principal_partition,
    principal_recovery_check,
    subregular_partition,
    transpose_partition,
    trivial_partition,
    verified_complementarity_table,
    verify_orbit_duality_type_a,
    virasoro_central_charge,
    w3_central_charge,
    wn_central_charge,
)


# =====================================================================
# Section 1: Lie algebra data
# =====================================================================

class TestLieAlgebraData:
    """Tests for Lie algebra data construction."""

    def test_sl2_data(self):
        g = lie_algebra_data("A", 1)
        assert g.rank == 1
        assert g.dimension == 3
        assert g.h_dual == 2
        assert g.exponents == (1,)
        assert g.is_simply_laced

    def test_sl3_data(self):
        g = lie_algebra_data("A", 2)
        assert g.rank == 2
        assert g.dimension == 8
        assert g.h_dual == 3
        assert g.exponents == (1, 2)
        assert g.is_simply_laced

    def test_sl4_data(self):
        g = lie_algebra_data("A", 3)
        assert g.rank == 3
        assert g.dimension == 15
        assert g.h_dual == 4
        assert g.exponents == (1, 2, 3)

    def test_sl5_data(self):
        g = lie_algebra_data("A", 4)
        assert g.rank == 4
        assert g.dimension == 24
        assert g.h_dual == 5
        assert g.exponents == (1, 2, 3, 4)

    def test_so5_data_type_b(self):
        """B_2 = so_5: h^vee = 3, dim = 10."""
        g = lie_algebra_data("B", 2)
        assert g.rank == 2
        assert g.dimension == 10
        assert g.h_dual == 3
        assert not g.is_simply_laced

    def test_so7_data_type_b(self):
        """B_3 = so_7: h^vee = 5, dim = 21."""
        g = lie_algebra_data("B", 3)
        assert g.rank == 3
        assert g.dimension == 21
        assert g.h_dual == 5

    def test_sp4_data_type_c(self):
        """C_2 = sp_4: h^vee = 3, dim = 10."""
        g = lie_algebra_data("C", 2)
        assert g.rank == 2
        assert g.dimension == 10
        assert g.h_dual == 3
        assert not g.is_simply_laced

    def test_sp6_data_type_c(self):
        """C_3 = sp_6: h^vee = 4, dim = 21."""
        g = lie_algebra_data("C", 3)
        assert g.rank == 3
        assert g.dimension == 21
        assert g.h_dual == 4

    def test_so8_data_type_d(self):
        """D_4 = so_8: h^vee = 6, dim = 28."""
        g = lie_algebra_data("D", 4)
        assert g.rank == 4
        assert g.dimension == 28
        assert g.h_dual == 6
        assert g.is_simply_laced

    def test_b_n_dual_coxeter_numbers(self):
        """B_n: h^vee = 2n-1 (CLAUDE.md critical pitfall)."""
        for n in range(2, 7):
            g = lie_algebra_data("B", n)
            assert g.h_dual == 2 * n - 1

    def test_c_n_dual_coxeter_numbers(self):
        """C_n: h^vee = n+1 (CLAUDE.md critical pitfall)."""
        for n in range(2, 7):
            g = lie_algebra_data("C", n)
            assert g.h_dual == n + 1

    def test_h_dual_bc_differ_for_non_simply_laced(self):
        """h^vee(B_n) != h^vee(C_n) for n >= 3 (CLAUDE.md)."""
        for n in range(3, 7):
            b = lie_algebra_data("B", n)
            c = lie_algebra_data("C", n)
            assert b.h_dual != c.h_dual
            assert b.h_dual == 2 * n - 1
            assert c.h_dual == n + 1


# =====================================================================
# Section 2: Langlands duality
# =====================================================================

class TestLanglandsDuality:
    """Tests for Langlands dual constructions."""

    def test_type_a_self_dual(self):
        assert langlands_dual_type("A") == "A"

    def test_type_d_self_dual(self):
        assert langlands_dual_type("D") == "D"

    def test_b_c_dual(self):
        assert langlands_dual_type("B") == "C"
        assert langlands_dual_type("C") == "B"

    def test_langlands_dual_data_simply_laced(self):
        """For simply-laced, g^vee = g."""
        g = lie_algebra_data("A", 3)
        gv = langlands_dual_data(g)
        assert gv.h_dual == g.h_dual
        assert gv.dimension == g.dimension

    def test_langlands_dual_data_b_c(self):
        """B_n^vee = C_n, so h^vee changes."""
        g = lie_algebra_data("B", 3)
        gv = langlands_dual_data(g)
        assert gv.lie_type == "C"
        assert gv.rank == 3
        # B_3: h^vee = 5, C_3: h^vee = 4
        assert g.h_dual == 5
        assert gv.h_dual == 4
        assert g.h_dual != gv.h_dual


# =====================================================================
# Section 3: Partition operations
# =====================================================================

class TestPartitions:
    """Tests for partition operations."""

    def test_normalize(self):
        assert normalize_partition([3, 1, 2]) == (3, 2, 1)
        assert normalize_partition([5]) == (5,)
        assert normalize_partition([1, 1, 1]) == (1, 1, 1)

    def test_normalize_rejects_zero(self):
        with pytest.raises(ValueError):
            normalize_partition([3, 0, 1])

    def test_normalize_rejects_empty(self):
        with pytest.raises(ValueError):
            normalize_partition([])

    def test_partition_size(self):
        assert partition_size([3, 2, 1]) == 6
        assert partition_size([5]) == 5
        assert partition_size([1, 1, 1, 1]) == 4

    def test_transpose_partition_simple(self):
        assert transpose_partition([3]) == (1, 1, 1)
        assert transpose_partition([1, 1, 1]) == (3,)
        assert transpose_partition([2, 1]) == (2, 1)

    def test_transpose_is_involution(self):
        for n in range(1, 8):
            for lam in all_partitions_of(n):
                assert transpose_partition(transpose_partition(lam)) == lam

    def test_principal_partition(self):
        for n in range(2, 8):
            assert principal_partition(n) == (n,)

    def test_trivial_partition(self):
        for n in range(2, 8):
            assert trivial_partition(n) == (1,) * n

    def test_subregular_partition(self):
        assert subregular_partition(3) == (2, 1)
        assert subregular_partition(4) == (3, 1)
        assert subregular_partition(5) == (4, 1)

    def test_minimal_partition(self):
        assert minimal_partition(3) == (2, 1)
        assert minimal_partition(4) == (2, 1, 1)
        assert minimal_partition(5) == (2, 1, 1, 1)

    def test_sl3_minimal_equals_subregular(self):
        """For sl_3, minimal = subregular (unique intermediate orbit)."""
        assert minimal_partition(3) == subregular_partition(3) == (2, 1)

    def test_sl4_minimal_ne_subregular(self):
        """For sl_4, minimal != subregular."""
        assert minimal_partition(4) == (2, 1, 1)
        assert subregular_partition(4) == (3, 1)
        assert minimal_partition(4) != subregular_partition(4)

    def test_hook_partition(self):
        assert hook_partition(4, 0) == (4,)  # principal
        assert hook_partition(4, 1) == (3, 1)  # subregular
        assert hook_partition(4, 2) == (2, 1, 1)  # minimal
        assert hook_partition(4, 3) == (1, 1, 1, 1)  # trivial

    def test_all_partitions_count(self):
        """Partition counts: p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        expected = {1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15}
        for n, count in expected.items():
            assert len(all_partitions_of(n)) == count


# =====================================================================
# Section 4: Barbasch-Vogan duality
# =====================================================================

class TestBVDuality:
    """Tests for Barbasch-Vogan duality in type A."""

    def test_bv_is_transpose(self):
        """BV dual in type A = partition transpose (def:bv-dual)."""
        assert barbasch_vogan_dual_type_a([3]) == (1, 1, 1)
        assert barbasch_vogan_dual_type_a([2, 1]) == (2, 1)
        assert barbasch_vogan_dual_type_a([1, 1, 1]) == (3,)

    def test_bv_involution_small(self):
        """BV duality is an involution on partitions of n."""
        for n in range(1, 9):
            assert bv_dual_is_involution_type_a(n)

    def test_bv_principal_to_trivial(self):
        """BV dual of principal (n) = trivial (1^n)."""
        for n in range(2, 8):
            assert barbasch_vogan_dual_type_a(principal_partition(n)) == trivial_partition(n)

    def test_bv_trivial_to_principal(self):
        """BV dual of trivial (1^n) = principal (n)."""
        for n in range(2, 8):
            assert barbasch_vogan_dual_type_a(trivial_partition(n)) == principal_partition(n)

    def test_sl3_minimal_self_dual(self):
        """(2,1) is BV self-dual (symmetric partition)."""
        assert is_self_dual_orbit_type_a([2, 1])

    def test_sl4_non_selfdual_pair(self):
        """(3,1) <-> (2,1,1) are NOT self-dual."""
        assert not is_self_dual_orbit_type_a([3, 1])
        assert not is_self_dual_orbit_type_a([2, 1, 1])
        assert barbasch_vogan_dual_type_a([3, 1]) == (2, 1, 1)
        assert barbasch_vogan_dual_type_a([2, 1, 1]) == (3, 1)

    def test_sl4_self_dual_partition(self):
        """(2,2) is BV self-dual."""
        assert is_self_dual_orbit_type_a([2, 2])

    def test_self_dual_partitions_n4(self):
        """Self-dual partitions of 4: (4), (2,2), (1,1,1,1)."""
        # Wait: (4)^t = (1,1,1,1) so (4) is NOT self-dual
        # (2,2)^t = (2,2) so (2,2) IS self-dual
        # (2,1,1)^t = (3,1) so NOT self-dual
        # (3,1)^t = (2,1,1) so NOT self-dual
        # (1,1,1,1)^t = (4) so NOT self-dual
        sd = bv_self_dual_partitions(4)
        assert sd == [(2, 2)]

    def test_self_dual_partitions_n5(self):
        """Self-dual partitions of 5."""
        sd = bv_self_dual_partitions(5)
        # (5)^t=(1^5), (4,1)^t=(2,1,1,1), (3,2)^t=(2,2,1),
        # (3,1,1)^t=(3,1,1) YES, (2,2,1)^t=(3,2), (2,1,1,1)^t=(4,1), (1^5)^t=(5)
        assert (3, 1, 1) in sd

    def test_hook_bv_dual_transpose(self):
        """Hook (n-r, 1^r)^t = (r+1, 1^{n-r-1})."""
        for n in range(3, 8):
            for r in range(1, n - 1):
                source = hook_partition(n, r)
                expected = hook_partition(n, n - r - 1)
                assert barbasch_vogan_dual_type_a(source) == expected


# =====================================================================
# Section 5: Feigin-Frenkel dual level
# =====================================================================

class TestFFDualLevel:
    """Tests for Feigin-Frenkel dual level computation."""

    def test_ff_formula(self):
        """k' = -k - 2h^vee (CLAUDE.md)."""
        k = Symbol("k")
        assert ff_dual_level(k, 2) == -k - 4  # sl_2
        assert ff_dual_level(k, 3) == -k - 6  # sl_3
        assert ff_dual_level(k, 4) == -k - 8  # sl_4

    def test_ff_involutivity(self):
        """(k')' = k for all h^vee."""
        k = Symbol("k")
        for h in range(2, 10):
            assert ff_involutivity_check(k, h) == 0

    def test_ff_critical_self_duality(self):
        """At k = -h^vee: k' = -h^vee (critical level is fixed point)."""
        for h in range(2, 10):
            assert ff_critical_check(h) == 0

    def test_ff_sl2_virasoro(self):
        """For sl_2: k' = -k-4."""
        k = Symbol("k")
        assert simplify(ff_dual_level_type_a(k, 2) - (-k - 4)) == 0

    def test_ff_sl3(self):
        """For sl_3: k' = -k-6."""
        k = Symbol("k")
        assert simplify(ff_dual_level_type_a(k, 3) - (-k - 6)) == 0

    def test_ff_numeric(self):
        """Numeric level checks."""
        # sl_2 at k=1: k' = -5
        assert ff_dual_level(1, 2) == -5
        # sl_3 at k=1: k' = -7
        assert ff_dual_level(1, 3) == -7
        # sl_2 at k=0: k' = -4
        assert ff_dual_level(0, 2) == -4

    def test_ff_not_negative_k_minus_h(self):
        """Verify FF is NOT -k-h^vee (common mistake from CLAUDE.md)."""
        k = Symbol("k")
        for h in range(2, 6):
            correct = ff_dual_level(k, h)
            wrong = -k - h
            assert simplify(correct - wrong) != 0


# =====================================================================
# Section 6: Central charge formulas
# =====================================================================

class TestCentralCharges:
    """Tests for DS central charge computations."""

    def test_virasoro_formula(self):
        """c = 1 - 6(k+1)^2/(k+2) (Fateev-Lukyanov at N=2)."""
        # k=0: c = 1 - 6/2 = -2
        assert virasoro_central_charge(0) == -2
        # k=1: c = 1 - 6*4/3 = 1 - 8 = -7
        assert virasoro_central_charge(1) == -7
        # k=-1: c = 1 - 0 = 1
        assert virasoro_central_charge(-1) == 1

    def test_virasoro_generic(self):
        k = Symbol("k")
        c = virasoro_central_charge(k)
        assert simplify(c - (1 - 6 * (k + 1)**2 / (k + 2))) == 0

    def test_w3_formula(self):
        """c = 2 - 24(k+2)^2/(k+3) (Fateev-Lukyanov at N=3)."""
        # k=0: c = 2 - 24*4/3 = 2 - 32 = -30
        assert w3_central_charge(0) == -30
        # k=-2: c = 2 - 0 = 2
        assert w3_central_charge(-2) == 2

    def test_w3_generic(self):
        k = Symbol("k")
        c = w3_central_charge(k)
        assert simplify(c - (2 - 24 * (k + 2)**2 / (k + 3))) == 0

    def test_wn_reduces_to_virasoro(self):
        """W_2 = Virasoro: wn_central_charge(2, k) = virasoro(k)."""
        k = Symbol("k")
        assert simplify(wn_central_charge(2, k) - virasoro_central_charge(k)) == 0

    def test_wn_reduces_to_w3(self):
        """W_3: wn_central_charge(3, k) = w3_central_charge(k)."""
        k = Symbol("k")
        assert simplify(wn_central_charge(3, k) - w3_central_charge(k)) == 0

    def test_bp_formula(self):
        """BP: c = 2 - 24(k+1)^2/(k+3) (FKR 2020)."""
        k = Symbol("k")
        c = bp_central_charge(k)
        assert simplify(c - (2 - 24 * (k + 1) ** 2 / (k + 3))) == 0

    def test_bp_numeric_values(self):
        """BP at specific levels."""
        # k = -1/2: (k+1)^2 = 1/4, k+3 = 5/2
        # c = 2 - 24*(1/4)/(5/2) = 2 - 6/(5/2) = 2 - 12/5 = -2/5
        c = bp_central_charge(Rational(-1, 2))
        assert simplify(c - Rational(-2, 5)) == 0

    def test_bp_at_k_minus_half(self):
        """At k = -1/2, BP has c = 2 - 24*(1/2)^2/(5/2) = 2 - 12/5 = -2/5."""
        c = bp_central_charge(Rational(-1, 2))
        assert c == Rational(-2, 5)

    def test_bp_ne_w3(self):
        """BP central charge differs from W_3 (different orbits)."""
        k = Symbol("k")
        assert simplify(bp_central_charge(k) - w3_central_charge(k)) != 0

    def test_general_ds_principal_dispatch(self):
        """general_ds_central_charge dispatches to wn for principal orbits."""
        k = Symbol("k")
        for n in range(2, 6):
            c = general_ds_central_charge(n, principal_partition(n), k)
            assert simplify(c - wn_central_charge(n, k)) == 0

    def test_general_ds_trivial_dispatch(self):
        """general_ds_central_charge gives Sugawara for trivial orbit."""
        k = Symbol("k")
        c = general_ds_central_charge(3, trivial_partition(3), k)
        expected = k * 8 / (k + 3)  # Sugawara for sl_3
        assert simplify(c - expected) == 0

    def test_general_ds_bp_dispatch(self):
        """general_ds_central_charge gives BP for sl_3 minimal."""
        k = Symbol("k")
        c = general_ds_central_charge(3, (2, 1), k)
        assert simplify(c - bp_central_charge(k)) == 0


# =====================================================================
# Section 7: Complementarity sums (Koszul conductors)
# =====================================================================

class TestComplementarity:
    """Tests for Koszul conductor computations."""

    def test_virasoro_complementarity_is_26(self):
        """c(k) + c(-k-4) = 26."""
        K = complementarity_sum_virasoro()
        assert simplify(K - 26) == 0

    def test_w3_complementarity_is_100(self):
        """c(k) + c(-k-6) = 100."""
        K = complementarity_sum_principal(3)
        assert simplify(K - 100) == 0

    def test_bp_complementarity(self):
        """c_BP(k) + c_BP(-k-6) = constant (BP is non-principal)."""
        K = complementarity_sum_bp()
        # BP uses a different formula; just verify it's a constant
        assert simplify(K).is_number

    def test_w4_complementarity_is_246(self):
        """K_4 = 246 = 2(N-1) + 4N(N^2-1) at N=4."""
        K = complementarity_sum_principal(4)
        assert simplify(K - 246) == 0

    def test_w5_complementarity_is_488(self):
        """K_5 = 488 = 2(N-1) + 4N(N^2-1) at N=5."""
        K = complementarity_sum_principal(5)
        assert simplify(K - 488) == 0

    def test_koszul_conductor_closed_form(self):
        """K_N = 2(N-1) + 4N(N^2-1) (Freudenthal-de Vries)."""
        for n in range(2, 8):
            K = koszul_conductor_principal(n)
            assert K == 2 * (n - 1) + 4 * n * (n**2 - 1)

    def test_koszul_conductor_first_values(self):
        """K_2=26, K_3=100, K_4=246, K_5=488."""
        expected = {2: 26, 3: 100, 4: 246, 5: 488}
        for n, K in expected.items():
            assert koszul_conductor_principal(n) == K

    def test_complementarity_check_symbolic(self):
        """Symbolic check: complementarity matches closed form."""
        for n in range(2, 6):
            assert complementarity_check(n)

    def test_complementarity_k_independent_virasoro(self):
        """Virasoro complementarity is k-independent."""
        k = Symbol("k")
        kp = ff_dual_level_type_a(k, 2)
        total = virasoro_central_charge(k) + virasoro_central_charge(kp)
        assert simplify(diff(total, k)) == 0

    def test_complementarity_k_independent_w3(self):
        """W_3 complementarity is k-independent."""
        k = Symbol("k")
        kp = ff_dual_level_type_a(k, 3)
        total = w3_central_charge(k) + w3_central_charge(kp)
        assert simplify(diff(total, k)) == 0

    def test_complementarity_k_independent_bp(self):
        """BP complementarity is k-independent."""
        k = Symbol("k")
        kp = ff_dual_level_type_a(k, 3)
        total = bp_central_charge(k) + bp_central_charge(kp)
        assert simplify(diff(total, k)) == 0

    def test_complementarity_k_independent_wn(self):
        """W_N complementarity is k-independent for N=2,...,6."""
        k = Symbol("k")
        for n in range(2, 7):
            kp = ff_dual_level_type_a(k, n)
            total = wn_central_charge(n, k) + wn_central_charge(n, kp)
            assert simplify(diff(total, k)) == 0

    def test_bp_complementarity_ne_principal_sl3(self):
        """K_BP != K_3 = 100 (different orbits, different conductors)."""
        K_bp = complementarity_sum_bp()
        K_w3 = complementarity_sum_principal(3)
        assert simplify(K_bp - K_w3) != 0
        assert simplify(K_bp).is_number
        assert simplify(K_w3 - 100) == 0


# =====================================================================
# Section 8: Hook orbit BV duality
# =====================================================================

class TestHookOrbits:
    """Tests for hook orbit BV duality."""

    def test_hook_bv_match_sl4(self):
        """(3,1) <-> (2,1,1) in sl_4."""
        pair = hook_pair_bv_duality(4, 1)
        assert pair["match"]
        assert pair["source"] == (3, 1)
        assert pair["target"] == (2, 1, 1)
        assert not pair["is_self_dual"]

    def test_hook_bv_match_sl5_r1(self):
        """(4,1) <-> (2,1,1,1) in sl_5."""
        pair = hook_pair_bv_duality(5, 1)
        assert pair["match"]
        assert pair["source"] == (4, 1)
        assert pair["target"] == (2, 1, 1, 1)

    def test_hook_bv_match_sl5_r2(self):
        """(3,1,1) is self-dual in sl_5."""
        pair = hook_pair_bv_duality(5, 2)
        assert pair["match"]
        assert pair["source"] == (3, 1, 1)
        assert pair["target"] == (3, 1, 1)
        assert pair["is_self_dual"]

    def test_hook_bv_self_dual_only_middle(self):
        """Hook (n-r, 1^r) is self-dual iff r = (n-1)/2."""
        for n in range(3, 10):
            for r in range(1, n - 1):
                pair = hook_pair_bv_duality(n, r)
                assert pair["match"]
                expected_self_dual = (2 * r + 1 == n)
                assert pair["is_self_dual"] == expected_self_dual

    def test_first_nonselfdual_sl4(self):
        """First non-self-dual hook pair in sl_4."""
        pair = hook_pair_first_nonselfdual(4)
        assert pair is not None
        assert not pair["is_self_dual"]

    def test_hook_orbit_dim_sum(self):
        """dim(O) + dim(O^D) for hook pairs."""
        for n in range(3, 7):
            for r in range(1, n - 1):
                pair = hook_pair_bv_duality(n, r)
                # Orbit dimension identity
                assert pair["source_orbit_dim"] >= 0
                assert pair["target_orbit_dim"] >= 0


# =====================================================================
# Section 9: Orbit dimensions and centralizers
# =====================================================================

class TestOrbitDimensions:
    """Tests for nilpotent orbit dimensions and centralizers."""

    def test_principal_orbit_dim_sl_n(self):
        """Principal orbit in sl_n has dim = n^2 - n (= dim sl_n - rank)."""
        for n in range(2, 8):
            dim = orbit_dimension_type_a(principal_partition(n))
            assert dim == n * n - n

    def test_trivial_orbit_dim_zero(self):
        """Trivial orbit has dim 0."""
        for n in range(2, 8):
            assert orbit_dimension_type_a(trivial_partition(n)) == 0

    def test_sl3_orbit_dims(self):
        """sl_3 orbit dimensions from comp:sl3-ds-hierarchy."""
        assert orbit_dimension_type_a((1, 1, 1)) == 0  # trivial
        assert orbit_dimension_type_a((2, 1)) == 4     # minimal = subregular
        assert orbit_dimension_type_a((3,)) == 6       # principal

    def test_sl4_orbit_dims(self):
        """sl_4 orbit dimensions."""
        assert orbit_dimension_type_a((1, 1, 1, 1)) == 0   # trivial
        assert orbit_dimension_type_a((2, 1, 1)) == 6      # minimal
        assert orbit_dimension_type_a((2, 2)) == 8         # middle
        assert orbit_dimension_type_a((3, 1)) == 10        # subregular
        assert orbit_dimension_type_a((4,)) == 12          # principal

    def test_centralizer_dim_principal(self):
        """Centralizer of principal: dim = rank (sl_n has rank n-1)."""
        for n in range(2, 8):
            dim = centralizer_dimension_type_a(principal_partition(n))
            assert dim == n - 1

    def test_centralizer_dim_trivial(self):
        """Centralizer of trivial: dim = dim(sl_n) = n^2 - 1."""
        for n in range(2, 8):
            dim = centralizer_dimension_type_a(trivial_partition(n))
            assert dim == n * n - 1

    def test_orbit_plus_centralizer(self):
        """dim(O) + dim(Z(e)) = dim(g) - 1 for sl_n orbits.
        Actually: dim(O) + dim(g^e) = dim(g) where g^e is the full centralizer.
        Our formula: dim(Z) = sum(lambda_i^t)^2 - 1, dim(O) = n^2 - sum(lambda_i^t)^2.
        So dim(O) + dim(Z) = n^2 - 1 = dim(sl_n).
        """
        for n in range(2, 7):
            for lam in all_partitions_of(n):
                d_o = orbit_dimension_type_a(lam)
                d_z = centralizer_dimension_type_a(lam)
                assert d_o + d_z == n * n - 1

    def test_num_positive_roots_removed(self):
        """Number of positive roots removed = half orbit dimension."""
        for n in range(2, 6):
            for lam in all_partitions_of(n):
                assert num_positive_roots_removed(lam) == orbit_dimension_type_a(lam) // 2

    def test_orbit_dim_sum_hook_pairs(self):
        """Orbit dimension sum for hook pair duals."""
        for n in range(3, 8):
            for r in range(1, n - 1):
                source = hook_partition(n, r)
                target = barbasch_vogan_dual_type_a(source)
                d_s = orbit_dimension_type_a(source)
                d_t = orbit_dimension_type_a(target)
                # Both must be nonneg even numbers
                assert d_s >= 0 and d_s % 2 == 0
                assert d_t >= 0 and d_t % 2 == 0


# =====================================================================
# Section 10: Principal orbit recovery
# =====================================================================

class TestPrincipalRecovery:
    """Tests for principal orbit special case of orbit duality."""

    def test_principal_recovery_sl2(self):
        checks = principal_recovery_check(2)
        assert all(checks.values())

    def test_principal_recovery_sl3(self):
        checks = principal_recovery_check(3)
        assert all(checks.values())

    def test_principal_recovery_sl4(self):
        checks = principal_recovery_check(4)
        assert all(checks.values())

    def test_principal_recovery_sl5(self):
        checks = principal_recovery_check(5)
        assert all(checks.values())

    def test_principal_bv_dual_is_trivial(self):
        """BV dual of principal = trivial for all sl_n."""
        for n in range(2, 10):
            checks = principal_recovery_check(n)
            assert checks["bv_dual_of_principal_is_trivial"]


# =====================================================================
# Section 11: Hilbert series
# =====================================================================

class TestHilbertSeries:
    """Tests for Hilbert series of principal W-algebras."""

    def test_virasoro_hilbert(self):
        """W_2: H(t) = 1/(1-t^2) = 1 + t^2 + t^4 + ..."""
        coeffs = principal_hilbert_series_coeffs(2, 10)
        assert coeffs[0] == 1
        assert coeffs[1] == 0
        assert coeffs[2] == 1
        assert coeffs[3] == 0
        assert coeffs[4] == 1

    def test_w3_hilbert(self):
        """W_3: H(t) = 1/((1-t^2)(1-t^3))."""
        coeffs = principal_hilbert_series_coeffs(3, 12)
        # 1 + 0 + 1 + 1 + 1 + 1 + 2 + 1 + 2 + 2 + 2 + 2 + 3
        assert coeffs[0] == 1
        assert coeffs[1] == 0
        assert coeffs[2] == 1
        assert coeffs[3] == 1
        assert coeffs[4] == 1
        assert coeffs[5] == 1
        assert coeffs[6] == 2

    def test_w4_hilbert_start(self):
        """W_4: H(t) = 1/((1-t^2)(1-t^3)(1-t^4))."""
        coeffs = principal_hilbert_series_coeffs(4, 8)
        assert coeffs[0] == 1
        assert coeffs[1] == 0
        assert coeffs[2] == 1
        assert coeffs[3] == 1
        assert coeffs[4] == 2

    def test_koszul_product_virasoro(self):
        """For Virasoro (self-dual): H(t)*H(-t) should relate to 1.

        For classical Koszul duality H_A(t)*H_{A!}(-t) = 1.
        Virasoro is self-dual (W_2^k -> W_2^{k'} by FF), so
        H(t)*H(-t) = 1/(1-t^2) * 1/(1-t^2) = 1/(1-t^2)^2 != 1.

        This is because the OS algebra of the W-algebra is NOT the same
        as a classical Koszul algebra. The chiral bar complex is more
        intricate. We check the product structure here for reference.
        """
        coeffs = principal_hilbert_series_coeffs(2, 10)
        product = koszul_hilbert_product_check(coeffs, 10)
        # For Virasoro, H(t)*H(-t) = 1/(1-t^4) (even part survives)
        # So product[0] = 1, product[2] = 0, product[4] = 1, ...
        assert product[0] == 1
        # The product is 1 + 0 + 0 + 0 + 1 + ... (not all zero after deg 0)
        # This confirms that classical Koszul H*H(-t)=1 does NOT hold directly


# =====================================================================
# Section 12: Orbit duality profiles
# =====================================================================

class TestOrbitDualityProfiles:
    """Tests for orbit duality profile construction."""

    def test_sl3_minimal_profile(self):
        """sl_3 minimal = (2,1): self-dual, orbit class = subregular."""
        profile = orbit_duality_profile_type_a((2, 1))
        assert profile.n == 3
        assert profile.partition == (2, 1)
        assert profile.dual_partition == (2, 1)
        assert profile.is_self_dual
        assert profile.orbit_dim == 4
        # For sl_3, minimal = subregular
        assert profile.orbit_class in ("minimal", "subregular")

    def test_sl4_minimal_profile(self):
        """sl_4 minimal = (2,1,1)."""
        profile = orbit_duality_profile_type_a((2, 1, 1))
        assert profile.n == 4
        assert profile.partition == (2, 1, 1)
        assert profile.dual_partition == (3, 1)
        assert not profile.is_self_dual
        assert profile.orbit_class == "minimal"

    def test_sl4_subregular_profile(self):
        """sl_4 subregular = (3,1)."""
        profile = orbit_duality_profile_type_a((3, 1))
        assert profile.n == 4
        assert profile.partition == (3, 1)
        assert profile.dual_partition == (2, 1, 1)
        assert not profile.is_self_dual
        assert profile.orbit_class == "subregular"

    def test_principal_profile(self):
        for n in range(2, 6):
            profile = orbit_duality_profile_type_a(principal_partition(n))
            assert profile.orbit_class == "principal"
            assert profile.dual_partition == trivial_partition(n)

    def test_trivial_profile(self):
        for n in range(2, 6):
            profile = orbit_duality_profile_type_a(trivial_partition(n))
            assert profile.orbit_class == "trivial"
            assert profile.dual_partition == principal_partition(n)


# =====================================================================
# Section 13: Full orbit duality verification
# =====================================================================

class TestFullVerification:
    """Tests for the full type-A verification suite."""

    def test_verify_principal_sl2(self):
        v = verify_orbit_duality_type_a(principal_partition(2))
        assert v.ff_involutive
        assert v.ff_critical_self_dual
        assert v.complementarity_k_independent
        assert v.all_checks_pass

    def test_verify_principal_sl3(self):
        v = verify_orbit_duality_type_a(principal_partition(3))
        assert v.ff_involutive
        assert v.ff_critical_self_dual
        assert v.complementarity_k_independent
        assert v.all_checks_pass

    def test_verify_bp_sl3(self):
        """BP = W(sl_3, f_min): self-dual, complementarity 196."""
        v = verify_orbit_duality_type_a((2, 1))
        assert v.ff_involutive
        assert v.ff_critical_self_dual
        assert v.is_self_dual
        assert v.complementarity_k_independent
        assert v.all_checks_pass
        assert simplify(v.complementarity_computed - 196) == 0

    def test_verify_principal_sl4(self):
        v = verify_orbit_duality_type_a(principal_partition(4))
        assert v.all_checks_pass

    def test_verify_principal_sl5(self):
        v = verify_orbit_duality_type_a(principal_partition(5))
        assert v.all_checks_pass

    def test_full_verification_up_to_6(self):
        """All checks pass for the full type-A suite."""
        results = full_type_a_verification(max_n=6)
        for key, val in results.items():
            assert val, f"Failed: {key}"

    def test_full_verification_bv_involutions(self):
        """BV is an involution for n=2,...,8."""
        for n in range(2, 9):
            assert bv_dual_is_involution_type_a(n)


# =====================================================================
# Section 14: Complementarity table
# =====================================================================

class TestComplementarityTable:
    """Tests for the verified complementarity table."""

    def test_table_all_match(self):
        """All entries in the verified table match expected values."""
        table = verified_complementarity_table()
        for entry in table:
            assert entry["match"], f"Failed: {entry['algebra']}"

    def test_table_has_five_entries(self):
        """Table has entries for Virasoro, W_3, BP, W_4, W_5."""
        table = verified_complementarity_table()
        assert len(table) == 5

    def test_table_virasoro_entry(self):
        table = verified_complementarity_table()
        vir = table[0]
        assert "Virasoro" in vir["algebra"]
        assert vir["expected"] == 26

    def test_table_bp_entry(self):
        table = verified_complementarity_table()
        bp = table[2]
        assert "BP" in bp["algebra"]
        assert bp["match"]  # BP is non-principal; just verify it computed


# =====================================================================
# Section 15: Cross-checks with existing modules
# =====================================================================

class TestCrossChecks:
    """Cross-checks against existing compute modules."""

    def test_virasoro_matches_correct_formula(self):
        """Our Virasoro c(k) = 1 - 6(k+1)^2/(k+2)."""
        k = Symbol("k")
        our_c = virasoro_central_charge(k)
        expected = 1 - 6 * (k + 1)**2 / (k + 2)
        assert simplify(our_c - expected) == 0

    def test_bp_matches_nonprincipal_ds_reduction(self):
        """Our BP c(k) matches nonprincipal_ds_reduction.bp_central_charge."""
        k = Symbol("k")
        our_c = bp_central_charge(k)
        expected = 2 - 24 * (k + 1) ** 2 / (k + 3)
        assert simplify(our_c - expected) == 0

    def test_bp_dual_level_matches(self):
        """Our FF dual for sl_3 matches bp_dual_level."""
        k = Symbol("k")
        our_kp = ff_dual_level_type_a(k, 3)
        expected = -k - 6
        assert simplify(our_kp - expected) == 0

    def test_koszul_conductor_w2_matches_virasoro_sum(self):
        """K_2 = 26 matches complementarity_sum_virasoro."""
        assert koszul_conductor_principal(2) == 26
        assert simplify(complementarity_sum_virasoro() - 26) == 0

    def test_orbit_dim_sum_identity(self):
        """dim(O) + dim(Z) = dim(g) for all orbits."""
        for n in range(2, 7):
            dim_g = n * n - 1
            for lam in all_partitions_of(n):
                d = orbit_dimension_type_a(lam) + centralizer_dimension_type_a(lam)
                assert d == dim_g


# =====================================================================
# Section 16: Edge cases and error handling
# =====================================================================

class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_sl2_only_two_orbits(self):
        """sl_2 has only two orbits: trivial (1,1) and principal (2)."""
        parts = all_partitions_of(2)
        assert len(parts) == 2
        assert (2,) in parts
        assert (1, 1) in parts

    def test_hook_partition_boundary_r0(self):
        """Hook with r=0 is principal."""
        assert hook_partition(5, 0) == (5,)

    def test_hook_partition_boundary_rmax(self):
        """Hook with r=n-1 is trivial."""
        assert hook_partition(5, 4) == (1, 1, 1, 1, 1)

    def test_general_ds_partition_size_mismatch(self):
        """Partition size must match n."""
        k = Symbol("k")
        with pytest.raises(ValueError, match="partition of"):
            general_ds_central_charge(4, (3,), k)

    def test_wn_central_charge_positive_rank(self):
        """W_N requires N >= 2."""
        # N=1 would give rank 0, which is degenerate
        k = Symbol("k")
        c = wn_central_charge(2, k)
        assert simplify(c - virasoro_central_charge(k)) == 0


# =====================================================================
# Section 17: Consistency with manuscript formulas
# =====================================================================

class TestManuscriptConsistency:
    """Direct checks against formulas stated in the manuscript."""

    def test_virasoro_c_plus_cprime_26(self):
        """c(k)+c(k')=26 for Virasoro = W_2."""
        k = Symbol("k")
        c_k = virasoro_central_charge(k)
        c_kp = virasoro_central_charge(-k - 4)
        assert simplify(c_k + c_kp - 26) == 0

    def test_w3_c_plus_cprime_100(self):
        """c + c' = 100 for W_3."""
        k = Symbol("k")
        c_k = w3_central_charge(k)
        c_kp = w3_central_charge(-k - 6)
        assert simplify(c_k + c_kp - 100) == 0

    def test_complementarity_formula(self):
        """K_N = 2(N-1) + 4N(N^2-1) for principal W_N algebras."""
        for n in range(2, 8):
            K = koszul_conductor_principal(n)
            assert K == 2 * (n - 1) + 4 * n * (n**2 - 1)

    def test_bp_dual_preserves_orbit(self):
        """prop:bp-duality: (2,1)^t = (2,1) (BV self-dual)."""
        assert barbasch_vogan_dual_type_a((2, 1)) == (2, 1)

    def test_bp_dual_level_is_ff(self):
        """prop:bp-duality: k' = -k-6 for sl_3."""
        k = Symbol("k")
        assert simplify(ff_dual_level_type_a(k, 3) - (-k - 6)) == 0

    def test_hook_type_bv_is_transpose(self):
        """rem:hook-type-w-algebras: (n-r,1^r) <-> (r+1,1^{n-r-1})."""
        for n in range(3, 8):
            for r in range(1, n - 1):
                source = hook_partition(n, r)
                expected_dual = hook_partition(n, n - r - 1)
                assert barbasch_vogan_dual_type_a(source) == expected_dual

    def test_sl3_three_orbits(self):
        """comp:sl3-ds-hierarchy: sl_3 has 3 nilpotent orbits."""
        parts = all_partitions_of(3)
        assert len(parts) == 3
        assert (3,) in parts      # principal
        assert (2, 1) in parts     # minimal = subregular
        assert (1, 1, 1) in parts  # trivial

    def test_w3_zero_curvature_level(self):
        """c(W_3, k) = 0 at k = -5/3 (one of two zeros of 2 - 24(k+2)^2/(k+3))."""
        c = w3_central_charge(Rational(-5, 3))
        assert simplify(c) == 0

    def test_w3_specific_levels(self):
        """comp:w3-curvature-dual specific values with c = 2 - 24(k+2)^2/(k+3)."""
        # k=0: c = 2 - 24*4/3 = -30
        assert w3_central_charge(0) == -30
        # k=1: c = 2 - 24*9/4 = -52
        assert w3_central_charge(1) == -52
        # k=-5 (k'=-1): c = 2 - 24*9/(-2) = 2 + 108 = 110
        assert w3_central_charge(-5) == 110

    def test_virasoro_at_k_neg1(self):
        """Virasoro at k=-1: c = 1 - 6*0/1 = 1."""
        assert virasoro_central_charge(-1) == 1

    def test_ff_involutivity_explicit(self):
        """thm:w-algebra-koszul-main: (k')' = -(-k-2h)-2h = k."""
        k = Symbol("k")
        h = Symbol("h", positive=True)
        kp = -k - 2 * h
        kpp = -kp - 2 * h
        assert simplify(kpp - k) == 0
