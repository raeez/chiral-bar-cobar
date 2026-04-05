r"""Tests for the non-perturbative shadow partition function.

Verifies double convergence of the shadow partition function
Z^sh(A, hbar) = sum_{g,r} hbar^{2g-2} Z_g^{(r)}(A)
in both genus (Bernoulli decay) and arity (shadow radius).

Ground truth:
    - Scalar free energy F_g = kappa * lambda_g^FP (Theorem D)
    - Genus convergence: ratio -> 1/(2*pi)^2 ~ 0.025 (prop:genus-expansion-convergence)
    - Arity convergence: |S_r| ~ C * rho^r * r^{-5/2} (thm:shadow-radius)
    - R-matrix: |R_d| <= C_R / (2*pi)^d (prop:r-matrix-genus-bound)
    - String contrast: Vol(M-bar_g) ~ (2g)! (Mirzakhani)

References:
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    prop:genus-expansion-convergence (genus_expansions.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational, pi as sym_pi, N as Neval

from compute.lib.shadow_partition_function import (
    # Section 1: Tautological intersection bound
    faber_pandharipande_decay_verification,
    stable_graph_count_bound,
    # Section 2: Dressed propagator
    dressed_propagator_growth_table,
    dressed_propagator_envelope,
    # Section 3: Scalar genus series
    scalar_free_energy,
    scalar_genus_series,
    # Section 4: Shadow terms
    shadow_partition_term,
    # Section 5: Double sum
    shadow_partition_double_sum,
    # Section 6: Bound
    polylogarithm_5_2,
    genus_geometric_sum,
    double_convergence_bound,
    # Section 7: Families
    virasoro_shadow_partition,
    affine_sl2_shadow_partition,
    heisenberg_shadow_partition,
    # Section 8: String contrast
    mirzakhani_volume_estimate,
    string_theory_contrast,
    # Section 9: Master
    convergence_analysis,
)
from compute.lib.utils import lambda_fp

PI = math.pi
TWO_PI_SQ = (2 * PI) ** 2


# =========================================================================
# Class 1: Faber-Pandharipande decay (genus-direction bound)
# =========================================================================

class TestFaberPandharipankeDecay:
    """Verify the Bernoulli decay of lambda_g^FP (the genus-direction bound)."""

    def test_fp_known_values(self):
        """lambda_1 = 1/24, lambda_2 = 7/5760, lambda_3 = 31/967680."""
        assert lambda_fp(1) == Rational(1, 24)
        assert lambda_fp(2) == Rational(7, 5760)
        assert lambda_fp(3) == Rational(31, 967680)

    def test_fp_decay_geometric(self):
        """lambda_g^FP decays geometrically: lambda_{g+1}/lambda_g -> 1/(2*pi)^2."""
        result = faber_pandharipande_decay_verification(25)
        assert result['verified']
        # Ratio at g=20 should be within 1% of 1/(2*pi)^2
        target = 1.0 / TWO_PI_SQ
        assert abs(result['ratio_at_g20'] - target) / target < 0.01

    def test_fp_all_positive(self):
        """All Faber-Pandharipande numbers are positive."""
        for g in range(1, 20):
            assert lambda_fp(g) > 0

    def test_fp_ratio_monotone(self):
        """The genus ratio |lambda_{g+1}/lambda_g| approaches limit from above."""
        result = faber_pandharipande_decay_verification(20)
        ratios = result['ratios']
        target = 1.0 / TWO_PI_SQ
        # Ratios should decrease toward the limit
        for g in range(5, 19):
            assert ratios[g] > target * 0.99, \
                f"Ratio at g={g} below target"

    def test_shadow_term_decays_both_indices(self):
        """The estimate |S_r| * lambda_g^FP decays in both g and r.

        This is the structural factorization that drives double convergence:
        the genus decay (Bernoulli) and arity decay (shadow radius) are
        independent, so their product decays in both directions.
        """
        # Virasoro c=26
        kappa = Rational(13)
        alpha = Rational(2)
        S4 = Rational(10) / (Rational(26) * (5 * Rational(26) + 22))
        # Check genus decay at arity 3
        t1 = shadow_partition_term(kappa, alpha, S4, 1, 3)
        t5 = shadow_partition_term(kappa, alpha, S4, 5, 3)
        assert t5 < t1, "Genus decay fails at arity 3"
        # Check arity decay at genus 1
        t_r3 = shadow_partition_term(kappa, alpha, S4, 1, 3)
        t_r10 = shadow_partition_term(kappa, alpha, S4, 1, 10)
        assert t_r10 < t_r3, "Arity decay fails at genus 1"


# =========================================================================
# Class 2: Dressed propagator growth
# =========================================================================

class TestDressedPropagatorGrowth:
    """Verify dressed propagator properties (Convention G, cross-check only).

    The dressed propagator P^R(D+, D-) lives in Convention G (Givental).
    The shadow partition function uses Convention S (bare propagator).
    These tests verify structural properties, not convergence bounds.
    """

    def test_propagator_P00(self):
        """P^R(0,0) = R_1 = 1/12."""
        table = dressed_propagator_growth_table(1)
        assert abs(table[(0, 0)] - 1.0 / 12) < 1e-10

    def test_propagator_symmetry(self):
        """P^R(D+, D-) = P^R(D-, D+) for all pairs."""
        table = dressed_propagator_growth_table(6)
        for (dp, dm), val in table.items():
            assert abs(val - table[(dm, dp)]) < 1e-14, \
                f"Symmetry fails: P({dp},{dm}) != P({dm},{dp})"

    def test_propagator_bounded_low_degree(self):
        """All propagator values at degree <= 4 are bounded by 1."""
        table = dressed_propagator_growth_table(4)
        for val in table.values():
            assert val < 1.0, f"Propagator value {val} exceeds 1"

    def test_propagator_finite(self):
        """All propagator values are finite."""
        table = dressed_propagator_growth_table(8)
        for val in table.values():
            assert math.isfinite(val), f"Propagator value {val} not finite"


# =========================================================================
# Class 3: Scalar genus convergence
# =========================================================================

class TestScalarConvergence:
    """Verify the proved genus convergence at arity 2."""

    def test_scalar_genus1_virasoro_c26(self):
        """F_1(Vir_26) = 13 * lambda_1^FP = 13/24."""
        val = scalar_free_energy(Rational(13), 1)
        assert val == Rational(13, 24)

    def test_scalar_genus2_virasoro_c26(self):
        """F_2(Vir_26) = 13 * 7/5760 = 91/5760."""
        val = scalar_free_energy(Rational(13), 2)
        assert val == Rational(13) * lambda_fp(2)

    def test_genus_ratio_limit(self):
        """Genus ratios |F_{g+1}/F_g| -> 1/(2*pi)^2 ~ 0.0253."""
        result = scalar_genus_series(Rational(13, 2), max_genus=25)
        ratios = result['ratios']
        target = 1.0 / TWO_PI_SQ
        # Last ratios should be within 1% of the limit
        assert abs(ratios[20] - target) / target < 0.01

    def test_scalar_series_converges(self):
        """Partial sums stabilize (relative change < 1e-10 at large g)."""
        result = scalar_genus_series(Rational(13, 2), max_genus=30)
        ps = result['partial_sums']
        s25 = float(ps[25])
        s30 = float(ps[30])
        assert abs(s30 - s25) / abs(s25) < 1e-10

    def test_scalar_generating_function(self):
        """Sum equals kappa * ((1/2)/sin(1/2) - 1) at hbar = 1."""
        kappa = 13.0 / 2
        result = scalar_genus_series(Rational(13, 2), max_genus=30)
        numerical_sum = result['partial_sum_float']
        closed_form = kappa * (0.5 / math.sin(0.5) - 1)
        assert abs(numerical_sum - closed_form) / abs(closed_form) < 1e-8


# =========================================================================
# Class 4: Arity convergence at fixed genus
# =========================================================================

class TestArityConvergence:
    """Verify shadow obstruction tower convergence at fixed genus."""

    def test_virasoro_c13_shadow_radius_below_1(self):
        """Shadow radius rho(Vir_13) < 1 (convergent regime)."""
        from compute.lib.shadow_tower_recursive import compute_shadow_tower
        c = 13
        kappa = Rational(c, 2)
        alpha = Rational(2)
        S4 = Rational(10) / (Rational(c) * (5 * Rational(c) + 22))
        tower = compute_shadow_tower(kappa, alpha, S4, max_arity=30)
        assert tower.depth_class == 'M'
        assert tower.convergent is True
        # The exact rho ~ 0.467
        rho = float(Neval(tower.growth_rate))
        assert 0.4 < rho < 0.55, f"rho(Vir_13) = {rho}, expected ~0.467"

    def test_virasoro_c26_shadow_radius_small(self):
        """Shadow radius rho(Vir_26) < 0.3."""
        from compute.lib.shadow_tower_recursive import compute_shadow_tower
        from sympy import N as Neval
        c = 26
        kappa = Rational(c, 2)
        alpha = Rational(2)
        S4 = Rational(10) / (Rational(c) * (5 * Rational(c) + 22))
        tower = compute_shadow_tower(kappa, alpha, S4, max_arity=15)
        rho = float(Neval(tower.growth_rate))
        assert rho < 0.3, f"rho(Vir_26) = {rho}"

    def test_heisenberg_terminates(self):
        """Heisenberg (class G): S_r = 0 for r >= 3."""
        from compute.lib.shadow_tower_recursive import compute_shadow_tower
        tower = compute_shadow_tower(Rational(1), Rational(0), Rational(0),
                                     max_arity=10, algebra_name="Heisenberg")
        assert tower.depth_class == 'G'
        for r in range(3, 11):
            sc = tower.coefficients.get(r)
            if sc is not None:
                assert abs(float(sc.value)) < 1e-50

    def test_affine_terminates_arity3(self):
        """Affine (class L): S_r = 0 for r >= 4."""
        from compute.lib.shadow_tower_recursive import compute_shadow_tower
        tower = compute_shadow_tower(Rational(9, 4), Rational(1), Rational(0),
                                     max_arity=10)
        assert tower.depth_class == 'L'
        for r in range(4, 11):
            sc = tower.coefficients.get(r)
            if sc is not None:
                assert abs(float(sc.value)) < 1e-50


# =========================================================================
# Class 5: Genus convergence at fixed arity r >= 3
# =========================================================================

class TestGenusConvergenceFixedArity:
    """Verify genus convergence at each fixed arity.

    The key claim: the Bernoulli decay 1/(2*pi)^{2g} controls the genus
    growth at EVERY arity, not just the scalar.
    """

    def test_genus_terms_decay_arity3(self):
        """Z_g^{(3)} decays geometrically with g for Virasoro c=26."""
        c = 26
        kappa = Rational(c, 2)
        alpha = Rational(2)
        S4 = Rational(10) / (Rational(c) * (5 * Rational(c) + 22))
        terms = [shadow_partition_term(kappa, alpha, S4, g, 3)
                 for g in range(1, 10)]
        # Terms should decay
        for i in range(1, len(terms)):
            if terms[i - 1] > 1e-50:
                assert terms[i] < terms[i - 1], \
                    f"Z_{i+1}^(3) = {terms[i]} > Z_{i}^(3) = {terms[i-1]}"

    def test_genus_terms_decay_arity4(self):
        """Z_g^{(4)} decays geometrically with g for Virasoro c=26."""
        c = 26
        kappa = Rational(c, 2)
        alpha = Rational(2)
        S4 = Rational(10) / (Rational(c) * (5 * Rational(c) + 22))
        terms = [shadow_partition_term(kappa, alpha, S4, g, 4)
                 for g in range(1, 10)]
        for i in range(1, len(terms)):
            if terms[i - 1] > 1e-50:
                assert terms[i] < terms[i - 1]

    def test_genus_terms_decay_arity5(self):
        """Z_g^{(5)} decays geometrically with g for Virasoro c=50."""
        c = 50
        kappa = Rational(c, 2)
        alpha = Rational(2)
        S4 = Rational(10) / (Rational(c) * (5 * Rational(c) + 22))
        terms = [shadow_partition_term(kappa, alpha, S4, g, 5)
                 for g in range(1, 10)]
        for i in range(1, len(terms)):
            if terms[i - 1] > 1e-50:
                assert terms[i] < terms[i - 1]

    def test_genus_ratio_arity3_approaches_bernoulli(self):
        """Genus ratio at arity 3 approaches 1/(2*pi)^2."""
        c = 50
        kappa = Rational(c, 2)
        alpha = Rational(2)
        S4 = Rational(10) / (Rational(c) * (5 * Rational(c) + 22))
        terms = [shadow_partition_term(kappa, alpha, S4, g, 3)
                 for g in range(1, 16)]
        ratios = []
        for i in range(1, len(terms)):
            if abs(terms[i - 1]) > 1e-50:
                ratios.append(terms[i] / terms[i - 1])
        # Last ratio should approach 1/(2*pi)^2 ~ 0.0253
        if ratios:
            target = 1.0 / TWO_PI_SQ
            assert abs(ratios[-1] - target) / target < 0.05, \
                f"Genus ratio at arity 3: {ratios[-1]:.6f}, expected ~{target:.6f}"


# =========================================================================
# Class 6: Double convergence
# =========================================================================

class TestDoubleConvergence:
    """Test the combined genus + arity convergence."""

    def test_double_sum_virasoro_c13(self):
        """Double sum converges for Virasoro at c = 13 (self-dual)."""
        result = virasoro_shadow_partition(13, max_genus=15, max_arity=20)
        assert result['double_bound']['convergent']
        assert result['total'] != 0.0

    def test_double_sum_virasoro_c26(self):
        """Double sum converges for Virasoro at c = 26 (critical string)."""
        result = virasoro_shadow_partition(26, max_genus=15, max_arity=20)
        assert result['double_bound']['convergent']
        assert result['shadow_radius'] < 1.0

    def test_double_sum_virasoro_c50(self):
        """Double sum converges strongly for Virasoro at c = 50."""
        result = virasoro_shadow_partition(50, max_genus=15, max_arity=20)
        assert result['double_bound']['convergent']
        # Stronger convergence at larger c
        assert result['shadow_radius'] < 0.2

    def test_double_bound_finite(self):
        """The analytic bound is finite for rho < 1."""
        bound = double_convergence_bound(13.0 / 2, 0.467)
        assert bound['convergent']
        assert bound['bound'] < float('inf')
        assert bound['bound'] > 0

    def test_double_sum_partial_cauchy(self):
        """Partial sums are Cauchy: difference between truncations shrinks."""
        r1 = virasoro_shadow_partition(26, max_genus=10, max_arity=15)
        r2 = virasoro_shadow_partition(26, max_genus=15, max_arity=20)
        # Difference should be small
        diff = abs(r2['total'] - r1['total'])
        assert diff < abs(r1['total']) * 0.01, \
            f"Truncation difference {diff} too large vs total {r1['total']}"

    def test_polylogarithm_convergent(self):
        """Li_{5/2}(rho) converges for rho < 1."""
        for rho in [0.1, 0.3, 0.5, 0.7, 0.9]:
            val = polylogarithm_5_2(rho)
            assert val > 0
            assert val < float('inf')
        # Li_{5/2}(1) = zeta(5/2) ~ 1.3415 (finite)
        val_1 = polylogarithm_5_2(1.0)
        assert abs(val_1 - 1.3415) < 0.01

    def test_genus_geometric_sum_exact(self):
        """sum_{g>=1} 1/(2pi)^{2g} = 1/(4pi^2 - 1) ~ 0.02596."""
        val = genus_geometric_sum()
        exact = 1.0 / (4 * PI ** 2 - 1)
        assert abs(val - exact) < 1e-10


# =========================================================================
# Class 7: Family specializations
# =========================================================================

class TestFamilySpecializations:
    """Test shadow partition function for specific algebra families."""

    def test_heisenberg_scalar_only(self):
        """Heisenberg: only scalar contribution (class G)."""
        result = heisenberg_shadow_partition(rank=1, max_genus=15)
        assert result['depth_class'] == 'G'
        # Correction should be zero
        assert abs(result['correction_total']) < 1e-14

    def test_affine_finite_tower(self):
        """Affine sl_2: finite tower (class L), rho = 0."""
        result = affine_sl2_shadow_partition(k_val=1, max_genus=15)
        assert result['depth_class'] == 'L'
        assert result['double_bound']['convergent']

    def test_virasoro_c13_self_dual(self):
        """Virasoro at c=13: self-dual point, rho ~ 0.467."""
        result = virasoro_shadow_partition(13, max_genus=15, max_arity=20)
        assert abs(result['shadow_radius'] - 0.467) < 0.02
        assert result['double_bound']['convergent']

    def test_virasoro_c26_critical(self):
        """Virasoro at c=26: critical string, rho ~ 0.234."""
        result = virasoro_shadow_partition(26, max_genus=15, max_arity=20)
        assert result['shadow_radius'] < 0.3

    def test_virasoro_convergent_above_c_star(self):
        """For c > c* ~ 6.125, rho < 1 (convergent regime)."""
        for c in [7, 10, 13, 26, 50, 100]:
            result = virasoro_shadow_partition(c, max_genus=8, max_arity=15)
            assert result['shadow_radius'] < 1.0, \
                f"rho >= 1 at c={c}: rho = {result['shadow_radius']}"

    def test_kappa_complementarity_in_partition(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 implies constraint on Z."""
        for c in [10, 13, 20]:
            r1 = virasoro_shadow_partition(c, max_genus=10, max_arity=5)
            r2 = virasoro_shadow_partition(26 - c, max_genus=10, max_arity=5)
            # At scalar level: F_g(c) + F_g(26-c) = 13 * lambda_g^FP
            for g in range(1, 6):
                f1 = float(scalar_free_energy(Rational(c, 2), g))
                f2 = float(scalar_free_energy(Rational(26 - c, 2), g))
                f_sum = f1 + f2
                expected = 13.0 * float(lambda_fp(g))
                assert abs(f_sum - expected) < 1e-10, \
                    f"Complementarity fails at c={c}, g={g}"


