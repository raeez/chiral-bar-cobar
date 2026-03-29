"""Complete W_4 OPE extraction via quantum Miura transformation.

Computes the FULL lambda-bracket algebra of W(sl_4) = W_4 from first
principles using the quantum Miura transform and Wick contractions.

MATHEMATICAL SETUP:
  The quantum Miura transformation for W(sl_4):
    L(z) = :(d + J_1(z))(d + J_2(z))(d + J_3(z))(d + J_4(z)):
  where J_i are free boson currents with OPE J_i(z)J_j(w) ~ k*delta_{ij}/(z-w)^2,
  and the J_i correspond to the weights of the fundamental representation of sl_4.

  Expanding L = d^4 + 0*d^3 + T*d^2 + W_3*d + W_4 gives the three generators.
  After projecting W_3, W_4 to Virasoro primaries, we compute all OPEs via
  free-field Wick contractions.

GENERATORS:
  T   = U_2 (stress tensor, weight 2)
  W_3 = primary projection of U_3 (weight 3)
  W_4 = primary projection of U_4 (weight 4)

CENTRAL CHARGE:
  c = 3 - 60(k+3)^2/(k+4) for W(sl_4) at level k.
  At alpha_0 = 1 (k=1): c = -57.  (CORRECTED from earlier modules.)
  Generic c = -2 corresponds to the FREE FIELD realization at k -> infinity... no.
  Actually c(k=1) = 3 - 60*16/5 = 3 - 192 = -189.  Let me be precise:
  c(k) = 3 - 60*(k+3)^2/(k+4).
  c(1) = 3 - 60*16/5 = 3 - 192 = -189.
  c(2) = 3 - 60*25/6 = 3 - 250 = -247.
  c(5) = 3 - 60*64/9 = 3 - 1280/3 = -1271/3.

SIX OPE BRACKETS (complete list):
  1. T x T:    standard Virasoro (poles 1-4)
  2. T x W_3:  primary condition (poles 1-2)
  3. T x W_4:  primary condition (poles 1-2)
  4. W_3 x W_3: poles 1-6, composite Lambda + W_4 at pole 2
  5. W_3 x W_4: poles 1-7
  6. W_4 x W_4: poles 1-8

STRUCTURE CONSTANTS (from bootstrap / DS reduction):
  c_334^2 = 42 c^2 (5c+22) / [(c+24)(7c+68)(3c+46)]
  c_444^2 = 112 c^2 (2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)]
  C_{3,4;3;0,4}^2 = (9/16) c_334^2
  C_{3,4;4;0,3}^2 = (5/7) c_334^2
  C_{4,4;2;0,6} = 2  (Ward identity)
  C_{3,4;2;0,5} = 0  (orthogonality)

BAR COMPLEX INPUT:
  From the OPE, the bar differential acts on the generators via the
  n-th products. At small weights, this is computable from the
  structure constants extracted here.

MC4 VERIFICATION:
  Coefficient stabilization at stage 4: the squared structure constants
  c_334^2, c_444^2 are rational functions of c. Their values at specific
  levels must match the rational function exactly (not just numerically).

References:
  - Fateev-Lukyanov (1988), quantum Miura transform
  - Hornfeck, Nucl. Phys. B 407 (1993) 57 (W_4 bootstrap)
  - Blumenhagen et al., Nucl. Phys. B 461 (1996) 460
  - Bouwknegt-Schoutens, Phys. Rep. 223 (1993) 183
  - concordance.tex: rem:mc4-winfty-computation-target
  - w4_ds_ope_extraction.py: known formulas
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    symbols,
    together,
    oo,
)

from compute.lib.w4_ds_ope import (
    DiffPoly,
    wick_ope,
    miura_expand_sl4,
    extract_central_charge_from_ope,
    make_primary_w3,
    make_primary_w4,
    compute_generators,
    extract_all_ope_data,
    w4_central_charge,
    w4_complementarity_sum,
    _extract_scalar,
    _extract_along,
    _propagator_coeff,
    _canonical_key,
)

from compute.lib.w4_ds_ope_extraction import (
    c334_squared_formula,
    c444_squared_formula,
    c343_formula,
    c344_formula,
)


# ====================================================================
# Central charge utilities
# ====================================================================

def central_charge(k):
    """Central charge c(k) = 3 - 60(k+3)^2/(k+4) for principal W_4.

    Special values:
      k=1: c = 3 - 60*16/5 = -189
      k=2: c = 3 - 60*25/6 = -247
      k=5: c = 3 - 60*64/9 = -1271/3
      k -> inf: c -> -57 (free field limit... actually c -> -inf)

    Actually, as k -> infinity: c ~ 3 - 60k -> -inf.
    The Feigin-Frenkel dual level is k' = -k-8.
    c(k) + c(k') = 246.
    """
    return w4_central_charge(k)


def dual_level(k):
    """Feigin-Frenkel dual level k' = -k - 8 for sl_4."""
    return -k - 8


# ====================================================================
# Generator computation via quantum Miura
# ====================================================================

def compute_w4_generators(k) -> Dict[str, DiffPoly]:
    """Compute primary generators T, W_3, W_4 at level k.

    Uses the quantum Miura operator expansion:
      L = (d + J_1)(d + J_2)(d + J_3)(d + J_4)
        = d^4 + 0*d^3 + U_2*d^2 + U_3*d + U_4

    Then projects U_3, U_4 to Virasoro primaries by subtracting
    Virasoro descendants.

    Returns dict with keys 'T', 'W3', 'W4'.
    """
    return compute_generators(k)


def verify_generators_at_k(k) -> Dict[str, object]:
    """Verify generator properties at a specific level k.

    Checks:
    1. Central charge matches c(k) = 3 - 60(k+3)^2/(k+4)
    2. W_3 is primary of weight 3 (no poles > 2 in T x W_3)
    3. W_4 is primary of weight 4 (no poles > 2 in T x W_4)
    4. Two-point functions are nonzero
    """
    gens = compute_w4_generators(k)
    T, W3, W4 = gens['T'], gens['W3'], gens['W4']

    # Central charge
    c_extracted = extract_central_charge_from_ope(T, k)
    c_expected = central_charge(k)

    # Primaryity of W_3
    ope_TW3 = wick_ope(T, W3, k)
    w3_primary = all(ope_TW3.get(p, DiffPoly()).is_zero() for p in range(3, 10))

    # Primaryity of W_4
    ope_TW4 = wick_ope(T, W4, k)
    w4_primary = all(ope_TW4.get(p, DiffPoly()).is_zero() for p in range(3, 10))

    # Two-point functions
    ope_W3W3 = wick_ope(W3, W3, k)
    ope_W4W4 = wick_ope(W4, W4, k)
    N3 = _extract_scalar(ope_W3W3.get(6, DiffPoly()))
    N4 = _extract_scalar(ope_W4W4.get(8, DiffPoly()))

    return {
        'k': k,
        'c_extracted': cancel(c_extracted),
        'c_expected': cancel(c_expected),
        'c_match': simplify(c_extracted - c_expected) == 0,
        'w3_primary': w3_primary,
        'w4_primary': w4_primary,
        'N3': cancel(N3),
        'N4': cancel(N4),
        'N3_nonzero': expand(N3) != 0,
        'N4_nonzero': expand(N4) != 0,
    }


# ====================================================================
# Complete OPE computation at a given level
# ====================================================================

def compute_all_opes(k) -> Dict[str, Dict[int, DiffPoly]]:
    """Compute all 6 OPE brackets at level k.

    Returns dict mapping bracket name to {pole_order: DiffPoly}.
    The DiffPoly values are normal-ordered differential polynomials
    in the free bosons.
    """
    gens = compute_w4_generators(k)
    T, W3, W4 = gens['T'], gens['W3'], gens['W4']

    return {
        'TT': wick_ope(T, T, k),
        'TW3': wick_ope(T, W3, k),
        'TW4': wick_ope(T, W4, k),
        'W3W3': wick_ope(W3, W3, k),
        'W3W4': wick_ope(W3, W4, k),
        'W4W4': wick_ope(W4, W4, k),
    }


def ope_pole_orders(opes: Dict[str, Dict[int, DiffPoly]]) -> Dict[str, List[int]]:
    """Extract the nonzero pole orders for each OPE bracket.

    Returns dict mapping bracket name to sorted list of pole orders.
    """
    result = {}
    for name, ope in opes.items():
        nonzero = [p for p, dp in ope.items() if not dp.is_zero()]
        result[name] = sorted(nonzero, reverse=True)
    return result


# ====================================================================
# Lambda-bracket extraction
# ====================================================================

def extract_lambda_brackets(k) -> Dict[str, Dict[int, Dict[str, object]]]:
    """Extract lambda-bracket coefficients for all 6 brackets at level k.

    For each bracket {A_lambda B}, extracts the coefficient of lambda^n
    for each pole order n, decomposed into contributions from generators
    and composites.

    The lambda-bracket is related to the OPE via:
      {A_lambda B} = sum_n (lambda^n / n!) A_(n) B
    where A_(n)B is the coefficient of (z-w)^{-(n+1)} in A(z)B(w).

    So the pole-(n+1) coefficient in the OPE = A_(n)B, and
    the lambda^n/n! coefficient in the lambda-bracket = A_(n)B.

    Returns dict mapping bracket name to {mode_n: {field_label: coeff}}.
    """
    gens = compute_w4_generators(k)
    T, W3, W4 = gens['T'], gens['W3'], gens['W4']
    opes = compute_all_opes(k)

    # Composite fields
    dT = T.derivative()
    d2T = dT.derivative()
    d3T = d2T.derivative()
    dW3 = W3.derivative()
    dW4 = W4.derivative()

    # Lambda = :TT: - (3/10) d^2T
    TT_product = T * T  # normal-ordered product
    Lambda = TT_product + d2T.scale(Rational(-3, 10))
    dLambda = Lambda.derivative()

    result = {}

    # Build reference fields for projection
    ref_fields = {
        'T': T, 'W3': W3, 'W4': W4,
        'dT': dT, 'dW3': dW3, 'dW4': dW4,
        'd2T': d2T, 'd3T': d3T,
        'Lambda': Lambda, 'dLambda': dLambda,
        'TT': TT_product,
    }

    for name, ope in opes.items():
        bracket_data = {}
        for pole, dp in sorted(ope.items(), reverse=True):
            if dp.is_zero():
                continue
            mode_n = pole - 1  # A_(n)B at pole n+1
            coeffs = {}

            # Extract scalar component (vacuum)
            scalar = _extract_scalar(dp)
            if expand(scalar) != 0:
                coeffs['vac'] = cancel(scalar)

            # Extract along each generator and composite
            for label, ref in ref_fields.items():
                if ref.is_zero():
                    continue
                c_val = _extract_along(dp, ref)
                if c_val is not None and expand(c_val) != 0:
                    coeffs[label] = cancel(c_val)

            if coeffs:
                bracket_data[mode_n] = coeffs

        result[name] = bracket_data

    return result


# ====================================================================
# Structure constant extraction (normalized)
# ====================================================================

def extract_structure_constants(k) -> Dict[str, object]:
    """Extract all independent OPE structure constants at level k.

    Uses the manuscript normalization convention:
      <W^(s)(z) W^(s)(0)> = (c/s) z^{-2s}

    The raw Miura generators have non-standard normalization.
    We normalize by dividing by the appropriate two-point function ratios.

    Returns all 6 independent structure constants for the stage-4 packet:
      c_334_sq:    (W_3 x W_3 -> W_4)^2
      c_444_sq:    (W_4 x W_4 -> W_4)^2
      C_34_3_sq:   (W_3 x W_4 -> W_3)^2
      C_34_4_sq:   (W_3 x W_4 -> W_4)^2
      C_44_T:      W_4 x W_4 -> T (Ward identity, should be 2)
      C_34_T:      W_3 x W_4 -> T (should be 0)
    plus stage-3 coefficients and diagnostics.
    """
    return extract_all_ope_data(k)


def extract_stage4_packet(k) -> Dict[str, object]:
    """Extract the 6-entry stage-4 packet at level k.

    This is the MC4-relevant data: the 4 higher-spin structure constants
    (squared, normalized) and the 2 Virasoro-target identities.
    """
    data = extract_structure_constants(k)

    return {
        'k': k,
        'c': data['c'],
        # Stage-4 higher-spin (squared)
        'c334_sq': data['c334_sq'],
        'c444_sq': data['c444_sq'],
        'C_34_3_sq': data['C_34_3_04_sq'],
        'C_34_4_sq': data['C_34_4_03_sq'],
        # Stage-4 Virasoro targets
        'C_44_T': data['C_res_44_2_06'],
        'C_34_T_zero': data['C_res_34_2_05_zero'],
        # Diagnostics
        'w3_primary': data['w3_primary'],
        'w4_primary': data['w4_primary'],
    }


# ====================================================================
# Multi-level extraction and interpolation
# ====================================================================

def extract_at_multiple_levels(k_values=None) -> List[Dict[str, object]]:
    """Extract stage-4 packet at multiple levels.

    Default levels chosen to avoid poles and give clean rational values.
    """
    if k_values is None:
        k_values = [Rational(1), Rational(2), Rational(3),
                    Rational(5), Rational(7), Rational(10)]

    results = []
    for k in k_values:
        try:
            packet = extract_stage4_packet(k)
            results.append(packet)
        except Exception as e:
            results.append({'k': k, 'error': str(e)})

    return results


def verify_against_known_formulas(k) -> Dict[str, object]:
    """Compare extracted structure constants against known closed-form formulas.

    The known formulas (from Hornfeck 1993 / DS reduction):
      c_334^2 = 42 c^2 (5c+22) / [(c+24)(7c+68)(3c+46)]
      c_444^2 = 112 c^2 (2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)]

    Returns verification results with relative errors.
    """
    data = extract_structure_constants(k)
    c_val = data['c']

    # Known formulas evaluated at this c
    c334_sq_known = c334_squared_formula(c_val)
    c444_sq_known = c444_squared_formula(c_val)
    c343_sq_known = c343_formula(c_val)
    c344_sq_known = c344_formula(c_val)

    # Extracted values
    c334_sq_ext = data['c334_sq']
    c444_sq_ext = data['c444_sq']
    c343_sq_ext = data['C_34_3_04_sq']
    c344_sq_ext = data['C_34_4_03_sq']

    return {
        'k': k,
        'c': c_val,
        # c_334
        'c334_sq_extracted': cancel(c334_sq_ext),
        'c334_sq_known': cancel(c334_sq_known),
        'c334_match': simplify(c334_sq_ext - c334_sq_known) == 0,
        # c_444
        'c444_sq_extracted': cancel(c444_sq_ext),
        'c444_sq_known': cancel(c444_sq_known),
        'c444_match': simplify(c444_sq_ext - c444_sq_known) == 0,
        # C_{3,4;3;0,4}
        'c343_sq_extracted': cancel(c343_sq_ext),
        'c343_sq_known': cancel(c343_sq_known),
        'c343_match': simplify(c343_sq_ext - c343_sq_known) == 0,
        # C_{3,4;4;0,3}
        'c344_sq_extracted': cancel(c344_sq_ext),
        'c344_sq_known': cancel(c344_sq_known),
        'c344_match': simplify(c344_sq_ext - c344_sq_known) == 0,
        # Virasoro targets
        'C_44_T': data['C_res_44_2_06'],
        'C_44_T_is_2': simplify(data['C_res_44_2_06'] - 2) == 0,
        'C_34_T_is_0': data['C_res_34_2_05_zero'],
    }


# ====================================================================
# Virasoro sub-algebra verification
# ====================================================================

def verify_virasoro_subalgebra(k) -> Dict[str, object]:
    """Verify the Virasoro sub-algebra T x T at level k.

    Checks:
    1. Pole 4: c/2 (central charge)
    2. Pole 2: 2T (conformal weight of T = 2)
    3. Pole 1: dT (translation)
    4. No poles > 4
    """
    gens = compute_w4_generators(k)
    T = gens['T']
    ope_TT = wick_ope(T, T, k)

    c_val = central_charge(k)

    # Pole 4: should be c/2 (scalar)
    pole4_scalar = _extract_scalar(ope_TT.get(4, DiffPoly()))
    pole4_correct = simplify(pole4_scalar - c_val / 2) == 0

    # Pole 2: should be 2*T
    pole2_T = _extract_along(ope_TT.get(2, DiffPoly()), T)
    pole2_correct = simplify(pole2_T - 2) == 0

    # Pole 1: should be dT
    dT = T.derivative()
    pole1_dT = _extract_along(ope_TT.get(1, DiffPoly()), dT)
    pole1_correct = simplify(pole1_dT - 1) == 0

    # No poles > 4
    no_higher = all(ope_TT.get(p, DiffPoly()).is_zero() for p in range(5, 10))

    return {
        'c': c_val,
        'pole4_scalar': cancel(pole4_scalar),
        'pole4_correct': pole4_correct,
        'pole2_T_coeff': cancel(pole2_T),
        'pole2_correct': pole2_correct,
        'pole1_dT_coeff': cancel(pole1_dT),
        'pole1_correct': pole1_correct,
        'no_higher_poles': no_higher,
        'all_correct': pole4_correct and pole2_correct and pole1_correct and no_higher,
    }


# ====================================================================
# Primary condition verification
# ====================================================================

def verify_primary_conditions(k) -> Dict[str, object]:
    """Verify primary conditions for W_3 and W_4 at level k.

    For a primary field W_s of weight s under T:
      T(z) W_s(w) ~ s * W_s(w) / (z-w)^2 + dW_s(w) / (z-w) + regular

    So the only nonzero poles in T x W_s are poles 2 and 1.
    Pole 2 coefficient is s * W_s, pole 1 is dW_s.
    """
    gens = compute_w4_generators(k)
    T, W3, W4 = gens['T'], gens['W3'], gens['W4']

    ope_TW3 = wick_ope(T, W3, k)
    ope_TW4 = wick_ope(T, W4, k)

    # W_3 checks
    w3_pole2 = _extract_along(ope_TW3.get(2, DiffPoly()), W3)
    w3_pole2_correct = simplify(w3_pole2 - 3) == 0
    w3_no_higher = all(ope_TW3.get(p, DiffPoly()).is_zero() for p in range(3, 10))

    # W_4 checks
    w4_pole2 = _extract_along(ope_TW4.get(2, DiffPoly()), W4)
    w4_pole2_correct = simplify(w4_pole2 - 4) == 0
    w4_no_higher = all(ope_TW4.get(p, DiffPoly()).is_zero() for p in range(3, 10))

    return {
        'W3_weight': cancel(w3_pole2),
        'W3_weight_correct': w3_pole2_correct,
        'W3_no_higher_poles': w3_no_higher,
        'W3_primary': w3_pole2_correct and w3_no_higher,
        'W4_weight': cancel(w4_pole2),
        'W4_weight_correct': w4_pole2_correct,
        'W4_no_higher_poles': w4_no_higher,
        'W4_primary': w4_pole2_correct and w4_no_higher,
    }


# ====================================================================
# W_3 x W_3 OPE detailed analysis
# ====================================================================

def analyze_w3w3_ope(k) -> Dict[str, object]:
    """Detailed analysis of the W_3 x W_3 OPE at level k.

    This is the most important OPE: it contains the W_4 primary coupling
    c_334 at pole 2, along with the composite Lambda = :TT: - (3/10)d^2T.

    Pole structure:
      Pole 6: c/3 (two-point function)
      Pole 5: 0 (no weight-1 field)
      Pole 4: 2T (from W_3 being weight 3: C_{3,3;2;0,4} = 2)
      Pole 3: dT
      Pole 2: (3/10)d^2T + alpha*Lambda + c_334*W_4
      Pole 1: derivatives of pole 2 + corrections
    """
    gens = compute_w4_generators(k)
    T, W3, W4 = gens['T'], gens['W3'], gens['W4']

    ope_W3W3 = wick_ope(W3, W3, k)
    c_val = central_charge(k)

    # Two-point function
    N3 = _extract_scalar(ope_W3W3.get(6, DiffPoly()))

    # Pole 4: T coefficient
    T_at_pole4 = _extract_along(ope_W3W3.get(4, DiffPoly()), T)

    # Pole 2: decompose into d^2T, Lambda, W_4
    pole2 = ope_W3W3.get(2, DiffPoly())
    W4_at_pole2 = _extract_along(pole2, W4)

    # Normalized c_334: requires normalizing W_3 and W_4
    # alpha3^2 = (c/3) / N3 normalizes W_3 to <W_3,W_3> = c/3
    ope_W4W4 = wick_ope(W4, W4, k)
    N4 = _extract_scalar(ope_W4W4.get(8, DiffPoly()))
    # alpha4^2 = (c/4) / N4

    # Alternatively, normalize via C_{3,3;2;0,4} = 2:
    # alpha3^2 * T_at_pole4 = 2
    alpha3_sq = cancel(Rational(2) / T_at_pole4) if expand(T_at_pole4) != 0 else 1
    alpha4_sq = cancel(c_val / (4 * N4)) if expand(N4) != 0 else 1

    # c_334^2 = (alpha3^2)^2 * W4_at_pole2^2 * (4 * N4 / c)
    c334_sq = cancel(alpha3_sq ** 2 * W4_at_pole2 ** 2 * 4 * N4 / c_val) if expand(c_val) != 0 else 0

    # Compare to known formula
    c334_sq_known = c334_squared_formula(c_val)

    return {
        'k': k,
        'c': c_val,
        'N3': cancel(N3),
        'N4': cancel(N4),
        'T_at_pole4': cancel(T_at_pole4),
        'W4_at_pole2_raw': cancel(W4_at_pole2),
        'alpha3_sq': cancel(alpha3_sq),
        'alpha4_sq': cancel(alpha4_sq),
        'c334_sq': cancel(c334_sq),
        'c334_sq_known': cancel(c334_sq_known),
        'c334_match': simplify(c334_sq - c334_sq_known) == 0,
        'pole_orders': sorted([p for p, dp in ope_W3W3.items() if not dp.is_zero()],
                              reverse=True),
    }


# ====================================================================
# W_4 x W_4 OPE detailed analysis
# ====================================================================

def analyze_w4w4_ope(k) -> Dict[str, object]:
    """Detailed analysis of the W_4 x W_4 OPE at level k.

    Pole structure:
      Pole 8: c/4 (two-point function)
      Pole 7: 0 (no weight-1 field)
      Pole 6: 2T (Ward identity: C_{4,4;2;0,6} = 2)
      Pole 5: dT
      Pole 4: d^2T + alpha_44*Lambda + c_444*W_4
      Pole 3: derivatives
      Pole 2: more composites
      Pole 1: more composites
    """
    gens = compute_w4_generators(k)
    T, W3, W4 = gens['T'], gens['W3'], gens['W4']

    ope_W4W4 = wick_ope(W4, W4, k)
    c_val = central_charge(k)

    # Two-point function
    N4 = _extract_scalar(ope_W4W4.get(8, DiffPoly()))

    # Pole 6: T coefficient (Ward identity prediction: 2)
    T_at_pole6 = _extract_along(ope_W4W4.get(6, DiffPoly()), T)
    # Normalize: alpha4^2 * T_at_pole6 = C_{4,4;2;0,6}
    alpha4_sq = cancel(c_val / (4 * N4)) if expand(N4) != 0 else 1
    C_44_T = cancel(alpha4_sq * T_at_pole6) if expand(T_at_pole6) != 0 else 0

    # Pole 4: W_4 coefficient (self-coupling c_444)
    W4_at_pole4 = _extract_along(ope_W4W4.get(4, DiffPoly()), W4)
    # c_444^2 = alpha4_sq * W4_at_pole4^2
    c444_sq = cancel(alpha4_sq * W4_at_pole4 ** 2)

    # Compare to known formula
    c444_sq_known = c444_squared_formula(c_val)

    return {
        'k': k,
        'c': c_val,
        'N4': cancel(N4),
        'T_at_pole6_raw': cancel(T_at_pole6),
        'C_44_T_normalized': cancel(C_44_T),
        'C_44_T_is_2': simplify(C_44_T - 2) == 0,
        'W4_at_pole4_raw': cancel(W4_at_pole4),
        'c444_sq': cancel(c444_sq),
        'c444_sq_known': cancel(c444_sq_known),
        'c444_match': simplify(c444_sq - c444_sq_known) == 0,
        'pole_orders': sorted([p for p, dp in ope_W4W4.items() if not dp.is_zero()],
                              reverse=True),
    }


# ====================================================================
# W_3 x W_4 OPE detailed analysis
# ====================================================================

def analyze_w3w4_ope(k) -> Dict[str, object]:
    """Detailed analysis of the W_3 x W_4 OPE at level k.

    Key predictions:
      C_{3,4;2;0,5} = 0 (mixed Virasoro vanishing)
      C_{3,4;3;0,4}^2 = (9/16) c_334^2 (metric adjoint relation)
      C_{3,4;4;0,3}^2 = (5/7) c_334^2 (Borcherds identity)
    """
    gens = compute_w4_generators(k)
    T, W3, W4 = gens['T'], gens['W3'], gens['W4']

    ope_W3W4 = wick_ope(W3, W4, k)
    c_val = central_charge(k)

    # Normalizations
    ope_W3W3 = wick_ope(W3, W3, k)
    ope_W4W4 = wick_ope(W4, W4, k)
    N3 = _extract_scalar(ope_W3W3.get(6, DiffPoly()))
    N4 = _extract_scalar(ope_W4W4.get(8, DiffPoly()))

    # Use C_{3,3;2;0,4}=2 normalization for alpha3
    T_at_pole4_w3w3 = _extract_along(ope_W3W3.get(4, DiffPoly()), T)
    alpha3_sq = cancel(Rational(2) / T_at_pole4_w3w3) if expand(T_at_pole4_w3w3) != 0 else 1
    alpha4_sq = cancel(c_val / (4 * N4)) if expand(N4) != 0 else 1

    # Pole 5: T coefficient (should be 0)
    T_at_pole5 = _extract_along(ope_W3W4.get(5, DiffPoly()), T)
    T_at_pole5_zero = expand(T_at_pole5) == 0 if T_at_pole5 is not None else True

    # Pole 4: W_3 coefficient
    W3_at_pole4 = _extract_along(ope_W3W4.get(4, DiffPoly()), W3)
    # C_{3,4;3;0,4}^2 = alpha4_sq * W3_at_pole4^2
    C_34_3_sq = cancel(alpha4_sq * W3_at_pole4 ** 2) if W3_at_pole4 is not None else 0

    # Pole 3: W_4 coefficient
    W4_at_pole3 = _extract_along(ope_W3W4.get(3, DiffPoly()), W4)
    # C_{3,4;4;0,3}^2 = alpha3_sq * W4_at_pole3^2
    C_34_4_sq = cancel(alpha3_sq * W4_at_pole3 ** 2) if W4_at_pole3 is not None else 0

    # Compare to known formulas
    c343_known = c343_formula(c_val)
    c344_known = c344_formula(c_val)

    return {
        'k': k,
        'c': c_val,
        'T_at_pole5_raw': cancel(T_at_pole5) if T_at_pole5 is not None else 0,
        'T_at_pole5_zero': T_at_pole5_zero,
        'W3_at_pole4_raw': cancel(W3_at_pole4) if W3_at_pole4 is not None else 0,
        'C_34_3_sq': cancel(C_34_3_sq),
        'C_34_3_sq_known': cancel(c343_known),
        'C_34_3_match': simplify(C_34_3_sq - c343_known) == 0,
        'W4_at_pole3_raw': cancel(W4_at_pole3) if W4_at_pole3 is not None else 0,
        'C_34_4_sq': cancel(C_34_4_sq),
        'C_34_4_sq_known': cancel(c344_known),
        'C_34_4_match': simplify(C_34_4_sq - c344_known) == 0,
        'pole_orders': sorted([p for p, dp in ope_W3W4.items() if not dp.is_zero()],
                              reverse=True),
    }


# ====================================================================
# Composite field analysis
# ====================================================================

def compute_composite_lambda(k) -> Dict[str, object]:
    """Compute the composite Lambda = :TT: - (3/10)d^2T at level k.

    Verify quasi-primarity: T(z)Lambda(w) should have no (z-w)^{-3} pole.

    Also compute the two-point norm <Lambda|Lambda>.
    """
    gens = compute_w4_generators(k)
    T = gens['T']

    dT = T.derivative()
    d2T = dT.derivative()

    # Lambda = :TT: - (3/10) d^2T
    TT = T * T
    Lambda = TT + d2T.scale(Rational(-3, 10))

    # T x Lambda OPE
    ope_T_Lambda = wick_ope(T, Lambda, k)

    # Quasi-primarity: pole 3 should be zero
    pole3 = ope_T_Lambda.get(3, DiffPoly())
    quasi_primary = pole3.is_zero()

    # Pole 2: should be 4*Lambda (weight 4)
    # Pole 4: anomaly (5c+22)/5 * T (from known W_3 computation)

    # Two-point function <Lambda|Lambda>
    ope_LL = wick_ope(Lambda, Lambda, k)
    norm_Lambda = _extract_scalar(ope_LL.get(8, DiffPoly()))

    c_val = central_charge(k)

    return {
        'k': k,
        'c': c_val,
        'quasi_primary': quasi_primary,
        'norm_Lambda': cancel(norm_Lambda),
        'expected_norm': cancel(c_val * (5 * c_val + 22) / 10),
        'norm_correct': simplify(norm_Lambda - c_val * (5 * c_val + 22) / 10) == 0,
    }


# ====================================================================
# Bar complex input computation
# ====================================================================

def compute_bar_differential_input(k) -> Dict[str, object]:
    """Compute bar differential input from the W_4 OPE data at level k.

    The bar complex B(W_4) has generators in each conformal weight.
    The differential d: B_n -> B_{n-1} is built from the OPE n-th products.

    At low weights, the bar differential is determined by:
    - d(T) involves T x T products
    - d(W_3) involves T x W_3 and W_3 x W_3 products
    - d(W_4) involves T x W_4, W_3 x W_4, W_4 x W_4 products

    The bar-cobar adjunction gives: d^2 = 0, which is equivalent to
    the Borcherds/Jacobi identity for the OPE.

    For the MC4 stage-4 packet, the relevant bar differential components
    are those involving the stage-4 structure constants c_334 and c_444.

    Returns the weight-graded components of the bar differential.
    """
    data = extract_structure_constants(k)
    c_val = data['c']

    # Stage-3 bar differential (Virasoro + W_3)
    bar_stage3 = {
        'C_TT_T': data['stage3_TT'],  # T x T -> T at pole 2
        'C_TW3_W3': data['stage3_TW'],  # T x W_3 -> W_3 at pole 2
        'C_W3W3_T': data['stage3_WW'],  # W_3 x W_3 -> T at pole 4
    }

    # Stage-4 bar differential (new in W_4)
    bar_stage4 = {
        'c334_sq': data['c334_sq'],
        'c444_sq': data['c444_sq'],
        'C_34_3_sq': data['C_34_3_04_sq'],
        'C_34_4_sq': data['C_34_4_03_sq'],
        'C_44_T': data['C_res_44_2_06'],
        'C_34_T_zero': data['C_res_34_2_05_zero'],
    }

    # Bar differential d^2 = 0 check:
    # The key identity is the Jacobi identity for the W_4 algebra.
    # At the bar level, this becomes: for each triple of generators
    # (A, B, C), the sum over all channels must vanish.
    #
    # For (W_3, W_3, W_3): the Jacobi identity at weight 9
    # involves c_334 in a quadratic relation (since W_3 x W_3 -> W_4
    # and then W_4 x W_3 -> ... must cancel against cyclic permutations).

    return {
        'k': k,
        'c': c_val,
        'stage3': bar_stage3,
        'stage4': bar_stage4,
        'w3_primary': data['w3_primary'],
        'w4_primary': data['w4_primary'],
    }


# ====================================================================
# MC4 coefficient stabilization verification
# ====================================================================

def verify_mc4_stabilization(k_values=None) -> Dict[str, object]:
    """Verify MC4 coefficient stabilization at stage 4.

    The MC4 splitting theorem says:
    - MC4+ (positive towers): structure constants stabilize exactly
    - MC4^0 (resonant towers): finite resonance problem

    For the W_4 algebra at generic level, the structure constants
    c_334^2, c_444^2 are rational functions of c (hence of k).
    Stabilization means: the rational function, once determined
    from finitely many sample points, gives the EXACT value at
    ALL levels (where it is defined).

    This is verified by:
    1. Computing at several k values
    2. Checking that all values lie on the SAME rational function
    3. Comparing to the known closed-form formula
    """
    if k_values is None:
        k_values = [Rational(1), Rational(2), Rational(3),
                    Rational(5), Rational(7)]

    results = []
    all_c334_match = True
    all_c444_match = True
    all_vir_match = True

    for k in k_values:
        data = extract_structure_constants(k)
        c_val = data['c']

        c334_sq_ext = data['c334_sq']
        c444_sq_ext = data['c444_sq']
        c334_sq_known = c334_squared_formula(c_val)
        c444_sq_known = c444_squared_formula(c_val)

        c334_ok = simplify(c334_sq_ext - c334_sq_known) == 0
        c444_ok = simplify(c444_sq_ext - c444_sq_known) == 0
        vir_ok = simplify(data['C_res_44_2_06'] - 2) == 0

        if not c334_ok:
            all_c334_match = False
        if not c444_ok:
            all_c444_match = False
        if not vir_ok:
            all_vir_match = False

        results.append({
            'k': k,
            'c': c_val,
            'c334_match': c334_ok,
            'c444_match': c444_ok,
            'C_44_T_is_2': vir_ok,
            'C_34_T_zero': data['C_res_34_2_05_zero'],
        })

    return {
        'results': results,
        'all_c334_stabilized': all_c334_match,
        'all_c444_stabilized': all_c444_match,
        'all_virasoro_targets': all_vir_match,
        'mc4_stabilization_verified': all_c334_match and all_c444_match and all_vir_match,
    }


# ====================================================================
# Feigin-Frenkel duality verification
# ====================================================================

def verify_ff_duality(k) -> Dict[str, object]:
    """Verify Feigin-Frenkel duality at level k.

    Under FF duality k -> k' = -k-8:
      c(k) + c(k') = 246
      The structure constants at dual levels are related by the
      c -> 246-c map.
    """
    c_k = central_charge(k)
    k_dual = dual_level(k)
    c_kp = central_charge(k_dual)

    # Complementarity sum
    comp_sum = cancel(c_k + c_kp)
    comp_correct = simplify(comp_sum - 246) == 0

    # Structure constants at dual levels
    c334_k = c334_squared_formula(c_k)
    c334_kp = c334_squared_formula(c_kp)

    c444_k = c444_squared_formula(c_k)
    c444_kp = c444_squared_formula(c_kp)

    return {
        'k': k,
        'k_dual': k_dual,
        'c_k': cancel(c_k),
        'c_kp': cancel(c_kp),
        'comp_sum': comp_sum,
        'comp_correct': comp_correct,
        'c334_sq_k': cancel(c334_k),
        'c334_sq_kp': cancel(c334_kp),
        'c444_sq_k': cancel(c444_k),
        'c444_sq_kp': cancel(c444_kp),
    }


# ====================================================================
# Classical limit verification
# ====================================================================

def verify_classical_limit() -> Dict[str, object]:
    """Verify structure constants in the classical limit c -> infinity.

    c_334^2 -> 42*5/(7*3) = 210/21 = 10
    c_444^2 -> 112*2*3/(7*10*5) = 672/350 = 96/50 = 48/25
    """
    c = Symbol('c')
    from sympy import limit

    c334_limit = limit(c334_squared_formula(c), c, oo)
    c444_limit = limit(c444_squared_formula(c), c, oo)

    return {
        'c334_sq_limit': c334_limit,
        'c334_sq_limit_expected': Rational(10),
        'c334_limit_correct': simplify(c334_limit - 10) == 0,
        'c444_sq_limit': c444_limit,
        'c444_sq_limit_expected': Rational(48, 25),
        'c444_limit_correct': simplify(c444_limit - Rational(48, 25)) == 0,
    }


# ====================================================================
# Zero and pole structure analysis
# ====================================================================

def analyze_zero_pole_structure() -> Dict[str, object]:
    """Analyze zeros and poles of the structure constants.

    c_334^2 = 42 c^2 (5c+22) / [(c+24)(7c+68)(3c+46)]
      Zeros: c=0 (double), c=-22/5
      Poles: c=-24, c=-68/7, c=-46/3

    c_444^2 = 112 c^2 (2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)]
      Zeros: c=0 (double), c=1/2, c=-46/3
      Poles: c=-24, c=-68/7, c=-197/10, c=-3/5
    """
    c = Symbol('c')

    c334 = c334_squared_formula(c)
    c444 = c444_squared_formula(c)

    # Verify zeros
    c334_at_0 = c334_squared_formula(Rational(0))
    c334_at_m22_5 = c334_squared_formula(Rational(-22, 5))
    c444_at_0 = c444_squared_formula(Rational(0))
    c444_at_half = c444_squared_formula(Rational(1, 2))
    c444_at_m46_3 = c444_squared_formula(Rational(-46, 3))

    return {
        'c334_zeros': {
            'c=0': c334_at_0,
            'c=-22/5': c334_at_m22_5,
        },
        'c444_zeros': {
            'c=0': c444_at_0,
            'c=1/2': c444_at_half,
            'c=-46/3': c444_at_m46_3,
        },
        'all_zeros_vanish': (
            c334_at_0 == 0 and c334_at_m22_5 == 0
            and c444_at_0 == 0 and c444_at_half == 0
            and c444_at_m46_3 == 0
        ),
    }


# ====================================================================
# Metric adjoint relations
# ====================================================================

def verify_metric_adjoint_relations() -> Dict[str, object]:
    """Verify metric adjoint relations between OPE coefficients.

    C_{3,4;3;0,4}^2 = (9/16) c_334^2
    C_{3,4;4;0,3}^2 = (5/7) c_334^2

    These follow from the invariant bilinear form identity:
      (W_3_{(1)} W_3, W_4) = -(W_3, W_3_{(3)} W_4)
    """
    c = Symbol('c')

    c334_sq = c334_squared_formula(c)
    c343_sq = c343_formula(c)
    c344_sq = c344_formula(c)

    ratio_343 = cancel(c343_sq / c334_sq)
    ratio_344 = cancel(c344_sq / c334_sq)

    return {
        'C_343/c334': ratio_343,
        'C_343/c334_expected': Rational(9, 16),
        'C_343_correct': simplify(ratio_343 - Rational(9, 16)) == 0,
        'C_344/c334': ratio_344,
        'C_344/c334_expected': Rational(5, 7),
        'C_344_correct': simplify(ratio_344 - Rational(5, 7)) == 0,
    }


# ====================================================================
# Unitary minimal model check
# ====================================================================

def w4_unitary_minimal_models(max_p=10) -> List[Dict[str, object]]:
    """Check structure constants at W_4 unitary minimal models.

    The W_4 unitary minimal models have:
      c = 3(1 - N(N-1)(N+1)^2 / ((p-1)p))
    for N=4, i.e. c = 3(1 - 60/((p-1)p)) = 3 - 180/((p-1)p),
    for p >= 5 (unitary series).

    Wait, the correct formula for W_N unitary minimal models is:
      c(p,q) = (N-1)(1 - N(N+1)(p-q)^2/(pq))
    with q = p+1 (unitary diagonal series).

    For W_4 (N=4):
      c(p) = 3(1 - 20(p-(p+1))^2/(p(p+1))) = 3(1 - 20/(p(p+1)))
            = 3 - 60/(p(p+1))

    The unitary series starts at p=4: c = 3 - 60/20 = 0 (trivial),
    then p=5: c = 3 - 60/30 = 1, p=6: c = 3 - 60/42 = 3 - 10/7 = 11/7, etc.

    At each unitary minimal model, all squared structure constants
    must be non-negative (unitarity).
    """
    results = []
    for p in range(5, max_p + 1):
        c_val = 3 - Rational(60, p * (p + 1))
        c334 = c334_squared_formula(c_val)
        c444 = c444_squared_formula(c_val)

        results.append({
            'p': p,
            'c': c_val,
            'c334_sq': c334,
            'c444_sq': c444,
            'c334_nonneg': c334 >= 0,
            'c444_nonneg': c444 >= 0,
            'unitary_ok': c334 >= 0 and c444 >= 0,
        })

    return results


# ====================================================================
# Full extraction report
# ====================================================================

def full_extraction_report(k=None) -> Dict[str, object]:
    """Complete extraction report at a given level.

    Combines all verifications into a single report.
    """
    if k is None:
        k = Rational(1)

    report = {
        'generators': verify_generators_at_k(k),
        'virasoro': verify_virasoro_subalgebra(k),
        'primary_conditions': verify_primary_conditions(k),
        'w3w3': analyze_w3w3_ope(k),
        'w4w4': analyze_w4w4_ope(k),
        'w3w4': analyze_w3w4_ope(k),
        'composite': compute_composite_lambda(k),
        'ff_duality': verify_ff_duality(k),
        'classical_limit': verify_classical_limit(),
        'metric_adjoint': verify_metric_adjoint_relations(),
        'zero_poles': analyze_zero_pole_structure(),
    }

    # Summary
    gens = report['generators']
    w3w3 = report['w3w3']
    w4w4 = report['w4w4']
    w3w4 = report['w3w4']

    report['summary'] = {
        'c_correct': gens['c_match'],
        'all_primary': gens['w3_primary'] and gens['w4_primary'],
        'virasoro_correct': report['virasoro']['all_correct'],
        'c334_match': w3w3['c334_match'],
        'c444_match': w4w4['c444_match'],
        'C_44_T_is_2': w4w4['C_44_T_is_2'],
        'C_34_T_zero': w3w4['T_at_pole5_zero'],
        'C_34_3_match': w3w4['C_34_3_match'],
        'C_34_4_match': w3w4['C_34_4_match'],
        'Lambda_quasi_primary': report['composite']['quasi_primary'],
        'Lambda_norm_correct': report['composite']['norm_correct'],
        'ff_complementarity': report['ff_duality']['comp_correct'],
        'classical_limits_correct': (
            report['classical_limit']['c334_limit_correct']
            and report['classical_limit']['c444_limit_correct']
        ),
        'metric_adjoint_correct': (
            report['metric_adjoint']['C_343_correct']
            and report['metric_adjoint']['C_344_correct']
        ),
        'all_zeros_correct': report['zero_poles']['all_zeros_vanish'],
    }

    all_ok = all(report['summary'].values())
    report['summary']['ALL_PASS'] = all_ok

    return report


# ====================================================================
# Runner
# ====================================================================

if __name__ == "__main__":
    from sympy import Rational as R, pprint

    print("=" * 72)
    print("COMPLETE W_4 OPE EXTRACTION VIA QUANTUM MIURA TRANSFORMATION")
    print("=" * 72)

    k_test = R(1)
    print(f"\nLevel k = {k_test}")
    print(f"Central charge c = {central_charge(k_test)}")

    print("\n--- Generator Verification ---")
    gv = verify_generators_at_k(k_test)
    for key, val in gv.items():
        print(f"  {key}: {val}")

    print("\n--- Virasoro Sub-algebra ---")
    vir = verify_virasoro_subalgebra(k_test)
    for key, val in vir.items():
        print(f"  {key}: {val}")

    print("\n--- Primary Conditions ---")
    pc = verify_primary_conditions(k_test)
    for key, val in pc.items():
        print(f"  {key}: {val}")

    print("\n--- W_3 x W_3 Analysis ---")
    w3w3 = analyze_w3w3_ope(k_test)
    for key, val in w3w3.items():
        print(f"  {key}: {val}")

    print("\n--- W_4 x W_4 Analysis ---")
    w4w4 = analyze_w4w4_ope(k_test)
    for key, val in w4w4.items():
        print(f"  {key}: {val}")

    print("\n--- W_3 x W_4 Analysis ---")
    w3w4 = analyze_w3w4_ope(k_test)
    for key, val in w3w4.items():
        print(f"  {key}: {val}")

    print("\n--- Classical Limits ---")
    cl = verify_classical_limit()
    for key, val in cl.items():
        print(f"  {key}: {val}")

    print("\n--- Metric Adjoint Relations ---")
    ma = verify_metric_adjoint_relations()
    for key, val in ma.items():
        print(f"  {key}: {val}")

    print("\n--- Zero/Pole Structure ---")
    zp = analyze_zero_pole_structure()
    for key, val in zp.items():
        print(f"  {key}: {val}")

    print("\n--- Unitary Minimal Models ---")
    um = w4_unitary_minimal_models(max_p=8)
    for entry in um:
        print(f"  p={entry['p']}: c={entry['c']}, c334^2={entry['c334_sq']}, "
              f"c444^2={entry['c444_sq']}, unitary={entry['unitary_ok']}")
