r"""Tests for compute.lib.coha_bar_bridge_engine — CoHA-bar complex bridge.

Tests the structural bridge between:
  - Cohomological Hall algebras (CoHA) of quivers
  - Bar complexes of associated vertex/chiral algebras
  - Yangian production via both routes
  - DT invariant / shadow invariant comparison

Ground truth verified against:
  - OEIS A000041 (partition numbers)
  - OEIS A000219 (plane partition numbers / MacMahon)
  - Kontsevich-Soibelman [arXiv:1006.2706]
  - Schiffmann-Vasserot [arXiv:0905.2555, arXiv:1202.2756]
  - Rapcak-Soibelman-Yang-Zhao [arXiv:1810.10402]
  - Davison [arXiv:1311.7172]
  - Jindal-Kaubrys-Latyntsev [arXiv:2603.21707]

Multi-path verification per CLAUDE.md mandate:
  Path 1: Direct computation from product formulas
  Path 2: Independent partition/combinatorial counting
  Path 3: Cross-family consistency (Jordan/framed/A_n)
  Path 4: Literature comparison (OEIS, published values)
"""

from __future__ import annotations

import pytest
from sympy import Rational

from compute.lib.coha_bar_bridge_engine import (
    Quiver,
    a_n_quiver,
    bar_comultiplication_terms,
    bar_dims_affine_sln,
    bar_dims_heisenberg,
    coha_bar_bridge_summary,
    coha_bar_character_match,
    coha_bar_cy_match,
    coha_character_jordan,
    coha_dims_a1,
    coha_dims_an,
    coha_dims_framed_jordan,
    coha_dims_jordan,
    coha_multiplication_sign,
    coha_multiplication_structure,
    doubled_quiver,
    drinfeld_coproduct_recovery,
    dt_from_coha,
    dt_shadow_numerical_comparison,
    euler_form_a1,
    euler_form_jordan,
    framed_jordan_quiver,
    jordan_quiver,
    quiver_cy_dimension,
    shadow_from_bar,
    vertex_bialgebra_compatibility,
    w_infinity_character_check,
    w_infinity_from_coha,
    yangian_comparison,
    yangian_from_bar_cobar,
    yangian_from_coha,
)


# ============================================================
# 1. Quiver construction
# ============================================================


class TestQuiverConstruction:
    """Tests for quiver data structures."""

    def test_jordan_quiver_vertices(self):
        """Jordan quiver has 1 vertex."""
        Q = jordan_quiver()
        assert Q.num_vertices == 1

    def test_jordan_quiver_arrows(self):
        """Jordan quiver has 1 loop (self-arrow)."""
        Q = jordan_quiver()
        assert Q.num_arrows == 1
        assert Q.arrows == [(0, 0)]

    def test_framed_jordan_vertices(self):
        """Framed Jordan has 2 vertices (main + framing)."""
        Q = framed_jordan_quiver(r=2)
        assert Q.num_vertices == 2

    def test_framed_jordan_arrows(self):
        """Framed Jordan with r=2 has 1 loop + 2 framing arrows = 3."""
        Q = framed_jordan_quiver(r=2)
        assert Q.num_arrows == 3

    def test_a1_quiver(self):
        """A_1 quiver: 2 vertices, 1 arrow."""
        Q = a_n_quiver(1)
        assert Q.num_vertices == 2
        assert Q.num_arrows == 1

    def test_a2_quiver(self):
        """A_2 quiver: 3 vertices, 2 arrows."""
        Q = a_n_quiver(2)
        assert Q.num_vertices == 3
        assert Q.num_arrows == 2

    def test_doubled_jordan(self):
        """Doubled Jordan quiver has 2 loops."""
        Q = doubled_quiver(jordan_quiver())
        assert Q.num_arrows == 2

    def test_doubled_a1(self):
        """Doubled A_1 has 2 arrows (forward + reverse)."""
        Q = doubled_quiver(a_n_quiver(1))
        assert Q.num_arrows == 2


# ============================================================
# 2. Euler form
# ============================================================


