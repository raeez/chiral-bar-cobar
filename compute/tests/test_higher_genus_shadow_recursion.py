"""Tests for higher-genus shadow recursion.

Verifies:
  1. Genus loop operator Lambda_P on standard families
  2. Free energy F_g = kappa * lambda_g^FP for g = 1,...,5
  3. Genus-1 shadow obstruction tower for all five families
  4. Genus-1 Hessian correction delta_H^{(1)}
  5. Genus-1 loop ratio rho^{(1)}
  6. Genus-2 shadow obstruction tower and shell decomposition
  7. Genus spectral sequence E_1 page
  8. Cross-family consistency and special values
  9. All-genera shadow table

Ground truth:
  - nonlinear_modular_shadows.tex: genus loop, shell decomposition
  - higher_genus_modular_koszul.tex: genus spectral sequence
  - modular_shadow_tower.py: delta_H^{(1)}_Vir, rho^{(1)}_Vir
  - Bernoulli numbers: B_2=1/6, B_4=-1/30, B_6=1/42, B_8=-1/30, B_10=5/66
"""

import pytest
from sympy import (
    Rational, Symbol, simplify, factor, bernoulli, factorial,
    binomial, limit, oo, S,
)
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from higher_genus_shadow_recursion import (
    lambda_fp,
    family_kappa, family_propagator, family_cubic, family_quartic,
    family_genus0_shadow,
    genus_loop_operator,
    genus1_shadow_tower, genus2_shadow_tower,
    genus2_shell_decomposition,
    genus_free_energy,
    genus_spectral_sequence_e1,
    genus_loop_ratio,
    all_genera_shadow_table,
    FAMILIES,
)

c = Symbol('c')
k = Symbol('k')


# =========================================================================
# I. Faber-Pandharipande numbers
# =========================================================================

class TestFaberPandharipande:
    """Tests for lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""

    def test_lambda1(self):
        """lambda_1 = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda2(self):
        """lambda_2 = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda3(self):
        """lambda_3 = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda4(self):
        """lambda_4 from B_8 = -1/30."""
        B8 = bernoulli(8)
        assert B8 == Rational(-1, 30)
        expected = (2**7 - 1) * abs(B8) / (2**7 * factorial(8))
        assert lambda_fp(4) == Rational(expected)

    def test_lambda5(self):
        """lambda_5 from B_10 = 5/66."""
        B10 = bernoulli(10)
        assert B10 == Rational(5, 66)
        expected = (2**9 - 1) * abs(B10) / (2**9 * factorial(10))
        assert lambda_fp(5) == Rational(expected)

    def test_lambda_raises_for_g0(self):
        """lambda_fp(g) undefined for g < 1."""
        with pytest.raises(ValueError):
            lambda_fp(0)


# =========================================================================
# II. Family data
# =========================================================================

class TestFamilyData:
    """Tests for family-specific shadow data."""

    def test_heisenberg_kappa(self):
        """kappa(H_1) = 1."""
        assert family_kappa('heisenberg', kappa=1) == 1

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        assert simplify(family_kappa('virasoro') - c / 2) == 0

    def test_affine_sl2_kappa(self):
        """kappa(sl_2_k) = 3(k+2)/4."""
        assert simplify(family_kappa('affine_sl2') - 3 * (k + 2) / 4) == 0

    def test_betagamma_kappa(self):
        """kappa(beta-gamma) = 1."""
        assert family_kappa('betagamma') == Rational(1)

    def test_w3_kappa(self):
        """kappa(W_3) = 5c/6."""
        assert simplify(family_kappa('w3') - 5 * c / 6) == 0

    def test_propagator_inverts_kappa(self):
        """P * kappa = 1 for all families."""
        for fam in ['heisenberg', 'betagamma']:
            P = family_propagator(fam)
            kap = family_kappa(fam)
            assert simplify(P * kap - 1) == 0

    def test_virasoro_propagator(self):
        """P_Vir = 2/c."""
        P = family_propagator('virasoro')
        assert simplify(P - 2 / c) == 0

    def test_affine_propagator(self):
        """P_aff = 4/(3(k+2))."""
        P = family_propagator('affine_sl2')
        assert simplify(P - 4 / (3 * (k + 2))) == 0

    def test_heisenberg_cubic_zero(self):
        """C_Heis = 0 (Gaussian)."""
        assert family_cubic('heisenberg') == 0

    def test_virasoro_cubic(self):
        """C_Vir = 2."""
        assert family_cubic('virasoro') == 2

    def test_heisenberg_quartic_zero(self):
        """Q_Heis = 0."""
        assert family_quartic('heisenberg') == 0

    def test_affine_quartic_zero(self):
        """Q_aff = 0 (Lie/tree)."""
        assert family_quartic('affine_sl2') == 0

    def test_virasoro_quartic(self):
        """Q^contact_Vir = 10/[c(5c+22)]."""
        Q = family_quartic('virasoro')
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(Q - expected) == 0


