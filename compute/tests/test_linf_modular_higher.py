r"""Tests for higher L-infinity brackets ell_5, ell_6 on the modular convolution algebra.

Verifies:
1.  Catalan numbers and binary tree enumeration
2.  Associahedron K_6, K_7 f-vectors and Euler characteristics
3.  Betti numbers of M_bar_{0,n} (extended range n <= 8)
4.  Unshuffle enumeration and Koszul signs
5.  ell_5 at the scalar level (vanishes for all algebras)
6.  ell_6 at the scalar level (vanishes for all algebras)
7.  Generalized Jacobi identity at order 5 (scalar)
8.  Generalized Jacobi identity at order 6 (scalar)
9.  Heisenberg: ell_5 = ell_6 = 0 (class G, terminates at arity 2)
10. Affine sl_2: ell_5 = ell_6 = 0 (class L, terminates at arity 3)
11. Beta-gamma: ell_5 = ell_6 = 0 (class C, terminates at arity 4)
12. Virasoro: ell_5 != 0, ell_6 != 0 at vector level (class M, infinite)
13. MC equation at arities 5--8 for all families
14. Obstruction class o_6 computation
15. Three-route verification (Feynman, HTT, stable graph)
16. Cross-family consistency (depth ordering)
17. Shadow obstruction tower extended coefficients (S_5 through S_8)
18. Depth classification from bracket vanishing pattern
19. Multinomial coefficients
20. HTT tree counts for ell_5, ell_6
21. Genus-0 stable graph counts

References:
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  thm:recursive-existence (higher_genus_modular_koszul.tex)
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
  constr:explicit-convolution-linfty (higher_genus_modular_koszul.tex)
  thm:operadic-complexity-detailed (higher_genus_modular_koszul.tex)
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, S, simplify

from compute.lib.linf_modular_higher import (
    # Catalan and binary trees
    catalan,
    binary_tree_count,
    # Associahedra
    associahedron_f_vector,
    associahedron_euler_char,
    k6_f_vector,
    k7_f_vector,
    # Betti numbers
    mbar_0n_betti_extended,
    mbar_0n_euler_extended,
    # Unshuffles and signs
    unshuffles,
    koszul_sign,
    unshuffle_sign,
    multinomial_coeff,
    # Scalar brackets
    HigherScalarBracket,
    scalar_mc_binary,
    # Vector brackets
    HigherVectorBracket,
    # Obstruction class
    obstruction_class_o6,
    # Jacobi identities
    generalized_jacobi_order_n_scalar,
    jacobi_order5_scalar,
    jacobi_order6_scalar,
    # HTT
    htt_tree_count,
    htt_ell5_tree_count,
    htt_ell6_tree_count,
    # Stable graphs
    genus0_stable_graph_count,
    genus0_binary_tree_channels,
    # Three routes
    verify_three_routes,
    # Concrete algebras
    virasoro_shadow_coefficients_extended,
    heisenberg_higher_brackets,
    affine_sl2_higher_brackets,
    betagamma_higher_brackets,
    virasoro_higher_brackets,
    # Depth classification
    depth_class_from_brackets,
    verify_depth_class,
    # Full MC
    mc_equation_full,
    # Theta evaluations
    ell_5_on_truncated_theta,
    ell_6_on_truncated_theta,
    # Summary
    higher_bracket_summary,
    cross_family_consistency,
)


c = Symbol('c')
k = Symbol('k')


# =========================================================================
# 1. Catalan numbers
# =========================================================================

class TestCatalan:
    """Catalan number computation and binary tree enumeration."""

    def test_catalan_small(self):
        """C_0=1, C_1=1, C_2=2, C_3=5, C_4=14, C_5=42, C_6=132."""
        expected = [1, 1, 2, 5, 14, 42, 132]
        for n, val in enumerate(expected):
            assert catalan(n) == val, f"C_{n} = {catalan(n)}, expected {val}"

    def test_catalan_negative(self):
        """C_n = 0 for n < 0."""
        assert catalan(-1) == 0

    def test_catalan_7(self):
        """C_7 = 429."""
        assert catalan(7) == 429

    def test_binary_tree_count_leaves(self):
        """Binary trees with n leaves: C_{n-1}."""
        assert binary_tree_count(2) == 1   # C_1 = 1
        assert binary_tree_count(3) == 2   # C_2 = 2
        assert binary_tree_count(4) == 5   # C_3 = 5
        assert binary_tree_count(5) == 14  # C_4 = 14
        assert binary_tree_count(6) == 42  # C_5 = 42
        assert binary_tree_count(7) == 132 # C_6 = 132

    def test_binary_tree_for_ell_k(self):
        """ell_k uses trees with k+1 leaves: count = C_k."""
        assert binary_tree_count(3 + 1) == catalan(3)   # ell_3: C_3 = 5
        assert binary_tree_count(4 + 1) == catalan(4)   # ell_4: C_4 = 14
        assert binary_tree_count(5 + 1) == catalan(5)   # ell_5: C_5 = 42
        assert binary_tree_count(6 + 1) == catalan(6)   # ell_6: C_6 = 132


# =========================================================================
# 2. Associahedra K_n
# =========================================================================

class TestAssociahedra:
    """Stasheff associahedra f-vectors and Euler characteristics."""

    def test_k3_f_vector(self):
        """K_3 = point: f = {0: 1}."""
        fv = associahedron_f_vector(3)
        assert fv == {0: 1}

    def test_k4_f_vector(self):
        """K_4 = interval: f = {0: 2, 1: 1}."""
        fv = associahedron_f_vector(4)
        assert fv == {0: 2, 1: 1}

    def test_k5_f_vector(self):
        """K_5 = pentagon: f = {0: 5, 1: 5, 2: 1}."""
        fv = associahedron_f_vector(5)
        assert fv == {0: 5, 1: 5, 2: 1}

    def test_k6_f_vector(self):
        """K_6 (3D polytope for ell_4): 14 vertices, 21 edges, 9 faces, 1 cell."""
        fv = associahedron_f_vector(6)
        assert fv[0] == 14    # C_4 = 14 vertices
        assert fv[1] == 21
        assert fv[2] == 9
        assert fv[3] == 1

    def test_k7_f_vector(self):
        """K_7 (4D polytope for ell_5): 42 vertices."""
        fv = associahedron_f_vector(7)
        assert fv[0] == 42    # C_5 = 42 vertices
        assert fv[1] == 84
        assert fv[2] == 56
        assert fv[3] == 14
        assert fv[4] == 1

    def test_k8_f_vector(self):
        """K_8 (5D polytope for ell_6): 132 vertices."""
        fv = associahedron_f_vector(8)
        assert fv[0] == 132   # C_6 = 132 vertices
        assert fv[1] == 330
        assert fv[2] == 300
        assert fv[3] == 120
        assert fv[4] == 20
        assert fv[5] == 1

    def test_k6_convenience(self):
        """k6_f_vector returns (42, 84, 56, 14, 1)."""
        assert k6_f_vector() == (42, 84, 56, 14, 1)

    def test_k7_convenience(self):
        """k7_f_vector returns (132, 330, 300, 120, 20, 1)."""
        assert k7_f_vector() == (132, 330, 300, 120, 20, 1)

    def test_euler_char_contractible(self):
        """All associahedra are contractible: chi = 1."""
        for n in range(3, 9):
            chi = associahedron_euler_char(n)
            assert chi == 1, f"chi(K_{n}) = {chi}, expected 1"

    def test_k7_euler_direct(self):
        """K_7: 42 - 84 + 56 - 14 + 1 = 1."""
        fv = k6_f_vector()  # (42, 84, 56, 14, 1)
        chi = fv[0] - fv[1] + fv[2] - fv[3] + fv[4]
        assert chi == 1

    def test_k8_euler_direct(self):
        """K_8: 132 - 330 + 300 - 120 + 20 - 1 = 1."""
        fv = k7_f_vector()  # (132, 330, 300, 120, 20, 1)
        chi = fv[0] - fv[1] + fv[2] - fv[3] + fv[4] - fv[5]
        assert chi == 1


# =========================================================================
# 3. Betti numbers of M_bar_{0,n}
# =========================================================================

class TestBettiNumbers:
    """Extended Betti numbers of M_bar_{0,n}."""

    def test_mbar_03(self):
        """M_bar_{0,3} = point."""
        assert mbar_0n_betti_extended(3) == {0: 1}

    def test_mbar_04(self):
        """M_bar_{0,4} = P^1."""
        assert mbar_0n_betti_extended(4) == {0: 1, 2: 1}

    def test_mbar_05(self):
        """M_bar_{0,5}: del Pezzo surface, b_2 = 5."""
        b = mbar_0n_betti_extended(5)
        assert b == {0: 1, 2: 5, 4: 1}

    def test_mbar_06(self):
        """M_bar_{0,6}: dim_C = 3, b_2 = 16."""
        b = mbar_0n_betti_extended(6)
        assert b[0] == 1
        assert b[2] == 16
        assert b[4] == 16
        assert b[6] == 1

    def test_mbar_07(self):
        """M_bar_{0,7}: dim_C = 4."""
        b = mbar_0n_betti_extended(7)
        assert b[0] == 1
        assert b[2] == 42
        assert b[4] == 127
        assert b[6] == 42
        assert b[8] == 1

    def test_mbar_08(self):
        """M_bar_{0,8}: dim_C = 5."""
        b = mbar_0n_betti_extended(8)
        assert b[0] == 1
        assert b[2] == 99
        assert b[10] == 1

    def test_euler_char_extended(self):
        """Euler characteristics of M_bar_{0,n}."""
        # n=3: 1, n=4: 2, n=5: 7, n=6: 34, n=7: 213, n=8: 1544
        expected = {3: 1, 4: 2, 5: 7, 6: 34, 7: 213, 8: 1544}
        for n, val in expected.items():
            chi = mbar_0n_euler_extended(n)
            assert chi == val, f"chi(M_bar_{{0,{n}}}) = {chi}, expected {val}"

    def test_poincare_duality(self):
        """Poincare duality: b_k = b_{2d-k} where d = dim_C = n-3."""
        for n in range(3, 9):
            b = mbar_0n_betti_extended(n)
            d = 2 * (n - 3)  # real dimension
            for deg, val in b.items():
                dual = b.get(d - deg, 0)
                assert val == dual, (
                    f"Poincare duality fails for M_bar_{{0,{n}}}: "
                    f"b_{deg} = {val} != b_{d - deg} = {dual}"
                )


# =========================================================================
# 4. Unshuffles and signs
# =========================================================================

class TestUnshuffles:
    """Unshuffle enumeration and Koszul signs."""

    def test_unshuffle_count(self):
        """Number of (p, n-p)-unshuffles = C(n, p)."""
        assert len(unshuffles(4, 2)) == 6   # C(4,2) = 6
        assert len(unshuffles(5, 2)) == 10  # C(5,2) = 10
        assert len(unshuffles(5, 3)) == 10  # C(5,3) = 10
        assert len(unshuffles(6, 3)) == 20  # C(6,3) = 20

    def test_unshuffle_5_1(self):
        """(1, 4)-unshuffles of {0,...,4}: 5 choices."""
        shuf = unshuffles(5, 1)
        assert len(shuf) == 5

    def test_koszul_sign_degree_0(self):
        """All signs +1 for degree-0 elements."""
        for perm in [(0, 1, 2), (1, 0, 2), (2, 1, 0)]:
            assert koszul_sign(perm, (0, 0, 0)) == 1

    def test_koszul_sign_odd_degree(self):
        """Odd-degree transposition gives -1."""
        assert koszul_sign((1, 0), (1, 1)) == -1

    def test_multinomial_all_distinct(self):
        """4 distinct values: multinomial = 4! = 24."""
        assert multinomial_coeff((2, 3, 4, 5)) == 24

    def test_multinomial_two_pairs(self):
        """Two pairs: (2,2,3,3) -> 4!/(2!*2!) = 6."""
        assert multinomial_coeff((2, 2, 3, 3)) == 6

    def test_multinomial_all_same(self):
        """All same: (2,2,2,2) -> 4!/4! = 1."""
        assert multinomial_coeff((2, 2, 2, 2)) == 1

    def test_multinomial_5_inputs(self):
        """5 inputs, all same: 5!/5! = 1."""
        assert multinomial_coeff((2, 2, 2, 2, 2)) == 1

    def test_multinomial_5_distinct(self):
        """5 distinct: 5! = 120."""
        assert multinomial_coeff((2, 3, 4, 5, 6)) == 120


# =========================================================================
# 5-6. ell_5 and ell_6 at scalar level
# =========================================================================

class TestScalarBrackets:
    """ell_5 and ell_6 at the scalar level (genus 0)."""

    def test_ell_5_scalar_vanishes_generic(self):
        """ell_5(scalars) = 0 at genus 0 for any algebra."""
        shadows = {2: c / 2, 3: S(2), 4: S(10) / (c * (5 * c + 22))}
        sb = HigherScalarBracket(shadows, "Virasoro")
        val, arity = sb.ell_5_scalar([c / 2] * 5, [2] * 5)
        assert simplify(val) == 0

    def test_ell_6_scalar_vanishes_generic(self):
        """ell_6(scalars) = 0 at genus 0 for any algebra."""
        shadows = {2: c / 2, 3: S(2)}
        sb = HigherScalarBracket(shadows, "Virasoro")
        val, arity = sb.ell_6_scalar([c / 2] * 6, [2] * 6)
        assert simplify(val) == 0

    def test_ell_5_output_arity(self):
        """ell_5 output arity = sum(arities) - 2*4 = sum - 8."""
        shadows = {2: S.One}
        sb = HigherScalarBracket(shadows)
        _, arity = sb.ell_5_scalar([S.One] * 5, [2] * 5)
        assert arity == 10 - 8  # = 2

    def test_ell_6_output_arity(self):
        """ell_6 output arity = sum(arities) - 2*5 = sum - 10."""
        shadows = {2: S.One}
        sb = HigherScalarBracket(shadows)
        _, arity = sb.ell_6_scalar([S.One] * 6, [2] * 6)
        assert arity == 12 - 10  # = 2

    def test_ell_5_mixed_arities_scalar(self):
        """ell_5 with mixed arities is still zero at scalar level."""
        shadows = {2: c / 2, 3: S(2), 4: S(10) / (c * (5 * c + 22))}
        sb = HigherScalarBracket(shadows)
        val, arity = sb.ell_5_scalar(
            [c / 2, c / 2, c / 2, c / 2, S(2)],
            [2, 2, 2, 2, 3]
        )
        assert simplify(val) == 0
        assert arity == 11 - 8  # = 3

    def test_ell_k_scalar_binary_nonzero(self):
        """ell_2 at scalar level is nonzero (the binary bracket)."""
        shadows = {2: S(5)}
        sb = HigherScalarBracket(shadows)
        val, arity = sb.ell_k_scalar(2, [S(5), S(5)], [2, 2])
        assert simplify(val) == simplify(2 * 2 * 5 * 5)  # j*k*s_j*s_k = 4*25 = 100

    def test_effective_ell5_zero(self):
        """Effective ell_5 at scalar level is zero."""
        shadows = {2: c / 2, 3: S(2), 4: S(10) / (c * (5 * c + 22))}
        sb = HigherScalarBracket(shadows, "Virasoro")
        assert sb.ell_5_effective_scalar() == S.Zero

    def test_effective_ell6_zero(self):
        """Effective ell_6 at scalar level is zero."""
        shadows = {2: c / 2}
        sb = HigherScalarBracket(shadows)
        assert sb.ell_6_effective_scalar() == S.Zero


# =========================================================================
# 7-8. Generalized Jacobi identities at orders 5 and 6
# =========================================================================

class TestJacobiIdentities:
    """Generalized Jacobi (higher homotopy) identities."""

    def test_jacobi_order5_scalar_satisfied(self):
        """J_5 = 0 at the scalar level."""
        result = jacobi_order5_scalar([c / 2] * 5, [2] * 5)
        assert result["satisfied"]
        assert simplify(result["total"]) == 0

    def test_jacobi_order6_scalar_satisfied(self):
        """J_6 = 0 at the scalar level."""
        result = jacobi_order6_scalar([c / 2] * 6, [2] * 6)
        assert result["satisfied"]
        assert simplify(result["total"]) == 0

    def test_jacobi_order5_all_terms_zero(self):
        """All individual terms of J_5 vanish at scalar level."""
        result = jacobi_order5_scalar([c / 2] * 5, [2] * 5)
        for key, val in result["terms"].items():
            assert simplify(val) == 0, f"Term {key} nonzero: {val}"

    def test_jacobi_order6_all_terms_zero(self):
        """All individual terms of J_6 vanish at scalar level."""
        result = jacobi_order6_scalar([c / 2] * 6, [2] * 6)
        for key, val in result["terms"].items():
            assert simplify(val) == 0, f"Term {key} nonzero: {val}"

    def test_jacobi_order5_heisenberg(self):
        """Jacobi at order 5 for Heisenberg (k = 1)."""
        kappa = S.One
        result = jacobi_order5_scalar([kappa] * 5, [2] * 5)
        assert result["satisfied"]

    def test_jacobi_order6_virasoro_concrete(self):
        """Jacobi at order 6 for Virasoro at c = 25."""
        kappa = Rational(25, 2)
        result = jacobi_order6_scalar([kappa] * 6, [2] * 6)
        assert result["satisfied"]

    def test_jacobi_general_n_structure(self):
        """Generalized Jacobi at order n: correct structure for n=5,6,7."""
        for n in [5, 6, 7]:
            vals = [S.One] * n
            arities = [2] * n
            result = generalized_jacobi_order_n_scalar(n, vals, arities)
            assert result["order"] == n
            assert result["satisfied"]


# =========================================================================
# 9. Heisenberg: class G
# =========================================================================

class TestHeisenberg:
    """Heisenberg algebra (class G, depth 2): all higher brackets vanish."""

    def test_ell_5_vanishes(self):
        """ell_5 = 0 for Heisenberg."""
        h = heisenberg_higher_brackets(S.One)
        assert h["ell_5_vanishes"]

    def test_ell_6_vanishes(self):
        """ell_6 = 0 for Heisenberg."""
        h = heisenberg_higher_brackets(S.One)
        assert h["ell_6_vanishes"]

    def test_ell_5_scalar_zero(self):
        """ell_5 at scalar level is zero."""
        h = heisenberg_higher_brackets(S.One)
        assert simplify(h["ell_5_scalar"]) == 0

    def test_ell_6_scalar_zero(self):
        """ell_6 at scalar level is zero."""
        h = heisenberg_higher_brackets(S.One)
        assert simplify(h["ell_6_scalar"]) == 0

    def test_jacobi_5_satisfied(self):
        h = heisenberg_higher_brackets(S.One)
        assert h["jacobi5"]

    def test_jacobi_6_satisfied(self):
        h = heisenberg_higher_brackets(S.One)
        assert h["jacobi6"]

    def test_o6_scalar_zero(self):
        """Obstruction class o_6 = 0 for Heisenberg (scalar level)."""
        h = heisenberg_higher_brackets(S.One)
        assert simplify(h["o6_scalar"]) == 0

    def test_depth_class_G(self):
        """Heisenberg is depth class G, depth 2."""
        assert verify_depth_class("Heisenberg", "G", 2)["matches"]


# =========================================================================
# 10. Affine sl_2: class L
# =========================================================================

class TestAffineSl2:
    """Affine sl_2 (class L, depth 3): ell_k = 0 for k >= 4."""

    def test_ell_5_vanishes(self):
        a = affine_sl2_higher_brackets(S.One)
        assert a["ell_5_vanishes"]

    def test_ell_6_vanishes(self):
        a = affine_sl2_higher_brackets(S.One)
        assert a["ell_6_vanishes"]

    def test_ell_5_scalar_zero(self):
        a = affine_sl2_higher_brackets(S.One)
        assert simplify(a["ell_5_scalar"]) == 0

    def test_ell_6_scalar_zero(self):
        a = affine_sl2_higher_brackets(S.One)
        assert simplify(a["ell_6_scalar"]) == 0

    def test_jacobi_5_satisfied(self):
        a = affine_sl2_higher_brackets(S.One)
        assert a["jacobi5"]

    def test_jacobi_6_satisfied(self):
        a = affine_sl2_higher_brackets(S.One)
        assert a["jacobi6"]

    def test_depth_class_L(self):
        assert verify_depth_class("affine_sl2", "L", 3)["matches"]


# =========================================================================
# 11. Beta-gamma: class C
# =========================================================================

class TestBetaGamma:
    """Beta-gamma system (class C, depth 4): ell_5 = ell_6 = 0."""

    def test_ell_5_vanishes(self):
        """ell_5 = 0 for beta-gamma (class C terminates at arity 4)."""
        b = betagamma_higher_brackets()
        assert b["ell_5_vanishes"]

    def test_ell_6_vanishes(self):
        b = betagamma_higher_brackets()
        assert b["ell_6_vanishes"]

    def test_ell_5_scalar_zero(self):
        b = betagamma_higher_brackets()
        assert simplify(b["ell_5_scalar"]) == 0

    def test_ell_6_scalar_zero(self):
        b = betagamma_higher_brackets()
        assert simplify(b["ell_6_scalar"]) == 0

    def test_jacobi_5_satisfied(self):
        b = betagamma_higher_brackets()
        assert b["jacobi5"]

    def test_jacobi_6_satisfied(self):
        b = betagamma_higher_brackets()
        assert b["jacobi6"]

    def test_depth_class_C(self):
        assert verify_depth_class("betagamma", "C", 4)["matches"]


# =========================================================================
# 12. Virasoro: class M
# =========================================================================

class TestVirasoro:
    """Virasoro algebra (class M, infinite depth): all ell_k nonzero."""

    def test_ell_5_nonzero_vector(self):
        """ell_5 is nonzero at the vector level for Virasoro."""
        v = virasoro_higher_brackets(Rational(25, 1))
        assert v["ell_5_nonzero_vector"]

    def test_ell_6_nonzero_vector(self):
        """ell_6 is nonzero at the vector level for Virasoro."""
        v = virasoro_higher_brackets(Rational(25, 1))
        assert v["ell_6_nonzero_vector"]

    def test_ell_5_scalar_zero(self):
        """ell_5 at scalar level is zero (even for Virasoro)."""
        v = virasoro_higher_brackets(Rational(25, 1))
        assert simplify(v["ell_5_scalar"]) == 0

    def test_ell_6_scalar_zero(self):
        """ell_6 at scalar level is zero."""
        v = virasoro_higher_brackets(Rational(25, 1))
        assert simplify(v["ell_6_scalar"]) == 0

    def test_ell_5_does_not_vanish(self):
        """For class M, ell_5 does NOT vanish identically."""
        v = virasoro_higher_brackets(Rational(25, 1))
        assert not v["ell_5_vanishes"]

    def test_ell_6_does_not_vanish(self):
        v = virasoro_higher_brackets(Rational(25, 1))
        assert not v["ell_6_vanishes"]

    def test_jacobi_5_satisfied(self):
        v = virasoro_higher_brackets(Rational(25, 1))
        assert v["jacobi5"]

    def test_jacobi_6_satisfied(self):
        v = virasoro_higher_brackets(Rational(25, 1))
        assert v["jacobi6"]

    def test_mc_arity5_satisfied(self):
        """MC equation at arity 5 (scalar level)."""
        v = virasoro_higher_brackets(Rational(25, 1))
        assert simplify(v["mc_arity5"]) == 0

    def test_mc_arity6_satisfied(self):
        """MC equation at arity 6 (scalar level)."""
        v = virasoro_higher_brackets(Rational(25, 1))
        assert simplify(v["mc_arity6"]) == 0

    def test_mc_arity7_satisfied(self):
        v = virasoro_higher_brackets(Rational(25, 1))
        assert simplify(v["mc_arity7"]) == 0

    def test_mc_arity8_satisfied(self):
        v = virasoro_higher_brackets(Rational(25, 1))
        assert simplify(v["mc_arity8"]) == 0

    def test_depth_class_M(self):
        assert verify_depth_class("Virasoro", "M", None)["matches"]

    def test_shadow_S5_nonzero(self):
        """S_5 is nonzero for Virasoro (infinite tower)."""
        v = virasoro_higher_brackets(Rational(25, 1))
        assert simplify(v["S5"]) != 0

    def test_shadow_S6_nonzero(self):
        """S_6 is nonzero for Virasoro."""
        v = virasoro_higher_brackets(Rational(25, 1))
        assert simplify(v["S6"]) != 0

    def test_virasoro_c1(self):
        """Virasoro at c=1: concrete shadow values."""
        v = virasoro_higher_brackets(S.One)
        assert simplify(v["kappa"] - Rational(1, 2)) == 0
        assert v["jacobi5"]


# =========================================================================
# 13. MC equation at arities 5--8
# =========================================================================

class TestMCEquation:
    """MC equation at higher arities for all families."""

    def test_mc_heisenberg_arity5(self):
        shadows = {2: S.One}
        for r in range(3, 9):
            shadows[r] = S.Zero
        mc = mc_equation_full(shadows, 5, "G")
        assert mc["mc_satisfied"]

    def test_mc_heisenberg_arity6(self):
        shadows = {2: S.One}
        for r in range(3, 9):
            shadows[r] = S.Zero
        mc = mc_equation_full(shadows, 6, "G")
        assert mc["mc_satisfied"]

    def test_mc_virasoro_arity5(self):
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        mc = mc_equation_full(shadows, 5, "M")
        assert mc["mc_satisfied"]

    def test_mc_virasoro_arity6(self):
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        mc = mc_equation_full(shadows, 6, "M")
        assert mc["mc_satisfied"]

    def test_mc_virasoro_arity7(self):
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        mc = mc_equation_full(shadows, 7, "M")
        assert mc["mc_satisfied"]

    def test_mc_virasoro_arity8(self):
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        mc = mc_equation_full(shadows, 8, "M")
        assert mc["mc_satisfied"]

    def test_mc_all_contributions_present(self):
        """MC at arity 5 has contributions from ell_1 through ell_6."""
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        mc = mc_equation_full(shadows, 5, "M")
        assert "ell_1" in mc["contributions"]
        assert "ell_5" in mc["contributions"]
        assert "ell_6" in mc["contributions"]

    def test_binary_mc_virasoro_c10(self):
        """Binary MC recursion closes at c = 10 for arities 5--8."""
        shadows = virasoro_shadow_coefficients_extended(Rational(10, 1), 10)
        for r in range(5, 9):
            residual = scalar_mc_binary(shadows, r)
            assert simplify(residual) == 0, f"MC fails at arity {r}"


# =========================================================================
# 14. Obstruction class o_6
# =========================================================================

class TestObstructionClass:
    """Obstruction class o_6(A)."""

    def test_o6_heisenberg_scalar_zero(self):
        """o_6 at scalar level = 0 for Heisenberg."""
        shadows = {2: S.One}
        for r in range(3, 9):
            shadows[r] = S.Zero
        o6 = obstruction_class_o6(shadows, "G")
        assert simplify(o6["scalar_total"]) == 0

    def test_o6_virasoro_scalar_mc_satisfied(self):
        """o_6 scalar MC equation is satisfied for Virasoro."""
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        o6 = obstruction_class_o6(shadows, "M")
        assert o6["scalar_mc_satisfied"]

    def test_o6_virasoro_vector_nonzero(self):
        """o_6 is nonzero at the vector level for Virasoro (class M)."""
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        o6 = obstruction_class_o6(shadows, "M")
        assert o6["vector_nonzero"]

    def test_o6_betagamma_vector_zero(self):
        """o_6 = 0 for beta-gamma (class C, terminates at depth 4)."""
        shadows = {2: S.One}
        for r in range(3, 9):
            shadows[r] = S.Zero
        o6 = obstruction_class_o6(shadows, "C")
        assert not o6["vector_nonzero"]

    def test_o6_has_binary_terms(self):
        """o_6 for Virasoro has nonzero binary terms."""
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        o6 = obstruction_class_o6(shadows, "M")
        assert len(o6["binary_terms"]) > 0


# =========================================================================
# 15. Three-route verification
# =========================================================================

class TestThreeRoutes:
    """Three independent computation routes for ell_k."""

    def test_route_counts_ell5(self):
        """ell_5: Feynman C_5=42, HTT C_4=14, stable (2*6-5)!!=105."""
        result = verify_three_routes(5)
        assert result["route_a"]["count"] == 42   # C_5
        assert result["route_b"]["count"] == 14   # C_4
        assert result["route_c"]["count"] == 105  # (2*6-5)!! = 7!! = 105

    def test_route_counts_ell6(self):
        """ell_6: Feynman C_6=132, HTT C_5=42, stable (2*7-5)!!=945."""
        result = verify_three_routes(6)
        assert result["route_a"]["count"] == 132  # C_6
        assert result["route_b"]["count"] == 42   # C_5
        assert result["route_c"]["count"] == 945  # 9!! = 945

    def test_scalar_agreement_ell5(self):
        """All three routes agree at the scalar level for ell_5."""
        result = verify_three_routes(5)
        assert result["scalar_agreement"]

    def test_scalar_agreement_ell6(self):
        result = verify_three_routes(6)
        assert result["scalar_agreement"]

    def test_htt_tree_counts(self):
        """HTT tree counts: C_{k-1} for ell_k."""
        assert htt_ell5_tree_count() == 14  # C_4
        assert htt_ell6_tree_count() == 42  # C_5

    def test_htt_general(self):
        for k_val in range(3, 8):
            assert htt_tree_count(k_val) == catalan(k_val - 1)

    def test_stable_graph_counts(self):
        """Trivalent genus-0 stable graphs with n legs: (2n-5)!!."""
        assert genus0_stable_graph_count(3) == 1
        assert genus0_stable_graph_count(4) == 3
        assert genus0_stable_graph_count(5) == 15
        assert genus0_stable_graph_count(6) == 105
        assert genus0_stable_graph_count(7) == 945


# =========================================================================
# 16. Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency of bracket vanishing and depth ordering."""

    def test_depth_ordering(self):
        """G < L < C < M: bracket vanishing hierarchy."""
        result = cross_family_consistency(Rational(25, 1))
        assert result["depth_order_correct"]

    def test_all_jacobi_satisfied(self):
        """Jacobi identities at orders 5 and 6 satisfied for all families."""
        result = cross_family_consistency(Rational(25, 1))
        assert result["all_jacobi_satisfied"]

    def test_depth_class_inference(self):
        """Infer depth class from bracket vanishing."""
        assert depth_class_from_brackets(True, True, True, True) == ("G", 2)
        assert depth_class_from_brackets(False, True, True, True) == ("L", 3)
        assert depth_class_from_brackets(False, False, True, True) == ("C", 4)
        assert depth_class_from_brackets(False, False, False, False) == ("M", None)

    def test_depth_5_hypothetical(self):
        """A hypothetical depth-5 algebra (not in standard landscape)."""
        cls, depth = depth_class_from_brackets(False, False, False, True)
        assert cls == "?"
        assert depth == 5


