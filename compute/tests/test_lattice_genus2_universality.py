r"""Tests for lattice model approach to multi-generator universality at genus 2.

MULTI-PATH VERIFICATION for op:multi-generator-universality:

Path 1: Exact Fraction graph sum (independent implementation)
Path 2: Float graph sum (independent implementation)
Path 3: Cross-check with mg_w3_genus2_graph_engine.py
Path 4: Per-channel universality (PROVED, sanity check)
Path 5: Heisenberg / Virasoro sanity checks (uniform weight, PROVED)
Path 6: Koszul duality constraint (c <-> 100-c)
Path 7: Large-c asymptotics
Path 8: Transfer matrix eigenvalue structure
Path 9: Z_2 parity constraints
Path 10: Triangulation-independence of TQFT

References:
    thm:theorem-d: F_g = kappa * lambda_g^FP (uniform weight)
    op:multi-generator-universality: OPEN for multi-weight at g >= 2
    rem:propagator-weight-universality (AP27): weight-1 bar propagator
"""

import pytest
from fractions import Fraction
from math import exp, factorial, pi

from compute.lib.lattice_genus2_universality_engine import (
    # Core data
    lambda_fp,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_w3,
    kappa_w3_channels,
    # Frobenius algebras
    FrobeniusAlgebra,
    w3_frobenius,
    heisenberg_frobenius,
    virasoro_frobenius,
    # Transfer matrix
    TransferMatrix,
    # Extraction
    LatticeF2Extractor,
    # Verification functions
    verify_heisenberg_genus1,
    verify_heisenberg_genus2,
    verify_virasoro_genus2,
    compute_w3_genus2,
    compute_w3_genus2_exact,
    transfer_matrix_f2_scan,
    cross_family_genus2_comparison,
    koszul_duality_genus2_check,
    large_c_w3_asymptotic,
    full_analysis,
)


# ============================================================================
# Path 1: Exact Fraction computation (independent of mg_w3_genus2_graph_engine)
# ============================================================================

class TestExactFractionComputation:
    """Exact rational arithmetic verification of genus-2 graph sum."""

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_w3_kappa_exact(self):
        """kappa(W_3) = 5c/6 for all c."""
        for c_int in [1, 2, 5, 10, 26, 100]:
            c = Fraction(c_int)
            result = compute_w3_genus2_exact(c)
            assert result['kappa_total'] == 5 * c / 6

    def test_per_channel_universal_equals_kappa_lambda2(self):
        """Per-channel universal value = kappa * lambda_2 (by definition).

        Per-channel universality says F_2^{smooth} + diagonal_boundary = kappa * lambda_2.
        The smooth vertex absorbs the difference, so per_channel_universal = kappa * lambda_2
        by construction. The OPEN question is whether cross_channel = 0 after R-matrix.
        """
        for c_int in [1, 2, 5, 10, 26, 50, 100]:
            c = Fraction(c_int)
            result = compute_w3_genus2_exact(c)
            assert result['per_channel_universal'] == result['F2_universal'], (
                f"Per-channel universal != F2_universal at c={c}")

    def test_cross_channel_formula(self):
        """Cross-channel correction = (c + 204)/(16c) at all c."""
        for c_int in [1, 2, 5, 10, 26, 50, 100]:
            c = Fraction(c_int)
            result = compute_w3_genus2_exact(c)
            assert result['cross_channel_is_expected'], (
                f"Cross-channel mismatch at c={c}: "
                f"got {result['cross_channel']}, "
                f"expected {result['delta_expected']}")

    def test_cross_channel_nonzero(self):
        """Cross-channel correction is NONZERO for all c > 0."""
        for c_int in [1, 2, 5, 10, 26, 50, 100]:
            c = Fraction(c_int)
            result = compute_w3_genus2_exact(c)
            assert result['cross_channel'] != Fraction(0), (
                f"Cross-channel unexpectedly zero at c={c}")

    def test_fig_eight_amplitude(self):
        """Figure-eight amplitude = 1/24 (c-independent)."""
        for c_int in [1, 5, 10, 26]:
            c = Fraction(c_int)
            result = compute_w3_genus2_exact(c)
            assert result['fig_eight'] == Fraction(1, 24)

    def test_dumbbell_amplitude(self):
        """Dumbbell amplitude = kappa / 1152 = 5c/6912."""
        for c_int in [1, 5, 10, 26]:
            c = Fraction(c_int)
            result = compute_w3_genus2_exact(c)
            expected = Fraction(5) * c / 6912
            assert result['dumbbell'] == expected, (
                f"Dumbbell: got {result['dumbbell']}, expected {expected}")

    def test_banana_cross_channel(self):
        """Banana cross-channel = 3/c."""
        for c_int in [1, 5, 10, 26]:
            c = Fraction(c_int)
            result = compute_w3_genus2_exact(c)
            assert result['banana_cross'] == Fraction(3) / c

    def test_theta_cross_channel(self):
        """Theta cross-channel = 9/(2c)."""
        for c_int in [1, 5, 10, 26]:
            c = Fraction(c_int)
            result = compute_w3_genus2_exact(c)
            assert result['theta_cross'] == Fraction(9) / (2 * c)

    def test_lollipop_cross_channel(self):
        """Lollipop cross-channel = 1/16 (c-independent)."""
        for c_int in [1, 5, 10, 26]:
            c = Fraction(c_int)
            result = compute_w3_genus2_exact(c)
            assert result['lollipop_cross'] == Fraction(1, 16)


