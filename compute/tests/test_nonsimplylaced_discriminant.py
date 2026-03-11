"""Tests for non-simply-laced discriminant analysis.

Verifies conj:non-simply-laced-discriminant from the monograph:
  For non-simply-laced g (B_n, C_n, F_4, G_2), the bar cohomology GF
  P_{g-hat}(x) is algebraic with discriminant Delta_g(x) satisfying:
    (i)   Delta_g has a simple root at x = 1/dim(g)
    (ii)  DS discriminant shares the same branch locus
    (iii) For G_2: dim(g)=14, predicted growth 14^n

Ground truth from CLAUDE.md, lie_algebra.py, and manuscript:
  B_2 = so(5): dim=10, h=4, h^vee=3, rank=2, exponents=[1,3]
  G_2: dim=14, h=6, h^vee=4, rank=2, exponents=[1,5]
  B_3 = so(7): dim=21, h=6, h^vee=5, rank=3, exponents=[1,3,5]
  C_2 = sp(4): dim=10, h=4, h^vee=3, rank=2, exponents=[1,3]
  C_3 = sp(6): dim=21, h=6, h^vee=4, rank=3, exponents=[1,3,5]
  F_4: dim=52, h=12, h^vee=9, rank=4, exponents=[1,5,7,11]
"""

import math
import pytest
from sympy import Rational, Symbol, Matrix, det, eye

from compute.lib.nonsimplylaced_discriminant import (
    cartan_matrix,
    symmetrizer,
    is_symmetrizable,
    symmetrized_cartan,
    is_positive_definite,
    lacing_number,
    root_system_data,
    weyl_group_order,
    coxeter_number,
    dual_coxeter_number,
    number_of_positive_roots,
    e1_dimensions_lqt,
    e1_small_values,
    predicted_growth_rate,
    predicted_discriminant_degree,
    predicted_discriminant_roots,
    simply_laced_discriminant,
    sl2_transfer_matrix,
    verify_sl2_transfer_matrix,
    conjectured_sl3_transfer_matrix,
    verify_sl3_transfer_matrix,
    nonsimplylaced_predicted_data,
    chain_group_dimensions,
    comparison_table,
    growth_rate_comparison,
    koszul_dual_prediction_h1,
    exponent_product_formula,
    exponent_sum_formula,
    conjectured_discriminant_structure,
    e1_growth_constants,
    verify_cartan_properties,
    verify_root_system_identities,
    verify_nonsimplylaced_h_distinction,
    verify_all,
)


# ===================================================================
# Cartan matrix properties
# ===================================================================

class TestCartanMatrixProperties:
    """Cartan matrix structure: diagonal=2, off-diag<=0, symmetrizable, pos-def."""

    def test_b2_diagonal(self):
        A = cartan_matrix("B", 2)
        assert A[0, 0] == 2 and A[1, 1] == 2

    def test_g2_diagonal(self):
        A = cartan_matrix("G", 2)
        assert A[0, 0] == 2 and A[1, 1] == 2

    def test_c3_diagonal(self):
        A = cartan_matrix("C", 3)
        for i in range(3):
            assert A[i, i] == 2

    def test_f4_diagonal(self):
        A = cartan_matrix("F", 4)
        for i in range(4):
            assert A[i, i] == 2

    def test_b2_off_diagonal(self):
        A = cartan_matrix("B", 2)
        assert A[0, 1] <= 0 and A[1, 0] <= 0

    def test_g2_off_diagonal(self):
        A = cartan_matrix("G", 2)
        assert A[0, 1] == -1 and A[1, 0] == -3

    def test_b2_not_symmetric(self):
        """B_2 Cartan matrix is NOT symmetric (non-simply-laced)."""
        A = cartan_matrix("B", 2)
        assert A[0, 1] != A[1, 0]

    def test_g2_not_symmetric(self):
        """G_2 Cartan matrix is NOT symmetric."""
        A = cartan_matrix("G", 2)
        assert A[0, 1] != A[1, 0]

    def test_f4_not_symmetric(self):
        """F_4 Cartan matrix is NOT symmetric."""
        A = cartan_matrix("F", 4)
        assert A[1, 2] != A[2, 1]

    def test_a2_symmetric(self):
        """A_2 Cartan matrix IS symmetric (simply-laced)."""
        A = cartan_matrix("A", 2)
        assert A[0, 1] == A[1, 0]

    def test_d4_symmetric(self):
        """D_4 Cartan matrix IS symmetric (simply-laced)."""
        A = cartan_matrix("D", 4)
        for i in range(4):
            for j in range(4):
                assert A[i, j] == A[j, i]


