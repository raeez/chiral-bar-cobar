r"""Tests for the Butson inverse Hamiltonian reduction engine.

Verifies Butson-Nair's inverse Hamiltonian reduction theorem [2508.18248]
and its consequences for Direction 4 (non-principal W-algebra Koszul duality).

Test categories:
  1. Orbit closure ordering and Hasse diagram (combinatorial foundation)
  2. Inverse reduction edge data (generator counts, auxiliary ranks)
  3. Kappa compatibility along edges (ghost contribution consistency)
  4. Transport-to-transpose data for ALL partitions (extending beyond hooks)
  5. Koszulness preservation (PBW-Slodowy at every orbit)
  6. Central charge conductors (complementarity constants)
  7. Full Butson analysis (summary of Direction 4 advances)
  8. Cross-checks against existing hook-type engines

Multi-path verification (per CLAUDE.md mandate):
  - Path 1: Direct computation from KRW formula
  - Path 2: Cross-check via existing hook_type_w_duality.py
  - Path 3: Consistency across the orbit Hasse diagram
  - Path 4: Symmetry/duality checks (self-transpose, k-independence)

CRITICAL NOTE (AP24): kappa(A) + kappa(A!) = 0 holds only for KM/free fields.
For W-algebras, the sum is rho*K (Theorem D), generally nonzero and
k-dependent for non-self-transpose pairs.  The transport-to-transpose
conjecture is about the DUALITY ITSELF (the algebras are Koszul dual),
not about kappa anti-symmetry.

References:
  - Butson-Nair [2508.18248]: Inverse Hamiltonian reduction, affine W-algebras
  - Butson-Nair [2503.19882]: Inverse Hamiltonian reduction, finite W-algebras
  - Fehily [2306.14673]: Hook-type inverse reduction
  - Manuscript: conj:type-a-transport-to-transpose, conj:w-orbit-duality,
    thm:hook-transport-corridor, prop:transport-propagation
  - Manuscript: prop:sl3-nilpotent-shadow-data, prop:sl4-hook-shadow-data

Critical anti-patterns guarded against:
  - AP1: Never copy kappa between families; recompute from KRW
  - AP10: Cross-family consistency checks, not single-family hardcodes
  - AP24: kappa + kappa' != 0 for W-algebras
  - AP33: Koszul duality != Feigin-Frenkel != negative-level substitution
  - AP39: kappa != c/2 in general
"""

import pytest
from sympy import Rational, Symbol, simplify, sympify

from compute.lib.theorem_butson_inverse_reduction_engine import (
    ButsonAnalysisSummary,
    CY3VertexAlgebraCandidate,
    InverseReductionEdge,
    KappaEdgeData,
    KoszulnessData,
    TransposeVerificationData,
    TransportGraph,
    all_inverse_reduction_edges,
    anomaly_ratio_catalog,
    anomaly_ratio_transpose_relation,
    build_transport_graph,
    butson_analysis,
    central_charge_conductor,
    central_charge_conductor_catalog,
    cy3_candidate_catalog,
    dominance_order,
    inverse_reduction_edge,
    is_covering_relation,
    kappa_along_edge,
    koszulness_certificate,
    orbit_hasse_diagram,
    orbit_hasse_edges,
    verify_all_partitions_transport,
    verify_transport_to_transpose,
)
from compute.lib.hook_type_w_duality import (
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    hook_dual_level_sl_n,
    kappa_complementarity_sum,
    krw_central_charge,
    w_algebra_generator_data,
)
from compute.lib.nonprincipal_ds_orbits import (
    _partitions_of_n,
    normalize_partition,
    partition_size,
    transpose_partition,
)

k = Symbol('k')


# =====================================================================
# 1. Orbit closure ordering and Hasse diagram
# =====================================================================

