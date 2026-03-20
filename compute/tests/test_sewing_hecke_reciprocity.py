"""
Tests for the two-variable L-object L_A(s,u) and its Rankin-Selberg factorization.

MAIN THEOREM UNDER TEST:
    L_A(s,u) = Gamma(v) * (2pi)^{-v} * S_A(v),   v := s + u - 1

The (s,u) dependence COLLAPSES to a single variable v = s + u - 1.
This is a THEOREM (not a conjecture) because F_A^conn depends only on |q| = e^{-2pi*y}.

Test groups:
    1. S_A(v) closed-form vs Dirichlet series (5 families)
    2. Collapse: L_A(s1,u1) = L_A(s2,u2) when s1+u1 = s2+u2 (all families, 10+ pairs)
    3. Sewing-Selberg recovery at u=0 (factor of -2)
    4. Direct Mellin integration vs factored formula
    5. Heisenberg explicit formula
    6. Virasoro explicit formula
    7. W_3 explicit formula
    8. betagamma explicit formula (rank-2 lattice)
    9. Residue structure at zeta poles
   10. Functional equation structure
   11. Cross-family scaling
   12. Special values at integer v
   13. Dirichlet coefficient verification
   14. Gamma factor extraction
   15. Critical line evaluation
"""

import pytest
from mpmath import (mp, mpf, zeta, gamma as mpgamma, pi as mppi, power,
                    fabs, mpc, exp as mpexp, log as mplog, euler as euler_gamma)

mp.dps = 40

from compute.lib.sewing_hecke_reciprocity import (
    S_A, S_heisenberg, S_virasoro, S_betagamma, S_WN,
    harmonic_zeta,
    L_factored, L_heisenberg_factored, L_virasoro_factored,
    L_betagamma_factored, L_WN_factored,
    L_direct_mellin,
    sewing_selberg_heisenberg, sewing_selberg_generic,
    verify_collapse,
    completed_L, gamma_factor, S_A_from_L,
    a_A, S_A_from_coefficients, verify_S_A_formula,
    residue_at_zeta_pole,
    functional_equation_ratio,
    L_on_critical_line, L_special_values,
    cross_family_table,
    weights_for_family,
    F_conn_fast,
    verify_S_A_closed_form,
)


# =============================================================================
# Group 1: S_A(v) closed-form vs Dirichlet series
# =============================================================================

class TestSAFormula:
    """Verify that the closed-form S_A(v) matches the Dirichlet series."""

    @pytest.mark.parametrize("v", [3, 4, 5, mpf('3.7')])
    def test_heisenberg_S_formula(self, v):
        """S_H(v) = zeta(v)*zeta(v+1) matches Dirichlet series."""
        closed = S_heisenberg(v)
        series = S_A_from_coefficients([1], v, N_max=800)
        assert fabs(closed - series) / fabs(closed) < mpf('1e-5')

    def test_heisenberg_S_formula_v2(self):
        """S_H(2) matches Dirichlet series (slower convergence, larger N_max)."""
        closed = S_heisenberg(2)
        series = S_A_from_coefficients([1], 2, N_max=5000)
        assert fabs(closed - series) / fabs(closed) < mpf('1e-3')

    @pytest.mark.parametrize("v", [3, 4])
    def test_virasoro_S_formula(self, v):
        """S_Vir(v) = zeta(v+1)*(zeta(v)-1) matches Dirichlet series."""
        closed = S_virasoro(v)
        series = S_A_from_coefficients([2], v, N_max=800)
        assert fabs(closed - series) / fabs(closed) < mpf('1e-5')

    def test_virasoro_S_formula_v2(self):
        """S_Vir(2) matches Dirichlet series (slower convergence)."""
        closed = S_virasoro(2)
        series = S_A_from_coefficients([2], 2, N_max=5000)
        assert fabs(closed - series) / fabs(closed) < mpf('1e-3')

    @pytest.mark.parametrize("v", [3, 4])
    def test_betagamma_S_formula(self, v):
        """S_bg(v) = 2*zeta(v)*zeta(v+1)."""
        closed = S_betagamma(v)
        series = S_A_from_coefficients([1, 1], v, N_max=800)
        assert fabs(closed - series) / fabs(closed) < mpf('1e-5')

    def test_betagamma_S_formula_v2(self):
        """S_bg(2) matches Dirichlet series (slower convergence)."""
        closed = S_betagamma(2)
        series = S_A_from_coefficients([1, 1], 2, N_max=5000)
        assert fabs(closed - series) / fabs(closed) < mpf('1e-3')

    @pytest.mark.parametrize("v", [2, 3, 4])
    def test_W3_S_formula(self, v):
        """S_{W_3}(v) = zeta(v+1)*(2*zeta(v) - H_1(v) - H_2(v))."""
        closed = S_WN(3, v)
        generic = S_A([2, 3], v)
        assert fabs(closed - generic) < mpf('1e-30')

    @pytest.mark.parametrize("v", [2, 3])
    def test_W4_S_formula(self, v):
        """S_{W_4}(v) consistent with generic formula."""
        closed = S_WN(4, v)
        generic = S_A([2, 3, 4], v)
        assert fabs(closed - generic) < mpf('1e-30')

    def test_generic_matches_specialized_heisenberg(self):
        """S_A([1], v) = S_heisenberg(v) at v=3."""
        assert fabs(S_A([1], 3) - S_heisenberg(3)) < mpf('1e-30')

    def test_generic_matches_specialized_virasoro(self):
        """S_A([2], v) = S_virasoro(v) at v=3."""
        assert fabs(S_A([2], 3) - S_virasoro(3)) < mpf('1e-30')


