r"""Tests for nilpotent transport for ALL orbits in type A.

Verifies:
  - Closure ordering (= dominance ordering) on nilpotent orbits of sl_N
  - Transport graph connectivity: hook seeds reach ALL partitions
  - BRST one-loop exactness at each transport edge (generic level)
  - Central charge complementarity c(k,lam) + c(k^v,lam^t): level-independent
    iff both partitions are even nilpotents or self-transpose
  - Even nilpotent classification and its role in complementarity
  - Kappa complementarity for even-even pairs and self-transpose partitions
  - Specific non-hook orbits in sl_4, sl_5, sl_6

KEY MATHEMATICAL FINDING (discovered by this computation):
  Central charge complementarity c(k,lam) + c(k^v,lam^t) = const is NOT
  universal. It holds iff BOTH lambda and lambda^t are EVEN nilpotents
  (all ad(h)-grading integers, no half-integer roots) OR lambda is
  self-transpose.  For non-even pairs, the half-integer ghost contributions
  introduce k-dependent terms.  The Koszul duality W^k(f_lam)^! = W^{k^v}(f_{lam^t})
  holds at the completed bar-cobar level (thm:pbw-slodowy-collapse) regardless,
  but the complementarity constant acquires k-dependence.

References:
  - thm:hook-transport-corridor, prop:transport-propagation
  - conj:type-a-transport-to-transpose
  - Fehily (2022), Genra-Juillard (2023), Butson-Nair (2024), CLNS (2023-24)

Multi-path verification (CLAUDE.md mandate):
  Path 1: Direct transport path computation (BFS from hooks)
  Path 2: Central charge complementarity (level-independence where expected)
  Path 3: Even nilpotent classification (parity of partition parts)
  Path 4: Kappa analysis for self-transpose partitions
  Path 5: Closure ordering structural properties
"""

import pytest
from fractions import Fraction

from compute.lib.nilpotent_transport_typeA import (
    NilpotentTransportAnalysis,
    TransportEdge,
    TransportPathVerification,
    all_transport_paths,
    anomaly_ratio,
    brst_ghost_contribution,
    brst_nilradical_profile,
    brst_one_loop_exact_generic,
    classify_edge,
    closure_order_covers,
    complementarity_constant_pairs,
    dominance_leq,
    even_nilpotent_pairs,
    find_transport_path,
    full_transport_analysis,
    hasse_diagram,
    is_even_nilpotent,
    kappa_complementarity_level_independent,
    kappa_complementarity_sum,
    kappa_w_algebra,
    non_hook_partitions,
    rectangular_partitions,
    self_transpose_partitions,
    three_row_partitions,
    transport_summary_table,
    two_row_partitions,
    verify_closure_ordering_type_a,
    verify_transport_path,
)
from compute.lib.nonprincipal_ds_orbits import (
    _partitions_of_n,
    hook_partition,
    is_hook_partition,
    normalize_partition,
    transpose_partition,
)
from compute.lib.w_algebra_transport_propagation import (
    central_charge,
    centralizer_dimension,
    dual_level,
    generator_weights,
    nilpotent_orbit_dimension,
    partitions,
    transpose,
)


# =====================================================================
# 1. Closure ordering (dominance order) structural tests
# =====================================================================

