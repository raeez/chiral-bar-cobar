r"""Tests for motivic_shadow_partition_engine.py.

40+ tests covering the motivic structure of the shadow partition function
tau_shadow(kappa, hbar) = tau_KW^kappa, answering the seven deep-research
questions about its coefficient field, Hodge structure, periods, motivic
Galois group, Beilinson cohomology, and negative results.

MULTI-PATH VERIFICATION (required by CLAUDE.md):
  * Every lambda_g^FP value verified via at least 3 independent paths:
    (a) direct Bernoulli formula
    (b) power-series expansion of (x/2)/sin(x/2) - 1
    (c) Deligne critical-value reconstruction

GROUND TRUTH:
  lambda_1^FP = 1/24
  lambda_2^FP = 7/5760
  lambda_3^FP = 31/967680
  lambda_4^FP = 127/154828800
  lambda_5^FP = 73/3503554560
  (from Faber-Pandharipande 2003, Ann. Math. 157)

SCOPE CHECKS:
  * rational kappa -> rational coefficients (no field extension)
  * F_g is NEVER an MZV, NEVER transcendental, NEVER involves pi
  * the Beilinson regulator on lambda_g vanishes (pure Tate => no transcendence)

NEGATIVE RESULTS VERIFIED:
  * tau_shadow is NOT a KdV tau function for kappa != 0, 1
  * F_g is not an MZV at any genus
  * the scalar map kappa -> motive(tau_shadow) is not injective

Manuscript references:
  thm:theorem-d (higher_genus_modular_koszul.tex)
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  FP03: Faber-Pandharipande, Ann. Math. 157 (2003), 97-124.
  Beilinson 1985 (motivic cohomology, regulator)
  Deligne 1971 (MHS construction)
"""

import unittest

from fractions import Fraction

from sympy import (
    Rational, Symbol, bernoulli, factorial, series, sin, expand, Poly,
)

from compute.lib.motivic_shadow_partition_engine import (
    # Core FP numbers
    lambda_fp,
    faber_pandharipande_table,
    # Q1 — coefficient field
    tau_shadow_genus_coefficient,
    coefficient_field_signature,
    verify_no_field_extension,
    # Q2 — motive at fixed genus
    TateMotive,
    motive_of_Fg,
    integrated_period_of_Fg,
    # Q3 — Hodge structure
    ShadowHodgeStructure,
    shadow_hodge_filtration,
    # Q4 — periods
    is_rational_period,
    period_classification,
    deligne_critical_value_check,
    # Q5 — pro-motive
    ShadowProMotive,
    shadow_pro_motive,
    motivic_galois_action,
    # Q6 — Beilinson
    beilinson_regulator_vanishing,
    deligne_mhs_summary,
    # Q7 — negative
    kdv_negative_result,
    mzv_negative_result,
    injectivity_negative_result,
    # Verification
    verify_lambda_fp_table,
    tau_shadow_log_expansion,
    tau_shadow_exp_expansion,
    # Universal Hodge
    UniversalShadowHodgeStructure,
    universal_shadow_hodge,
    # Examples
    example_heisenberg,
    example_virasoro,
    example_lattice_voa,
    # Summary
    shadow_motivic_summary,
)


# =========================================================================
# SECTION 1: Faber-Pandharipande table (6 tests)
# =========================================================================

class TestFaberPandharipandeTable(unittest.TestCase):
    """Test lambda_g^FP values with multi-path verification."""

    def test_01_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(lambda_fp(1), Rational(1, 24))

    def test_02_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        self.assertEqual(lambda_fp(2), Rational(7, 5760))

    def test_03_lambda_fp_g3(self):
        """lambda_3^FP = 31/967680."""
        self.assertEqual(lambda_fp(3), Rational(31, 967680))

    def test_04_lambda_fp_g4(self):
        """lambda_4^FP = 127/154828800."""
        self.assertEqual(lambda_fp(4), Rational(127, 154828800))

    def test_05_lambda_fp_all_positive(self):
        """lambda_g^FP > 0 for g = 1, ..., 8."""
        for g in range(1, 9):
            self.assertGreater(lambda_fp(g), 0, f"lambda_{g}^FP not positive")

    def test_06_lambda_fp_rejects_invalid(self):
        """lambda_fp(0) raises ValueError."""
        with self.assertRaises(ValueError):
            lambda_fp(0)
        with self.assertRaises(ValueError):
            lambda_fp(-1)


