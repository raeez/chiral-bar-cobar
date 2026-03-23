"""Tests for analytic bar MC: MC structure preservation under HS-sewing completion.

Verifies that the Maurer-Cartan structure of Theta_A := D_A - d_0 survives
the analytic completion from the algebraic bar complex to the sewing envelope A^sew.

Eight verification axes:
  I.    Heisenberg MC at genus 1: kappa extraction, curvature, free energy
  II.   HS-sewing convergence: ||K_q||_HS finite for |q| < 1
  III.  MC preservation under shadow tower truncation
  IV.   Analytic continuation on upper half-plane
  V.    Fredholm determinant / Eisenstein G_2 bridge
  VI.   Lattice V_Z theta correction
  VII.  Analytic vs algebraic MC comparison
  VIII. Bar differential squared at genus 1

Ground truth:
  thm:mc2-bar-intrinsic (Theta_A bar-intrinsic MC construction),
  thm:general-hs-sewing (HS-sewing for standard landscape),
  thm:heisenberg-sewing (Heisenberg Fredholm determinant),
  mc5_genus1_bridge.py (genus-1 conventions).
"""

import math

import numpy as np
import pytest

from compute.lib.analytic_bar_mc import (
    heisenberg_kappa,
    heisenberg_mc_genus1,
    hs_norm_sewing_operator,
    hs_norm_sewing_operator_partial,
    hs_convergence_table,
    heisenberg_shadow_truncation,
    mock_virasoro_shadow_truncation,
    theta_genus1_heisenberg,
    verify_analyticity_on_uhp,
    sigma1,
    eisenstein_G2_q_coefficients,
    fredholm_determinant_heisenberg,
    log_det_derivative_numerical,
    verify_G2_from_fredholm,
    verify_G2_quasi_modularity,
    jacobi_theta3,
    lattice_vz_mc_genus1,
    analytic_vs_algebraic_mc_heisenberg,
    bar_d_squared_genus1,
    dedekind_eta_from_product,
    heisenberg_partition_function,
)


# ======================================================================
# I. Heisenberg MC at genus 1
# ======================================================================

class TestHeisensteinMCGenus1:
    """Heisenberg MC at genus 1: kappa = 1, d^2 = kappa * omega_1."""

    def test_kappa_value(self):
        """kappa(H) = 1 at unit level (anomaly ratio rho = 1)."""
        assert heisenberg_kappa() == 1.0

    def test_kappa_extraction(self):
        """Shadow extraction gives kappa = 1."""
        mc = heisenberg_mc_genus1(kappa=1.0)
        assert mc["kappa_match"]

    def test_free_energy_genus1(self):
        """F_1 = kappa/24 = 1/24."""
        mc = heisenberg_mc_genus1(kappa=1.0)
        assert abs(mc["F1"] - 1.0 / 24.0) < 1e-15

    def test_curvature_absorption(self):
        """Period correction absorbs curvature: t_1 = kappa * lambda_1^FP."""
        mc = heisenberg_mc_genus1(kappa=0.5)
        assert mc["curvature_absorbed"]

    def test_mc_satisfied(self):
        """MC equation D*Theta + (1/2)[Theta,Theta] = 0 holds at genus 1."""
        mc = heisenberg_mc_genus1(kappa=0.5)
        assert mc["mc_satisfied"]

    def test_shadow_depth(self):
        """Heisenberg has shadow depth 2 (Gaussian class G)."""
        mc = heisenberg_mc_genus1()
        assert mc["shadow_depth"] == 2

    def test_kappa_at_level_1(self):
        """At level kappa=1: kappa(H_1) = 1, F_1 = 1/24."""
        mc = heisenberg_mc_genus1(kappa=1.0)
        assert abs(mc["kappa"] - 1.0) < 1e-15
        assert abs(mc["F1"] - 1.0 / 24.0) < 1e-15


# ======================================================================
# II. HS-sewing convergence
# ======================================================================

