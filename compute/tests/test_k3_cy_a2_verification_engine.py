r"""Tests for the CY-A_2 verification engine applied to K3 surfaces.

Verifies the complete chain:
  D^b(Coh(K3)) --Phi--> E_2-chiral algebra A_{K3}
with all invariants cross-checked against manuscript sources.

Sources:
  Vol III cy_to_chiral.tex: Theorem CY-A_2 (thm:cy-to-chiral)
  Vol III cy_categories.tex: Example ex:hh-k3, Theorem thm:cy-d-d2
  Vol I toroidal_elliptic.tex: Proposition prop:kappa-k3
  Vol I cy_lattice_voa_k3_engine.py: lattice/shadow data
  Vol I cy_factorization_envelope_k3_engine.py: boundary algebra
"""

import pytest
from fractions import Fraction

from compute.lib.k3_cy_a2_verification_engine import (
    # Hodge data
    k3_hodge,
    K3_COMPLEX_DIM,
    # Topological invariants
    euler_characteristic_topological,
    euler_characteristic_holomorphic,
    noether_formula,
    # HH data
    hh_dimensions_k3,
    hh_total_dimension,
    hh_euler_characteristic,
    chi_cy_categorical,
    # Phi(D^b(K3)) properties
    phi_k3_central_charge,
    phi_k3_kappa_ch,
    phi_k3_kappa_ch_not_c_over_2,
    phi_k3_r_matrix_level,
    phi_k3_r_matrix_vanishes_at_zero_level,
    # Decomposition
    generator_decomposition,
    h11_lattice_data,
    mukai_lattice_from_hh,
    # Shadow class
    shadow_class_analysis,
    # Genus expansion
    faber_pandharipande_lambda,
    genus_expansion_phi_k3,
    # Cross-checks
    cross_check_with_sigma_model,
    cross_check_with_boundary_algebra,
    # Hodge consistency
    hodge_diamond_consistency,
    # Complete package
    phi_k3_complete_verification,
)


# =========================================================================
# Section 1: K3 Hodge diamond
# =========================================================================

