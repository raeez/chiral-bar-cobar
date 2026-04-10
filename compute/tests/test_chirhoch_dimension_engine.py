r"""Tests for chirhoch_dimension_engine.py: ChirHoch dimension census.

Verifies dim ChirHoch^n(A) for n in {0, 1, 2} across all standard families.
The key datum is sl_2 total = 5 > 4, which forces correction of Theorem H.

Test categories:
    1. Individual family dimensions (manuscript ground truth)
    2. Concentration in degrees {0, 1, 2} (Theorem H, unconditional)
    3. Old Theorem H bound violations (dim_total <= 4)
    4. Koszul duality consistency (palindromic Poincare polynomial)
    5. Parametric scaling (affine KM: ChirHoch^1 = dim(g))
    6. W_2 = Virasoro consistency
    7. Lie algebra dimension data correctness
    8. Edge cases and error handling

Manuscript references:
    thm:hochschild-polynomial-growth (Theorem H)
    chiral_center_theorem.tex lines 1780-1920 (explicit dimensions)
    chiral_hochschild_koszul.tex lines 4760-4824 (Heisenberg, bc, bg)
"""

import pytest

from compute.lib.chirhoch_dimension_engine import (
    ChirHochData,
    chirhoch_heisenberg,
    chirhoch_affine_km,
    chirhoch_virasoro,
    chirhoch_free_fermion_bc,
    chirhoch_free_betagamma,
    chirhoch_w_algebra,
    chirhoch_lattice,
    chirhoch_dimensions,
    all_standard_families,
    old_theorem_h_bound_holds,
    theorem_h_concentration_holds,
    koszul_duality_check,
    dim_simple_lie_algebra,
    rank_simple_lie_algebra,
    generate_summary_table,
    LIE_ALGEBRA_DIMS,
    DUAL_COXETER_NUMBERS,
)


# =============================================================================
# 1. Individual family dimensions -- manuscript ground truth
# =============================================================================

class TestHeisenberg:
    """Heisenberg H_k: (1, 1, 1), total 3.

    Source: chiral_center_theorem.tex lines 1780-1795
    HH^0 = C (center = scalars)
    HH^1 = C (outer derivation D(alpha) = 1, level deformation)
    HH^2 = C (dual vacuum, obstruction class)
    """

    def test_dimensions(self):
        h = chirhoch_heisenberg()
        # VERIFIED: [DC] chiral_center_theorem.tex lines 1780-1795
        # VERIFIED: [DC] chiral_hochschild_koszul.tex lines 4760-4772
        assert h.dim0 == 1
        assert h.dim1 == 1
        assert h.dim2 == 1

    def test_total(self):
        h = chirhoch_heisenberg()
        assert h.total == 3

    def test_poincare(self):
        h = chirhoch_heisenberg()
        assert h.poincare_poly == "1 + t + t^2"

    def test_hilbert_triple(self):
        h = chirhoch_heisenberg()
        assert h.hilbert_triple == (1, 1, 1)


class TestAffineSl2:
    """Affine sl_2 at generic k: (1, 3, 1), total 5.

    Source: chiral_center_theorem.tex lines 1800-1815
    HH^1 = sl_2 (3-dim: outer derivations = current deformations)
    CRITICAL: total = 5 > 4, violating old Theorem H bound.
    """

    def test_dimensions(self):
        a = chirhoch_affine_km("sl_2")
        # VERIFIED: [DC] chiral_center_theorem.tex lines 1800-1815
        # VERIFIED: [DC] proof lines 1883-1890: "V = sl_2 (three-dimensional)"
        assert a.dim0 == 1
        assert a.dim1 == 3   # KEY: dim(sl_2) = 3
        assert a.dim2 == 1

    def test_total_exceeds_old_bound(self):
        """The key datum: sl_2 total = 5 > 4."""
        a = chirhoch_affine_km("sl_2")
        assert a.total == 5
        assert a.total > 4  # violates old Theorem H

    def test_old_bound_violated(self):
        a = chirhoch_affine_km("sl_2")
        assert not old_theorem_h_bound_holds(a)

    def test_hilbert_triple(self):
        a = chirhoch_affine_km("sl_2")
        assert a.hilbert_triple == (1, 3, 1)


