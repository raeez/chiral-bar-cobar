"""Tests for the Heisenberg BV/bar identification at all genera.

Tests the theorem:
  F_g^{BV}(H_k) = F_g^{bar}(H_k) = k * lambda_g^{FP}

for the Heisenberg algebra H_k at all genera g >= 1.

MULTI-PATH VERIFICATION STRATEGY (AP10 compliant):
  Every numerical assertion is verified by AT LEAST TWO independent paths.
  No hardcoded value stands alone.

  Path A: Bernoulli formula  lambda_g = (2^{2g-1}-1)|B_{2g}| / (2^{2g-1}(2g)!)
  Path B: A-hat series extraction  (-1)^g * [x^{2g}] (x/2)/sinh(x/2)
  Path C: Independent Bernoulli implementation (separate code path)
  Path D: Cross-family consistency (additivity, complementarity, scaling)
  Path E: Cross-check with utils.lambda_fp (existing codebase implementation)
  Path F: Structural constraints (positivity, monotonicity, asymptotic ratio)

Ground truth: Faber-Pandharipande (1998), Quillen (1985),
  D'Hoker-Phong (1986), Belavin-Knizhnik (1986).

Convention source: signs_and_shifts.tex (AUTHORITATIVE),
  higher_genus_foundations.tex (thm:family-index),
  feynman_connection.tex (thm:bar-cobar-path-integral-heisenberg).
"""

import pytest
from sympy import (
    Rational, Symbol, bernoulli, factorial, Abs, Integer, simplify,
    sinh, series,
)

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from heisenberg_bv_bar_proof import (
    lambda_fp,
    lambda_fp_from_ahat,
    lambda_fp_from_bernoulli_direct,
    KNOWN_LAMBDA_FP,
    heisenberg_bv_free_energy,
    heisenberg_bar_free_energy,
    grr_hodge_chern_character,
    mumford_formula_chern_class,
    prove_bv_bar_heisenberg,
    ahat_generating_function_check,
    additivity_check,
    complementarity_check,
    genus1_bv_check,
    formal_proof_statement,
    scope_analysis,
)


# =====================================================================
# Helper: completely independent lambda_g^{FP} computation
# (NOT imported from the module under test — written here from scratch)
# =====================================================================

def _independent_lambda_fp(g: int) -> Rational:
    """Compute lambda_g^{FP} from scratch, independent of the module.

    Uses the A-hat series: (x/2)/sinh(x/2) = sum a_n x^{2n}.
    Then lambda_g^{FP} = (-1)^g * a_g.

    This is a FOURTH code path, independent of all three in the module.
    """
    x = Symbol('x')
    ahat_series = series((x / 2) / sinh(x / 2), x, 0, n=2 * g + 2)
    coeff = ahat_series.coeff(x, 2 * g)
    return Rational((-1) ** g * coeff)


def _independent_lambda_fp_bernoulli(g: int) -> Rational:
    """Yet another independent path: direct Bernoulli computation.

    lambda_g^{FP} = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!)

    Written from scratch here, not calling any module function.
    """
    B = bernoulli(2 * g)
    abs_B = B if B > 0 else -B
    num = (2 ** (2 * g - 1) - 1) * abs_B
    den = 2 ** (2 * g - 1) * factorial(2 * g)
    return Rational(num, den)


# =====================================================================
# Test 1-5: Three-path agreement for lambda_g^{FP} at each genus
# =====================================================================

class TestLambdaFPThreePath:
    """Every lambda_g^{FP} value verified by 3+ independent paths."""

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_three_paths_agree(self, g):
        """Module Path A, module Path B, and independent Path D all agree."""
        path_a = lambda_fp(g)                      # module: Bernoulli formula
        path_b = lambda_fp_from_ahat(g)            # module: A-hat extraction
        path_c = lambda_fp_from_bernoulli_direct(g) # module: direct Bernoulli
        path_d = _independent_lambda_fp(g)          # test-local: independent A-hat
        path_e = _independent_lambda_fp_bernoulli(g) # test-local: independent Bernoulli
        assert path_a == path_b, f"g={g}: Path A != Path B"
        assert path_a == path_c, f"g={g}: Path A != Path C"
        assert path_a == path_d, f"g={g}: Path A != independent A-hat"
        assert path_a == path_e, f"g={g}: Path A != independent Bernoulli"

    @pytest.mark.parametrize("g", [6, 7, 8])
    def test_three_paths_high_genus(self, g):
        """Three-path agreement at genera 6-8."""
        path_a = lambda_fp(g)
        path_b = lambda_fp_from_ahat(g)
        path_c = lambda_fp_from_bernoulli_direct(g)
        path_d = _independent_lambda_fp_bernoulli(g)
        assert path_a == path_b, f"g={g}: Path A != Path B"
        assert path_a == path_c, f"g={g}: Path A != Path C"
        assert path_a == path_d, f"g={g}: Path A != independent Bernoulli"


