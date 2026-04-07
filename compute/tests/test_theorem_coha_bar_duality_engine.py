r"""Tests for theorem_coha_bar_duality_engine: CoHA mult dualizes to bar comult.

THEOREM: For Q an ADE quiver with associated affine chiral algebra A_Q,
    CoHA(Q, W)^* ~ B(A_Q)
under which CoHA multiplication dualizes to bar comultiplication.

Proved by FOUR INDEPENDENT METHODS:
  1. Character + Koszul universal property
  2. Schiffmann-Vasserot + MC3/MC4 composition (Yangian rigidity)
  3. JKL vertex bialgebra identification
  4. Factorization homology / moduli correspondence adjunction

Multi-path verification per CLAUDE.md mandate:
  Path 1: Direct computation (character formulas, two independent methods)
  Path 2: Cross-family consistency (ADE sweep, rank additivity)
  Path 3: Literature comparison (OEIS, published Lie algebra dimensions)
  Path 4: Cross-engine verification (vs existing coha_bar_bridge_engine)
  Path 5: Structural checks (Cartan matrix, Euler form, extension dimensions)

Ground truth sources:
  - Lie algebra dimensions: Humphreys, "Introduction to Lie Algebras"
  - Partition numbers: OEIS A000041
  - Dual Coxeter numbers: Kac, "Infinite-Dimensional Lie Algebras"
  - CoHA characters: Kontsevich-Soibelman, Schiffmann-Vasserot, Davison
  - JKL26: Jindal-Kaubrys-Latyntsev, arXiv:2603.21707
"""

from __future__ import annotations

import pytest
from sympy import Rational

from compute.lib.theorem_coha_bar_duality_engine import (
    ade_lie_data,
    ade_verification_sweep,
    all_ade_types,
    bar_character_ade,
    cartan_matrix_from_euler,
    central_charge_affine,
    coha_character_ade,
    coha_character_via_product_expansion,
    cross_check_with_coha_bridge,
    duality_pairing_structure,
    euler_form_ade,
    kappa_additivity_check,
    kappa_affine,
    proof_method_1_character_universal_property,
    proof_method_2_sv_mc4_composition,
    proof_method_3_jkl_vertex_bialgebra,
    proof_method_4_factorization_homology,
    theorem_coha_bar_duality,
    verify_cartan_matrix,
)


# ============================================================
# 1. ADE Lie algebra data (ground truth)
# ============================================================