class TestSymmetrizability:
    """All Cartan matrices are symmetrizable: D*A is symmetric."""

    def test_b2_symmetrizable(self):
        assert is_symmetrizable("B", 2)

    def test_b3_symmetrizable(self):
        assert is_symmetrizable("B", 3)

    def test_c2_symmetrizable(self):
        assert is_symmetrizable("C", 2)

    def test_c3_symmetrizable(self):
        assert is_symmetrizable("C", 3)

    def test_g2_symmetrizable(self):
        assert is_symmetrizable("G", 2)

    def test_f4_symmetrizable(self):
        assert is_symmetrizable("F", 4)

    def test_a2_symmetrizable(self):
        assert is_symmetrizable("A", 2)

    def test_d4_symmetrizable(self):
        assert is_symmetrizable("D", 4)


class TestSymmetrizer:
    """Symmetrizer values match root length ratios."""

    def test_b2_symmetrizer(self):
        """B_2: alpha_1 long (|a|^2=2), alpha_2 short (|a|^2=1)."""
        d = symmetrizer("B", 2)
        assert d == [2, 1]

    def test_g2_symmetrizer(self):
        """G_2: symmetrizer [3,1] (from a_{21}/a_{12} = 3)."""
        d = symmetrizer("G", 2)
        assert d == [3, 1]

    def test_c3_symmetrizer(self):
        """C_3: alpha_1,alpha_2 short, alpha_3 long."""
        d = symmetrizer("C", 3)
        assert d == [1, 1, 2]

    def test_f4_symmetrizer(self):
        """F_4: symmetrizer [1,1,2,2] (nodes 3,4 have double bond to 2)."""
        d = symmetrizer("F", 4)
        assert d == [1, 1, 2, 2]

    def test_a2_symmetrizer_trivial(self):
        """A_2 (simply-laced): all d_i = 1."""
        d = symmetrizer("A", 2)
        assert d == [1, 1]


class TestPositiveDefiniteness:
    """Symmetrized Cartan matrix D*A is positive-definite."""

    def test_b2_pos_def(self):
        DA = symmetrized_cartan("B", 2)
        assert is_positive_definite(DA)

    def test_g2_pos_def(self):
        DA = symmetrized_cartan("G", 2)
        assert is_positive_definite(DA)

    def test_c3_pos_def(self):
        DA = symmetrized_cartan("C", 3)
        assert is_positive_definite(DA)

    def test_f4_pos_def(self):
        DA = symmetrized_cartan("F", 4)
        assert is_positive_definite(DA)

    def test_symmetrized_is_symmetric_b2(self):
        DA = symmetrized_cartan("B", 2)
        assert DA[0, 1] == DA[1, 0]

    def test_symmetrized_is_symmetric_g2(self):
        DA = symmetrized_cartan("G", 2)
        assert DA[0, 1] == DA[1, 0]

    def test_symmetrized_is_symmetric_f4(self):
        DA = symmetrized_cartan("F", 4)
        for i in range(4):
            for j in range(4):
                assert DA[i, j] == DA[j, i]


# ===================================================================
# Lacing number
# ===================================================================

class TestLacingNumber:
    """Lacing number = ratio of long to short root lengths squared."""

    def test_a2_lacing_1(self):
        """Simply-laced: lacing = 1."""
        assert lacing_number("A", 2) == 1

    def test_d4_lacing_1(self):
        assert lacing_number("D", 4) == 1

    def test_b2_lacing_2(self):
        """B-type: lacing = 2."""
        assert lacing_number("B", 2) == 2

    def test_c2_lacing_2(self):
        """C-type: lacing = 2."""
        assert lacing_number("C", 2) == 2

    def test_f4_lacing_2(self):
        """F_4: lacing = 2."""
        assert lacing_number("F", 4) == 2

    def test_g2_lacing_3(self):
        """G_2: lacing = 3."""
        assert lacing_number("G", 2) == 3


