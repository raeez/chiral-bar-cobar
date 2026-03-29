"""W_4 DS OPE coefficient extraction via Miura transform.

Fills structural gap H3: Extract the 4 free OPE coefficients from the
principal Drinfeld-Sokolov W_4 algebra for MC4 verification.

The W_4 algebra = principal DS reduction of sl_4-hat at level k.
  Generators: T (spin 2), W_3 (spin 3), W_4 (spin 4).
  Central charge: c = 3 - 60(k+3)^2/(k+4).

METHOD: Miura transform + free-field Wick contraction.

The Miura operator for sl_N decomposes the DS generators as differential
polynomials in (N-1) free bosons. For sl_4:

  L = (d + J_1)(d + J_2)(d + J_3)(d + J_4)
    = d^4 + U_2 d^2 + U_3 d + U_4

where J_i = sum_a e_i^a dphi_a are free boson currents and e_i are weights
of the fundamental representation of sl_4. The expansion uses QUANTUM
operator multiplication: (d + J_i) applied to f means df + :J_i f: where
normal ordering includes the self-contraction correction when d hits
a normal-ordered product.

The sl_4 fundamental weights in the rank-3 weight space:
  e_1 = (1, 0, 0),  e_2 = (-1, 1, 0),  e_3 = (0, -1, 1),  e_4 = (0, 0, -1)

Propagator: <dphi_a(z) dphi_b(w)> = k delta_{ab} / (z-w)^2

TARGET OUTPUTS (the 4 free + 2 checks):
  Free:
    c_334 = C^DS_{3,3;4;0,2}    (W_3 x W_3 -> W_4 coupling)
    c_444 = C^DS_{4,4;4;0,4}    (W_4 x W_4 -> W_4 self-coupling)
    C_{3,4;3;0,4}               (W_3 x W_4 -> W_3 at pole 4)
    C_{3,4;4;0,3}               (W_3 x W_4 -> W_4 at pole 3)
  Checks:
    C^res_{4,4;2;0,6} = 2       (universal T-coupling)
    C^res_{3,4;2;0,5} = 0       (mixed Virasoro vanishing)

References:
  - concordance.tex: rem:mc4-winfty-computation-target
  - w4_stage4_coefficients.py: structural analysis (72 tests)
  - w3_bar.py: W_3 OPE conventions
"""

from __future__ import annotations

from functools import lru_cache
from math import factorial
from typing import Dict, List, Optional, Tuple

from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    sqrt as sym_sqrt,
    symbols,
    together,
)


# ====================================================================
# Core data structure: differential polynomials in free bosons
# ====================================================================

# A monomial is encoded as (coeff, key) where key is a tuple of
# (boson_index, derivative_order) pairs in canonical order.
# Example: 3 :dphi_0 dphi_1: has coeff=3, key=((0,1),(1,1)).

def _canonical_key(factors: Tuple[Tuple[int, int], ...]) -> Tuple[Tuple[int, int], ...]:
    """Sort factors into canonical order: by (deriv_order DESC, index ASC)."""
    return tuple(sorted(factors, key=lambda f: (-f[1], f[0])))


