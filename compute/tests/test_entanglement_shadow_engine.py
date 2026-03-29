r"""Tests for entanglement_shadow_engine.py.

Verification strategy:
  1. Calabrese-Cardy reproduction from modular characteristic
  2. Complementarity constraints on entanglement (Theorem C projection)
  3. Renyi entropy consistency (direct vs replica derivation)
  4. A-hat generating function cross-check
  5. Shadow depth classification for entanglement complexity
  6. Shadow correction bounds and convergence
  7. QES stationarity condition
  8. Standard landscape census
  9. Self-dual point properties
  10. Cross-family additivity
"""

import math
import pytest
from fractions import Fraction
from sympy import Rational, simplify

from compute.lib.entanglement_shadow_engine import (
    # Section 1: modular characteristic
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    kappa_betagamma,
    twist_operator_dimension,
    twist_dimension_total,
    # Section 2: Renyi and von Neumann
    renyi_entropy_scalar,
    von_neumann_entropy_scalar,
    calabrese_cardy_coefficient,
    # Section 3: complementarity
    entanglement_complementarity_sum,
    verify_complementarity_constraint,
    self_dual_entanglement,
    # Section 4: Faber-Pandharipande
    faber_pandharipande,
    scalar_free_energy,
    # Section 5: replica
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
    # Section 8: genus structure
    lagrangian_dimension_genus_1,
    bulk_boundary_entanglement_genus_1,
    moduli_dimension,
    shifted_symplectic_degree,
    # Section 9: QES
    qes_area_term,
    qes_bulk_entropy_bound,
    qes_ratio,
    # Section 10: verification
    verify_renyi_consistency,
    verify_von_neumann_limit,
    verify_ahat_connection,
    entanglement_entropy_table,
)


# ===================================================================
#  1. MODULAR CHARACTERISTIC
# ===================================================================

class TestModularCharacteristic:
    """Verify kappa values for all standard families."""

    def test_kappa_virasoro_basic(self):
        assert kappa_virasoro(Rational(1)) == Rational(1, 2)
        assert kappa_virasoro(Rational(26)) == Rational(13)
        assert kappa_virasoro(Rational(13)) == Rational(13, 2)

    def test_kappa_virasoro_minimal_models(self):
        """Minimal model central charges."""
        assert kappa_virasoro(Rational(1, 2)) == Rational(1, 4)  # Ising
        assert kappa_virasoro(Rational(7, 10)) == Rational(7, 20)  # tri-critical Ising
        assert kappa_virasoro(Rational(4, 5)) == Rational(2, 5)  # 3-state Potts

    def test_kappa_affine_sl2(self):
        assert kappa_affine(3, Rational(1), 2) == Rational(9, 4)
        assert kappa_affine(3, Rational(2), 2) == Rational(3)
        # Critical level k = -h^v = -2
        assert kappa_affine(3, Rational(-2), 2) == Rational(0)

    def test_kappa_heisenberg(self):
        assert kappa_heisenberg(Rational(1)) == Rational(1)
        assert kappa_heisenberg(Rational(2)) == Rational(2)

    def test_kappa_betagamma(self):
        assert kappa_betagamma(Rational(1)) == Rational(1)
        assert kappa_betagamma(Rational(2)) == Rational(13)
        # bc ghost: lambda = 2, kappa = 13

    def test_kappa_duality_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c in [Rational(1, 2), Rational(1), Rational(7, 10),
                  Rational(13), Rational(25), Rational(26)]:
            total = kappa_virasoro(c) + kappa_virasoro(26 - c)
            assert total == Rational(13), f"Failed at c={c}: got {total}"


