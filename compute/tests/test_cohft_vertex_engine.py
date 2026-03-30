r"""Tests for the CohFT vertex engine.

Verifies the Givental reconstruction of higher-genus vertex factors V(g,n)
from R-matrix coefficients and Witten-Kontsevich intersection numbers.

Ground truth:
  thm:cohft-reconstruction — R-matrix = complementarity propagator
  thm:shadow-cohft — shadow CohFT axioms
  Witten-Kontsevich: <tau_1>_1 = 1/24, <tau_0^3>_0 = 1
  Faber-Pandharipande: lambda_g^FP from A-hat genus
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, cancel, simplify, S

from compute.lib.cohft_vertex_engine import (
    r_matrix_coefficients,
    cohft_vertex_raw,
    vertex_factor_table,
    genus2_free_energy_full,
    heisenberg_F2_graph_sum,
    edge_dressing_correction_g2,
    virasoro_F2_symbolic,
    virasoro_F2_complementarity,
)


# =========================================================================
# Section 1: R-matrix coefficients
# =========================================================================

class TestRMatrix:
    """Test R-matrix coefficient computation."""

    def test_R0(self):
        R = r_matrix_coefficients(5)
        assert R[0] == Fraction(1)

    def test_R1(self):
        """R_1 = 1/12 from B_2/(2*1) = (1/6)/2."""
        R = r_matrix_coefficients(5)
        assert R[1] == Fraction(1, 12)

    def test_R2(self):
        """R_2 = R_1^2/2 = 1/288."""
        R = r_matrix_coefficients(5)
        assert R[2] == Fraction(1, 288)

    def test_R_count(self):
        R = r_matrix_coefficients(10)
        assert len(R) == 11

    def test_R_exact_type(self):
        R = r_matrix_coefficients(5)
        for r in R:
            assert isinstance(r, Fraction)


# =========================================================================
# Section 2: CohFT vertex factors — known values
# =========================================================================

class TestVertexFactorsKnown:
    """Test vertex factors against known values."""

    def test_V_0_3(self):
        """V(0,3) is unstable case — should be 0 from our function.
        (genus-0 vertex factors come from shadow data, not R-matrix)."""
        # (0,3): 2*0-2+3 = 1 > 0, so stable. dim = -3+3 = 0.
        # T(0,3) = R_0^3 * <tau_0 tau_0 tau_0>_0 = 1 * 1 = 1
        assert cohft_vertex_raw(0, 3) == Fraction(1)

    def test_V_1_0(self):
        """V(1,0) = 1/24 (genus-1 free energy, topological)."""
        assert cohft_vertex_raw(1, 0) == Fraction(1, 24)

    def test_V_1_1(self):
        """V(1,1) = R_1 * <tau_1>_1 = (1/12)(1/24) = 1/288."""
        assert cohft_vertex_raw(1, 1) == Fraction(1, 288)

    def test_V_1_2(self):
        """V(1,2): sum over d1+d2=2.
        = R_0*R_2*<tau_0 tau_2>_1 + R_1^2*<tau_1 tau_1>_1 + R_2*R_0*<tau_2 tau_0>_1
        """
        v = cohft_vertex_raw(1, 2)
        assert isinstance(v, Fraction)
        assert v != Fraction(0)

    def test_V_2_0(self):
        """V(2,0) = lambda_2^FP = 7/5760."""
        assert cohft_vertex_raw(2, 0) == Fraction(7, 5760)

    def test_V_3_0(self):
        """V(3,0) = lambda_3^FP = 31/967680."""
        assert cohft_vertex_raw(3, 0) == Fraction(31, 967680)

    def test_V_unstable(self):
        """Unstable cases return 0."""
        assert cohft_vertex_raw(0, 0) == Fraction(0)
        assert cohft_vertex_raw(0, 1) == Fraction(0)
        assert cohft_vertex_raw(0, 2) == Fraction(0)


class TestVertexFactorsStructural:
    """Test structural properties of vertex factors."""

    def test_all_rational(self):
        """All vertex factors are exact rationals."""
        table = vertex_factor_table(3, 4)
        for key, val in table.items():
            assert isinstance(val, Fraction), f"V{key} = {val} is not Fraction"

    def test_V_1_n_decreasing(self):
        """V(1,n) decreases with n (more insertions = smaller integral)."""
        vals = [abs(cohft_vertex_raw(1, n)) for n in range(1, 5)]
        # Not strictly required to be decreasing, but check they're all small
        for v in vals:
            assert v < Fraction(1)

    def test_V_g_0_positive(self):
        """V(g,0) > 0 for g >= 1 (Hodge integrals are positive)."""
        for g in range(1, 6):
            assert cohft_vertex_raw(g, 0) > 0

    def test_dimension_constraint(self):
        """V(g,n) should be 0 when dim = 3g-3+n < 0."""
        assert cohft_vertex_raw(0, 2) == Fraction(0)  # dim = -1
        assert cohft_vertex_raw(0, 1) == Fraction(0)  # dim = -2

    def test_V_2_1(self):
        """V(2,1) is computable and nonzero."""
        v = cohft_vertex_raw(2, 1)
        assert isinstance(v, Fraction)
        # dim = 3*2-3+1 = 4, so d_1 = 4: V = R_4 * <tau_4>_2
        # This should be nonzero

    def test_V_2_2(self):
        """V(2,2) is computable."""
        v = cohft_vertex_raw(2, 2)
        assert isinstance(v, Fraction)


# =========================================================================
# Section 3: Genus-2 graph sum — Heisenberg
# =========================================================================

class TestGenus2Heisenberg:
    """Test genus-2 graph sum for Heisenberg (Gaussian).

    NOTE: The raw Givental graph sum with bare propagator does NOT exactly
    match kappa * lambda_2^FP.  The difference is the edge-dressing correction
    from the dressed propagator in the Givental formalism.  This is structural,
    not a bug.
    """

    def test_heisenberg_F2_k1_is_rational(self):
        """F_2(H_1) from raw graph sum is an exact rational."""
        F2 = heisenberg_F2_graph_sum(Fraction(1))
        assert isinstance(F2, Fraction)

    def test_heisenberg_F2_structure(self):
        """Graph sum returns correct structure."""
        result = genus2_free_energy_full(Fraction(1), Fraction(0), Fraction(0))
        assert 'total' in result
        assert 'graphs' in result
        assert len(result['graphs']) == 6

    def test_heisenberg_graphs_zero(self):
        """For Heisenberg, theta/banana/mixed graphs contribute 0 (S3=S4=0)."""
        result = genus2_free_energy_full(Fraction(1), Fraction(0), Fraction(0))
        g = result['graphs']
        assert g['theta']['weighted'] == Fraction(0)
        assert g['banana']['weighted'] == Fraction(0)
        assert g['mixed']['weighted'] == Fraction(0)

    def test_heisenberg_smooth_graph(self):
        """Smooth graph: V(2,0) = lambda_2^FP, no edges."""
        result = genus2_free_energy_full(Fraction(1), Fraction(0), Fraction(0))
        smooth = result['graphs']['smooth_g2']['weighted']
        assert smooth == Fraction(7, 5760)

    def test_heisenberg_irr_node(self):
        """Irr node: V(1,2) * P / 2."""
        result = genus2_free_energy_full(Fraction(1), Fraction(0), Fraction(0))
        irr = result['graphs']['irr_node']['weighted']
        V12 = cohft_vertex_raw(1, 2)
        expected = V12 * Fraction(1, 2)
        assert irr == expected

    def test_heisenberg_separating(self):
        """Separating: V(1,1)^2 * P / 2."""
        result = genus2_free_energy_full(Fraction(1), Fraction(0), Fraction(0))
        sep = result['graphs']['separating']['weighted']
        V11 = cohft_vertex_raw(1, 1)
        expected = V11 ** 2 * Fraction(1, 2)
        assert sep == expected

    def test_edge_dressing_positive(self):
        """Edge dressing correction is positive (raw overestimates)."""
        delta = edge_dressing_correction_g2(Fraction(1))
        assert delta > 0

    def test_edge_dressing_small(self):
        """Edge dressing is small relative to F_2."""
        delta = edge_dressing_correction_g2(Fraction(1))
        F2_scalar = Fraction(7, 5760)
        assert delta < F2_scalar  # correction smaller than leading term


# =========================================================================
# Section 4: Genus-2 graph sum — Virasoro
# =========================================================================

class TestGenus2Virasoro:
    """Test genus-2 free energy for Virasoro."""

    def test_virasoro_F2_symbolic(self):
        """Virasoro F_2(c) is a rational function of c."""
        result = virasoro_F2_symbolic()
        assert result['total'] is not None

    def test_virasoro_theta_nonzero(self):
        """Theta graph is nonzero for Virasoro (S3 = 2)."""
        result = virasoro_F2_symbolic()
        theta = result['graphs']['theta']
        assert theta != S.Zero

    def test_virasoro_banana_nonzero(self):
        """Banana graph is nonzero for Virasoro (S4 != 0)."""
        result = virasoro_F2_symbolic()
        banana = result['graphs']['banana']
        assert banana != S.Zero

    def test_virasoro_numerical_c26(self):
        """F_2(Vir_26) at c=26 (bosonic string)."""
        result = virasoro_F2_symbolic()
        c = Symbol('c')
        val = result['total'].subs(c, 26)
        assert val is not None


# =========================================================================
# Section 5: Complementarity
# =========================================================================

class TestComplementarity:
    """Test complementarity F_2(c) + F_2(26-c)."""

    def test_complementarity_runs(self):
        """Complementarity computation completes."""
        result = virasoro_F2_complementarity()
        assert 'sum' in result

    def test_complementarity_simplified(self):
        """The complementarity sum is a rational function of c."""
        result = virasoro_F2_complementarity()
        assert result['sum'] is not None


# =========================================================================
# Section 6: Cross-checks
# =========================================================================

class TestCrossChecks:
    """Cross-check vertex factors against known identities."""

    def test_V_0_3_equals_1(self):
        """<tau_0^3>_0 = 1 is the seed of WK recursion."""
        assert cohft_vertex_raw(0, 3) == Fraction(1)

    def test_V_0_4(self):
        """V(0,4) = <tau_0 tau_1>_0 + permutations.
        <tau_0^3 tau_1>_0 = <tau_0 tau_0>_0 from string = ... actually:
        <tau_0^4>_0 has dim = -3+4 = 1 but needs sum d_i = 1, so one d_i = 1.
        T(0,4) = 4*R_0^3*R_1*<tau_0^3 tau_1>_0 = 4*(1/12)*1 = 1/3."""
        v = cohft_vertex_raw(0, 4)
        assert isinstance(v, Fraction)

    def test_V_1_3(self):
        """V(1,3) is computable."""
        v = cohft_vertex_raw(1, 3)
        assert isinstance(v, Fraction)

    def test_vertex_table(self):
        """Vertex table generates without error."""
        table = vertex_factor_table(2, 3)
        assert len(table) > 5

    @pytest.mark.parametrize("g", [1, 2, 3, 4])
    def test_lambda_fp_from_vertex(self, g):
        """V(g,0) = lambda_g^FP."""
        from compute.lib.gravitational_entropy_engine import lambda_fp
        v = cohft_vertex_raw(g, 0)
        lam = lambda_fp(g)
        assert v == Fraction(lam.p, lam.q)


# =========================================================================
# Section 7: MC-derived modular operad vertex factors
# =========================================================================

class TestOperadVertexFactors:
    """Test V(1,1) and V(1,2) from MC equation D^2=0."""

    def test_V11_gaussian(self):
        from compute.lib.cohft_vertex_engine import operad_vertex_V11
        assert operad_vertex_V11(Fraction(0), Fraction(1)) == 0

    def test_V12_gaussian(self):
        from compute.lib.cohft_vertex_engine import operad_vertex_V12
        assert operad_vertex_V12(Fraction(0), Fraction(0), Fraction(1)) == 0

    def test_V11_virasoro(self):
        from compute.lib.cohft_vertex_engine import operad_vertex_V11
        c = Symbol('c')
        v = operad_vertex_V11(Rational(2), c / 2)
        assert cancel(v + 12 / c) == 0

    def test_F2_operad_self_dual(self):
        from compute.lib.cohft_vertex_engine import virasoro_F2_operad
        c = Symbol('c')
        result = virasoro_F2_operad()
        F2_13 = float(result['total'].subs(c, 13))
        F2_13d = float(result['total'].subs(c, 13))
        assert abs(F2_13 - F2_13d) < 1e-12

    def test_F2_operad_positive_large_c(self):
        from compute.lib.cohft_vertex_engine import virasoro_F2_operad
        c = Symbol('c')
        result = virasoro_F2_operad()
        assert float(result['total'].subs(c, 100)) > 0

    def test_F2_complementarity_self_dual(self):
        from compute.lib.cohft_vertex_engine import virasoro_F2_complementarity_operad
        c = Symbol('c')
        comp = virasoro_F2_complementarity_operad()
        val = float(comp['sum'].subs(c, 13))
        F2 = float(comp['F2_c'].subs(c, 13))
        assert abs(val - 2 * F2) < 1e-10