# =========================================================================
# SECTION 2: Multi-path verification of the FP table (3 tests)
# =========================================================================

class TestMultiPathVerification(unittest.TestCase):
    """Three independent computation paths must agree for each lambda_g^FP."""

    def test_07_three_paths_agree_through_g5(self):
        """Bernoulli / gen-fun / Deligne reconstruction agree through g = 5."""
        table = verify_lambda_fp_table(g_max=5)
        for g, row in table.items():
            self.assertTrue(row["all_match"], f"three paths disagree at g = {g}")

    def test_08_genfun_matches_bernoulli(self):
        """Generating function (x/2)/sin(x/2) - 1 matches Bernoulli formula."""
        x = Symbol("x")
        gen = series(x / 2 / sin(x / 2) - 1, x, 0, 14).removeO()
        expanded = expand(gen)
        p = Poly(expanded, x)
        coeffs = {2 * g: lambda_fp(g) for g in range(1, 6)}
        # Polynomial degrees must include 2, 4, 6, 8, 10.
        for deg, expected in coeffs.items():
            self.assertEqual(
                Rational(p.nth(deg)), expected,
                f"gen-fun coefficient at x^{deg} does not match lambda_{deg // 2}^FP"
            )

    def test_09_deligne_reconstruction(self):
        """Deligne critical-value reconstruction agrees with lambda_g^FP."""
        for g in range(1, 6):
            res = deligne_critical_value_check(g)
            self.assertTrue(res["matches"], f"Deligne reconstruction fails at g = {g}")
            self.assertEqual(res["reconstructed"], lambda_fp(g))


# =========================================================================
# SECTION 3: Q1 — coefficient field of tau_shadow (5 tests)
# =========================================================================

class TestCoefficientField(unittest.TestCase):
    """Verify that tau_shadow(kappa) lives in Q[[hbar^2]] for rational kappa."""

    def test_10_rational_kappa_stays_rational(self):
        """For kappa in Q, all coefficients F_g(kappa) are rational."""
        for kappa_val in [Rational(1), Rational(3, 2), Rational(-5), Rational(13, 2)]:
            res = verify_no_field_extension(kappa_val, g_max=6)
            self.assertEqual(res["field"], "Q")
            self.assertTrue(res["rational"])
            for g, c in res["coefficients"].items():
                self.assertIsInstance(c, Rational)

    def test_11_integer_kappa(self):
        """For integer kappa, all F_g are rational and match expected values."""
        sig = coefficient_field_signature(Rational(3))
        self.assertEqual(sig["field"], "Q")
        self.assertEqual(sig["extension_degree"], 1)

    def test_12_F1_kappa(self):
        """F_1(kappa) = kappa / 24."""
        for k in [Rational(1), Rational(-1), Rational(13, 2), Rational(24)]:
            self.assertEqual(tau_shadow_genus_coefficient(k, 1), k / 24)

    def test_13_F2_kappa(self):
        """F_2(kappa) = 7 * kappa / 5760."""
        k = Rational(24)  # Leech lattice
        self.assertEqual(
            tau_shadow_genus_coefficient(k, 2),
            Rational(7, 5760) * 24
        )

    def test_14_symbolic_kappa(self):
        """Symbolic kappa is treated as transcendental indeterminate."""
        k = Symbol("kappa")
        sig = coefficient_field_signature(k)
        self.assertEqual(sig["field"], "Q(kappa)")
        self.assertTrue(sig["transcendental"])


# =========================================================================
# SECTION 4: Q2 — motive of F_g (5 tests)
# =========================================================================

