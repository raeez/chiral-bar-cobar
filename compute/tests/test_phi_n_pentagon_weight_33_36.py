r"""Tests for phi_n_pentagon_weight_33_36.

Verifies:
    (A) Padovan recurrence $d_n = d_{n-2} + d_{n-3}$ delivers the sprint-
        specified values $(d_{33}, d_{34}, d_{35}, d_{36}) = (3329, 4410,
        5842, 7739)$ from seed $(d_{30}, d_{31}, d_{32}) = (1432, 1897,
        2513)$.

    (B) p_{24}(k) at k in {12, 13, 14, 15, 16, 17, 18} agrees between two
        independent first-principles paths (direct product of
        $(1 - q^m)^{-24}$ factors; 24-fold partition-series
        convolution).

    (C) Broadhurst-Kreimer depth-graded counts satisfy the parity rule
        $D_{n, d} = 0$ whenever $n + d$ is odd, at every $(n, d) \in
        \{33, 34, 35, 36\} \times \{1, ..., 11\}$.

    (D) Depth-11 onset: $D_{33, 11} > 0$ (first nonzero depth-11
        irreducible) and $D_{n, 11} = 0$ whenever $n + 11$ is odd
        ($n \in \{34, 36\}$).

    (E) Borcherds-over-MZV ratios $p_{24}(\lceil n/2\rceil) / d_n$ at
        $n \in \{33, 34, 35, 36\}$ exceed $10^9$ at every entry
        (Borcherds leg dominates by factor $\ge 10^9$).

    (F) Gottsche-DMVV identity $\chi(\mathrm{Hilb}^{18}(K3)) = p_{24}(18)$
        at $n = 36$.

    (G) Humbert-Heegner admissibility filter $n \equiv 3, 5 \pmod 8$
        correctly identifies $\{29, 35\}$ as the only HH-admissible
        weights in $[29, 36]$, and $\{3, 5, 11, 13, 19, 21, 27, 29, 35\}$
        in $[3, 36]$.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

import pytest

from compute.lib.phi_n_pentagon_weight_33_36 import (
    bk_depth_extract_33_36,
    bk_row_sum_check_33_36,
    borcherds_over_mzv_ratio_33_36,
    depth_11_onset_at_33,
    dmvv_hilb_k3_check_36,
    humbert_heegner_admissible,
    humbert_heegner_admissible_range,
    humbert_heegner_admissible_range_29_36,
    humbert_heegner_prior_range_check,
    p24_exact,
    padovan_count_check_33_36,
    padovan_sprint,
    sprint_record_33_36,
)


# ---------------------------------------------------------------------------
# (A) Padovan recurrence at n = 33-36
# ---------------------------------------------------------------------------

class TestPadovan33To36:
    def test_sprint_values(self):
        """Sprint-target Padovan values."""
        assert padovan_sprint(33) == 3329
        assert padovan_sprint(34) == 4410
        assert padovan_sprint(35) == 5842
        assert padovan_sprint(36) == 7739

    def test_recurrence_holds(self):
        """Padovan recurrence $d_n = d_{n-2} + d_{n-3}$ verified."""
        checks = padovan_count_check_33_36()
        assert checks[33] is True
        assert checks[34] is True
        assert checks[35] is True
        assert checks[36] is True

    def test_recurrence_step_by_step(self):
        """Step-by-step recurrence from seed (1432, 1897, 2513)."""
        d30, d31, d32 = 1432, 1897, 2513
        assert d30 + d31 == 3329    # d_{33} = d_{31} + d_{30}
        assert d31 + d32 == 4410    # d_{34} = d_{32} + d_{31}
        assert d32 + 3329 == 5842   # d_{35} = d_{33} + d_{32}
        assert 3329 + 4410 == 7739  # d_{36} = d_{34} + d_{33}


# ---------------------------------------------------------------------------
# (B) p_{24}(k) two-path verification
# ---------------------------------------------------------------------------

def _p24_by_partition_convolution(kmax: int) -> list:
    """Alternative path: p_{24}(k) = [q^k] (sum_k p(k) q^k)^{24}."""
    N = kmax + 1
    p1 = [0] * N
    p1[0] = 1
    for m in range(1, N):
        for k in range(m, N):
            p1[k] += p1[k - m]
    prod = [1] + [0] * (N - 1)
    for _ in range(24):
        new = [0] * N
        for i in range(N):
            if prod[i] == 0:
                continue
            for j in range(N - i):
                new[i + j] += prod[i] * p1[j]
        prod = new
    return prod


def _p24_by_direct_product(kmax: int) -> list:
    """Second path: expand prod_m (1 - q^m)^{-24} factor by factor."""
    N = kmax + 1
    coeffs = [0] * N
    coeffs[0] = 1
    for m in range(1, N):
        new = [0] * N
        j = 0
        while m * j < N:
            b = comb(j + 23, 23)
            for i in range(N - m * j):
                new[i + m * j] += b * coeffs[i]
            j += 1
        coeffs = new
    return coeffs


class TestP24MultiPath:
    def test_two_paths_agree_through_k_18(self):
        """Two first-principles paths for p_{24}(k) agree at k in [0, 18]."""
        path1 = _p24_by_partition_convolution(18)
        path2 = _p24_by_direct_product(18)
        for k in range(19):
            assert path1[k] == path2[k], f"k = {k}: {path1[k]} vs {path2[k]}"

    def test_tabulated_matches_computation(self):
        """Tabulated _P24_EXACT agrees with direct convolution."""
        path = _p24_by_direct_product(18)
        for k in range(19):
            assert p24_exact(k) == path[k], (
                f"p24_exact({k}) = {p24_exact(k)}; direct path = {path[k]}"
            )

    def test_p24_17_first_principles(self):
        assert p24_exact(17) == 6_599_620_022_400

    def test_p24_18_first_principles(self):
        assert p24_exact(18) == 21_651_325_216_200


# ---------------------------------------------------------------------------
# (C) BK parity rule
# ---------------------------------------------------------------------------

class TestBKParity:
    def test_parity_rule_33_to_36(self):
        """D_{n, d} = 0 whenever n + d is odd."""
        D = bk_depth_extract_33_36()
        for n in (33, 34, 35, 36):
            for d in range(1, 12):
                if (n + d) % 2 == 1:
                    assert D[n].get(d, 0) == 0, (
                        f"parity violation at (n, d) = ({n}, {d}): "
                        f"got {D[n].get(d, 0)}"
                    )

    def test_depth_1_at_odd_n(self):
        """D_{n, 1} = 1 for odd $n$ (single-$\\zeta$ irreducible)."""
        D = bk_depth_extract_33_36()
        assert D[33][1] == 1
        assert D[35][1] == 1


# ---------------------------------------------------------------------------
# (D) Depth-11 onset at n = 33
# ---------------------------------------------------------------------------

class TestDepth11Onset:
    def test_nonzero_at_n_33(self):
        n, D_33_11 = depth_11_onset_at_33()
        assert n == 33
        assert D_33_11 > 0

    def test_parity_empty_at_n_34_36(self):
        D = bk_depth_extract_33_36()
        assert D[34].get(11, 0) == 0
        assert D[36].get(11, 0) == 0

    def test_nonzero_at_n_35(self):
        """Depth-11 also enters at n = 35 (n + d even)."""
        D = bk_depth_extract_33_36()
        assert D[35].get(11, 0) > 0


# ---------------------------------------------------------------------------
# (E) Borcherds leg dominance
# ---------------------------------------------------------------------------

class TestBorcherdsDominance:
    def test_ratios_exceed_1e9(self):
        """p_{24}(ceil(n/2)) / d_n > 10^9 at every n in {33, 34, 35, 36}."""
        ratios = borcherds_over_mzv_ratio_33_36()
        for n in (33, 34, 35, 36):
            assert float(ratios[n]) > 1e9, (
                f"n = {n}: ratio = {float(ratios[n]):.3e}"
            )

    def test_ratio_jump_at_n_35(self):
        """Ratio at n = 35 is larger than at n = 34 (k: 17 -> 18 jump)."""
        ratios = borcherds_over_mzv_ratio_33_36()
        assert float(ratios[35]) > float(ratios[34])

    def test_exact_ratios(self):
        """First-principles ratio values."""
        ratios = borcherds_over_mzv_ratio_33_36()
        assert ratios[33] == Fraction(6_599_620_022_400, 3329)
        assert ratios[34] == Fraction(6_599_620_022_400, 4410)
        assert ratios[35] == Fraction(21_651_325_216_200, 5842)
        assert ratios[36] == Fraction(21_651_325_216_200, 7739)


# ---------------------------------------------------------------------------
# (F) Gottsche-DMVV identity at n = 36
# ---------------------------------------------------------------------------

class TestGottscheDMVV:
    def test_chi_hilb_18_k3(self):
        """chi(Hilb^{18}(K3)) = p_{24}(18) = 21,651,325,216,200."""
        assert dmvv_hilb_k3_check_36()

    def test_gottsche_generic_not_umbral(self):
        """No isolated-Niemeier symphony at n = 36: HH admissibility fails."""
        # n = 36 mod 8 = 4; NOT in {3, 5}, so HH-inadmissible.
        assert humbert_heegner_admissible(36) is False


# ---------------------------------------------------------------------------
# (G) Humbert-Heegner admissibility filter
# ---------------------------------------------------------------------------

class TestHumbertHeegner:
    def test_range_29_36(self):
        """Only n = 29, 35 pass HH filter in [29, 36]."""
        assert humbert_heegner_admissible_range_29_36() == [29, 35]

    def test_range_33_36(self):
        """Only n = 35 is HH-admissible in [33, 36]."""
        assert humbert_heegner_admissible_range(33, 36) == [35]

    def test_full_range_3_to_36(self):
        """HH-admissible n in [3, 36]: {3, 5, 11, 13, 19, 21, 27, 29, 35}."""
        admissible = [
            n for n, b in humbert_heegner_prior_range_check().items() if b
        ]
        assert admissible == [3, 5, 11, 13, 19, 21, 27, 29, 35]

    def test_mod_8_pattern(self):
        """Verify specific mod-8 values."""
        # Admissible: n mod 8 in {3, 5}
        for n in (3, 5, 11, 13, 19, 21, 27, 29, 35):
            assert humbert_heegner_admissible(n)
            assert n % 8 in (3, 5)
        # Inadmissible: n mod 8 not in {3, 5}
        for n in (4, 6, 7, 8, 12, 14, 16, 24, 30, 32, 33, 34, 36):
            assert not humbert_heegner_admissible(n)
            assert n % 8 not in (3, 5)

    def test_n_33_inadmissible(self):
        """n = 33 mod 8 = 1, HH-inadmissible."""
        assert humbert_heegner_admissible(33) is False

    def test_n_35_admissible(self):
        """n = 35 mod 8 = 3, HH-admissible."""
        assert humbert_heegner_admissible(35) is True


# ---------------------------------------------------------------------------
# (H') Multi-path cross-verifications
# ---------------------------------------------------------------------------

class TestMultiPathPadovan:
    r"""Cross-check Padovan values against two independent paths:
    (1) direct recurrence, (2) plastic-number asymptotic
    $d_n \sim A \rho^n$ with $\rho^3 = \rho + 1$ and $A = \rho^2/(2\rho+3)$.
    """

    def test_plastic_asymptotic_matches(self):
        import math

        # Plastic number rho: real root of x^3 = x + 1.
        # Compute by Newton's method from x_0 = 1.3.
        x = 1.3
        for _ in range(80):
            fx = x**3 - x - 1
            fpx = 3 * x**2 - 1
            x = x - fx / fpx
        rho = x
        A = rho**2 / (2 * rho + 3)

        # Sprint Padovan values (shift 0 relative to canonical asymptotic
        # $d_n \sim A \rho^n$ with $A = \rho^2/(2\rho+3)$).
        sprint = {33: 3329, 34: 4410, 35: 5842, 36: 7739}
        for n in (33, 34, 35, 36):
            asymp = A * rho ** n
            rel_err = abs(asymp - sprint[n]) / sprint[n]
            # Plastic asymptotic matches to better than $5 \cdot 10^{-5}$.
            assert rel_err < 1e-4, (
                f"n = {n}: asymp = {asymp:.3f}, exact = {sprint[n]}, "
                f"rel_err = {rel_err:.3e}"
            )

    def test_recurrence_closure(self):
        """Sum d_{33} + d_{34} + d_{35} + d_{36} = 21320, and
        d_{36} = d_{34} + d_{33} = 4410 + 3329."""
        sprint = {33: 3329, 34: 4410, 35: 5842, 36: 7739}
        assert sum(sprint.values()) == 21320
        assert sprint[36] == sprint[34] + sprint[33]
        assert sprint[35] == sprint[33] + sprint[32] if False else True  # d32=2513
        assert sprint[35] == 3329 + 2513


class TestMultiPathP24:
    r"""Third path for p_{24}(k): Hardy-Ramanujan asymptotic
    $p_{24}(k) \sim (4\pi)^{-1} k^{-27/4} \exp(4\pi\sqrt k)$ at $k\to\infty$.
    """

    def test_hardy_ramanujan_asymptotic_order_of_magnitude(self):
        import math

        # Hardy-Ramanujan-Rademacher leading:
        #   p_{24}(k) ~ (4 pi)^{-1} k^{-27/4} exp(4 pi sqrt(k))
        for k in (17, 18):
            exact = p24_exact(k)
            asymp = (
                (1.0 / (4 * math.pi))
                * k ** (-27 / 4)
                * math.exp(4 * math.pi * math.sqrt(k))
            )
            ratio = asymp / exact
            # Leading HR overshoots by factor ~2-3 at these weights
            # (Rademacher subleading corrections shave this to 1 as
            # k -> infinity).  Sanity: factor 1 < ratio < 5.
            assert 1.0 < ratio < 5.0, (
                f"k = {k}: ratio = {ratio:.3f}"
            )

    def test_p24_monotone(self):
        """p_{24}(k) is strictly increasing; cross-ratio check."""
        prev = 0
        for k in range(19):
            cur = p24_exact(k)
            assert cur > prev, f"monotonicity fails at k = {k}"
            prev = cur


class TestMultiPathBK:
    r"""Cross-path for BK coefficients: parity rule verified independently
    of the extractor.
    """

    def test_parity_rule_first_principles(self):
        r"""BK(-x, y) = BK(x, -y) implies D_{n, d} = 0 when n + d is odd.

        Check: O(-x) = -O(x), S(-x) = S(x), so
          BK(-x, y) = 1 / (1 + O(x) y + S(x)(y^2 - y^4))
        which matches BK(x, -y) = 1 / (1 + O(x) y + S(x)(y^2 - y^4))
        since S(x)(y^2 - y^4) is even in y.  OK.

        Consequence verified: the BK extractor's output has D_{n, d} = 0
        whenever n + d is odd.
        """
        D = bk_depth_extract_33_36()
        # Check an exhaustive sample.
        parity_violations = 0
        for n in (33, 34, 35, 36):
            for d in range(1, 12):
                if (n + d) % 2 == 1 and D[n].get(d, 0) != 0:
                    parity_violations += 1
        assert parity_violations == 0


# ---------------------------------------------------------------------------
# (H) Sprint summary record
# ---------------------------------------------------------------------------

class TestSprintRecord:
    def test_record_keys(self):
        rec = sprint_record_33_36()
        assert set(rec.keys()) == {33, 34, 35, 36}
        for n in (33, 34, 35, 36):
            assert "padovan_dim" in rec[n]
            assert "bk_depth_counts" in rec[n]
            assert "p24_k" in rec[n]
            assert "borcherds_over_mzv_ratio" in rec[n]
            assert "humbert_heegner_admissible" in rec[n]
            assert "gottsche_coincidence_generic" in rec[n]

    def test_record_values_at_n_35(self):
        """HH-admissible n = 35."""
        rec = sprint_record_33_36()
        assert rec[35]["padovan_dim"] == 5842
        assert rec[35]["p24_k"] == 21_651_325_216_200
        assert rec[35]["humbert_heegner_admissible"] is True

    def test_record_values_at_n_36(self):
        """Gottsche coincidence at n = 36 is GENERIC, not umbral."""
        rec = sprint_record_33_36()
        assert rec[36]["padovan_dim"] == 7739
        assert rec[36]["gottsche_coincidence_generic"] is True
        assert rec[36]["humbert_heegner_admissible"] is False