class DiffPoly:
    """Normal-ordered differential polynomial in free bosons.

    Internal representation: dict mapping canonical factor-key to coefficient.
    The empty key () represents a scalar (the identity operator).
    """

    __slots__ = ('_data',)

    def __init__(self, data: Optional[Dict[Tuple[Tuple[int, int], ...], object]] = None):
        self._data: Dict[Tuple[Tuple[int, int], ...], object] = {}
        if data:
            for k, v in data.items():
                ck = _canonical_key(k)
                v_exp = expand(v)
                if v_exp != 0:
                    if ck in self._data:
                        self._data[ck] = expand(self._data[ck] + v_exp)
                    else:
                        self._data[ck] = v_exp
            # Remove zeros
            self._data = {k: v for k, v in self._data.items() if expand(v) != 0}

    @staticmethod
    def zero() -> DiffPoly:
        return DiffPoly()

    @staticmethod
    def scalar(c) -> DiffPoly:
        if expand(c) == 0:
            return DiffPoly()
        return DiffPoly({(): c})

    @staticmethod
    def dphi(idx: int, coeff=1) -> DiffPoly:
        """Single dphi_idx field."""
        return DiffPoly({((idx, 1),): coeff})

    @staticmethod
    def dnphi(idx: int, n: int, coeff=1) -> DiffPoly:
        """d^n phi_idx field."""
        return DiffPoly({((idx, n),): coeff})

    def __add__(self, other: DiffPoly) -> DiffPoly:
        result = dict(self._data)
        for k, v in other._data.items():
            if k in result:
                result[k] = expand(result[k] + v)
            else:
                result[k] = v
        return DiffPoly(result)

    def __sub__(self, other: DiffPoly) -> DiffPoly:
        result = dict(self._data)
        for k, v in other._data.items():
            if k in result:
                result[k] = expand(result[k] - v)
            else:
                result[k] = expand(-v)
        return DiffPoly(result)

    def __neg__(self) -> DiffPoly:
        return DiffPoly({k: -v for k, v in self._data.items()})

    def scale(self, c) -> DiffPoly:
        """Multiply all coefficients by scalar c."""
        return DiffPoly({k: expand(v * c) for k, v in self._data.items()})

    def __mul__(self, other: DiffPoly) -> DiffPoly:
        """Normal-ordered product (no contractions)."""
        result: Dict = {}
        for k1, v1 in self._data.items():
            for k2, v2 in other._data.items():
                key = _canonical_key(k1 + k2)
                val = expand(v1 * v2)
                if key in result:
                    result[key] = expand(result[key] + val)
                else:
                    result[key] = val
        return DiffPoly(result)

    def derivative(self) -> DiffPoly:
        """d/dz of a normal-ordered differential polynomial.

        d(:A_1 ... A_n:) = sum_i :A_1 ... (dA_i) ... A_n:
        where d(d^m phi_j) = d^{m+1} phi_j.
        """
        result: Dict = {}
        for key, coeff in self._data.items():
            if not key:
                continue  # d(scalar) = 0
            factors = list(key)
            for i in range(len(factors)):
                new_factors = list(factors)
                idx, order = new_factors[i]
                new_factors[i] = (idx, order + 1)
                new_key = _canonical_key(tuple(new_factors))
                val = coeff  # coefficient unchanged by product rule
                if new_key in result:
                    result[new_key] = expand(result[new_key] + val)
                else:
                    result[new_key] = val
        return DiffPoly(result)

    def weight(self) -> Optional[int]:
        """Conformal weight if homogeneous, else None."""
        weights = set()
        for key in self._data:
            w = sum(order for _, order in key)
            weights.add(w)
        if len(weights) == 1:
            return weights.pop()
        return None

    def get_coeff(self, key: Tuple[Tuple[int, int], ...]):
        """Get coefficient of a specific monomial."""
        ck = _canonical_key(key)
        return self._data.get(ck, 0)

    def is_zero(self) -> bool:
        return not self._data

    @property
    def terms(self) -> Dict[Tuple[Tuple[int, int], ...], object]:
        return dict(self._data)

    def filter_weight(self, w: int) -> DiffPoly:
        """Keep only terms of given conformal weight."""
        return DiffPoly({k: v for k, v in self._data.items()
                         if sum(order for _, order in k) == w})

    def __repr__(self):
        if not self._data:
            return "DiffPoly(0)"
        parts = []
        for key, coeff in sorted(self._data.items()):
            if not key:
                parts.append(str(coeff))
            else:
                factors_str = "*".join(
                    f"d{''.join(['^' + str(o)] if o > 1 else [])}phi_{i}"
                    for i, o in key
                )
                parts.append(f"{coeff}*{factors_str}")
        return "DiffPoly(" + " + ".join(parts) + ")"


# ====================================================================
# Wick contraction engine
# ====================================================================

def _propagator_coeff(m: int, n: int) -> int:
    """Contraction coefficient for d^m phi_a(z) with d^n phi_b(w).

    With <dphi_a(z) dphi_b(w)> = delta_{ab} / (z-w)^2:

      <d^m phi_a(z) d^n phi_b(w)> = (-1)^{m-1} (m+n-1)! delta_{ab} / (z-w)^{m+n}

    Returns (-1)^{m-1} * (m+n-1)! (the pole is of order m+n).
    """
    return ((-1) ** (m - 1)) * factorial(m + n - 1)


def wick_ope(A: DiffPoly, B: DiffPoly, k_level,
             max_contractions: int = 10) -> Dict[int, DiffPoly]:
    """Compute the singular part of the OPE A(z)B(w) via Wick's theorem.

    With propagator <dphi_a(z) dphi_b(w)> = k * delta_{ab} / (z-w)^2.
    Each contraction carries a factor of k_level.

    Returns {pole_order: DiffPoly} for the singular terms only (pole > 0).

    The OPE is: A(z)B(w) ~ sum_{n>0} C_n(w) / (z-w)^n + :A(w)B(w):
    This function returns {n: C_n} for n > 0.
    """
    result_data: Dict[int, Dict[Tuple, object]] = {}

    for key_a, coeff_a in A._data.items():
        for key_b, coeff_b in B._data.items():
            _wick_recurse(
                coeff_a * coeff_b,
                list(key_a), 0,  # factors of A, current index in A
                list(key_b),     # factors of B (available for contraction)
                [],              # skipped A-factors (not contracted)
                0,               # accumulated pole order
                1,               # accumulated contraction coefficient product
                result_data,
                max_contractions,
                k_level,
            )

    # Build DiffPoly for each pole
    return {p: DiffPoly(data) for p, data in result_data.items() if p > 0}


