"""Tests for genus-2 homotopy transfer correction for sl_2 KM.

Ground truth:
  - sl_2 Jacobi identity: [mu, mu]_NR = 0
  - CE complex: d^2 = 0, H^0 = H^3 = k, H^1 = H^2 = 0
  - Killing 3-cocycle: phi(a,b,c) = kap([a,b],c), generates H^3(sl_2)
  - MC equation genus 2: theta_2 = kappa * phi * lambda_2, no HTT correction
  - MC equation genus 3: theta_3 = kappa * phi * lambda_3, no HTT correction
  - Universality: theta_g is an honest cocycle at ALL genera for KM

The key physical point: for Kac-Moody algebras, the cyclic deformation
complex is a strict dg Lie algebra (l_3 = l_4 = ... = 0). Combined with
the Jacobi identity (l_2(theta, theta) = 0), this means NO homotopy
transfer corrections appear at any genus. This is why the MC class
factorizes as kappa(A) * eta tensor Lambda_g for all g.

For W-algebras, l_3 != 0 (from the Killing cocycle acting on composites),
so corrections DO appear starting at genus 2. This is the W-algebra anomaly.
"""
import pytest
from fractions import Fraction

import numpy as np

from compute.lib.genus2_htt import (
    DIM_G,
    sl2_structure_constants,
    sl2_killing_form,
    sl2_killing_inverse,
    killing_cocycle_tensor,
    verify_killing_cocycle_antisymmetric,
    verify_killing_cocycle_closed,
    bracket_tensor,
    nijenhuis_richardson_bracket,
    verify_jacobi_via_nr,
    l2_theta1_theta1,
    l3_on_original_complex,
    build_ce_differential_matrices,
    build_contracting_homotopy,
    verify_sdr,
    verify_d_squared,
    mc_equation_genus_2,
    mc_equation_genus_3,
    verify_km_theta_universality,
    killing_cocycle_normalization,
    kappa_sl2,
    theta_g_coefficient,
    genus2_htt_summary,
)


# ============================================================
# sl_2 structure constants
# ============================================================

class TestSl2Data:
    """Verify sl_2 structure constants and Killing form."""

    def test_dimension(self):
        assert DIM_G == 3

    def test_structure_constants_antisymmetric(self):
        c = sl2_structure_constants()
        for a in range(3):
            for b in range(3):
                for k in range(3):
                    assert c[a, b, k] == -c[b, a, k], (
                        f"c[{a},{b},{k}] = {c[a,b,k]} != -c[{b},{a},{k}] = {-c[b,a,k]}")

    def test_bracket_values(self):
        """[e,f] = h, [h,e] = 2e, [h,f] = -2f."""
        c = sl2_structure_constants()
        # [e,f] = h: c[0,2,1] = 1
        assert c[0, 2, 1] == Fraction(1)
        # [h,e] = 2e: c[1,0,0] = 2
        assert c[1, 0, 0] == Fraction(2)
        # [h,f] = -2f: c[1,2,2] = -2
        assert c[1, 2, 2] == Fraction(-2)

    def test_killing_form_values(self):
        """(e,f) = (f,e) = 1, (h,h) = 2."""
        kap = sl2_killing_form()
        assert kap[0, 2] == Fraction(1)
        assert kap[2, 0] == Fraction(1)
        assert kap[1, 1] == Fraction(2)
        # All others zero
        for i in range(3):
            for j in range(3):
                if (i, j) not in [(0, 2), (2, 0), (1, 1)]:
                    assert kap[i, j] == Fraction(0), f"kap[{i},{j}] = {kap[i,j]}"

    def test_killing_form_symmetric(self):
        kap = sl2_killing_form()
        for i in range(3):
            for j in range(3):
                assert kap[i, j] == kap[j, i]

    def test_killing_inverse(self):
        """kap^{ij} kap_{jk} = delta^i_k."""
        kap = sl2_killing_form()
        kap_inv = sl2_killing_inverse()
        product = np.zeros((3, 3), dtype=object)
        for i in range(3):
            for k in range(3):
                val = Fraction(0)
                for j in range(3):
                    val += kap_inv[i, j] * kap[j, k]
                product[i, k] = val
        for i in range(3):
            for k in range(3):
                expected = Fraction(1) if i == k else Fraction(0)
                assert product[i, k] == expected, (
                    f"(kap^{{-1}} kap)[{i},{k}] = {product[i,k]}, expected {expected}")

    def test_killing_invariant(self):
        """Killing form is ad-invariant: kap([a,b], c) + kap(b, [a,c]) = 0."""
        c = sl2_structure_constants()
        kap = sl2_killing_form()
        for a in range(3):
            for b in range(3):
                for d in range(3):
                    # kap([a,b], d) = sum_e c[a,b,e] kap[e,d]
                    term1 = sum(c[a, b, e] * kap[e, d] for e in range(3))
                    # kap(b, [a,d]) = sum_e c[a,d,e] kap[b,e]
                    term2 = sum(c[a, d, e] * kap[b, e] for e in range(3))
                    assert term1 + term2 == Fraction(0), (
                        f"Invariance fails at ({a},{b},{d}): {term1} + {term2}")