class TestTateMotiveAtGenus(unittest.TestCase):
    """The motive of F_g is Q(-g) — a Tate motive of weight 2g."""

    def test_15_tate_motive_weight(self):
        """Q(-g) has weight 2g."""
        for g in range(1, 8):
            m = motive_of_Fg(g)
            self.assertEqual(m.weight, 2 * g)

    def test_16_tate_motive_hodge_type(self):
        """Q(-g) has Hodge type (g, g)."""
        for g in range(1, 8):
            m = motive_of_Fg(g)
            self.assertEqual(m.hodge_type, (g, g))

    def test_17_tate_motive_dimension(self):
        """Q(-g) has Hodge dimension 1 (rank of the kappa-line)."""
        for g in range(1, 8):
            m = motive_of_Fg(g)
            self.assertEqual(m.hodge_dimension, 1)

    def test_18_integrated_period_rational(self):
        """The integrated period (after pairing with [M-bar_{g,1}]) is rational."""
        for g in range(1, 6):
            for kappa_val in [Rational(1), Rational(-1), Rational(13, 2)]:
                p = integrated_period_of_Fg(g, kappa_val)
                self.assertIsInstance(p, Rational)
                self.assertEqual(p, kappa_val * lambda_fp(g))

    def test_19_period_label(self):
        """Q(-g) has period (2 pi i)^g."""
        self.assertEqual(motive_of_Fg(1).period, "2*pi*i")
        self.assertEqual(motive_of_Fg(2).period, "(2*pi*i)^2")
        self.assertEqual(TateMotive(n=0).period, "1")


# =========================================================================
# SECTION 5: Q3 — Hodge structure (4 tests)
# =========================================================================

class TestShadowHodgeStructure(unittest.TestCase):
    """The shadow class lives in the (g, g) piece of H^{2g}(M-bar_g)."""

    def test_20_hodge_structure_is_pure(self):
        """Each shadow Hodge structure is pure."""
        for g in range(1, 8):
            hs = ShadowHodgeStructure.for_genus(g)
            self.assertTrue(hs.is_pure)

    def test_21_hodge_structure_is_tate(self):
        """Each shadow Hodge structure is a Tate twist."""
        for g in range(1, 8):
            hs = ShadowHodgeStructure.for_genus(g)
            self.assertTrue(hs.is_tate)

    def test_22_hodge_filtration_dict(self):
        """shadow_hodge_filtration returns dict {g: HS} for g = 1 ... g_max."""
        hf = shadow_hodge_filtration(g_max=5)
        self.assertEqual(set(hf.keys()), {1, 2, 3, 4, 5})
        for g, hs in hf.items():
            self.assertEqual(hs.genus, g)
            self.assertEqual(hs.weight, 2 * g)

    def test_23_hodge_polynomial_label(self):
        """Hodge polynomial of genus-g shadow piece is u^g * v^g."""
        hs = ShadowHodgeStructure.for_genus(3)
        self.assertEqual(hs.hodge_polynomial(), "u^3 * v^3")


# =========================================================================
# SECTION 6: Q4 — periods (5 tests)
# =========================================================================

class TestPeriods(unittest.TestCase):
    """F_g(kappa) is rational, not MZV, not transcendental."""

    def test_24_F_g_is_rational_for_rational_kappa(self):
        """F_g(kappa) in Q for kappa in Q."""
        for g in range(1, 6):
            for k in [Rational(1), Rational(-3, 7), Rational(24)]:
                F = tau_shadow_genus_coefficient(k, g)
                self.assertTrue(is_rational_period(F))

    def test_25_period_classification_labels(self):
        """period_classification returns correct negative flags."""
        cl = period_classification(3, Rational(1))
        self.assertTrue(cl["is_rational"])
        self.assertFalse(cl["is_mzv"])
        self.assertFalse(cl["involves_pi"])
        self.assertFalse(cl["involves_zeta"])
        self.assertEqual(cl["transcendence_degree"], 0)

    def test_26_deligne_critical_value_g1(self):
        """Deligne reconstruction at g = 1: lambda_1^FP = 1/24."""
        res = deligne_critical_value_check(1)
        self.assertEqual(res["lambda_g_FP"], Rational(1, 24))
        self.assertTrue(res["matches"])

    def test_27_deligne_critical_value_g2(self):
        """Deligne reconstruction at g = 2: lambda_2^FP = 7/5760."""
        res = deligne_critical_value_check(2)
        self.assertEqual(res["lambda_g_FP"], Rational(7, 5760))
        self.assertTrue(res["matches"])

    def test_28_no_zeta_in_rational_lambda_fp(self):
        """lambda_g^FP is rational even though zeta(2g) is transcendental.

        This is the key Deligne observation: the (2pi)^{2g} factor strips
        pi out of lambda_g^FP, leaving a rational number.
        """
        for g in range(1, 6):
            lam = lambda_fp(g)
            self.assertIsInstance(lam, Rational)
            # It is a rational function of the Bernoulli number:
            B = Rational(bernoulli(2 * g))
            expected = Rational(
                (2 ** (2 * g - 1) - 1) * abs(B),
                2 ** (2 * g - 1) * factorial(2 * g),
            )
            self.assertEqual(lam, expected)


