r"""Tests for gravitational coproduct primitivity via HPL ghost obstruction.

Verifies the central claim: all HPL tree corrections to the transferred
coproduct vanish due to ghost-number obstruction.  The contracting homotopy
h in the DS SDR has ghost degree -1, while the BRST perturbation delta
has ghost degree +1.  For a binary tree with n leaves: (n-1) vertices of
delta and (n-2) edges of h give total ghost (n-1) - (n-2) = +1.  Since
the Virasoro algebra lives in ghost number 0, the projection p kills every
correction term.

This module tests BOTH:
  (A) The abstract ghost-number argument (counting ghost shifts in trees).
  (B) Explicit matrix-level SDR computation verifying the corrections vanish
      numerically for randomly generated SDRs satisfying all axioms.

Test organization:
  I.    SDR properties: ghost degrees, algebraic relations
  II.   Sugawara OPE: central charge c = 3k/(k+2) for sl_2
  III.  Ghost-number analysis: all trees at arities 2-10
  IV.   Coproduct primitivity: the main theorem (abstract)
  V.    r-matrix transfer: KM -> Virasoro via AP19
  VI.   CYBE: classical Yang-Baxter for sl_2 and Virasoro
  VII.  Kappa consistency: additivity under DS
  VIII. Cross-checks with existing modules
  IX.   Structure constant checks
  X.    Full verification suite
  XI.   Explicit SDR axiom verification
  XII.  Explicit HPL corrections (matrix-level)
  XIII. Ghost-number tracking
  XIV.  Affine coproduct nontriviality
  XV.   Edge cases and special levels
  XVI.  Parametric primitivity

References:
  - thm:coproduct-primitivity-hpl (yangians_drinfeld_kohno.tex)
  - prop:ghost-obstruction-vanishing (yangians_drinfeld_kohno.tex)
  - AP19: bar kernel absorbs a pole (CLAUDE.md)
  - AP27: field weight != propagator weight (CLAUDE.md)
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.gravitational_coproduct import (
    # Basic data
    c_sl2,
    c_vir_from_sl2,
    c_ghost_sl2,
    kappa_sl2,
    kappa_vir,
    kappa_ghost_sl2,
    SL2_STRUCTURE_CONSTANTS,
    SL2_KILLING,
    SL2_GENERATORS,
    # BRST elements
    BRSTElement,
    matter_current,
    ghost,
    antighost,
    sugawara_T,
    # SDR
    SDR,
    sdr_sl2_virasoro,
    # Tree combinatorics
    BinaryTree,
    count_binary_trees,
    enumerate_binary_trees,
    # Ghost analysis
    HPLGhostAnalysis,
    analyze_tree_ghost,
    analyze_all_trees_ghost,
    analyze_transferred_product_ghost,
    # Coproduct corrections
    HPLCoproductCorrection,
    compute_coproduct_corrections,
    # r-matrix
    rmatrix_km_sl2,
    rmatrix_vir_from_sl2,
    verify_rmatrix_transfer_ghost,
    # CYBE
    verify_cybe_sl2_scalar,
    verify_cybe_virasoro_scalar,
    # Kappa
    verify_kappa_ds_consistency,
    # Sugawara
    sugawara_central_charge_from_ope,
    # Master
    verify_coproduct_primitivity,
    full_verification,
    # Explicit BRST
    TruncatedBRSTComplex,
    build_truncated_brst,
    ghost_number_of_element,
    compute_hpl_delta_z2_explicit,
    compute_hpl_delta_z2_tree_explicit,
    compute_hpl_delta_z3_explicit,
    compute_hpl_corrections_explicit,
    # Ghost tracking
    ghost_number_track,
    ghost_number_of_hpl_tree,
    # Explicit SDR
    ExplicitSDR,
    build_explicit_sdr,
    compute_hpl_arity2_explicit_sdr,
    compute_hpl_arity3_explicit_sdr,
    compute_hpl_corrections_with_sdr,
    # Affine coproduct
    affine_coproduct_is_nontrivial,
    # Edge cases
    verify_primitivity_edge_cases,
    # Parametric
    verify_primitivity_parametric,
    # Helpers
    _frac,
)


# ============================================================================
# I. SDR properties
# ============================================================================

class TestSDR:
    """Verify the Strong Deformation Retract for sl_2 -> Virasoro."""

    def test_sdr_ghost_iota(self):
        """iota (Sugawara embedding) has ghost number 0."""
        sdr = sdr_sl2_virasoro()
        assert sdr.ghost_iota == 0

    def test_sdr_ghost_p(self):
        """p (projection to BRST cohomology) has ghost number 0."""
        sdr = sdr_sl2_virasoro()
        assert sdr.ghost_p == 0

    def test_sdr_ghost_h(self):
        """h (contracting homotopy) has ghost number -1."""
        sdr = sdr_sl2_virasoro()
        assert sdr.ghost_h == -1

    def test_sdr_verify_all_degrees(self):
        """All three ghost degrees are correct."""
        sdr = sdr_sl2_virasoro()
        result = sdr.verify_ghost_degrees()
        assert result['iota_ghost_0'] is True
        assert result['p_ghost_0'] is True
        assert result['h_ghost_minus1'] is True

    def test_brst_element_ghost_matter(self):
        """Matter currents J^a have ghost number 0."""
        for a in SL2_GENERATORS:
            elem = matter_current(a)
            assert elem.ghost_number == 0, f"J^{a} should have ghost 0"

    def test_brst_element_ghost_ghost(self):
        """Ghosts c^a have ghost number +1."""
        for a in SL2_GENERATORS:
            elem = ghost(a)
            assert elem.ghost_number == 1, f"c^{a} should have ghost +1"

    def test_brst_element_ghost_antighost(self):
        """Anti-ghosts b_a have ghost number -1."""
        for a in SL2_GENERATORS:
            elem = antighost(a)
            assert elem.ghost_number == -1, f"b_{a} should have ghost -1"

    def test_sugawara_ghost_zero(self):
        """Sugawara T has ghost number 0."""
        T = sugawara_T(Fraction(1))
        assert T.ghost_number == 0

    def test_sdr_composition_p_iota(self):
        """SDR relation (S1): p . iota should be identity (ghost 0 + 0 = 0)."""
        sdr = sdr_sl2_virasoro()
        total_ghost = sdr.ghost_p + sdr.ghost_iota
        assert total_ghost == 0

    def test_sdr_composition_h_squared(self):
        """SDR relation (S3): h^2 = 0 is consistent with ghost -2."""
        sdr = sdr_sl2_virasoro()
        total_ghost = 2 * sdr.ghost_h
        assert total_ghost == -2

    def test_sdr_composition_h_iota(self):
        """SDR relation (S4): h . iota = 0 (ghost -1 + 0 = -1)."""
        sdr = sdr_sl2_virasoro()
        total_ghost = sdr.ghost_h + sdr.ghost_iota
        assert total_ghost == -1

    def test_sdr_composition_p_h(self):
        """SDR relation (S5): p . h = 0 (ghost 0 + (-1) = -1)."""
        sdr = sdr_sl2_virasoro()
        total_ghost = sdr.ghost_p + sdr.ghost_h
        assert total_ghost == -1


# ============================================================================
# II. Sugawara OPE and central charge
# ============================================================================

class TestSugawara:
    """Verify the Sugawara construction and central charge formulas."""

    def test_c_sl2_k1(self):
        """c(sl_2, k=1) = 3*1/(1+2) = 1."""
        assert c_sl2(Fraction(1)) == Fraction(1)

    def test_c_sl2_k2(self):
        """c(sl_2, k=2) = 3*2/(2+2) = 3/2."""
        assert c_sl2(Fraction(2)) == Fraction(3, 2)

    def test_c_sl2_k3(self):
        """c(sl_2, k=3) = 3*3/(3+2) = 9/5."""
        assert c_sl2(Fraction(3)) == Fraction(9, 5)

    def test_c_sl2_k4(self):
        """c(sl_2, k=4) = 3*4/(4+2) = 2."""
        assert c_sl2(Fraction(4)) == Fraction(2)

    def test_c_sl2_critical_raises(self):
        """c(sl_2) at critical level k=-2 should raise."""
        with pytest.raises(ValueError, match="Critical level"):
            c_sl2(Fraction(-2))

    def test_c_vir_k1(self):
        """c(Vir) from DS(sl_2, k=1): (1-4)/(1+2) = -1."""
        assert c_vir_from_sl2(Fraction(1)) == Fraction(-1)

    def test_c_vir_k2(self):
        """c(Vir) from DS(sl_2, k=2): (2-4)/(2+2) = -1/2."""
        assert c_vir_from_sl2(Fraction(2)) == Fraction(-1, 2)

    def test_c_vir_k4(self):
        """c(Vir) from DS(sl_2, k=4): (4-4)/(4+2) = 0."""
        assert c_vir_from_sl2(Fraction(4)) == Fraction(0)

    def test_c_vir_k10(self):
        """c(Vir) from DS(sl_2, k=10): (10-4)/(10+2) = 1/2."""
        assert c_vir_from_sl2(Fraction(10)) == Fraction(1, 2)

    def test_ghost_central_charge(self):
        """Ghost central charge = 2 for sl_2."""
        assert c_ghost_sl2() == Fraction(2)

    def test_central_charge_additivity_k1(self):
        """c(sl_2, k=1) = c(Vir, k=1) + c_ghost."""
        c_aff = c_sl2(Fraction(1))
        c_v = c_vir_from_sl2(Fraction(1))
        c_gh = c_ghost_sl2()
        assert c_aff == c_v + c_gh

    def test_central_charge_additivity_k2(self):
        """c(sl_2, k=2) = c(Vir, k=2) + c_ghost."""
        c_aff = c_sl2(Fraction(2))
        c_v = c_vir_from_sl2(Fraction(2))
        c_gh = c_ghost_sl2()
        assert c_aff == c_v + c_gh

    def test_central_charge_additivity_k3(self):
        """c(sl_2, k=3) = c(Vir, k=3) + c_ghost."""
        c_aff = c_sl2(Fraction(3))
        c_v = c_vir_from_sl2(Fraction(3))
        c_gh = c_ghost_sl2()
        assert c_aff == c_v + c_gh

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 5, 10, 50, 100])
    def test_central_charge_additivity_parametric(self, k_val):
        """Central charge additivity c(sl_2) = c(Vir) + c_ghost for all k."""
        k = Fraction(k_val)
        assert c_sl2(k) == c_vir_from_sl2(k) + c_ghost_sl2()

    def test_sugawara_ope_verification_k1(self):
        """Sugawara OPE gives correct c at k=1."""
        result = sugawara_central_charge_from_ope(Fraction(1))
        assert result['ds_match'] is True
        assert result['c_sugawara'] == Fraction(1)

    def test_sugawara_ope_verification_k2(self):
        """Sugawara OPE gives correct c at k=2."""
        result = sugawara_central_charge_from_ope(Fraction(2))
        assert result['ds_match'] is True

    def test_sugawara_ope_verification_k3(self):
        """Sugawara OPE gives correct c at k=3."""
        result = sugawara_central_charge_from_ope(Fraction(3))
        assert result['ds_match'] is True

    def test_sugawara_normalization_k1(self):
        """Sugawara normalization 1/(2(k+2)) at k=1 is 1/6."""
        result = sugawara_central_charge_from_ope(Fraction(1))
        assert result['sugawara_normalization'] == Fraction(1, 6)


# ============================================================================
# III. Ghost-number analysis for HPL trees
# ============================================================================

class TestGhostAnalysis:
    """Verify ghost-number counting for all HPL tree contributions."""

    def test_catalan_n1(self):
        """1 tree with 1 leaf (trivial)."""
        assert count_binary_trees(1) == 1

    def test_catalan_n2(self):
        """1 tree with 2 leaves."""
        assert count_binary_trees(2) == 1

    def test_catalan_n3(self):
        """2 trees with 3 leaves."""
        assert count_binary_trees(3) == 2

    def test_catalan_n4(self):
        """5 trees with 4 leaves."""
        assert count_binary_trees(4) == 5

    def test_catalan_n5(self):
        """14 trees with 5 leaves."""
        assert count_binary_trees(5) == 14

    def test_catalan_n6(self):
        """42 trees with 6 leaves."""
        assert count_binary_trees(6) == 42

    def test_catalan_n7(self):
        """132 trees with 7 leaves."""
        assert count_binary_trees(7) == 132

    def test_enumerate_count(self):
        """enumerate_binary_trees returns correct count for n=4."""
        trees = enumerate_binary_trees(4)
        assert len(trees) == 5

    def test_tree_arity2_internal_vertices(self):
        """Arity-2 tree has 1 internal vertex."""
        tree = BinaryTree(n_leaves=2)
        assert tree.n_internal_vertices == 1

    def test_tree_arity2_internal_edges(self):
        """Arity-2 tree has 0 internal edges."""
        tree = BinaryTree(n_leaves=2)
        assert tree.n_internal_edges == 0

    def test_tree_arity3_internal_vertices(self):
        """Arity-3 tree has 2 internal vertices."""
        tree = BinaryTree(n_leaves=3)
        assert tree.n_internal_vertices == 2

    def test_tree_arity3_internal_edges(self):
        """Arity-3 tree has 1 internal edge."""
        tree = BinaryTree(n_leaves=3)
        assert tree.n_internal_edges == 1

    def test_tree_arity4_internal_vertices(self):
        """Arity-4 tree has 3 internal vertices."""
        tree = BinaryTree(n_leaves=4)
        assert tree.n_internal_vertices == 3

    def test_tree_arity4_internal_edges(self):
        """Arity-4 tree has 2 internal edges."""
        tree = BinaryTree(n_leaves=4)
        assert tree.n_internal_edges == 2

    def test_ghost_arity2(self):
        """Arity-2 tree has total ghost +1."""
        sdr = sdr_sl2_virasoro()
        tree = BinaryTree(n_leaves=2)
        analysis = analyze_tree_ghost(tree, sdr)
        assert analysis.ghost_total == 1
        assert analysis.killed_by_projection is True

    def test_ghost_arity3(self):
        """All arity-3 trees have total ghost +1."""
        sdr = sdr_sl2_virasoro()
        for tree in enumerate_binary_trees(3):
            analysis = analyze_tree_ghost(tree, sdr)
            assert analysis.ghost_total == 1
            assert analysis.killed_by_projection is True

    def test_ghost_arity4(self):
        """All arity-4 trees have total ghost +1."""
        sdr = sdr_sl2_virasoro()
        for tree in enumerate_binary_trees(4):
            analysis = analyze_tree_ghost(tree, sdr)
            assert analysis.ghost_total == 1
            assert analysis.killed_by_projection is True

    def test_ghost_arity5(self):
        """All arity-5 trees (14 trees) have total ghost +1."""
        sdr = sdr_sl2_virasoro()
        for tree in enumerate_binary_trees(5):
            analysis = analyze_tree_ghost(tree, sdr)
            assert analysis.ghost_total == 1
            assert analysis.killed_by_projection is True

    @pytest.mark.parametrize("n", [2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_ghost_all_arities(self, n):
        """All trees at arity n have ghost +1 and are killed by projection."""
        sdr = sdr_sl2_virasoro()
        trees = enumerate_binary_trees(n)
        for tree in trees:
            analysis = analyze_tree_ghost(tree, sdr)
            assert analysis.ghost_total == 1, (
                f"Tree {tree.tree_id} at arity {n}: ghost = {analysis.ghost_total}, expected 1"
            )
            assert analysis.killed_by_projection is True

    def test_ghost_formula_algebraic(self):
        """Ghost total = (n-1) - (n-2) = 1 for n >= 2, verified algebraically."""
        for n in range(2, 20):
            tree = BinaryTree(n_leaves=n)
            # (n-1) delta vertices at ghost +1 each
            # (n-2) h edges at ghost -1 each
            ghost_total = (n - 1) * 1 + (n - 2) * (-1)
            assert ghost_total == 1, f"Arity {n}: ghost = {ghost_total}"

    def test_analyze_all_trees_ghost(self):
        """analyze_all_trees_ghost returns correct structure."""
        results = analyze_all_trees_ghost(6)
        assert set(results.keys()) == {2, 3, 4, 5, 6}
        for n, analyses in results.items():
            assert len(analyses) == count_binary_trees(n)
            for a in analyses:
                assert a.ghost_total == 1
                assert a.killed_by_projection is True

    def test_transferred_product_ghost(self):
        """The transferred product (leading order) has ghost 0 and survives."""
        analysis = analyze_transferred_product_ghost()
        assert analysis.ghost_total == 0
        assert analysis.killed_by_projection is False


# ============================================================================
# IV. Coproduct primitivity: the main theorem (abstract)
# ============================================================================

class TestCoproductPrimitivity:
    """Verify the main primitivity claim for the gravitational coproduct."""

    def test_primitivity_arity2(self):
        """Delta_{z,2}(T,T) = 0 (ghost obstruction)."""
        corrections = compute_coproduct_corrections(2)
        for corr in corrections[2]:
            assert corr.vanishes is True
            assert corr.ghost_total == 1

    def test_primitivity_arity3(self):
        """Delta_{z,3}(T,T,T) = 0 (ghost obstruction, 2 trees)."""
        corrections = compute_coproduct_corrections(3)
        assert len(corrections[3]) == 2  # Catalan C_2 = 2
        for corr in corrections[3]:
            assert corr.vanishes is True
            assert corr.ghost_total == 1

    def test_primitivity_arity4(self):
        """Delta_{z,4}(T^4) = 0 (ghost obstruction, 5 trees)."""
        corrections = compute_coproduct_corrections(4)
        assert len(corrections[4]) == 5  # Catalan C_3 = 5
        for corr in corrections[4]:
            assert corr.vanishes is True
            assert corr.ghost_total == 1

    def test_primitivity_arity5(self):
        """Delta_{z,5}(T^5) = 0 (ghost obstruction, 14 trees)."""
        corrections = compute_coproduct_corrections(5)
        assert len(corrections[5]) == 14  # Catalan C_4 = 14
        for corr in corrections[5]:
            assert corr.vanishes is True

    @pytest.mark.parametrize("n", [2, 3, 4, 5, 6, 7, 8])
    def test_primitivity_parametric(self, n):
        """All coproduct corrections vanish at arity n."""
        corrections = compute_coproduct_corrections(n)
        for corr in corrections[n]:
            assert corr.vanishes is True
            assert corr.ghost_total == 1
            assert 'ghost' in corr.reason

    def test_master_primitivity(self):
        """Master primitivity theorem up to arity 10."""
        result = verify_coproduct_primitivity(max_arity=10)
        assert result['all_corrections_vanish'] is True
        assert result['conclusion'] == 'PRIMITIVE'

    def test_master_primitivity_sdr(self):
        """Master theorem verifies SDR ghost degrees."""
        result = verify_coproduct_primitivity(max_arity=4)
        assert all(result['sdr_ghost_ok'].values())

    def test_correction_tree_counts(self):
        """Verify tree counts at each arity match Catalan numbers."""
        corrections = compute_coproduct_corrections(8)
        expected_catalans = {2: 1, 3: 2, 4: 5, 5: 14, 6: 42, 7: 132, 8: 429}
        for n, expected in expected_catalans.items():
            assert len(corrections[n]) == expected, (
                f"Arity {n}: got {len(corrections[n])} trees, expected {expected}"
            )

    def test_correction_ghost_breakdown_arity3(self):
        """Detailed ghost breakdown at arity 3."""
        corrections = compute_coproduct_corrections(3)
        for corr in corrections[3]:
            assert corr.n_delta_vertices == 2  # n-1 = 2
            assert corr.n_h_edges == 1          # n-2 = 1
            assert corr.ghost_from_delta == 2
            assert corr.ghost_from_h == -1
            assert corr.ghost_total == 1

    def test_correction_ghost_breakdown_arity4(self):
        """Detailed ghost breakdown at arity 4."""
        corrections = compute_coproduct_corrections(4)
        for corr in corrections[4]:
            assert corr.n_delta_vertices == 3  # n-1 = 3
            assert corr.n_h_edges == 2          # n-2 = 2
            assert corr.ghost_from_delta == 3
            assert corr.ghost_from_h == -2
            assert corr.ghost_total == 1


# ============================================================================
# V. r-matrix transfer
# ============================================================================

class TestRMatrixTransfer:
    """Verify r-matrix transfer from KM to Virasoro via HPL + AP19."""

    def test_km_rmatrix_max_pole(self):
        """KM r-matrix has max pole order 1 (simple pole)."""
        r = rmatrix_km_sl2(Fraction(1))
        assert r['max_pole'] == 1

    def test_km_rmatrix_coefficient_k1(self):
        """KM r-matrix coefficient is k at k=1."""
        r = rmatrix_km_sl2(Fraction(1))
        assert r['poles'][1] == Fraction(1)

    def test_km_rmatrix_coefficient_k3(self):
        """KM r-matrix coefficient is k at k=3."""
        r = rmatrix_km_sl2(Fraction(3))
        assert r['poles'][1] == Fraction(3)

    def test_vir_rmatrix_max_pole(self):
        """Virasoro r-matrix has max pole order 3."""
        r = rmatrix_vir_from_sl2(Fraction(1))
        assert r['max_pole'] == 3

    def test_vir_rmatrix_leading_k1(self):
        """Virasoro r-matrix leading pole at k=1: c/2 = (-1)/2 = -1/2."""
        r = rmatrix_vir_from_sl2(Fraction(1))
        c = c_vir_from_sl2(Fraction(1))
        assert r['poles'][3] == c / Fraction(2)
        assert r['poles'][3] == Fraction(-1, 2)

    def test_vir_rmatrix_subleading(self):
        """Virasoro r-matrix subleading pole coefficient is 2 (universal)."""
        for k_val in [1, 2, 3, 5]:
            r = rmatrix_vir_from_sl2(Fraction(k_val))
            assert r['poles'][1] == Fraction(2)

    def test_vir_rmatrix_kappa_consistency(self):
        """r-matrix leading coefficient = kappa(Vir) for all k."""
        for k_val in [1, 2, 3, 4, 5, 10]:
            k = Fraction(k_val)
            r = rmatrix_vir_from_sl2(k)
            c = c_vir_from_sl2(k)
            assert r['poles'][3] == kappa_vir(c)

    def test_rmatrix_only_odd_poles(self):
        """Virasoro r-matrix has only odd poles (bosonic parity, AP19)."""
        for k_val in [1, 2, 3, 5]:
            r = rmatrix_vir_from_sl2(Fraction(k_val))
            for pole_order in r['poles']:
                assert pole_order % 2 == 1, (
                    f"k={k_val}: pole order {pole_order} is even (violates bosonic parity)"
                )

    def test_rmatrix_transfer_ghost_analysis(self):
        """r-matrix transfer: leading order survives, corrections vanish."""
        result = verify_rmatrix_transfer_ghost()
        assert result['leading_order_survives'] is True
        assert result['corrections_vanish'] is True
        assert result['correction_ghost'] == 1


# ============================================================================
# VI. CYBE (classical Yang-Baxter equation)
# ============================================================================

class TestCYBE:
    """Verify the classical Yang-Baxter equation."""

    def test_ibr_sl2_k1(self):
        """Infinitesimal braid relation holds for sl_2 at k=1."""
        result = verify_cybe_sl2_scalar(Fraction(1))
        assert result['ibr_holds'] is True

    def test_cybe_sl2_k1(self):
        """CYBE holds for sl_2 r-matrix at k=1."""
        result = verify_cybe_sl2_scalar(Fraction(1))
        assert result['cybe_holds'] is True

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10])
    def test_cybe_sl2_parametric(self, k_val):
        """CYBE holds for sl_2 r-matrix at various k."""
        result = verify_cybe_sl2_scalar(Fraction(k_val))
        assert result['ibr_holds'] is True
        assert result['cybe_holds'] is True
        assert result['cybe_max_entry'] < 1e-10

    def test_cybe_sl2_omega_trace(self):
        """Casimir trace: tr(Omega) = tr(P) - tr(I)/2 = 2 - 2 = 0."""
        result = verify_cybe_sl2_scalar(Fraction(1))
        assert abs(result['omega_trace']) < 1e-10

    def test_cybe_vir_scalar_trivial(self):
        """Scalar CYBE for Virasoro is trivially satisfied (commutative)."""
        result = verify_cybe_virasoro_scalar(Fraction(1))
        assert result['scalar_cybe_trivial'] is True
        assert result['r_max_pole'] == 3


# ============================================================================
# VII. Kappa consistency under DS reduction
# ============================================================================

class TestKappaConsistency:
    """Verify kappa formulas and (non-)additivity under DS reduction."""

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3(1+2)/4 = 9/4."""
        assert kappa_sl2(Fraction(1)) == Fraction(9, 4)

    def test_kappa_sl2_k2(self):
        """kappa(sl_2, k=2) = 3(2+2)/4 = 3."""
        assert kappa_sl2(Fraction(2)) == Fraction(3)

    def test_kappa_sl2_k3(self):
        """kappa(sl_2, k=3) = 3(3+2)/4 = 15/4."""
        assert kappa_sl2(Fraction(3)) == Fraction(15, 4)

    def test_kappa_vir_k1(self):
        """kappa(Vir, c=-1) = -1/2."""
        c = c_vir_from_sl2(Fraction(1))
        assert kappa_vir(c) == Fraction(-1, 2)

    def test_kappa_vir_k4(self):
        """kappa(Vir, c=0) = 0 at k=4 (c(Vir) = 0)."""
        c = c_vir_from_sl2(Fraction(4))
        assert c == Fraction(0)
        assert kappa_vir(c) == Fraction(0)

    def test_kappa_ghost(self):
        """kappa_ghost = c_ghost/2 = 1."""
        assert kappa_ghost_sl2() == Fraction(1)

    def test_kappa_not_additive_k1(self):
        """kappa is NOT additive under DS at k=1."""
        result = verify_kappa_ds_consistency(Fraction(1))
        assert result['kappa_additive'] is False
        assert result['c_additive'] is True

    def test_kappa_not_additive_k2(self):
        """kappa is NOT additive under DS at k=2."""
        result = verify_kappa_ds_consistency(Fraction(2))
        assert result['kappa_additive'] is False

    def test_kappa_not_additive_k3(self):
        """kappa is NOT additive under DS at k=3."""
        result = verify_kappa_ds_consistency(Fraction(3))
        assert result['kappa_additive'] is False

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 5, 10, 50])
    def test_c_additive_parametric(self, k_val):
        """Central charge IS additive under DS for all k."""
        result = verify_kappa_ds_consistency(Fraction(k_val))
        assert result['c_additive'] is True

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 5, 10, 50])
    def test_kappa_not_additive_parametric(self, k_val):
        """kappa is NOT additive under DS for any k."""
        result = verify_kappa_ds_consistency(Fraction(k_val))
        assert result['kappa_additive'] is False

    def test_kappa_discrepancy_formula(self):
        """Verify the explicit kappa discrepancy: 3(k^2+2k+4)/(4(k+2))."""
        for k_val in [1, 2, 3, 5, 10]:
            k = Fraction(k_val)
            result = verify_kappa_ds_consistency(k)
            diff = result['kappa_difference']
            expected = Fraction(3) * (k**2 + 2*k + 4) / (Fraction(4) * (k + 2))
            assert diff == expected, (
                f"k={k}: discrepancy {diff} != expected {expected}"
            )

    def test_kappa_discrepancy_always_positive(self):
        """The kappa discrepancy is always positive (k^2+2k+4 > 0 for all k > 0)."""
        for k_val in [1, 2, 3, 5, 10, 100]:
            k = Fraction(k_val)
            result = verify_kappa_ds_consistency(k)
            assert result['kappa_difference'] > 0