# =============================================================================
# Group 2: Collapse L_A(s1,u1) = L_A(s2,u2) when s1+u1 = s2+u2
# =============================================================================

class TestCollapse:
    """The two-variable L-object depends only on v = s+u-1."""

    FAMILIES = [
        ('heisenberg', [1]),
        ('virasoro', [2]),
        ('betagamma', [1, 1]),
        ('W3', [2, 3]),
        ('affine_sl2', [1, 1, 1]),
    ]

    # Pairs with the same v = s+u-1
    COLLAPSE_PAIRS = [
        (2, 1, 1.5, 1.5),    # v=2
        (3, 0, 2, 1),        # v=2
        (3, 1, 2, 2),        # v=3
        (4, 0, 3, 1),        # v=3
        (2, 0.5, 1.5, 1),    # v=1.5
        (5, 0, 4, 1),        # v=4
        (3.5, 0.5, 2.5, 1.5),  # v=3
        (2.75, 1.25, 3.0, 1.0),  # v=3 (using exact binary fractions)
    ]

    @pytest.mark.parametrize("s1,u1,s2,u2", COLLAPSE_PAIRS)
    @pytest.mark.parametrize("name,weights", FAMILIES)
    def test_collapse(self, name, weights, s1, u1, s2, u2):
        """L_A(s1,u1) = L_A(s2,u2) when s1+u1 = s2+u2."""
        res = verify_collapse(weights, s1, u1, s2, u2, name)
        assert res['match'], f"{name} at v={res['v']}: ratio={float(res['ratio'])}"


# =============================================================================
# Group 3: Sewing-Selberg recovery at u=0
# =============================================================================

class TestSewingSelbergRecovery:
    """Sewing-Selberg = -2 * L_A(s, 0)."""

    @pytest.mark.parametrize("s", [3, 4, 5, 6])
    def test_heisenberg_ratio(self, s):
        """sewing_selberg_H(s) / L_H(s,0) = -2."""
        ss = sewing_selberg_heisenberg(s)
        lh = L_heisenberg_factored(s, 0)
        ratio = ss / lh
        assert fabs(ratio - (-2)) < mpf('1e-20'), f"ratio = {float(ratio)}"

    @pytest.mark.parametrize("s", [3, 4, 5])
    def test_virasoro_ratio(self, s):
        """sewing_selberg_Vir(s) / L_Vir(s,0) = -2."""
        ss = sewing_selberg_generic([2], s)
        lv = L_virasoro_factored(s, 0)
        ratio = ss / lv
        assert fabs(ratio - (-2)) < mpf('1e-20')

    @pytest.mark.parametrize("s", [3, 4, 5])
    def test_W3_ratio(self, s):
        """sewing_selberg_{W_3}(s) / L_{W_3}(s,0) = -2."""
        ss = sewing_selberg_generic([2, 3], s)
        lw = L_WN_factored(3, s, 0)
        ratio = ss / lw
        assert fabs(ratio - (-2)) < mpf('1e-20')

    def test_sewing_selberg_explicit_heisenberg(self):
        """At s=3: SS_H = -2*(2pi)^{-2}*Gamma(2)*zeta(2)*zeta(3)."""
        s = mpf(3)
        expected = -2 * power(2 * mppi, -2) * mpgamma(2) * zeta(2) * zeta(3)
        actual = sewing_selberg_heisenberg(s)
        assert fabs(actual - expected) < mpf('1e-25')


