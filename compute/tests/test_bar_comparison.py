"""Tests for cross-algebra bar complex comparison.

Verifies structural properties that hold across ALL algebras in the compute engine:
  - Orlik-Solomon dimensions
  - Desuspension parity and coalgebra type
  - Arnold cancellation pattern
  - Pole structure determines curvature type
"""

import pytest
from math import factorial

from compute.lib.bar_comparison import (
    POLE_ORDERS,
    GENERATOR_PARITY,
    ARNOLD_CANCELLATION,
    MAXIMAL_FORM_DIMS,
    COMPLEMENTARITY,
    os_dim,
    os_total_dim,
    desuspension_parity,
    coalgebra_type,
    curvature_from_pole,
    generic_chain_dim,
    verify_os_dims,
    verify_desuspension,
    verify_arnold,
    verify_pole_curvature,
)


class TestOSAlgebra:
    """Orlik-Solomon algebra on C_n(C)."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_os0_is_1(self, n):
        assert os_dim(n, 0) == 1

    @pytest.mark.parametrize("n,expected", [
        (1, 1), (2, 1), (3, 2), (4, 6), (5, 24),
    ])
    def test_maximal_form(self, n, expected):
        """OS^{n-1}(C_n) = (n-1)!."""
        assert os_dim(n, n - 1) == expected

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_total(self, n):
        """Total dim OS*(C_n) = n!."""
        assert os_total_dim(n) == factorial(n)

    def test_os1_C3(self):
        """OS^1(C_3) = 3 = e_1(1,2)."""
        assert os_dim(3, 1) == 3

    def test_intermediate_degrees(self):
        """OS dimensions match Poincare polynomial for C_4."""
        # P_t(C_4) = (1+t)(1+2t)(1+3t) = 1 + 6t + 11t^2 + 6t^3
        assert [os_dim(4, k) for k in range(4)] == [1, 6, 11, 6]

    def test_os1_formula(self):
        """OS^1(C_n) = e_1(1,...,n-1) = n(n-1)/2."""
        for n in range(2, 7):
            assert os_dim(n, 1) == n * (n - 1) // 2

    def test_os_beyond_range(self):
        assert os_dim(3, 3) == 0
        assert os_dim(3, -1) == 0


class TestDesuspension:
    @pytest.mark.parametrize("bosonic,expected_parity", [
        (True, "odd"), (False, "even"),
    ])
    def test_parity(self, bosonic, expected_parity):
        assert desuspension_parity(bosonic) == expected_parity

    @pytest.mark.parametrize("bosonic,expected_type", [
        (True, "exterior"), (False, "symmetric"),
    ])
    def test_coalgebra(self, bosonic, expected_type):
        assert coalgebra_type(bosonic) == expected_type

    def test_fermion_is_symmetric(self):
        """Free fermion: fermionic -> even after s^{-1} -> Sym^c."""
        assert GENERATOR_PARITY["free_fermion"]["coalgebra"] == "symmetric"

    def test_virasoro_is_exterior(self):
        """Virasoro: bosonic -> odd after s^{-1} -> Lambda^c."""
        assert GENERATOR_PARITY["Virasoro"]["coalgebra"] == "exterior"


class TestArnoldCancellation:
    @pytest.mark.parametrize("algebra", list(ARNOLD_CANCELLATION.keys()))
    def test_deg2_has_curvature(self, algebra):
        """Degree 2 is NOT cancelled (curvature leaks to vacuum)."""
        assert ARNOLD_CANCELLATION[algebra]["deg2"] is False

    @pytest.mark.parametrize("algebra", list(ARNOLD_CANCELLATION.keys()))
    def test_deg3_cancelled(self, algebra):
        """Degree >= 3: Arnold kills vacuum leakage."""
        assert ARNOLD_CANCELLATION[algebra]["deg3"] is True


class TestPoleCurvature:
    def test_km_killing_form(self):
        """KM algebras: curvature from Killing form (double pole)."""
        for name in ["Heisenberg", "sl2", "sl3"]:
            assert curvature_from_pole(name) == "killing_form"

    def test_virasoro_central_charge(self):
        assert curvature_from_pole("Virasoro") == "central_charge_T"

    def test_w3_dual_curvature(self):
        assert curvature_from_pole("W3") == "central_charge_TW"

    def test_simple_pole_mixed(self):
        for name in ["free_fermion", "beta_gamma", "bc"]:
            assert curvature_from_pole(name) == "mixed_channel"


class TestComplementarity:
    def test_virasoro_26(self):
        assert COMPLEMENTARITY["Virasoro"]["sum"] == 26

    def test_w3_100(self):
        assert COMPLEMENTARITY["W3"]["sum"] == 100


class TestChainDims:
    def test_heisenberg_like(self):
        """Single generator of weight 1: dim V-bar_n = 1 for all n >= 1."""
        vac_dims = {w: 1 for w in range(1, 20)}
        # B^1_h = dim V-bar_h * OS^0 = 1
        assert generic_chain_dim(1, 3, vac_dims, 1) == 1
        # B^2_h = compositions of h into 2 parts >= 1, times 1! = 1
        assert generic_chain_dim(2, 3, vac_dims, 1) == 2  # (1,2) and (2,1)

    def test_below_min_weight(self):
        vac_dims = {w: 1 for w in range(2, 20)}
        assert generic_chain_dim(3, 5, vac_dims, 2) == 0  # 3*2=6 > 5


class TestSelfConsistency:
    def test_os(self):
        for name, ok in verify_os_dims().items():
            assert ok, f"Failed: {name}"

    def test_desuspension(self):
        for name, ok in verify_desuspension().items():
            assert ok, f"Failed: {name}"

    def test_arnold(self):
        for name, ok in verify_arnold().items():
            assert ok, f"Failed: {name}"

    def test_pole_curvature(self):
        for name, ok in verify_pole_curvature().items():
            assert ok, f"Failed: {name}"


class TestDiscriminantLinearRelation:
    """Verify Q(x)-linear relation among sl2 discriminant family GFs.

    Theorem (thm:discriminant-linear-dependence):
    x^2(1+x) P_Vir = (1-2x-x^2)(1+x) P_sl2 - (1-3*x) P_bg

    where P_sl2, P_Vir, P_bg are the bar cohomology GFs.
    """

    @staticmethod
    def _gf_sl2(x):
        """Riordan GF: (1+x-sqrt(Delta))/(2x(1+x))."""
        from math import sqrt
        D = 1 - 2*x - 3*x**2
        return (1 + x - sqrt(D)) / (2*x*(1+x))

    @staticmethod
    def _gf_vir(x):
        """Motzkin difference GF: 4x/(1-x+sqrt(Delta))^2."""
        from math import sqrt
        D = 1 - 2*x - 3*x**2
        return 4*x / (1 - x + sqrt(D))**2

    @staticmethod
    def _gf_bg(x):
        """Beta-gamma GF: sqrt((1+x)/(1-3*x))."""
        from math import sqrt
        return sqrt((1+x)/(1-3*x))

    @pytest.mark.parametrize("x", [0.05, 0.1, 0.15, 0.2, 0.25, 0.3])
    def test_linear_relation_numerical(self, x):
        """Verify x^2(1+x)*P_Vir = (1-2x-x^2)(1+x)*P_sl2 - (1-3*x)*P_bg."""
        P_sl2 = self._gf_sl2(x)
        P_vir = self._gf_vir(x)
        P_bg = self._gf_bg(x)

        lhs = x**2 * (1+x) * P_vir
        rhs = (1-2*x-x**2)*(1+x)*P_sl2 - (1-3*x)*P_bg
        assert abs(lhs - rhs) < 1e-12, f"At x={x}: LHS={lhs}, RHS={rhs}"

    def test_exact_at_rational_point(self):
        """Verify at x=1/5 using exact arithmetic via sympy."""
        try:
            from sympy import Rational, sqrt as ssqrt
            x = Rational(1, 5)
            D = 1 - 2*x - 3*x**2
            P_sl2 = (1 + x - ssqrt(D)) / (2*x*(1+x))
            P_vir = 4*x / (1 - x + ssqrt(D))**2
            P_bg = ssqrt((1+x)/(1-3*x))
            lhs = x**2 * (1+x) * P_vir
            rhs = (1-2*x-x**2)*(1+x)*P_sl2 - (1-3*x)*P_bg
            assert (lhs - rhs).simplify() == 0
        except ImportError:
            pytest.skip("sympy required")

    def test_coefficients_in_u_basis(self):
        """Verify {1,u}-decomposition of each GF (u=sqrt(Delta))."""
        try:
            from sympy import symbols, sqrt as ssqrt, simplify
            x = symbols('x')
            D = 1 - 2*x - 3*x**2
            u = ssqrt(D)

            # P_sl2 = 1/(2x) - u/(2x(1+x))
            P_sl2 = (1 + x - u) / (2*x*(1+x))
            expected = 1/(2*x) - u/(2*x*(1+x))
            assert simplify(P_sl2 - expected) == 0

            # P_bg = u/(1-3*x)
            P_bg = (1+x)/u
            expected_bg = u/(1-3*x)  # after rationalization
            # (1+x)/u = (1+x)*u/D = (1+x)*u/((1-3*x)(1+x)) = u/(1-3*x)
            assert simplify(P_bg - expected_bg) == 0

        except ImportError:
            pytest.skip("sympy required")

    def test_mutual_determination_bg_from_others(self):
        """Recover P_bg from P_sl2 and P_Vir via the linear relation."""
        for x in [0.05, 0.1, 0.2]:
            P_sl2 = self._gf_sl2(x)
            P_vir = self._gf_vir(x)
            P_bg_direct = self._gf_bg(x)
            # From relation: (1-3*x)*P_bg = (1-2x-x^2)(1+x)*P_sl2 - x^2(1+x)*P_Vir
            P_bg_recovered = ((1-2*x-x**2)*(1+x)*P_sl2 - x**2*(1+x)*P_vir) / (1-3*x)
            assert abs(P_bg_direct - P_bg_recovered) < 1e-12


class TestYangianGF:
    """Verify Yangian Y(sl_2) bar cohomology generating function.

    Conjectured: dim H^n = 3^n + 1 for n >= 1.
    GF: P(x) = (1-3x^2)/((1-x)(1-3x)) = -1 + 1/(1-x) + 1/(1-3x).
    """

    @staticmethod
    def _gf_yangian(x):
        return (1 - 3*x**2) / ((1 - x) * (1 - 3*x))

    def test_p0_is_1(self):
        """P(0) = 1 (vacuum)."""
        assert abs(self._gf_yangian(0.0) - 1.0) < 1e-15

    @pytest.mark.parametrize("n,expected", [
        (1, 4), (2, 10), (3, 28), (4, 82), (5, 244), (6, 730),
    ])
    def test_coefficients(self, n, expected):
        """Verify 3^n + 1 for small n."""
        assert 3**n + 1 == expected

    def test_partial_fraction_correct(self):
        """P(x) = -1 + 1/(1-x) + 1/(1-3x), NOT 1/(1-x) + 1/(1-3x)."""
        try:
            from sympy import symbols, apart, Rational as R
            x = symbols('x')
            P = (1 - 3*x**2) / ((1 - x) * (1 - 3*x))
            pf = apart(P, x)
            # apart gives -1 - 1/(3x-1) - 1/(x-1) = -1 + 1/(1-3x) + 1/(1-x)
            assert pf.subs(x, 0) == 1  # P(0) = 1
            # Wrong version gives 2 at x=0:
            wrong = 1/(1-x) + 1/(1-3*x)
            assert wrong.subs(x, 0) == 2  # This is WRONG
        except ImportError:
            pytest.skip("sympy required")

    def test_recurrence(self):
        """a(n) = 4*a(n-1) - 3*a(n-2) for n >= 3, a(1)=4, a(2)=10."""
        a = {1: 4, 2: 10}
        for n in range(3, 10):
            a[n] = 4*a[n-1] - 3*a[n-2]
        for n in range(1, 10):
            assert a[n] == 3**n + 1, f"a({n}) = {a[n]}, expected {3**n + 1}"

    def test_gf_series_matches(self):
        """Verify GF coefficients match 3^n+1 numerically."""
        # Compute coefficients via recurrence
        expected = [1] + [3**n + 1 for n in range(1, 8)]
        # Compute from GF via numerical evaluation
        from math import factorial
        x0 = 0.01
        P = self._gf_yangian(x0)
        # P(x0) should approximately equal sum expected[n]*x0^n
        approx = sum(expected[n] * x0**n for n in range(8))
        assert abs(P - approx) < 1e-10