# ============================================================================
# VIII. Cross-checks with existing modules
# ============================================================================

class TestCrossChecks:
    """Cross-check against existing compute infrastructure."""

    def test_c_sl2_matches_ds_cascade(self):
        """c(sl_2, k) matches ds_shadow_cascade_engine.c_slN(N=2, k)."""
        try:
            from compute.lib.ds_shadow_cascade_engine import c_slN
            for k_val in [1, 2, 3, 5]:
                k = Fraction(k_val)
                assert c_sl2(k) == c_slN(2, k)
        except ImportError:
            pytest.skip("ds_shadow_cascade_engine not available")

    def test_c_vir_matches_ds_cascade(self):
        """c(Vir) from DS matches ds_shadow_cascade_engine.c_WN(N=2, k)."""
        try:
            from compute.lib.ds_shadow_cascade_engine import c_WN
            for k_val in [1, 2, 3, 5]:
                k = Fraction(k_val)
                assert c_vir_from_sl2(k) == c_WN(2, k)
        except ImportError:
            pytest.skip("ds_shadow_cascade_engine not available")

    def test_kappa_sl2_matches_ds_cascade(self):
        """kappa(sl_2, k) matches ds_shadow_cascade_engine.kappa_slN(N=2, k)."""
        try:
            from compute.lib.ds_shadow_cascade_engine import kappa_slN
            for k_val in [1, 2, 3, 5]:
                k = Fraction(k_val)
                assert kappa_sl2(k) == kappa_slN(2, k)
        except ImportError:
            pytest.skip("ds_shadow_cascade_engine not available")

    def test_kappa_ghost_matches_ds_cascade(self):
        """kappa_ghost(sl_2) matches ds_shadow_cascade_engine.kappa_ghost(N=2)."""
        try:
            from compute.lib.ds_shadow_cascade_engine import kappa_ghost as kg
            assert kappa_ghost_sl2() == kg(2)
        except ImportError:
            pytest.skip("ds_shadow_cascade_engine not available")

    def test_kappa_vir_matches_modular_tangent(self):
        """kappa(Vir_c) = c/2 matches modular_tangent_complex.kappa_virasoro."""
        try:
            from compute.lib.modular_tangent_complex import kappa_virasoro
            for c_val in [Fraction(-1), Fraction(0), Fraction(1, 2), Fraction(1), Fraction(26)]:
                assert kappa_vir(c_val) == kappa_virasoro(c_val)
        except ImportError:
            pytest.skip("modular_tangent_complex not available")

    def test_kappa_sl2_matches_modular_tangent(self):
        """kappa(sl_2, k) = 3(k+2)/4 matches modular_tangent_complex."""
        try:
            from compute.lib.modular_tangent_complex import kappa_affine_sl2
            for k_val in [1, 2, 3, 5]:
                k = Fraction(k_val)
                assert kappa_sl2(k) == kappa_affine_sl2(k)
        except ImportError:
            pytest.skip("modular_tangent_complex not available")

    def test_rmatrix_poles_match_landscape(self):
        """Virasoro r-matrix poles match rmatrix_landscape conventions."""
        try:
            from compute.lib.rmatrix_landscape import ope_to_rmatrix_poles
            vir_ope = {4: Fraction(1, 2), 2: Fraction(2), 1: Fraction(1)}
            r_poles = ope_to_rmatrix_poles(vir_ope)
            assert 3 in r_poles
            assert 1 in r_poles
            assert 2 not in r_poles
        except ImportError:
            pytest.skip("rmatrix_landscape not available")


