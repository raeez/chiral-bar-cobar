"""Tests for spectral sequences, CE cohomology, and Orlik-Solomon algebra.

Verifies:
  - OS algebra dimensions via Poincare polynomial (Stirling numbers)
  - Arnold dimensions (n-1)! for top-degree forms
  - CE differential d^2 = 0 for sl_2
  - PBW spectral sequence known dimension tables
  - Bar comparison structural data (pole orders, desuspension, cancellation)
"""

import pytest
from sympy import Rational, Matrix


# ============================================================================
# Orlik-Solomon algebra dimensions
# ============================================================================


class TestArnoldDimension:
    """Arnold dimension = (n-1)! for top-degree OS forms on Conf_n(C)."""

    @pytest.mark.parametrize("n,expected", [
        (1, 1), (2, 1), (3, 2), (4, 6), (5, 24),
        (6, 120), (7, 720), (8, 5040), (9, 40320), (10, 362880),
    ])
    def test_arnold_dimension(self, n, expected):
        """dim H^{n-1}(Conf_n(C)) = (n-1)!."""
        from compute.lib.bar_complex import arnold_dimension
        assert arnold_dimension(n) == expected


class TestOSDimBarComparison:
    """OS^k dimensions from bar_comparison module."""

    @pytest.mark.parametrize("n", range(1, 9))
    def test_os_dim_degree_zero(self, n):
        """OS^0(Conf_n) = 1 for all n >= 1."""
        from compute.lib.bar_comparison import os_dim
        assert os_dim(n, 0) == 1

    @pytest.mark.parametrize("n", range(2, 9))
    def test_os_dim_degree_one(self, n):
        """OS^1(Conf_n) = n(n-1)/2 (number of edges in K_n)."""
        from compute.lib.bar_comparison import os_dim
        assert os_dim(n, 1) == n * (n - 1) // 2

    @pytest.mark.parametrize("n", range(1, 9))
    def test_os_total_dim(self, n):
        """Total dim of OS*(Conf_n) = n!."""
        from compute.lib.bar_comparison import os_total_dim
        from math import factorial
        assert os_total_dim(n) == factorial(n)


class TestOSDimOSAlgebra:
    """OS^k dimensions from os_algebra module (independent implementation)."""

    @pytest.mark.parametrize("n", range(1, 8))
    def test_os_dimension_degree_zero(self, n):
        """OS^0(Conf_n) = 1."""
        from compute.lib.os_algebra import os_dimension
        assert os_dimension(n, 0) == 1

    @pytest.mark.parametrize("n", range(2, 8))
    def test_os_dimension_degree_one(self, n):
        """OS^1(Conf_n) = n(n-1)/2."""
        from compute.lib.os_algebra import os_dimension
        assert os_dimension(n, 1) == n * (n - 1) // 2

    @pytest.mark.parametrize("n,expected", [
        (3, 2), (4, 6), (5, 24), (6, 120), (7, 720),
    ])
    def test_os_dimension_top_degree(self, n, expected):
        """OS^{n-1}(Conf_n) = (n-1)!."""
        from compute.lib.os_algebra import os_dimension
        assert os_dimension(n, n - 1) == expected

    def test_os_dimension_vanishing(self):
        """OS^k(Conf_n) = 0 for k >= n."""
        from compute.lib.os_algebra import os_dimension
        assert os_dimension(3, 3) == 0
        assert os_dimension(4, 4) == 0
        assert os_dimension(5, 5) == 0


class TestMaximalFormDims:
    """MAXIMAL_FORM_DIMS ground truth table."""

    @pytest.mark.parametrize("n,expected", [
        (1, 1), (2, 1), (3, 2), (4, 6), (5, 24), (6, 120),
    ])
    def test_maximal_form_dims(self, n, expected):
        """MAXIMAL_FORM_DIMS[n] = (n-1)!."""
        from compute.lib.bar_comparison import MAXIMAL_FORM_DIMS
        assert MAXIMAL_FORM_DIMS[n] == expected


class TestOSCrossCheck:
    """Cross-check: os_dim (bar_comparison) vs os_dimension (os_algebra)."""

    @pytest.mark.parametrize("n,k", [
        (2, 0), (2, 1), (3, 0), (3, 1), (3, 2),
        (4, 0), (4, 1), (4, 2), (4, 3),
        (5, 0), (5, 1), (5, 2), (5, 3), (5, 4),
    ])
    def test_two_implementations_agree(self, n, k):
        """bar_comparison.os_dim and os_algebra.os_dimension agree."""
        from compute.lib.bar_comparison import os_dim
        from compute.lib.os_algebra import os_dimension
        assert os_dim(n, k) == os_dimension(n, k)


# ============================================================================
# CE differential d^2 = 0
# ============================================================================


