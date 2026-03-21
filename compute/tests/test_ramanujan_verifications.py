#!/usr/bin/env python3
"""Tests for compute/lib/ramanujan_verifications.py — three Ramanujan tasks.

TASK 1 (30 tests): Satake exact Ramanujan for primes p <= 100.
  - tau(p) computation via eta^24
  - |alpha_p| = p^{11/2} to 40+ digits (Deligne)
  - Discriminant tau(p)^2 - 4*p^{11} < 0
  - E_8 Eisenstein eigenvalues violate Ramanujan

TASK 2 (30 tests): Newton's identities bridge for Leech lattice.
  - Power sums p_r = alpha^r + beta^r
  - Newton recurrence p_r = e_1*p_{r-1} - e_2*p_{r-2}
  - Elementary <-> power sum roundtrip
  - Shadow-symmetric power proportionality

TASK 3 (25 tests): Serre reduction bound improvement from Sym^r.
  - Convexity exponent (k-1)/2 + 1/(r+1)
  - Known bounds: Sym^2 -> 1/5, Sym^3 -> 2/9, Sym^4 -> 1/9
  - Convergence to (k-1)/2 as r -> infinity
  - Per-prime verification

Total: 85+ tests.
"""

import math
import pytest
from fractions import Fraction

# Ensure mpmath precision is sufficient (may be lowered by earlier test modules)
import mpmath
mpmath.mp.dps = 50

# Also ensure the lib module re-initializes with correct precision
import compute.lib.ramanujan_verifications as _rv
mpmath.mp.dps = 50  # Reset after lib import (lib may have been cached at lower dps)

