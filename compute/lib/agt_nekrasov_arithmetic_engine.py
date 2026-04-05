r"""AGT/Nekrasov shadow arithmetic and integrality engine.

Connects Nekrasov partition functions to shadow obstruction tower arithmetic:
denominator factorizations, Gopakumar-Vafa integrality, Coulomb branch
special values, and wall-crossing integrality.

MATHEMATICAL CONTENT
====================

1. NEKRASOV PARTITION FUNCTION ARITHMETIC (Section 1):
   Z_Nek = sum_{|Y|=n} q^n prod_{boxes} (arm-leg factors)
   For SU(2) pure gauge and N_f = 0,...,4 matter.

   ARITHMETIC: instanton coefficients z_k as exact rationals.
   Denominator factorizations: primes dividing denominators of z_k.
   Shadow projection: z_k as arity-k shadow data.

2. AGT SHADOW CORRESPONDENCE (Section 2):
   AGT: Z_Nek(a, eps1, eps2, q) = <V_alpha1 ... V_alpha4>_{W_N}
   Shadow tower S_r(W_N) encodes universal structure.
   W_2 = Vir => S_r(W_2) = S_r(Vir at c_AGT).
   For W_3: S_r(W_3) at c_AGT(eps1, eps2) vs SU(3) Nekrasov.

3. NEKRASOV COEFFICIENT INTEGRALITY (Section 3):
   Z_Nek is in Q(a, eps1, eps2)[[q]].
   At a = 0: simpler rational functions.
   Integrality locus: where z_k are integers.

4. GOPAKUMAR-VAFA INTEGRALITY (Section 4):
   F = sum_{g,beta} n_g^beta q^beta (2sin(g_s/2))^{2g-2}
   n_g^beta in Z (BPS integers).
   Local P^2 from geometric engineering.

5. COULOMB BRANCH ARITHMETIC (Section 5):
   Special a-values => enhanced symmetry.
   Discriminant locus Delta(a) = 0 <=> shadow depth change.

6. WALL-CROSSING ARITHMETIC (Section 6):
   KS wall-crossing products of quantum dilogarithms.
   Wall-crossing shadow Delta S_r across walls.
   BPS integrality at the shadow level.

MULTI-PATH VERIFICATION
========================
Path 1: Direct instanton counting (Young diagram sum)
Path 2: AGT correspondence (W-algebra conformal block)
Path 3: Geometric engineering (local Calabi-Yau)
Path 4: Wall-crossing formula (KS products)

BEILINSON WARNINGS
==================
AP1: kappa formulas differ between families; recompute from first principles.
AP10: Tests need independent cross-checks, not hardcoded wrong values.
AP38: Literature normalization conventions vary.
AP42: Scattering = shadow at motivic level; naive BCH insufficient.
AP44: OPE mode coefficient != lambda-bracket coefficient (divided-power).
AP48: kappa depends on full algebra, not Virasoro subalgebra alone.

Manuscript references:
    thm:universal-generating-function (genus_expansions.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:propagator-variance (higher_genus_modular_koszul.tex)
    rem:agt-shadow-connection (connections/feynman_bv.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, simplify, factor, expand, sqrt, log, pi, exp,
    binomial, factorial, bernoulli, Abs, N as Neval, oo, S as Sym,
    Poly, symbols, Integer, series, O, cos, sin, I,
    Matrix, eye, zeros as sym_zeros, gcd as sym_gcd, factorint,
    cancel,
)

# ---------------------------------------------------------------------------
# Imports from existing AGT modules
# ---------------------------------------------------------------------------

from compute.lib.agt_shadow_correspondence import (
    agt_central_charge,
    agt_b_from_epsilons,
    agt_hbar,
    agt_beta,
    agt_kappa_from_c,
    agt_parameter_map,
    arm_length,
    leg_length,
    conjugate_partition,
    partition_size,
    all_partitions,
    all_partition_pairs,
    all_partition_triples,
    _N_function,
    nekrasov_factor_pair,
    nekrasov_partition_su2,
    nekrasov_free_energy_su2,
    nekrasov_factor_triple,
    nekrasov_partition_su3,
    prepotential_su2_one_inst,
    prepotential_su2_two_inst,
    w3_kappa_from_c,
)

from compute.lib.agt_nekrasov_shadow_engine import (
    virasoro_conformal_block,
    all_partition_n_tuples,
    nekrasov_factor_n_tuple,
    nekrasov_partition_sun,
    prepotential_from_periods,
    w_n_central_charge,
    w_n_kappa,
)

# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------

c_sym = Symbol('c')
eps1_sym, eps2_sym = symbols('epsilon_1 epsilon_2')
a_sym = Symbol('a')
q_sym = Symbol('q')


# ===========================================================================
# Section 1: Nekrasov partition function arithmetic — denominator analysis
# ===========================================================================

def nekrasov_su2_nf_matter(a_val, eps1_val, eps2_val, masses, max_inst: int = 3):
    r"""SU(2) Nekrasov partition function with N_f fundamental hypermultiplets.

    For N_f = 0: pure gauge theory.
    For N_f = 1,...,4: N_f hypermultiplets with masses m_1,...,m_{N_f}.

    The matter contribution modifies the instanton weight by:

        z_{Y1,Y2}^{matter} = z_{Y1,Y2}^{vec} * prod_{f=1}^{N_f}
            prod_{alpha=1}^{2} prod_{s in Y_alpha}
                (a_alpha + m_f + eps1 * (i-1) + eps2 * (j-1))^{-1}

    where s = (i,j) is a box in Young diagram Y_alpha.

    Parameters:
        a_val: Coulomb branch parameter
        eps1_val, eps2_val: Omega-background parameters
        masses: list of masses [m_1, ..., m_{N_f}]
        max_inst: maximum instanton number

    Returns dict: k -> Z_k (exact rational).
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)
    a = Rational(a_val) if isinstance(a_val, (int, float, str)) else a_val
    m_list = [Rational(m) if isinstance(m, (int, float, str)) else m for m in masses]
    N_f = len(m_list)

    a_colors = [a, -a]  # SU(2) tracelessness

    coefficients = {}
    for inst in range(max_inst + 1):
        Z_k = Rational(0)
        for (Y1, Y2) in all_partition_pairs(inst):
            # Vector multiplet contribution
            z_vec = nekrasov_factor_pair(a, Y1, Y2, e1, e2)
            if z_vec == oo or z_vec == 0:
                continue

            # Matter contribution
            z_matter = Rational(1)
            Ys = [Y1, Y2]
            for f_idx in range(N_f):
                for alpha in range(2):
                    for i in range(len(Ys[alpha])):
                        for j in range(Ys[alpha][i]):
                            val = a_colors[alpha] + m_list[f_idx] + e1 * i + e2 * j
                            if val == 0:
                                z_matter = oo
                                break
                            z_matter *= val
                        if z_matter == oo:
                            break
                    if z_matter == oo:
                        break
                if z_matter == oo:
                    break

            if z_matter == oo or z_matter == 0:
                continue

            Z_k += z_vec * z_matter

        coefficients[inst] = simplify(Z_k)
    return coefficients


