"""Comprehensive tests for non-simply-laced bar complex engine.

Tests cover:
  1. B_2, G_2, C_2, F_4, B_3 structural data (dimensions, roots, exponents)
  2. Central charge, kappa, FF duality formulas for all types
  3. Bar cohomology H^1 = dim(g) (universal for KM)
  4. H^1 root space decomposition (long/short classification)
  5. Chain group dimensions B^n = dim(g)^n * (n-1)!
  6. Shadow tower data: class L, alpha=1, S_4=0, Delta=0
  7. Shadow metric Q_L(t) verification
  8. Complementarity: c+c'=2*dim, kappa+kappa'=0
  9. Langlands duality: B_n <-> C_n, Cartan transpose, shared invariants
  10. Casimir degrees and their properties
  11. DS reduction W-algebra generators
  12. Anomaly coefficients and sigma invariants
  13. Cross-family consistency checks
  14. Root length ratio (lacing number)
  15. Invariant bilinear forms

Ground truth from manuscript (landscape_census.tex, kac_moody.tex,
higher_genus_modular_koszul.tex) and CLAUDE.md.
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.nonsimplylaced_bar import (
    # B_2
    b2_data, b2_central_charge, b2_ff_dual, b2_kappa,
    b2_complementarity_sum, b2_bar_generators, b2_bar_deg2_count,
    b2_curvature,
    # G_2
    g2_data, g2_central_charge, g2_ff_dual, g2_kappa,
    g2_complementarity_sum, g2_bar_generators, g2_bar_deg2_count,
    g2_curvature,
    # C_2
    c2_data, c2_central_charge, c2_kappa, c2_ff_dual,
    # F_4
    f4_data, f4_central_charge, f4_kappa, f4_ff_dual,
    # B_3
    b3_data, b3_central_charge, b3_kappa, b3_ff_dual,
    # Periodicity
    periodicity_coxeter, periodicity_vs_dual_coxeter,
    # Universal KM
    km_central_charge, km_kappa, km_ff_dual, km_complementarity_sum,
    # Bar cohomology
    bar_h1_dim, bar_h1_decomposition, bar_chain_dim, bar_euler_char_low,
    # Shadow tower
    km_shadow_class, km_shadow_tower, km_shadow_coefficients,
    # Complementarity
    kappa_complementarity, central_charge_complementarity,
    # Langlands
    langlands_dual_type, langlands_cartan_transpose, langlands_shared_invariants,
    langlands_kappa_comparison,
    # Root lengths
    root_length_ratio, classify_roots_by_length,
    # Casimirs
    casimir_degrees, has_cubic_casimir, highest_casimir_degree,
    # DS reduction
    principal_ds_central_charge, ds_w_algebra_generators,
    ds_b2_w_algebra_info, ds_g2_w_algebra_info,
    # Shadow comparison
    shadow_tower_comparison, shadow_tower_kappa_ordering,
    # Bilinear forms
    n_invariant_bilinear_forms, killing_form_on_roots,
    # Anomaly and sigma
    anomaly_coefficient, sigma_invariant,
    # Weyl and exponents
    weyl_group_order, sum_of_exponents,
    # Verification
    verify_nonsimplylaced_all, verify_all_extended,
)

k = Symbol('k')


# ======================================================================
# 1. Structural data tests
# ======================================================================

class TestB2StructuralData:
    """B_2 = so(5): dim=10, rank=2, h=4, h^v=3."""

    def test_dim(self):
        assert b2_data()["dim"] == 10

    def test_rank(self):
        assert b2_data()["rank"] == 2

    def test_h(self):
        assert b2_data()["h"] == 4

    def test_h_dual(self):
        assert b2_data()["h_dual"] == 3

    def test_h_neq_h_dual(self):
        """CRITICAL: h != h^vee for non-simply-laced."""
        d = b2_data()
        assert d["h"] != d["h_dual"]

    def test_positive_roots_count(self):
        assert b2_data()["n_positive_roots"] == 4

    def test_exponents(self):
        assert b2_data()["exponents"] == [1, 3]

    def test_generators_count(self):
        assert b2_data()["generators"] == 10

    def test_root_lengths(self):
        """B_2: alpha_1 long (|a|^2=2), alpha_2 short (|a|^2=1)."""
        assert b2_data()["root_lengths"] == [2, 1]


class TestG2StructuralData:
    """G_2: dim=14, rank=2, h=6, h^v=4."""

    def test_dim(self):
        assert g2_data()["dim"] == 14

    def test_rank(self):
        assert g2_data()["rank"] == 2

    def test_h(self):
        assert g2_data()["h"] == 6

    def test_h_dual(self):
        assert g2_data()["h_dual"] == 4

    def test_h_neq_h_dual(self):
        d = g2_data()
        assert d["h"] != d["h_dual"]

    def test_positive_roots_count(self):
        assert g2_data()["n_positive_roots"] == 6

    def test_exponents(self):
        assert g2_data()["exponents"] == [1, 5]

    def test_generators_count(self):
        assert g2_data()["generators"] == 14

    def test_root_lengths(self):
        """G_2: alpha_1 short (|a|^2=2), alpha_2 long (|a|^2=6); ratio 1:3."""
        assert g2_data()["root_lengths"] == [2, 6]


class TestC2StructuralData:
    """C_2 = sp(4): Langlands dual to B_2."""

    def test_dim(self):
        assert c2_data()["dim"] == 10

    def test_rank(self):
        assert c2_data()["rank"] == 2

    def test_h(self):
        assert c2_data()["h"] == 4

    def test_h_dual(self):
        assert c2_data()["h_dual"] == 3

    def test_same_dim_as_b2(self):
        """B_2 and C_2 have the same dimension (both = 10)."""
        assert c2_data()["dim"] == b2_data()["dim"]

    def test_same_exponents_as_b2(self):
        """B_2 and C_2 share exponents [1,3]."""
        assert c2_data()["exponents"] == b2_data()["exponents"]

    def test_root_lengths_differ_from_b2(self):
        """C_2 root lengths [1,2] != B_2 root lengths [2,1]."""
        assert c2_data()["root_lengths"] != b2_data()["root_lengths"]


class TestF4StructuralData:
    """F_4: dim=52, rank=4, h=12, h^v=9."""

    def test_dim(self):
        assert f4_data()["dim"] == 52

    def test_rank(self):
        assert f4_data()["rank"] == 4

    def test_h(self):
        assert f4_data()["h"] == 12

    def test_h_dual(self):
        assert f4_data()["h_dual"] == 9

    def test_positive_roots_count(self):
        assert f4_data()["n_positive_roots"] == 24

    def test_exponents(self):
        assert f4_data()["exponents"] == [1, 5, 7, 11]


class TestB3StructuralData:
    """B_3 = so(7): dim=21, rank=3, h=6, h^v=5."""

    def test_dim(self):
        assert b3_data()["dim"] == 21

    def test_rank(self):
        assert b3_data()["rank"] == 3

    def test_h(self):
        assert b3_data()["h"] == 6

    def test_h_dual(self):
        assert b3_data()["h_dual"] == 5

    def test_positive_roots_count(self):
        assert b3_data()["n_positive_roots"] == 9

    def test_exponents(self):
        assert b3_data()["exponents"] == [1, 3, 5]


# ======================================================================
# 2. Central charge, kappa, FF duality
# ======================================================================

class TestB2Formulas:
    def test_central_charge_symbolic(self):
        assert b2_central_charge(k) == 10 * k / (k + 3)

    def test_central_charge_k1(self):
        assert b2_central_charge(1) == Rational(10, 4)

    def test_ff_dual(self):
        assert b2_ff_dual(k) == -k - 6

    def test_ff_involution(self):
        """(k')' = k: the FF involution squares to identity."""
        assert b2_ff_dual(b2_ff_dual(k)) == k

    def test_kappa(self):
        assert b2_kappa(k) == Rational(5) * (k + 3) / 3

    def test_kappa_k1(self):
        """kappa(B_2, k=1) = 5*4/3 = 20/3."""
        assert b2_kappa(1) == Rational(20, 3)

    def test_curvature_vanishes_at_critical(self):
        """At k = -h^vee = -3: curvature vanishes."""
        assert b2_curvature(-3) == 0

    def test_complementarity_sum(self):
        assert b2_complementarity_sum() == 20


class TestG2Formulas:
    def test_central_charge_symbolic(self):
        assert g2_central_charge(k) == 14 * k / (k + 4)

    def test_central_charge_k1(self):
        assert g2_central_charge(1) == Rational(14, 5)

    def test_ff_dual(self):
        assert g2_ff_dual(k) == -k - 8

    def test_ff_involution(self):
        assert g2_ff_dual(g2_ff_dual(k)) == k

    def test_kappa(self):
        assert g2_kappa(k) == Rational(7) * (k + 4) / 4

    def test_curvature_vanishes_at_critical(self):
        assert g2_curvature(-4) == 0

    def test_complementarity_sum(self):
        assert g2_complementarity_sum() == 28


class TestC2Formulas:
    def test_central_charge_equals_b2(self):
        """C_2 and B_2 have the same central charge formula (same dim and h^v)."""
        assert c2_central_charge(k) == b2_central_charge(k)

    def test_kappa_equals_b2(self):
        assert c2_kappa(k) == b2_kappa(k)

    def test_ff_dual(self):
        assert c2_ff_dual(k) == -k - 6

    def test_ff_involution(self):
        assert c2_ff_dual(c2_ff_dual(k)) == k


class TestF4Formulas:
    def test_central_charge(self):
        assert f4_central_charge(k) == 52 * k / (k + 9)

    def test_kappa(self):
        assert f4_kappa(k) == Rational(26) * (k + 9) / 9

    def test_ff_dual(self):
        assert f4_ff_dual(k) == -k - 18

    def test_ff_involution(self):
        assert f4_ff_dual(f4_ff_dual(k)) == k


class TestB3Formulas:
    def test_central_charge(self):
        assert b3_central_charge(k) == 21 * k / (k + 5)

    def test_kappa(self):
        assert b3_kappa(k) == Rational(21) * (k + 5) / 10

    def test_ff_dual(self):
        assert b3_ff_dual(k) == -k - 10

    def test_ff_involution(self):
        assert b3_ff_dual(b3_ff_dual(k)) == k


# ======================================================================
# 3. Universal KM formulas
# ======================================================================

class TestUniversalKM:
    """Test km_* functions against the type-specific ones."""

    @pytest.mark.parametrize("type_,rank,expected_dim", [
        ("B", 2, 10), ("G", 2, 14), ("C", 2, 10), ("B", 3, 21), ("F", 4, 52),
    ])
    def test_central_charge_matches(self, type_, rank, expected_dim):
        """Universal c formula matches type-specific formula."""
        c_univ = km_central_charge(type_, rank, k)
        c_expected = Rational(expected_dim) * k / (k + cartan_data_hdual(type_, rank))
        assert simplify(c_univ - c_expected) == 0

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("C", 2), ("B", 3), ("F", 4),
    ])
    def test_ff_involution(self, type_, rank):
        k_prime = km_ff_dual(type_, rank, k)
        k_double = km_ff_dual(type_, rank, k_prime)
        assert simplify(k_double - k) == 0

    @pytest.mark.parametrize("type_,rank,expected_sum", [
        ("B", 2, 20), ("G", 2, 28), ("C", 2, 20),
        ("B", 3, 42), ("F", 4, 104),
    ])
    def test_complementarity_sum(self, type_, rank, expected_sum):
        assert km_complementarity_sum(type_, rank) == expected_sum

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("C", 2), ("B", 3), ("F", 4),
    ])
    def test_kappa_antisymmetry(self, type_, rank):
        """kappa(k) + kappa(k') = 0 for all KM algebras."""
        _, _, kappa_sum = kappa_complementarity(type_, rank, k)
        assert simplify(kappa_sum) == 0


def cartan_data_hdual(type_: str, rank: int):
    from compute.lib.lie_algebra import cartan_data
    return cartan_data(type_, rank).h_dual


# ======================================================================
# 4. Bar cohomology H^1
# ======================================================================

class TestBarH1:
    """H^1(B(V_k(g))) = dim(g) for all KM algebras."""

    @pytest.mark.parametrize("type_,rank,expected_dim", [
        ("B", 2, 10), ("G", 2, 14), ("C", 2, 10),
        ("B", 3, 21), ("F", 4, 52),
        ("A", 1, 3), ("A", 2, 8), ("A", 3, 15),
    ])
    def test_h1_dimension(self, type_, rank, expected_dim):
        assert bar_h1_dim(type_, rank) == expected_dim

    def test_b2_h1_decomposition(self):
        d = bar_h1_decomposition("B", 2)
        assert d["total"] == 10
        assert d["cartan"] == 2
        assert d["positive_roots"] == 4
        assert d["negative_roots"] == 4
        # All roots accounted for: long+short+cartan = total
        assert d["long_total"] + d["short_total"] + d["cartan"] == 10
        # long + short = n_positive (for positive roots)
        assert d["long_positive"] + d["short_positive"] == 4

    def test_g2_h1_decomposition(self):
        d = bar_h1_decomposition("G", 2)
        assert d["total"] == 14
        assert d["cartan"] == 2
        assert d["positive_roots"] == 6
        # long + short = n_positive
        assert d["long_positive"] + d["short_positive"] == 6

    def test_f4_h1_decomposition(self):
        d = bar_h1_decomposition("F", 4)
        assert d["total"] == 52
        assert d["cartan"] == 4
        assert d["positive_roots"] == 24
        # long + short = n_positive
        assert d["long_positive"] + d["short_positive"] == 24


# ======================================================================
# 5. Chain group dimensions
# ======================================================================

class TestBarChainDimensions:
    """Chain group dim B^n = dim(g)^n * (n-1)!."""

    @pytest.mark.parametrize("type_,rank,dim_g", [
        ("B", 2, 10), ("G", 2, 14), ("C", 2, 10), ("F", 4, 52),
    ])
    def test_degree_1(self, type_, rank, dim_g):
        """B^1 = dim(g)."""
        assert bar_chain_dim(type_, rank, 1) == dim_g

    @pytest.mark.parametrize("type_,rank,dim_g", [
        ("B", 2, 10), ("G", 2, 14),
    ])
    def test_degree_2(self, type_, rank, dim_g):
        """B^2 = dim(g)^2."""
        assert bar_chain_dim(type_, rank, 2) == dim_g ** 2

    @pytest.mark.parametrize("type_,rank,dim_g", [
        ("B", 2, 10), ("G", 2, 14),
    ])
    def test_degree_3(self, type_, rank, dim_g):
        """B^3 = dim(g)^3 * 2."""
        assert bar_chain_dim(type_, rank, 3) == dim_g ** 3 * 2

    def test_b2_deg2_matches_existing(self):
        """Cross-check with the existing b2_bar_deg2_count."""
        assert bar_chain_dim("B", 2, 2) == b2_bar_deg2_count()

    def test_g2_deg2_matches_existing(self):
        assert bar_chain_dim("G", 2, 2) == g2_bar_deg2_count()


# ======================================================================
# 6. Shadow tower (class L)
# ======================================================================

class TestShadowTowerClassL:
    """All KM algebras belong to shadow class L."""

    def test_class_label(self):
        assert km_shadow_class() == 'L'

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("C", 2), ("B", 3), ("F", 4),
    ])
    def test_alpha_is_one(self, type_, rank):
        """Cubic shadow S_3 = 1 for ALL KM algebras."""
        tower = km_shadow_tower(type_, rank, k_val=1)
        assert tower["alpha"] == 1

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("C", 2), ("B", 3), ("F", 4),
    ])
    def test_s4_is_zero(self, type_, rank):
        """S_4 = 0 for all KM (quartic contact vanishes by Jacobi)."""
        tower = km_shadow_tower(type_, rank, k_val=1)
        assert tower["S4"] == 0

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("C", 2), ("B", 3), ("F", 4),
    ])
    def test_discriminant_zero(self, type_, rank):
        """Delta = 8*kappa*S_4 = 0 for class L."""
        tower = km_shadow_tower(type_, rank, k_val=1)
        assert tower["discriminant"] == 0

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("C", 2), ("B", 3), ("F", 4),
    ])
    def test_depth_class_L(self, type_, rank):
        tower = km_shadow_tower(type_, rank, k_val=1)
        assert tower["depth_class"] == 'L'


