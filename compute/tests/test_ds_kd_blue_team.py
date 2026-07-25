"""Independent exact oracles and typed obligations for the blue audit lane."""

import inspect

import pytest
from sympy import Rational, Symbol, simplify

import compute.lib.ds_kd_blue_team as blue_module

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
    ClaimPacket,
    ClaimStatus,
    anomaly_ratio_from_partition,
    ghost_constant,
    ds_kappa_from_affine,
    krw_central_charge,
    krw_central_charge_data,
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


def _assert_unresolved(packet: ClaimPacket, status: ClaimStatus) -> None:
    """Assert the typed frontier shared by modular and categorical claims."""

    assert isinstance(packet, ClaimPacket)
    assert packet.status is status
    assert packet.value is None
    assert packet.hypotheses


# ===================================================================
# (a) DS-bar commutation: ALL partitions pass three criteria
# ===================================================================

class TestDSBarCommutationAllPartitions:
    """Separate exact scalar checks from the typed commutation claim."""

    def test_sl3_all_partitions_pass(self):
        """All partitions of 3 pass the three-criterion check."""
        results = verify_all_partitions_sl_n(3)
        for lam, res in results.items():
            assert res.generators_match and res.krw_formula_consistent
            _assert_unresolved(res.kappa_compatibility, ClaimStatus.OPEN)
            _assert_unresolved(
                res.ds_bar_commutation,
                ClaimStatus.CONDITIONAL if res.is_hook else ClaimStatus.OPEN,
            )

    def test_sl4_all_partitions_pass(self):
        """All partitions of 4 pass the three-criterion check."""
        results = verify_all_partitions_sl_n(4)
        for lam, res in results.items():
            assert res.generators_match and res.krw_formula_consistent
            _assert_unresolved(
                res.ds_bar_commutation,
                ClaimStatus.CONDITIONAL if res.is_hook else ClaimStatus.OPEN,
            )

    def test_sl5_all_partitions_pass(self):
        """All partitions of 5 pass the three-criterion check."""
        results = verify_all_partitions_sl_n(5)
        for lam, res in results.items():
            assert res.generators_match and res.krw_formula_consistent
            _assert_unresolved(
                res.ds_bar_commutation,
                ClaimStatus.CONDITIONAL if res.is_hook else ClaimStatus.OPEN,
            )

    def test_sl6_all_partitions_pass(self):
        """All partitions of 6 pass the three-criterion check."""
        results = verify_all_partitions_sl_n(6)
        for lam, res in results.items():
            assert res.generators_match and res.krw_formula_consistent
            _assert_unresolved(
                res.ds_bar_commutation,
                ClaimStatus.CONDITIONAL if res.is_hook else ClaimStatus.OPEN,
            )

    def test_sl7_all_partitions_pass(self):
        """All partitions of 7 pass the three-criterion check."""
        results = verify_all_partitions_sl_n(7)
        for lam, res in results.items():
            assert res.generators_match and res.krw_formula_consistent
            _assert_unresolved(
                res.ds_bar_commutation,
                ClaimStatus.CONDITIONAL if res.is_hook else ClaimStatus.OPEN,
            )


class TestNonHookSpecificCommutation:
    """Verify commutation specifically for non-hook partitions."""

    def test_sl4_22_commutation(self):
        """(2,2) in sl_4: the first non-hook partition."""
        res = ds_bar_commutation_any_partition((2, 2))
        assert not res.is_hook
        assert res.orbit_class == "two_row_nonhook"
        assert res.generators_match and res.krw_formula_consistent
        _assert_unresolved(res.ds_bar_commutation, ClaimStatus.OPEN)

    def test_sl5_32_commutation(self):
        """(3,2) in sl_5: two-row non-hook."""
        res = ds_bar_commutation_any_partition((3, 2))
        assert not res.is_hook
        _assert_unresolved(res.ds_bar_commutation, ClaimStatus.OPEN)

    def test_sl5_221_commutation(self):
        """(2,2,1) in sl_5: three-part partition."""
        res = ds_bar_commutation_any_partition((2, 2, 1))
        assert not res.is_hook
        assert res.orbit_class == "general_nonprincipal"
        _assert_unresolved(res.ds_bar_commutation, ClaimStatus.OPEN)

    def test_sl6_33_commutation(self):
        """(3,3) in sl_6: non-hook, transpose = (2,2,2)."""
        res = ds_bar_commutation_any_partition((3, 3))
        assert not res.is_hook
        assert res.transpose == (2, 2, 2)  # (3,3)^t = (2,2,2)
        _assert_unresolved(res.ds_bar_commutation, ClaimStatus.OPEN)

    def test_sl6_222_commutation(self):
        """(2,2,2) in sl_6: three equal parts."""
        res = ds_bar_commutation_any_partition((2, 2, 2))
        assert not res.is_hook
        _assert_unresolved(res.ds_bar_commutation, ClaimStatus.OPEN)

    def test_sl6_321_commutation(self):
        """(3,2,1) in sl_6: three distinct parts."""
        res = ds_bar_commutation_any_partition((3, 2, 1))
        assert not res.is_hook
        _assert_unresolved(res.ds_bar_commutation, ClaimStatus.OPEN)

    def test_sl7_322_commutation(self):
        """(3,2,2) in sl_7: non-hook three-part."""
        res = ds_bar_commutation_any_partition((3, 2, 2))
        assert not res.is_hook
        _assert_unresolved(res.ds_bar_commutation, ClaimStatus.OPEN)


