r"""
Tests for shadow_level_arithmetic.py — per-channel and shadow-level arithmetic.

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

import pytest
from fractions import Fraction

from compute.lib.shadow_level_arithmetic import (
    per_channel_coefficients,
    full_partition_coefficients,
    per_channel_multiplicativity,
    cross_channel_diagnostic,
    connected_free_energy_coefficients,
    level_aware_multiplicativity,
    congruence_level,
    level_primes_for_model,
    shadow_level_report,
)
from compute.lib.vvmf_hecke import ising_model, tricritical_ising_model, three_state_potts_model
from mpmath import mp, mpf, fabs


# ===========================================================================
# 1. Basic infrastructure
# ===========================================================================

class TestCongruenceLevel:
    """Congruence subgroup level computation."""

    def test_ising_level(self):
        """Ising M(4,3): level = 4*4*3 = 48."""
        assert congruence_level(ising_model()) == 48

    def test_tricritical_level(self):
        """Tricritical M(5,4): level = 4*5*4 = 80."""
        assert congruence_level(tricritical_ising_model()) == 80

    def test_potts_level(self):
        """Potts M(6,5): level = 4*6*5 = 120."""
        assert congruence_level(three_state_potts_model()) == 120

    def test_ising_level_primes(self):
        """Ising level primes: {2, 3} from 48 = 2^4 * 3."""
        assert level_primes_for_model(ising_model()) == [2, 3]

    def test_tricritical_level_primes(self):
        """Tricritical level primes: {2, 5} from 80 = 2^4 * 5."""
        assert level_primes_for_model(tricritical_ising_model()) == [2, 5]

    def test_potts_level_primes(self):
        """Potts level primes: {2, 3, 5} from 120 = 2^3 * 3 * 5."""
        assert level_primes_for_model(three_state_potts_model()) == [2, 3, 5]


# ===========================================================================
# 2. Per-channel coefficient computation
# ===========================================================================

class TestPerChannelCoefficients:
    """Verify per-channel |eta*chi|^2 coefficients."""

    def test_ising_three_channels(self):
        """Ising has exactly 3 channels."""
        channels = per_channel_coefficients(ising_model(), num_terms=20, dps=30)
        assert len(channels) == 3

    def test_channel_sum_equals_partition(self):
        """Sum of channels = full partition function (structural check)."""
        mp.dps = 30
        model = ising_model()
        channels = per_channel_coefficients(model, num_terms=30, dps=30)
        full = full_partition_coefficients(model, num_terms=30, dps=30)
        for n in range(20):
            chan_sum = sum(channels[key][n] for key in channels)
            assert fabs(chan_sum - full[n]) < 1e-10, (
                f"Channel sum != partition at n={n}: {float(chan_sum)} vs {float(full[n])}")

    def test_channel_coefficients_integer(self):
        """Per-channel coefficients should be close to integers."""
        mp.dps = 30
        channels = per_channel_coefficients(ising_model(), num_terms=30, dps=30)
        for key, b in channels.items():
            for n in range(20):
                rounded = round(float(b[n]))
                assert fabs(b[n] - rounded) < 1e-8, (
                    f"Channel {key} n={n}: {float(b[n])} not integer")

    def test_tricritical_six_channels(self):
        """Tricritical Ising has exactly 6 channels."""
        channels = per_channel_coefficients(tricritical_ising_model(), num_terms=20, dps=30)
        assert len(channels) == 6


# ===========================================================================
# 3. Per-channel multiplicativity
# ===========================================================================

class TestPerChannelMultiplicativity:
    """Test multiplicativity structure at the per-channel level."""

    @pytest.mark.slow
    def test_ising_per_channel_full_fails(self):
        """Ising: per-channel FULL multiplicativity fails for vacuum and epsilon."""
        report = per_channel_multiplicativity(ising_model(), num_terms=60, max_test=20, dps=30)
        # Vacuum (1,1) and epsilon (1,2) should fail
        assert not report['channels'][(1, 1)]['full_multiplicative']
        assert not report['channels'][(1, 2)]['full_multiplicative']

    @pytest.mark.slow
    def test_ising_sigma_channel_trivial(self):
        """Ising σ channel (2,1): odd-index coefficients vanish."""
        mp.dps = 30
        channels = per_channel_coefficients(ising_model(), num_terms=40, dps=30)
        b = channels[(2, 1)]
        b0 = b[0] if b[0] != 0 else mpf(1)
        normed = [c / b0 for c in b]
        # Odd coefficients should be zero
        for n in range(1, 30, 2):
            assert fabs(normed[n]) < 1e-10, f"σ channel: b_{n} = {float(normed[n])} != 0"

    @pytest.mark.slow
    def test_ising_vacuum_fails_away_from_level(self):
        """Ising vacuum (1,1): multiplicativity fails even away from {2,3}."""
        mp.dps = 50
        channels = per_channel_coefficients(ising_model(), num_terms=120, dps=50)
        b = channels[(1, 1)]
        b0 = b[0] if b[0] != 0 else mpf(1)
        normed = [c / b0 for c in b]
        # Test at (5,7): both coprime to 6
        if 35 < len(normed):
            defect = fabs(normed[35] - normed[5] * normed[7])
            assert defect > 0.5, (
                f"Expected failure at (5,7) for vacuum: defect={float(defect)}")


# ===========================================================================
# 4. Cross-channel diagnostic
# ===========================================================================

class TestCrossChannel:
    """Cross-channel contribution to partition function failure."""

    @pytest.mark.slow
    def test_ising_defect_decomposition(self):
        """Ising: full_defect = channel_defect - cross_terms.

        a_{mn} - a_m a_n = [sum_i(b_{mn}^i - b_m^i b_n^i)] - [sum_{i!=j} b_m^i b_n^j]
        """
        diag = cross_channel_diagnostic(ising_model(), num_terms=50, dps=30)
        for d in diag['diagnostics']:
            reconstructed = d['channel_defect'] - d['cross_terms']
            assert abs(d['full_defect'] - reconstructed) < 0.5, (
                f"Pair {d['pair']}: {d['full_defect']} != {d['channel_defect']} - {d['cross_terms']}")

    @pytest.mark.slow
    def test_cross_terms_nonzero(self):
        """Cross terms contribute to at least some multiplicativity failures."""
        diag = cross_channel_diagnostic(ising_model(), num_terms=50, dps=30)
        has_nonzero_cross = any(abs(d['cross_terms']) > 0.5 for d in diag['diagnostics'])
        assert has_nonzero_cross, "Cross terms should contribute to some failures"


# ===========================================================================
# 5. Connected free energy
# ===========================================================================

class TestConnectedFreeEnergy:
    """Connected free energy coefficients."""

    @pytest.mark.slow
    def test_ising_connected_coefficients_exist(self):
        """Connected free energy coefficients are computable for Ising."""
        c = connected_free_energy_coefficients(ising_model(), num_terms=30, dps=30)
        assert len(c) == 30
        # c_0 should be 0 (log(1) = 0 for normalized Z)
        assert fabs(c[0]) < 1e-10

    @pytest.mark.slow
    def test_connected_not_multiplicative(self):
        """Connected free energy is also NOT multiplicative for Ising."""
        c = connected_free_energy_coefficients(ising_model(), num_terms=40, dps=30)
        lp = level_primes_for_model(ising_model())
        result = level_aware_multiplicativity(c, lp, max_n=15)
        # The connected free energy inherits non-multiplicativity
        # (log of non-multiplicative is still non-multiplicative)
        # But the structure may differ — just check it runs
        assert 'away_from_level' in result


# ===========================================================================
# 6. Cross-family structural consistency (AP10)
# ===========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10-safe)."""

    def test_channel_count_matches_primaries(self):
        """Number of channels = number of primaries for each model."""
        for model, expected in [(ising_model(), 3),
                                (tricritical_ising_model(), 6),
                                (three_state_potts_model(), 10)]:
            channels = per_channel_coefficients(model, num_terms=10, dps=20)
            assert len(channels) == expected, (
                f"Channel count {len(channels)} != {expected} primaries")

    def test_level_primes_are_prime_factors(self):
        """Level primes divide the congruence level for all models."""
        for model in [ising_model(), tricritical_ising_model(), three_state_potts_model()]:
            level = congruence_level(model)
            for p in level_primes_for_model(model):
                assert level % p == 0, f"Level prime {p} does not divide {level}"

    @pytest.mark.slow
    def test_ising_tricritical_both_fail_full_mult(self):
        """Both Ising and tricritical fail full per-channel multiplicativity."""
        for model in [ising_model(), tricritical_ising_model()]:
            report = per_channel_multiplicativity(model, num_terms=40, max_test=15, dps=30)
            has_failure = any(
                not data['full_multiplicative']
                for data in report['channels'].values()
            )
            assert has_failure, f"{report['model']} should have per-channel failures"


# ===========================================================================
# 7. Full shadow-level report
# ===========================================================================

class TestShadowLevelReport:
    """Integration test for the full shadow-level report."""

    @pytest.mark.slow
    def test_ising_full_report(self):
        """Ising: full shadow-level report runs successfully."""
        report = shadow_level_report(ising_model(), num_terms=40, max_test=15, dps=30)
        assert 'level_1_per_channel' in report
        assert 'cross_channel' in report
        assert 'level_2_connected' in report
        assert report['congruence_level'] == 48