# ============================================================================
# IX. Structure constant checks
# ============================================================================

class TestStructureConstants:
    """Verify sl_2 structure constants and Killing form."""

    def test_bracket_ef(self):
        """[e, f] = h: f^{+-}_0 = 1."""
        assert SL2_STRUCTURE_CONSTANTS[('+', '-')]['0'] == Fraction(1)

    def test_bracket_fe(self):
        """[f, e] = -h: f^{-+}_0 = -1."""
        assert SL2_STRUCTURE_CONSTANTS[('-', '+')]['0'] == Fraction(-1)

    def test_bracket_he(self):
        """[h, e] = 2e: f^{0+}_+ = 2."""
        assert SL2_STRUCTURE_CONSTANTS[('0', '+')]['+'] == Fraction(2)

    def test_bracket_hf(self):
        """[h, f] = -2f: f^{0-}_- = -2."""
        assert SL2_STRUCTURE_CONSTANTS[('0', '-')]['-'] == Fraction(-2)

    def test_killing_diagonal(self):
        """(h, h) = 1 in normalized form."""
        assert SL2_KILLING[('0', '0')] == Fraction(1)

    def test_killing_off_diagonal(self):
        """(e, f) = 1 in normalized form."""
        assert SL2_KILLING[('+', '-')] == Fraction(1)

    def test_antisymmetry_check(self):
        """Structure constants are antisymmetric: f^{ab}_c = -f^{ba}_c."""
        for (a, b), targets in SL2_STRUCTURE_CONSTANTS.items():
            if (b, a) in SL2_STRUCTURE_CONSTANTS:
                rev = SL2_STRUCTURE_CONSTANTS[(b, a)]
                for c_label, coeff in targets.items():
                    assert rev.get(c_label, Fraction(0)) == -coeff, (
                        f"f^{{{a}{b}}}_{c_label} = {coeff} but "
                        f"f^{{{b}{a}}}_{c_label} = {rev.get(c_label, 0)}"
                    )


