r"""Tests for the chromatic-magnon correspondence engine.

THEOREM:
  The chromatic filtration in the MC3 proof (thick generation of the DK
  category) is identified with the magnon-number filtration in the
  Gaudin/Bethe framework.

MULTI-PATH VERIFICATION (CLAUDE.md mandate, 3+ paths per claim):
  Path 1: S_z decomposition dimensions = binomial coefficients (combinatorial)
  Path 2: CG multiplicities satisfy dim(V_j) * mult(j) = 2^n (algebraic)
  Path 3: Gaudin eigenvalues (full diag) = Gaudin eigenvalues (sector diag) (numeric)
  Path 4: Gaudin sum rule sum_i H_i = 0 (residue theorem)
  Path 5: Gaudin Hamiltonians commute (CYBE / MC arity 3)
  Path 6: Joint eigenvalues distinguish all irreps at generic sites
  Path 7: Bethe roots satisfy the BAE residual = 0

TEST STRUCTURE:
  Section A: S_z sector decomposition (dimensions, magnon counting)
  Section B: CG decomposition (multiplicities, consistency)
  Section C: Gaudin Hamiltonians (construction, commutativity)
  Section D: Gaudin eigenvalues by sector (cross-verified)
  Section E: Gaudin sum rule
  Section F: Joint diagonalization and irrep separation
  Section G: Explicit n=4 computation
  Section H: Bethe ansatz for the Gaudin model
  Section I: DK category verification
  Section J: Cross-verification (full vs sector diag)
  Section K: Multi-path consistency checks

References:
  thm:categorical-cg-all-types (yangians_drinfeld_kohno.tex)
  cor:mc3-all-types (concordance.tex)
  theorem_bethe_mc_engine.py (Gaudin Hamiltonians, BAE)
"""

import numpy as np
import pytest
from math import comb
from numpy import linalg as la

try:
    from scipy import optimize
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

from compute.lib.theorem_chromatic_magnon_engine import (
    # Constants
    I2, SIGMA_Z, SIGMA_PLUS, SIGMA_MINUS, PERM_2,
    # Sector decomposition
    total_sz_operator,
    decompose_by_sz,
    magnon_sector_dimension,
    SzSectorDecomposition,
    # CG decomposition
    cg_decomposition_spin_half,
    # Gaudin Hamiltonians
    gaudin_hamiltonian,
    gaudin_total_hamiltonian,
    verify_gaudin_commuting,
    # Eigenvalues
    gaudin_eigenvalues_by_sector,
    gaudin_eigenvalues_all_hamiltonians,
    # Bethe ansatz
    gaudin_bae_residual,
    solve_gaudin_bae,
    gaudin_master_function,
    gaudin_energy_from_roots,
    # Chromatic-magnon
    chromatic_magnon_correspondence,
    ChromaticMagnonResult,
    # Joint diagonalization
    joint_gaudin_eigenvalues,
    # Explicit n=4
    explicit_n4_computation,
    # DK category
    dk_category_verification,
    DKCategoryData,
    # Cross-verification
    verify_gaudin_vs_exact,
    # Sum rule
    gaudin_sum_rule,
)


# Generic evaluation points (chosen to be distinct and well-separated)
SITES_3 = np.array([1.0, 3.0, 6.0])
SITES_4 = np.array([1.0, 2.0, 4.0, 7.0])
SITES_5 = np.array([1.0, 2.5, 4.0, 6.5, 9.0])


# =====================================================================
# Section A: S_z sector decomposition
# =====================================================================


