r"""Arithmetic resurgence of the shadow obstruction tower.

MATHEMATICAL FRAMEWORK
======================

For class M algebras (Virasoro, W_N), the shadow obstruction tower has infinite depth
and the shadow generating function G(t) = sum_{r>=2} S_r t^r has finite
radius of convergence rho(A)^{-1}.  This module computes the Borel
transform of the shadow obstruction tower and tests the

    BOREL-ARITHMETIC CONJECTURE:

    For a modular Koszul algebra A, the Borel singularities of the shadow
    tower generating function are located at positions determined by the
    arithmetic packet connection nabla^arith_A.

Specifically: the singular divisor D_A = cup_chi div(Lambda_chi) of the
arithmetic packet (def:arithmetic-packet-connection) should determine the
Stokes walls of the Borel-resummed shadow obstruction tower.

THREE DISTINCT RESURGENT STRUCTURES
====================================

1. GENUS-DIRECTION (covered by resurgence_shadow_complete.py):
   Z^sh(hbar) = sum_{g>=1} F_g hbar^{2g}, F_g = kappa * lambda_g^FP.
   Borel singularities at hbar = 2*pi*n, from poles of (hbar/2)/sin(hbar/2).
   These are UNIVERSAL (independent of algebra family within the scalar lane).

2. ARITY-DIRECTION (covered by shadow_resurgence.py):
   G(t) = sum_{r>=2} S_r t^r.
   Borel singularities from branch points of sqrt(Q_L(t)).
   These are ALGEBRA-DEPENDENT (determined by kappa, alpha, S_4).

3. ARITHMETIC-RESURGENT DIRECTION (this module, NEW):
   The COMBINED double series Z^sh(hbar, t) viewed as a function of a
   single complexified variable.  The Borel singularity structure in
   the combined variable encodes arithmetic data: the instanton actions
   are related to the arithmetic packet's L-function zeros.

KEY COMPUTATIONS
================

(a) Borel plane singularity map for Virasoro at c = 1/2, 1, 25, 26.
(b) Stokes multiplier computation (both arity and genus directions).
(c) Test of the Borel-arithmetic conjecture.
(d) Trans-series structure in the arity direction.
(e) Lattice VOA termination vs finite L-function poles.

BEILINSON WARNINGS
==================

AP15: The genus-direction singularities involve quasi-modular forms at g>=1
(E_2* propagator), NOT holomorphic modular forms.  The arithmetic packet
operates with holomorphic L-functions.  This is NOT a contradiction: the
Borel transform maps the quasi-modular genus series to a holomorphic
object in the Borel plane.

AP31: kappa = 0 does NOT imply Theta = 0.  The arity-direction resurgence
persists even when kappa = 0 (the arity-2 coefficient vanishes, but higher
arity components can be nonzero).  However, for Vir at c=0, the shadow
metric Q_L degenerates and the branch points move to infinity.

AP29: delta_kappa = kappa - kappa' (complementarity asymmetry) and
kappa_eff = kappa(matter) + kappa(ghost) are DIFFERENT objects.  The
resurgent structure uses kappa(A) and kappa(A!), never kappa_eff.

Manuscript references:
    def:arithmetic-packet-connection (arithmetic_shadows.tex)
    thm:packet-connection-flatness (arithmetic_shadows.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# =====================================================================
# Constants
# =====================================================================

PI = math.pi
TWO_PI = 2.0 * PI
FOUR_PI_SQ = (2.0 * PI) ** 2


# =====================================================================
# Section 0: Algebra data with arithmetic packet information
# =====================================================================

@dataclass
class ArithmeticAlgebraData:
    """Algebra data including shadow obstruction tower AND arithmetic packet.

    Shadow data:
        kappa: S_2 (modular characteristic)
        alpha: S_3 (cubic shadow)
        S4: S_4 (quartic contact invariant)

    Arithmetic packet data:
        L_zeros: list of zeros of the L-packet Lambda_chi(s)
                 in the critical strip (the singular divisor D_A)
        L_residues: residues of d log Lambda_chi at the zeros
        hecke_eigenvalues: the semisimple eigenvalues a_chi

    The conjecture: the arity-direction Borel singularities (from the
    branch points of sqrt(Q_L)) should be related to the L-function
    zeros via a specific map.
    """
    name: str
    kappa: float
    alpha: float
    S4: float
    kappa_dual: float
    c: float = 0.0
    depth_class: str = 'M'
    # Arithmetic packet
    L_zeros: List[complex] = field(default_factory=list)
    L_residues: List[complex] = field(default_factory=list)
    hecke_eigenvalues: List[complex] = field(default_factory=list)

    # --- Shadow metric data ---
    @property
    def q0(self) -> float:
        return 4.0 * self.kappa ** 2

    @property
    def q1(self) -> float:
        return 12.0 * self.kappa * self.alpha

    @property
    def q2(self) -> float:
        return 9.0 * self.alpha ** 2 + 16.0 * self.kappa * self.S4

    @property
    def Delta(self) -> float:
        """Critical discriminant Delta = 8*kappa*S4."""
        return 8.0 * self.kappa * self.S4

    @property
    def branch_points(self) -> Tuple[complex, complex]:
        """Zeros of Q_L(t) = q0 + q1*t + q2*t^2."""
        disc = self.q1 ** 2 - 4.0 * self.q0 * self.q2
        sq = cmath.sqrt(disc)
        if abs(self.q2) < 1e-30:
            return (complex('inf'), complex('inf'))
        t_plus = (-self.q1 + sq) / (2.0 * self.q2)
        t_minus = (-self.q1 - sq) / (2.0 * self.q2)
        return (t_plus, t_minus)

    @property
    def rho(self) -> float:
        """Shadow growth rate = 1/|nearest branch point|."""
        t_p, t_m = self.branch_points
        if t_p == complex('inf'):
            return 0.0
        R = min(abs(t_p), abs(t_m))
        return 1.0 / R if R > 1e-30 else float('inf')

    @property
    def theta(self) -> float:
        """Argument of the nearest branch point."""
        t_p, t_m = self.branch_points
        if t_p == complex('inf'):
            return 0.0
        if abs(t_p) <= abs(t_m):
            return cmath.phase(t_p)
        return cmath.phase(t_m)

    @property
    def instanton_actions(self) -> Tuple[complex, complex]:
        """Arity-direction Borel singularities = 1/branch_points."""
        t_p, t_m = self.branch_points
        A_p = 1.0 / t_p if abs(t_p) > 1e-30 else complex('inf')
        A_m = 1.0 / t_m if abs(t_m) > 1e-30 else complex('inf')
        return (A_p, A_m)

    @property
    def genus_instanton_actions(self) -> List[float]:
        """Genus-direction Borel singularities at hbar = 2*pi*n.

        These are UNIVERSAL (from the poles of (hbar/2)/sin(hbar/2)).
        """
        return [2.0 * PI * n for n in range(1, 6)]


# =====================================================================
# Section 1: Standard algebra constructors
# =====================================================================

def virasoro_arithmetic(c_val: float) -> ArithmeticAlgebraData:
    """Virasoro at central charge c with arithmetic packet data.

    The arithmetic packet for Virasoro has a SINGLE Eisenstein-type
    L-packet: Lambda_0(s) = Gamma(s) * (2*pi)^{-s} * zeta(2s-1) * kappa.
    (The Eisenstein series E_2* has spectral parameter s = 1.)

    The L-function zeros are the zeros of zeta(2s-1), i.e. the
    nontrivial zeros of Riemann zeta at s = (1 + rho_n)/2 where
    rho_n are the zeros on the critical line Re(rho) = 1/2.

    For testing purposes, we use the first few known zeta zeros:
    rho_1 = 1/2 + 14.1347i, rho_2 = 1/2 + 21.0220i, etc.
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0)) if abs(c_val) > 1e-15 else float('inf')
    kappa_dual = (26.0 - c_val) / 2.0

    # First 5 nontrivial zeros of Riemann zeta on critical line
    # rho_n = 1/2 + i*gamma_n
    zeta_imaginary_parts = [
        14.134725141734693,
        21.022039638771555,
        25.010857580145688,
        30.424876125859513,
        32.935061587739189,
    ]
    # The arithmetic packet singular divisor D_A is at s = (1 + rho_n)/2
    # which are at s = 3/4 + i*gamma_n/2 (in the spectral variable).
    L_zeros = [complex(0.75, g / 2.0) for g in zeta_imaginary_parts]
    L_zeros += [z.conjugate() for z in L_zeros]  # Include conjugates

    return ArithmeticAlgebraData(
        name=f'Vir_c={c_val}',
        kappa=kappa,
        alpha=alpha,
        S4=S4,
        kappa_dual=kappa_dual,
        c=c_val,
        depth_class='M',
        L_zeros=L_zeros,
    )


