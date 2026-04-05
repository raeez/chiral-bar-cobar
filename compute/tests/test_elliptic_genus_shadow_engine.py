r"""Tests for elliptic_genus_shadow_engine.py — elliptic genera from shadow tower.

Tests cover:
1. phi_{0,1} Jacobi form properties (weight, index, modularity constraint)
2. K3 elliptic genus = 2*phi_{0,1}
3. Mathieu moonshine multiplicities A_n and M24 decomposition
4. Sigma-model kappa values
5. Witten genus from shadow tower
6. Mock modular forms
7. Anomaly polynomial (A-hat) matching
8. Multi-path verification (3+ independent paths per result)
9. CY3 elliptic genus properties
10. Free energy from shadow tower

MULTI-PATH VERIFICATION STRATEGY:
- K3 elliptic genus: (1) shadow tower, (2) phi_{0,1}, (3) N=4 decomposition
- Witten genus: (1) shadow, (2) index theorem, (3) loop space
- A_n: (1) tabulated values, (2) phi_{0,1} decomposition, (3) M24 representations

References:
  Eichler-Zagier, "The Theory of Jacobi Forms" (1985)
  Eguchi-Ooguri-Tachikawa, arXiv:1004.0956 (2010)
  Dabholkar-Murthy-Zagier, arXiv:1208.4074 (2012)
"""

import math
import pytest
from fractions import Fraction

from compute.lib.elliptic_genus_shadow_engine import (
    # Arithmetic helpers
    sigma_k,
    partition_number,
    bernoulli_number,
    # Modular forms
    eta_coeffs,
    eta_power_coeffs,
    e4_coeffs,
    e6_coeffs,
    e2_coeffs,
    # Jacobi forms
    JacobiForm,
    phi_01,
    phi_01_fourier,
    # K3
    k3_elliptic_genus,
    k3_witten_genus,
    k3_elliptic_genus_coefficients,
    # Mathieu moonshine
    mathieu_moonshine_multiplicities,
    verify_mathieu_multiplicities_from_phi01,
    mathieu_m24_decompositions,
    _check_m24_decomposition,
    # Sigma model
    sigma_model_kappa,
    sigma_model_shadow_tower,
    sigma_model_free_energy,
    # CY3
    quintic_cy3_elliptic_genus,
    # Witten genus
    witten_genus_from_shadow,
    witten_genus_from_index_theorem,
    witten_genus_from_loop_space,
    # Mock modular
    mock_modular_H_function,
    # Anomaly polynomial
    ahat_genus_shadow_gf,
    verify_ahat_geometric_matching,
    # Multi-path
    verify_k3_elliptic_genus_three_paths,
    verify_witten_genus_three_paths,
    # Full analysis
    full_shadow_genus_analysis,
    run_all_verifications,
)


# =====================================================================
# Section 1: Arithmetic helpers
# =====================================================================

