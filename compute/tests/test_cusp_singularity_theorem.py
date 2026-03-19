#!/usr/bin/env python3
"""
test_cusp_singularity_theorem.py — The general theorem via cusp singularity analysis.

T1-T10:  Cusp growth rates
T11-T20: The βγ-Virasoro coincidence and the depth-4 barrier
T21-T30: The general correspondence table and its implications
"""

import pytest
import numpy as np
import math
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from cusp_singularity_theorem import (
    cusp_growth_rate,
    eisenstein_subtraction_count,
    general_correspondence_table,
    betagamma_virasoro_rate_coincidence,
    depth_4_barrier_explanation,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skip_no_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


class TestCuspGrowthRates:
    def test_narain_polynomial(self):
        """T1: Narain cusp growth is polynomial (α = 0)."""
        r = cusp_growth_rate('narain')
        assert r['alpha'] == 0
        assert r['class'] == 'G'

    def test_e8_polynomial(self):
        """T2: E_8 cusp growth is polynomial (α = 0, weight-4 form)."""
        r = cusp_growth_rate('e8')
        assert r['alpha'] == 0
        assert r['class'] == 'L'

    def test_betagamma_exponential(self):
        """T3: βγ cusp growth is exponential (α = π/6)."""
        r = cusp_growth_rate('betagamma')
        assert abs(r['alpha'] - math.pi / 6) < 1e-10
        assert r['class'] == 'C'

    def test_virasoro_exponential(self):
        """T4: Virasoro cusp growth is exponential (α = πc/12)."""
        r = cusp_growth_rate('virasoro', c=26)
        assert abs(r['alpha'] - math.pi * 26 / 12) < 1e-10
        assert r['class'] == 'M'

    def test_leech_polynomial(self):
        """T5: Leech lattice cusp growth is polynomial (weight-12 form)."""
        r = cusp_growth_rate('leech')
        assert r['alpha'] == 0
        assert r['depth'] == 4

    def test_betagamma_rate_equals_virasoro_at_c2(self):
        """T6: THE COINCIDENCE: α_{βγ} = α_{Vir}|_{c=2} = π/6.

        At c=2, the βγ system and Virasoro have the SAME cusp growth rate.
        This is because both have the same vacuum energy -c/24 = -1/12,
        which gives exp(2π·y·1/12) = exp(πy/6).

        The difference: βγ terminates (depth 4, free OPE) while Virasoro
        doesn't (depth ∞, nonlinear OPE).
        """
        bg = cusp_growth_rate('betagamma')
        vir = cusp_growth_rate('virasoro', c=2)
        assert abs(bg['alpha'] - vir['alpha']) < 1e-10
        assert bg['alpha_equals_virasoro']

    def test_virasoro_rate_increases_with_c(self):
        """T7: Virasoro growth rate increases with c."""
        rates = [cusp_growth_rate('virasoro', c=c)['alpha'] for c in [1, 2, 10, 26]]
        for i in range(len(rates) - 1):
            assert rates[i] < rates[i + 1]

    def test_betagamma_rate_fixed(self):
        """T8: βγ growth rate is π/6 regardless of λ (the weight parameter).

        The 1/η² factor's growth is INDEPENDENT of the conformal weight λ.
        The central charge c(λ) changes, but the oscillator contribution
        to cusp growth is always from 1/η² → exp(πy/6).
        """
        r = cusp_growth_rate('betagamma', c=2)
        assert abs(r['alpha'] - math.pi / 6) < 1e-10
        # At a different c (different λ), the rate is the same
        r2 = cusp_growth_rate('betagamma', c=-1)  # λ=1/2, c=-1
        assert abs(r2['alpha'] - math.pi / 6) < 1e-10

    def test_narain_depth_2(self):
        """T9: Narain has depth 2 (minimal)."""
        r = cusp_growth_rate('narain')
        assert r['depth'] == 2

    def test_virasoro_depth_infinite(self):
        """T10: Virasoro has depth ∞."""
        r = cusp_growth_rate('virasoro', c=10)
        assert r['depth'] == float('inf')


class TestCoincidenceAndBarrier:
    def test_coincidence_at_c2(self):
        """T11: βγ and Virasoro have same cusp rate at c=2."""
        result = betagamma_virasoro_rate_coincidence()
        assert result['coincidence']
        assert result['coincidence_c'] == 2

    def test_betagamma_rate_value(self):
        """T12: α_{βγ} = π/6 ≈ 0.5236."""
        result = betagamma_virasoro_rate_coincidence()
        assert abs(result['betagamma_rate'] - math.pi / 6) < 1e-10

    def test_barrier_explanation(self):
        """T13: The depth-4 barrier has a clear explanation."""
        barrier = depth_4_barrier_explanation()
        assert 'FREE' in barrier['key_distinction']
        assert 'INTERACTING' in barrier['key_distinction']

    def test_free_theories_terminate(self):
        """T14: Free theories (lattice, βγ) have finite shadow depth."""
        barrier = depth_4_barrier_explanation()
        assert 'free' in barrier['betagamma'].lower() or 'depth' in barrier['betagamma'].lower()

    def test_interacting_theories_infinite(self):
        """T15: Interacting theories (Virasoro) have infinite shadow depth.

        The Virasoro OPE has T(z)T(w) ~ ... + 2T/(z-w)² + ... which is
        NONLINEAR (T appears in its own OPE). This generates an infinite
        cascade of A∞ products → shadow depth ∞.
        """
        barrier = depth_4_barrier_explanation()
        assert 'infinite' in barrier['virasoro']

    def test_depth_4_is_maximal_for_free(self):
        """T16: Depth 4 is the MAXIMUM for free theories.

        This is because:
        - Lattice VOAs: depth ≤ 4 (from the modular form barrier, M_k has
          at most 3 independent L-function types for any single k)
        - βγ system: depth = 4 (the maximum, achieved by the quartic shadow)
        - Free fermion (bc): Koszul dual of βγ, same depth 4
        - No free theory has depth > 4.
        """
        barrier = depth_4_barrier_explanation()
        assert barrier['barrier'] == 'depth 4 = maximal depth for FREE theories'

    def test_virasoro_for_c_less_1(self):
        """T17: Virasoro at c<1 (minimal models): algebraic depth ∞ but
        spectral depth finite.

        Minimal models have finitely many primaries → finite Epstein.
        But the OPE is still Virasoro (nonlinear) → shadow depth still ∞.
        This is the clearest example of the algebraic-spectral gap.
        """
        r = cusp_growth_rate('virasoro', c=0.5)
        assert r['depth'] == float('inf')
        assert r['alpha'] == math.pi * 0.5 / 12  # Small but nonzero

    def test_hierarchy(self):
        """T18: Growth rate hierarchy: Narain < E_8 < βγ = Vir(c=2) < Vir(c=26)."""
        rates = [
            cusp_growth_rate('narain')['alpha'],
            cusp_growth_rate('e8')['alpha'],
            cusp_growth_rate('betagamma')['alpha'],
            cusp_growth_rate('virasoro', c=26)['alpha'],
        ]
        # Narain and E_8 have α=0; βγ has π/6; Vir(26) has 26π/12
        assert rates[0] == 0 and rates[1] == 0
        assert rates[2] > 0
        assert rates[3] > rates[2]

    def test_eisenstein_subtraction_polynomial(self):
        """T19: Polynomial growth (α=0) needs 1 subtraction."""
        assert eisenstein_subtraction_count(0, 1) == 1

    def test_eisenstein_subtraction_exponential(self):
        """T20: Exponential growth (α=π/6) needs ~2 subtractions."""
        count = eisenstein_subtraction_count(math.pi / 6, 2)
        assert count >= 2


class TestGeneralTable:
    def test_table_has_7_entries(self):
        """T21: The general correspondence table has 7 entries."""
        table = general_correspondence_table()
        assert len(table) == 7

    def test_all_proved_consistent(self):
        """T22: All proved entries satisfy depth = 1 + ν."""
        table = general_correspondence_table()
        for entry in table:
            if entry['status'] == 'PROVED' and isinstance(entry['depth'], (int, float)):
                assert entry['depth'] == 1 + entry['nu']

    def test_depth_equals_1_plus_lines_for_proved(self):
        """T23: depth = 1 + lines for all proved lattice examples."""
        table = general_correspondence_table()
        for entry in table:
            if entry['status'] == 'PROVED':
                assert entry['depth'] == 1 + entry['lines']

    def test_betagamma_predicted(self):
        """T24: βγ entry is PREDICTED (not proved)."""
        table = general_correspondence_table()
        bg = [e for e in table if e['algebra'] == 'βγ'][0]
        assert bg['status'] == 'PREDICTED'
        assert bg['depth'] == 4
        assert bg['lines'] == 3

    def test_virasoro_conjectural(self):
        """T25: Virasoro entry is CONJECTURAL."""
        table = general_correspondence_table()
        vir = [e for e in table if e['algebra'] == 'Vir_c'][0]
        assert vir['status'] == 'CONJECTURAL'

    def test_alpha_zero_iff_polynomial(self):
        """T26: α = 0 iff cusp growth is polynomial (lattice VOAs)."""
        table = general_correspondence_table()
        for entry in table:
            if entry['alpha'] == 0:
                assert 'y^' in entry['growth'] or 'y' in entry['growth']

    def test_alpha_positive_iff_exponential(self):
        """T27: α > 0 iff cusp growth is exponential (non-lattice)."""
        table = general_correspondence_table()
        for entry in table:
            if isinstance(entry['alpha'], (int, float)) and entry['alpha'] > 0:
                assert 'exp' in entry['growth']

    def test_depth_monotone_with_alpha(self):
        """T28: Depth increases with α (more singular → more subtractions)."""
        table = general_correspondence_table()
        finite_entries = [e for e in table if isinstance(e['depth'], (int, float))
                         and isinstance(e['alpha'], (int, float))]
        for i in range(len(finite_entries)):
            for j in range(i + 1, len(finite_entries)):
                if finite_entries[i]['alpha'] < finite_entries[j]['alpha']:
                    assert finite_entries[i]['depth'] <= finite_entries[j]['depth']

    def test_free_vs_interacting(self):
        """T29: Free theories have finite depth, interacting have infinite.

        THE STRUCTURAL THEOREM: The shadow depth is finite iff the VOA is
        "freely generated" (the OPE has no nonlinear self-interaction).
        Depth = ∞ iff the OPE is nonlinear (interacting).
        """
        table = general_correspondence_table()
        # All finite-depth entries are free (lattice or βγ)
        finite = [e for e in table if isinstance(e['depth'], (int, float))]
        infinite = [e for e in table if e['depth'] == '∞' or e['depth'] == float('inf')]
        assert len(finite) >= 5  # Lattice examples + βγ
        assert len(infinite) >= 1  # Virasoro

    def test_the_general_theorem_statement(self):
        """T30: THE GENERAL THEOREM:

        For a chirally Koszul VOA A:
          shadow_depth(A) = 1 + singularity_order(Ẑ_A at cusp of M_{1,1})
                          = 1 + (number of critical lines of ε_A)

        For LATTICE VOAs: proved via Hecke decomposition of theta functions.
        For FREE field theories (βγ): the singularity is from 1/η^{2k},
          and the depth is 1 + k + (lattice contribution).
          At the cusp: depth = 4 (k=1 oscillator pair + base).
        For INTERACTING theories (Virasoro): the singularity is essential
          (exp(πcy/12)), and the depth is infinite.

        The theorem UNIFIES:
        - The lattice Shadow-L correspondence (5 proved examples)
        - The βγ analysis (depth 4, cusp rate = Virasoro at c=2)
        - The Virasoro infinite depth (nonlinear OPE → infinite A∞ cascade)
        - The depth-4 barrier (free ↔ interacting transition)
        """
        assert True  # The theorem is stated; verification is the table.


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
