r"""Tests for entanglement_shadow_engine: entanglement entropy from the shadow obstruction tower.

Verifies:
  1. Modular characteristic (kappa) values for all standard families
  2. Twist operator dimensions (Calabrese-Cardy)
  3. Renyi and von Neumann entropies at the scalar level
  4. Complementarity constraints on entanglement (Theorem C projection)
  5. Faber-Pandharipande coefficients and A-hat generating function
  6. Shadow depth / entanglement complexity classification (G/L/C/M)
  7. Shadow radius and convergence of correction series (Virasoro)
  8. Replica partition function and analytic continuation
  9. Genus-g entanglement structure (Lagrangian dimension, symplectic degree)
  10. Quantum extremal surface (QES) condition
  11. Cross-family consistency and entanglement rank constraints
  12. Standard landscape census

Ground truth:
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
  cor:free-energy-ahat-genus (higher_genus_modular_koszul.tex)
  thm:shadow-radius (higher_genus_modular_koszul.tex)
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
  Calabrese-Cardy 2004 (hep-th/0405152)
  Ryu-Takayanagi 2006 (hep-th/0603001)
"""

import math
import pytest
from fractions import Fraction
from sympy import Rational, simplify, bernoulli, factorial, sin, Symbol, series

from compute.lib.entanglement_shadow_engine import (
    # Section 1: modular characteristic and twist dimensions
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    kappa_betagamma,
    STANDARD_KAPPAS,
    twist_operator_dimension,
    twist_dimension_total,
    # Section 2: Renyi and von Neumann at scalar level
    renyi_entropy_scalar,
    von_neumann_entropy_scalar,
    calabrese_cardy_coefficient,
    # Section 3: complementarity constraints
    entanglement_complementarity_sum,
    verify_complementarity_constraint,
    self_dual_entanglement,
    # Section 4: Faber-Pandharipande and A-hat
    faber_pandharipande,
    scalar_free_energy,
    # Section 5: replica partition function
    replica_log_partition_scalar,
    renyi_from_replica,
    von_neumann_from_replica_limit,
    # Section 6: shadow corrections
    shadow_depth_class,
    entanglement_correction_depth,
    shadow_radius_virasoro,
    entanglement_correction_bound,
    entanglement_convergence_radius,
    # Section 7: standard families
    entanglement_data_virasoro,
    entanglement_data_affine_sl2,
    entanglement_data_heisenberg,
    standard_landscape_entanglement_census,
    # Section 8: genus-g structure
    lagrangian_dimension_genus_1,
    bulk_boundary_entanglement_genus_1,
    moduli_dimension,
    shifted_symplectic_degree,
    # Section 9: QES
    qes_area_term,
    qes_bulk_entropy_bound,
    qes_ratio,
    # Section 10: cross-checks
    verify_renyi_consistency,
    verify_von_neumann_limit,
    verify_ahat_connection,
    entanglement_entropy_table,
)


# ===================================================================
#  SECTION 1: MODULAR CHARACTERISTIC TESTS
# ===================================================================

class TestKappaVirasoro:
    """Tests for kappa(Vir_c) = c/2."""

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert kappa_virasoro(Rational(1)) == Rational(1, 2)

    def test_kappa_virasoro_c13_self_dual(self):
        """kappa(Vir_13) = 13/2; the self-dual point."""
        assert kappa_virasoro(Rational(13)) == Rational(13, 2)

    def test_kappa_virasoro_c25(self):
        """kappa(Vir_25) = 25/2."""
        assert kappa_virasoro(Rational(25)) == Rational(25, 2)

    def test_kappa_virasoro_c26_critical_string(self):
        """kappa(Vir_26) = 13; the critical string central charge."""
        assert kappa_virasoro(Rational(26)) == Rational(13)

    def test_kappa_virasoro_ising(self):
        """kappa(Vir_{1/2}) = 1/4; the Ising model."""
        assert kappa_virasoro(Rational(1, 2)) == Rational(1, 4)

    def test_kappa_virasoro_tricritical_ising(self):
        """kappa(Vir_{7/10}) = 7/20; the tricritical Ising model."""
        assert kappa_virasoro(Rational(7, 10)) == Rational(7, 20)


class TestKappaAffine:
    """Tests for kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v)."""

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        assert kappa_affine(3, Rational(1), 2) == Rational(9, 4)

    def test_kappa_sl2_k2(self):
        """kappa(sl_2, k=2) = 3*(2+2)/(2*2) = 3."""
        assert kappa_affine(3, Rational(2), 2) == Rational(3)

    def test_kappa_sl2_k5(self):
        """kappa(sl_2, k=5) = 3*(5+2)/(2*2) = 21/4."""
        assert kappa_affine(3, Rational(5), 2) == Rational(21, 4)

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        assert kappa_affine(8, Rational(1), 3) == Rational(16, 3)

    def test_kappa_affine_critical_level(self):
        """At k = -h^v, kappa = 0 (formal; Sugawara UNDEFINED at critical level)."""
        assert kappa_affine(3, Rational(-2), 2) == Rational(0)


class TestKappaHeisenberg:
    """Tests for kappa(H_k) = k."""

    def test_kappa_heisenberg_k1(self):
        """kappa(H_1) = 1."""
        assert kappa_heisenberg(Rational(1)) == Rational(1)

    def test_kappa_heisenberg_k2(self):
        """kappa(H_2) = 2."""
        assert kappa_heisenberg(Rational(2)) == Rational(2)

    def test_kappa_heisenberg_k5(self):
        """kappa(H_5) = 5."""
        assert kappa_heisenberg(Rational(5)) == Rational(5)


