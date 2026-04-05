r"""Tests for elliptic_genus_deep_engine.py — Witten genus from bar-cobar duality.

MULTI-PATH VERIFICATION STRATEGY:
  Path 1: Shadow tower extraction (kappa, F_g, A-hat GF)
  Path 2: Direct Jacobi form computation (phi_{0,1}, discriminant)
  Path 3: Character/trace formula (N=4 decomposition, Mathieu moonshine)
  Path 4: Chern number formula (chi_y genus, Hodge diamond)
  Path 5: Modularity/elliptic transformation (Jacobi form axioms)
  Path 6: K3 moonshine coefficient matching (M24 representations)

Total: 100+ tests across 13 test classes.

References:
  Eichler-Zagier (1985), Witten (1988), EOT (2010), Gritsenko (1999)
"""

import math
import pytest
from fractions import Fraction

from compute.lib.elliptic_genus_deep_engine import (
    # Arithmetic
    sigma_k,
    bernoulli_number,
    lambda_g_fp,
    # Modular forms
    eta_coeffs,
    eta_power_coeffs,
    e2_coeffs,
    e4_coeffs,
    e6_coeffs,
    j_invariant_coeffs,
    # N=2 SCA
    N2SuperconformalData,
    n2_sca_data,
    n2_sca_for_cy,
    n2_bar_complex_dimensions,
    n2_ope_structure_constants,
    n2_r_matrix_poles,
    # Jacobi forms
    JacobiFormDeep,
    phi_01_deep,
    phi_m21_coeffs,
    # K3
    k3_elliptic_genus,
    k3_chi_y_genus,
    k3_chern_numbers,
    k3_hodge_diamond,
    witten_genus_k3,
    # Shadow decomposition
    shadow_arity_decomposition,
    shadow_free_energy,
    shadow_ahat_generating_function,
    verify_ahat_coefficients,
    # Elliptic/modular transformations
    verify_modularity_constraint,
    verify_elliptic_transformation,
    # Mathieu moonshine
    MATHIEU_M24_IRREP_DIMS,
    M24_ORDER,
    MOONSHINE_A_N,
    mathieu_moonshine_A,
    mathieu_m24_decomposition_exists,
    mathieu_known_decompositions,
    mathieu_verify_from_phi01,
    mathieu_mock_modular_H,
    # GV
    cy3_chi_y_genus,
    quintic_cy3_data,
    resolved_conifold_gv_invariants,
    gv_free_energy,
    verify_gv_integrality,
    # Chern numbers
    chern_number_elliptic_genus,
    # Multi-path
    verify_k3_elliptic_genus_6_paths,
    verify_witten_genus_3_paths,
    # N=2 shadow
    n2_shadow_kappa,
    sigma_model_kappa,
    n2_shadow_depth,
    n2_shadow_radius,
    target_shadow_free_energy,
    # Full analysis
    full_analysis,
    run_all_deep_verifications,
)


# =====================================================================
# Class 1: Arithmetic primitives
# =====================================================================

class TestArithmeticPrimitives:
    """Test sigma_k, Bernoulli, lambda_g^FP."""

    def test_sigma1_of_6(self):
        """sigma_1(6) = 1+2+3+6 = 12."""
        assert sigma_k(6, 1) == 12

    def test_sigma3_of_2(self):
        """sigma_3(2) = 1+8 = 9."""
        assert sigma_k(2, 3) == 9

    def test_sigma_zero_input(self):
        assert sigma_k(0, 1) == 0
        assert sigma_k(-1, 1) == 0

    def test_sigma1_primes(self):
        """sigma_1(p) = 1+p for prime p."""
        for p in [2, 3, 5, 7, 11, 13]:
            assert sigma_k(p, 1) == 1 + p

    def test_bernoulli_basic(self):
        assert bernoulli_number(0) == Fraction(1)
        assert bernoulli_number(1) == Fraction(-1, 2)
        assert bernoulli_number(2) == Fraction(1, 6)
        assert bernoulli_number(4) == Fraction(-1, 30)
        assert bernoulli_number(6) == Fraction(1, 42)
        assert bernoulli_number(8) == Fraction(-1, 30)

    def test_bernoulli_odd_vanish(self):
        for n in [3, 5, 7, 9, 11, 13]:
            assert bernoulli_number(n) == 0

    def test_lambda_g_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_g_fp(1) == Fraction(1, 24)

    def test_lambda_g_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_g_fp(2) == Fraction(7, 5760)

    def test_lambda_g_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_g_fp(3) == Fraction(31, 967680)

    def test_lambda_g_fp_genus0(self):
        """lambda_0^FP = 0."""
        assert lambda_g_fp(0) == Fraction(0)

    def test_lambda_g_fp_positive(self):
        """lambda_g^FP > 0 for g >= 1 (from positive Bernoulli in A-hat)."""
        for g in range(1, 8):
            assert lambda_g_fp(g) > 0


# =====================================================================
# Class 2: Modular forms
# =====================================================================

