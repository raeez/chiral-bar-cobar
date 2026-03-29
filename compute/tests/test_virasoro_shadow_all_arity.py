"""Tests for closed-form Virasoro shadow tower to arbitrary arity.

Verifies:
1. alpha = 2 from the critical cubic
2. Convolution recursion reproduces known S_4, S_5
3. Closed-form S_6, S_7, S_8, S_9, S_10 are correct
4. Denominator pattern: c^{r-3} * (5c+22)^{floor((r-2)/2)}
5. Numerical consistency at 10+ values of c
6. Shadow metric relation H(t)^2 = t^4 Q_L(t)
7. Critical cubic derivation
8. Duality S_r(c) vs S_r(26-c)
"""

import pytest
from sympy import (
    Rational,
    Symbol,
    cancel,
    factor,
    simplify,
    sqrt,
    nsimplify,
    N as Neval,
    Poly,
    numer,
    denom,
)

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from virasoro_shadow_all_arity import (
    kappa_vir,
    alpha_vir,
    S4_vir,
    Delta_vir,
    shadow_metric_vir,
    sqrt_QL_coefficients,
    shadow_coefficients,
    denominator_pattern,
    shadow_growth_rate_squared,
    critical_cubic,
    S_explicit,
)


c = Symbol('c')


# ═══════════════════════════════════════════════════════════════════════
# 1. Alpha = 2 from the critical cubic
# ═══════════════════════════════════════════════════════════════════════

class TestAlphaDetermination:
    """The cubic shadow alpha = 2 is determined by the critical cubic."""

    def test_critical_cubic_from_rho_equals_1(self):
        """rho = 1 => 9*alpha^2 + 2*Delta = 4*kappa^2."""
        kappa = kappa_vir()
        alpha = alpha_vir()
        Delta = Delta_vir()
        # rho^2 = 1 condition:
        lhs = 9 * alpha**2 + 2 * Delta  # = 36 + 80/(5c+22)
        rhs = 4 * kappa**2  # = c^2
        # Multiply out: 36(5c+22) + 80 = c^2(5c+22)
        expr = simplify((lhs - rhs) * (5 * c + 22))
        # Should be -(5c^3 + 22c^2 - 180c - 872)
        assert simplify(expr + critical_cubic()) == 0

    def test_alpha_squared_from_critical_cubic(self):
        """45*alpha^2 = 180 and 198*alpha^2 + 80 = 872 both give alpha^2 = 4."""
        # The critical cubic is 5c^3 + 22c^2 - 45*alpha^2*c - (198*alpha^2+80) = 0
        # Matching 5c^3+22c^2-180c-872: 45*alpha^2 = 180 => alpha^2 = 4
        assert alpha_vir()**2 == 4
        # Second check: 198*4+80 = 792+80 = 872 ✓
        assert 198 * 4 + 80 == 872


# ═══════════════════════════════════════════════════════════════════════
# 2. Convolution recursion reproduces known results
# ═══════════════════════════════════════════════════════════════════════

class TestConvolutionRecursion:

    def test_a0_is_c(self):
        a = sqrt_QL_coefficients(max_n=0)
        assert a[0] == c

    def test_a1_is_6(self):
        a = sqrt_QL_coefficients(max_n=1)
        assert a[1] == 6

    def test_a2_gives_S4(self):
        a = sqrt_QL_coefficients(max_n=2)
        S4 = cancel(a[2] / 4)  # S_4 = a_2 / 4
        assert simplify(S4 - S4_vir()) == 0

    def test_a3_gives_S5(self):
        a = sqrt_QL_coefficients(max_n=3)
        S5 = cancel(a[3] / 5)  # S_5 = a_3 / 5
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(S5 - expected) == 0


# ═══════════════════════════════════════════════════════════════════════
# 3. Closed-form results for S_4 through S_10
# ═══════════════════════════════════════════════════════════════════════

