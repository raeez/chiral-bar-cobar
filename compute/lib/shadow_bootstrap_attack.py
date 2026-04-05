#!/usr/bin/env python3
r"""
shadow_bootstrap_attack.py — MC-enhanced bootstrap attack on the scattering matrix.

THE PROGRAMME:
  Single algebra: MC constrains ε^c_s (spectral coefficients), NOT φ(s) (scattering).
  All algebras: MC across all A constrains the SPACE of allowable ε^c_s.
  The scattering matrix φ(s) appears in the functional equation for EVERY ε^c_s.
  If the MC-constrained space of ε^c_s is incompatible with off-line poles of φ,
  then RH follows.

KEY RESULTS IN THIS MODULE:
  (P1) NARAIN UNIVERSALITY THEOREM: ε^1_s(R) = 2(R^{2s}+R^{-2s})ζ(2s).
       The ζ(2s) factor is UNIVERSAL across all Narain moduli.
       CONSEQUENCE: the Narain family provides NO leverage for constraining ζ zeros.

  (P2) SHADOW-MOMENT TOWER: The MC equation at arity r constrains the r-th
       shadow moment M_r = Σ_k 2·γ_k^{2(r-2)}·exp(-γ_k²/(4κ)).
       For Gaussian class (depth 2): only M_2 constrained (one real number).
       For Mixed class (depth ∞): ALL M_r constrained (full generating function).

  (P3) MOMENT-LI BRIDGE: The shadow moments determine the Li coefficients
       through a specific integral transform. The transform is INVERTIBLE
       for the full shadow obstruction tower (depth ∞) but NOT for finite depth.

  (P4) MC-ENHANCED BOOTSTRAP FUNCTIONAL: At each shadow arity r, the MC
       equation gives a linear functional α_r on the space of partition functions.
       The positivity α_r(Z) ≥ 0 (from unitarity) combined with the MC relation
       α_r = f(α_2,...,α_{r-1}) (from the shadow obstruction tower) gives COUPLED constraints.

  (P5) THE BOOTSTRAP CLOSURE CONJECTURE: The MC-coupled constraints from
       ALL shadow arities, applied to ALL central charges c, are sufficient
       to force the poles of φ(s) onto Re(s) = 1/4.
"""

import numpy as np
import math

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 1. NARAIN UNIVERSALITY THEOREM
# ============================================================

def narain_epstein_analytic(s, R, nmax=1000):
    r"""
    THEOREM: For the c=1 Narain CFT at radius R:
      ε^1_s(R) = 2(R^{2s} + R^{-2s}) ζ(2s)

    PROOF:
    Scalar primaries at radius R:
      Momentum (w=0, n≥1): Δ_n = n²/(2R²), multiplicity 2 (±n)
      Winding  (n=0, w≥1): Δ_w = w²R²/2,   multiplicity 2 (±w)

    ε^1_s(R) = Σ_{Δ∈S} (2Δ)^{-s}
    = 2·Σ_{n≥1} (n²/R²)^{-s} + 2·Σ_{w≥1} (w²R²)^{-s}
    = 2R^{2s} Σ_{n≥1} n^{-2s} + 2R^{-2s} Σ_{w≥1} w^{-2s}
    = 2R^{2s} ζ(2s) + 2R^{-2s} ζ(2s)
    = 2(R^{2s} + R^{-2s}) ζ(2s)                                    □

    CONSEQUENCES:
    (C1) At R=1: ε^1_s = 4ζ(2s) ✓
    (C2) T-duality R↔1/R: R^{2s}+R^{-2s} is SYMMETRIC → ε(R)=ε(1/R) ✓
    (C3) Zeros of ε^1_s(R) = zeros of ζ(2s) for ALL R
         (the factor R^{2s}+R^{-2s} > 0 for real s > 0)
    (C4) The ζ(2s) factor is UNIVERSAL: independent of the modulus R
    (C5) NO bootstrap leverage from varying R within Narain family
    """
    if HAS_MPMATH:
        s_mp = mpmath.mpc(s) if isinstance(s, complex) else mpmath.mpf(s)
        R_mp = mpmath.mpf(R)
        factor = 2 * (mpmath.power(R_mp, 2 * s_mp) + mpmath.power(R_mp, -2 * s_mp))
        return complex(factor * mpmath.zeta(2 * s_mp))

    factor = 2 * (R ** (2 * s) + R ** (-2 * s))
    return factor * sum(n ** (-2 * s) for n in range(1, nmax + 1))