class TestModularForms:
    """Test q-expansions of modular forms."""

    def test_eta_pentagonal(self):
        """eta = q^{1/24}(1 - q - q^2 + q^5 + q^7 - q^12 - ...)."""
        c = eta_coeffs(15)
        assert c[0] == 1
        assert c[1] == -1
        assert c[2] == -1
        assert c[3] == 0
        assert c[4] == 0
        assert c[5] == 1
        assert c[7] == 1

    def test_e4_leading(self):
        c = e4_coeffs(5)
        assert c[0] == 1
        assert c[1] == 240
        assert c[2] == 2160

    def test_e6_leading(self):
        c = e6_coeffs(5)
        assert c[0] == 1
        assert c[1] == -504
        assert c[2] == -16632

    def test_e2_leading(self):
        """E_2 is quasi-modular (AP15). E_2 = 1 - 24q - 72q^2 - ..."""
        c = e2_coeffs(5)
        assert c[0] == 1
        assert c[1] == -24
        assert c[2] == -72
        assert c[3] == -96

    def test_eta_power_positive(self):
        """eta^3 = q^{1/8}(1 - 3q + 5q^3 - 7q^6 + ...)."""
        c = eta_power_coeffs(10, 3)
        assert c[0] == 1
        assert c[1] == -3

    def test_eta_power_negative(self):
        """eta^{-1} = partition numbers."""
        c = eta_power_coeffs(10, -1)
        assert c[0] == 1
        assert c[1] == 1
        assert c[2] == 2
        assert c[3] == 3
        assert c[4] == 5

    def test_eta_power_zero(self):
        c = eta_power_coeffs(5, 0)
        assert c[0] == 1
        assert all(c[i] == 0 for i in range(1, 5))

    def test_j_invariant_leading(self):
        """j = q^{-1} + 744 + 196884q + ..."""
        c = j_invariant_coeffs(5)
        assert c[0] == 1       # q^{-1}
        assert c[1] == 744     # constant
        assert c[2] == 196884  # q^1

    def test_delta_discriminant(self):
        """Delta = eta^{24} = q - 24q^2 + 252q^3 - ..."""
        c = eta_power_coeffs(10, 24)
        assert c[0] == 1
        assert c[1] == -24
        assert c[2] == 252

    def test_e4_cubed_vs_j_eta24(self):
        r"""Verify E_4^3 = j * Delta where Delta = eta^{24}.

        j(tau) = q^{-1} + 744 + 196884q + ...
        Delta = q - 24q^2 + 252q^3 - ...
        E_4^3 = j * Delta.

        j[k] = coefficient of q^{k-1} (so j[0]=1 for q^{-1}).
        eta24[n] = coefficient of q^n in prod(1-q^n)^24
          (the actual Delta = q * sum eta24[n] q^n).

        (j * Delta) at q^m = sum_k j[k] * Delta_{m-k+1}
          = sum_k j[k] * eta24[m-k]  (since Delta_n = eta24[n-1]).
        """
        nmax = 8
        e4 = e4_coeffs(nmax)
        e4_cubed = _convolve_helper(e4, e4, e4, nmax)
        eta24 = eta_power_coeffs(nmax + 2, 24)
        j = j_invariant_coeffs(nmax + 2)

        for m in range(min(5, nmax)):
            # (j * Delta) at q^m = sum_k j[k] * eta24[m - k]
            # where j[k] is coeff of q^{k-1}, Delta_n = eta24[n-1]
            # j * Delta at q^m: j contributes q^{k-1}, Delta q^{n+1}
            # k-1 + n+1 = m => n = m-k => need eta24[m-k]
            s = 0
            for k in range(m + 2):
                idx = m - k
                if 0 <= k < len(j) and 0 <= idx < len(eta24):
                    s += j[k] * eta24[idx]
            assert s == e4_cubed[m], f"Mismatch at q^{m}: {s} vs {e4_cubed[m]}"


def _convolve_helper(a, b, c, nmax):
    """Helper: three-way convolution."""
    from compute.lib.elliptic_genus_deep_engine import _convolve
    return _convolve(_convolve(a, b, nmax), c, nmax)


# =====================================================================
# Class 3: N=2 Superconformal Algebra
# =====================================================================