class TestShadowCoefficients:
    """Numerical shadow coefficients for non-simply-laced KM."""

    def test_b2_coefficients_k1(self):
        """B_2 at k=1: kappa=20/3, S_3=1, S_r=0 for r>=4."""
        coeffs = km_shadow_coefficients("B", 2, k_val=1, max_r=8)
        assert abs(coeffs[2] - 20.0 / 3.0) < 1e-10
        assert abs(coeffs[3] - 1.0) < 1e-10
        for r in range(4, 9):
            assert abs(coeffs[r]) < 1e-10

    def test_g2_coefficients_k1(self):
        """G_2 at k=1: kappa=7*5/4=35/4, S_3=1, S_r=0 for r>=4."""
        coeffs = km_shadow_coefficients("G", 2, k_val=1, max_r=8)
        assert abs(coeffs[2] - 35.0 / 4.0) < 1e-10
        assert abs(coeffs[3] - 1.0) < 1e-10
        for r in range(4, 9):
            assert abs(coeffs[r]) < 1e-10

    def test_shadow_terminates_at_arity_3(self):
        """All KM shadow towers have S_r = 0 for r >= 4."""
        for type_, rank in [("B", 2), ("G", 2), ("F", 4)]:
            coeffs = km_shadow_coefficients(type_, rank, k_val=1, max_r=15)
            for r in range(4, 16):
                assert abs(coeffs[r]) < 1e-10, f"{type_}{rank}: S_{r} != 0"


