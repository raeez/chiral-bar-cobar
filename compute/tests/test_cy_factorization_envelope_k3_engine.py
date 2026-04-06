r"""Tests for factorization envelope technology on K3 chiral algebras.

Multi-path verification across 5 independent directions:
  (a) Topological data (Hodge diamond, Euler characteristic, Mukai lattice)
  (b) Character computations (q-series, Leech connection)
  (c) Shadow obstruction tower (kappa, cubic, quartic, discriminant)
  (d) DS reduction analysis (sigma model vs W-algebra)
  (e) Nishinaka envelope comparison (Lie conformal -> vertex algebra)

Target: >= 80 tests.
"""

import math
from fractions import Fraction

import pytest

from compute.lib.cy_factorization_envelope_k3_engine import (
    # Arithmetic helpers
    sigma_k,
    partition_count,
    bernoulli_number,
    faber_pandharipande,
    # q-series
    eta_coeffs,
    eta_power_coeffs,
    eisenstein_coeffs,
    # K3 topological data
    K3_HODGE,
    K3_COMPLEX_DIM,
    K3_EULER_CHAR,
    K3_BETTI,
    K3_SIGNATURE,
    MUKAI_LATTICE_RANK,
    MUKAI_LATTICE_SIGNATURE,
    K3_COHOMOLOGY_RANKS,
    ELLIPTIC_EULER_CHAR,
    K3_SIGMA_C,
    K3_SIGMA_KAPPA,
    BOUNDARY_C,
    BOUNDARY_KAPPA,
    BOUNDARY_RANK,
    N4_NUM_GENERATORS,
    N4_NUM_BOSONIC,
    N4_NUM_FERMIONIC,
    N4_SU2_LEVEL_K3,
    N4_SUGAWARA_C_SU2,
    k3_hodge_number,
    k3_euler_from_hodge,
    k3_total_betti,
    k3_chi_O,
    k3_noether,
    # Mukai pairing
    MukaiPairing,
    mukai_pairing,
    mukai_pairing_rank,
    mukai_pairing_signature,
    # Boundary algebra
    BoundaryAlgebraData,
    boundary_algebra_data,
    boundary_algebra_kappa,
    boundary_algebra_kappa_path_rank,
    boundary_algebra_kappa_path_euler,
    boundary_algebra_kappa_path_c,
    boundary_algebra_kappa_path_complementarity,
    boundary_algebra_kappa_all_paths,
    # Characters
    boundary_character_coeffs,
    boundary_character_check_leading,
    k3_sigma_character_leading,
    leech_connection,
    # Genus-g free energies
    boundary_genus_g_free_energy,
    k3_sigma_genus_g_free_energy,
    compare_free_energies,
    boundary_ahat_generating_function,
    # Shadow towers
    BoundaryShadowTower,
    boundary_shadow_tower,
    K3SigmaShadowTower,
    k3_sigma_shadow_tower,
    # DS reduction
    DSReductionAnalysis,
    ds_reduction_analysis,
    # Nishinaka
    NishinakaComparison,
    nishinaka_comparison,
    # Platonic datum
    PlatonicDatum,
    boundary_platonic_datum,
    k3_sigma_platonic_datum,
    # Koszul dual
    boundary_koszul_dual_data,
    k3_sigma_koszul_dual_data,
    # Factorization domain
    FactorizationDomainAnalysis,
    factorization_domain_analysis,
    # HS sewing
    hs_sewing_check_boundary,
    hs_sewing_check_sigma,
    # Multi-path verification
    verify_boundary_kappa_multipath,
    verify_sigma_kappa_multipath,
    full_verification_report,
    # Census
    landscape_census_entry_boundary,
    landscape_census_entry_sigma,
)

F = Fraction


# =========================================================================
# Section 1: K3 topological data (12 tests)
# =========================================================================