# =========================================================================
# III. Genus loop operator
# =========================================================================

class TestGenusLoopOperator:
    """Tests for Lambda_P: contracts two legs with propagator."""

    def test_loop_of_kappa_x2(self):
        """Lambda_P(kappa * x^2) = C(2,2)*P*kappa = 1."""
        # On 1D line: P*kappa = 1, C(2,2) = 1
        result = genus_loop_operator(Rational(1), Rational(1), 2)
        assert result == 1

    def test_loop_combinatorial_rank2(self):
        """C(2,2) = 1 contraction from rank-2 tensor."""
        assert genus_loop_operator(Rational(1), Rational(1), 2) == 1

    def test_loop_combinatorial_rank3(self):
        """C(3,2) = 3 contractions from rank-3 tensor."""
        assert genus_loop_operator(Rational(1), Rational(1), 3) == 3

    def test_loop_combinatorial_rank4(self):
        """C(4,2) = 6 contractions from rank-4 tensor."""
        assert genus_loop_operator(Rational(1), Rational(1), 4) == 6

    def test_loop_combinatorial_rank5(self):
        """C(5,2) = 10 contractions from rank-5 tensor."""
        assert genus_loop_operator(Rational(1), Rational(1), 5) == 10

    def test_loop_combinatorial_rank6(self):
        """C(6,2) = 15 contractions from rank-6 tensor."""
        assert genus_loop_operator(Rational(1), Rational(1), 6) == 15

    def test_loop_of_cubic(self):
        """Lambda_P(C*x^3) = 3*P*C."""
        C_coeff = Rational(2)
        P = Rational(2) / c
        result = genus_loop_operator(C_coeff, P, 3)
        assert simplify(result - 3 * P * C_coeff) == 0
        assert simplify(result - Rational(12) / c) == 0

    def test_loop_of_quartic_virasoro(self):
        """Lambda_P(Q_Vir*x^4) = 6*(2/c)*10/[c(5c+22)] = 120/[c^2(5c+22)]."""
        Q = Rational(10) / (c * (5 * c + 22))
        P = Rational(2) / c
        result = genus_loop_operator(Q, P, 4)
        expected = Rational(120) / (c**2 * (5 * c + 22))
        assert simplify(result - expected) == 0

    def test_loop_of_zero(self):
        """Lambda_P(0) = 0."""
        assert genus_loop_operator(Rational(0), Rational(1), 4) == 0

    def test_loop_rank_below_2(self):
        """Lambda_P on arity < 2 gives 0."""
        assert genus_loop_operator(Rational(1), Rational(1), 1) == 0
        assert genus_loop_operator(Rational(1), Rational(1), 0) == 0

    def test_loop_of_hessian_is_dim(self):
        """Lambda_P(H_Vir) = C(2,2)*P*H = 1 (dimension of primary line)."""
        H_coeff = c / 2
        P = 2 / c
        result = genus_loop_operator(H_coeff, P, 2)
        assert simplify(result - 1) == 0


# =========================================================================
# IV. Free energy tests
# =========================================================================