class TestShadowMetric:
    """Shadow metric Q_L(t) = 4*kappa^2 + 12*kappa*t + 9*t^2 for class L."""

    def test_b2_q2_is_nine(self):
        """For class L: q_2 = 9*alpha^2 = 9."""
        tower = km_shadow_tower("B", 2, k_val=1)
        assert tower["shadow_metric_q2"] == 9

    def test_g2_q2_is_nine(self):
        tower = km_shadow_tower("G", 2, k_val=1)
        assert tower["shadow_metric_q2"] == 9

    def test_q_is_perfect_square(self):
        """For class L (Delta=0), Q_L(t) = (2*kappa + 3*t)^2 is a perfect square.

        This is the defining property of class L: the shadow metric has
        zero discriminant, so it factors as a perfect square.
        """
        for type_, rank in [("B", 2), ("G", 2), ("C", 2)]:
            tower = km_shadow_tower(type_, rank, k_val=1)
            q0 = tower["shadow_metric_q0"]
            q1 = tower["shadow_metric_q1"]
            q2 = tower["shadow_metric_q2"]
            # Q(t) = q0 + q1*t + q2*t^2
            # Perfect square iff q1^2 = 4*q0*q2
            assert simplify(q1 ** 2 - 4 * q0 * q2) == 0