class TestK3TopologicalData:
    """Verify K3 topological invariants from multiple independent computations."""

    def test_euler_char_from_constant(self):
        """chi(K3) = 24 (standard result)."""
        assert K3_EULER_CHAR == 24

    def test_euler_char_from_hodge(self):
        """chi(K3) = sum (-1)^{p+q} h^{p,q} computed directly."""
        assert k3_euler_from_hodge() == 24

    def test_euler_char_two_paths_agree(self):
        """Cross-check: constant vs Hodge computation."""
        assert K3_EULER_CHAR == k3_euler_from_hodge()

    def test_complex_dim(self):
        assert K3_COMPLEX_DIM == 2

    def test_hodge_diamond_symmetry(self):
        """h^{p,q} = h^{q,p} (Hodge symmetry) and h^{p,q} = h^{2-p,2-q} (Serre duality)."""
        for (p, q), h in K3_HODGE.items():
            assert K3_HODGE.get((q, p), 0) == h, f"Hodge symmetry fails at ({p},{q})"
            assert K3_HODGE.get((2 - p, 2 - q), 0) == h, f"Serre duality fails at ({p},{q})"

    def test_betti_numbers(self):
        """b_0=1, b_1=0, b_2=22, b_3=0, b_4=1."""
        assert K3_BETTI == {0: 1, 1: 0, 2: 22, 3: 0, 4: 1}

    def test_b2_from_hodge(self):
        """b_2 = h^{2,0} + h^{1,1} + h^{0,2} = 1 + 20 + 1 = 22."""
        b2 = k3_hodge_number(2, 0) + k3_hodge_number(1, 1) + k3_hodge_number(0, 2)
        assert b2 == 22

    def test_chi_O(self):
        """chi(O_{K3}) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2."""
        assert k3_chi_O() == F(2)

    def test_noether_formula(self):
        """chi(O) = (c1^2 + c2)/12 = (0 + 24)/12 = 2."""
        assert k3_noether() == F(2)

    def test_chi_O_equals_noether(self):
        """Cross-check: Hodge computation vs Noether formula."""
        assert k3_chi_O() == k3_noether()

    def test_signature(self):
        """Hirzebruch signature = (1/3)(c1^2 - 2*c2) = (0 - 48)/3 = -16."""
        assert K3_SIGNATURE == -16

    def test_total_betti_number(self):
        """Total Betti sum = 1 + 0 + 22 + 0 + 1 = 24."""
        assert k3_total_betti() == 24


# =========================================================================
# Section 2: Mukai lattice (8 tests)
# =========================================================================

class TestMukaiLattice:
    """Verify Mukai lattice properties from independent sources."""

    def test_rank(self):
        """Mukai lattice rank = 24 = total Betti number."""
        assert mukai_pairing_rank() == 24

    def test_rank_equals_total_betti(self):
        """Cross-check: rank = sum of all Betti numbers."""
        assert mukai_pairing_rank() == k3_total_betti()

    def test_signature(self):
        """Signature = (4, 20)."""
        assert mukai_pairing_signature() == (4, 20)

    def test_signature_sum(self):
        """Signature positive + negative = rank."""
        sig = mukai_pairing_signature()
        assert sig[0] + sig[1] == mukai_pairing_rank()

    def test_h2_sublattice(self):
        """H^2(K3,Z) sublattice: rank 22, signature (3,19)."""
        mp = mukai_pairing()
        assert mp.h2_sublattice_rank() == 22
        assert mp.h2_sublattice_signature() == (3, 19)

    def test_even_unimodular(self):
        """Mukai lattice is even and unimodular."""
        mp = mukai_pairing()
        assert mp.is_even
        assert mp.is_unimodular

    def test_decomposition(self):
        """Standard decomposition: U^4 + (-E_8)^2."""
        mp = mukai_pairing()
        assert 'U^4' in mp.decomposition()
        assert 'E_8' in mp.decomposition()

    def test_discriminant(self):
        """Discriminant = (-1)^{20} = 1 for even unimodular."""
        mp = mukai_pairing()
        assert mp.discriminant == 1


# =========================================================================
# Section 3: Boundary algebra data (10 tests)
# =========================================================================

