"""Tests for the Virasoro quartic contact coefficient Q^contact_Vir.

Extracts the FIRST Ring 2 nonlinear modular shadow coefficient for a
non-abelian algebra: Q^contact_Vir = 10/[c(5c+22)].

Verifies:
  1. Gram matrix derivation of ⟨Λ|Λ⟩ = c(5c+22)/10
  2. Quasi-primary condition L₁Λ = 0 with coefficient a = 3/5
  3. Quartic contact coefficient Q = 10/[c(5c+22)]
  4. Special values at c = 1, 13, 25, 26, -22/5
  5. Consistency with beta-gamma comparison
  6. Full quartic shadow Θ^≤4_Vir structure

Ground truth: nonlinear_modular_shadows.tex (Thm thm:nms-virasoro-quartic).
"""

import pytest
from sympy import Rational, Symbol, simplify, expand, factor, S

from compute.lib.virasoro_quartic_contact import (
    lambda_vir_norm,
    lambda_vir_norm_from_gram,
    quartic_contact_coefficient,
    quartic_shadow_full,
    verify_gram_derivation,
    verify_quasi_primary_condition,
    verify_special_values,
)

c = Symbol('c')


class TestLambdaNorm:
    """Verify ⟨Λ|Λ⟩ = c(5c+22)/10."""

    def test_formula(self):
        norm = lambda_vir_norm()
        expected = c * (5*c + 22) / 10
        assert simplify(norm - expected) == 0

    def test_from_gram_matrix(self):
        norm = lambda_vir_norm_from_gram()
        expected = c * (5*c + 22) / 10
        assert simplify(norm - expected) == 0

    def test_gram_matches_direct(self):
        result = verify_gram_derivation()
        assert result["match"]

    def test_positive_for_c_gt_0(self):
        """⟨Λ|Λ⟩ > 0 for c > 0 (unitary regime)."""
        for c_val in [1, 2, 10, 25, 26, 100]:
            val = lambda_vir_norm().subs(c, c_val)
            assert val > 0, f"Norm negative at c={c_val}"

    def test_vanishes_at_c0(self):
        assert lambda_vir_norm().subs(c, 0) == 0

    def test_vanishes_at_lee_yang(self):
        """⟨Λ|Λ⟩ = 0 at c = -22/5 (Lee-Yang): Λ decouples."""
        assert lambda_vir_norm().subs(c, Rational(-22, 5)) == 0


class TestQuasiPrimary:
    """Verify L₁Λ = 0 determines a = 3/5."""

    def test_coefficient(self):
        result = verify_quasi_primary_condition()
        assert result["a"] == Rational(3, 5)

    def test_L1_vanishes(self):
        result = verify_quasi_primary_condition()
        assert result["is_zero"]


class TestQuarticContact:
    """Verify Q^contact_Vir = 10/[c(5c+22)]."""

    def test_formula(self):
        Q = quartic_contact_coefficient()
        expected = 10 / (c * (5*c + 22))
        assert simplify(Q - expected) == 0

    def test_rational_function_of_c(self):
        Q = quartic_contact_coefficient()
        assert Q.is_rational_function(c)

    def test_positive_for_c_gt_0(self):
        for c_val in [1, 2, 10, 25, 26, 100]:
            val = quartic_contact_coefficient().subs(c, c_val)
            assert val > 0

    def test_at_c1(self):
        """Q(c=1) = 10/27."""
        Q = quartic_contact_coefficient().subs(c, 1)
        assert Q == Rational(10, 27)

    def test_at_c13(self):
        """Q(c=13) = 10/1131 (self-dual point)."""
        Q = quartic_contact_coefficient().subs(c, 13)
        assert Q == Rational(10, 1131)

    def test_at_c25(self):
        """Q(c=25) = 10/3675 = 2/735."""
        Q = quartic_contact_coefficient().subs(c, 25)
        assert Q == Rational(2, 735)

    def test_at_c26(self):
        """Q(c=26) = 10/3952 = 5/1976."""
        Q = quartic_contact_coefficient().subs(c, 26)
        assert Q == Rational(5, 1976)

    def test_diverges_at_c0(self):
        """Q → ∞ as c → 0 (degenerate Virasoro)."""
        from sympy import oo, limit
        Q = quartic_contact_coefficient()
        assert limit(Q, c, 0, '+') == oo

    def test_diverges_at_lee_yang(self):
        """Q diverges at c = -22/5 (Λ decouples, denominator vanishes)."""
        from sympy import oo, limit
        Q = quartic_contact_coefficient()
        lim = limit(Q, c, Rational(-22, 5))
        # At Lee-Yang, norm_Λ = 0, so Q = 1/0 = ∞
        assert lim in (oo, -oo, S.ComplexInfinity)


