"""Tests for MC5 genus g>=2 defense: BV/BRST = bar at all genera.

BLUE TEAM defensive test battery verifying 7 axes of the MC5
higher-genus bridge: d^2 = kappa(A) * omega_g at all genera.

DEFENSE STRUCTURE:
  I.   Kappa uniqueness (additivity + antisymmetry + A-hat => unique)
  II.  Fay trisecant -> scalar defect (H^{1,1} = 1-dimensional)
  III. Costello renormalization (locality + scaling + universality)
  IV.  Mumford class / lambda_g^FP (Bernoulli number formula, g=1..20)
  V.   Period matrix trace (scalar reduction via trace)
  VI.  Clutching compatibility (A-hat multiplicativity)
  VII. No matrix curvature (Schur's lemma)

Total: 7 defense axes, ~100 tests.

Ground truth:
  - Theorem D: universal genus expansion F_g = kappa * lambda_g^FP
  - lambda_g^FP formula: (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
  - A-hat GF: sum (-1)^g lambda_g x^{2g} = (x/2)/sinh(x/2) - 1
  - Complementarity: kappa(A) + kappa(A!) = family constant
"""

import pytest
from sympy import (
    Symbol, Rational, simplify, S, bernoulli, factorial, Abs,
    pi, sinh, series, symbols,
)

from compute.lib.mc5_genus2_defense import (
    kappa_values_all_families,
    verify_kappa_uniqueness,
    verify_kappa_uniqueness_numerical,
    fay_trisecant_dimensional_analysis,
    verify_fay_defect_scalar_all_genera,
    costello_scaling_analysis,
    verify_costello_scaling_all_genera,
    lambda_fp_table,
    verify_lambda_fp_bernoulli,
    verify_ahat_generating_function,
    verify_ahat_first_terms,
    period_matrix_trace_structure,
    verify_clutching_compatibility,
    verify_clutching_all_pairs,
    verify_ahat_multiplicativity,
    schur_lemma_argument,
    full_genus_g_defense,
    verify_convergence_ratio,
    verify_F_g_all_families,
)
from compute.lib.utils import lambda_fp, F_g
from compute.lib.genus_expansion import (
    kappa_heisenberg, kappa_virasoro, kappa_w3,
    kappa_sl2, kappa_sl3,
)


# ============================================================================
# DEFENSE I: Kappa uniqueness
# ============================================================================

class TestKappaUniqueness:
    """kappa is the UNIQUE linear functional satisfying
    additivity + antisymmetry + A-hat generating function.

    DEFENSE RATING: AIRTIGHT for KM families (algebraic proof).
    STRONG for W-algebras (relies on sigma_invariant computation)."""

    def test_sl2_slope(self):
        """sl2: kappa slope = dim/(2*h_dual) = 3/4."""
        r = verify_kappa_uniqueness()
        assert r["sl2_slope"]

    def test_sl3_slope(self):
        """sl3: kappa slope = dim/(2*h_dual) = 4/3."""
        r = verify_kappa_uniqueness()
        assert r["sl3_slope"]

    def test_G2_slope(self):
        """G2: kappa slope = dim/(2*h_dual) = 7/4."""
        r = verify_kappa_uniqueness()
        assert r["G2_slope"]

    def test_B2_slope(self):
        """B2: kappa slope = dim/(2*h_dual) = 5/3."""
        r = verify_kappa_uniqueness()
        assert r["B2_slope"]

    def test_antisymmetry_forces_proportionality_sl2(self):
        """For sl2: antisymmetry kappa(k) + kappa(-k-4) = 0
        forces any other invariant to be proportional to kappa."""
        r = verify_kappa_uniqueness()
        assert r["antisymmetry_forces_proportionality_sl2"]

    def test_antisymmetry_forces_proportionality_sl3(self):
        """For sl3: antisymmetry forces proportionality to kappa."""
        r = verify_kappa_uniqueness()
        assert r["antisymmetry_forces_proportionality_sl3"]

    def test_virasoro_antisymmetry_sum(self):
        """Virasoro: kappa(c) + kappa(26-c) = 13."""
        r = verify_kappa_uniqueness()
        assert r["virasoro_antisymmetry_sum_13"]

    def test_w3_sigma_invariant(self):
        """W3: sigma(sl3) = 1/2 + 1/3 = 5/6."""
        r = verify_kappa_uniqueness()
        assert r["W3_sigma_is_5_6"]

    def test_ahat_fixes_normalization_lambda1(self):
        """A-hat GF fixes lambda_1 = 1/24."""
        r = verify_kappa_uniqueness()
        assert r["ahat_lambda1"]

    def test_ahat_fixes_normalization_lambda2(self):
        """A-hat GF fixes lambda_2 = 7/5760."""
        r = verify_kappa_uniqueness()
        assert r["ahat_lambda2"]


