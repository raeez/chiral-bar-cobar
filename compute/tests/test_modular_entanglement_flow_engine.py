r"""Tests for modular_entanglement_flow_engine.py.

Verification strategy:
  1. Calabrese-Cardy at several c values
  2. Renyi S_n = (c/6)(1+1/n)*log(L/eps) for n=2,3,4,5,10
  3. Von Neumann as n->1 limit of Renyi
  4. Twist dimension h_n = (c/24)(n-1/n)
  5. Complementarity S(c) + S(26-c) = (26/3)*log(L/eps)
  6. Modular Hamiltonian for Heisenberg, Virasoro, affine sl_2
  7. Shadow correction convergence for rho < 1
  8. Class-by-class: G=exact, L=one correction, C=two, M=infinite
  9. QES condition at scalar level
  10. Mutual information from cross-ratio
  11. Page point at c=13
  12. Entanglement capacity C_E
  13. Replica Z_n positivity
  14. Growth bound (Carlson theorem)
  15. Entanglement spectrum spacing
  16. 60+ total tests
"""

import math
import pytest
from fractions import Fraction
from sympy import Rational, simplify, pi, Symbol

from compute.lib.modular_entanglement_flow_engine import (
    # 1. Modular Hamiltonian
    modular_hamiltonian_scalar,
    modular_hamiltonian_entanglement_weight,
    modular_hamiltonian_shadow_correction,
    modular_hamiltonian_full,
    # 2. Modular flow
    modular_flow_velocity_scalar,
    modular_flow_orbit,
    modular_flow_period,
    modular_flow_velocity_shadow_correction,
    # 3. Replica partition function
    replica_factor_genus0,
    replica_factor_genus1,
    replica_log_partition_full,
    replica_partition_function_value,
    replica_growth_bound,
    # 4. Renyi with shadow
    renyi_entropy_with_shadow,
    von_neumann_shadow_corrected,
    # 5. Entanglement spectrum
    entanglement_energy,
    entanglement_eigenvalue,
    entanglement_spectrum_spacing,
    entanglement_spectrum_primaries,
    # 6. QES
    qes_stationarity_scalar,
    qes_heisenberg,
    qes_virasoro,
    qes_affine_sl2,
    # 7. Mutual information
    mutual_information_scalar,
    mutual_information_value,
    mutual_information_complementarity,
    # 8. Temperature and capacity
    entanglement_temperature,
    entanglement_temperature_numerical,
    entanglement_capacity_scalar,
    entanglement_capacity_shadow_corrected,
    # 9. Page curve
    page_transition_virasoro,
    page_curve_virasoro,
    page_curve_table,
    # 10. Census
    cross_family_census,
    # 11. Shadow corrections
    shadow_correction_series_bound,
    shadow_correction_by_class,
    # 12. Genus structure
    genus_g_free_energy,
    genus_g_entanglement_correction,
    total_genus_expansion,
    # 13. Verification
    verify_modular_flow_fixed_points,
    verify_complementarity_all_c,
    verify_renyi_von_neumann_limit,
    verify_page_point_self_duality,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    von_neumann_entropy_scalar,
    renyi_entropy_scalar,
    twist_dimension_total,
    faber_pandharipande,
    shadow_radius_virasoro,
)


# ===================================================================
#  1. CALABRESE-CARDY REPRODUCTION
# ===================================================================

class TestCalabreseCardy:
    """S_EE = (c/3)*log(L/eps) for various c values."""

    @pytest.mark.parametrize("c_val,expected_coeff", [
        (Rational(1, 2), Rational(1, 6)),
        (Rational(1), Rational(1, 3)),
        (Rational(13), Rational(13, 3)),
        (Rational(26), Rational(26, 3)),
        (Rational(7, 10), Rational(7, 30)),
    ])
    def test_calabrese_cardy_coefficient(self, c_val, expected_coeff):
        """S_EE = (c/3)*log(L/eps): verify coefficient c/3."""
        kappa = kappa_virasoro(c_val)
        s_ee = von_neumann_entropy_scalar(kappa, 1)
        assert s_ee == expected_coeff

    def test_calabrese_cardy_ising(self):
        """Ising model c=1/2: S_EE = (1/6)*log(L/eps)."""
        kappa = kappa_virasoro(Rational(1, 2))
        assert von_neumann_entropy_scalar(kappa, 1) == Rational(1, 6)

    def test_calabrese_cardy_free_boson(self):
        """Free boson c=1: S_EE = (1/3)*log(L/eps)."""
        kappa = kappa_virasoro(Rational(1))
        assert von_neumann_entropy_scalar(kappa, 1) == Rational(1, 3)

    def test_calabrese_cardy_string(self):
        """Critical string c=26: S_EE = (26/3)*log(L/eps)."""
        kappa = kappa_virasoro(Rational(26))
        assert von_neumann_entropy_scalar(kappa, 1) == Rational(26, 3)