class TestFreeEnergy:
    """F_g = kappa * lambda_g^FP for all families."""

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all families."""
        for fam in ['heisenberg', 'betagamma']:
            fe = genus_free_energy(fam, max_g=1)
            kap = family_kappa(fam)
            assert simplify(fe[1] - kap / 24) == 0

    def test_F1_virasoro(self):
        """F_1(Vir) = c/48."""
        fe = genus_free_energy('virasoro', max_g=1)
        assert simplify(fe[1] - c / 48) == 0

    def test_F1_affine_sl2(self):
        """F_1(sl_2_k) = 3(k+2)/96 = (k+2)/32."""
        fe = genus_free_energy('affine_sl2', max_g=1)
        expected = 3 * (k + 2) / (4 * 24)
        assert simplify(fe[1] - expected) == 0

    def test_F2_equals_kappa_times_7_over_5760(self):
        """F_2 = kappa * 7/5760 for all families."""
        for fam in ['heisenberg', 'betagamma']:
            fe = genus_free_energy(fam, max_g=2)
            kap = family_kappa(fam)
            assert simplify(fe[2] - kap * Rational(7, 5760)) == 0

    def test_F2_virasoro(self):
        """F_2(Vir) = c/2 * 7/5760 = 7c/11520."""
        fe = genus_free_energy('virasoro', max_g=2)
        assert simplify(fe[2] - 7 * c / 11520) == 0

    def test_F3_equals_kappa_times_31_over_967680(self):
        """F_3 = kappa * 31/967680."""
        for fam in ['heisenberg', 'virasoro']:
            fe = genus_free_energy(fam, max_g=3)
            kap = family_kappa(fam)
            assert simplify(fe[3] - kap * Rational(31, 967680)) == 0

    def test_F_g_heisenberg_at_kappa1(self):
        """F_g for Heisenberg at kappa=1 equals lambda_g^FP."""
        fe = genus_free_energy('heisenberg', max_g=5, kappa=1)
        for g in range(1, 6):
            assert fe[g] == lambda_fp(g)

    def test_F_g_virasoro_at_c1(self):
        """F_g for Virasoro at c=1."""
        fe = genus_free_energy('virasoro', max_g=3, c=1)
        assert fe[1] == Rational(1, 2) * lambda_fp(1)
        assert fe[2] == Rational(1, 2) * lambda_fp(2)
        assert fe[3] == Rational(1, 2) * lambda_fp(3)

    def test_F_g_affine_sl2_at_k0(self):
        """F_g for affine sl_2 at k=0: kappa = 3*2/4 = 3/2."""
        fe = genus_free_energy('affine_sl2', max_g=3, k=0)
        kap = Rational(3, 2)
        for g in range(1, 4):
            assert fe[g] == kap * lambda_fp(g)

    def test_F_g_monotone_decreasing(self):
        """F_g decreases rapidly with g (for kappa > 0)."""
        fe = genus_free_energy('virasoro', max_g=5, c=10)
        for g in range(1, 5):
            assert fe[g] > fe[g + 1]

    def test_F_g_all_positive(self):
        """F_g > 0 for all g >= 1 when kappa > 0."""
        fe = genus_free_energy('virasoro', max_g=5, c=10)
        for g in range(1, 6):
            assert fe[g] > 0


# =========================================================================
# V. Genus-1 shadow obstruction tower
# =========================================================================

class TestGenus1ShadowTower:
    """Tests for genus-1 shadows Theta^{(1,n)}."""

    def test_g1_arity0_is_F1(self):
        """(1,0) = F_1 = kappa/24 for all families."""
        for fam in ['heisenberg', 'virasoro', 'affine_sl2', 'betagamma']:
            g1 = genus1_shadow_tower(fam, max_n=0)
            kap = family_kappa(fam)
            assert simplify(g1[0] - kap / 24) == 0

    def test_heisenberg_g1_all_zero_beyond_arity0(self):
        """Heisenberg: all genus-1 shadows vanish for n >= 2.

        Heisenberg is Gaussian (depth 2), so all genus-0 shadows vanish
        for arity >= 3, hence Lambda_P applied to them gives zero.
        """
        g1 = genus1_shadow_tower('heisenberg', max_n=8)
        for n in range(2, 9, 2):
            assert g1[n] == 0

    def test_affine_g1_arity2_from_cubic(self):
        """Affine sl_2: (1,2) = Lambda_P(C * x^3) = 3*P*C (nonzero for C != 0).

        BUT: Q_aff = 0, so the arity-2 genus-1 shadow comes from the
        quartic applied via Lambda_P. Since Q_aff = 0:
            (1,2) = Lambda_P(Q_aff * x^4) = 0.

        Wait, the recursion is (1,n) = Lambda_P(Sh^{(0)}_{n+2}).
        (1,2) = Lambda_P(Sh_4^{(0)}) = Lambda_P(Q * x^4).
        For affine: Q = 0, so (1,2) = 0.
        """
        g1 = genus1_shadow_tower('affine_sl2', max_n=2)
        assert g1[2] == 0

    def test_betagamma_g1_arity2_zero(self):
        """Beta-gamma: (1,2) = Lambda_P(Q * x^4) = 0 (Q = 0 on weight line)."""
        g1 = genus1_shadow_tower('betagamma', max_n=2)
        assert g1[2] == 0

    def test_virasoro_g1_arity2_is_delta_H(self):
        """Virasoro: (1,2) = delta_H^{(1)} = 120/[c^2(5c+22)]."""
        g1 = genus1_shadow_tower('virasoro', max_n=2)
        expected = Rational(120) / (c**2 * (5 * c + 22))
        assert simplify(g1[2] - expected) == 0

    def test_virasoro_g1_arity4_nonzero(self):
        """Virasoro: (1,4) is nonzero (involves genus-0 arity-6 shadow)."""
        g1 = genus1_shadow_tower('virasoro', max_n=4)
        # (1,4) = Lambda_P(Sh_6^{(0)}) + bracket correction
        # Since Sh_6^{(0)} is nonzero for Virasoro, this is nonzero
        assert simplify(g1[4]) != 0

    def test_virasoro_g1_arity0_value(self):
        """Virasoro: (1,0) = c/48."""
        g1 = genus1_shadow_tower('virasoro', max_n=0)
        assert simplify(g1[0] - c / 48) == 0


# =========================================================================
# VI. Genus-1 Hessian correction and loop ratio
# =========================================================================

class TestGenus1HessianAndRatio:
    """Tests for delta_H^{(1)} and rho^{(1)} = delta_H / H."""

    def test_virasoro_delta_H_formula(self):
        """delta_H^{(1)}_Vir = 120/[c^2(5c+22)]."""
        rho = genus_loop_ratio('virasoro', genus=1)
        kap = c / 2
        dH = rho * kap
        expected = Rational(120) / (c**2 * (5 * c + 22))
        assert simplify(dH - expected) == 0

    def test_virasoro_loop_ratio_formula(self):
        """rho^{(1)}_Vir = 240/[c^3(5c+22)]."""
        rho = genus_loop_ratio('virasoro', genus=1)
        expected = Rational(240) / (c**3 * (5 * c + 22))
        assert simplify(rho - expected) == 0

    def test_heisenberg_loop_ratio_zero(self):
        """Heisenberg: rho^{(1)} = 0 (Q = 0)."""
        rho = genus_loop_ratio('heisenberg', genus=1)
        assert rho == 0

    def test_affine_loop_ratio_zero(self):
        """Affine sl_2: rho^{(1)} = 0 (Q = 0)."""
        rho = genus_loop_ratio('affine_sl2', genus=1)
        assert rho == 0

    def test_betagamma_loop_ratio_zero(self):
        """Beta-gamma: rho^{(1)} = 0 (Q = 0 on weight line)."""
        rho = genus_loop_ratio('betagamma', genus=1)
        assert rho == 0

    def test_virasoro_loop_ratio_at_c1(self):
        """rho^{(1)}_Vir at c=1: 240/27 = 80/9."""
        rho = genus_loop_ratio('virasoro', genus=1)
        val = rho.subs(c, 1)
        assert val == Rational(240, 27)

    def test_virasoro_loop_ratio_at_c13(self):
        """rho^{(1)}_Vir at c=13 (self-dual point)."""
        rho = genus_loop_ratio('virasoro', genus=1)
        val = rho.subs(c, 13)
        expected = Rational(240) / (2197 * 87)
        assert simplify(val - expected) == 0

    def test_virasoro_loop_ratio_large_c(self):
        """rho^{(1)} ~ 48/c^4 as c -> oo."""
        rho = genus_loop_ratio('virasoro', genus=1)
        asymp = limit(rho * c**4, c, oo)
        assert asymp == Rational(48)


# =========================================================================
# VII. Genus-2 shadow obstruction tower
# =========================================================================

class TestGenus2ShadowTower:
    """Tests for genus-2 shadows."""

    def test_g2_arity0_is_F2(self):
        """(2,0) = F_2 = kappa * 7/5760."""
        for fam in ['heisenberg', 'virasoro']:
            g2 = genus2_shadow_tower(fam, max_n=0)
            kap = family_kappa(fam)
            assert simplify(g2[0] - kap * Rational(7, 5760)) == 0

    def test_virasoro_g2_arity0(self):
        """Virasoro: F_2 = 7c/11520."""
        g2 = genus2_shadow_tower('virasoro', max_n=0)
        assert simplify(g2[0] - 7 * c / 11520) == 0

    def test_heisenberg_g2_arity2_zero(self):
        """Heisenberg: (2,2) = 0 (Gaussian, no genus-1 arity-4 shadow)."""
        g2 = genus2_shadow_tower('heisenberg', max_n=2)
        assert g2.get(2, 0) == 0


# =========================================================================
# VIII. Genus-2 shell decomposition
# =========================================================================

class TestGenus2ShellDecomposition:
    """Tests for the three-shell decomposition at genus 2."""

    def test_heisenberg_only_loop2(self):
        """Heisenberg: only loop^2 contributes (G class)."""
        shells = genus2_shell_decomposition('heisenberg')
        assert shells['sep_loop'] == 0
        assert shells['pf'] == 0
        # Total must equal F_2
        kap = family_kappa('heisenberg')
        assert simplify(shells['total'] - kap * Rational(7, 5760)) == 0

    def test_heisenberg_loop2_equals_total(self):
        """Heisenberg: loop^2 = F_2 (the entire genus-2 free energy)."""
        shells = genus2_shell_decomposition('heisenberg')
        assert simplify(shells['loop2'] - shells['total']) == 0

    def test_affine_no_pf(self):
        """Affine sl_2: no planted-forest correction (L class)."""
        shells = genus2_shell_decomposition('affine_sl2')
        assert shells['pf'] == 0

    def test_affine_has_sep_loop(self):
        """Affine sl_2: separating degeneration contributes (L class)."""
        shells = genus2_shell_decomposition('affine_sl2')
        assert simplify(shells['sep_loop']) != 0

    def test_betagamma_no_pf(self):
        """Beta-gamma: no planted-forest correction (C class)."""
        shells = genus2_shell_decomposition('betagamma')
        assert shells['pf'] == 0

    def test_virasoro_all_three_shells(self):
        """Virasoro: all three shells nonzero (M class)."""
        shells = genus2_shell_decomposition('virasoro')
        assert simplify(shells['loop2']) != 0
        assert simplify(shells['sep_loop']) != 0
        assert simplify(shells['pf']) != 0

    def test_shell_decomposition_sums_to_total(self):
        """loop^2 + sep_loop + pf = F_2 for all families."""
        for fam in ['heisenberg', 'affine_sl2', 'betagamma', 'virasoro']:
            shells = genus2_shell_decomposition(fam)
            total = shells['loop2'] + shells['sep_loop'] + shells['pf']
            assert simplify(total - shells['total']) == 0

    def test_virasoro_total_is_F2(self):
        """Virasoro: total shell = F_2 = 7c/11520."""
        shells = genus2_shell_decomposition('virasoro')
        assert simplify(shells['total'] - 7 * c / 11520) == 0


# =========================================================================
# IX. Genus spectral sequence E_1 page
# =========================================================================

class TestGenusSpectralSequenceE1:
    """Tests for E_1^{p,q} with p = genus, q = arity."""

    def test_heisenberg_genus0_only_arity2(self):
        """Heisenberg: only E_1^{0,2} is nonzero at genus 0."""
        e1 = genus_spectral_sequence_e1('heisenberg', max_g=0, max_n=6)
        assert e1[(0, 2)] == 1
        assert e1[(0, 4)] == 0
        assert e1[(0, 6)] == 0

    def test_virasoro_genus0_through_arity6(self):
        """Virasoro: E_1^{0,q} nonzero for q = 2, 4, 6."""
        e1 = genus_spectral_sequence_e1('virasoro', max_g=0, max_n=6)
        assert e1[(0, 2)] == 1
        assert e1[(0, 4)] == 1
        assert e1[(0, 6)] == 1

    def test_affine_genus0_through_arity4(self):
        """Affine: E_1^{0,2} = 1, E_1^{0,4} = 0 (depth 3, Q=0)."""
        e1 = genus_spectral_sequence_e1('affine_sl2', max_g=0, max_n=6)
        assert e1[(0, 2)] == 1
        # Cubic is arity 3, not arity 4 on 1D even line; quartic is 0
        assert e1[(0, 4)] == 0

    def test_heisenberg_genus1_only_arity0(self):
        """Heisenberg: only (1,0) = F_1 is nonzero at genus 1."""
        e1 = genus_spectral_sequence_e1('heisenberg', max_g=1, max_n=6)
        assert e1[(1, 0)] == 1
        assert e1[(1, 2)] == 0
        assert e1[(1, 4)] == 0

    def test_virasoro_genus1_nonzero_entries(self):
        """Virasoro: (1,0) and (1,2) are nonzero at genus 1."""
        e1 = genus_spectral_sequence_e1('virasoro', max_g=1, max_n=4)
        assert e1[(1, 0)] == 1
        assert e1[(1, 2)] == 1

    def test_genus0_arity0_always_zero(self):
        """No genus-0 free energy: E_1^{0,0} = 0 for all families."""
        for fam in ['heisenberg', 'virasoro', 'affine_sl2']:
            e1 = genus_spectral_sequence_e1(fam, max_g=0, max_n=0)
            assert e1[(0, 0)] == 0


# =========================================================================
# X. Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-checks between families and computations."""

    def test_F1_universal(self):
        """F_1 = kappa/24 is universal across all five families."""
        for fam in FAMILIES:
            fe = genus_free_energy(fam, max_g=1)
            kap = family_kappa(fam)
            assert simplify(fe[1] - kap / 24) == 0

    def test_F2_universal(self):
        """F_2 = kappa * 7/5760 is universal across all five families."""
        for fam in FAMILIES:
            fe = genus_free_energy(fam, max_g=2)
            kap = family_kappa(fam)
            assert simplify(fe[2] - kap * Rational(7, 5760)) == 0

    def test_F3_universal(self):
        """F_3 = kappa * 31/967680 is universal across all five families."""
        for fam in FAMILIES:
            fe = genus_free_energy(fam, max_g=3)
            kap = family_kappa(fam)
            assert simplify(fe[3] - kap * Rational(31, 967680)) == 0

    def test_propagator_times_kappa_is_one(self):
        """P * kappa = 1 for all families (1D primary line)."""
        for fam in FAMILIES:
            P = family_propagator(fam)
            kap = family_kappa(fam)
            assert simplify(P * kap - 1) == 0

    def test_shadow_depth_classification(self):
        """Shadow depth classes: G=2, L=3, C=4, M=None."""
        assert FAMILIES['heisenberg']['shadow_depth'] == 2
        assert FAMILIES['affine_sl2']['shadow_depth'] == 3
        assert FAMILIES['betagamma']['shadow_depth'] == 4
        assert FAMILIES['virasoro']['shadow_depth'] is None
        assert FAMILIES['w3']['shadow_depth'] is None

    def test_shadow_class_labels(self):
        """Shadow class labels: G, L, C, M."""
        assert FAMILIES['heisenberg']['shadow_class'] == 'G'
        assert FAMILIES['affine_sl2']['shadow_class'] == 'L'
        assert FAMILIES['betagamma']['shadow_class'] == 'C'
        assert FAMILIES['virasoro']['shadow_class'] == 'M'
        assert FAMILIES['w3']['shadow_class'] == 'M'

    def test_finite_depth_genus0_vanishing(self):
        """Genus-0 shadows vanish beyond shadow depth for finite-depth families."""
        assert family_genus0_shadow('heisenberg', 3) == 0
        assert family_genus0_shadow('heisenberg', 4) == 0
        assert family_genus0_shadow('affine_sl2', 4) == 0
        assert family_genus0_shadow('affine_sl2', 5) == 0
        assert family_genus0_shadow('betagamma', 5) == 0
        assert family_genus0_shadow('betagamma', 6) == 0