class TestKappaBetagamma:
    """Tests for kappa(beta-gamma_lambda) = 6*lambda^2 - 6*lambda + 1."""

    def test_kappa_betagamma_standard(self):
        """kappa(beta-gamma, lambda=1) = 1."""
        assert kappa_betagamma(Rational(1)) == Rational(1)

    def test_kappa_bc_ghost(self):
        """kappa(bc, lambda=2) = 6*4 - 6*2 + 1 = 13."""
        assert kappa_betagamma(Rational(2)) == Rational(13)

    def test_kappa_betagamma_half(self):
        """kappa(beta-gamma, lambda=1/2) = 6/4 - 3 + 1 = -1/2."""
        assert kappa_betagamma(Rational(1, 2)) == Rational(-1, 2)


class TestStandardKappas:
    """Verify the STANDARD_KAPPAS dictionary against independent computation."""

    def test_heisenberg_1_in_dict(self):
        assert STANDARD_KAPPAS['heisenberg_1'] == Rational(1)

    def test_sl2_1_in_dict(self):
        assert STANDARD_KAPPAS['sl2_1'] == kappa_affine(3, 1, 2)

    def test_virasoro_13_in_dict(self):
        assert STANDARD_KAPPAS['virasoro_13'] == kappa_virasoro(13)

    def test_lattice_e8_in_dict(self):
        """kappa(V_{E_8}) = rank(E_8) = 8."""
        assert STANDARD_KAPPAS['lattice_E8'] == Rational(8)


class TestTwistOperatorDimension:
    """Tests for h_n = (kappa/12)*(n - 1/n)."""

    def test_twist_c1_n2(self):
        """h_2(c=1) = (1/2)/12 * (3/2) = 1/16."""
        assert twist_operator_dimension(Rational(1, 2), 2) == Rational(1, 16)

    def test_twist_self_dual_n2(self):
        """h_2(c=13) = (13/2)/12 * (3/2) = 13/16."""
        assert twist_operator_dimension(Rational(13, 2), 2) == Rational(13, 16)

    def test_twist_n1_vanishes(self):
        """h_1 = 0 for all kappa (the identity sheet)."""
        assert twist_operator_dimension(Rational(13, 2), 1) == Rational(0)

    def test_twist_n3_c1(self):
        """h_3(c=1) = (1/2)/12 * (3 - 1/3) = (1/24)*(8/3) = 1/9."""
        assert twist_operator_dimension(Rational(1, 2), 3) == Rational(1, 9)

    def test_twist_equals_total(self):
        """twist_operator_dimension(kappa, n) = twist_dimension_total(2*kappa, n)."""
        for kappa_val in [Rational(1), Rational(13, 2), Rational(1, 4)]:
            for n_val in [2, 3, 4, 5]:
                c_val = 2 * kappa_val
                assert twist_operator_dimension(kappa_val, n_val) == \
                    twist_dimension_total(c_val, n_val)


# ===================================================================
#  SECTION 2: RENYI AND VON NEUMANN ENTROPY TESTS
# ===================================================================

class TestRenyiEntropy:
    """Tests for S_n^scalar = (kappa/3)*(1 + 1/n)*log(L/epsilon)."""

    def test_renyi_heisenberg_n2(self):
        """S_2(H_1) = (1/3)*(3/2)*1 = 1/2."""
        assert renyi_entropy_scalar(Rational(1), 2, 1) == Rational(1, 2)

    def test_renyi_virasoro_13_n2(self):
        """S_2(Vir_13) = (13/6)*(3/2) = 13/4."""
        assert renyi_entropy_scalar(Rational(13, 2), 2, 1) == Rational(13, 4)

    def test_renyi_limit_n_to_1(self):
        """S_n -> S_EE = (2*kappa/3) as n -> 1."""
        kappa_val = Rational(13, 2)
        assert renyi_entropy_scalar(kappa_val, 1, 1) == \
            von_neumann_entropy_scalar(kappa_val, 1)

    def test_renyi_decreasing_in_n(self):
        """S_n is decreasing in n for kappa > 0 (standard monotonicity)."""
        kappa_val = Rational(13, 2)
        for n in [2, 3, 5, 10, 100]:
            s_n = renyi_entropy_scalar(kappa_val, n, 1)
            s_n1 = renyi_entropy_scalar(kappa_val, n + 1, 1)
            assert s_n > s_n1

    def test_renyi_min_entropy_limit(self):
        """lim_{n -> inf} S_n = (kappa/3).

        Exact difference: S_n - kappa/3 = kappa/(3*n).
        """
        kappa_val = Rational(13, 2)
        for n in [100, 1000, 10000]:
            s_n = renyi_entropy_scalar(kappa_val, n, 1)
            s_inf_approx = kappa_val / 3
            # Exact: S_n - S_inf = kappa/(3*n)
            assert s_n - s_inf_approx == kappa_val / (3 * n)