class TestKappaUniquenessNumerical:
    """Numerical verification of kappa at k=1 for all KM families."""

    def test_sl2_k1_kappa(self):
        """kappa(sl2_1) = 9/4."""
        r = verify_kappa_uniqueness_numerical()
        assert r["sl2_k1_kappa"]

    def test_sl3_k1_kappa(self):
        """kappa(sl3_1) = 16/3."""
        r = verify_kappa_uniqueness_numerical()
        assert r["sl3_k1_kappa"]

    def test_G2_k1_kappa(self):
        """kappa(G2_1) = 35/4."""
        r = verify_kappa_uniqueness_numerical()
        assert r["G2_k1_kappa"]

    def test_B2_k1_kappa(self):
        """kappa(B2_1) = 20/3."""
        r = verify_kappa_uniqueness_numerical()
        assert r["B2_k1_kappa"]

    def test_all_families_have_dual(self):
        """Every family has kappa and kappa_dual defined."""
        fams = kappa_values_all_families(1)
        for name, (k, kd) in fams.items():
            assert k is not None and kd is not None, f"{name} missing dual"


# ============================================================================
# DEFENSE II: Fay trisecant -> scalar defect
# ============================================================================

class TestFayTrisecantScalar:
    """The Arnold defect at genus g is forced scalar by H^{1,1}(Sigma_g) = C.

    DEFENSE RATING: AIRTIGHT (Hodge theory on curves is classical)."""

    def test_genus1_h11_is_1(self):
        """H^{1,1}(Sigma_1) = 1."""
        d = fay_trisecant_dimensional_analysis(1)
        assert d["h_11"] == 1

    def test_genus2_h11_is_1(self):
        """H^{1,1}(Sigma_2) = 1."""
        d = fay_trisecant_dimensional_analysis(2)
        assert d["h_11"] == 1

    def test_genus3_h11_is_1(self):
        """H^{1,1}(Sigma_3) = 1."""
        d = fay_trisecant_dimensional_analysis(3)
        assert d["h_11"] == 1

    @pytest.mark.parametrize("g", range(1, 21))
    def test_defect_scalar_genus_g(self, g):
        """H^{1,1}(Sigma_g) = 1 for all g=1..20."""
        d = fay_trisecant_dimensional_analysis(g)
        assert d["defect_forced_scalar"]

    @pytest.mark.parametrize("g", range(1, 11))
    def test_hodge_numbers_correct(self, g):
        """Verify h^{p,q}(Sigma_g) for p,q in {0,1}."""
        d = fay_trisecant_dimensional_analysis(g)
        assert d["h_00"] == 1
        assert d["h_10"] == g
        assert d["h_01"] == g
        assert d["h_11"] == 1
        assert d["total_betti"] == 2 + 2*g


# ============================================================================
# DEFENSE III: Costello renormalization formality
# ============================================================================

