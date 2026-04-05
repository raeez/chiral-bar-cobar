r"""BC-84: Categorical zeta functions at roots of unity.

Mathematical foundation
-----------------------
At q = exp(2*pi*i/(k+h^vee)), the quantum group U_q(g) has FINITELY many
irreducible representations: the integrable highest-weight modules of the
affine algebra hat{g} at level k.  The categorical zeta TRUNCATES to a
finite sum, the "modular categorical zeta":

    zeta^{mod}_{g,k}(s) = sum_{lambda integrable, nontrivial} dim_q(V_lambda)^{-s}

where dim_q is the quantum dimension (= ratio of S-matrix entries).

KEY IDENTITY (sl_2 at level k):
    Integrable reps: V_0, V_1, ..., V_k with quantum dimensions
    dim_q V_j = [j+1]_q = sin((j+1)*pi/(k+2)) / sin(pi/(k+2)),
    where q = exp(2*pi*i/(k+2)).

    The modular categorical zeta (excluding trivial V_0):
    zeta^{mod}_{sl_2,k}(s) = sum_{j=1}^{k} [j+1]_q^{-s}

    As k -> infinity: [j+1]_q -> j+1, so
    zeta^{mod}_{sl_2,k}(s) -> sum_{j=1}^{infty} (j+1)^{-s} = zeta(s) - 1.

VERLINDE FORMULA CONNECTION:
    The fusion ring at level k has structure constants N_{ij}^l given by:
    N_{ij}^l = sum_m S_{im} S_{jm} S*_{lm} / S_{0m}
    where S is the modular S-matrix:
    S_{jl} = sqrt(2/(k+2)) * sin((j+1)(l+1)*pi/(k+2))

    The categorical zeta via the S-matrix:
    zeta^{Ver}_{g,k}(s) = sum_lambda (S_{0,lambda}/S_{0,0})^{-s}

SL_3 AT LEVEL K:
    Integrable weights: (a,b) with a,b >= 0 and a+b <= k.
    Quantum dimension via the Weyl-Kac formula with q = exp(2*pi*i/(k+3)).
    dim_q V(a,b) = product over positive roots alpha of
    sin(<lambda+rho, alpha>*pi/(k+3)) / sin(<rho, alpha>*pi/(k+3))

G_2 AT LEVEL K:
    Integrable weights: (a,b) with a + 2b <= k (long root normalization:
    the comarks are (2,1), so integrability is a*theta_1^vee + b*theta_2^vee <= k
    where theta_1^vee = 2 (short coroot) and theta_2^vee = 1 (long coroot);
    but in Bourbaki convention for G_2 with alpha_1 short, alpha_2 long, the
    dual Coxeter labels are a_1^vee = 1, a_2^vee = 1 for SIMPLE coroots,
    while the highest coroot theta^vee has expansion 3*alpha_1^vee + 2*alpha_2^vee
    in simple coroot basis.  Integrability: <lambda, theta^vee> <= k, i.e.
    3a + 2b <= k if we use <omega_i, alpha_j^vee> = delta_{ij} (fund. weights
    pair integrally with SIMPLE coroots), but theta^vee = 3*alpha_1^vee + 2*alpha_2^vee,
    so <a*omega_1 + b*omega_2, theta^vee> = 3a + 2b.  But wait: this is wrong
    for Bourbaki G_2 where alpha_1 is SHORT.  The CORRECT condition for G_2
    (Bourbaki: alpha_1 short, alpha_2 long) is:
      <lambda, theta^vee> = 2a + b <= k
    since the highest root is theta = 3*alpha_1 + 2*alpha_2 and
    theta^vee = (2/||theta||^2)*theta; with ||short||^2 = 1, ||long||^2 = 3,
    ||theta||^2 = ||3*alpha_1 + 2*alpha_2||^2 ... Actually, the simplest approach:
    the comarks of G_2 in Bourbaki convention (alpha_1 short) are a_1^vee = 1,
    a_2^vee = 1, so theta^vee = 2*alpha_1^vee + alpha_2^vee (checking:
    h^vee = 1 + sum a_i^vee = 1 + 1 + 1 ... no, h^vee = 4 for G_2).

    RESOLVED: For G_2 in Bourbaki convention (alpha_1 short, alpha_2 long),
    h^vee = 4.  The comarks are a_0^vee = 1, a_1^vee = 2, a_2^vee = 1.
    (Note: a_0^vee is the affine node.)  The integrability condition
    sum_i a_i^vee * lambda_i <= k gives 2*a + 1*b <= k for lambda = a*omega_1 + b*omega_2,
    since <omega_i, alpha_j^vee> = delta_{ij} and theta^vee = a_1^vee * alpha_1^vee + a_2^vee * alpha_2^vee
    = 2*alpha_1^vee + alpha_2^vee.

    CORRECTION: The Kac labels (marks) and comarks for G_2 depend on the
    convention.  In Kac's "Infinite-dimensional Lie algebras", Table Aff 1,
    for G_2^(1): the marks are a_0=1, a_1=2, a_2=3 and the comarks are
    a_0^vee=1, a_1^vee=1, a_2^vee=1.  So theta = 2*alpha_1 + 3*alpha_2
    (highest root in terms of simple roots of G_2 with alpha_1 SHORT) and
    theta^vee = alpha_1^vee + alpha_2^vee.  The integrability condition is
    <lambda, theta^vee> = a + b <= k.

    WAIT: This gives h^vee = 1 + 1 + 1 = 3, but h^vee(G_2) = 4.
    Let me recheck.  Kac Table Aff 1, row G_2^(1):
    Dynkin diagram: alpha_0 -- alpha_1 ==> alpha_2 (triple bond, arrow toward alpha_2)
    Wait: G_2 has the triple bond.  In G_2^(1), the extended Dynkin diagram is:
      0 --- 1 <<< 2  (triple bond from 1 to 2, short root is 1)
    Marks: a_0=1, a_1=2, a_2=3.  So theta = 2*alpha_1 + 3*alpha_2 (wrong for G_2
    where highest root should be in terms of simple roots).

    Actually: For G_2, the positive roots are:
    alpha_1, alpha_2, alpha_1+alpha_2, 2alpha_1+alpha_2, 3alpha_1+alpha_2, 3alpha_1+2alpha_2.
    The highest root theta = 3*alpha_1 + 2*alpha_2 (alpha_1 short, alpha_2 long, Bourbaki).
    The marks: theta = a_1*alpha_1 + a_2*alpha_2, so a_1=3, a_2=2.
    But Kac says a_0=1, a_1=2, a_2=3... There is a labeling issue.

    FINAL RESOLUTION: Use the NUMERICAL condition directly.
    For G_2 (h^vee = 4), q = exp(2*pi*i/(k+4)).  The integrability condition
    is a + b <= k where (a,b) are Dynkin labels.  This is because the comarks
    of the SIMPLE roots of G_2 in the numbering where alpha_1 is short are
    a_1^vee = 1, a_2^vee = 1 (since both have the same comark contribution to
    theta^vee).  WRONG AGAIN: h^vee = 1 + sum a_i^vee = 1 + a_1^vee + a_2^vee = 4
    gives a_1^vee + a_2^vee = 3, not 2.

    I will use the EXPLICIT positive root system and Weyl-Kac quantum dimension
    formula, which is unambiguous.  The integrability condition will be determined
    by enumerating weights for which the quantum dimension is real and positive.

LEVEL-RANK DUALITY:
    sl_N at level k <-> sl_k at level N.  The modular tensor categories are
    related but NOT identical; the quantum dimensions satisfy a nontrivial
    correspondence (not simple equality of the zeta functions).

SHADOW-MODULAR COMPARISON:
    The shadow characteristic kappa(sl_2, k) = dim(sl_2)*(k+h^vee)/(2*h^vee)
    = 3*(k+2)/4.  The modular categorical zeta at level k and the shadow zeta
    at kappa = 3(k+2)/4 probe different aspects of the same algebra.

Verification paths
------------------
    Path 1: k -> infinity limit recovers categorical zeta (= Riemann zeta for sl_2)
    Path 2: Quantum dimension formula vs Verlinde S-matrix (must agree)
    Path 3: Level-rank duality check
    Path 4: Fusion ring rank = #integrable weights (independent combinatorial count)
    Path 5: zeta^{mod}(0) = #nontrivial reps (dimension count)

References
----------
    Kac, "Infinite-dimensional Lie algebras", Cambridge 1990.
    Di Francesco-Mathieu-Senechal, "Conformal Field Theory", Springer 1997.
    Bakalov-Kirillov, "Lectures on Tensor Categories and Modular Functors", AMS 2001.
    thm:categorical-cg-all-types (yangians_drinfeld_kohno.tex)
    quantum_group_root_of_unity_engine.py (this repository)
    bc_categorical_zeta_engine.py (this repository)
    concordance.tex: MC3 status
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np


# =========================================================================
# 0. Root system data for quantum dimension computation
# =========================================================================

# Positive roots of simple Lie algebras, in simple root coordinates.
# Each root alpha = sum c_i * alpha_i is stored as tuple (c_1, ..., c_r).

def _sl2_positive_roots() -> List[Tuple[int]]:
    """Positive roots of sl_2 = A_1: just alpha_1."""
    return [(1,)]


def _sl3_positive_roots() -> List[Tuple[int, int]]:
    """Positive roots of sl_3 = A_2: alpha_1, alpha_2, alpha_1+alpha_2."""
    return [(1, 0), (0, 1), (1, 1)]


def _g2_positive_roots() -> List[Tuple[int, int]]:
    """Positive roots of G_2 (alpha_1 short, alpha_2 long, Bourbaki).

    The 6 positive roots are:
    alpha_1, alpha_2, alpha_1+alpha_2, 2*alpha_1+alpha_2,
    3*alpha_1+alpha_2, 3*alpha_1+2*alpha_2.
    """
    return [
        (1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)
    ]


def _slN_positive_roots(N: int) -> List[Tuple[int, ...]]:
    """Positive roots of sl_N = A_{N-1}.

    The positive roots are e_i - e_j for 1 <= i < j <= N.
    In simple root coordinates: alpha_{i,j} = alpha_i + alpha_{i+1} + ... + alpha_{j-1}.
    """
    rank = N - 1
    roots = []
    for i in range(rank):
        for j in range(i, rank):
            root = tuple(1 if i <= m <= j else 0 for m in range(rank))
            roots.append(root)
    return roots


# Weyl vector rho in fundamental weight coordinates: rho = (1, 1, ..., 1).
# The inner product <lambda, alpha> with lambda in fund. wt. coordinates
# and alpha in simple root coordinates is: sum_i lambda_i * alpha_i
# (because <omega_i, alpha_j> uses the Cartan matrix; but <omega_i, alpha_j^vee>
# = delta_{ij}, and for simply-laced types alpha = alpha^vee).
#
# For NON-simply-laced types (G_2, B_n, C_n, F_4), we need the
# symmetrized inner product.  The quantum dimension formula at level k uses:
#
# dim_q V_lambda = prod_{alpha > 0} sin(pi * <lambda+rho, alpha^vee> / (k+h^vee))
#                                  / sin(pi * <rho, alpha^vee> / (k+h^vee))
#
# where the pairing <omega_i, alpha_j^vee> = delta_{ij} (by definition of
# fundamental weights as dual basis to simple coroots).
#
# For the positive coroots alpha^vee = (2/<alpha,alpha>) * alpha:
# - Simply-laced (A_n, D_n, E_n): alpha^vee = alpha.
# - G_2: alpha_1^vee = alpha_1 (short root, ||alpha_1||^2 = 2/3 or normalized),
#         alpha_2^vee = alpha_2 (long root).
#   Actually, coroots in terms of simple coroots: the simple coroots ARE
#   alpha_1^vee and alpha_2^vee.  The positive coroots are the images of
#   positive roots under alpha -> alpha^vee.


def _sl_coroots_in_coroot_coords(N: int) -> List[Tuple[int, ...]]:
    """Positive coroots of sl_N in simple coroot coordinates.

    For sl_N (simply-laced), coroots = roots in the same coordinates.
    """
    return _slN_positive_roots(N)


def _g2_coroots_in_coroot_coords() -> List[Tuple[int, int]]:
    """Positive coroots of G_2 in simple coroot coordinates.

    G_2 roots (alpha_1 short, alpha_2 long, Bourbaki):
    Positive roots: alpha_1, alpha_2, alpha_1+alpha_2, 2alpha_1+alpha_2,
                    3alpha_1+alpha_2, 3alpha_1+2alpha_2.

    The Cartan matrix of G_2 (Bourbaki, alpha_1 short):
    A = [[2, -1], [-3, 2]]
    So a_{12} = -1, a_{21} = -3, meaning ||alpha_2||^2 / ||alpha_1||^2 = 3.

    Coroot alpha^vee = 2*alpha / <alpha, alpha>.
    In the basis of simple coroots {alpha_1^vee, alpha_2^vee}:
    - alpha_1^vee = (1, 0)
    - alpha_2^vee = (0, 1)
    - (alpha_1+alpha_2)^vee: need to express in coroot basis.

    For a root beta = c_1*alpha_1 + c_2*alpha_2, the coroot is
    beta^vee = (2/<beta,beta>) * beta.

    Let ||alpha_1||^2 = t (short), ||alpha_2||^2 = 3t (long).
    <alpha_1, alpha_2> = (a_{12}/2) * ||alpha_2||^2 = (-1/2)*3t = -3t/2.
    Check: a_{21} = 2<alpha_2,alpha_1>/||alpha_1||^2 = 2*(-3t/2)/t = -3. Correct.

    For beta = c_1*alpha_1 + c_2*alpha_2:
    ||beta||^2 = c_1^2*t + c_2^2*3t + 2*c_1*c_2*(-3t/2)
               = t*(c_1^2 + 3*c_2^2 - 3*c_1*c_2)

    beta^vee = (2/||beta||^2) * beta
    In the coroot basis: beta = c_1*alpha_1 + c_2*alpha_2
                                = c_1*(||alpha_1||^2/2)*alpha_1^vee + c_2*(||alpha_2||^2/2)*alpha_2^vee
    Wait, alpha_i = (||alpha_i||^2/2) * alpha_i^vee.
    So beta = c_1*(t/2)*alpha_1^vee + c_2*(3t/2)*alpha_2^vee.
    beta^vee = (2/||beta||^2) * beta
             = (2/(t*(c_1^2+3c_2^2-3c_1c_2))) * (c_1*t/2*alpha_1^vee + c_2*3t/2*alpha_2^vee)
             = (c_1 / (c_1^2+3c_2^2-3c_1c_2)) * alpha_1^vee
               + (3*c_2 / (c_1^2+3c_2^2-3c_1c_2)) * alpha_2^vee

    For the quantum dimension formula, what we actually need is just
    <lambda+rho, alpha^vee> where lambda = a*omega_1 + b*omega_2 (in fund wt coords)
    and alpha^vee is a positive coroot.  Since <omega_i, alpha_j^vee> = delta_{ij},
    we need alpha^vee in simple COROOT coordinates.

    The simple approach: use <lambda, alpha^vee> = sum_i lambda_i * (coefficient
    of alpha_i^vee in alpha^vee).  We just need those coefficients.

    For each positive root beta = c_1*alpha_1 + c_2*alpha_2 of G_2, the coroot is:
    beta^vee = (c_1 * d_1 / D(beta)) * alpha_1^vee + (c_2 * d_2 / D(beta)) * alpha_2^vee
    where d_i = ||alpha_i||^2 / 2 and D(beta) = ||beta||^2 / 2.

    With ||alpha_1||^2 = 2/3 (short, normalized so long = 2), ||alpha_2||^2 = 2:
    d_1 = 1/3, d_2 = 1.
    <alpha_1, alpha_2> = (a_{12}/2)*||alpha_2||^2 = (-1/2)*2 = -1.
    ||beta||^2 = c_1^2*(2/3) + c_2^2*2 + 2*c_1*c_2*(-1) = (2/3)*c_1^2 + 2*c_2^2 - 2*c_1*c_2.

    Rather than carrying this algebra, we use the TRIGONOMETRIC quantum dimension
    formula directly: sin-ratio with appropriate inner products.

    Actually, the cleanest approach: the quantum dimension formula for ANY simple
    Lie algebra at level k with q = exp(2*pi*i/(k+h^vee)) is:

    dim_q(V_lambda) = prod_{alpha > 0} sin(pi*(lambda+rho, alpha^vee)/(k+h^vee))
                                       / sin(pi*(rho, alpha^vee)/(k+h^vee))

    where (lambda, alpha^vee) = sum_i lambda_i * a_i^vee(alpha) with alpha^vee expressed
    in the simple coroot basis and lambda in fund. wt. coordinates.

    For simply-laced: alpha^vee = alpha, so (lambda, alpha^vee) = sum_i lambda_i * c_i(alpha).
    For G_2: we need the coroot coordinates explicitly.

    SIMPLEST CORRECT APPROACH: use the inverse Cartan matrix to go from root to
    fundamental weight coordinates, then use the fact that the Weyl-Kac formula
    in terms of the FINITE Weyl group is:

    dim_q(V_lambda) = sum_{w in W} (-1)^{l(w)} * q^{<w(lambda+rho) - rho, ...>} / ...

    TOO COMPLEX.  Use the PRODUCT FORMULA with integer-valued inner products.

    For G_2, the product formula uses <lambda+rho, alpha^vee> which must be
    a positive integer for dominant lambda.  We compute these directly.
    """
    # For G_2, the positive coroots in simple coroot basis are:
    # (Using the explicit computation for each root)
    #
    # For a simply-laced root system, coroots = roots (same coordinates).
    # For G_2, the coroots are DIFFERENT from the roots.
    #
    # The coroot system of G_2 is isomorphic to G_2 itself (G_2 is self-dual
    # as a root system), but with short and long exchanged.
    # If alpha_1 is short in the root system, then alpha_1^vee is LONG in the
    # coroot system.
    #
    # The positive coroots in simple coroot coordinates are:
    # alpha_1^vee, alpha_2^vee, alpha_1^vee + alpha_2^vee,
    # alpha_1^vee + 2*alpha_2^vee, alpha_1^vee + 3*alpha_2^vee,
    # 2*alpha_1^vee + 3*alpha_2^vee.
    #
    # This is because the COROOT system of G_2 is also G_2, but with
    # alpha_1^vee being LONG (3 short coroots) and alpha_2^vee being SHORT.
    # So the coroots of G_2 with (alpha_1 short, alpha_2 long) are the
    # roots of G_2 with (alpha_1^vee long, alpha_2^vee short), i.e.,
    # the G_2 root system with roles swapped.
    #
    # Positive roots of G_2 with alpha_1 long, alpha_2 short:
    # alpha_2, alpha_1, alpha_1+alpha_2, alpha_1+2*alpha_2, alpha_1+3*alpha_2, 2*alpha_1+3*alpha_2
    # In the original simple coroot basis, these are the positive coroots.

    return [
        (1, 0), (0, 1), (3, 1), (3, 2), (1, 1), (2, 1)
    ]


# Dual Coxeter numbers
_DUAL_COXETER = {
    ('A', 1): 2,   # sl_2
    ('A', 2): 3,   # sl_3
    ('A', 3): 4,   # sl_4
    ('A', 4): 5,   # sl_5
    ('G', 2): 4,   # G_2
    ('B', 2): 3,   # so_5
    ('B', 3): 5,   # so_7
    ('C', 2): 3,   # sp_4
    ('C', 3): 4,   # sp_6
}


def dual_coxeter_number(typ: str, rank: int) -> int:
    """Dual Coxeter number h^vee for simple Lie algebra (typ, rank).

    A_n: h^vee = n + 1
    B_n: h^vee = 2n - 1
    C_n: h^vee = n + 1
    D_n: h^vee = 2n - 2
    G_2: h^vee = 4
    F_4: h^vee = 9
    E_6: h^vee = 12
    E_7: h^vee = 18
    E_8: h^vee = 30
    """
    if (typ, rank) in _DUAL_COXETER:
        return _DUAL_COXETER[(typ, rank)]
    if typ == 'A':
        return rank + 1
    elif typ == 'B':
        return 2 * rank - 1
    elif typ == 'C':
        return rank + 1
    elif typ == 'D':
        return 2 * rank - 2
    raise ValueError(f"Unsupported type ({typ}, {rank})")


def lie_algebra_dim(typ: str, rank: int) -> int:
    """Dimension of the simple Lie algebra.

    A_n: (n+1)^2 - 1
    B_n: n(2n+1)
    C_n: n(2n+1)
    D_n: n(2n-1)
    G_2: 14
    """
    if typ == 'A':
        return (rank + 1) ** 2 - 1
    elif typ == 'B':
        return rank * (2 * rank + 1)
    elif typ == 'C':
        return rank * (2 * rank + 1)
    elif typ == 'D':
        return rank * (2 * rank - 1)
    elif typ == 'G' and rank == 2:
        return 14
    raise ValueError(f"Unsupported type ({typ}, {rank})")


# =========================================================================
# 1. Quantum dimensions at roots of unity via trigonometric formula
# =========================================================================

def quantum_dim_sl2(j: int, k: int) -> float:
    """Quantum dimension of V_j for sl_2 at level k.

    dim_q V_j = sin((j+1)*pi/(k+2)) / sin(pi/(k+2))
    = [j+1]_q with q = exp(i*pi/(k+2)).

    Integrable representations: j = 0, 1, ..., k.
    """
    if j < 0 or j > k:
        raise ValueError(f"j={j} not integrable at level k={k}")
    p = k + 2  # = k + h^vee for sl_2 (h^vee = 2)
    return math.sin((j + 1) * math.pi / p) / math.sin(math.pi / p)


def quantum_dim_sl3(a: int, b: int, k: int) -> float:
    """Quantum dimension of V(a,b) for sl_3 at level k.

    Integrability: a + b <= k, a >= 0, b >= 0.
    h^vee(sl_3) = 3, so q = exp(2*pi*i/(k+3)).

    The quantum Weyl dimension formula for sl_3:
    dim_q V(a,b) = prod_{alpha > 0} sin(pi*<lambda+rho, alpha>/(k+3))
                                    / sin(pi*<rho, alpha>/(k+3))

    For sl_3 (simply-laced), coroots = roots.
    Positive roots of A_2: alpha_1 = (1,0), alpha_2 = (0,1), alpha_1+alpha_2 = (1,1).
    rho = (1,1) in fund. wt. coords.
    lambda = (a, b).
    lambda+rho = (a+1, b+1).

    <lambda+rho, alpha_1> = a + 1
    <lambda+rho, alpha_2> = b + 1
    <lambda+rho, alpha_1+alpha_2> = a + b + 2

    <rho, alpha_1> = 1
    <rho, alpha_2> = 1
    <rho, alpha_1+alpha_2> = 2

    dim_q = sin((a+1)*pi/p) * sin((b+1)*pi/p) * sin((a+b+2)*pi/p)
          / (sin(pi/p) * sin(pi/p) * sin(2*pi/p))
    where p = k + 3.
    """
    if a < 0 or b < 0 or a + b > k:
        raise ValueError(f"(a,b)=({a},{b}) not integrable at level k={k}")
    p = k + 3  # k + h^vee
    s = lambda x: math.sin(x * math.pi / p)
    return (s(a + 1) * s(b + 1) * s(a + b + 2)) / (s(1) * s(1) * s(2))


def quantum_dim_g2(a: int, b: int, k: int) -> float:
    """Quantum dimension of V(a,b) for G_2 at level k.

    Convention: Bourbaki Cartan matrix A = [[2,-1],[-3,2]], where alpha_1 is
    LONG and alpha_2 is SHORT.  (This is the standard Bourbaki convention for G_2.)

    h^vee(G_2) = 4, so p = k + 4.

    The quantum Weyl dimension formula uses the positive coroots.
    For G_2, lambda = a*omega_1 + b*omega_2 in fundamental weight coordinates.
    rho = (1, 1).

    COROOT DERIVATION (from first principles):
    ||alpha_1||^2 = 2 (long), ||alpha_2||^2 = 2/3 (short), <alpha_1,alpha_2> = -1.
    Verified: a_{12} = 2<alpha_2,alpha_1>/||alpha_1||^2 = 2(-1)/2 = -1.
              a_{21} = 2<alpha_1,alpha_2>/||alpha_2||^2 = 2(-1)/(2/3) = -3.

    Positive roots (alpha_1 long, alpha_2 short):
    alpha_1=(1,0), alpha_2=(0,1), alpha_1+alpha_2=(1,1), alpha_1+2alpha_2=(1,2),
    alpha_1+3alpha_2=(1,3), 2alpha_1+3alpha_2=(2,3).

    In the simple coroot basis {alpha_1^vee, alpha_2^vee}:
    alpha_1 = (||alpha_1||^2/2)*alpha_1^vee = alpha_1^vee
    alpha_2 = (||alpha_2||^2/2)*alpha_2^vee = (1/3)*alpha_2^vee.

    For root beta = c_1*alpha_1 + c_2*alpha_2:
    beta = c_1*alpha_1^vee + (c_2/3)*alpha_2^vee  (in coroot basis)
    ||beta||^2 = c_1^2*2 + c_2^2*(2/3) + 2*c_1*c_2*(-1)
    beta^vee = (2/||beta||^2)*beta

    Positive coroots (c^vee_1, c^vee_2) in simple coroot coordinates:
    root (1,0) long:  ||beta||^2=2, coroot = (1, 0),      <rho,cv>=1
    root (0,1) short: ||beta||^2=2/3, coroot = (0, 1),    <rho,cv>=1
    root (1,1) short: ||beta||^2=2/3, coroot = (3, 1),    <rho,cv>=4
    root (1,2) short: ||beta||^2=2/3, coroot = (3, 2),    <rho,cv>=5
    root (1,3) long:  ||beta||^2=2, coroot = (1, 1),      <rho,cv>=2
    root (2,3) long:  ||beta||^2=2, coroot = (2, 1),      <rho,cv>=3

    Product of <rho, beta^vee> = 1*1*4*5*2*3 = 120.

    Highest coroot theta^vee: the comarks of G_2^(1) are (a_0^vee, a_1^vee, a_2^vee)
    = (1, 2, 1).  So theta^vee = 2*alpha_1^vee + alpha_2^vee = (2, 1).
    <rho, theta^vee> = 3, h^vee = 1 + 3 = 4.  CORRECT.

    Integrability: <lambda, theta^vee> = 2a + b <= k.

    Classical dimension verification:
    V(1,0) [adjoint, 14-dim]: lambda+rho=(2,1), product = 2*1*7*8*3*5 = 1680,
    dim = 1680/120 = 14.  CORRECT.
    V(0,1) [fundamental, 7-dim]: lambda+rho=(1,2), product = 1*2*5*7*3*4 = 840,
    dim = 840/120 = 7.  CORRECT.
    """
    if a < 0 or b < 0 or 2 * a + b > k:
        raise ValueError(f"(a,b)=({a},{b}) not integrable at level k={k}: need 2a+b<=k")
    p = k + 4  # k + h^vee(G_2) = k + 4

    # For non-simply-laced algebras, the quantum dimension formula uses the
    # SYMMETRIZED inner product, NOT the coroot pairing:
    #
    # dim_q(V_lambda) = prod_{alpha > 0} sin(pi * <lambda+rho, alpha>_s / p)
    #                                    / sin(pi * <rho, alpha>_s / p)
    #
    # where <omega_i, alpha_j>_s = d_j * delta_{ij} with d_j = ||alpha_j||^2/2.
    # For G_2 (alpha_1 long, alpha_2 short): d_1 = 1, d_2 = 1/3.
    #
    # This ensures all factors are positive for integrable representations.

    roots = [(1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3)]
    d1 = 1.0      # ||alpha_1||^2 / 2 (long root)
    d2 = 1.0 / 3  # ||alpha_2||^2 / 2 (short root)

    lr = (a + 1, b + 1)  # lambda + rho
    rho = (1, 1)

    num = 1.0
    den = 1.0
    for c1, c2 in roots:
        inner_lr = d1 * lr[0] * c1 + d2 * lr[1] * c2
        inner_rho = d1 * rho[0] * c1 + d2 * rho[1] * c2
        num *= math.sin(inner_lr * math.pi / p)
        den *= math.sin(inner_rho * math.pi / p)

    return num / den


def quantum_dim_general(typ: str, rank: int, hw: Tuple[int, ...], k: int) -> float:
    """Quantum dimension via the Weyl-Kac formula for general type.

    Uses the trigonometric product formula:
    dim_q V_lambda = prod_{alpha^vee > 0} sin(pi*<lambda+rho, alpha^vee>/(k+h^vee))
                                          / sin(pi*<rho, alpha^vee>/(k+h^vee))

    Args:
        typ: Lie type ('A', 'G')
        rank: rank of the algebra
        hw: highest weight in fundamental weight coordinates
        k: level
    """
    if typ == 'A' and rank == 1:
        return quantum_dim_sl2(hw[0], k)
    elif typ == 'A' and rank == 2:
        return quantum_dim_sl3(hw[0], hw[1], k)
    elif typ == 'G' and rank == 2:
        return quantum_dim_g2(hw[0], hw[1], k)
    elif typ == 'A':
        return _quantum_dim_slN(rank + 1, hw, k)
    else:
        raise ValueError(f"Unsupported type ({typ}, {rank})")


def _quantum_dim_slN(N: int, hw: Tuple[int, ...], k: int) -> float:
    """Quantum dimension for sl_N at level k.

    Simply-laced: coroots = roots.
    Positive roots: e_i - e_j, 1 <= i < j <= N.
    In simple root coordinates: alpha_{i,j} = (0,...,0,1,...,1,0,...,0)
    (1's in positions i through j-1).

    <lambda+rho, alpha_{i,j}> = sum_{m=i}^{j-1} (lambda+rho)_m
    """
    rank = N - 1
    h_vee = N
    p = k + h_vee
    if len(hw) != rank:
        raise ValueError(f"hw has length {len(hw)}, expected {rank}")

    lr = tuple(hw[i] + 1 for i in range(rank))  # lambda + rho

    num = 1.0
    den = 1.0
    for i in range(rank):
        for j in range(i, rank):
            # alpha_{i,j} in simple root coords: 1's in positions i..j
            inner_lr = sum(lr[m] for m in range(i, j + 1))
            inner_rho = j - i + 1  # sum of rho_m for m=i..j, each = 1
            num *= math.sin(inner_lr * math.pi / p)
            den *= math.sin(inner_rho * math.pi / p)

    return num / den


# =========================================================================
# 2. Integrable weight enumeration
# =========================================================================

def integrable_weights_sl2(k: int) -> List[int]:
    """Integrable highest weights for sl_2 at level k.

    Returns j = 0, 1, ..., k (j is the Dynkin label = 2 * spin).
    """
    return list(range(k + 1))


def integrable_weights_sl3(k: int) -> List[Tuple[int, int]]:
    """Integrable highest weights for sl_3 at level k.

    Condition: a + b <= k, a >= 0, b >= 0.
    Returns list of (a, b) pairs.
    """
    result = []
    for a in range(k + 1):
        for b in range(k + 1 - a):
            result.append((a, b))
    return result


def integrable_weights_g2(k: int) -> List[Tuple[int, int]]:
    """Integrable highest weights for G_2 at level k.

    Condition: 2a + b <= k, a >= 0, b >= 0.
    (Derived from coroot analysis: theta^vee = (2,1) in coroot coords,
    so <lambda, theta^vee> = 2a + b.)
    """
    result = []
    for a in range(k // 2 + 1):
        for b in range(k - 2 * a + 1):
            result.append((a, b))
    return result


def integrable_weights_slN(N: int, k: int) -> List[Tuple[int, ...]]:
    """Integrable highest weights for sl_N at level k.

    Condition: sum of Dynkin labels <= k.
    """
    rank = N - 1
    result = []
    _enum_bounded(rank, k, [], result)
    return result


def _enum_bounded(rank: int, remaining: int,
                  partial: List[int], result: List[Tuple[int, ...]]) -> None:
    """Enumerate tuples of length `rank` with nonneg entries summing <= remaining."""
    if len(partial) == rank:
        result.append(tuple(partial))
        return
    for c in range(remaining + 1):
        _enum_bounded(rank, remaining - c, partial + [c], result)


def num_integrable_weights(typ: str, rank: int, k: int) -> int:
    """Number of integrable highest weights at level k (INCLUDING trivial).

    For sl_2: k + 1 representations.
    For sl_3: (k+1)(k+2)/2 representations.
    For sl_N: C(k+N-1, N-1) = (k+N-1)! / (k! * (N-1)!) representations.
    For G_2: number of (a,b) with a >= 0, b >= 0, a + 2b <= k.
    """
    if typ == 'A':
        N = rank + 1
        # C(k + N - 1, N - 1) = product formula
        num = 1
        den = 1
        for i in range(1, N):
            num *= (k + i)
            den *= i
        return num // den
    elif typ == 'G' and rank == 2:
        return len(integrable_weights_g2(k))
    raise ValueError(f"Unsupported type ({typ}, {rank})")


# =========================================================================
# 3. Modular S-matrix (Verlinde)
# =========================================================================

def s_matrix_sl2(k: int) -> np.ndarray:
    """Modular S-matrix for sl_2 at level k.

    S_{j,l} = sqrt(2/(k+2)) * sin((j+1)(l+1)*pi/(k+2))

    for j, l = 0, 1, ..., k.

    Properties:
    - S is symmetric and unitary: S S^* = I.
    - S^2 = C (charge conjugation), so S^4 = I.
    - S_{0,j}/S_{0,0} = quantum dimension of V_j.
    """
    p = k + 2
    n = k + 1
    S = np.zeros((n, n))
    prefactor = math.sqrt(2.0 / p)
    for j in range(n):
        for l in range(n):
            S[j, l] = prefactor * math.sin((j + 1) * (l + 1) * math.pi / p)
    return S


def verify_s_matrix_unitarity(k: int) -> float:
    """Verify S S^dagger = I for the sl_2 S-matrix at level k.

    Returns the Frobenius norm ||S S^dagger - I||_F.
    """
    S = s_matrix_sl2(k)
    product = S @ S.T  # S is real and symmetric, so S^dagger = S^T = S
    identity = np.eye(k + 1)
    return float(np.linalg.norm(product - identity))


def verlinde_quantum_dim_sl2(j: int, k: int) -> float:
    """Quantum dimension of V_j from the S-matrix ratio.

    dim_q V_j = S_{0j} / S_{00}.

    Must agree with quantum_dim_sl2(j, k).
    """
    S = s_matrix_sl2(k)
    return S[0, j] / S[0, 0]


def verlinde_fusion_sl2(i: int, j: int, l: int, k: int) -> float:
    """Verlinde fusion coefficient N_{ij}^l for sl_2 at level k.

    N_{ij}^l = sum_m S_{im} S_{jm} S*_{lm} / S_{0m}

    Should be a nonneg integer (up to numerical error).
    """
    S = s_matrix_sl2(k)
    n = k + 1
    result = 0.0
    for m in range(n):
        if abs(S[0, m]) < 1e-15:
            continue
        result += S[i, m] * S[j, m] * S[l, m] / S[0, m]
    return result


# =========================================================================
# 4. Modular categorical zeta function
# =========================================================================

def modular_zeta_sl2(s: complex, k: int) -> complex:
    """Modular categorical zeta for sl_2 at level k.

    zeta^{mod}_{sl_2,k}(s) = sum_{j=1}^{k} [j+1]_q^{-s}

    where [j+1]_q = sin((j+1)*pi/(k+2)) / sin(pi/(k+2)).
    Excludes j=0 (trivial representation, quantum dim = 1).
    """
    result = complex(0)
    for j in range(1, k + 1):
        d_q = quantum_dim_sl2(j, k)
        if abs(d_q) < 1e-15:
            continue
        result += d_q ** (-s)
    return result


def modular_zeta_sl3(s: complex, k: int) -> complex:
    """Modular categorical zeta for sl_3 at level k.

    zeta^{mod}_{sl_3,k}(s) = sum_{(a,b) nontrivial} dim_q(V(a,b))^{-s}

    Excludes (0,0) (trivial representation).
    """
    result = complex(0)
    for a, b in integrable_weights_sl3(k):
        if a == 0 and b == 0:
            continue
        d_q = quantum_dim_sl3(a, b, k)
        if abs(d_q) < 1e-15:
            continue
        result += d_q ** (-s)
    return result


def modular_zeta_g2(s: complex, k: int) -> complex:
    """Modular categorical zeta for G_2 at level k.

    zeta^{mod}_{G_2,k}(s) = sum_{(a,b) nontrivial} dim_q(V(a,b))^{-s}

    Excludes (0,0) (trivial representation).
    """
    result = complex(0)
    for a, b in integrable_weights_g2(k):
        if a == 0 and b == 0:
            continue
        d_q = quantum_dim_g2(a, b, k)
        if abs(d_q) < 1e-15:
            continue
        result += d_q ** (-s)
    return result


def modular_zeta_slN(s: complex, N: int, k: int) -> complex:
    """Modular categorical zeta for sl_N at level k.

    Excludes the trivial representation (all Dynkin labels = 0).
    """
    result = complex(0)
    rank = N - 1
    trivial = tuple(0 for _ in range(rank))
    for hw in integrable_weights_slN(N, k):
        if hw == trivial:
            continue
        d_q = _quantum_dim_slN(N, hw, k)
        if abs(d_q) < 1e-15:
            continue
        result += d_q ** (-s)
    return result


def modular_zeta_general(s: complex, typ: str, rank: int, k: int) -> complex:
    """Modular categorical zeta for general type.

    Dispatches to the appropriate specialized function.
    """
    if typ == 'A' and rank == 1:
        return modular_zeta_sl2(s, k)
    elif typ == 'A' and rank == 2:
        return modular_zeta_sl3(s, k)
    elif typ == 'A':
        return modular_zeta_slN(s, rank + 1, k)
    elif typ == 'G' and rank == 2:
        return modular_zeta_g2(s, k)
    raise ValueError(f"Unsupported type ({typ}, {rank})")


# =========================================================================
# 5. k -> infinity limit and convergence to Riemann zeta
# =========================================================================

def modular_zeta_convergence_sl2(s: complex, k_values: List[int]) -> List[Dict[str, Any]]:
    """Track convergence of zeta^{mod}_{sl_2,k}(s) to zeta(s) - 1 as k -> infinity.

    Returns list of dicts with k, zeta_mod, error vs zeta(s)-1.

    The quantum dimension [j+1]_q at level k satisfies:
    [j+1]_q = (j+1) * (1 - (j+1)^2 * pi^2 / (6*(k+2)^2) + O(1/k^4))
    (from the Taylor expansion of sin(x)/x at small x).

    Therefore the correction is O(1/k^2).
    """
    # Compute zeta(s) - 1 via Euler-Maclaurin
    zeta_limit = _riemann_zeta_em(s, 200) - 1.0

    results = []
    for k in k_values:
        z_mod = modular_zeta_sl2(s, k)
        error = abs(z_mod - zeta_limit)
        results.append({
            'k': k,
            'zeta_mod': z_mod,
            'zeta_limit': zeta_limit,
            'error': error,
        })
    return results


def _riemann_zeta_em(s: complex, N: int = 200) -> complex:
    """Riemann zeta via Euler-Maclaurin (for Re(s) > 1)."""
    if abs(s - 1.0) < 1e-12:
        return complex(float('inf'))
    partial = sum(n ** (-s) for n in range(1, N + 1))
    tail = N ** (1 - s) / (s - 1) + 0.5 * N ** (-s)
    # Bernoulli corrections
    B = [Fraction(1, 6), Fraction(-1, 30), Fraction(1, 42), Fraction(-1, 30),
         Fraction(5, 66), Fraction(-691, 2730)]
    correction = complex(0)
    for k_idx, bk in enumerate(B):
        kk = k_idx + 1
        if kk == 1:
            correction += float(bk) / 2.0 * s * N ** (-(s + 1))
        else:
            prod_s = complex(1)
            for j_idx in range(2 * kk - 1):
                prod_s *= (s + j_idx)
            correction += float(bk) * prod_s / math.factorial(2 * kk) * N ** (-(s + 2 * kk - 1))
    return partial + tail + correction


def asymptotic_expansion_sl2(s: complex, k: int, n_terms: int = 3) -> Dict[str, Any]:
    """Asymptotic expansion of zeta^{mod}_{sl_2,k}(s) for large k.

    zeta^{mod}_{sl_2,k}(s) = zeta(s) - 1 + c_1(s)/k^2 + c_2(s)/k^4 + ...

    The leading correction comes from [j+1]_q = sin((j+1)*pi/(k+2))/sin(pi/(k+2)).
    Let eps = pi/(k+2).  Then [j+1]_q = sin((j+1)*eps)/sin(eps).

    sin((j+1)*eps)/sin(eps) = (j+1) - (j+1)*((j+1)^2 - 1)*eps^2/6 + O(eps^4)
    (using sin(x)/x = 1 - x^2/6 + x^4/120 - ..., and similarly for the ratio).

    More precisely:
    sin((j+1)*eps) / sin(eps) = (j+1) * (1 - ((j+1)^2 - 1)*eps^2/6 + O(eps^4))
                               / (1 - eps^2/6 + O(eps^4))
    = (j+1) * (1 - ((j+1)^2 - 1)*eps^2/6) * (1 + eps^2/6) + O(eps^4)
    = (j+1) * (1 - ((j+1)^2 - 1 - 1)*eps^2/6) + O(eps^4)
    = (j+1) * (1 - ((j+1)^2 - 2)*eps^2/6) + O(eps^4)

    Hmm, let me be more careful.  Let d = j + 1, x = d*eps, y = eps.
    sin(x)/sin(y) = (x/y) * (sin(x)/x) / (sin(y)/y)
    = d * (1 - x^2/6 + x^4/120 - ...) / (1 - y^2/6 + y^4/120 - ...)
    = d * (1 - d^2*eps^2/6 + d^4*eps^4/120 - ...) / (1 - eps^2/6 + eps^4/120 - ...)
    = d * (1 - d^2*eps^2/6 + ...) * (1 + eps^2/6 + eps^4/36 + eps^4/120 + ...)
    = d * (1 - (d^2 - 1)*eps^2/6 + O(eps^4))

    So [d]_q = d * (1 - (d^2 - 1)*eps^2/6 + O(eps^4)) where eps = pi/(k+2).

    Then [d]_q^{-s} = d^{-s} * (1 - (d^2-1)*eps^2/6)^{-s}
                    = d^{-s} * (1 + s*(d^2-1)*eps^2/6 + O(eps^4))

    Summing: sum_{d=2}^{k+1} [d]_q^{-s}
    = sum_{d=2}^{k+1} d^{-s} + (s*eps^2/6) * sum_{d=2}^{k+1} d^{-s}*(d^2-1) + ...
    = sum_{d=2}^{k+1} d^{-s} + (s*eps^2/6) * (sum d^{2-s} - sum d^{-s}) + ...

    The first term approaches zeta(s) - 1 as k -> infinity.
    The second term involves (s*pi^2/(6*(k+2)^2)) * (zeta(s-2) - 1 - (zeta(s) - 1)) + ...
    = s*pi^2 / (6*(k+2)^2) * (zeta(s-2) - zeta(s)) + O(1/k^4)

    Returns dict with expansion coefficients.
    """
    eps = math.pi / (k + 2)

    # Compute the actual modular zeta
    z_mod = modular_zeta_sl2(s, k)

    # Limit value
    z_limit = _riemann_zeta_em(s, 500) - 1.0

    # Leading correction coefficient c_1(s)
    # c_1(s) = s * pi^2 / 6 * (zeta(s-2) - zeta(s))
    # (from the expansion above, with the substitution eps^2 = pi^2/(k+2)^2)
    if s.real > 3 if isinstance(s, complex) else s > 3:
        zeta_sm2 = _riemann_zeta_em(s - 2, 500)
    else:
        zeta_sm2 = complex(float('nan'))  # zeta(s-2) may not converge

    c1_coeff = s * math.pi ** 2 / 6.0

    # The correction is c1_coeff * (zeta(s-2) - zeta(s)) / (k+2)^2
    # but this is only valid for Re(s) > 3 (so zeta(s-2) converges)

    result = {
        's': s,
        'k': k,
        'zeta_mod': z_mod,
        'zeta_limit': z_limit,
        'error': abs(z_mod - z_limit),
        'eps': eps,
    }

    if not math.isnan(zeta_sm2.real if isinstance(zeta_sm2, complex) else zeta_sm2):
        zeta_s = _riemann_zeta_em(s, 500)
        c1_value = c1_coeff * (zeta_sm2 - zeta_s)
        predicted_correction = c1_value / (k + 2) ** 2
        result['c1_coeff'] = c1_coeff
        result['c1_value'] = c1_value
        result['predicted_correction'] = predicted_correction
        result['actual_correction'] = z_mod - z_limit

    return result


# =========================================================================
# 6. Modular zeta at s = 0 (representation counting)
# =========================================================================

def modular_zeta_at_zero(typ: str, rank: int, k: int) -> Dict[str, Any]:
    """Modular zeta at s = 0 counts nontrivial integrable representations.

    zeta^{mod}(0) = sum_{lambda nontrivial} 1 = #(integrable weights) - 1.

    For sl_2: k
    For sl_3: (k+1)(k+2)/2 - 1
    For sl_N: C(k+N-1, N-1) - 1
    For G_2: #(a,b: a+2b<=k, a,b>=0) - 1
    """
    # Compute via the zeta function at s = 0
    z0 = modular_zeta_general(0, typ, rank, k)

    # Compute via direct counting
    if typ == 'A':
        N = rank + 1
        total = num_integrable_weights('A', rank, k)
    elif typ == 'G' and rank == 2:
        total = num_integrable_weights('G', 2, k)
    else:
        raise ValueError(f"Unsupported type ({typ}, {rank})")

    count = total - 1  # exclude trivial

    return {
        'typ': typ,
        'rank': rank,
        'k': k,
        'zeta_at_0': z0,
        'count': count,
        'match': abs(z0.real - count) < 0.5 if isinstance(z0, complex) else abs(z0 - count) < 0.5,
    }


# =========================================================================
# 7. Level-rank duality
# =========================================================================

def level_rank_quantum_dims_sl(N: int, k: int) -> List[float]:
    """Sorted list of quantum dimensions for sl_N at level k.

    For the level-rank duality comparison sl_N,k <-> sl_k,N.
    """
    dims = []
    rank = N - 1
    trivial = tuple(0 for _ in range(rank))
    for hw in integrable_weights_slN(N, k):
        if hw == trivial:
            continue
        d = _quantum_dim_slN(N, hw, k)
        dims.append(abs(d))
    return sorted(dims)


def level_rank_duality_check(N: int, k: int, s: complex) -> Dict[str, Any]:
    """Test level-rank duality: compare sl_N at level k with sl_k at level N.

    Level-rank duality states that the modular tensor categories are related,
    but the relationship is NOT simply equality of the categorical zeta.
    The quantum dimensions are related by a nontrivial permutation/scaling.

    The simplest invariant that DOES match is the total quantum dimension:
    D^2 = sum_lambda (dim_q V_lambda)^2 = 1/S_{00}^2.

    For sl_N at level k: S_{00} = sqrt(N/(k+N)) * prod_{alpha>0} sin(pi*<rho,alpha>/(k+N))
    ... this is complicated.  A cleaner invariant:
    D^2_{sl_N,k} = (k+N)^{N-1} / (N * prod_{j=1}^{N-1} j!)  [up to combinatorial factors]

    Actually the SIMPLEST check: the number of integrable representations.
    For sl_N at level k: C(k+N-1, N-1).
    For sl_k at level N: C(N+k-1, k-1).
    These are equal (binomial coefficient symmetry)!

    Returns comparison data.
    """
    # Number of integrable reps (including trivial)
    n_NK = num_integrable_weights('A', N - 1, k)
    n_KN = num_integrable_weights('A', k - 1, N)

    # Modular zeta values
    z_NK = modular_zeta_slN(s, N, k)
    z_KN = modular_zeta_slN(s, k, N)

    # Total quantum dimension squared
    total_qdim2_NK = 0.0
    for hw in integrable_weights_slN(N, k):
        d = _quantum_dim_slN(N, hw, k)
        total_qdim2_NK += d ** 2

    total_qdim2_KN = 0.0
    for hw in integrable_weights_slN(k, N):
        d = _quantum_dim_slN(k, hw, N)
        total_qdim2_KN += d ** 2

    return {
        'N': N,
        'k': k,
        's': s,
        'n_reps_NK': n_NK,
        'n_reps_KN': n_KN,
        'reps_equal': n_NK == n_KN,
        'zeta_NK': z_NK,
        'zeta_KN': z_KN,
        'zeta_ratio': z_NK / z_KN if abs(z_KN) > 1e-15 else float('inf'),
        'total_qdim2_NK': total_qdim2_NK,
        'total_qdim2_KN': total_qdim2_KN,
        'total_qdim2_ratio': total_qdim2_NK / total_qdim2_KN if total_qdim2_KN > 1e-15 else float('inf'),
    }


# =========================================================================
# 8. Zeros of the modular categorical zeta
# =========================================================================

def modular_zeta_on_line(sigma: float, t_values: np.ndarray,
                         k: int) -> np.ndarray:
    """Evaluate zeta^{mod}_{sl_2,k}(sigma + i*t) along a vertical line.

    Returns array of complex values.
    """
    results = np.zeros(len(t_values), dtype=complex)
    for idx, t in enumerate(t_values):
        s = complex(sigma, t)
        results[idx] = modular_zeta_sl2(s, k)
    return results


def find_zeros_modular_zeta_sl2(k: int, sigma_range: Tuple[float, float] = (-5.0, 5.0),
                                 t_range: Tuple[float, float] = (-50.0, 50.0),
                                 grid_density: int = 200) -> List[complex]:
    """Find zeros of zeta^{mod}_{sl_2,k}(s) in a rectangular region.

    Since the modular zeta is a finite sum of exponentials:
    zeta^{mod}(s) = sum_{j=1}^k d_j^{-s} = sum_{j=1}^k exp(-s * log d_j)

    this is an EXPONENTIAL SUM whose zeros can be found by grid search
    followed by Newton refinement.
    """
    # Get the quantum dimensions
    dims = []
    for j in range(1, k + 1):
        d = quantum_dim_sl2(j, k)
        if d > 0:
            dims.append(d)

    if not dims:
        return []

    # Grid search for approximate zeros
    sigma_grid = np.linspace(sigma_range[0], sigma_range[1], grid_density)
    t_grid = np.linspace(t_range[0], t_range[1], grid_density * 5)

    def f(s):
        return sum(d ** (-s) for d in dims)

    # Find sign changes / small values on grid
    candidates = []
    for sigma in sigma_grid:
        vals = [f(complex(sigma, t)) for t in t_grid]
        for i in range(len(vals) - 1):
            # Check if |f| has a local minimum near zero
            if abs(vals[i]) < 1.0 and abs(vals[i + 1]) < 1.0:
                # Check if real and imaginary parts change sign
                if (vals[i].real * vals[i + 1].real < 0 or
                    vals[i].imag * vals[i + 1].imag < 0):
                    candidates.append(complex(sigma, (t_grid[i] + t_grid[i + 1]) / 2))

    # Newton refinement
    zeros = []
    for s0 in candidates:
        z = _newton_refine(f, s0, dims)
        if z is not None and abs(f(z)) < 1e-8:
            # Check uniqueness
            is_new = True
            for existing in zeros:
                if abs(z - existing) < 0.01:
                    is_new = False
                    break
            if is_new and t_range[0] <= z.imag <= t_range[1]:
                zeros.append(z)

    # Sort by imaginary part
    zeros.sort(key=lambda z: (abs(z.imag), z.real))
    return zeros


def _newton_refine(f, s0: complex, dims: List[float],
                   max_iter: int = 50, tol: float = 1e-12) -> Optional[complex]:
    """Newton's method for f(s) = sum d_j^{-s} = 0.

    f'(s) = -sum d_j^{-s} * log(d_j).
    """
    s = s0
    for _ in range(max_iter):
        val = f(s)
        if abs(val) < tol:
            return s
        # Derivative
        deriv = sum(-d ** (-s) * math.log(d) for d in dims if d > 0 and d != 1.0)
        if abs(deriv) < 1e-30:
            return None
        s = s - val / deriv
    if abs(f(s)) < 1e-8:
        return s
    return None


# =========================================================================
# 9. Shadow-modular comparison
# =========================================================================

def kappa_affine(typ: str, rank: int, k: int) -> float:
    """Modular characteristic kappa for the affine Lie algebra at level k.

    kappa(hat{g}_k) = dim(g) * (k + h^vee) / (2 * h^vee).

    For sl_2: kappa = 3 * (k + 2) / 4.
    For sl_3: kappa = 8 * (k + 3) / 6 = 4 * (k + 3) / 3.
    For G_2: kappa = 14 * (k + 4) / 8 = 7 * (k + 4) / 4.
    """
    dim_g = lie_algebra_dim(typ, rank)
    h_vee = dual_coxeter_number(typ, rank)
    return dim_g * (k + h_vee) / (2.0 * h_vee)


def shadow_modular_comparison(typ: str, rank: int, k: int, s: complex) -> Dict[str, Any]:
    """Compare modular categorical zeta with shadow zeta data.

    The shadow zeta ζ_A(s) uses shadow coefficients S_r.
    The modular categorical zeta ζ^{mod}(s) uses quantum dimensions.
    At level k, kappa(hat{g}_k) = dim(g)*(k+h^vee)/(2*h^vee).

    These are DIFFERENT objects probing different aspects of the same algebra.
    The comparison reveals how the finite truncation (modular) relates to the
    infinite categorical structure (shadow).
    """
    kap = kappa_affine(typ, rank, k)
    z_mod = modular_zeta_general(s, typ, rank, k)
    n_reps = num_integrable_weights(typ, rank, k) - 1  # nontrivial

    # For sl_2, the k -> infinity limit of z_mod is zeta(s) - 1
    # The shadow zeta at the same kappa would involve the invariants
    # S_r(hat{sl}_2, k) which are functions of k.

    return {
        'typ': typ,
        'rank': rank,
        'k': k,
        's': s,
        'kappa': kap,
        'zeta_mod': z_mod,
        'n_nontrivial_reps': n_reps,
        'kappa_over_n': kap / n_reps if n_reps > 0 else float('inf'),
    }


# =========================================================================
# 10. Quantum dimension spectra
# =========================================================================

def quantum_dim_spectrum_sl2(k: int) -> List[Tuple[int, float]]:
    """Full quantum dimension spectrum for sl_2 at level k.

    Returns [(j, dim_q(V_j)) for j = 0, ..., k].
    """
    return [(j, quantum_dim_sl2(j, k)) for j in range(k + 1)]


def quantum_dim_spectrum_sl3(k: int) -> List[Tuple[Tuple[int, int], float]]:
    """Full quantum dimension spectrum for sl_3 at level k.

    Returns [((a,b), dim_q(V(a,b))) for all integrable (a,b)].
    """
    result = []
    for a, b in integrable_weights_sl3(k):
        result.append(((a, b), quantum_dim_sl3(a, b, k)))
    return result


def quantum_dim_spectrum_g2(k: int) -> List[Tuple[Tuple[int, int], float]]:
    """Full quantum dimension spectrum for G_2 at level k.

    Returns [((a,b), dim_q(V(a,b))) for all integrable (a,b)].
    """
    result = []
    for a, b in integrable_weights_g2(k):
        result.append(((a, b), quantum_dim_g2(a, b, k)))
    return result


def classical_dim_sl2(j: int) -> int:
    """Classical dimension of V_j for sl_2: j + 1."""
    return j + 1


def classical_dim_sl3(a: int, b: int) -> int:
    """Classical dimension of V(a,b) for sl_3: (a+1)(b+1)(a+b+2)/2."""
    return (a + 1) * (b + 1) * (a + b + 2) // 2


def classical_dim_g2(a: int, b: int) -> int:
    """Classical dimension of V(a,b) for G_2.

    Uses the Weyl dimension formula with the positive coroots in simple coroot
    coordinates: (1,0), (0,1), (3,1), (3,2), (1,1), (2,1).
    (Bourbaki convention: alpha_1 long, alpha_2 short.)

    V(1,0) = 14-dimensional adjoint, V(0,1) = 7-dimensional fundamental.
    """
    lr = (a + 1, b + 1)
    rho_vals = [1, 1, 4, 5, 2, 3]  # <rho, beta^vee> for each coroot
    coroots = [(1, 0), (0, 1), (3, 1), (3, 2), (1, 1), (2, 1)]

    num = 1
    den = 1
    for cv, rv in zip(coroots, rho_vals):
        inner = lr[0] * cv[0] + lr[1] * cv[1]
        num *= inner
        den *= rv
    return num // den


def quantum_vs_classical_sl2(k: int) -> List[Tuple[int, float, int, float]]:
    """Compare quantum and classical dimensions for sl_2 at level k.

    Returns [(j, dim_q, dim_cl, ratio) for j = 0..k].
    """
    result = []
    for j in range(k + 1):
        dq = quantum_dim_sl2(j, k)
        dc = classical_dim_sl2(j)
        result.append((j, dq, dc, dq / dc if dc > 0 else float('inf')))
    return result


# =========================================================================
# 11. Modular zeta on the critical strip
# =========================================================================

def modular_zeta_critical_line_sl2(k: int, t_values: List[float]) -> List[Dict[str, Any]]:
    """Evaluate zeta^{mod}_{sl_2,k}(1/2 + it) on the critical line.

    Returns list of {t, s, value, abs_value}.
    """
    results = []
    for t in t_values:
        s = complex(0.5, t)
        val = modular_zeta_sl2(s, k)
        results.append({
            't': t,
            's': s,
            'value': val,
            'abs_value': abs(val),
        })
    return results


# =========================================================================
# 12. Comprehensive verification report
# =========================================================================

def full_verification_report(typ: str, rank: int, k: int,
                              s_values: List[complex] = None) -> Dict[str, Any]:
    """Run all verification checks for the modular categorical zeta.

    Returns a comprehensive report.
    """
    if s_values is None:
        s_values = [2.0, 3.0, 4.0]

    report = {
        'typ': typ,
        'rank': rank,
        'k': k,
        'h_vee': dual_coxeter_number(typ, rank),
        'kappa': kappa_affine(typ, rank, k),
    }

    # Count check
    z0_data = modular_zeta_at_zero(typ, rank, k)
    report['zeta_at_0'] = z0_data

    # Zeta values
    report['zeta_values'] = {}
    for s in s_values:
        report['zeta_values'][s] = modular_zeta_general(s, typ, rank, k)

    # S-matrix check (sl_2 only)
    if typ == 'A' and rank == 1:
        report['s_matrix_unitarity_error'] = verify_s_matrix_unitarity(k)

        # Verlinde vs direct quantum dimension check
        max_err = 0.0
        for j in range(k + 1):
            d_direct = quantum_dim_sl2(j, k)
            d_verlinde = verlinde_quantum_dim_sl2(j, k)
            max_err = max(max_err, abs(d_direct - d_verlinde))
        report['verlinde_vs_direct_max_error'] = max_err

    return report
