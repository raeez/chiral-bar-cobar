r"""Tests for Chern-Simons bar complex knot invariant engine.

Tests the chain: B(V_k(sl_N)) -> r-matrix -> R-matrix -> braid rep -> knot invariant.
This is the CFG [2602.12412] factorization homology trace in our framework.

Multi-path verification (CLAUDE.md mandate): every numerical claim verified by
at least 3 independent paths where possible.

Convention notes:
  - q = quantum parameter, t = q^2 for the Jones variable
  - Kassel normalization throughout
  - V_{3_1}(t) = -t^{-4} + t^{-3} + t^{-1} (trefoil Jones polynomial)
  - V_{4_1}(t) = t^2 - t + 1 - t^{-1} + t^{-2} (figure-eight Jones polynomial)
  - check_R eigenvalues: q (sym), -q^{-1} (anti) for sl_2 fundamental
  - kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N) (AP1, AP39)
"""

import cmath
import math

import numpy as np
import pytest

from compute.lib.theorem_cs_knot_invariant_engine import (
    cs_partition_function_s3,
    cs_kappa,
    cs_central_charge,
    factorization_trace_jones,
    factorization_trace_colored,
    factorization_trace_slN,
    jones_trefoil_exact,
    jones_trefoil_from_bar_rmatrix,
    jones_trefoil_from_homflypt,
    verify_trefoil_three_paths,
    colored_jones_unknot,
    verify_unknot_quantum_dimension,
    hopf_link_invariant,
    hopf_link_from_eigenvalues,
    linking_number_from_r_matrix,
    homflypt_trefoil_sl_N,
    verify_homflypt_skein,
    homflypt_jones_consistency,
    rt_invariant_at_level,
    bar_to_rmatrix_chain,
    figure_eight_invariants,
    torus_knot_jones,
    verify_mirror_symmetry,
    colored_jones_at_root,
    cs_bar_anomaly_data,
    verify_reidemeister_invariance,
    knot_invariant_table,
    cs_level_scan,
)


# =========================================================================
# Test parameters
# =========================================================================

# Generic q (not a root of unity, not close to 1)
Q_GENERIC = np.exp(0.3j)
Q_GENERIC_2 = np.exp(0.7j)

TOL = 1e-8


# =========================================================================
# 1. Trefoil: three-path verification
# =========================================================================

class TestTrefoilThreePaths:
    """Verify the trefoil Jones polynomial by 3 independent paths."""

    def test_trefoil_exact_formula(self):
        """Path 1: exact polynomial V_{3_1}(t) = -t^{-4} + t^{-3} + t^{-1}."""
        q = Q_GENERIC
        t = q * q
        val = jones_trefoil_exact(q)
        expected = -t**(-4) + t**(-3) + t**(-1)
        assert abs(val - expected) < TOL

    def test_trefoil_from_bar_rmatrix(self):
        """Path 2: bar-cobar R-matrix braid rep + quantum Markov trace."""
        q = Q_GENERIC
        val = jones_trefoil_from_bar_rmatrix(q)
        expected = jones_trefoil_exact(q)
        assert abs(val - expected) < TOL

    def test_trefoil_from_homflypt(self):
        """Path 3: HOMFLYPT at N=2 (independent code path)."""
        q = Q_GENERIC
        val = jones_trefoil_from_homflypt(q)
        expected = jones_trefoil_exact(q)
        assert abs(val - expected) < TOL

    def test_trefoil_three_path_convergence(self):
        """All three paths agree at two different q values."""
        for q in [Q_GENERIC, Q_GENERIC_2]:
            result = verify_trefoil_three_paths(q)
            assert result['all_agree'], (
                f"Three-path divergence at q={q}: "
                f"d12={result['discrepancy_12']:.2e}, "
                f"d13={result['discrepancy_13']:.2e}, "
                f"d23={result['discrepancy_23']:.2e}"
            )

    def test_trefoil_specific_value(self):
        """Trefoil at q = e^{i/3}: cross-check the numerical value."""
        q = np.exp(1j / 3.0)
        t = q * q
        exact = -t**(-4) + t**(-3) + t**(-1)
        from_braid = jones_trefoil_from_bar_rmatrix(q)
        assert abs(exact - from_braid) < TOL