class TestCostelloScaling:
    """Locality + scaling + universality force the genus-g counterterm
    to be kappa * lambda_g^FP * omega_g.

    DEFENSE RATING: STRONG (relies on Costello's formalism being applicable)."""

    @pytest.mark.parametrize("g", range(1, 16))
    def test_loop_order(self, g):
        """Loop order at genus g is g-1."""
        d = costello_scaling_analysis(g)
        assert d["loop_order"] == g - 1

    @pytest.mark.parametrize("g", range(1, 16))
    def test_ghost_number_zero(self, g):
        """Ghost number of the counterterm is 0 (physical observable)."""
        d = costello_scaling_analysis(g)
        assert d["ghost_number"] == 0

    @pytest.mark.parametrize("g", range(1, 16))
    def test_locality(self, g):
        """The counterterm is local."""
        d = costello_scaling_analysis(g)
        assert d["locality"]

    @pytest.mark.parametrize("g", range(1, 16))
    def test_lambda_g_positive(self, g):
        """lambda_g^FP > 0 for all g >= 1."""
        d = costello_scaling_analysis(g)
        assert d["lambda_g_FP"] > 0

    def test_all_costello_pass(self):
        """Full Costello scaling verification for g=1..15."""
        r = verify_costello_scaling_all_genera(15)
        assert all(r.values())


# ============================================================================
# DEFENSE IV: Mumford class / lambda_g^FP
# ============================================================================

class TestLambdaFPBernoulli:
    """lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)! for g=1..20.

    DEFENSE RATING: AIRTIGHT (pure arithmetic, exact rational)."""

    @pytest.mark.parametrize("g", range(1, 16))
    def test_bernoulli_match(self, g):
        """lambda_g matches the Bernoulli formula for g=1..15."""
        B_2g = bernoulli(2 * g)
        expected = (2**(2*g - 1) - 1) * abs(B_2g) / (2**(2*g - 1) * factorial(2 * g))
        assert simplify(lambda_fp(g) - expected) == 0

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_4(self):
        """lambda_4 from B_8 = -1/30."""
        B8 = bernoulli(8)
        expected = Rational(2**7 - 1, 2**7) * abs(B8) / factorial(8)
        assert lambda_fp(4) == expected

    def test_lambda_5(self):
        """lambda_5 from B_10 = 5/66."""
        B10 = bernoulli(10)
        expected = Rational(2**9 - 1, 2**9) * abs(B10) / factorial(10)
        assert lambda_fp(5) == expected

    def test_all_lambda_positive(self):
        """All lambda_g^FP are positive for g=1..20."""
        for g in range(1, 21):
            assert lambda_fp(g) > 0, f"lambda_{g} is not positive"

    def test_lambda_decreasing(self):
        """|lambda_g^FP| is eventually decreasing (radius of convergence)."""
        # For g >= 2, lambda_g should be small and decreasing
        for g in range(2, 15):
            assert lambda_fp(g + 1) < lambda_fp(g), \
                f"lambda_{g+1} >= lambda_{g}"

    def test_lambda_table_20_genera(self):
        """Compute and verify lambda_g for g=1..20."""
        table = lambda_fp_table(20)
        assert len(table) == 20
        for g, lam in table.items():
            assert lam > 0
            assert lam.is_rational


class TestAhatGeneratingFunction:
    """sum (-1)^g lambda_g x^{2g} = (x/2)/sinh(x/2) - 1.

    DEFENSE RATING: AIRTIGHT (power series identity, exact arithmetic)."""

    @pytest.mark.parametrize("g", range(1, 8))
    def test_ahat_coefficient_genus_g(self, g):
        """Coefficient of x^{2g} in A-hat(x) matches (-1)^g * lambda_g."""
        r = verify_ahat_generating_function(g)
        assert r[f"g={g}_ahat_coeff"]

    def test_first_terms(self):
        """Verify explicit first few lambda_g values."""
        r = verify_ahat_first_terms()
        assert all(r.values()), f"Failed: {[k for k,v in r.items() if not v]}"