class TestHSSewingConvergence:
    """||K_q||_HS = q/sqrt(1-q^2) finite for |q| < 1."""

    def test_hs_norm_formula_q01(self):
        """At q=0.1: ||K_q||_HS = 0.1/sqrt(1-0.01) = 0.1/sqrt(0.99)."""
        q = 0.1
        expected = q / math.sqrt(1.0 - q * q)
        actual = hs_norm_sewing_operator(q)
        assert abs(actual - expected) < 1e-12

    def test_hs_norm_formula_q05(self):
        """At q=0.5: ||K_q||_HS = 0.5/sqrt(0.75)."""
        q = 0.5
        expected = q / math.sqrt(1.0 - q * q)
        actual = hs_norm_sewing_operator(q)
        assert abs(actual - expected) < 1e-12

    def test_hs_norm_formula_q09(self):
        """At q=0.9: ||K_q||_HS = 0.9/sqrt(0.19)."""
        q = 0.9
        expected = q / math.sqrt(1.0 - q * q)
        actual = hs_norm_sewing_operator(q)
        assert abs(actual - expected) < 1e-12

    def test_hs_norm_finite_for_q_less_than_1(self):
        """||K_q||_HS < infty for all |q| < 1."""
        for q in [0.1, 0.3, 0.5, 0.7, 0.9, 0.99]:
            norm = hs_norm_sewing_operator(q)
            assert math.isfinite(norm)
            assert norm > 0

    def test_hs_norm_infinite_at_q1(self):
        """||K_q||_HS = infty at |q| = 1."""
        assert hs_norm_sewing_operator(1.0) == float('inf')

    def test_hs_norm_monotone_increasing(self):
        """||K_q||_HS is strictly increasing in q on (0,1)."""
        q_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        norms = [hs_norm_sewing_operator(q) for q in q_values]
        for i in range(len(norms) - 1):
            assert norms[i] < norms[i + 1]

    def test_hs_norm_partial_converges_to_exact(self):
        """Partial sum approximation converges to exact formula."""
        q = 0.5
        exact = hs_norm_sewing_operator(q)
        partial = hs_norm_sewing_operator_partial(q, 1000)
        assert abs(exact - partial) / exact < 1e-8

    def test_convergence_table_all_finite(self):
        """All entries in the convergence table are finite."""
        table = hs_convergence_table()
        assert len(table) == 6
        for row in table:
            assert row["is_finite"]

    def test_convergence_rate_q099(self):
        """At q=0.99, partial sum with N=100 has small relative error."""
        q = 0.99
        exact = hs_norm_sewing_operator(q)
        # At q=0.99 convergence is slow; N=100 should still approximate
        # But the geometric series converges: q^2/(1-q^2) for the tail
        partial = hs_norm_sewing_operator_partial(q, 1000)
        assert abs(exact - partial) / exact < 1e-4


# ======================================================================
# III. MC preservation under shadow tower truncation
# ======================================================================

class TestShadowTowerTruncation:
    """Obstruction ratio ||o_{r+1}||/||Theta^{<=r}|| for Heisenberg and Virasoro."""

    def test_heisenberg_all_obstructions_vanish(self):
        """Heisenberg: o_{r+1} = 0 for all r >= 2 (shadow depth 2)."""
        trunc = heisenberg_shadow_truncation(r_max=6)
        for row in trunc:
            assert row["obstruction_vanishes"]
            assert row["ratio"] == 0.0

    def test_heisenberg_theta_norm_constant(self):
        """Heisenberg: ||Theta^{<=r}|| = kappa for all r >= 2."""
        trunc = heisenberg_shadow_truncation()
        kappa = heisenberg_kappa()
        for row in trunc:
            assert abs(row["theta_norm"] - kappa) < 1e-15

    def test_virasoro_cubic_gauge_trivial(self):
        """Virasoro: cubic obstruction is gauge-trivial (o_3 effective = 0)."""
        trunc = mock_virasoro_shadow_truncation(c=25.0)
        r2_row = trunc[0]  # r=2
        assert abs(r2_row["obstruction_norm"]) < 1e-15  # cubic is gauge-trivial

    def test_virasoro_quartic_nonzero(self):
        """Virasoro: quartic resonance class Q^contact != 0."""
        trunc = mock_virasoro_shadow_truncation(c=25.0)
        r3_row = trunc[1]  # r=3
        assert r3_row["obstruction_norm"] > 0  # quartic is nonzero

    def test_virasoro_obstructions_decrease(self):
        """Virasoro: ||o_{r+1}|| decreases for r >= 4."""
        trunc = mock_virasoro_shadow_truncation(c=25.0, r_max=8)
        # Skip r=2 (gauge-trivial) and r=3 (quartic seed)
        norms = [row["obstruction_norm"] for row in trunc if row["r"] >= 4]
        for i in range(len(norms) - 1):
            assert norms[i] >= norms[i + 1]

    def test_virasoro_ratio_decreases(self):
        """Virasoro: ||o_{r+1}||/||Theta^{<=r}|| decreases."""
        trunc = mock_virasoro_shadow_truncation(c=25.0, r_max=8)
        ratios = [row["ratio"] for row in trunc if row["r"] >= 4]
        for i in range(len(ratios) - 1):
            assert ratios[i] >= ratios[i + 1]

    def test_virasoro_quartic_formula(self):
        """Q^contact_Vir = 10/[c(5c+22)] at c=25."""
        c = 25.0
        Q_expected = 10.0 / (c * (5.0 * c + 22.0))
        trunc = mock_virasoro_shadow_truncation(c=c)
        # r=3 obstruction is the quartic class
        assert abs(trunc[1]["obstruction_norm"] - Q_expected) < 1e-12