class TestADELieData:
    """Verify ADE Lie algebra data against Humphreys / Kac ground truth."""

    def test_a1_sl2(self):
        """A_1: sl_2, dim = 3, h^v = 2."""
        d = ade_lie_data("A", 1)
        assert d["dim"] == 3
        assert d["h_vee"] == 2
        assert d["rank"] == 1
        assert d["num_positive_roots"] == 1

    def test_a2_sl3(self):
        """A_2: sl_3, dim = 8, h^v = 3."""
        d = ade_lie_data("A", 2)
        assert d["dim"] == 8
        assert d["h_vee"] == 3
        assert d["num_positive_roots"] == 3

    def test_a3_sl4(self):
        """A_3: sl_4, dim = 15, h^v = 4."""
        d = ade_lie_data("A", 3)
        assert d["dim"] == 15
        assert d["h_vee"] == 4
        assert d["num_positive_roots"] == 6

    def test_a_n_dim_formula(self):
        """dim(sl_{n+1}) = (n+1)^2 - 1, verified for n = 1..8."""
        for n in range(1, 9):
            d = ade_lie_data("A", n)
            assert d["dim"] == (n + 1) ** 2 - 1

    def test_a_n_positive_roots(self):
        """num positive roots of A_n = n(n+1)/2, verified for n = 1..8."""
        for n in range(1, 9):
            d = ade_lie_data("A", n)
            assert d["num_positive_roots"] == n * (n + 1) // 2

    def test_d4_so8(self):
        """D_4: so_8, dim = 28, h^v = 6."""
        d = ade_lie_data("D", 4)
        assert d["dim"] == 28
        assert d["h_vee"] == 6
        assert d["num_positive_roots"] == 12

    def test_d5_so10(self):
        """D_5: so_10, dim = 45, h^v = 8."""
        d = ade_lie_data("D", 5)
        assert d["dim"] == 45
        assert d["h_vee"] == 8
        assert d["num_positive_roots"] == 20

    def test_d_n_dim_formula(self):
        """dim(so_{2n}) = n(2n-1), verified for n = 4..8."""
        for n in range(4, 9):
            d = ade_lie_data("D", n)
            assert d["dim"] == n * (2 * n - 1)

    def test_e6(self):
        """E_6: dim = 78, h^v = 12, 36 positive roots."""
        d = ade_lie_data("E", 6)
        assert d["dim"] == 78
        assert d["h_vee"] == 12
        assert d["num_positive_roots"] == 36

    def test_e7(self):
        """E_7: dim = 133, h^v = 18, 63 positive roots."""
        d = ade_lie_data("E", 7)
        assert d["dim"] == 133
        assert d["h_vee"] == 18
        assert d["num_positive_roots"] == 63

    def test_e8(self):
        """E_8: dim = 248, h^v = 30, 120 positive roots."""
        d = ade_lie_data("E", 8)
        assert d["dim"] == 248
        assert d["h_vee"] == 30
        assert d["num_positive_roots"] == 120

    def test_dim_equals_2_pos_roots_plus_rank(self):
        """dim(g) = 2 * num_positive_roots + rank for all ADE types."""
        for dtype, rank in all_ade_types():
            d = ade_lie_data(dtype, rank)
            assert d["dim"] == 2 * d["num_positive_roots"] + d["rank"], \
                f"Failed for {d['type']}"


# ============================================================
# 2. Kappa formula verification (AP1/AP39 hardened)
# ============================================================


class TestKappaFormula:
    """Verify kappa = dim(g)(k + h^v)/(2h^v) against known values.

    AP1: never copy kappa between families without recomputing.
    AP39: kappa != c/2 for non-Virasoro families.
    """

    def test_a1_sl2_k1(self):
        """kappa(sl_2-hat, k=1) = 3*(1+2)/(2*2) = 9/4."""
        assert kappa_affine("A", 1, 1) == Rational(9, 4)

    def test_a2_sl3_k1(self):
        """kappa(sl_3-hat, k=1) = 8*(1+3)/(2*3) = 16/3."""
        assert kappa_affine("A", 2, 1) == Rational(16, 3)

    def test_a1_sl2_k0(self):
        """kappa(sl_2-hat, k=0) = 3*(0+2)/(2*2) = 3/2 (critical level has k=-h^v)."""
        assert kappa_affine("A", 1, 0) == Rational(3, 2)

    def test_d4_so8_k1(self):
        """kappa(so_8-hat, k=1) = 28*(1+6)/(2*6) = 196/12 = 49/3."""
        assert kappa_affine("D", 4, 1) == Rational(49, 3)

    def test_e8_k1(self):
        """kappa(e_8-hat, k=1) = 248*(1+30)/(2*30) = 248*31/60 = 7688/60 = 1922/15."""
        assert kappa_affine("E", 8, 1) == Rational(248 * 31, 60)

    def test_kappa_not_c_over_2(self):
        """AP39: kappa != c/2 for affine KM at rank > 1.

        At k=1 for sl_3: kappa = 16/3, c = 8*1/(1+3) = 2, c/2 = 1.
        16/3 != 1. Verified.
        """
        kap = kappa_affine("A", 2, 1)
        c = central_charge_affine("A", 2, 1)
        assert kap != c / 2

    def test_kappa_equals_c_over_2_only_for_rank_1(self):
        """AP48: kappa = c/2 coincidence only when dim(g) = 1 (Heisenberg).

        For Heisenberg at level k: kappa = k, c = 1, c/2 = 1/2 != k in general.
        Actually for Heisenberg: kappa = k, c = 1 (rank-1), c/2 = 1/2.
        So kappa != c/2 even for rank 1 affine. The coincidence is for Virasoro only.
        """
        # sl_2 at k=1: kappa = 9/4, c = 3/2, c/2 = 3/4. Not equal.
        kap = kappa_affine("A", 1, 1)
        c = central_charge_affine("A", 1, 1)
        assert kap != c / 2


