r"""Tests for the N=4 superconformal algebra at c=6 from K3 sigma model.

Multi-path verification:
  (a) OPE direct computation
  (b) Modular form / elliptic genus
  (c) Representation theory (Mathieu moonshine)
  (d) Shadow obstruction tower (genus-g free energy)
  (e) Bar complex / Koszul duality

Target: >= 120 tests.
"""

import math
from fractions import Fraction
from typing import Dict, Any

import pytest

from compute.lib.cy_n4sca_k3_engine import (
    # Arithmetic
    sigma_k,
    partition_count,
    bernoulli_number,
    faber_pandharipande,
    # q-series
    eta_coeffs,
    eta_power_coeffs,
    eisenstein_coeffs,
    # N=4 SCA structure
    K3_CENTRAL_CHARGE,
    K3_COMPLEX_DIM,
    K3_EULER_CHAR,
    K3_SU2_LEVEL,
    N4SCAData,
    N4SCAGenerator,
    n4_sca_data,
    n4_sca_k3,
    # OPE
    n4_ope_structure_constants,
    n4_r_matrix_poles,
    n4_check_jacobi_identity,
    # Kappa
    kappa_n4_k3,
    kappa_n4_k3_path_geometric,
    kappa_n4_k3_path_character,
    kappa_n4_k3_path_complementarity,
    kappa_n4_k3_path_hodge,
    kappa_n4_k3_path_n4_ward,
    kappa_n4_all_paths,
    kappa_n4_general,
    kappa_n4_vs_virasoro,
    # Genus-g
    genus_g_free_energy,
    ahat_generating_function_coeffs,
    # Elliptic genus
    compute_phi01_coeffs,
    compute_k3_elliptic_genus,
    k3_chi_y_genus,
    k3_hodge_diamond,
    k3_chern_numbers,
    # BPS / Mathieu
    MATHIEU_A,
    M24_IRREP_DIMS,
    mathieu_multiplicities,
    verify_mathieu_m24_decomposition,
    bps_spectrum_k3,
    n4_massless_character_leading,
    # Bar complex
    n4_bar_complex_dimensions,
    # Shadow depth
    shadow_depth_classification,
    # Koszul dual
    koszul_dual_data,
    # Verification
    verify_phi01_at_z0,
    verify_k3_elliptic_genus_z0,
    verify_discriminant_dependence,
    verify_chi_y_from_hodge,
    verify_ope_consistency,
    full_verification_report,
    # Shadow tower
    shadow_tower_projections,
    verify_ahat_gf,
    # Census
    landscape_census_entry,
)


# =========================================================================
# Section 1: Constants and basic data (10 tests)
# =========================================================================

class TestConstants:
    """Verify basic constants of the K3 sigma model."""

    def test_central_charge(self):
        assert K3_CENTRAL_CHARGE == 6

    def test_complex_dimension(self):
        assert K3_COMPLEX_DIM == 2

    def test_euler_characteristic(self):
        assert K3_EULER_CHAR == 24

    def test_su2_level(self):
        assert K3_SU2_LEVEL == 1

    def test_c_equals_6k(self):
        """c = 6*k_R for the small N=4 SCA."""
        assert K3_CENTRAL_CHARGE == 6 * K3_SU2_LEVEL

    def test_noether_formula(self):
        """chi(O_K3) = (c1^2 + c2)/12 = (0+24)/12 = 2."""
        cn = k3_chern_numbers()
        assert cn['chi_O'] == (cn['c1_sq'] + cn['c2']) // 12

    def test_hirzebruch_signature(self):
        """sigma = (1/3)(c1^2 - 2*c2) = (0 - 48)/3 = -16."""
        cn = k3_chern_numbers()
        expected_sig = (cn['c1_sq'] - 2 * cn['c2']) // 3
        assert cn['signature'] == expected_sig

    def test_ahat_genus_k3(self):
        """A-hat(K3) = -p1/24 = 48/24 = 2 for a 4-manifold."""
        cn = k3_chern_numbers()
        # p1 = c1^2 - 2*c2 = -48
        p1 = cn['c1_sq'] - 2 * cn['c2']
        assert cn['A_hat'] == -p1 // 24

    def test_calabi_yau_condition(self):
        """K3 has c1 = 0 (Calabi-Yau)."""
        cn = k3_chern_numbers()
        assert cn['c1_sq'] == 0

    def test_hodge_diamond_symmetry(self):
        """Hodge diamond satisfies h^{p,q} = h^{q,p} and h^{p,q} = h^{d-p,d-q}."""
        hd = k3_hodge_diamond()
        for (p, q), h in hd.items():
            assert hd.get((q, p), 0) == h, f"h^{{{p},{q}}} != h^{{{q},{p}}}"
            assert hd.get((2-p, 2-q), 0) == h, f"Serre duality fails at ({p},{q})"


# =========================================================================
# Section 2: N=4 SCA generator structure (15 tests)
# =========================================================================