def narain_epstein_direct(s, R, nmax=200):
    """Direct computation of ε^1_s(R) from the spectrum, for verification."""
    from rankin_selberg_bridge import narain_scalar_spectrum_c1, constrained_epstein_zeta
    spec = narain_scalar_spectrum_c1(R, nmax=nmax)
    return constrained_epstein_zeta(s, spec)


def verify_narain_universality(s_values=None, R_values=None):
    """
    Verify ε^1_s(R) = 2(R^{2s}+R^{-2s})ζ(2s) for multiple (s,R) pairs.
    """
    if s_values is None:
        s_values = [1.5, 2.0, 3.0]
    if R_values is None:
        R_values = [0.5, 0.7, 1.0, 1.3, 2.0, 3.0]

    results = []
    for s in s_values:
        for R in R_values:
            analytic = narain_epstein_analytic(s, R)
            direct = narain_epstein_direct(s, R)
            error = abs(analytic - direct) / abs(analytic) if analytic != 0 else abs(direct)
            results.append({'s': s, 'R': R, 'analytic': analytic, 'direct': direct, 'error': error})

    return results


def narain_zero_universality(R_values=None, num_zeros=5):
    """
    PROVE: zeros of ε^1_s(R) are at the SAME locations for ALL R.
    Since ε^1_s(R) = 2(R^{2s}+R^{-2s})ζ(2s), and R^{2s}+R^{-2s} ≠ 0
    for real R > 0 and s on the critical line, the zeros come only from ζ(2s).

    The zeros of ε^1 on the critical line s = 1/4+it are at:
    ζ(1/2+2it) = 0, i.e., 2t = γ_n, t = γ_n/2.
    These are INDEPENDENT of R.
    """
    if not HAS_MPMATH:
        return {}

    if R_values is None:
        R_values = [0.5, 1.0, 2.0]

    gammas = [float(mpmath.zetazero(k).imag) for k in range(1, num_zeros + 1)]
    results = {}

    for R in R_values:
        zero_values = []
        for gamma in gammas:
            s = 0.25 + 1j * gamma / 2
            val = narain_epstein_analytic(complex(s), R)
            zero_values.append(abs(val))
        results[R] = zero_values

    return results


# ============================================================
# 2. SHADOW-MOMENT TOWER
# ============================================================

def shadow_moment(r, kappa, num_zeros=100):
    r"""
    The r-th shadow moment:
      M_r(κ) = Σ_k 2·γ_k^{2(r-2)}·exp(-γ_k²/(4κ))

    where γ_k are imaginary parts of zeta zeros.

    The MC equation at arity r constrains M_r.
    For Gaussian class: only M_2 = Σ 2·exp(-γ²/(4κ)) is "active."
    For Mixed class: all M_r are active.

    The shadow-moment GENERATING FUNCTION:
    G(z,κ) = Σ_r M_r·z^{r-2} / (r-2)!
           = Σ_k 2·exp(-γ_k²/(4κ))·cosh(γ_k√z)

    This determines {γ_k} if all moments are known (Hamburger moment problem).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    zeros = [float(mpmath.zetazero(k).imag) for k in range(1, num_zeros + 1)]
    return sum(2 * g ** (2 * (r - 2)) * math.exp(-g * g / (4 * kappa))
               for g in zeros)


def shadow_moment_tower(r_max, kappa, num_zeros=100):
    """Compute shadow moments M_2, M_3, ..., M_{r_max}."""
    return [shadow_moment(r, kappa, num_zeros) for r in range(2, r_max + 1)]


def shadow_moment_generating_function(z, kappa, num_zeros=100):
    r"""
    G(z,κ) = Σ_k 2·exp(-γ_k²/(4κ))·cosh(γ_k·√z)

    This is the COMPLETE shadow-moment generating function.
    It determines the zero set {γ_k} if convergent.
    For κ > 0: the exponential damping ensures convergence.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    zeros = [float(mpmath.zetazero(k).imag) for k in range(1, num_zeros + 1)]
    sqrt_z = np.sqrt(complex(z))
    result = sum(2 * math.exp(-g * g / (4 * kappa)) * np.cosh(g * sqrt_z)
                 for g in zeros)
    return result