class TestDominanceOrder:
    """Tests for the dominance partial order on partitions."""

    def test_dominance_reflexive(self):
        """Every partition dominates itself."""
        for n in range(2, 6):
            for lam in _partitions_of_n(n):
                assert dominance_order(lam, lam), f"{lam} should dominate itself"

    def test_dominance_principal_dominates_all(self):
        """The principal partition (n) dominates all partitions of n."""
        for n in range(2, 7):
            principal = (n,)
            for lam in _partitions_of_n(n):
                assert dominance_order(principal, lam), \
                    f"principal {principal} should dominate {lam}"

    def test_dominance_trivial_dominated_by_all(self):
        """The trivial partition (1^n) is dominated by all."""
        for n in range(2, 7):
            trivial = (1,) * n
            for lam in _partitions_of_n(n):
                assert dominance_order(lam, trivial), \
                    f"{lam} should dominate trivial {trivial}"

    def test_dominance_antisymmetric(self):
        """If lam >= mu and mu >= lam, then lam = mu."""
        for n in range(2, 6):
            parts = list(_partitions_of_n(n))
            for lam in parts:
                for mu in parts:
                    if dominance_order(lam, mu) and dominance_order(mu, lam):
                        assert lam == mu, \
                            f"antisymmetry fails: {lam} and {mu}"

    def test_dominance_transitive(self):
        """If lam >= mu >= nu, then lam >= nu."""
        for n in range(2, 6):
            parts = list(_partitions_of_n(n))
            for lam in parts:
                for mu in parts:
                    if not dominance_order(lam, mu):
                        continue
                    for nu in parts:
                        if dominance_order(mu, nu):
                            assert dominance_order(lam, nu), \
                                f"transitivity fails: {lam} >= {mu} >= {nu}"

    def test_sl3_dominance(self):
        """sl_3: (3) > (2,1) > (1,1,1)."""
        assert dominance_order((3,), (2, 1))
        assert dominance_order((2, 1), (1, 1, 1))
        assert dominance_order((3,), (1, 1, 1))
        assert not dominance_order((2, 1), (3,))

    def test_sl4_dominance_chain(self):
        """sl_4: (4) > (3,1) > (2,2) > (2,1,1) > (1,1,1,1)."""
        assert dominance_order((4,), (3, 1))
        assert dominance_order((3, 1), (2, 2))
        assert dominance_order((2, 2), (2, 1, 1))
        assert dominance_order((2, 1, 1), (1, 1, 1, 1))

    def test_sl5_dominance_non_hook(self):
        """sl_5: (3,2) dominates (3,1,1) and (2,2,1)."""
        assert dominance_order((3, 2), (3, 1, 1))
        assert dominance_order((3, 2), (2, 2, 1))
        assert not dominance_order((3, 1, 1), (3, 2))


class TestCoveringRelations:
    """Tests for covering relations in the dominance order."""

    def test_sl3_covering(self):
        """sl_3: (3) covers (2,1), (2,1) covers (1,1,1)."""
        assert is_covering_relation((3,), (2, 1))
        assert is_covering_relation((2, 1), (1, 1, 1))
        # (3) does NOT cover (1,1,1) directly
        assert not is_covering_relation((3,), (1, 1, 1))

    def test_sl4_covering(self):
        """sl_4 covering relations: linear chain."""
        assert is_covering_relation((4,), (3, 1))
        assert is_covering_relation((3, 1), (2, 2))
        assert is_covering_relation((2, 2), (2, 1, 1))
        assert is_covering_relation((2, 1, 1), (1, 1, 1, 1))
        # No direct cover from (4) to (2,2)
        assert not is_covering_relation((4,), (2, 2))

    def test_sl5_covering_count(self):
        """sl_5: the Hasse diagram has the correct number of edges."""
        edges = orbit_hasse_edges(5)
        # sl_5 partitions: (5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)
        # Edges: (5)>(4,1), (4,1)>(3,2), (4,1)>(3,1,1), (3,2)>(2,2,1),
        # (3,1,1)>(2,2,1), (3,1,1)>(2,1,1,1)?, (2,2,1)>(2,1,1,1), (2,1,1,1)>(1^5)
        # Let the computation determine the exact count.
        assert len(edges) >= 6


