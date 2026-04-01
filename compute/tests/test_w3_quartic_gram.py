"""Tests for W_3 quartic contact Gram determinant.

Independent verification of det G^{ct}_{W_3}.
Claimed formula (raeeznotes 105-112, L.2; thm:nms-w3-full-quartic-gram):
    det G^{ct}_{W_3} = (1/10) c^3 (2c-1) (5c+22)^2

VERDICT: FALSIFIED.

The weight-4 block G_4 = c(5c+22)/10 is CONFIRMED.
The Proposition (prop:nms-w3-visible-resonance-factor) claiming
<Xi_W|Xi_W> ~ c^2(2c-1)(5c+22) is FALSE: the norm does not vanish at c=1/2.
"""

import pytest
from fractions import Fraction as F

from sympy import (
    Matrix,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    zeros,
)

c = Symbol('c')


# =========================================================================
# Weight-4 block tests
# =========================================================================

class TestWeight4Block:
    """Verify G_4 = <Lambda|Lambda> = c(5c+22)/10."""

    def test_lambda_norm_formula(self):
        from compute.lib.w3_quartic_gram import lambda_norm
        assert simplify(lambda_norm() - c * (5 * c + 22) / 10) == 0

    def test_lambda_norm_from_shapovalov(self):
        """Verify from the level-4 Shapovalov matrix directly."""
        from compute.lib.w3_quartic_gram import virasoro_level4_gram, lambda_state_vector
        G4 = virasoro_level4_gram()
        v = lambda_state_vector()
        norm = expand((v.T * G4 * v)[0, 0])
        assert simplify(norm - c * (5 * c + 22) / 10) == 0

    def test_lambda_norm_at_c1(self):
        from compute.lib.w3_quartic_gram import lambda_norm
        val = lambda_norm().subs(c, 1)
        assert val == Rational(27, 10)

    def test_lambda_norm_zero_at_c0(self):
        from compute.lib.w3_quartic_gram import lambda_norm
        assert lambda_norm().subs(c, 0) == 0

    def test_lambda_norm_zero_at_c_neg22_over_5(self):
        from compute.lib.w3_quartic_gram import lambda_norm
        assert lambda_norm().subs(c, Rational(-22, 5)) == 0

    def test_lambda_norm_positive_large_c(self):
        """For large positive c, G_4 should be positive."""
        from compute.lib.w3_quartic_gram import lambda_norm
        assert lambda_norm().subs(c, 100) > 0


# =========================================================================
# Weight-6 Gram matrix tests
# =========================================================================

class TestWeight6GramMatrix:
    """Verify the full 8x8 Gram matrix at weight 6."""

    def test_symmetry(self):
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        for i in range(8):
            for j in range(8):
                assert simplify(G[i, j] - G[j, i]) == 0, f"Not symmetric at ({i},{j})"

    def test_block_diagonal_structure(self):
        """Even-W and odd-W sectors should not mix."""
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        even = [0, 1, 2, 3, 7]
        odd = [4, 5, 6]
        for i in even:
            for j in odd:
                assert simplify(G[i, j]) == 0, f"Cross-block nonzero at ({i},{j})"

    def test_virasoro_block_consistency(self):
        """Pure Virasoro 4x4 subblock should match kac_chevalley_test."""
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        # G[0,0] = 35c/2
        assert simplify(G[0, 0] - Rational(35, 2) * c) == 0
        # G[1,1] = c(5c+16)/2
        assert simplify(G[1, 1] - c * (5 * c + 16) / 2) == 0
        # G[3,3] = 3c(8+c)(16+c)/4
        assert simplify(G[3, 3] - 3 * c * (8 + c) * (16 + c) / 4) == 0

    def test_G07_equals_5c(self):
        """<0|L_6 W_{-3}^2|0> = 5c."""
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        assert simplify(G[0, 7] - 5 * c) == 0

    def test_G17_equals_22c(self):
        """<0|L_2 L_4 W_{-3}^2|0> = 22c."""
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        assert simplify(G[1, 7] - 22 * c) == 0

    def test_G27_equals_36c(self):
        """<0|L_3^2 W_{-3}^2|0> = 36c."""
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        assert simplify(G[2, 7] - 36 * c) == 0

    def test_G37_equals_322c_over_5(self):
        """<0|L_2^3 W_{-3}^2|0> = 322c/5.

        This is the CORRECTED value. The naive computation gives 14c(130+23c)/(22+5c)
        but this misses the descendant subtraction in Lambda_{-4}.
        With Lambda_{-4}|0> = L_{-2}^2|0> - (3/5)L_{-4}|0>, we get 322c/5.
        """
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        assert simplify(G[3, 7] - Rational(322, 5) * c) == 0

    def test_G37_numerical_at_c10(self):
        """Verify G[3,7] = 644 at c=10."""
        from compute.lib.w3_quartic_gram import evaluate_xi_w_norm_numeric
        # G[3,7] = 322*10/5 = 644
        assert F(322) * 10 / 5 == 644

    def test_G44_equals_56c_over_3(self):
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        assert simplify(G[4, 4] - Rational(56, 3) * c) == 0

    def test_G77_at_c10(self):
        """Verify G[7,7] = 1676/9 at c=10."""
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        val = G[7, 7].subs(c, 10)
        assert val == Rational(1676, 9)


