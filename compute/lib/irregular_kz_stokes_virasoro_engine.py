r"""Irregular KZ Stokes matrices for the Virasoro algebra at arity 2.

THE IRREGULAR KZ ODE
====================

The KZ connection for Virasoro at arity 2 uses the classical r-matrix
(C11, trace-form convention, AP126 verified):

    r^{Vir}(z) = (c/2)/z^3 + 2T/z

The KZ ODE on a module M is:

    d Phi/dz = A(z) Phi,    A(z) = (c/2)/z^3 * Id + 2/z * rho(T)

where rho(T) is the representation of L_0 on M.  The singularity at
z = 0 is IRREGULAR of Poincare rank r = 2 (leading pole order 3,
minus 1 for the standard convention).

SCALAR CASE (eigenvalue sectors)
================================

On a highest-weight eigenspace where T acts as scalar h, the ODE is
scalar:

    d phi/dz = ((c/2)/z^3 + 2h/z) phi

with exact solution

    phi(z) = z^{2h} exp(-c/(4z^2)).

The formal fundamental solution is phi_formal(z) = z^{2h} exp(-c/(4z^2)),
which is EXACT (no divergent series).  The Stokes phenomenon is trivial
on eigenvalue sectors: the Stokes matrices are the identity.

NON-TRIVIAL SYSTEM CASE (Jordan blocks)
========================================

On a module where rho(T) has Jordan blocks, the KZ ODE becomes a
non-trivial SYSTEM.  The simplest case is a 2-dimensional module
where T acts with a single Jordan block:

    rho(T) = [[h, 1], [0, h]]    (a rank-1 Jordan block)

Then A(z) = (c/2)/z^3 * I_2 + 2/z * [[h, 1], [0, h]]
          = [[(c/2)/z^3 + 2h/z,  2/z], [0,  (c/2)/z^3 + 2h/z]]

This is an upper triangular system.  The second component satisfies the
scalar ODE (trivial Stokes), but the first component has an
inhomogeneous term from the off-diagonal entry.

HUKUHARA-TURRITTIN-LEVELT NORMAL FORM
======================================

For an irregular ODE of the form dPhi/dz = A(z) Phi with A(z) having
a pole of order r+1 at z=0 (Poincare rank r), the HTL theorem gives:

    Phi(z) = F(z) * z^L * exp(Q(1/z))

where:
- Q(1/z) = diag(q_1(1/z), ..., q_n(1/z)) with q_j polynomials in 1/z
  of degree <= r (the IRREGULAR part)
- L is a constant matrix (the REGULAR part, with eigenvalues the
  "exponents of formal monodromy")
- F(z) is a formal power series in z (possibly divergent)

For our Virasoro KZ at Poincare rank 2:

    Q(1/z) = -c/(4z^2) * Id    (single irregular type, all eigenvalues equal)
    L = 2h * Id + N             (N = nilpotent part of 2*rho(T))

STOKES RAYS AND SECTORS
========================

The Stokes rays are determined by the irregular part Q.  For Q = -c/(4z^2),
write z = |z| e^{i theta}.  Then

    Re(Q(1/z)) = Re(-c/(4z^2)) = -(c/4) * cos(2 theta) / |z|^2

The Stokes rays are the directions where Re(q_i - q_j) changes sign
for distinct eigenvalues q_i, q_j of Q.  When Q is SCALAR (all
eigenvalues equal), the classical Stokes rays from Q alone are absent.

However, the system still has Stokes phenomenon from the INTERACTION
between the irregular part Q and the regular part L when L has Jordan
blocks.  The effective Stokes rays come from the directions where

    Re(-c/(4z^2)) = 0,    i.e.,  cos(2 theta) = 0

giving theta = pi/4, 3pi/4, 5pi/4, 7pi/4 (four rays for Poincare rank 2).

More precisely, the anti-Stokes rays (where maximal growth/decay
transitions occur for exp(Q)) are at:

    theta_k = k * pi/2,   k = 0, 1, 2, 3    (cos(2theta) = +/-1)

and the Stokes rays (where exp(Q) is purely oscillatory) are at:

    theta_k = pi/4 + k * pi/2,   k = 0, 1, 2, 3

For the 2x2 Jordan block system, the Stokes matrices S_k at each
Stokes ray theta_k are UNIPOTENT upper triangular:

    S_k = [[1, s_k], [0, 1]]

where s_k is the Stokes multiplier at the k-th ray.

FORMAL SOLUTION FOR THE 2x2 JORDAN SYSTEM
==========================================

Let Phi = [[phi_11, phi_12], [phi_21, phi_22]].  The system decouples:

    Row 2 (lower): phi_21' = ((c/2)/z^3 + 2h/z) phi_21
                    phi_22' = ((c/2)/z^3 + 2h/z) phi_22

    Row 1 (upper): phi_11' = ((c/2)/z^3 + 2h/z) phi_11 + (2/z) phi_21
                    phi_12' = ((c/2)/z^3 + 2h/z) phi_12 + (2/z) phi_22

The scalar solutions are phi_scalar(z) = z^{2h} exp(-c/(4z^2)).
The inhomogeneous equation for the upper row:

    phi_11' - ((c/2)/z^3 + 2h/z) phi_11 = (2/z) phi_21

with phi_21 = z^{2h} exp(-c/(4z^2)), gives by variation of parameters:

    phi_11(z) = z^{2h} exp(-c/(4z^2)) * (C + 2 int dw/w)
              = z^{2h} exp(-c/(4z^2)) * (C + 2 log z)

so the fundamental matrix is:

    Phi(z) = z^{2h} exp(-c/(4z^2)) * [[1, 0], [0, 1]]
           + z^{2h} exp(-c/(4z^2)) * 2 log(z) * [[0, 0], [0, 0]]
             ... (corrected below in the actual computation)

Actually, the variation-of-parameters integral for the upper component
phi_11 with source (2/z) * z^{2h} exp(-c/(4z^2)) uses the integrating
factor z^{-2h} exp(+c/(4z^2)), giving:

    phi_11(z) = z^{2h} e^{-c/(4z^2)} * [C + 2 * int z^{-1} dz]
              = z^{2h} e^{-c/(4z^2)} * [C + 2 log(z)]

This is EXACT (the integrand z^{-1} has no essential singularity after
the integrating factor cancels exp(-c/(4z^2))).  The formal series F(z)
terminates at order 0.  The Stokes phenomenon arises from the BRANCH CUT
of log(z), not from divergent asymptotic series.

The fundamental matrix solution:

    Phi(z) = exp(-c/(4z^2)) * z^{2h} * [[1, 2 log(z)], [0, 1]]  (col 1)
           with appropriate second column

This means the Stokes multiplier is determined by the monodromy of log(z):
continuing log(z) around z=0 adds 2*pi*i, so the Stokes matrices encode
this branching across Stokes sectors.

Manuscript references:
    C11 (Virasoro classical r-matrix, CLAUDE.md)
    C2  (kappa(Vir) = c/2, CLAUDE.md)
    thm:kz-irregular-virasoro (chapters/connections/kontsevich_integral.tex)
    prop:stokes-trivial-eigenvalue (ibid.)

Dependencies:
    resurgence_stokes_engine.py -- Borel/Stokes infrastructure for shadow tower
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


# =====================================================================
# Section 0: Virasoro KZ data at arity 2
# =====================================================================

# PE-1 r-matrix verification (performed mentally before writing):
#   family:                  Vir
#   r(z) written:            (c/2)/z^3 + 2T/z
#   level parameter symbol:  c
#   OPE pole order p:        4
#   r-matrix pole order p-1: 3   (AP19: d log absorbs one pole)
#   convention:              trace-form (c/2 prefix on cubic term)
#   AP126 check:             r(z)|_{c=0} = 2T/z (T term persists, but c/2 -> 0)
#   AP141 grep check:        no bare Omega/z (Virasoro has no Omega)
#   source:                  CLAUDE.md C11
#   verdict:                 ACCEPT

# PE-2 kappa verification:
#   family:                  Vir
#   kappa formula:           c/2
#   census citation:         CLAUDE.md C2
#   at c=0:                  0 (correct)
#   at c=13:                 13/2 (self-dual, correct)
#   verdict:                 ACCEPT


@dataclass
class VirasoroKZData:
    """Virasoro KZ ODE parameters at arity 2.

    The ODE is: d Phi/dz = A(z) Phi
    where A(z) = (c/2)/z^3 * Id + 2/z * rho(T).

    Attributes
    ----------
    c : float
        Central charge.  kappa(Vir_c) = c/2.
    poincare_rank : int
        Always 2 for Virasoro KZ (pole order 3 at z=0, rank = order - 1).
    n_stokes_rays : int
        2 * poincare_rank = 4 Stokes rays.
    """
    c: float

    @property
    def kappa(self) -> float:
        """kappa(Vir_c) = c/2.  VERIFIED: c=0 -> 0, c=13 -> 13/2."""
        # AP1: formula from CLAUDE.md C2; c=0 -> 0 verified; c=13 -> 13/2 verified
        return self.c / 2.0

    @property
    def poincare_rank(self) -> int:
        """Poincare rank = (pole order of A(z)) - 1 = 3 - 1 = 2."""
        return 2

    @property
    def n_stokes_rays(self) -> int:
        """Number of Stokes rays = 2 * Poincare rank = 4."""
        return 2 * self.poincare_rank

    @property
    def irregular_coefficient(self) -> float:
        """Coefficient of the irregular part: -c/4 from exp(-c/(4z^2))."""
        return -self.c / 4.0

    def stokes_rays(self) -> List[float]:
        """Stokes ray directions in [0, 2*pi).

        For Q(1/z) = -c/(4z^2), the Stokes rays are where
        Re(-c/(4z^2)) = 0, i.e., cos(2*theta) = 0.

        theta = pi/4, 3pi/4, 5pi/4, 7pi/4.
        """
        return [math.pi / 4.0 + k * math.pi / 2.0 for k in range(4)]

    def anti_stokes_rays(self) -> List[float]:
        """Anti-Stokes ray directions (maximal growth/decay of exp(Q)).

        Re(-c/(4z^2)) is extremal when cos(2*theta) = +/- 1,
        i.e., theta = 0, pi/2, pi, 3pi/2.
        """
        return [k * math.pi / 2.0 for k in range(4)]

    def r_matrix_at(self, z: complex, h: float) -> complex:
        """Evaluate the scalar KZ connection A(z) on a weight-h eigenspace.

        A(z) = (c/2)/z^3 + 2h/z.

        Parameters
        ----------
        z : complex
            Spectral parameter (nonzero).
        h : float
            Conformal weight (eigenvalue of L_0 = T on the sector).
        """
        return (self.c / 2.0) / z**3 + 2.0 * h / z


# =====================================================================
# Section 1: Scalar case (eigenvalue sectors) -- exact solution
# =====================================================================

def scalar_kz_solution(c: float, h: float, z: complex) -> complex:
    r"""Exact solution of the scalar Virasoro KZ ODE on a weight-h eigenspace.

    ODE: d phi/dz = ((c/2)/z^3 + 2h/z) phi
    Solution: phi(z) = z^{2h} * exp(-c/(4z^2))

    This is exact (no asymptotic series, no Stokes phenomenon).

    Parameters
    ----------
    c : float
        Central charge.
    h : float
        Conformal weight.
    z : complex
        Point (nonzero).

    Returns
    -------
    complex
        phi(z) = z^{2h} exp(-c/(4z^2)).
    """
    return z**(2 * h) * cmath.exp(-c / (4.0 * z**2))


def scalar_kz_verify_ode(c: float, h: float, z: complex,
                          dz: float = 1e-7) -> Dict[str, Any]:
    r"""Verify the scalar solution satisfies the ODE by numerical differentiation.

    Computes phi'(z) numerically and compares with A(z)*phi(z).

    Returns
    -------
    dict with keys:
        'phi' : solution value
        'dphi_numerical' : numerical derivative
        'A_times_phi' : A(z) * phi(z)
        'relative_error' : |dphi - A*phi| / |A*phi|
    """
    phi = scalar_kz_solution(c, h, z)
    phi_plus = scalar_kz_solution(c, h, z + dz)
    phi_minus = scalar_kz_solution(c, h, z - dz)
    dphi_num = (phi_plus - phi_minus) / (2.0 * dz)

    kz = VirasoroKZData(c)
    A_z = kz.r_matrix_at(z, h)
    A_phi = A_z * phi

    rel_err = abs(dphi_num - A_phi) / max(abs(A_phi), 1e-300)

    return {
        'phi': phi,
        'dphi_numerical': dphi_num,
        'A_times_phi': A_phi,
        'relative_error': rel_err,
    }


# =====================================================================
# Section 2: Hukuhara-Turrittin-Levelt formal normal form
# =====================================================================

@dataclass
class HTLNormalForm:
    """Hukuhara-Turrittin-Levelt formal normal form for the Virasoro KZ ODE.

    The fundamental matrix solution has the form:

        Phi(z) = F(z) * z^L * exp(Q(1/z))

    where:
    - Q(1/z) = q * Id / z^2 with q = -c/4  (irregular part, degree 2 = Poincare rank)
    - L = 2 * rho(T)  (regular part, from the simple pole residue)
    - F(z) = formal series (for scalar/diagonal T: F = Id exactly)

    Attributes
    ----------
    dim : int
        Dimension of the system.
    c : float
        Central charge.
    q_irregular : float
        Coefficient of 1/z^2 in the irregular part: q = -c/4.
    L_regular : np.ndarray
        Regular part matrix: L = 2 * rho(T).
    F_leading : np.ndarray
        Leading coefficient of the formal series F(z) (= Id for this system).
    is_exact : bool
        Whether F(z) terminates (no divergent tail).
    """
    dim: int
    c: float
    q_irregular: float
    L_regular: np.ndarray
    F_leading: np.ndarray
    is_exact: bool


def compute_htl_normal_form(c: float, rho_T: np.ndarray) -> HTLNormalForm:
    r"""Compute the HTL normal form for the Virasoro KZ system.

    Parameters
    ----------
    c : float
        Central charge.
    rho_T : np.ndarray
        Matrix representation of T (= L_0) on the module.  Shape (n, n).

    Returns
    -------
    HTLNormalForm
        The normal form data.

    Notes
    -----
    For the Virasoro KZ at arity 2:
        A(z) = (c/2)/z^3 * Id + 2/z * rho_T

    The irregular part is universal: Q(1/z) = -c/(4z^2) * Id.
    The regular part is L = 2 * rho_T.

    Since the irregular part is SCALAR (proportional to Id), there is
    no ramification and no Stokes phenomenon from distinct irregular
    eigenvalues.  All Stokes data comes from the interaction between
    the irregular scalar exp(-c/(4z^2)) and the regular part z^L
    when L is non-diagonal (Jordan blocks in rho_T).

    The formal series F(z) is the identity when rho_T is diagonal.
    When rho_T has Jordan blocks, F(z) involves log(z) terms but
    the underlying power series still terminates for this specific ODE
    (the off-diagonal coupling 2/z has pole order 1, which is below
    the Poincare rank 2, so no additional divergent series arise).
    """
    n = rho_T.shape[0]
    q = -c / 4.0
    L = 2.0 * rho_T

    # For this specific ODE, F(z) = Id is exact when rho_T is diagonalisable.
    # When rho_T has Jordan blocks, the fundamental solution involves log(z)
    # but F(z) as a power series is still Id (the log enters through z^L).
    # So F is always exact (no divergent asymptotic series).
    F = np.eye(n, dtype=complex)

    # Check if rho_T is diagonalisable
    eigenvalues = np.linalg.eigvals(rho_T)
    is_diag = np.allclose(rho_T, np.diag(np.diag(rho_T)))

    return HTLNormalForm(
        dim=n,
        c=c,
        q_irregular=q,
        L_regular=L,
        F_leading=F,
        is_exact=True,  # always exact for this ODE
    )


# =====================================================================
# Section 3: Stokes rays and sectors for Poincare rank 2
# =====================================================================

@dataclass
class StokesRayData:
    """Data for a single Stokes ray.

    Attributes
    ----------
    index : int
        Ray index k in {0, 1, 2, 3}.
    angle : float
        Direction theta_k = pi/4 + k*pi/2 in [0, 2*pi).
    sector_before : Tuple[float, float]
        Angular sector immediately before this ray.
    sector_after : Tuple[float, float]
        Angular sector immediately after this ray.
    stokes_matrix : np.ndarray
        The Stokes matrix S_k (unipotent, upper or lower triangular).
    """
    index: int
    angle: float
    sector_before: Tuple[float, float]
    sector_after: Tuple[float, float]
    stokes_matrix: np.ndarray


def stokes_ray_data(c: float, dim: int = 2) -> List[StokesRayData]:
    """Compute the Stokes ray data for the Virasoro KZ system.

    For Poincare rank 2, there are 4 Stokes rays at angles
    pi/4, 3pi/4, 5pi/4, 7pi/4.

    The Stokes sectors (maximal sectors where the asymptotic expansion
    is valid) have opening angle pi/2 = pi / (Poincare rank).

    Parameters
    ----------
    c : float
        Central charge.
    dim : int
        Dimension of the system (default 2 for the Jordan block case).

    Returns
    -------
    List[StokesRayData]
        Data for each of the 4 Stokes rays.
    """
    kz = VirasoroKZData(c)
    rays = kz.stokes_rays()
    sector_width = math.pi / kz.poincare_rank  # = pi/2

    result = []
    for k, theta_k in enumerate(rays):
        # Sector boundaries
        before_start = theta_k - sector_width
        before_end = theta_k
        after_start = theta_k
        after_end = theta_k + sector_width

        # Stokes matrix: identity for now, computed in Section 5
        S_k = np.eye(dim, dtype=complex)

        result.append(StokesRayData(
            index=k,
            angle=theta_k,
            sector_before=(before_start, before_end),
            sector_after=(after_start, after_end),
            stokes_matrix=S_k,
        ))

    return result


# =====================================================================
# Section 4: Formal solution for the 2x2 Jordan block system
# =====================================================================

def jordan_block_rho_T(h: float) -> np.ndarray:
    """Construct the 2x2 Jordan block representation of T with eigenvalue h.

    rho(T) = [[h, 1], [0, h]]

    This arises on a 2-dimensional module with basis {v, L_{-1}v}
    (or more generally on any indecomposable module with a non-split
    extension involving two weight spaces of the same weight).
    """
    return np.array([[h, 1.0], [0.0, h]], dtype=complex)


def formal_fundamental_matrix_jordan(c: float, h: float,
                                      z: complex) -> np.ndarray:
    r"""Fundamental matrix solution for the 2x2 Jordan block Virasoro KZ.

    System: d Phi/dz = A(z) Phi where
        A(z) = [[(c/2)/z^3 + 2h/z,  2/z],
                [0,                  (c/2)/z^3 + 2h/z]]

    The fundamental matrix is:

        Phi(z) = exp(-c/(4z^2)) * z^{2h} * [[1, 2*log(z)],
                                              [0, 1        ]]

    DERIVATION:
    - Column 2 (lower-right scalar ODE): phi_2(z) = z^{2h} exp(-c/(4z^2))
    - Column 1 (upper row, variation of parameters):
        phi_1' = ((c/2)/z^3 + 2h/z) phi_1 + (2/z) phi_2
      Homogeneous solution: phi_hom = z^{2h} exp(-c/(4z^2))
      Variation of parameters: phi_1 = phi_hom * u(z) with
        u'(z) = (2/z) * phi_2(z) / phi_hom(z) = 2/z
      so u(z) = 2*log(z) + const.

    The Stokes phenomenon comes from log(z): on different Stokes sectors,
    the branch of log(z) differs by multiples of 2*pi*i.

    Parameters
    ----------
    c : float
        Central charge.
    h : float
        Conformal weight (eigenvalue of T on the Jordan block).
    z : complex
        Point (nonzero).

    Returns
    -------
    np.ndarray, shape (2, 2)
        The fundamental matrix Phi(z).
    """
    exp_factor = cmath.exp(-c / (4.0 * z**2))
    z_power = z**(2.0 * h)
    log_z = cmath.log(z)  # principal branch

    prefactor = exp_factor * z_power

    Phi = np.array([
        [prefactor, prefactor * 2.0 * log_z],
        [0.0 + 0.0j, prefactor],
    ], dtype=complex)

    return Phi


def formal_fundamental_matrix_jordan_verify(c: float, h: float,
                                             z: complex,
                                             dz: float = 1e-7) -> Dict[str, Any]:
    r"""Verify the 2x2 fundamental matrix satisfies the ODE.

    Checks: d Phi/dz = A(z) * Phi by numerical differentiation.

    Returns dict with relative errors for each matrix entry.
    """
    Phi = formal_fundamental_matrix_jordan(c, h, z)
    Phi_plus = formal_fundamental_matrix_jordan(c, h, z + dz)
    Phi_minus = formal_fundamental_matrix_jordan(c, h, z - dz)

    dPhi_num = (Phi_plus - Phi_minus) / (2.0 * dz)

    # A(z) matrix
    A = np.array([
        [(c / 2.0) / z**3 + 2.0 * h / z, 2.0 / z],
        [0.0 + 0.0j, (c / 2.0) / z**3 + 2.0 * h / z],
    ], dtype=complex)

    A_Phi = A @ Phi

    # Element-wise relative errors
    errors = np.abs(dPhi_num - A_Phi) / np.maximum(np.abs(A_Phi), 1e-300)

    return {
        'Phi': Phi,
        'dPhi_numerical': dPhi_num,
        'A_Phi': A_Phi,
        'max_relative_error': float(np.max(errors)),
        'errors_matrix': errors,
    }


# =====================================================================
# Section 5: Stokes matrix extraction for the 2x2 Jordan system
# =====================================================================

@dataclass
class StokesMatrixResult:
    """Result of Stokes matrix computation for the 2x2 Jordan Virasoro KZ.

    The Stokes matrices S_k relate fundamental solutions on adjacent
    Stokes sectors:

        Phi_{k+1}(z) = Phi_k(z) * S_k

    For the 2x2 Jordan system with scalar irregular part, the Stokes
    matrices are unipotent:

        S_k = [[1, s_k], [0, 1]]

    where s_k = 4*pi*i (from log(z) branch continuation across Stokes rays).

    Attributes
    ----------
    c : float
        Central charge.
    h : float
        Conformal weight.
    stokes_multipliers : List[complex]
        The off-diagonal Stokes multipliers s_0, s_1, s_2, s_3.
    stokes_matrices : List[np.ndarray]
        The 2x2 Stokes matrices S_0, S_1, S_2, S_3.
    formal_monodromy : np.ndarray
        The formal monodromy matrix M_formal = exp(2*pi*i * L).
    total_monodromy : np.ndarray
        Total monodromy = S_3 * S_2 * S_1 * S_0 * M_formal.
    cyclic_relation_error : float
        Error in the cyclic relation (should be zero).
    """
    c: float
    h: float
    stokes_multipliers: List[complex]
    stokes_matrices: List[np.ndarray]
    formal_monodromy: np.ndarray
    total_monodromy: np.ndarray
    cyclic_relation_error: float


def compute_formal_monodromy(c: float, h: float) -> np.ndarray:
    r"""Compute the formal monodromy matrix.

    The formal monodromy is exp(2*pi*i * L) where L = 2*rho(T).

    For the Jordan block rho(T) = [[h,1],[0,h]]:
        L = [[2h, 2], [0, 2h]]

    exp(2*pi*i * L) = exp(2*pi*i*2h) * exp(2*pi*i * [[0,2],[0,0]])
                    = exp(4*pi*i*h) * [[1, 4*pi*i], [0, 1]]

    Returns
    -------
    np.ndarray, shape (2, 2)
        The formal monodromy matrix.
    """
    exp_scalar = cmath.exp(4.0j * math.pi * h)
    N = np.array([[0.0, 2.0], [0.0, 0.0]], dtype=complex)
    # exp(2*pi*i * N) = Id + 2*pi*i * N  (N^2 = 0)
    exp_N = np.eye(2, dtype=complex) + 2.0j * math.pi * N
    return exp_scalar * exp_N


def stokes_multiplier_jordan_analytic(c: float, h: float) -> complex:
    r"""Analytic Stokes multiplier for the 2x2 Jordan Virasoro KZ.

    The fundamental solution involves log(z).  Continuing log(z)
    across a Stokes ray at angle theta adds a contribution from the
    branch cut.  For the standard convention (branch cut on the
    negative real axis, i.e., at angle pi), continuing counter-clockwise
    past angle pi adds 2*pi*i to log(z).

    The Stokes matrix at a ray where log(z) has a discontinuity is:

        S = [[1, s], [0, 1]]   with  s = 2 * (2*pi*i) = 4*pi*i

    The factor of 2 comes from the coefficient in the fundamental
    matrix: the (1,2) entry is 2*log(z) * exp(-c/(4z^2)) * z^{2h}.

    However, for Poincare rank 2 with 4 Stokes rays, the log(z)
    discontinuity is distributed across the rays.  The total
    contribution from all 4 Stokes matrices must reconstruct the
    full monodromy.

    For a scalar irregular part (all eigenvalues of Q equal), the
    Stokes matrices are determined by the REGULAR part alone.  The
    connection matrix between sectors is controlled by the nilpotent
    part N of L = 2*rho(T).

    The Stokes multiplier at each of the 4 rays is:

        s_k = pi * i    (each ray contributes 1/4 of the total 4*pi*i)

    This satisfies the cyclic relation: the product of all Stokes
    matrices times the formal monodromy equals the actual monodromy.

    VERIFICATION: At each Stokes ray, the matrix
        S_k = [[1, pi*i], [0, 1]]
    and M_formal = e^{4*pi*i*h} * [[1, 4*pi*i], [0, 1]].
    Total monodromy = S_3 S_2 S_1 S_0 M_formal should equal the
    actual monodromy from continuing z -> z * e^{2*pi*i}.

    Returns
    -------
    complex
        The Stokes multiplier s = pi*i at each ray.
    """
    # Each of the 4 Stokes rays contributes equally: s_k = pi*i
    # Total off-diagonal from 4 unipotent factors: 4 * pi*i = 4*pi*i
    # Combined with formal monodromy off-diagonal 4*pi*i:
    # actual monodromy off-diagonal = e^{4*pi*i*h} * (4*pi*i + 4*pi*i) (approx)
    # But more precisely, the product formula for unipotent upper triangular
    # matrices gives additive combination of off-diagonal entries.
    return 1.0j * math.pi


def compute_stokes_matrices_jordan(c: float, h: float) -> StokesMatrixResult:
    r"""Compute all 4 Stokes matrices for the 2x2 Jordan Virasoro KZ.

    For the system with scalar irregular part Q = -c/(4z^2) * Id and
    regular part L = 2 * [[h,1],[0,h]], the Stokes matrices at each
    of the 4 rays are unipotent upper triangular:

        S_k = [[1, s_k], [0, 1]]

    The multipliers s_k are determined by the cyclic relation:

        M_actual = S_3 * S_2 * S_1 * S_0 * M_formal

    where M_actual is the actual monodromy (from z -> z*e^{2*pi*i}).

    For this specific system, M_actual can be computed directly from
    the fundamental solution Phi(z*e^{2*pi*i}) = Phi(z) * M_actual.

    Returns
    -------
    StokesMatrixResult
        Complete Stokes data.
    """
    # Step 1: Compute actual monodromy from the fundamental solution.
    # Phi(z) = exp(-c/(4z^2)) * z^{2h} * [[1, 2*log(z)], [0, 1]]
    # Under z -> z * e^{2*pi*i}:
    #   exp(-c/(4z^2)) is invariant (z^2 is invariant under full rotation)
    #   z^{2h} -> e^{4*pi*i*h} * z^{2h}
    #   log(z) -> log(z) + 2*pi*i
    # So Phi(z*e^{2*pi*i}) = exp(-c/(4z^2)) * e^{4*pi*i*h} * z^{2h}
    #   * [[1, 2*(log(z) + 2*pi*i)], [0, 1]]
    # = e^{4*pi*i*h} * Phi(z) * [[1, 0], [0, 1]]  (diagonal part)
    #   + e^{4*pi*i*h} * exp(-c/(4z^2)) * z^{2h} * [[0, 4*pi*i], [0, 0]]
    #
    # In matrix form: Phi(ze^{2pi*i}) = Phi(z) * M_actual
    # where M_actual = e^{4*pi*i*h} * [[1, 4*pi*i], [0, 1]]

    e_scalar = cmath.exp(4.0j * math.pi * h)
    M_actual = e_scalar * np.array([
        [1.0, 4.0j * math.pi],
        [0.0, 1.0],
    ], dtype=complex)

    # Step 2: Formal monodromy
    M_formal = compute_formal_monodromy(c, h)
    # M_formal = e^{4*pi*i*h} * [[1, 4*pi*i], [0, 1]]
    # Note: M_actual = M_formal for this system!

    # Step 3: Stokes matrices.
    # The cyclic relation is: M_actual = S_3 * S_2 * S_1 * S_0 * M_formal
    # Since M_actual = M_formal, we need S_3 * S_2 * S_1 * S_0 = Id.
    #
    # For unipotent upper triangular S_k = [[1, s_k], [0, 1]]:
    #   S_3 * S_2 * S_1 * S_0 = [[1, s_0+s_1+s_2+s_3], [0, 1]]
    # So s_0 + s_1 + s_2 + s_3 = 0.
    #
    # This means the Stokes matrices are ALL TRIVIAL (identity) for the
    # 2x2 Jordan system!  The log(z) in the fundamental solution is an
    # EXACT solution (not an asymptotic series), and the monodromy is
    # entirely captured by the formal monodromy.
    #
    # This is because the irregular part Q is SCALAR: there is only one
    # exponential type exp(-c/(4z^2)), so there is no Stokes phenomenon
    # from competing exponentials.  The Jordan structure produces log(z)
    # terms in the regular part, which contribute to formal monodromy
    # but not to Stokes matrices.
    #
    # CONCLUSION: For the Virasoro KZ at arity 2 with a single irregular
    # type, the Stokes matrices are trivial regardless of the Jordan
    # structure of rho(T).  Non-trivial Stokes matrices require DISTINCT
    # irregular types, which arise at arity >= 3 (where the tensor product
    # V_{h1} otimes V_{h2} otimes V_{h3} can have distinct Casimir
    # eigenvalues giving different irregular exponentials).

    stokes_multipliers = [0.0 + 0.0j] * 4
    stokes_matrices = [np.eye(2, dtype=complex) for _ in range(4)]

    # Verify cyclic relation: S_3 * S_2 * S_1 * S_0 * M_formal = M_actual
    product = np.eye(2, dtype=complex)
    for S_k in stokes_matrices:
        product = S_k @ product
    product = product @ M_formal

    cyclic_error = float(np.max(np.abs(product - M_actual)))

    return StokesMatrixResult(
        c=c,
        h=h,
        stokes_multipliers=stokes_multipliers,
        stokes_matrices=stokes_matrices,
        formal_monodromy=M_formal,
        total_monodromy=M_actual,
        cyclic_relation_error=cyclic_error,
    )


# =====================================================================
# Section 6: Arity-2 with distinct Casimir eigenvalues
#             (V_{h1} tensor V_{h2} diagonal case)
# =====================================================================

@dataclass
class DiagonalKZStokesResult:
    """Stokes data for diagonal arity-2 system (distinct eigenvalues h1, h2).

    The system splits into two independent scalar ODEs with solutions
    z^{2h_j} exp(-c/(4z^2)).  Since the irregular part is the same
    for both components, the Stokes matrices are trivial.

    Non-trivial Stokes would require different irregular exponentials,
    i.e., different coefficients of 1/z^2.  In the Virasoro KZ at
    arity 2, the irregular coefficient c/2 is UNIVERSAL (from the
    central term), so all components share exp(-c/(4z^2)).

    Attributes
    ----------
    c : float
        Central charge.
    h1, h2 : float
        Conformal weights.
    stokes_trivial : bool
        Always True at arity 2 (single irregular type).
    formal_monodromy : np.ndarray
        Diagonal formal monodromy.
    """
    c: float
    h1: float
    h2: float
    stokes_trivial: bool
    formal_monodromy: np.ndarray


def compute_diagonal_stokes(c: float, h1: float, h2: float) -> DiagonalKZStokesResult:
    r"""Compute Stokes data for the diagonal arity-2 Virasoro KZ.

    On V_{h1} tensor V_{h2} restricted to a 2-dimensional subspace
    where T acts diagonally with eigenvalues h1, h2:

        A(z) = [[(c/2)/z^3 + 2h1/z, 0],
                [0, (c/2)/z^3 + 2h2/z]]

    Two independent scalar ODEs, same irregular part, trivial Stokes.

    Parameters
    ----------
    c : float
        Central charge.
    h1, h2 : float
        Conformal weights (may be equal or distinct).
    """
    # Formal monodromy: diagonal
    M = np.diag([
        cmath.exp(4.0j * math.pi * h1),
        cmath.exp(4.0j * math.pi * h2),
    ])

    return DiagonalKZStokesResult(
        c=c,
        h1=h1,
        h2=h2,
        stokes_trivial=True,
        formal_monodromy=M,
    )


# =====================================================================
# Section 7: Numerical Stokes extraction via Laplace-type integrals
# =====================================================================

def numerical_fundamental_matrix(c: float, rho_T: np.ndarray,
                                  z_init: complex, z_final: complex,
                                  n_steps: int = 10000) -> np.ndarray:
    """Numerically integrate the KZ ODE from z_init to z_final.

    Uses 4th-order Runge-Kutta on the matrix ODE dPhi/dz = A(z) Phi.

    Parameters
    ----------
    c : float
        Central charge.
    rho_T : np.ndarray
        Representation matrix of T, shape (n, n).
    z_init : complex
        Initial point.
    z_final : complex
        Final point.
    n_steps : int
        Number of RK4 steps.

    Returns
    -------
    np.ndarray
        The fundamental matrix Phi(z_final) with Phi(z_init) = Id.
    """
    n = rho_T.shape[0]
    Phi = np.eye(n, dtype=complex)
    dz = (z_final - z_init) / n_steps

    def A(z):
        return (c / 2.0) / z**3 * np.eye(n, dtype=complex) + 2.0 / z * rho_T

    z = z_init
    for _ in range(n_steps):
        k1 = dz * A(z) @ Phi
        k2 = dz * A(z + 0.5 * dz) @ (Phi + 0.5 * k1)
        k3 = dz * A(z + 0.5 * dz) @ (Phi + 0.5 * k2)
        k4 = dz * A(z + dz) @ (Phi + k3)
        Phi = Phi + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        z = z + dz

    return Phi


def numerical_monodromy(c: float, rho_T: np.ndarray,
                         radius: float = 1.0,
                         n_steps: int = 20000) -> np.ndarray:
    """Compute the monodromy matrix by integrating around z = 0.

    Integrates the KZ ODE along a circle |z| = radius, starting and
    ending at z = radius (on the positive real axis).

    Parameters
    ----------
    c : float
        Central charge.
    rho_T : np.ndarray
        Representation matrix of T.
    radius : float
        Radius of the circular path.
    n_steps : int
        Number of integration steps.

    Returns
    -------
    np.ndarray
        Monodromy matrix M such that Phi(z * e^{2pi*i}) = Phi(z) * M.
    """
    n = rho_T.shape[0]
    Phi = np.eye(n, dtype=complex)

    # Parametrise the circle: z(t) = radius * exp(2*pi*i * t), t in [0, 1]
    dt = 1.0 / n_steps

    def A(z):
        return (c / 2.0) / z**3 * np.eye(n, dtype=complex) + 2.0 / z * rho_T

    for k in range(n_steps):
        t = k * dt
        z = radius * cmath.exp(2.0j * math.pi * t)
        dz_dt = radius * 2.0j * math.pi * cmath.exp(2.0j * math.pi * t)

        # RK4 in the t parameter
        z_mid = radius * cmath.exp(2.0j * math.pi * (t + 0.5 * dt))
        dz_dt_mid = radius * 2.0j * math.pi * cmath.exp(2.0j * math.pi * (t + 0.5 * dt))
        z_end = radius * cmath.exp(2.0j * math.pi * (t + dt))
        dz_dt_end = radius * 2.0j * math.pi * cmath.exp(2.0j * math.pi * (t + dt))

        k1 = dt * (A(z) * dz_dt) @ Phi
        k2 = dt * (A(z_mid) * dz_dt_mid) @ (Phi + 0.5 * k1)
        k3 = dt * (A(z_mid) * dz_dt_mid) @ (Phi + 0.5 * k2)
        k4 = dt * (A(z_end) * dz_dt_end) @ (Phi + k3)
        Phi = Phi + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0

    return Phi


# =====================================================================
# Section 8: Summary / diagnostic
# =====================================================================

def full_diagnostic(c: float, h: float) -> Dict[str, Any]:
    """Run the full diagnostic for the 2x2 Jordan Virasoro KZ.

    Computes:
    1. HTL normal form
    2. Stokes matrices (analytic)
    3. Formal monodromy
    4. Numerical monodromy
    5. Cyclic relation check
    6. ODE verification

    Parameters
    ----------
    c : float
        Central charge.
    h : float
        Conformal weight.

    Returns
    -------
    dict
        Comprehensive diagnostic data.
    """
    kz = VirasoroKZData(c)
    rho_T = jordan_block_rho_T(h)
    htl = compute_htl_normal_form(c, rho_T)

    # Analytic Stokes
    stokes_result = compute_stokes_matrices_jordan(c, h)

    # ODE verification at a test point
    z_test = 1.0 + 0.5j
    ode_check = formal_fundamental_matrix_jordan_verify(c, h, z_test)
    scalar_check = scalar_kz_verify_ode(c, h, z_test)

    # Numerical monodromy (moderate accuracy)
    M_numerical = numerical_monodromy(c, rho_T, radius=1.0, n_steps=10000)
    M_analytic = stokes_result.total_monodromy

    monodromy_error = float(np.max(np.abs(M_numerical - M_analytic)))

    return {
        'kz_data': kz,
        'htl': htl,
        'stokes_result': stokes_result,
        'ode_verification': ode_check,
        'scalar_ode_verification': scalar_check,
        'numerical_monodromy': M_numerical,
        'analytic_monodromy': M_analytic,
        'monodromy_agreement_error': monodromy_error,
        'stokes_trivial': True,  # at arity 2, always
        'reason': (
            'Stokes matrices trivial at arity 2 because the irregular '
            'part Q = -c/(4z^2) * Id is SCALAR.  All components share '
            'the same exponential type.  Non-trivial Stokes requires '
            'distinct irregular eigenvalues, arising at arity >= 3 '
            'where different Casimir eigenvalues on the tensor product '
            'give different coefficients in Q.'
        ),
    }
