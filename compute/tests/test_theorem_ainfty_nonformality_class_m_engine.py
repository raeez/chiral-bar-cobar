r"""Tests for A-infinity non-formality of class M algebras (Virasoro, W_N).

Verifies thm:dnp-bar-cobar-identification(iii): the non-renormalization =
Koszulness correspondence.

KEY MATHEMATICAL CONTENT:
  1. Class M algebras (Virasoro, W_N) have m_k^{SC} != 0 for ALL k >= 3.
  2. Class L algebras (affine KM) have m_k^{SC} = 0 for k >= 4 (depth 3).
  3. Class G algebras (Heisenberg) have m_k^{SC} = 0 for k >= 3 (depth 2).
  4. Class C algebras (betagamma) have m_3 = 0, m_4 != 0, m_k = 0 for k >= 5.
  5. ALL standard families are Koszul (bar A-infinity formal), despite varying
     Swiss-cheese non-formality depth. This is the AP14 distinction.

MULTI-PATH VERIFICATION:
  Path A: Direct mode-sum computation of ell_3, ell_4.
  Path B: Algebraic formula verification (S_3 = 2, S_4 = -(5c+22)/(10c)).
  Path C: Cross-family consistency (G < L < C < M ordering).
  Path D: OPE pole-order analysis (heuristic -> shadow depth).
  Path E: Critical discriminant (Delta = 0 <=> tower terminates).
  Path F: Physical interpretation (loop exactness order).

References:
  thm:dnp-bar-cobar-identification (chiral_koszul_pairs.tex)
  thm:koszul-equivalences-meta item (iii)
  prop:shadow-formality-low-arity (higher_genus_modular_koszul.tex)
  thm:ds-koszul-obstruction (chiral_koszul_pairs.tex)
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_ainfty_nonformality_class_m_engine import (
    SHADOW_CLASSES,
    classify_shadow_class,
    virasoro_killing_form,
    virasoro_propagator,
    virasoro_bracket,
    virasoro_ope_coefficients,
    virasoro_S3_ope_ratio,
    affine_sl2_killing_form,
    affine_sl2_propagator,
    heisenberg_killing_form,
    heisenberg_propagator,
    swiss_cheese_m3_virasoro,
    swiss_cheese_m3_heisenberg,
    swiss_cheese_m3_affine_sl2,
    swiss_cheese_m4_betagamma,
    virasoro_quartic_shadow,
    virasoro_quintic_shadow,
    nonformality_depth,
    koszulness_nonformality_dictionary,
    linfty_ell3_virasoro_mode_sum,
    linfty_ell3_heisenberg,
    linfty_ell4_virasoro_exact,
    loop_exactness_order,
    shadow_depth_from_ope,
    shadow_tower_terminates,
    w3_shadow_data,
    nonformality_summary,
    F,
)


# ============================================================================
# Test 1-5: Shadow class classification
# ============================================================================

class TestShadowClassification:
    """Verify shadow class G/L/C/M classification."""

    def test_classify_G(self):
        """Shadow depth 2 -> class G (Gaussian)."""
        assert classify_shadow_class(2) == "G"

    def test_classify_L(self):
        """Shadow depth 3 -> class L (Lie/tree)."""
        assert classify_shadow_class(3) == "L"

    def test_classify_C(self):
        """Shadow depth 4 -> class C (contact/quartic)."""
        assert classify_shadow_class(4) == "C"

    def test_classify_M(self):
        """Shadow depth >= 5 -> class M (mixed/infinite)."""
        assert classify_shadow_class(5) == "M"
        assert classify_shadow_class(100) == "M"

    def test_all_four_classes_defined(self):
        """All four shadow classes are present in the dictionary."""
        assert set(SHADOW_CLASSES.keys()) == {"G", "L", "C", "M"}


# ============================================================================
# Test 6-10: Virasoro OPE data
# ============================================================================

class TestVirasoroOPE:
    """Verify Virasoro Killing form, propagator, and bracket."""

    def test_killing_form_m2(self):
        """eta(L_2, L_{-2}) = (c/12) * 2 * (4-1) = c/2."""
        c = F(26)
        eta = virasoro_killing_form(2, c)
        assert eta == c / F(2), f"eta(L_2, L_{{-2}}) = {eta}, expected {c/F(2)}"

    def test_killing_form_m3(self):
        """eta(L_3, L_{-3}) = (c/12) * 3 * (9-1) = 2c."""
        c = F(12)
        eta = virasoro_killing_form(3, c)
        assert eta == F(2) * c, f"eta(L_3, L_{{-3}}) = {eta}, expected {F(2)*c}"

    def test_killing_form_m1_vanishes(self):
        """eta(L_1, L_{-1}) = (c/12) * 1 * 0 = 0 (m^2 - 1 = 0 at m=1)."""
        eta = virasoro_killing_form(1, F(26))
        assert eta == F(0)

    def test_propagator_m2(self):
        """P(2) = 1/eta(L_2, L_{-2}) = 2/c."""
        c = F(26)
        P = virasoro_propagator(2, c)
        assert P == F(2) / c

    def test_propagator_m0_none(self):
        """P(0) = None (eta vanishes at m=0)."""
        assert virasoro_propagator(0, F(26)) is None


# ============================================================================
# Test 11-15: Swiss-cheese m_3 for Virasoro (CLASS M: NONZERO)
# ============================================================================

class TestSwissCheeseVirasoroM3:
    """Verify m_3^{SC} != 0 for Virasoro (class M).

    This is the CORE VERIFICATION of non-formality for class M.
    S_3 = 2 (c-independent) is the cubic shadow coefficient.
    """

    def test_m3_SC_nonzero_c26(self):
        """m_3^{SC} != 0 for Virasoro at c=26."""
        data = swiss_cheese_m3_virasoro(F(26))
        assert data["m3_SC_nonzero"] is True
        assert data["class"] == "M"

    def test_S3_equals_2_c26(self):
        """S_3 = 2 for Virasoro at c=26 (algebraic formula)."""
        data = swiss_cheese_m3_virasoro(F(26))
        assert data["S3_algebraic"] == F(2)

    def test_S3_c_independent(self):
        """S_3 = 2 is c-independent: same for c=1, c=26, c=100."""
        for c_val in [F(1), F(26), F(100), F(1, 2)]:
            data = swiss_cheese_m3_virasoro(c_val)
            assert data["S3_algebraic"] == F(2), f"S_3 != 2 at c={c_val}"

    def test_virasoro_shadow_depth_infinite(self):
        """Virasoro has infinite shadow depth (class M)."""
        data = swiss_cheese_m3_virasoro(F(26))
        assert data["shadow_depth"] == float("inf")

    def test_S3_ope_ratio_equals_2(self):
        """OPE coefficient ratio gives S_3 = 2 exactly."""
        data = swiss_cheese_m3_virasoro(F(26))
        assert data["S3_ope_ratio"] == F(2), f"OPE ratio = {data['S3_ope_ratio']}"

    def test_S3_methods_agree(self):
        """OPE ratio and shadow GF methods agree on S_3 = 2."""
        data = swiss_cheese_m3_virasoro(F(26))
        assert data["methods_agree"] is True


# ============================================================================
# Test 16-18: Swiss-cheese m_3 for Heisenberg (CLASS G: ZERO)
# ============================================================================

class TestSwissCheeseHeisenbergM3:
    """Verify m_3^{SC} = 0 for Heisenberg (class G).

    Heisenberg bracket is central: [a_m, a_n] = k m delta_{m+n,0}.
    Nested brackets vanish: [[a_m, a_n], a_p] = 0.
    """

    def test_m3_SC_zero(self):
        """m_3^{SC} = 0 for Heisenberg."""
        data = swiss_cheese_m3_heisenberg(F(1))
        assert data["m3_SC_zero"] is True
        assert data["m3_SC_value"] == F(0)

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (shadow depth 2)."""
        data = swiss_cheese_m3_heisenberg(F(1))
        assert data["class"] == "G"
        assert data["shadow_depth"] == 2

    def test_m4_SC_also_zero(self):
        """m_4^{SC} = 0 for Heisenberg (all higher ops vanish)."""
        data = swiss_cheese_m3_heisenberg(F(1))
        assert data["m4_SC_zero"] is True