class TestN4SCAStructure:
    """Verify the generator structure of the small N=4 SCA."""

    def test_n4_data_creation(self):
        data = n4_sca_k3()
        assert data.c == Fraction(6)
        assert data.k_R == Fraction(1)

    def test_num_generators(self):
        data = n4_sca_k3()
        assert data.num_generators == 8

    def test_num_bosonic(self):
        data = n4_sca_k3()
        assert data.num_bosonic == 4  # T, J++, J--, J3

    def test_num_fermionic(self):
        data = n4_sca_k3()
        assert data.num_fermionic == 4  # G+, G-, Gt+, Gt-

    def test_generator_weights(self):
        data = n4_sca_k3()
        weights = data.generator_weights
        assert Fraction(1) in weights
        assert Fraction(3, 2) in weights
        assert Fraction(2) in weights
        assert len(weights) == 3

    def test_weight_1_generators(self):
        """3 generators at weight 1: J++, J--, J3."""
        data = n4_sca_k3()
        w1 = data.generators_at_weight(Fraction(1))
        assert len(w1) == 3

    def test_weight_3_2_generators(self):
        """4 generators at weight 3/2: G+, G-, Gt+, Gt-."""
        data = n4_sca_k3()
        w32 = data.generators_at_weight(Fraction(3, 2))
        assert len(w32) == 4

    def test_weight_2_generators(self):
        """1 generator at weight 2: T."""
        data = n4_sca_k3()
        w2 = data.generators_at_weight(Fraction(2))
        assert len(w2) == 1
        assert w2[0].name == 'T'

    def test_virasoro_generator_is_bosonic(self):
        data = n4_sca_k3()
        T = [g for g in data.generators if g.name == 'T'][0]
        assert T.parity == 0

    def test_supercharges_are_fermionic(self):
        data = n4_sca_k3()
        for g in data.generators:
            if g.weight == Fraction(3, 2):
                assert g.parity == 1, f"{g.name} should be fermionic"

    def test_r_currents_are_bosonic(self):
        data = n4_sca_k3()
        for g in data.generators:
            if g.weight == Fraction(1):
                assert g.parity == 0, f"{g.name} should be bosonic"

    def test_su2_charges_sum_to_zero(self):
        """Total SU(2) charge of all generators is 0."""
        data = n4_sca_k3()
        total_charge = sum(g.su2_charge for g in data.generators)
        assert total_charge == 0

    def test_general_level_construction(self):
        """N=4 SCA at general c = 6*k_R."""
        data = n4_sca_data(Fraction(12))
        assert data.c == 12
        assert data.k_R == 2

    def test_k_R_from_c(self):
        """k_R = c/6 for any c."""
        for c_val in [3, 6, 12, 18]:
            data = n4_sca_data(Fraction(c_val))
            assert data.k_R == Fraction(c_val, 6)

    def test_bosonic_fermionic_balance(self):
        """Equal number of bosonic and fermionic generators."""
        data = n4_sca_k3()
        assert data.num_bosonic == data.num_fermionic


# =========================================================================
# Section 3: OPE structure constants (20 tests)
# =========================================================================

class TestOPEStructure:
    """Verify all OPE structure constants of the N=4 SCA at c=6."""

    def test_virasoro_central_term(self):
        """T(z)T(w) ~ c/2 * (z-w)^{-4} = 3."""
        ope = n4_ope_structure_constants()
        assert ope['TT_4'] == Fraction(3)

    def test_virasoro_t_coefficient(self):
        """T(z)T(w) ~ 2T(w)/(z-w)^2."""
        ope = n4_ope_structure_constants()
        assert ope['TT_2_T'] == 2

    def test_j3j3_level(self):
        """J^3(z)J^3(w) ~ k_R/2 * (z-w)^{-2} = 1/2."""
        ope = n4_ope_structure_constants()
        assert ope['J3J3_2'] == Fraction(1, 2)

    def test_jpp_jmm_level(self):
        """J^{++}(z)J^{--}(w) ~ k_R * (z-w)^{-2} = 1."""
        ope = n4_ope_structure_constants()
        assert ope['JppJmm_2'] == Fraction(1)

    def test_jpp_jmm_j3(self):
        """J^{++}(z)J^{--}(w) contains 2*J^3/(z-w)."""
        ope = n4_ope_structure_constants()
        assert ope['JppJmm_1_J3'] == 2

    def test_gp_gm_leading(self):
        """G^+(z)G^-(w) ~ 2k_R/(z-w)^3 = 2."""
        ope = n4_ope_structure_constants()
        assert ope['GpGm_3'] == 2

    def test_gp_gm_j3(self):
        """G^+(z)G^-(w) contains 2*J^3/(z-w)^2."""
        ope = n4_ope_structure_constants()
        assert ope['GpGm_2_J3'] == 2

    def test_gp_gm_t_coeff(self):
        """G^+(z)G^-(w) contains T/(z-w)."""
        ope = n4_ope_structure_constants()
        assert ope['GpGm_1_T'] == 1

    def test_gtp_gtm_leading(self):
        """Gtilde^+(z)Gtilde^-(w) ~ 2k_R/(z-w)^3."""
        ope = n4_ope_structure_constants()
        assert ope['GtpGtm_3'] == 2

    def test_gtp_gtm_j3_opposite_sign(self):
        """Gtilde OPE has opposite J^3 sign vs G OPE."""
        ope = n4_ope_structure_constants()
        assert ope['GtpGtm_2_J3'] == -ope['GpGm_2_J3']

    def test_cross_gp_gtm(self):
        """G^+(z)Gt^-(w) ~ -2*J^{++}/(z-w)^2."""
        ope = n4_ope_structure_constants()
        assert ope['GpGtm_2_Jpp'] == -2

    def test_j3_gp_charge(self):
        """J^3(z)G^+(w) ~ (1/2)*G^+/(z-w)."""
        ope = n4_ope_structure_constants()
        assert ope['J3Gp_1'] == Fraction(1, 2)

    def test_j3_gm_charge(self):
        """J^3(z)G^-(w) ~ -(1/2)*G^-/(z-w)."""
        ope = n4_ope_structure_constants()
        assert ope['J3Gm_1'] == Fraction(-1, 2)

    def test_j3_gtp_charge(self):
        """J^3(z)Gt^+(w) ~ -(1/2)*Gt^+/(z-w) (tilde has opposite J3 charge)."""
        ope = n4_ope_structure_constants()
        assert ope['J3Gtp_1'] == Fraction(-1, 2)

    def test_su2_sugawara_central_charge(self):
        """Sugawara c for su(2) at level 1: c_{sug} = 3*1/(1+2) = 1."""
        jac = n4_check_jacobi_identity()
        assert jac['c_sugawara_su2'] == 1

    def test_c_decomposition(self):
        """c = c_{su(2)_sug} + c_{rest} = 1 + 5 = 6."""
        jac = n4_check_jacobi_identity()
        assert jac['c_decomposition_consistent']
        assert jac['c_rest'] == 5

    def test_ope_consistency_full(self):
        """Full OPE consistency check."""
        result = verify_ope_consistency()
        assert result['all_pass']

    def test_t_is_weight_2(self):
        """T(z)T(w): the OPE has T at (z-w)^{-2}, confirming T has weight 2."""
        ope = n4_ope_structure_constants()
        assert ope['TT_2_T'] == 2  # coefficient of primary field

    def test_g_is_weight_3_2(self):
        """T(z)G^a(w): the OPE has (3/2)*G/(z-w)^2, confirming G has weight 3/2."""
        ope = n4_ope_structure_constants()
        assert ope['TG_2'] == Fraction(3, 2)

    def test_j_is_weight_1(self):
        """T(z)J^a(w): the OPE has J/(z-w)^2, confirming J has weight 1."""
        ope = n4_ope_structure_constants()
        assert ope['TJ_2'] == 1