class TestN2SCA:
    """Test N=2 SCA data and bar complex structure."""

    def test_n2_cy2_central_charge(self):
        """N=2 SCA for CY 2-fold (K3): c = 6."""
        n2 = n2_sca_for_cy(2)
        assert n2.c == 6
        assert n2.d == 2

    def test_n2_cy3_central_charge(self):
        """N=2 SCA for CY 3-fold: c = 9."""
        n2 = n2_sca_for_cy(3)
        assert n2.c == 9

    def test_n2_kappa_worldsheet(self):
        """kappa_worldsheet = c/2 for N=2 SCA."""
        for d in [2, 3, 4]:
            n2 = n2_sca_for_cy(d)
            assert n2.kappa == Fraction(3 * d, 2)

    def test_n2_generators(self):
        """N=2 SCA has 4 generators: T, J, G+, G-."""
        n2 = n2_sca_for_cy(2)
        assert len(n2.generators) == 4
        assert 'T' in n2.generators
        assert 'J' in n2.generators
        assert 'G+' in n2.generators
        assert 'G-' in n2.generators

    def test_n2_generator_weights(self):
        """T: weight 2, J: weight 1, G^pm: weight 3/2."""
        n2 = n2_sca_for_cy(2)
        assert n2.generators['T']['weight'] == 2
        assert n2.generators['J']['weight'] == 1
        assert n2.generators['G+']['weight'] == Fraction(3, 2)
        assert n2.generators['G-']['weight'] == Fraction(3, 2)

    def test_n2_generator_parities(self):
        """T, J are bosonic (parity 0); G^pm are fermionic (parity 1)."""
        n2 = n2_sca_for_cy(2)
        assert n2.generators['T']['parity'] == 0
        assert n2.generators['J']['parity'] == 0
        assert n2.generators['G+']['parity'] == 1
        assert n2.generators['G-']['parity'] == 1

    def test_n2_ope_TT(self):
        """T(z)T(w) has leading coefficient c/2."""
        ope = n2_ope_structure_constants(Fraction(6))
        assert ope['c_TT_4'] == 3  # c/2 = 6/2 = 3

    def test_n2_ope_JJ(self):
        """J(z)J(w) ~ (c/3)/(z-w)^2."""
        ope = n2_ope_structure_constants(Fraction(6))
        assert ope['c_JJ_2'] == 2  # c/3 = 6/3 = 2

    def test_n2_ope_GG(self):
        """G^+(z)G^-(w) ~ (2c/3)/(z-w)^3."""
        ope = n2_ope_structure_constants(Fraction(6))
        assert ope['c_GG_3'] == 4  # 2c/3 = 12/3 = 4

    def test_n2_r_matrix_pole_orders(self):
        """AP19: bar r-matrix pole = OPE pole - 1."""
        poles = n2_r_matrix_poles(Fraction(6))
        assert poles['TT']['rmatrix_max_pole'] == poles['TT']['ope_max_pole'] - 1
        assert poles['JJ']['rmatrix_max_pole'] == poles['JJ']['ope_max_pole'] - 1
        assert poles['G+G-']['rmatrix_max_pole'] == poles['G+G-']['ope_max_pole'] - 1

    def test_n2_bar_complex_dimensions_low(self):
        """Bar complex of N=2 at low weights."""
        dims = n2_bar_complex_dimensions(Fraction(6), weight_max=3)
        # Weight 1 (J): bar deg 1 has 1 element
        assert dims[2]['bar_deg_1'] == 1  # 2*weight = 2 for J


# =====================================================================
# Class 4: Jacobi form phi_{0,1}
# =====================================================================

class TestPhi01Deep:
    """Test the fundamental weak Jacobi form phi_{0,1}."""

    def test_phi01_z0_constant_12(self):
        """phi_{0,1}(tau, 0) = 12 (constant, independent of tau)."""
        jf = phi_01_deep(nmax=10)
        y0 = jf.evaluate_y0(10)
        assert y0[0] == 12
        for n in range(1, 10):
            assert y0[n] == 0, f"q^{n} coefficient is {y0[n]}, should be 0"

    def test_phi01_q0_terms(self):
        """At q^0: c(0,0)=10, c(0,+/-1)=1, c(0,+/-2)=0."""
        jf = phi_01_deep(nmax=5)
        assert jf.get(0, 0) == 10
        assert jf.get(0, 1) == 1
        assert jf.get(0, -1) == 1
        assert jf.get(0, 2) == 0

    def test_phi01_q1_terms(self):
        """At q^1: c(1,0)=108, c(1,+/-1)=-64, c(1,+/-2)=10."""
        jf = phi_01_deep(nmax=5)
        assert jf.get(1, 0) == 108
        assert jf.get(1, 1) == -64
        assert jf.get(1, -1) == -64
        assert jf.get(1, 2) == 10
        assert jf.get(1, -2) == 10

    def test_phi01_q2_terms(self):
        """At q^2: c(2,0)=808, c(2,+/-1)=-513, c(2,+/-2)=108, c(2,+/-3)=1."""
        jf = phi_01_deep(nmax=5)
        assert jf.get(2, 0) == 808
        assert jf.get(2, 1) == -513
        assert jf.get(2, 2) == 108
        assert jf.get(2, 3) == 1

    def test_phi01_discriminant_dependence(self):
        """c(n,l) depends only on D = 4n - l^2."""
        jf = phi_01_deep(nmax=8)
        assert jf.verify_discriminant_dependence(8)

    def test_phi01_parity_symmetry(self):
        """c(n, l) = c(n, -l) for weight-0 Jacobi form."""
        jf = phi_01_deep(nmax=8)
        assert jf.verify_parity(8)

    def test_phi01_weak_condition(self):
        """No negative-n coefficients (weak Jacobi form)."""
        jf = phi_01_deep(nmax=5)
        assert jf.verify_weak()

    def test_phi01_weight_index(self):
        """Weight 0, index 1."""
        jf = phi_01_deep(nmax=5)
        assert jf.weight == 0
        assert jf.index == Fraction(1)

    def test_phi01_n1_z0_constraint(self):
        """Constraint: sum_l c(1,l) = 0 (from phi(tau,0) = constant)."""
        jf = phi_01_deep(nmax=5)
        s = sum(jf.get(1, l) for l in range(-5, 6))
        assert s == 0

    def test_phi01_n2_z0_constraint(self):
        """sum_l c(2,l) = 0."""
        jf = phi_01_deep(nmax=5)
        s = sum(jf.get(2, l) for l in range(-10, 11))
        assert s == 0

    def test_phi01_n3_z0_constraint(self):
        """sum_l c(3,l) = 0."""
        jf = phi_01_deep(nmax=5)
        s = sum(jf.get(3, l) for l in range(-10, 11))
        assert s == 0

    def test_phi01_discriminant_values(self):
        """Specific discriminant values from the table."""
        jf = phi_01_deep(nmax=5)
        # D=-1 at (0,1): c = 1
        assert jf.get(0, 1) == 1
        # D=0 at (0,0): c = 10
        assert jf.get(0, 0) == 10
        # D=3 at (1,1): c = -64
        assert jf.get(1, 1) == -64
        # D=4 at (1,0): c = 108
        assert jf.get(1, 0) == 108
        # D=7 at (2,1): c = -513
        assert jf.get(2, 1) == -513
        # D=8 at (2,0): c = 808
        assert jf.get(2, 0) == 808


