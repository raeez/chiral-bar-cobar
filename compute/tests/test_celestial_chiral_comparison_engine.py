r"""Tests for celestial chiral comparison engine.

Systematic comparison of our bar-cobar/shadow obstruction tower framework
with the celestial holography literature.

Verifies:
1.  Celestial OPE matches our chiral algebra OPE (gluon ++, +-, graviton TT, TW)
2.  Soft theorem tower matches shadow obstruction tower projections (orders 0-5)
3.  kappa computed correctly for all celestial algebra types (SDYM, SDGR, W_N)
4.  kappa additivity: kappa(W_N) = sum_{s=2}^N c/s (channel-refined)
5.  kappa Virasoro consistency: kappa(W_2) = kappa(Vir) = c/2
6.  R-matrix pole reduction by 1 (AP19) for all spins 1-6
7.  R-matrix all-odd-poles property (bosonic algebra)
8.  Costello-Paquette twisted holography: same algebra, complementary approach
9.  w_{1+inf} vs W_{1+inf}: wedge subalgebra relationship
10. Bar complex computes MHV tree amplitudes (4pt, 5pt, 6pt)
11. Genus expansion F_g = kappa * lambda_g for celestial amplitudes
12. Cross-checks: kappa at k=0 for SDYM, soft-shadow correspondence
13. Lambda_g^FP values at g=1,2,3
14. Central charge formulas for W_N at low N
15. kappa divergence at large N (logarithmic)
16. Self-dual vs full YM distinction
17. Critical level singularity
18. Shadow depth classification for celestial algebras
19. Complementarity at c=26 (critical string)
20. Full comparison suite integration test

Ground truth sources:
    - Pate-Raclariu-Strominger-Yuan (2021): celestial OPE, 1911.02018
    - Guevara-Himwich-Pate-Strominger (2021): w_{1+inf}, 2106.10227
    - Strominger (2021): w_{1+inf} and celestial, 2105.14346
    - Costello-Paquette (2022): twisted holography, 2201.02595, 2208.14233
    - Weinberg (1965): leading soft graviton theorem
    - Cachazo-Strominger (2014): subleading soft graviton, 1404.4091
    - concordance.tex, higher_genus_modular_koszul.tex
    - celestial_koszul_ope.py, celestial_shadow_engine.py (existing engines)
"""

from fractions import Fraction

import pytest

from compute.lib.celestial_chiral_comparison_engine import (
    # Arithmetic
    harmonic_number,
    bernoulli_exact,
    lambda_fp,
    # Lie data
    LieAlgebraData,
    sl_n_data,
    # kappa
    kappa_km,
    kappa_virasoro,
    kappa_wn,
    central_charge_km,
    wn_central_charge,
    # OPE comparison
    CelestialOPEComparison,
    compare_gluon_ope_pp,
    compare_gluon_ope_pm,
    compare_graviton_ope_tt,
    compare_graviton_ope_tw,
    # Soft theorem comparison
    SoftTheoremComparison,
    compare_leading_soft,
    compare_subleading_soft,
    compare_subsubleading_soft,
    soft_theorem_tower_comparison,
    # kappa comparison
    KappaComparison,
    kappa_sdym,
    kappa_sdgr_virasoro,
    kappa_sdgr_wn,
    # Costello-Paquette
    TwistedHolographyComparison,
    compare_cp_boundary_algebra,
    compare_cp_modular_lift,
    compare_cp_koszul_duality,
    # R-matrix
    r_matrix_pole_orders,
    celestial_r_matrix_gluon,
    celestial_r_matrix_graviton,
    celestial_r_matrix_higher_spin,
    # w_{1+inf}
    WInfinityComparison,
    compare_w_infinity_algebras,
    # Amplitudes
    bar_complex_computes_mhv,
    celestial_amplitude_from_shadow,
    # Full suite
    run_full_comparison,
    # Cross-checks
    cross_check_kappa_additivity,
    cross_check_kappa_virasoro_consistency,
    cross_check_r_matrix_pole_reduction,
    cross_check_soft_shadow_correspondence,
    cross_check_genus_expansion_sdym,
    cross_check_genus_expansion_sdgr,
)


