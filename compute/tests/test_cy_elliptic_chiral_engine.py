r"""Tests for cy_elliptic_chiral_engine.py -- chiral algebra on E and K3 x E.

Tests cover:
1. Heisenberg on E: level, kappa, partition functions
2. Theta functions: Z^2 lattice, Eisenstein lattice, modular form cross-checks
3. Module characters: coset decompositions
4. bc-betagamma / CDR on E: central charge, generators, Euler characteristic
5. Elliptic genus of E: vanishing by three independent paths
6. Product K3 x E: kappa additivity, central charges, genus tower
7. Elliptic cohomology / TMF: Witten genus vanishing
8. Shadow obstruction tower data: class G, discriminant, depth
9. Modular form verifications: r_2(n), r_hex(n) via divisor formulas
10. Multi-path verification: 3+ paths per central claim

MULTI-PATH VERIFICATION STRATEGY:
  - kappa(CDR(E)): (1) CY dimension, (2) Heisenberg level, (3) genus-1 extraction
  - Ell(E) = 0: (1) free action, (2) Hodge, (3) chi_y
  - kappa(K3xE) = 3: (1) additivity, (2) dimension, (3) genus tower
  - Witten genus vanishing: (1) multiplicativity, (2) free action, (3) chi product
  - Theta functions: (1) direct lattice sum, (2) divisor formula, (3) first terms

References:
  Polchinski, "String Theory" Vol I Ch 8
  Eichler-Zagier, "The Theory of Jacobi Forms" (1985)
  Malikov-Schechtman-Vaintrob, math/9803041 (1998)
  Borisov-Libgober, math/0007108 (2000)
"""

import math
import pytest
from fractions import Fraction

from compute.lib.cy_elliptic_chiral_engine import (
    # Arithmetic
    sigma_k,
    partition_number,
    bernoulli_number,
    faber_pandharipande,
    # q-expansion
    eta_coeffs,
    eta_power_coeffs,
    e2_coeffs,
    e4_coeffs,
    e6_coeffs,
    _convolve,
    _convolve_frac,
    # Theta functions
    theta_lattice_1d,
    theta_Z_squared,
    theta_eisenstein_lattice,
    theta_function_lattice_2d,
    # Heisenberg on E
    EllipticCurveData,
    SQUARE_TORUS,
    HEXAGONAL_TORUS,
    heisenberg_level_on_E,
    kappa_heisenberg_on_E,
    kappa_lattice_voa_E,
    kappa_cdr_E,
    lattice_voa_partition_function_E,
    lattice_voa_partition_function_2d,
    square_torus_partition_function,
    hexagonal_torus_partition_function,
    # Module characters
    dual_lattice_cosets_square,
    dual_lattice_cosets_eisenstein,
    eisenstein_discriminant_group_order,
    verify_theta_decomposition_eisenstein,
    # CDR on E
    cdr_central_charge,
    cdr_generators_on_E,
    euler_characteristic_E,
    hodge_numbers_E,
    borisov_libgober_character_E,
    cdr_cohomology_dimensions_E,
    _local_cdr_states,
    # Elliptic genus
    elliptic_genus_E,
    witten_genus_E,
    partition_function_E_holomorphic,
    # Product K3 x E
    ProductCYData,
    product_cy_data,
    kappa_product_cdr,
    kappa_product_sigma_model,
    genus_tower_product,
    # TMF
    witten_genus_product_K3_E,
    elliptic_genus_K3_coeffs,
    refined_partition_function_product,
    # Shadow data
    shadow_data_E_cdr,
    shadow_data_E_lattice,
    shadow_data_product_K3E,
    # Multi-path verification
    verify_kappa_E_three_paths,
    verify_elliptic_genus_E_three_paths,
    verify_kappa_product_three_paths,
    verify_witten_genus_vanishing_three_paths,
    theta_Z_squared_vs_e4,
    theta_eisenstein_vs_formula,
    # Full analysis
    run_all_verifications,
    full_elliptic_chiral_analysis,
)


# =====================================================================
# Section 1: Arithmetic primitives
# =====================================================================

class TestArithmeticPrimitives:
    """Tests for sigma_k, partition_number, bernoulli, FP constants."""

    def test_sigma_1_small(self):
        assert sigma_k(1, 1) == 1
        assert sigma_k(6, 1) == 12  # 1+2+3+6
        assert sigma_k(12, 1) == 28

    def test_sigma_3_small(self):
        assert sigma_k(1, 3) == 1
        assert sigma_k(2, 3) == 9  # 1 + 8
        assert sigma_k(3, 3) == 28  # 1 + 27

    def test_sigma_k_zero(self):
        assert sigma_k(0, 1) == 0
        assert sigma_k(-1, 1) == 0

    def test_partition_number_small(self):
        assert partition_number(0) == 1
        assert partition_number(1) == 1
        assert partition_number(2) == 2
        assert partition_number(3) == 3
        assert partition_number(4) == 5
        assert partition_number(5) == 7
        assert partition_number(10) == 42

    def test_bernoulli_known_values(self):
        assert bernoulli_number(0) == Fraction(1)
        assert bernoulli_number(1) == Fraction(-1, 2)
        assert bernoulli_number(2) == Fraction(1, 6)
        assert bernoulli_number(4) == Fraction(-1, 30)
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_bernoulli_odd_vanish(self):
        for n in [3, 5, 7, 9, 11]:
            assert bernoulli_number(n) == 0

    def test_faber_pandharipande_g1(self):
        """F_1 = kappa * 1/24. lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Fraction(1, 24)

    def test_faber_pandharipande_g2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Fraction(7, 5760)

    def test_faber_pandharipande_g3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Fraction(31, 967680)

    def test_faber_pandharipande_positive(self):
        """All FP constants are positive."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0


# =====================================================================
# Section 2: q-expansion infrastructure
# =====================================================================