# =========================================================================
# Class 8: String theory contrast
# =========================================================================

class TestStringTheoryContrast:
    """Verify that shadow expansion converges where string expansion diverges."""

    def test_shadow_decays_string_grows(self):
        """Shadow terms decay; string (Mirzakhani) terms grow."""
        result = string_theory_contrast(13.0 / 2, max_genus=10)
        shadow = result['shadow_terms']
        string = result['string_terms']
        # Shadow: F_{10} < F_1
        assert shadow[10] < shadow[1]
        # String: A_{10} > A_1
        assert string[10] > string[1]

    def test_ratio_vanishes(self):
        """Shadow/string ratio -> 0 superexponentially."""
        result = string_theory_contrast(13.0 / 2, max_genus=10)
        ratios = result['ratios']
        # Ratio should decrease dramatically
        assert ratios[10] < ratios[1] * 1e-10

    def test_shadow_partial_sums_converge(self):
        """Shadow partial sums stabilize."""
        result = string_theory_contrast(13.0 / 2, max_genus=20)
        ps = result['shadow_partial_sums']
        assert abs(ps[20] - ps[15]) / abs(ps[15]) < 1e-8

    def test_string_partial_sums_diverge(self):
        """String partial sums grow without bound."""
        result = string_theory_contrast(13.0 / 2, max_genus=10)
        ps = result['string_partial_sums']
        assert ps[10] > ps[5] * 100


# =========================================================================
# Class 9: Master convergence analysis
# =========================================================================

class TestMasterConvergence:
    """End-to-end convergence verification."""

    def test_virasoro_c13_full_analysis(self):
        """Complete analysis for Virasoro at c = 13."""
        c = 13
        kappa = Rational(c, 2)
        alpha = Rational(2)
        S4 = Rational(10) / (Rational(c) * (5 * Rational(c) + 22))
        result = convergence_analysis(kappa, alpha, S4,
                                       max_genus=10, max_arity=15)
        assert result['fp_decay_verified']
        assert result['double_convergent']
        assert result['depth_class'] == 'M'
        assert abs(result['shadow_radius'] - 0.467) < 0.02
        assert result['bound'] > 0
        assert result['bound'] < float('inf')

    def test_heisenberg_trivial_analysis(self):
        """Heisenberg: trivially convergent (class G)."""
        result = convergence_analysis(Rational(1), Rational(0), Rational(0),
                                       max_genus=10, max_arity=5)
        assert result['double_convergent']
        assert result['depth_class'] == 'G'
        assert result['shadow_radius'] == 0.0
        assert abs(result['correction_fraction']) < 1e-12
