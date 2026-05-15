r"""Finite two-channel genus-2 boundary arithmetic for the W3 shadow.

This module records exact rational checks for the T/W primary-channel
normalizations used by the genus-2 cross-channel engine.  Its verified
surface is deliberately narrow:

* kappa_T = c/2, kappa_W = c/3, kappa(W3) = 5c/6;
* diagonal Zamolodchikov metric eta_TT = c/2, eta_WW = c/3;
* C_TTT = C_TWW = c and odd W-count cubic constants vanish;
* finite boundary-graph mixed constants
  3/c, 9/(2c), 1/16, 21/(4c), with total (c + 204)/(16c).

The module does not prove full W3 CohFT genus-2 universality.  The
primary table is a truncated OPE table, not a closed Frobenius algebra
for generic c.  The function ``compute_delta_F2_numerical`` therefore
returns a sector-additivity check, not a direct CohFT graph computation.

Typed firewall used here:

* A is the input chiral algebra.
* B(A) is the ordered bar coalgebra before cohomology.
* A^i is H^*(B(A)).
* A^! is the Verdier/continuous-linear dual branch under the stated
  finite-type or completed hypotheses.
* Omega(B(A)) = A is bar-cobar inversion.
* Z_ch^der(A) = ChirHoch^*(A,A) is the Hochschild bulk object.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
from typing import Dict, List, Optional, Tuple


CHANNELS: Tuple[str, str] = ("T", "W")
BASIS_3D: Tuple[str, str, str] = ("1", "T", "W")

HOLOGRAPHIC_PACKAGE_ENTRIES: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)

MODULAR_KOSZUL_PRIMARY_PROJECTIONS: Tuple[str, ...] = (
    "Fact_X(L)",
    "barB_X(L)",
    "Theta_L",
    "L_L",
    "(V_br, T_br)",
    "R4_mod(L)",
)

OBJECT_FIREWALL: Dict[str, str] = {
    "A": "input chiral algebra",
    "B(A)": "ordered bar coalgebra before cohomology",
    "A^i": "bar cohomology coalgebra H^*(B(A))",
    "A^!": (
        "Verdier/continuous-linear dual branch under finite-type or "
        "completed hypotheses"
    ),
    "Omega(B(A))": "bar-cobar inversion recovering A",
    "Z_ch^der(A)": "ChirHoch^*(A,A), the Hochschild/derived-centre bulk object",
}

KERNEL_NORMALIZATIONS: Dict[str, str] = {
    "affine_raw_collision": "k*Omega_tr/z",
    "affine_KZ_coefficient": "Omega/((k+h^vee)z)",
    "heisenberg_raw_collision": "k/z",
    "virasoro_collision": "(c/2)/z^3 + 2T/z",
}


def holographic_package_entries() -> Tuple[str, ...]:
    """Seven entries of the holographic modular Koszul package."""
    return HOLOGRAPHIC_PACKAGE_ENTRIES


def modular_koszul_primary_projections() -> Tuple[str, ...]:
    """Six primary projections of the compute-side modular Koszul package."""
    return MODULAR_KOSZUL_PRIMARY_PROJECTIONS


def object_firewall() -> Dict[str, str]:
    """Typed roles for A, B(A), A^i, A^!, Omega(B(A)), and Z_ch^der(A)."""
    return dict(OBJECT_FIREWALL)


def kernel_normalizations() -> Dict[str, str]:
    """Collision-kernel normalization constants."""
    return dict(KERNEL_NORMALIZATIONS)


# ============================================================================
# W3 primary-channel data
# ============================================================================


def _check_channel(channel: str) -> None:
    if channel not in CHANNELS:
        raise ValueError(f"Unknown channel: {channel}")


def _check_nonzero_c(c: Fraction) -> None:
    if c == 0:
        raise ZeroDivisionError("The channel metric is degenerate at c=0.")


def kappa_T(c: Fraction) -> Fraction:
    """T-channel characteristic kappa_T = c/2."""
    return c / 2


def kappa_W(c: Fraction) -> Fraction:
    """W-channel characteristic kappa_W = c/3."""
    return c / 3


def kappa_total(c: Fraction) -> Fraction:
    """Total W3 characteristic kappa_T + kappa_W = 5c/6."""
    return kappa_T(c) + kappa_W(c)


def metric(channel: str, c: Fraction) -> Fraction:
    """Diagonal Zamolodchikov metric on the T/W primary channels."""
    _check_channel(channel)
    return kappa_T(c) if channel == "T" else kappa_W(c)


def propagator(channel: str, c: Fraction) -> Fraction:
    """Inverse diagonal metric: eta^TT = 2/c and eta^WW = 3/c."""
    _check_channel(channel)
    _check_nonzero_c(c)
    return Fraction(1) / metric(channel, c)


def C3(i: str, j: str, k: str, c: Fraction) -> Fraction:
    """Truncated W3 cubic constants on primary labels T and W.

    The parity rule W -> -W kills odd W-count cubics.  With the
    normalization eta_TT = c/2 and eta_WW = c/3, the nonzero primary
    constants used by this finite engine are C_TTT = C_TWW = c.
    """
    for channel in (i, j, k):
        _check_channel(channel)
    w_count = sum(label == "W" for label in (i, j, k))
    if w_count % 2:
        return Fraction(0)
    if sorted((i, j, k)) in (["T", "T", "T"], ["T", "W", "W"]):
        return c
    return Fraction(0)


def frobenius_mult(i: str, j: str, c: Fraction) -> Dict[str, Fraction]:
    """Truncated primary product obtained by raising one index.

    The returned table omits the vacuum component.  It is useful for
    local T/W channel arithmetic, but it is not a closed unital Frobenius
    algebra and must not be used as a Teleman input.
    """
    _check_channel(i)
    _check_channel(j)
    _check_nonzero_c(c)
    return {k: propagator(k, c) * C3(i, j, k, c) for k in CHANNELS}


def euler_field_eigenvalue(channel: str) -> Fraction:
    """Eigenvalue of truncated T-multiplication on the primary line."""
    _check_channel(channel)
    return Fraction(2) if channel == "T" else Fraction(3)


def _basis_product(a: str, b: str, c: Fraction) -> Dict[str, Fraction]:
    """Product table on the truncated vacuum/T/W primary span."""
    if a not in BASIS_3D or b not in BASIS_3D:
        raise ValueError(f"Unknown basis label: {a}, {b}")
    if a == "1":
        return {b: Fraction(1)}
    if b == "1":
        return {a: Fraction(1)}
    if a == "T" and b == "T":
        return {"1": c / 2, "T": Fraction(2)}
    if {a, b} == {"T", "W"}:
        return {"W": Fraction(3)}
    return {"1": c / 3, "T": Fraction(2)}


def _clean_vector(vector: Dict[str, Fraction]) -> Dict[str, Fraction]:
    return {key: value for key, value in vector.items() if value != 0}


def _multiply_vectors(
    left: Dict[str, Fraction],
    right: Dict[str, Fraction],
    c: Fraction,
) -> Dict[str, Fraction]:
    total: Dict[str, Fraction] = {}
    for a, coeff_a in left.items():
        for b, coeff_b in right.items():
            for basis, coeff in _basis_product(a, b, c).items():
                total[basis] = total.get(basis, Fraction(0)) + coeff_a * coeff_b * coeff
    return _clean_vector(total)


def product_3d(a: str, b: str, c: Fraction) -> Dict[str, Fraction]:
    """Vacuum/T/W product table induced by the displayed cubic constants."""
    return _basis_product(a, b, c)


def associator_3d(a: str, b: str, d: str, c: Fraction) -> Dict[str, Fraction]:
    """Compute (a*b)*d - a*(b*d) in the truncated vacuum/T/W table."""
    left = _multiply_vectors(_basis_product(a, b, c), {d: Fraction(1)}, c)
    right = _multiply_vectors({a: Fraction(1)}, _basis_product(b, d, c), c)
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, Fraction(0)) - value
    return _clean_vector(result)


def is_truncated_product_associative(c: Fraction) -> bool:
    """Check associativity of the displayed 3D table on basis elements."""
    return all(
        not associator_3d(a, b, d, c)
        for a in BASIS_3D
        for b in BASIS_3D
        for d in BASIS_3D
    )


def frobenius_3d_multiplication_matrix_T(c: Fraction) -> List[List[Fraction]]:
    """Matrix of multiplication by T in the basis (1, T, W)."""
    return [
        [Fraction(0), c / 2, Fraction(0)],
        [Fraction(1), Fraction(2), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(3)],
    ]


def frobenius_3d_metric(c: Fraction) -> List[List[Fraction]]:
    """Diagonal metric diag(1, c/2, c/3) on the vacuum/T/W span."""
    return [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), c / 2, Fraction(0)],
        [Fraction(0), Fraction(0), c / 3],
    ]


def euler_eigenvalues_3d(c: Fraction) -> Tuple[Fraction, Fraction]:
    """Return the W eigenvalue and the quadratic discriminant.

    The characteristic polynomial of multiplication by T is
    (3 - lambda)(lambda^2 - 2 lambda - c/2).  The two remaining
    eigenvalues are 1 +/- sqrt(1 + c/2).
    """
    return (Fraction(3), Fraction(1) + c / 2)


# ============================================================================
# Faber-Pandharipande numbers
# ============================================================================


def faber_pandharipande(g: int) -> Fraction:
    """Faber-Pandharipande lambda_g coefficient, with local fallback."""
    try:
        from hodge_bundle_universality import faber_pandharipande_lambda_g

        return faber_pandharipande_lambda_g(g)
    except ImportError:
        return _lambda_fp(g)


@lru_cache(maxsize=64)
def _bernoulli(n: int) -> Fraction:
    """Exact Bernoulli number B_n."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    total = Fraction(0)
    for k in range(n):
        total += Fraction(comb(n + 1, k)) * _bernoulli(k)
    return -total / Fraction(n + 1)