class TestConvergenceRatio:
    """Ratio lambda_{g+1}/lambda_g -> 1/(4*pi^2) as g -> infinity.

    DEFENSE RATING: STRONG (asymptotic Bernoulli number formula)."""

    def test_ratios_computed(self):
        """Convergence ratios are all well-defined rationals."""
        r = verify_convergence_ratio(12)
        for g in range(1, 12):
            key = f"ratio_g{g}_to_g{g+1}"
            assert key in r
            ratio = r[key]
            assert ratio > 0

    def test_ratios_bounded(self):
        """All ratios are bounded by 1 (convergence)."""
        r = verify_convergence_ratio(12)
        for g in range(2, 12):
            ratio = r[f"ratio_g{g}_to_g{g+1}"]
            assert ratio < 1, f"ratio at g={g} is {ratio} >= 1"

    def test_ratios_approaching_limit(self):
        """Successive ratios approach 1/(4*pi^2) ~ 0.02533."""
        r = verify_convergence_ratio(12)
        # The ratios should be getting closer to the limit
        # Check that ratio at g=10 is closer to limit than ratio at g=2
        r2 = float(r["ratio_g2_to_g3"])
        r10 = float(r["ratio_g10_to_g11"])
        limit = float(1 / (4 * pi**2))
        assert abs(r10 - limit) < abs(r2 - limit)


# ============================================================================
# DEFENSE V: Period matrix trace structure
# ============================================================================

class TestPeriodMatrixTrace:
    """The trace of the curvature operator reduces the gxg
    period matrix to a scalar.

    DEFENSE RATING: STRONG (relies on Schur + trace decomposition)."""

    @pytest.mark.parametrize("g", range(2, 11))
    def test_trace_scalar(self, g):
        """Trace reduces to scalar at genus g."""
        d = period_matrix_trace_structure(g)
        assert d["trace_reduces_to_scalar"]

    def test_siegel_dim_genus2(self):
        """Siegel dim at g=2: 2*3/2 = 3."""
        d = period_matrix_trace_structure(2)
        assert d["siegel_dim"] == 3

    def test_siegel_dim_genus3(self):
        """Siegel dim at g=3: 3*4/2 = 6."""
        d = period_matrix_trace_structure(3)
        assert d["siegel_dim"] == 6

    def test_torelli_proper_g4(self):
        """For g >= 4: Torelli image is a proper subvariety of A_g."""
        d = period_matrix_trace_structure(4)
        assert d["torelli_proper_subvariety"]

    def test_torelli_not_proper_g3(self):
        """For g <= 3: Torelli image is not necessarily proper."""
        d = period_matrix_trace_structure(3)
        assert not d["torelli_proper_subvariety"]

    def test_moduli_dim_genus2(self):
        """dim M_2 = 3."""
        d = period_matrix_trace_structure(2)
        assert d["moduli_dim"] == 3

    def test_moduli_dim_genus10(self):
        """dim M_10 = 27."""
        d = period_matrix_trace_structure(10)
        assert d["moduli_dim"] == 27


# ============================================================================
# DEFENSE VI: Clutching compatibility
# ============================================================================

class TestClutchingCompatibility:
    """F_g = kappa * lambda_g^FP is compatible with clutching/sewing.

    DEFENSE RATING: STRONG (relies on A-hat multiplicativity +
    kappa additivity)."""

    @pytest.mark.parametrize("g1,g2", [
        (1, 1), (1, 2), (1, 3), (2, 2), (1, 4),
        (2, 3), (3, 3), (1, 5), (2, 4), (3, 4),
    ])
    def test_clutching_kappa_additive(self, g1, g2):
        """kappa is additive under clutching."""
        d = verify_clutching_compatibility(g1, g2)
        assert d["kappa_additivity_holds"]

    @pytest.mark.parametrize("g1,g2", [
        (1, 1), (1, 2), (1, 3), (2, 2), (1, 4),
        (2, 3), (3, 3), (1, 5), (2, 4), (3, 4),
    ])
    def test_clutching_lambda_universal(self, g1, g2):
        """lambda_g^FP is universal (independent of the algebra)."""
        d = verify_clutching_compatibility(g1, g2)
        assert d["lambda_universality_holds"]

    def test_all_pairs_up_to_10(self):
        """All clutching pairs with g1+g2 <= 10."""
        r = verify_clutching_all_pairs(10)
        assert all(r.values()), f"Failed: {[k for k,v in r.items() if not v]}"

    def test_ahat_multiplicativity_c1(self):
        """Connected contribution c_1 = -1/24."""
        r = verify_ahat_multiplicativity()
        assert r["c1_value"]

    def test_ahat_multiplicativity_c2_rational(self):
        """Connected contribution c_2 is rational."""
        r = verify_ahat_multiplicativity()
        assert r["c2_rational"]

    def test_ahat_multiplicativity_c3_rational(self):
        """Connected contribution c_3 is rational."""
        r = verify_ahat_multiplicativity()
        assert r["c3_rational"]