# =============================================================================
# Group 4: Direct Mellin integration vs factored formula
# =============================================================================

class TestDirectMellin:
    """Compare direct numerical integration with the factored formula."""

    @pytest.mark.parametrize("s,u", [(3, 1), (4, 1), (3, 2)])
    def test_heisenberg_mellin_vs_factored(self, s, u):
        """Direct Mellin integral matches factored form for Heisenberg."""
        mp.dps = 30
        factored = L_heisenberg_factored(s, u)
        direct = L_direct_mellin([1], s, u, terms=150)
        rel_err = fabs(factored - direct) / fabs(factored)
        assert rel_err < mpf('0.01'), f"rel_err = {float(rel_err)}"

    @pytest.mark.parametrize("s,u", [(3, 1), (4, 1)])
    def test_virasoro_mellin_vs_factored(self, s, u):
        """Direct Mellin integral matches factored form for Virasoro."""
        mp.dps = 30
        factored = L_virasoro_factored(s, u)
        direct = L_direct_mellin([2], s, u, terms=150)
        rel_err = fabs(factored - direct) / fabs(factored)
        assert rel_err < mpf('0.01'), f"rel_err = {float(rel_err)}"


# =============================================================================
# Group 5: Heisenberg explicit formula
# =============================================================================

class TestHeisenbergExplicit:
    """L_H(s,u) = Gamma(v)/(2pi)^v * zeta(v)*zeta(v+1), v=s+u-1."""

    def test_v2(self):
        """L_H at v=2: Gamma(2)/(2pi)^2 * zeta(2)*zeta(3)."""
        expected = mpgamma(2) * power(2 * mppi, -2) * zeta(2) * zeta(3)
        actual = L_heisenberg_factored(2, 1)
        assert fabs(actual - expected) < mpf('1e-25')

    def test_v3(self):
        """L_H at v=3: Gamma(3)/(2pi)^3 * zeta(3)*zeta(4)."""
        expected = mpgamma(3) * power(2 * mppi, -3) * zeta(3) * zeta(4)
        actual = L_heisenberg_factored(3, 1)
        assert fabs(actual - expected) < mpf('1e-25')

    def test_v4(self):
        """L_H at v=4: Gamma(4)/(2pi)^4 * zeta(4)*zeta(5)."""
        expected = mpgamma(4) * power(2 * mppi, -4) * zeta(4) * zeta(5)
        actual = L_heisenberg_factored(4, 1)
        assert fabs(actual - expected) < mpf('1e-25')

    def test_heisenberg_factored_equals_generic(self):
        """L_heisenberg_factored = L_factored([1], ...)."""
        for s, u in [(2, 1), (3, 0), (1.5, 1.5)]:
            lh = L_heisenberg_factored(s, u)
            lg = L_factored([1], s, u)
            assert fabs(lh - lg) < mpf('1e-25')

    def test_heisenberg_S_is_zeta_product(self):
        """S_H(v) = zeta(v)*zeta(v+1) for several v."""
        for v in [2, 3, 4, mpf('2.5')]:
            assert fabs(S_heisenberg(v) - zeta(v) * zeta(v + 1)) < mpf('1e-30')


# =============================================================================
# Group 6: Virasoro explicit formula
# =============================================================================

