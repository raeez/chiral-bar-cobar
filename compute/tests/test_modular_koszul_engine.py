"""Tests for the Modular Koszul Engine.

Verifies that the unified pipeline produces correct output for all
standard-landscape families, matching known values from individual modules.

Ground truth:
  tridegree_shadow_engine.py: kappa, cubic, quartic, depth class
  shadow_metric_census.py: Delta, Q_L, G/L/C/M classification
  shadow_connection.py: monodromy
  factorization_homology_engine.py: Koszulness, FH concentration
  resonance_rank_engine.py: rho(A), MC4 class

References:
  thm:mc2-bar-intrinsic, def:shadow-metric, thm:shadow-connection,
  thm:shadow-archetype-classification, thm:fh-concentration-koszulness,
  constr:platonic-package
"""

import pytest
from sympy import Symbol, Rational, simplify, S

from compute.lib.modular_koszul_engine import (
    ModularKoszulDatum,
    compute_datum,
    _canon,
)

c = Symbol('c')
k = Symbol('k')


# ================================================================
# Ground truth table
# ================================================================

FAMILIES = [
    ('heisenberg', {},
     {'depth_class': 'G', 'shadow_depth': 2,
      'is_koszul': True, 'monodromy': -1}),
    ('affine_sl2', {},
     {'depth_class': 'L', 'shadow_depth': 3,
      'is_koszul': True, 'monodromy': -1}),
    ('virasoro', {},
     {'depth_class': 'M', 'shadow_depth': None,
      'is_koszul': True, 'monodromy': -1}),
    ('w3', {},
     {'depth_class': 'M', 'shadow_depth': None,
      'is_koszul': True, 'monodromy': -1}),
    ('betagamma', {},
     {'depth_class': 'C', 'shadow_depth': 4,
      'is_koszul': True, 'monodromy': -1}),
    ('free_fermion', {},
     {'depth_class': 'G', 'shadow_depth': 2,
      'is_koszul': True, 'monodromy': -1}),
    ('lattice', {},
     {'depth_class': 'G', 'shadow_depth': 2,
      'is_koszul': True, 'monodromy': -1}),
    ('affine_sl3', {},
     {'depth_class': 'L', 'shadow_depth': 3,
      'is_koszul': True, 'monodromy': -1}),
]

FAMILY_IDS = [f[0] for f in FAMILIES]


# ================================================================
# Name canonicalization
# ================================================================

class TestCanonicalNames:

    def test_lowercase(self):
        assert _canon('virasoro') == 'virasoro'

    def test_alias(self):
        assert _canon('vir') == 'virasoro'
        assert _canon('heis') == 'heisenberg'
        assert _canon('bg') == 'betagamma'

    def test_capitalized(self):
        assert _canon('Heisenberg') == 'heisenberg'
        assert _canon('Virasoro') == 'virasoro'

    def test_unknown_raises(self):
        with pytest.raises(ValueError, match="Unknown family"):
            _canon('not_a_family')


# ================================================================
# Pipeline output correctness
# ================================================================

class TestComputeDatum:
    """Verify compute_datum() for each standard family."""

    @pytest.mark.parametrize("family,params,expected", FAMILIES, ids=FAMILY_IDS)
    def test_depth_class(self, family, params, expected):
        datum = compute_datum(family, **params)
        assert datum.depth_class == expected['depth_class']

    @pytest.mark.parametrize("family,params,expected", FAMILIES, ids=FAMILY_IDS)
    def test_shadow_depth(self, family, params, expected):
        datum = compute_datum(family, **params)
        assert datum.shadow_depth == expected['shadow_depth']

    @pytest.mark.parametrize("family,params,expected", FAMILIES, ids=FAMILY_IDS)
    def test_koszulness(self, family, params, expected):
        datum = compute_datum(family, **params)
        assert datum.is_koszul == expected['is_koszul']

    @pytest.mark.parametrize("family,params,expected", FAMILIES, ids=FAMILY_IDS)
    def test_monodromy(self, family, params, expected):
        """thm:shadow-connection: monodromy = -1 for all families."""
        datum = compute_datum(family, **params)
        assert datum.monodromy == expected['monodromy']


class TestKappaValues:
    """Verify kappa(A) against known formulas."""

    def test_heisenberg_kappa(self):
        datum = compute_datum('heisenberg')
        assert simplify(datum.kappa - k) == 0

    def test_virasoro_kappa(self):
        """thm:genus-universality: kappa(Vir_c) = c/2."""
        datum = compute_datum('virasoro')
        assert simplify(datum.kappa - c / 2) == 0

    def test_betagamma_kappa(self):
        datum = compute_datum('betagamma')
        assert datum.kappa == 1  # c(bg,lam=1)=2, kappa=c/2=1