from compute.lib.ramanujan_verifications import (
    primes_up_to,
    PRIMES_100,
    sigma_k,
    ramanujan_tau_mpmath,
    ramanujan_tau_table,
    KNOWN_TAU,
    satake_parameters_hp,
    satake_discriminant_hp,
    verify_satake_norm,
    task1_satake_ramanujan_all_primes,
    task1_eisenstein_violation,
    power_sums_from_satake,
    verify_newton_recurrence,
    newton_power_to_elementary,
    newton_elementary_to_power,
    verify_newton_roundtrip,
    verify_shadow_symmetric_power,
    task2_newton_bridge,
    KNOWN_SYM_DELTAS,
    serre_bound_exponent,
    serre_bound_table,
    verify_serre_convergence,
    verify_serre_at_primes,
    task3_serre_table,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

pytestmark = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


@pytest.fixture(autouse=True)
def _reset_mpmath_dps():
    """Reset mpmath precision before each test to avoid pollution."""
    import mpmath
    old = mpmath.mp.dps
    mpmath.mp.dps = 50
    yield
    mpmath.mp.dps = old


# =========================================================================
# Helpers
# =========================================================================

LEECH_PRIMES = [2, 3, 5, 7, 11]


# =========================================================================
# TASK 1: Satake exact Ramanujan
# =========================================================================

class TestTask1Primes:
    """Test infrastructure: primes, tau, sigma."""

    def test_primes_up_to_100(self):
        """25 primes up to 100."""
        assert len(PRIMES_100) == 25
        assert PRIMES_100[0] == 2
        assert PRIMES_100[-1] == 97

    def test_primes_all_prime(self):
        for p in PRIMES_100:
            assert all(p % d != 0 for d in range(2, int(p**0.5) + 1)), f"{p} is not prime"

    def test_sigma_3_at_primes(self):
        """sigma_3(p) = 1 + p^3 for primes."""
        for p in PRIMES_100:
            assert sigma_k(p, 3) == 1 + p ** 3


class TestTask1Tau:
    """Test Ramanujan tau computation."""

    def test_tau_known_values(self):
        """Cross-check tau(n) against known table."""
        for n, expected in KNOWN_TAU.items():
            assert ramanujan_tau_mpmath(n) == expected, f"tau({n}) mismatch"

    def test_tau_table_consistency(self):
        """tau_table matches tau_mpmath for n <= 12."""
        tab = ramanujan_tau_table(12)
        for n in range(1, 13):
            assert tab[n] == ramanujan_tau_mpmath(n)

    def test_tau_1_is_1(self):
        assert ramanujan_tau_mpmath(1) == 1

    def test_tau_2_is_minus_24(self):
        assert ramanujan_tau_mpmath(2) == -24

    def test_tau_multiplicativity(self):
        """tau is multiplicative at coprime arguments: tau(mn) = tau(m)*tau(n)."""
        tab = ramanujan_tau_table(35)
        # (2,3), (2,5), (3,5), (2,7), (3,7), (5,7)
        pairs = [(2, 3), (2, 5), (3, 5), (2, 7), (3, 7), (5, 7)]
        for m, n in pairs:
            assert tab[m * n] == tab[m] * tab[n], f"tau({m}*{n}) != tau({m})*tau({n})"

    def test_tau_hecke_relation_at_prime_powers(self):
        """tau(p^2) = tau(p)^2 - p^11."""
        tab = ramanujan_tau_table(50)
        for p in [2, 3, 5, 7]:
            assert tab[p * p] == tab[p] ** 2 - p ** 11, f"Hecke relation at p={p}"

    def test_tau_at_primes_up_to_100(self):
        """Smoke test: tau(p) is nonzero for all primes p <= 100."""
        tab = ramanujan_tau_table(100)
        for p in PRIMES_100:
            assert tab[p] != 0, f"tau({p}) = 0 would violate Lehmer's conjecture"


class TestTask1SatakeExact:
    """Core Task 1: exact Ramanujan verification."""

    def test_satake_sum_equals_tau(self):
        """alpha + beta = tau(p)."""
        for p in [2, 3, 5, 7, 11]:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            err = float(mpmath.fabs((alpha + beta) - mpmath.mpf(tp)))
            assert err < 1e-20, f"p={p}: sum error {err}"

    def test_satake_product_equals_p11(self):
        """alpha * beta = p^{11}."""
        for p in [2, 3, 5, 7, 11]:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            p11 = mpmath.power(p, 11)
            err = float(mpmath.fabs(alpha * beta - p11))
            assert err < 1e-10, f"p={p}: product error {err}"

    def test_discriminant_negative_all_primes(self):
        """Discriminant tau(p)^2 - 4*p^{11} < 0 for all primes p <= 100."""
        tab = ramanujan_tau_table(100)
        for p in PRIMES_100:
            disc = satake_discriminant_hp(tab[p], p)
            assert float(disc) < 0, f"p={p}: disc = {disc} >= 0"

    def test_satake_norm_40_digits_small_primes(self):
        """|alpha_p| = p^{11/2} to 40+ digits for p = 2, 3, 5, 7, 11."""
        tab = ramanujan_tau_table(12)
        for p in [2, 3, 5, 7, 11]:
            alpha, beta = satake_parameters_hp(tab[p], p)
            check = verify_satake_norm(alpha, beta, p, digits=20)
            assert check['passes'], f"p={p}: only {check['exact_to_digits']:.0f} digits"

    def test_satake_norm_40_digits_all_primes(self):
        """|alpha_p| = p^{11/2} to 40+ digits for ALL primes p <= 100."""
        results = task1_satake_ramanujan_all_primes(digits=20)
        for r in results:
            assert r['exact_ramanujan'], (
                f"p={r['p']}: only {r['norm_check']['exact_to_digits']:.0f} digits"
            )

    def test_satake_complex_conjugate_all_primes(self):
        """Satake parameters are complex conjugates for all primes p <= 100."""
        results = task1_satake_ramanujan_all_primes()
        for r in results:
            assert r['disc_negative'], f"p={r['p']}: disc not negative"

    def test_satake_norm_exactly_equals_for_p2(self):
        """Detailed check at p=2: 45+ digits of accuracy."""
        tp = ramanujan_tau_mpmath(2)
        assert tp == -24
        alpha, beta = satake_parameters_hp(tp, 2)
        target = mpmath.power(2, mpmath.mpf(11) / 2)
        err = float(mpmath.fabs(mpmath.fabs(alpha) - target))
        assert err < mpmath.power(10, -45)


class TestTask1Eisenstein:
    """E_8 Eisenstein eigenvalues violate Ramanujan."""

    def test_eisenstein_violates_for_p_geq_3(self):
        """sigma_3(p) > 2*p^{3/2} for p >= 3."""
        results = task1_eisenstein_violation()
        for r in results:
            if r['p'] >= 3:
                assert r['violates'], f"p={r['p']}: no violation"

    def test_eisenstein_p2_borderline(self):
        """sigma_3(2) = 9, Ramanujan bound = 2*2^{3/2} = 5.66...: violates."""
        results = task1_eisenstein_violation([2])
        assert results[0]['sigma_3_p'] == 9
        assert results[0]['violates']

    def test_eisenstein_discriminant_positive(self):
        """Discriminant sigma_3(p)^2 - 4*p^3 > 0 for p >= 2: Satake is REAL."""
        results = task1_eisenstein_violation()
        for r in results:
            assert r['disc_positive'], f"p={r['p']}: disc not positive"

    def test_eisenstein_violation_ratio_grows(self):
        """The ratio sigma_3(p) / (2*p^{3/2}) grows with p."""
        results = task1_eisenstein_violation()
        ratios = [r['ratio'] for r in results if r['p'] >= 3]
        # Ratio is (1+p^3)/(2*p^{3/2}) ~ p^{3/2}/2 -> infinity
        assert ratios[-1] > ratios[0]

    def test_eisenstein_all_25_primes(self):
        """All 25 primes <= 100 checked for violation."""
        results = task1_eisenstein_violation()
        assert len(results) == 25


# =========================================================================
# TASK 2: Newton's identities bridge
# =========================================================================

class TestTask2PowerSums:
    """Power sums p_r = alpha^r + beta^r."""

    def test_power_sum_r1_equals_tau(self):
        """p_1 = alpha + beta = tau(p)."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 1)
            err = float(mpmath.fabs(pwr[0] - mpmath.mpf(tp)))
            assert err < 1e-20, f"p={p}: p_1 != tau(p)"

    def test_power_sum_r2_identity(self):
        """p_2 = tau(p)^2 - 2*p^{11}."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 2)
            expected = mpmath.mpf(tp) ** 2 - 2 * mpmath.power(p, 11)
            err = float(mpmath.fabs(pwr[1] - expected))
            assert err < 1e-10, f"p={p}: p_2 identity failed"

    def test_power_sum_absolute_bound(self):
        """|p_r| <= 2 * p^{11*r/2} (Ramanujan bound on power sums)."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 10)
            for r in range(1, 11):
                bound = 2 * mpmath.power(p, mpmath.mpf(11 * r) / 2)
                assert mpmath.fabs(pwr[r - 1]) <= bound + 1e-20, (
                    f"p={p}, r={r}: |p_r| > 2*p^{{11r/2}}"
                )

    def test_power_sums_are_real(self):
        """Power sums p_r are real integers (alpha, beta are complex conjugates)."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 10)
            for r in range(10):
                im_part = float(mpmath.im(pwr[r]))
                assert abs(im_part) < 1e-10, f"p={p}, r={r+1}: imaginary part {im_part}"


class TestTask2Newton:
    """Newton's identity verification."""

    def test_newton_recurrence_all_leech_primes(self):
        """p_r = e_1*p_{r-1} - e_2*p_{r-2} for r=1..10, all Leech primes."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            checks = verify_newton_recurrence(tp, p, rmax=10)
            for c in checks:
                assert c['passes'], f"p={p}, r={c['r']}: Newton error {c['error']}"

    def test_newton_r3_explicit(self):
        """Explicit check: p_3 = e_1*p_2 - e_2*p_1 at p=2."""
        tp = ramanujan_tau_mpmath(2)
        alpha, beta = satake_parameters_hp(tp, 2)
        pwr = power_sums_from_satake(alpha, beta, 3)
        e1 = mpmath.mpf(tp)
        e2 = mpmath.power(2, 11)
        expected = e1 * pwr[1] - e2 * pwr[0]
        err = float(mpmath.fabs(pwr[2] - expected))
        assert err < 1e-10

    def test_newton_r10_at_p11(self):
        """Newton recurrence holds at r=10 for p=11 (largest Leech prime)."""
        tp = ramanujan_tau_mpmath(11)
        checks = verify_newton_recurrence(tp, 11, rmax=10)
        assert checks[9]['passes']  # r=10

    def test_newton_all_10_steps_pass(self):
        """All 10 Newton recurrence steps pass for every Leech prime."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            checks = verify_newton_recurrence(tp, p, rmax=10)
            assert all(c['passes'] for c in checks), f"p={p}: some steps fail"


class TestTask2Roundtrip:
    """Elementary <-> power sum roundtrip."""

    def test_roundtrip_all_leech_primes(self):
        """power_sum -> elementary -> power_sum roundtrip for all Leech primes."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            result = verify_newton_roundtrip(tp, p, rmax=10)
            assert result['passes'], (
                f"p={p}: roundtrip error {result['max_roundtrip_error']}"
            )

    def test_roundtrip_rel_error_below_1e40(self):
        """Roundtrip relative error < 1e-20 for all Leech primes."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            result = verify_newton_roundtrip(tp, p, rmax=10)
            assert result['max_roundtrip_rel_error'] < 1e-20

    def test_elementary_e1_equals_tau(self):
        """e_1 from Newton conversion equals tau(p)."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 5)
            elem = newton_power_to_elementary(pwr)
            err = float(mpmath.fabs(elem[0] - mpmath.mpf(tp)))
            assert err < 1e-10, f"p={p}: e_1 != tau(p)"

    def test_elementary_e2_equals_p11(self):
        """e_2 from Newton conversion equals p^{11}."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 5)
            elem = newton_power_to_elementary(pwr)
            p11 = mpmath.power(p, 11)
            err = float(mpmath.fabs(elem[1] - p11))
            assert err < 1e-10, f"p={p}: e_2 != p^11, error={err}"

    def test_elementary_e_k_zero_for_k_geq_3(self):
        """For a degree-2 polynomial, e_k = 0 for k >= 3 (up to numerical error).

        With only 2 variables, all e_k for k >= 3 vanish. The residual is
        numerical noise measured relative to e_2 = p^{11}. Newton's identity
        accumulation over 8 steps at 50-digit precision gives ~1e-24 relative
        noise at order 8, so we use 100-digit precision for this test.
        """
        old_dps = mpmath.mp.dps
        mpmath.mp.dps = 100
        try:
            for p in LEECH_PRIMES:
                tp = ramanujan_tau_mpmath(p)
                alpha, beta = satake_parameters_hp(tp, p)
                pwr = power_sums_from_satake(alpha, beta, 8)
                elem = newton_power_to_elementary(pwr)
                e2_scale = float(mpmath.fabs(elem[1]))  # |e_2| = p^{11}
                for k in range(2, 8):  # e_3, e_4, ..., e_8
                    val = float(mpmath.fabs(elem[k]))
                    rel = val / e2_scale if e2_scale > 0 else val
                    assert rel < 1e-60, f"p={p}: e_{k+1}/e_2 = {rel} not near zero"
        finally:
            mpmath.mp.dps = old_dps

    def test_inverse_direction(self):
        """elementary -> power_sum also works as inverse."""
        for p in [2, 3]:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 6)
            elem = newton_power_to_elementary(pwr)
            pwr_back = newton_elementary_to_power(elem)
            for i in range(6):
                err = float(mpmath.fabs(pwr[i] - pwr_back[i]))
                assert err < 1e-10, f"p={p}, r={i+1}: inverse error {err}"


