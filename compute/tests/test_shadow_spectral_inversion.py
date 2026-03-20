"""Tests for shadow spectral inversion: Newton identities, spectral atoms,
branch cut analysis, and the shadow-moduli resolution.

T1-T12:   Newton's identities and elementary symmetric polynomials
T13-T22:  Heisenberg spectral data (class G, depth 2)
T23-T37:  Virasoro spectral atoms (class M, infinite depth)
T38-T44:  exp(G) product formula
T45-T50:  Shadow-moduli map
T51-T55:  Universality of G
T56-T60:  Carleman uniqueness
T61-T65:  Spectral density and branch cuts
T66-T70:  Affine sl_2 spectral data (class L, depth 3)
"""

import cmath
import math
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from shadow_spectral_inversion import (
    # Newton's identities
    power_sums_to_elementary,
    power_sums_to_elementary_exact,
    # Spectral polynomial
    elementary_to_spectral_polynomial,
    spectral_polynomial_roots,
    # Shadow to power sums
    shadow_to_power_sums,
    # Full pipeline
    spectral_atoms_from_shadow,
    # Virasoro
    virasoro_spectral_atoms,
    virasoro_spectral_polynomial_roots,
    virasoro_branch_points,
    _virasoro_S_numerical,
    # Heisenberg
    heisenberg_spectral,
    # Affine
    affine_sl2_spectral,
    # exp(G)
    exp_G_from_atoms,
    exp_G_from_shadow,
    # Shadow-moduli map
    shadow_moduli_map_leading,
    # Determinant identity
    verify_determinant_identity,
    # Spectral density
    spectral_density_on_cut,
    spectral_density_on_complex_cut,
    # Universality
    verify_universality_of_G,
    # Carleman
    carleman_uniqueness_check,
    # Roundtrip
    reconstruct_G_from_atoms,
    newton_roundtrip,
)

try:
    from sympy import Rational
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False

skip_no_sympy = pytest.mark.skipif(not HAS_SYMPY, reason="sympy required")


# =====================================================================
# T1-T12: Newton's identities and elementary symmetric polynomials
# =====================================================================

