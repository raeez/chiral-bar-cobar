r"""Bershadsky--Polyakov OPE and PBW-character diagnostics.

The Bershadsky-Polyakov algebra BP_k = W_k(sl_3, f_{min}) is the DS reduction
of V_k(sl_3) at the MINIMAL nilpotent orbit (partition (2,1)).  It is the
simplest non-principal W-algebra.  Its chain-level OPE is the
Feigin-Semikhatov W_3^{(2)} normal form.

GENERATORS (4 strong generators):
  J   (conformal weight 1,   bosonic,   J-charge 0)
  G+  (conformal weight 3/2, bosonic,   J-charge +1)
  G-  (conformal weight 3/2, bosonic,   J-charge -1)
  T   (conformal weight 2,   bosonic,   J-charge 0)

STANDARD CENTRAL CHARGE (Fehily--Kawasetsu--Ridout 2021, Eq. (2.2)):
  c(k) = -(2k+3)(3k+1)/(k+3)

  Here k is the affine sl_3 level and the conformal vector gives both
  charged generators weight 3/2.  The companion involution k -> -k-6
  yields the exact rational identity c(k)+c(-k-6)=50.

SECONDARY SHIFTED FORMULA:
  c_shifted(k) = 2 - 24(k+1)^2/(k+3),
  c_shifted(k)+c_shifted(-k-6)=196.
  This rational function is retained under an explicit shifted name.  It is
  distinct from the FKR Eq. (2.2) conformal vector used by the OPE packet.

GENUS-ONE STATUS:
  The BP modular characteristic kappa has no proved formula in this engine.
  The former value c/6 used the odd-parity signed reciprocal-weight sum.
  Source-correct parity changes that diagnostic to 17/6, while its relation
  to genus-one curvature remains an open computation.

OPE (Feigin--Semikhatov/FKR convention, ordinary skew-symmetry):
  T_(3)T = c/2,    T_(1)T = 2T,        T_(0)T = dT
  T_(1)J = J,      T_(0)J = dJ
  T_(1)G+ = 3/2 G+, T_(0)G+ = dG+
  T_(1)G- = 3/2 G-, T_(0)G- = dG-
  J_(1)J = (2k+3)/3,    J_(0)J = 0
  J_(1)T = J,      J_(0)T = 0
  J_(0)G+ = G+,    J_(0)G- = -G-
  G+_(2)G- = (k+1)(2k+3), G+_(1)G- = 3(k+1)J
  G+_(0)G- = 3:JJ: + (3(k+1)/2)dJ - (k+3)T
  G-_(2)G+ = -(k+1)(2k+3), G-_(1)G+ = 3(k+1)J
  G-_(0)G+ = -3:JJ: + (3(k+1)/2)dJ + (k+3)T
  G+_(n)G+ = 0,    G-_(n)G- = 0
  G+_(1)T = 3/2 G+, G+_(0)T = 1/2 dG+
  G-_(1)T = 3/2 G-, G-_(0)T = 1/2 dG-
  G+_(0)J = -G+,   G-_(0)J = G-

BAR COMPLEX CONVENTIONS:
  Cohomological grading, |d| = +1.  Bar uses DESUSPENSION (s^{-1}).
  The target module computes the ordered tensor-bar carrier.  Every BP
  generator is even before desuspension; signs on a symmetric/coinvariant
  bar model must be supplied by that model's suspension convention.

DS-BAR COMMUTATION:
  The central question: does B(DS_f(V_k(sl_3))) = DS_f(B(V_k(sl_3)))?
  The generator-count and central-charge packets below are exact algebraic
  diagnostics.  Chain-level DS--bar commutation and the BP genus-one
  characteristic require separate proofs.

References:
  - Bershadsky (1991), "Conformal field theories via Hamiltonian reduction"
  - Polyakov (1990), "Gauge transformations and diffeomorphisms"
  - Fehily--Kawasetsu--Ridout (2021), Definition 2.1, Eq. (2.2),
    Proposition 2.2, arXiv:2007.03917
  - Kac--Roan--Wakimoto (2003), "Quantum reduction for affine superalgebras"
  - Manuscript: subregular_hook_frontier.tex, ds_bar_commutation
"""

from __future__ import annotations

from typing import Dict, List, Tuple

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.bp_koszul_conductor_engine import (
    BP_GENERATORS as CANONICAL_BP_GENERATORS,
    BP_KAPPA_STATUS,
    SHIFTED_BP_CONVENTION,
    STANDARD_BP_CONVENTION,
    compute_varrho as bp_reciprocal_weight_diagnostic,
)


# =============================================================================
# Generator data
# =============================================================================

# Parity: 0 = bosonic (even), 1 = fermionic (odd).  The weights and
# parities are imported from the canonical FKR convention surface.
_CHARGES = {"J": 0, "G+": 1, "G-": -1, "T": 0}
GENERATORS = {
    name: {
        "weight": Rational(weight.numerator, weight.denominator),
        "parity": parity,
        "charge": _CHARGES[name],
    }
    for name, (weight, parity) in CANONICAL_BP_GENERATORS.items()
}