def _wick_recurse(
    outer_coeff,
    factors_a: list, a_idx: int,
    factors_b: list,
    skipped_a: list,
    pole: int, contraction_product,
    result: Dict[int, Dict],
    max_contractions: int,
    k_level,
):
    """Recursive Wick contraction.

    Process factors of A left to right. For each, either skip it or
    contract it with one available factor of B.
    """
    if a_idx >= len(factors_a):
        # All A-factors processed. Record result if we made at least one contraction.
        if pole > 0:
            remaining = tuple(skipped_a) + tuple(factors_b)
            key = _canonical_key(remaining)
            val = expand(outer_coeff * contraction_product)
            if val != 0:
                if pole not in result:
                    result[pole] = {}
                if key in result[pole]:
                    result[pole][key] = expand(result[pole][key] + val)
                else:
                    result[pole][key] = val
        return

    current_a = factors_a[a_idx]
    idx_a, order_a = current_a

    # Option 1: Skip this A-factor
    skipped_a.append(current_a)
    _wick_recurse(
        outer_coeff, factors_a, a_idx + 1,
        factors_b, skipped_a,
        pole, contraction_product,
        result, max_contractions, k_level,
    )
    skipped_a.pop()

    # Option 2: Contract with each compatible B-factor
    if max_contractions > 0:
        for j in range(len(factors_b)):
            idx_b, order_b = factors_b[j]
            if idx_a != idx_b:
                continue

            prop = _propagator_coeff(order_a, order_b) * k_level
            new_pole = pole + order_a + order_b

            # Remove B[j] from available list
            saved_b = factors_b[j]
            factors_b[j] = factors_b[-1]
            factors_b.pop()

            _wick_recurse(
                outer_coeff, factors_a, a_idx + 1,
                factors_b, skipped_a,
                new_pole, contraction_product * prop,
                result, max_contractions - 1, k_level,
            )

            # Restore B
            factors_b.append(saved_b)
            factors_b[-1], factors_b[j] = factors_b[j], factors_b[-1]


# ====================================================================
# Miura transform for sl_4
# ====================================================================

# Fundamental weights of sl_4 (in rank-3 weight space).
# These are the weights of the defining 4-dimensional representation.
SL4_FUND_WEIGHTS: List[Tuple[int, ...]] = [
    (1, 0, 0),
    (-1, 1, 0),
    (0, -1, 1),
    (0, 0, -1),
]


def _J_current(weight: Tuple[int, ...]) -> DiffPoly:
    """Free boson current J_i = sum_a e_i^a dphi_a for one weight vector."""
    result = DiffPoly()
    for a, e_a in enumerate(weight):
        if e_a != 0:
            result = result + DiffPoly.dphi(a, e_a)
    return result


def _inner_product(w1: Tuple[int, ...], w2: Tuple[int, ...]) -> int:
    """Standard inner product of weight vectors."""
    return sum(a * b for a, b in zip(w1, w2))