# ===================================================================
# Root system data
# ===================================================================

class TestRootSystemData:
    """Root system structure: dimensions, exponents, root counts."""

    def test_b2_dim(self):
        assert root_system_data("B", 2)["dim"] == 10

    def test_g2_dim(self):
        assert root_system_data("G", 2)["dim"] == 14

    def test_b3_dim(self):
        assert root_system_data("B", 3)["dim"] == 21

    def test_c3_dim(self):
        assert root_system_data("C", 3)["dim"] == 21

    def test_f4_dim(self):
        assert root_system_data("F", 4)["dim"] == 52

    def test_b2_positive_roots(self):
        assert root_system_data("B", 2)["n_positive_roots"] == 4

    def test_g2_positive_roots(self):
        assert root_system_data("G", 2)["n_positive_roots"] == 6

    def test_f4_positive_roots(self):
        assert root_system_data("F", 4)["n_positive_roots"] == 24

    def test_b2_total_roots(self):
        assert root_system_data("B", 2)["n_total_roots"] == 8

    def test_g2_total_roots(self):
        assert root_system_data("G", 2)["n_total_roots"] == 12

    def test_b2_exponents(self):
        assert root_system_data("B", 2)["exponents"] == [1, 3]

    def test_g2_exponents(self):
        assert root_system_data("G", 2)["exponents"] == [1, 5]

    def test_f4_exponents(self):
        assert root_system_data("F", 4)["exponents"] == [1, 5, 7, 11]

    def test_b2_not_simply_laced(self):
        assert not root_system_data("B", 2)["simply_laced"]

    def test_g2_not_simply_laced(self):
        assert not root_system_data("G", 2)["simply_laced"]

    def test_a2_simply_laced(self):
        assert root_system_data("A", 2)["simply_laced"]

    def test_g2_long_short_split(self):
        """G_2 has 3 long + 3 short positive roots (6 total)."""
        data = root_system_data("G", 2)
        assert data["n_long_positive"] + data["n_short_positive"] == 6

    def test_b2_long_short_split(self):
        """B_2 has 2 long + 2 short positive roots (4 total)."""
        data = root_system_data("B", 2)
        assert data["n_long_positive"] + data["n_short_positive"] == 4


class TestCoxeterNumbers:
    """h vs h^vee distinction — critical for non-simply-laced."""

    def test_b2_h(self):
        assert coxeter_number("B", 2) == 4

    def test_b2_h_dual(self):
        assert dual_coxeter_number("B", 2) == 3

    def test_g2_h(self):
        assert coxeter_number("G", 2) == 6

    def test_g2_h_dual(self):
        assert dual_coxeter_number("G", 2) == 4

    def test_b3_h(self):
        assert coxeter_number("B", 3) == 6

    def test_b3_h_dual(self):
        assert dual_coxeter_number("B", 3) == 5

    def test_c3_h(self):
        assert coxeter_number("C", 3) == 6

    def test_c3_h_dual(self):
        assert dual_coxeter_number("C", 3) == 4

    def test_f4_h(self):
        assert coxeter_number("F", 4) == 12

    def test_f4_h_dual(self):
        assert dual_coxeter_number("F", 4) == 9

    def test_a2_h_equals_h_dual(self):
        """Simply-laced: h = h^vee."""
        assert coxeter_number("A", 2) == dual_coxeter_number("A", 2) == 3

    def test_d4_h_equals_h_dual(self):
        assert coxeter_number("D", 4) == dual_coxeter_number("D", 4) == 6


class TestExponentIdentities:
    """Standard identities: sum(m_i) = n_pos, prod(m_i+1) = |W|, max(m_i)+1 = h."""

    @pytest.mark.parametrize("type_,rank", [
        ("A", 1), ("A", 2), ("B", 2), ("B", 3),
        ("C", 2), ("C", 3), ("G", 2), ("D", 4), ("F", 4),
    ])
    def test_sum_exponents_equals_n_pos(self, type_, rank):
        assert exponent_sum_formula(type_, rank) == number_of_positive_roots(type_, rank)

    @pytest.mark.parametrize("type_,rank", [
        ("A", 1), ("A", 2), ("B", 2), ("B", 3),
        ("C", 2), ("C", 3), ("G", 2), ("D", 4), ("F", 4),
    ])
    def test_product_exponents_equals_weyl_order(self, type_, rank):
        assert exponent_product_formula(type_, rank) == weyl_group_order(type_, rank)