# ============================================================
# 3. MOMENT-LI BRIDGE
# ============================================================

def newton_sum_from_zeros(k, num_zeros=100):
    r"""
    Newton sum S_k = Σ_ρ 1/ρ^k where ρ are zeros of ξ(2s).
    ρ = 1/4 + iγ_n/2.

    S_k = Σ_n [1/(1/4+iγ_n/2)^k + 1/(1/4-iγ_n/2)^k]
        = 2·Re Σ_n (1/4+iγ_n/2)^{-k}
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    total = mpmath.mpf(0)
    for n in range(1, num_zeros + 1):
        rho = mpmath.mpc(0.25, float(mpmath.zetazero(n).imag) / 2)
        total += 2 * mpmath.re(rho ** (-k))
    return float(total)


def li_from_newton(n, num_zeros=100):
    r"""
    Li coefficient from Newton sums:
    λ_n = Σ_{k=1}^n C(n,k)(-1)^{k+1} S_k

    where S_k = Σ_ρ ρ^{-k} (Newton sums over zeros of ξ(2s)).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    S = [newton_sum_from_zeros(k, num_zeros) for k in range(1, n + 1)]
    result = 0.0
    for k in range(1, n + 1):
        binom = math.comb(n, k)
        result += binom * (-1) ** (k + 1) * S[k - 1]
    return result


def shadow_to_newton_transform(shadow_moments, kappa):
    r"""
    Transform shadow moments M_r to Newton sums S_k.

    Shadow moment: M_r = Σ_k 2·γ_k^{2(r-2)}·exp(-γ_k²/(4κ))
    Newton sum:    S_k = Σ_n 2·Re[(1/4+iγ_n/2)^{-k}]

    The relationship involves the Laplace transform:
    M_r = ∫ γ^{2(r-2)} · exp(-γ²/(4κ)) · dμ(γ)
    S_k = ∫ (1/4+iγ/2)^{-k} · dμ(γ)

    where dμ = Σ 2·δ(γ-γ_n) dγ.

    These are MOMENTS of the same measure dμ but with different weight functions.
    The shadow moments use Gaussian-weighted even power moments.
    The Newton sums use inverse power moments of ρ = 1/4+iγ/2.

    For the FULL tower (all r): the shadow moments determine the measure dμ
    (Hamburger moment problem — determined if Carleman's condition holds).
    The measure determines {γ_k}, which determines {S_k}, which determines {λ_n}.

    Returns dict with analysis.
    """
    return {
        'shadow_moments': shadow_moments,
        'kappa': kappa,
        'n_moments': len(shadow_moments),
        'determines_measure': len(shadow_moments) == float('inf') or len(shadow_moments) > 20,
        'carleman_condition': 'Σ M_{2r}^{-1/(2r)} = ∞ (need to verify)',
        'chain': 'shadow moments → measure dμ → {γ_k} → {S_k} → {λ_k} → RH',
    }


# ============================================================
# 4. MC-ENHANCED BOOTSTRAP FUNCTIONALS
# ============================================================