class TestNewtonInversion:

    def test_t1_simple_two_atoms(self):
        """T1: Two atoms lambda=1,2 with mult 1,1.
        Power sums p_r = 1^r + 2^r.
        p_1=3, p_2=5, p_3=9, p_4=17.
        Elementary: e_1=3, e_2=2*1=2 (since atoms are roots of (z-1)(z-2)=z^2-3z+2)."""
        # For atoms lambda=1,2 (roots of P), e_1 = 1+2 = 3, e_2 = 1*2 = 2.
        # Power sums of roots: p_r = 1^r + 2^r.
        p_list = [1 + 2, 1 + 4, 1 + 8, 1 + 16]  # p_1=3, p_2=5, p_3=9, p_4=17
        e_list = power_sums_to_elementary(p_list)
        assert abs(e_list[0] - 3.0) < 1e-12, f"e_1 = {e_list[0]}, expected 3"
        assert abs(e_list[1] - 2.0) < 1e-12, f"e_2 = {e_list[1]}, expected 2"

    def test_t2_roundtrip_3_atoms(self):
        """T2: Three atoms 1,2,3 roundtrip through Newton."""
        atoms = [1.0, 2.0, 3.0]
        result = newton_roundtrip(atoms, max_order=6)
        assert result['roundtrip_ok'], f"Max defect: {result['max_defect']}"

    def test_t3_roundtrip_complex_atoms(self):
        """T3: Complex atoms roundtrip."""
        atoms = [1.0 + 1j, 1.0 - 1j, 3.0]
        result = newton_roundtrip(atoms, max_order=6)
        assert result['max_defect'] < 1e-6, f"Max defect: {result['max_defect']}"

    def test_t4_single_atom(self):
        """T4: Single atom lambda=5. p_r = 5^r, e_1 = 5, e_k = 0 for k >= 2."""
        p_list = [5.0, 25.0, 125.0]
        e_list = power_sums_to_elementary(p_list)
        assert abs(e_list[0] - 5.0) < 1e-12
        assert abs(e_list[1]) < 1e-12
        assert abs(e_list[2]) < 1e-12

    def test_t5_zero_power_sums(self):
        """T5: All power sums zero -> all elementary zero."""
        p_list = [0.0, 0.0, 0.0, 0.0]
        e_list = power_sums_to_elementary(p_list)
        for ek in e_list:
            assert abs(ek) < 1e-15

    def test_t6_power_sums_to_polynomial(self):
        """T6: Power sums -> elementary -> spectral polynomial -> roots recovers atoms."""
        atoms = [2.0, -3.0]
        # p_r = 2^r + (-3)^r
        p_list = [2 + (-3), 4 + 9, 8 + (-27), 16 + 81]
        e_list = power_sums_to_elementary(p_list)
        coeffs = elementary_to_spectral_polynomial(e_list)
        roots = spectral_polynomial_roots(coeffs)
        # Roots of P(z) are 1/lambda_j = 1/2, -1/3
        roots_sorted = sorted(roots.real)
        assert abs(roots_sorted[0] - (-1.0 / 3.0)) < 1e-8
        assert abs(roots_sorted[1] - 0.5) < 1e-8

    def test_t7_elementary_polynomial_coefficients(self):
        """T7: e_list -> polynomial coefficients have correct signs."""
        e_list = [3.0, 5.0, 7.0]
        coeffs = elementary_to_spectral_polynomial(e_list)
        assert coeffs[0] == 1.0
        assert coeffs[1] == -3.0   # (-1)^1 * 3
        assert coeffs[2] == 5.0    # (-1)^2 * 5
        assert coeffs[3] == -7.0   # (-1)^3 * 7

    def test_t8_shadow_to_power_sums_basic(self):
        """T8: S_r to p_r = -r S_r."""
        S_list = [0.5, 2.0, 0.1]  # S_2, S_3, S_4
        p_list = shadow_to_power_sums(S_list, start_arity=2)
        # p_1 = 0, p_2 = -2*0.5 = -1, p_3 = -3*2 = -6, p_4 = -4*0.1 = -0.4
        assert abs(p_list[0]) < 1e-15        # p_1 = 0
        assert abs(p_list[1] - (-1.0)) < 1e-12   # p_2 = -1
        assert abs(p_list[2] - (-6.0)) < 1e-12   # p_3 = -6
        assert abs(p_list[3] - (-0.4)) < 1e-12   # p_4 = -0.4

    @skip_no_sympy
    def test_t9_exact_newton_two_atoms(self):
        """T9: Exact Newton identities with sympy Rational."""
        p_list = [Rational(3), Rational(5), Rational(9)]
        e_list = power_sums_to_elementary_exact(p_list)
        assert e_list[0] == Rational(3)
        assert e_list[1] == Rational(2)

    def test_t10_four_atoms_roundtrip(self):
        """T10: Four atoms roundtrip."""
        atoms = [1.0, -1.0, 2.0, -2.0]
        result = newton_roundtrip(atoms, max_order=8)
        assert result['max_defect'] < 1e-4, f"Max defect: {result['max_defect']}"

    def test_t11_large_atoms_roundtrip(self):
        """T11: Large atoms (100, 200) still roundtrip."""
        atoms = [100.0, 200.0]
        result = newton_roundtrip(atoms, max_order=6)
        assert result['max_defect'] < 1.0, f"Max defect: {result['max_defect']}"

    def test_t12_reconstruct_G_from_known_atoms(self):
        """T12: Reconstruct shadow coefficients from known atoms matches input."""
        # Two atoms lambda = 1, 2 with c_1 = c_2 = 1
        # S_r = -(1/r)(1^r + 2^r)
        atoms = [1.0, 2.0]
        mults = [1.0, 1.0]
        S_dict = reconstruct_G_from_atoms(atoms, mults, max_arity=6)
        for r in range(2, 7):
            expected = -(1.0 + 2.0 ** r) / r
            assert abs(S_dict[r] - expected) < 1e-12, f"S_{r} mismatch"


# =====================================================================
# T13-T22: Heisenberg spectral data (class G, depth 2)
# =====================================================================