class TestWeylGroupOrder:
    """Weyl group orders = prod(m_i + 1)."""

    def test_a2_weyl(self):
        """|W(A_2)| = 3! = 6."""
        assert weyl_group_order("A", 2) == 6

    def test_b2_weyl(self):
        """|W(B_2)| = 2^2 * 2! = 8."""
        assert weyl_group_order("B", 2) == 8

    def test_g2_weyl(self):
        """|W(G_2)| = 12."""
        assert weyl_group_order("G", 2) == 12

    def test_d4_weyl(self):
        """|W(D_4)| = 2^3 * 4! = 192."""
        assert weyl_group_order("D", 4) == 192

    def test_f4_weyl(self):
        """|W(F_4)| = 1152."""
        assert weyl_group_order("F", 4) == 1152


# ===================================================================
# E_1 page dimensions
# ===================================================================

class TestE1Dimensions:
    """E_1 page dimensions via LQT theorem."""

    def test_e1_degree_0(self):
        """E_1^{0,0} = 1 for any algebra."""
        dims = e1_dimensions_lqt("B", 2, 10)
        assert dims[0] == 1

    def test_e1_small_degrees_b2(self):
        """B_2 has exponents [1,3], so first LQT generators at degrees 3 and 7.

        At degree 3: one generator (e=1, n=0). dim = 1.
        At degree 7: TWO generators with this degree:
          (e=1, n=2) at 2*1+1+4 = 7, and (e=3, n=0) at 2*3+1 = 7.
        dim E_1^{0,7} = 2 (pick either one).
        """
        dims = e1_dimensions_lqt("B", 2, 10)
        assert dims[3] == 1
        assert dims[7] == 2  # two generators at degree 7

    def test_e1_small_degrees_g2(self):
        """G_2 has exponents [1,5], so first LQT generators at degrees 3 and 11.

        At degree 3: one generator (e=1, n=0). dim = 1.
        At degree 11: TWO generators with this degree:
          (e=1, n=4) at 2*1+1+8 = 11, and (e=5, n=0) at 2*5+1 = 11.
        dim E_1^{0,11} = 2 (pick either one).
        """
        dims = e1_dimensions_lqt("G", 2, 12)
        assert dims[3] == 1
        assert dims[11] == 2  # two generators at degree 11

    def test_e1_sum_property(self):
        """E_1 at p=0 is always 1 (empty subset)."""
        for type_, rank in [("B", 2), ("G", 2), ("C", 3), ("F", 4)]:
            dims = e1_dimensions_lqt(type_, rank, 5)
            assert dims[0] == 1

    def test_e1_matches_lqt_module_b2(self):
        """Cross-validate with lqt_e1_growth module for B2."""
        from compute.lib.lqt_e1_growth import e1_dimensions as lqt_e1
        ours = e1_dimensions_lqt("B", 2, 30)
        theirs = lqt_e1("B2", 30)
        for p in range(31):
            assert ours[p] == theirs[p], f"Mismatch at p={p}: {ours[p]} vs {theirs[p]}"

    def test_e1_matches_lqt_module_g2(self):
        """Cross-validate with lqt_e1_growth module for G2."""
        from compute.lib.lqt_e1_growth import e1_dimensions as lqt_e1
        ours = e1_dimensions_lqt("G", 2, 30)
        theirs = lqt_e1("G2", 30)
        for p in range(31):
            assert ours[p] == theirs[p]

    def test_e1_matches_lqt_module_f4(self):
        """Cross-validate with lqt_e1_growth module for F4."""
        from compute.lib.lqt_e1_growth import e1_dimensions as lqt_e1
        ours = e1_dimensions_lqt("F", 4, 30)
        theirs = lqt_e1("F4", 30)
        for p in range(31):
            assert ours[p] == theirs[p]


# ===================================================================
# Discriminant predictions
# ===================================================================

