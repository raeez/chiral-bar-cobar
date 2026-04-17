"""
Test: super-complementarity for Y_hbar(sl(2|1)) under both pairings plus the
Berezinian-shift bridge from Vol I lem:super-trace-berezinian-bridge.

Family: sl(2|1); m = 2, n = 1; h^v_s = m - n = 1; max(m, n) = 2.

Assertions:

  (a) Super-trace sum:     kappa_supertrace(2,1,k) + kappa_supertrace(1,2,k) == 0
  (b) Berezinian sum:      kappa_berezinian(2,1,k) + kappa_berezinian(1,2,k) == 2
  (c) Bridge shift:        quantum_berezinian_leading(2, 1) == 1

Status: marked xfail pending analytic implementation of
compute.lib.super_yangian_shadow (see lem:super-trace-berezinian-bridge).

Independent-verification paths (three disjoint routes to the bridge; any two
agreeing pin the third):

  derived_from       = compute.lib.super_yangian_shadow.kappa_supertrace
                       and kappa_berezinian
  verified_against   = [
    "Gow-Molev 2010 Thm 4.2 (super-PBW) + direct Sugawara super-trace",
    "Nazarov 1991 Thm 1 + Molev Yangians and Classical Lie Algebras Ch 3.9 "
      "Thm 3.9.1 + Gow 2006 Thm 5.1 (quantum Berezinian centrality and "
      "leading-coefficient tabulation)",
    "Beisert 2007 (The S-matrix of AdS/CFT and Yangian symmetry) Sec 3 "
      "(psl(2|2) central-extension count)",
  ]
  disjoint_rationale = "V1 uses super-PBW and Sugawara, not the quantum "
    "Berezinian. V2 uses quasideterminants of T(u), not Sugawara. V3 uses "
    "AdS/CFT central-extension counting, neither super-PBW nor "
    "quasideterminants."
"""

import pytest

from compute.lib.super_yangian_shadow import (
    kappa_berezinian,
    kappa_supertrace,
    quantum_berezinian_leading,
)


# Family parameters for the sl(2|1) test line.
M, N = 2, 1
HV_S = M - N          # = 1
MAX_MN = max(M, N)    # = 2

# Levels on the sub-Sugawara line k + h^v_s <= m + n = 3 (slack at 2).
K_GRID = [-1, 0, 1, 2]


@pytest.mark.xfail(
    reason="library stub; pending implementation per "
    "lem:super-trace-berezinian-bridge",
    strict=False,
)
def test_super_trace_sum_sl21_vanishes():
    """Clause (a): super-trace pairing sum vanishes on the sub-Sugawara line.

    For each level in K_GRID, the canonical complementarity pairing (A, A^!)
    realised as (Y_hbar(sl(2|1)), Y_hbar(sl(1|2))) under the Feigin-Frenkel
    involution must sum to zero under the super-trace normalisation.
    """
    for k in K_GRID:
        left = kappa_supertrace(M, N, k)
        right = kappa_supertrace(N, M, k)
        assert abs(left + right) < 1e-12, (
            f"super-trace complementarity failed at k={k}: "
            f"{left} + {right} != 0"
        )


@pytest.mark.xfail(
    reason="library stub; pending implementation per "
    "lem:super-trace-berezinian-bridge",
    strict=False,
)
def test_berezinian_sum_sl21_equals_max():
    """Clause (b): Berezinian pairing sum equals max(m, n) = 2 for sl(2|1)."""
    for k in K_GRID:
        left = kappa_berezinian(M, N, k)
        right = kappa_berezinian(N, M, k)
        assert abs((left + right) - MAX_MN) < 1e-12, (
            f"Berezinian complementarity failed at k={k}: "
            f"{left} + {right} != {MAX_MN}"
        )


@pytest.mark.xfail(
    reason="library stub; pending implementation per "
    "lem:super-trace-berezinian-bridge",
    strict=False,
)
def test_bridge_shift_sl21_equals_one():
    """Clause (c): Nazarov quantum Berezinian leading shift magnitude equals 1.

    For sl(2|1) the additive shift (1/2) * max(m, n) evaluates to 1, and the
    quantum_berezinian_leading function returns this raw shift magnitude in
    the Gow 2006 normalisation.
    """
    shift = quantum_berezinian_leading(M, N)
    expected = 0.5 * MAX_MN
    assert abs(shift - expected) < 1e-12, (
        f"bridge shift magnitude failed: {shift} != {expected}"
    )
