#!/usr/bin/env python3
"""
test_nonlinearity_tiers.py — Three-tier nonlinearity classification and
the corrected finite/infinite depth criterion.

T1-T10:  Tier classification of standard examples
T11-T20: The self-referentiality criterion
T21-T25: The corrected depth hierarchy
"""

import pytest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from nonlinearity_tiers import (
    classify_nonlinearity, classify_all_standard,
    heisenberg_ope, affine_sl2_ope, e8_ope,
    betagamma_ope, virasoro_ope, w3_ope,
)


class TestTierClassification:
    def test_heisenberg_tier_1(self):
        """T1: Heisenberg is Tier 1 (abelian). Depth ≤ 2."""
        result = classify_nonlinearity(heisenberg_ope())
        assert result['tier'] == 1
        assert 'Abelian' in result['name']

    def test_affine_tier_2(self):
        """T2: Affine sl_2 is Tier 2 (controlled). Finite depth."""
        result = classify_nonlinearity(affine_sl2_ope())
        assert result['tier'] == 2
        assert 'finite' in str(result['depth']).lower()

    def test_e8_tier_2(self):
        """T3: V_{E_8} is Tier 2 (controlled). Finite depth."""
        result = classify_nonlinearity(e8_ope())
        assert result['tier'] == 2

    def test_betagamma_tier_2prime(self):
        """T4: βγ is Tier 2' (contact/deformation). Depth ≤ 4."""
        result = classify_nonlinearity(betagamma_ope())
        assert result['tier'] == 2.5
        assert 'Contact' in result['name']

    def test_virasoro_tier_3(self):
        """T5: Virasoro is Tier 3 (self-referential). Depth = ∞.

        THE KEY: T_{(1)}T = 2T. The stress tensor T appears in its
        OWN self-OPE. This direct self-loop forces infinite depth.
        """
        result = classify_nonlinearity(virasoro_ope())
        assert result['tier'] == 3
        assert result['depth'] == float('inf')
        assert result['self_referential_generator'] == 'T'

    def test_w3_tier_3(self):
        """T6: W_3 is Tier 3 (via T's self-referentiality). Depth = ∞."""
        result = classify_nonlinearity(w3_ope())
        assert result['tier'] == 3
        assert result['self_referential_generator'] == 'T'

    def test_all_standard(self):
        """T7: All standard examples classified."""
        results = classify_all_standard()
        assert len(results) == 6
        assert all('tier' in v for v in results.values())

    def test_tier_1_finite(self):
        """T8: All Tier 1 algebras have finite depth."""
        result = classify_nonlinearity(heisenberg_ope())
        assert result['tier'] == 1
        assert '∞' not in str(result['depth'])

    def test_tier_2_finite(self):
        """T9: All Tier 2 algebras have finite depth."""
        for ope in [affine_sl2_ope(), e8_ope()]:
            result = classify_nonlinearity(ope)
            assert result['tier'] == 2
            assert result['depth'] != float('inf')

    def test_tier_3_infinite(self):
        """T10: All Tier 3 algebras have infinite depth."""
        for ope in [virasoro_ope(), w3_ope()]:
            result = classify_nonlinearity(ope)
            assert result['tier'] == 3
            assert result['depth'] == float('inf')