class TestTwistOperator:
    """Twist operator dimensions from modular characteristic."""

    def test_twist_n2_free_boson(self):
        """h_2 = (kappa/12)(2 - 1/2) = kappa/8 for n=2."""
        assert twist_operator_dimension(Rational(1), 2) == Rational(1, 8)

    def test_twist_n2_virasoro_c1(self):
        """h_2 = (c/24)(2 - 1/2) = c/16 for n=2."""
        assert twist_dimension_total(Rational(1), 2) == Rational(1, 16)

    def test_twist_n2_ising(self):
        """h_2(c=1/2) = 1/32."""
        assert twist_dimension_total(Rational(1, 2), 2) == Rational(1, 32)

    def test_twist_n1_vanishes(self):
        """h_1 = 0 (identity twist)."""
        assert twist_dimension_total(Rational(1), 1) == 0

    def test_twist_large_n(self):
        """h_n ~ (c/24)*n for large n."""
        n = 100
        h_n = twist_dimension_total(Rational(1), n)
        asymptotic = Rational(1, 24) * n
        # h_n = (c/24)(n - 1/n) ~ (c/24)*n for large n
        assert abs(float(h_n - asymptotic)) < 0.001

    def test_twist_kappa_vs_c(self):
        """Consistency: h_n(kappa) = h_n(c=2*kappa)."""
        for kappa in [Rational(1), Rational(13, 2), Rational(1, 4)]:
            c = 2 * kappa
            for n in [2, 3, 4]:
                assert twist_operator_dimension(kappa, n) == twist_dimension_total(c, n)


# ===================================================================
#  2. RENYI AND VON NEUMANN ENTROPIES
# ===================================================================

class TestRenyiEntropy:
    """Renyi entropy at scalar level."""

    def test_renyi_n2(self):
        """S_2 = (3/4) * (c/3) * log(L/eps) for n=2."""
        # S_2 = (kappa/3)(1 + 1/2) = kappa/2
        assert renyi_entropy_scalar(Rational(1), 2, 1) == Rational(1, 2)

    def test_renyi_n1_limit(self):
        """lim_{n->1} S_n = S_EE = (2*kappa/3)."""
        kappa = Rational(13, 2)
        s_ee = von_neumann_entropy_scalar(kappa, 1)
        # S_n at n very close to 1 should approach S_EE
        s_near = renyi_entropy_scalar(kappa, Rational(101, 100), 1)
        assert abs(float(s_near - s_ee)) < 0.1

    def test_renyi_monotone(self):
        """S_n is non-increasing in n (for fixed kappa, log_ratio)."""
        kappa = Rational(1)
        for n1, n2 in [(2, 3), (3, 4), (4, 10)]:
            assert renyi_entropy_scalar(kappa, n1, 1) >= renyi_entropy_scalar(kappa, n2, 1)

    def test_renyi_linearity_in_log_ratio(self):
        """S_n is linear in log(L/epsilon)."""
        kappa = Rational(1)
        s1 = renyi_entropy_scalar(kappa, 2, 1)
        s2 = renyi_entropy_scalar(kappa, 2, 2)
        assert s2 == 2 * s1


class TestVonNeumannEntropy:
    """Von Neumann entanglement entropy (Calabrese-Cardy)."""

    def test_calabrese_cardy_c1(self):
        """S_EE = (1/3) * log(L/eps) for c=1 (free boson)."""
        assert von_neumann_entropy_scalar(Rational(1, 2), 1) == Rational(1, 3)

    def test_calabrese_cardy_c26(self):
        """S_EE = (26/3) * log(L/eps) for c=26 (critical string)."""
        assert von_neumann_entropy_scalar(Rational(13), 1) == Rational(26, 3)

    def test_calabrese_cardy_coefficient(self):
        """Coefficient is c/3."""
        assert calabrese_cardy_coefficient(Rational(1)) == Rational(1, 3)
        assert calabrese_cardy_coefficient(Rational(26)) == Rational(26, 3)

    def test_positivity(self):
        """S_EE > 0 for positive kappa."""
        for kappa in [Rational(1, 4), Rational(1), Rational(13, 2)]:
            assert von_neumann_entropy_scalar(kappa, 1) > 0

    def test_von_neumann_matches_kappa_formula(self):
        """S_EE = (2*kappa/3) = (c/3) for kappa = c/2."""
        for c in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            kappa = kappa_virasoro(c)
            s_ee = von_neumann_entropy_scalar(kappa, 1)
            expected = Rational(c, 3)
            assert s_ee == expected


# ===================================================================
#  3. COMPLEMENTARITY CONSTRAINTS
# ===================================================================