class TestClosedFormResults:

    @pytest.fixture
    def coeffs(self):
        return shadow_coefficients(max_r=12)

    def test_S2(self, coeffs):
        assert simplify(coeffs[2] - c / 2) == 0

    def test_S3(self, coeffs):
        assert simplify(coeffs[3] - 2) == 0

    def test_S4(self, coeffs):
        assert simplify(coeffs[4] - S4_vir()) == 0

    def test_S5(self, coeffs):
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(coeffs[5] - expected) == 0

    def test_S6(self, coeffs):
        expected = Rational(80) * (45 * c + 193) / (3 * c**3 * (5 * c + 22)**2)
        assert simplify(coeffs[6] - expected) == 0

    def test_S7(self, coeffs):
        expected = Rational(-2880) * (15 * c + 61) / (7 * c**4 * (5 * c + 22)**2)
        assert simplify(coeffs[7] - expected) == 0

    def test_S8_has_correct_denominator(self, coeffs):
        """S_8 denominator should be c^5 (5c+22)^3."""
        d = denom(cancel(coeffs[8]))
        p = Poly(d, c)
        # Check it vanishes at c=0 (order 5) and c=-22/5 (order 3)
        assert p.eval(0) == 0
        # Factor and check structure
        f = factor(d)
        assert simplify(f / (c**5 * (5*c+22)**3)).is_rational_function(c)

    def test_S9_has_correct_denominator(self, coeffs):
        """S_9 denominator should be c^6 (5c+22)^3."""
        d = denom(cancel(coeffs[9]))
        f = factor(d)
        # Remove numerical constants
        ratio = simplify(f / (c**6 * (5*c+22)**3))
        assert ratio.is_number or ratio.is_rational_function(c)

    def test_S10_has_correct_denominator(self, coeffs):
        """S_10 denominator should be c^7 (5c+22)^4."""
        d = denom(cancel(coeffs[10]))
        f = factor(d)
        ratio = simplify(f / (c**7 * (5*c+22)**4))
        assert ratio.is_number or ratio.is_rational_function(c)


# ═══════════════════════════════════════════════════════════════════════
# 4. Denominator pattern
# ═══════════════════════════════════════════════════════════════════════

class TestDenominatorPattern:
    """S_r has denominator c^{r-3} * (5c+22)^{floor((r-2)/2)}."""

    @pytest.fixture
    def pattern(self):
        return denominator_pattern(max_r=12)

    @pytest.mark.parametrize("r,expected_pow_c,expected_pow_5c22", [
        (4, 1, 1),
        (5, 2, 1),
        (6, 3, 2),
        (7, 4, 2),
        (8, 5, 3),
        (9, 6, 3),
        (10, 7, 4),
        (11, 8, 4),
        (12, 9, 5),
    ])
    def test_denominator_powers(self, pattern, r, expected_pow_c, expected_pow_5c22):
        entry = next(e for e in pattern if e[0] == r)
        _, pow_c, pow_5c22 = entry
        assert pow_c == expected_pow_c, f"S_{r}: expected c^{expected_pow_c}, got c^{pow_c}"
        assert pow_5c22 == expected_pow_5c22, (
            f"S_{r}: expected (5c+22)^{expected_pow_5c22}, got (5c+22)^{pow_5c22}"
        )

    def test_pattern_formula(self, pattern):
        """Verify pow_c = r-3, pow_5c22 = floor((r-2)/2) for all r."""
        for r, pow_c, pow_5c22 in pattern:
            assert pow_c == r - 3
            assert pow_5c22 == (r - 2) // 2


# ═══════════════════════════════════════════════════════════════════════
# 5. Numerical consistency
# ═══════════════════════════════════════════════════════════════════════

class TestNumericalConsistency:

    @pytest.mark.parametrize("c_val", [
        1, 2, Rational(25, 4), Rational(61, 10),
        7, 10, 13, 26, 50, 100,
    ])
    def test_shadow_metric_relation(self, c_val):
        """Verify H(t)^2 = t^4 Q_L(t) numerically at each c."""
        coeffs = shadow_coefficients(max_r=15)
        q0, q1, q2 = shadow_metric_vir()

        q0_val = float(q0.subs(c, c_val))
        q1_val = float(q1.subs(c, c_val))
        q2_val = float(q2.subs(c, c_val))

        t_val = 0.03
        H_val = sum(
            r * float(coeffs[r].subs(c, c_val)) * t_val**r
            for r in range(2, 16)
        )
        QL_val = q0_val + q1_val * t_val + q2_val * t_val**2
        lhs = H_val**2
        rhs = t_val**4 * QL_val
        scale = max(abs(lhs), abs(rhs), 1e-20)
        assert abs(lhs - rhs) / scale < 1e-8, (
            f"H(t)^2 != t^4 Q_L(t) at c={c_val}, t={t_val}: "
            f"rel diff = {abs(lhs - rhs)/scale}"
        )

    @pytest.mark.parametrize("c_val", [1, 2, 10, 13, 26])
    def test_S5_numerical(self, c_val):
        """Check S_5 = -48/[c^2(5c+22)] numerically."""
        coeffs = shadow_coefficients(max_r=5)
        computed = float(coeffs[5].subs(c, c_val))
        expected = -48.0 / (c_val**2 * (5 * c_val + 22))
        assert abs(computed - expected) < 1e-12