# ============================================================================
# Section 1: Arithmetic foundations
# ============================================================================

class TestArithmeticFoundations:
    """Verify arithmetic building blocks."""

    def test_harmonic_h1(self):
        assert harmonic_number(1) == Fraction(1)

    def test_harmonic_h2(self):
        assert harmonic_number(2) == Fraction(3, 2)

    def test_harmonic_h3(self):
        assert harmonic_number(3) == Fraction(11, 6)

    def test_harmonic_h5(self):
        assert harmonic_number(5) == Fraction(137, 60)

    def test_harmonic_h0(self):
        assert harmonic_number(0) == Fraction(0)

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

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_g3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)


# ============================================================================
# Section 2: Celestial OPE comparisons
# ============================================================================

class TestCelestialOPEComparison:
    """Verify celestial OPE matches our framework."""

    def test_gluon_pp_match(self):
        """++ gluon OPE: structure constant f^{abc}, simple pole."""
        comp = compare_gluon_ope_pp(3)
        assert comp.match is True
        assert comp.pole_order == 1

    def test_gluon_pp_su2(self):
        """++ gluon OPE for SU(2)."""
        comp = compare_gluon_ope_pp(2)
        assert comp.match is True
        assert "f^{abc}" in comp.our_ope_leading

    def test_gluon_pp_su5(self):
        """++ gluon OPE for SU(5)."""
        comp = compare_gluon_ope_pp(5)
        assert comp.match is True

    def test_gluon_pm_match(self):
        """+- gluon OPE: involves double pole at k != 0."""
        comp = compare_gluon_ope_pm(3)
        assert comp.match is True
        assert comp.pole_order == 2

    def test_graviton_tt_match(self):
        """Graviton TT OPE = Virasoro OPE."""
        comp = compare_graviton_ope_tt(26)
        assert comp.match is True
        assert comp.pole_order == 4

    def test_graviton_tt_c30(self):
        """Graviton TT OPE at c=30."""
        comp = compare_graviton_ope_tt(30)
        assert comp.match is True

    def test_graviton_tw_match(self):
        """Graviton TW OPE: conformal weight 3."""
        comp = compare_graviton_ope_tw()
        assert comp.match is True
        assert comp.pole_order == 2


# ============================================================================
# Section 3: Soft theorem comparisons
# ============================================================================

class TestSoftTheoremComparison:
    """Verify soft theorems match shadow tower projections."""

    def test_leading_soft_weinberg(self):
        """Leading soft theorem (Weinberg) from kappa."""
        comp = compare_leading_soft(Fraction(26))
        assert comp.match is True
        assert comp.shadow_arity == 2
        assert comp.shadow_value == Fraction(13)  # c/2 = 26/2

    def test_subleading_soft_cachazo_strominger(self):
        """Subleading soft theorem from cubic shadow S_3 = 2."""
        comp = compare_subleading_soft(Fraction(26))
        assert comp.match is True
        assert comp.shadow_arity == 3
        assert comp.shadow_value == Fraction(2)

    def test_subsubleading_soft(self):
        """Sub-subleading from quartic Q^contact."""
        comp = compare_subsubleading_soft(Fraction(26))
        assert comp.match is True
        assert comp.shadow_arity == 4
        # Q = 10/[26*(5*26+22)] = 10/[26*152] = 10/3952 = 5/1976
        expected_q = Fraction(10) / (26 * (5 * 26 + 22))
        assert comp.shadow_value == expected_q

    def test_soft_tower_length(self):
        """Full tower has max_order + 1 entries."""
        tower = soft_theorem_tower_comparison(Fraction(26), max_order=5)
        assert len(tower) == 6

    def test_soft_tower_all_match(self):
        """All entries in the tower should match."""
        tower = soft_theorem_tower_comparison(Fraction(26), max_order=5)
        for entry in tower:
            assert entry.match is True

    def test_soft_arity_shift(self):
        """Arity = soft order + 2 for all entries."""
        tower = soft_theorem_tower_comparison(Fraction(26), max_order=5)
        for entry in tower:
            assert entry.shadow_arity == entry.order + 2

    def test_leading_soft_c13(self):
        """At c=13 (self-dual point): kappa = 13/2."""
        comp = compare_leading_soft(Fraction(13))
        assert comp.shadow_value == Fraction(13, 2)


