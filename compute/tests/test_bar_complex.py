"""Tests for compute/lib/bar_complex.py — bar dimensions, OPE algebras.

Ground truth from PROVED formulas in the manuscript:
  Free fermion: dim B-bar^n(F) = p(n-1)  [rem:bar-dims-partitions]
  Heisenberg:   dim B-bar^n(H) = p(n-2) for n>=2, 1 for n=1  [rem:bar-dims-partitions]
  KM chain groups: dim B-bar^n = dim(g)^n * (n-1)!  [rem:bar-dims-level-independent]
  KM bar COHOMOLOGY: dim H^n(B-bar) given in Master Table  [examples_summary.tex]

The Master Table reports bar COHOMOLOGY (not chain groups).
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.bar_complex import (
    OPEAlgebra,
    Generator,
    heisenberg_algebra,
    sl2_algebra,
    virasoro_algebra,
    free_fermion_algebra,
    bar_dim_heisenberg,
    bar_dim_free_fermion,
    bar_dim_sl2,
    bar_dim_virasoro,
    bar_dim_w3,
    bar_dim_sl3,
    km_chain_space_dim,
    KNOWN_BAR_DIMS,
    KNOWN_CHAIN_GROUP_DIMS,
    verify_bar_dim,
)


# ---------------------------------------------------------------------------
# OPE algebra construction
# ---------------------------------------------------------------------------

class TestOPEAlgebra:
    def test_heisenberg(self):
        H = heisenberg_algebra()
        assert H.dim == 1
        assert H.gen_names == ["J"]
        # No simple pole
        assert H.simple_pole("J", "J") == {}
        # Double pole = kappa
        dp = H.double_pole("J", "J")
        assert "1" in dp

    def test_sl2(self):
        sl2 = sl2_algebra()
        assert sl2.dim == 3
        assert set(sl2.gen_names) == {"e", "h", "f"}
        # e(z)f(w) has simple pole h and double pole k
        sp = sl2.simple_pole("e", "f")
        assert sp == {"h": Rational(1)}

    def test_virasoro(self):
        vir = virasoro_algebra()
        assert vir.dim == 1
        assert vir.gen_names == ["T"]

    def test_free_fermion(self):
        ff = free_fermion_algebra()
        assert ff.dim == 1
        # Simple pole only, no double pole
        assert ff.simple_pole("psi", "psi") == {"1": Rational(1)}
        assert ff.double_pole("psi", "psi") == {}


# ---------------------------------------------------------------------------
# Known bar dimensions (Master Table ground truth)
# ---------------------------------------------------------------------------

class TestHeisenbergBarDims:
    """Heisenberg bar dimensions: 1, 1, 1, 2, 3.

    dim B-bar^1(H) = 1 (one generator J)
    dim B-bar^n(H) = p(n-2) for n >= 2  (partition function)
    Source: free_fields.tex rem:bar-dims-partitions, lines 2767-2773
    """
    def test_degree_1(self):
        assert bar_dim_heisenberg(1) == 1

    def test_degree_2(self):
        assert bar_dim_heisenberg(2) == 1  # p(0) = 1

    def test_degree_3(self):
        assert bar_dim_heisenberg(3) == 1  # p(1) = 1

    def test_degree_4(self):
        assert bar_dim_heisenberg(4) == 2  # p(2) = 2

    def test_degree_5(self):
        assert bar_dim_heisenberg(5) == 3  # p(3) = 3

    def test_matches_master_table(self):
        """Cross-check against Master Table ground truth."""
        for deg, expected in KNOWN_BAR_DIMS["Heisenberg"].items():
            computed = bar_dim_heisenberg(deg)
            assert computed == expected, (
                f"Heisenberg bar dim at degree {deg}: "
                f"computed {computed}, Master Table says {expected}"
            )


class TestFreeFermionBarDims:
    """Free fermion bar dimensions: 1, 1, 2, 3, 5 = p(n-1).

    Source: free_fields.tex rem:bar-dims-partitions, lines 2750-2754
    """
    def test_degree_1(self):
        assert bar_dim_free_fermion(1) == 1  # p(0) = 1

    def test_degree_2(self):
        assert bar_dim_free_fermion(2) == 1  # p(1) = 1

    def test_degree_3(self):
        assert bar_dim_free_fermion(3) == 2  # p(2) = 2

    def test_degree_4(self):
        assert bar_dim_free_fermion(4) == 3  # p(3) = 3

    def test_degree_5(self):
        assert bar_dim_free_fermion(5) == 5  # p(4) = 5

    def test_matches_master_table(self):
        for deg, expected in KNOWN_BAR_DIMS["free_fermion"].items():
            computed = bar_dim_free_fermion(deg)
            assert computed == expected, (
                f"Free fermion bar dim at degree {deg}: "
                f"computed {computed}, Master Table says {expected}"
            )


class TestKnownBarDims:
    """Verify known bar dimensions from PROVED formulas."""

    def test_sl2_cohomology_dims(self):
        """sl_2 bar cohomology = Riordan R(n+3) (OEIS A005043)."""
        assert bar_dim_sl2(1) == 3
        assert bar_dim_sl2(2) == 6
        assert bar_dim_sl2(3) == 15
        assert bar_dim_sl2(4) == 36
        assert bar_dim_sl2(5) == 91
        assert bar_dim_sl2(6) == 232
        assert bar_dim_sl2(7) == 603

    def test_sl3_cohomology_dims(self):
        """sl_3 bar cohomology: 8, 36, 204 (Master Table)."""
        assert bar_dim_sl3(1) == 8
        assert bar_dim_sl3(2) == 36
        assert bar_dim_sl3(3) == 204

    def test_virasoro_known(self):
        """Virasoro: M(n+1) - M(n) where M = Motzkin (OEIS A002026)."""
        assert bar_dim_virasoro(1) == 1
        assert bar_dim_virasoro(2) == 2
        assert bar_dim_virasoro(3) == 5
        assert bar_dim_virasoro(4) == 12
        assert bar_dim_virasoro(5) == 30
        assert bar_dim_virasoro(6) == 76
        assert bar_dim_virasoro(7) == 196
        assert bar_dim_virasoro(8) == 512

    def test_w3_known(self):
        """W_3: from summary table (not independently proved)."""
        assert bar_dim_w3(1) == 2
        assert bar_dim_w3(2) == 5
        assert bar_dim_w3(3) == 16
        assert bar_dim_w3(4) == 52


class TestChainGroupDims:
    """Chain group dims: dim B-bar^n = dim(g)^n * (n-1)! (proved)."""

    def test_sl2_chain_groups(self):
        for n in range(1, 6):
            expected = KNOWN_CHAIN_GROUP_DIMS["sl2"][n]
            assert km_chain_space_dim(3, n) == expected

    def test_sl3_chain_groups(self):
        for n in range(1, 5):
            expected = KNOWN_CHAIN_GROUP_DIMS["sl3"][n]
            assert km_chain_space_dim(8, n) == expected

    def test_chain_larger_than_cohomology(self):
        """Chain groups are always >= cohomology dims."""
        for n in range(1, 6):
            chain = km_chain_space_dim(3, n)
            cohom = bar_dim_sl2(n)
            assert chain >= cohom, f"deg {n}: chain {chain} < cohom {cohom}"


class TestVerification:
    def test_correct_value(self):
        ok, msg = verify_bar_dim("Heisenberg", 1, 1)
        assert ok
        assert "VERIFIED" in msg

    def test_wrong_value(self):
        ok, msg = verify_bar_dim("Heisenberg", 1, 999)
        assert not ok
        assert "MISMATCH" in msg

    def test_unknown_value(self):
        """Unknown algebra passes (no ground truth to contradict)."""
        ok, msg = verify_bar_dim("unknown_algebra", 4, 42)
        assert ok
        assert "No ground truth" in msg

    def test_all_known_self_consistent(self):
        """Every entry in KNOWN_BAR_DIMS verifies against itself."""
        for algebra, dims in KNOWN_BAR_DIMS.items():
            for degree, expected in dims.items():
                ok, msg = verify_bar_dim(algebra, degree, expected)
                assert ok, f"Self-consistency failed: {msg}"


# ---------------------------------------------------------------------------
# Chevalley-Eilenberg complex and explicit bar differentials
# ---------------------------------------------------------------------------

class TestCEComplex:
    """Tests for the CE complex of sl_2.
    
    Ground truth: H*(sl_2; k) = Λ(x_3) with x_3 in degree 3.
    Source: Weibel, Homological Algebra, Theorem 7.7.2
    """

    def test_ce_dimensions(self):
        from compute.lib.chiral_bar import CEComplex, sl2_structure_constants
        ce = CEComplex(3, sl2_structure_constants())
        assert ce.dim(0) == 1
        assert ce.dim(1) == 3
        assert ce.dim(2) == 3
        assert ce.dim(3) == 1

    def test_ce_d_squared_zero(self):
        """d² = 0 in the CE complex (from Jacobi identity)."""
        from compute.lib.chiral_bar import CEComplex, sl2_structure_constants
        ce = CEComplex(3, sl2_structure_constants())
        assert ce.verify_d_squared(0)
        assert ce.verify_d_squared(1)

    def test_ce_cohomology(self):
        """H*(sl_2) = Λ(x_3): dims 1,0,0,1."""
        from compute.lib.chiral_bar import CEComplex, sl2_structure_constants
        ce = CEComplex(3, sl2_structure_constants())
        cohom = ce.cohomology_dims()
        assert cohom == {0: 1, 1: 0, 2: 0, 3: 1}

    def test_d1_rank(self):
        """d1: C^1 → C^2 has rank 3 (isomorphism for semisimple g)."""
        from compute.lib.chiral_bar import CEComplex, sl2_structure_constants
        ce = CEComplex(3, sl2_structure_constants())
        d1 = ce.differential(1)
        assert d1.rank() == 3


class TestAssociativeBarDifferential:
    """Tests for the associative bar complex with Lie bracket.
    
    Ground truth: D21 matrix from comp:sl2-bar-matrix in detailed_computations.tex.
    """

    def test_d21_matches_manuscript(self):
        """D21 matrix matches comp:sl2-bar-matrix."""
        from compute.lib.chiral_bar import sl2_assoc_bar_diff_2to1
        from sympy import Matrix
        D21 = sl2_assoc_bar_diff_2to1()
        expected = Matrix([
            [0, -2, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, -1, 0, 0],
            [0, 0, 0, 0, 0, -2, 0, 2, 0]
        ])
        assert D21.equals(expected)

    def test_d21_rank(self):
        from compute.lib.chiral_bar import sl2_assoc_bar_diff_2to1
        assert sl2_assoc_bar_diff_2to1().rank() == 3

    def test_d32_rank(self):
        from compute.lib.chiral_bar import sl2_assoc_bar_diff_3to2
        assert sl2_assoc_bar_diff_3to2().rank() == 8

    def test_d_squared_nonzero(self):
        """d² ≠ 0 for associative bar with Lie bracket (curvature = associator)."""
        from compute.lib.chiral_bar import sl2_assoc_bar_diff_2to1, sl2_assoc_bar_diff_3to2
        from sympy import zeros
        D21 = sl2_assoc_bar_diff_2to1()
        D32 = sl2_assoc_bar_diff_3to2()
        product = D21 * D32
        assert not product.equals(zeros(*product.shape)), "d² should be nonzero (curvature)"

    def test_associator_example(self):
        """d²([e|e|f]) = 2e (from [[e,e],f] - [e,[e,f]] = -[e,h] = 2e)."""
        from compute.lib.chiral_bar import sl2_assoc_bar_diff_2to1, sl2_assoc_bar_diff_3to2
        D21 = sl2_assoc_bar_diff_2to1()
        D32 = sl2_assoc_bar_diff_3to2()
        product = D21 * D32
        # [e|e|f] is column 0*9 + 0*3 + 2 = 2
        result = product[:, 2]
        assert result[0] == 2   # 2·e
        assert result[1] == 0
        assert result[2] == 0


class TestSl3BarGFConjecture:
    """Tests for conj:sl3-bar-gf — rational GF for sl₃ bar cohomology.

    GF = 4x(2-13x-2x²) / ((1-8x)(1-3x-x²))
    Recurrence: a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3)
    Characteristic polynomial: (t-8)(t²-3t-1)
    """

    def test_recurrence_matches_known(self):
        """Recurrence reproduces known values a(1)=8, a(2)=36, a(3)=204."""
        from compute.lib.bar_complex import bar_dim_sl3_conjectured
        assert bar_dim_sl3_conjectured(1) == 8
        assert bar_dim_sl3_conjectured(2) == 36
        assert bar_dim_sl3_conjectured(3) == 204

    def test_predicted_deg4(self):
        """Predicted a(4) = 1352."""
        from compute.lib.bar_complex import bar_dim_sl3_conjectured
        assert bar_dim_sl3_conjectured(4) == 1352

    def test_predicted_deg5(self):
        """Predicted a(5) = 9892."""
        from compute.lib.bar_complex import bar_dim_sl3_conjectured
        assert bar_dim_sl3_conjectured(5) == 9892

    def test_gf_series_expansion(self):
        """GF power series matches recurrence through degree 10."""
        from sympy import symbols, series, Rational
        from compute.lib.bar_complex import bar_dim_sl3_conjectured
        x = symbols('x')
        gf = -4*x*(2*x**2 + 13*x - 2) / ((1-8*x)*(1-3*x-x**2))
        s = series(gf, x, 0, 11)
        for n in range(1, 11):
            assert s.coeff(x, n) == bar_dim_sl3_conjectured(n)

    def test_characteristic_polynomial(self):
        """Char poly (t-8)(t²-3t-1) matches denominator."""
        from sympy import symbols, factor, expand
        t = symbols('t')
        char_poly = t**3 - 11*t**2 + 23*t + 8
        assert factor(char_poly) == (t - 8) * (t**2 - 3*t - 1)

    def test_growth_rate(self):
        """a(n)/a(n-1) → 8 = dim(sl₃)."""
        from compute.lib.bar_complex import bar_dim_sl3_conjectured
        ratio = bar_dim_sl3_conjectured(15) / bar_dim_sl3_conjectured(14)
        assert abs(ratio - 8.0) < 0.001

    def test_all_positive(self):
        """All bar cohomology dimensions are positive."""
        from compute.lib.bar_complex import bar_dim_sl3_conjectured
        for n in range(1, 20):
            assert bar_dim_sl3_conjectured(n) > 0

    def test_h2_equals_sym2(self):
        """H² = C(d+1,2) = dim S²(g) for KM algebras."""
        from math import comb
        # sl₂: dim=3, H²=6
        assert comb(3+1, 2) == 6 == KNOWN_BAR_DIMS["sl2"][2]
        # sl₃: dim=8, H²=36
        assert comb(8+1, 2) == 36 == KNOWN_BAR_DIMS["sl3"][2]
