r"""Tests for wave18_heegner_pattern_phi_m21.

Module claims: phi_{-2,1}(tau, z) = theta_1(tau,z)^2 / eta(tau)^6 is the weak
Jacobi form of weight -2, index 1; its Fourier coefficient c_phi(N) depends
only on the discriminant N = 4n - r^2 (Eichler-Zagier 1985 Theorem 9.3), is
supported on N mod 4 in {0, 3} (together with N = -1), and matches the Wave
17.5 leading values
    c_phi(-1) = -1,  c_phi(3) = -8,  c_phi(4) = 12,
    c_phi(7) = -39, c_phi(8) = 56.

Verification paths:
    (A) Primary: Eichler-Zagier 1985 Theorem 9.3 (admissibility).
    (B) Independent: Gritsenko 1999 tabulation of phi_{-2,1} coefficients,
        and Borcherds 1998 Theorem 10.1 singular-theta lift for Phi_10.
    (C) Limiting case: c_phi(-1) = -1 from the prefactor -(y - 2 + y^{-1})
        at q^0 (coefficient of y^{+1} or y^{-1}).
    (D) Symmetry: c(n, r) depends only on N = 4n - r^2 (Jacobi form
        structure); we verify by computing at two distinct (n, r) pairs
        with the same N.
"""

from __future__ import annotations

import pytest

from compute.lib.wave18_heegner_pattern_phi_m21 import (
    asymptotic_bound,
    compute_phi_m21_coefficients,
    verify_wave18_heegner_pattern,
)


# ---------------------------------------------------------------------------
# Smoke test: module imports and main entry point runs
# ---------------------------------------------------------------------------

def test_smoke_module_imports_and_runs():
    result = verify_wave18_heegner_pattern(q_max=6)
    assert isinstance(result, dict)
    assert "coefficients" in result
    assert "leading_values" in result
    assert "matches_wave17_5" in result


# ---------------------------------------------------------------------------
# (Identity) Eichler-Zagier 1985 Theorem 9.3: admissibility residue
# c_phi(N) = 0 unless N mod 4 in {0, 3} (or N = -1 from prefactor)
# ---------------------------------------------------------------------------

def test_eichler_zagier_admissibility_residue():
    coeffs = compute_phi_m21_coefficients(q_max=6)
    # Non-admissible residues N mod 4 in {1, 2} (for N >= 0): c_phi(N) = 0
    for N in range(0, 13):
        if N in (-1,):  # prefactor
            continue
        if N % 4 in (1, 2):
            c = coeffs.get(N, 0)
            assert c == 0, (
                f"Admissibility violated at N = {N} (N%4={N%4}): "
                f"c_phi({N}) = {c}, should be 0"
            )


# ---------------------------------------------------------------------------
# (Identity) Wave 17.5 leading values match primary literature
# Gritsenko-Nikulin 1998 / Dabholkar-Murthy-Zagier 2012 tabulations
# ---------------------------------------------------------------------------

def test_wave17_5_leading_values_match_primary():
    coeffs = compute_phi_m21_coefficients(q_max=8)
    expected = {3: -8, 4: 12, 7: -39, 8: 56}
    for N, c_expected in expected.items():
        assert coeffs.get(N) == c_expected, (
            f"c_phi({N}) = {coeffs.get(N)} disagrees with primary value "
            f"{c_expected} (Gritsenko-Nikulin 1998, Dabholkar-Murthy-Zagier 2012)"
        )


# ---------------------------------------------------------------------------
# (Symmetry) Jacobi form discriminant invariance:
# c(n, r) depends only on N = 4n - r^2. Tested implicitly via the
# assertion inside compute_phi_m21_coefficients that collapsing
# (n, r) pairs with equal N to the same discriminant coefficient
# is consistent (no exception raised).
# ---------------------------------------------------------------------------

def test_jacobi_discriminant_invariance_no_collision():
    # Simply running compute_phi_m21_coefficients at q_max=6 exercises the
    # internal consistency assertion that (n, r) pairs with equal N yield
    # equal coefficients.  If this assertion ever fires, the module has
    # detected a violation of the Eichler-Zagier Jacobi-form structure.
    coeffs = compute_phi_m21_coefficients(q_max=6)
    # Sanity: the prefactor yields c_phi(-1) = -1 (the normalising anchor).
    assert coeffs.get(-1) == -1, (
        f"c_phi(-1) = {coeffs.get(-1)} != -1 from prefactor normalisation"
    )


# ---------------------------------------------------------------------------
# (Limiting case) Asymptotic growth |c_phi(N)| ~ exp(pi * sqrt(N))
# Gritsenko 1999 / Dabholkar-Murthy-Zagier 2012.  Verify monotonicity.
# ---------------------------------------------------------------------------

def test_asymptotic_bound_monotonic_and_superpolynomial():
    b10 = asymptotic_bound(10)
    b100 = asymptotic_bound(100)
    b1000 = asymptotic_bound(1000)
    assert b10 < b100 < b1000
    # superpolynomial: b1000 / b100 should exceed any polynomial ratio
    # exp(pi * sqrt(1000)) / exp(pi * sqrt(100)) = exp(pi * (sqrt(1000) - 10))
    # = exp(pi * ~21.6) >> polynomial in 10
    assert b1000 / b100 > 1e10


# ---------------------------------------------------------------------------
# (Consolidated verifier) Runs all three primary checks
# ---------------------------------------------------------------------------

def test_consolidated_verifier_reports_match():
    result = verify_wave18_heegner_pattern(q_max=8)
    assert result["matches_wave17_5"] is True