# =====================================================================
# Class 5: phi_{-2,1}
# =====================================================================

class TestPhiM21:
    """Test phi_{-2,1} the weight -2 index 1 Jacobi form."""

    def test_phi_m21_z0_vanishes(self):
        """phi_{-2,1}(tau, 0) = 0 identically (theta_1(tau,0) = 0)."""
        jf = phi_m21_coeffs(nmax=5)
        y0 = jf.evaluate_y0(5)
        for n in range(5):
            assert y0[n] == 0, f"phi_{{-2,1}}(tau,0) has nonzero q^{n}: {y0[n]}"

    def test_phi_m21_q0_terms(self):
        """At q^0: c(0,0)=-2, c(0,+/-1)=1."""
        jf = phi_m21_coeffs(nmax=3)
        assert jf.get(0, 0) == -2
        assert jf.get(0, 1) == 1
        assert jf.get(0, -1) == 1

    def test_phi_m21_weight_index(self):
        jf = phi_m21_coeffs(nmax=3)
        assert jf.weight == -2
        assert jf.index == Fraction(1)


# =====================================================================
# Class 6: K3 elliptic genus
# =====================================================================

class TestK3EllipticGenus:
    """Test the elliptic genus of K3."""

    def test_k3_chi(self):
        """phi(K3; tau, 0) = chi(K3) = 24."""
        k3 = k3_elliptic_genus(nmax=8)
        y0 = k3.evaluate_y0(8)
        assert y0[0] == 24

    def test_k3_constant(self):
        """phi(K3; tau, 0) = 24 is constant (q-independent)."""
        k3 = k3_elliptic_genus(nmax=10)
        y0 = k3.evaluate_y0(10)
        for n in range(1, 10):
            assert y0[n] == 0

    def test_k3_is_2_phi01(self):
        """phi(K3) = 2 * phi_{0,1}."""
        base = phi_01_deep(nmax=5)
        k3 = k3_elliptic_genus(nmax=5)
        for (n, l), c in base.coeffs.items():
            assert k3.get(n, l) == 2 * c

    def test_k3_q0_coefficients(self):
        """At q^0: c(0,0)=20, c(0,+/-1)=2."""
        k3 = k3_elliptic_genus(nmax=3)
        assert k3.get(0, 0) == 20
        assert k3.get(0, 1) == 2
        assert k3.get(0, -1) == 2

    def test_k3_chi_y_genus(self):
        """chi_y(K3) = 2y^{-1} + 20 + 2y."""
        chi_y = k3_chi_y_genus()
        assert chi_y[-1] == 2
        assert chi_y[0] == 20
        assert chi_y[1] == 2

    def test_k3_chi_y_at_1(self):
        """chi_y(K3) at y=1 = 24 = chi(K3)."""
        chi_y = k3_chi_y_genus()
        assert sum(chi_y.values()) == 24

    def test_k3_chi_y_at_neg1(self):
        r"""chi_y(K3) at y=-1 in Jacobi form convention.

        The K3 elliptic genus at q^0 is 2y^{-1} + 20 + 2y (Jacobi form).
        At y=-1: -2 + 20 - 2 = 16.

        The STANDARD chi_y genus is y^{d/2} * (EG at q^0) = y * (2y^{-1}+20+2y)
        = 2 + 20y + 2y^2.  At y=-1: 2 - 20 + 2 = -16 = sigma(K3).

        So EG_Jacobi at y=-1 = -sigma(K3) for d=2 (due to y^{-d/2} shift).
        """
        chi_y = k3_chi_y_genus()
        s = sum((-1)**l * v for l, v in chi_y.items())
        assert s == 16  # Jacobi convention: +16, not -16
        # Standard chi_y at y=-1 = sigma = -16 (consistent with Chern numbers)
        cn = k3_chern_numbers()
        assert s == -cn['sigma']  # 16 = -(-16)

    def test_k3_hodge_diamond(self):
        """K3 Hodge numbers: h^{0,0}=1, h^{1,1}=20, h^{2,0}=h^{0,2}=1."""
        hd = k3_hodge_diamond()
        assert hd[(0, 0)] == 1
        assert hd[(1, 1)] == 20
        assert hd[(2, 0)] == 1
        assert hd[(0, 2)] == 1
        assert hd[(1, 0)] == 0
        assert hd[(0, 1)] == 0

    def test_k3_chern_c2(self):
        """c_2(K3) = chi(K3) = 24."""
        cn = k3_chern_numbers()
        assert cn['c2'] == 24

    def test_k3_chern_c1_sq(self):
        """c_1(K3)^2 = 0 (Calabi-Yau)."""
        cn = k3_chern_numbers()
        assert cn['c1_sq'] == 0

    def test_k3_noether(self):
        """Noether: chi(O) = (c_1^2 + c_2)/12 = 24/12 = 2."""
        cn = k3_chern_numbers()
        assert cn['chi_O'] == (cn['c1_sq'] + cn['c2']) // 12

    def test_k3_ahat(self):
        """A-hat(K3) = 2 (from -p_1/24 = 48/24 for a 4-manifold)."""
        cn = k3_chern_numbers()
        assert cn['A_hat'] == 2

    def test_k3_signature(self):
        """sigma(K3) = -16 (b^+ = 3, b^- = 19)."""
        cn = k3_chern_numbers()
        assert cn['sigma'] == -16

    def test_k3_p1(self):
        """p_1(K3) = c_1^2 - 2c_2 = -48."""
        cn = k3_chern_numbers()
        assert cn['p1'] == cn['c1_sq'] - 2 * cn['c2']

    def test_k3_hirzebruch_signature(self):
        """Hirzebruch: sigma = p_1/3."""
        cn = k3_chern_numbers()
        assert cn['sigma'] == cn['p1'] // 3