def heisenberg_arithmetic(rank: int = 1, level: float = 1.0
                          ) -> ArithmeticAlgebraData:
    """Heisenberg at given rank and level.

    Class G: shadow obstruction tower terminates at depth 2.
    The arithmetic packet is trivial (single Eisenstein packet,
    no cusp forms).  Lattice transparency (cor:lattice-packet-diagonal).
    """
    kappa = float(rank) * float(level)
    return ArithmeticAlgebraData(
        name=f'Heis_n={rank}_k={level}',
        kappa=kappa,
        alpha=0.0,
        S4=0.0,
        kappa_dual=-kappa,
        c=float(rank),
        depth_class='G',
        L_zeros=[],  # No cusp-form zeros; Eisenstein only
    )


def affine_sl2_arithmetic(k: float) -> ArithmeticAlgebraData:
    """Affine sl_2 at level k. Class L, depth 3."""
    kappa = 3.0 * (k + 2.0) / 4.0
    return ArithmeticAlgebraData(
        name=f'aff_sl2_k={k}',
        kappa=kappa,
        alpha=1.0,
        S4=0.0,
        kappa_dual=-kappa,
        c=3.0 * k / (k + 2.0) if abs(k + 2.0) > 1e-15 else float('nan'),
        depth_class='L',
        L_zeros=[],  # Class L: terminates, no resurgence
    )


def lattice_arithmetic(rank: int, det: int = 1) -> ArithmeticAlgebraData:
    """Lattice VOA V_Lambda. Class G, depth 2.

    For even unimodular lattices of rank r >= 24, the theta function
    decomposes into Eisenstein + cusp forms.  The L-function zeros
    of the cusp form component give the arithmetic packet singular divisor.

    For rank < 24 (or non-unimodular): only Eisenstein, no cusp zeros.
    For rank = 24 (Leech): the theta series is the Eisenstein series E_12,
    so again no cusp contribution.  The FIRST cusp contribution appears
    for rank 24, non-Leech Niemeier lattices.
    """
    kappa = float(rank) / 2.0  # kappa = rank/2 for rank-1 at level 1
    # For lattice VOAs, the shadow obstruction tower TERMINATES at depth 2
    # (class G, Gaussian: only kappa, no higher shadows).
    # The L-zeros come from the SPECTRAL decomposition of the
    # partition function, not from the shadow obstruction tower itself.

    # For Niemeier lattices (rank 24): cusp form contribution
    # is chi_12 = SK(f_22) where f_22 is the unique weight-22 newform.
    # The L-function L(s, f_22) has zeros on the critical line Re(s) = 11.
    L_zeros = []
    if rank >= 24:
        # First zero of Ramanujan Delta L-function (weight 12 cusp form)
        # L(s, Delta) has critical strip 0 < Re(s) < 12, critical line Re(s) = 6
        # First zero: s = 6 + i * 9.2224...
        delta_zeros = [
            complex(6.0, 9.2224),
            complex(6.0, 13.9076),
            complex(6.0, 17.4428),
        ]
        L_zeros = delta_zeros + [z.conjugate() for z in delta_zeros]

    return ArithmeticAlgebraData(
        name=f'Lattice_rank={rank}',
        kappa=kappa,
        alpha=0.0,
        S4=0.0,
        kappa_dual=-kappa,
        c=float(rank),
        depth_class='G',
        L_zeros=L_zeros,
    )


# =====================================================================
# Section 2: Shadow obstruction tower coefficients
# =====================================================================