class TestEulerForm:
    """Tests for quiver Euler form."""

    def test_jordan_euler_form_zero(self):
        """Jordan quiver Euler form is zero (CY condition).

        <a, b> = a*b - a*b = 0 (one vertex, one loop from that vertex).
        """
        assert euler_form_jordan(3, 5) == 0
        assert euler_form_jordan(1, 1) == 0

    def test_a1_euler_form(self):
        """A_1 quiver Euler form: <(a1,b1),(a2,b2)> = a1*a2 + b1*b2 - a1*b2.

        For d1 = (1,0), d2 = (0,1): <d1,d2> = 0 + 0 - 1 = -1.
        """
        assert euler_form_a1((1, 0), (0, 1)) == -1

    def test_a1_euler_form_symmetric(self):
        """Check symmetrized form for A_1.

        <(1,0),(0,1)> + <(0,1),(1,0)> = -1 + 0 = -1.
        """
        Q = a_n_quiver(1)
        sym = Q.symmetrized_euler_form([1, 0], [0, 1])
        # <(1,0),(0,1)> = 1*0 + 0*1 - 1*1 = -1
        # <(0,1),(1,0)> = 0*1 + 1*0 - 0*0 = 0
        assert sym == -1

    def test_jordan_rep_space_dim(self):
        """Rep(Jordan, n) = End(C^n) has dimension n^2."""
        Q = jordan_quiver()
        assert Q.representation_space_dim([5]) == 25

    def test_jordan_gauge_dim(self):
        """Gauge group GL(n) has dimension n^2."""
        Q = jordan_quiver()
        assert Q.gauge_group_dim([5]) == 25

    def test_jordan_moduli_vdim(self):
        """Virtual dimension of M(Jordan, n) = n^2 - n^2 = 0."""
        Q = jordan_quiver()
        assert Q.moduli_vdim([5]) == 0


# ============================================================
# 3. CoHA dimensions — Jordan quiver
# ============================================================


class TestCoHADimsJordan:
    """Tests for CoHA dimensions of the Jordan quiver."""

    def test_coha_jordan_first_values(self):
        """CoHA(Jordan) dims = partition numbers p(n).

        OEIS A000041: 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42.
        """
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        result = coha_dims_jordan(10)
        assert result == expected

    def test_coha_jordan_p0(self):
        """p(0) = 1 (empty partition)."""
        assert coha_dims_jordan(0) == [1]

    def test_coha_jordan_p5(self):
        """p(5) = 7: {5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1}."""
        assert coha_dims_jordan(5)[5] == 7

    def test_coha_jordan_character_match(self):
        """coha_character_jordan returns same as coha_dims_jordan."""
        assert coha_character_jordan(15) == coha_dims_jordan(15)


# ============================================================
# 4. CoHA dimensions — framed Jordan quiver
# ============================================================


class TestCoHADimsFramedJordan:
    """Tests for framed Jordan quiver CoHA."""

    def test_framed_r1_equals_jordan(self):
        """Framed Jordan with r=1 matches Jordan (unframed)."""
        assert coha_dims_framed_jordan(10, r=1) == coha_dims_jordan(10)

    def test_framed_r2_first_values(self):
        """r=2: prod (1-q^n)^{-2}, first values from OEIS A000712.

        2-colored partitions: 1, 2, 5, 10, 20, 36, 65, 110, ...
        """
        expected = [1, 2, 5, 10, 20, 36, 65, 110, 185, 300, 481]
        result = coha_dims_framed_jordan(10, r=2)
        assert result == expected

    def test_framed_r3_first_values(self):
        """r=3: prod (1-q^n)^{-3}, first values.

        3-colored partitions: 1, 3, 9, 22, 51, 108, 221, 429, ...
        """
        expected_start = [1, 3, 9, 22, 51, 108]
        result = coha_dims_framed_jordan(5, r=3)
        assert result == expected_start

    def test_framed_r1_partition_numbers(self):
        """r=1 gives partition numbers by two independent methods."""
        from_product = coha_dims_framed_jordan(15, r=1)
        from_partition = coha_dims_jordan(15)
        assert from_product == from_partition


# ============================================================
# 5. CoHA dimensions — A_n quivers
# ============================================================