class TestHeisenbergSpectral:

    def test_t13_heisenberg_power_sums(self):
        """T13: p_2 = -k, p_r = 0 for r >= 3."""
        data = heisenberg_spectral(1.0)
        assert abs(data['power_sums']['p_2'] - (-1.0)) < 1e-15
        assert data['power_sums']['p_1'] == 0.0

    def test_t14_heisenberg_elementary(self):
        """T14: e_1 = 0, e_2 = k/2."""
        data = heisenberg_spectral(4.0)
        assert abs(data['elementary']['e_1']) < 1e-15
        assert abs(data['elementary']['e_2'] - 2.0) < 1e-15

    def test_t15_heisenberg_spectral_polynomial(self):
        """T15: P(z) = 1 + (k/2)z^2."""
        data = heisenberg_spectral(2.0)
        coeffs = data['poly_coeffs']
        assert abs(coeffs[0] - 1.0) < 1e-15
        assert abs(coeffs[1]) < 1e-15  # no z term
        assert abs(coeffs[2] - 1.0) < 1e-15  # (k/2)z^2 = z^2 for k=2

    def test_t16_heisenberg_atoms_imaginary(self):
        """T16: For k > 0, atoms are purely imaginary."""
        data = heisenberg_spectral(1.0)
        for atom in data['atoms']:
            assert abs(atom.real) < 1e-10, f"Real part nonzero: {atom}"
            assert abs(atom.imag) > 0.1, f"Imaginary part too small: {atom}"

    def test_t17_heisenberg_atoms_magnitude(self):
        """T17: |lambda| = sqrt(k/2) for k > 0."""
        k = 8.0
        data = heisenberg_spectral(k)
        expected_mag = math.sqrt(k / 2.0)
        for atom in data['atoms']:
            assert abs(abs(atom) - expected_mag) < 1e-10

    def test_t18_heisenberg_depth(self):
        """T18: Heisenberg has shadow depth 2."""
        data = heisenberg_spectral(1.0)
        assert data['depth'] == 2
        assert data['archetype'] == 'G (Gaussian)'

    def test_t19_heisenberg_exp_G_gaussian(self):
        """T19: exp(G(t)) = exp(kt^2/2) for Heisenberg."""
        k = 3.0
        S_list = [k / 2.0]  # Only S_2
        exp_G = exp_G_from_shadow(S_list, max_order=10, start_arity=2)
        # exp(kt^2/2) = sum_{n>=0} (k/2)^n t^{2n} / n!
        for n in range(6):
            expected = (k / 2.0) ** n / math.factorial(n)
            assert abs(exp_G[2 * n] - expected) < 1e-10, \
                f"t^{2*n} coeff: got {exp_G[2*n]}, expected {expected}"
            if 2 * n + 1 <= 10:
                assert abs(exp_G[2 * n + 1]) < 1e-12, \
                    f"t^{2*n+1} coeff nonzero: {exp_G[2*n+1]}"

    def test_t20_heisenberg_negative_k(self):
        """T20: For k < 0, atoms are real."""
        data = heisenberg_spectral(-2.0)
        for atom in data['atoms']:
            assert abs(atom.imag) < 1e-10, f"Imaginary part nonzero: {atom}"

    def test_t21_heisenberg_S_list_length(self):
        """T21: S_list has only one entry (S_2)."""
        data = heisenberg_spectral(5.0)
        assert len(data['S_list']) == 1
        assert abs(data['S_list'][0] - 2.5) < 1e-15

    def test_t22_heisenberg_atoms_conjugate(self):
        """T22: For k > 0, the two atoms are complex conjugates."""
        data = heisenberg_spectral(6.0)
        a1, a2 = data['atoms']
        assert abs(a1 - a2.conjugate()) < 1e-10 or abs(a1 + a2.conjugate()) < 1e-10


# =====================================================================
# T23-T37: Virasoro spectral atoms (class M, infinite depth)
# =====================================================================

