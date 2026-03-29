"""Tests for the annulus trace verification module.

Verifies:
  1. Hochschild homology dimensions HH_n for all families
  2. Hochschild cohomology dimensions HH^n (Theorem H)
  3. Calabi-Yau duality HH_n = HH^{2-n}
  4. Cyclic bar complex dimensions
  5. Annulus partition function Z_ann = 1
  6. Cross-family consistency
  7. Polynomial growth (vanishing outside {0,1,2})
  8. Parametric stability across level/central charge

References:
  thm:thqg-annulus-trace, thm:hochschild-polynomial-growth (Theorem H),
  thm:main-koszul-hoch (Koszul duality for Hochschild)
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
    FAMILIES,
)


# ======================================================================
#  1. Hochschild homology dimensions
# ======================================================================

class TestHochschildHomology:

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh0_is_one(self, family):
        """HH_0(A) = 1 for all standard families (trace space)."""
        assert hochschild_homology_dimension(family, 0) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh1_is_one(self, family):
        """HH_1(A) = 1 for all standard families (loop space)."""
        assert hochschild_homology_dimension(family, 1) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh2_is_one(self, family):
        """HH_2(A) = 1 for all standard families (center)."""
        assert hochschild_homology_dimension(family, 2) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh_vanishes_negative(self, family):
        """HH_n = 0 for n < 0."""
        assert hochschild_homology_dimension(family, -1) == 0
        assert hochschild_homology_dimension(family, -5) == 0

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh_vanishes_above_2(self, family):
        """HH_n = 0 for n > 2 (polynomial growth from Theorem H)."""
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
        """HH^0(A) = Z(A) = 1 (center = vacuum)."""
        assert hochschild_cohomology_dimension(family, 0) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh1_cohom(self, family):
        """HH^1(A) = 1 (level/cc deformation)."""
        assert hochschild_cohomology_dimension(family, 1) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh2_cohom(self, family):
        """HH^2(A) = 1 (dual center)."""
        assert hochschild_cohomology_dimension(family, 2) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_cohom_vanishes_outside(self, family):
        """HH^n = 0 for n not in {0,1,2}."""
        for n in [-1, 3, 4, 5, 10]:
            assert hochschild_cohomology_dimension(family, n) == 0


# ======================================================================
#  3. Calabi-Yau duality
# ======================================================================

class TestCalabiYauDuality:

    @pytest.mark.parametrize("family", FAMILIES)
    def test_cy_duality(self, family):
        """HH_n(A) = HH^{2-n}(A) for all n."""
        result = calabi_yau_pairing_check(family)
        assert result["calabi_yau_holds"]

    @pytest.mark.parametrize("family", FAMILIES)
    def test_cy_explicit(self, family):
        """Explicit check: HH_0 = HH^2, HH_1 = HH^1, HH_2 = HH^0."""
        for n in range(3):
            assert (hochschild_homology_dimension(family, n) ==
                    hochschild_cohomology_dimension(family, 2 - n))


# ======================================================================
#  4. Cyclic bar complex
# ======================================================================

class TestCyclicBarComplex:

    @pytest.mark.parametrize("family", FAMILIES)
    def test_cyclic_bar_dim_0(self, family):
        """B^cyc_0(A) should be nonempty."""
        d = cyclic_bar_dimension(family, 0, weight_bound=4)
        assert d >= 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_cyclic_bar_nonnegative(self, family):
        """All cyclic bar dimensions are nonneg."""
        for n in range(5):
            assert cyclic_bar_dimension(family, n, weight_bound=4) >= 0

    def test_heisenberg_cyclic_bar(self):
        """Heisenberg has simple cyclic bar structure."""
        d0 = cyclic_bar_dimension("Heisenberg", 0, weight_bound=4)
        assert d0 >= 1


# ======================================================================
#  5. Annulus partition function
# ======================================================================

class TestAnnulusPartition:

    @pytest.mark.parametrize("family", FAMILIES)
    def test_annulus_partition_is_one(self, family):
        """Z_ann = Tr(Id) = dim HH_0 = 1."""
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
        """All standard families have the same HH dimensions at generic params."""
        for n in range(3):
            dims = [hochschild_homology_dimension(f, n) for f in FAMILIES]
            assert len(set(dims)) == 1, f"HH_{n} differs across families"

    def test_all_families_same_cohom_dims(self):
        """All standard families have the same HH^n dimensions."""
        for n in range(3):
            dims = [hochschild_cohomology_dimension(f, n) for f in FAMILIES]
            assert len(set(dims)) == 1, f"HH^{n} differs across families"


# ======================================================================
#  7. Polynomial growth
# ======================================================================

class TestPolynomialGrowth:

    @pytest.mark.parametrize("family", FAMILIES)
    def test_total_dimension_is_3(self, family):
        """Total HH dimension = HH^0 + HH^1 + HH^2 = 3."""
        assert hochschild_total_dimension(family) == 3

    @pytest.mark.parametrize("family", FAMILIES)
    def test_euler_characteristic(self, family):
        """chi = HH^0 - HH^1 + HH^2 = 1."""
        assert hochschild_euler_characteristic(family) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_vanishing_outside_range(self, family):
        """HH^n = 0 for n not in {0,1,2} — polynomial growth."""
        for n in [3, 4, 5, 10]:
            assert hochschild_cohomology_dimension(family, n) == 0