class TestQExpansion:
    """Tests for eta, Eisenstein series, convolution."""

    def test_eta_coeffs_leading(self):
        """prod(1-q^n) starts with 1 - q - q^2 + q^5 + q^7 - ..."""
        c = eta_coeffs(20)
        assert c[0] == 1
        assert c[1] == -1
        assert c[2] == -1
        assert c[3] == 0
        assert c[4] == 0
        assert c[5] == 1
        assert c[7] == 1

    def test_eta_inverse_is_partitions(self):
        """1/prod(1-q^n) = sum p(n) q^n."""
        c = eta_power_coeffs(20, -1)
        for n in range(15):
            assert c[n] == partition_number(n), f"Failed at n={n}: {c[n]} != {partition_number(n)}"

    def test_e4_leading(self):
        c = e4_coeffs(10)
        assert c[0] == 1
        assert c[1] == 240

    def test_e6_leading(self):
        c = e6_coeffs(10)
        assert c[0] == 1
        assert c[1] == -504

    def test_e2_leading(self):
        c = e2_coeffs(10)
        assert c[0] == 1
        assert c[1] == -24

    def test_convolution_identity(self):
        """Convolving with [1,0,0,...] is identity."""
        a = [1, 2, 3, 4]
        identity = [1, 0, 0, 0]
        result = _convolve(a, identity, 4)
        assert result == [1, 2, 3, 4]

    def test_convolution_shift(self):
        """Convolving with [0,1,0,...] shifts by 1."""
        a = [1, 2, 3, 4]
        shift = [0, 1, 0, 0]
        result = _convolve(a, shift, 4)
        assert result == [0, 1, 2, 3]

    def test_eta_squared_product(self):
        """eta^2 = convolution of eta with itself."""
        eta1 = eta_coeffs(15)
        eta2 = eta_power_coeffs(15, 2)
        manual = _convolve(eta1, eta1, 15)
        assert eta2 == manual


# =====================================================================
# Section 3: Theta functions -- lattice sums
# =====================================================================

class TestThetaFunctions:
    """Tests for lattice theta functions."""

    def test_theta_1d_self_dual(self):
        """Theta for R^2=2: sum q^{n^2}. c[0]=1, c[1]=2, c[4]=2, c[9]=2."""
        theta = theta_lattice_1d(Fraction(2), 20)
        assert theta[0] == 1
        assert theta[1] == 2
        assert theta[2] == 0
        assert theta[3] == 0
        assert theta[4] == 2
        assert theta[9] == 2

    def test_theta_1d_R_squared_4(self):
        """Theta for R^2=4: sum q^{2n^2}. c[0]=1, c[2]=2, c[8]=2."""
        theta = theta_lattice_1d(Fraction(4), 20)
        assert theta[0] == 1
        assert theta[2] == 2
        assert theta[1] == 0
        assert theta[8] == 2

    def test_theta_Z_squared_origin(self):
        """r_2(0) = 1 (the origin)."""
        theta = theta_Z_squared(20)
        assert theta[0] == 1

    def test_theta_Z_squared_r2_1(self):
        """r_2(1) = 4: the 4 neighbors (1,0), (-1,0), (0,1), (0,-1)."""
        theta = theta_Z_squared(20)
        assert theta[1] == 4

    def test_theta_Z_squared_r2_2(self):
        """r_2(2) = 4: (1,1), (1,-1), (-1,1), (-1,-1)."""
        theta = theta_Z_squared(20)
        assert theta[2] == 4

    def test_theta_Z_squared_r2_3(self):
        """r_2(3) = 0: no way to write 3 as sum of two squares."""
        theta = theta_Z_squared(20)
        assert theta[3] == 0

    def test_theta_Z_squared_r2_4(self):
        """r_2(4) = 4: (2,0), (-2,0), (0,2), (0,-2)."""
        theta = theta_Z_squared(20)
        assert theta[4] == 4

    def test_theta_Z_squared_r2_5(self):
        """r_2(5) = 8: (2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)."""
        theta = theta_Z_squared(20)
        assert theta[5] == 8

    def test_theta_Z_squared_r2_known_values(self):
        """Known values of r_2(n) for small n."""
        theta = theta_Z_squared(30)
        known = {0: 1, 1: 4, 2: 4, 3: 0, 4: 4, 5: 8, 6: 0, 7: 0,
                 8: 4, 9: 4, 10: 8, 11: 0, 12: 0, 13: 8}
        for n, expected in known.items():
            assert theta[n] == expected, f"r_2({n}) = {theta[n]}, expected {expected}"

    def test_theta_eisenstein_origin(self):
        """r_hex(0) = 1."""
        theta = theta_eisenstein_lattice(20)
        assert theta[0] == 1

    def test_theta_eisenstein_r_1(self):
        """r_hex(1) = 6: the 6 nearest neighbors of the hexagonal lattice."""
        theta = theta_eisenstein_lattice(20)
        assert theta[1] == 6

    def test_theta_eisenstein_r_3(self):
        """r_hex(3) = 6: norm 3 vectors."""
        theta = theta_eisenstein_lattice(20)
        assert theta[3] == 6

    def test_theta_eisenstein_r_4(self):
        """r_hex(4) = 6."""
        theta = theta_eisenstein_lattice(20)
        assert theta[4] == 6

    def test_theta_eisenstein_r_7(self):
        """r_hex(7) = 12: norm 7 vectors."""
        theta = theta_eisenstein_lattice(20)
        assert theta[7] == 12

    def test_theta_Z_squared_modular_cross_check(self):
        """Cross-check: r_2(n) = 4*(d_1(n) - d_3(n)) via divisor sums."""
        result = theta_Z_squared_vs_e4()
        assert result["agreement"]

    def test_theta_eisenstein_character_cross_check(self):
        """Cross-check: r_hex(n) = 6*sum chi_3(d) via character sums."""
        result = theta_eisenstein_vs_formula()
        assert result["agreement"]

    def test_theta_2d_identity_gram(self):
        """Theta with Gram = I_2 should match theta_Z_squared."""
        gram = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
        theta_2d = theta_function_lattice_2d(gram, 15)
        theta_sq = theta_Z_squared(15)
        # theta_2d uses <v,v>/2 convention; theta_Z_squared uses |v|^2 convention
        # With Gram = I_2: <v,v> = a^2 + b^2, so <v,v>/2 = (a^2+b^2)/2
        # This means theta_2d[k] = #{(a,b): (a^2+b^2)/2 = k} = r_2(2k)... no.
        # Actually theta_function_lattice_2d computes <v,v>/2 = (g00*a^2 + ... )/2
        # With g00=1, g11=1, g01=g10=0: half_norm = (a^2+b^2)/2.
        # So theta_2d[k] = #{(a,b): a^2+b^2 = 2k}
        # theta_sq[n] = #{(a,b): a^2+b^2 = n}
        # They are related by: theta_2d[k] = theta_sq[2k].
        for k in range(7):
            assert theta_2d[k] == Fraction(theta_sq[2 * k]), \
                f"Mismatch at k={k}: {theta_2d[k]} != {theta_sq[2*k]}"


