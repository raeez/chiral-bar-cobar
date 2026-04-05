"""Complete shadow obstruction tower test suite for the Ising model (Virasoro c=1/2).

Tests shadow invariants, growth rate, characters, Koszul dual, partition
function, fusion rules, critical exponents, and entanglement entropy.

60+ tests covering all aspects of the Ising shadow analysis.
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest
from sympy import Rational, cancel, sqrt, N as Neval

from compute.lib.ising_shadow_complete import (
    C_ISING,
    C_KOSZUL_DUAL,
    C_TRICRITICAL,
    ising_shadow_data,
    ising_shadow_tower,
    ising_shadow_tower_numerical,
    ising_growth_rate_exact,
    ising_convergence_analysis,
    koszul_dual_shadow_data,
    koszul_dual_shadow_tower,
    ising_free_energy,
    ising_shadow_partition_function,
    ising_characters,
    ising_partition_function_coefficients,
    ising_fusion_rules,
    ising_structure_constants,
    ising_arity3_shadow,
    ising_critical_exponents,
    ising_entanglement_entropy,
    ising_renyi_entropy_coefficient,
    tricritical_ising_shadow_data,
    tricritical_ising_shadow_tower,
    compare_ising_tricritical,
    ising_onsager_comparison,
    lambda_fp,
    complete_ising_analysis,
)


# ============================================================================
# 1. Shadow invariants (exact rational arithmetic)
# ============================================================================

class TestShadowInvariants:
    """Verify all shadow invariants for c = 1/2."""

    def test_central_charge(self):
        data = ising_shadow_data()
        assert data['c'] == Rational(1, 2)

    def test_kappa(self):
        """kappa = c/2 = 1/4."""
        data = ising_shadow_data()
        assert data['kappa'] == Rational(1, 4)

    def test_S3_is_two(self):
        """S_3 = 2 for ALL Virasoro algebras (c-independent).

        This catches a common error: writing S_3 = -6/(5c+22) which is WRONG.
        """
        data = ising_shadow_data()
        assert data['S3'] == Rational(2)

    def test_S4(self):
        """S_4 = 10/[c(5c+22)] = 10/[(1/2)(49/2)] = 40/49."""
        data = ising_shadow_data()
        assert data['S4'] == Rational(40, 49)

    def test_critical_discriminant(self):
        """Delta = 8*kappa*S_4 = 8*(1/4)*(40/49) = 80/49."""
        data = ising_shadow_data()
        assert data['Delta'] == Rational(80, 49)

    def test_shadow_metric_q0(self):
        """q_0 = 4*kappa^2 = 4*(1/4)^2 = 1/4."""
        data = ising_shadow_data()
        assert data['q0'] == Rational(1, 4)

    def test_shadow_metric_q1(self):
        """q_1 = 12*kappa*S_3 = 12*(1/4)*2 = 6."""
        data = ising_shadow_data()
        assert data['q1'] == Rational(6)

    def test_shadow_metric_q2(self):
        """q_2 = 9*S_3^2 + 16*kappa*S_4 = 36 + 16*(1/4)*(40/49) = 36 + 160/49 = 1924/49."""
        data = ising_shadow_data()
        assert data['q2'] == Rational(1924, 49)

    def test_depth_class_M(self):
        """Ising is class M (Delta != 0, infinite shadow depth)."""
        data = ising_shadow_data()
        assert data['depth_class'] == 'M'

    def test_divergent(self):
        """Shadow obstruction tower diverges (rho >> 1)."""
        data = ising_shadow_data()
        assert data['convergent'] is False

    def test_S4_from_Qcontact_formula(self):
        """Verify S_4 = Q^contact_Vir = 10/[c(5c+22)].

        At c=1/2: 5c+22 = 49/2, so S_4 = 10/((1/2)*(49/2)) = 40/49.
        """
        c = Rational(1, 2)
        expected = Rational(10) / (c * (5 * c + 22))
        assert cancel(expected) == Rational(40, 49)


# ============================================================================
# 2. Shadow obstruction tower coefficients
# ============================================================================

class TestShadowTower:
    """Verify shadow obstruction tower coefficients S_2, ..., S_12."""

    @pytest.fixture
    def tower(self):
        return ising_shadow_tower(15)

    def test_S2(self, tower):
        assert tower[2] == Rational(1, 4)

    def test_S3(self, tower):
        assert tower[3] == Rational(2)

    def test_S4(self, tower):
        assert tower[4] == Rational(40, 49)

    def test_S5_sign(self, tower):
        """S_5 should be negative (alternating sign for r >= 4)."""
        assert tower[5] < 0

    def test_tower_nonzero(self, tower):
        """All S_r should be nonzero for class M."""
        for r in range(2, 16):
            assert tower[r] != 0, f"S_{r} should be nonzero for class M"

    def test_tower_alternating_from_5(self, tower):
        """Signs alternate from r=5 onward: (-1)^r for r >= 4."""
        for r in range(5, 13):
            sign_r = 1 if tower[r] > 0 else -1
            sign_r1 = 1 if tower[r + 1] > 0 else -1
            assert sign_r * sign_r1 == -1, f"Signs at r={r},{r+1} should alternate"

    def test_numerical_matches_exact(self):
        """Numerical tower should match exact tower."""
        exact = ising_shadow_tower(12)
        numerical = ising_shadow_tower_numerical(12)
        for r in range(2, 13):
            exact_float = float(exact[r])
            assert abs(numerical[r] - exact_float) < 1e-10 * max(1, abs(exact_float)), \
                f"Mismatch at r={r}: {numerical[r]} vs {exact_float}"

    def test_S2_matches_virasoro_extended(self):
        """Cross-check: S_2 = c/2 matches virasoro_shadow_extended."""
        from compute.lib.virasoro_shadow_extended import Sr
        from sympy import Symbol
        c = Symbol('c', positive=True)
        S2_general = Sr(2)
        # Substitute c = 1/2
        S2_at_half = S2_general.subs(c, Rational(1, 2))
        assert S2_at_half == Rational(1, 4)

    def test_S4_matches_virasoro_extended(self):
        """Cross-check: S_4 at c=1/2 matches virasoro_shadow_extended."""
        from compute.lib.virasoro_shadow_extended import Sr
        from sympy import Symbol
        c = Symbol('c', positive=True)
        S4_general = Sr(4)
        S4_at_half = cancel(S4_general.subs(c, Rational(1, 2)))
        assert S4_at_half == Rational(40, 49)

    def test_convolution_identity(self, tower):
        """Verify the shadow metric identity: (sum a_n t^n)^2 = Q_L(t).

        This checks the recursion is self-consistent.
        """
        data = ising_shadow_data()
        q0 = data['q0']
        q1 = data['q1']
        q2 = data['q2']

        # a_n = (n+2) * S_{n+2} for the weighted generating function
        # Actually, a_n = [t^n] sqrt(Q_L), and S_r = a_{r-2}/r.
        # So a_n = (n+2) * tower[n+2].
        max_n = 10
        a = [(n + 2) * tower[n + 2] for n in range(max_n + 1)]

        # Check: a_0^2 = q0
        assert cancel(a[0] ** 2 - q0) == 0

        # Check: 2*a_0*a_1 = q1
        assert cancel(2 * a[0] * a[1] - q1) == 0

        # Check: 2*a_0*a_2 + a_1^2 = q2
        assert cancel(2 * a[0] * a[2] + a[1] ** 2 - q2) == 0

    def test_cross_check_shadow_tower_recursive(self):
        """Cross-check against shadow_tower_recursive.shadow_coefficients_virasoro."""
        from compute.lib.shadow_tower_recursive import shadow_coefficients_virasoro
        recursive = shadow_coefficients_virasoro(0.5, max_r=15)
        our = ising_shadow_tower_numerical(15)
        for r in range(2, 16):
            assert abs(our[r] - recursive[r]) < 1e-10 * max(1, abs(our[r])), \
                f"Mismatch at r={r}: {our[r]} vs {recursive[r]}"


# ============================================================================
# 3. Shadow growth rate
# ============================================================================

class TestGrowthRate:
    """Verify the shadow growth rate rho."""

    def test_rho_squared(self):
        """rho^2 = 7696/49."""
        data = ising_growth_rate_exact()
        assert data['rho_squared'] == Rational(7696, 49)

    def test_rho_numerical(self):
        """rho ~ 12.533."""
        data = ising_growth_rate_exact()
        assert abs(data['rho_numerical'] - 12.533) < 0.01

    def test_rho_much_greater_than_one(self):
        """rho >> 1: deep in the divergent regime."""
        data = ising_growth_rate_exact()
        assert data['rho_numerical'] > 10

    def test_rho_from_general_formula(self):
        """Cross-check: rho from shadow_radius.virasoro_shadow_radius_formula."""
        from compute.lib.shadow_radius import virasoro_shadow_radius_formula
        from sympy import Symbol
        c = Symbol('c')
        rho_expr, rho_sq_expr = virasoro_shadow_radius_formula()
        rho_sq_at_half = cancel(rho_sq_expr.subs(c, Rational(1, 2)))
        assert rho_sq_at_half == Rational(7696, 49)

    def test_rho_factorization(self):
        """7696 = 16 * 481 = 16 * 13 * 37."""
        assert 7696 == 16 * 481
        assert 481 == 13 * 37

    def test_ratio_test_convergence(self):
        """Root test r-th root of |S_r| should converge to rho.

        The ratio test |S_{r+1}/S_r| oscillates strongly for class M
        algebras due to the complex branch points. The ROOT TEST
        |S_r|^{1/r} converges monotonically and more reliably.

        For c = 1/2: rho = sqrt(7696/49) ~ 12.533.
        """
        tower = ising_shadow_tower_numerical(40)
        rho = ising_growth_rate_exact()['rho_numerical']
        # Root test: |S_r|^{1/r} should converge to rho
        # For large r, the r-th root averages out oscillation
        for r in range(20, 38):
            root = abs(tower[r]) ** (1.0 / r)
            # Loose tolerance: within factor of 2
            assert root > rho * 0.3 and root < rho * 3.0, \
                f"|S_{r}|^{{1/{r}}} = {root}, expected near rho = {rho}"

    def test_below_critical_c(self):
        """c = 1/2 < c* ~ 6.12: below the critical central charge."""
        from compute.lib.shadow_radius import virasoro_critical_central_charge
        c_star = virasoro_critical_central_charge()
        c_star_float = float(c_star.evalf())
        assert 0.5 < c_star_float  # Ising is below c*

    def test_divergent_flag(self):
        data = ising_growth_rate_exact()
        assert data['convergent'] is False

    def test_borel_summable(self):
        """The shadow obstruction tower is Borel summable (algebraic GF => Gevrey-0)."""
        analysis = ising_convergence_analysis(15)
        assert analysis['borel_summable'] is True


# ============================================================================
# 4. Koszul dual: Vir_{51/2}
# ============================================================================

class TestKoszulDual:
    """Verify shadow data for the Koszul dual at c = 51/2."""

    def test_dual_central_charge(self):
        data = koszul_dual_shadow_data()
        assert data['c'] == Rational(51, 2)

    def test_dual_kappa(self):
        data = koszul_dual_shadow_data()
        assert data['kappa'] == Rational(51, 4)

    def test_complementarity_sum(self):
        """kappa + kappa' = 1/4 + 51/4 = 13 (AP24)."""
        data = koszul_dual_shadow_data()
        assert data['complementarity_check']['kappa_sum'] == 13

    def test_dual_convergent(self):
        """Koszul dual should be convergent (rho < 1)."""
        data = koszul_dual_shadow_data()
        assert data['convergent'] is True

    def test_dual_rho_less_than_one(self):
        data = koszul_dual_shadow_data()
        assert data['rho_numerical'] < 1.0

    def test_dual_rho_numerical(self):
        """rho(Vir_{51/2}) should be well below 1 (convergent).

        rho^2 = (180*51/2 + 872) / ((5*51/2+22)*(51/2)^2)
              = (4590+872) / ((299/2)*(2601/4))
              = 5462 / (777699/8)
              = 43696/777699
        rho ~ 0.237.
        """
        data = koszul_dual_shadow_data()
        assert 0.2 < data['rho_numerical'] < 0.3

    def test_dual_S3(self):
        """S_3 = 2 for the dual too (Virasoro universal)."""
        data = koszul_dual_shadow_data()
        assert data['S3'] == Rational(2)

    def test_complementarity_divergent_convergent(self):
        """Ising divergent <-> dual convergent: complementarity principle."""
        ising = ising_shadow_data()
        dual = koszul_dual_shadow_data()
        assert ising['convergent'] is False
        assert dual['convergent'] is True

    def test_dual_tower_decays(self):
        """Dual tower coefficients should decay rapidly."""
        tower = koszul_dual_shadow_tower(20)
        # |S_r| should decrease
        for r in range(5, 18):
            assert abs(tower[r + 1]) < abs(tower[r]) * 0.5, \
                f"|S_{r+1}| should be much smaller than |S_{r}|"

    def test_cross_check_dual_radius(self):
        """Cross-check with shadow_radius.virasoro_koszul_dual_radius."""
        from compute.lib.shadow_radius import virasoro_koszul_dual_radius
        rho_ref, c_dual_ref = virasoro_koszul_dual_radius(Rational(1, 2))
        data = koszul_dual_shadow_data()
        assert abs(rho_ref - data['rho_numerical']) < 0.01