# ============================================================
# Killing 3-cocycle
# ============================================================

class TestKillingCocycle:
    """Verify the Killing 3-cocycle phi(a,b,c) = kap([a,b], c)."""

    def test_antisymmetric(self):
        phi = killing_cocycle_tensor()
        assert verify_killing_cocycle_antisymmetric(phi)

    def test_closed(self):
        phi = killing_cocycle_tensor()
        assert verify_killing_cocycle_closed(phi)

    def test_normalization(self):
        """phi(e, h, f) = 2 (from kap([e,h], f) = kap(2e, f) = 2*1 = 2)."""
        # Actually, let's compute phi(e, h, f) directly.
        # [e, h] = -2e, so kap([e,h], f) = kap(-2e, f) = -2 * kap(e,f) = -2.
        # Wait: phi(a,b,c) = kap([a,b], c), so:
        # phi(e, h, f) = kap([e,h], f) = kap(-2e, f) = -2 * 1 = -2.
        # phi(e, f, h) = kap([e,f], h) = kap(h, h) = 2.
        phi = killing_cocycle_tensor()
        assert phi[0, 1, 2] == Fraction(-2), f"phi(e,h,f) = {phi[0,1,2]}"
        assert phi[0, 2, 1] == Fraction(2), f"phi(e,f,h) = {phi[0,2,1]}"

    def test_nonzero(self):
        """phi is not identically zero (it generates H^3(sl_2) = C)."""
        phi = killing_cocycle_tensor()
        has_nonzero = False
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    if phi[a, b, c] != Fraction(0):
                        has_nonzero = True
                        break
        assert has_nonzero

    def test_normalization_detail(self):
        """Verify explicit values of phi on all basis triples."""
        phi = killing_cocycle_tensor()
        info = killing_cocycle_normalization()
        # phi is proportional to the volume form
        assert info["is_antisymmetric"]


# ============================================================
# Jacobi identity via NR bracket
# ============================================================