class TestDiscriminantPredictions:
    """Predicted discriminant structure from conj:non-simply-laced-discriminant."""

    def test_b2_growth_rate(self):
        assert predicted_growth_rate("B", 2) == 10

    def test_g2_growth_rate(self):
        """Conjecture (iii): G_2 growth rate = 14^n."""
        assert predicted_growth_rate("G", 2) == 14

    def test_f4_growth_rate(self):
        assert predicted_growth_rate("F", 4) == 52

    def test_b2_discriminant_degree(self):
        """rank(B_2) + 1 = 3."""
        assert predicted_discriminant_degree("B", 2) == 3

    def test_g2_discriminant_degree(self):
        """rank(G_2) + 1 = 3."""
        assert predicted_discriminant_degree("G", 2) == 3

    def test_f4_discriminant_degree(self):
        """rank(F_4) + 1 = 5."""
        assert predicted_discriminant_degree("F", 4) == 5

    def test_c3_discriminant_degree(self):
        """rank(C_3) + 1 = 4."""
        assert predicted_discriminant_degree("C", 3) == 4

    def test_b2_growth_pole(self):
        """Growth pole at x = 1/10."""
        roots = predicted_discriminant_roots("B", 2)
        assert roots["growth_pole"] == Rational(1, 10)

    def test_g2_growth_pole(self):
        """Growth pole at x = 1/14."""
        roots = predicted_discriminant_roots("G", 2)
        assert roots["growth_pole"] == Rational(1, 14)

    def test_f4_growth_pole(self):
        """Growth pole at x = 1/52."""
        roots = predicted_discriminant_roots("F", 4)
        assert roots["growth_pole"] == Rational(1, 52)

    def test_ds_invariant_degree(self):
        """DS-invariant factor has degree = rank."""
        for type_, rank in [("B", 2), ("G", 2), ("C", 3), ("F", 4)]:
            roots = predicted_discriminant_roots(type_, rank)
            data = root_system_data(type_, rank)
            assert roots["ds_invariant_degree"] == data["rank"]


class TestSimplyLacedDiscriminant:
    """Verify known discriminants for simply-laced cases."""

    def test_sl2_discriminant_roots(self):
        disc = simply_laced_discriminant("A", 1)
        assert disc is not None
        assert set(disc["roots"]) == {Rational(1, 3), Rational(-1)}

    def test_sl2_growth_rate(self):
        disc = simply_laced_discriminant("A", 1)
        assert disc["growth_rate"] == 3

    def test_sl2_status(self):
        disc = simply_laced_discriminant("A", 1)
        assert disc["status"] == "proved"

    def test_sl3_conjectured(self):
        disc = simply_laced_discriminant("A", 2)
        assert disc is not None
        assert disc["status"] == "conjectured"
        assert disc["growth_rate"] == 8


class TestTransferMatrix:
    """Transfer matrix det(I - xT) = discriminant."""

    def test_sl2_eigenvalues(self):
        result = verify_sl2_transfer_matrix()
        assert result["eigenvalues_correct"]
        assert result["eigenvalues"] == [-1, 3]

    def test_sl2_det_equals_discriminant(self):
        result = verify_sl2_transfer_matrix()
        assert result["det_equals_discriminant"]

    def test_sl2_growth_equals_dim(self):
        result = verify_sl2_transfer_matrix()
        assert result["growth_equals_dim"]

    def test_sl3_det_equals_discriminant(self):
        result = verify_sl3_transfer_matrix()
        assert result["det_equals_discriminant"]

    def test_sl3_growth_pole(self):
        result = verify_sl3_transfer_matrix()
        assert result["growth_pole_at_1_over_8"]

    def test_sl2_transfer_2x2(self):
        """sl_2 transfer matrix is 2x2 (rank+1 = 2)."""
        T = sl2_transfer_matrix()
        assert T.rows == 2 and T.cols == 2

    def test_sl3_transfer_3x3(self):
        """sl_3 transfer matrix is 3x3 (rank+1 = 3)."""
        T = conjectured_sl3_transfer_matrix()
        assert T.rows == 3 and T.cols == 3


# ===================================================================
# Chain group dimensions
# ===================================================================