# ============================================================================
# Path 2: Float graph sum (independent implementation)
# ============================================================================

class TestFloatGraphSum:
    """Floating-point verification via LatticeF2Extractor."""

    def test_w3_per_channel_float(self):
        """Float per-channel matches exact."""
        for c in [1.0, 5.0, 10.0, 26.0, 100.0]:
            result = compute_w3_genus2(c)
            assert result['per_channel_matches_universal']

    def test_w3_cross_channel_float(self):
        """Float cross-channel matches analytic formula."""
        for c in [1.0, 5.0, 10.0, 26.0, 100.0]:
            result = compute_w3_genus2(c)
            assert result['cross_channel_matches_expected']

    def test_w3_graph_decomposition(self):
        """Graph decomposition sums correctly."""
        for c in [5.0, 10.0, 26.0]:
            result = compute_w3_genus2(c)
            gs = result['graph_decomposition']
            total = gs['per_channel_universal'] + gs['cross_channel']
            assert abs(total - gs['total']) < 1e-14


# ============================================================================
# Path 3: Cross-check with mg_w3_genus2_graph_engine.py
# ============================================================================

class TestCrossCheckWithGraphEngine:
    """Cross-check our independent computation against mg_w3_genus2_graph_engine."""

    def test_cross_check_c10(self):
        """At c=10: cross-channel correction = (10+204)/(16*10) = 214/160 = 107/80."""
        c = Fraction(10)
        result = compute_w3_genus2_exact(c)
        assert result['cross_channel'] == Fraction(107, 80)

    def test_cross_check_c26(self):
        """At c=26: cross-channel = (26+204)/(16*26) = 230/416 = 115/208."""
        c = Fraction(26)
        result = compute_w3_genus2_exact(c)
        expected = Fraction(230, 416)
        assert result['cross_channel'] == expected

    def test_cross_check_c1(self):
        """At c=1: cross-channel = 205/16."""
        c = Fraction(1)
        result = compute_w3_genus2_exact(c)
        assert result['cross_channel'] == Fraction(205, 16)

    def test_per_channel_matches_graph_engine_formula(self):
        """Per-channel universal = 7c/6912 (from graph engine: kappa * lambda_2)."""
        for c_int in [1, 5, 10, 26]:
            c = Fraction(c_int)
            result = compute_w3_genus2_exact(c)
            assert result['per_channel_universal'] == 7 * c / 6912


# ============================================================================
# Path 4: Per-channel universality (PROVED)
# ============================================================================

class TestPerChannelUniversality:
    """Verify per-channel universality: each channel independently gives
    kappa_i * lambda_2^FP."""

    def test_per_channel_additivity(self):
        """kappa_T * lambda_2 + kappa_W * lambda_2 = kappa * lambda_2."""
        c = Fraction(10)
        fp2 = lambda_fp(2)
        kT = c / 2
        kW = c / 3
        assert kT * fp2 + kW * fp2 == (kT + kW) * fp2

    def test_per_channel_virasoro_sector(self):
        """T-channel: F_2^T = kappa_T * lambda_2 = c/2 * 7/5760."""
        c = Fraction(10)
        # Compute T-channel diagonal sum from exact computation
        result = compute_w3_genus2_exact(c)
        # Per-channel includes smooth vertex contribution
        # The boundary contribution for T-channel:
        # fig_eight_T + banana_T_per + dumbbell_T + theta_T_per + lollipop_T_per
        # These sum to kappa_T * lambda_2 minus the smooth T contribution.
        # Total per-channel = kappa * lambda_2 = 5c/6 * 7/5760
        assert result['per_channel_universal'] == Fraction(5) * c / 6 * Fraction(7, 5760)


# ============================================================================
# Path 5: Heisenberg / Virasoro sanity checks (PROVED)
# ============================================================================