# =========================================================================
# 17. Shadow obstruction tower extended coefficients
# =========================================================================

class TestShadowTowerExtended:
    """Virasoro shadow obstruction tower S_5 through S_8."""

    def test_S5_virasoro(self):
        """S_5 for Virasoro at c = 25: nonzero."""
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        assert simplify(shadows[5]) != 0

    def test_S6_virasoro(self):
        """S_6 for Virasoro at c = 25: nonzero."""
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        assert simplify(shadows[6]) != 0

    def test_S7_virasoro(self):
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        assert simplify(shadows[7]) != 0

    def test_S8_virasoro(self):
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        assert simplify(shadows[8]) != 0

    def test_tower_matches_existing(self):
        """Extended tower matches existing virasoro_shadow_coefficients."""
        from compute.lib.convolution_linf_algebra import virasoro_shadow_coefficients
        c_val = Rational(25, 1)
        old = virasoro_shadow_coefficients(c_val, 8)
        new = virasoro_shadow_coefficients_extended(c_val, 8)
        for r in range(2, 9):
            assert simplify(old.get(r, S.Zero) - new.get(r, S.Zero)) == 0, (
                f"Shadow S_{r} mismatch: old={old.get(r)}, new={new.get(r)}"
            )

    def test_mc_recursion_extended(self):
        """MC recursion holds at all arities through 10."""
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 12)
        for r in range(5, 11):
            residual = scalar_mc_binary(shadows, r)
            assert simplify(residual) == 0, f"MC fails at arity {r}"

    def test_tower_c1(self):
        """Shadow obstruction tower at c = 1."""
        shadows = virasoro_shadow_coefficients_extended(S.One, 8)
        assert simplify(shadows[2] - Rational(1, 2)) == 0
        assert simplify(shadows[3] - S(2)) == 0
        # S_4 = 10/(1 * 27) = 10/27
        assert simplify(shadows[4] - Rational(10, 27)) == 0