# ============================================================================
# Test 19-21: Swiss-cheese for affine sl_2 (CLASS L: depth 3)
# ============================================================================

class TestSwissCheeseAffineSl2:
    """Verify affine sl_2 is class L (shadow depth 3)."""

    def test_class_L(self):
        """Affine sl_2 at level k=1 is class L."""
        data = swiss_cheese_m3_affine_sl2(F(1))
        assert data["class"] == "L"
        assert data["shadow_depth"] == 3

    def test_S3_affine_sl2(self):
        """S_3(sl_2, k=1) = 4/(k+2) = 4/3."""
        data = swiss_cheese_m3_affine_sl2(F(1))
        expected_S3 = F(4) / F(3)
        assert data["S3"] == expected_S3, f"S_3 = {data['S3']}, expected {expected_S3}"

    def test_S4_vanishes(self):
        """S_4 = 0 for affine sl_2 (tower terminates at depth 3)."""
        data = swiss_cheese_m3_affine_sl2(F(1))
        assert data["S4"] == F(0)


# ============================================================================
# Test 22-23: Swiss-cheese for betagamma (CLASS C: depth 4)
# ============================================================================

class TestSwissCheeseBetagamma:
    """Verify betagamma is class C (shadow depth 4)."""

    def test_class_C(self):
        """Betagamma is class C (shadow depth 4)."""
        data = swiss_cheese_m4_betagamma()
        assert data["class"] == "C"
        assert data["shadow_depth"] == 4

    def test_m3_zero_m4_nonzero(self):
        """Betagamma: m_3^{SC} = 0, m_4^{SC} != 0 (quartic contact)."""
        data = swiss_cheese_m4_betagamma()
        assert data["m3_SC_zero"] is True
        assert data["m4_SC_nonzero"] is True