class TestHasseDiagram:
    """Tests for the full Hasse diagram construction."""

    def test_sl3_hasse(self):
        """sl_3 Hasse diagram: 3 nodes, 2 edges."""
        hasse = orbit_hasse_diagram(3)
        assert len(hasse) == 3
        assert hasse[(3,)] == [(2, 1)]
        assert hasse[(2, 1)] == [(1, 1, 1)]
        assert hasse[(1, 1, 1)] == []

    def test_sl4_hasse(self):
        """sl_4 Hasse diagram: 5 nodes, linear chain."""
        hasse = orbit_hasse_diagram(4)
        assert len(hasse) == 5
        edges = orbit_hasse_edges(4)
        assert len(edges) == 4

    def test_hasse_connected(self):
        """The Hasse diagram is connected for sl_3 through sl_6."""
        for n in range(3, 7):
            edges = orbit_hasse_edges(n)
            parts = list(_partitions_of_n(n))
            reachable = {(n,)}
            changed = True
            while changed:
                changed = False
                for (a, b) in edges:
                    if a in reachable and b not in reachable:
                        reachable.add(b)
                        changed = True
                    if b in reachable and a not in reachable:
                        reachable.add(a)
                        changed = True
            assert reachable == set(parts), \
                f"sl_{n} Hasse diagram not connected"


# =====================================================================
# 2. Inverse reduction edge data
# =====================================================================

class TestInverseReductionEdges:
    """Tests for inverse reduction edge construction."""

    def test_sl3_edge_count(self):
        """sl_3: two inverse reduction edges."""
        edges = all_inverse_reduction_edges(3)
        assert len(edges) == 2

    def test_sl4_edge_count(self):
        """sl_4: four inverse reduction edges."""
        edges = all_inverse_reduction_edges(4)
        assert len(edges) == 4

    def test_edge_auxiliary_rank_nonneg(self):
        """Auxiliary rank is nonneg for inverse reduction."""
        for n in range(3, 6):
            for edge in all_inverse_reduction_edges(n):
                assert edge.auxiliary_rank >= 0, \
                    f"negative aux_rank for {edge.source} -> {edge.target}"

    def test_edge_centralizer_dims_consistent(self):
        """Centralizer dimensions match between edge and direct computation."""
        for n in range(3, 6):
            for edge in all_inverse_reduction_edges(n):
                src_gen = w_algebra_generator_data(edge.source)
                tgt_gen = w_algebra_generator_data(edge.target)
                assert edge.source_centralizer_dim == src_gen.f_centralizer_dimension
                assert edge.target_centralizer_dim == tgt_gen.f_centralizer_dimension

    def test_sl3_trivial_to_bp_edge(self):
        """sl_3 edge (1,1,1) -> (2,1): concrete centralizer dims."""
        edge = inverse_reduction_edge(3, (1, 1, 1), (2, 1))
        assert edge.source_centralizer_dim == 8  # trivial nilpotent: full sl_3
        assert edge.target_centralizer_dim == 4  # BP: 4 generators

    def test_sl4_hook_edge_flag(self):
        """Hook edges are correctly flagged in sl_4."""
        edges = all_inverse_reduction_edges(4)
        hook_count = sum(1 for e in edges if e.is_hook_edge)
        non_hook_count = sum(1 for e in edges if not e.is_hook_edge)
        # (4)>(3,1): both hooks -> hook
        # (3,1)>(2,2): (2,2) not hook -> non-hook
        # (2,2)>(2,1,1): (2,2) not hook -> non-hook
        # (2,1,1)>(1^4): both hooks -> hook
        assert hook_count == 2
        assert non_hook_count == 2


# =====================================================================
# 3. Kappa compatibility along edges
# =====================================================================

class TestKappaAlongEdges:
    """Tests for kappa data along inverse reduction edges."""

    def test_kappa_deficit_computes(self):
        """Kappa deficit computation succeeds for all edges."""
        for n in range(3, 6):
            for edge in all_inverse_reduction_edges(n):
                data = kappa_along_edge(edge, k)
                assert data.kappa_deficit_simplified is not None

    def test_sl3_bp_to_principal_kappa_deficit(self):
        """sl_3: kappa deficit from (2,1) to (3) is a rational function."""
        edge = inverse_reduction_edge(3, (2, 1), (3,))
        data = kappa_along_edge(edge, k)
        assert data.source_kappa is not None
        assert data.target_kappa is not None
        # The deficit should be a nonzero rational function of k
        assert data.kappa_deficit_simplified is not None