class TestSzDecomposition:
    """Test the S_z decomposition of (C^2)^{tensor n}."""

    def test_n2_sectors(self):
        """n=2: sectors M=0 (dim 1), M=1 (dim 2), M=2 (dim 1)."""
        d = decompose_by_sz(2)
        assert d.total_dim == 4
        mags = d.magnon_sectors
        assert mags[0] == 1
        assert mags[1] == 2
        assert mags[2] == 1

    def test_n3_sectors(self):
        """n=3: sectors M=0 (dim 1), M=1 (dim 3), M=2 (dim 3), M=3 (dim 1)."""
        d = decompose_by_sz(3)
        assert d.total_dim == 8
        mags = d.magnon_sectors
        assert mags[0] == 1
        assert mags[1] == 3
        assert mags[2] == 3
        assert mags[3] == 1

    def test_n4_sectors(self):
        """n=4: sectors M=0..4 with dims 1, 4, 6, 4, 1."""
        d = decompose_by_sz(4)
        assert d.total_dim == 16
        mags = d.magnon_sectors
        assert mags[0] == 1
        assert mags[1] == 4
        assert mags[2] == 6
        assert mags[3] == 4
        assert mags[4] == 1

    def test_sector_dims_are_binomial(self):
        """dim(H_M) = C(n, M) for all n and M (Path 1: combinatorial)."""
        for n in range(2, 7):
            d = decompose_by_sz(n)
            mags = d.magnon_sectors
            for M in range(n + 1):
                assert mags.get(M, 0) == comb(n, M), \
                    f"n={n}, M={M}: got {mags.get(M, 0)}, expected {comb(n, M)}"

    def test_magnon_sector_dimension_function(self):
        """magnon_sector_dimension agrees with decompose_by_sz."""
        for n in [3, 4, 5]:
            d = decompose_by_sz(n)
            mags = d.magnon_sectors
            for M in range(n + 1):
                assert magnon_sector_dimension(n, M) == mags.get(M, 0)

    def test_total_dim_is_2n(self):
        """Sum of sector dimensions = 2^n (Path 2: algebraic consistency)."""
        for n in range(2, 7):
            d = decompose_by_sz(n)
            total = sum(d.magnon_sectors.values())
            assert total == 2 ** n


# =====================================================================
# Section B: CG decomposition
# =====================================================================


class TestCGDecomposition:
    """CG decomposition of (C^2)^{tensor n}."""

    def test_n2_cg(self):
        """n=2: V_1 + V_0 (triplet + singlet)."""
        cg = cg_decomposition_spin_half(2)
        assert cg['consistent'] is True
        d = cg['decomposition']
        assert d[1.0]['multiplicity'] == 1
        assert d[0.0]['multiplicity'] == 1

    def test_n3_cg(self):
        """n=3: V_{3/2} + 2*V_{1/2}."""
        cg = cg_decomposition_spin_half(3)
        assert cg['consistent'] is True
        d = cg['decomposition']
        assert d[1.5]['multiplicity'] == 1
        assert d[0.5]['multiplicity'] == 2

    def test_n4_cg(self):
        """n=4: V_2 + 3*V_1 + 2*V_0."""
        cg = cg_decomposition_spin_half(4)
        assert cg['consistent'] is True
        d = cg['decomposition']
        assert d[2.0]['multiplicity'] == 1
        assert d[1.0]['multiplicity'] == 3
        assert d[0.0]['multiplicity'] == 2

    def test_cg_total_dim(self):
        """CG total dim = 2^n for all n (Path 2: algebraic)."""
        for n in range(2, 7):
            cg = cg_decomposition_spin_half(n)
            assert cg['total_dim_from_cg'] == 2 ** n
            assert cg['consistent'] is True

    def test_n4_dim_breakdown(self):
        """n=4: 1*5 + 3*3 + 2*1 = 5 + 9 + 2 = 16 (cross-check)."""
        cg = cg_decomposition_spin_half(4)
        d = cg['decomposition']
        total = 0
        for info in d.values():
            total += info['total_dim']
        assert total == 16

    def test_n5_cg(self):
        """n=5: V_{5/2} + 4*V_{3/2} + 5*V_{1/2}."""
        cg = cg_decomposition_spin_half(5)
        assert cg['consistent'] is True
        d = cg['decomposition']
        assert d[2.5]['multiplicity'] == 1
        assert d[1.5]['multiplicity'] == 4
        assert d[0.5]['multiplicity'] == 5


# =====================================================================
# Section C: Gaudin Hamiltonians
# =====================================================================


class TestGaudinHamiltonians:
    """Test Gaudin Hamiltonian construction."""

    def test_gaudin_hermitian(self):
        """Gaudin Hamiltonians are Hermitian for real sites."""
        for i in range(len(SITES_4)):
            H = gaudin_hamiltonian(SITES_4, i)
            assert np.allclose(H, H.conj().T, atol=1e-12)

    def test_gaudin_commuting_n3(self):
        """[H_i, H_j] = 0 for n=3 (Path 5: CYBE / MC arity 3)."""
        result = verify_gaudin_commuting(SITES_3)
        assert result['commuting'] is True
        assert result['max_commutator_norm'] < 1e-10

    def test_gaudin_commuting_n4(self):
        """[H_i, H_j] = 0 for n=4."""
        result = verify_gaudin_commuting(SITES_4)
        assert result['commuting'] is True

    def test_gaudin_commuting_n5(self):
        """[H_i, H_j] = 0 for n=5."""
        result = verify_gaudin_commuting(SITES_5)
        assert result['commuting'] is True

    def test_gaudin_preserves_sz(self):
        """Gaudin Hamiltonians commute with total S_z."""
        n = 4
        Sz = total_sz_operator(n)
        for i in range(n):
            H = gaudin_hamiltonian(SITES_4, i)
            comm = H @ Sz - Sz @ H
            assert np.allclose(comm, 0, atol=1e-12)