# ============================================================================
# Test 24-28: Quartic shadow S_4 for Virasoro
# ============================================================================

class TestVirasoroQuarticShadow:
    """Verify S_4 = -(5c+22)/(10c) and Q^{contact} = 10/[c(5c+22)]."""

    def test_S4_formula_c26(self):
        """S_4(c=26) = -(5*26+22)/(10*26) = -152/260 = -19/32.5 = ... exact check."""
        data = virasoro_quartic_shadow(F(26))
        expected = -(F(5) * F(26) + F(22)) / (F(10) * F(26))
        assert data["S4"] == expected

    def test_Q_contact_c26(self):
        """Q^{contact}(c=26) = 10/(26 * (5*26+22)) = 10/(26*152)."""
        data = virasoro_quartic_shadow(F(26))
        expected = F(10) / (F(26) * F(152))
        assert data["Q_contact"] == expected

    def test_S4_c_dependent(self):
        """S_4 IS c-dependent (unlike S_3)."""
        S4_1 = virasoro_quartic_shadow(F(1))["S4"]
        S4_26 = virasoro_quartic_shadow(F(26))["S4"]
        assert S4_1 != S4_26, "S_4 should be c-dependent"

    def test_Delta_nonzero_generic(self):
        """Delta != 0 for generic c (confirming class M, infinite tower)."""
        for c_val in [F(1), F(26), F(100), F(1, 2)]:
            data = virasoro_quartic_shadow(c_val)
            assert data["Delta"] != F(0), f"Delta = 0 at c={c_val}, unexpected"
            assert data["tower_infinite"] is True

    def test_Delta_zero_at_c_minus_22_over_5(self):
        """Delta = 0 at c = -22/5 (degenerate minimal model, tower truncates)."""
        data = virasoro_quartic_shadow(F(-22, 5))
        assert data["Delta"] == F(0), "Delta should vanish at c=-22/5"


# ============================================================================
# Test 29-31: Quintic shadow S_5 (class M infinite tower witness)
# ============================================================================

class TestVirasoroQuinticShadow:
    """Verify S_5 = -48/(c^2(5c+22))."""

    def test_S5_formula_c26(self):
        """S_5(c=26) = -48/(26^2 * 152)."""
        data = virasoro_quintic_shadow(F(26))
        expected = F(-48) / (F(26) * F(26) * F(152))
        assert data["S5"] == expected

    def test_S5_nonzero_generic(self):
        """S_5 != 0 for generic c (infinite tower persists beyond arity 4)."""
        for c_val in [F(1), F(26), F(100)]:
            data = virasoro_quintic_shadow(c_val)
            assert data["S5_nonzero"] is True, f"S_5 = 0 at c={c_val}"

    def test_S5_c_dependent(self):
        """S_5 is c-dependent."""
        S5_1 = virasoro_quintic_shadow(F(1))["S5"]
        S5_26 = virasoro_quintic_shadow(F(26))["S5"]
        assert S5_1 != S5_26


# ============================================================================
# Test 32-36: L-infinity ell_3 mode sum
# ============================================================================

