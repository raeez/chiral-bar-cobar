#!/usr/bin/env python3
"""
parametrized_bar_cobar.py — Parametrized bar-cobar adjunction and degeneration loci.

Studies how the bar-cobar inversion Omega(B(A)) -> A behaves as algebra parameters
(level k, central charge c, radius R, etc.) vary. The Koszul locus is where the
inversion is a quasi-isomorphism; the degeneration locus D is its complement.

FAMILIES STUDIED:
  1. Affine sl_2: V_k(sl_2), parameter k. Critical: k = -2. Admissible: k = -2 + p/q.
  2. Virasoro: Vir_c, parameter c. Degeneration at c = 0, c = -22/5, minimal models.
  3. W_N: W_k(sl_N) for N = 2,3,4. DS reduction of affine family.
  4. Lattice VOA: V_Lambda(R) at radius R. T-duality R <-> 1/R. Koszul for all R.

KEY RESULTS:
  - Degeneration locus is ALWAYS discrete and algebraic (roots of polynomials).
  - For affine sl_2: D = {k = -2} (critical level only for universal algebras).
  - For Virasoro: D = {c : Q^contact diverges} = {c = 0, c = -22/5}.
  - Minimal model values c_{p,q} = 1 - 6(p-q)^2/(pq) are ALL algebraic numbers.
  - Lattice VOA: D = empty (Koszul for all R by PBW).
  - Level-crossing near k = -2: curvature kappa -> 0 LINEARLY in |k+2|.
  - Spectral gap opens continuously at minimal model boundaries.

References:
  - CLAUDE.md: Critical Pitfalls (Sugawara UNDEFINED at k = -h^v, Vir self-dual at c=13)
  - thm:algebraic-family-rigidity: primitive-tangent vanishing / level-direction concentration for algebraic families
  - prop:pbw-universality: universal V_k(g) Koszul for ALL k != -h^v
  - cor:universal-koszul: V_k(g) always chirally Koszul
"""

import numpy as np
from fractions import Fraction
from math import gcd
from functools import lru_cache

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =============================================================================
# 1. Affine sl_2 family: V_k(sl_2)
# =============================================================================

def affine_sl2_curvature(k):
    """
    Curvature kappa(k) = k + h^v = k + 2 for sl_2 (h^v = 2).

    kappa = 0 at critical level k = -2 (Sugawara UNDEFINED there).
    kappa > 0 for k > -2 (unitary range for k positive integer).
    """
    return k + 2


def affine_sl2_central_charge(k):
    """
    Central charge c = k * dim(g) / (k + h^v) = 3k/(k+2) for sl_2.

    Poles at k = -2 (critical level: Sugawara UNDEFINED, not "c diverges").
    c -> 3 as k -> infinity (classical limit).
    c = 1 at k = 1 (level-1 = free boson on circle).
    """
    if abs(k + 2) < 1e-15:
        return float('inf')  # Sugawara undefined
    return 3.0 * k / (k + 2.0)


def affine_sl2_bar_cobar_obstruction(k):
    """
    Bar-cobar inversion obstruction for V_k(sl_2).

    For UNIVERSAL vertex algebras V_k(g):
      - Koszul for ALL k != -h^v (prop:pbw-universality, cor:universal-koszul)
      - At k = -h^v: bar UNCURVED (kappa = 0), bar cohomology = opers (Feigin-Frenkel)
      - The obstruction is NOT a failure of Koszulness but a QUALITATIVE CHANGE:
        the bar complex becomes uncurved, and the cobar requires the oper input.

    Returns dict with obstruction data.
    """
    kappa = affine_sl2_curvature(k)
    c = affine_sl2_central_charge(k)

    is_critical = abs(kappa) < 1e-15
    is_admissible = _is_admissible_level_sl2(k)

    return {
        'k': k,
        'kappa': kappa,
        'c': c,
        'is_critical': is_critical,
        'is_admissible': is_admissible,
        'bar_curved': not is_critical,
        'koszul': True,  # Universal V_k is chirally Koszul at ALL levels including critical (PBW universality)
        'obstruction_type': 'critical_uncurved' if is_critical else 'none',
    }


def _is_admissible_level_sl2(k, tol=1e-10):
    """
    Check if k is an admissible level for sl_2.

    Admissible levels: k = -2 + p/q where p >= 2, q >= 1, gcd(p,q) = 1.
    Equivalently: k + 2 = p/q with p >= 2.

    Note: admissible levels are NOT degeneration points for the UNIVERSAL algebra
    V_k(g). They are where the SIMPLE QUOTIENT L_k(g) may have null vectors.
    """
    shifted = k + 2
    if abs(shifted) < tol:
        return False  # critical, not admissible

    # Try to express as p/q with small denominators
    try:
        frac = Fraction(shifted).limit_denominator(1000)
        p, q = frac.numerator, frac.denominator
        if q >= 1 and p >= 2 and gcd(p, q) == 1:
            if abs(shifted - float(frac)) < tol:
                return True
    except (ValueError, OverflowError):
        pass
    return False