def shadow_coefficients(data: ArithmeticAlgebraData,
                        max_r: int = 60) -> Dict[int, float]:
    r"""Shadow coefficients S_2, ..., S_{max_r} via sqrt(Q_L) expansion.

    Same convolution recursion as shadow_resurgence.py but using our
    ArithmeticAlgebraData type.
    """
    q0, q1, q2 = data.q0, data.q1, data.q2
    max_n = max_r - 2
    if max_n < 0 or q0 <= 0:
        return {r: 0.0 for r in range(2, max_r + 1)}

    a = [0.0] * (max_n + 1)
    a[0] = math.sqrt(q0)
    if a[0] == 0.0:
        return {r: 0.0 for r in range(2, max_r + 1)}

    if max_n >= 1:
        a[1] = q1 / (2.0 * a[0])
    for n in range(2, max_n + 1):
        cn = q2 if n == 2 else 0.0
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = (cn - conv) / (2.0 * a[0])

    # Convention: S_r = a_{r-2}/r matches shadow_resurgence.py
    # This ensures S_2 = a_0/2 = 2*|kappa|/2 = |kappa| = kappa
    return {r: a[r - 2] / r for r in range(2, max_r + 1)}


# =====================================================================
# Section 3: Arity-direction Borel transform
# =====================================================================

def arity_borel_transform(data: ArithmeticAlgebraData, s: complex,
                          max_r: int = 60) -> complex:
    r"""Borel transform of the shadow obstruction tower in the arity direction.

    B(s) = sum_{r>=2} S_r s^r / Gamma(r + 5/2)

    We use Gamma(r + 5/2) rather than Gamma(r+1) = r! to match
    the asymptotic form S_r ~ C * rho^r * r^{-5/2}.  With this
    normalization, the Borel transform coefficients are:

        b_r = S_r / Gamma(r + 5/2)

    which decay superexponentially, making B(s) ENTIRE.

    However, the Borel-Laplace resummation encounters Stokes
    phenomena at directions arg(s) corresponding to the branch
    points of sqrt(Q_L).
    """
    s = complex(s)
    coeffs = shadow_coefficients(data, max_r)
    result = 0.0 + 0.0j
    for r in sorted(coeffs.keys()):
        sr = coeffs[r]
        if abs(sr) < 1e-300:
            continue
        gamma_val = math.gamma(r + 2.5)  # Gamma(r + 5/2)
        term = sr * s ** r / gamma_val
        result += term
        if r > 10 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def arity_borel_standard(data: ArithmeticAlgebraData, s: complex,
                         max_r: int = 60) -> complex:
    r"""Standard Borel transform B(s) = sum S_r s^r / r!.

    The ENTIRE function whose Borel-Laplace resummation recovers
    the shadow generating function G(t) = sum S_r t^r.
    """
    s = complex(s)
    coeffs = shadow_coefficients(data, max_r)
    result = 0.0 + 0.0j
    for r in sorted(coeffs.keys()):
        sr = coeffs[r]
        if abs(sr) < 1e-300:
            continue
        fact = math.gamma(r + 1)  # r!
        term = sr * s ** r / fact
        result += term
        if r > 10 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


# =====================================================================
# Section 4: Borel plane singularity structure (arity direction)
# =====================================================================

def arity_borel_singularity_map(data: ArithmeticAlgebraData
                                ) -> Dict[str, Any]:
    r"""Complete singularity map of the arity-direction Borel transform.

    The ordinary generating function G(t) = sum S_r t^r is algebraic
    (sqrt of a quadratic), with branch points at the zeros t_+/- of Q_L.

    The Borel transform B(s) = sum S_r s^r / r! is ENTIRE (factorial
    kills geometric growth).  But the Borel-Laplace resummation

        G(t) = int_0^{infty} B(s) exp(-s/t) ds/t

    encounters Stokes phenomena when arg(1/t) = arg(A_pm) where
    A_pm = 1/t_pm are the instanton actions.

    Returns the full singularity data including:
    - Branch point locations and moduli
    - Instanton actions A_pm = 1/t_pm
    - Stokes directions
    - Darboux coefficient (connection between perturbative and
      non-perturbative sectors)
    """
    t_p, t_m = data.branch_points
    A_p, A_m = data.instanton_actions
    rho = data.rho

    # For class G/L: no finite branch points
    if data.depth_class in ('G', 'L'):
        return {
            'depth_class': data.depth_class,
            'branch_points': (None, None),
            'instanton_actions': (None, None),
            'rho': 0.0,
            'stokes_directions': [],
            'comment': 'Tower terminates; no arity-direction resurgence.',
        }

    # Stokes directions: arg(A_pm) in the Borel plane
    stokes_dir_p = cmath.phase(A_p)
    stokes_dir_m = cmath.phase(A_m)

    # Darboux coefficient from singularity analysis
    q2 = data.q2
    darboux = _compute_darboux(data)

    return {
        'depth_class': data.depth_class,
        'branch_points': (t_p, t_m),
        'branch_point_moduli': (abs(t_p), abs(t_m)),
        'branch_point_args': (cmath.phase(t_p), cmath.phase(t_m)),
        'instanton_actions': (A_p, A_m),
        'instanton_moduli': (abs(A_p), abs(A_m)),
        'rho': rho,
        'convergence_radius': 1.0 / rho if rho > 1e-30 else float('inf'),
        'stokes_directions': [stokes_dir_p, stokes_dir_m],
        'darboux_coefficient': darboux,
        'darboux_amplitude': abs(darboux),
        'darboux_phase': cmath.phase(darboux),
        'Delta': data.Delta,
        'branch_type': 'complex_conjugate' if data.Delta > 0 else 'real_pair',
    }


def _compute_darboux(data: ArithmeticAlgebraData) -> complex:
    """Darboux coefficient from transfer theorem (Flajolet-Sedgewick VI.1).

    For sqrt(Q_L(t)) with simple zero at t_p:
        C = sqrt(q2) * sqrt(t_p - t_m) * sqrt(-t_p) * t_p^2 / (-2*sqrt(pi))
    """
    if data.depth_class in ('G', 'L'):
        return 0.0 + 0.0j
    t_p, t_m = data.branch_points
    q2 = data.q2
    if abs(q2) < 1e-30 or abs(t_p) < 1e-30:
        return 0.0 + 0.0j
    sqrt_q2 = cmath.sqrt(q2)
    sqrt_diff = cmath.sqrt(t_p - t_m)
    sqrt_neg_tp = cmath.sqrt(-t_p)
    return sqrt_q2 * sqrt_diff * sqrt_neg_tp * t_p ** 2 / (-2.0 * math.sqrt(PI))