# =========================================================================
# 2. Unknot: quantum dimension
# =========================================================================

class TestUnknotQuantumDimension:
    """Verify J_n(unknot; q) = [n]_q."""

    def test_unknot_color_1(self):
        """J_1(unknot; q) = [1]_q = 1."""
        val = colored_jones_unknot(1, Q_GENERIC)
        assert abs(val - 1.0) < TOL

    def test_unknot_color_2(self):
        """J_2(unknot; q) = [2]_q = q + q^{-1}."""
        q = Q_GENERIC
        val = colored_jones_unknot(2, q)
        expected = q + 1.0 / q
        assert abs(val - expected) < TOL

    def test_unknot_color_3(self):
        """J_3(unknot; q) = [3]_q = q^2 + 1 + q^{-2}."""
        q = Q_GENERIC
        val = colored_jones_unknot(3, q)
        expected = q**2 + 1 + q**(-2)
        assert abs(val - expected) < TOL

    def test_unknot_multipath(self):
        """Verify [n]_q by formula, sum, and trig (on unit circle)."""
        q = np.exp(0.5j)  # on unit circle
        result = verify_unknot_quantum_dimension(q, max_color=6)
        assert result['all_pass'], f"Unknot multipath failed: {result}"

    def test_unknot_classical_limit(self):
        """[n]_q -> n as q -> 1."""
        q = 1.0 + 1e-8j
        for n in range(1, 6):
            val = colored_jones_unknot(n, q)
            assert abs(val - n) < 1e-4, f"[{n}]_q = {val} != {n} at q~1"


# =========================================================================
# 3. Hopf link: linking number from R-matrix
# =========================================================================

class TestHopfLink:
    """Verify Hopf link invariants and linking number extraction."""

    def test_hopf_link_computed(self):
        """Hopf link invariant is nonzero at generic q."""
        val = hopf_link_invariant(Q_GENERIC, 2)
        assert abs(val) > 1e-10

    def test_hopf_link_eigenvalue_decomposition(self):
        """R-matrix eigenvalue decomposition gives correct Hopf invariant."""
        result = hopf_link_from_eigenvalues(Q_GENERIC)
        assert result['match'], (
            f"Eigenvalue vs braid mismatch: "
            f"{result['jones_hopf_from_eigenvalues']} vs "
            f"{result['jones_hopf_from_braid']}"
        )

    def test_linking_number(self):
        """Linking number of Hopf link = 1."""
        result = linking_number_from_r_matrix(Q_GENERIC)
        assert result['linking_number'] == 1

    def test_eigenvalue_ratio(self):
        """R-matrix eigenvalue ratio lambda_sym/lambda_anti = -q^2."""
        result = linking_number_from_r_matrix(Q_GENERIC)
        assert result['ratio_match'], (
            f"Ratio {result['eigenvalue_ratio']} != expected {result['expected_ratio']}"
        )

    def test_hopf_link_sl3(self):
        """Hopf link invariant for sl_3 is nonzero."""
        val = hopf_link_invariant(Q_GENERIC, 3)
        assert abs(val) > 1e-10


# =========================================================================
# 4. HOMFLYPT polynomial
# =========================================================================

class TestHOMFLYPT:
    """Verify HOMFLYPT polynomial from sl_N bar-cobar R-matrix."""

    def test_homflypt_trefoil_sl2(self):
        """HOMFLYPT at N=2 equals Jones for trefoil."""
        q = Q_GENERIC
        jones = jones_trefoil_from_bar_rmatrix(q)
        homfly = homflypt_trefoil_sl_N(q, 2)
        assert abs(jones - homfly) < TOL

    def test_homflypt_trefoil_sl3(self):
        """HOMFLYPT at N=3 for trefoil is nonzero."""
        val = homflypt_trefoil_sl_N(Q_GENERIC, 3)
        assert abs(val) > 1e-10

    def test_skein_relation_sl2(self):
        """Verify HOMFLYPT skein relation for sl_2."""
        result = verify_homflypt_skein(Q_GENERIC, 2)
        assert result['all_pass'], (
            f"Skein failed: hecke={result['hecke_residual']:.2e}, "
            f"skein={result['skein_residual']:.2e}, "
            f"braid={result['braid_residual']:.2e}, "
            f"link={result['link_skein_residual']:.2e}"
        )

    def test_skein_relation_sl3(self):
        """Verify HOMFLYPT skein relation for sl_3."""
        result = verify_homflypt_skein(Q_GENERIC, 3)
        assert result['all_pass']

    def test_homflypt_jones_consistency(self):
        """HOMFLYPT at N=2 recovers Jones for trefoil and figure-eight."""
        result = homflypt_jones_consistency(Q_GENERIC)
        assert result['all_pass'], (
            f"Consistency failed: {result['results']}"
        )