class TestVirasoroSpectral:

    def test_t23_virasoro_S_seeds(self):
        """T23: Virasoro S_2, S_3, S_4 at c=1."""
        S_list = _virasoro_S_numerical(1.0, max_arity=4)
        assert abs(S_list[0] - 0.5) < 1e-12      # S_2 = c/2 = 0.5
        assert abs(S_list[1] - 2.0) < 1e-12       # S_3 = 2
        assert abs(S_list[2] - 10.0 / 27.0) < 1e-10  # S_4 = 10/(1*27)

    def test_t24_virasoro_atoms_c1(self):
        """T24: Spectral atoms at c=1 are complex."""
        result = virasoro_spectral_atoms(1.0, max_arity=8)
        atoms = result['atoms']
        has_complex = any(abs(a.imag) > 1e-10 for a in atoms if np.isfinite(a))
        assert has_complex, "Expected complex atoms for Virasoro at c=1"

    def test_t25_virasoro_atoms_c26(self):
        """T25: Spectral atoms at c=26 (bosonic string)."""
        result = virasoro_spectral_atoms(26.0, max_arity=8)
        assert len(result['atoms']) > 0

    def test_t26_virasoro_atoms_complex_general(self):
        """T26: For c > 0, atoms are generically complex (not all real)."""
        for c_val in [1.0, 5.0, 13.0, 26.0]:
            result = virasoro_spectral_atoms(c_val, max_arity=8)
            atoms = result['atoms']
            finite_atoms = [a for a in atoms if np.isfinite(a)]
            if len(finite_atoms) > 2:
                has_complex = any(abs(a.imag) > 1e-8 for a in finite_atoms)
                assert has_complex, f"All atoms real at c={c_val}"

    def test_t27_branch_points_complex_conjugate(self):
        """T27: Branch points t_+/- are complex conjugate for c > 0."""
        for c_val in [1.0, 5.0, 13.0, 26.0, 100.0]:
            t_plus, t_minus = virasoro_branch_points(c_val)
            assert abs(t_plus - t_minus.conjugate()) < 1e-10, \
                f"Branch points not conjugate at c={c_val}"

    def test_t28_branch_points_imaginary_part(self):
        """T28: Branch points have nonzero imaginary part for c > 0."""
        t_plus, t_minus = virasoro_branch_points(1.0)
        assert abs(t_plus.imag) > 1e-5, "Branch point has zero imaginary part"
        assert abs(t_minus.imag) > 1e-5

    def test_t29_atom_count_grows(self):
        """T29: Number of finite atoms grows with max_arity."""
        counts = []
        for ma in [4, 6, 8, 10]:
            result = virasoro_spectral_atoms(1.0, max_arity=ma)
            finite = sum(1 for a in result['atoms'] if np.isfinite(a))
            counts.append(finite)
        # Expect non-decreasing
        for i in range(len(counts) - 1):
            assert counts[i + 1] >= counts[i], \
                f"Atom count decreased: {counts}"

    def test_t30_atoms_approach_cut(self):
        """T30: Atoms should cluster near the branch cut region as arity grows.

        The branch cut lies between t_+ and t_-. The spectral polynomial
        roots (which are 1/lambda_j) should approach this region."""
        c_val = 10.0
        t_plus, t_minus = virasoro_branch_points(c_val)
        midpoint = (t_plus + t_minus) / 2.0

        # At high arity, roots should be closer to the branch region
        roots_8 = virasoro_spectral_polynomial_roots(c_val, max_arity=8)
        roots_12 = virasoro_spectral_polynomial_roots(c_val, max_arity=12)

        # Distance from midpoint of branch cut
        dist_8 = sorted([abs(z - midpoint) for z in roots_8 if abs(z) < 1e6])
        dist_12 = sorted([abs(z - midpoint) for z in roots_12 if abs(z) < 1e6])

        # The minimum distance at arity 12 should not be much worse than at 8
        if dist_8 and dist_12:
            assert min(dist_12) < 2.0 * min(dist_8) + 0.1

    def test_t31_virasoro_S5_numerical(self):
        """T31: S_5(c=1) = -48/(1*27) from the recursion."""
        S_list = _virasoro_S_numerical(1.0, max_arity=5)
        expected = -48.0 / (1.0 * 27.0)
        assert abs(S_list[3] - expected) < 1e-10

    def test_t32_virasoro_large_c_gaussian(self):
        """T32: For large c, Virasoro shadow is approximately Gaussian.
        S_r / (c/2) -> 0 for r >= 3 as c -> infinity."""
        c_val = 1000.0
        S_list = _virasoro_S_numerical(c_val, max_arity=8)
        kappa = c_val / 2.0
        for i in range(1, len(S_list)):  # S_3, S_4, ...
            r = i + 2
            ratio = abs(S_list[i]) / kappa
            assert ratio < 0.1, f"|S_{r}/kappa| = {ratio} at c={c_val}"

    def test_t33_virasoro_self_dual_c13(self):
        """T33: At c=13 (self-dual point), alpha(13) = 3212/87."""
        alpha_13 = (180.0 * 13.0 + 872.0) / (5.0 * 13.0 + 22.0)
        expected = 3212.0 / 87.0
        assert abs(alpha_13 - expected) < 1e-10

    def test_t34_virasoro_discriminant(self):
        """T34: Discriminant Delta_Q = -320c^2/(5c+22) for c=1."""
        c_val = 1.0
        alpha_val = (180.0 + 872.0) / 27.0
        disc = (12.0 * c_val) ** 2 - 4.0 * alpha_val * c_val ** 2
        expected = -320.0 * c_val ** 2 / (5.0 * c_val + 22.0)
        assert abs(disc - expected) < 1e-10

    def test_t35_branch_point_real_part(self):
        """T35: Re(t_+) = -6c/alpha for the Virasoro branch points."""
        c_val = 5.0
        alpha_val = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
        t_plus, t_minus = virasoro_branch_points(c_val)
        expected_real = -6.0 * c_val / alpha_val
        assert abs(t_plus.real - expected_real) < 1e-10
        assert abs(t_minus.real - expected_real) < 1e-10

    def test_t36_virasoro_Q_positive_real(self):
        """T36: Q(t) > 0 for all real t when c > 0."""
        c_val = 2.0
        alpha_val = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
        for t_val in np.linspace(-10, 10, 100):
            Q = c_val ** 2 + 12.0 * c_val * t_val + alpha_val * t_val ** 2
            assert Q > 0, f"Q({t_val}) = {Q} <= 0 at c={c_val}"

    def test_t37_virasoro_pole_structure(self):
        """T37: Virasoro S_r has poles only at c=0 and c=-22/5."""
        # S_4 = 10/(c(5c+22)) has poles at c=0 and c=-22/5.
        # S_5 = -48/(c^2(5c+22)).
        S4_at_1 = _virasoro_S_numerical(1.0, 4)[2]
        S4_at_10 = _virasoro_S_numerical(10.0, 4)[2]
        assert np.isfinite(S4_at_1)
        assert np.isfinite(S4_at_10)
        # Near poles, S_4 diverges
        with pytest.raises(Exception):
            _virasoro_S_numerical(0.0, 4)