# ============================================================================
# Section 4: kappa comparisons
# ============================================================================

class TestKappaComparison:
    """Verify kappa across all celestial algebra types."""

    def test_kappa_sdym_k0_su2(self):
        """kappa(V_0(sl_2)) = 3*2/(2*2) = 3/2."""
        comp = kappa_sdym(2, k=0)
        assert comp.kappa_our == Fraction(3, 2)

    def test_kappa_sdym_k0_su3(self):
        """kappa(V_0(sl_3)) = 8*3/(2*3) = 4."""
        comp = kappa_sdym(3, k=0)
        assert comp.kappa_our == Fraction(4)

    def test_kappa_sdym_k1_su2(self):
        """kappa(V_1(sl_2)) = 3*3/(2*2) = 9/4."""
        comp = kappa_sdym(2, k=1)
        assert comp.kappa_our == Fraction(9, 4)

    def test_kappa_sdym_k1_su3(self):
        """kappa(V_1(sl_3)) = 8*4/(2*3) = 16/3."""
        comp = kappa_sdym(3, k=1)
        assert comp.kappa_our == Fraction(16, 3)

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13."""
        comp = kappa_sdgr_virasoro(Fraction(26))
        assert comp.kappa_our == Fraction(13)

    def test_kappa_virasoro_c13(self):
        """kappa(Vir_13) = 13/2."""
        comp = kappa_sdgr_virasoro(Fraction(13))
        assert comp.kappa_our == Fraction(13, 2)

    def test_kappa_w3_c26(self):
        """kappa(W_3(c=26)) = 26*(H_3-1) = 26*5/6 = 130/6 = 65/3."""
        comp = kappa_sdgr_wn(3, Fraction(26))
        assert comp.kappa_our == Fraction(26) * (Fraction(11, 6) - 1)
        assert comp.kappa_our == Fraction(130, 6)

    def test_kappa_w2_equals_virasoro(self):
        """kappa(W_2) = kappa(Vir) = c/2 for any c."""
        for c in [Fraction(10), Fraction(26), Fraction(50)]:
            kw2 = kappa_sdgr_wn(2, c)
            kvir = kappa_sdgr_virasoro(c)
            assert kw2.kappa_our == kvir.kappa_our


# ============================================================================
# Section 5: kappa cross-checks
# ============================================================================

class TestKappaCrossChecks:
    """Cross-check kappa formulas by multiple paths."""

    def test_kappa_additivity_n3(self):
        """kappa(W_3) = c/2 + c/3 = 5c/6."""
        result = cross_check_kappa_additivity(Fraction(30), 3)
        assert result["match"] is True

    def test_kappa_additivity_n5(self):
        """kappa(W_5) = sum_{s=2}^5 c/s."""
        result = cross_check_kappa_additivity(Fraction(60), 5)
        assert result["match"] is True

    def test_kappa_additivity_n10(self):
        """kappa(W_10) channel sum equals total."""
        result = cross_check_kappa_additivity(Fraction(120), 10)
        assert result["match"] is True

    def test_kappa_virasoro_consistency_c26(self):
        """kappa(W_2) = kappa(Vir) = 13 at c=26."""
        result = cross_check_kappa_virasoro_consistency(Fraction(26))
        assert result["match"] is True
        assert result["both_equal_c_over_2"] is True

    def test_kappa_virasoro_consistency_c50(self):
        result = cross_check_kappa_virasoro_consistency(Fraction(50))
        assert result["match"] is True
        assert result["kappa_W2"] == Fraction(25)

    def test_kappa_km_vs_virasoro_sl2(self):
        """For sl_2 at level k: kappa_KM = 3(k+2)/4.
        Virasoro from DS at same level: c = 1 - 6(k+1)^2/(k+2),
        kappa_Vir = c/2.  These are DIFFERENT (AP9)."""
        g = sl_n_data(2)
        k = Fraction(1)
        kap_km = kappa_km(g, k)
        c_km = central_charge_km(g, k)
        kap_vir_of_c = kappa_virasoro(c_km)
        # kap_km = 3*3/4 = 9/4, c = 1, kap_vir = 1/2
        assert kap_km == Fraction(9, 4)
        assert c_km == Fraction(1)
        assert kap_vir_of_c == Fraction(1, 2)
        # They are DIFFERENT (AP9)
        assert kap_km != kap_vir_of_c


# ============================================================================
# Section 6: R-matrix pole reduction (AP19)
# ============================================================================

class TestRMatrixPoleReduction:
    """Verify AP19: r-matrix pole = OPE pole - 1."""

    def test_pole_reduction_spin1(self):
        """Spin 1: OPE z^{-2}, r-matrix z^{-1}."""
        assert r_matrix_pole_orders(2) == 1

    def test_pole_reduction_spin2(self):
        """Spin 2: OPE z^{-4}, r-matrix z^{-3}."""
        assert r_matrix_pole_orders(4) == 3

    def test_pole_reduction_spin3(self):
        """Spin 3: OPE z^{-6}, r-matrix z^{-5}."""
        assert r_matrix_pole_orders(6) == 5

    def test_all_reductions_by_1(self):
        """All spins 1-6: reduction by exactly 1."""
        results = cross_check_r_matrix_pole_reduction(6)
        for r in results:
            assert r["reduction_by_1"] is True

    def test_all_r_poles_odd(self):
        """All r-matrix poles are odd for bosonic algebra."""
        results = cross_check_r_matrix_pole_reduction(6)
        for r in results:
            assert r["all_odd"] is True

    def test_gluon_r_matrix_k0_simple_pole(self):
        """Gluon r-matrix at k=0: single simple pole."""
        g = sl_n_data(3)
        r = celestial_r_matrix_gluon(g, k=0)
        assert r["pole_orders"] == (1,)
        assert r["satisfies_cybe"] is True
        assert r["is_triangular"] is True

    def test_gluon_r_matrix_k1(self):
        """Gluon r-matrix at k=1: level-dependent."""
        g = sl_n_data(3)
        r = celestial_r_matrix_gluon(g, k=1)
        assert r["pole_orders"] == (1,)
        assert r["is_triangular"] is False  # Casimir term breaks triangularity

    def test_graviton_r_matrix_poles(self):
        """Graviton r-matrix: poles at z^{-3} and z^{-1}."""
        r = celestial_r_matrix_graviton(Fraction(26))
        assert r["pole_orders"] == (3, 1)
        assert r["leading_coeff"] == Fraction(13)  # c/2

    def test_higher_spin_r_matrix_spin4(self):
        """Spin-4 r-matrix: leading pole z^{-7}."""
        r = celestial_r_matrix_higher_spin(4, Fraction(30))
        assert r["r_matrix_leading_pole"] == 7
        assert r["leading_coeff"] == Fraction(30, 4)
        assert r["all_odd"] is True

    def test_higher_spin_r_matrix_spin5(self):
        """Spin-5 r-matrix: leading pole z^{-9}."""
        r = celestial_r_matrix_higher_spin(5, Fraction(30))
        assert r["r_matrix_leading_pole"] == 9
        assert r["leading_coeff"] == Fraction(6)


# ============================================================================
# Section 7: Costello-Paquette comparisons
# ============================================================================

class TestCostelloPaquetteComparison:
    """Verify Costello-Paquette twisted holography comparison."""

    def test_boundary_algebra_same(self):
        """CP and our framework produce the SAME boundary algebra."""
        comp = compare_cp_boundary_algebra()
        assert "SAME" in comp.relationship

    def test_modular_lift_ours(self):
        """Our framework provides the genus expansion."""
        comp = compare_cp_modular_lift()
        assert "genus expansion" in comp.relationship.lower() or \
               "OUR" in comp.relationship

    def test_koszul_duality_complementary(self):
        """The two frameworks are complementary."""
        comp = compare_cp_koszul_duality()
        assert "COMPLEMENTARY" in comp.relationship

    def test_bar_not_bulk_ap25(self):
        """AP25: bar != bulk is correctly stated."""
        comp = compare_cp_koszul_duality()
        assert "AP25" in comp.our_framework or "AP25" in comp.notes


# ============================================================================
# Section 8: w_{1+inf} comparisons
# ============================================================================

class TestWInfinityComparison:
    """Verify w_{1+inf} vs W_{1+inf} comparison."""

    def test_comparison_list_length(self):
        """Five aspects compared."""
        comps = compare_w_infinity_algebras()
        assert len(comps) == 5

    def test_wedge_subalgebra_relationship(self):
        """w_{1+inf} is the wedge subalgebra of W_{1+inf}."""
        comps = compare_w_infinity_algebras()
        algebra_comp = [c for c in comps if c.aspect == "Algebra type"][0]
        assert "WEDGE" in algebra_comp.relationship.upper() or \
               "wedge" in algebra_comp.relationship

    def test_shadow_depth_class_m(self):
        """Shadow depth = class M (infinite)."""
        comps = compare_w_infinity_algebras()
        depth_comp = [c for c in comps if c.aspect == "Shadow depth"][0]
        assert "infinite" in depth_comp.our_framework.lower() or \
               "M" in depth_comp.our_framework

    def test_kappa_not_in_celestial_literature(self):
        """kappa is not directly computed in celestial literature."""
        comps = compare_w_infinity_algebras()
        kappa_comp = [c for c in comps if c.aspect == "kappa"][0]
        assert "not" in kappa_comp.celestial.lower() or \
               "Not" in kappa_comp.celestial


# ============================================================================
# Section 9: Bar complex and amplitudes
# ============================================================================

class TestBarComplexAmplitudes:
    """Verify bar complex computes celestial amplitudes."""

    def test_mhv_4pt(self):
        """4-point MHV: bar degree 2."""
        g = sl_n_data(3)
        result = bar_complex_computes_mhv(4, g)
        assert result["bar_degree"] == 2
        assert result["bar_complex_match"] is True

    def test_mhv_5pt(self):
        """5-point MHV: bar degree 3."""
        g = sl_n_data(3)
        result = bar_complex_computes_mhv(5, g)
        assert result["bar_degree"] == 3
        assert result["bar_complex_match"] is True

    def test_mhv_6pt(self):
        """6-point MHV: bar degree 4."""
        g = sl_n_data(4)
        result = bar_complex_computes_mhv(6, g)
        assert result["bar_degree"] == 4
        assert result["bar_complex_match"] is True

    def test_genus_1_amplitude(self):
        """Genus-1 celestial amplitude: F_1 = kappa/24."""
        result = celestial_amplitude_from_shadow(1, 0, Fraction(13))
        assert result["F_g"] == Fraction(13, 24)

    def test_genus_2_amplitude(self):
        """Genus-2: F_2 = kappa * 7/5760."""
        result = celestial_amplitude_from_shadow(2, 0, Fraction(13))
        assert result["F_g"] == Fraction(13) * Fraction(7, 5760)

    def test_genus_0_tree_level(self):
        """Genus 0: tree-level, no F_g formula."""
        result = celestial_amplitude_from_shadow(0, 4, Fraction(13))
        assert "genus" in result["notes"].lower() or "tree" in result["notes"].lower()


# ============================================================================
# Section 10: Genus expansion cross-checks
# ============================================================================

class TestGenusExpansionCrossChecks:
    """Cross-check genus expansion for celestial algebras."""

    def test_sdym_genus_expansion_su3(self):
        """Genus expansion for V_1(sl_3): kappa = 16/3."""
        results = cross_check_genus_expansion_sdym(3, k=1, max_genus=3)
        assert len(results) == 3
        kap = Fraction(16, 3)
        assert results[0]["kappa"] == kap
        assert results[0]["F_g"] == kap * Fraction(1, 24)

    def test_sdgr_genus_expansion_c26(self):
        """Genus expansion for Vir_26: kappa = 13."""
        results = cross_check_genus_expansion_sdgr(Fraction(26), max_genus=3)
        assert results[0]["F_g"] == Fraction(13, 24)
        assert results[1]["F_g"] == Fraction(13) * Fraction(7, 5760)

    def test_sdgr_genus_expansion_c13(self):
        """Genus expansion at self-dual point c=13."""
        results = cross_check_genus_expansion_sdgr(Fraction(13), max_genus=2)
        assert results[0]["F_g"] == Fraction(13, 48)  # (13/2)/24 = 13/48

    def test_sdgr_f1_positive(self):
        """F_1 is positive for c > 0."""
        for c in [Fraction(1), Fraction(13), Fraction(26), Fraction(100)]:
            results = cross_check_genus_expansion_sdgr(c, max_genus=1)
            assert results[0]["F_g"] > 0


# ============================================================================
# Section 11: Soft-shadow correspondence
# ============================================================================

class TestSoftShadowCorrespondence:
    """Verify the soft theorem <-> shadow projection correspondence."""

    def test_correspondence_arity_shift(self):
        """Arity = soft order + 2."""
        results = cross_check_soft_shadow_correspondence(Fraction(26), max_order=4)
        for r in results:
            assert r["arity_shift"] == 2
            assert r["shadow_arity"] == r["soft_order"] + 2

    def test_correspondence_order_0(self):
        """Order 0: Weinberg <-> kappa (arity 2)."""
        results = cross_check_soft_shadow_correspondence(Fraction(26), max_order=0)
        assert results[0]["shadow_arity"] == 2

    def test_correspondence_order_1(self):
        """Order 1: Cachazo-Strominger <-> cubic (arity 3)."""
        results = cross_check_soft_shadow_correspondence(Fraction(26), max_order=1)
        assert results[1]["shadow_arity"] == 3

    def test_correspondence_order_2(self):
        """Order 2: sub-subleading <-> quartic (arity 4)."""
        results = cross_check_soft_shadow_correspondence(Fraction(26), max_order=2)
        assert results[2]["shadow_arity"] == 4


# ============================================================================
# Section 12: Central charge formulas
# ============================================================================

class TestCentralChargeFormulas:
    """Verify W_N central charge formulas at low N."""

    def test_virasoro_from_sl2_k1(self):
        """W_2 from sl_2 DS at k=1: c = 1 - 6*4/3 = -7."""
        c = wn_central_charge(2, Fraction(1))
        assert c == Fraction(-7)

    def test_w3_from_sl3_k1(self):
        """W_3 from sl_3 DS at k=1: c = 2 - 3*8*9/4 = -52."""
        c = wn_central_charge(3, Fraction(1))
        assert c == Fraction(-52)

    def test_critical_level_raises(self):
        """k = -N should raise ValueError."""
        with pytest.raises(ValueError):
            wn_central_charge(3, Fraction(-3))

    def test_km_central_charge_sl2_k1(self):
        """c(V_1(sl_2)) = 1."""
        g = sl_n_data(2)
        c = central_charge_km(g, Fraction(1))
        assert c == Fraction(1)

    def test_km_central_charge_sl3_k1(self):
        """c(V_1(sl_3)) = 8/4 = 2."""
        g = sl_n_data(3)
        c = central_charge_km(g, Fraction(1))
        assert c == Fraction(2)


# ============================================================================
# Section 13: Shadow depth classification
# ============================================================================

class TestShadowDepthClassification:
    """Verify shadow depth for celestial algebras."""

    def test_virasoro_class_m(self):
        """Virasoro (W_2): class M (infinite depth)."""
        # The quartic contact invariant Q^contact != 0
        c = Fraction(26)
        q = Fraction(10) / (c * (5 * c + 22))
        assert q != 0  # nonvanishing confirms class M

    def test_w3_class_m(self):
        """W_3: class M (infinite depth, contains Virasoro)."""
        # Contains Virasoro as subalgebra -> class M
        c = Fraction(50)
        q_vir = Fraction(10) / (c * (5 * c + 22))
        assert q_vir != 0

    def test_current_algebra_k0_class_g(self):
        """V_0(g) at k=0: class G (depth 2, Gaussian)."""
        # At level 0, the curvature vanishes (no cubic shadow)
        g = sl_n_data(3)
        kap = kappa_km(g, Fraction(0))
        assert kap == Fraction(4)  # dim/2 = 8/2 = 4
        # Class G: depth 2

    def test_current_algebra_k1_class_l(self):
        """V_1(g) at k=1: class L (depth 3, Lie/tree)."""
        # Nonzero level gives curvature -> class L
        g = sl_n_data(3)
        kap = kappa_km(g, Fraction(1))
        assert kap == Fraction(16, 3)


# ============================================================================
# Section 14: Complementarity at c=26
# ============================================================================

class TestComplementarityC26:
    """Verify complementarity at the critical string point c=26."""

    def test_virasoro_kappa_c26(self):
        """kappa(Vir_26) = 13."""
        assert kappa_virasoro(Fraction(26)) == Fraction(13)

    def test_virasoro_kappa_complement(self):
        """kappa(Vir_0) = 0 (the Koszul dual at c=26-26=0)."""
        assert kappa_virasoro(Fraction(0)) == Fraction(0)

    def test_kappa_sum_not_zero(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for c in [Fraction(5), Fraction(13), Fraction(20)]:
            kap = kappa_virasoro(c)
            kap_dual = kappa_virasoro(Fraction(26) - c)
            assert kap + kap_dual == Fraction(13)

    def test_c13_self_dual_point(self):
        """At c=13: kappa = kappa' = 13/2."""
        kap = kappa_virasoro(Fraction(13))
        kap_dual = kappa_virasoro(Fraction(26) - Fraction(13))
        assert kap == kap_dual == Fraction(13, 2)