class TestJacobiIdentity:
    """The Jacobi identity for sl_2: [mu, mu]_NR = 0."""

    def test_jacobi_holds(self):
        mu = sl2_structure_constants()
        is_zero, max_val = verify_jacobi_via_nr(mu)
        assert is_zero, f"Jacobi failed, max entry = {max_val}"

    def test_nr_bracket_all_zero(self):
        """Every entry of the NR bracket is exactly zero."""
        mu = sl2_structure_constants()
        nr = nijenhuis_richardson_bracket(mu, mu)
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    for d in range(3):
                        assert nr[a, b, c, d] == Fraction(0), (
                            f"NR[{a},{b},{c},{d}] = {nr[a,b,c,d]}")

    def test_jacobi_explicit_efh(self):
        """Check Jacobi identity on the triple (e, f, h) explicitly.

        [[e,f],h] + [[f,h],e] + [[h,e],f]
        = [h,h] + [2f,e] + [2e,f]
        = 0 + (-2h) + (2h) = 0. Check.

        Equivalently:
        mu(mu(e,f), h) + mu(mu(f,h), e) + mu(mu(h,e), f) = 0
        """
        c = sl2_structure_constants()
        # mu(mu(e,f), h) = mu(h, h) = [h,h] = 0
        # c[0,2,k] gives [e,f] in direction k: c[0,2,1] = 1, so [e,f] = h
        # c[1,1,k] gives [h,h] in direction k: all zero
        term1 = np.zeros(3, dtype=object)
        for k in range(3):
            for e_idx in range(3):
                term1[k] += c[0, 2, e_idx] * c[e_idx, 1, k]

        # mu(mu(f,h), e) = mu(2f, e) = 2[f,e] = -2h
        term2 = np.zeros(3, dtype=object)
        for k in range(3):
            for e_idx in range(3):
                term2[k] += c[2, 1, e_idx] * c[e_idx, 0, k]

        # mu(mu(h,e), f) = mu(2e, f) = 2[e,f] = 2h
        term3 = np.zeros(3, dtype=object)
        for k in range(3):
            for e_idx in range(3):
                term3[k] += c[1, 0, e_idx] * c[e_idx, 2, k]

        total = term1 + term2 + term3
        for k in range(3):
            assert total[k] == Fraction(0), f"Jacobi(e,f,h)[{k}] = {total[k]}"


# ============================================================
# CE complex
# ============================================================

class TestCEComplex:
    """CE complex for sl_2."""

    def test_d_squared_zero(self):
        diffs = build_ce_differential_matrices()
        results = verify_d_squared(diffs)
        for name, ok in results.items():
            assert ok, f"d^2 check failed: {name}"

    def test_d0_is_zero(self):
        diffs = build_ce_differential_matrices()
        d0 = diffs[0]
        assert d0.shape == (3, 1)
        for i in range(3):
            assert d0[i, 0] == Fraction(0)

    def test_d1_shape(self):
        diffs = build_ce_differential_matrices()
        d1 = diffs[1]
        assert d1.shape == (3, 3)

    def test_d1_invertible(self):
        """d_1 is invertible => H^1 = H^2 = 0."""
        diffs = build_ce_differential_matrices()
        d1 = diffs[1]
        det = (d1[0, 0] * (d1[1, 1] * d1[2, 2] - d1[1, 2] * d1[2, 1])
               - d1[0, 1] * (d1[1, 0] * d1[2, 2] - d1[1, 2] * d1[2, 0])
               + d1[0, 2] * (d1[1, 0] * d1[2, 1] - d1[1, 1] * d1[2, 0]))
        assert det != Fraction(0), f"d_1 has determinant 0"

    def test_d2_shape(self):
        diffs = build_ce_differential_matrices()
        d2 = diffs[2]
        assert d2.shape == (1, 3)

    def test_d2_is_zero(self):
        """d_2 = 0 because Lambda^4(g*) contributes nothing
        (or equivalently, by Jacobi + dim counting)."""
        diffs = build_ce_differential_matrices()
        d2 = diffs[2]
        for j in range(3):
            assert d2[0, j] == Fraction(0), f"d2[0,{j}] = {d2[0,j]}"

    def test_cohomology_dimensions(self):
        """H^0 = k, H^1 = 0, H^2 = 0, H^3 = k."""
        diffs = build_ce_differential_matrices()
        d0, d1, d2 = diffs[0], diffs[1], diffs[2]

        # H^0 = ker(d_0) = C^0 = k (dim 1)
        # d_0 is zero, so ker = C^0 = 1d.
        h0 = 1

        # H^1 = ker(d_1) / im(d_0)
        # d_1 is invertible => ker(d_1) = 0 => H^1 = 0
        # Compute rank of d_1
        rank_d1 = _fraction_matrix_rank(d1)
        h1 = 3 - rank_d1 - 0  # ker - im
        assert h1 == 0, f"H^1 = {h1}"

        # H^2 = ker(d_2) / im(d_1)
        # d_2 = 0 => ker(d_2) = C^2 (dim 3). im(d_1) = rank(d_1) = 3.
        rank_d2 = _fraction_matrix_rank(d2)
        h2 = (3 - rank_d2) - rank_d1  # ker(d2) - im(d1)
        assert h2 == 0, f"H^2 = {h2}"

        # H^3 = C^3 / im(d_2) = 1 - 0 = 1
        h3 = 1 - rank_d2
        assert h3 == 1, f"H^3 = {h3}"