# =========================================================================
# 5. Figure-eight knot
# =========================================================================

class TestFigureEight:
    """Verify figure-eight knot invariants."""

    def test_figure_eight_exact(self):
        """V_{4_1}(t) = t^2 - t + 1 - t^{-1} + t^{-2}."""
        q = Q_GENERIC
        result = figure_eight_invariants(q)
        assert abs(result['exact'] - result['from_rmatrix']) < TOL

    def test_figure_eight_amphichiral(self):
        """4_1 is amphichiral: V(q) = V(1/q)."""
        result = figure_eight_invariants(Q_GENERIC)
        assert result['amphichiral'], (
            f"Amphichirality failed: disc={result['amphichiral_disc']:.2e}"
        )


# =========================================================================
# 6. CS partition function and kappa
# =========================================================================

class TestCSPartitionFunction:
    """Verify CS partition function and modular characteristic."""

    def test_cs_s3_sl2_k1(self):
        """Z(S^3, sl_2, k=1) = sqrt(2/3) * 2 sin(pi/3) = sqrt(2)."""
        z = cs_partition_function_s3(1, 2)
        assert abs(z - math.sqrt(2)) < TOL

    def test_cs_s3_sl2_k2(self):
        """Z(S^3, sl_2, k=2) = sqrt(1/2) * 2 sin(pi/4) = 1."""
        z = cs_partition_function_s3(2, 2)
        assert abs(z - 1.0) < TOL

    def test_kappa_sl2(self):
        """kappa(V_k(sl_2)) = 3(k+2)/4 (AP1)."""
        for k in range(1, 6):
            kappa = cs_kappa(k, 2)
            expected = 3.0 * (k + 2) / 4.0
            assert abs(kappa - expected) < TOL

    def test_kappa_ne_c_half_sl2(self):
        """kappa != c/2 for sl_2 at any finite level (AP39 for rank=1 is actually equality).

        For sl_2: kappa = 3(k+2)/4, c/2 = 3k/(2(k+2)).
        These are NOT equal for any k > 0.
        """
        for k in range(1, 6):
            kappa = cs_kappa(k, 2)
            c = cs_central_charge(k, 2)
            # For sl_2, kappa and c/2 are genuinely different
            assert abs(kappa - c / 2.0) > 0.1

    def test_kappa_sl3(self):
        """kappa(V_k(sl_3)) = 8(k+3)/6 = 4(k+3)/3."""
        for k in range(1, 6):
            kappa = cs_kappa(k, 3)
            expected = 8.0 * (k + 3) / 6.0
            assert abs(kappa - expected) < TOL

    def test_central_charge_sl2(self):
        """c(sl_2, k) = 3k/(k+2)."""
        for k in range(1, 6):
            c = cs_central_charge(k, 2)
            expected = 3.0 * k / (k + 2.0)
            assert abs(c - expected) < TOL


# =========================================================================
# 7. Bar-to-R-matrix chain
# =========================================================================

class TestBarToRMatrixChain:
    """Verify the full chain from bar complex to knot invariants."""

    def test_chain_sl2(self):
        """Full chain for sl_2 at generic q."""
        result = bar_to_rmatrix_chain(Q_GENERIC, 2)
        assert result['chain_complete'], (
            f"Chain incomplete: hecke={result['hecke_satisfied']}, "
            f"braid={result['braid_satisfied']}, "
            f"trefoil={result['trefoil_match']}"
        )

    def test_chain_sl3(self):
        """Full chain for sl_3 at generic q."""
        result = bar_to_rmatrix_chain(Q_GENERIC, 3)
        assert result['chain_complete']

    def test_classical_limit(self):
        """In the classical limit q -> 1, check_R -> P (permutation)."""
        result = bar_to_rmatrix_chain(1.0 + 1e-6, 2)
        # The rate of approach should be finite
        assert result['classical_limit_rate'] < 100, (
            f"Classical limit rate too large: {result['classical_limit_rate']}"
        )