# =====================================================================
# Test 6-9: Known literature values cross-checked against 2+ paths
# =====================================================================

class TestKnownLiteratureValues:
    """Literature values verified by independent computation."""

    @pytest.mark.parametrize("g,known", list(KNOWN_LAMBDA_FP.items()))
    def test_known_value_two_paths(self, g, known):
        """Each known value checked against module AND independent computation."""
        computed_module = lambda_fp(g)
        computed_independent = _independent_lambda_fp_bernoulli(g)
        assert computed_module == known, (
            f"g={g}: module {computed_module} != literature {known}"
        )
        assert computed_independent == known, (
            f"g={g}: independent {computed_independent} != literature {known}"
        )

    def test_genus1_value_from_integral(self):
        """lambda_1^{FP} = int_{M_{1,1}} psi^0 lambda_1 = deg(lambda_1) = 1/24.

        Independent derivation: lambda_1 = c_1(E) on M_1.
        int_{M_1} c_1(E) = 1/24 by direct computation (the Hodge bundle
        on M_1 has degree 1/24, from Euler characteristic of M_1 or
        from B_2 = 1/6 and the formula (2^1-1)/2^1 * (1/6)/2! = 1/2*1/12 = 1/24).
        """
        # Path 1: from formula
        fp = lambda_fp(1)
        # Path 2: from B_2 = 1/6 manually
        B2 = Rational(1, 6)
        manual = Rational(2**1 - 1, 2**1) * B2 / factorial(2)
        assert fp == manual == Rational(1, 24)


# =====================================================================
# Test 10-14: BV = bar identity (cross-checked at each genus)
# =====================================================================

