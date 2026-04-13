r"""Tests for sl3_verlinde_engine.py.

This file follows the existing Verlinde-engine pattern:
  - genus identities first
  - known low-level values with explicit verification trails
  - cross-engine agreement against independent implementations
  - polynomial family checks

Verification tags:
  [DC] direct computation
  [LT] literature / standard theorem
  [CF] cross-engine comparison
  [LC] limiting case
  [SY] symmetry / pointed-category argument
"""

from __future__ import annotations

import pytest
from sympy import Poly, expand, symbols

from compute.lib.conformal_blocks_genus_engine import verlinde_dim_sl3
from compute.lib.factorization_homology_engine import verlinde_formula
from compute.lib.factorization_homology_explicit_engine import (
    fh_higher_genus_verlinde,
)
from compute.lib.sl3_verlinde_engine import (
    sl3_genus2_polynomial,
    sl3_integrable_weights,
    sl3_normalized_verlinde_sum,
    sl3_num_integrable_reps,
    sl3_quantum_dimensions,
    sl3_total_quantum_dimension_squared,
    sl3_verlinde_dimension,
    sl3_verlinde_polynomial,
    verify_genus0_unitarity,
    verify_genus1_count,
)
from compute.lib.verlinde_shadow_cohft_engine import verlinde_from_weyl_qdim


class TestIntegrableWeights:
    """Weight enumeration and level-1 quantum dimensions."""

    @pytest.mark.parametrize("level", range(0, 11))
    def test_weight_count(self, level: int):
        """|P_+^k| = (k+1)(k+2)/2 for sl_3.
        # VERIFIED: [DC] direct count of pairs (a,b) with a+b <= k
        # VERIFIED: [LT] genus-1 Verlinde count = number of integrable weights
        """
        expected = (level + 1) * (level + 2) // 2
        assert len(sl3_integrable_weights(level)) == expected
        assert sl3_num_integrable_reps(level) == expected

    def test_level1_quantum_dimensions_are_all_one(self):
        """At level 1 all three sl_3 quantum dimensions are 1.
        # VERIFIED: [DC] direct sine-ratio evaluation at k=1
        # VERIFIED: [SY] SU(3)_1 is a pointed Z/3 modular category
        """
        dimensions = sl3_quantum_dimensions(1)
        assert len(dimensions) == 3
        for dimension in dimensions:
            assert abs(dimension - 1) < 1e-30


class TestVerlindeDimensions:
    """Genus identities, low-level values, and integrality."""

    @pytest.mark.parametrize("level", range(0, 11))
    def test_genus0_is_one(self, level: int):
        """Z_0(k) = 1.
        # VERIFIED: [SY] unitarity of the first S-matrix row
        # VERIFIED: [LC] unique vacuum conformal block at genus 0
        """
        assert verify_genus0_unitarity(level)
        assert sl3_verlinde_dimension(0, level) == 1

    @pytest.mark.parametrize("level", range(0, 11))
    def test_genus1_is_rep_count(self, level: int):
        """Z_1(k) = (k+1)(k+2)/2.
        # VERIFIED: [DC] integrable-weight count
        # VERIFIED: [LT] genus-1 Verlinde = number of integrable simples
        """
        expected = (level + 1) * (level + 2) // 2
        assert verify_genus1_count(level)
        assert sl3_verlinde_dimension(1, level) == expected

    @pytest.mark.parametrize("genus", range(0, 7))
    def test_level1_is_three_to_g(self, genus: int):
        """At level 1, Z_g = 3^g.
        # VERIFIED: [DC] three channels each with d_lambda = 1
        # VERIFIED: [SY] pointed Z/3 modular category gives N^g with N=3
        """
        assert sl3_verlinde_dimension(genus, 1) == 3 ** genus

    @pytest.mark.parametrize(
        ("level", "expected"),
        [
            (1, 9),    # VERIFIED: [DC] 3^2 from the pointed level-1 formula
                       # VERIFIED: [SY] all three quantum dimensions are 1
                       # VERIFIED: [CF] conformal_blocks_genus_engine.py
            (2, 45),   # VERIFIED: [DC] genus-2 polynomial at k=2
                       # VERIFIED: [CF] conformal_blocks_genus_engine.py
            (3, 166),  # VERIFIED: [DC] genus-2 polynomial at k=3
                       # VERIFIED: [CF] conformal_blocks_genus_engine.py
        ],
    )
    def test_genus2_known_values(self, level: int, expected: int):
        """Known genus-2 sl_3 Verlinde dimensions."""
        assert sl3_verlinde_dimension(2, level) == expected

    @pytest.mark.parametrize("level", range(1, 11))
    @pytest.mark.parametrize("genus", [2, 3, 4])
    def test_positive_integer_for_g_ge_2(self, level: int, genus: int):
        """Z_g(k) is a positive integer for g >= 2.
        # VERIFIED: [DC] quantum-dimension computation with integer rounding
        # VERIFIED: [LT] Verlinde dimensions are ranks of conformal-block bundles
        """
        value = sl3_verlinde_dimension(genus, level)
        assert isinstance(value, int)
        assert value > 0

    def test_normalized_sum_needs_s00_prefactor(self):
        """The ratio sum is not the raw Verlinde dimension for g >= 2.
        # VERIFIED: [DC] Q_2(k) != Z_2(k) at k=2
        # VERIFIED: [SY] Z_g = S_{0,0}^{2-2g} * Q_g and S_{0,0}^{-2} = sum d^2
        """
        normalized = sl3_normalized_verlinde_sum(2, 2)
        total_qdim_sq = sl3_total_quantum_dimension_squared(2)
        corrected = int(round(total_qdim_sq * normalized))
        assert corrected == sl3_verlinde_dimension(2, 2)
        assert corrected != int(round(normalized))


