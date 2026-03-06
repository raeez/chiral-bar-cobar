"""Tests for CONJECTURAL values — separated from proved values.

These tests verify regression on conjectured quantities. They should NOT
break CI if a conjectural value is updated. Mark with @pytest.mark.conjectural.

Every test here documents the provenance status of its value.
"""

import pytest


pytestmark = pytest.mark.conjectural


class TestW3Conjectural:
    """W₃ bar cohomology beyond degree 3."""

    def test_w3_h4(self):
        """H⁴(B̄(W₃)) = 52.
        Provenance: UNKNOWN — no documented derivation.
        First appears in Master Table (examples_summary.tex).
        See COMPUTE_NEXT_STEPS.md item M11."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        assert KNOWN_BAR_DIMS["W3"][4] == 52

    def test_w3_h5_gf_prediction(self):
        """H⁵(B̄(W₃)) = 171 from recurrence a(n) = 3a(n-1) + a(n-2) - 1.
        Provenance: interpolation from 4 data points (incl. unverified H⁴=52).
        NOT an independent computation."""
        a = [0, 2, 5, 16, 52]
        a5 = 3 * a[4] + a[3] - 1
        assert a5 == 171

    def test_w3_recurrence_consistency(self):
        """The depth-2+constant recurrence reproduces known values."""
        a = {0: 0, 1: 2, 2: 5, 3: 16, 4: 52}
        for n in range(2, 5):
            predicted = 3 * a[n - 1] + a[n - 2] - 1
            assert predicted == a[n], f"Recurrence fails at n={n}"


class TestSl3Conjectural:
    """sl₃ bar cohomology beyond degree 3."""

    def test_sl3_h4(self):
        """H⁴(B̄(ŝl₃)) = 1352 from recurrence a(n)=11a(n-1)-23a(n-2)-8a(n-3).
        Provenance: rational GF fit to 3 data points.
        NOT an independent computation."""
        from compute.lib.bar_complex import bar_dim_sl3_conjectured
        assert bar_dim_sl3_conjectured(4) == 1352

    def test_sl3_h5(self):
        """H⁵(B̄(ŝl₃)) = 9892 from same recurrence."""
        from compute.lib.bar_complex import bar_dim_sl3_conjectured
        assert bar_dim_sl3_conjectured(5) == 9892

    def test_sl3_recurrence_consistency(self):
        """Recurrence reproduces known proved values."""
        from compute.lib.bar_complex import bar_dim_sl3_conjectured, KNOWN_BAR_DIMS
        for n in [1, 2, 3]:
            assert bar_dim_sl3_conjectured(n) == KNOWN_BAR_DIMS["sl3"][n]


class TestYangianConjectural:
    """Yangian bar cohomology (3^n + 1 conjecture)."""

    def test_yangian_formula(self):
        """H^n(B̄(Y(sl₂))) = 3^n + 1 (conjectured)."""
        from compute.lib.yangian_bar import yangian_bar_cohomology_conjectured
        expected = {1: 4, 2: 10, 3: 28, 4: 82, 5: 244}
        for n, val in expected.items():
            assert yangian_bar_cohomology_conjectured(n) == val

    def test_yangian_seed_values(self):
        """Seed values match KNOWN_BAR_DIMS."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        from compute.lib.yangian_bar import yangian_bar_cohomology_conjectured
        for n in [1, 2, 3]:
            assert yangian_bar_cohomology_conjectured(n) == KNOWN_BAR_DIMS["Yangian_sl2"][n]
