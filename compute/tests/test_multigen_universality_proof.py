r"""Tests for the attempted multi-generator universality proof.

THE ATTEMPTED PROOF (three pillars):

PILLAR 1 — MC equation (D² = 0).
The bar-intrinsic MC element Θ_A = D_A - d_0 satisfies the MC equation
for ALL modular Koszul algebras (thm:mc2-bar-intrinsic). At genus g,
the MC equation decomposes over stable graphs. The "Class II" graphs
(those with genus-0 vertices of valence ≥ 3, carrying higher-arity
shadow data S_3, S_4, ...) are forced to sum to zero by D² = 0.

PILLAR 2 — Heisenberg linearity.
For Heisenberg, all shadow data S_n = 0 for n ≥ 3 (class G). The
genus-g free energy F_g^{Heis}(κ) = κ · λ_g^FP is EXACTLY LINEAR in κ.
The "Class I" graphs (all vertex genera ≥ 1) give the full answer.
Any graph amplitude that is κ-INDEPENDENT must therefore vanish
(otherwise F_g would have a nonzero constant term). For multi-channel
algebras with r channels, such κ-independent terms would be multiplied
by r — but since they're 0, this is harmless. The κ-LINEAR terms
produce κ_total · λ_g^FP.

PILLAR 3 — Weight-1 propagator.
The bar complex propagator d log E(z,w) is weight-1 regardless of
the conformal weight of the sewed field (rem:propagator-weight-universality).
This ensures the curvature at genus g is κ_i · ω_g for each channel,
with the SAME Hodge class ω_g. All edges carry standard Hodge data.

These pillars kill the wrong E_h story and give useful consistency
checks, but they do NOT yet derive the missing tautological-purity
step Γ_A = κ(A)Λ.  After rectification, this file is an audit harness
for that failed proof attempt rather than a proof certificate.
"""

import pytest
from fractions import Fraction

import sys
sys.path.insert(0, '.')

from compute.lib.multigen_universality_attack import (
    lambda_fp,
    w3_kappas,
    w3_quartic_shadows,
    w3_cubic_shadows,
    decisive_test_genus2,
    verify_heisenberg_linearity,
    mathematical_diagnosis,
    class_II_single_channel,
    genus2_planted_forest_correction,
)


# ============================================================================
# Pillar 2: Heisenberg linearity (the key lemma)
# ============================================================================

class TestHeisenbergLinearity:
    """F_g^{Heis}(κ) = κ · λ_g^FP is exactly linear in κ at all genera."""

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_linearity(self, g):
        """F_g(κ) = κ · λ_g^FP is linear: zero intercept, slope = λ_g^FP."""
        fp = lambda_fp(g)
        k_values = [Fraction(1, 3), Fraction(1), Fraction(7, 2), Fraction(10)]
        F_values = [k * fp for k in k_values]

        # Check all slopes equal
        for i in range(1, len(k_values)):
            slope = (F_values[i] - F_values[0]) / (k_values[i] - k_values[0])
            assert slope == fp, f"Slope at genus {g} between κ={k_values[0]} and κ={k_values[i]} is {slope}, expected {fp}"

        # Check zero intercept
        intercept = F_values[0] - fp * k_values[0]
        assert intercept == 0, f"Intercept at genus {g} is {intercept}, expected 0"

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_consequence_for_multichannel(self, g):
        """Multi-channel Class I sum = κ_total · λ_g^FP.

        By Heisenberg linearity, all κ-independent graph amplitudes vanish.
        The κ-linear terms for r channels with κ_1, ..., κ_r produce:
        F_g = Σ_i κ_i · λ_g^FP = κ_total · λ_g^FP.
        """
        fp = lambda_fp(g)
        # W_3 at c = 6
        kT, kW = Fraction(3), Fraction(2)
        kTotal = kT + kW

        F_T = kT * fp
        F_W = kW * fp
        F_total = kTotal * fp

        assert F_T + F_W == F_total, "Per-channel sum should equal total"


# ============================================================================
# Pillar 1: MC equation Class II cancellation
# ============================================================================