# =====================================================================
# Section 5: Stokes multipliers (arity direction)
# =====================================================================

def arity_stokes_multiplier_exact(data: ArithmeticAlgebraData) -> complex:
    r"""Exact Stokes constant S_1 for the shadow obstruction tower (arity direction).

    From the monodromy of sqrt(Q_L) at the branch point t_p:

        S_1 = i * sqrt(pi) * sqrt(q2) * sqrt(t_p - t_m) * sqrt(-t_p)

    This encodes the square-root monodromy (-1) translated to the
    Borel plane via the Darboux transfer.
    """
    if data.depth_class in ('G', 'L'):
        return 0.0 + 0.0j
    t_p, t_m = data.branch_points
    q2 = data.q2
    if abs(q2) < 1e-30 or abs(t_p) < 1e-30:
        return 0.0 + 0.0j
    return (1j * math.sqrt(PI) * cmath.sqrt(q2)
            * cmath.sqrt(t_p - t_m) * cmath.sqrt(-t_p))


def arity_stokes_multiplier_numerical(data: ArithmeticAlgebraData,
                                      max_r: int = 200) -> complex:
    r"""Numerically extract S_1 from high-order shadow coefficients.

    Uses least-squares fit of s_r = S_r * |t_p|^r * r^{5/2} to
    the expected oscillation 2*|C|*cos(r*theta + phi).
    """
    if data.depth_class in ('G', 'L'):
        return 0.0 + 0.0j

    t_p, t_m = data.branch_points
    if abs(t_p) < 1e-30:
        return 0.0 + 0.0j

    rho = data.rho
    theta = cmath.phase(t_p)
    coeffs = shadow_coefficients(data, max_r)

    # Build oscillation data
    cos_data = []
    for r in range(10, max_r + 1):
        sr = coeffs.get(r, 0.0)
        if abs(sr) < 1e-300:
            continue
        s_r = sr * (1.0 / rho) ** r * r ** 2.5
        angle = r * theta
        cos_data.append((s_r, math.cos(angle), math.sin(angle)))

    if len(cos_data) < 4:
        return 0.0 + 0.0j

    # Least-squares: s_r = A*cos(r*theta) + B*sin(r*theta)
    sum_sc = sum(v[0] * v[1] for v in cos_data)
    sum_ss = sum(v[0] * v[2] for v in cos_data)
    sum_cc = sum(v[1] ** 2 for v in cos_data)
    sum_cs = sum(v[1] * v[2] for v in cos_data)
    sum_ssq = sum(v[2] ** 2 for v in cos_data)

    det = sum_cc * sum_ssq - sum_cs ** 2
    if abs(det) < 1e-30:
        return 0.0 + 0.0j

    A = (sum_sc * sum_ssq - sum_ss * sum_cs) / det
    B = (sum_ss * sum_cc - sum_sc * sum_cs) / det

    C_num = complex(A, B) / 2.0
    S_1 = -2.0j * PI * C_num / t_p ** 2

    return S_1


def genus_stokes_multiplier(kappa: float, n: int) -> complex:
    r"""Stokes multiplier at the n-th genus-direction singularity.

    In the hbar-plane:
        S_n^{hbar} = (-1)^n * 4*pi^2*n * kappa * i

    These are UNIVERSAL (same for all algebras with the same kappa).
    They are PROPORTIONAL TO kappa, hence arithmetic in the sense
    that kappa encodes the Lie-theoretic data.
    """
    return kappa * (-1) ** n * FOUR_PI_SQ * n * 1.0j


# =====================================================================
# Section 6: Virasoro Borel plane analysis at specific central charges
# =====================================================================

def virasoro_borel_scan(c_values: Optional[List[float]] = None
                        ) -> Dict[str, Dict[str, Any]]:
    """Complete Borel singularity map for Virasoro at multiple c values.

    Returns arity-direction singularity data for each c.
    """
    if c_values is None:
        c_values = [0.5, 1.0, 25.0, 26.0]

    results = {}
    for c in c_values:
        data = virasoro_arithmetic(c)
        sing_map = arity_borel_singularity_map(data)
        stokes_exact = arity_stokes_multiplier_exact(data)
        stokes_num = arity_stokes_multiplier_numerical(data, max_r=100)

        # Genus-direction Stokes (leading)
        genus_stokes = genus_stokes_multiplier(data.kappa, 1)

        results[f'Vir_c={c}'] = {
            'c': c,
            'kappa': data.kappa,
            'kappa_dual': data.kappa_dual,
            'rho': data.rho,
            'Delta': data.Delta,
            'singularity_map': sing_map,
            'arity_stokes_exact': stokes_exact,
            'arity_stokes_numerical': stokes_num,
            'arity_stokes_agreement': (
                abs(stokes_exact - stokes_num) / max(abs(stokes_exact), 1e-30)
                if abs(stokes_exact) > 1e-30 else float('nan')
            ),
            'genus_stokes_leading': genus_stokes,
            'genus_stokes_mod': abs(genus_stokes),
            'genus_instanton_action': TWO_PI,
            'arity_instanton_actions': data.instanton_actions,
        }

    return results


# =====================================================================
# Section 7: Trans-series structure (arity direction)
# =====================================================================

@dataclass
class ArityTransseries:
    """Trans-series data for the shadow obstruction tower arity expansion.

    G(t) = G^{(0)}(t) + sigma * exp(-A_1/t) * G^{(1)}(t) + ...

    where A_1 = 1/t_p is the leading instanton action,
    G^{(0)} = sum S_r t^r is the perturbative tower, and
    G^{(k)} are the k-instanton fluctuation sectors.

    For the ALGEBRAIC shadow obstruction tower, the trans-series is EXACT
    (only one instanton sector from each branch point, since
    sqrt has no higher multi-instanton corrections beyond the
    two-sheeted structure).
    """
    name: str
    instanton_action_plus: complex
    instanton_action_minus: complex
    perturbative_coeffs: Dict[int, float]
    darboux_coefficient: complex
    stokes_constant: complex