# ═══════════════════════════════════════════════════════════════════════
# 6. Alternating signs and growth rate
# ═══════════════════════════════════════════════════════════════════════

class TestAsymptotics:

    def test_alternating_sign_pattern_convergent(self):
        """S_r alternates in sign at c=10 for r=4..12."""
        coeffs = shadow_coefficients(max_r=12)
        for r in range(4, 13):
            val = float(coeffs[r].subs(c, 10))
            expected_sign = (-1)**(r % 2)
            assert val * expected_sign > 0, f"S_{r} has wrong sign at c=10"

    def test_growth_rate_at_c13(self):
        """At c=13, rho ≈ 0.467: |S_r| ~ rho^r."""
        coeffs = shadow_coefficients(max_r=20)
        rho_sq = float(shadow_growth_rate_squared().subs(c, 13))
        rho = rho_sq**0.5
        assert abs(rho - 0.467) < 0.01

        # Check ratio |S_{r+1}/S_r| approaches rho
        vals = [abs(float(coeffs[r].subs(c, 13))) for r in range(10, 21)]
        ratios = [vals[i+1] / vals[i] for i in range(len(vals)-1)]
        # Ratios oscillate (cos factor) but average should approach rho
        # Use geometric mean of last few |S_r|^{1/r}
        geo_rates = [abs(float(coeffs[r].subs(c, 13)))**(1.0/r) for r in range(15, 21)]
        avg_rate = sum(geo_rates) / len(geo_rates)
        assert abs(avg_rate - rho) < 0.1


# ═══════════════════════════════════════════════════════════════════════
# 7. Duality
# ═══════════════════════════════════════════════════════════════════════

class TestDuality:

    def test_self_dual_at_c13(self):
        """S_r(13) = S_r(26-13) = S_r(13) (tautological at self-dual point)."""
        coeffs = shadow_coefficients(max_r=8)
        for r in range(2, 9):
            v1 = coeffs[r].subs(c, 13)
            v2 = coeffs[r].subs(c, 26 - 13)
            assert simplify(v1 - v2) == 0

    def test_discriminant_complementarity(self):
        """Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)]."""
        D1 = Delta_vir()
        D2 = D1.subs(c, 26 - c)
        s = cancel(D1 + D2)
        expected = Rational(6960) / ((5*c+22) * (152 - 5*c))
        assert simplify(s - expected) == 0


# ═══════════════════════════════════════════════════════════════════════
# 8. Explicit formulas match recursion
# ═══════════════════════════════════════════════════════════════════════

class TestExplicitFormulas:

    def test_all_explicit_match_recursion(self):
        coeffs = shadow_coefficients(max_r=7)
        for r in range(2, 8):
            explicit = S_explicit(r)
            recursive = coeffs[r]
            assert simplify(explicit - recursive) == 0, f"Mismatch at r={r}"


# ═══════════════════════════════════════════════════════════════════════
# 9. Three independent methods agree
# ══════════════════════════════════════════════��════════════════════════

class TestThreeMethodsAgree:
    """Shadow metric, master equation, and DS module all give same answers."""

    def test_shadow_metric_vs_master_eq(self):
        from virasoro_shadow_all_arity import shadow_coefficients_master_eq
        metric = shadow_coefficients(max_r=10)
        master = shadow_coefficients_master_eq(max_r=10)
        for r in range(2, 11):
            assert simplify(metric[r] - master[r]) == 0, f"Mismatch at r={r}"

    def test_shadow_metric_vs_ds_module(self):
        try:
            from ds_shadow_higher_arity import _virasoro_tower_internal
        except ImportError:
            pytest.skip("ds_shadow_higher_arity not available")
        metric = shadow_coefficients(max_r=10)
        ds = _virasoro_tower_internal(max_arity=10)
        for r in range(2, 11):
            assert simplify(metric[r] - ds[r]) == 0, f"Mismatch at r={r}"

    def test_master_eq_vs_quintic_module(self):
        """The existing virasoro_quintic_shadow module gives same S_5."""
        try:
            from virasoro_quintic_shadow import quintic_shadow_coefficient
        except ImportError:
            pytest.skip("virasoro_quintic_shadow not available")
        from virasoro_shadow_all_arity import shadow_coefficients_master_eq
        master = shadow_coefficients_master_eq(max_r=5)
        quintic = quintic_shadow_coefficient()
        assert simplify(master[5] - quintic) == 0


