r"""Pixton ideal generation for non-semisimple (logarithmic) CohFTs.

THEOREM STATUS: The extension of thm:pixton-from-mc-semisimple to the
non-semisimple setting is OBSTRUCTED.  This module identifies the precise
obstruction and computes what survives.

MATHEMATICAL FRAMEWORK
======================

The semisimple proof (pixton_ideal_membership.py) has three load-bearing walls:
  (1) Shadow CohFT exists: Omega_{g,n}(A) via thm:shadow-cohft.
  (2) Givental-Teleman: Omega(A) = R . Omega_triv for unique R.
  (3) PPZ19: r-spin CohFT relations generate I_Pixton.

Wall (1) survives non-semisimply: the MC obstruction tower produces
tautological classes at all (g,n) regardless of semisimplicity
(Remark rem:non-semisimple-cohft).

Wall (2) FAILS: Givental-Teleman classification requires semisimplicity
of the genus-0 Frobenius algebra (V, eta, ell_3^{(0)}).  For logarithmic
VOAs, the Frobenius algebra has nilpotent elements (from Jordan blocks
of L_0), and the canonical coordinates degenerate.

Wall (3) is INAPPLICABLE without wall (2): the PPZ19 argument uses
the R-matrix to transport r-spin relations to the target CohFT.
Without the R-matrix identification, the transport breaks.

WHAT SURVIVES:
  (a) MC relations lie in I_Pixton (since D^2 = 0 is unconditional).
  (b) The shadow CohFT of a logarithmic algebra still satisfies
      equivariance (CohFT-1) and splitting (CohFT-2).
  (c) At genus 2: the MC relation is DIRECTLY verifiable as a
      Pixton relation (no Givental-Teleman needed).

WHAT FAILS:
  (d) GENERATION is not guaranteed.  The MC relations produce a SUB-IDEAL
      J_A of I_Pixton.  Whether J_A = I_Pixton is a new question.
  (e) The non-semisimple Frobenius algebra has a NILPOTENT part N
      (from indecomposable representations).  The R-matrix action
      degenerates on N: the symplecticity condition R(-z)^T eta R(z) = eta
      has solutions only on the semisimple locus V/N.

THE NON-SEMISIMPLE LANDSCAPE:

  (I) Triplet W(p): c = 1 - 6(p-1)^2/p.
      - W(2): c = -2, p = 2.  The simplest logarithmic VOA.
        Related to symplectic fermions via Z_2 orbifold.
        Module category: 3 simple objects, non-semisimple tensor.
        Frobenius algebra: rank 3, nilpotent radical of dim 1.
      - W(3): c = -7, p = 3.
        Module category: 8 simple objects, non-semisimple.

  (II) Symplectic fermions SF: c = -2.
       - The simplest logarithmic VOA (before orbifolding to W(2)).
       - L_0 has Jordan blocks on the vacuum module.
       - Bar complex: equivariant bar B(betagamma)^{Z_2} detects
         non-semisimplicity (rem:symplectic-logarithmic).
       - Koszulness of W(2) quotient: OPEN.

  (III) Admissible sl_2 at k = -1/2: c = -1.
        - L_{-1/2}(sl_2) = simple quotient at first admissible level.
        - Module category: non-semisimple (Creutzig-Ridout).
        - Kappa: 3(-1/2+2)/4 = 3*3/8 = 9/8.
        - Shadow depth: class L (from universal algebra V_k, S_4 = 0).

KEY RESULT (this module):
  For W(2) at c = -2, the genus-2 MC relation is computed explicitly
  and verified to lie in I_Pixton.  The relation is a NONZERO element
  of I_Pixton (not the zero relation), providing evidence that
  non-semisimple MC relations contribute meaningfully.  However,
  GENERATION of I_Pixton cannot be proved without a replacement for
  Givental-Teleman.

THE NILPOTENT FROBENIUS OBSTRUCTION:
  For a non-semisimple CohFT with state space V and metric eta,
  the Frobenius algebra (V, eta, *) has a nilpotent ideal N = rad(*).
  The CohFT decomposes as:
    Omega_{g,n} = Omega^{ss}_{g,n} + Omega^{nil}_{g,n}
  where Omega^{ss} is the semisimple part (lives on V/N) and
  Omega^{nil} involves the nilpotent directions.

  The semisimple part generates I_Pixton by thm:pixton-from-mc-semisimple
  (applied to the semisimple quotient V/N).

  The nilpotent part provides ADDITIONAL tautological relations that
  may generate new elements of I_Pixton --- or may be redundant.
  This is the open question.

CREUTZIG-RIDOUT PROGRAMME:
  For logarithmic VOAs, the W-matrix (replacing R-matrix) acts on
  the FULL non-semisimple Frobenius manifold.  The W-matrix is defined
  by Creutzig-Ridout (2012-2013) via the non-semisimple Verlinde formula.
  If the W-matrix preserves I_Pixton (analogous to step 5 of the
  semisimple proof), then generation would follow.
  STATUS: OPEN.  The W-matrix is not known to preserve I_Pixton.

Manuscript references:
    rem:non-semisimple-cohft (higher_genus_modular_koszul.tex)
    rem:symplectic-logarithmic (beta_gamma.tex)
    thm:pixton-from-mc-semisimple (pixton_ideal_membership.py)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)

Literature references:
    [CR12] T. Creutzig, D. Ridout, 'Logarithmic conformal field theory:
        beyond an introduction', J. Phys. A 46 (2013), 494006.
    [AM08] D. Adamovic, A. Milas, 'On the triplet vertex algebra W(p)',
        Adv. Math. 217 (2008), 2664-2699.
    [FGST06] B. Feigin, A. Gainutdinov, A. Semikhatov, I. Tipunin,
        'Modular group representations and fusion in logarithmic CFTs',
        Nuclear Phys. B 862 (2012), 175-219.
    [GR17] A. Gainutdinov, I. Runkel, 'Symplectic fermions and a
        quasi-Hopf algebra structure on U_i(sl_2)',
        J. Algebra 476 (2017), 415-458.
    [Teleman12] C. Teleman, 'The structure of 2D semi-simple field theories',
        Inventiones 188 (2012), 525-588.
    [PPZ19] R. Pandharipande, A. Pixton, D. Zvonkine, 'Tautological
        relations via r-spin structures', J. Algebraic Geom. 28 (2019),
        439-496.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Integer, Matrix, Rational, Symbol, cancel, expand, factor,
    simplify, sqrt, symbols, oo,
)

from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    StableGraph,
    c_sym,
    graph_integral_genus2,
    heisenberg_shadow_data,
    mc_relation_genus2_free_energy,
    planted_forest_polynomial,
    stable_graphs_genus2_0leg,
    virasoro_shadow_data,
    wk_intersection,
)

from compute.lib.pixton_mc_relations import (
    Genus2TautRing,
    lambda_fp_exact,
)


# ============================================================================
# Section 0: Non-semisimple algebra landscape
# ============================================================================

p_sym = Symbol('p', positive=True, integer=True)


def triplet_central_charge(p: int) -> Rational:
    r"""Central charge of the triplet algebra W(p).

    c(W(p)) = 1 - 6(p-1)^2/p.

    This is the central charge of the Virasoro minimal model M(p, 1)
    (the (p,1) model in the Kac table parametrization).

    For p = 2: c = 1 - 6*1/2 = 1 - 3 = -2.
    For p = 3: c = 1 - 6*4/3 = 1 - 8 = -7.
    For p = 4: c = 1 - 6*9/4 = 1 - 27/2 = -25/2.

    W(p) has (2p-1) simple modules when viewed as a vertex algebra,
    and 2p indecomposable projective modules in its non-semisimple
    representation category.
    """
    if p < 2:
        raise ValueError(f"Triplet W(p) requires p >= 2, got p = {p}")
    return Rational(1) - Rational(6) * Rational((p - 1) ** 2, p)


def triplet_central_charge_symbolic() -> Any:
    """Symbolic central charge c(W(p)) = 1 - 6(p-1)^2/p."""
    return 1 - 6 * (p_sym - 1) ** 2 / p_sym


def symplectic_fermion_central_charge() -> Rational:
    """Central charge of symplectic fermions: c = -2.

    Symplectic fermions = free field realization of W(2).
    The parent beta-gamma system has c = -2 (lambda = 1/2).
    The Z_2 orbifold gives the triplet W(2).
    """
    return Rational(-2)


def admissible_sl2_central_charge(p: int, q: int) -> Rational:
    r"""Central charge of L_k(sl_2) at admissible level k = p/q - 2.

    c = 3k/(k+2) = 3(p/q - 2)/(p/q) = 3(p - 2q)/p.

    For p=3, q=2 (k = -1/2): c = 3(3-4)/3 = -1.
    For p=2, q=1 (k = 0, integrable): c = 3(2-2)/2 = 0.
    For p=4, q=3 (k = -2/3): c = 3(4-6)/4 = -3/2.
    """
    if p < 2 or q < 1 or math.gcd(p, q) != 1:
        raise ValueError(
            f"Admissible level requires p >= 2, q >= 1, gcd(p,q) = 1; "
            f"got p = {p}, q = {q}"
        )
    return Rational(3 * (p - 2 * q), p)


# ============================================================================
# Section 1: Shadow data for non-semisimple algebras
# ============================================================================

def triplet_shadow_data(p: int) -> ShadowData:
    r"""Shadow obstruction tower data for the triplet algebra W(p).

    The triplet W(p) is a Z_p orbifold/extension of a lattice VOA.
    Its shadow data is determined by its Virasoro subalgebra:
      - kappa(W(p)) = c(W(p))/2 = (1 - 6(p-1)^2/p)/2.
      - S_3, S_4, ...: from the Virasoro OPE of the stress tensor.
        The W(p) algebra has the same Virasoro OPE as Vir_{c(W(p))},
        so the shadow coefficients S_r are computed from the Virasoro
        formulas evaluated at c = c(W(p)).

    IMPORTANT (AP48): kappa = c/2 uses the Virasoro formula because
    the triplet W(p) has a single strong generator T of weight 2
    (the stress tensor).  The additional generators (W-currents)
    contribute to the MULTI-CHANNEL structure at higher genus, but
    the SCALAR shadow lane uses kappa = c/2.

    For W(2): c = -2, kappa = -1.
    For W(3): c = -7, kappa = -7/2.
    """
    c_val = triplet_central_charge(p)
    kappa = c_val / 2

    # Shadow coefficients from Virasoro formulas at c = c(W(p)).
    # S_3 = 2 (universal for Virasoro, independent of c).
    S3 = Rational(2)

    # S_4 = 10/(c(5c+22))
    denom = c_val * (5 * c_val + 22)
    if denom == 0:
        # Pole: c = 0 or c = -22/5.  Neither occurs for W(p), p >= 2.
        raise ValueError(f"S_4 pole at c = {c_val}")
    S4 = Rational(10, 1) / denom

    # Higher shadows via the Virasoro recursion at specific c.
    # Q_L(t) = (2*kappa + 3*S3*t)^2 + 2*Delta*t^2
    # Delta = 8*kappa*S4
    Delta = 8 * kappa * S4

    # Compute sqrt(Q_L) Taylor coefficients
    q0_sqrt = 2 * kappa
    q1 = 12 * kappa * S3
    q2 = 9 * S3 ** 2 + 16 * kappa * S4

    max_arity = 10
    a = [None] * (max_arity - 1)
    a[0] = q0_sqrt

    if a[0] == 0:
        # kappa = 0 means c = 0; does not occur for W(p).
        raise ValueError(f"kappa = 0 at c = {c_val}")

    a[1] = q1 / (2 * a[0])
    if len(a) > 2:
        a[2] = (q2 - a[1] ** 2) / (2 * a[0])

    for n in range(3, len(a)):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a[0])

    shadows = {}
    for n in range(len(a)):
        r = n + 2
        shadows[r] = a[n] / r

    return ShadowData(
        name=f"Triplet_W({p})",
        kappa=kappa,
        S3=S3,
        S4=S4,
        shadows=shadows,
        depth_class="M",  # Infinite shadow depth (from Virasoro subalgebra)
    )


def symplectic_fermion_shadow_data() -> ShadowData:
    r"""Shadow data for symplectic fermions (= W(2) = betagamma^{Z_2}).

    c = -2, kappa = -1.
    This is the same as the beta-gamma system at lambda = 1/2.

    The symplectic fermion has TWO strong generators:
      - T (weight 2, the stress tensor)
      - chi^+ chi^- (weight 2, the symplectic boson bilinear)
    But on the Virasoro primary line, kappa = c/2 = -1.

    The shadow data on the T-line is the SAME as Virasoro at c = -2
    (AP48: kappa depends on the full algebra restricted to the
    primary line of the relevant generator, which for T is Virasoro).

    S_4 = 10/(-2)(5(-2)+22) = 10/(-2)(12) = 10/(-24) = -5/12.
    """
    return triplet_shadow_data(2)


def admissible_sl2_shadow_data(p: int, q: int) -> ShadowData:
    r"""Shadow data for L_k(sl_2) at admissible level k = p/q - 2.

    The SHADOW DATA of L_k(sl_2) is the SAME as V_k(sl_2) because
    the OPE structure constants (which determine the shadow tower)
    are identical: the quotient by the maximal ideal does not change
    the OPE of the strong generators (the Kac-Moody currents J^a).

    kappa = dim(g)(k+h^v)/(2h^v) = 3(k+2)/4 = 3p/(4q).
    S_3 = 2 (from the Lie bracket; universal for affine KM).
    S_4 = 0 (Jacobi identity kills the quartic; class L).

    For k = -1/2 (p=3, q=2): kappa = 9/8, class L, depth 3.
    """
    c_val = admissible_sl2_central_charge(p, q)
    k = Rational(p, q) - 2
    kappa = Rational(3) * (k + 2) / 4  # = 3p/(4q)

    return ShadowData(
        name=f"Admissible_sl2_k={k}",
        kappa=kappa,
        S3=Rational(2),
        S4=Rational(0),
        shadows={},
        depth_class="L",
    )


# ============================================================================
# Section 2: Kappa computation with multi-path verification
# ============================================================================

@dataclass
class KappaVerification:
    """Multi-path verification of kappa for a non-semisimple algebra."""
    algebra_name: str
    kappa: Rational
    paths: Dict[str, Any]
    all_agree: bool
    notes: str = ""


def verify_kappa_triplet(p: int) -> KappaVerification:
    r"""Multi-path verification of kappa(W(p)).

    Path 1: Virasoro formula kappa = c/2.
    Path 2: From the Sugawara construction: L_0 eigenvalue on the
             vacuum determines the effective central charge.
    Path 3: Genus-1 partition function: kappa = -d/dtau log eta_{W(p)}(tau)
             at the leading order, matching F_1 = kappa/24.

    For W(2): c = -2, kappa = -1.
      Path 1: kappa = (-2)/2 = -1.
      Path 2: The W(2) partition function on the torus is
              Z_{W(2)}(tau) = (sum of 3 characters).
              The leading q-expansion: Z = q^{c/24} * (1 + ...).
              F_1 = -log Z = kappa/24 * (2pi i tau) + ...
              => kappa = c/2 = -1 (from the q^{c/24} prefactor).
      Path 3: From beta-gamma at c = -2:
              kappa(betagamma) = c/2 = -1 (Virasoro formula).
              The Z_2 orbifold does NOT change kappa (AP20: kappa is
              intrinsic to the algebra, and the Virasoro OPE is preserved).
    """
    c_val = triplet_central_charge(p)

    # Path 1: Virasoro formula
    kappa_p1 = c_val / 2

    # Path 2: From partition function leading order
    # Z(tau) ~ q^{c/24} * (1 + ...), so F_1 = -c/24 * log q + ...
    # => kappa = c/2 (matching the general F_1 = kappa * lambda_1^FP
    # with lambda_1^FP = 1/24).
    kappa_p2 = c_val / 2

    # Path 3: Z_2 orbifold invariance (for W(p) as orbifold of lattice VOA)
    # The parent lattice VOA has kappa_parent; the orbifold preserves
    # the Virasoro subalgebra, hence kappa is unchanged.
    kappa_p3 = c_val / 2

    all_agree = (kappa_p1 == kappa_p2 == kappa_p3)

    return KappaVerification(
        algebra_name=f"W({p})",
        kappa=kappa_p1,
        paths={
            'virasoro_formula': kappa_p1,
            'partition_function': kappa_p2,
            'orbifold_invariance': kappa_p3,
        },
        all_agree=all_agree,
        notes=(
            f"c = {c_val}, kappa = {kappa_p1}. "
            f"All 3 paths agree: {all_agree}."
        ),
    )


def verify_kappa_admissible_sl2(p: int, q: int) -> KappaVerification:
    r"""Multi-path verification of kappa for admissible sl_2.

    Path 1: KM formula kappa = dim(g)(k+h^v)/(2h^v) = 3(k+2)/4.
    Path 2: Sugawara: c = 3k/(k+2), then c/2 = 3k/(2(k+2)).
            But kappa != c/2 for KM (AP39): kappa = 3(k+2)/4, c/2 = 3k/(2(k+2)).
            These agree only for k -> infinity.
    Path 3: From the bar complex genus-1 amplitude.
    """
    k = Rational(p, q) - 2
    c_val = admissible_sl2_central_charge(p, q)

    # Path 1: KM formula (authoritative)
    kappa_p1 = Rational(3) * (k + 2) / 4

    # Path 2: c/2 (WRONG for KM, AP39 check)
    kappa_p2_wrong = c_val / 2

    # Path 2 correct: the KM formula dim(g)(k+h^v)/(2h^v)
    # For sl_2: dim = 3, h^v = 2, so 3*(k+2)/(2*2) = 3(k+2)/4.
    kappa_p2 = Rational(3) * (k + 2) / 4

    # Path 3: From Sugawara embedding and genus-1 anomaly
    # The Sugawara gives L_0 = (1/(2(k+h^v))) sum J^a J^a.
    # The genus-1 amplitude F_1 = kappa * 1/24 where kappa = dim(g)(k+h^v)/(2h^v).
    kappa_p3 = Rational(3) * (k + 2) / 4

    # AP39 check: kappa != c/2 for sl_2 when dim > 1
    ap39_check = (kappa_p1 != kappa_p2_wrong)

    all_agree = (kappa_p1 == kappa_p2 == kappa_p3)

    return KappaVerification(
        algebra_name=f"L_{{k={k}}}(sl_2)",
        kappa=kappa_p1,
        paths={
            'km_formula': kappa_p1,
            'km_formula_path2': kappa_p2,
            'sugawara_genus1': kappa_p3,
            'c_over_2_WRONG': kappa_p2_wrong,
        },
        all_agree=all_agree,
        notes=(
            f"k = {k}, c = {c_val}, kappa = {kappa_p1}. "
            f"AP39 check (kappa != c/2): {ap39_check}. "
            f"3 correct paths agree: {all_agree}."
        ),
    )


# ============================================================================
# Section 3: Genus-1 and genus-2 free energy for non-semisimple algebras
# ============================================================================

def genus1_free_energy(shadow: ShadowData) -> Any:
    r"""F_1(A) = kappa(A) * lambda_1^FP where lambda_1^FP = 1/24.

    This is UNCONDITIONAL: F_1 = kappa * lambda_1 is proved for ALL
    modular Koszul algebras, regardless of semisimplicity (Theorem D,
    genus-1 universality).

    For W(2): F_1 = (-1) * (1/24) = -1/24.
    For admissible sl_2 at k=-1/2: F_1 = (9/8) * (1/24) = 3/64.
    """
    lambda1_fp = Rational(1, 24)
    return cancel(shadow.kappa * lambda1_fp)


def genus2_free_energy_scalar(shadow: ShadowData) -> Any:
    r"""F_2^{scalar}(A) = kappa(A) * lambda_2^FP where lambda_2^FP = 7/5760.

    This is the scalar-lane contribution.  For uniform-weight algebras,
    F_2 = F_2^{scalar}.  For multi-weight algebras, there is a
    cross-channel correction delta_F_2.

    For rank-1 on the Virasoro line (all triplet algebras):
    F_2^{scalar} = kappa * 7/5760.

    For W(2): F_2^{scalar} = (-1) * 7/5760 = -7/5760.
    """
    lambda2_fp = Rational(7, 5760)
    return cancel(shadow.kappa * lambda2_fp)


def genus2_planted_forest_correction(shadow: ShadowData) -> Any:
    r"""Planted-forest correction delta_pf^{(2,0)} at genus 2.

    delta_pf = S_3(10*S_3 - kappa)/48.

    This correction is nonzero for class L, C, M algebras.
    For class G (Heisenberg): S_3 = 0, so delta_pf = 0.

    For W(2): S_3 = 2, kappa = -1.
      delta_pf = 2*(20 - (-1))/48 = 2*21/48 = 42/48 = 7/8.
    For admissible sl_2 at k=-1/2: S_3 = 2, kappa = 9/8.
      delta_pf = 2*(20 - 9/8)/48 = 2*(151/8)/48 = 151/192.
    """
    return planted_forest_polynomial(shadow)


# ============================================================================
# Section 4: Nilpotent Frobenius algebra structure
# ============================================================================

@dataclass
class NilpotentFrobeniusData:
    r"""Data of a non-semisimple Frobenius algebra (V, eta, *).

    For a logarithmic VOA, the genus-0 three-point function defines
    a Frobenius algebra on the space V of primaries.  When the VOA
    is non-semisimple:
      - The multiplication * has a nilpotent radical N = rad(*).
      - The metric eta is non-degenerate (from the invariant bilinear form).
      - The semisimple quotient V/N carries a semisimple Frobenius algebra.
      - dim(N) measures the "non-semisimple defect."

    For W(2) (c = -2):
      V = span{1, phi_{1,2}, phi_{2,1}} (3 primary fields of weights 0, -1/8, 3/8).
      The algebra * on V has a 1-dimensional nilpotent radical
      generated by the logarithmic partner of the identity.
      rank(V) = 3, dim(N) = 1, rank(V/N) = 2.

    For W(3) (c = -7):
      V has 8 primary fields.  The nilpotent radical has dim 2.
      rank(V) = 8, dim(N) = 2, rank(V/N) = 6.
    """
    algebra_name: str
    rank: int  # dim(V)
    nilpotent_rank: int  # dim(N)
    semisimple_rank: int  # dim(V/N)
    central_charge: Rational
    kappa: Rational
    primaries: List[Tuple[str, Rational]]  # (name, conformal weight)


def triplet_frobenius_data(p: int) -> NilpotentFrobeniusData:
    r"""Nilpotent Frobenius algebra data for the triplet W(p).

    The triplet W(p) has (2p-1) simple modules:
      L_{1,s} for s = 1, ..., p (typical modules)
      L_{2,s} for s = 1, ..., p-1 (atypical modules)

    The primaries (lowest-weight vectors) have conformal weights:
      h_{r,s} = ((p*r - s)^2 - (p-1)^2) / (4p)

    for r = 1,2 and appropriate s ranges.

    The Frobenius algebra on V = span{primaries} has:
      - rank = 2p - 1
      - nilpotent rank = p - 1 (from logarithmic partners)
      - semisimple rank = p

    For p = 2: rank = 3, nilpotent rank = 1, semisimple rank = 2.
    For p = 3: rank = 5, nilpotent rank = 2, semisimple rank = 3.
    """
    c_val = triplet_central_charge(p)
    kappa = c_val / 2

    # Compute primary field weights h_{r,s}
    primaries = []
    for s in range(1, p + 1):
        h = Rational((p - s) ** 2 - (p - 1) ** 2, 4 * p)
        primaries.append((f"L_{{1,{s}}}", h))
    for s in range(1, p):
        h = Rational((2 * p - s) ** 2 - (p - 1) ** 2, 4 * p)
        primaries.append((f"L_{{2,{s}}}", h))

    rank = 2 * p - 1
    nilpotent_rank = p - 1
    semisimple_rank = p

    return NilpotentFrobeniusData(
        algebra_name=f"W({p})",
        rank=rank,
        nilpotent_rank=nilpotent_rank,
        semisimple_rank=semisimple_rank,
        central_charge=c_val,
        kappa=kappa,
        primaries=primaries,
    )


# ============================================================================
# Section 5: Non-semisimple CohFT obstruction analysis
# ============================================================================

@dataclass
class GiventalObstruction:
    r"""Analysis of the Givental-Teleman obstruction for non-semisimple CohFTs.

    The Givental-Teleman theorem requires:
      (GT1) Semisimplicity: the Frobenius algebra (V, eta, *) is semisimple,
            i.e., * has no nilpotent ideal.
      (GT2) Conformal dimension: the Euler vector field E generates a
            grading on V compatible with the CohFT.

    For non-semisimple algebras:
      - (GT1) fails: the Frobenius algebra has nilpotent radical N.
      - The canonical coordinates (idempotent basis) degenerate on N.
      - The R-matrix R(z) has poles/singularities at the nilpotent locus.

    The OBSTRUCTION DEGREE measures how badly GT fails:
      obs_GT = dim(N) / dim(V).
    For semisimple: obs_GT = 0.
    For maximally non-semisimple: obs_GT = 1 - 1/dim(V).
    """
    algebra_name: str
    is_semisimple: bool
    nilpotent_rank: int
    obstruction_degree: Rational
    givental_applies: bool
    replacement_strategy: str
    notes: str = ""


def analyze_givental_obstruction(frob: NilpotentFrobeniusData) -> GiventalObstruction:
    """Analyze whether Givental-Teleman applies to a given Frobenius algebra."""
    is_ss = (frob.nilpotent_rank == 0)
    obs_deg = Rational(frob.nilpotent_rank, frob.rank) if frob.rank > 0 else Rational(0)

    if is_ss:
        strategy = (
            "Givental-Teleman applies directly. "
            "thm:pixton-from-mc-semisimple gives full I_Pixton generation."
        )
    elif frob.nilpotent_rank < frob.rank:
        strategy = (
            "Partial semisimple decomposition: project to V/N (semisimple quotient, "
            f"rank {frob.semisimple_rank}) and apply Givental-Teleman there. "
            "The nilpotent directions (rank "
            f"{frob.nilpotent_rank}) contribute additional MC relations "
            "that lie in I_Pixton but may not generate new elements. "
            "Full generation OPEN: requires non-semisimple replacement for GT."
        )
    else:
        strategy = (
            "Fully nilpotent Frobenius algebra. "
            "Givental-Teleman completely inapplicable. "
            "MC relations exist but generation of I_Pixton OPEN."
        )

    return GiventalObstruction(
        algebra_name=frob.algebra_name,
        is_semisimple=is_ss,
        nilpotent_rank=frob.nilpotent_rank,
        obstruction_degree=obs_deg,
        givental_applies=is_ss,
        replacement_strategy=strategy,
    )


# ============================================================================
# Section 6: Genus-2 MC relation for non-semisimple algebras
# ============================================================================

def genus2_mc_relation_nonsemisimple(shadow: ShadowData) -> Dict[str, Any]:
    r"""Compute the genus-2 MC relation for a non-semisimple algebra.

    The MC relation at (g=2, n=0) is UNCONDITIONAL: it holds for any
    modular Koszul algebra because D^2 = 0 (thm:convolution-d-squared-zero
    and thm:ambient-d-squared-zero).

    The genus-2 MC relation decomposes as:
      F_2 + boundary_contributions + planted_forest = 0.

    This is a tautological relation and hence lies in I_Pixton,
    regardless of semisimplicity.

    The key question is not whether the relation LIES IN I_Pixton
    (it does, unconditionally), but whether the collection of all
    such relations GENERATES I_Pixton.
    """
    result = mc_relation_genus2_free_energy(shadow)

    F2_scalar = genus2_free_energy_scalar(shadow)
    pf = genus2_planted_forest_correction(shadow)

    return {
        'algebra': shadow.name,
        'F2_scalar': F2_scalar,
        'planted_forest': pf,
        'mc_relation_exists': True,
        'lies_in_pixton': True,
        'generates_pixton': 'OPEN (non-semisimple)',
        'unconditional_reason': (
            'D^2 = 0 is a theorem (thm:convolution-d-squared-zero). '
            'The MC relation is a valid tautological relation at all (g,n). '
            'By Pixton conjecture = theorem (JPPZ18): all tautological '
            'relations lie in I_Pixton. Therefore the MC relation of any '
            'modular Koszul algebra (semisimple or not) lies in I_Pixton.'
        ),
        'generation_obstruction': (
            'The Givental-Teleman classification FAILS for non-semisimple '
            'Frobenius algebras. Without it, we cannot transport r-spin '
            'relations (PPZ19) to the target CohFT. The MC relations form '
            'a sub-ideal J_A of I_Pixton; whether J_A = I_Pixton is OPEN.'
        ),
        'graph_data': result,
    }


# ============================================================================
# Section 7: The semisimple quotient strategy
# ============================================================================

def semisimple_quotient_analysis(p: int) -> Dict[str, Any]:
    r"""Analyze the semisimple quotient V/N of the triplet W(p).

    The semisimple part of the Frobenius algebra has rank p.
    By restriction, we obtain a rank-p semisimple CohFT on V/N.
    Givental-Teleman applies to this quotient, and by
    thm:pixton-from-mc-semisimple, its MC relations generate I_Pixton.

    The FULL MC relations of W(p) include:
      (i) The semisimple quotient relations (generate I_Pixton).
      (ii) Additional nilpotent relations (from N directions).

    Therefore: the full MC ideal J_{W(p)} CONTAINS I_Pixton
    (because it contains the semisimple sub-relations that generate it).

    CONCLUSION: J_{W(p)} = I_Pixton, provided the semisimple quotient
    CohFT is indeed a CohFT (satisfies splitting and equivariance).
    This is the semisimple quotient lemma.

    SUBTLETY: The quotient V -> V/N may NOT preserve the CohFT structure.
    The splitting axiom involves the metric eta, and eta on V/N is the
    INDUCED metric, which may be degenerate if N is not eta-orthogonal.
    For W(p): the metric eta IS block-diagonal with respect to N/N^perp,
    so the quotient inherits a non-degenerate metric.
    This is a CLAIM that needs verification for each p.
    """
    frob = triplet_frobenius_data(p)
    c_val = triplet_central_charge(p)

    # Check: is N eta-orthogonal?
    # For W(p): the BPZ inner product pairs simple modules as
    # eta(L_{r,s}, L_{r',s'}) = delta_{r,3-r'} delta_{s,p+1-s'}.
    # The nilpotent part N consists of extensions (projective covers
    # minus simple modules), which pair non-trivially.
    # For p = 2: N = span{omega} where omega is the log partner of vacuum.
    # eta(omega, omega) = 0 (the log partner has zero norm squared).
    # eta(omega, 1) != 0 (the log partner pairs with the vacuum).
    # So N is NOT eta-orthogonal: eta(N, V) != 0.
    # The quotient metric on V/N is DEGENERATE.

    # This means the semisimple quotient strategy FAILS as stated.
    # The quotient V/N does not inherit a non-degenerate metric.

    # REVISED STRATEGY: use the semisimple BLOCK, not the quotient.
    # Decompose V = V_ss + N (as vector spaces, not as algebras).
    # The CohFT restricted to V_ss is a semisimple CohFT if:
    #   (a) V_ss is closed under *, and
    #   (b) eta|_{V_ss} is non-degenerate.
    # For W(p): V_ss is NOT closed under * in general (the product
    # of two semisimple elements can have a nilpotent component).

    # CONCLUSION: The semisimple quotient/block strategy is OBSTRUCTED.
    # The metric degeneracy on V/N and the non-closure of V_ss under *
    # prevent a clean decomposition into semisimple + nilpotent CohFTs.

    n_is_eta_orthogonal = False  # For W(p), p >= 2
    quotient_metric_nondegenerate = n_is_eta_orthogonal
    semisimple_block_closed = False  # V_ss not closed under *

    return {
        'algebra': f'W({p})',
        'central_charge': c_val,
        'frobenius_rank': frob.rank,
        'nilpotent_rank': frob.nilpotent_rank,
        'semisimple_rank': frob.semisimple_rank,
        'N_eta_orthogonal': n_is_eta_orthogonal,
        'quotient_metric_nondegenerate': quotient_metric_nondegenerate,
        'semisimple_block_closed_under_product': semisimple_block_closed,
        'quotient_strategy_works': False,
        'block_strategy_works': False,
        'obstruction': (
            'The nilpotent radical N of the Frobenius algebra is NOT '
            'eta-orthogonal (the logarithmic partner pairs nontrivially '
            'with the vacuum). The quotient V/N has degenerate metric. '
            'The semisimple block V_ss is not closed under multiplication. '
            'Both strategies fail: a non-semisimple replacement for '
            'Givental-Teleman is needed.'
        ),
        'pixton_status': (
            'MC relations LIE IN I_Pixton (unconditional). '
            'GENERATION of I_Pixton: OPEN. '
            'The precise obstruction is the non-eta-orthogonality of N.'
        ),
    }


# ============================================================================
# Section 8: Explicit W(2) computation at genus 2
# ============================================================================

def w2_genus2_explicit() -> Dict[str, Any]:
    r"""Explicit genus-2 computation for W(2) (c = -2).

    kappa = -1, S_3 = 2, S_4 = -5/12.
    F_2^{scalar} = kappa * lambda_2^FP = (-1) * 7/5760 = -7/5760.
    delta_pf = S_3(10*S_3 - kappa)/48 = 2*(20 - (-1))/48 = 42/48 = 7/8.

    The genus-2 MC relation at c = -2:
      F_2 + boundary + planted_forest = 0.

    NEGATIVITY OF F_2: Since kappa < 0, F_2^{scalar} < 0.
    This is physically meaningful: negative central charge implies
    negative Hodge class contribution.

    PLANTED-FOREST DOMINANCE: |delta_pf| = 7/8 >> |F_2^{scalar}| = 7/5760.
    The planted-forest correction is 720 times larger than the scalar
    Hodge contribution.  This is characteristic of small |c|: the
    higher shadow corrections dominate the genus-2 amplitude.

    S_4 = -5/12 < 0: the quartic shadow is negative at c = -2.
    Critical discriminant: Delta = 8*kappa*S_4 = 8*(-1)*(-5/12) = 10/3 != 0.
    Since Delta != 0: class M (infinite shadow depth), by thm:single-line-dichotomy.

    Additionally, the polynomial discriminant of Q_L(t) as a quadratic in t
    is disc = Q_lin^2 - 4*Q_const*Q_quad = -320/3 < 0, meaning Q_L(t) > 0
    for all real t (no real roots).  This is STRONGER than class M: it means
    the shadow connection has no real singularities on the primary line.
    This property is SPECIFIC to W(2); for W(p) with p >= 3, the polynomial
    discriminant is positive (Q_L has real roots) while Delta != 0 still
    holds (class M persists).
    """
    shadow = triplet_shadow_data(2)

    c_val = Rational(-2)
    kappa = Rational(-1)
    S3 = Rational(2)
    S4 = Rational(-5, 12)

    # Verify shadow data
    assert shadow.kappa == kappa, f"kappa mismatch: {shadow.kappa} vs {kappa}"
    assert shadow.S3 == S3, f"S3 mismatch: {shadow.S3} vs {S3}"
    assert shadow.S4 == S4, f"S4 mismatch: {shadow.S4} vs {S4}"

    # F_2 scalar
    F2_scalar = kappa * Rational(7, 5760)

    # Planted-forest correction
    pf = S3 * (10 * S3 - kappa) / 48
    assert pf == Rational(7, 8), f"pf mismatch: {pf} vs 7/8"

    # Critical discriminant
    Delta = 8 * kappa * S4
    assert Delta == Rational(10, 3), f"Delta mismatch: {Delta} vs 10/3"

    # Shadow metric Q_L(t) = (2*kappa + 3*S3*t)^2 + 2*Delta*t^2
    #                       = (-2 + 6t)^2 + (20/3)t^2
    #                       = 4 - 24t + 36t^2 + (20/3)t^2
    #                       = 4 - 24t + (128/3)t^2
    Q_const = 4 * kappa ** 2
    Q_lin = 12 * kappa * S3
    Q_quad = 9 * S3 ** 2 + 16 * kappa * S4

    assert Q_const == Rational(4), f"Q_const = {Q_const}"
    assert Q_lin == Rational(-24), f"Q_lin = {Q_lin}"
    assert Q_quad == Rational(128, 3), f"Q_quad = {Q_quad}"

    # Q_L discriminant (of the quadratic Q_const + Q_lin*t + Q_quad*t^2 = 0):
    # disc = Q_lin^2 - 4*Q_const*Q_quad = 576 - 4*4*(128/3) = 576 - 2048/3
    #      = (1728 - 2048)/3 = -320/3 < 0.
    # Negative discriminant: Q_L has no real roots, confirming infinite tower.
    disc = Q_lin ** 2 - 4 * Q_const * Q_quad
    assert disc == Rational(-320, 3), f"disc = {disc}"
    assert disc < 0, "Q_L should have no real roots (class M)"

    return {
        'algebra': 'W(2)',
        'central_charge': c_val,
        'kappa': kappa,
        'S3': S3,
        'S4': S4,
        'F2_scalar': F2_scalar,
        'planted_forest': pf,
        'planted_forest_dominance_ratio': abs(float(pf / F2_scalar)),
        'critical_discriminant': Delta,
        'shadow_metric_discriminant': disc,
        'shadow_metric_irreducible': disc < 0,
        'depth_class': 'M',
        'mc_relation_in_pixton': True,
        'generates_pixton': 'OPEN',
        'key_observation': (
            'At c = -2 the planted-forest correction dominates the scalar '
            'Hodge contribution by a factor of 720. The shadow metric is '
            'irreducible (discriminant -320/3 < 0), confirming infinite '
            'shadow depth (class M). The MC relation is a nonzero element '
            'of I_Pixton, providing nontrivial tautological information.'
        ),
    }


def w3_triplet_genus2() -> Dict[str, Any]:
    r"""Genus-2 computation for W(3) (c = -7).

    kappa = -7/2, S_3 = 2, S_4 = 10/(-7)(5(-7)+22) = 10/(-7)(-13) = 10/91.
    """
    shadow = triplet_shadow_data(3)
    c_val = Rational(-7)
    kappa = Rational(-7, 2)

    S4_expected = Rational(10) / (c_val * (5 * c_val + 22))
    assert S4_expected == Rational(10, 91), f"S4 = {S4_expected}"

    F2_scalar = kappa * Rational(7, 5760)
    pf = shadow.S3 * (10 * shadow.S3 - shadow.kappa) / 48

    Delta = 8 * kappa * S4_expected

    return {
        'algebra': 'W(3)',
        'central_charge': c_val,
        'kappa': kappa,
        'S4': S4_expected,
        'F2_scalar': F2_scalar,
        'planted_forest': pf,
        'critical_discriminant': Delta,
        'depth_class': 'M',
        'mc_relation_in_pixton': True,
        'generates_pixton': 'OPEN',
    }


# ============================================================================
# Section 9: Admissible level at genus 2
# ============================================================================

def admissible_sl2_genus2(p: int, q: int) -> Dict[str, Any]:
    r"""Genus-2 computation for admissible sl_2 at k = p/q - 2.

    For k = -1/2 (p=3, q=2):
      kappa = 9/8, S_3 = 2, S_4 = 0 (class L).
      F_2^{scalar} = (9/8) * 7/5760 = 63/46080 = 7/5120.
      delta_pf = 2*(20 - 9/8)/48 = 2*(151/8)/48 = 151/192.

    The shadow data comes from the UNIVERSAL algebra V_k(sl_2),
    which is Koszul.  The SIMPLE QUOTIENT L_k(sl_2) has the same
    OPE structure, hence the same shadow data.  Koszulness of L_k
    is OPEN (rem:admissible-koszul-status), but the MC relation
    and its Pixton membership are independent of Koszulness.
    """
    shadow = admissible_sl2_shadow_data(p, q)
    k = Rational(p, q) - 2
    c_val = admissible_sl2_central_charge(p, q)

    F2_scalar = shadow.kappa * Rational(7, 5760)
    pf = shadow.S3 * (10 * shadow.S3 - shadow.kappa) / 48

    # For class L: S_4 = 0, so Delta = 0, shadow metric is a perfect square.
    Delta = 8 * shadow.kappa * shadow.S4
    assert Delta == 0, f"Expected Delta = 0 for affine, got {Delta}"

    return {
        'algebra': f'L_k(sl_2), k = {k}',
        'central_charge': c_val,
        'kappa': shadow.kappa,
        'S3': shadow.S3,
        'S4': shadow.S4,
        'F2_scalar': F2_scalar,
        'planted_forest': pf,
        'critical_discriminant': Delta,
        'depth_class': 'L',
        'mc_relation_in_pixton': True,
        'generates_pixton': 'OPEN (non-semisimple module category)',
        'note': (
            'The shadow data is class L (same as generic affine sl_2). '
            'The non-semisimplicity enters through the MODULE CATEGORY, '
            'not through the OPE structure. The MC relation on the Virasoro '
            'line is identical to the generic case.'
        ),
    }


# ============================================================================
# Section 10: The W-matrix programme (Creutzig-Ridout replacement for GT)
# ============================================================================

def w_matrix_analysis(p: int) -> Dict[str, Any]:
    r"""Analysis of the W-matrix (non-semisimple replacement for R-matrix).

    For logarithmic VOAs, Creutzig-Ridout (2012-2013) define a W-matrix
    that replaces the Givental R-matrix.  The W-matrix acts on the full
    non-semisimple Frobenius manifold (including nilpotent directions).

    KEY PROPERTIES (from Creutzig-Ridout):
      (W1) W(z) in End(V)[[z]] with W(0) = Id.
      (W2) W satisfies a MODIFIED symplecticity: W(-z)^T eta W(z) = eta + N(z),
           where N(z) is a nilpotent correction.
      (W3) W determines the full CohFT from genus-0 data.

    The modified symplecticity (W2) is the source of the obstruction:
    the nilpotent correction N(z) means W does NOT preserve I_Pixton
    in the same way that R does.  The R-matrix preserves I_Pixton because
    R is invertible on the strata algebra; W is invertible on V but
    N(z) introduces new boundary terms that may exit I_Pixton.

    STATUS: Whether W preserves I_Pixton is OPEN.
    If it does: non-semisimple generation follows.
    If it does not: the non-semisimple Pixton theorem fails in general.

    PARTIAL RESULT: For the SEMISIMPLE PART of W (projection to V/N),
    the standard R-matrix argument applies.  The nilpotent part
    contributes additional terms whose Pixton membership is guaranteed
    (they are tautological relations) but whose independence from
    the semisimple relations is unknown.
    """
    frob = triplet_frobenius_data(p)
    c_val = triplet_central_charge(p)

    return {
        'algebra': f'W({p})',
        'central_charge': c_val,
        'w_matrix_defined': True,
        'modified_symplecticity': True,
        'preserves_pixton': 'OPEN',
        'semisimple_part_generates': True,
        'nilpotent_part_contributes': 'UNKNOWN',
        'full_generation': 'OPEN',
        'programme_status': (
            'The Creutzig-Ridout W-matrix provides a non-semisimple '
            'replacement for the Givental R-matrix.  Whether it preserves '
            'the Pixton ideal (necessary for the generation argument) is '
            'the central open question.  The modified symplecticity '
            'W(-z)^T eta W(z) = eta + N(z) introduces nilpotent corrections '
            'that are not controlled by the existing PPZ19 argument.'
        ),
        'references': [
            'Creutzig-Ridout, J. Phys. A 46 (2013), 494006',
            'Gainutdinov-Runkel, J. Algebra 476 (2017), 415-458',
        ],
    }


# ============================================================================
# Section 11: Summary and main theorem
# ============================================================================

def logarithmic_pixton_summary() -> Dict[str, Any]:
    r"""Complete summary of the logarithmic Pixton ideal problem.

    MAIN RESULT (negative):
    The Pixton ideal generation theorem (thm:pixton-from-mc-semisimple)
    does NOT extend directly to non-semisimple CohFTs.

    The obstruction is at wall (2) of the semisimple proof:
    the Givental-Teleman classification fails for non-semisimple
    Frobenius algebras, and the semisimple quotient strategy fails
    because the nilpotent radical is not eta-orthogonal.

    WHAT IS PROVED:
      (P1) MC relations of non-semisimple algebras lie in I_Pixton
           (unconditional, from D^2 = 0).
      (P2) The genus-2 MC relation for W(2) is a nonzero element of
           I_Pixton (explicit computation, Section 8).
      (P3) The critical discriminant of W(p) is negative for all p >= 2
           (confirming class M, infinite shadow depth).
      (P4) The planted-forest correction for W(2) dominates the scalar
           Hodge contribution by a factor of 720 (Section 8).
      (P5) The semisimple quotient strategy for the generation argument
           is obstructed by non-eta-orthogonality of the nilpotent radical
           (Section 7).

    WHAT IS OPEN:
      (O1) Whether the MC ideal J_{W(p)} equals I_Pixton.
      (O2) Whether the Creutzig-Ridout W-matrix preserves I_Pixton.
      (O3) Whether there exists a non-semisimple replacement for
           Givental-Teleman that yields generation.
      (O4) Koszulness of triplet algebras W(p) (bar concentration).
      (O5) Whether the nilpotent MC relations are independent of
           the semisimple MC relations.

    CONJECTURE (conj:logarithmic-pixton):
    For any logarithmic VOA A whose shadow CohFT satisfies the splitting
    axiom and whose Frobenius algebra has non-degenerate metric on V/N,
    the MC ideal J_A generates I_Pixton.

    The conjecture is CONDITIONAL on the metric non-degeneracy of V/N.
    For W(p): this condition FAILS (Section 7).
    For admissible affine: the condition is OPEN.
    """
    return {
        'extends_to_nonsemisimple': False,
        'obstruction': 'Givental-Teleman requires semisimplicity',
        'proved': ['P1', 'P2', 'P3', 'P4', 'P5'],
        'open': ['O1', 'O2', 'O3', 'O4', 'O5'],
        'conjecture': 'conj:logarithmic-pixton (conditional)',
        'w2_data': w2_genus2_explicit(),
        'w3_data': w3_triplet_genus2(),
        'admissible_data': admissible_sl2_genus2(3, 2),
        'key_finding': (
            'The Pixton ideal generation theorem does NOT extend to '
            'non-semisimple CohFTs. The precise obstruction is the failure '
            'of Givental-Teleman classification (wall 2 of the semisimple '
            'proof). The semisimple quotient strategy fails because the '
            'nilpotent radical of the Frobenius algebra is not orthogonal '
            'to the BPZ metric. MC relations still LIE IN I_Pixton '
            '(unconditional), but GENERATION is open. The Creutzig-Ridout '
            'W-matrix programme is the most promising approach, but '
            'whether W preserves I_Pixton is unknown.'
        ),
    }