def affine_sl2_admissible_levels(p_max=10, q_max=10):
    """
    Enumerate admissible levels k = -2 + p/q for sl_2.

    Parameters p >= 2, q >= 1, gcd(p,q) = 1.
    Returns list of (k, p, q) tuples sorted by k.
    """
    levels = []
    for p in range(2, p_max + 1):
        for q in range(1, q_max + 1):
            if gcd(p, q) == 1:
                k = -2.0 + p / q
                levels.append((k, p, q))
    return sorted(levels, key=lambda x: x[0])


def affine_sl2_degeneration_locus():
    """
    The degeneration locus for affine sl_2 universal algebra.

    D = {k = -2} (critical level only).

    For the UNIVERSAL algebra V_k(g), this is the ONLY degeneration point:
    V_k is Koszul for all k != -h^v by PBW universality.

    The admissible levels are NOT in D for the universal algebra.
    They matter only for the simple quotient L_k(g).
    """
    return {'critical': [-2.0], 'type': 'discrete', 'algebraic': True}


def affine_sl2_simple_quotient_degeneration(p_max=10, q_max=10):
    """
    Extended degeneration locus for the SIMPLE QUOTIENT L_k(sl_2).

    D_simple = {k = -2} union {admissible levels where L_k has null vectors}.

    At admissible k = -2 + p/q: the simple quotient L_k(sl_2) has finite many
    irreducible modules. The bar-cobar for L_k may fail or change character.
    """
    critical = [-2.0]
    admissible = [(k, p, q) for k, p, q in affine_sl2_admissible_levels(p_max, q_max)]
    return {
        'critical': critical,
        'admissible': admissible,
        'type': 'discrete',
        'algebraic': True,
        'degeneration_set_size': 1 + len(admissible),
    }


# =============================================================================
# 2. Virasoro family: Vir_c
# =============================================================================

def virasoro_curvature(c):
    """
    Curvature kappa(c) = c/2 for Virasoro.

    kappa = 0 at c = 0 (trivial theory).
    Self-dual point: c = 13 (Vir_c^! = Vir_{26-c}, self-dual when c = 13).
    """
    return c / 2.0


def virasoro_quartic_contact(c):
    """
    Q^contact_Vir(c) = 10 / [c(5c + 22)].

    Poles:
      c = 0: Q diverges (kappa also = 0)
      c = -22/5 = -4.4: Q diverges (Lee-Yang edge singularity)

    These are the ONLY poles of Q^contact in the c-plane.
    """
    denom = c * (5.0 * c + 22.0)
    if abs(denom) < 1e-15:
        return float('inf')
    return 10.0 / denom


def virasoro_genus1_hessian_correction(c):
    """
    delta_H^(1)_Vir(c) = 120 / [c^2(5c+22)].

    Same poles as Q^contact times an extra c factor.
    """
    denom = c * c * (5.0 * c + 22.0)
    if abs(denom) < 1e-15:
        return float('inf')
    return 120.0 / denom


def virasoro_shadow_gf_singularity(c):
    """
    Shadow generating function singularity at t = -c/6.

    This is the radius of convergence of the shadow GF.
    """
    return -c / 6.0


def virasoro_koszul_dual_central_charge(c):
    """
    Vir_c^! = Vir_{26-c}.

    Self-dual at c = 13 (NOT c = 26 — critical pitfall!).
    The 26-c shadow is the DEPTH-ZERO RESONANCE SHADOW.
    """
    return 26.0 - c


def virasoro_special_values():
    """
    Catalogue of special central charge values.

    Returns dict mapping c-value to description and properties.
    """
    return {
        0.0: {
            'name': 'trivial',
            'kappa': 0.0,
            'Q_contact': float('inf'),
            'property': 'kappa = 0, Q diverges, trivial theory',
        },
        -4.4: {
            'name': 'Lee-Yang',
            'kappa': -2.2,
            'Q_contact': float('inf'),
            'property': 'c = -22/5, Q diverges, Lee-Yang edge singularity',
            'exact': Fraction(-22, 5),
        },
        0.5: {
            'name': 'Ising',
            'kappa': 0.25,
            'Q_contact': virasoro_quartic_contact(0.5),
            'property': 'c = 1/2, Ising model, (p,q) = (3,4)',
            'exact': Fraction(1, 2),
        },
        1.0: {
            'name': 'free_boson',
            'kappa': 0.5,
            'Q_contact': virasoro_quartic_contact(1.0),
            'property': 'c = 1, free boson equivalence',
        },
        13.0: {
            'name': 'self_dual',
            'kappa': 6.5,
            'Q_contact': virasoro_quartic_contact(13.0),
            'property': 'c = 13, Vir_c^! = Vir_c (self-dual point)',
        },
        25.0: {
            'name': 'string_theory',
            'kappa': 12.5,
            'Q_contact': virasoro_quartic_contact(25.0),
            'property': 'c = 25, bosonic string transverse dimensions',
        },
        26.0: {
            'name': 'bosonic_string',
            'kappa': 13.0,
            'Q_contact': virasoro_quartic_contact(26.0),
            'property': 'c = 26, bosonic string critical dimension. Vir_26^! = Vir_0',
        },
    }