# =========================================================================
# 8. RT invariants at roots of unity
# =========================================================================

class TestRTInvariant:
    """Verify RT invariants at CS levels."""

    def test_rt_trefoil_k1(self):
        """RT invariant of trefoil at level k=1."""
        result = rt_invariant_at_level("3_1", k=1, N=2, color=2)
        assert result['admissible']
        assert abs(result['rt_value']) > 1e-10

    def test_rt_trefoil_k2(self):
        """RT invariant of trefoil at level k=2."""
        result = rt_invariant_at_level("3_1", k=2, N=2, color=2)
        assert result['admissible']

    def test_colored_jones_root_unity(self):
        """Colored Jones at root of unity with admissibility check."""
        result = colored_jones_at_root("3_1", k=3, color=2)
        assert result['admissible']
        assert abs(result['quantum_dimension'].real) > 1e-10

    def test_inadmissible_color(self):
        """Color exceeding k+1 is inadmissible."""
        result = colored_jones_at_root("3_1", k=1, color=4)
        assert not result['admissible']


# =========================================================================
# 9. Mirror symmetry
# =========================================================================

class TestMirrorSymmetry:
    """Verify V_{K*}(q) = V_K(1/q)."""

    def test_mirror_trefoil(self):
        """Trefoil mirror relation."""
        result = verify_mirror_symmetry("3_1", Q_GENERIC)
        assert result['mirror_relation'], (
            f"Mirror failed for trefoil: disc={result['discrepancy']:.2e}"
        )

    def test_mirror_figure_eight(self):
        """Figure-eight mirror relation (amphichiral: V(q) = V(1/q))."""
        result = verify_mirror_symmetry("4_1", Q_GENERIC)
        assert result['mirror_relation']

    def test_mirror_51(self):
        """5_1 torus knot mirror relation."""
        result = verify_mirror_symmetry("5_1", Q_GENERIC)
        assert result['mirror_relation']


# =========================================================================
# 10. Reidemeister invariance
# =========================================================================

class TestReidemeister:
    """Verify topological invariance of the factorization homology trace."""

    def test_reidemeister_sl2(self):
        """R2 and R3 invariance for sl_2."""
        result = verify_reidemeister_invariance(Q_GENERIC, N=2)
        assert result['all_pass'], (
            f"Reidemeister failed: R2={result['R2_discrepancy']:.2e}, "
            f"R3={result['R3_discrepancy']:.2e}"
        )

    def test_reidemeister_sl3(self):
        """R2 and R3 invariance for sl_3."""
        result = verify_reidemeister_invariance(Q_GENERIC, N=3)
        assert result['all_pass']


# =========================================================================
# 11. Torus knots
# =========================================================================

class TestTorusKnots:
    """Verify torus knot invariants from bar-cobar R-matrix."""

    def test_torus_23_is_trefoil(self):
        """T(2,3) = trefoil."""
        q = Q_GENERIC
        torus = torus_knot_jones(2, 3, q)
        trefoil = jones_trefoil_from_bar_rmatrix(q)
        assert abs(torus['jones'] - trefoil) < TOL

    def test_torus_22_is_hopf(self):
        """T(2,2) = Hopf link."""
        q = Q_GENERIC
        torus = torus_knot_jones(2, 2, q)
        hopf = hopf_link_invariant(q, 2)
        assert abs(torus['jones'] - hopf) < TOL

    def test_torus_25_writhe(self):
        """T(2,5) has writhe 5."""
        result = torus_knot_jones(2, 5, Q_GENERIC)
        assert result['writhe'] == 5


# =========================================================================
# 12. CS anomaly data
# =========================================================================

