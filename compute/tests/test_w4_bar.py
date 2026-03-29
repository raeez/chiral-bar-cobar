"""Tests for compute/lib/w4_bar.py — W_4 bar complex OPE products and stage-4 extraction.

Verifies:
  - W_4 OPE n-th product structure (generator pairs, pole orders)
  - Virasoro sub-OPE: T x T has correct poles and coefficients
  - Primary conditions: T x W_s has pole-1 coefficient = s (weight)
  - Ward identity: C_{4,4;2;0,6} = 2 (algebraically determined)
  - Mixed orthogonality: C_{3,4;2;0,5} = 0 (algebraically determined)
  - Stage-4 extraction returns 6 channels
  - W_3 x W_3 pole structure matches Zamolodchikov

References:
  concordance.tex: prop:winfty-mc4-frontier-package
  w_algebras.tex: W_4 OPE structure
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.w4_bar import (
    w4_nth_products,
    extract_c_res_stage4_virasoro_targets,
    verify_virasoro_targets,
    extract_c_res_stage4,
)


# ═══════════════════════════════════════════════════════════════
# Import test
# ═══════════════════════════════════════════════════════════════

class TestImport:
    def test_module_loads(self):
        """Module imports without error."""
        import compute.lib.w4_bar
        assert hasattr(compute.lib.w4_bar, 'w4_nth_products')


# ═══════════════════════════════════════════════════════════════
# OPE structure tests
# ═══════════════════════════════════════════════════════════════

class TestW4NthProducts:
    """Verify the W_4 OPE n-th product dictionary structure."""

    def setup_method(self):
        self.products = w4_nth_products()
        self.c = Symbol('c')

    def test_generator_pairs_present(self):
        """All 5 generator pairs should be present."""
        expected_pairs = {
            ("T", "T"), ("T", "W3"), ("T", "W4"),
            ("W3", "W3"), ("W3", "W4"), ("W4", "W4"),
        }
        assert expected_pairs.issubset(set(self.products.keys()))

    def test_tt_virasoro_ope(self):
        """T x T: standard Virasoro OPE with poles at orders 3, 1, 0."""
        tt = self.products[("T", "T")]
        # Pole 4 (= mode 3): vacuum with coefficient c/2
        assert tt[3]["vac"] == self.c / 2
        # Pole 2 (= mode 1): T with coefficient 2
        assert tt[1]["T"] == Rational(2)
        # Pole 1 (= mode 0): dT with coefficient 1
        assert tt[0]["dT"] == Rational(1)

    def test_tw3_primary_condition(self):
        """T x W_3: primary of weight 3 means pole-2 coeff = 3."""
        tw3 = self.products[("T", "W3")]
        # Pole 2 (= mode 1): W3 with coefficient = weight = 3
        assert tw3[1]["W3"] == Rational(3)
        # Pole 1 (= mode 0): derivative
        assert tw3[0]["dW3"] == Rational(1)

    def test_tw4_primary_condition(self):
        """T x W_4: primary of weight 4 means pole-2 coeff = 4."""
        tw4 = self.products[("T", "W4")]
        assert tw4[1]["W4"] == Rational(4)
        assert tw4[0]["dW4"] == Rational(1)

    def test_w3w3_leading_pole(self):
        """W_3 x W_3: leading pole is order 6 (= mode 5), coeff = c/3."""
        w3w3 = self.products[("W3", "W3")]
        assert w3w3[5]["vac"] == self.c / 3

    def test_w3w3_subleading_structure(self):
        """W_3 x W_3: T appears at mode 3 with coefficient 2."""
        w3w3 = self.products[("W3", "W3")]
        assert w3w3[3]["T"] == Rational(2)

    def test_w3w3_contains_w4(self):
        """W_3 x W_3: W_4 appears at pole 2 (mode 1) with symbolic c334."""
        w3w3 = self.products[("W3", "W3")]
        assert "W4" in w3w3[1]
        # Coefficient should be the symbolic c334
        assert w3w3[1]["W4"] == Symbol('c334')

    def test_w4w4_leading_pole(self):
        """W_4 x W_4: leading pole is order 8 (= mode 7), coeff = c/4."""
        w4w4 = self.products[("W4", "W4")]
        assert w4w4[7]["vac"] == self.c / 4

    def test_w4w4_t_coefficient_ward_identity(self):
        """W_4 x W_4: T at mode 5 (= pole 6) has coefficient 2 from Ward identity.

        For a weight-h primary: C_T = (2h/c) * <W_h|W_h> = (2*4/c)*(c/4) = 2.
        This is normalization-independent and algebraically determined.
        """
        w4w4 = self.products[("W4", "W4")]
        assert w4w4[5]["T"] == Rational(2)

    def test_w3w3_composite_lambda(self):
        """W_3 x W_3: composite field Lambda coefficient = 16/(22+5c)."""
        w3w3 = self.products[("W3", "W3")]
        alpha_33 = Rational(16) / (22 + 5 * self.c)
        assert w3w3[1]["Lambda"] == alpha_33


# ═══════════════════════════════════════════════════════════════
# Virasoro target extraction tests
# ═══════════════════════════════════════════════════════════════

class TestVirasiroTargets:
    """The two Virasoro-target identities are the strongest falsifiability tests."""

    def test_c_4426_equals_2(self):
        """C_{4,4;2;0,6} = 2: Ward identity for W_4 self-coupling to T."""
        targets = extract_c_res_stage4_virasoro_targets()
        assert targets[(4, 4, 2, 6)] == 2

    def test_c_3425_equals_0(self):
        """C_{3,4;2;0,5} = 0: mixed-source orthogonality for W_3 x W_4 -> T.

        W_3 and W_4 are orthogonal primaries, so the T coefficient at
        the mixed pole vanishes.
        """
        targets = extract_c_res_stage4_virasoro_targets()
        assert targets[(3, 4, 2, 5)] == 0

    def test_verify_virasoro_targets_both_pass(self):
        """Both Virasoro target verifications should pass."""
        results = verify_virasoro_targets()
        assert results["C_{4,4;2;0,6} = 2"] is True
        assert results["C_{3,4;2;0,5} = 0"] is True


# ═══════════════════════════════════════════════════════════════
# Full stage-4 extraction
# ═══════════════════════════════════════════════════════════════

class TestStage4Extraction:
    """Test the full 6-channel stage-4 extraction."""

    def test_extraction_returns_six_channels(self):
        """The stage-4 extraction should return entries for 6 channels."""
        results = extract_c_res_stage4()
        # At least the 2 Virasoro targets + 4 higher-spin channels
        assert len(results) >= 6

    def test_virasoro_targets_in_full_extraction(self):
        """The two Virasoro targets should appear in the full extraction."""
        results = extract_c_res_stage4()
        assert (4, 4, 2, 6) in results
        assert (3, 4, 2, 5) in results
        assert results[(4, 4, 2, 6)] == 2
        assert results[(3, 4, 2, 5)] == 0

    def test_higher_spin_channels_are_symbolic(self):
        """Higher-spin channels should return symbolic expressions."""
        results = extract_c_res_stage4()
        # C_{3,3;4;0,2} = c334 (symbolic)
        c334_val = results.get((3, 3, 4, 2))
        assert c334_val is not None
        assert c334_val == Symbol('c334')

    def test_w4w4_self_coupling_channel(self):
        """C_{4,4;4;0,4} should be the symbolic c444."""
        results = extract_c_res_stage4()
        c444_val = results.get((4, 4, 4, 4))
        assert c444_val is not None
        assert c444_val == Symbol('c444')


# ═══════════════════════════════════════════════════════════════
# Structural consistency checks
# ═══════════════════════════════════════════════════════════════

class TestStructuralConsistency:
    """Cross-consistency checks on the OPE structure."""

    def test_virasoro_two_point_normalization(self):
        """Leading pole of W_s x W_s is c/s (two-point function normalization).

        T: c/2, W_3: c/3, W_4: c/4.
        """
        products = w4_nth_products()
        c = Symbol('c')
        assert products[("T", "T")][3]["vac"] == c / 2
        assert products[("W3", "W3")][5]["vac"] == c / 3
        assert products[("W4", "W4")][7]["vac"] == c / 4

    def test_primary_weight_consistency(self):
        """T x W_s: pole-2 coefficient should equal the conformal weight s."""
        products = w4_nth_products()
        assert products[("T", "W3")][1]["W3"] == Rational(3)
        assert products[("T", "W4")][1]["W4"] == Rational(4)

    def test_leading_pole_order_matches_sum_of_weights(self):
        """Leading pole order for W_s x W_t is s + t.

        T x T: 2+2 = 4, so mode index 3
        W_3 x W_3: 3+3 = 6, so mode index 5
        W_4 x W_4: 4+4 = 8, so mode index 7
        """
        products = w4_nth_products()
        # Verify leading pole modes
        tt_max = max(products[("T", "T")].keys())
        w3w3_max = max(products[("W3", "W3")].keys())
        w4w4_max = max(products[("W4", "W4")].keys())
        assert tt_max == 3      # pole order 4
        assert w3w3_max == 5    # pole order 6
        assert w4w4_max == 7    # pole order 8

    def test_dt_coefficient_one_from_translation_invariance(self):
        """The dT coefficient in T x T at mode 0 should be 1 (translation)."""
        products = w4_nth_products()
        assert products[("T", "T")][0]["dT"] == Rational(1)