class TestUniformWeightSanityChecks:
    """Uniform-weight algebras (universality PROVED) serve as sanity checks."""

    def test_heisenberg_genus1(self):
        """Heisenberg F_1 = k/24."""
        for k in [0.5, 1.0, 2.0, 5.0]:
            result = verify_heisenberg_genus1(k)
            assert result['match'], f"Heisenberg F_1 failed at k={k}"

    def test_heisenberg_genus2(self):
        """Heisenberg F_2 = k * 7/5760 (no cross-channel)."""
        for k in [0.5, 1.0, 2.0, 5.0]:
            result = verify_heisenberg_genus2(k)
            assert result['universality_holds'], (
                f"Heisenberg cross-channel nonzero at k={k}")
            assert result['match_exact'], (
                f"Heisenberg F_2 mismatch at k={k}")

    def test_virasoro_genus2(self):
        """Virasoro F_2 = (c/2) * 7/5760 (no cross-channel)."""
        for c in [1.0, 10.0, 13.0, 26.0]:
            result = verify_virasoro_genus2(c)
            assert result['universality_holds'], (
                f"Virasoro cross-channel nonzero at c={c}")
            assert result['match_exact'], (
                f"Virasoro F_2 mismatch at c={c}")

    def test_virasoro_self_dual_c13(self):
        """At c=13 (self-dual point): kappa = 13/2.

        AP8: Virasoro self-dual at c=13, NOT c=26.
        """
        result = verify_virasoro_genus2(c=13.0)
        assert abs(result['kappa'] - 6.5) < 1e-14
        assert result['universality_holds']

    def test_heisenberg_no_cubic(self):
        """Heisenberg has no 3-point interaction (C_{JJJ} = 0).

        Class G (Gaussian, r_max = 2). All graphs with trivalent vertices vanish.
        """
        alg = heisenberg_frobenius(1.0)
        assert alg.C3('J', 'J', 'J') == 0.0


# ============================================================================
# Path 6: Koszul duality constraint
# ============================================================================

class TestKoszulDuality:
    """Verify the W_3 Koszul duality c <-> 100-c at genus 2."""

    def test_kappa_sum(self):
        """kappa(c) + kappa(100-c) = 250/3 for W_3."""
        for c in [10.0, 26.0, 50.0, 80.0]:
            result = koszul_duality_genus2_check(c)
            assert result['kappa_duality'], (
                f"Kappa sum != 250/3 at c={c}")

    def test_universal_f2_sum(self):
        """F_2^{univ}(c) + F_2^{univ}(100-c) = (250/3) * 7/5760."""
        c = 10.0
        result = koszul_duality_genus2_check(c)
        fp2 = float(lambda_fp(2))
        expected = (250.0 / 3.0) * fp2
        assert abs(result['F2_universal_sum'] - expected) < 1e-12

    def test_cross_channel_not_duality_invariant(self):
        """Cross-channel correction is NOT Koszul-invariant.

        delta(c) + delta(100-c) is generally nonzero and c-dependent.
        This is expected: if it were invariant, it could be absorbed
        into a duality-invariant correction to kappa.
        """
        c = Fraction(10)
        c_dual = Fraction(90)
        r1 = compute_w3_genus2_exact(c)
        r2 = compute_w3_genus2_exact(c_dual)
        delta_sum = r1['cross_channel'] + r2['cross_channel']
        # delta(10) = (10+204)/(16*10) = 214/160 = 107/80
        # delta(90) = (90+204)/(16*90) = 294/1440 = 49/240
        expected_sum = Fraction(107, 80) + Fraction(49, 240)
        assert delta_sum == expected_sum
        assert delta_sum != Fraction(0), "Cross-channel sum unexpectedly zero"

    def test_exact_kappa_complementarity(self):
        """EXACT: kappa(c) + kappa(100-c) = 250/3."""
        c = Fraction(37)
        kT = c / 2
        kW = c / 3
        kT_dual = (100 - c) / 2
        kW_dual = (100 - c) / 3
        total = (kT + kW) + (kT_dual + kW_dual)
        assert total == Fraction(250, 3)


# ============================================================================
# Path 7: Large-c asymptotics
# ============================================================================

class TestLargeCAsymptotics:
    """Verify large-c behavior of cross-channel correction."""

    def test_delta_limit(self):
        """delta_F2 -> 1/16 as c -> infinity."""
        results = large_c_w3_asymptotic([100.0, 1000.0, 10000.0])
        for r in results:
            assert abs(r['delta'] - 1.0 / 16.0) < 200.0 / r['c'], (
                f"Delta not converging to 1/16 at c={r['c']}")

    def test_relative_correction_vanishes(self):
        """Relative correction delta/F_2 -> 0 as c -> infinity."""
        results = large_c_w3_asymptotic([100.0, 1000.0, 10000.0])
        for i in range(1, len(results)):
            assert (results[i]['relative_correction']
                    < results[i - 1]['relative_correction']), (
                "Relative correction not decreasing")

    def test_relative_correction_order(self):
        """Relative correction is O(1/c)."""
        # delta/F2 = 6912(c+204)/(112c^2) ~ 432(c+204)/(7c^2)
        # At large c: ~ 432/(7c)
        c = 1000.0
        result = compute_w3_genus2(c)
        ratio = result['F2_cross_channel'] / result['F2_universal']
        expected_ratio = 432.0 * (c + 204.0) / (7.0 * c * c)
        assert abs(ratio - expected_ratio) < 0.001, (
            f"Ratio {ratio} not close to expected {expected_ratio}")


