"""Tests for the explicit chiral derived center computations.

Tests cover:
1. Hochschild cohomology dimensions for standard families
2. Derived center structure maps (product, bracket, BV)
3. Annulus trace computations
4. Open/closed MC element verification
5. Deformation quantization checks
6. Bulk-boundary maps and composition
7. Morita invariance
8. Hochschild-Kostant-Rosenberg
9. Cross-family consistency (kappa additivity, complementarity)
10. Weight-graded enumeration

CRITICAL PITFALLS TESTED:
- AP1: kappa formula correctness per family
- AP19: r-matrix vs OPE pole orders (indirect)
- AP20: kappa(A) vs kappa_eff distinction
- AP24: complementarity sum != 0 for Virasoro
- AP25/AP34: bar != Verdier dual != cobar != derived center
- AP33: H_k^! = Sym^ch(V*) != H_{-k}
"""

import pytest
from fractions import Fraction

from compute.lib.derived_center_explicit import (
    # Basic invariants
    kappa,
    generator_weights,
    num_generators,
    FAMILIES,
    # Hochschild cocycle enumeration
    HochschildCocycleEnumerator,
    heisenberg_hh_cocycles,
    affine_sl2_hh_dimensions,
    affine_sl2_hh_at_levels,
    virasoro_hh2_weight_graded,
    # Structure maps
    DerivedCenterStructureMaps,
    # Annulus trace
    AnnulusTrace,
    # Open/closed MC
    OpenClosedMCElement,
    # Deformation quantization
    DeformationQuantization,
    # Bulk-boundary
    BulkBoundaryMaps,
    # Morita
    morita_invariance_check,
    # HKR
    chiral_hkr_dimension,
    # Cross-family
    verify_kappa_additivity,
    verify_complementarity,
    # Master package
    full_derived_center_package,
)


# ======================================================================
#  Section 1: kappa (modular characteristic) — AP1 verified
# ======================================================================

class TestKappa:
    """Test kappa formulas for each family independently (AP1)."""

    def test_kappa_heisenberg_k1(self):
        assert kappa("Heisenberg", k=1) == Fraction(1)

    def test_kappa_heisenberg_k2(self):
        assert kappa("Heisenberg", k=2) == Fraction(2)

    def test_kappa_heisenberg_k_half(self):
        assert kappa("Heisenberg", k=Fraction(1, 2)) == Fraction(1, 2)

    def test_kappa_affine_sl2_k1(self):
        # kappa = 3(k+2)/4 = 3*3/4 = 9/4
        assert kappa("Affine_sl2", k=1) == Fraction(9, 4)

    def test_kappa_affine_sl2_k2(self):
        # kappa = 3*4/4 = 3
        assert kappa("Affine_sl2", k=2) == Fraction(3)

    def test_kappa_affine_sl2_k3(self):
        # kappa = 3*5/4 = 15/4
        assert kappa("Affine_sl2", k=3) == Fraction(15, 4)

    def test_kappa_virasoro_c26(self):
        assert kappa("Virasoro", c=26) == Fraction(13)

    def test_kappa_virasoro_c1(self):
        assert kappa("Virasoro", c=1) == Fraction(1, 2)

    def test_kappa_virasoro_c0(self):
        assert kappa("Virasoro", c=0) == Fraction(0)

    def test_kappa_virasoro_c13(self):
        # Self-dual point
        assert kappa("Virasoro", c=13) == Fraction(13, 2)

    def test_kappa_w3_c2(self):
        # AP1: kappa(W_3) = 5c/6 = 5*2/6 = 5/3
        assert kappa("W3", c=2) == Fraction(5, 3)

    def test_kappa_w3_c26(self):
        # AP1: kappa(W_3) = 5*26/6 = 65/3
        assert kappa("W3", c=26) == Fraction(65, 3)


# ======================================================================
#  Section 2: Generator data
# ======================================================================

class TestGenerators:

    def test_heisenberg_weights(self):
        assert generator_weights("Heisenberg") == [1]

    def test_affine_sl2_weights(self):
        assert generator_weights("Affine_sl2") == [1, 1, 1]

    def test_virasoro_weights(self):
        assert generator_weights("Virasoro") == [2]

    def test_w3_weights(self):
        assert generator_weights("W3") == [2, 3]

    def test_num_generators(self):
        assert num_generators("Heisenberg") == 1
        assert num_generators("Affine_sl2") == 3
        assert num_generators("Virasoro") == 1
        assert num_generators("W3") == 2