class TestQuarticContact:
    """Verify quartic contact Q^ct."""

    def test_virasoro_quartic(self):
        """cor:virasoro-quartic-shadow-explicit: Q^ct = 10/[c(5c+22)]."""
        datum = compute_datum('virasoro')
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(datum.quartic_contact - expected) == 0

    def test_heisenberg_quartic_zero(self):
        """Heisenberg = class G: quartic vanishes."""
        datum = compute_datum('heisenberg')
        assert datum.quartic_contact == 0

    def test_betagamma_quartic(self):
        """Q^ct(bg) = 10/[c(5c+22)] at c=2: 10/(2*32) = 5/32."""
        datum = compute_datum('betagamma')
        assert datum.quartic_contact == Rational(5, 32)


# ================================================================
# Delta identity
# ================================================================

class TestDeltaConsistency:
    """Verify Delta = 8*kappa*S4 for all families."""

    @pytest.mark.parametrize("family,params,expected", FAMILIES, ids=FAMILY_IDS)
    def test_delta_identity(self, family, params, expected):
        datum = compute_datum(family, **params)
        assert simplify(datum.Delta - 8 * datum.kappa * datum.S4) == 0


# ================================================================
# Shadow tower properties
# ================================================================

class TestShadowTower:

    def test_heisenberg_terminates(self):
        """Heisenberg = class G: tower zero beyond arity 2."""
        datum = compute_datum('heisenberg')
        for r in [3, 4]:
            val = datum.shadow_tower.get(r, 0)
            assert val == 0, f"Heisenberg Sh_{r} should be 0, got {val}"

    def test_virasoro_nonzero_quintic(self):
        """Virasoro = class M: tower nonzero at arity 5."""
        datum = compute_datum('virasoro', max_shadow_arity=8)
        assert 5 in datum.shadow_tower
        assert datum.shadow_tower[5] != 0


# ================================================================
# Verify method
# ================================================================

class TestVerify:

    @pytest.mark.parametrize("family", ['heisenberg', 'virasoro', 'betagamma'])
    def test_verify_passes(self, family):
        datum = compute_datum(family)
        checks = datum.verify()
        for name, passed in checks.items():
            assert passed, f"Check {name!r} failed for {family}"


# ================================================================
# Summary and serialization
# ================================================================

class TestOutput:

    def test_summary_nonempty(self):
        datum = compute_datum('virasoro')
        s = datum.summary()
        assert len(s) > 100
        assert 'Virasoro' in s

    def test_to_dict_has_keys(self):
        datum = compute_datum('heisenberg')
        d = datum.to_dict()
        for key in ['family', 'kappa', 'depth_class', 'is_koszul', 'monodromy']:
            assert key in d

    def test_to_dict_serializable(self):
        datum = compute_datum('heisenberg', level=1)
        d = datum.to_dict()
        for val in d.values():
            str(val)  # should not raise


# ================================================================
# Koszul dual
# ================================================================

class TestKoszulDual:

    def test_virasoro_complementarity(self):
        """thm:quantum-complementarity-main: c + c' = 26 for Virasoro."""
        datum = compute_datum('virasoro')
        assert datum.complementarity_sum == 26
        assert simplify(datum.dual_central_charge - (26 - c)) == 0

    def test_virasoro_dual_name(self):
        datum = compute_datum('virasoro')
        assert datum.dual_family == 'Vir_{26-c}'

    def test_heisenberg_dual_kappa(self):
        """Heisenberg: kappa(A!) = -kappa(A)."""
        datum = compute_datum('heisenberg')
        assert simplify(datum.dual_kappa + datum.kappa) == 0


# ================================================================
# Holographic datum
# ================================================================

class TestHolographic:

    @pytest.mark.parametrize("family,params,expected", FAMILIES, ids=FAMILY_IDS)
    def test_collision_residue_present(self, family, params, expected):
        datum = compute_datum(family, **params)
        assert datum.collision_residue_type is not None

    def test_heisenberg_kappa_antisymmetric(self):
        datum = compute_datum('heisenberg')
        assert datum.kappa_anti_symmetric is True

    def test_connection_flat(self):
        datum = compute_datum('virasoro')
        assert datum.connection_is_flat is True


# ================================================================
# Name aliases
# ================================================================

class TestAliases:

    def test_vir_equals_virasoro(self):
        d1 = compute_datum('vir')
        d2 = compute_datum('virasoro')
        assert d1.family == d2.family
        assert d1.depth_class == d2.depth_class

    def test_bg_equals_betagamma(self):
        d1 = compute_datum('bg')
        d2 = compute_datum('betagamma')
        assert d1.family == d2.family