def _sl2_integer_structure_constants():
    """Convert sl_2 structure constants to integer-indexed format.

    Basis ordering: 0=e, 1=h, 2=f.
    [e,f]=h, [h,e]=2e, [h,f]=-2f.
    """
    sc = {}
    # [e, f] = h  =>  (0, 2) -> {1: 1}
    sc[(0, 2)] = {1: Rational(1)}
    # [h, e] = 2e  =>  (0, 1) -> {0: -2}  (antisymmetry: [e,h] = -2e)
    # Store as (a,b) with a < b: [e, h] = -2e
    sc[(0, 1)] = {0: Rational(-2)}
    # [h, f] = -2f => [h,f] = -2f => stored as (1, 2) -> {2: -2}
    sc[(1, 2)] = {2: Rational(-2)}
    return sc


class TestCEDifferentialSl2:
    """Chevalley-Eilenberg differential d^2 = 0 for sl_2."""

    def test_d0_shape(self):
        """d_0: Lambda^0 -> Lambda^1 has shape (3, 1)."""
        from compute.lib.spectral_sequence import ce_differential_matrix
        sc = _sl2_integer_structure_constants()
        d0 = ce_differential_matrix(3, sc, 0)
        assert d0.shape == (3, 1)

    def test_d1_shape(self):
        """d_1: Lambda^1 -> Lambda^2 has shape (3, 3)."""
        from compute.lib.spectral_sequence import ce_differential_matrix
        sc = _sl2_integer_structure_constants()
        d1 = ce_differential_matrix(3, sc, 1)
        assert d1.shape == (3, 3)

    def test_d2_shape(self):
        """d_2: Lambda^2 -> Lambda^3 has shape (1, 3)."""
        from compute.lib.spectral_sequence import ce_differential_matrix
        sc = _sl2_integer_structure_constants()
        d2 = ce_differential_matrix(3, sc, 2)
        assert d2.shape == (1, 3)

    def test_d1_circ_d0_is_zero(self):
        """d_1 * d_0 = 0 (CE d^2 = 0 at degree 0)."""
        from compute.lib.spectral_sequence import ce_differential_matrix
        sc = _sl2_integer_structure_constants()
        d0 = ce_differential_matrix(3, sc, 0)
        d1 = ce_differential_matrix(3, sc, 1)
        product = d1 * d0
        assert product == Matrix([[0], [0], [0]])

    def test_d2_circ_d1_is_zero(self):
        """d_2 * d_1 = 0 (CE d^2 = 0 at degree 1)."""
        from compute.lib.spectral_sequence import ce_differential_matrix
        sc = _sl2_integer_structure_constants()
        d1 = ce_differential_matrix(3, sc, 1)
        d2 = ce_differential_matrix(3, sc, 2)
        product = d2 * d1
        assert product == Matrix([[0, 0, 0]])


# ============================================================================
# PBW spectral sequence dimension tables
# ============================================================================


class TestVirasoroBarCoh:
    """Virasoro bar cohomology dimensions (associahedron/Catalan structure)."""

    @pytest.mark.parametrize("deg,expected", [
        (1, 1), (2, 2), (3, 5), (4, 12), (5, 30),
        (6, 76), (7, 196), (8, 512), (9, 1353), (10, 3610),
    ])
    def test_virasoro_bar_coh(self, deg, expected):
        """Virasoro bar H^n matches known table."""
        from compute.lib.spectral_sequence import VIRASORO_BAR_COH
        assert VIRASORO_BAR_COH[deg] == expected

    def test_virasoro_bar_coh_positive(self):
        """All Virasoro bar cohomology entries are positive."""
        from compute.lib.spectral_sequence import VIRASORO_BAR_COH
        for deg, dim in VIRASORO_BAR_COH.items():
            assert dim > 0, f"dim at degree {deg} should be positive"

    def test_virasoro_bar_coh_monotone(self):
        """Virasoro bar cohomology dimensions are strictly increasing."""
        from compute.lib.spectral_sequence import VIRASORO_BAR_COH
        dims = [VIRASORO_BAR_COH[i] for i in range(1, 11)]
        for i in range(len(dims) - 1):
            assert dims[i] < dims[i + 1]


class TestSl2BarCoh:
    """sl_2 bar cohomology known dimensions."""

    @pytest.mark.parametrize("deg,expected", [
        (1, 3), (2, 5), (3, 15),
    ])
    def test_sl2_bar_coh(self, deg, expected):
        """sl_2 bar H^n matches known values."""
        from compute.lib.spectral_sequence import SL2_BAR_COH
        assert SL2_BAR_COH[deg] == expected

    def test_sl2_bar_deg1_equals_dim(self):
        """sl_2 bar H^1 = dim(sl_2) = 3."""
        from compute.lib.spectral_sequence import SL2_BAR_COH
        assert SL2_BAR_COH[1] == 3

    def test_sl2_bar_deg2_is_5(self):
        """sl_2 bar H^2 = 5, NOT Riordan R(5) = 6."""
        from compute.lib.spectral_sequence import SL2_BAR_COH
        assert SL2_BAR_COH[2] == 5