class TestAffineSl3:
    """Affine sl_3 at generic k: (1, 8, 1), total 10.

    dim(sl_3) = 8 = 3^2 - 1.
    """

    def test_dimensions(self):
        a = chirhoch_affine_km("sl_3")
        # VERIFIED: [DC] dim(sl_3) = 8; Koszul resolution gives HH^1 = g
        # VERIFIED: [DA] A_2: dim = n(n+2) = 2*4 = 8
        assert a.dim0 == 1
        assert a.dim1 == 8
        assert a.dim2 == 1

    def test_total(self):
        a = chirhoch_affine_km("sl_3")
        assert a.total == 10


class TestVirasoro:
    """Virasoro Vir_c: (1, 0, 1), total 2.

    Source: chiral_center_theorem.tex lines 1826-1833
    HH^1 = 0 (quartic pole; all derivations inner)
    """

    def test_dimensions(self):
        v = chirhoch_virasoro()
        # VERIFIED: [DC] chiral_center_theorem.tex lines 1826-1833
        # VERIFIED: [DC] proof Part (iii) lines 1899-1916
        assert v.dim0 == 1
        assert v.dim1 == 0
        assert v.dim2 == 1

    def test_total(self):
        v = chirhoch_virasoro()
        assert v.total == 2

    def test_poincare(self):
        v = chirhoch_virasoro()
        assert v.poincare_poly == "1 + t^2"

    def test_old_bound_holds(self):
        v = chirhoch_virasoro()
        assert old_theorem_h_bound_holds(v)


class TestFreeFermionBc:
    """Free fermion bc: (1, 0, 1), total 2.

    Source: chiral_hochschild_koszul.tex lines 4796-4810
    HH^1 = 0 (simple pole makes derivations inner)
    """

    def test_dimensions(self):
        f = chirhoch_free_fermion_bc()
        # VERIFIED: [DC] chiral_hochschild_koszul.tex lines 4796-4810
        # VERIFIED: [DC] Koszul duality check lines 4820-4824
        assert f.dim0 == 1
        assert f.dim1 == 0
        assert f.dim2 == 1

    def test_total(self):
        f = chirhoch_free_fermion_bc()
        assert f.total == 2


class TestFreeBetagamma:
    """Free betagamma: (1, 0, 1), total 2.

    Source: chiral_hochschild_koszul.tex lines 4820-4824
    Koszul dual to bc.
    """

    def test_dimensions(self):
        bg = chirhoch_free_betagamma()
        # VERIFIED: [DC] chiral_hochschild_koszul.tex lines 4820-4824
        # VERIFIED: [SY] Koszul dual to bc: ChirHoch^n(BG) = ChirHoch^{2-n}(bc)^*
        assert bg.dim0 == 1
        assert bg.dim1 == 0
        assert bg.dim2 == 1

    def test_total(self):
        bg = chirhoch_free_betagamma()
        assert bg.total == 2