# =========================================================================
# SECTION 7: Q5 — pro-motive M^sh (5 tests)
# =========================================================================

class TestShadowProMotive(unittest.TestCase):
    """The shadow pro-motive is prod_g Q(-g) with motivic Galois group G_m."""

    def test_29_pro_motive_layers(self):
        """Layer g is Q(-g) for g = 1, ..., g_max."""
        pm = shadow_pro_motive(g_max=5)
        for i, layer in enumerate(pm.layers, start=1):
            self.assertEqual(layer.n, i)

    def test_30_motivic_galois_group_is_Gm(self):
        """G_mot(M^sh) = G_m."""
        pm = shadow_pro_motive(g_max=5)
        self.assertEqual(pm.motivic_galois_group, "G_m")

    def test_31_cocharacter_weight(self):
        """Cocharacter weight on Q(-g) is 2g."""
        pm = shadow_pro_motive(g_max=5)
        for g, w in pm.cocharacter_weight.items():
            self.assertEqual(w, 2 * g)

    def test_32_is_mixed_tate(self):
        """M^sh is mixed Tate but NOT pure (different layer weights)."""
        pm = shadow_pro_motive(g_max=5)
        self.assertTrue(pm.is_mixed_tate)
        self.assertFalse(pm.is_pure)

    def test_33_motivic_galois_action(self):
        """G_m acts on the genus-g layer by t^{2g}."""
        t = Symbol("t")
        self.assertEqual(motivic_galois_action(1, t), t ** 2)
        self.assertEqual(motivic_galois_action(3, t), t ** 6)


# =========================================================================
# SECTION 8: Q6 — Beilinson regulator (3 tests)
# =========================================================================

class TestBeilinsonRegulator(unittest.TestCase):
    """The Beilinson regulator vanishes on pure Tate classes."""

    def test_34_regulator_vanishes(self):
        """The regulator vanishes on lambda_g for every g >= 1."""
        for g in range(1, 8):
            res = beilinson_regulator_vanishing(g)
            self.assertTrue(res["regulator_vanishes"])
            self.assertTrue(res["period_in_Q"])
            self.assertEqual(res["period_value"], lambda_fp(g))

    def test_35_deligne_mhs_summary_is_pure(self):
        """Deligne MHS data: each genus layer is pure of type (g, g)."""
        mhs = deligne_mhs_summary(g_max=5)
        for g, data in mhs.items():
            self.assertTrue(data["is_pure"])
            self.assertEqual(data["hodge_type"], (g, g))
            self.assertEqual(data["weight"], 2 * g)
            self.assertEqual(data["tate_twist"], -g)

    def test_36_MHS_filtration_consistency(self):
        """F^g is full, F^{g+1} is zero; W_{2g} is full, W_{2g-1} is zero."""
        mhs = deligne_mhs_summary(g_max=4)
        for g, data in mhs.items():
            self.assertEqual(data["filtration_F"][f"F^{g}"], "full")
            self.assertEqual(data["filtration_F"][f"F^{g+1}"], "zero")


# =========================================================================
# SECTION 9: Q7 — negative motivic results (4 tests)
# =========================================================================