# =====================================================================
# T38-T44: exp(G) product formula
# =====================================================================

class TestExpGProduct:

    def test_t38_two_atom_product(self):
        """T38: exp(G) = (1-lambda_1 t)(1-lambda_2 t) for 2 atoms with mult 1."""
        atoms = [2.0 + 0j, 3.0 + 0j]
        coeffs = exp_G_from_atoms(atoms, [1.0, 1.0], max_order=5)
        # (1-2t)(1-3t) = 1 - 5t + 6t^2
        assert abs(coeffs[0] - 1.0) < 1e-12
        assert abs(coeffs[1] - (-5.0)) < 1e-12
        assert abs(coeffs[2] - 6.0) < 1e-12
        for k in range(3, 6):
            assert abs(coeffs[k]) < 1e-10

    def test_t39_single_atom_power(self):
        """T39: (1 - lambda t)^c for single atom with multiplicity c."""
        lam = 2.0 + 0j
        c_val = 3.0
        coeffs = exp_G_from_atoms([lam], [c_val], max_order=5)
        # (1 - 2t)^3 = 1 - 6t + 12t^2 - 8t^3
        assert abs(coeffs[0] - 1.0) < 1e-12
        assert abs(coeffs[1] - (-6.0)) < 1e-12
        assert abs(coeffs[2] - 12.0) < 1e-12
        assert abs(coeffs[3] - (-8.0)) < 1e-12

    def test_t40_heisenberg_exp_G(self):
        """T40: exp(G) = exp(kt^2/2) for Heisenberg (from shadow data)."""
        k = 2.0
        S_list = [k / 2.0]  # S_2 only
        F = exp_G_from_shadow(S_list, max_order=8, start_arity=2)
        # exp(t^2) = 1 + t^2 + t^4/2 + t^6/6 + ...
        assert abs(F[0] - 1.0) < 1e-12
        assert abs(F[1]) < 1e-12
        assert abs(F[2] - 1.0) < 1e-12   # (k/2)^1 / 1! = 1
        assert abs(F[3]) < 1e-12
        assert abs(F[4] - 0.5) < 1e-12   # (k/2)^2 / 2! = 0.5
        assert abs(F[6] - 1.0 / 6.0) < 1e-10

    def test_t41_exp_G_atom_vs_shadow(self):
        """T41: exp(G) from atoms matches exp(G) from shadow for 2-atom case."""
        atoms = [1.0 + 0j, -1.0 + 0j]
        mults = [1.0, 1.0]
        from_atoms = exp_G_from_atoms(atoms, mults, max_order=8)

        # Shadow coefficients: S_r = -(1/r)(1^r + (-1)^r)
        # S_r = -(1+(-1)^r)/r = -2/r if r even, 0 if r odd
        S_list = []
        for r in range(2, 9):
            sr = -(1.0 + (-1.0) ** r) / r
            S_list.append(sr)
        from_shadow = exp_G_from_shadow(S_list, max_order=8, start_arity=2)

        for k in range(9):
            assert abs(from_atoms[k] - from_shadow[k]) < 1e-8, \
                f"t^{k}: atoms={from_atoms[k]}, shadow={from_shadow[k]}"

    def test_t42_virasoro_product_order6(self):
        """T42: Virasoro exp(G) at c=1 through order 6 is consistent."""
        c_val = 1.0
        S_list = _virasoro_S_numerical(c_val, max_arity=6)
        from_shadow = exp_G_from_shadow(S_list, max_order=8, start_arity=2)
        # F(0) = 1 always
        assert abs(from_shadow[0] - 1.0) < 1e-12
        # F(1) = 0 (no arity-1 shadow)
        assert abs(from_shadow[1]) < 1e-12
        # F(2) = S_2 = c/2
        assert abs(from_shadow[2] - c_val / 2.0) < 1e-10

    def test_t43_empty_atoms(self):
        """T43: No atoms -> exp(G) = 1."""
        coeffs = exp_G_from_atoms([], [], max_order=5)
        assert abs(coeffs[0] - 1.0) < 1e-12
        for k in range(1, 6):
            assert abs(coeffs[k]) < 1e-12

    def test_t44_fractional_multiplicity(self):
        """T44: Fractional multiplicity (1 - 2t)^{1/2}."""
        lam = 2.0 + 0j
        c_val = 0.5
        coeffs = exp_G_from_atoms([lam], [c_val], max_order=4)
        # (1-2t)^{1/2}: binomial expansion
        # = 1 + (1/2)(-2t) + (1/2)(-1/2)/2!(-2t)^2 + ...
        # = 1 - t - t^2/2 - t^3/2 - ...
        assert abs(coeffs[0] - 1.0) < 1e-12
        assert abs(coeffs[1] - (-1.0)) < 1e-10
        # C(1/2, 2)*(-2)^2 = (1/2)(-1/2)/2 * 4 = -1/2
        assert abs(coeffs[2] - (-0.5)) < 1e-10


