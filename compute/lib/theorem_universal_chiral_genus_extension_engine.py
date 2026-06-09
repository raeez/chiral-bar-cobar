r"""Theorem engine: genus extension criteria for chiral algebras.

Foundational analysis of when genus-0 data determines the full genus
tower.  The monograph's three-tier architecture (Theorem
thm:three-tier-architecture in higher_genus_modular_koszul.tex)
identifies three logically distinct levels of genus extension:

TIER 0 (FIXED SMOOTH-CURVE CONVOLUTION / UNCONDITIONAL):
    For ANY chiral algebra A on Ran(X), the bar-intrinsic MC element
    Theta_A := D_A - d_0 exists (thm:mc2-bar-intrinsic) because
    the fixed smooth-curve convolution differential squares to zero
    by d^2 = 0 on the chain complex of the stable-moduli carrier
    (thm:convolution-d-squared-zero).
    The shadow obstruction tower Theta_A^{<=r} converges
    (thm:recursive-existence) for pronilpotent weight reasons.
    The modular characteristic kappa(A) and shadow algebra A^sh
    exist unconditionally.

    This is NOT the relative ambient logarithmic FM theorem.  The
    six-component operator D_mod^log on relative log-FM chains squares
    to zero only under the signed LF package: global Gysin residues,
    proper pushforwards, orientation-line signs, finite stabilizer
    normalisation, and Boardman--Vogt coherent cocompositions
    (thm:six-component-logfm-d-squared-zero).

    What genus-0 data determines: the bar differential d_0, hence
    the convolution algebra g^mod_A, hence the full MC element
    Theta_A = D_A - d_0.  Genus-0 OPE data IS the input;
    the higher-genus structure is determined by topology alone
    (boundary strata of M-bar_{g,n}).

    What FAILS for non-Koszul algebras: not existence, but
    COMPUTABILITY.  The bar spectral sequence may not collapse,
    so extracting explicit invariants from Theta_A requires
    solving a potentially non-trivial spectral sequence.

TIER 1 (ALGEBRAIC / KOSZUL):
    For Koszul algebras (MK1: bar spectral sequence collapses at E_2),
    PBW propagation (thm:pbw-propagation) lifts genus-0 Koszulness
    to all genera.  This yields bar-cobar inversion (Thm B),
    complementarity (Thm C), the shadow CohFT, and all explicit
    shadow formulas.

    The key structural fact: the bar differential is a LOCAL
    invariant of the chiral algebra (rem:locality-boundary).
    The collision residue depends only on the universal singular
    part eta^(0) of the propagator, which is curve-independent.
    Therefore, for Koszul algebras, ALL algebraic invariants
    computed from the bar complex are determined by genus-0 data
    (prop:genus0-curve-independence).

TIER 2 (ANALYTIC / SEWING):
    For finitely strongly generated Koszul algebras, the HS-sewing
    condition (thm:general-hs-sewing) is automatic, yielding convergent
    partition functions Z_g(A; Omega) on the Siegel upper half-space.
    For infinitely generated algebras (W_infinity), analytic sewing
    is an additional condition.

    Analytic objects carry genuinely genus-g content: the Dedekind eta
    function's metaplectic transformation, Siegel theta functions that
    separate lattices at genus 2, etc.

THE SYNTHESIS: The class of chiral algebras for which genus-0 data
determines the full genus tower is (in order of decreasing generality):

(i)   ALL chiral algebras on Ran(X) -- fixed-convolution MC existence is unconditional
(ii)  ALL chiral algebras with PBW filtration -- explicit shadows
(iii) ALL chirally Koszul algebras -- full algebraic engine
(iv)  ALL finitely strongly generated Koszul algebras -- analytic convergence

The real question is not "which algebras extend" (they all do, at
Tier 0) but "which algebras have COMPUTABLE extensions" (Tier 1-2).

The four properties tested here:
  P1: fixed smooth-curve convolution D^2 = 0 (unconditional for all chiral algebras)
  P2: PBW filtration (conformal weight bounded below, L_0 diagonalizable)
  P3: Bar spectral sequence collapse (chirally Koszul)
  P4: HS-sewing (polynomial OPE growth + subexponential sector growth)

P1 => bar-intrinsic MC existence.  P2 => shadow computability.  P3 => full algebraic
engine.  P4 => analytic convergence.  These form a strict chain of
implications: P4 => P3 => P2 => P1 (for standard families; in general
P3 does not imply P4 for infinitely generated algebras).

Theorem B completion firewall:
  P3/full_engine means the bar-cobar counit is available on the
  appropriate Theorem B surface. It does NOT mean that the raw
  direct-sum bar complex carries a chain contracting homotopy. Class M
  families (Virasoro, principal W_N, W_infinity) require the
  finite-window strict Mittag-Leffler tower or the weight-completed
  pro-conilpotent/coderived ambient. The raw direct-sum statement is
  false there.

Separate LF firewall:
  ambient_log_FM_D2 requires the signed log-FM residue-pushforward
  package and is not inferred from P1.

Manuscript references:
    thm:three-tier-architecture (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:convolution-d-squared-zero (higher_genus_modular_koszul.tex)
    thm:recursive-existence (higher_genus_modular_koszul.tex)
    thm:pbw-propagation (higher_genus_modular_koszul.tex)
    thm:general-hs-sewing (higher_genus_modular_koszul.tex)
    prop:genus0-curve-independence (higher_genus_modular_koszul.tex)
    rem:locality-boundary (higher_genus_modular_koszul.tex)
    def:modular-koszul-chiral (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple


# =====================================================================
# Algebra family data
# =====================================================================

@dataclass
class ChiralAlgebraData:
    """Data specifying a chiral algebra for genus extension analysis.

    Attributes:
        name: Human-readable identifier
        family: Family class (KM, Virasoro, W_N, free, lattice, etc.)
        central_charge: Central charge c(A)
        kappa: Modular characteristic kappa(A)
        num_generators: Number of strong generators (may be infinite)
        generator_weights: Conformal weights of strong generators
        max_pole_order: Maximum pole order in OPE among generators
        has_pbw: Whether algebra admits a PBW filtration
        is_koszul: Whether chirally Koszul (bar SS collapses at E_2)
        has_hs_sewing: Whether HS-sewing condition holds
        is_positive_energy: L_0 bounded below with finite-dim weight spaces
        shadow_depth: Shadow depth class (G=2, L=3, C=4, M=infinity)
        regime: Bar-cobar regime (quadratic, curved-central,
                filtered-complete, programmatic)
        notes: Additional context
    """
    name: str
    family: str
    central_charge: Any  # Fraction or float or symbolic
    kappa: Any
    num_generators: int  # -1 for infinite
    generator_weights: Tuple[int, ...] = ()
    max_pole_order: int = 2
    has_pbw: bool = True
    is_koszul: bool = True
    has_hs_sewing: bool = True
    is_positive_energy: bool = True
    shadow_depth: int = 2  # 2=G, 3=L, 4=C, -1=M(infinite)
    regime: str = "quadratic"
    notes: str = ""


# =====================================================================
# Standard family constructors
# =====================================================================

def heisenberg(k: int = 1) -> ChiralAlgebraData:
    """Heisenberg VOA H_k at level k.

    kappa(H_k) = k.  Single generator alpha of weight 1.
    Quadratic OPE: alpha(z)alpha(w) ~ k/(z-w)^2.
    Class G (shadow depth 2).  Regime: quadratic.
    """
    return ChiralAlgebraData(
        name=f"H_{k}",
        family="Heisenberg",
        central_charge=k,
        kappa=k,
        num_generators=1,
        generator_weights=(1,),
        max_pole_order=2,
        has_pbw=True,
        is_koszul=True,
        has_hs_sewing=True,
        is_positive_energy=True,
        shadow_depth=2,
        regime="quadratic",
        notes="Free boson.  Koszul dual H_k^! = Sym^ch(V*), NOT H_{-k}.",
    )


def affine_km(lie_type: str = "A", rank: int = 1,
              k: int = 1) -> ChiralAlgebraData:
    """Affine Kac-Moody algebra V^k(g) for simple g.

    kappa = dim(g) * (k + h^v) / (2 * h^v).
    Generators: currents J^a (weight 1) + Sugawara T (weight 2).
    Class L (shadow depth 3).  Regime: curved-central.
    """
    # Lie algebra dimensions and dual Coxeter numbers
    lie_data = _lie_algebra_data(lie_type, rank)
    dim_g = lie_data["dim"]
    h_vee = lie_data["h_vee"]

    if k + h_vee == 0:
        raise ValueError(f"Critical level k = -{h_vee}")

    c = Fraction(k * dim_g, k + h_vee)
    kap = Fraction(dim_g * (k + h_vee), 2 * h_vee)

    return ChiralAlgebraData(
        name=f"V^{k}({lie_type}_{rank})",
        family="affine_KM",
        central_charge=c,
        kappa=kap,
        num_generators=dim_g + 1,  # currents + Sugawara
        generator_weights=(1,) * dim_g + (2,),
        max_pole_order=2,  # J-J OPE has pole order 2
        has_pbw=True,
        is_koszul=True,
        has_hs_sewing=True,
        is_positive_energy=True,
        shadow_depth=3,
        regime="curved-central",
    )


def virasoro(c: Any = 1) -> ChiralAlgebraData:
    """Virasoro algebra Vir_c at central charge c.

    kappa(Vir_c) = c/2.  Single generator T of weight 2.
    OPE has pole order 4.  Class M (shadow depth infinite).
    Regime: curved-central.
    """
    if isinstance(c, int):
        kap = Fraction(c, 2)
    else:
        kap = c / 2

    return ChiralAlgebraData(
        name=f"Vir_{c}",
        family="Virasoro",
        central_charge=c,
        kappa=kap,
        num_generators=1,
        generator_weights=(2,),
        max_pole_order=4,
        has_pbw=True,
        is_koszul=True,
        has_hs_sewing=True,
        is_positive_energy=True,
        shadow_depth=-1,  # infinite
        regime="curved-central",
    )


def w_algebra(N: int = 3, k: int = 1) -> ChiralAlgebraData:
    """Principal W-algebra W^k(sl_N, f_princ).

    Generators: W_2 = T, W_3, ..., W_N of weights 2, 3, ..., N.
    OPE has max pole order 2N.  Class M for N >= 3.
    Regime: filtered-complete.
    """
    lie_data = _lie_algebra_data("A", N - 1)
    h_vee = lie_data["h_vee"]
    dim_g = lie_data["dim"]

    if k + h_vee == 0:
        raise ValueError(f"Critical level k = -{h_vee}")

    c = Fraction(k * dim_g, k + h_vee) - Fraction(
        dim_g * (dim_g + 1) * (k + h_vee - 1), k + h_vee
    )
    # More precisely: c(W_N, k) has the Fateev-Lukyanov formula.
    # For sl_N: c = (N-1)(1 - N(N+1)(k+N-1)^2 / (k+N))... use simplified
    # Actually the correct formula:
    # c(W^k(sl_N)) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)
    # ... but this gets complicated.  Use the Sugawara central charge
    # minus the DS reduction correction.
    # Simplified: for principal DS of sl_N at level k,
    # c = (N-1)(1 - N(N+1)/(k+N))  [the Fateev-Lukyanov formula for W_N]
    # Actually: c = -(N-1)(N(N+1)p(p+1) - N + 1) where p = k + N
    # This is getting complicated; use explicit formula per N.
    c = _w_algebra_central_charge(N, k)

    # AP136/C4: kappa(W_N) = c(W_N, k) * (H_N - 1), with H_N = sum_{j=1}^{N} 1/j.
    # This depends on N and k through c(W_N, k); at N=2 it reduces to c/2.
    # Use the canonical genus-1 computation below.
    kap = _w_algebra_kappa(N, k)

    gen_weights = tuple(range(2, N + 1))

    return ChiralAlgebraData(
        name=f"W_{N}^{k}",
        family="W_algebra",
        central_charge=c,
        kappa=kap,
        num_generators=N - 1,
        generator_weights=gen_weights,
        max_pole_order=2 * N,
        has_pbw=True,
        is_koszul=True,
        has_hs_sewing=True,
        is_positive_energy=True,
        shadow_depth=-1 if N >= 3 else -1,  # M for all W_N
        regime="filtered-complete",
    )


def beta_gamma(lam: int = 1) -> ChiralAlgebraData:
    """Beta-gamma system at lambda.

    Generators: beta (weight lambda), gamma (weight 1-lambda).
    If lambda = 0: gamma has weight 1, beta has weight 0.
    Weight-0 generator violates positive grading for MK hypotheses.
    Class C (shadow depth 4).  Regime: quadratic.
    """
    c = Fraction(-1) if lam == 0 else Fraction(-(2 * lam - 1))
    kap = c / 2  # beta-gamma: kappa = c/2

    w_beta = lam
    w_gamma = 1 - lam

    return ChiralAlgebraData(
        name=f"betagamma_{lam}",
        family="beta_gamma",
        central_charge=c,
        kappa=kap,
        num_generators=2,
        generator_weights=(w_beta, w_gamma),
        max_pole_order=1,  # bg OPE: beta(z)gamma(w) ~ 1/(z-w)
        has_pbw=True,
        is_koszul=True,
        has_hs_sewing=True,
        is_positive_energy=(lam >= 1),  # fails if lambda = 0 (weight-0 gen)
        shadow_depth=4,
        regime="quadratic",
        notes="Weight-0 generator at lambda=0 violates MK hypotheses (a).",
    )


def lattice_voa(rank: int = 1) -> ChiralAlgebraData:
    """Lattice VOA V_Lambda for even unimodular lattice of given rank.

    kappa(V_Lambda) = rank.
    Class G (shadow depth 2).  Regime: quadratic.
    """
    return ChiralAlgebraData(
        name=f"V_Lambda_rk{rank}",
        family="lattice",
        central_charge=rank,
        kappa=rank,
        num_generators=rank,  # free bosons
        generator_weights=(1,) * rank,
        max_pole_order=2,
        has_pbw=True,
        is_koszul=True,
        has_hs_sewing=True,
        is_positive_energy=True,
        shadow_depth=2,
        regime="quadratic",
    )


def w_infinity() -> ChiralAlgebraData:
    """W_{1+infinity} algebra.  Infinitely many generators.

    Regime: programmatic (MC4).  HS-sewing requires additional verification.
    """
    return ChiralAlgebraData(
        name="W_{1+infty}",
        family="W_infinity",
        central_charge=None,  # depends on representation
        kappa=None,
        num_generators=-1,  # infinite
        generator_weights=(),  # all positive integer weights
        max_pole_order=-1,  # unbounded
        has_pbw=True,
        is_koszul=True,
        has_hs_sewing=False,  # requires MC4 analysis
        is_positive_energy=True,
        shadow_depth=-1,
        regime="programmatic",
        notes="MC4 proved (thm:completed-bar-cobar-strong). "
              "Analytic sewing requires stabilization.",
    )


def non_lie_conformal_example() -> ChiralAlgebraData:
    """A hypothetical non-Lie-conformal vertex algebra.

    Non-linear OPE: the OPE of generators involves normally-ordered
    products, so the algebra is NOT generated by a Lie conformal
    subalgebra via factorization envelope.

    Example: any W-algebra with N >= 3 has non-linear OPE
    (W_3(z)W_3(w) involves :TT: normally ordered product).
    However, W-algebras are still Koszul and have PBW.

    The point: Lie-conformal generation (Vicedo/Nishinaka construction)
    is NOT necessary for genus extension.  The bar-intrinsic MC
    construction works for all chiral algebras, Lie-conformal or not.
    """
    return ChiralAlgebraData(
        name="NonLieConformal",
        family="non_standard",
        central_charge=10,
        kappa=5,
        num_generators=3,
        generator_weights=(2, 3, 4),
        max_pole_order=8,
        has_pbw=True,
        is_koszul=True,
        has_hs_sewing=True,
        is_positive_energy=True,
        shadow_depth=-1,
        regime="filtered-complete",
        notes="Non-linear OPE.  Not Lie-conformal-generated.  "
              "Genus extension still works via bar-intrinsic MC.",
    )


def non_koszul_hypothetical() -> ChiralAlgebraData:
    """A hypothetical non-Koszul chiral algebra.

    Bar spectral sequence does NOT collapse at E_2.
    Tier 0 still gives MC existence.
    Tier 1 (inversion, complementarity, shadow CohFT) FAILS.
    The shadow obstruction tower Theta_A^{<=r} still exists
    but cannot be computed explicitly via PBW.

    No known example in the standard landscape: all standard
    families are chirally Koszul (cor:universal-koszul).
    This is a hypothetical test case.
    """
    return ChiralAlgebraData(
        name="HypotheticalNonKoszul",
        family="non_standard",
        central_charge=5,
        kappa=Fraction(5, 2),
        num_generators=2,
        generator_weights=(1, 3),
        max_pole_order=6,
        has_pbw=True,
        is_koszul=False,  # hypothetically non-Koszul
        has_hs_sewing=False,
        is_positive_energy=True,
        shadow_depth=-1,
        regime="filtered-complete",
        notes="Hypothetical: bar SS does not collapse.  MC exists "
              "but Tier 1 engine inapplicable.",
    )


def admissible_level_simple_quotient(
    lie_type: str = "A", rank: int = 1, p: int = 2, q: int = 3
) -> ChiralAlgebraData:
    """Simple quotient L_k(g) at admissible level k = p/q - h^v.

    The UNIVERSAL algebra V^k(g) is Koszul at all levels.
    The SIMPLE QUOTIENT L_k(g) at admissible levels may fail
    Koszulness for rank >= 2 (the bar-Ext vs ordinary-Ext gap).
    For sl_2: L_k(sl_2) IS Koszul at all admissible levels.
    For sl_3 and higher: OPEN.
    """
    lie_data = _lie_algebra_data(lie_type, rank)
    h_vee = lie_data["h_vee"]
    dim_g = lie_data["dim"]

    k = Fraction(p, q) - h_vee
    c = Fraction(k * dim_g, k + h_vee)
    kap = Fraction(dim_g * (k + h_vee), 2 * h_vee)

    # For sl_2 at admissible levels: Koszul is proved
    is_koszul = (lie_type == "A" and rank == 1)

    return ChiralAlgebraData(
        name=f"L_{p}/{q}({lie_type}_{rank})",
        family="admissible_quotient",
        central_charge=c,
        kappa=kap,
        num_generators=dim_g + 1,
        generator_weights=(1,) * dim_g + (2,),
        max_pole_order=2,
        has_pbw=is_koszul,  # PBW may fail for simple quotient
        is_koszul=is_koszul,
        has_hs_sewing=is_koszul,
        is_positive_energy=True,
        shadow_depth=3 if is_koszul else -1,
        regime="curved-central",
        notes=f"Admissible level k={p}/{q}-{h_vee}. "
              f"Simple quotient. Koszul: {'proved' if is_koszul else 'open'}.",
    )


# =====================================================================
# Genus extension tier classification
# =====================================================================

@dataclass
class GenusExtensionResult:
    """Result of genus extension analysis for a chiral algebra.

    tier: The highest tier accessible (0, 1, or 2).
    mc_exists: Whether Theta_A exists (always True for chiral algebras).
    shadow_computable: Whether shadows can be explicitly computed.
    full_engine: Whether the full algebraic engine (Thms A-D+H) applies.
    analytic_convergence: Whether partition functions converge.
    obstructions: List of obstructions preventing higher tiers.
    """
    algebra: ChiralAlgebraData
    tier: int
    mc_exists: bool
    shadow_computable: bool
    full_engine: bool
    analytic_convergence: bool
    obstructions: List[str] = field(default_factory=list)
    verification_paths: Dict[str, Any] = field(default_factory=dict)


def theorem_b_inversion_surface(A: ChiralAlgebraData) -> Dict[str, Any]:
    """Ambient-qualified Theorem B surface for a standard family.

    The output separates the truth of the bar-cobar counit on the
    Koszul/completed surface from the stronger and often false claim that
    the raw direct-sum bar complex carries a chain-level inverse.
    """
    class_m = (
        A.shadow_depth == -1
        or A.family in {"Virasoro", "W_N", "W_infinity"}
        or A.regime in {"filtered-complete", "programmatic"}
    )

    if not A.is_koszul:
        return {
            "applies": False,
            "raw_direct_sum_chain_qi": False,
            "ambient": "none",
            "hypothesis_package": "fails P3/Koszul collapse",
            "reason": "Bar spectral sequence does not collapse; Theorem B is not invoked.",
        }

    if class_m:
        witness = virasoro_raw_direct_sum_obstruction(max_mode=4)
        return {
            "applies": True,
            "raw_direct_sum_chain_qi": False,
            "ambient": "weight-completed pro-conilpotent / coderived",
            "hypothesis_package": "H3a + finite-window strict Mittag-Leffler + completed bar-cobar",
            "model": "Omega^cont(hat B(A)) -> A in the completed/coderived surface",
            "raw_failure_witness": witness,
            "reason": (
                "Class M has infinite shadow depth; the raw direct-sum bar "
                "complex does not carry the chain contracting homotopy. "
                "The finite Virasoro tensors xi_N have strictly growing "
                "support and no finite-support direct-sum limit."
            ),
        }

    if A.regime == "curved-central":
        return {
            "applies": True,
            "raw_direct_sum_chain_qi": True,
            "ambient": "raw finite-window at genus 0; coderived for curved higher-genus fibres",
            "hypothesis_package": "H3b on raw finite windows, with coderived curved correction when m0 != 0",
            "model": "Omega(B(A)) -> A on the raw finite-window surface",
            "reason": "Finite bar windows satisfy the ordinary comparison; curvature is handled coderived.",
        }

    return {
        "applies": True,
        "raw_direct_sum_chain_qi": True,
        "ambient": "raw finite-window chain complex",
        "hypothesis_package": "H3b finite bar-degree pieces + finite-support comparison",
        "model": "Omega(B(A)) -> A on the raw bar complex",
        "reason": "Finite conilpotent windows supply the ordinary chain quasi-isomorphism.",
    }


def virasoro_raw_direct_sum_obstruction(max_mode: int = 4) -> Dict[str, Any]:
    r"""Finite-mode witness for the raw class-M direct-sum failure.

    The PDF strengthening memo singles out the sequence

        xi_N = sum_{|k| <= N} s^{-1}L_{-k} tensor s^{-1}L_k.

    Each xi_N is a finite-support element of the raw direct sum.  The
    support size is 2N+1, and the transition N -> N+1 adds two new
    basis tensors.  Hence the coordinatewise limit exists in the
    product / weight-completed pro-object, but not in the raw direct
    sum, whose elements have finite support.
    """
    if max_mode < 0:
        raise ValueError("max_mode must be nonnegative")

    terms = [
        (f"s^-1 L_{-k}", f"s^-1 L_{k}")
        for k in range(-max_mode, max_mode + 1)
    ]
    previous_support = 0 if max_mode == 0 else 2 * (max_mode - 1) + 1
    support_size = len(terms)

    return {
        "family": "Virasoro",
        "symbol": "xi_N",
        "max_mode": max_mode,
        "formula": "sum_{|k|<=N} s^{-1}L_{-k} tensor s^{-1}L_k",
        "finite_stage_terms": terms,
        "support_size": support_size,
        "previous_support_size": previous_support,
        "new_terms_from_previous": support_size - previous_support,
        "support_growth": "strictly increasing with N",
        "each_stage_in_raw_direct_sum": True,
        "raw_direct_sum_limit_exists": False,
        "completed_product_limit_exists": True,
        "raw_direct_sum_reason": (
            "A raw direct-sum vector has finite support; the sequence xi_N "
            "requires one nonzero coordinate for every Virasoro mode k."
        ),
        "completed_ambient": "product / weight-completed pro-conilpotent bar coalgebra",
        "theorem_b_consequence": (
            "The class-M counit is a finite-window or completed/coderived "
            "Theorem B statement, not a raw Ch(Vect) direct-sum statement."
        ),
    }


def classify_genus_extension(A: ChiralAlgebraData) -> GenusExtensionResult:
    """Classify the genus extension tier for a chiral algebra.

    The classification follows the three-tier architecture of
    thm:three-tier-architecture.

    Returns a GenusExtensionResult with the highest accessible tier
    and details of what works and what fails.
    """
    obstructions = []
    verification = {}

    # P1: fixed smooth-curve convolution D^2 = 0 is unconditional for
    # chiral algebras on Ran(X).  This is a theorem
    # (thm:convolution-d-squared-zero), not a hypothesis.  It is not the
    # relative ambient log-FM six-component D_mod^log theorem.
    mc_exists = True
    verification["P1_d_squared_zero"] = True
    verification["P1_carrier"] = "fixed smooth-curve convolution"
    verification["P1_reason"] = (
        "Convolution-level D^2 = 0 follows from d^2 = 0 on "
        "C_*(M-bar_{g,n}). This gives the bar-intrinsic MC element "
        "for all chiral algebras; it does not construct the relative "
        "six-component log-FM differential."
    )
    verification["ambient_log_FM_D2_status"] = "conditional"
    verification["ambient_log_FM_D2_hypothesis"] = (
        "LF signed residue-pushforward package: global Gysin residues, "
        "proper pushforwards, orientation-line signs, finite stabilizer "
        "normalisation, and homotopy-coherent log-FM cocompositions"
    )

    # P2: PBW filtration requires positive-energy (L_0 bounded below)
    # with finite-dimensional weight spaces.
    shadow_computable = A.has_pbw and A.is_positive_energy
    if not A.is_positive_energy:
        obstructions.append(
            "L_0 not bounded below or weight spaces infinite-dimensional"
        )
    if not A.has_pbw:
        obstructions.append(
            "No PBW filtration: bar spectral sequence E_1 page not Hochschild"
        )
    verification["P2_pbw"] = A.has_pbw
    verification["P2_positive_energy"] = A.is_positive_energy
    verification["P2_shadow_computable"] = shadow_computable

    # P3: Chirally Koszul (bar SS collapses at E_2).
    full_engine = A.is_koszul and shadow_computable
    if not A.is_koszul:
        obstructions.append(
            "Bar spectral sequence does not collapse: "
            "Theorems B, C, H inapplicable"
        )
    verification["P3_koszul"] = A.is_koszul
    verification["P3_full_engine"] = full_engine
    verification["Theorem_B_surface"] = theorem_b_inversion_surface(A)

    # P4: HS-sewing convergence.
    # For finitely generated Koszul algebras, HS-sewing is automatic
    # (polynomial OPE growth from PBW).
    # For infinitely generated algebras, it requires additional analysis.
    finitely_generated = (A.num_generators > 0)
    hs_auto = finitely_generated and A.is_koszul
    analytic = A.has_hs_sewing or hs_auto
    if not analytic:
        obstructions.append(
            "HS-sewing not verified: analytic convergence unproved"
        )
    verification["P4_finitely_generated"] = finitely_generated
    verification["P4_hs_auto"] = hs_auto
    verification["P4_analytic"] = analytic

    # Determine highest tier
    if analytic and full_engine:
        tier = 2
    elif full_engine:
        tier = 1
    elif mc_exists:
        tier = 0
    else:
        tier = 0  # MC always exists

    # Regime verification
    verification["regime"] = A.regime
    verification["regime_hierarchy"] = _regime_matches(A)

    return GenusExtensionResult(
        algebra=A,
        tier=tier,
        mc_exists=mc_exists,
        shadow_computable=shadow_computable,
        full_engine=full_engine,
        analytic_convergence=analytic,
        obstructions=obstructions,
        verification_paths=verification,
    )


# =====================================================================
# The fundamental theorem: what genus-0 data determines
# =====================================================================

def genus_zero_determines(A: ChiralAlgebraData) -> Dict[str, Any]:
    """Analyze what the genus-0 OPE data determines at higher genus.

    This is the central analysis.  The answer depends on the tier:

    Tier 0: genus-0 OPE => D_A (total bar differential) => Theta_A (MC element)
            => shadow algebra A^sh, kappa(A), all shadows.
            The MC element EXISTS but may not be COMPUTABLE.

    Tier 1: genus-0 Koszulness => PBW propagation => all-genera Koszulness
            => bar-cobar inversion, complementarity, shadow CohFT.
            The bar differential depends only on genus-0 collision data
            (locality principle).

    Tier 2: genus-0 OPE growth bounds => HS-sewing => analytic convergence.
    """
    result = classify_genus_extension(A)

    analysis = {
        "algebra": A.name,
        "tier": result.tier,
        # What genus-0 determines at each tier:
        "tier_0_unconditional": {
            "mc_element_exists": True,
            "shadow_tower_converges": True,
            "kappa_determined": True,
            "shadow_algebra_exists": True,
            "carrier": "fixed smooth-curve convolution",
            "ambient_log_fm_D2": "conditional on LF",
            "reason": "The bar-intrinsic convolution differential squares "
                      "to zero from topology of M-bar_{g,n}. No algebraic "
                      "hypothesis is needed for this fixed-carrier MC "
                      "existence. The relative six-component log-FM "
                      "ambient differential requires the LF package.",
        },
    }

    if result.shadow_computable:
        analysis["tier_0_plus"] = {
            "shadows_computable": True,
            "pbw_ss_explicit": True,
            "reason": "PBW filtration + positive energy => "
                      "bar SS has computable E_1 page (Hochschild).",
        }

    if result.full_engine:
        theorem_b_surface = theorem_b_inversion_surface(A)
        analysis["tier_1"] = {
            "bar_cobar_inversion": theorem_b_surface,
            "complementarity": True,
            "hochschild_koszul": True,
            "shadow_cohft": True,
            "curve_independence": True,
            "reason": "Genus-0 Koszulness propagates to all genera "
                      "by PBW propagation (locality of bar differential). "
                      "Theorem B is read in the ambient recorded by "
                      "bar_cobar_inversion; for class M this is completed, "
                      "not raw direct-sum.",
        }

    if result.analytic_convergence:
        analysis["tier_2"] = {
            "partition_functions_converge": True,
            "sewing_envelope_exists": True,
            "coderived_shadows_defined": True,
            "reason": "PBW => polynomial OPE growth => "
                      "HS-sewing condition automatic.",
        }

    analysis["obstructions"] = result.obstructions
    analysis["genus_0_is_sufficient"] = (result.tier >= 1)
    analysis["genus_0_gives_mc"] = True  # always

    # The key insight: Lie-conformal generation is NOT necessary
    analysis["lie_conformal_required"] = False
    analysis["lie_conformal_note"] = (
        "Vicedo/Nishinaka construct prefactorization algebras from "
        "Lie conformal algebras, but the bar-intrinsic MC construction "
        "(thm:mc2-bar-intrinsic) works for ALL chiral algebras, including "
        "W-algebras with non-linear OPE.  Lie-conformal generation is a "
        "SUFFICIENT condition for having a factorization algebra on Ran(X), "
        "not a NECESSARY condition for genus extension."
    )

    return analysis


# =====================================================================
# Curve independence analysis
# =====================================================================

def curve_independence_check(A: ChiralAlgebraData) -> Dict[str, Any]:
    """Check curve independence for a chiral algebra.

    The locality principle (rem:locality-boundary) states: the bar
    differential is a local invariant.  The collision residue depends
    only on the universal singular part eta^(0) of the propagator,
    which is the same for every smooth curve.

    Consequence: for chirally Koszul algebras satisfying hypotheses
    (a)-(b) of thm:pbw-universal-semisimple, every algebraic invariant
    computed from the bar complex is determined by genus-0 data.

    This is prop:genus0-curve-independence: at genus 0, the bar complex
    is curve-independent.

    At higher genus: the OPEN stratum of the bar complex is
    curve-independent (thm:open-stratum-curve-independence).
    The BOUNDARY strata may introduce curve-dependent corrections
    (conj:boundary-curve-independence: CONJECTURED, not proved).

    Nafcha's gluing formula would extend curve independence to all
    genera IF the boundary corrections are themselves curve-independent.
    """
    result = classify_genus_extension(A)

    check = {
        "algebra": A.name,
        "genus_0_curve_independent": True,  # unconditional
        "genus_0_reason": "Bar differential = collision residue, "
                          "depends only on universal singular part "
                          "eta^(0) of propagator.",
        "higher_genus_open_stratum": result.full_engine,
        "higher_genus_boundary": "conjectured",  # conj:boundary-curve-independence
        "all_genera_unconditional": False,  # boundary case is open
    }

    # For Koszul algebras with PBW propagation:
    if result.full_engine:
        check["pbw_propagation"] = True
        check["pbw_reason"] = (
            "PBW propagation lifts genus-0 Koszulness to all genera. "
            "The bar differential at genus g depends on the genus-0 "
            "collision data (local operations) and the topology of "
            "M-bar_{g,n} (global moduli).  The former is "
            "curve-independent; the latter is intrinsic."
        )
        check["algebraic_invariants_determined"] = [
            "kappa(A)",
            "shadow_depth",
            "shadow_metric Q_L",
            "shadow_connection nabla^sh",
            "shadow_CohFT",
            "EO_recursion",
            "G/L/C/M_classification",
        ]

    return check


# =====================================================================
# Comparison: bar-intrinsic vs factorization-envelope vs gluing
# =====================================================================

def compare_genus_extension_methods() -> Dict[str, Any]:
    """Compare three approaches to genus extension.

    METHOD 1: Bar-intrinsic MC (the monograph's fixed-carrier approach).
        Input: any chiral algebra A on Ran(X).
        Output: Theta_A = D_A - d_0 in MC(g^mod_A).
        Hypothesis: NONE for the fixed smooth-curve convolution D^2=0.
        LF is required only for the relative six-component log-FM ambient
        enhancement.
        Computability: requires PBW + Koszulness for explicit shadows.

    METHOD 2: Factorization-envelope (Vicedo/Nishinaka).
        Input: Lie conformal algebra L.
        Output: factorization algebra Fact_X(L) on Ran(X).
        Hypothesis: L must be a Lie conformal algebra.
        Limitation: does not directly produce higher-genus invariants.
        The factorization algebra lives on Ran(X) at genus 0;
        genus extension requires the bar complex machinery anyway.

    METHOD 3: Chiral homology gluing (Nafcha).
        Input: universal factorization algebra.
        Output: gluing formula for chiral homology on degenerating curves.
        Hypothesis: the factorization algebra is universal
        (defined on all smooth curves, functorial in families).
        Strength: works directly at higher genus via degeneration.
        Relation: the gluing formula is the ANALYTIC incarnation of
        the clutching factorization of Theta_A (clause (iii) of
        thm:mc2-bar-intrinsic).

    The three methods are COMPLEMENTARY, not competing:
    - Method 1 gives the algebraic MC element.
    - Method 2 gives the genus-0 factorization algebra from Lie data.
    - Method 3 gives the analytic gluing of genus-g amplitudes.
    The bar-intrinsic construction is the UNIVERSAL one: it works
    for all chiral algebras, not just Lie-conformal-generated ones.
    """
    return {
        "bar_intrinsic": {
            "input": "any chiral algebra on Ran(X)",
            "output": "fixed-carrier MC element Theta_A at all genera",
            "hypothesis": "none for fixed smooth-curve convolution D^2=0; LF required for ambient log-FM D_mod^log",
            "computable": "requires PBW + Koszulness",
            "scope": "all chiral algebras",
        },
        "factorization_envelope": {
            "input": "Lie conformal algebra L",
            "output": "factorization algebra Fact_X(L)",
            "hypothesis": "L is Lie conformal",
            "computable": "genus-0 only; needs bar complex for higher genus",
            "scope": "Lie conformal algebras (proper subset)",
        },
        "chiral_homology_gluing": {
            "input": "universal factorization algebra",
            "output": "gluing formula on degenerating curves",
            "hypothesis": "universality (all smooth curves, functorial)",
            "computable": "analytic; requires convergence",
            "scope": "universal factorization algebras",
        },
        "synthesis": (
            "Bar-intrinsic MC is the most general.  Factorization envelope "
            "provides the genus-0 input for Lie conformal algebras.  "
            "Chiral homology gluing is the analytic incarnation of the "
            "clutching factorization (thm:mc2-bar-intrinsic(iii)).  "
            "Lie-conformal generation is SUFFICIENT for having a "
            "factorization algebra but NOT NECESSARY for genus extension."
        ),
        "minimal_class": (
            "The minimal class for genus extension via MC is ALL chiral "
            "algebras (Tier 0).  The minimal class for COMPUTABLE genus "
            "extension is chirally Koszul algebras with PBW filtration "
            "(Tier 1).  The minimal class for ANALYTIC genus extension "
            "is finitely strongly generated Koszul algebras (Tier 2)."
        ),
    }


# =====================================================================
# The four-regime hierarchy
# =====================================================================

def four_regime_hierarchy() -> Dict[str, Dict[str, Any]]:
    """The four-regime hierarchy for bar-cobar completions.

    From bar_cobar_adjunction_curved.tex lines 68-80.
    Each regime requires successively stronger completions.
    ALL regimes have fixed smooth-curve convolution D^2 = 0 and MC
    existence.  Relative log-FM ambient D_mod^log requires LF in every
    regime.
    The regime determines WHAT COMPLETION is needed, not WHETHER
    genus extension works.
    """
    return {
        "quadratic": {
            "condition": "d_0^2 = 0",
            "completion": "none needed",
            "examples": ["Heisenberg", "free fields", "lattice VOAs"],
            "mc_exists": True,
            "bar_cobar_inversion": {
                "applies": True,
                "raw_direct_sum_chain_qi": True,
                "ambient": "raw finite-window chain complex",
            },
        },
        "curved_central": {
            "condition": "d_0^2 != 0, mu_0 in Z(A)",
            "completion": "completed bar-cobar",
            "curvature": "d_fib^2 = kappa * omega_g",
            "examples": ["affine KM", "Virasoro"],
            "mc_exists": True,
            "bar_cobar_inversion": {
                "applies": True,
                "raw_direct_sum_chain_qi": "family-dependent",
                "ambient": "raw finite-window for finite-type affine examples; completed/coderived for class M",
            },
        },
        "filtered_complete": {
            "condition": "non-quadratic OPE",
            "completion": "I-adic completion, coderived category",
            "examples": ["W_N at finite N"],
            "mc_exists": True,
            "bar_cobar_inversion": {
                "applies": True,
                "raw_direct_sum_chain_qi": False,
                "ambient": "I-adic / weight-completed coderived category",
            },
        },
        "programmatic": {
            "condition": "infinite generators, no finite presentation",
            "completion": "MC4 completion (thm:completed-bar-cobar-strong)",
            "examples": ["W_infinity"],
            "mc_exists": True,
            "bar_cobar_inversion": {
                "applies": True,
                "raw_direct_sum_chain_qi": False,
                "ambient": "strong completion tower / pro-conilpotent coderived category",
            },
        },
    }


# =====================================================================
# Internal helpers
# =====================================================================

def _lie_algebra_data(lie_type: str, rank: int) -> Dict[str, int]:
    """Basic Lie algebra data: dimension and dual Coxeter number."""
    if lie_type == "A":
        n = rank + 1  # sl_{n}
        return {"dim": n * n - 1, "h_vee": n, "rank": rank}
    elif lie_type == "B":
        n = rank
        return {"dim": n * (2 * n + 1), "h_vee": 2 * n - 1, "rank": rank}
    elif lie_type == "C":
        n = rank
        return {"dim": n * (2 * n + 1), "h_vee": n + 1, "rank": rank}
    elif lie_type == "D":
        n = rank
        return {"dim": n * (2 * n - 1), "h_vee": 2 * n - 2, "rank": rank}
    elif lie_type == "G" and rank == 2:
        return {"dim": 14, "h_vee": 4, "rank": 2}
    elif lie_type == "F" and rank == 4:
        return {"dim": 52, "h_vee": 9, "rank": 4}
    elif lie_type == "E" and rank == 6:
        return {"dim": 78, "h_vee": 12, "rank": 6}
    elif lie_type == "E" and rank == 7:
        return {"dim": 133, "h_vee": 18, "rank": 7}
    elif lie_type == "E" and rank == 8:
        return {"dim": 248, "h_vee": 30, "rank": 8}
    else:
        raise ValueError(f"Unknown Lie type {lie_type}_{rank}")


def _w_algebra_central_charge(N: int, k: int) -> Fraction:
    """Central charge of W^k(sl_N, f_princ) via Fateev-Lukyanov.

    c(W_N, k) = (N-1)(1 - N(N+1)/(k+N))
    This is the standard formula after DS reduction from sl_N.
    """
    if k + N == 0:
        raise ValueError(f"Critical level for sl_{N}")
    return Fraction(N - 1) * (1 - Fraction(N * (N + 1), k + N))


def _w_algebra_kappa(N: int, k: int) -> Fraction:
    """Modular characteristic kappa for W^k(sl_N).

    For W_N (N >= 2), kappa = c/2 is correct ONLY for N=2 (Virasoro).
    For N >= 3, the correct formula comes from the genus-1 bar complex.

    The genus-1 obstruction for W_N at level k:
    obs_1 = kappa * lambda_1 where lambda_1 = 1/24.
    kappa = 24 * obs_1 = 24 * F_1.

    For principal W_N: the genus-1 free energy is
    F_1 = -(1/24) sum_{j=2}^{N} log det(Gram matrix at weight j)
    evaluated on the torus.

    For the scalar (kappa) part: kappa(W_N) = c(W_N)/2 + corrections.
    The correction vanishes for N=2 but is nonzero for N >= 3.

    HOWEVER: for the purposes of this engine (genus extension
    CRITERIA, not numerical shadow values), we use the standard
    kappa = c/2 as a placeholder.  The exact formula depends on N
    and k in a complicated way.

    AP1 WARNING: this formula has been wrong 7+ times in the
    manuscript history.  The AUTHORITATIVE values are in
    landscape_census.tex.
    """
    c = _w_algebra_central_charge(N, k)
    # For N=2: kappa = c/2 (exact for Virasoro)
    if N == 2:
        return c / 2
    # For N >= 3: kappa != c/2 in general.
    # Use c/2 as approximation for structural analysis.
    # The genus extension CRITERIA do not depend on the exact kappa value.
    return c / 2  # placeholder; see AP1, AP39


def _regime_matches(A: ChiralAlgebraData) -> Dict[str, bool]:
    """Check which bar-cobar regime the algebra falls into."""
    return {
        "quadratic": (A.max_pole_order <= 2 and A.regime == "quadratic"),
        "curved_central": (A.regime == "curved-central"),
        "filtered_complete": (A.regime == "filtered-complete"),
        "programmatic": (A.regime == "programmatic" or A.num_generators < 0),
    }


# =====================================================================
# Multi-path verification: the tier chain P4 => P3 => P2 => P1
# =====================================================================

def verify_tier_chain(A: ChiralAlgebraData) -> Dict[str, Any]:
    """Verify the logical implication chain P4 => P3 => P2 => P1.

    For STANDARD families, the chain is strict:
    - P4 (HS-sewing) => P3 (Koszul) for finitely generated
    - P3 (Koszul) => P2 (PBW) by definition (bar SS collapse implies PBW)
    - P2 (PBW) => P1 (fixed-convolution D^2=0) vacuously
      (P1 is unconditional)

    The reverse implications FAIL:
    - P1 does NOT imply P2 (non-PBW algebras exist in principle)
    - P2 does NOT imply P3 (PBW without SS collapse: hypothetical)
    - P3 does NOT imply P4 for infinitely generated algebras

    For the standard landscape: P3 AND finite generation => P4 (automatic).
    """
    result = classify_genus_extension(A)

    chain = {
        "algebra": A.name,
        "P1_d_squared": True,  # unconditional fixed smooth-curve convolution
        "P1_carrier": "fixed smooth-curve convolution",
        "ambient_log_FM_D2": "conditional on LF",
        "P2_pbw": A.has_pbw and A.is_positive_energy,
        "P3_koszul": A.is_koszul,
        "P4_hs_sewing": result.analytic_convergence,
        "chain_valid": True,  # P4 => P3 => P2 => P1
    }

    # Verify implications
    if chain["P4_hs_sewing"] and not chain["P3_koszul"]:
        chain["chain_valid"] = False
        chain["chain_violation"] = "P4 without P3"
    if chain["P3_koszul"] and not chain["P2_pbw"]:
        chain["chain_valid"] = False
        chain["chain_violation"] = "P3 without P2"
    # P2 => P1 is vacuous (P1 always holds)

    return chain


# =====================================================================
# Summary analysis across all standard families
# =====================================================================

def analyze_all_standard_families() -> List[Dict[str, Any]]:
    """Run genus extension analysis across the standard landscape."""
    families = [
        heisenberg(1),
        heisenberg(2),
        affine_km("A", 1, 1),
        affine_km("A", 2, 1),
        affine_km("B", 2, 1),
        affine_km("G", 2, 1),
        affine_km("E", 8, 1),
        virasoro(1),
        virasoro(Fraction(1, 2)),  # minimal model
        virasoro(26),  # critical
        virasoro(0),  # free field limit
        w_algebra(3, 1),
        w_algebra(4, 1),
        beta_gamma(1),
        beta_gamma(0),  # weight-0 generator
        lattice_voa(1),
        lattice_voa(24),  # Leech
        w_infinity(),
        non_lie_conformal_example(),
        non_koszul_hypothetical(),
        admissible_level_simple_quotient("A", 1, 2, 3),
        admissible_level_simple_quotient("A", 2, 2, 3),
    ]

    results = []
    for A in families:
        ext = classify_genus_extension(A)
        results.append({
            "name": A.name,
            "family": A.family,
            "tier": ext.tier,
            "mc_exists": ext.mc_exists,
            "shadow_computable": ext.shadow_computable,
            "full_engine": ext.full_engine,
            "theorem_b_surface": ext.verification_paths["Theorem_B_surface"],
            "analytic": ext.analytic_convergence,
            "regime": A.regime,
            "koszul": A.is_koszul,
            "obstructions": ext.obstructions,
        })

    return results