class TestLinftyEll3:
    """Verify L-infinity bracket ell_3 on the convolution algebra."""

    def test_ell3_virasoro_nonzero_c26(self):
        """ell_3 is nonzero for Virasoro at c=26 (class M)."""
        data = linfty_ell3_virasoro_mode_sum(F(26))
        assert data["ell3_nonzero"] is True

    def test_ell3_virasoro_S3_ope_ratio_exact(self):
        """OPE ratio method gives S_3 = 2 exactly for c=26."""
        data = linfty_ell3_virasoro_mode_sum(F(26))
        assert data["S3_ope_ratio"] == F(2)

    def test_ell3_heisenberg_zero(self):
        """ell_3 = 0 for Heisenberg (central bracket)."""
        data = linfty_ell3_heisenberg(F(1))
        assert data["ell3_zero"] is True
        assert data["S3"] == F(0)

    def test_ell3_exact_value(self):
        """S_3 = 2 is the exact algebraic result for Virasoro."""
        data = linfty_ell3_virasoro_mode_sum(F(26))
        assert data["S3_exact"] == F(2)

    def test_ell3_virasoro_c_independence(self):
        """S_3 = 2 is c-independent: verified at multiple c values."""
        data = linfty_ell3_virasoro_mode_sum(F(26))
        assert data["S3_c_independent"] is True

    def test_ell3_shadow_gf_consistent(self):
        """Shadow generating function consistency check passes."""
        data = linfty_ell3_virasoro_mode_sum(F(26))
        assert data["shadow_gf_consistent"] is True


# ============================================================================
# Test 37-40: Koszulness vs non-formality dictionary
# ============================================================================

class TestKoszulnessNonformalityDictionary:
    """Verify the Koszulness <-> non-formality dictionary (AP14 distinction)."""

    def test_all_standard_families_koszul(self):
        """ALL standard families are Koszul (bar A-infinity formal)."""
        d = koszulness_nonformality_dictionary()
        for name, info in d.items():
            assert info["koszul"] is True, f"{name} should be Koszul"
            assert info["bar_ainfty_formal"] is True, f"{name} bar A-inf should be formal"

    def test_class_M_swiss_cheese_nonformal(self):
        """Class M families (Virasoro, W_3) are Swiss-cheese NON-formal."""
        d = koszulness_nonformality_dictionary()
        assert d["Virasoro"]["swiss_cheese_formal"] is False
        assert d["W_3"]["swiss_cheese_formal"] is False

    def test_class_G_swiss_cheese_formal(self):
        """Heisenberg (class G) is Swiss-cheese formal."""
        d = koszulness_nonformality_dictionary()
        assert d["Heisenberg"]["swiss_cheese_formal"] is True

    def test_shadow_depth_ordering(self):
        """Shadow depth ordering: G(2) < L(3) < C(4) < M(inf)."""
        d = koszulness_nonformality_dictionary()
        assert d["Heisenberg"]["shadow_depth"] == 2
        assert d["affine_sl2"]["shadow_depth"] == 3
        assert d["betagamma"]["shadow_depth"] == 4
        assert d["Virasoro"]["shadow_depth"] == float("inf")


# ============================================================================
# Test 41-44: Loop exactness order (physical interpretation)
# ============================================================================

class TestLoopExactness:
    """Verify loop exactness order for line-operator OPE."""

    def test_heisenberg_tree_level(self):
        """Heisenberg: tree-level exact (0 loops)."""
        data = loop_exactness_order("Heisenberg")
        assert data["loop_exact_order"] == 0

    def test_affine_1loop(self):
        """Affine KM: 1-loop exact."""
        data = loop_exactness_order("affine_sl2")
        assert data["loop_exact_order"] == 1

    def test_betagamma_2loop(self):
        """Betagamma: 2-loop exact (m_3=0, m_4!=0)."""
        data = loop_exactness_order("betagamma")
        assert data["loop_exact_order"] == 2

    def test_virasoro_all_loop(self):
        """Virasoro: all-loop (no finite truncation suffices)."""
        data = loop_exactness_order("Virasoro")
        assert data["loop_exact_order"] == float("inf")


# ============================================================================
# Test 45-48: OPE pole structure -> shadow depth
# ============================================================================

class TestOPEPoleStructure:
    """Verify OPE pole order -> shadow depth heuristic."""

    def test_simple_pole_class_G(self):
        """Simple pole (order 1) -> depth 2 (class G, Heisenberg)."""
        assert shadow_depth_from_ope(1) == 2

    def test_double_pole_class_L(self):
        """Double pole (order 2) -> depth 3 (class L, affine KM)."""
        assert shadow_depth_from_ope(2) == 3

    def test_triple_pole_class_C(self):
        """Triple pole (order 3) -> depth 4 (class C)."""
        assert shadow_depth_from_ope(3) == 4

    def test_quartic_pole_class_M(self):
        """Quartic pole (order 4) -> depth infinity (class M, Virasoro)."""
        # Convention: -1 means infinity
        assert shadow_depth_from_ope(4) == -1