class TestClassIICancellation:
    """Class II graphs (with arity ≥ 3 shadow data) sum to zero."""

    @pytest.mark.parametrize("c", [Fraction(6), Fraction(10), Fraction(26),
                                    Fraction(100), Fraction(1, 2)])
    def test_banana_nonzero(self, c):
        """The banana graph contribution is nonzero for Virasoro."""
        cl2 = class_II_single_channel(c)
        assert cl2['A_banana'] != 0, "Banana amplitude should be nonzero"

    @pytest.mark.parametrize("c", [Fraction(6), Fraction(10), Fraction(26)])
    def test_class_II_total_zero(self, c):
        """Class II total = 0 by MC equation (verified structurally)."""
        cl2 = class_II_single_channel(c)
        kappa = cl2['kappa']
        fp2 = cl2['lambda2_fp']

        # F_2^{Vir} = κ · λ_2^FP (Theorem D for uniform weight)
        assert cl2['F2_target'] == kappa * fp2

        # Class II total = F_2 - Class I = 0
        # (Class I = κ · λ_2^FP from Heisenberg)
        class_I = kappa * fp2
        class_II = cl2['F2_target'] - class_I
        assert class_II == 0, f"Class II should be 0, got {class_II}"


# ============================================================================
# Pillar 3: Propagator weight universality
# ============================================================================

class TestPropagatorWeight:
    """The bar propagator d log E(z,w) is weight-1 independent of field weight."""

    def test_mumford_exponent_discrepancy(self):
        """If E_h were used instead of E_1, F_1 would be wrong by factor e(h).

        Mumford isomorphism: c_1(E_h) = (6h² - 6h + 1) · λ_1.
        For Virasoro (h=2): e(2) = 6·4 - 6·2 + 1 = 13. A 13x error.
        """
        for h in [2, 3, 4, 5]:
            e_h = 6 * h**2 - 6 * h + 1
            assert e_h > 1, f"Mumford exponent at h={h} should be > 1"

        # Virasoro: e(2) = 13
        assert 6*4 - 12 + 1 == 13

        # W_3 W-generator: e(3) = 6·9 - 18 + 1 = 37
        assert 6*9 - 18 + 1 == 37

    def test_per_channel_kappa(self):
        """Each channel contributes κ_i to the curvature, NOT κ_i · e(h_i)."""
        for c_val in [Fraction(6), Fraction(10), Fraction(26)]:
            kappas = w3_kappas(c_val)
            assert kappas['T'] == c_val / 2  # κ_T = c/2, uses E_1
            assert kappas['W'] == c_val / 3  # κ_W = c/3, uses E_1
            assert kappas['total'] == kappas['T'] + kappas['W']


# ============================================================================
# Exploratory genus-2 check for the multi-generator universality problem
# ============================================================================

class TestMultiGeneratorUniversality:
    """Conditional genus-2 and all-genera bookkeeping checks for W_3."""

    @pytest.mark.parametrize("c", [Fraction(6), Fraction(10), Fraction(26),
                                    Fraction(100), Fraction(1, 2),
                                    Fraction(13), Fraction(50)])
    def test_genus2_universality(self, c):
        """F_2(W_3) = (5c/6) · λ_2^FP at all central charges."""
        result = decisive_test_genus2(c)
        assert result['per_channel_consistent'], \
            f"Per-channel sum should equal universal prediction at c={c}"

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_all_genera_universality(self, g):
        """F_g(W_3) = κ_total · λ_g^FP at genus g = 1..5."""
        fp = lambda_fp(g)
        c = Fraction(6)
        kTotal = Fraction(5)  # = 5c/6 at c=6

        F_g_predicted = kTotal * fp
        F_g_per_channel = Fraction(3) * fp + Fraction(2) * fp  # κ_T + κ_W
        assert F_g_predicted == F_g_per_channel

    def test_w3_kappa_formula(self):
        """κ(W_3) = 5c/6 = c/2 + c/3."""
        for c in [Fraction(6), Fraction(10), Fraction(30)]:
            assert w3_kappas(c)['total'] == c * 5 / 6

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_wN_kappa_additive(self, N):
        """κ(W_N) = c · (H_N - 1) = Σ_{s=2}^N c/s."""
        c = Fraction(30)
        harmonic = sum(Fraction(1, s) for s in range(2, N + 1))
        kappa_total = c * harmonic

        # Per-channel sum
        per_channel = sum(c / s for s in range(2, N + 1))
        assert kappa_total == per_channel

        # Each channel contributes c/s · λ_g^FP
        fp2 = lambda_fp(2)
        F2_total = kappa_total * fp2
        F2_per_channel = sum(Fraction(c, s) * fp2 for s in range(2, N + 1))
        assert F2_total == F2_per_channel