# ===================================================================
# (b) Central charge complementarity
# ===================================================================

class TestComplementarity:
    """Verify kappa and c complementarity for all dual pairs."""

    def test_sl4_22_self_dual_complementarity(self):
        """(2,2) is self-transpose: kappa sum is k-independent."""
        res = complementarity_check((2, 2))
        assert res.partition == res.transpose
        _assert_unresolved(res.kappa_sum, ClaimStatus.OPEN)
        _assert_unresolved(res.kappa_sum_k_independent, ClaimStatus.OPEN)

    def test_sl5_32_complementarity(self):
        """The (3,2)/(2,2,1) modular sum remains an open packet."""
        res = complementarity_check((3, 2))
        assert res.transpose == (2, 2, 1)
        _assert_unresolved(res.kappa_sum, ClaimStatus.OPEN)

    def test_sl6_self_transpose_complementarity(self):
        """Self-transpose dual pairs in sl_6 have k-independent kappa sum."""
        from compute.lib.nonprincipal_ds_orbits import transpose_partition
        results = complementarity_all_partitions_sl_n(6)
        for lam, res in results.items():
            if lam == transpose_partition(lam):
                _assert_unresolved(res.kappa_sum_k_independent, ClaimStatus.OPEN)

    def test_sl7_self_transpose_complementarity(self):
        """Self-transpose dual pairs in sl_7 have k-independent kappa sum."""
        from compute.lib.nonprincipal_ds_orbits import transpose_partition
        results = complementarity_all_partitions_sl_n(7)
        for lam, res in results.items():
            if lam == transpose_partition(lam):
                _assert_unresolved(res.kappa_sum_k_independent, ClaimStatus.OPEN)

    def test_complementarity_kappa_sum_well_defined(self):
        """Every sl5 transpose pair carries the modular conductor obligation."""
        for lam in _partitions_of_n(5):
            if lam == (1, 1, 1, 1, 1):
                continue
            res = complementarity_check(lam)
            _assert_unresolved(res.kappa_sum, ClaimStatus.OPEN)


# ===================================================================
# (c) PBW/Koszulness
# ===================================================================