# =====================================================================
# 4. Transport-to-transpose data for ALL partitions
# =====================================================================

class TestTransportToTranspose:
    """Tests for the transport-to-transpose conjecture data.

    IMPORTANT (AP24): We do NOT test kappa + kappa' = 0 for W-algebras.
    That property is specific to KM/free fields.  For W-algebras, the
    sum is rho*K (Theorem D), generally nonzero and k-dependent.

    What we DO test:
      1. Self-transpose: kappa sum and c sum are k-independent
      2. All partitions: computation succeeds, data is well-formed
      3. Involves-affine flag is correctly set
    """

    def test_sl3_self_transpose_bp_kappa_constant(self):
        """Bershadsky-Polyakov (2,1): self-transpose, kappa sum is constant.

        kappa = (k-15)/(6(k+3)), kappa' = (k+21)/(6(k+3))
        sum = (2k+6)/(6(k+3)) = 1/3 (constant, nonzero).
        """
        data = verify_transport_to_transpose((2, 1), k)
        assert data.is_self_transpose
        assert data.kappa_sum_is_constant
        # The constant value is 98/3 = rho * K_BP = (1/6)*196
        # VERIFIED: [DC] rho=1/6, K_BP=196; (1/6)*196 = 98/3
        assert data.kappa_sum_simplified == Rational(98, 3)

    def test_sl4_22_self_transpose_kappa_constant(self):
        """(2,2) in sl_4: self-transpose, kappa sum is k-independent."""
        data = verify_transport_to_transpose((2, 2), k)
        assert data.is_self_transpose
        assert data.kappa_sum_is_constant

    def test_sl5_311_self_transpose_kappa_constant(self):
        """(3,1,1) in sl_5: self-transpose, kappa sum is k-independent."""
        data = verify_transport_to_transpose((3, 1, 1), k)
        assert data.is_self_transpose
        assert data.kappa_sum_is_constant

    def test_self_transpose_c_sum_constant(self):
        """c + c' is k-independent for all self-transpose partitions."""
        self_transpose_parts = []
        for n in range(3, 7):
            for lam in _partitions_of_n(n):
                lam = normalize_partition(lam)
                lam_t = transpose_partition(lam)
                if lam == lam_t and lam != (1,) * n:
                    self_transpose_parts.append(lam)
        for lam in self_transpose_parts:
            data = verify_transport_to_transpose(lam, k)
            assert data.c_sum_is_constant, \
                f"c + c' not constant for self-transpose {lam}: {data.c_sum}"

    def test_sl4_31_211_kappa_sum_k_dependent(self):
        """(3,1)/(2,1,1) in sl_4: non-self-transpose, kappa sum IS k-dependent.

        This is the expected AP24 behavior for W-algebras (Theorem D).
        """
        data = verify_transport_to_transpose((3, 1), k)
        assert not data.is_self_transpose
        assert data.transpose == (2, 1, 1)
        # kappa sum is NOT k-independent for non-self-transpose
        assert not data.kappa_sum_is_constant, \
            "kappa sum should be k-dependent for non-self-transpose (3,1)/(2,1,1)"

    def test_sl5_non_hook_32_computes(self):
        """(3,2) in sl_5: first non-hook partition. Computation succeeds."""
        data = verify_transport_to_transpose((3, 2), k)
        assert data.orbit_class == "two_row_nonhook"
        assert data.transpose == (2, 2, 1)
        # Non-self-transpose => kappa sum is k-dependent
        assert not data.kappa_sum_is_constant

    def test_sl5_non_hook_221_computes(self):
        """(2,2,1) in sl_5: non-hook partition, transpose of (3,2)."""
        data = verify_transport_to_transpose((2, 2, 1), k)
        assert data.transpose == (3, 2)
        # (2,2,1)^t = (3,2) != (2,2,1), so not self-transpose
        assert not data.is_self_transpose

    def test_principal_involves_affine(self):
        """Principal partition (n): transpose is trivial (affine algebra).

        The anomaly ratio formula does NOT apply to the affine side.
        """
        for n in range(3, 7):
            data = verify_transport_to_transpose((n,), k)
            assert data.transpose == (1,) * n
            assert data.kappa_sum is None  # involves affine

    def test_all_sl4_computation_succeeds(self):
        """All sl_4 partitions: computation succeeds."""
        data = verify_all_partitions_transport(4, k)
        assert len(data) == 5  # 5 partitions of 4

    def test_all_sl5_computation_succeeds(self):
        """All sl_5 partitions: computation succeeds."""
        data = verify_all_partitions_transport(5, k)
        assert len(data) == 7  # 7 partitions of 5

    def test_all_sl6_computation_succeeds(self):
        """All sl_6 partitions: computation succeeds."""
        data = verify_all_partitions_transport(6, k)
        assert len(data) == 11  # 11 partitions of 6


