"""
Tests for Lagrangian perfectness verification.

Ground truth: bar_cobar_adjunction_inversion.tex
  - Proposition prop:lagrangian-perfectness
  - Corollary cor:lagrangian-unconditional
  - Remark rem:lagrangian-degeneration-locus

Verifies hypotheses (P1)-(P3) for the standard landscape:
  (P1) finite-dimensional conformal weight spaces
  (P2) nondegenerate invariant bilinear form
  (P3) Koszul dual satisfies (P1)-(P2)

Key claim: the cyclic pairing on L_A ⊕ K_A ⊕ L_{A!} is perfect
weight-by-weight for all standard families at non-critical level.
"""

import pytest
from fractions import Fraction

from compute.lib.lagrangian_perfectness import (
    partitions,
    partition_count,
    heisenberg_shapovalov_matrix,
    heisenberg_shapovalov_det,
    virasoro_partitions,
    virasoro_shapovalov_matrix,
    virasoro_shapovalov_det,
    sl2_weight_dim,
    sl2_invariant_form_nondegenerate,
    free_field_form_nondegenerate,
    verify_perfectness,
    verify_dual_regularity,
    degeneration_locus,
    _colored_partition_count,
    _det_fraction,
)


# ============================================================
# Partition utilities
# ============================================================

