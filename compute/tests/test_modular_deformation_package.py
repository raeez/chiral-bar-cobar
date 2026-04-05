"""Tests for compute/lib/modular_deformation_package.py — modular deformation package.

Validates:
  1. Genus-completed tensor product structure and MC convergence
  2. Five-component differential D = d_int + [tau,-] + d_sew + d_pf + hbar*Delta
  3. D^2 = 0 at convolution and ambient levels
  4. Bar-intrinsic MC element Theta_A := D_A - d_0
  5. Shadow extraction: kappa, cubic, quartic for standard families
  6. Clutching factorization (separating and non-separating)
  7. Verdier duality: D(Theta_A) = Theta_{A!}, complementarity
  8. Genus bootstrap: inductive genus determination
  9. Genus spectral sequence E_1 page
  10. Quantum L-infinity MC equation
  11. Free energy from graph sums and universal formula
  12. Independent sum factorization (prop:independent-sum-factorization)
  13. Stable graph census and genus filtration

References:
  - higher_genus_modular_koszul.tex: thm:mc2-bar-intrinsic,
    thm:convolution-d-squared-zero, thm:ambient-d-squared-zero,
    def:modular-cyclic-deformation-complex, def:stable-graph-coefficient-algebra,
    cor:shadow-extraction, prop:independent-sum-factorization,
    thm:cubic-gauge-triviality
  - concordance.tex: const:vol1-genus-spectral-sequence,
    const:vol1-modular-tangent-complex
"""

import pytest
from fractions import Fraction

from compute.lib.modular_deformation_package import (
    ModularCoefficientAlgebra,
    CyclicDeformationComplexData,
    CompletedTensorProduct,
    FiveComponentDifferential,
    DSquaredVerification,
    BarIntrinsicMC,
    ShadowExtraction,
    ClutchingFactorization,
    VerdierDuality,
    GenusBootstrap,
    QuantumLInfinityMC,
    ModularDeformationPackage,
    heisenberg_package,
    affine_sl2_package,
    betagamma_package,
    virasoro_package,
    scalar_free_energy,
    scalar_free_energy_from_graphs,
    genus2_graph_amplitudes,
    kappa_standard_landscape,
    stable_graph_census,
    verify_genus_filtration_bracket,
    verify_independent_sum_factorization,
    verify_complementarity_slN_landscape,
    verify_modular_deformation_package,
)
from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
    _bernoulli_exact,
    _lambda_fp_exact,
)


# ===================================================================
# Section 1: ModularCoefficientAlgebra (G_mod)
# ===================================================================

class TestModularCoefficientAlgebra:
    """Tests for the modular graph coefficient algebra G_mod."""

    def setup_method(self):
        self.G = ModularCoefficientAlgebra(max_genus=3)

    def test_graph_count_g0_n3(self):
        """G_mod^{(0)} at n=3: 1 stable graph (single vertex)."""
        assert self.G.graph_count(0, 3) == 1

    def test_graph_count_g0_n4(self):
        """G_mod^{(0)} at n=4: 4 stable graphs (1 smooth + 3 channels)."""
        assert self.G.graph_count(0, 4) == 4

    def test_graph_count_g1_n0(self):
        """G_mod^{(1)} at n=0: 2 stable graphs (smooth + self-loop)."""
        assert self.G.graph_count(1, 0) == 2

    def test_graph_count_g1_n1(self):
        """G_mod^{(1)} at n=1: 2 stable graphs."""
        assert self.G.graph_count(1, 1) == 2

    def test_graph_count_g2_n0(self):
        """G_mod^{(2)} at n=0: 6 stable graphs."""
        assert self.G.graph_count(2, 0) == 6

    def test_unstable_empty(self):
        """Unstable (g,n) pairs have no graphs."""
        assert self.G.graph_count(0, 0) == 0
        assert self.G.graph_count(0, 1) == 0
        assert self.G.graph_count(0, 2) == 0

    def test_genus_filtration_bracket(self):
        """[G^{m1}, G^{m2}] subset G^{m1+m2}: bracket respects filtration."""
        assert self.G.genus_filtration_respects_bracket(0, 0)
        assert self.G.genus_filtration_respects_bracket(1, 1)
        assert self.G.genus_filtration_respects_bracket(0, 2)

    def test_graph_amplitude_scalar_heisenberg(self):
        """Scalar amplitude for smooth genus-2: kappa^0 = 1."""
        gamma = StableGraph(vertex_genera=(2,), edges=(), legs=())
        assert self.G.graph_amplitude_scalar(gamma, Fraction(1, 2)) == Fraction(1)

    def test_weighted_amplitude_banana(self):
        """Weighted amplitude for banana (2 self-loops): kappa^2/8."""
        gamma = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        kappa = Fraction(1, 2)
        expected = kappa ** 2 / Fraction(8)
        assert self.G.weighted_amplitude(gamma, kappa) == expected

    def test_weighted_amplitude_theta(self):
        """Weighted amplitude for theta graph (3 parallel edges): kappa^3/12."""
        gamma = StableGraph(
            vertex_genera=(0, 0), edges=((0, 1), (0, 1), (0, 1)), legs=()
        )
        kappa = Fraction(1, 2)
        expected = kappa ** 3 / Fraction(12)
        assert self.G.weighted_amplitude(gamma, kappa) == expected