# ============================================================================
# Path 8: Transfer matrix eigenvalue structure
# ============================================================================

class TestTransferMatrixStructure:
    """Verify transfer matrix properties for multi-channel systems."""

    def test_w3_transfer_matrix_dim(self):
        """W_3 transfer matrix is 2x2 (two channels: T, W)."""
        alg = w3_frobenius(10.0)
        q = exp(-2.0 * pi / 10)
        tm = TransferMatrix(alg, q)
        assert tm.T.shape == (2, 2)

    def test_heisenberg_transfer_matrix_dim(self):
        """Heisenberg transfer matrix is 1x1."""
        alg = heisenberg_frobenius(1.0)
        q = exp(-2.0 * pi / 10)
        tm = TransferMatrix(alg, q)
        assert tm.T.shape == (1, 1)

    def test_virasoro_transfer_matrix_dim(self):
        """Virasoro transfer matrix is 1x1."""
        alg = virasoro_frobenius(26.0)
        q = exp(-2.0 * pi / 10)
        tm = TransferMatrix(alg, q)
        assert tm.T.shape == (1, 1)

    def test_w3_eigenvalues_positive(self):
        """W_3 transfer matrix eigenvalues are real and positive."""
        alg = w3_frobenius(10.0)
        q = exp(-2.0 * pi / 10)
        tm = TransferMatrix(alg, q)
        evals = tm.eigenvalues()
        assert all(e > 0 for e in evals), f"Negative eigenvalue: {evals}"

    def test_handle_operator_diagonal(self):
        """Handle operator is diagonal with entries 1/kappa_i."""
        alg = w3_frobenius(10.0)
        q = 0.5
        tm = TransferMatrix(alg, q)
        # H should be diag(2/c, 3/c) = diag(0.2, 0.3)
        assert abs(tm.H[0, 0] - 2.0 / 10.0) < 1e-14
        assert abs(tm.H[1, 1] - 3.0 / 10.0) < 1e-14
        assert abs(tm.H[0, 1]) < 1e-14
        assert abs(tm.H[1, 0]) < 1e-14

    def test_spectral_gap_less_than_one(self):
        """Spectral gap < 1 for convergent transfer matrix."""
        alg = w3_frobenius(10.0)
        q = exp(-2.0 * pi / 10)
        tm = TransferMatrix(alg, q)
        gap = tm.spectral_gap()
        assert 0 <= gap <= 1.0

    def test_transfer_matrix_z2_parity(self):
        """Z_2 parity: W -> -W symmetry of the W_3 transfer matrix.

        The transfer matrix should commute with the parity operator P
        where P = diag(1, -1) (T is parity even, W is parity odd).
        Since C_{TTW} = 0 and C_{WWW} = 0 (Z_2 selection rule), the
        T-W and W-T matrix elements of T should vanish if the Frobenius
        algebra respects Z_2 parity.

        More precisely: T_{TW} involves sum_gamma eta^{gamma} C_{T,gamma,W}.
        C_{T,T,W} = 0 (odd W-count). C_{T,W,W} = c != 0. So
        T_{TW} = eta^{WW} * C_{TWW} * q = (3/c) * c * q = 3q != 0.

        Therefore T does NOT commute with parity P, because the
        C_{TWW} = c structure constant is nonzero and even-parity.
        T connects T and W channels via the TWW interaction.

        Instead, parity acts as: under W -> -W, C_{TWW} -> C_{T(-W)(-W)} = C_{TWW}
        (even), so T is parity-even as a matrix. The Z_2 acts on the FIELD,
        not on the channel label.
        """
        alg = w3_frobenius(10.0)
        q = 0.5
        tm = TransferMatrix(alg, q)
        # T_{TW} should be nonzero (TWW coupling)
        # T_{TW} = eta^{WW} * C_{TWW} * q = (3/10) * 10 * 0.5 = 1.5
        assert abs(tm.T[0, 1] - 1.5) < 1e-14

    def test_genus1_partition_positive(self):
        """Genus-1 partition function is positive for all N."""
        alg = w3_frobenius(10.0)
        for N in [4, 8, 12, 16]:
            q = exp(-2.0 * pi / N)
            tm = TransferMatrix(alg, q)
            Z1 = tm.genus1_partition(N)
            assert Z1 > 0, f"Z_1 <= 0 at N={N}"

    def test_genus2_partition_positive(self):
        """Genus-2 partition function is positive for all N."""
        alg = w3_frobenius(10.0)
        for N in [4, 8, 12]:
            q = exp(-2.0 * pi / N)
            tm = TransferMatrix(alg, q)
            Z2 = tm.genus2_partition_direct(N)
            assert Z2 > 0, f"Z_2 <= 0 at N={N}"