class TestChainGroupDimensions:
    """dim B-bar^n = dim(g)^n * (n-1)! — proved."""

    def test_b2_chain_dim_1(self):
        dims = chain_group_dimensions("B", 2, 3)
        assert dims[1] == 10

    def test_b2_chain_dim_2(self):
        dims = chain_group_dimensions("B", 2, 3)
        assert dims[2] == 100  # 10^2 * 1

    def test_b2_chain_dim_3(self):
        dims = chain_group_dimensions("B", 2, 3)
        assert dims[3] == 2000  # 10^3 * 2

    def test_g2_chain_dim_1(self):
        dims = chain_group_dimensions("G", 2, 3)
        assert dims[1] == 14

    def test_g2_chain_dim_2(self):
        dims = chain_group_dimensions("G", 2, 3)
        assert dims[2] == 196  # 14^2

    def test_g2_chain_dim_3(self):
        """From conj text: dim^3 * 2! = 14^3 * 2 = 5488."""
        dims = chain_group_dimensions("G", 2, 3)
        assert dims[3] == 5488

    def test_f4_chain_dim_1(self):
        dims = chain_group_dimensions("F", 4, 2)
        assert dims[1] == 52


# ===================================================================
# Koszul dual predictions
# ===================================================================

class TestKoszulDualPredictions:
    """H^1(B-bar) = dim(g) for all KM algebras."""

    @pytest.mark.parametrize("type_,rank,expected_dim", [
        ("A", 1, 3), ("A", 2, 8), ("B", 2, 10),
        ("G", 2, 14), ("C", 3, 21), ("F", 4, 52),
    ])
    def test_h1_equals_dim(self, type_, rank, expected_dim):
        assert koszul_dual_prediction_h1(type_, rank) == expected_dim


# ===================================================================
# Comparison: simply-laced vs non-simply-laced
# ===================================================================

class TestComparison:
    """Comparing properties across simply-laced and non-simply-laced types."""

    def test_comparison_table_length(self):
        table = comparison_table()
        assert len(table) == 10  # 10 types in the table

    def test_comparison_table_has_nsl(self):
        table = comparison_table()
        nsl = [r for r in table if not r["simply_laced"]]
        assert len(nsl) >= 5  # B2, B3, C2, C3, G2, F4

    def test_growth_rate_matches_dim(self):
        results = growth_rate_comparison()
        for label, data in results.items():
            assert data["matches_dim"]

    def test_sl2_growth_proved(self):
        results = growth_rate_comparison()
        assert results["A1"]["status"] == "proved"

    def test_g2_growth_predicted(self):
        results = growth_rate_comparison()
        assert results["G2"]["status"] == "predicted"


# ===================================================================
# Discriminant structure conjectures
# ===================================================================

class TestDiscriminantStructureConjectures:
    """Conjectured discriminant structure for non-simply-laced types."""

    def test_b2_structure(self):
        s = conjectured_discriminant_structure("B", 2)
        assert s["total_discriminant_degree"] == 3
        assert s["growth_pole"] == Rational(1, 10)
        assert not s["simply_laced"]

    def test_g2_structure(self):
        s = conjectured_discriminant_structure("G", 2)
        assert s["total_discriminant_degree"] == 3
        assert s["growth_pole"] == Rational(1, 14)
        assert s["coxeter_discrepancy"] == 2  # h=6, h^vee=4

    def test_f4_structure(self):
        s = conjectured_discriminant_structure("F", 4)
        assert s["total_discriminant_degree"] == 5
        assert s["coxeter_discrepancy"] == 3  # h=12, h^vee=9

    def test_c3_structure(self):
        s = conjectured_discriminant_structure("C", 3)
        assert s["total_discriminant_degree"] == 4
        assert s["coxeter_discrepancy"] == 2  # h=6, h^vee=4

    def test_a2_no_coxeter_discrepancy(self):
        s = conjectured_discriminant_structure("A", 2)
        assert s["simply_laced"]
        assert "coxeter_discrepancy" not in s


# ===================================================================
# E_1 growth constants
# ===================================================================