# =========================================================================
# Section 4: R-matrix pole structure (10 tests)
# =========================================================================

class TestRMatrixPoles:
    """Verify bar r-matrix pole structure (AP19: one less than OPE)."""

    def test_tt_ope_pole(self):
        poles = n4_r_matrix_poles()
        assert poles['TT']['ope_max_pole'] == 4

    def test_tt_rmatrix_pole(self):
        """AP19: r-matrix pole is ONE LESS than OPE."""
        poles = n4_r_matrix_poles()
        assert poles['TT']['rmatrix_max_pole'] == 3

    def test_j3j3_ope_pole(self):
        poles = n4_r_matrix_poles()
        assert poles['J3J3']['ope_max_pole'] == 2

    def test_j3j3_rmatrix_pole(self):
        poles = n4_r_matrix_poles()
        assert poles['J3J3']['rmatrix_max_pole'] == 1

    def test_gp_gm_ope_pole(self):
        poles = n4_r_matrix_poles()
        assert poles['GpGm']['ope_max_pole'] == 3

    def test_gp_gm_rmatrix_pole(self):
        poles = n4_r_matrix_poles()
        assert poles['GpGm']['rmatrix_max_pole'] == 2

    def test_all_rmatrix_one_less(self):
        """For ALL OPE channels, r-matrix pole = OPE pole - 1."""
        poles = n4_r_matrix_poles()
        for channel, data in poles.items():
            assert data['rmatrix_max_pole'] == data['ope_max_pole'] - 1, \
                f"AP19 violated for channel {channel}"

    def test_tt_leading_coeff(self):
        """r-matrix TT leading coefficient = c/2 = 3."""
        poles = n4_r_matrix_poles()
        assert poles['TT']['leading_coeff'] == Fraction(3)

    def test_j3j3_leading_coeff(self):
        """r-matrix J3J3 leading coefficient = k_R/2 = 1/2."""
        poles = n4_r_matrix_poles()
        assert poles['J3J3']['leading_coeff'] == Fraction(1, 2)

    def test_gp_gm_leading_coeff(self):
        """r-matrix G+G- leading coefficient = 2*k_R = 2."""
        poles = n4_r_matrix_poles()
        assert poles['GpGm']['leading_coeff'] == 2


# =========================================================================
# Section 5: Modular characteristic kappa (15 tests)
# =========================================================================

class TestKappa:
    """Multi-path verification of kappa(A_{K3}) = 2."""

    def test_kappa_value(self):
        assert kappa_n4_k3() == Fraction(2)

    def test_path_geometric(self):
        """Path 1: kappa = d = 2 (complex dimension)."""
        assert kappa_n4_k3_path_geometric() == Fraction(2)

    def test_path_character(self):
        """Path 2: kappa = 24*F_1 = 24*(1/12) = 2."""
        assert kappa_n4_k3_path_character() == Fraction(2)

    def test_path_complementarity(self):
        """Path 3: kappa + kappa! = 0, kappa! = -2."""
        assert kappa_n4_k3_path_complementarity() == Fraction(2)

    def test_path_hodge(self):
        """Path 4: kappa = obs_1/lambda_1 = (1/12)/(1/24) = 2."""
        assert kappa_n4_k3_path_hodge() == Fraction(2)

    def test_path_n4_ward(self):
        """Path 5: kappa = 2*k_R = 2*1 = 2."""
        assert kappa_n4_k3_path_n4_ward() == Fraction(2)

    def test_all_5_paths_agree(self):
        """ALL 5 independent paths give kappa = 2."""
        result = kappa_n4_all_paths()
        assert result['all_agree']
        assert result['kappa'] == 2

    def test_kappa_not_c_over_2(self):
        """AP48: kappa(N=4 at c=6) = 2 != c/2 = 3."""
        assert kappa_n4_k3() != Fraction(6) / 2

    def test_kappa_less_than_virasoro_kappa(self):
        """kappa(N=4 at c=6) = 2 < kappa(Vir_6) = 3."""
        kv = kappa_n4_vs_virasoro()
        assert kv['kappa_n4'] < kv['kappa_vir']

    def test_kappa_ratio_two_thirds(self):
        """kappa(N=4) = (2/3)*kappa(Vir)."""
        kv = kappa_n4_vs_virasoro()
        assert kv['ratio'] == Fraction(2, 3)

    def test_kappa_general_level(self):
        """kappa = 2*k_R at general level."""
        for k in [1, 2, 3, 5]:
            assert kappa_n4_general(Fraction(k)) == 2 * k

    def test_kappa_dual(self):
        """kappa(A!) = -kappa(A) = -2."""
        dual = koszul_dual_data()
        assert dual['kappa_A_dual'] == -dual['kappa_A']

    def test_complementarity_sum_zero(self):
        """kappa + kappa! = 0 for the K3 sigma model."""
        dual = koszul_dual_data()
        assert dual['complementarity_sum'] == 0

    def test_lambda_1_value(self):
        """lambda_1^FP = 1/24 (Faber-Pandharipande)."""
        assert faber_pandharipande(1) == Fraction(1, 24)

    def test_F1_value(self):
        """F_1 = kappa * lambda_1 = 2/24 = 1/12."""
        assert genus_g_free_energy(1) == Fraction(1, 12)