# =========================================================================
# 18. Depth classification
# =========================================================================

class TestDepthClassification:
    """Depth classification from bracket vanishing."""

    def test_heisenberg_depth(self):
        assert verify_depth_class("Heisenberg", "G", 2)["matches"]

    def test_affine_depth(self):
        assert verify_depth_class("affine_sl2", "L", 3)["matches"]

    def test_betagamma_depth(self):
        assert verify_depth_class("betagamma", "C", 4)["matches"]

    def test_virasoro_depth(self):
        assert verify_depth_class("Virasoro", "M", None)["matches"]

    def test_vector_bracket_vanishing_G(self):
        """Class G: ell_k vanishes for k >= 3."""
        vb = HigherVectorBracket({2: S.One}, "H", "G")
        assert vb.ell_k_vanishes(3)
        assert vb.ell_k_vanishes(4)
        assert vb.ell_k_vanishes(5)
        assert vb.ell_k_vanishes(6)

    def test_vector_bracket_vanishing_L(self):
        """Class L: ell_k vanishes for k >= 4."""
        vb = HigherVectorBracket({2: S.One}, "sl2", "L")
        assert not vb.ell_k_vanishes(3)  # ell_3 is nonzero
        assert vb.ell_k_vanishes(4)
        assert vb.ell_k_vanishes(5)
        assert vb.ell_k_vanishes(6)

    def test_vector_bracket_vanishing_C(self):
        """Class C: ell_k vanishes for k >= 5."""
        vb = HigherVectorBracket({2: S.One}, "bg", "C")
        assert not vb.ell_k_vanishes(3)
        assert not vb.ell_k_vanishes(4)
        assert vb.ell_k_vanishes(5)
        assert vb.ell_k_vanishes(6)

    def test_vector_bracket_vanishing_M(self):
        """Class M: no ell_k vanishes."""
        vb = HigherVectorBracket({2: c / 2}, "Vir", "M")
        for k_val in range(3, 10):
            assert not vb.ell_k_vanishes(k_val)


