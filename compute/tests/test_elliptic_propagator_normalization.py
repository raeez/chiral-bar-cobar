"""Tests for the genus-1 elliptic propagator normalization."""

from __future__ import annotations

import cmath
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _parity_sign(n: int) -> int:
    return -1 if n % 2 else 1


def theta1_period_1(u: complex, tau: complex, terms: int = 60) -> complex:
    """Jacobi theta_1 in the manuscript's period lattice Z + tau Z."""
    return -1j * sum(
        _parity_sign(n)
        * cmath.exp(
            math.pi * 1j * tau * (n + 0.5) ** 2
            + math.pi * 1j * (2 * n + 1) * u
        )
        for n in range(-terms, terms + 1)
    )


def theta1_period_1_prime(u: complex, tau: complex, terms: int = 60) -> complex:
    """Derivative of theta1_period_1 with respect to u."""
    return -1j * sum(
        _parity_sign(n)
        * (math.pi * 1j * (2 * n + 1))
        * cmath.exp(
            math.pi * 1j * tau * (n + 0.5) ** 2
            + math.pi * 1j * (2 * n + 1) * u
        )
        for n in range(-terms, terms + 1)
    )


def g1_coefficient(u: complex, tau: complex) -> complex:
    """Corrected coefficient of eta^(1): theta'/theta + 2 pi i Im(u)/Im(tau)."""
    return (
        theta1_period_1_prime(u, tau) / theta1_period_1(u, tau)
        + 2 * math.pi * 1j * (u.imag / tau.imag)
    )


class TestEllipticPropagatorNormalization:
    tau = 0.37 + 1.21j
    u = 0.23 + 0.19j

    def test_corrected_coefficient_is_doubly_periodic(self):
        base = g1_coefficient(self.u, self.tau)
        assert abs(g1_coefficient(self.u + 1, self.tau) - base) < 1e-10
        assert abs(g1_coefficient(self.u + self.tau, self.tau) - base) < 1e-10

    def test_holomorphic_quotient_has_b_cycle_deficit(self):
        quotient = theta1_period_1_prime(self.u, self.tau) / theta1_period_1(self.u, self.tau)
        shifted = (
            theta1_period_1_prime(self.u + self.tau, self.tau)
            / theta1_period_1(self.u + self.tau, self.tau)
        )
        assert abs((shifted - quotient) + 2 * math.pi * 1j) < 1e-10

    def test_corrected_coefficient_is_odd_so_eta_is_symmetric(self):
        assert abs(g1_coefficient(-self.u, self.tau) + g1_coefficient(self.u, self.tau)) < 1e-10

    def test_residue_at_the_diagonal_is_one(self):
        epsilon = 1e-6
        assert abs(epsilon * g1_coefficient(epsilon, self.tau) - 1) < 1e-6

    def test_retired_tex_normalizations_are_absent_from_live_surfaces(self):
        live_files = [
            "chapters/theory/fourier_seed.tex",
            "chapters/theory/higher_genus_foundations.tex",
            "chapters/theory/configuration_spaces.tex",
            "chapters/examples/kac_moody.tex",
            "chapters/examples/beta_gamma.tex",
            "chapters/examples/heisenberg_eisenstein.tex",
            "standalone/chiral_chern_weil.tex",
        ]
        retired_fragments = [
            r"\eta_{ij}^{(1)} = d\log",
            r"\eta_{12}^{(1)} = d\log",
            r"d(\overline{z_i - z_j})",
            r"z_i - z_j}{2\pi i",
            r"\operatorname{Im}(z_i - z_j)\,d\bar{z}_i",
            r"\operatorname{Im}(z_i-z_j)}{\operatorname{Im}\tau}\,d\bar z_i",
            r"\im(z_1-z_2)}{\im(\tau)}\,d\bar z_1",
            r"\eta_{ij}^{(1)}(z_i + \tau, z_j) &= \eta_{ij}^{(1)}(z_i, z_j) -",
        ]
        for relative_path in live_files:
            text = (ROOT / relative_path).read_text()
            for fragment in retired_fragments:
                assert fragment not in text, f"{relative_path}: retired fragment {fragment}"