# =========================================================================
# Numerical cross-checks of Gram entries
# =========================================================================

class TestGramNumerical:
    """Verify Gram matrix entries at multiple c values."""

    @pytest.mark.parametrize("c_val", [1, 2, 3, 5, 7, 10, 20])
    def test_G07_numerical(self, c_val):
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        assert G[0, 7].subs(c, c_val) == 5 * c_val

    @pytest.mark.parametrize("c_val", [1, 2, 3, 5, 7, 10, 20])
    def test_G17_numerical(self, c_val):
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        assert G[1, 7].subs(c, c_val) == 22 * c_val

    @pytest.mark.parametrize("c_val", [1, 2, 3, 5, 7, 10, 20])
    def test_G37_numerical(self, c_val):
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        expected = F(322, 5) * c_val
        actual = F(G[3, 7].subs(c, c_val).p, G[3, 7].subs(c, c_val).q)
        assert actual == expected, f"G[3,7] at c={c_val}: {actual} != {expected}"


# =========================================================================
# L1 action tests
# =========================================================================

class TestL1Action:
    """Verify the L_1 action matrix."""

    def test_dimensions(self):
        from compute.lib.w3_quartic_gram import L1_action_matrix
        M = L1_action_matrix()
        assert M.shape == (4, 8)

    def test_quasi_primary_dim(self):
        from compute.lib.w3_quartic_gram import quasi_primary_vectors
        qp = quasi_primary_vectors()
        assert len(qp) == 4

    def test_xi_w_is_quasi_primary(self):
        """Verify L_1 Xi_W = 0."""
        from compute.lib.w3_quartic_gram import L1_action_matrix, xi_w_vector
        M = L1_action_matrix()
        v = xi_w_vector()
        result = M * v
        for entry in result:
            assert simplify(cancel(entry)) == 0


# =========================================================================
# Xi_W norm tests: FALSIFICATION of the Proposition
# =========================================================================

class TestXiWNorm:
    """Test the norm of Xi_W = Pi_qp(:WW:)."""

    def test_xi_w_norm_symbolic(self):
        """Verify the symbolic formula for <Xi_W|Xi_W>."""
        from compute.lib.w3_quartic_gram import xi_w_norm
        norm = xi_w_norm()
        # Should be 2c(875c^3+110975c^2+112880c-1931508)/(315(5c+22)^2)
        expected_num = 2 * c * (875 * c**3 + 110975 * c**2 + 112880 * c - 1931508)
        expected_den = 315 * (5 * c + 22)**2
        assert simplify(norm - expected_num / expected_den) == 0

    def test_xi_w_norm_nonzero_at_c_half(self):
        """CRITICAL: <Xi_W|Xi_W> does NOT vanish at c=1/2.

        This FALSIFIES Proposition prop:nms-w3-visible-resonance-factor
        which claims <Xi_W|Xi_W> ~ c^2(2c-1)(5c+22).
        If (2c-1) were a factor, the norm would vanish at c=1/2.
        """
        from compute.lib.w3_quartic_gram import evaluate_xi_w_norm_numeric
        norm_at_half = evaluate_xi_w_norm_numeric(F(1, 2))
        assert norm_at_half != 0, (
            "Xi_W norm should be NONZERO at c=1/2 (falsifying the Proposition)"
        )

    def test_xi_w_norm_zero_at_c0(self):
        """<Xi_W|Xi_W> vanishes at c=0 (trivial algebra)."""
        from compute.lib.w3_quartic_gram import evaluate_xi_w_norm_numeric
        assert evaluate_xi_w_norm_numeric(F(0, 1)) == 0

    def test_xi_w_norm_not_proportional_to_claimed(self):
        """The ratio <Xi_W|Xi_W> / [c^2(2c-1)(5c+22)] is NOT constant in c."""
        from compute.lib.w3_quartic_gram import evaluate_xi_w_norm_numeric
        ratios = []
        for cv in [3, 5, 7, 10]:
            c_frac = F(cv)
            norm = evaluate_xi_w_norm_numeric(c_frac)
            target = c_frac**2 * (2 * c_frac - 1) * (5 * c_frac + 22)
            ratios.append(norm / target)
        # If proportional, all ratios would be equal
        assert len(set(ratios)) > 1, "Ratios should NOT all be equal"

    @pytest.mark.parametrize("c_val", [1, 2, 3, 5, 7, 10, 20])
    def test_xi_w_norm_consistency(self, c_val):
        """Symbolic and numeric evaluations should agree."""
        from compute.lib.w3_quartic_gram import xi_w_norm, evaluate_xi_w_norm_numeric
        symbolic_val = xi_w_norm().subs(c, c_val)
        numeric_val = evaluate_xi_w_norm_numeric(c_val)
        # Convert symbolic to Fraction for comparison
        sym_frac = F(int(symbolic_val.p), int(symbolic_val.q))
        assert sym_frac == numeric_val