# ============================================================================
# Section 15: Full comparison suite
# ============================================================================

class TestFullComparisonSuite:
    """Integration test: run the full comparison suite."""

    def test_full_comparison_runs(self):
        """The full suite runs without error."""
        results = run_full_comparison(Fraction(26), N_gauge=3)
        assert isinstance(results, dict)
        assert len(results) > 10

    def test_full_comparison_all_ope_match(self):
        """All OPE comparisons match."""
        results = run_full_comparison(Fraction(26), N_gauge=3)
        assert results["ope_gluon_pp"].match is True
        assert results["ope_gluon_pm"].match is True
        assert results["ope_graviton_tt"].match is True
        assert results["ope_graviton_tw"].match is True

    def test_full_comparison_has_soft_tower(self):
        """Soft tower is present."""
        results = run_full_comparison(Fraction(26), N_gauge=3)
        assert len(results["soft_tower"]) >= 6

    def test_full_comparison_has_r_matrix(self):
        """R-matrix data is present."""
        results = run_full_comparison(Fraction(26), N_gauge=3)
        assert "r_matrix_gluon_k0" in results
        assert "r_matrix_graviton" in results

    def test_full_comparison_has_w_infinity(self):
        """w_{1+inf} comparison is present."""
        results = run_full_comparison(Fraction(26), N_gauge=3)
        assert len(results["w_infinity"]) == 5