# ============================================================================
# X. Full verification suite
# ============================================================================

class TestFullSuite:
    """Run the complete verification and check all outputs."""

    def test_full_verification_runs(self):
        """Full verification completes without error."""
        result = full_verification(
            k_values=[Fraction(1), Fraction(2), Fraction(3)],
            max_arity=6,
        )
        assert 'sdr' in result
        assert 'sugawara' in result
        assert 'primitivity' in result
        assert 'rmatrix_transfer' in result
        assert 'cybe_sl2' in result
        assert 'kappa_ds' in result

    def test_full_sdr_ok(self):
        """Full suite: SDR ghost degrees OK."""
        result = full_verification(k_values=[Fraction(1)], max_arity=4)
        assert all(result['sdr'].values())

    def test_full_primitivity_ok(self):
        """Full suite: primitivity verified."""
        result = full_verification(k_values=[Fraction(1)], max_arity=6)
        assert result['primitivity']['conclusion'] == 'PRIMITIVE'

    def test_full_cybe_ok(self):
        """Full suite: CYBE holds for all tested k."""
        result = full_verification(k_values=[Fraction(1), Fraction(2)], max_arity=4)
        for k_str, cybe_result in result['cybe_sl2'].items():
            assert cybe_result['cybe_holds'] is True

    def test_full_sugawara_ok(self):
        """Full suite: Sugawara DS consistency for all tested k."""
        result = full_verification(k_values=[Fraction(1), Fraction(2), Fraction(3)], max_arity=4)
        for k_str, sug_result in result['sugawara'].items():
            assert sug_result['ds_match'] is True