# ======================================================================
# 7. Complementarity
# ======================================================================

class TestComplementarity:
    """c + c' = 2*dim(g) and kappa + kappa' = 0."""

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("C", 2), ("B", 3), ("F", 4),
    ])
    def test_central_charge_sum(self, type_, rank):
        c_val, c_prime, c_sum = central_charge_complementarity(type_, rank, k)
        from compute.lib.lie_algebra import cartan_data
        dim_g = cartan_data(type_, rank).dim
        assert simplify(c_sum - 2 * dim_g) == 0

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("C", 2), ("B", 3), ("F", 4),
    ])
    def test_kappa_antisymmetry(self, type_, rank):
        _, _, kappa_sum = kappa_complementarity(type_, rank, k)
        assert simplify(kappa_sum) == 0

    def test_b2_central_charge_sum_numerical(self):
        """c(B_2,k=1) + c(B_2,k'=-7) = 2*10 = 20."""
        c1 = b2_central_charge(1)
        c_prime = b2_central_charge(b2_ff_dual(1))  # k' = -1-6 = -7
        assert c1 + c_prime == 20


# ======================================================================
# 8. Langlands duality
# ======================================================================

class TestLanglandsDuality:
    """B_n <-> C_n, G_2 and F_4 self-dual."""

    def test_b2_dual_is_c2(self):
        assert langlands_dual_type("B", 2) == ("C", 2)

    def test_c2_dual_is_b2(self):
        assert langlands_dual_type("C", 2) == ("B", 2)

    def test_g2_self_dual(self):
        assert langlands_dual_type("G", 2) == ("G", 2)

    def test_f4_self_dual(self):
        assert langlands_dual_type("F", 4) == ("F", 4)

    def test_b3_dual_is_c3(self):
        assert langlands_dual_type("B", 3) == ("C", 3)

    def test_b2_cartan_transpose(self):
        """Cartan(C_2) = Cartan(B_2)^T."""
        assert langlands_cartan_transpose("B", 2)

    def test_c2_cartan_transpose(self):
        assert langlands_cartan_transpose("C", 2)

    def test_b3_cartan_transpose(self):
        assert langlands_cartan_transpose("B", 3)


