r"""Advanced Pixton ideal generation tests at genus 4.

Tests the GENERATION question for conj:pixton-from-shadows at genus 4:
does the shadow MC tower generate independent Pixton relations beyond
what lower-genus data provides?

KEY RESULTS TESTED:
  1. S_6 contributes 6 genuinely new monomials to delta_pf^{(4,0)}.
  2. These terms are structurally independent of genus-3 clutching
     pushforwards (which involve only S_3, S_4, S_5).
  3. Cross-family independence: G/L/C/M produce 3 independent Pixton
     elements at codimension 4, where S_6 is active.
  4. Shadow subspace dimension: cross-family rank >= 2 at codims 2-9,
     reaching 3 at codim 4.  Total shadow rank >= 17.
  5. Virasoro rank by codimension: each nonzero codim contributes
     rank 1 from the single-parameter family.

40 tests organized in 6 sections:
  Q. S_6-restricted polynomial (genuinely new terms)
  R. Clutching independence (structural argument)
  S. Shadow subspace dimension by codimension
  T. Cross-family rank analysis
  U. Virasoro per-codimension rank
  V. Generation strength (combined assessment)

Manuscript references:
    conj:pixton-from-shadows (concordance.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
    thm:mc-tautological-descent (higher_genus_modular_koszul.tex)
    thm:convolution-d-squared-zero (bar_cobar_adjunction_curved.tex)
"""

import pytest
from fractions import Fraction

from sympy import (
    Integer, Rational, Symbol, cancel, expand, simplify,
)

from compute.lib.theorem_pixton_generation_g4_engine import (
    # Existing imports
    FABER_GENUS4_DIMS,
    pf_by_codimension,
    shadow_isolation_by_codim,
    s6_codim_isolation,
    cross_family_independence_test,
    lower_genus_pf_content,
    genus4_pixton_ideal_dimension,
    # New sections
    s6_restricted_polynomial,
    clutching_independence_genus4,
    shadow_subspace_dimension,
    shadow_subspace_summary,
    virasoro_rank_by_codimension,
)
from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_shadow_data,
    c_sym,
)
from compute.lib.theorem_pixton_genus4_shadow_engine import (
    delta_pf_genus4,
    s6_isolation_test,
)
from compute.lib.theorem_shadow_arity_frontier_engine import (
    shadow_visibility_genus,
)


c = c_sym


# ============================================================================
# Section Q: S_6-restricted polynomial (genuinely new terms)
# ============================================================================

class TestS6RestrictedPolynomial:
    """Extract and verify the S_6/S_7-containing terms of delta_pf^{(4,0)}."""

    @pytest.fixture(scope="class")
    def s6r_data(self):
        return s6_restricted_polynomial()

    def test_p_new_is_nonzero(self, s6r_data):
        """The S_6/S_7-dependent part P_new is nonzero."""
        assert s6r_data['p_new_nonzero']

    def test_p_new_has_terms(self, s6r_data):
        """P_new has a positive number of monomial terms."""
        assert s6r_data['n_terms_new'] > 0

    def test_p_new_term_count(self, s6r_data):
        """P_new has exactly 6 monomials involving S_6 or S_7."""
        assert s6r_data['n_terms_new'] == 6

    def test_p_old_has_terms(self, s6r_data):
        """P_old (S_3, S_4, S_5 only) has a positive number of terms."""
        assert s6r_data['n_terms_old'] > 0

    def test_p_old_term_count(self, s6r_data):
        """P_old has 31 monomials in kappa, S_3, S_4, S_5."""
        assert s6r_data['n_terms_old'] == 31

    def test_total_terms_consistent(self, s6r_data):
        """P_old + P_new accounts for the full planted-forest polynomial."""
        assert s6r_data['n_terms_old'] + s6r_data['n_terms_new'] == 37

    def test_p_new_degree(self, s6r_data):
        """P_new has total degree 3 (mixed monomials in shadow variables)."""
        assert s6r_data['degree_new'] == 3

    def test_p_old_plus_p_new_equals_pf(self, s6r_data):
        """P_old + P_new reconstructs the full delta_pf^{(4,0)}."""
        p_old = s6r_data['p_old']
        p_new = s6r_data['p_new']
        total = expand(p_old + p_new)

        kappa_sym = Symbol('kappa')
        S3_sym = Symbol('S_3')
        S4_sym = Symbol('S_4')
        S5_sym = Symbol('S_5')
        S6_sym = Symbol('S_6')
        S7_sym = Symbol('S_7')

        shadow_generic = ShadowData(
            'generic', kappa_sym, S3_sym, S4_sym,
            shadows={5: S5_sym, 6: S6_sym, 7: S7_sym},
            depth_class='M',
        )
        pf_full = expand(delta_pf_genus4(shadow_generic))
        assert simplify(total - pf_full) == 0

    def test_p_new_vanishes_when_s6_s7_zero(self, s6r_data):
        """Setting S_6 = S_7 = 0 kills P_new entirely."""
        p_new = s6r_data['p_new']
        S6_sym = Symbol('S_6')
        S7_sym = Symbol('S_7')
        result = p_new.subs([(S6_sym, 0), (S7_sym, 0)])
        assert simplify(result) == 0


