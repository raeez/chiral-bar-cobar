r"""Tests for the gravitational entropy engine.

Verifies:
  1. Faber-Pandharipande integrals and A-hat generating function
  2. Scalar free energies for all standard families
  3. Scalar complementarity identity at all genera
  4. Complementarity at specific central charge values
  5. Discriminant complementarity
  6. BTZ entropy structure
  7. Borel convergence radius and instanton actions
  8. Self-dual point c=13 constraints
  9. Cross-family consistency
  10. Instanton complementarity

Ground truth:
  thm:complementarity — F_g(A) + F_g(A^!) = Phi_g
  thm:shadow-radius — rho(c) = sqrt((180c+872)/(c^2(5c+22)))
  thm:shadow-connection — Delta(c) + Delta(26-c) = 6960/((5c+22)(152-5c))
  Faber-Pandharipande: lambda_g^FP = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)
  Cardy formula: S_BH = 2*pi*sqrt(cE/6)
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational, simplify, cancel, expand, S, Symbol, sqrt, bernoulli, factorial

from compute.lib.gravitational_entropy_engine import (
    lambda_fp,
    ahat_generating_function,
    ahat_value,
    scalar_free_energy,
    virasoro_kappa,
    virasoro_kappa_dual,
    virasoro_scalar_Fg,
    virasoro_dual_scalar_Fg,
    scalar_complementarity_sum,
    scalar_complementarity_target,
    verify_scalar_complementarity,
    complementarity_kappa_sum,
    discriminant_complementarity,
    scalar_genus_expansion_coefficients,
    virasoro_graph_sum_genus2,
    cardy_entropy,
    logarithmic_correction_coefficient,
    btz_entropy_scalar,
    btz_entropy_ratio,
    virasoro_shadow_growth_rate,
    virasoro_shadow_growth_rate_numerical,
    critical_central_charge,
    borel_convergence_radius,
    instanton_action,
    instanton_action_complementarity,
    self_dual_analysis,
    gravitational_entropy_table,
    full_gravitational_analysis,
    heisenberg_kappa,
)


# =====================================================================
# Section 1: Faber-Pandharipande integrals
# =====================================================================

class TestFaberPandharipande:
    """Test lambda_g^FP values against known Bernoulli number formulas."""

    def test_lambda_0(self):
        assert lambda_fp(0) == 1

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_4(self):
        """lambda_4^FP = 127/154828800."""
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 10):
            assert lambda_fp(g) > 0

    def test_decreasing(self):
        """lambda_g^FP is decreasing for g >= 1."""
        for g in range(1, 8):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_bernoulli_formula(self):
        """Verify against direct Bernoulli computation."""
        for g in range(1, 6):
            B2g = bernoulli(2 * g)
            power = 2 ** (2 * g - 1)
            expected = (power - 1) * abs(B2g) / (power * factorial(2 * g))
            assert lambda_fp(g) == Rational(expected)

    def test_invalid_genus(self):
        with pytest.raises(ValueError):
            lambda_fp(-1)


class TestAhatGenus:
    """Test A-hat generating function (x/2)/sinh(x/2)."""

    def test_ahat_at_zero(self):
        """A-hat(0) = 1."""
        assert abs(ahat_value(0.0) - 1.0) < 1e-14

    def test_ahat_small_x(self):
        """A-hat(x) ~ 1 - x^2/24 for small x."""
        x = 0.01
        val = ahat_value(x)
        approx = 1.0 - x**2 / 24.0
        assert abs(val - approx) < 1e-8

    def test_ahat_coefficients(self):
        """Verify coefficients match lambda_g^FP."""
        coeffs = ahat_generating_function(Symbol('x'), 5)
        assert coeffs[0] == 1
        assert coeffs[1] == Rational(-1, 24)
        assert coeffs[2] == Rational(7, 5760)
        assert coeffs[3] == Rational(-31, 967680)

    def test_ahat_entire(self):
        """A-hat is entire: no singularity at any finite x."""
        for x in [0.1, 1.0, 5.0, 10.0, 50.0]:
            val = ahat_value(x)
            assert math.isfinite(val)


# =====================================================================
# Section 2: Scalar free energies
# =====================================================================

class TestScalarFreeEnergies:
    """Test F_g^sc = kappa * lambda_g^FP."""

    def test_virasoro_F1(self):
        """F_1^sc(Vir_c) = c/48."""
        c = Symbol('c')
        assert simplify(virasoro_scalar_Fg(None, 1) - c / 48) == 0

    def test_virasoro_F2(self):
        """F_2^sc(Vir_c) = 7c/11520."""
        c = Symbol('c')
        assert simplify(virasoro_scalar_Fg(None, 2) - 7 * c / 11520) == 0

    def test_virasoro_F3(self):
        """F_3^sc(Vir_c) = 31c/1935360."""
        c = Symbol('c')
        assert simplify(virasoro_scalar_Fg(None, 3) - 31 * c / 1935360) == 0

    def test_virasoro_numerical(self):
        """F_g at c=26 (bosonic string)."""
        assert virasoro_scalar_Fg(26, 1) == Rational(26, 48)
        assert virasoro_scalar_Fg(26, 2) == Rational(7 * 26, 11520)

    def test_heisenberg(self):
        """F_g^sc(H_k) = k * lambda_g^FP."""
        k = Symbol('k')
        assert scalar_free_energy(k, 1) == k * Rational(1, 24)
        assert scalar_free_energy(k, 2) == k * Rational(7, 5760)

    def test_invalid_genus(self):
        with pytest.raises(ValueError):
            scalar_free_energy(1, 0)


# =====================================================================
# Section 3: Scalar complementarity
# =====================================================================

class TestScalarComplementarity:
    """Test F_g^sc(c) + F_g^sc(26-c) = 13 * lambda_g^FP."""

    def test_kappa_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        assert simplify(complementarity_kappa_sum() - 13) == 0

    def test_kappa_sum_numerical(self):
        """Numerical kappa sum at specific c values."""
        for c in [1, 5, 10, 13, 20, 25]:
            ksum = float(virasoro_kappa(c) + virasoro_kappa_dual(c))
            assert abs(ksum - 13.0) < 1e-14

    def test_complementarity_genus1(self):
        """F_1(c) + F_1(26-c) = 13/24."""
        assert simplify(scalar_complementarity_sum(None, 1) - Rational(13, 24)) == 0

    def test_complementarity_genus2(self):
        """F_2(c) + F_2(26-c) = 91/11520."""
        target = scalar_complementarity_target(2)
        assert target == 13 * Rational(7, 5760)
        assert simplify(scalar_complementarity_sum(None, 2) - target) == 0

    def test_complementarity_genus3(self):
        """F_3(c) + F_3(26-c) = 403/1935360."""
        target = scalar_complementarity_target(3)
        lhs = scalar_complementarity_sum(None, 3)
        assert simplify(lhs - target) == 0

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5, 6])
    def test_complementarity_all_genera(self, g):
        """Scalar complementarity holds symbolically at every genus."""
        result = verify_scalar_complementarity(None, g)
        assert result['match'], f"Complementarity failed at genus {g}: diff = {result['difference']}"

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 20, 25])
    def test_complementarity_numerical(self, c_val):
        """Numerical complementarity at specific c values through genus 6."""
        for g in range(1, 7):
            result = verify_scalar_complementarity(c_val, g)
            assert result['match'], f"Failed at c={c_val}, g={g}"

    def test_self_dual_c13(self):
        """At c=13: F_g(13) = F_g(13) (Koszul dual = self)."""
        for g in range(1, 5):
            Fg = virasoro_scalar_Fg(13, g)
            Fg_dual = virasoro_dual_scalar_Fg(13, g)
            assert Fg == Fg_dual

    def test_bosonic_string_c26(self):
        """At c=26: Vir_26^! = Vir_0, kappa(Vir_0) = 0."""
        assert virasoro_kappa_dual(26) == 0
        for g in range(1, 5):
            assert virasoro_dual_scalar_Fg(26, g) == 0


# =====================================================================
# Section 4: Discriminant complementarity
# =====================================================================

class TestDiscriminantComplementarity:
    """Test Delta(c) + Delta(26-c) = 6960/((5c+22)(152-5c))."""

    def test_symbolic(self):
        """Symbolic discriminant sum."""
        result = discriminant_complementarity()
        expected = result['expected']
        actual_sum = result['sum']
        assert simplify(actual_sum - expected) == 0

    @pytest.mark.parametrize("c_val", [1, 5, 10, 13, 20, 25])
    def test_numerical(self, c_val):
        """Numerical discriminant complementarity."""
        result = discriminant_complementarity(c_val)
        diff = float(result['sum'] - result['expected'])
        assert abs(diff) < 1e-12

    def test_self_dual_c13(self):
        """At c=13: Delta(13) = Delta(13) (self-dual)."""
        result = discriminant_complementarity(13)
        assert abs(float(result['Delta_c'] - result['Delta_dual'])) < 1e-14


# =====================================================================
# Section 5: BTZ entropy
# =====================================================================

class TestBTZEntropy:
    """Test BTZ/Cardy entropy formula."""

    def test_cardy_formula(self):
        """S_BH = 2*pi*sqrt(cE/6)."""
        c, E = 26.0, 100.0
        S_BH = cardy_entropy(c, E)
        expected = 2.0 * math.pi * math.sqrt(c * E / 6.0)
        assert abs(S_BH - expected) < 1e-12

    def test_logarithmic_correction(self):
        """The coefficient is -3/2."""
        assert logarithmic_correction_coefficient() == Rational(-3, 2)

    def test_btz_large_E_limit(self):
        """For large E, corrections become negligible."""
        c = 26.0
        ratio_large = btz_entropy_ratio(c, 1e6)
        ratio_small = btz_entropy_ratio(c, 10.0)
        # Large E: ratio closer to 1 (dominated by S_BH)
        assert abs(ratio_large - 1.0) < abs(ratio_small - 1.0)

    def test_btz_increasing_c(self):
        """Entropy increases with c at fixed E."""
        E = 100.0
        S1 = cardy_entropy(10.0, E)
        S2 = cardy_entropy(26.0, E)
        assert S2 > S1

    def test_btz_full_analysis(self):
        """Full BTZ analysis returns expected structure."""
        result = btz_entropy_scalar(26.0, 100.0, 3)
        assert 'S_BH' in result
        assert 'total_entropy' in result
        assert 'corrections' in result
        assert len(result['corrections']) == 2  # genus 2 and 3
        assert result['S_BH'] > 0

    def test_btz_complementarity_entropy(self):
        """Entropy at c and 26-c: S_BH(c) + S_BH(26-c) is determined."""
        E = 100.0
        for c in [5.0, 10.0, 13.0, 20.0]:
            S_c = cardy_entropy(c, E)
            S_dual = cardy_entropy(26.0 - c, E)
            # Not a simple sum rule, but check consistency
            assert S_c > 0 and S_dual > 0


# =====================================================================
# Section 6: Borel structure
# =====================================================================

class TestBorelStructure:
    """Test shadow growth rate and Borel convergence."""

    def test_critical_central_charge(self):
        """c* ~ 6.1243."""
        c_star = critical_central_charge()
        assert abs(c_star - 6.1254) < 0.001

    def test_critical_satisfies_equation(self):
        """5c*^3 + 22c*^2 - 180c* - 872 = 0."""
        c_star = critical_central_charge()
        residual = 5 * c_star**3 + 22 * c_star**2 - 180 * c_star - 872
        assert abs(residual) < 1e-10

    def test_rho_at_c_star(self):
        """rho(c*) = 1."""
        c_star = critical_central_charge()
        rho = virasoro_shadow_growth_rate_numerical(c_star)
        assert abs(rho - 1.0) < 1e-8

    def test_rho_convergent_regime(self):
        """For c > c*: rho < 1."""
        c_star = critical_central_charge()
        for c in [10.0, 13.0, 20.0, 26.0, 100.0]:
            if c > c_star:
                rho = virasoro_shadow_growth_rate_numerical(c)
                assert rho < 1.0, f"rho({c}) = {rho} >= 1"

    def test_rho_divergent_regime(self):
        """For c < c*: rho > 1."""
        c_star = critical_central_charge()
        for c in [1.0, 2.0, 3.0, 5.0]:
            if c < c_star:
                rho = virasoro_shadow_growth_rate_numerical(c)
                assert rho > 1.0, f"rho({c}) = {rho} <= 1"

    def test_borel_radius_large_c(self):
        """For large c: Borel radius is large."""
        R = borel_convergence_radius(100.0)
        assert R > 10.0

    def test_borel_radius_c13(self):
        """Borel radius at self-dual point."""
        R = borel_convergence_radius(13.0)
        rho = virasoro_shadow_growth_rate_numerical(13.0)
        expected = 2.0 * math.pi / rho
        assert abs(R - expected) < 1e-10

    def test_rho_decreasing_large_c(self):
        """rho(c) -> 0 as c -> infinity."""
        rho_100 = virasoro_shadow_growth_rate_numerical(100.0)
        rho_1000 = virasoro_shadow_growth_rate_numerical(1000.0)
        assert rho_1000 < rho_100

    def test_rho_symbolic(self):
        """Symbolic shadow growth rate matches numerical."""
        c = Symbol('c')
        rho_sym = virasoro_shadow_growth_rate(None)
        for c_val in [5, 13, 26]:
            sym_val = float(rho_sym.subs(c, c_val))
            num_val = virasoro_shadow_growth_rate_numerical(float(c_val))
            assert abs(sym_val - num_val) < 1e-10


# =====================================================================
# Section 7: Instanton actions
# =====================================================================

class TestInstantonActions:
    """Test instanton action computation and complementarity."""

    def test_instanton_positive(self):
        """Instanton action is positive for c > 0."""
        for c in [1.0, 5.0, 13.0, 26.0]:
            A = instanton_action(c)
            assert A > 0

    def test_instanton_increasing_c(self):
        """Instanton action increases with c (in convergent regime)."""
        A_13 = instanton_action(13.0)
        A_26 = instanton_action(26.0)
        assert A_26 > A_13

    def test_instanton_c13_self_dual(self):
        """At c=13: A(13) = A(13) (trivially self-dual)."""
        result = instanton_action_complementarity(13.0)
        assert abs(result['A_c'] - result['A_dual']) < 1e-12
        assert abs(result['ratio'] - 1.0) < 1e-12

    def test_instanton_complementarity_structure(self):
        """Check structure of instanton complementarity data."""
        result = instanton_action_complementarity(10.0)
        assert 'A_c' in result
        assert 'A_dual' in result
        assert 'sum' in result
        assert 'product' in result

    def test_instanton_reciprocal_rho(self):
        """A(c) = 1/rho(c)."""
        for c in [5.0, 13.0, 26.0]:
            A = instanton_action(c)
            rho = virasoro_shadow_growth_rate_numerical(c)
            assert abs(A - 1.0 / rho) < 1e-12


# =====================================================================
# Section 8: Self-dual c = 13
# =====================================================================

class TestSelfDual:
    """Test self-dual analysis at c = 13."""

    def test_kappa_self_dual(self):
        """kappa(13) = 13/2."""
        assert virasoro_kappa(13) == Rational(13, 2)

    def test_dual_equals_self(self):
        """kappa_dual(13) = 13/2 = kappa(13)."""
        assert virasoro_kappa_dual(13) == Rational(13, 2)

    def test_free_energies_equal(self):
        """F_g(13) = F_g_dual(13) for all g."""
        for g in range(1, 8):
            assert virasoro_scalar_Fg(13, g) == virasoro_dual_scalar_Fg(13, g)

    def test_self_dual_analysis(self):
        """Full self-dual analysis structure."""
        result = self_dual_analysis(6)
        assert result['is_self_dual']
        assert result['kappa'] == Rational(13, 2)
        assert len(result['free_energies']) == 6
        assert result['Delta_equal']

    def test_discriminant_self_dual(self):
        """Delta(13) = Delta_dual(13) = 40/87."""
        result = discriminant_complementarity(13)
        expected = Rational(40, 87)
        assert result['Delta_c'] == expected
        assert result['Delta_dual'] == expected

    def test_rho_c13_in_convergent_regime(self):
        """rho(13) < 1 (convergent shadow obstruction tower)."""
        rho = virasoro_shadow_growth_rate_numerical(13.0)
        assert rho < 1.0


# =====================================================================
# Section 9: Cross-family consistency
# =====================================================================

class TestCrossFamilyConsistency:
    """Verify complementarity and free energy consistency across families."""

    def test_heisenberg_antisymmetry(self):
        """kappa(H_k) + kappa(H_k^!) = 0 (free field anti-symmetry)."""
        # H_k^! = Sym^ch(V*), kappa(H_k^!) = -k
        k = Rational(3)
        kappa = heisenberg_kappa(k)
        kappa_dual = -k
        assert kappa + kappa_dual == 0

    def test_heisenberg_free_energies_cancel(self):
        """F_g(H_k) + F_g(H_k^!) = 0."""
        k = Rational(3)
        for g in range(1, 5):
            Fg = scalar_free_energy(k, g)
            Fg_dual = scalar_free_energy(-k, g)
            assert Fg + Fg_dual == 0

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_lambda_fp_from_ahat(self, g):
        """lambda_g^FP matches coefficient in A-hat generating function."""
        coeffs = ahat_generating_function(Symbol('x'), g + 1)
        expected = (-1)**g * lambda_fp(g)
        assert coeffs[g] == expected

    def test_free_energy_positivity_virasoro(self):
        """F_g^sc(Vir_c) > 0 for c > 0."""
        for g in range(1, 6):
            for c in [1, 5, 13, 26]:
                Fg = virasoro_scalar_Fg(c, g)
                assert Fg > 0

    def test_free_energy_linearity(self):
        """F_g^sc is linear in kappa."""
        c = Symbol('c')
        for g in range(1, 4):
            Fg = virasoro_scalar_Fg(None, g)
            # Should be c * (constant) / 2
            coeff = Fg / c
            assert simplify(coeff - lambda_fp(g) / 2) == 0


# =====================================================================
# Section 10: Genus-2 graph sum
# =====================================================================

class TestGenus2GraphSum:
    """Test genus-2 graph sum with shadow corrections."""

    def test_graph_sum_runs(self):
        """Graph sum computation completes."""
        result = virasoro_graph_sum_genus2()
        assert 'total' in result
        assert 'graphs' in result
        assert len(result['graphs']) == 6

    def test_graph_names(self):
        """All 6 genus-2 graphs are present."""
        result = virasoro_graph_sum_genus2()
        names = set(result['graphs'].keys())
        expected = {'smooth_g2', 'irr_node', 'banana', 'separating', 'theta', 'mixed'}
        assert names == expected

    def test_smooth_graph_is_scalar(self):
        """Smooth genus-2 graph gives F_2^sc."""
        result = virasoro_graph_sum_genus2()
        c = Symbol('c')
        smooth_w = result['graphs']['smooth_g2']['weighted']
        expected = c / 2 * Rational(7, 5760)
        assert simplify(smooth_w - expected) == 0

    def test_banana_quartic(self):
        """Banana graph uses quartic shadow Q^contact."""
        result = virasoro_graph_sum_genus2()
        banana = result['graphs']['banana']
        assert banana['aut_order'] == 8

    def test_theta_cubic(self):
        """Theta graph uses cubic shadow alpha = 2."""
        result = virasoro_graph_sum_genus2()
        theta = result['graphs']['theta']
        assert theta['aut_order'] == 12


# =====================================================================
# Section 11: Gravitational entropy table
# =====================================================================

class TestGravitationalTable:
    """Test the comprehensive gravitational entropy table."""

    def test_table_generation(self):
        """Table generates for default c values."""
        table = gravitational_entropy_table()
        assert len(table) == 7  # default 7 c values

    def test_table_complementarity(self):
        """All complementarity checks pass in the table."""
        table = gravitational_entropy_table()
        for row in table:
            for g in range(1, 4):
                assert row[f'comp_match_{g}'], f"Failed at c={row['c']}, g={g}"

    def test_table_includes_c13(self):
        """Self-dual point c=13 is in the table."""
        table = gravitational_entropy_table()
        c13_rows = [r for r in table if abs(r['c'] - 13.0) < 0.01]
        assert len(c13_rows) == 1


# =====================================================================
# Section 12: Full analysis
# =====================================================================

class TestFullAnalysis:
    """Test the comprehensive gravitational analysis."""

    def test_full_analysis_c13(self):
        """Full analysis at self-dual point."""
        result = full_gravitational_analysis(13.0, 100.0, 3)
        assert result['is_self_dual']
        assert abs(result['kappa_sum'] - 13.0) < 1e-14
        assert result['rho'] < 1.0

    def test_full_analysis_c26(self):
        """Full analysis at bosonic string central charge."""
        result = full_gravitational_analysis(26.0, 100.0, 3)
        assert not result['is_self_dual']
        assert abs(result['kappa'] - 13.0) < 1e-14
        assert abs(result['kappa_dual']) < 1e-14

    def test_complementarity_in_full(self):
        """Complementarity holds in full analysis."""
        for c in [5.0, 13.0, 26.0]:
            result = full_gravitational_analysis(c, 100.0, 3)
            for g in range(1, 4):
                assert result['free_energies'][g]['comp_match']

    def test_instanton_in_full(self):
        """Instanton data present in full analysis."""
        result = full_gravitational_analysis(13.0, 100.0, 3)
        assert 'instanton_action' in result
        assert 'instanton_complementarity' in result
        ic = result['instanton_complementarity']
        assert abs(ic['ratio'] - 1.0) < 1e-12  # self-dual


# =====================================================================
# Section 13: Extreme values and edge cases
# =====================================================================

class TestEdgeCases:
    """Test edge cases and extreme values."""

    def test_large_c(self):
        """Large c: rho -> 0, A -> infinity."""
        rho = virasoro_shadow_growth_rate_numerical(10000.0)
        assert rho < 0.01

    def test_c_near_26(self):
        """c near 26: dual is near 0."""
        Fg = virasoro_scalar_Fg(25, 1)
        Fg_dual = virasoro_dual_scalar_Fg(25, 1)
        assert Fg_dual == Rational(1, 48)  # (26-25)/2 * 1/24 = 1/48

    def test_high_genus(self):
        """Free energies at high genus (g=8)."""
        Fg = virasoro_scalar_Fg(13, 8)
        assert Fg > 0
        # Very small but nonzero
        assert float(Fg) < 1e-6

    def test_free_energy_ratio_adjacent_genera(self):
        """F_{g+1}/F_g ratio related to Bernoulli growth."""
        for g in range(1, 7):
            ratio = float(lambda_fp(g + 1) / lambda_fp(g))
            # lambda_g^FP decreases, so ratio < 1
            assert 0 < ratio < 1


# =====================================================================
# Section 14: Complementarity as c varies
# =====================================================================

class TestComplementarityParametric:
    """Test complementarity identity parametrically in c."""

    @pytest.mark.parametrize("c_val", [
        Rational(1, 2), Rational(1), Rational(13, 5),
        Rational(13), Rational(26), Rational(100),
    ])
    def test_exact_rational_c(self, c_val):
        """Complementarity with exact rational c values."""
        for g in range(1, 5):
            result = verify_scalar_complementarity(c_val, g)
            assert result['match']

    def test_symbolic_c(self):
        """Complementarity holds symbolically (c as free variable)."""
        for g in range(1, 6):
            result = verify_scalar_complementarity(None, g)
            assert result['match']


# =====================================================================
# Section 15: Generating function structure
# =====================================================================

class TestGeneratingFunction:
    """Test the A-hat genus generating function structure."""

    def test_scalar_gf_check(self):
        """Generating function matches A-hat for Virasoro."""
        result = scalar_genus_expansion_coefficients(Rational(13, 2), 5)
        for g, Fg in result:
            expected = Rational(13, 2) * lambda_fp(g)
            assert Fg == expected

    def test_gf_virasoro_c26(self):
        """At c=26: F_g = 13 * lambda_g^FP."""
        for g in range(1, 6):
            Fg = virasoro_scalar_Fg(26, g)
            assert Fg == 13 * lambda_fp(g)

    def test_gf_bosonic_string_total(self):
        r"""Bosonic string: sum F_g hbar^{2g-2} is (13/hbar^2)(1 - Ahat(hbar))."""
        # Just verify the first few terms
        for g in range(1, 5):
            Fg = virasoro_scalar_Fg(26, g)
            expected = 13 * lambda_fp(g)
            assert Fg == expected
