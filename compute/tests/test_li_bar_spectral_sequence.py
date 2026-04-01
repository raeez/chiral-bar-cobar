"""
Tests for the Li-bar spectral sequence and the associated-variety audit surface.

Verifies:
- constr:li-bar-spectral-sequence (Li filtration multiplicativity)
- prop:li-bar-poisson-differential (Poisson bracket = d_1)
- thm:associated-variety-koszulness (reduced-level geometric criterion)
- cor:minimal-orbit-koszul (conditional minimal-orbit route)
- prop:large-orbit-obstruction (large orbit obstruction)
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from li_bar_spectral_sequence import (
    partitions,
    orbit_dimension,
    is_minimal_orbit,
    is_regular_orbit,
    is_zero_orbit,
    springer_resolution_cohomology,
    minimal_orbit_poisson_cohomology,
    sl2_nilcone_poisson_cohomology,
    koszulness_prediction,
    orbit_hierarchy_table,
    admissible_orbit_sl2,
    barbasch_vogan_dual_partition,
    verify_li_filtration_multiplicativity,
    analyze_li_bar_degeneration,
    verify_orbit_duality_compatibility,
)


# ──────────────────────────────────────────────────────────
# Partition combinatorics
# ──────────────────────────────────────────────────────────

class TestPartitions:
    def test_partitions_small(self):
        assert partitions(1) == [(1,)]
        assert partitions(2) == [(2,), (1, 1)]
        assert partitions(3) == [(3,), (2, 1), (1, 1, 1)]
        assert len(partitions(4)) == 5
        assert len(partitions(5)) == 7

    def test_partition_count_6(self):
        assert len(partitions(6)) == 11

    def test_partitions_sum_correct(self):
        for n in range(1, 8):
            for lam in partitions(n):
                assert sum(lam) == n


# ──────────────────────────────────────────────────────────
# Orbit dimensions
# ──────────────────────────────────────────────────────────

class TestOrbitDimension:
    def test_zero_orbit_dim_0(self):
        """Zero orbit has dimension 0 for all N."""
        for N in range(2, 10):
            assert orbit_dimension(tuple([1] * N), N) == 0

    def test_regular_orbit_dim(self):
        """Regular orbit has dim N^2 - N for sl_N."""
        for N in range(2, 10):
            assert orbit_dimension((N,), N) == N * N - N

    def test_minimal_orbit_dim(self):
        """Minimal orbit has dim 2(N-1) for sl_N."""
        for N in range(2, 10):
            lam = tuple([2] + [1] * (N - 2))
            assert orbit_dimension(lam, N) == 2 * (N - 1)

    def test_subregular_orbit_dim_sl3(self):
        """Subregular orbit (2,1) in sl_3 has dim 4."""
        assert orbit_dimension((2, 1), 3) == 4

    def test_subregular_orbit_dim_sl4(self):
        """Subregular orbit (3,1) in sl_4 has dim 10."""
        assert orbit_dimension((3, 1), 4) == 10

    def test_orbit_dim_nonnegative(self):
        """All orbit dimensions should be non-negative."""
        for N in range(2, 8):
            for lam in partitions(N):
                assert orbit_dimension(lam, N) >= 0

    def test_orbit_dim_even(self):
        """All nilpotent orbit dimensions are even."""
        for N in range(2, 8):
            for lam in partitions(N):
                assert orbit_dimension(lam, N) % 2 == 0


# ──────────────────────────────────────────────────────────
# Orbit classification
# ──────────────────────────────────────────────────────────

class TestOrbitClassification:
    def test_zero_orbit(self):
        for N in range(2, 8):
            assert is_zero_orbit(tuple([1] * N), N)
            assert not is_zero_orbit((N,), N)

    def test_minimal_orbit(self):
        for N in range(2, 8):
            lam = tuple([2] + [1] * (N - 2))
            assert is_minimal_orbit(lam, N)

    def test_regular_orbit(self):
        for N in range(2, 8):
            assert is_regular_orbit((N,), N)
            assert not is_regular_orbit(tuple([1] * N), N)


# ──────────────────────────────────────────────────────────
# External reduced-geometry comparison models
# ──────────────────────────────────────────────────────────

class TestGeometricComparisonModels:
    def test_sl2_nilcone_concentrated(self):
        """sl_2 nilcone comparison model is concentrated in degree 0."""
        hp = sl2_nilcone_poisson_cohomology()
        assert hp[0] == -1  # infinite-dimensional H^0
        # No higher cohomology
        for n in range(1, 10):
            assert hp.get(n, 0) == 0

    def test_minimal_orbit_concentrated(self):
        """Minimal-orbit comparison model is concentrated in degree 0."""
        for N in range(2, 8):
            hp = minimal_orbit_poisson_cohomology(N)
            assert hp[0] == -1
            for n in range(1, 10):
                assert hp.get(n, 0) == 0

    def test_springer_sl2_concentrated(self):
        """Springer comparison model for sl_2 is concentrated."""
        hp = springer_resolution_cohomology(2)
        for n in range(1, 10):
            assert hp.get(n, 0) == 0

    def test_springer_all_concentrated(self):
        """The chosen Springer comparison model is concentrated for all N."""
        for N in range(2, 8):
            hp = springer_resolution_cohomology(N)
            for n in range(1, 10):
                assert hp.get(n, 0) == 0, \
                    f"H^{n}(T*(G/B), O) should vanish for sl_{N}"


# ──────────────────────────────────────────────────────────
# Koszulness predictions
# ──────────────────────────────────────────────────────────

class TestKoszulnessPredictions:
    def test_zero_requires_nilradical_check(self):
        for N in range(2, 10):
            assert koszulness_prediction('zero', N) == 'reduced-point; nilradical-dependent'

    def test_minimal_is_conditional_on_reducedness(self):
        for N in range(2, 10):
            assert koszulness_prediction('minimal', N) == 'conditional on reducedness'

    def test_regular_nilradical_dependent(self):
        """Regular orbit Koszulness is nilradical-dependent for all N."""
        for N in range(2, 10):
            assert koszulness_prediction('regular', N) == 'nilradical-dependent'

    def test_subregular_nilradical_dependent(self):
        """Subregular orbit Koszulness is nilradical-dependent."""
        for N in range(2, 10):
            assert koszulness_prediction('subregular', N) == 'nilradical-dependent'

    def test_admissible_sl2_examples_are_partial_not_global(self):
        """Only documented sl_2 orbit examples are encoded unconditionally."""
        assert admissible_orbit_sl2(3, 2) == 'zero'
        assert admissible_orbit_sl2(2, 3) == 'regular'
        assert admissible_orbit_sl2(5, 3) == 'under_audit'


# ──────────────────────────────────────────────────────────
# Barbasch-Vogan duality
# ──────────────────────────────────────────────────────────

class TestBarbaschVoganDuality:
    def test_bv_is_involution(self):
        """BV duality (= transpose) is an involution."""
        for N in range(2, 8):
            for lam in partitions(N):
                lam_t = barbasch_vogan_dual_partition(lam)
                lam_tt = barbasch_vogan_dual_partition(lam_t)
                assert lam_tt == lam, f"BV not involution for {lam}"

    def test_bv_zero_to_regular(self):
        """BV maps zero orbit to regular orbit for sl_N."""
        for N in range(2, 8):
            zero_part = tuple([1] * N)
            dual = barbasch_vogan_dual_partition(zero_part)
            assert dual == (N,), f"BV({zero_part}) = {dual}, expected ({N},)"

    def test_bv_minimal_to_subregular(self):
        """BV maps minimal to subregular for sl_N, N >= 3."""
        for N in range(3, 8):
            min_part = tuple([2] + [1] * (N - 2))
            dual = barbasch_vogan_dual_partition(min_part)
            expected = tuple([N - 1, 1])
            assert dual == expected, f"BV({min_part}) = {dual}, expected {expected}"

    def test_bv_preserves_partition_sum(self):
        """BV dual partition sums to same N."""
        for N in range(2, 8):
            for lam in partitions(N):
                lam_t = barbasch_vogan_dual_partition(lam)
                assert sum(lam_t) == N


# ──────────────────────────────────────────────────────────
# Li filtration
# ──────────────────────────────────────────────────────────

class TestLiFiltration:
    def test_poisson_lowers_by_1(self):
        """a_{(0)} b should lower Li filtration by 1."""
        filt = verify_li_filtration_multiplicativity()
        for p, q in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0)]:
            assert filt[(p, q, 0)]['filtration_level'] == p + q - 1

    def test_product_preserves(self):
        """a_{(-1)} b should preserve Li filtration."""
        filt = verify_li_filtration_multiplicativity()
        for p, q in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0)]:
            assert filt[(p, q, -1)]['filtration_level'] == p + q

    def test_negative_modes_preserve(self):
        """a_{(-2)} b should preserve Li filtration."""
        filt = verify_li_filtration_multiplicativity()
        for p, q in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            assert filt[(p, q, -2)]['filtration_level'] == p + q

    def test_higher_modes_lower_more(self):
        """a_{(n)} b with n >= 1 should lower filtration by more than 1."""
        filt = verify_li_filtration_multiplicativity()
        for p, q in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            for n in [1, 2, 3]:
                level = filt[(p, q, n)]['filtration_level']
                assert level <= p + q - 2, \
                    f"a_({{n}}) b should lower filtration by >= 2 for n={n}"

    def test_d1_from_poisson(self):
        """The d_1 differential should come from the Poisson bracket."""
        filt = verify_li_filtration_multiplicativity()
        # a_{(0)} contributes to d_1
        for p, q in [(0, 0), (1, 0), (0, 1)]:
            assert filt[(p, q, 0)]['contributes_to'] == 'd_1'


# ──────────────────────────────────────────────────────────
# Degeneration analysis
# ──────────────────────────────────────────────────────────

class TestDegenerationAnalysis:
    def test_zero_orbit_reduced_concentration_only(self):
        for N in [2, 3, 4, 5]:
            result = analyze_li_bar_degeneration('zero', N)
            assert 'nilradical-dependent' in result['koszul_conclusion']
            assert result['E_2_diagonal'] is True

    def test_minimal_orbit_is_conditional(self):
        for N in [2, 3, 4, 5]:
            result = analyze_li_bar_degeneration('minimal', N)
            assert result['koszul_conclusion'] == 'conditional on reducedness of gr^F L_k'
            assert result['E_2_diagonal'] is True

    def test_regular_reduced_concentrated(self):
        """Regular orbit: reduced comparison model is concentrated for all N."""
        for N in [2, 3, 4, 5]:
            result = analyze_li_bar_degeneration('regular', N)
            assert result['E_2_diagonal'] is True  # reduced part
            assert 'nilradical' in result['koszul_conclusion']


# ──────────────────────────────────────────────────────────
# Orbit hierarchy
# ──────────────────────────────────────────────────────────

class TestOrbitHierarchy:
    def test_hierarchy_table_complete(self):
        """Hierarchy table should have one entry per partition."""
        for N in range(2, 6):
            table = orbit_hierarchy_table(N)
            parts = partitions(N)
            assert len(table) == len(parts)

    def test_hierarchy_endpoints(self):
        """Zero orbit dim 0, regular orbit dim N^2 - N."""
        for N in range(2, 6):
            table = orbit_hierarchy_table(N)
            zero = [e for e in table if e['orbit_type'] == 'zero']
            reg = [e for e in table if e['orbit_type'] == 'regular']
            assert len(zero) == 1
            assert zero[0]['orbit_dim'] == 0
            assert len(reg) == 1
            assert reg[0]['orbit_dim'] == N * N - N

    def test_hierarchy_monotone(self):
        """Orbit dimensions should be non-negative even integers."""
        for N in range(2, 6):
            table = orbit_hierarchy_table(N)
            for entry in table:
                assert entry['orbit_dim'] >= 0
                assert entry['orbit_dim'] % 2 == 0


# ──────────────────────────────────────────────────────────
# Orbit duality compatibility
# ──────────────────────────────────────────────────────────

class TestOrbitDualityCompatibility:
    def test_duality_compatible(self):
        """All orbit duality pairs should be compatible."""
        for N in range(2, 6):
            results = verify_orbit_duality_compatibility(N)
            for r in results:
                assert r['compatible'], \
                    f"Incompatible at {r['partition']}"

    def test_zero_dual_regular(self):
        """Zero orbit should be BV-dual to regular orbit."""
        for N in range(2, 6):
            results = verify_orbit_duality_compatibility(N)
            zero_entry = [r for r in results
                         if r['orbit_type'] == 'zero'][0]
            assert zero_entry['dual_orbit_type'] == 'regular'


# ──────────────────────────────────────────────────────────
# Integration tests
# ──────────────────────────────────────────────────────────

class TestIntegration:
    def test_sl2_complete_picture(self):
        """Complete verification for sl_2.

        sl_2 has two reduced orbit types: {0} and the nilcone.
        The reduced geometric comparison model is concentrated for both,
        but the full simple-quotient problem still depends on nilradical
        data.
        """
        assert koszulness_prediction('zero', 2) == 'reduced-point; nilradical-dependent'
        # Regular orbit: nilradical-dependent
        assert koszulness_prediction('regular', 2) == 'nilradical-dependent'
        # Reduced geometric comparison model concentrated
        hp = sl2_nilcone_poisson_cohomology()
        assert all(hp.get(n, 0) == 0 for n in range(1, 10))

    def test_sl3_complete_picture(self):
        """Complete verification for sl_3.

        sl_3 has three reduced orbit types: {0}, O_min, and N.
        Zero is still nilradical-dependent, the minimal route is conditional,
        and the regular orbit is nilradical-dependent.
        """
        assert koszulness_prediction('zero', 3) == 'reduced-point; nilradical-dependent'
        assert koszulness_prediction('minimal', 3) == 'conditional on reducedness'
        assert koszulness_prediction('regular', 3) == 'nilradical-dependent'

    def test_sl4_hierarchy(self):
        """For sl_4, the orbit hierarchy.

        sl_4 has 5 reduced orbit types. Zero remains nilradical-dependent,
        the minimal route is conditional, and regular/subregular are
        nilradical-dependent.
        """
        assert koszulness_prediction('zero', 4) == 'reduced-point; nilradical-dependent'
        assert koszulness_prediction('minimal', 4) == 'conditional on reducedness'
        assert koszulness_prediction('regular', 4) == 'nilradical-dependent'
        assert koszulness_prediction('subregular', 4) == 'nilradical-dependent'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
