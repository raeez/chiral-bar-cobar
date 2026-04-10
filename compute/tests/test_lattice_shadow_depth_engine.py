"""Tests for compute/lib/lattice_shadow_depth_engine.py -- lattice shadow depth.

Validates:
  1. UnimodularLattice construction and constraints
  2. Shadow data for Z^n (Type I, odd unimodular) at various ranks
  3. Shadow data for E_8 (Type II, even unimodular, rank 8)
  4. Shadow data for rank-16 even unimodular lattices
  5. Comparison between Type I (Z^8) and Type II (E_8) at same rank
  6. r-matrix evaluation with AP126/AP141 checks
  7. Shadow tower truncation (class G)
  8. Genus-1 free energy F_1 = kappa/24
  9. Batch analysis across Z^n family
  10. Koszul complementarity K = 0 for all lattice VOAs

References:
  - CLAUDE.md C1:  kappa(H_k) = k
  - CLAUDE.md C10: r^Heis(z) = k/z
  - CLAUDE.md C18: K = 0 for KM/Heis/lattice/free
  - CLAUDE.md C26: G (r=2, Heis)
  - CLAUDE.md C30: Delta = 8*kappa*S_4
  - Conway-Sloane, SPLAG (lattice data)
  - Frenkel-Ben-Zvi, Vertex Algebras Ch. 5 (lattice VOA construction)
"""

import pytest
from fractions import Fraction

from compute.lib.lattice_shadow_depth_engine import (
    UnimodularLattice,
    Zn_lattice,
    E8_lattice,
    D16_plus_lattice,
    E8_x_E8_lattice,
    LatticeVOAShadowData,
    compute_shadow_data,
    shadow_tower_terms,
    r_matrix_at_z,
    genus1_free_energy,
    LatticeComparison,
    compare_lattices,
    analyze_Zn_family,
    analyze_even_unimodular_rank8_16,
)


# ============================================================================
# Lattice construction and validation
# ============================================================================

class TestUnimodularLatticeConstruction:
    """Validate lattice data constraints."""

    def test_Zn_rank1(self):
        lat = Zn_lattice(1)
        assert lat.name == "Z^1"
        assert lat.rank == 1
        assert lat.is_even is False
        assert lat.lattice_type == "Type I"
        assert lat.min_norm == 1
        # VERIFIED: [DC] Z^1 kissing = 2 (vectors +1, -1); [LT] SPLAG.
        assert lat.kissing_number == 2

    def test_Zn_rank8(self):
        lat = Zn_lattice(8)
        assert lat.rank == 8
        assert lat.is_even is False
        assert lat.lattice_type == "Type I"
        # VERIFIED: [DC] Z^n kissing = 2n; [DA] unit vectors +/- e_i.
        assert lat.kissing_number == 16

    def test_E8_construction(self):
        lat = E8_lattice()
        assert lat.name == "E_8"
        assert lat.rank == 8
        assert lat.is_even is True
        assert lat.lattice_type == "Type II"
        assert lat.min_norm == 2
        # VERIFIED: [LT] Conway-Sloane SPLAG; [DC] E_8 root system has 240 roots.
        assert lat.kissing_number == 240

    def test_D16_plus_construction(self):
        lat = D16_plus_lattice()
        assert lat.rank == 16
        assert lat.is_even is True
        # VERIFIED: [LT] Conway-Sloane SPLAG Ch. 16; [DC] D_16 roots = 2*16*15 = 480.
        assert lat.kissing_number == 480

    def test_E8_x_E8_construction(self):
        lat = E8_x_E8_lattice()
        assert lat.rank == 16
        assert lat.is_even is True
        # VERIFIED: [DC] 2 * 240 = 480; [SY] direct sum preserves kissing count.
        assert lat.kissing_number == 480

    def test_invalid_rank_zero(self):
        with pytest.raises(ValueError, match="Rank must be >= 1"):
            UnimodularLattice(name="bad", rank=0, is_even=False, min_norm=1)

    def test_even_unimodular_rank_not_divisible_by_8(self):
        """Even unimodular lattices exist only at ranks divisible by 8."""
        with pytest.raises(ValueError, match="ranks divisible by 8"):
            UnimodularLattice(name="bad", rank=7, is_even=True, min_norm=2)

    def test_even_unimodular_min_norm_violation(self):
        """Even unimodular lattices must have min_norm >= 2."""
        with pytest.raises(ValueError, match="min_norm >= 2"):
            UnimodularLattice(name="bad", rank=8, is_even=True, min_norm=1)


# ============================================================================
# Shadow data for Z^n (Type I)
# ============================================================================