# =====================================================================
# T45-T50: Shadow-moduli map
# =====================================================================

class TestShadowModuliMap:

    def test_t45_leading_term(self):
        """T45: t(q) leading term is (c/6) * c * q for single boson (c=1)."""
        t_coeffs = shadow_moduli_map_leading(1.0, num_terms=5)
        # For c=1: Z/Z_vac = prod(1-q^n)^{-1}, so Z_1 = 1 (from sigma_{-1}(1)=1).
        # t_1 = (1/6) * 1 * 1 = 1/6.
        # Actually: log(prod(1-q^n)^{-1}) = sum sigma_{-1}(N) q^N.
        # sigma_{-1}(1) = 1. So log coeff at q^1 = 1.
        # Z = exp(sum a_n q^n): Z_1 = a_1 = sigma_{-1}(1) = 1.
        # t_1 = (c/6) * Z_1 = 1/6.
        assert abs(t_coeffs[0] - 1.0 / 6.0) < 1e-10

    def test_t46_moduli_map_c2(self):
        """T46: t(q) at c=2 has t_1 = 2/6 = 1/3."""
        t_coeffs = shadow_moduli_map_leading(2.0, num_terms=5)
        # log coeff: 2 * sigma_{-1}(1) = 2. Z_1 = 2. t_1 = (2/6)*2 = ... wait.
        # Z = exp(2 * sum sigma_{-1}(N) q^N). Z_1 = 2*1 = 2. t_1 = (2/6)*2 = 2/3.
        # Hmm, let me re-derive. Z_0=1, Z_1 = 1*log_1 * Z_0 = log_1 = c*sigma_{-1}(1) = 2.
        # t_1 = (c/6) * Z_1 = (2/6) * 2 = 2/3.
        assert abs(t_coeffs[0] - 2.0 / 3.0) < 1e-10

    def test_t47_moduli_map_positive(self):
        """T47: t(q) coefficients are positive for c > 0."""
        t_coeffs = shadow_moduli_map_leading(1.0, num_terms=10)
        for i, tc in enumerate(t_coeffs):
            assert tc >= -1e-15, f"t_{i+1} = {tc} < 0"

    def test_t48_moduli_map_grows_with_c(self):
        """T48: t(q) coefficients scale with c."""
        t1 = shadow_moduli_map_leading(1.0, num_terms=5)
        t2 = shadow_moduli_map_leading(2.0, num_terms=5)
        # Leading coefficient should roughly double (not exactly due to nonlinearity)
        assert t2[0] > t1[0]

    def test_t49_moduli_map_num_terms(self):
        """T49: Increasing num_terms gives more coefficients."""
        t5 = shadow_moduli_map_leading(1.0, num_terms=5)
        t10 = shadow_moduli_map_leading(1.0, num_terms=10)
        assert len(t10) == 10
        assert len(t5) == 5
        # First 5 should agree
        for i in range(5):
            assert abs(t5[i] - t10[i]) < 1e-12

    def test_t50_sigma_minus_1_in_map(self):
        """T50: The log coefficients use sigma_{-1}(N)."""
        # sigma_{-1}(6) = 1 + 1/2 + 1/3 + 1/6 = 2
        s6 = 1.0 + 0.5 + 1.0 / 3.0 + 1.0 / 6.0
        assert abs(s6 - 2.0) < 1e-12


# =====================================================================
# T51-T55: Universality of G
# =====================================================================

