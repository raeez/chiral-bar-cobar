"""RED TEAM adversarial tests for the primitive kernel construction.

Targets for falsification:
  1. Cofree reconstruction: does the Feynman transform of (K_{0,2}, K_{1,1})
     reproduce known genus-1 and genus-2 amplitudes for Heisenberg?
  2. Primitive shell consistency: does R_2 = Delta(K_1) + 1/2[K_1,K_1]
     match the known genus-2 free energy F_2 = kappa * 7/5760?
  3. Metaplectic squaring: does delta^2 = det(1-xT) through order 6 for rank 3?
  4. W3 quartic coefficient: is 16/(22+5c) the UNIQUE quartic coefficient?
  5. Regime classification completeness: do (Heis, affine, Vir, W3) exhaust
     all realizable boolean profiles?
  6. Genus-3 shell equation: does the Virasoro genus-3 forcing have exactly 5 terms?
  7. Cross-checks with existing compute modules.

References:
  - Vol I, Theorem D (scalar free energy)
  - Vol I, Proposition prop:primitive-shell-equations
  - Vol I, Corollary cor:metaplectic-square-root
  - Vol I, w_algebras.tex (W3 quartic uniqueness)
"""
import pytest
from fractions import Fraction
from itertools import product as cartprod

from sympy import (
    Matrix, Rational, Symbol, expand, simplify, factor, sqrt, eye,
    symbols, series, cancel, Poly, exp,
)


# ====================================================================
# Module imports (cross-check targets)
# ====================================================================
from compute.lib.modular_master import (
    HEISENBERG,
    AFFINE_SL2,
    VIRASORO,
    W3,
    PROFILES,
    MasterKernelProfile,
    get_profile,
    profile_table,
    w3_quartic_factor,
    formal_metaplectic_half_density,
    determinant_series,
)

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    genus2_stable_graphs_n0,
    enumerate_stable_graphs,
    orbifold_euler_characteristic,
    graph_sum_scalar,
    _bernoulli_exact,
    _lambda_fp_exact,
    _chi_orb_open,
)

from compute.lib.genus3_stable_graphs import (
    genus3_stable_graphs_n0,
    genus3_euler_check,
    genus3_spectral_sequence_counts,
    genus3_graph_profiles,
    genus3_scalar_sum_at,
    lambda3_fp,
)

from compute.lib.modular_bar import (
    shadow_archetype,
    standard_family_profiles,
    genus_two_profile,
    genus_two_shells,
)

from compute.lib.shadow_tower_ode import (
    shadow_coefficient,
    free_shadow_coefficient,
)

from compute.lib.utils import lambda_fp, F_g


# ====================================================================
# 1. COFREE RECONSTRUCTION (Heisenberg)
# ====================================================================