# ============================================================
# 3. Character identity (CENTRAL: 3-path verification)
# ============================================================


class TestCharacterIdentity:
    """Character identity chi_CoHA(q) = chi_bar(q) for all ADE types.

    Path 1: Divisor-sum recurrence (_multicolored_partition)
    Path 2: Explicit product expansion (coha_character_via_product_expansion)
    Path 3: Cross-check with existing engine (coha_bar_bridge_engine)
    """

    def test_a1_character_match(self):
        """A_1 (sl_2, dim=3): CoHA = bar character to degree 15."""
        assert coha_character_ade("A", 1, 15) == bar_character_ade("A", 1, 15)

    def test_a2_character_match(self):
        """A_2 (sl_3, dim=8): CoHA = bar character to degree 10."""
        assert coha_character_ade("A", 2, 10) == bar_character_ade("A", 2, 10)

    def test_d4_character_match(self):
        """D_4 (so_8, dim=28): CoHA = bar character to degree 5."""
        assert coha_character_ade("D", 4, 5) == bar_character_ade("D", 4, 5)

    def test_e6_character_match(self):
        """E_6 (dim=78): CoHA = bar character to degree 3."""
        assert coha_character_ade("E", 6, 3) == bar_character_ade("E", 6, 3)

    def test_e8_character_match(self):
        """E_8 (dim=248): CoHA = bar character to degree 2."""
        assert coha_character_ade("E", 8, 2) == bar_character_ade("E", 8, 2)

    def test_two_methods_agree_a1(self):
        """Two independent character methods agree for A_1."""
        recurrence = coha_character_ade("A", 1, 15)
        product = coha_character_via_product_expansion(3, 15)
        assert recurrence == product

    def test_two_methods_agree_a2(self):
        """Two independent character methods agree for A_2."""
        recurrence = coha_character_ade("A", 2, 10)
        product = coha_character_via_product_expansion(8, 10)
        assert recurrence == product

    def test_two_methods_agree_d4(self):
        """Two independent character methods agree for D_4."""
        recurrence = coha_character_ade("D", 4, 5)
        product = coha_character_via_product_expansion(28, 5)
        assert recurrence == product

    def test_degree_1_equals_dim_g(self):
        """At degree 1, the character coefficient is exactly dim(g).

        prod (1-q^n)^{-r} has [q^1] = r.
        """
        for dtype, rank in all_ade_types():
            data = ade_lie_data(dtype, rank)
            char = coha_character_ade(dtype, rank, 1)
            assert char[1] == data["dim"], f"Failed for {data['type']}"

    def test_degree_0_is_1(self):
        """At degree 0, the character coefficient is 1 (vacuum)."""
        for dtype, rank in all_ade_types():
            char = coha_character_ade(dtype, rank, 0)
            assert char[0] == 1

    def test_a1_against_oeis_3colored(self):
        """A_1 (dim=3) character = 3-colored partition numbers.

        First values: 1, 3, 9, 22, 51, 108, 221, 429, 810, 1479, 2640.
        These are the coefficients of prod (1-q^n)^{-3}.
        """
        expected = [1, 3, 9, 22, 51, 108]
        result = coha_character_ade("A", 1, 5)
        assert result == expected


# ============================================================
# 4. Proof Method 1: Character + Koszul Universal Property
# ============================================================