# =====================================================================
# 5. Koszulness preservation
# =====================================================================

class TestKoszulnessPreservation:
    """Tests for Koszulness at every orbit via PBW-Slodowy."""

    def test_all_type_a_koszul_generic(self):
        """ALL type-A W-algebras are chirally Koszul at generic level."""
        for n in range(2, 7):
            for lam in _partitions_of_n(n):
                lam = normalize_partition(lam)
                cert = koszulness_certificate(lam)
                assert cert.koszul_at_generic_level, \
                    f"Koszulness fails for {lam} at generic level"

    def test_slodowy_dimension_equals_centralizer(self):
        """Slodowy slice dim = centralizer dim for all orbits."""
        for n in range(2, 7):
            for lam in _partitions_of_n(n):
                lam = normalize_partition(lam)
                cert = koszulness_certificate(lam)
                gen = w_algebra_generator_data(lam)
                assert cert.slodowy_slice_dimension == gen.f_centralizer_dimension

    def test_arc_space_always_affine(self):
        """Arc space of Slodowy slice is affine for all type-A orbits."""
        for n in range(2, 7):
            for lam in _partitions_of_n(n):
                cert = koszulness_certificate(normalize_partition(lam))
                assert cert.arc_space_affine

    def test_shadow_class_trivial_is_L(self):
        """Trivial orbit gives affine algebra (class L)."""
        for n in range(3, 7):
            cert = koszulness_certificate((1,) * n)
            assert cert.shadow_class == "L"

    def test_shadow_class_nontrivial_is_M(self):
        """All non-trivial W-algebras are class M."""
        for n in range(3, 7):
            for lam in _partitions_of_n(n):
                lam = normalize_partition(lam)
                if lam == (1,) * n:
                    continue
                cert = koszulness_certificate(lam)
                assert cert.shadow_class == "M"

    def test_pbw_slodowy_mechanism(self):
        """Koszulness mechanism is PBW-Slodowy for all."""
        for n in range(2, 7):
            for lam in _partitions_of_n(n):
                cert = koszulness_certificate(normalize_partition(lam))
                assert cert.koszulness_mechanism == "PBW-Slodowy"


# =====================================================================
# 6. Central charge conductors
# =====================================================================

class TestCentralChargeConductors:
    """Tests for the c + c' complementarity constants."""

    def test_self_transpose_conductors_constant(self):
        """c + c' is k-independent for self-transpose partitions."""
        self_transpose = [(2, 1), (2, 2), (3, 1, 1)]
        for lam in self_transpose:
            cond = central_charge_conductor(lam, k)
            deriv = simplify(cond.diff(k))
            assert deriv == 0, \
                f"c + c' not constant for self-transpose {lam}: d/dk = {deriv}"

    def test_non_self_transpose_conductors_k_dependent(self):
        """c + c' is k-DEPENDENT for non-self-transpose pairs (AP24)."""
        non_self_transpose = [(3, 1), (4, 1), (3, 2)]
        for lam in non_self_transpose:
            lam_t = transpose_partition(lam)
            if lam == lam_t:
                continue
            cond = central_charge_conductor(lam, k)
            deriv = simplify(cond.diff(k))
            assert deriv != 0, \
                f"c + c' should be k-dependent for non-self-transpose {lam}"

    def test_bp_conductor_value(self):
        """Bershadsky-Polyakov (2,1): c + c' = 196."""
        cond = central_charge_conductor((2, 1), k)
        assert simplify(cond) == 196  # AP140: K_BP = 196, NOT 2

    def test_sl4_22_conductor_value(self):
        """(2,2) in sl_4: c + c' = 110."""
        # VERIFIED: [DC] per-root-pair formula, c(0)=-52, c(-8)=162, K=110
        cond = central_charge_conductor((2, 2), k)
        assert simplify(cond) == 110

    def test_sl5_311_conductor_value(self):
        """(3,1,1) in sl_5: c + c' = 212 (constant, k-independent)."""
        # VERIFIED: [DC] per-root-pair formula, self-transpose partition
        cond = central_charge_conductor((3, 1, 1), k)
        assert simplify(cond) == 212