def miura_expand_sl4(k) -> Tuple[DiffPoly, DiffPoly, DiffPoly]:
    """Expand the Miura operator for sl_4 and extract U_2, U_3, U_4.

    L = (d + J_1)(d + J_2)(d + J_3)(d + J_4) = d^4 + U_2 d^2 + U_3 d + U_4

    This is an OPERATOR product. The key rule: (d + J_i) applied to a
    differential polynomial f(w) gives:
        (d + J_i) f = df + :J_i f:

    When we chain multiple factors, the derivative d acts on composite
    expressions. The derivatives of normal-ordered products are:
        d(:J_i ... J_j f:) = :dJ_i ... J_j f: + ... + :J_i ... dJ_j f: + :J_i ... J_j df:

    Since dJ_i = sum_a e_i^a d^2phi_a (no contractions arise from
    classical differentiation of a normal-ordered expression), the
    quantum corrections come entirely from the ORDERING of the factors
    in the operator product expansion.

    Concretely, for (d + A)(d + B):
        (d + A)(d + B) = d^2 + (A + B)d + (AB + dB)
    where AB = :AB: is the NORMAL-ORDERED product and dB is the
    ordinary derivative. At the classical level this is correct.
    The QUANTUM correction arises when we have:
        (d + A)(d + B)f = d(df + Bf) + A(df + Bf)
                        = d^2f + dBf + Bdf + Adf + ABf
                        = d^2f + (A+B)df + (AB + dB)f

    But AB here means the operator product A(z)B(z), which at the
    quantum level is :AB: + <AB> (OPE self-contraction at z=w).
    The self-contraction <J_i(z)J_j(z)> is formally infinite and
    is DISCARDED in normal ordering. So AB = :AB: here, and the
    quantum corrections come from the HIGHER operators.

    Actually, the quantum correction in the Miura transform arises
    because (d + J)(f) = df + Jf includes Jf as a normal-ordered product,
    but when we apply d to Jf, we get d(Jf) = (dJ)f + J(df). The term
    dJ = d/dz J(z) is the derivative of the current. When J_i comes from
    an earlier factor (further left), the d from a later factor does NOT
    act on it (the product is already normal-ordered). The quantum
    correction comes from the Weyl vector term rho.dphi which shifts T.

    For the principal embedding, the exact result is known:
    the quantum Miura transform gives (see Fateev-Lukyanov 1988):

        T = sum_{i<j} :J_i J_j: + rho . d^2phi
        W_3 = sum_{i<j<k} :J_i J_j J_k: + ...
        W_4 = :J_1 J_2 J_3 J_4: + ...

    where rho = half-sum of positive roots.

    For practical computation: the "classical" expansion (treating d
    as a formal variable commuting with J) gives the CORRECT result
    because the quantum correction from [d, J_i] = dJ_i is already
    included in our expansion rule (d + J_i)f = df + J_i f, where the
    dJ_i terms arise when d hits J_j for j > i in the chain.

    Let me verify: for (d + J_1)(d + J_2)f:
        = (d + J_1)(df + J_2 f)
        = d(df) + d(J_2 f) + J_1(df) + J_1(J_2 f)
        = d^2f + (dJ_2)f + J_2(df) + J_1(df) + :J_1 J_2: f
        = d^2f + (J_1 + J_2)df + (:J_1 J_2: + dJ_2)f

    So U_0 = :J_1 J_2: + dJ_2 (for the two-factor case).
    The dJ_2 term is the quantum correction. This is NOT present in the
    naive classical product J_1 J_2, but IS present in our expansion
    because d acts on J_2 f and produces (dJ_2)f + J_2(df).

    So our iterative expansion is correct: start from the right and
    apply (d + J_i) as an operator.
    """
    Js = [_J_current(w) for w in SL4_FUND_WEIGHTS]

    # Represent the operator as a polynomial in d:
    # sum_{j=0}^{n} A_j d^j  where A_j are DiffPolys.
    # Initialize with the rightmost factor: (d + J_4) = 1*d^1 + J_4*d^0
    coeffs: Dict[int, DiffPoly] = {0: Js[3], 1: DiffPoly.scalar(1)}

    # Multiply on the left by (d + J_i) for i = 3, 2, 1 (indices 2, 1, 0)
    for i in [2, 1, 0]:
        J = Js[i]
        new_coeffs: Dict[int, DiffPoly] = {}

        for j, A_j in coeffs.items():
            # (d + J) * (A_j d^j) = d(A_j d^j) + J(A_j d^j)
            #                     = (dA_j)d^j + A_j d^{j+1} + (J*A_j)d^j

            # J * A_j term at d^j
            JA = J * A_j
            if j in new_coeffs:
                new_coeffs[j] = new_coeffs[j] + JA
            else:
                new_coeffs[j] = JA

            # dA_j term at d^j
            dA = A_j.derivative()
            if j in new_coeffs:
                new_coeffs[j] = new_coeffs[j] + dA
            else:
                new_coeffs[j] = dA

            # A_j at d^{j+1}
            if j + 1 in new_coeffs:
                new_coeffs[j + 1] = new_coeffs[j + 1] + A_j
            else:
                new_coeffs[j + 1] = A_j

        coeffs = new_coeffs

    # coeffs[4] = 1 (coefficient of d^4)
    # coeffs[3] = J_1 + J_2 + J_3 + J_4 = 0 (weights sum to zero)
    # coeffs[2] = U_2
    # coeffs[1] = U_3
    # coeffs[0] = U_4
    U2 = coeffs.get(2, DiffPoly())
    U3 = coeffs.get(1, DiffPoly())
    U4 = coeffs.get(0, DiffPoly())

    return U2, U3, U4


# ====================================================================
# Central charge and generator extraction
# ====================================================================

def extract_central_charge_from_ope(T: DiffPoly, k) -> object:
    """Extract c from T(z)T(w) ~ c/2 / (z-w)^4 + ..."""
    ope = wick_ope(T, T, k)
    if 4 not in ope:
        return 0
    # Quartic pole should be a scalar
    scalar = ope[4]._data.get((), 0)
    return expand(2 * scalar)