# ======================================================================
#  Section 3: Hochschild cohomology dimensions
# ======================================================================

class TestHochschildDimensions:
    """Test HH^n(A,A) dimensions."""

    # --- Heisenberg ---

    def test_heisenberg_hh_cocycles_basic(self):
        cocycles = heisenberg_hh_cocycles(k=Fraction(1), max_weight=4)
        # HH^0 at weight 0 = 1 (center)
        assert cocycles[(0, 0)] == 1
        # HH^1 at weight 0 = 1 (level deformation)
        assert cocycles[(1, 0)] == 1
        # HH^2 at weight 0 = 1 (dual center)
        assert cocycles[(2, 0)] == 1

    def test_heisenberg_hh_vanishing(self):
        cocycles = heisenberg_hh_cocycles(k=Fraction(1), max_weight=4)
        # HH^n = 0 for n >= 3
        for n in range(3, 5):
            for w in range(5):
                assert cocycles[(n, w)] == 0

    def test_heisenberg_hh_higher_weight_zero(self):
        cocycles = heisenberg_hh_cocycles(k=Fraction(1), max_weight=4)
        # All higher-weight components vanish for Heisenberg
        for n in range(3):
            for w in range(1, 5):
                assert cocycles[(n, w)] == 0

    # --- Affine sl_2 ---

    def test_affine_sl2_hh_k1(self):
        dims = affine_sl2_hh_dimensions(1)
        assert dims[0] == 1  # center
        assert dims[1] == 3  # dim(sl_2) outer derivations
        assert dims[2] == 1  # dual center

    def test_affine_sl2_hh_k2(self):
        dims = affine_sl2_hh_dimensions(2)
        assert dims == {0: 1, 1: 3, 2: 1}

    def test_affine_sl2_hh_k3(self):
        dims = affine_sl2_hh_dimensions(3)
        assert dims == {0: 1, 1: 3, 2: 1}

    def test_affine_sl2_critical_level_raises(self):
        with pytest.raises(ValueError, match="Critical level"):
            affine_sl2_hh_dimensions(-2)

    def test_affine_sl2_hh_at_levels(self):
        results = affine_sl2_hh_at_levels()
        assert set(results.keys()) == {1, 2, 3}
        for k in [1, 2, 3]:
            assert results[k][0] == 1
            assert results[k][1] == 3
            assert results[k][2] == 1

    # --- Virasoro ---

    def test_virasoro_hh2_weight_graded(self):
        result = virasoro_hh2_weight_graded(c=Fraction(26), max_weight=8)
        # Weight 0: the c-deformation (1 class)
        assert result[0] == 1
        # All higher weights: 0 (Jacobi blocks)
        for w in range(1, 9):
            assert result[w] == 0

    def test_virasoro_hh2_generic_c(self):
        # Result should be independent of c (at generic c)
        for c_val in [1, 13, 26]:
            result = virasoro_hh2_weight_graded(c=Fraction(c_val), max_weight=4)
            assert result[0] == 1
            for w in range(1, 5):
                assert result[w] == 0


# ======================================================================
#  Section 4: Derived center structure maps (Heisenberg)
# ======================================================================