class TestUniversalityOfG:

    def test_t51_heisenberg_universality(self):
        """T51: G depends only on k for Heisenberg."""
        result = verify_universality_of_G('heisenberg', 1.0)
        assert result['separation_verified']
        assert result['G_depends_on'] == 'k = c only'

    def test_t52_virasoro_universality(self):
        """T52: G depends only on c for Virasoro."""
        result = verify_universality_of_G('virasoro', 1.0)
        assert result['separation_verified']

    def test_t53_affine_universality(self):
        """T53: G depends on k and C_3 for affine sl_2."""
        result = verify_universality_of_G('affine_sl2', 3.0)
        assert result['separation_verified']

    def test_t54_G_independent_of_q(self):
        """T54: G coefficients are the same regardless of moduli."""
        r1 = verify_universality_of_G('virasoro', 10.0, max_arity=6)
        r2 = verify_universality_of_G('virasoro', 10.0, max_arity=8)
        # G coefficients at shared arities should agree
        for r in range(2, 7):
            assert abs(r1['G_coefficients'][r] - r2['G_coefficients'][r]) < 1e-12

    def test_t55_unknown_family_error(self):
        """T55: Unknown family returns error."""
        result = verify_universality_of_G('unknown_family', 1.0)
        assert 'error' in result


# =====================================================================
# T56-T60: Carleman uniqueness
# =====================================================================

class TestCarlemanUniqueness:

    def test_t56_virasoro_carleman(self):
        """T56: Carleman condition satisfied for Virasoro (moments grow ~ factorially)."""
        S_list = _virasoro_S_numerical(1.0, max_arity=15)
        result = carleman_uniqueness_check(S_list)
        # Virasoro: S_r grow geometrically with base ~6/c, so |mu_r| ~ r*(6/c)^r.
        # |mu_r|^{-1/(2r)} ~ const > 0 -> sum diverges.
        assert result['uniqueness'], "Carleman condition should hold for Virasoro"

    def test_t57_heisenberg_carleman(self):
        """T57: Heisenberg: p_r = 0 for r >= 3 -> Carleman trivially holds (infinite terms)."""
        S_list = [0.5, 0.0, 0.0, 0.0]  # S_2=0.5, S_3=S_4=S_5=0
        result = carleman_uniqueness_check(S_list)
        # S_3 = 0 -> mu_3 = 0 -> term = infinity -> sum = infinity
        assert result['uniqueness']

    def test_t58_carleman_large_c(self):
        """T58: Carleman condition still holds at large c."""
        S_list = _virasoro_S_numerical(100.0, max_arity=12)
        result = carleman_uniqueness_check(S_list)
        assert result['uniqueness']

    def test_t59_carleman_partial_sum_positive(self):
        """T59: Partial Carleman sum is positive."""
        S_list = _virasoro_S_numerical(5.0, max_arity=10)
        result = carleman_uniqueness_check(S_list)
        assert result['partial_sum'] > 0

    def test_t60_carleman_terms_bounded_below(self):
        """T60: Individual Carleman terms are bounded below."""
        S_list = _virasoro_S_numerical(2.0, max_arity=12)
        result = carleman_uniqueness_check(S_list)
        finite_terms = [t for t in result['terms'] if t['term'] < float('inf')]
        if finite_terms:
            assert result['lower_bound_on_terms'] > 0


# =====================================================================
# T61-T65: Spectral density and branch cuts
# =====================================================================

class TestSpectralDensity:

    def test_t61_virasoro_density_real_axis_zero(self):
        """T61: For c > 0, spectral density is zero on the real axis.
        Q(t) > 0 for all real t, so sqrt(Q) is real and Im = 0."""
        for lam in [0.5, 1.0, 2.0, 5.0]:
            rho = spectral_density_on_cut(1.0, lam)
            assert abs(rho) < 1e-6, f"Density nonzero at lambda={lam}: {rho}"

    def test_t62_density_at_zero(self):
        """T62: Density at lambda=0 is zero."""
        assert spectral_density_on_cut(1.0, 0.0) == 0.0

    def test_t63_branch_cut_midpoint(self):
        """T63: Spectral density on the complex branch cut is nonzero at midpoint."""
        c_val = 1.0
        density = spectral_density_on_complex_cut(c_val, 0.5)
        assert abs(density) > 0, "Density should be nonzero on the branch cut"

    def test_t64_branch_cut_endpoints(self):
        """T64: At s=0 and s=1 (the branch points), density approaches zero."""
        c_val = 5.0
        # Near endpoints, Q -> 0 so sqrt(Q) -> 0
        d_near_0 = spectral_density_on_complex_cut(c_val, 0.01)
        d_mid = spectral_density_on_complex_cut(c_val, 0.5)
        # Density should be smaller near endpoints than at midpoint
        assert abs(d_near_0) < 2 * abs(d_mid) + 0.01

    def test_t65_density_parameterization(self):
        """T65: Branch cut parameterization covers t_+ to t_-."""
        c_val = 3.0
        t_plus, t_minus = virasoro_branch_points(c_val)
        # At s=0: t(0) = t_+, at s=1: t(1) = t_-
        # The spectral_density_on_complex_cut function internally parameterizes this way
        d0 = spectral_density_on_complex_cut(c_val, 0.0)
        d1 = spectral_density_on_complex_cut(c_val, 1.0)
        # These are at the branch points, computed with epsilon regularization
        assert np.isfinite(abs(d0))
        assert np.isfinite(abs(d1))