class TestBoundaryAlgebra:
    """Verify boundary algebra A_E from KS reduction."""

    def test_rank(self):
        """24 generators (one per harmonic form on K3)."""
        bdy = boundary_algebra_data()
        assert bdy.rank == 24

    def test_rank_equals_euler(self):
        """Cross-check: rank = chi(K3)."""
        assert BOUNDARY_RANK == K3_EULER_CHAR

    def test_central_charge(self):
        """c = 24 (one free boson per generator)."""
        bdy = boundary_algebra_data()
        assert bdy.central_charge == F(24)

    def test_kappa(self):
        """kappa = 24 (= rank for free bosons, AP48)."""
        bdy = boundary_algebra_data()
        assert bdy.kappa == F(24)

    def test_kappa_equals_rank(self):
        """AP48: kappa = rank for free-boson VOAs."""
        assert boundary_algebra_kappa() == F(BOUNDARY_RANK)

    def test_shadow_depth_class_G(self):
        """Class G (Gaussian) for free fields."""
        bdy = boundary_algebra_data()
        assert bdy.shadow_depth_class == 'G'

    def test_r_max_2(self):
        """Shadow tower terminates at arity 2."""
        bdy = boundary_algebra_data()
        assert bdy.r_max == 2

    def test_cubic_shadow_zero(self):
        """Cubic shadow C = 0 for abelian (free) algebra."""
        bdy = boundary_algebra_data()
        assert bdy.cubic_shadow == F(0)

    def test_quartic_Q_zero(self):
        """Quartic contact Q = 0 for class G."""
        bdy = boundary_algebra_data()
        assert bdy.quartic_Q == F(0)

    def test_critical_discriminant_zero(self):
        """Delta = 0 for class G (tower terminates)."""
        bdy = boundary_algebra_data()
        assert bdy.critical_discriminant == F(0)


# =========================================================================
# Section 4: Multi-path kappa verification — boundary (6 tests)
# =========================================================================

class TestBoundaryKappaMultipath:
    """Multi-path verification of kappa(A_E) = 24."""

    def test_path_rank(self):
        """Path 1: kappa = rank of Mukai lattice = 24."""
        assert boundary_algebra_kappa_path_rank() == F(24)

    def test_path_euler(self):
        """Path 2: kappa = chi(K3) = 24."""
        assert boundary_algebra_kappa_path_euler() == F(24)

    def test_path_level_sum(self):
        """Path 3: kappa = 24 bosons at level 1."""
        assert boundary_algebra_kappa_path_c() == F(24)

    def test_path_complementarity(self):
        """Path 4: kappa + kappa' = 0, kappa' = -24."""
        assert boundary_algebra_kappa_path_complementarity() == F(24)

    def test_all_paths_agree(self):
        """All 4 paths give kappa = 24."""
        result = boundary_algebra_kappa_all_paths()
        assert result['all_agree'] == F(1)
        assert result['kappa'] == F(24)

    def test_5_path_verification(self):
        """Full 5-path verification via verify_boundary_kappa_multipath."""
        result = verify_boundary_kappa_multipath()
        assert result['all_agree'] is True
        assert result['kappa'] == F(24)
        assert result['num_paths'] >= 5


# =========================================================================
# Section 5: Multi-path kappa verification — K3 sigma model (6 tests)
# =========================================================================

class TestSigmaKappaMultipath:
    """Multi-path verification of kappa(V_{K3}) = 2."""

    def test_geometric(self):
        """Path 1: kappa = complex dimension d = 2."""
        assert K3_SIGMA_KAPPA == K3_COMPLEX_DIM

    def test_noether(self):
        """Path 2: kappa = chi(O_{K3}) = chi(K3)/12 = 2."""
        assert k3_noether() == F(2)

    def test_genus_1(self):
        """Path 3: F_1 = kappa/24 = 1/12, hence kappa = 2."""
        F_1 = k3_sigma_genus_g_free_energy(1)
        assert F_1 == F(1, 12)
        assert F_1 * 24 == F(2)

    def test_n4_ward(self):
        """Path 4: kappa = 2*k_R = 2*1 = 2 (N=4 Ward identity)."""
        assert 2 * N4_SU2_LEVEL_K3 == K3_SIGMA_KAPPA

    def test_susy_reduction(self):
        """Path 5: kappa(Vir_6) * (2/3) = 3 * (2/3) = 2."""
        kappa_vir = F(K3_SIGMA_C, 2)
        assert kappa_vir == F(3)
        assert kappa_vir * F(2, 3) == F(2)

    def test_all_paths_agree(self):
        """All 5 paths give kappa = 2."""
        result = verify_sigma_kappa_multipath()
        assert result['all_agree'] is True
        assert result['kappa'] == F(2)
        assert result['num_paths'] >= 5


# =========================================================================
# Section 6: Character computations (10 tests)
# =========================================================================

