r"""Tests for qec_koszul_code_engine.py.

Verification strategy:
  1. Weight-level Hilbert space dimensions (partition counts)
  2. Symplectic code construction at each weight
  3. Code parameters for 5+ algebras
  4. Knill-Laflamme verification via three independent paths
  5. Code distance vs shadow depth (multi-path)
  6. Encoding/decoding round-trip
  7. Logical operators from Koszul dual
  8. Threshold error rate estimates
  9. Holographic tensor network construction
  10. Decoupling bounds
  11. Comparison with HaPPY, Steane, toric codes
  12. Multi-path cross-checks
  13. Full code dictionary
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.qec_koszul_code_engine import (
    # Weight dimensions
    partition_count,
    heisenberg_weight_dim,
    affine_sl2_weight_dim,
    virasoro_weight_dim,
    betagamma_weight_dim,
    # Symplectic code
    symplectic_code_at_weight,
    code_parameters_at_weight,
    code_parameters_up_to_weight,
    # Heisenberg codes
    heisenberg_code_parameters,
    heisenberg_code_parameter_table,
    # Knill-Laflamme (3 paths)
    knill_laflamme_path1_lagrangian,
    knill_laflamme_path2_direct,
    knill_laflamme_path2_genus2,
    knill_laflamme_path3_complementarity,
    verify_knill_laflamme_three_paths,
    # Code distance
    code_distance_from_shadow_depth,
    code_distance_census,
    # Encoding/decoding
    encoding_decoding_structure,
    bar_cobar_round_trip_dimensions,
    # Logical operators
    logical_operators_from_koszul_pair,
    # Threshold
    threshold_from_shadow_radius,
    threshold_census,
    # Tensor network
    bar_complex_tensor_network,
    # Decoupling
    decoupling_bound,
    # Comparisons
    compare_with_happy,
    compare_with_steane,
    compare_with_toric,
    # Dictionary
    full_code_dictionary,
    code_summary_report,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    shadow_depth_class,
)


# ===================================================================
#  1. WEIGHT-LEVEL HILBERT SPACE DIMENSIONS
# ===================================================================

class TestPartitionCounts:
    """Partition function p(n) for Heisenberg weight dimensions."""

    def test_p0(self):
        assert partition_count(0) == 1

    def test_p1(self):
        assert partition_count(1) == 1

    def test_p2(self):
        assert partition_count(2) == 2

    def test_p3(self):
        assert partition_count(3) == 3

    def test_p4(self):
        assert partition_count(4) == 5

    def test_p5(self):
        assert partition_count(5) == 7

    def test_p10(self):
        assert partition_count(10) == 42

    def test_p_negative(self):
        assert partition_count(-1) == 0


class TestWeightDimensions:
    """Hilbert space dimensions at each weight level."""

    def test_heisenberg_rank1_low_weights(self):
        """Heisenberg rank 1: p(h)."""
        expected = [1, 1, 2, 3, 5, 7]
        for h, exp in enumerate(expected):
            assert heisenberg_weight_dim(h, 1) == exp, f"h={h}"

    def test_heisenberg_rank2_weight0(self):
        """Rank 2 at weight 0 is 1."""
        assert heisenberg_weight_dim(0, 2) == 1

    def test_heisenberg_rank2_weight1(self):
        """Rank 2 at weight 1: two generators."""
        assert heisenberg_weight_dim(1, 2) == 2

    def test_affine_sl2_weight0(self):
        """Affine sl_2: dim V_0 = 1 (vacuum)."""
        assert affine_sl2_weight_dim(0) == 1

    def test_affine_sl2_weight1(self):
        """Affine sl_2: dim V_1 = 3 (adjoint)."""
        assert affine_sl2_weight_dim(1) == 3

    def test_virasoro_weight0(self):
        """Virasoro: dim V_0 = 1 (vacuum)."""
        assert virasoro_weight_dim(0) == 1

    def test_virasoro_weight1(self):
        """Virasoro: dim V_1 = 0 (no weight-1 states; generator has weight 2)."""
        assert virasoro_weight_dim(1) == 0

    def test_virasoro_weight2(self):
        """Virasoro: dim V_2 = 1 (L_{-2}|0>)."""
        assert virasoro_weight_dim(2) == 1

    def test_virasoro_weight4(self):
        """Virasoro: dim V_4 = 2 (L_{-4}|0>, L_{-2}^2|0>)."""
        assert virasoro_weight_dim(4) == 2

    def test_virasoro_weight6(self):
        """Virasoro: dim V_6 = 4 (partitions of 6 into parts >= 2)."""
        assert virasoro_weight_dim(6) == 4

    def test_betagamma_weight0(self):
        """Beta-gamma: dim V_0 = 1."""
        assert betagamma_weight_dim(0) == 1

    def test_betagamma_weight1(self):
        """Beta-gamma: dim V_1 = 2 (two rank-1 generators contribute)."""
        assert betagamma_weight_dim(1) == 2


# ===================================================================
#  2. SYMPLECTIC CODE CONSTRUCTION
# ===================================================================

class TestSymplecticCode:
    """Symplectic code at individual weight levels."""

    def test_heisenberg_weight0(self):
        code = symplectic_code_at_weight('heisenberg', 0)
        assert code['n_h'] == 2  # 2 * p(0) = 2
        assert code['k_h'] == 1
        assert code['rate'] == Fraction(1, 2)
        assert code['lagrangian'] is True
        assert code['symplectic'] is True

    def test_heisenberg_weight2(self):
        code = symplectic_code_at_weight('heisenberg', 2)
        assert code['n_h'] == 4  # 2 * p(2) = 4
        assert code['k_h'] == 2

    def test_heisenberg_weight5(self):
        code = symplectic_code_at_weight('heisenberg', 5)
        assert code['n_h'] == 14  # 2 * p(5) = 14
        assert code['k_h'] == 7

    def test_virasoro_weight2(self):
        code = symplectic_code_at_weight('virasoro', 2)
        assert code['n_h'] == 2  # 2 * 1 = 2
        assert code['k_h'] == 1

    def test_rate_always_half(self):
        """Rate = 1/2 universally (Lagrangian)."""
        for fam in ['heisenberg', 'virasoro', 'affine', 'betagamma']:
            for h in range(8):
                code = symplectic_code_at_weight(fam, h)
                if code['n_h'] > 0:
                    assert code['rate'] == Fraction(1, 2), f"{fam}, h={h}"

    def test_code_parameters_tuple(self):
        n, k, d = code_parameters_at_weight('heisenberg', 0)
        assert n == 2
        assert k == 1
        assert d == 2


class TestAggregateCodeParameters:
    """Aggregate code parameters up to h_max."""

    def test_heisenberg_aggregate(self):
        params = code_parameters_up_to_weight('heisenberg', 5)
        assert params['N'] == 2 * params['K']
        assert params['rate'] == Fraction(1, 2)
        assert params['D'] == 2

    def test_virasoro_aggregate(self):
        params = code_parameters_up_to_weight('virasoro', 6)
        assert params['N'] == 2 * params['K']
        assert params['rate'] == Fraction(1, 2)

    def test_affine_aggregate(self):
        params = code_parameters_up_to_weight('affine', 5)
        assert params['N'] == 2 * params['K']
        assert params['rate'] == Fraction(1, 2)

    def test_aggregate_monotone(self):
        """N increases with h_max."""
        prev_N = 0
        for h_max in range(8):
            params = code_parameters_up_to_weight('heisenberg', h_max)
            assert params['N'] >= prev_N
            prev_N = params['N']


# ===================================================================
#  3. HEISENBERG CODE PARAMETERS
# ===================================================================

class TestHeisenbergCodes:
    """Explicit code parameters for Heisenberg H_k."""

    def test_h1_parameters(self):
        params = heisenberg_code_parameters(1, h_max=5)
        assert params['kappa'] == 1
        assert params['shadow_class'] == 'G'
        assert params['redundancy_channels'] == 0
        assert params['exact_recovery'] is True
        assert params['rate'] == Fraction(1, 2)

    def test_h1_dimensions(self):
        """H_1 up to weight 5: N = 2*(1+1+2+3+5+7) = 38."""
        params = heisenberg_code_parameters(1, h_max=5)
        expected_K = 1 + 1 + 2 + 3 + 5 + 7  # p(0) + ... + p(5)
        assert params['K'] == expected_K
        assert params['N'] == 2 * expected_K

    def test_table_length(self):
        table = heisenberg_code_parameter_table(10)
        assert len(table) == 10

    def test_table_all_rate_half(self):
        table = heisenberg_code_parameter_table(5)
        assert all(t['rate'] == Fraction(1, 2) for t in table)

    def test_table_all_class_G(self):
        table = heisenberg_code_parameter_table(5)
        assert all(t['shadow_class'] == 'G' for t in table)

    def test_table_all_zero_redundancy(self):
        table = heisenberg_code_parameter_table(5)
        assert all(t['redundancy_channels'] == 0 for t in table)

    def test_table_kappa_values(self):
        """kappa(H_k) = k."""
        table = heisenberg_code_parameter_table(5)
        for i, entry in enumerate(table):
            assert entry['kappa'] == i + 1


# ===================================================================
#  4. KNILL-LAFLAMME (THREE PATHS)
# ===================================================================

class TestKnillLaflamme:
    """Knill-Laflamme verification via three independent paths."""

    def test_path1_lagrangian_isotropy(self):
        result = knill_laflamme_path1_lagrangian()
        assert result['isotropy_verified'] is True
        assert result['kl_genus_1'] is True
        assert result['cross_pairing_sign'] == -1

    def test_path2_direct_genus1(self):
        result = knill_laflamme_path2_direct()
        assert result['kl_verified'] is True
        assert result['isotropy_verified'] is True
        assert result['cross_pairing_verified'] is True
        assert abs(result['isotropy_code']) < 1e-10
        assert abs(result['isotropy_error']) < 1e-10

    def test_path2_direct_genus2(self):
        result = knill_laflamme_path2_genus2(dim_code=2)
        assert result['isotropy_verified'] is True
        assert result['cross_pairing_verified'] is True
        # KL for Lagrangian-preserving errors
        assert result['kl_lagrangian_preserving'] == result['kl_total_tested']

    def test_path2_direct_genus2_larger(self):
        result = knill_laflamme_path2_genus2(dim_code=5)
        assert result['isotropy_verified'] is True
        assert result['kl_verified'] is True

    def test_path3_complementarity_c13(self):
        result = knill_laflamme_path3_complementarity(Rational(13))
        assert result['code_fraction'] == Rational(1, 2)
        assert result['self_dual'] is True
        assert result['kl_structural'] is True

    def test_path3_complementarity_c1(self):
        result = knill_laflamme_path3_complementarity(Rational(1))
        assert result['kappa'] == Rational(1, 2)
        assert result['kappa_dual'] == Rational(25, 2)
        assert result['kappa_sum'] == 13

    def test_three_paths_agree(self):
        result = verify_knill_laflamme_three_paths()
        assert result['all_paths_agree'] is True
        assert result['num_paths'] == 3


# ===================================================================
#  5. CODE DISTANCE VS SHADOW DEPTH
# ===================================================================

class TestCodeDistance:
    """Code distance from shadow depth via three paths."""

    def test_heisenberg_distance(self):
        result = code_distance_from_shadow_depth('heisenberg')
        assert result['arity_distance'] == 2
        assert result['redundancy_channels'] == 0
        assert result['all_paths_agree'] is True

    def test_affine_distance(self):
        result = code_distance_from_shadow_depth('affine')
        assert result['arity_distance'] == 2
        assert result['redundancy_channels'] == 1
        assert result['all_paths_agree'] is True

    def test_betagamma_distance(self):
        result = code_distance_from_shadow_depth('betagamma')
        assert result['arity_distance'] == 2
        assert result['redundancy_channels'] == 2
        assert result['all_paths_agree'] is True

    def test_virasoro_distance(self):
        result = code_distance_from_shadow_depth('virasoro')
        assert result['arity_distance'] == 2
        assert result['redundancy_channels'] == -1  # infinite
        assert result['all_paths_agree'] is True

    def test_distance_universal(self):
        """Arity distance = 2 for ALL families."""
        census = code_distance_census()
        for fam, data in census.items():
            assert data['arity_distance'] == 2, f"Family {fam}"

    def test_three_distance_paths_agree(self):
        """All three paths agree for every family."""
        census = code_distance_census()
        for fam, data in census.items():
            assert data['all_paths_agree'], f"Family {fam}"


# ===================================================================
#  6. ENCODING/DECODING ROUND-TRIP
# ===================================================================

class TestEncodingDecoding:
    """Bar-cobar encoding/decoding round-trip."""

    def test_structure_heisenberg(self):
        result = encoding_decoding_structure('heisenberg', h=2)
        assert result['round_trip'] == 'quasi-isomorphism'
        assert result['exact_recovery'] is True

    def test_structure_virasoro(self):
        result = encoding_decoding_structure('virasoro', h=4)
        assert result['exact_recovery'] is True

    def test_round_trip_dimensions_heisenberg(self):
        """Dimensions preserved at each weight."""
        data = bar_cobar_round_trip_dimensions('heisenberg', 6)
        assert all(d['match'] for d in data)
        assert all(d['dim_in'] == d['dim_out'] for d in data)

    def test_round_trip_dimensions_virasoro(self):
        data = bar_cobar_round_trip_dimensions('virasoro', 8)
        assert all(d['match'] for d in data)

    def test_round_trip_dimensions_affine(self):
        data = bar_cobar_round_trip_dimensions('affine', 5)
        assert all(d['match'] for d in data)

    def test_ap25_note(self):
        """AP25: bar-cobar recovers A itself, NOT A!."""
        result = encoding_decoding_structure('heisenberg', h=1)
        assert 'Omega(B(A)) = A' in result['note_ap25']
        assert 'Verdier duality' in result['note_ap25']


# ===================================================================
#  7. LOGICAL OPERATORS
# ===================================================================

class TestLogicalOperators:
    """Logical operators from the Koszul dual pair."""

    def test_virasoro_c13_self_dual(self):
        result = logical_operators_from_koszul_pair('virasoro', c_val=Rational(13))
        assert result['kappa_x'] == Rational(13, 2)
        assert result['kappa_z'] == Rational(13, 2)
        assert result['commutation_nondegenerate'] is True
        assert result['complementarity_check']['self_dual'] is True

    def test_virasoro_c1(self):
        result = logical_operators_from_koszul_pair('virasoro', c_val=Rational(1))
        assert result['kappa_x'] == Rational(1, 2)
        assert result['kappa_z'] == Rational(25, 2)
        assert result['complementarity_check']['kappa_sum'] == 13

    def test_virasoro_c26(self):
        """At c=26: kappa=13, kappa'=0 (critical string)."""
        result = logical_operators_from_koszul_pair('virasoro', c_val=Rational(26))
        assert result['kappa_x'] == Rational(13)
        assert result['kappa_z'] == Rational(0)
        assert result['kappa_x'] + result['kappa_z'] == 13

    def test_commutation_nondegenerate_all(self):
        """Cross-pairing is non-degenerate for all families."""
        for c in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            result = logical_operators_from_koszul_pair('virasoro', c_val=c)
            assert result['commutation_nondegenerate'] is True