# ===================================================================
#  2. RENYI ENTROPY
# ===================================================================

class TestRenyiEntropy:
    """S_n = (c/6)(1+1/n)*log(L/eps) for several n."""

    @pytest.mark.parametrize("n", [2, 3, 4, 5, 10])
    def test_renyi_formula_c1(self, n):
        """Renyi at c=1 for n=2,3,4,5,10."""
        kappa = Rational(1, 2)  # c=1 => kappa=1/2
        expected = (kappa / 3) * (1 + Rational(1, n))
        got = renyi_entropy_scalar(kappa, n, 1)
        assert got == expected

    @pytest.mark.parametrize("n", [2, 3, 4, 5, 10])
    def test_renyi_formula_c26(self, n):
        """Renyi at c=26 for n=2,3,4,5,10."""
        kappa = Rational(13)
        expected = (kappa / 3) * (1 + Rational(1, n))
        got = renyi_entropy_scalar(kappa, n, 1)
        assert got == expected

    def test_renyi_monotonicity(self):
        """S_n is non-increasing in n."""
        kappa = Rational(13, 2)
        prev = renyi_entropy_scalar(kappa, 2, 1)
        for n in [3, 4, 5, 10, 100]:
            curr = renyi_entropy_scalar(kappa, n, 1)
            assert curr <= prev
            prev = curr

    def test_renyi_large_n_limit(self):
        """S_inf = (kappa/3)*log(L/eps) = half of S_EE."""
        kappa = Rational(13, 2)
        s_inf = renyi_entropy_scalar(kappa, 1000, 1)
        expected_inf = kappa / 3  # (kappa/3)*(1+0) at n=inf
        assert abs(float(s_inf) - float(expected_inf)) < 0.01


# ===================================================================
#  3. VON NEUMANN AS n->1 LIMIT
# ===================================================================

class TestVonNeumannLimit:
    """lim_{n->1} S_n = S_EE."""

    def test_limit_kappa_1(self):
        assert verify_renyi_von_neumann_limit(Rational(1))

    def test_limit_kappa_half(self):
        assert verify_renyi_von_neumann_limit(Rational(1, 2))

    def test_limit_kappa_13_over_2(self):
        assert verify_renyi_von_neumann_limit(Rational(13, 2))

    def test_limit_numerical_approach(self):
        """S_n for n close to 1 approximates S_EE."""
        kappa = Rational(13, 2)
        s_ee = float(von_neumann_entropy_scalar(kappa, 1))
        # n = 1 + 1e-6
        s_near = float(renyi_entropy_scalar(kappa, Rational(1000001, 1000000), 1))
        assert abs(s_near - s_ee) < 1e-4


# ===================================================================
#  4. TWIST DIMENSION
# ===================================================================

class TestTwistDimension:
    """h_n = (c/24)(n - 1/n)."""

    @pytest.mark.parametrize("n,c_val,expected", [
        (2, 1, Rational(1, 16)),
        (2, Rational(1, 2), Rational(1, 32)),
        (3, 1, Rational(1, 9)),
        (1, 1, 0),
        (2, 26, Rational(13, 8)),
    ])
    def test_twist_dimension_values(self, n, c_val, expected):
        assert twist_dimension_total(Rational(c_val), n) == expected

    def test_twist_positivity(self):
        """h_n > 0 for n >= 2 and c > 0."""
        for n in [2, 3, 4, 5]:
            for c in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
                assert twist_dimension_total(c, n) > 0


# ===================================================================
#  5. COMPLEMENTARITY
# ===================================================================

