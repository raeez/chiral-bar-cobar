"""
Tests for modular shadow obstruction tower: higher-arity propagation and genus loop.

Verifies:
  1. All-arity master equation structure
  2. Quintic obstruction for all model families
  3. Genus loop operator Lambda_P
  4. Genus-1 Hessian correction delta H^(1)
  5. Virasoro loop ratio rho^(1) = 240/[c^3(5c+22)]
  6. Finite termination for primitive archetypes
  7. Virasoro infinite tower (quintic forced)
  8. Special value evaluations
  9. Cross-family comparison

Ground truth: nonlinear_modular_shadows.tex,
    Theorems thm:nms-all-arity-master-equation through thm:nms-beyond-ahat
"""

import pytest
from sympy import (
    Rational, Symbol, simplify, factor, limit, oo,
    binomial, S
)
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from modular_shadow_tower import (
    virasoro_hessian, virasoro_cubic, virasoro_quartic_contact,
    virasoro_propagator, genus_loop_1d,
    genus_loop_cubic_virasoro, genus_loop_quartic_virasoro,
    virasoro_genus1_hessian_correction, virasoro_loop_ratio,
    sewing_product_1d,
    quintic_obstruction_virasoro, quintic_obstruction_heisenberg,
    quintic_obstruction_affine, quintic_obstruction_betagamma,
    shadow_termination_arity, w3_genus1_hessian_correction,
)

c = Symbol('c')


# =========================================================================
# I. Quintic obstruction tests
# =========================================================================

class TestQuinticObstruction:
    """Tests for the quintic master equation o^(5) = {C, Q}_H."""

    def test_heisenberg_quintic_vanishes(self):
        """Heisenberg: C=Q=0 => o^(5)=0."""
        assert quintic_obstruction_heisenberg() == 0

    def test_affine_quintic_vanishes(self):
        """Affine sl2: Q=0 in minimal gauge => o^(5)=0."""
        assert quintic_obstruction_affine() == 0

    def test_betagamma_quintic_vanishes(self):
        """Beta-gamma: C=0 => o^(5)=0."""
        assert quintic_obstruction_betagamma() == 0

    def test_virasoro_quintic_nonzero(self):
        """Virasoro: o^(5) = {C, Q}_H != 0 for generic c."""
        o5 = quintic_obstruction_virasoro()
        # Should be nonzero symbolically
        assert simplify(o5) != 0

    def test_virasoro_quintic_formula(self):
        """Virasoro quintic obstruction: o^(5) = 480/[c^2(5c+22)]."""
        o5 = quintic_obstruction_virasoro()
        expected = Rational(480) / (c**2 * (5*c + 22))
        assert simplify(o5 - expected) == 0

    def test_virasoro_quintic_at_c1(self):
        """o^(5)_Vir at c=1: 480/(1*27) = 160/9."""
        o5 = quintic_obstruction_virasoro()
        val = o5.subs(c, 1)
        assert val == Rational(480, 27)
        assert val == Rational(160, 9)

    def test_virasoro_quintic_at_c13(self):
        """o^(5)_Vir at c=13 (self-dual point)."""
        o5 = quintic_obstruction_virasoro()
        val = o5.subs(c, 13)
        expected = Rational(480) / (169 * 87)
        assert simplify(val - expected) == 0

    def test_virasoro_quintic_large_c(self):
        """Asymptotic: o^(5) ~ 96/c^3 as c -> oo."""
        o5 = quintic_obstruction_virasoro()
        asymp = limit(o5 * c**3, c, oo)
        assert asymp == Rational(96)

    def test_quintic_poles(self):
        """o^(5)_Vir has poles at c=0 and c=-22/5."""
        o5 = quintic_obstruction_virasoro()
        assert limit(o5 * c**2, c, 0) != 0  # double pole at c=0
        assert not (o5.subs(c, Rational(-22, 5))).is_finite  # pole at c=-22/5


# =========================================================================
# II. Genus loop operator tests
# =========================================================================