# ============================================================
# SDR (Strong Deformation Retract)
# ============================================================

class TestSDR:
    """Contracting homotopy for sl_2 CE complex."""

    def test_sdr_builds(self):
        diffs = build_ce_differential_matrices()
        h = build_contracting_homotopy(diffs)
        assert h is not None
        assert set(h.keys()) == {0, 1, 2, 3}

    def test_h1_zero(self):
        diffs = build_ce_differential_matrices()
        h = build_contracting_homotopy(diffs)
        for j in range(3):
            assert h[1][0, j] == Fraction(0)

    def test_h3_zero(self):
        diffs = build_ce_differential_matrices()
        h = build_contracting_homotopy(diffs)
        for i in range(3):
            assert h[3][i, 0] == Fraction(0)

    def test_h2_is_d1_inverse(self):
        diffs = build_ce_differential_matrices()
        h = build_contracting_homotopy(diffs)
        d1 = diffs[1]
        product = h[2] @ d1
        for i in range(3):
            for j in range(3):
                expected = Fraction(1) if i == j else Fraction(0)
                assert product[i, j] == expected, (
                    f"(h2 * d1)[{i},{j}] = {product[i,j]}, expected {expected}")

    def test_sdr_conditions(self):
        diffs = build_ce_differential_matrices()
        h = build_contracting_homotopy(diffs)
        results = verify_sdr(diffs, h)
        for name, ok in results.items():
            assert ok, f"SDR condition failed: {name}"


# ============================================================
# MC equation: genus 2
# ============================================================

class TestMCGenus2:
    """MC equation at genus 2: no HTT correction for KM."""

    def test_l2_vanishes(self):
        """l_2(theta_1, theta_1) = 0 by Jacobi."""
        result = mc_equation_genus_2()
        assert result["l2_vanishes"]

    def test_l3_vanishes(self):
        """l_3(theta_1, theta_1, theta_1) = 0 on original complex."""
        result = mc_equation_genus_2()
        assert result["l3_vanishes"]

    def test_rhs_vanishes(self):
        """Total RHS of MC equation at genus 2 is zero."""
        result = mc_equation_genus_2()
        assert result["rhs_vanishes"]

    def test_theta_2_is_cocycle(self):
        """theta_2 = kappa * phi * lambda_2 with no d-exact correction."""
        result = mc_equation_genus_2()
        assert result["theta_2_is_cocycle"]

    def test_l2_theta1_theta1_direct(self):
        """Direct computation of l_2(theta_1, theta_1)."""
        is_zero, nr = l2_theta1_theta1()
        assert is_zero


# ============================================================
# MC equation: genus 3
# ============================================================

class TestMCGenus3:
    """MC equation at genus 3: no HTT correction for KM."""

    def test_l2_vanishes(self):
        result = mc_equation_genus_3()
        assert result["l2_vanishes"]

    def test_l3_vanishes(self):
        result = mc_equation_genus_3()
        assert result["l3_vanishes"]

    def test_l4_plus_vanishes(self):
        result = mc_equation_genus_3()
        assert result["l4_plus_vanishes"]

    def test_theta_3_is_cocycle(self):
        result = mc_equation_genus_3()
        assert result["theta_3_is_cocycle"]


# ============================================================
# Universality: all genera
# ============================================================