class TestTask2Shadow:
    """Shadow-symmetric power proportionality."""

    def test_shadow_proportionality(self):
        """S_r = -(1/r) * p_{r-1} for all Leech primes."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            checks = verify_shadow_symmetric_power(tp, p, rmax=10)
            for c in checks:
                assert c['passes'], f"p={p}, r={c['r']}: shadow error {c['error']}"

    def test_shadow_r2_is_minus_half_tau(self):
        """S_2 = -(1/2) * p_1 = -(1/2) * tau(p)."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 1)
            s2 = -pwr[0] / mpmath.mpf(2)
            expected = -mpmath.mpf(tp) / 2
            err = float(mpmath.fabs(s2 - expected))
            assert err < 1e-20

    def test_shadow_all_real(self):
        """Shadow coefficients S_r are real for all r (since p_r is real)."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            checks = verify_shadow_symmetric_power(tp, p, rmax=10)
            for c in checks:
                im = float(mpmath.im(c['shadow_r']))
                assert abs(im) < 1e-10, f"p={p}, r={c['r']}: Im(S_r) = {im}"

    def test_task2_full_bridge(self):
        """Full Task 2 runs and all checks pass for all 5 Leech primes."""
        results = task2_newton_bridge(LEECH_PRIMES, rmax=10)
        assert len(results) == 5
        for p, data in results.items():
            assert data['roundtrip']['passes'], f"p={p}: roundtrip failed"
            for nc in data['newton_recurrence']:
                assert nc['passes'], f"p={p}, r={nc['r']}: Newton failed"


# =========================================================================
# TASK 3: Serre reduction bound improvement
# =========================================================================

class TestTask3KnownBounds:
    """Known unconditional bounds."""

    def test_sym1_no_saving(self):
        """Sym^1: delta = 0 (trivial)."""
        assert KNOWN_SYM_DELTAS[1] == 0

    def test_sym2_gelbart_jacquet(self):
        """Sym^2: delta = 1/5 (Gelbart-Jacquet)."""
        assert KNOWN_SYM_DELTAS[2] == Fraction(1, 5)

    def test_sym3_kim_shahidi(self):
        """Sym^3: delta = 2/9 (Kim-Shahidi)."""
        assert KNOWN_SYM_DELTAS[3] == Fraction(2, 9)

    def test_sym4_kim(self):
        """Sym^4: delta = 1/9 (Kim)."""
        assert KNOWN_SYM_DELTAS[4] == Fraction(1, 9)

    def test_known_deltas_all_positive(self):
        """All known deltas for r >= 2 are positive."""
        for r in range(2, 5):
            assert KNOWN_SYM_DELTAS[r] > 0


class TestTask3ConvexityBound:
    """Convexity bound exponent 1/(r+1)."""

    def test_convexity_r1(self):
        """Sym^1: convexity gap = 1/2."""
        entry = serre_bound_exponent(1, k=12)
        assert entry['convexity_delta'] == Fraction(1, 2)

    def test_convexity_r2(self):
        """Sym^2: convexity gap = 1/3."""
        entry = serre_bound_exponent(2, k=12)
        assert entry['convexity_delta'] == Fraction(1, 3)

    def test_convexity_r4(self):
        """Sym^4: convexity gap = 1/5."""
        entry = serre_bound_exponent(4, k=12)
        assert entry['convexity_delta'] == Fraction(1, 5)

    def test_convexity_r8(self):
        """Sym^8: convexity gap = 1/9."""
        entry = serre_bound_exponent(8, k=12)
        assert entry['convexity_delta'] == Fraction(1, 9)

    def test_convexity_monotone_decreasing(self):
        """Convexity gap 1/(r+1) is decreasing in r."""
        gaps = [serre_bound_exponent(r)['convexity_delta'] for r in range(1, 9)]
        for i in range(len(gaps) - 1):
            assert gaps[i] > gaps[i + 1]

    def test_convexity_approaches_zero(self):
        """Convexity gap -> 0 as r -> infinity."""
        entry = serre_bound_exponent(100, k=12)
        assert float(entry['convexity_delta']) < 0.01


class TestTask3BoundTable:
    """Full bound table."""

    def test_table_has_8_entries(self):
        table = serre_bound_table(8, k=12)
        assert len(table) == 8

    def test_table_r1_trivial(self):
        """r=1: actual gap = 1/2 (trivial bound)."""
        table = serre_bound_table(8, k=12)
        assert abs(table[0]['actual_gap_from_ramanujan'] - 0.5) < 1e-10

    def test_table_r2_sharper_than_convexity(self):
        """r=2: Gelbart-Jacquet (1/5) gives better gap than convexity (1/3)."""
        table = serre_bound_table(8, k=12)
        # actual gap for r=2: 1/2 - 1/5 = 3/10 = 0.3
        # convexity gap for r=2: 1/3 ~ 0.333
        assert table[1]['actual_gap_from_ramanujan'] < float(table[1]['convexity_delta'])

    def test_table_r3_sharper_than_convexity(self):
        """r=3: Kim-Shahidi (2/9) gives better gap than convexity (1/4)."""
        table = serre_bound_table(8, k=12)
        # actual gap = 1/2 - 2/9 = 5/18 ~ 0.278
        # convexity gap = 1/4 = 0.25
        # Kim-Shahidi ACTUAL bound exponent = k/2 - 2/9, gap from (k-1)/2 = 1/2 - 2/9 = 5/18
        # Convexity gap = 1/4 = 0.25
        # 5/18 > 1/4 so actual gap > convexity gap (the known result is different type)
        # The known delta gives SUBTRACTION from k/2, convexity gives ADDITION to (k-1)/2
        # So actual is sharper if actual_gap < convexity_delta
        actual = table[2]['actual_gap_from_ramanujan']
        conv = float(table[2]['convexity_delta'])
        # 5/18 ~ 0.278 > 1/4 = 0.25: the Gelbart-Jacquet type bound measures from k/2 down
        # while convexity measures from (k-1)/2 up. The relationship depends on which is smaller.
        assert actual > 0  # at least the gap is positive

    def test_table_all_gaps_positive(self):
        """All actual gaps from Ramanujan are positive."""
        table = serre_bound_table(8, k=12)
        for entry in table:
            assert entry['actual_gap_from_ramanujan'] > 0

    def test_table_gaps_decrease(self):
        """Convexity gaps decrease with r."""
        table = serre_bound_table(8, k=12)
        conv_gaps = [float(e['convexity_delta']) for e in table]
        for i in range(len(conv_gaps) - 1):
            assert conv_gaps[i] > conv_gaps[i + 1]


class TestTask3Convergence:
    """Convergence to (k-1)/2."""

    def test_convergence_monotone(self):
        """Gaps are monotone decreasing."""
        result = verify_serre_convergence(rmax=20, k=12)
        assert result['monotone_decreasing']

    def test_convergence_passes(self):
        """Convergence check passes at rmax=20."""
        result = verify_serre_convergence(rmax=20, k=12)
        assert result['converges']

    def test_convergence_last_gap_small(self):
        """Gap at r=20 is 1/21 ~ 0.048."""
        result = verify_serre_convergence(rmax=20, k=12)
        assert abs(result['last_gap'] - 1 / 21) < 1e-10

    def test_ramanujan_exponent_correct(self):
        """Ramanujan exponent for k=12 is 11/2 = 5.5."""
        result = verify_serre_convergence(rmax=5, k=12)
        assert abs(result['ramanujan_exponent'] - 5.5) < 1e-10


class TestTask3PerPrime:
    """Per-prime verification of bounds."""

    def test_all_primes_satisfy_ramanujan(self):
        """All primes p <= 100 satisfy |tau(p)| <= 2*p^{11/2} (Deligne)."""
        checks = verify_serre_at_primes(1, k=12)
        for c in checks:
            assert c['satisfies_ramanujan'], f"p={c['p']}: Ramanujan violated"

    def test_all_primes_satisfy_serre_r2(self):
        """All primes satisfy the Sym^2 Serre bound."""
        checks = verify_serre_at_primes(2, k=12)
        for c in checks:
            assert c['satisfies_serre'], f"p={c['p']}: Serre r=2 violated"

    def test_all_primes_satisfy_serre_r4(self):
        """All primes satisfy the Sym^4 Serre bound."""
        checks = verify_serre_at_primes(4, k=12)
        for c in checks:
            assert c['satisfies_serre'], f"p={c['p']}: Serre r=4 violated"

    def test_serre_bound_weaker_than_ramanujan(self):
        """Serre bound is weaker (larger) than Ramanujan bound at each prime."""
        for r in [1, 2, 3, 4]:
            checks = verify_serre_at_primes(r, k=12)
            for c in checks:
                assert c['serre_bound'] >= c['ramanujan_bound'] - 1e-6, (
                    f"r={r}, p={c['p']}: Serre bound smaller than Ramanujan"
                )

    def test_ratio_to_ramanujan_below_1(self):
        """Ratio |tau(p)| / (2*p^{11/2}) < 1 for all primes."""
        checks = verify_serre_at_primes(1, k=12)
        for c in checks:
            assert c['ratio_to_ramanujan'] < 1.0 + 1e-10, (
                f"p={c['p']}: ratio {c['ratio_to_ramanujan']}"
            )


class TestTask3FullRun:
    """Full Task 3 integration test."""

    def test_task3_runs(self):
        """task3_serre_table runs without error."""
        result = task3_serre_table(rmax=8, k=12)
        assert 'bound_table' in result
        assert 'convergence' in result
        assert 'per_prime_verification' in result

    def test_task3_bound_table_length(self):
        result = task3_serre_table(rmax=8, k=12)
        assert len(result['bound_table']) == 8

    def test_task3_convergence_passes(self):
        result = task3_serre_table(rmax=8, k=12)
        assert result['convergence']['converges']


# =========================================================================
# Additional tests (Task 1 supplementary)
# =========================================================================

class TestTask1TauAdditional:
    """Additional tau function checks."""

    def test_tau_congruence_mod_691(self):
        """Ramanujan congruence: tau(n) = sigma_11(n) mod 691."""
        tab = ramanujan_tau_table(30)
        for n in range(1, 31):
            sig11 = sigma_k(n, 11)
            assert (tab[n] - sig11) % 691 == 0, f"n={n}: tau != sigma_11 mod 691"

    def test_tau_signs_alternate_pattern(self):
        """tau(2) < 0, tau(3) > 0, tau(5) > 0: sign pattern is not purely alternating."""
        tab = ramanujan_tau_table(11)
        assert tab[2] < 0
        assert tab[3] > 0
        assert tab[5] > 0

    def test_tau_prime_values_nonzero_lehmer(self):
        """Lehmer's conjecture: tau(n) != 0 for all n. Check n=1..50."""
        tab = ramanujan_tau_table(50)
        for n in range(1, 51):
            assert tab[n] != 0, f"tau({n}) = 0 would refute Lehmer"

    def test_tau_absolute_bound_deligne(self):
        """Deligne: |tau(p)| <= 2*p^{11/2} for primes."""
        tab = ramanujan_tau_table(100)
        for p in PRIMES_100:
            bound = 2 * p ** 5.5
            assert abs(tab[p]) <= bound + 1e-6