class TestComplementarityEntanglement:
    """Theorem C projection to entanglement entropy."""

    def test_complementarity_sum_generic(self):
        """S_EE(Vir_c) + S_EE(Vir_{26-c}) = (13/3) for all c."""
        for c in [Rational(1, 2), Rational(1), Rational(7, 10),
                  Rational(4, 5), Rational(6), Rational(13),
                  Rational(25), Rational(26)]:
            assert verify_complementarity_constraint(c)

    def test_complementarity_self_dual(self):
        """At c=13: S_EE = S_dual = 13/3."""
        s = self_dual_entanglement(1)
        assert s == Rational(13, 3)
        # Verify: 2 * (13/3) = 26/3 (complementarity sum)
        assert 2 * s == Rational(26, 3)

    def test_complementarity_critical_string(self):
        """At c=26: S_EE(Vir_26) = 26/3, S_EE(Vir_0) = 0.
        Sum = 26/3 + 0 ... wait, c=0 gives kappa=0.
        But Vir_0 has c=0, so S_EE = 0.
        Sum = 26/3 != 13/3.  HOWEVER: kappa(Vir_26) + kappa(Vir_0) = 13 + 0 = 13.
        S_EE sum = 2*13/3 + 2*0/3 = 26/3 != 13/3.

        RESOLUTION: The complementarity constraint is on KAPPA, not directly
        on S_EE.  We have kappa + kappa' = 13 (correct), and
        S_EE + S_EE' = (2/3)(kappa + kappa') = (2/3)*13 = 26/3.

        WAIT: Let me recompute.  kappa(Vir_c) = c/2.
        kappa(Vir_26) = 13.  kappa(Vir_0) = 0.  Sum = 13.
        S_EE(Vir_26) = 2*13/3 = 26/3.  S_EE(Vir_0) = 0.
        S_EE sum = 26/3.  And (2/3)*13 = 26/3.  So sum IS (2*13)/3 = 26/3.

        But the function entanglement_complementarity_sum returns
        (2*kappa/3 + 2*kappa'/3) = (2/3)*(kappa + kappa') = (2/3)*13 = 26/3.

        The expected value in the function is (13/3)*log_ratio.
        That's WRONG if the sum is actually (26/3)*log_ratio.

        Let me check: the function computes
          s_c = (2*kappa_c/3) * log_ratio
          s_dual = (2*kappa_dual/3) * log_ratio
          total = s_c + s_dual = (2/3)*(kappa_c + kappa_dual)*log_ratio
                = (2/3)*13*log_ratio = (26/3)*log_ratio

        But verify_complementarity_constraint compares to (13/3)*log_ratio.
        THAT IS A BUG in the engine.  The correct sum is (26/3)*log_ratio.

        Actually wait: von_neumann_entropy_scalar(kappa, log_ratio) = (2*kappa/3)*log_ratio.
        This uses kappa, not c.  But kappa = c/2.  So S_EE = (2*(c/2)/3) = c/3.
        Sum = c/3 + (26-c)/3 = 26/3.  The expected value should be 26/3, not 13/3.

        This is a bug in the engine!  Let me fix the test to match reality,
        and we'll fix the engine too.
        """
        # The CORRECT complementarity sum for Virasoro is:
        # S_EE(c) + S_EE(26-c) = c/3 + (26-c)/3 = 26/3
        total = entanglement_complementarity_sum(Rational(26), 1)
        assert total == Rational(26, 3)

    def test_complementarity_sum_value(self):
        """The true complementarity sum: S + S' = 26/3 * log(L/eps)."""
        # kappa + kappa' = 13  =>  S + S' = 2*13/3 = 26/3
        for c in [Rational(1), Rational(13), Rational(26)]:
            total = entanglement_complementarity_sum(c, 1)
            assert total == Rational(26, 3)

    def test_self_dual_splits_evenly(self):
        """At c=13: S_EE = S_dual = 13/3 (both kappa = 13/2)."""
        data = entanglement_data_virasoro(Rational(13))
        assert data['S_EE_scalar'] == data['S_EE_dual_scalar']
        # S_EE = (2*kappa/3) = (2*(13/2)/3) = 13/3
        assert data['S_EE_scalar'] == Rational(13, 3)


# ===================================================================
#  4. FABER-PANDHARIPANDE AND A-HAT
# ===================================================================

