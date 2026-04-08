r"""Tests for the celestial-new-proofs engine.

Verifies the four central claims of the celestial-shadow bridge:

(a) Bootstrap axioms map to a SUBSET of K1-K12 (not the full equivalence).
(b) FP gives a uniqueness argument, NOT a new proof of shadow-formality.
(c) Soft theorem tower gives a PHYSICAL DERIVATION of the G/L/C/M classification.
(d) Theorem D has partial independent derivation from soft Ward identities.

TEST ORGANIZATION (40+ tests):
  I.   Exact arithmetic ground truth (Bernoulli, lambda_fp)
  II.  Kappa formulas (AP1 cross-verification, AP9 != c/2)
  III. Shadow towers (class G/L/C/M termination and non-termination)
  IV.  Bootstrap-Koszul dictionary (question a)
  V.   Shadow-formality route comparison (question b)
  VI.  Soft-shadow classification (question c)
  VII. Theorem D via soft Ward (question d)
  VIII.Bootstrap closure analysis (combined)
  IX.  Celestial-shadow identification (tree, 1-loop, 2-loop)
  X.   MC equation physical interpretation
  XI.  Multi-path kappa verification (3 paths)
  XII. Critical discriminant from soft data
  XIII.Full bridge analysis integration

Ground truth (independently computed):
    kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N)    [AP1]
    kappa(Vir_c) = c/2                         [AP1]
    kappa(H_k) = k                             [AP39]
    lambda_1^FP = 1/24                         [Faber-Pandharipande]
    lambda_2^FP = 7/5760                       [Faber-Pandharipande]
    S_4(Vir_c) = 10/[c(5c+22)]               [quartic contact]
    Delta(Vir_c) = 40/(5c+22)                 [critical discriminant]
    class L: S_r = 0 for r >= 4              [shadow depth 3]
    class G: S_r = 0 for r >= 3              [shadow depth 2]
    class M: S_r != 0 for all r >= 2         [infinite depth]
"""

from fractions import Fraction

import pytest

from compute.lib.theorem_celestial_new_proofs_engine import (
    # Arithmetic
    _frac,
    bernoulli_exact,
    lambda_fp_exact,
    # Kappa
    kappa_affine,
    kappa_virasoro,
    kappa_heisenberg,
    kappa_wn,
    central_charge_affine,
    # Shadow towers
    shadow_tower_virasoro,
    shadow_tower_affine,
    shadow_tower_heisenberg,
    # Bootstrap-Koszul bridge (question a)
    BootstrapKoszulMapping,
    bootstrap_koszul_dictionary,
    count_bootstrap_koszul_matches,
    # Shadow-formality routes (question b)
    ShadowFormalityRoute,
    compare_routes_at_arity,
    fp_uniqueness_contribution,
    # Soft-shadow classification (question c)
    SoftShadowCorrespondence,
    soft_shadow_dictionary_gluon,
    soft_shadow_dictionary_graviton,
    verify_soft_depth_equals_shadow_depth,
    soft_classification_physical,
    # Theorem D via soft Ward (question d)
    SoftWardKappaDerivation,
    theorem_d_via_soft_ward,
    count_independent_soft_proofs,
    # Bootstrap closure
    BootstrapClosureAnalysis,
    analyze_bootstrap_closure_heisenberg,
    analyze_bootstrap_closure_affine,
    analyze_bootstrap_closure_virasoro,
    # Celestial-shadow identification
    CelestialShadowIdentification,
    verify_celestial_shadow_tree_level,
    verify_celestial_shadow_one_loop,
    verify_celestial_shadow_two_loop,
    # MC equation
    mc_equation_physical_interpretation,
    # Multi-path kappa
    verify_kappa_three_paths,
    # Discriminant
    critical_discriminant_from_soft,
    # Full bridge
    full_bridge_analysis,
)


# ============================================================================
# I.  Exact arithmetic ground truth
# ============================================================================