# ===================================================================
#  8. THRESHOLD ERROR RATE
# ===================================================================

class TestThreshold:
    """Threshold error rate from shadow radius."""

    def test_heisenberg_trivial(self):
        result = threshold_from_shadow_radius('heisenberg')
        assert result['convergent'] is True
        assert result['p_threshold_shadow'] == 1.0

    def test_affine_trivial(self):
        result = threshold_from_shadow_radius('affine')
        assert result['convergent'] is True
        assert result['p_threshold_shadow'] == 1.0

    def test_virasoro_c13_convergent(self):
        result = threshold_from_shadow_radius('virasoro', c_val=13)
        assert result['convergent'] is True
        assert result['p_threshold_shadow'] > 0

    def test_virasoro_c26_convergent(self):
        result = threshold_from_shadow_radius('virasoro', c_val=26)
        assert result['convergent'] is True
        assert result['p_threshold_shadow'] > 0

    def test_virasoro_c_half_divergent(self):
        """c=1/2: rho > 1, divergent."""
        result = threshold_from_shadow_radius('virasoro', c_val=Rational(1, 2))
        assert result['convergent'] is False
        assert result['p_threshold_shadow'] == 0.0

    def test_threshold_ordering(self):
        """Higher c gives lower rho, hence higher threshold."""
        t13 = threshold_from_shadow_radius('virasoro', c_val=13)
        t26 = threshold_from_shadow_radius('virasoro', c_val=26)
        assert t26['p_threshold_shadow'] >= t13['p_threshold_shadow']

    def test_threshold_census_completeness(self):
        census = threshold_census()
        assert len(census) >= 5
        assert 'heisenberg' in census
        assert 'virasoro_c=13' in census