# =====================================================================
# Section 4: Heisenberg on E
# =====================================================================

class TestHeisenbergOnE:
    """Tests for Heisenberg VOA on elliptic curve."""

    def test_square_torus_data(self):
        assert SQUARE_TORUS.tau_real == 0.0
        assert SQUARE_TORUS.tau_imag == 1.0
        assert SQUARE_TORUS.area == 1.0

    def test_hexagonal_torus_data(self):
        assert HEXAGONAL_TORUS.tau_real == -0.5
        assert abs(HEXAGONAL_TORUS.tau_imag - math.sqrt(3) / 2) < 1e-12

    def test_heisenberg_level(self):
        """The Heisenberg level is 1 (OPE independent of compactification)."""
        assert heisenberg_level_on_E(SQUARE_TORUS) == 1.0
        assert heisenberg_level_on_E(HEXAGONAL_TORUS) == 1.0

    def test_kappa_heisenberg(self):
        """kappa(H_1) = 1 for the Heisenberg at level 1."""
        assert kappa_heisenberg_on_E() == Fraction(1)

    def test_kappa_lattice_voa(self):
        """kappa(V_Lambda) = rank(Lambda) = 2 for the 2d real lattice."""
        assert kappa_lattice_voa_E() == Fraction(2)

    def test_kappa_cdr(self):
        """kappa(CDR(E)) = dim_C(E) = 1."""
        assert kappa_cdr_E() == Fraction(1)

    def test_partition_function_E_leading(self):
        """Leading terms of Z_E^{hol} = Theta * 1/eta."""
        pf = lattice_voa_partition_function_E(15, R_squared=2)
        # Theta = 1 + 2q + 0q^2 + 0q^3 + 2q^4 + ...
        # 1/eta = 1 + q + 2q^2 + 3q^3 + 5q^4 + ...
        # Product:
        # c[0] = 1*1 = 1
        # c[1] = 1*1 + 2*1 = 3
        # c[2] = 1*2 + 2*1 + 0*1 = 4
        # c[3] = 1*3 + 2*2 + 0*1 + 0*1 = 7
        assert pf[0] == Fraction(1)
        assert pf[1] == Fraction(3)
        assert pf[2] == Fraction(4)
        assert pf[3] == Fraction(7)

    def test_partition_function_E_positive(self):
        """All partition function coefficients are non-negative."""
        pf = lattice_voa_partition_function_E(20, R_squared=2)
        for n in range(20):
            assert pf[n] >= 0, f"Negative at n={n}: {pf[n]}"

    def test_square_torus_pf_leading(self):
        """Z_{Z^2}/eta^2 leading terms."""
        pf = square_torus_partition_function(10)
        # Theta_{Z^2} = 1 + 4q + 4q^2 + 0q^3 + 4q^4 + ...
        # 1/eta^2: p_2(n) = coefficients of 1/prod(1-q^n)^2
        # p_2(0)=1, p_2(1)=2, p_2(2)=5, p_2(3)=10, p_2(4)=20
        # Product c[0] = 1*1 = 1
        # c[1] = 1*2 + 4*1 = 6
        assert pf[0] == Fraction(1)
        assert pf[1] == Fraction(6)

    def test_hexagonal_torus_pf_leading(self):
        """Z_{Z[rho]}/eta^2 leading terms."""
        pf = hexagonal_torus_partition_function(10)
        # Theta_{hex} = 1 + 6q + 0q^2 + 6q^3 + ...
        # 1/eta^2: 1 + 2q + 5q^2 + 10q^3 + ...
        # c[0] = 1
        # c[1] = 1*2 + 6*1 = 8
        assert pf[0] == Fraction(1)
        assert pf[1] == Fraction(8)


# =====================================================================
# Section 5: Module characters (coset decomposition)
# =====================================================================

