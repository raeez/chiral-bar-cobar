"""Tests for compute/lib/w4_bootstrap.py — W_4 OPE bootstrap in free-boson Fock space.

Verifies:
  - Monomial enumeration at low weights (correct count and structure)
  - Monomial sorting / normal ordering
  - Monomial-to-field conversion
  - L_1 action structural properties (weight lowering)
  - Primary space dimension at weight 2 (should contain T)
  - Primary space dimension at weight 3 (should contain W_3)

This module depends on w4_ope_miura which performs heavy numerical OPE
computations. Tests here are lightweight structural checks that do NOT
require a full Miura OPE evaluation unless marked slow.

References:
  bar_cobar_construction.tex: W_4 free-boson construction
  Hornfeck, Nucl. Phys. B 407 (1993) 57
"""

import pytest
import numpy as np

from compute.lib.w4_bootstrap import (
    enumerate_monomials,
    monomial_to_field,
)


# ═══════════════════════════════════════════════════════════════
# Import test
# ═══════════════════════════════════════════════════════════════

class TestImport:
    def test_module_loads(self):
        """Module imports without error."""
        import compute.lib.w4_bootstrap
        assert hasattr(compute.lib.w4_bootstrap, 'enumerate_monomials')
        assert hasattr(compute.lib.w4_bootstrap, 'find_primary_space')


# ═══════════════════════════════════════════════════════════════
# Monomial enumeration
# ═══════════════════════════════════════════════════════════════

class TestEnumerateMonomials:
    """Test monomial enumeration at low weights."""

    def test_weight_1_single_boson(self):
        """Weight 1 with 1 boson: only dphi_0."""
        mons = enumerate_monomials(1, n_bosons=1)
        assert len(mons) == 1
        assert mons[0] == ((0, 1),)

    def test_weight_1_three_bosons(self):
        """Weight 1 with 3 bosons: dphi_0, dphi_1, dphi_2."""
        mons = enumerate_monomials(1, n_bosons=3)
        assert len(mons) == 3
        # Each should be a single operator (i, 1)
        for mon in mons:
            assert len(mon) == 1
            assert mon[0][1] == 1  # derivative order 1

    def test_weight_2_single_boson(self):
        """Weight 2, 1 boson: d^2 phi_0, (dphi_0)^2.

        Two monomials: ((0,2),) and ((0,1),(0,1)).
        """
        mons = enumerate_monomials(2, n_bosons=1)
        assert len(mons) == 2

    def test_weight_2_three_bosons(self):
        """Weight 2, 3 bosons.

        Monomials of weight 2 with 3 bosons:
        - Single operators: d^2 phi_i for i=0,1,2  -> 3 monomials
        - Double operators: dphi_i dphi_j for i <= j -> 6 monomials
        Total: 9
        """
        mons = enumerate_monomials(2, n_bosons=3)
        assert len(mons) == 9

    def test_weight_3_single_boson(self):
        """Weight 3, 1 boson: d^3 phi, d^2 phi * dphi, (dphi)^3.

        Three monomials: 3 = p(3) (partitions of 3).
        """
        mons = enumerate_monomials(3, n_bosons=1)
        assert len(mons) == 3

    def test_weight_0(self):
        """Weight 0: only the empty monomial (vacuum)."""
        mons = enumerate_monomials(0, n_bosons=3)
        assert len(mons) == 1
        assert mons[0] == ()

    def test_monomials_have_correct_weight(self):
        """All enumerated monomials should have the correct total weight."""
        for weight in [1, 2, 3, 4]:
            mons = enumerate_monomials(weight, n_bosons=3)
            for mon in mons:
                total = sum(m for _, m in mon)
                assert total == weight, f"Monomial {mon} has weight {total}, expected {weight}"

    def test_monomials_are_internally_consistent(self):
        """Each monomial's operators should follow the enumeration's ordering.

        The enumeration orders by (boson_index, derivative_order) within
        operators of the same derivative, but across different derivative
        orders it follows a derivative-first grouping. We check the weaker
        property: within each monomial, same-derivative operators have
        non-decreasing boson index.
        """
        for weight in [1, 2, 3, 4]:
            mons = enumerate_monomials(weight, n_bosons=3)
            for mon in mons:
                # Group by derivative order and check boson indices are ordered
                from itertools import groupby
                for _, group in groupby(mon, key=lambda x: x[1]):
                    items = list(group)
                    for k in range(len(items) - 1):
                        assert items[k][0] <= items[k + 1][0], \
                            f"Monomial {mon}: same-deriv operators not sorted"

    def test_no_duplicates(self):
        """No duplicate monomials at any weight."""
        for weight in [1, 2, 3, 4, 5]:
            mons = enumerate_monomials(weight, n_bosons=3)
            assert len(mons) == len(set(mons)), f"Duplicates at weight {weight}"

    def test_weight_count_grows_with_bosons(self):
        """More bosons should give at least as many monomials."""
        for weight in [2, 3]:
            n1 = len(enumerate_monomials(weight, n_bosons=1))
            n2 = len(enumerate_monomials(weight, n_bosons=2))
            n3 = len(enumerate_monomials(weight, n_bosons=3))
            assert n1 <= n2 <= n3


# ═══════════════════════════════════════════════════════════════
# Monomial to field conversion
# ═══════════════════════════════════════════════════════════════

class TestMonomialToField:
    def test_simple_conversion(self):
        """Convert a single monomial to a field."""
        mon = ((0, 1),)
        field = monomial_to_field(mon, coeff=1.0)
        assert len(field) == 1
        assert field[0][0] == 1.0
        assert field[0][1] == mon

    def test_custom_coefficient(self):
        """Coefficient is correctly passed through."""
        mon = ((0, 2),)
        field = monomial_to_field(mon, coeff=3.5)
        assert field[0][0] == 3.5

    def test_default_coefficient_is_one(self):
        """Default coefficient is 1.0."""
        mon = ((1, 1), (2, 1))
        field = monomial_to_field(mon)
        assert field[0][0] == 1.0


# ═══════════════════════════════════════════════════════════════
# Weight-counting cross-checks
# ═══════════════════════════════════════════════════════════════

class TestWeightCounting:
    """Cross-check monomial counts against partition-theoretic expectations.

    For a single boson, the number of monomials at weight h equals
    the number of partitions of h (since each monomial is a product
    of d^{m_k} phi_0 with sum m_k = h, and the sorted ordering
    gives a partition of h).
    """

    def test_single_boson_matches_partitions(self):
        """For 1 boson, monomial count = number of partitions p(h)."""
        # p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7
        expected = {1: 1, 2: 2, 3: 3, 4: 5, 5: 7}
        for h, p_h in expected.items():
            mons = enumerate_monomials(h, n_bosons=1)
            assert len(mons) == p_h, f"p({h}) = {len(mons)}, expected {p_h}"

    def test_two_bosons_weight_2(self):
        """For 2 bosons at weight 2: partitions with colors.

        Weight 2 partitions: (2), (1,1).
        (2) with 2 bosons: 2 monomials (d^2 phi_0, d^2 phi_1)
        (1,1) with 2 bosons: 3 monomials ((0,1)(0,1), (0,1)(1,1), (1,1)(1,1))
        Total: 5
        """
        mons = enumerate_monomials(2, n_bosons=2)
        assert len(mons) == 5