class TestComplementarity:
    """S(c) + S(26-c) = (26/3)*log(L/eps)."""

    @pytest.mark.parametrize("c_val", [
        Rational(1, 2), Rational(1), Rational(7, 10),
        Rational(4, 5), Rational(6), Rational(13),
        Rational(20), Rational(25), Rational(26),
    ])
    def test_complementarity_sum(self, c_val):
        kap = kappa_virasoro(c_val)
        kap_d = kappa_virasoro(26 - c_val)
        s = von_neumann_entropy_scalar(kap, 1)
        s_d = von_neumann_entropy_scalar(kap_d, 1)
        assert s + s_d == Rational(26, 3)

    def test_complementarity_self_dual(self):
        """At c=13: S = S_dual = 13/3."""
        kap = kappa_virasoro(Rational(13))
        s = von_neumann_entropy_scalar(kap, 1)
        assert s == Rational(13, 3)
        # 2 * 13/3 = 26/3
        assert 2 * s == Rational(26, 3)

    def test_complementarity_verification_function(self):
        results = verify_complementarity_all_c()
        for c_val, data in results.items():
            assert data['verified'], f"Complementarity failed at c={c_val}"


# ===================================================================
#  6. MODULAR HAMILTONIAN
# ===================================================================

class TestModularHamiltonian:
    """Modular Hamiltonian K_A for various families."""

    def test_modular_hamiltonian_heisenberg(self):
        """K coefficient for Heisenberg (kappa=1): 2/3."""
        kap = kappa_heisenberg(Rational(1))
        assert modular_hamiltonian_scalar(kap) == Rational(2, 3)

    def test_modular_hamiltonian_virasoro_c1(self):
        """K coefficient for Virasoro c=1: 1/3."""
        kap = kappa_virasoro(Rational(1))
        assert modular_hamiltonian_scalar(kap) == Rational(1, 3)

    def test_modular_hamiltonian_virasoro_c26(self):
        """K coefficient for Virasoro c=26: 26/3."""
        kap = kappa_virasoro(Rational(26))
        assert modular_hamiltonian_scalar(kap) == Rational(26, 3)

    def test_modular_hamiltonian_affine_sl2(self):
        """K coefficient for sl_2 at k=1: 2*9/4/3 = 3/2."""
        kap = kappa_affine(3, Rational(1), 2)
        assert modular_hamiltonian_scalar(kap) == Rational(3, 2)

    def test_entanglement_weight_endpoints(self):
        """w(0) = w(1) = 0."""
        assert modular_hamiltonian_entanglement_weight(0) == 0
        assert modular_hamiltonian_entanglement_weight(1) == 0

    def test_entanglement_weight_midpoint(self):
        """w(1/2) = 1/4 (maximum)."""
        assert modular_hamiltonian_entanglement_weight(Rational(1, 2)) == Rational(1, 4)

    def test_entanglement_weight_symmetry(self):
        """w(x) = w(1-x)."""
        for x in [Rational(1, 4), Rational(1, 3), Rational(1, 5)]:
            assert modular_hamiltonian_entanglement_weight(x) == \
                   modular_hamiltonian_entanglement_weight(1 - x)

    def test_shadow_correction_subleading(self):
        """Shadow corrections at arity r are O(1/r) relative to scalar."""
        kap = kappa_virasoro(Rational(13))
        for r in [3, 4, 5]:
            corr = modular_hamiltonian_shadow_correction(kap, Rational(1), r)
            assert corr == Rational(1, 3 * r)

    def test_full_hamiltonian_no_corrections(self):
        """Heisenberg: class G, no corrections."""
        kap = kappa_heisenberg(Rational(1))
        result = modular_hamiltonian_full(kap, {})
        assert result['scalar'] == Rational(2, 3)
        assert result['correction_sum'] == 0


# ===================================================================
#  7. SHADOW CORRECTION CONVERGENCE
# ===================================================================

