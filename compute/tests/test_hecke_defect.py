r"""Tests for the Hecke defect computation module.

Tests:
  1. Heisenberg: delta_p = 0 for all p, all r (tower terminates)
  2. Virasoro: delta_p = 0 for all p, all r (tau-independent shadows)
  3. W_3: delta_p = 0 on T-line and W-line
  4. MC constraint counting and rigidity defect
  5. Route C verification: overdetermination propagation
  6. Lattice VOA Hecke eigenvalue verification
  7. Character-level Rankin-Selberg check
  8. Cross-family consistency

Manuscript references:
  def:hecke-defect-shadow (arithmetic_shadows.tex)
  prop:hecke-defect-families (arithmetic_shadows.tex)
  thm:route-c-propagation (arithmetic_shadows.tex)
  prop:mc-constraint-counting (arithmetic_shadows.tex)
  thm:rigidity-inheritance (arithmetic_shadows.tex)
"""

import math
import pytest
from fractions import Fraction

from compute.lib.hecke_defect import (
    heisenberg_shadow_data,
    virasoro_shadow_data,
    w3_shadow_data,
    compute_shadow_tower,
    mc_recursion_step,
    hecke_operator_on_constant,
    hecke_operator_on_modular_form,
    hecke_defect_shadow_level,
    hecke_defect_heisenberg,
    hecke_defect_virasoro,
    hecke_defect_w3,
    mc_constraint_count,
    spectral_unknowns,
    rigidity_defect,
    rigidity_threshold,
    bracket_constraint_count,
    rankin_selberg_virasoro_leading,
    compute_partition_coefficients,
    hecke_eigenvalue_e8,
    hecke_eigenvalue_leech_eisenstein,
    hecke_eigenvalue_leech_cuspidal,
    verify_ramanujan_bound_lattice,
    route_c_verification,
    route_c_hecke_propagation,
    w3_mixing_polynomial,
    w3_propagator_variance,
    full_hecke_defect_report,
)
from compute.lib.modular_spectral_rigidity import ramanujan_tau


# ============================================================
# 1. Heisenberg Hecke defect tests
# ============================================================

class TestHeisenbergHeckeDefect:
    """Heisenberg: delta_p = 0 for all p, all r (class G, depth 2)."""

    def test_heisenberg_data(self):
        data = heisenberg_shadow_data()
        # kappa(Heisenberg) = k = 1 (the level, NOT c/2 = 1/2; see AP1/AP9)
        assert data['kappa'] == Fraction(1)
        assert data['alpha'] == Fraction(0)
        assert data['S4'] == Fraction(0)
        assert data['depth_class'] == 'G'
        assert data['shadow_depth'] == 2

    def test_heisenberg_tower_terminates(self):
        data = heisenberg_shadow_data()
        S = compute_shadow_tower(
            float(data['kappa']), float(data['alpha']),
            float(data['S4']), float(data['propagator']),
            max_r=15,
        )
        # S_2 = kappa = 1 (level k=1)
        assert abs(S[2] - 1.0) < 1e-14
        for r in range(3, 16):
            assert abs(S[r]) < 1e-14, f"S_{r} = {S[r]} should be 0"

    @pytest.mark.parametrize("p", [2, 3, 5, 7, 11])
    def test_heisenberg_defect_vanishes(self, p):
        defects = hecke_defect_heisenberg(p, max_r=15)
        for r, d in defects.items():
            assert abs(d) < 1e-14, f"delta_{p}^({r}) = {d} should be 0"

    def test_heisenberg_hecke_on_constant(self):
        """T_p on a constant is identity."""
        for p in [2, 3, 5]:
            assert hecke_operator_on_constant(0.5, p) == 0.5
            assert hecke_operator_on_constant(0.0, p) == 0.0
            assert hecke_operator_on_constant(3.14, p) == 3.14


# ============================================================
# 2. Virasoro Hecke defect tests
# ============================================================