class TestGenusLoopOperator:
    """Tests for Lambda_P: Sym^r -> Sym^{r-2}."""

    def test_loop_of_hessian_is_dim(self):
        """Lambda_P(H) = dim V on a 1d space: C(2,2)*P*H_coeff = 1*1 = 1."""
        H_coeff = virasoro_hessian()
        P = virasoro_propagator()
        # On 1d: Lambda_P(H_coeff * x^2) = C(2,2) * P * H_coeff = 1 * (2/c) * (c/2) = 1
        result = genus_loop_1d(H_coeff, 2, P)
        assert simplify(result - 1) == 0

    def test_loop_of_cubic(self):
        """Lambda_P(C_Vir) = 12/c * x (linear form on deformation space)."""
        lc = genus_loop_cubic_virasoro()
        expected = Rational(12) / c
        assert simplify(lc - expected) == 0

    def test_loop_of_quartic(self):
        """Lambda_P(Q_Vir) = 120/[c^2(5c+22)] * x^2."""
        lq = genus_loop_quartic_virasoro()
        expected = Rational(120) / (c**2 * (5*c + 22))
        assert simplify(lq - expected) == 0

    def test_genus_loop_1d_combinatorics(self):
        """Check C(r,2) factor for various ranks."""
        P = Rational(1)
        alpha = Rational(1)
        assert genus_loop_1d(alpha, 2, P) == 1  # C(2,2) = 1
        assert genus_loop_1d(alpha, 3, P) == 3  # C(3,2) = 3
        assert genus_loop_1d(alpha, 4, P) == 6  # C(4,2) = 6
        assert genus_loop_1d(alpha, 5, P) == 10  # C(5,2) = 10


# =========================================================================
# III. Genus-1 Hessian correction tests
# =========================================================================

class TestGenus1HessianCorrection:
    """Tests for delta H^(1) = Lambda_P(Q^(0))."""

    def test_hessian_correction_formula(self):
        """delta H^(1)_Vir = 120/[c^2(5c+22)]."""
        dH = virasoro_genus1_hessian_correction()
        expected = Rational(120) / (c**2 * (5*c + 22))
        assert simplify(dH - expected) == 0

    def test_hessian_correction_at_c1(self):
        """delta H^(1) at c=1: 120/27 = 40/9."""
        dH = virasoro_genus1_hessian_correction()
        assert dH.subs(c, 1) == Rational(120, 27)
        assert dH.subs(c, 1) == Rational(40, 9)

    def test_hessian_correction_at_c26(self):
        """delta H^(1) at c=26 (critical string)."""
        dH = virasoro_genus1_hessian_correction()
        val = dH.subs(c, 26)
        expected = Rational(120) / (676 * 152)
        assert simplify(val - expected) == 0

    def test_hessian_correction_not_proportional_to_kappa(self):
        """delta H^(1) / H^(0) is NOT constant => not determined by kappa."""
        rho = virasoro_loop_ratio()
        # If rho were constant (= some number), it would be proportional to kappa.
        # Check that it depends on c.
        val1 = rho.subs(c, 1)
        val2 = rho.subs(c, 2)
        assert val1 != val2

    def test_hessian_correction_heisenberg_zero(self):
        """Heisenberg: delta H^(1) = 0 (Q = 0)."""
        # Heisenberg has Q = 0, so Lambda_P(Q) = 0
        assert genus_loop_1d(0, 4, Rational(1)) == 0

    def test_correction_vanishes_at_large_c(self):
        """delta H^(1) -> 0 as c -> oo."""
        dH = virasoro_genus1_hessian_correction()
        assert limit(dH, c, oo) == 0

    def test_correction_positive_for_c_gt_0(self):
        """delta H^(1) > 0 for c > 0 (since 5c+22 > 0 for c > 0)."""
        dH = virasoro_genus1_hessian_correction()
        for cv in [Rational(1, 10), 1, 5, 13, 25, 100]:
            assert dH.subs(c, cv) > 0


# =========================================================================
# IV. Loop ratio tests
# =========================================================================

class TestLoopRatio:
    """Tests for rho^(1) = delta H^(1) / H^(0)."""

    def test_loop_ratio_formula(self):
        """rho^(1)_Vir = 240/[c^3(5c+22)]."""
        rho = virasoro_loop_ratio()
        expected = Rational(240) / (c**3 * (5*c + 22))
        assert simplify(rho - expected) == 0

    def test_loop_ratio_at_c1(self):
        """rho^(1) at c=1: 240/27 = 80/9."""
        rho = virasoro_loop_ratio()
        assert rho.subs(c, 1) == Rational(240, 27)

    def test_loop_ratio_at_c13(self):
        """rho^(1) at c=13 (self-dual)."""
        rho = virasoro_loop_ratio()
        val = rho.subs(c, 13)
        expected = Rational(240) / (2197 * 87)
        assert simplify(val - expected) == 0

    def test_loop_ratio_large_c(self):
        """rho^(1) ~ 48/c^4 for large c."""
        rho = virasoro_loop_ratio()
        assert limit(rho * c**4, c, oo) == Rational(48)

    def test_loop_ratio_distinguishes_same_kappa(self):
        """
        Two values of c with same kappa = c/2 have different rho^(1).
        This proves the loop ratio carries information beyond kappa.

        Well, c determines kappa = c/2 uniquely, so same kappa means same c.
        But the POINT is that rho^(1) is a different function of c than kappa:
        rho = 240/(c^3(5c+22)) while kappa = c/2.
        So rho/kappa = 480/(c^4(5c+22)) is nontrivial.
        """
        rho = virasoro_loop_ratio()
        kappa = c / 2
        ratio = simplify(rho / kappa)
        # This should be 480/[c^4(5c+22)], not constant
        val1 = ratio.subs(c, 1)
        val2 = ratio.subs(c, 10)
        assert val1 != val2