class TestShadowCorrectionConvergence:
    """Sum |delta_S_r| < infinity for rho < 1."""

    def test_convergent_series_rho_half(self):
        """rho=0.5: total bound should be small."""
        result = shadow_correction_series_bound(0.5, max_r=20)
        assert result['convergent']
        assert result['total_bound'] < 0.1

    def test_divergent_series_rho_two(self):
        """rho=2.0: series diverges."""
        result = shadow_correction_series_bound(2.0, max_r=20)
        assert not result['convergent']

    def test_marginal_rho_one(self):
        """rho=1.0: marginally divergent."""
        result = shadow_correction_series_bound(1.0, max_r=20)
        assert not result['convergent']

    def test_virasoro_c13_convergent(self):
        """Virasoro c=13: rho ~ 0.467 < 1 => convergent."""
        rho = shadow_radius_virasoro(13)
        assert rho < 1.0
        result = shadow_correction_series_bound(rho, max_r=20)
        assert result['convergent']
        assert result['total_bound'] < 0.05

    def test_series_decreasing_terms(self):
        """For rho < 1, terms should decrease."""
        result = shadow_correction_series_bound(0.3, max_r=10)
        terms = [t for _, t in result['terms']]
        for i in range(1, len(terms)):
            assert terms[i] < terms[i - 1]


# ===================================================================
#  8. CLASS-BY-CLASS VERIFICATION
# ===================================================================

class TestClassByClass:
    """G=exact, L=one correction, C=two, M=infinite."""

    def test_class_G_exact(self):
        """Heisenberg: class G, zero corrections."""
        result = shadow_correction_by_class('heisenberg', Rational(1))
        assert result['class'] == 'G'
        assert result['exact'] is True
        assert result['nonzero_corrections'] == 0

    def test_class_L_one_correction(self):
        """Affine: class L, at most one correction."""
        coeffs = {3: Rational(1)}
        result = shadow_correction_by_class('affine', Rational(9, 4), coeffs)
        assert result['class'] == 'L'
        assert result['nonzero_corrections'] == 1

    def test_class_C_two_corrections(self):
        """Beta-gamma: class C, at most two corrections."""
        coeffs = {3: Rational(1), 4: Rational(-5, 12)}
        result = shadow_correction_by_class('betagamma', Rational(1), coeffs)
        assert result['class'] == 'C'
        assert result['nonzero_corrections'] <= 2

    def test_class_M_infinite(self):
        """Virasoro: class M, infinite tower."""
        coeffs = {r: Rational(1, r) for r in range(3, 9)}
        result = shadow_correction_by_class('virasoro', Rational(13, 2), coeffs)
        assert result['class'] == 'M'
        assert result['infinite_tower'] is True
        assert result['nonzero_corrections'] == 6


# ===================================================================
#  9. QES CONDITION
# ===================================================================

class TestQES:
    """Quantum extremal surface at scalar level."""

    def test_qes_virasoro_stationarity(self):
        """S_gen(c) = S(c) + S(26-c) = 26/3 is constant => stationary."""
        for c in [Rational(1), Rational(13), Rational(25)]:
            result = qes_virasoro(c)
            assert result['is_stationary']
            assert result['S_gen'] == Rational(26, 3)

    def test_qes_heisenberg_exact(self):
        """Heisenberg: exact, class G, no corrections."""
        result = qes_heisenberg(Rational(1))
        assert result['exact']
        assert result['shadow_corrections'] == 0
        assert result['S_EE'] == Rational(2, 3)

    def test_qes_affine_sl2(self):
        """Affine sl_2: class L, correction depth 3."""
        result = qes_affine_sl2(Rational(1))
        assert result['class'] == 'L'
        assert result['correction_depth'] == 3

    def test_qes_stationarity_scalar_direct(self):
        """Direct QES stationarity check."""
        result = qes_stationarity_scalar(Rational(13, 2), Rational(13, 2), 1)
        assert result['is_stationary']
        assert result['kappa_sum'] == Rational(13)


# ===================================================================
#  10. MUTUAL INFORMATION
# ===================================================================