# ============================================================================
# Test 49-52: Shadow tower termination
# ============================================================================

class TestShadowTowerTermination:
    """Verify shadow tower termination criteria."""

    def test_heisenberg_terminates(self):
        """Heisenberg tower terminates at depth 2."""
        data = shadow_tower_terminates("Heisenberg")
        assert data["terminates"] is True
        assert data["depth"] == 2

    def test_virasoro_generic_infinite(self):
        """Virasoro at generic c has infinite tower."""
        data = shadow_tower_terminates("Virasoro", c=F(26))
        assert data["terminates"] is False
        assert data["depth"] == float("inf")

    def test_virasoro_degenerate_terminates(self):
        """Virasoro at c=-22/5 has Delta=0, tower terminates."""
        data = shadow_tower_terminates("Virasoro", c=F(-22, 5))
        assert data["terminates"] is True

    def test_affine_terminates(self):
        """Affine sl_2 tower terminates at depth 3."""
        data = shadow_tower_terminates("affine_sl2")
        assert data["terminates"] is True
        assert data["depth"] == 3


# ============================================================================
# Test 53-55: W_3 shadow data
# ============================================================================

class TestW3ShadowData:
    """Verify W_3 shadow data."""

    def test_w3_class_M(self):
        """W_3 is class M (shadow depth infinity)."""
        data = w3_shadow_data(F(26))
        assert data["class"] == "M"
        assert data["shadow_depth"] == float("inf")

    def test_w3_kappa(self):
        """kappa(W_3, c=26) = c/2 = 13."""
        data = w3_shadow_data(F(26))
        assert data["kappa"] == F(13)

    def test_w3_multi_generator(self):
        """W_3 is multi-generator (T and W)."""
        data = w3_shadow_data(F(26))
        assert data["multi_generator"] is True


# ============================================================================
# Test 56-60: Nonformality depth across families
# ============================================================================

class TestNonformalityDepth:
    """Verify nonformality depth computation across all families."""

    def test_heisenberg_formal(self):
        """Heisenberg: d_NF = infinity (fully formal)."""
        data = nonformality_depth("Heisenberg")
        assert data["d_NF"] == float("inf")
        assert data["is_formal"] is True

    def test_virasoro_d_NF_3(self):
        """Virasoro: d_NF = 3 (first nonzero Swiss-cheese operation at k=3)."""
        data = nonformality_depth("Virasoro", c=F(26))
        assert data["d_NF"] == 3
        assert data["is_formal"] is False

    def test_betagamma_d_NF_4(self):
        """Betagamma: d_NF = 4 (m_3=0, m_4!=0)."""
        data = nonformality_depth("betagamma")
        assert data["d_NF"] == 4
        assert data["is_formal"] is False

    def test_w3_d_NF_3(self):
        """W_3: d_NF = 3 (class M, same as Virasoro)."""
        data = nonformality_depth("W_3", c=F(26))
        assert data["d_NF"] == 3
        assert data["is_formal"] is False

    def test_affine_d_NF_3(self):
        """Affine sl_2 at generic k: d_NF = 3 (S_3 != 0)."""
        data = nonformality_depth("affine_sl2", k=F(1))
        assert data["d_NF"] == 3


# ============================================================================
# Test 61-63: Cross-consistency checks (multi-path verification)
# ============================================================================

class TestCrossConsistency:
    """Cross-family and cross-method consistency checks."""

    def test_kappa_additivity_heisenberg(self):
        """kappa is additive: kappa(H_k1 + H_k2) = k1 + k2.

        Verified via the Heisenberg Swiss-cheese engine.
        """
        data1 = swiss_cheese_m3_heisenberg(F(3))
        data2 = swiss_cheese_m3_heisenberg(F(5))
        assert data1["kappa"] + data2["kappa"] == F(8)

    def test_S3_virasoro_equals_ell3_ope_ratio(self):
        """S_3 from Swiss-cheese engine matches ell_3 OPE ratio (cross-check)."""
        sc_data = swiss_cheese_m3_virasoro(F(26))
        ell3_data = linfty_ell3_virasoro_mode_sum(F(26))
        assert sc_data["S3_ope_ratio"] == ell3_data["S3_ope_ratio"]
        assert sc_data["S3_algebraic"] == ell3_data["S3_exact"]

    def test_Q_contact_from_S4(self):
        """Q^{contact} = 10/[c(5c+22)] is consistent between quartic shadow and ell_4.

        Multi-path: computed from S_4 formula and from ell_4 engine.
        """
        S4_data = virasoro_quartic_shadow(F(26))
        ell4_data = linfty_ell4_virasoro_exact(F(26))
        assert S4_data["Q_contact"] == ell4_data["Q_contact"]


