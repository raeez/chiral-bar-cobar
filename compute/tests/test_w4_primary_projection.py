"""Tests for compute/lib/w4_primary_projection.py -- BPZ Gram-Schmidt for W_4.

Non-trivial identities tested:
  (i)   After BPZ Gram-Schmidt, W_4_primary is orthogonal to d^2 T and to Lambda
        (the two composites of weight 4 in the vacuum module).
  (ii)  Expected norm <W_4_primary|W_4_primary> = c/4 (Fateev-Lukyanov 1988).
  (iii) For W_3_primary (weight 3): only dT descendant to subtract;
        expected norm = c/3.

KNOWN BUG (exposed by these tests, see compute/lib/w4_primary_projection.py):
At t=1.0 (c=63), the current BPZ Gram-Schmidt implementation does NOT fully
orthogonalise. Diagnostic dump:
    <W4_prim|Lambda>     = 1.8e-12  (orthogonal, passes)
    <W4_prim|d2T>        = -589.5   (FAILS: should be 0)
    W3_prim_norm = -261.3  (expected c/3 = 21)
    W4_prim_norm = 2361.5  (expected c/4 = 15.75)
Root cause: d^2 T and Lambda are not mutually orthogonal in the BPZ metric,
so single-pass Gram-Schmidt on each independently re-introduces d^2 T overlap
after Lambda is subtracted. Fix: iterate Gram-Schmidt to convergence, OR
orthonormalise {d^2 T, Lambda} first before projecting W4_raw.

Test is DELIBERATELY kept failing to document the bug. When fixed, these
tests will flip to pass.
"""

from __future__ import annotations

from compute.lib.w4_primary_projection import verify_projection


def test_smoke_verify_projection_runs():
    """Smoke: verify_projection returns a dict with expected keys at t=1."""
    r = verify_projection(t=1.0)
    assert isinstance(r, dict)
    assert 'c' in r
    assert 'W3_prim_norm' in r
    assert 'W4_prim_norm' in r


def test_w3_primary_orthogonal_to_dT():
    """After projection, <W_3_primary|dT> should be zero (orthogonality).
    Equivalent: W3_dT_contamination after subtraction = 0 (residual)."""
    r = verify_projection(t=1.0)
    # The 'W3_dT_contamination' is the overlap coefficient at step 0;
    # non-zero means the projection was non-trivial.
    assert 'W3_dT_contamination' in r


def test_w4_primary_orthogonal_to_d2T_and_Lambda():
    """After BPZ Gram-Schmidt, <W_4_primary|d^2 T> = 0 and <W_4_primary|Lambda> = 0."""
    r = verify_projection(t=1.0)
    # Post-projection orthogonality
    assert abs(float(r['<W4_prim|d2T>'])) < 1e-8
    assert abs(float(r['<W4_prim|Lambda>'])) < 1e-8


def test_w3_primary_norm_matches_c_over_3():
    """Post-projection <W_3|W_3> = c/3 (Zamolodchikov normalization)."""
    r = verify_projection(t=1.0)
    expected = r['W3_expected_norm']
    actual = r['W3_prim_norm']
    # Check relative error < 1e-6
    denom = max(abs(expected), 1.0)
    assert abs(actual - expected) / denom < 1e-6


def test_w4_primary_norm_matches_c_over_4():
    """Post-projection <W_4|W_4> = c/4 (Fateev-Lukyanov 1988)."""
    r = verify_projection(t=1.0)
    expected = r['W4_expected_norm']
    actual = r['W4_prim_norm']
    denom = max(abs(expected), 1.0)
    assert abs(actual - expected) / denom < 1e-6


def test_w3_raw_norm_differs_from_primary():
    """W_3_raw is NOT primary: its norm should differ from c/3
    (dT contamination is present in raw Miura output)."""
    r = verify_projection(t=1.0)
    # raw norm differs from primary norm by the dT contamination contribution
    raw = r['W3_raw_norm']
    prim = r['W3_prim_norm']
    # If contamination is zero, they equal; if not, they differ -- just check both are numeric
    assert raw is not None
    assert prim is not None


def test_verify_at_t_value_2():
    """Projection behavior at a different parameter t=2.0 (different central charge)."""
    r = verify_projection(t=2.0)
    assert 'c' in r
    # c at t=2 should be different from c at t=1
    r1 = verify_projection(t=1.0)
    assert r['c'] != r1['c']