# ============================================================================
# Section R: Clutching independence (structural argument)
# ============================================================================

class TestClutchingIndependence:
    """Prove S_6-dependent terms are independent of clutching pushforwards."""

    @pytest.fixture(scope="class")
    def ci_data(self):
        return clutching_independence_genus4()

    def test_s6_terms_exist(self, ci_data):
        """S_6/S_7 terms exist in delta_pf^{(4,0)}."""
        assert ci_data['s6_terms_exist']

    def test_structural_independence(self, ci_data):
        """Structural independence from lower-genus pushforwards."""
        assert ci_data['structural_independence']

    def test_n_new_terms_positive(self, ci_data):
        """Positive number of genuinely new terms."""
        assert ci_data['n_new_terms'] > 0

    def test_max_clutching_shadow_is_5(self, ci_data):
        """Clutching from genera <= 3 uses at most S_5."""
        assert ci_data['max_clutching_shadow_arity'] == 5

    def test_new_shadows_are_s6_s7(self, ci_data):
        """The new shadow coefficients at genus 4 are S_6 and S_7."""
        assert ci_data['new_shadows_at_genus4'] == {'S_6', 'S_7'}

    def test_clutching_channels(self, ci_data):
        """Three clutching channels to genus 4: (1,3), (2,2), (3,ns)."""
        channels = ci_data['clutching_channels']
        assert (1, 3) in channels
        assert (2, 2) in channels
        assert (3, 'ns') in channels

    def test_s6_visibility_genus_is_4(self):
        """g_min(S_6) = 4: S_6 first contributes at genus 4."""
        assert shadow_visibility_genus(6) == 4

    def test_s7_visibility_genus_is_4(self):
        """g_min(S_7) = 4: S_7 also first contributes at genus 4."""
        assert shadow_visibility_genus(7) == 4


# ============================================================================
# Section S: Shadow subspace dimension by codimension
# ============================================================================

class TestShadowSubspaceDimension:
    """Compute dim(shadow subspace) at each codimension of R*(M-bar_4)."""

    @pytest.fixture(scope="class")
    def ss_data(self):
        return shadow_subspace_summary()

    def test_total_shadow_rank_positive(self, ss_data):
        """Total shadow rank across all codimensions is positive."""
        assert ss_data['total_shadow_rank'] > 0

    def test_total_shadow_rank_lower_bound(self, ss_data):
        """Total shadow rank >= 17 (from 8 codimensions with rank >= 2)."""
        assert ss_data['total_shadow_rank'] >= 17

    def test_max_rank_is_3(self, ss_data):
        """Maximum cross-family rank at any codimension is 3."""
        assert ss_data['max_cross_family_rank'] == 3

    def test_s6_codims(self, ss_data):
        """S_6 contributes at codim 4."""
        assert 4 in ss_data['codims_with_s6']

    def test_rank_ge_2_codims(self, ss_data):
        """Cross-family rank >= 2 at codimensions 2-9."""
        rge2 = ss_data['codims_with_rank_ge_2']
        for k in range(2, 10):
            assert k in rge2, f"Codim {k} missing from rank >= 2 list"

    def test_codim_0_rank_zero(self, ss_data):
        """Codim 0 (fundamental class): no planted-forest contribution."""
        d = ss_data['by_codim'][0]
        assert d['cross_family_rank_lower_bound'] == 0

    def test_codim_1_rank_zero(self, ss_data):
        """Codim 1 (divisor classes): no planted-forest contribution."""
        d = ss_data['by_codim'][1]
        assert d['cross_family_rank_lower_bound'] == 0

    def test_codim_4_rank_3(self, ss_data):
        """Codim 4 has rank 3 (S_6 active: L, C, M are independent)."""
        d = ss_data['by_codim'][4]
        assert d['cross_family_rank_lower_bound'] == 3

    def test_heisenberg_never_contributes(self, ss_data):
        """Class G (Heisenberg) contributes zero at every codimension."""
        for k in range(10):
            d = ss_data['by_codim'][k]
            assert not d['heisenberg_contributes']

    def test_virasoro_contributes_at_codim_2_plus(self, ss_data):
        """Virasoro contributes at codimensions >= 2."""
        for k in range(2, 10):
            d = ss_data['by_codim'][k]
            assert d['virasoro_contributes'], (
                f"Virasoro should contribute at codim {k}"
            )

    def test_three_families_contribute_at_codim_4(self, ss_data):
        """At codim 4, three families (L, C, M) contribute."""
        d = ss_data['by_codim'][4]
        assert d['n_contributing_families'] == 3