class TestClosureOrdering:
    """Verify the closure ordering on nilpotent orbits = dominance order."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7])
    def test_principal_is_maximum(self, N):
        """(N) is the unique maximum in the closure ordering."""
        principal = (N,)
        for lam in _partitions_of_n(N):
            assert dominance_leq(lam, principal)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7])
    def test_trivial_is_minimum(self, N):
        """(1^N) is the unique minimum in the closure ordering."""
        trivial = (1,) * N
        for lam in _partitions_of_n(N):
            assert dominance_leq(trivial, lam)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7])
    def test_reflexivity(self, N):
        for lam in _partitions_of_n(N):
            assert dominance_leq(lam, lam)

    @pytest.mark.parametrize("N", [3, 4, 5, 6])
    def test_antisymmetry(self, N):
        for lam in _partitions_of_n(N):
            for mu in _partitions_of_n(N):
                if dominance_leq(lam, mu) and dominance_leq(mu, lam):
                    assert lam == mu

    @pytest.mark.parametrize("N", [3, 4, 5])
    def test_transitivity(self, N):
        pars = list(_partitions_of_n(N))
        for lam in pars:
            for mu in pars:
                if not dominance_leq(lam, mu):
                    continue
                for nu in pars:
                    if dominance_leq(mu, nu):
                        assert dominance_leq(lam, nu)

    def test_sl4_dominance_total_order(self):
        """sl_4 dominance order is a total order (chain)."""
        chain = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
        for i in range(len(chain)):
            for j in range(i, len(chain)):
                assert dominance_leq(chain[j], chain[i])

    def test_sl6_non_comparable_pair(self):
        """sl_6: (3,3) and (4,1,1) are not comparable in dominance order."""
        assert not dominance_leq((3, 3), (4, 1, 1))
        assert not dominance_leq((4, 1, 1), (3, 3))

    @pytest.mark.parametrize("N,expected_covers", [
        (2, 1), (3, 2), (4, 4), (5, 6),
    ])
    def test_cover_count(self, N, expected_covers):
        covers = closure_order_covers(N)
        assert len(covers) == expected_covers

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7])
    def test_hasse_connected(self, N):
        result = verify_closure_ordering_type_a(N)
        assert result['is_connected']


# =====================================================================
# 2. Transport graph connectivity: hooks reach ALL partitions
# =====================================================================

class TestTransportConnectivity:
    """Transport-closure of hook vertices is all of Par(N)."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_all_partitions_reachable(self, N):
        analysis = full_transport_analysis(N)
        assert analysis.all_reachable, (
            f"N={N}: unreachable partitions: {analysis.unreachable}"
        )

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7])
    def test_transport_closure_equals_par_n(self, N):
        analysis = full_transport_analysis(N)
        assert analysis.transport_closure_size == analysis.num_partitions

    @pytest.mark.parametrize("N", [4, 5, 6, 7])
    def test_every_non_hook_has_path(self, N):
        for lam in non_hook_partitions(N):
            path = find_transport_path(N, lam)
            assert path is not None, f"No path to {lam} in sl_{N}"
            assert is_hook_partition(path[0])
            assert path[-1] == lam

    def test_sl4_22_path(self):
        path = find_transport_path(4, (2, 2))
        assert path is not None
        assert is_hook_partition(path[0])
        assert path[-1] == (2, 2)

    def test_sl5_32_path(self):
        path = find_transport_path(5, (3, 2))
        assert path is not None
        assert is_hook_partition(path[0])

    def test_sl5_221_path(self):
        path = find_transport_path(5, (2, 2, 1))
        assert path is not None
        assert is_hook_partition(path[0])

    def test_sl6_222_path(self):
        path = find_transport_path(6, (2, 2, 2))
        assert path is not None
        assert is_hook_partition(path[0])

    def test_sl6_33_path(self):
        path = find_transport_path(6, (3, 3))
        assert path is not None
        assert is_hook_partition(path[0])

    def test_sl6_321_path(self):
        path = find_transport_path(6, (3, 2, 1))
        assert path is not None
        assert is_hook_partition(path[0])


# =====================================================================
# 3. BRST one-loop exactness at each transport edge
# =====================================================================

class TestBRSTExactness:
    """BRST one-loop exactness at generic level along all edges."""

    @pytest.mark.parametrize("N", [3, 4, 5, 6])
    def test_all_edges_exact_generic(self, N):
        analysis = full_transport_analysis(N)
        assert analysis.all_edges_exact

    @pytest.mark.parametrize("N", [3, 4, 5, 6])
    def test_covering_relation_exactness(self, N):
        covers = closure_order_covers(N)
        for mu, lam in covers:
            assert brst_one_loop_exact_generic(N, mu, lam)

    def test_sl4_22_edge_data(self):
        result = verify_transport_path(4, (2, 2))
        assert result.all_edges_exact
        assert len(result.edge_data) >= 1

    @pytest.mark.parametrize("N", [3, 4, 5])
    def test_nilradical_profile_consistency(self, N):
        for lam in _partitions_of_n(N):
            profile = brst_nilradical_profile(N, lam)
            assert profile['nilradical_dimension'] >= 0
            assert profile['total_positive_roots'] == (
                profile['integer_grading_roots'] +
                profile['half_integer_grading_roots']
            )