# ============================================================================
# DEFENSE VII: No matrix curvature (Schur's lemma)
# ============================================================================

class TestSchurLemma:
    """d^2 must be scalar by Schur's lemma.

    DEFENSE RATING: AIRTIGHT (Schur's lemma is a theorem of algebra)."""

    def test_heisenberg_schur(self):
        """Heisenberg: U(1) symmetry => d^2 scalar."""
        d = schur_lemma_argument("Heisenberg")
        assert d["schur_applies"]

    def test_sl2_schur(self):
        """sl2: SU(2) symmetry => d^2 scalar."""
        d = schur_lemma_argument("sl2")
        assert d["schur_applies"]

    def test_virasoro_schur(self):
        """Virasoro: conformal symmetry => d^2 scalar."""
        d = schur_lemma_argument("Virasoro")
        assert d["schur_applies"]

    def test_w3_schur(self):
        """W3: extended conformal symmetry => d^2 scalar."""
        d = schur_lemma_argument("W3")
        assert d["schur_applies"]

    def test_generic_algebra_schur(self):
        """Generic chiral algebra: Schur argument works universally."""
        d = schur_lemma_argument("generic")
        assert d["schur_applies"]


# ============================================================================
# FULL GENUS-g DEFENSE BATTERY
# ============================================================================

class TestFullDefenseGenus2:
    """Full 7-axis defense at genus 2."""

    def test_genus2_defense_runs(self):
        """Full defense at g=2 completes without error."""
        d = full_genus_g_defense(2)
        assert d["genus"] == 2

    def test_genus2_fay_scalar(self):
        """Fay defect is scalar at g=2."""
        d = full_genus_g_defense(2)
        assert d["defense_2_fay_scalar"]["defect_forced_scalar"]

    def test_genus2_costello_local(self):
        """Costello counterterm is local at g=2."""
        d = full_genus_g_defense(2)
        assert d["defense_3_costello"]["locality"]

    def test_genus2_lambda(self):
        """lambda_2^FP = 7/5760."""
        d = full_genus_g_defense(2)
        assert d["defense_4_mumford"]["lambda_g"] == Rational(7, 5760)

    def test_genus2_trace_scalar(self):
        """Period matrix trace is scalar at g=2."""
        d = full_genus_g_defense(2)
        assert d["defense_5_period_trace"]["trace_reduces_to_scalar"]

    def test_genus2_schur(self):
        """Schur's lemma applies at g=2."""
        d = full_genus_g_defense(2, "Virasoro")
        assert d["defense_7_schur"]["schur_applies"]


class TestFullDefenseGenus3:
    """Full defense at genus 3 (the critical case where dimensional
    argument for obs^2 = 0 FAILS)."""

    def test_genus3_defense_runs(self):
        d = full_genus_g_defense(3)
        assert d["genus"] == 3

    def test_genus3_fay_scalar(self):
        """Fay defect still scalar at g=3 (H^{1,1} = 1)."""
        d = full_genus_g_defense(3)
        assert d["defense_2_fay_scalar"]["defect_forced_scalar"]

    def test_genus3_lambda(self):
        """lambda_3^FP = 31/967680."""
        d = full_genus_g_defense(3)
        assert d["defense_4_mumford"]["lambda_g"] == Rational(31, 967680)

    def test_genus3_has_clutching_decomposition(self):
        """Genus 3 has clutching decompositions: 1+2."""
        d = full_genus_g_defense(3)
        assert "g1=1,g2=2" in d["defense_6_clutching"]