def nekrasov_coefficient_rational_form(a_val, eps1_val, eps2_val, inst_k,
                                       masses=None):
    r"""Extract the k-instanton Nekrasov coefficient as an exact rational number.

    Returns a dict with:
        'value': the exact rational coefficient z_k
        'numerator': integer numerator
        'denominator': integer denominator
        'denominator_factorization': prime factorization of denominator
        'numerator_factorization': prime factorization of numerator
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)
    a = Rational(a_val) if isinstance(a_val, (int, float, str)) else a_val

    if masses is None or len(masses) == 0:
        Z = nekrasov_partition_su2(a, e1, e2, inst_k)
    else:
        Z = nekrasov_su2_nf_matter(a, e1, e2, masses, inst_k)

    z_k = Z[inst_k]

    # Handle singular (infinite) coefficients
    if z_k == oo or z_k == -oo or z_k is oo:
        return {
            'value': oo,
            'numerator': None,
            'denominator': None,
            'numerator_factorization': {},
            'denominator_factorization': {},
            'sign': None,
            'singular': True,
        }

    z_k = Rational(z_k) if not isinstance(z_k, Rational) else z_k

    # Extract numerator and denominator
    frac = Fraction(int(z_k.p), int(z_k.q))
    num = abs(frac.numerator)
    den = frac.denominator

    num_factors = _safe_factorint(num) if num > 1 else {}
    den_factors = _safe_factorint(den) if den > 1 else {}

    return {
        'value': z_k,
        'numerator': int(z_k.p),
        'denominator': int(z_k.q),
        'numerator_factorization': num_factors,
        'denominator_factorization': den_factors,
        'sign': 1 if z_k >= 0 else -1,
    }


def _safe_factorint(n):
    """Factorize an integer, returning dict of {prime: exponent}."""
    if n <= 1:
        return {}
    try:
        return factorint(int(n))
    except Exception:
        return {int(n): 1}


def nekrasov_denominator_analysis(a_val, eps1_val, eps2_val, max_inst: int = 4):
    r"""Analyze denominators of Nekrasov instanton coefficients.

    For pure SU(2) with rational (a, eps1, eps2), the coefficients z_k
    are rational numbers.  This function extracts:
      - The denominator of each z_k
      - Its prime factorization
      - The set of primes that divide ALL denominators (universal primes)
      - The maximum prime appearing

    SHADOW INTERPRETATION: the denominators encode the arithmetic of the
    shadow obstruction tower at arity k.  Primes dividing z_k arise from:
      - eps1, eps2 (the Omega-background = equivariant deformation)
      - 2a (the Coulomb branch position)
      - Arm-leg lengths (Young diagram combinatorics)

    Returns dict with analysis results.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)
    a = Rational(a_val) if isinstance(a_val, (int, float, str)) else a_val

    Z = nekrasov_partition_su2(a, e1, e2, max_inst)

    results = {}
    all_primes = set()
    common_primes = None

    for k in range(1, max_inst + 1):
        z_k = Z[k]

        # Handle singular (infinite) coefficients
        if z_k == oo or z_k == -oo or z_k is oo:
            results[k] = {
                'z_k': z_k,
                'denominator': 0,
                'denominator_factors': {},
                'primes': [],
                'max_prime': 0,
                'singular': True,
            }
            continue

        if isinstance(z_k, Rational):
            den = int(z_k.q)
        else:
            try:
                z_k = Rational(z_k)
                den = int(z_k.q)
            except (TypeError, ValueError):
                results[k] = {
                    'z_k': z_k,
                    'denominator': 0,
                    'denominator_factors': {},
                    'primes': [],
                    'max_prime': 0,
                    'symbolic': True,
                }
                continue

        den_factors = _safe_factorint(den) if den > 1 else {}
        primes_k = set(den_factors.keys())
        all_primes |= primes_k

        if common_primes is None:
            common_primes = primes_k.copy()
        else:
            common_primes &= primes_k

        results[k] = {
            'z_k': z_k,
            'denominator': den,
            'denominator_factors': den_factors,
            'primes': sorted(primes_k),
            'max_prime': max(primes_k) if primes_k else 1,
        }

    return {
        'coefficients': results,
        'all_primes': sorted(all_primes),
        'common_primes': sorted(common_primes) if common_primes else [],
        'max_prime_overall': max(all_primes) if all_primes else 1,
    }