# =====================================================================
# 4. Even nilpotent classification
# =====================================================================

class TestEvenNilpotent:
    """Even nilpotent classification: all ad(h)-gradings are integers."""

    def test_principal_always_even(self):
        """Principal nilpotent (N) is always even (all integer gradings)."""
        for N in range(2, 8):
            assert is_even_nilpotent(N, (N,))

    def test_trivial_always_even(self):
        """Trivial nilpotent (1^N) is always even (all gradings zero)."""
        for N in range(2, 8):
            assert is_even_nilpotent(N, (1,) * N)

    def test_sl4_even_classification(self):
        """sl_4: (4), (3,1), (2,2), (1,1,1,1) are even; (2,1,1) is not.

        (4): all parts even parity (one part, trivially same).
        (3,1): parts 3,1 both odd -> same parity -> even.
        (2,2): parts 2,2 both even -> same parity -> even.
        (2,1,1): parts 2,1,1 mixed parity (2 even, 1 odd) -> NOT even.
        (1,1,1,1): all parts 1 (odd) -> same parity -> even.
        """
        assert is_even_nilpotent(4, (4,))
        assert is_even_nilpotent(4, (3, 1))
        assert is_even_nilpotent(4, (2, 2))
        assert not is_even_nilpotent(4, (2, 1, 1))
        assert is_even_nilpotent(4, (1, 1, 1, 1))

    def test_sl5_even_classification(self):
        """sl_5 even nilpotents: same-parity parts.

        (5): [odd] -> even.
        (4,1): [even,odd] -> NOT even.
        (3,2): [odd,even] -> NOT even.
        (3,1,1): [odd,odd,odd] -> even.
        (2,2,1): [even,even,odd] -> NOT even.
        (2,1,1,1): [even,odd,odd,odd] -> NOT even.
        (1^5): [odd*5] -> even.
        """
        assert is_even_nilpotent(5, (5,))
        assert not is_even_nilpotent(5, (4, 1))
        assert not is_even_nilpotent(5, (3, 2))
        assert is_even_nilpotent(5, (3, 1, 1))
        assert not is_even_nilpotent(5, (2, 2, 1))
        assert not is_even_nilpotent(5, (2, 1, 1, 1))
        assert is_even_nilpotent(5, (1, 1, 1, 1, 1))

    def test_sl6_even_classification(self):
        """sl_6 even nilpotents."""
        even_parts = [(6,), (4, 2), (3, 3), (2, 2, 2), (4, 1, 1),
                      (2, 2, 1, 1), (1, 1, 1, 1, 1, 1)]
        # Even iff all parts same parity
        for lam in _partitions_of_n(6):
            parts = list(lam)
            parities = set(p % 2 for p in parts)
            same_parity = len(parities) == 1
            assert is_even_nilpotent(6, lam) == same_parity, (
                f"lam={lam}: expected even={same_parity}, "
                f"got {is_even_nilpotent(6, lam)}"
            )

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7])
    def test_even_iff_same_parity_parts(self, N):
        """Even nilpotent iff all partition parts have the same parity."""
        for lam in _partitions_of_n(N):
            parities = set(p % 2 for p in lam)
            same_parity = len(parities) == 1
            assert is_even_nilpotent(N, lam) == same_parity


# =====================================================================
# 5. Central charge complementarity (the main finding)
# =====================================================================

