r"""Tests for theorem: Virasoro constraints = genus-0 arity-(n+2) MC projections.

THEOREM UNDER TEST:
  L_n Z^sh = 0 (n >= -1) is the (g=0, arity n+2) projection of the
  MC equation D*Theta + (1/2)[Theta,Theta] = 0 in g^mod_A.

VERIFICATION STRATEGY (multi-path, per mandate):
  Path 1: DVV recursion (which IS the MC boundary equation)
  Path 2: Direct WK intersection number computation
  Path 3: Kappa-scaled verification
  Path 4: Structural (boundary strata counts, dimension checks)

All arithmetic is exact (fractions.Fraction). No floating point.
"""

from fractions import Fraction
import pytest

from compute.lib.theorem_virasoro_constraints_mc_engine import (
    lambda_fp,
    shadow_free_energy,
    wk_intersection,
    genus0_boundary_strata,
    mc_genus0_arity_k_terms,
    proof1_mc_projection_equals_virasoro,
    proof2_kodaira_spencer,
    proof3_kappa_scaling,
    proof4_w_constraints,
    mc_general_genus_projection,
    verify_mc_at_genus_arity,
    virasoro_mc_address_table,
    triple_verification_constraint,
    full_theorem_verification,
    mc_boundary_chain_genus0,
    shadow_equation_classification,
    mc_arity_virasoro_dictionary,
    kappa_scaled_virasoro_operators,
)


# ============================================================================
# Section 0: Faber-Pandharipande number verification (foundation)
# ============================================================================

