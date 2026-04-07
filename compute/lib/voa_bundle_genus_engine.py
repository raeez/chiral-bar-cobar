r"""VOA bundles on moduli of curves and the genus extension problem.

MATHEMATICAL FRAMEWORK
======================

For a vertex operator algebra A and a smooth pointed curve (C, p_1,...,p_n),
the space of CONFORMAL BLOCKS (or coinvariants) is a finite-dimensional
vector space V_A(C, p_1,...,p_n; M_1,...,M_n) depending on modules M_i.
As (C, p_i) vary over the moduli space M_{g,n}, these spaces assemble into
a VECTOR BUNDLE (the Verlinde bundle or bundle of conformal blocks).

CONFORMAL BLOCKS vs SHADOW CohFT
=================================

The shadow CohFT (thm:shadow-cohft) gives cohomology classes
Omega_{g,n}^A in R*(M-bar_{g,n}) from the bar-intrinsic MC element
Theta_A.  The CENTRAL QUESTION is how these relate to the Chern
character of the conformal block bundle.

KEY IDENTIFICATION (Theorem thm:conformal-block-reconstruction):
For uniform-weight modular Koszul algebras on the scalar lane:
  c_1(L_A) = kappa(A) * lambda
where L_A = det R pi_{g*} B-bar^{ch,(g)}(A) is the determinant line
bundle and lambda = c_1(det E^v) is the Hodge class.

LITERATURE
==========

[FBZ04] Frenkel-Ben-Zvi, Vertex Algebras and Algebraic Curves, Ch 17-20:
  conformal blocks as sheaves on M_{g,n}, coordinate-free vertex operators.

[DGT19] Damiolini-Gibney-Tarasca, arXiv:1901.06981:
  For C2-cofinite VOAs, coinvariants give quasi-coherent sheaves on
  M-bar_{g,n} with twisted D-module structure (projectively flat
  connection generalizing Hitchin/KZ).

[DGT19b] Damiolini-Gibney-Tarasca, arXiv:1909.04683:
  Factorization + vector bundle property under finiteness+semisimplicity.
  "CohFT-type" VOAs produce semisimple CohFTs.

[MOP13] Marian-Oprea-Pandharipande, arXiv:1308.4425:
  First Chern class of Verlinde bundle V_{r,k} for SU(r) at level k:
    c_1(V_{r,k}) = mu(r,k) * lambda
  where mu(r,k) is the slope computed from strange duality + Hitchin
  projective flatness.

[MOP14] Marian-Oprea-Pandharipande, arXiv:1311.3028:
  Full Chern character ch(V_k) as a semisimple CohFT on M-bar_{g,n}.
  Determined by Givental-Teleman reconstruction from genus-0 data
  (fusion algebra) + the slope c_1 on M_g + Hitchin projective flatness.

[Loo10] Looijenga, arXiv:1009.2245:
  WZW model as local system on the det bundle over M-bar_{g,n}.
  Projectively flat Hitchin connection with regular singularities.

[AU07] Andersen-Ueno (2007):
  Abelian TCFT and determinant bundles.

[Ver88] Verlinde (1988):
  Fusion rules and modular transformations.

[Bea96] Beauville (1996):
  Conformal blocks, fusion rules, and the Verlinde formula.

[BL94] Beauville-Laszlo (1995):
  Formal gluing for constructing conformal blocks from local data.
  Sewing = Beauville-Laszlo gluing on punctured formal disc.

CONVENTIONS (AP38, AP39, AP48):
  - kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v) for affine KM
  - kappa(Vir_c) = c/2 for Virasoro (NOT c(A)/2 for general A)
  - lambda = c_1(det E^v) where E = R^0 pi_* omega_{C/M_g}
  - The Verlinde bundle slope uses the PROJECTIVE flatness of
    Hitchin, which means c_1 is proportional to lambda.
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
from sympy import (
    Rational,
    bernoulli,
    binomial,
    factorial,
    simplify,
    pi as sym_pi,
    sin as sym_sin,
    sqrt as sym_sqrt,
    Symbol,
)

# Import from the existing Verlinde engine for core data
from compute.lib.verlinde_shadow_cohft_engine import (
    S_matrix,
    _get_lie_data,
    central_charge,
    fusion_coefficients,
    integrable_weights,
    kappa_affine,
    kappa_affine_exact,
    lambda_fp,
    num_integrable_reps,
    quantum_dim_weyl,
    quantum_dimensions,
    shadow_F_g,
    sl2_verlinde_closed_form,
    total_quantum_dim_sq,
    verlinde_dimension,
    verlinde_dimension_exact,
    verlinde_from_weyl_qdim,
)


# =========================================================================
# Section 1: Conformal block dimensions with marked points
# =========================================================================

def conformal_block_dim_sl2(
    level: int, genus: int, spins: Tuple[int, ...] = ()
) -> int:
    """Dimension of the space of conformal blocks for sl_2 at level k.

    V(Sigma_g, j_1, ..., j_n) = sum_{l=0}^{k}
        S_{0,l}^{2-2g-n} * prod_{i=1}^{n} S_{j_i, l} / S_{0, l}

    where S is the modular S-matrix and spins j_i in {0, 1, ..., k}.

    This is the VERLINDE FORMULA WITH INSERTIONS.

    At genus g with no insertions: recovers V_g = sum S_{0,l}^{2-2g}.
    At genus 0 with 3 insertions: recovers the fusion coefficient N_{j1,j2}^{j3*}.

    CONVENTIONS:
      - Spins are DYNKIN LABELS (0 = vacuum, k = highest spin)
      - S_{j,l} = sqrt(2/(k+2)) * sin(pi*(j+1)*(l+1)/(k+2))
      - Formula is from [Ver88], [Bea96], [FBZ04] Ch 19.
    """
    k = level
    n_pts = len(spins)
    # Validate spins
    for j in spins:
        if j < 0 or j > k:
            raise ValueError(f"Spin {j} out of range [0, {k}]")

    S = S_matrix("A", 1, k)
    n_wts = S.shape[0]  # = k + 1

    total = 0.0 + 0.0j
    power = 2 - 2 * genus - n_pts
    for l in range(n_wts):
        s0l = S[0, l]
        if abs(s0l) < 1e-15:
            continue
        contrib = s0l ** power
        for j in spins:
            contrib *= S[j, l]
        total += contrib

    result = total.real
    rounded = int(round(result))
    if abs(result - rounded) > 0.01:
        raise RuntimeError(
            f"Conformal block dimension not integer: {result} "
            f"(g={genus}, k={k}, spins={spins})"
        )
    return max(0, rounded)


def conformal_block_dim_general(
    lie_type: str, rank: int, level: int, genus: int,
    reps: Tuple[Tuple[int, ...], ...] = ()
) -> int:
    """Conformal block dimension for general type via Verlinde formula.

    V(Sigma_g, lambda_1, ..., lambda_n) = sum_mu
        S_{0,mu}^{2-2g-n} * prod_{i=1}^{n} S_{lambda_i, mu} / S_{0, mu}

    where the sum is over integrable weights mu.

    This is the generalized Verlinde formula [Ver88], [Bea96].
    For n=0: recovers the standard Verlinde dimension V_g.
    """
    n_pts = len(reps)
    S = S_matrix(lie_type, rank, level)
    weights = integrable_weights(lie_type, rank, level)
    n_wts = len(weights)

    # Build weight-to-index map
    wt_to_idx = {wt: i for i, wt in enumerate(weights)}

    # Validate representations
    for rep in reps:
        if rep not in wt_to_idx:
            raise ValueError(
                f"Representation {rep} not integrable at level {level}"
            )

    power = 2 - 2 * genus - n_pts
    total = 0.0 + 0.0j
    for mu_idx in range(n_wts):
        s0mu = S[0, mu_idx]
        if abs(s0mu) < 1e-15:
            continue
        contrib = s0mu ** power
        for rep in reps:
            rep_idx = wt_to_idx[rep]
            contrib *= S[rep_idx, mu_idx]
        total += contrib

    result = total.real
    rounded = int(round(result))
    if abs(result - rounded) > 0.01:
        raise RuntimeError(
            f"CB dim not integer: {result} "
            f"(g={genus}, type={lie_type}_{rank}, k={level}, reps={reps})"
        )
    return max(0, rounded)


# =========================================================================
# Section 2: Verlinde bundle rank and slope
# =========================================================================

def verlinde_bundle_rank(
    lie_type: str, rank: int, level: int, genus: int
) -> int:
    """Rank of the Verlinde bundle = V_g (no insertions).

    The Verlinde bundle E_{r,k} over M_g has fiber
    = space of conformal blocks = V_g(g, r, k).

    rk(E_{r,k}) = sum_lambda S_{0,lambda}^{2-2g}.
    """
    return verlinde_dimension_exact(lie_type, rank, level, genus)


def verlinde_slope_sl2(level: int, genus: int) -> Rational:
    r"""Slope of the Verlinde bundle for sl_2 at level k.

    The Marian-Oprea-Pandharipande formula [MOP13, Thm 1]:
    For SU(2) at level k on M_g (g >= 2):

        c_1(V_k) = (k(k+2)/4) * lambda_1 * rk(V_k)   [WRONG reading]

    Actually the correct formula from [MOP13] is:

        mu(V_k) = c_1(V_k) / rk(V_k)

    For SU(2) (sl_2) at level k, the slope is:
        mu = (k/2) * lambda

    in Pic(M_g) tensor Q, where lambda is the Hodge class.

    This follows from projective flatness of the Hitchin connection:
    the Verlinde bundle is projectively flat, so c_1/rk is determined
    by the central charge via the Knizhnik-Zamolodchikov level.

    The key formula is:
        c_1(V_{r,k}) / rk(V_{r,k}) = (k * r) / (2 * (k + r)) * lambda

    For r = 2 (SU(2), i.e., sl_2):
        c_1(V_k) / rk(V_k) = (k * 2) / (2 * (k + 2)) * lambda
                            = k / (k + 2) * lambda

    NOTE: This uses the convention where the Verlinde bundle is for
    SU(r) (i.e., the GROUP, not the Lie algebra). For the Lie algebra
    sl_r at level k, the rank is r and the dual Coxeter h^v = r.

    CROSS-CHECK with our kappa:
        kappa(sl_2, k) = 3(k+2)/(2*2) = 3(k+2)/4
        c/2 = k*3/(2*(k+2)) = 3k/(2(k+2))

    The slope k/(k+2) = (2/3) * c/2 * (2/dim) = c / dim(g).
    More precisely: slope = k*dim(g) / (dim(g)*(k+h^v)) = k/(k+h^v).

    For general type:
        slope(V_{r,k}(g)) = k / (k + h^v) * lambda

    This is the RATIO c_1/rank. The absolute c_1 is:
        c_1(V_k) = rk(V_k) * k / (k + h^v) * lambda

    CRITICAL CHECK: Does this match kappa * lambda?
    kappa = dim(g) * (k + h^v) / (2 h^v)
    slope = k / (k + h^v)
    slope * rk = rk * k / (k + h^v)

    These are DIFFERENT objects:
    - kappa * lambda is the SCALAR shadow (c_1 of the DETERMINANT line L_A)
    - slope * rk * lambda is c_1 of the full VERLINDE BUNDLE

    The relationship is:
        c_1(V_k) = rk(V_k) * slope * lambda
        c_1(L_A) = kappa * lambda  (determinant line of bar cohomology)

    They coincide when rk = 1 (genus 0 limit) but diverge at higher genus.
    """
    k = level
    # Slope for SU(r) level k: k / (k + r) for the GROUP SU(r)
    # For the Lie algebra sl_r at level k: slope = k / (k + h^v) where h^v = r
    h_v = 2  # dual Coxeter for sl_2
    return Rational(k, k + h_v)


def verlinde_slope_general(
    lie_type: str, rank: int, level: int
) -> Rational:
    r"""Slope of the Verlinde bundle for general type.

    mu(V_{g,k}) = c_1(V_{g,k}) / rk(V_{g,k}) = (k / (k + h^v)) * lambda

    where h^v is the dual Coxeter number.

    This follows from the projective flatness of the Hitchin connection
    [MOP13, Thm 1], [Loo10].

    The slope coefficient k/(k+h^v) equals c(g_k) / dim(g):
        c = k * dim(g) / (k + h^v)   (Sugawara formula)
        c / dim(g) = k / (k + h^v) = slope

    So the slope is the central charge per degree of freedom.
    """
    data = _get_lie_data(lie_type, rank)
    hv = data["hv"]
    return Rational(level, level + hv)


def verlinde_c1(
    lie_type: str, rank: int, level: int, genus: int
) -> Dict[str, Any]:
    r"""First Chern class of the Verlinde bundle.

    c_1(V_{g,k}) = rk(V_{g,k}) * slope * [lambda]

    Returns the coefficient of lambda in c_1, i.e.,
    c_1 / [lambda] = rk * slope.

    Also computes the shadow determinant line c_1:
        c_1(L_A) = kappa(A) * [lambda]

    The RATIO c_1(V) / c_1(L) encodes the quantum group data
    beyond the scalar shadow.
    """
    rk = verlinde_bundle_rank(lie_type, rank, level, genus)
    slope = verlinde_slope_general(lie_type, rank, level)
    kap = kappa_affine_exact(lie_type, rank, level)

    c1_verlinde = rk * slope  # coefficient of lambda
    c1_shadow = kap  # coefficient of lambda

    result = {
        "lie_type": lie_type, "rank": rank, "level": level, "genus": genus,
        "verlinde_rank": rk,
        "slope": slope,
        "c1_verlinde_coeff": c1_verlinde,  # c_1(V) / lambda
        "c1_shadow_coeff": c1_shadow,       # c_1(L_A) / lambda = kappa
        "kappa": kap,
    }

    if c1_shadow != 0:
        result["ratio_c1V_c1L"] = c1_verlinde / c1_shadow

    return result


# =========================================================================
# Section 3: Chern character of the Verlinde bundle as CohFT
# =========================================================================

def verlinde_cohft_unit(
    lie_type: str, rank: int, level: int
) -> Dict[str, Any]:
    r"""The genus-0 Frobenius algebra underlying the Verlinde CohFT.

    The Verlinde CohFT (Marian-Oprea-Pandharipande) is a SEMISIMPLE CohFT
    whose genus-0 data is the fusion algebra with the metric from the
    S-matrix.

    The fusion algebra has:
      - basis: integrable highest weights {lambda_0, ..., lambda_N}
      - metric: eta_{ij} = delta_{ij} (in the idempotent basis)
      - structure constants: fusion coefficients N_{ij}^k
      - unit: vacuum lambda_0

    In the canonical (idempotent) basis for semisimple Frobenius algebras:
      - eigenvalues of multiplication by lambda_i: S_{i,alpha}/S_{0,alpha}
      - metric: diag(Delta_alpha^2) where Delta_alpha = 1/S_{0,alpha}
    """
    weights = integrable_weights(lie_type, rank, level)
    n_wts = len(weights)
    S = S_matrix(lie_type, rank, level)

    # Quantum dimensions = eigenvalues in vacuum row
    qdims = np.array([abs(S[0, j]) / abs(S[0, 0]) for j in range(n_wts)])

    # Total quantum dimension squared
    D2 = sum(d**2 for d in qdims)

    # Canonical idempotent data
    # In the idempotent basis, the Frobenius algebra is diagonal:
    # e_alpha * e_beta = delta_{alpha,beta} / Delta_alpha * e_alpha
    # where Delta_alpha = S_{0,0} / S_{0,alpha} is the inverse qdim.
    deltas = np.array([abs(S[0, 0]) / abs(S[0, j])
                       if abs(S[0, j]) > 1e-15 else float('inf')
                       for j in range(n_wts)])

    return {
        "lie_type": lie_type, "rank": rank, "level": level,
        "num_weights": n_wts,
        "quantum_dims": qdims.tolist(),
        "D_squared": D2,
        "idempotent_norms": (1.0 / deltas**2).tolist(),
        "is_semisimple": True,  # Integrable affine = always semisimple
    }


def verlinde_R_matrix(
    lie_type: str, rank: int, level: int
) -> Dict[str, Any]:
    r"""R-matrix of the Verlinde CohFT in the Givental framework.

    For a semisimple CohFT, the Givental-Teleman reconstruction
    determines the full CohFT from genus-0 data + R-matrix.

    For the Verlinde bundle, the R-matrix is determined by:
      R_alpha(z) = exp(-slope * z / 2) * Id_alpha

    in each idempotent channel alpha, where slope = k/(k+h^v).

    More precisely, the R-matrix acts on each channel independently:
    in the idempotent basis {e_alpha}, R(z) = diag(R_alpha(z)) where

        R_alpha(z) = exp(sum_{m >= 1} r_m^{(alpha)} z^m)

    The FIRST coefficient r_1^{(alpha)} = -slope/2 = -k/(2(k+h^v))
    is universal (from the Hitchin connection's projective flatness).

    For our shadow CohFT, the R-matrix (thm:cohft-reconstruction) is
    R_A(z) = 1 + sum P_A^{(k)} z^k, the complementarity propagator.

    The comparison: the Verlinde R-matrix is the EXPONENTIAL of the
    shadow connection data, while the shadow R-matrix is the propagator
    P_A itself. These are related by Givental's quantization formula.
    """
    data = _get_lie_data(lie_type, rank)
    hv = data["hv"]
    slope = Rational(level, level + hv)
    n_wts = num_integrable_reps(lie_type, rank, level)

    # In the simplest approximation:
    # R_alpha(z) ≈ 1 - (slope/2) z + O(z^2)
    # The higher coefficients depend on the specific CohFT.

    return {
        "lie_type": lie_type, "rank": rank, "level": level,
        "slope": slope,
        "R_first_coeff": -slope / 2,  # coefficient of z in R(z)
        "num_channels": n_wts,
        "is_diagonal": True,  # semisimple => diagonal in idempotent basis
    }


# =========================================================================
# Section 4: Hitchin connection vs shadow connection comparison
# =========================================================================

def hitchin_shadow_comparison(
    lie_type: str, rank: int, level: int
) -> Dict[str, Any]:
    r"""Compare the Hitchin connection on conformal blocks with our
    shadow connection nabla^sh.

    HITCHIN CONNECTION (genus >= 1):
    The Verlinde bundle carries a PROJECTIVELY FLAT connection
    nabla^Hitchin with regular singularities along the boundary of
    M-bar_g.  Its curvature is a scalar:
        F(nabla^Hitchin) = (slope) * omega_{WP}
    where omega_{WP} is the Weil-Petersson form and
    slope = k/(k+h^v).

    This determines c_1(V) = rk * slope * lambda.

    SHADOW CONNECTION (our framework):
    nabla^sh = d - Q'_L/(2Q_L) dt is the shadow connection on the
    single-line shadow metric Q_L.  Its monodromy is -1 (Koszul sign).

    KEY RELATIONSHIP:
    The Hitchin connection acts on the FULL Verlinde bundle (rank = V_g).
    The shadow connection acts on the DETERMINANT LINE (rank = 1).
    The Hitchin connection, projected to the determinant, gives the
    shadow connection (up to a gauge transformation).

    Precisely: if nabla^H is the Hitchin connection on V_k, then
    det(nabla^H) = nabla^{det} is a connection on det(V_k) = L^{rk*slope},
    and c_1(det(V_k)) = rk * slope * lambda.

    Our shadow determinant line L_A has c_1(L_A) = kappa * lambda.
    The relationship: kappa ≠ rk * slope in general.

    For sl_2 at level k, genus 1:
        rk * slope = (k+1) * k/(k+2)
        kappa = 3(k+2)/4

    These are different: the Verlinde bundle DETERMINANT sees the
    quantum group structure (sum of S-matrix powers), while the
    shadow determinant sees only the scalar kappa.

    HOWEVER: the PROJECTIVE flatness of both connections is controlled
    by the SAME scalar: the central charge c (or equivalently kappa).
    The projective connection = connection mod scalars is universal.
    """
    data = _get_lie_data(lie_type, rank)
    hv = data["hv"]
    k = level

    slope = Rational(k, k + hv)
    kappa = kappa_affine_exact(lie_type, rank, k)
    c = central_charge(lie_type, rank, k)

    # Hitchin curvature coefficient (projective)
    hitchin_proj_curvature = slope

    # Shadow connection residue at t=0
    # nabla^sh = d - Q'/(2Q) dt, residue at zeros of Q
    shadow_residue = Rational(1, 2)  # Koszul monodromy -1

    # The projective part of both connections is controlled by c
    # Hitchin: curv = (c/dim) * omega_WP
    # Shadow: curv = (c/dim) * omega_WP (restricted to scalar line)
    proj_curvature_from_c = Rational(int(round(1000 * c)), 1000) / data["dim"]

    return {
        "lie_type": lie_type, "rank": rank, "level": level,
        "slope": slope,
        "kappa": kappa,
        "central_charge": c,
        "hitchin_proj_curvature_coeff": slope,
        "shadow_connection_residue": shadow_residue,
        "curvature_ratio": slope,  # c/dim = k/(k+h^v)
        "slope_equals_c_over_dim": abs(float(slope) - c / data["dim"]) < 1e-10,
    }


# =========================================================================
# Section 5: Factorization / sewing verification
# =========================================================================

def factorization_check_sl2(
    level: int, genus: int, partition: Tuple[int, int]
) -> Dict[str, Any]:
    r"""Verify factorization of conformal blocks (Beauville-Laszlo sewing).

    SEPARATING DEGENERATION:
    When a genus-g curve degenerates into two components of genera
    g_1 and g_2 (with g_1 + g_2 = g), joined at a node, the
    Verlinde dimension factorizes:

        V_g = sum_{j=0}^{k} V(Sigma_{g_1}, j) * V(Sigma_{g_2}, j)

    where V(Sigma_{g_i}, j) is the CB dimension with one insertion
    of spin j at the node.

    This is the SEWING AXIOM for conformal blocks, equivalent to
    the separating boundary axiom of the shadow CohFT
    (thm:shadow-cohft(ii)).

    In our framework (MC5, thm:general-hs-sewing): sewing convergence
    is proved for the entire standard landscape. The factorization
    check below verifies the algebraic identity underlying sewing.
    """
    g1, g2 = partition
    if g1 + g2 != genus:
        raise ValueError(f"Partition {partition} does not sum to genus {genus}")
    if g1 < 0 or g2 < 0:
        raise ValueError(f"Partition components must be non-negative")

    k = level
    V_g = verlinde_dimension_exact("A", 1, k, genus)

    # Factorized sum: sum_j V(Sigma_{g1}, j) * V(Sigma_{g2}, j)
    # V(Sigma_{g_i}, j) = conformal block dim at genus g_i with one
    # insertion of spin j
    factored_sum = 0
    channel_contributions = {}
    for j in range(k + 1):
        V1 = conformal_block_dim_sl2(k, g1, (j,))
        V2 = conformal_block_dim_sl2(k, g2, (j,))
        contrib = V1 * V2
        channel_contributions[j] = {"V1": V1, "V2": V2, "product": contrib}
        factored_sum += contrib

    return {
        "level": k, "genus": genus,
        "partition": partition,
        "V_g": V_g,
        "factored_sum": factored_sum,
        "factorization_holds": V_g == factored_sum,
        "channels": channel_contributions,
    }


def nonseparating_check_sl2(level: int, genus: int) -> Dict[str, Any]:
    r"""Verify non-separating degeneration (pinching a non-separating cycle).

    NONSEPARATING DEGENERATION:
    When a genus-g curve acquires a non-separating node (reducing to
    genus g-1 with two marked points identified), the Verlinde
    dimension satisfies:

        V_g = sum_{j=0}^{k} V(Sigma_{g-1}, j, j*)

    where j* is the conjugate representation.

    For sl_2: j* = j (all reps are self-conjugate).

    This is the non-separating boundary axiom of the shadow CohFT
    (thm:shadow-cohft(iii)).
    """
    if genus < 1:
        raise ValueError(f"Non-separating requires genus >= 1, got {genus}")

    k = level
    V_g = verlinde_dimension_exact("A", 1, k, genus)

    # Non-separating sum: V(Sigma_{g-1}, j, j) for all j
    nsep_sum = 0
    channel_contributions = {}
    for j in range(k + 1):
        # For sl_2, j* = j (self-conjugate)
        V_lower = conformal_block_dim_sl2(k, genus - 1, (j, j))
        channel_contributions[j] = V_lower
        nsep_sum += V_lower

    return {
        "level": k, "genus": genus,
        "V_g": V_g,
        "nonseparating_sum": nsep_sum,
        "nonseparating_holds": V_g == nsep_sum,
        "channels": channel_contributions,
    }


def factorization_check_general(
    lie_type: str, rank: int, level: int, genus: int,
    partition: Tuple[int, int]
) -> Dict[str, Any]:
    """Verify separating factorization for general type."""
    g1, g2 = partition
    if g1 + g2 != genus:
        raise ValueError(f"Partition {partition} does not sum to genus {genus}")

    V_g = verlinde_dimension_exact(lie_type, rank, level, genus)
    weights = integrable_weights(lie_type, rank, level)

    factored_sum = 0
    for wt in weights:
        # Conjugate weight for type A: reverse Dynkin labels
        if lie_type == "A":
            conj_wt = tuple(reversed(wt))
        else:
            conj_wt = wt  # Approximate: use same weight (correct for self-conjugate)

        V1 = conformal_block_dim_general(lie_type, rank, level, g1, (wt,))
        V2 = conformal_block_dim_general(lie_type, rank, level, g2, (conj_wt,))
        factored_sum += V1 * V2

    return {
        "lie_type": lie_type, "rank": rank, "level": level,
        "genus": genus, "partition": partition,
        "V_g": V_g,
        "factored_sum": factored_sum,
        "factorization_holds": V_g == factored_sum,
    }


# =========================================================================
# Section 6: Shadow CohFT vs Chern character comparison
# =========================================================================

def shadow_vs_chern_character(
    lie_type: str, rank: int, level: int, genus: int
) -> Dict[str, Any]:
    r"""Compare our shadow CohFT with the Chern character of the Verlinde bundle.

    QUESTION: Is the shadow CohFT Omega_{g,n}^A equal to ch(V_k)?

    ANSWER: NO. They are DIFFERENT objects that share the same genus-0
    Frobenius algebra structure but differ at higher genus.

    The shadow CohFT (thm:shadow-cohft) captures the BAR-COMPLEX
    obstruction to extending flat data from genus 0 to higher genus.
    Its scalar projection is F_g = kappa * lambda_g^FP.

    The Chern character of the Verlinde bundle [MOP14] captures the
    TOPOLOGICAL invariant of the conformal block vector bundle.
    Its scalar projection is ch_1(V_k) = rk * slope * lambda.

    KEY STRUCTURAL DIFFERENCE:
    1. Shadow CohFT: rank = dim(V) where V is the generator space.
       F_g ~ Bernoulli decay (Faber-Pandharipande).
    2. Verlinde CohFT: rank = V_g (Verlinde dimension, grows with g).
       ch_1 ~ exponential growth in g (since rk grows exponentially).

    WHAT THEY SHARE:
    - Same fusion algebra at genus 0 (when V = space of integrable reps)
    - Same projective connection (Hitchin = shadow up to scalars)
    - The RATIO ch_1(V) / rk(V) = slope * lambda is the AVERAGED
      version of the shadow obstruction kappa * lambda.

    BRIDGE: The shadow CohFT is the "logarithmic derivative" of the
    Verlinde CohFT in the following sense:
        slope = k/(k+h^v) = c/dim
        kappa = dim * (k+h^v) / (2h^v)
        slope = (kappa - dim/2) * (2/dim)   [for the shifted version]

    Actually: slope = c/dim(g), while kappa = (c + dim)/2 (for KM).
    These are linearly related but NOT equal.
    """
    data = _get_lie_data(lie_type, rank)
    k = level
    hv = data["hv"]
    dim_g = data["dim"]

    rk_V = verlinde_bundle_rank(lie_type, rank, k, genus)
    slope = verlinde_slope_general(lie_type, rank, k)
    kap = kappa_affine_exact(lie_type, rank, k)
    c = central_charge(lie_type, rank, k)

    # Shadow CohFT scalar (genus g, no insertions)
    if genus >= 1:
        F_shadow = shadow_F_g(lie_type, rank, k, genus)
    else:
        F_shadow = Rational(0)

    # Verlinde CohFT c_1 coefficient
    c1_verlinde = rk_V * slope

    # Comparisons
    result = {
        "lie_type": lie_type, "rank": rank, "level": k, "genus": genus,
        "dim_g": dim_g, "h_dual": hv,
        "central_charge": c,
        "kappa": kap,
        "slope": slope,
        "verlinde_rank": rk_V,
        "shadow_F_g": float(F_shadow) if genus >= 1 else 0,
        "c1_verlinde": float(c1_verlinde),
        "c1_shadow_det": float(kap),
        "slope_equals_c_over_dim": abs(float(slope) - c / dim_g) < 1e-10,
    }

    if genus >= 1 and float(F_shadow) != 0:
        result["ratio_c1V_over_Fshadow"] = float(c1_verlinde) / float(F_shadow)

    return result


def genus1_three_way_comparison(
    lie_type: str, rank: int, level: int
) -> Dict[str, Any]:
    r"""At genus 1, three quantities to compare:

    1. V_1 = number of integrable reps |P_+^k|
    2. F_1 = kappa / 24 (shadow scalar partition function)
    3. c_1(V) / lambda = rk * slope = V_1 * k/(k+h^v)

    Key relationships:
    - V_1 / F_1 = 24 * V_1 / kappa (ratio of full to scalar)
    - c_1(V) / c_1(L) = V_1 * slope / kappa (ratio of Verlinde to shadow c_1)

    At genus 1, V_1 = |P_+^k| (integer), while F_1 is typically fractional.
    The ratio V_1 / F_1 encodes the quantum-group information beyond kappa.
    """
    data = _get_lie_data(lie_type, rank)
    hv = data["hv"]
    k = level

    V1 = verlinde_dimension_exact(lie_type, rank, k, 1)
    F1 = float(shadow_F_g(lie_type, rank, k, 1))
    kap = kappa_affine_exact(lie_type, rank, k)
    slope = Rational(k, k + hv)
    c1_V = V1 * slope
    c1_L = kap

    return {
        "lie_type": lie_type, "rank": rank, "level": k,
        "V_1": V1,
        "F_1": F1,
        "kappa": float(kap),
        "slope": float(slope),
        "c1_verlinde": float(c1_V),
        "c1_shadow_det": float(c1_L),
        "ratio_V1_over_F1": V1 / F1 if F1 != 0 else None,
        "ratio_c1V_over_c1L": float(c1_V / c1_L) if c1_L != 0 else None,
    }


# =========================================================================
# Section 7: C2-cofiniteness and finite generation
# =========================================================================

def c2_cofiniteness_check(
    lie_type: str, rank: int, level: int
) -> Dict[str, Any]:
    r"""Check C2-cofiniteness conditions for affine VOAs.

    C2-COFINITENESS [DGT19]:
    A VOA V is C2-cofinite if V/C_2(V) is finite-dimensional,
    where C_2(V) = span{a_{(-2)} b : a, b in V}.

    For affine KM at positive integer level: ALWAYS C2-cofinite
    (and in fact RATIONAL = C2-cofinite + finitely many simple modules).

    Consequence [DGT19, DGT19b]:
    - Coinvariants form quasi-coherent sheaves on M-bar_{g,n}
    - These sheaves have twisted D-module structure
    - Under rationality: sheaves are VECTOR BUNDLES of finite rank
    - The connection has REGULAR SINGULARITIES along boundary

    For non-rational VOAs (e.g., Virasoro at generic c, admissible levels):
    - C2-cofiniteness may fail
    - Conformal blocks may be infinite-dimensional
    - Connection may have IRREGULAR singularities

    IMPLICATION FOR OUR FRAMEWORK:
    Koszulness (our framework) implies C2-cofiniteness for the standard
    landscape. The shadow CohFT exists for ALL Koszul algebras, but
    the interpretation as Chern character of a vector bundle requires
    C2-cofiniteness + rationality.
    """
    data = _get_lie_data(lie_type, rank)
    k = level

    n_reps = num_integrable_reps(lie_type, rank, k)

    # For integrable affine: always C2-cofinite and rational
    is_c2_cofinite = True
    is_rational = True
    n_simples = n_reps  # number of simple modules = integrable reps

    # The conformal block bundle has rank V_g at genus g
    # This is finite for all g (guaranteed by C2-cofiniteness + rationality)

    return {
        "lie_type": lie_type, "rank": rank, "level": k,
        "is_c2_cofinite": is_c2_cofinite,
        "is_rational": is_rational,
        "num_simple_modules": n_simples,
        "conformal_blocks_are_vector_bundles": is_c2_cofinite and is_rational,
        "connection_regular_singularities": is_c2_cofinite,
    }


# =========================================================================
# Section 8: Determinant line bundle and bar complex comparison
# =========================================================================

def determinant_line_comparison(
    lie_type: str, rank: int, level: int, max_genus: int = 5
) -> Dict[str, Any]:
    r"""Compare the determinant line of the Verlinde bundle with our L_A.

    Two determinant lines:

    1. det(V_k) = (det of Verlinde bundle) = a line bundle on M_g
       c_1(det V_k) = c_1(V_k) = rk * slope * lambda

    2. L_A = det R pi_{g*} B-bar^{ch,(g)}(A)  (our determinant line)
       c_1(L_A) = kappa * lambda

    These are DIFFERENT line bundles with DIFFERENT c_1:
       c_1(det V_k) = rk(V_g) * k/(k+h^v) * lambda
       c_1(L_A) = dim(g)*(k+h^v)/(2h^v) * lambda

    The ratio encodes the relationship between:
    - The quantum group (Verlinde bundle, exponential rank growth)
    - The modular obstruction (bar complex, fixed kappa)

    As g -> infinity:
       c_1(det V_k) / lambda ~ rk(V_g) * slope ~ D^{2g-2} * slope
       c_1(L_A) / lambda = kappa (constant!)

    So the Verlinde determinant diverges exponentially while the
    shadow determinant is CONSTANT across all genera.
    """
    data = _get_lie_data(lie_type, rank)
    k = level
    hv = data["hv"]

    kap = kappa_affine_exact(lie_type, rank, k)
    slope = Rational(k, k + hv)

    genus_data = []
    for g in range(1, max_genus + 1):
        rk = verlinde_bundle_rank(lie_type, rank, k, g)
        c1_V = rk * slope
        c1_L = kap
        F_g_val = shadow_F_g(lie_type, rank, k, g)

        genus_data.append({
            "genus": g,
            "verlinde_rank": rk,
            "c1_det_verlinde": float(c1_V),
            "c1_shadow_det": float(c1_L),
            "ratio": float(c1_V / c1_L) if c1_L != 0 else None,
            "shadow_F_g": float(F_g_val),
        })

    return {
        "lie_type": lie_type, "rank": rank, "level": k,
        "kappa": float(kap),
        "slope": float(slope),
        "genus_data": genus_data,
        "shadow_det_constant": True,  # kappa doesn't depend on g
        "verlinde_det_grows": True,   # rk grows, so c1(det V) grows
    }


# =========================================================================
# Section 9: Beauville-Laszlo sewing and MC5
# =========================================================================

def beauville_laszlo_sewing_verification(
    level: int, max_genus: int = 4
) -> Dict[str, Any]:
    r"""Verify the Beauville-Laszlo sewing identity for sl_2.

    The Beauville-Laszlo theorem provides the algebraic framework for
    sewing conformal blocks from local data on the formal disc.

    In our framework (MC5, thm:general-hs-sewing):
    - Sewing convergence is proved for the standard landscape
    - The sewing identity is the FACTORIZATION axiom of the CohFT
    - Both the shadow CohFT and the Verlinde CohFT satisfy it

    This function verifies BOTH factorization axioms:
    (1) Separating: V_g = sum_j V(g_1, j) * V(g_2, j)
    (2) Non-separating: V_g = sum_j V(g-1, j, j)

    for all partitions of g.
    """
    k = level
    results = {
        "level": k,
        "separating": [],
        "nonseparating": [],
        "all_pass": True,
    }

    for g in range(2, max_genus + 1):
        # Non-separating check
        nsep = nonseparating_check_sl2(k, g)
        results["nonseparating"].append(nsep)
        if not nsep["nonseparating_holds"]:
            results["all_pass"] = False

        # Separating checks: all (g1, g2) with g1+g2=g, g1 >= g2 >= 0
        for g1 in range(g, (g - 1) // 2, -1):
            g2 = g - g1
            if g1 >= 0 and g2 >= 0:
                sep = factorization_check_sl2(k, g, (g1, g2))
                results["separating"].append(sep)
                if not sep["factorization_holds"]:
                    results["all_pass"] = False

    return results


# =========================================================================
# Section 10: Full VOA bundle diagnostic
# =========================================================================

def full_voa_bundle_diagnostic(
    lie_type: str, rank: int, level: int, max_genus: int = 4
) -> Dict[str, Any]:
    """Complete diagnostic for VOA bundles on moduli of curves.

    Collects:
    1. Conformal block dimensions at all genera
    2. Verlinde bundle c_1 and slope
    3. Shadow CohFT comparison
    4. Factorization verification (for sl_2)
    5. C2-cofiniteness status
    6. Hitchin vs shadow connection comparison
    """
    result = {
        "algebra": _get_lie_data(lie_type, rank)["name"],
        "lie_type": lie_type, "rank": rank, "level": level,
    }

    # Basic invariants
    result["kappa"] = float(kappa_affine_exact(lie_type, rank, level))
    result["central_charge"] = central_charge(lie_type, rank, level)
    result["slope"] = float(verlinde_slope_general(lie_type, rank, level))
    result["num_reps"] = num_integrable_reps(lie_type, rank, level)

    # Genus-by-genus data
    genus_data = {}
    for g in range(max_genus + 1):
        gd = {"genus": g}
        gd["verlinde_dim"] = verlinde_dimension_exact(lie_type, rank, level, g)
        if g >= 1:
            gd["shadow_F_g"] = float(shadow_F_g(lie_type, rank, level, g))
            c1_info = verlinde_c1(lie_type, rank, level, g)
            gd["c1_verlinde"] = float(c1_info["c1_verlinde_coeff"])
            gd["c1_shadow"] = float(c1_info["c1_shadow_coeff"])
        genus_data[g] = gd
    result["genus_data"] = genus_data

    # C2-cofiniteness
    result["c2_check"] = c2_cofiniteness_check(lie_type, rank, level)

    # Hitchin comparison
    result["hitchin_comparison"] = hitchin_shadow_comparison(
        lie_type, rank, level
    )

    # Genus-1 three-way
    result["genus1_comparison"] = genus1_three_way_comparison(
        lie_type, rank, level
    )

    return result


# =========================================================================
# Section 11: Conformal block dimension tables (sl_2)
# =========================================================================

def sl2_conformal_block_table(
    level: int, max_genus: int = 3, max_insertions: int = 2
) -> Dict[str, Any]:
    """Build a table of conformal block dimensions for sl_2.

    Returns dimensions V(Sigma_g, j_1, ..., j_n) for:
    - genus g = 0, ..., max_genus
    - n = 0, 1, 2, ... max_insertions marked points
    - all spin configurations
    """
    k = level
    table = {}

    for g in range(max_genus + 1):
        for n in range(max_insertions + 1):
            if 2 * g - 2 + n <= 0 and not (g == 0 and n >= 3):
                # Need 2g - 2 + n > 0 for stability
                # Exception: g=0 needs n >= 3
                if g == 0 and n < 3:
                    continue
                if g == 1 and n < 1:
                    # g=1, n=0 is stable
                    pass

            # Generate all spin configurations
            if n == 0:
                configs = [()]
            else:
                configs = _generate_spin_configs(k, n)

            for spins in configs:
                try:
                    dim = conformal_block_dim_sl2(k, g, spins)
                    table[(g, spins)] = dim
                except Exception:
                    pass

    return {"level": k, "table": table}


def _generate_spin_configs(k: int, n: int) -> List[Tuple[int, ...]]:
    """Generate all spin configurations (j_1,...,j_n) with 0 <= j_i <= k."""
    if n == 0:
        return [()]
    if n == 1:
        return [(j,) for j in range(k + 1)]
    configs = []
    for j in range(k + 1):
        for sub in _generate_spin_configs(k, n - 1):
            configs.append((j,) + sub)
    return configs


# =========================================================================
# Section 12: Verlinde bundle Chern numbers
# =========================================================================

def verlinde_chern_numbers(
    lie_type: str, rank: int, level: int, max_genus: int = 5
) -> Dict[str, Any]:
    r"""Compute Chern numbers of the Verlinde bundle integrated against
    tautological classes on M-bar_g.

    For the Verlinde bundle V_k on M_g:
      rk(V_k) = Verlinde dimension V_g
      c_1(V_k) = rk * slope * lambda
      c_1 integrated against [M_g]: uses int_{M_g} lambda = lambda_g^FP

    So:
      int_{M_g} c_1(V_k) = rk(V_g) * slope * lambda_g^FP

    Compare with shadow:
      int_{M_g} c_1(L_A) = kappa * lambda_g^FP = F_g

    The ratio:
      int c_1(V) / int c_1(L) = rk(V_g) * slope / kappa
    """
    data = _get_lie_data(lie_type, rank)
    hv = data["hv"]
    k = level
    kap = kappa_affine_exact(lie_type, rank, k)
    slope = Rational(k, k + hv)

    genus_results = []
    for g in range(1, max_genus + 1):
        rk = verlinde_bundle_rank(lie_type, rank, k, g)
        fp = lambda_fp(g)

        int_c1_V = rk * slope * fp  # integral of c_1(V) over M_g
        int_c1_L = kap * fp          # integral of c_1(L) = shadow F_g

        genus_results.append({
            "genus": g,
            "verlinde_rank": rk,
            "int_c1_verlinde": float(int_c1_V),
            "int_c1_shadow": float(int_c1_L),
            "ratio": float(int_c1_V / int_c1_L) if int_c1_L != 0 else None,
            "lambda_fp": float(fp),
        })

    return {
        "lie_type": lie_type, "rank": rank, "level": k,
        "kappa": float(kap),
        "slope": float(slope),
        "genus_results": genus_results,
    }