# =========================================================================
# XI. Special values
# =========================================================================

class TestSpecialValues:
    """Evaluations at physically significant parameters."""

    def test_virasoro_c1_F1(self):
        """F_1(Vir_1) = 1/48."""
        fe = genus_free_energy('virasoro', max_g=1, c=1)
        assert fe[1] == Rational(1, 48)

    def test_virasoro_c26_F1(self):
        """F_1(Vir_26) = 26/48 = 13/24."""
        fe = genus_free_energy('virasoro', max_g=1, c=26)
        assert fe[1] == Rational(13, 24)

    def test_virasoro_c13_F1(self):
        """F_1(Vir_13) = 13/48 (self-dual point)."""
        fe = genus_free_energy('virasoro', max_g=1, c=13)
        assert fe[1] == Rational(13, 48)

    def test_affine_k1_F1(self):
        """F_1(sl_2_1) = 3*3/4 / 24 = 9/96 = 3/32."""
        fe = genus_free_energy('affine_sl2', max_g=1, k=1)
        assert fe[1] == Rational(3, 32)

    def test_betagamma_F1(self):
        """F_1(beta-gamma) = 1/24 (kappa = 1)."""
        fe = genus_free_energy('betagamma', max_g=1)
        assert fe[1] == Rational(1, 24)

    def test_w3_c2_F1(self):
        """F_1(W_3) at c=2: kappa = 5*2/6 = 5/3, F_1 = 5/72."""
        fe = genus_free_energy('w3', max_g=1, c=2)
        assert fe[1] == Rational(5, 72)

    def test_virasoro_c_half_loop_ratio(self):
        """rho^{(1)} at c=1/2 (Ising model)."""
        rho = genus_loop_ratio('virasoro', genus=1)
        val = rho.subs(c, Rational(1, 2))
        expected = Rational(240) / (Rational(1, 8) * Rational(49, 2))
        assert simplify(val - expected) == 0