# =========================================================================
# 19. ell_5 on truncated theta
# =========================================================================

class TestEll5OnTheta:
    """ell_5 evaluated on Theta^{<=4}."""

    def test_heisenberg_vanishes(self):
        shadows = {2: S.One}
        for r in range(3, 9):
            shadows[r] = S.Zero
        result = ell_5_on_truncated_theta(shadows, "G")
        assert result["vanishes"]

    def test_virasoro_nonvanishing(self):
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 8)
        result = ell_5_on_truncated_theta(shadows, "M")
        assert not result["vanishes"]
        assert result["vector_nonzero"]
        assert result["scalar_value"] == S.Zero

    def test_betagamma_vanishes(self):
        shadows = {2: S.One}
        for r in range(3, 9):
            shadows[r] = S.Zero
        result = ell_5_on_truncated_theta(shadows, "C")
        assert result["vanishes"]


# =========================================================================
# 20. ell_6 on truncated theta
# =========================================================================

class TestEll6OnTheta:
    """ell_6 evaluated on Theta^{<=4}."""

    def test_heisenberg_vanishes(self):
        shadows = {2: S.One}
        for r in range(3, 9):
            shadows[r] = S.Zero
        result = ell_6_on_truncated_theta(shadows, "G")
        assert result["vanishes"]

    def test_virasoro_nonvanishing(self):
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 8)
        result = ell_6_on_truncated_theta(shadows, "M")
        assert not result["vanishes"]
        assert result["vector_nonzero"]

    def test_affine_vanishes(self):
        shadows = {2: Rational(3, 4) * 3}
        for r in range(3, 9):
            shadows[r] = S.Zero
        result = ell_6_on_truncated_theta(shadows, "L")
        assert result["vanishes"]