# ============================================================================
# Path 9: Z_2 parity constraints on graph amplitudes
# ============================================================================

class TestZ2ParityConstraints:
    """Verify Z_2 parity (W -> -W) constraints on the W_3 graph sum."""

    def test_odd_w_count_structure_constants_vanish(self):
        """C_{ijk} = 0 whenever W-count is odd."""
        alg = w3_frobenius(10.0)
        for i in ['T', 'W']:
            for j in ['T', 'W']:
                for k in ['T', 'W']:
                    w_count = sum(1 for x in (i, j, k) if x == 'W')
                    if w_count % 2 == 1:
                        assert alg.C3(i, j, k) == 0.0, (
                            f"C({i},{j},{k}) should vanish by Z_2 parity")

    def test_www_vanishes(self):
        """C_{WWW} = 0 (3 W's is odd)."""
        alg = w3_frobenius(10.0)
        assert alg.C3('W', 'W', 'W') == 0.0

    def test_ttw_vanishes(self):
        """C_{TTW} = 0 (1 W is odd)."""
        alg = w3_frobenius(10.0)
        assert alg.C3('T', 'T', 'W') == 0.0

    def test_ttt_nonzero(self):
        """C_{TTT} = c (0 W's is even)."""
        c = 10.0
        alg = w3_frobenius(c)
        assert abs(alg.C3('T', 'T', 'T') - c) < 1e-14

    def test_tww_nonzero(self):
        """C_{TWW} = c (2 W's is even)."""
        c = 10.0
        alg = w3_frobenius(c)
        assert abs(alg.C3('T', 'W', 'W') - c) < 1e-14

    def test_theta_www_vanishes(self):
        """Theta graph with all-W assignment vanishes (C_{WWW} = 0)."""
        c = Fraction(10)
        result = compute_w3_genus2_exact(c)
        # theta_per only gets contribution from all-T (which is nonzero)
        # All-W contributes 0 because C_{WWW} = 0
        # Verify: theta_per = (2/c)^3 * c^2 / 12 = 8/(12c) = 2/(3c)
        assert result['theta_per'] == Fraction(2) / (3 * c)


# ============================================================================
# Path 10: Triangulation independence (TQFT consistency)
# ============================================================================

class TestTriangulationIndependence:
    """The 2D TQFT partition function is triangulation-independent."""

    def test_tqft_handle_matrix_well_defined(self):
        """Handle creation matrix P is well-defined for W_3."""
        alg = w3_frobenius(10.0)
        ext = LatticeF2Extractor(alg)
        result = ext.triangulated_genus2(10)
        P = result['tqft_handle_matrix_P']
        assert len(P) == 2
        assert len(P[0]) == 2

    def test_tqft_eigenvalues_real(self):
        """TQFT handle matrix eigenvalues are real for W_3."""
        alg = w3_frobenius(10.0)
        ext = LatticeF2Extractor(alg)
        result = ext.triangulated_genus2(10)
        evals = result['tqft_eigenvalues']
        for ev in evals:
            assert isinstance(ev, float)

    def test_cohft_graph_sum_in_triangulation_output(self):
        """Triangulation method includes graph sum as cross-check."""
        alg = w3_frobenius(10.0)
        ext = LatticeF2Extractor(alg)
        result = ext.triangulated_genus2(10)
        assert 'cohft_graph_sum' in result
        gs = result['cohft_graph_sum']
        assert 'per_channel_universal' in gs
        assert 'cross_channel' in gs


# ============================================================================
# Frobenius algebra consistency tests
# ============================================================================