class TestK3HodgeDiamond:
    """Verify the K3 Hodge diamond is internally consistent."""

    def test_h00(self):
        # VERIFIED [DC] [LT: Beauville VIII]
        assert k3_hodge(0, 0) == 1

    def test_h10(self):
        # VERIFIED [DC]: K3 simply connected, h^{1,0} = 0
        assert k3_hodge(1, 0) == 0

    def test_h01(self):
        # VERIFIED [DC]: Hodge symmetry h^{0,1} = h^{1,0} = 0
        assert k3_hodge(0, 1) == 0

    def test_h20(self):
        # VERIFIED [DC] [LT: CY_2 condition h^{2,0} = 1]
        assert k3_hodge(2, 0) == 1

    def test_h11(self):
        # VERIFIED [DC] [LT: Beauville, Noether formula constraint]
        assert k3_hodge(1, 1) == 20

    def test_h02(self):
        # VERIFIED [DC]: Hodge symmetry h^{0,2} = h^{2,0} = 1
        assert k3_hodge(0, 2) == 1

    def test_h22(self):
        # VERIFIED [DC] [LT: compact surface, h^{2,2} = 1]
        assert k3_hodge(2, 2) == 1

    def test_h21_vanishes(self):
        # VERIFIED [DC]: h^{2,1} = h^{1,2} = 0 by Hodge symmetry + h^{1,0}=0
        assert k3_hodge(2, 1) == 0

    def test_h12_vanishes(self):
        # VERIFIED [DC]: h^{1,2} = 0
        assert k3_hodge(1, 2) == 0

    def test_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} for all p,q."""
        for p in range(K3_COMPLEX_DIM + 1):
            for q in range(K3_COMPLEX_DIM + 1):
                assert k3_hodge(p, q) == k3_hodge(q, p), \
                    f"Hodge symmetry fails at ({p},{q})"

    def test_serre_duality(self):
        """h^{p,q} = h^{n-p,n-q} for CY_n (n=2)."""
        n = K3_COMPLEX_DIM
        for p in range(n + 1):
            for q in range(n + 1):
                assert k3_hodge(p, q) == k3_hodge(n - p, n - q), \
                    f"Serre duality fails at ({p},{q})"

    def test_cy_condition(self):
        """h^{n,0} = 1 for CY_n."""
        assert k3_hodge(K3_COMPLEX_DIM, 0) == 1

    def test_total_hodge_numbers(self):
        """Sum of all h^{p,q} = 24."""
        # VERIFIED [DC]: 1+0+0+1+20+1+0+0+1 = 24
        # VERIFIED [CF]: chi_top(K3) = 24
        total = sum(k3_hodge(p, q)
                    for p in range(K3_COMPLEX_DIM + 1)
                    for q in range(K3_COMPLEX_DIM + 1))
        assert total == 24

    def test_all_consistency_checks(self):
        checks = hodge_diamond_consistency()
        for name, val in checks.items():
            assert val, f"Hodge consistency check failed: {name}"


# =========================================================================
# Section 2: Topological invariants
# =========================================================================

class TestTopologicalInvariants:
    """Verify topological and holomorphic Euler characteristics."""

    def test_chi_top_equals_24(self):
        # VERIFIED [DC]: alternating sum of h^{p,q}
        # VERIFIED [LT]: Beauville Ch. VIII
        assert euler_characteristic_topological() == 24

    def test_chi_hol_equals_2(self):
        # VERIFIED [DC]: 1 - 0 + 1 = 2
        # VERIFIED [LT]: Noether formula
        assert euler_characteristic_holomorphic() == Fraction(2)

    def test_noether_formula_equals_2(self):
        # VERIFIED [DC]: (0 + 24)/12 = 2
        # VERIFIED [CF]: agrees with chi(O_K3)
        assert noether_formula() == Fraction(2)

    def test_noether_agrees_with_chi_hol(self):
        """Two independent computations of chi(O_K3) agree."""
        assert noether_formula() == euler_characteristic_holomorphic()


# =========================================================================
# Section 3: Hochschild cohomology
# =========================================================================

class TestHochschildCohomology:
    """Verify HH*(D^b(Coh(K3))) dimensions via HKR."""

    def test_hh0_dim_2(self):
        # VERIFIED [DC]: H^0(O) + H^2(O) = 1 + 1 = 2
        # VERIFIED [LT]: cy_categories.tex Example ex:hh-k3
        hh = hh_dimensions_k3()
        assert hh[0] == 2

    def test_hh1_dim_20(self):
        # VERIFIED [DC]: H^0(Omega^1) + H^1(Omega^1) + H^2(Omega^1) = 0+20+0 = 20
        # VERIFIED [LT]: cy_categories.tex Example ex:hh-k3
        hh = hh_dimensions_k3()
        assert hh[1] == 20

    def test_hh2_dim_2(self):
        # VERIFIED [DC]: H^0(Omega^2) + H^1(Omega^2) + H^2(Omega^2) = 1+0+1 = 2
        # VERIFIED [LT]: cy_categories.tex Example ex:hh-k3
        hh = hh_dimensions_k3()
        assert hh[2] == 2

    def test_hh_total_24(self):
        # VERIFIED [DC]: 2 + 20 + 2 = 24
        # VERIFIED [CF]: equals chi_top(K3)
        assert hh_total_dimension() == 24

    def test_hh_total_equals_chi_top(self):
        """dim HH*(K3) = chi_top(K3) (a general identity for smooth projective)."""
        assert hh_total_dimension() == euler_characteristic_topological()

    def test_hh_euler_char(self):
        """chi(HH*) = sum (-1)^p dim HH^p = 2 - 20 + 2 = -16."""
        # VERIFIED [DC]: 2 - 20 + 2 = -16
        assert hh_euler_characteristic() == -16

    def test_chi_cy_equals_chi_hol(self):
        """chi^CY(D^b(K3)) = chi(O_K3) = 2."""
        # VERIFIED [DC] [LT: thm:cy-d-d2, rem:kappa-cat-from-chi]
        assert chi_cy_categorical() == Fraction(2)

    def test_chi_cy_not_hh_alternating_sum(self):
        """chi^CY != sum(-1)^p dim HH^p (they differ: 2 vs -16)."""
        assert chi_cy_categorical() != hh_euler_characteristic()


# =========================================================================
# Section 4: Properties of Phi(D^b(K3))
# =========================================================================

class TestPhiK3Properties:
    """Verify the invariants of the chiral algebra Phi(D^b(Coh(K3)))."""

    def test_central_charge_24(self):
        # VERIFIED [DC]: 24 generators from dim HH*(K3) = 24
        # VERIFIED [CF]: matches boundary algebra c
        assert phi_k3_central_charge() == 24

    def test_kappa_ch_equals_2(self):
        # VERIFIED [DC]: chi(O_K3) = 2
        # VERIFIED [LT]: Theorem thm:cy-d-d2
        # VERIFIED [CF]: K3 sigma model kappa_ch = 2
        # VERIFIED [LC]: Noether formula 24/12 = 2
        assert phi_k3_kappa_ch() == Fraction(2)

    def test_kappa_ch_not_c_over_2(self):
        """kappa_ch = 2 != c/2 = 12 (AP1: kappa = c/2 is Virasoro ONLY)."""
        result = phi_k3_kappa_ch_not_c_over_2()
        assert result['kappa_ch'] == Fraction(2)
        assert result['c_over_2'] == Fraction(12)
        assert result['are_equal'] is False

    def test_kappa_ch_equals_complex_dimension(self):
        """kappa_ch = d = 2 for CY_d (d=2)."""
        assert phi_k3_kappa_ch() == Fraction(K3_COMPLEX_DIM)

    def test_kappa_ch_equals_chi_hol(self):
        """kappa_ch = chi(O_K3) = 2."""
        assert phi_k3_kappa_ch() == euler_characteristic_holomorphic()


# =========================================================================
# Section 5: r-matrix
# =========================================================================

class TestRMatrix:
    """Verify r-matrix properties (AP126, AP141 compliance)."""

    def test_r_matrix_level_equals_kappa(self):
        """r(z) = kappa_ch * Omega / z, level = kappa_ch = 2."""
        # AP126: level prefix present
        assert phi_k3_r_matrix_level() == Fraction(2)

    def test_r_matrix_vanishes_at_zero_level(self):
        """AP126/AP141: r(z)|_{kappa_ch=0} = 0."""
        assert phi_k3_r_matrix_vanishes_at_zero_level() is True

    def test_r_matrix_level_positive(self):
        """Level is positive (not at critical level for this family)."""
        assert phi_k3_r_matrix_level() > 0


# =========================================================================
# Section 6: Generator decomposition
# =========================================================================

class TestGeneratorDecomposition:
    """Verify the Hodge-type decomposition of generators."""

    def test_decomposition_sums_to_24(self):
        dec = generator_decomposition()
        assert dec['total_generators'] == 24

    def test_rank_lattice_piece_20(self):
        """20 generators from H^{1,1}(K3)."""
        dec = generator_decomposition()
        assert dec['rank_lattice_piece'] == 20

    def test_extra_free_fields_4(self):
        """4 generators from H^{0,0}, H^{0,2}, H^{2,0}, H^{2,2}."""
        dec = generator_decomposition()
        assert dec['num_extra_free_fields'] == 4

    def test_decomposition_valid(self):
        """20 + 4 = 24."""
        dec = generator_decomposition()
        assert dec['decomposition_valid'] is True


# =========================================================================
# Section 7: Lattice data
# =========================================================================

class TestLatticeData:
    """Verify lattice-theoretic data."""

    def test_h11_rank_20(self):
        data = h11_lattice_data()
        assert data['rank'] == 20

    def test_h11_c_if_free(self):
        """If H^{1,1} generators are free bosons: c = 20."""
        data = h11_lattice_data()
        assert data['c_if_free'] == 20

    def test_mukai_rank_24(self):
        data = mukai_lattice_from_hh()
        assert data['rank'] == 24

    def test_mukai_signature(self):
        # VERIFIED [LT]: Mukai 1987
        data = mukai_lattice_from_hh()
        assert data['signature'] == (4, 20)

    def test_mukai_even_unimodular(self):
        data = mukai_lattice_from_hh()
        assert data['is_even'] is True
        assert data['is_unimodular'] is True

    def test_mukai_decomposition(self):
        data = mukai_lattice_from_hh()
        assert data['decomposition'] == 'U^4 + (-E_8)^2'


# =========================================================================
# Section 8: Shadow class
# =========================================================================

class TestShadowClass:
    """Verify shadow class analysis for Phi(D^b(K3))."""

    def test_bracket_target_vanishes(self):
        """H^2(T_K3) = h^{1,2} = 0, so [HH^1, HH^1] -> 0."""
        analysis = shadow_class_analysis()
        assert analysis['h12_target_of_bracket'] == 0
        assert analysis['bracket_hh1_hh1_vanishes'] is True

    def test_no_global_vector_fields(self):
        """H^0(T_K3) = h^{1,0} = 0."""
        analysis = shadow_class_analysis()
        assert analysis['no_global_vector_fields'] is True

    def test_hh3_vanishes(self):
        """HH^3(K3) = 0."""
        analysis = shadow_class_analysis()
        assert analysis['hh3_vanishes'] is True

    def test_classical_lie_conformal_abelian(self):
        """At cohomology level, Gerstenhaber bracket on HH*(K3) vanishes."""
        analysis = shadow_class_analysis()
        assert analysis['classical_lie_conformal_abelian'] is True

    def test_classical_class_G(self):
        """Classical shadow class is G (Gaussian, free fields)."""
        analysis = shadow_class_analysis()
        assert analysis['classical_shadow_class'] == 'G'

    def test_classical_shadow_depth_2(self):
        """Classical shadow depth r_max = 2."""
        analysis = shadow_class_analysis()
        assert analysis['classical_shadow_depth'] == 2

    def test_quantum_caveat_present(self):
        """Engine records the quantum corrections caveat."""
        analysis = shadow_class_analysis()
        assert 'quantum' in analysis['quantum_corrections_caveat'].lower()


# =========================================================================
# Section 9: Genus expansion
# =========================================================================

class TestGenusExpansion:
    """Verify genus expansion F_g = kappa_ch * lambda_g^FP."""

    def test_F1(self):
        """F_1 = 2 * 1/24 = 1/12."""
        # VERIFIED [DC]: 2/24 = 1/12
        # VERIFIED [CF]: matches K3 sigma model
        fg = genus_expansion_phi_k3()
        assert fg[1] == Fraction(1, 12)

    def test_F2(self):
        """F_2 = 2 * 7/5760 = 7/2880."""
        # VERIFIED [DC]: 2 * 7/5760 = 14/5760 = 7/2880
        fg = genus_expansion_phi_k3()
        assert fg[2] == Fraction(7, 2880)

    def test_F3(self):
        """F_3 = 2 * 31/967680 = 31/483840."""
        # VERIFIED [DC]: 2 * 31/967680 = 62/967680 = 31/483840
        fg = genus_expansion_phi_k3()
        assert fg[3] == Fraction(31, 483840)

    def test_F1_sigma_model_agreement(self):
        """F_1 agrees with K3 sigma model genus-1 obstruction."""
        fg = genus_expansion_phi_k3()
        sigma_F1 = Fraction(2) * Fraction(1, 24)
        assert fg[1] == sigma_F1

    def test_genus_expansion_ratio(self):
        """F_g(Phi(K3)) / F_g(boundary A_E) = kappa_ch/kappa_bdy = 2/24 = 1/12."""
        fg = genus_expansion_phi_k3()
        boundary_kappa = Fraction(24)
        for g in range(1, 6):
            boundary_Fg = boundary_kappa * faber_pandharipande_lambda(g)
            ratio = fg[g] / boundary_Fg
            assert ratio == Fraction(1, 12), f"Ratio mismatch at g={g}"


# =========================================================================
# Section 10: Cross-checks with existing engines
# =========================================================================

class TestCrossChecks:
    """Cross-check against K3 sigma model and boundary algebra."""

    def test_sigma_model_kappas_agree(self):
        """Phi(D^b(K3)) and K3 sigma model share kappa_ch = 2."""
        xc = cross_check_with_sigma_model()
        assert xc['kappas_agree'] is True

    def test_sigma_model_c_differs(self):
        """Phi(D^b(K3)) has c=24, sigma model has c=6."""
        xc = cross_check_with_sigma_model()
        assert xc['central_charges_differ'] is True
        assert xc['phi_k3_c'] == 24
        assert xc['sigma_model_c'] == 6

    def test_sigma_model_F1_agrees(self):
        """F_1 = 1/12 for both."""
        xc = cross_check_with_sigma_model()
        assert xc['F1_agree'] is True

    def test_boundary_c_agrees(self):
        """Phi(D^b(K3)) and boundary algebra both have c=24."""
        xc = cross_check_with_boundary_algebra()
        assert xc['central_charges_agree'] is True

    def test_boundary_kappas_differ(self):
        """Phi(D^b(K3)) kappa_ch=2, boundary kappa=24."""
        xc = cross_check_with_boundary_algebra()
        assert xc['kappas_differ'] is True

    def test_boundary_both_class_G(self):
        """Both are class G at classical level."""
        xc = cross_check_with_boundary_algebra()
        assert xc['both_class_G_classical'] is True


# =========================================================================
# Section 11: Not-a-lattice-VOA verification
# =========================================================================

class TestNotLatticeVOA:
    """Verify that Phi(D^b(K3)) is NOT a standard lattice VOA.

    A rank-r lattice VOA has c = r and kappa = r.
    Phi(D^b(K3)) has c = 24 but kappa_ch = 2, so it is NOT
    a rank-24 lattice VOA (which would have kappa = 24).

    Similarly, "rank-20 lattice + 4 free fields" would give
    kappa = 20 + 4 = 24, not 2.

    The kappa_ch = 2 arises from the CY Euler characteristic
    chi(O_K3) = 2, which involves cancellations in the supertrace.
    """

    def test_not_rank_24_lattice_voa(self):
        """A rank-24 lattice VOA has kappa=24; Phi(D^b(K3)) has kappa_ch=2."""
        rank_24_lattice_kappa = 24  # kappa = rank for lattice VOAs
        assert phi_k3_kappa_ch() != rank_24_lattice_kappa

    def test_not_rank_20_plus_4_lattice_voa(self):
        """rank-20 + rank-4 lattice VOA has kappa = 20+4 = 24 != 2."""
        combined_lattice_kappa = 20 + 4  # kappa = rank for each piece
        assert phi_k3_kappa_ch() != combined_lattice_kappa

    def test_kappa_discrepancy_explanation(self):
        """The kappa_ch = 2 comes from chi(O_K3) = 2, involving sign cancellations.

        In the supertrace computation:
          kappa_ch = sum (-1)^{weight shift} * (contribution per HH^p)
        The Hodge-graded generators have alternating signs that cancel
        most of the c=24 down to kappa_ch=2.
        """
        # The supertrace of the identity on HH^{bullet+1} generators
        # with the CY grading gives chi^CY = chi(O_K3) = 2.
        assert phi_k3_kappa_ch() == euler_characteristic_holomorphic()
        assert phi_k3_central_charge() == hh_total_dimension()

    def test_c_and_kappa_are_independent(self):
        """c = 24 and kappa_ch = 2 are genuinely different invariants."""
        c = phi_k3_central_charge()
        kappa = phi_k3_kappa_ch()
        assert c == 24
        assert kappa == Fraction(2)
        assert c != int(kappa)


# =========================================================================
# Section 12: Complete verification package
# =========================================================================

class TestCompleteVerification:
    """Run the complete verification and check all assertions."""

    def test_complete_package_runs(self):
        """The complete verification assembles without error."""
        result = phi_k3_complete_verification()
        assert isinstance(result, dict)

    def test_chi_top(self):
        result = phi_k3_complete_verification()
        assert result['chi_top_equals_24'] is True

    def test_chi_hol(self):
        result = phi_k3_complete_verification()
        assert result['chi_hol_equals_2'] is True

    def test_noether_agrees(self):
        result = phi_k3_complete_verification()
        assert result['noether_agrees'] is True

    def test_hh_total(self):
        result = phi_k3_complete_verification()
        assert result['hh_total_24'] is True

    def test_hh_matches_chi_top(self):
        result = phi_k3_complete_verification()
        assert result['hh_matches_chi_top'] is True

    def test_c_24(self):
        result = phi_k3_complete_verification()
        assert result['c_equals_24'] is True

    def test_kappa_2(self):
        result = phi_k3_complete_verification()
        assert result['kappa_ch_equals_2'] is True

    def test_r_matrix_vanishes(self):
        result = phi_k3_complete_verification()
        assert result['r_matrix_vanishes_at_zero'] is True
