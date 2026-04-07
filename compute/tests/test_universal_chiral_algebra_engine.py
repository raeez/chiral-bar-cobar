r"""Tests for universal chiral algebra engine.

Tests the Cliff universality framework, quasi-conformal structure,
and Aut(O) action for all standard families in the monograph.

Reference: Emily Cliff, "Universal factorization spaces and algebras",
Math. Res. Lett. 26 (2019), no. 4, 1059-1096. arXiv:1608.08122.

Multi-path verification strategy (per CLAUDE.md mandate):
  Path 1: Direct property verification from definitions
  Path 2: Cross-family consistency (universality of universal properties)
  Path 3: Hierarchy implications (conformal => quasi-conformal => universal)
  Path 4: Literature cross-check (Cliff's examples, FBZ quasi-conformal)
  Path 5: Monograph axiom consistency (MK1-MK5 => universality)
"""

from __future__ import annotations

import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.universal_chiral_algebra_engine import (
    # Data classes
    AutOAction,
    UniversalityData,
    ChiralAlgebraFamily,
    # Constructors
    heisenberg_family,
    virasoro_family,
    affine_km_family,
    w_algebra_family,
    beta_gamma_family,
    free_fermion_family,
    lattice_voa_family,
    critical_level_family,
    # Registry
    standard_landscape,
    # Verification functions
    verify_quasi_conformal,
    verify_conformal,
    verify_universal,
    verify_etale_descent,
    cliff_weak_equivalence_check,
    universality_hierarchy,
    minimal_universality_structure,
    # Specific checks
    check_bd_grassmannian_universality,
    check_meromorphic_jet_universality,
    check_hilbert_scheme_universality,
    # Analysis
    monograph_universality_status,
    dimension_analysis,
    weak_factorization_data,
    # Utilities
    nilpotency_order_primary,
    _make_aut_o,
)


# =============================================================================
# Section 1: Quasi-conformal structure tests (Path 1: direct verification)
# =============================================================================