class TestVirasoroExplicit:
    """L_Vir(s,u) = Gamma(v)/(2pi)^v * zeta(v+1)*(zeta(v)-1), v=s+u-1."""

    def test_v2(self):
        """L_Vir at v=2: Gamma(2)/(2pi)^2 * zeta(3)*(zeta(2)-1)."""
        v = mpf(2)
        expected = mpgamma(v) * power(2 * mppi, -v) * zeta(3) * (zeta(2) - 1)
        actual = L_virasoro_factored(2, 1)
        assert fabs(actual - expected) < mpf('1e-25')

    def test_v3(self):
        """L_Vir at v=3."""
        v = mpf(3)
        expected = mpgamma(v) * power(2 * mppi, -v) * zeta(4) * (zeta(3) - 1)
        actual = L_virasoro_factored(3, 1)
        assert fabs(actual - expected) < mpf('1e-25')

    def test_virasoro_factored_equals_generic(self):
        """L_virasoro_factored = L_factored([2], ...)."""
        for s, u in [(2, 1), (3, 0), (2.5, 0.5)]:
            lv = L_virasoro_factored(s, u)
            lg = L_factored([2], s, u)
            assert fabs(lv - lg) < mpf('1e-25')

    def test_virasoro_vs_heisenberg_ratio(self):
        """S_Vir(v)/S_H(v) = 1 - 1/zeta(v) (for all v > 1)."""
        for v in [2, 3, 4]:
            v = mpf(v)
            ratio = S_virasoro(v) / S_heisenberg(v)
            expected = 1 - 1 / zeta(v)
            assert fabs(ratio - expected) < mpf('1e-25')


# =============================================================================
# Group 7: W_3 explicit formula
# =============================================================================

class TestW3Explicit:
    """L_{W_3} with weights {2, 3}."""

    def test_W3_at_v2(self):
        """S_{W_3}(2) = zeta(3)*(2*zeta(2) - 1 - (1 + 1/4))."""
        v = mpf(2)
        # H_1(2) = 1, H_2(2) = 1 + 1/4 = 5/4
        expected = zeta(3) * (2 * zeta(2) - 1 - mpf('5') / 4)
        actual = S_WN(3, v)
        assert fabs(actual - expected) < mpf('1e-25')

    def test_W3_generic_vs_specialized(self):
        """S_A([2,3], v) = S_WN(3, v)."""
        for v in [2, 3, 4]:
            assert fabs(S_A([2, 3], v) - S_WN(3, v)) < mpf('1e-30')

    def test_W3_collapse(self):
        """W_3 satisfies collapse: L(2,1) = L(1.5,1.5)."""
        res = verify_collapse([2, 3], 2, 1, 1.5, 1.5)
        assert res['match']


# =============================================================================
# Group 8: betagamma explicit formula
# =============================================================================

class TestBetagammaExplicit:
    """betagamma: W = {1,1}, so S_bg = 2*zeta(v)*zeta(v+1)."""

    def test_betagamma_is_double_heisenberg(self):
        """S_bg(v) = 2 * S_H(v) for all v > 1."""
        for v in [2, 3, 4, mpf('2.5')]:
            assert fabs(S_betagamma(v) - 2 * S_heisenberg(v)) < mpf('1e-25')

    def test_betagamma_factored_equals_generic(self):
        """L_betagamma_factored = L_factored([1,1], ...)."""
        for s, u in [(2, 1), (3, 0)]:
            lb = L_betagamma_factored(s, u)
            lg = L_factored([1, 1], s, u)
            assert fabs(lb - lg) < mpf('1e-25')

    def test_betagamma_L_is_double_heisenberg_L(self):
        """L_bg(s,u) = 2 * L_H(s,u)."""
        for s, u in [(2, 1), (3, 1), (4, 0)]:
            lb = L_betagamma_factored(s, u)
            lh = L_heisenberg_factored(s, u)
            assert fabs(lb - 2 * lh) < mpf('1e-25')


# =============================================================================
# Group 9: Residue structure at zeta poles
# =============================================================================