# ============================================================================
# Section T: Cross-family rank analysis
# ============================================================================

class TestCrossFamilyRank:
    """Cross-family independence verified by structural shadow analysis."""

    @pytest.fixture(scope="class")
    def independence_data(self):
        return cross_family_independence_test()

    def test_hierarchy_confirmed(self, independence_data):
        """G subset L subset C subset M hierarchy is confirmed."""
        assert independence_data['hierarchy_G_subset_L_subset_C_subset_M']

    def test_m_exceeds_l_structurally(self, independence_data):
        """M exceeds L structurally (M uses S_6, L does not)."""
        assert independence_data['M_exceeds_L']

    def test_m_exceeds_c_structurally(self, independence_data):
        """M exceeds C structurally."""
        assert independence_data['M_exceeds_C']

    def test_m_uses_s6(self, independence_data):
        """M uses S_6 (structural independence certificate)."""
        assert independence_data['M_uses_S6']

    def test_g_is_trivial(self, independence_data):
        """Class G (Heisenberg) has trivial planted-forest."""
        assert independence_data['G_pf_zero']


# ============================================================================
# Section U: Virasoro per-codimension rank
# ============================================================================

class TestVirasPerCodimRank:
    """Virasoro planted-forest rank at each codimension."""

    @pytest.fixture(scope="class")
    def rank_data(self):
        return virasoro_rank_by_codimension()

    def test_codim_0_rank_zero(self, rank_data):
        """Codim 0: rank 0 (no planted-forest at codim 0)."""
        assert rank_data[0]['rank'] == 0

    def test_codim_1_rank_zero(self, rank_data):
        """Codim 1: rank 0 (no planted-forest at codim 1)."""
        assert rank_data[1]['rank'] == 0

    def test_codim_2_rank_one(self, rank_data):
        """Codim 2: rank 1 (single rational function of c)."""
        assert rank_data[2]['rank'] == 1

    def test_nonzero_codims_have_rank_one(self, rank_data):
        """Every nonzero codim has rank 1 (single-parameter family)."""
        for k in range(10):
            if rank_data[k]['nonzero']:
                assert rank_data[k]['rank'] == 1

    def test_at_least_6_nonzero_codims(self, rank_data):
        """At least 6 codimensions have nonzero Virasoro contribution."""
        n_nonzero = sum(1 for k in range(10) if rank_data[k]['nonzero'])
        assert n_nonzero >= 6


# ============================================================================
# Section V: Generation strength (combined assessment)
# ============================================================================

class TestGenerationStrength:
    """Combined assessment of Pixton generation strength at genus 4."""

    def test_s6_isolation_confirms_contribution(self):
        """S_6 isolation test confirms nonzero contribution."""
        s6 = s6_isolation_test()
        assert s6['s6_contributes']

    def test_6_new_monomials(self):
        """6 genuinely new monomials from S_6/S_7 at genus 4."""
        s6r = s6_restricted_polynomial()
        assert s6r['n_terms_new'] == 6

    def test_structural_independence_from_clutching(self):
        """Structural independence from all lower-genus clutching."""
        ci = clutching_independence_genus4()
        assert ci['structural_independence']

    def test_total_rank_exceeds_pixton_codim_5_start(self):
        """Total shadow rank exceeds the genus-4 Pixton start codimension.

        The Pixton ideal has nontrivial generators starting at codim
        g+1 = 5.  The shadow subspace has rank >= 17 across codims 0-9,
        indicating substantial generation power.
        """
        ss = shadow_subspace_summary()
        assert ss['total_shadow_rank'] >= 5

    def test_three_independent_elements_at_codim_4(self):
        """Three linearly independent Pixton elements at codim 4.

        Classes L (S_3 only), C (S_3, S_4), and M (S_3, ..., S_7) give
        three structurally independent planted-forest polynomials at
        codimension 4, where S_6 is active.
        """
        ss = shadow_subspace_summary()
        assert ss['by_codim'][4]['cross_family_rank_lower_bound'] == 3

    def test_generation_advances_conjecture(self):
        """Combined evidence: conj:pixton-from-shadows is significantly
        advanced at genus 4.

        Membership: PROVED (D^2=0 + JPPZ18).
        Independence: PROVED (S_6 structural argument).
        Generation: 3 independent elements at codim 4, rank >= 17 total.
        """
        ci = clutching_independence_genus4()
        ss = shadow_subspace_summary()
        assert ci['structural_independence']
        assert ss['total_shadow_rank'] >= 17
        assert ss['max_cross_family_rank'] >= 3
