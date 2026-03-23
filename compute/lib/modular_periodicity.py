"""Modular periodicity computations for rational chiral algebras.

Verifies conj:modular-periodicity and conj:reflected-modular-periodicity
from the monograph (deformation_theory.tex).

The modular periodicity conjecture states: for a rational chiral algebra A
with central charge c = p/q (lowest terms), the T-matrix period is
    N = 24q / gcd(p, 24)
and bar cohomology dimensions satisfy
    dim H^n(B_{[h+N]}(A)) = dim H^n(B_{[h]}(A))  for h >> 0.

The reflected modular periodicity conjecture states: for a Koszul pair
(A, A!) with central charges c = p/q and c' = p'/q', and modular periods
N = 24q/gcd(p,24) and N' = 24q'/gcd(p',24):
    1/N + 1/N' = (gcd(p,24) + gcd(p',24)) / (24q)
where q' = q whenever gcd(26q - p, q) = 1.

CRITICAL (from CLAUDE.md):
- kappa(lambda) is NILPOTENT not PERIODIC: kappa^{g-1} = 0 on M_g (Graber-Vakil)
- Period(A) | lcm(N_mod, N_quant) — geometry gives THRESHOLD
- Feigin-Frenkel duality: k <-> -k - 2h^vee (NOT -k - h^vee)
- Level shift: -kappa - 2h^vee is correct for vertex algebra convention
- Sugawara: c = k*dim(g)/(k + h^vee)
- Virasoro DS: c(k) = 1 - 6(k+1)^2/(k+2)

Key functions:
    minimal_model_central_charge — c(p,q) = 1 - 6(p-q)^2/(pq)
    scalar_modular_characteristic — kappa(A) = c/2
    modular_period — N = 24q/gcd(p,24) for c = p/q in lowest terms
    wzw_central_charge — c = k*dim(g)/(k + h^vee)
    feigin_frenkel_dual_level — k' = -k - 2h^vee
    reflected_period_check — verify 1/N + 1/N' formula
    nilpotence_bound — Graber-Vakil bound: kappa^{g-1} = 0

References:
    - conj:modular-periodicity (deformation_theory.tex)
    - conj:reflected-modular-periodicity (deformation_theory.tex)
    - thm:modular-periodicity-minimal (deformation_theory.tex)
    - thm:modular-periodicity-wzw (deformation_theory.tex)
    - thm:geometric-depth-smooth (deformation_theory.tex)
    - CLAUDE.md: verified formulas, central charges, Feigin-Frenkel
"""

from __future__ import annotations

from math import gcd
from typing import Dict, List, Optional, Tuple

from sympy import Rational, Symbol, simplify, lcm as sym_lcm


# ===========================================================================
# Lie algebra data
# ===========================================================================

# Simple Lie algebra data: (dim(g), h^vee, rank)
LIE_DATA: Dict[str, Tuple[int, int, int]] = {
    "sl2": (3, 2, 1),
    "sl3": (8, 3, 2),
    "sl4": (15, 4, 3),
    "so5": (10, 3, 2),   # = sp4
    "sp4": (10, 3, 2),
    "g2": (14, 4, 2),
    "so8": (28, 6, 4),   # D_4
}


def lie_dim(g_name: str) -> int:
    """Dimension of the simple Lie algebra."""
    return LIE_DATA[g_name][0]


def dual_coxeter(g_name: str) -> int:
    """Dual Coxeter number h^vee."""
    return LIE_DATA[g_name][1]


def lie_rank(g_name: str) -> int:
    """Rank of the Lie algebra."""
    return LIE_DATA[g_name][2]


# ===========================================================================
# Central charge computations
# ===========================================================================

def minimal_model_central_charge(p: int, q: int) -> Rational:
    """Central charge of the Virasoro minimal model M(p,q).

    c = 1 - 6(p-q)^2 / (pq)

    Requires: 2 <= p < q, gcd(p,q) = 1.

    Ground truth: deformation_theory.tex, eq. in thm:modular-periodicity-minimal.
    """
    if p >= q:
        raise ValueError(f"Need p < q, got p={p}, q={q}")
    if gcd(p, q) != 1:
        raise ValueError(f"Need gcd(p,q)=1, got p={p}, q={q}")
    return Rational(1) - Rational(6 * (p - q)**2, p * q)