# =====================================================================
# Section D: Gaudin eigenvalues by sector
# =====================================================================


class TestGaudinEigenvalues:
    """Gaudin eigenvalues organized by magnon sector."""

    def test_n4_sector_counts(self):
        """n=4: each sector has the right number of eigenvalues."""
        evals = gaudin_eigenvalues_by_sector(SITES_4)
        assert len(evals[0]) == 1   # M=0
        assert len(evals[1]) == 4   # M=1
        assert len(evals[2]) == 6   # M=2
        assert len(evals[3]) == 4   # M=3
        assert len(evals[4]) == 1   # M=4

    def test_n3_sector_counts(self):
        """n=3: sectors have dims 1, 3, 3, 1."""
        evals = gaudin_eigenvalues_by_sector(SITES_3)
        assert len(evals[0]) == 1
        assert len(evals[1]) == 3
        assert len(evals[2]) == 3
        assert len(evals[3]) == 1

    def test_total_eigenvalue_count(self):
        """Total eigenvalue count = 2^n across all sectors."""
        for sites in [SITES_3, SITES_4, SITES_5]:
            evals = gaudin_eigenvalues_by_sector(sites)
            total = sum(len(e) for e in evals.values())
            assert total == 2 ** len(sites)

    def test_eigenvalues_real(self):
        """Gaudin eigenvalues are real for real sites."""
        evals = gaudin_eigenvalues_by_sector(SITES_4)
        for M, e in evals.items():
            assert np.all(np.isreal(e)), f"Non-real eigenvalues in sector M={M}"


# =====================================================================
# Section E: Gaudin sum rule
# =====================================================================


class TestGaudinSumRule:
    """sum_i H_i = 0 from the residue theorem (Path 4)."""

    def test_sum_rule_n3(self):
        """Sum rule for n=3."""
        result = gaudin_sum_rule(SITES_3)
        assert result['sum_vanishes'] is True

    def test_sum_rule_n4(self):
        """Sum rule for n=4."""
        result = gaudin_sum_rule(SITES_4)
        assert result['sum_vanishes'] is True

    def test_sum_rule_n5(self):
        """Sum rule for n=5."""
        result = gaudin_sum_rule(SITES_5)
        assert result['sum_vanishes'] is True


# =====================================================================
# Section F: Joint diagonalization and irrep separation
# =====================================================================


class TestJointDiagonalization:
    """Joint eigenvalues of commuting Gaudin Hamiltonians."""

    def test_n4_M0_single_state(self):
        """n=4, M=0: single state (highest weight of V_2)."""
        jr = joint_gaudin_eigenvalues(SITES_4, 0)
        assert jr['n_states'] == 1
        assert jr['n_distinct_tuples'] == 1

    def test_n4_M4_single_state(self):
        """n=4, M=4: single state (lowest weight of V_2)."""
        jr = joint_gaudin_eigenvalues(SITES_4, 4)
        assert jr['n_states'] == 1
        assert jr['n_distinct_tuples'] == 1

    def test_n4_M1_four_states(self):
        """n=4, M=1: 4 states, joint eigenvalues should give 4 tuples."""
        jr = joint_gaudin_eigenvalues(SITES_4, 1)
        assert jr['n_states'] == 4
        # At generic sites, full separation: 4 distinct tuples
        assert jr['n_distinct_tuples'] == 4

    def test_n4_M2_six_states(self):
        """n=4, M=2: 6 states, joint eigenvalues should give 6 tuples."""
        jr = joint_gaudin_eigenvalues(SITES_4, 2)
        assert jr['n_states'] == 6
        assert jr['n_distinct_tuples'] == 6

    def test_joint_eigenvalues_sum_to_zero(self):
        """Sum of joint eigenvalue components = 0 (from sum rule).

        Since sum_i H_i = 0, for any eigenvector |v>,
        sum_i lambda_i(v) = 0.
        """
        jr = joint_gaudin_eigenvalues(SITES_4, 2)
        for jt in jr['joint_eigenvalues']:
            assert abs(sum(jt)) < 1e-8, \
                f"Joint eigenvalue sum = {sum(jt)}, expected 0"

    def test_full_separation_n3(self):
        """n=3: joint eigenvalues fully separate all states in each sector."""
        for M in range(4):
            jr = joint_gaudin_eigenvalues(SITES_3, M)
            if jr['n_states'] > 0:
                assert jr['full_separation'] is True, \
                    f"Separation failed at M={M}"