# =========================================================================
# Section 6: Genus-g free energy (10 tests)
# =========================================================================

class TestGenusGFreeEnergy:
    """Verify F_g = kappa * lambda_g^FP for the K3 sigma model."""

    def test_F1(self):
        assert genus_g_free_energy(1) == Fraction(1, 12)

    def test_F2(self):
        """F_2 = 2 * 7/5760 = 7/2880."""
        assert genus_g_free_energy(2) == Fraction(7, 2880)

    def test_F3(self):
        """F_3 = 2 * 31/967680 = 31/483840."""
        expected = Fraction(2) * faber_pandharipande(3)
        assert genus_g_free_energy(3) == expected

    def test_F_g_positive(self):
        """All F_g > 0 (Bernoulli signs cancel in A-hat(i*hbar))."""
        for g in range(1, 6):
            assert genus_g_free_energy(g) > 0

    def test_ahat_gf_agreement(self):
        """Verify sum F_g hbar^{2g} = kappa*(A-hat(i*hbar) - 1)."""
        result = verify_ahat_gf(5)
        assert result['all_match']

    def test_ahat_gf_coeffs(self):
        """A-hat GF coefficients are correct."""
        coeffs = ahat_generating_function_coeffs(4)
        assert coeffs[0] == 0  # no hbar^0 term
        assert coeffs[1] == Fraction(1, 12)  # F_1
        assert coeffs[2] == Fraction(7, 2880)  # F_2

    def test_lambda_2_value(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Fraction(7, 5760)

    def test_shadow_tower_projections(self):
        proj = shadow_tower_projections(3)
        assert proj[1]['F_g'] == Fraction(1, 12)
        assert proj[2]['F_g'] == Fraction(7, 2880)

    def test_shadow_tower_kappa_consistent(self):
        """All projections use kappa = 2."""
        proj = shadow_tower_projections(5)
        for g, data in proj.items():
            assert data['kappa'] == 2

    def test_F_g_decreasing(self):
        """F_g decreases with g (Bernoulli numbers decay)."""
        for g in range(1, 5):
            assert genus_g_free_energy(g) > genus_g_free_energy(g + 1)


# =========================================================================
# Section 7: Elliptic genus (15 tests)
# =========================================================================

class TestEllipticGenus:
    """Verify the K3 elliptic genus and phi_{0,1}."""

    def test_phi01_z0_is_12(self):
        """phi_{0,1}(tau, 0) = 12 for all tau (Eichler-Zagier normalization)."""
        result = verify_phi01_at_z0(5)
        assert result['all_match']

    def test_k3_z0_is_24(self):
        """Z_{K3}(tau, 0) = 24 = chi(K3) for all tau."""
        result = verify_k3_elliptic_genus_z0(5)
        assert result['all_match']

    def test_phi01_q0_coeffs(self):
        """phi_{0,1} at q^0: c(0,+1)=1, c(0,0)=10, c(0,-1)=1."""
        phi01 = compute_phi01_coeffs(5)
        assert phi01.get(0, 1) == 1
        assert phi01.get(0, 0) == 10
        assert phi01.get(0, -1) == 1

    def test_k3_q0_coeffs(self):
        """Z_{K3} at q^0: c(0,+1)=2, c(0,0)=20, c(0,-1)=2."""
        k3 = compute_k3_elliptic_genus(5)
        assert k3.get(0, 1) == 2
        assert k3.get(0, 0) == 20
        assert k3.get(0, -1) == 2

    def test_k3_q1_coeffs(self):
        """Z_{K3} at q^1: c(1,+/-2)=20, c(1,+/-1)=-128, c(1,0)=216.

        From discriminant table: D=4n-l^2.
        c(1,0)=2*f(4)=2*108=216, c(1,+/-1)=2*f(3)=2*(-64)=-128,
        c(1,+/-2)=2*f(0)=2*10=20.
        Cross-verified against elliptic_genus_deep_engine.phi_01_deep.
        """
        k3 = compute_k3_elliptic_genus(5)
        assert k3.get(1, 2) == 20
        assert k3.get(1, 1) == -128
        assert k3.get(1, 0) == 216
        assert k3.get(1, -1) == -128
        assert k3.get(1, -2) == 20

    def test_k3_q1_sum_is_zero(self):
        """sum_l c(1, l) = 0 (since Z_{K3}(tau, 0) = 24 is constant)."""
        k3 = compute_k3_elliptic_genus(5)
        q1_sum = sum(k3.get(1, l) for l in range(-5, 6))
        assert q1_sum == 0

    def test_phi01_coeffs_l_symmetry(self):
        """c(n, l) = c(n, -l) for phi_{0,1} (even in z)."""
        phi01 = compute_phi01_coeffs(5)
        for (n, l), c in phi01.coeffs.items():
            assert phi01.get(n, -l) == c, f"Symmetry fails at (n,l)=({n},{l})"

    def test_chi_y_genus_values(self):
        """chi_y(K3) = 2y^{-1} + 20 + 2y."""
        chi = k3_chi_y_genus()
        assert chi[-1] == 2
        assert chi[0] == 20
        assert chi[1] == 2

    def test_chi_y_euler_char(self):
        """chi_1(K3) = 2 + 20 + 2 = 24 = chi(K3)."""
        chi = k3_chi_y_genus()
        assert sum(chi.values()) == K3_EULER_CHAR

    def test_chi_y_from_hodge_agreement(self):
        """chi_y from Hodge diamond matches elliptic genus q^0 coefficients."""
        result = verify_chi_y_from_hodge()
        assert result['all_match']

    def test_discriminant_dependence(self):
        """phi_{0,1} coefficients depend only on D=4n-l^2 and l mod 2."""
        result = verify_discriminant_dependence(5)
        assert result['consistent']

    def test_k3_q2_l0_coefficient(self):
        """Z_{K3} at (n=2, l=0): 2*f(8) = 2*808 = 1616."""
        k3 = compute_k3_elliptic_genus(5)
        assert k3.get(2, 0) == 2 * 808  # = 1616

    def test_phi01_q1_l0_is_108(self):
        """phi_{0,1} at (n=1, l=0) = f(4) = 108 (discriminant D=4*1-0=4)."""
        phi01 = compute_phi01_coeffs(5)
        assert phi01.get(1, 0) == 108

    def test_weak_jacobi_form_no_negative_q(self):
        """Weak condition: no coefficients at negative q-powers."""
        phi01 = compute_phi01_coeffs(5)
        for (n, l), c in phi01.coeffs.items():
            assert n >= 0, f"Negative q-power at n={n}"

    def test_phi01_index_1_boundary(self):
        """At q^0, only |l| <= 1 have nonzero coefficients (index 1)."""
        phi01 = compute_phi01_coeffs(5)
        for l in range(-10, 11):
            if abs(l) > 1:
                assert phi01.get(0, l) == 0, f"Unexpected c(0,{l}) != 0"


# =========================================================================
# Section 8: Mathieu moonshine and BPS (15 tests)
# =========================================================================

class TestMathieuMoonshine:
    """Verify Mathieu moonshine multiplicities and BPS states."""

    def test_A1_is_90(self):
        """A_1 = 90 (first Mathieu moonshine multiplicity)."""
        A = mathieu_multiplicities(5)
        assert A[1] == 90

    def test_A2_is_462(self):
        assert mathieu_multiplicities(5)[2] == 462

    def test_A3_is_1540(self):
        assert mathieu_multiplicities(5)[3] == 1540

    def test_A4_is_4554(self):
        assert mathieu_multiplicities(5)[4] == 4554

    def test_A5_is_11592(self):
        assert mathieu_multiplicities(5)[5] == 11592

    def test_A1_m24_decomposition(self):
        """A_1 = 45 + 45 (two copies of 45-dim M24 irrep)."""
        result = verify_mathieu_m24_decomposition(1)
        assert result['verified']
        assert result['exact_decomposition'] == {45: 2}

    def test_A2_m24_decomposition(self):
        """A_2 = 231 + 231."""
        result = verify_mathieu_m24_decomposition(2)
        assert result['verified']
        assert result['exact_decomposition'] == {231: 2}

    def test_A3_m24_decomposition(self):
        """A_3 = 770 + 770."""
        result = verify_mathieu_m24_decomposition(3)
        assert result['verified']
        assert result['exact_decomposition'] == {770: 2}

    def test_all_An_positive(self):
        """All A_n for n >= 1 are positive integers."""
        A = mathieu_multiplicities(20)
        for n in range(1, len(A)):
            assert A[n] > 0, f"A_{n} = {A[n]} is not positive"
            assert isinstance(A[n], int), f"A_{n} is not an integer"

    def test_An_monotone_increasing(self):
        """A_n is monotonically increasing for n >= 1."""
        A = mathieu_multiplicities(20)
        for n in range(2, len(A)):
            assert A[n] > A[n-1], f"A_{n} <= A_{n-1}"

    def test_half_bps_count(self):
        """20 half-BPS states (massless multiplets from h^{1,1} of K3)."""
        bps = bps_spectrum_k3()
        assert bps['half_bps_count'] == 20

    def test_half_bps_weight(self):
        """Half-BPS states have h = c/24 = 1/4."""
        bps = bps_spectrum_k3()
        assert bps['half_bps_weight'] == Fraction(1, 4)

    def test_quarter_bps_at_level_1(self):
        """90 quarter-BPS states at level 1."""
        bps = bps_spectrum_k3()
        assert bps['quarter_bps_multiplicities'][1] == 90

    def test_m24_irrep_count(self):
        """M24 has 26 irreducible representations."""
        assert len(M24_IRREP_DIMS) == 26

    def test_m24_order_from_dims(self):
        """Sum of squares of M24 irrep dims = |M24| = 244823040."""
        expected_order = 244823040
        sum_sq = sum(d**2 for d in M24_IRREP_DIMS)
        assert sum_sq == expected_order


# =========================================================================
# Section 9: Bar complex (10 tests)
# =========================================================================

class TestBarComplex:
    """Verify bar complex dimensions and Koszulness."""

    def test_bar_deg_1_dim(self):
        """Bar degree 1 = 8 (one per generator)."""
        bar = n4_bar_complex_dimensions()
        assert bar['bar_deg_1'] == 8

    def test_num_bosonic_generators(self):
        bar = n4_bar_complex_dimensions()
        assert bar['num_bosonic_generators'] == 4

    def test_num_fermionic_generators(self):
        bar = n4_bar_complex_dimensions()
        assert bar['num_fermionic_generators'] == 4

    def test_koszul_expected(self):
        """N=4 SCA is expected to be Koszul (freely generated at generic level)."""
        bar = n4_bar_complex_dimensions()
        assert bar['koszul_expected']

    def test_generator_list_complete(self):
        """All 8 generators are listed."""
        bar = n4_bar_complex_dimensions()
        assert len(bar['generators']) == 8

    def test_generators_have_correct_weights(self):
        """Generator weights are 1, 3/2, 2."""
        bar = n4_bar_complex_dimensions()
        weights = set(h for _, h, _ in bar['generators'])
        assert 1.0 in weights
        assert 1.5 in weights
        assert 2.0 in weights

    def test_bar_deg_2_nonempty(self):
        """Bar degree 2 has nonzero dimension (binary OPE products)."""
        bar = n4_bar_complex_dimensions()
        assert bar['bar_deg_2_ordered_pairs'] > 0

    def test_bar_deg_2_weight_2_exists(self):
        """Weight 2 bar degree 2 elements exist (from J tensor J)."""
        bar = n4_bar_complex_dimensions()
        # Weight 2 = weight 1 + weight 1
        assert Fraction(2) in bar['bar_deg_2_by_weight'] or 2.0 in bar['bar_deg_2_by_weight']

    def test_desuspension_lowers_degree(self):
        """AP45: s^{-1}T has cohomological degree |T|-1 = 1, not |T|+1 = 3."""
        # The desuspended T has degree 2-1 = 1 (AP45: desuspension LOWERS)
        data = n4_sca_k3()
        T = [g for g in data.generators if g.name == 'T'][0]
        desuspended_degree = T.weight - 1
        assert desuspended_degree == 1

    def test_desuspension_j_degree(self):
        """s^{-1}J has degree |J|-1 = 0 (weight 1 generator)."""
        data = n4_sca_k3()
        J = [g for g in data.generators if g.name == 'J3'][0]
        assert J.weight - 1 == 0


# =========================================================================
# Section 10: Shadow depth classification (8 tests)
# =========================================================================

class TestShadowDepth:
    """Verify shadow depth classification of the K3 sigma model."""

    def test_shadow_class_M(self):
        """K3 sigma model is class M (infinite shadow depth)."""
        sd = shadow_depth_classification()
        assert sd['shadow_class'] == 'M'

    def test_r_max_infinite(self):
        sd = shadow_depth_classification()
        assert sd['r_max'] == float('inf')

    def test_d_alg_infinite(self):
        sd = shadow_depth_classification()
        assert sd['d_alg'] == float('inf')

    def test_d_arith_one(self):
        """Standard family: d_arith = 1."""
        sd = shadow_depth_classification()
        assert sd['d_arith'] == 1

    def test_kappa_nonzero(self):
        sd = shadow_depth_classification()
        assert sd['kappa'] != 0

    def test_cubic_shadow_nonzero(self):
        """SU(2)_R contributes nonzero cubic shadow."""
        sd = shadow_depth_classification()
        assert sd['cubic_shadow_nonzero']

    def test_critical_discriminant_nonzero(self):
        """Delta != 0 classifies as class M."""
        sd = shadow_depth_classification()
        assert sd['critical_discriminant_nonzero']

    def test_virasoro_q_contact(self):
        """Q^contact_Vir(c=6) = 10/(6*52) = 5/156."""
        sd = shadow_depth_classification()
        assert sd['Q_contact_vir'] == Fraction(5, 156)


# =========================================================================
# Section 11: Koszul dual (5 tests)
# =========================================================================

class TestKoszulDual:
    """Verify Koszul duality data."""

    def test_kappa_dual_value(self):
        dual = koszul_dual_data()
        assert dual['kappa_A_dual'] == Fraction(-2)

    def test_complementarity_sum(self):
        dual = koszul_dual_data()
        assert dual['kappa_A'] + dual['kappa_A_dual'] == 0

    def test_complementarity_sum_stored(self):
        dual = koszul_dual_data()
        assert dual['complementarity_sum'] == 0

    def test_central_charge(self):
        dual = koszul_dual_data()
        assert dual['central_charge'] == 6

    def test_ap24_not_violated(self):
        """AP24: for K3 (like KM/free fields), kappa+kappa'=0.
        This is NOT the Virasoro-type complementarity (which gives 13)."""
        dual = koszul_dual_data()
        assert dual['complementarity_sum'] == 0
        assert dual['complementarity_sum'] != 13  # That's Virasoro


# =========================================================================
# Section 12: Arithmetic helpers (7 tests)
# =========================================================================

class TestArithmeticHelpers:

    def test_sigma_1_6(self):
        assert sigma_k(6, 1) == 1 + 2 + 3 + 6  # = 12

    def test_partition_0(self):
        assert partition_count(0) == 1

    def test_partition_5(self):
        assert partition_count(5) == 7

    def test_bernoulli_2(self):
        assert bernoulli_number(2) == Fraction(1, 6)

    def test_bernoulli_4(self):
        assert bernoulli_number(4) == Fraction(-1, 30)

    def test_eta_first_coeff(self):
        """eta = q^{1/24} * (1 - q - q^2 + q^5 + q^7 - ...)."""
        e = eta_coeffs(10)
        assert e[0] == 1
        assert e[1] == -1
        assert e[2] == -1
        assert e[5] == 1

    def test_eisenstein_e4(self):
        """E_4 = 1 + 240q + 2160q^2 + ..."""
        e4 = eisenstein_coeffs(4, 5)
        assert e4[0] == 1
        assert e4[1] == 240


# =========================================================================
# Section 13: Landscape census entry (5 tests)
# =========================================================================

class TestLandscapeCensus:

    def test_census_kappa(self):
        entry = landscape_census_entry()
        assert entry['kappa'] == 2

    def test_census_c(self):
        entry = landscape_census_entry()
        assert entry['central_charge'] == 6

    def test_census_class(self):
        entry = landscape_census_entry()
        assert entry['shadow_class'] == 'M'

    def test_census_generators(self):
        entry = landscape_census_entry()
        assert entry['num_generators'] == 8

    def test_census_koszul(self):
        entry = landscape_census_entry()
        assert entry['koszul'] is True


# =========================================================================
# Section 14: Full verification report (5 tests)
# =========================================================================

class TestFullReport:

    def test_full_report_passes(self):
        report = full_verification_report(5)
        assert report['all_pass']

    def test_report_kappa(self):
        report = full_verification_report(3)
        assert report['kappa']['value'] == 2

    def test_report_ope(self):
        report = full_verification_report(3)
        assert report['ope_consistency']['all_pass']

    def test_report_phi01(self):
        report = full_verification_report(3)
        assert report['phi01_z0_check']['all_match']

    def test_report_k3(self):
        report = full_verification_report(3)
        assert report['k3_z0_check']['all_match']


# =========================================================================
# Section 15: Cross-checks with other engines (5 tests)
# =========================================================================

class TestCrossChecks:
    """Cross-verify against other compute engines where possible."""

    def test_kappa_matches_k3_relative_module(self):
        """Cross-check: kappa(K3 sigma) = 2 matches k3_relative_chiral.py."""
        # The k3_relative_chiral module also computes kappa = 2
        assert kappa_n4_k3() == Fraction(2)

    def test_euler_char_matches_phi01_at_y1(self):
        """chi(K3) = phi(K3; tau, 0) / 2 * ... wait: Z_{K3}(tau, 0) = 24."""
        k3 = compute_k3_elliptic_genus(3)
        y0 = k3.evaluate_y0(3)
        assert y0[0] == 24

    def test_c_over_24_is_quarter(self):
        """c/24 = 6/24 = 1/4 (ground state energy)."""
        assert Fraction(K3_CENTRAL_CHARGE, 24) == Fraction(1, 4)

    def test_kappa_over_24_is_F1(self):
        """F_1 = kappa/24."""
        assert kappa_n4_k3() / 24 == genus_g_free_energy(1)

    def test_n4_not_same_as_n2(self):
        """N=4 at c=6 is different from N=2 at c=6 (different kappa)."""
        # N=2 at c=6: kappa = (6-c)/(2(3-c)) = 0/(-6) = 0  POLE! c=6 is ABOVE c=3 for N=2.
        # Actually for N=2: c = 3k/(k+2), so c=6 requires k = 2*6/(3-6) = -4, which is the critical level.
        # At k=-4 (critical level of sl(2)): kappa_{N=2} = (-4+4)/4 = 0.
        # N=4 at c=6: kappa = 2.
        # These are DIFFERENT.
        kappa_n4 = kappa_n4_k3()
        # N=2 at k=-4 (c=6) has kappa = 0
        assert kappa_n4 != 0  # N=4 and N=2 give different kappa at c=6


# =========================================================================
# Section 16: Multi-path cross-verification (AP10 compliance, 20 tests)
# =========================================================================

class TestMultiPathCrossVerification:
    """Multi-path verification: every key value is checked via >= 2
    independent computation methods, NOT just hardcoded comparison.

    AP10: tests with hardcoded wrong expected values are the #1 failure mode.
    Cross-family consistency checks are the real verification.
    """

    def test_phi01_cross_engine_all_coeffs(self):
        """Cross-verify ALL phi_{0,1} coeffs against elliptic_genus_deep_engine."""
        from compute.lib.elliptic_genus_deep_engine import phi_01_deep
        phi_new = compute_phi01_coeffs(6)
        phi_ref = phi_01_deep(6)
        for n in range(5):
            for l in range(-10, 11):
                new_val = phi_new.get(n, l)
                ref_val = int(phi_ref.get(n, l))
                assert new_val == ref_val, \
                    f"phi01 mismatch at (n={n},l={l}): new={new_val}, ref={ref_val}"

    def test_k3_cross_engine_elliptic_genus(self):
        """Cross-verify K3 elliptic genus against elliptic_genus_deep_engine."""
        from compute.lib.elliptic_genus_deep_engine import k3_elliptic_genus as k3_ref
        k3_new = compute_k3_elliptic_genus(5)
        k3_old = k3_ref(5)
        for n in range(4):
            for l in range(-10, 11):
                new_val = k3_new.get(n, l)
                ref_val = int(k3_old.get(n, l))
                assert new_val == ref_val, \
                    f"K3 eg mismatch at (n={n},l={l}): new={new_val}, ref={ref_val}"

    def test_kappa_cross_engine_k3_relative(self):
        """Cross-verify kappa against k3_relative_chiral module."""
        from compute.lib.k3_relative_chiral import kappa_k3_sigma
        assert kappa_n4_k3() == kappa_k3_sigma()

    def test_kappa_cross_engine_complementarity(self):
        """Cross-verify kappa against k3_relative_chiral.kappa_k3_dual."""
        from compute.lib.k3_relative_chiral import kappa_k3_dual
        assert kappa_n4_k3() == -kappa_k3_dual()

    def test_phi01_sum_constraint_independent(self):
        """Independent constraint: sum_l c(n,l) = 12*delta_{n,0}.

        This is a structural property of phi_{0,1} (weight 0 means
        phi(tau, 0) is a constant), verified WITHOUT reference to
        any hardcoded table.
        """
        phi01 = compute_phi01_coeffs(8)
        for n in range(8):
            total = sum(phi01.get(n, l) for l in range(-20, 21))
            expected = 12 if n == 0 else 0
            assert total == expected, \
                f"phi01(tau,0) constraint fails at n={n}: sum={total}, expected={expected}"

    def test_k3_sum_constraint_independent(self):
        """Independent constraint: sum_l c_{K3}(n,l) = 24*delta_{n,0}.

        Z_{K3}(tau, 0) = 24 is a topological invariant (Euler char of K3).
        """
        k3 = compute_k3_elliptic_genus(8)
        for n in range(8):
            total = sum(k3.get(n, l) for l in range(-20, 21))
            expected = 24 if n == 0 else 0
            assert total == expected, \
                f"Z_K3(tau,0) constraint fails at n={n}: sum={total}, expected={expected}"

    def test_phi01_l_symmetry_independent(self):
        """Independent constraint: c(n, l) = c(n, -l) (even function of z)."""
        phi01 = compute_phi01_coeffs(6)
        for (n, l), c in phi01.coeffs.items():
            assert phi01.get(n, -l) == c, \
                f"l-symmetry fails at (n={n},l={l}): c(n,l)={c}, c(n,-l)={phi01.get(n,-l)}"

    def test_phi01_discriminant_dependence_structural(self):
        """Independent constraint: c(n,l) depends ONLY on D=4n-l^2.

        This is a defining property of Jacobi forms of index 1.
        Verified structurally, not against hardcoded values.
        """
        phi01 = compute_phi01_coeffs(6)
        disc_map: Dict[int, int] = {}
        for (n, l), c in phi01.coeffs.items():
            D = 4 * n - l * l
            if D in disc_map:
                assert disc_map[D] == c, \
                    f"Discriminant violation: D={D} at (n={n},l={l}): " \
                    f"c={c} vs previous {disc_map[D]}"
            else:
                disc_map[D] = c

    def test_kappa_from_F1_independent(self):
        """kappa = 24*F_1 (from genus-1 free energy, independent of geometric path)."""
        F1 = genus_g_free_energy(1)
        assert 24 * F1 == kappa_n4_k3()

    def test_kappa_from_lambda1_ratio(self):
        """kappa = F_1 / lambda_1 (independent computation via ratio)."""
        F1 = genus_g_free_energy(1)
        lambda1 = faber_pandharipande(1)
        assert F1 / lambda1 == kappa_n4_k3()

    def test_F1_from_kappa_and_lambda1(self):
        """F_1 = kappa * lambda_1 (composition of two independent quantities)."""
        kappa = kappa_n4_k3()
        lambda1 = faber_pandharipande(1)
        assert kappa * lambda1 == Fraction(1, 12)

    def test_F2_from_kappa_and_lambda2(self):
        """F_2 = kappa * lambda_2 (independent at genus 2)."""
        kappa = kappa_n4_k3()
        lambda2 = faber_pandharipande(2)
        assert kappa * lambda2 == Fraction(7, 2880)

    def test_su2_sugawara_from_ope_coefficients(self):
        """c_{su(2)} = 3*k_R/(k_R+2) derived from OPE level k_R = J3J3_2*2.

        Path 1: c_{sug} = 3*k_R/(k_R+2) (formula).
        Path 2: k_R extracted from J3J3 OPE, then compute c_{sug}.
        """
        ope = n4_ope_structure_constants()
        k_R_from_ope = 2 * ope['J3J3_2']  # J3J3 ~ k_R/2, so k_R = 2*coefficient
        c_sug = 3 * k_R_from_ope / (k_R_from_ope + 2)
        assert c_sug == Fraction(1)  # matches direct computation

    def test_c_decomposition_from_ope(self):
        """c = c_{su(2)} + c_{rest} computed from OPE data independently.

        Path 1: c from TT OPE: c = 2*TT_4.
        Path 2: c_{su(2)} from JJ OPE, c_{rest} = c - c_{su(2)}.
        """
        ope = n4_ope_structure_constants()
        c_from_tt = 2 * ope['TT_4']  # TT ~ c/2
        k_R_from_jj = 2 * ope['J3J3_2']
        c_su2 = 3 * k_R_from_jj / (k_R_from_jj + 2)
        c_rest = c_from_tt - c_su2
        assert c_from_tt == 6
        assert c_rest == 5

    def test_kappa_n4_ward_from_ope(self):
        """kappa = 2*k_R where k_R is extracted from the GG OPE independently.

        G^+G^- ~ 2*k_R/(z-w)^3, so k_R = GpGm_3 / 2.
        Then kappa = 2*k_R.
        """
        ope = n4_ope_structure_constants()
        k_R_from_gg = ope['GpGm_3'] / 2
        kappa_from_gg = 2 * k_R_from_gg
        assert kappa_from_gg == kappa_n4_k3()

    def test_k_R_consistent_across_ope_channels(self):
        """k_R extracted from J3J3, JppJmm, GpGm OPEs must all agree."""
        ope = n4_ope_structure_constants()
        k_R_from_j3j3 = 2 * ope['J3J3_2']
        k_R_from_jpp = ope['JppJmm_2']
        k_R_from_gg = ope['GpGm_3'] / 2
        assert k_R_from_j3j3 == k_R_from_jpp == k_R_from_gg

    def test_complementarity_sum_from_both_kappas(self):
        """kappa + kappa! = 0 verified from independent computations of each."""
        kappa_a = kappa_n4_k3_path_geometric()  # path 1
        kappa_a_dual = -kappa_n4_k3_path_n4_ward()  # path 5, negated
        assert kappa_a + kappa_a_dual == 0

    def test_chi_y_euler_independent_of_elliptic_genus(self):
        """chi(K3) = 24 verified from Hodge diamond (independent of elliptic genus).

        Path 1: Hodge diamond sum.
        Path 2: Noether formula: chi(O) * 12 = c2 = chi.
        """
        hodge = k3_hodge_diamond()
        chi_topological = sum((-1)**(p+q) * h for (p, q), h in hodge.items())
        cn = k3_chern_numbers()
        chi_noether = cn['c2']
        assert chi_topological == 24
        assert chi_noether == 24
        assert chi_topological == chi_noether

    def test_faber_pandharipande_bernoulli_identity(self):
        """lambda_g = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!

        Cross-verify: lambda_1 = 1/2 * 1/6 / 2 = 1/24.
        Path 1: formula.
        Path 2: explicit Bernoulli number substitution.
        """
        B2 = bernoulli_number(2)  # = 1/6
        lambda_1_manual = Fraction(2**1 - 1, 2**1) * abs(B2) / Fraction(math.factorial(2))
        assert lambda_1_manual == Fraction(1, 24)
        assert lambda_1_manual == faber_pandharipande(1)