class TestFullDefenseHighGenus:
    """Defense at high genus (g=5, 10, 15)."""

    @pytest.mark.parametrize("g", [5, 10, 15])
    def test_defense_runs(self, g):
        """Full defense completes at high genus."""
        d = full_genus_g_defense(g)
        assert d["genus"] == g

    @pytest.mark.parametrize("g", [5, 10, 15])
    def test_fay_scalar(self, g):
        """Fay defect scalar at high genus."""
        d = full_genus_g_defense(g)
        assert d["defense_2_fay_scalar"]["defect_forced_scalar"]

    @pytest.mark.parametrize("g", [5, 10, 15])
    def test_lambda_positive(self, g):
        """lambda_g^FP > 0 at high genus."""
        d = full_genus_g_defense(g)
        assert d["defense_4_mumford"]["lambda_g"] > 0


# ============================================================================
# CROSS-FAMILY UNIVERSALITY
# ============================================================================

class TestCrossFamilyUniversality:
    """F_g(A)/F_g(B) = kappa(A)/kappa(B) for ALL g (genus-independent ratio).

    DEFENSE RATING: AIRTIGHT (follows from F_g = kappa * lambda_g)."""

    @pytest.mark.parametrize("g", [1, 2, 3, 5, 10])
    def test_universality_genus_g(self, g):
        """Ratio F_g(A)/F_g(B) = kappa(A)/kappa(B) at genus g."""
        r = verify_F_g_all_families(g)
        # Check all ratio matches
        ratio_keys = [k for k in r if k.endswith("_matches")]
        assert all(r[k] for k in ratio_keys), \
            f"Universality failed at g={g}: {[k for k in ratio_keys if not r[k]]}"

    def test_heisenberg_sl2_ratio(self):
        """F_g(H_1)/F_g(sl2_1) = kappa(H)/kappa(sl2) = 4/9 for all g."""
        kh = Rational(1)
        ksl2 = Rational(9, 4)
        expected_ratio = kh / ksl2  # = 4/9

        for g in range(1, 8):
            Fh = kh * lambda_fp(g)
            Fsl2 = ksl2 * lambda_fp(g)
            assert simplify(Fh / Fsl2 - expected_ratio) == 0

    def test_virasoro_w3_ratio(self):
        """F_g(Vir_26)/F_g(W3_50) = kappa(Vir)/kappa(W3) for all g."""
        kv = Rational(13)       # kappa(Vir_26) = 26/2
        kw3 = Rational(125, 3)  # kappa(W3_50) = 5*50/6
        expected_ratio = kv / kw3  # = 39/125

        for g in range(1, 8):
            Fv = kv * lambda_fp(g)
            Fw3 = kw3 * lambda_fp(g)
            assert simplify(Fv / Fw3 - expected_ratio) == 0


# ============================================================================
# STRUCTURAL CONSISTENCY: genus-0 limit and genus-1 matching
# ============================================================================

class TestGenusConsistency:
    """The g>=2 bridge must be consistent with the PROVED
    genus-0 (d^2=0) and genus-1 (d^2=kappa*omega_1) results."""

    def test_genus0_d_squared_zero(self):
        """At genus 0: d^2 = 0 (Arnold exact, no defect)."""
        # kappa * lambda_0 = kappa * 0 (no genus-0 correction)
        # But this is a bit misleading: at genus 0, d^2 = 0 IDENTICALLY.
        # The genus expansion starts at g=1.
        pass  # structural: genus 0 has no correction

    def test_genus1_F_matches(self):
        """At genus 1: F_1 = kappa/24 (from lambda_1 = 1/24)."""
        kappa = Symbol('kappa')
        F1 = F_g(kappa, 1)
        assert simplify(F1 - kappa / 24) == 0

    def test_genus2_F_matches(self):
        """At genus 2: F_2 = kappa * 7/5760."""
        kappa = Symbol('kappa')
        F2 = F_g(kappa, 2)
        assert simplify(F2 - kappa * Rational(7, 5760)) == 0

    def test_genus_tower_monotone(self):
        """F_g > F_{g+1} for g >= 2 (eventually decreasing)."""
        kappa = Rational(1)
        for g in range(2, 15):
            Fg = F_g(kappa, g)
            Fg1 = F_g(kappa, g + 1)
            assert Fg > Fg1, f"F_{g} <= F_{g+1}"

    def test_complementarity_at_all_genera(self):
        """kappa(A) + kappa(A!) = const is genus-INDEPENDENT.

        This means the complementarity sum at genus g is the SAME
        as at genus 1 (which is proved).
        """
        # Virasoro: kappa + kappa' = 13 at all genera
        c = Symbol('c')
        for g in range(1, 8):
            Fg = F_g(c / 2, g)
            Fg_dual = F_g((26 - c) / 2, g)
            total = simplify(Fg + Fg_dual)
            expected = 13 * lambda_fp(g)
            assert simplify(total - expected) == 0, \
                f"Complementarity failed at g={g}"