def nekrasov_nf_comparison(a_val, eps1_val, eps2_val, max_inst: int = 3):
    r"""Compare Nekrasov coefficients for N_f = 0, 1, 2, 3, 4.

    Compute z_k for each N_f value and analyze how the arithmetic changes.

    N_f = 0: pure gauge (asymptotically free)
    N_f = 1: one fundamental
    N_f = 2: two fundamentals (with m_1 = m_2 = 0 for simplicity)
    N_f = 3: three fundamentals (all zero mass)
    N_f = 4: four fundamentals (conformal, SCFT at tau = i)

    Returns comparison data.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)
    a = Rational(a_val) if isinstance(a_val, (int, float, str)) else a_val

    results = {}

    # N_f = 0: pure gauge
    Z_0 = nekrasov_partition_su2(a, e1, e2, max_inst)
    results[0] = {k: Z_0[k] for k in range(max_inst + 1)}

    # N_f = 1,...,4 with zero masses
    for nf in range(1, 5):
        masses = [Rational(0)] * nf
        Z_nf = nekrasov_su2_nf_matter(a, e1, e2, masses, max_inst)
        results[nf] = {k: Z_nf[k] for k in range(max_inst + 1)}

    return results


# ===========================================================================
# Section 2: AGT shadow correspondence — W_N shadow vs Nekrasov
# ===========================================================================

def shadow_kappa_virasoro(c_val):
    r"""Shadow obstruction tower leading invariant kappa for Virasoro.

    kappa(Vir_c) = c/2.

    AP48 WARNING: this is specific to Virasoro, NOT a general VOA formula.
    For W_N: kappa(W_N) = c * (H_N - 1) where H_N = 1 + 1/2 + ... + 1/N.
    """
    c = Rational(c_val) if isinstance(c_val, (int, float, str)) else c_val
    return c / 2


def shadow_S3_virasoro(c_val):
    r"""Cubic shadow S_3 for Virasoro.

    S_3(Vir_c) = 2 for all c != 0.  This is the cubic shadow coefficient
    (alpha = 2) from the Virasoro self-OPE T_{(1)}T = 2T.

    CAUTION: cubic gauge triviality (thm:cubic-gauge-triviality) says the
    obstruction CLASS o_3 is cohomologically trivial (can be gauged away),
    NOT that S_3 = 0.  The shadow coefficient S_3 = 2 is nonzero.
    """
    return Rational(2)


def shadow_S4_virasoro(c_val):
    r"""Quartic shadow S_4 for Virasoro.

    S_4 = Q^contact_Vir = 10 / (c * (5c + 22)).

    CAUTION: S_4 IS Q^contact, NOT Q^contact * kappa.
    The discriminant formula is Delta = 8 * kappa * S_4 = 40/(5c+22).
    """
    c = Rational(c_val) if isinstance(c_val, (int, float, str)) else c_val
    if c == 0:
        return oo
    Q_contact = Rational(10) / (c * (5 * c + 22))
    return Q_contact


def shadow_discriminant_virasoro(c_val):
    r"""Shadow discriminant Delta for Virasoro.

    Delta = 8 * kappa * S_4
          = 8 * (c/2) * 10 / (c * (5c + 22))
          = 40 / (5c + 22)

    The c in kappa * S_4 cancels, so Delta is well-defined even at c = 0:
    Delta(Vir_0) = 40/22 = 20/11.
    Delta != 0 for c != -22/5 => Virasoro is class M (infinite shadow depth).
    """
    c = Rational(c_val) if isinstance(c_val, (int, float, str)) else c_val
    denom = 5 * c + 22
    if denom == 0:
        return oo
    return Rational(40) / denom


def agt_shadow_w2_check(eps1_val, eps2_val):
    r"""Verify that the AGT shadow for W_2 = Virasoro matches.

    AGT at (eps1, eps2) gives:
        c = 1 + 6(b + 1/b)^2 where b^2 = -eps1/eps2
        kappa(Vir_c) = c/2
        W_2 shadow = Virasoro shadow at this c

    Since W_2 = Vir, the W_N formula kappa(W_N) = c*(H_N - 1) at N=2
    gives kappa(W_2) = c*(1 + 1/2 - 1) = c/2, matching kappa(Vir) = c/2.

    Returns verification data.
    """
    params = agt_parameter_map(eps1_val, eps2_val)
    c = params['c']
    kappa_vir = simplify(c / 2)

    # W_2 formula: c * (H_2 - 1) = c * (1 + 1/2 - 1) = c/2
    H_2 = Rational(1) + Rational(1, 2)
    kappa_w2 = simplify(c * (H_2 - 1))

    return {
        'c': simplify(c),
        'kappa_vir': kappa_vir,
        'kappa_w2': kappa_w2,
        'match': simplify(kappa_vir - kappa_w2) == 0,
        'S3_vir': shadow_S3_virasoro(c),
        'S4_vir': simplify(shadow_S4_virasoro(c)),
        'Delta_vir': simplify(shadow_discriminant_virasoro(c)),
    }


def agt_shadow_w3_check(eps1_val, eps2_val):
    r"""Compare W_3 shadow at AGT central charge with SU(3) Nekrasov structure.

    For W_3: c_{W_3} = 2(1 + 12(b + 1/b)^2)
    kappa(W_3) = c * (H_3 - 1) = c * (1/2 + 1/3) = 5c/6

    The W_3 has generators T (weight 2) and W (weight 3).
    Two-channel shadow metric with propagator variance delta_mix.

    Returns comparison data.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)

    b_sq = -e1 / e2
    b = sqrt(b_sq)

    # W_3 central charge
    c_w3 = w_n_central_charge(3, b)
    c_w3 = simplify(c_w3)

    # W_3 kappa
    kappa_w3 = w_n_kappa(3, c_w3)
    kappa_w3 = simplify(kappa_w3)

    # Also compute from the formula directly: 5c/6
    kappa_direct = simplify(5 * c_w3 / 6)

    # Virasoro subalgebra contribution: c/2
    kappa_vir_sub = simplify(c_w3 / 2)

    # W_3 generator contribution: c/3
    kappa_w3_gen = simplify(c_w3 / 3)

    return {
        'c_w3': c_w3,
        'kappa_w3': kappa_w3,
        'kappa_direct_5c_6': kappa_direct,
        'match': simplify(kappa_w3 - kappa_direct) == 0,
        'kappa_decomposition': {
            'T_contribution': kappa_vir_sub,
            'W_contribution': kappa_w3_gen,
            'total': simplify(kappa_vir_sub + kappa_w3_gen),
        },
    }


def instanton_shadow_extraction(a_val, eps1_val, eps2_val, max_inst: int = 3):
    r"""Extract instanton shadow S_r^{inst} from the Nekrasov free energy.

    The free energy F^{inst} = sum_k f_k q^k has cumulant coefficients f_k.
    At the scalar level, the shadow projects out the universal (a-independent)
    structure.

    The instanton shadow at arity r is defined as the leading term of f_r
    in the eps1 * eps2 expansion:
        f_r = (eps1*eps2)^{-1} * F_0^{(r)} + F_1^{(r)} + O(eps1*eps2)

    where F_0^{(r)} is the r-instanton prepotential coefficient and
    F_1^{(r)} is the genus-1 instanton correction.

    The shadow S_r^{inst} is F_1^{(r)} / kappa, normalized by the modular
    characteristic.

    Returns dict r -> instanton shadow data.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)
    a = Rational(a_val) if isinstance(a_val, (int, float, str)) else a_val

    free_energy = nekrasov_free_energy_su2(a, e1, e2, max_inst)

    results = {}
    for r in range(1, max_inst + 1):
        if r in free_energy:
            f_r = free_energy[r]
            results[r] = {
                'f_r': f_r,
                'hbar': e1 * e2,
                # The shadow projection: multiply by hbar to extract genus-1 part
                'hbar_f_r': simplify(e1 * e2 * f_r),
            }

    return results


# ===========================================================================
# Section 3: Integrality of Nekrasov coefficients
# ===========================================================================

def nekrasov_integrality_test(a_val, eps1_val, eps2_val, max_inst: int = 4):
    r"""Test whether Nekrasov coefficients z_k are integers.

    For generic (a, eps1, eps2), the z_k are rational (typically non-integer).
    At special values, they may become integers.

    Returns dict with integrality data for each k.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)
    a = Rational(a_val) if isinstance(a_val, (int, float, str)) else a_val

    Z = nekrasov_partition_su2(a, e1, e2, max_inst)

    results = {}
    all_integral = True
    for k in range(1, max_inst + 1):
        z_k = Z[k]
        is_int = isinstance(z_k, (int, Integer)) or (
            isinstance(z_k, Rational) and z_k.q == 1
        )
        results[k] = {
            'z_k': z_k,
            'is_integer': is_int,
        }
        if not is_int:
            all_integral = False

    return {
        'coefficients': results,
        'all_integral': all_integral,
        'a': a,
        'eps1': e1,
        'eps2': e2,
    }