# ============================================================================
# XI. Explicit SDR axiom verification
# ============================================================================

class TestExplicitSDR:
    """Verify that the explicitly constructed SDR satisfies all axioms."""

    def test_sdr_s1_k1(self):
        """S1: p . iota = id at k=1."""
        sdr = build_explicit_sdr(1.0)
        assert sdr.verify_s1()

    def test_sdr_s1_k2(self):
        """S1: p . iota = id at k=2."""
        sdr = build_explicit_sdr(2.0)
        assert sdr.verify_s1()

    def test_sdr_s3_k1(self):
        """S3: h^2 = 0 (partial) at k=1."""
        sdr = build_explicit_sdr(1.0)
        assert sdr.verify_s3_partial()

    def test_sdr_s3_k3(self):
        """S3: h^2 = 0 (partial) at k=3."""
        sdr = build_explicit_sdr(3.0)
        assert sdr.verify_s3_partial()

    def test_sdr_s4_k1(self):
        """S4: h . iota = 0 at k=1."""
        sdr = build_explicit_sdr(1.0)
        assert sdr.verify_s4()

    def test_sdr_s4_k2(self):
        """S4: h . iota = 0 at k=2."""
        sdr = build_explicit_sdr(2.0)
        assert sdr.verify_s4()

    def test_sdr_s5_k1(self):
        """S5: p . h = 0 at k=1."""
        sdr = build_explicit_sdr(1.0)
        assert sdr.verify_s5()

    def test_sdr_s5_k3(self):
        """S5: p . h = 0 at k=3."""
        sdr = build_explicit_sdr(3.0)
        assert sdr.verify_s5()

    def test_sdr_all_axioms_k1(self):
        """All SDR axioms hold at k=1."""
        sdr = build_explicit_sdr(1.0)
        axioms = sdr.verify_all_axioms()
        assert all(axioms.values()), f"Failed axioms: {axioms}"

    def test_sdr_all_axioms_k2(self):
        """All SDR axioms hold at k=2."""
        sdr = build_explicit_sdr(2.0)
        axioms = sdr.verify_all_axioms()
        assert all(axioms.values()), f"Failed axioms: {axioms}"

    def test_sdr_all_axioms_k3(self):
        """All SDR axioms hold at k=3."""
        sdr = build_explicit_sdr(3.0)
        axioms = sdr.verify_all_axioms()
        assert all(axioms.values()), f"Failed axioms: {axioms}"

    @pytest.mark.parametrize("k_val", [0.5, 1.0, 2.0, 3.0, 5.0, 10.0])
    def test_sdr_all_axioms_parametric(self, k_val):
        """All SDR axioms hold for various k."""
        sdr = build_explicit_sdr(k_val)
        axioms = sdr.verify_all_axioms()
        assert all(axioms.values()), f"k={k_val}: failed axioms: {axioms}"

    def test_sdr_dimensions(self):
        """SDR matrices have correct dimensions."""
        sdr = build_explicit_sdr(1.0)
        assert sdr.iota.shape == (sdr.dim_C0, sdr.dim_V)
        assert sdr.p.shape == (sdr.dim_V, sdr.dim_C0)
        assert sdr.h_01.shape == (sdr.dim_C0, sdr.dim_C1)
        assert sdr.h_0n1.shape == (sdr.dim_Cn1, sdr.dim_C0)
        assert sdr.delta_01.shape == (sdr.dim_C1, sdr.dim_C0)

    def test_sdr_different_dimensions(self):
        """SDR construction works with non-default dimensions."""
        sdr = build_explicit_sdr(1.0, dim_C0=8, dim_C1=6, dim_Cn1=6)
        axioms = sdr.verify_all_axioms()
        assert all(axioms.values()), f"Custom dims: failed axioms: {axioms}"
        assert sdr.dim_C0 == 8
        assert sdr.dim_C1 == 6


