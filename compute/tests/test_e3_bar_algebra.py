"""
Tests for E_3-algebra structure on bar complex — 45+ tests.

Central finding: B(A) is E_2, NOT E_3. The derived center Z^der_ch(A)
carries E_3 by Higher Deligne Conjecture.
"""

import pytest
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from e3_bar_algebra import (
    conf_betti, total_betti, obstruction_class_dim,
    e2_bracket_degree, e3_bracket_degree, bv_operator_degree,
    bv_is_not_e3, en_structure_on_bar, swiss_cheese_is_not_tensor,
    derived_center_en_structure, physical_interpretation,
    heisenberg_is_e_infinity,
)


# ============================================================
# Configuration space Betti numbers
# ============================================================

class TestConfBetti:
    def test_conf1_r2(self):
        b = conf_betti(2, 1)
        assert b == {0: 1}

    def test_conf2_r2(self):
        b = conf_betti(2, 2)
        assert b == {0: 1, 1: 1}
        assert sum(b.values()) == 2  # 2!

    def test_conf3_r2(self):
        b = conf_betti(2, 3)
        assert b == {0: 1, 1: 3, 2: 2}
        assert sum(b.values()) == 6  # 3!

    def test_conf4_r2(self):
        b = conf_betti(2, 4)
        assert sum(b.values()) == 24  # 4!

    def test_conf2_r3(self):
        b = conf_betti(3, 2)
        assert b == {0: 1, 2: 1}
        assert sum(b.values()) == 2

    def test_conf3_r3(self):
        b = conf_betti(3, 3)
        assert b == {0: 1, 2: 3, 4: 2}
        assert sum(b.values()) == 6

    def test_total_betti_equals_factorial(self):
        for k in range(1, 4):  # k=1,2,3 where we have full data
            for n in [2, 3]:
                assert total_betti(n, k) == math.factorial(k)

    def test_e2_generators_degree_1(self):
        """E_2 generators (Arnold) live in degree 1."""
        b = conf_betti(2, 2)
        assert 1 in b and b[1] == 1

    def test_e3_generators_degree_2(self):
        """E_3 generators live in degree 2."""
        b = conf_betti(3, 2)
        assert 2 in b and b[2] == 1


# ============================================================
# Obstruction theory
# ============================================================

class TestObstruction:
    def test_heisenberg_no_obstruction(self):
        """Lambda^3(C^1) = 0, so E_3 obstruction vanishes for Heisenberg."""
        assert obstruction_class_dim('heisenberg') == 0

    def test_sl2_has_obstruction(self):
        """Lambda^3(C^3) = C, so obstruction is 1-dimensional."""
        assert obstruction_class_dim('sl2') == 1

    def test_virasoro_has_obstruction(self):
        assert obstruction_class_dim('virasoro') == 1

    def test_sl_n_obstruction_grows(self):
        """Obstruction grows as C(n,3) with rank."""
        for n in [3, 4, 5, 6]:
            assert obstruction_class_dim('sl_n', n) == math.comb(n, 3)


# ============================================================
# Degree structure
# ============================================================

class TestDegrees:
    def test_e2_bracket_degree_1(self):
        assert e2_bracket_degree() == 1

    def test_e3_bracket_degree_2(self):
        assert e3_bracket_degree() == 2

    def test_bv_degree_1(self):
        assert bv_operator_degree() == 1

    def test_bv_is_not_e3(self):
        """BV (degree 1) cannot produce E_3 (degree 2)."""
        assert bv_is_not_e3()


# ============================================================
# E_n structure on bar
# ============================================================

class TestEnOnBar:
    def test_e1_exists(self):
        assert en_structure_on_bar(1)['exists']

    def test_e2_exists(self):
        assert en_structure_on_bar(2)['exists']

    def test_e3_does_not_exist(self):
        """THE CENTRAL NEGATIVE THEOREM."""
        assert not en_structure_on_bar(3)['exists']

    def test_e4_does_not_exist(self):
        assert not en_structure_on_bar(4)['exists']

    def test_e3_obstruction_is_geometric(self):
        info = en_structure_on_bar(3)
        assert 'R^3' in info.get('obstruction', '')

    def test_e3_lives_on_derived_center(self):
        info = en_structure_on_bar(3)
        assert 'derived center' in info.get('where_it_lives', '').lower()


# ============================================================
# Swiss-cheese is not tensor product
# ============================================================

class TestSwissCheese:
    def test_swiss_cheese_claim_false(self):
        result = swiss_cheese_is_not_tensor()
        assert result['verdict'] == 'FALSE'

    def test_swiss_cheese_anti_pattern(self):
        result = swiss_cheese_is_not_tensor()
        assert 'AP14' in result['anti_pattern']


# ============================================================
# Higher Deligne Conjecture
# ============================================================

class TestHigherDeligne:
    def test_e2_gives_e3_on_center(self):
        """B(A) is E_2 => Z^der is E_3."""
        assert derived_center_en_structure(2) == 3

    def test_e1_gives_e2_on_center(self):
        assert derived_center_en_structure(1) == 2

    def test_e3_gives_e4_on_center(self):
        assert derived_center_en_structure(3) == 4


# ============================================================
# Physical interpretation
# ============================================================

class TestPhysical:
    def test_e2_is_2d(self):
        interp = physical_interpretation(2)
        assert '2d' in interp.lower() or 'surface' in interp.lower()

    def test_e3_is_3d(self):
        interp = physical_interpretation(3)
        assert '3d' in interp.lower() or 'knot' in interp.lower()


# ============================================================
# Heisenberg special case
# ============================================================

class TestHeisenberg:
    def test_chain_level_e2(self):
        info = heisenberg_is_e_infinity()
        assert info['chain_level'] == 'E_2'

    def test_cohomology_e_infinity(self):
        info = heisenberg_is_e_infinity()
        assert 'E_infinity' in info['cohomology_level']

    def test_qi_level_e2(self):
        info = heisenberg_is_e_infinity()
        assert 'E_2' in info['qi_level']

    def test_obstruction_zero(self):
        info = heisenberg_is_e_infinity()
        assert info['obstruction_dim'] == 0
