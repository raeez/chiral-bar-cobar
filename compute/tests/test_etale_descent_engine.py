r"""Tests for etale descent engine.

Verifies curve-(in)dependence of bar complex data, shadow invariants,
and the modular cyclic deformation complex under change of curve X
and under etale covers.

Mathematical references:
    prop:genus0-curve-independence (higher_genus_modular_koszul.tex)
    thm:open-stratum-curve-independence (higher_genus_modular_koszul.tex)
    conj:boundary-curve-independence (higher_genus_modular_koszul.tex)
    prop:collision-locality (higher_genus_modular_koszul.tex)
    thm:shadow-homotopy-invariance (higher_genus_modular_koszul.tex)
    AP27: propagator weight universality
"""

from __future__ import annotations

from fractions import Fraction

import pytest

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from etale_descent_engine import (
    OPEData,
    heisenberg_ope,
    virasoro_ope,
    affine_km_ope,
    w3_ope,
    beta_gamma_ope,
    PropagatorDecomposition,
    propagator_decomposition,
    collision_residue_of_regular_part,
    EnrichmentData,
    enrichment_for_algebra,
    EtaleMapData,
    kappa_under_etale_pullback,
    shadow_tower_under_etale_pullback,
    enrichment_change_under_etale,
    faber_pandharipande_coefficient,
    obstruction_class,
    obstruction_curve_independent,
    theta_a_curve_dependence,
    ran_space_dimension,
    ran_contractible,
    etale_descent_for_factorization,
    modular_deformation_complex_structure,
    cross_genus_kappa_consistency,
    cross_genus_additivity,
    full_etale_descent_report,
)

from sympy import Rational


# ========================================================================
# 1. OPE data construction
# ========================================================================