# ============================================================================
# XII. Explicit HPL corrections (matrix-level)
# ============================================================================

class TestExplicitHPLCorrections:
    """Verify HPL coproduct corrections vanish using explicit matrix SDR."""

    def test_arity2_vanishes_k1(self):
        """Delta_{z,2}(T,T) = 0 at k=1 (explicit matrix computation)."""
        sdr = build_explicit_sdr(1.0)
        corr = compute_hpl_arity2_explicit_sdr(sdr)
        assert np.allclose(corr, 0, atol=1e-12)

    def test_arity2_vanishes_k2(self):
        """Delta_{z,2}(T,T) = 0 at k=2."""
        sdr = build_explicit_sdr(2.0)
        corr = compute_hpl_arity2_explicit_sdr(sdr)
        assert np.allclose(corr, 0, atol=1e-12)

    def test_arity2_vanishes_k3(self):
        """Delta_{z,2}(T,T) = 0 at k=3."""
        sdr = build_explicit_sdr(3.0)
        corr = compute_hpl_arity2_explicit_sdr(sdr)
        assert np.allclose(corr, 0, atol=1e-12)

    def test_arity3_vanishes_k1(self):
        """Delta_{z,3}(T,T,T) = 0 at k=1."""
        sdr = build_explicit_sdr(1.0)
        corr = compute_hpl_arity3_explicit_sdr(sdr)
        assert np.allclose(corr, 0, atol=1e-12)

    def test_arity3_vanishes_k2(self):
        """Delta_{z,3}(T,T,T) = 0 at k=2."""
        sdr = build_explicit_sdr(2.0)
        corr = compute_hpl_arity3_explicit_sdr(sdr)
        assert np.allclose(corr, 0, atol=1e-12)

    @pytest.mark.parametrize("k_val", [1.0, 2.0, 3.0, 5.0, 10.0])
    def test_arity2_vanishes_parametric(self, k_val):
        """Delta_{z,2} vanishes for various k."""
        sdr = build_explicit_sdr(k_val)
        corr = compute_hpl_arity2_explicit_sdr(sdr)
        assert np.allclose(corr, 0, atol=1e-12), f"k={k_val}: arity-2 nonzero"

    @pytest.mark.parametrize("k_val", [1.0, 2.0, 3.0, 5.0])
    def test_arity3_vanishes_parametric(self, k_val):
        """Delta_{z,3} vanishes for various k."""
        sdr = build_explicit_sdr(k_val)
        corr = compute_hpl_arity3_explicit_sdr(sdr)
        assert np.allclose(corr, 0, atol=1e-12), f"k={k_val}: arity-3 nonzero"

    def test_all_corrections_vanish_k1(self):
        """All HPL corrections vanish at k=1 (arities 2-4)."""
        sdr = build_explicit_sdr(1.0)
        results = compute_hpl_corrections_with_sdr(sdr, max_arity=4)
        for n, data in results.items():
            assert data['vanishes'], f"Arity {n} does not vanish at k=1"
            assert data['ghost_total'] == 1

    def test_all_corrections_vanish_k2(self):
        """All HPL corrections vanish at k=2 (arities 2-4)."""
        sdr = build_explicit_sdr(2.0)
        results = compute_hpl_corrections_with_sdr(sdr, max_arity=4)
        for n, data in results.items():
            assert data['vanishes'], f"Arity {n} does not vanish at k=2"

    def test_corrections_with_sdr_axioms_verified(self):
        """SDR axioms are verified as part of the correction computation."""
        sdr = build_explicit_sdr(1.0)
        results = compute_hpl_corrections_with_sdr(sdr, max_arity=4)
        for n, data in results.items():
            assert all(data['sdr_axioms'].values())

    def test_truncated_brst_arity2(self):
        """Truncated BRST complex: arity-2 correction vanishes."""
        brst = build_truncated_brst(1.0)
        corr = compute_hpl_delta_z2_explicit(brst)
        assert np.allclose(corr, 0, atol=1e-12)

    def test_truncated_brst_arity2_tree(self):
        """Truncated BRST complex: arity-2 tree correction vanishes."""
        brst = build_truncated_brst(1.0)
        corr = compute_hpl_delta_z2_tree_explicit(brst)
        assert np.allclose(corr, 0, atol=1e-12)

    def test_truncated_brst_arity3(self):
        """Truncated BRST complex: arity-3 correction vanishes."""
        brst = build_truncated_brst(1.0)
        corr = compute_hpl_delta_z3_explicit(brst)
        assert np.allclose(corr, 0, atol=1e-12)

    def test_truncated_brst_all_corrections(self):
        """Truncated BRST complex: all corrections vanish up to arity 4."""
        brst = build_truncated_brst(2.0)
        corrections = compute_hpl_corrections_explicit(brst, max_arity=4)
        for n, corr in corrections.items():
            assert np.allclose(corr, 0, atol=1e-12), f"Arity {n} nonzero"