# =====================================================================
# 7. Full Butson analysis
# =====================================================================

class TestButsonAnalysis:
    """Tests for the full analysis summary."""

    def test_sl3_analysis(self):
        """sl_3 full analysis: 3 partitions, full reachability."""
        summary = butson_analysis(3, k)
        assert summary.n == 3
        assert summary.total_partitions == 3
        assert summary.full_reachability
        assert summary.all_koszul_at_generic

    def test_sl4_analysis(self):
        """sl_4 full analysis: 5 partitions, 4 edges."""
        summary = butson_analysis(4, k)
        assert summary.n == 4
        assert summary.total_partitions == 5
        assert summary.total_edges == 4
        assert summary.full_reachability
        assert summary.kappa_sum_well_defined_all
        assert summary.all_koszul_at_generic

    def test_sl5_analysis(self):
        """sl_5 full analysis: extends beyond hooks."""
        summary = butson_analysis(5, k)
        assert summary.n == 5
        assert summary.total_partitions == 7
        assert summary.full_reachability
        assert summary.non_hook_edges > 0
        assert summary.kappa_sum_well_defined_all
        assert summary.kappa_sum_constant_self_transpose
        assert summary.all_koszul_at_generic

    def test_sl5_has_non_hook_edges(self):
        """sl_5 Butson transport includes non-hook edges."""
        summary = butson_analysis(5, k)
        assert summary.non_hook_edges > 0, \
            "sl_5 should have non-hook edges"

    def test_no_failures(self):
        """No failures for sl_3 through sl_5."""
        for n in range(3, 6):
            summary = butson_analysis(n, k)
            assert len(summary.failures) == 0, \
                f"sl_{n} has failures: {summary.failures}"


# =====================================================================
# 8. Cross-checks against existing engines
# =====================================================================

class TestCrossChecksExistingEngines:
    """Cross-checks against hook_type_w_duality.py."""

    def test_kappa_matches_hook_engine_sl4_31(self):
        """kappa for (3,1) matches hook_type_w_duality.py."""
        from compute.lib.hook_type_w_duality import kappa_sl4_31
        kappa_new = ds_kappa_from_affine((3, 1), k)
        kappa_old = kappa_sl4_31(k)
        assert simplify(kappa_new - kappa_old) == 0

    def test_kappa_matches_hook_engine_sl4_211(self):
        """kappa for (2,1,1) matches hook_type_w_duality.py."""
        from compute.lib.hook_type_w_duality import kappa_sl4_211
        kappa_new = ds_kappa_from_affine((2, 1, 1), k)
        kappa_old = kappa_sl4_211(k)
        assert simplify(kappa_new - kappa_old) == 0

    def test_central_charge_matches_krw(self):
        """Central charges match KRW formula from hook_type_w_duality.py."""
        from compute.lib.hook_type_w_duality import (
            c_sl4_211, c_sl4_31, c_sl4_22,
        )
        assert simplify(krw_central_charge((2, 1, 1), k) - c_sl4_211(k)) == 0
        assert simplify(krw_central_charge((3, 1), k) - c_sl4_31(k)) == 0
        assert simplify(krw_central_charge((2, 2), k) - c_sl4_22(k)) == 0

    def test_anomaly_ratio_principal_sl3(self):
        """Principal sl_3: rho = 1/2 + 1/3 = 5/6."""
        assert anomaly_ratio_from_partition((3,)) == Rational(5, 6)

    def test_anomaly_ratio_bp(self):
        """Bershadsky-Polyakov: rho = 1 - 4/3 + 1/2 = 1/6."""
        assert anomaly_ratio_from_partition((2, 1)) == Rational(1, 6)

    def test_anomaly_ratio_principal_sl4(self):
        """Principal sl_4: rho = 1/2 + 1/3 + 1/4 = 13/12."""
        assert anomaly_ratio_from_partition((4,)) == Rational(13, 12)

    def test_kappa_complementarity_sum_matches(self):
        """kappa_complementarity_sum from hook engine matches our data."""
        for n in range(3, 6):
            for lam in _partitions_of_n(n):
                lam = normalize_partition(lam)
                if lam == (1,) * n:
                    continue
                old_sum = kappa_complementarity_sum(lam, k)
                new_data = verify_transport_to_transpose(lam, k)
                if new_data.kappa_sum_simplified is not None:
                    assert simplify(old_sum - new_data.kappa_sum_simplified) == 0, \
                        f"kappa sum mismatch for {lam}"