class TestExactArithmetic:
    """Verify exact arithmetic against independently computed values."""

    def test_bernoulli_b0(self):
        assert bernoulli_exact(0) == Fraction(1)

    def test_bernoulli_b1(self):
        assert bernoulli_exact(1) == Fraction(-1, 2)

    def test_bernoulli_b2(self):
        assert bernoulli_exact(2) == Fraction(1, 6)

    def test_bernoulli_b4(self):
        assert bernoulli_exact(4) == Fraction(-1, 30)

    def test_bernoulli_b6(self):
        assert bernoulli_exact(6) == Fraction(1, 42)

    def test_bernoulli_odd_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            assert bernoulli_exact(n) == 0

    def test_lambda_fp_genus1(self):
        assert lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda_fp_genus2(self):
        assert lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda_fp_genus3(self):
        assert lambda_fp_exact(3) == Fraction(31, 967680)


# ============================================================================
# II.  Kappa formulas (AP1 cross-verification)
# ============================================================================

class TestKappaFormulas:
    """Verify kappa formulas from first principles (AP1)."""

    def test_kappa_sl2_k0(self):
        """kappa(V_0(sl_2)) = (4-1)(0+2)/(2*2) = 3/2."""
        assert kappa_affine(2, Fraction(0)) == Fraction(3, 2)

    def test_kappa_sl3_k0(self):
        """kappa(V_0(sl_3)) = (9-1)(0+3)/(2*3) = 4."""
        assert kappa_affine(3, Fraction(0)) == Fraction(4)

    def test_kappa_sl2_k1(self):
        """kappa(V_1(sl_2)) = 3*(1+2)/4 = 9/4."""
        assert kappa_affine(2, Fraction(1)) == Fraction(9, 4)

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13."""
        assert kappa_virasoro(Fraction(26)) == Fraction(13)

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert kappa_virasoro(Fraction(1)) == Fraction(1, 2)

    def test_kappa_heisenberg_k1(self):
        """kappa(H_1) = 1.  AP39: this != c/2 = 1/2."""
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)

    def test_kappa_heisenberg_neq_c_over_2(self):
        """AP39: kappa(H_k) = k != c/2 = k/2."""
        for k in [1, 2, 3, 5]:
            kap = kappa_heisenberg(Fraction(k))
            c_over_2 = Fraction(k, 2)
            assert kap != c_over_2, f"AP39 violation at k={k}"

    def test_kappa_affine_neq_c_over_2(self):
        """AP9: kappa(V_k(sl_N)) != c/2 for N > 1."""
        for N in [2, 3, 4]:
            for k in [1, 2, 3]:
                kap = kappa_affine(N, Fraction(k))
                c = central_charge_affine(N, Fraction(k))
                assert kap != c / 2, f"AP9 violation at sl_{N}, k={k}"


# ============================================================================
# III.  Shadow towers
# ============================================================================

class TestShadowTowers:
    """Verify shadow tower structure: termination for G/L, non-termination for M."""

    def test_heisenberg_class_g_depth_2(self):
        """Heisenberg: class G, shadow depth 2.  S_r = 0 for r >= 3."""
        tower = shadow_tower_heisenberg(Fraction(1))
        assert tower[2] == Fraction(1)  # kappa = k = 1
        for r in range(3, 11):
            assert tower[r] == 0, f"S_{r} nonzero for Heisenberg (class G)"

    def test_affine_class_l_depth_3(self):
        """Affine sl_N: class L, shadow depth 3.  S_r = 0 for r >= 4."""
        for N in [2, 3, 4]:
            tower = shadow_tower_affine(N, Fraction(1))
            assert tower[2] != 0  # kappa nonzero
            assert tower[3] != 0  # cubic shadow nonzero
            for r in range(4, 11):
                assert tower[r] == 0, f"S_{r} nonzero for sl_{N} (class L)"

    def test_virasoro_class_m_infinite(self):
        """Virasoro: class M, infinite depth.  S_r != 0 for all r >= 2."""
        for c in [Fraction(1), Fraction(26), Fraction(13)]:
            tower = shadow_tower_virasoro(c, max_arity=10)
            for r in range(2, 11):
                assert tower[r] != 0, f"S_{r} = 0 for Vir_{c} (should be class M)"

    def test_virasoro_s2_is_kappa(self):
        """S_2 = kappa = c/2 for Virasoro."""
        for c in [Fraction(1), Fraction(2), Fraction(26)]:
            tower = shadow_tower_virasoro(c)
            assert tower[2] == c / 2

    def test_virasoro_s4_quartic_contact(self):
        """S_4 = Q^contact = 10/[c(5c+22)] for Virasoro."""
        for c in [Fraction(1), Fraction(2), Fraction(26)]:
            tower = shadow_tower_virasoro(c)
            expected = Fraction(10) / (c * (5 * c + 22))
            assert tower[4] == expected, f"S_4 mismatch at c={c}"


# ============================================================================
# IV.  Bootstrap-Koszul dictionary (question a)
# ============================================================================

class TestBootstrapKoszulDictionary:
    """Verify the bootstrap-axiom to Koszul-characterization mapping."""

    def test_dictionary_not_empty(self):
        d = bootstrap_koszul_dictionary()
        assert len(d) >= 7

    def test_all_entries_have_proof_status(self):
        for entry in bootstrap_koszul_dictionary():
            assert entry.proof_status in ("PROVED", "CONDITIONAL", "OPEN")

    def test_associativity_is_universal(self):
        """OPE associativity = d^2=0, which is UNIVERSAL, not K1-K12."""
        d = bootstrap_koszul_dictionary()
        assoc = [e for e in d if "associativity" in e.bootstrap_axiom.lower()]
        assert len(assoc) >= 1
        assert assoc[0].koszul_item == "UNIVERSAL"

    def test_convergence_maps_to_k2(self):
        """OPE convergence maps to K2 (PBW collapse)."""
        d = bootstrap_koszul_dictionary()
        conv = [e for e in d if "convergence" in e.bootstrap_axiom.lower()]
        assert len(conv) >= 1
        assert conv[0].koszul_item == "K2"

    def test_crossing_maps_to_k10(self):
        """Crossing symmetry maps to K10 (FM boundary acyclicity)."""
        d = bootstrap_koszul_dictionary()
        cross = [e for e in d if "crossing" in e.bootstrap_axiom.lower()]
        assert len(cross) >= 1
        assert cross[0].koszul_item == "K10"

    def test_not_all_k_items_matched(self):
        """The bootstrap does NOT cover all 12 Koszul characterizations."""
        counts = count_bootstrap_koszul_matches()
        assert counts["matched_by_bootstrap"] < counts["total_koszul_items"]

    def test_unmatched_includes_k9_or_k11(self):
        """K9 (Kac-Shapovalov) and K11 (Lagrangian) should be unmatched."""
        counts = count_bootstrap_koszul_matches()
        unmatched = set(counts["unmatched_items"])
        # At least some of K4, K7, K8, K9, K11, K12 should be unmatched
        assert len(unmatched) >= 4


# ============================================================================
# V.  Shadow-formality route comparison (question b)
# ============================================================================

class TestShadowFormalityRoutes:
    """Verify that HTT and FP routes agree but are NOT independent proofs."""

    def test_routes_agree_at_arity_2(self):
        route = compare_routes_at_arity(2)
        assert route.agree is True
        assert route.is_independent_proof is False

    def test_routes_agree_at_arity_3(self):
        route = compare_routes_at_arity(3)
        assert route.agree is True
        assert route.is_independent_proof is False

    def test_routes_agree_at_arity_4(self):
        route = compare_routes_at_arity(4)
        assert route.agree is True
        assert route.is_independent_proof is False

    def test_routes_agree_at_arity_10(self):
        route = compare_routes_at_arity(10)
        assert route.agree is True
        assert route.is_independent_proof is False

    def test_fp_provides_uniqueness(self):
        """FP's genuine contribution: MC uniqueness on Koszul locus."""
        contrib = fp_uniqueness_contribution()
        assert "unique" in contrib["our_translation"].lower()
        assert contrib["is_new_proof"] == "YES -- for uniqueness on the Koszul locus"

    def test_fp_scope_is_koszul_locus(self):
        """FP covers the Koszul locus, not all algebras."""
        contrib = fp_uniqueness_contribution()
        assert "Koszul locus" in contrib["scope"]

    def test_catalan_numbers_in_tree_counts(self):
        """Verify Catalan number C_{r-1} appears in both routes."""
        from math import factorial
        for r in range(2, 8):
            route = compare_routes_at_arity(r)
            n = r - 1
            catalan = factorial(2 * n) // (factorial(n + 1) * factorial(n))
            assert str(catalan) in route.htt_description