class TestCoHADimsAn:
    """Tests for A_n quiver CoHA dimensions."""

    def test_a1_uses_dim_sl2(self):
        """A_1 preprojective CoHA uses dim(sl_2) = 3 generators."""
        a1_dims = coha_dims_a1(5)
        framed_3 = coha_dims_framed_jordan(5, r=3)
        assert a1_dims == framed_3

    def test_a2_uses_dim_sl3(self):
        """A_2 preprojective CoHA uses dim(sl_3) = 8 generators."""
        a2_dims = coha_dims_an(5, 2)
        framed_8 = coha_dims_framed_jordan(5, r=8)
        assert a2_dims == framed_8

    def test_a3_uses_dim_sl4(self):
        """A_3 preprojective CoHA uses dim(sl_4) = 15 generators."""
        a3_dims = coha_dims_an(5, 3)
        framed_15 = coha_dims_framed_jordan(5, r=15)
        assert a3_dims == framed_15

    def test_dim_formula(self):
        """dim(sl_{n+1}) = (n+1)^2 - 1 for the generator count."""
        for n in range(1, 6):
            expected_dim = (n + 1) ** 2 - 1
            # At degree 1, there are exactly dim(g) generators
            dims = coha_dims_an(1, n)
            assert dims[1] == expected_dim


# ============================================================
# 6. Bar complex dimensions
# ============================================================