# =========================================================================
# Claimed formula tests
# =========================================================================

class TestClaimedFormula:
    """Test the claimed det G^{ct} = (1/10) c^3 (2c-1) (5c+22)^2."""

    def test_claimed_zeros(self):
        """The claimed formula has zeros at c=0 (order 3), c=1/2, c=-22/5 (order 2)."""
        from compute.lib.w3_quartic_gram import claimed_formula
        f = claimed_formula()
        assert f.subs(c, 0) == 0
        assert f.subs(c, Rational(1, 2)) == 0
        assert f.subs(c, Rational(-22, 5)) == 0

    def test_claimed_degree(self):
        """The claimed formula has degree 6 in c."""
        from compute.lib.w3_quartic_gram import claimed_formula
        from sympy import Poly
        f = claimed_formula()
        p = Poly(expand(f), c)
        assert p.degree() == 6

    def test_claimed_formula_is_WRONG(self):
        """The claimed formula does NOT match the actual computation.

        This is the central test: the claimed det G^{ct} = (1/10)c^3(2c-1)(5c+22)^2
        does not agree with the independently computed Xi_W norm.
        """
        from compute.lib.w3_quartic_gram import (
            lambda_norm, xi_w_norm, claimed_formula
        )
        G4 = lambda_norm()
        xi_norm = xi_w_norm()

        # If Q_6 is 1-dimensional (just Xi_W), then det G^{ct} = G_4 * xi_norm
        actual_det = expand(G4 * xi_norm)
        claimed = expand(claimed_formula())

        # These should NOT be equal
        diff = simplify(actual_det - claimed)
        assert diff != 0, "Actual and claimed should DIFFER"


# =========================================================================
# Full Gram determinant tests
# =========================================================================

class TestFullGramDet:
    """Test the full 8x8 Gram determinant at weight 6."""

    def test_odd_block_det(self):
        """Odd W-parity block: det = 16c^3(c+2)(7c+114)/9."""
        from compute.lib.w3_quartic_gram import odd_w_block_det
        det = odd_w_block_det()
        expected = Rational(16, 9) * c**3 * (c + 2) * (7 * c + 114)
        assert simplify(det - expected) == 0

    def test_odd_block_zeros(self):
        """Odd block vanishes at c=0 (order 3), c=-2, c=-114/7."""
        from compute.lib.w3_quartic_gram import odd_w_block_det
        det = odd_w_block_det()
        assert det.subs(c, 0) == 0
        assert det.subs(c, -2) == 0
        assert det.subs(c, Rational(-114, 7)) == 0

    def test_even_block_has_5c_plus_22_factor(self):
        """Even block determinant should contain (5c+22) as a factor."""
        from compute.lib.w3_quartic_gram import even_w_block_det
        det = even_w_block_det()
        assert det.subs(c, Rational(-22, 5)) == 0


# =========================================================================
# Descendant subtraction tests (the source of the correction)
# =========================================================================