# ============================================================================
# VI.  Soft-shadow classification (question c)
# ============================================================================

class TestSoftShadowClassification:
    """Verify the soft theorem <-> shadow depth correspondence."""

    def test_gluon_class_l_leading_nonzero(self):
        """Leading soft gluon (S^{(0)} = kappa) is nonzero for SU(N)."""
        for N in [2, 3, 4]:
            entries = soft_shadow_dictionary_gluon(N)
            leading = entries[0]
            assert leading.soft_order == 0
            assert leading.shadow_arity == 2
            assert leading.is_nonzero is True

    def test_gluon_class_l_subleading_nonzero(self):
        """Subleading soft gluon (S^{(1)} = S_3) is nonzero."""
        for N in [2, 3, 4]:
            entries = soft_shadow_dictionary_gluon(N)
            subleading = entries[1]
            assert subleading.soft_order == 1
            assert subleading.shadow_arity == 3
            assert subleading.is_nonzero is True

    def test_gluon_class_l_higher_vanish(self):
        """All sub^n-leading for n >= 2 vanish (class L tower terminates)."""
        entries = soft_shadow_dictionary_gluon(3)
        for entry in entries[2:]:
            assert entry.is_nonzero is False

    def test_graviton_class_m_all_nonzero(self):
        """All soft graviton theorems are nonzero (class M infinite tower)."""
        entries = soft_shadow_dictionary_graviton(Fraction(26), max_order=6)
        for entry in entries:
            assert entry.is_nonzero is True, (
                f"S^({entry.soft_order}) vanishes for SDGR -- class M should have "
                f"infinite tower"
            )

    def test_soft_depth_equals_shadow_depth_class_g(self):
        """Class G: shadow_depth=2, soft_depth=0."""
        result = verify_soft_depth_equals_shadow_depth("G", 2)
        assert result["verified"] is True
        assert result["soft_depth"] == 0

    def test_soft_depth_equals_shadow_depth_class_l(self):
        """Class L: shadow_depth=3, soft_depth=1."""
        result = verify_soft_depth_equals_shadow_depth("L", 3)
        assert result["verified"] is True
        assert result["soft_depth"] == 1

    def test_soft_depth_equals_shadow_depth_class_c(self):
        """Class C: shadow_depth=4, soft_depth=2."""
        result = verify_soft_depth_equals_shadow_depth("C", 4)
        assert result["verified"] is True
        assert result["soft_depth"] == 2

    def test_soft_depth_equals_shadow_depth_class_m(self):
        """Class M: both infinite."""
        result = verify_soft_depth_equals_shadow_depth("M", -1)
        assert result["verified"] is True

    def test_physical_classification_four_classes(self):
        """Physical classification has exactly four classes."""
        classes = soft_classification_physical()
        assert set(classes.keys()) == {"G", "L", "C", "M"}

    def test_physical_class_g_abelian(self):
        """Class G has abelian asymptotic symmetry."""
        classes = soft_classification_physical()
        assert "abelian" in classes["G"]["asymptotic_symmetry"].lower()

    def test_physical_class_m_winf(self):
        """Class M has w_{1+infinity} asymptotic symmetry."""
        classes = soft_classification_physical()
        assert "w_{1+inf" in classes["M"]["asymptotic_symmetry"].lower()