class TestMutualInformation:
    """I(A:B) = (c/3)*log(1/eta) from cross-ratio."""

    def test_mutual_info_coefficient(self):
        """I coefficient = 2*kappa/3 = c/3."""
        kap = kappa_virasoro(Rational(1))
        assert mutual_information_scalar(kap, 0.5) == Rational(1, 3)

    def test_mutual_info_positivity(self):
        """I(A:B) > 0 for 0 < eta < 1."""
        for eta in [0.1, 0.3, 0.5, 0.9]:
            I = mutual_information_value(1.0, eta)
            assert I > 0

    def test_mutual_info_monotone_in_eta(self):
        """I decreases as eta -> 0 (intervals move apart)."""
        I_close = mutual_information_value(1.0, 0.9)
        I_far = mutual_information_value(1.0, 0.1)
        assert I_far > I_close  # log(1/0.1) > log(1/0.9)

    def test_mutual_info_complementarity(self):
        """I(c) + I(26-c) = (26/3)*log(1/eta)."""
        for c in [1.0, 5.0, 13.0, 25.0]:
            result = mutual_information_complementarity(c, 0.5)
            assert result['consistent']

    def test_mutual_info_eta_bounds(self):
        """eta must be in (0, 1)."""
        with pytest.raises(ValueError):
            mutual_information_value(1.0, 0.0)
        with pytest.raises(ValueError):
            mutual_information_value(1.0, 1.0)
        with pytest.raises(ValueError):
            mutual_information_value(1.0, 1.5)


# ===================================================================
#  11. PAGE POINT AT c=13
# ===================================================================

class TestPageCurve:
    """Page transition at c=13 for Virasoro."""

    def test_page_point(self):
        """Page point is c=13."""
        data = page_transition_virasoro()
        assert data['page_point_c'] == Rational(13)
        assert data['self_dual'] is True

    def test_page_curve_sub_page(self):
        """For c < 13: S(A) < S(A!)."""
        result = page_curve_virasoro(Rational(1))
        assert result['phase'] == 'sub-Page'
        assert result['S_A'] < result['S_dual']

    def test_page_curve_super_page(self):
        """For c > 13: S(A) > S(A!)."""
        result = page_curve_virasoro(Rational(25))
        assert result['phase'] == 'super-Page'
        assert result['S_A'] > result['S_dual']

    def test_page_curve_at_page_point(self):
        """At c=13: S(A) = S(A!)."""
        result = page_curve_virasoro(Rational(13))
        assert result['at_page_point']
        assert result['S_A'] == result['S_dual']
        assert result['S_A'] == Rational(13, 3)

    def test_page_total_constant(self):
        """S_A + S_dual = 26/3 at all c."""
        for c in [Rational(1), Rational(6), Rational(13), Rational(25)]:
            result = page_curve_virasoro(c)
            assert result['S_total'] == Rational(26, 3)

    def test_page_curve_table(self):
        """Table has 10 entries, all with correct total."""
        table = page_curve_table()
        assert len(table) == 10
        for entry in table:
            assert entry['S_total'] == Rational(26, 3)

    def test_page_self_duality_verification(self):
        """verify_page_point_self_duality returns consistent results."""
        result = verify_page_point_self_duality()
        assert result['equal']
        assert result['page_condition']
        assert result['S_EE'] == Rational(13, 3)


# ===================================================================
#  12. ENTANGLEMENT CAPACITY
# ===================================================================

class TestEntanglementCapacity:
    """C_E = T_E * dS/dT_E."""

    def test_capacity_scalar_virasoro(self):
        """|C_E| = 2*kappa/3 = c/3."""
        kap = kappa_virasoro(Rational(13))
        assert entanglement_capacity_scalar(kap) == Rational(13, 3)

    def test_capacity_heisenberg(self):
        """|C_E| = 2/3 for Heisenberg kappa=1."""
        kap = kappa_heisenberg(Rational(1))
        assert entanglement_capacity_scalar(kap) == Rational(2, 3)

    def test_capacity_equals_calabrese_cardy(self):
        """|C_E| = S_EE coefficient (the Calabrese-Cardy coefficient)."""
        for c in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            kap = kappa_virasoro(c)
            c_e = entanglement_capacity_scalar(kap)
            s_coeff = von_neumann_entropy_scalar(kap, 1)
            assert c_e == s_coeff

    def test_capacity_shadow_corrected(self):
        """Shadow corrections add sub-leading terms to C_E."""
        kap = kappa_virasoro(Rational(13))
        coeffs = {3: Rational(2), 4: Rational(10, 143)}
        result = entanglement_capacity_shadow_corrected(kap, coeffs)
        assert result['scalar'] == Rational(13, 3)
        assert 3 in result['corrections']
        assert 4 in result['corrections']