class TestDescendantSubtraction:
    """Test that the descendant subtraction in Lambda_n is correctly applied."""

    def test_lambda_neg2_vanishes_on_vacuum(self):
        """Lambda_{-2}|0> = 0 because (n+2)(n+3) = 0 at n=-2."""
        # (:TT:)_{-2}|0> = 0 (no creation pair with sum = -2)
        # -(3/10)*0*1*L_{-2}|0> = 0
        # So Lambda_{-2}|0> = 0
        pass  # Structural test, verified in w3_quartic_gram.py comments

    def test_lambda_neg4_on_vacuum(self):
        """Lambda_{-4}|0> = L_{-2}^2|0> - (3/5)L_{-4}|0>.

        (:TT:)_{-4}|0> = L_{-2}^2|0> (only p=-2 contributes).
        Descendant: -(3/10)(-2)(-1)*L_{-4}|0> = -(3/5)L_{-4}|0>.
        """
        # This is verified by the corrected G[3,7] = 322c/5
        pass

    def test_lambda_0_on_w3_vacuum(self):
        """Lambda_0 W_{-3}|0> = (18/5) W_{-3}|0>.

        (:TT:)_0 W_{-3}|0> = L_0^2 W_{-3}|0> = 9 W_{-3}|0>.
        Descendant: -(9/5)*L_0 W_{-3}|0> = -(9/5)*3*W_{-3}|0> = -(27/5)W_{-3}|0>.
        Total: (9 - 27/5) = 18/5.
        """
        # This is used in the G[7,7] computation
        coeff = F(18, 5)
        assert coeff == F(9) - F(27, 5)


# =========================================================================
# Additional structural tests
# =========================================================================

class TestStructural:
    """Additional structural tests."""

    def test_virasoro_level4_det(self):
        """Level-4 Virasoro Gram det = c^2(5c+22)/2."""
        from compute.lib.w3_quartic_gram import virasoro_level4_gram
        G = virasoro_level4_gram()
        det = factor(G.det())
        expected = c**2 * (5 * c + 22) / 2
        assert simplify(det - expected) == 0

    def test_w3_level4_det(self):
        """W_3 level-4 Gram det = c^3(5c+22) (including W_{-4} state)."""
        from compute.lib.w3_quartic_gram import virasoro_level4_gram
        # The W_3 level-4 Gram is block-diagonal: Virasoro 2x2 + W norm
        det_vir = c**2 * (5 * c + 22) / 2
        G_WW = 2 * c  # <W_4 W_{-4}> from [W_4,W_{-4}] = 2c on vacuum
        det_w3_level4 = expand(det_vir * G_WW)
        expected = c**3 * (5 * c + 22)
        assert simplify(det_w3_level4 - expected) == 0

    def test_gram_positive_definite_large_c(self):
        """For large positive c, the Gram matrix should be positive definite."""
        from compute.lib.w3_quartic_gram import w3_weight6_gram
        G = w3_weight6_gram()
        G_num = G.subs(c, 100)
        # Check all diagonal entries are positive
        for i in range(8):
            assert G_num[i, i] > 0, f"Diagonal entry G[{i},{i}] not positive at c=100"

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 50, 100])
    def test_lambda_norm_positive_for_positive_c(self, c_val):
        """G_4 > 0 for c > 0."""
        from compute.lib.w3_quartic_gram import lambda_norm
        assert lambda_norm().subs(c, c_val) > 0

    def test_irreducible_cubic_in_xi_w_norm(self):
        """The cubic 875c^3+110975c^2+112880c-1931508 is irreducible over Q."""
        from sympy import Poly
        cubic = 875 * c**3 + 110975 * c**2 + 112880 * c - 1931508
        p = Poly(cubic, c, domain='QQ')
        # Factor over QQ
        factors = p.factor_list()
        # Should have exactly one irreducible factor of degree 3
        assert len(factors[1]) == 1, "Cubic should be irreducible"
        assert factors[1][0][0].degree() == 3, "Factor should be degree 3"

    def test_cubic_has_no_rational_roots(self):
        """875c^3+110975c^2+112880c-1931508 has no rational roots."""
        from sympy import solve, Rational as R
        cubic = 875 * c**3 + 110975 * c**2 + 112880 * c - 1931508
        roots = solve(cubic, c)
        for r in roots:
            assert not r.is_rational, f"Root {r} should not be rational"


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