# ===================================================================
# Section 2: CompletedTensorProduct
# ===================================================================

class TestCompletedTensorProduct:
    """Tests for the genus-completed tensor product L ⊗̂ G_mod."""

    def setup_method(self):
        self.cdc = CyclicDeformationComplexData(
            lie_algebra_dim=3,
            structure_constants=None,
            killing_form=None,
            level=Fraction(1),
            family="affine",
        )
        self.G = ModularCoefficientAlgebra(max_genus=3)
        self.tp = CompletedTensorProduct(
            deformation_complex=self.cdc,
            coefficient_algebra=self.G,
            max_genus=3,
        )

    def test_mc_convergence_all_genera(self):
        """MC equation converges at each genus (finite sum)."""
        for g in range(4):
            assert self.tp.mc_equation_finite_at_genus(g)

    def test_bracket_genus_components_g0(self):
        """At genus 0: only (0,0) pair."""
        comps = self.tp.bracket_genus_components(0)
        assert comps == [(0, 0)]

    def test_bracket_genus_components_g1(self):
        """At genus 1: (0,1) and (1,0) pairs."""
        comps = self.tp.bracket_genus_components(1)
        assert comps == [(0, 1), (1, 0)]

    def test_bracket_genus_components_g2(self):
        """At genus 2: (0,2), (1,1), (2,0) pairs."""
        comps = self.tp.bracket_genus_components(2)
        assert comps == [(0, 2), (1, 1), (2, 0)]


# ===================================================================
# Section 3: FiveComponentDifferential
# ===================================================================

class TestFiveComponentDifferential:
    """Tests for D = d_int + [tau,-] + d_sew + d_pf + hbar*Delta."""

    def setup_method(self):
        self.D = FiveComponentDifferential()

    def test_d_int_preserves_genus(self):
        assert self.D.d_int_preserves_genus()

    def test_tau_preserves_genus(self):
        assert self.D.tau_bracket_preserves_genus()

    def test_d_sew_preserves_genus(self):
        assert self.D.d_sew_preserves_genus()

    def test_d_pf_preserves_genus(self):
        assert self.D.d_pf_preserves_genus()

    def test_delta_raises_genus(self):
        assert self.D.delta_raises_genus()

    def test_genus_grading_compatibility(self):
        """All components respect genus grading."""
        result = self.D.verify_genus_grading_compatibility()
        assert all(result.values())

    def test_d_squared_cross_terms_structure(self):
        """Cross-term identity is the codim-2 cancellation."""
        ct = self.D.d_squared_cross_terms()
        assert "d_int_squared" in ct
        assert "delta_squared" in ct
        assert "d_sew_d_pf_cross" in ct


# ===================================================================
# Section 4: D^2 = 0 verification
# ===================================================================

class TestDSquaredZero:
    """Tests for D^2 = 0 at convolution and ambient levels."""

    def setup_method(self):
        self.d2v = DSquaredVerification()

    def test_convolution_d_squared_zero(self):
        """D^2 = 0 at convolution level (from del^2 = 0 on M-bar_{g,n})."""
        assert self.d2v.convolution_d_squared_zero()

    def test_ambient_d_squared_zero(self):
        """D^2 = 0 at ambient level (thm:ambient-d-squared-zero)."""
        assert self.d2v.ambient_d_squared_zero()

    def test_cross_term_identity(self):
        """Critical cross-term: [d_sew, d_pf] + [d_int, hbar*Delta] + ... = 0."""
        result = self.d2v.verify_cross_term_identity()
        assert "identity" in result
        assert "mechanism" in result

    def test_genus_0_d_squared(self):
        """At genus 0, D^2 = 0 reduces to d_CE^2 = 0 (Jacobi)."""
        result = self.d2v.verify_at_genus_0()
        assert result["d_int_squared_zero"]
        assert result["twisted_d_squared_zero"]

    def test_genus_1_structure(self):
        """At genus 1, non-separating clutching produces curvature."""
        result = self.d2v.verify_at_genus_1()
        assert result["delta_from_genus_0"]
        assert result["curvature_proportional_to_kappa"]


# ===================================================================
# Section 5: BarIntrinsicMC (Theta_A := D_A - d_0)
# ===================================================================