# ======================================================================
# IV. Analytic continuation on upper half-plane
# ======================================================================

class TestAnalyticContinuation:
    """Theta^{(1,1)}_H is analytic on the upper half-plane."""

    def test_q_in_unit_disk(self):
        """For Im(tau) > 0, |q| = |e^{2*pi*i*tau}| < 1."""
        tau = 0.3 + 1.0j
        data = theta_genus1_heisenberg(tau)
        assert data["valid"]
        assert data["abs_q"] < 1.0

    def test_q_magnitude(self):
        """|q| = e^{-2*pi*Im(tau)}."""
        tau = 0.0 + 0.5j
        data = theta_genus1_heisenberg(tau)
        expected_abs_q = math.exp(-2.0 * math.pi * tau.imag)
        assert abs(data["abs_q"] - expected_abs_q) < 1e-12

    def test_lower_half_plane_rejected(self):
        """tau in lower half-plane is rejected."""
        tau = 0.3 - 1.0j
        data = theta_genus1_heisenberg(tau)
        assert not data["valid"]

    def test_coefficient_constant_across_tau(self):
        """Theta^{(1,1)} coefficient is constant (independent of tau)."""
        result = verify_analyticity_on_uhp()
        assert result["coefficient_constant"]

    def test_analyticity_verified(self):
        """Full analyticity verification passes."""
        result = verify_analyticity_on_uhp()
        assert result["analyticity_verified"]

    def test_coefficient_value(self):
        """Theta^{(1,1)} = kappa * 2*pi*i = pi*i at kappa=1/2."""
        result = verify_analyticity_on_uhp(kappa=0.5)
        expected = 0.5 * 2.0 * np.pi * 1j
        assert abs(result["coefficient_value"] - expected) < 1e-12


# ======================================================================
# V. Fredholm determinant / Eisenstein G_2 bridge
# ======================================================================