# =====================================================================
# Class 7: Witten genus
# =====================================================================

class TestWittenGenus:
    """Test Witten genus from multiple paths."""

    def test_witten_k3_value(self):
        """W(K3) = 24 from all three paths."""
        w = witten_genus_k3()
        assert w['path1_shadow']['W_K3'] == 24
        assert w['path2_index']['W_K3'] == 24
        assert w['path3_chern']['W_K3'] == 24
        assert w['all_agree'] is True

    def test_witten_k3_shadow_kappa(self):
        """Shadow path: kappa(K3) = 2."""
        w = witten_genus_k3()
        assert w['path1_shadow']['kappa'] == Fraction(2)

    def test_witten_k3_shadow_F1(self):
        """F_1 = kappa/24 = 2/24 = 1/12."""
        w = witten_genus_k3()
        assert w['path1_shadow']['F_1'] == Fraction(1, 12)

    def test_witten_k3_ahat(self):
        """A-hat(K3) = 2 from shadow: 24*F_1 = 2."""
        w = witten_genus_k3()
        assert w['path1_shadow']['A_hat_genus'] == Fraction(2)

    def test_witten_k3_chern_chi_y(self):
        """Path 3: chi_y at y=1 = 24."""
        w = witten_genus_k3()
        assert w['path3_chern']['chi_y_at_1'] == 24


# =====================================================================
# Class 8: Shadow tower and A-hat generating function
# =====================================================================

class TestShadowTower:
    """Test shadow tower, free energy, A-hat GF."""

    def test_shadow_free_energy_c6_F1(self):
        """F_1(N=2, c=6) = kappa_ws/24 = 3/24 = 1/8 (worldsheet)."""
        fe = shadow_free_energy(Fraction(6), gmax=3)
        assert fe[0] == 0
        assert fe[1] == Fraction(1, 8)

    def test_target_free_energy_K3_F1(self):
        """F_1(target, K3) = 2/24 = 1/12."""
        fe = target_shadow_free_energy(2, gmax=3)
        assert fe[1] == Fraction(1, 12)

    def test_target_free_energy_K3_F2(self):
        """F_2(target, K3) = 2 * 7/5760 = 7/2880."""
        fe = target_shadow_free_energy(2, gmax=3)
        assert fe[2] == Fraction(7, 2880)

    def test_target_free_energy_CY3_F1(self):
        """F_1(target, CY3) = 3/24 = 1/8."""
        fe = target_shadow_free_energy(3, gmax=3)
        assert fe[1] == Fraction(1, 8)

    def test_ahat_coefficients_match(self):
        """Verify A-hat(ix) coefficients match lambda_g^FP for all g <= 5."""
        checks = verify_ahat_coefficients(gmax=5)
        for g, lam, coeff, ok in checks:
            assert ok, f"A-hat mismatch at genus {g}: {lam} vs {coeff}"

    def test_ahat_gf_k3(self):
        """A-hat GF at kappa=2 matches target F_g."""
        gf = shadow_ahat_generating_function(Fraction(2), gmax=3)
        fe = target_shadow_free_energy(2, gmax=3)
        for g in range(4):
            assert gf[g] == fe[g]

    def test_shadow_decomposition_arity0(self):
        """Arity-0 contribution vanishes."""
        sd = shadow_arity_decomposition(Fraction(6), nmax=5)
        assert all(x == 0 for x in sd[0])

    def test_shadow_decomposition_arity2_leading(self):
        """Arity-2 leading term = kappa/12 = 3/12 = 1/4 for c=6."""
        sd = shadow_arity_decomposition(Fraction(6), nmax=5)
        # kappa_ws = 3, arity-2 leading = kappa/12 * E_2[0] = 3/12 * 1 = 1/4
        assert sd[2][0] == Fraction(1, 4)

    def test_shadow_decomposition_arity4_exists(self):
        """Arity-4 contribution is nonzero for c != 0."""
        sd = shadow_arity_decomposition(Fraction(6), nmax=5)
        assert sd[4][0] != 0  # quartic contact contributes

    def test_kappa_worldsheet_vs_target(self):
        """Worldsheet kappa != target kappa in general."""
        kappa_ws = n2_shadow_kappa(Fraction(6))  # = 3
        kappa_tgt = sigma_model_kappa(2)          # = 2
        assert kappa_ws != kappa_tgt
        assert kappa_ws == Fraction(3)
        assert kappa_tgt == Fraction(2)

    def test_sigma_model_kappa_values(self):
        """sigma_model_kappa(d) = d."""
        for d in [1, 2, 3, 4, 5]:
            assert sigma_model_kappa(d) == Fraction(d)