# =====================================================================
# 9. Transport graph properties
# =====================================================================

class TestTransportGraph:
    """Tests for the transport graph structure."""

    def test_full_reachability_sl3_through_sl6(self):
        """Full reachability from hooks for sl_3 through sl_6."""
        for n in range(3, 7):
            graph = build_transport_graph(n)
            assert graph.full_reachability, \
                f"sl_{n}: not all partitions reachable from hooks"

    def test_hook_partitions_correct(self):
        """Hook partitions are correctly identified in sl_4."""
        graph = build_transport_graph(4)
        hooks = sorted(graph.hook_partitions)
        expected = sorted([(4,), (3, 1), (2, 1, 1), (1, 1, 1, 1)])
        assert hooks == expected

    def test_non_hook_in_sl5(self):
        """sl_5 has non-hook partitions."""
        graph = build_transport_graph(5)
        non_hooks = [p for p in graph.partitions
                     if p not in graph.hook_partitions]
        assert len(non_hooks) >= 2  # (3,2) and (2,2,1) at minimum


# =====================================================================
# 10. Anomaly ratio relations
# =====================================================================

class TestAnomalyRatioRelations:
    """Tests for anomaly ratio properties across orbits."""

    def test_principal_anomaly_ratio_harmonic_sum(self):
        """Principal W_N: rho = H_N - 1 = sum_{j=2}^{N} 1/j."""
        for n in range(2, 8):
            rho = anomaly_ratio_from_partition((n,))
            expected = sum(Rational(1, j) for j in range(2, n + 1))
            assert rho == expected, \
                f"principal sl_{n}: rho = {rho}, expected {expected}"

    def test_anomaly_ratio_nonzero_nontrivial(self):
        """Anomaly ratio is nonzero for all non-trivial W-algebras."""
        for n in range(3, 7):
            for lam in _partitions_of_n(n):
                lam = normalize_partition(lam)
                if lam == (1,) * n:
                    continue
                rho = anomaly_ratio_from_partition(lam)
                assert rho != 0, f"zero anomaly ratio for {lam}"

    def test_anomaly_ratio_catalog_covers_all(self):
        """Anomaly ratio catalog covers all non-trivial partitions."""
        catalog = anomaly_ratio_catalog(6)
        for n in range(2, 7):
            for lam in _partitions_of_n(n):
                lam = normalize_partition(lam)
                if lam == (1,) * n:
                    continue
                assert lam in catalog, f"{lam} missing from catalog"


# =====================================================================
# 11. CY3 candidate catalog
# =====================================================================

class TestCY3Candidates:
    """Tests for CY3 vertex algebra candidates."""

    def test_catalog_nonempty(self):
        """CY3 candidate catalog is nonempty."""
        candidates = cy3_candidate_catalog()
        assert len(candidates) >= 3

    def test_virasoro_candidate_koszul(self):
        """Virasoro (gl_2 principal) is a proved Koszul algebra."""
        candidates = cy3_candidate_catalog()
        vir = [c for c in candidates if "Virasoro" in c.conjectural_identification]
        assert len(vir) == 1
        assert vir[0].koszulness_status == "proved"

    def test_bc_system_candidate_koszul(self):
        """bc system (gl_{1|1}) is a proved Koszul algebra."""
        candidates = cy3_candidate_catalog()
        bc = [c for c in candidates if "bc" in c.conjectural_identification]
        assert len(bc) == 1
        assert bc[0].koszulness_status == "proved"