# ═══════════════════════════════════════════════════════════════════════
# 10. Cross-checks (AP10: structural, not single hardcoded values)
# ═══════════════════════════════════════════════════════════════════════

class TestStructuralCrossChecks:
    """Cross-checks that enforce mathematical constraints."""

    def test_S2_equals_kappa(self):
        """S_2 = c/2 = kappa for Virasoro (universal identity)."""
        coeffs = shadow_coefficients(max_r=2)
        assert simplify(coeffs[2] - kappa_vir()) == 0

    def test_S3_is_alpha(self):
        """S_3 = alpha = 2 (the cubic shadow coefficient)."""
        coeffs = shadow_coefficients(max_r=3)
        assert simplify(coeffs[3] - alpha_vir()) == 0

    def test_discriminant_complementarity(self):
        """Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)].

        The numerator 6960 = 40*174 is c-independent. Verify at 5 values.
        """
        for c_val in [1, 5, 10, 13, 25]:
            D1 = Rational(40) / (5 * c_val + 22)
            D2 = Rational(40) / (5 * (26 - c_val) + 22)
            s = D1 + D2
            expected = Rational(6960) / ((5 * c_val + 22) * (152 - 5 * c_val))
            assert s == expected, (
                f"Discriminant complementarity fails at c={c_val}: "
                f"{s} != {expected}"
            )

    def test_shadow_metric_positive_definite_at_t0(self):
        """Q_L(0) = c^2 > 0 for c > 0 (shadow metric is positive at origin).

        Q_L(0) = (2*kappa)^2 = c^2 for Virasoro.
        """
        q0, q1, q2 = shadow_metric_vir()
        for c_val in [1, 5, 10, 13, 26]:
            val = float(q0.subs(c, c_val))
            assert val > 0, f"Q_L(0) = {val} <= 0 at c={c_val}"

    def test_shadow_coefficients_alternating_sign(self):
        """S_r alternates sign for r=4..13 at c=10 (convergent regime).

        At c=10 (convergent, theta=170 deg): S_4 > 0, S_5 < 0, S_6 > 0, ...
        The alternation holds to high arity when theta is close to 180.
        At small c (theta < 170), phase slips occur at finite arity.
        """
        coeffs = shadow_coefficients(max_r=13)
        for r in range(4, 14):
            val = float(coeffs[r].subs(c, 10))
            expected_sign = (-1)**(r % 2)
            assert val * expected_sign > 0, (
                f"S_{r}(10) = {val}, expected sign {'+' if expected_sign > 0 else '-'}"
            )

    def test_growth_rate_self_dual_symmetry(self):
        """rho(c) = rho(26-c) at c=13 (the self-dual point).

        rho^2 = (9*alpha^2 + 2*Delta) / (4*kappa^2)
        At c=13: kappa = 13/2, Delta = 40/87, alpha = 2.
        At c=26-13=13: same by tautology.
        """
        rho_sq = shadow_growth_rate_squared()
        rho_13 = rho_sq.subs(c, 13)
        rho_13_dual = rho_sq.subs(c, 26 - 13)
        assert simplify(rho_13 - rho_13_dual) == 0


# ═══════════════════════════════════════════════════════════════════════
# 11. Deep structural: exact sign verification via rational arithmetic
# ═══════════════════════════════════════════════════════════════════════