class TestWAlgebra:
    """W_N algebras: (1, 0, 1), total 2 for all N >= 2."""

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: must give identical dimensions."""
        w2 = chirhoch_w_algebra(2)
        vir = chirhoch_virasoro()
        assert w2.dim0 == vir.dim0
        assert w2.dim1 == vir.dim1
        assert w2.dim2 == vir.dim2
        assert w2.total == vir.total

    def test_w3_dimensions(self):
        w3 = chirhoch_w_algebra(3)
        # VERIFIED: [LT] W_3 structure determined by c at generic c
        # VERIFIED: [DC] W_2 = Vir consistency
        assert w3.dim0 == 1
        assert w3.dim1 == 0
        assert w3.dim2 == 1
        assert w3.total == 2

    def test_w4_dimensions(self):
        w4 = chirhoch_w_algebra(4)
        assert w4.total == 2

    def test_invalid_n(self):
        with pytest.raises(ValueError, match="N >= 2"):
            chirhoch_w_algebra(1)


class TestLattice:
    """Lattice V_Lambda: (1, rank, 1), total rank+2."""

    def test_rank1(self):
        lat = chirhoch_lattice(1)
        assert lat.dim0 == 1
        assert lat.dim1 == 1
        assert lat.dim2 == 1
        assert lat.total == 3

    def test_rank2(self):
        lat = chirhoch_lattice(2)
        assert lat.dim1 == 2
        assert lat.total == 4

    def test_rank8(self):
        lat = chirhoch_lattice(8)
        assert lat.dim1 == 8
        assert lat.total == 10

    def test_invalid_rank(self):
        with pytest.raises(ValueError, match="rank must be >= 1"):
            chirhoch_lattice(0)


# =============================================================================
# 2. Concentration in degrees {0, 1, 2} -- Theorem H unconditional
# =============================================================================

class TestConcentration:
    """Theorem H concentration: ChirHoch^n = 0 for n not in {0, 1, 2}.

    This is proved for ALL Koszul chiral algebras via the de Rham
    amplitude bound on curves (dim X = 1 => Ext vanishes for n > 2).
    """

    def test_all_families_concentrated(self):
        for data in all_standard_families():
            assert theorem_h_concentration_holds(data), (
                f"{data.family} fails concentration"
            )


# =============================================================================
# 3. Old Theorem H bound violations
# =============================================================================

class TestOldBoundViolations:
    """The old "dim_total <= 4" claim is violated by affine KM with dim(g) >= 3.

    Source: chiral_center_theorem.tex line 1904 states "total dimension at
    most 4" but sl_2 gives total 5.
    """

    def test_sl2_violates(self):
        """The primary violation: sl_2 total = 5."""
        assert not old_theorem_h_bound_holds(chirhoch_affine_km("sl_2"))

    def test_sl3_violates(self):
        assert not old_theorem_h_bound_holds(chirhoch_affine_km("sl_3"))

    def test_e8_violates(self):
        """E8: total = 250."""
        e8 = chirhoch_affine_km("E8")
        assert e8.total == 250
        assert not old_theorem_h_bound_holds(e8)

    def test_heisenberg_satisfies(self):
        assert old_theorem_h_bound_holds(chirhoch_heisenberg())

    def test_virasoro_satisfies(self):
        assert old_theorem_h_bound_holds(chirhoch_virasoro())

    def test_bc_satisfies(self):
        assert old_theorem_h_bound_holds(chirhoch_free_fermion_bc())

    def test_count_violations_in_census(self):
        """Count how many standard families violate the old bound."""
        families = all_standard_families()
        violations = [f for f in families if not old_theorem_h_bound_holds(f)]
        # At minimum: sl_2, sl_3, sl_4, G2, E8
        assert len(violations) >= 5


# =============================================================================
# 4. Koszul duality consistency
# =============================================================================

class TestKoszulDuality:
    """Palindromic duality: dim0(A) = dim2(A!), dim2(A) = dim0(A!).

    For self-dual families or Koszul pairs with known dual dimensions.
    """

    def test_bc_betagamma_duality(self):
        """bc and betagamma are Koszul dual."""
        bc = chirhoch_free_fermion_bc()
        bg = chirhoch_free_betagamma()
        assert koszul_duality_check(bc, bg)

    def test_heisenberg_self_dual_structure(self):
        """Heisenberg: dim0 = dim2 = 1 (symmetric Poincare polynomial)."""
        h = chirhoch_heisenberg()
        assert h.dim0 == h.dim2  # palindromic

    def test_affine_sl2_palindromic(self):
        """Affine sl_2: dim0 = dim2 = 1 (palindromic)."""
        a = chirhoch_affine_km("sl_2")
        assert a.dim0 == a.dim2

    def test_all_families_dim0_equals_dim2(self):
        """For all standard families at generic parameters, dim0 = dim2 = 1."""
        for data in all_standard_families():
            assert data.dim0 == 1, f"{data.family}: dim0 = {data.dim0}"
            assert data.dim2 == 1, f"{data.family}: dim2 = {data.dim2}"


# =============================================================================
# 5. Parametric scaling for affine KM
# =============================================================================

class TestAffineKMScaling:
    """ChirHoch^1(V_k(g)) = dim(g) at generic level."""

    @pytest.mark.parametrize("g,expected_dim1", [
        ("sl_2", 3),
        ("sl_3", 8),
        ("sl_4", 15),
        ("sl_5", 24),
        ("sl_6", 35),
        ("G2", 14),
        ("F4", 52),
        ("E6", 78),
        ("E7", 133),
        ("E8", 248),
    ])
    def test_dim1_equals_dim_g(self, g, expected_dim1):
        """ChirHoch^1 = dim(g) for all simple Lie algebras."""
        data = chirhoch_affine_km(g)
        # VERIFIED: [DC] Koszul resolution, generating space V = g
        # VERIFIED: [LT] Ext^1 = V for Koszul algebras
        assert data.dim1 == expected_dim1

    @pytest.mark.parametrize("g,expected_total", [
        ("sl_2", 5),
        ("sl_3", 10),
        ("sl_4", 17),
        ("E8", 250),
    ])
    def test_total_equals_dim_g_plus_2(self, g, expected_total):
        """Total = dim(g) + 2 for all affine KM."""
        data = chirhoch_affine_km(g)
        assert data.total == expected_total
        assert data.total == dim_simple_lie_algebra(g) + 2

    def test_sl_n_formula(self):
        """For sl_N: dim = N^2 - 1, total = N^2 + 1."""
        for n in range(2, 10):
            data = chirhoch_affine_km(f"sl_{n}")
            assert data.dim1 == n * n - 1
            assert data.total == n * n + 1


# =============================================================================
# 6. Lie algebra dimension data
# =============================================================================

class TestLieAlgebraDims:
    """Verify the Lie algebra dimension table."""

    def test_sl_formula(self):
        """dim(sl_N) = N^2 - 1."""
        for n in range(2, 20):
            # VERIFIED: [DC] A_{n-1} has dim n^2 - 1
            # VERIFIED: [LT] Humphreys, Introduction to Lie Algebras
            assert dim_simple_lie_algebra(f"sl_{n}") == n * n - 1

    def test_exceptional_dims(self):
        """Exceptional Lie algebra dimensions from Humphreys."""
        # VERIFIED: [LT] Humphreys Table p.66
        # VERIFIED: [DC] root system counting
        assert dim_simple_lie_algebra("G2") == 14
        assert dim_simple_lie_algebra("F4") == 52
        assert dim_simple_lie_algebra("E6") == 78
        assert dim_simple_lie_algebra("E7") == 133
        assert dim_simple_lie_algebra("E8") == 248

    def test_e8_adjoint(self):
        """E8 adjoint = 248, matching compute/lib/ FUNDAMENTAL_DIMS."""
        # VERIFIED: [DC] compute/lib/bc_exceptional_categorical_zeta_engine.py
        # VERIFIED: [LT] E8 root system: 240 roots + 8 Cartan = 248
        assert LIE_ALGEBRA_DIMS["E8"] == 248

    def test_rank_sl(self):
        """rank(sl_N) = N - 1."""
        for n in range(2, 10):
            assert rank_simple_lie_algebra(f"sl_{n}") == n - 1

    def test_unknown_algebra(self):
        with pytest.raises(KeyError):
            dim_simple_lie_algebra("unknown_algebra")


# =============================================================================
# 7. Generic interface
# =============================================================================

class TestGenericInterface:
    """Test the chirhoch_dimensions() dispatcher."""

    def test_heisenberg_alias(self):
        h1 = chirhoch_dimensions("heisenberg")
        h2 = chirhoch_dimensions("heis")
        assert h1.hilbert_triple == h2.hilbert_triple

    def test_virasoro_alias(self):
        v1 = chirhoch_dimensions("virasoro")
        v2 = chirhoch_dimensions("vir")
        assert v1.hilbert_triple == v2.hilbert_triple

    def test_affine_km(self):
        a = chirhoch_dimensions("affine_km", lie_algebra="sl_2")
        assert a.dim1 == 3

    def test_w_algebra(self):
        w = chirhoch_dimensions("w_algebra", N=3)
        assert w.total == 2

    def test_lattice(self):
        lat = chirhoch_dimensions("lattice", rank=3)
        assert lat.total == 5

    def test_unknown_family(self):
        with pytest.raises(KeyError):
            chirhoch_dimensions("nonexistent")

    def test_missing_param(self):
        with pytest.raises(ValueError):
            chirhoch_dimensions("affine_km")  # no lie_algebra


# =============================================================================
# 8. Summary table
# =============================================================================

class TestSummaryTable:
    """Test the summary table generation."""

    def test_table_not_empty(self):
        table = generate_summary_table()
        assert len(table) > 100

    def test_table_contains_key_families(self):
        table = generate_summary_table()
        assert "Heisenberg" in table
        assert "Virasoro" in table
        assert "sl_2" in table
        assert "E8" in table

    def test_table_reports_violations(self):
        table = generate_summary_table()
        assert "VIOLATED" in table
        assert "**N**" in table


# =============================================================================
# 9. DataClass invariants
# =============================================================================

class TestDataClassInvariants:
    """Test that ChirHochData enforces its invariants."""

    def test_total_consistency(self):
        """total = dim0 + dim1 + dim2 for all families."""
        for data in all_standard_families():
            assert data.total == data.dim0 + data.dim1 + data.dim2, (
                f"{data.family}: {data.total} != "
                f"{data.dim0} + {data.dim1} + {data.dim2}"
            )

    def test_all_dim0_positive(self):
        for data in all_standard_families():
            assert data.dim0 >= 1

    def test_all_dim1_nonnegative(self):
        for data in all_standard_families():
            assert data.dim1 >= 0

    def test_all_dim2_positive(self):
        for data in all_standard_families():
            assert data.dim2 >= 1


# =============================================================================
# 10. Cross-checks with CLAUDE.md constants
# =============================================================================

class TestCrossChecks:
    """Cross-check with CLAUDE.md C27 and Theorem H status."""

    def test_c27_correction(self):
        """CLAUDE.md C27 states 'dim_total <= 4'. This is WRONG for sl_2.

        The engine demonstrates the correction: concentration in {0,1,2}
        holds, but the total dimension bound must be removed or weakened.
        """
        sl2 = chirhoch_affine_km("sl_2")
        assert sl2.total == 5  # contradicts C27 "dim <= 4"
        # But concentration still holds
        assert sl2.concentrated_in_012

    def test_theorem_h_correct_statement(self):
        """Correct Theorem H: concentration in {0,1,2}, no universal dim bound.

        For affine V_k(g): total = dim(g) + 2.
        For Virasoro/W_N/bc/bg: total = 2.
        For Heisenberg: total = 3.
        """
        assert chirhoch_virasoro().total == 2
        assert chirhoch_heisenberg().total == 3
        assert chirhoch_affine_km("sl_2").total == 5
        assert chirhoch_affine_km("E8").total == 250
        # All concentrated in {0,1,2}
        for data in all_standard_families():
            assert data.concentrated_in_012