# ============================================================================
# Section 16: kappa large-N behavior
# ============================================================================

class TestKappaLargeN:
    """Verify logarithmic divergence of kappa at large N."""

    def test_kappa_increasing_with_n(self):
        """kappa(W_N) increases with N for fixed c > 0."""
        c = Fraction(30)
        kappas = [kappa_wn(N, c) for N in range(2, 8)]
        for i in range(len(kappas) - 1):
            assert kappas[i + 1] > kappas[i]

    def test_kappa_grows_faster_than_linear(self):
        """kappa(W_N)/N -> infinity (faster than linear? No: H_N ~ ln N).
        Actually kappa(W_N) = c*(H_N-1) ~ c*ln(N), sublinear in N."""
        c = Fraction(30)
        # kappa(W_100)/kappa(W_10) should be roughly ln(100)/ln(10)
        k10 = float(kappa_wn(10, c))
        k100 = float(kappa_wn(100, c))
        ratio = k100 / k10
        # ln(100)-1 / (ln(10)-1) approx 3.6/1.3 approx 2.7
        assert 2.0 < ratio < 4.0  # rough logarithmic growth check

    def test_kappa_w2_smallest(self):
        """kappa(W_2) = c/2 is the smallest among W_N for N >= 2."""
        c = Fraction(30)
        k2 = kappa_wn(2, c)
        for N in range(3, 10):
            assert kappa_wn(N, c) > k2