class TestLambdaFP:
    """Verify FP numbers by multiple paths (AP10: never trust hardcoded alone)."""

    def test_lambda_fp_g1(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_g2(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_g3(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_fp_g4(self):
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_lambda_fp_positive(self):
        """All lambda_g^FP are positive (AP22)."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_lambda_fp_decreasing(self):
        """lambda_g^FP is strictly decreasing (Bernoulli decay)."""
        for g in range(1, 7):
            assert lambda_fp(g) > lambda_fp(g + 1)


# ============================================================================
# Section 1: WK intersection number verification (DVV recursion)
# ============================================================================

class TestWKIntersection:
    """Verify WK numbers by direct computation."""

    def test_seed_tau0_cubed(self):
        """<tau_0^3>_0 = 1 (the normalization seed)."""
        assert wk_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_tau1_genus1(self):
        """<tau_1>_1 = 1/24."""
        assert wk_intersection(1, (1,)) == Fraction(1, 24)

    def test_string_equation_genus0(self):
        """String equation: <tau_0 tau_0 tau_d>_0 = 1 for d=0."""
        # <tau_0^3>_0 = 1 via seed
        assert wk_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_dimension_constraint(self):
        """Vanishing when dimension constraint fails."""
        # sum d_i != 3g - 3 + n
        assert wk_intersection(0, (1, 0, 0)) == Fraction(0)  # sum=1, target=0
        assert wk_intersection(1, (0,)) == Fraction(0)  # sum=0, target=1

    def test_stability_constraint(self):
        """Vanishing when stability fails."""
        assert wk_intersection(0, (0,)) == Fraction(0)  # 2*0-2+1 = -1 <= 0
        assert wk_intersection(0, (0, 0)) == Fraction(0)  # 2*0-2+2 = 0 <= 0

    def test_genus1_dilaton(self):
        """Dilaton: <tau_1 tau_1>_1 = (2*1-2+1)*<tau_1>_1 = 1/24."""
        val = wk_intersection(1, (1, 1))
        expected = Fraction(1) * Fraction(1, 24)  # (2*1-2+1) * 1/24
        assert val == expected

    def test_genus2_tau4(self):
        """<tau_4>_2 = 1/1152 (unique nonzero 1-point at genus 2)."""
        assert wk_intersection(2, (4,)) == Fraction(1, 1152)

    def test_genus0_four_point(self):
        """<tau_0 tau_0 tau_0 tau_1>_0 = 1 (via string equation)."""
        # String: <tau_0 * tau_0 tau_0 tau_1>_0 = <tau_0 tau_0 tau_0>_0 = 1
        val = wk_intersection(0, (0, 0, 0, 1))
        # String equation: inserting tau_0 into <tau_0 tau_0 tau_1>_0
        # = <tau_0 tau_0 tau_0>_0 (lowering tau_1 to tau_0) = 1
        assert val == Fraction(1)


# ============================================================================
# Section 2: Genus-0 boundary strata (geometric verification)
# ============================================================================

class TestGenus0BoundaryStrata:
    """Verify boundary strata enumeration for M-bar_{0,k}."""

    def test_mbar03_no_boundary(self):
        """M-bar_{0,3} = point, no codimension-1 boundary."""
        result = genus0_boundary_strata(3)
        assert result['num_strata'] == 0
        assert result['dimension'] == 0

    def test_mbar04_one_stratum(self):
        """M-bar_{0,4} = P^1 has 3 boundary divisors (3 partitions of 4 into 2+2)."""
        result = genus0_boundary_strata(4)
        assert result['dimension'] == 1
        assert result['num_strata'] == 3

    def test_mbar05_strata_count(self):
        """M-bar_{0,5} has 10 boundary divisors."""
        result = genus0_boundary_strata(5)
        assert result['dimension'] == 2
        assert result['num_strata'] == 10

    def test_mbar06_strata_count(self):
        """M-bar_{0,6} has 25 boundary divisors."""
        result = genus0_boundary_strata(6)
        assert result['dimension'] == 3
        assert result['num_strata'] == 25

    def test_boundary_formula(self):
        """Number of strata = (2^{k-1} - k - 1) for k >= 4.

        For unordered partitions with point 1 fixed in I:
        we need |I| >= 2 (1 is in I, need one more from {2,...,k})
        and |J| >= 2 (at least 2 points not in I).
        Total masks: 2^{k-1} (each of points 2,...,k in I or J).
        Subtract: all in I (1 mask), all in J (1 mask),
        exactly one in J = k-1 masks. Also subtract 0 masks where |J|<2.
        Actually the formula is more subtle. Just check values.
        """
        # Known counts:
        expected = {4: 3, 5: 10, 6: 25, 7: 56}
        for k, exp in expected.items():
            result = genus0_boundary_strata(k)
            assert result['num_strata'] == exp, \
                f"M-bar_{{0,{k}}}: expected {exp} strata, got {result['num_strata']}"


# ============================================================================
# Section 3: MC decomposition at genus 0 (structural verification)
# ============================================================================

class TestMCGenus0AritykTerms:
    """Verify the MC equation decomposition at genus 0."""

    def test_arity2_is_string(self):
        """MC at (0,2) = L_{-1} = string equation."""
        result = mc_genus0_arity_k_terms(2)
        assert result['virasoro_index'] == -1
        assert result['handle_term'] == 'ABSENT at genus 0'

    def test_arity3_is_dilaton(self):
        """MC at (0,3) = L_0 = dilaton equation."""
        result = mc_genus0_arity_k_terms(3)
        assert result['virasoro_index'] == 0

    def test_arity4_is_L1(self):
        """MC at (0,4) = L_1."""
        result = mc_genus0_arity_k_terms(4)
        assert result['virasoro_index'] == 1

    def test_arity_k_is_L_kminus3(self):
        """MC at (0,k) = L_{k-3} for k >= 2."""
        for k in range(2, 10):
            result = mc_genus0_arity_k_terms(k)
            assert result['virasoro_index'] == k - 3

    def test_no_handle_at_genus0(self):
        """Handle terms are absent at genus 0."""
        for k in range(2, 8):
            result = mc_genus0_arity_k_terms(k)
            assert result['handle_term'] == 'ABSENT at genus 0'

    def test_genus_is_zero(self):
        """All genus-0 MC terms have genus = 0."""
        for k in range(2, 8):
            result = mc_genus0_arity_k_terms(k)
            assert result['genus'] == 0


# ============================================================================
# Section 4: PROOF 1 — MC projection = Virasoro constraint (computational)
# ============================================================================

class TestProof1MCProjection:
    """Verify Proof 1: DVV/MC boundary = Virasoro constraint."""

    def test_string_equation_all_pass(self):
        """L_{-1} (string equation) verified at multiple genera."""
        result = proof1_mc_projection_equals_virasoro(-1, max_genus=2, max_extra_insertions=2)
        assert result['all_pass']

    def test_dilaton_equation_all_pass(self):
        """L_0 (dilaton equation) verified at multiple genera."""
        result = proof1_mc_projection_equals_virasoro(0, max_genus=2, max_extra_insertions=2)
        assert result['all_pass']

    def test_L1_all_pass(self):
        """L_1 verified at multiple genera."""
        result = proof1_mc_projection_equals_virasoro(1, max_genus=2, max_extra_insertions=2)
        assert result['all_pass']

    def test_L2_all_pass(self):
        """L_2 verified at multiple genera."""
        result = proof1_mc_projection_equals_virasoro(2, max_genus=2, max_extra_insertions=1)
        assert result['all_pass']

    def test_L3_all_pass(self):
        """L_3 verified."""
        result = proof1_mc_projection_equals_virasoro(3, max_genus=1, max_extra_insertions=1)
        assert result['all_pass']

    def test_L4_all_pass(self):
        """L_4 verified."""
        result = proof1_mc_projection_equals_virasoro(4, max_genus=1, max_extra_insertions=1)
        assert result['all_pass']

    def test_L5_all_pass(self):
        """L_5 verified."""
        result = proof1_mc_projection_equals_virasoro(5, max_genus=1, max_extra_insertions=0)
        assert result['all_pass']

    def test_mc_arity_matches_virasoro_index(self):
        """MC arity in results matches n_vir + 2."""
        for n_vir in range(-1, 4):
            result = proof1_mc_projection_equals_virasoro(n_vir, max_genus=1, max_extra_insertions=0)
            assert result['mc_arity'] == n_vir + 2

    def test_string_genus0_explicit(self):
        """L_{-1} at genus 0: <tau_0^3>_0 = 1 via string equation."""
        result = proof1_mc_projection_equals_virasoro(-1, max_genus=0, max_extra_insertions=3)
        # Should include the seed case
        assert result['all_pass']


# ============================================================================
# Section 5: PROOF 2 — Kodaira-Spencer identification
# ============================================================================

class TestProof2KodairaSpencer:
    """Verify Proof 2: bar complex = KS deformation complex."""

    def test_kodaira_spencer_all_pass(self):
        result = proof2_kodaira_spencer(max_genus=2)
        assert result['all_pass']

    def test_frobenius_metric_seed(self):
        result = proof2_kodaira_spencer(max_genus=1)
        assert result['frobenius_metric']['passes']

    def test_wdvv_vacuous_rank1(self):
        """WDVV is vacuous for rank-1 Frobenius manifold."""
        result = proof2_kodaira_spencer(max_genus=1)
        assert 'vacuous' in result['wdvv_rank1']['status']

    def test_arity_map_complete(self):
        """Arity map covers L_{-1} through L_4."""
        result = proof2_kodaira_spencer(max_genus=1)
        for k in range(2, 8):
            assert k in result['arity_map']
            assert result['arity_map'][k]['virasoro_index'] == k - 3


# ============================================================================
# Section 6: PROOF 3 — Kappa-scaling compatibility
# ============================================================================

class TestProof3KappaScaling:
    """Verify Proof 3: Virasoro constraints survive kappa-scaling."""

    def test_kappa_half_all_pass(self):
        """kappa = 1/2 (Virasoro at c=1)."""
        result = proof3_kappa_scaling(Fraction(1, 2))
        assert result['all_pass']

    def test_kappa_1_all_pass(self):
        """kappa = 1 (Heisenberg at k=1, or KW itself)."""
        result = proof3_kappa_scaling(Fraction(1))
        assert result['all_pass']

    def test_kappa_13_half_all_pass(self):
        """kappa = 13/2 (Virasoro at c=13, self-dual point)."""
        result = proof3_kappa_scaling(Fraction(13, 2))
        assert result['all_pass']

    def test_ratio_is_kappa(self):
        """F_g^shadow / F_g^KW = kappa for all g."""
        kappa = Fraction(3, 7)
        result = proof3_kappa_scaling(kappa, max_genus=6)
        for g_data in result['genus_checks'].values():
            assert g_data['kappa_constant']

    def test_virasoro_linearity(self):
        """L_n is a first-order differential operator."""
        result = proof3_kappa_scaling(Fraction(1, 2))
        assert result['virasoro_linearity']['kappa_commutes']

    def test_kdv_negative_result(self):
        """tau_KW^kappa does NOT satisfy KdV for kappa != 1."""
        result = proof3_kappa_scaling(Fraction(1, 2))
        assert 'NOT' in result['kdv_negative']['statement']

    def test_kappa_scaled_operator_unchanged(self):
        """L_n^{(kappa)} = L_n (the operator does not deform)."""
        for n in range(-1, 5):
            op = kappa_scaled_virasoro_operators(n, Fraction(1, 2))
            assert op['no_deformation']


# ============================================================================
# Section 7: PROOF 4 — W-constraints for W_N
# ============================================================================

class TestProof4WConstraints:
    """Verify Proof 4: W-constraints generalize Virasoro for W_N."""

    def test_w_constraints_all_pass(self):
        result = proof4_w_constraints(max_N=4)
        assert result['all_pass']

    def test_n2_is_virasoro(self):
        """W_2 = Virasoro."""
        result = proof4_w_constraints()
        assert result['n2_reduction']['passes']
        assert result['families'][2]['n_generators'] == 1

    def test_n3_is_boussinesq(self):
        """W_3 gives Boussinesq (3rd Gelfand-Dickey)."""
        result = proof4_w_constraints()
        assert result['families'][3]['n_generators'] == 2
        assert 'Boussinesq' in result['families'][3]['hierarchy']

    def test_rank_equals_n_minus_1(self):
        """W_N has rank N-1."""
        result = proof4_w_constraints(max_N=5)
        for N in range(2, 6):
            assert result['families'][N]['rank'] == N - 1


# ============================================================================
# Section 8: MC at general genus (handle terms)
# ============================================================================

class TestMCGeneralGenus:
    """Verify MC equation at g > 0 includes handle terms."""

    def test_genus0_no_handle(self):
        result = mc_general_genus_projection(0, 4)
        assert result['bracket_handle'] == 'ABSENT'
        assert result['is_classical']

    def test_genus1_has_handle(self):
        result = mc_general_genus_projection(1, 4)
        assert 'ABSENT' not in result['bracket_handle']
        assert result['quantum_correction']

    def test_genus2_has_handle(self):
        result = mc_general_genus_projection(2, 3)
        assert '1' in result['bracket_handle']  # genus 2 -> 1

    def test_virasoro_index_correct(self):
        """Virasoro index = arity - 3."""
        for k in range(2, 8):
            result = mc_general_genus_projection(0, k)
            assert result['virasoro_index'] == k - 3

    def test_verify_mc_genus1_arity3(self):
        """MC at (1, 3) = L_0 at genus 1."""
        result = verify_mc_at_genus_arity(1, 3, ())
        assert result['passes']

    def test_verify_mc_genus1_arity2(self):
        """MC at (1, 2) = L_{-1} at genus 1."""
        result = verify_mc_at_genus_arity(1, 2, (0,))
        assert result['passes']


# ============================================================================
# Section 9: Address table
# ============================================================================

class TestAddressTable:
    """Verify the Virasoro-MC address table."""

    def test_address_table_has_entries(self):
        table = virasoro_mc_address_table(max_n=5, max_g=3)
        assert len(table) > 0

    def test_l_minus1_address(self):
        table = virasoro_mc_address_table()
        entry = table['L_-1_g0']
        assert entry['mc_arity'] == 1  # -1 + 2 = 1
        assert entry['virasoro_index'] == -1

    def test_l0_address(self):
        table = virasoro_mc_address_table()
        entry = table['L_0_g0']
        assert entry['mc_arity'] == 2
        assert entry['virasoro_index'] == 0

    def test_l1_address(self):
        table = virasoro_mc_address_table()
        entry = table['L_1_g0']
        assert entry['mc_arity'] == 3
        assert entry['virasoro_index'] == 1

    def test_handle_terms_only_at_positive_genus(self):
        table = virasoro_mc_address_table(max_n=5, max_g=3)
        for key, entry in table.items():
            if entry['genus'] == 0:
                assert not entry['handle_terms']
            else:
                assert entry['handle_terms']


# ============================================================================
# Section 10: Triple cross-verification
# ============================================================================

class TestTripleVerification:
    """Verify all three paths agree for individual constraints."""

    def test_triple_string_genus0(self):
        result = triple_verification_constraint(-1, 0, (0, 0), Fraction(1, 2))
        assert result['all_three_agree']

    def test_triple_dilaton_genus1(self):
        result = triple_verification_constraint(0, 1, (1,), Fraction(1, 2))
        assert result['all_three_agree']

    def test_triple_L1_genus1(self):
        """L_1 at genus 1 with tau_0 insertion."""
        result = triple_verification_constraint(1, 1, (0,), Fraction(1, 2))
        assert result['all_three_agree']

    def test_triple_kappa_13_half(self):
        """Triple verification at the self-dual point kappa = 13/2."""
        result = triple_verification_constraint(-1, 0, (0, 0), Fraction(13, 2))
        assert result['all_three_agree']

    def test_triple_kappa_3(self):
        """Triple verification at kappa = 3 (affine sl_2 at k=2)."""
        result = triple_verification_constraint(0, 1, (1,), Fraction(3))
        assert result['all_three_agree']


# ============================================================================
# Section 11: Full theorem verification
# ============================================================================

class TestFullTheorem:
    """Comprehensive theorem verification."""

    def test_full_verification_kappa_half(self):
        """Full verification at kappa = 1/2 (Virasoro at c=1)."""
        result = full_theorem_verification(
            kappa_val=Fraction(1, 2), max_genus=2, max_n_vir=3, max_extra=1)
        assert result['all_pass'], result.get('summary', '')

    def test_full_verification_kappa_1(self):
        """Full verification at kappa = 1 (Heisenberg at k=1)."""
        result = full_theorem_verification(
            kappa_val=Fraction(1), max_genus=2, max_n_vir=3, max_extra=1)
        assert result['all_pass'], result.get('summary', '')

    def test_all_four_proofs_pass(self):
        """Each of the four proofs passes independently."""
        result = full_theorem_verification(
            kappa_val=Fraction(1, 2), max_genus=2, max_n_vir=3, max_extra=1)
        assert result['proofs']['proof1_mc_projection']['all_pass']
        assert result['proofs']['proof2_kodaira_spencer']['all_pass']
        assert result['proofs']['proof3_kappa_scaling']['all_pass']
        assert result['proofs']['proof4_w_constraints']['all_pass']

    def test_cross_checks_pass(self):
        """All triple cross-checks pass."""
        result = full_theorem_verification(
            kappa_val=Fraction(1, 2), max_genus=2, max_n_vir=3, max_extra=1)
        assert result['cross_checks_all_pass']


# ============================================================================
# Section 12: Boundary chain verification
# ============================================================================

class TestBoundaryChain:
    """Verify MC boundary chain at genus 0."""

    def test_boundary_arity4(self):
        result = mc_boundary_chain_genus0(4)
        assert result['dim_mbar_0k'] == 1
        assert result['num_strata'] == 3

    def test_boundary_arity5(self):
        result = mc_boundary_chain_genus0(5)
        assert result['dim_mbar_0k'] == 2
        assert result['num_strata'] == 10

    def test_no_handle_genus0(self):
        for k in range(3, 8):
            result = mc_boundary_chain_genus0(k)
            assert result['mc_decomposition']['handle_term'] == 'ABSENT (genus 0)'


# ============================================================================
# Section 13: Equation classification (positive and negative results)
# ============================================================================

class TestEquationClassification:
    """Verify which equations the shadow PF satisfies/does not satisfy."""

    def test_satisfies_virasoro(self):
        result = shadow_equation_classification(Fraction(1, 2))
        assert result['satisfies']['virasoro_constraints']

    def test_satisfies_mc(self):
        result = shadow_equation_classification(Fraction(1, 2))
        assert result['satisfies']['mc_equation']

    def test_satisfies_string(self):
        result = shadow_equation_classification(Fraction(1, 2))
        assert result['satisfies']['string_equation']

    def test_satisfies_dilaton(self):
        result = shadow_equation_classification(Fraction(1, 2))
        assert result['satisfies']['dilaton_equation']

    def test_does_not_satisfy_kdv_kappa_half(self):
        """tau_KW^{1/2} does NOT satisfy KdV."""
        result = shadow_equation_classification(Fraction(1, 2))
        assert result['does_not_satisfy']['kdv_hierarchy']

    def test_kdv_at_kappa_1(self):
        """tau_KW^1 = tau_KW DOES satisfy KdV."""
        result = shadow_equation_classification(Fraction(1))
        assert not result['does_not_satisfy']['kdv_hierarchy']

    def test_free_energy_ratios_constant(self):
        result = shadow_equation_classification(Fraction(3, 7))
        assert result['free_energy_check']['ratios_constant']


# ============================================================================
# Section 14: Dictionary verification
# ============================================================================

class TestDictionary:
    """Verify the MC-arity to Virasoro dictionary."""

    def test_dictionary_has_entries(self):
        d = mc_arity_virasoro_dictionary()
        assert len(d) > 0

    def test_arity2_is_string(self):
        d = mc_arity_virasoro_dictionary()
        assert d['arity_2']['virasoro'] == 'L_-1'

    def test_arity3_is_dilaton(self):
        d = mc_arity_virasoro_dictionary()
        assert d['arity_3']['virasoro'] == 'L_0'

    def test_arity4_is_L1(self):
        d = mc_arity_virasoro_dictionary()
        assert d['arity_4']['virasoro'] == 'L_1'

    def test_all_have_merge_terms(self):
        d = mc_arity_virasoro_dictionary()
        for key, entry in d.items():
            assert entry['merge_terms'] == 'yes (D-term)'

    def test_handle_terms_at_positive_genus_only(self):
        d = mc_arity_virasoro_dictionary()
        for key, entry in d.items():
            assert entry['handle_terms'] == 'at g > 0 only'


# ============================================================================
# Section 15: Shadow free energy consistency
# ============================================================================

class TestShadowFreeEnergy:
    """Verify F_g = kappa * lambda_g^FP."""

    def test_shadow_free_energy_g1(self):
        assert shadow_free_energy(Fraction(1, 2), 1) == Fraction(1, 48)

    def test_shadow_free_energy_g2(self):
        assert shadow_free_energy(Fraction(1, 2), 2) == Fraction(7, 11520)

    def test_shadow_free_energy_kappa_1(self):
        """At kappa = 1, F_g = lambda_g^FP."""
        for g in range(1, 6):
            assert shadow_free_energy(Fraction(1), g) == lambda_fp(g)

    def test_shadow_free_energy_additivity(self):
        """F_g(kappa_1 + kappa_2) = F_g(kappa_1) + F_g(kappa_2)."""
        k1, k2 = Fraction(1, 3), Fraction(2, 5)
        for g in range(1, 5):
            assert (shadow_free_energy(k1 + k2, g)
                    == shadow_free_energy(k1, g) + shadow_free_energy(k2, g))


# ============================================================================
# Section 16: Explicit DVV recursion checks (independent of Proof 1 wrapper)
# ============================================================================

class TestExplicitDVV:
    """Verify DVV recursion at specific correlators, independent of Proof 1."""

    def test_dvv_genus0_tau0_tau0_tau0(self):
        """<tau_0^3>_0 = 1 (seed, no recursion needed)."""
        assert wk_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_dvv_genus0_tau0_tau1(self):
        """<tau_0 tau_1>_0 = 0 (unstable: 2*0-2+2=0)."""
        assert wk_intersection(0, (0, 1)) == Fraction(0)

    def test_dvv_genus0_5point(self):
        """<tau_0^4 tau_1>_0 via string equation."""
        # <tau_0^4 tau_1>_0: n=5, g=0, sum=1, target=3*0-3+5=2. 1 != 2, so 0.
        assert wk_intersection(0, (0, 0, 0, 0, 1)) == Fraction(0)

    def test_dvv_genus1_tau1_tau1(self):
        """<tau_1^2>_1 = 1/24 (dilaton applied to <tau_1>_1)."""
        # Dilaton: <tau_1 tau_1>_1 = (2*1-2+1) * <tau_1>_1 = 1 * 1/24
        assert wk_intersection(1, (1, 1)) == Fraction(1, 24)

    def test_dvv_genus2_unique_1point(self):
        """<tau_4>_2 = 1/1152."""
        assert wk_intersection(2, (4,)) == Fraction(1, 1152)


# ============================================================================
# Section 17: Consistency of MC decomposition terms
# ============================================================================

class TestMCDecompositionConsistency:
    """Verify that MC decomposition (merge + split) = total DVV."""

    def test_L1_genus1_decomposition(self):
        """At genus 1, L_1 with no extra insertions: merge + handle + split = total."""
        from compute.lib.theorem_virasoro_constraints_mc_engine import (
            _verify_higher_virasoro,
        )
        result = _verify_higher_virasoro(1, 1, ())
        assert result['passes']
        # Check decomposition terms sum to total
        if 'mc_decomposition' in result:
            decomp = result['mc_decomposition']
            merge = decomp['merge (D-term)']
            handle = decomp['handle (absent at g=0)']
            split = decomp['split ([,]-term)']
            total = merge + handle + split
            assert total == result['lhs']

    def test_L2_genus0_decomposition(self):
        """At genus 0, L_2: handle = 0, merge + split = total."""
        from compute.lib.theorem_virasoro_constraints_mc_engine import (
            _verify_higher_virasoro,
        )
        # Need valid insertions: d=3, g=0, need sum = 3*0-3+n+1, n+1 = n_extra+1
        # d=3 + sum(insertions) = -3 + n+1 = n-2
        # With 4 insertions of (0,0,0,0): sum=3+0+0+0+0=3, target=3*0-3+5=2. 3!=2, fail.
        # With 3 insertions of (0,0): d=3, sum=3+0+0=3, target=3*0-3+4=1. 3!=1, fail.
        # Try with 5 insertions: d=3+sum=3*0-3+6=3. sum(ins)=0, 3=3. OK.
        # But that means 5 points with (0,0,0,0,0) and d=3:
        # total insertions = (0,0,0,0,0,3), n=6, sum=3, target=3*0-3+6=3. YES.
        result = _verify_higher_virasoro(2, 0, (0, 0, 0, 0, 0))
        assert result['passes']
        if 'mc_decomposition' in result:
            assert result['mc_decomposition']['handle (absent at g=0)'] == Fraction(0)


# ============================================================================
# Section 18: Multiple kappa values (AP39: kappa != c/2 in general)
# ============================================================================

class TestMultipleKappaValues:
    """Verify theorem at multiple kappa values from different families."""

    @pytest.mark.parametrize("kappa_val,family", [
        (Fraction(1, 2), "Virasoro c=1"),
        (Fraction(1), "Heisenberg k=1"),
        (Fraction(3), "Heisenberg k=3"),
        (Fraction(13, 2), "Virasoro c=13 (self-dual)"),
        (Fraction(13), "Virasoro c=26 (critical)"),
        (Fraction(3, 4), "Affine sl_2 k=-1"),
    ])
    def test_kappa_scaling_multiple_families(self, kappa_val, family):
        """F_g^shadow = kappa * lambda_g^FP for multiple families."""
        for g in range(1, 5):
            F_g = shadow_free_energy(kappa_val, g)
            assert F_g == kappa_val * lambda_fp(g), \
                f"Failed for {family} at genus {g}"

    @pytest.mark.parametrize("kappa_val", [
        Fraction(1, 2), Fraction(1), Fraction(5, 3),
    ])
    def test_triple_verify_multiple_kappa(self, kappa_val):
        """Triple verification at multiple kappa values."""
        result = triple_verification_constraint(-1, 0, (0, 0), kappa_val)
        assert result['all_three_agree']