# ===================================================================
#  9. HOLOGRAPHIC TENSOR NETWORK
# ===================================================================

class TestTensorNetwork:
    """Holographic tensor network from bar complex."""

    def test_heisenberg_tree(self):
        result = bar_complex_tensor_network('heisenberg', 3)
        assert result['num_vertices'] == 3
        assert result['num_edges'] == 2
        assert result['graph_type'] == 'tree'
        assert result['min_cut_edges'] == 1

    def test_virasoro_tree(self):
        result = bar_complex_tensor_network('virasoro', 5, c=13)
        assert result['num_vertices'] == 5
        assert result['num_edges'] == 4

    def test_tensor_arities_class_G(self):
        """Class G: only arity 2."""
        result = bar_complex_tensor_network('heisenberg', 3)
        assert 2 in result['tensor_arities']

    def test_rt_formula_present(self):
        result = bar_complex_tensor_network('heisenberg', 3)
        assert 'area' in result['rt_formula']
        assert 'G_Newton' in result['rt_formula']


# ===================================================================
#  10. DECOUPLING BOUNDS
# ===================================================================

class TestDecouplingBounds:
    """Decoupling bounds from shadow CohFT."""

    def test_1_logical(self):
        result = decoupling_bound(Rational(1), k_logical=1)
        assert result['N_min'] == 2
        assert result['rate'] == Fraction(1, 2)

    def test_k_logical(self):
        result = decoupling_bound(Rational(1), k_logical=5)
        assert result['N_min'] == 10
        assert result['rate'] == Fraction(1, 2)

    def test_lagrangian_bound(self):
        """N >= 2k always (Lagrangian)."""
        for k in range(1, 10):
            result = decoupling_bound(Rational(1), k_logical=k)
            assert result['N_min'] >= 2 * k