class TestResidueStructure:
    """Residues of Lambda_A(v) at poles of S_A and Gamma."""

    def test_heisenberg_residue_at_v1(self):
        """Residue of Lambda_H at v=1 from zeta(v) pole."""
        # zeta(v) ~ 1/(v-1) near v=1
        # S_H(v) = zeta(v)*zeta(v+1) ~ zeta(2)/(v-1) near v=1
        # Gamma(v) ~ Gamma(1) = 1 near v=1
        # (2pi)^{-v} ~ (2pi)^{-1} near v=1
        # Residue = Gamma(1)*(2pi)^{-1} * zeta(2) = pi/12
        expected = zeta(2) / (2 * mppi)  # = pi/12
        res = residue_at_zeta_pole([1], mpf(1))
        assert fabs(res - expected) / fabs(expected) < mpf('0.01')

    def test_virasoro_residue_at_v1(self):
        """Residue of Lambda_Vir at v=1: zeta(2)*(1-1)/(2pi) -- but zeta(v)-1 vanishes
        at v=1 as well, so the pole is cancelled."""
        # S_Vir(v) = zeta(v+1)*(zeta(v)-1). At v=1: zeta(v)-1 ~ 1/(v-1) - 1 = (2-v+...)/(v-1)
        # Actually zeta(v) - 1 = 1/(v-1) + gamma - 1 + O(v-1), so pole remains
        # Residue = zeta(2) * 1 / (2pi) = pi/12
        # Actually: the (zeta(v)-1) still has a pole at v=1 since zeta(v) ~ 1/(v-1).
        # So S_Vir(v) ~ zeta(2)/(v-1) - zeta(2) near v=1.
        # Residue of S_Vir at v=1 = zeta(2) (same as Heisenberg!).
        # But wait, zeta(v)-1 = zeta(v) - 1, so it has pole 1/(v-1) minus 1.
        # Near v=1: zeta(v)-1 = 1/(v-1) + (gamma-1) + O(v-1)
        # So S_Vir ~ zeta(2) * [1/(v-1) + (gamma-1)] near v=1
        # Residue of S_Vir at v=1 = zeta(2) = pi^2/6
        # Residue of Lambda_Vir at v=1 = Gamma(1)*(2pi)^{-1}*zeta(2) = pi/12
        expected = zeta(2) / (2 * mppi)
        res = residue_at_zeta_pole([2], mpf(1))
        assert fabs(res - expected) / fabs(expected) < mpf('0.01')

    def test_W3_residue_at_v1(self):
        """W_3 has |W| = 2 generators, but the residue at v=1 depends
        on whether the harmonic corrections cancel the pole."""
        # S_{W_3}(v) = zeta(v+1)*(2*zeta(v) - H_1(v) - H_2(v))
        # Near v=1: zeta(v) ~ 1/(v-1) + gamma, H_n(v) is regular
        # Residue of (2*zeta(v) - H_1 - H_2) at v=1 = 2 (from 2*zeta)
        # So Res S_{W_3} at v=1 = 2*zeta(2)
        # Res Lambda_{W_3} at v=1 = 2*zeta(2)/(2pi) = pi/6
        expected = 2 * zeta(2) / (2 * mppi)
        res = residue_at_zeta_pole([2, 3], mpf(1))
        assert fabs(res - expected) / fabs(expected) < mpf('0.01')


# =============================================================================
# Group 10: Functional equation structure
# =============================================================================

class TestFunctionalEquation:
    """Functional equation from Eisenstein series E*(s) = E*(1-s)."""

    def test_fe_ratio_structure(self):
        """Lambda_A(v) / Lambda_A(1-v) gives a well-defined ratio."""
        # At v = 3: Lambda_H(3) / Lambda_H(-2) should be computable
        # Gamma(-2) has a pole, so this ratio diverges.
        # At v=2: Gamma(2)/(2pi)^2 * S_H(2) vs Gamma(-1)/(2pi)^{-1} * S_H(-1)
        # Gamma(-1) is a pole. So the ratio is 0 or infinity.
        # For non-integer v, we can test:
        v = mpf('2.5')
        ratio = functional_equation_ratio([1], v)
        # Just check it's finite and nonzero
        assert fabs(ratio) > mpf('1e-50')
        assert fabs(ratio) < mpf('1e50')

    def test_fe_at_half_integer(self):
        """Functional equation ratio at v = 1.5."""
        v = mpf('1.5')
        ratio = functional_equation_ratio([1], v)
        assert fabs(ratio) > mpf('1e-30')


# =============================================================================
# Group 11: Cross-family scaling
# =============================================================================