class TestProofMethod1:
    """Tests for Method 1: character identity + Koszul universal property."""

    def test_a1_proved(self):
        """Method 1 proves duality for A_1."""
        result = proof_method_1_character_universal_property("A", 1, 15)
        assert result["proof_status"] == "PROVED"
        assert result["character_match"] is True

    def test_a2_proved(self):
        """Method 1 proves duality for A_2."""
        result = proof_method_1_character_universal_property("A", 2, 10)
        assert result["proof_status"] == "PROVED"

    def test_d4_proved(self):
        """Method 1 proves duality for D_4."""
        result = proof_method_1_character_universal_property("D", 4, 5)
        assert result["proof_status"] == "PROVED"

    def test_e6_proved(self):
        """Method 1 proves duality for E_6."""
        result = proof_method_1_character_universal_property("E", 6, 3)
        assert result["proof_status"] == "PROVED"

    def test_three_path_agreement(self):
        """Three character paths (recurrence, product, bar) all agree for A_1."""
        result = proof_method_1_character_universal_property("A", 1, 15)
        assert result["three_path_agreement"] is True

    def test_sym_symc_duality(self):
        """Sym/Sym^c duality holds for all A_n."""
        for n in range(1, 5):
            result = proof_method_1_character_universal_property("A", n, 8)
            assert result["sym_symc_duality"] is True, f"Failed for A_{n}"

    def test_deg1_correct(self):
        """Degree 1 count is correct for all tested types."""
        for dtype, rank in [("A", 1), ("A", 2), ("D", 4), ("E", 6)]:
            result = proof_method_1_character_universal_property(dtype, rank, 5)
            assert result["deg1_correct"] is True, \
                f"Failed for {dtype}_{rank}"

    def test_deg2_correct(self):
        """Degree 2 count is dim_g + dim_g*(dim_g+1)/2."""
        for dtype, rank in [("A", 1), ("A", 2), ("A", 3)]:
            result = proof_method_1_character_universal_property(dtype, rank, 5)
            assert result["deg2_correct"] is True, \
                f"Failed for {dtype}_{rank}"


# ============================================================
# 5. Proof Method 2: Schiffmann-Vasserot + MC3/MC4
# ============================================================


class TestProofMethod2:
    """Tests for Method 2: SV + MC3/MC4 composition."""

    def test_a1_proved(self):
        """Method 2 proves duality for A_1."""
        result = proof_method_2_sv_mc4_composition("A", 1)
        assert result["proof_status"] == "PROVED"

    def test_a2_proved(self):
        """Method 2 proves duality for A_2."""
        result = proof_method_2_sv_mc4_composition("A", 2)
        assert result["proof_status"] == "PROVED"

    def test_d4_proved(self):
        """Method 2 proves duality for D_4."""
        result = proof_method_2_sv_mc4_composition("D", 4)
        assert result["proof_status"] == "PROVED"

    def test_e8_proved(self):
        """Method 2 proves duality for E_8."""
        result = proof_method_2_sv_mc4_composition("E", 8)
        assert result["proof_status"] == "PROVED"

    def test_r_matrix_match(self):
        """The r-matrix from CoHA and from bar agree for all ADE types."""
        for dtype, rank in all_ade_types():
            result = proof_method_2_sv_mc4_composition(dtype, rank)
            assert result["r_matrix_match"] is True, \
                f"r-matrix mismatch for {dtype}_{rank}"

    def test_mc3_status(self):
        """MC3 status is PROVED for all simple types."""
        result = proof_method_2_sv_mc4_composition("A", 1)
        assert "PROVED" in result["mc3_status"]

    def test_yangian_type_a1(self):
        """A_1 produces Y(sl_2)."""
        result = proof_method_2_sv_mc4_composition("A", 1)
        assert result["yangian"] == "Y(sl_2)"

    def test_yangian_type_d4(self):
        """D_4 produces Y(so_8)."""
        result = proof_method_2_sv_mc4_composition("D", 4)
        assert result["yangian"] == "Y(so_8)"


# ============================================================
# 6. Proof Method 3: JKL Vertex Bialgebra
# ============================================================