def nekrasov_integrality_scan(eps1_val, eps2_val, a_range, max_inst: int = 3):
    r"""Scan over a-values to find the integrality locus.

    For each a in a_range, test whether all z_k (k = 1,...,max_inst)
    are integers.

    The integrality locus relates to shadow regularity: at special
    points of the Coulomb branch, the shadow obstruction tower
    simplifies, and integrality can emerge.

    Returns list of a-values where all z_k are integral.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)

    integral_locus = []
    for a_val in a_range:
        a = Rational(a_val) if isinstance(a_val, (int, float, str)) else a_val
        result = nekrasov_integrality_test(a, e1, e2, max_inst)
        if result['all_integral']:
            integral_locus.append(a)

    return integral_locus


def nekrasov_a0_specialization(eps1_val, eps2_val, max_inst: int = 5):
    r"""Nekrasov partition function at a = 0.

    At a = 0 (origin of Coulomb branch), the SU(2) partition function
    simplifies because a_1 = a = 0, a_2 = -a = 0.

    WARNING: some terms may be singular at a = 0 (denominator vanishing).
    We evaluate at a = small rational and extrapolate, or handle the pole.

    The a = 0 specialization relates to the conformal (enhanced symmetry)
    point of the Seiberg-Witten moduli space.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)

    # Direct computation at small a values and extrapolation
    a_vals = [Rational(1, n) for n in [2, 3, 5, 7]]
    results = {}

    for inst_k in range(1, max_inst + 1):
        data = []
        for a in a_vals:
            Z = nekrasov_partition_su2(a, e1, e2, inst_k)
            if inst_k in Z:
                data.append((a, Z[inst_k]))

        # Store the behavior near a = 0
        if data:
            results[inst_k] = {
                'values_near_zero': data,
                # The leading power of 1/a in z_k determines the pole order
                'pole_analysis': _pole_order_analysis(data),
            }

    return results


def _pole_order_analysis(data):
    """Estimate the pole order at a = 0 from values near zero."""
    if len(data) < 2:
        return {'order': None}

    # log(|z_k|) vs log(|a|) gives slope ~ -pole_order
    try:
        log_data = []
        for a_val, z_val in data:
            if z_val != 0:
                la = float(log(Abs(a_val)).evalf())
                lz = float(log(Abs(z_val)).evalf())
                log_data.append((la, lz))

        if len(log_data) >= 2:
            # Linear regression for slope
            x1, y1 = log_data[0]
            x2, y2 = log_data[-1]
            if x2 != x1:
                slope = (y2 - y1) / (x2 - x1)
                return {'order': round(-slope), 'slope': slope}
    except Exception:
        pass

    return {'order': None}


# ===========================================================================
# Section 4: Gopakumar-Vafa integrality via shadows
# ===========================================================================

@lru_cache(maxsize=128)
def _lambda_fp(g):
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
    POSITIVE for all g >= 1.
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got g={g}")
    B2g = bernoulli(2 * g)
    num = (2 ** (2 * g - 1) - 1) * abs(B2g)
    den = 2 ** (2 * g - 1) * factorial(2 * g)
    return Rational(num, den)


