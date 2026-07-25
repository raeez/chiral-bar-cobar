"""Regression tests for the finite annulus-trace table helper.

These tests preserve the old schematic table row. They do not prove
Theorem H, Calabi-Yau duality, topological Hochschild homology, or a
completed cyclic-bar computation.
"""

import pytest
from fractions import Fraction

from compute.lib.annulus_trace_verification import (
    hochschild_homology_dimension,
    hochschild_cohomology_dimension,
    calabi_yau_pairing_check,
    annulus_partition_function,
    cyclic_bar_dimension,
    hochschild_euler_characteristic,
    hochschild_total_dimension,
    MODEL_SCOPE,
    FAMILIES,
)


# ======================================================================
#  1. Hochschild homology dimensions
# ======================================================================

class TestHochschildHomology:

    def test_model_scope_is_table_metadata(self):
        assert MODEL_SCOPE["status"] == "finite schematic table"
        assert "Theorem H" in MODEL_SCOPE["not_a_proof_of"]
        assert "THH" in MODEL_SCOPE["not_a_proof_of"]
        assert MODEL_SCOPE["ordinary_hochschild_differential"] == "b"

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh0_is_one(self, family):
        """The stored HH_0 table entry is 1."""
        assert hochschild_homology_dimension(family, 0) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh1_is_one(self, family):
        """The stored HH_1 table entry is 1."""
        assert hochschild_homology_dimension(family, 1) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh2_is_one(self, family):
        """The stored HH_2 table entry is 1."""
        assert hochschild_homology_dimension(family, 2) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh_vanishes_negative(self, family):
        """HH_n = 0 for n < 0."""
        assert hochschild_homology_dimension(family, -1) == 0
        assert hochschild_homology_dimension(family, -5) == 0

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh_vanishes_above_2(self, family):
        """The stored table row has no entries above degree 2."""
        for n in range(3, 10):
            assert hochschild_homology_dimension(family, n) == 0

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError):
            hochschild_homology_dimension("Unknown", 0)


# ======================================================================
#  2. Hochschild cohomology dimensions (Theorem H)
# ======================================================================

class TestHochschildCohomology:

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh0_cohom(self, family):
        """The stored HH^0 table entry is 1."""
        assert hochschild_cohomology_dimension(family, 0) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh1_cohom(self, family):
        """The stored HH^1 table entry is 1."""
        assert hochschild_cohomology_dimension(family, 1) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh2_cohom(self, family):
        """The stored HH^2 table entry is 1."""
        assert hochschild_cohomology_dimension(family, 2) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_cohom_vanishes_outside(self, family):
        """The stored cohomology row has support in {0,1,2}."""
        for n in [-1, 3, 4, 5, 10]:
            assert hochschild_cohomology_dimension(family, n) == 0


# ======================================================================
#  3. Calabi-Yau duality
# ======================================================================

class TestCalabiYauDuality:

    @pytest.mark.parametrize("family", FAMILIES)
    def test_cy_duality(self, family):
        """The stored rows are compatible with the chosen CY shift."""
        result = calabi_yau_pairing_check(family)
        assert result["calabi_yau_holds"]

    @pytest.mark.parametrize("family", FAMILIES)
    def test_cy_explicit(self, family):
        """Explicit table check: HH_0 = HH^2, HH_1 = HH^1, HH_2 = HH^0."""
        for n in range(3):
            assert (hochschild_homology_dimension(family, n) ==
                    hochschild_cohomology_dimension(family, 2 - n))


# ======================================================================
#  4. Cyclic bar complex
# ======================================================================

class TestCyclicBarComplex:

    @pytest.mark.parametrize("family", FAMILIES)
    def test_cyclic_bar_dim_0(self, family):
        """The finite cyclic-word orbit count is nonempty in degree 0."""
        d = cyclic_bar_dimension(family, 0, weight_bound=4)
        assert d >= 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_cyclic_bar_nonnegative(self, family):
        """All finite cyclic-word orbit counts are nonnegative."""
        for n in range(5):
            assert cyclic_bar_dimension(family, n, weight_bound=4) >= 0

    def test_heisenberg_cyclic_bar(self):
        """The Heisenberg finite cyclic-word count is nonempty."""
        d0 = cyclic_bar_dimension("Heisenberg", 0, weight_bound=4)
        assert d0 >= 1


# ======================================================================
#  5. Annulus partition function
# ======================================================================

class TestAnnulusPartition:

    @pytest.mark.parametrize("family", FAMILIES)
    def test_annulus_partition_is_one(self, family):
        """The normalized scalar identity-trace table entry is 1."""
        assert annulus_partition_function(family) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_annulus_is_integer(self, family):
        z = annulus_partition_function(family)
        assert z == 1
        assert z > 0


# ======================================================================
#  6. Cross-family consistency
# ======================================================================

class TestCrossFamilyConsistency:

    def test_all_families_same_hh_dims(self):
        """The finite homology table row is the same for each family."""
        for n in range(3):
            dims = [hochschild_homology_dimension(f, n) for f in FAMILIES]
            assert len(set(dims)) == 1, f"HH_{n} differs across families"

    def test_all_families_same_cohom_dims(self):
        """The finite cohomology table row is the same for each family."""
        for n in range(3):
            dims = [hochschild_cohomology_dimension(f, n) for f in FAMILIES]
            assert len(set(dims)) == 1, f"HH^{n} differs across families"


# ======================================================================
#  7. Polynomial growth
# ======================================================================

class TestPolynomialGrowth:

    @pytest.mark.parametrize("family", FAMILIES)
    def test_total_dimension_is_3(self, family):
        """Total dimension of the stored table row is 3."""
        assert hochschild_total_dimension(family) == 3

    @pytest.mark.parametrize("family", FAMILIES)
    def test_euler_characteristic(self, family):
        """Euler characteristic of the stored table row is 1."""
        assert hochschild_euler_characteristic(family) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_vanishing_outside_range(self, family):
        """The stored cohomology row has no entries above degree 2."""
        for n in [3, 4, 5, 10]:
            assert hochschild_cohomology_dimension(family, n) == 0