class TestCharacterComputations:
    """Verify character coefficients from multiple independent methods."""

    def test_vacuum_coefficient(self):
        """c[0] = 1 (vacuum state)."""
        coeffs = boundary_character_coeffs(5)
        assert coeffs[0] == 1

    def test_level_1_coefficient(self):
        """c[1] = 24 (one excitation per boson)."""
        coeffs = boundary_character_coeffs(5)
        assert coeffs[1] == 24

    def test_level_2_coefficient(self):
        """c[2] = 324 (from colored partition counting)."""
        coeffs = boundary_character_coeffs(5)
        assert coeffs[2] == 324

    def test_level_2_from_combinatorics(self):
        """Cross-check: c[2] = C(25,2) + 24 = 300 + 24 = 324."""
        from_partitions = math.comb(25, 2) + 24  # {1,1} + {2}
        coeffs = boundary_character_coeffs(5)
        assert coeffs[2] == from_partitions

    def test_level_3_coefficient(self):
        """c[3] = 3200."""
        coeffs = boundary_character_coeffs(5)
        assert coeffs[3] == 3200

    def test_level_3_from_combinatorics(self):
        """Cross-check: c[3] = C(26,3) + 24*24 + 24 = 2600 + 576 + 24 = 3200."""
        # Partitions of 3 with 24 colors:
        # {1,1,1}: C(3+23, 23) = C(26, 3) = 2600
        # {2,1}: 24 * 24 = 576 (24 colors for part of size 2, 24 for part of size 1)
        # {3}: 24
        expected = math.comb(26, 3) + 24 * 24 + 24
        coeffs = boundary_character_coeffs(5)
        assert coeffs[3] == expected

    def test_leading_check(self):
        """boundary_character_check_leading verifies first 4 coefficients."""
        result = boundary_character_check_leading(10)
        assert result['all_match'] is True

    def test_leech_connection_low_terms(self):
        """Free boson and Leech VOA characters agree at q^{-1}, q^0, q^1."""
        conn = leech_connection()
        assert conn['match_at_q_minus_1'] is True
        assert conn['match_at_q_0'] is True
        assert conn['match_at_q_1'] is True

    def test_leech_divergence_at_q2(self):
        """Characters diverge at q^2 due to 196560 Leech norm-4 vectors."""
        conn = leech_connection()
        coeffs = boundary_character_coeffs(10)
        assert conn['leech_q2_coeff'] == coeffs[3] + 196560

    def test_leech_kissing_number(self):
        """Leech lattice kissing number = 196560."""
        conn = leech_connection()
        assert conn['leech_kissing'] == 196560


# =========================================================================
# Section 7: Genus-g free energies (10 tests)
# =========================================================================

class TestGenusGFreeEnergy:
    """Verify genus-g free energies from independent computations."""

    def test_boundary_F1(self):
        """F_1(A_E) = 24 * (1/24) = 1."""
        assert boundary_genus_g_free_energy(1) == F(1)

    def test_boundary_F1_from_lambda(self):
        """Cross-check: F_1 = kappa * lambda_1 = 24 * 1/24."""
        lam1 = faber_pandharipande(1)
        assert lam1 == F(1, 24)
        assert F(24) * lam1 == F(1)

    def test_boundary_F2(self):
        """F_2(A_E) = 24 * (7/5760) = 7/240."""
        assert boundary_genus_g_free_energy(2) == F(7, 240)

    def test_boundary_F2_from_bernoulli(self):
        """Cross-check: lambda_2 = (2^3-1)/2^3 * |B_4|/4! = 7/8 * (1/30)/24 = 7/5760."""
        B4 = bernoulli_number(4)
        assert B4 == F(-1, 30)
        lam2 = F(7, 8) * abs(B4) / math.factorial(4)
        assert lam2 == F(7, 5760)
        assert F(24) * lam2 == F(7, 240)

    def test_sigma_F1(self):
        """F_1(V_{K3}) = 2 * (1/24) = 1/12."""
        assert k3_sigma_genus_g_free_energy(1) == F(1, 12)

    def test_sigma_F2(self):
        """F_2(V_{K3}) = 2 * (7/5760) = 7/2880."""
        assert k3_sigma_genus_g_free_energy(2) == F(7, 2880)

    def test_ratio_constant(self):
        """F_g(A_E) / F_g(V_{K3}) = 12 for all g (ratio of kappas)."""
        result = compare_free_energies(5)
        for g in range(1, 6):
            assert result['genera'][g]['ratio'] == F(12)

    def test_ratio_equals_kappa_ratio(self):
        """The constant ratio = kappa(A_E) / kappa(V_{K3}) = 24/2 = 12."""
        result = compare_free_energies()
        assert result['kappa_ratio'] == F(12)
        assert result['constant_ratio'] == F(12)

    def test_boundary_F3(self):
        """F_3(A_E) = 24 * (31/967680) = 31/40320."""
        F3 = boundary_genus_g_free_energy(3)
        # lambda_3 = (2^5 - 1)/2^5 * |B_6|/6! = 31/32 * (1/42)/720 = 31/967680
        assert F3 == F(24) * faber_pandharipande(3)
        assert F3 == F(31, 40320)

    def test_ahat_generating_function(self):
        """Verify generating function coefficients match individual F_g."""
        gf = boundary_ahat_generating_function(6)
        for g in range(1, 6):
            assert gf[f'F_{g}'] == boundary_genus_g_free_energy(g)