# =========================================================================
# XII. All-genera shadow table
# =========================================================================

class TestAllGeneraShadowTable:
    """Tests for the formatted all-genera table."""

    def test_table_has_correct_keys(self):
        """Table has entries for all (g, n) pairs."""
        table = all_genera_shadow_table('virasoro', max_g=2, max_n=4)
        for g in range(3):
            for n in range(0, 5, 2):
                assert (g, n) in table

    def test_table_genus0_matches_genus0_shadows(self):
        """Table genus-0 row matches family_genus0_shadow."""
        table = all_genera_shadow_table('virasoro', max_g=0, max_n=4)
        for n in range(0, 5, 2):
            expected = family_genus0_shadow('virasoro', n)
            assert simplify(table[(0, n)] - expected) == 0

    def test_table_genus1_matches_tower(self):
        """Table genus-1 row matches genus1_shadow_tower."""
        table = all_genera_shadow_table('virasoro', max_g=1, max_n=4)
        g1 = genus1_shadow_tower('virasoro', max_n=4)
        for n in range(0, 5, 2):
            assert simplify(table[(1, n)] - g1[n]) == 0

    def test_table_genus3_free_energy(self):
        """Table genus-3 arity-0 entry is F_3."""
        table = all_genera_shadow_table('virasoro', max_g=3, max_n=0)
        expected = family_kappa('virasoro') * lambda_fp(3)
        assert simplify(table[(3, 0)] - expected) == 0

    def test_heisenberg_table_sparse(self):
        """Heisenberg table is sparse: only (g,0) entries nonzero for g >= 1."""
        table = all_genera_shadow_table('heisenberg', max_g=3, max_n=4)
        for g in range(1, 4):
            for n in range(2, 5, 2):
                assert table[(g, n)] == 0
            assert table[(g, 0)] != 0