def _lambda_fp(g: int) -> Fraction:
    """lambda_g^FP = ((2^(2g-1)-1)/2^(2g-1)) * |B_2g|/(2g)!."""
    if g < 1:
        raise ValueError("Faber-Pandharipande lambda_g is defined here for g >= 1.")
    return (
        Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
        * abs(_bernoulli(2 * g))
        / Fraction(factorial(2 * g))
    )


# ============================================================================
# Genus-2 stable graph catalogue
# ============================================================================


@dataclass(frozen=True)
class Genus2Graph:
    """Stable graph metadata for genus 2, n=0."""

    key: str
    name: str
    vertices: Tuple[Tuple[int, int], ...]
    edges: int
    first_betti: int
    aut_order: int

    @property
    def arithmetic_genus(self) -> int:
        return self.first_betti + sum(genus for genus, _ in self.vertices)

    def stable(self) -> bool:
        return all(2 * genus - 2 + valence > 0 for genus, valence in self.vertices)


def genus2_graph_catalogue() -> Tuple[Genus2Graph, ...]:
    """Seven stable graph topologies for Mbar_{2,0}; Gamma_0 is smooth."""
    return (
        Genus2Graph("Gamma_0", "smooth", ((2, 0),), 0, 0, 1),
        Genus2Graph("Gamma_1", "figure-eight", ((1, 2),), 1, 1, 2),
        Genus2Graph("Gamma_2", "banana", ((0, 4),), 2, 2, 8),
        Genus2Graph("Gamma_3", "dumbbell", ((1, 1), (1, 1)), 1, 0, 2),
        Genus2Graph("Gamma_4", "theta", ((0, 3), (0, 3)), 3, 2, 12),
        Genus2Graph("Gamma_5", "lollipop", ((0, 3), (1, 1)), 2, 1, 2),
        Genus2Graph("Gamma_7", "barbell", ((0, 3), (0, 3)), 3, 2, 8),
    )