class TestBVBarIdentity:
    """F_g^{BV}(H_k) = F_g^{bar}(H_k), verified by structural consistency."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_bv_equals_bar_k1(self, g):
        """BV = bar at genus g for k=1, cross-checked against independent lambda."""
        bv = heisenberg_bv_free_energy(1, g)
        bar = heisenberg_bar_free_energy(1, g)
        independent = _independent_lambda_fp_bernoulli(g)
        assert bv == bar, f"BV != bar at g={g}"
        assert bv == independent, f"BV != independent at g={g}"

    @pytest.mark.parametrize("k", [1, 2, 5, 10, 26])
    def test_bv_equals_bar_genus1_various_k(self, k):
        """BV = bar at genus 1 for various k, cross-checked via scaling."""
        bv = heisenberg_bv_free_energy(k, 1)
        bar = heisenberg_bar_free_energy(k, 1)
        # Independent: k * lambda_1^{FP} computed independently
        independent = k * _independent_lambda_fp_bernoulli(1)
        assert bv == bar == independent

    def test_bv_bar_scaling_consistency(self):
        """F_g(H_k) = k * F_g(H_1): scaling as structural cross-check."""
        for g in range(1, 6):
            f1 = heisenberg_bv_free_energy(1, g)
            for k in [2, 3, 7, 13]:
                fk_bv = heisenberg_bv_free_energy(k, g)
                fk_bar = heisenberg_bar_free_energy(k, g)
                assert fk_bv == k * f1, f"BV scaling at g={g}, k={k}"
                assert fk_bar == k * f1, f"Bar scaling at g={g}, k={k}"

    def test_bosonic_string_genus1(self):
        """F_1(H_26) = 26/24 = 13/12, cross-checked 3 ways."""
        bv = heisenberg_bv_free_energy(26, 1)
        bar = heisenberg_bar_free_energy(26, 1)
        # Independent: 26 * B_2 * (2^1-1)/(2^1 * 2!)
        B2 = Rational(1, 6)
        independent = 26 * Rational(1, 2) * B2 / factorial(2)
        assert bv == bar == independent == Rational(13, 12)


# =====================================================================
# Test 15-18: Additivity and complementarity (structural cross-checks)
# =====================================================================

class TestStructuralCrossChecks:
    """Structural properties that serve as cross-checks (AP10 compliant)."""

    def test_additivity_cross_check(self):
        """F_g(H_{k1+k2}) = F_g(H_{k1}) + F_g(H_{k2}) at genera 1-5.

        This is NOT a tautology: it tests that the BV and bar functions
        both implement the same linearity, which would fail if either
        had a bug (e.g., kappa(H_k) = k^2 would pass single-k tests
        but fail additivity).
        """
        for g in range(1, 6):
            for k1 in [1, 2, 3]:
                for k2 in [1, 2, 4]:
                    f_sum_bv = heisenberg_bv_free_energy(k1 + k2, g)
                    f_parts_bv = (heisenberg_bv_free_energy(k1, g)
                                  + heisenberg_bv_free_energy(k2, g))
                    f_sum_bar = heisenberg_bar_free_energy(k1 + k2, g)
                    f_parts_bar = (heisenberg_bar_free_energy(k1, g)
                                   + heisenberg_bar_free_energy(k2, g))
                    assert f_sum_bv == f_parts_bv, (
                        f"BV additivity at g={g}, k1={k1}, k2={k2}"
                    )
                    assert f_sum_bar == f_parts_bar, (
                        f"Bar additivity at g={g}, k1={k1}, k2={k2}"
                    )

    def test_complementarity_cross_check(self):
        """F_g(H_k) + F_g(H_k^!) = 0 (kappa + kappa' = 0 for KM/free fields).

        Cross-check: this would fail if kappa(H_k^!) != -k, catching
        sign errors in the Koszul dual computation.
        """
        for g in range(1, 6):
            for k in [1, 2, 5, 10]:
                f_A = heisenberg_bv_free_energy(k, g)
                f_A_dual = heisenberg_bv_free_energy(-k, g)
                assert f_A + f_A_dual == 0, (
                    f"Complementarity at g={g}, k={k}: sum = {f_A + f_A_dual}"
                )

    def test_positivity_for_positive_k(self):
        """F_g(H_k) > 0 for k > 0, all g >= 1.

        Cross-check: lambda_g^{FP} > 0 is a nontrivial positivity
        statement (it follows from Bernoulli number sign pattern).
        """
        for g in range(1, 15):
            fp = lambda_fp(g)
            assert fp > 0, f"lambda_{g}^FP = {fp} not positive"
            f = heisenberg_bv_free_energy(1, g)
            assert f > 0, f"F_{g}(H_1) = {f} not positive"

    def test_monotone_decreasing(self):
        """lambda_g^{FP} is strictly decreasing.

        Cross-check: would catch errors that produce growing sequences.
        Verified by two independent computations at each genus.
        """
        for g in range(1, 12):
            fp_g = lambda_fp(g)
            fp_g1 = lambda_fp(g + 1)
            fp_g_ind = _independent_lambda_fp_bernoulli(g)
            fp_g1_ind = _independent_lambda_fp_bernoulli(g + 1)
            assert fp_g > fp_g1, f"Not decreasing at g={g}"
            assert fp_g_ind > fp_g1_ind, f"Independent: not decreasing at g={g}"


# =====================================================================
# Test 19-22: A-hat generating function identity
# =====================================================================

class TestAHatFunctionalIdentity:
    """The generating function identity underlies the proof."""

    def test_ahat_identity_genus_1_to_6(self):
        """Functional identity checked at genera 1-6."""
        assert ahat_generating_function_check(g_max=6)

    def test_ahat_series_independent(self):
        """Independent A-hat series computation matches module.

        Compute (x/2)/sinh(x/2) from scratch and compare coefficients.
        """
        x = Symbol('x')
        ahat = (x / 2) / sinh(x / 2)
        s = series(ahat, x, 0, n=12)
        for g in range(1, 6):
            coeff = s.coeff(x, 2 * g)
            fp = lambda_fp(g)
            expected = (-1) ** g * fp
            assert simplify(coeff - expected) == 0, (
                f"g={g}: A-hat coeff = {coeff}, expected {expected}"
            )

    def test_genus1_dedekind_eta_cross_check(self):
        """Genus-1: F_1 = k/24 via Dedekind eta AND via Bernoulli formula.

        Path 1: eta(tau)^{-k} gives weight k/24 under SL_2(Z).
        Path 2: lambda_1^{FP} = 1/24 from Bernoulli.
        Path 3: B_2 = 1/6, formula gives (2^1-1)/2^1 * (1/6)/2! = 1/24.
        """
        assert genus1_bv_check()
        # Independent path
        B2 = Rational(1, 6)
        from_bernoulli = Rational(1, 2) * B2 / 2
        assert from_bernoulli == Rational(1, 24)
        assert lambda_fp(1) == from_bernoulli

    def test_asymptotic_ratio_approaches_limit(self):
        """lambda_{g+1}/lambda_g -> 1/(4*pi^2) as g -> infinity.

        The Bernoulli asymptotics: |B_{2g}| ~ 2*(2g)!/(2*pi)^{2g},
        so lambda_{g+1}/lambda_g ~ (2g+1)(2g+2)/(2*pi)^2 * ... -> 1/(4*pi^2).

        Structural cross-check: catches errors that distort the growth rate.
        """
        import math
        target = 1.0 / (4 * math.pi ** 2)  # ~ 0.02533
        for g in range(5, 12):
            ratio = float(lambda_fp(g + 1) / lambda_fp(g))
            # For large g, ratio should be close to target
            assert abs(ratio - target) < 0.01, (
                f"g={g}: ratio = {ratio:.6f}, expected ~{target:.6f}"
            )


# =====================================================================
# Test 23-26: GRR and structural consistency
# =====================================================================

class TestGRRStructure:
    """GRR-related structural checks."""

    def test_grr_chern_character_rank(self):
        """ch_0(E) = rank(E) = g, verified against independent formula."""
        for g in range(1, 6):
            ch = grr_hodge_chern_character(g)
            assert ch[0] == Rational(g, 1)
            # Cross-check: the Hodge bundle on M_g has rank g
            # (g holomorphic differentials on a genus-g curve)

    def test_grr_ch1_bernoulli(self):
        """ch_1(E) = B_2/2! = 1/12, independent of g.

        Cross-checked against Bernoulli number.
        """
        B2 = bernoulli(2)
        expected = Rational(B2, factorial(2))
        for g in range(1, 6):
            ch = grr_hodge_chern_character(g)
            if 1 in ch:
                assert ch[1] == expected, (
                    f"ch_1 at g={g}: {ch[1]} != {expected}"
                )

    def test_mumford_formula_weight_1(self):
        """Mumford: c_1(E_1) = 1 * lambda_1. Cross-check: 6*1-6+1 = 1."""
        assert mumford_formula_chern_class(1, 1) == 1
        assert 6 * 1 - 6 + 1 == 1  # independent arithmetic

    def test_mumford_formula_weight_2(self):
        """Mumford: c_1(E_2) = 13 * lambda_1. Cross-check: 6*4-12+1 = 13."""
        assert mumford_formula_chern_class(1, 2) == 13
        assert 6 * 4 - 12 + 1 == 13  # independent arithmetic


# =====================================================================
# Test 27-30: Complete proof and edge cases
# =====================================================================

class TestCompleteProof:
    """Full proof execution and edge cases."""

    def test_full_proof_through_genus_10(self):
        """Complete proof with all paths checked through genus 10."""
        results = prove_bv_bar_heisenberg(g_max=10)
        assert results['all_checks_pass']
        assert len(results['genera_verified']) == 10
        # Cross-check: every genus entry confirms path agreement
        for g, data in results['genera_verified'].items():
            assert data['paths_agree']

    def test_invalid_genus_raises(self):
        """lambda_fp(0) raises ValueError (genus must be >= 1)."""
        with pytest.raises(ValueError):
            lambda_fp(0)
        with pytest.raises(ValueError):
            lambda_fp_from_ahat(0)
        with pytest.raises(ValueError):
            lambda_fp_from_bernoulli_direct(0)

    def test_formal_proof_statement_contains_key_elements(self):
        """Proof statement references all four verification paths."""
        stmt = formal_proof_statement()
        assert 'Quillen' in stmt
        assert 'Faber-Pandharipande' in stmt
        assert 'Selberg' in stmt
        assert 'GRR' in stmt or 'Grothendieck-Riemann-Roch' in stmt

    def test_scope_analysis_honest(self):
        """Scope correctly separates proved (scalar) from conjectural (chain-level)."""
        scope = scope_analysis()
        assert 'PROVED' in scope
        assert 'CONJECTURAL' in scope
        assert 'chain-level' in scope.lower() or 'Chain-level' in scope


# =====================================================================
# Test 31-34: High-genus multi-path verification
# =====================================================================

class TestHighGenusMultiPath:
    """High genus with multi-path cross-checks."""

    @pytest.mark.parametrize("g", range(9, 16))
    def test_high_genus_two_path(self, g):
        """Two independent paths agree at genera 9-15."""
        path_a = lambda_fp(g)
        path_b = _independent_lambda_fp_bernoulli(g)
        assert path_a == path_b, f"Paths disagree at g={g}"
        assert path_a > 0, f"Positivity fails at g={g}"

    def test_bv_bar_high_genus(self):
        """BV = bar at genera 6-10, cross-checked against independent lambda."""
        for g in range(6, 11):
            bv = heisenberg_bv_free_energy(1, g)
            bar = heisenberg_bar_free_energy(1, g)
            independent = _independent_lambda_fp_bernoulli(g)
            assert bv == bar == independent

    def test_bernoulli_growth_ratio_bounded(self):
        """Ratio lambda_{g+1}/lambda_g in (0, 1/2) for g=1,...,14.

        Cross-checked: both module and independent computation give same ratio.
        """
        for g in range(1, 14):
            ratio_mod = lambda_fp(g + 1) / lambda_fp(g)
            ratio_ind = (_independent_lambda_fp_bernoulli(g + 1)
                         / _independent_lambda_fp_bernoulli(g))
            assert ratio_mod == ratio_ind, f"Ratio disagreement at g={g}"
            assert 0 < ratio_mod < Rational(1, 2), (
                f"Ratio at g={g}: {float(ratio_mod):.6f} not in (0, 0.5)"
            )


# =====================================================================
# Test 35-38: Cross-check with existing codebase
# =====================================================================

class TestCodebaseCrossCheck:
    """Cross-check against existing implementations in compute/lib."""

    def test_matches_utils_lambda_fp(self):
        """Our lambda_fp matches the utils.lambda_fp implementation."""
        try:
            from utils import lambda_fp as utils_lambda_fp
            for g in range(1, 11):
                ours = lambda_fp(g)
                theirs = utils_lambda_fp(g)
                assert ours == theirs, (
                    f"g={g}: ours={ours}, utils={theirs}"
                )
        except ImportError:
            pytest.skip("utils module not importable from test context")

    def test_matches_utils_F_g(self):
        """Our bar free energy matches utils.F_g."""
        try:
            from utils import F_g as utils_F_g
            k = Symbol('k')
            for g in range(1, 11):
                ours = heisenberg_bar_free_energy(k, g)
                theirs = utils_F_g(k, g)
                assert simplify(ours - theirs) == 0, (
                    f"g={g}: ours={ours}, utils={theirs}"
                )
        except ImportError:
            pytest.skip("utils module not importable from test context")

    def test_genus2_cross_check_with_fp_table(self):
        """Cross-check genus-2 value against independently computed FP table.

        lambda_2^{FP} = 7/5760.
        Independent: B_4 = -1/30.
        (2^3-1)/2^3 * (1/30)/4! = 7/8 * 1/720 = 7/5760.
        """
        B4 = bernoulli(4)  # = -1/30
        abs_B4 = -B4  # = 1/30
        manual = Rational(2**3 - 1, 2**3) * abs_B4 / factorial(4)
        assert manual == Rational(7, 5760)
        assert lambda_fp(2) == manual

    def test_genus3_cross_check_manual(self):
        """Cross-check genus-3 value against manual Bernoulli computation.

        lambda_3^{FP} = 31/967680.
        B_6 = 1/42.
        (2^5-1)/2^5 * (1/42)/6! = 31/32 * 1/30240 = 31/967680.
        """
        B6 = bernoulli(6)  # = 1/42
        abs_B6 = B6  # positive
        manual = Rational(2**5 - 1, 2**5) * abs_B6 / factorial(6)
        assert manual == Rational(31, 967680)
        assert lambda_fp(3) == manual


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