class TestCSAnomaly:
    """Verify anomaly data for the CS-bar complex connection."""

    def test_anomaly_sl2_k1(self):
        """Anomaly data at k=1, N=2."""
        result = cs_bar_anomaly_data(1, 2)
        assert abs(result['kappa'] - 3.0 * 3 / 4.0) < TOL
        assert abs(result['central_charge'] - 1.0) < TOL

    def test_anomaly_sl2_k2(self):
        """Anomaly data at k=2, N=2."""
        result = cs_bar_anomaly_data(2, 2)
        assert abs(result['kappa'] - 3.0) < TOL
        assert abs(result['central_charge'] - 1.5) < TOL

    def test_kappa_ne_c_half(self):
        """kappa != c/2 for sl_2 (AP39)."""
        for k in range(1, 8):
            result = cs_bar_anomaly_data(k, 2)
            assert not result['kappa_eq_c_half']


# =========================================================================
# 13. Knot invariant table
# =========================================================================

class TestKnotTable:
    """Verify multi-knot invariant computations."""

    def test_table_default_knots(self):
        """Table for default set of knots."""
        table = knot_invariant_table(Q_GENERIC)
        assert "3_1" in table
        assert "4_1" in table
        # Unknot has trivial invariant
        assert abs(table["0_1"]['value'] - 1.0) < TOL

    def test_table_sl3(self):
        """Table for sl_3."""
        table = knot_invariant_table(Q_GENERIC, knots=["3_1", "4_1"], N=3)
        assert "3_1" in table
        assert abs(table["3_1"]['value']) > 1e-10


# =========================================================================
# 14. CS level scan
# =========================================================================

class TestCSLevelScan:
    """Verify CS level scan."""

    def test_level_scan_trefoil(self):
        """Scan trefoil across levels k=1..5."""
        result = cs_level_scan("3_1", k_max=5, N=2)
        assert len(result['scan']) == 5
        # All values should be nonzero
        for entry in result['scan']:
            assert abs(entry['rt_value']) > 1e-14


# =========================================================================
# 15. Factorization homology trace identifications
# =========================================================================

class TestFactorizationTrace:
    """Verify the CFG identification: FH trace = quantum Markov trace."""

    def test_fh_trace_jones_trefoil(self):
        """FH trace for sl_2 on trefoil = Jones polynomial."""
        q = Q_GENERIC
        fh_val = factorization_trace_jones([1, 1, 1], 2, q)
        jones_val = jones_trefoil_exact(q)
        assert abs(fh_val - jones_val) < TOL

    def test_fh_trace_slN_trefoil(self):
        """FH trace for sl_3 on trefoil."""
        q = Q_GENERIC
        fh_val = factorization_trace_slN([1, 1, 1], 2, q, 3)
        direct = homflypt_trefoil_sl_N(q, 3)
        assert abs(fh_val - direct) < TOL

    def test_fh_trace_colored(self):
        """FH colored trace at color 2 = ordinary FH trace."""
        q = Q_GENERIC
        fh_col = factorization_trace_colored([1, 1, 1], 2, q, 2)
        fh_ord = factorization_trace_jones([1, 1, 1], 2, q)
        assert abs(fh_col - fh_ord) < TOL


# =========================================================================
# 16. Cross-engine consistency
# =========================================================================

class TestCrossEngineConsistency:
    """Verify consistency with existing engines (no reimplementation)."""

    def test_vs_knot_invariant_engine_jones(self):
        """Our FH trace matches the knot_invariant_shadow_engine Jones."""
        from compute.lib.knot_invariant_shadow_engine import jones_at as shadow_jones
        q = Q_GENERIC
        for knot in ["3_1", "4_1", "5_1"]:
            our_val = factorization_trace_jones(
                *([1, 1, 1], 2) if knot == "3_1" else
                ([1, -2, 1, -2], 3) if knot == "4_1" else
                ([1, 1, 1, 1, 1], 2)
            , q)
            shadow_val = shadow_jones(knot, q)
            assert abs(our_val - shadow_val) < TOL, (
                f"Mismatch for {knot}: {our_val} vs {shadow_val}"
            )

    def test_vs_yangian_roots_unity_engine_qdim(self):
        """Our quantum dimension matches the roots-of-unity engine."""
        from compute.lib.theorem_yangian_roots_unity_engine import (
            quantum_integer as ru_qi
        )
        q = Q_GENERIC
        for n in range(1, 8):
            our_val = colored_jones_unknot(n, q)
            ru_val = ru_qi(n, q)
            assert abs(our_val - ru_val) < TOL