# ===================================================================
#  13. REPLICA Z_n POSITIVITY
# ===================================================================

class TestReplicaPositivity:
    """Z_n > 0 always."""

    @pytest.mark.parametrize("n", [2, 3, 4, 5, 10, 100])
    def test_replica_positivity(self, n):
        """Z_n = exp(real) > 0."""
        kappa = 6.5  # c=13
        Z = replica_partition_function_value(kappa, n, 1.0)
        assert Z > 0

    def test_replica_normalization(self):
        """Z_1 = 1 (normalization)."""
        kappa = 6.5
        Z1 = replica_partition_function_value(kappa, 1, 1.0)
        assert abs(Z1 - 1.0) < 1e-12

    def test_replica_decreasing(self):
        """Z_n decreases for increasing n (kappa > 0)."""
        kappa = 6.5
        Z_prev = replica_partition_function_value(kappa, 2, 1.0)
        for n in [3, 5, 10]:
            Z_n = replica_partition_function_value(kappa, n, 1.0)
            assert Z_n < Z_prev
            Z_prev = Z_n


# ===================================================================
#  14. GROWTH BOUND (CARLSON THEOREM)
# ===================================================================

class TestCarlsonBound:
    """|Z_n| bounded for Carlson's theorem."""

    @pytest.mark.parametrize("n", [2, 3, 5, 10, 50, 100])
    def test_carlson_satisfied(self, n):
        """Z_n satisfies Carlson bound for all tested n."""
        kappa = 6.5
        result = replica_growth_bound(kappa, n, 1.0)
        assert result['satisfies_carlson']

    def test_growth_rate_negative(self):
        """Growth rate is negative for kappa > 0 (Z_n decays)."""
        kappa = 6.5
        result = replica_growth_bound(kappa, 10, 1.0)
        assert result['growth_rate'] < 0

    def test_carlson_large_n(self):
        """Even at large n, Carlson is satisfied."""
        result = replica_growth_bound(13.0, 200, 2.0)
        assert result['satisfies_carlson']


# ===================================================================
#  15. ENTANGLEMENT SPECTRUM SPACING
# ===================================================================

class TestEntanglementSpectrum:
    """Entanglement spectrum from modular Hamiltonian."""

    def test_spacing_universal(self):
        """Delta_E = h_2 - h_1 (independent of c)."""
        for c in [Rational(1), Rational(13), Rational(26)]:
            spacing = entanglement_spectrum_spacing(c, 0, 1)
            assert spacing == 1

    def test_vacuum_energy(self):
        """E_0 = -c/24 for the vacuum (h=0)."""
        for c in [Rational(1), Rational(13), Rational(26)]:
            E = entanglement_energy(c, 0)
            assert E == -Rational(c) / 24

    def test_eigenvalue_positivity(self):
        """All eigenvalues are positive."""
        for c in [1.0, 13.0, 26.0]:
            for h in [0.0, 0.5, 1.0, 2.0]:
                lam = entanglement_eigenvalue(c, h)
                assert lam > 0

    def test_spectrum_ordering(self):
        """Eigenvalues decrease with increasing h."""
        c = 13.0
        primaries = [0.0, 0.5, 1.0, 2.0, 3.0]
        spectrum = entanglement_spectrum_primaries(c, primaries)
        lambdas = [s['lambda'] for s in spectrum]
        for i in range(len(lambdas) - 1):
            assert lambdas[i] >= lambdas[i + 1]

    def test_spectrum_primaries(self):
        """Full spectrum for a few primaries."""
        spectrum = entanglement_spectrum_primaries(Rational(1), [0, 1, 2])
        assert len(spectrum) == 3
        assert all('h' in s and 'E' in s and 'lambda' in s for s in spectrum)


# ===================================================================
#  16. MODULAR FLOW
# ===================================================================