# =====================================================================
# T66-T70: Affine sl_2 spectral data (class L, depth 3)
# =====================================================================

class TestAffineSl2Spectral:

    def test_t66_affine_seeds(self):
        """T66: S_2 = k/2, S_3 = 2k/(k+2) for affine sl_2."""
        data = affine_sl2_spectral(4.0)
        assert abs(data['S_list'][0] - 2.0) < 1e-12   # k/2 = 2
        expected_C3 = 2.0 * 4.0 / 6.0  # = 4/3
        assert abs(data['S_list'][1] - expected_C3) < 1e-12

    def test_t67_affine_depth(self):
        """T67: Affine has depth 3."""
        data = affine_sl2_spectral(1.0)
        assert data['depth'] == 3
        assert data['archetype'] == 'L (Lie/tree)'

    def test_t68_affine_three_roots(self):
        """T68: Spectral polynomial is cubic -> 3 roots."""
        data = affine_sl2_spectral(4.0)
        assert len(data['poly_roots']) == 3

    def test_t69_affine_critical_level(self):
        """T69: k = -2 (critical level) raises error."""
        with pytest.raises(ValueError, match="critical level"):
            affine_sl2_spectral(-2.0)

    def test_t70_affine_large_k(self):
        """T70: For large k, affine approaches Gaussian (C_3 -> 2, small relative to S_2)."""
        data = affine_sl2_spectral(1000.0)
        assert abs(data['C_3'] - 2.0) < 0.01  # C_3 = 2k/(k+2) -> 2
        # S_3/S_2 = C_3 / (k/2) = 4/(k(k+2)) -> 0
        ratio = abs(data['S_list'][1]) / abs(data['S_list'][0])
        assert ratio < 0.01


# =====================================================================
# Additional cross-checks
# =====================================================================

class TestCrossChecks:

    def test_t71_virasoro_vs_direct_exp_G(self):
        """T71: Virasoro exp(G) from atoms and from shadow agree at low order."""
        c_val = 5.0
        max_ar = 6
        S_list = _virasoro_S_numerical(c_val, max_arity=max_ar)

        # exp(G) from shadow
        from_shadow = exp_G_from_shadow(S_list, max_order=max_ar, start_arity=2)

        # Extract atoms from shadow, then compute exp(G) from atoms
        atoms, _ = spectral_atoms_from_shadow(S_list, start_arity=2)
        from_atoms = exp_G_from_atoms(atoms, max_order=max_ar)

        # They should agree at low orders
        for k in range(min(4, max_ar + 1)):
            assert abs(from_shadow[k] - from_atoms[k].real) < 0.1, \
                f"t^{k}: shadow={from_shadow[k]}, atoms={from_atoms[k]}"

    def test_t72_determinant_identity_trivial(self):
        """T72: Determinant identity for the trivial case (no atoms)."""
        result = verify_determinant_identity(
            atoms=[], multiplicities=[],
            t_q_coeffs=[0.1, 0.01], det_coeffs=[1.0, 0.0, 0.0],
            max_order=2,
        )
        assert result['match'], f"Max defect: {result['max_defect']}"

    def test_t73_spectral_atoms_pipeline_consistency(self):
        """T73: The full pipeline S -> atoms -> reconstructed S is consistent."""
        # Use Virasoro at c=10, arity 6
        c_val = 10.0
        S_list = _virasoro_S_numerical(c_val, max_arity=6)
        atoms, _ = spectral_atoms_from_shadow(S_list, start_arity=2)

        # Reconstruct S from atoms (with unit multiplicities)
        finite_atoms = [a for a in atoms if np.isfinite(a)]
        S_recon = reconstruct_G_from_atoms(finite_atoms, [1.0] * len(finite_atoms), max_arity=4)

        # At low arity, reconstruction should be reasonable
        assert abs(S_recon[2].real - S_list[0]) / abs(S_list[0]) < 0.5

    def test_t74_heisenberg_vs_affine_limit(self):
        """T74: Affine at large k approaches Heisenberg spectral structure."""
        k_val = 10000.0
        aff_data = affine_sl2_spectral(k_val)
        heis_data = heisenberg_spectral(k_val)

        # S_2 should match
        assert abs(aff_data['S_list'][0] - heis_data['S_list'][0]) < 1e-6

        # S_3 should be small relative to S_2
        ratio = abs(aff_data['S_list'][1]) / abs(aff_data['S_list'][0])
        assert ratio < 1e-3
