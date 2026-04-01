r"""Genus-2 free energy F_2 across the standard landscape.

Computes F_2 for six families, distinguishing the scalar (uniform-weight)
lane from multi-generator algebras where the planted-forest correction
enters.

SCALAR LANE (uniform-weight, single-generator or all generators same weight):
    F_2 = kappa * lambda_2^FP = kappa * 7/5760

    lambda_2^FP = (2^3 - 1)/2^3 * |B_4|/4! = (7/8)(1/30)/24 = 7/5760

    Proved: thm:multi-generator-universality (uniform-weight lane),
    thm:algebraic-family-rigidity.

MULTI-GENERATOR CORRECTION:
    For algebras with generators of different conformal weights, the
    genus-2 free energy decomposes as:

        F_2 = F_2^{scal} + delta_pf^{(2,0)}

    where F_2^{scal} = kappa * lambda_2^FP is the scalar contribution
    and delta_pf^{(2,0)} is the planted-forest correction from the
    higher shadow tower. The planted-forest correction on a single
    primary line with shadow data (kappa_line, S_3) is:

        delta_pf^{(2,0)}_line = S_3 * (10*S_3 - kappa_line) / 48

    For multi-generator algebras, the total correction sums over all
    primary lines.

    STATUS: The planted-forest formula is PROVED at genus 2
    (rem:planted-forest-correction-explicit). The multi-generator
    universality F_2 = kappa * lambda_2^FP for multi-WEIGHT algebras
    at genus >= 2 is OPEN (op:multi-generator-universality). Whether
    delta_pf contributes a correction to F_2 or is absorbed into the
    scalar formula depends on this open problem.

FAMILIES:
    1. Heisenberg at k=1: kappa = 1, scalar lane (1 generator, weight 1).
    2. Virasoro at c=25: kappa = 25/2, scalar lane (1 generator, weight 2).
    3. Affine sl_2 at k=1: kappa = 9/4, scalar lane (dim g = 3 generators,
       all weight 1 by AP27 propagator-weight universality).
    4. W_3 at generic c: kappa = 5c/6, MULTI-WEIGHT (T weight 2, W weight 3).
       Two primary lines: T-line (kappa_T = c/2, S_3^T = 2) and
       W-line (kappa_W = c/3, S_3^W = 0 by Z_2 parity).
    5. betagamma at lambda=1: kappa = 1, MULTI-WEIGHT (beta weight 1,
       gamma weight 0). Class C (shadow depth 4). The scalar-lane formula
       F_2 = kappa * lambda_2^FP is CONDITIONAL on op:multi-generator-universality
       at genus >= 2 for multi-weight algebras.
    6. E_8 lattice VOA: kappa = rank = 8, scalar lane (8 generators, all
       weight 1, abelian hence uniform-weight by Heisenberg tensor product).

Manuscript references:
    thm:universal-generating-function (higher_genus_modular_koszul.tex)
    rem:planted-forest-correction-explicit (higher_genus_modular_koszul.tex)
    thm:multi-generator-universality (higher_genus_foundations.tex)
    op:multi-generator-universality (higher_genus_foundations.tex)
    thm:algebraic-family-rigidity (higher_genus_modular_koszul.tex)
    rem:propagator-weight-universality (higher_genus_foundations.tex)
    prop:betagamma-obstruction-coefficient (beta_gamma.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, Optional, Tuple

from sympy import Rational, Symbol, cancel, simplify


# ============================================================================
# Faber-Pandharipande number lambda_2^FP
# ============================================================================

def lambda_fp_2() -> Rational:
    r"""Faber-Pandharipande number at genus 2.

    lambda_2^FP = (2^3 - 1)/2^3 * |B_4| / 4!
               = (7/8) * (1/30) / 24
               = 7 / 5760

    Independent derivation:
        B_4 = -1/30  (fourth Bernoulli number)
        |B_4| = 1/30
        2^{2*2-1} = 8
        (8 - 1)/8 = 7/8
        4! = 24
        lambda_2 = (7/8)(1/30)/24 = 7/5760
    """
    return Rational(7, 5760)


# ============================================================================
# Kappa formulas for each family
# ============================================================================

def kappa_heisenberg(k: int) -> Rational:
    r"""kappa(H_k) = k.

    For Heisenberg, the level IS the obstruction coefficient.
    Single generator J of conformal weight 1.
    Scalar lane: yes (single generator).
    """
    return Rational(k)


def kappa_virasoro(c) -> Rational:
    r"""kappa(Vir_c) = c/2.

    Single generator T of conformal weight 2.
    Scalar lane: yes (single generator).
    """
    return Rational(c) / 2


def kappa_affine_sl2(k) -> Rational:
    r"""kappa(sl_2 at level k) = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k+2)/4.

    dim(sl_2) = 3, h^v(sl_2) = 2.
    Generators: J^a for a = 1, 2, 3, all of conformal weight 1.
    Scalar lane: yes (all generators weight 1; AP27 says bar propagator
    d log E(z,w) is weight 1 for ALL channels).
    """
    return Rational(3) * (Rational(k) + 2) / 4


def kappa_w3(c=None):
    r"""kappa(W_3) = 5c/6.

    Two generators: T (weight 2) and W (weight 3).
    Decomposition: kappa = kappa_T + kappa_W = c/2 + c/3 = 5c/6.
    Scalar lane: NO (weights 2 and 3 differ).
    """
    if c is None:
        return Rational(5) * Symbol('c') / 6
    return Rational(5) * Rational(c) / 6


def kappa_w3_T(c=None):
    """Per-channel kappa for the T line: kappa_T = c/2."""
    if c is None:
        return Symbol('c') / 2
    return Rational(c) / 2


def kappa_w3_W(c=None):
    """Per-channel kappa for the W line: kappa_W = c/3."""
    if c is None:
        return Symbol('c') / 3
    return Rational(c) / 3


def kappa_betagamma(lam) -> Rational:
    r"""kappa(betagamma at weight lambda) = 6*lambda^2 - 6*lambda + 1.

    Two generators: beta (weight lambda) and gamma (weight 1-lambda).
    c = 2*(6*lambda^2 - 6*lambda + 1), so kappa = c/2.
    At lambda=1: kappa = 6 - 6 + 1 = 1.
    Scalar lane: only at lambda = 1/2 (where both weights = 1/2).
    At lambda = 1: weights are 1 and 0, hence MULTI-WEIGHT.
    Shadow depth = 4 (class C, contact/quartic archetype).
    """
    lam = Rational(lam)
    return 6 * lam ** 2 - 6 * lam + 1


def kappa_E8_lattice() -> Rational:
    r"""kappa(V_{E_8}) = rank(E_8) = 8.

    Lattice VOA of rank 8. The 8 generators are free bosons of weight 1.
    kappa = rank for all even self-dual lattice VOAs.
    Scalar lane: yes (all generators weight 1, abelian).
    This is 8 copies of Heisenberg at k=1, so kappa = 8*1 = 8.
    """
    return Rational(8)


# ============================================================================
# Scalar-lane F_2 (proved for uniform-weight algebras)
# ============================================================================

def F2_scalar(kappa) -> Rational:
    r"""F_2 on the scalar lane: F_2 = kappa * lambda_2^FP = 7*kappa/5760.

    This is the genus-2 free energy for any modular Koszul algebra on the
    uniform-weight lane (proved by thm:multi-generator-universality on that
    lane plus thm:algebraic-family-rigidity).
    """
    return kappa * lambda_fp_2()


# ============================================================================
# Planted-forest correction at genus 2
# ============================================================================

def planted_forest_g2(S_3, kappa_line) -> Rational:
    r"""Planted-forest correction delta_pf^{(2,0)} on a single primary line.

    delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa_line) / 48

    where S_3 = alpha is the cubic shadow coefficient and kappa_line is
    the per-channel kappa on that line.

    From rem:planted-forest-correction-explicit (higher_genus_modular_koszul.tex).

    For Heisenberg (class G): S_3 = 0, delta_pf = 0.
    For affine KM (class L): S_3 != 0 but tower terminates at arity 3.
    For Virasoro (class M): S_3 = 2, kappa = c/2, delta_pf = 2(20 - c/2)/48.
    """
    return S_3 * (10 * S_3 - kappa_line) / Rational(48)


def planted_forest_g2_w3_T(c=None):
    r"""Planted-forest correction on the W_3 T-line.

    T-line shadow data: kappa_T = c/2, S_3^T = alpha_T = 2.
    Identical to the Virasoro planted-forest correction.

    delta_pf_T = 2 * (20 - c/2) / 48 = (40 - c) / 48
    """
    if c is None:
        c_sym = Symbol('c')
        return planted_forest_g2(Rational(2), c_sym / 2)
    return planted_forest_g2(Rational(2), Rational(c) / 2)


def planted_forest_g2_w3_W(c=None):
    r"""Planted-forest correction on the W_3 W-line.

    W-line shadow data: kappa_W = c/3, S_3^W = alpha_W = 0.
    Z_2 parity (W -> -W) forces all odd arities to vanish.

    delta_pf_W = 0 * (0 - c/3) / 48 = 0
    """
    if c is None:
        return planted_forest_g2(Rational(0), Symbol('c') / 3)
    return planted_forest_g2(Rational(0), Rational(c) / 3)


def planted_forest_g2_w3_total(c=None):
    r"""Total planted-forest correction for W_3 at genus 2.

    Sum over both primary lines:
        delta_pf^{(2,0)}(W_3) = delta_pf_T + delta_pf_W
                               = (40 - c)/48 + 0
                               = (40 - c)/48

    This is the multi-channel correction beyond the scalar formula.
    Whether this enters F_2(W_3) depends on op:multi-generator-universality.
    """
    return planted_forest_g2_w3_T(c) + planted_forest_g2_w3_W(c)


# ============================================================================
# Per-family genus-2 free energy
# ============================================================================

def F2_heisenberg(k: int = 1) -> Dict[str, Any]:
    r"""Genus-2 free energy for Heisenberg at level k.

    kappa = k. Scalar lane (single generator, weight 1).
    F_2 = k * 7/5760.

    At k=1: F_2 = 7/5760.
    Class G (Gaussian, shadow depth 2). S_3 = 0, delta_pf = 0.
    """
    kappa = kappa_heisenberg(k)
    F2 = F2_scalar(kappa)
    return {
        'family': 'Heisenberg',
        'parameter': f'k={k}',
        'kappa': kappa,
        'F2': F2,
        'scalar_lane': True,
        'shadow_class': 'G',
        'shadow_depth': 2,
        'delta_pf': Rational(0),
        'status': 'PROVED',
        'notes': 'Single generator weight 1. Class G: tower terminates at arity 2.',
    }


def F2_virasoro(c=25) -> Dict[str, Any]:
    r"""Genus-2 free energy for Virasoro at central charge c.

    kappa = c/2. Scalar lane (single generator T, weight 2).
    F_2 = (c/2) * 7/5760 = 7c/11520.

    At c=25: F_2 = 175/11520 = 35/2304.
    Class M (mixed, shadow depth infinity). S_3 = 2.
    The planted-forest correction delta_pf = (40-c)/48 exists but is
    ABSORBED into the scalar formula by single-generator universality.
    """
    kappa = kappa_virasoro(c)
    F2 = F2_scalar(kappa)
    delta = planted_forest_g2(Rational(2), kappa)
    return {
        'family': 'Virasoro',
        'parameter': f'c={c}',
        'kappa': kappa,
        'F2': F2,
        'scalar_lane': True,
        'shadow_class': 'M',
        'shadow_depth': 'infinity',
        'S_3': Rational(2),
        'delta_pf': delta,
        'delta_pf_status': 'Absorbed into scalar formula (single generator)',
        'status': 'PROVED',
        'notes': ('Single generator weight 2. Class M: infinite tower. '
                  'Planted-forest correction exists but does not modify '
                  'F_2 = kappa * lambda_2^FP because the scalar-lane '
                  'universality is proved for single-generator algebras.'),
    }


def F2_affine_sl2(k=1) -> Dict[str, Any]:
    r"""Genus-2 free energy for affine sl_2 at level k.

    kappa = 3(k+2)/4. Scalar lane: YES.
    All 3 generators (J^1, J^2, J^3) have conformal weight 1.
    This is a uniform-weight algebra (all generators same weight).

    At k=1: kappa = 9/4, F_2 = (9/4) * 7/5760 = 63/23040 = 7/2560.
    Class L (Lie/tree, shadow depth 3). S_3 = structure constants.
    """
    kappa = kappa_affine_sl2(k)
    F2 = F2_scalar(kappa)
    return {
        'family': 'Affine sl_2',
        'parameter': f'k={k}',
        'kappa': kappa,
        'F2': F2,
        'scalar_lane': True,
        'shadow_class': 'L',
        'shadow_depth': 3,
        'delta_pf': Rational(0),
        'delta_pf_status': 'Zero: class L has S_3 from structure constants '
                           'but the planted-forest correction is absorbed '
                           'into the scalar formula (uniform weight)',
        'status': 'PROVED',
        'notes': ('3 generators all weight 1 (uniform weight). Class L: '
                  'tower terminates at arity 3. kappa = dim*'
                  '(k+h^v)/(2*h^v) = 3*(k+2)/4.'),
    }


def F2_w3(c=None) -> Dict[str, Any]:
    r"""Genus-2 free energy for W_3 at central charge c.

    kappa = 5c/6 = kappa_T + kappa_W = c/2 + c/3.
    NOT on the scalar lane: T has weight 2, W has weight 3.

    Scalar contribution: F_2^{scal} = (5c/6) * 7/5760 = 7c/6912.

    Planted-forest correction (per primary line):
        T-line: S_3^T = 2, kappa_T = c/2
            delta_pf_T = 2*(20 - c/2)/48 = (40-c)/48
        W-line: S_3^W = 0, kappa_W = c/3
            delta_pf_W = 0
        Total: delta_pf = (40-c)/48

    STATUS: F_2 = kappa * lambda_2^FP is OPEN for multi-weight algebras
    at genus >= 2 (op:multi-generator-universality). The scalar-lane
    formula gives F_2^{scal} = 7c/6912 unconditionally. Whether the
    planted-forest correction modifies or is absorbed depends on the
    open problem.

    The full F_2(W_3) is:
        CONDITIONAL: F_2 = 7c/6912  (if universality holds)
        ALTERNATIVE: F_2 = 7c/6912 + (40-c)/48  (if correction enters)
    """
    if c is not None:
        c_val = Rational(c)
    else:
        c_val = Symbol('c')

    kappa = kappa_w3(c)
    F2_scal = F2_scalar(kappa) if c is not None else kappa * lambda_fp_2()
    kT = kappa_w3_T(c)
    kW = kappa_w3_W(c)
    dpf_T = planted_forest_g2_w3_T(c)
    dpf_W = planted_forest_g2_w3_W(c)
    dpf_total = planted_forest_g2_w3_total(c)

    result = {
        'family': 'W_3',
        'parameter': f'c={c}' if c is not None else 'c (generic)',
        'kappa_total': kappa,
        'kappa_T': kT,
        'kappa_W': kW,
        'F2_scalar': F2_scal,
        'scalar_lane': False,
        'shadow_class': 'M',
        'shadow_depth': 'infinity',
        'T_line': {
            'kappa': kT,
            'S_3': Rational(2),
            'delta_pf': dpf_T,
        },
        'W_line': {
            'kappa': kW,
            'S_3': Rational(0),
            'delta_pf': dpf_W,
        },
        'delta_pf_total': dpf_total,
        'status': 'CONDITIONAL on op:multi-generator-universality',
        'notes': ('Two generators: T (weight 2, class M) and W (weight 3, '
                  'class M with Z_2 parity). Multi-weight: NOT on scalar lane. '
                  'Scalar formula gives F_2^{scal} = 7*kappa/5760 = 7c/6912. '
                  'Planted-forest correction delta_pf = (40-c)/48 from T-line; '
                  'W-line contributes 0 by Z_2 parity.'),
    }

    return result


def F2_betagamma(lam=1) -> Dict[str, Any]:
    r"""Genus-2 free energy for betagamma at conformal weight lambda.

    Two generators: beta (weight lambda) and gamma (weight 1-lambda).
    kappa = 6*lambda^2 - 6*lambda + 1.
    At lambda=1: kappa = 1, c = 2.
    At lambda=1/2: kappa = -1/2, c = -1 (symmetric point, BOTH weight 1/2).

    Scalar lane: only at lambda = 1/2 (where both generators have weight 1/2).
    At lambda=1: weights are 1 and 0, so this is MULTI-WEIGHT.

    Shadow depth = 4 (class C, contact/quartic archetype).
    The quartic contact invariant vanishes on the weight line, but the
    shadow tower terminates at arity 4 by stratum separation.

    STATUS: For lambda != 1/2, this is a multi-weight algebra and
    F_2 = kappa * lambda_2^FP is CONDITIONAL on op:multi-generator-universality.
    At lambda = 1/2 (uniform weight), the scalar lane applies but
    kappa = -1/2 (note the sign).
    """
    lam_r = Rational(lam)
    kappa = kappa_betagamma(lam)
    F2_scal = F2_scalar(kappa)
    is_scalar_lane = (lam_r == Rational(1, 2))
    weight_beta = lam_r
    weight_gamma = 1 - lam_r

    status = 'PROVED' if is_scalar_lane else 'CONDITIONAL on op:multi-generator-universality'

    return {
        'family': 'betagamma',
        'parameter': f'lambda={lam}',
        'kappa': kappa,
        'c': 2 * kappa,
        'F2_scalar': F2_scal,
        'scalar_lane': is_scalar_lane,
        'shadow_class': 'C',
        'shadow_depth': 4,
        'weight_beta': weight_beta,
        'weight_gamma': weight_gamma,
        'status': status,
        'notes': (f'Two generators: beta (weight {weight_beta}) and '
                  f'gamma (weight {weight_gamma}). '
                  f'{"Uniform weight: scalar lane applies." if is_scalar_lane else "Multi-weight: NOT on scalar lane."} '
                  f'Class C: shadow depth 4 (quartic contact). '
                  f'kappa = 6*{lam}^2 - 6*{lam} + 1 = {kappa}.'),
    }


def F2_E8_lattice() -> Dict[str, Any]:
    r"""Genus-2 free energy for the E_8 lattice VOA.

    kappa = rank(E_8) = 8. Scalar lane (8 free bosons, all weight 1).
    This is the tensor product of 8 copies of Heisenberg at k=1.
    F_2 = 8 * 7/5760 = 56/5760 = 7/720.
    Class G (Gaussian, shadow depth 2, abelian). S_3 = 0, delta_pf = 0.
    """
    kappa = kappa_E8_lattice()
    F2 = F2_scalar(kappa)
    return {
        'family': 'E_8 lattice',
        'parameter': 'rank=8',
        'kappa': kappa,
        'F2': F2,
        'scalar_lane': True,
        'shadow_class': 'G',
        'shadow_depth': 2,
        'delta_pf': Rational(0),
        'status': 'PROVED',
        'notes': ('8 free bosons (Heisenberg at k=1), all weight 1. '
                  'kappa = rank = 8. Class G: abelian, tower terminates at '
                  'arity 2. F_2 = 8 * 7/5760 = 7/720.'),
    }


# ============================================================================
# Full landscape table
# ============================================================================

def genus2_landscape_table() -> Dict[str, Dict[str, Any]]:
    """Complete genus-2 free energy table for the six standard families.

    Returns a dictionary keyed by family name with all computed data.
    """
    return {
        'Heisenberg_k1': F2_heisenberg(k=1),
        'Virasoro_c25': F2_virasoro(c=25),
        'Affine_sl2_k1': F2_affine_sl2(k=1),
        'W3_generic': F2_w3(c=None),
        'betagamma_lam1': F2_betagamma(lam=1),
        'E8_lattice': F2_E8_lattice(),
    }


# ============================================================================
# Cross-family consistency checks (AP10: never rely on hardcoded expected
# values alone; cross-family structural checks are the real verification)
# ============================================================================

def verify_kappa_additivity() -> Dict[str, bool]:
    r"""Verify kappa additivity for tensor product algebras.

    E_8 lattice = Heisenberg^{tensor 8} implies kappa(V_{E_8}) = 8 * kappa(H_1).
    W_3 decomposition: kappa(W_3) = kappa_T + kappa_W = c/2 + c/3 = 5c/6.
    """
    results = {}

    # E_8 = 8 copies of Heisenberg
    k_H = kappa_heisenberg(1)
    k_E8 = kappa_E8_lattice()
    results['E8 = 8 * Heisenberg'] = (k_E8 == 8 * k_H)

    # W_3 channel decomposition (at a specific c to avoid symbolic issues)
    c_val = 50  # arbitrary test value
    k_total = kappa_w3(c_val)
    k_T = kappa_w3_T(c_val)
    k_W = kappa_w3_W(c_val)
    results['W3 kappa = kappa_T + kappa_W'] = (k_total == k_T + k_W)

    return results


def verify_F2_linearity() -> Dict[str, bool]:
    r"""Verify F_2 is linear in kappa on the scalar lane.

    F_2(2*kappa) = 2 * F_2(kappa) for any kappa.
    F_2(H_k) = k * F_2(H_1) (Heisenberg additivity).
    """
    results = {}

    # Linearity
    F2_1 = F2_scalar(Rational(1))
    F2_2 = F2_scalar(Rational(2))
    results['F2(2) = 2*F2(1)'] = (F2_2 == 2 * F2_1)

    # Heisenberg additivity
    F2_H1 = F2_heisenberg(1)['F2']
    F2_H3 = F2_heisenberg(3)['F2']
    results['F2(H_3) = 3*F2(H_1)'] = (F2_H3 == 3 * F2_H1)

    # E_8 = 8 * Heisenberg
    F2_E = F2_E8_lattice()['F2']
    results['F2(E8) = 8*F2(H_1)'] = (F2_E == 8 * F2_H1)

    return results


def verify_complementarity_F2() -> Dict[str, Any]:
    r"""Verify complementarity for F_2 on Koszul dual pairs.

    For Virasoro: Vir_c^! = Vir_{26-c}. Koszul duality sum:
        kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
    So F_2(Vir_c) + F_2(Vir_{26-c}) = 13 * lambda_2^FP = 91/5760.

    AP24: kappa + kappa! = 13 for Virasoro (NOT zero).
    For affine KM: kappa(sl_2, k) + kappa(sl_2, -k-4) = 0.
    """
    results = {}

    # Virasoro complementarity
    c_val = 25
    F2_c = F2_virasoro(c_val)['F2']
    F2_c_dual = F2_virasoro(26 - c_val)['F2']
    F2_sum = F2_c + F2_c_dual
    expected_sum = Rational(13) * lambda_fp_2()  # 91/5760
    results['Vir F2 + F2_dual'] = {
        'c': c_val,
        'c_dual': 26 - c_val,
        'F2(c)': F2_c,
        'F2(c_dual)': F2_c_dual,
        'sum': F2_sum,
        'expected': expected_sum,
        'match': F2_sum == expected_sum,
    }

    # Affine sl_2 complementarity: kappa + kappa' = 0
    k_val = 1
    k_dual = -k_val - 4  # Feigin-Frenkel: k' = -k - 2*h^v = -k - 4
    kappa_k = kappa_affine_sl2(k_val)
    kappa_k_dual = kappa_affine_sl2(k_dual)
    results['sl2 kappa + kappa_dual = 0'] = {
        'k': k_val,
        'k_dual': k_dual,
        'kappa(k)': kappa_k,
        'kappa(k_dual)': kappa_k_dual,
        'sum': kappa_k + kappa_k_dual,
        'expected': Rational(0),
        'match': kappa_k + kappa_k_dual == Rational(0),
    }

    return results


def verify_planted_forest_consistency() -> Dict[str, bool]:
    r"""Verify planted-forest correction consistency.

    1. Heisenberg (class G): delta_pf = 0 (S_3 = 0).
    2. W_3 W-line: delta_pf = 0 (S_3 = 0 by Z_2 parity).
    3. Virasoro at c=40: delta_pf = 0 (the special value where 10*S_3 = kappa).
       S_3 = 2, kappa = 20, so 10*2 - 20 = 0.
    4. Virasoro at c=26: delta_pf = (40-26)/48 = 14/48 = 7/24.
    """
    results = {}

    # Heisenberg: delta_pf = 0
    dpf_H = planted_forest_g2(Rational(0), Rational(1))
    results['Heisenberg delta_pf = 0'] = (dpf_H == 0)

    # W_3 W-line: delta_pf = 0
    dpf_W = planted_forest_g2_w3_W(50)
    results['W3 W-line delta_pf = 0'] = (dpf_W == 0)

    # Virasoro at c=40: special vanishing
    dpf_Vir40 = planted_forest_g2(Rational(2), Rational(20))  # kappa = 40/2 = 20
    results['Virasoro c=40 delta_pf = 0'] = (dpf_Vir40 == 0)

    # Virasoro at c=26: check specific value
    dpf_Vir26 = planted_forest_g2(Rational(2), Rational(13))  # kappa = 26/2 = 13
    expected_26 = Rational(2) * (20 - 13) / 48  # = 14/48 = 7/24
    results['Virasoro c=26 delta_pf = 7/24'] = (dpf_Vir26 == expected_26)

    return results


# ============================================================================
# Summary report
# ============================================================================

def print_landscape_summary():
    """Print a formatted summary of the genus-2 landscape."""
    table = genus2_landscape_table()

    print("=" * 72)
    print("GENUS-2 FREE ENERGY LANDSCAPE")
    print("=" * 72)
    print(f"{'Family':<20} {'kappa':<12} {'F_2':<18} {'Lane':<10} {'Status'}")
    print("-" * 72)

    for key, data in table.items():
        family = data['family']
        kappa = data.get('kappa', data.get('kappa_total', '?'))
        F2 = data.get('F2', data.get('F2_scalar', '?'))
        lane = 'scalar' if data['scalar_lane'] else 'multi-wt'
        status = data['status'][:20]
        print(f"{family:<20} {str(kappa):<12} {str(F2):<18} {lane:<10} {status}")

    print("=" * 72)
    print(f"\nlambda_2^FP = {lambda_fp_2()} = 7/5760")
    print(f"F_2^{{scalar}} = kappa * 7/5760\n")

    # W_3 planted-forest detail
    w3 = table['W3_generic']
    print("W_3 planted-forest detail (generic c):")
    print(f"  T-line: S_3 = {w3['T_line']['S_3']}, delta_pf = {w3['T_line']['delta_pf']}")
    print(f"  W-line: S_3 = {w3['W_line']['S_3']}, delta_pf = {w3['W_line']['delta_pf']}")
    print(f"  Total delta_pf = {w3['delta_pf_total']}")


if __name__ == '__main__':
    print_landscape_summary()

    print("\n" + "=" * 72)
    print("CONSISTENCY CHECKS")
    print("=" * 72)

    print("\nKappa additivity:")
    for name, ok in verify_kappa_additivity().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\nF_2 linearity:")
    for name, ok in verify_F2_linearity().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\nPlanted-forest consistency:")
    for name, ok in verify_planted_forest_consistency().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\nComplementarity:")
    comp = verify_complementarity_F2()
    for name, data in comp.items():
        if isinstance(data, dict):
            print(f"  [{'PASS' if data['match'] else 'FAIL'}] {name}: "
                  f"sum = {data['sum']}, expected = {data['expected']}")