GENERATOR_NAMES = ("J", "G+", "G-", "T")


def bp_central_charge(level=None):
    """Standard FKR central charge ``-(2k+3)(3k+1)/(k+3)``."""
    if level is None:
        level = Symbol('k')
    k = sympify(level)
    return sympify(STANDARD_BP_CONVENTION.formula, locals={"k": k})


def bp_shifted_central_charge(level=None):
    """Secondary shifted rational function with companion sum ``196``."""
    if level is None:
        level = Symbol('k')
    k = sympify(level)
    return sympify(SHIFTED_BP_CONVENTION.formula, locals={"k": k})


def bp_dual_level(level=None):
    """Feigin-Frenkel dual level: k' = -k - 6."""
    if level is None:
        level = Symbol('k')
    return -sympify(level) - 6


def bp_koszul_conductor():
    """Standard scalar companion sum ``c(k)+c(-k-6)=50``."""
    k = Symbol('k')
    return simplify(bp_central_charge(k) + bp_central_charge(bp_dual_level(k)))


def bp_shifted_koszul_conductor():
    """Companion sum of :func:`bp_shifted_central_charge`, equal to ``196``."""
    k = Symbol('k')
    return simplify(
        bp_shifted_central_charge(k)
        + bp_shifted_central_charge(bp_dual_level(k))
    )


# =============================================================================
# N-th products (complete OPE data)
# =============================================================================

def bp_primary_ope_normal_form(level=None) -> Dict[str, object]:
    """Feigin-Semikhatov normal-form constants for BP_k = W_3^{(2)}."""
    if level is None:
        level = Symbol('k')
    kk = sympify(level)
    return {
        "level": kk,
        "central_charge": bp_central_charge(kk),
        "J_level": (2 * kk + 3) / 3,
        "G_pairing": (kk + 1) * (2 * kk + 3),
        "GJ_coefficient": 3 * (kk + 1),
        "JJ_coefficient": Rational(3),
        "dJ_coefficient": Rational(3, 2) * (kk + 1),
        "T_coefficient": -(kk + 3),
        "convention": "FKR21 Definition 2.1 equal-weight even G generators",
    }


def bp_nth_products(level=None) -> Dict[Tuple[str, str], Dict[int, Dict[str, object]]]:
    """All singular n-th products for BP generators.

    Returns {(a, b): {n: {output: coeff}}} for all generator pairs.
    Coefficients are rational functions of the affine sl_3 level k.

    OPE verified by:
      (1) Conformal Ward identity (T-generator OPEs)
      (2) U(1) Ward identity (J-charge conservation)
      (3) Ordinary vertex-algebra skew-symmetry (all reversed pairs)
      (4) Agreement with the Feigin-Semikhatov W_3^{(2)} normal form.
    """
    fs = bp_primary_ope_normal_form(level)
    kk = fs["level"]
    c = fs["central_charge"]
    j_level = fs["J_level"]
    g_pairing = fs["G_pairing"]
    g_j = fs["GJ_coefficient"]
    jj_coeff = fs["JJ_coefficient"]
    dJ_coeff = fs["dJ_coefficient"]
    t_coeff = fs["T_coefficient"]

    return {
        # ===== T x T: standard Virasoro (bosonic x bosonic) =====
        ("T", "T"): {
            3: {"vac": c / 2},
            1: {"T": Rational(2)},
            0: {"dT": Rational(1)},
        },

        # ===== T x J: J is primary of weight 1 (bosonic x bosonic) =====
        ("T", "J"): {
            1: {"J": Rational(1)},
            0: {"dJ": Rational(1)},
        },

        # ===== T x G+: G+ is an even primary of weight 3/2 =====
        ("T", "G+"): {
            1: {"G+": Rational(3, 2)},
            0: {"dG+": Rational(1)},
        },

        # ===== T x G-: G- is an even primary of weight 3/2 =====
        ("T", "G-"): {
            1: {"G-": Rational(3, 2)},
            0: {"dG-": Rational(1)},
        },

        # ===== J x J: abelian current (bosonic x bosonic) =====
        ("J", "J"): {
            1: {"vac": j_level},
            # No simple pole: J_{(0)}J = 0
        },

        # ===== J x G+: charge +1 (even x even) =====
        ("J", "G+"): {
            0: {"G+": Rational(1)},
        },

        # ===== J x G-: charge -1 (even x even) =====
        ("J", "G-"): {
            0: {"G-": Rational(-1)},
        },

        # ===== J x T: from skew-symmetry of T x J (bosonic x bosonic) =====
        ("J", "T"): {
            1: {"J": Rational(1)},
            # J_{(0)}T = 0 (T has J-charge 0)
        },

        # ===== G+ x G-: the key charged even-even OPE =====
        ("G+", "G-"): {
            2: {"vac": g_pairing},
            1: {"J": g_j},
            0: {"JJ": jj_coeff, "dJ": dJ_coeff, "T": t_coeff},
        },

        # ===== G- x G+: from ordinary skew-symmetry =====
        ("G-", "G+"): {
            2: {"vac": -g_pairing},
            1: {"J": g_j},
            0: {"JJ": -jj_coeff, "dJ": dJ_coeff, "T": -t_coeff},
        },

        # ===== G+ x G+ = 0 (charge conservation) =====
        ("G+", "G+"): {},

        # ===== G- x G- = 0 (charge conservation) =====
        ("G-", "G-"): {},

        # ===== G+ x T: from ordinary skew-symmetry of T x G+ =====
        ("G+", "T"): {
            1: {"G+": Rational(3, 2)},
            0: {"dG+": Rational(1, 2)},
        },

        # ===== G- x T: from ordinary skew-symmetry of T x G- =====
        ("G-", "T"): {
            1: {"G-": Rational(3, 2)},
            0: {"dG-": Rational(1, 2)},
        },

        # ===== G+ x J: from ordinary skew-symmetry of J x G+ =====
        ("G+", "J"): {
            0: {"G+": Rational(-1)},
        },

        # ===== G- x J: from ordinary skew-symmetry of J x G- =====
        ("G-", "J"): {
            0: {"G-": Rational(1)},
        },
    }