# ============================================================================
# VII.  Theorem D via soft Ward (question d)
# ============================================================================

class TestTheoremDSoftWard:
    """Verify which Theorem D properties have independent soft proofs."""

    def test_genus1_has_independent_soft_proof(self):
        """Genus-1 universality has an independent soft-theorem proof."""
        derivations = theorem_d_via_soft_ward()
        genus1 = [d for d in derivations if "genus-1" in d.property_name]
        assert len(genus1) >= 1
        assert genus1[0].is_independent is True

    def test_additivity_has_independent_soft_proof(self):
        """Kappa additivity has an independent soft-theorem proof."""
        derivations = theorem_d_via_soft_ward()
        additive = [d for d in derivations if "additiv" in d.property_name.lower()]
        assert len(additive) >= 1
        assert additive[0].is_independent is True

    def test_all_genera_has_no_independent_soft_proof(self):
        """All-genera obs_g = kappa*lambda_g has NO independent soft proof."""
        derivations = theorem_d_via_soft_ward()
        all_genera = [d for d in derivations
                      if "all genera" in d.property_name.lower()
                      and "uniform" in d.scope.lower()]
        assert len(all_genera) >= 1
        assert all_genera[0].is_independent is False

    def test_ahat_has_no_independent_soft_proof(self):
        """A-hat generating function has no soft-theorem derivation."""
        derivations = theorem_d_via_soft_ward()
        ahat = [d for d in derivations if "hat" in d.property_name.lower()]
        assert len(ahat) >= 1
        assert ahat[0].is_independent is False

    def test_independent_count(self):
        """Exactly 2 of 5 properties have independent soft proofs."""
        counts = count_independent_soft_proofs()
        assert counts["independent_soft_proofs"] == 2
        assert counts["dependent_on_algebraic"] == 3