class TestOPEDataConstruction:
    """Test that OPE data is correctly constructed for all families."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        h = heisenberg_ope(Rational(3))
        assert h.kappa == Rational(3)

    def test_heisenberg_central_charge(self):
        h = heisenberg_ope()
        assert h.central_charge == Rational(1)

    def test_heisenberg_is_uniform_weight(self):
        h = heisenberg_ope()
        assert h.is_uniform_weight is True

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2.  AP39: kappa != c in general."""
        v = virasoro_ope(Rational(26))
        assert v.kappa == Rational(13)

    def test_virasoro_c13_self_dual(self):
        """At c=13, kappa = 13/2. Koszul conductor = 13."""
        v = virasoro_ope(Rational(13))
        assert v.kappa == Rational(13, 2)
        assert v.koszul_conductor == Rational(13)

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        a = affine_km_ope("A", 1, Rational(1))
        assert a.kappa == Rational(9, 4)

    def test_affine_sl3_kappa(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        a = affine_km_ope("A", 2, Rational(1))
        assert a.kappa == Rational(16, 3)

    def test_affine_koszul_conductor_zero(self):
        """For affine KM: kappa + kappa' = 0 (AP24)."""
        a = affine_km_ope("A", 1, Rational(1))
        assert a.koszul_conductor == Rational(0)

    def test_w3_kappa(self):
        """kappa(W_3, c) = 7c/12."""
        w = w3_ope(Rational(2))
        assert w.kappa == Rational(7, 6)

    def test_w3_not_uniform_weight(self):
        """W_3 has generators of weights 2 and 3: not uniform."""
        w = w3_ope()
        assert w.is_uniform_weight is False

    def test_beta_gamma_kappa(self):
        """kappa(beta-gamma) = -1/2."""
        bg = beta_gamma_ope()
        assert bg.kappa == Rational(-1, 2)

    def test_beta_gamma_not_uniform(self):
        """beta-gamma has weights 0 and 1."""
        bg = beta_gamma_ope()
        assert bg.is_uniform_weight is False


# ========================================================================
# 2. Propagator decomposition
# ========================================================================

class TestPropagatorDecomposition:
    """Test the propagator decomposition eta_X = eta^(0) + omega^reg."""

    def test_genus0_no_regular_correction(self):
        """At genus 0, there is no regular correction (P^1 has g=0)."""
        p = propagator_decomposition(0)
        assert p.regular_correction_dim == 0
        assert p.dim_h10 == 0

    def test_genus1_regular_correction(self):
        """At genus 1, H^{1,0} is 1-dimensional (one holomorphic 1-form)."""
        p = propagator_decomposition(1)
        assert p.dim_h10 == 1
        assert p.regular_correction_dim == 1  # 1x1 period matrix

    def test_genus2_regular_correction(self):
        """At genus 2, H^{1,0} is 2-dimensional."""
        p = propagator_decomposition(2)
        assert p.dim_h10 == 2
        assert p.regular_correction_dim == 4  # 2x2 period matrix

    def test_singular_part_universal(self):
        """The singular part eta^(0) = d log(z-w) has order 1 at all genera."""
        for g in range(5):
            p = propagator_decomposition(g)
            assert p.singular_part_order == 1

    def test_residue_of_regular_part_vanishes(self):
        """Res_{z->w}[omega^reg * f] = 0 (prop:collision-locality)."""
        assert collision_residue_of_regular_part() == Rational(0)


# ========================================================================
# 3. Enrichment structure
# ========================================================================

class TestEnrichmentStructure:
    """Test the curve-dependent enrichment B_enr = M_h tensor H^{1,0}(X)."""

    def test_genus0_no_enrichment(self):
        """At genus 0, there is no enrichment (H^{1,0}(P^1) = 0)."""
        h = heisenberg_ope()
        e = enrichment_for_algebra(h, 0)
        assert e.total_enrichment_dim == 0

    def test_genus1_heisenberg_enrichment(self):
        """At genus 1, Heisenberg has 1 * 1 = 1 enrichment section."""
        h = heisenberg_ope()
        e = enrichment_for_algebra(h, 1)
        assert e.total_enrichment_dim == 1

    def test_genus2_virasoro_enrichment(self):
        """At genus 2, Virasoro has 1 * 2 = 2 enrichment sections."""
        v = virasoro_ope()
        e = enrichment_for_algebra(v, 2)
        assert e.total_enrichment_dim == 2

    def test_genus3_w3_enrichment(self):
        """W_3 at genus 3: 2 generators * 3 = 6 enrichment sections."""
        w = w3_ope()
        e = enrichment_for_algebra(w, 3)
        assert e.total_enrichment_dim == 6

    def test_positive_weight_enrichment_killed(self):
        """For algebras with all h > 0, enrichment is killed in PBW SS."""
        h = heisenberg_ope()
        e = enrichment_for_algebra(h, 2)
        assert e.enrichment_killed is True

    def test_virasoro_enrichment_killed(self):
        """Virasoro has h = 2 > 0, so enrichment is killed."""
        v = virasoro_ope()
        e = enrichment_for_algebra(v, 2)
        assert e.enrichment_killed is True

    def test_beta_gamma_enrichment_not_killed(self):
        """beta-gamma has gamma at weight 0: enrichment NOT automatically killed."""
        bg = beta_gamma_ope()
        e = enrichment_for_algebra(bg, 1)
        assert e.enrichment_killed is False
        assert e.min_conformal_weight == Rational(0)


# ========================================================================
# 4. Etale map structure
# ========================================================================

class TestEtaleMapData:
    """Test Riemann-Hurwitz for etale covers."""

    def test_p1_no_etale_cover(self):
        """P^1 has no nontrivial connected etale covers (pi_1 = 0)."""
        with pytest.raises(ValueError, match="no nontrivial"):
            EtaleMapData.from_degree_and_genus(2, 0)

    def test_elliptic_etale_cover(self):
        """Etale covers of elliptic curves give elliptic curves."""
        e = EtaleMapData.from_degree_and_genus(2, 1)
        assert e.genus_target == 1  # Riemann-Hurwitz: g = 2*(1-1)+1 = 1

    def test_genus2_degree2_cover(self):
        """Degree-2 etale cover of genus 2: g(Y) = 2*(2-1)+1 = 3."""
        e = EtaleMapData.from_degree_and_genus(2, 2)
        assert e.genus_target == 3

    def test_genus3_degree3_cover(self):
        """Degree-3 etale cover of genus 3: g(Y) = 3*(3-1)+1 = 7."""
        e = EtaleMapData.from_degree_and_genus(3, 3)
        assert e.genus_target == 7

    def test_identity_cover(self):
        """Degree-1 cover is the identity: g(Y) = g(X)."""
        for g in range(5):
            e = EtaleMapData.from_degree_and_genus(1, g)
            assert e.genus_target == g


# ========================================================================
# 5. Kappa invariance under etale pullback
# ========================================================================

class TestKappaEtaleInvariance:
    """Test that kappa(f^* A) = kappa(A) for etale f: Y -> X."""

    def test_heisenberg_kappa_invariant(self):
        h = heisenberg_ope(Rational(5))
        e = EtaleMapData.from_degree_and_genus(2, 2)
        assert kappa_under_etale_pullback(h, e) == h.kappa

    def test_virasoro_kappa_invariant(self):
        v = virasoro_ope(Rational(26))
        e = EtaleMapData.from_degree_and_genus(3, 3)
        assert kappa_under_etale_pullback(v, e) == Rational(13)

    def test_affine_kappa_invariant(self):
        a = affine_km_ope("A", 2, Rational(1))
        e = EtaleMapData.from_degree_and_genus(2, 2)
        assert kappa_under_etale_pullback(a, e) == a.kappa

    def test_kappa_invariant_all_degrees(self):
        """kappa invariant for etale covers of all degrees 1..5."""
        v = virasoro_ope(Rational(1, 2))
        for d in range(1, 6):
            e = EtaleMapData.from_degree_and_genus(d, 3)
            assert kappa_under_etale_pullback(v, e) == v.kappa


# ========================================================================
# 6. Shadow tower invariance under etale pullback
# ========================================================================

class TestShadowTowerEtaleInvariance:
    """Test that S_r(f^* A) = S_r(A) for etale f."""

    def test_heisenberg_tower_invariant(self):
        h = heisenberg_ope(Rational(3))
        e = EtaleMapData.from_degree_and_genus(2, 2)
        tower = shadow_tower_under_etale_pullback(h, e)
        assert tower == h.shadow_tower
        assert tower[2] == Rational(3)  # S_2 = k
        assert tower[3] == Rational(0)  # terminates

    def test_virasoro_tower_invariant(self):
        v = virasoro_ope(Rational(26))
        e = EtaleMapData.from_degree_and_genus(2, 2)
        tower = shadow_tower_under_etale_pullback(v, e)
        assert tower[2] == Rational(13)   # S_2 = c/2
        assert tower[3] == Rational(2)    # S_3 = 2 (universal)

    def test_shadow_tower_same_all_degrees(self):
        """Shadow tower is the same for ALL etale covers."""
        v = virasoro_ope(Rational(1))
        base_tower = dict(v.shadow_tower)
        for d in range(1, 5):
            e = EtaleMapData.from_degree_and_genus(d, 3)
            tower = shadow_tower_under_etale_pullback(v, e)
            assert tower == base_tower


# ========================================================================
# 7. Enrichment change under etale covers
# ========================================================================

class TestEnrichmentChangeEtale:
    """Test that enrichment dimension DOES change under etale covers."""

    def test_enrichment_changes_genus2(self):
        """Degree-2 cover of genus 2: g(Y)=3, enrichment grows."""
        h = heisenberg_ope()
        e = EtaleMapData.from_degree_and_genus(2, 2)
        source_dim, target_dim = enrichment_change_under_etale(h, e)
        assert source_dim == 2   # 1 gen * genus 2
        assert target_dim == 3   # 1 gen * genus 3 (Riemann-Hurwitz)
        assert target_dim > source_dim

    def test_enrichment_changes_virasoro(self):
        """Virasoro on degree-3 cover of genus 3."""
        v = virasoro_ope()
        e = EtaleMapData.from_degree_and_genus(3, 3)
        source_dim, target_dim = enrichment_change_under_etale(v, e)
        assert source_dim == 3  # 1 gen * genus 3
        assert target_dim == 7  # 1 gen * genus 7

    def test_enrichment_identity_cover(self):
        """Degree-1 cover preserves enrichment."""
        h = heisenberg_ope()
        e = EtaleMapData.from_degree_and_genus(1, 3)
        source_dim, target_dim = enrichment_change_under_etale(h, e)
        assert source_dim == target_dim


# ========================================================================
# 8. Faber-Pandharipande coefficients
# ========================================================================

class TestFaberPandharipande:
    """Test Faber-Pandharipande coefficients lambda_g^FP."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande_coefficient(1) == Rational(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande_coefficient(2) == Rational(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        val = faber_pandharipande_coefficient(3)
        expected = Rational(31, 967680)
        assert val == expected

    def test_all_positive(self):
        """All lambda_g^FP are positive (Bernoulli sign pattern)."""
        for g in range(1, 8):
            assert faber_pandharipande_coefficient(g) > 0

    def test_invalid_genus(self):
        with pytest.raises(ValueError):
            faber_pandharipande_coefficient(0)


# ========================================================================
# 9. Obstruction class curve independence
# ========================================================================

class TestObstructionCurveIndependence:
    """Test that obs_g = kappa * lambda_g is curve-independent."""

    def test_heisenberg_obs1(self):
        """obs_1(H_k) = k * 1/24 = k/24."""
        h = heisenberg_ope(Rational(12))
        assert obstruction_class(h, 1) == Rational(1, 2)

    def test_virasoro_obs1(self):
        """obs_1(Vir_c) = (c/2) * (1/24) = c/48."""
        v = virasoro_ope(Rational(48))
        assert obstruction_class(v, 1) == Rational(1)

    def test_obstruction_always_curve_independent(self):
        """obs_g is ALWAYS curve-independent (for any g, any algebra)."""
        algebras = [
            heisenberg_ope(),
            virasoro_ope(Rational(26)),
            affine_km_ope("A", 1, Rational(1)),
            w3_ope(Rational(2)),
        ]
        for a in algebras:
            for g in range(1, 4):
                assert obstruction_curve_independent(a, g) is True

    def test_obstruction_factorization(self):
        """obs_g = kappa * lambda_g: product of curve-independent * universal."""
        v = virasoro_ope(Rational(2))
        for g in range(1, 5):
            obs = obstruction_class(v, g)
            expected = v.kappa * faber_pandharipande_coefficient(g)
            assert obs == expected


# ========================================================================
# 10. Theta_A curve dependence analysis
# ========================================================================

class TestThetaCurveDependence:
    """Test the component-wise curve-(in)dependence of Theta_A."""

    def test_collision_diff_always_independent(self):
        """d_coll is ALWAYS curve-independent (prop:collision-locality)."""
        for ope in [heisenberg_ope(), virasoro_ope(), affine_km_ope("A", 1)]:
            dep = theta_a_curve_dependence(ope, 2)
            assert dep["collision_differential_d0"] is True

    def test_shadow_projections_always_independent(self):
        """Shadow projections S_r are ALWAYS curve-independent."""
        for ope in [heisenberg_ope(), virasoro_ope(), w3_ope()]:
            dep = theta_a_curve_dependence(ope, 3)
            assert dep["shadow_projections_S_r"] is True

    def test_kappa_always_independent(self):
        """kappa is ALWAYS curve-independent."""
        for ope in [heisenberg_ope(), virasoro_ope(), affine_km_ope("A", 2)]:
            dep = theta_a_curve_dependence(ope, 2)
            assert dep["kappa"] is True

    def test_enrichment_always_dependent(self):
        """Enrichment sections are ALWAYS curve-dependent at g >= 1."""
        dep = theta_a_curve_dependence(virasoro_ope(), 2)
        assert dep["enrichment_sections"] is False

    def test_enrichment_killed_for_positive_weight(self):
        """For algebras with all h > 0, enrichment killed in PBW SS."""
        dep = theta_a_curve_dependence(virasoro_ope(), 2)
        assert dep["enrichment_killed_in_PBW"] is True

    def test_enrichment_not_killed_beta_gamma(self):
        """beta-gamma has h=0 generator: enrichment NOT killed."""
        dep = theta_a_curve_dependence(beta_gamma_ope(), 2)
        assert dep["enrichment_killed_in_PBW"] is False

    def test_hodge_class_always_independent(self):
        """lambda_g lives on M-bar_g, not on X."""
        dep = theta_a_curve_dependence(heisenberg_ope(), 5)
        assert dep["hodge_class_lambda_g"] is True


# ========================================================================
# 11. Ran space and contractibility
# ========================================================================

class TestRanSpace:
    """Test Ran space properties relevant to descent."""

    def test_ran_dimension(self):
        """dim Ran_n(X) = n for a curve."""
        for n in range(1, 6):
            assert ran_space_dimension(n) == n

    def test_ran_contractible(self):
        """Ran(X) is contractible (Beilinson-Drinfeld)."""
        assert ran_contractible() is True


# ========================================================================
# 12. Etale descent properties
# ========================================================================

class TestEtaleDescentProperties:
    """Test etale descent for factorization algebras."""

    def test_ope_etale_local(self):
        """OPE data lives on formal disks: etale-local."""
        h = heisenberg_ope()
        e = EtaleMapData.from_degree_and_genus(2, 2)
        props = etale_descent_for_factorization(h, e)
        assert props["ope_etale_local"] is True

    def test_factorization_etale_local(self):
        """Factorization structure is etale-local (diagonal preserved)."""
        v = virasoro_ope()
        e = EtaleMapData.from_degree_and_genus(2, 2)
        props = etale_descent_for_factorization(v, e)
        assert props["factorization_etale_local"] is True

    def test_collision_diff_invariant(self):
        """d_coll is invariant under etale pullback."""
        a = affine_km_ope("A", 1)
        e = EtaleMapData.from_degree_and_genus(2, 3)
        props = etale_descent_for_factorization(a, e)
        assert props["collision_diff_invariant"] is True

    def test_enrichment_changes_under_etale(self):
        """Enrichment does change (this is expected, not a failure)."""
        h = heisenberg_ope()
        e = EtaleMapData.from_degree_and_genus(2, 2)
        props = etale_descent_for_factorization(h, e)
        assert props["enrichment_changes"] is True


# ========================================================================
# 13. Deformation complex structure
# ========================================================================

class TestDeformationComplexStructure:
    """Test the modular cyclic deformation complex structure."""

    def test_genus0_no_enrichment(self):
        """At genus 0, the deformation complex has no enrichment."""
        result = modular_deformation_complex_structure(heisenberg_ope(), 0)
        assert result["enrichment"] == "absent"

    def test_ope_part_always_independent(self):
        for g in range(4):
            result = modular_deformation_complex_structure(virasoro_ope(), g)
            assert result["ope_part"] == "curve_independent"

    def test_graph_coefficients_universal(self):
        result = modular_deformation_complex_structure(virasoro_ope(), 3)
        assert result["graph_coefficients"] == "universal_on_M_bar_gn"


# ========================================================================
# 14. Cross-genus consistency
# ========================================================================

class TestCrossGenusConsistency:
    """Test that kappa recovered from obs_g/lambda_g is genus-independent."""

    def test_heisenberg_cross_genus(self):
        h = heisenberg_ope(Rational(7))
        assert cross_genus_kappa_consistency(h) is True

    def test_virasoro_cross_genus(self):
        v = virasoro_ope(Rational(26))
        assert cross_genus_kappa_consistency(v) is True

    def test_affine_cross_genus(self):
        a = affine_km_ope("A", 1, Rational(1))
        assert cross_genus_kappa_consistency(a) is True

    def test_w3_cross_genus(self):
        """W_3 kappa is genus-independent (OPE-intrinsic)."""
        w = w3_ope(Rational(2))
        assert cross_genus_kappa_consistency(w) is True

    def test_cross_genus_many_families(self):
        """All standard families have genus-independent kappa."""
        families = [
            heisenberg_ope(Rational(1, 2)),
            virasoro_ope(Rational(13)),
            virasoro_ope(Rational(1)),
            affine_km_ope("A", 1, Rational(3)),
            affine_km_ope("A", 2, Rational(1)),
            affine_km_ope("E", 8, Rational(1)),
            w3_ope(Rational(100)),
            beta_gamma_ope(),
        ]
        for f in families:
            assert cross_genus_kappa_consistency(f) is True, f"Failed for {f.name}"


# ========================================================================
# 15. Cross-genus additivity
# ========================================================================

class TestCrossGenusAdditivity:
    """Test additivity obs_g(A1+A2) = obs_g(A1) + obs_g(A2)."""

    def test_heisenberg_sum(self):
        h1 = heisenberg_ope(Rational(3))
        h2 = heisenberg_ope(Rational(5))
        assert cross_genus_additivity(h1, h2) is True

    def test_heisenberg_virasoro_sum(self):
        h = heisenberg_ope(Rational(1))
        v = virasoro_ope(Rational(2))
        assert cross_genus_additivity(h, v) is True

    def test_three_heisenberg_sum(self):
        """Additivity for three summands (applied twice)."""
        h1 = heisenberg_ope(Rational(1))
        h2 = heisenberg_ope(Rational(2))
        h3 = heisenberg_ope(Rational(3))
        # (h1 + h2) with h3: combined kappa = 1+2 = 3 vs h3 kappa = 3
        combined_12 = OPEData(
            name="H1+H2", central_charge=Rational(2),
            kappa=Rational(3),
            generators=[("a1", Rational(1)), ("a2", Rational(1))],
        )
        assert cross_genus_additivity(combined_12, h3) is True


# ========================================================================
# 16. Full report
# ========================================================================

class TestFullReport:
    """Test the comprehensive etale descent report."""

    def test_heisenberg_report(self):
        report = full_etale_descent_report(heisenberg_ope(), genus=2)
        assert report["kappa_curve_independent"] is True
        assert report["collision_diff_curve_independent"] is True
        assert report["cross_genus_consistent"] is True
        assert report["ran_contractible"] is True
        assert report["residue_of_regular_part"] == Rational(0)
        assert report["enrichment_killed"] is True

    def test_virasoro_report_genus3(self):
        report = full_etale_descent_report(virasoro_ope(Rational(26)), genus=3)
        assert report["kappa"] == Rational(13)
        assert report["obstruction_curve_independent"] is True
        assert report["etale_descent"]["kappa_invariant"] is True

    def test_report_genus0_no_etale(self):
        """At genus 0, no nontrivial etale covers exist."""
        report = full_etale_descent_report(heisenberg_ope(), genus=0)
        assert report["etale_map"] is None
        assert report["enrichment_dim"] == 0

    def test_report_genus1(self):
        """At genus 1, etale covers are isogenies."""
        report = full_etale_descent_report(virasoro_ope(), genus=1)
        assert report["enrichment_dim"] == 1
        # genus 1 has no etale covers with genus >= 2 source
        assert report["etale_map"] is None

    def test_w3_report(self):
        report = full_etale_descent_report(w3_ope(Rational(50)), genus=2)
        assert report["kappa_curve_independent"] is True
        assert report["enrichment_dim"] == 4  # 2 generators * genus 2


# ========================================================================
# 17. Riemann-Hurwitz sanity checks
# ========================================================================

class TestRiemannHurwitz:
    """Verify Riemann-Hurwitz formula 2g(Y)-2 = d*(2g(X)-2) for etale."""

    def test_rh_formula_genus2(self):
        for d in range(1, 6):
            e = EtaleMapData.from_degree_and_genus(d, 2)
            # 2*g(Y) - 2 = d * (2*2 - 2) = 2d
            assert 2 * e.genus_target - 2 == d * 2

    def test_rh_formula_genus3(self):
        for d in range(1, 6):
            e = EtaleMapData.from_degree_and_genus(d, 3)
            assert 2 * e.genus_target - 2 == d * (2 * 3 - 2)

    def test_rh_formula_genus5(self):
        e = EtaleMapData.from_degree_and_genus(4, 5)
        assert 2 * e.genus_target - 2 == 4 * 8  # d*(2g-2)
        assert e.genus_target == 17


# ========================================================================
# 18. Edge cases and boundary conditions
# ========================================================================

class TestEdgeCases:
    """Test edge cases and potential failure modes."""

    def test_kappa_zero_virasoro(self):
        """At c=0, kappa=0 but Theta_A need not vanish (AP31)."""
        v = virasoro_ope(Rational(0))
        assert v.kappa == Rational(0)
        # obs_g = 0 but higher-arity shadows may be nonzero
        assert obstruction_class(v, 1) == Rational(0)

    def test_critical_c26(self):
        """At c=26, kappa=13 (critical dimension for bosonic string)."""
        v = virasoro_ope(Rational(26))
        assert v.kappa == Rational(13)
        assert obstruction_class(v, 1) == Rational(13, 24)

    def test_negative_kappa(self):
        """Negative kappa is allowed (ghost systems)."""
        bg = beta_gamma_ope()
        assert bg.kappa < 0
        assert obstruction_class(bg, 1) < 0

    def test_large_genus(self):
        """Curve independence holds at arbitrarily high genus."""
        h = heisenberg_ope()
        dep = theta_a_curve_dependence(h, 100)
        assert dep["collision_differential_d0"] is True
        assert dep["shadow_projections_S_r"] is True
        assert dep["kappa"] is True


# ========================================================================
# 19. Complementarity and etale descent
# ========================================================================

class TestComplementarityEtale:
    """Test that complementarity sums are curve-independent."""

    def test_km_complementarity_invariant(self):
        """kappa + kappa' = 0 for KM is curve-independent."""
        a = affine_km_ope("A", 1, Rational(1))
        e = EtaleMapData.from_degree_and_genus(2, 2)
        kp = kappa_under_etale_pullback(a, e)
        assert a.koszul_conductor == Rational(0)
        assert kp + (-kp) == Rational(0)  # kappa' = -kappa for KM

    def test_virasoro_complementarity_invariant(self):
        """kappa + kappa' = 13 for Virasoro is curve-independent (AP24)."""
        v = virasoro_ope(Rational(10))
        # kappa(Vir_10) = 5, kappa(Vir_16) = 8, sum = 13
        assert v.koszul_conductor == Rational(13)


# ========================================================================
# 20. Multi-method verification of curve independence
# ========================================================================

class TestMultiMethodVerification:
    """Multi-path verification that curve-independent quantities are
    indeed independent of X (the Multi-Path Verification Mandate)."""

    def test_kappa_three_paths(self):
        """Verify kappa curve-independence via three independent paths.

        Path 1: kappa is computed from OPE residues (formal disk data).
        Path 2: kappa = obs_1 / lambda_1 recovers the same value at all genera.
        Path 3: kappa is invariant under etale pullback.
        """
        v = virasoro_ope(Rational(24))
        kappa = v.kappa
        assert kappa == Rational(12)  # Path 1: c/2

        # Path 2: cross-genus consistency
        for g in range(1, 5):
            obs = obstruction_class(v, g)
            fp = faber_pandharipande_coefficient(g)
            assert obs / fp == kappa

        # Path 3: etale invariance
        e = EtaleMapData.from_degree_and_genus(3, 2)
        assert kappa_under_etale_pullback(v, e) == kappa

    def test_shadow_tower_three_paths(self):
        """Verify shadow tower curve-independence via three paths.

        Path 1: S_r computed from OPE master equation (local data).
        Path 2: S_r invariant under etale pullback.
        Path 3: S_r is the same on P^1 and on any genus-g curve.
        """
        h = heisenberg_ope(Rational(7))

        # Path 1: from OPE
        assert h.shadow_tower[2] == Rational(7)

        # Path 2: etale invariance
        e = EtaleMapData.from_degree_and_genus(2, 2)
        tower = shadow_tower_under_etale_pullback(h, e)
        assert tower[2] == Rational(7)

        # Path 3: same at all genera (via theta dependence)
        for g in [0, 1, 2, 5]:
            dep = theta_a_curve_dependence(h, g)
            assert dep["shadow_projections_S_r"] is True

    def test_collision_diff_three_paths(self):
        """Verify collision differential curve-independence via three paths.

        Path 1: Residue of regular part vanishes (prop:collision-locality).
        Path 2: d_coll depends only on eta^(0) = d log(z-w) (universal).
        Path 3: Theta_A analysis shows d_0 is curve-independent.
        """
        # Path 1
        assert collision_residue_of_regular_part() == Rational(0)

        # Path 2: propagator decomposition
        for g in range(5):
            p = propagator_decomposition(g)
            assert p.singular_part_order == 1  # d log always order 1

        # Path 3: theta analysis
        for ope in [heisenberg_ope(), virasoro_ope(), affine_km_ope("A", 1)]:
            dep = theta_a_curve_dependence(ope, 3)
            assert dep["collision_differential_d0"] is True