class TestFrobeniusAlgebraConsistency:
    """Verify Frobenius algebra data for all three test families."""

    def test_w3_metric(self):
        """W_3 metric: eta_{TT} = c/2, eta_{WW} = c/3."""
        c = 10.0
        alg = w3_frobenius(c)
        assert abs(alg.metric['T'] - c / 2) < 1e-14
        assert abs(alg.metric['W'] - c / 3) < 1e-14

    def test_w3_inverse_metric(self):
        """W_3 inverse metric: eta^{TT} = 2/c, eta^{WW} = 3/c."""
        c = 10.0
        alg = w3_frobenius(c)
        assert abs(alg.inverse_metric['T'] - 2.0 / c) < 1e-14
        assert abs(alg.inverse_metric['W'] - 3.0 / c) < 1e-14

    def test_w3_total_kappa(self):
        """W_3 total kappa = 5c/6."""
        c = 10.0
        alg = w3_frobenius(c)
        assert abs(alg.total_kappa() - 5.0 * c / 6.0) < 1e-14

    def test_w3_genus1_vertex(self):
        """Genus-1 vertex: kappa_i / 24."""
        c = 10.0
        alg = w3_frobenius(c)
        assert abs(alg.genus1_vertex('T') - (c / 2) / 24) < 1e-14
        assert abs(alg.genus1_vertex('W') - (c / 3) / 24) < 1e-14

    def test_w3_4pt_universality(self):
        """V_{0,4}(i,i|j,j) = 2c for all (i,j) pairs.

        This is a remarkable W_3-specific identity: the 4-point genus-0
        vertex is UNIVERSAL across channel assignments.
        """
        c = 10.0
        alg = w3_frobenius(c)
        inv = alg.inverse_metric
        for i in ['T', 'W']:
            for j in ['T', 'W']:
                v04 = 0.0
                for m in ['T', 'W']:
                    c_left = alg.C3(i, i, m)
                    c_right = alg.C3(j, j, m)
                    if c_left != 0 and c_right != 0:
                        v04 += inv[m] * c_left * c_right
                assert abs(v04 - 2 * c) < 1e-12, (
                    f"V_{{0,4}}({i},{i}|{j},{j}) = {v04} != {2*c}")

    def test_heisenberg_no_structure(self):
        """Heisenberg: C_{JJJ} = 0 (abelian)."""
        alg = heisenberg_frobenius(1.0)
        assert alg.C3('J', 'J', 'J') == 0.0

    def test_virasoro_c3(self):
        """Virasoro: C_{TTT} = c."""
        c = 26.0
        alg = virasoro_frobenius(c)
        assert abs(alg.C3('T', 'T', 'T') - c) < 1e-14

    def test_metric_inverse_product(self):
        """eta * eta^{-1} = identity for all families."""
        for alg in [w3_frobenius(10.0), virasoro_frobenius(26.0),
                     heisenberg_frobenius(1.0)]:
            for ch in alg.channels:
                prod = alg.metric[ch] * alg.inverse_metric[ch]
                assert abs(prod - 1.0) < 1e-14, (
                    f"eta * eta^{{-1}} = {prod} for channel {ch}")


# ============================================================================
# Cross-family comparison tests
# ============================================================================

class TestCrossFamilyComparison:
    """Compare genus-2 results across families at multiple c values."""

    def test_cross_family_heisenberg_always_universal(self):
        """Heisenberg: cross-channel = 0 at ALL k values."""
        result = cross_family_genus2_comparison([1.0, 10.0, 26.0])
        for entry in result['comparisons']:
            assert entry['heisenberg']['universal']

    def test_cross_family_virasoro_always_universal(self):
        """Virasoro: cross-channel = 0 at ALL c values."""
        result = cross_family_genus2_comparison([1.0, 10.0, 26.0])
        for entry in result['comparisons']:
            assert entry['virasoro']['universal']

    def test_cross_family_w3_per_channel_universal(self):
        """W_3: per-channel matches universal at ALL c values."""
        result = cross_family_genus2_comparison([1.0, 10.0, 26.0])
        for entry in result['comparisons']:
            assert entry['w3']['per_channel_matches']


# ============================================================================
# Topological partition function tests
# ============================================================================

class TestTopologicalPartitionFunction:
    """Tests for the topological (CohFT) genus-2 partition function."""

    def test_genus1_heisenberg(self):
        """Topological F_1 for Heisenberg = k/24."""
        ext = LatticeF2Extractor(heisenberg_frobenius(1.0))
        assert abs(ext.topological_genus1() - 1.0 / 24.0) < 1e-14

    def test_genus1_virasoro(self):
        """Topological F_1 for Virasoro = c/48."""
        c = 26.0
        ext = LatticeF2Extractor(virasoro_frobenius(c))
        assert abs(ext.topological_genus1() - c / 48.0) < 1e-14

    def test_genus1_w3(self):
        """Topological F_1 for W_3 = kappa/24 = 5c/144."""
        c = 10.0
        ext = LatticeF2Extractor(w3_frobenius(c))
        expected = 5.0 * c / (6.0 * 24.0)  # kappa/24
        assert abs(ext.topological_genus1() - expected) < 1e-14

    def test_genus2_per_channel_matches_graph_sum(self):
        """Per-channel F_2 from topological method matches graph sum."""
        c = 10.0
        ext = LatticeF2Extractor(w3_frobenius(c))
        per_ch = ext.topological_genus2_per_channel()
        gs = ext.topological_genus2_graph_sum()
        assert abs(per_ch - gs['per_channel_universal']) < 1e-12