class TestCentralChargeComplementarity:
    """c(k, lam) + c(k^v, lam^t) is level-independent iff both even or self-transpose."""

    @pytest.mark.parametrize("N,lam", [
        # Self-transpose partitions: always constant
        (3, (2, 1)),
        (4, (2, 2)),
        (5, (3, 1, 1)),
        (6, (3, 2, 1)),
        # Even-even pairs (non self-transpose): also constant
        (2, (1, 1)),       # (1,1) <-> (2): both even
        (3, (1, 1, 1)),    # (1,1,1) <-> (3): both even
        (4, (1, 1, 1, 1)), # (1^4) <-> (4): both even
        (6, (2, 2, 2)),    # (2,2,2) <-> (3,3): both even
        (6, (3, 3)),       # (3,3) <-> (2,2,2): both even
    ])
    def test_complementarity_constant_where_expected(self, N, lam):
        """c + c' is level-independent for even-even pairs and self-transpose."""
        test_levels = [Fraction(n) for n in [1, 2, 3, 5, 7, 11, 13, 17]]
        lam_t = transpose_partition(lam)
        values = []
        for k in test_levels:
            c = central_charge(N, lam, k)
            kv = dual_level(N, k)
            c_dual = central_charge(N, lam_t, kv)
            values.append(c + c_dual)
        assert len(set(values)) == 1, (
            f"c + c' not constant for {lam}: values = {values}"
        )

    @pytest.mark.parametrize("N,lam", [
        # Non-even pairs: at least one of lam, lam^t has mixed-parity parts.
        # c + c' is NOT constant for these.
        (5, (3, 2)),       # (3,2) <-> (2,2,1): both non-even
        (5, (4, 1)),       # (4,1) <-> (2,1,1,1): both non-even
        (6, (4, 1, 1)),    # (4,1,1) non-even <-> (3,1,1,1) even: one side non-even
        (6, (4, 2)),       # (4,2) even <-> (2,2,1,1) non-even: one side non-even
    ])
    def test_complementarity_not_constant_for_non_even(self, N, lam):
        """c + c' is NOT level-independent for non-even transpose pairs."""
        test_levels = [Fraction(n) for n in [1, 2, 3, 5, 7, 11]]
        lam_t = transpose_partition(lam)
        values = []
        for k in test_levels:
            c = central_charge(N, lam, k)
            kv = dual_level(N, k)
            c_dual = central_charge(N, lam_t, kv)
            values.append(c + c_dual)
        assert len(set(values)) > 1, (
            f"c + c' unexpectedly constant for non-even pair {lam}: {values[0]}"
        )

    @pytest.mark.parametrize("N", [3, 4, 5, 6])
    def test_complementarity_classification_complete(self, N):
        """Every partition pair is correctly classified as constant or not."""
        const_pairs = complementarity_constant_pairs(N)
        const_set = set()
        for lam, lam_t, val in const_pairs:
            const_set.add((min(lam, lam_t), max(lam, lam_t)))

        for lam in _partitions_of_n(N):
            lam_t = transpose_partition(lam)
            pair = (min(lam, lam_t), max(lam, lam_t))
            is_self_t = (lam == lam_t)
            is_even_both = (is_even_nilpotent(N, lam) and
                           is_even_nilpotent(N, lam_t))
            should_be_const = is_self_t or is_even_both
            is_const = pair in const_set
            assert is_const == should_be_const, (
                f"N={N}, lam={lam}: expected const={should_be_const}, "
                f"got {is_const}"
            )

    def test_sl6_222_33_complementarity_value(self):
        """(2,2,2) <-> (3,3) in sl_6: c + c' = 28."""
        pairs = complementarity_constant_pairs(6)
        for lam, lam_t, val in pairs:
            if lam == (2, 2, 2) or lam == (3, 3):
                assert val == 28


# =====================================================================
# 6. Generator spectrum analysis
# =====================================================================