# =========================================================================
# Section 8: Shadow obstruction tower — boundary (6 tests)
# =========================================================================

class TestBoundaryShadowTower:
    """Verify shadow tower for the boundary algebra (class G)."""

    def test_kappa_24(self):
        tower = boundary_shadow_tower()
        assert tower.kappa == F(24)

    def test_cubic_zero(self):
        tower = boundary_shadow_tower()
        assert tower.cubic_C == F(0)

    def test_quartic_zero(self):
        tower = boundary_shadow_tower()
        assert tower.quartic_Q == F(0)

    def test_discriminant_zero(self):
        tower = boundary_shadow_tower()
        assert tower.critical_discriminant == F(0)

    def test_perfect_square(self):
        """Q_L is a perfect square for class G (tower terminates)."""
        tower = boundary_shadow_tower()
        assert tower.is_perfect_square()

    def test_shadow_metric(self):
        """Q_L = (2*kappa)^2 = (2*24)^2 = 2304."""
        tower = boundary_shadow_tower()
        assert tower.shadow_metric_Q() == F(2304)


# =========================================================================
# Section 9: Shadow obstruction tower — K3 sigma model (8 tests)
# =========================================================================

class TestK3SigmaShadowTower:
    """Verify shadow tower for the K3 sigma model (class M)."""

    def test_kappa_2(self):
        tower = k3_sigma_shadow_tower()
        assert tower.kappa == F(2)

    def test_shadow_class_M(self):
        tower = k3_sigma_shadow_tower()
        assert tower.shadow_depth_class == 'M'

    def test_r_max_infinite(self):
        tower = k3_sigma_shadow_tower()
        assert tower.r_max == -1  # encoding infinite

    def test_virasoro_Q_contact(self):
        """Q^contact_Vir(c=6) = 10/(6*52) = 5/156."""
        tower = k3_sigma_shadow_tower()
        Q = tower.virasoro_Q_contact()
        assert Q == F(10, 6 * (5 * 6 + 22))
        assert Q == F(5, 156)

    def test_su2_kappa(self):
        """kappa(su(2)_1) = 3*(1+2)/(2*2) = 9/4."""
        tower = k3_sigma_shadow_tower()
        assert tower.su2_kappa() == F(9, 4)

    def test_sugawara_c(self):
        """c_sug(su(2)_1) = 3*1/(1+2) = 1."""
        tower = k3_sigma_shadow_tower()
        assert tower.sugawara_c() == F(1)

    def test_c_rest(self):
        """c_rest = c - c_sug = 6 - 1 = 5."""
        tower = k3_sigma_shadow_tower()
        assert tower.c_rest() == F(5)

    def test_kappa_vs_virasoro(self):
        """kappa(N=4) = 2, kappa(Vir_6) = 3, ratio = 2/3."""
        tower = k3_sigma_shadow_tower()
        comparison = tower.kappa_vs_virasoro()
        assert comparison['kappa_n4'] == F(2)
        assert comparison['kappa_vir'] == F(3)
        assert comparison['ratio'] == F(2, 3)


# =========================================================================
# Section 10: DS reduction analysis (6 tests)
# =========================================================================

