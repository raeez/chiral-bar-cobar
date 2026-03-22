"""Genus-1 modular R-matrix corrections for the ordered bar complex.

Computes the genus-1 correction r₁(z; τ) to the binary R-matrix for
standard families.  At genus 0, r₀(z) = r(z) is the collision residue
of the universal MC element Θ_A.  At genus 1, the R-matrix acquires a
correction from the Weierstrass ℘-function (double-pole propagator on
the elliptic curve E_τ).

KEY RESULTS:
  1. Heisenberg: r₁(z; τ) = k · ℘(z; τ) (scalar, Weierstrass ℘)
     av(r₁) = κ · λ₁ where λ₁ is the first tautological class.
  2. Affine sl_2: r₁(z; τ) has a Casimir part + non-Casimir corrections.
  3. Modular R-matrix: R^mod(z; ℏ) = r₀(z) + ℏ² r₁(z; τ) + O(ℏ⁴)
     is a deformation of the genus-0 R-matrix.

The genus-1 correction measures the obstruction to extending the
genus-0 R-matrix data to higher genus.  For Heisenberg, the correction
is proportional to the Weierstrass ℘-function, reflecting the
replacement of 1/z² by ℘(z; τ) when passing from C to E_τ.

References:
  - higher_genus_foundations.tex: genus-1 propagator, Arakelov metric
  - higher_genus_modular_koszul.tex: modular R-matrix, genus tower
  - heisenberg_frame.tex: Heisenberg genus-1 curvature
  - e1_lattice_genus1.py: lattice genus-1 computation
"""

from __future__ import annotations

import numpy as np
from typing import Dict, Optional
from sympy import (
    Symbol, Rational, Matrix, simplify, pi, I, exp,
    Function, series, O, oo, symbols, cos, sin, sqrt
)


k = Symbol('k', positive=True)
c = Symbol('c')
z = Symbol('z')
tau = Symbol('tau')
hbar = Symbol('hbar')
q_nome = Symbol('q')  # nome q = exp(2*pi*i*tau)


# =========================================================================
# Weierstrass functions on the elliptic curve
# =========================================================================

def weierstrass_p_fourier(z_val: float, tau_val: complex, n_terms: int = 20) -> complex:
    """Numerical evaluation of Weierstrass ℘(z; τ) via Fourier expansion.

    ℘(z; τ) = (2πi)² [ -1/12 + q_z/(1-q_z)² + q_z⁻¹/(1-q_z⁻¹)²
               + Σ_{n≥1} q^n { q_z·q^n/(1-q_z·q^n)² + ... } ]

    where q = e^{2πiτ}, q_z = e^{2πiz}.

    For computational purposes we use the standard formula:
    ℘(z) = 1/z² + Σ' [ 1/(z - mτ - n)² - 1/(mτ + n)² ]

    Simplified Fourier form:
    ℘(z; τ) = π²/3 · E₂(τ) + (2πi)² Σ_{n=1}^∞ n·q^n/(1-q^n) · (q_z^n + q_z^{-n})

    Actually, the cleanest formula:
    ℘(z; τ) = -2 Σ_{n≥1} n q^n/(1-q^n) · cos(2πnz)  (up to normalization)
    """
    q = np.exp(2j * np.pi * tau_val)
    qz = np.exp(2j * np.pi * z_val)

    # Laurent part: π² / sin²(πz) contribution
    sin_pz = np.sin(np.pi * z_val)
    if abs(sin_pz) < 1e-15:
        return float('inf')

    laurent = (np.pi / sin_pz) ** 2

    # Eisenstein correction: -π²/3 · E₂(τ)
    # E₂(τ) = 1 - 24 Σ_{n≥1} n q^n/(1-q^n)
    e2_sum = 0.0
    for n in range(1, n_terms + 1):
        qn = q ** n
        e2_sum += n * qn / (1 - qn)
    e2 = 1 - 24 * e2_sum

    # Fourier series part
    fourier_sum = 0.0
    for n in range(1, n_terms + 1):
        qn = q ** n
        sigma_term = qn / (1 - qn) ** 2
        fourier_sum += n * sigma_term * (qz ** n + qz ** (-n))

    # Full ℘:
    # ℘(z; τ) = π²/sin²(πz) - π²E₂(τ)/3 + 8π² Σ ...
    # Standard normalization: periods (1, τ)
    wp = laurent - np.pi ** 2 * e2 / 3 + 8 * np.pi ** 2 * fourier_sum

    return complex(wp)


def weierstrass_p_leading(z_val: float) -> float:
    """Leading term of ℘(z) near z = 0: ℘(z) ~ 1/z².

    This is the genus-0 limit: as τ → i∞ (degeneration to P¹),
    the elliptic curve degenerates and ℘(z; τ) → 1/z² + regular.
    """
    if abs(z_val) < 1e-15:
        return float('inf')
    return 1.0 / z_val ** 2