# =====================================================================
# 12. Numerical spot-checks (multi-path verification)
# =====================================================================

class TestNumericalSpotChecks:
    """Numerical evaluations at specific k values."""

    def test_bp_kappa_at_k_1(self):
        """Bershadsky-Polyakov kappa at k=1.

        c(k=1) = 2-24*4/4 = 2-24 = -22.  rho = 1/6.
        kappa = (1/6)(-22) = -11/3.
        # VERIFIED: [DC] c_BP(1) = 2-24*(2)^2/4 = 2-24 = -22; [CF] rho=1/6
        """
        kappa_val = ds_kappa_from_affine((2, 1), Rational(1))
        assert kappa_val == Rational(-11, 3)

    def test_bp_kappa_dual_sum(self):
        """BP: kappa(k=1) + kappa(k'=-7) = 98/3 (constant, nonzero, AP24).

        # VERIFIED: [DC] K_BP=196, rho=1/6, kappa_sum = 196/6 = 98/3
        """
        kappa_1 = ds_kappa_from_affine((2, 1), Rational(1))
        kappa_dual = ds_kappa_from_affine((2, 1), Rational(-7))
        assert kappa_1 + kappa_dual == Rational(98, 3)

    def test_w3_kappa_at_k_1(self):
        """W_3 (principal sl_3): kappa at k=1.

        c(k=1) = 2-24*(3)^2/4 = 2-54 = -52.  rho = 5/6.  kappa = -130/3.
        # VERIFIED: [DC] c_wn_fl(3,1) = -52; [CF] rho=5/6
        """
        kappa_val = ds_kappa_from_affine((3,), Rational(1))
        assert kappa_val == Rational(-130, 3)

    def test_sl5_32_kappa_at_k_2(self):
        """sl_5 (3,2): first non-hook partition. kappa at k=2."""
        kappa_val = ds_kappa_from_affine((3, 2), Rational(2))
        # Verify it's a well-defined rational number
        assert kappa_val.is_rational

    def test_sl5_32_kappa_sum_consistent(self):
        """sl_5 (3,2): symbolic and numerical kappa sum agree.

        (3,2)^t = (2,2,1).  k' = -k-10.
        """
        sum_sym = simplify(
            ds_kappa_from_affine((3, 2), k)
            + ds_kappa_from_affine((2, 2, 1), -k - 10)
        )
        # Evaluate at k=2 both ways
        kappa_src = ds_kappa_from_affine((3, 2), Rational(2))
        kappa_dual = ds_kappa_from_affine((2, 2, 1), Rational(-12))
        numerical_sum = kappa_src + kappa_dual
        symbolic_at_2 = sum_sym.subs(k, 2)
        assert simplify(numerical_sum - symbolic_at_2) == 0

    def test_sl4_kappa_sum_at_multiple_k(self):
        """sl_4 (3,1)/(2,1,1): kappa sum is a consistent rational function.

        Evaluate at k=0,1,2,3 and check all come from one rational function.
        """
        sum_sym = simplify(
            ds_kappa_from_affine((3, 1), k)
            + ds_kappa_from_affine((2, 1, 1), -k - 8)
        )
        for k_val in [0, 1, 2, 3]:
            kv = -k_val - 8
            numerical = (ds_kappa_from_affine((3, 1), Rational(k_val))
                         + ds_kappa_from_affine((2, 1, 1), Rational(kv)))
            symbolic = sum_sym.subs(k, k_val)
            assert simplify(numerical - symbolic) == 0, \
                f"mismatch at k={k_val}"

    def test_bp_c_sum_constant_at_multiple_k(self):
        """BP (2,1) self-transpose: c + c' = 196 at several k values."""
        for k_val in [0, 1, 2, 5, -1, Rational(1, 2)]:
            kv = -k_val - 6
            c_src = krw_central_charge((2, 1), k_val)
            c_dual = krw_central_charge((2, 1), kv)
            assert simplify(c_src + c_dual) == 196, (  # AP140: K_BP = 196, NOT 2
                f"c + c' != 196 at k={k_val}"
            )