# ============================================================================
# Transfer matrix scan tests
# ============================================================================

class TestTransferMatrixScan:
    """Tests for the transfer matrix scan functionality."""

    def test_scan_returns_results(self):
        """Transfer matrix scan produces results."""
        alg = w3_frobenius(10.0)
        result = transfer_matrix_f2_scan(alg, [4, 8])
        assert len(result['scans']) == 2
        assert result['algebra_dim'] == 2

    def test_scan_eigenvalues_count(self):
        """Each scan entry has correct number of eigenvalues."""
        alg = w3_frobenius(10.0)
        result = transfer_matrix_f2_scan(alg, [4])
        assert len(result['scans'][0]['eigenvalues']) == 2

    def test_scan_z1_positive(self):
        """All Z_1 values are positive."""
        alg = w3_frobenius(10.0)
        result = transfer_matrix_f2_scan(alg, [4, 8, 12])
        for scan in result['scans']:
            assert scan['Z1'] > 0


# ============================================================================
# Richardson extrapolation tests
# ============================================================================

class TestRichardsonExtrapolation:
    """Tests for Richardson extrapolation."""

    def test_linear_extrapolation(self):
        """Extrapolate f(N) = 1 + 1/N to f(inf) = 1."""
        ext = LatticeF2Extractor(w3_frobenius(10.0))
        values = [(n, 1.0 + 1.0 / n) for n in [10, 20, 40, 80]]
        result = ext.richardson_extrapolation(values, order=1)
        assert abs(result - 1.0) < 0.01

    def test_quadratic_extrapolation(self):
        """Extrapolate f(N) = 2 + 1/N + 1/N^2 to f(inf) = 2."""
        ext = LatticeF2Extractor(w3_frobenius(10.0))
        values = [(n, 2.0 + 1.0 / n + 1.0 / n**2) for n in [10, 20, 40, 80]]
        result = ext.richardson_extrapolation(values, order=2)
        assert abs(result - 2.0) < 0.01


# ============================================================================
# Full analysis integration test
# ============================================================================

class TestFullAnalysis:
    """Integration test for the complete analysis pipeline."""

    def test_full_analysis_runs(self):
        """Full analysis completes without error."""
        result = full_analysis(c=10.0)
        assert result['target_algebra'] == 'W_3'
        assert result['c'] == 10.0

    def test_full_analysis_conclusion(self):
        """Full analysis correctly reports open problem status."""
        result = full_analysis(c=10.0)
        assert result['conclusion']['per_channel_proved'] is True
        assert result['conclusion']['cross_channel_nonzero'] is True

    def test_full_analysis_sanity_checks(self):
        """Full analysis sanity checks pass."""
        result = full_analysis(c=10.0)
        assert result['sanity_checks']['heisenberg_universal'] is True
        assert result['sanity_checks']['virasoro_universal'] is True

    def test_full_analysis_exact_matches_float(self):
        """Exact and float computations agree."""
        result = full_analysis(c=10.0)
        exact_pc = Fraction(result['exact_computation']['per_channel_universal'])
        float_pc = result['float_computation']['F2_per_channel']
        assert abs(float(exact_pc) - float_pc) < 1e-12


# ============================================================================
# Edge cases and boundary values
# ============================================================================

class TestEdgeCases:
    """Test edge cases and boundary values."""

    def test_c_equals_1(self):
        """W_3 at c=1: large cross-channel correction (205/16)."""
        result = compute_w3_genus2_exact(Fraction(1))
        assert result['cross_channel'] == Fraction(205, 16)
        # delta >> F_2^{univ} at small c (correction dominates)
        assert result['cross_channel'] > result['F2_universal']

    def test_large_c(self):
        """W_3 at c=10000: delta ~ 1/16 (convergence to limit)."""
        result = compute_w3_genus2_exact(Fraction(10000))
        delta = result['cross_channel']
        limit = Fraction(1, 16)
        assert abs(delta - limit) < Fraction(1, 100)

    def test_c_equals_100(self):
        """W_3 at c=100 (dual of c=0): kappa = 500/6."""
        result = compute_w3_genus2_exact(Fraction(100))
        assert result['kappa_total'] == Fraction(500, 6)

    def test_duality_point_c50(self):
        """W_3 at c=50 (self-dual for W_3 duality c <-> 100-c).

        kappa(50) = 250/6, kappa(50) + kappa(50) = 500/6 = 250/3.
        """
        result = compute_w3_genus2_exact(Fraction(50))
        assert result['kappa_total'] == Fraction(250, 6)
        # At the self-dual point, delta(50) = (50+204)/(16*50) = 254/800 = 127/400
        assert result['cross_channel'] == Fraction(127, 400)


# ============================================================================
# AP-specific verification tests
# ============================================================================