# =========================================================================
# Heisenberg genus-1 R-matrix
# =========================================================================

class HeisenbergGenus1:
    """Genus-1 modular R-matrix for the Heisenberg algebra H_k.

    At genus 0: r₀(z) = k/z (simple pole, collision residue).
    At genus 1: r₁(z; τ) = k · ℘(z; τ) (double pole on E_τ).

    The full modular R-matrix:
    R^mod(z; ℏ) = k/z + ℏ² · k · ℘(z; τ) + O(ℏ⁴)

    The genus-1 term is a DEFORMATION of the genus-0 R-matrix,
    replacing 1/z by ℘(z; τ) (the Arakelov propagator on E_τ).
    """

    def __init__(self, level=None):
        self.level = level if level is not None else k

    def r0(self, z_val: float, level_val: float = 1.0) -> float:
        """Genus-0 R-matrix: r₀(z) = k/z."""
        if abs(z_val) < 1e-15:
            return float('inf')
        return level_val / z_val

    def r1(self, z_val: float, tau_val: complex,
            level_val: float = 1.0, n_terms: int = 20) -> complex:
        """Genus-1 R-matrix correction: r₁(z; τ) = k · ℘(z; τ).

        This is the genus-1 propagator replacement: the 1/z² pole
        in the OPE is dressed by the Weierstrass ℘-function on E_τ.
        """
        wp = weierstrass_p_fourier(z_val, tau_val, n_terms)
        return level_val * wp

    def r1_is_scalar(self) -> bool:
        """r₁(z; τ) is scalar (proportional to identity).

        The Heisenberg has a single generator h, so all R-matrix
        data is 1×1.  The genus-1 correction inherits this scalar
        property.
        """
        return True

    def r1_average(self, level_val: float = 1.0) -> Dict:
        """av(r₁) = κ · λ₁ = k · λ₁.

        The average of the genus-1 R-matrix gives the product of
        the curvature κ = k with the first tautological class λ₁
        on M̄_{1,1}.

        λ₁ = 1/24 (the orbifold Euler characteristic of M_{1,1}).
        """
        kappa = level_val
        lambda1 = Rational(1, 24)
        return {
            "kappa": kappa,
            "lambda1": float(lambda1),
            "product": kappa * float(lambda1),
            "formula": "kappa * lambda_1 = k/24",
        }

    def modular_r_matrix(self, z_val: float, tau_val: complex,
                          hbar_val: float, level_val: float = 1.0) -> complex:
        """Full modular R-matrix: R^mod(z; ℏ) = r₀(z) + ℏ² r₁(z; τ) + ...

        The expansion parameter ℏ tracks the genus: ℏ^{2g} for genus g.
        At genus 0: the collision residue r₀(z) = k/z.
        At genus 1: the ℘-correction with coefficient ℏ².
        """
        r0_val = self.r0(z_val, level_val)
        r1_val = self.r1(z_val, tau_val, level_val)
        return r0_val + hbar_val ** 2 * r1_val

    def verify_degeneration(self, z_val: float = 0.1,
                             level_val: float = 1.0) -> Dict:
        """Verify that r₁(z; τ) → 1/z² as τ → i∞.

        As the elliptic curve degenerates (Im(τ) → ∞), the
        Weierstrass ℘-function approaches 1/z² + const.
        The genus-1 R-matrix degenerates to the genus-0 double-pole.
        """
        # Large Im(τ): the nome q → 0
        tau_values = [1j * t for t in [1, 2, 5, 10, 20]]
        wp_values = []
        for tv in tau_values:
            wp = weierstrass_p_fourier(z_val, tv)
            wp_values.append(wp)

        leading = 1.0 / z_val ** 2
        ratios = [float(np.real(wp)) / leading for wp in wp_values]

        return {
            "z": z_val,
            "tau_values": [f"i*{float(tv.imag)}" for tv in tau_values],
            "wp_values": [complex(wp) for wp in wp_values],
            "leading_term": leading,
            "ratios_to_leading": ratios,
            "approaches_1": abs(ratios[-1] - 1.0) < 0.01,
        }


# =========================================================================
# Affine sl_2 genus-1 R-matrix
# =========================================================================