# =====================================================================
# Class 9: Mathieu moonshine
# =====================================================================

class TestMathieuMoonshine:
    """Test Mathieu moonshine multiplicities and M24 decompositions."""

    def test_A1(self):
        """A_1 = 90 = 2*45."""
        assert mathieu_moonshine_A(1) == 90

    def test_A2(self):
        """A_2 = 462 = 2*231."""
        assert mathieu_moonshine_A(2) == 462

    def test_A3(self):
        """A_3 = 1540 = 2*770."""
        assert mathieu_moonshine_A(3) == 1540

    def test_A4(self):
        """A_4 = 4554 = 2*2277."""
        assert mathieu_moonshine_A(4) == 4554

    def test_A5(self):
        """A_5 = 11592 = 2*5796."""
        assert mathieu_moonshine_A(5) == 11592

    def test_first_10(self):
        """Known A_n for n=1..10."""
        expected = [90, 462, 1540, 4554, 11592, 27830, 62100, 132210, 269640, 531894]
        for n in range(1, 11):
            assert mathieu_moonshine_A(n) == expected[n - 1]

    def test_first_20(self):
        """Known A_n for n=1..20."""
        for n in range(1, 21):
            An = mathieu_moonshine_A(n)
            assert An > 0, f"A_{n} should be positive, got {An}"

    def test_all_positive(self):
        """All A_n > 0 (representation dimensions are positive)."""
        for n in range(1, len(MOONSHINE_A_N)):
            assert MOONSHINE_A_N[n] > 0

    def test_m24_order(self):
        """M24 has order 244823040."""
        assert M24_ORDER == 244823040

    def test_m24_irrep_count(self):
        """M24 has 26 irreducible representations."""
        assert len(MATHIEU_M24_IRREP_DIMS) == 26

    def test_m24_sum_squares(self):
        """Sum of squares of irrep dimensions = |M24|."""
        ss = sum(d**2 for d in MATHIEU_M24_IRREP_DIMS)
        assert ss == M24_ORDER

    def test_m24_decomposition_A1(self):
        """A_1 = 90 decomposes into M24 irreps."""
        assert mathieu_m24_decomposition_exists(90)

    def test_m24_decomposition_A2(self):
        assert mathieu_m24_decomposition_exists(462)

    def test_m24_decomposition_first_5(self):
        """All A_n for n=1..5 have M24 decompositions."""
        for n in range(1, 6):
            An = MOONSHINE_A_N[n]
            assert mathieu_m24_decomposition_exists(An), f"A_{n}={An} fails M24 decomp"

    def test_known_decompositions_sums(self):
        """Verify known explicit decompositions sum correctly."""
        decomps = mathieu_known_decompositions()
        for n, parts in decomps.items():
            total = sum(d * m for d, m in parts)
            assert total == MOONSHINE_A_N[n], f"n={n}: {total} vs {MOONSHINE_A_N[n]}"

    def test_moonshine_verification(self):
        """mathieu_verify_from_phi01 returns all True."""
        results = mathieu_verify_from_phi01(nmax=5)
        for n, An, ok in results:
            assert ok, f"Verification failed at n={n}, A_n={An}"

    def test_mock_modular_H_A0(self):
        """Mock modular H: A_0 = -2 = -kappa(K3)."""
        H = mathieu_mock_modular_H()
        assert H['coefficients'][0] == -2

    def test_mock_modular_H_kappa_relation(self):
        """A_0 = -kappa(K3_target) = -2."""
        H = mathieu_mock_modular_H()
        assert H['A0_equals_neg_kappa'] is True
        assert H['kappa_K3'] == Fraction(2)

    def test_mock_modular_weight(self):
        """H(tau) has weight 1/2."""
        H = mathieu_mock_modular_H()
        assert H['weight'] == Fraction(1, 2)


# =====================================================================
# Class 10: CY3 and Gopakumar-Vafa
# =====================================================================