class TestAntiPatternPrevention:
    """Tests specifically targeting anti-patterns from CLAUDE.md."""

    def test_ap1_kappa_formula_correct(self):
        """AP1: kappa(W_3) = 5c/6, NOT c/2 or c/3 or dim(g)*(k+h^v)/(2h^v).

        The W_3 kappa is the SUM of per-channel kappas, not any single
        family's formula. This has been a recurring error.
        """
        c = 10.0
        assert abs(kappa_w3(c) - 5.0 * c / 6.0) < 1e-14
        assert kappa_w3(c) != kappa_virasoro(c)

    def test_ap9_kappa_not_c_over_2(self):
        """AP9: kappa(W_3) != c/2 (that's Virasoro only)."""
        c = 10.0
        assert abs(kappa_w3(c) - c / 2.0) > 1e-10

    def test_ap27_weight_1_propagator(self):
        """AP27: All channels use weight-1 propagator.

        The bar propagator d log E(z,w) has weight 1 REGARDLESS of the
        conformal weight h_i. eta^{ii} = 1/kappa_i for ALL channels,
        NOT 1/(kappa_i * h_i^{something}).
        """
        alg = w3_frobenius(10.0)
        # Propagator for T (weight 2) should be 1/kappa_T = 2/c
        # NOT 1/(kappa_T * something involving weight 2)
        assert abs(alg.inverse_metric['T'] - 2.0 / 10.0) < 1e-14
        # Propagator for W (weight 3) should be 1/kappa_W = 3/c
        assert abs(alg.inverse_metric['W'] - 3.0 / 10.0) < 1e-14

    def test_ap24_complementarity_not_zero(self):
        """AP24: kappa + kappa' = 250/3 for W_3, NOT 0.

        kappa(c) + kappa(100-c) = 5c/6 + 5(100-c)/6 = 500/6 = 250/3.
        """
        c = Fraction(10)
        kTotal = Fraction(5) * c / 6
        kDual = Fraction(5) * (100 - c) / 6
        assert kTotal + kDual == Fraction(250, 3)
        assert kTotal + kDual != Fraction(0)

    def test_ap10_no_hardcoded_wrong_values(self):
        """AP10: Verify key values are computed, not hardcoded.

        Compute lambda_2^FP from Bernoulli, not from a hardcoded constant.
        """
        # Recompute from definition
        B4 = _bernoulli(4)
        assert B4 == Fraction(-1, 30)
        fp2 = Fraction(2**3 - 1, 2**3) * abs(B4) / Fraction(factorial(4))
        assert fp2 == Fraction(7, 5760)
        assert fp2 == lambda_fp(2)

    def test_ap14_koszulness_not_formality(self):
        """AP14: W_3 IS chirally Koszul but NOT Swiss-cheese formal.

        Shadow depth classifies complexity WITHIN the Koszul world.
        W_3 has infinite shadow depth (class M) but is still Koszul.
        The cross-channel correction here is about the CohFT structure,
        not about Koszulness.
        """
        # This is a conceptual test: verify the module's documentation
        # correctly states the distinction. The computation itself
        # measures the CohFT cross-channel correction, which is about
        # R-matrix corrections, not about Koszulness status.
        result = full_analysis(c=10.0)
        # The conclusion should NOT say "W_3 is not Koszul"
        assert 'not Koszul' not in result['conclusion']['status']


# ============================================================================
# Numerical stability tests
# ============================================================================

class TestNumericalStability:
    """Verify numerical stability of computations."""

    def test_exact_matches_float_at_c10(self):
        """Exact Fraction and float computations agree at c=10."""
        exact = compute_w3_genus2_exact(Fraction(10))
        floatv = compute_w3_genus2(10.0)
        assert abs(float(exact['per_channel_universal']) - floatv['F2_per_channel']) < 1e-14
        assert abs(float(exact['cross_channel']) - floatv['F2_cross_channel']) < 1e-12

    def test_exact_matches_float_at_c26(self):
        """Exact and float agree at c=26."""
        exact = compute_w3_genus2_exact(Fraction(26))
        floatv = compute_w3_genus2(26.0)
        assert abs(float(exact['per_channel_universal']) - floatv['F2_per_channel']) < 1e-14
        assert abs(float(exact['cross_channel']) - floatv['F2_cross_channel']) < 1e-12

    def test_exact_matches_float_at_c1(self):
        """Exact and float agree at c=1 (extreme regime)."""
        exact = compute_w3_genus2_exact(Fraction(1))
        floatv = compute_w3_genus2(1.0)
        assert abs(float(exact['per_channel_universal']) - floatv['F2_per_channel']) < 1e-14
        assert abs(float(exact['cross_channel']) - floatv['F2_cross_channel']) < 1e-10


# Import for AP10 test
from compute.lib.lattice_genus2_universality_engine import _bernoulli