class TestDerivedCenterStructureMaps:

    @pytest.fixture
    def maps_k1(self):
        return DerivedCenterStructureMaps("Heisenberg", k=Fraction(1))

    @pytest.fixture
    def maps_k2(self):
        return DerivedCenterStructureMaps("Heisenberg", k=Fraction(2))

    # --- Product ---

    def test_product_vac_is_unit(self, maps_k1):
        for g in ["vac", "xi_k", "eta"]:
            name, coeff = maps_k1.product("vac", g)
            assert name == g
            assert coeff == Fraction(1)

    def test_product_unit_from_right(self, maps_k1):
        for g in ["vac", "xi_k", "eta"]:
            name, coeff = maps_k1.product(g, "vac")
            assert name == g
            assert coeff == Fraction(1)

    def test_product_xi_xi_at_k1(self, maps_k1):
        name, coeff = maps_k1.product("xi_k", "xi_k")
        assert name == "eta"
        assert coeff == Fraction(1)

    def test_product_xi_xi_at_k2(self, maps_k2):
        name, coeff = maps_k2.product("xi_k", "xi_k")
        assert name == "eta"
        assert coeff == Fraction(2)

    def test_product_degree_3_vanishes(self, maps_k1):
        # xi * eta in HH^3 = 0
        name, coeff = maps_k1.product("xi_k", "eta")
        assert name == "0"
        assert coeff == Fraction(0)

    def test_product_degree_4_vanishes(self, maps_k1):
        # eta * eta in HH^4 = 0
        name, coeff = maps_k1.product("eta", "eta")
        assert name == "0"
        assert coeff == Fraction(0)

    # --- Gerstenhaber bracket ---

    def test_bracket_vac_zero(self, maps_k1):
        for g in ["vac", "xi_k", "eta"]:
            name, coeff = maps_k1.gerstenhaber_bracket("vac", g)
            assert coeff == Fraction(0)

    def test_bracket_xi_xi_zero(self, maps_k1):
        """Unobstructed deformation: [xi_k, xi_k] = 0."""
        name, coeff = maps_k1.gerstenhaber_bracket("xi_k", "xi_k")
        assert coeff == Fraction(0)

    def test_bracket_xi_eta(self, maps_k1):
        """[xi, eta] = -eta (determined by BV relation)."""
        name, coeff = maps_k1.gerstenhaber_bracket("xi_k", "eta")
        assert name == "eta"
        assert coeff == Fraction(-1)

    def test_bracket_eta_xi_antisymmetry(self, maps_k1):
        """Graded antisymmetry: [eta, xi] = -(-1)^0 [xi, eta] = eta."""
        name1, coeff1 = maps_k1.gerstenhaber_bracket("xi_k", "eta")
        name2, coeff2 = maps_k1.gerstenhaber_bracket("eta", "xi_k")
        assert name2 == name1
        assert coeff2 == -coeff1

    def test_bracket_eta_eta_zero(self, maps_k1):
        name, coeff = maps_k1.gerstenhaber_bracket("eta", "eta")
        assert coeff == Fraction(0)

    # --- BV operator ---

    def test_bv_vac_zero(self, maps_k1):
        name, coeff = maps_k1.bv_operator("vac")
        assert coeff == Fraction(0)

    def test_bv_xi(self, maps_k1):
        name, coeff = maps_k1.bv_operator("xi_k")
        assert name == "vac"
        assert coeff == Fraction(1)

    def test_bv_eta_zero(self, maps_k1):
        """Delta(eta) = 0, forced by BV relation + [xi,xi]=0."""
        name, coeff = maps_k1.bv_operator("eta")
        assert coeff == Fraction(0)

    # --- BV relation ---

    def test_bv_relation_vac_vac(self, maps_k1):
        result = maps_k1.verify_bv_relation("vac", "vac")
        assert result["match"]

    def test_bv_relation_vac_xi(self, maps_k1):
        result = maps_k1.verify_bv_relation("vac", "xi_k")
        assert result["match"]

    def test_bv_relation_xi_xi(self, maps_k1):
        result = maps_k1.verify_bv_relation("xi_k", "xi_k")
        assert result["match"]

    def test_bv_relation_xi_eta(self, maps_k1):
        result = maps_k1.verify_bv_relation("xi_k", "eta")
        assert result["match"]

    def test_bv_relation_eta_eta(self, maps_k1):
        result = maps_k1.verify_bv_relation("eta", "eta")
        assert result["match"]


# ======================================================================
#  Section 5: Annulus trace
# ======================================================================