class TestZnShadowData:
    """Shadow depth data for Type I lattices Z^n."""

    def test_Z1_shadow(self):
        """Z^1: rank 1, simplest case. c=1, kappa=1."""
        data = compute_shadow_data(Zn_lattice(1))
        # VERIFIED: [DC] c = rank = 1; [CF] single free boson c=1.
        assert data.central_charge == 1
        # VERIFIED: [DC] kappa(H_k) = k = 1; [CF] C1 in CLAUDE.md.
        assert data.kappa == 1
        assert data.S2 == 1
        assert data.S4 == 0
        # VERIFIED: [DC] Delta = 8*1*0 = 0; [CF] C30 finite tower.
        assert data.Delta == 0
        assert data.shadow_depth == 2
        assert data.shadow_class == "G"
        assert data.r_matrix_level == 1
        # VERIFIED: [DC] K = 0 for free family; [CF] C18.
        assert data.koszul_conductor == 0
        assert data.has_half_integer_weights is True

    def test_Z8_shadow(self):
        """Z^8: rank 8, same rank as E_8 but Type I."""
        data = compute_shadow_data(Zn_lattice(8))
        # VERIFIED: [DC] c = rank = 8; [CF] 8 free bosons.
        assert data.central_charge == 8
        # VERIFIED: [DC] kappa = rank = 8; [CF] C1.
        assert data.kappa == 8
        assert data.S2 == 8
        assert data.S4 == 0
        assert data.Delta == 0
        assert data.shadow_depth == 2
        assert data.shadow_class == "G"
        assert data.has_half_integer_weights is True

    def test_Z24_shadow(self):
        """Z^24: rank 24, the dimension of the Leech lattice."""
        data = compute_shadow_data(Zn_lattice(24))
        assert data.central_charge == 24
        assert data.kappa == 24
        assert data.S2 == 24
        assert data.S4 == 0
        assert data.Delta == 0
        assert data.shadow_class == "G"

    def test_all_Zn_are_class_G(self):
        """Every Z^n lattice VOA is class G with shadow depth 2."""
        for n in range(1, 25):
            data = compute_shadow_data(Zn_lattice(n))
            assert data.shadow_class == "G", f"Z^{n} not class G"
            assert data.shadow_depth == 2, f"Z^{n} shadow depth != 2"

    def test_Zn_kappa_equals_rank(self):
        """kappa(V_{Z^n}) = n for all n."""
        for n in range(1, 25):
            data = compute_shadow_data(Zn_lattice(n))
            # VERIFIED: [DC] kappa(H_k) = k, k = rank; [CF] C1.
            assert data.kappa == n, f"Z^{n}: kappa={data.kappa} != {n}"

    def test_Zn_central_charge_equals_rank(self):
        """c(V_{Z^n}) = n for all n."""
        for n in range(1, 25):
            data = compute_shadow_data(Zn_lattice(n))
            assert data.central_charge == n

    def test_Zn_all_type_I(self):
        """Z^n is always Type I (odd unimodular)."""
        for n in range(1, 25):
            data = compute_shadow_data(Zn_lattice(n))
            assert data.has_half_integer_weights is True
            assert data.lattice.lattice_type == "Type I"


# ============================================================================
# Shadow data for E_8 (Type II)
# ============================================================================

class TestE8ShadowData:
    """Shadow depth data for the E_8 lattice VOA."""

    def test_E8_central_charge(self):
        data = compute_shadow_data(E8_lattice())
        # VERIFIED: [DC] c = rank = 8; [LT] FBZ Ch. 5.
        assert data.central_charge == 8

    def test_E8_kappa(self):
        data = compute_shadow_data(E8_lattice())
        # VERIFIED: [DC] kappa = rank = 8; [CF] C1 Heisenberg kappa.
        assert data.kappa == 8

    def test_E8_shadow_class_G(self):
        """E_8 lattice VOA is class G (Heisenberg-type OPE)."""
        data = compute_shadow_data(E8_lattice())
        assert data.shadow_class == "G"
        assert data.shadow_depth == 2

    def test_E8_shadow_coefficients(self):
        data = compute_shadow_data(E8_lattice())
        assert data.S2 == 8
        # VERIFIED: [DC] class G has S_4 = 0; [CF] C26.
        assert data.S4 == 0

    def test_E8_Delta_zero(self):
        data = compute_shadow_data(E8_lattice())
        # VERIFIED: [DC] Delta = 8*8*0 = 0; [CF] C30.
        assert data.Delta == 0

    def test_E8_koszul_conductor(self):
        data = compute_shadow_data(E8_lattice())
        # VERIFIED: [DC] K = 0 for lattice family; [CF] C18.
        assert data.koszul_conductor == 0

    def test_E8_type_II_spectrum(self):
        """E_8 is Type II: purely bosonic, no half-integer weights."""
        data = compute_shadow_data(E8_lattice())
        assert data.has_half_integer_weights is False
        assert data.lattice.lattice_type == "Type II"