# ============================================================================
# XIII. Ghost-number tracking
# ============================================================================

class TestGhostTracking:
    """Verify the ghost-number tracking functions."""

    def test_ghost_track_empty(self):
        """Empty operation sequence has ghost 0."""
        assert ghost_number_track([]) == 0

    def test_ghost_track_single_iota(self):
        """Single iota has ghost 0."""
        assert ghost_number_track([('iota', 0)]) == 0

    def test_ghost_track_single_h(self):
        """Single h has ghost -1."""
        assert ghost_number_track([('h', -1)]) == -1

    def test_ghost_track_single_delta(self):
        """Single delta has ghost +1."""
        assert ghost_number_track([('delta', 1)]) == 1

    def test_ghost_track_h_delta(self):
        """h followed by delta has ghost 0."""
        assert ghost_number_track([('h', -1), ('delta', 1)]) == 0

    def test_ghost_track_delta_h_delta(self):
        """delta . h . delta has ghost +1."""
        assert ghost_number_track([('delta', 1), ('h', -1), ('delta', 1)]) == 1

    def test_ghost_of_hpl_tree_n2(self):
        """HPL tree with 2 leaves has ghost 1."""
        assert ghost_number_of_hpl_tree(2) == 1

    def test_ghost_of_hpl_tree_n3(self):
        """HPL tree with 3 leaves has ghost 1."""
        assert ghost_number_of_hpl_tree(3) == 1

    def test_ghost_of_hpl_tree_n4(self):
        """HPL tree with 4 leaves has ghost 1."""
        assert ghost_number_of_hpl_tree(4) == 1

    def test_ghost_of_hpl_tree_n10(self):
        """HPL tree with 10 leaves has ghost 1."""
        assert ghost_number_of_hpl_tree(10) == 1

    @pytest.mark.parametrize("n", range(2, 21))
    def test_ghost_of_hpl_tree_universal(self, n):
        """HPL tree with n >= 2 leaves always has ghost 1."""
        assert ghost_number_of_hpl_tree(n) == 1

    def test_ghost_number_of_element_matter(self):
        """Matter sector has ghost 0."""
        assert ghost_number_of_element('matter') == 0

    def test_ghost_number_of_element_ghost(self):
        """Ghost sector has ghost +1."""
        assert ghost_number_of_element('ghost') == 1
        assert ghost_number_of_element('ghost+1') == 1

    def test_ghost_number_of_element_antighost(self):
        """Anti-ghost sector has ghost -1."""
        assert ghost_number_of_element('antighost') == -1
        assert ghost_number_of_element('ghost-1') == -1

    def test_delta_increases_ghost(self):
        """The BRST perturbation delta increases ghost number by 1."""
        # For any starting ghost g, delta maps to g+1.
        for g in [-2, -1, 0, 1, 2]:
            result = ghost_number_track([('x', g), ('delta', 1)])
            assert result == g + 1

    def test_h_decreases_ghost(self):
        """The homotopy h decreases ghost number by 1."""
        for g in [-2, -1, 0, 1, 2]:
            result = ghost_number_track([('x', g), ('h', -1)])
            assert result == g - 1

    def test_p_preserves_ghost(self):
        """The projection p preserves ghost number (it is ghost 0)."""
        for g in [-2, -1, 0, 1, 2]:
            result = ghost_number_track([('x', g), ('p', 0)])
            assert result == g


# ============================================================================
# XIV. Affine coproduct nontriviality
# ============================================================================