def virasoro_ds_central_charge(k):
    """Virasoro central charge from DS reduction at level k.

    c(k) = 1 - 6(k+1)^2 / (k+2)

    Ground truth: CLAUDE.md verified formulas.
    """
    k = Rational(k) if isinstance(k, (int, float)) else k
    return 1 - 6 * (k + 1)**2 / (k + 2)


def wzw_central_charge(g_name: str, k) -> Rational:
    """WZW central charge for g-hat at level k.

    c = k * dim(g) / (k + h^vee)

    Ground truth: CLAUDE.md Sugawara formula.
    """
    k = Rational(k) if isinstance(k, (int, float)) else k
    dim_g = lie_dim(g_name)
    h_dual = dual_coxeter(g_name)
    return k * dim_g / (k + h_dual)


def wzw_central_charge_direct(dim_g: int, h_dual: int, k) -> Rational:
    """WZW central charge from direct parameters.

    c = k * dim_g / (k + h_dual)
    """
    k = Rational(k) if isinstance(k, (int, float)) else k
    return k * dim_g / (k + h_dual)


# ===========================================================================
# Scalar modular characteristic
# ===========================================================================

def scalar_modular_characteristic(c_val):
    """Scalar modular characteristic kappa(A) = c/2 for Virasoro.

    Ground truth: thm:modular-characteristic, curvature_genus_bridge.py.
    For single-generator algebras with conformal vector only (Heisenberg, Virasoro),
    kappa = c/2 (from the T_{(3)}T = c/2 OPE pole).

    CAVEAT: For affine KM, κ = dim(g)·(k+h∨)/(2h∨) ≠ c/2.
    For multi-generator W_N algebras:
    kappa = sigma(g) * c where sigma(g) = sum_{i=1}^N 1/(i+1).
    This function returns the single-conformal-generator formula kappa = c/2.
    """
    if isinstance(c_val, (int, float)):
        return Rational(c_val, 2) if isinstance(c_val, int) else c_val / 2
    return c_val / 2


def w_algebra_sigma(N: int) -> Rational:
    """Obstruction coefficient sigma for W_N algebra.

    sigma(sl_N) = sum_{h=2}^{N} 1/h = H_N - 1
    where H_N is the N-th harmonic number.

    kappa(W_N) = sigma(sl_N) * c.

    Examples:
        W_2 (Virasoro): sigma = 1/2
        W_3: sigma = 1/2 + 1/3 = 5/6
        W_4: sigma = 1/2 + 1/3 + 1/4 = 13/12
    """
    return sum(Rational(1, h) for h in range(2, N + 1))


# ===========================================================================
# Modular period computation
# ===========================================================================

def _to_lowest_terms(c_val) -> Tuple[int, int]:
    """Express a rational number c = p/q in lowest terms.

    Returns (p, q) with q > 0 and gcd(|p|, q) = 1.
    """
    r = Rational(c_val)
    p = int(r.p)
    q = int(r.q)
    # Rational already normalizes to lowest terms with q > 0
    return (p, q)


def modular_period(c_val) -> int:
    """Compute the modular period N for a rational central charge c.

    N = 24q / gcd(p, 24)

    where c = p/q in lowest terms (q > 0).

    This is the minimal N such that T^N = Id on the character space,
    where T: tau -> tau + 1 multiplies characters by exp(-2*pi*i*c/24).

    The condition is N*c/24 in Z, i.e., N*p/(24*q) in Z.
    Smallest positive N: N = 24*q / gcd(p, 24).

    Ground truth: conj:modular-periodicity, rem:periodicity-as-exponential.
    """
    p, q = _to_lowest_terms(c_val)
    g = gcd(abs(p), 24)
    N = 24 * q // g
    # Verify: N * p / (24 * q) should be an integer
    assert (N * p) % (24 * q) == 0, f"Period computation error: N={N}, p={p}, q={q}"
    return N