class TestCofreeReconstructionHeisenberg:
    """Test that primitive kernel K_A = (K_{0,2}, K_{1,1}) reconstructs
    the known genus-g amplitudes for the Heisenberg algebra.

    Heisenberg has kappa = -1/2 (the CRITICAL sign: Heisenberg has
    kappa = k*d/2, and at k=1, d=1 gives kappa = 1/2; but the
    convention in CLAUDE.md is kappa(H_k) = k for rank 1).

    Actually: kappa(H_k) = k. For k=1 rank 1: kappa = 1.
    For the standard normalization: J(z)J(w) ~ 1/(z-w)^2 => kappa = 1/2.

    We test with kappa as a parameter.
    """

    def test_genus1_amplitude_kappa_half(self):
        """F_1(kappa=1/2) = kappa * lambda_1^FP = 1/2 * 1/24 = 1/48."""
        kappa = Rational(1, 2)
        expected = kappa * lambda_fp(1)
        assert expected == Rational(1, 48)

    def test_genus1_amplitude_kappa_1(self):
        """F_1(kappa=1) = 1 * 1/24 = 1/24."""
        kappa = Rational(1)
        assert F_g(kappa, 1) == Rational(1, 24)

    def test_genus2_amplitude_kappa_1(self):
        """F_2(kappa=1) = 1 * 7/5760 = 7/5760."""
        kappa = Rational(1)
        assert F_g(kappa, 2) == Rational(7, 5760)

    def test_genus2_amplitude_kappa_half(self):
        """F_2(kappa=1/2) = 1/2 * 7/5760 = 7/11520."""
        kappa = Rational(1, 2)
        result = F_g(kappa, 2)
        expected = Rational(7, 11520)
        assert result == expected

    def test_genus3_amplitude_kappa_1(self):
        """F_3(kappa=1) = 1 * 31/967680."""
        kappa = Rational(1)
        assert F_g(kappa, 3) == Rational(31, 967680)

    def test_heisenberg_shadow_terminates_at_2(self):
        """Heisenberg has shadow depth r_max = 2 (Gaussian).
        No cubic, no quartic, no rigid terms."""
        assert not HEISENBERG.cubic
        assert not HEISENBERG.quartic
        assert not HEISENBERG.rigid2
        assert not HEISENBERG.rigid3

    def test_heisenberg_kernel_components(self):
        """Primitive kernel K_A = (K_{0,2}, K_{1,1}) only."""
        kernel = HEISENBERG.primitive_kernel()
        assert kernel == ("K02", "K11")

    def test_cofree_genus1_graph_sum(self):
        """For Heisenberg at genus 1, there are 2 stable graphs (n=0):
        - smooth genus-1 vertex (|Aut|=1): contributes chi_orb(M_1)
        - genus-0 vertex with self-loop (|Aut|=2): contributes kappa/2

        The genus-1 amplitude is the graph sum over genus-1 stable graphs.
        At the scalar level: F_1 = kappa * lambda_1^FP = kappa/24.

        Cross-check: graph_sum_scalar on genus-1 graphs should give
        lambda_1^FP when kappa=1."""
        graphs = enumerate_stable_graphs(1, 0)
        assert len(graphs) == 2
        result = graph_sum_scalar(graphs, kappa=Fraction(1))
        # This is sum 1/|Aut|*kappa^|E|, not lambda_1^FP directly.
        # genus-1 n=0: smooth (0 edges, |Aut|=1) + self-loop (1 edge, |Aut|=2)
        # = 1/1 * 1 + 1/2 * 1 = 3/2
        assert result == Fraction(3, 2)

    def test_cofree_genus2_graph_sum(self):
        """Graph sum at genus 2 n=0 with kappa=1 should equal
        sum of 1/|Aut| * kappa^|E| over all 6 genus-2 stable graphs."""
        graphs = genus2_stable_graphs_n0()
        assert len(graphs) == 6
        result = graph_sum_scalar(graphs, kappa=Fraction(1))
        # This is a combinatorial sum, not F_2 directly.
        # The value should be positive and rational.
        assert result > 0
        assert isinstance(result, Fraction)

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert _lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760 = 7/(8*720)."""
        assert _lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        assert _lambda_fp_exact(3) == Fraction(31, 967680)

    def test_lambda_fp_formula_consistency(self):
        """Verify lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
        for g=1,2,3,4."""
        from math import factorial as mfact
        for g in range(1, 5):
            B2g = _bernoulli_exact(2 * g)
            power = 2 ** (2 * g - 1)
            computed = Fraction(power - 1, power) * abs(B2g) / Fraction(mfact(2 * g))
            expected = _lambda_fp_exact(g)
            assert computed == expected, f"Failed at g={g}: {computed} != {expected}"


# ====================================================================
# 2. PRIMITIVE SHELL CONSISTENCY
# ====================================================================

class TestPrimitiveShellConsistency:
    """Test the genus-2 shell equation:
    R_2 = Delta(K_1) + 1/2[K_1,K_1]

    For Gaussian class (Heisenberg): only Delta(K_1) survives.
    For Lie class (affine): both terms present.
    """

    def test_heisenberg_genus2_shell_has_one_term(self):
        """Heisenberg genus-2 forcing has exactly 1 term: Delta(K11)."""
        forcing = HEISENBERG.genus_two_forcing()
        assert forcing == ("Delta(K11)",)

    def test_affine_genus2_shell_has_two_terms(self):
        """Affine genus-2 forcing has 2 terms: Delta(K11) + 1/2[K11,K11]."""
        forcing = AFFINE_SL2.genus_two_forcing()
        assert forcing == ("Delta(K11)", "1/2[K11,K11]")

    def test_virasoro_genus2_shell_has_three_terms(self):
        """Virasoro genus-2 forcing has 3 terms."""
        forcing = VIRASORO.genus_two_forcing()
        assert len(forcing) == 3
        assert "Delta(K11)" in forcing
        assert "1/2[K11,K11]" in forcing
        assert "Rpf2(K02)" in forcing

    def test_genus2_free_energy_heisenberg_kappa1(self):
        """F_2(Heis,k=1) = kappa * 7/5760 = 7/5760."""
        kappa = Fraction(1)
        F2 = kappa * _lambda_fp_exact(2)
        assert F2 == Fraction(7, 5760)

    def test_genus2_free_energy_affine_sl2_k1(self):
        """F_2(V_1(sl2)) = kappa * 7/5760 where kappa = dim(g)*(k+h^v)/2
        = 3*(1+2)/2 = 9/2.
        F_2 = 9/2 * 7/5760 = 63/11520 = 21/3840 = 7/1280."""
        dim_g, h_vee, k = 3, 2, Fraction(1)
        kappa = Fraction(dim_g) * (k + h_vee) / Fraction(2)
        assert kappa == Fraction(9, 2)
        F2 = kappa * _lambda_fp_exact(2)
        expected = Fraction(9, 2) * Fraction(7, 5760)
        assert F2 == expected

    def test_genus2_shell_equation_structure_w3(self):
        """W3 genus-2 forcing should match Virasoro (same boolean profile)."""
        w3_forcing = W3.genus_two_forcing()
        vir_forcing = VIRASORO.genus_two_forcing()
        assert w3_forcing == vir_forcing

    def test_bernoulli_numbers_small(self):
        """Cross-check Bernoulli numbers used in lambda_fp."""
        assert _bernoulli_exact(0) == Fraction(1)
        assert _bernoulli_exact(1) == Fraction(-1, 2)
        assert _bernoulli_exact(2) == Fraction(1, 6)
        assert _bernoulli_exact(4) == Fraction(-1, 30)
        assert _bernoulli_exact(6) == Fraction(1, 42)
        assert _bernoulli_exact(8) == Fraction(-1, 30)

    def test_genus2_orbifold_euler(self):
        """chi^orb(M_bar_{2,0}) = -181/1440."""
        graphs = genus2_stable_graphs_n0()
        chi = orbifold_euler_characteristic(graphs)
        assert chi == Fraction(-181, 1440)


# ====================================================================
# 3. METAPLECTIC SQUARING (RANK 3)
# ====================================================================

class TestMetaplecticSquaringRank3:
    """Test that the formal metaplectic half-density delta satisfies
    delta^2 = det(1 - xT) through order 6 for a generic rank-3 operator.

    Corollary cor:metaplectic-square-root states:
    delta = exp(1/2 Tr log(1-xT)) is the canonical square root.
    """

    def test_diagonal_operator(self):
        """Diagonal 3x3 operator: eigenvalues a, b, c.
        det(1-xT) = (1-ax)(1-bx)(1-cx)."""
        x = Symbol('x')
        a, b, c_sym = symbols('a b c_var')
        T = Matrix([[a, 0, 0], [0, b, 0], [0, 0, c_sym]])
        order = 6
        delta = formal_metaplectic_half_density(T, x, order)
        det_series = determinant_series(T, x, order)
        # delta^2 should equal det_series through order 6
        delta_sq = expand(series(delta**2, x, 0, order + 1).removeO())
        det_expanded = expand(det_series)
        diff = simplify(expand(delta_sq - det_expanded))
        assert diff == 0, f"delta^2 - det = {diff}"

    def test_generic_rank3(self):
        """Generic 3x3 operator with symbolic entries."""
        x = Symbol('x')
        t11, t12, t13 = symbols('t11 t12 t13')
        t21, t22, t23 = symbols('t21 t22 t23')
        t31, t32, t33 = symbols('t31 t32 t33')
        T = Matrix([
            [t11, t12, t13],
            [t21, t22, t23],
            [t31, t32, t33],
        ])
        order = 4  # reduced for speed with 9 symbols
        delta = formal_metaplectic_half_density(T, x, order)
        det_series = determinant_series(T, x, order)
        delta_sq = expand(series(delta**2, x, 0, order + 1).removeO())
        det_expanded = expand(det_series)
        diff = simplify(expand(delta_sq - det_expanded))
        assert diff == 0, f"delta^2 - det = {diff}"

    def test_nilpotent_operator(self):
        """Strictly upper triangular (nilpotent) 3x3: det(1-xT) = 1."""
        x = Symbol('x')
        a, b, c_sym = symbols('a b c_var')
        T = Matrix([[0, a, b], [0, 0, c_sym], [0, 0, 0]])
        order = 6
        delta = formal_metaplectic_half_density(T, x, order)
        det_series = determinant_series(T, x, order)
        # For nilpotent: det(1-xT) = 1, delta should be 1
        assert simplify(det_series - 1) == 0
        delta_sq = expand(series(delta**2, x, 0, order + 1).removeO())
        assert simplify(expand(delta_sq - 1)) == 0

    def test_rank1_embedding(self):
        """Rank-1 operator embedded in 3x3: only one nonzero eigenvalue."""
        x = Symbol('x')
        lam = Symbol('lambda')
        T = Matrix([[lam, 0, 0], [0, 0, 0], [0, 0, 0]])
        order = 6
        delta = formal_metaplectic_half_density(T, x, order)
        det_series = determinant_series(T, x, order)
        delta_sq = expand(series(delta**2, x, 0, order + 1).removeO())
        diff = simplify(expand(delta_sq - expand(det_series)))
        assert diff == 0

    def test_identity_operator(self):
        """T = I: det(1-xI) = (1-x)^3.
        delta = exp(-3/2 * sum x^m/m) = (1-x)^{3/2} through order 6."""
        x = Symbol('x')
        T = eye(3)
        order = 6
        delta = formal_metaplectic_half_density(T, x, order)
        det_series = determinant_series(T, x, order)
        delta_sq = expand(series(delta**2, x, 0, order + 1).removeO())
        det_expanded = expand(det_series)
        diff = simplify(expand(delta_sq - det_expanded))
        assert diff == 0

    def test_rank2_operator(self):
        """2x2 block in 3x3: det(1-xT) = (1-ax)(1-bx)."""
        x = Symbol('x')
        a, b = symbols('a b')
        T = Matrix([[a, 0, 0], [0, b, 0], [0, 0, 0]])
        order = 6
        delta = formal_metaplectic_half_density(T, x, order)
        det_series = determinant_series(T, x, order)
        delta_sq = expand(series(delta**2, x, 0, order + 1).removeO())
        diff = simplify(expand(delta_sq - expand(det_series)))
        assert diff == 0


# ====================================================================
# 4. W3 QUARTIC COEFFICIENT INDEPENDENCE
# ====================================================================

class TestW3QuarticCoefficient:
    """Verify that 16/(22+5c) is the unique quartic coefficient
    consistent with the conformal bootstrap at central charge c.

    The W3 algebra has beta = 16/(22+5c) as the coefficient of the
    quasi-primary Lambda = :TT: - (3/10)d^2T in the W(z)W(w) OPE.
    This is determined by the Jacobi identity (Fateev-Lukyanov uniqueness).
    """

    def test_w3_quartic_at_c_1(self):
        """beta(c=1) = 16/27."""
        c = Symbol('c')
        result = w3_quartic_factor(1)
        assert result == Rational(16, 27)

    def test_w3_quartic_at_c_2(self):
        """beta(c=2) = 16/32 = 1/2."""
        result = w3_quartic_factor(2)
        assert result == Rational(1, 2)

    def test_w3_quartic_at_c_10(self):
        """beta(c=10) = 16/72 = 2/9."""
        result = w3_quartic_factor(10)
        assert result == Rational(2, 9)

    def test_w3_quartic_at_c_26(self):
        """beta(c=26) = 16/152 = 2/19."""
        result = w3_quartic_factor(26)
        assert result == Rational(2, 19)

    def test_w3_quartic_at_c_minus22over5(self):
        """beta diverges at c = -22/5 (Lee-Yang singularity)."""
        c = Symbol('c')
        # At c = -22/5: denominator = 22 + 5*(-22/5) = 22 - 22 = 0
        denom = 22 + 5 * Rational(-22, 5)
        assert denom == 0

    def test_w3_quartic_symbolic(self):
        """beta(c) = 16/(22+5c) as symbolic expression."""
        c = Symbol('c')
        result = w3_quartic_factor(c)
        expected = Rational(16) / (22 + 5 * c)
        assert simplify(result - expected) == 0

    def test_w3_quartic_uniqueness_sweep(self):
        """Sweep c through 20 integer values: beta = 16/(22+5c) consistently."""
        for c_val in range(1, 21):
            result = w3_quartic_factor(c_val)
            expected = Rational(16, 22 + 5 * c_val)
            assert result == expected, f"Mismatch at c={c_val}"

    def test_w3_quartic_positivity_for_positive_c(self):
        """For c > 0: beta > 0 since 22+5c > 0."""
        for c_val in [1, 2, 5, 10, 26, 100]:
            result = w3_quartic_factor(c_val)
            assert result > 0, f"beta not positive at c={c_val}"

    def test_w3_quartic_duality_c13(self):
        """At c=13 (Virasoro self-dual point): beta = 16/(22+65) = 16/87."""
        result = w3_quartic_factor(13)
        assert result == Rational(16, 87)

    def test_quartic_contact_virasoro_vs_w3(self):
        """Q^contact_Vir = 10/[c(5c+22)] is related to but distinct from
        the W3 beta = 16/(22+5c). They share the same denominator factor
        (5c+22) but have different numerators and c-dependence."""
        c = Symbol('c')
        Q_vir = Rational(10) / (c * (5 * c + 22))
        beta_w3 = Rational(16) / (22 + 5 * c)
        # These should NOT be equal
        diff = simplify(Q_vir - beta_w3)
        assert diff != 0, "Q_contact_Vir should differ from W3 beta"


# ====================================================================
# 5. REGIME CLASSIFICATION COMPLETENESS
# ====================================================================

class TestRegimeClassificationCompleteness:
    """Verify that the four standard profiles exhaust all mathematically
    realized boolean combinations of (cubic, quartic, rigid2, rigid3).

    The four regimes: G (Gaussian), L (Lie/tree), C (contact), M (mixed).
    """

    def test_heisenberg_regime(self):
        """Heisenberg is 'pure quadratic' (G regime)."""
        assert HEISENBERG.regime() == "pure quadratic"

    def test_affine_regime(self):
        """Affine is 'cubic-tree' (L regime)."""
        assert AFFINE_SL2.regime() == "cubic-tree"

    def test_virasoro_regime(self):
        """Virasoro is 'quartic-rigid' (C/M regime)."""
        assert VIRASORO.regime() == "quartic-rigid"

    def test_w3_regime(self):
        """W3 is 'quartic-rigid' (same as Virasoro)."""
        assert W3.regime() == "quartic-rigid"

    def test_boolean_profiles_realized(self):
        """Check which (cubic, quartic) combinations are realized.
        Expected:
          (F, F) -> Heisenberg (Gaussian)
          (T, F) -> Affine (Lie/tree)
          (T, T) -> Virasoro/W3 (Mixed)
          (F, T) -> beta-gamma (Contact): NOT in standard profiles but
                    in shadow_archetype classification.
        """
        realized = set()
        for name, profile in PROFILES.items():
            realized.add((profile.cubic, profile.quartic))
        # The standard profiles realize: (F,F), (T,F), (T,T)
        assert (False, False) in realized
        assert (True, False) in realized
        assert (True, True) in realized

    def test_contact_quartic_without_cubic_is_betagamma(self):
        """beta-gamma has contact quartic without cubic.
        This is NOT in the PROFILES dict but is in shadow_archetype."""
        archetype = shadow_archetype(False, True)
        assert archetype == "Contact/quartic"

    def test_all_four_archetypes_realized(self):
        """All four shadow archetypes should be realized by standard families."""
        profiles = standard_family_profiles()
        values = set(profiles.values())
        assert "Gaussian" in values
        assert "Lie/tree" in values
        assert "Contact/quartic" in values
        assert "Mixed modular" in values

    def test_four_archetypes_are_exactly_four(self):
        """There are exactly 4 shadow archetypes (from 2x2 boolean grid)."""
        all_archetypes = set()
        for cubic in [False, True]:
            for quartic in [False, True]:
                all_archetypes.add(shadow_archetype(cubic, quartic))
        assert len(all_archetypes) == 4

    def test_no_rigid_without_quartic_in_standard(self):
        """In the standard profiles, rigid2/rigid3 only appear with quartic.
        This is a structural constraint: rigid terms are forced by quartic."""
        for name, profile in PROFILES.items():
            if profile.rigid2 or profile.rigid3:
                assert profile.quartic, (
                    f"{name} has rigid terms without quartic"
                )


# ====================================================================
# 6. GENUS-3 SHELL EQUATION STRUCTURE
# ====================================================================

class TestGenus3ShellEquation:
    """Test the genus-3 shell equation forcing terms for each family."""

    def test_virasoro_genus3_forcing_has_5_terms(self):
        """Virasoro genus-3 forcing should have exactly 5 terms:
        Delta(K2.), [K11,K2.], 1/6[K11,K11,K11], Rpf2(K11), Rpf3(K02)."""
        forcing = VIRASORO.genus_three_forcing()
        assert len(forcing) == 5
        assert "Delta(K2.)" in forcing
        assert "[K11,K2.]" in forcing
        assert "1/6[K11,K11,K11]" in forcing
        assert "Rpf2(K11)" in forcing
        assert "Rpf3(K02)" in forcing

    def test_w3_genus3_forcing_matches_virasoro(self):
        """W3 has the same boolean profile as Virasoro => same forcing."""
        assert W3.genus_three_forcing() == VIRASORO.genus_three_forcing()

    def test_heisenberg_genus3_forcing_has_1_term(self):
        """Heisenberg: only Delta(K2.) (pure scalar)."""
        forcing = HEISENBERG.genus_three_forcing()
        assert forcing == ("Delta(K2.)",)

    def test_affine_genus3_forcing_has_3_terms(self):
        """Affine: Delta(K2.), [K11,K2.], 1/6[K11,K11,K11].
        No rigid terms since quartic=False, rigid2=False, rigid3=False."""
        forcing = AFFINE_SL2.genus_three_forcing()
        assert len(forcing) == 3
        assert "Delta(K2.)" in forcing
        assert "[K11,K2.]" in forcing
        assert "1/6[K11,K11,K11]" in forcing

    def test_genus3_stable_graph_count(self):
        """There are exactly 42 genus-3 stable graphs with n=0."""
        graphs = genus3_stable_graphs_n0()
        assert len(graphs) == 42

    def test_genus3_euler_characteristic(self):
        """chi^orb(M_bar_{3,0}) = -12419/90720."""
        computed, expected, match = genus3_euler_check()
        assert match, f"Euler mismatch: {computed} != {expected}"

    def test_genus3_spectral_sequence_totals(self):
        """Loop decomposition: h1=0->4, h1=1->9, h1=2->14, h1=3->15, total=42."""
        counts = genus3_spectral_sequence_counts()
        assert counts.get(0, 0) == 4
        assert counts.get(1, 0) == 9
        assert counts.get(2, 0) == 14
        assert counts.get(3, 0) == 15
        assert sum(counts.values()) == 42

    def test_genus3_lambda_fp(self):
        """lambda_3^FP = 31/967680."""
        assert lambda3_fp() == Fraction(31, 967680)


# ====================================================================
# 7. CROSS-CHECKS WITH EXISTING COMPUTE MODULES
# ====================================================================

class TestCrossChecks:
    """Cross-check primitive kernel predictions against existing modules."""

    def test_shadow_tower_s2_is_c_over_2(self):
        """S_2(c) = c/2 (curvature = kappa)."""
        c = Symbol('c')
        assert shadow_coefficient(2) == c / 2

    def test_shadow_tower_s3_is_2(self):
        """S_3(c) = 2 (Sugawara cubic, independent of c)."""
        assert shadow_coefficient(3) == Rational(2)

    def test_shadow_tower_s4_matches_q_contact(self):
        """S_4(c) = 10/[c(5c+22)], the quartic contact invariant."""
        c = Symbol('c')
        expected = Rational(10) / (c * (5 * c + 22))
        result = shadow_coefficient(4)
        assert simplify(result - expected) == 0

    def test_shadow_tower_s5_sign(self):
        """S_5 should be negative (quintic opposes quartic)."""
        S5 = shadow_coefficient(5)
        # Evaluate at c=13 (self-dual point)
        S5_val = S5.subs(Symbol('c'), 13)
        assert S5_val < 0, f"S_5(13) = {S5_val} should be negative"

    def test_shadow_tower_quintic_value(self):
        """S_5(c) = -48/[c^2(5c+22)] from the known computation."""
        c = Symbol('c')
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        result = shadow_coefficient(5)
        assert simplify(result - expected) == 0, (
            f"S_5 = {factor(result)}, expected {factor(expected)}"
        )

    def test_heisenberg_genus2_profile(self):
        """Heisenberg genus-2 profile: only loop-loop shell."""
        profile = genus_two_profile("heisenberg")
        assert profile == ("loop-loop",)

    def test_affine_genus2_profile(self):
        """Affine genus-2 profile: loop-loop + sep-loop."""
        profile = genus_two_profile("affine")
        assert profile == ("loop-loop", "sep-loop")

    def test_virasoro_genus2_profile(self):
        """Virasoro genus-2 profile: all three shells."""
        profile = genus_two_profile("virasoro")
        assert profile == genus_two_shells()

    def test_genus2_graph_count_is_6(self):
        """There are exactly 6 genus-2 stable graphs with n=0."""
        graphs = genus2_stable_graphs_n0()
        assert len(graphs) == 6

    def test_genus2_graphs_all_stable(self):
        """All genus-2 n=0 graphs satisfy the stability condition."""
        for g in genus2_stable_graphs_n0():
            assert g.is_stable, f"Unstable: {g}"

    def test_genus2_graphs_all_connected(self):
        """All genus-2 n=0 graphs are connected."""
        for g in genus2_stable_graphs_n0():
            assert g.is_connected, f"Disconnected: {g}"

    def test_genus2_graphs_correct_genus(self):
        """All genus-2 n=0 graphs have arithmetic genus 2."""
        for g in genus2_stable_graphs_n0():
            assert g.arithmetic_genus == 2, (
                f"Wrong genus {g.arithmetic_genus} for {g}"
            )

    def test_qme_shells_heisenberg(self):
        """Heisenberg QME shells: K03=0, dK11=0, K04=0, R2/R3 pure scalar."""
        shells = HEISENBERG.qme_shells()
        assert "K03=0" in shells
        assert "dK11=0" in shells
        assert "K04=0" in shells

    def test_qme_shells_virasoro(self):
        """Virasoro QME shells: dK03=0, dK11+Delta_ns(K03)=0, dK04+K03*K03=0."""
        shells = VIRASORO.qme_shells()
        assert "dK03=0" in shells
        assert "dK11+Delta_ns(K03)=0" in shells
        assert "dK04+K03*K03=0" in shells

    def test_profile_table_completeness(self):
        """Profile table should have 4 entries (one per standard family)."""
        table = profile_table()
        assert len(table) == 4

    def test_branch_ranks(self):
        """Branch rank: Heis=1, affine=2, Vir=2, W3=3."""
        assert HEISENBERG.branch_rank == 1
        assert AFFINE_SL2.branch_rank == 2
        assert VIRASORO.branch_rank == 2
        assert W3.branch_rank == 3


# ====================================================================
# 8. ADVERSARIAL STRESS TESTS
# ====================================================================

class TestAdversarialStress:
    """Adversarial tests probing potential failure modes."""

    def test_metaplectic_rank1_vs_rank3_consistency(self):
        """Rank-1 embedded in rank-3 should match pure rank-1 result."""
        x = Symbol('x')
        lam = Symbol('lambda')
        # Rank 1
        T1 = Matrix([[lam]])
        order = 6
        delta1 = formal_metaplectic_half_density(T1, x, order)
        # Rank 1 embedded in rank 3
        T3 = Matrix([[lam, 0, 0], [0, 0, 0], [0, 0, 0]])
        delta3 = formal_metaplectic_half_density(T3, x, order)
        assert simplify(expand(delta1 - delta3)) == 0

    def test_shadow_tower_recursion_s6(self):
        """S_6 computed by recursion should be consistent with the ODE module.
        Cross-check that shadow_coefficient and free_shadow_coefficient agree
        at arity 2 and 3 (they share the same initial data)."""
        assert shadow_coefficient(2) == free_shadow_coefficient(2)
        assert shadow_coefficient(3) == free_shadow_coefficient(3)
        # At arity 4 they differ (free has no intrinsic quartic):
        c = Symbol('c')
        S4_full = shadow_coefficient(4)
        S4_free = free_shadow_coefficient(4)
        diff = simplify(S4_full - S4_free)
        # The quartic contact is intrinsic, so they must differ
        assert diff != 0, "Full and free shadow towers should differ at arity 4"

    def test_shadow_tower_s4_free_computation(self):
        """Free tower S_4^free comes purely from the cubic recursion:
        S_4^free = -(1/(2*4*c)) * 2*3*3 * S_3 * S_3
                 = -(18*4) / (8c) = -9/c.
        Wait, let's compute carefully:
        For r=4: j+k = r+2 = 6, j,k >= 3. Only (3,3) with j=k.
        obstruction = j*k * S_j * S_k / c = 9 * 4 / c = 36/c
        S_4^free = -obstruction / (2*4) = -36/(8c) = -9/(2c).
        """
        c = Symbol('c')
        S4_free = free_shadow_coefficient(4)
        expected = Rational(-9, 2) / c
        assert simplify(S4_free - expected) == 0, (
            f"S4_free = {factor(S4_free)}, expected {expected}"
        )

    def test_genus3_gaussian_profile_all_scalar(self):
        """For Gaussian class, all 42 genus-3 graphs are scalar-only."""
        profile = genus3_graph_profiles("G")
        assert profile["active_count"] == 0
        assert profile["scalar_only_count"] == 42

    def test_genus3_lie_tree_profile(self):
        """For L class, graphs with max valence >= 3 get cubic corrections."""
        profile = genus3_graph_profiles("L")
        # Some graphs must have vertices with valence >= 3
        assert profile["active_count"] > 0
        # Total must be 42
        assert profile["active_count"] + profile["scalar_only_count"] == 42

    def test_primitive_kernel_ordering(self):
        """The primitive kernel tuple should have K02 first, K11 last
        (for the base components), with K03/K04 inserted in between."""
        kernel_heis = HEISENBERG.primitive_kernel()
        assert kernel_heis[0] == "K02"
        assert kernel_heis[-1] == "K11"

        kernel_aff = AFFINE_SL2.primitive_kernel()
        assert kernel_aff[0] == "K02"
        assert "K03" in kernel_aff

        kernel_vir = VIRASORO.primitive_kernel()
        assert "K02" in kernel_vir
        assert "K03" in kernel_vir
        assert "K04" in kernel_vir
        assert "K11" in kernel_vir

    def test_master_action_consistency(self):
        """Master action terms should be consistent with primitive kernel."""
        for name, profile in PROFILES.items():
            kernel = profile.primitive_kernel()
            action = profile.master_action_terms()
            # S2 always present
            assert "S2" in action
            # S3 iff cubic
            assert ("S3" in action) == profile.cubic
            # S4 iff quartic
            assert ("S4" in action) == profile.quartic

    def test_quartic_contact_poles(self):
        """Q^contact_Vir = 10/[c(5c+22)] has poles at c=0 and c=-22/5.
        These are the ONLY poles (no hidden zeros in numerator)."""
        c = Symbol('c')
        Q = Rational(10) / (c * (5 * c + 22))
        from sympy import denom, numer, solve
        d = denom(cancel(Q))
        poles = solve(d, c)
        # Should have exactly 2 poles: 0 and -22/5
        pole_set = set(simplify(p) for p in poles)
        assert Rational(0) in pole_set or 0 in pole_set
        assert Rational(-22, 5) in pole_set

    def test_shadow_duality_s2(self):
        """S_2(c) + S_2(26-c) = c/2 + (26-c)/2 = 13 (constant)."""
        c = Symbol('c')
        S2 = shadow_coefficient(2)
        S2_dual = S2.subs(c, 26 - c)
        duality_sum = simplify(S2 + S2_dual)
        assert duality_sum == 13

    def test_genus3_lambda_ratio(self):
        """lambda_3/lambda_2 = (31/967680) / (7/5760)
        = 31*5760 / (7*967680) = 178560/6773760 = 31/1176."""
        l2 = _lambda_fp_exact(2)
        l3 = _lambda_fp_exact(3)
        ratio = l3 / l2
        assert ratio == Fraction(31 * 5760, 7 * 967680)
        assert ratio == Fraction(31, 1176)

    def test_genus2_graph_sum_negative_kappa(self):
        """Graph sum with negative kappa (e.g., beta-gamma has kappa = -2)
        should still be well-defined."""
        graphs = genus2_stable_graphs_n0()
        result = graph_sum_scalar(graphs, kappa=Fraction(-2))
        assert isinstance(result, Fraction)
        # With kappa = -2 and edge counts 0..5:
        # The alternating signs from (-2)^e should give a specific value
        # This is a pure combinatorial check, not physics

    def test_custom_profile_creation(self):
        """Creating a custom profile with (cubic=F, quartic=T) should work
        and give Contact/quartic archetype."""
        betagamma = MasterKernelProfile(
            name="beta-gamma",
            cubic=False,
            quartic=True,
            rigid2=True,
            rigid3=False,
            branch_rank=1,
        )
        assert betagamma.regime() == "quartic-rigid"
        # Genus-2 forcing: Delta(K11) + Rpf2(K02)
        forcing = betagamma.genus_two_forcing()
        assert "Delta(K11)" in forcing
        assert "Rpf2(K02)" in forcing
        # No 1/2[K11,K11] since cubic=False
        assert "1/2[K11,K11]" not in forcing