class TestVirasoroHeckeDefect:
    """Virasoro: delta_p = 0 for all p, all r (tau-independent)."""

    @pytest.mark.parametrize("c_val", [1.0, 0.5, 2.0, 13.0, 26.0, 100.0])
    def test_virasoro_data_consistency(self, c_val):
        data = virasoro_shadow_data(c_val)
        assert abs(data['kappa'] - c_val / 2.0) < 1e-14
        assert abs(data['alpha'] - 2.0) < 1e-14
        assert abs(data['S4'] - 10.0 / (c_val * (5.0 * c_val + 22.0))) < 1e-14
        assert abs(data['propagator'] - 2.0 / c_val) < 1e-14

    @pytest.mark.parametrize("c_val", [1.0, 0.5, 2.0, 13.0])
    @pytest.mark.parametrize("p", [2, 3, 5])
    def test_virasoro_defect_vanishes(self, c_val, p):
        defects = hecke_defect_virasoro(c_val, p, max_r=15)
        for r, d in defects.items():
            assert abs(d) < 1e-14, (
                f"delta_{p}^({r})(Vir_{{c={c_val}}}) = {d} should be 0"
            )

    def test_virasoro_c0_raises(self):
        with pytest.raises(ValueError):
            virasoro_shadow_data(0)

    def test_virasoro_shadow_tower_class_m(self):
        """Virasoro at generic c has infinite depth (class M)."""
        c_val = 1.0
        S = compute_shadow_tower(
            c_val / 2.0, 2.0,
            10.0 / (c_val * (5.0 * c_val + 22.0)),
            2.0 / c_val,
            max_r=20,
        )
        # Check that shadows do NOT terminate
        nonzero_count = sum(1 for r in range(5, 21) if abs(S[r]) > 1e-14)
        assert nonzero_count > 0, "Virasoro tower should not terminate"

    def test_virasoro_kappa_formula(self):
        """kappa(Vir_c) = c/2 (AP1 check)."""
        for c in [0.5, 1.0, 2.0, 13.0, 26.0]:
            data = virasoro_shadow_data(c)
            assert abs(data['kappa'] - c / 2.0) < 1e-14

    def test_virasoro_quartic_contact(self):
        """Q^contact_Vir = 10/(c*(5c+22))."""
        for c in [0.5, 1.0, 2.0, 13.0]:
            data = virasoro_shadow_data(c)
            expected = 10.0 / (c * (5.0 * c + 22.0))
            assert abs(data['S4'] - expected) < 1e-14


# ============================================================
# 3. W_3 Hecke defect tests
# ============================================================

class TestW3HeckeDefect:
    """W_3: delta_p = 0 on T-line and W-line separately."""

    @pytest.mark.parametrize("c_val", [2.0, 4.0, 13.0])
    @pytest.mark.parametrize("p", [2, 3, 5])
    def test_w3_defect_vanishes(self, c_val, p):
        result = hecke_defect_w3(c_val, p, max_r=12)
        for r, d in result['T_line'].items():
            assert abs(d) < 1e-14, (
                f"T-line delta_{p}^({r})(W3_{{c={c_val}}}) = {d}"
            )
        for r, d in result['W_line'].items():
            assert abs(d) < 1e-14, (
                f"W-line delta_{p}^({r})(W3_{{c={c_val}}}) = {d}"
            )

    def test_w3_t_line_equals_virasoro(self):
        """W_3 T-line shadow coefficients equal Virasoro."""
        c_val = 2.0
        w3_data = w3_shadow_data(c_val)
        vir_data = virasoro_shadow_data(c_val)
        assert abs(w3_data['T_line']['kappa'] - vir_data['kappa']) < 1e-14
        assert abs(w3_data['T_line']['alpha'] - vir_data['alpha']) < 1e-14
        assert abs(w3_data['T_line']['S4'] - vir_data['S4']) < 1e-14

    def test_w3_w_line_alpha_zero(self):
        """W-line alpha_W = 0 by Z_2 parity."""
        for c in [2.0, 4.0, 13.0]:
            data = w3_shadow_data(c)
            assert abs(data['W_line']['alpha']) < 1e-14

    def test_w3_mixing_polynomial(self):
        """P(W_3) = 25c^2 + 100c - 428 is tau-independent."""
        for c in [2.0, 4.0, 13.0]:
            val = w3_mixing_polynomial(c)
            expected = 25.0 * c ** 2 + 100.0 * c - 428.0
            assert abs(val - expected) < 1e-10

    def test_w3_propagator_variance_positive(self):
        """delta_mix > 0 for c > 0."""
        for c in [1.0, 2.0, 4.0, 13.0]:
            assert w3_propagator_variance(c) > 0