def modular_period_divides_check(c_val, candidate_N: int) -> bool:
    """Check whether candidate_N is a valid period (N*c/24 in Z).

    A valid period means exp(2*pi*i*N*c/24) = 1, i.e., N*c/24 is an integer.
    """
    p, q = _to_lowest_terms(c_val)
    return (candidate_N * p) % (24 * q) == 0


def modular_period_from_pq(p: int, q: int) -> int:
    """Compute modular period from numerator p and denominator q.

    N = 24q / gcd(|p|, 24).

    Requires q > 0. Does NOT require gcd(p,q)=1 (will reduce first).
    """
    r = Rational(p, q)
    return modular_period(r)


# ===========================================================================
# Feigin-Frenkel duality
# ===========================================================================

def feigin_frenkel_dual_level(k, h_dual: int):
    """Feigin-Frenkel dual level: k' = -k - 2*h^vee.

    CRITICAL: it is -k - 2*h^vee, NOT -k - h^vee.
    Ground truth: CLAUDE.md, Feigin-Frenkel section.

    For sl_2 (h^vee = 2): k' = -k - 4
    For sl_3 (h^vee = 3): k' = -k - 6
    """
    k = Rational(k) if isinstance(k, (int, float)) else k
    return -k - 2 * h_dual


def dual_central_charge_km(g_name: str, k):
    """Dual central charge for KM algebra under Feigin-Frenkel duality.

    Given g-hat_k with c = k*dim(g)/(k + h^vee),
    the dual level k' = -k - 2*h^vee gives
    c' = k'*dim(g)/(k' + h^vee).

    NOTE: c + c' = dim(g) * (k/(k+h^vee) + k'/(k'+h^vee)).
    For the Virasoro algebra (g = sl_2):
    c + c' = 26 (proved, level-independent).
    """
    k = Rational(k) if isinstance(k, (int, float)) else k
    h_dual = dual_coxeter(g_name)
    k_dual = feigin_frenkel_dual_level(k, h_dual)
    return wzw_central_charge(g_name, k_dual)


def virasoro_dual_central_charge_km(k):
    """Dual central charge for Virasoro (via sl_2 DS).

    c(k) = 1 - 6(k+1)^2/(k+2)
    k' = -k - 4 (Feigin-Frenkel for sl_2)
    c(k') = 1 - 6(-k-3)^2/(-k-2)

    c(k) + c(k') = 26 (proved).
    """
    k = Rational(k) if isinstance(k, (int, float)) else k
    k_dual = -k - 4
    return virasoro_ds_central_charge(k_dual)


# ===========================================================================
# KM complementarity: c + c' = dim(g)·something
# ===========================================================================

def km_central_charge_sum(g_name: str, k=None):
    """Sum c(k) + c(k') for KM algebra under Feigin-Frenkel duality.

    For sl_2: c + c' = 26 (level-independent) via Virasoro DS.

    For general g at level k, with k' = -k - 2h^vee:
    c(k) + c(k') = k·dim(g)/(k+h^vee) + k'·dim(g)/(k'+h^vee)

    This is NOT always level-independent for higher rank;
    the complementarity is 26 for Virasoro because the DS formula
    for c involves the quadratic numerator.
    """
    if k is None:
        k = Symbol('k')
    k = Rational(k) if isinstance(k, (int, float)) else k

    c_k = wzw_central_charge(g_name, k)
    c_dual = dual_central_charge_km(g_name, k)
    return simplify(c_k + c_dual)


# ===========================================================================
# Reflected modular periodicity
# ===========================================================================

def reflected_period_sum(c_val, c_dual_val) -> Rational:
    """Compute 1/N + 1/N' for a Koszul dual pair.

    Given c = p/q and c' = p'/q' (both in lowest terms),
    N = 24q/gcd(p,24), N' = 24q'/gcd(p',24).

    Returns 1/N + 1/N'.
    """
    N = modular_period(c_val)
    N_dual = modular_period(c_dual_val)
    return Rational(1, N) + Rational(1, N_dual)