class TestHeisensteinBarE2:
    """Heisenberg bar cohomology E_2 leading weight."""

    def test_heisenstein_leading_weight_all_one(self):
        """Leading-weight E_2 contribution is 1 in each degree."""
        from compute.lib.spectral_sequence import HEISENBERG_BAR_COH_E2_LEADING
        for n in range(1, 11):
            assert HEISENBERG_BAR_COH_E2_LEADING[n] == 1


class TestFermionBarCoh:
    """Free fermion bar cohomology."""

    def test_fermion_deg1(self):
        """F_2 bar H^1 = 2 (two generators)."""
        from compute.lib.spectral_sequence import FERMION_BAR_COH
        assert FERMION_BAR_COH[1] == 2

    def test_fermion_deg2(self):
        """F_2 bar H^2 = 3."""
        from compute.lib.spectral_sequence import FERMION_BAR_COH
        assert FERMION_BAR_COH[2] == 3


# ============================================================================
# Bar comparison structural data
# ============================================================================


class TestPoleOrders:
    """Highest pole orders in the OPE for each family."""

    @pytest.mark.parametrize("algebra,expected_pole", [
        ("Heisenberg", 2),
        ("sl2", 2),
        ("sl3", 2),
        ("Virasoro", 4),
        ("W3", 6),
        ("free_fermion", 1),
        ("beta_gamma", 1),
        ("bc", 1),
    ])
    def test_pole_order(self, algebra, expected_pole):
        """Highest pole order matches family structure."""
        from compute.lib.bar_comparison import POLE_ORDERS
        assert POLE_ORDERS[algebra]["highest_pole"] == expected_pole

    def test_all_pole_orders_positive(self):
        """All pole orders are positive integers."""
        from compute.lib.bar_comparison import POLE_ORDERS
        for alg, data in POLE_ORDERS.items():
            assert data["highest_pole"] > 0
            assert isinstance(data["highest_pole"], int)


class TestDesuspensionParity:
    """Desuspension s^{-1} flips parity: bosonic -> odd, fermionic -> even."""

    def test_bosonic_to_odd(self):
        """Bosonic generators become odd after desuspension."""
        from compute.lib.bar_comparison import desuspension_parity
        assert desuspension_parity(True) == "odd"

    def test_fermionic_to_even(self):
        """Fermionic generators become even after desuspension."""
        from compute.lib.bar_comparison import desuspension_parity
        assert desuspension_parity(False) == "even"

    def test_bosonic_exterior_coalgebra(self):
        """Bosonic generators -> exterior coalgebra after desuspension."""
        from compute.lib.bar_comparison import coalgebra_type
        assert coalgebra_type(True) == "exterior"

    def test_fermionic_symmetric_coalgebra(self):
        """Fermionic generators -> symmetric coalgebra after desuspension."""
        from compute.lib.bar_comparison import coalgebra_type
        assert coalgebra_type(False) == "symmetric"


class TestGeneratorParity:
    """GENERATOR_PARITY table consistency."""

    @pytest.mark.parametrize("algebra,bosonic", [
        ("Heisenberg", True),
        ("sl2", True),
        ("Virasoro", True),
        ("W3", True),
        ("free_fermion", False),
        ("bc", False),
        ("beta_gamma", True),
    ])
    def test_generator_parity_consistent(self, algebra, bosonic):
        """Generator parity and coalgebra type are consistent."""
        from compute.lib.bar_comparison import GENERATOR_PARITY
        data = GENERATOR_PARITY[algebra]
        assert data["bosonic"] == bosonic
        expected_coal = "exterior" if bosonic else "symmetric"
        assert data["coalgebra"] == expected_coal


class TestArnoldCancellation:
    """Arnold cancellation data for all families."""

    def test_all_families_have_cancellation_data(self):
        """Arnold cancellation data exists for all pole-order families."""
        from compute.lib.bar_comparison import ARNOLD_CANCELLATION, POLE_ORDERS
        for alg in POLE_ORDERS:
            assert alg in ARNOLD_CANCELLATION

    @pytest.mark.parametrize("algebra", [
        "Heisenberg", "sl2", "sl3", "Virasoro", "W3",
        "free_fermion", "beta_gamma", "bc",
    ])
    def test_deg3_cancellation_present(self, algebra):
        """Degree-3 Arnold cancellation is active for all families."""
        from compute.lib.bar_comparison import ARNOLD_CANCELLATION
        assert ARNOLD_CANCELLATION[algebra]["deg3"] is True