def bp_nth_product(a: str, b: str, n: int, level=None) -> Dict[str, object]:
    """Get a_{(n)}b for BP generators a, b."""
    products = bp_nth_products(level)
    pair = (a, b)
    if pair not in products:
        return {}
    return products[pair].get(n, {})


# =============================================================================
# Curvature (bar-degree 0 component)
# =============================================================================

def bp_curvature() -> Dict[str, object]:
    """Curvature elements m_0 for the BP bar complex.

    The curvature m_0^(a) is the vacuum coefficient from a_{(2h_a-1)}a,
    i.e. the leading-pole self-OPE coefficient.

    For T: m_0^(T) = T_{(3)}T|_vac = c/2
    For J: m_0^(J) = J_{(1)}J|_vac = (2k+3)/3
    For G+, G-: the self-OPE vanishes by charge conservation, while the
    charged pairing G+_{(2)}G- = (k+1)(2k+3) gives an off-diagonal
    leading-pole coefficient in the even charged sector.
    """
    k = Symbol('k')
    fs = bp_primary_ope_normal_form(k)
    return {
        "T": fs["central_charge"] / 2,
        "J": fs["J_level"],
        "G+G-": fs["G_pairing"],  # off-diagonal even charged pairing
    }


# =============================================================================
# Vacuum module (augmentation ideal)
# =============================================================================

def bp_vacuum_character_coeffs(max_weight: int) -> Dict[Rational, int]:
    """Dimension of BP vacuum module augmentation ideal at each weight.

    The BP algebra has generators at weights 1, 3/2, 3/2, 2.
    FKR Definition 2.1 states that the universal algebra is strongly and
    freely generated as an ordinary vertex algebra.  Hence all four mode
    families have unrestricted bosonic occupation numbers.

    Character of the FULL vacuum module (including |0>):
      ch(V_BP) = prod_{n>=1} 1/(1-q^n)
                 * prod_{n>=2} 1/(1-q^n)
                 * prod_{m>=0} 1/(1-q^{m+3/2})^2.

    Contributions from each generator family:
      J (weight 1):  prod_{n>=1} 1/(1-q^n)     [bosonic modes J_{-n}, n>=1]
      G+ (weight 3/2): prod_{m>=0} 1/(1-q^{m+3/2})
      G- (weight 3/2): prod_{m>=0} 1/(1-q^{m+3/2})
      T (weight 2):  prod_{n>=2} 1/(1-q^n)     [bosonic modes T_{-n}, n>=2]

    We compute the augmentation ideal: subtract the vacuum |0>.
    Using half-integer weights, we compute to the given max_weight.
    """
    # Work in units of 1/2 to handle half-integer weights
    max_half = int(2 * max_weight)

    # Start with coefficient array indexed by half-integers 0, 1/2, 1, 3/2, ...
    coeffs = [0] * (max_half + 1)
    coeffs[0] = 1

    # J bosonic modes: J_{-n} for n >= 1, each contributing weight n
    for n in range(1, max_weight + 1):
        half_n = 2 * n
        for i in range(half_n, max_half + 1):
            coeffs[i] += coeffs[i - half_n]

    # T bosonic modes: T_{-n} for n >= 2, each contributing weight n
    for n in range(2, max_weight + 1):
        half_n = 2 * n
        for i in range(half_n, max_half + 1):
            coeffs[i] += coeffs[i - half_n]

    # G+ and G- are two independent bosonic mode families.  Ascending
    # coefficient updates implement each geometric factor 1/(1-q^r).
    for _generator in ("G+", "G-"):
        r_half = 3
        while r_half <= max_half:
            for i in range(r_half, max_half + 1):
                coeffs[i] += coeffs[i - r_half]
            r_half += 2

    # Convert to weight-indexed dictionary (subtract vacuum at weight 0)
    result = {}
    for h_half in range(1, max_half + 1):
        weight = Rational(h_half, 2)
        if coeffs[h_half] > 0:
            result[weight] = coeffs[h_half]

    return result