# ============================================================================
# Vertex normalizations used by the finite boundary engine
# ============================================================================


def vertex_g0_3pt(i: str, j: str, k: str, c: Fraction) -> Fraction:
    """Genus-0 trivalent primary vertex C_ijk."""
    return C3(i, j, k, c)


def vertex_g0_4pt(i: str, j: str, k: str, l: str, c: Fraction) -> Fraction:
    """S-channel genus-0 four-point vertex for the finite graph model."""
    _check_nonzero_c(c)
    return sum(C3(i, j, m, c) * propagator(m, c) * C3(m, k, l, c) for m in CHANNELS)


def vertex_g1_2pt(i: str, j: str, c: Fraction) -> Fraction:
    """Genus-1 two-leg normalization used by the finite boundary model."""
    _check_channel(i)
    _check_channel(j)
    if i != j:
        return Fraction(0)
    return metric(i, c) / 24


def vertex_g1_1pt(i: str, c: Fraction) -> Fraction:
    """Genus-1 one-leg normalization used by the finite boundary model."""
    _check_channel(i)
    return metric(i, c) / 24


# ============================================================================
# Exact boundary graph amplitudes in the finite T/W model
# ============================================================================


def gamma0_amplitude(c: Fraction) -> Dict[str, Optional[Fraction]]:
    """Smooth genus-2 term; not computed by this boundary engine."""
    return {"amplitude": None, "status": "requires full CohFT interior data"}