class TestArithmeticHelpers:
    """Test basic arithmetic functions."""

    def test_sigma_k_basic(self):
        """sigma_1(6) = 1+2+3+6 = 12, sigma_3(2) = 1+8 = 9."""
        assert sigma_k(6, 1) == 12
        assert sigma_k(2, 3) == 9
        assert sigma_k(1, 0) == 1  # sigma_0(1) = 1

    def test_sigma_k_zero(self):
        assert sigma_k(0, 1) == 0
        assert sigma_k(-1, 1) == 0

    def test_partition_numbers(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        assert partition_number(0) == 1
        assert partition_number(1) == 1
        assert partition_number(2) == 2
        assert partition_number(3) == 3
        assert partition_number(4) == 5
        assert partition_number(5) == 7

    def test_bernoulli_numbers(self):
        """B_0=1, B_1=-1/2, B_2=1/6, B_4=-1/30, B_6=1/42."""
        assert bernoulli_number(0) == Fraction(1)
        assert bernoulli_number(1) == Fraction(-1, 2)
        assert bernoulli_number(2) == Fraction(1, 6)
        assert bernoulli_number(4) == Fraction(-1, 30)
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_bernoulli_odd_vanish(self):
        """B_n = 0 for odd n > 1."""
        for n in [3, 5, 7, 9, 11]:
            assert bernoulli_number(n) == 0


# =====================================================================
# Section 2: Modular forms
# =====================================================================

class TestModularForms:
    """Test q-expansions of modular forms."""

    def test_eta_leading(self):
        """eta = q^{1/24}(1 - q - q^2 + q^5 + ...) (pentagonal numbers)."""
        c = eta_coeffs(10)
        assert c[0] == 1
        assert c[1] == -1
        assert c[2] == -1
        assert c[5] == 1
        assert c[7] == 1

    def test_e4_leading(self):
        """E_4 = 1 + 240q + 2160q^2 + ..."""
        c = e4_coeffs(5)
        assert c[0] == 1
        assert c[1] == 240
        assert c[2] == 2160

    def test_e6_leading(self):
        """E_6 = 1 - 504q - 16632q^2 - ..."""
        c = e6_coeffs(5)
        assert c[0] == 1
        assert c[1] == -504
        assert c[2] == -16632

    def test_e2_leading(self):
        """E_2 = 1 - 24q - 72q^2 - ... (quasi-modular, AP15)."""
        c = e2_coeffs(5)
        assert c[0] == 1
        assert c[1] == -24
        assert c[2] == -72

    def test_eta_power_positive(self):
        """eta^3 starts with 1, -3, 0, 5, ..."""
        c = eta_power_coeffs(10, 3)
        assert c[0] == 1
        assert c[1] == -3

    def test_eta_power_negative(self):
        """eta^{-1} gives partition numbers."""
        c = eta_power_coeffs(10, -1)
        assert c[0] == 1
        assert c[1] == 1
        assert c[2] == 2
        assert c[3] == 3

    def test_eta_power_zero(self):
        """eta^0 = 1."""
        c = eta_power_coeffs(5, 0)
        assert c[0] == 1
        assert all(c[i] == 0 for i in range(1, 5))


# =====================================================================
# Section 3: Jacobi form phi_{0,1}
# =====================================================================

class TestPhi01:
    """Test the fundamental weak Jacobi form phi_{0,1}."""

    def test_phi01_z0_is_12(self):
        """phi_{0,1}(tau, 0) = 12 (constant, independent of tau)."""
        jf = phi_01(nmax=10)
        y0 = jf.evaluate_y0(nmax=10)
        assert y0[0] == 12
        for n in range(1, 10):
            assert y0[n] == 0, f"phi_01(tau, 0) has nonzero q^{n} coefficient: {y0[n]}"

    def test_phi01_q0_coefficients(self):
        """At q^0: c(0, 0)=10, c(0, +-1)=1, rest zero."""
        jf = phi_01(nmax=5)
        assert jf.get_coeff(0, 0) == 10
        assert jf.get_coeff(0, 1) == 1
        assert jf.get_coeff(0, -1) == 1
        assert jf.get_coeff(0, 2) == 0

    def test_phi01_q1_coefficients(self):
        """At q^1: c(1, 0)=108, c(1, +-1)=-64, c(1, +-2)=10."""
        jf = phi_01(nmax=5)
        assert jf.get_coeff(1, 0) == 108
        assert jf.get_coeff(1, 1) == -64
        assert jf.get_coeff(1, -1) == -64
        assert jf.get_coeff(1, 2) == 10
        assert jf.get_coeff(1, -2) == 10

    def test_phi01_discriminant_dependence(self):
        """c(n, l) depends only on D = 4n - l^2."""
        jf = phi_01(nmax=8)
        # D = 0 appears at (0,0) and (1,2): both should be 10
        assert jf.get_coeff(0, 0) == 10
        assert jf.get_coeff(1, 2) == 10
        assert jf.get_coeff(1, -2) == 10
        # D = -1 appears at (0,1) and (2,3): both should be 1
        assert jf.get_coeff(0, 1) == 1
        assert jf.get_coeff(2, 3) == 1
        # D = 4 appears at (1,0) and (2,2): both should be 108
        assert jf.get_coeff(1, 0) == 108
        assert jf.get_coeff(2, 2) == 108

    def test_phi01_symmetry(self):
        """c(n, l) = c(n, -l) (parity)."""
        jf = phi_01(nmax=5)
        for n in range(5):
            for l in range(1, 10):
                assert jf.get_coeff(n, l) == jf.get_coeff(n, -l), \
                    f"Asymmetry at (n={n}, l={l})"

    def test_phi01_weak_condition(self):
        """c(n, l) = 0 for n < 0 (weak Jacobi form)."""
        jf = phi_01(nmax=5)
        # Our representation only stores n >= 0, so this is trivially satisfied.
        # Verify no negative-n keys exist.
        for (n, l) in jf.coeffs:
            assert n >= 0

    def test_phi01_weight_and_index(self):
        """phi_{0,1} has weight 0 and index 1."""
        jf = phi_01(nmax=5)
        assert jf.weight == 0
        assert jf.index == Fraction(1)

    def test_phi01_fourier_alias(self):
        """phi_01_fourier is an alias for phi_01."""
        jf1 = phi_01(nmax=5)
        jf2 = phi_01_fourier(nmax=5)
        y01 = jf1.evaluate_y0(5)
        y02 = jf2.evaluate_y0(5)
        assert y01 == y02


# =====================================================================
# Section 4: K3 elliptic genus
# =====================================================================

class TestK3EllipticGenus:
    """Test the elliptic genus of K3 surface."""

    def test_k3_euler_characteristic(self):
        """phi(K3; tau, 0) = chi(K3) = 24."""
        k3 = k3_elliptic_genus(nmax=5)
        y0 = k3.evaluate_y0(nmax=5)
        assert y0[0] == 24

    def test_k3_is_constant(self):
        """phi(K3; tau, 0) = 24 (constant, all higher q-coefficients vanish)."""
        k3 = k3_elliptic_genus(nmax=10)
        y0 = k3.evaluate_y0(nmax=10)
        for n in range(1, 10):
            assert y0[n] == 0

    def test_k3_equals_2_phi01(self):
        """phi(K3) = 2 * phi_{0,1}."""
        base = phi_01(nmax=5)
        k3 = k3_elliptic_genus(nmax=5)
        for (n, l), c in base.coeffs.items():
            assert k3.get_coeff(n, l) == 2 * c

    def test_k3_q0_terms(self):
        """At q^0: K3 has c(0, 0)=20, c(0, +-1)=2."""
        k3 = k3_elliptic_genus(nmax=3)
        assert k3.get_coeff(0, 0) == 20
        assert k3.get_coeff(0, 1) == 2
        assert k3.get_coeff(0, -1) == 2

    def test_k3_weight_index(self):
        """K3 elliptic genus has weight 0, index 1 = dim_C(K3)/2."""
        k3 = k3_elliptic_genus(nmax=3)
        assert k3.weight == 0
        assert k3.index == Fraction(1)

    def test_k3_witten_genus_constant(self):
        """Witten genus of K3 = 24 (constant)."""
        w = k3_witten_genus(nmax=10)
        assert w[0] == 24
        for n in range(1, 10):
            assert w[n] == 0

    def test_k3_coefficients_dict(self):
        """k3_elliptic_genus_coefficients returns correct dict format."""
        coeffs = k3_elliptic_genus_coefficients(nmax=3)
        assert 0 in coeffs
        assert coeffs[0][0] == 20
        assert coeffs[0][1] == 2
        assert coeffs[0][-1] == 2


# =====================================================================
# Section 5: Mathieu moonshine
# =====================================================================

class TestMathieuMoonshine:
    """Test Mathieu moonshine multiplicities A_n (EOT 2010)."""

    def test_A1(self):
        """A_1 = 90 = 2 * 45 (two copies of 45-dim M24 irrep)."""
        A = mathieu_moonshine_multiplicities(5)
        assert A[1] == 90

    def test_A2(self):
        """A_2 = 462 = 2 * 231."""
        A = mathieu_moonshine_multiplicities(5)
        assert A[2] == 462

    def test_A3(self):
        """A_3 = 1540 = 2 * 770."""
        A = mathieu_moonshine_multiplicities(5)
        assert A[3] == 1540

    def test_A4(self):
        """A_4 = 4554 = 2 * 2277."""
        A = mathieu_moonshine_multiplicities(5)
        assert A[4] == 4554

    def test_A5(self):
        """A_5 = 11592."""
        A = mathieu_moonshine_multiplicities(6)
        assert A[5] == 11592

    def test_first_10_values(self):
        """Known A_n for n = 1, ..., 10 (Cheng 2010, OEIS A169717)."""
        A = mathieu_moonshine_multiplicities(11)
        expected = [0, 90, 462, 1540, 4554, 11592, 27830, 62100, 132210, 269640, 531894]
        for n in range(1, 11):
            assert A[n] == expected[n], f"A_{n} = {A[n]}, expected {expected[n]}"

    def test_first_20_values(self):
        """Known A_n for n = 1, ..., 20."""
        A = mathieu_moonshine_multiplicities(21)
        expected_20 = [
            0, 90, 462, 1540, 4554, 11592, 27830, 62100, 132210,
            269640, 531894, 1012452, 1873290, 3373560, 5934030,
            10211310, 17236626, 28545390, 46466580, 74446590, 117542760
        ]
        for n in range(1, 21):
            assert A[n] == expected_20[n], f"A_{n} = {A[n]}, expected {expected_20[n]}"

    def test_all_positive(self):
        """All A_n > 0 for n >= 1 (dimension of a representation)."""
        A = mathieu_moonshine_multiplicities(21)
        for n in range(1, len(A)):
            assert A[n] > 0, f"A_{n} = {A[n]} is not positive"

    def test_all_even(self):
        """All A_n are even (real M24 reps pair into complex conjugates)."""
        A = mathieu_moonshine_multiplicities(21)
        for n in range(1, len(A)):
            assert A[n] % 2 == 0, f"A_{n} = {A[n]} is odd"

    def test_m24_decomposition_A1(self):
        """A_1 = 90 = 2*45, decomposable as M24 representations."""
        M24_dims = [1, 23, 45, 45, 231, 231, 252, 253, 483, 770, 770,
                    990, 990, 1035, 1035, 1035, 1265, 1771, 2024, 2277,
                    3312, 3520, 5313, 5544, 5796, 10395]
        assert _check_m24_decomposition(90, M24_dims)

    def test_m24_decomposition_A2(self):
        """A_2 = 462 = 2*231."""
        M24_dims = [1, 23, 45, 45, 231, 231, 252, 253, 483, 770, 770,
                    990, 990, 1035, 1035, 1035, 1265, 1771, 2024, 2277,
                    3312, 3520, 5313, 5544, 5796, 10395]
        assert _check_m24_decomposition(462, M24_dims)

    def test_m24_decomposition_A3(self):
        """A_3 = 1540 = 2*770."""
        M24_dims = [1, 23, 45, 45, 231, 231, 252, 253, 483, 770, 770,
                    990, 990, 1035, 1035, 1035, 1265, 1771, 2024, 2277,
                    3312, 3520, 5313, 5544, 5796, 10395]
        assert _check_m24_decomposition(1540, M24_dims)

    def test_m24_decomposition_first_5(self):
        """A_1, ..., A_5 all decompose as M24 representations."""
        checks = verify_mathieu_multiplicities_from_phi01(5)
        for n, An, ok in checks:
            assert ok, f"A_{n} = {An} not decomposable as M24 reps"

    def test_known_decompositions(self):
        """Verify known explicit M24 decompositions."""
        decomps = mathieu_m24_decompositions()
        A = mathieu_moonshine_multiplicities(7)
        for n, parts in decomps.items():
            total = sum(d * m for d, m in parts)
            assert total == A[n], f"Decomposition sum {total} != A_{n} = {A[n]}"

    def test_m24_irrep_dimensions(self):
        """M24 has exactly 26 irreducible representations.

        Dimensions (from Atlas of Finite Groups): 1, 23, 45, 45, 231, 231,
        252, 253, 483, 770, 770, 990, 990, 1035, 1035, 1035, 1265, 1771,
        2024, 2277, 3312, 3520, 5313, 5544, 5796, 10395.
        Note THREE copies of 1035 (not two).
        Sum of squares = |M24| = 244823040.
        """
        M24_dims = sorted([1, 23, 45, 45, 231, 231, 252, 253, 483, 770, 770,
                           990, 990, 1035, 1035, 1035, 1265, 1771, 2024, 2277,
                           3312, 3520, 5313, 5544, 5796, 10395])
        assert len(M24_dims) == 26
        assert sum(d**2 for d in M24_dims) == 244823040, "M24 irrep dimension check failed"


# =====================================================================
# Section 6: Sigma-model shadow tower
# =====================================================================

class TestSigmaModelShadow:
    """Test sigma-model kappa and shadow tower."""

    def test_kappa_K3(self):
        """kappa(Omega^{ch}(K3)) = 2 (complex dimension of K3)."""
        assert sigma_model_kappa('K3_bosonic') == 2
        assert sigma_model_kappa('K3_scft') == 2

    def test_kappa_T4(self):
        """kappa(T^4) = 2 (2 complex dimensions)."""
        assert sigma_model_kappa('T4_bosonic') == 2

    def test_kappa_T2(self):
        """kappa(T^2) = 1 (1 complex dimension)."""
        assert sigma_model_kappa('T2_bosonic') == 1

    def test_kappa_CY3(self):
        """kappa(CY3) = 3 (3 complex dimensions)."""
        assert sigma_model_kappa('CY3_bosonic') == 3

    def test_shadow_tower_class_G(self):
        """CY sigma models have class G (Gaussian) shadow tower: terminates at r=2."""
        tower = sigma_model_shadow_tower('K3_bosonic', rmax=10)
        assert tower[2] == 2  # kappa = 2
        for r in range(3, 11):
            assert tower[r] == 0, f"S_{r} = {tower[r]} should be 0 for class G"

    def test_unknown_manifold_raises(self):
        """Unknown manifold raises ValueError."""
        with pytest.raises(ValueError):
            sigma_model_kappa('unknown_manifold')


# =====================================================================
# Section 7: Free energy
# =====================================================================

class TestFreeEnergy:
    """Test genus-g free energy F_g = kappa * lambda_g^FP."""

    def test_F1_K3(self):
        """F_1(K3) = kappa/24 = 2/24 = 1/12."""
        Fg = sigma_model_free_energy('K3_bosonic', gmax=1)
        assert Fg[1] == Fraction(1, 12)

    def test_F2_K3(self):
        """F_2(K3) = 2 * 7/5760 = 7/2880."""
        Fg = sigma_model_free_energy('K3_bosonic', gmax=2)
        assert Fg[2] == Fraction(7, 2880)

    def test_F3_K3(self):
        """F_3(K3) = 2 * 31/967680 = 31/483840."""
        Fg = sigma_model_free_energy('K3_bosonic', gmax=3)
        assert Fg[3] == Fraction(31, 483840)

    def test_F1_T2(self):
        """F_1(T^2) = kappa/24 = 1/24."""
        Fg = sigma_model_free_energy('T2_bosonic', gmax=1)
        assert Fg[1] == Fraction(1, 24)

    def test_free_energy_positive(self):
        """F_g > 0 for all g >= 1 (from A-hat coefficients being positive)."""
        Fg = sigma_model_free_energy('K3_bosonic', gmax=5)
        for g in range(1, 6):
            assert Fg[g] > 0

    def test_free_energy_decreasing(self):
        """F_g decreases with g (factorial suppression)."""
        Fg = sigma_model_free_energy('K3_bosonic', gmax=5)
        for g in range(2, 6):
            assert Fg[g] < Fg[g - 1]

    def test_ahat_gf(self):
        """Shadow generating function = kappa * (A-hat(i*hbar) - 1)."""
        kappa = Fraction(2)
        Fg = ahat_genus_shadow_gf(kappa, gmax=3)
        assert Fg[1] == kappa * Fraction(1, 24)
        assert Fg[2] == kappa * Fraction(7, 5760)


# =====================================================================
# Section 8: Witten genus
# =====================================================================

class TestWittenGenus:
    """Test Witten genus computation from multiple paths."""

    def test_witten_K3_shadow(self):
        """Witten genus of K3 from shadow = 24 (constant)."""
        w = witten_genus_from_shadow('K3_scft')
        assert w[0] == 24

    def test_witten_K3_index(self):
        """Witten genus of K3 from index theorem = 24."""
        w = witten_genus_from_index_theorem('K3_scft', nmax=5)
        assert w[0] == 24

    def test_witten_K3_loop(self):
        """Witten genus of K3 from loop space = 24."""
        w = witten_genus_from_loop_space('K3_scft', nmax=5)
        assert w[0] == 24

    def test_witten_torus_vanishes(self):
        """Witten genus of torus = 0."""
        for m in ['T2_bosonic', 'T4_bosonic']:
            w = witten_genus_from_shadow(m, gmax=3)
            assert w[0] == 0

    def test_witten_3path_K3(self):
        """All three paths agree for K3 Witten genus."""
        v = verify_witten_genus_three_paths('K3_scft')
        assert v['all_agree']

    def test_witten_3path_torus(self):
        """All three paths agree for T^4 Witten genus."""
        v = verify_witten_genus_three_paths('T4_bosonic')
        assert v['all_agree']


# =====================================================================
# Section 9: A-hat matching (anomaly polynomial)
# =====================================================================

class TestAhatMatching:
    """Test anomaly polynomial matching between shadow and geometry."""

    def test_ahat_K3(self):
        """A-hat(K3) = 2 from both shadow tower and geometry."""
        result = verify_ahat_geometric_matching('K3_bosonic')
        assert result['match'] is True
        assert result['A_hat_from_shadow'] == 2
        assert result['A_hat_geometric'] == 2

    def test_ahat_formula(self):
        """A-hat = 24 * F_1 = 24 * kappa/24 = kappa."""
        result = verify_ahat_geometric_matching('K3_bosonic')
        assert result['A_hat_from_shadow'] == result['kappa']

    def test_ahat_torus_shadow_vs_geometric(self):
        """For torus: shadow gives kappa=2 but A-hat_geometric = 0.

        The formula A-hat = 24*F_1 = kappa applies to CY manifolds.
        For the torus (flat, all Pontryagin classes vanish), A-hat_geometric = 0
        but kappa = d (number of free bosons). The mismatch is expected:
        the shadow tower captures the algebraic (VOA) data, not the geometric
        characteristic classes of the underlying manifold.
        """
        result = verify_ahat_geometric_matching('T4_bosonic')
        # Shadow gives kappa = 2 (from 2 free bosons)
        assert result['A_hat_from_shadow'] == 2
        # Geometric A-hat is 0 for flat torus
        assert result['A_hat_geometric'] == 0
        # They do NOT match for torus (mismatch is the geometric content)
        assert result['match'] is False

    def test_ahat_K3_kappa_relation(self):
        """For CY d-fold: A-hat = kappa = d."""
        result = verify_ahat_geometric_matching('K3_bosonic')
        assert result['kappa'] == 2  # d = 2 for K3


# =====================================================================
# Section 10: CY3 (quintic) elliptic genus
# =====================================================================

class TestCY3EllipticGenus:
    """Test CY3 elliptic genus properties."""

    def test_quintic_euler_characteristic(self):
        """chi(quintic) = -200."""
        q = quintic_cy3_elliptic_genus()
        assert q['chi'] == -200

    def test_quintic_hodge_numbers(self):
        """Quintic: h^{1,1} = 1, h^{2,1} = 101."""
        q = quintic_cy3_elliptic_genus()
        assert q['h11'] == 1
        assert q['h21'] == 101

    def test_quintic_index(self):
        """CY3 elliptic genus has index d/2 = 3/2 (half-integral)."""
        q = quintic_cy3_elliptic_genus()
        assert q['index'] == Fraction(3, 2)

    def test_quintic_weight(self):
        """CY3 elliptic genus has weight 0."""
        q = quintic_cy3_elliptic_genus()
        assert q['weight'] == 0

    def test_quintic_q0_chi_y(self):
        """q^0 terms of quintic elliptic genus: chi_y genus."""
        q = quintic_cy3_elliptic_genus()
        # chi_y = -100*y^{-1/2} - 100*y^{1/2} (half-integer y-powers for CY3)
        assert q['q0_terms'][Fraction(-1, 2)] == -100
        assert q['q0_terms'][Fraction(1, 2)] == -100


# =====================================================================
# Section 11: Mock modular forms
# =====================================================================

class TestMockModular:
    """Test mock modular form H(tau) from K3 moonshine."""

    def test_H_constant_term(self):
        """H(tau) has constant term A_0 = -2."""
        H = mock_modular_H_function()
        assert H['coefficients'][0] == -2

    def test_H_weight(self):
        """H(tau) is weight 1/2."""
        H = mock_modular_H_function()
        assert H['weight'] == Fraction(1, 2)

    def test_H_is_mock_modular(self):
        """H(tau) is mock modular."""
        H = mock_modular_H_function()
        assert H['is_mock_modular'] is True

    def test_H_shadow(self):
        """Shadow of H is 24 * eta^3."""
        H = mock_modular_H_function()
        assert '24' in H['shadow']
        assert 'eta' in H['shadow']

    def test_H_kappa_relation(self):
        """A_0 = -2 = -kappa(K3)."""
        H = mock_modular_H_function()
        kappa_K3 = sigma_model_kappa('K3_scft')
        assert H['coefficients'][0] == -int(kappa_K3)

    def test_H_first_few_coefficients(self):
        """H = -2 + 90q + 462q^2 + ..."""
        H = mock_modular_H_function()
        A = mathieu_moonshine_multiplicities(5)
        assert H['coefficients'][0] == -2
        for n in range(1, min(5, len(H['coefficients']))):
            assert H['coefficients'][n] == A[n]


# =====================================================================
# Section 12: Multi-path verification
# =====================================================================

class TestMultiPathVerification:
    """Test 3+ independent paths per result."""

    def test_k3_three_paths(self):
        """K3 elliptic genus verified from 3 independent paths."""
        v = verify_k3_elliptic_genus_three_paths()
        assert v['all_paths_agree']

    def test_k3_path1_shadow(self):
        """Path 1: shadow tower gives phi(K3; tau, 0) = 24."""
        v = verify_k3_elliptic_genus_three_paths()
        assert v['path1_shadow']['matches']

    def test_k3_path2_jacobi(self):
        """Path 2: Jacobi form gives phi(K3; tau, 0) = 24 (constant)."""
        v = verify_k3_elliptic_genus_three_paths()
        assert v['path2_jacobi']['constant']

    def test_k3_path3_n4(self):
        """Path 3: N=4 decomposition gives correct M24 multiplicities."""
        v = verify_k3_elliptic_genus_three_paths()
        assert v['path3_n4']['A_n_verified']

    def test_witten_three_paths_K3(self):
        """Witten genus of K3 verified from 3 paths."""
        v = verify_witten_genus_three_paths('K3_scft')
        assert v['all_agree']


# =====================================================================
# Section 13: Full analysis
# =====================================================================

class TestFullAnalysis:
    """Test comprehensive shadow-genus analysis."""

    def test_full_analysis_K3(self):
        """Full analysis runs without error for K3."""
        result = full_shadow_genus_analysis('K3_bosonic')
        assert result['kappa'] == 2
        assert result['witten_verification']['all_agree']
        assert result['ahat_matching']['match']

    def test_full_analysis_T4(self):
        """Full analysis runs without error for T^4."""
        result = full_shadow_genus_analysis('T4_bosonic')
        assert result['kappa'] == 2

    def test_run_all_verifications(self):
        """All 15 verification checks pass."""
        results = run_all_verifications()
        for key, val in results.items():
            assert val, f"Verification {key} failed"


# =====================================================================
# Section 14: Discriminant table consistency
# =====================================================================

class TestDiscriminantTable:
    """Test internal consistency of phi_{0,1} discriminant table."""

    def test_constraint_n1(self):
        """n=1: c(4) + 2*c(3) + 2*c(0) = 0."""
        from compute.lib.elliptic_genus_shadow_engine import _phi01_discriminant_table
        t = _phi01_discriminant_table()
        assert t[4] + 2 * t[3] + 2 * t[0] == 0

    def test_constraint_n2(self):
        """n=2: c(8) + 2*c(7) + 2*c(4) + 2*c(-1) = 0."""
        from compute.lib.elliptic_genus_shadow_engine import _phi01_discriminant_table
        t = _phi01_discriminant_table()
        assert t[8] + 2 * t[7] + 2 * t[4] + 2 * t[-1] == 0

    def test_constraint_n3(self):
        """n=3: c(12) + 2*c(11) + 2*c(8) + 2*c(3) = 0."""
        from compute.lib.elliptic_genus_shadow_engine import _phi01_discriminant_table
        t = _phi01_discriminant_table()
        assert t[12] + 2 * t[11] + 2 * t[8] + 2 * t[3] == 0

    def test_constraint_n4(self):
        """n=4: c(16) + 2*c(15) + 2*c(12) + 2*c(7) + 2*c(0) = 0."""
        from compute.lib.elliptic_genus_shadow_engine import _phi01_discriminant_table
        t = _phi01_discriminant_table()
        assert t[16] + 2 * t[15] + 2 * t[12] + 2 * t[7] + 2 * t[0] == 0

    def test_constraint_n5(self):
        """n=5: c(20) + 2*c(19) + 2*c(16) + 2*c(11) + 2*c(4) = 0."""
        from compute.lib.elliptic_genus_shadow_engine import _phi01_discriminant_table
        t = _phi01_discriminant_table()
        assert t[20] + 2 * t[19] + 2 * t[16] + 2 * t[11] + 2 * t[4] == 0

    def test_constraint_n6(self):
        """n=6: c(24) + 2*c(23) + 2*c(20) + 2*c(15) + 2*c(8) + 2*c(-1) = 0."""
        from compute.lib.elliptic_genus_shadow_engine import _phi01_discriminant_table
        t = _phi01_discriminant_table()
        assert t[24] + 2 * t[23] + 2 * t[20] + 2 * t[15] + 2 * t[8] + 2 * t[-1] == 0

    def test_constraint_n7(self):
        """n=7: c(28) + 2*c(27) + 2*c(24) + 2*c(19) + 2*c(12) + 2*c(3) = 0."""
        from compute.lib.elliptic_genus_shadow_engine import _phi01_discriminant_table
        t = _phi01_discriminant_table()
        assert t[28] + 2 * t[27] + 2 * t[24] + 2 * t[19] + 2 * t[12] + 2 * t[3] == 0


# =====================================================================
# Section 15: Cross-checks and edge cases
# =====================================================================

class TestCrossChecks:
    """Cross-checks between different parts of the engine."""

    def test_kappa_from_F1(self):
        """kappa = 24 * F_1 for all manifolds."""
        for m in ['K3_bosonic', 'T2_bosonic', 'CY3_bosonic']:
            kappa = sigma_model_kappa(m)
            Fg = sigma_model_free_energy(m, gmax=1)
            assert kappa == 24 * Fg[1]

    def test_euler_char_from_phi(self):
        """chi(K3) = phi(K3; tau, 0) = 24."""
        k3 = k3_elliptic_genus(nmax=3)
        chi = sum(k3.get_coeff(0, l) for l in range(-10, 11))
        assert chi == 24

    def test_jacobi_form_class(self):
        """JacobiForm class operations work correctly."""
        jf = JacobiForm(weight=0, index=Fraction(1), nmax=5)
        jf.set_coeff(0, 0, 10)
        jf.set_coeff(0, 1, 1)
        assert jf.get_coeff(0, 0) == 10
        assert jf.get_coeff(0, 1) == 1
        assert jf.get_coeff(0, 2) == 0  # default

    def test_chi_y_genus(self):
        """chi_y genus is the y-expansion at fixed q-order."""
        jf = phi_01(nmax=3)
        chi_y = jf.chi_y_genus(nmax=3)
        # At n=0: should have l=-1:1, l=0:10, l=1:1
        assert chi_y[0][0] == 10
        assert chi_y[0][1] == 1
        assert chi_y[0][-1] == 1

    def test_mock_modular_first_coefficients_match_moonshine(self):
        """Mock modular H coefficients match Mathieu moonshine A_n."""
        H = mock_modular_H_function(nmax=10)
        A = mathieu_moonshine_multiplicities(10)
        for n in range(1, min(10, len(H['coefficients']))):
            assert H['coefficients'][n] == A[n]

    def test_shadow_tower_terminates_for_class_G(self):
        """Class G (Gaussian) shadow tower: S_r = 0 for r >= 3."""
        for m in ['K3_bosonic', 'T4_bosonic', 'T2_bosonic', 'CY3_bosonic']:
            tower = sigma_model_shadow_tower(m, rmax=10)
            for r in range(3, 11):
                assert tower[r] == 0, f"{m}: S_{r} = {tower[r]} should be 0"

    def test_phi01_sum_constraint_extended(self):
        """phi_{0,1}(tau, 0) = 12 verified to q^11."""
        jf = phi_01(nmax=12)
        y0 = jf.evaluate_y0(nmax=12)
        assert y0[0] == 12
        for n in range(1, 12):
            assert y0[n] == 0, f"q^{n} coefficient = {y0[n]}, should be 0"

    def test_k3_q1_sum(self):
        """Sum of K3 c(1, l) over l is 0 (from phi(tau, 0) = 24 constant)."""
        k3 = k3_elliptic_genus(nmax=3)
        total = sum(k3.get_coeff(1, l) for l in range(-10, 11))
        assert total == 0

    def test_discriminant_table_c0_c_neg1(self):
        """c(0) = 10 and c(-1) = 1 are correct base values."""
        from compute.lib.elliptic_genus_shadow_engine import _phi01_discriminant_table
        t = _phi01_discriminant_table()
        assert t[-1] == 1
        assert t[0] == 10
        assert t[-1] + t[-1] + t[0] == 12  # n=0 constraint