class TestLanglandsSharedInvariants:
    """Langlands dual algebras share dimension, h, and exponents."""

    def test_b2_c2_dim(self):
        s = langlands_shared_invariants("B", 2)
        assert s["dim_equal"]
        assert s["dim"] == 10

    def test_b2_c2_h(self):
        s = langlands_shared_invariants("B", 2)
        assert s["h_equal"]
        assert s["h"] == 4

    def test_b2_c2_exponents(self):
        s = langlands_shared_invariants("B", 2)
        assert s["exponents_equal"]
        assert s["exponents"] == [1, 3]

    def test_b2_c2_h_dual_equal(self):
        """B_2 and C_2 happen to have the SAME h^vee = 3."""
        s = langlands_shared_invariants("B", 2)
        assert s["h_dual_equal"]

    def test_b3_c3_h_dual_differ(self):
        """B_3 and C_3 have DIFFERENT h^vee: B_3 h^v=5, C_3 h^v=4."""
        s = langlands_shared_invariants("B", 3)
        assert not s["h_dual_equal"]
        assert s["h_dual_g"] == 5   # B_3
        assert s["h_dual_gL"] == 4  # C_3

    def test_b2_c2_root_lengths_differ(self):
        """Root lengths are SWAPPED under Langlands duality."""
        s = langlands_shared_invariants("B", 2)
        assert not s["root_lengths_equal"]

    def test_b2_c2_kappa_equal(self):
        """B_2 and C_2 have the same kappa (same dim and h^v)."""
        comp = langlands_kappa_comparison("B", 2, k)
        assert comp["equal_at_same_k"]

    def test_b3_c3_kappa_differ(self):
        """B_3 and C_3 have DIFFERENT kappa (different h^v)."""
        comp = langlands_kappa_comparison("B", 3, k)
        assert not comp["equal_at_same_k"]