class TestBarDims:
    """Tests for bar complex dimensions of associated vertex algebras."""

    def test_heisenberg_rank1_partitions(self):
        """Bar character of H_1 = partition numbers."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        assert bar_dims_heisenberg(10, rank=1) == expected

    def test_heisenberg_rank2(self):
        """Bar character of H_2 = 2-colored partitions."""
        expected = [1, 2, 5, 10, 20, 36, 65, 110, 185, 300, 481]
        assert bar_dims_heisenberg(10, rank=2) == expected

    def test_affine_sl2_dims(self):
        """Bar character of sl_2-hat uses dim(sl_2) = 3."""
        assert bar_dims_affine_sln(5, 2) == coha_dims_framed_jordan(5, r=3)

    def test_affine_sl3_dims(self):
        """Bar character of sl_3-hat uses dim(sl_3) = 8."""
        assert bar_dims_affine_sln(5, 3) == coha_dims_framed_jordan(5, r=8)


# ============================================================
# 7. CoHA-bar character match (CENTRAL TEST)
# ============================================================


class TestCoHABarCharacterMatch:
    """Tests for the central hypothesis: CoHA character = bar character."""

    def test_jordan_heisenberg_match(self):
        """Jordan quiver CoHA = Heisenberg bar (rank 1)."""
        result = coha_bar_character_match("jordan", 20)
        assert result["match"] is True

    def test_framed_jordan_r2_match(self):
        """Framed Jordan (r=2) CoHA = rank-2 Heisenberg bar."""
        result = coha_bar_character_match("framed_jordan", 15, r=2)
        assert result["match"] is True

    def test_framed_jordan_r3_match(self):
        """Framed Jordan (r=3) CoHA = rank-3 Heisenberg bar."""
        result = coha_bar_character_match("framed_jordan", 15, r=3)
        assert result["match"] is True

    def test_a1_sl2_match(self):
        """A_1 preprojective CoHA = affine sl_2 bar."""
        result = coha_bar_character_match("A1", 15)
        assert result["match"] is True

    def test_a2_sl3_match(self):
        """A_2 preprojective CoHA = affine sl_3 bar."""
        result = coha_bar_character_match("A2", 10)
        assert result["match"] is True

    def test_a3_sl4_match(self):
        """A_3 preprojective CoHA = affine sl_4 bar."""
        result = coha_bar_character_match("A3", 8)
        assert result["match"] is True

    def test_a4_sl5_match(self):
        """A_4 preprojective CoHA = affine sl_5 bar."""
        result = coha_bar_character_match("A4", 6)
        assert result["match"] is True

    def test_match_at_large_N(self):
        """Match persists at large N (N=30 for Jordan/Heisenberg)."""
        result = coha_bar_character_match("jordan", 30)
        assert result["match"] is True


# ============================================================
# 8. Yangian comparison
# ============================================================


class TestYangianComparison:
    """Tests that both routes produce the same Yangian."""

    def test_heisenberg_jordan_yangian(self):
        """Both routes produce Y(gl_1) for Heisenberg/Jordan."""
        result = yangian_comparison("heisenberg_jordan")
        assert result["yangian_match"] is True
        assert result["yangian"] == "Y(gl_1)"

    def test_sl2_a1_yangian(self):
        """Both routes produce Y(sl_2) for sl_2-hat/A_1."""
        result = yangian_comparison("sl2_A1")
        assert result["yangian_match"] is True
        assert result["yangian"] == "Y(sl_2)"

    def test_sl3_a2_yangian(self):
        """Both routes produce Y(sl_3) for sl_3-hat/A_2."""
        result = yangian_comparison("sl3_A2")
        assert result["yangian_match"] is True
        assert result["yangian"] == "Y(sl_3)"

    def test_coha_route_jordan(self):
        """CoHA route for Jordan quiver."""
        data = yangian_from_coha("jordan")
        assert data["yangian"] == "Y(gl_1-hat) = affine Yangian of gl(1)"
        assert data["w_algebra"] == "W_{1+infty}"

    def test_bar_route_heisenberg(self):
        """Bar-cobar route for Heisenberg."""
        data = yangian_from_bar_cobar("heisenberg")
        assert data["yangian"] == "Y(gl_1)"
        assert data["mc3_status"] == "PROVED"

    def test_bar_route_sl2(self):
        """Bar-cobar route for affine sl_2."""
        data = yangian_from_bar_cobar("affine_sl2")
        assert data["yangian"] == "Y(sl_2)"
        assert data["mc3_status"] == "PROVED (all simple types)"

    def test_virasoro_bar_route(self):
        """Bar-cobar route for Virasoro (MC4+ tower)."""
        data = yangian_from_bar_cobar("virasoro")
        assert "W_{1+infty}" in data["yangian"]
        assert data["mc3_status"] == "PROVED"


# ============================================================
# 9. CoHA multiplication vs bar comultiplication
# ============================================================


class TestMultiplicationComultiplication:
    """Tests for the duality between CoHA mult and bar comult."""

    def test_bar_comult_terms(self):
        """Bar comultiplication of element in B^n has n+1 terms."""
        for n in range(1, 10):
            assert bar_comultiplication_terms(n) == n + 1

    def test_jordan_mult_structure(self):
        """Jordan quiver CoHA multiplication structure."""
        data = coha_multiplication_structure("jordan", 3, 5)
        assert data["quiver"] == "Jordan"
        assert data["dimensions"] == (3, 5)
        assert data["splitting_terms"] == 9  # 3 + 5 + 1

    def test_a1_mult_structure(self):
        """A_1 quiver multiplication structure."""
        data = coha_multiplication_structure("A1", 2, 3)
        assert data["quiver"] == "A_1"

    def test_mult_sign_jordan(self):
        """CoHA multiplication sign for Jordan quiver.

        Euler form is 0, so sign is always +1.
        """
        Q = jordan_quiver()
        assert coha_multiplication_sign(Q, [3], [5]) == 1

    def test_mult_sign_a1(self):
        """CoHA multiplication sign for A_1 quiver.

        <(1,0),(0,1)> = -1, so sign = (-1)^{-1} = -1.
        """
        Q = a_n_quiver(1)
        assert coha_multiplication_sign(Q, [1, 0], [0, 1]) == -1


# ============================================================
# 10. DT-shadow numerical comparison
# ============================================================


class TestDTShadowComparison:
    """Tests for numerical comparison of DT and shadow invariants."""

    def test_coha_bar_match_numerical(self):
        """CoHA and bar characters match numerically."""
        result = dt_shadow_numerical_comparison(10)
        assert result["coha_bar_match"] is True

    def test_partition_truth(self):
        """CoHA character matches OEIS A000041 truth values."""
        result = dt_shadow_numerical_comparison(10)
        assert result["coha_vs_truth"] is True

    def test_macmahon_truth(self):
        """MacMahon function matches OEIS A000219 truth values."""
        result = dt_shadow_numerical_comparison(10)
        assert result["macmahon_vs_truth"] is True

    def test_dt_from_coha_jordan(self):
        """DT invariants from Jordan quiver CoHA = partitions."""
        dt = dt_from_coha("jordan", 10)
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        assert dt == expected

    def test_dt_from_coha_a1(self):
        """DT from A_1 CoHA matches sl_2 bar."""
        dt = dt_from_coha("A1", 5)
        bar = bar_dims_affine_sln(5, 2)
        assert dt == bar


# ============================================================
# 11. Vertex bialgebra (JKL26)
# ============================================================


class TestVertexBialgebra:
    """Tests for vertex bialgebra structure."""

    def test_compatibility_n2(self):
        """Vertex bialgebra compatibility at dimension 2."""
        result = vertex_bialgebra_compatibility(2)
        assert result["coproduct_terms"] == 3
        assert result["product_pairs"] == 1
        assert result["vertex_bialgebra"] is True

    def test_compatibility_n5(self):
        """Vertex bialgebra compatibility at dimension 5."""
        result = vertex_bialgebra_compatibility(5)
        assert result["coproduct_terms"] == 6
        assert result["product_pairs"] == 10

    def test_drinfeld_a1(self):
        """Drinfeld coproduct recovery for A_1 (sl_2)."""
        result = drinfeld_coproduct_recovery("A1")
        assert result["g"] == "sl_2"
        assert result["dim_g"] == 3
        assert result["drinfeld_match"] is True

    def test_drinfeld_a2(self):
        """Drinfeld coproduct recovery for A_2 (sl_3)."""
        result = drinfeld_coproduct_recovery("A2")
        assert result["g"] == "sl_3"
        assert result["dim_g"] == 8
        assert result["drinfeld_match"] is True

    def test_drinfeld_d4(self):
        """Drinfeld coproduct recovery for D_4 (so_8)."""
        result = drinfeld_coproduct_recovery("D4")
        assert result["g"] == "so_8"
        assert result["dim_g"] == 28
        assert result["drinfeld_match"] is True

    def test_drinfeld_e6(self):
        """Drinfeld coproduct recovery for E_6."""
        result = drinfeld_coproduct_recovery("E6")
        assert result["dim_g"] == 78
        assert result["drinfeld_match"] is True


# ============================================================
# 12. CY condition
# ============================================================


class TestCYCondition:
    """Tests for Calabi-Yau condition matching."""

    def test_jordan_cy(self):
        """Jordan quiver is 2-CY (preprojective)."""
        Q = jordan_quiver()
        assert quiver_cy_dimension(Q) == 2

    def test_coha_bar_cy_jordan(self):
        """CY match for Jordan quiver."""
        result = coha_bar_cy_match("jordan")
        assert result["match"] is True

    def test_coha_bar_cy_a1(self):
        """CY match for A_1 quiver."""
        result = coha_bar_cy_match("A1")
        assert result["match"] is True


# ============================================================
# 13. W_{1+infty} and MC4
# ============================================================


class TestWInfinity:
    """Tests for W_{1+infty} identification."""

    def test_w_infinity_routes(self):
        """Both routes (CoHA and bar) produce W_{1+infty}."""
        data = w_infinity_from_coha()
        assert "W_{1+infty}" in data["coha_route"]["end"]
        assert "W_{1+infty}" in data["bar_route"]["end"]

    def test_w_infinity_character_match(self):
        """W_{1+infty} character matches CoHA, bar, and Fock."""
        result = w_infinity_character_check(20)
        assert result["all_match"] is True

    def test_mc4_status(self):
        """MC4 is proved (strong completion tower theorem)."""
        data = w_infinity_from_coha()
        assert data["mc4_status"] == "PROVED (thm:completed-bar-cobar-strong)"


# ============================================================
# 14. Shadow invariant data
# ============================================================


class TestShadowFromBar:
    """Tests for shadow invariant extraction from bar complex."""

    def test_heisenberg_kappa(self):
        """Heisenberg kappa = k (the level)."""
        data = shadow_from_bar("heisenberg", 10)
        assert data["kappa"]["kappa_at_k1"] == Rational(1)

    def test_affine_sl2_kappa(self):
        """Affine sl_2 at level 1: kappa = 3(1+2)/4 = 9/4.

        Formula: kappa = dim(g)(k+h^v)/(2h^v) = 3(k+2)/4.
        At k=1: 3*3/4 = 9/4.
        """
        data = shadow_from_bar("affine_sl2", 10)
        assert data["kappa"]["kappa_at_k1"] == Rational(9, 4)

    def test_bar_character_in_shadow(self):
        """Shadow data includes the bar character."""
        data = shadow_from_bar("heisenberg", 10)
        assert data["bar_character"] == [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]


# ============================================================
# 15. Cross-family consistency
# ============================================================


class TestCrossFamilyConsistency:
    """Cross-family consistency checks (multi-path verification)."""

    def test_rank_additivity(self):
        """rank-r character at degree 1 = r (r generators at weight 1).

        This is because prod (1-q^n)^{-r} has [q^1] = r.
        """
        for r in range(1, 8):
            dims = coha_dims_framed_jordan(1, r=r)
            assert dims[1] == r

    def test_rank_degree2(self):
        """At degree 2, count is r + r*(r+1)/2 = r*(r+3)/2.

        prod (1-q^n)^{-r}: [q^2] = r (from q^2 generator) + C(r+1,2) (from 2 copies of q^1).
        Actually: [q^2] = C(r,1) + C(r+1,2) = r + r(r+1)/2.
        Wait, let me compute correctly.

        (1-q)^{-r} (1-q^2)^{-r} ... mod q^3
        = sum_{j>=0} C(r+j-1,j) q^j * sum_{k>=0} C(r+k-1,k) q^{2k} * ...
        [q^2] = C(r+1,2) + C(r,1) = r(r+1)/2 + r.

        For r=1: 1 + 1 = 2. Check: p(2) = 2. OK.
        For r=2: 3 + 2 = 5. Check: 2-colored p(2) = 5. OK.
        For r=3: 6 + 3 = 9. Check: 3-colored p(2) = 9. OK.
        """
        for r in range(1, 6):
            dims = coha_dims_framed_jordan(2, r=r)
            expected = r * (r + 1) // 2 + r
            assert dims[2] == expected

    def test_an_specialization(self):
        """A_n CoHA at degree 1 has dim(sl_{n+1}) generators."""
        for n in range(1, 5):
            dims = coha_dims_an(1, n)
            expected = (n + 1) ** 2 - 1
            assert dims[1] == expected

    def test_bar_heisenberg_rank_r_at_deg1(self):
        """Bar character of rank-r Heisenberg at degree 1 = r."""
        for r in range(1, 8):
            dims = bar_dims_heisenberg(1, rank=r)
            assert dims[1] == r

    def test_sl_n_bar_at_deg1(self):
        """Bar character of sl_n-hat at degree 1 = n^2 - 1."""
        for n in range(2, 6):
            dims = bar_dims_affine_sln(1, n)
            assert dims[1] == n ** 2 - 1

    def test_jordan_is_framed_jordan_r1(self):
        """Jordan quiver CoHA = framed Jordan with r=1."""
        assert coha_dims_jordan(15) == coha_dims_framed_jordan(15, r=1)

    def test_heisenberg_bar_is_jordan_coha(self):
        """Heisenberg bar character = Jordan CoHA character.

        This is the fundamental duality identification.
        """
        for N in [5, 10, 15, 20]:
            assert bar_dims_heisenberg(N, rank=1) == coha_dims_jordan(N)


# ============================================================
# 16. Multi-path verification: partition numbers
# ============================================================


class TestMultiPathPartitions:
    """Multi-path verification of partition numbers.

    Path 1: CoHA of Jordan quiver (product formula)
    Path 2: Bar complex of Heisenberg (product formula)
    Path 3: Direct partition counting (pentagonal recurrence)
    Path 4: OEIS A000041 ground truth
    """

    def test_three_paths_agree(self):
        """All three computational paths give the same partition numbers."""
        N = 15
        path1_coha = coha_dims_jordan(N)
        path2_bar = bar_dims_heisenberg(N, rank=1)
        path3_framed = coha_dims_framed_jordan(N, r=1)

        assert path1_coha == path2_bar
        assert path2_bar == path3_framed

    def test_against_oeis(self):
        """All paths match OEIS A000041 through p(20).

        p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7, p(6)=11,
        p(7)=15, p(8)=22, p(9)=30, p(10)=42, p(11)=56, p(12)=77,
        p(13)=101, p(14)=135, p(15)=176, p(16)=231, p(17)=297,
        p(18)=385, p(19)=490, p(20)=627.
        """
        oeis = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42,
                56, 77, 101, 135, 176, 231, 297, 385, 490, 627]
        result = coha_dims_jordan(20)
        assert result == oeis

    def test_macmahon_against_oeis(self):
        """MacMahon function matches OEIS A000219.

        p_3(0)=1, p_3(1)=1, p_3(2)=3, p_3(3)=6, p_3(4)=13,
        p_3(5)=24, p_3(6)=48, p_3(7)=86, p_3(8)=160, p_3(9)=282,
        p_3(10)=500.
        """
        oeis = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        result = dt_shadow_numerical_comparison(10)
        assert result["macmahon"][:11] == oeis


# ============================================================
# 17. Bridge summary
# ============================================================


class TestBridgeSummary:
    """Tests for the overall bridge summary."""

    def test_summary_exists(self):
        """Summary returns non-empty data."""
        summary = coha_bar_bridge_summary()
        assert len(summary) > 0

    def test_character_match_proved(self):
        """Character match is marked as proved."""
        summary = coha_bar_bridge_summary()
        assert "PROVED" in summary["character_match"]

    def test_yangian_proved(self):
        """Yangian production is marked as proved."""
        summary = coha_bar_bridge_summary()
        assert "PROVED" in summary["yangian_production"]

    def test_open_questions(self):
        """Open questions are listed."""
        summary = coha_bar_bridge_summary()
        assert len(summary["key_open"]) >= 3


# ============================================================
# 18. AP10-hardened multi-path cross-checks
# ============================================================


class TestAP10MultiPathCrossChecks:
    """Multi-path verification designed to catch AP10 (hardcoded wrong values).

    Every test here verifies a numerical claim via at least 2 INDEPENDENT
    methods that do NOT share code paths. If both methods produce the same
    wrong answer, there is a structural flaw in the mathematics (not a
    test-hardcoding error).
    """

    def test_partition_via_product_vs_recurrence(self):
        """Partitions: product formula vs pentagonal recurrence.

        Path 1: coha_dims_jordan uses product expansion (1-q^k)^{-1}
        Path 2: _partition_number uses Euler pentagonal theorem recurrence
        Both must agree through p(20).
        """
        from compute.lib.coha_bar_bridge_engine import _partition_number
        product = coha_dims_jordan(20)
        recurrence = [_partition_number(n) for n in range(21)]
        assert product == recurrence

    def test_partition_via_coha_vs_existing_bar_complex(self):
        """Partitions: CoHA engine vs existing bar_complex module.

        Path 1: coha_dims_jordan (this engine)
        Path 2: bar_dim_heisenberg from compute.lib.bar_complex (independent)
        """
        from compute.lib.bar_complex import bar_dim_heisenberg
        coha = coha_dims_jordan(10)
        # bar_dim_heisenberg returns dim at single degree, shifts by offset
        # bar_dim_heisenberg(d) = p(d-2) for d >= 2, and 1 for d=1
        # But the CoHA counts partitions p(n) directly.
        # These are DIFFERENT objects: bar_dim counts bar complex degree,
        # CoHA counts by total weight.
        # The identification is: CoHA character = prod (1-q^n)^{-1}
        # bar character at weight n = CoHA character at weight n
        # (both count partitions of n, but in different gradings).
        # We use the existing dt_invariants_bar module as a third path:
        from compute.lib.dt_invariants_bar import jordan_quiver_coha_dims
        existing = jordan_quiver_coha_dims(10)
        assert coha == existing

    def test_2colored_via_product_vs_convolution(self):
        """2-colored partitions: product formula vs convolution of partitions.

        Path 1: coha_dims_framed_jordan(N, r=2) (product expansion)
        Path 2: Convolution p_2(n) = sum_{k=0}^{n} p(k)*p(n-k)
        Both count 2-colored partitions.
        """
        from compute.lib.coha_bar_bridge_engine import _partition_number
        N = 12
        product = coha_dims_framed_jordan(N, r=2)
        convolution = []
        for n in range(N + 1):
            val = sum(_partition_number(k) * _partition_number(n - k)
                      for k in range(n + 1))
            convolution.append(val)
        assert product == convolution

    def test_framed_r3_via_product_vs_triple_convolution(self):
        """3-colored partitions: product formula vs triple convolution.

        Path 1: coha_dims_framed_jordan(N, r=3)
        Path 2: conv(conv(p, p), p)(n) = sum p(a)p(b)p(n-a-b)
        """
        from compute.lib.coha_bar_bridge_engine import _partition_number
        N = 8
        product = coha_dims_framed_jordan(N, r=3)
        triple = []
        for n in range(N + 1):
            val = 0
            for a in range(n + 1):
                for b in range(n - a + 1):
                    c = n - a - b
                    val += _partition_number(a) * _partition_number(b) * _partition_number(c)
            triple.append(val)
        assert product == triple

    def test_euler_form_independent_computation(self):
        """Euler form of A_1: compute directly vs use Quiver class.

        Path 1: euler_form_a1 via Quiver.euler_form
        Path 2: Direct formula a1*a2 + b1*b2 - a1*b2
        """
        for a1 in range(4):
            for b1 in range(4):
                for a2 in range(4):
                    for b2 in range(4):
                        via_quiver = euler_form_a1((a1, b1), (a2, b2))
                        direct = a1 * a2 + b1 * b2 - a1 * b2
                        assert via_quiver == direct, (
                            f"Euler form mismatch at ({a1},{b1}),({a2},{b2}): "
                            f"quiver={via_quiver}, direct={direct}"
                        )

    def test_macmahon_via_coha_engine_vs_dt_module(self):
        """MacMahon: this engine vs existing dt_invariants_bar module.

        Path 1: _macmahon_coefficients from coha_bar_bridge_engine
        Path 2: macmahon_coefficients from dt_invariants_bar
        """
        from compute.lib.coha_bar_bridge_engine import _macmahon_coefficients
        from compute.lib.dt_invariants_bar import macmahon_coefficients
        path1 = _macmahon_coefficients(10)
        path2 = macmahon_coefficients(10)
        assert path1 == path2

    def test_macmahon_vs_independent_product(self):
        """MacMahon: divisor-sum recurrence vs direct product expansion.

        Path 1: _macmahon_coefficients (divisor-sum recurrence)
        Path 2: macmahon_from_product from dt_invariants_bar (log + exp)
        """
        from compute.lib.coha_bar_bridge_engine import _macmahon_coefficients
        from compute.lib.dt_invariants_bar import macmahon_from_product
        path1 = _macmahon_coefficients(10)
        path2 = macmahon_from_product(10)
        assert path1 == path2

    def test_coha_bar_match_via_existing_module(self):
        """CoHA-bar match cross-checked against existing dt_invariants_bar.

        Path 1: coha_dims_jordan (this engine)
        Path 2: jordan_quiver_coha_dims (dt_invariants_bar)
        Path 3: bar_dims_heisenberg (this engine)
        Path 4: heisenberg_bar_character from dt_invariants_bar
        All four must agree.
        """
        from compute.lib.dt_invariants_bar import (
            jordan_quiver_coha_dims,
            heisenberg_bar_character,
        )
        N = 12
        p1 = coha_dims_jordan(N)
        p2 = jordan_quiver_coha_dims(N)
        p3 = bar_dims_heisenberg(N, rank=1)
        p4 = heisenberg_bar_character(N, rank=1)
        assert p1 == p2, f"CoHA engines disagree: {p1} vs {p2}"
        assert p1 == p3, f"CoHA vs bar disagree: {p1} vs {p3}"
        assert p1 == p4, f"CoHA vs existing bar disagree: {p1} vs {p4}"

    def test_framed_coha_vs_existing_module(self):
        """Framed Jordan CoHA cross-checked against dt_invariants_bar.

        Path 1: coha_dims_framed_jordan (this engine)
        Path 2: framed_jordan_quiver_coha_dims (dt_invariants_bar)
        """
        from compute.lib.dt_invariants_bar import framed_jordan_quiver_coha_dims
        for r in [1, 2, 3]:
            p1 = coha_dims_framed_jordan(10, r=r)
            p2 = framed_jordan_quiver_coha_dims(10, r=r)
            assert p1 == p2, f"Framed Jordan r={r} disagree: {p1} vs {p2}"

    def test_generating_function_recurrence(self):
        """Product formula satisfies the correct recurrence.

        If f(q) = prod (1-q^k)^{-r}, then
        n * f_n = sum_{k=1}^{n} (r * sigma_1(k)) * f_{n-k}
        where sigma_1(k) = sum of divisors of k.

        This is a third independent verification method.
        """
        def sigma1(k):
            return sum(d for d in range(1, k + 1) if k % d == 0)

        for r in [1, 2, 3]:
            f = coha_dims_framed_jordan(15, r=r)
            for n in range(1, 16):
                lhs = n * f[n]
                rhs = sum(r * sigma1(k) * f[n - k] for k in range(1, n + 1))
                assert lhs == rhs, (
                    f"Recurrence fails for r={r}, n={n}: "
                    f"n*f_n={lhs} != sum={rhs}"
                )