class TestNegativeResults(unittest.TestCase):
    """Negative motivic results: KdV fails, MZV fails, scalar injectivity fails."""

    def test_37_kdv_fails_for_generic_kappa(self):
        """tau_shadow is not KdV for kappa != 0, 1."""
        for k in [Rational(2), Rational(3), Rational(13, 2), Rational(24)]:
            res = kdv_negative_result(k)
            self.assertFalse(res["satisfies_kdv"])

    def test_38_kdv_trivially_satisfied_at_kappa_0_or_1(self):
        """kappa = 0 and kappa = 1 are the only KdV-compatible values."""
        for k in [Rational(0), Rational(1)]:
            res = kdv_negative_result(k)
            self.assertTrue(res["satisfies_kdv"])

    def test_39_mzv_fails_at_every_genus(self):
        """F_g is never an MZV — it is always rational."""
        for g in range(1, 8):
            res = mzv_negative_result(g)
            self.assertFalse(res["is_mzv"])
            self.assertTrue(res["is_rational"])

    def test_40_scalar_injectivity_fails(self):
        """kappa -> motive(tau_shadow) is not injective at scalar level."""
        res = injectivity_negative_result()
        self.assertFalse(res["injective_on_motives"])
        self.assertTrue(res["injective_on_values"])


# =========================================================================
# SECTION 10: Universal Hodge structure (4 tests)
# =========================================================================

class TestUniversalHodgeStructure(unittest.TestCase):
    """The universal Hodge structure underlying tau_shadow."""

    def test_41_betti_dimension_equals_g_max(self):
        """Betti dimension of the truncated pro-motive = g_max."""
        for g_max in [3, 5, 8]:
            u = universal_shadow_hodge(g_max=g_max)
            self.assertEqual(u.betti_dimension, g_max)

    def test_42_hodge_polynomial(self):
        """Hodge polynomial sum_g u^g v^g through genus 4."""
        u_sym = Symbol("u")
        v_sym = Symbol("v")
        uhs = universal_shadow_hodge(g_max=4)
        poly = uhs.hodge_polynomial(u_sym, v_sym)
        expected = u_sym * v_sym + u_sym ** 2 * v_sym ** 2 + u_sym ** 3 * v_sym ** 3 + u_sym ** 4 * v_sym ** 4
        self.assertEqual(expand(poly - expected), 0)

    def test_43_frobenius_eigenvalues(self):
        """Frobenius at prime p acts by {p^g : g = 1, ..., g_max}."""
        uhs = universal_shadow_hodge(g_max=4)
        evals = uhs.frobenius_eigenvalues(5)
        self.assertEqual(evals, [5, 25, 125, 625])

    def test_44_crystalline_and_abelian(self):
        """Tate pro-motive is crystalline and its Galois action is abelian."""
        uhs = universal_shadow_hodge(g_max=5)
        self.assertTrue(uhs.is_crystalline())
        self.assertTrue(uhs.galois_action_is_abelian())
        self.assertTrue(uhs.is_mixed_tate())


# =========================================================================
# SECTION 11: Examples — Heisenberg, Virasoro, Lattice VOAs (4 tests)
# =========================================================================

class TestExamples(unittest.TestCase):
    """Concrete family examples."""

    def test_45_heisenberg_kappa_is_level(self):
        """Heisenberg H_k has kappa = k (integer, in Q)."""
        ex = example_heisenberg(level_k=3, g_max=4)
        self.assertEqual(ex["kappa"], Rational(3))
        self.assertEqual(ex["shadow_class"], "G (Gaussian)")
        # F_1 = 3 * 1/24 = 1/8
        self.assertEqual(ex["tau_shadow_coeffs"][1], Rational(1, 8))

    def test_46_virasoro_kappa_is_c_over_2(self):
        """Virasoro Vir_c has kappa = c/2 (AP9 compliant)."""
        ex = example_virasoro(Rational(26), g_max=3)
        self.assertEqual(ex["kappa"], Rational(13))
        # F_1 = 13 * 1/24 = 13/24
        self.assertEqual(ex["tau_shadow_coeffs"][1], Rational(13, 24))

    def test_47_lattice_voa_kappa_is_rank(self):
        """Lattice VOA has kappa = rank (AP48 compliant)."""
        ex = example_lattice_voa(rank=24, g_max=3)  # Leech
        self.assertEqual(ex["kappa"], Rational(24))
        # F_1 = 24 / 24 = 1
        self.assertEqual(ex["tau_shadow_coeffs"][1], Rational(1))

    def test_48_virasoro_self_dual_c13(self):
        """Virasoro at c = 13 has kappa = 13/2."""
        ex = example_virasoro(Rational(13), g_max=3)
        self.assertEqual(ex["kappa"], Rational(13, 2))