# ===================================================================
#  11. COMPARISON WITH KNOWN CODES
# ===================================================================

class TestCodeComparisons:
    """Comparison with HaPPY, Steane, toric codes."""

    def test_happy_comparison_structure(self):
        result = compare_with_happy()
        assert result['correspondence_count'] == 4
        assert 'symplectic' in result['koszul_code']['type']
        assert 'stabilizer' in result['happy_code']['type']

    def test_happy_correspondences(self):
        result = compare_with_happy()
        assert len(result['correspondences']) == 4

    def test_steane_rate_mismatch(self):
        result = compare_with_steane()
        assert result['rate_match'] is False
        assert result['steane_code']['n'] == 7
        assert result['steane_code']['k'] == 1

    def test_steane_obstruction(self):
        """Koszul codes have rate 1/2; Steane has rate 1/7."""
        result = compare_with_steane()
        assert result['koszul_rate'] == Fraction(1, 2)
        assert result['steane_code']['rate'] == Fraction(1, 7)

    def test_toric_correspondence(self):
        result = compare_with_toric()
        assert result['structural_correspondence'] is True

    def test_toric_candidate(self):
        result = compare_with_toric()
        assert result['koszul_candidate']['shadow_class'] == 'G'


# ===================================================================
#  12. MULTI-PATH CROSS-CHECKS
# ===================================================================