class TestCrossFamilyScaling:
    """Compare Lambda_A across families at the same v."""

    def test_betagamma_double_heisenberg_at_all_v(self):
        """Lambda_bg(v) = 2 * Lambda_H(v) for all v."""
        for v in [2, 3, 4, mpf('2.5')]:
            lbg = completed_L([1, 1], v)
            lh = completed_L([1], v)
            assert fabs(lbg - 2 * lh) < mpf('1e-25')

    def test_lattice_rank_r_is_r_times_heisenberg(self):
        """For a rank-r lattice (weights all 1): Lambda = r * Lambda_H."""
        for r in [1, 2, 3, 4, 5]:
            v = mpf(3)
            lr = completed_L([1] * r, v)
            lh = completed_L([1], v)
            assert fabs(lr - r * lh) < mpf('1e-25')

    def test_WN_ordering(self):
        """Lambda_{W_N}(v) < Lambda_{W_{N+1}}(v) for v > 1 (more generators -> larger)."""
        v = mpf(3)
        for N in range(3, 7):
            lN = completed_L(list(range(2, N + 1)), v)
            lN1 = completed_L(list(range(2, N + 2)), v)
            assert lN1 > lN


# =============================================================================
# Group 12: Special values at integer v
# =============================================================================

class TestSpecialValues:
    """Special values of Lambda_A(v) at small integer v."""

    def test_heisenberg_v2_explicit(self):
        """Lambda_H(2) = 1/(4pi^2) * zeta(2)*zeta(3) = zeta(3)/24."""
        # Gamma(2) = 1, (2pi)^{-2} = 1/(4pi^2)
        expected = zeta(2) * zeta(3) / (4 * mppi**2)
        actual = completed_L([1], 2)
        assert fabs(actual - expected) < mpf('1e-25')

    def test_heisenberg_v3_explicit(self):
        """Lambda_H(3) = 2/(2pi)^3 * zeta(3)*zeta(4) = zeta(3)*pi/720."""
        # Gamma(3) = 2
        expected = 2 * zeta(3) * zeta(4) / (2 * mppi)**3
        actual = completed_L([1], 3)
        assert fabs(actual - expected) < mpf('1e-25')

    def test_heisenberg_v4_explicit(self):
        """Lambda_H(4) = 6/(2pi)^4 * zeta(4)*zeta(5)."""
        expected = 6 * zeta(4) * zeta(5) / (2 * mppi)**4
        actual = completed_L([1], 4)
        assert fabs(actual - expected) < mpf('1e-25')

    def test_special_values_dict(self):
        """L_special_values returns the right structure."""
        sv = L_special_values([1])
        assert 2 in sv
        assert 'Lambda_A' in sv[2]
        assert sv[2]['Lambda_A'] > 0


# =============================================================================
# Group 13: Dirichlet coefficient verification
# =============================================================================

class TestDirichletCoefficients:
    """Verify the Dirichlet coefficients a_A(N)."""

    def test_heisenberg_a1(self):
        """a_H(1) = sigma_{-1}(1) = 1."""
        assert a_A([1], 1) == 1

    def test_heisenberg_a2(self):
        """a_H(2) = sigma_{-1}(2) = 1 + 1/2 = 3/2."""
        assert fabs(a_A([1], 2) - mpf('1.5')) < mpf('1e-30')

    def test_heisenberg_a6(self):
        """a_H(6) = sigma_{-1}(6) = 1 + 1/2 + 1/3 + 1/6 = 2."""
        assert fabs(a_A([1], 6) - mpf(2)) < mpf('1e-30')

    def test_virasoro_a1(self):
        """a_Vir(1) = 0 (weight starts at 2, so no N/d >= 2 for N=1)."""
        assert a_A([2], 1) == 0

    def test_virasoro_a2(self):
        """a_Vir(2) = sum_{d|2, 2/d>=2} 1/d = 1/1 = 1 (d=1, m=2>=2)."""
        assert fabs(a_A([2], 2) - mpf(1)) < mpf('1e-30')

    def test_virasoro_a3(self):
        """a_Vir(3): d|3 are {1,3}. d=1: m=3>=2, yes. d=3: m=1>=2, no. So 1."""
        assert fabs(a_A([2], 3) - mpf(1)) < mpf('1e-30')

    def test_virasoro_a4(self):
        """a_Vir(4): d|4={1,2,4}. d=1:m=4>=2 yes(1). d=2:m=2>=2 yes(1/2). d=4:m=1>=2 no. Total=3/2."""
        assert fabs(a_A([2], 4) - mpf('1.5')) < mpf('1e-30')

    def test_betagamma_a1(self):
        """a_bg(1) = 2 (two generators of weight 1)."""
        assert fabs(a_A([1, 1], 1) - mpf(2)) < mpf('1e-30')

    def test_W3_a1(self):
        """a_{W_3}(1) = 0 (min weight is 2)."""
        assert a_A([2, 3], 1) == 0

    def test_W3_a2(self):
        """a_{W_3}(2): d|2={1,2}. For w=2: d=1,m=2>=2(1); d=2,m=1>=2(no).
        For w=3: d=1,m=2>=3(no); d=2,m=1>=3(no). Total = 1."""
        assert fabs(a_A([2, 3], 2) - mpf(1)) < mpf('1e-30')

    def test_dirichlet_convergence(self):
        """Dirichlet series converges to closed form for v=3."""
        res = verify_S_A_formula([1], 3)
        assert res['rel_error'] < 1e-5