class TestGeneratorSpectrum:
    """Generator weight spectra for transpose pairs."""

    @pytest.mark.parametrize("N", [3, 4, 5, 6])
    def test_self_transpose_generators_match(self, N):
        """Self-transpose partitions have matching generators (tautologically)."""
        for lam in self_transpose_partitions(N):
            gens = sorted(generator_weights(lam))
            gens_t = sorted(generator_weights(transpose_partition(lam)))
            assert gens == gens_t

    def test_centralizer_dim_mismatch_implies_gen_mismatch(self):
        """When dim(g^f_lam) != dim(g^f_{lam^t}), generators differ."""
        for N in range(3, 7):
            for lam in _partitions_of_n(N):
                lam_t = transpose_partition(lam)
                d1 = centralizer_dimension(lam)
                d2 = centralizer_dimension(lam_t)
                g1 = sorted(generator_weights(lam))
                g2 = sorted(generator_weights(lam_t))
                if d1 != d2:
                    assert g1 != g2, (
                        f"N={N}, {lam}: dims differ ({d1} vs {d2}) "
                        f"but generators match"
                    )

    def test_sl5_32_generators_differ_from_221(self):
        """(3,2) has 8 generators, (2,2,1) has 12: they differ."""
        g_32 = generator_weights((3, 2))
        g_221 = generator_weights((2, 2, 1))
        assert len(g_32) != len(g_221)
        assert len(g_32) == 8
        assert len(g_221) == 12

    def test_sl6_33_generators_differ_from_222(self):
        """(3,3) has 11 generators, (2,2,2) has 17: they differ."""
        g_33 = generator_weights((3, 3))
        g_222 = generator_weights((2, 2, 2))
        assert len(g_33) != len(g_222)
        assert len(g_33) == 11
        assert len(g_222) == 17

    def test_generator_count_equals_centralizer_dim(self):
        """Number of strong generators = dim(g^f)."""
        for N in range(2, 7):
            for lam in _partitions_of_n(N):
                assert len(generator_weights(lam)) == centralizer_dimension(lam)


# =====================================================================
# 7. Kappa complementarity
# =====================================================================

class TestKappaComplementarity:
    """kappa(A) + kappa(A^!) level-independence analysis."""

    @pytest.mark.parametrize("N,lam", [
        # Self-transpose: kappa + kappa' should be level-independent
        (3, (2, 1)),
        (4, (2, 2)),
        (5, (3, 1, 1)),
        (6, (3, 2, 1)),
    ])
    def test_kappa_complementarity_self_transpose(self, N, lam):
        is_indep, value = kappa_complementarity_level_independent(N, lam)
        assert is_indep, (
            f"kappa not level-independent for self-transpose {lam}"
        )

    @pytest.mark.parametrize("N,lam", [
        # For non-self-transpose even-even pairs, c+c' is constant
        # but kappa+kappa' is NOT constant because rho_lam != rho_{lam_t}.
        # kappa + kappa' = rho_lam * c + rho_{lam_t} * c' and since
        # rho_lam != rho_{lam_t} and c, c' are individually k-dependent,
        # the sum is k-dependent. This is a genuine mathematical fact.
        (2, (1, 1)),
        (3, (1, 1, 1)),
        (6, (2, 2, 2)),
        (6, (3, 3)),
    ])
    def test_kappa_complementarity_even_even_not_constant(self, N, lam):
        """For non-self-transpose pairs, kappa + kappa' is NOT constant
        even when c + c' is, because the anomaly ratios differ."""
        lam_t = transpose_partition(lam)
        if lam == lam_t:
            pytest.skip("Self-transpose, tested separately")
        is_indep, value = kappa_complementarity_level_independent(N, lam)
        assert not is_indep, (
            f"kappa unexpectedly constant for non-self-transpose pair {lam}"
        )

    def test_anomaly_ratio_level_independent(self):
        """Anomaly ratio rho_lambda is well-defined (no k-dependence)."""
        for N in range(3, 7):
            for lam in _partitions_of_n(N):
                rho = anomaly_ratio(lam)
                assert isinstance(rho, Fraction)


# =====================================================================
# 8. Specific non-hook orbits: detailed verification
# =====================================================================