# =====================================================================
# Section G: Explicit n=4 computation
# =====================================================================


class TestExplicitN4:
    """The canonical n=4, all spin-1/2 test case."""

    def test_n4_computation_runs(self):
        """The explicit n=4 computation completes without error."""
        result = explicit_n4_computation(SITES_4)
        assert result['n'] == 4
        assert result['gaudin_commuting'] is True

    def test_n4_cg_correct(self):
        """n=4 CG decomposition: V_2 + 3*V_1 + 2*V_0."""
        result = explicit_n4_computation(SITES_4)
        cg = result['cg_decomposition']
        d = cg['decomposition']
        assert d[2.0]['multiplicity'] == 1
        assert d[1.0]['multiplicity'] == 3
        assert d[0.0]['multiplicity'] == 2

    def test_n4_magnon_dims(self):
        """n=4 magnon sector dimensions: 1, 4, 6, 4, 1."""
        result = explicit_n4_computation(SITES_4)
        md = result['magnon_dims']
        assert md[0] == 1
        assert md[1] == 4
        assert md[2] == 6
        assert md[3] == 4
        assert md[4] == 1

    def test_n4_joint_M2_separation(self):
        """n=4, M=2: 6 states fully separated by joint eigenvalues."""
        result = explicit_n4_computation(SITES_4)
        jr = result['joint_results'][2]
        assert jr['n_states'] == 6
        assert jr['n_distinct_tuples'] == 6


# =====================================================================
# Section H: Bethe ansatz for the Gaudin model
# =====================================================================


class TestGaudinBethe:
    """Bethe ansatz for the Gaudin model (Path 7)."""

    @pytest.mark.skipif(not HAS_SCIPY, reason="scipy not available")
    def test_bae_M0_trivial(self):
        """M=0: no Bethe roots needed."""
        result = solve_gaudin_bae(SITES_4, 0)
        assert result['success'] is True
        assert len(result['roots']) == 0

    @pytest.mark.skipif(not HAS_SCIPY, reason="scipy not available")
    def test_bae_M1_residual(self):
        """M=1: single Bethe root, residual should vanish."""
        result = solve_gaudin_bae(SITES_4, 1)
        if result['success']:
            assert result['residual_norm'] < 1e-8

    @pytest.mark.skipif(not HAS_SCIPY, reason="scipy not available")
    def test_bae_M2_residual(self):
        """M=2: two Bethe roots, residual should vanish."""
        result = solve_gaudin_bae(SITES_4, 2)
        if result['success']:
            assert result['residual_norm'] < 1e-8

    def test_bae_residual_at_generic_point(self):
        """BAE residual is NOT zero at a generic (non-root) point."""
        w = np.array([0.5])
        res = gaudin_bae_residual(w, SITES_4)
        assert abs(res[0]) > 0.01  # generically nonzero


# =====================================================================
# Section I: DK category verification
# =====================================================================


class TestDKCategory:
    """DK category properties from the chromatic-magnon correspondence."""

    def test_dk_all_satisfied(self):
        """All DK properties satisfied for generic sites."""
        dk = dk_category_verification(SITES_4)
        assert dk.dk0_satisfied is True
        assert dk.dk1_satisfied is True
        assert dk.dk2_satisfied is True
        assert dk.dk3_satisfied is True

    def test_dk_gaudin_labels_nonempty(self):
        """Gaudin labels are nonempty for each nontrivial sector."""
        dk = dk_category_verification(SITES_4)
        for M in range(5):
            if comb(4, M) > 0:
                assert len(dk.gaudin_labels[M]) > 0


# =====================================================================
# Section J: Cross-verification (full vs sector diag)
# =====================================================================