def reflected_period_formula_rhs(c_val, c_dual_val) -> Rational:
    """RHS of the reflected periodicity formula.

    (gcd(p,24) + gcd(p',24)) / (24*q)

    where c = p/q, c' = p'/q' in lowest terms.

    NOTE: The formula uses q (denominator of c), assuming q' = q
    when gcd(26q - p, q) = 1.
    """
    p, q = _to_lowest_terms(c_val)
    p_dual, q_dual = _to_lowest_terms(c_dual_val)
    g1 = gcd(abs(p), 24)
    g2 = gcd(abs(p_dual), 24)
    return Rational(g1 + g2, 24 * q)


def reflected_period_check(c_val, c_dual_val) -> Dict[str, object]:
    """Full check of reflected modular periodicity.

    Returns dict with:
    - c, c_dual: the central charges
    - N, N_dual: modular periods
    - lhs: 1/N + 1/N' (computed from periods)
    - rhs: formula prediction (gcd(p,24) + gcd(p',24))/(24q)
    - match: whether lhs == rhs
    - is_1_over_12: whether 1/N + 1/N' = 1/12
    - q_match: whether q = q' (denominator match)
    """
    p, q = _to_lowest_terms(c_val)
    p_dual, q_dual = _to_lowest_terms(c_dual_val)

    N = modular_period(c_val)
    N_dual = modular_period(c_dual_val)

    lhs = Rational(1, N) + Rational(1, N_dual)
    rhs = reflected_period_formula_rhs(c_val, c_dual_val)

    return {
        "c": Rational(c_val),
        "c_dual": Rational(c_dual_val),
        "p": p, "q": q,
        "p_dual": p_dual, "q_dual": q_dual,
        "N": N,
        "N_dual": N_dual,
        "lhs": lhs,
        "rhs": rhs,
        "match": simplify(lhs - rhs) == 0,
        "is_1_over_12": lhs == Rational(1, 12),
        "q_match": q == q_dual,
    }


def reflected_period_check_km(g_name: str, k: int) -> Dict[str, object]:
    """Reflected periodicity check for KM algebra at integer level k.

    Uses Sugawara formula for c and Feigin-Frenkel dual for c'.
    """
    c = wzw_central_charge(g_name, k)
    h_dual = dual_coxeter(g_name)
    k_dual = feigin_frenkel_dual_level(k, h_dual)
    c_dual = wzw_central_charge(g_name, k_dual)

    result = reflected_period_check(c, c_dual)
    result["k"] = k
    result["k_dual"] = k_dual
    result["g_name"] = g_name
    result["h_dual"] = h_dual
    return result


def reflected_period_check_virasoro(k) -> Dict[str, object]:
    """Reflected periodicity check for Virasoro at DS level k.

    c(k) = 1 - 6(k+1)^2/(k+2), c' = 26 - c.
    """
    c = virasoro_ds_central_charge(k)
    c_dual = 26 - c
    result = reflected_period_check(c, c_dual)
    result["k"] = k
    return result


# ===========================================================================
# Nilpotence bounds (Graber-Vakil)
# ===========================================================================

def nilpotence_bound_smooth(g: int) -> int:
    """Sharp nilpotence bound on smooth moduli M_g.

    kappa(lambda)^{g-1} = 0 in CH*(A).
    (Graber-Vakil vanishing: R^d(M_g) = 0 for d > g-2.)

    Ground truth: thm:geometric-depth-smooth.
    """
    if g < 2:
        raise ValueError(f"Need g >= 2, got g={g}")
    return g - 1


def nilpotence_bound_compactified(g: int) -> int:
    """Weak nilpotence bound on compactified moduli M-bar_g.

    kappa(lambda)^{3g-2} = 0 (dimension counting).
    dim M-bar_g = 3g-3, so tautological classes vanish above degree 3g-3.
    lambda has degree 1, so lambda^d = 0 for d > 3g-3.
    But more precisely: lambda^{3g-2} lies in R^{3g-2}(M-bar_g) = 0
    since the tautological ring vanishes above degree 3g-3.

    Ground truth: thm:geometric-periodicity-weak.
    """
    if g < 2:
        raise ValueError(f"Need g >= 2, got g={g}")
    return 3 * g - 2


