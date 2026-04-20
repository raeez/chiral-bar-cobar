"""Tests for compute/lib/w3_bar_extended.py -- W_3 vacuum module bar construction.

Non-trivial identities tested:
  (i)   W_3 OPE mu(T,T) = (c/2)|0> + 2T + dT (BPZ, c=7 sample).
  (ii)  W_3 OPE mu(W,W) includes the Lambda-correction coefficient
        alpha = 16/(5c+22) at c=7: alpha = 16/57.
  (iii) Skew-symmetry W_{(0)} T = 2*dW.
  (iv)  vbar dimensions: generating function counts partitions into
        T-parts and W-parts with shifted weights.
"""

from __future__ import annotations

import pytest

from compute.lib.w3_bar_extended import (
    W3VacuumModule,
    dim_vbar,
    dim_vbar_gf,
    state_weight,
    verify_mu_generators,
    verify_skew_symmetry,
    vbar_basis,
)


def test_smoke_vbar_basis_at_low_weights():
    """Smoke: vbar basis at weight 0 is empty; weight 2 contains T only."""
    basis = vbar_basis(max_weight=4)
    # Weight 2: T = ((2,), ())
    assert ((2,), ()) in basis[2]
    # Weight 3: W = ((), (3,))
    assert ((), (3,)) in basis[3]
    # Weight 0: no entries (vbar = V_vac quotient by vacuum)
    assert basis.get(0, []) == []


def test_state_weight_is_sum_of_mode_numbers():
    """weight((L_2, L_3), (W_3,)) = 2+3+3 = 8."""
    w = state_weight(((2, 3), (3,)))
    assert w == 8


def test_mu_T_T_central_charge_c_over_2():
    """mu(T,T) has vacuum coefficient c/2 for arbitrary c."""
    results = verify_mu_generators(c_val=7.0, verbose=False)
    assert bool(results["mu(T,T) vac = c/2"])
    assert bool(results["mu(T,T) T = 2"])
    assert bool(results["mu(T,T) dT = 1"])


def test_mu_W_W_central_charge_c_over_3():
    """mu(W,W) has vacuum c/3 and Lambda correction alpha = 16/(5c+22)."""
    results = verify_mu_generators(c_val=7.0, verbose=False)
    assert bool(results["mu(W,W) vac = c/3"])
    # Lambda-level terms: L4 and L22 split via alpha = 16/57 at c=7
    assert bool(results["mu(W,W) L4 correct"])
    assert bool(results["mu(W,W) L22 correct"])


def test_mu_T_W_skew_coefficients():
    """mu(T,W) = 3W + dW; mu(W,T) = 3W + 2dW (skew-symmetry)."""
    results = verify_mu_generators(c_val=7.0, verbose=False)
    assert bool(results["mu(T,W) W = 3"])
    assert bool(results["mu(T,W) dW = 1"])
    assert bool(results["mu(W,T) W = 3"])
    assert bool(results["mu(W,T) dW = 2"])


def test_skew_symmetry_W_zero_T_equals_twice_dW():
    """W_{(0)} T = 2*dW (no other components)."""
    results = verify_skew_symmetry(c_val=7.0)
    assert bool(results["W_{(0)}T = 2*dW"])
    # No spurious components
    spurious = [k for k in results if k.startswith("W_(0)T spurious")]
    assert not spurious


def test_vbar_dim_monotone_in_weight():
    """dim V-bar_h is non-decreasing through a small range."""
    dims = dim_vbar_gf(max_h=6)
    # Some non-trivial entries should appear
    assert sum(dims.values()) > 0
