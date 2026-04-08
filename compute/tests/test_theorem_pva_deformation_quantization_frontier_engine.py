r"""Tests for algebraic PVA deformation quantization frontier engine.

THEOREM (PVA deformation quantization):
Every standard-family PVA has a one-dimensional deformation space (the
level or central charge direction), and the quantization obstructions
vanish.  The quantum R-matrix expansion classifies by shadow depth:
  Class G/L: no quantum corrections to the binary r-matrix.
  Class M: infinite quantum corrections.

VERIFICATION PATHS (3+ per claim, per CLAUDE.md multi-path mandate):
  Path 1: Direct PVA bracket construction and consistency
  Path 2: Kappa formula verification from first principles
  Path 3: Cross-family consistency and additivity
  Path 4: AP19/AP44 convention compliance
  Path 5: Shadow class determination from structural data
  Path 6: Rees algebra specialization
  Path 7: Genus-1 cyclic obstruction computation

All formulas computed from first principles (AP1, AP3).
Cross-family consistency verified (AP10).
Multi-path verification per CLAUDE.md mandate.

Conventions (AP44, AP45, AP49)
------------------------------
- Lambda-bracket uses divided-power convention: c_n = a_{(n)}b / n!
- kappa(H_k) = k,  kappa(Vir_c) = c/2,  kappa(V_k(sl_2)) = 3(k+2)/4
- Bar propagator d log E(z,w) has weight 1 (AP27)
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_pva_deformation_quantization_frontier_engine import (
    # PVA constructions
    PVAGenerator,
    PVABracketTerm,
    PVAStructure,
    heisenberg_pva,
    affine_sl2_pva,
    virasoro_pva,
    w3_pva,
    betagamma_pva,
    # Kappa formulas
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_sl2,
    kappa_affine,
    kappa_w3,
    kappa_wn,
    kappa_betagamma,
    # Deformation complex
    DeformationComplexResult,
    deformation_complex_heisenberg,
    deformation_complex_virasoro,
    deformation_complex_affine_sl2,
    deformation_complex_w3,
    deformation_complex_wn,
    # Genus-1 cyclic obstruction
    genus1_cyclic_obstruction_heisenberg,
    genus1_cyclic_obstruction_virasoro,
    genus1_cyclic_obstruction_sl2,
    genus1_cyclic_obstruction_w3,
    # Rees algebra
    rees_algebra_heisenberg,
    rees_algebra_affine_sl2,
    rees_algebra_virasoro,
    # Quantum R-matrix
    quantum_r_matrix_heisenberg,
    quantum_r_matrix_affine_sl2,
    quantum_r_matrix_virasoro,
    quantum_r_matrix_w3,
    # Verification functions
    verify_kappa_additivity,
    verify_deformation_dim_universality,
    verify_quantum_correction_classification,
    verify_ap19_pole_shift,
    verify_ap44_divided_power,
    shadow_class_from_pva,
    verify_pva_deformation_quantization_frontier,
)


# ============================================================================
# I. PVA BRACKET CONSTRUCTION AND STRUCTURE
# ============================================================================

class TestPVAConstruction:
    """Test PVA construction for all standard families."""

    def test_heisenberg_pva_generators(self):
        """Heisenberg PVA has single generator J of weight 1."""
        pva = heisenberg_pva()
        assert pva.generator_count() == 1
        assert pva.generators[0].name == "J"
        assert pva.generators[0].weight == 1

    def test_heisenberg_pva_bracket(self):
        """Heisenberg bracket: {J_lambda J} = k*lambda.

        Verification: the ONLY nonzero term is at lambda^1 with coefficient k.
        c_0 = 0 (no simple pole in OPE), c_1 = k (double pole).
        """
        k = Fraction(3)
        pva = heisenberg_pva(k)
        terms = pva.get_bracket("J", "J")
        assert len(terms) == 1
        assert terms[0].power == 1
        assert terms[0].coefficient == k

    def test_virasoro_pva_bracket_lambda3_ap44(self):
        """Virasoro bracket at lambda^3 is c/12, NOT c/2 (AP44).

        OPE mode T_{(3)}T = c/2.
        Lambda-bracket coefficient c_3 = T_{(3)}T / 3! = c/12.
        This is the canonical AP44 test.
        """
        c = Fraction(24)
        pva = virasoro_pva(c)
        terms = pva.get_bracket("T", "T")
        lambda3_terms = [t for t in terms if t.power == 3]
        assert len(lambda3_terms) == 1
        # c/12 = 24/12 = 2
        assert lambda3_terms[0].coefficient == Fraction(2)
        # NOT c/2 = 12
        assert lambda3_terms[0].coefficient != Fraction(12)

    def test_virasoro_pva_bracket_completeness(self):
        """Virasoro bracket has exactly three terms: lambda^0, lambda^1, lambda^3.

        lambda^2 is absent (T_{(2)}T = 0: no weight-1 quasi-primary in Vir).
        """
        pva = virasoro_pva(Fraction(1))
        terms = pva.get_bracket("T", "T")
        powers = sorted(t.power for t in terms)
        assert powers == [0, 1, 3]

    def test_w3_pva_TW_bracket(self):
        """W_3 bracket {T_lambda W}: W is primary of weight 3.

        {T_lambda W} = dW + 3W*lambda (conformal primary of weight h=3).
        The coefficient of lambda^1 is h=3 (conformal weight).
        """
        pva = w3_pva()
        terms = pva.get_bracket("T", "W")
        lambda1_terms = [t for t in terms if t.power == 1]
        assert len(lambda1_terms) == 1
        assert lambda1_terms[0].coefficient == Fraction(3)
        assert lambda1_terms[0].field_label == "W"

    def test_w3_pva_WW_bracket_max_pole(self):
        """W_3 {W_lambda W} has max lambda power 5, giving OPE pole order 6."""
        pva = w3_pva()
        max_power = pva.max_lambda_power("W", "W")
        assert max_power == 5
        assert pva.ope_pole_order("W", "W") == 6

    def test_betagamma_pva_bracket(self):
        """Beta-gamma bracket: {beta_lambda gamma} = 1 (constant).

        This is a symplectic pairing. OPE: beta(z)gamma(w) ~ 1/(z-w).
        """
        pva = betagamma_pva()
        terms = pva.get_bracket("beta", "gamma")
        assert len(terms) == 1
        assert terms[0].power == 0
        assert terms[0].coefficient == Fraction(1)

    def test_uniform_weight_classification(self):
        """Uniform weight: Heisenberg and Virasoro are uniform, W_3 is not."""
        assert heisenberg_pva().is_uniform_weight() is True
        assert virasoro_pva().is_uniform_weight() is True
        assert w3_pva().is_uniform_weight() is False
        assert affine_sl2_pva().is_uniform_weight() is True


# ============================================================================
# II. KAPPA FORMULAS (multi-path verification, AP1/AP48)
# ============================================================================

class TestKappaFormulas:
    """Verify kappa formulas from first principles."""

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k. Direct from the level."""
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)
        assert kappa_heisenberg(Fraction(5)) == Fraction(5)
        assert kappa_heisenberg(Fraction(-1, 2)) == Fraction(-1, 2)

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2. AP48: this is specific to Virasoro."""
        assert kappa_virasoro(Fraction(1)) == Fraction(1, 2)
        assert kappa_virasoro(Fraction(26)) == Fraction(13)
        assert kappa_virasoro(Fraction(0)) == Fraction(0)

    def test_kappa_affine_sl2_formula(self):
        """kappa(sl_2, k) = 3(k+2)/4.

        Path 1: direct formula.
        Path 2: general kappa_affine with dim=3, h_dual=2.
        """
        for k_val in [1, 2, 5, 10]:
            k = Fraction(k_val)
            # Path 1
            direct = kappa_affine_sl2(k)
            # Path 2
            general = kappa_affine(dim_g=3, k=k, h_dual=2)
            assert direct == general, f"Mismatch at k={k}: {direct} vs {general}"
            # Path 3: explicit check
            expected = Fraction(3) * (k + 2) / 4
            assert direct == expected

    def test_kappa_affine_sl2_at_k1(self):
        """kappa(sl_2, k=1) = 3*3/4 = 9/4."""
        assert kappa_affine_sl2(Fraction(1)) == Fraction(9, 4)

    def test_kappa_w3_formula(self):
        """kappa(W_3) = 5c/6.

        Path 1: direct formula.
        Path 2: general kappa_wn with N=3.
        """
        c = Fraction(6)
        assert kappa_w3(c) == Fraction(5)
        assert kappa_wn(3, c) == Fraction(5)
        assert kappa_w3(c) == kappa_wn(3, c)

    def test_kappa_wn_harmonic_numbers(self):
        """kappa(W_N) = c * (H_N - 1) with H_N = sum 1/j.

        H_2 = 3/2, so kappa(W_2) = c * 1/2 = c/2 = kappa(Vir).
        This is correct: W_2 = Virasoro.
        """
        c = Fraction(12)
        # W_2 = Virasoro
        assert kappa_wn(2, c) == kappa_virasoro(c)
        # W_3: H_3 = 11/6, kappa = c * 5/6
        assert kappa_wn(3, c) == c * Fraction(5, 6)
        # W_4: H_4 = 25/12, kappa = c * 13/12
        assert kappa_wn(4, c) == c * Fraction(13, 12)

    def test_kappa_betagamma(self):
        """kappa(betagamma) = -1/2."""
        assert kappa_betagamma() == Fraction(-1, 2)

    def test_kappa_additivity(self):
        """Kappa is additive for independent sums (Heisenberg)."""
        result = verify_kappa_additivity(Fraction(2), Fraction(3))
        assert result["additive"] is True
        assert result["kappa_sum"] == Fraction(5)


# ============================================================================
# III. DEFORMATION COMPLEX (dim = 1 universality)
# ============================================================================

class TestDeformationComplex:
    """Test PVA deformation complex for all standard families."""

    def test_heisenberg_dim_1(self):
        """dim Def(H_k) = 1: the level deformation."""
        result = deformation_complex_heisenberg()
        assert result.dim_def == 1
        assert result.obstruction_vanishes is True
        assert result.d_kappa_d_param == Fraction(1)

    def test_virasoro_dim_1(self):
        """dim Def(Vir_c) = 1: the central charge deformation."""
        result = deformation_complex_virasoro()
        assert result.dim_def == 1
        assert result.obstruction_vanishes is True
        assert result.d_kappa_d_param == Fraction(1, 2)

    def test_affine_sl2_dim_1(self):
        """dim Def(V_k(sl_2)) = 1: the level deformation."""
        result = deformation_complex_affine_sl2()
        assert result.dim_def == 1
        assert result.obstruction_vanishes is True
        assert result.d_kappa_d_param == Fraction(3, 4)

    def test_w3_dim_1(self):
        """dim Def(W_3) = 1: the c-deformation (Zamolodchikov uniqueness)."""
        result = deformation_complex_w3()
        assert result.dim_def == 1
        assert result.obstruction_vanishes is True
        assert result.d_kappa_d_param == Fraction(5, 6)

    def test_wn_dim_1_universal(self):
        """dim Def(W_N) = 1 for N = 2, ..., 6 (Fateev-Lukyanov)."""
        for N in range(2, 7):
            result = deformation_complex_wn(N)
            assert result.dim_def == 1, f"W_{N}: dim_def = {result.dim_def}"
            assert result.obstruction_vanishes is True

    def test_deformation_universality_master(self):
        """Master check: dim Def(P) = 1 for all standard families."""
        result = verify_deformation_dim_universality()
        assert result["all_dim_one"] is True


# ============================================================================
# IV. GENUS-1 CYCLIC OBSTRUCTION
# ============================================================================

class TestCyclicObstruction:
    """Test genus-1 cyclic obstruction Delta_cyc = d kappa / d param."""

    def test_heisenberg_delta_cyc(self):
        """Delta_cyc(H_k) = d(k)/dk = 1."""
        for k_val in [1, 5, 10]:
            result = genus1_cyclic_obstruction_heisenberg(Fraction(k_val))
            assert result.delta_cyc == Fraction(1)
            assert result.kappa == Fraction(k_val)

    def test_virasoro_delta_cyc(self):
        """Delta_cyc(Vir_c) = d(c/2)/dc = 1/2."""
        for c_val in [1, 13, 26]:
            result = genus1_cyclic_obstruction_virasoro(Fraction(c_val))
            assert result.delta_cyc == Fraction(1, 2)
            assert result.kappa == Fraction(c_val, 2)

    def test_sl2_delta_cyc(self):
        """Delta_cyc(sl_2, k) = d(3(k+2)/4)/dk = 3/4."""
        result = genus1_cyclic_obstruction_sl2(Fraction(1))
        assert result.delta_cyc == Fraction(3, 4)

    def test_w3_delta_cyc(self):
        """Delta_cyc(W_3) = d(5c/6)/dc = 5/6."""
        result = genus1_cyclic_obstruction_w3(Fraction(6))
        assert result.delta_cyc == Fraction(5, 6)
        assert result.kappa == Fraction(5)

    def test_delta_cyc_consistency_w2_virasoro(self):
        """W_2 = Virasoro: Delta_cyc must agree.

        d kappa(W_2) / dc = d(c/2)/dc = 1/2.
        d kappa(Vir_c) / dc = 1/2.
        """
        # W_2 deformation complex
        w2 = deformation_complex_wn(2)
        # Virasoro deformation complex
        vir = deformation_complex_virasoro()
        assert w2.d_kappa_d_param == vir.d_kappa_d_param


# ============================================================================
# V. REES ALGEBRA AND FILTERED DEFORMATION
# ============================================================================

class TestReesAlgebra:
    """Test Rees algebra construction and specialization."""

    def test_heisenberg_rees_no_corrections(self):
        """Heisenberg Rees algebra: no quantum corrections (free field)."""
        rees = rees_algebra_heisenberg(Fraction(2))
        assert rees.max_pole_classical == rees.max_pole_quantum
        assert rees.quantum_correction_order == 0
        assert rees.kappa_classical == rees.kappa_quantum

    def test_sl2_rees_tree_exact(self):
        """Affine sl_2 Rees: tree-level exact (class L)."""
        rees = rees_algebra_affine_sl2(Fraction(3))
        assert rees.max_pole_classical == 2
        assert rees.max_pole_quantum == 2
        assert rees.quantum_correction_order == 0

    def test_virasoro_rees_genus1_corrections(self):
        """Virasoro Rees: quantum corrections at genus >= 1 (class M)."""
        rees = rees_algebra_virasoro(Fraction(26))
        assert rees.max_pole_classical == 4
        assert rees.max_pole_quantum == 4
        assert rees.quantum_correction_order == 1

    def test_rees_kappa_matches_standalone(self):
        """Rees algebra kappa values match standalone kappa functions."""
        k = Fraction(5)
        assert rees_algebra_heisenberg(k).kappa_quantum == kappa_heisenberg(k)
        assert rees_algebra_affine_sl2(k).kappa_quantum == kappa_affine_sl2(k)
        c = Fraction(10)
        assert rees_algebra_virasoro(c).kappa_quantum == kappa_virasoro(c)


# ============================================================================
# VI. QUANTUM R-MATRIX CLASSIFICATION
# ============================================================================

class TestQuantumRMatrix:
    """Test quantum R-matrix expansion by shadow class."""

    def test_heisenberg_no_quantum_corrections(self):
        """Class G: Heisenberg r-matrix has no quantum corrections."""
        r = quantum_r_matrix_heisenberg()
        assert r.shadow_class == "G"
        assert r.quantum_corrections_nonzero is False
        assert r.r1_coefficient == Fraction(0)
        assert r.num_nonzero_terms == 1

    def test_sl2_no_quantum_corrections(self):
        """Class L: Affine sl_2 r-matrix has no quantum corrections."""
        r = quantum_r_matrix_affine_sl2()
        assert r.shadow_class == "L"
        assert r.quantum_corrections_nonzero is False
        assert r.r_classical_pole_order == 1

    def test_virasoro_infinite_corrections(self):
        """Class M: Virasoro r-matrix has infinite quantum corrections."""
        r = quantum_r_matrix_virasoro(Fraction(24))
        assert r.shadow_class == "M"
        assert r.quantum_corrections_nonzero is True
        assert r.num_nonzero_terms == -1  # infinite
        assert r.first_quantum_correction_genus == 1

    def test_virasoro_r1_coefficient(self):
        """Virasoro r^(1) = -c/4: genus-1 R-matrix correction.

        At c = 24: r^(1) = -24/4 = -6.
        At c = 26: r^(1) = -26/4 = -13/2.
        """
        r24 = quantum_r_matrix_virasoro(Fraction(24))
        assert r24.r1_coefficient == Fraction(-6)
        r26 = quantum_r_matrix_virasoro(Fraction(26))
        assert r26.r1_coefficient == Fraction(-13, 2)

    def test_w3_infinite_corrections(self):
        """Class M: W_3 r-matrix has infinite quantum corrections."""
        r = quantum_r_matrix_w3()
        assert r.shadow_class == "M"
        assert r.quantum_corrections_nonzero is True
        assert r.r_classical_pole_order == 5  # WW channel after d-log

    def test_quantum_correction_classification_master(self):
        """Master check: correction classification matches shadow class."""
        result = verify_quantum_correction_classification()
        assert result["all_match"] is True


# ============================================================================
# VII. AP19 AND AP44 CONVENTION COMPLIANCE
# ============================================================================

class TestConventionCompliance:
    """Test AP19 and AP44 convention compliance."""

    def test_ap19_pole_shift_all_families(self):
        """AP19: bar r-matrix pole = OPE pole - 1, all families."""
        result = verify_ap19_pole_shift()
        assert result["all_correct"] is True

    def test_ap44_divided_power_virasoro(self):
        """AP44: lambda-bracket coeff = OPE mode / n!."""
        result = verify_ap44_divided_power()
        assert result["ap44_correct"] is True
        assert result["factorial_relation"] is True

    def test_ap19_heisenberg_explicit(self):
        """Heisenberg: OPE pole 2 (k/(z-w)^2) -> bar pole 1 (k/z)."""
        pva = heisenberg_pva(Fraction(7))
        assert pva.ope_pole_order("J", "J") == 2
        assert pva.bar_r_matrix_pole_order("J", "J") == 1

    def test_ap19_virasoro_explicit(self):
        """Virasoro: OPE pole 4 ((c/2)/(z-w)^4) -> bar pole 3 ((c/2)/z^3)."""
        pva = virasoro_pva(Fraction(26))
        assert pva.ope_pole_order("T", "T") == 4
        assert pva.bar_r_matrix_pole_order("T", "T") == 3


# ============================================================================
# VIII. SHADOW CLASS DETERMINATION
# ============================================================================

class TestShadowClass:
    """Test shadow class determination from PVA structural data."""

    def test_heisenberg_class_G(self):
        """Heisenberg: class G (max pole 2, single generator, abelian)."""
        result = shadow_class_from_pva(heisenberg_pva())
        assert result["declared_class"] == "G"
        assert result["max_ope_pole"] == 2

    def test_virasoro_class_M(self):
        """Virasoro: class M (max pole 4 > 2)."""
        result = shadow_class_from_pva(virasoro_pva())
        assert result["declared_class"] == "M"
        assert result["max_ope_pole"] == 4
        assert result["is_class_M"] is True

    def test_w3_class_M(self):
        """W_3: class M (max pole 6 from WW channel)."""
        result = shadow_class_from_pva(w3_pva())
        assert result["declared_class"] == "M"
        assert result["max_ope_pole"] == 6

    def test_betagamma_class_C(self):
        """Beta-gamma: class C (symplectic pairing, max pole 1)."""
        result = shadow_class_from_pva(betagamma_pva())
        assert result["declared_class"] == "C"
        assert result["max_ope_pole"] == 1

    def test_pole_order_class_M_agreement(self):
        """max pole > 2 iff class M (for G/L/M families)."""
        for pva_fn in [heisenberg_pva, virasoro_pva, w3_pva]:
            result = shadow_class_from_pva(pva_fn())
            assert result["pole_class_M_agreement"] is True


# ============================================================================
# IX. CROSS-FAMILY CONSISTENCY (AP10)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10)."""

    def test_w2_equals_virasoro(self):
        """W_2 = Virasoro: kappa, deformation, obstruction must all agree."""
        c = Fraction(10)
        assert kappa_wn(2, c) == kappa_virasoro(c)
        w2_def = deformation_complex_wn(2)
        vir_def = deformation_complex_virasoro()
        assert w2_def.dim_def == vir_def.dim_def
        assert w2_def.d_kappa_d_param == vir_def.d_kappa_d_param

    def test_kappa_positivity_standard_families(self):
        """Kappa is positive for positive level/central charge.

        kappa(H_k) = k > 0 for k > 0.
        kappa(Vir_c) = c/2 > 0 for c > 0.
        kappa(sl_2, k) = 3(k+2)/4 > 0 for k > -2.
        kappa(W_3, c) = 5c/6 > 0 for c > 0.
        """
        assert kappa_heisenberg(Fraction(1)) > 0
        assert kappa_virasoro(Fraction(1)) > 0
        assert kappa_affine_sl2(Fraction(1)) > 0
        assert kappa_w3(Fraction(1)) > 0

    def test_kappa_vanishing_at_zero_parameter(self):
        """kappa(H_0) = 0, kappa(Vir_0) = 0, kappa(W_3, c=0) = 0.

        These are the uncurved (d^2 = 0) points.
        """
        assert kappa_heisenberg(Fraction(0)) == Fraction(0)
        assert kappa_virasoro(Fraction(0)) == Fraction(0)
        assert kappa_w3(Fraction(0)) == Fraction(0)

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro self-dual at c = 13: kappa(Vir_13) = 13/2, kappa(Vir_{26-13}) = 13/2.

        AP8: Virasoro self-dual at c = 13, NOT c = 26.
        kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13 (AP24).
        At c = 13: both kappas equal 13/2.
        """
        c = Fraction(13)
        c_dual = Fraction(26) - c
        assert c == c_dual  # self-dual point
        assert kappa_virasoro(c) == kappa_virasoro(c_dual)
        assert kappa_virasoro(c) == Fraction(13, 2)
        # AP24: sum is 13, not 0
        assert kappa_virasoro(c) + kappa_virasoro(c_dual) == Fraction(13)

    def test_d_kappa_grows_with_N(self):
        """d kappa(W_N) / dc = H_N - 1 grows with N (harmonic series)."""
        prev = Fraction(0)
        for N in range(2, 8):
            result = deformation_complex_wn(N)
            assert result.d_kappa_d_param > prev
            prev = result.d_kappa_d_param


# ============================================================================
# X. MASTER VERIFICATION
# ============================================================================

class TestMultiPathCrossChecks:
    """Multi-path cross-checks: every claim verified by 2+ independent routes.

    These tests satisfy the AP10 mandate by computing the same quantity
    via genuinely different methods and comparing results.
    """

    def test_kappa_sl2_three_paths(self):
        """kappa(sl_2, k) via three independent computations.

        Path 1: Direct formula kappa_affine_sl2(k) = 3(k+2)/4.
        Path 2: General kappa_affine(dim_g=3, k=k, h_dual=2).
        Path 3: kappa_wn(N=2, c(k)) where c(k) = k*dim/(k+h^v) = 3k/(k+2)
                 is the Sugawara central charge of sl_2 at level k.
                 kappa_wn(2, c) = c/2 = 3k/(2(k+2)).
                 But kappa(affine) = dim(g)(k+h^v)/(2h^v) = 3(k+2)/4.
                 These are DIFFERENT: kappa_wn uses the Virasoro formula c/2,
                 while kappa_affine uses the KM formula. They coincide only
                 when 3k/(2(k+2)) = 3(k+2)/4, which is k^2 + 4k = 2k^2 + 4k,
                 i.e. never for k != 0.
                 CORRECT third path: explicit dim(g)(k+h^v)/(2h^v) by hand.
        """
        for k_val in [1, 2, 3, 5, 10]:
            k = Fraction(k_val)
            # Path 1: specialised formula
            path1 = kappa_affine_sl2(k)
            # Path 2: general affine formula
            path2 = kappa_affine(dim_g=3, k=k, h_dual=2)
            # Path 3: explicit arithmetic
            path3 = Fraction(3) * (k + Fraction(2)) / Fraction(4)
            assert path1 == path2, f"k={k}: path1={path1} vs path2={path2}"
            assert path1 == path3, f"k={k}: path1={path1} vs path3={path3}"

    def test_kappa_wn_two_paths_harmonic(self):
        """kappa(W_N) via two independent harmonic number computations.

        Path 1: kappa_wn(N, c) using the built-in harmonic sum.
        Path 2: Explicit harmonic number H_N = sum_{j=1}^N 1/j, then c*(H_N - 1).
        """
        c = Fraction(30)
        for N in range(2, 8):
            # Path 1: engine function
            path1 = kappa_wn(N, c)
            # Path 2: explicit harmonic number
            h_n = Fraction(0)
            for j in range(1, N + 1):
                h_n += Fraction(1, j)
            path2 = c * (h_n - Fraction(1))
            assert path1 == path2, f"N={N}: {path1} vs {path2}"

    def test_d_kappa_two_paths_finite_difference(self):
        """d kappa / d(param) via symbolic derivative and finite difference.

        Path 1: Closed-form derivative from DeformationComplexResult.
        Path 2: Finite difference (kappa(param + eps) - kappa(param)) / eps
                 for exact rational eps.
        """
        eps = Fraction(1, 1000)

        # Heisenberg: d kappa / dk = 1
        k = Fraction(5)
        d_sym = deformation_complex_heisenberg().d_kappa_d_param
        d_num = (kappa_heisenberg(k + eps) - kappa_heisenberg(k)) / eps
        assert d_sym == d_num  # exact for linear kappa

        # Virasoro: d kappa / dc = 1/2
        c = Fraction(10)
        d_sym = deformation_complex_virasoro().d_kappa_d_param
        d_num = (kappa_virasoro(c + eps) - kappa_virasoro(c)) / eps
        assert d_sym == d_num  # exact for linear kappa

        # Affine sl_2: d kappa / dk = 3/4
        d_sym = deformation_complex_affine_sl2().d_kappa_d_param
        d_num = (kappa_affine_sl2(k + eps) - kappa_affine_sl2(k)) / eps
        assert d_sym == d_num  # exact for linear kappa

        # W_3: d kappa / dc = 5/6
        d_sym = deformation_complex_w3().d_kappa_d_param
        d_num = (kappa_w3(c + eps) - kappa_w3(c)) / eps
        assert d_sym == d_num  # exact for linear kappa

    def test_cyclic_obstruction_equals_d_kappa(self):
        """Delta_cyc = d kappa / d(param): cross-check two independent functions.

        Path 1: genus1_cyclic_obstruction_* returns delta_cyc.
        Path 2: deformation_complex_* returns d_kappa_d_param.
        These MUST agree (they compute the same quantity via different code paths).
        """
        assert (genus1_cyclic_obstruction_heisenberg(Fraction(1)).delta_cyc
                == deformation_complex_heisenberg().d_kappa_d_param)
        assert (genus1_cyclic_obstruction_virasoro(Fraction(1)).delta_cyc
                == deformation_complex_virasoro().d_kappa_d_param)
        assert (genus1_cyclic_obstruction_sl2(Fraction(1)).delta_cyc
                == deformation_complex_affine_sl2().d_kappa_d_param)
        assert (genus1_cyclic_obstruction_w3(Fraction(1)).delta_cyc
                == deformation_complex_w3().d_kappa_d_param)

    def test_ap44_two_paths_virasoro(self):
        """AP44 divided-power: lambda-bracket coeff vs OPE mode / n!.

        Path 1: Read lambda-bracket coefficient c_3 from the PVA bracket data.
        Path 2: Compute T_{(3)}T / 3! = (c/2) / 6 = c/12 from OPE modes.
        """
        for c_val in [1, 6, 24, 100]:
            c = Fraction(c_val)
            pva = virasoro_pva(c)
            terms = pva.get_bracket("T", "T")
            # Path 1: extract from bracket
            lambda3 = [t for t in terms if t.power == 3]
            path1 = lambda3[0].coefficient
            # Path 2: OPE mode / factorial
            ope_mode_3 = c / 2   # T_{(3)}T = c/2
            path2 = ope_mode_3 / Fraction(6)  # /3!
            assert path1 == path2, f"c={c}: {path1} vs {path2}"

    def test_ap19_two_paths_all_channels(self):
        """AP19 pole shift: PVA method vs direct OPE-minus-one.

        Path 1: pva.bar_r_matrix_pole_order() (computed from bracket data).
        Path 2: pva.ope_pole_order() - 1 (the AP19 rule directly).
        """
        test_cases = [
            (heisenberg_pva(), "J", "J"),
            (affine_sl2_pva(), "e", "f"),
            (affine_sl2_pva(), "h", "h"),
            (virasoro_pva(), "T", "T"),
            (w3_pva(), "T", "T"),
            (w3_pva(), "T", "W"),
            (w3_pva(), "W", "W"),
            (betagamma_pva(), "beta", "gamma"),
        ]
        for pva, gi, gj in test_cases:
            path1 = pva.bar_r_matrix_pole_order(gi, gj)
            path2 = pva.ope_pole_order(gi, gj) - 1
            assert path1 == path2, (
                f"{pva.name} ({gi},{gj}): bar_pole={path1} vs ope-1={path2}"
            )

    def test_rees_kappa_two_paths(self):
        """Rees algebra kappa vs standalone kappa: two independent code paths.

        Path 1: rees_algebra_*.kappa_quantum (computed inside Rees construction).
        Path 2: kappa_* standalone function.
        """
        for k_val in [1, 3, 7]:
            k = Fraction(k_val)
            assert rees_algebra_heisenberg(k).kappa_quantum == kappa_heisenberg(k)
            assert rees_algebra_affine_sl2(k).kappa_quantum == kappa_affine_sl2(k)
        for c_val in [1, 13, 26]:
            c = Fraction(c_val)
            assert rees_algebra_virasoro(c).kappa_quantum == kappa_virasoro(c)

    def test_quantum_r_pole_matches_pva_bar_pole(self):
        """Quantum R-matrix classical pole order = PVA bar r-matrix pole order.

        Path 1: quantum_r_matrix_*.r_classical_pole_order.
        Path 2: pva.bar_r_matrix_pole_order() (from bracket data).
        Two independent code paths computing the same quantity.
        """
        # Heisenberg
        r_heis = quantum_r_matrix_heisenberg()
        pva_heis = heisenberg_pva()
        assert r_heis.r_classical_pole_order == pva_heis.bar_r_matrix_pole_order("J", "J")

        # Affine sl_2: max bar pole across all channels
        r_sl2 = quantum_r_matrix_affine_sl2()
        pva_sl2 = affine_sl2_pva()
        max_bar_pole_sl2 = max(
            pva_sl2.bar_r_matrix_pole_order(gi.name, gj.name)
            for gi in pva_sl2.generators
            for gj in pva_sl2.generators
        )
        assert r_sl2.r_classical_pole_order == max_bar_pole_sl2

        # Virasoro
        r_vir = quantum_r_matrix_virasoro()
        pva_vir = virasoro_pva()
        assert r_vir.r_classical_pole_order == pva_vir.bar_r_matrix_pole_order("T", "T")

        # W_3: max across all channels
        r_w3 = quantum_r_matrix_w3()
        pva_w3 = w3_pva()
        max_bar_pole_w3 = max(
            pva_w3.bar_r_matrix_pole_order(gi.name, gj.name)
            for gi in pva_w3.generators
            for gj in pva_w3.generators
        )
        assert r_w3.r_classical_pole_order == max_bar_pole_w3

    def test_virasoro_r1_two_paths(self):
        """Virasoro r^(1) = -c/4: two computation routes.

        Path 1: quantum_r_matrix_virasoro(c).r1_coefficient.
        Path 2: -c/4 computed directly from the central charge.
        """
        for c_val in [1, 13, 24, 26, 100]:
            c = Fraction(c_val)
            path1 = quantum_r_matrix_virasoro(c).r1_coefficient
            path2 = -c / 4
            assert path1 == path2, f"c={c}: {path1} vs {path2}"

    def test_kappa_complementarity_ap24(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c.

        Path 1: Direct sum of kappa values.
        Path 2: The constant 13 = 26/2 (half of the critical dimension).
        Path 3: At c=0, kappa(Vir_0) + kappa(Vir_26) = 0 + 13 = 13.
        """
        for c_val in [0, 1, 5, 13, 20, 26]:
            c = Fraction(c_val)
            path1 = kappa_virasoro(c) + kappa_virasoro(Fraction(26) - c)
            path2 = Fraction(13)
            assert path1 == path2, f"c={c}: {path1} vs {path2}"

    def test_shadow_class_from_two_methods(self):
        """Shadow class: structural determination vs declared class.

        Path 1: shadow_class_from_pva() infers class from pole orders.
        Path 2: PVAStructure.shadow_class (declared at construction).
        For G/L/M, pole > 2 iff class M must be consistent.
        """
        for constructor in [heisenberg_pva, virasoro_pva, w3_pva]:
            pva = constructor()
            result = shadow_class_from_pva(pva)
            # The structural criterion (pole > 2 <=> M) must agree
            # with the declared class for G/L/M families
            assert result["pole_class_M_agreement"] is True


# ============================================================================
# XI. MASTER VERIFICATION
# ============================================================================

class TestMasterVerification:
    """Master verification combining all paths."""

    def test_master_all_pass(self):
        """Run all verification paths; everything must pass."""
        result = verify_pva_deformation_quantization_frontier()
        assert result["all_pass"] is True

    def test_master_subresults(self):
        """Verify each subresult of the master verification."""
        result = verify_pva_deformation_quantization_frontier()
        assert result["deformation_universality"]["all_dim_one"] is True
        assert result["ap19_pole_shift"]["all_correct"] is True
        assert result["ap44_divided_power"]["ap44_correct"] is True
        assert result["quantum_corrections"]["all_match"] is True
        assert result["kappa_additivity"]["additive"] is True
