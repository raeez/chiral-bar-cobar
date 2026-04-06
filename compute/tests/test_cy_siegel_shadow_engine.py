r"""Tests for the Siegel shadow engine: shadow tower vs Phi_10 for K3 x E.

Organized into sections:
  1.  Shadow tower F_g values (multi-path, 5 paths per genus)
  2.  Faber-Pandharipande cross-verification
  3.  Kappa values (AP20, AP48 verification)
  4.  Shadow partition function structure
  5.  Fourier-Jacobi expansion of phi_{10,1}
  6.  phi_{10,1} structural properties
  7.  BPS degeneracies and Rademacher
  8.  Genus-2 bridge
  9.  Schottky problem and higher genus
  10. Shadow-Siegel dictionary
  11. Product formula and Borcherds lift
  12. Genus-1 eta connection
  13. Charge lattice and discriminant
  14. Quantitative comparison
  15. Definitive answer tests
  16. Edge cases and consistency

Multi-path verification: >= 3 independent paths per result.
Total: >= 90 tests.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.cy_siegel_shadow_engine import (
    # Bernoulli / FP
    bernoulli_number,
    lambda_fp,
    ahat_generating_function_coefficients,
    # Shadow tower
    KAPPA_CHIRAL,
    KAPPA_BPS,
    CHI_K3,
    WEIGHT_PHI10,
    ShadowTowerK3E,
    shadow_tower_k3e,
    shadow_fg_values,
    # Fourier-Jacobi
    dedekind_eta_coefficients,
    eta_power_coefficients,
    ramanujan_tau,
    phi_10_1_fourier_coefficients,
    phi_10_1_diagonal,
    phi_10_1_leading_coefficients,
    phi_10_1_vanishes_at_z0,
    theta_decomposition_phi_10_1,
    phi_10_m_structure,
    # BPS
    bps_degeneracy_known,
    bps_asymptotic_entropy,
    rademacher_leading,
    # Bridge
    genus_2_bridge,
    genus_g_bridge,
    ShadowSiegelComparison,
    # Schottky
    schottky_data,
    higher_genus_siegel_obstruction,
    # Dictionary
    quantitative_comparison,
    shadow_does_not_produce_phi10,
    full_shadow_siegel_dictionary,
    # Product formula
    phi10_product_formula_exponents,
    verify_product_formula_consistency,
    # Genus-1
    genus1_eta_connection,
    # Charge lattice
    charge_lattice_k3e,
    # Phi_10_1 table
    compute_phi_10_1_table,
    # Multi-path
    multi_path_shadow_k3e,
    verify_kappa_not_c_over_2,
)

F = Fraction


# ============================================================================
# SECTION 1: Shadow tower F_g values (multi-path)
# ============================================================================

class TestShadowTowerFgValues:
    """F_g = kappa_ch * lambda_g^FP for K3 x E with kappa_ch = 3."""

    def test_F1_exact(self):
        """F_1 = 3 * 1/24 = 1/8."""
        tower = shadow_tower_k3e()
        assert tower.F_g(1) == F(1, 8)

    def test_F2_exact(self):
        """F_2 = 3 * 7/5760 = 7/1920."""
        tower = shadow_tower_k3e()
        assert tower.F_g(2) == F(7, 1920)

    def test_F3_exact(self):
        """F_3 = 3 * 31/967680 = 31/322560."""
        tower = shadow_tower_k3e()
        assert tower.F_g(3) == F(31, 322560)

    def test_F4_exact(self):
        """F_4 = 3 * 127/154828800 = 127/51609600."""
        tower = shadow_tower_k3e()
        expected = F(3) * F(127, 154828800)
        assert tower.F_g(4) == expected

    def test_F5_exact(self):
        """F_5 = 3 * 73/3503554560 = 73/1167851520."""
        tower = shadow_tower_k3e()
        expected = F(3) * F(73, 3503554560)
        assert tower.F_g(5) == expected

    def test_Fg_positive_all_genera(self):
        """F_g > 0 for all g >= 1 (Bernoulli signs give positive lambda_g)."""
        tower = shadow_tower_k3e()
        for g in range(1, 11):
            assert tower.F_g(g) > 0, f"F_{g} should be positive"

    def test_Fg_decreasing(self):
        """F_g is decreasing: F_1 > F_2 > F_3 > ..."""
        tower = shadow_tower_k3e()
        for g in range(1, 10):
            assert tower.F_g(g) > tower.F_g(g + 1), f"F_{g} > F_{g+1} failed"

    def test_multi_path_genus1(self):
        """5-path verification at genus 1."""
        result = multi_path_shadow_k3e(1)
        assert result['all_5_paths_agree']
        assert result['F_g'] == F(1, 8)

    def test_multi_path_genus2(self):
        """5-path verification at genus 2."""
        result = multi_path_shadow_k3e(2)
        assert result['all_5_paths_agree']
        assert result['F_g'] == F(7, 1920)

    def test_multi_path_genus3(self):
        """5-path verification at genus 3."""
        result = multi_path_shadow_k3e(3)
        assert result['all_5_paths_agree']

    def test_multi_path_genus4(self):
        """5-path verification at genus 4."""
        result = multi_path_shadow_k3e(4)
        assert result['all_5_paths_agree']

    def test_multi_path_genus5(self):
        """5-path verification at genus 5."""
        result = multi_path_shadow_k3e(5)
        assert result['all_5_paths_agree']

    def test_multi_path_additivity(self):
        """kappa(K3 x E) = kappa(K3) + kappa(E) = 2 + 1 = 3 at all genera."""
        for g in range(1, 6):
            result = multi_path_shadow_k3e(g)
            assert result['kappa_K3'] == F(2)
            assert result['kappa_E'] == F(1)
            assert result['kappa_total'] == F(3)
            assert result['path_additive'] == result['path_direct']


# ============================================================================
# SECTION 2: Faber-Pandharipande cross-verification
# ============================================================================

class TestFaberPandharipande:
    """Lambda_g^FP intersection numbers."""

    def test_lambda1(self):
        """lambda_1 = 1/24."""
        assert lambda_fp(1) == F(1, 24)

    def test_lambda2(self):
        """lambda_2 = 7/5760."""
        assert lambda_fp(2) == F(7, 5760)

    def test_lambda3(self):
        """lambda_3 = 31/967680."""
        assert lambda_fp(3) == F(31, 967680)

    def test_lambda_via_bernoulli(self):
        """Verify lambda_g via independent Bernoulli computation."""
        for g in range(1, 8):
            B_2g = bernoulli_number(2 * g)
            power = 2 ** (2 * g - 1)
            expected = F(power - 1, power) * abs(B_2g) / F(math.factorial(2 * g))
            assert lambda_fp(g) == expected, f"lambda_{g} Bernoulli check failed"

    def test_ahat_coefficients_match(self):
        """A-hat generating function coefficients = lambda_g^FP."""
        coeffs = ahat_generating_function_coefficients(7)
        for g in range(1, 8):
            assert coeffs[g] == lambda_fp(g), f"A-hat coeff at g={g} mismatch"

    def test_lambda_g_positive(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 15):
            assert lambda_fp(g) > 0, f"lambda_{g} should be positive"


# ============================================================================
# SECTION 3: Kappa values (AP20, AP48)
# ============================================================================

class TestKappaValues:
    """Two distinct kappa values: chiral (3) vs BPS (5)."""

    def test_kappa_chiral_equals_3(self):
        """kappa(Omega^ch(K3 x E)) = 3 = dim_C."""
        assert KAPPA_CHIRAL == F(3)

    def test_kappa_bps_equals_5(self):
        """kappa_BPS = chi(K3)/4 - 1 = 24/4 - 1 = 5."""
        assert KAPPA_BPS == F(5)
        assert KAPPA_BPS == F(CHI_K3, 4) - 1

    def test_kappa_chiral_not_equal_bps(self):
        """kappa_ch != kappa_BPS (AP20: different objects)."""
        assert KAPPA_CHIRAL != KAPPA_BPS

    def test_weight_phi10_is_twice_kappa_bps(self):
        """weight(Phi_10) = 10 = 2 * kappa_BPS."""
        assert WEIGHT_PHI10 == 2 * int(KAPPA_BPS)

    def test_chi_k3_equals_24(self):
        """chi(K3) = 24."""
        assert CHI_K3 == 24

    def test_kappa_not_c_over_2(self):
        """AP48: kappa(K3 x E) != c/2 in general."""
        result = verify_kappa_not_c_over_2()
        assert result['ap48_confirmed']
        assert result['kappa_equals_c']  # kappa = c = 3 for CY
        assert not result['kappa_equals_c_over_2']  # kappa != c/2

    def test_kappa_additivity(self):
        """kappa(K3 x E) = kappa(K3) + kappa(E) = 2 + 1 = 3."""
        kappa_K3 = F(2)  # dim_C(K3)
        kappa_E = F(1)   # dim_C(E)
        assert KAPPA_CHIRAL == kappa_K3 + kappa_E

    def test_kappa_ratio(self):
        """kappa_BPS / kappa_ch = 5/3."""
        assert KAPPA_BPS / KAPPA_CHIRAL == F(5, 3)


# ============================================================================
# SECTION 4: Shadow partition function structure
# ============================================================================

class TestShadowPartitionFunction:
    """Z^sh = sum F_g hbar^{2g} (AP22: power is 2g, not 2g-2)."""

    def test_shadow_pf_dict(self):
        """Shadow PF returns correct dict for first 5 genera."""
        tower = shadow_tower_k3e()
        pf = tower.shadow_partition_function(max_g=5)
        assert len(pf) == 5
        for g in range(1, 6):
            assert g in pf
            assert pf[g] == tower.F_g(g)

    def test_shadow_pf_numerical_positive(self):
        """Z^sh(hbar) > 0 for small positive hbar."""
        tower = shadow_tower_k3e()
        for hbar in [0.1, 0.5, 1.0]:
            val = tower.shadow_pf_numerical(hbar, max_g=10)
            assert val > 0, f"Z^sh({hbar}) should be positive"

    def test_shadow_pf_convergent(self):
        """Z^sh converges: successive terms decrease for |hbar| < 1."""
        tower = shadow_tower_k3e()
        hbar = 0.5
        terms = [float(tower.F_g(g)) * hbar ** (2 * g) for g in range(1, 11)]
        for i in range(len(terms) - 1):
            assert terms[i] > terms[i + 1], f"Term {i+1} not decreasing"

    def test_shadow_fg_values_function(self):
        """shadow_fg_values returns multi-path verified data."""
        results = shadow_fg_values(max_g=5)
        for g in range(1, 6):
            assert results[g]['all_paths_agree']
            assert results[g]['kappa_used'] == F(3)

    def test_shadow_pf_hbar_zero(self):
        """Z^sh(0) = 0."""
        tower = shadow_tower_k3e()
        assert tower.shadow_pf_numerical(0.0, max_g=10) == 0.0


# ============================================================================
# SECTION 5: Fourier-Jacobi expansion of phi_{10,1}
# ============================================================================

class TestFourierJacobi:
    """Fourier coefficients of phi_{10,1} = eta^{18} * theta_1^2."""

    def test_phi_10_1_sum_vanishes_at_z0(self):
        """phi_{10,1}(tau, 0) = 0: sum_l f(n,l) = 0 for each n.

        The vanishing at z=0 is NOT that f(n,0) = 0 individually.
        It is that sum_l f(n,l) = 0 for each n. The individual
        f(n,0) coefficients are generically nonzero.
        """
        result = phi_10_1_vanishes_at_z0(max_n=8)
        assert result['all_vanish'], "sum_l f(n,l) should be 0 for all n"

    def test_phi_10_1_l0_coefficients_nonzero(self):
        """The l=0 coefficients f(n,0) are generically nonzero."""
        diag = phi_10_1_diagonal(max_n=5)
        # f(1, 0) = -2 (from theta_1^2 central term)
        assert diag[1] != 0, "f(1,0) should be nonzero"
        assert diag[1] == -2, f"f(1,0) should be -2, got {diag[1]}"

    def test_phi_10_1_leading_term(self):
        """Leading coefficients: f(1,1) = 1, f(1,0) = -2, f(1,-1) = 1.

        This corresponds to q * (y - 2 + y^{-1}) = q * (y^{1/2} - y^{-1/2})^2.
        """
        coeffs = phi_10_1_fourier_coefficients(max_n=3, max_l=2)
        assert coeffs.get((1, 1), 0) == 1
        assert coeffs.get((1, 0), 0) == -2
        assert coeffs.get((1, -1), 0) == 1

    def test_phi_10_1_has_nonzero_coefficients(self):
        """phi_{10,1} has nonzero f(n, l) for l != 0."""
        coeffs = phi_10_1_fourier_coefficients(max_n=5, max_l=3)
        nonzero = {k: v for k, v in coeffs.items() if v != 0}
        assert len(nonzero) > 0, "phi_{10,1} should have nonzero coefficients"

    def test_phi_10_1_jacobi_constraint(self):
        """4n - l^2 >= 0 for all nonzero f(n, l)."""
        coeffs = phi_10_1_fourier_coefficients(max_n=8, max_l=5)
        for (n, l), val in coeffs.items():
            if val != 0:
                assert 4 * n - l * l >= 0, (
                    f"Jacobi constraint violated: n={n}, l={l}, 4n-l^2={4*n-l*l}"
                )

    def test_phi_10_1_even_weight_symmetry(self):
        """f(n, l) = f(n, -l) for weight 10 (even)."""
        coeffs = phi_10_1_fourier_coefficients(max_n=6, max_l=4)
        for (n, l), val in coeffs.items():
            if l > 0 and (n, -l) in coeffs:
                assert coeffs[(n, -l)] == val, (
                    f"Symmetry failed at n={n}, l={l}: "
                    f"f(n,l)={val}, f(n,-l)={coeffs[(n, -l)]}"
                )

    def test_phi_10_1_starts_at_q1(self):
        """First nonzero coefficients have n >= 1 (from q^1 prefactor)."""
        coeffs = phi_10_1_fourier_coefficients(max_n=5, max_l=3)
        for (n, l), val in coeffs.items():
            if val != 0:
                assert n >= 1, f"Coefficient at n={n} should not exist"

    def test_phi_10_1_table_computation(self):
        """compute_phi_10_1_table returns consistent data."""
        table = compute_phi_10_1_table(max_n=5, max_l=3)
        assert table['all_symmetric']
        assert table['all_jacobi_ok']
        assert table['num_nonzero'] > 0

    def test_phi_10_1_n1_sum_vanishes(self):
        """At n=1: f(1,1) + f(1,0) + f(1,-1) = 1 + (-2) + 1 = 0."""
        coeffs = phi_10_1_fourier_coefficients(max_n=2, max_l=2)
        total = sum(coeffs.get((1, l), 0) for l in range(-2, 3))
        assert total == 0, f"sum_l f(1,l) = {total}, should be 0"


# ============================================================================
# SECTION 6: phi_{10,1} structural properties
# ============================================================================

class TestPhi101Structure:
    """Structural properties of phi_{10,1}."""

    def test_theta_decomposition(self):
        """phi_{10,1} = eta^{18} * theta_1^2: weight and index."""
        data = theta_decomposition_phi_10_1()
        assert data['weight'] == 10
        assert data['index'] == 1
        assert data['eta_power'] == 18
        assert data['theta_power'] == 2
        assert data['vanishing_order_at_z0'] == 2

    def test_uniqueness(self):
        """phi_{10,1} is unique (dim J_{10,1}^weak = 1)."""
        data = theta_decomposition_phi_10_1()
        assert data['dim_J_10_1_weak'] == 1
        assert data['is_weak_jacobi']

    def test_is_first_fj_of_phi10(self):
        """phi_{10,1} is the first FJ coefficient of Phi_10."""
        data = theta_decomposition_phi_10_1()
        assert data['phi10_1_is_first_FJ_of_Phi10']

    def test_phi_10_m_index_m(self):
        """phi_m has weight 10 and index m."""
        for m in range(1, 4):
            data = phi_10_m_structure(m)
            assert data['weight'] == 10
            assert data['index'] == m

    def test_phi_1_uniquely_determined(self):
        """phi_1 is uniquely determined (dim = 1)."""
        data = phi_10_m_structure(1)
        assert data['is_uniquely_determined']

    def test_higher_phi_m_not_unique(self):
        """phi_m for m >= 2 has dim > 1."""
        for m in range(2, 5):
            data = phi_10_m_structure(m)
            assert not data['is_uniquely_determined']


# ============================================================================
# SECTION 7: BPS degeneracies and Rademacher
# ============================================================================

class TestBPSDegeneracies:
    """BPS state counting from 1/Phi_10."""

    def test_known_degeneracies_exist(self):
        """Known BPS degeneracies are recorded."""
        known = bps_degeneracy_known()
        assert -1 in known
        assert 0 in known

    def test_polar_term(self):
        """d(-1) = 1 (tachyon/ground state polar term)."""
        known = bps_degeneracy_known()
        assert known[-1] == 1

    def test_threshold(self):
        """d(0) = -2."""
        known = bps_degeneracy_known()
        assert known[0] == -2

    def test_asymptotic_entropy_positive(self):
        """S_BH = pi*sqrt(4D) > 0 for D > 0."""
        for D in [1, 4, 10, 100]:
            S = bps_asymptotic_entropy(D)
            assert S > 0
            assert abs(S - math.pi * math.sqrt(4 * D)) < 1e-10

    def test_asymptotic_entropy_formula(self):
        """S_BH = pi * sqrt(4D) exactly."""
        D = 100
        expected = math.pi * math.sqrt(400)
        actual = bps_asymptotic_entropy(D)
        assert abs(actual - expected) < 1e-10

    def test_rademacher_growth(self):
        """Rademacher leading term grows exponentially."""
        vals = [rademacher_leading(D) for D in [10, 50, 100]]
        # Should be monotonically increasing for large enough D
        assert vals[1] > vals[0]
        assert vals[2] > vals[1]

    def test_entropy_zero_at_D_zero(self):
        """S_BH(0) = 0."""
        assert bps_asymptotic_entropy(0) == 0.0

    def test_bps_kappa_is_5(self):
        """BPS kappa = 5, not 3 (AP20)."""
        # The weight 10 of Phi_10 = 2 * kappa_BPS
        assert WEIGHT_PHI10 == 10
        assert KAPPA_BPS == F(5)
        assert WEIGHT_PHI10 == 2 * int(KAPPA_BPS)


# ============================================================================
# SECTION 8: Genus-2 bridge
# ============================================================================

class TestGenus2Bridge:
    """The genus-2 shadow-Siegel bridge via the Torelli map."""

    def test_torelli_birational(self):
        """At g=2, the Torelli map M_2 -> A_2 is birational."""
        bridge = genus_2_bridge()
        assert bridge['torelli_birational']

    def test_F2_shadow_value(self):
        """F_2 = 7/1920 for K3 x E."""
        bridge = genus_2_bridge()
        assert bridge['F_2_shadow'] == F(7, 1920)

    def test_shadow_not_siegel_form(self):
        """F_2 is an intersection number, NOT a Siegel modular form."""
        bridge = genus_2_bridge()
        assert not bridge['shadow_is_siegel_form']
        assert bridge['shadow_is_intersection_number']

    def test_first_cusp_form_weight_10(self):
        """First Siegel cusp form has weight 10 (= chi_10 = Phi_10)."""
        bridge = genus_2_bridge()
        assert bridge['first_cusp_form_weight'] == 10

    def test_genus_2_bridge_exists(self):
        """The g=2 bridge exists (birational Torelli)."""
        comp = genus_g_bridge(2)
        assert comp.bridge_exists
        assert 'birational' in comp.bridge_type

    def test_genus_1_bridge_isomorphism(self):
        """At g=1, M_1 = A_1 (isomorphism)."""
        comp = genus_g_bridge(1)
        assert comp.bridge_exists
        assert 'isomorphism' in comp.bridge_type

    def test_genus_1_shadow_value(self):
        """F_1 = 1/8 at genus 1."""
        comp = genus_g_bridge(1)
        assert comp.shadow_value == F(1, 8)


# ============================================================================
# SECTION 9: Schottky problem and higher genus
# ============================================================================

class TestSchottkyProblem:
    """The Schottky problem: M_g strictly inside A_g for g >= 4."""

    def test_schottky_data_dimensions(self):
        """dim M_g = 3g-3, dim A_g = g(g+1)/2."""
        data = schottky_data()
        assert data[2]['dim_M_g'] == 3
        assert data[2]['dim_A_g'] == 3
        assert data[3]['dim_M_g'] == 6
        assert data[3]['dim_A_g'] == 6
        assert data[4]['dim_M_g'] == 9
        assert data[4]['dim_A_g'] == 10

    def test_no_schottky_for_g_leq_3(self):
        """No genuine Schottky obstruction for g <= 3."""
        data = schottky_data()
        for g in range(1, 4):
            assert not data[g]['genuine_schottky']

    def test_schottky_at_g4(self):
        """First genuine Schottky obstruction at g = 4."""
        data = schottky_data()
        assert data[4]['genuine_schottky']
        assert data[4]['codimension'] == 1

    def test_schottky_codimension_formula(self):
        """codim(J_g in A_g) = (g-2)(g-3)/2 for g >= 4."""
        data = schottky_data()
        for g in range(4, 11):
            expected_codim = (g - 2) * (g - 3) // 2
            assert data[g]['codimension'] == expected_codim, (
                f"codim at g={g}: expected {expected_codim}, got {data[g]['codimension']}"
            )

    def test_shadow_captures_full_for_low_genus(self):
        """Shadow captures full Siegel data for g <= 3."""
        data = schottky_data()
        for g in range(1, 4):
            assert data[g]['shadow_captures_full_siegel']

    def test_shadow_misses_at_g4(self):
        """Shadow misses Schottky data at g >= 4."""
        data = schottky_data()
        for g in range(4, 8):
            assert not data[g]['shadow_captures_full_siegel']

    def test_genus_4_bridge_obstructed(self):
        """The g=4 bridge is obstructed by Schottky."""
        comp = genus_g_bridge(4)
        assert not comp.bridge_exists
        assert 'Schottky' in comp.bridge_type

    def test_higher_genus_obstruction(self):
        """higher_genus_siegel_obstruction returns correct data."""
        for g in [3, 4, 5, 6]:
            data = higher_genus_siegel_obstruction(g)
            assert data['genus'] == g
            assert data['F_g'] > 0
            if g >= 4:
                assert data['schottky_obstruction']


# ============================================================================
# SECTION 10: Shadow-Siegel dictionary
# ============================================================================

class TestShadowSiegelDictionary:
    """The full shadow-Siegel dictionary."""

    def test_full_dictionary_exists(self):
        """full_shadow_siegel_dictionary returns complete data."""
        d = full_shadow_siegel_dictionary()
        assert d['kappa_chiral'] == 3
        assert d['kappa_bps'] == 5
        assert len(d['shadow_captures']) > 0
        assert len(d['shadow_misses']) > 0

    def test_dictionary_F_values(self):
        """Dictionary contains correct F_g values."""
        d = full_shadow_siegel_dictionary()
        assert d['F_values'][1]['F_g'] == F(1, 8)
        assert d['F_values'][2]['F_g'] == F(7, 1920)

    def test_dictionary_answer(self):
        """Dictionary gives the definitive answer."""
        d = full_shadow_siegel_dictionary()
        assert 'does NOT produce Phi_10' in d['answer_to_main_question']

    def test_dictionary_bridge_genus_1(self):
        """Genus-1 bridge via eta function."""
        d = full_shadow_siegel_dictionary()
        assert 'eta' in d['bridge_genus_1']

    def test_dictionary_bridge_genus_4(self):
        """Genus >= 4 bridge obstructed by Schottky."""
        d = full_shadow_siegel_dictionary()
        assert 'Schottky' in d['bridge_genus_4_plus']


# ============================================================================
# SECTION 11: Product formula and Borcherds lift
# ============================================================================

class TestProductFormula:
    """Borcherds product formula for Phi_10."""

    def test_c0_minus1_equals_2(self):
        """c_0(-1) = 2 (determines leading monomial q*y*p)."""
        exponents = phi10_product_formula_exponents()
        assert exponents[-1] == 2

    def test_c0_zero_equals_minus2(self):
        """c_0(0) = -2 (threshold)."""
        exponents = phi10_product_formula_exponents()
        assert exponents[0] == -2

    def test_c0_3_equals_minus48(self):
        """c_0(3) = -48 (from K3 BPS spectrum)."""
        exponents = phi10_product_formula_exponents()
        assert exponents[3] == -48

    def test_product_formula_consistency(self):
        """Product formula passes structural checks."""
        result = verify_product_formula_consistency()
        assert result['borcherds_consistent']
        assert result['c_0_minus1'] == 2

    def test_exponents_sign_alternation(self):
        """Product formula exponents have expected sign pattern."""
        exponents = phi10_product_formula_exponents()
        # c_0(-1) = 2 > 0, c_0(0) = -2 < 0
        assert exponents[-1] > 0
        assert exponents[0] < 0


# ============================================================================
# SECTION 12: Genus-1 eta connection
# ============================================================================

class TestGenus1Eta:
    """The genus-1 shadow-eta connection."""

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa_ch / 24 = 1/8."""
        result = genus1_eta_connection()
        assert result['F_1_shadow'] == F(1, 8)
        assert result['F1_equals_kappa_over_24']

    def test_eta_power_minus6(self):
        """Z_1 = eta^{-6}: eta power = -2*kappa_ch = -6."""
        result = genus1_eta_connection()
        assert result['eta_power'] == F(-6)

    def test_c_eff_equals_kappa(self):
        """For CY sigma models: c_eff = kappa_ch = dim_C."""
        result = genus1_eta_connection()
        assert result['kappa_ch_equals_c_eff']
        assert result['c_eff'] == F(3)

    def test_bps_kappa_mismatch(self):
        """F_1 with kappa_BPS = 5 gives different value."""
        result = genus1_eta_connection()
        assert result['bps_kappa_mismatch']
        assert result['F_1_bps'] == F(5, 24)
        assert result['F_1_bps'] != result['F_1_shadow']