class TestMultiPathCrossChecks:
    """Cross-checks that verify consistency across computations."""

    def test_kl_distance_consistent(self):
        """KL verified AND distance = 2 for all families."""
        kl = verify_knill_laflamme_three_paths()
        assert kl['all_paths_agree']
        census = code_distance_census()
        for fam, data in census.items():
            assert data['arity_distance'] == 2

    def test_lagrangian_rate_universal(self):
        """Rate = 1/2 from Lagrangian structure, for all families at all weights."""
        for fam in ['heisenberg', 'virasoro', 'affine', 'betagamma']:
            params = code_parameters_up_to_weight(fam, 5)
            assert params['rate'] == Fraction(1, 2), f"Family {fam}"

    def test_shadow_class_redundancy_consistent(self):
        """Shadow class determines redundancy channels."""
        expected = {'G': 0, 'L': 1, 'C': 2, 'M': -1}
        for fam, cls in [('heisenberg', 'G'), ('affine', 'L'),
                          ('betagamma', 'C'), ('virasoro', 'M')]:
            result = code_distance_from_shadow_depth(fam)
            assert result['shadow_class'] == cls
            assert result['redundancy_channels'] == expected[cls]

    def test_encoding_decoding_kl_consistent(self):
        """Exact recovery (encoding/decoding) implies KL at genus 1."""
        enc = encoding_decoding_structure('heisenberg', h=0)
        assert enc['exact_recovery'] is True
        kl = knill_laflamme_path2_direct()
        assert kl['kl_verified'] is True

    def test_complementarity_kl_threshold_consistent(self):
        """Complementarity (path 3) + shadow radius (threshold) consistent."""
        for c in [Rational(1), Rational(13), Rational(26)]:
            kl = knill_laflamme_path3_complementarity(c)
            thr = threshold_from_shadow_radius('virasoro', c_val=c)
            # Both should confirm the code exists
            assert kl['kl_structural'] is True
            # Convergence status matches expectation
            if float(c) > 7:
                assert thr['convergent'] is True