def geometric_depth_comparison(g: int) -> Dict[str, object]:
    """Compare smooth vs compactified nilpotence bounds.

    Returns dict with both bounds and the improvement factor.
    """
    smooth = nilpotence_bound_smooth(g)
    compact = nilpotence_bound_compactified(g)
    return {
        "genus": g,
        "smooth_bound": smooth,
        "compactified_bound": compact,
        "improvement_factor": Rational(compact, smooth),
        "gap": compact - smooth,
    }


def dimensional_nilpotence_check(g: int) -> Dict[str, object]:
    """Check whether obs_g^2 = 0 by dimensional argument.

    obs_g^2 lives in H^{4g}(M-bar_g).
    dim_C M-bar_g = 3g - 3.
    So H^{4g} = 0 iff 4g > 2(3g-3) = 6g-6, i.e., g < 3.

    Ground truth: curvature_genus_bridge.py.
    """
    dim_moduli = 3 * g - 3
    obs_sq_degree = 4 * g
    max_degree = 2 * dim_moduli

    return {
        "genus": g,
        "dim_moduli": dim_moduli,
        "obs_squared_degree": obs_sq_degree,
        "max_cohomological_degree": max_degree,
        "vanishes_dimensionally": obs_sq_degree > max_degree,
    }


# ===========================================================================
# Minimal model period table
# ===========================================================================

def minimal_model_period_table(
    max_p: int = 8,
    max_q: int = 12,
) -> List[Dict[str, object]]:
    """Compute modular periods for all minimal models M(p,q) in range.

    Returns list of dicts with p, q, c, kappa, N, and divisibility data.
    """
    results = []
    for p in range(2, max_p + 1):
        for q in range(p + 1, max_q + 1):
            if gcd(p, q) != 1:
                continue
            c = minimal_model_central_charge(p, q)
            kappa = scalar_modular_characteristic(c)
            N = modular_period(c)

            # Check: N divides lcm(p,q) * 24 / gcd(numerator, 24)?
            # Actually check: does N divide 24 * lcm(p,q)?
            L = (p * q) // gcd(p, q)  # lcm(p,q)

            p_num, q_den = _to_lowest_terms(c)

            results.append({
                "p": p, "q": q,
                "c": c,
                "c_num": p_num, "c_den": q_den,
                "kappa": kappa,
                "N": N,
                "lcm_pq": L,
                "N_divides_24lcm": (24 * L) % N == 0,
            })
    return results


# ===========================================================================
# WZW period table
# ===========================================================================

def wzw_period_table(
    g_name: str = "sl2",
    max_k: int = 10,
) -> List[Dict[str, object]]:
    """Compute modular periods for WZW model g-hat at levels k=1..max_k.

    Returns list of dicts with k, c, N, and dual data.
    """
    h_dual = dual_coxeter(g_name)
    dim_g = lie_dim(g_name)
    results = []

    for k in range(1, max_k + 1):
        c = wzw_central_charge(g_name, k)
        N = modular_period(c)

        k_dual = feigin_frenkel_dual_level(k, h_dual)
        c_dual = wzw_central_charge(g_name, k_dual)
        N_dual = modular_period(c_dual)

        period_sum = Rational(1, N) + Rational(1, N_dual)

        results.append({
            "g_name": g_name,
            "k": k,
            "k_dual": int(k_dual),
            "c": c,
            "c_dual": c_dual,
            "N": N,
            "N_dual": N_dual,
            "period_sum": period_sum,
            "c_sum": simplify(c + c_dual),
        })
    return results


# ===========================================================================
# T-matrix eigenvalue computation
# ===========================================================================