class TestFullQuarticShadow:
    """Verify Θ^≤4_Vir = (c/2)x² + 2x³ + Q·x⁴."""

    def test_hessian(self):
        x = Symbol('x')
        result = quartic_shadow_full()
        assert simplify(result["H (Hessian)"] - c/2 * x**2) == 0

    def test_cubic(self):
        x = Symbol('x')
        result = quartic_shadow_full()
        assert simplify(result["C (cubic)"] - 2*x**3) == 0

    def test_quartic_coefficient(self):
        result = quartic_shadow_full()
        Q = result["Q_coefficient"]
        assert simplify(Q - 10/(c*(5*c+22))) == 0

    def test_full_shadow_structure(self):
        x = Symbol('x')
        result = quartic_shadow_full()
        theta = result["Theta^<=4"]
        expected = c/2 * x**2 + 2*x**3 + 10/(c*(5*c+22)) * x**4
        assert simplify(theta - expected) == 0


class TestSpecialValues:
    """Verify Q at physically significant central charges."""

    def test_all_special_values(self):
        results = verify_special_values()
        for key, val in results.items():
            if isinstance(val, bool):
                assert val, f"Failed: {key}"

    def test_lee_yang_decoupling(self):
        """At c = -22/5, the Λ quasi-primary decouples from the algebra."""
        results = verify_special_values()
        assert results["Lee-Yang: Λ decouples"]

    def test_free_boson(self):
        """At c = 1 (free boson), Q = 10/27."""
        results = verify_special_values()
        assert results["Q(c=1) = 10/27"]


class TestComparisonWithBetaGamma:
    """Compare with the beta-gamma result μ_{βγ} = 0."""

    def test_virasoro_nonzero(self):
        """Q^contact_Vir ≠ 0 (unlike μ_{βγ} = 0 for beta-gamma)."""
        Q = quartic_contact_coefficient()
        # Q = 10/[c(5c+22)] is nonzero for generic c
        assert Q != 0

    def test_virasoro_nonabelian(self):
        """The difference: Virasoro has [T,T] = 2T ≠ 0 (non-abelian bracket).

        This is why Q ≠ 0: the Virasoro deformation is NOT rank-one rigid.
        The beta-gamma weight-changing class has [η,η] = 0 (abelian), giving μ = 0.
        """
        # T_{(1)}T = 2T (nonzero bracket)
        from compute.lib.virasoro_bar import virasoro_nth_product
        bracket = virasoro_nth_product(1)
        assert bracket.get("T", 0) == 2  # [T,T] = 2T ≠ 0

    def test_asymptotic_behavior(self):
        """Q ~ 2/(c²) for large c: quartic shadow weakens at large central charge."""
        Q = quartic_contact_coefficient()
        # For large c: 10/(c·(5c+22)) ~ 10/(5c²) = 2/c²
        # Verify the exact factored form
        Q_expanded = 10 / (5*c**2 + 22*c)
        assert simplify(Q_expanded - Q) == 0
        # Check asymptotic: Q * c² → 2 as c → ∞
        from sympy import limit, oo
        assert limit(Q * c**2, c, oo) == 2


class TestNumericalValues:
    """Exact rational values at integer central charges."""

    def test_table(self):
        """Compute Q at c = 1, 2, ..., 10."""
        Q = quartic_contact_coefficient()
        expected = {
            1: Rational(10, 27),      # 10/(1·27)
            2: Rational(10, 64),      # 10/(2·32) = 5/32
            3: Rational(10, 111),     # 10/(3·37)
            4: Rational(10, 168),     # 10/(4·42) = 5/84
            5: Rational(10, 235),     # 10/(5·47) = 2/47
            6: Rational(10, 312),     # 10/(6·52) = 5/156
        }
        for c_val, exp in expected.items():
            actual = Q.subs(c, c_val)
            assert actual == exp, f"Q(c={c_val}): {actual} ≠ {exp}"