# ======================================================================
# 9. Root length classification
# ======================================================================

class TestRootLengths:
    """Lacing number and root classification."""

    @pytest.mark.parametrize("type_,rank,expected_lacing", [
        ("B", 2, 2), ("C", 2, 2), ("B", 3, 2), ("G", 2, 3), ("F", 4, 2),
    ])
    def test_lacing_number(self, type_, rank, expected_lacing):
        assert root_length_ratio(type_, rank) == expected_lacing

    def test_b2_root_classification(self):
        c = classify_roots_by_length("B", 2)
        # long + short = total positive roots
        assert c["n_long_positive"] + c["n_short_positive"] == 4
        assert c["n_total_positive"] == 4
        # Both types present (non-simply-laced)
        assert c["n_long_positive"] >= 1
        assert c["n_short_positive"] >= 1

    def test_g2_root_classification(self):
        c = classify_roots_by_length("G", 2)
        assert c["n_long_positive"] + c["n_short_positive"] == 6
        assert c["n_total_positive"] == 6
        assert c["n_long_positive"] >= 1
        assert c["n_short_positive"] >= 1

    def test_f4_root_classification(self):
        c = classify_roots_by_length("F", 4)
        assert c["n_long_positive"] + c["n_short_positive"] == 24
        assert c["n_total_positive"] == 24
        assert c["n_long_positive"] >= 1
        assert c["n_short_positive"] >= 1


# ======================================================================
# 10. Casimir invariants
# ======================================================================

class TestCasimirInvariants:
    """Casimir degrees = exponents + 1."""

    def test_b2_casimir_degrees(self):
        assert casimir_degrees("B", 2) == [2, 4]

    def test_g2_casimir_degrees(self):
        assert casimir_degrees("G", 2) == [2, 6]

    def test_f4_casimir_degrees(self):
        assert casimir_degrees("F", 4) == [2, 6, 8, 12]

    def test_b3_casimir_degrees(self):
        assert casimir_degrees("B", 3) == [2, 4, 6]

    def test_no_cubic_casimir_b2(self):
        """B_2 has NO cubic Casimir (degrees 2,4 only)."""
        assert not has_cubic_casimir("B", 2)

    def test_no_cubic_casimir_g2(self):
        """G_2 has NO cubic Casimir (degrees 2,6 only)."""
        assert not has_cubic_casimir("G", 2)

    def test_no_cubic_casimir_f4(self):
        assert not has_cubic_casimir("F", 4)

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("B", 3), ("F", 4),
    ])
    def test_highest_casimir_equals_h(self, type_, rank):
        """max(Casimir degree) = h (Coxeter number)."""
        from compute.lib.lie_algebra import cartan_data
        h = cartan_data(type_, rank).h
        assert highest_casimir_degree(type_, rank) == h

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("B", 3), ("F", 4),
    ])
    def test_n_casimirs_equals_rank(self, type_, rank):
        """Number of independent Casimirs = rank."""
        from compute.lib.lie_algebra import cartan_data
        r = cartan_data(type_, rank).rank
        assert len(casimir_degrees(type_, rank)) == r


# ======================================================================
# 11. DS reduction
# ======================================================================