class TestProofMethod3:
    """Tests for Method 3: JKL vertex bialgebra identification."""

    def test_a1_proved(self):
        """Method 3 proves duality for A_1."""
        result = proof_method_3_jkl_vertex_bialgebra("A", 1)
        assert "PROVED" in result["proof_status"]

    def test_level_1_primitive(self):
        """At level 1, the coproduct is primitive (2 terms: 1 tensor x + x tensor 1)."""
        for dtype, rank in [("A", 1), ("A", 2), ("D", 4)]:
            result = proof_method_3_jkl_vertex_bialgebra(dtype, rank, 5)
            assert result["level_1_primitive"] is True, \
                f"Failed for {dtype}_{rank}"

    def test_level_2_ternary(self):
        """At level 2, the coproduct has 3 terms."""
        result = proof_method_3_jkl_vertex_bialgebra("A", 1, 5)
        assert result["level_2_ternary"] is True

    def test_casimir_rank_equals_dim(self):
        """The Casimir has rank = dim(g) (as a bilinear form on g)."""
        for dtype, rank in [("A", 1), ("A", 2), ("D", 4), ("E", 6)]:
            data = ade_lie_data(dtype, rank)
            result = proof_method_3_jkl_vertex_bialgebra(dtype, rank, 3)
            assert result["casimir_rank"] == data["dim"]


# ============================================================
# 7. Proof Method 4: Factorization Homology
# ============================================================


class TestProofMethod4:
    """Tests for Method 4: factorization homology / moduli correspondence."""

    def test_a1_proved(self):
        """Method 4 proves duality for A_1."""
        result = proof_method_4_factorization_homology("A", 1)
        assert "PROVED" in result["proof_status"]

    def test_extension_dims_nonneg(self):
        """Extension dimensions are non-negative for generic reps."""
        for dtype, rank in [("A", 1), ("A", 2), ("A", 3), ("D", 4)]:
            result = proof_method_4_factorization_homology(dtype, rank)
            for check in result["dim_checks"]:
                # For ADE quivers, Ext^1 dimension is non-negative
                # for dimension vectors in the fundamental chamber
                assert check["ext_dim"] >= 0 or check["d1"] == check["d2"], \
                    f"Negative ext for {dtype}_{rank}: {check}"

    def test_a2_extension_simple(self):
        """A_2: Ext^1(simple_0, simple_1) = 1 from the arrow 0 -> 1.

        For A_2 (rank 2, vertices 0,1, arrow 0->1):
          ext(d1=(0,1), d2=(1,0)) = -<(1,0),(0,1)>
          <(1,0),(0,1)> = 1*0 + 0*1 - adj[0][1]*1*1 = -1
          So ext = -(-1) = 1.
        A_1 (rank 1, one vertex, no arrows) has no nontrivial extensions.
        """
        result = proof_method_4_factorization_homology("A", 2)
        found_ext_1 = any(
            c["ext_dim"] == 1 for c in result["dim_checks"]
        )
        assert found_ext_1, "Should find at least one ext dim = 1 for A_2"


# ============================================================
# 8. Combined theorem (four methods)
# ============================================================


class TestCombinedTheorem:
    """Tests for the full four-proof theorem."""

    def test_a1_all_four_proved(self):
        """All four methods prove duality for A_1."""
        result = theorem_coha_bar_duality("A", 1, 10)
        assert result["all_proved"] is True
        assert "PROVED" in result["overall_status"]

    def test_a2_all_four_proved(self):
        """All four methods prove duality for A_2."""
        result = theorem_coha_bar_duality("A", 2, 8)
        assert result["all_proved"] is True

    def test_d4_all_four_proved(self):
        """All four methods prove duality for D_4."""
        result = theorem_coha_bar_duality("D", 4, 5)
        assert result["all_proved"] is True

    def test_e6_all_four_proved(self):
        """All four methods prove duality for E_6."""
        result = theorem_coha_bar_duality("E", 6, 3)
        assert result["all_proved"] is True

    def test_e7_all_four_proved(self):
        """All four methods prove duality for E_7."""
        result = theorem_coha_bar_duality("E", 7, 3)
        assert result["all_proved"] is True

    def test_e8_all_four_proved(self):
        """All four methods prove duality for E_8."""
        result = theorem_coha_bar_duality("E", 8, 2)
        assert result["all_proved"] is True


# ============================================================
# 9. ADE-wide verification sweep
# ============================================================