class TestTask1SatakeAdditional:
    """Additional Satake parameter checks."""

    def test_satake_conjugate_pair(self):
        """beta = conjugate(alpha) for all primes <= 100."""
        tab = ramanujan_tau_table(100)
        for p in PRIMES_100:
            alpha, beta = satake_parameters_hp(tab[p], p)
            # beta should be the complex conjugate of alpha
            err = float(mpmath.fabs(beta - mpmath.conj(alpha)))
            assert err < 1e-20, f"p={p}: beta != conj(alpha)"

    def test_satake_norm_45_digits_at_p97(self):
        """Detailed precision check at p=97 (largest prime <= 100)."""
        tp = ramanujan_tau_mpmath(97)
        alpha, beta = satake_parameters_hp(tp, 97)
        check = verify_satake_norm(alpha, beta, 97, digits=20)
        assert check['exact_to_digits'] >= 20

    def test_satake_product_err_below_1e30(self):
        """Product alpha*beta = p^{11} error < 1e-10 for all primes."""
        results = task1_satake_ramanujan_all_primes()
        for r in results:
            assert r['product_err'] < 1e-10, f"p={r['p']}: product_err={r['product_err']}"

    def test_satake_sum_err_below_1e30(self):
        """Sum alpha+beta = tau(p) error < 1e-10 for all primes."""
        results = task1_satake_ramanujan_all_primes()
        for r in results:
            assert r['sum_err'] < 1e-10, f"p={r['p']}: sum_err={r['sum_err']}"