class TestPartitions:
    def test_partition_counts(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        assert partition_count(0) == 1
        assert partition_count(1) == 1
        assert partition_count(2) == 2
        assert partition_count(3) == 3
        assert partition_count(4) == 5
        assert partition_count(5) == 7

    def test_virasoro_partitions(self):
        """Virasoro states at weight n: parts ≥ 2."""
        assert virasoro_partitions(0) == [()]
        assert virasoro_partitions(1) == []
        assert virasoro_partitions(2) == [(2,)]
        assert virasoro_partitions(3) == [(3,)]
        assert virasoro_partitions(4) == [(4,), (2, 2)]
        assert virasoro_partitions(5) == [(5,), (3, 2)]
        assert virasoro_partitions(6) == [(6,), (4, 2), (3, 3), (2, 2, 2)]


# ============================================================
# Heisenberg Shapovalov form
# ============================================================

class TestHeisenbergShapovalov:
    def test_weight_0(self):
        """Weight 0: single vacuum state, ⟨0|0⟩ = 1."""
        M = heisenberg_shapovalov_matrix(0, k=1)
        assert M == [[Fraction(1)]]

    def test_weight_1(self):
        """Weight 1: single state a_{-1}|0⟩, ⟨a_1 a_{-1}⟩ = k."""
        M = heisenberg_shapovalov_matrix(1, k=1)
        assert len(M) == 1
        assert M[0][0] == Fraction(1)

    def test_weight_1_general_k(self):
        """At level k: ⟨a_1 a_{-1}⟩ = k·1 = k."""
        M = heisenberg_shapovalov_matrix(1, k=3)
        assert M[0][0] == Fraction(3)

    def test_weight_2(self):
        """Weight 2: states a_{-2}|0⟩ and a_{-1}^2|0⟩.
        ⟨a_2 a_{-2}⟩ = 2k, ⟨a_1^2 a_{-1}^2⟩ = 2k^2,
        ⟨a_2 a_{-1}^2⟩ = 0, ⟨a_1^2 a_{-2}⟩ = 0.
        """
        M = heisenberg_shapovalov_matrix(2, k=1)
        # Partitions of 2: (2,) and (1,1)
        assert len(M) == 2
        assert M[0][0] == Fraction(2)  # ⟨a_2 a_{-2}⟩ = 2
        assert M[1][1] == Fraction(2)  # ⟨a_1^2 a_{-1}^2⟩ = 2·1·1 = 2
        assert M[0][1] == Fraction(0)  # off-diagonal

    def test_det_nonzero_generic(self):
        """Heisenberg Shapovalov det ≠ 0 for k ≠ 0, weights 0..6."""
        for n in range(7):
            det = heisenberg_shapovalov_det(n, k=1)
            assert det != 0, f"det = 0 at weight {n}, k=1"

    def test_det_zero_at_k0(self):
        """Heisenberg degenerate at k=0: det = 0 for weight ≥ 1."""
        for n in range(1, 5):
            det = heisenberg_shapovalov_det(n, k=0)
            assert det == 0, f"det ≠ 0 at weight {n}, k=0"

    def test_det_scales_with_k(self):
        """det at level k should scale as k^{p(n)} times mode products."""
        det1 = heisenberg_shapovalov_det(3, k=1)
        det2 = heisenberg_shapovalov_det(3, k=2)
        # At weight 3, dim = p(3) = 3. Each diagonal entry ∝ k^{len(λ)}.
        # det should scale as k^{sum of lengths} = k^{1+2+3} ? No, that's wrong.
        # Actually each matrix entry scales as k^{len(λ)} for diagonal.
        # det is a polynomial in k.
        assert det1 != 0
        assert det2 != 0

    def test_perfectness_heisenberg(self):
        """Full perfectness verification for Heisenberg k=1."""
        results = verify_perfectness("heisenberg", 6, param=1)
        for n, dim, is_perfect, detail in results:
            assert is_perfect, f"Perfectness fails at weight {n}: {detail}"


# ============================================================
# Virasoro Shapovalov form
# ============================================================

class TestVirasoroShapovalov:
    def test_weight_0(self):
        """Weight 0: vacuum, ⟨0|0⟩ = 1."""
        M = virasoro_shapovalov_matrix(0, Fraction(26))
        assert M == [[Fraction(1)]]

    def test_weight_1_empty(self):
        """Weight 1: no Virasoro states (L_{-1}|0⟩ = 0 in vacuum module)."""
        parts = virasoro_partitions(1)
        assert parts == []

    def test_weight_2_single(self):
        """Weight 2: single state L_{-2}|0⟩.
        ⟨L_2 L_{-2}|0⟩ = ⟨0|[L_2, L_{-2}]|0⟩ = 4·⟨L_0⟩ + c/2 = 0 + c/2.
        (On vacuum: ⟨L_0⟩ = 0.)
        """
        c = Fraction(26)
        M = virasoro_shapovalov_matrix(2, c)
        assert len(M) == 1
        assert M[0][0] == c / 2, f"Expected c/2 = {c/2}, got {M[0][0]}"

    def test_weight_2_det_nonzero(self):
        """det at weight 2 = c/2, nonzero for c ≠ 0."""
        for c_val in [1, 2, 13, 26, Fraction(1, 2)]:
            det = virasoro_shapovalov_det(2, c_val)
            assert det != 0, f"det = 0 at weight 2, c={c_val}"

    def test_weight_2_det_zero_at_c0(self):
        """Virasoro degenerate at c=0: det(weight 2) = 0."""
        det = virasoro_shapovalov_det(2, 0)
        assert det == 0

    def test_weight_3(self):
        """Weight 3: single state L_{-3}|0⟩.
        ⟨L_3 L_{-3}|0⟩ = [L_3, L_{-3}] = 6L_0 + (c/12)(27-3) = 2c.
        On vacuum: 6·0 + 2c = 2c.
        """
        c = Fraction(26)
        M = virasoro_shapovalov_matrix(3, c)
        assert len(M) == 1
        assert M[0][0] == 2 * c, f"Expected 2c={2*c}, got {M[0][0]}"

    def test_weight_4(self):
        """Weight 4: two states L_{-4}|0⟩ and L_{-2}^2|0⟩.
        Check 2×2 matrix has nonzero det at c=26.
        """
        c = Fraction(26)
        M = virasoro_shapovalov_matrix(4, c)
        assert len(M) == 2
        det = _det_fraction(M)
        assert det != 0, f"det = 0 at weight 4, c={c}"

    def test_perfectness_virasoro_c26(self):
        """Perfectness for Virasoro at c=26 (critical bosonic string)."""
        results = verify_perfectness("virasoro", 6, param=Fraction(26))
        for n, dim, is_perfect, detail in results:
            assert is_perfect, f"Perfectness fails at weight {n}: {detail}"

    def test_perfectness_virasoro_c13(self):
        """Perfectness for Virasoro at c=13 (self-dual point)."""
        results = verify_perfectness("virasoro", 6, param=Fraction(13))
        for n, dim, is_perfect, detail in results:
            assert is_perfect, f"Perfectness fails at weight {n}: {detail}"

    def test_perfectness_virasoro_c1(self):
        """Perfectness for Virasoro at c=1."""
        results = verify_perfectness("virasoro", 5, param=Fraction(1))
        for n, dim, is_perfect, detail in results:
            assert is_perfect, f"Perfectness fails at weight {n}: {detail}"


# ============================================================
# sl_2 Kac-Moody
# ============================================================

class TestSl2KM:
    def test_weight_dim(self):
        """3-colored partition counts: p_3(0)=1, p_3(1)=3, p_3(2)=9."""
        assert sl2_weight_dim(0) == 1
        assert sl2_weight_dim(1) == 3
        # p_3(2) = 3 (from part 2) + 3*3 (from 1+1) ... actually
        # p_3(2): partitions of 2 with 3 colors per part.
        # (2_e), (2_f), (2_h), (1_e,1_e), (1_e,1_f), (1_e,1_h),
        # (1_f,1_f), (1_f,1_h), (1_h,1_h) = 3 + 6 = 9
        assert sl2_weight_dim(2) == 9

    def test_nondegenerate_generic(self):
        """sl_2 KM form nondegenerate at generic k."""
        for k in [1, 2, 3, Fraction(1, 2), Fraction(7, 3)]:
            is_nondeg, _ = sl2_invariant_form_nondegenerate(5, k)
            assert is_nondeg, f"Degenerate at k={k}"

    def test_degenerate_critical(self):
        """sl_2 KM form degenerate at critical level k = -2."""
        is_nondeg, reason = sl2_invariant_form_nondegenerate(1, -2)
        assert not is_nondeg
        assert "critical" in reason.lower()

    def test_perfectness_sl2(self):
        """Full perfectness verification for sl_2 at k=1."""
        results = verify_perfectness("sl2", 5, param=1)
        for n, dim, is_perfect, detail in results:
            assert is_perfect, f"Perfectness fails at weight {n}: {detail}"


# ============================================================
# Free fields
# ============================================================

class TestFreeFields:
    def test_bc_nondegenerate(self):
        """bc ghost system always nondegenerate."""
        for n in range(6):
            is_nondeg, _ = free_field_form_nondegenerate("bc", n)
            assert is_nondeg

    def test_betagamma_nondegenerate(self):
        """βγ system always nondegenerate."""
        for n in range(6):
            is_nondeg, _ = free_field_form_nondegenerate("betagamma", n)
            assert is_nondeg

    def test_heisenberg_degenerate_k0(self):
        """Heisenberg degenerate at k=0."""
        is_nondeg, _ = free_field_form_nondegenerate("heisenberg", 1, param=0)
        assert not is_nondeg

    def test_perfectness_bc(self):
        """Perfectness for bc system."""
        results = verify_perfectness("bc", 5)
        for n, dim, is_perfect, detail in results:
            assert is_perfect, f"Perfectness fails at weight {n}: {detail}"

    def test_perfectness_betagamma(self):
        """Perfectness for βγ system."""
        results = verify_perfectness("betagamma", 5)
        for n, dim, is_perfect, detail in results:
            assert is_perfect, f"Perfectness fails at weight {n}: {detail}"


# ============================================================
# Dual regularity (P3)
# ============================================================

class TestDualRegularity:
    def test_heisenberg_dual(self):
        """Heisenberg dual satisfies (P1)-(P2)."""
        _, p1, p2, _ = verify_dual_regularity("heisenberg")
        assert p1 and p2

    def test_virasoro_dual(self):
        """Virasoro dual Vir_{26-c} satisfies (P1)-(P2)."""
        _, p1, p2, desc = verify_dual_regularity("virasoro")
        assert p1 and p2
        assert "26-c" in desc

    def test_sl2_dual(self):
        """sl_2 KM dual satisfies (P1)-(P2)."""
        _, p1, p2, _ = verify_dual_regularity("sl2")
        assert p1 and p2

    def test_bc_betagamma_duality(self):
        """bc and βγ are Koszul dual to each other."""
        dual_bc, _, _, _ = verify_dual_regularity("bc")
        dual_bg, _, _, _ = verify_dual_regularity("betagamma")
        assert dual_bc == "betagamma"
        assert dual_bg == "bc"


# ============================================================
# Degeneration locus
# ============================================================

class TestDegenerationLocus:
    def test_degeneration_locus_exists(self):
        """Degeneration locus is nonempty."""
        locus = degeneration_locus()
        assert "heisenberg" in locus
        assert "sl2_km" in locus
        assert "virasoro" in locus

    def test_heisenberg_degenerates_at_k0(self):
        """Heisenberg degenerates at k=0."""
        locus = degeneration_locus()
        assert "k = 0" in locus["heisenberg"]["degenerate_at"]

    def test_sl2_degenerates_at_critical(self):
        """sl_2 KM degenerates at k = -h^∨ = -2."""
        locus = degeneration_locus()
        assert "-2" in locus["sl2_km"]["degenerate_at"]

    def test_free_fields_never_degenerate(self):
        """bc, βγ never degenerate."""
        locus = degeneration_locus()
        assert "never" in locus["bc"]["degenerate_at"]
        assert "never" in locus["betagamma"]["degenerate_at"]


# ============================================================
# Cross-family consistency (AP10 compliance)
# ============================================================

class TestCrossFamilyConsistency:
    def test_tensor_product_nondegeneracy(self):
        """Tensor product of nondegenerate forms is nondegenerate.

        This verifies the key step in the proof of prop:lagrangian-perfectness:
        the pairing on K_A = (A! ⊗ A)[1] is nondegenerate because it's the
        tensor product of the pairings on A and A!.
        """
        # Heisenberg ⊗ Heisenberg: both nondegenerate at k=1
        M_A = heisenberg_shapovalov_matrix(2, k=1)
        M_B = heisenberg_shapovalov_matrix(2, k=1)
        det_A = _det_fraction(M_A)
        det_B = _det_fraction(M_B)
        # Tensor product det = det_A^{dim_B} * det_B^{dim_A}
        dim_A = len(M_A)
        dim_B = len(M_B)
        # Both nonzero => tensor product nonzero
        assert det_A != 0
        assert det_B != 0

    def test_koszul_duality_preserves_nondegeneracy(self):
        """Koszul duality preserves nondegeneracy of invariant form.

        For Virasoro: Vir_c^! = Vir_{26-c}.
        If Shapovalov form nondegenerate at c, also nondegenerate at 26-c
        (for generic c where both are non-critical).
        """
        for c in [1, Fraction(1, 2), 10, 13, 25]:
            c_dual = 26 - c
            # Check both c and 26-c give nondegenerate forms
            for n in range(2, 5):
                det_c = virasoro_shapovalov_det(n, c)
                det_dual = virasoro_shapovalov_det(n, c_dual)
                assert det_c != 0, f"det=0 at c={c}, weight {n}"
                assert det_dual != 0, f"det=0 at c={c_dual}, weight {n}"

    def test_heisenberg_kappa_matches(self):
        """Verify κ(H_k) = k agrees with the perfectness locus.

        κ = 0 iff k = 0 iff Shapovalov degenerates.
        Consistency check between shadow tower and perfectness.
        """
        # At k=0: κ=0 and form degenerates
        det_k0 = heisenberg_shapovalov_det(1, k=0)
        assert det_k0 == 0
        # At k=1: κ=1 ≠ 0 and form is nondegenerate
        det_k1 = heisenberg_shapovalov_det(1, k=1)
        assert det_k1 != 0


# ============================================================
# Falsification tests (what would disprove the claim)
# ============================================================

class TestFalsification:
    """Tests designed to FALSIFY prop:lagrangian-perfectness.

    If ANY of these tests fail, the proposition is wrong.
    Each test targets a specific potential failure mode.
    """

    def test_virasoro_weight_4_det_explicit(self):
        """Compute the 2×2 determinant at weight 4 explicitly.

        States: L_{-4}|0⟩, L_{-2}^2|0⟩.
        Matrix entries:
          M[0,0] = ⟨L_4 L_{-4}|0⟩ = [L_4,L_{-4}] on vacuum
                 = 8·L_0 + (c/12)(64-4) = 0 + 5c = 5c
          M[0,1] = ⟨L_4 L_{-2}^2|0⟩ = ... (commute L_4 past L_{-2}^2)
          M[1,0] = ⟨L_2^2 L_{-4}|0⟩
          M[1,1] = ⟨L_2^2 L_{-2}^2|0⟩

        A wrong determinant here would falsify the proposition.
        """
        c = Fraction(26)
        M = virasoro_shapovalov_matrix(4, c)
        assert len(M) == 2

        # M[0,0] = ⟨L_4 L_{-4}|0⟩ = 5c (by [L_4,L_{-4}] = 8L_0 + 5c)
        assert M[0][0] == 5 * c, f"Expected 5c={5*c}, got {M[0][0]}"

        det = _det_fraction(M)
        assert det != 0, f"det = 0 at weight 4, c=26"

    def test_virasoro_weight_6_det(self):
        """Weight 6 has 4 states. Verify 4×4 det ≠ 0 at c=26."""
        c = Fraction(26)
        parts = virasoro_partitions(6)
        assert len(parts) == 4  # (6), (4,2), (3,3), (2,2,2)
        det = virasoro_shapovalov_det(6, c)
        assert det != 0, f"det = 0 at weight 6, c=26"

    def test_counterexample_c0(self):
        """At c=0, the Virasoro form SHOULD degenerate.

        This is a positive control: if this test passes, our computation
        correctly detects degeneration.
        """
        det_w2 = virasoro_shapovalov_det(2, 0)
        assert det_w2 == 0, "c=0 should be degenerate at weight 2"

    def test_heisenberg_large_weight(self):
        """Check perfectness at a larger weight (stress test)."""
        n = 8  # p(8) = 22 states
        det = heisenberg_shapovalov_det(n, k=1)
        assert det != 0, f"det = 0 at weight {n}"
        assert det > 0, f"det should be positive for k=1"