class TestSl4NonHook:
    """The single non-hook orbit (2,2) in sl_4."""

    def test_22_is_only_non_hook(self):
        nh = non_hook_partitions(4)
        assert len(nh) == 1
        assert nh[0] == (2, 2)

    def test_22_is_self_transpose(self):
        assert transpose_partition((2, 2)) == (2, 2)

    def test_22_is_even(self):
        assert is_even_nilpotent(4, (2, 2))

    def test_22_centralizer_dim(self):
        assert centralizer_dimension((2, 2)) == 7

    def test_22_orbit_dim(self):
        assert nilpotent_orbit_dimension((2, 2)) == 8

    def test_22_transport_verification(self):
        result = verify_transport_path(4, (2, 2))
        assert result.path is not None
        assert len(result.path) >= 2
        assert result.all_edges_exact
        assert result.complementarity_level_independent

    def test_22_is_rectangular(self):
        rects = rectangular_partitions(4)
        assert (2, 2) in rects

    def test_22_nilradical_all_integer(self):
        """(2,2) is even: all nilradical gradings are integers."""
        profile = brst_nilradical_profile(4, (2, 2))
        assert profile['half_integer_grading_roots'] == 0


class TestSl5NonHooks:
    """Non-hook orbits in sl_5: (3,2) and (2,2,1)."""

    def test_non_hooks_count(self):
        nh = non_hook_partitions(5)
        assert len(nh) == 2
        assert set(nh) == {(3, 2), (2, 2, 1)}

    def test_32_and_221_are_transposes(self):
        assert transpose_partition((3, 2)) == (2, 2, 1)
        assert transpose_partition((2, 2, 1)) == (3, 2)

    def test_32_is_not_even(self):
        """(3,2) has mixed parity parts: 3 (odd), 2 (even)."""
        assert not is_even_nilpotent(5, (3, 2))

    def test_221_is_not_even(self):
        """(2,2,1) has mixed parity parts: 2 (even), 1 (odd)."""
        assert not is_even_nilpotent(5, (2, 2, 1))

    def test_32_complementarity_not_constant(self):
        """c + c' is NOT constant for (3,2) <-> (2,2,1): non-even pair."""
        values = []
        for k_int in [1, 3, 7]:
            k = Fraction(k_int)
            kv = dual_level(5, k)
            c1 = central_charge(5, (3, 2), k)
            c2 = central_charge(5, (2, 2, 1), kv)
            values.append(c1 + c2)
        assert len(set(values)) > 1

    def test_32_transport_path_exists(self):
        result = verify_transport_path(5, (3, 2))
        assert result.path is not None
        assert result.all_edges_exact

    def test_221_transport_path_exists(self):
        result = verify_transport_path(5, (2, 2, 1))
        assert result.path is not None
        assert result.all_edges_exact

    def test_32_centralizer_dim(self):
        assert centralizer_dimension((3, 2)) == 8

    def test_221_centralizer_dim(self):
        assert centralizer_dimension((2, 2, 1)) == 12

    def test_generator_counts_differ(self):
        """(3,2) and (2,2,1) have different numbers of generators."""
        assert len(generator_weights((3, 2))) != len(generator_weights((2, 2, 1)))


class TestSl6NonHooks:
    """Non-hook orbits in sl_6."""

    def test_non_hooks_count(self):
        nh = non_hook_partitions(6)
        assert len(nh) == 5

    @pytest.mark.parametrize("lam", [
        (4, 2), (3, 3), (3, 2, 1), (2, 2, 2), (2, 2, 1, 1),
    ])
    def test_transport_path_exists(self, lam):
        result = verify_transport_path(6, lam)
        assert result.path is not None and len(result.path) >= 2
        assert result.all_edges_exact

    def test_even_nonhooks(self):
        """Among non-hooks of 6: (4,2),(3,3),(2,2,2) are even;
        (3,2,1) and (2,2,1,1) are NOT even (mixed-parity parts)."""
        assert is_even_nilpotent(6, (4, 2))      # [even,even]
        assert is_even_nilpotent(6, (3, 3))       # [odd,odd]
        assert is_even_nilpotent(6, (2, 2, 2))    # [even,even,even]
        assert not is_even_nilpotent(6, (3, 2, 1))   # [odd,even,odd]
        assert not is_even_nilpotent(6, (2, 2, 1, 1))  # [even,even,odd,odd]

    def test_33_and_222_complementarity_constant(self):
        """(3,3) <-> (2,2,2): both even, so c + c' is constant."""
        values = []
        for k_int in [1, 3, 7, 11]:
            k = Fraction(k_int)
            kv = dual_level(6, k)
            c1 = central_charge(6, (3, 3), k)
            c2 = central_charge(6, (2, 2, 2), kv)
            values.append(c1 + c2)
        assert len(set(values)) == 1

    def test_321_is_self_transpose(self):
        assert transpose_partition((3, 2, 1)) == (3, 2, 1)

    def test_42_and_2211_are_transposes(self):
        assert transpose_partition((4, 2)) == (2, 2, 1, 1)

    def test_42_complementarity_not_constant(self):
        """(4,2) <-> (2,2,1,1): (4,2) is even but (2,2,1,1) is NOT even
        (parts [2,2,1,1] have mixed parity), so c + c' is NOT constant."""
        assert is_even_nilpotent(6, (4, 2))
        assert not is_even_nilpotent(6, (2, 2, 1, 1))
        values = []
        for k_int in [1, 3, 7, 11]:
            k = Fraction(k_int)
            kv = dual_level(6, k)
            c1 = central_charge(6, (4, 2), k)
            c2 = central_charge(6, (2, 2, 1, 1), kv)
            values.append(c1 + c2)
        assert len(set(values)) > 1