class TestBarIntrinsicMC:
    """Tests for the bar-intrinsic MC element (thm:mc2-bar-intrinsic)."""

    def test_heisenberg_mc(self):
        """Heisenberg: Theta_A satisfies MC because D_A^2 = 0."""
        mc = BarIntrinsicMC("heisenberg", Fraction(1), 2, "G")
        assert mc.mc_from_d_squared_zero()

    def test_affine_mc(self):
        """Affine sl_2: Theta_A satisfies MC."""
        mc = BarIntrinsicMC("affine", Fraction(9, 4), 3, "L")
        assert mc.mc_from_d_squared_zero()

    def test_virasoro_mc(self):
        """Virasoro: Theta_A satisfies MC (infinite shadow obstruction tower)."""
        mc = BarIntrinsicMC("virasoro", Fraction(1, 2), None, "M")
        assert mc.mc_from_d_squared_zero()

    def test_genus_0_mc_equation(self):
        """Genus-0 MC equation: d_0(Theta^{(0)}) + 1/2[Theta^{(0)}, Theta^{(0)}] = 0."""
        mc = BarIntrinsicMC("heisenberg", Fraction(1), 2, "G")
        result = mc.genus_g_mc_equation(0)
        assert result["genus"] == 0
        assert result["non_separating"] is None

    def test_genus_1_mc_equation(self):
        """Genus-1 MC equation has non-separating term from genus 0."""
        mc = BarIntrinsicMC("heisenberg", Fraction(1), 2, "G")
        result = mc.genus_g_mc_equation(1)
        assert result["genus"] == 1
        assert result["non_separating"] is not None

    def test_genus_bootstrap_inductive(self):
        """Genus bootstrap produces equations at each genus."""
        mc = BarIntrinsicMC("heisenberg", Fraction(1), 2, "G")
        boot = mc.genus_bootstrap_inductive(3)
        assert len(boot) == 4  # g = 0, 1, 2, 3
        for g in range(4):
            assert boot[g]["genus"] == g


# ===================================================================
# Section 6: ShadowExtraction
# ===================================================================