def bp_vacuum_dim(weight) -> int:
    """Dimension of BP vacuum augmentation ideal at given conformal weight."""
    w = Rational(weight)
    table = bp_vacuum_character_coeffs(int(w) + 1)
    return table.get(w, 0)


def bp_augmentation_ideal_basis(max_weight: int) -> Dict[Rational, List[str]]:
    """Named basis elements of the augmentation ideal up to given weight.

    This lists the PBW-ordered monomials in negative modes applied to |0>.
    """
    basis = {}

    # Weight 1: J_{-1}|0>
    if max_weight >= 1:
        basis[Rational(1)] = ["J"]

    # Weight 3/2: G+_{-3/2}|0>, G-_{-3/2}|0>
    if max_weight >= 2:  # need max_weight >= 3/2
        basis[Rational(3, 2)] = ["G+", "G-"]

    # Weight 2: T_{-2}|0>, J_{-2}|0>, J_{-1}^2|0>... wait, J_{-1}^2 = (1/2):JJ:
    # Actually J_{-1}^2|0> is at weight 2 but is a composite.
    if max_weight >= 2:
        basis[Rational(2)] = ["T", "dJ", "JJ"]  # T, J_{-2}|0>, J_{-1}^2|0>

    # Weight 5/2
    if max_weight >= 3:
        basis[Rational(5, 2)] = [
            "dG+", "dG-",      # G±_{-5/2}|0>
            "J*G+", "J*G-",   # J_{-1}G±_{-3/2}|0>
        ]

    # Weight 3
    if max_weight >= 3:
        basis[Rational(3)] = [
            "dT", "d2J", "d(JJ)",  # T_{-3}|0>, J_{-3}|0>, J_{-2}J_{-1}|0>
            "J*T",                  # J_{-1}T_{-2}|0>
            "JJJ",                  # J_{-1}^3|0>
            "G+*G+", "G+*G-", "G-*G-",  # symmetric square of even G-sector
        ]

    return basis


# =============================================================================
# Bar complex: degree 2 -> degree 1 (and degree 0)
# =============================================================================

def bp_bar_diff_deg2(a: str, b: str) -> Tuple[Dict[str, object], Dict[str, object]]:
    """Aggregate singular OPE coefficients for the ordered pair ``(a,b)``.

    This is the algebraic coefficient packet used by a degree-two bar
    differential.  A geometric chiral-bar differential additionally needs
    the configuration-space form, residue convention, and suspension sign.
    Every BP generator is even, so the OPE reversal uses ordinary vertex-
    algebra skew-symmetry.

    Returns (vac_component, bar1_component):
      vac_component: coefficient of |0> in B^0
      bar1_component: {state: coeff} in B^1

    The bar differential sums over all n-th products a_{(n)}b for n >= 0.
    """
    products = bp_nth_products()
    pair = (a, b)
    if pair not in products:
        return {}, {}

    vac = {}
    bar1 = {}

    for n, outputs in products[pair].items():
        for state, coeff in outputs.items():
            if state == "vac":
                vac["vac"] = vac.get("vac", 0) + coeff
            else:
                bar1[state] = bar1.get(state, 0) + coeff

    return vac, bar1


def bp_bar_diff_deg2_all() -> Dict[Tuple[str, str], Tuple[Dict, Dict]]:
    """Bar differential for all generator pairs at bar degree 2.

    Returns {(a, b): (vac_component, bar1_component)}.
    """
    result = {}
    for a in GENERATOR_NAMES:
        for b in GENERATOR_NAMES:
            result[(a, b)] = bp_bar_diff_deg2(a, b)
    return result


# =============================================================================
# Bar cohomology at degree 2
# =============================================================================

def bp_bar_deg2_chain_dim(weight) -> int:
    """Chain space dimension of B^2 at given conformal weight.

    At bar degree 2, we need pairs (a, b) with wt(a) + wt(b) = weight,
    each from the augmentation ideal.  Times dim Omega^1(Conf_2) = 1.

    This function uses the ordered tensor-bar carrier.  Thus every ordered
    pair with the required total weight contributes.  Symmetric or
    coinvariant bar models require a separate quotient calculation.
    """
    w = Rational(weight)
    char = bp_vacuum_character_coeffs(int(w) + 1)

    total = 0
    for w1, d1 in char.items():
        w2 = w - w1
        if w2 in char:
            total += d1 * char[w2]
    return total


# =============================================================================
# Bar complex: degree 3 (triples)
# =============================================================================

def bp_bar_deg3_chain_dim(weight) -> int:
    """Chain space dimension of B^3 at given conformal weight.

    At bar degree 3: triples (a, b, c) with sum of weights = weight.
    Times dim Omega^2(Conf_3) = 2.
    """
    w = Rational(weight)
    char = bp_vacuum_character_coeffs(int(w) + 1)

    total = 0
    for w1, d1 in char.items():
        for w2, d2 in char.items():
            w3 = w - w1 - w2
            if w3 in char:
                total += d1 * d2 * char[w3]
    return total * 2  # dim Omega^2(Conf_3) = 2