class TestCY3GV:
    """Test CY3 elliptic genus and GV invariants."""

    def test_quintic_chi(self):
        """Quintic: chi = 2(h^{1,1} - h^{2,1}) = 2(1-101) = -200."""
        q = quintic_cy3_data()
        assert q['chi'] == -200

    def test_quintic_hodge(self):
        """Quintic: h^{1,1}=1, h^{2,1}=101."""
        q = quintic_cy3_data()
        assert q['h11'] == 1
        assert q['h21'] == 101

    def test_quintic_phi_z0_vanishes(self):
        """For CY3 (d=3 odd): phi(tau, 0) = 0."""
        q = quintic_cy3_data()
        assert q['phi_at_z0_vanishes'] is True

    def test_cy3_chi_y_genus_symmetry(self):
        """chi_1 = -chi_2 for CY3."""
        data = cy3_chi_y_genus(1, 101)
        assert data['chi_p'][1] == -data['chi_p'][2]

    def test_cy3_chi0_chi3_vanish(self):
        """chi_0 = chi_3 = 0 for CY3."""
        data = cy3_chi_y_genus(1, 101)
        assert data['chi_p'][0] == 0
        assert data['chi_p'][3] == 0

    def test_gv_conifold_n01(self):
        """Resolved conifold: n_0^1 = 1, all others 0."""
        gv = resolved_conifold_gv_invariants(3)
        assert gv[0][1] == 1
        assert gv[0][2] == 0
        assert gv[1][1] == 0

    def test_gv_integrality(self):
        """All GV invariants are integers (BPS interpretation)."""
        gv = resolved_conifold_gv_invariants(5)
        assert verify_gv_integrality(gv)

    def test_gv_free_energy_g0_conifold(self):
        """F_0 of conifold: F_0 = sum q^k/k^3. F_0[1] = 1, F_0[2] = 1/8."""
        gv = resolved_conifold_gv_invariants(5)
        fe = gv_free_energy(gv, gmax=1, dmax=5)
        assert fe[0][1] == Fraction(1)
        assert fe[0][2] == Fraction(1, 8)
        assert fe[0][3] == Fraction(1, 27)


# =====================================================================
# Class 11: Chern numbers and Hodge data
# =====================================================================

class TestChernNumbers:
    """Test Chern number verification for specific manifolds."""

    def test_k3_chern_consistency(self):
        """K3: all Chern number relations hold."""
        cn = chern_number_elliptic_genus('K3')
        assert cn['consistent'] is True
        assert cn['chi_y_at_1'] == 24

    def test_k3_chi_y_at_neg1_is_signature(self):
        """chi_y at y=-1 = sigma(K3) = -16."""
        cn = chern_number_elliptic_genus('K3')
        assert cn['chi_y_at_neg1'] == -16

    def test_k3_chi_omega_p(self):
        """chi(K3, O)=2, chi(K3, Omega^1)=-20, chi(K3, Omega^2)=2."""
        cn = chern_number_elliptic_genus('K3')
        assert cn['chi_Omega_p'][0] == 2
        assert cn['chi_Omega_p'][1] == -20
        assert cn['chi_Omega_p'][2] == 2

    def test_t4_chi_vanishes(self):
        """chi(T^4) = 0."""
        cn = chern_number_elliptic_genus('T4')
        assert cn['chi_y_at_1'] == 0

    def test_cp2_chi(self):
        """chi(CP^2) = 3."""
        cn = chern_number_elliptic_genus('CP2')
        assert cn['chi'] == 3


# =====================================================================
# Class 12: Modularity and elliptic transformations
# =====================================================================

class TestModularityElliptic:
    """Test Jacobi form modular and elliptic properties."""

    def test_modularity_all(self):
        """Full modularity constraint check on phi_{0,1}."""
        mod = verify_modularity_constraint(nmax=5)
        assert mod['all_pass'] is True

    def test_modularity_discriminant(self):
        mod = verify_modularity_constraint(nmax=5)
        assert mod['discriminant_dependence'] is True

    def test_modularity_parity(self):
        mod = verify_modularity_constraint(nmax=5)
        assert mod['parity_symmetry'] is True

    def test_modularity_weak(self):
        mod = verify_modularity_constraint(nmax=5)
        assert mod['weak_condition'] is True

    def test_modularity_constant_z0(self):
        mod = verify_modularity_constraint(nmax=5)
        assert mod['constant_at_z0'] is True

    def test_elliptic_transformation(self):
        """Elliptic transformation checks pass."""
        et = verify_elliptic_transformation(nmax=5)
        assert et['all_pass'] is True


# =====================================================================
# Class 13: Multi-path verification and full analysis
# =====================================================================