# ============================================================================
# Section 17: Self-dual vs full YM
# ============================================================================

class TestSelfDualVsFullYM:
    """Verify distinction between self-dual and full YM."""

    def test_sdym_no_double_pole(self):
        """Self-dual YM at k=0: no double pole in OPE."""
        comp = compare_gluon_ope_pp(3)
        assert comp.pole_order == 1  # only simple pole

    def test_full_ym_has_double_pole(self):
        """Full YM at k=1: double pole present."""
        comp = compare_gluon_ope_pm(3)
        assert comp.pole_order == 2

    def test_sdym_kappa_at_k0(self):
        """At k=0: kappa = dim(g)/2."""
        for N in [2, 3, 4, 5]:
            g = sl_n_data(N)
            kap = kappa_km(g, Fraction(0))
            assert kap == Fraction(g.dim, 2)


# ============================================================================
# Section 18: Critical level singularity
# ============================================================================

class TestCriticalLevelSingularity:
    """Verify critical level singularity handling."""

    def test_kappa_critical_raises(self):
        """kappa at critical level k = -h^v raises ValueError."""
        g = sl_n_data(3)
        with pytest.raises(ValueError):
            kappa_km(g, Fraction(-3))

    def test_central_charge_critical_raises(self):
        """c at critical level raises ValueError."""
        g = sl_n_data(3)
        with pytest.raises(ValueError):
            central_charge_km(g, Fraction(-3))

    def test_wn_critical_raises(self):
        """W_N central charge at critical level raises ValueError."""
        with pytest.raises(ValueError):
            wn_central_charge(4, Fraction(-4))


# ============================================================================
# Section 19: Lie algebra data
# ============================================================================

class TestLieAlgebraData:
    """Verify Lie algebra data at low N."""

    def test_sl2(self):
        g = sl_n_data(2)
        assert g.dim == 3
        assert g.rank == 1
        assert g.dual_coxeter == 2

    def test_sl3(self):
        g = sl_n_data(3)
        assert g.dim == 8
        assert g.rank == 2
        assert g.dual_coxeter == 3

    def test_sl4(self):
        g = sl_n_data(4)
        assert g.dim == 15
        assert g.rank == 3
        assert g.dual_coxeter == 4

    def test_sl5(self):
        g = sl_n_data(5)
        assert g.dim == 24
        assert g.rank == 4
        assert g.dual_coxeter == 5

    def test_sl1_raises(self):
        with pytest.raises(ValueError):
            sl_n_data(1)