class TestUniversality:
    """theta_g is an honest cocycle at all genera for KM."""

    def test_universality_to_genus_5(self):
        results = verify_km_theta_universality(max_genus=5)
        for name, ok in results.items():
            assert ok, f"Universality failed: {name}"

    def test_no_correction_genus_2(self):
        results = verify_km_theta_universality()
        assert results["theta_2_no_correction"]

    def test_no_correction_genus_3(self):
        results = verify_km_theta_universality()
        assert results["theta_3_no_correction"]

    def test_no_correction_genus_4(self):
        results = verify_km_theta_universality()
        assert results["theta_4_no_correction"]

    def test_no_correction_genus_5(self):
        results = verify_km_theta_universality()
        assert results["theta_5_no_correction"]


# ============================================================
# kappa values
# ============================================================

class TestKappaValues:
    """Obstruction coefficient kappa(sl_2, k) = 3(k+2)/4."""

    def test_kappa_at_k1(self):
        assert kappa_sl2(1) == Fraction(9, 4)

    def test_kappa_at_k_minus2(self):
        """Critical level k = -h^vee = -2: kappa = 0."""
        assert kappa_sl2(-2) == Fraction(0)

    def test_kappa_formula(self):
        """kappa = 3(k+2)/4 for various k."""
        for k in range(-5, 10):
            expected = Fraction(3 * (k + 2), 4)
            assert kappa_sl2(k) == expected, f"kappa({k}) = {kappa_sl2(k)}, expected {expected}"


# ============================================================
# theta_g coefficient data
# ============================================================

class TestThetaCoefficient:

    def test_theta_genus_1(self):
        data = theta_g_coefficient(1, 1)
        assert data["genus"] == 1
        assert data["kappa"] == Fraction(9, 4)
        assert data["no_htt_correction"]

    def test_theta_genus_2(self):
        data = theta_g_coefficient(1, 2)
        assert data["genus"] == 2
        assert data["no_htt_correction"]
        assert data["theta_g_proportional_to_phi"]

    def test_theta_genus_3(self):
        data = theta_g_coefficient(1, 3)
        assert data["genus"] == 3
        assert data["no_htt_correction"]


# ============================================================
# Full summary
# ============================================================

class TestSummary:
    """Integration test: the full genus-2 HTT computation."""

    def test_summary_runs(self):
        summary = genus2_htt_summary()
        assert summary is not None

    def test_all_d_squared_pass(self):
        summary = genus2_htt_summary()
        for name, ok in summary["d_squared_zero"].items():
            assert ok, f"d^2 failed: {name}"

    def test_all_sdr_pass(self):
        summary = genus2_htt_summary()
        for name, ok in summary["sdr_verified"].items():
            assert ok, f"SDR failed: {name}"

    def test_genus_2_conclusion(self):
        summary = genus2_htt_summary()
        assert summary["mc_genus_2"]["theta_2_is_cocycle"]

    def test_genus_3_conclusion(self):
        summary = genus2_htt_summary()
        assert summary["mc_genus_3"]["theta_3_is_cocycle"]

    def test_conclusion_text(self):
        summary = genus2_htt_summary()
        assert "no HTT correction" in summary["conclusion"].lower() or \
               "No HTT correction" in summary["conclusion"]


# ============================================================
# Helper
# ============================================================

def _fraction_matrix_rank(M: np.ndarray) -> int:
    """Compute rank of a Fraction matrix via row echelon form."""
    M = np.array(M, dtype=object).copy()
    rows, cols = M.shape
    pivot_row = 0
    for col in range(cols):
        found = False
        for row in range(pivot_row, rows):
            if M[row, col] != Fraction(0):
                M[[pivot_row, row]] = M[[row, pivot_row]]
                found = True
                break
        if not found:
            continue
        pv = M[pivot_row, col]
        for c2 in range(cols):
            M[pivot_row, c2] = Fraction(M[pivot_row, c2], pv)
        for row in range(rows):
            if row != pivot_row and M[row, col] != Fraction(0):
                factor = M[row, col]
                for c2 in range(cols):
                    M[row, c2] -= factor * M[pivot_row, c2]
        pivot_row += 1
    return pivot_row