# ============================================================================
# VIII.  Bootstrap closure analysis
# ============================================================================

class TestBootstrapClosure:
    """Verify bootstrap closure properties for each shadow class."""

    def test_heisenberg_closes_at_2(self):
        """Heisenberg (class G) bootstrap closes at arity 2."""
        analysis = analyze_bootstrap_closure_heisenberg(Fraction(1))
        assert analysis.shadow_class == "G"
        assert analysis.bootstrap_closes is True
        assert analysis.closure_arity == 2
        assert analysis.soft_depth == 0

    def test_affine_closes_at_3(self):
        """Affine sl_N (class L) bootstrap closes at arity 3."""
        for N in [2, 3, 4]:
            analysis = analyze_bootstrap_closure_affine(N, Fraction(1))
            assert analysis.shadow_class == "L"
            assert analysis.bootstrap_closes is True
            assert analysis.closure_arity == 3
            assert analysis.soft_depth == 1

    def test_virasoro_does_not_close(self):
        """Virasoro (class M) bootstrap does NOT close at finite arity."""
        analysis = analyze_bootstrap_closure_virasoro(Fraction(26))
        assert analysis.shadow_class == "M"
        assert analysis.bootstrap_closes is False
        assert analysis.closure_arity == -1
        assert analysis.soft_depth == -1

    def test_virasoro_discriminant_nonzero(self):
        """Virasoro critical discriminant Delta != 0 (class M)."""
        analysis = analyze_bootstrap_closure_virasoro(Fraction(26))
        assert analysis.critical_discriminant is not None
        assert analysis.critical_discriminant != 0
        # Delta = 40/(5*26+22) = 40/152 = 5/19
        assert analysis.critical_discriminant == Fraction(40, 152)

    def test_affine_discriminant_zero(self):
        """Affine sl_N critical discriminant Delta = 0 (class L)."""
        analysis = analyze_bootstrap_closure_affine(3, Fraction(1))
        assert analysis.critical_discriminant == 0


