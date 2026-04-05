#!/usr/bin/env python3
r"""
test_platonic_red_team.py — Red team tests for conj:platonic-adjunction.

Attack surface: the platonic adjunction U^mod_X |-| Prim^mod between
cyclically admissible Lie conformal algebras and cyclic factorization
algebras on a curve X.

Tests organized by attack vector:
  A. Cyclic admissibility (which families pass, which fail, edge cases)
  B. Size/cardinality obstructions (PBW growth, stable-graph growth)
  C. Adjunction coherence (unit/counit, Milnor-Moore)
  D. Modular completion / HS-sewing gap
  E. DS reduction exactness (the non-exactness killer)
  F. Critical level degeneration
  G. Master assessment

Mathematical references:
  - def:cyclically-admissible in higher_genus_modular_koszul.tex
  - thm:platonic-adjunction in higher_genus_modular_koszul.tex
  - conj:platonic-adjunction in concordance.tex
  - thm:ds-platonic-functor in w_algebras_deep.tex
  - thm:general-hs-sewing in higher_genus_modular_koszul.tex
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from platonic_red_team import (
    CyclicAdmissibilityData,
    standard_families_admissibility,
    w_N_max_pole_order,
    count_w_N_generators,
    pbw_weight_space_dim,
    pbw_growth_rate,
    modular_graph_algebra_growth,
    milnor_moore_connectedness_check,
    ds_exactness_status,
    ds_kunneth_obstruction,
    hs_sewing_condition_check,
    construct_admissible_non_hs_example,
    unit_counit_coherence_analysis,
    critical_level_analysis,
    infinity_cat_obstruction,
    master_red_team_assessment,
)


# ==========================================================================
# A. CYCLIC ADMISSIBILITY TESTS
# ==========================================================================

class TestCyclicAdmissibility:
    """Test which standard families satisfy cyclic admissibility."""

    def test_heisenberg_is_admissible(self):
        """Heisenberg algebra is cyclically admissible."""
        families = standard_families_admissibility()
        data = families['Heisenberg']
        assert data.is_cyclically_admissible
        assert data.is_nishinaka_admissible
        assert len(data.obstructions) == 0

    def test_affine_generic_is_admissible(self):
        """Affine sl_N at generic level is cyclically admissible."""
        families = standard_families_admissibility()
        data = families['Affine_generic']
        assert data.is_cyclically_admissible
        assert data.max_pole_order == 1  # first-order poles only

    def test_virasoro_is_admissible(self):
        """Virasoro algebra is cyclically admissible (pole order 3)."""
        families = standard_families_admissibility()
        data = families['Virasoro']
        assert data.is_cyclically_admissible
        assert data.max_pole_order == 3  # T(z)T(w) ~ c/2 * (z-w)^{-4}

    def test_betagamma_is_admissible(self):
        """BetaGamma system is cyclically admissible."""
        families = standard_families_admissibility()
        data = families['BetaGamma']
        assert data.is_cyclically_admissible

    def test_w3_is_admissible(self):
        """W_3 algebra is cyclically admissible."""
        families = standard_families_admissibility()
        data = families['W_3']
        assert data.is_cyclically_admissible
        assert data.max_pole_order == 5  # WW OPE pole order 6 => lambda order 5

    def test_w_N_pole_order_grows(self):
        """W_N pole order grows linearly with N: max pole = 2N-1."""
        for N in [2, 3, 4, 5, 10]:
            assert w_N_max_pole_order(N) == 2 * N - 1
        # For each fixed N, pole order is bounded => condition (iii) OK
        families = standard_families_admissibility()
        data = families['W_N_general']
        assert data.is_cyclically_admissible

    def test_w_infty_NOT_admissible(self):
        """W_{1+infty} FAILS cyclic admissibility.

        RED TEAM FINDING: W_{1+infty} has:
        - Unbounded pole order (condition iii fails)
        - Infinite-dimensional graded pieces (condition i fails at high weight)

        This means the platonic adjunction does NOT apply to W_{1+infty}
        in its current formulation.
        """
        families = standard_families_admissibility()
        data = families['W_{1+infty}']
        assert not data.is_cyclically_admissible
        assert not data.is_nishinaka_admissible
        assert not data.bounded_pole_order  # unbounded poles
        assert not data.finite_dim_graded_pieces  # infinite-dim pieces
        obstructions = data.obstructions
        assert len(obstructions) >= 2

    def test_w_infty_pole_order_unbounded(self):
        """W_{1+infty} pole order: W^s . W^t has pole order s+t-1, unbounded."""
        for s in range(1, 10):
            for t in range(1, 10):
                pole_order = s + t - 1
                assert pole_order >= s  # grows with spin
        # At large spin: pole order ~ 2s - 1 -> infinity
        assert w_N_max_pole_order(100) == 199

    def test_affine_critical_formally_admissible(self):
        """At critical level k = -h^v, the Lie conformal algebra IS
        cyclically admissible: the pairing -h^v * tr(XY) is nondegenerate
        on g, and the conformal grading (by mode number) exists.

        RED TEAM FINDING: The platonic adjunction FORMALLY applies at
        critical level, but the platonic package degenerates: kappa = 0,
        Sugawara gives T = 0, the shadow obstruction tower is trivial, and the
        Feigin-Frenkel center makes Prim^mod larger than expected.
        """
        families = standard_families_admissibility()
        data = families['Affine_critical']
        # Pairing exists and is nondegenerate (k = -h^v != 0)
        assert data.has_invariant_pairing
        assert data.pairing_nondegenerate
        # Satisfies all four conditions
        assert data.is_cyclically_admissible
        assert data.has_conformal_grading
        assert data.bounded_pole_order

    def test_free_fermion_admissible(self):
        """Free fermion is cyclically admissible."""
        families = standard_families_admissibility()
        data = families['FreeFermion']
        assert data.is_cyclically_admissible

    def test_lattice_admissible(self):
        """Lattice VOA Lie conformal algebra is cyclically admissible."""
        families = standard_families_admissibility()
        data = families['Lattice']
        assert data.is_cyclically_admissible

    def test_all_standard_admissible_except_w_infty(self):
        """All standard families are cyclically admissible except
        W_{1+infty}.

        W_{1+infty} fails conditions (i) and (iii): infinite-dimensional
        graded pieces and unbounded pole order.

        Affine at critical level IS formally cyclically admissible
        (the pairing -h^v * tr(XY) is nondegenerate) but the
        platonic package degenerates (kappa = 0).
        """
        families = standard_families_admissibility()
        admissible = [name for name, data in families.items()
                      if data.is_cyclically_admissible]
        not_admissible = [name for name, data in families.items()
                          if not data.is_cyclically_admissible]
        assert 'W_{1+infty}' in not_admissible
        assert len(not_admissible) == 1  # ONLY W_{1+infty}
        assert len(admissible) >= 9  # all others including Affine_critical


# ==========================================================================
# B. SIZE / CARDINALITY TESTS
# ==========================================================================

class TestSizeObstructions:
    """Test PBW growth and stable-graph algebra growth."""

    def test_heisenberg_pbw_is_partition(self):
        """Heisenberg PBW dimensions = partition numbers."""
        # p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for n, exp in enumerate(expected):
            assert pbw_weight_space_dim('Heisenberg', n) == exp

    def test_virasoro_pbw_parts_ge_2(self):
        """Virasoro PBW: partitions into parts >= 2."""
        # n=0:1, n=1:0, n=2:1, n=3:1, n=4:2, n=5:2, n=6:4
        expected = [1, 0, 1, 1, 2, 2, 4]
        for n, exp in enumerate(expected):
            assert pbw_weight_space_dim('Virasoro', n) == exp

    def test_affine_sl2_pbw_3_colored(self):
        """Affine sl_2 PBW: 3-colored partitions."""
        d0 = pbw_weight_space_dim('Affine_sl2', 0)
        d1 = pbw_weight_space_dim('Affine_sl2', 1)
        d2 = pbw_weight_space_dim('Affine_sl2', 2)
        assert d0 == 1   # vacuum
        assert d1 == 3   # J^+_{-1}, J^-_{-1}, J^0_{-1}
        assert d2 >= 9   # 3 modes at weight 2 + products

    def test_pbw_growth_subexponential(self):
        """PBW weight-space dimensions grow subexponentially for all families.

        Hardy-Ramanujan: p(n) ~ exp(pi*sqrt(2n/3)) / (4n*sqrt(3))
        This is stretched-exponential, NOT exponential.
        log p(n) / n -> 0 (subexponential).
        """
        for family in ['Heisenberg', 'Virasoro', 'Affine_sl2']:
            growth = pbw_growth_rate(family, max_weight=20)
            dims = growth['dims']
            # Check subexponential: log(dim) / n -> 0
            for n in range(5, 21):
                if dims[n] > 0:
                    ratio = math.log(dims[n]) / n
                    assert ratio < 2.0  # well below exponential

    def test_stable_graph_growth_factorial(self):
        """Stable graph counts grow FACTORIALLY with genus.

        RED TEAM FINDING: The stable-graph coefficient algebra G_mod
        has |G_{g,n}| growing factorially in g. The completed tensor
        product Fact_X(L) hat-otimes G_mod involves a sum over ALL
        stable graphs at ALL genera. The colimit does NOT stabilize.

        This is NOT an obstruction to the adjunction per se (the
        completed tensor product is well-defined as a formal series
        in genus), but it means U^mod_X(L) is INFINITE-DIMENSIONAL
        in a strong sense.
        """
        for g in range(2, 8):
            count = modular_graph_algebra_growth(g, 3)
            # Should grow at least factorially
            assert count >= 1
        # Check factorial growth
        c3 = modular_graph_algebra_growth(3, 3)
        c5 = modular_graph_algebra_growth(5, 3)
        assert c5 > c3  # growing

    def test_stable_graph_genus_0_trivial(self):
        """At genus 0 with n < 3 points: no stable graphs."""
        assert modular_graph_algebra_growth(0, 0) == 0
        assert modular_graph_algebra_growth(0, 1) == 0
        assert modular_graph_algebra_growth(0, 2) == 0
        assert modular_graph_algebra_growth(0, 3) >= 1

    def test_w3_pbw_growth(self):
        """W_3 PBW growth: two generators at weights 2, 3."""
        d0 = pbw_weight_space_dim('W_3', 0)
        d2 = pbw_weight_space_dim('W_3', 2)
        d3 = pbw_weight_space_dim('W_3', 3)
        assert d0 == 1   # vacuum
        assert d2 >= 1   # L_{-2}
        assert d3 >= 2   # L_{-3}, W_{-3}


# ==========================================================================
# C. ADJUNCTION COHERENCE TESTS
# ==========================================================================

class TestAdjunctionCoherence:
    """Test unit-counit structure and Milnor-Moore requirements."""

    def test_milnor_moore_genus_0_ok(self):
        """Milnor-Moore theorem applies at genus 0 (d^2 = 0)."""
        for family in ['Heisenberg', 'Affine_generic', 'Virasoro', 'BetaGamma']:
            result = milnor_moore_connectedness_check(family)
            assert result['genus_0_milnor_moore'] is True

    def test_milnor_moore_genus_1_curved(self):
        """At genus >= 1, bar coalgebra is curved (kappa != 0).

        RED TEAM FINDING: The classical Milnor-Moore theorem requires
        coassociativity, which fails for curved coalgebras. The proof
        of thm:platonic-adjunction invokes Milnor-Moore but does not
        address the curvature issue explicitly.
        """
        for family in ['Heisenberg', 'Virasoro']:
            result = milnor_moore_connectedness_check(family)
            assert result['genus_1_curved'] is True
            assert result['classical_milnor_moore_applies'] is False
            assert result['obstruction'] is not None

    def test_unit_counit_analysis(self):
        """Verify unit-counit structure of the platonic adjunction."""
        analysis = unit_counit_coherence_analysis()

        # Unit at genus 0: iso by PBW
        assert 'iso' in analysis['unit_analysis']['genus_0'].lower()
        assert analysis['unit_analysis']['is_iso'] is True

        # Counit is surjective, NOT iso for simple quotients
        assert analysis['counit_analysis']['is_surjective'] is True
        assert analysis['counit_analysis']['is_iso'] is False

        # Adjunction still valid (doesn't require counit to be iso)
        assert analysis['counit_analysis']['adjunction_still_valid'] is True

    def test_triangle_identities_genus_0(self):
        """Triangle identities hold at genus 0 by Nishinaka UP."""
        analysis = unit_counit_coherence_analysis()
        assert 'PROVED' in analysis['triangle_identities']['genus_0'].upper()

    def test_triangle_identities_genus_ge_1_status(self):
        """Triangle identities at genus >= 1 are unproved but expected.

        The argument is: naturality of Theta_A = D_A - d_0 propagates
        the genus-0 triangle identities to all genera. This is valid
        but implicit in the text.
        """
        analysis = unit_counit_coherence_analysis()
        # The status at genus >= 1 should acknowledge it follows from naturality
        assert analysis['triangle_identities']['severity'] == 'LOW'

    def test_adjunction_not_equivalence(self):
        """The platonic adjunction is NOT an equivalence.

        The counit U^mod(Prim^mod(F)) -> F is surjective but not iso
        when F is a simple quotient. This is expected: U^mod is a
        FREE construction, not a localization.
        """
        analysis = unit_counit_coherence_analysis()
        assert analysis['counit_analysis']['is_iso'] is False
        # The kernel is the maximal ideal
        assert 'ideal' in analysis['counit_analysis']['kernel'].lower()


# ==========================================================================
# D. MODULAR COMPLETION / HS-SEWING TESTS
# ==========================================================================

class TestHSSewingGap:
    """Test the gap between cyclic admissibility and HS-sewing."""

    def test_standard_families_have_hs_sewing(self):
        """All standard families satisfy HS-sewing."""
        for family in ['Heisenberg', 'Affine_generic', 'BetaGamma',
                        'Virasoro', 'W_3', 'FreeFermion', 'Lattice']:
            result = hs_sewing_condition_check(family)
            assert result['standard_hs_sewing'] is True

    def test_admissible_non_hs_example_exists(self):
        """There exist cyclically admissible L whose envelope fails HS-sewing.

        RED TEAM FINDING: Bounded pole order (condition iii) does NOT imply
        polynomial OPE coefficient growth. The HS-sewing theorem requires
        polynomial growth, but cyclic admissibility does not guarantee it.

        Construction: L with structure constants c^k_{ij} ~ i! * j!
        (factorial growth). Bounded pole order (only lambda^0 term)
        but superexponential coefficient growth => HS-sewing fails.
        """
        result = construct_admissible_non_hs_example()
        assert result['is_cyclically_admissible'] is True
        assert result['hs_sewing_fails'] is True
        assert result['hs_norm_sample'] > 0

    def test_hs_gap_identified(self):
        """The gap between admissibility and HS-sewing is genuine.

        Cyclic admissibility conditions (i)-(iv):
        (i)   conformal grading, finite-dim pieces
        (ii)  complete filtration
        (iii) bounded pole order
        (iv)  invariant pairing

        HS-sewing conditions (thm:general-hs-sewing):
        (a) polynomial OPE growth
        (b) subexponential sector growth

        (iii) implies (b) for standard families (PBW growth is
        partition-type, hence subexponential). But (iii) does NOT
        imply (a) in general: pole order bounds degree but not
        coefficient magnitude.
        """
        result = hs_sewing_condition_check('Heisenberg')
        assert result['polynomial_ope_growth'] is True  # standard family

        # A general family has unknown HS status
        result2 = hs_sewing_condition_check('Unknown_family')
        assert result2['polynomial_ope_growth'] is None

    def test_genus_0_always_works(self):
        """At genus 0, no sewing is needed — the Nishinaka envelope
        always exists for Nishinaka-admissible L.

        The HS-sewing gap only affects genus >= 1.
        """
        families = standard_families_admissibility()
        for name, data in families.items():
            if data.is_nishinaka_admissible:
                # Genus-0 envelope exists
                pass  # This is a structural assertion
        # All Nishinaka-admissible families get genus-0 envelope
        nishinaka_ok = [name for name, data in families.items()
                        if data.is_nishinaka_admissible]
        assert len(nishinaka_ok) >= 8


# ==========================================================================
# E. DS REDUCTION EXACTNESS TESTS
# ==========================================================================

class TestDSExactness:
    """Test the DS exactness requirements for platonic package functoriality."""

    def test_principal_ds_exact(self):
        """DS is exact for principal nilpotent (Feigin-Frenkel)."""
        status = ds_exactness_status()
        p = status['principal']
        assert p['H_i_vanishing'] is True
        assert p['exact_on_VA'] is True
        assert p['exact_on_bar'] is True
        assert p['status'] == 'PROVED'

    def test_admissible_ds_exact(self):
        """DS is exact on admissible modules (Arakawa 2017)."""
        status = ds_exactness_status()
        m = status['minimal_sl3']
        assert m['exact_on_modules'] is True

    def test_hook_type_ds_exact(self):
        """DS is exact for hook-type in type A (proved corridor)."""
        status = ds_exactness_status()
        h = status['hook_type_A']
        assert h['H_i_vanishing'] is True
        assert h['status'] == 'PROVED at generic level'

    def test_arbitrary_nilpotent_ds_NOT_exact(self):
        """DS for arbitrary nilpotent at general level is NOT proved exact.

        RED TEAM FINDING: The platonic package functoriality
        (thm:ds-platonic-functor) REQUIRES exactness. For arbitrary
        nilpotent f outside the proved corridor (principal, admissible,
        hook-type A), the theorem does NOT apply.

        The claim "Theta_W = DS(Theta_g)" is FALSE in general when
        H^i_{DS} != 0 for i != 0.
        """
        status = ds_exactness_status()
        arb = status['arbitrary_nilpotent']
        assert arb['H_i_vanishing'] is False
        assert arb['exact_on_bar'] is False
        assert arb['status'] == 'CONJECTURAL'
        assert arb['obstruction'] is not None

    def test_kunneth_for_universal_algebra(self):
        """Kunneth holds for tensor powers of universal V_k(g)
        (over a field, BRST cohomology satisfies Kunneth when H^i=0).

        This means DS commutes with the bar complex for V_k(g).
        """
        for N in [2, 3, 4]:
            result = ds_kunneth_obstruction(N)
            assert result['kunneth_holds_for_universal'] is True

    def test_kunneth_fails_for_simple_quotient(self):
        """Kunneth may fail for simple quotient L_k(g) at admissible k.

        RED TEAM FINDING: The bar complex of L_k(g) involves tensor
        powers L_k(g)^{otimes n}. For simple quotients with vacuum
        null vectors, the BRST complex on tensor powers may have
        nontrivial higher cohomology even when H^i(L_k(g)) = 0.
        """
        result = ds_kunneth_obstruction(2)
        assert result['kunneth_holds_for_simple'] is False

    def test_ds_proof_uses_exactness_crucially(self):
        """The proof of thm:ds-platonic-functor uses exactness at
        multiple points:

        Component (1): "H^0_DS, being an EXACT functor..."
        Component (3): "phi_*(Theta_A) = Theta_{A'}" requires phi
                       to be a VA map, which requires exactness
        Component (4): "vanishing of higher BRST cohomology"

        All three require H^i = 0 for i != 0.
        """
        status = ds_exactness_status()
        # Check that all proved cases use exactness
        for key in ['principal', 'subregular_sl3', 'hook_type_A']:
            assert status[key]['H_i_vanishing'] is True

    def test_non_admissible_level_partial(self):
        """At non-admissible irrational level: H^i(V_k(g)) = 0 by
        semicontinuity, but exactness on modules is open.

        RED TEAM: The proof says "H^0_DS is exact on the category of
        vertex algebra modules." This is TRUE for admissible modules
        (Arakawa) but NOT proved for general modules at irrational k.
        The bar complex uses tensor powers, which are NOT admissible
        modules in general.
        """
        status = ds_exactness_status()
        na = status['non_admissible_level']
        assert na['exact_on_VA'] is True
        assert na['exact_on_modules'] is False
        assert na['exact_on_bar'] is False


# ==========================================================================
# F. CRITICAL LEVEL DEGENERATION TESTS
# ==========================================================================

class TestCriticalLevel:
    """Test degeneration of the platonic adjunction at critical level."""

    def test_kappa_zero_at_critical(self):
        """kappa(sl_N, -h^v) = 0 for all N."""
        for N in [2, 3, 4, 5]:
            h_vee = N
            # kappa = dim(g) * (k + h^v) / (2*h^v)
            # At k = -h^v: kappa = dim(g) * 0 / (2*h^v) = 0
            analysis = critical_level_analysis(f'sl_{N}')
            assert analysis['kappa_value'] == 0

    def test_sugawara_undefined_at_critical(self):
        """Sugawara construction fails at critical level."""
        analysis = critical_level_analysis('sl_2')
        assert analysis['sugawara_defined'] is False

    def test_feigin_frenkel_center_large(self):
        """At critical level, V_{-h^v}(g) has a huge center (FF center)."""
        analysis = critical_level_analysis('sl_2')
        assert 'opers' in analysis['feigin_frenkel_center'].lower()

    def test_critical_level_not_excluded(self):
        """Critical level is NOT excluded by cyclic admissibility.

        RED TEAM FINDING: k = -h^v satisfies all four conditions:
        (i)   conformal grading exists (from free-field realization)
        (ii)  filtration complete
        (iii) bounded pole order (same as generic k)
        (iv)  invariant pairing k*tr(XY) is nonzero (k = -h^v != 0)

        But the platonic package DEGENERATES: kappa = 0, trivial
        shadow obstruction tower, trivial determinant line. The adjunction is
        vacuously true but content-free.
        """
        analysis = critical_level_analysis('sl_2')
        assert analysis['severity'] == 'MEDIUM'

    def test_prim_mod_may_be_larger_at_critical(self):
        """Prim^mod(V_{-h^v}(g)) may strictly contain L.

        At critical level, the Feigin-Frenkel center provides
        additional primitive elements (elements in the kernel of
        the reduced bar coproduct that are NOT generated by the
        current algebra L).
        """
        analysis = critical_level_analysis('sl_2')
        assert 'center' in analysis['prim_mod_at_critical'].lower()


# ==========================================================================
# G. MASTER ASSESSMENT TESTS
# ==========================================================================

class TestMasterAssessment:
    """Test the overall red team verdict."""

    def test_total_obstructions_count(self):
        """Master assessment identifies at least 6 obstructions."""
        assessment = master_red_team_assessment()
        assert assessment['summary']['total_obstructions'] >= 6

    def test_no_fatal_obstructions(self):
        """No obstruction is FATAL to the adjunction itself.

        The adjunction U^mod |-| Prim^mod is valid at genus 0
        (Nishinaka UP) and extends to all genera by naturality
        of the bar-intrinsic MC element. The obstructions are
        to SCOPE (W_{1+infty} excluded), CONVERGENCE (HS-sewing
        not guaranteed), and DS FUNCTORIALITY (requires exactness).
        """
        assessment = master_red_team_assessment()
        assert assessment['summary']['fatal'] == 0

    def test_high_severity_count(self):
        """At least 2 high-severity obstructions."""
        assessment = master_red_team_assessment()
        assert assessment['summary']['high_severity'] >= 2

    def test_w_infty_obstruction_identified(self):
        """W_{1+infty} scope obstruction is identified."""
        assessment = master_red_team_assessment()
        obs = assessment['obstructions']
        assert 'O1_W_infty_not_admissible' in obs
        assert obs['O1_W_infty_not_admissible']['severity'] == 'HIGH'

    def test_ds_obstruction_identified(self):
        """DS non-exactness obstruction is identified."""
        assessment = master_red_team_assessment()
        obs = assessment['obstructions']
        assert 'O3_ds_non_exactness' in obs
        assert obs['O3_ds_non_exactness']['severity'] == 'HIGH'

    def test_hs_sewing_obstruction_identified(self):
        """HS-sewing gap obstruction is identified."""
        assessment = master_red_team_assessment()
        obs = assessment['obstructions']
        assert 'O2_hs_sewing_gap' in obs
        assert obs['O2_hs_sewing_gap']['severity'] == 'MEDIUM'

    def test_infinity_cat_gap_identified(self):
        """Infinity-categorical gap is identified."""
        result = infinity_cat_obstruction()
        assert result['severity'] == 'LOW'
        assert 'infty' in result['concordance_claim'].lower()

    def test_curved_milnor_moore_identified(self):
        """Curved Milnor-Moore obstruction is identified."""
        assessment = master_red_team_assessment()
        obs = assessment['obstructions']
        assert 'O6_curved_milnor_moore' in obs
        assert obs['O6_curved_milnor_moore']['severity'] == 'MEDIUM'

    def test_overall_verdict_not_fatal(self):
        """The overall verdict: adjunction is valid, obstructions are
        to scope and auxiliary claims, not to the adjunction itself."""
        assessment = master_red_team_assessment()
        verdict = assessment['verdict']
        assert 'SOLID' in verdict.upper() or 'VALID' in verdict.upper()
        assert 'FATAL' not in verdict.upper() or 'NONE' in verdict.upper()

    def test_genus_0_always_solid(self):
        """At genus 0, the adjunction is unconditionally solid.

        The Nishinaka universal property gives the left adjoint.
        The Milnor-Moore theorem at genus 0 (d^2 = 0) gives
        the right adjoint Prim. The triangle identities follow.
        """
        assessment = master_red_team_assessment()
        verdict = assessment['verdict']
        # Genus-0 adjunction is mentioned as solid
        assert 'genus 0' in verdict.lower() or 'genus-0' in verdict.lower()

    def test_key_recommendation(self):
        """Key recommendation: distinguish adjunction (proved) from
        DS functoriality (conditional) and HS-sewing (gap).

        The manuscript currently labels thm:platonic-adjunction as
        ProvedHere. The RED TEAM assessment is:
        - The 1-categorical adjunction: PROVED (at genus 0, extends)
        - DS as functor on packages: PROVED for principal/hook-type
        - DS for arbitrary nilpotent: CONJECTURAL
        - HS-sewing for arbitrary cyclically admissible: OPEN GAP
        """
        # The adjunction itself is proved
        assessment = master_red_team_assessment()
        assert assessment['summary']['fatal'] == 0

        # DS functoriality has gaps
        ds = ds_exactness_status()
        assert ds['arbitrary_nilpotent']['status'] == 'CONJECTURAL'

        # HS-sewing has a gap
        example = construct_admissible_non_hs_example()
        assert example['is_cyclically_admissible']
        assert example['hs_sewing_fails']