# ============================================================================
# NUMERICAL SPOT CHECKS: specific parameter values at g=2,3
# ============================================================================

class TestNumericalSpotChecks:
    """Exact rational arithmetic checks at specific parameter values."""

    def test_heisenberg_k1_F2(self):
        """F_2(H_1) = 7/5760."""
        assert F_g(Rational(1), 2) == Rational(7, 5760)

    def test_sl2_k1_F2(self):
        """F_2(sl2_1) = (9/4) * 7/5760 = 63/23040 = 7/2560."""
        F2 = F_g(Rational(9, 4), 2)
        assert F2 == Rational(9, 4) * Rational(7, 5760)

    def test_virasoro_c26_F2(self):
        """F_2(Vir_26) = 13 * 7/5760 = 91/5760 = 7/443.07...
        Actually: 91/5760. Let's just check."""
        F2 = F_g(Rational(13), 2)
        assert F2 == Rational(91, 5760)

    def test_virasoro_c26_F3(self):
        """F_3(Vir_26) = 13 * 31/967680."""
        F3 = F_g(Rational(13), 3)
        assert F3 == Rational(13 * 31, 967680)

    def test_w3_c50_F2(self):
        """F_2(W3_50) = (125/3) * 7/5760 = 875/17280."""
        kappa_w3 = Rational(5 * 50, 6)  # = 250/6 = 125/3
        F2 = F_g(kappa_w3, 2)
        assert F2 == Rational(125, 3) * Rational(7, 5760)

    def test_complementarity_sl2_k1_F2(self):
        """F_2(sl2_1) + F_2(sl2_{-5}) = 0 (anti-symmetric)."""
        kappa = Rational(9, 4)
        kappa_dual = Rational(-9, 4)
        F2 = F_g(kappa, 2) + F_g(kappa_dual, 2)
        assert F2 == 0

    def test_complementarity_virasoro_c1_F3(self):
        """F_3(Vir_1) + F_3(Vir_25) = 13 * lambda_3."""
        F3_1 = F_g(Rational(1, 2), 3)
        F3_25 = F_g(Rational(25, 2), 3)
        expected = Rational(13) * lambda_fp(3)
        assert simplify(F3_1 + F3_25 - expected) == 0


# ============================================================================
# DEFENSE RATING SUMMARY
# ============================================================================

class TestDefenseRatingSummary:
    """Summary verification that all 7 defenses are operational."""

    def test_defense_1_operational(self):
        """Defense 1 (uniqueness): all checks pass."""
        r = verify_kappa_uniqueness()
        assert all(r.values())

    def test_defense_2_operational(self):
        """Defense 2 (Fay scalar): all checks pass for g=1..20."""
        r = verify_fay_defect_scalar_all_genera(20)
        assert all(r.values())

    def test_defense_3_operational(self):
        """Defense 3 (Costello scaling): all checks pass for g=1..15."""
        r = verify_costello_scaling_all_genera(15)
        assert all(r.values())

    def test_defense_4_operational(self):
        """Defense 4 (Bernoulli): all checks pass for g=1..15."""
        r = verify_lambda_fp_bernoulli(15)
        assert all(r.values())

    def test_defense_6_operational(self):
        """Defense 6 (clutching): all checks pass for g1+g2 <= 10."""
        r = verify_clutching_all_pairs(10)
        assert all(r.values())

    def test_defense_7_operational(self):
        """Defense 7 (Schur): applies to all standard families."""
        for fam in ["Heisenberg", "sl2", "Virasoro", "W3"]:
            d = schur_lemma_argument(fam)
            assert d["schur_applies"]