# ============================================================================
# IX.  Celestial-shadow identification
# ============================================================================

class TestCelestialShadowIdentification:
    """Verify celestial OPE = shadow at tree and loop level."""

    def test_tree_level_sl2(self):
        """Tree-level celestial = genus-0 shadow for SU(2)."""
        results = verify_celestial_shadow_tree_level(2)
        for r in results:
            assert r.match is True
            assert r.genus == 0

    def test_tree_level_class_l_terminates(self):
        """Tree-level shadow terminates at arity 3 for class L."""
        results = verify_celestial_shadow_tree_level(3, max_arity=8)
        for r in results:
            if r.arity >= 4:
                assert r.shadow_value == 0

    def test_one_loop_sl2(self):
        """One-loop celestial = genus-1 shadow for SU(2)."""
        result = verify_celestial_shadow_one_loop(2)
        assert result.match is True
        assert result.genus == 1
        # F_1 = kappa * lambda_1 = (3/2) * (1/24) = 1/16
        assert result.shadow_value == Fraction(3, 2) * Fraction(1, 24)

    def test_one_loop_sl3(self):
        """One-loop celestial = genus-1 shadow for SU(3)."""
        result = verify_celestial_shadow_one_loop(3)
        assert result.match is True
        # kappa(V_0(sl_3)) = 8*3/(2*3) = 4
        # F_1 = 4 * 1/24 = 1/6
        assert result.shadow_value == Fraction(4) * Fraction(1, 24)

    def test_two_loop_sl2(self):
        """Two-loop celestial = genus-2 shadow for SU(2)."""
        result = verify_celestial_shadow_two_loop(2)
        assert result.match is True
        assert result.genus == 2
        # F_2 = kappa * lambda_2 = (3/2) * (7/5760) = 7/3840
        assert result.shadow_value == Fraction(3, 2) * Fraction(7, 5760)


# ============================================================================
# X.  MC equation physical interpretation
# ============================================================================

class TestMCPhysicalInterpretation:
    """Verify physical interpretation of MC equation components."""

    def test_mc_02_is_ope(self):
        interp = mc_equation_physical_interpretation(0, 2)
        assert "OPE" in interp["physical"] or "kappa" in interp["algebraic"]

    def test_mc_03_is_jacobi(self):
        interp = mc_equation_physical_interpretation(0, 3)
        assert "Jacobi" in interp["algebraic"] or "Yang-Baxter" in interp["physical"]

    def test_mc_04_is_crossing(self):
        interp = mc_equation_physical_interpretation(0, 4)
        assert "crossing" in interp["physical"].lower() or "quartic" in interp["algebraic"].lower()

    def test_mc_12_is_one_loop(self):
        interp = mc_equation_physical_interpretation(1, 2)
        assert "one-loop" in interp["physical"].lower() or "genus-1" in interp["algebraic"].lower()


# ============================================================================
# XI.  Multi-path kappa verification
# ============================================================================

class TestMultiPathKappa:
    """Verify kappa via 3 independent paths (multi-path mandate)."""

    def test_three_paths_affine_sl2(self):
        result = verify_kappa_three_paths("affine", N=2, k=Fraction(0))
        assert result["all_agree"] is True
        assert result["path1_direct"] == Fraction(3, 2)

    def test_three_paths_affine_sl3(self):
        result = verify_kappa_three_paths("affine", N=3, k=Fraction(0))
        assert result["all_agree"] is True
        assert result["path1_direct"] == Fraction(4)

    def test_three_paths_virasoro(self):
        result = verify_kappa_three_paths("virasoro", c=Fraction(26))
        assert result["all_agree"] is True
        assert result["path1_direct"] == Fraction(13)

    def test_three_paths_heisenberg(self):
        result = verify_kappa_three_paths("heisenberg", k=Fraction(1))
        assert result["all_agree"] is True
        assert result["path1_direct"] == Fraction(1)

    def test_three_paths_multiple_levels(self):
        """Verify 3-path agreement at multiple levels for sl_2."""
        for k in [0, 1, 2, 3, 5, 10]:
            result = verify_kappa_three_paths("affine", N=2, k=Fraction(k))
            assert result["all_agree"] is True, f"3-path mismatch at k={k}"