# =============================================================================
# Group 14: Gamma factor extraction
# =============================================================================

class TestGammaFactor:
    """Verify gamma factor and S_A extraction."""

    def test_gamma_factor_v2(self):
        """Gamma(2)/(2pi)^2 = 1/(4pi^2)."""
        gf = gamma_factor(2)
        expected = 1 / (4 * mppi**2)
        assert fabs(gf - expected) < mpf('1e-25')

    def test_gamma_factor_v3(self):
        """Gamma(3)/(2pi)^3 = 2/(8pi^3)."""
        gf = gamma_factor(3)
        expected = 2 / (8 * mppi**3)
        assert fabs(gf - expected) < mpf('1e-25')

    def test_S_extraction_heisenberg(self):
        """Extract S_H(3) from Lambda_H(3)."""
        v = mpf(3)
        L_val = completed_L([1], v)
        S_extracted = S_A_from_L(L_val, v)
        S_expected = S_heisenberg(v)
        assert fabs(S_extracted - S_expected) < mpf('1e-25')

    def test_S_extraction_virasoro(self):
        """Extract S_Vir(3) from Lambda_Vir(3)."""
        v = mpf(3)
        L_val = completed_L([2], v)
        S_extracted = S_A_from_L(L_val, v)
        S_expected = S_virasoro(v)
        assert fabs(S_extracted - S_expected) < mpf('1e-25')

    def test_roundtrip(self):
        """gamma_factor(v) * S_A(v) = completed_L(v)."""
        for v in [2, 3, 4]:
            gf = gamma_factor(v)
            sv = S_A([1], v)
            lv = completed_L([1], v)
            assert fabs(gf * sv - lv) < mpf('1e-25')


# =============================================================================
# Group 15: Critical line evaluation
# =============================================================================

class TestCriticalLine:
    """Evaluation on the critical line v = 1/2 + it."""

    def test_critical_line_nonzero(self):
        """Lambda_H(1/2 + it) is nonzero for small t."""
        for t in [1, 2, 5, 10]:
            val = L_on_critical_line([1], t, u=1)
            assert fabs(val) > mpf('1e-50')

    def test_critical_line_conjugate_symmetry(self):
        """Lambda_A(1/2 + it) = conj(Lambda_A(1/2 - it))."""
        # For real coefficients, the Dirichlet series satisfies
        # L(conj(s)) = conj(L(s)). Since S_A has real coefficients,
        # S_A(1/2+it) = conj(S_A(1/2-it)).
        # The Gamma factor is also conjugate-symmetric.
        t = mpf(3)
        val_pos = L_on_critical_line([1], t)
        val_neg = L_on_critical_line([1], -t)
        # Should be complex conjugates
        diff_val = fabs(val_pos - val_neg.conjugate())
        scale = fabs(val_pos)
        assert diff_val / scale < mpf('1e-15')


# =============================================================================
# Additional tests for completeness
# =============================================================================

class TestHarmonicZeta:
    """Test the harmonic zeta function H_n(v)."""

    def test_H0(self):
        """H_0(v) = 0."""
        assert harmonic_zeta(0, 2) == 0

    def test_H1(self):
        """H_1(v) = 1."""
        assert fabs(harmonic_zeta(1, 2) - 1) < mpf('1e-30')

    def test_H2_at_v2(self):
        """H_2(2) = 1 + 1/4 = 5/4."""
        assert fabs(harmonic_zeta(2, 2) - mpf('1.25')) < mpf('1e-30')

    def test_zeta_minus_H(self):
        """zeta(v) - H_{n-1}(v) = sum_{m>=n} m^{-v} (tail of zeta)."""
        v = mpf(3)
        n = 5
        tail = zeta(v) - harmonic_zeta(n - 1, v)
        direct = sum(power(mpf(m), -v) for m in range(n, 10000))
        assert fabs(tail - direct) / fabs(tail) < mpf('1e-3')