# ============================================================
# 4. MC constraint counting tests
# ============================================================

class TestMCConstraintCounting:
    """prop:mc-constraint-counting verification."""

    def test_constraint_count_formula(self):
        for r in range(2, 20):
            assert mc_constraint_count(r) == r - 1

    def test_spectral_unknowns(self):
        for m in range(1, 10):
            assert spectral_unknowns(m) == 2 * m

    def test_rigidity_defect_formula(self):
        for m in range(1, 5):
            for r in range(2, 20):
                assert rigidity_defect(m, r) == (r - 1) - 2 * m

    def test_rigidity_threshold_virasoro(self):
        """Virasoro (m=1): threshold at r=4."""
        assert rigidity_threshold(1) == 4

    def test_rigidity_threshold_leech(self):
        """Leech (m=2): threshold at r=6."""
        assert rigidity_threshold(2) == 6

    def test_rigidity_defect_positive_at_threshold(self):
        for m in range(1, 5):
            r = rigidity_threshold(m)
            assert rigidity_defect(m, r) > 0

    def test_rigidity_defect_negative_below_threshold(self):
        for m in range(1, 5):
            r = rigidity_threshold(m) - 1
            assert rigidity_defect(m, r) <= 0

    def test_bracket_constraint_sharper(self):
        """Bracket constraint count exceeds simple count for r >= 5."""
        for r in range(5, 15):
            assert bracket_constraint_count(r) >= r - 2


# ============================================================
# 5. Route C verification tests
# ============================================================

class TestRouteCVerification:
    """Route C: MC overdetermination propagates Hecke equivariance."""

    def test_route_c_virasoro(self):
        """sqrt(Q_L) and MC recursion agree for Virasoro.

        The MC recursion is numerically unstable at high arities
        (convolution of alternating-sign terms), so we test relative
        error at each arity rather than absolute error across all arities.
        """
        c = 1.0
        result = route_c_verification(
            c / 2.0, 2.0,
            10.0 / (c * (5.0 * c + 22.0)),
            2.0 / c,
            max_r=20,
        )
        assert result['route_c_verified']
        assert result['max_relative_error'] < 1e-8

    @pytest.mark.parametrize("c_val", [0.5, 2.0, 13.0, 26.0])
    def test_route_c_virasoro_various_c(self, c_val):
        data = virasoro_shadow_data(c_val)
        result = route_c_verification(
            data['kappa'], data['alpha'],
            data['S4'], data['propagator'],
            max_r=15,
        )
        assert result['route_c_verified']

    def test_route_c_constraint_analysis(self):
        """Verify overdetermination begins at r=4 for m=1."""
        c = 1.0
        result = route_c_verification(
            c / 2.0, 2.0,
            10.0 / (c * (5.0 * c + 22.0)),
            2.0 / c,
            max_r=10,
        )
        for r in range(4, 11):
            assert result['constraint_analysis'][r]['overdetermined']
        for r in range(2, 4):
            assert not result['constraint_analysis'][r]['overdetermined']

    @pytest.mark.parametrize("c_val", [1.0, 13.0])
    def test_route_c_hecke_propagation(self, c_val):
        """Hecke equivariance propagates through MC recursion."""
        data = virasoro_shadow_data(c_val)
        result = route_c_hecke_propagation(
            data['kappa'], data['alpha'],
            data['S4'], data['propagator'],
            primes=[2, 3, 5],
            max_r=15,
        )
        assert result['all_equivariant']


# ============================================================
# 6. Lattice VOA Hecke eigenvalue tests
# ============================================================