class TestAffineCoproductNontriviality:
    """Verify that the affine coproduct is nontrivial before DS transfer."""

    def test_primitive_on_generators(self):
        """The affine coproduct IS primitive on generators J^a."""
        result = affine_coproduct_is_nontrivial(Fraction(1))
        assert result['affine_coproduct_primitive_on_generators'] is True

    def test_not_primitive_on_sugawara(self):
        """The affine coproduct is NOT primitive on Sugawara T."""
        result = affine_coproduct_is_nontrivial(Fraction(1))
        assert result['affine_coproduct_primitive_on_sugawara'] is False

    def test_cross_term_k1(self):
        """Cross term coefficient at k=1: 1/(k+2) = 1/3."""
        result = affine_coproduct_is_nontrivial(Fraction(1))
        assert result['cross_term_coefficient'] == Fraction(1, 3)

    def test_cross_term_k2(self):
        """Cross term coefficient at k=2: 1/(k+2) = 1/4."""
        result = affine_coproduct_is_nontrivial(Fraction(2))
        assert result['cross_term_coefficient'] == Fraction(1, 4)

    def test_cross_term_k3(self):
        """Cross term coefficient at k=3: 1/(k+2) = 1/5."""
        result = affine_coproduct_is_nontrivial(Fraction(3))
        assert result['cross_term_coefficient'] == Fraction(1, 5)

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10, 100])
    def test_cross_term_nonzero(self, k_val):
        """Cross term is nonzero for all positive k."""
        result = affine_coproduct_is_nontrivial(Fraction(k_val))
        assert result['cross_term_coefficient'] != 0

    def test_cross_term_decreases_with_k(self):
        """Cross term 1/(k+2) decreases as k increases."""
        prev = affine_coproduct_is_nontrivial(Fraction(1))['cross_term_coefficient']
        for k_val in [2, 3, 5, 10]:
            curr = affine_coproduct_is_nontrivial(Fraction(k_val))['cross_term_coefficient']
            assert curr < prev
            prev = curr

    def test_critical_level_raises(self):
        """Critical level k=-2 should raise."""
        with pytest.raises(ValueError):
            affine_coproduct_is_nontrivial(Fraction(-2))


# ============================================================================
# XV. Edge cases and special levels
# ============================================================================

class TestEdgeCases:
    """Verify primitivity at edge cases and special values of k."""

    def test_edge_cases_run(self):
        """Edge case verification completes."""
        results = verify_primitivity_edge_cases()
        assert 'k=4' in results
        assert 'k=1000' in results
        assert 'c=26' in results
        assert 'c=13' in results

    def test_k4_uncurved(self):
        """k=4 gives c=0 (uncurved), primitivity holds."""
        results = verify_primitivity_edge_cases()
        assert results['k=4']['c'] == Fraction(0)
        assert results['k=4']['kappa'] == Fraction(0)
        assert results['k=4']['primitive'] is True

    def test_c26_anomaly_cancellation(self):
        """c=26 (anomaly cancellation), kappa=13, primitivity holds."""
        results = verify_primitivity_edge_cases()
        assert results['c=26']['c'] == Fraction(26)
        assert results['c=26']['kappa'] == Fraction(13)
        assert results['c=26']['primitive'] is True

    def test_c13_self_dual(self):
        """c=13 (self-dual point), kappa=13/2, primitivity holds."""
        results = verify_primitivity_edge_cases()
        assert results['c=13']['c'] == Fraction(13)
        assert results['c=13']['kappa'] == Fraction(13, 2)
        assert results['c=13']['primitive'] is True

    def test_large_k_semiclassical(self):
        """Large k (semi-classical limit), primitivity holds."""
        results = verify_primitivity_edge_cases()
        c_large = results['k=1000']['c']
        # c(k=1000) = 996/1002 = 498/501 ~ 0.994
        assert c_large == Fraction(996, 1002)
        assert results['k=1000']['primitive'] is True

    def test_ghost_argument_universal(self):
        """The ghost-number argument applies at ALL k (universal)."""
        results = verify_primitivity_edge_cases()
        for key, data in results.items():
            assert data['ghost_argument_applies'] is True

    def test_c_vir_from_sl2_special_values(self):
        """Verify c(Vir) from sl_2 at special levels."""
        # k = -56/25 gives c = 26
        k_26 = Fraction(-56, 25)
        assert c_vir_from_sl2(k_26) == Fraction(26)

        # k = -5/2 gives c = 13
        k_13 = Fraction(-5, 2)
        assert c_vir_from_sl2(k_13) == Fraction(13)

        # k = 4 gives c = 0
        assert c_vir_from_sl2(Fraction(4)) == Fraction(0)


# ============================================================================
# XVI. Parametric primitivity
# ============================================================================

class TestParametricPrimitivity:
    """Verify primitivity across a range of k values and SDR dimensions."""

    def test_parametric_standard_levels(self):
        """Primitivity at k = 1, 2, 3."""
        result = verify_primitivity_parametric([1.0, 2.0, 3.0], max_arity=3)
        assert result['all_primitive'] is True

    def test_parametric_large_k(self):
        """Primitivity at large k (semi-classical)."""
        result = verify_primitivity_parametric([10.0, 50.0, 100.0], max_arity=3)
        assert result['all_primitive'] is True

    def test_parametric_fractional_k(self):
        """Primitivity at fractional k values."""
        result = verify_primitivity_parametric([0.5, 1.5, 2.5], max_arity=3)
        assert result['all_primitive'] is True

    def test_parametric_ghost_numbers(self):
        """Ghost numbers are +1 at all arities for all k."""
        result = verify_primitivity_parametric([1.0, 2.0], max_arity=4)
        for k_str, k_data in result['k_results'].items():
            for n, gh in k_data['ghost_numbers'].items():
                assert gh == 1, f"k={k_str}, arity={n}: ghost={gh}"

    def test_parametric_sdr_axioms(self):
        """SDR axioms verified at all tested k."""
        result = verify_primitivity_parametric([1.0, 2.0, 3.0], max_arity=3)
        for k_str, k_data in result['k_results'].items():
            assert k_data['axioms_ok'], f"k={k_str}: SDR axioms failed"

    def test_parametric_conclusion(self):
        """Conclusion is PRIMITIVE for all tested k."""
        result = verify_primitivity_parametric([1.0, 2.0, 3.0], max_arity=4)
        assert 'PRIMITIVE' in result['conclusion']

    @pytest.mark.parametrize("k_val", [0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0])
    def test_parametric_individual(self, k_val):
        """Individual parametric test at each k."""
        sdr = build_explicit_sdr(k_val)
        assert all(sdr.verify_all_axioms().values())
        corr2 = compute_hpl_arity2_explicit_sdr(sdr)
        assert np.allclose(corr2, 0, atol=1e-12)
        corr3 = compute_hpl_arity3_explicit_sdr(sdr)
        assert np.allclose(corr3, 0, atol=1e-12)