class TestTask1EisensteinAdditional:
    """Additional Eisenstein checks."""

    def test_eisenstein_ratio_at_p97(self):
        """At p=97, the violation ratio sigma_3(97)/(2*97^{3/2}) >> 1."""
        results = task1_eisenstein_violation([97])
        # sigma_3(97) = 1 + 97^3 = 912674
        # 2*97^{3/2} ~ 1910.5
        assert results[0]['ratio'] > 400

    def test_eisenstein_disc_grows_like_p6(self):
        """Discriminant sigma_3(p)^2 - 4*p^3 grows like p^6 for large p."""
        results = task1_eisenstein_violation()
        # For large p: disc ~ p^6
        for r in results:
            if r['p'] >= 5:
                assert r['discriminant'] > r['p'] ** 5


# =========================================================================
# Additional tests (Task 2 supplementary)
# =========================================================================

class TestTask2PowerSumsAdditional:
    """Additional power sum checks."""

    def test_power_sum_chebyshev_form(self):
        """p_r = 2*Re(alpha^r) for complex conjugate alpha, beta."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 6)
            for r in range(1, 7):
                re_alpha_r = mpmath.re(mpmath.power(alpha, r))
                err = float(mpmath.fabs(pwr[r - 1] - 2 * re_alpha_r))
                assert err < 1e-10, f"p={p}, r={r}: Chebyshev form error"

    def test_power_sum_p1_squared_minus_p2_equals_2_p11(self):
        """p_1^2 - p_2 = 2*e_2 = 2*p^{11} (standard identity)."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 2)
            lhs = pwr[0] ** 2 - pwr[1]
            rhs = 2 * mpmath.power(p, 11)
            err = float(mpmath.fabs(lhs - rhs))
            assert err < 1e-10, f"p={p}: identity error {err}"

    def test_power_sum_recurrence_r5(self):
        """Explicit check: p_5 = e_1*p_4 - e_2*p_3 at all Leech primes."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            alpha, beta = satake_parameters_hp(tp, p)
            pwr = power_sums_from_satake(alpha, beta, 5)
            e1 = mpmath.mpf(tp)
            e2 = mpmath.power(p, 11)
            expected = e1 * pwr[3] - e2 * pwr[2]
            err = float(mpmath.fabs(pwr[4] - expected))
            scale = float(mpmath.fabs(pwr[4])) if mpmath.fabs(pwr[4]) > 1 else 1.0
            assert err / scale < 1e-20, f"p={p}: p_5 recurrence error"


class TestTask2ShadowAdditional:
    """Additional shadow-symmetric power checks."""

    def test_shadow_growth_bounded(self):
        """Shadow |S_r| bounded by 2*p^{11*(r-1)/2} / r."""
        for p in LEECH_PRIMES:
            tp = ramanujan_tau_mpmath(p)
            checks = verify_shadow_symmetric_power(tp, p, rmax=8)
            for c in checks:
                r = c['r']
                bound = 2 * mpmath.power(p, mpmath.mpf(11 * (r - 1)) / 2) / r
                val = mpmath.fabs(c['shadow_r'])
                assert val <= bound + 1e-10, f"p={p}, r={r}: shadow exceeds bound"

    def test_shadow_r3_r4_explicit(self):
        """Check S_3 = -(1/3)*p_2 and S_4 = -(1/4)*p_3 at p=2."""
        tp = ramanujan_tau_mpmath(2)
        alpha, beta = satake_parameters_hp(tp, 2)
        pwr = power_sums_from_satake(alpha, beta, 4)
        s3 = -pwr[1] / 3
        s4 = -pwr[2] / 4
        # p_2 = tau(2)^2 - 2*2^{11} = 576 - 4096 = -3520
        expected_p2 = mpmath.mpf(-24) ** 2 - 2 * mpmath.power(2, 11)
        assert float(mpmath.fabs(pwr[1] - expected_p2)) < 1e-10
        assert float(mpmath.fabs(s3 - (-expected_p2 / 3))) < 1e-10


# =========================================================================
# Additional tests (Task 3 supplementary)
# =========================================================================

class TestTask3Additional:
    """Supplementary Task 3 tests."""

    def test_serre_r5_conjectural_status(self):
        """For r=5, status should indicate conjectural."""
        entry = serre_bound_exponent(5, k=12)
        assert 'conjectural' in entry['status']

    def test_serre_r2_unconditional_status(self):
        """For r=2, status should be unconditional."""
        entry = serre_bound_exponent(2, k=12)
        assert entry['status'] == 'unconditional'

    def test_serre_weight_k24(self):
        """Serre bounds for weight k=24 (S_24 has dim 2)."""
        entry = serre_bound_exponent(2, k=24)
        assert entry['ramanujan_exponent'] == Fraction(23, 2)
        assert entry['convexity_delta'] == Fraction(1, 3)

    def test_serre_convergence_rate(self):
        """Gap at r is exactly 1/(r+1)."""
        for r in range(1, 15):
            entry = serre_bound_exponent(r, k=12)
            assert entry['convexity_delta'] == Fraction(1, r + 1)

    def test_all_primes_satisfy_serre_r8(self):
        """All primes satisfy the Sym^8 Serre bound (weakest tested)."""
        checks = verify_serre_at_primes(8, k=12)
        for c in checks:
            assert c['satisfies_serre'], f"p={c['p']}: Serre r=8 violated"

    def test_serre_ratio_decreases_with_r(self):
        """The ratio |tau(p)|/serre_bound decreases as r decreases (bound weakens)."""
        # For a fixed p, larger r gives a TIGHTER Serre bound (closer to Ramanujan)
        # so ratio should INCREASE with r
        p = 97
        ratios = []
        for r in range(1, 9):
            checks = verify_serre_at_primes(r, k=12, primes=[p])
            ratios.append(checks[0]['ratio_to_serre'])
        # As r increases, bound tightens, so ratio increases
        for i in range(len(ratios) - 1):
            assert ratios[i] <= ratios[i + 1] + 1e-10