class TestModularFlow:
    """Bisognano-Wichmann modular flow."""

    def test_flow_fixed_points(self):
        """phi_t(0) = 0 and phi_t(1) = 1 for all t."""
        for t in [0.0, 1.0, 5.0, 10.0]:
            assert abs(modular_flow_orbit(0.0, t) - 0.0) < 1e-14
            assert abs(modular_flow_orbit(1.0, t) - 1.0) < 1e-14

    def test_flow_identity_at_t0(self):
        """phi_0(x) = x."""
        for x in [0.1, 0.3, 0.5, 0.7, 0.9]:
            assert abs(modular_flow_orbit(x, 0.0) - x) < 1e-14

    def test_flow_monotone(self):
        """phi_t(x) is monotonically increasing in t for x in (0, 1)."""
        x = 0.3
        prev = modular_flow_orbit(x, 0.0)
        for t in [1.0, 2.0, 5.0, 10.0]:
            curr = modular_flow_orbit(x, t)
            assert curr >= prev
            prev = curr

    def test_flow_approaches_1(self):
        """phi_t(x) -> 1 as t -> infinity for x in (0, 1)."""
        x = 0.1
        large_t = modular_flow_orbit(x, 50.0)
        assert abs(large_t - 1.0) < 0.01

    def test_flow_velocity_endpoints(self):
        """v(0) = v(1) = 0 (fixed point velocity vanishes)."""
        assert modular_flow_velocity_scalar(0) == 0
        assert modular_flow_velocity_scalar(1) == 0

    def test_flow_velocity_midpoint(self):
        """v(1/2) = 1/4 (maximum)."""
        assert modular_flow_velocity_scalar(Rational(1, 2)) == Rational(1, 4)

    def test_flow_period(self):
        """beta_eff = 2*pi*L."""
        assert modular_flow_period(1) == 2 * pi

    def test_flow_verification(self):
        """Full fixed-point verification."""
        results = verify_modular_flow_fixed_points()
        for t_val, data in results.items():
            assert abs(data['phi_0']) < 1e-14
            assert abs(data['phi_1'] - 1.0) < 1e-14


# ===================================================================
#  17. REPLICA FACTORS
# ===================================================================

class TestReplicaFactors:
    """Genus-level replica factors."""

    def test_replica_factor_genus0_n2(self):
        """R_0(2) = 2 - 1/2 = 3/2."""
        assert replica_factor_genus0(2) == Rational(3, 2)

    def test_replica_factor_genus0_n1(self):
        """R_0(1) = 1 - 1 = 0 (normalization)."""
        assert replica_factor_genus0(1) == 0

    def test_replica_factor_genus1_n2(self):
        """R_1(2) = (4-1)/(24) = 3/24 = 1/8."""
        assert replica_factor_genus1(2) == Rational(1, 8)

    def test_replica_factor_genus1_n1(self):
        """R_1(1) = (1-1)/12 = 0."""
        assert replica_factor_genus1(1) == 0

    def test_replica_full_scalar_consistency(self):
        """Full replica log Z_n^{scalar} matches direct formula."""
        kappa = Rational(13, 2)
        for n in [2, 3, 5]:
            result = replica_log_partition_full(kappa, n, 1)
            expected_scalar = -(kappa / 3) * (Rational(n) - Rational(1, n))
            assert result['scalar'] == expected_scalar


# ===================================================================
#  18. RENYI WITH SHADOW CORRECTIONS
# ===================================================================

class TestRenyiShadowCorrected:
    """Renyi entropy with shadow obstruction tower corrections."""

    def test_no_corrections_matches_scalar(self):
        """Without shadow coefficients, S_n = S_n^{scalar}."""
        kappa = Rational(13, 2)
        for n in [2, 3, 5]:
            result = renyi_entropy_with_shadow(kappa, n, 1)
            expected = renyi_entropy_scalar(kappa, n, 1)
            assert result['scalar'] == expected
            assert result['total_leading'] == expected

    def test_shadow_corrections_subleading(self):
        """Shadow corrections are sub-leading (don't contribute to log term)."""
        kappa = Rational(13, 2)
        coeffs = {3: Rational(2), 4: Rational(10, 143)}
        result = renyi_entropy_with_shadow(kappa, 2, 1, coeffs)
        assert result['total_leading'] == result['scalar']

    def test_von_neumann_shadow_corrected_structure(self):
        """Von Neumann with shadow corrections has correct structure."""
        kappa = Rational(13, 2)
        coeffs = {3: Rational(2), 4: Rational(10, 143)}
        result = von_neumann_shadow_corrected(kappa, 1, coeffs)
        assert result['scalar'] == Rational(13, 3)
        assert 3 in result['corrections']
        assert 4 in result['corrections']