def make_primary_w4(U2: DiffPoly, U3: DiffPoly, U4: DiffPoly,
                     k) -> DiffPoly:
    """Adjust U_4 to be primary w.r.t. T = U_2.

    We set W_4 = U_4 + a * d^2 U_2 + b * dU_3 and determine a, b
    so that T(z)W_4(w) has no poles of order > 2 (i.e., W_4 is primary
    of conformal weight 4 under T).

    T(z)W_4(w) should have the form:
      4 W_4(w) / (z-w)^2 + dW_4(w) / (z-w) + (regular)

    So poles 3, 4, 5, 6 must vanish.
    """
    T = U2
    dT = T.derivative()
    d2T = dT.derivative()
    dU3 = U3.derivative()

    # Compute OPEs: T with U_4, d^2T, dU_3
    ope_TU4 = wick_ope(T, U4, k)
    ope_Td2T = wick_ope(T, d2T, k)
    ope_TdU3 = wick_ope(T, dU3, k)

    # Collect all pole orders > 2 and all monomial keys at those poles
    a_sym, b_sym = symbols('_a _b')

    equations = []
    for p in sorted(set(list(ope_TU4.keys()) + list(ope_Td2T.keys()) + list(ope_TdU3.keys()))):
        if p <= 2:
            continue
        # Collect all monomial keys at this pole
        all_keys = set()
        for ope_dict in [ope_TU4, ope_Td2T, ope_TdU3]:
            if p in ope_dict:
                all_keys.update(ope_dict[p]._data.keys())

        for key in all_keys:
            c_U4 = ope_TU4[p]._data.get(key, 0) if p in ope_TU4 else 0
            c_d2T = ope_Td2T[p]._data.get(key, 0) if p in ope_Td2T else 0
            c_dU3 = ope_TdU3[p]._data.get(key, 0) if p in ope_TdU3 else 0
            eq = expand(c_U4 + a_sym * c_d2T + b_sym * c_dU3)
            if eq != 0:
                equations.append(eq)

    from sympy import solve
    if not equations:
        return U4  # Already primary

    solution = solve(equations, [a_sym, b_sym], dict=True)
    if isinstance(solution, list) and len(solution) > 0:
        solution = solution[0]
    elif not isinstance(solution, dict):
        solution = {}
    a_val = solution.get(a_sym, 0)
    b_val = solution.get(b_sym, 0)

    W4 = U4 + d2T.scale(a_val) + dU3.scale(b_val)
    return W4


def make_primary_w3(U2: DiffPoly, U3: DiffPoly, k) -> DiffPoly:
    """Check and adjust U_3 to be primary w.r.t. T = U_2.

    For the principal sl_4 embedding, U_3 should already be primary.
    This function verifies and corrects if needed.

    T(z)W_3(w) should have the form:
      3 W_3(w) / (z-w)^2 + dW_3(w) / (z-w) + (regular)
    """
    T = U2
    dT = T.derivative()

    ope_TU3 = wick_ope(T, U3, k)

    # Check for poles > 2
    has_higher_poles = any(p > 2 for p in ope_TU3 if not ope_TU3[p].is_zero())

    if not has_higher_poles:
        return U3  # Already primary

    # Correction: W_3 = U_3 + a * dT (the only weight-3 derivative correction)
    a_sym = Symbol('_a3')
    ope_TdT = wick_ope(T, dT, k)

    equations = []
    for p in sorted(ope_TU3.keys()):
        if p <= 2:
            continue
        all_keys = set(ope_TU3[p]._data.keys())
        if p in ope_TdT:
            all_keys.update(ope_TdT[p]._data.keys())

        for key in all_keys:
            c_U3 = ope_TU3[p]._data.get(key, 0) if p in ope_TU3 else 0
            c_dT = ope_TdT[p]._data.get(key, 0) if p in ope_TdT else 0
            eq = expand(c_U3 + a_sym * c_dT)
            if eq != 0:
                equations.append(eq)

    from sympy import solve
    if not equations:
        return U3

    solution = solve(equations, [a_sym], dict=True)
    if isinstance(solution, list) and len(solution) > 0:
        solution = solution[0]
    elif not isinstance(solution, dict):
        solution = {}
    a_val = solution.get(a_sym, 0)
    return U3 + dT.scale(a_val)


# ====================================================================
# Normalization helpers
# ====================================================================

def _extract_scalar(dp: DiffPoly) -> object:
    """Extract the scalar (identity operator) part of a DiffPoly."""
    return dp._data.get((), 0)


def _extract_along(dp: DiffPoly, target: DiffPoly) -> object:
    """Extract the coefficient of 'target' in 'dp'.

    Finds C such that dp = C * target + (other terms orthogonal to target).
    Uses the first nonzero monomial of target as a reference.
    """
    if not target._data:
        return 0
    ref_key = next(iter(target._data))
    ref_coeff = target._data[ref_key]
    if expand(ref_coeff) == 0:
        return 0
    dp_coeff = dp._data.get(ref_key, 0)
    return cancel(dp_coeff / ref_coeff)