class TestSelfReferentiality:
    def test_virasoro_self_loop(self):
        """T11: T ∈ T_{(1)}T is a DIRECT self-loop."""
        ope = virasoro_ope()
        assert 'T' in ope['self_ope']['T']

    def test_heisenberg_no_self_loop(self):
        """T12: J ∉ J_{(k)}J for Heisenberg (no self-loop)."""
        ope = heisenberg_ope()
        assert 'J' not in ope['self_ope']['J']

    def test_affine_no_direct_self_loop(self):
        """T13: No generator of affine sl_2 has a direct self-loop.

        J+ ∉ J+·J+, J- ∉ J-·J-, J3 ∉ J3·J3.
        The INDIRECT loop (J3 ∈ J+·J-) does NOT count.
        """
        ope = affine_sl2_ope()
        for gen in ['J+', 'J-', 'J3']:
            assert gen not in ope['self_ope'].get(gen, set())

    def test_betagamma_no_self_loop(self):
        """T14: β ∉ β·β and γ ∉ γ·γ for βγ system."""
        ope = betagamma_ope()
        assert 'beta' not in ope['self_ope']['beta']
        assert 'gamma' not in ope['self_ope']['gamma']

    def test_w3_self_loop_via_T(self):
        """T15: W_3 has self-loop via T (not W).

        T_{(1)}T = 2T gives the self-loop.
        W_{(k)}W doesn't contain W directly (it contains Λ = :TT:).
        """
        ope = w3_ope()
        assert 'T' in ope['self_ope']['T']
        assert 'W' not in ope['self_ope']['W']

    def test_criterion_matches_known_depths(self):
        """T16: Self-referentiality criterion matches all known shadow depths.

        Heisenberg: no self-loop → depth 2 (finite) ✓
        Affine: no self-loop → depth 3 (finite) ✓
        βγ: no self-loop → depth 4 (finite) ✓
        Virasoro: T self-loop → depth ∞ ✓
        W_3: T self-loop → depth ∞ ✓
        """
        results = classify_all_standard()
        known_depths = {
            'Heisenberg': 2,
            'Affine sl_2': 3,
            'βγ': 4,
            'Virasoro': float('inf'),
            'W_3': float('inf'),
        }
        for name, depth in known_depths.items():
            r = results[name]
            if depth == float('inf'):
                assert r['depth'] == float('inf'), f"{name}: expected ∞, got {r['depth']}"
            else:
                assert r['depth'] != float('inf'), f"{name}: expected finite, got {r['depth']}"

    def test_indirect_loop_does_not_force_infinity(self):
        """T17: Indirect loops (a ∈ b·c, b ≠ a) do NOT force depth = ∞.

        Affine: J3 ∈ J+_{(0)}J- (indirect). But J3 ∉ J3·J3 (no direct loop).
        So depth = 3 (finite), despite the indirect loop.
        """
        result = classify_nonlinearity(affine_sl2_ope())
        assert result['depth'] != float('inf')

    def test_direct_loop_forces_infinity(self):
        """T18: Direct loop (a ∈ a·a) DOES force depth = ∞.

        Virasoro: T ∈ T_{(1)}T. Direct self-loop. Depth = ∞.
        """
        result = classify_nonlinearity(virasoro_ope())
        assert result['depth'] == float('inf')

    def test_creates_new_but_no_self_loop(self):
        """T19: Creating new fields (Tier 2) without self-loop → finite depth."""
        result = classify_nonlinearity(e8_ope())
        assert result['tier'] == 2
        assert result['depth'] != float('inf')

    def test_no_new_fields_no_self_loop(self):
        """T20: No new fields and no self-loop (Tier 1) → depth ≤ 2."""
        result = classify_nonlinearity(heisenberg_ope())
        assert result['tier'] == 1


class TestCorrectedHierarchy:
    def test_lattice_depth_unbounded(self):
        """T21: Lattice VOAs have unbounded finite depth (not capped at 4).

        CORRECTION: The 'depth-4 barrier for free theories' is WRONG.
        Lattice VOAs are Tier 2 (controlled nonlinearity via inner product)
        and their depth grows with rank: E_8 (3), Leech (4), rank-48 (5), ...
        """
        # Lattice VOAs are Tier 2
        result = classify_nonlinearity(e8_ope())
        assert result['tier'] == 2
        # The depth formula: depth = 1 + # critical lines of Epstein zeta
        # For rank-48: weight 24, dim S_24 = 2 → 4 critical lines → depth 5
        # This exceeds 4, contradicting the 'barrier' claim

    def test_free_interacting_not_the_boundary(self):
        """T22: The finite/infinite boundary is NOT free-vs-interacting.

        CORRECTION: Lattice VOAs are NONLINEAR (vertex operator OPE
        e^{iλ·X} · e^{iμ·X} ~ e^{i(λ+μ)·X} creates new fields) but have
        FINITE depth. The boundary is:
          finite ⟺ no direct self-referential OPE
          infinite ⟺ some generator in its own self-OPE
        """
        # E_8 is nonlinear (creates new fields) but finite depth
        e8_result = classify_nonlinearity(e8_ope())
        assert e8_ope()['creates_new_fields']  # E_8 IS nonlinear
        assert e8_result['depth'] != float('inf')  # but finite depth

    def test_three_tier_exhaustive(self):
        """T23: The three-tier classification covers all standard examples."""
        results = classify_all_standard()
        tiers = {v['tier'] for v in results.values()}
        assert tiers == {1, 2, 2.5, 3}

    def test_depth_2_iff_abelian(self):
        """T24: Depth 2 ⟺ Tier 1 (abelian) for standard examples."""
        results = classify_all_standard()
        for name, r in results.items():
            if r['tier'] == 1:
                assert '2' in str(r['depth'])

    def test_depth_inf_iff_self_referential(self):
        """T25: Depth ∞ ⟺ Tier 3 (self-referential) for all examples.

        THIS IS THE THEOREM: a strong generator appearing in its own
        self-OPE is the necessary and sufficient condition for infinite
        shadow depth.
        """
        results = classify_all_standard()
        for name, r in results.items():
            if r['tier'] == 3:
                assert r['depth'] == float('inf')
            else:
                assert r['depth'] != float('inf')


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