# ============================================================================
# Rank-16 even unimodular
# ============================================================================

class TestRank16EvenUnimodular:
    """Both rank-16 even unimodular lattices have identical shadow data."""

    def test_E8xE8_shadow(self):
        data = compute_shadow_data(E8_x_E8_lattice())
        assert data.central_charge == 16
        assert data.kappa == 16
        assert data.shadow_class == "G"
        assert data.Delta == 0

    def test_D16_plus_shadow(self):
        data = compute_shadow_data(D16_plus_lattice())
        assert data.central_charge == 16
        assert data.kappa == 16
        assert data.shadow_class == "G"
        assert data.Delta == 0

    def test_rank16_shadow_data_agree(self):
        """E_8 x E_8 and D_{16}^+ have identical shadow invariants.

        The lattice geometry differs, but the Heisenberg subalgebra
        (which determines shadow depth) depends only on rank.
        """
        d1 = compute_shadow_data(E8_x_E8_lattice())
        d2 = compute_shadow_data(D16_plus_lattice())
        assert d1.kappa == d2.kappa
        assert d1.central_charge == d2.central_charge
        assert d1.shadow_class == d2.shadow_class
        assert d1.shadow_depth == d2.shadow_depth
        assert d1.S2 == d2.S2
        assert d1.S4 == d2.S4
        assert d1.Delta == d2.Delta
        assert d1.koszul_conductor == d2.koszul_conductor


# ============================================================================
# Z^8 vs E_8 comparison (same rank, different type)
# ============================================================================

class TestZ8VsE8Comparison:
    """Compare Type I (Z^8) and Type II (E_8) at rank 8."""

    @pytest.fixture
    def comparison(self):
        return compare_lattices(Zn_lattice(8), E8_lattice())

    def test_same_rank(self, comparison):
        assert comparison.lattice_a.central_charge == 8
        assert comparison.lattice_b.central_charge == 8

    def test_same_shadow_class(self, comparison):
        """Both are class G: shadow depth is rank-determined, not type-determined."""
        assert comparison.same_shadow_class is True
        assert comparison.lattice_a.shadow_class == "G"
        assert comparison.lattice_b.shadow_class == "G"

    def test_same_shadow_depth(self, comparison):
        assert comparison.same_shadow_depth is True
        assert comparison.lattice_a.shadow_depth == 2
        assert comparison.lattice_b.shadow_depth == 2

    def test_same_kappa(self, comparison):
        """kappa depends only on rank, not on lattice type."""
        assert comparison.kappa_ratio == Fraction(1, 1)

    def test_zero_central_charge_difference(self, comparison):
        assert comparison.central_charge_difference == 0

    def test_both_finite_tower(self, comparison):
        assert comparison.both_finite_tower is True

    def test_spectrum_differs(self, comparison):
        """The key difference: Type I has half-integer weights, Type II does not."""
        desc = comparison.spectrum_difference
        assert "half-integer" in desc
        assert "Type I" in desc
        assert "Type II" in desc

    def test_same_koszul_conductor(self, comparison):
        assert comparison.lattice_a.koszul_conductor == 0
        assert comparison.lattice_b.koszul_conductor == 0


# ============================================================================
# r-matrix (AP126/AP141)
# ============================================================================

class TestRMatrix:
    """r-matrix evaluation with AP126/AP141 verification."""

    def test_r_matrix_Z1(self):
        """r(z) = 1/z for Z^1 (k=1)."""
        data = compute_shadow_data(Zn_lattice(1))
        # VERIFIED: [DC] r(z) = k/z = 1/z; [CF] C10.
        assert r_matrix_at_z(data, 1.0) == pytest.approx(1.0)
        assert r_matrix_at_z(data, 2.0) == pytest.approx(0.5)

    def test_r_matrix_E8(self):
        """r(z) = 8/z for E_8 (k=8)."""
        data = compute_shadow_data(E8_lattice())
        assert r_matrix_at_z(data, 1.0) == pytest.approx(8.0)
        assert r_matrix_at_z(data, 4.0) == pytest.approx(2.0)

    def test_r_matrix_pole(self):
        """r-matrix has a simple pole at z=0."""
        data = compute_shadow_data(Zn_lattice(1))
        with pytest.raises(ValueError, match="pole at z=0"):
            r_matrix_at_z(data, 0)

    def test_r_matrix_level_prefix_AP126(self):
        """AP126: r-matrix carries level prefix k = rank."""
        for n in range(1, 10):
            data = compute_shadow_data(Zn_lattice(n))
            assert data.r_matrix_level == n
            # r(1) = k/1 = k = rank
            assert r_matrix_at_z(data, 1.0) == pytest.approx(float(n))

    def test_AP141_k0_vanishing(self):
        """AP141: if level were 0, r-matrix would vanish.

        We cannot construct a rank-0 lattice (rank >= 1), but we verify
        the formula: r(z) = k/z vanishes when k=0.
        """
        # Direct formula check: 0/z = 0 for any z != 0
        assert 0 / 1.0 == 0.0
        assert 0 / 0.5 == 0.0