class TestFaberPandharipande:
    """Faber-Pandharipande coefficients."""

    def test_lambda_1(self):
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_lambda_2(self):
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_lambda_3(self):
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_positivity(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 10):
            assert faber_pandharipande(g) > 0

    def test_scalar_free_energy(self):
        """F_g^sc = kappa * lambda_g^FP."""
        assert scalar_free_energy(Rational(1), 1) == Rational(1, 24)
        assert scalar_free_energy(Rational(13, 2), 1) == Rational(13, 48)

    def test_ahat_connection(self):
        """A-hat generating function reproduces FP coefficients."""
        assert verify_ahat_connection(Rational(1), 5)

    def test_ahat_connection_virasoro(self):
        """A-hat for Virasoro kappa = c/2."""
        assert verify_ahat_connection(Rational(13, 2), 3)


# ===================================================================
#  5. REPLICA TRICK
# ===================================================================

class TestReplicaTrick:
    """Replica partition function and limits."""

    def test_replica_log_partition(self):
        """log Z_n = -(kappa/3)(n - 1/n) * log(L/eps) [non-chiral]."""
        # n=2, kappa=1: -(1/3)(2 - 1/2) = -(1/3)(3/2) = -1/2
        val = replica_log_partition_scalar(Rational(1), 2, 1)
        assert val == Rational(-1, 2)

    def test_replica_n1_vanishes(self):
        """log Z_1 = 0 (normalization)."""
        assert replica_log_partition_scalar(Rational(1), 1, 1) == 0

    def test_renyi_from_replica_consistency(self):
        """Renyi from replica matches direct formula."""
        for kappa in [Rational(1), Rational(13, 2)]:
            for n in [2, 3, 4, 5]:
                assert verify_renyi_consistency(kappa, n)

    def test_von_neumann_from_replica_c1(self):
        """Replica limit gives S_EE = (2*kappa/3) for kappa=1."""
        # kappa = 1 => c = 2 => S_EE = 2/3
        assert von_neumann_from_replica_limit(Rational(1), 1) == Rational(2, 3)

    def test_von_neumann_limit_symbolic(self):
        """Symbolic verification of n -> 1 limit."""
        assert verify_von_neumann_limit(Rational(1))
        assert verify_von_neumann_limit(Rational(13, 2))
        assert verify_von_neumann_limit(Rational(1, 4))


# ===================================================================
#  6. SHADOW DEPTH AND CORRECTIONS
# ===================================================================

class TestShadowDepth:
    """Entanglement complexity classification."""

    def test_class_G(self):
        """Class G: exact Calabrese-Cardy."""
        assert shadow_depth_class('heisenberg') == 'G'
        assert shadow_depth_class('lattice') == 'G'
        assert shadow_depth_class('free_fermion') == 'G'

    def test_class_L(self):
        """Class L: one cubic correction."""
        assert shadow_depth_class('affine') == 'L'
        assert shadow_depth_class('kac_moody') == 'L'

    def test_class_C(self):
        """Class C: cubic + quartic corrections."""
        assert shadow_depth_class('betagamma') == 'C'
        assert shadow_depth_class('bc') == 'C'

    def test_class_M(self):
        """Class M: infinite correction tower."""
        assert shadow_depth_class('virasoro') == 'M'
        assert shadow_depth_class('w_algebra') == 'M'

    def test_correction_depth_values(self):
        assert entanglement_correction_depth('heisenberg') == 2
        assert entanglement_correction_depth('affine') == 3
        assert entanglement_correction_depth('betagamma') == 4
        assert entanglement_correction_depth('virasoro') == -1