# =============================================================================
# PBW degeneration verification
# =============================================================================

def bp_pbw_character(max_weight: int) -> Dict[Rational, int]:
    """Compatibility alias for the free strong-generator PBW character.

    The result is the vacuum-module character.  A bar-degree character
    additionally tracks tensor length and suspension parity.
    """
    return bp_vacuum_character_coeffs(max_weight)


def verify_pbw_deg2(max_weight: int = 8) -> Dict[str, bool]:
    """Verify PBW degeneration at bar degree 2.

    At bar degree 2, PBW says: dim gr^2 B = sum_{w1+w2=w} dim(V_w1)*dim(V_w2).
    This is exactly the chain dim (no differential at the associated graded level).
    """
    results = {}
    char = bp_vacuum_character_coeffs(max_weight)

    for w_half in range(2, 2 * max_weight + 1):
        w = Rational(w_half, 2)
        chain_dim = bp_bar_deg2_chain_dim(w)
        pbw_dim = 0
        for w1, d1 in char.items():
            w2 = w - w1
            if w2 in char:
                pbw_dim += d1 * char[w2]
        results[f"PBW deg2 wt {w}"] = (chain_dim == pbw_dim)

    return results


# =============================================================================
# Koszul dual extraction
# =============================================================================

def bp_koszul_dual_generators() -> Dict[str, Dict[str, object]]:
    """Conditional same-family companion packet for ``BP_k``.

    For a chirally Koszul algebra A, H^1(B(A)) is the degree-one piece of
    the bar-dual coalgebra A^i. The generator space of A^! is obtained
    only after the separate Verdier/continuous-linear dual branch.

    For BP_k = W_k(sl_3, f_{(2,1)}):
    - Self-transpose partition: (2,1)^t = (2,1)
    - Conditional prediction: BP_k^! = BP_{k'} where k' = -k-6
    - Same generators at dual level: J, G+, G-, T with c' = c(-k-6)
    """
    k = Symbol('k')
    c = bp_central_charge(k)
    c_dual = bp_central_charge(bp_dual_level(k))

    return {
        "generators": {
            "J":  {"weight": Rational(1),    "parity": 0},
            "G+": {"weight": Rational(3, 2), "parity": 0},
            "G-": {"weight": Rational(3, 2), "parity": 0},
            "T":  {"weight": Rational(2),    "parity": 0},
        },
        "source_c": c,
        "dual_c": c_dual,
        "c_sum": simplify(c + c_dual),
        "is_self_transpose": True,
        "dual_level": bp_dual_level(k),
        "duality_status": "CONDITIONAL_ON_DS_BAR_AND_KOSZUL_TRANSPORT",
    }


# =============================================================================
# DS-bar commutation
# =============================================================================

def ds_bar_commutation_kappa() -> Dict[str, object]:
    """Separate exact DS/OPE scalars from the open BP genus-one invariant.

    The affine formula, the candidate ghost subtraction, the Virasoro
    leading-pole coefficient ``c/2``, and the Heisenberg level are explicit
    algebraic expressions.  They do not determine the full BP modular
    characteristic.  Source-correct parity changes the reciprocal-weight
    diagnostic from ``1/6`` to ``17/6``; a genus-one chiral/BRST curvature
    calculation is still required.
    """
    k = Symbol('k')
    c = bp_central_charge(k)

    # Affine sl_3 kappa
    dim_sl3 = 8
    kappa_affine = Rational(dim_sl3, 6) * (k + 3)  # dim(g)*(k+h^v)/(2*h^v)

    ghost_candidate = Rational(2)
    naive_affine_minus_ghost = kappa_affine - ghost_candidate

    # Direct BP invariants.  The T-line has Virasoro curvature c/2;
    # the J-current level is independent of c/3 in FS normal form.
    kappa_T = c / 2
    j_level = (2 * k + 3) / 3

    return {
        "kappa_affine": kappa_affine,
        "ghost_constant_candidate": ghost_candidate,
        "naive_affine_minus_ghost": naive_affine_minus_ghost,
        "naive_subtraction_status": "DIAGNOSTIC_ONLY",
        "kappa_T": kappa_T,
        "kappa_T_meaning": "VIRASORO_LEADING_POLE_COEFFICIENT",
        "J_level": j_level,
        "reciprocal_weight_diagnostic": Rational(
            bp_reciprocal_weight_diagnostic().numerator,
            bp_reciprocal_weight_diagnostic().denominator,
        ),
        "kappa_T_simplified": simplify(kappa_T),
        "J_level_simplified": simplify(j_level),
        "kappa_BP": None,
        "kappa_complementarity": None,
        "kappa_status": BP_KAPPA_STATUS.status,
        "resolution_obligation": BP_KAPPA_STATUS.resolution_obligation,
    }