def gamma1_all_channels(c: Fraction) -> Fraction:
    """Figure-eight boundary amplitude with both T and W channel choices."""
    total = sum(propagator(ch, c) * vertex_g1_2pt(ch, ch, c) for ch in CHANNELS)
    return total / 2


def gamma2_mixed_amplitude(c: Fraction) -> Fraction:
    """Banana mixed amplitude: (1/8)*2*(2/c)*(3/c)*(2c) = 3/c."""
    mixed = 2 * propagator("T", c) * propagator("W", c) * (2 * c)
    return mixed / 8


def gamma2_all_channels(c: Fraction) -> Fraction:
    """Banana amplitude summed over the four T/W edge assignments."""
    total = Fraction(0)
    for ch1 in CHANNELS:
        for ch2 in CHANNELS:
            total += (
                propagator(ch1, c)
                * propagator(ch2, c)
                * vertex_g0_4pt(ch1, ch1, ch2, ch2, c)
            )
    return total / 8


def gamma3_all_channels(c: Fraction) -> Fraction:
    """Dumbbell boundary amplitude."""
    total = Fraction(0)
    for ch in CHANNELS:
        vertex = vertex_g1_1pt(ch, c)
        total += propagator(ch, c) * vertex * vertex
    return total / 2


def gamma4_mixed_amplitude(c: Fraction) -> Fraction:
    """Theta mixed amplitude: only the TWW assignments survive parity."""
    amp_tww = propagator("T", c) * propagator("W", c) ** 2 * C3("T", "W", "W", c) ** 2
    return (3 * amp_tww) / 12


def gamma4_all_channels(c: Fraction) -> Fraction:
    """Theta amplitude summed over all eight T/W edge assignments."""
    total = Fraction(0)
    for ch1 in CHANNELS:
        for ch2 in CHANNELS:
            for ch3 in CHANNELS:
                total += (
                    propagator(ch1, c)
                    * propagator(ch2, c)
                    * propagator(ch3, c)
                    * C3(ch1, ch2, ch3, c) ** 2
                )
    return total / 12


def gamma5_mixed_amplitude(c: Fraction) -> Fraction:
    """Lollipop mixed amplitude under V_{1,1}(T)=kappa_T/24."""
    amp_wt = (
        propagator("W", c)
        * propagator("T", c)
        * C3("W", "W", "T", c)
        * vertex_g1_1pt("T", c)
    )
    return amp_wt / 2


def gamma5_all_channels(c: Fraction) -> Fraction:
    """Lollipop amplitude over the four self-loop/bridge assignments."""
    total = Fraction(0)
    for loop_ch in CHANNELS:
        for bridge_ch in CHANNELS:
            total += (
                propagator(loop_ch, c)
                * propagator(bridge_ch, c)
                * C3(loop_ch, loop_ch, bridge_ch, c)
                * vertex_g1_1pt(bridge_ch, c)
            )
    return total / 2


def barbell_mixed_amplitude(c: Fraction) -> Fraction:
    """Barbell mixed amplitude: (12/c + 12/c + 18/c)/8 = 21/(4c)."""
    return Fraction(21, 4 * c)


def gamma7_all_channels(c: Fraction) -> Fraction:
    """Barbell amplitude over two loop channels and one bridge channel."""
    total = Fraction(0)
    for left_loop in CHANNELS:
        for right_loop in CHANNELS:
            for bridge in CHANNELS:
                total += (
                    propagator(left_loop, c)
                    * propagator(right_loop, c)
                    * propagator(bridge, c)
                    * C3(left_loop, left_loop, bridge, c)
                    * C3(right_loop, right_loop, bridge, c)
                )
    return total / 8


def genus2_boundary_sum(c: Fraction) -> Dict[str, Fraction]:
    """Boundary graph sum in the finite T/W model, excluding Gamma_0."""
    amplitudes = {
        "Gamma_1": gamma1_all_channels(c),
        "Gamma_2": gamma2_all_channels(c),
        "Gamma_3": gamma3_all_channels(c),
        "Gamma_4": gamma4_all_channels(c),
        "Gamma_5": gamma5_all_channels(c),
        "Gamma_7": gamma7_all_channels(c),
    }
    amplitudes["boundary_sum"] = sum(amplitudes.values())
    return amplitudes