# ============================================================================
# SECTION 13: Charge lattice and discriminant
# ============================================================================

class TestChargeLattice:
    """Charge lattice structure for K3 x S^1 BPS states."""

    def test_lattice_is_narain(self):
        """The charge lattice is Narain Gamma^{6,22}."""
        data = charge_lattice_k3e()
        assert 'Narain' in data['lattice']

    def test_discriminant_formula(self):
        """D = Q_e^2 * Q_m^2 - (Q_e . Q_m)^2."""
        data = charge_lattice_k3e()
        assert 'Q_e^2 * Q_m^2' in data['discriminant']

    def test_t_duality_invariance(self):
        """BPS degeneracy depends only on D (T-duality invariant)."""
        data = charge_lattice_k3e()
        assert data['t_duality_invariant']

    def test_generating_function(self):
        """Z_BPS = 1/Phi_10."""
        data = charge_lattice_k3e()
        assert '1/Phi_10' in data['bps_generating_function']


# ============================================================================
# SECTION 14: Quantitative comparison
# ============================================================================

class TestQuantitativeComparison:
    """Quantitative shadow vs BPS comparison."""

    def test_kappa_ratio_5_over_3(self):
        """kappa_BPS / kappa_ch = 5/3 at all genera."""
        result = quantitative_comparison(max_g=5)
        assert result['kappa_ratio'] == F(5, 3)

    def test_ratio_uniform(self):
        """The ratio F_g^{BPS} / F_g^{shadow} = 5/3 uniformly."""
        result = quantitative_comparison(max_g=5)
        for g in range(1, 6):
            assert result['genera'][g]['ratio_equals_5_over_3']

    def test_shadow_values_correct(self):
        """Shadow values match independent computation."""
        result = quantitative_comparison(max_g=3)
        assert result['genera'][1]['F_g_shadow'] == F(1, 8)
        assert result['genera'][2]['F_g_shadow'] == F(7, 1920)

    def test_bps_values_different(self):
        """BPS-kappa values differ from shadow values."""
        result = quantitative_comparison(max_g=3)
        for g in range(1, 4):
            assert result['genera'][g]['F_g_bps_kappa'] != result['genera'][g]['F_g_shadow']

    def test_bps_kappa_F1(self):
        """F_1 with kappa_BPS = 5: F_1^{BPS} = 5/24."""
        result = quantitative_comparison()
        assert result['genera'][1]['F_g_bps_kappa'] == F(5, 24)