class TestFconnFast:
    """Test the fast connected free energy computation."""

    def test_heisenberg_Fconn(self):
        """F^conn_H(e^{-2pi*y}) = -log(prod_{m>=1}(1-e^{-2pi*m*y}))."""
        y = mpf('0.5')
        q = mpexp(-2 * mppi * y)
        # -log(prod_{m>=1}(1-q^m)) = sum_{m>=1} sum_{k>=1} q^{mk}/k
        expected = mpf(0)
        for m in range(1, 100):
            qm = power(q, m)
            if fabs(qm) < mpf('1e-40'):
                break
            expected -= mplog(1 - qm)
        actual = F_conn_fast([1], y, terms=100)
        assert fabs(actual - expected) / fabs(expected) < mpf('1e-10')

    def test_Fconn_positivity(self):
        """F^conn > 0 for all y > 0 (all terms positive)."""
        for y in [mpf('0.1'), mpf('0.5'), mpf(1), mpf(2)]:
            assert F_conn_fast([1], y) > 0


class TestWeightsForFamily:
    """Test the family name -> weights lookup."""

    def test_heisenberg(self):
        assert weights_for_family('heisenberg') == [1]

    def test_virasoro(self):
        assert weights_for_family('virasoro') == [2]

    def test_W_N(self):
        assert weights_for_family('W_N', N=4) == [2, 3, 4]

    def test_lattice(self):
        assert weights_for_family('lattice_rank_r', r=3) == [1, 1, 1]


class TestCollapseExhaustive:
    """Exhaustive collapse tests at various v values."""

    @pytest.mark.parametrize("v", [mpf('1.5'), mpf(2), mpf('2.5'), mpf(3), mpf(4)])
    def test_five_representations_same_v(self, v):
        """Five different (s,u) pairs with the same v all give the same L."""
        v = mpf(v)
        # Generate 5 pairs (s, u) with s+u-1 = v
        pairs = [(v + 1, 0), (v, 1), (v - mpf('0.5'), mpf('1.5')),
                 (v + mpf('0.3'), mpf('0.7')), (1, v)]
        vals = [L_factored([1], s, u) for s, u in pairs]
        for i in range(1, len(vals)):
            assert fabs(vals[i] - vals[0]) < mpf('1e-25'), \
                f"v={v}, pair {i}: {float(vals[i])} != {float(vals[0])}"

    def test_affine_sl2_collapse(self):
        """affine sl_2 (3 weight-1 generators): collapse holds."""
        res = verify_collapse([1, 1, 1], 2, 1, 1.5, 1.5)
        assert res['match']

    def test_W5_collapse(self):
        """W_5 collapse: L(3,1) = L(2,2)."""
        res = verify_collapse([2, 3, 4, 5], 3, 1, 2, 2)
        assert res['match']


class TestCrossConsistency:
    """Cross-consistency between different computational paths."""

    def test_S_closed_vs_explicit_heisenberg(self):
        """Closed-form S_H matches explicit double sum."""
        res = verify_S_A_closed_form([1], 3)
        assert res['rel_error'] < 1e-4

    def test_S_closed_vs_explicit_virasoro(self):
        """Closed-form S_Vir matches explicit double sum."""
        res = verify_S_A_closed_form([2], 3)
        assert res['rel_error'] < 1e-4

    def test_cross_family_table_structure(self):
        """cross_family_table returns the right structure."""
        table = cross_family_table(3)
        assert 'heisenberg' in table
        assert 'virasoro' in table
        assert 'Lambda' in table['heisenberg']

    def test_cross_family_heisenberg_dominates_virasoro(self):
        """Lambda_H(v) > Lambda_Vir(v) for v > 1 (Heisenberg starts at w=1)."""
        for v in [2, 3, 4]:
            lh = completed_L([1], v)
            lv = completed_L([2], v)
            assert lh > lv