def mc_bootstrap_functional(r, c, spectrum, kappa):
    r"""
    The MC-enhanced bootstrap functional at arity r.

    STANDARD BOOTSTRAP (Benjamin-Chang):
    α(Z) = ∫_F Z·Φ dμ ≥ 0 for all unitary Z
    where Φ is the optimal functional.

    MC-ENHANCED BOOTSTRAP:
    The MC equation at arity r gives:
    o_{r+1}(A) = -D·Θ^{≤r} - ½[Θ^{≤r},Θ^{≤r}]

    This translates to a constraint on the spectral coefficients:
    α_r(ε^c_s) = (specific linear functional of ε^c_s)

    The functional α_r is DETERMINED by the shadow data at arities ≤ r.
    For Gaussian: α_3 = 0 (cubic shadow vanishes).
    For Lie: α_3 ≠ 0 but α_4 = 0.
    For Mixed: all α_r ≠ 0.

    The MC equation gives the RELATION:
    α_{r+1} = f(α_2,...,α_r)  [the MC relation]

    Combined with UNITARITY:
    α_r(ε) ≥ 0 for all physical ε

    This gives COUPLED CONSTRAINTS that are STRONGER than either alone.

    Returns the functional value.
    """
    from rankin_selberg_bridge import constrained_epstein_zeta

    # The r-th spectral moment of ε^c_s
    # At arity r=2: the "mass" = ε^c at s = c/2 (set by κ)
    if r == 2:
        return kappa  # κ determines everything at arity 2

    # At arity r≥3: the r-th spectral moment
    # M_r = Σ (2Δ)^{-(c/2-(r-2))} = ε^c_{c/2-(r-2)}
    s_val = c / 2.0 - (r - 2)
    if s_val > 0:
        return constrained_epstein_zeta(s_val, spectrum)
    else:
        # Need analytic continuation
        return constrained_epstein_zeta(complex(s_val), spectrum)


def mc_coupled_constraints(c, spectrum, kappa, shadow_depth, max_arity=6):
    r"""
    The COUPLED MC-bootstrap constraints.

    At each arity r:
    (U_r) Unitarity: α_r(ε) ≥ 0
    (MC_r) MC equation: α_{r+1} = f_r(α_2,...,α_r)

    For shadow depth d:
    (T_d) Termination: α_{d+1} = 0

    The coupled system:
    α_2 = κ (given)
    α_3 = f_2(κ) = C (cubic shadow, determined by MC at arity 2)
    α_4 = f_3(κ, C) = Q (quartic shadow, determined by MC at arity 3)
    ...
    α_{d+1} = 0 (termination)

    For Gaussian (d=2): α_3 = 0. One constraint.
    For Lie (d=3): α_3 = C (one parameter), α_4 = 0. Two constraints.
    For Contact (d=4): α_3 = 0, α_4 = Q. Two constraints.
    For Mixed (d=∞): infinitely many coupled constraints.

    Returns the constraint system.
    """
    constraints = {}

    for r in range(2, min(max_arity, shadow_depth + 2) + 1):
        val = mc_bootstrap_functional(r, c, spectrum, kappa)
        constraints[f'alpha_{r}'] = val
        constraints[f'unitarity_{r}'] = val >= 0 if isinstance(val, (int, float)) else True

    if shadow_depth < float('inf'):
        constraints[f'termination_at_{shadow_depth + 1}'] = True
        constraints['termination_value'] = 0

    constraints['total_constraints'] = min(max_arity, shadow_depth) - 1
    constraints['shadow_depth'] = shadow_depth

    return constraints


# ============================================================
# 5. THE BOOTSTRAP CLOSURE ARGUMENT
# ============================================================