# =========================================================================
# XIII. Virasoro genus-0 higher-arity shadows
# =========================================================================

class TestVirasoroHigherArity:
    """Tests for Virasoro genus-0 shadows at arity >= 5."""

    def test_virasoro_arity5_nonzero(self):
        """Sh_5^{(0)} for Virasoro is nonzero (quintic forced)."""
        sh5 = family_genus0_shadow('virasoro', 5)
        assert simplify(sh5) != 0

    def test_virasoro_arity5_formula(self):
        """Sh_5 = o^(5) = {C, Q}_H = 480/[c^2(5c+22)]."""
        sh5 = family_genus0_shadow('virasoro', 5)
        expected = Rational(480) / (c**2 * (5 * c + 22))
        assert simplify(sh5 - expected) == 0

    def test_virasoro_arity6_nonzero(self):
        """Sh_6^{(0)} for Virasoro is nonzero."""
        sh6 = family_genus0_shadow('virasoro', 6)
        assert simplify(sh6) != 0

    def test_virasoro_arity5_at_c1(self):
        """Sh_5 at c=1: 480/27 = 160/9."""
        sh5 = family_genus0_shadow('virasoro', 5)
        assert sh5.subs(c, 1) == Rational(160, 9)


# =========================================================================
# XIV. Bernoulli number cross-checks
# =========================================================================