class TestMultiPathVerification:
    """Test the comprehensive multi-path verification suite."""

    def test_k3_6_paths(self):
        """All 6 paths agree for K3 elliptic genus."""
        results = verify_k3_elliptic_genus_6_paths(nmax=5)
        assert results['all_6_paths_agree'] is True

    def test_k3_path1_shadow(self):
        results = verify_k3_elliptic_genus_6_paths(nmax=5)
        assert results['path1_shadow']['pass'] is True

    def test_k3_path2_jacobi(self):
        results = verify_k3_elliptic_genus_6_paths(nmax=5)
        assert results['path2_jacobi']['pass'] is True

    def test_k3_path3_moonshine(self):
        results = verify_k3_elliptic_genus_6_paths(nmax=5)
        assert results['path3_moonshine']['pass'] is True

    def test_k3_path4_chern(self):
        results = verify_k3_elliptic_genus_6_paths(nmax=5)
        assert results['path4_chern']['pass'] is True

    def test_k3_path5_modularity(self):
        results = verify_k3_elliptic_genus_6_paths(nmax=5)
        assert results['path5_modularity']['pass'] is True

    def test_k3_path6_ahat(self):
        results = verify_k3_elliptic_genus_6_paths(nmax=5)
        assert results['path6_ahat']['pass'] is True

    def test_witten_3_paths_d2(self):
        """3-path Witten genus verification for CY 2-fold."""
        results = verify_witten_genus_3_paths(2)
        assert results['path1_shadow']['kappa'] == Fraction(2)

    def test_witten_3_paths_d3(self):
        """3-path Witten genus for CY 3-fold."""
        results = verify_witten_genus_3_paths(3)
        assert results['path1_shadow']['kappa'] == Fraction(3)

    def test_full_analysis_d2(self):
        """Full analysis for K3 (d=2) runs without error."""
        result = full_analysis(2, nmax=5)
        assert result['CY_dimension'] == 2
        assert result['central_charge'] == 6  # c = 3d = 3*2 = 6

    def test_full_analysis_d3(self):
        """Full analysis for CY3 (d=3) runs without error."""
        result = full_analysis(3, nmax=5)
        assert result['CY_dimension'] == 3
        assert result['central_charge'] == 9

    def test_run_all_deep_verifications(self):
        """The comprehensive verification suite passes."""
        results = run_all_deep_verifications()
        for key, val in results.items():
            assert val is True, f"Verification failed: {key} = {val}"

    def test_n2_shadow_depth(self):
        """N=2 SCA has shadow depth class M (infinite)."""
        assert n2_shadow_depth(Fraction(6)) == 'M'

    def test_n2_shadow_radius_positive(self):
        """Shadow radius is positive for c > 0."""
        rho = n2_shadow_radius(Fraction(6))
        assert rho > 0

    def test_n2_shadow_radius_zero_at_c0(self):
        """Shadow radius vanishes at c=0."""
        rho = n2_shadow_radius(Fraction(0))
        assert rho == 0


# =====================================================================
# Additional cross-checks
# =====================================================================

class TestCrossChecks:
    """Cross-verification between different computation paths."""

    def test_k3_ahat_from_chern_vs_shadow(self):
        """A-hat(K3) = 2 from both Chern numbers and shadow tower."""
        cn = k3_chern_numbers()
        w = witten_genus_k3()
        assert cn['A_hat'] == w['path1_shadow']['A_hat_genus']

    def test_k3_signature_from_hodge_and_chern(self):
        """sigma(K3) from Hodge: b^+ - b^- = 3 - 19 = -16."""
        hd = k3_hodge_diamond()
        # b^+ = 1 + h^{2,0} + h^{0,2} = 1 + 1 + 1 = 3
        # b^- = h^{1,1} - 1 = 20 - 1 = 19
        # Wait: for a surface, b_2 = h^{2,0} + h^{1,1} + h^{0,2} = 1 + 20 + 1 = 22.
        # b^+ = 2h^{2,0} + 1 = 3 (from the holomorphic 2-form and its conjugate, plus 1).
        # b^- = h^{1,1} - 1 = 19.  Actually: b^+ = 2pg + 1 = 3, b^- = h^{1,1} - 1 = 19.
        # But that gives b_2 = b^+ + b^- = 22. CHECK.
        b_plus = 2 * hd[(2, 0)] + 1  # = 3
        b_minus = hd[(1, 1)] - 1      # = 19
        sigma = b_plus - b_minus       # = -16
        cn = k3_chern_numbers()
        assert sigma == cn['sigma']

    def test_k3_euler_from_hodge(self):
        """chi(K3) from Hodge diamond: sum (-1)^{p+q} h^{p,q} = 24."""
        hd = k3_hodge_diamond()
        chi = sum((-1)**(p + q) * h for (p, q), h in hd.items())
        assert chi == 24

    def test_fp_vs_ahat_explicit(self):
        """lambda_1^FP = 1/24 matches (1/24) coefficient of A-hat(ix)."""
        # A-hat(ix) = 1 + x^2/24 + 7x^4/5760 + ...
        assert lambda_g_fp(1) == Fraction(1, 24)
        assert lambda_g_fp(2) == Fraction(7, 5760)

    def test_k3_chi_from_elliptic_genus(self):
        """chi(K3) = phi(K3; tau, 0) = 24 from the Jacobi form."""
        k3 = k3_elliptic_genus(nmax=3)
        y0 = k3.evaluate_y0(3)
        assert y0[0] == 24

    def test_k3_chi_from_noether(self):
        """chi(O_K3) = 2 via Noether, consistent with A-hat = 2."""
        cn = k3_chern_numbers()
        chi_O = (cn['c1_sq'] + cn['c2']) // 12
        assert chi_O == 2
        assert chi_O == cn['A_hat']

    def test_moonshine_A0_vs_kappa(self):
        """Mock modular A_0 = -2 = -kappa(K3_target)."""
        H = mathieu_mock_modular_H()
        kappa = sigma_model_kappa(2)
        assert H['coefficients'][0] == -int(kappa)

    def test_gv_multicovering_consistency(self):
        """Multi-covering: F_0[k*d] receives contribution from n_0^d."""
        gv = resolved_conifold_gv_invariants(5)
        fe = gv_free_energy(gv, gmax=0, dmax=5)
        # F_0[1] = n_0^1 / 1^3 = 1
        assert fe[0][1] == Fraction(1)
        # F_0[2] = n_0^2/1 + n_0^1/8 = 0 + 1/8 = 1/8
        assert fe[0][2] == Fraction(1, 8)
        # F_0[3] = n_0^3/1 + n_0^1/27 = 0 + 1/27 = 1/27
        assert fe[0][3] == Fraction(1, 27)