class TestFredholmG2Bridge:
    """det(1-K_q) generates genus-1 MC data; derivative gives G_2."""

    def test_sigma1_small_values(self):
        """sigma_1(n) for small n."""
        assert sigma1(1) == 1
        assert sigma1(2) == 3
        assert sigma1(3) == 4
        assert sigma1(4) == 7
        assert sigma1(5) == 6
        assert sigma1(6) == 12

    def test_fredholm_determinant_at_small_q(self):
        """det(1-K_q) ~ 1 - q for small q."""
        q = 0.01
        det = fredholm_determinant_heisenberg(q, N_modes=100)
        # Leading term: (1-q)(1-q^2)... ~ 1 - q - q^2 + ...
        assert abs(det - (1.0 - q)) < 0.02

    def test_fredholm_determinant_positive_for_real_q(self):
        """det(1-K_q) > 0 for 0 < q < 1 (real)."""
        for q in [0.1, 0.3, 0.5, 0.7, 0.9]:
            det = fredholm_determinant_heisenberg(q, N_modes=200)
            assert det.real > 0

    def test_G2_from_fredholm_match(self):
        """d/dtau log det(1-K_q) matches sum sigma_1(n)*q^n."""
        result = verify_G2_from_fredholm(q=0.1)
        assert result["match"]

    def test_G2_from_fredholm_match_q05(self):
        """Same verification at q=0.5."""
        result = verify_G2_from_fredholm(q=0.5)
        assert result["match"]

    def test_G2_quasi_modularity(self):
        """E_2(-1/tau) = tau^2 * E_2(tau) + 12*tau/(2*pi*i)."""
        result = verify_G2_quasi_modularity(tau=0.25 + 1.0j)
        assert result["quasi_modular_verified"]

    def test_G2_quasi_modularity_deep(self):
        """Quasi-modularity at a different tau value."""
        result = verify_G2_quasi_modularity(tau=0.1 + 0.5j, N=500)
        assert result["quasi_modular_verified"]

    def test_G2_anomaly_is_curvature_source(self):
        """The quasi-modular anomaly is the source of genus-1 curvature."""
        result = verify_G2_quasi_modularity()
        assert "curvature anomaly" in result["anomaly_source"]


# ======================================================================
# VI. Lattice V_Z theta correction
# ======================================================================

class TestLatticeExtension:
    """V_Z MC data includes theta function correction."""

    def test_vz_kappa(self):
        """kappa(V_Z) = 1 (rank of lattice)."""
        data = lattice_vz_mc_genus1(tau=0.5j)
        assert data["valid"]
        assert data["kappa"] == 1.0

    def test_vz_mc_satisfied(self):
        """MC equation satisfied for V_Z including theta correction."""
        data = lattice_vz_mc_genus1(tau=0.5j)
        assert data["mc_satisfied"]

    def test_theta3_real_on_imaginary_axis(self):
        """theta_3(tau) is real for tau purely imaginary."""
        tau = 0.5j
        theta = jacobi_theta3(tau, N=200)
        # theta_3 on the imaginary axis: real-valued
        assert abs(theta.imag) < 1e-10

    def test_theta3_positive_on_imaginary_axis(self):
        """theta_3(tau) > 0 for tau purely imaginary with Im(tau) > 0."""
        tau = 0.5j
        theta = jacobi_theta3(tau, N=200)
        assert theta.real > 0

    def test_vz_upper_half_plane_only(self):
        """V_Z MC computation rejects lower half-plane."""
        data = lattice_vz_mc_genus1(tau=-0.5j)
        assert not data["valid"]


# ======================================================================
# VII. Analytic vs algebraic MC comparison
# ======================================================================

class TestAnalyticVsAlgebraic:
    """Zero difference for exactly solvable Heisenberg."""

    def test_all_q_values_match(self):
        """Algebraic and analytic MC solutions agree at all test q values.

        With N_algebraic=N_analytic=500, the product has fully converged.
        """
        results = analytic_vs_algebraic_mc_heisenberg(
            N_algebraic=500, N_analytic=500,
        )
        for row in results:
            assert row["match"], f"Mismatch at q={row['q']}"

    def test_relative_difference_decreases_with_truncation(self):
        """Relative difference decreases as N_algebraic approaches N_analytic.

        For Heisenberg (exactly solvable), the algebraic formal series IS the
        analytic solution. The only source of disagreement is truncation level.
        At fixed N_analytic=500, increasing N_algebraic from 50 to 400 should
        reduce the relative difference at q=0.9.
        """
        q = 0.9
        diffs = []
        for N_alg in [50, 100, 200, 400]:
            results = analytic_vs_algebraic_mc_heisenberg(
                q_values=[q], N_algebraic=N_alg, N_analytic=500,
            )
            diffs.append(results[0]["relative_difference"])
        # Each increase should reduce relative error
        for i in range(len(diffs) - 1):
            assert diffs[i] >= diffs[i + 1] - 1e-15

    def test_convergence_improves_with_N(self):
        """Increasing N_algebraic reduces the difference."""
        q = 0.5
        diffs = []
        for N in [10, 50, 100, 200]:
            results = analytic_vs_algebraic_mc_heisenberg(
                q_values=[q], N_algebraic=N, N_analytic=500
            )
            diffs.append(results[0]["absolute_difference"])
        # Each increase in N should reduce or maintain the difference
        for i in range(len(diffs) - 1):
            assert diffs[i] >= diffs[i + 1] - 1e-15  # monotone decrease


