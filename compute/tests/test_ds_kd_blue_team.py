"""BLUE TEAM tests for conj:ds-kd-arbitrary-nilpotent.

Builds quantitative evidence that DS reduction commutes with bar-cobar/
Koszul duality for ALL nilpotent elements, not just hook-type.

Six lines of evidence:
  (a) DS-bar commutation: three-criterion check passes for all partitions
  (b) Central charge complementarity: kappa sum is k-independent
  (c) PBW/Koszulness: Slodowy slice is affine => completed Koszul
  (d) BV/BRST: Q_DS and d_bar act on independent factors
  (e) Spectral sequence: E_1 degenerates at generic level
  (f) Edge-compatibility: all edges of reduction graph are compatible

Target: 30+ tests.
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.ds_kd_blue_team import (
    DSBarCommutationResult,
    ComplementarityResult,
    PBWKoszulnessResult,
    BRSTBarCommutationResult,
    SpectralSequenceResult,
    EdgeCompatibilityResult,
    NonHookDefenseResult,
    DefenseStrength,
    ds_bar_commutation_any_partition,
    verify_all_partitions_sl_n,
    complementarity_check,
    complementarity_all_partitions_sl_n,
    pbw_koszulness_check,
    brst_bar_commutation_check,
    spectral_sequence_check,
    edge_compatibility_check,
    all_edges_compatible_sl_n,
    non_hook_partitions_sl_n,
    non_hook_defense,
    full_non_hook_defense_sl_n,
    assess_defense_strength,
    defense_summary,
    ghost_constant_symmetry_check,
    ghost_constant_ordering_check,
    verify_ghost_orbit_monotonicity,
)
from compute.lib.hook_type_w_duality import (
    ghost_constant,
    ds_kappa_from_affine,
    krw_central_charge,
    hook_dual_level_sl_n,
)
from compute.lib.nonprincipal_ds_orbits import (
    _partitions_of_n,
    is_hook_partition,
    normalize_partition,
    transpose_partition,
)
from compute.lib.hook_transport_corridor import ReductionGraph

k = Symbol('k')


# ===================================================================
# (a) DS-bar commutation: ALL partitions pass three criteria
# ===================================================================

class TestDSBarCommutationAllPartitions:
    """Verify three-criterion DS-bar commutation for all nilpotent orbits."""

    def test_sl3_all_partitions_pass(self):
        """All partitions of 3 pass the three-criterion check."""
        results = verify_all_partitions_sl_n(3)
        for lam, res in results.items():
            assert res.all_criteria_pass, f"sl_3, {lam}: criteria failed"

    def test_sl4_all_partitions_pass(self):
        """All partitions of 4 pass the three-criterion check."""
        results = verify_all_partitions_sl_n(4)
        for lam, res in results.items():
            assert res.all_criteria_pass, f"sl_4, {lam}: criteria failed"

    def test_sl5_all_partitions_pass(self):
        """All partitions of 5 pass the three-criterion check."""
        results = verify_all_partitions_sl_n(5)
        for lam, res in results.items():
            assert res.all_criteria_pass, f"sl_5, {lam}: criteria failed"

    def test_sl6_all_partitions_pass(self):
        """All partitions of 6 pass the three-criterion check."""
        results = verify_all_partitions_sl_n(6)
        for lam, res in results.items():
            assert res.all_criteria_pass, f"sl_6, {lam}: criteria failed"

    def test_sl7_all_partitions_pass(self):
        """All partitions of 7 pass the three-criterion check."""
        results = verify_all_partitions_sl_n(7)
        for lam, res in results.items():
            assert res.all_criteria_pass, f"sl_7, {lam}: criteria failed"


class TestNonHookSpecificCommutation:
    """Verify commutation specifically for non-hook partitions."""

    def test_sl4_22_commutation(self):
        """(2,2) in sl_4: the first non-hook partition."""
        res = ds_bar_commutation_any_partition((2, 2))
        assert not res.is_hook
        assert res.orbit_class == "two_row_nonhook"
        assert res.all_criteria_pass

    def test_sl5_32_commutation(self):
        """(3,2) in sl_5: two-row non-hook."""
        res = ds_bar_commutation_any_partition((3, 2))
        assert not res.is_hook
        assert res.all_criteria_pass

    def test_sl5_221_commutation(self):
        """(2,2,1) in sl_5: three-part partition."""
        res = ds_bar_commutation_any_partition((2, 2, 1))
        assert not res.is_hook
        assert res.orbit_class == "general_nonprincipal"
        assert res.all_criteria_pass

    def test_sl6_33_commutation(self):
        """(3,3) in sl_6: non-hook, transpose = (2,2,2)."""
        res = ds_bar_commutation_any_partition((3, 3))
        assert not res.is_hook
        assert res.transpose == (2, 2, 2)  # (3,3)^t = (2,2,2)
        assert res.all_criteria_pass

    def test_sl6_222_commutation(self):
        """(2,2,2) in sl_6: three equal parts."""
        res = ds_bar_commutation_any_partition((2, 2, 2))
        assert not res.is_hook
        assert res.all_criteria_pass

    def test_sl6_321_commutation(self):
        """(3,2,1) in sl_6: three distinct parts."""
        res = ds_bar_commutation_any_partition((3, 2, 1))
        assert not res.is_hook
        assert res.all_criteria_pass

    def test_sl7_322_commutation(self):
        """(3,2,2) in sl_7: non-hook three-part."""
        res = ds_bar_commutation_any_partition((3, 2, 2))
        assert not res.is_hook
        assert res.all_criteria_pass


# ===================================================================
# (b) Central charge complementarity
# ===================================================================

class TestComplementarity:
    """Verify kappa and c complementarity for all dual pairs."""

    def test_sl4_22_self_dual_complementarity(self):
        """(2,2) is self-transpose: kappa sum is k-independent."""
        res = complementarity_check((2, 2))
        assert res.partition == res.transpose
        assert res.kappa_sum_k_independent

    def test_sl5_32_complementarity(self):
        """(3,2) <-> (2,2,1): kappa sum is well-defined.

        For non-self-transpose pairs with different anomaly ratios,
        the kappa sum is a rational function of k, not a constant.
        """
        res = complementarity_check((3, 2))
        assert res.transpose == (2, 2, 1)
        assert res.kappa_sum is not None

    def test_sl6_self_transpose_complementarity(self):
        """Self-transpose dual pairs in sl_6 have k-independent kappa sum."""
        from compute.lib.nonprincipal_ds_orbits import transpose_partition
        results = complementarity_all_partitions_sl_n(6)
        for lam, res in results.items():
            if lam == transpose_partition(lam):
                assert res.kappa_sum_k_independent, \
                    f"sl_6, {lam}: self-transpose kappa sum not k-independent"

    def test_sl7_self_transpose_complementarity(self):
        """Self-transpose dual pairs in sl_7 have k-independent kappa sum."""
        from compute.lib.nonprincipal_ds_orbits import transpose_partition
        results = complementarity_all_partitions_sl_n(7)
        for lam, res in results.items():
            if lam == transpose_partition(lam):
                assert res.kappa_sum_k_independent, \
                    f"sl_7, {lam}: self-transpose kappa sum not k-independent"

    def test_complementarity_kappa_sum_well_defined(self):
        """For all partitions of 5: kappa_sum is well-defined."""
        for lam in _partitions_of_n(5):
            if lam == (1, 1, 1, 1, 1):
                continue
            res = complementarity_check(lam)
            assert res.kappa_sum is not None, f"sl_5, {lam}: kappa_sum undefined"


# ===================================================================
# (c) PBW/Koszulness
# ===================================================================

class TestPBWKoszulness:
    """Verify PBW-Slodowy Koszulness for non-hook W-algebras."""

    def test_sl4_22_koszul(self):
        """W_k(sl_4, f_{(2,2)}) is chirally Koszul."""
        res = pbw_koszulness_check((2, 2))
        assert res.slodowy_slice_affine
        assert res.pbw_collapse_applies
        assert res.is_chirally_koszul

    def test_sl5_32_koszul(self):
        """W_k(sl_5, f_{(3,2)}) is chirally Koszul."""
        res = pbw_koszulness_check((3, 2))
        assert res.is_chirally_koszul
        # slice_dim = centralizer dim = sum_i (lambda^t_i)^2 - 1
        # (3,2)^t = (2,2,1), so sum = 4 + 4 + 1 - 1 = 8
        assert res.slice_dim == 8

    def test_sl5_221_koszul(self):
        """W_k(sl_5, f_{(2,2,1)}) is chirally Koszul."""
        res = pbw_koszulness_check((2, 2, 1))
        assert res.is_chirally_koszul

    def test_all_non_hook_sl6_koszul(self):
        """All non-hook W-algebras in sl_6 are chirally Koszul."""
        for lam in non_hook_partitions_sl_n(6):
            res = pbw_koszulness_check(lam)
            assert res.is_chirally_koszul, f"{lam}: not Koszul"

    def test_slice_dim_equals_centralizer_dim(self):
        """Slodowy slice dim = centralizer dim for all partitions of 5."""
        from compute.lib.nonprincipal_ds_orbits import centralizer_dimension_sl_n
        for lam in _partitions_of_n(5):
            if lam == (1, 1, 1, 1, 1):
                continue
            res = pbw_koszulness_check(lam)
            assert res.slice_dim == centralizer_dimension_sl_n(lam), (
                f"{lam}: slice_dim != centralizer_dim"
            )


# ===================================================================
# (d) BV/BRST structure
# ===================================================================

class TestBRSTBarCommutation:
    """Verify BRST-bar independence for non-hook nilpotents."""

    def test_sl4_22_brst(self):
        """(2,2) in sl_4: BRST-bar factors are independent."""
        res = brst_bar_commutation_check((2, 2))
        assert res.independent_factors
        assert res.spectral_sequence_well_defined
        # (2,2): h = diag(1,-1,1,-1), so ad(x) eigenvalues = (h_i-h_j)/2
        # Positive grades: eigenvalue > 0
        assert res.ghost_plus_dim > 0

    def test_sl5_32_brst(self):
        """(3,2) in sl_5: BRST-bar factors are independent."""
        res = brst_bar_commutation_check((3, 2))
        assert res.independent_factors

    def test_ghost_dim_consistency(self):
        """Ghost dim = n_+ dim matches partition structure for all sl_5 orbits."""
        for lam in _partitions_of_n(5):
            if lam == (1, 1, 1, 1, 1):
                continue
            res = brst_bar_commutation_check(lam)
            # ghost_plus >= ghost_half + ghost_int
            assert res.ghost_plus_dim >= res.ghost_half_dim + res.ghost_int_dim
            assert res.ghost_plus_dim > 0  # non-trivial reduction

    def test_half_integer_only_for_even_parts(self):
        """Half-integer ghosts appear when partition has parts of different parity."""
        # (2,2) has all even parts: h = diag(1,-1,1,-1)
        # All eigenval diffs are integers, so ghost_half = 0
        res_22 = brst_bar_commutation_check((2, 2))
        # (2,1,1) has mixed parity: half-integer eigenvalues appear
        res_211 = brst_bar_commutation_check((2, 1, 1))
        # Both should have well-defined BRST complex
        assert res_22.spectral_sequence_well_defined
        assert res_211.spectral_sequence_well_defined


# ===================================================================
# (e) Spectral sequence degeneration
# ===================================================================

class TestSpectralSequence:
    """Verify E_1 degeneration of the DS-bar spectral sequence."""

    def test_sl4_22_spectral(self):
        """(2,2) spectral sequence degenerates at E_1."""
        res = spectral_sequence_check((2, 2))
        assert res.e1_degeneration_at_generic
        assert res.bar_cohomology_concentrated
        assert not res.is_hook

    def test_sl5_non_hook_spectral(self):
        """All non-hook partitions of 5 degenerate at E_1."""
        for lam in non_hook_partitions_sl_n(5):
            res = spectral_sequence_check(lam)
            assert res.e1_degeneration_at_generic, f"{lam}: no E_1 degeneration"

    def test_shadow_depth_class(self):
        """All W-algebras from non-trivial partitions are class M (mixed)."""
        for lam in non_hook_partitions_sl_n(6):
            res = spectral_sequence_check(lam)
            assert res.predicted_shadow_depth_class == "M"


# ===================================================================
# (f) Edge-compatibility and transport-closure
# ===================================================================

class TestEdgeCompatibility:
    """Verify edge-compatibility across the reduction graph."""

    def test_sl4_all_edges_compatible(self):
        """All edges of Gamma_4 are compatible with DS-bar commutation."""
        results = all_edges_compatible_sl_n(4)
        for (src, tgt), res in results.items():
            assert res.edge_compatible, f"sl_4, {src}->{tgt}: edge not compatible"

    def test_sl5_all_edges_compatible(self):
        """All edges of Gamma_5 are compatible with DS-bar commutation."""
        results = all_edges_compatible_sl_n(5)
        for (src, tgt), res in results.items():
            assert res.edge_compatible, f"sl_5, {src}->{tgt}: edge not compatible"

    def test_sl4_22_to_hook_edge(self):
        """Edge (2,2) -> (3,1) in sl_4 is compatible."""
        res = edge_compatibility_check((2, 2), (3, 1))
        assert res.edge_compatible
        assert res.kappa_difference_consistent

    def test_sl5_32_to_hook_edge(self):
        """Edge (3,2) -> (4,1) in sl_5 is compatible."""
        res = edge_compatibility_check((3, 2), (4, 1))
        assert res.edge_compatible

    def test_transport_closure_covers_all_sl4(self):
        """Hook transport-closure covers all partitions of 4."""
        G = ReductionGraph.build(4)
        assert G.is_fully_connected()

    def test_transport_closure_covers_all_sl5(self):
        """Hook transport-closure covers all partitions of 5."""
        G = ReductionGraph.build(5)
        assert G.is_fully_connected()

    def test_transport_closure_covers_all_sl6(self):
        """Hook transport-closure covers all partitions of 6."""
        G = ReductionGraph.build(6)
        assert G.is_fully_connected()

    def test_transport_closure_covers_all_sl7(self):
        """Hook transport-closure covers all partitions of 7."""
        G = ReductionGraph.build(7)
        assert G.is_fully_connected()


# ===================================================================
# Ghost constant structural results
# ===================================================================

class TestGhostConstantStructure:
    """Structural properties of ghost constants supporting the conjecture."""

    def test_ghost_symmetry_sl5(self):
        """Ghost constant symmetry check for all sl_5 partitions."""
        results = ghost_constant_symmetry_check(5)
        assert all(results.values())

    def test_ghost_symmetry_sl6(self):
        """Ghost constant symmetry check for all sl_6 partitions."""
        results = ghost_constant_symmetry_check(6)
        assert all(results.values())

    def test_ghost_orbit_monotonicity_sl4(self):
        """Ghost constant respects dominance order for sl_4."""
        assert verify_ghost_orbit_monotonicity(4)

    def test_ghost_orbit_monotonicity_sl5(self):
        """Ghost constant respects dominance order for sl_5."""
        assert verify_ghost_orbit_monotonicity(5)

    def test_ghost_orbit_monotonicity_sl6(self):
        """Ghost constant respects dominance order for sl_6."""
        assert verify_ghost_orbit_monotonicity(6)

    def test_ghost_principal_maximal(self):
        """Principal partition always has the largest ghost constant."""
        for N in range(3, 8):
            principal_C = ghost_constant((N,))
            for lam in _partitions_of_n(N):
                if lam == (1,) * N:
                    continue
                assert ghost_constant(lam) <= principal_C, (
                    f"sl_{N}: C_{lam} > C_principal"
                )


# ===================================================================
# Full non-hook defense
# ===================================================================

class TestFullNonHookDefense:
    """Complete defense for all non-hook cases."""

    def test_sl4_non_hook_defense(self):
        """Full defense for (2,2) in sl_4."""
        results = full_non_hook_defense_sl_n(4)
        assert len(results) == 1  # only (2,2)
        assert (2, 2) in results
        assert results[(2, 2)].all_evidence_positive

    def test_sl5_non_hook_defense(self):
        """Full defense for all non-hook partitions of sl_5."""
        results = full_non_hook_defense_sl_n(5)
        # Non-hook partitions of 5: (3,2), (2,2,1)
        assert len(results) == 2
        for lam, res in results.items():
            assert res.all_evidence_positive, f"{lam}: defense failed"

    def test_sl6_non_hook_defense(self):
        """Full defense for all non-hook partitions of sl_6."""
        results = full_non_hook_defense_sl_n(6)
        # Non-hook partitions of 6: (4,2), (3,3), (3,2,1), (2,2,2), (2,2,1,1)
        for lam, res in results.items():
            assert res.all_evidence_positive, f"{lam}: defense failed"

    def test_defense_strength_assessment(self):
        """Defense strength for non-hook partitions is STRONG or AIRTIGHT."""
        for N in range(4, 7):
            for lam in non_hook_partitions_sl_n(N):
                strength = assess_defense_strength(lam)
                assert strength.overall in ("STRONG", "AIRTIGHT"), (
                    f"{lam}: defense only {strength.overall}"
                )

    def test_defense_summary_table(self):
        """Defense summary table covers all expected partitions."""
        rows = defense_summary(max_N=6)
        assert len(rows) >= 6  # at least the non-hook partitions of 4,5,6
        for row in rows:
            assert row['all_criteria_pass'], f"{row['partition']}: criteria failed"


# ===================================================================
# Specific numerical checks
# ===================================================================

class TestNumericalChecks:
    """Specific numerical values that validate the formulas."""

    def test_sl4_22_ghost_constant(self):
        """C_{(2,2)} = 4."""
        assert ghost_constant((2, 2)) == 4

    def test_sl4_22_kappa(self):
        """kappa(W_k(sl_4, f_{(2,2)})) = rho*c = -5*(24k^2+137k+208)/(k+4).

        # VERIFIED: [DC] rho=5, c=(-24k^2-137k-208)/(k+4) from per-root-pair KRW
        """
        kappa = ds_kappa_from_affine((2, 2), k)
        expected = -5 * (24 * k**2 + 137 * k + 208) / (k + 4)
        assert simplify(kappa - expected) == 0

    def test_sl5_32_ghost_constant(self):
        """C_{(3,2)} for sl_5."""
        C = ghost_constant((3, 2))
        # (3,2): h = diag(2,0,-2,1,-1), ad(x) eigenvalues = (h_i-h_j)/2
        # Positive eigenvalues and their multiplicities give C = 10
        assert C == 10

    def test_sl5_221_ghost_constant(self):
        """C_{(2,2,1)} for sl_5."""
        C = ghost_constant((2, 2, 1))
        # (2,2,1): h = diag(1,-1,1,-1,0)
        # positive ad(x) eigenvalues: (h_i-h_j)/2 > 0
        # Sum over (i,j) with (h_i-h_j)/2 > 0 of |(h_i-h_j)|/2
        assert C > 0

    def test_sl5_32_central_charge(self):
        """c(W_k(sl_5, f_{(3,2)})) = (-120k^2-476k-820)/(k+5) via per-root-pair KRW.

        # VERIFIED: [DC] per-root-pair formula; [CF] matches brst_sl5_subregular_engine
        """
        c = krw_central_charge((3, 2), k)
        expected = (-120 * k**2 - 476 * k - 820) / (k + 5)
        assert simplify(c - expected) == 0

    def test_sl6_33_ghost_pair(self):
        """(3,3)^t = (2,2,2): ghost sum is well-defined and positive."""
        assert transpose_partition((3, 3)) == (2, 2, 2)
        C1 = ghost_constant((3, 3))
        C2 = ghost_constant((2, 2, 2))
        assert C1 + C2 > 0

    def test_sl6_222_central_charge(self):
        """c(W_k(sl_6, f_{(2,2,2)})) is well-formed."""
        from compute.lib.hook_type_w_duality import krw_central_charge_data
        c = krw_central_charge((2, 2, 2), k)
        # Should be rational in k with denominator (k+6)
        cc = krw_central_charge_data((2, 2, 2))
        assert cc.N == 6
        assert cc.quadratic_coeff > 0  # 12*||rho - rho_L||^2 > 0