class TestE1GrowthConstants:
    """Growth constant C_g = pi*sqrt(r/12) for sub-exponential E_1 growth."""

    def test_rank_1_constant(self):
        consts = e1_growth_constants()
        expected = math.pi * math.sqrt(1 / 12.0)
        assert abs(consts["A1"]["C_theory"] - expected) < 1e-10

    def test_rank_2_constants_equal(self):
        """All rank-2 types have the same C_g (depends only on rank)."""
        consts = e1_growth_constants()
        rank2_types = ["A2", "B2", "C2", "G2"]
        c_values = [consts[t]["C_theory"] for t in rank2_types]
        for c in c_values:
            assert abs(c - c_values[0]) < 1e-10

    def test_rank_4_constants_equal(self):
        """D_4 and F_4 have same rank and same C_g."""
        consts = e1_growth_constants()
        assert abs(consts["D4"]["C_theory"] - consts["F4"]["C_theory"]) < 1e-10

    def test_simply_laced_flag(self):
        consts = e1_growth_constants()
        assert consts["A2"]["simply_laced"]
        assert not consts["B2"]["simply_laced"]
        assert not consts["G2"]["simply_laced"]


# ===================================================================
# Nonsimplylaced predicted data
# ===================================================================

class TestNonsimplyLacedPredictedData:
    """Predicted data for all non-simply-laced types."""

    def test_all_have_h_neq_h_dual(self):
        data = nonsimplylaced_predicted_data()
        for label, d in data.items():
            assert d["h_neq_h_dual"], f"{label} should have h != h^vee"

    def test_b2_data(self):
        data = nonsimplylaced_predicted_data()["B2"]
        assert data["dim"] == 10
        assert data["h"] == 4
        assert data["h_dual"] == 3
        assert data["predicted_growth_rate"] == 10
        assert data["predicted_discriminant_degree"] == 3

    def test_g2_data(self):
        data = nonsimplylaced_predicted_data()["G2"]
        assert data["dim"] == 14
        assert data["h"] == 6
        assert data["h_dual"] == 4
        assert data["predicted_growth_rate"] == 14

    def test_f4_data(self):
        data = nonsimplylaced_predicted_data()["F4"]
        assert data["dim"] == 52
        assert data["predicted_discriminant_degree"] == 5

    def test_chain_dim_consistency(self):
        """Chain dim at degree 1 = dim(g) for all types."""
        data = nonsimplylaced_predicted_data()
        for label, d in data.items():
            assert d["chain_dim_1"] == d["dim"]

    def test_chain_dim_2_formula(self):
        """Chain dim at degree 2 = dim(g)^2."""
        data = nonsimplylaced_predicted_data()
        for label, d in data.items():
            assert d["chain_dim_2"] == d["dim"] ** 2


# ===================================================================
# Comprehensive verification
# ===================================================================

class TestVerifyAll:
    """Run all verification checks from the module."""

    def test_all_cartan_properties_pass(self):
        results = verify_cartan_properties()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_all_root_identities_pass(self):
        results = verify_root_system_identities()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_all_h_distinction_pass(self):
        results = verify_nonsimplylaced_h_distinction()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_verify_all_pass(self):
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"


# ===================================================================
# B_2 / C_2 isomorphism
# ===================================================================

class TestB2C2Isomorphism:
    """B_2 = so(5) and C_2 = sp(4) are isomorphic: same dim, exponents, |W|."""

    def test_same_dim(self):
        assert root_system_data("B", 2)["dim"] == root_system_data("C", 2)["dim"] == 10

    def test_same_exponents(self):
        assert root_system_data("B", 2)["exponents"] == root_system_data("C", 2)["exponents"]

    def test_same_h(self):
        assert coxeter_number("B", 2) == coxeter_number("C", 2)

    def test_same_h_dual(self):
        assert dual_coxeter_number("B", 2) == dual_coxeter_number("C", 2)

    def test_same_weyl_order(self):
        assert weyl_group_order("B", 2) == weyl_group_order("C", 2)

    def test_same_predicted_growth(self):
        assert predicted_growth_rate("B", 2) == predicted_growth_rate("C", 2)

    def test_different_cartan(self):
        """But Cartan matrices differ (transpose of each other)."""
        A_B = cartan_matrix("B", 2)
        A_C = cartan_matrix("C", 2)
        assert A_B != A_C
        assert A_B == A_C.T