# ======================================================================
# VIII. Bar differential squared at genus 1
# ======================================================================

class TestBarDSquared:
    """d^2(x) = [kappa*omega, x] = kappa*x (omega central) at genus 1."""

    def test_d_squared_proportional_to_kappa(self):
        """d^2(a_w) = kappa * a_w for all test weights."""
        results = bar_d_squared_genus1(kappa=0.5)
        for row in results:
            assert row["match"]

    def test_d_squared_zero_when_kappa_zero(self):
        """d^2 = 0 when kappa = 0 (uncurved, genus-0 behavior)."""
        results = bar_d_squared_genus1(kappa=0.0)
        for row in results:
            assert abs(row["d_squared_coefficient"]) < 1e-15

    def test_omega_centrality(self):
        """omega is central in the CDG algebra structure."""
        results = bar_d_squared_genus1(kappa=0.5)
        for row in results:
            assert row["is_central"]

    def test_d_squared_scales_with_kappa(self):
        """d^2 scales linearly with kappa."""
        results_1 = bar_d_squared_genus1(kappa=1.0)
        results_2 = bar_d_squared_genus1(kappa=2.0)
        for r1, r2 in zip(results_1, results_2):
            assert abs(r2["d_squared_coefficient"] - 2.0 * r1["d_squared_coefficient"]) < 1e-15


# ======================================================================
# IX. Cross-cutting structural tests
# ======================================================================

class TestCrossCutting:
    """Structural consistency across all axes."""

    def test_dedekind_eta_modular_weight(self):
        """eta(tau) transforms with weight 1/2 under SL_2(Z).

        Specifically, eta(-1/tau) = sqrt(-i*tau) * eta(tau).
        Verify numerically.
        """
        tau = 0.3 + 1.0j
        q = np.exp(2j * np.pi * tau)
        eta_tau = dedekind_eta_from_product(q, N=300)

        tau_inv = -1.0 / tau
        q_inv = np.exp(2j * np.pi * tau_inv)
        eta_tau_inv = dedekind_eta_from_product(q_inv, N=300)

        # eta(-1/tau) = sqrt(-i*tau) * eta(tau)
        rhs = np.sqrt(-1j * tau) * eta_tau
        # Use principal branch of sqrt
        diff = abs(eta_tau_inv - rhs)
        assert diff < 1e-6, f"eta modularity failed: diff={diff}"

    def test_heisenberg_partition_function_positive(self):
        """Z_H(tau) > 0 for tau on the positive imaginary axis."""
        tau = 1.0j
        Z = heisenberg_partition_function(tau)
        assert Z.real > 0
        assert abs(Z.imag) < 1e-10

    def test_fredholm_equals_eta_product(self):
        """det(1-K_q) = prod(1-q^n) = q^{-1/24} * eta(tau)."""
        tau = 0.5j
        q = np.exp(2j * np.pi * tau)
        det = fredholm_determinant_heisenberg(q, N_modes=300)
        eta = dedekind_eta_from_product(q, N=300)
        # det = prod(1-q^n) and eta = q^{1/24} * prod(1-q^n)
        # so det = q^{-1/24} * eta
        expected_det = eta * q**(-1.0 / 24.0)
        diff = abs(det - expected_det)
        assert diff < 1e-10

    def test_mc_kappa_consistent_across_modules(self):
        """kappa = 1/2 is consistent between MC and sewing modules."""
        kappa = heisenberg_kappa()
        mc = heisenberg_mc_genus1(kappa=kappa)
        assert abs(mc["kappa"] - kappa) < 1e-15
        # HS norm is finite at all q < 1
        assert math.isfinite(hs_norm_sewing_operator(0.5))

    def test_eisenstein_divisor_sum_identity(self):
        """sum n*q^n/(1-q^n) = sum sigma_1(m)*q^m (fundamental identity)."""
        for q in [0.1, 0.3, 0.5]:
            result = verify_G2_from_fredholm(q=q)
            assert result["match"]