# =========================================================================
# V. Finite termination tests
# =========================================================================

class TestFiniteTermination:
    """Tests for shadow obstruction tower termination behavior."""

    def test_heisenberg_terminates_at_2(self):
        """Heisenberg: exact Gaussian, terminates at arity 2."""
        terms = shadow_termination_arity()
        assert terms['heisenberg'] == 2

    def test_affine_terminates_at_3(self):
        """Affine sl2: Lie/tree archetype, terminates at arity 3."""
        terms = shadow_termination_arity()
        assert terms['affine_sl2'] == 3

    def test_betagamma_terminates_at_4(self):
        """Beta-gamma: contact/quartic archetype, terminates at arity 4."""
        terms = shadow_termination_arity()
        assert terms['betagamma'] == 4

    def test_virasoro_infinite(self):
        """Virasoro: infinite tower (None = no termination)."""
        terms = shadow_termination_arity()
        assert terms['virasoro'] is None

    def test_virasoro_quintic_nonzero_implies_infinite(self):
        """If o^(5) != 0, Sh_5 != 0, which by induction forces infinite tower."""
        o5 = quintic_obstruction_virasoro()
        assert simplify(o5) != 0
        # o^(5) != 0 => Sh_5 != 0 (by master equation)
        # Sh_5 != 0 => o^(6) contains {C, Sh_5} != 0 => Sh_6 != 0
        # By induction: Sh_r != 0 for all r >= 5

    def test_archetype_ordering(self):
        """Termination arities are strictly ordered: 2 < 3 < 4 < infinity."""
        terms = shadow_termination_arity()
        assert terms['heisenberg'] < terms['affine_sl2']
        assert terms['affine_sl2'] < terms['betagamma']
        # Virasoro is infinite (None), strictly greater than all finite values


# =========================================================================
# VI. Sewing product tests
# =========================================================================

class TestSewingProduct:
    """Tests for the single-edge sewing contraction."""

    def test_sewing_symmetric(self):
        """Sewing is symmetric: {alpha, beta} = {beta, alpha} on 1d."""
        P = Rational(1)
        a, b = Rational(3), Rational(7)
        s1 = sewing_product_1d(a, 3, b, 4, P)
        s2 = sewing_product_1d(b, 4, a, 3, P)
        assert s1 == s2

    def test_sewing_cubic_cubic(self):
        """
        {C,C}_H for Virasoro: sewing two cubics.
        C = 2x^3, P = 2/c.
        {C,C} = 3*3 * (2/c) * 2 * 2 * x^4 = 36 * (2/c) * x^4... wait.

        Actually: {C,C}(x^4) = p*q * P * C_coeff^2 = 3*3*(2/c)*4 = 36*2/c.
        Hmm, let me use the function directly.
        """
        C_coeff = virasoro_cubic()
        P = virasoro_propagator()
        sewing = sewing_product_1d(C_coeff, 3, C_coeff, 3, P)
        # = 3 * 3 * (2/c) * 2 * 2 = 72/c
        assert simplify(sewing - Rational(72) / c) == 0

    def test_quartic_obstruction_from_sewing(self):
        """o^(4) = (1/2){C,C}_H. For Virasoro: (1/2)*72/c = 36/c."""
        C_coeff = virasoro_cubic()
        P = virasoro_propagator()
        sewing = sewing_product_1d(C_coeff, 3, C_coeff, 3, P)
        o4 = sewing / 2
        assert simplify(o4 - Rational(36) / c) == 0


# =========================================================================
# VII. Cross-consistency tests
# =========================================================================