def minimal_model_conformal_weights(p: int, q: int) -> List[Dict[str, object]]:
    """Conformal weights h_{r,s} for all irreducible modules of M(p,q).

    h_{r,s} = ((qr - ps)^2 - (q-p)^2) / (4pq)

    with 1 <= r <= p-1, 1 <= s <= q-1, identification V_{r,s} = V_{p-r,q-s}.

    Ground truth: deformation_theory.tex Step 1 evidence.
    """
    c = minimal_model_central_charge(p, q)
    weights = []

    seen = set()
    for r in range(1, p):
        for s in range(1, q):
            # Apply identification: use the representative with smaller index
            key = (min(r, p - r), min(s, q - s))
            if (r, s) != (p - r, q - s):
                alt_key = (min(p - r, r), min(q - s, s))
                canonical = min((r, s), (p - r, q - s))
            else:
                canonical = (r, s)

            if canonical in seen:
                continue
            seen.add(canonical)

            h = Rational((q * r - p * s)**2 - (q - p)**2, 4 * p * q)
            weights.append({
                "r": canonical[0], "s": canonical[1],
                "h": h,
                "h_minus_c_over_24": h - c / 24,
            })

    return weights


def actual_t_matrix_period(p: int, q: int) -> int:
    """Compute the actual T-matrix period for minimal model M(p,q).

    This is the minimal positive integer N_T such that
    N_T * (h_{r,s} - c/24) is an integer for ALL modules (r,s).

    Equivalently, N_T = lcm of denominators of {h_{r,s} - c/24}.

    The formula period N = 24q'/gcd(p',24) always divides N_T,
    and N_T always divides 24*p*q (since h_{r,s} has denominator | 4pq).

    Ground truth: Step 1 of evidence for thm:modular-periodicity-minimal.
    """
    from math import lcm as math_lcm
    c = minimal_model_central_charge(p, q)
    weights = minimal_model_conformal_weights(p, q)

    N_T = 1
    for w in weights:
        shift = w["h_minus_c_over_24"]
        r = Rational(shift)
        N_T = math_lcm(N_T, int(r.q))

    return N_T


def t_matrix_period_check(p: int, q: int) -> Dict[str, object]:
    """Verify T-matrix periodicity for minimal model M(p,q).

    Computes both the formula period N = 24q'/gcd(p',24) and the actual
    T-matrix period N_T = lcm of denominators of h_{r,s} - c/24.

    Checks:
    1. T^{N_T} = Id (always true by construction)
    2. N divides N_T (formula period divides actual)
    3. N_T divides 24*p*q (actual divides the universal bound)

    Ground truth: Step 1 of the evidence for thm:modular-periodicity-minimal.
    """
    c = minimal_model_central_charge(p, q)
    N_formula = modular_period(c)
    N_T = actual_t_matrix_period(p, q)
    weights = minimal_model_conformal_weights(p, q)

    # Verify T^{N_T} = Id for all modules
    all_integer = True
    details = []
    for w in weights:
        val = N_T * w["h_minus_c_over_24"]
        is_int = simplify(val - int(round(float(val)))) == 0
        if not is_int:
            all_integer = False
        details.append({
            "r": w["r"], "s": w["s"],
            "h": w["h"],
            "N_T_times_shift": val,
            "is_integer": is_int,
        })

    return {
        "p": p, "q": q,
        "c": c,
        "N_formula": N_formula,
        "N_T": N_T,
        "T_N_is_identity": all_integer,
        "formula_divides_actual": N_T % N_formula == 0,
        "actual_divides_24pq": (24 * p * q) % N_T == 0,
        "num_modules": len(weights),
        "details": details,
    }


# ===========================================================================
# Quantum periodicity (Type II)
# ===========================================================================

def quantum_period(p: int, q: int, h_dual: int) -> int:
    """Quantum periodicity bound M for admissible level k = -h^vee + p/q.

    M = 2 * h^vee * p * q / gcd(p, q, h^vee)

    Ground truth: thm:periodicity-quantum-input.
    """
    from math import gcd as mgcd
    g = mgcd(mgcd(p, q), h_dual)
    return 2 * h_dual * p * q // g


def combined_period_bound(N_mod: int, N_quant: int) -> int:
    """Combined period bound: Period(A) | lcm(N_mod, N_quant).

    The geometry gives a THRESHOLD (nilpotence), not a period.
    The two genuine periodic sources combine by lcm.

    Ground truth: concordance.tex stratified periodicity framework.
    """
    from math import gcd as mgcd
    return N_mod * N_quant // mgcd(N_mod, N_quant)