# ====================================================================
# Full OPE coefficient extraction at a given level k
# ====================================================================

def compute_generators(k) -> Dict[str, DiffPoly]:
    """Compute the primary generators T, W_3, W_4 at level k.

    Returns a dict with keys 'T', 'W3', 'W4'.
    """
    U2, U3, U4 = miura_expand_sl4(k)
    T = U2
    W3 = make_primary_w3(U2, U3, k)
    W4 = make_primary_w4(U2, W3, U4, k)
    return {'T': T, 'W3': W3, 'W4': W4}


def extract_all_ope_data(k) -> Dict[str, object]:
    """Extract all OPE data at a specific level k.

    Returns a dict with:
    - Central charge c
    - All stage-3 and stage-4 OPE coefficients
    - Normalization data
    - Primaryity verification flags
    """
    gens = compute_generators(k)
    T, W3, W4 = gens['T'], gens['W3'], gens['W4']

    # Central charge
    ope_TT = wick_ope(T, T, k)
    c = expand(2 * _extract_scalar(ope_TT.get(4, DiffPoly())))

    # Verify primaryity of W_3 and W_4
    ope_TW3 = wick_ope(T, W3, k)
    ope_TW4 = wick_ope(T, W4, k)

    w3_primary = all(ope_TW3.get(p, DiffPoly()).is_zero() for p in range(3, 10))
    w4_primary = all(ope_TW4.get(p, DiffPoly()).is_zero() for p in range(3, 10))

    # Stage-3 coefficients
    # C_{2,2;2;0,2}: T at pole 2 in TxT
    stage3_TT = _extract_along(ope_TT.get(2, DiffPoly()), T)

    # C_{2,3;3;0,2}: W3 at pole 2 in TxW3 (should be 3 for weight-3 primary)
    stage3_TW = _extract_along(ope_TW3.get(2, DiffPoly()), W3)

    # Two-point normalizations: W_3 x W_3 at pole 6, W_4 x W_4 at pole 8
    ope_W3W3 = wick_ope(W3, W3, k)
    ope_W4W4 = wick_ope(W4, W4, k)

    N3 = _extract_scalar(ope_W3W3.get(6, DiffPoly()))  # <W3 W3> ~ N3/(z-w)^6
    N4 = _extract_scalar(ope_W4W4.get(8, DiffPoly()))  # <W4 W4> ~ N4/(z-w)^8

    # C_{3,3;2;0,4}: T at pole 4 in W3xW3
    raw_33_T4 = _extract_along(ope_W3W3.get(4, DiffPoly()), T)

    # Normalize: if W3 -> alpha*W3 with alpha^2 = (c/3)/N3, then
    # C_{3,3;2;0,4} = alpha^2 * raw_33_T4 = (c/3)/N3 * raw_33_T4
    alpha3_sq = cancel(Rational(1, 3) * c / N3) if expand(N3) != 0 else 1
    stage3_WW = cancel(alpha3_sq * raw_33_T4) if expand(N3) != 0 else 0

    # Similarly for W4 normalization
    alpha4_sq = cancel(Rational(1, 4) * c / N4) if expand(N4) != 0 else 1

    # ----- Stage-4 coefficients -----

    # c_334: W4 at pole 2 in W3xW3
    # normalized: alpha3^2 / alpha4 * raw
    # c_334 = alpha3^2 * raw / sqrt(alpha4^2)
    raw_33_W4_2 = _extract_along(ope_W3W3.get(2, DiffPoly()), W4)

    # For the self-normalized coefficient: the W_3 normalization is fixed by
    # requiring C_{3,3;2;0,4} = 2. Let's define alpha3_sq_2 for this:
    # alpha3_sq_2 * raw_33_T4 = 2  =>  alpha3_sq_2 = 2 / raw_33_T4
    alpha3_sq_2 = cancel(Rational(2) / raw_33_T4) if expand(raw_33_T4) != 0 else 1

    # With this normalization, the W_3 two-point function is
    # N3_normalized = alpha3_sq_2 * N3

    # The c_334 with this normalization is:
    # c_334 = alpha3_sq_2 * raw_33_W4_2 / sqrt(alpha4_sq_eff)
    # where alpha4_sq_eff normalizes W4 by its two-point function.
    # But what IS the W4 normalization? We use c/4 convention:
    # alpha4^2 * N4 = c/4  =>  alpha4^2 = (c/4)/N4
    # So c_334 = alpha3_sq_2 * raw_33_W4_2 / sqrt((c/4)/N4)
    #          = alpha3_sq_2 * raw_33_W4_2 * sqrt(N4) / sqrt(c/4)

    # To avoid square roots, compute c_334^2:
    # c_334^2 = alpha3_sq_2^2 * raw_33_W4_2^2 * N4 / (c/4)
    #         = alpha3_sq_2^2 * raw_33_W4_2^2 * 4*N4/c
    c334_sq = cancel(alpha3_sq_2 ** 2 * raw_33_W4_2 ** 2 * 4 * N4 / c) if expand(c) != 0 else 0

    # C_{4,4;2;0,6}: T at pole 6 in W4xW4
    raw_44_T6 = _extract_along(ope_W4W4.get(6, DiffPoly()), T)
    C_res_44_2_06 = cancel(alpha4_sq * raw_44_T6)

    # W3 x W4 OPE
    ope_W3W4 = wick_ope(W3, W4, k)

    # C_{3,4;2;0,5}: T at pole 5 in W3xW4
    raw_34_T5 = _extract_along(ope_W3W4.get(5, DiffPoly()), T)
    # This should be zero. The normalization factor cancels if raw is 0.
    C_res_34_2_05_zero = (expand(raw_34_T5) == 0)

    # C_{3,4;3;0,4}: W3 at pole 4 in W3xW4
    # With W3 norm alpha3 and W4 norm alpha4:
    # (alpha3 W3)(z)(alpha4 W4)(w) ~ ... + C * (alpha3 W3)/(z-w)^4 + ...
    # alpha3 * alpha4 * raw = C * alpha3
    # C = alpha4 * raw
    # C^2 = alpha4^2 * raw^2 = alpha4_sq * raw^2
    raw_34_W3_4 = _extract_along(ope_W3W4.get(4, DiffPoly()), W3)

    # But we also need the correct alpha for the W3-normalization convention.
    # Using the manuscript convention (C_{3,3;2;0,4} = 2):
    # alpha3 = sqrt(alpha3_sq_2), alpha4 = sqrt(alpha4_sq)
    # C_{3,4;3;0,4} = sqrt(alpha3_sq_2) * sqrt(alpha4_sq) * raw / sqrt(alpha3_sq_2)
    #               = sqrt(alpha4_sq) * raw
    # C^2 = alpha4_sq * raw^2
    # Normalization: (alpha3 W3)(alpha4 W4) at pole 4 contains C * (alpha3 W3).
    # So alpha3 * alpha4 * raw_34_W3_4 = C * alpha3, giving C = alpha4 * raw.
    # Here alpha4^2 = (c/4)/N4  (the alpha4_sq we computed above).
    C_34_3_04_sq = cancel(alpha4_sq * raw_34_W3_4 ** 2)

    # C_{3,4;4;0,3}: W4 at pole 3 in W3xW4
    # (alpha3 W3)(alpha4 W4) at pole 3 contains C * (alpha4 W4).
    # alpha3 * alpha4 * raw = C * alpha4
    # C = alpha3 * raw
    # C^2 = alpha3^2 * raw^2
    # Here alpha3^2 = alpha3_sq_2 (the one that gives C_{3,3;2;0,4}=2).
    raw_34_W4_3 = _extract_along(ope_W3W4.get(3, DiffPoly()), W4)
    C_34_4_03_sq = cancel(alpha3_sq_2 * raw_34_W4_3 ** 2)

    # c_444: W4 at pole 4 in W4xW4
    # (alpha4 W4)(alpha4 W4) at pole 4 contains C * (alpha4 W4).
    # alpha4^2 * raw = C * alpha4
    # C = alpha4 * raw
    # C^2 = alpha4^2 * raw^2
    raw_44_W4_4 = _extract_along(ope_W4W4.get(4, DiffPoly()), W4)
    c444_sq = cancel(alpha4_sq * raw_44_W4_4 ** 2)

    return {
        'k': k,
        'c': cancel(c),
        # Primaryity
        'w3_primary': w3_primary,
        'w4_primary': w4_primary,
        # Raw normalizations
        'N3': cancel(N3),
        'N4': cancel(N4),
        'alpha3_sq': cancel(alpha3_sq),
        'alpha4_sq': cancel(alpha4_sq),
        'alpha3_sq_2': cancel(alpha3_sq_2),
        # Stage-3 verification
        'stage3_TT': cancel(stage3_TT),
        'stage3_TW': cancel(stage3_TW),
        'stage3_WW': cancel(stage3_WW),
        # Stage-4 free coefficients (squared)
        'c334_sq': cancel(c334_sq),
        'c444_sq': cancel(c444_sq),
        'C_34_3_04_sq': cancel(C_34_3_04_sq),
        'C_34_4_03_sq': cancel(C_34_4_03_sq),
        # Stage-4 residue checks
        'C_res_44_2_06': cancel(C_res_44_2_06),
        'C_res_34_2_05_zero': C_res_34_2_05_zero,
        # Raw data for debugging
        'raw_33_T4': cancel(raw_33_T4),
        'raw_33_W4_2': cancel(raw_33_W4_2),
        'raw_44_T6': cancel(raw_44_T6),
        'raw_34_T5': cancel(raw_34_T5),
        'raw_34_W3_4': cancel(raw_34_W3_4),
        'raw_34_W4_3': cancel(raw_34_W4_3),
        'raw_44_W4_4': cancel(raw_44_W4_4),
    }