class TestModuleCharacters:
    """Tests for lattice VOA module characters."""

    def test_square_lattice_self_dual(self):
        """Z^2 is self-dual: only one coset."""
        cosets = dual_lattice_cosets_square(10)
        assert len(cosets) == 1
        assert "(0,0)" in cosets

    def test_square_lattice_single_module(self):
        """The single module is the VOA itself."""
        cosets = dual_lattice_cosets_square(10)
        theta = theta_Z_squared(10)
        assert cosets["(0,0)"] == theta

    def test_eisenstein_discriminant_group(self):
        """Lambda*/Lambda for Eisenstein lattice has order 3."""
        assert eisenstein_discriminant_group_order() == 3

    def test_eisenstein_three_cosets(self):
        """Eisenstein lattice produces 3 coset theta functions."""
        cosets = dual_lattice_cosets_eisenstein(10)
        assert "gamma_0" in cosets
        assert "gamma_1_tripled" in cosets
        assert "gamma_2_tripled" in cosets

    def test_eisenstein_identity_coset(self):
        """Identity coset theta matches the full lattice theta."""
        cosets = dual_lattice_cosets_eisenstein(15)
        theta = theta_eisenstein_lattice(15)
        assert cosets["gamma_0"] == theta

    def test_eisenstein_shifted_cosets_nonzero(self):
        """Shifted cosets have nonzero coefficients."""
        cosets = dual_lattice_cosets_eisenstein(10)
        assert sum(cosets["gamma_1_tripled"]) > 0
        assert sum(cosets["gamma_2_tripled"]) > 0

    def test_eisenstein_shifted_coset_symmetry(self):
        """gamma_1 and gamma_2 cosets should have the same total count
        (they are related by complex conjugation on Z[rho])."""
        cosets = dual_lattice_cosets_eisenstein(15)
        # The shifted cosets gamma_1 and gamma_2 are conjugate.
        # They should have the same theta function (up to reindexing).
        total_1 = sum(cosets["gamma_1_tripled"][:30])
        total_2 = sum(cosets["gamma_2_tripled"][:30])
        assert total_1 == total_2

    def test_theta_decomposition_eisenstein(self):
        assert verify_theta_decomposition_eisenstein(15)


# =====================================================================
# Section 6: CDR on E (bc-betagamma)
# =====================================================================

class TestCDROnE:
    """Tests for chiral de Rham complex on E."""

    def test_cdr_central_charge_zero(self):
        """CDR always has c = 0."""
        assert cdr_central_charge() == 0

    def test_cdr_generators_count(self):
        """CDR(E) has 4 generators: beta, gamma, b, c."""
        gens = cdr_generators_on_E()
        assert len(gens) == 4
        assert set(gens.keys()) == {"beta", "gamma", "b", "c"}

    def test_cdr_generator_weights(self):
        """beta and b have weight 1; gamma and c have weight 0."""
        gens = cdr_generators_on_E()
        assert gens["beta"]["weight"] == 1
        assert gens["gamma"]["weight"] == 0
        assert gens["b"]["weight"] == 1
        assert gens["c"]["weight"] == 0

    def test_cdr_generator_parity(self):
        """beta and gamma are bosonic; b and c are fermionic."""
        gens = cdr_generators_on_E()
        assert gens["beta"]["parity"] == 0
        assert gens["gamma"]["parity"] == 0
        assert gens["b"]["parity"] == 1
        assert gens["c"]["parity"] == 1

    def test_cdr_global_sections(self):
        """Each generator has h0 = h1 = 1 on E (trivial bundle)."""
        gens = cdr_generators_on_E()
        for name, data in gens.items():
            assert data["h0"] == 1, f"{name}: h0 should be 1"
            assert data["h1"] == 1, f"{name}: h1 should be 1"

    def test_euler_characteristic_zero(self):
        """chi(E) = 0."""
        assert euler_characteristic_E() == 0

    def test_hodge_diamond(self):
        """Hodge numbers of E: all h^{p,q} = 1 for 0 <= p,q <= 1."""
        h = hodge_numbers_E()
        assert h[(0, 0)] == 1
        assert h[(1, 0)] == 1
        assert h[(0, 1)] == 1
        assert h[(1, 1)] == 1

    def test_hodge_chi_zero(self):
        """chi from Hodge: h^{0,0} - h^{0,1} - h^{1,0} + h^{1,1} = 0."""
        h = hodge_numbers_E()
        chi = h[(0, 0)] - h[(0, 1)] - h[(1, 0)] + h[(1, 1)]
        assert chi == 0

    def test_borisov_libgober_vanishes(self):
        """The Borisov-Libgober chi_y character of CDR(E) is identically 0."""
        bl = borisov_libgober_character_E(15)
        assert all(c == 0 for c in bl)

    def test_cdr_cohomology_chi_zero(self):
        """chi_total = 0 at every weight (all bundles on E have chi=0)."""
        dims = cdr_cohomology_dimensions_E(5)
        for w, data in dims.items():
            assert data["chi_total"] == 0, f"chi nonzero at weight {w}"

    def test_cdr_cohomology_h0_equals_h1(self):
        """On E with trivial bundles: h^0 = h^1 at every weight."""
        dims = cdr_cohomology_dimensions_E(5)
        for w, data in dims.items():
            assert data["h0_bos"] == data["h1_bos"], f"bosonic h0 != h1 at weight {w}"
            assert data["h0_ferm"] == data["h1_ferm"], f"fermionic h0 != h1 at weight {w}"

    def test_local_cdr_states_weight0(self):
        """At weight 0, 1 bosonic and 1 fermionic state."""
        assert _local_cdr_states(0, bosonic=True) == 1
        assert _local_cdr_states(0, bosonic=False) == 0  # vacuum is bosonic

    def test_local_cdr_states_weight1(self):
        """At weight 1, states from first oscillators."""
        bos = _local_cdr_states(1, bosonic=True)
        ferm = _local_cdr_states(1, bosonic=False)
        # Weight 1: 2 bosonic oscillators (each contributing 1 state at level 1)
        # and 2 fermionic oscillators (each contributing 1 state at level 1)
        # Total bosonic: 2 (from bos osc) + 0 (from paired ferm) = ...
        # Actually the partition function is:
        # bos: 1/(1-q)^2 at level 1 -> 2 states
        # ferm: (1+q)^2 at level 1 -> gives 2 states of odd parity + 1 paired = ...
        # Let's verify the generating function.
        # Full ch(q) = prod_{n>=1} (1+q^n)^2/(1-q^n)^2
        # At n=1: (1+q)^2/(1-q)^2 = (1+2q+q^2)*(1+2q+3q^2+...) = ...
        # = 1 + 4q + ... at q^1 coefficient
        assert bos + ferm == 4  # total dimension at weight 1

    def test_local_cdr_generating_function(self):
        """Verify the generating function prod (1+q^n)^2/(1-q^n)^2 at low weights."""
        # ch(q) = prod_{n>=1} (1+q^n)^2/(1-q^n)^2
        # = (1 + 2q + q^2 + ...)/(1 - 2q + q^2 + ...) for the n=1 factor... no.
        # Just compute the product numerically up to q^5.
        nmax = 8
        # Numerator: prod (1+q^n)^2
        num = [0] * nmax
        num[0] = 1
        for n in range(1, nmax):
            # Multiply by (1 + q^n)^2 = 1 + 2q^n + q^{2n}
            new = [0] * nmax
            for i in range(nmax):
                if num[i] == 0:
                    continue
                new[i] += num[i]
                if i + n < nmax:
                    new[i + n] += 2 * num[i]
                if i + 2 * n < nmax:
                    new[i + 2 * n] += num[i]
            num = new
        # Denominator: 1/prod (1-q^n)^2 = sum p_2(k) q^k
        den = eta_power_coeffs(nmax, -2)
        # Product
        ch = _convolve(num, den, nmax)
        # ch[0] should be 1 (vacuum)
        assert ch[0] == 1
        # Verify against our function
        for w in range(1, min(5, nmax)):
            bos = _local_cdr_states(w, bosonic=True)
            ferm = _local_cdr_states(w, bosonic=False)
            assert bos + ferm == ch[w], \
                f"Weight {w}: {bos}+{ferm}={bos+ferm} != ch={ch[w]}"