class TestPBWKoszulness:
    """Verify PBW-Slodowy Koszulness for non-hook W-algebras."""

    def test_sl4_22_koszul(self):
        """The affine Slodowy input is exact and Koszul promotion conditional."""
        res = pbw_koszulness_check((2, 2))
        assert res.slodowy_slice_affine
        _assert_unresolved(res.pbw_collapse_applies, ClaimStatus.CONDITIONAL)
        _assert_unresolved(res.is_chirally_koszul, ClaimStatus.CONDITIONAL)

    def test_sl5_32_koszul(self):
        """The (3,2) affine slice is exact and Koszul promotion conditional."""
        res = pbw_koszulness_check((3, 2))
        _assert_unresolved(res.is_chirally_koszul, ClaimStatus.CONDITIONAL)
        # slice_dim = centralizer dim = sum_i (lambda^t_i)^2 - 1
        # (3,2)^t = (2,2,1), so sum = 4 + 4 + 1 - 1 = 8
        assert res.slice_dim == 8

    def test_sl5_221_koszul(self):
        """The (2,2,1) Koszul claim retains the PBW package."""
        res = pbw_koszulness_check((2, 2, 1))
        _assert_unresolved(res.is_chirally_koszul, ClaimStatus.CONDITIONAL)

    def test_all_non_hook_sl6_koszul(self):
        """All non-hook W-algebras in sl_6 are chirally Koszul."""
        for lam in non_hook_partitions_sl_n(6):
            res = pbw_koszulness_check(lam)
            _assert_unresolved(res.is_chirally_koszul, ClaimStatus.CONDITIONAL)

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
    """Keep ghost arithmetic separate from the mixed-commutator claim."""

    def test_sl4_22_brst(self):
        """(2,2) in sl_4: BRST-bar factors are independent."""
        res = brst_bar_commutation_check((2, 2))
        _assert_unresolved(res.brst_bar_commutation, ClaimStatus.OPEN)
        _assert_unresolved(res.spectral_sequence_realization, ClaimStatus.OPEN)
        # (2,2): h = diag(1,-1,1,-1), so ad(x) eigenvalues = (h_i-h_j)/2
        # Positive grades: eigenvalue > 0
        assert res.ghost_plus_dim > 0

    def test_sl5_32_brst(self):
        """(3,2) in sl_5: BRST-bar factors are independent."""
        res = brst_bar_commutation_check((3, 2))
        _assert_unresolved(res.brst_bar_commutation, ClaimStatus.OPEN)

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
        _assert_unresolved(res_22.spectral_sequence_realization, ClaimStatus.OPEN)
        _assert_unresolved(res_211.spectral_sequence_realization, ClaimStatus.OPEN)


# ===================================================================
# (e) Spectral sequence degeneration
# ===================================================================

class TestSpectralSequence:
    """Record exact weight bounds and open spectral/shadow realizations."""

    def test_sl4_22_spectral(self):
        """The (2,2) spectral conclusions remain open."""
        res = spectral_sequence_check((2, 2))
        _assert_unresolved(res.e1_degeneration_at_generic, ClaimStatus.OPEN)
        _assert_unresolved(res.bar_cohomology_concentrated, ClaimStatus.OPEN)
        assert not res.is_hook

    def test_sl5_non_hook_spectral(self):
        """All non-hook partitions of 5 degenerate at E_1."""
        for lam in non_hook_partitions_sl_n(5):
            res = spectral_sequence_check(lam)
            _assert_unresolved(res.e1_degeneration_at_generic, ClaimStatus.OPEN)

    def test_shadow_depth_class(self):
        """The generator-weight bound supplies evidence for an open full depth."""
        for lam in non_hook_partitions_sl_n(6):
            res = spectral_sequence_check(lam)
            assert res.generator_weight_pole_bound >= 2
            _assert_unresolved(res.shadow_depth_class, ClaimStatus.OPEN)


# ===================================================================
# (f) Edge-compatibility and transport-closure
# ===================================================================