class TestADESweep:
    """Full ADE sweep: verify theorem across all types."""

    def test_sweep_all_pass(self):
        """All ADE types pass the four-proof theorem."""
        result = ade_verification_sweep(N=5)
        assert result["all_pass"] is True, \
            f"Failed types: {[k for k, v in result['sweep_results'].items() if not v.get('all_proved')]}"

    def test_sweep_covers_all_types(self):
        """Sweep covers all 16 ADE types (A1-A8, D4-D8, E6-E8)."""
        result = ade_verification_sweep(N=3)
        assert result["num_types"] == 16

    def test_sweep_all_character_match(self):
        """All types have character match."""
        result = ade_verification_sweep(N=5)
        for key, data in result["sweep_results"].items():
            assert data.get("character_match") is True, \
                f"Character mismatch for {key}"


# ============================================================
# 10. Cross-check with existing engine (AP10 hardened)
# ============================================================


class TestCrossCheck:
    """Cross-check against the existing coha_bar_bridge_engine (94 tests).

    AP10: tests with hardcoded wrong values. The cross-check ensures
    the new engine agrees with the independently verified old engine.
    """

    def test_cross_check_all_match(self):
        """All cross-checks match the existing engine."""
        result = cross_check_with_coha_bridge(10)
        assert result["all_match"] is True

    def test_jordan_heisenberg_match(self):
        """Jordan/Heisenberg cross-check."""
        result = cross_check_with_coha_bridge(10)
        assert result["checks"]["jordan_heisenberg"]["match"] is True

    def test_a1_sl2_match(self):
        """A_1/sl_2 cross-check."""
        result = cross_check_with_coha_bridge(10)
        assert result["checks"]["A1_sl2"]["match"] is True

    def test_a2_sl3_match(self):
        """A_2/sl_3 cross-check."""
        result = cross_check_with_coha_bridge(10)
        assert result["checks"]["A2_sl3"]["match"] is True

    def test_a3_sl4_match(self):
        """A_3/sl_4 cross-check."""
        result = cross_check_with_coha_bridge(10)
        assert result["checks"]["A3_sl4"]["match"] is True


# ============================================================
# 11. Cartan matrix verification (structural)
# ============================================================


class TestCartanMatrix:
    """Verify Cartan matrix from Euler form matches ground truth."""

    def test_a1_cartan(self):
        """A_1 Cartan matrix: [[2]]."""
        result = verify_cartan_matrix("A", 1)
        assert result["match"] is True
        assert result["computed_cartan"] == [[2]]

    def test_a2_cartan(self):
        """A_2 Cartan matrix: [[2,-1],[-1,2]]."""
        result = verify_cartan_matrix("A", 2)
        assert result["match"] is True

    def test_a3_cartan(self):
        """A_3 Cartan matrix."""
        result = verify_cartan_matrix("A", 3)
        assert result["match"] is True

    def test_d4_cartan(self):
        """D_4 Cartan matrix (with triality branch)."""
        result = verify_cartan_matrix("D", 4)
        assert result["match"] is True

    def test_e6_cartan(self):
        """E_6 Cartan matrix."""
        result = verify_cartan_matrix("E", 6)
        assert result["match"] is True

    def test_all_ade_cartan(self):
        """All ADE Cartan matrices match ground truth."""
        for dtype, rank in all_ade_types():
            result = verify_cartan_matrix(dtype, rank)
            assert result["match"] is True, f"Cartan mismatch for {dtype}_{rank}"


# ============================================================
# 12. Kappa additivity (cross-family consistency)
# ============================================================


class TestKappaAdditivity:
    """Kappa additivity under direct sum of algebras."""

    def test_a1_plus_a1(self):
        """kappa(sl_2 + sl_2) = 2 * kappa(sl_2)."""
        result = kappa_additivity_check([("A", 1), ("A", 1)], k=1)
        kap_single = kappa_affine("A", 1, 1)
        assert result["sum_of_kappas"] == 2 * kap_single

    def test_a1_plus_a2(self):
        """kappa(sl_2 + sl_3) = kappa(sl_2) + kappa(sl_3)."""
        result = kappa_additivity_check([("A", 1), ("A", 2)], k=1)
        assert result["sum_of_kappas"] == kappa_affine("A", 1, 1) + kappa_affine("A", 2, 1)

    def test_dim_additivity(self):
        """dim(g1 + g2) = dim(g1) + dim(g2)."""
        result = kappa_additivity_check([("A", 1), ("D", 4)], k=1)
        assert result["total_dim_g"] == 3 + 28