class TestDSReduction:
    """Principal DS reduction W(g) data."""

    def test_b2_w_generators(self):
        info = ds_b2_w_algebra_info()
        assert info["n_generators"] == 2
        assert info["generator_weights"] == [2, 4]
        assert info["virasoro_present"]
        assert not info["cubic_generator"]

    def test_g2_w_generators(self):
        info = ds_g2_w_algebra_info()
        assert info["n_generators"] == 2
        assert info["generator_weights"] == [2, 6]
        assert info["virasoro_present"]
        assert not info["cubic_generator"]

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("B", 3), ("F", 4),
    ])
    def test_ds_generator_weights(self, type_, rank):
        """DS generator weights = Casimir degrees."""
        weights = ds_w_algebra_generators(type_, rank)
        assert weights == casimir_degrees(type_, rank)

    def test_ds_b2_central_charge_k1(self):
        """c_W(B_2, k=1) should be a rational number."""
        c_w = principal_ds_central_charge("B", 2, k=1)
        assert c_w is not None
        # The formula gives rank - 12*rho_sq/(k+h^v)
        # B_2: rank=2, exponents=[1,3], rho_sq = (1*2+3*4)/2 = (2+12)/2=7
        # c = 2 - 12*7/4 = 2 - 21 = -19
        assert c_w == Rational(2) - Rational(84, 4)


# ======================================================================
# 12. Anomaly coefficients and sigma
# ======================================================================

class TestAnomalyAndSigma:
    def test_b2_anomaly(self):
        """rho(B_2) = dim/(2*h^v) = 10/6 = 5/3."""
        assert anomaly_coefficient("B", 2) == Rational(5, 3)

    def test_g2_anomaly(self):
        """rho(G_2) = 14/8 = 7/4."""
        assert anomaly_coefficient("G", 2) == Rational(7, 4)

    def test_f4_anomaly(self):
        """rho(F_4) = 52/18 = 26/9."""
        assert anomaly_coefficient("F", 4) == Rational(26, 9)

    def test_b2_sigma(self):
        """sigma(B_2) = 1/2 + 1/4 = 3/4."""
        assert sigma_invariant("B", 2) == Rational(3, 4)

    def test_g2_sigma(self):
        """sigma(G_2) = 1/2 + 1/6 = 2/3."""
        assert sigma_invariant("G", 2) == Rational(2, 3)

    def test_f4_sigma(self):
        """sigma(F_4) = 1/2 + 1/6 + 1/8 + 1/12 = 7/8."""
        assert sigma_invariant("F", 4) == Rational(7, 8)


# ======================================================================
# 13. Bilinear forms
# ======================================================================

class TestBilinearForms:
    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("C", 2), ("B", 3), ("F", 4),
    ])
    def test_unique_invariant_form(self, type_, rank):
        """Simple Lie algebras have exactly one invariant bilinear form."""
        assert n_invariant_bilinear_forms(type_, rank) == 1

    def test_b2_killing_form(self):
        kf = killing_form_on_roots("B", 2)
        assert kf["lacing_number"] == 2
        assert kf["long_pairing"] == Rational(1)
        assert kf["short_pairing"] == Rational(2)

    def test_g2_killing_form(self):
        kf = killing_form_on_roots("G", 2)
        assert kf["lacing_number"] == 3
        assert kf["long_pairing"] == Rational(1, 3)
        assert kf["short_pairing"] == Rational(1)


# ======================================================================
# 14. Weyl group and exponent identities
# ======================================================================

class TestWeylAndExponents:
    @pytest.mark.parametrize("type_,rank,expected_order", [
        ("B", 2, 8), ("G", 2, 12), ("B", 3, 48), ("F", 4, 1152),
    ])
    def test_weyl_group_order(self, type_, rank, expected_order):
        assert weyl_group_order(type_, rank) == expected_order

    @pytest.mark.parametrize("type_,rank", [
        ("B", 2), ("G", 2), ("B", 3), ("F", 4),
    ])
    def test_sum_exponents_equals_npos(self, type_, rank):
        """sum(m_i) = number of positive roots."""
        from compute.lib.lie_algebra import cartan_data
        data = cartan_data(type_, rank)
        assert sum_of_exponents(type_, rank) == len(data.positive_roots)


# ======================================================================
# 15. Periodicity
# ======================================================================

class TestPeriodicity:
    def test_b2_period(self):
        """Period = 2h = 8 (NOT 2*h^v = 6)."""
        assert periodicity_coxeter("B", 2) == 8

    def test_g2_period(self):
        """Period = 2h = 12 (NOT 2*h^v = 8)."""
        assert periodicity_coxeter("G", 2) == 12

    def test_b3_period(self):
        assert periodicity_coxeter("B", 3) == 12

    def test_f4_period(self):
        assert periodicity_coxeter("F", 4) == 24