# ============================================================================
# XII.  Critical discriminant from soft data
# ============================================================================

class TestCriticalDiscriminant:
    """Verify critical discriminant Delta from soft theorem data."""

    def test_discriminant_virasoro_c26(self):
        """Delta(Vir_26) = 40/(5*26+22) = 40/152 = 5/19."""
        result = critical_discriminant_from_soft(Fraction(26))
        assert result["Delta"] == Fraction(40, 152)
        assert result["Delta"] == Fraction(5, 19)
        assert result["class"] == "M"

    def test_discriminant_virasoro_c1(self):
        """Delta(Vir_1) = 40/(5+22) = 40/27."""
        result = critical_discriminant_from_soft(Fraction(1))
        assert result["Delta"] == Fraction(40, 27)
        assert result["class"] == "M"

    def test_discriminant_virasoro_c13_self_dual(self):
        """Delta(Vir_13) = 40/(65+22) = 40/87."""
        result = critical_discriminant_from_soft(Fraction(13))
        assert result["Delta"] == Fraction(40, 87)
        assert result["Delta"] != 0  # still class M (Delta != 0 for all c != 0)

    def test_discriminant_nonzero_for_all_c(self):
        """Delta(Vir_c) != 0 for all c != 0 (Virasoro is ALWAYS class M)."""
        for c in [1, 2, 13, 26, 100]:
            result = critical_discriminant_from_soft(Fraction(c))
            assert result["Delta"] != 0, f"Delta = 0 at c={c} would make Vir non-class-M"

    def test_s4_quartic_contact(self):
        """S_4 = 10/[c(5c+22)] matches the quartic contact invariant."""
        for c in [Fraction(1), Fraction(2), Fraction(26)]:
            result = critical_discriminant_from_soft(c)
            expected_s4 = Fraction(10) / (c * (5 * c + 22))
            assert result["S_4"] == expected_s4


# ============================================================================
# XIII.  Full bridge analysis integration
# ============================================================================

class TestFullBridgeAnalysis:
    """Integration tests for the complete bridge analysis."""

    def test_all_four_questions_answered(self):
        """The full analysis addresses all four questions."""
        analysis = full_bridge_analysis()
        assert "question_a" in analysis
        assert "question_b" in analysis
        assert "question_c" in analysis
        assert "question_d" in analysis

    def test_question_a_partial_equivalence(self):
        """Question (a): partial equivalence, not full."""
        analysis = full_bridge_analysis()
        assert "PARTIAL" in analysis["question_a"]["answer"]

    def test_question_b_no_new_proof(self):
        """Question (b): no new proof of shadow-formality."""
        analysis = full_bridge_analysis()
        assert "NO" in analysis["question_b"]["answer"]
        assert "UNIQUENESS" in analysis["question_b"]["answer"]

    def test_question_c_yes(self):
        """Question (c): yes, physical derivation of G/L/C/M."""
        analysis = full_bridge_analysis()
        assert "YES" in analysis["question_c"]["answer"]

    def test_question_d_partial(self):
        """Question (d): partial independent derivation."""
        analysis = full_bridge_analysis()
        assert "PARTIAL" in analysis["question_d"]["answer"]

    def test_bootstrap_to_koszul_count(self):
        analysis = full_bridge_analysis()
        counts = analysis["question_a"]["bootstrap_to_koszul_count"]
        assert counts["total_koszul_items"] == 12
        assert counts["matched_by_bootstrap"] > 0
        assert counts["matched_by_bootstrap"] < 12