class TestShadowExtraction:
    """Tests for shadow projections of Theta_A."""

    # --- Kappa formulas ---

    def test_kappa_heisenberg_rank1(self):
        """kappa(H^1) = 1 (rank = 1, anomaly ratio rho = 1)."""
        assert ShadowExtraction.kappa_heisenberg(1) == Fraction(1)

    def test_kappa_heisenberg_rank2(self):
        """kappa(H^2) = 2 (rank = 2)."""
        assert ShadowExtraction.kappa_heisenberg(2) == Fraction(2)

    def test_kappa_affine_sl2_k1(self):
        """kappa(V_1(sl_2)) = 3(1+2)/4 = 9/4."""
        assert ShadowExtraction.kappa_affine_sl2(Fraction(1)) == Fraction(9, 4)

    def test_kappa_affine_sl2_k2(self):
        """kappa(V_2(sl_2)) = 3(2+2)/4 = 3."""
        assert ShadowExtraction.kappa_affine_sl2(Fraction(2)) == Fraction(3)

    def test_kappa_affine_sl2_critical(self):
        """kappa(V_{-2}(sl_2)) = 3(-2+2)/4 = 0."""
        assert ShadowExtraction.kappa_affine_sl2(Fraction(-2)) == Fraction(0)

    def test_kappa_affine_slN_sl3_k1(self):
        """kappa(V_1(sl_3)) = (1+3)*8/(2*3) = 16/3."""
        assert ShadowExtraction.kappa_affine_slN(3, Fraction(1)) == Fraction(16, 3)

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert ShadowExtraction.kappa_virasoro(Fraction(1)) == Fraction(1, 2)

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13."""
        assert ShadowExtraction.kappa_virasoro(Fraction(26)) == Fraction(13)

    def test_kappa_betagamma(self):
        """kappa(beta-gamma) = +1."""
        assert ShadowExtraction.kappa_betagamma() == Fraction(1)

    # --- Shadow depth ---

    def test_shadow_depth_heisenberg(self):
        """Heisenberg: r_max = 2 (Gaussian class)."""
        assert ShadowExtraction.shadow_depth("heisenberg") == 2

    def test_shadow_depth_affine(self):
        """Affine: r_max = 3 (Lie/tree class)."""
        assert ShadowExtraction.shadow_depth("affine") == 3

    def test_shadow_depth_betagamma(self):
        """beta-gamma: r_max = 4 (contact class)."""
        assert ShadowExtraction.shadow_depth("betagamma") == 4

    def test_shadow_depth_virasoro(self):
        """Virasoro: r_max = infinity (mixed class)."""
        assert ShadowExtraction.shadow_depth("virasoro") is None

    def test_shadow_depth_w_n(self):
        """W_N: r_max = infinity (mixed class)."""
        assert ShadowExtraction.shadow_depth("w_n") is None

    # --- Obstruction classes ---

    def test_heisenberg_all_obstructions_vanish(self):
        """Heisenberg: o_r = 0 for all r >= 3."""
        for r in range(3, 7):
            assert ShadowExtraction.obstruction_class_vanishes("heisenberg", r)

    def test_affine_o3_nonzero(self):
        """Affine: o_3 != 0 (Killing 3-cocycle)."""
        assert not ShadowExtraction.obstruction_class_vanishes("affine", 3)

    def test_affine_o4_zero(self):
        """Affine: o_4 = 0 (terminates at arity 3, Whitehead rigidity)."""
        assert ShadowExtraction.obstruction_class_vanishes("affine", 4)

    def test_betagamma_o4_nonzero(self):
        """beta-gamma: o_4 != 0 (quartic contact interaction)."""
        assert not ShadowExtraction.obstruction_class_vanishes("betagamma", 4)

    def test_betagamma_o5_zero(self):
        """beta-gamma: o_5 = 0 (terminates at arity 4)."""
        assert ShadowExtraction.obstruction_class_vanishes("betagamma", 5)

    def test_virasoro_o5_nonzero(self):
        """Virasoro: o_5 != 0 (infinite tower forced)."""
        assert not ShadowExtraction.obstruction_class_vanishes("virasoro", 5)

    # --- Quartic contact invariant ---

    def test_quartic_contact_virasoro_c1(self):
        """Q^contact_Vir(c=1) = 10/(1*27) = 10/27."""
        assert ShadowExtraction.quartic_contact_virasoro(Fraction(1)) == Fraction(10, 27)

    def test_quartic_contact_virasoro_c25(self):
        """Q^contact_Vir(c=25) = 10/(25*147) = 10/3675 = 2/735."""
        result = ShadowExtraction.quartic_contact_virasoro(Fraction(25))
        assert result == Fraction(10, 25 * 147)

    def test_quartic_contact_virasoro_c0_undefined(self):
        """Q^contact_Vir is undefined at c=0."""
        assert ShadowExtraction.quartic_contact_virasoro(Fraction(0)) is None

    def test_quartic_contact_virasoro_c_minus22_over5_undefined(self):
        """Q^contact_Vir is undefined at c = -22/5."""
        assert ShadowExtraction.quartic_contact_virasoro(Fraction(-22, 5)) is None

    # --- Hessian correction ---

    def test_hessian_correction_c1(self):
        """delta_H^(1)_Vir(c=1) = 120/(1*27) = 40/9."""
        result = ShadowExtraction.hessian_correction_virasoro(Fraction(1))
        assert result == Fraction(120, 27)


# ===================================================================
# Section 7: ClutchingFactorization
# ===================================================================

class TestClutchingFactorization:
    """Tests for separating and non-separating clutching."""

    def test_separating_components_g0(self):
        """At genus 0, only (0,0) separating pair."""
        cf = ClutchingFactorization(kappa=Fraction(1, 2))
        assert cf.separating_components(0) == [(0, 0)]

    def test_separating_components_g2(self):
        """At genus 2: (0,2), (1,1), (2,0)."""
        cf = ClutchingFactorization(kappa=Fraction(1, 2))
        comps = cf.separating_components(2)
        assert (0, 2) in comps
        assert (1, 1) in comps
        assert (2, 0) in comps

    def test_nonseparating_source_g1(self):
        """Non-separating clutching to genus 1 comes from genus 0."""
        cf = ClutchingFactorization(kappa=Fraction(1, 2))
        assert cf.nonseparating_source_genus(1) == 0

    def test_genus_1_clutching_heisenberg(self):
        """Genus-1 clutching for Heisenberg: self-loop graph, |Aut|=2."""
        cf = ClutchingFactorization(kappa=Fraction(1, 2))
        result = cf.verify_genus_1_clutching()
        assert result["nonsep_aut"] == 2
        assert result["no_separating_at_g1_n0"]
        # The weighted amplitude: kappa^1/2 = (1/2)/2 = 1/4
        assert result["nonsep_amplitude"] == Fraction(1, 4)


# ===================================================================
# Section 8: VerdierDuality / Complementarity
# ===================================================================

class TestVerdierDuality:
    """Tests for D(Theta_A) = Theta_{A!} and complementarity."""

    def test_feigin_frenkel_dual_level_sl2(self):
        """k! = -k - 2h^v. For sl_2 (h^v=2): k! = -k - 4."""
        assert VerdierDuality.feigin_frenkel_dual_level(
            Fraction(1), 2
        ) == Fraction(-5)

    def test_dual_central_charge_sl2_k1(self):
        """c(V_{-5}(sl_2)) = (-5)*3/(-5+2) = -15/(-3) = 5."""
        c_dual = VerdierDuality.dual_central_charge_slN(2, Fraction(1))
        assert c_dual == Fraction(5)

    def test_complementarity_sl2_k1(self):
        """kappa(V_1(sl_2)) + kappa(V_{-5}(sl_2)) = 3."""
        result = VerdierDuality.verify_kappa_complementarity_slN(2, Fraction(1))
        assert result["complementarity_holds"]
        assert result["expected_sum"] == Fraction(3)

    def test_complementarity_sl2_k10(self):
        """kappa complementarity for sl_2 at k=10."""
        result = VerdierDuality.verify_kappa_complementarity_slN(2, Fraction(10))
        assert result["complementarity_holds"]

    def test_complementarity_sl3_k1(self):
        """kappa(V_1(sl_3)) + kappa(V_{k!}(sl_3)) = 8."""
        result = VerdierDuality.verify_kappa_complementarity_slN(3, Fraction(1))
        assert result["complementarity_holds"]
        assert result["expected_sum"] == Fraction(8)

    def test_complementarity_sl4_k2(self):
        """sl_4 at k=2: expected sum = 15."""
        result = VerdierDuality.verify_kappa_complementarity_slN(4, Fraction(2))
        assert result["complementarity_holds"]
        assert result["expected_sum"] == Fraction(15)

    def test_complementarity_sl5_k3(self):
        """sl_5 at k=3: expected sum = 24."""
        result = VerdierDuality.verify_kappa_complementarity_slN(5, Fraction(3))
        assert result["complementarity_holds"]
        assert result["expected_sum"] == Fraction(24)

    def test_virasoro_self_duality_c13(self):
        """Vir_c is self-dual at c=13: Vir_13^! = Vir_13."""
        result = VerdierDuality.verify_virasoro_self_duality(Fraction(13))
        assert result["is_self_dual"]
        assert result["sum_is_13"]

    def test_virasoro_not_self_dual_c1(self):
        """Vir_1 is NOT self-dual: Vir_1^! = Vir_25."""
        result = VerdierDuality.verify_virasoro_self_duality(Fraction(1))
        assert not result["is_self_dual"]
        assert result["sum_is_13"]
        assert result["kappa_dual"] == Fraction(25, 2)

    def test_virasoro_dual_kappa_sum_always_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c in [0, 1, 2, 7, 13, 20, 26, -10]:
            result = VerdierDuality.verify_virasoro_self_duality(Fraction(c))
            assert result["sum_is_13"]


# ===================================================================
# Section 9: GenusBootstrap
# ===================================================================

class TestGenusBootstrap:
    """Tests for inductive genus determination."""

    def test_heisenberg_free_energy_g1(self):
        """F_1(H_{1/2}) = (1/2) * (1/24) = 1/48."""
        f1 = GenusBootstrap.free_energy_heisenberg(1, Fraction(1, 2))
        assert f1 == Fraction(1, 48)

    def test_heisenberg_free_energy_g2(self):
        """F_2(H_{1/2}) = (1/2) * (7/5760) = 7/11520."""
        f2 = GenusBootstrap.free_energy_heisenberg(2, Fraction(1, 2))
        assert f2 == Fraction(7, 11520)

    def test_heisenberg_free_energy_g3(self):
        """F_3(H_{1/2}) = (1/2) * (31/967680) = 31/1935360."""
        f3 = GenusBootstrap.free_energy_heisenberg(3, Fraction(1, 2))
        assert f3 == Fraction(31, 1935360)

    def test_affine_sl2_free_energy_g1_k1(self):
        """F_1(V_1(sl_2)) = kappa * 1/24 where kappa = 9/4.
        F_1 = 9/4 * 1/24 = 3/32."""
        f1 = GenusBootstrap.free_energy_affine_sl2(1, Fraction(1))
        assert f1 == Fraction(3, 32)

    def test_affine_sl2_free_energy_g1_k2(self):
        """F_1(V_2(sl_2)) = 3 * (1/24) = 1/8."""
        f1 = GenusBootstrap.free_energy_affine_sl2(1, Fraction(2))
        assert f1 == Fraction(1, 8)

    def test_bernoulli_values(self):
        """Lambda_g^FP ground truth values."""
        vals = GenusBootstrap.genus_bernoulli_values(5)
        assert vals[1] == Fraction(1, 24)
        assert vals[2] == Fraction(7, 5760)
        assert vals[3] == Fraction(31, 967680)

    def test_genus_spectral_sequence_g1(self):
        """E_1 page at genus 1: 2 graphs, split by loop genus."""
        e1 = GenusBootstrap.genus_spectral_sequence_e1(2)
        assert e1[1]["graph_count"] == 2  # genus-1 with 1 marked point

    def test_genus_spectral_sequence_g2(self):
        """E_1 page at genus 2: 6 graphs."""
        e1 = GenusBootstrap.genus_spectral_sequence_e1(2)
        assert e1[2]["graph_count"] == 6


# ===================================================================
# Section 10: QuantumLInfinityMC
# ===================================================================

class TestQuantumLInfinityMC:
    """Tests for the quantum L-infinity MC equation."""

    def test_strict_model_brackets(self):
        """Strict model has ell_1^(0), ell_2^(0), ell_1^(1)."""
        brackets = QuantumLInfinityMC.strict_model_brackets()
        assert "ell_1_g0" in brackets
        assert "ell_2_g0" in brackets
        assert "ell_1_g1" in brackets

    def test_quantum_mc_genus_0_terms(self):
        """At genus 0: ell_1(Theta^(0)) + 1/2 ell_2(Theta^(0), Theta^(0))."""
        terms = QuantumLInfinityMC.quantum_mc_genus_terms(0)
        assert len(terms) == 2  # ell_1 + ell_2

    def test_quantum_mc_genus_1_terms(self):
        """At genus 1: ell_1(Theta^(1)) + ell_2(Theta^(0),Theta^(1))
        + ell_2(Theta^(1),Theta^(0)) + Delta(Theta^(0))."""
        terms = QuantumLInfinityMC.quantum_mc_genus_terms(1)
        assert len(terms) == 4  # ell_1 + 2 ell_2 + Delta

    def test_quantum_mc_genus_2_terms(self):
        """At genus 2: ell_1 + 3 ell_2 terms + Delta."""
        terms = QuantumLInfinityMC.quantum_mc_genus_terms(2)
        assert len(terms) == 5  # ell_1 + 3 ell_2 + Delta


# ===================================================================
# Section 11: Scalar free energy
# ===================================================================

class TestScalarFreeEnergy:
    """Tests for F_g = kappa * lambda_g^FP."""

    def test_f1_kappa_1(self):
        """F_1(kappa=1) = 1/24."""
        assert scalar_free_energy(1, Fraction(1)) == Fraction(1, 24)

    def test_f2_kappa_1(self):
        """F_2(kappa=1) = 7/5760."""
        assert scalar_free_energy(2, Fraction(1)) == Fraction(7, 5760)

    def test_f3_kappa_1(self):
        """F_3(kappa=1) = 31/967680."""
        assert scalar_free_energy(3, Fraction(1)) == Fraction(31, 967680)

    def test_f1_kappa_half(self):
        """F_1(kappa=1/2) = 1/48."""
        assert scalar_free_energy(1, Fraction(1, 2)) == Fraction(1, 48)

    def test_f_g_linearity_in_kappa(self):
        """F_g(a*kappa) = a * F_g(kappa)."""
        for g in range(1, 4):
            for a in [Fraction(1), Fraction(2), Fraction(3, 7)]:
                lhs = scalar_free_energy(g, a * Fraction(1))
                rhs = a * scalar_free_energy(g, Fraction(1))
                assert lhs == rhs

    def test_f_g_negative_kappa(self):
        """Free energy with negative kappa (e.g., beta-gamma)."""
        f1 = scalar_free_energy(1, Fraction(-1))
        assert f1 == Fraction(-1, 24)

    def test_invalid_genus_raises(self):
        """genus < 1 raises ValueError."""
        with pytest.raises(ValueError):
            scalar_free_energy(0, Fraction(1))


# ===================================================================
# Section 12: Genus-2 graph amplitudes
# ===================================================================

class TestGenus2GraphAmplitudes:
    """Tests for individual genus-2 graph amplitudes."""

    def test_six_amplitudes(self):
        """There are exactly 6 genus-2 graph amplitudes."""
        amps = genus2_graph_amplitudes(Fraction(1, 2))
        assert len(amps) == 6

    def test_smooth_amplitude(self):
        """Smooth g=2: 0 edges, |Aut|=1, amplitude = 1."""
        amps = genus2_graph_amplitudes(Fraction(1, 2))
        assert amps["smooth_g2"] == Fraction(1)

    def test_banana_amplitude(self):
        """Banana: 2 self-loops, |Aut|=8, amplitude = kappa^2/8."""
        kappa = Fraction(1, 2)
        amps = genus2_graph_amplitudes(kappa)
        assert amps["banana_g0"] == kappa ** 2 / Fraction(8)

    def test_theta_amplitude(self):
        """Theta: 3 parallel edges, |Aut|=12, amplitude = kappa^3/12."""
        kappa = Fraction(1, 2)
        amps = genus2_graph_amplitudes(kappa)
        assert amps["theta_g0_g0"] == kappa ** 3 / Fraction(12)

    def test_irr_node_amplitude(self):
        """Irr node: 1 self-loop, |Aut|=2, amplitude = kappa/2."""
        kappa = Fraction(1, 2)
        amps = genus2_graph_amplitudes(kappa)
        assert amps["irr_node_g1"] == kappa / Fraction(2)


# ===================================================================
# Section 13: Independent sum factorization
# ===================================================================

class TestIndependentSumFactorization:
    """Tests for prop:independent-sum-factorization."""

    def test_additive_kappa(self):
        """kappa(L1 + L2) = kappa(L1) + kappa(L2)."""
        result = verify_independent_sum_factorization(
            Fraction(1, 2), Fraction(3, 4)
        )
        assert result["kappa_additive"]

    def test_additive_free_energy_all_genera(self):
        """F_g(L1+L2) = F_g(L1) + F_g(L2) for g = 1, 2, 3."""
        result = verify_independent_sum_factorization(
            Fraction(1, 2), Fraction(3, 4), max_g=3
        )
        for g in range(1, 4):
            assert result["genus_checks"][f"genus_{g}"]["additive"]

    def test_heisenberg_plus_heisenberg(self):
        """H^1 + H^1: kappa = 1/2 + 1/2 = 1."""
        result = verify_independent_sum_factorization(
            Fraction(1, 2), Fraction(1, 2)
        )
        assert result["kappa_sum"] == Fraction(1)

    def test_zero_kappa(self):
        """Adding kappa=0 (critical level) preserves free energy."""
        result = verify_independent_sum_factorization(
            Fraction(1, 2), Fraction(0)
        )
        for g in range(1, 4):
            assert result["genus_checks"][f"genus_{g}"]["additive"]


# ===================================================================
# Section 14: Complementarity landscape
# ===================================================================

class TestComplementarityLandscape:
    """Tests for Theorem C across the sl_N landscape."""

    def test_sl2_all_levels(self):
        """Complementarity for sl_2 at k = 1, 2, 3, 5, 10."""
        results = verify_complementarity_slN_landscape(
            N_values=[2], k_values=[Fraction(n) for n in [1, 2, 3, 5, 10]]
        )
        for key, val in results.items():
            assert val["complementarity_holds"], f"Failed: {key}"

    def test_sl3_all_levels(self):
        """Complementarity for sl_3 at k = 1, 2, 3, 5, 10."""
        results = verify_complementarity_slN_landscape(
            N_values=[3], k_values=[Fraction(n) for n in [1, 2, 3, 5, 10]]
        )
        for key, val in results.items():
            assert val["complementarity_holds"], f"Failed: {key}"

    def test_sl4_all_levels(self):
        """Complementarity for sl_4 at k = 1, 2, 5."""
        results = verify_complementarity_slN_landscape(
            N_values=[4], k_values=[Fraction(n) for n in [1, 2, 5]]
        )
        for key, val in results.items():
            assert val["complementarity_holds"], f"Failed: {key}"

    def test_complementarity_sum_is_dim_g(self):
        """For all sl_N: kappa(A) + kappa(A!) = N^2 - 1."""
        for N in [2, 3, 4, 5]:
            for k_val in [1, 3, 7]:
                result = VerdierDuality.verify_kappa_complementarity_slN(
                    N, Fraction(k_val)
                )
                assert result["expected_sum"] == Fraction(N * N - 1)
                assert result["complementarity_holds"]


# ===================================================================
# Section 15: Stable graph census
# ===================================================================

class TestStableGraphCensus:
    """Tests for the graph count census."""

    def test_census_g1_n0(self):
        assert stable_graph_census(max_g=2, max_n=2)[(1, 0)] == 2

    def test_census_g1_n1(self):
        assert stable_graph_census(max_g=2, max_n=2)[(1, 1)] == 2

    def test_census_g1_n2(self):
        assert stable_graph_census(max_g=2, max_n=2)[(1, 2)] == 5

    def test_census_g2_n0(self):
        assert stable_graph_census(max_g=2, max_n=2)[(2, 0)] == 6

    def test_census_explicit_g0_n3(self):
        """Explicit check: (0,3) has 1 stable graph."""
        assert len(enumerate_stable_graphs(0, 3)) == 1

    def test_census_explicit_g0_n4(self):
        """Explicit check: (0,4) has 4 stable graphs."""
        assert len(enumerate_stable_graphs(0, 4)) == 4

    def test_genus_filtration_bracket(self):
        """Genus filtration is respected by the bracket."""
        checks = verify_genus_filtration_bracket()
        assert all(checks.values())


# ===================================================================
# Section 16: ModularDeformationPackage (full assembly)
# ===================================================================

class TestModularDeformationPackageHeisenberg:
    """Full package tests for Heisenberg."""

    def setup_method(self):
        self.pkg = heisenberg_package()

    def test_mc_equation(self):
        result = self.pkg.verify_mc_equation()
        assert result["d0_squared_zero"]
        assert result["dA_squared_zero"]
        assert result["ambient_d_squared_zero"]
        assert result["mc_from_d_squared"]

    def test_shadow_termination(self):
        result = self.pkg.verify_shadow_termination()
        assert result["shadow_class"] == "G"
        assert result["shadow_depth"] == 2
        checks = result["obstruction_checks"]
        assert checks["o_3_vanishes"]
        assert checks["o_4_vanishes"]

    def test_free_energy_table(self):
        fe = self.pkg.free_energy_table()
        # kappa = 1 for rank-1 Heisenberg: F_g = kappa * lambda_g^FP
        assert fe[1] == Fraction(1, 24)
        assert fe[2] == Fraction(7, 5760)
        assert fe[3] == Fraction(31, 967680)

    def test_verify_all(self):
        """Full verification suite runs without error."""
        result = self.pkg.verify_all()
        assert "mc_equation" in result
        assert "shadow_termination" in result
        assert "genus_bootstrap" in result
        assert "free_energy" in result


class TestModularDeformationPackageAffineSl2:
    """Full package tests for affine sl_2."""

    def setup_method(self):
        self.pkg = affine_sl2_package(Fraction(1))

    def test_kappa_value(self):
        assert self.pkg.kappa == Fraction(9, 4)

    def test_shadow_class_L(self):
        result = self.pkg.verify_shadow_termination()
        assert result["shadow_class"] == "L"
        assert result["shadow_depth"] == 3

    def test_o3_nonzero_o4_zero(self):
        checks = self.pkg.verify_shadow_termination()["obstruction_checks"]
        assert not checks["o_3_vanishes"]
        assert checks["o_4_vanishes"]


class TestModularDeformationPackageBetaGamma:
    """Full package tests for beta-gamma system."""

    def setup_method(self):
        self.pkg = betagamma_package()

    def test_kappa_value(self):
        assert self.pkg.kappa == Fraction(1)

    def test_shadow_class_C(self):
        result = self.pkg.verify_shadow_termination()
        assert result["shadow_class"] == "C"
        assert result["shadow_depth"] == 4

    def test_o4_nonzero_o5_zero(self):
        checks = self.pkg.verify_shadow_termination()["obstruction_checks"]
        assert not checks["o_4_vanishes"]
        assert checks["o_5_vanishes"]


class TestModularDeformationPackageVirasoro:
    """Full package tests for Virasoro."""

    def setup_method(self):
        self.pkg = virasoro_package(Fraction(1))

    def test_kappa_value(self):
        assert self.pkg.kappa == Fraction(1, 2)

    def test_shadow_class_M(self):
        result = self.pkg.verify_shadow_termination()
        assert result["shadow_class"] == "M"
        assert result["shadow_depth"] is None

    def test_o5_nonzero(self):
        checks = self.pkg.verify_shadow_termination()["obstruction_checks"]
        assert not checks["o_5_vanishes"]


# ===================================================================
# Section 17: Kappa standard landscape
# ===================================================================

class TestKappaStandardLandscape:
    """Tests for the kappa ground truth table."""

    def test_landscape_has_all_families(self):
        landscape = kappa_standard_landscape()
        assert "heisenberg_rank1" in landscape
        assert "affine_sl2_k1" in landscape
        assert "affine_sl3_k1" in landscape
        assert "virasoro_c1" in landscape
        assert "betagamma" in landscape

    def test_heisenberg_landscape(self):
        landscape = kappa_standard_landscape()
        assert landscape["heisenberg_rank1"]["kappa"] == Fraction(1)

    def test_betagamma_landscape(self):
        landscape = kappa_standard_landscape()
        assert landscape["betagamma"]["kappa"] == Fraction(1)

    def test_affine_sl3_landscape(self):
        """kappa(V_1(sl_3)) = 4*(1+3)/3 = 16/3."""
        landscape = kappa_standard_landscape()
        assert landscape["affine_sl3_k1"]["kappa"] == Fraction(16, 3)


# ===================================================================
# Section 18: Integration test
# ===================================================================

class TestFullVerificationSuite:
    """Integration test running the complete verification suite."""

    def test_full_verification_runs(self):
        """verify_modular_deformation_package() runs without error."""
        results = verify_modular_deformation_package()
        assert isinstance(results, dict)
        assert "heisenberg" in results
        assert "affine_sl2_k1" in results
        assert "betagamma" in results
        assert "virasoro_c1" in results
        assert "d_squared_zero" in results

    def test_all_mc_equations_hold(self):
        """MC equation verified for all standard families."""
        results = verify_modular_deformation_package()
        for family in ["heisenberg", "affine_sl2_k1", "betagamma", "virasoro_c1"]:
            mc = results[family]["mc_equation"]
            assert mc["mc_from_d_squared"], f"MC failed for {family}"

    def test_d_squared_zero_both_levels(self):
        """D^2 = 0 at convolution and ambient levels."""
        results = verify_modular_deformation_package()
        d2 = results["d_squared_zero"]
        assert d2["convolution"]
        assert d2["ambient"]

    def test_all_complementarity_checks(self):
        """Complementarity holds for all sl_2 levels tested."""
        results = verify_modular_deformation_package()
        for k_val in [1, 2, 3, 5, 10]:
            key = f"complementarity_sl2_k{k_val}"
            assert results[key]["complementarity_holds"]