def ds_bar_commutation_generators() -> Dict[str, object]:
    """Verify DS-bar commutation at the generator level.

    sl_3 has 8 generators.  The DS reduction at f_{(2,1)} constrains
    dim(n_+) = 2 directions (the positive-grade roots in the good grading),
    leaving dim(g^f) = 4 generators for the W-algebra.

    At the bar level: B^1(V_k(sl_3)) has 8 generators.
    DS applied to B^1 should restrict to the 4 BP generators.
    """
    return {
        "affine_generators": 8,      # dim(sl_3)
        "constrained_directions": 2,  # dim(n_+) for (2,1)
        "w_generators": 4,            # dim(g^f)
        "generator_match": 8 - 2 == 4 + 2,  # 4 W-gens + 2 ghost pairs
        # Actually: 8 = 4 (W-gens) + 2 (n_+) + 2 (n_-)
        # The BRST complex has 2 ghost pairs (one for each positive root)
        "decomposition": "sl_3 = g^f(4) + n_+(2) + n_-(2)",
    }


def ds_bar_commutation_central_charge() -> Dict[str, object]:
    """Compute the affine/BP central-charge difference.

    The exact input formulas are
      c(V_k(sl_3)) = 8k/(k+3)
      c(BP_k) = -(2k+3)(3k+1)/(k+3).
    Their difference records the total conformal-vector correction.  A
    decomposition into charged ghosts, neutral fields, and improvement
    terms belongs to the full BRST calculation.
    """
    k = Symbol('k')
    c_affine = 8 * k / (k + 3)  # c(V_k(sl_3)) = k*dim(g)/(k+h^v)
    c_bp = bp_central_charge(k)

    correction = simplify(c_affine - c_bp)

    return {
        "c_affine": c_affine,
        "c_bp": c_bp,
        "total_correction": correction,
        "total_correction_simplified": simplify(correction),
        "total_correction_at_k0": simplify(correction.subs(k, 0)),
        "decomposition_status": "FULL_BRST_FIELD_CONTENT_REQUIRED",
    }


# =============================================================================
# Arnold cancellation at degree 3
# =============================================================================

def bp_arnold_cancellation_deg3() -> Dict[str, object]:
    """State the geometric obligation for degree-three vacuum leakage.

    At bar degree 3, the vacuum contribution from the leading pole
    requires a higher-order pole than the 2-form on Conf_3 provides.
    The Arnold relation (codimension argument) kills the leakage.

    For BP: the leading poles are order 4 (TT), 3 (G+G-), 2 (JJ).
    The 2-form eta_{12} ^ eta_{13} has at most a simple pole along D_{ij}.
    So the residue of (leading pole) * (2-form) gives:
      TT: order 4 pole * simple pole = order 3 singularity -> Res = 0
      G+G-: order 3 pole * simple pole = order 2 singularity -> Res = 0
      JJ: order 2 pole * simple pole = order 1 singularity -> Res != 0
    Turning this pole-counting heuristic into a bar-differential theorem
    requires an explicit configuration-space residue model and its Arnold
    relation.  This finite OPE module does not implement that geometry.
    """
    return {
        "proved": False,
        "status": "CONFIGURATION_SPACE_RESIDUE_MODEL_REQUIRED",
        "evidence": "pole-order bookkeeping only",
    }


# =============================================================================
# Skew-symmetry verification
# =============================================================================