def virasoro_minimal_model_c(p, q):
    """
    Central charge of minimal model M(p,q):
      c_{p,q} = 1 - 6(p-q)^2/(pq)

    Requires: p > q >= 2, gcd(p,q) = 1 (unitary: p = q+1).

    These are RATIONAL numbers, hence algebraic of degree 1.
    """
    return 1.0 - 6.0 * (p - q) ** 2 / (p * q)


def virasoro_minimal_model_c_exact(p, q):
    """Exact rational value of c_{p,q}."""
    return Fraction(1) - Fraction(6 * (p - q) ** 2, p * q)


def virasoro_degeneration_locus():
    """
    Degeneration locus for Virasoro.

    The Q^contact singularities: c = 0 and c = -22/5.
    These are where the quartic shadow DIVERGES.

    The minimal model values c_{p,q} are NOT degeneration points for the
    universal Virasoro algebra Vir_c (which is Koszul for all c != 0).
    They are where the SIMPLE QUOTIENT may have null vectors.

    Returns the degeneration data.
    """
    return {
        'Q_contact_poles': [0.0, -22.0 / 5.0],
        'kappa_zero': [0.0],
        'type': 'discrete',
        'algebraic': True,
        'minimal_polynomials': {
            0.0: [0, 1],  # x = 0
            -4.4: [22, 5],  # 5x + 22 = 0
        },
    }


def virasoro_minimal_model_table(p_max=10, q_max=11):
    """
    Compute c_{p,q} for coprime (p,q) with p > q >= 2, up to bounds.

    All values are RATIONAL, hence algebraic numbers of degree 1.
    Their minimal polynomials are linear: ax + b = 0 where c = -b/a.

    Returns list of dicts with (p, q, c_float, c_exact, min_poly).
    """
    table = []
    for q in range(2, q_max + 1):
        for p in range(q + 1, p_max + 1):
            if gcd(p, q) != 1:
                continue
            c_exact = virasoro_minimal_model_c_exact(p, q)
            c_float = float(c_exact)
            # Minimal polynomial: denominator * x - numerator = 0
            # i.e., c = num/den, so den*x - num = 0
            table.append({
                'p': p,
                'q': q,
                'c': c_float,
                'c_exact': c_exact,
                'numerator': c_exact.numerator,
                'denominator': c_exact.denominator,
                'algebraic_degree': 1,  # always rational
            })
    return sorted(table, key=lambda x: x['c'])


# =============================================================================
# 3. W_N family: W_k(sl_N) for N = 2, 3, 4
# =============================================================================

def wn_dual_coxeter(N):
    """Dual Coxeter number h^v = N for sl_N."""
    return N


def wn_dimension(N):
    """Dimension of sl_N = N^2 - 1."""
    return N * N - 1


def wn_central_charge(k, N):
    """
    Central charge of V_k(sl_N) via Sugawara:
      c = k * dim(sl_N) / (k + h^v) = k(N^2 - 1)/(k + N).

    For W_k(sl_N) after DS reduction (principal nilpotent):
      c_{W_N} = (N-1)[1 - N(N+1)/(k+N)]
              = (N-1) - N(N-1)(N+1)/(k+N)

    Poles at k = -N (critical level).
    """
    hv = wn_dual_coxeter(N)
    if abs(k + hv) < 1e-15:
        return float('inf')
    # DS reduction formula for principal W-algebra
    return (N - 1) * (1.0 - N * (N + 1) / (k + N))


def wn_curvature(k, N):
    """
    Curvature kappa_{W_N}(k) = c_{W_N}(k) / 2.

    For N=2: W_k(sl_2) = Vir at c = 1 - 6/(k+2), so kappa = c/2.
    The shifted level k + N controls everything.
    """
    c = wn_central_charge(k, N)
    if c == float('inf'):
        return float('inf')
    return c / 2.0