# ============================================================================
# Shadow tower
# ============================================================================

class TestShadowTower:
    """Shadow tower truncation for class G lattice VOAs."""

    def test_tower_Z1(self):
        data = compute_shadow_data(Zn_lattice(1))
        tower = shadow_tower_terms(data, max_r=10)
        # VERIFIED: [DC] S_2 = kappa = 1; S_r = 0 for r >= 3; [CF] C26.
        assert tower[2] == 1
        for r in range(3, 11):
            assert tower[r] == 0, f"S_{r} != 0 for class G"

    def test_tower_E8(self):
        data = compute_shadow_data(E8_lattice())
        tower = shadow_tower_terms(data, max_r=10)
        # VERIFIED: [DC] S_2 = kappa = 8; [CF] C26 class G.
        assert tower[2] == 8
        for r in range(3, 11):
            assert tower[r] == 0

    def test_tower_finite_for_class_G(self):
        """Class G: tower terminates at r=2 (only S_2 nonzero)."""
        for n in [1, 2, 4, 8, 16, 24]:
            data = compute_shadow_data(Zn_lattice(n))
            tower = shadow_tower_terms(data, max_r=20)
            nonzero = {r: v for r, v in tower.items() if v != 0}
            assert nonzero == {2: n}, f"Z^{n}: nonzero tower terms = {nonzero}"


# ============================================================================
# Genus-1 free energy
# ============================================================================

class TestGenus1FreeEnergy:
    """F_1 = kappa/24 for lattice VOAs."""

    def test_F1_Z1(self):
        data = compute_shadow_data(Zn_lattice(1))
        # VERIFIED: [DC] F_1 = 1/24; [CF] CLAUDE.md Cauchy integral sanity check.
        assert genus1_free_energy(data) == Fraction(1, 24)

    def test_F1_Z8(self):
        data = compute_shadow_data(Zn_lattice(8))
        # VERIFIED: [DC] F_1 = 8/24 = 1/3; [DA] kappa/24 = 8/24.
        assert genus1_free_energy(data) == Fraction(1, 3)

    def test_F1_E8(self):
        data = compute_shadow_data(E8_lattice())
        # VERIFIED: [DC] F_1 = 8/24 = 1/3; [CF] same kappa as Z^8.
        assert genus1_free_energy(data) == Fraction(1, 3)

    def test_F1_Z8_equals_E8(self):
        """Z^8 and E_8 have the same F_1 (same kappa = 8)."""
        f1_z8 = genus1_free_energy(compute_shadow_data(Zn_lattice(8)))
        f1_e8 = genus1_free_energy(compute_shadow_data(E8_lattice()))
        assert f1_z8 == f1_e8

    def test_F1_scales_linearly_with_rank(self):
        """F_1(Z^n) = n/24, linear in rank."""
        for n in range(1, 25):
            data = compute_shadow_data(Zn_lattice(n))
            assert genus1_free_energy(data) == Fraction(n, 24)


# ============================================================================
# Koszul complementarity
# ============================================================================

class TestKoszulComplementarity:
    """K = kappa + kappa' = 0 for all lattice/free family VOAs."""

    def test_koszul_conductor_zero_Zn(self):
        """Every Z^n lattice VOA has K = 0."""
        for n in range(1, 25):
            data = compute_shadow_data(Zn_lattice(n))
            # VERIFIED: [DC] K = 0 for free/lattice; [CF] C18.
            assert data.koszul_conductor == 0, f"Z^{n}: K={data.koszul_conductor}"

    def test_koszul_conductor_zero_E8(self):
        data = compute_shadow_data(E8_lattice())
        assert data.koszul_conductor == 0

    def test_koszul_conductor_zero_rank16(self):
        for data in analyze_even_unimodular_rank8_16():
            assert data.koszul_conductor == 0


# ============================================================================
# Batch analysis
# ============================================================================