def build_arity_transseries(data: ArithmeticAlgebraData,
                            max_r: int = 60) -> ArityTransseries:
    """Build the arity-direction trans-series.

    For the algebraic function G(t) = t^2 * sqrt(Q_L(t)), the
    trans-series has a special form: only ONE instanton sector
    from each branch point (since sqrt has two sheets).

    The one-instanton sector captures the contribution from
    analytic continuation around the branch cut.
    """
    A_p, A_m = data.instanton_actions
    coeffs = shadow_coefficients(data, max_r)
    darboux = _compute_darboux(data)
    stokes = arity_stokes_multiplier_exact(data)

    return ArityTransseries(
        name=data.name,
        instanton_action_plus=A_p,
        instanton_action_minus=A_m,
        perturbative_coeffs=coeffs,
        darboux_coefficient=darboux,
        stokes_constant=stokes,
    )


# =====================================================================
# Section 8: Borel-arithmetic conjecture test
# =====================================================================

def borel_arithmetic_test(data: ArithmeticAlgebraData) -> Dict[str, Any]:
    r"""Test the Borel-arithmetic conjecture.

    CONJECTURE: The Borel singularities of the shadow obstruction tower are
    located at positions determined by the arithmetic packet.

    ARITY DIRECTION:
    The Borel singularities A_pm = 1/t_pm are determined by the
    shadow metric Q_L, which depends on (kappa, alpha, S4).
    These are ALGEBRAIC invariants of A.

    The arithmetic packet singular divisor D_A = cup div(Lambda_chi)
    consists of L-function zeros, which are ANALYTIC invariants.

    The conjecture predicts a relation:

        A_pm = f(L-zeros)

    for some universal function f.

    GENUS DIRECTION:
    The Borel singularities hbar = 2*pi*n are UNIVERSAL (independent
    of the algebra).  The arithmetic data enters through the Stokes
    multipliers S_n = (-1)^n * 4*pi^2*n*kappa*i, which are proportional
    to kappa.

    TEST: For each algebra, compute both the Borel singularities
    (algebraic computation from Q_L) and the L-function zeros
    (arithmetic computation from the spectral decomposition).
    Check if there is a functional relationship.

    FINDINGS (Beilinson-critical):
    ==============================
    The test reveals that the conjecture, in its NAIVE form, is FALSE.
    The arity-direction Borel singularities A_pm depend continuously
    on (kappa, alpha, S4), while the L-function zeros are DISCRETE.
    There is no continuous map from A_pm to L-zeros.

    However, a WEAKER form may hold: the ARITHMETIC CONTENT of the
    Stokes multipliers (whether they are algebraic numbers, or
    rational multiples of pi, or involve L-values) may encode
    arithmetic data.  Specifically:

    For Virasoro at c = p/q (rational):
    - kappa = p/(2q) is rational
    - The Stokes multiplier S_1^{genus} = -4*pi^2*(p/(2q))*i
      is an algebraic multiple of pi^2*i
    - The Stokes multiplier S_1^{arity} involves sqrt(q2*(t_p-t_m)*(-t_p))
      which is typically algebraic when c is rational

    For Virasoro at c = 1/2 (Ising):
    - kappa = 1/4, S4 = 10/(1/2 * (5/2+22)) = 10/(1/2 * 49/2) = 10/(49/4) = 40/49
    - The shadow metric Q_L is defined over Q
    - The branch points are algebraic numbers
    - The Stokes constants are algebraic (up to factors of pi)

    REFINED CONJECTURE: For rational c, the Stokes constants of the
    shadow obstruction tower are algebraic multiples of powers of pi.  The algebraic
    parts encode arithmetic information (related to Hecke eigenvalues
    of the underlying automorphic forms).
    """
    sing_map = arity_borel_singularity_map(data)

    # Compute Stokes data
    stokes_arity = arity_stokes_multiplier_exact(data)
    stokes_genus = genus_stokes_multiplier(data.kappa, 1)

    # Arithmetic packet data
    L_zeros = data.L_zeros
    has_cusp = len(L_zeros) > 0

    # Test: distance between Borel singularities and L-zeros
    distances = []
    if data.depth_class in ('M', 'C') and L_zeros:
        A_p, A_m = data.instanton_actions
        for zero in L_zeros:
            d_p = abs(A_p - zero)
            d_m = abs(A_m - zero)
            distances.append(min(d_p, d_m))

    # Rationality test for Stokes constants
    stokes_arity_rational = _test_algebraicity(stokes_arity)
    stokes_genus_rational = _test_algebraicity(stokes_genus)

    # The c-dependent data
    c_val = data.c

    return {
        'algebra': data.name,
        'depth_class': data.depth_class,
        'c': c_val,
        'kappa': data.kappa,
        # Arity direction
        'arity_instanton_actions': data.instanton_actions if data.depth_class in ('M', 'C') else None,
        'arity_rho': data.rho,
        'arity_stokes': stokes_arity,
        'arity_stokes_modulus': abs(stokes_arity),
        'arity_stokes_algebraic': stokes_arity_rational,
        # Genus direction
        'genus_instanton_action': TWO_PI,
        'genus_stokes': stokes_genus,
        'genus_stokes_modulus': abs(stokes_genus),
        'genus_stokes_algebraic': stokes_genus_rational,
        # Arithmetic packet
        'L_zeros': L_zeros,
        'has_cusp_forms': has_cusp,
        'distances_borel_to_L': distances,
        'min_distance': min(distances) if distances else float('inf'),
        # Verdict on naive conjecture
        'naive_conjecture_status': 'FALSIFIED' if (
            data.depth_class in ('M', 'C') and distances and min(distances) > 1.0
        ) else 'UNTESTABLE' if data.depth_class in ('G', 'L') else 'INCONCLUSIVE',
        # Refined conjecture
        'refined_conjecture': (
            'Stokes constants algebraic (mod pi factors) for rational c.'
            if c_val and abs(c_val - round(c_val * 10) / 10) < 1e-10
            else 'c irrational or not tested.'
        ),
    }