# ============================================================================
# Test 64-66: Virasoro bracket verification
# ============================================================================

class TestVirasoroBracket:
    """Verify Virasoro commutation relations used in the mode sums."""

    def test_bracket_L2_Lm2(self):
        """[L_2, L_{-2}] = 4 L_0 + (c/12) * 2 * 3 = 4 L_0 + c/2."""
        struct, central = virasoro_bracket(2, -2, F(12))
        assert struct == F(4)  # (2 - (-2)) = 4
        assert central == F(12) / F(2)  # (12/12) * 2 * 3 = 6

    def test_bracket_L3_Lm3(self):
        """[L_3, L_{-3}] = 6 L_0 + (c/12) * 3 * 8 = 6 L_0 + 2c."""
        struct, central = virasoro_bracket(3, -3, F(12))
        assert struct == F(6)
        assert central == F(24)  # (12/12) * 3 * 8 = 24

    def test_bracket_symmetric_modes(self):
        """[L_m, L_m] = 0 (struct coeff (m-m) = 0, no central for m+m != 0)."""
        struct, central = virasoro_bracket(2, 2, F(26))
        assert struct == F(0)
        assert central == F(0)


# ============================================================================
# Test 67-70: Comprehensive nonformality summary
# ============================================================================

class TestNonformalitySummary:
    """Verify comprehensive nonformality summary."""

    def test_summary_all_koszul(self):
        """All families in summary are Koszul."""
        summary = nonformality_summary()
        for name, info in summary.items():
            assert info["koszul"] is True, f"{name} should be Koszul"

    def test_summary_class_ordering(self):
        """Class ordering: G < L < C < M."""
        summary = nonformality_summary()
        assert summary["Heisenberg"]["class"] == "G"
        assert summary["affine_sl2"]["class"] == "L"
        assert summary["betagamma"]["class"] == "C"
        assert summary["Virasoro"]["class"] == "M"

    def test_summary_virasoro_nonzero(self):
        """Virasoro entry confirms m_3^{SC} nonzero."""
        summary = nonformality_summary()
        assert summary["Virasoro"]["m3_SC_nonzero"] is True

    def test_summary_heisenberg_zero(self):
        """Heisenberg entry confirms m_3^{SC} zero."""
        summary = nonformality_summary()
        assert summary["Heisenberg"]["m3_SC_zero"] is True


# ============================================================================
# Test 71-73: Killing form and propagator for affine/Heisenberg
# ============================================================================

class TestKillingFormPropagator:
    """Verify Killing form and propagator for affine sl_2 and Heisenberg."""

    def test_affine_sl2_killing_m1(self):
        """Affine sl_2 at level k: eta(J_1, J_{-1}) = k."""
        assert affine_sl2_killing_form(1, F(3)) == F(3)

    def test_heisenberg_killing_m2(self):
        """Heisenberg at level k: eta(a_2, a_{-2}) = 2k."""
        assert heisenberg_killing_form(2, F(5)) == F(10)

    def test_heisenberg_propagator_m0_none(self):
        """Heisenberg propagator at m=0: None (eta vanishes)."""
        assert heisenberg_propagator(0, F(1)) is None


# ============================================================================
# Test 74-75: ell_4 for Virasoro
# ============================================================================

class TestLinftyEll4:
    """Verify L-infinity ell_4 for Virasoro."""

    def test_ell4_nonzero(self):
        """ell_4 is nonzero for Virasoro (class M)."""
        data = linfty_ell4_virasoro_exact(F(26))
        assert data["ell4_nonzero"] is True

    def test_ell4_S4_matches_quartic_shadow(self):
        """ell_4 S_4 matches independent quartic shadow computation."""
        ell4_data = linfty_ell4_virasoro_exact(F(26))
        s4_data = virasoro_quartic_shadow(F(26))
        assert ell4_data["S4"] == s4_data["S4"]