def genus2_cross_channel_corrections(c: Fraction) -> Dict[str, Fraction]:
    """Mixed-channel boundary corrections in the finite T/W model."""
    delta2 = gamma2_mixed_amplitude(c)
    delta4 = gamma4_mixed_amplitude(c)
    delta5 = gamma5_mixed_amplitude(c)
    delta7 = barbell_mixed_amplitude(c)
    return {
        "delta_Gamma2_banana": delta2,
        "delta_Gamma4_theta": delta4,
        "delta_Gamma5_mixed": delta5,
        "delta_Gamma7_barbell": delta7,
        "delta_total": delta2 + delta4 + delta5 + delta7,
    }


def delta_F2_rational(c: Fraction) -> Fraction:
    """Finite boundary-model mixed correction delta = (c + 204)/(16c)."""
    return genus2_cross_channel_corrections(c)["delta_total"]


def genus2_cross_channel_banana(c: Fraction) -> Dict[str, object]:
    """Compatibility wrapper with the historical banana/cross-channel keys."""
    corrections = genus2_cross_channel_corrections(c)
    return {
        "delta_banana": corrections["delta_Gamma2_banana"],
        "delta_theta": corrections["delta_Gamma4_theta"],
        "delta_mixed_graph": corrections["delta_Gamma5_mixed"],
        "delta_barbell": corrections["delta_Gamma7_barbell"],
        "delta_cross_channel": corrections["delta_total"],
        "F2_universal": kappa_total(c) * _lambda_fp(2),
        "universality_holds": False,
        "status": "finite boundary correction, not a full CohFT computation",
    }


# ============================================================================
# Sector-additivity check, not a full Teleman proof
# ============================================================================


def genus2_per_channel_sum(c: Fraction) -> Dict[str, Fraction]:
    """Per-channel sector sum kappa_T*lambda_2 + kappa_W*lambda_2."""
    fp2 = faber_pandharipande(2)
    f2_t = kappa_T(c) * fp2
    f2_w = kappa_W(c) * fp2
    return {
        "F2_T": f2_t,
        "F2_W": f2_w,
        "F2_per_channel": f2_t + f2_w,
        "kappa_times_fp2": kappa_total(c) * fp2,
    }


def compute_delta_F2_numerical(c_val: Fraction) -> Dict[str, object]:
    """Check the tautological per-sector formula at genus 2.

    The equality
        kappa_T*lambda_2 + kappa_W*lambda_2 = (kappa_T+kappa_W)*lambda_2
    is a sector additivity identity.  It is useful as a normalization
    check but does not compute the full W3 CohFT graph sum.
    """
    fp2 = _lambda_fp(2)
    f2_t = kappa_T(c_val) * fp2
    f2_w = kappa_W(c_val) * fp2
    f2_sector = f2_t + f2_w
    f2_universal = kappa_total(c_val) * fp2
    return {
        "c": c_val,
        "kappa_T": kappa_T(c_val),
        "kappa_W": kappa_W(c_val),
        "kappa_total": kappa_total(c_val),
        "F2_Virasoro_sector": f2_t,
        "F2_W_sector": f2_w,
        "F2_total": f2_sector,
        "F2_universal": f2_universal,
        "delta_sector_sum": f2_sector - f2_universal,
        "sector_formula_matches_universal": f2_sector == f2_universal,
        "delta_F2": None,
        "universality_holds": None,
        "full_cohft_universality_proved": False,
    }


def teleman_reconstruction_check(c: Fraction) -> Dict[str, object]:
    """Report whether the local data satisfy the Teleman input tests.

    For generic c the displayed vacuum/T/W product is not associative, so
    the truncated primary table is not a Frobenius algebra.  Even at the
    exceptional associative value, this file does not compute the full
    R-matrix/idempotent CohFT data.
    """
    lambda_w, discriminant = euler_eigenvalues_3d(c)
    closed = is_truncated_product_associative(c)
    return {
        "frobenius_closed": closed,
        "teleman_applicable_to_truncation": False,
        "semisimple_euler_test": discriminant != 0,
        "eigenvalues": (lambda_w, f"1 +/- sqrt({discriminant})"),
        "sector_formula_matches_universal": compute_delta_F2_numerical(c)[
            "sector_formula_matches_universal"
        ],
        "match": None,
        "delta_F2": None,
        "open_obligation": "compute full R-matrix/idempotent CohFT graph data",
    }