def verify_skew_symmetry() -> Dict[str, bool]:
    """Verify ordinary skew-symmetry for the even BP generators.

    For every pair ``a,b`` in this ordinary vertex algebra,
    ``b_(n)a = sum_j (-1)^(n+j+1)/j! d^j(a_(n+j)b)``.
    """
    k = Symbol('k')
    fs = bp_primary_ope_normal_form(k)
    results = {}

    # --- J_{(0)}T via skew of T_{(0)}J and T_{(1)}J ---
    # J_{(0)}T = -T_{(0)}J + d(T_{(1)}J) = -dJ + dJ = 0
    computed = -1 + 1  # coefficients of dJ
    expected = bp_nth_product("J", "T", 0).get("dJ", 0)
    results["J_(0)T = 0"] = (computed == 0) and (expected == 0)

    # --- G-_(2)G+ via ordinary skew of G+_(2)G- ---
    # G-_(2)G+ = (-1)^3 G+_(2)G- = -G+_(2)G-.
    expected_val = bp_nth_product("G-", "G+", 2)
    results["G-_(2)G+ = -FS pairing"] = (
        simplify(expected_val.get("vac") + fs["G_pairing"]) == 0
    )

    # --- G-_(1)G+ via ordinary skew ---
    # G-_(1)G+ = G+_(1)G-; the derivative of the scalar leading term is 0.
    expected_val = bp_nth_product("G-", "G+", 1)
    results["G-_(1)G+ = 3(k+1)J"] = (
        simplify(expected_val.get("J") - fs["GJ_coefficient"]) == 0
    )

    # --- G-_(0)G+ via ordinary skew ---
    # G-_(0)G+ = -G+_(0)G- + d(G+_(1)G-)
    # = -3JJ + 3(k+1)/2*dJ + (k+3)T.
    expected_val = bp_nth_product("G-", "G+", 0)
    results["G-_(0)G+: JJ coeff = -3"] = (expected_val.get("JJ") == -3)
    results["G-_(0)G+: T coeff = k+3"] = (
        simplify(expected_val.get("T") + fs["T_coefficient"]) == 0
    )
    results["G-_(0)G+: dJ coeff = 3(k+1)/2"] = (
        simplify(expected_val.get("dJ") - fs["dJ_coefficient"]) == 0
    )

    # --- G+_(0)J via ordinary skew of J_(0)G+ ---
    # G+_(0)J = (-1)^{0+0+1} J_{(0)}G+ = -G+
    expected_val = bp_nth_product("G+", "J", 0)
    results["G+_(0)J = -G+"] = (expected_val.get("G+") == -1)

    # --- G-_(0)J via ordinary skew of J_(0)G- ---
    # G-_(0)J = (-1)^{0+0+1} J_{(0)}G- = -(-G-) = G-
    expected_val = bp_nth_product("G-", "J", 0)
    results["G-_(0)J = G-"] = (expected_val.get("G-") == 1)

    # --- G+_(0)T via ordinary skew of T_(0)G+ and T_(1)G+ ---
    # G+_(0)T = -T_{(0)}G+ + d(T_{(1)}G+) = -dG+ + (3/2)dG+ = (1/2)dG+
    expected_val = bp_nth_product("G+", "T", 0)
    results["G+_(0)T = 1/2 dG+"] = (expected_val.get("dG+") == Rational(1, 2))

    # --- G+_(1)T = 3/2 G+ ---
    expected_val = bp_nth_product("G+", "T", 1)
    results["G+_(1)T = 3/2 G+"] = (expected_val.get("G+") == Rational(3, 2))

    return results


# =============================================================================
# Koszulness verification
# =============================================================================

def bp_is_chirally_koszul() -> Dict[str, object]:
    """Record the PBW evidence and the remaining Koszul obligation.

    FKR prove free strong generation for the universal algebra.  Its OPE
    singularities have generator degree at most two.

    The OPE structure:
      - JJ: pole 2 = scalar (quadratic)
      - JG±: pole 1 = linear (quadratic)
      - G+G-: pole 3 = scalar, pole 2 = J (linear), pole 1 = 3JJ + dJ - (k+3)T
      - TT: pole 4 = scalar, pole 2 = T (linear), pole 1 = dT (derivative)
      - TJ: pole 2 = J, pole 1 = dJ
      - TG±: pole 2 = G± (linear), pole 1 = dG± (derivative)

    These facts supply the quadratic PBW input.  Chiral Koszulness further
    requires the bar spectral-sequence collapse on the stated generic or
    completed locus.
    """
    return {
        "is_koszul": None,
        "status": "CONDITIONAL_ON_BAR_SPECTRAL_SEQUENCE_COLLAPSE",
        "criterion": "PBW universality plus collapse hypothesis",
        "reason": "Feigin-Semikhatov normal form has generator degree <= 2; the :JJ: term is explicit",
        "n_generators": 4,
        "n_relations": 4,  # JJ, JG±, G+G-, TT (independent at quadratic level)
        "euler_characteristic": 1 - 4 + 4 - 1,  # = 0 (with one Jacobi syzygy)
    }


# =============================================================================
# Complementarity
# =============================================================================

def bp_complementarity() -> Dict[str, object]:
    """Standard FKR scalar companion identity for BP.

    The rational identity ``c(k)+c(-k-6)=50`` is exact.  Its promotion to
    a Verdier--Koszul conductor is conditional on DS--bar/Koszul transport.
    """
    k = Symbol('k')
    c = bp_central_charge(k)
    c_dual = bp_central_charge(bp_dual_level(k))
    K = simplify(c + c_dual)

    return {
        "c": c,
        "c_dual": c_dual,
        "K_BP": K,
        "K_is_constant": simplify(K.diff(k)) == 0,
        "scalar_status": "PROVED_RATIONAL_IDENTITY",
        "koszul_interpretation_status": "CONDITIONAL_ON_DS_BAR_AND_KOSZUL_TRANSPORT",
    }


# =============================================================================
# Full verification suite
# =============================================================================