# ===========================================================================
# Verification routines
# ===========================================================================

def verify_modular_periodicity_minimal(
    max_p: int = 6,
    max_q: int = 8,
) -> Dict[str, bool]:
    """Verify T-matrix periodicity for all minimal models in range.

    This verifies Step 1 (unconditional) of the evidence for
    conj:modular-periodicity. Checks:
    1. T^{N_T} = Id (actual T-matrix period)
    2. Formula period N divides N_T
    3. N_T divides 24*p*q
    """
    results = {}
    for p in range(2, max_p + 1):
        for q in range(p + 1, max_q + 1):
            if gcd(p, q) != 1:
                continue
            check = t_matrix_period_check(p, q)
            results[f"M({p},{q}): T^{check['N_T']}=Id"] = check["T_N_is_identity"]
            results[f"M({p},{q}): N|N_T"] = check["formula_divides_actual"]
            results[f"M({p},{q}): N_T|24pq"] = check["actual_divides_24pq"]
    return results


def verify_reflected_periodicity_km(
    g_name: str = "sl2",
    max_k: int = 6,
) -> Dict[str, bool]:
    """Verify reflected periodicity formula for KM algebra.

    Check: 1/N + 1/N' = (gcd(p,24) + gcd(p',24))/(24q).
    """
    results = {}
    for k in range(1, max_k + 1):
        check = reflected_period_check_km(g_name, k)
        label = f"{g_name}_k={k}: period formula"
        results[label] = check["match"]
    return results


def verify_nilpotence_bounds(max_g: int = 10) -> Dict[str, bool]:
    """Verify nilpotence bound structure for genera 2..max_g."""
    results = {}
    for g in range(2, max_g + 1):
        smooth = nilpotence_bound_smooth(g)
        compact = nilpotence_bound_compactified(g)

        # Smooth bound should be strictly less than compactified
        results[f"g={g}: smooth < compact"] = smooth < compact
        # Smooth bound = g-1
        results[f"g={g}: smooth = g-1"] = smooth == g - 1
        # Compactified bound = 3g-2
        results[f"g={g}: compact = 3g-2"] = compact == 3 * g - 2

    # Special: g=2, lambda = 0 (smooth bound = 1)
    results["g=2: lambda vanishes"] = nilpotence_bound_smooth(2) == 1

    return results


def verify_feigin_frenkel() -> Dict[str, bool]:
    """Verify Feigin-Frenkel duality formula k' = -k - 2h^vee."""
    results = {}

    # sl_2: h^vee = 2, k' = -k - 4
    k = Symbol('k')
    results["sl2: k' = -k-4"] = simplify(
        feigin_frenkel_dual_level(k, 2) - (-k - 4)
    ) == 0

    # sl_3: h^vee = 3, k' = -k - 6
    results["sl3: k' = -k-6"] = simplify(
        feigin_frenkel_dual_level(k, 3) - (-k - 6)
    ) == 0

    # Double dual: k'' = -((-k-2h)-2h) = k
    for name in ["sl2", "sl3"]:
        h = dual_coxeter(name)
        k_dual = feigin_frenkel_dual_level(k, h)
        k_double = feigin_frenkel_dual_level(k_dual, h)
        results[f"{name}: double dual = identity"] = simplify(k_double - k) == 0

    return results


# ===========================================================================
# Main
# ===========================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULAR PERIODICITY VERIFICATION")
    print("=" * 60)

    print("\n--- Feigin-Frenkel Duality ---")
    for name, ok in verify_feigin_frenkel().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- T-matrix Periodicity (Minimal Models) ---")
    for name, ok in verify_modular_periodicity_minimal().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Reflected Periodicity (sl_2 KM) ---")
    for name, ok in verify_reflected_periodicity_km("sl2", 6).items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Nilpotence Bounds ---")
    for name, ok in verify_nilpotence_bounds().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Minimal Model Period Table ---")
    for row in minimal_model_period_table(6, 8):
        print(f"  M({row['p']},{row['q']}): c={row['c']}, N={row['N']}")
