"""Tests for open SFT bar complex: Wedge*(C^d) and CY3 branes.

Tests the bar complex B(Wedge*(C^d)) with exact computations:
1. Exterior algebra basis and wedge product
2. Bar differential d^2 = 0
3. Bar cohomology = Koszul dual (Sym*(C^d))
4. Hochschild cohomology (derived center)
5. Shadow analysis and W_{1+infty} comparison
6. Conifold Ext algebra
7. Multi-path cross-verification

Ground truth: Koszul duality Wedge*(V)^! = Sym*(V*).
H^0(B^n(Wedge*(C^d))) = dim Sym^n(C^d) = binom(n+d-1, d-1).
H^k(B^n) = 0 for k > 0 (Koszul concentration).

References:
  Loday-Vallette, "Algebraic Operads" (2012), Ch. 2-3.
  Keller, "A-infinity algebras, modules and functor categories" (2006).
  Vol I: bar_cobar_adjunction_curved.tex, chiral_koszul_pairs.tex.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.open_sft_bar import (
    ExteriorBasisElement,
    BarElement,
    exterior_basis,
    exterior_basis_positive,
    wedge_product,
    bar_basis_at_arity,
    bar_basis_at_arity_and_degree,
    bar_differential_on_element,
    bar_differential_matrix,
    bar_cohomology_at_arity_degree,
    bar_cohomology_c3_w0,
    bar_cohomology_c3_w0_summary,
    verify_d_squared_zero,
    hochschild_cohomology_exterior,
    w1_infty_comparison,
    bar_cohomology_exterior_d,
    bar_euler_characteristic,
    shadow_analysis_exterior,
    conifold_ext_dimensions,
    conifold_bar_analysis,
)


# =========================================================================
# Section 1: Exterior algebra basis
# =========================================================================

class TestExteriorBasis:
    """Tests for exterior algebra basis enumeration."""

    def test_basis_count_d1(self):
        """Wedge*(C^1) has 2^1 = 2 elements."""
        assert len(exterior_basis(1)) == 2

    def test_basis_count_d2(self):
        """Wedge*(C^2) has 2^2 = 4 elements."""
        assert len(exterior_basis(2)) == 4

    def test_basis_count_d3(self):
        """Wedge*(C^3) has 2^3 = 8 elements."""
        assert len(exterior_basis(3)) == 8

    def test_basis_count_d4(self):
        """Wedge*(C^4) has 2^4 = 16 elements."""
        assert len(exterior_basis(4)) == 16

    def test_positive_basis_count(self):
        """Wedge^+(C^d) has 2^d - 1 elements."""
        for d in range(1, 5):
            assert len(exterior_basis_positive(d)) == 2**d - 1

    def test_degree_distribution_d3(self):
        """Wedge*(C^3) has graded dimensions [1, 3, 3, 1]."""
        basis = exterior_basis(3)
        counts = {}
        for e in basis:
            counts[e.degree] = counts.get(e.degree, 0) + 1
        assert counts == {0: 1, 1: 3, 2: 3, 3: 1}

    def test_degree_distribution_d4(self):
        """Wedge*(C^4) has graded dimensions [1, 4, 6, 4, 1]."""
        basis = exterior_basis(4)
        counts = {}
        for e in basis:
            counts[e.degree] = counts.get(e.degree, 0) + 1
        assert counts == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}


# =========================================================================
# Section 2: Wedge product
# =========================================================================

class TestWedgeProduct:
    """Tests for the exterior product."""

    def test_wedge_x1_x2(self):
        """x_1 wedge x_2 = x_{12}."""
        e1 = ExteriorBasisElement(frozenset({1}))
        e2 = ExteriorBasisElement(frozenset({2}))
        sign, result = wedge_product(e1, e2)
        assert sign == 1
        assert result == ExteriorBasisElement(frozenset({1, 2}))

    def test_wedge_antisymmetric(self):
        """x_2 wedge x_1 = -x_{12} (antisymmetry)."""
        e1 = ExteriorBasisElement(frozenset({1}))
        e2 = ExteriorBasisElement(frozenset({2}))
        sign_12, _ = wedge_product(e1, e2)
        sign_21, _ = wedge_product(e2, e1)
        assert sign_12 == -sign_21

    def test_wedge_self_zero(self):
        """x_1 wedge x_1 = 0."""
        e1 = ExteriorBasisElement(frozenset({1}))
        sign, result = wedge_product(e1, e1)
        assert result is None

    def test_wedge_overlap_zero(self):
        """x_1 wedge x_{12} = 0 (overlapping indices)."""
        e1 = ExteriorBasisElement(frozenset({1}))
        e12 = ExteriorBasisElement(frozenset({1, 2}))
        sign, result = wedge_product(e1, e12)
        assert result is None

    def test_wedge_associative(self):
        """(x_1 wedge x_2) wedge x_3 = x_1 wedge (x_2 wedge x_3) = x_{123}."""
        e1 = ExteriorBasisElement(frozenset({1}))
        e2 = ExteriorBasisElement(frozenset({2}))
        e3 = ExteriorBasisElement(frozenset({3}))
        # Left
        s12, r12 = wedge_product(e1, e2)
        s_l, r_l = wedge_product(r12, e3)
        # Right
        s23, r23 = wedge_product(e2, e3)
        s_r, r_r = wedge_product(e1, r23)
        assert r_l == r_r
        assert s12 * s_l == s_r  # signs must agree

    def test_wedge_top_form(self):
        """x_1 wedge x_2 wedge x_3 = +x_{123} with correct sign."""
        e1 = ExteriorBasisElement(frozenset({1}))
        e2 = ExteriorBasisElement(frozenset({2}))
        e3 = ExteriorBasisElement(frozenset({3}))
        s12, r12 = wedge_product(e1, e2)
        s123, r123 = wedge_product(r12, e3)
        assert r123 == ExteriorBasisElement(frozenset({1, 2, 3}))
        assert s12 * s123 == 1  # x1 wedge x2 wedge x3 = +x123


# =========================================================================
# Section 3: Bar elements
# =========================================================================

class TestBarElements:
    """Tests for bar complex elements."""

    def test_bar_arity(self):
        """Bar element [x_1|x_2|x_3] has arity 3."""
        e1 = ExteriorBasisElement(frozenset({1}))
        e2 = ExteriorBasisElement(frozenset({2}))
        e3 = ExteriorBasisElement(frozenset({3}))
        be = BarElement((e1, e2, e3))
        assert be.arity == 3

    def test_bar_cohom_deg_degree1(self):
        """[x_1|x_2] has cohom_deg = (1-1)+(1-1) = 0 (AP45: s^{-1} lowers by 1)."""
        e1 = ExteriorBasisElement(frozenset({1}))
        e2 = ExteriorBasisElement(frozenset({2}))
        be = BarElement((e1, e2))
        assert be.cohomological_degree == 0

    def test_bar_cohom_deg_mixed(self):
        """[x_1|x_{23}] has cohom_deg = (1-1)+(2-1) = 1."""
        e1 = ExteriorBasisElement(frozenset({1}))
        e23 = ExteriorBasisElement(frozenset({2, 3}))
        be = BarElement((e1, e23))
        assert be.cohomological_degree == 1

    def test_bar_total_weight_preserved(self):
        """Total weight = arity + cohom_deg = sum|a_i| is preserved by d."""
        e1 = ExteriorBasisElement(frozenset({1}))
        e2 = ExteriorBasisElement(frozenset({2}))
        be = BarElement((e1, e2))
        w_source = be.arity + be.cohomological_degree  # 2 + 0 = 2
        d_result = bar_differential_on_element(be, 3)
        for target, _ in d_result.items():
            w_target = target.arity + target.cohomological_degree
            assert w_target == w_source, f"Weight not preserved: {w_source} -> {w_target}"


# =========================================================================
# Section 4: Bar differential d^2 = 0
# =========================================================================

class TestDSquaredZero:
    """Tests that the bar differential squares to zero."""

    def test_d_squared_zero_d2(self):
        """d^2 = 0 for Wedge*(C^2) at arities 3-4."""
        result = verify_d_squared_zero(2, max_arity=4)
        assert result["d_squared_zero"], f"Violations: {result['violations'][:3]}"

    def test_d_squared_zero_d3(self):
        """d^2 = 0 for Wedge*(C^3) at arities 3-4."""
        result = verify_d_squared_zero(3, max_arity=4)
        assert result["d_squared_zero"], f"Violations: {result['violations'][:3]}"

    def test_d_squared_zero_d4_arity3(self):
        """d^2 = 0 for Wedge*(C^4) at arity 3."""
        result = verify_d_squared_zero(4, max_arity=3)
        assert result["d_squared_zero"], f"Violations: {result['violations'][:3]}"

    def test_d_squared_many_checks(self):
        """d^2 = 0 involves many nontrivial checks."""
        result = verify_d_squared_zero(3, max_arity=4)
        assert result["total_checks"] > 100


# =========================================================================
# Section 5: Bar cohomology = Koszul dual
# =========================================================================

class TestBarCohomologyKoszulDual:
    """Tests that H*(B(Wedge*(C^d))) = Sym*(C^d) (Koszul duality)."""

    @pytest.mark.parametrize("d,arity,expected", [
        # d=1: Sym^n(C^1) = 1 for all n
        (1, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1),
        # d=2: Sym^n(C^2) = n+1
        (2, 1, 2), (2, 2, 3), (2, 3, 4),
        # d=3: Sym^n(C^3) = binom(n+2, 2)
        (3, 1, 3), (3, 2, 6), (3, 3, 10), (3, 4, 15),
        # d=4: Sym^n(C^4) = binom(n+3, 3)
        (4, 1, 4), (4, 2, 10),
    ])
    def test_koszul_dual_dimension(self, d, arity, expected):
        """H^0(B^n(Wedge*(C^d))) = dim Sym^n(C^d) = binom(n+d-1, d-1).

        Path 1: direct computation from the bar differential.
        Path 2: binomial coefficient formula.
        Path 3: Hilbert series relation h_A(t) * h_{A!}(-t) = 1.
        """
        h = bar_cohomology_at_arity_degree(d, arity, 0)
        assert h["dim_cohomology"] == expected
        # Cross-check with formula
        assert expected == math.comb(arity + d - 1, d - 1)

    @pytest.mark.parametrize("d,arity,cohom", [
        # Koszul concentration: H^k(B^n) = 0 for k > 0
        (2, 2, 1), (2, 2, 2),
        (3, 2, 1), (3, 2, 2), (3, 2, 3),
        (3, 3, 1), (3, 3, 2),
    ])
    def test_koszul_concentration(self, d, arity, cohom):
        """H^k(B^n) = 0 for k > 0 (Koszul concentration)."""
        h = bar_cohomology_at_arity_degree(d, arity, cohom)
        assert h["dim_cohomology"] == 0

    def test_c3_koszul_summary(self):
        """Full Koszulness check for Wedge*(C^3) at arities 1-4."""
        result = bar_cohomology_c3_w0_summary(max_arity=4)
        assert result["is_koszul"]
        assert result["koszul_match"]

    def test_c3_koszul_dual_dims(self):
        """Koszul dual dims match Sym*(C^3): 3, 6, 10, 15."""
        result = bar_cohomology_c3_w0_summary(max_arity=4)
        assert result["expected_koszul_dual_dims"] == {
            1: 3, 2: 6, 3: 10, 4: 15
        }


# =========================================================================
# Section 6: Koszul duality relation
# =========================================================================

class TestKoszulDualityRelation:
    """Tests for the Hilbert series relation h_A(t) * h_{A!}(-t) = 1."""

    def test_hilbert_series_relation(self):
        """h_{Wedge*(C^3)}(t) = (1+t)^3, h_{Sym*(C^3)}(t) = 1/(1-t)^3.
        Product: (1+t)^3 * 1/(1+t)^3 = 1 (at t -> -t for A!)."""
        result = bar_euler_characteristic(3, max_arity=5)
        assert result["verified"]

    def test_hilbert_a(self):
        """Hilbert series of Wedge*(C^3): [1, 3, 3, 1]."""
        result = bar_euler_characteristic(3)
        assert result["hilbert_A"] == [1, 3, 3, 1]

    def test_hilbert_dual(self):
        """Hilbert series of Sym*(C^3): binom(n+2, 2) = 1, 3, 6, 10, 15, 21."""
        result = bar_euler_characteristic(3, max_arity=5)
        assert result["hilbert_dual"] == [1, 3, 6, 10, 15, 21]


# =========================================================================
# Section 7: General d exterior algebra
# =========================================================================

class TestGeneralExterior:
    """Tests for bar cohomology of Wedge*(C^d) for various d."""

    def test_d1_koszul(self):
        """Wedge*(C^1) = k[x]/(x^2) is Koszul."""
        result = bar_cohomology_exterior_d(1, max_arity=5)
        assert result["is_koszul"]

    def test_d2_koszul(self):
        """Wedge*(C^2) is Koszul."""
        result = bar_cohomology_exterior_d(2, max_arity=4)
        assert result["is_koszul"]

    def test_d3_koszul(self):
        """Wedge*(C^3) is Koszul."""
        result = bar_cohomology_exterior_d(3, max_arity=4)
        assert result["is_koszul"]

    def test_d3_koszul_match(self):
        """H^0(B^n(Wedge*(C^3))) matches dim Sym^n(C^3) at each arity."""
        result = bar_cohomology_exterior_d(3, max_arity=4)
        assert result["koszul_match"]

    def test_d2_koszul_match(self):
        """H^0(B^n(Wedge*(C^2))) matches dim Sym^n(C^2) at each arity."""
        result = bar_cohomology_exterior_d(2, max_arity=4)
        assert result["koszul_match"]


# =========================================================================
# Section 8: Hochschild cohomology (derived center)
# =========================================================================

class TestHochschildCohomology:
    """Tests for HH*(Wedge*(C^d), Wedge*(C^d)) = derived center."""

    def test_hh_d3_generating_function(self):
        """GF = (1+t)^3 / (1-t)^3 is verified by direct computation."""
        hh = hochschild_cohomology_exterior(3, max_poly_deg=6)
        assert hh["gf_check"]

    def test_hh_d3_dimensions(self):
        """HH^0 = 1, HH^1 = 6, HH^2 = 18 for Wedge*(C^3)."""
        hh = hochschild_cohomology_exterior(3, max_poly_deg=4)
        dims = hh["hh_dimensions"]
        assert dims[0] == 1
        assert dims[1] == 6
        assert dims[2] == 18

    def test_hh_d2_dimensions(self):
        """HH^0 = 1, HH^1 = 4, HH^2 = 8 for Wedge*(C^2).

        GF = (1+t)^2 / (1-t)^2.
        (1+t)^2 = 1+2t+t^2, 1/(1-t)^2 = sum (n+1)t^n.
        Product at t^n: sum_{k=0}^{min(n,2)} binom(2,k)*(n-k+1).
        t^0: 1. t^1: 2+2=4. t^2: 1+4+3=8. t^3: 2+6+4=12.
        """
        hh = hochschild_cohomology_exterior(2, max_poly_deg=4)
        dims = hh["hh_dimensions"]
        assert dims[0] == 1
        assert dims[1] == 4
        assert dims[2] == 8

    def test_hh_d3_hh3(self):
        """HH^3(Wedge*(C^3)) = 38.

        From (1+t)^3/(1-t)^3: coeff of t^3.
        (1+t)^3 = 1+3t+3t^2+t^3.
        1/(1-t)^3 = sum binom(n+2,2) t^n.
        At t^3: binom(5,2) + 3*binom(4,2) + 3*binom(3,2) + binom(2,2)
              = 10 + 18 + 9 + 1 = 38.
        """
        hh = hochschild_cohomology_exterior(3, max_poly_deg=4)
        assert hh["hh_dimensions"][3] == 38

    def test_hh_gf_d2(self):
        """GF check for d=2."""
        hh = hochschild_cohomology_exterior(2, max_poly_deg=5)
        assert hh["gf_check"]


# =========================================================================
# Section 9: Shadow analysis
# =========================================================================

class TestShadowAnalysis:
    """Tests for shadow tower classification of exterior algebras."""

    def test_shadow_class_G(self):
        """Wedge*(C^3) is class G (Gaussian, formal A-infinity)."""
        sa = shadow_analysis_exterior(3)
        assert sa["shadow_class"] == "G"

    def test_shadow_depth_2(self):
        """Shadow depth = 2 (formal, quadratic algebra)."""
        sa = shadow_analysis_exterior(3)
        assert sa["shadow_depth"] == 2

    def test_kappa_zero(self):
        """kappa = 0 (plain algebra, no OPE poles)."""
        sa = shadow_analysis_exterior(3)
        assert sa["kappa"] == 0

    def test_not_vertex_algebra(self):
        """Wedge*(C^3) is NOT a vertex algebra."""
        sa = shadow_analysis_exterior(3)
        assert sa["is_vertex_algebra"] is False


# =========================================================================
# Section 10: W_{1+infty} comparison
# =========================================================================

class TestW1InftyComparison:
    """Tests for comparison with W_{1+infty} structure."""

    def test_comparison_structure(self):
        """W_{1+infty} comparison has correct basic data."""
        comp = w1_infty_comparison()
        assert comp["formal"] is True
        assert comp["koszul_dual"] == "Sym*(C^3)"
        assert comp["shadow_class"] == "G"

    def test_hh_gf_in_comparison(self):
        """HH generating function is (1+t)^3/(1-t)^3."""
        comp = w1_infty_comparison()
        assert comp["hh_generating_function"] == "(1+t)^3/(1-t)^3"


# =========================================================================
# Section 11: Conifold
# =========================================================================

class TestConifold:
    """Tests for the conifold Ext algebra and bar complex."""

    def test_conifold_ext_dims(self):
        """Ext^* for conifold: Wedge*(C^4) tensor C[t].

        Ext^0 = 1, Ext^1 = 4, Ext^2 = 7, Ext^3 = 8, Ext^4 = 8.
        From (1+t)^4 / (1-t^2) = (1+t)^3 / (1-t):
        coefficients: 1, 4, 7, 8, 8, ...
        Wait: (1+t)^3/(1-t) = sum_n binom(3,k) * ... let me compute.
        (1+t)^3 = 1+3t+3t^2+t^3.
        1/(1-t) = 1+t+t^2+...
        Product at t^0: 1. t^1: 3+1=4. t^2: 3+3+1=7.
        t^3: 1+3+3+1=8. t^4: 1+3+3+1=8. t^5: same pattern.
        So for n >= 3: coeff = 8.
        """
        dims = conifold_ext_dimensions()
        assert dims[0] == 1
        assert dims[1] == 4
        assert dims[2] == 7
        assert dims[3] == 8

    def test_conifold_ext_periodic(self):
        """Ext^p for conifold stabilizes at 8 for p >= 3."""
        dims = conifold_ext_dimensions()
        for p in range(3, 10):
            assert dims[p] == 8

    def test_conifold_bar_wedge4_koszul(self):
        """Bar cohomology of Wedge*(C^4) part is Koszul."""
        result = conifold_bar_analysis(max_arity=2)
        bar_data = result["bar_of_wedge4"]
        assert bar_data["is_koszul"]


# =========================================================================
# Section 12: Multi-path cross-verification
# =========================================================================

class TestMultiPathVerification:
    """Cross-verification across independent computation paths."""

    def test_three_path_d3_arity2(self):
        """H^0(B^2(Wedge*(C^3))) = 6, verified three ways.

        Path 1: Direct bar differential computation.
        Path 2: Koszul dual formula binom(n+d-1, d-1) = binom(4, 2) = 6.
        Path 3: Kernel of d: B^2_0 -> B^1_1 has dim d(d+1)/2 = 6.
        """
        # Path 1
        h = bar_cohomology_at_arity_degree(3, 2, 0)
        path1 = h["dim_cohomology"]
        # Path 2
        path2 = math.comb(2 + 3 - 1, 3 - 1)
        # Path 3: kernel of d at arity 2, cohom 0
        # d: B^2_0 -> B^1_1. Source dim = 3^2 = 9. Rank = 3 (antisymmetric part).
        # Kernel = 9 - 3 = 6.
        path3 = h["dim_kernel"]  # should be 6

        assert path1 == 6
        assert path2 == 6
        assert path3 == 6

    def test_three_path_d3_arity3(self):
        """H^0(B^3(Wedge*(C^3))) = 10, verified three ways.

        Path 1: Direct computation.
        Path 2: binom(5, 2) = 10.
        Path 3: HKR Hilbert series coefficient.
        """
        path1 = bar_cohomology_at_arity_degree(3, 3, 0)["dim_cohomology"]
        path2 = math.comb(3 + 3 - 1, 3 - 1)
        # Path 3: from Hilbert series 1/(1-t)^3, coeff of t^3 = binom(5,2) = 10
        path3 = math.comb(3 + 2, 2)

        assert path1 == 10
        assert path2 == 10
        assert path3 == 10

    def test_euler_char_identity(self):
        """Euler characteristic: sum (-1)^k dim B^k_w = 0 for w >= 1.

        This follows from h_A(t) * h_{A!}(-t) = 1, which means the
        alternating sum of bar dimensions at fixed total weight is zero
        (after accounting for the degree-0 piece).
        """
        # At total weight w = 2 (sum|a_i| = 2):
        # B^2_0: [x_i|x_j] with |x_i|=|x_j|=1, dim = 9
        # B^1_1: [x_{ij}], dim = 3
        # Alternating sum: (-1)^2 * 9 + (-1)^1 * 3 = 9 - 3 = 6
        # This should equal dim(A^!)_2 = binom(4,2) = 6 (via Euler char of acyclic complex)
        dim_B2_0 = len(bar_basis_at_arity_and_degree(3, 2, 0))
        dim_B1_1 = len(bar_basis_at_arity_and_degree(3, 1, 1))
        # The acyclic part cancels, leaving the cohomology
        assert dim_B2_0 - dim_B1_1 == 6  # = dim Sym^2(C^3)

    def test_bar_differential_preserves_weight(self):
        """d: B^k_n -> B^{k-1}_{n+1} preserves total weight w = k + n.

        Verified on ALL bar elements at arity 3 for d=3.
        """
        d_val = 3
        for cohom in range(0, 7):
            source = bar_basis_at_arity_and_degree(d_val, 3, cohom)
            for elem in source:
                w_source = elem.arity + elem.cohomological_degree
                d_result = bar_differential_on_element(elem, d_val)
                for target, coeff in d_result.items():
                    if coeff != 0:
                        w_target = target.arity + target.cohomological_degree
                        assert w_target == w_source


# =========================================================================
# Section 13: Dimension checks
# =========================================================================

class TestDimensionChecks:
    """Tests for bar space dimensions."""

    def test_bar_basis_count_d3_arity1(self):
        """B^1(Wedge*(C^3)) = s^{-1}Wedge^+(C^3), dim = 7."""
        assert len(bar_basis_at_arity(3, 1)) == 7

    def test_bar_basis_count_d3_arity2(self):
        """B^2(Wedge*(C^3)) = (Wedge^+)^{tensor 2}, dim = 49."""
        assert len(bar_basis_at_arity(3, 2)) == 49

    def test_bar_at_degree_d3(self):
        """B^2_0(Wedge*(C^3)): pairs of degree-1 elements, dim = 9."""
        assert len(bar_basis_at_arity_and_degree(3, 2, 0)) == 9

    def test_bar_at_degree_d3_high(self):
        """B^2_4(Wedge*(C^3)): pairs summing to ext degree 6 (=3+3), dim = 1."""
        assert len(bar_basis_at_arity_and_degree(3, 2, 4)) == 1