# =========================================================================
# 21. Higher bracket summary
# =========================================================================

class TestSummary:
    """Full summary function for higher brackets."""

    def test_heisenberg_summary(self):
        shadows = {2: S.One}
        for r in range(3, 9):
            shadows[r] = S.Zero
        s = higher_bracket_summary("Heisenberg", shadows, "G")
        assert s["ell_5_vanishes"]
        assert s["ell_6_vanishes"]
        assert s["jacobi5_satisfied"]
        assert s["jacobi6_satisfied"]
        assert s["ell_5_scalar_zero"]
        assert s["ell_6_scalar_zero"]

    def test_virasoro_summary(self):
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        s = higher_bracket_summary("Virasoro", shadows, "M")
        assert not s["ell_5_vanishes"]
        assert not s["ell_6_vanishes"]
        assert s["jacobi5_satisfied"]
        assert s["jacobi6_satisfied"]
        assert s["ell_5_scalar_zero"]
        assert s["ell_6_scalar_zero"]
        assert s["o6_vector_nonzero"]

    def test_mc_all_arities_in_summary(self):
        shadows = virasoro_shadow_coefficients_extended(Rational(25, 1), 10)
        s = higher_bracket_summary("Virasoro", shadows, "M")
        for r in range(5, 9):
            assert s["mc_satisfied"][r], f"MC fails at arity {r}"


