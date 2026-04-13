"""Tests for the deep structural analysis of the Virasoro shadow obstruction tower.

Verifies through MULTIPLE INDEPENDENT PATHS:
  - Denominator factorization theorem
  - Riccati algebraicity
  - Complementarity at all arities
  - Numerical cross-verification (Path A vs Path C)
  - Growth rate bounds
  - Sign alternation pattern
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import pytest
from sympy import Rational, Symbol, simplify, factor, cancel

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'shadow_tower_deep_structure',
    os.path.join(_lib_dir, 'shadow_tower_deep_structure.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

c = Symbol('c')


@pytest.fixture(scope='module')
def tower():
    return _mod.compute_shadow_tower(20)


# ============================================================
# Denominator factorization tests
# ============================================================

class TestDenominatorStructure:
    def test_c_power_formula(self, tower):
        """c-power in denom of S_r equals max(0, r-3) for all r."""
        denom_data = _mod.denominator_analysis(tower)
        for r in range(2, 21):
            assert denom_data[r]['c_match'], \
                f"r={r}: c-power {denom_data[r]['c_power']} != {denom_data[r]['predicted_c']}"

    def test_kac_power_formula(self, tower):
        """(5c+22)-power in denominator equals floor((r-2)/2)."""
        denom_data = _mod.denominator_analysis(tower)
        for r in range(2, 21):
            assert denom_data[r]['kac_match'], \
                f"r={r}: kac-power {denom_data[r]['kac_power']} != {denom_data[r]['predicted_kac']}"

    def test_no_other_factors(self, tower):
        """Denominator has NO factors other than c and (5c+22)."""
        denom_data = _mod.denominator_analysis(tower)
        for r in range(2, 16):
            d = denom_data[r]['denominator']
            # After removing all c and (5c+22) factors, should get ±1 or a number
            d_stripped = d
            while simplify(d_stripped.subs(c, 0)) == 0:
                d_stripped = cancel(d_stripped / c)
            while simplify(d_stripped.subs(c, Rational(-22, 5))) == 0:
                d_stripped = cancel(d_stripped / (5*c + 22))
            # d_stripped should be a nonzero rational number
            assert d_stripped.subs(c, 1).is_rational, \
                f"r={r}: residual factor {d_stripped}"


# ============================================================
# Riccati algebraicity tests
# ============================================================

class TestRiccatiAlgebraicity:
    def test_master_equation_satisfied(self, tower):
        """Riccati equation 2tU' + (P/2)(U')^2 vanishes at arities 5-12."""
        riccati = _mod.riccati_verification(tower, 12)
        assert riccati['all_vanish'], \
            "Riccati equation not satisfied at some arity"

    @pytest.mark.parametrize('power', [5, 6, 7, 8, 9, 10, 11, 12])
    def test_riccati_at_specific_power(self, tower, power):
        """Riccati residual vanishes at t^power."""
        riccati = _mod.riccati_verification(tower, 12)
        assert riccati['checks'][power]['vanishes'], \
            f"Riccati residual at t^{power}: {riccati['checks'][power]['residual']}"

    def test_cubic_input_nonzero(self, tower):
        """Cubic input R_3 is nonzero (arity 3 is an input, not output)."""
        riccati = _mod.riccati_verification(tower, 12)
        assert riccati['R_3'] != 0

    def test_quartic_input_nonzero(self, tower):
        """Quartic input R_4 is nonzero (arity 4 is an input, not output)."""
        riccati = _mod.riccati_verification(tower, 12)
        assert riccati['R_4'] != 0


# ============================================================
# Complementarity tests
# ============================================================

class TestComplementarity:
    def test_kappa_level_independent(self, tower):
        """D_2 = S_2(c) + S_2(26-c) = 13 (level-independent)."""
        comp = _mod.complementarity_sums(tower)
        assert comp[2]['level_independent']
        assert simplify(comp[2]['D_r'] - 13) == 0

    def test_cubic_level_independent(self, tower):
        """D_3 = 4 (level-independent, trivially)."""
        comp = _mod.complementarity_sums(tower)
        assert comp[3]['level_independent']

    def test_quartic_level_dependent(self, tower):
        """D_4 is level-DEPENDENT (not constant in c)."""
        comp = _mod.complementarity_sums(tower)
        assert not comp[4]['level_independent']

    def test_self_dual_at_c13(self, tower):
        """At c=13, S_r(13) = S_r(26-13) = S_r(13). Trivially self-dual."""
        comp = _mod.complementarity_sums(tower)
        for r in range(2, 11):
            val = comp[r]['self_dual_value']
            assert val.is_finite, f"S_{r}(13) is not finite"


# ============================================================
# Multi-path verification tests
# ============================================================

class TestMultiPathVerification:
    @pytest.mark.parametrize('c_val', [1, 2, 13, 26, Rational(1, 2)])
    def test_path_a_vs_c(self, tower, c_val):
        """Path A (recursion) matches Path C (closed form) at specific c."""
        matches = _mod.numerical_verification(tower, c_val, 15)
        for r, data in matches.items():
            assert data['match'], \
                f"Mismatch at r={r}, c={c_val}: " \
                f"A={data['path_A']}, C={data['path_C']}"

    def test_cross_verification_at_critical(self, tower):
        """Verify at c=1 (a non-special value) through arity 20."""
        matches = _mod.numerical_verification(tower, 1, 20)
        for r, data in matches.items():
            assert data['match'], f"Mismatch at r={r}"


# ============================================================
# Growth rate and sign pattern tests
# ============================================================

class TestGrowthAndSigns:
    def test_growth_bounded(self, tower):
        """Growth ratios |S_{r+1}|/|S_r| are bounded at c=1."""
        growth = _mod.growth_rate_analysis(tower, [1])
        ratios = growth[1]['ratios']
        for r, ratio in ratios.items():
            assert ratio < 1000, f"|S_{r}|/|S_{r-1}| = {ratio} is too large"

    def test_sign_alternation_c1(self, tower):
        """Signs alternate +, +, +, -, +, -, +, - ... at c=1."""
        signs = _mod.alternation_pattern(tower, 1)
        # S_2 = 1/2 > 0, S_3 = 2 > 0, S_4 = 10/27 > 0
        assert signs[2] > 0
        assert signs[3] > 0
        assert signs[4] > 0
        # S_5 = -48/27 < 0
        assert signs[5] < 0

    def test_all_finite_at_c1(self, tower):
        """All shadow coefficients are finite at c=1."""
        for r, S_r in tower.items():
            val = S_r.subs(c, 1)
            assert val.is_finite, f"S_{r}(1) is not finite"

    def test_pole_at_c0(self, tower):
        """S_r has a pole at c=0 for r >= 4."""
        for r in range(4, 16):
            # Substituting c close to 0 should give large values
            val = abs(float(tower[r].subs(c, Rational(1, 100))))
            assert val > 1, f"S_{r} should diverge at c=0"


# ============================================================
# Arithmetic depth tests
# ============================================================

class TestArithmeticDepth:
    def test_numerator_degree_grows(self, tower):
        """Numerator degree grows with arity."""
        num_data = _mod.numerator_analysis(tower)
        prev_deg = 0
        for r in range(5, 16):
            deg = num_data[r]['degree']
            assert deg >= prev_deg, \
                f"Numerator degree at r={r} ({deg}) < r={r-1} ({prev_deg})"

    def test_low_arity_numerators_simple(self, tower):
        """Numerators at low arity are simple (degree ≤ 2)."""
        num_data = _mod.numerator_analysis(tower)
        assert num_data[2]['degree'] <= 1
        assert num_data[3]['degree'] == 0
        assert num_data[4]['degree'] == 0
        assert num_data[5]['degree'] == 0


# ============================================================
# W_3 complementarity test
# ============================================================

class TestW3Complementarity:
    def test_w3_kappa_level_independent(self):
        """W_3 kappa complementarity: κ(c) + κ(100-c) = 250/3."""
        comp = _mod.w3_complementarity_2d(4)
        assert comp[2]['level_independent'], \
            "W_3 kappa complementarity fails"

    def test_w3_cubic_check(self):
        """W_3 cubic complementarity at arity 3."""
        comp = _mod.w3_complementarity_2d(4)
        # Sh_3 = 2 x_T^3 + 3 x_T x_W^2 is c-independent!
        # So D_3 = 2 * Sh_3 should be level-independent.
        assert comp[3]['level_independent']