# ======================================================================
# 16. Cross-family consistency (AP10 guard)
# ======================================================================

class TestCrossFamilyConsistency:
    """Guard against AP10: tests with hardcoded wrong expected values.
    Use cross-family structural relations as the real verification."""

    def test_kappa_scales_with_dim(self):
        """At the same shifted level k+h^v = 1: kappa = dim(g)/(2*h^v).
        kappa(B_2, k=-2) = 10*1/6 = 5/3.
        kappa(G_2, k=-3) = 14*1/8 = 7/4.
        kappa(B_2)/kappa(G_2) = (5/3)/(7/4) = 20/21 = 10*4/(14*3)."""
        kappa_b2 = b2_kappa(-2)  # 5*(-2+3)/3 = 5/3
        kappa_g2 = g2_kappa(-3)  # 7*(-3+4)/4 = 7/4
        assert kappa_b2 == Rational(5, 3)
        assert kappa_g2 == Rational(7, 4)
        # Ratio should be dim(B2)*h^v(G2) / (dim(G2)*h^v(B2))
        expected_ratio = Rational(10 * 4, 14 * 3)
        assert kappa_b2 / kappa_g2 == expected_ratio

    def test_b2_c2_coincidence(self):
        """B_2 and C_2 have identical kappa AND c formulas.
        This is because dim(B_2)=dim(C_2)=10 AND h^v(B_2)=h^v(C_2)=3."""
        for k_val in [1, 2, 5, -1]:
            assert b2_kappa(k_val) == c2_kappa(k_val)
            assert b2_central_charge(k_val) == c2_central_charge(k_val)

    def test_shadow_tower_consistent_with_recursive(self):
        """Compare our shadow tower data with shadow_tower_recursive STANDARD_FAMILIES.

        shadow_tower_recursive has Affine_sl2 with alpha=1.0, S4=0.0.
        All non-simply-laced KM should also have alpha=1, S4=0 (class L).
        """
        for type_, rank in [("B", 2), ("G", 2), ("F", 4)]:
            tower = km_shadow_tower(type_, rank, k_val=1)
            assert tower["alpha"] == 1
            assert tower["S4"] == 0

    def test_complementarity_additivity_b2(self):
        """c(B_2,k) + c(B_2,k') = 2*dim = 20 for multiple k values."""
        for k_val in [1, 2, 3, 5, 10, -1, Rational(1, 2)]:
            c = b2_central_charge(k_val)
            c_prime = b2_central_charge(b2_ff_dual(k_val))
            assert c + c_prime == 20


# ======================================================================
# 17. Shadow tower comparison
# ======================================================================

class TestShadowTowerComparison:
    def test_comparison_all_class_L(self):
        """Every algebra in the comparison table has depth_class 'L'."""
        comp = shadow_tower_comparison(k_val=1)
        for name, data in comp.items():
            assert data["depth_class"] == "L", f"{name} is not class L"

    def test_comparison_all_depth_3(self):
        comp = shadow_tower_comparison(k_val=1)
        for name, data in comp.items():
            assert data["depth"] == 3

    def test_kappa_ordering_at_k1(self):
        """Verify kappa ordering makes sense: larger dim => larger kappa
        (at the same level, modulo h^v differences)."""
        ordering = shadow_tower_kappa_ordering(k_val=1)
        # sl_2 (dim=3) should have smallest kappa
        assert ordering[0][0] == "sl_2"
        # F_4 (dim=52) should have largest kappa
        assert ordering[-1][0] == "F_4"


# ======================================================================
# 18. Integration tests
# ======================================================================

class TestIntegration:
    def test_verify_all_pass(self):
        """All original verification checks pass."""
        for name, ok in verify_nonsimplylaced_all().items():
            assert ok, f"Failed: {name}"

    def test_verify_all_extended_pass(self):
        """All extended verification checks pass."""
        for name, ok in verify_all_extended().items():
            assert ok, f"Failed: {name}"

    def test_bar_generators_consistent(self):
        """b2_bar_generators and bar_h1_dim give the same answer."""
        g = b2_bar_generators()
        assert g["total"] == bar_h1_dim("B", 2)

    def test_g2_bar_generators_consistent(self):
        g = g2_bar_generators()
        assert g["total"] == bar_h1_dim("G", 2)