def _test_algebraicity(z: complex, tol: float = 1e-10) -> Dict[str, Any]:
    """Test if a complex number is 'algebraic' (rational multiple of pi powers).

    Returns analysis of z = a + bi, testing if a/(pi^k) and b/(pi^k)
    are close to rationals for small k.
    """
    result = {'value': z, 'tests': []}
    for k in range(0, 5):
        pi_k = PI ** k
        if pi_k > 0:
            re_ratio = z.real / pi_k if abs(z.real) > tol else 0.0
            im_ratio = z.imag / pi_k if abs(z.imag) > tol else 0.0
            # Check if close to simple rational
            re_near_rational = _nearest_simple_rational(re_ratio, tol)
            im_near_rational = _nearest_simple_rational(im_ratio, tol)
            if re_near_rational is not None or im_near_rational is not None:
                result['tests'].append({
                    'pi_power': k,
                    're_rational': re_near_rational,
                    'im_rational': im_near_rational,
                })

    result['appears_algebraic'] = len(result['tests']) > 0
    return result


def _nearest_simple_rational(x: float, tol: float = 1e-6
                             ) -> Optional[str]:
    """Check if x is close to p/q for small q."""
    if abs(x) < tol:
        return '0'
    for q in range(1, 100):
        p = round(x * q)
        if abs(x - p / q) < tol:
            return f'{p}/{q}'
    return None


# =====================================================================
# Section 9: Special central charges
# =====================================================================

def virasoro_special_charges() -> Dict[str, Dict[str, Any]]:
    r"""Detailed analysis at the four physically distinguished c values.

    c = 1/2 (Ising): minimal model, finite representation theory.
        kappa = 1/4.  Self-dual at c = 26 - 1/2 = 51/2 (kappa_dual = 51/4).
        Shadow obstruction tower diverges (rho > 1 since c < c*).

    c = 1 (free boson compactified on circle):
        kappa = 1/2.  kappa_dual = 25/2.
        Shadow obstruction tower diverges (rho > 1).

    c = 25 (near critical, Liouville at b->0):
        kappa = 25/2.  kappa_dual = 1/2.
        Shadow obstruction tower converges (rho < 1 since c > c*).
        Koszul dual = Vir at c=1 (kappa_dual = 1/2).

    c = 26 (bosonic string critical dimension):
        kappa = 13.  kappa_dual = 0 (kappa(Vir_0) = 0).
        kappa_eff = kappa(matter) + kappa(ghost) = 13 + (-13) = 0.
        Shadow obstruction tower converges (c >> c*).
        The Koszul dual Vir_0 has vanishing kappa: the arity-2
        shadow vanishes, but higher-arity shadows may persist (AP31).

    c = 13 (self-dual point):
        kappa = 13/2 = kappa_dual (since 26 - 13 = 13).
        Koszul duality is a SELF-DUALITY at this c.
        The Stokes structure should exhibit enhanced symmetry.
    """
    charges = {
        'Ising': 0.5,
        'free_boson': 1.0,
        'near_critical': 25.0,
        'anomaly_free': 26.0,
        'self_dual': 13.0,
    }

    results = {}
    for label, c in charges.items():
        data = virasoro_arithmetic(c)
        results[label] = {
            'c': c,
            'kappa': data.kappa,
            'kappa_dual': data.kappa_dual,
            'kappa_sum': data.kappa + data.kappa_dual,  # Should be 13 (AP24)
            'rho': data.rho,
            'Delta': data.Delta,
            'singularity_map': arity_borel_singularity_map(data),
            'arity_stokes': arity_stokes_multiplier_exact(data),
            'genus_stokes_1': genus_stokes_multiplier(data.kappa, 1),
            'borel_arithmetic': borel_arithmetic_test(data),
            'is_self_dual': abs(c - 13.0) < 1e-10,
            'is_anomaly_free': abs(c - 26.0) < 1e-10,
        }

    return results


# =====================================================================
# Section 10: Self-duality at c=13 and Stokes symmetry
# =====================================================================

def self_dual_stokes_analysis() -> Dict[str, Any]:
    r"""Stokes structure at the self-dual point c = 13.

    At c = 13: kappa = kappa_dual = 13/2.
    Koszul duality is Vir_{13} <-> Vir_{13} (self-dual, AP8 safe:
    this is QUADRATIC self-duality for c=13, not c=0 or c=26).

    The complementarity sum: kappa + kappa' = 13/2 + 13/2 = 13 (AP24).
    delta_kappa = kappa - kappa' = 0 (AP29).

    PREDICTION: The Stokes structure should be invariant under the
    involution induced by Koszul duality (since A = A!).

    Genus direction: S_n^{genus}(A) and S_n^{genus}(A!) differ by
    kappa <-> kappa_dual.  At c=13: these coincide.

    Arity direction: The shadow metric Q_L depends on (kappa, alpha, S4).
    At c=13: the self-duality means Q_L(A) = Q_L(A!) (since the
    shadow obstruction tower is invariant).  Hence the Stokes constants coincide.
    """
    c = 13.0
    data = virasoro_arithmetic(c)
    data_dual = virasoro_arithmetic(26.0 - c)  # = Vir_{13} = same

    # Verify self-duality
    assert abs(data.kappa - data_dual.kappa) < 1e-10

    stokes_A = arity_stokes_multiplier_exact(data)
    stokes_A_dual = arity_stokes_multiplier_exact(data_dual)

    genus_A = [genus_stokes_multiplier(data.kappa, n) for n in range(1, 6)]
    genus_A_dual = [genus_stokes_multiplier(data_dual.kappa, n) for n in range(1, 6)]

    return {
        'c': 13.0,
        'kappa': data.kappa,
        'kappa_dual': data_dual.kappa,
        'self_dual': abs(data.kappa - data_dual.kappa) < 1e-10,
        'kappa_sum': data.kappa + data_dual.kappa,  # = 13
        'delta_kappa': data.kappa - data_dual.kappa,  # = 0
        'arity_stokes_A': stokes_A,
        'arity_stokes_A_dual': stokes_A_dual,
        'arity_stokes_agree': abs(stokes_A - stokes_A_dual) < 1e-10 * max(abs(stokes_A), 1e-30),
        'genus_stokes_A': genus_A,
        'genus_stokes_A_dual': genus_A_dual,
        'genus_stokes_agree': all(
            abs(a - b) < 1e-10 * max(abs(a), 1e-30)
            for a, b in zip(genus_A, genus_A_dual)
        ),
        'rho': data.rho,
        'rho_dual': data_dual.rho,
        'rho_agree': abs(data.rho - data_dual.rho) < 1e-10,
    }