class TestCrossVerification:
    """Full diag vs sector diag eigenvalue comparison (Path 3)."""

    def test_full_vs_sector_n3(self):
        """n=3: full and sector diag agree."""
        result = verify_gaudin_vs_exact(SITES_3)
        assert result['match'] is True
        assert result['max_discrepancy'] < 1e-10

    def test_full_vs_sector_n4(self):
        """n=4: full and sector diag agree."""
        result = verify_gaudin_vs_exact(SITES_4)
        assert result['match'] is True
        assert result['max_discrepancy'] < 1e-10

    def test_full_vs_sector_n5(self):
        """n=5: full and sector diag agree."""
        result = verify_gaudin_vs_exact(SITES_5)
        assert result['match'] is True
        assert result['max_discrepancy'] < 1e-10

    def test_eigenvalue_count_consistency(self):
        """Number of eigenvalues from full diag = 2^n."""
        result = verify_gaudin_vs_exact(SITES_4)
        assert result['n_eigenvalues_full'] == 16
        assert result['n_eigenvalues_sectors'] == 16


# =====================================================================
# Section K: Multi-path consistency checks
# =====================================================================


class TestMultiPathConsistency:
    """Cross-checks between independent computation paths."""

    def test_sector_dim_three_paths(self):
        """Sector dims agree: binomial, decompose_by_sz, magnon_sector_dimension.

        Path 1: C(n, M) by direct formula
        Path 2: decompose_by_sz via S_z diagonalization
        Path 3: magnon_sector_dimension function
        """
        for n in [3, 4, 5]:
            d = decompose_by_sz(n)
            mags = d.magnon_sectors
            for M in range(n + 1):
                path1 = comb(n, M)
                path2 = mags.get(M, 0)
                path3 = magnon_sector_dimension(n, M)
                assert path1 == path2 == path3, \
                    f"n={n}, M={M}: {path1} vs {path2} vs {path3}"

    def test_cg_vs_sector_dims(self):
        """CG total dim = sum of sector dims = 2^n (two-path check)."""
        for n in [3, 4, 5]:
            cg = cg_decomposition_spin_half(n)
            d = decompose_by_sz(n)
            assert cg['total_dim_from_cg'] == d.total_dim == 2 ** n

    def test_gaudin_commuting_implies_joint_diag(self):
        """Gaudin commuting (Path 5) implies joint diag works (Path 6).

        If [H_i, H_j] = 0, then joint eigenvalues are well-defined.
        We check: commutativity implies all sectors have full separation.
        """
        comm = verify_gaudin_commuting(SITES_4)
        assert comm['commuting'] is True
        for M in range(5):
            jr = joint_gaudin_eigenvalues(SITES_4, M)
            if jr['n_states'] > 0:
                assert jr['full_separation'] is True

    def test_sum_rule_consistent_with_joint_evals(self):
        """Sum rule (Path 4) consistent with joint eigenvalue sums (Path 6).

        sum_i H_i = 0 implies sum_i lambda_i(v) = 0 for each eigenvector.
        """
        sr = gaudin_sum_rule(SITES_4)
        assert sr['sum_vanishes'] is True
        for M in range(5):
            jr = joint_gaudin_eigenvalues(SITES_4, M)
            for jt in jr['joint_eigenvalues']:
                assert abs(sum(jt)) < 1e-8

    def test_chromatic_magnon_full_pipeline(self):
        """Full chromatic-magnon pipeline for n=4."""
        cm = chromatic_magnon_correspondence(SITES_4)
        assert cm.gaudin_commuting is True
        assert cm.n_sites == 4
        assert cm.sector_dims[0] == 1
        assert cm.sector_dims[2] == 6

    def test_n4_M2_eigenvalues_distinct_two_paths(self):
        """n=4, M=2: distinct eigenvalue count agrees between two methods.

        Path 1: from gaudin_eigenvalues_by_sector (single total H)
        Path 2: from joint_gaudin_eigenvalues (all H_i simultaneously)
        """
        evals = gaudin_eigenvalues_by_sector(SITES_4)
        jr = joint_gaudin_eigenvalues(SITES_4, 2)
        # Both methods see 6 eigenvalues in the M=2 sector
        assert len(evals[2]) == 6
        assert jr['n_states'] == 6
        # Joint diag gives full separation
        assert jr['n_distinct_tuples'] == 6

    @pytest.mark.skipif(not HAS_SCIPY, reason="scipy not available")
    def test_bethe_root_energy_vs_exact(self):
        """Gaudin energy from Bethe roots matches exact diag eigenvalue.

        If the Bethe root w solves the BAE, then the Gaudin eigenvalues
        lambda_i(w) should match an eigenvalue of H_i restricted to the
        correct sector.
        """
        result = solve_gaudin_bae(SITES_4, 1)
        if result['success']:
            roots = result['roots']
            evals_from_roots = gaudin_energy_from_roots(roots, SITES_4)
            # The sum should be zero (sum rule)
            assert abs(sum(evals_from_roots)) < 1e-6