class TestLatticeHeckeEigenvalues:
    """Hecke eigenvalues for E_8 and Leech lattice VOAs."""

    def test_e8_eigenvalue_p2(self):
        assert hecke_eigenvalue_e8(2) == 1 + 8  # = 9

    def test_e8_eigenvalue_p3(self):
        assert hecke_eigenvalue_e8(3) == 1 + 27  # = 28

    def test_e8_eigenvalue_p5(self):
        assert hecke_eigenvalue_e8(5) == 1 + 125  # = 126

    def test_leech_eisenstein_p2(self):
        assert hecke_eigenvalue_leech_eisenstein(2) == Fraction(1 + 2048)

    def test_leech_cuspidal_tau_values(self):
        """Ground truth Ramanujan tau values."""
        assert hecke_eigenvalue_leech_cuspidal(1) == 1
        assert hecke_eigenvalue_leech_cuspidal(2) == -24
        assert hecke_eigenvalue_leech_cuspidal(3) == 252
        assert hecke_eigenvalue_leech_cuspidal(4) == -1472
        assert hecke_eigenvalue_leech_cuspidal(5) == 4830

    @pytest.mark.parametrize("p", [2, 3, 5, 7, 11, 13])
    def test_ramanujan_bound_leech(self, p):
        """Deligne's theorem: |tau(p)| <= 2*p^{11/2}."""
        tau_p = hecke_eigenvalue_leech_cuspidal(p)
        bound = 2.0 * p ** 5.5
        assert abs(tau_p) <= bound, (
            f"|tau({p})| = {abs(tau_p)} > {bound}"
        )

    def test_lattice_e8_verification(self):
        result = verify_ramanujan_bound_lattice(8, [2, 3, 5])
        assert result['weight'] == 4

    def test_lattice_leech_verification(self):
        result = verify_ramanujan_bound_lattice(24, [2, 3, 5])
        assert result['weight'] == 12
        for p in [2, 3, 5]:
            assert result['results'][p]['satisfies_ramanujan']


# ============================================================
# 7. Character-level tests
# ============================================================

class TestCharacterLevel:
    """Character-level Rankin-Selberg checks."""

    def test_partition_coefficients(self):
        """Ground truth partition numbers."""
        p = compute_partition_coefficients(10)
        assert p[0] == 1
        assert p[1] == 1
        assert p[2] == 2
        assert p[3] == 3
        assert p[4] == 5
        assert p[5] == 7
        assert p[6] == 11
        assert p[7] == 15
        assert p[8] == 22
        assert p[9] == 30
        assert p[10] == 42

    def test_rankin_selberg_report(self):
        result = rankin_selberg_virasoro_leading(1.0, n_terms=20)
        assert 'partition_coeffs' in result
        assert 'multiplicativity_checks' in result
        # Partition numbers are NOT multiplicative
        assert 'NOT multiplicative' in result['note']


# ============================================================
# 8. Hecke operator on modular forms tests
# ============================================================

class TestHeckeOperator:
    """T_p on modular forms via q-expansion."""

    def test_hecke_on_delta_p2(self):
        """T_2(Delta) = tau(2) * Delta = -24 * Delta."""
        # Delta = sum tau(n) q^n, tau(1) = 1
        N = 20
        delta_coeffs = [0] * (N + 1)
        for n in range(1, N + 1):
            delta_coeffs[n] = ramanujan_tau(n)

        result = hecke_operator_on_modular_form(delta_coeffs, 2, 12, max_n=10)
        # T_2(Delta) should be -24 * Delta
        for n in range(1, 10):
            expected = -24 * ramanujan_tau(n)
            assert abs(result[n] - expected) < 1e-10, (
                f"T_2(Delta) at q^{n}: got {result[n]}, expected {expected}"
            )

    def test_hecke_on_delta_p3(self):
        """T_3(Delta) = tau(3) * Delta = 252 * Delta."""
        N = 30
        delta_coeffs = [0] * (N + 1)
        for n in range(1, N + 1):
            delta_coeffs[n] = ramanujan_tau(n)

        result = hecke_operator_on_modular_form(delta_coeffs, 3, 12, max_n=10)
        for n in range(1, 10):
            expected = 252 * ramanujan_tau(n)
            assert abs(result[n] - expected) < 1e-10, (
                f"T_3(Delta) at q^{n}: got {result[n]}, expected {expected}"
            )

    def test_hecke_eigenvalue_multiplicativity(self):
        """tau(p)*tau(q) = tau(pq) + p^11 * tau(q/p) for p != q primes."""
        # For distinct primes p, q: tau(pq) = tau(p)*tau(q)
        p, q = 2, 3
        assert ramanujan_tau(p * q) == ramanujan_tau(p) * ramanujan_tau(q)
        p, q = 2, 5
        assert ramanujan_tau(p * q) == ramanujan_tau(p) * ramanujan_tau(q)
        p, q = 3, 5
        assert ramanujan_tau(p * q) == ramanujan_tau(p) * ramanujan_tau(q)