class TestDSReduction:
    """Verify that the N=4 SCA is NOT a DS reduction."""

    def test_not_w_algebra(self):
        ds = ds_reduction_analysis()
        assert ds.is_w_algebra is False

    def test_not_ds_reduction(self):
        ds = ds_reduction_analysis()
        assert ds.is_ds_reduction is False

    def test_realization_sigma_model(self):
        ds = ds_reduction_analysis()
        assert ds.realization == "sigma_model"

    def test_sigma_model_decomposition(self):
        """c = 4 (bosons) + 2 (fermions) = 6."""
        ds = ds_reduction_analysis()
        decomp = ds.sigma_model_c_decomposition()
        assert decomp['c_total'] == F(6)
        assert decomp['c_bosons'] + decomp['c_fermions'] == F(6)

    def test_su2_ds_not_n4(self):
        """DS of su(2)_1 does NOT give the N=4 SCA."""
        ds = ds_reduction_analysis()
        result = ds.su2_ds_result()
        assert result['is_n4_sca'] is False

    def test_multiple_construction_routes(self):
        """At least 2 known construction routes for N=4 SCA at c=6."""
        ds = ds_reduction_analysis()
        routes = ds.n4_construction_routes()
        assert len(routes) >= 2


# =========================================================================
# Section 11: Nishinaka comparison (8 tests)
# =========================================================================

class TestNishinakaComparison:
    """Verify Nishinaka envelope construction matches expectations."""

    def test_n4_is_super(self):
        """The N=4 Lie conformal algebra is SUPER."""
        nc = nishinaka_comparison()
        data = nc.n4_lie_conformal_data()
        assert data['is_super'] is True
        assert data['is_ordinary_lie_conformal'] is False

    def test_boundary_is_ordinary(self):
        """The boundary Lie conformal algebra is ordinary (not super)."""
        nc = nishinaka_comparison()
        data = nc.boundary_lie_conformal_data()
        assert data['is_super'] is False
        assert data['is_ordinary_lie_conformal'] is True

    def test_boundary_generators_count(self):
        """24 generators in the boundary Lie conformal algebra."""
        nc = nishinaka_comparison()
        data = nc.boundary_lie_conformal_data()
        assert len(data['generators']) == 24

    def test_boundary_weights_all_one(self):
        """All boundary generators have weight 1 (currents)."""
        nc = nishinaka_comparison()
        data = nc.boundary_lie_conformal_data()
        assert all(w == 1 for w in data['weights'])

    def test_envelope_boundary_verified(self):
        """U(Cur(h_{24})) = Heisenberg rank 24 (verified)."""
        nc = nishinaka_comparison()
        result = nc.envelope_verification()
        assert result['boundary']['verified'] is True
        assert result['boundary']['c_expected'] == 24

    def test_envelope_n4_verified(self):
        """U(L_{N=4,1}) = N=4 SCA at c=6 (verified)."""
        nc = nishinaka_comparison()
        result = nc.envelope_verification()
        assert result['n4_sca']['verified'] is True
        assert result['n4_sca']['c_expected'] == 6

    def test_kappa_boundary_match(self):
        """Envelope kappa matches direct kappa for boundary algebra."""
        nc = nishinaka_comparison()
        kc = nc.kappa_comparison()
        assert kc['kappa_bdy_envelope'] == kc['kappa_bdy_direct']
        assert kc['boundary_match'] is True

    def test_kappa_n4_match(self):
        """Envelope kappa matches direct kappa for N=4 SCA."""
        nc = nishinaka_comparison()
        kc = nc.kappa_comparison()
        assert kc['kappa_n4_envelope'] == kc['kappa_n4_direct']
        assert kc['n4_match'] is True


# =========================================================================
# Section 12: Platonic datum (6 tests)
# =========================================================================

class TestPlatonicDatum:
    """Verify Platonic datum assembly."""

    def test_boundary_datum_kappa(self):
        pd = boundary_platonic_datum()
        assert pd.kappa == F(24)

    def test_boundary_datum_class_G(self):
        pd = boundary_platonic_datum()
        assert pd.shadow_class == 'G'

    def test_boundary_datum_F1(self):
        pd = boundary_platonic_datum()
        assert pd.F_g[1] == F(1)

    def test_sigma_datum_kappa(self):
        pd = k3_sigma_platonic_datum()
        assert pd.kappa == F(2)

    def test_sigma_datum_class_M(self):
        pd = k3_sigma_platonic_datum()
        assert pd.shadow_class == 'M'

    def test_boundary_datum_modular_koszul(self):
        pd = boundary_platonic_datum()
        assert pd.is_modular_koszul


# =========================================================================
# Section 13: Koszul duality (6 tests)
# =========================================================================