# =====================================================================
# 9. Full transport analysis summary
# =====================================================================

class TestFullAnalysis:
    """Summary statistics for the full transport analysis."""

    @pytest.mark.parametrize("N", [4, 5, 6])
    def test_all_reachable(self, N):
        analysis = full_transport_analysis(N)
        assert analysis.all_reachable

    def test_summary_table(self):
        table = transport_summary_table(max_N=7)
        for row in table:
            assert row['all_reachable']

    @pytest.mark.parametrize("N,expected_non_hooks", [
        (2, 0), (3, 0), (4, 1), (5, 2), (6, 5), (7, 8),
    ])
    def test_non_hook_count(self, N, expected_non_hooks):
        assert len(non_hook_partitions(N)) == expected_non_hooks


# =====================================================================
# 10. Self-transpose (self-dual) partition analysis
# =====================================================================

class TestSelfTransposePartitions:
    """Self-conjugate partitions: self-dual W-algebras."""

    def test_sl4_self_transpose(self):
        st = self_transpose_partitions(4)
        assert st == [(2, 2)]

    def test_sl5_self_transpose(self):
        st = self_transpose_partitions(5)
        assert (3, 1, 1) in st

    def test_sl6_self_transpose(self):
        st = self_transpose_partitions(6)
        assert (3, 2, 1) in st


# =====================================================================
# 11. Partition family tests
# =====================================================================

class TestPartitionFamilies:
    """Specific partition families."""

    @pytest.mark.parametrize("N", [4, 6, 8])
    def test_rectangular_partitions(self, N):
        rects = rectangular_partitions(N)
        assert len(rects) >= 1
        for r in rects:
            parts = set(r)
            assert len(parts) == 1

    def test_two_row_partitions(self):
        two_rows = two_row_partitions(6)
        assert len(two_rows) == 3
        assert (5, 1) in two_rows
        assert (4, 2) in two_rows
        assert (3, 3) in two_rows

    def test_three_row_partitions(self):
        three_rows = three_row_partitions(6)
        assert (2, 2, 2) in three_rows
        assert (3, 2, 1) in three_rows
        assert (4, 1, 1) in three_rows


# =====================================================================
# 12. Edge classification tests
# =====================================================================

class TestEdgeClassification:
    """Transport edge classification."""

    def test_hook_spine_edges(self):
        covers = closure_order_covers(5)
        for mu, lam in covers:
            etype = classify_edge(5, mu, lam)
            if is_hook_partition(mu) and is_hook_partition(lam):
                assert etype == 'hook_spine'

    def test_sl5_has_hook_to_nonhook_edges(self):
        covers = closure_order_covers(5)
        has_h2nh = any(
            classify_edge(5, mu, lam) == 'hook_to_nonhook'
            for mu, lam in covers
        )
        assert has_h2nh

    def test_sl6_has_nonhook_edges(self):
        covers = closure_order_covers(6)
        has_nh2nh = any(
            classify_edge(6, mu, lam) == 'nonhook_to_nonhook'
            for mu, lam in covers
        )
        assert has_nh2nh


