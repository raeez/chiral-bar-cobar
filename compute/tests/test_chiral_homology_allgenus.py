"""Tests for compute/lib/chiral_homology_allgenus.py.

Key results:
  - Scalar genus tower: F_g(A) = kappa(A) * lambda_g^FP (Theorem D)
  - PBW concentration: bar cohomology is genus-independent at generic level
  - Complementarity: kappa(A) + kappa(A!) = root-datum invariant
  - Heisenberg bar cohomology: H_h = p(h-2) for h >= 2
  - Verlinde: integer conformal block dimensions at integrable levels
"""

import pytest
from sympy import Rational

from compute.lib.chiral_homology_allgenus import (
    BAR_COHOMOLOGY,
    bar_hilbert_series,
    fiberwise_chiral_homology_dim,
    verify_pbw_genus_independence,
    KAPPA_TABLE,
    verlinde_sl2,
    verlinde_integer_sl2,
    is_exceptional_level_sl2,
    verify_level_independence_integrable,
    complementarity_kappa_sum,
    heisenberg_bar_cohomology_predicted,
    chiral_homology_package,
    verify_allgenus_package,
    verify_verlinde_normalization,
)


class TestBarHilbertSeries:
    """Known bar cohomology dimensions at genus 0, generic level."""

    def test_heisenberg_degree1(self):
        dims = bar_hilbert_series("Heisenberg")
        assert dims[1] == 1

    def test_heisenberg_matches_betagamma(self):
        """Heisenberg and betagamma share the same bar Hilbert series."""
        h = bar_hilbert_series("Heisenberg")
        bg = bar_hilbert_series("betagamma")
        for n in h:
            assert h[n] == bg.get(n, 0)

    def test_sl2_degree1(self):
        dims = bar_hilbert_series("sl2")
        assert dims[1] == 3  # dim(sl_2) = 3

    def test_max_degree_filter(self):
        dims = bar_hilbert_series("Heisenberg", max_degree=3)
        assert all(n <= 3 for n in dims)

    def test_all_dims_positive(self):
        for family in BAR_COHOMOLOGY:
            dims = bar_hilbert_series(family)
            assert all(d > 0 for d in dims.values()), f"{family} has non-positive dim"


class TestPBWGenusIndependence:
    """PBW concentration: fiberwise chiral homology = genus-0 bar cohomology."""

    @pytest.mark.parametrize("family", ["Heisenberg", "Virasoro", "sl2"])
    def test_genus_independence(self, family):
        """KEY RESULT: bar cohomology dims are genus-independent."""
        results = verify_pbw_genus_independence(family, max_genus=3)
        assert all(results), f"{family}: PBW genus independence failed"

    def test_fiberwise_equals_genus0(self):
        """Fiberwise dim at any genus = genus-0 dim."""
        for g in range(4):
            assert fiberwise_chiral_homology_dim("Heisenberg", g, 1) == 1
            assert fiberwise_chiral_homology_dim("Heisenberg", g, 4) == 2


class TestHeisenbergPartitionFormula:
    """Heisenberg bar cohomology: H_h = p(h-2) for h >= 2."""

    def test_degree1(self):
        assert heisenberg_bar_cohomology_predicted(1) == 1

    def test_degree2(self):
        """H_2 = p(0) = 1."""
        assert heisenberg_bar_cohomology_predicted(2) == 1

    def test_degree4(self):
        """H_4 = p(2) = 2."""
        assert heisenberg_bar_cohomology_predicted(4) == 2

    def test_degree5(self):
        """H_5 = p(3) = 3."""
        assert heisenberg_bar_cohomology_predicted(5) == 3

    def test_matches_table(self):
        """Predicted values match the BAR_COHOMOLOGY table."""
        for h, d in BAR_COHOMOLOGY["Heisenberg"].items():
            assert heisenberg_bar_cohomology_predicted(h) == d


class TestComplementarity:
    """kappa(A) + kappa(A!) = root-datum invariant."""

    def test_km_antisymmetry(self):
        """For affine KM: kappa + kappa' = 0."""
        for fam in ["sl2", "sl3", "Heisenberg"]:
            assert complementarity_kappa_sum(fam) == 0

    def test_virasoro_sum_13(self):
        assert complementarity_kappa_sum("Virasoro") == Rational(13)

    def test_w3_sum(self):
        assert complementarity_kappa_sum("W3") == Rational(250, 3)

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError):
            complementarity_kappa_sum("unknown_family")


class TestVerlinde:
    """Verlinde formula at integrable levels for SU(2)."""

    def test_genus1_equals_k_plus_1(self):
        """At genus 1: Z_g = k + 1 (number of integrable reps)."""
        for k in [1, 2, 3, 5, 10]:
            assert verlinde_sl2(k, 1) == Rational(k + 1)

    def test_integer_dim_genus1(self):
        for k in range(1, 6):
            assert verlinde_integer_sl2(k, 1) == k + 1

    def test_integer_dim_genus0(self):
        """At genus 0 with no punctures: dim = 1 (unique vacuum block)."""
        for k in range(1, 6):
            assert verlinde_integer_sl2(k, 0) == 1

    def test_integer_dim_positive(self):
        """Integer Verlinde dims are always positive."""
        for k in [1, 2, 3]:
            for g in [1, 2, 3]:
                d = verlinde_integer_sl2(k, g)
                assert d > 0, f"k={k}, g={g}: dim = {d}"


class TestLevelIndependence:
    """Integrable levels are outside the exceptional set Sigma_n."""

    def test_critical_is_exceptional(self):
        """k = -h^vee = -2 (critical level) IS exceptional."""
        assert is_exceptional_level_sl2(-2)

    def test_integrable_not_exceptional(self):
        """Positive integer k is NOT exceptional."""
        for k in range(1, 10):
            assert not is_exceptional_level_sl2(k)

    def test_verify_integrable_independence(self):
        results = verify_level_independence_integrable("sl2", max_k=5)
        assert all(results.values())


class TestVerlindeNormalization:
    """Two Verlinde normalizations are consistent."""

    def test_genus1_match(self):
        result = verify_verlinde_normalization(2, 1)
        assert result["match"]
        assert result["dim_is_integer"]

    def test_genus2_match(self):
        result = verify_verlinde_normalization(2, 2)
        assert result["match"]


class TestChiralHomologyPackage:
    """Integration: full chiral homology package assembly."""

    @pytest.mark.parametrize("family", ["Heisenberg", "Virasoro", "sl2"])
    def test_package_assembles(self, family):
        pkg = chiral_homology_package(family)
        assert pkg["family"] == family
        assert pkg["kappa"] is not None
        assert pkg["pbw_genus_independent_at_generic_level"]

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError):
            chiral_homology_package("nonexistent")

    @pytest.mark.parametrize("family", ["Heisenberg", "Virasoro", "sl2"])
    def test_verify_package(self, family):
        results = verify_allgenus_package(family)
        for name, ok in results.items():
            assert ok, f"{family}: {name} failed"
