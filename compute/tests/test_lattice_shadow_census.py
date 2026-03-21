"""Tests for lattice_shadow_census: shadow tower, theta functions, genus expansion.

70+ tests verifying:
  - Shadow tower termination (Gaussian class G) for all lattice VOAs
  - Theta function coefficients against known values (root counts, E_4, Leech)
  - Genus expansion against Faber-Pandharipande numbers
  - Tridegree decomposition triviality
  - Gram matrix properties (determinants, evenness, unimodularity)
  - Complementarity data
  - Additivity (independent sum factorization)
  - Partition function coefficients

Mathematical ground truth:
  - lattice_foundations.tex: thm:lattice:curvature-braiding-orthogonal
  - higher_genus_modular_koszul.tex: shadow depth classification
  - concordance.tex: sec:concordance-lattice-shadow
"""

import math
import pytest
import numpy as np

from sympy import Rational

from compute.lib.lattice_shadow_census import (
    faber_pandharipande,
    root_lattice_gram,
    get_gram_matrix,
    get_rank,
    lattice_theta_coefficients,
    hypercubic_theta_coefficients,
    leech_theta_coefficients,
    e8_theta_coefficients,
    lattice_shadow_data,
    lattice_genus_expansion,
    lattice_tridegree_table,
    lattice_partition_function_coefficients,
    lattice_complementarity,
    effective_action_correction,
    full_census,
    verify_additivity,
    gram_determinant,
    is_even_lattice,
    dual_lattice_index,
    _ramanujan_tau,
    _sigma_k,
)


# =========================================================================
# Faber-Pandharipande numbers
# =========================================================================