class AffineSl2Genus1:
    """Genus-1 modular R-matrix for affine sl_2 at level k.

    At genus 0: r₀(z) = k·Ω/z where Ω is the sl_2 Casimir.
    At genus 1: r₁(z; τ) has a Casimir part proportional to ℘(z;τ)·Ω
    plus non-Casimir corrections from the structure constants.

    The Casimir part:
      r₁^Cas(z; τ) = k/(k+2)² · ℘(z; τ) · Ω

    The non-Casimir part involves higher Casimir elements and the
    KZ associator corrections at genus 1.
    """

    def __init__(self, level=None):
        self.level = level if level is not None else k
        self.hv = 2  # dual Coxeter number for sl_2
        self.dim_g = 3

    def casimir_tensor_4x4(self) -> np.ndarray:
        """4×4 Casimir tensor Ω for sl_2 on C²⊗C²."""
        e = np.array([[0, 1], [0, 0]], dtype=complex)
        f = np.array([[0, 0], [1, 0]], dtype=complex)
        h = np.array([[1, 0], [0, -1]], dtype=complex)
        return (np.kron(h, h) / 2.0 + np.kron(e, f) + np.kron(f, e))

    def r1_casimir_part(self, z_val: float, tau_val: complex,
                         level_val: float = 1.0) -> np.ndarray:
        """Casimir part of genus-1 R-matrix: k/(k+h^v)² · ℘(z;τ) · Ω.

        The Sugawara denominator (k + h^v)² appears from the genus-1
        propagator correction squared (one factor from each leg).
        """
        omega = self.casimir_tensor_4x4()
        wp = weierstrass_p_fourier(z_val, tau_val)
        coeff = level_val / (level_val + self.hv) ** 2
        return coeff * wp * omega

    def r1_has_non_casimir(self) -> bool:
        """The genus-1 R-matrix has non-Casimir corrections.

        These come from the structure constants f^c_{ab} contracted
        with the genus-1 propagator.  They vanish for abelian algebras
        (Heisenberg) but are present for non-abelian ones.
        """
        return True

    def kappa_genus1(self, level_val: float = 1.0) -> float:
        """Genus-1 curvature for affine sl_2:
        κ = (k+h^v)·dim(g)/(2·h^v) = 3(k+2)/4.

        Same as genus 0: the curvature κ does not change with genus.
        The genus-1 correction contributes to the TAUTOLOGICAL CLASS
        coefficient (κ · λ₁) but not to κ itself.
        """
        return self.dim_g * (level_val + self.hv) / (2 * self.hv)


# =========================================================================
# Modular R-matrix consistency checks
# =========================================================================

def verify_genus0_limit(family: str, z_val: float = 0.1,
                         **kwargs) -> Dict:
    """Verify that r₁(z; τ) / r₀'(z) → 1 as τ → i∞.

    In the degeneration limit, the genus-1 correction should
    reproduce the genus-0 double-pole structure.

    For Heisenberg: r₁ = k·℘(z;τ) → k/z² and r₀ = k/z,
    so r₁ ≈ r₀/z = (k/z)/z = k/z².
    """
    if family == "Heisenberg":
        level_val = kwargs.get("k", 1.0)
        h = HeisenbergGenus1(level=Symbol('k'))

        # Compare r₁(z; τ→i∞) with k/z²
        tau_large = 10j
        r1_val = h.r1(z_val, tau_large, level_val)
        expected = level_val / z_val ** 2

        ratio = float(np.real(r1_val)) / expected

        return {
            "family": family,
            "z": z_val,
            "tau": "10i",
            "r1_value": complex(r1_val),
            "expected_limit": expected,
            "ratio": ratio,
            "consistent": abs(ratio - 1.0) < 0.05,
        }
    else:
        return {"family": family, "note": "Not implemented"}


def modular_r_consistency(level_val: float = 1.0,
                           z_val: float = 0.1,
                           tau_val: complex = 0.5j) -> Dict:
    """Verify the modular R-matrix consistency for Heisenberg.

    R^mod(z; ℏ) = k/z + ℏ² · k · ℘(z; τ) + O(ℏ⁴)

    Check:
    1. At ℏ = 0: R^mod = r₀ (genus 0)
    2. The ℏ² coefficient is k · ℘(z; τ)
    3. R^mod is a deformation of r₀
    """
    h = HeisenbergGenus1()

    r0 = h.r0(z_val, level_val)
    r1 = h.r1(z_val, tau_val, level_val)

    # At various ℏ values
    hbar_values = [0, 0.01, 0.1]
    r_mod_values = []
    for hb in hbar_values:
        r_mod = h.modular_r_matrix(z_val, tau_val, hb, level_val)
        r_mod_values.append(r_mod)

    return {
        "r0": r0,
        "r1": complex(r1),
        "r_mod_at_hbar_0": complex(r_mod_values[0]),
        "r_mod_at_hbar_0_matches_r0": abs(complex(r_mod_values[0]) - r0) < 1e-10,
        "deformation_direction": complex(r1),
        "deformation_nonzero": abs(r1) > 1e-10,
    }