# =========================================================================
# Additional cross-checks and edge cases
# =========================================================================

class TestEdgeCases:
    """Edge cases and cross-checks."""

    def test_catalan_recursion(self):
        """C_{n+1} = sum_{i=0}^n C_i * C_{n-i}."""
        for n in range(7):
            total = sum(catalan(i) * catalan(n - i) for i in range(n + 1))
            assert total == catalan(n + 1)

    def test_associahedron_vertex_count_is_catalan(self):
        """K_n has C_{n-2} vertices."""
        for n in range(3, 10):
            fv = associahedron_f_vector(n)
            assert fv[0] == catalan(n - 2), (
                f"K_{n} has {fv[0]} vertices, expected C_{n-2} = {catalan(n - 2)}"
            )

    def test_binary_tree_catalan_relation(self):
        """binary_tree_count(n) = C_{n-1}."""
        for n in range(2, 9):
            assert binary_tree_count(n) == catalan(n - 1)

    def test_ell_k_scalar_raises_on_wrong_input(self):
        """ell_k raises on wrong number of inputs."""
        sb = HigherScalarBracket({2: S.One})
        with pytest.raises(ValueError):
            sb.ell_5_scalar([S.One] * 4, [2] * 4)  # 4 inputs, not 5
        with pytest.raises(ValueError):
            sb.ell_6_scalar([S.One] * 5, [2] * 5)  # 5 inputs, not 6

    def test_mbar_0n_invalid(self):
        """M_bar_{0,n} raises for n < 3."""
        with pytest.raises(ValueError):
            mbar_0n_betti_extended(2)

    def test_associahedron_invalid(self):
        """K_n raises for n < 3."""
        with pytest.raises(ValueError):
            associahedron_f_vector(2)

    def test_virasoro_symbolic(self):
        """Virasoro at symbolic c: Jacobi still holds."""
        v = virasoro_higher_brackets(c)
        assert v["jacobi5"]
        assert v["jacobi6"]

    def test_graph_coeff_model(self):
        """Vector bracket graph coefficient: C_k * prod(a_i)."""
        vb = HigherVectorBracket({2: S.One}, "test", "M")
        g5 = vb.vector_bracket_graph_coeff(5, (2, 2, 2, 2, 2))
        assert g5 == catalan(5) * 2**5  # = 42 * 32 = 1344

        g6 = vb.vector_bracket_graph_coeff(6, (2, 2, 2, 2, 2, 2))
        assert g6 == catalan(6) * 2**6  # = 132 * 64 = 8448

    def test_ell_5_vector_effective_class_G(self):
        """Class G vector bracket: ell_5 = 0."""
        vb = HigherVectorBracket({2: S.One}, "H", "G")
        val = vb.ell_5_vector_effective([S.One] * 5, [2] * 5)
        assert simplify(val) == 0

    def test_ell_5_vector_effective_class_M(self):
        """Class M vector bracket: ell_5 nonzero."""
        vb = HigherVectorBracket({2: Rational(25, 2)}, "Vir", "M")
        val = vb.ell_5_vector_effective(
            [Rational(25, 2)] * 5, [2] * 5
        )
        assert simplify(val) != 0