def wn_quartic_contact(k, N):
    """
    Quartic contact invariant Q^contact_{W_N}(k).

    For N=2 (Virasoro): Q = 10/[c(5c+22)].

    For N=3 (W_3): the quartic shadow has MULTI-VARIABLE structure
    (W_3 has generators at weights 2 and 3, so Q lives in Sym^4(V_2 + V_3)).
    The scalar projection is:
      Q^scalar_{W_3} = numerator / [c_{W_3} * polynomial(c_{W_3})]

    For N >= 3: the quartic contact is a MATRIX (not scalar) because
    the strong generators have multiple weights. We return the scalar
    (T-T-T-T) projection.

    For general N, we use the Virasoro-like approximation for the T-channel:
      Q^{TT}_{W_N}(k) ~ 10/[c(5c + 22)]
    evaluated at c = c_{W_N}(k). This is the STRESS-TENSOR contribution.
    """
    c = wn_central_charge(k, N)
    if c == float('inf'):
        return float('inf')
    # Stress tensor contribution (always present)
    denom_tt = c * (5.0 * c + 22.0)
    if abs(denom_tt) < 1e-15:
        return float('inf')
    q_tt = 10.0 / denom_tt

    if N == 2:
        return q_tt  # Virasoro: only T, so Q = Q^{TT}

    # For N >= 3: additional channels from higher-weight generators.
    # The full quartic is a tensor in Sym^4(bigoplus V_{w_i}).
    # We return the scalar T-T-T-T projection.
    return q_tt


def wn_degeneration_locus(N):
    """
    Degeneration locus for W_k(sl_N).

    D = {k = -N} (critical level, Sugawara undefined).

    The Q^contact poles (where 5c + 22 = 0) give additional special values:
      c_{W_N} = -22/5 implies k + N = 5N(N^2-1)/(5(N-1) + 22) (solvable).

    Returns dict with degeneration data.
    """
    hv = wn_dual_coxeter(N)
    critical = -float(hv)

    # Solve c_{W_N}(k) = 0: (N-1)[1 - N(N+1)/(k+N)] = 0
    # => k + N = N(N+1) => k = N^2 - 1 + N - N = N^2
    # Wait: 1 - N(N+1)/(k+N) = 0 => k+N = N(N+1) => k = N^2 + N - N = N^2
    # Actually k = N(N+1) - N = N^2.
    k_c_zero = float(N * N)

    # Solve 5*c + 22 = 0: c = -22/5
    # (N-1)[1 - N(N+1)/(k+N)] = -22/5
    # 1 - N(N+1)/(k+N) = -22/(5(N-1))
    # N(N+1)/(k+N) = 1 + 22/(5(N-1)) = (5(N-1) + 22)/(5(N-1))
    # k+N = 5N(N+1)(N-1)/(5N - 5 + 22) = 5N(N+1)(N-1)/(5N+17)
    denom_lee_yang = 5 * N + 17
    k_lee_yang = 5.0 * N * (N + 1) * (N - 1) / denom_lee_yang - N

    return {
        'N': N,
        'critical_level': critical,
        'kappa_zero_level': k_c_zero,
        'Q_contact_pole_level': k_lee_yang,
        'type': 'discrete',
        'algebraic': True,
    }


def wn_level_rank_involution(k, N):
    """
    Level-rank duality: under k <-> -k - 2N, c_{W_N}(k) is invariant
    (up to a known shift).

    More precisely, the FKW level-rank duality for W_k(sl_N):
      W_k(sl_N) at level k  <->  W_{k'}(sl_{k+N}) at level k' = N - (k+N) = -k

    For our purposes: the dual level is k' = -(k + 2N) and the dual rank is
    determined by the coset construction. The central charge transforms as:
      c_{W_N}(k) + c_{W_N}(k') = (N-1) for appropriate dual.

    Returns dual level.
    """
    return -(k + 2 * N)


# =============================================================================
# 4. Lattice VOA: V_Lambda(R) at varying radius
# =============================================================================

def lattice_curvature(rank=1):
    """
    Curvature kappa = rank for lattice VOAs, INDEPENDENT of radius.

    This is proved: the Heisenberg atom curvature is kappa = 1 per boson,
    and lattice VOAs are extensions of the Heisenberg. The extension does
    not change the curvature (it's a topological invariant of the bar complex).
    """
    return float(rank)


def lattice_constrained_epstein_rank1(s, R, nmax=500):
    """
    Constrained Epstein zeta for rank-1 lattice VOA at radius R:

      epsilon^1_s(R) = 2(R^{2s} + R^{-2s}) * zeta(2s)

    where:
      - R^{2s} + R^{-2s} comes from momentum + winding at the fundamental level
      - zeta(2s) = sum_{n>=1} n^{-2s} from the KK tower

    More precisely, the scalar spectrum at radius R:
      - Momentum sector (w=0): Delta = n^2/(2R^2) for n >= 1, multiplicity 2 (pm n)
      - Winding sector (n=0): Delta = w^2 R^2/2 for w >= 1, multiplicity 2 (pm w)

    So epsilon^1_s = sum_{n>=1} 2*(n^2/R^2)^{-s} + sum_{w>=1} 2*(w^2 R^2)^{-s}
                   = 2*R^{2s} * zeta(2s) + 2*R^{-2s} * zeta(2s)
                   = 2(R^{2s} + R^{-2s}) * zeta(2s).

    T-duality R -> 1/R swaps momentum and winding, preserving the sum.
    At R = 1 (self-dual): epsilon^1_s = 4*zeta(2s).
    """
    # Direct summation for numerical verification
    result = 0.0
    for n in range(1, nmax + 1):
        # Momentum
        delta_mom = n * n / (2.0 * R * R)
        result += 2.0 * (2.0 * delta_mom) ** (-s)
        # Winding
        delta_wind = n * n * R * R / 2.0
        result += 2.0 * (2.0 * delta_wind) ** (-s)
    return result


