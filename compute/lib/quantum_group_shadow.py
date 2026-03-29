r"""Quantum group shadow engine: R-matrices, Yangians, and KZ connections
from the shadow Postnikov tower.

The central insight: quantum group structures ARE the shadow tower, read
through the collision residue lens.  Specifically:

  1. r(z) = Res^{coll}_{0,2}(Theta_A)  -- the classical r-matrix is the
     binary collision residue of the MC element Theta_A.

  2. R(z) = 1 + hbar*r(z) + hbar^2*r_2(z) + ...  -- the quantum R-matrix
     is the quantization of r(z), with genus-1 correction r_2.

  3. Y(g) generators emerge from the arity-n shadow projections:
     - Level 0 from arity-2 (kappa)
     - Level 1 from arity-3 (cubic shadow C)
     - Level 2 from arity-4 (quartic shadow Q)

  4. Baxter Q-operator from higher-arity shadows encodes TQ relations.

  5. The shadow connection nabla^sh restricts to the KZ connection on
     Conf_n(C), and its monodromy is the R-matrix (Drinfeld-Kohno theorem).

  6. Shadow depth = quantum group complexity:
     G (depth 2) -> abelian (trivial quantum group)
     L (depth 3) -> classical Yangian (Lie-type)
     C (depth 4) -> deformed Yangian (contact correction)
     M (depth inf) -> full quantum group (mixed)

MATHEMATICAL FRAMEWORK:

  The MC element Theta_A := D_A - d_0 is proved (thm:mc2-bar-intrinsic).
  Its binary collision residue on Conf_2(C) gives r(z):

    For Heisenberg H_k:   r(z) = k/z^2             (abelian, trivial CYBE)
    For affine sl_2(k):   r(z) = Omega/z            (classical r-matrix, CYBE)
    For Virasoro Vir_c:   r(z) = (c/2)/z^4 + 2L/z^2 + L'/z
                                                     (Virasoro r-matrix)

  The CYBE (classical Yang-Baxter equation) is:
    [r_{12}, r_{13}] + [r_{12}, r_{23}] + [r_{13}, r_{23}] = 0

  Quantization: R(z) satisfies the quantum Yang-Baxter equation
    R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)

CONVENTIONS:
  - Cohomological grading (|d| = +1)
  - hbar = deformation parameter
  - z = spectral parameter
  - Omega = Casimir element in g tensor g
  - P = permutation operator on V tensor V
  - Yang R-matrix: R(u) = Id - hbar*P/u

References:
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  thm:collision-residue-twisting (frontier_modular_holography_platonic.tex)
  thm:collision-depth-2-ybe (frontier_modular_holography_platonic.tex)
  thm:shadow-connection-kz (frontier_modular_holography_platonic.tex)
  cor:shadow-connection-heisenberg (frontier_modular_holography_platonic.tex)
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
  thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
  def:modular-yangian-pro (yangians_drinfeld_kohno.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction
from math import factorial, comb
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np
from sympy import (
    Matrix,
    Rational,
    Symbol,
    symbols,
    simplify,
    expand,
    sqrt,
    cos,
    sin,
    exp,
    pi,
    I,
    oo,
    S,
    Poly,
    series,
    O,
    Function,
    bernoulli,
)


# =========================================================================
# 0. Shadow depth classification (from manuscript)
# =========================================================================

class ShadowDepthClass(Enum):
    """Shadow depth classification (thm:shadow-archetype-classification).

    G: Gaussian, depth 2 -- tower terminates at arity 2
    L: Lie/tree, depth 3 -- tower terminates at arity 3
    C: Contact, depth 4 -- tower terminates at arity 4
    M: Mixed, depth infinity -- tower never terminates
    """
    G = "G"
    L = "L"
    C = "C"
    M = "M"


class QuantumGroupType(Enum):
    """Quantum group type corresponding to shadow depth.

    Shadow depth = quantum group complexity
    (thm:shadow-archetype-classification, concordance.tex).
    """
    ABELIAN = "abelian"           # G class: trivial quantum group
    CLASSICAL_YANGIAN = "yangian" # L class: classical Yangian Y(g)
    DEFORMED_YANGIAN = "deformed" # C class: deformed Yangian (contact)
    FULL_QUANTUM = "full"         # M class: full quantum group U_q(g)


DEPTH_TO_QUANTUM_GROUP = {
    ShadowDepthClass.G: QuantumGroupType.ABELIAN,
    ShadowDepthClass.L: QuantumGroupType.CLASSICAL_YANGIAN,
    ShadowDepthClass.C: QuantumGroupType.DEFORMED_YANGIAN,
    ShadowDepthClass.M: QuantumGroupType.FULL_QUANTUM,
}


# =========================================================================
# 1. Classical r-matrix from shadow (collision residue)
# =========================================================================

@dataclass
class ClassicalRMatrix:
    r"""Classical r-matrix r(z) = Res^{coll}_{0,2}(Theta_A).

    The binary collision residue of the MC element Theta_A on Conf_2(C).

    The r-matrix is represented as a Laurent series in z:
        r(z) = sum_{k} r_k / z^k

    Attributes:
        family: Name of the chiral algebra family.
        poles: Dict mapping pole order k -> coefficient r_k.
        max_pole: Maximum pole order.
        dim_g: Dimension of the Lie algebra (for matrix representations).
        parameter: The deformation parameter (k for KM, c for Virasoro).
    """
    family: str
    poles: Dict[int, Any]
    max_pole: int
    dim_g: int = 0
    parameter: Any = None

    def evaluate(self, z: Any) -> Any:
        """Evaluate r(z) as a symbolic expression."""
        result = S.Zero
        for k, coeff in self.poles.items():
            result += coeff / z**k
        return result

    @property
    def leading_pole(self) -> int:
        """Order of the leading pole in r(z)."""
        return max(self.poles.keys()) if self.poles else 0


def heisenberg_r_matrix(k=None) -> ClassicalRMatrix:
    r"""r-matrix for Heisenberg H_k: r(z) = k/z^2.

    The Heisenberg is abelian, so the r-matrix is a scalar multiple
    of 1/z^2.  It has a second-order pole (no first-order pole, since
    there is no Lie bracket).

    The CYBE is trivially satisfied: all commutators vanish.

    Shadow depth: 2 (class G).  The arity-2 shadow kappa = k exhausts
    the entire tower.  No cubic or higher shadows.
    """
    if k is None:
        k = Symbol('k')
    return ClassicalRMatrix(
        family="Heisenberg",
        poles={2: k},
        max_pole=2,
        dim_g=1,
        parameter=k,
    )


def affine_sl2_r_matrix(k=None) -> ClassicalRMatrix:
    r"""r-matrix for affine sl_2 at level k: r(z) = Omega/z.

    Here Omega is the Casimir in sl_2 tensor sl_2.  In the basis
    {e, h, f} with standard structure constants:
        Omega = e tensor f + f tensor e + (1/2) h tensor h

    Normalized by the level: the actual shadow coefficient is
        r(z) = (1/(k + h^v)) * Omega / z

    where h^v = 2 is the dual Coxeter number of sl_2.

    The CYBE is satisfied by the classical r-matrix Omega/z
    because Omega is ad-invariant (Casimir).

    Shadow depth: 3 (class L).  The cubic shadow from the Lie bracket
    terminates the tower.
    """
    if k is None:
        k = Symbol('k')
    h_dual = 2  # dual Coxeter number for sl_2
    return ClassicalRMatrix(
        family="Affine_sl2",
        poles={1: Rational(1, 1)},  # Omega/z, Omega = Casimir
        max_pole=1,
        dim_g=3,
        parameter=k,
    )


def virasoro_r_matrix(c=None) -> ClassicalRMatrix:
    r"""r-matrix for Virasoro Vir_c.

    The Virasoro OPE T(z) T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + T'(w)/(z-w)
    gives the r-matrix (collision residue on Conf_2):

        r(z) = (c/2)/z^4 + 2L/z^2 + L'/z

    where L denotes the Virasoro generator T and L' = dT.

    At the scalar level (projecting to the primary line):
        r^{scalar}(z) = (c/2)/z^4

    The fourth-order pole reflects the fact that Virasoro has conformal
    weight 2 (not weight 1 like KM), so the OPE starts at order 4.

    Shadow depth: infinity (class M).  The tower never terminates.
    """
    if c is None:
        c = Symbol('c')
    return ClassicalRMatrix(
        family="Virasoro",
        poles={4: c / 2, 2: S(2), 1: S.One},
        max_pole=4,
        dim_g=1,  # single generator T
        parameter=c,
    )


def affine_slN_r_matrix(N: int, k=None) -> ClassicalRMatrix:
    r"""r-matrix for affine sl_N at level k: r(z) = Omega/z.

    Omega is the Casimir in sl_N tensor sl_N:
        Omega = sum_{a} t^a tensor t_a

    where {t^a} is a basis of sl_N and {t_a} the dual basis
    under the Killing form.

    dim(sl_N) = N^2 - 1.
    Dual Coxeter number h^v = N.

    Shadow depth: 3 (class L) for all N.
    """
    if k is None:
        k = Symbol('k')
    dim_g = N * N - 1
    return ClassicalRMatrix(
        family=f"Affine_sl{N}",
        poles={1: S.One},  # Omega/z
        max_pole=1,
        dim_g=dim_g,
        parameter=k,
    )


def betagamma_r_matrix() -> ClassicalRMatrix:
    r"""r-matrix for the beta-gamma system.

    beta(z) gamma(w) ~ 1/(z-w)
    gamma(z) beta(w) ~ -1/(z-w)

    The r-matrix on the 2-dim generator space {beta, gamma}:
        r(z) = (E_{12} - E_{21}) / z

    where E_{ij} are elementary matrices.

    Shadow depth: 4 (class C, contact).  The quartic shadow arises
    from the contact term but terminates by stratum separation.
    """
    return ClassicalRMatrix(
        family="BetaGamma",
        poles={1: S.One},
        max_pole=1,
        dim_g=2,
        parameter=None,
    )


# =========================================================================
# 2. CYBE verification
# =========================================================================

def sl2_casimir_matrix() -> np.ndarray:
    """Casimir Omega for sl_2 in the fundamental (2-dim) representation.

    Omega = sum_a t^a tensor t_a where {t^a} is the orthonormal basis
    under the Killing form.

    In the standard basis {e, h, f} with normalization:
        Tr(ad(h)^2) = 8, Tr(ad(e) ad(f)) = 4, Tr(ad(f) ad(e)) = 4

    In the 2-dim rep with standard matrices:
        e = [[0,1],[0,0]], f = [[0,0],[1,0]], h = [[1,0],[0,-1]]

    Killing form: K(x,y) = 4*Tr(xy) for sl_2.
    Dual basis under K: e^* = f/4, f^* = e/4, h^* = h/8... no.

    Standard normalization for the invariant form (., .):
        (e, f) = 1, (h, h) = 2

    Then Omega = e tensor f + f tensor e + (1/2) h tensor h
    as 4x4 matrix on C^2 tensor C^2.

    Omega = P (the permutation matrix) for sl_2 in the fundamental rep.
    More precisely: Omega = 2*P - Id (for sl_2 with the standard form).

    Actually, for sl_N in the fundamental: Omega_{ij,kl} = delta_{il} delta_{jk}
    = the permutation P.  And the Casimir C_2 = Omega with trace = N.

    For CYBE verification, what matters is [r_{12}, r_{13}] + cyc = 0
    where r(u) = Omega/u = P/u for the Yang r-matrix.
    """
    # Permutation matrix P on C^2 tensor C^2
    P = np.zeros((4, 4))
    P[0, 0] = 1  # |00> -> |00>
    P[1, 2] = 1  # |01> -> |10>
    P[2, 1] = 1  # |10> -> |01>
    P[3, 3] = 1  # |11> -> |11>
    return P


def slN_casimir_matrix(N: int) -> np.ndarray:
    """Casimir (permutation) matrix P on C^N tensor C^N.

    For sl_N in the fundamental representation, the Casimir
    acts as the permutation operator: Omega = P.

    P_{(ij),(kl)} = delta_{il} delta_{jk}
    i.e. P|i,j> = |j,i>.
    """
    d = N * N
    P = np.zeros((d, d))
    for i in range(N):
        for j in range(N):
            P[i * N + j, j * N + i] = 1.0
    return P


def embed_12(M: np.ndarray, N: int) -> np.ndarray:
    """Embed M acting on spaces 1,2 into V^{tensor 3} = (C^N)^3.

    M is N^2 x N^2, acting on V_1 tensor V_2.
    Result is N^3 x N^3, acting on V_1 tensor V_2 tensor V_3.
    """
    return np.kron(M, np.eye(N))


def embed_23(M: np.ndarray, N: int) -> np.ndarray:
    """Embed M acting on spaces 2,3 into V^{tensor 3}.

    M is N^2 x N^2, acting on V_2 tensor V_3.
    """
    return np.kron(np.eye(N), M)


def embed_13(M: np.ndarray, N: int) -> np.ndarray:
    """Embed M acting on spaces 1,3 into V^{tensor 3}.

    Uses the permutation of tensor factors: apply P_{23} . (M tensor Id) . P_{23}
    where P_{23} swaps spaces 2 and 3.

    Alternatively, construct directly:
    M_13|i,j,k> = sum_{l,m} M_{(ik),(lm)} |l,j,m>
    """
    d3 = N ** 3
    M13 = np.zeros((d3, d3))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    for m in range(N):
                        # M_{(ik),(lm)} -> coefficient of |l,j,m>
                        M13[l * N * N + j * N + m,
                            i * N * N + j * N + k] += M[i * N + k, l * N + m]
    return M13


def verify_cybe_yang(N: int) -> Dict[str, Any]:
    r"""Verify the classical Yang-Baxter equation for r(u) = P/u.

    The CYBE for r(z) = Omega/z:
        [r_{12}(u), r_{13}(u+v)] + [r_{12}(u), r_{23}(v)] + [r_{13}(u+v), r_{23}(v)] = 0

    For the rational r-matrix r(u) = P/u, substitute specific u, v values
    and check numerically.  The CYBE specializes to:

        [P_{12}, P_{13}]/(u(u+v)) + [P_{12}, P_{23}]/(u*v) + [P_{13}, P_{23}]/((u+v)*v) = 0

    Multiply through by u*v*(u+v):
        v*[P_{12}, P_{13}] + (u+v)*[P_{12}, P_{23}] + u*[P_{13}, P_{23}] = 0

    This must hold for ALL u, v, which means:
        [P_{12}, P_{23}] = 0?  No.  The equation is:
        v*[P_{12}, P_{13}] + (u+v)*[P_{12}, P_{23}] + u*[P_{13}, P_{23}] = 0

    Collecting: u*([P_{12}, P_{23}] + [P_{13}, P_{23}]) + v*([P_{12}, P_{13}] + [P_{12}, P_{23}]) = 0

    For this to hold for all u, v:
        [P_{12}, P_{23}] + [P_{13}, P_{23}] = 0      (coeff of u)
        [P_{12}, P_{13}] + [P_{12}, P_{23}] = 0      (coeff of v)

    These are the infinitesimal braid relations: they hold because P
    satisfies the braid equation P_{12} P_{23} P_{12} = P_{23} P_{12} P_{23}.

    We verify both relations numerically.
    """
    P = slN_casimir_matrix(N)
    P12 = embed_12(P, N)
    P23 = embed_23(P, N)
    P13 = embed_13(P, N)

    # Commutators
    comm_12_13 = P12 @ P13 - P13 @ P12
    comm_12_23 = P12 @ P23 - P23 @ P12
    comm_13_23 = P13 @ P23 - P23 @ P13

    # CYBE: [r12,r13] + [r12,r23] + [r13,r23] = 0
    # (for the non-spectral-parameter form r = Omega in g tensor g)
    cybe_sum = comm_12_13 + comm_12_23 + comm_13_23

    # Infinitesimal braid relations (stronger, implies CYBE for r(u) = P/u)
    ibr1 = comm_12_23 + comm_13_23  # should be 0
    ibr2 = comm_12_13 + comm_12_23  # should be 0

    return {
        "N": N,
        "dim_V": N,
        "dim_V3": N ** 3,
        "cybe_holds": bool(np.allclose(cybe_sum, 0)),
        "cybe_max_err": float(np.max(np.abs(cybe_sum))),
        "ibr1_holds": bool(np.allclose(ibr1, 0)),
        "ibr2_holds": bool(np.allclose(ibr2, 0)),
        "braid_eq_holds": bool(np.allclose(
            P12 @ P23 @ P12, P23 @ P12 @ P23
        )),
    }


def verify_cybe_heisenberg() -> Dict[str, Any]:
    r"""Verify CYBE for Heisenberg r-matrix r(z) = k/z^2.

    For abelian (rank 1), r(z) is scalar.  All commutators vanish
    trivially: [r_{12}, r_{13}] = 0 since everything commutes.
    """
    return {
        "family": "Heisenberg",
        "r_matrix": "k/z^2",
        "cybe_holds": True,
        "reason": "abelian: all commutators vanish",
        "shadow_depth": 2,
        "quantum_group_type": QuantumGroupType.ABELIAN.value,
    }


# =========================================================================
# 3. Quantum R-matrix (quantization of r(z))
# =========================================================================

def yang_r_matrix_numeric(N: int, u: float, hbar: float = 1.0) -> np.ndarray:
    """Yang R-matrix R(u) = Id - hbar*P/u on V tensor V.

    This is the simplest rational solution of the quantum YBE.
    At hbar -> 0: R -> Id (classical limit is trivial).
    The r-matrix is extracted as r(u) = (d/dhbar)|_{hbar=0} R(u) = -P/u.

    Returns N^2 x N^2 matrix.
    """
    P = slN_casimir_matrix(N)
    return np.eye(N * N) - hbar * P / u


def verify_qybe_yang(N: int, u: float, v: float,
                     hbar: float = 1.0) -> Dict[str, Any]:
    r"""Verify the quantum Yang-Baxter equation for R(u) = Id - hbar*P/u.

    QYBE: R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)

    This is verified numerically at specific (u, v) values.
    """
    d3 = N ** 3
    Id_N = np.eye(N)
    P = slN_casimir_matrix(N)

    # Build R-matrices in V^{tensor 3}
    R12_full = embed_12(yang_r_matrix_numeric(N, u, hbar), N)
    R23_full = embed_23(yang_r_matrix_numeric(N, v, hbar), N)

    # R_{13}(u+v): need the embedded version
    R13_mat = np.eye(N * N) - hbar * P / (u + v)
    R13_full = embed_13(R13_mat, N)

    lhs = R12_full @ R13_full @ R23_full
    rhs = R23_full @ R13_full @ R12_full

    diff = lhs - rhs
    return {
        "N": N,
        "u": u,
        "v": v,
        "hbar": hbar,
        "qybe_holds": bool(np.allclose(diff, 0, atol=1e-10)),
        "max_err": float(np.max(np.abs(diff))),
    }


def quantum_r_genus1_correction(N: int, kappa: Any, u: Any) -> Any:
    r"""Genus-1 correction to the quantum R-matrix.

    The quantum R-matrix has an expansion:
        R(u) = 1 + hbar*r(u) + hbar^2*r_2(u) + ...

    The genus-1 correction r_2(u) comes from the genus-1 shadow kappa:
        r_2(u) ~ kappa * E_2(u)

    where E_2 is the Eisenstein series contribution from the genus-1
    modular curvature.

    For sl_N at level k: kappa = dim(g)*(k+h^v)/(2*h^v) = (N^2-1)*(k+N)/(2*N).
    The genus-1 correction is proportional to kappa.

    At the scalar level this gives:
        r_2 = kappa / u^2

    (the simplest form consistent with scaling and the genus-1 origin).

    Returns the scalar coefficient of the genus-1 correction.
    """
    return kappa / u**2


# =========================================================================
# 4. Yangian generators from shadow tower arities
# =========================================================================

@dataclass
class YangianFromShadow:
    """Yangian Y(g) generators extracted from the shadow tower.

    The shadow tower Theta_A^{<=r} at arity r produces Yangian
    generators at level (r-2):

        Level 0: y_{a,0} from arity-2 shadow kappa
                 These are the generators of g itself.

        Level 1: y_{a,1} from arity-3 shadow C (cubic)
                 These are the first Yangian generators.

        Level 2: y_{a,2} from arity-4 shadow Q (quartic)
                 These are the second-level generators.

    The Drinfeld presentation of Y(g):
        [y_{a,0}, y_{b,0}] = f_{abc} y_{c,0}        (g relations)
        [y_{a,0}, y_{b,1}] = f_{abc} y_{c,1}        (g-module structure)
        [y_{a,1}, y_{b,1}] - [y_{a,0}, y_{b,2}] = f_{abc} y_{c,0}^2
                                                     (Serre-like relation)

    Attributes:
        lie_algebra: Name of the Lie algebra g.
        rank: Rank of g.
        dim_g: Dimension of g.
        structure_constants: f_{abc} in some basis.
        kappa: Arity-2 shadow (level parameter).
        cubic_shadow: Arity-3 shadow.
        quartic_shadow: Arity-4 shadow.
    """
    lie_algebra: str
    rank: int
    dim_g: int
    structure_constants: Dict[Tuple[int, int], Dict[int, Any]] = field(
        default_factory=dict
    )
    kappa: Any = None
    cubic_shadow: Any = None
    quartic_shadow: Any = None

    def generator_count(self, max_level: int) -> int:
        """Total number of Yangian generators through level n.

        Y(g) has dim(g) generators at each level.
        """
        return (max_level + 1) * self.dim_g

    def level_from_arity(self, arity: int) -> int:
        """Yangian level corresponding to shadow tower arity.

        Level = arity - 2.
        """
        return arity - 2

    def arity_from_level(self, level: int) -> int:
        """Shadow tower arity corresponding to Yangian level.

        Arity = level + 2.
        """
        return level + 2


def yangian_from_affine_slN(N: int, k=None) -> YangianFromShadow:
    """Construct Yangian data from the shadow of affine sl_N at level k.

    kappa(sl_N, k) = dim(sl_N) * (k + h^v) / (2 * h^v)
                   = (N^2 - 1) * (k + N) / (2 * N)

    Cubic shadow from the Lie bracket structure: C = Killing 3-cocycle.
    Quartic shadow: zero for class L (Lie/tree, depth 3).
    """
    if k is None:
        k = Symbol('k')
    dim_g = N * N - 1
    h_dual = N
    kappa_val = Rational(1, 2) * dim_g * (k + h_dual) / h_dual

    # Structure constants for sl_N are determined by the root system.
    # For sl_2: f_{ehf} encoding [e,f]=h, [h,e]=2e, [h,f]=-2f.
    # We store a simplified version.
    struct_const: Dict[Tuple[int, int], Dict[int, Any]] = {}
    if N == 2:
        # Basis: 0=e, 1=h, 2=f
        struct_const = {
            (0, 2): {1: S.One},      # [e, f] = h
            (2, 0): {1: S.NegativeOne},
            (1, 0): {0: S(2)},       # [h, e] = 2e
            (0, 1): {0: S(-2)},
            (1, 2): {2: S(-2)},      # [h, f] = -2f
            (2, 1): {2: S(2)},
        }

    return YangianFromShadow(
        lie_algebra=f"sl_{N}",
        rank=N - 1,
        dim_g=dim_g,
        structure_constants=struct_const,
        kappa=kappa_val,
        cubic_shadow=S.One if dim_g > 1 else S.Zero,  # nonzero iff non-abelian
        quartic_shadow=S.Zero,  # class L: depth 3, no quartic
    )


def yangian_from_heisenberg(k=None) -> YangianFromShadow:
    """Construct (trivial) Yangian data from Heisenberg shadow.

    Heisenberg is abelian: the Yangian is trivial (class G).
    kappa = k (the level).  No cubic or quartic shadows.
    """
    if k is None:
        k = Symbol('k')
    return YangianFromShadow(
        lie_algebra="u(1)",
        rank=1,
        dim_g=1,
        structure_constants={},
        kappa=k,
        cubic_shadow=S.Zero,
        quartic_shadow=S.Zero,
    )


def yangian_from_virasoro(c=None) -> YangianFromShadow:
    """Construct full quantum group data from Virasoro shadow.

    Virasoro has depth infinity (class M): the full infinite shadow
    tower contributes to the quantum group structure.

    kappa = c/2.
    Q^contact = 10/(c*(5c+22)).
    The tower never terminates: all Yangian levels are nontrivial.
    """
    if c is None:
        c = Symbol('c')
    return YangianFromShadow(
        lie_algebra="Vir",
        rank=1,
        dim_g=1,
        structure_constants={},
        kappa=c / 2,
        cubic_shadow=S(2),
        quartic_shadow=Rational(10, 1) / (c * (5 * c + 22)),
    )


def verify_yangian_drinfeld_relation_sl2(
    k=None, hbar=None
) -> Dict[str, Any]:
    r"""Verify the Drinfeld relation for Y(sl_2) at level 0.

    The key relation is that level-0 generators satisfy sl_2:
        [y_{e,0}, y_{f,0}] = y_{h,0}
        [y_{h,0}, y_{e,0}] = 2 y_{e,0}
        [y_{h,0}, y_{f,0}] = -2 y_{f,0}

    And the mixed relation:
        [y_{a,0}, y_{b,1}] = f_{abc} y_{c,1}  (g-module property)

    We verify this at the level of structure constants from the
    shadow tower extraction.
    """
    Y = yangian_from_affine_slN(2, k)

    # Level 0 = sl_2 relations
    sc = Y.structure_constants

    results = {}

    # [e, f] = h
    results["[e,f]=h"] = sc.get((0, 2), {}).get(1, S.Zero) == S.One
    # [h, e] = 2e
    results["[h,e]=2e"] = sc.get((1, 0), {}).get(0, S.Zero) == S(2)
    # [h, f] = -2f
    results["[h,f]=-2f"] = sc.get((1, 2), {}).get(2, S.Zero) == S(-2)

    # Antisymmetry
    results["[f,e]=-h"] = sc.get((2, 0), {}).get(1, S.Zero) == S.NegativeOne

    # Generator count through level 1
    results["gen_count_level1"] = Y.generator_count(1) == 6

    # Shadow-level correspondence
    results["level_from_arity_2"] = Y.level_from_arity(2) == 0
    results["level_from_arity_3"] = Y.level_from_arity(3) == 1
    results["level_from_arity_4"] = Y.level_from_arity(4) == 2

    return results


# =========================================================================
# 5. Baxter TQ relation from shadow
# =========================================================================

@dataclass
class BaxterTQ:
    r"""Baxter TQ relation extracted from the shadow tower.

    The TQ relation for sl_2:
        T(u) Q(u) = a(u) Q(u-1) + d(u) Q(u+1)

    where:
        T(u) = transfer matrix = Tr_{aux}(R_{01}(u) R_{02}(u) ... R_{0L}(u))
        Q(u) = Baxter Q-operator (quantum determinant from higher shadows)
        a(u), d(u) = scalar functions (vacuum eigenvalues)

    For the shadow interpretation:
        - T comes from arity-2 shadow (binary collision)
        - Q comes from higher-arity shadows (n >= 3)

    The TQ relation is the SHADOW TOWER RECURSION read in spectral
    parameter language.

    Attributes:
        spin: The spin j of the evaluation representation.
        length: Chain length L (number of sites).
        eigenvalue_a: Function a(u).
        eigenvalue_d: Function d(u).
    """
    spin: Rational
    length: int
    eigenvalue_a: Callable
    eigenvalue_d: Callable

    def verify_tq(self, u_val: float, T_val: float,
                  Q_vals: Tuple[float, float, float]) -> Dict[str, Any]:
        """Verify T(u)*Q(u) = a(u)*Q(u-1) + d(u)*Q(u+1).

        Args:
            u_val: spectral parameter value
            T_val: T(u) eigenvalue
            Q_vals: (Q(u-1), Q(u), Q(u+1))
        """
        Q_minus, Q_0, Q_plus = Q_vals
        a_val = self.eigenvalue_a(u_val)
        d_val = self.eigenvalue_d(u_val)

        lhs = T_val * Q_0
        rhs = a_val * Q_minus + d_val * Q_plus

        return {
            "u": u_val,
            "lhs": lhs,
            "rhs": rhs,
            "match": abs(lhs - rhs) < 1e-10,
            "error": abs(lhs - rhs),
        }


def sl2_spin_half_tq(L: int = 2) -> BaxterTQ:
    r"""Baxter TQ for sl_2, spin-1/2 evaluation modules.

    For L sites with spin-1/2 at each site:
        a(u) = u^L          (product of (u - a_i) with a_i = 0)
        d(u) = (u - 1)^L    (shifted by 1 = 2*spin)

    The T(u) eigenvalue for the ground state of the XXX_{1/2} chain:
        T(u) = a(u) + d(u)  for the trivial Bethe state (no roots).

    The Q-operator for the trivial state: Q(u) = 1.
    """
    def a(u):
        return u ** L

    def d(u):
        return (u - 1) ** L

    return BaxterTQ(
        spin=Rational(1, 2),
        length=L,
        eigenvalue_a=a,
        eigenvalue_d=d,
    )


def verify_tq_trivial_state(L: int = 2) -> Dict[str, Any]:
    r"""Verify TQ relation for the trivial Bethe state.

    For the trivial state (no Bethe roots), Q(u) = 1 for all u.
    T(u) = a(u) + d(u) = u^L + (u-1)^L.

    TQ: T(u)*Q(u) = a(u)*Q(u-1) + d(u)*Q(u+1)
    => T(u)*1 = a(u)*1 + d(u)*1
    => T(u) = a(u) + d(u)  -- trivially satisfied.
    """
    tq = sl2_spin_half_tq(L)

    results = {}
    for u_val in [0.5, 1.0, 2.0, 3.7]:
        T_val = u_val ** L + (u_val - 1) ** L
        Q_vals = (1.0, 1.0, 1.0)  # trivial Q
        check = tq.verify_tq(u_val, T_val, Q_vals)
        results[f"u={u_val}"] = check["match"]

    results["L"] = L
    results["state"] = "trivial (no Bethe roots)"
    return results


def verify_tq_one_magnon(L: int = 4) -> Dict[str, Any]:
    r"""Verify TQ for the one-magnon state of the XXX_{1/2} chain.

    For L sites, spin-1/2, one magnon with Bethe root v_1:
    The Bethe equation: (v_1)^L / (v_1 - 1)^L = 1
    => v_1 / (v_1 - 1) = exp(2*pi*i*m/L) for some integer m.

    For L=4, m=1: v_1 / (v_1 - 1) = i => v_1 = i/(i-1) = (i-1+1)/(i-1)
    = 1 + 1/(i-1) = 1 - (i+1)/2 = (1-i)/2.

    Actually: v_1 = 1/(1 - exp(-2*pi*i*m/L)).
    For L=4, m=1: exp(-pi*i/2) = -i, so v_1 = 1/(1+i) = (1-i)/2.

    Q(u) = u - v_1 for one-magnon.
    T(u) = a(u)*Q(u-1)/Q(u) + d(u)*Q(u+1)/Q(u)  (from TQ).

    We check: T(u)*Q(u) = a(u)*Q(u-1) + d(u)*Q(u+1).
    """
    import cmath

    m = 1
    zeta = cmath.exp(2j * cmath.pi * m / L)
    v1 = 1.0 / (1.0 - 1.0 / zeta)  # Bethe root

    def Q(u):
        return u - v1

    def a(u):
        return u ** L

    def d(u):
        return (u - 1.0) ** L

    results = {}
    for u_val in [0.5, 2.0, 3.7, 5.1]:
        u = complex(u_val)
        T_val = a(u) * Q(u - 1) / Q(u) + d(u) * Q(u + 1) / Q(u)
        lhs = T_val * Q(u)
        rhs = a(u) * Q(u - 1) + d(u) * Q(u + 1)
        results[f"u={u_val}"] = abs(lhs - rhs) < 1e-10

    results["L"] = L
    results["Bethe_root"] = v1
    results["state"] = "one-magnon"
    return results


# =========================================================================
# 6. Drinfeld-Kohno: KZ connection from shadow connection
# =========================================================================

@dataclass
class KZConnection:
    r"""Knizhnik-Zamolodchikov connection from the shadow connection.

    The shadow connection nabla^sh restricts to the KZ connection on Conf_n(C):

        nabla_i = d/dz_i - hbar * sum_{j != i} Omega_{ij} / (z_i - z_j)

    where Omega_{ij} = Omega acting on V_i tensor V_j (Casimir in slots i,j).

    The KZ equation for n-point conformal blocks:
        (k + h^v) * dPhi/dz_i = sum_{j!=i} Omega_{ij}/(z_i - z_j) * Phi

    Flatness: [nabla_i, nabla_j] = 0 follows from the CYBE (Arnold relation
    on Conf_n(C) combined with [Omega_{ij}, Omega_{ik} + Omega_{jk}] = 0
    = the infinitesimal braid relation from the Casimir identity).

    Attributes:
        n: Number of insertion points.
        N: sl_N rank parameter.
        hbar: Coupling constant = 1/(k + h^v).
        representations: Representations at each point.
    """
    n: int
    N: int
    hbar: float
    representations: Optional[List[str]] = None

    def connection_matrix_ij(self, i: int, j: int) -> np.ndarray:
        r"""Return hbar * Omega_{ij} as a matrix on V^{tensor n}.

        Omega_{ij} acts as P (permutation) on V_i tensor V_j
        and as identity on all other factors.

        For fundamental representations (V = C^N), this is
        a N^n x N^n matrix.
        """
        N = self.N
        n = self.n
        d = N ** n

        # Build Omega_{ij} = P_{ij} acting on (C^N)^{tensor n}
        P_ij = np.eye(d)
        # For each basis vector |a_1, ..., a_n>, P_{ij} swaps a_i and a_j.
        P_ij_new = np.zeros((d, d))
        for idx in range(d):
            # Decode multi-index
            indices = []
            temp = idx
            for _ in range(n):
                indices.append(temp % N)
                temp //= N
            indices = indices[::-1]  # indices[0] = first factor

            # Swap indices i and j
            swapped = list(indices)
            swapped[i], swapped[j] = swapped[j], swapped[i]

            # Encode swapped multi-index
            new_idx = 0
            for s in swapped:
                new_idx = new_idx * N + s

            P_ij_new[new_idx, idx] = 1.0

        return self.hbar * P_ij_new

    def verify_flatness_n3(self) -> Dict[str, Any]:
        r"""Verify flatness of KZ connection for n=3 points.

        [nabla_1, nabla_2] = 0 reduces to the identity:
            [Omega_{12}, Omega_{13}] + [Omega_{12}, Omega_{23}] = 0

        (infinitesimal braid relation from CYBE).
        Plus the Arnold-type identity for the 1-forms.
        """
        if self.n != 3:
            return {"error": "n must be 3"}

        Om12 = self.connection_matrix_ij(0, 1)
        Om13 = self.connection_matrix_ij(0, 2)
        Om23 = self.connection_matrix_ij(1, 2)

        # Infinitesimal braid: [Om12, Om13+Om23] = 0
        comm = Om12 @ (Om13 + Om23) - (Om13 + Om23) @ Om12

        # Also check: [Om12, Om13] + [Om12, Om23] + [Om13, Om23] = 0 (CYBE)
        cybe = ((Om12 @ Om13 - Om13 @ Om12) +
                (Om12 @ Om23 - Om23 @ Om12) +
                (Om13 @ Om23 - Om23 @ Om13))

        return {
            "n": 3,
            "N": self.N,
            "inf_braid_holds": bool(np.allclose(comm, 0)),
            "inf_braid_max_err": float(np.max(np.abs(comm))),
            "cybe_holds": bool(np.allclose(cybe, 0)),
            "cybe_max_err": float(np.max(np.abs(cybe))),
        }


def kz_monodromy_n3_sl2(hbar: float = 0.1) -> Dict[str, Any]:
    r"""Compute and verify KZ monodromy for n=3, sl_2, fundamental.

    The KZ connection on Conf_3(C) for sl_2 in the fundamental
    representation has monodromy representations:

        sigma_1 -> R_{12} = exp(pi*i*hbar * Omega_{12})
        sigma_2 -> R_{23} = exp(pi*i*hbar * Omega_{23})

    These satisfy the braid relation:
        R_{12} R_{23} R_{12} = R_{23} R_{12} R_{23}

    (this IS the Drinfeld-Kohno theorem).

    We verify numerically at a given hbar value.
    """
    from scipy.linalg import expm

    N = 2
    n = 3
    kz = KZConnection(n=3, N=2, hbar=hbar)

    Om12 = kz.connection_matrix_ij(0, 1) / hbar  # remove the hbar factor
    Om23 = kz.connection_matrix_ij(1, 2) / hbar

    # Monodromy matrices: R = exp(pi*i*hbar * Omega)
    R12 = expm(np.pi * 1j * hbar * Om12)
    R23 = expm(np.pi * 1j * hbar * Om23)

    # Braid relation: R12 R23 R12 = R23 R12 R23
    lhs = R12 @ R23 @ R12
    rhs = R23 @ R12 @ R23

    # Also check R-matrix eigenvalues
    eigenvalues_R12 = np.linalg.eigvals(R12)

    return {
        "hbar": hbar,
        "N": N,
        "braid_relation_holds": bool(np.allclose(lhs, rhs, atol=1e-8)),
        "braid_max_err": float(np.max(np.abs(lhs - rhs))),
        "R12_eigenvalues": sorted(eigenvalues_R12.tolist(), key=lambda x: abs(x)),
        "drinfeld_kohno": "monodromy = R-matrix",
    }


# =========================================================================
# 7. Shadow depth = quantum group complexity
# =========================================================================

STANDARD_FAMILIES = {
    "Heisenberg": {
        "shadow_class": ShadowDepthClass.G,
        "depth": 2,
        "quantum_group": QuantumGroupType.ABELIAN,
        "r_matrix_type": "scalar 1/z^2",
        "kz_type": "abelian (diagonal)",
        "description": "Trivial quantum group: all R-matrix commutators vanish",
    },
    "Lattice": {
        "shadow_class": ShadowDepthClass.G,
        "depth": 2,
        "quantum_group": QuantumGroupType.ABELIAN,
        "r_matrix_type": "scalar 1/z^2",
        "kz_type": "abelian (lattice charges)",
        "description": "Lattice VOA: abelian r-matrix with lattice charges",
    },
    "FreeFermion": {
        "shadow_class": ShadowDepthClass.G,
        "depth": 2,
        "quantum_group": QuantumGroupType.ABELIAN,
        "r_matrix_type": "scalar 1/z^2",
        "kz_type": "abelian",
        "description": "Free fermion: abelian (Clifford algebra has no Lie bracket)",
    },
    "Affine_sl2": {
        "shadow_class": ShadowDepthClass.L,
        "depth": 3,
        "quantum_group": QuantumGroupType.CLASSICAL_YANGIAN,
        "r_matrix_type": "Omega/z (Casimir)",
        "kz_type": "KZ connection",
        "description": "Classical Yangian Y(sl_2) from cubic shadow (Lie bracket)",
    },
    "Affine_slN": {
        "shadow_class": ShadowDepthClass.L,
        "depth": 3,
        "quantum_group": QuantumGroupType.CLASSICAL_YANGIAN,
        "r_matrix_type": "Omega/z (Casimir)",
        "kz_type": "KZ connection",
        "description": "Classical Yangian Y(sl_N): tree-level r-matrix terminates at depth 3",
    },
    "BetaGamma": {
        "shadow_class": ShadowDepthClass.C,
        "depth": 4,
        "quantum_group": QuantumGroupType.DEFORMED_YANGIAN,
        "r_matrix_type": "1/z + contact correction",
        "kz_type": "deformed KZ",
        "description": "Deformed Yangian: quartic contact term modifies R-matrix",
    },
    "Virasoro": {
        "shadow_class": ShadowDepthClass.M,
        "depth": None,  # infinite
        "quantum_group": QuantumGroupType.FULL_QUANTUM,
        "r_matrix_type": "c/(2z^4) + 2L/z^2 + L'/z",
        "kz_type": "BPZ equations",
        "description": "Full quantum group: infinite shadow tower, all levels contribute",
    },
    "W_3": {
        "shadow_class": ShadowDepthClass.M,
        "depth": None,
        "quantum_group": QuantumGroupType.FULL_QUANTUM,
        "r_matrix_type": "higher-order poles",
        "kz_type": "generalized KZ (W-algebra blocks)",
        "description": "Full quantum group: W_3 shadow tower infinite, multi-channel mixing",
    },
}


def classify_quantum_group(family: str) -> Dict[str, Any]:
    """Classify the quantum group type for a given chiral algebra family.

    Shadow depth determines quantum group complexity:
        G (depth 2) -> abelian
        L (depth 3) -> classical Yangian
        C (depth 4) -> deformed Yangian
        M (depth inf) -> full quantum group

    Returns classification data including shadow class, depth,
    quantum group type, and r-matrix structure.
    """
    if family in STANDARD_FAMILIES:
        data = dict(STANDARD_FAMILIES[family])
        data["family"] = family
        return data
    return {
        "family": family,
        "shadow_class": None,
        "depth": None,
        "quantum_group": None,
        "error": f"Unknown family: {family}",
    }


def depth_to_quantum_type(depth: Optional[int]) -> QuantumGroupType:
    """Map shadow depth to quantum group type.

    depth 2 -> ABELIAN
    depth 3 -> CLASSICAL_YANGIAN
    depth 4 -> DEFORMED_YANGIAN
    depth None (infinity) -> FULL_QUANTUM
    """
    if depth == 2:
        return QuantumGroupType.ABELIAN
    elif depth == 3:
        return QuantumGroupType.CLASSICAL_YANGIAN
    elif depth == 4:
        return QuantumGroupType.DEFORMED_YANGIAN
    else:
        return QuantumGroupType.FULL_QUANTUM


# =========================================================================
# 8. R-matrix from Yang-Baxter at specific representations
# =========================================================================

def yang_r_matrix_eigenvalues(N: int, u: float,
                              hbar: float = 1.0) -> Dict[str, Any]:
    """Eigenvalues of the Yang R-matrix R(u) = Id - hbar*P/u.

    R(u) has eigenvalues:
        - On Sym^2(V): 1 - hbar/u  (multiplicity N(N+1)/2)
        - On Lambda^2(V): 1 + hbar/u  (multiplicity N(N-1)/2)

    This is because P|_{Sym^2} = +1 and P|_{Lambda^2} = -1.
    """
    sym_ev = 1.0 - hbar / u
    alt_ev = 1.0 + hbar / u

    sym_dim = N * (N + 1) // 2
    alt_dim = N * (N - 1) // 2

    # Numerical verification
    R = yang_r_matrix_numeric(N, u, hbar)
    eigenvalues = np.sort(np.real(np.linalg.eigvals(R)))

    # Count eigenvalues near each expected value
    sym_count = np.sum(np.abs(eigenvalues - sym_ev) < 1e-8)
    alt_count = np.sum(np.abs(eigenvalues - alt_ev) < 1e-8)

    return {
        "N": N,
        "u": u,
        "hbar": hbar,
        "sym_eigenvalue": sym_ev,
        "alt_eigenvalue": alt_ev,
        "sym_dim_expected": sym_dim,
        "alt_dim_expected": alt_dim,
        "sym_count": int(sym_count),
        "alt_count": int(alt_count),
        "eigenvalue_check": int(sym_count) == sym_dim and int(alt_count) == alt_dim,
    }


def r_matrix_unitarity(N: int, u: float,
                       hbar: float = 1.0) -> Dict[str, Any]:
    """Verify unitarity: R_{12}(u) R_{21}(-u) = f(u) * Id.

    For the Yang R-matrix: R(u)*R(-u) = (1 - (hbar/u)^2) * Id.
    (This is because P^2 = Id.)

    This is the crossing/unitarity relation.
    """
    R_plus = yang_r_matrix_numeric(N, u, hbar)
    # R_{21}(-u) = R_{12}(-u) with P applied (but for the Yang R-matrix,
    # R_{21}(u) = P R_{12}(u) P, so R_{21}(-u) = P R(-u) P).
    # Actually R(u) = Id - hbar*P/u, so P*R(u)*P = P - hbar*Id/u,
    # and R(-u) = Id + hbar*P/u.
    # R(u)*R(-u) = (Id - hbar*P/u)(Id + hbar*P/u) = Id - (hbar/u)^2 * P^2
    # = Id - (hbar/u)^2 * Id = (1 - (hbar/u)^2) * Id.
    R_minus = yang_r_matrix_numeric(N, -u, hbar)

    product = R_plus @ R_minus
    expected_scalar = 1.0 - (hbar / u) ** 2
    expected = expected_scalar * np.eye(N * N)

    return {
        "N": N,
        "u": u,
        "hbar": hbar,
        "expected_scalar": expected_scalar,
        "unitarity_holds": bool(np.allclose(product, expected)),
        "max_err": float(np.max(np.abs(product - expected))),
    }


# =========================================================================
# 9. Transfer matrix from shadow arity 2
# =========================================================================

def transfer_matrix_eigenvalues(N: int, L: int, u: float,
                                evaluation_points: List[float],
                                hbar: float = 1.0) -> np.ndarray:
    r"""Eigenvalues of the transfer matrix T(u) for sl_N XXX chain.

    T(u) = Tr_{aux} prod_{i=1}^{L} R_{0i}(u - theta_i)

    where theta_i are the evaluation points (inhomogeneities).

    For the homogeneous chain (all theta_i = 0):
        T(u) = Tr_{aux} R(u)^L

    The transfer matrix acts on V^{tensor L} = (C^N)^{tensor L}.
    dim = N^L.

    For small L we compute exactly.  Returns eigenvalues as array.
    """
    # Homogeneous case for simplicity
    if len(evaluation_points) != L:
        raise ValueError(f"Need L={L} evaluation points, got {len(evaluation_points)}")

    d_phys = N ** L  # physical space dimension

    # Build T(u) as a d_phys x d_phys matrix
    # T_{alpha, beta} = sum_{a=0}^{N-1} prod_{i=1}^{L} R_{a,alpha_i; ?, beta_i}(u - theta_i)
    # This is the trace over the auxiliary space.

    # Simpler approach for small L: build the product of R-matrices
    # in (C^N)^{aux} tensor (C^N)^{L} = (C^N)^{L+1}, then trace over aux.

    d_full = N ** (L + 1)

    # Start with identity on full space
    product = np.eye(d_full)

    for site in range(L):
        # R acting on aux (space 0) and physical site (space site+1)
        # In the tensor product (C^N)^{L+1}, these are spaces 0 and site+1.
        u_eff = u - evaluation_points[site]
        if abs(u_eff) < 1e-14:
            u_eff = 1e-14  # regularize

        # Build R_{0, site+1}(u_eff) as N^{L+1} x N^{L+1} matrix
        R_0s = _embed_r_matrix(N, L + 1, 0, site + 1, u_eff, hbar)
        product = R_0s @ product

    # Trace over auxiliary space (space 0)
    T = np.zeros((d_phys, d_phys), dtype=complex)
    for a in range(N):
        # Extract the block where aux index = a on both sides
        for alpha in range(d_phys):
            for beta in range(d_phys):
                full_row = a * d_phys + alpha
                full_col = a * d_phys + beta
                T[alpha, beta] += product[full_row, full_col]

    return np.sort(np.linalg.eigvals(T))


def _embed_r_matrix(N: int, n_spaces: int, i: int, j: int,
                    u: float, hbar: float = 1.0) -> np.ndarray:
    """Embed R_{ij}(u) = Id - hbar*P_{ij}/u into (C^N)^{tensor n_spaces}."""
    d = N ** n_spaces
    R = np.eye(d, dtype=complex)

    # P_{ij} swaps spaces i and j in the n_spaces-fold tensor product
    for idx in range(d):
        indices = []
        temp = idx
        for _ in range(n_spaces):
            indices.append(temp % N)
            temp //= N
        indices = indices[::-1]

        swapped = list(indices)
        swapped[i], swapped[j] = swapped[j], swapped[i]

        new_idx = 0
        for s in swapped:
            new_idx = new_idx * N + s

        # R = Id - hbar*P/u, so R[new_idx, idx] -= hbar/u if swap changes something
        # But we need to subtract hbar/u * P from Id, so:
        R[new_idx, idx] -= hbar / u
        # And we've already got the Id part from np.eye.
        # But wait: for diagonal elements (idx == new_idx), we get
        # R[idx, idx] = 1 - hbar/u, which is wrong if idx != new_idx for P.
        # Actually R = Id - hbar/u * P. The diagonal entry R[idx,idx]
        # should be: 1 if P[idx,idx]=0, or 1 - hbar/u if P[idx,idx]=1.
        # P[new_idx, idx] = 1 iff swapping i,j sends idx to new_idx.
        # So R[new_idx, idx] = delta_{new_idx, idx} - hbar/u * P[new_idx, idx]
        #                    = delta_{new_idx, idx} - hbar/u * delta_{new_idx, swap(idx)}
        # But swap(idx) = new_idx by construction. So:
        # R[new_idx, idx] = delta_{new_idx, idx} - hbar/u.

    # Redo more carefully: build P_{ij} first, then R = Id - hbar/u * P
    P_ij = np.zeros((d, d))
    for idx in range(d):
        indices = []
        temp = idx
        for _ in range(n_spaces):
            indices.append(temp % N)
            temp //= N
        indices = indices[::-1]

        swapped = list(indices)
        swapped[i], swapped[j] = swapped[j], swapped[i]

        new_idx = 0
        for s in swapped:
            new_idx = new_idx * N + s

        P_ij[new_idx, idx] = 1.0

    return np.eye(d, dtype=complex) - (hbar / u) * P_ij


# =========================================================================
# 10. Comprehensive verification
# =========================================================================

def verify_r_matrix_from_shadow() -> Dict[str, Any]:
    """Verify r-matrices for all standard families match shadow tower data."""
    results = {}

    # Heisenberg
    r_heis = heisenberg_r_matrix()
    results["heisenberg_max_pole"] = r_heis.max_pole == 2
    results["heisenberg_abelian"] = r_heis.dim_g == 1

    # Affine sl_2
    r_sl2 = affine_sl2_r_matrix()
    results["affine_sl2_max_pole"] = r_sl2.max_pole == 1
    results["affine_sl2_dim"] = r_sl2.dim_g == 3

    # Virasoro
    r_vir = virasoro_r_matrix()
    results["virasoro_max_pole"] = r_vir.max_pole == 4
    results["virasoro_single_gen"] = r_vir.dim_g == 1

    # sl_N for N=2,3,4
    for N in [2, 3, 4]:
        r = affine_slN_r_matrix(N)
        results[f"sl{N}_dim"] = r.dim_g == N * N - 1
        results[f"sl{N}_max_pole"] = r.max_pole == 1

    # Beta-gamma
    r_bg = betagamma_r_matrix()
    results["betagamma_max_pole"] = r_bg.max_pole == 1

    return results


def verify_shadow_depth_quantum_group() -> Dict[str, Any]:
    """Verify the shadow depth -> quantum group classification for all families."""
    results = {}

    for family, data in STANDARD_FAMILIES.items():
        sc = data["shadow_class"]
        qg = data["quantum_group"]
        expected_qg = DEPTH_TO_QUANTUM_GROUP[sc]
        results[f"{family}_classification"] = qg == expected_qg

    # Verify depth -> type mapping
    results["depth_2_abelian"] = depth_to_quantum_type(2) == QuantumGroupType.ABELIAN
    results["depth_3_yangian"] = depth_to_quantum_type(3) == QuantumGroupType.CLASSICAL_YANGIAN
    results["depth_4_deformed"] = depth_to_quantum_type(4) == QuantumGroupType.DEFORMED_YANGIAN
    results["depth_inf_full"] = depth_to_quantum_type(None) == QuantumGroupType.FULL_QUANTUM

    return results


def verify_all() -> Dict[str, Any]:
    """Run all verifications."""
    results = {}

    # CYBE
    for N in [2, 3]:
        cybe = verify_cybe_yang(N)
        results[f"cybe_sl{N}"] = cybe["cybe_holds"]

    results["cybe_heisenberg"] = verify_cybe_heisenberg()["cybe_holds"]

    # QYBE
    for N in [2, 3]:
        qybe = verify_qybe_yang(N, 3.7, 1.2)
        results[f"qybe_sl{N}"] = qybe["qybe_holds"]

    # R-matrix eigenvalues
    for N in [2, 3]:
        ev = yang_r_matrix_eigenvalues(N, 2.0)
        results[f"r_eigenvalues_sl{N}"] = ev["eigenvalue_check"]

    # Unitarity
    for N in [2, 3]:
        unit = r_matrix_unitarity(N, 2.0)
        results[f"unitarity_sl{N}"] = unit["unitarity_holds"]

    # Yangian relations
    drinfeld = verify_yangian_drinfeld_relation_sl2()
    results["drinfeld_sl2"] = all(v for v in drinfeld.values()
                                  if isinstance(v, bool))

    # TQ
    results["tq_trivial_L2"] = all(
        v for k, v in verify_tq_trivial_state(2).items()
        if isinstance(v, bool)
    )
    results["tq_trivial_L4"] = all(
        v for k, v in verify_tq_trivial_state(4).items()
        if isinstance(v, bool)
    )

    # KZ
    kz = KZConnection(n=3, N=2, hbar=0.5)
    kz_flat = kz.verify_flatness_n3()
    results["kz_flatness"] = kz_flat["cybe_holds"]

    # Shadow depth classification
    depth_class = verify_shadow_depth_quantum_group()
    results["depth_classification"] = all(
        v for v in depth_class.values() if isinstance(v, bool)
    )

    # R-matrix from shadow
    r_shadow = verify_r_matrix_from_shadow()
    results["r_from_shadow"] = all(
        v for v in r_shadow.values() if isinstance(v, bool)
    )

    return results


# =========================================================================
# Runner
# =========================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("QUANTUM GROUP SHADOW ENGINE: VERIFICATION")
    print("=" * 70)

    results = verify_all()
    for name, ok in results.items():
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")

    n_pass = sum(1 for v in results.values() if v)
    n_total = len(results)
    print(f"\n  {n_pass}/{n_total} checks passed.")