# ===================================================================
#  19. ENTANGLEMENT TEMPERATURE
# ===================================================================

class TestEntanglementTemperature:
    """T_E = 1/(2*pi*L)."""

    def test_temperature_L1(self):
        """T_E = 1/(2*pi) for L=1."""
        assert entanglement_temperature(1) == 1 / (2 * pi)

    def test_temperature_numerical(self):
        """Numerical temperature check."""
        T = entanglement_temperature_numerical(1.0)
        assert abs(T - 1.0 / (2 * math.pi)) < 1e-12

    def test_temperature_scales_inversely(self):
        """T_E(2L) = T_E(L)/2."""
        T1 = entanglement_temperature_numerical(1.0)
        T2 = entanglement_temperature_numerical(2.0)
        assert abs(T2 - T1 / 2.0) < 1e-12


# ===================================================================
#  20. GENUS-g STRUCTURE
# ===================================================================

class TestGenusStructure:
    """Genus-g free energy and entanglement corrections."""

    def test_genus1_free_energy(self):
        """F_1(A) = kappa * 1/24."""
        kap = Rational(13, 2)
        assert genus_g_free_energy(kap, 1) == kap * Rational(1, 24)

    def test_genus2_free_energy(self):
        """F_2(A) = kappa * 7/5760."""
        kap = Rational(13, 2)
        assert genus_g_free_energy(kap, 2) == kap * Rational(7, 5760)

    def test_genus_correction_g1(self):
        """delta_S^{(1)} = 2 * kappa * lambda_1."""
        kap = Rational(13, 2)
        expected = 2 * kap * faber_pandharipande(1)
        assert genus_g_entanglement_correction(kap, 1, 1) == expected

    def test_genus_expansion_structure(self):
        """Total expansion has correct structure."""
        kap = Rational(13, 2)
        result = total_genus_expansion(kap, max_genus=3)
        assert result['scalar'] == Rational(13, 3)
        assert 1 in result['genus_corrections']
        assert 2 in result['genus_corrections']
        assert 3 in result['genus_corrections']


# ===================================================================
#  21. CROSS-FAMILY CENSUS
# ===================================================================

class TestCrossFamilyCensus:
    """Complete entanglement census."""

    def test_census_has_all_families(self):
        """Census includes at least 8 families."""
        census = cross_family_census()
        assert len(census) >= 8

    def test_census_positive_kappa(self):
        """All families with positive kappa have positive S_EE coefficient."""
        census = cross_family_census()
        for f in census:
            if f['kappa'] > 0:
                assert f['S_EE_coeff'] > 0

    def test_census_class_G_exact(self):
        """Class G families are marked as exact."""
        census = cross_family_census()
        for f in census:
            if f['class'] == 'G':
                assert f['exact'] is True

    def test_census_consistency(self):
        """S_EE_coeff = K_coeff = C_E for all families."""
        census = cross_family_census()
        for f in census:
            assert f['S_EE_coeff'] == f['K_coeff']
            assert f['S_EE_coeff'] == f['C_E']


# ===================================================================
#  22. SHADOW FLOW CORRECTIONS
# ===================================================================

class TestShadowFlowCorrections:
    """Shadow corrections to modular flow velocity."""

    def test_shadow_correction_at_midpoint(self):
        """Shadow correction coefficient at x=1/2."""
        S_r = Rational(1)
        r = 3
        corr = modular_flow_velocity_shadow_correction(S_r, r, Rational(1, 2))
        assert corr == Rational(1, 8)  # S_r * (1/2)^3

    def test_shadow_correction_decreasing_in_r(self):
        """Higher arity corrections are smaller at midpoint."""
        S_r = Rational(1)
        prev = abs(float(modular_flow_velocity_shadow_correction(S_r, 3, Rational(1, 2))))
        for r in [4, 5, 6, 7]:
            curr = abs(float(modular_flow_velocity_shadow_correction(S_r, r, Rational(1, 2))))
            assert curr < prev
            prev = curr