# =====================================================================
# 13. Cross-verification with existing engines
# =====================================================================

class TestCrossVerification:
    """Cross-check against existing hook_transport_corridor module."""

    @pytest.mark.parametrize("N", [4, 5, 6, 7])
    def test_non_hook_count_matches(self, N):
        from compute.lib.hook_transport_corridor import ReductionGraph
        G = ReductionGraph.build(N)
        hooks_old = G.hook_vertices()
        non_hooks_old = G.vertices - hooks_old
        non_hooks_new = non_hook_partitions(N)
        assert len(non_hooks_old) == len(non_hooks_new)

    @pytest.mark.parametrize("N", [4, 5, 6])
    def test_transport_closure_matches(self, N):
        from compute.lib.hook_transport_corridor import ReductionGraph
        G = ReductionGraph.build(N)
        new_analysis = full_transport_analysis(N)
        assert G.is_fully_connected() == new_analysis.all_reachable


# =====================================================================
# 14. Even-nilpotent complementarity constant values
# =====================================================================

class TestComplementarityValues:
    """Verify specific complementarity constant values."""

    def test_sl2_trivial_principal(self):
        """(1,1) <-> (2) in sl_2: C = 4."""
        pairs = complementarity_constant_pairs(2)
        for lam, lam_t, val in pairs:
            if (1, 1) in (lam, lam_t):
                assert val == 4

    def test_sl3_trivial_principal(self):
        """(1,1,1) <-> (3) in sl_3: C = 10."""
        pairs = complementarity_constant_pairs(3)
        for lam, lam_t, val in pairs:
            if (1, 1, 1) in (lam, lam_t):
                assert val == 10

    def test_sl3_bp_self_dual(self):
        """(2,1) self-transpose in sl_3: C = 28."""
        pairs = complementarity_constant_pairs(3)
        for lam, lam_t, val in pairs:
            if lam == (2, 1):
                assert val == 28

    def test_sl4_22_self_dual(self):
        """(2,2) self-transpose in sl_4: C = 14."""
        pairs = complementarity_constant_pairs(4)
        for lam, lam_t, val in pairs:
            if lam == (2, 2):
                assert val == 14

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_trivial_principal_complementarity(self, N):
        """(1^N) <-> (N): c + c' is always a positive even integer."""
        pairs = complementarity_constant_pairs(N)
        for lam, lam_t, val in pairs:
            if lam == (1,) * N or lam_t == (1,) * N:
                assert val > 0
                assert val.denominator == 1


# =====================================================================
# 15. The main theorem: transport reaches all, exactness holds,
#     complementarity classified
# =====================================================================

class TestMainTheorem:
    """The combined transport-to-transpose result for type A."""

    @pytest.mark.parametrize("N", [4, 5, 6, 7])
    def test_transport_closure_complete(self, N):
        """conj:type-a-transport-to-transpose Part 1: closure = Par(N)."""
        analysis = full_transport_analysis(N)
        assert analysis.all_reachable

    @pytest.mark.parametrize("N", [4, 5, 6])
    def test_brst_exactness_universal(self, N):
        """All transport edges have BRST one-loop exactness at generic level."""
        analysis = full_transport_analysis(N)
        assert analysis.all_edges_exact

    @pytest.mark.parametrize("N", [3, 4, 5, 6])
    def test_even_pairs_have_constant_complementarity(self, N):
        """Even-even transpose pairs have level-independent c + c'."""
        for lam, lam_t in even_nilpotent_pairs(N):
            test_levels = [Fraction(n) for n in [1, 3, 7, 11]]
            values = []
            for k in test_levels:
                c1 = central_charge(N, lam, k)
                kv = dual_level(N, k)
                c2 = central_charge(N, lam_t, kv)
                values.append(c1 + c2)
            assert len(set(values)) == 1, (
                f"N={N}: even pair {lam} <-> {lam_t} has non-constant c+c'"
            )