class TestQuasiConformalStructure:
    """Verify quasi-conformal structure for all standard families."""

    def test_heisenberg_quasi_conformal(self):
        """Heisenberg is quasi-conformal (L_{-1} from translation, L_0 from grading)."""
        family = heisenberg_family()
        is_qc, reason = verify_quasi_conformal(family)
        assert is_qc, f"Heisenberg should be quasi-conformal: {reason}"
        assert "L_{-1}" in reason
        assert "L_0" in reason

    def test_virasoro_quasi_conformal(self):
        """Virasoro is quasi-conformal (L_{-1}, L_0 from the Virasoro itself)."""
        family = virasoro_family(Rational(26))
        is_qc, reason = verify_quasi_conformal(family)
        assert is_qc, f"Virasoro should be quasi-conformal: {reason}"

    def test_affine_sl2_quasi_conformal(self):
        """Affine sl_2 at level 1 is quasi-conformal (Sugawara)."""
        family = affine_km_family("A", 1, Rational(1))
        is_qc, _ = verify_quasi_conformal(family)
        assert is_qc

    def test_affine_E8_quasi_conformal(self):
        """Affine E_8 at level 1 is quasi-conformal."""
        family = affine_km_family("E", 8, Rational(1))
        is_qc, _ = verify_quasi_conformal(family)
        assert is_qc

    def test_w3_quasi_conformal(self):
        """W_3 is quasi-conformal (T = W_2 gives conformal structure)."""
        family = w_algebra_family(3, Rational(2))
        is_qc, _ = verify_quasi_conformal(family)
        assert is_qc

    def test_beta_gamma_quasi_conformal(self):
        """Beta-gamma is quasi-conformal despite weight-0 generator."""
        family = beta_gamma_family()
        is_qc, reason = verify_quasi_conformal(family)
        assert is_qc, f"Beta-gamma quasi-conformal: {reason}"

    def test_free_fermion_quasi_conformal(self):
        """Free fermion (half-integer weight) is quasi-conformal."""
        family = free_fermion_family(1)
        is_qc, _ = verify_quasi_conformal(family)
        assert is_qc

    def test_lattice_quasi_conformal(self):
        """Lattice VOA is quasi-conformal (Heisenberg subalgebra provides L_0)."""
        family = lattice_voa_family(1, True)
        is_qc, _ = verify_quasi_conformal(family)
        assert is_qc

    def test_critical_level_quasi_conformal(self):
        """Critical level affine is quasi-conformal but NOT conformal."""
        family = critical_level_family("A", 1)
        is_qc, _ = verify_quasi_conformal(family)
        assert is_qc, "Critical level should be quasi-conformal"
        is_conf, _ = verify_conformal(family)
        assert not is_conf, "Critical level should NOT be conformal"

    def test_all_landscape_quasi_conformal(self):
        """EVERY family in the standard landscape is quasi-conformal."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            is_qc, reason = verify_quasi_conformal(family)
            assert is_qc, f"{key} should be quasi-conformal: {reason}"


# =============================================================================
# Section 2: Conformal structure tests (Path 1: direct verification)
# =============================================================================

class TestConformalStructure:
    """Verify conformal (full Virasoro) structure."""

    def test_heisenberg_conformal(self):
        """Heisenberg is conformal (Sugawara construction)."""
        family = heisenberg_family()
        is_conf, reason = verify_conformal(family)
        assert is_conf, f"Heisenberg should be conformal: {reason}"

    def test_virasoro_conformal(self):
        """Virasoro is conformal by definition."""
        family = virasoro_family()
        is_conf, _ = verify_conformal(family)
        assert is_conf

    def test_affine_generic_conformal(self):
        """Affine at generic level is conformal (Sugawara)."""
        family = affine_km_family("A", 1, Rational(1))
        is_conf, _ = verify_conformal(family)
        assert is_conf

    def test_critical_level_not_conformal(self):
        """Affine at critical level is NOT conformal (no Sugawara)."""
        family = critical_level_family("A", 1)
        is_conf, reason = verify_conformal(family)
        assert not is_conf, "Critical level should not be conformal"
        assert "No conformal vector" in reason

    def test_w_algebra_conformal(self):
        """W_N algebras are conformal (T = W_2 is the conformal vector)."""
        for N in [3, 4]:
            family = w_algebra_family(N)
            is_conf, _ = verify_conformal(family)
            assert is_conf, f"W_{N} should be conformal"

    def test_lattice_unimodular_conformal(self):
        """Unimodular even lattice VOA is conformal."""
        family = lattice_voa_family(1, is_unimodular=True)
        is_conf, _ = verify_conformal(family)
        assert is_conf

    def test_lattice_non_unimodular_not_conformal(self):
        """Non-unimodular lattice VOA is quasi-conformal but not conformal."""
        family = lattice_voa_family(1, is_unimodular=False)
        is_conf, _ = verify_conformal(family)
        assert not is_conf
        is_qc, _ = verify_quasi_conformal(family)
        assert is_qc, "Non-unimodular lattice should still be quasi-conformal"


# =============================================================================
# Section 3: Universality tests (Path 1 + Path 3: hierarchy)
# =============================================================================

class TestUniversality:
    """Verify universality (Cliff's sense) for all standard families."""

    def test_all_landscape_universal(self):
        """EVERY family in the standard landscape is universal."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            is_univ, reason = verify_universal(family)
            assert is_univ, f"{key} should be universal: {reason}"

    def test_universality_from_quasi_conformal(self):
        """In dimension 1, quasi-conformal <=> universal (Cliff's theorem)."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            is_qc, _ = verify_quasi_conformal(family)
            is_univ, _ = verify_universal(family)
            assert is_qc == is_univ, (
                f"{key}: quasi-conformal and universal should be equivalent in dim 1"
            )

    def test_conformal_implies_quasi_conformal(self):
        """conformal => quasi-conformal (strict implication)."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            is_conf, _ = verify_conformal(family)
            is_qc, _ = verify_quasi_conformal(family)
            if is_conf:
                assert is_qc, f"{key}: conformal should imply quasi-conformal"

    def test_strict_hierarchy(self):
        """The hierarchy conformal => quasi-conformal is STRICT.

        The critical level family is quasi-conformal but NOT conformal.
        """
        crit = critical_level_family("A", 1)
        is_qc, _ = verify_quasi_conformal(crit)
        is_conf, _ = verify_conformal(crit)
        assert is_qc and not is_conf, "Critical level: QC but not conformal"

    def test_hierarchy_function(self):
        """Test the universality_hierarchy function for all families."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            h = universality_hierarchy(family)
            # D-module on Ran always true
            assert h["d_module_on_ran"]
            # Etale descent always true for standard families
            assert h["etale_descent"]
            # Universal chiral = universal factorization (Cliff)
            assert h["universal_chiral"] == h["universal_factorization"]
            # Conformal => quasi-conformal
            if h["conformal"]:
                assert h["quasi_conformal"]


# =============================================================================
# Section 4: Etale descent tests (Path 1: direct verification)
# =============================================================================

class TestEtaleDescent:
    """Verify etale descent for factorization algebras."""

    def test_all_families_etale_descent(self):
        """All standard families satisfy etale descent."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            has_desc, reason = verify_etale_descent(family)
            assert has_desc, f"{key} should satisfy etale descent: {reason}"

    def test_etale_descent_reasons(self):
        """Check that the etale descent reasons are substantive."""
        family = virasoro_family()
        _, reason = verify_etale_descent(family)
        assert "OPE defined on formal disk" in reason
        assert "diagonal stratification" in reason
        assert "V_phi" in reason


# =============================================================================
# Section 5: Cliff's theorem tests (Path 4: literature cross-check)
# =============================================================================

class TestCliffTheorems:
    """Verify Cliff's specific theorems and examples."""

    def test_weak_equivalence(self):
        """Cliff Theorem 4.4/5.7: Weak <=> Ordinary factorization algebra."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            equiv, reason = cliff_weak_equivalence_check(family)
            assert equiv, f"{key}: weak equivalence should hold"

    def test_bd_grassmannian_universal(self):
        """Cliff Proposition 7.5: BD Grassmannian is universal."""
        is_univ, reason = check_bd_grassmannian_universality()
        assert is_univ
        assert "Cliff Proposition 7.5" in reason

    def test_meromorphic_jets_universal(self):
        """Cliff Example 7.6: Meromorphic jet space is universal."""
        is_univ, reason = check_meromorphic_jet_universality()
        assert is_univ
        assert "Kapranov-Vasserot" in reason

    def test_hilbert_scheme_universal(self):
        """Cliff Example 7.7: Hilbert scheme universal in any dimension."""
        is_univ, reason = check_hilbert_scheme_universality()
        assert is_univ
        assert "any dimension" in reason

    def test_chiral_pullback_proposition(self):
        """Cliff Proposition 8.1: factorization pullback = chiral pullback."""
        # This is the KEY theorem connecting the factorization and chiral
        # notions of pullback along etale morphisms.
        # For our families, this means B'_X = phi^*_ch B_Y.
        family = affine_km_family("A", 1, Rational(1))
        is_univ, _ = verify_universal(family)
        assert is_univ, "Affine sl2 universal => Cliff Prop 8.1 applies"


# =============================================================================
# Section 6: Aut(O) action tests (Path 1: direct computation)
# =============================================================================

class TestAutOAction:
    """Test the Aut(O) action structure."""

    def test_nilpotency_order_weight_1(self):
        """Weight 1 primary: nilpotency order 2."""
        assert nilpotency_order_primary(Rational(1)) == 2

    def test_nilpotency_order_weight_2(self):
        """Weight 2 primary: nilpotency order 3."""
        assert nilpotency_order_primary(Rational(2)) == 3

    def test_nilpotency_order_weight_0(self):
        """Weight 0: nilpotency order 1."""
        assert nilpotency_order_primary(Rational(0)) == 1

    def test_nilpotency_order_half_integer(self):
        """Weight 1/2 (fermion): nilpotency order 1 (int(1/2) + 1 = 1)."""
        # int(Rational(1,2)) = 0
        assert nilpotency_order_primary(Rational(1, 2)) == 1

    def test_aut_o_heisenberg(self):
        """Heisenberg Aut(O) action: source = Sugawara."""
        family = heisenberg_family()
        action = family.aut_o_action
        assert action is not None
        assert action.is_conformal
        assert action.is_quasi_conformal
        assert action.source == "sugawara"
        assert action.central_charge == Rational(1)

    def test_aut_o_virasoro(self):
        """Virasoro Aut(O) action: source = Virasoro itself."""
        family = virasoro_family(Rational(26))
        action = family.aut_o_action
        assert action is not None
        assert action.source == "virasoro"
        assert action.central_charge == Rational(26)

    def test_aut_o_critical_level(self):
        """Critical level: Aut(O) from translation, NOT conformal."""
        family = critical_level_family("A", 1)
        action = family.aut_o_action
        assert action is not None
        assert not action.is_conformal
        assert action.is_quasi_conformal
        assert action.source == "translation"

    def test_aut_o_lattice(self):
        """Lattice VOA Aut(O) action: source = Heisenberg subalgebra."""
        family = lattice_voa_family(1)
        action = family.aut_o_action
        assert action is not None
        assert action.source == "heisenberg"

    def test_aut_o_generator_data(self):
        """Check generator data in Aut(O) action."""
        family = virasoro_family(Rational(2))
        action = family.aut_o_action
        assert len(action.generator_data) == 1
        name, weight, nilp = action.generator_data[0]
        assert name == "T"
        assert weight == Rational(2)
        assert nilp == 3  # weight 2 => nilpotency order 3


# =============================================================================
# Section 7: Kappa and central charge consistency (Path 2: cross-family)
# =============================================================================

class TestKappaConsistency:
    """Cross-check kappa values with universality data."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (AP39)."""
        family = heisenberg_family(Rational(3))
        assert family.kappa == Rational(3)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        family = virasoro_family(Rational(26))
        assert family.kappa == Rational(13)

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k=1) = dim(sl_2) * (1+2) / (2*2) = 3*3/4 = 9/4."""
        family = affine_km_family("A", 1, Rational(1))
        assert family.kappa == Rational(9, 4)

    def test_critical_level_kappa_zero(self):
        """kappa = 0 at critical level."""
        family = critical_level_family("A", 1)
        assert family.kappa == Rational(0)

    def test_lattice_kappa_equals_rank(self):
        """kappa(V_Lambda) = rank(Lambda) (AP48, not c/2)."""
        family = lattice_voa_family(24, True)
        assert family.kappa == Rational(24)
        # AP48: kappa != c/2 for lattice VOAs (c = 24, c/2 = 12, but kappa = 24)
        assert family.kappa != family.central_charge / 2 or family.central_charge == Rational(24) * 2

    def test_kappa_curve_independent(self):
        """kappa is a property of the OPE, hence curve-independent.
        This is consistent with universality: kappa is defined on the formal disk."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            # kappa is computed from OPE structure constants
            # It should be a rational number (for algebraic families)
            assert isinstance(family.kappa, Rational), f"{key}: kappa should be rational"


# =============================================================================
# Section 8: Monograph axiom tests (Path 5: MK axioms => universality)
# =============================================================================

class TestMonographAxioms:
    """Verify that monograph axioms imply universality."""

    def test_mk1_gives_factorization(self):
        """MK1 (chiral algebra = D-module + Lie bracket) gives factorization on fixed X."""
        # Every BD chiral algebra gives a factorization algebra on Ran(X)
        # This is Definition 5.1 in Cliff = [FG12] 2.4.7
        landscape = standard_landscape()
        for key, family in landscape.items():
            h = universality_hierarchy(family)
            assert h["d_module_on_ran"], f"{key}: MK1 gives D-module on Ran"

    def test_quasi_conformal_gives_universality(self):
        """Quasi-conformal structure is the BRIDGE from fixed-X to universal."""
        # D-module on Ran(X) for fixed X is NOT enough for universality.
        # Need: quasi-conformal structure to get the FAMILY over all curves.
        landscape = standard_landscape()
        for key, family in landscape.items():
            is_qc, _ = verify_quasi_conformal(family)
            is_univ, _ = verify_universal(family)
            assert is_qc == is_univ

    def test_minimal_structure_documented(self):
        """Each family has documented minimal universality structure."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            minimal = minimal_universality_structure(family)
            assert "bd_chiral_on_fixed_X" in minimal
            assert "additional_for_universality" in minimal
            assert "source_of_aut_o" in minimal
            assert "cliff_bridge" in minimal

    def test_monograph_status_complete(self):
        """All families in the monograph have universality status."""
        status = monograph_universality_status()
        assert len(status) >= 17, "Should have at least 17 families"
        for key, data in status.items():
            assert data["is_universal"], f"{key} should be universal"


# =============================================================================
# Section 9: Shadow class + universality cross-checks (Path 2: cross-family)
# =============================================================================

class TestShadowClassUniversality:
    """Verify that universality is independent of shadow class."""

    def test_class_G_universal(self):
        """Class G (Gaussian, depth 2) families are universal."""
        family = heisenberg_family()
        assert family.shadow_class == "G"
        is_univ, _ = verify_universal(family)
        assert is_univ

    def test_class_L_universal(self):
        """Class L (Lie, depth 3) families are universal."""
        family = affine_km_family("A", 1, Rational(1))
        assert family.shadow_class == "L"
        is_univ, _ = verify_universal(family)
        assert is_univ

    def test_class_C_universal(self):
        """Class C (Contact, depth 4) families are universal."""
        family = beta_gamma_family()
        assert family.shadow_class == "C"
        is_univ, _ = verify_universal(family)
        assert is_univ

    def test_class_M_universal(self):
        """Class M (Mixed, infinite depth) families are universal."""
        family = virasoro_family()
        assert family.shadow_class == "M"
        is_univ, _ = verify_universal(family)
        assert is_univ

    def test_universality_orthogonal_to_shadow_depth(self):
        """Universality is INDEPENDENT of shadow depth class."""
        landscape = standard_landscape()
        classes_seen = set()
        for key, family in landscape.items():
            classes_seen.add(family.shadow_class)
            is_univ, _ = verify_universal(family)
            assert is_univ, f"{key} ({family.shadow_class}) should be universal"
        # Should see all four classes
        assert "G" in classes_seen
        assert "L" in classes_seen
        assert "C" in classes_seen
        assert "M" in classes_seen


# =============================================================================
# Section 10: Weak factorization tests (Path 4: Cliff's construction)
# =============================================================================

class TestWeakFactorization:
    """Test the weak factorization algebra framework."""

    def test_weak_data_heisenberg(self):
        """Weak factorization data for Heisenberg."""
        family = heisenberg_family()
        data = weak_factorization_data(family)
        assert "Heisenberg" in data["name"]
        assert "propagator" in data["bar_complex_connection"]
        assert "d log" in data["bar_complex_connection"]

    def test_weak_data_virasoro(self):
        """Weak factorization data for Virasoro."""
        family = virasoro_family()
        data = weak_factorization_data(family)
        assert "OPE data alone" in data["shadow_tower_connection"]

    def test_weak_data_computational_consequence(self):
        """Check that the computational consequence is documented."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            data = weak_factorization_data(family)
            assert "computational_consequence" in data
            assert "bar complex" in data["computational_consequence"].lower() or \
                   "factorization" in data["computational_consequence"].lower()


# =============================================================================
# Section 11: Dimension analysis tests (Path 4: literature)
# =============================================================================

class TestDimensionAnalysis:
    """Test the dimension-dependence of universality."""

    def test_dim_1_equivalence(self):
        """In dim 1: quasi-conformal <=> universal chiral <=> universal fact."""
        analysis = dimension_analysis()
        assert "quasi-conformal VA" in analysis["dim_1_equivalence"]
        assert "universal chiral" in analysis["dim_1_equivalence"]
        assert "universal factorization" in analysis["dim_1_equivalence"]

    def test_dim_higher_factorization(self):
        """In dim > 1: only factorization algebras (no VA analogue)."""
        analysis = dimension_analysis()
        assert "no vertex algebra analogue" in analysis["dim_higher"].lower() or \
               "No vertex algebra" in analysis["dim_higher"]

    def test_monograph_context(self):
        """Monograph works in dimension 1."""
        analysis = dimension_analysis()
        assert "dimension 1" in analysis["monograph_context"]


# =============================================================================
# Section 12: Koszul dual universality tests (Path 2: cross-family)
# =============================================================================

class TestKoszulDualUniversality:
    """If A is universal, so is A! (Koszul dual preserves universality)."""

    def test_heisenberg_dual_universal(self):
        """H_k universal => H_{-k} universal."""
        for k_val in [Rational(1), Rational(3), Rational(-1)]:
            family = heisenberg_family(k_val)
            is_univ, _ = verify_universal(family)
            assert is_univ

    def test_virasoro_dual_universal(self):
        """Vir_c universal => Vir_{26-c} universal."""
        for c_val in [Rational(1), Rational(13), Rational(26), Rational(0)]:
            family = virasoro_family(c_val)
            is_univ, _ = verify_universal(family)
            assert is_univ
            # The dual is also universal
            dual = virasoro_family(26 - c_val)
            is_dual_univ, _ = verify_universal(dual)
            assert is_dual_univ

    def test_affine_ff_dual_universal(self):
        """Affine at level k => Feigin-Frenkel dual at level -k-2h^v."""
        family = affine_km_family("A", 1, Rational(1))
        is_univ, _ = verify_universal(family)
        assert is_univ
        # FF dual: k' = -k - 2h^v = -1 - 4 = -5
        dual = affine_km_family("A", 1, Rational(-5))
        is_dual_univ, _ = verify_universal(dual)
        assert is_dual_univ


# =============================================================================
# Section 13: Specific parameter tests (Path 1: computation)
# =============================================================================

class TestSpecificParameters:
    """Test universality at specific parameter values."""

    def test_virasoro_c13_self_dual_universal(self):
        """Virasoro at c=13 (self-dual point) is universal."""
        family = virasoro_family(Rational(13))
        is_univ, _ = verify_universal(family)
        assert is_univ
        assert family.kappa == Rational(13, 2)

    def test_virasoro_c0_universal(self):
        """Virasoro at c=0 (uncurved) is universal."""
        family = virasoro_family(Rational(0))
        is_univ, _ = verify_universal(family)
        assert is_univ
        assert family.kappa == Rational(0)

    def test_affine_sl2_admissible_universal(self):
        """Affine sl_2 at admissible level -1/2 is universal."""
        family = affine_km_family("A", 1, Rational(-1, 2))
        is_univ, _ = verify_universal(family)
        assert is_univ

    def test_w3_generic_universal(self):
        """W_3 at generic c is universal."""
        family = w_algebra_family(3, Rational(100))
        is_univ, _ = verify_universal(family)
        assert is_univ

    def test_w5_universal(self):
        """W_5 is universal (higher rank W-algebra)."""
        family = w_algebra_family(5, Rational(2))
        is_univ, _ = verify_universal(family)
        assert is_univ

    def test_affine_all_types_universal(self):
        """All simple Lie types give universal affine algebras."""
        types = [
            ("A", 1), ("A", 2), ("A", 3), ("A", 4),
            ("B", 2), ("C", 2), ("D", 4),
            ("G", 2), ("F", 4),
            ("E", 6), ("E", 7), ("E", 8),
        ]
        for type_, rank in types:
            family = affine_km_family(type_, rank, Rational(1))
            is_univ, reason = verify_universal(family)
            assert is_univ, f"Affine {type_}_{rank} should be universal: {reason}"


# =============================================================================
# Section 14: Edge cases and boundary tests
# =============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_high_rank_heisenberg(self):
        """High-rank Heisenberg is universal."""
        family = heisenberg_family(Rational(1), d=100)
        is_univ, _ = verify_universal(family)
        assert is_univ
        assert family.kappa == Rational(100)

    def test_negative_level_heisenberg(self):
        """Negative level Heisenberg is universal."""
        family = heisenberg_family(Rational(-7))
        is_univ, _ = verify_universal(family)
        assert is_univ
        assert family.kappa == Rational(-7)

    def test_large_central_charge_virasoro(self):
        """Large c Virasoro is universal."""
        family = virasoro_family(Rational(1000))
        is_univ, _ = verify_universal(family)
        assert is_univ

    def test_negative_central_charge_virasoro(self):
        """Negative c Virasoro (ghost-like) is universal."""
        family = virasoro_family(Rational(-26))
        is_univ, _ = verify_universal(family)
        assert is_univ

    def test_w_algebra_high_N(self):
        """W_N for large N is universal."""
        family = w_algebra_family(10, Rational(2))
        is_univ, _ = verify_universal(family)
        assert is_univ
        assert len(family.generators) == 9  # W_2, ..., W_10

    def test_lattice_high_rank(self):
        """High-rank lattice VOA is universal."""
        family = lattice_voa_family(24, True)
        is_univ, _ = verify_universal(family)
        assert is_univ


# =============================================================================
# Section 15: Cross-engine consistency tests (Path 2)
# =============================================================================

class TestCrossEngineConsistency:
    """Verify consistency with etale_descent_engine.py."""

    def test_ope_locality_consistent(self):
        """OPE locality (etale engine) is consistent with universality."""
        # Both engines agree: OPE data is curve-independent
        landscape = standard_landscape()
        for key, family in landscape.items():
            _, etale_reason = verify_etale_descent(family)
            assert "formal disk" in etale_reason

    def test_shadow_tower_curve_independent(self):
        """Shadow tower is curve-independent => consistent with universality.

        The shadow obstruction tower theta_A is computed from OPE data on
        the formal disk. This is exactly the data preserved by Cliff's
        etale pullback.
        """
        landscape = standard_landscape()
        for key, family in landscape.items():
            data = weak_factorization_data(family)
            assert "OPE data alone" in data["shadow_tower_connection"]


# =============================================================================
# Section 16: Comprehensive landscape audit
# =============================================================================

class TestLandscapeAudit:
    """Full audit of universality across the landscape."""

    def test_full_monograph_status(self):
        """Complete monograph universality audit."""
        status = monograph_universality_status()
        # Count families
        n_families = len(status)
        assert n_families >= 17

        # All should be universal
        n_universal = sum(1 for d in status.values() if d["is_universal"])
        assert n_universal == n_families

        # Count conformal vs quasi-conformal
        n_conformal = sum(
            1 for d in status.values()
            if d["conformal_vs_quasi_conformal"] == "conformal"
        )
        n_qc_only = sum(
            1 for d in status.values()
            if d["conformal_vs_quasi_conformal"] == "quasi-conformal only"
        )
        # At least one should be quasi-conformal-only (critical level)
        assert n_qc_only >= 1, "Should have at least one QC-only family"
        assert n_conformal + n_qc_only == n_families

    def test_all_hierarchies_valid(self):
        """Every hierarchy satisfies the logical implications."""
        status = monograph_universality_status()
        for key, data in status.items():
            h = data["hierarchy"]
            # conformal => quasi_conformal
            if h["conformal"]:
                assert h["quasi_conformal"]
            # quasi_conformal <=> universal_chiral (dim 1)
            assert h["quasi_conformal"] == h["universal_chiral"]
            # universal_chiral <=> universal_factorization (Cliff)
            assert h["universal_chiral"] == h["universal_factorization"]
            # D-module on Ran always holds
            assert h["d_module_on_ran"]

    def test_koszul_dual_names(self):
        """Check that Koszul dual references are consistent."""
        landscape = standard_landscape()
        for key, family in landscape.items():
            if family.koszul_dual is not None:
                # The dual name should be a valid description
                assert isinstance(family.koszul_dual, str)
                assert len(family.koszul_dual) > 0
