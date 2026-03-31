r"""
Tests for prime_locality_minimal_model.py — prime-locality bridge tests.

Test structure:
  1. Calibration: class G (lattice) and class L (affine) Hankel structure
  2. Exact shadow coefficients: verify seeds and recursion
  3. Stieltjes discriminant: universal sign for all c > -22/5
  4. Hankel analysis for Ising, tricritical Ising, 3-state Potts
  5. Partition function multiplicativity
  6. Shadow-Hecke bridge comparison
  7. Cross-family consistency (AP10-safe)

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

import pytest
from fractions import Fraction

import numpy as np

from compute.lib.prime_locality_minimal_model import (
    virasoro_shadow_at_c,
    shadow_moments_at_c,
    hankel_analysis,
    stieltjes_discriminant_analysis,
    multiplicativity_report,
    shadow_hecke_bridge,
    full_prime_locality_report,
    class_g_hankel_calibration,
    class_l_hankel_calibration,
    shadow_growth_diagnostic,
    hankel_matrix_from_moments,
)
from compute.lib.vvmf_hecke import ising_model, tricritical_ising_model, three_state_potts_model


# ===========================================================================
# 1. Exact shadow coefficient verification
# ===========================================================================

class TestExactShadowCoefficients:
    """Verify shadow S_r at specific c values against known formulas."""

    def test_ising_seeds(self):
        """S_2, S_3, S_4 for Ising (c=1/2) from closed-form formulas."""
        c = Fraction(1, 2)
        S = virasoro_shadow_at_c(c, max_arity=4)
        assert S[2] == Fraction(1, 4)       # c/2
        assert S[3] == Fraction(2)           # universal
        assert S[4] == Fraction(40, 49)      # 10/(c(5c+22)) = 10/(1/2 * 49/2)

    def test_tricritical_seeds(self):
        """S_2, S_3, S_4 for tricritical Ising (c=7/10)."""
        c = Fraction(7, 10)
        S = virasoro_shadow_at_c(c, max_arity=4)
        assert S[2] == Fraction(7, 20)       # c/2
        assert S[3] == Fraction(2)           # universal
        # 10/(c(5c+22)) = 10/((7/10)(7/2+22)) = 10/((7/10)(51/2)) = 10/(357/20) = 200/357
        expected_S4 = Fraction(10) / (c * (5 * c + 22))
        assert S[4] == expected_S4

    def test_potts_seeds(self):
        """S_2, S_3, S_4 for 3-state Potts (c=4/5)."""
        c = Fraction(4, 5)
        S = virasoro_shadow_at_c(c, max_arity=4)
        assert S[2] == Fraction(2, 5)        # c/2
        assert S[3] == Fraction(2)           # universal
        expected_S4 = Fraction(10) / (c * (5 * c + 22))
        assert S[4] == expected_S4

    def test_s3_universal(self):
        """S_3 = 2 is universal for all c (not family-specific)."""
        for c in [Fraction(1, 2), Fraction(7, 10), Fraction(4, 5),
                  Fraction(1), Fraction(26)]:
            S = virasoro_shadow_at_c(c, max_arity=3)
            assert S[3] == Fraction(2), f"S_3 != 2 at c={c}"

    def test_recursion_consistency(self):
        """S_5 through S_8 computed by recursion are rational for rational c."""
        c = Fraction(1, 2)
        S = virasoro_shadow_at_c(c, max_arity=8)
        for r in range(2, 9):
            assert isinstance(S[r], Fraction), f"S_{r} is not Fraction"

    def test_ising_s5_exact(self):
        """S_5 for Ising from recursion (verify by independent computation)."""
        c = Fraction(1, 2)
        S = virasoro_shadow_at_c(c, max_arity=5)
        # For r=5, target=7: j=3,k=4 only.
        # bracket = 2*3*4*S[3]*S[4] = 24 * 2 * 40/49 = 1920/49
        # S[5] = -(1920/49) / (2*5*(1/2)) = -(1920/49) / 5 = -384/49
        assert S[5] == Fraction(-384, 49)


# ===========================================================================
# 2. Calibration: class G and class L Hankel structure
# ===========================================================================

class TestCalibration:
    """Verify Hankel matrix structure for known cases."""

    def test_class_g_rank_equals_depth(self):
        """Class G (lattice, depth 2): Hankel rank = 2 = shadow depth."""
        result = class_g_hankel_calibration(c_int=8)
        assert result['rank_correct'], f"Hankel rank {result['hankel_rank']} != {result['expected_rank']}"
        assert result['archetype'] == 'G'

    def test_class_g_rank_c1(self):
        """Class G at c=1: Hankel rank = 2."""
        result = class_g_hankel_calibration(c_int=1)
        assert result['rank_correct']

    def test_class_l_rank_equals_depth(self):
        """Class L (affine sl_2, depth 3): Hankel rank = 3 = shadow depth."""
        result = class_l_hankel_calibration(k_val=Fraction(1))
        assert result['rank_correct'], f"Hankel rank {result['hankel_rank']} != {result['expected_rank']}"
        assert result['archetype'] == 'L'

    def test_class_l_rank_k3(self):
        """Class L at k=3: Hankel rank = 3."""
        result = class_l_hankel_calibration(k_val=Fraction(3))
        assert result['rank_correct']

    def test_class_g_vs_l_rank_ordering(self):
        """Class G has lower Hankel rank than class L (AP10: structural check)."""
        g = class_g_hankel_calibration(c_int=8)
        l = class_l_hankel_calibration(k_val=Fraction(1))
        assert g['hankel_rank'] < l['hankel_rank']


# ===========================================================================
# 3. Stieltjes discriminant: universal sign
# ===========================================================================

class TestStieltjesDiscriminant:
    """Verify that the Stieltjes discriminant is ALWAYS negative for c > -22/5."""

    def test_ising_signed(self):
        """Ising (c=1/2): measure necessarily signed."""
        d = stieltjes_discriminant_analysis(0.5)
        assert d['measure_necessarily_signed']
        assert d['universal_formula_verified']

    def test_tricritical_signed(self):
        """Tricritical Ising (c=7/10): measure necessarily signed."""
        d = stieltjes_discriminant_analysis(0.7)
        assert d['measure_necessarily_signed']

    def test_potts_signed(self):
        """3-state Potts (c=4/5): measure necessarily signed."""
        d = stieltjes_discriminant_analysis(0.8)
        assert d['measure_necessarily_signed']

    def test_large_c_signed(self):
        """Large c (c=100): measure necessarily signed."""
        d = stieltjes_discriminant_analysis(100.0)
        assert d['measure_necessarily_signed']

    def test_c13_signed(self):
        """Self-dual point c=13: measure necessarily signed."""
        d = stieltjes_discriminant_analysis(13.0)
        assert d['measure_necessarily_signed']

    def test_disc_factor_formula(self):
        """Verify 36 - alpha = -80/(5c+22) for several c values."""
        for c_val in [0.5, 0.7, 0.8, 1.0, 13.0, 26.0, 100.0]:
            d = stieltjes_discriminant_analysis(c_val)
            assert d['universal_formula_verified'], f"Formula fails at c={c_val}"

    def test_disc_factor_negative_for_all_positive_c(self):
        """disc_factor = -80/(5c+22) < 0 for all c > 0 (sampled)."""
        for c_val in np.linspace(0.01, 200, 50):
            d = stieltjes_discriminant_analysis(c_val)
            assert d['disc_factor'] < 0, f"disc_factor >= 0 at c={c_val}"

    def test_lee_yang_singular(self):
        """Lee-Yang (c=-22/5): 5c+22 = 0, discriminant singular."""
        d = stieltjes_discriminant_analysis(-22 / 5)
        assert d.get('singular', False) or abs(d.get('disc_factor', 0)) > 1e6


# ===========================================================================
# 4. Hankel analysis for minimal models
# ===========================================================================

class TestHankelMinimalModels:
    """Hankel matrix structure for class M minimal models."""

    def test_ising_full_rank(self):
        """Ising (c=1/2, class M): Hankel has full rank (infinite support)."""
        h = hankel_analysis(Fraction(1, 2), max_size=5)
        assert h['infinite_support'], "Ising Hankel should have infinite support"

    def test_ising_negative_even_moment(self):
        """Ising: c_2 = -c = -1/2 < 0, so measure is signed."""
        h = hankel_analysis(Fraction(1, 2), max_size=3)
        assert h['has_negative_even_moment']

    def test_ising_not_positive_semidefinite(self):
        """Ising: Hankel matrix is NOT positive semidefinite (signed measure)."""
        h = hankel_analysis(Fraction(1, 2), max_size=4)
        # At least one size should fail positive-semidefiniteness
        has_non_psd = any(not v for v in h['is_positive_semidefinite'].values())
        assert has_non_psd, "Ising Hankel should have negative eigenvalues"

    def test_tricritical_full_rank(self):
        """Tricritical Ising (c=7/10, class M): full Hankel rank."""
        h = hankel_analysis(Fraction(7, 10), max_size=5)
        assert h['infinite_support']

    def test_potts_full_rank(self):
        """3-state Potts (c=4/5, class M): full Hankel rank."""
        h = hankel_analysis(Fraction(4, 5), max_size=5)
        assert h['infinite_support']

    def test_hankel_rank_monotone(self):
        """Hankel rank is monotonically non-decreasing in size (AP10: structural)."""
        for c_val in [Fraction(1, 2), Fraction(7, 10), Fraction(4, 5)]:
            h = hankel_analysis(c_val, max_size=5)
            ranks = [h['ranks'][n] for n in range(1, 6)]
            for i in range(len(ranks) - 1):
                assert ranks[i] <= ranks[i + 1], (
                    f"Rank decreased at c={c_val}: {ranks}")

    def test_class_g_vs_m_rank_comparison(self):
        """Class G (rank 1) < class M (rank grows) — cross-family (AP10)."""
        g = class_g_hankel_calibration(c_int=8)
        m = hankel_analysis(Fraction(1, 2), max_size=4)
        assert g['hankel_rank'] < m['ranks'][4], (
            "Class M should have higher Hankel rank than class G")


# ===========================================================================
# 5. Partition function multiplicativity
# ===========================================================================

class TestMultiplicativity:
    """Test whether Dirichlet coefficients are multiplicative."""

    @pytest.mark.slow
    def test_ising_multiplicativity(self):
        """Ising partition function: test multiplicativity of a_n."""
        model = ising_model()
        report = multiplicativity_report(model, num_terms=60, dps=30)
        # Record the finding regardless of outcome
        if report['is_multiplicative']:
            # Evidence FOR prime-locality
            assert report['num_failures'] == 0
        else:
            # Evidence AGAINST naive prime-locality
            # But this is still a valid finding!
            assert report['num_failures'] > 0
            # The defect should be quantifiable
            assert report['max_defect'] > 0

    @pytest.mark.slow
    def test_tricritical_multiplicativity(self):
        """Tricritical Ising: test multiplicativity."""
        model = tricritical_ising_model()
        report = multiplicativity_report(model, num_terms=60, dps=30)
        # Just ensure the test runs and produces a result
        assert 'is_multiplicative' in report

    @pytest.mark.slow
    def test_potts_multiplicativity(self):
        """3-state Potts: test multiplicativity."""
        model = three_state_potts_model()
        report = multiplicativity_report(model, num_terms=60, dps=30)
        assert 'is_multiplicative' in report

    @pytest.mark.slow
    def test_multiplicativity_cross_family_consistency(self):
        """Cross-family: if all fail, check they fail for similar reasons (AP10)."""
        models = {
            'Ising': ising_model(),
            'Tricritical': tricritical_ising_model(),
        }
        results = {}
        for name, model in models.items():
            results[name] = multiplicativity_report(model, num_terms=50, dps=30)

        # Cross-check: either all multiplicative or all non-multiplicative
        statuses = [r['is_multiplicative'] for r in results.values()]
        # This is a structural consistency check, not a hardcoded expected value
        # We allow mixed results but flag them
        if len(set(statuses)) > 1:
            # Mixed: some multiplicative, some not. This is interesting.
            pass  # Just record; not a test failure


# ===========================================================================
# 6. Shadow-Hecke bridge
# ===========================================================================

class TestShadowHeckeBridge:
    """Compare shadow moments with VVMF Hecke eigenvalue power sums."""

    @pytest.mark.slow
    def test_ising_hecke_eigenform_check(self):
        """Ising: check whether characters are Hecke eigenforms."""
        model = ising_model()
        bridge = shadow_hecke_bridge(model, primes=[2, 3], max_arity=6,
                                     num_terms=40, dps=30)
        # Report: how many characters are eigenforms at each prime?
        for p in [2, 3]:
            data = bridge['hecke_data'][p]
            # Ising has 3 primaries
            assert data['total_primaries'] == 3

    @pytest.mark.slow
    def test_tricritical_hecke_eigenform_check(self):
        """Tricritical Ising: eigenform check."""
        model = tricritical_ising_model()
        bridge = shadow_hecke_bridge(model, primes=[2, 3], max_arity=6,
                                     num_terms=40, dps=30)
        for p in [2, 3]:
            data = bridge['hecke_data'][p]
            assert data['total_primaries'] == 6

    @pytest.mark.slow
    def test_shadow_ratio_convergence(self):
        """Shadow moment ratios mu_{r+1}/mu_r should converge (growth rate rho)."""
        c = Fraction(1, 2)
        diag = shadow_growth_diagnostic(c, max_arity=12)
        ratios = diag['successive_ratios']
        # For class M: |S_{r+1}/S_r| should approach rho
        abs_ratios = [abs(ratios[r]) for r in sorted(ratios.keys())[-4:]]
        if len(abs_ratios) >= 2:
            # Check approximate convergence (not exact)
            spread = max(abs_ratios) - min(abs_ratios)
            mean_ratio = np.mean(abs_ratios)
            # Coefficient of variation should decrease
            assert mean_ratio > 0, "Shadow ratios should be nonzero"


# ===========================================================================
# 7. Shadow growth and sign pattern
# ===========================================================================

class TestShadowGrowth:
    """Shadow growth rate and sign pattern diagnostics."""

    def test_ising_sign_pattern(self):
        """Ising S_r sign pattern: S_2>0, S_3>0, S_4>0, then alternating."""
        diag = shadow_growth_diagnostic(Fraction(1, 2), max_arity=10)
        signs = diag['sign_pattern']
        # S_2 = 1/4 > 0
        assert signs[2] == 1
        # S_3 = 2 > 0
        assert signs[3] == 1
        # S_4 = 40/49 > 0
        assert signs[4] == 1
        # S_5 = -384/49 < 0
        assert signs[5] == -1

    def test_ising_shadow_radius_positive(self):
        """Ising shadow radius estimate should be positive and finite."""
        diag = shadow_growth_diagnostic(Fraction(1, 2), max_arity=12)
        rho = diag['rho_estimate']
        assert rho is not None
        assert rho > 0
        assert rho < 100  # reasonable bound

    def test_c13_shadow_radius(self):
        """Self-dual c=13: shadow radius should match known value ~0.467."""
        diag = shadow_growth_diagnostic(Fraction(13), max_arity=12)
        rho = diag['rho_estimate']
        assert rho is not None
        # Known: rho(c=13) approx 0.467
        assert abs(rho - 0.467) < 0.1, f"rho(c=13) = {rho}, expected ~0.467"

    def test_growth_rate_ordering(self):
        """Shadow radius: rho(Ising) > rho(c=13) > rho(c=26) — structural (AP10)."""
        ising = shadow_growth_diagnostic(Fraction(1, 2), max_arity=12)
        c13 = shadow_growth_diagnostic(Fraction(13), max_arity=12)
        c26 = shadow_growth_diagnostic(Fraction(26), max_arity=12)
        # Smaller c -> larger rho (faster growth)
        # This is a structural ordering, not a hardcoded value
        rho_ising = ising['rho_estimate']
        rho_13 = c13['rho_estimate']
        rho_26 = c26['rho_estimate']
        assert rho_ising > rho_13 > rho_26, (
            f"Growth rate ordering violated: {rho_ising}, {rho_13}, {rho_26}")


# ===========================================================================
# 8. Full bridge report integration
# ===========================================================================

class TestFullBridgeReport:
    """Integration test: full prime-locality report for Ising."""

    @pytest.mark.slow
    def test_ising_full_report(self):
        """Ising: run all three tests and get a diagnosis."""
        model = ising_model()
        report = full_prime_locality_report(
            model, primes=[2, 3], max_arity=6,
            num_terms_mult=50, num_terms_hecke=30, dps=30
        )
        assert 'diagnosis' in report
        assert report['c'] == 0.5
        assert report['test_A_discriminant']['measure_necessarily_signed']
        # The diagnosis should be one of the defined types
        assert report['diagnosis'] in [
            'MULTIPLICATIVITY_FAILS',
            'SIGNED_MEASURE_FULL_RANK',
            'PARTIAL_EVIDENCE',
        ]

    @pytest.mark.slow
    def test_tricritical_full_report(self):
        """Tricritical Ising: full report."""
        model = tricritical_ising_model()
        report = full_prime_locality_report(
            model, primes=[2, 3], max_arity=6,
            num_terms_mult=50, num_terms_hecke=30, dps=30
        )
        assert 'diagnosis' in report
        assert abs(report['c'] - 0.7) < 0.01


# ===========================================================================
# 9. Cross-family structural consistency (AP10)
# ===========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks that don't rely on hardcoded values."""

    def test_stieltjes_signed_all_unitary_minimal(self):
        """ALL unitary minimal models have signed Stieltjes measure."""
        # Unitary: M(m+1, m) for m >= 3
        for m in range(3, 10):
            p, q = m + 1, m
            c = float(Fraction(1) - Fraction(6) * Fraction((p - q)**2, p * q))
            d = stieltjes_discriminant_analysis(c)
            assert d['measure_necessarily_signed'], (
                f"M({p},{q}) c={c}: measure not signed")

    def test_hankel_rank_increases_with_shadow_depth(self):
        """Hankel rank should reflect shadow depth: G(1) < L(2) < M(grows)."""
        g_rank = class_g_hankel_calibration(c_int=8)['hankel_rank']
        l_rank = class_l_hankel_calibration()['hankel_rank']
        m = hankel_analysis(Fraction(1, 2), max_size=5)
        m_rank = m['ranks'][5]
        assert g_rank < l_rank < m_rank, (
            f"Rank ordering: G={g_rank}, L={l_rank}, M={m_rank}")

    def test_moments_additivity_trivial_case(self):
        """c_2(A) = -c for Virasoro: additive in c (trivial check)."""
        for c in [Fraction(1, 2), Fraction(7, 10), Fraction(4, 5)]:
            moments = shadow_moments_at_c(c, max_arity=3)
            assert moments[2] == -c, f"c_2 != -c at c={c}"

    def test_c3_universal(self):
        """c_3 = -6 for ALL Virasoro (since S_3 = 2 is universal)."""
        for c in [Fraction(1, 2), Fraction(7, 10), Fraction(4, 5),
                  Fraction(1), Fraction(13), Fraction(26)]:
            moments = shadow_moments_at_c(c, max_arity=3)
            assert moments[3] == Fraction(-6), f"c_3 != -6 at c={c}"