class TestKoszulDuality:
    """Verify Koszul dual data and complementarity."""

    def test_boundary_complementarity_sum(self):
        """kappa + kappa' = 0 for free fields (AP24)."""
        data = boundary_koszul_dual_data()
        assert data['complementarity_sum'] == F(0)

    def test_boundary_kappa_dual(self):
        """kappa(A_E^!) = -24."""
        data = boundary_koszul_dual_data()
        assert data['kappa_A_dual'] == F(-24)

    def test_boundary_not_self_dual(self):
        """A_E is NOT self-dual (AP33: H_k^! != H_{-k})."""
        data = boundary_koszul_dual_data()
        assert data['is_self_dual'] is False

    def test_sigma_complementarity_sum(self):
        """kappa + kappa' = 0 for K3 sigma model."""
        data = k3_sigma_koszul_dual_data()
        assert data['complementarity_sum'] == F(0)

    def test_sigma_kappa_dual(self):
        """kappa(V_{K3}^!) = -2."""
        data = k3_sigma_koszul_dual_data()
        assert data['kappa_A_dual'] == F(-2)

    def test_sigma_c_preserved(self):
        """Central charge preserved under Koszul duality for sigma models."""
        data = k3_sigma_koszul_dual_data()
        assert data['c'] == data['c_dual']


# =========================================================================
# Section 14: Factorization domain (3 tests)
# =========================================================================

class TestFactorizationDomain:
    """Verify factorization domain analysis."""

    def test_boundary_on_curve(self):
        fda = factorization_domain_analysis()
        assert 'Ran(E)' in fda.factorization_domain_boundary

    def test_cdr_on_surface(self):
        fda = factorization_domain_analysis()
        assert 'Ran(K3)' in fda.factorization_domain_cdr

    def test_bar_cobar_on_curve(self):
        fda = factorization_domain_analysis()
        assert 'Ran(E)' in fda.bar_cobar_applicable


# =========================================================================
# Section 15: HS-sewing convergence (4 tests)
# =========================================================================

class TestHSSewing:
    """Verify HS-sewing convergence for both algebras."""

    def test_boundary_converges(self):
        result = hs_sewing_check_boundary()
        assert result['hs_sewing_converges'] is True

    def test_sigma_converges(self):
        result = hs_sewing_check_sigma()
        assert result['hs_sewing_converges'] is True

    def test_boundary_growth_constant(self):
        """Growth constant C_24 = pi*sqrt(16) = 4*pi."""
        result = hs_sewing_check_boundary()
        expected = math.pi * 4
        assert abs(result['growth_constant'] - expected) < 1e-10

    def test_sigma_growth_constant(self):
        """Growth constant C_sigma = 2*pi*sqrt(c/6) = 2*pi."""
        result = hs_sewing_check_sigma()
        expected = 2 * math.pi
        assert abs(result['growth_constant'] - expected) < 1e-10