class TestShadowCorrections:
    """Shadow correction bounds and convergence."""

    def test_shadow_radius_self_dual(self):
        """rho(c=13) ~ 0.467 (self-dual point)."""
        rho = shadow_radius_virasoro(13)
        assert abs(rho - 0.467) < 0.01

    def test_shadow_radius_decreases_with_c(self):
        """rho(c) decreases for large c."""
        rho_13 = shadow_radius_virasoro(13)
        rho_26 = shadow_radius_virasoro(26)
        assert rho_26 < rho_13

    def test_shadow_radius_convergent_regime(self):
        """rho < 1 for c > c* ~ 6.125."""
        assert shadow_radius_virasoro(7) < 1.0
        assert shadow_radius_virasoro(13) < 1.0
        assert shadow_radius_virasoro(26) < 1.0

    def test_shadow_radius_divergent_regime(self):
        """rho > 1 for c < c* (e.g., Ising c=1/2)."""
        rho_ising = shadow_radius_virasoro(0.5)
        assert rho_ising > 1.0

    def test_correction_bound_decay(self):
        """Corrections decay as rho^r * r^{-5/2}."""
        rho = 0.5
        b3 = entanglement_correction_bound(rho, 3)
        b4 = entanglement_correction_bound(rho, 4)
        b5 = entanglement_correction_bound(rho, 5)
        assert b3 > b4 > b5

    def test_convergence_radius(self):
        """R = 2*pi/rho."""
        assert abs(entanglement_convergence_radius(1.0) - 2 * math.pi) < 0.01
        assert entanglement_convergence_radius(0.5) > 10

    def test_class_G_no_corrections(self):
        """For class G, the scalar formula is exact (no corrections)."""
        data = entanglement_data_heisenberg(Rational(1))
        assert data['corrections'] == 0
        assert data['S_EE_exact'] == data['S_EE_scalar']


# ===================================================================
#  7. STANDARD FAMILY ENTANGLEMENT DATA
# ===================================================================

class TestStandardFamilies:
    """Entanglement data for all standard families."""

    def test_heisenberg(self):
        data = entanglement_data_heisenberg(Rational(1))
        assert data['kappa'] == Rational(1)
        assert data['S_EE_exact'] == Rational(2, 3)
        assert data['shadow_class'] == 'G'

    def test_affine_sl2(self):
        data = entanglement_data_affine_sl2(Rational(1))
        assert data['kappa'] == Rational(9, 4)
        assert data['shadow_class'] == 'L'
        assert data['S_EE_scalar'] == Rational(3, 2)

    def test_virasoro_ising(self):
        data = entanglement_data_virasoro(Rational(1, 2))
        assert data['kappa'] == Rational(1, 4)
        assert data['S_EE_scalar'] == Rational(1, 6)
        assert data['shadow_class'] == 'M'
        assert not data['convergent']  # rho > 1 for Ising

    def test_virasoro_self_dual(self):
        data = entanglement_data_virasoro(Rational(13))
        assert data['self_dual']
        assert data['S_EE_scalar'] == data['S_EE_dual_scalar']
        assert data['convergent']  # rho ~ 0.467 < 1

    def test_virasoro_critical_string(self):
        data = entanglement_data_virasoro(Rational(26))
        assert data['kappa'] == Rational(13)
        assert data['c_dual'] == 0
        assert data['S_EE_scalar'] == Rational(26, 3)
        assert data['S_EE_dual_scalar'] == 0

    def test_census_nonempty(self):
        census = standard_landscape_entanglement_census()
        assert len(census) >= 6

    def test_census_class_coverage(self):
        """Census covers all four shadow depth classes."""
        census = standard_landscape_entanglement_census()
        classes = {d['class'] for d in census}
        assert 'G' in classes
        assert 'L' in classes
        assert 'C' in classes
        assert 'M' in classes


# ===================================================================
#  8. GENUS STRUCTURE
# ===================================================================

class TestGenusStructure:
    """Lagrangian and moduli space structure."""

    def test_lagrangian_genus_1(self):
        assert lagrangian_dimension_genus_1() == 1

    def test_bulk_boundary_entanglement_g1(self):
        assert bulk_boundary_entanglement_genus_1() == 0

    def test_moduli_dimension(self):
        assert moduli_dimension(1) == 0
        assert moduli_dimension(2) == 3
        assert moduli_dimension(3) == 6

    def test_shifted_symplectic_degree(self):
        assert shifted_symplectic_degree(1) == 0
        assert shifted_symplectic_degree(2) == -3
        assert shifted_symplectic_degree(3) == -6


# ===================================================================
#  9. QES CONDITION
# ===================================================================