class TestFaberPandharipande:
    """Exact values of lambda_g^FP."""

    def test_fp_genus1(self):
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_fp_genus2(self):
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_fp_genus3(self):
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_fp_genus4(self):
        # lambda_4 = (2^7-1)/2^7 * |B_8|/8! = 127/128 * (1/30) / 40320
        # B_8 = -1/30, |B_8| = 1/30
        # = 127 / (128 * 30 * 40320) = 127 / 154828800
        assert faber_pandharipande(4) == Rational(127, 154828800)

    def test_fp_genus5(self):
        # lambda_5 = (2^9-1)/2^9 * |B_{10}|/10!
        # B_{10} = 5/66, |B_{10}| = 5/66
        # = 511/512 * (5/66) / 3628800 = 511*5 / (512*66*3628800)
        # = 2555 / 122624409600
        val = faber_pandharipande(5)
        assert val == Rational(2555, 122624409600)

    def test_fp_invalid_genus(self):
        with pytest.raises(ValueError):
            faber_pandharipande(0)

    def test_fp_positivity(self):
        """All FP numbers are positive."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0

    def test_fp_monotone_decrease(self):
        """FP numbers decrease with genus."""
        for g in range(1, 7):
            assert faber_pandharipande(g) > faber_pandharipande(g + 1)


# =========================================================================
# Gram matrices
# =========================================================================

class TestGramMatrices:
    """Gram matrix construction and properties."""

    def test_a2_gram(self):
        G = root_lattice_gram('A2')
        expected = np.array([[2, -1], [-1, 2]])
        np.testing.assert_array_equal(G, expected)

    def test_a2_det(self):
        G = root_lattice_gram('A2')
        assert gram_determinant(G) == 3

    def test_d4_rank(self):
        G = root_lattice_gram('D4')
        assert G.shape == (4, 4)

    def test_d4_det(self):
        G = root_lattice_gram('D4')
        assert gram_determinant(G) == 4

    def test_e6_det(self):
        G = root_lattice_gram('E6')
        assert gram_determinant(G) == 3

    def test_e7_det(self):
        G = root_lattice_gram('E7')
        assert gram_determinant(G) == 2

    def test_e8_det(self):
        """E_8 is unimodular: det = 1."""
        G = root_lattice_gram('E8')
        assert gram_determinant(G) == 1

    def test_e8_unimodular(self):
        G = root_lattice_gram('E8')
        assert dual_lattice_index(G) == 1

    def test_all_even(self):
        """All root lattice Gram matrices define even lattices."""
        for name in ['A2', 'A3', 'D4', 'D5', 'E6', 'E7', 'E8']:
            G = root_lattice_gram(name)
            assert is_even_lattice(G), f"{name} should be even"

    def test_hypercubic_even(self):
        """Hypercubic lattice Z^n (with norm 2) is even."""
        for n in range(1, 9):
            G = get_gram_matrix(f'Z{n}') if n > 1 else get_gram_matrix('Z')
            assert is_even_lattice(G), f"Z^{n} should be even"

    def test_hypercubic_det(self):
        """det(Z^n) = 2^n."""
        for n in range(1, 9):
            name = f'Z{n}' if n > 1 else 'Z'
            G = get_gram_matrix(name)
            assert gram_determinant(G) == 2 ** n

    def test_z_alias(self):
        """'Z' and 'Z1' give the same lattice."""
        G1 = get_gram_matrix('Z')
        G2 = get_gram_matrix('Z1')
        np.testing.assert_array_equal(G1, G2)

    def test_symmetric(self):
        """All Gram matrices are symmetric."""
        for name in ['A2', 'D4', 'E8', 'Z', 'Z4']:
            G = get_gram_matrix(name)
            np.testing.assert_array_equal(G, G.T)

    def test_positive_definite(self):
        """All Gram matrices are positive definite."""
        for name in ['A2', 'A3', 'D4', 'D5', 'E6', 'E7', 'E8']:
            G = root_lattice_gram(name)
            eigenvalues = np.linalg.eigvalsh(G)
            assert all(ev > 0 for ev in eigenvalues), f"{name} not positive definite"


# =========================================================================
# Shadow tower data
# =========================================================================

class TestShadowTower:
    """Shadow tower invariants for all lattice VOAs."""

    @pytest.mark.parametrize("name,expected_rank", [
        ('Z', 1), ('Z2', 2), ('Z3', 3), ('Z4', 4),
        ('Z5', 5), ('Z6', 6), ('Z7', 7), ('Z8', 8),
        ('A2', 2), ('D4', 4), ('E8', 8), ('Leech', 24),
    ])
    def test_kappa_equals_rank(self, name, expected_rank):
        """kappa(V_Lambda) = rank(Lambda) for all lattice VOAs."""
        data = lattice_shadow_data(name)
        assert data['kappa'] == Rational(expected_rank)

    @pytest.mark.parametrize("name", [
        'Z', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8',
        'A2', 'D4', 'E8', 'Leech',
    ])
    def test_cubic_vanishes(self, name):
        """Cubic shadow C = 0 for all lattice VOAs."""
        data = lattice_shadow_data(name)
        assert data['cubic_shadow'] == 0

    @pytest.mark.parametrize("name", [
        'Z', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8',
        'A2', 'D4', 'E8', 'Leech',
    ])
    def test_quartic_vanishes(self, name):
        """Quartic contact Q = 0 for all lattice VOAs."""
        data = lattice_shadow_data(name)
        assert data['quartic_contact'] == 0

    @pytest.mark.parametrize("name", [
        'Z', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8',
        'A2', 'D4', 'E8', 'Leech',
    ])
    def test_shadow_depth_two(self, name):
        """Shadow depth = 2 (Gaussian class) for all lattice VOAs."""
        data = lattice_shadow_data(name)
        assert data['shadow_depth'] == 2

    @pytest.mark.parametrize("name", [
        'Z', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8',
        'A2', 'D4', 'E8', 'Leech',
    ])
    def test_gaussian_class(self, name):
        """All lattice VOAs are class G (Gaussian)."""
        data = lattice_shadow_data(name)
        assert data['shadow_class'] == 'G'

    @pytest.mark.parametrize("name", [
        'Z', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8',
        'A2', 'D4', 'E8', 'Leech',
    ])
    def test_discriminant_zero(self, name):
        """Critical discriminant Delta = 0 for all lattice VOAs."""
        data = lattice_shadow_data(name)
        assert data['critical_discriminant'] == 0

    @pytest.mark.parametrize("name,expected_rank", [
        ('Z', 1), ('Z4', 4), ('E8', 8), ('Leech', 24),
    ])
    def test_shadow_metric_value(self, name, expected_rank):
        """Shadow metric Q_L = (2*kappa)^2 = 4*rank^2."""
        data = lattice_shadow_data(name)
        assert data['shadow_metric'] == 4 * Rational(expected_rank) ** 2

    def test_central_charge_equals_rank(self):
        """c = rank for lattice VOAs."""
        for name in ['Z', 'A2', 'D4', 'E8', 'Leech']:
            data = lattice_shadow_data(name)
            assert data['central_charge'] == data['kappa']

    def test_alpha_zero(self):
        """Cubic coefficient alpha = 0 on primary line."""
        for name in ['Z', 'A2', 'D4', 'E8']:
            data = lattice_shadow_data(name)
            assert data['alpha'] == 0

    def test_s4_zero(self):
        """Quartic coefficient S_4 = 0 on primary line."""
        for name in ['Z', 'A2', 'D4', 'E8']:
            data = lattice_shadow_data(name)
            assert data['S4'] == 0


# =========================================================================
# Genus expansion
# =========================================================================

class TestGenusExpansion:
    """Genus expansion F_g = rank * lambda_g^FP."""

    def test_f1_all_lattices(self):
        """F_1 = rank/24 for all lattice VOAs."""
        for name, expected_rank in [('Z', 1), ('A2', 2), ('D4', 4), ('E8', 8), ('Leech', 24)]:
            expansion = lattice_genus_expansion(expected_rank, max_g=1)
            assert expansion[1] == Rational(expected_rank, 24)

    def test_f2_rank1(self):
        """F_2(V_Z) = 7/5760."""
        expansion = lattice_genus_expansion(1, max_g=2)
        assert expansion[2] == Rational(7, 5760)

    def test_f2_rank8(self):
        """F_2(V_{E_8}) = 8 * 7/5760 = 7/720."""
        expansion = lattice_genus_expansion(8, max_g=2)
        assert expansion[2] == Rational(8) * Rational(7, 5760)

    def test_f3_rank1(self):
        """F_3(V_Z) = 31/967680."""
        expansion = lattice_genus_expansion(1, max_g=3)
        assert expansion[3] == Rational(31, 967680)

    def test_genus_proportional_to_rank(self):
        """F_g scales linearly with rank."""
        for g in range(1, 4):
            fp = faber_pandharipande(g)
            for r in [1, 2, 4, 8]:
                expansion = lattice_genus_expansion(r, max_g=g)
                assert expansion[g] == r * fp

    def test_leech_f1(self):
        """F_1(V_Leech) = 24/24 = 1."""
        expansion = lattice_genus_expansion(24, max_g=1)
        assert expansion[1] == Rational(1)


# =========================================================================
# Theta function coefficients
# =========================================================================

class TestThetaCoefficients:
    """Theta function coefficients r_Lambda(n)."""

    def test_z_theta_r0(self):
        """r_Z(0) = 1 (zero vector)."""
        G = get_gram_matrix('Z')
        coeffs = lattice_theta_coefficients(G, max_n=5)
        assert coeffs[0] == 1

    def test_z_theta_r1(self):
        """r_Z(1) = 2 for Z with norm (m,m) = 2m^2.

        (m,m)/2 = m^2.  So r(1) = #{m : m^2 = 1} = 2 (m=+/-1).
        """
        G = get_gram_matrix('Z')
        coeffs = lattice_theta_coefficients(G, max_n=5)
        assert coeffs[1] == 2

    def test_z_theta_r2(self):
        """r_Z(2) = 0 for Z with norm (m,m) = 2m^2.

        (m,m)/2 = m^2.  Need m^2 = 2, no integer solution.
        """
        G = get_gram_matrix('Z')
        coeffs = lattice_theta_coefficients(G, max_n=5)
        assert coeffs[2] == 0

    def test_z_theta_r4(self):
        """r_Z(4) = 2: m^2 = 4, m = +/-2."""
        G = get_gram_matrix('Z')
        coeffs = lattice_theta_coefficients(G, max_n=5)
        assert coeffs[4] == 2

    def test_z_theta_perfect_squares(self):
        """r_Z(n) = 2 iff n is a perfect square > 0, else 0."""
        G = get_gram_matrix('Z')
        coeffs = lattice_theta_coefficients(G, max_n=16)
        for n in range(1, 17):
            sqrt_n = int(math.isqrt(n))
            if sqrt_n * sqrt_n == n:
                assert coeffs[n] == 2, f"r_Z({n}) should be 2"
            else:
                assert coeffs[n] == 0, f"r_Z({n}) should be 0"

    def test_a2_roots(self):
        """r_{A_2}(1) = 6 (the 6 roots of A_2)."""
        G = root_lattice_gram('A2')
        coeffs = lattice_theta_coefficients(G, max_n=5)
        assert coeffs[1] == 6

    def test_d4_roots(self):
        """r_{D_4}(1) = 24 (the 24 roots of D_4)."""
        G = root_lattice_gram('D4')
        coeffs = lattice_theta_coefficients(G, max_n=3)
        assert coeffs[1] == 24

    def test_e8_roots(self):
        """r_{E_8}(1) = 240 (the 240 roots of E_8)."""
        coeffs = e8_theta_coefficients(max_n=5)
        assert coeffs[1] == 240

    def test_e8_second_shell(self):
        """r_{E_8}(2) = 2160."""
        coeffs = e8_theta_coefficients(max_n=5)
        assert coeffs[2] == 2160

    def test_e8_third_shell(self):
        """r_{E_8}(3) = 6720."""
        coeffs = e8_theta_coefficients(max_n=5)
        assert coeffs[3] == 6720

    def test_e8_is_e4(self):
        """Theta_{E_8} = E_4: check first 5 nonzero coefficients.

        E_4(q) = 1 + 240*sigma_3(n) q^n.
        """
        coeffs = e8_theta_coefficients(max_n=5)
        for n in range(6):
            if n == 0:
                assert coeffs[n] == 1
            else:
                assert coeffs[n] == 240 * _sigma_k(n, 3)

    def test_leech_no_roots(self):
        """r_{Leech}(1) = 0: the Leech lattice has no roots!"""
        coeffs = leech_theta_coefficients(max_n=5)
        assert coeffs[1] == 0

    def test_leech_minimal_vectors(self):
        """r_{Leech}(2) = 196560: the 196560 minimal vectors of the Leech lattice."""
        coeffs = leech_theta_coefficients(max_n=5)
        assert coeffs[2] == 196560

    def test_leech_r0(self):
        """r_{Leech}(0) = 1."""
        coeffs = leech_theta_coefficients(max_n=2)
        assert coeffs[0] == 1

    def test_leech_third_shell(self):
        """r_{Leech}(3) = 16773120."""
        coeffs = leech_theta_coefficients(max_n=5)
        assert coeffs[3] == 16773120

    def test_leech_fourth_shell(self):
        """r_{Leech}(4) = 398034000."""
        coeffs = leech_theta_coefficients(max_n=5)
        assert coeffs[4] == 398034000

    def test_z2_theta(self):
        """Z^2 theta = (theta_Z)^2.

        r_{Z^2}(n) = sum_{a+b=n} r_Z(a)*r_Z(b), where
        r_Z(k) = 2 if k is a perfect square > 0, r_Z(0) = 1.
        """
        G1 = get_gram_matrix('Z')
        G2 = get_gram_matrix('Z2')
        c1 = lattice_theta_coefficients(G1, max_n=10)
        c2 = lattice_theta_coefficients(G2, max_n=10)
        # Verify convolution
        for n in range(11):
            conv = sum(c1[a] * c1[n - a] for a in range(n + 1))
            assert c2[n] == conv, f"Z^2 theta at n={n}: got {c2[n]}, expected {conv}"

    def test_a2_r0(self):
        """r_{A_2}(0) = 1."""
        G = root_lattice_gram('A2')
        coeffs = lattice_theta_coefficients(G, max_n=1)
        assert coeffs[0] == 1


# =========================================================================
# Tridegree decomposition
# =========================================================================

class TestTridegree:
    """Tridegree decomposition of the shadow tower."""

    def test_arity2_nonzero(self):
        """Tridegree (g, 2, 0) = kappa for all g."""
        for rank in [1, 2, 4, 8]:
            table = lattice_tridegree_table(rank, max_g=2)
            for g in range(1, 3):
                assert table[(g, 2, 0)] == Rational(rank)

    def test_arity3_vanishes(self):
        """All tridegree entries with n = 3 vanish."""
        for rank in [1, 2, 4, 8]:
            table = lattice_tridegree_table(rank, max_g=2)
            for g in range(1, 3):
                for d in range(3):
                    assert table[(g, 3, d)] == 0

    def test_arity4_vanishes(self):
        """All tridegree entries with n = 4 vanish."""
        for rank in [1, 2, 4, 8]:
            table = lattice_tridegree_table(rank, max_g=2)
            for g in range(1, 3):
                for d in range(3):
                    assert table[(g, 4, d)] == 0

    def test_arity5_vanishes(self):
        """All tridegree entries with n = 5 vanish."""
        for rank in [1, 4]:
            table = lattice_tridegree_table(rank, max_g=2)
            for g in range(1, 3):
                for d in range(3):
                    assert table[(g, 5, d)] == 0

    def test_depth_nonzero_vanishes(self):
        """All tridegree entries with d >= 1 vanish."""
        table = lattice_tridegree_table(4, max_g=2)
        for g in range(1, 3):
            for n in range(2, 6):
                for d in range(1, 3):
                    assert table[(g, n, d)] == 0


# =========================================================================
# Complementarity
# =========================================================================

class TestComplementarity:
    """Koszul dual and complementarity data."""

    def test_e8_self_dual(self):
        """E_8 is unimodular, hence V_{E_8}^! = V_{E_8}."""
        data = lattice_shadow_data('E8')
        assert data['is_self_dual'] is True

    def test_leech_self_dual(self):
        """Leech is unimodular, hence V_Leech^! = V_Leech."""
        data = lattice_shadow_data('Leech')
        assert data['is_self_dual'] is True

    def test_a2_not_self_dual(self):
        """A_2 has det 3, not unimodular."""
        data = lattice_shadow_data('A2')
        assert data['is_self_dual'] is False

    def test_complementarity_sum_self_dual(self):
        """For unimodular lattice: kappa = kappa_dual (same lattice)."""
        G = root_lattice_gram('E8')
        kappa, kappa_dual, total = lattice_complementarity(G)
        assert kappa == kappa_dual
        assert total == 2 * Rational(8)

    def test_complementarity_rank_preserved(self):
        """Dual lattice has same rank, so kappa_dual = rank."""
        for name in ['Z', 'A2', 'D4']:
            G = get_gram_matrix(name)
            kappa, kappa_dual, _ = lattice_complementarity(G)
            assert kappa == kappa_dual


# =========================================================================
# Effective action corrections
# =========================================================================

class TestEffectiveAction:
    """All nonlinear corrections vanish for lattice VOAs."""

    def test_cubic_correction_zero(self):
        assert effective_action_correction(1, order=3) == 0

    def test_quartic_correction_zero(self):
        assert effective_action_correction(8, order=4) == 0

    def test_quintic_correction_zero(self):
        assert effective_action_correction(24, order=5) == 0


# =========================================================================
# Partition function
# =========================================================================

class TestPartitionFunction:
    """Genus-1 partition function coefficients."""

    def test_z_leading_coeff(self):
        """Leading coefficient of Z_1(V_Z) is 1 (from theta_0 * eta_inv_0)."""
        G = get_gram_matrix('Z')
        pf = lattice_partition_function_coefficients(G, max_n=5)
        assert pf[0] == 1

    def test_a2_leading_coeff(self):
        """Leading coefficient of Z_1(V_{A_2}) is 1."""
        G = root_lattice_gram('A2')
        pf = lattice_partition_function_coefficients(G, max_n=3)
        assert pf[0] == 1

    def test_z_second_coeff(self):
        """Second coefficient of Z_1(V_Z): theta_Z(1)*eta_inv(0) + theta_Z(0)*eta_inv(1).

        r_Z(1) = 2, eta_inv_1(rank=1) = p(1) = 1.
        So coeff = 2*1 + 1*1 = 3.
        """
        G = get_gram_matrix('Z')
        pf = lattice_partition_function_coefficients(G, max_n=3)
        assert pf[1] == 3


# =========================================================================
# Additivity
# =========================================================================

class TestAdditivity:
    """Independent sum factorization: kappa is additive."""

    def test_additivity_1_1(self):
        """F_g(V_{Z^2}) = F_g(V_Z) + F_g(V_Z)."""
        assert verify_additivity(1, 1, max_g=5)

    def test_additivity_2_2(self):
        """F_g(V_{Z^4}) = F_g(V_{Z^2}) + F_g(V_{Z^2})."""
        assert verify_additivity(2, 2, max_g=5)

    def test_additivity_1_7(self):
        """F_g(V_{Z^8}) = F_g(V_Z) + F_g(V_{Z^7})."""
        assert verify_additivity(1, 7, max_g=5)

    def test_additivity_3_5(self):
        assert verify_additivity(3, 5, max_g=5)


# =========================================================================
# Arithmetic helpers
# =========================================================================

class TestArithmeticHelpers:
    """Internal arithmetic functions."""

    def test_sigma_3_1(self):
        assert _sigma_k(1, 3) == 1

    def test_sigma_3_2(self):
        assert _sigma_k(2, 3) == 1 + 8  # 1^3 + 2^3 = 9

    def test_sigma_3_3(self):
        assert _sigma_k(3, 3) == 1 + 27  # 1^3 + 3^3 = 28

    def test_sigma_11_1(self):
        assert _sigma_k(1, 11) == 1

    def test_sigma_11_2(self):
        assert _sigma_k(2, 11) == 1 + 2048  # 1 + 2^11

    def test_ramanujan_tau_1(self):
        assert _ramanujan_tau(1) == 1

    def test_ramanujan_tau_2(self):
        assert _ramanujan_tau(2) == -24

    def test_ramanujan_tau_3(self):
        assert _ramanujan_tau(3) == 252

    def test_ramanujan_tau_4(self):
        assert _ramanujan_tau(4) == -1472

    def test_ramanujan_tau_5(self):
        assert _ramanujan_tau(5) == 4830


# =========================================================================
# Full census
# =========================================================================

class TestFullCensus:
    """End-to-end census over all standard lattice VOAs."""

    def test_census_runs(self):
        """Census completes without error."""
        results = full_census(max_n_theta=5, max_g=3)
        assert len(results) == 16  # all named lattices

    def test_census_all_gaussian(self):
        """Every entry in the census is Gaussian class."""
        results = full_census(max_n_theta=3, max_g=2)
        for name, data in results.items():
            assert data['shadow']['shadow_class'] == 'G', f"{name} not Gaussian"

    def test_census_all_depth_two(self):
        """Every entry in the census has shadow depth 2."""
        results = full_census(max_n_theta=3, max_g=2)
        for name, data in results.items():
            assert data['shadow']['shadow_depth'] == 2, f"{name} depth != 2"

    def test_census_kappa_rank_agreement(self):
        """kappa = rank for every census entry."""
        results = full_census(max_n_theta=3, max_g=2)
        for name, data in results.items():
            assert data['shadow']['kappa'] == Rational(data['shadow']['rank']), \
                f"{name}: kappa != rank"


# =========================================================================
# Edge cases and consistency
# =========================================================================

class TestConsistency:
    """Cross-checks and edge cases."""

    def test_e8_theta_via_gram_vs_formula(self):
        """E_8 theta from Gram matrix matches E_4 formula.

        For E_8 (rank 8, det 1), lattice_theta_coefficients dispatches to
        e8_theta_coefficients. This checks that the dispatch is consistent.
        """
        G = root_lattice_gram('E8')
        from_dispatch = lattice_theta_coefficients(G, max_n=5)
        from_e4 = e8_theta_coefficients(max_n=5)
        for n in range(6):
            assert from_dispatch[n] == from_e4[n], \
                f"E_8 theta mismatch at n={n}: dispatch={from_dispatch[n]}, E_4={from_e4[n]}"

    def test_leech_integrality(self):
        """All Leech theta coefficients are non-negative integers."""
        coeffs = leech_theta_coefficients(max_n=20)
        for n, c in enumerate(coeffs):
            assert isinstance(c, int), f"r_Leech({n}) not int"
            assert c >= 0, f"r_Leech({n}) = {c} < 0"

    def test_leech_growth(self):
        """Leech theta coefficients grow (after the gap at n=1)."""
        coeffs = leech_theta_coefficients(max_n=10)
        for n in range(3, 10):
            assert coeffs[n] > coeffs[n - 1], \
                f"Leech theta not growing at n={n}"

    def test_get_rank_by_name(self):
        """get_rank returns correct rank for named lattices."""
        assert get_rank('Z') == 1
        assert get_rank('A2') == 2
        assert get_rank('D4') == 4
        assert get_rank('E8') == 8
        assert get_rank('Leech') == 24

    def test_get_rank_by_gram(self):
        """get_rank from Gram matrix."""
        G = np.array([[2, -1], [-1, 2]])
        assert get_rank(G) == 2

    def test_unknown_lattice(self):
        with pytest.raises(ValueError):
            get_gram_matrix('F4')

    def test_d4_theta_r0(self):
        """r_{D_4}(0) = 1."""
        G = root_lattice_gram('D4')
        coeffs = lattice_theta_coefficients(G, max_n=1)
        assert coeffs[0] == 1