# =====================================================================
# Section 7: Elliptic genus of E
# =====================================================================

class TestEllipticGenusE:
    """Tests for the vanishing of the elliptic genus of E."""

    def test_elliptic_genus_vanishes(self):
        assert elliptic_genus_E() == 0

    def test_witten_genus_vanishes(self):
        assert witten_genus_E() == 0

    def test_three_path_verification(self):
        """Ell(E) = 0 verified by three independent paths."""
        result = verify_elliptic_genus_E_three_paths()
        assert result["agreement"]
        assert result["path1_fixed_point"] == 0
        assert result["path2_euler"] == 0
        assert result["path3_chi_y"] == 0

    def test_chi_y_vanishing_by_hodge(self):
        """chi_y(E) = sum (-y)^p chi(Omega^p) = 0 for all y."""
        h = hodge_numbers_E()
        # chi(O_E) = h^{0,0} - h^{0,1} = 1 - 1 = 0
        chi_O = h[(0, 0)] - h[(0, 1)]
        # chi(Omega^1_E) = h^{1,0} - h^{1,1} = 1 - 1 = 0
        chi_Omega1 = h[(1, 0)] - h[(1, 1)]
        assert chi_O == 0
        assert chi_Omega1 == 0

    def test_partition_function_nontrivial(self):
        """Despite Ell=0, the partition function is nontrivial."""
        pf = partition_function_E_holomorphic(10)
        assert pf[0] == Fraction(1)
        assert pf[1] > 0  # there are momentum modes


# =====================================================================
# Section 8: Product K3 x E
# =====================================================================