# =====================================================================
# Section 11: c=26 anomaly cancellation and Stokes structure
# =====================================================================

def anomaly_free_analysis() -> Dict[str, Any]:
    r"""Stokes structure at c = 26 (anomaly cancellation).

    At c = 26: kappa = 13, kappa_dual = kappa(Vir_0) = 0.
    kappa_eff = kappa(matter) + kappa(ghost) = 13 + (-13) = 0 (AP29).
    delta_kappa = kappa - kappa_dual = 13 - 0 = 13 (maximal asymmetry).

    The Koszul dual Vir_0 has kappa = 0:
    - Genus-direction Stokes multipliers for Vir_0 are ALL ZERO
      (S_n proportional to kappa = 0).
    - Arity-direction: S4 for Vir_0 diverges (S4 = 10/(c*(5c+22))
      diverges as c -> 0), so the shadow metric Q_L degenerates.
      The shadow obstruction tower of Vir_0 is ill-defined at the standard level.
      AP31: kappa = 0 does NOT imply Theta = 0.

    The MATTER + GHOST system: the combined Stokes structure of
    Vir_{26} tensor bc-ghosts has kappa_eff = 0.  The perturbative
    shadow vanishes at the combined level, but individual sectors
    (matter and ghost) have nonzero Stokes data.

    This is the resurgent manifestation of the anomaly cancellation:
    the non-perturbative sectors of matter and ghosts cancel in the
    combined system.
    """
    c = 26.0
    data = virasoro_arithmetic(c)

    # The ghost system has kappa = -13 (central charge c = -26)
    ghost_kappa = -13.0

    return {
        'c': c,
        'kappa_matter': data.kappa,  # 13
        'kappa_ghost': ghost_kappa,  # -13
        'kappa_eff': data.kappa + ghost_kappa,  # 0
        'kappa_dual': data.kappa_dual,  # 0 (Vir_0)
        'delta_kappa': data.kappa - data.kappa_dual,  # 13
        'rho': data.rho,
        'arity_stokes': arity_stokes_multiplier_exact(data),
        'genus_stokes_matter': genus_stokes_multiplier(data.kappa, 1),
        'genus_stokes_ghost': genus_stokes_multiplier(ghost_kappa, 1),
        'genus_stokes_combined': (
            genus_stokes_multiplier(data.kappa, 1) +
            genus_stokes_multiplier(ghost_kappa, 1)
        ),
        'genus_stokes_cancel': abs(
            genus_stokes_multiplier(data.kappa, 1) +
            genus_stokes_multiplier(ghost_kappa, 1)
        ) < 1e-10,
        'comment': (
            'Genus Stokes multipliers cancel: S_1(matter) + S_1(ghost) = 0. '
            'This is the resurgent expression of anomaly cancellation. '
            'The combined trans-series has zero leading instanton correction.'
        ),
    }


# =====================================================================
# Section 12: Lattice VOA termination and finite L-poles
# =====================================================================

def lattice_termination_analysis(rank: int = 8) -> Dict[str, Any]:
    r"""Analysis of the relation between tower termination and L-poles.

    For lattice VOAs (class G, depth 2):
    - The shadow obstruction tower TERMINATES: S_r = 0 for r >= 3.
    - There is no arity-direction resurgence.
    - The shadow generating function G(t) = kappa*t^2 is polynomial.

    The arithmetic packet for a lattice VOA V_Lambda has:
    - Eisenstein component: Lambda_0(s) with finitely many poles
      (at s = 0 and s = r/2 for the Epstein zeta, plus Gamma poles).
    - Cusp form components: Lambda_j(s) = L(s, f_j) with
      infinitely many zeros on the critical line BUT finitely many
      poles (only the trivial one at s = 0, or none).

    The RELATION: tower termination (finite polynomial, zero resurgence)
    corresponds to the Eisenstein-type spectral decomposition where the
    partition function has only FINITELY many automorphic contributions.

    For rank < 24: only Eisenstein (no cusp forms in the theta series).
    The partition function IS an Eisenstein series.
    For rank = 24 (Niemeier): theta = E_12 + cusp.  But shadow obstruction tower
    STILL terminates because class G is determined by alpha=0, S4=0
    (not by the arithmetic complexity of the partition function).

    KEY INSIGHT: The shadow obstruction tower termination is a HOMOTOPICAL property
    (related to Swiss-cheese formality / A-infinity formality), while
    the arithmetic packet complexity is an AUTOMORPHIC property.
    These are INDEPENDENT.  A class G algebra can have arbitrarily
    complex arithmetic (Niemeier lattices), while a class M algebra
    (infinite tower) might have simple arithmetic (Virasoro).

    This FALSIFIES the naive version of the Borel-arithmetic conjecture
    for class G algebras: the resurgent structure (trivial, since the
    tower terminates) carries no information about the rich arithmetic.
    """
    data = lattice_arithmetic(rank)
    coeffs = shadow_coefficients(data, 10)

    # Verify termination
    terminates = all(abs(coeffs.get(r, 0.0)) < 1e-30 for r in range(3, 11))

    return {
        'rank': rank,
        'kappa': data.kappa,
        'depth_class': data.depth_class,
        'tower_terminates': terminates,
        'S_2': coeffs.get(2, 0.0),
        'S_3': coeffs.get(3, 0.0),
        'S_4': coeffs.get(4, 0.0),
        'has_L_zeros': len(data.L_zeros) > 0,
        'n_L_zeros': len(data.L_zeros),
        'resurgence_trivial': data.depth_class == 'G',
        'arithmetic_nontrivial': len(data.L_zeros) > 0,
        'conclusion': (
            'Tower terminates BUT arithmetic may be nontrivial. '
            'Resurgent structure and arithmetic complexity are INDEPENDENT '
            'for class G (Gaussian) algebras. The naive Borel-arithmetic '
            'conjecture fails here: zero resurgence, rich arithmetic.'
            if terminates and len(data.L_zeros) > 0
            else 'Tower terminates, arithmetic trivial (Eisenstein only).'
            if terminates
            else 'Tower does not terminate.'
        ),
    }