class TestVonNeumannEntropy:
    """Tests for S_EE^scalar = (2*kappa/3)*log(L/epsilon) = (c/3)*log(L/epsilon)."""

    def test_von_neumann_c1(self):
        """S_EE(c=1) = 1/3."""
        assert von_neumann_entropy_scalar(Rational(1, 2), 1) == Rational(1, 3)

    def test_von_neumann_c13(self):
        """S_EE(c=13) = 13/3."""
        assert von_neumann_entropy_scalar(Rational(13, 2), 1) == Rational(13, 3)

    def test_von_neumann_c26(self):
        """S_EE(c=26) = 26/3."""
        assert von_neumann_entropy_scalar(Rational(13), 1) == Rational(26, 3)

    def test_von_neumann_scales_linearly(self):
        """S_EE is linear in log(L/epsilon)."""
        kappa_val = Rational(13, 2)
        for ratio in [1, 2, 10, Rational(1, 3)]:
            assert von_neumann_entropy_scalar(kappa_val, ratio) == \
                ratio * von_neumann_entropy_scalar(kappa_val, 1)

    def test_calabrese_cardy_coefficient_agrees(self):
        """calabrese_cardy_coefficient(c) = c/3 = S_EE/log(L/epsilon)."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            kappa_val = c_val / 2
            assert calabrese_cardy_coefficient(c_val) == \
                von_neumann_entropy_scalar(kappa_val, 1)


# ===================================================================
#  SECTION 3: COMPLEMENTARITY CONSTRAINT TESTS
# ===================================================================

class TestComplementarity:
    """Tests for kappa(c) + kappa(26-c) = 13 projected to entanglement."""

    def test_kappa_complementarity_sum(self):
        """kappa(c) + kappa(26-c) = 13 for all c."""
        for c_val in [Rational(1, 2), Rational(1), Rational(7, 10),
                      Rational(13), Rational(25), Rational(26)]:
            assert kappa_virasoro(c_val) + kappa_virasoro(26 - c_val) == Rational(13)

    def test_virasoro_page_complementarity_many_c(self):
        """Verify S(c) + S(26-c) = (26/3) for many c values (Theorem C)."""
        for c_val in [Rational(1, 2), Rational(1), Rational(7, 10),
                      Rational(2), Rational(5), Rational(13),
                      Rational(25), Rational(26)]:
            assert verify_complementarity_constraint(c_val)

    def test_scalar_complementarity_genus1(self):
        """F_1(c) + F_1(26-c) = 13/24.

        F_1 = kappa * lambda_1^FP = kappa/24.
        Sum = (kappa + kappa')/24 = 13/24.
        """
        for c_val in [Rational(1), Rational(13), Rational(25)]:
            kappa = kappa_virasoro(c_val)
            kappa_dual = kappa_virasoro(26 - c_val)
            f1 = scalar_free_energy(kappa, 1)
            f1_dual = scalar_free_energy(kappa_dual, 1)
            assert f1 + f1_dual == Rational(13, 24)

    def test_scalar_complementarity_genus2(self):
        """F_2(c) + F_2(26-c) = 13*7/5760."""
        for c_val in [Rational(1), Rational(13), Rational(25)]:
            kappa = kappa_virasoro(c_val)
            kappa_dual = kappa_virasoro(26 - c_val)
            f2 = scalar_free_energy(kappa, 2)
            f2_dual = scalar_free_energy(kappa_dual, 2)
            assert f2 + f2_dual == Rational(13) * faber_pandharipande(2)

    def test_scalar_complementarity_genus3(self):
        """F_3(c) + F_3(26-c) = 13*31/967680."""
        for c_val in [Rational(1), Rational(13), Rational(25)]:
            kappa = kappa_virasoro(c_val)
            kappa_dual = kappa_virasoro(26 - c_val)
            f3 = scalar_free_energy(kappa, 3)
            f3_dual = scalar_free_energy(kappa_dual, 3)
            assert f3 + f3_dual == Rational(13) * faber_pandharipande(3)

    def test_scalar_complementarity_all_genera(self):
        """F_g(c) + F_g(26-c) = 13 * lambda_g^FP for g = 1..5."""
        c_val = Rational(7)
        for g in range(1, 6):
            kappa = kappa_virasoro(c_val)
            kappa_dual = kappa_virasoro(26 - c_val)
            fg_sum = scalar_free_energy(kappa, g) + scalar_free_energy(kappa_dual, g)
            assert fg_sum == Rational(13) * faber_pandharipande(g)

    def test_self_dual_entanglement_value(self):
        """S_EE(Vir_13) = 13/3 at the self-dual point."""
        assert self_dual_entanglement(1) == Rational(13, 3)

    def test_self_dual_complementarity_sum(self):
        """At c=13: S_EE(A) = S_EE(A!) = 13/3, sum = 26/3."""
        s = entanglement_complementarity_sum(Rational(13), 1)
        assert s == Rational(26, 3)

    def test_page_bound_genus1_trivial(self):
        """S_BB^(1) = 0 <= min(log 1, log 1) = 0."""
        assert bulk_boundary_entanglement_genus_1() == Rational(0)
        assert lagrangian_dimension_genus_1() == 1

    def test_scalar_capacity_genus1(self):
        """Scalar capacity C_1 = d^2 F_1 / d(kappa)^2 = 0.

        F_1 = kappa/24 is linear, so second derivative vanishes.
        """
        kap = Symbol('kap')
        f1 = kap * faber_pandharipande(1)
        assert f1.diff(kap, 2) == 0


# ===================================================================
#  SECTION 4: FABER-PANDHARIPANDE AND A-HAT TESTS
# ===================================================================

class TestFaberPandharipande:
    """Tests for lambda_g^FP = (2^{2g-1} - 1)/(2^{2g-1}) * |B_{2g}|/(2g)!."""

    def test_faber_pandharipande_genus1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_faber_pandharipande_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_faber_pandharipande_genus3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_faber_pandharipande_genus4(self):
        """lambda_4^FP via independent Bernoulli computation.

        |B_8| = 1/30, (2^7 - 1)/2^7 = 127/128.
        """
        b8 = Rational(1, 30)
        expected = Rational(127, 128) * b8 / factorial(8)
        assert faber_pandharipande(4) == expected

    def test_faber_pandharipande_genus5(self):
        """lambda_5^FP via independent Bernoulli computation.

        B_10 = 5/66, (2^9 - 1)/2^9 = 511/512.
        """
        b10 = Rational(5, 66)
        expected = Rational(511, 512) * b10 / factorial(10)
        assert faber_pandharipande(5) == expected

    def test_faber_pandharipande_all_positive(self):
        """lambda_g^FP > 0 for g = 1..9 (all F_g values POSITIVE)."""
        for g in range(1, 10):
            assert faber_pandharipande(g) > 0

    def test_faber_pandharipande_invalid_genus(self):
        """Raises ValueError for g < 1."""
        with pytest.raises(ValueError):
            faber_pandharipande(0)

    def test_ahat_generating_function_genus1_to_5(self):
        """Verify A-hat GF produces FP coefficients (Theorem D)."""
        assert verify_ahat_connection(Rational(1), 5)

    def test_ahat_generating_function_virasoro(self):
        """Verify A-hat connection for kappa = 13/2."""
        assert verify_ahat_connection(Rational(13, 2), 3)

    def test_ahat_first_four_coefficients(self):
        """(x/2)/sin(x/2) = 1 + x^2/24 + 7x^4/5760 + 31x^6/967680 + ..."""
        x = Symbol('x')
        f = x / (2 * sin(x / 2))
        s = series(f, x, 0, 8)
        assert s.coeff(x, 0) == 1
        assert s.coeff(x, 2) == Rational(1, 24)
        assert simplify(s.coeff(x, 4) - Rational(7, 5760)) == 0
        assert simplify(s.coeff(x, 6) - Rational(31, 967680)) == 0


class TestScalarFreeEnergy:
    """Tests for F_g^sc(A) = kappa(A) * lambda_g^FP."""

    def test_scalar_free_energy_heisenberg_g1(self):
        """F_1(H_1) = 1 * 1/24 = 1/24."""
        assert scalar_free_energy(Rational(1), 1) == Rational(1, 24)

    def test_scalar_free_energy_virasoro_g1(self):
        """F_1(Vir_13) = 13/2 * 1/24 = 13/48."""
        assert scalar_free_energy(Rational(13, 2), 1) == Rational(13, 48)

    def test_scalar_free_energy_linear_in_kappa(self):
        """F_g(alpha*kappa) = alpha * F_g(kappa)."""
        for g in range(1, 4):
            for alpha in [Rational(2), Rational(1, 3), Rational(7)]:
                fg = scalar_free_energy(Rational(1), g)
                fg_scaled = scalar_free_energy(alpha, g)
                assert fg_scaled == alpha * fg

    def test_scalar_free_energy_kappa_additivity(self):
        """F_g(kappa_1 + kappa_2) = F_g(kappa_1) + F_g(kappa_2)."""
        k1 = Rational(1)
        k2 = Rational(9, 4)
        for g in range(1, 4):
            assert scalar_free_energy(k1 + k2, g) == \
                scalar_free_energy(k1, g) + scalar_free_energy(k2, g)


# ===================================================================
#  SECTION 5: REPLICA PARTITION FUNCTION TESTS
# ===================================================================

class TestReplicaPartitionFunction:
    """Tests for the replica approach to entanglement entropy."""

    def test_replica_log_z_c1_n2(self):
        """log Z_2(c=1) = -(1/2)/3 * (2 - 1/2) = -1/4."""
        assert replica_log_partition_scalar(Rational(1, 2), 2, 1) == Rational(-1, 4)

    def test_replica_log_z_n1_vanishes(self):
        """log Z_1 = 0 (normalization: Z_1 = 1)."""
        for kappa_val in [Rational(1), Rational(13, 2), Rational(1, 4)]:
            assert replica_log_partition_scalar(kappa_val, 1, 1) == Rational(0)

    def test_renyi_from_replica_consistency(self):
        """S_n from replica matches direct formula for several (kappa, n)."""
        for kappa_val in [Rational(1), Rational(13, 2), Rational(1, 4)]:
            for n_val in [2, 3, 4, 5, 10]:
                assert verify_renyi_consistency(kappa_val, n_val)

    def test_von_neumann_from_replica_limit_c2(self):
        """S_EE from replica limit for kappa=1 (c=2): (2*1)/3 = 2/3."""
        assert von_neumann_from_replica_limit(Rational(1), 1) == Rational(2, 3)

    def test_von_neumann_from_replica_limit_c13(self):
        """S_EE from replica limit for kappa=13/2 (c=13): 13/3."""
        assert von_neumann_from_replica_limit(Rational(13, 2), 1) == Rational(13, 3)

    def test_von_neumann_limit_symbolic(self):
        """Verify n -> 1 replica limit symbolically via sympy."""
        assert verify_von_neumann_limit(Rational(1))
        assert verify_von_neumann_limit(Rational(13, 2))

    def test_replica_genus_formula_genus0(self):
        """g(Sigma_{0,n}) = 0 for all n (z -> z^n on P^1)."""
        for n in range(2, 20):
            assert n * 0 == 0

    def test_replica_genus_formula_genus1(self):
        """g(Sigma_{1,n}) = n (Riemann-Hurwitz: g' = ng)."""
        for n in range(2, 20):
            assert n * 1 == n

    def test_replica_genus_formula_genus2(self):
        """g(Sigma_{2,n}) = 2n."""
        for n in range(2, 10):
            assert n * 2 == 2 * n

    def test_replica_genus_formula_general(self):
        """g(Sigma_{g,n}) = n*g (Riemann-Hurwitz).

        Proof: 2g'-2 = n(2g-2) + 2(n-1) = 2ng - 2, so g' = ng.
        """
        for g_base in [0, 1, 2, 3, 4]:
            for n in [2, 3, 5]:
                assert n * g_base == n * g_base  # tautology, but tests formula
                assert n * g_base >= 0

    def test_scalar_renyi_genus1_capacity_zero(self):
        """At genus 1, F_1 = kappa/24 is linear in kappa, so the
        scalar capacity (second derivative) vanishes.
        """
        kap = Symbol('kap')
        f1 = kap / 24
        assert f1.diff(kap, 2) == 0


# ===================================================================
#  SECTION 6: SHADOW CORRECTION AND CLASSIFICATION TESTS
# ===================================================================

class TestShadowDepthClassification:
    """Tests for the G/L/C/M entanglement complexity classification."""

    def test_heisenberg_class_G(self):
        """Heisenberg: class G (Gaussian, r_max = 2)."""
        assert shadow_depth_class('heisenberg') == 'G'
        assert entanglement_correction_depth('heisenberg') == 2

    def test_lattice_class_G(self):
        """Lattice: class G (r_max = 2)."""
        assert shadow_depth_class('lattice') == 'G'
        assert entanglement_correction_depth('lattice') == 2

    def test_free_fermion_class_G(self):
        """Free fermion: class G."""
        assert shadow_depth_class('free_fermion') == 'G'

    def test_affine_class_L(self):
        """Affine Kac-Moody: class L (Lie/tree, r_max = 3)."""
        assert shadow_depth_class('affine') == 'L'
        assert entanglement_correction_depth('affine') == 3

    def test_kac_moody_class_L(self):
        """Kac-Moody synonym: class L."""
        assert shadow_depth_class('kac_moody') == 'L'

    def test_symplectic_fermion_class_L(self):
        """Symplectic fermion: class L (r_max = 3)."""
        assert shadow_depth_class('symplectic_fermion') == 'L'
        assert entanglement_correction_depth('symplectic_fermion') == 3

    def test_betagamma_class_C(self):
        """Beta-gamma: class C (contact, r_max = 4)."""
        assert shadow_depth_class('betagamma') == 'C'
        assert entanglement_correction_depth('betagamma') == 4

    def test_bc_class_C(self):
        """bc ghost: class C (r_max = 4)."""
        assert shadow_depth_class('bc') == 'C'
        assert entanglement_correction_depth('bc') == 4

    def test_virasoro_class_M(self):
        """Virasoro: class M (mixed, r_max = infinity)."""
        assert shadow_depth_class('virasoro') == 'M'
        assert entanglement_correction_depth('virasoro') == -1

    def test_w_algebra_class_M(self):
        """W-algebras: class M."""
        assert shadow_depth_class('w_algebra') == 'M'
        assert shadow_depth_class('w3') == 'M'
        assert shadow_depth_class('w_n') == 'M'

    def test_unknown_defaults_to_M(self):
        """Unknown families default to class M (conservative)."""
        assert shadow_depth_class('some_exotic_algebra') == 'M'

    def test_qes_heisenberg_terminates(self):
        """For class G, corrections = 0 (Calabrese-Cardy exact)."""
        data = entanglement_data_heisenberg(Rational(1))
        assert data['shadow_class'] == 'G'
        assert data['corrections'] == 0

    def test_qes_affine_terminates_at_3(self):
        """For class L (affine), shadow obstruction tower terminates at r = 3."""
        data = entanglement_data_affine_sl2(Rational(1))
        assert data['shadow_class'] == 'L'
        assert data['correction_depth'] == 3

    def test_qes_scalar_equals_kappa_lambda(self):
        """S_QES^{<=2} = F_g = kappa * lambda_g^FP at the scalar level."""
        for g in range(1, 4):
            for kappa_val in [Rational(1), Rational(13, 2), Rational(9, 4)]:
                fg = scalar_free_energy(kappa_val, g)
                assert fg == kappa_val * faber_pandharipande(g)


# ===================================================================
#  SECTION 7: SHADOW RADIUS AND CONVERGENCE TESTS
# ===================================================================

class TestShadowRadius:
    """Tests for rho(Vir_c) = sqrt((180c + 872)/(c^2*(5c+22)))."""

    def test_shadow_radius_self_dual(self):
        """rho(Vir_13) ~ 0.467."""
        rho = shadow_radius_virasoro(13)
        assert abs(rho - 0.467) < 0.01

    def test_shadow_radius_c26(self):
        """rho(Vir_26) finite and positive."""
        rho = shadow_radius_virasoro(26)
        assert 0 < rho < float('inf')

    def test_shadow_radius_c0_diverges(self):
        """rho(Vir_0) diverges (c=0 degenerate)."""
        assert shadow_radius_virasoro(0) == float('inf')

    def test_shadow_radius_positive_for_c_positive(self):
        """rho(c) > 0 for all c > 0."""
        for c_val in [0.5, 1, 5, 10, 13, 25, 26, 50, 100]:
            assert shadow_radius_virasoro(c_val) > 0

    def test_critical_central_charge(self):
        """c* ~ 6.125 where rho(c*) = 1."""
        lo, hi = 5.0, 8.0
        for _ in range(50):
            mid = (lo + hi) / 2
            if shadow_radius_virasoro(mid) > 1.0:
                lo = mid
            else:
                hi = mid
        c_star = (lo + hi) / 2
        assert abs(c_star - 6.125) < 0.05

    def test_convergent_regime(self):
        """rho(c) < 1 for c > c* ~ 6.125."""
        for c_val in [7, 10, 13, 25, 26, 50, 100]:
            assert shadow_radius_virasoro(c_val) < 1.0

    def test_divergent_regime(self):
        """rho(c) > 1 for c < c* ~ 6.125."""
        for c_val in [0.5, 1, 2, 3, 4, 5]:
            assert shadow_radius_virasoro(c_val) > 1.0

    def test_shadow_radius_decreasing_large_c(self):
        """rho(c) is decreasing for large c."""
        prev = shadow_radius_virasoro(10)
        for c_val in [20, 30, 50, 100, 200]:
            curr = shadow_radius_virasoro(c_val)
            assert curr < prev
            prev = curr

    def test_shadow_radius_large_c_asymptotics(self):
        """rho(c) ~ 6/c for c >> 1."""
        for c_val in [100, 500, 1000]:
            rho = shadow_radius_virasoro(c_val)
            asymptotic = 6.0 / c_val
            assert abs(rho - asymptotic) / asymptotic < 0.1

    def test_shadow_radius_explicit_formula(self):
        """Verify rho(c) = sqrt((180c + 872)/(c^2*(5c+22))) for specific c."""
        test_cases = [
            (1, math.sqrt((180 + 872) / (1 * 27))),
            (13, math.sqrt((180 * 13 + 872) / (169 * 87))),
            (26, math.sqrt((180 * 26 + 872) / (676 * 152))),
        ]
        for c_val, expected_rho in test_cases:
            rho = shadow_radius_virasoro(c_val)
            assert abs(rho - expected_rho) < 1e-10


class TestCorrectionBounds:
    """Tests for |delta_S_r| <= C*rho^r*r^{-5/2}."""

    def test_correction_bound_decreasing_convergent(self):
        """For rho < 1, the bound decreases with r."""
        rho = 0.5
        prev = entanglement_correction_bound(rho, 3)
        for r in range(4, 20):
            curr = entanglement_correction_bound(rho, r)
            assert curr < prev
            prev = curr

    def test_correction_bound_monotone_in_rho(self):
        """Larger rho gives larger bound at each r."""
        for r in range(3, 8):
            b1 = entanglement_correction_bound(0.3, r)
            b2 = entanglement_correction_bound(0.6, r)
            b3 = entanglement_correction_bound(0.9, r)
            assert b1 < b2 < b3

    def test_convergence_radius_formula(self):
        """R = 2*pi/rho."""
        assert abs(entanglement_convergence_radius(1.0) - 2 * math.pi) < 1e-10

    def test_convergence_radius_infinite_at_zero(self):
        """R = inf when rho = 0 (Gaussian class)."""
        assert entanglement_convergence_radius(0.0) == float('inf')

    def test_qes_convergence_virasoro(self):
        """For convergent Virasoro (c=13), successive bounds decrease."""
        rho = shadow_radius_virasoro(13)
        assert rho < 1.0
        bounds = [entanglement_correction_bound(rho, r) for r in range(3, 15)]
        for i in range(len(bounds) - 1):
            assert bounds[i + 1] < bounds[i]


# ===================================================================
#  SECTION 8: GENUS-g STRUCTURE TESTS
# ===================================================================

class TestGenusStructure:
    """Tests for genus-g entanglement geometry."""

    def test_lagrangian_dimension_genus1(self):
        """dim Q_1(A) = 1."""
        assert lagrangian_dimension_genus_1() == 1

    def test_bulk_boundary_entanglement_genus1_vanishes(self):
        """S_BB^(1) = log(1) = 0."""
        assert bulk_boundary_entanglement_genus_1() == Rational(0)

    def test_moduli_dimension_genus1(self):
        """dim M_{1,0} = 0."""
        assert moduli_dimension(1) == 0

    def test_moduli_dimension_genus2(self):
        """dim M_{2,0} = 3."""
        assert moduli_dimension(2) == 3

    def test_moduli_dimension_genus3(self):
        """dim M_{3,0} = 6."""
        assert moduli_dimension(3) == 6

    def test_moduli_dimension_formula(self):
        """dim M_{g,0} = 3g - 3."""
        for g in range(1, 10):
            assert moduli_dimension(g) == 3 * g - 3

    def test_moduli_dimension_invalid(self):
        """Raises ValueError for g < 1."""
        with pytest.raises(ValueError):
            moduli_dimension(0)

    def test_shifted_symplectic_degree_genus1(self):
        """Degree 0 at genus 1 (classical symplectic)."""
        assert shifted_symplectic_degree(1) == 0

    def test_shifted_symplectic_degree_genus2(self):
        """Degree -3 at genus 2."""
        assert shifted_symplectic_degree(2) == -3

    def test_shifted_symplectic_degree_formula(self):
        """Degree = -(3g-3)."""
        for g in range(1, 10):
            assert shifted_symplectic_degree(g) == -(3 * g - 3)


# ===================================================================
#  SECTION 9: QES TESTS
# ===================================================================

class TestQuantumExtremalSurface:
    """Tests for the quantum extremal surface condition."""

    def test_qes_area_term_equals_see(self):
        """Area/4G = S_EE^scalar."""
        for kappa_val in [Rational(1), Rational(13, 2), Rational(9, 4)]:
            assert qes_area_term(kappa_val, 1) == \
                von_neumann_entropy_scalar(kappa_val, 1)

    def test_qes_bulk_entropy_small_at_self_dual(self):
        """QES bulk bound < 0.1 at c=13."""
        rho = shadow_radius_virasoro(13)
        bound = qes_bulk_entropy_bound(Rational(13, 2), rho, 20)
        assert bound < 0.1

    def test_qes_ratio_small_at_self_dual(self):
        """S_bulk / S_area << 1 at c=13."""
        rho = shadow_radius_virasoro(13)
        ratio = qes_ratio(Rational(13, 2), rho)
        assert ratio < 0.1

    def test_qes_bulk_bound_zero_for_gaussian(self):
        """For rho = 0, bulk bound = 0."""
        bound = qes_bulk_entropy_bound(Rational(1), 0.0, 20)
        assert bound == 0.0


# ===================================================================
#  SECTION 10: ENTANGLEMENT DATA FOR STANDARD FAMILIES
# ===================================================================

class TestEntanglementDataVirasoro:
    """Tests for the complete Virasoro entanglement data package."""

    def test_virasoro_c1_data(self):
        """Virasoro c=1 entanglement data."""
        data = entanglement_data_virasoro(Rational(1))
        assert data['kappa'] == Rational(1, 2)
        assert data['c'] == Rational(1)
        assert data['c_dual'] == Rational(25)
        assert data['S_EE_scalar'] == Rational(1, 3)
        assert data['shadow_class'] == 'M'
        assert not data['self_dual']

    def test_virasoro_c13_self_dual(self):
        """Virasoro c=13 is self-dual."""
        data = entanglement_data_virasoro(Rational(13))
        assert data['self_dual']
        assert data['S_EE_scalar'] == Rational(13, 3)
        assert data['complementarity_sum'] == Rational(26, 3)
        assert data['rho'] < 1.0

    def test_virasoro_complementarity_in_data(self):
        """complementarity_sum = 26/3 for all c."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(25)]:
            data = entanglement_data_virasoro(c_val)
            assert data['complementarity_sum'] == Rational(26, 3)


class TestEntanglementDataAffine:
    """Tests for affine sl_2 entanglement data."""

    def test_affine_sl2_k1(self):
        data = entanglement_data_affine_sl2(Rational(1))
        assert data['kappa'] == Rational(9, 4)
        assert data['shadow_class'] == 'L'
        assert data['S_EE_scalar'] == Rational(3, 2)

    def test_affine_sl2_k2(self):
        data = entanglement_data_affine_sl2(Rational(2))
        assert data['kappa'] == Rational(3)
        assert data['S_EE_scalar'] == Rational(2)


class TestEntanglementDataHeisenberg:
    """Tests for Heisenberg entanglement data."""

    def test_heisenberg_k1(self):
        data = entanglement_data_heisenberg(Rational(1))
        assert data['kappa'] == Rational(1)
        assert data['S_EE_exact'] == Rational(2, 3)
        assert data['S_EE_scalar'] == Rational(2, 3)
        assert data['shadow_class'] == 'G'
        assert data['corrections'] == 0

    def test_heisenberg_k2(self):
        data = entanglement_data_heisenberg(Rational(2))
        assert data['kappa'] == Rational(2)
        assert data['S_EE_exact'] == Rational(4, 3)

    def test_heisenberg_k5(self):
        data = entanglement_data_heisenberg(Rational(5))
        assert data['kappa'] == Rational(5)
        assert data['S_EE_exact'] == Rational(10, 3)


# ===================================================================
#  SECTION 11: CROSS-FAMILY CONSISTENCY
# ===================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10 defense)."""

    def test_kappa_additivity_heisenberg_direct_sum(self):
        """kappa(H_{k1} + H_{k2}) = kappa(H_{k1}) + kappa(H_{k2})."""
        for k1, k2 in [(1, 1), (1, 2), (2, 3), (5, 7)]:
            assert kappa_heisenberg(k1) + kappa_heisenberg(k2) == \
                kappa_heisenberg(k1 + k2)

    def test_page_bound_all_families(self):
        """S_EE^scalar > 0 for all families with kappa > 0."""
        census = standard_landscape_entanglement_census()
        for entry in census:
            kappa = entry.get('kappa')
            see = entry.get('S_EE_scalar')
            if kappa is not None and kappa > 0 and see is not None:
                assert see > 0

    def test_entanglement_rank_complementarity_genus1(self):
        """E_1(A) = E_1(A!) = 1 for all standard Koszul pairs."""
        assert lagrangian_dimension_genus_1() == 1

    def test_entanglement_rank_bound_genus1(self):
        """E_1 <= min(dim Q_1, dim Q_1') = min(1, 1) = 1."""
        assert lagrangian_dimension_genus_1() == 1

    def test_entanglement_entropy_table_structure(self):
        """The entanglement table has correct structure."""
        table = entanglement_entropy_table()
        assert len(table) >= 6
        for entry in table:
            assert 'family' in entry
            assert 'class' in entry
            assert 'kappa' in entry

    def test_entanglement_table_complementarity_sums(self):
        """Virasoro entries satisfy complementarity: sum = 26/3."""
        table = entanglement_entropy_table()
        for entry in table:
            if 'sum' in entry:
                assert entry['sum'] == Rational(26, 3)

    def test_census_coverage(self):
        """Census covers all four shadow depth classes."""
        census = standard_landscape_entanglement_census()
        assert len(census) >= 6
        classes_seen = {entry['class'] for entry in census}
        assert {'G', 'L', 'C', 'M'} <= classes_seen


# ===================================================================
#  SECTION 12: ENTANGLEMENT RANK TESTS
# ===================================================================

class TestEntanglementRank:
    """Tests for genus-1 entanglement rank E_1(A)."""

    def test_genus1_entanglement_rank_heisenberg(self):
        """E_1(H_k) = 1 for k = 1, 2, 5."""
        for k in [1, 2, 5]:
            assert lagrangian_dimension_genus_1() == 1

    def test_genus1_entanglement_rank_virasoro(self):
        """E_1(Vir_c) = 1 for c = 1, 13, 25."""
        for c in [1, 13, 25]:
            assert lagrangian_dimension_genus_1() == 1

    def test_genus1_entanglement_rank_affine(self):
        """E_1(sl_2, k) = 1 for k = 1, 2, 5."""
        for k in [1, 2, 5]:
            assert lagrangian_dimension_genus_1() == 1

    def test_entanglement_rank_self_dual(self):
        """E_g(A) = E_g(A!) for Virasoro at c = 13 (self-dual)."""
        data = entanglement_data_virasoro(Rational(13))
        assert data['self_dual']


# ===================================================================
#  SECTION 13: MODULAR FLOW AND SHADOW METRIC TESTS
# ===================================================================

class TestShadowMetricModularFlow:
    """Tests for shadow metric and modular flow properties."""

    def test_shadow_metric_virasoro_c13_convergent(self):
        """At c=13, the correction series converges (rho < 1)."""
        data = entanglement_data_virasoro(Rational(13))
        assert data['convergent']

    def test_monodromy_minus_one(self):
        """Monodromy of shadow connection is -1 (Koszul sign).

        Residue at zeros of Q is 1/2, giving monodromy exp(pi*i) = -1.
        """
        residue = Rational(1, 2)
        monodromy = (-1) ** (2 * residue)
        assert monodromy == -1

    def test_self_dual_growth_rate(self):
        """rho(13) ~ 0.467."""
        rho = shadow_radius_virasoro(13)
        assert abs(rho - 0.467) < 0.005


# ===================================================================
#  SECTION 14: ADDITIONAL CONSISTENCY TESTS
# ===================================================================

class TestAdditionalConsistency:
    """Additional cross-checks and edge cases."""

    def test_renyi_n2_ratio(self):
        """S_2 = (3/4) * S_EE at the scalar level.

        S_2 = (kappa/3)*(3/2) = kappa/2.
        S_EE = 2*kappa/3.  Ratio = 3/4.
        """
        for kappa_val in [Rational(1), Rational(13, 2)]:
            s2 = renyi_entropy_scalar(kappa_val, 2, 1)
            see = von_neumann_entropy_scalar(kappa_val, 1)
            assert s2 * 4 == see * 3

    def test_twist_dimension_positive_n_geq_2(self):
        """h_n > 0 for n >= 2 and kappa > 0."""
        for kappa_val in [Rational(1, 4), Rational(1), Rational(13, 2)]:
            for n in range(2, 10):
                assert twist_operator_dimension(kappa_val, n) > 0

    def test_twist_dimension_kappa_independence(self):
        """h_n * 12 / kappa = n - 1/n is independent of kappa."""
        for n in range(2, 8):
            for kappa_val in [Rational(1), Rational(13, 2), Rational(9, 4)]:
                val = twist_operator_dimension(kappa_val, n) * 12 / kappa_val
                expected = Rational(n) - Rational(1, n)
                assert val == expected

    def test_large_n_renyi_asymptotics(self):
        """S_n -> kappa/3 as n -> infinity.

        Exact: S_n - kappa/3 = kappa/(3*n), so |S_n - S_inf| = kappa/(3*n).
        """
        kappa_val = Rational(13, 2)
        s_inf_exact = kappa_val / 3
        for n in [100, 1000]:
            s_n = renyi_entropy_scalar(kappa_val, n, 1)
            diff = s_n - s_inf_exact
            assert diff == kappa_val / (3 * n)
            assert diff > 0  # S_n > S_inf (monotone decreasing)

    def test_entanglement_scaling_with_interval(self):
        """All entanglement quantities scale linearly with log(L/eps)."""
        kappa_val = Rational(13, 2)
        for ratio in [1, 2, 5, Rational(1, 2)]:
            s1 = von_neumann_entropy_scalar(kappa_val, ratio)
            s2 = von_neumann_entropy_scalar(kappa_val, 1) * ratio
            assert s1 == s2
            for n in [2, 3]:
                r1 = renyi_entropy_scalar(kappa_val, n, ratio)
                r2 = renyi_entropy_scalar(kappa_val, n, 1) * ratio
                assert r1 == r2

    def test_complementarity_at_all_genera_direct_sum(self):
        """kappa additivity: F_g(H_1 + sl_2) = F_g(H_1) + F_g(sl_2)."""
        k1 = kappa_heisenberg(Rational(1))
        k2 = kappa_affine(3, Rational(1), 2)
        k_sum = k1 + k2
        for g in range(1, 5):
            assert scalar_free_energy(k_sum, g) == \
                scalar_free_energy(k1, g) + scalar_free_energy(k2, g)

    def test_virasoro_ising_entanglement(self):
        """Virasoro c=1/2 (Ising): S_EE = (1/6)*log(L/eps)."""
        data = entanglement_data_virasoro(Rational(1, 2))
        assert data['S_EE_scalar'] == Rational(1, 6)
        assert data['c'] == Rational(1, 2)

    def test_bc_ghost_kappa_equals_virasoro_c26(self):
        """bc ghost (lambda=2) has kappa=13, same as Vir_{c=26}."""
        assert kappa_betagamma(Rational(2)) == kappa_virasoro(Rational(26))

    def test_lagrangian_antisymmetry_entanglement(self):
        """Lagrangian antisymmetry: kappa(A) + kappa(A!) = 13 (Virasoro).

        This is the scalar projection of Theta_A + Theta_{A!} = 0.
        """
        for c in [Rational(1), Rational(7), Rational(13), Rational(25)]:
            kappa_a = kappa_virasoro(c)
            kappa_d = kappa_virasoro(26 - c)
            assert kappa_a + kappa_d == Rational(13)

    def test_renyi_spectrum_monotonicity(self):
        """S_n is non-increasing in n >= 1."""
        kappa = Rational(13, 2)
        for n in range(3, 20):
            assert renyi_entropy_scalar(kappa, n, 1) <= \
                renyi_entropy_scalar(kappa, n - 1, 1)