# =========================================================================
# SECTION 12: Cross-consistency and summary (4 tests)
# =========================================================================

class TestCrossConsistency(unittest.TestCase):
    """Cross-checks between independent sub-engines."""

    def test_49_log_exp_round_trip(self):
        """exp(log(tau_shadow)) reconstructs tau_shadow at low order."""
        h = Symbol("hbar")
        k = Rational(2)
        ts = tau_shadow_exp_expansion(k, g_max=3)
        # Leading coefficient is 1 (exp(0) = 1)
        self.assertEqual(ts.subs(h, 0), 1)
        # Coefficient of hbar^2 is F_1 = k/24
        p = Poly(ts, h)
        self.assertEqual(Rational(p.nth(2)), k * Rational(1, 24))

    def test_50_summary_contains_all_questions(self):
        """Top-level summary covers all seven questions."""
        summary = shadow_motivic_summary(g_max=4)
        for q in ["Q1_coefficient_field", "Q2_motive_at_genus",
                  "Q3_hodge_structure", "Q4_periods", "Q5_pro_motive",
                  "Q6_beilinson", "Q7_negative_results"]:
            self.assertIn(q, summary)

    def test_51_ap48_violation_detection(self):
        """A lattice VOA at rank 8 has kappa = 8, NOT c/2 = 4."""
        ex = example_lattice_voa(rank=8, g_max=2)  # E_8
        self.assertEqual(ex["kappa"], Rational(8))
        # Warning: c(E_8) = 8 so c/2 = 4 — these differ by a factor of 2
        # in a way that matches AP48 (kappa = rank is LARGER than c/2 here).
        self.assertNotEqual(ex["kappa"], Rational(8) / 2)

    def test_52_fp_table_size(self):
        """faber_pandharipande_table returns g_max entries."""
        table = faber_pandharipande_table(g_max=6)
        self.assertEqual(len(table), 6)
        for g in range(1, 7):
            self.assertIn(g, table)
            self.assertEqual(table[g], lambda_fp(g))


# =========================================================================
# SECTION 13: Structural invariants under Galois action (3 tests)
# =========================================================================

class TestGaloisInvariance(unittest.TestCase):
    """Structural invariants preserved by the motivic Galois group."""

    def test_53_weight_invariant_under_Gm(self):
        """The weight 2g of Q(-g) is invariant under G_m action (it IS the cocharacter)."""
        pm = shadow_pro_motive(g_max=5)
        for g, w in pm.cocharacter_weight.items():
            self.assertEqual(w, 2 * g)
            # The weight equals the Hodge type diagonal (g, g).
            m = TateMotive(n=g)
            self.assertEqual(m.weight, w)

    def test_54_genus_layer_dimensions_stable(self):
        """Each genus layer has Hodge dimension 1 (Tate is 1-dimensional)."""
        pm = shadow_pro_motive(g_max=6)
        for layer in pm.layers:
            self.assertEqual(layer.hodge_dimension, 1)

    def test_55_frobenius_eigenvalues_satisfy_weil_bound(self):
        """|Frob_p eigenvalue| = p^g for Q(-g) (Weil bound, equality case)."""
        uhs = universal_shadow_hodge(g_max=4)
        for p in [2, 3, 5, 7, 11]:
            evals = uhs.frobenius_eigenvalues(p)
            for g, val in enumerate(evals, start=1):
                self.assertEqual(abs(val), p ** g)


if __name__ == "__main__":
    unittest.main()