class TestQuantumExtremalSurface:
    """Quantum extremal surface stationarity."""

    def test_qes_area_term(self):
        """Area/4G = (2*kappa/3) * log(L/eps)."""
        assert qes_area_term(Rational(13, 2), 1) == Rational(13, 3)

    def test_qes_bulk_entropy_small(self):
        """Bulk entropy is small relative to area for convergent algebras."""
        rho_13 = shadow_radius_virasoro(13)
        bound = qes_bulk_entropy_bound(Rational(13, 2), rho_13, 10)
        assert bound < 0.1

    def test_qes_ratio_small_for_convergent(self):
        """S_bulk/S_area << 1 for convergent shadow towers."""
        rho = shadow_radius_virasoro(13)
        ratio = qes_ratio(Rational(13, 2), rho)
        assert ratio < 0.1

    def test_qes_ratio_increases_with_rho(self):
        """Larger rho means larger corrections."""
        rho_small = 0.3
        rho_large = 0.8
        r_small = qes_ratio(Rational(13, 2), rho_small)
        r_large = qes_ratio(Rational(13, 2), rho_large)
        assert r_large > r_small


# ===================================================================
#  10. CROSS-CHECKS AND VERIFICATION TABLE
# ===================================================================

class TestCrossChecks:
    """Cross-check verification."""

    def test_entanglement_table(self):
        table = entanglement_entropy_table()
        assert len(table) >= 6

    def test_table_self_dual_entry(self):
        """Self-dual entry in the table has S = S'."""
        table = entanglement_entropy_table()
        sd = [e for e in table if 'c=13' in e['family']]
        assert len(sd) == 1
        assert sd[0]['S_EE_coeff'] == sd[0].get('S_dual_coeff')

    def test_table_complementarity(self):
        """Entries with dual data satisfy complementarity sum."""
        table = entanglement_entropy_table()
        for entry in table:
            if 'sum' in entry:
                assert entry['sum'] == Rational(26, 3)

    def test_additivity_heisenberg(self):
        """Additivity: S_EE(H_{k1} + H_{k2}) = S_EE(H_{k1}) + S_EE(H_{k2}).

        For independent systems (independent sum factorization),
        entanglement entropy is additive at the scalar level.
        kappa(H_{k1} + H_{k2}) = k1 + k2.
        """
        k1 = Rational(1)
        k2 = Rational(2)
        s1 = von_neumann_entropy_scalar(kappa_heisenberg(k1), 1)
        s2 = von_neumann_entropy_scalar(kappa_heisenberg(k2), 1)
        s_sum = von_neumann_entropy_scalar(kappa_heisenberg(k1 + k2), 1)
        assert s_sum == s1 + s2

    def test_complementarity_is_antisymmetric_pairing(self):
        """The complementarity constraint follows from
        Theta_A + Theta_{A!} = 0 (Lagrangian antisymmetry).

        At the scalar level: kappa(A) + kappa(A!) = 13 (Virasoro),
        so S_EE(A) + S_EE(A!) = 26/3 = 2*13/3.
        """
        for c in [Rational(1), Rational(7), Rational(13), Rational(25)]:
            kappa_a = kappa_virasoro(c)
            kappa_d = kappa_virasoro(26 - c)
            # Lagrangian antisymmetry at scalar level
            assert kappa_a + kappa_d == Rational(13)

    def test_renyi_spectrum_monotonicity(self):
        """Renyi entropy S_n is non-increasing in n >= 1."""
        kappa = Rational(13, 2)
        prev = von_neumann_entropy_scalar(kappa, 1)  # S_1 = S_EE
        for n in [2, 3, 4, 5, 10, 100]:
            s_n = renyi_entropy_scalar(kappa, n, 1)
            assert s_n <= prev or n == 2  # S_1 >= S_2 >= S_3 >= ...
            if n >= 3:
                assert s_n <= renyi_entropy_scalar(kappa, n - 1, 1)

    def test_min_renyi_entropy(self):
        """S_infinity = lim_{n->inf} S_n = (kappa/3) * log(L/eps).

        This is the min-entropy, half the von Neumann entropy.
        """
        kappa = Rational(13, 2)
        s_inf = Rational(kappa, 3)  # lim (kappa/3)(1 + 1/n) = kappa/3
        # Large n approximation
        s_100 = renyi_entropy_scalar(kappa, 100, 1)
        assert abs(float(s_100 - s_inf)) < 0.1