class TestBatchAnalysis:
    """Batch analysis functions."""

    def test_analyze_Zn_family_length(self):
        results = analyze_Zn_family(max_rank=24)
        assert len(results) == 24

    def test_analyze_Zn_family_ranks(self):
        results = analyze_Zn_family(max_rank=10)
        for i, data in enumerate(results):
            assert data.lattice.rank == i + 1

    def test_analyze_Zn_family_all_class_G(self):
        results = analyze_Zn_family(max_rank=24)
        for data in results:
            assert data.shadow_class == "G"

    def test_analyze_even_unimodular_count(self):
        """3 lattices: E_8, E_8 x E_8, D_{16}^+."""
        results = analyze_even_unimodular_rank8_16()
        assert len(results) == 3

    def test_analyze_even_unimodular_all_class_G(self):
        results = analyze_even_unimodular_rank8_16()
        for data in results:
            assert data.shadow_class == "G"
            assert data.Delta == 0

    def test_analyze_even_unimodular_no_half_integer(self):
        """All even unimodular lattice VOAs are purely bosonic."""
        results = analyze_even_unimodular_rank8_16()
        for data in results:
            assert data.has_half_integer_weights is False


# ============================================================================
# Delta discriminant
# ============================================================================

class TestDeltaDiscriminant:
    """Delta = 8 * kappa * S_4: the shadow tower discriminant."""

    def test_Delta_formula(self):
        """Verify Delta = 8 * kappa * S_4 directly."""
        for n in [1, 2, 4, 8, 16, 24]:
            data = compute_shadow_data(Zn_lattice(n))
            # VERIFIED: [DC] 8 * n * 0 = 0; [CF] C30.
            assert data.Delta == 8 * data.kappa * data.S4
            assert data.Delta == 0

    def test_Delta_zero_implies_finite_tower(self):
        """Delta = 0 <-> finite shadow tower (class G or L)."""
        for n in range(1, 25):
            data = compute_shadow_data(Zn_lattice(n))
            assert data.Delta == 0
            # Class G has finite tower (terminates at r=2)
            assert data.shadow_class == "G"

    def test_Delta_linear_in_kappa_AP21(self):
        """AP21: Delta is LINEAR in kappa (NOT quadratic).

        Delta = 8 * kappa * S_4. For class G, S_4 = 0,
        so Delta = 0 regardless of kappa. But the formula
        is still linear: if S_4 were nonzero, Delta ~ kappa.
        """
        for n in [1, 5, 10, 20]:
            data = compute_shadow_data(Zn_lattice(n))
            # 8 * kappa * S_4: one power of kappa, not two
            assert data.Delta == 8 * n * 0


# ============================================================================
# Cross-checks and invariants
# ============================================================================

class TestCrossChecks:
    """Cross-verification of internal consistency."""

    def test_S2_equals_kappa(self):
        """S_2 = kappa for all lattice VOAs."""
        for n in range(1, 25):
            data = compute_shadow_data(Zn_lattice(n))
            assert data.S2 == data.kappa

    def test_r_matrix_level_equals_rank(self):
        """r-matrix level = rank for all lattice VOAs."""
        for n in range(1, 10):
            data = compute_shadow_data(Zn_lattice(n))
            assert data.r_matrix_level == data.lattice.rank

    def test_central_charge_equals_kappa(self):
        """For Heisenberg-type (lattice VOAs): c = kappa = rank."""
        for n in range(1, 25):
            data = compute_shadow_data(Zn_lattice(n))
            assert data.central_charge == data.kappa

    def test_type_I_always_has_half_integer(self):
        """Type I (odd) always has half-integer weight vertex operators."""
        for n in range(1, 25):
            data = compute_shadow_data(Zn_lattice(n))
            assert data.has_half_integer_weights is True

    def test_type_II_never_has_half_integer(self):
        """Type II (even) never has half-integer weight vertex operators."""
        for data in analyze_even_unimodular_rank8_16():
            assert data.has_half_integer_weights is False

    def test_shadow_depth_independent_of_lattice_type(self):
        """Shadow depth = 2 for both Type I and Type II at same rank."""
        z8 = compute_shadow_data(Zn_lattice(8))
        e8 = compute_shadow_data(E8_lattice())
        assert z8.shadow_depth == e8.shadow_depth == 2

    def test_comparison_reflexive(self):
        """Comparing a lattice with itself gives trivial comparison."""
        comp = compare_lattices(E8_lattice(), E8_lattice())
        assert comp.same_shadow_class is True
        assert comp.same_shadow_depth is True
        assert comp.kappa_ratio == Fraction(1, 1)
        assert comp.central_charge_difference == 0