class TestCrossChecks:
    """Agreement with independent existing engines and delegated callers."""

    @pytest.mark.parametrize("level", range(0, 7))
    @pytest.mark.parametrize("genus", range(0, 5))
    def test_matches_kac_peterson_engine(self, level: int, genus: int):
        """Dedicated sl_3 engine matches the Kac-Peterson S-matrix engine.
        # VERIFIED: [DC] new qdim+unitarity computation
        # VERIFIED: [CF] conformal_blocks_genus_engine.py
        """
        assert sl3_verlinde_dimension(genus, level) == verlinde_dim_sl3(level, genus)

    @pytest.mark.parametrize("level", range(0, 6))
    @pytest.mark.parametrize("genus", range(0, 5))
    def test_matches_weyl_qdim_engine(self, level: int, genus: int):
        """Dedicated sl_3 engine matches the independent Weyl-qdim engine.
        # VERIFIED: [DC] new qdim+unitarity computation
        # VERIFIED: [CF] verlinde_shadow_cohft_engine.py
        """
        expected = int(round(verlinde_from_weyl_qdim("A", 2, level, genus)))
        assert sl3_verlinde_dimension(genus, level) == expected

    @pytest.mark.parametrize("level", range(0, 6))
    @pytest.mark.parametrize("genus", range(0, 5))
    def test_factorization_homology_engine_delegates(self, level: int, genus: int):
        """factorization_homology_engine.py now uses the canonical sl_3 engine."""
        assert verlinde_formula("sl3", level, genus) == sl3_verlinde_dimension(
            genus, level
        )

    @pytest.mark.parametrize("level", range(1, 6))
    @pytest.mark.parametrize("genus", range(0, 5))
    def test_explicit_factorization_homology_engine_delegates(
        self, level: int, genus: int
    ):
        """factorization_homology_explicit_engine.py now uses the canonical sl_3 engine."""
        result = fh_higher_genus_verlinde(3, level, genus)
        assert result["dim"] == sl3_verlinde_dimension(genus, level)


class TestPolynomialFamily:
    """Polynomial family in the level k for fixed genus."""

    def test_genus2_closed_form(self):
        """Explicit genus-2 polynomial matches the expected factorization.
        # VERIFIED: [DC] interpolation from genus-2 values
        # VERIFIED: [CF] conformal_blocks_genus_engine.py at k=0,...,10
        """
        k = symbols("k")
        expected = Poly(
            expand(
                (k + 1)
                * (k + 2)
                * (k + 3) ** 2
                * (k + 4)
                * (k + 5)
                * (k ** 2 + 6 * k + 56)
                / 20160
            ),
            k,
            domain="QQ",
        )
        assert sl3_genus2_polynomial(k) == expected
        assert sl3_verlinde_polynomial(2, k) == expected

    @pytest.mark.parametrize("level", range(0, 11))
    def test_genus1_polynomial_values(self, level: int):
        """The genus-1 polynomial is (k+1)(k+2)/2.
        # VERIFIED: [DC] integrable-weight count
        # VERIFIED: [LT] genus-1 Verlinde = number of integrable simples
        """
        k = symbols("k")
        polynomial = sl3_verlinde_polynomial(1, k)
        assert polynomial.eval(level) == (level + 1) * (level + 2) // 2

    @pytest.mark.parametrize("level", range(0, 11))
    def test_genus2_polynomial_values(self, level: int):
        """The genus-2 polynomial evaluates to the genus-2 Verlinde numbers."""
        polynomial = sl3_verlinde_polynomial(2)
        assert polynomial.eval(level) == sl3_verlinde_dimension(2, level)

    @pytest.mark.parametrize("level", range(0, 19))
    def test_genus3_polynomial_values(self, level: int):
        """The interpolated genus-3 polynomial matches direct evaluation."""
        polynomial = sl3_verlinde_polynomial(3)
        assert polynomial.eval(level) == sl3_verlinde_dimension(3, level)
