"""Tests for low-genus modular-bar combinatorics."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.modular_bar import (
    fm3_planted_forest_types,
    genus_two_profile,
    genus_two_shells,
    mok_codimension,
    quartic_channels,
    shadow_archetype,
    standard_family_profiles,
)


class TestMokCodimension:
    def test_pair_collision_codim_one(self):
        assert mok_codimension([], [2]) == 1

    def test_nested_collision_codim_two(self):
        assert mok_codimension([], [3]) == 2

    def test_grid_and_tree_contributions_add(self):
        assert mok_codimension([1, 0, 2], [2, 3]) == 1 + 0 + 2 + 1 + 2


class TestFM3PlantedForests:
    def test_count(self):
        forests = fm3_planted_forest_types()
        assert len(forests) == 7

    def test_codimension_multiset(self):
        forests = fm3_planted_forest_types()
        codims = sorted(f.codimension for f in forests)
        assert codims == [1, 1, 1, 1, 2, 2, 2]

    def test_nested_names_present(self):
        names = {f.name for f in fm3_planted_forest_types()}
        assert {"12<123", "23<123", "13<123"}.issubset(names)


class TestQuarticChannels:
    def test_four_channels(self):
        assert quartic_channels() == ("contact", "12|34", "13|24", "14|23")


class TestShadowArchetypes:
    def test_classifier(self):
        assert shadow_archetype(False, False) == "Gaussian"
        assert shadow_archetype(True, False) == "Lie/tree"
        assert shadow_archetype(False, True) == "Contact/quartic"
        assert shadow_archetype(True, True) == "Mixed modular"

    def test_standard_profiles(self):
        profiles = standard_family_profiles()
        assert profiles["Heisenberg"] == "Gaussian"
        assert profiles["Affine"] == "Lie/tree"
        assert profiles["beta-gamma"] == "Contact/quartic"
        assert profiles["Virasoro"] == "Mixed modular"


class TestGenusTwoShells:
    def test_shell_names(self):
        assert genus_two_shells() == ("loop-loop", "sep-loop", "planted-forest")

    def test_family_profiles(self):
        assert genus_two_profile("Heisenberg") == ("loop-loop",)
        assert genus_two_profile("affine") == ("loop-loop", "sep-loop")
        assert genus_two_profile("Virasoro") == ("loop-loop", "sep-loop", "planted-forest")