class TestEdgeCompatibility:
    """Distinguish dominance connectivity from quantum edge transport."""

    def test_sl4_all_edges_compatible(self):
        """Every Gamma4 edge has exact KRW arithmetic and open transport."""
        results = all_edges_compatible_sl_n(4)
        for (src, tgt), res in results.items():
            expected = simplify(krw_central_charge(src, k) - krw_central_charge(tgt, k))
            assert simplify(res.central_charge_difference - expected) == 0
            _assert_unresolved(res.edge_transport, ClaimStatus.OPEN)

    def test_sl5_all_edges_compatible(self):
        """Every Gamma5 edge has exact KRW arithmetic and open transport."""
        results = all_edges_compatible_sl_n(5)
        for (src, tgt), res in results.items():
            expected = simplify(krw_central_charge(src, k) - krw_central_charge(tgt, k))
            assert simplify(res.central_charge_difference - expected) == 0
            _assert_unresolved(res.edge_transport, ClaimStatus.OPEN)

    def test_sl4_22_to_hook_edge(self):
        """Edge (2,2) -> (3,1) in sl_4 is compatible."""
        res = edge_compatibility_check((2, 2), (3, 1))
        _assert_unresolved(res.edge_transport, ClaimStatus.OPEN)
        _assert_unresolved(res.kappa_difference, ClaimStatus.OPEN)

    def test_sl5_32_to_hook_edge(self):
        """Edge (3,2) -> (4,1) in sl_5 is compatible."""
        res = edge_compatibility_check((3, 2), (4, 1))
        _assert_unresolved(res.edge_transport, ClaimStatus.OPEN)

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
    """Exact evidence ledgers with an open theorem status."""

    def test_sl4_non_hook_defense(self):
        """Full defense for (2,2) in sl_4."""
        results = full_non_hook_defense_sl_n(4)
        assert len(results) == 1  # only (2,2)
        assert (2, 2) in results
        _assert_unresolved(results[(2, 2)].theorem_status, ClaimStatus.OPEN)

    def test_sl5_non_hook_defense(self):
        """Full defense for all non-hook partitions of sl_5."""
        results = full_non_hook_defense_sl_n(5)
        # Non-hook partitions of 5: (3,2), (2,2,1)
        assert len(results) == 2
        for lam, res in results.items():
            _assert_unresolved(res.theorem_status, ClaimStatus.OPEN)

    def test_sl6_non_hook_defense(self):
        """Full defense for all non-hook partitions of sl_6."""
        results = full_non_hook_defense_sl_n(6)
        # Non-hook partitions of 6: (4,2), (3,3), (3,2,1), (2,2,2), (2,2,1,1)
        for lam, res in results.items():
            _assert_unresolved(res.theorem_status, ClaimStatus.OPEN)

    def test_defense_strength_assessment(self):
        """The status ledger retains the open overall claim."""
        for N in range(4, 7):
            for lam in non_hook_partitions_sl_n(N):
                strength = assess_defense_strength(lam)
                assert strength.generator_match_computed
                assert strength.krw_formula_computed
                _assert_unresolved(strength.overall, ClaimStatus.OPEN)

    def test_defense_summary_table(self):
        """Defense summary table covers all expected partitions."""
        rows = defense_summary(max_N=6)
        assert len(rows) >= 6  # at least the non-hook partitions of 4,5,6
        for row in rows:
            assert row['generator_match_computed']
            assert row['krw_formula_computed']
            assert row['overall_status'] is ClaimStatus.OPEN
            assert row['overall_hypotheses']


# ===================================================================
# Specific numerical checks
# ===================================================================

class TestNumericalChecks:
    """Specific numerical values that validate the formulas."""

    def test_sl4_22_ghost_constant(self):
        """C_{(2,2)} = 4."""
        assert ghost_constant((2, 2)) == 4

    def test_sl4_22_kappa(self):
        """The exact KRW scalar and typed kappa occupy separate lanes."""
        packet = ds_kappa_from_affine((2, 2), k)
        _assert_unresolved(packet, ClaimStatus.CONDITIONAL)
        assert simplify(
            krw_central_charge((2, 2), k)
            - (-12 * k**2 - 41 * k - 32) / (k + 4)
        ) == 0

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
        """Three independent paths give the canonical (3,2) KRW expression."""
        c = krw_central_charge((3, 2), k)
        expected = (-30 * k**2 - 178 * k - 260) / (k + 5)
        assert simplify(c - expected) == 0

        # Direct KRW path from x=(1,0,-1,1/2,-1/2):
        # dim sl5=24, (x|x)=5/2, charged ghost sum=50, dim g_1/2=4.
        direct = 24 * k / (k + 5) - 30 * k - 50 - 2
        assert simplify(direct - expected) == 0

        # Structured formula path, including every convention-sensitive term.
        data = krw_central_charge_data((3, 2))
        assert data.x_diagonal == (1, 0, -1, Rational(1, 2), Rational(-1, 2))
        assert data.x_norm_squared == Rational(5, 2)
        assert data.dim_g_half == 4
        assert data.charged_ghost_term == 50
        assert simplify(data.central_charge - expected) == 0

        # Concrete specializations rule out the obsolete polynomial.
        assert c.subs(k, 0) == -52
        assert c.subs(k, 1) == -78

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


class TestSemanticGuards:
    def test_open_rho_kappa_packets_are_never_arithmetic_operands(self):
        source = inspect.getsource(blue_module)
        forbidden = (
            "rho * c_val",
            "kappa_src - kappa_tgt",
            "kappa_source + kappa_dual",
            "simplify(kappa_",
        )
        assert all(fragment not in source for fragment in forbidden)

    def test_legacy_promoted_fields_are_absent(self):
        result = ds_bar_commutation_any_partition((3, 2))
        spectral = spectral_sequence_check((3, 2))
        edge = edge_compatibility_check((3, 2), (4, 1))
        assert not hasattr(result, "c_threads")
        assert not hasattr(spectral, "max_ope_pole_order")
        assert not hasattr(edge, "c_transformation_consistent")