# =========================================================================
# Section 16: Cross-family consistency (6 tests)
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family and cross-object consistency checks."""

    def test_boundary_kappa_vs_sigma_kappa(self):
        """kappa(A_E) = 24 != kappa(V_{K3}) = 2 — DIFFERENT algebras (AP48)."""
        assert boundary_algebra_kappa() != F(K3_SIGMA_KAPPA)

    def test_boundary_c_vs_sigma_c(self):
        """c(A_E) = 24 != c(V_{K3}) = 6 — DIFFERENT central charges."""
        assert BOUNDARY_C != K3_SIGMA_C

    def test_boundary_rank_equals_mukai_rank(self):
        """rank(A_E) = rank(Mukai) = 24."""
        assert BOUNDARY_RANK == MUKAI_LATTICE_RANK

    def test_kappa_not_c_over_2_for_boundary(self):
        """AP48: kappa = rank (24) = c (24) for this family, but NOT c/2 = 12."""
        # For Heisenberg at level 1, kappa = rank = c.
        # This is a special coincidence; in general kappa != c/2.
        assert BOUNDARY_KAPPA == BOUNDARY_C  # rank = c for level-1 Heisenberg
        assert BOUNDARY_KAPPA != BOUNDARY_C // 2  # NOT c/2

    def test_k3_kappa_not_c_over_2(self):
        """AP48: kappa(V_{K3}) = 2 != c/2 = 3."""
        assert K3_SIGMA_KAPPA != K3_SIGMA_C // 2

    def test_n4_susy_reduces_kappa(self):
        """N=4 SUSY reduces kappa by factor 2/3 compared to Virasoro alone."""
        kappa_vir = F(K3_SIGMA_C, 2)  # kappa(Vir_6) = 3
        kappa_n4 = F(K3_SIGMA_KAPPA)  # kappa(N=4) = 2
        assert kappa_n4 == kappa_vir * F(2, 3)


# =========================================================================
# Section 17: Full verification report (3 tests)
# =========================================================================

class TestFullVerification:
    """Integration tests on the full verification report."""

    def test_report_has_all_sections(self):
        report = full_verification_report()
        assert 'boundary_kappa' in report
        assert 'sigma_kappa' in report
        assert 'boundary_character' in report
        assert 'leech_connection' in report
        assert 'free_energy_comparison' in report

    def test_all_kappas_verified(self):
        report = full_verification_report()
        assert report['boundary_kappa']['all_agree'] is True
        assert report['sigma_kappa']['all_agree'] is True

    def test_all_characters_match(self):
        report = full_verification_report()
        assert report['boundary_character']['all_match'] is True


# =========================================================================
# Section 18: Census entries (4 tests)
# =========================================================================

class TestCensusEntries:
    """Verify landscape census entries for both algebras."""

    def test_boundary_census(self):
        entry = landscape_census_entry_boundary()
        assert entry['kappa'] == 24
        assert entry['c'] == 24
        assert entry['shadow_class'] == 'G'

    def test_sigma_census(self):
        entry = landscape_census_entry_sigma()
        assert entry['kappa'] == 2
        assert entry['c'] == 6
        assert entry['shadow_class'] == 'M'

    def test_boundary_hs_sewing(self):
        entry = landscape_census_entry_boundary()
        assert entry['hs_sewing'] is True

    def test_sigma_hs_sewing(self):
        entry = landscape_census_entry_sigma()
        assert entry['hs_sewing'] is True


# =========================================================================
# Section 19: Arithmetic helpers verification (6 tests)
# =========================================================================

class TestArithmeticHelpers:
    """Verify arithmetic helpers against known values."""

    def test_bernoulli_2(self):
        assert bernoulli_number(2) == F(1, 6)

    def test_bernoulli_4(self):
        assert bernoulli_number(4) == F(-1, 30)

    def test_bernoulli_6(self):
        assert bernoulli_number(6) == F(1, 42)

    def test_faber_pandharipande_1(self):
        """lambda_1 = (2^1 - 1)/2^1 * |B_2|/2! = 1/2 * (1/6)/2 = 1/24."""
        assert faber_pandharipande(1) == F(1, 24)

    def test_faber_pandharipande_2(self):
        """lambda_2 = (2^3 - 1)/2^3 * |B_4|/4! = 7/8 * (1/30)/24 = 7/5760."""
        assert faber_pandharipande(2) == F(7, 5760)

    def test_partition_counts(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        assert partition_count(0) == 1
        assert partition_count(1) == 1
        assert partition_count(2) == 2
        assert partition_count(3) == 3
        assert partition_count(4) == 5
        assert partition_count(5) == 7


# =========================================================================
# Section 20: q-series cross-checks (4 tests)
# =========================================================================

class TestQSeries:
    """Cross-check q-series computations."""

    def test_eta_leading(self):
        """eta coefficients: c[0]=1, c[1]=-1, c[2]=-1."""
        ec = eta_coeffs(10)
        assert ec[0] == 1
        assert ec[1] == -1
        assert ec[2] == -1

    def test_eta_pentagonal(self):
        """Pentagonal numbers: c[k(3k-1)/2] = (-1)^k."""
        ec = eta_coeffs(30)
        # k=1: index 1 -> (-1)^1 = -1
        assert ec[1] == -1
        # k=2: index 5 -> (-1)^2 = 1
        assert ec[5] == 1
        # k=3: index 12 -> (-1)^3 = -1
        assert ec[12] == -1

    def test_eisenstein_E4(self):
        """E_4(tau) = 1 + 240*q + 2160*q^2 + ..."""
        ec = eisenstein_coeffs(4, 5)
        assert ec[0] == 1
        assert ec[1] == 240
        assert ec[2] == 2160

    def test_eisenstein_E6(self):
        """E_6(tau) = 1 - 504*q - 16632*q^2 - ..."""
        ec = eisenstein_coeffs(6, 5)
        assert ec[0] == 1
        assert ec[1] == -504
        assert ec[2] == -16632