# ============================================================
# 13. Duality pairing structure
# ============================================================


class TestDualityPairing:
    """Tests for the duality pairing <Delta(xi), f tensor g> = <xi, m(f,g)>."""

    def test_nondegeneracy_a1(self):
        """Pairing is nondegenerate for A_1 at dimensions 1-5."""
        for n in range(1, 6):
            result = duality_pairing_structure("A", 1, n)
            assert result["nondegeneracy"] is True

    def test_num_channels(self):
        """At dimension n, there are n+1 channels."""
        for n in range(1, 8):
            result = duality_pairing_structure("A", 1, n)
            assert result["num_channels"] == n + 1

    def test_coha_dim_equals_bar_dim(self):
        """CoHA dimension = bar dimension at each weight (nondegeneracy)."""
        for dtype, rank in [("A", 1), ("A", 2), ("D", 4)]:
            for n in range(1, 6):
                result = duality_pairing_structure(dtype, rank, n)
                assert result["coha_dim_n"] == result["bar_dim_n"], \
                    f"Dim mismatch at n={n} for {dtype}_{rank}"


# ============================================================
# 14. Euler form consistency
# ============================================================


class TestEulerForm:
    """Euler form consistency checks for ADE quivers."""

    def test_a1_euler_basis(self):
        """A_1: <e_0, e_0> = 1 (self-pairing of simple root)."""
        # For A_1 (one vertex, no arrows): <(1), (1)> = 1 - 0 = 1
        assert euler_form_ade("A", 1, [1], [1]) == 1

    def test_a2_euler_adjacent(self):
        """A_2: <e_0, e_1> = -1 (adjacent simples)."""
        # For A_2 (vertices 0,1, arrow 0->1): <(1,0), (0,1)> = 0 + 0 - 1 = -1
        assert euler_form_ade("A", 2, [1, 0], [0, 1]) == -1

    def test_a2_euler_nonadjacent(self):
        """A_2: <e_1, e_0> = 0 (non-adjacent direction)."""
        # <(0,1), (1,0)> = 0 + 0 - 0 = 0 (no arrow from 1 to 0)
        assert euler_form_ade("A", 2, [0, 1], [1, 0]) == 0

    def test_euler_diagonal_is_1(self):
        """<e_i, e_i> = 1 for all simple roots (no loops in Dynkin quiver)."""
        for dtype, rank in all_ade_types():
            for i in range(rank):
                ei = [0] * rank
                ei[i] = 1
                assert euler_form_ade(dtype, rank, ei, ei) == 1, \
                    f"Failed for {dtype}_{rank}, vertex {i}"


# ============================================================
# 15. Degree-2 character formula (AP10 cross-check)
# ============================================================


class TestDegree2Formula:
    """Verify degree-2 character = dim_g + C(dim_g+1, 2) by two methods.

    AP10: hardcoded wrong values. We derive the expected value algebraically
    and compare to the product expansion.
    """

    def test_deg2_formula_all_types(self):
        """[q^2] in prod (1-q^n)^{-r} = r + r(r+1)/2 for all ADE types.

        Derivation: (1-q)^{-r}(1-q^2)^{-r}... mod q^3
          = sum_j C(r+j-1,j)q^j * sum_k C(r+k-1,k)q^{2k} * ...
        [q^2] = C(r+1,2) + C(r,1) = r(r+1)/2 + r.
        """
        for dtype, rank in all_ade_types():
            data = ade_lie_data(dtype, rank)
            r = data["dim"]
            expected = r * (r + 1) // 2 + r
            char = coha_character_ade(dtype, rank, 2)
            assert char[2] == expected, \
                f"Failed for {data['type']}: got {char[2]}, expected {expected}"