# ============================================================================
# SECTION 15: Definitive answer tests
# ============================================================================

class TestDefinitiveAnswer:
    """The shadow tower does NOT produce Phi_10."""

    def test_answer_is_no(self):
        """The definitive answer is NO."""
        result = shadow_does_not_produce_phi10()
        assert result['answer'] is False

    def test_categorical_gap(self):
        """Categorical gap: intersection number vs modular form."""
        result = shadow_does_not_produce_phi10()
        assert 'intersection number' in result['categorical_gap']

    def test_kappa_gap(self):
        """Kappa gap: 3 vs 5."""
        result = shadow_does_not_produce_phi10()
        assert '3' in result['kappa_gap']
        assert '5' in result['kappa_gap']

    def test_genus_gap(self):
        """Genus gap: all g vs genus 2."""
        result = shadow_does_not_produce_phi10()
        assert 'genus 2' in result['genus_gap']

    def test_connection_via_integration(self):
        """The connection goes through integration, not identification."""
        result = shadow_does_not_produce_phi10()
        assert 'integration' in result['what_connects_them'].lower() or \
               'integrates' in result['what_connects_them'].lower()


# ============================================================================
# SECTION 16: Edge cases and consistency
# ============================================================================

class TestEdgeCasesConsistency:
    """Edge cases, Bernoulli numbers, Ramanujan tau, eta coefficients."""

    def test_bernoulli_known_values(self):
        """Verify known Bernoulli numbers."""
        assert bernoulli_number(0) == F(1)
        assert bernoulli_number(1) == F(-1, 2)
        assert bernoulli_number(2) == F(1, 6)
        assert bernoulli_number(4) == F(-1, 30)
        assert bernoulli_number(6) == F(1, 42)

    def test_bernoulli_odd_vanish(self):
        """B_{2k+1} = 0 for k >= 1."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert bernoulli_number(n) == F(0)

    def test_ramanujan_tau_known(self):
        """Known Ramanujan tau values."""
        assert ramanujan_tau(1) == 1
        assert ramanujan_tau(2) == -24
        assert ramanujan_tau(3) == 252
        assert ramanujan_tau(4) == -1472
        assert ramanujan_tau(5) == 4830

    def test_eta24_is_ramanujan_tau(self):
        """eta^{24} coefficients = Ramanujan tau function."""
        coeffs = dedekind_eta_coefficients(10)
        for n in range(1, 6):
            assert coeffs.get(n, 0) == ramanujan_tau(n), (
                f"eta^24 coeff at n={n}: {coeffs.get(n, 0)} != tau({n}) = {ramanujan_tau(n)}"
            )

    def test_eta_power_at_0(self):
        """prod(1-q^n)^k has constant term 1."""
        for k in [1, 6, 18, 24]:
            coeffs = eta_power_coefficients(k, 5)
            assert coeffs.get(0, 0) == 1

    def test_eta18_first_coefficients(self):
        """eta^{18} product coefficients at low order."""
        coeffs = eta_power_coefficients(18, 3)
        # prod(1-q^n)^{18} = 1 - 18q + 135q^2 - 480q^3 + ...
        assert coeffs[0] == 1
        assert coeffs[1] == -18

    def test_lambda_fp_raises_for_g0(self):
        """lambda_fp(0) raises ValueError."""
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_shadow_tower_default_kappa(self):
        """Default shadow tower has kappa_chiral = 3."""
        tower = ShadowTowerK3E()
        assert tower.kappa_chiral == F(3)
        assert tower.kappa_bps == F(5)

    def test_shadow_numerical_matches_exact(self):
        """Numerical F_g matches exact computation."""
        tower = shadow_tower_k3e()
        for g in range(1, 8):
            exact = float(tower.F_g(g))
            numerical = tower.F_g_numerical(g)
            assert abs(exact - numerical) < 1e-15

    def test_genus_g_bridge_returns_correct_type(self):
        """genus_g_bridge returns ShadowSiegelComparison."""
        for g in range(1, 6):
            comp = genus_g_bridge(g)
            assert isinstance(comp, ShadowSiegelComparison)
            assert comp.genus == g

    def test_schottky_codim_zero_for_g2_g3(self):
        """codim = 0 for g = 2, 3 (dim M_g = dim A_g)."""
        data = schottky_data()
        assert data[2]['codimension'] == 0
        assert data[3]['codimension'] == 0

    def test_schottky_codim_grows(self):
        """Schottky codimension grows quadratically."""
        data = schottky_data()
        for g in range(4, 10):
            assert data[g]['codimension'] > data[g - 1]['codimension'] or g == 4