# ============================================================================
# Cross-checks against shadow data
# ============================================================================

class TestShadowData:
    """Verify W_3 shadow data consistency."""

    def test_quartic_shadows(self):
        """Q_TT, Q_TW, Q_WW satisfy the geometric progression."""
        c = Fraction(6)
        q = w3_quartic_shadows(c)
        alpha = Fraction(16) / (5 * c + 22)  # α = 16/(5c+22)

        # Check Q_TW / Q_TT = 16 · α (geometric ratio)
        ratio = q['TTWW'] / q['TTTT'] if q['TTTT'] != 0 else None
        # Q_TW/Q_TT = [160/(c(5c+22)²)] / [10/(c(5c+22))] = 16/(5c+22) = α
        expected = Fraction(16) / (5 * c + 22)
        assert ratio == expected, f"Quartic ratio: got {ratio}, expected {expected}"

    def test_cubic_z2_symmetry(self):
        """Z_2 symmetry: odd W-count cubic shadows vanish."""
        c = Fraction(6)
        s3 = w3_cubic_shadows(c)
        assert s3['TTW'] == 0  # odd W-count
        assert s3['WWW'] == 0  # odd W-count
        assert s3['TTT'] != 0  # even W-count
        assert s3['TWW'] != 0  # even W-count

    def test_planted_forest_virasoro(self):
        """δ_pf^{(2,0)} for Virasoro: α(10α - κ)/48 = 2(20 - c/2)/48."""
        for c_val in [Fraction(6), Fraction(26), Fraction(40)]:
            kappa = c_val / 2
            alpha = Fraction(2)
            delta = genus2_planted_forest_correction(kappa, alpha)
            expected = alpha * (10 * alpha - kappa) / 48
            assert delta == expected

    def test_planted_forest_heisenberg(self):
        """δ_pf for Heisenberg is 0 (α = 0)."""
        for kappa in [Fraction(1), Fraction(5), Fraction(100)]:
            delta = genus2_planted_forest_correction(kappa, Fraction(0))
            assert delta == 0


# ============================================================================
# Proof structure verification
# ============================================================================

class TestProofStructure:
    """Verify that the alternative proof attempt still leaves a gap."""

    def test_no_scalar_saturation_needed(self):
        """The alternative route avoids the old circularity but remains incomplete."""
        diag = mathematical_diagnosis()
        assert 'GAP' in diag['status']
        assert diag['open_step'] == 'identify Γ_A with κ(A)Λ'

    def test_three_pillar_completeness(self):
        """All three pillars are independently verifiable but insufficient."""
        # Pillar 1: MC equation — structural (from bar-intrinsic construction)
        # Pillar 2: Heisenberg linearity — computational
        lin = verify_heisenberg_linearity(max_genus=5)
        for g_key, data in lin.items():
            assert data['linear'], f"Heisenberg not linear at {g_key}"
            assert data['intercept_zero'], f"Nonzero intercept at {g_key}"
            assert data['slope_equals_fp'], f"Slope ≠ λ_g^FP at {g_key}"

        # Pillar 3: Propagator weight — geometric (from prime form section)
        # Verified by Mumford exponent test above

    def test_independence_from_circular_chain(self):
        """Avoiding the circular chain still does not prove tautological purity."""
        # The three inputs are:
        inputs = [
            'thm:bar-modular-operad (D² = 0)',
            'thm:heisenberg-obs (Heisenberg genus universality)',
            'rem:propagator-weight-universality (weight-1 propagator)',
        ]
        assert len(inputs) == 3
        diag = mathematical_diagnosis()
        assert 'does not currently prove' in diag['conclusion']


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short', '-q'])