class TestBernoulliCrossChecks:
    """Verify Bernoulli numbers used in the free energy computation."""

    def test_B2(self):
        """B_2 = 1/6."""
        assert bernoulli(2) == Rational(1, 6)

    def test_B4(self):
        """B_4 = -1/30."""
        assert bernoulli(4) == Rational(-1, 30)

    def test_B6(self):
        """B_6 = 1/42."""
        assert bernoulli(6) == Rational(1, 42)

    def test_B8(self):
        """B_8 = -1/30."""
        assert bernoulli(8) == Rational(-1, 30)

    def test_B10(self):
        """B_10 = 5/66."""
        assert bernoulli(10) == Rational(5, 66)

    def test_lambda1_from_B2(self):
        """lambda_1 = (2^1-1)/2^1 * |B_2|/2! = (1/2)*(1/6)/2 = 1/24."""
        result = (2**1 - 1) * abs(bernoulli(2)) / (2**1 * factorial(2))
        assert Rational(result) == Rational(1, 24)

    def test_lambda2_from_B4(self):
        """lambda_2 = (2^3-1)/2^3 * |B_4|/4! = (7/8)*(1/30)/24 = 7/5760."""
        result = (2**3 - 1) * abs(bernoulli(4)) / (2**3 * factorial(4))
        assert Rational(result) == Rational(7, 5760)