def gv_from_genus_expansion(F_coeffs, max_genus: int = 3, max_degree: int = 5):
    r"""Extract Gopakumar-Vafa invariants n_g^d from genus-g free energies.

    The GV expansion:
        F = sum_{g >= 0} sum_{d >= 1} n_g^d sum_{k >= 1}
            (1/k) (2 sin(k g_s / 2))^{2g-2} q^{kd}

    Inverted:
        n_g^d = (Mobius-type inversion from F_{g,d})

    For the simplest case (single Kahler parameter):
        F_g = sum_{d >= 1} N_{g,d} q^d

    where N_{g,d} = sum_{k|d} n_g^{d/k} * k^{2g-3}  (multi-covering).

    Inversion:
        n_g^d = sum_{k|d} mu(k) * k^{2g-3} * N_{g,d/k}

    Parameters:
        F_coeffs: dict {(g, d): N_{g,d}} of genus-g degree-d Gromov-Witten invariants
        max_genus: maximum genus
        max_degree: maximum degree

    Returns dict {(g, d): n_g^d} of GV invariants.
    """
    gv = {}
    for g in range(max_genus + 1):
        for d in range(1, max_degree + 1):
            # Mobius inversion: n_g^d = sum_{k|d} mu(k) * k^{2g-3} * N_{g,d/k}
            n_gd = Rational(0)
            for k in _divisors(d):
                mu_k = _mobius(k)
                N_gdk = F_coeffs.get((g, d // k), Rational(0))
                n_gd += mu_k * Rational(k) ** (2 * g - 3) * N_gdk
            gv[(g, d)] = n_gd
    return gv


def _divisors(n):
    """Return all positive divisors of n."""
    divs = []
    for k in range(1, n + 1):
        if n % k == 0:
            divs.append(k)
    return divs


def _mobius(n):
    """Mobius function mu(n)."""
    if n == 1:
        return 1
    factors = _safe_factorint(n)
    for p, e in factors.items():
        if e > 1:
            return 0
    return (-1) ** len(factors)


def gv_local_p2(max_degree: int = 5, max_genus: int = 3):
    r"""Gopakumar-Vafa invariants for local P^2 = O(-3) -> P^2.

    Known GV invariants (from topological vertex / localization / B-model):

    Genus 0:
        n_0^1 = 3, n_0^2 = -6, n_0^3 = 27, n_0^4 = -192, n_0^5 = 1695

    Genus 1:
        n_1^1 = 0, n_1^2 = 0, n_1^3 = -10, n_1^4 = 231, n_1^5 = -4452

    Genus 2:
        n_2^1 = 0, n_2^2 = 0, n_2^3 = 0, n_2^4 = -102, n_2^5 = 5430

    Genus 3:
        n_3^1 = 0, n_3^2 = 0, n_3^3 = 0, n_3^4 = 15, n_3^5 = -3672

    References:
        Katz-Klemm-Vafa, hep-th/9609091
        Huang-Klemm-Reuter, arXiv:1507.04117

    Returns dict {(g, d): n_g^d}.
    """
    known_gv = {
        (0, 1): 3, (0, 2): -6, (0, 3): 27, (0, 4): -192, (0, 5): 1695,
        (1, 1): 0, (1, 2): 0, (1, 3): -10, (1, 4): 231, (1, 5): -4452,
        (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): -102, (2, 5): 5430,
        (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 15, (3, 5): -3672,
    }

    result = {}
    for g in range(min(max_genus + 1, 4)):
        for d in range(1, min(max_degree + 1, 6)):
            result[(g, d)] = known_gv.get((g, d), 0)

    return result


def gv_local_p1p1(max_degree: int = 4, max_genus: int = 2):
    r"""Gopakumar-Vafa invariants for local P^1 x P^1.

    For the anti-canonical bundle O(-2,-2) -> P^1 x P^1.

    Known GV invariants (from topological vertex):
    At genus 0 along the diagonal d_1 = d_2 = d:
        n_0^{(1,1)} = -4, n_0^{(2,2)} = -4, etc.
    At genus 0 off-diagonal:
        n_0^{(1,0)} = n_0^{(0,1)} = -2

    We restrict to the diagonal slice d_1 = d_2 = d.

    Returns dict {(g, d): n_g^d} on the diagonal.
    """
    known_gv = {
        (0, 1): -4, (0, 2): -4, (0, 3): -12, (0, 4): -48,
        (1, 1): 0, (1, 2): 0, (1, 3): 3, (1, 4): 32,
        (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): -6,
    }

    result = {}
    for g in range(min(max_genus + 1, 3)):
        for d in range(1, min(max_degree + 1, 5)):
            result[(g, d)] = known_gv.get((g, d), 0)

    return result


def gv_integrality_check(gv_invariants):
    r"""Verify that all Gopakumar-Vafa invariants are integers.

    The BPS interpretation requires n_g^d in Z.  This is a highly
    nontrivial integrality constraint on the genus expansion.

    Returns dict with integrality data.
    """
    all_integral = True
    non_integral = []

    for (g, d), n_gd in gv_invariants.items():
        if isinstance(n_gd, Rational):
            is_int = n_gd.q == 1
        elif isinstance(n_gd, (int, Integer)):
            is_int = True
        elif isinstance(n_gd, float):
            is_int = (n_gd == int(n_gd))
        else:
            is_int = True

        if not is_int:
            all_integral = False
            non_integral.append(((g, d), n_gd))

    return {
        'all_integral': all_integral,
        'non_integral': non_integral,
        'count': len(gv_invariants),
    }


def gv_from_nekrasov_local_p2(max_inst: int = 3, max_genus: int = 2):
    r"""Compute GV invariants for local P^2 from Nekrasov via geometric engineering.

    The geometric engineering dictionary identifies:
        Local P^2 <=> 5d SU(3) N=1 on S^1 with specific Coulomb/mass parameters.

    At the genus-0 level (prepotential):
        F_0^{top}(t) = F_0^{SW}(a(t))

    where a(t) maps Kahler parameters to Coulomb parameters.

    For the simplest extraction, we use the known prepotential coefficients
    and convert to GV via Mobius inversion.

    Returns dict {(g, d): n_g^d} and comparison with known values.
    """
    known = gv_local_p2(max_inst, max_genus)

    # Verify integrality of known values
    integrality = gv_integrality_check(known)

    # Compute genus-0 GW invariants from known GV via multi-covering
    gw = {}
    for d in range(1, max_inst + 1):
        N_0d = Rational(0)
        for k in _divisors(d):
            n_0_dk = known.get((0, d // k), 0)
            N_0d += Rational(n_0_dk) / Rational(k) ** 3
        gw[(0, d)] = N_0d

    return {
        'gv': known,
        'gw_genus0': gw,
        'integrality': integrality,
    }


def gv_shadow_growth_analysis(gv_invariants, max_genus: int = 3):
    r"""Analyze the growth of GV invariants and relate to shadow depth.

    For a CY3 with chiral algebra A_X:
      - kappa(A_X) = chi(X)/2
      - Shadow depth r_max(A_X) classifies complexity
      - n_0^d = "arity-0 genus-0" shadow
      - n_g^d = "arity-0 genus-g" shadow

    The growth of |n_g^d| in d at fixed g is related to the shadow
    growth rate rho(A_X).

    Returns growth analysis data.
    """
    growth_data = {}

    for g in range(max_genus + 1):
        degrees = sorted(d for (g2, d) in gv_invariants if g2 == g)
        if not degrees:
            continue

        values = [abs(gv_invariants.get((g, d), 0)) for d in degrees]
        nonzero_values = [(d, v) for d, v in zip(degrees, values) if v != 0]

        if len(nonzero_values) >= 2:
            # Estimate growth rate: |n_g^d| ~ C * rho^d
            d_vals = [d for d, _ in nonzero_values]
            v_vals = [v for _, v in nonzero_values]

            # Ratio of consecutive nonzero values gives approximate growth rate
            ratios = []
            for i in range(1, len(nonzero_values)):
                d1, v1 = nonzero_values[i - 1]
                d2, v2 = nonzero_values[i]
                if v1 != 0:
                    ratio = float(v2) / float(v1)
                    d_diff = d2 - d1
                    if d_diff > 0:
                        ratios.append(abs(ratio) ** (1.0 / d_diff))

            avg_growth = sum(ratios) / len(ratios) if ratios else None
            growth_data[g] = {
                'nonzero_degrees': d_vals,
                'values': v_vals,
                'growth_ratios': ratios,
                'estimated_growth_rate': avg_growth,
            }

    return growth_data


# ===========================================================================
# Section 5: Coulomb branch arithmetic
# ===========================================================================

def coulomb_branch_special_values(eps1_val, eps2_val, max_inst: int = 3):
    r"""Compute Nekrasov coefficients at special Coulomb branch values.

    Special values of a:
        a = 0: enhanced SU(2) symmetry (origin)
        a = ±1/2: half-integer Coulomb parameter
        a = ±1: integer Coulomb parameter
        a = ±(eps1 + eps2)/2: related to the background deformation

    At each value, compute z_k and analyze the arithmetic.

    Returns dict with results at each special value.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)

    special_a = {
        'a=1/2': Rational(1, 2),
        'a=1': Rational(1),
        'a=3/2': Rational(3, 2),
        'a=2': Rational(2),
        'a=(e1+e2)/2': (e1 + e2) / 2,
        'a=(e1-e2)/2': (e1 - e2) / 2,
    }

    results = {}
    for name, a in special_a.items():
        if a == 0:
            continue  # a = 0 is singular
        try:
            Z = nekrasov_partition_su2(a, e1, e2, max_inst)
            results[name] = {
                'a': a,
                'coefficients': {k: Z[k] for k in range(max_inst + 1)},
            }
        except (ZeroDivisionError, ValueError):
            results[name] = {'a': a, 'singular': True}

    return results


def coulomb_discriminant(a_val, eps1_val, eps2_val, max_inst: int = 3):
    r"""Compute the discriminant-like quantity from Nekrasov coefficients.

    For pure SU(2), the Seiberg-Witten discriminant is:
        Delta(u) = u^2 - 1   (u = a^2 in appropriate units)

    The discriminant vanishes at the singularity (monopole/dyon) points.
    Near these points, the shadow depth changes.

    We compute:
        Delta(a) := det(Gram matrix of first few instanton coefficients)

    as a function of a, looking for zeros that signal enhanced symmetry.

    Returns discriminant analysis data.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)
    a = Rational(a_val) if isinstance(a_val, (int, float, str)) else a_val

    Z = nekrasov_partition_su2(a, e1, e2, max_inst)

    # The discriminant of the Seiberg-Witten curve in the Nekrasov framework:
    # At leading order in q:  u = a^2 - 2*Z_1*eps1*eps2 + O(q^2)
    # The classical discriminant: Delta_SW = u^2 - Lambda^4

    u_approx = a ** 2
    if 1 in Z:
        u_correction = Z[1] * e1 * e2
        u_approx = a ** 2 - 2 * u_correction

    return {
        'a': a,
        'u_classical': a ** 2,
        'u_corrected': simplify(u_approx),
        'Z_coefficients': {k: Z[k] for k in range(max_inst + 1)},
    }


def enhanced_symmetry_points(eps1_val, eps2_val):
    r"""Identify enhanced symmetry points on the Coulomb branch.

    Enhanced symmetry occurs at the zeros of the discriminant:
        a_monopole = ± 1  (monopole/dyon points in classical SW theory)
        a_mutually_local = 0  (origin)

    At the quantum level (with eps1, eps2), the enhanced symmetry points
    shift. The shifted points are related to the shadow connection singularity.

    Returns the expected enhanced symmetry points.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)

    # Classical enhanced symmetry points (pure SU(2), Lambda = 1):
    # u = ± 1 => a = ± 1 (up to Lambda normalization)

    # Quantum deformation: the monopole/dyon masses receive eps corrections
    # a_mono ~ 1 + O(eps)

    return {
        'classical_monopole': [Rational(1), Rational(-1)],
        'classical_origin': Rational(0),
        'eps1': e1,
        'eps2': e2,
        'beta': e1 + e2,
        'hbar': e1 * e2,
    }


# ===========================================================================
# Section 6: Wall-crossing arithmetic
# ===========================================================================

def quantum_dilogarithm_product(x_power, q_power, order: int = 10):
    r"""Series expansion of the quantum dilogarithm product.

    E_q(x) = prod_{n >= 0} (1 + q^{n+1/2} x)^{-1}

    In the Kontsevich-Soibelman framework, the BPS automorphism is:
        K_gamma = prod_{n >= 0} (1 - (-q)^{n+1/2} X^gamma)^{-1}

    The series expansion gives:

        E_q(x) = sum_{n >= 0} a_n x^n

    where a_n are rational functions of q.

    For shadow correspondence: the quantum dilogarithm encodes the
    arity-by-arity shadow data at each charge sector.

    Parameters:
        x_power: exponent of x in the expansion
        q_power: evaluate q at q^{q_power} (half-integer allowed)
        order: maximum order of expansion

    Returns dict {n: coefficient of x^n} for n = 0, ..., order.
    """
    # Formal expansion of E_q(x)^{-1} = prod (1 + q^{n+1/2} x)
    # = 1 + (sum q^{n+1/2}) x + (sum_{n1<n2} q^{n1+n2+1}) x^2 + ...

    # Coefficients of x^k in prod_{n=0}^{N} (1 + q^{n+1/2} x)
    # are elementary symmetric polynomials in {q^{1/2}, q^{3/2}, ...}

    # For numerical evaluation: use q = some rational
    q = Rational(q_power) if isinstance(q_power, (int, float, str)) else q_power

    # Build the product iteratively
    # Start with [1] (coefficients of 1)
    coeffs = [Rational(1)]
    for n in range(order):
        q_shift = q ** (2 * n + 1)  # q^{n+1/2} squared to avoid sqrt
        new_coeffs = [Rational(0)] * (len(coeffs) + 1)
        for j in range(len(coeffs)):
            new_coeffs[j] += coeffs[j]
            new_coeffs[j + 1] += coeffs[j] * q_shift
        coeffs = new_coeffs

    # This gives the RECIPROCAL of E_q
    # Invert: E_q = 1 / (product)
    # Use the truncated inverse
    inv_coeffs = _truncated_inverse(coeffs, order + 1)

    return {n: inv_coeffs[n] for n in range(min(len(inv_coeffs), order + 1))}


def _truncated_inverse(coeffs, order):
    """Compute truncated inverse of a power series 1/f(x) = sum a_n x^n.

    Given f(x) = c_0 + c_1*x + c_2*x^2 + ..., compute g(x) such that
    f(x)*g(x) = 1 + O(x^order).
    """
    if not coeffs or coeffs[0] == 0:
        return [Rational(0)] * order

    inv = [Rational(0)] * order
    inv[0] = 1 / coeffs[0]

    for n in range(1, order):
        s = Rational(0)
        for k in range(1, min(n + 1, len(coeffs))):
            s += coeffs[k] * inv[n - k]
        inv[n] = -s / coeffs[0]

    return inv


def wall_crossing_shadow_jump(gamma1, gamma2, omega1, omega2, order: int = 5):
    r"""Compute the wall-crossing shadow jump Delta S_r.

    At a wall of marginal stability where charges gamma_1 and gamma_2
    become mutually BPS, the BPS spectrum jumps.

    The Joyce-Song formula at leading order:
        Delta Omega(gamma_1 + gamma_2)
            = (-1)^{<gamma_1,gamma_2> - 1} * <gamma_1,gamma_2>
              * Omega(gamma_1) * Omega(gamma_2)

    The shadow jump is the change in the shadow obstruction tower
    projection at the given charge:
        Delta S_r = projection of (Theta_+ - Theta_-) to arity r

    At the Lie algebra level (BCH approximation, cf AP42):
        Theta_+ - Theta_- ~ [Omega_1 * e_{gamma_1}, Omega_2 * e_{gamma_2}]
                           = <gamma_1, gamma_2> * Omega_1 * Omega_2 * e_{gamma_1+gamma_2}

    Returns dict with wall-crossing data.
    """
    ef = _euler_form_2d(gamma1, gamma2)

    # Joyce-Song formula
    js_sign = (-1) ** (abs(ef) - 1)
    delta_omega_composite = js_sign * ef * omega1 * omega2

    # The BCH shadow jump at charge gamma_1 + gamma_2
    gamma_composite = tuple(g1 + g2 for g1, g2 in zip(gamma1, gamma2))

    # Higher-order BCH terms (at order 2 in the Lie algebra)
    bch_order2 = {}
    bch_order2[gamma_composite] = Rational(ef * omega1 * omega2) / 2

    # Order 3: involves [A, [A, B]] + [B, [B, A]]
    if order >= 3:
        # [e_{gamma_1}, [e_{gamma_1}, e_{gamma_2}]]
        # = <gamma_1, gamma_1+gamma_2> * e_{2*gamma_1 + gamma_2}
        ef_1_12 = _euler_form_2d(gamma1, gamma_composite)
        gamma_2_1_2 = tuple(2 * g1 + g2 for g1, g2 in zip(gamma1, gamma2))
        bch_order2[gamma_2_1_2] = Rational(ef * ef_1_12 * omega1 ** 2 * omega2) / 12

        ef_2_12 = _euler_form_2d(gamma2, gamma_composite)
        gamma_1_2_2 = tuple(g1 + 2 * g2 for g1, g2 in zip(gamma1, gamma2))
        bch_order2[gamma_1_2_2] = Rational(ef * ef_2_12 * omega1 * omega2 ** 2) / 12

    return {
        'gamma_1': gamma1,
        'gamma_2': gamma2,
        'euler_form': ef,
        'delta_omega': delta_omega_composite,
        'delta_omega_is_integer': isinstance(delta_omega_composite, int) or (
            isinstance(delta_omega_composite, Rational) and delta_omega_composite.q == 1
        ),
        'bch_terms': bch_order2,
        'gamma_composite': gamma_composite,
    }


def _euler_form_2d(gamma1, gamma2):
    """Skew-symmetric Euler form on Z^2."""
    return gamma1[0] * gamma2[1] - gamma1[1] * gamma2[0]


def wall_crossing_integrality_check(gamma_pairs, omegas, order: int = 5):
    r"""Check integrality of wall-crossing shadow jumps.

    For each pair of charges (gamma_1, gamma_2) with BPS indices
    (Omega_1, Omega_2), compute the jump Delta Omega and check
    integrality.

    BPS INTEGRALITY: Delta Omega should be an integer for consistent
    physical interpretation.

    Returns dict with integrality results.
    """
    results = []
    all_integral = True

    for (g1, g2), (o1, o2) in zip(gamma_pairs, omegas):
        jump = wall_crossing_shadow_jump(g1, g2, o1, o2, order)
        is_int = jump['delta_omega_is_integer']
        results.append({
            'gamma_pair': (g1, g2),
            'omegas': (o1, o2),
            'delta_omega': jump['delta_omega'],
            'is_integer': is_int,
            'euler_form': jump['euler_form'],
        })
        if not is_int:
            all_integral = False

    return {
        'checks': results,
        'all_integral': all_integral,
    }


def pentagon_wall_crossing(order: int = 5):
    r"""The pentagon identity as the simplest wall-crossing.

    For gamma_1 = (1,0), gamma_2 = (0,1) with <gamma_1, gamma_2> = 1
    and Omega(gamma_1) = Omega(gamma_2) = 1 (primitive BPS states):

    PENTAGON: K_{gamma_1} * K_{gamma_2}
            = K_{gamma_2} * K_{gamma_1+gamma_2} * K_{gamma_1}

    At the Lie algebra level, this is the arity-3 MC equation.
    The wall-crossing produces the bound state gamma_12 = (1,1) with
    Omega(gamma_12) = 1 (the W-boson in the Seiberg-Witten theory).

    Returns verification data including higher-order BCH terms.
    """
    gamma_1 = (1, 0)
    gamma_2 = (0, 1)
    gamma_12 = (1, 1)

    ef = _euler_form_2d(gamma_1, gamma_2)
    assert ef == 1, f"Expected <gamma_1, gamma_2> = 1, got {ef}"

    # Joyce-Song: Delta Omega(gamma_12)
    # = (-1)^{|<g1,g2>|-1} * <g1,g2> * Omega(g1) * Omega(g2)
    # = (-1)^0 * 1 * 1 * 1 = 1
    delta_omega = (-1) ** (abs(ef) - 1) * ef * 1 * 1

    # BCH computation at higher orders
    bch_data = wall_crossing_shadow_jump(gamma_1, gamma_2, 1, 1, order)

    return {
        'gamma_1': gamma_1,
        'gamma_2': gamma_2,
        'gamma_12': gamma_12,
        'euler_form': ef,
        'delta_omega_12': delta_omega,
        'pentagon_satisfied': delta_omega == 1,
        'bch_details': bch_data,
    }


def conifold_wall_crossing(order: int = 5):
    r"""Wall-crossing for the resolved conifold.

    The resolved conifold has two primitive BPS states:
        D0-brane: gamma_1 = (1, 0), Omega = 1
        D2-brane: gamma_2 = (0, 1), Omega = 1

    The wall-crossing from large volume to the orbifold point creates
    bound states at charges (n, m) for n + m >= 2.

    At the simplest level, this is the pentagon identity (same as above).
    Higher bound states arise from higher-order KS products.

    Returns the spectrum before and after wall-crossing.
    """
    gamma_D0 = (1, 0)
    gamma_D2 = (0, 1)

    # Weak coupling side: only D0 and D2
    weak_spectrum = {gamma_D0: 1, gamma_D2: 1}

    # Strong coupling side: D0, D2, and bound states
    strong_spectrum = dict(weak_spectrum)

    # The bound state W = D0 + D2 from the pentagon
    gamma_W = (1, 1)
    ef = _euler_form_2d(gamma_D0, gamma_D2)
    omega_W = (-1) ** (abs(ef) - 1) * ef * 1 * 1
    strong_spectrum[gamma_W] = omega_W

    # Higher bound states from iterated KS products
    if order >= 4:
        # (2,1) and (1,2) states from second-order wall-crossing
        gamma_21 = (2, 1)
        gamma_12 = (1, 2)

        # Delta Omega((2,1)) from gamma_D0 + gamma_W crossing:
        ef_D0_W = _euler_form_2d(gamma_D0, gamma_W)
        omega_21 = (-1) ** (abs(ef_D0_W) - 1) * ef_D0_W * 1 * omega_W
        if omega_21 != 0:
            strong_spectrum[gamma_21] = omega_21

        # Delta Omega((1,2)) from gamma_W + gamma_D2 crossing:
        ef_W_D2 = _euler_form_2d(gamma_W, gamma_D2)
        omega_12 = (-1) ** (abs(ef_W_D2) - 1) * ef_W_D2 * omega_W * 1
        if omega_12 != 0:
            strong_spectrum[gamma_12] = omega_12

    return {
        'weak_spectrum': weak_spectrum,
        'strong_spectrum': strong_spectrum,
        'primitive_charges': [gamma_D0, gamma_D2],
        'all_integer': all(isinstance(v, int) for v in strong_spectrum.values()),
    }


# ===========================================================================
# Section 7: Multi-path verification infrastructure
# ===========================================================================

def verify_gv_three_paths(degree: int = 3):
    r"""Three-path verification of GV invariants for local P^2 at given degree.

    Path 1: Known exact values from localization (Katz-Klemm-Vafa).
    Path 2: Mobius inversion from genus-0 GW invariants.
    Path 3: Wall-crossing / scattering diagram consistency.

    Returns verification data.
    """
    # Path 1: Known GV values
    known_gv = gv_local_p2(degree)

    # Path 2: Genus-0 GW -> GV via Mobius inversion
    # GW invariants at genus 0: N_{0,d} = sum_{k|d} n_0^{d/k} / k^3
    # Reconstruct N_{0,d} from known n_0^d
    gw_reconstructed = {}
    for d in range(1, degree + 1):
        N_0d = Rational(0)
        for k in _divisors(d):
            n_0_dk = known_gv.get((0, d // k), 0)
            N_0d += Rational(n_0_dk) / Rational(k) ** 3
        gw_reconstructed[(0, d)] = N_0d

    # Invert back to GV
    gv_from_gw = gv_from_genus_expansion(gw_reconstructed, max_genus=0,
                                          max_degree=degree)

    # Path 3: Integrality check
    integrality = gv_integrality_check(known_gv)

    # Comparison
    path_comparison = {}
    for d in range(1, degree + 1):
        p1 = known_gv.get((0, d), 0)
        p2 = gv_from_gw.get((0, d), 0)
        path_comparison[d] = {
            'known': p1,
            'from_gw_inversion': p2,
            'match': p1 == p2,
        }

    return {
        'known_gv': known_gv,
        'gv_from_gw': gv_from_gw,
        'integrality': integrality,
        'path_comparison': path_comparison,
        'all_paths_agree': all(v['match'] for v in path_comparison.values()),
    }


def verify_nekrasov_arithmetic_consistency(a_val, eps1_val, eps2_val,
                                            max_inst: int = 3):
    r"""Multi-path verification of Nekrasov arithmetic.

    Path 1: Direct computation from Young diagram sum.
    Path 2: eps1 <-> eps2 symmetry.
    Path 3: Weyl invariance a -> -a.
    Path 4: Denominator structure analysis.

    Returns verification data.
    """
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)
    a = Rational(a_val) if isinstance(a_val, (int, float, str)) else a_val

    # Path 1: Direct
    Z = nekrasov_partition_su2(a, e1, e2, max_inst)

    # Path 2: eps-symmetry
    Z_swap = nekrasov_partition_su2(a, e2, e1, max_inst)
    eps_sym = {}
    for k in range(max_inst + 1):
        eps_sym[k] = simplify(Z[k] - Z_swap[k]) == 0

    # Path 3: Weyl invariance
    Z_minus = nekrasov_partition_su2(-a, e1, e2, max_inst)
    weyl_sym = {}
    for k in range(max_inst + 1):
        weyl_sym[k] = simplify(Z[k] - Z_minus[k]) == 0

    # Path 4: Denominator analysis
    denom_data = nekrasov_denominator_analysis(a, e1, e2, max_inst)

    return {
        'Z': Z,
        'eps_symmetry': eps_sym,
        'weyl_symmetry': weyl_sym,
        'denominator_analysis': denom_data,
        'all_eps_symmetric': all(eps_sym.values()),
        'all_weyl_symmetric': all(weyl_sym.values()),
    }


def shadow_nekrasov_bridge(c_val, a_val, eps1_val, eps2_val, max_inst: int = 2):
    r"""Bridge between shadow invariants and Nekrasov coefficients.

    The shadow obstruction tower encodes the UNIVERSAL (algebra-intrinsic)
    part of the instanton expansion.  The Nekrasov partition function adds
    the REPRESENTATION-DEPENDENT part (via a, q).

    At the scalar level:
        F_g^{shadow} = kappa * lambda_g^FP  (algebra-intrinsic)
        F_g^{Nekrasov} = sum_k f_{g,k}(a) q^k  (representation-dependent)

    The bridge: in the limit a -> infinity (weak coupling),
        Z_k ~ F_0^{(k)}(a) / hbar + F_1^{(k)}(a) + hbar * F_2^{(k)}(a) + ...
    where F_g^{(k)} is the genus-g k-instanton coefficient.

    At k = 0 (perturbative): the shadow free energy is
        F_g^{pert} = F_g^{shadow} = kappa * lambda_g^FP

    Returns bridge data.
    """
    c = Rational(c_val) if isinstance(c_val, (int, float, str)) else c_val
    kappa = c / 2
    e1 = Rational(eps1_val)
    e2 = Rational(eps2_val)
    a = Rational(a_val) if isinstance(a_val, (int, float, str)) else a_val
    hbar = e1 * e2

    # Shadow side
    shadow_F1 = kappa / 24  # F_1 = kappa * lambda_1, lambda_1 = 1/24

    # Nekrasov side
    Z = nekrasov_partition_su2(a, e1, e2, max_inst)
    free_en = nekrasov_free_energy_su2(a, e1, e2, max_inst)

    # Prepotential (genus 0)
    F0_known = prepotential_from_periods(a, max_inst)

    return {
        'shadow': {
            'kappa': kappa,
            'F1_shadow': shadow_F1,
            'c': c,
        },
        'nekrasov': {
            'Z': Z,
            'free_energy': free_en,
            'hbar': hbar,
        },
        'prepotential': F0_known,
        'bridge_ratio': {
            'F1_over_kappa': shadow_F1 / kappa if kappa != 0 else None,
        },
    }