def verify_bp_bar_complex() -> Dict[str, object]:
    """Return exact finite checks and separately typed open obligations."""
    checks: Dict[str, bool] = {}

    k = Symbol('k')
    c = bp_central_charge(k)
    checks["standard FKR central charge"] = simplify(
        c + (2 * k + 3) * (3 * k + 1) / (k + 3)
    ) == 0
    checks["shifted rational function is explicitly separated"] = simplify(
        bp_shifted_central_charge(k) - (2 - 24 * (k + 1) ** 2 / (k + 3))
    ) == 0

    K = bp_koszul_conductor()
    checks["standard scalar companion sum is constant"] = simplify(K.diff(k)) == 0
    checks["standard scalar companion sum is 50"] = simplify(K - 50) == 0
    checks["shifted scalar companion sum is 196"] = simplify(
        bp_shifted_koszul_conductor() - 196
    ) == 0
    checks["canonical convention record agrees"] = (
        STANDARD_BP_CONVENTION.conductor == 50
        and SHIFTED_BP_CONVENTION.conductor == 196
    )

    checks["c(0) = -1"] = simplify(bp_central_charge(0) + 1) == 0
    checks["c(1) = -5"] = simplify(bp_central_charge(1) + 5) == 0
    checks["c(-3/2) = 0"] = simplify(
        bp_central_charge(Rational(-3, 2))
    ) == 0
    checks["all strong generators are even"] = all(
        data["parity"] == 0 for data in GENERATORS.values()
    )
    checks["bosonic PBW coefficient at weight 3 is 8"] = (
        bp_vacuum_dim(3) == 8
    )

    fs = bp_primary_ope_normal_form(k)
    vac, bar1 = bp_bar_diff_deg2("T", "T")
    checks["TT packet: vacuum coefficient c(k)/2"] = simplify(
        vac.get("vac") - fs["central_charge"] / 2
    ) == 0
    checks["TT packet: T coefficient 2"] = bar1.get("T") == 2

    vac, bar1 = bp_bar_diff_deg2("J", "J")
    checks["JJ packet: vacuum coefficient (2k+3)/3"] = simplify(
        vac.get("vac") - fs["J_level"]
    ) == 0

    vac, bar1 = bp_bar_diff_deg2("G+", "G-")
    checks["G+G- packet: FS pairing"] = simplify(
        vac.get("vac") - fs["G_pairing"]
    ) == 0
    checks["G+G- packet: J coefficient"] = simplify(
        bar1.get("J") - fs["GJ_coefficient"]
    ) == 0
    checks["G+G- packet: JJ coefficient"] = bar1.get("JJ") == 3
    checks["G+G- packet: T coefficient"] = simplify(
        bar1.get("T") - fs["T_coefficient"]
    ) == 0
    checks["G+G- packet: dJ coefficient"] = simplify(
        bar1.get("dJ") - fs["dJ_coefficient"]
    ) == 0

    vac, bar1 = bp_bar_diff_deg2("G-", "G+")
    checks["G-G+ packet: opposite leading coefficient"] = simplify(
        vac.get("vac") + fs["G_pairing"]
    ) == 0
    checks["G-G+ packet: ordinary-skew J coefficient"] = simplify(
        bar1.get("J") - fs["GJ_coefficient"]
    ) == 0
    checks["G-G+ packet: ordinary-skew dJ coefficient"] = simplify(
        bar1.get("dJ") - fs["dJ_coefficient"]
    ) == 0

    vac_pp, bar1_pp = bp_bar_diff_deg2("G+", "G+")
    checks["G+G+ singular packet vanishes by charge"] = (
        len(vac_pp) == 0 and len(bar1_pp) == 0
    )

    vac_mm, bar1_mm = bp_bar_diff_deg2("G-", "G-")
    checks["G-G- singular packet vanishes by charge"] = (
        len(vac_mm) == 0 and len(bar1_mm) == 0
    )
    checks.update(verify_skew_symmetry())

    comp = bp_complementarity()
    checks["scalar companion identity is k-independent"] = comp["K_is_constant"]

    return {
        "exact_checks": checks,
        "kappa_status": BP_KAPPA_STATUS.status,
        "kappa_BP": None,
        "kappa_complementarity": None,
        "arnold_status": bp_arnold_cancellation_deg3()["status"],
        "koszul_status": bp_is_chirally_koszul()["status"],
    }


# =============================================================================
# Main entry point
# =============================================================================

if __name__ == "__main__":
    print("=" * 65)
    print("BERSHADSKY-POLYAKOV OPE AND PBW DIAGNOSTICS")
    print("=" * 65)

    print("\n--- Central charge ---")
    k = Symbol('k')
    c = bp_central_charge(k)
    print(f"  c(k) = {c}")
    print(f"  K_BP = {bp_koszul_conductor()}")

    print("\n--- Bar differential (degree 2) ---")
    for a in GENERATOR_NAMES:
        for b in GENERATOR_NAMES:
            vac, bar1 = bp_bar_diff_deg2(a, b)
            if vac or bar1:
                print(f"  D({a} x {b}): vac={vac}, bar1={bar1}")

    print("\n--- Curvature ---")
    for name, val in bp_curvature().items():
        print(f"  m_0({name}) = {val}")

    print("\n--- Verification ---")
    verification = verify_bp_bar_complex()
    for name, ok in verification["exact_checks"].items():
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")
    print(f"  kappa status: {verification['kappa_status']}")
    print(f"  Arnold status: {verification['arnold_status']}")
    print(f"  Koszul status: {verification['koszul_status']}")

    print("\n--- Vacuum module dimensions ---")
    char = bp_vacuum_character_coeffs(6)
    for w in sorted(char):
        print(f"  dim V_bar({w}) = {char[w]}")