class TestCrossConsistency:
    """Cross-checks between different computations."""

    def test_quintic_equals_sewing_CQ(self):
        """o^(5) should equal {C, Q}_H (coefficient 1 since p<q)."""
        o5 = quintic_obstruction_virasoro()
        C_coeff = virasoro_cubic()
        Q_coeff = virasoro_quartic_contact()
        P = virasoro_propagator()
        sewing_CQ = sewing_product_1d(C_coeff, 3, Q_coeff, 4, P)
        assert simplify(o5 - sewing_CQ) == 0

    def test_propagator_inverts_hessian(self):
        """P * H = 1 on the 1d primary line."""
        H = virasoro_hessian()
        P = virasoro_propagator()
        assert simplify(H * P - 1) == 0

    def test_loop_of_hessian_matches_dim(self):
        """Lambda_P(H) = dim V = 1 on a 1d space."""
        H = virasoro_hessian()
        P = virasoro_propagator()
        result = genus_loop_1d(H, 2, P)
        assert simplify(result - 1) == 0

    def test_genus_loop_from_quartic_contact_coefficient(self):
        """
        Cross-check: Q_0 = 10/[c(5c+22)], P = 2/c,
        Lambda_P(Q_0 x^4) = 6 * (2/c) * Q_0 = 120/[c^2(5c+22)].
        """
        Q0 = virasoro_quartic_contact()
        P = virasoro_propagator()
        dH = 6 * P * Q0  # binomial(4,2) * P * Q0
        expected = Rational(120) / (c**2 * (5*c + 22))
        assert simplify(dH - expected) == 0

    def test_virasoro_loop_ratio_from_direct_computation(self):
        """Direct: rho = (12*Q0/c) / (c/2) = 24*Q0/c^2."""
        Q0 = virasoro_quartic_contact()
        rho_direct = 24 * Q0 / c**2
        # Wait: delta_H = 12*Q0/c, H = c/2, rho = (12*Q0/c)/(c/2) = 24*Q0/c^2
        # = 24*10/[c^3(5c+22)] = 240/[c^3(5c+22)]
        expected = Rational(240) / (c**3 * (5*c + 22))
        assert simplify(rho_direct - expected) == 0


# =========================================================================
# VIII. Special value tests
# =========================================================================

class TestSpecialValues:
    """Numerical evaluations at physically significant central charges."""

    def test_at_c_half(self):
        """c = 1/2 (Ising model)."""
        dH = virasoro_genus1_hessian_correction()
        val = dH.subs(c, Rational(1, 2))
        expected = Rational(120) / (Rational(1, 4) * Rational(49, 2))
        assert simplify(val - expected) == 0

    def test_at_c25(self):
        """c = 25 (bosonic string ghost complement)."""
        dH = virasoro_genus1_hessian_correction()
        val = dH.subs(c, 25)
        expected = Rational(120) / (625 * 147)
        assert simplify(val - expected) == 0

    def test_at_c26(self):
        """c = 26 (critical bosonic string)."""
        rho = virasoro_loop_ratio()
        val = rho.subs(c, 26)
        expected = Rational(240) / (26**3 * 152)
        assert simplify(val - expected) == 0

    def test_selfdual_c13(self):
        """c = 13 (self-dual point, Vir_c^! = Vir_{26-c})."""
        dH = virasoro_genus1_hessian_correction()
        val = dH.subs(c, 13)
        expected = Rational(120) / (169 * 87)
        assert simplify(val - expected) == 0

    def test_lee_yang_pole(self):
        """c = -22/5 (Lee-Yang): pole in quartic contact => pole in loop."""
        dH = virasoro_genus1_hessian_correction()
        # Should diverge at c = -22/5
        assert not dH.subs(c, Rational(-22, 5)).is_finite


# =========================================================================
# IX. W3 tests
# =========================================================================

class TestW3GenusLoop:
    """Tests for W3 genus-1 Hessian correction."""

    def test_w3_tt_correction_formula(self):
        """W3 delta_H_tt = 6 * (2/c) * 16/(22+5c) = 192/[c(22+5c)]."""
        result = w3_genus1_hessian_correction()
        expected = Rational(192) / (c * (22 + 5*c))
        assert simplify(result['delta_H_tt'] - expected) == 0

    def test_w3_tt_at_c1(self):
        """W3 delta_H_tt at c=1: 192/27."""
        result = w3_genus1_hessian_correction()
        val = result['delta_H_tt'].subs(c, 1)
        assert val == Rational(192, 27)