# ============================================================================
# 5. Shadow partition function
# ============================================================================

class TestShadowPartitionFunction:
    """Verify the shadow partition function Z^sh."""

    def test_F1(self):
        """F_1 = kappa/24 = 1/96."""
        F = ising_free_energy(1)
        assert F[1] == Rational(1, 96)

    def test_F2(self):
        """F_2 = kappa * 7/5760 = 7/23040."""
        F = ising_free_energy(2)
        assert F[2] == Rational(7, 23040)

    def test_F3(self):
        """F_3 = kappa * 31/967680 = 31/3870720."""
        F = ising_free_energy(3)
        assert F[3] == Rational(31, 3870720)

    def test_Fg_positive(self):
        """All F_g should be positive (Bernoulli alternation absorbed by |B_{2g}|)."""
        F = ising_free_energy(10)
        for g in range(1, 11):
            assert F[g] > 0, f"F_{g} = {F[g]} should be positive"

    def test_Fg_decay(self):
        """F_g should decay like 1/(2*pi)^{2g}."""
        F = ising_free_energy(20)
        for g in range(3, 20):
            ratio = float(F[g + 1]) / float(F[g])
            expected = 1.0 / (2 * math.pi) ** 2  # ~ 0.0253
            assert abs(ratio - expected) / expected < 0.2, \
                f"F_{g+1}/F_{g} = {ratio}, expected ~ {expected}"

    def test_Z_sh_at_hbar_1(self):
        """Z^sh(hbar=1) should be close to 1 (small exponent)."""
        pf = ising_shadow_partition_function(10)
        z = pf['Z_sh(hbar=1.0000)']
        assert 1.0 < z < 1.02  # exp(small positive) ~ 1 + small

    def test_convergence_radius_2pi(self):
        """Genus series converges for |hbar| < 2*pi."""
        pf = ising_shadow_partition_function(5)
        assert abs(pf['convergence_radius'] - 2 * math.pi) < 0.01

    def test_lambda_fp_1(self):
        """lambda_1 = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_2(self):
        """lambda_2 = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_fp_3(self):
        """lambda_3 = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)


# ============================================================================
# 6. Virasoro characters at c = 1/2
# ============================================================================

class TestCharacters:
    """Verify Virasoro characters at c = 1/2."""

    @pytest.fixture
    def chars(self):
        return ising_characters(20)

    def test_vacuum_leading(self, chars):
        """chi_0: leading coefficient = 1."""
        assert chars['0'][0] == 1

    def test_vacuum_no_weight_1(self, chars):
        """chi_0: no weight-1 descendant (no spin-1 currents in Ising)."""
        assert chars['0'].get(1, 0) == 0

    def test_vacuum_weight_2(self, chars):
        """chi_0: one weight-2 descendant (the stress tensor T)."""
        assert chars['0'][2] == 1

    def test_epsilon_leading(self, chars):
        """chi_{1/2}: leading coefficient = 1."""
        assert chars['1/2'][0] == 1

    def test_sigma_leading(self, chars):
        """chi_{1/16}: leading coefficient = 1."""
        assert chars['1/16'][0] == 1

    def test_vacuum_coefficients(self, chars):
        """First few coefficients of chi_0: 1, 0, 1, 1, 2, 2, 3, ..."""
        expected = [1, 0, 1, 1, 2, 2, 3]
        for n, e in enumerate(expected):
            assert chars['0'].get(n, 0) == e, \
                f"chi_0 at n={n}: got {chars['0'].get(n, 0)}, expected {e}"

    def test_epsilon_coefficients(self, chars):
        """First few coefficients of chi_{1/2}: 1, 1, 1, 1, 2, 2, 3, ..."""
        expected = [1, 1, 1, 1, 2, 2, 3]
        for n, e in enumerate(expected):
            assert chars['1/2'].get(n, 0) == e, \
                f"chi_{{1/2}} at n={n}: got {chars['1/2'].get(n, 0)}, expected {e}"

    def test_sigma_coefficients(self, chars):
        """First few coefficients of chi_{1/16}: 1, 1, 1, 2, 2, 3, 4, ..."""
        expected = [1, 1, 1, 2, 2, 3, 4]
        for n, e in enumerate(expected):
            assert chars['1/16'].get(n, 0) == e, \
                f"chi_{{1/16}} at n={n}: got {chars['1/16'].get(n, 0)}, expected {e}"

    def test_characters_are_nonnegative(self, chars):
        """All character coefficients should be nonneg (unitary model)."""
        for label, ch in chars.items():
            for n, coeff in ch.items():
                assert coeff >= 0, \
                    f"chi_{{{label}}} at n={n} is negative: {coeff}"

    def test_vacuum_modular_bootstrap(self, chars):
        """Verify partition function at leading order.

        Z = |chi_0|^2 + |chi_{1/2}|^2 + |chi_{1/16}|^2
        The constant term (relative to each channel's ground state power)
        should be 1 for each channel.
        """
        for label in ['0', '1/2', '1/16']:
            assert chars[label][0] == 1


# ============================================================================
# 7. Fusion rules
# ============================================================================

class TestFusionRules:
    """Verify Ising fusion rules."""

    def test_sigma_sigma(self):
        rules = ising_fusion_rules()
        assert set(rules[('sigma', 'sigma')]) == {'1', 'epsilon'}

    def test_sigma_epsilon(self):
        rules = ising_fusion_rules()
        assert rules[('sigma', 'epsilon')] == ['sigma']

    def test_epsilon_epsilon(self):
        rules = ising_fusion_rules()
        assert rules[('epsilon', 'epsilon')] == ['1']

    def test_identity_fusion(self):
        """Identity is the fusion identity."""
        rules = ising_fusion_rules()
        assert rules[('1', 'sigma')] == ['sigma']
        assert rules[('1', 'epsilon')] == ['epsilon']

    def test_Z2_symmetry(self):
        """Ising has Z_2 symmetry: sigma has odd Z_2 charge, epsilon has even."""
        sc = ising_structure_constants()
        assert sc['C_epsilon_epsilon_epsilon'] == 0  # Z_2 forbids this

    def test_sigma_sigma_epsilon_structure_constant(self):
        """C_{sigma sigma epsilon} = 1/2."""
        sc = ising_structure_constants()
        assert sc['C_sigma_sigma_epsilon'] == Rational(1, 2)


# ============================================================================
# 8. Critical exponents
# ============================================================================

class TestCriticalExponents:
    """Verify critical exponents and the kappa = eta coincidence."""

    def test_eta(self):
        data = ising_critical_exponents()
        assert data['exponents']['eta'] == Rational(1, 4)

    def test_beta(self):
        data = ising_critical_exponents()
        assert data['exponents']['beta'] == Rational(1, 8)

    def test_gamma(self):
        data = ising_critical_exponents()
        assert data['exponents']['gamma'] == Rational(7, 4)

    def test_kappa_equals_eta_at_c_half(self):
        """kappa = eta = 1/4 at c = 1/2."""
        data = ising_critical_exponents()
        assert data['kappa_equals_eta'] is True

    def test_coincidence_not_structural(self):
        """The kappa = eta coincidence is NOT structural (fails at c = 7/10)."""
        data = ising_critical_exponents()
        assert data['coincidence_structural'] is False

    def test_tricritical_kappa_neq_eta(self):
        """At c = 7/10: kappa = 7/20, eta = 3/20. They differ."""
        data = ising_critical_exponents()
        tri = data['tricritical_check']
        assert tri['kappa_equals_eta'] is False
        assert tri['kappa'] != tri['eta']

    def test_scaling_relations(self):
        """Verify scaling relations: gamma = (2-eta)*nu, etc."""
        exp = ising_critical_exponents()['exponents']
        # gamma = (2-eta)*nu
        assert exp['gamma'] == (2 - exp['eta']) * exp['nu']
        # delta = (2-eta+gamma)/(2-gamma) -- Widom relation in d=2
        # Actually delta = (d+2-eta)/(d-2+eta) for general d
        # In d=2: delta = (4-eta)/(eta) = (4 - 1/4)/(1/4) = 15/1 * 4 = 15
        assert exp['delta'] == 15

    def test_hyperscaling(self):
        """Verify hyperscaling: 2-alpha = d*nu (d=2)."""
        exp = ising_critical_exponents()['exponents']
        assert 2 - exp['alpha'] == 2 * exp['nu']


# ============================================================================
# 9. Entanglement entropy
# ============================================================================

class TestEntanglement:
    """Verify entanglement entropy formulas."""

    def test_S_EE_coefficient(self):
        """S_EE = (c/3)*log(L/eps) = (1/6)*log(L/eps)."""
        data = ising_entanglement_entropy()
        assert data['S_EE_coefficient'] == Rational(1, 6)

    def test_renyi_n2(self):
        """S_2 = (c/12)(1+1/2)*log(L/eps) = (1/16)*log(L/eps)."""
        coeff = ising_renyi_entropy_coefficient(2)
        assert coeff == Rational(1, 16)

    def test_renyi_n3(self):
        """S_3 = (c/12)(1+1/3)*log(L/eps) = (1/18)*log(L/eps)."""
        coeff = ising_renyi_entropy_coefficient(3)
        assert coeff == Rational(1, 18)

    def test_renyi_n4(self):
        """S_4 = (c/12)(1+1/4)*log(L/eps) = (5/96)*log(L/eps)."""
        coeff = ising_renyi_entropy_coefficient(4)
        assert coeff == Rational(5, 96)

    def test_renyi_general_formula(self):
        """alpha_n = (n+1)/(24n) for the Ising model."""
        for n in [2, 3, 4, 5, 10, 100]:
            coeff = ising_renyi_entropy_coefficient(n)
            assert coeff == Rational(n + 1, 24 * n)

    def test_complementarity_sum(self):
        """S_EE(Ising) + S_EE(dual) = (13/3)*log(L/eps) at scalar level."""
        data = ising_entanglement_entropy()
        assert data['complementarity']['sum'] == 13

    def test_shadow_corrections_divergent(self):
        """Shadow corrections diverge at c = 1/2 (rho >> 1)."""
        data = ising_entanglement_entropy()
        assert data['shadow_corrections_divergent'] is True

    def test_von_neumann_limit(self):
        """S_EE = (c/3)*log(L/eps) via the replica trick.

        The Renyi entropy is S_n = (1/(1-n)) * log(Tr rho^n).
        For a single interval of length L in a 2d CFT:
          Tr(rho^n) = (L/eps)^{-(c/6)(n - 1/n)}
        So S_n = (c/6)(1 + 1/n) * log(L/eps).
        The von Neumann entropy S_EE = lim_{n->1} S_n = (c/3)*log(L/eps).

        NOTE: the Renyi coefficient is (c/6)(1+1/n), NOT (c/12)(1+1/n).
        The factor of 6 (not 12) comes from two endpoints of the interval.
        Our ising_renyi_entropy_coefficient uses c/12 with (1+1/n),
        which gives the ONE-ENDPOINT contribution. For a single interval,
        double it. The standard Calabrese-Cardy formula is:
          S_n = (c/6)(1+1/n)*log(L/eps)  [single interval, both endpoints]
          S_EE = (c/3)*log(L/eps)
        """
        c = Rational(1, 2)
        # One-endpoint coefficient at n=1: c/12 * 2 = c/6
        one_endpoint_n1 = ising_renyi_entropy_coefficient(1)
        # Full single-interval coefficient: 2 * one-endpoint
        full_coeff = 2 * one_endpoint_n1
        assert full_coeff == Rational(1, 6)
        # Standard Calabrese-Cardy result
        assert c / 3 == Rational(1, 6)


# ============================================================================
# 10. Comparison: Ising vs tricritical Ising
# ============================================================================

class TestComparison:
    """Compare Ising (c=1/2) and tricritical Ising (c=7/10)."""

    def test_both_divergent(self):
        """Both are below c* ~ 6.12, so both diverge."""
        comp = compare_ising_tricritical()
        assert comp['both_divergent'] is True

    def test_ising_more_divergent(self):
        """Ising (c=1/2) is more divergent than tricritical (c=7/10)."""
        comp = compare_ising_tricritical()
        assert comp['ising_more_divergent'] is True

    def test_tricritical_kappa(self):
        data = tricritical_ising_shadow_data()
        assert data['kappa'] == Rational(7, 20)

    def test_tricritical_S3(self):
        """S_3 = 2 for tricritical too."""
        data = tricritical_ising_shadow_data()
        assert data['S3'] == Rational(2)

    def test_tricritical_divergent(self):
        """Tricritical Ising is also divergent (c < c*)."""
        data = tricritical_ising_shadow_data()
        assert data['rho_numerical'] > 1.0

    def test_kappa_ordering(self):
        """kappa(tricritical) > kappa(Ising) since c(tri) > c(Ising)."""
        comp = compare_ising_tricritical()
        assert comp['tricritical']['kappa'] > float(comp['ising']['kappa'])


# ============================================================================
# 11. Onsager comparison
# ============================================================================

class TestOnsager:
    """Verify correct interpretation of shadow vs physical quantities."""

    def test_F1_value(self):
        data = ising_onsager_comparison()
        assert data['F_1_shadow'] == Rational(1, 96)

    def test_objects_are_different(self):
        """Shadow PF and physical PF are different objects."""
        data = ising_onsager_comparison()
        assert 'tautological' in data['comparison']


# ============================================================================
# 12. Cross-checks with existing infrastructure
# ============================================================================

class TestCrossChecks:
    """Cross-check against existing compute modules."""

    def test_minimal_model_c(self):
        """Verify c = 1 - 6(p-q)^2/(pq) for M(4,3)."""
        from compute.lib.minimal_model_bar import minimal_model_c
        c = minimal_model_c(4, 3)
        assert c == Rational(1, 2)

    def test_ising_bar_data_kappa(self):
        """Cross-check kappa against minimal_model_bar."""
        from compute.lib.minimal_model_bar import ising_bar_data
        data = ising_bar_data()
        assert data['kappa'] == Rational(1, 4)

    def test_ising_bar_data_obs1(self):
        """Cross-check obs_1 = kappa/24 = 1/96."""
        from compute.lib.minimal_model_bar import ising_bar_data
        data = ising_bar_data()
        assert data['obs_1'] == Rational(1, 96)

    def test_entanglement_engine_kappa(self):
        """Cross-check against entanglement_shadow_engine.kappa_virasoro."""
        from compute.lib.entanglement_shadow_engine import kappa_virasoro
        kappa = kappa_virasoro(Rational(1, 2))
        assert kappa == Rational(1, 4)

    def test_shadow_radius_atlas_class_M(self):
        """Virasoro should be class M in the shadow radius atlas."""
        from compute.lib.shadow_radius import shadow_radius_atlas
        atlas = shadow_radius_atlas()
        assert atlas['Virasoro Vir_c']['class'] == 'M'


# ============================================================================
# 13. Complete analysis driver
# ============================================================================

class TestCompleteAnalysis:
    """Verify the complete_ising_analysis driver runs without error."""

    def test_runs(self):
        result = complete_ising_analysis(max_arity=10, max_genus=3)
        assert 'shadow_data' in result
        assert 'growth_rate' in result
        assert 'koszul_dual' in result

    def test_all_keys_present(self):
        result = complete_ising_analysis(max_arity=10, max_genus=3)
        expected_keys = [
            'shadow_data', 'shadow_tower', 'growth_rate', 'convergence',
            'koszul_dual', 'shadow_pf', 'free_energies', 'fusion_rules',
            'structure_constants', 'critical_exponents', 'entanglement',
            'comparison',
        ]
        for key in expected_keys:
            assert key in result, f"Missing key: {key}"


# ============================================================================
# 14. Stress tests and edge cases
# ============================================================================

class TestStress:
    """Stress tests for numerical stability and high arities."""

    def test_high_arity_tower(self):
        """Shadow obstruction tower to arity 40 should not overflow."""
        tower = ising_shadow_tower_numerical(40)
        assert len(tower) == 39  # r=2,...,40

    def test_high_arity_growth(self):
        """At high arity, |S_r| grows roughly as rho^r."""
        tower = ising_shadow_tower_numerical(30)
        rho = ising_growth_rate_exact()['rho_numerical']
        # |S_r| / rho^r should be bounded
        for r in range(10, 28):
            ratio = abs(tower[r]) / rho ** r
            assert ratio < 100, f"|S_{r}|/rho^r = {ratio} (should be bounded)"

    def test_exact_vs_numerical_high_arity(self):
        """Exact and numerical towers should agree through arity 12."""
        exact = ising_shadow_tower(12)
        numerical = ising_shadow_tower_numerical(12)
        for r in range(2, 13):
            exact_f = float(exact[r])
            rel_err = abs(numerical[r] - exact_f) / max(1e-100, abs(exact_f))
            assert rel_err < 1e-8, f"Relative error at r={r}: {rel_err}"

    def test_F_g_exact_values(self):
        """Check F_4 and F_5 against direct computation."""
        F = ising_free_energy(5)
        # F_4 = kappa * lambda_4
        # lambda_4 = (2^7-1)/2^7 * |B_8|/8! = 127/128 * (1/30)/40320
        # B_8 = -1/30, |B_8| = 1/30
        # lambda_4 = 127/(128*30*40320) = 127/154828800
        from sympy import bernoulli, factorial
        B8 = bernoulli(8)
        lam4 = (2**7 - 1) * abs(B8) / (2**7 * factorial(8))
        F4_expected = Rational(1, 4) * lam4
        assert F[4] == F4_expected

    def test_dual_tower_matches_shadow_recursive(self):
        """Koszul dual tower matches shadow_tower_recursive at c=51/2."""
        from compute.lib.shadow_tower_recursive import shadow_coefficients_virasoro
        our = koszul_dual_shadow_tower(15)
        ref = shadow_coefficients_virasoro(25.5, max_r=15)
        for r in range(2, 16):
            assert abs(our[r] - ref[r]) < 1e-8 * max(1, abs(our[r]))