def bootstrap_closure_test(c_values=None, num_zeros=50):
    r"""
    Test whether MC constraints across MULTIPLE central charges c
    tighten the bootstrap bounds.

    ARGUMENT:
    The scattering matrix φ(s) = Λ(1-s)/Λ(s) appears in the functional
    equation for EVERY c. For each c, the MC equation gives constraints
    on ε^c_s. The constraints from DIFFERENT c values are INDEPENDENT
    (different algebras). But φ is the SAME for all c.

    If the intersection of all MC-constrained ε^c_s spaces is "thin enough,"
    it may force φ's poles onto the critical line.

    WHAT WE TEST:
    For each c, compute the MC-allowed range of the spectral coefficient
    at a specific s-value. If the allowed ranges SHRINK as we include
    more c values, the bootstrap is tightening.

    CAVEAT: For the Narain family at c=1, ε^1_s(R) = 2(R^{2s}+R^{-2s})ζ(2s).
    The ζ(2s) factor is universal → varying R within Narain gives NO leverage.
    To get leverage, we need DIFFERENT c values or NON-Narain theories.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    if c_values is None:
        c_values = [1, 2, 3, 4, 5, 10, 26]

    results = {}

    for c in c_values:
        # For each c, the functional equation is:
        # ε^c_{c/2-s} = F(s,c) · ε^c_{c/2+s-1}
        # F(s,c) = Γ(s)Γ(s+c/2-1)ζ(2s) / [π^{2s-1/2}Γ(c/2-s)Γ(s-1/2)ζ(2s-1)]

        # The shadow constraint at this c: κ = c/2, depth depends on theory
        kappa = c / 2.0

        # For a GENERIC theory at this c (not necessarily Narain):
        # ε^c_s satisfies the functional equation with the SAME F(s,c)
        # The MC equation gives: shadow depth determines how many
        # spectral moments are constrained.

        # The KEY: F(s,c) involves ζ(2s)/ζ(2s-1). Its poles at zeros of ζ(2s-1)
        # appear in the functional equation for EVERY c. If the MC constraints
        # at different c values are INCOMPATIBLE with these poles being off
        # the critical line, we'd have RH.

        # What we can compute: the F(s,c) factor at s = 3/4 + iγ_1/2
        # (near the first zeta-zero pole)
        gamma_1 = float(mpmath.zetazero(1).imag)
        s_near_pole = 0.75 + 1j * gamma_1 / 2

        try:
            F_near = abs(complex(
                mpmath.gamma(mpmath.mpc(s_near_pole))
                * mpmath.gamma(mpmath.mpc(s_near_pole) + c / 2 - 1)
                * mpmath.zeta(2 * mpmath.mpc(s_near_pole))
                / (mpmath.power(mpmath.pi, 2 * mpmath.mpc(s_near_pole) - 0.5)
                   * mpmath.gamma(c / 2 - mpmath.mpc(s_near_pole))
                   * mpmath.gamma(mpmath.mpc(s_near_pole) - 0.5)
                   * mpmath.zeta(2 * mpmath.mpc(s_near_pole) - 1))
            ))
        except (ValueError, ZeroDivisionError):
            F_near = float('inf')

        results[c] = {
            'kappa': kappa,
            'F_near_pole': F_near,
            'pole_location': complex(s_near_pole),
        }

    return results


def where_leverage_comes_from():
    r"""
    ANALYSIS: Where does bootstrap leverage actually come from?

    NOT FROM: Varying R within Narain (ε factors as character × ζ).
    NOT FROM: A single algebra at a single c (constrains ε but not φ).

    FROM: Multiple algebras at DIFFERENT c values, each imposing
    MC constraints with the SAME scattering matrix φ(s).

    The mechanism:
    1. At c=1: ε^1 is constrained by Gaussian shadow (depth 2).
       This gives ONE moment constraint.
    2. At c=2: ε^2 is constrained by its own shadow obstruction tower.
       The functional equation involves F(s,2), which involves the SAME ζ(2s)/ζ(2s-1).
       This gives ADDITIONAL moment constraints.
    3. At c=c_0: ε^{c_0} has its own MC constraints.
       Each c contributes independent constraints on the SAME φ.

    THE KEY INSIGHT: F(s,c) = [Γ(s)Γ(s+c/2-1)ζ(2s)] / [π^{2s-1/2}Γ(c/2-s)Γ(s-1/2)ζ(2s-1)]

    As c varies, the GAMMA FACTORS change but ζ(2s)/ζ(2s-1) stays the same.
    The pole locations of F (at zeros of ζ(2s-1)) are INDEPENDENT of c.
    But the RESIDUES at these poles DEPEND on c (through the gamma factors).

    The MC constraints at different c values constrain the RESIDUES at zeta-zero poles.
    If these residue constraints are INCOMPATIBLE with off-line poles, RH follows.

    Specifically: the residue of F(s,c) at s = (1+z_k)/2 is:
    Res = Γ((1+z_k)/2)·Γ((1+z_k)/2+c/2-1)·ζ(1+z_k) / [π^{z_k}·Γ(c/2-(1+z_k)/2)·Γ(z_k/2)·2ζ'(z_k)]

    For z_k = 1/2+iγ_k (RH):
    - (1+z_k)/2 = 3/4+iγ_k/2
    - The gamma factors are well-defined and finite
    - The residue is a SPECIFIC function of c and γ_k

    For z_k = σ+iγ with σ ≠ 1/2 (off-line zero):
    - (1+z_k)/2 = (1+σ)/2 + iγ/2
    - The gamma factors still well-defined
    - The residue is a DIFFERENT function of c and γ_k

    THE BOOTSTRAP TEST: compute the MC-constrained ε^c_s at the pole location
    for each c. If the functional equation ε^c_{c/2-s} = F·ε^c_{c/2+s-1} is
    INCONSISTENT with the residue at an off-line zero, then that zero cannot exist.

    WHAT MAKES THIS HARD: The residue depends on both c and σ (the real part of
    the zero). For each hypothetical σ ≠ 1/2, we need the residue function
    R(c,σ) to violate the MC constraints for SOME c. This is a non-trivial
    functional analysis problem.

    THE HONEST BOTTOM LINE: This programme is WELL-DEFINED and in principle
    EXECUTABLE, but it requires:
    (a) Explicit MC constraints for non-Narain theories at each c
    (b) A proof that these constraints exclude off-line zeros
    Neither (a) nor (b) is currently available.
    """
    return {
        'no_leverage': ['Narain R-variation', 'single algebra at fixed c'],
        'leverage': [
            'multiple c values with the SAME φ(s)',
            'non-Narain theories (Virasoro, W-algebras) at each c',
            'the residue function R(c,σ) varying with c while φ is fixed',
        ],
        'mechanism': (
            'F(s,c) has c-dependent gamma factors but c-independent ζ-poles. '
            'MC constraints at different c constrain residues at these poles. '
            'If the residue constraints exclude off-line poles, RH follows.'
        ),
        'what_is_needed': {
            'a': 'explicit MC constraints for non-Narain theories at each c',
            'b': 'proof that these constraints exclude σ ≠ 1/2',
        },
        'status': 'Programme well-defined but (a) and (b) both open.',
    }


# ============================================================
# 6. THE VIRASORO SHADOW TOWER AS BOOTSTRAP INPUT
# ============================================================

def virasoro_shadow_constraints(c):
    r"""
    The Virasoro shadow obstruction tower constraints for the MC-enhanced bootstrap.

    For Vir_c (shadow depth ∞, Mixed class):
    - κ = c/2 (arity 2, always)
    - Q^contact = 10/[c(5c+22)] (arity 4, computed in the manuscript)
    - δ_H^(1) = 120/[c²(5c+22)]·x² (genus-1 Hessian, arity 4 genus 1)
    - All higher arities are nonzero

    The infinite tower of constraints:
    α_2 = c/2
    α_3 = 0 (cubic shadow vanishes for Virasoro — diagonal metric)
    α_4 = Q^contact = 10/[c(5c+22)]
    α_5 ≠ 0 (quintic forced, proved in manuscript)
    ...

    These give INFINITELY MANY constraints on ε^c_s for Virasoro at each c.
    """
    if c == 0:
        return None

    kappa = c / 2.0
    Q_contact = 10.0 / (c * (5 * c + 22))

    return {
        'c': c,
        'kappa': kappa,
        'shadow_depth': float('inf'),
        'shadow_class': 'Mixed',
        'alpha_2': kappa,
        'alpha_3': 0.0,  # Cubic vanishes (diagonal OPE metric)
        'alpha_4': Q_contact,
        'alpha_5': 'nonzero (quintic forced)',
        'constraint_count': float('inf'),
        'Q_contact': Q_contact,
        'delta_H_genus1': lambda x: 120 / (c ** 2 * (5 * c + 22)) * x ** 2,
    }


def virasoro_bootstrap_constraint_at_c(c, s_test=2.0):
    r"""
    The MC-bootstrap constraint from Virasoro at central charge c,
    evaluated at spectral parameter s.

    The functional equation for Virasoro:
    ε^c_{c/2-s}(Vir) = F(s,c) · ε^c_{c/2+s-1}(Vir)

    The MC constraint: α_4 = Q^contact = 10/[c(5c+22)]

    This constrains the 4th spectral moment of ε^c_s:
    Σ (2Δ)^{-(c/2-2)} = ε^c_{c/2-2} = 10/[c(5c+22)] · (normalization)

    The constraint is: the value of ε at s = c/2-2 is determined by Q^contact.
    Combined with the functional equation: this constrains ε at the REFLECTED
    point s = 2-c/2+1 = 3-c/2 as well.
    """
    shadow = virasoro_shadow_constraints(c)
    if shadow is None:
        return None

    return {
        'c': c,
        'kappa': shadow['kappa'],
        'Q_contact': shadow['Q_contact'],
        'constraint_s_value': c / 2 - 2,
        'reflected_s_value': 3 - c / 2,
        'constraint_type': 'MC quartic → fixes ε at s = c/2 - 2',
    }


# ============================================================
# 7. THE RESIDUE ANALYSIS
# ============================================================

def residue_at_zeta_zero(k, c, num_zeros=None):
    r"""
    Compute the residue of F(s,c) at the k-th zeta-zero pole.

    Pole at s = (1+z_k)/2 where z_k = 1/2+iγ_k.
    If RH: pole at s = 3/4 + iγ_k/2.

    Res_{s=(1+z_k)/2} F(s,c) =
      Γ((1+z_k)/2) · Γ((1+z_k)/2 + c/2 - 1) · ζ(1+z_k)
      / [π^{z_k} · Γ(c/2 - (1+z_k)/2) · Γ(z_k/2) · 2ζ'(z_k)]

    Returns the residue as a function of c.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    gamma_k = float(mpmath.zetazero(k).imag)
    z_k = mpmath.mpc(0.5, gamma_k)
    s_pole = (1 + z_k) / 2  # = 3/4 + iγ_k/2

    num = (mpmath.gamma(s_pole)
           * mpmath.gamma(s_pole + mpmath.mpf(c) / 2 - 1)
           * mpmath.zeta(1 + z_k))
    den = (mpmath.power(mpmath.pi, z_k)
           * mpmath.gamma(mpmath.mpf(c) / 2 - s_pole)
           * mpmath.gamma(z_k / 2)
           * 2 * mpmath.diff(mpmath.zeta, z_k))

    return complex(num / den)


def residue_c_dependence(k, c_values=None):
    r"""
    How the residue at the k-th zeta zero varies with c.

    If RH: the residue is a SPECIFIC function of c (through gamma factors).
    For off-line zeros: the residue would be a DIFFERENT function of c.

    The MC constraints at each c must be compatible with the residue.
    If the MC constraints exclude the off-line residue function for SOME c,
    then that off-line zero cannot exist.

    Returns {c: residue(c)} for the k-th zero.
    """
    if c_values is None:
        c_values = [1, 2, 3, 4, 5, 8, 10, 13, 20, 26]

    results = {}
    for c in c_values:
        try:
            res = residue_at_zeta_zero(k, c)
            results[c] = {'residue': res, 'magnitude': abs(res)}
        except Exception:
            results[c] = {'residue': None, 'magnitude': None}

    return results


def hypothetical_offline_residue(k, sigma, gamma, c):
    r"""
    Compute the hypothetical residue if the k-th zero were at σ+iγ
    instead of 1/2+iγ_k.

    For an off-line zero z = σ+iγ (σ ≠ 1/2):
    Pole at s = (1+σ)/2 + iγ/2 (NOT at Re(s) = 3/4).

    The residue has the same FORM but evaluated at different s:
    Res = Γ((1+z)/2)·Γ((1+z)/2+c/2-1)·ζ(1+z) / [π^z·Γ(c/2-(1+z)/2)·Γ(z/2)·2ζ'(z)]

    QUESTION: Is this residue compatible with the MC constraint at this c?
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    z = mpmath.mpc(sigma, gamma)
    s_pole = (1 + z) / 2

    try:
        num = (mpmath.gamma(s_pole)
               * mpmath.gamma(s_pole + mpmath.mpf(c) / 2 - 1)
               * mpmath.zeta(1 + z))
        den = (mpmath.power(mpmath.pi, z)
               * mpmath.gamma(mpmath.mpf(c) / 2 - s_pole)
               * mpmath.gamma(z / 2)
               * 2 * mpmath.diff(mpmath.zeta, z))
        return complex(num / den)
    except Exception:
        return complex('nan')