# ===================================================================
#  13. FULL CODE DICTIONARY
# ===================================================================

class TestFullDictionary:
    """The complete algebra -> code parameters dictionary."""

    def test_dictionary_length(self):
        d = full_code_dictionary(5)
        assert len(d) >= 5

    def test_all_rate_half(self):
        d = full_code_dictionary(5)
        assert all(entry['rate'] == Fraction(1, 2) for entry in d)

    def test_all_distance_2(self):
        d = full_code_dictionary(5)
        assert all(entry['D'] == 2 for entry in d)

    def test_heisenberg_entries(self):
        """H_1 through H_5 in dictionary."""
        d = full_code_dictionary(5)
        heis = [e for e in d if 'Heisenberg' in e['family']]
        assert len(heis) == 5
        kappas = [e['kappa'] for e in heis]
        assert kappas == [1, 2, 3, 4, 5]

    def test_shadow_classes(self):
        """Dictionary includes all four shadow classes."""
        d = full_code_dictionary(5)
        classes = set(e['shadow_class'] for e in d)
        assert 'G' in classes
        assert 'L' in classes
        assert 'C' in classes
        assert 'M' in classes

    def test_summary_report(self):
        report = code_summary_report(5)
        assert 'Heisenberg' in report
        assert 'Lagrangian' in report
        assert 'rate = 1/2' in report

    def test_virasoro_convergence(self):
        """Virasoro c=13 convergent, c=1/2 divergent."""
        d = full_code_dictionary(5)
        c13 = [e for e in d if 'c=13' in e['family']][0]
        c_half = [e for e in d if 'c=1/2' in e['family']][0]
        assert c13['convergent'] is True
        assert c_half['convergent'] is False


# ===================================================================
#  14. ADDITIONAL MULTI-PATH VERIFICATIONS
# ===================================================================

class TestAdditionalVerifications:
    """Additional tests for mathematical consistency."""

    def test_partition_count_monotone(self):
        """p(n) is non-decreasing for n >= 0."""
        prev = 0
        for n in range(20):
            curr = partition_count(n)
            assert curr >= prev, f"p({n}) = {curr} < p({n-1}) = {prev}"
            prev = curr

    def test_virasoro_no_weight1(self):
        """Virasoro has no weight-1 states (generator at weight 2)."""
        assert virasoro_weight_dim(1) == 0

    def test_virasoro_dimensions_growth(self):
        """Virasoro dimensions grow with weight (for h >= 2)."""
        prev = 0
        for h in range(2, 20, 2):
            curr = virasoro_weight_dim(h)
            assert curr >= prev, f"Virasoro dim at h={h}"
            prev = curr

    def test_heisenberg_code_N_equals_2K(self):
        """N = 2K universally for Heisenberg (Lagrangian)."""
        for k in range(1, 6):
            params = heisenberg_code_parameters(k, h_max=8)
            assert params['N'] == 2 * params['K']

    def test_kl_genus2_larger_dims(self):
        """KL at genus 2 with dim 3, 5, 7."""
        for dim in [3, 5, 7]:
            result = knill_laflamme_path2_genus2(dim_code=dim)
            assert result['isotropy_verified'] is True
            assert result['kl_verified'] is True

    def test_code_distance_all_families_equal_2(self):
        """All standard families have arity distance 2."""
        for fam in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            result = code_distance_from_shadow_depth(fam)
            assert result['arity_distance'] == 2

    def test_threshold_self_dual_value(self):
        """At c=13 (self-dual), rho ~ 0.467, threshold ~ 0.533."""
        result = threshold_from_shadow_radius('virasoro', c_val=13)
        assert 0.4 < result['rho'] < 0.5
        assert 0.5 < result['p_threshold_shadow'] < 0.6

    def test_tensor_network_edges_correct(self):
        """Tree with n vertices has n-1 edges."""
        for n in range(2, 10):
            result = bar_complex_tensor_network('heisenberg', n)
            assert result['num_edges'] == n - 1

    def test_decoupling_scales_linearly(self):
        """N_min = 2k (linear scaling from Lagrangian)."""
        for k in range(1, 20):
            result = decoupling_bound(Rational(1), k_logical=k)
            assert result['N_min'] == 2 * k

    def test_happy_vs_koszul_type_difference(self):
        """HaPPY is orthogonal, Koszul is symplectic."""
        result = compare_with_happy()
        assert 'orthogonal' in result['happy_code']['type']
        assert 'symplectic' in result['koszul_code']['type']