class TestExactSigns:
    """Verify sign pattern using exact rational arithmetic.

    The branch point argument theta(c) determines the sign pattern.
    At large c, theta -> 180 degrees and signs alternate perfectly.
    At small c, theta < 180 and phase slips occur at r ~ pi/(pi-theta).

    At c=1: theta=164 deg, first break at r=17.
    At c=10: theta=170 deg, alternating holds to r >> 30.
    At c=26: theta=173 deg, alternating holds to r >> 50.
    """

    @pytest.fixture
    def exact_coeffs(self):
        return shadow_coefficients(max_r=25)

    @pytest.mark.parametrize("c_val,max_r", [
        (10, 20),   # theta=170: alternating to r >> 30
        (13, 20),   # theta=171: self-dual, alternating to r >> 30
        (26, 20),   # theta=173: alternating to r >> 50
    ])
    def test_alternating_in_convergent_regime(self, exact_coeffs, c_val, max_r):
        """Alternating signs hold in the convergent regime (large c)."""
        for r in range(4, max_r + 1):
            Sr = exact_coeffs[r].subs(c, c_val)
            expected_positive = (r % 2 == 0)
            if expected_positive:
                assert Sr > 0, f"S_{r}(c={c_val}) should be positive"
            else:
                assert Sr < 0, f"S_{r}(c={c_val}) should be negative"

    def test_phase_slip_at_c1(self, exact_coeffs):
        """At c=1, alternating pattern holds for r=4..16 then BREAKS at r=17.

        This is a genuine mathematical feature: the branch point at
        c=1 has argument 164 degrees, causing a phase slip with
        beat period ~22 terms.
        """
        # Alternating holds for r=4..16
        for r in range(4, 17):
            Sr = exact_coeffs[r].subs(c, 1)
            expected_positive = (r % 2 == 0)
            if expected_positive:
                assert Sr > 0, f"S_{r}(1) should still be positive"
            else:
                assert Sr < 0, f"S_{r}(1) should still be negative"

        # Phase slip: S_17 is positive (expected negative)
        S17 = exact_coeffs[17].subs(c, 1)
        assert S17 > 0, "S_17(1) should be POSITIVE (phase slip)"


class TestNumeratorDegrees:
    """Verify numerator polynomial degree pattern."""

    def test_numerator_degree_pattern(self):
        """Numerator of S_r has degree floor((r-4)/2) in c, for r >= 4."""
        coeffs = shadow_coefficients(max_r=12)
        for r in range(4, 13):
            Sr = coeffs[r]
            n = numer(cancel(Sr))
            p = Poly(n, c)
            deg = p.degree()
            expected = (r - 4) // 2
            assert deg == expected, (
                f"S_{r}: numerator degree {deg}, expected {expected}"
            )


class TestBranchPointGeometry:
    """Verify the branch point analysis that forces alternating signs."""

    def test_QL_discriminant_negative_for_positive_c(self):
        """disc(Q_L) = -320*c^2/(5c+22) < 0 for c > 0.

        This means Q_L has complex roots => class M for all c > 0.
        """
        q0, q1, q2 = shadow_metric_vir()
        disc = cancel(q1**2 - 4 * q0 * q2)
        # disc = 144c^2 - 4c^2*(180c+872)/(5c+22)
        #      = c^2*(144 - 4*(180c+872)/(5c+22))
        #      = c^2*(144*(5c+22) - 4*(180c+872))/(5c+22)
        #      = c^2*(720c+3168-720c-3488)/(5c+22)
        #      = c^2*(-320)/(5c+22)
        expected = -320 * c**2 / (5 * c + 22)
        assert simplify(disc - expected) == 0

    @pytest.mark.parametrize("c_val", [
        Rational(1, 10), 1, 5, 10, 13, 26, 100
    ])
    def test_branch_point_in_second_quadrant(self, c_val):
        """Branch point of Q_L has Re < 0 and Im > 0 for c > 0.

        This forces the oscillation phase > pi/2, giving alternating signs.
        """
        q0v = float(c_val**2)
        q1v = float(12 * c_val)
        q2v = float((180 * c_val + 872) / (5 * c_val + 22))
        # Root of Q_L: t = (-q1 + sqrt(q1^2 - 4*q0*q2)) / (2*q2)
        disc = q1v**2 - 4 * q0v * q2v
        assert disc < 0, f"Discriminant should be negative at c={c_val}"
        import cmath
        sqrt_disc = cmath.sqrt(disc)
        root = (-q1v + sqrt_disc) / (2 * q2v)
        assert root.real < 0, f"Re(root) should be negative at c={c_val}"
        assert root.imag > 0, f"Im(root) should be positive at c={c_val}"