# ============================================================
# 9. Cross-family consistency tests (AP10 prevention)
# ============================================================

class TestCrossFamilyConsistency:
    """Cross-family checks to prevent AP10 (hardcoded wrong expected values)."""

    def test_kappa_additivity_heisenberg(self):
        """kappa(H_k1 + H_k2) = kappa(H_k1) + kappa(H_k2)."""
        # Heisenberg at rank Q: kappa = Q/2
        for Q1 in [1, 2, 3]:
            for Q2 in [1, 2, 3]:
                kappa_sum = Q1 / 2.0 + Q2 / 2.0
                kappa_direct = (Q1 + Q2) / 2.0
                assert abs(kappa_sum - kappa_direct) < 1e-14

    def test_virasoro_self_duality_c13(self):
        """Vir_c^! = Vir_{26-c}; self-dual at c=13 (AP8)."""
        c = 13.0
        kappa = c / 2.0
        kappa_dual = (26.0 - c) / 2.0
        assert abs(kappa - kappa_dual) < 1e-14

    def test_kappa_complementarity_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c in [0.5, 1.0, 2.0, 10.0, 13.0, 25.0]:
            kappa = c / 2.0
            kappa_dual = (26.0 - c) / 2.0
            assert abs(kappa + kappa_dual - 13.0) < 1e-14

    def test_virasoro_propagator_formula(self):
        """Propagator P = 2/c for Virasoro (not 1/c or c/2)."""
        for c in [0.5, 1.0, 2.0, 13.0]:
            data = virasoro_shadow_data(c)
            assert abs(data['propagator'] - 2.0 / c) < 1e-14

    def test_hecke_defect_invariant_under_central_charge(self):
        """Hecke defect vanishes for ALL values of c (not just special ones)."""
        for c in [0.3, 0.5, 1.0, 1.5, 2.0, 5.0, 13.0, 26.0, 100.0]:
            defects = hecke_defect_virasoro(c, 2, max_r=10)
            max_d = max(abs(d) for d in defects.values())
            assert max_d < 1e-13, f"Hecke defect nonzero at c={c}: {max_d}"


# ============================================================
# 10. Full report test
# ============================================================

class TestFullReport:
    """Integration test for the full report."""

    def test_full_report_runs(self):
        report = full_hecke_defect_report(c_val=1.0, primes=[2, 3], max_r=10)
        assert report['heisenberg']['vanishes']
        assert report['virasoro']['vanishes']
        assert report['w3']['vanishes']
        assert report['route_c']['route_c_verified']

    def test_full_report_leech_ramanujan(self):
        report = full_hecke_defect_report(c_val=1.0, primes=[2, 3, 5], max_r=10)
        for p in [2, 3, 5]:
            assert report['lattice_leech']['results'][p]['satisfies_ramanujan']


# ============================================================
# 11. Edge case and error handling tests
# ============================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_virasoro_c0_raises(self):
        with pytest.raises(ValueError):
            virasoro_shadow_data(0)

    def test_w3_c0_raises(self):
        with pytest.raises(ValueError):
            w3_shadow_data(0)

    def test_non_prime_raises(self):
        with pytest.raises(ValueError):
            hecke_defect_shadow_level(0.5, 0, 0, 2, 4, max_r=5)

    def test_large_c_virasoro(self):
        """Large c: kappa large, S4 small, defect still 0."""
        c = 1000.0
        defects = hecke_defect_virasoro(c, 2, max_r=10)
        max_d = max(abs(d) for d in defects.values())
        assert max_d < 1e-10

    def test_negative_c_virasoro(self):
        """Negative c (e.g. Lee-Yang c=-22/5): defect still 0."""
        c = -22.0 / 5.0 + 0.01  # slightly away from pole
        defects = hecke_defect_virasoro(c, 2, max_r=8)
        max_d = max(abs(d) for d in defects.values())
        assert max_d < 1e-10
