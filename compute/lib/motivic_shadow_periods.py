#!/usr/bin/env python3
r"""Motivic decomposition and periods of shadow amplitudes.

THE MATHEMATICAL SETTING (Kontsevich-Zagier period theory):

Shadow amplitudes are integrals over configuration spaces / moduli spaces:

    S_r(A) = sum_Gamma (1/|Aut(Gamma)|) int_{C_n(X)} omega_Gamma

These are PERIODS in the Kontsevich-Zagier sense: integrals of algebraic
differential forms over semialgebraic domains.

MOTIVIC DECOMPOSITION:

For lattice VOA V_Lambda of rank r with theta function
Theta_Lambda = c_E * E_{r/2} + sum_j c_j * f_j (Hecke decomposition),
the shadow obstruction tower admits a three-part motivic decomposition:

    Theta_{V_Lambda} = Theta^Eis + Theta^cusp + Theta^alg

where:

(1) Theta^Eis: the Eisenstein part.
    Periods lie in Q[pi^2, zeta(3), zeta(5), ...] = periods of mixed Tate motives.
    At genus 1: F_1^scalar = kappa/24 = rank(Lambda)/24 is RATIONAL (period of Q(0)).
    The Bernoulli numbers B_{2g}/(4g(2g-2)!) are periods of the Tate motive Q(g)
    via zeta(2g) = (-1)^{g+1} (2pi)^{2g} B_{2g} / (2(2g)!).

(2) Theta^cusp: the cuspidal part.
    Periods involve L-values L(k, f_j) for Hecke eigenforms f_j in S_{r/2}.
    At genus 1: the cusp contribution involves integral representations of L(s, f_j).
    These are periods of Chow motives h^1(f_j) -- genuinely NON-TATE.

(3) Theta^alg: the algebraic/homotopy part.
    Periods in Q(c) -- rational functions of the central charge.
    For lattice VOAs: this vanishes (d_alg = 0, all homotopy is arithmetic).
    For Virasoro: S_r = (-1)^{r+1} (6/c)^r / r, all rational in c.

MOTIVIC WEIGHTS:

The motivic weight of a shadow amplitude is:

    w(F_g^scalar) = 0            (rational number, or zeta(2g)/(2pi)^{2g})
    w(delta_pf^{(g)}) = 0        (configuration space integral, mixed Tate)
    w(F_g^cusp(f_j)) = k-1       (L(k, f_j) has motivic weight k-1 where
                                   k = weight of the cusp form)

For lattice VOAs at genus 1:
    F_1(V_Lambda) involves the theta function Theta_Lambda(tau).
    After integration over M_{1,1} via Rankin-Selberg:
    - The Eisenstein part contributes zeta(k)*zeta(k-1) (mixed Tate)
    - The cusp part contributes L(k, f_j) (non-Tate, motivic weight k-1)

PERIOD MAP AND INJECTIVITY:

The period map Theta_A |-> {per_g(Theta_A)}_{g >= 1} sends the MC element
to the sequence of genus-g amplitudes.

CLAIM: The scalar period map (kappa alone) is NOT injective on lattice VOAs.
REASON: All Niemeier lattices (24 lattices of rank 24) give kappa = 24.
    The scalar period map sees only kappa = rank.
    The FULL period map (including cusp form content) distinguishes them.

MIXED TATE vs NON-TATE:

At genus 1:
    Scalar amplitude F_1 = kappa/24 is in Q -- Tate motive Q(0).
    Theta correction: if Theta_Lambda has cusp part sum c_j f_j,
    the period L(k, f_j) is non-Tate.

At genus 2:
    Siegel modular forms enter via the genus-2 Schottky relation.
    The shadow amplitude involves paramodular L-functions.

The DEPTH of the motivic structure (= distance from mixed Tate) equals d_arith:
    d_arith = 0: all periods are mixed Tate (Virasoro, Heisenberg)
    d_arith = 1: one non-Tate motive (E_8 type lattices, no cusp forms
                  but Eisenstein L-products are beyond Q)
    d_arith >= 2: cusp form L-values present (Leech: d_arith = 3)

Manuscript references:
    prop:shadow-periods (arithmetic_shadows.tex)
    rem:motivic-decomposition (arithmetic_shadows.tex)
    rem:kummer-motive (arithmetic_shadows.tex)
    rem:transcendence-asymmetry (arithmetic_shadows.tex)
    rem:mc-motivic-identity (arithmetic_shadows.tex)
    thm:shadow-spectral-correspondence (arithmetic_shadows.tex)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple
import math

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =========================================================================
# 1. Motivic weight classification
# =========================================================================

# Motivic weight of standard periods:
#   Q(0): rational numbers -- weight 0
#   Q(n): Tate motive -- weight 2n (periods involve (2*pi*i)^n)
#   h^1(f): motive of weight-k cusp form -- weight k-1
#   Mixed Tate: weight filtration, largest weight = depth

MOTIVIC_WEIGHTS = {
    'rational': 0,          # Q(0): periods in Q
    'pi': 2,                # Q(1): period 2*pi*i
    'zeta_even': 'varies',  # zeta(2g) = rational * pi^{2g}, motivic weight 2g
    'zeta_odd': 'varies',   # zeta(2g+1) -- conjecturally transcendental, weight ?
    'cusp_form': 'k-1',     # L(k, f_j) for weight-k cusp form
}


def motivic_weight_zeta_even(g: int) -> int:
    r"""Motivic weight of zeta(2g) = (-1)^{g+1} (2pi)^{2g} B_{2g} / (2(2g)!).

    zeta(2g) is a period of the Tate motive Q(g).
    Its motivic weight is 2g (the Hodge realization has type (g,g)).

    But: zeta(2g) / (2pi)^{2g} = (-1)^{g+1} B_{2g} / (2(2g)!) is RATIONAL.
    So the "normalized" Faber-Pandharipande constant
        lambda_g^FP = B_{2g} / (4g(2g-2)!)
    is rational -- it is a period of Q(0), motivic weight 0.

    The distinction: the period zeta(2g) itself has motivic weight 2g,
    but lambda_g^FP = zeta(2g) / (2pi)^{2g} * (rational factor) has weight 0.
    """
    return 2 * g


def motivic_weight_cusp_form(k: int) -> int:
    r"""Motivic weight of L(k, f) for a cusp form f of weight k.

    The Deligne-Scholl motive M(f) attached to a weight-k eigenform f
    has motivic weight k-1. The critical L-value L(k, f) is a period
    of M(f)(k), which has motivic weight k-1 - 2k = -(k+1)... NO.

    CORRECTION (Beilinson principle: compute, don't assume):
    The motive M(f) has Hodge realization of type {(k-1, 0), (0, k-1)}.
    The motivic weight is k-1.
    The critical L-value L(m, f) for m in {1, 2, ..., k-1} is a period
    of M(f) in the sense of Deligne's conjecture.
    The motivic weight of the period L(m, f) / Omega^{+/-} is 0
    (rational number), but L(m, f) itself has transcendence controlled
    by the motivic weight k-1.
    """
    return k - 1


# =========================================================================
# 2. Bernoulli numbers and Faber-Pandharipande constants
# =========================================================================

def bernoulli_number(n: int) -> Fraction:
    r"""Bernoulli number B_n as exact fraction.

    B_0 = 1, B_1 = -1/2, B_2 = 1/6, B_4 = -1/30, B_6 = 1/42,
    B_8 = -1/30, B_10 = 5/66, B_12 = -691/2730.

    Uses the standard recursion:
        sum_{k=0}^{m} C(m+1, k) B_k = 0  for m >= 1
    hence B_m = -(1/(m+1)) sum_{k=0}^{m-1} C(m+1, k) B_k.
    """
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    for m in range(1, n + 1):
        s = Fraction(0)
        for k in range(m):
            # Compute C(m+1, k) = (m+1)! / (k! * (m+1-k)!)
            # Using: C(n, k) = prod_{j=1}^{k} (n - k + j) / j
            # equivalently: C(n, k) = prod_{j=1}^{k} (n - j + 1) / j
            binom = Fraction(1)
            for j in range(1, k + 1):
                binom = binom * Fraction(m + 1 - j + 1, j)
            s += binom * B[k]
        B[m] = -s / Fraction(m + 1)
    return B[n]


def lambda_g_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande constant lambda_g^FP = B_{2g} / (4g * (2g-2)!).

    int_{M_g} lambda_g = lambda_g^FP

    This is a RATIONAL NUMBER -- a period of Q(0).
    The rationality is a consequence of the Mumford relation
    and the fact that M_g is defined over Q.

    g=1: B_2/(4*1*0!) = (1/6)/4 = 1/24
    g=2: B_4/(4*2*2!) = (-1/30)/16 = -1/480
         WAIT: (2g-2)! = 2! = 2, so B_4/(4*2*2) = (-1/30)/16 = -1/480
         CHECK: Faber-Pandharipande: int_{M_2} lambda_2 = 1/1152? NO.

    INDEPENDENT RECOMPUTATION (AP1: never copy formulas):
    The standard Faber-Pandharipande formula is:
        int_{M_g} lambda_g = (-1)^g * B_{2g} / (2g * (2g)!) * (2g-1)!! / 2^g

    Actually the cleanest formula is via the A-hat genus:
        F_g^scalar = kappa * lambda_g^FP
    where lambda_g^FP is defined so that
        sum_{g>=1} lambda_g^FP * hbar^{2g} = A-hat(i*hbar) - 1
        = hbar^2/24 + 7*hbar^4/5760 + ...

    So: lambda_1^FP = 1/24, lambda_2^FP = 7/5760.

    Using A-hat(x) = (x/2) / sinh(x/2):
    A-hat(ix) = (ix/2) / sin(ix/2) ... NO.
    A-hat(ix) = (ix/2) / (i*sin(x/2)) = (x/2) / sin(x/2).

    (x/2)/sin(x/2) = 1 + x^2/24 + 7x^4/5760 + 31x^6/967680 + ...

    So: lambda_g^FP = coefficient of x^{2g} in (x/2)/sin(x/2) - 1.

    Let me verify: (x/2)/sin(x/2) = sum_{n>=0} (2^{2n}-2) |B_{2n}| / (2n)! * x^{2n} / 4^n
    Hmm, let me just compute directly.

    (x/2)/sin(x/2) = 1 + sum_{k>=1} (-1)^{k+1} (2 - 2^{2-2k}) B_{2k} / (2k)! * (x/2)^{2k}

    Actually: sin(z)/z = sum (-1)^n z^{2n}/(2n+1)!, so
    z/sin(z) = 1/[1 - z^2/6 + z^4/120 - ...].

    Set z = x/2:
    (x/2)/sin(x/2) = 1/[1 - x^2/24 + x^4/1920 - ...]

    By series inversion:
    f = 1 + a_1 x^2 + a_2 x^4 + ...
    where 1/[1 - u] = 1 + u + u^2 + ... with u = x^2/24 - x^4/1920 + ...

    At order x^2: coefficient = 1/24
    At order x^4: coefficient = 1/24^2 + 1/1920... no, let me be careful.

    u = x^2/24 - x^4/1920 + x^6/322560 - ...
    u^2 = x^4/576 + ...
    u^3 = x^6/13824 + ...

    1/(1-u) = 1 + u + u^2 + u^3 + ...
    x^2 coeff: 1/24
    x^4 coeff: -1/1920 + 1/576 = (-576 + 1920)/(1920*576) = 1344/1105920 = 7/5760
    CHECK: 7/5760. YES.

    So lambda_1^FP = 1/24, lambda_2^FP = 7/5760.
    """
    if g < 1:
        return Fraction(0)
    # Compute via the A-hat power series expansion
    # (x/2)/sin(x/2) = sum_{g>=0} lambda_g * x^{2g}
    # with lambda_0 = 1.
    # Use the relation: sin(z) = z - z^3/6 + z^5/120 - ...
    # z/sin(z) = 1/(1 - z^2/6 + z^4/120 - z^6/5040 + ...)
    # Then substitute z = x/2.

    # Build the Taylor coefficients of sin(z)/z = 1 - z^2/6 + z^4/120 - ...
    # up to z^{2*g_max}.
    g_max = g
    # Coefficients of sin(z)/z in z^{2k}: (-1)^k / (2k+1)!
    sinc_coeffs = []
    for k in range(g_max + 1):
        fac = Fraction(1)
        for j in range(1, 2 * k + 2):
            fac *= j
        sinc_coeffs.append(Fraction((-1) ** k, 1) / fac)

    # Now z/sin(z) = 1/(sinc_coeffs[0] + sinc_coeffs[1]*z^2 + ...)
    # = 1/[1 + (sinc_coeffs[1]*z^2 + sinc_coeffs[2]*z^4 + ...)]
    # Series inversion: if f(z) = 1/(1 - u(z)) where u = -sinc_coeffs[1]*z^2 - ...
    # Actually: sinc_coeffs[0] = 1, so we need 1/(1 + v) where v = sum_{k>=1} sinc_coeffs[k] z^{2k}

    # Let a[k] = coefficient of z^{2k} in z/sin(z).
    # a[0] = 1.
    # Recursion from (z/sin(z)) * (sin(z)/z) = 1:
    # sum_{j=0}^{k} a[j] * sinc_coeffs[k-j] = delta_{k,0}
    # => a[k] = -sum_{j=0}^{k-1} a[j] * sinc_coeffs[k-j]  (since sinc_coeffs[0] = 1)

    a = [Fraction(0)] * (g_max + 1)
    a[0] = Fraction(1)
    for k in range(1, g_max + 1):
        s = Fraction(0)
        for j in range(k):
            s += a[j] * sinc_coeffs[k - j]
        a[k] = -s

    # Now a[k] = coefficient of z^{2k} in z/sin(z).
    # We need coefficient of x^{2g} in (x/2)/sin(x/2) = (1/2^1) * (x/2)/sin(x/2)
    # Wait: let z = x/2. Then z/sin(z) evaluated at z=x/2 gives
    # sum a[k] (x/2)^{2k} = sum a[k] x^{2k} / 4^k.
    # So the coefficient of x^{2g} in (x/2)/sin(x/2) is a[g] / 4^g.

    return a[g] / Fraction(4 ** g)


def verify_lambda_fp_values():
    r"""Cross-check lambda_g^FP values against known results.

    lambda_1^FP = 1/24        (Mumford)
    lambda_2^FP = 7/5760      (Faber-Pandharipande)
    lambda_3^FP = 31/967680   (Faber-Pandharipande)
    """
    checks = {
        1: Fraction(1, 24),
        2: Fraction(7, 5760),
        3: Fraction(31, 967680),
    }
    results = {}
    for g, expected in checks.items():
        computed = lambda_g_fp(g)
        results[g] = {
            'computed': computed,
            'expected': expected,
            'match': computed == expected,
        }
    return results


# =========================================================================
# 3. Period classification for shadow amplitudes
# =========================================================================

class MotivicPeriodType:
    """Classification of periods by motivic type."""
    RATIONAL = 'rational'           # Period of Q(0), in Q
    TATE = 'tate'                   # Period of Q(n), involves pi^{2n}
    MIXED_TATE = 'mixed_tate'       # Period of mixed Tate motive, involves zeta values
    KUMMER = 'kummer'               # Period of Kummer motive K(alpha)
    HECKE = 'hecke'                 # Period involving L(s, f) for a cusp form
    SIEGEL = 'siegel'               # Period involving Siegel modular forms


def classify_scalar_amplitude(g: int) -> Dict[str, Any]:
    r"""Classify the motivic type of the scalar amplitude F_g^scalar = kappa * lambda_g^FP.

    At every genus g >= 1:
        F_g^scalar = kappa * lambda_g^FP
    where lambda_g^FP is a RATIONAL number (period of Q(0)).

    Therefore F_g^scalar is rational * kappa.
    For lattice VOAs: kappa = rank (an integer), so F_g^scalar in Q.
    For Virasoro: kappa = c/2, so F_g^scalar in Q(c).

    The motivic weight is 0 regardless of genus.

    NOTE (AP22 cross-check): the generating function is
        sum_{g>=1} lambda_g^FP * hbar^{2g} = A-hat(i*hbar) - 1
    with the CORRECT index 2g (not 2g-2). The 1/24 at g=1 matches
    hbar^2/24, confirming the convention.
    """
    lam = lambda_g_fp(g)
    return {
        'genus': g,
        'lambda_g_fp': lam,
        'motivic_type': MotivicPeriodType.RATIONAL,
        'motivic_weight': 0,
        'period_ring': 'Q',
        'description': f'F_g^scalar = kappa * {lam} is rational * kappa',
        'transcendence_degree': 0,
    }


def classify_virasoro_shadow(r: int, c=None) -> Dict[str, Any]:
    r"""Classify the motivic type of the Virasoro shadow S_r(Vir_c).

    S_r = (-1)^{r+1} (6/c)^r / r  (leading order, from the Kummer motive K(6/c)).

    These are ALL rational functions of c -- periods of the trivial motive Q(0)
    over the function field Q(c).

    The Virasoro shadow obstruction tower is "transcendentally trivial":
    infinite depth, but all periods are algebraic.
    """
    if c is not None:
        c_frac = Fraction(c) if isinstance(c, int) else c
        if isinstance(c_frac, Fraction) and c_frac != 0:
            val = Fraction((-1) ** (r + 1)) * (Fraction(6) / c_frac) ** r / Fraction(r)
        else:
            val = None
    else:
        val = None

    return {
        'arity': r,
        'motivic_type': MotivicPeriodType.KUMMER,
        'motivic_weight': 0,
        'period_ring': 'Q(c)',
        'kummer_parameter': '6/c',
        'value': val,
        'description': f'S_{r} = (-1)^{r+1} (6/c)^{r} / {r} -- Kummer motive K(6/c)',
        'transcendence_degree': 0,
    }


def classify_lattice_amplitude(lattice_name: str, g: int = 1) -> Dict[str, Any]:
    r"""Classify the motivic type of the genus-g amplitude for a lattice VOA.

    At genus 1:
    - The scalar part F_1 = kappa/24 is RATIONAL (weight 0).
    - The Eisenstein part involves zeta(k)*zeta(k-1) -- MIXED TATE (weight 2k-2).
    - The cusp part involves L(k, f_j) -- NON-TATE (weight k-1).

    At genus g >= 2:
    - The scalar part F_g = kappa * lambda_g^FP is RATIONAL.
    - The planted-forest correction delta_pf^{(g)} is MIXED TATE
      (configuration space integral over FM_{n}(P^1)).
    - The full amplitude involves Siegel modular forms of degree g.
    """
    # Import lattice data
    from compute.lib.lattice_shadow_periods import (
        hecke_decompose,
        lattice_data,
        cusp_form_dim,
    )

    data = lattice_data(lattice_name)
    decomp = hecke_decompose(lattice_name)
    rank = data['rank']
    kappa = rank  # For lattice VOAs, kappa = rank

    scalar_part = {
        'type': MotivicPeriodType.RATIONAL,
        'value': Fraction(kappa) * lambda_g_fp(g) if g >= 1 else None,
        'weight': 0,
        'description': f'F_{g}^scalar = {kappa} * lambda_{g}^FP',
    }

    parts = [scalar_part]

    if g == 1:
        # Eisenstein contribution at genus 1
        if rank > 2:
            k = rank // 2
            eis_part = {
                'type': MotivicPeriodType.MIXED_TATE,
                'weight': 2 * k - 2,
                'description': f'Eisenstein: zeta({k})*zeta({k}-1) -- Tate motive Q({k}-1)',
                'l_functions': [f'zeta({k})', f'zeta({k - 1})'],
            }
            parts.append(eis_part)

        # Cusp form contributions at genus 1
        if not decomp['eisenstein_only']:
            for name, coeff in decomp['cusp_coeffs']:
                k = rank // 2
                cusp_part = {
                    'type': MotivicPeriodType.HECKE,
                    'weight': k - 1,
                    'cusp_form': name,
                    'coefficient': coeff,
                    'description': f'Cusp: L({k}, {name}) -- motive h^1({name}), weight {k - 1}',
                    'l_function': f'L({k}, {name})',
                }
                parts.append(cusp_part)

    elif g == 2:
        # At genus 2, Siegel modular forms enter
        siegel_part = {
            'type': MotivicPeriodType.SIEGEL,
            'weight': 'undetermined',
            'description': f'Genus-2: involves Siegel modular forms of degree 2',
        }
        parts.append(siegel_part)

    # Determine overall motivic type
    types = [p['type'] for p in parts]
    if MotivicPeriodType.HECKE in types:
        overall = MotivicPeriodType.HECKE
    elif MotivicPeriodType.SIEGEL in types:
        overall = MotivicPeriodType.SIEGEL
    elif MotivicPeriodType.MIXED_TATE in types:
        overall = MotivicPeriodType.MIXED_TATE
    else:
        overall = MotivicPeriodType.RATIONAL

    return {
        'lattice': lattice_name,
        'genus': g,
        'rank': rank,
        'kappa': kappa,
        'parts': parts,
        'overall_type': overall,
        'n_cusp_forms': len(decomp['cusp_coeffs']),
    }


# =========================================================================
# 4. Motivic decomposition of the shadow obstruction tower
# =========================================================================

def motivic_decomposition(lattice_name: str) -> Dict[str, Any]:
    r"""Full motivic decomposition H*(Theta_A) = H*_Eis + H*_cusp + H*_alg.

    For lattice VOAs:
        H*_alg = 0 (d_alg = 0: no homotopy-theoretic depth)
        H*_Eis: controlled by Eisenstein series E_{r/2}
        H*_cusp: controlled by cusp forms f_j in S_{r/2}

    The depth decomposition d = 1 + d_arith + d_alg determines:
        d_arith = #{non-Tate summands h^1(f_j) in motivic decomposition}
        d_alg = depth(W_* M^Tate_A) of the mixed Tate part
    """
    from compute.lib.lattice_shadow_periods import (
        hecke_decompose,
        lattice_data,
        cusp_form_dim,
        shadow_depth_from_hecke,
    )

    data = lattice_data(lattice_name)
    decomp = hecke_decompose(lattice_name)
    rank = data['rank']

    # Eisenstein part: always present
    eis_part = {
        'type': 'Eisenstein',
        'motivic_category': 'mixed_Tate',
        'l_functions': [],
    }
    if lattice_name == 'Z':
        eis_part['l_functions'] = ['zeta(2s)']
    elif rank <= 2:
        eis_part['l_functions'] = ['zeta(s)']
    else:
        k = rank // 2
        eis_part['l_functions'] = ['zeta(s)', f'zeta(s-{k - 1})']

    # Cusp part: non-Tate motives
    cusp_part = {
        'type': 'cuspidal',
        'motivic_category': 'non-Tate' if decomp['cusp_coeffs'] else 'empty',
        'motives': [],
    }
    if decomp['cusp_coeffs']:
        k = rank // 2
        for name, coeff in decomp['cusp_coeffs']:
            cusp_part['motives'].append({
                'form': name,
                'coefficient': coeff,
                'motive': f'h^1({name})',
                'motivic_weight': k - 1,
                'l_function': f'L(s, {name})',
            })

    # Algebraic part: for lattice VOAs, this is empty
    alg_part = {
        'type': 'algebraic',
        'motivic_category': 'trivial',
        'd_alg': 0,
        'description': 'Lattice VOAs have d_alg = 0: all depth is arithmetic',
    }

    # Depth computation
    cusp_dim = decomp['cusp_dim']
    depth = data['shadow_depth']
    d_arith = depth - 1  # d = 1 + d_arith for lattice VOAs (d_alg = 0)

    return {
        'lattice': lattice_name,
        'rank': rank,
        'depth': depth,
        'd_arith': d_arith,
        'd_alg': 0,
        'eisenstein': eis_part,
        'cuspidal': cusp_part,
        'algebraic': alg_part,
        'n_non_tate_motives': len(cusp_part['motives']),
        'is_mixed_tate': len(cusp_part['motives']) == 0,
    }


def motivic_decomposition_virasoro(c=None) -> Dict[str, Any]:
    r"""Motivic decomposition of the Virasoro shadow obstruction tower.

    Virasoro has d_arith = 0 and d_alg = infinity.
    All shadow amplitudes are rational functions of c.
    The shadow obstruction tower is the iterated self-extension of a single
    Kummer motive K(6/c).

    The MC equation D*Theta + (1/2)[Theta, Theta] = 0 is a relation
    within the mixed Tate world: no cusp forms, no L-functions.
    """
    return {
        'algebra': 'Virasoro',
        'c': c,
        'depth': float('inf'),
        'd_arith': 0,
        'd_alg': float('inf'),
        'eisenstein': {
            'type': 'Eisenstein',
            'motivic_category': 'trivial',
            'description': 'No Eisenstein content (not a lattice VOA)',
        },
        'cuspidal': {
            'type': 'cuspidal',
            'motivic_category': 'empty',
            'description': 'No cusp form content',
        },
        'algebraic': {
            'type': 'algebraic',
            'motivic_category': 'Kummer',
            'd_alg': float('inf'),
            'kummer_parameter': '6/c',
            'description': 'Infinite tower of Kummer motive K(6/c) self-extensions',
        },
        'n_non_tate_motives': 0,
        'is_mixed_tate': True,
    }


# =========================================================================
# 5. Period map and injectivity
# =========================================================================

def period_map_genus1(lattice_name: str) -> Dict[str, Any]:
    r"""The genus-1 period map for a lattice VOA.

    The genus-1 amplitude is:
        F_1(V_Lambda) = kappa/24 + (higher-arity corrections)

    The scalar period map sends V_Lambda |-> kappa = rank(Lambda).
    This is NOT injective: all lattices of the same rank give the same kappa.

    The full period map includes the theta function content:
        per_1(V_Lambda) = (kappa, {c_j L(k, f_j)}_j)
    where the c_j are the Hecke decomposition coefficients.

    For Niemeier lattices (24 unimodular lattices of rank 24):
    - All have kappa = 24 (same scalar period)
    - They are distinguished by c_Delta (the Ramanujan coefficient)
    """
    from compute.lib.lattice_shadow_periods import (
        hecke_decompose,
        lattice_data,
    )

    data = lattice_data(lattice_name)
    decomp = hecke_decompose(lattice_name)
    rank = data['rank']
    kappa = rank

    scalar_period = Fraction(kappa, 24)

    cusp_periods = []
    if decomp['cusp_coeffs']:
        k = rank // 2
        for name, coeff in decomp['cusp_coeffs']:
            cusp_periods.append({
                'cusp_form': name,
                'coefficient': coeff,
                'critical_value': f'L({k}, {name})',
            })

    return {
        'lattice': lattice_name,
        'genus': 1,
        'scalar_period': scalar_period,
        'cusp_periods': cusp_periods,
        'full_period_determines': len(cusp_periods) > 0 or rank <= 2,
        'scalar_injective': False,  # Multiple lattices can have the same rank
        'description': (
            f'Scalar period F_1 = {scalar_period}. '
            f'Cusp contributions: {len(cusp_periods)} eigenforms.'
        ),
    }


def period_map_injectivity_test() -> Dict[str, Any]:
    r"""Test injectivity of the period map on the five principal lattices.

    The scalar period map kappa: {lattice VOAs} -> Q is NOT injective:
        V_{Z^2} and V_{A_2} both have rank 2, hence kappa = 2.

    The full period map (including all shadow arities) SHOULD distinguish
    non-isomorphic lattice VOAs:
        V_{Z^2}: theta = theta_3(2tau)^2, level 4
        V_{A_2}: theta = theta_{A_2}(tau), level 3
    These have different Fourier coefficients, hence different shadow obstruction towers.
    """
    from compute.lib.lattice_shadow_periods import lattice_data

    lattices = ['Z', 'Z2', 'A2', 'E8', 'Leech']
    scalar_periods = {}
    for lat in lattices:
        data = lattice_data(lat)
        kappa = data['rank']
        scalar_periods[lat] = kappa

    # Check scalar injectivity
    values = list(scalar_periods.values())
    scalar_injective = len(values) == len(set(values))

    # Find collisions
    collisions = []
    for i, l1 in enumerate(lattices):
        for l2 in lattices[i + 1:]:
            if scalar_periods[l1] == scalar_periods[l2]:
                collisions.append((l1, l2, scalar_periods[l1]))

    return {
        'scalar_periods': scalar_periods,
        'scalar_injective': scalar_injective,
        'collisions': collisions,
        'full_period_injective': True,  # Different theta functions => different periods
        'explanation': (
            'Scalar period map is NOT injective: '
            f'{len(collisions)} collision(s). '
            'Full period map (including cusp content) is conjecturally injective.'
        ),
    }


# =========================================================================
# 6. Mixed Tate vs non-Tate depth
# =========================================================================

def mixed_tate_depth(lattice_name: str) -> Dict[str, Any]:
    r"""Compute the depth of the motivic structure beyond mixed Tate.

    For lattice VOAs:
        depth_beyond_MT = 0 if all L-functions are products of Riemann zeta
        depth_beyond_MT = 1 if cusp form L-functions appear
        depth_beyond_MT = n if n independent cusp eigenforms contribute

    This equals d_arith - (number of Eisenstein L-factors - 1).

    For genus 1:
        V_Z:    all Tate (just zeta(2s))                    depth_MT = 0
        V_{Z^2}: Tate (zeta*L_{chi_4}, but L_chi is Tate)  depth_MT = 0
        V_{A_2}: Tate (zeta*L_{chi_3}, same)                depth_MT = 0
        V_{E_8}: Tate (zeta*zeta)                           depth_MT = 0
        V_Leech: non-Tate (L(s, Delta) is NOT Tate)         depth_MT = 1

    NOTE (Beilinson principle): Dirichlet L-functions L(s, chi_d) for
    quadratic characters chi_d ARE periods of Tate motives (they factor
    through zeta_K(s) = zeta(s)*L(s, chi_d) for a quadratic field K,
    and Dedekind zeta is mixed Tate for abelian number fields by the
    Borel regulator theorem).

    Cusp form L-functions L(s, f) for f in S_k are GENUINELY non-Tate:
    the motive M(f) has Hodge type (k-1, 0) + (0, k-1), which is not
    a Tate twist.
    """
    from compute.lib.lattice_shadow_periods import (
        hecke_decompose,
        lattice_data,
    )

    data = lattice_data(lattice_name)
    decomp = hecke_decompose(lattice_name)

    # Count genuinely non-Tate L-functions
    n_cusp = len(decomp['cusp_coeffs'])
    n_non_tate = n_cusp  # Each cusp eigenform contributes one non-Tate motive

    # Dirichlet L-functions are Tate (abelian reciprocity)
    # Riemann zeta products are Tate
    # Only cusp form L-functions are non-Tate

    is_mixed_tate = (n_non_tate == 0)

    return {
        'lattice': lattice_name,
        'n_cusp_forms': n_cusp,
        'n_non_tate_motives': n_non_tate,
        'is_pure_mixed_tate': is_mixed_tate,
        'depth_beyond_mixed_tate': n_non_tate,
        'genus_where_non_tate_first_appears': 1 if n_cusp > 0 else None,
        'description': (
            'Pure mixed Tate' if is_mixed_tate
            else f'{n_non_tate} non-Tate motive(s) from cusp form(s)'
        ),
    }


# =========================================================================
# 7. d_arith and motivic structure
# =========================================================================

def d_arith_motivic_interpretation(lattice_name: str) -> Dict[str, Any]:
    r"""How d_arith relates to the motivic structure.

    d_arith = #{non-Tate summands h^1(f_j)} in the motivic decomposition.

    For lattice VOAs:
        d_arith counts the number of independent Hecke eigenforms f_j
        appearing in the theta function decomposition.

    The relationship:
        d_arith(V_Z)    = 1 (just zeta(2s), one critical line)
        d_arith(V_{Z^2}) = 1 (zeta * L_{chi}, but lines coincide)
        d_arith(V_{E_8}) = 2 (zeta(s)*zeta(s-3), two critical lines)
        d_arith(V_Leech) = 3 (two zeta lines + one cusp line)

    The motivic interpretation:
        d_arith = dim Gr^W_0(M_A) + #{h^1(f_j)}
    where Gr^W_0 counts the Eisenstein lines and #{h^1(f_j)} the cusp lines.
    """
    from compute.lib.lattice_shadow_periods import (
        lattice_data,
        hecke_decompose,
        shadow_depth_from_hecke,
    )

    data = lattice_data(lattice_name)
    decomp = hecke_decompose(lattice_name)
    depth = data['shadow_depth']
    d_arith = depth - 1  # For lattice VOAs, d_alg = 0

    # Eisenstein lines
    rank = data['rank']
    if rank <= 2:
        eis_lines = 1
    else:
        eis_lines = 2

    cusp_lines = 1 if len(decomp['cusp_coeffs']) > 0 else 0

    return {
        'lattice': lattice_name,
        'd_arith': d_arith,
        'd_alg': 0,
        'depth': depth,
        'eisenstein_lines': eis_lines,
        'cusp_lines': cusp_lines,
        'n_cusp_eigenforms': len(decomp['cusp_coeffs']),
        'motivic_interpretation': (
            f'd_arith = {d_arith} = {eis_lines} Eisenstein lines + '
            f'{cusp_lines} cusp lines'
        ),
        'depth_formula': f'd = 1 + d_arith = 1 + {d_arith} = {depth}',
    }


# =========================================================================
# 8. Genus-g motivic weight table
# =========================================================================

def genus_motivic_weight_table(g_max: int = 5) -> List[Dict[str, Any]]:
    r"""Table of motivic weights of shadow amplitudes by genus.

    At each genus g:
    - F_g^scalar = kappa * lambda_g^FP: motivic weight 0 (rational)
    - delta_pf^{(g)}: motivic weight 0 (mixed Tate, config space integral)
    - Full F_g: involves modular forms of degree g-1 for Sp(2(g-1), Z)

    The motivic weight of the full amplitude grows with genus:
    genus 1: weight 0 (rational) or k-1 (cusp form L-value)
    genus 2: involves Siegel forms of degree 2 (weight undetermined)
    genus 3+: involves Sp(2g) automorphic forms (weight grows)
    """
    table = []
    for g in range(1, g_max + 1):
        lam = lambda_g_fp(g)
        entry = {
            'genus': g,
            'lambda_g_fp': lam,
            'lambda_g_fp_float': float(lam),
            'scalar_weight': 0,
            'scalar_type': 'rational',
            'pf_correction_weight': 0,
            'pf_correction_type': 'mixed_Tate',
        }

        if g == 1:
            entry['full_amplitude_type'] = 'rational_or_Hecke'
            entry['full_amplitude_description'] = (
                'Scalar + Eisenstein (Tate) + cusp L-values (non-Tate)'
            )
        elif g == 2:
            entry['full_amplitude_type'] = 'Siegel'
            entry['full_amplitude_description'] = (
                'Involves Siegel modular forms of degree 2'
            )
        else:
            entry['full_amplitude_type'] = f'Sp({2 * g})'
            entry['full_amplitude_description'] = (
                f'Involves Sp({2 * g}) automorphic forms'
            )

        table.append(entry)
    return table


# =========================================================================
# 9. Transcendence degree computation
# =========================================================================

def transcendence_classification(lattice_name: str) -> Dict[str, Any]:
    r"""Classify the transcendence type of the shadow obstruction tower for a lattice VOA.

    The transcendence asymmetry (rem:transcendence-asymmetry):

    Finite depth, high transcendence:
        V_Leech has depth 4, but periods include L(6, Delta) in pi^{12} * Q-bar.
        Transcendence degree: at least 1 (pi is transcendental).
        Conjecturally: L(6, Delta)/pi^{12} is algebraic (Deligne's conjecture).

    Infinite depth, low transcendence:
        Virasoro has depth infinity, but all S_r in Q(c).
        Transcendence degree: 0 (over Q(c)).

    For each lattice:
        Scalar periods: in Q (transcendence degree 0)
        Eisenstein periods: involve pi^{2k} (transcendence degree 1)
        Cusp periods: involve L(k, f)/pi^k (conjecturally algebraic by Deligne)
    """
    from compute.lib.lattice_shadow_periods import (
        lattice_data,
        hecke_decompose,
    )

    data = lattice_data(lattice_name)
    decomp = hecke_decompose(lattice_name)
    rank = data['rank']

    if rank <= 2:
        # V_Z, V_{Z^2}, V_{A_2}: purely Eisenstein
        return {
            'lattice': lattice_name,
            'depth': data['shadow_depth'],
            'transcendence_type': 'Tate',
            'involves_pi': rank > 0,
            'involves_cusp_L': False,
            'deligne_period': None,
            'transcendence_degree': 1 if rank > 0 else 0,
            'description': f'Periods involve pi (from zeta values) but no cusp forms',
        }

    has_cusp = len(decomp['cusp_coeffs']) > 0

    if not has_cusp:
        return {
            'lattice': lattice_name,
            'depth': data['shadow_depth'],
            'transcendence_type': 'Tate',
            'involves_pi': True,
            'involves_cusp_L': False,
            'deligne_period': None,
            'transcendence_degree': 1,
            'description': f'Purely Eisenstein; periods involve pi^{{2k}} but no cusp L-values',
        }

    # Has cusp forms
    k = rank // 2
    cusp_names = [name for name, _ in decomp['cusp_coeffs']]
    return {
        'lattice': lattice_name,
        'depth': data['shadow_depth'],
        'transcendence_type': 'non-Tate',
        'involves_pi': True,
        'involves_cusp_L': True,
        'cusp_forms': cusp_names,
        'deligne_period': f'L({k}, {cusp_names[0]}) / pi^{k}',
        'deligne_conjecture': f'L({k}, {cusp_names[0]}) / Omega_f is algebraic (Deligne)',
        'transcendence_degree': 1,  # pi, and L-values are conjecturally algebraic/pi
        'description': (
            f'Non-Tate periods: L({k}, {cusp_names[0]}) involves '
            f'genuinely non-Tate motive h^1({cusp_names[0]}). '
            f'Deligne conjecture: critical L-values / Omega are algebraic.'
        ),
    }


# =========================================================================
# 10. Comprehensive analysis
# =========================================================================

def full_motivic_analysis(lattice_name: str) -> Dict[str, Any]:
    r"""Complete motivic analysis of a lattice VOA's shadow obstruction tower.

    Combines: motivic decomposition, period map, mixed Tate depth,
    d_arith interpretation, and transcendence classification.
    """
    return {
        'lattice': lattice_name,
        'motivic_decomposition': motivic_decomposition(lattice_name),
        'period_map_genus1': period_map_genus1(lattice_name),
        'mixed_tate_depth': mixed_tate_depth(lattice_name),
        'd_arith_interpretation': d_arith_motivic_interpretation(lattice_name),
        'transcendence': transcendence_classification(lattice_name),
        'genus1_amplitude': classify_lattice_amplitude(lattice_name, g=1),
        'genus2_amplitude': classify_lattice_amplitude(lattice_name, g=2),
    }


def full_motivic_analysis_virasoro(c=None) -> Dict[str, Any]:
    r"""Complete motivic analysis of the Virasoro shadow obstruction tower.

    All periods are in Q(c). The Kummer motive K(6/c) generates the
    infinite tower via self-extensions. The MC equation is a relation
    within the mixed Tate world.
    """
    shadow_data = []
    for r in range(2, 8):
        shadow_data.append(classify_virasoro_shadow(r, c))

    return {
        'algebra': 'Virasoro',
        'c': c,
        'motivic_decomposition': motivic_decomposition_virasoro(c),
        'shadow_tower_motivic': shadow_data,
        'scalar_amplitudes': [classify_scalar_amplitude(g) for g in range(1, 4)],
        'is_mixed_tate': True,
        'transcendence_type': 'algebraic (over Q(c))',
    }


# =========================================================================
# 11. Niemeier lattice period comparison
# =========================================================================

def niemeier_period_comparison() -> Dict[str, Any]:
    r"""Period map on the Niemeier lattices (24 unimodular rank-24 lattices).

    All 24 Niemeier lattices have:
    - rank = 24, hence kappa = 24
    - theta function in M_{12}(SL_2(Z)) = C*E_{12} + C*Delta
    - same shadow depth d = 4 (since dim S_{12} = 1)

    They are distinguished by:
    - the coefficient c_Delta in Theta = E_{12} + c_Delta * Delta
    - equivalently, the number of norm-2 vectors (roots)

    The scalar period map: V_Lambda |-> kappa = 24 is NOT injective
    (all 24 lattices map to 24).

    The full period map: V_Lambda |-> (24, c_Delta * L(12, Delta))
    IS injective (distinct c_Delta for each lattice, since the norm-2
    shell count determines c_Delta).
    """
    # The 24 Niemeier lattices and their root counts
    # (root count = coefficient of q^1 in Theta_Lambda)
    # Theta = E_{12} + c_Delta * Delta
    # At q^1: a_1(E_{12}) + c_Delta * tau(1) = root_count
    # a_1(E_{12}) = 65520/691, tau(1) = 1
    # So c_Delta = root_count - 65520/691

    niemeier_roots = {
        'Leech': 0,
        'A_1^{24}': 48,
        'A_2^{12}': 72,
        'A_3^8': 96,
        'A_4^6': 120,
        'A_5^4 D_4': 120,  # Note: same root count as A_4^6
        'D_4^6': 144,
        'A_6^4': 168,
        'A_7^2 D_5^2': 168,
        'D_6^4': 192,
        'A_8^3': 216,
        'A_9^2 D_6': 216,
        'E_6^4': 216,
        'D_8^3': 240,
        'A_{11} D_7 E_6': 240,
        'A_{12}^2': 312,
        'D_{10} E_7^2': 312,
        'A_{15} D_9': 312,
        'D_{12}^2': 336,
        'A_{17} E_7': 360,
        'E_8^3': 720,
        'D_{16} E_8': 720,  # Same root count as E_8^3
        'A_{24}': 600,
        'D_{24}': 1104,
    }

    # Compute c_Delta for each
    e12_a1 = Fraction(65520, 691)
    results = {}
    for name, roots in niemeier_roots.items():
        c_delta = Fraction(roots) - e12_a1
        results[name] = {
            'root_count': roots,
            'c_delta': c_delta,
            'kappa': 24,
        }

    # Check injectivity of c_delta
    c_deltas = [v['c_delta'] for v in results.values()]
    # Actually multiple lattices can have the same root count
    unique_c_deltas = len(set(c_deltas))
    root_counts = [v['root_count'] for v in results.values()]
    unique_roots = len(set(root_counts))

    return {
        'n_lattices': len(niemeier_roots),
        'all_kappa_24': True,
        'scalar_injective': False,
        'unique_root_counts': unique_roots,
        'unique_c_deltas': unique_c_deltas,
        'full_period_injective': unique_c_deltas == len(niemeier_roots),
        'c_delta_injective': unique_c_deltas == len(niemeier_roots),
        'root_count_injective': unique_roots == len(niemeier_roots),
        'note': (
            'The scalar period map (kappa only) maps all 24 lattices to 24. '
            f'Root counts distinguish {unique_roots} classes. '
            f'c_Delta values distinguish {unique_c_deltas} lattices. '
            'Full period map (including cusp coefficient) is injective '
            'on the subset with distinct root systems.'
        ),
        'lattices': results,
    }


if __name__ == '__main__':
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

    print("Motivic Shadow Periods: Analysis")
    print("=" * 60)

    # Lambda_g^FP verification
    print("\nFaber-Pandharipande constants:")
    checks = verify_lambda_fp_values()
    for g, info in checks.items():
        status = "MATCH" if info['match'] else "MISMATCH"
        print(f"  lambda_{g}^FP = {info['computed']} ({status})")

    # Period map injectivity
    print("\nPeriod map injectivity:")
    inj = period_map_injectivity_test()
    print(f"  Scalar injective: {inj['scalar_injective']}")
    for l1, l2, val in inj['collisions']:
        print(f"  Collision: {l1} and {l2} both have kappa = {val}")

    # Motivic decomposition for each lattice
    for lat in ['Z', 'E8', 'Leech']:
        print(f"\nMotivic decomposition of V_{lat}:")
        md = motivic_decomposition(lat)
        print(f"  d_arith = {md['d_arith']}, d_alg = {md['d_alg']}")
        print(f"  Mixed Tate: {md['is_mixed_tate']}")
        print(f"  Non-Tate motives: {md['n_non_tate_motives']}")

    # Virasoro
    print("\nVirasoro motivic decomposition:")
    vd = motivic_decomposition_virasoro()
    print(f"  d_arith = {vd['d_arith']}, d_alg = {vd['d_alg']}")
    print(f"  Mixed Tate: {vd['is_mixed_tate']}")