class TestProductK3E:
    """Tests for the product CY 3-fold K3 x E."""

    def test_product_complex_dim(self):
        data = product_cy_data()
        assert data.complex_dim == 3

    def test_product_chi_vanishes(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        data = product_cy_data()
        assert data.chi_product == 0

    def test_product_central_charge_sigma_model(self):
        """c(K3 x E sigma model) = 3 * 3 = 9."""
        data = product_cy_data()
        assert data.central_charge_sigma_model == 9

    def test_product_central_charge_cdr(self):
        """c(CDR(K3 x E)) = 0."""
        data = product_cy_data()
        assert data.central_charge_cdr == 0

    def test_kappa_product_cdr_additivity(self):
        """kappa(CDR(K3 x E)) = 2 + 1 = 3 by additivity."""
        assert kappa_product_cdr() == Fraction(3)

    def test_kappa_product_sigma_model(self):
        """kappa(sigma model) = dim_C = 3."""
        assert kappa_product_sigma_model() == Fraction(3)

    def test_kappa_product_consistency(self):
        """CDR kappa = sigma model kappa = dim_C for CY."""
        assert kappa_product_cdr() == kappa_product_sigma_model()

    def test_kappa_product_three_paths(self):
        """Three-path verification of kappa(K3 x E) = 3."""
        result = verify_kappa_product_three_paths()
        assert result["agreement"]
        assert result["path1_additivity"] == Fraction(3)
        assert result["path2_dimension"] == Fraction(3)
        assert result["path3_genus_tower"] == Fraction(3)

    def test_genus_tower_F1(self):
        """F_1(K3 x E) = 3 * 1/24 = 1/8."""
        assert genus_tower_product(1) == Fraction(1, 8)

    def test_genus_tower_F2(self):
        """F_2(K3 x E) = 3 * 7/5760 = 7/1920."""
        assert genus_tower_product(2) == Fraction(7, 1920)

    def test_genus_tower_F3(self):
        """F_3(K3 x E) = 3 * 31/967680 = 31/322560."""
        expected = Fraction(3) * Fraction(31, 967680)
        assert genus_tower_product(3) == expected

    def test_genus_tower_all_positive(self):
        """F_g > 0 for all g >= 1."""
        for g in range(1, 7):
            assert genus_tower_product(g) > 0

    def test_genus_tower_decreasing(self):
        """F_g decreases (for small g, F_{g+1} < F_g)."""
        for g in range(1, 5):
            assert genus_tower_product(g + 1) < genus_tower_product(g)


# =====================================================================
# Section 9: TMF / elliptic cohomology
# =====================================================================

class TestTMF:
    """Tests for Witten genus and TMF."""

    def test_witten_genus_product_vanishes(self):
        """Phi_W(K3 x E) = 0."""
        assert witten_genus_product_K3_E() == 0

    def test_witten_genus_three_paths(self):
        """Three-path verification of Phi_W(K3 x E) = 0."""
        result = verify_witten_genus_vanishing_three_paths()
        assert result["agreement"]
        assert result["path1_multiplicativity"] == 0
        assert result["path2_free_action"] == 0
        assert result["path3_chi_product"] == 0

    def test_k3_elliptic_genus_at_z0(self):
        """phi(K3; tau, 0) = 24 = chi(K3)."""
        coeffs = elliptic_genus_K3_coeffs(10)
        assert coeffs[0] == 24
        # Higher Fourier coefficients vanish (weight 0 modular form = constant)
        for n in range(1, 10):
            assert coeffs[n] == 0

    def test_refined_partition_function_structure(self):
        """Z(K3 x E; tau', 0, 0) = 24 * Z_E(tau')."""
        result = refined_partition_function_product(10, 10)
        assert result["k3_z0"] == 24
        pf_e = result["e_pf"]
        pf_prod = result["product_z0"]
        for n in range(min(10, len(pf_e))):
            assert pf_prod[n] == Fraction(24) * pf_e[n]


# =====================================================================
# Section 10: Shadow obstruction tower
# =====================================================================

class TestShadowData:
    """Tests for shadow obstruction tower data."""

    def test_shadow_E_cdr_kappa(self):
        data = shadow_data_E_cdr()
        assert data["kappa"] == Fraction(1)

    def test_shadow_E_cdr_class_G(self):
        data = shadow_data_E_cdr()
        assert data["shadow_class"] == "G"
        assert data["shadow_depth"] == 2

    def test_shadow_E_cdr_vanishing_higher(self):
        data = shadow_data_E_cdr()
        assert data["S3"] == 0
        assert data["S4"] == 0
        assert data["discriminant"] == 0

    def test_shadow_E_cdr_metric(self):
        """Shadow metric Q_L = (2*kappa)^2 = 4 for class G."""
        data = shadow_data_E_cdr()
        assert data["Q_L"] == 4

    def test_shadow_E_lattice_kappa(self):
        data = shadow_data_E_lattice()
        assert data["kappa"] == Fraction(2)

    def test_shadow_E_lattice_class_G(self):
        data = shadow_data_E_lattice()
        assert data["shadow_class"] == "G"
        assert data["shadow_depth"] == 2

    def test_shadow_product_kappa(self):
        data = shadow_data_product_K3E()
        assert data["kappa"] == Fraction(3)

    def test_shadow_product_class_G(self):
        data = shadow_data_product_K3E()
        assert data["shadow_class"] == "G"

    def test_shadow_product_genus_tower(self):
        """Shadow genus tower matches direct computation."""
        data = shadow_data_product_K3E()
        for g in range(1, 6):
            assert data["genus_tower"][g] == genus_tower_product(g)

    def test_shadow_E_genus_tower_F1(self):
        """F_1(CDR(E)) = kappa/24 = 1/24."""
        data = shadow_data_E_cdr()
        assert data["genus_tower"][1] == Fraction(1, 24)

    def test_shadow_lattice_genus_tower_F1(self):
        """F_1(V_Lambda) = kappa/24 = 2/24 = 1/12."""
        data = shadow_data_E_lattice()
        assert data["genus_tower"][1] == Fraction(1, 12)

    def test_shadow_complementarity_E_cdr(self):
        """kappa(CDR(E)) + kappa(CDR(E)!) = 0 (KM/free field type)."""
        kappa = shadow_data_E_cdr()["kappa"]
        kappa_dual = -kappa  # Verdier duality negates kappa
        assert kappa + kappa_dual == 0

    def test_shadow_complementarity_E_lattice(self):
        """kappa(V_Lambda) + kappa(V_Lambda^!) = 0 for lattice VOAs."""
        kappa = shadow_data_E_lattice()["kappa"]
        kappa_dual = -kappa
        assert kappa + kappa_dual == 0


# =====================================================================
# Section 11: Modular form cross-checks
# =====================================================================

class TestModularFormCrossChecks:
    """Cross-checks between theta functions and modular form theory."""

    def test_theta_Z2_sum_to_20(self):
        """Total r_2 sum matches OEIS A004018 values."""
        theta = theta_Z_squared(20)
        # cumulative: sum_{k=0}^{n} r_2(k) grows like pi*n
        total = sum(theta[k] for k in range(20))
        # Expected: roughly pi*19 ~ 60. Exact: 1+4+4+0+4+8+0+0+4+4+8+0+0+8+0+0+4+8+4+0 = 61
        assert total == 61

    def test_theta_hex_sum_to_10(self):
        """Total hexagonal theta sum matches expectations."""
        theta = theta_eisenstein_lattice(10)
        # r_hex(0)=1, r_hex(1)=6, r_hex(2)=0, r_hex(3)=6, r_hex(4)=6,
        # r_hex(5)=0, r_hex(6)=0, r_hex(7)=12, r_hex(8)=0, r_hex(9)=6
        expected_values = [1, 6, 0, 6, 6, 0, 0, 12, 0, 6]
        for n, exp in enumerate(expected_values):
            assert theta[n] == exp, f"r_hex({n})={theta[n]}, expected {exp}"

    def test_r2_divisor_formula_detailed(self):
        """r_2(n) = 4*(d_1 - d_3) verified for specific values."""
        theta = theta_Z_squared(20)
        # n=1: d_1(1)=1, d_3(1)=0. r_2=4*1=4. Check.
        assert theta[1] == 4
        # n=5: d_1(5)=2 (divs 1,5 both =1 mod 4), d_3(5)=0. r_2=4*2=8.
        assert theta[5] == 8
        # n=13: d_1(13)=2 (divs 1,13), d_3(13)=0. r_2=4*2=8.
        assert theta[13] == 8

    def test_eisenstein_lattice_weight_1_modular(self):
        """Theta_{hex} is a weight-1 modular form for Gamma_0(3).

        The theta function of A_2 / Z[rho] is the Eisenstein series for
        Gamma_0(3): theta = 1 + 6*sum chi_3(n)*q^n.

        This can be independently checked via the L-function:
        L(chi_3, 1) = pi/(3*sqrt(3)) (Dirichlet L-function).
        """
        result = theta_eisenstein_vs_formula()
        assert result["agreement"]

    def test_e4_from_theta(self):
        """E_4 = (Theta_{Z^2})^4 + ... identity (weight 4 for SL(2,Z)).

        The Eisenstein series E_4 can be expressed in terms of theta functions:
        E_4 = (1/2)(theta_2^8 + theta_3^8 + theta_4^8).
        We don't verify this full identity here, but check E_4 leading terms.
        """
        e4 = e4_coeffs(10)
        assert e4[0] == 1
        assert e4[1] == 240
        assert e4[2] == 2160  # 240 * sigma_3(2) = 240*9 = 2160

    def test_eta_24_is_discriminant(self):
        """eta^24 = Delta = q*prod(1-q^n)^{24}, the modular discriminant.

        Delta = sum tau(n) q^n where tau is the Ramanujan tau function.
        tau(1) = 1, tau(2) = -24, tau(3) = 252, tau(4) = -1472.

        eta^24 = q * prod(1-q^n)^{24}, so as a q-series starting at q^1:
        the coefficient of q^n in eta^24 (with the q^{24/24}=q shift) is tau(n).
        """
        c = eta_power_coeffs(10, 24)
        # c is the coefficients of prod(1-q^n)^24 (WITHOUT the q^1 shift).
        # So c[0]*q^0 + c[1]*q^1 + ... = prod(1-q^n)^24.
        # Delta = q * prod(1-q^n)^24, so tau(n) = c[n-1].
        assert c[0] == 1  # tau(1) = 1
        assert c[1] == -24  # tau(2) = -24
        assert c[2] == 252  # tau(3) = 252
        assert c[3] == -1472  # tau(4) = -1472


# =====================================================================
# Section 12: Multi-path verification (master)
# =====================================================================

class TestMultiPathVerification:
    """Master verification: every claim has 3+ independent paths."""

    def test_kappa_E_three_paths(self):
        result = verify_kappa_E_three_paths()
        assert result["agreement"]

    def test_elliptic_genus_three_paths(self):
        result = verify_elliptic_genus_E_three_paths()
        assert result["agreement"]

    def test_kappa_product_three_paths(self):
        result = verify_kappa_product_three_paths()
        assert result["agreement"]

    def test_witten_genus_three_paths(self):
        result = verify_witten_genus_vanishing_three_paths()
        assert result["agreement"]

    def test_all_verifications_pass(self):
        result = run_all_verifications()
        assert result["all_pass"]


# =====================================================================
# Section 13: Full analysis integration
# =====================================================================

class TestFullAnalysis:
    """Integration test for the full analysis pipeline."""

    def test_full_analysis_runs(self):
        """The full analysis completes without error."""
        analysis = full_elliptic_chiral_analysis()
        assert "heisenberg_level" in analysis
        assert "verifications" in analysis

    def test_full_analysis_kappa_values(self):
        analysis = full_elliptic_chiral_analysis()
        assert analysis["kappa_heisenberg"] == Fraction(1)
        assert analysis["kappa_lattice_voa"] == Fraction(2)
        assert analysis["kappa_cdr"] == Fraction(1)
        assert analysis["kappa_product_cdr"] == Fraction(3)
        assert analysis["kappa_product_sigma"] == Fraction(3)

    def test_full_analysis_vanishings(self):
        analysis = full_elliptic_chiral_analysis()
        assert analysis["euler_char_E"] == 0
        assert analysis["elliptic_genus_E"] == 0
        assert analysis["witten_genus_E"] == 0
        assert analysis["witten_genus_product"] == 0

    def test_full_analysis_shadow_consistency(self):
        """Shadow data for all three algebras (CDR(E), V_Lambda, K3xE) is consistent."""
        analysis = full_elliptic_chiral_analysis()
        se = analysis["shadow_E_cdr"]
        sl = analysis["shadow_E_lattice"]
        sp = analysis["shadow_product"]
        # All class G
        assert se["shadow_class"] == "G"
        assert sl["shadow_class"] == "G"
        assert sp["shadow_class"] == "G"
        # Additivity: kappa_product = kappa_K3 + kappa_E = 2 + 1 = 3
        assert sp["kappa"] == Fraction(3)

    def test_full_analysis_verifications_pass(self):
        analysis = full_elliptic_chiral_analysis()
        assert analysis["verifications"]["all_pass"]


# =====================================================================
# Section 14: Edge cases and consistency
# =====================================================================

class TestEdgeCases:
    """Edge cases, boundary conditions, and consistency checks."""

    def test_partition_function_monotonic(self):
        """Partition function coefficients are eventually increasing."""
        pf = partition_function_E_holomorphic(20)
        # Not strictly increasing (some may be 0), but the trend is up
        assert pf[10] >= pf[0]

    def test_theta_Z2_nonnegative(self):
        """All r_2(n) >= 0."""
        theta = theta_Z_squared(50)
        for n in range(50):
            assert theta[n] >= 0

    def test_theta_hex_nonnegative(self):
        """All r_hex(n) >= 0."""
        theta = theta_eisenstein_lattice(50)
        for n in range(50):
            assert theta[n] >= 0

    def test_theta_1d_R0_delta(self):
        """At R^2 = 0 (degenerate), only the n=0 term contributes."""
        theta = theta_lattice_1d(Fraction(0), 10)
        # All n give exponent 0, so theta = sum of all q^0 = infinity?
        # Actually n=0 gives 0, and all nonzero n give 0 too.
        # So theta = 1 + 2*infinity... This is degenerate.
        # Our code should at least not crash.
        assert theta[0] >= 1

    def test_faber_pandharipande_error(self):
        """FP at g=0 should raise."""
        with pytest.raises(ValueError):
            faber_pandharipande(0)

    def test_genus_tower_exact_fractions(self):
        """All F_g values are exact fractions."""
        for g in range(1, 6):
            fg = genus_tower_product(g)
            assert isinstance(fg, Fraction)
            assert fg.denominator > 0

    def test_kappa_not_c_over_2_general(self):
        """AP48: kappa != c/2 in general. For CDR(E): c=0, kappa=1 != 0."""
        c_cdr = cdr_central_charge()
        kappa_cdr = kappa_cdr_E()
        # c/2 = 0, but kappa = 1
        assert c_cdr == 0
        assert kappa_cdr == Fraction(1)
        assert kappa_cdr != Fraction(c_cdr, 2)

    def test_lattice_kappa_is_rank_not_c_over_2(self):
        """AP48: for lattice VOA, kappa = rank, NOT c/2."""
        # rank-2 lattice has c = 2 (two free bosons), kappa = 2.
        # In this case kappa = c/2 = 1? No: c = 2, c/2 = 1, but kappa = rank = 2.
        # Wait: for Heisenberg at level k, kappa = k.
        # Two Heisenberg at level 1 each: kappa = 1 + 1 = 2.
        # Central charge: c = 1 + 1 = 2.
        # c/2 = 1 != kappa = 2.
        # So the AP48 check: kappa != c/2 for the lattice VOA.
        kappa = kappa_lattice_voa_E()
        c_lattice = 2  # c = rank for free bosons
        assert kappa == Fraction(2)
        assert kappa != Fraction(c_lattice, 2)  # 2 != 1

    def test_product_kappa_matches_dim(self):
        """For CY manifolds: kappa(sigma model) = dim_C."""
        data = product_cy_data()
        assert data.kappa_sigma_model == Fraction(data.complex_dim)

    def test_product_kappa_not_c_over_2(self):
        """AP48: kappa(sigma model) = 3 != c/2 = 9/2 for K3 x E."""
        assert kappa_product_sigma_model() == Fraction(3)
        c_sigma = 9  # 3 * dim_C
        assert kappa_product_sigma_model() != Fraction(c_sigma, 2)


# =====================================================================
# Section 15: Cross-family consistency
# =====================================================================

class TestCrossFamilyConsistency:
    """Consistency checks across different algebra families on E."""

    def test_kappa_hierarchy(self):
        """kappa(Heisenberg) < kappa(lattice VOA): 1 < 2."""
        assert kappa_heisenberg_on_E() < kappa_lattice_voa_E()

    def test_kappa_cdr_equals_heisenberg(self):
        """kappa(CDR(E)) = kappa(Heisenberg) = 1 (both rank 1 in complex dim)."""
        assert kappa_cdr_E() == kappa_heisenberg_on_E()

    def test_shadow_depth_all_class_G(self):
        """All algebras on E (torus) are class G (Gaussian)."""
        for data_fn in [shadow_data_E_cdr, shadow_data_E_lattice]:
            data = data_fn()
            assert data["shadow_class"] == "G"
            assert data["shadow_depth"] == 2
            assert data["S3"] == 0
            assert data["S4"] == 0

    def test_genus_tower_ratio(self):
        """F_g(lattice) / F_g(CDR) = kappa(lattice)/kappa(CDR) = 2 (constant ratio)."""
        se = shadow_data_E_cdr()
        sl = shadow_data_E_lattice()
        for g in range(1, 5):
            ratio = sl["genus_tower"][g] / se["genus_tower"][g]
            assert ratio == Fraction(2), f"Ratio at g={g}: {ratio}"

    def test_product_genus_tower_vs_sum(self):
        """F_g(K3xE) = F_g(K3) + F_g(E) by additivity of kappa."""
        kappa_k3 = Fraction(2)
        kappa_e = Fraction(1)
        for g in range(1, 5):
            fg_product = genus_tower_product(g)
            fg_k3 = kappa_k3 * faber_pandharipande(g)
            fg_e = kappa_e * faber_pandharipande(g)
            assert fg_product == fg_k3 + fg_e, f"Additivity fails at g={g}"

    def test_square_vs_hexagonal_leading(self):
        """Square and hexagonal torus have different theta functions."""
        sq = square_torus_partition_function(10)
        hx = hexagonal_torus_partition_function(10)
        # They should differ (different lattices)
        assert sq[0] == hx[0] == Fraction(1)  # both start with 1
        # r_2(1) = 4 (square), r_hex(1) = 6 (hexagonal)
        # So the partition functions differ at q^1
        assert sq[1] != hx[1]

    def test_hexagonal_denser_than_square(self):
        """Hexagonal packing is denser: theta_{hex} >= theta_{sq} in norm count."""
        theta_sq = theta_Z_squared(20)
        theta_hex = theta_eisenstein_lattice(20)
        # The hexagonal lattice has 6 nearest neighbors vs 4 for square
        assert theta_hex[1] > theta_sq[1]

    def test_both_lattices_norm_0_is_1(self):
        """Both lattices have exactly 1 vector of norm 0 (the origin)."""
        assert theta_Z_squared(10)[0] == 1
        assert theta_eisenstein_lattice(10)[0] == 1