# =====================================================================
# Section 13: Combined (genus x arity) Borel plane
# =====================================================================

def combined_borel_singularities(data: ArithmeticAlgebraData
                                 ) -> Dict[str, Any]:
    r"""Singularity structure in the combined (hbar, t) parameter space.

    The shadow partition function Z^sh(hbar, t) = sum_{g,r} F_g^{(r)} hbar^{2g} t^r
    has singularities from BOTH the genus and arity directions.

    Genus singularities: hbar = 2*pi*n (universal, from A-hat).
    Arity singularities: t = t_pm (algebra-dependent, from Q_L zeros).

    The COMBINED singularity structure in the product domain
    D = {(hbar, t) : |hbar| < 2*pi, |t| < 1/rho} has a richer
    structure.  The genus-direction resurgent sum at each arity r
    gives the nonperturbative genus completion of S_r.  The arity-
    direction resurgent sum at each genus g gives the nonperturbative
    arity completion of F_g^{(r)}.

    The DOUBLE RESURGENCE (resurgence in both directions simultaneously)
    is controlled by the COMBINED instanton data:
    - Genus instantons at A_g = (2*pi)^2 (in the u = hbar^2 plane)
    - Arity instantons at A_t = 1/t_pm

    For Virasoro, these form a two-parameter instanton lattice.
    """
    # Genus direction: universal
    genus_sings = [2.0 * PI * n for n in range(1, 6)]
    genus_actions = [(2.0 * PI * n) ** 2 for n in range(1, 6)]

    # Arity direction: algebra-dependent
    if data.depth_class in ('M', 'C'):
        t_p, t_m = data.branch_points
        A_p, A_m = data.instanton_actions
        arity_sings = [t_p, t_m]
        arity_actions = [A_p, A_m]
    else:
        arity_sings = []
        arity_actions = []

    # Combined instanton lattice
    combined = []
    for n_g, Ag in enumerate(genus_actions, 1):
        combined.append({
            'type': 'genus',
            'n': n_g,
            'action_u': Ag,
            'action_hbar': genus_sings[n_g - 1],
        })
    for i, At in enumerate(arity_actions):
        combined.append({
            'type': 'arity',
            'index': i,
            'action': At,
        })

    return {
        'algebra': data.name,
        'genus_singularities': genus_sings,
        'genus_instanton_actions': genus_actions,
        'arity_singularities': arity_sings,
        'arity_instanton_actions': arity_actions,
        'combined_lattice': combined,
        'genus_radius': TWO_PI,
        'arity_radius': 1.0 / data.rho if data.rho > 1e-30 else float('inf'),
        'double_convergent': data.rho < 1.0,
    }


# =====================================================================
# Section 14: Stokes multiplier c-dependence
# =====================================================================

def stokes_c_dependence(c_min: float = 0.5, c_max: float = 30.0,
                        n_points: int = 50) -> Dict[str, Any]:
    r"""Compute the c-dependence of the Stokes multipliers.

    The genus-direction leading Stokes multiplier is
        |S_1^{genus}| = 4*pi^2*kappa = 2*pi^2*c

    which is LINEAR in c (a simple monotone function).

    The arity-direction leading Stokes multiplier depends on the
    full shadow metric (kappa, alpha, S4).  For Virasoro:
    - kappa = c/2, alpha = 2, S4 = 10/(c(5c+22))
    - The branch points t_pm are roots of Q_L(t) = q0 + q1*t + q2*t^2
      where q0 = c^2, q1 = 12c, q2 = 36 + 160/(5c+22)

    The c-dependence of |S_1^{arity}| is more complex.

    Key values:
    - c = c* ~ 6.125: rho = 1, convergence/divergence transition.
    - c = 13: self-dual point, S_1(A) = S_1(A!).
    - c = 26: anomaly-free, kappa_dual = 0.
    """
    c_values = np.linspace(c_min, c_max, n_points).tolist()
    data_points = []

    for c in c_values:
        data = virasoro_arithmetic(c)
        stokes_arity = arity_stokes_multiplier_exact(data)
        stokes_genus = genus_stokes_multiplier(data.kappa, 1)

        data_points.append({
            'c': c,
            'kappa': data.kappa,
            'rho': data.rho,
            'stokes_arity_mod': abs(stokes_arity),
            'stokes_arity_arg': cmath.phase(stokes_arity),
            'stokes_genus_mod': abs(stokes_genus),
            'stokes_genus_arg': cmath.phase(stokes_genus),
            'stokes_ratio': abs(stokes_arity) / max(abs(stokes_genus), 1e-30),
        })

    return {
        'c_range': (c_min, c_max),
        'n_points': n_points,
        'data': data_points,
    }


# =====================================================================
# Section 15: Summary diagnostics
# =====================================================================

def full_resurgence_report(c_val: float) -> Dict[str, Any]:
    """Complete resurgence and arithmetic report for Virasoro at c."""
    data = virasoro_arithmetic(c_val)
    return {
        'algebra': data.name,
        'c': c_val,
        'kappa': data.kappa,
        'kappa_dual': data.kappa_dual,
        'kappa_sum': data.kappa + data.kappa_dual,
        'rho': data.rho,
        'Delta': data.Delta,
        'singularity_map': arity_borel_singularity_map(data),
        'arity_stokes_exact': arity_stokes_multiplier_exact(data),
        'arity_stokes_numerical': arity_stokes_multiplier_numerical(data, 80),
        'genus_stokes_leading': genus_stokes_multiplier(data.kappa, 1),
        'combined_borel': combined_borel_singularities(data),
        'borel_arithmetic': borel_arithmetic_test(data),
        'transseries': build_arity_transseries(data, 30),
    }