class TestAnnulusTrace:

    def test_heisenberg_trace_identity_k1(self):
        tr = AnnulusTrace("Heisenberg", k=1)
        assert tr.trace_on_identity() == Fraction(1)

    def test_heisenberg_trace_identity_k2(self):
        tr = AnnulusTrace("Heisenberg", k=2)
        assert tr.trace_on_identity() == Fraction(2)

    def test_affine_sl2_trace_identity(self):
        tr = AnnulusTrace("Affine_sl2", k=1)
        assert tr.trace_on_identity() == Fraction(9, 4)

    def test_virasoro_trace_identity_c26(self):
        tr = AnnulusTrace("Virasoro", c=26)
        assert tr.trace_on_identity() == Fraction(13)

    def test_virasoro_trace_identity_c1(self):
        tr = AnnulusTrace("Virasoro", c=1)
        assert tr.trace_on_identity() == Fraction(1, 2)

    def test_heisenberg_trace_hh1(self):
        tr = AnnulusTrace("Heisenberg", k=1)
        assert tr.trace_on_hh1() == Fraction(1)

    def test_affine_sl2_trace_hh1(self):
        tr = AnnulusTrace("Affine_sl2", k=1)
        assert tr.trace_on_hh1() == Fraction(3, 4)

    def test_virasoro_trace_hh1(self):
        tr = AnnulusTrace("Virasoro", c=26)
        assert tr.trace_on_hh1() == Fraction(1, 2)

    def test_heisenberg_trace_hh2(self):
        tr = AnnulusTrace("Heisenberg", k=1)
        # kappa^2 / 24 = 1/24
        assert tr.trace_on_hh2() == Fraction(1, 24)

    def test_virasoro_trace_hh2_c26(self):
        tr = AnnulusTrace("Virasoro", c=26)
        # kappa = 13, kappa^2/24 = 169/24
        assert tr.trace_on_hh2() == Fraction(169, 24)

    # --- Complementarity (AP24) ---

    def test_heisenberg_complementarity(self):
        tr = AnnulusTrace("Heisenberg", k=1)
        result = tr.verify_modularity()
        assert result["complement_ok"] is True
        # kappa + kappa_dual = 1 + (-1) = 0
        assert result["complement_sum"] == Fraction(0)

    def test_affine_sl2_complementarity(self):
        tr = AnnulusTrace("Affine_sl2", k=1)
        result = tr.verify_modularity()
        assert result["complement_ok"] is True
        assert result["complement_sum"] == Fraction(0)

    def test_virasoro_complementarity_nonzero(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        tr = AnnulusTrace("Virasoro", c=26)
        result = tr.verify_modularity()
        assert result["complement_ok"] is True
        assert result["complement_sum"] == Fraction(13)

    def test_virasoro_complementarity_c1(self):
        tr = AnnulusTrace("Virasoro", c=1)
        result = tr.verify_modularity()
        assert result["complement_sum"] == Fraction(13)

    def test_virasoro_complementarity_c13(self):
        """At self-dual point c=13."""
        tr = AnnulusTrace("Virasoro", c=13)
        result = tr.verify_modularity()
        assert result["complement_sum"] == Fraction(13)


# ======================================================================
#  Section 6: Open/closed MC element
# ======================================================================

class TestOpenClosedMC:

    @pytest.fixture
    def mc_heis(self):
        return OpenClosedMCElement("Heisenberg", k=1)

    # --- Theta values ---

    def test_theta_genus0_n3_vanishes(self, mc_heis):
        """Heisenberg is Gaussian (class G): no cubic."""
        assert mc_heis.theta_oc(0, 3) == Fraction(0)

    def test_theta_genus0_n4_vanishes(self, mc_heis):
        """Class G: no quartic."""
        assert mc_heis.theta_oc(0, 4) == Fraction(0)

    def test_theta_genus1_n0(self, mc_heis):
        """F_1 = kappa/24 for Heisenberg k=1."""
        assert mc_heis.theta_oc(1, 0) == Fraction(1, 24)

    def test_theta_genus1_n1(self, mc_heis):
        """Theta_{1,1} = kappa for annulus trace."""
        assert mc_heis.theta_oc(1, 1) == Fraction(1)

    def test_theta_genus1_n2(self, mc_heis):
        assert mc_heis.theta_oc(1, 2) == Fraction(1)

    def test_theta_genus2_n0(self, mc_heis):
        """F_2 = kappa/1152."""
        assert mc_heis.theta_oc(2, 0) == Fraction(1, 1152)

    def test_theta_genus0_unstable_vanishes(self, mc_heis):
        """Unstable curves (g=0, n <= 2)."""
        assert mc_heis.theta_oc(0, 0) == Fraction(0)
        assert mc_heis.theta_oc(0, 1) == Fraction(0)
        assert mc_heis.theta_oc(0, 2) == Fraction(0)

    # --- MC equation ---

    def test_mc_equation_genus0_n3(self, mc_heis):
        result = mc_heis.verify_mc_equation(0, 3)
        assert result["MC_satisfied"]

    def test_mc_equation_genus1_n0(self, mc_heis):
        result = mc_heis.verify_mc_equation(1, 0)
        assert result["MC_satisfied"]

    def test_mc_equation_genus1_n1(self, mc_heis):
        result = mc_heis.verify_mc_equation(1, 1)
        assert result["MC_satisfied"]

    def test_mc_equation_genus1_n2(self, mc_heis):
        result = mc_heis.verify_mc_equation(1, 2)
        assert result["MC_satisfied"]

    # --- Level dependence ---

    def test_theta_genus1_k2(self):
        mc = OpenClosedMCElement("Heisenberg", k=2)
        # F_1 = 2/24 = 1/12
        assert mc.theta_oc(1, 0) == Fraction(2, 24)
        # Theta_{1,1} = 2
        assert mc.theta_oc(1, 1) == Fraction(2)


# ======================================================================
#  Section 7: Deformation quantization
# ======================================================================

class TestDeformationQuantization:

    @pytest.fixture
    def dq_k1(self):
        return DeformationQuantization("Heisenberg", k=1)

    @pytest.fixture
    def dq_k2(self):
        return DeformationQuantization("Heisenberg", k=2)

    def test_classical_poisson_zero(self, dq_k1):
        assert dq_k1.classical_poisson_bracket("vac", "vac") == Fraction(0)
        assert dq_k1.classical_poisson_bracket("vac", "xi_k") == Fraction(0)

    def test_quantum_commutator_xi_xi(self, dq_k1):
        name, coeff = dq_k1.quantum_commutator("xi_k", "xi_k")
        assert coeff == Fraction(0)  # unobstructed

    def test_weyl_dim_weight0(self, dq_k1):
        assert dq_k1.weyl_algebra_dimension(0) == 1

    def test_weyl_dim_weight1(self, dq_k1):
        assert dq_k1.weyl_algebra_dimension(1) == 2

    def test_weyl_dim_weight4(self, dq_k1):
        assert dq_k1.weyl_algebra_dimension(4) == 5

    def test_weyl_dim_negative(self, dq_k1):
        assert dq_k1.weyl_algebra_dimension(-1) == 0

    def test_verify_quantization_k1(self, dq_k1):
        result = dq_k1.verify_quantization()
        assert result["unobstructed"]
        assert result["cup_matches_expected"]
        assert result["classical_limit_commutative"]

    def test_verify_quantization_k2(self, dq_k2):
        result = dq_k2.verify_quantization()
        assert result["unobstructed"]
        assert result["cup_matches_expected"]
        name, coeff = result["cup_product_xi_xi"]
        assert name == "eta"
        assert coeff == Fraction(2)


# ======================================================================
#  Section 8: Bulk-boundary maps
# ======================================================================

class TestBulkBoundaryMaps:

    @pytest.fixture
    def bb_k1(self):
        return BulkBoundaryMaps("Heisenberg", k=1)

    @pytest.fixture
    def bb_k2(self):
        return BulkBoundaryMaps("Heisenberg", k=2)

    def test_restriction_identity(self, bb_k1):
        for gen in ["vac", "xi_k", "eta"]:
            name, coeff = bb_k1.restriction(gen)
            assert name == gen
            assert coeff == Fraction(1)

    def test_annulus_map_vac(self, bb_k1):
        name, coeff = bb_k1.annulus_map("vac")
        assert name == "vac"
        assert coeff == Fraction(1)  # kappa = 1

    def test_annulus_map_vac_k2(self, bb_k2):
        name, coeff = bb_k2.annulus_map("vac")
        assert name == "vac"
        assert coeff == Fraction(2)  # kappa = 2

    def test_composition_a_r_vac(self, bb_k1):
        name, coeff = bb_k1.composition_a_r("vac")
        assert name == "vac"
        assert coeff == Fraction(1)  # kappa * 1 = 1

    def test_composition_a_r_xi(self, bb_k1):
        name, coeff = bb_k1.composition_a_r("xi_k")
        assert name == "xi_k"
        assert coeff == Fraction(1)  # kappa * 1 = 1

    def test_composition_a_r_equals_kappa(self, bb_k2):
        """a . r = kappa * Id."""
        result = bb_k2.verify_composition()
        for gen in result:
            assert result[gen]["match"]


# ======================================================================
#  Section 9: Morita invariance
# ======================================================================

class TestMoritaInvariance:

    def test_heisenberg_morita_n2(self):
        result = morita_invariance_check("Heisenberg", 2)
        assert result["morita_invariant"]

    def test_heisenberg_morita_n3(self):
        result = morita_invariance_check("Heisenberg", 3)
        assert result["morita_invariant"]

    def test_affine_sl2_morita_n2(self):
        result = morita_invariance_check("Affine_sl2", 2)
        assert result["morita_invariant"]

    def test_virasoro_morita_n2(self):
        result = morita_invariance_check("Virasoro", 2)
        assert result["morita_invariant"]

    def test_w3_morita_n2(self):
        result = morita_invariance_check("W3", 2)
        assert result["morita_invariant"]

    def test_morita_preserves_all_hh(self):
        """HH^k(Mat_n(A)) = HH^k(A) for all k, all standard families."""
        for family in FAMILIES:
            for n in [2, 3, 5]:
                result = morita_invariance_check(family, n)
                assert result["morita_invariant"], (
                    f"Morita invariance failed for {family}, n={n}")


# ======================================================================
#  Section 10: Chiral HKR
# ======================================================================

class TestChiralHKR:

    def test_heisenberg_hkr(self):
        assert chiral_hkr_dimension("Heisenberg", 0) == 1
        assert chiral_hkr_dimension("Heisenberg", 1) == 1
        assert chiral_hkr_dimension("Heisenberg", 2) == 1
        assert chiral_hkr_dimension("Heisenberg", 3) == 0

    def test_affine_sl2_hkr(self):
        assert chiral_hkr_dimension("Affine_sl2", 0) == 1
        assert chiral_hkr_dimension("Affine_sl2", 1) == 3
        assert chiral_hkr_dimension("Affine_sl2", 2) == 1
        assert chiral_hkr_dimension("Affine_sl2", 3) == 0

    def test_virasoro_hkr_polynomial_ring(self):
        """ChirHoch*(Vir) = C[Theta], |Theta|=2."""
        assert chiral_hkr_dimension("Virasoro", 0) == 1
        assert chiral_hkr_dimension("Virasoro", 1) == 0
        assert chiral_hkr_dimension("Virasoro", 2) == 1
        assert chiral_hkr_dimension("Virasoro", 3) == 0
        assert chiral_hkr_dimension("Virasoro", 4) == 1

    def test_w3_hkr_polynomial_ring(self):
        """ChirHoch*(W_3) = C[Theta_1, Theta_2], |Theta_1|=2, |Theta_2|=3."""
        assert chiral_hkr_dimension("W3", 0) == 1
        assert chiral_hkr_dimension("W3", 1) == 0
        assert chiral_hkr_dimension("W3", 2) == 1
        assert chiral_hkr_dimension("W3", 3) == 1
        assert chiral_hkr_dimension("W3", 4) == 1  # Theta_1^2
        assert chiral_hkr_dimension("W3", 5) == 1  # Theta_1 Theta_2
        assert chiral_hkr_dimension("W3", 6) == 2  # Theta_1^3, Theta_2^2

    def test_hkr_negative_degree(self):
        for family in FAMILIES:
            assert chiral_hkr_dimension(family, -1) == 0


# ======================================================================
#  Section 11: Cross-family consistency
# ======================================================================

class TestCrossFamilyConsistency:

    def test_kappa_additivity(self):
        """kappa(H_1 + H_2) = kappa(H_1) + kappa(H_2)."""
        result = verify_kappa_additivity([
            ("Heisenberg", {"k": 1}),
            ("Heisenberg", {"k": 2}),
        ])
        assert result["sum"] == Fraction(3)

    def test_kappa_additivity_mixed(self):
        """kappa(H_1 + Vir_1) = 1 + 1/2 = 3/2."""
        result = verify_kappa_additivity([
            ("Heisenberg", {"k": 1}),
            ("Virasoro", {"c": 1}),
        ])
        assert result["sum"] == Fraction(3, 2)

    def test_complementarity_heisenberg(self):
        result = verify_complementarity("Heisenberg", k=1)
        assert result["match"]
        assert result["sum"] == Fraction(0)

    def test_complementarity_heisenberg_k3(self):
        result = verify_complementarity("Heisenberg", k=3)
        assert result["match"]
        assert result["sum"] == Fraction(0)

    def test_complementarity_affine_sl2(self):
        result = verify_complementarity("Affine_sl2", k=1)
        assert result["match"]
        assert result["sum"] == Fraction(0)

    def test_complementarity_virasoro_ap24(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        result = verify_complementarity("Virasoro", c=26)
        assert result["match"]
        assert result["sum"] == Fraction(13)

    def test_complementarity_virasoro_c0(self):
        result = verify_complementarity("Virasoro", c=0)
        assert result["match"]
        assert result["sum"] == Fraction(13)

    def test_complementarity_virasoro_selfdual(self):
        """At self-dual c=13: kappa = 13/2, kappa_dual = 13/2, sum = 13."""
        result = verify_complementarity("Virasoro", c=13)
        assert result["match"]
        assert result["kappa_A"] == Fraction(13, 2)
        assert result["kappa_A_dual"] == Fraction(13, 2)
        assert result["sum"] == Fraction(13)


# ======================================================================
#  Section 12: Weight-graded cocycle enumerator
# ======================================================================

class TestCocycleEnumerator:

    def test_heisenberg_degree0(self):
        enum = HochschildCocycleEnumerator("Heisenberg", weight_bound=4)
        # Degree 0, weight 0: single map a -> a (identity on gen)
        dim = enum.cochain_dimension(0, 0)
        assert dim == 1

    def test_affine_sl2_degree0(self):
        enum = HochschildCocycleEnumerator("Affine_sl2", weight_bound=4)
        # Degree 0, weight 0: endomorphisms of the 3 generators
        # preserving weight. 3 generators all weight 1, so
        # any map g_i -> g_j preserves weight. 3x3 = 9 maps.
        dim = enum.cochain_dimension(0, 0)
        assert dim == 9

    def test_virasoro_degree0(self):
        enum = HochschildCocycleEnumerator("Virasoro", weight_bound=8)
        # Degree 0, weight 0: identity on T (weight 2 -> weight 2)
        dim = enum.cochain_dimension(0, 0)
        assert dim == 1

    def test_negative_degree_zero(self):
        for family in FAMILIES:
            enum = HochschildCocycleEnumerator(family, weight_bound=4)
            assert enum.cochain_dimension(-1, 0) == 0


# ======================================================================
#  Section 13: Full derived center package
# ======================================================================

class TestFullPackage:

    def test_heisenberg_package(self):
        pkg = full_derived_center_package("Heisenberg", k=1)
        assert pkg["kappa"] == Fraction(1)
        assert pkg["shadow_depth"] == "G"
        assert pkg["calabi_yau"] is True
        assert pkg["euler_characteristic"] == 1
        assert pkg["morita_invariant_n2"] is True

    def test_affine_sl2_package(self):
        pkg = full_derived_center_package("Affine_sl2", k=1)
        assert pkg["kappa"] == Fraction(9, 4)
        assert pkg["shadow_depth"] == "L"
        assert pkg["HH_dimensions"][1] == 3
        assert pkg["calabi_yau"] is True

    def test_virasoro_package(self):
        pkg = full_derived_center_package("Virasoro", c=26)
        assert pkg["kappa"] == Fraction(13)
        assert pkg["shadow_depth"] == "M"
        assert pkg["calabi_yau"] is True
        assert pkg["euler_characteristic"] == 1

    def test_w3_package(self):
        pkg = full_derived_center_package("W3", c=2)
        assert pkg["kappa"] == Fraction(5, 3)  # AP1: 5c/6 = 5*2/6 = 5/3
        assert pkg["shadow_depth"] == "M"
        assert pkg["num_generators"] == 2

    def test_all_families_calabi_yau(self):
        """CY duality holds for all standard families."""
        for family in FAMILIES:
            pkg = full_derived_center_package(family)
            assert pkg["calabi_yau"] is True, (
                f"CY duality failed for {family}")

    def test_euler_characteristic_values(self):
        """Euler characteristic chi = dim HH^0 - dim HH^1 + dim HH^2.

        Heisenberg: 1 - 1 + 1 = 1
        Affine sl_2: 1 - 3 + 1 = -1
        Virasoro: 1 - 1 + 1 = 1
        W_3: 1 - 1 + 1 = 1
        """
        expected = {
            "Heisenberg": 1,
            "Affine_sl2": -1,
            "Virasoro": 1,
            "W3": 1,
        }
        for family in FAMILIES:
            pkg = full_derived_center_package(family)
            assert pkg["euler_characteristic"] == expected[family], (
                f"Euler char wrong for {family}: "
                f"got {pkg['euler_characteristic']}, expected {expected[family]}")

    def test_annulus_trace_equals_kappa(self):
        """Tr(1) = kappa for all families."""
        for family in FAMILIES:
            pkg = full_derived_center_package(family)
            assert pkg["annulus_trace_identity"] == pkg["kappa"], (
                f"Trace != kappa for {family}")