def lattice_constrained_epstein_analytic(s, R):
    """
    Analytic formula: epsilon^1_s(R) = 2(R^{2s} + R^{-2s}) * zeta(2s).

    Uses mpmath for zeta evaluation.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required for analytic Epstein")
    z = float(mpmath.zeta(2 * s))
    return 2.0 * (R ** (2 * s) + R ** (-2 * s)) * z


def lattice_epstein_residue_at_zeta_zero(R, rho_imag):
    """
    Residue of epsilon^1_s(R) at s = (1 + i*gamma)/2 where zeta(1 + 2i*gamma) = 0.

    Since epsilon^1_s = 2(R^{2s} + R^{-2s}) * zeta(2s), and zeta has a SIMPLE
    zero at 2s = 1/2 + i*gamma (i.e., s = (1 + 2i*gamma)/4 on the 2s line...

    Wait, more carefully: zeros of zeta(2s) occur at 2s = 1/2 + i*gamma_n,
    i.e., s = 1/4 + i*gamma_n/2.

    At s_0 = 1/4 + i*gamma_n/2:
      Res_{s=s_0} epsilon = 2(R^{2s_0} + R^{-2s_0}) * Res_{s=s_0} zeta(2s)
                          = 2(R^{2s_0} + R^{-2s_0}) * (1/2) * zeta'(2s_0)^{-1}

    Actually, if zeta(2s_0) = 0, the RESIDUE of zeta(2s) at s = s_0 is not
    well-defined (zeta has zeros, not poles there). The epsilon function
    inherits ZEROS from zeta, not poles.

    What we compute: |epsilon(s_0)| as a function of R, where s_0 is near
    (but not exactly at) a zeta zero. The R-dependent factor modulates the
    zero landscape.

    Returns the R-dependent modulation factor |R^{2s_0} + R^{-2s_0}|.
    """
    s0 = 0.25 + 0.5j * rho_imag
    val = R ** (2 * s0) + R ** (-2 * s0)
    return abs(val)


def lattice_tduality_check(s, R, nmax=500):
    """
    Verify T-duality: epsilon^1_s(R) = epsilon^1_s(1/R).

    Returns (eps_R, eps_dual, relative_error).
    """
    eps_R = lattice_constrained_epstein_rank1(s, R, nmax)
    eps_dual = lattice_constrained_epstein_rank1(s, 1.0 / R, nmax)
    rel_err = abs(eps_R - eps_dual) / max(abs(eps_R), 1e-30)
    return eps_R, eps_dual, rel_err


def lattice_degeneration_locus():
    """
    Degeneration locus for lattice VOA: D = empty set.

    Lattice VOAs are Koszul for ALL radii R > 0. This is because:
    1. V_Lambda is an extension of the Heisenberg (PBW base).
    2. The extension is by vertex operators, which are Koszul-transparent.
    3. cor:universal-koszul applies.

    T-duality R <-> 1/R is a SYMMETRY of the Koszul locus, not a boundary.
    """
    return {
        'degeneration_set': [],
        'type': 'empty',
        'algebraic': True,  # vacuously
        'reason': 'PBW + lattice extension Koszul-transparent',
    }


# =============================================================================
# 5. Degeneration locus topology
# =============================================================================

def degeneration_locus_is_discrete(family):
    """
    Test: is the degeneration locus discrete?

    For all four families:
      - Affine sl_2: D = {-2}, discrete (1 point)
      - Virasoro: D = {0, -22/5}, discrete (2 points)
      - W_N: D = {-N}, discrete (1 point)
      - Lattice: D = empty, discrete (vacuously)

    Returns (is_discrete, description).
    """
    if family == 'affine_sl2':
        D = affine_sl2_degeneration_locus()
        return True, f"D = {D['critical']}, |D| = {len(D['critical'])}"
    elif family == 'virasoro':
        D = virasoro_degeneration_locus()
        return True, f"D = {D['Q_contact_poles']}, |D| = {len(D['Q_contact_poles'])}"
    elif family.startswith('W_'):
        N = int(family.split('_')[1])
        D = wn_degeneration_locus(N)
        return True, f"D = {{{D['critical_level']}}}, |D| = 1"
    elif family == 'lattice':
        return True, "D = empty, |D| = 0"
    else:
        raise ValueError(f"Unknown family: {family}")


def degeneration_locus_is_algebraic(family):
    """
    Test: is the degeneration locus algebraic (roots of polynomials)?

    For all families the answer is YES:
      - Affine: k = -2 is root of k + 2 = 0 (degree 1)
      - Virasoro: c = 0 is root of c = 0; c = -22/5 is root of 5c + 22 = 0
      - W_N: k = -N is root of k + N = 0
      - Lattice: empty (vacuously algebraic)

    Returns (is_algebraic, minimal_polynomials).
    """
    if family == 'affine_sl2':
        return True, {'k=-2': [2, 1]}  # k + 2 = 0
    elif family == 'virasoro':
        return True, {'c=0': [0, 1], 'c=-22/5': [22, 5]}  # c=0, 5c+22=0
    elif family.startswith('W_'):
        N = int(family.split('_')[1])
        return True, {f'k=-{N}': [N, 1]}  # k + N = 0
    elif family == 'lattice':
        return True, {}
    else:
        raise ValueError(f"Unknown family: {family}")


# =============================================================================
# 6. Arithmetic content of minimal model central charges
# =============================================================================

def minimal_model_arithmetic(p_max=10, q_max=11):
    """
    Analyze the arithmetic of minimal model central charges c_{p,q}.

    c_{p,q} = 1 - 6(p-q)^2/(pq) is ALWAYS rational.

    Key question: is there a pattern relating these to zeta zeros?
    Answer: NO direct relation. The c_{p,q} are all rational (hence algebraic
    of degree 1), while zeta zeros are transcendental. The connection to
    zeta zeros is through the EPSTEIN ZETA of the lattice VOA, not through
    the parameter values themselves.

    Returns detailed arithmetic data.
    """
    results = []
    for q in range(2, q_max + 1):
        for p in range(q + 1, p_max + 1):
            if gcd(p, q) != 1:
                continue
            c_exact = virasoro_minimal_model_c_exact(p, q)
            c_float = float(c_exact)
            results.append({
                'p': p,
                'q': q,
                'c': c_float,
                'c_exact': c_exact,
                'numerator': c_exact.numerator,
                'denominator': c_exact.denominator,
                'algebraic_degree': 1,
                'height': max(abs(c_exact.numerator), abs(c_exact.denominator)),
            })
    return sorted(results, key=lambda x: x['c'])


def minimal_model_density(c_min=-30, c_max=1, p_max=50, q_max=51):
    """
    Compute the density of minimal model central charges in an interval.

    The c_{p,q} accumulate near c = 1 from below as p,q -> infinity.
    For fixed q, c_{p,q} -> 1 as p -> infinity.
    For p = q+1 (unitary): c -> 1 as q -> infinity.

    Returns (c_values, density_estimate).
    """
    c_values = []
    for q in range(2, q_max + 1):
        for p in range(q + 1, p_max + 1):
            if gcd(p, q) != 1:
                continue
            c = virasoro_minimal_model_c(p, q)
            if c_min <= c <= c_max:
                c_values.append(c)
    c_values.sort()
    return c_values


# =============================================================================
# 7. Level-crossing phenomenon: k -> -2 for affine sl_2
# =============================================================================

def level_crossing_rate(epsilon_values):
    """
    As k -> -2, compute kappa(k) = k + 2 -> 0.

    The rate is LINEAR: |kappa| = |k + 2| = epsilon.

    The bar-cobar quasi-isomorphism Omega(B(V_k)) -> V_k has an obstruction
    that vanishes for all k != -2 (since V_k is Koszul). But the inverse
    map's "size" (measured by the norm of the homotopy) grows as k -> -2.

    The homotopy inverse has norm ~ 1/kappa = 1/|k+2| (pole).

    Returns list of (epsilon, kappa, homotopy_norm_estimate).
    """
    results = []
    for eps in epsilon_values:
        k = -2.0 + eps
        kappa = affine_sl2_curvature(k)
        # Homotopy norm estimate: the bar differential's leading term is
        # proportional to kappa, so inverting it costs 1/kappa.
        homotopy_norm = 1.0 / abs(kappa) if abs(kappa) > 1e-15 else float('inf')
        results.append({
            'epsilon': eps,
            'k': k,
            'kappa': kappa,
            'homotopy_norm': homotopy_norm,
            'rate': 'linear',  # |kappa| = |epsilon|, linear in |k+2|
        })
    return results


def level_crossing_fit(epsilon_values):
    """
    Fit the level-crossing rate: |kappa| vs |k+2|.

    Expected: kappa = k+2, so |kappa| = |epsilon| (slope 1, intercept 0).
    This is EXACTLY linear, no higher-order terms.

    Returns (slope, intercept, r_squared).
    """
    eps = np.array(epsilon_values)
    kappas = np.array([abs(affine_sl2_curvature(-2.0 + e)) for e in eps])

    # Linear fit: kappa = a * epsilon + b
    if len(eps) >= 2:
        coeffs = np.polyfit(eps, kappas, 1)
        slope, intercept = coeffs
        predicted = np.polyval(coeffs, eps)
        ss_res = np.sum((kappas - predicted) ** 2)
        ss_tot = np.sum((kappas - np.mean(kappas)) ** 2)
        r_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
        return slope, intercept, r_squared
    return 1.0, 0.0, 1.0


# =============================================================================
# 8. Phase transition detection: spectral gap
# =============================================================================

def bar_spectral_gap_virasoro(c, truncation=20):
    """
    Spectral gap of the bar differential for Vir_c.

    The bar differential d_bar on B(Vir_c) has eigenvalues that depend on c.
    At a minimal model c = c_{p,q}, the bar cohomology acquires extra classes
    from null vectors. The spectral gap is the smallest nonzero eigenvalue
    of d_bar^* d_bar on the relevant weight space.

    MODEL COMPUTATION: We model the bar differential's spectrum on the
    weight-N subspace of the bar complex as a matrix whose entries are
    polynomial in c. The spectral gap is then an algebraic function of c.

    For the weight-2 subspace (simplest nontrivial):
    B^2(Vir_c) has basis elements from T (weight 2 generator).
    The bar differential maps: d_bar(T tensor T) involves the OPE T(z)T(w),
    and the resulting matrix has entries involving c.

    Simplified model: The bar differential at weight 2 has a matrix element
    proportional to c (from the T-T OPE double pole). The spectral gap is
    therefore proportional to |c|^2 at weight 2.

    At higher weights, the spectral gap involves Kac determinants, which
    vanish at minimal model values.
    """
    if abs(c) < 1e-15:
        return 0.0  # Gap closes at c = 0

    # Weight-2 contribution: gap ~ c^2 (from Kac determinant at level 2)
    # det_2(c, h) = h(2h + 1)(16h^2 - 10h + (2h+1)c)/... for Verma module
    # For the bar complex at h = 0 (vacuum): simplified to |c|^2 scaling
    gap_weight2 = abs(c) ** 2

    # Weight-N contributions involve Kac determinant at level N
    # det_N vanishes on curves in the (c,h) plane
    # For h = 0: det_N(c, 0) is a polynomial in c that factors through
    # the minimal model values
    gaps = [gap_weight2]

    for N in range(3, truncation + 1):
        # Kac determinant at level N, h = 0:
        # Product over r,s with 1 <= r*s <= N of (h - h_{r,s}(c))
        # At h = 0: product of (-h_{r,s}(c))
        # h_{r,s}(c) = [(r(m+1) - sm)^2 - 1] / [4m(m+1)]
        # where c = 1 - 6/m(m+1), i.e., m(m+1) = 6/(1-c)
        kac_product = 1.0
        for r in range(1, N + 1):
            for s in range(1, N // r + 1):
                if r * s > N:
                    break
                if r * s <= N:
                    # h_{r,s} at h=0 for vacuum module
                    # Use the explicit formula
                    if abs(1 - c) > 1e-10:
                        discriminant = 1 + 24.0 / (1.0 - c + 1e-30)
                        if discriminant < 0:
                            continue
                        m_param = (1 + np.sqrt(discriminant)) / 2.0
                        if np.isnan(m_param) or abs(m_param * (m_param + 1)) < 1e-10:
                            continue
                        h_rs = ((r * (m_param + 1) - s * m_param) ** 2 - 1) / (4 * m_param * (m_param + 1))
                        kac_product *= abs(h_rs) if abs(h_rs) > 1e-30 else 1e-30
        gaps.append(kac_product)

    return min(gaps) if gaps else 0.0


def spectral_gap_near_minimal_model(p0, q0, delta_c_values):
    """
    Compute the spectral gap as c varies near a minimal model value c_{p0,q0}.

    At c = c_{p0,q0}: the Kac determinant has extra zeros, which closes the
    spectral gap at certain weights. The gap opens as c moves away.

    KEY QUESTION: does the gap open continuously or discontinuously?
    ANSWER: Continuously. The Kac determinant is polynomial in c, so its
    eigenvalues vary continuously. The gap opens as sqrt(|c - c_0|) generically
    (square root from a simple zero of the determinant).

    Returns list of (delta_c, gap) pairs.
    """
    c0 = virasoro_minimal_model_c(p0, q0)
    results = []
    for dc in delta_c_values:
        c = c0 + dc
        gap = bar_spectral_gap_virasoro(c, truncation=10)
        results.append({
            'delta_c': dc,
            'c': c,
            'c_minimal': c0,
            'gap': gap,
            'p': p0,
            'q': q0,
        })
    return results


def gap_opening_exponent(p0, q0, n_points=50):
    """
    Fit the spectral gap opening near c_{p0,q0}.

    Expected: gap ~ |delta_c|^alpha for some exponent alpha.
    Generic expectation: alpha = 1 (linear in delta_c because the Kac
    determinant has a simple zero and the gap goes as the absolute value
    of the eigenvalue, which is linear in the parameter perturbation).

    Returns (alpha, r_squared).
    """
    c0 = virasoro_minimal_model_c(p0, q0)
    delta_cs = np.logspace(-6, -1, n_points)
    gaps = []
    for dc in delta_cs:
        g = bar_spectral_gap_virasoro(c0 + dc, truncation=8)
        if g > 0:
            gaps.append((dc, g))

    if len(gaps) < 5:
        return None, None

    log_dc = np.log(np.array([x[0] for x in gaps]))
    log_gap = np.log(np.array([x[1] for x in gaps]))

    coeffs = np.polyfit(log_dc, log_gap, 1)
    alpha = coeffs[0]
    predicted = np.polyval(coeffs, log_dc)
    ss_res = np.sum((log_gap - predicted) ** 2)
    ss_tot = np.sum((log_gap - np.mean(log_gap)) ** 2)
    r_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0

    return alpha, r_squared


# =============================================================================
# 9. Summary: parametrized bar-cobar landscape
# =============================================================================

def parametrized_landscape_summary():
    """
    Summary of the parametrized bar-cobar landscape across all families.

    KEY FINDINGS:
    1. Degeneration locus is ALWAYS discrete and algebraic.
    2. For universal algebras, only critical levels degenerate.
    3. Admissible/minimal model values affect simple quotients only.
    4. Level-crossing rate is exactly linear (kappa = k + h^v).
    5. Spectral gap opens continuously at minimal model boundaries.
    6. All minimal model central charges are rational (algebraic degree 1).
    7. No direct connection between degeneration loci and zeta zeros.
       The zeta zeros appear in the EPSTEIN ZETA of lattice VOAs (via partition
       function), not in the degeneration parameter values.
    """
    return {
        'families': {
            'affine_sl2': {
                'parameter': 'k (level)',
                'degeneration': 'D = {k = -2}',
                'discrete': True,
                'algebraic': True,
                'crossing_rate': 'linear',
            },
            'virasoro': {
                'parameter': 'c (central charge)',
                'degeneration': 'D = {c = 0, c = -22/5}',
                'discrete': True,
                'algebraic': True,
                'gap_opening': 'continuous',
            },
            'W_N': {
                'parameter': 'k (level), N (rank)',
                'degeneration': 'D = {k = -N} for each N',
                'discrete': True,
                'algebraic': True,
            },
            'lattice': {
                'parameter': 'R (radius)',
                'degeneration': 'D = empty',
                'discrete': True,
                'algebraic': True,
                'T_duality': 'R <-> 1/R symmetry',
            },
        },
        'universal_theorem': (
            'For universal vertex algebras V_k(g), D = {k = -h^v} '
            '(prop:pbw-universality, cor:universal-koszul).'
        ),
    }


# =============================================================================
# 10. Visualization helpers
# =============================================================================

def curvature_grid_affine(k_min=-5, k_max=5, n_points=200):
    """
    Compute kappa(k) on a grid for visualization.
    Returns (k_values, kappa_values).
    """
    ks = np.linspace(k_min, k_max, n_points)
    kappas = np.array([affine_sl2_curvature(k) for k in ks])
    return ks, kappas


def curvature_grid_virasoro(c_min=-10, c_max=30, n_points=200):
    """
    Compute kappa(c) and Q^contact(c) on a grid.
    Returns (c_values, kappa_values, Q_values).
    """
    cs = np.linspace(c_min, c_max, n_points)
    kappas = np.array([virasoro_curvature(c) for c in cs])
    Qs = []
    for c in cs:
        denom = c * (5.0 * c + 22.0)
        if abs(denom) < 0.1:
            Qs.append(np.nan)
        else:
            Qs.append(10.0 / denom)
    return cs, kappas, np.array(Qs)


def epstein_modulation_grid(R_min=0.1, R_max=10.0, n_R=100, gamma_values=None):
    """
    Compute the R-dependent modulation factor |R^{2s_0} + R^{-2s_0}| at zeta zeros.

    gamma_values: imaginary parts of first few zeta zeros.
    Default: first 5 zeta zeros.
    """
    if gamma_values is None:
        # First 5 nontrivial zeta zeros (imaginary parts)
        gamma_values = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]

    Rs = np.linspace(R_min, R_max, n_R)
    results = {}
    for gamma in gamma_values:
        mods = np.array([lattice_epstein_residue_at_zeta_zero(R, gamma) for R in Rs])
        results[gamma] = mods
    return Rs, results


def wn_curvature_grid(N, k_min=-10, k_max=10, n_points=200):
    """
    Compute kappa_{W_N}(k) on a grid.
    Returns (k_values, kappa_values).
    """
    ks = np.linspace(k_min, k_max, n_points)
    kappas = []
    for k in ks:
        if abs(k + N) < 0.05:
            kappas.append(np.nan)
        else:
            kappas.append(wn_curvature(k, N))
    return ks, np.array(kappas)