# =========================================================================
# XV. Genus-2 free energy numerical checks
# =========================================================================

class TestGenus2Numerical:
    """Numerical checks for genus-2 free energies."""

    def test_virasoro_F2_at_c10(self):
        """F_2(Vir_10) = 5 * 7/5760 = 7/1152."""
        fe = genus_free_energy('virasoro', max_g=2, c=10)
        assert fe[2] == Rational(7, 1152)

    def test_heisenberg_F2_at_kappa2(self):
        """F_2(H_2) = 2 * 7/5760 = 7/2880."""
        fe = genus_free_energy('heisenberg', max_g=2, kappa=2)
        assert fe[2] == Rational(7, 2880)

    def test_affine_F2_at_k1(self):
        """F_2(sl_2_1) = 9/4 * 7/5760 = 63/23040 = 7/2560."""
        fe = genus_free_energy('affine_sl2', max_g=2, k=1)
        kap = Rational(9, 4)
        expected = kap * Rational(7, 5760)
        assert fe[2] == expected

    def test_w3_F2_at_c3(self):
        """F_2(W_3) at c=3: kappa = 5/2, F_2 = (5/2)*7/5760 = 7/2304."""
        fe = genus_free_energy('w3', max_g=2, c=3)
        assert fe[2] == Rational(5, 2) * Rational(7, 5760)