# ====================================================================
# Central charge
# ====================================================================

def w4_central_charge(k):
    """Central charge c(k) = 3 - 60(k+3)^2/(k+4) for principal W_4."""
    return 3 - Rational(60) * (k + 3) ** 2 / (k + 4)


def w4_complementarity_sum():
    """c(k) + c(-k-8) for the W_4 algebra. Should be 246."""
    k = Symbol('k')
    return simplify(w4_central_charge(k) + w4_central_charge(-k - 8))


# ====================================================================
# Multi-k interpolation
# ====================================================================

def interpolate_rational_func(data_points: List[Tuple], var_name: str = 'k',
                               degree_num: int = 4, degree_den: int = 2):
    """Interpolate a rational function from (x, f(x)) sample points.

    Constructs P(x)/Q(x) with Q monic of the specified degree.

    Args:
        data_points: List of (x_i, f_i) pairs (exact rationals).
        var_name: Name of the variable.
        degree_num: Degree of numerator.
        degree_den: Degree of denominator.

    Returns:
        Rational function of Symbol(var_name), or None if underdetermined.
    """
    from sympy import Matrix, Rational as R, zeros as _zeros

    x = Symbol(var_name)
    n_params = degree_num + 1 + degree_den  # Q is monic, so leading coeff fixed
    if len(data_points) < n_params:
        return None

    # Build linear system: P(x_i) = f_i * Q(x_i) for each data point.
    # P = a_0 + a_1 x + ... + a_{d_n} x^{d_n}
    # Q = 1 + b_1 x + ... + b_{d_d-1} x^{d_d-1} + x^{d_d}  (monic)
    # Unknowns: a_0, ..., a_{d_n}, b_1, ..., b_{d_d-1}
    # Wait, we normalize Q(0) = 1 instead (constant term 1):
    # Q = 1 + b_1 x + ... + b_{d_d} x^{d_d}
    # n_params = (d_n + 1) + d_d

    M = _zeros(len(data_points), n_params)
    rhs = _zeros(len(data_points), 1)

    for i, (xi, fi) in enumerate(data_points):
        xi = R(xi) if isinstance(xi, int) else xi
        fi = R(fi) if isinstance(fi, int) else fi
        # P(xi): a_0 + a_1 xi + ... + a_{d_n} xi^{d_n}
        for j in range(degree_num + 1):
            M[i, j] = xi ** j
        # -fi * Q(xi) = -fi * (1 + b_1 xi + ... + b_{d_d} xi^{d_d})
        # Move -fi*1 to RHS
        rhs[i, 0] = fi
        for j in range(1, degree_den + 1):
            M[i, degree_num + j] = -fi * xi ** j

    try:
        sol = M.solve(rhs)
    except Exception:
        return None

    P = sum(sol[j] * x ** j for j in range(degree_num + 1))
    Q = 1 + sum(sol[degree_num + j] * x ** j for j in range(1, degree_den + 1))
    return cancel(P / Q)


# ====================================================================
# Runner
# ====================================================================

if __name__ == "__main__":
    from sympy import Rational as R, pprint

    print("=" * 70)
    print("W_4 DS OPE EXTRACTION VIA MIURA TRANSFORM")
    print("=" * 70)

    k_test = R(1)
    print(f"\nTesting at k = {k_test}")
    print(f"Expected central charge: c = {w4_central_charge(k_test)}")

    print("\n--- Miura expansion ---")
    U2, U3, U4 = miura_expand_sl4(k_test)
    print(f"  U2: {len(U2._data)} monomials")
    print(f"  U3: {len(U3._data)} monomials")
    print(f"  U4: {len(U4._data)} monomials")

    print("\n--- Central charge from OPE ---")
    c_ope = extract_central_charge_from_ope(U2, k_test)
    c_expected = w4_central_charge(k_test)
    print(f"  Extracted: c = {c_ope}")
    print(f"  Expected:  c = {c_expected}")
    print(f"  Match: {simplify(c_ope - c_expected) == 0}")

    print("\n--- Full extraction ---")
    data = extract_all_ope_data(k_test)
    for key in sorted(data.keys()):
        print(f"  {key} = {data[key]}")
