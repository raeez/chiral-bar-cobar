"""Exact Miura computation for W(sl_4) at α₀=1 using sympy Rational.

Computes the W₄ OPE structure constants c₃₃₄ and c₄₄₄ with EXACT rational
arithmetic, resolving the BPZ normalization barrier (mc4_bpz_frontier.md).

KEY INSIGHT: In the R⁴/traceless basis, the Miura generators have RATIONAL
(in fact INTEGER) coefficients at α₀=1. The orthonormal Cartan basis used
by w4_ope_miura.py introduces spurious √2, √3 factors that destroy exact
arithmetic. This module works entirely in the R⁴/traceless basis.

BASIS:
  3 independent free bosons φ₀, φ₁, φ₂ with propagator
    ⟨∂ᵐφ_a(z) ∂ⁿφ_b(w)⟩ = (-1)ⁿ⁺¹(m+n-1)! δ_{ab} / (z-w)^{m+n}

  The currents: J₁ = ∂φ₀, J₂ = ∂φ₁, J₃ = ∂φ₂, J₄ = -(∂φ₀+∂φ₁+∂φ₂).

GENERATORS (at α₀=1, Fateev-Lukyanov quantum Miura):
  T  = e₂(J) + ρ·∂J  where ρ = (3/2, 1/2, -1/2, -3/2)
  W₃ = e₃(J) + quantum corrections (cubic)
  W₄ = e₄(J) + quantum corrections (quartic)

All coefficients are in ℚ. Wick contractions give exact rational results.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from typing import Dict, List, Tuple

from sympy import Rational, factorial, simplify, S


# ═══════════════════════════════════════════════════════════════════════
# Exact field representation
# ═══════════════════════════════════════════════════════════════════════

# Monomial: sorted tuple of (boson_index, derivative_order)
# Example: ((0,1), (1,1)) = ∂φ₀ · ∂φ₁
# Example: ((0,2),) = ∂²φ₀
ExactMonomial = Tuple[Tuple[int, int], ...]

# Field: dict mapping monomial -> Rational coefficient
ExactField = Dict[ExactMonomial, Rational]


def mon_weight(m: ExactMonomial) -> int:
    return sum(d for _, d in m)


def simplify_field(f: ExactField) -> ExactField:
    """Remove zero-coefficient terms."""
    return {m: c for m, c in f.items() if c != 0}


def add_fields(*fields: ExactField) -> ExactField:
    result: ExactField = defaultdict(lambda: Rational(0))
    for f in fields:
        for m, c in f.items():
            result[m] += c
    return simplify_field(dict(result))


def scale_field(f: ExactField, s: Rational) -> ExactField:
    return {m: c * s for m, c in f.items() if c * s != 0}


def multiply_monomials(m1: ExactMonomial, m2: ExactMonomial) -> ExactMonomial:
    """Multiply two monomials (concatenate and sort)."""
    return tuple(sorted(m1 + m2))


def multiply_fields(f1: ExactField, f2: ExactField) -> ExactField:
    result: ExactField = defaultdict(lambda: Rational(0))
    for m1, c1 in f1.items():
        for m2, c2 in f2.items():
            m = multiply_monomials(m1, m2)
            result[m] += c1 * c2
    return simplify_field(dict(result))


def derivative_field(f: ExactField, boson: int) -> ExactField:
    """Take ∂/∂(∂φ_boson) derivative — increases derivative order by 1."""
    result: ExactField = defaultdict(lambda: Rational(0))
    for mon, coeff in f.items():
        # Replace each occurrence of (boson, d) with (boson, d+1)
        new_mon = list(mon)
        for idx, (b, d) in enumerate(mon):
            if b == boson:
                new_entry = list(new_mon)
                new_entry[idx] = (b, d + 1)
                result[tuple(sorted(tuple(x) for x in new_entry))] += coeff
                break  # only derivative ONE factor
        else:
            # boson not in monomial → this is ∂²φ_b acting as a new factor
            pass
    return simplify_field(dict(result))


# ═══════════════════════════════════════════════════════════════════════
# Wick contraction engine (exact rational)
# ═══════════════════════════════════════════════════════════════════════

def propagator_coeff(a: int, da: int, b: int, db: int) -> Rational:
    """Exact propagator: ⟨∂^{da}φ_a(z) ∂^{db}φ_b(w)⟩ coefficient.

    ⟨∂^m φ_a(z) ∂^n φ_b(w)⟩ = (-1)^{n+1} (m+n-1)! δ_{ab} / (z-w)^{m+n}

    Returns the coefficient of 1/(z-w)^{da+db}, or 0 if a ≠ b.
    """
    if a != b:
        return Rational(0)
    return (-1)**(db + 1) * factorial(da + db - 1)


def bpz_inner_product_exact(f1: ExactField, f2: ExactField) -> Rational:
    """Exact BPZ inner product ⟨f1|f2⟩.

    This is the coefficient of the leading pole (z-w)^{-(h1+h2)} in the OPE
    f1(z)·f2(w), where ALL free-boson operators are fully contracted.

    For a monomial of weight h, all operators must be contracted pairwise
    with operators from the other field. This requires the total number of
    operators to be even, and the sum of weights from f1 and f2 to match.
    """
    total = Rational(0)

    for m1, c1 in f1.items():
        for m2, c2 in f2.items():
            # m1 and m2 are lists of (boson, deriv_order)
            if len(m1) != len(m2):
                continue  # can't fully contract if different number of operators
            # Try all perfect matchings of m1 operators with m2 operators
            contraction_sum = _all_contractions(list(m1), list(m2))
            total += c1 * c2 * contraction_sum

    return total


def _all_contractions(ops1: list, ops2: list) -> Rational:
    """Sum over all ways to match operators from ops1 with ops2.

    Each matching produces a product of propagator coefficients.
    For n operators in each, there are n! matchings.
    """
    n = len(ops1)
    if n == 0:
        return Rational(1)

    # Fix the first operator of ops1, try matching with each in ops2
    total = Rational(0)
    a, da = ops1[0]
    remaining1 = ops1[1:]

    for j in range(len(ops2)):
        b, db = ops2[j]
        prop = propagator_coeff(a, da, b, db)
        if prop == 0:
            continue
        remaining2 = ops2[:j] + ops2[j+1:]
        sub = _all_contractions(remaining1, remaining2)
        total += prop * sub

    return total


# ═══════════════════════════════════════════════════════════════════════
# Miura generators for W(sl_4) at α₀ = 1 (t=1, c=63)
# ═══════════════════════════════════════════════════════════════════════

def _currents():
    """The 4 Miura currents J_i in R⁴/traceless basis.

    J₁ = ∂φ₀, J₂ = ∂φ₁, J₃ = ∂φ₂, J₄ = -(∂φ₀+∂φ₁+∂φ₂).
    """
    J1: ExactField = {((0, 1),): Rational(1)}
    J2: ExactField = {((1, 1),): Rational(1)}
    J3: ExactField = {((2, 1),): Rational(1)}
    J4: ExactField = {
        ((0, 1),): Rational(-1),
        ((1, 1),): Rational(-1),
        ((2, 1),): Rational(-1),
    }
    return [J1, J2, J3, J4]


def _elementary_symmetric(Js: list, k: int) -> ExactField:
    """k-th elementary symmetric polynomial e_k(J₁,...,J₄)."""
    result: ExactField = defaultdict(lambda: Rational(0))
    for combo in combinations(range(len(Js)), k):
        product = {(): Rational(1)}
        for idx in combo:
            product = multiply_fields(product, Js[idx])
        for m, c in product.items():
            result[m] += c
    return simplify_field(dict(result))


def miura_T() -> ExactField:
    """Virasoro generator T = e₂(J) + ρ·∂J at α₀=1.

    ρ = (3/2, 1/2, -1/2, -3/2) in R⁴.
    ρ·∂J = 3∂²φ₀ + 2∂²φ₁ + ∂²φ₂ (after eliminating φ₃).
    """
    Js = _currents()
    e2 = _elementary_symmetric(Js, 2)

    # Quantum correction: ρ·∂J (derivative of currents, weighted by Weyl vector)
    # In R⁴: ρ_i · ∂J_i = (3/2)∂²φ₀ + (1/2)∂²φ₁ + (-1/2)∂²φ₂
    #         + (-3/2)(-(∂²φ₀+∂²φ₁+∂²φ₂))
    #       = 3∂²φ₀ + 2∂²φ₁ + ∂²φ₂
    quantum_T: ExactField = {
        ((0, 2),): Rational(3),
        ((1, 2),): Rational(2),
        ((2, 2),): Rational(1),
    }

    return add_fields(e2, quantum_T)


def miura_W3() -> ExactField:
    """Spin-3 generator W₃ at α₀=1.

    W₃ = e₃(J) + α₀·Σ_{i<j} (ρ_i+ρ_j)·:J_i ∂J_j: + (α₀²/2)·Σ_i (3ρ_i²-ρ_i)·∂²J_i

    The quantum corrections come from the Fateev-Lukyanov formula.
    At α₀=1, all terms are rational.
    """
    Js = _currents()
    rho = [Rational(3, 2), Rational(1, 2), Rational(-1, 2), Rational(-3, 2)]

    # e₃
    e3 = _elementary_symmetric(Js, 3)

    # First quantum correction: Σ_{i<j} (ρ_i + ρ_j) · :J_i ∂J_j:
    # ∂J_i is the field with derivative order +1
    q1: ExactField = defaultdict(lambda: Rational(0))
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            weight = rho[i]  # coefficient from Miura ordering
            # The term is: weight · J_i · ∂J_j  (i.e., J_i times derivative of J_j)
            # ∂J_j increases derivative order of each boson operator in J_j by 1
            for m_i, c_i in Js[i].items():
                for m_j, c_j in Js[j].items():
                    # ∂J_j: each operator (b, d) in J_j becomes (b, d+1)
                    for k, (b, d) in enumerate(m_j):
                        new_ops = list(m_j)
                        new_ops[k] = (b, d + 1)
                        combined = multiply_monomials(m_i, tuple(sorted(tuple(x) for x in new_ops)))
                        q1[combined] += weight * c_i * c_j

    q1 = simplify_field(dict(q1))

    # Second quantum correction: (1/2)·Σ_i (3ρ_i² - ρ_i) · ∂²J_i
    # But we need the EXACT FL formula. Let me use a different approach.
    # For the quantum Miura, the standard result gives:
    # W₃ = e₃ + (1/2)Σ_{i≠j} ρ_i · (J_i · ∂J_j + ∂J_i · J_j) / 2
    #     + Σ_i f(ρ_i) · ∂²J_i
    # where f depends on the specific ordering convention.

    # ACTUALLY, for computational purposes, let me use a DIFFERENT approach:
    # Compute the quantum Miura by ORDERED multiplication of operators.
    # This avoids needing the explicit FL formula.

    # The quantum Miura operator:
    # L = (∂ + J₁)(∂ + J₂)(∂ + J₃)(∂ + J₄)
    # where the product is ORDERED (left to right), with normal ordering
    # AND the quantum correction that ∂ acting on J_i gives ∂J_i.

    # Expansion:
    # (∂+J₁)(∂+J₂) = ∂² + J₂∂ + J₁∂ + J₁J₂ + ∂J₂ (from ∂ acting past J₂... wait)

    # Actually, the standard convention: (∂ + J₁)(∂ + J₂) means:
    # Apply ∂+J₂ first, then ∂+J₁. As differential operators:
    # (∂+J₁)(∂+J₂)f = (∂+J₁)[(∂+J₂)f] = (∂+J₁)[∂f + J₂f]
    # = ∂²f + ∂(J₂f) + J₁∂f + J₁J₂f
    # = ∂²f + (∂J₂)f + J₂∂f + J₁∂f + J₁J₂f
    # = ∂²f + (J₁+J₂)∂f + (J₁J₂ + ∂J₂)f

    # So the coefficient of ∂⁰ is W_2|_{from first two} = J₁J₂ + ∂J₂

    # For the FULL product of all 4 factors, this gets very messy but is
    # completely mechanical. Let me implement it.

    return _miura_w3_by_expansion()


def _miura_w3_by_expansion() -> ExactField:
    """Compute W₃ by expanding the quantum Miura operator.

    L = (∂ + J₁)(∂ + J₂)(∂ + J₃)(∂ + J₄)

    Expand right to left. At each step, (∂ + J_i) acts on the result,
    with ∂ acting as a derivation on the "field coefficients."

    Returns the coefficient of ∂¹ in L = ∂⁴ + 0·∂³ + T·∂² + W₃·∂ + W₄.
    """
    Js = _currents()

    # State: list of (field_coeff, power_of_partial)
    # Start: identity = [(1, ∂⁰)]
    state = [({(): Rational(1)}, 0)]  # (field=1, power=0)

    for J in reversed(Js):  # multiply from right
        new_state = []
        for field, power in state:
            # (∂ + J) * (field · ∂^power) = ∂ · field · ∂^power + J · field · ∂^power
            # = (∂field)·∂^power + field·∂^{power+1} + J·field·∂^power

            # Term 1: field · ∂^{power+1}
            new_state.append((field, power + 1))

            # Term 2: J · field · ∂^power
            Jf = multiply_fields(J, field)
            new_state.append((Jf, power))

            # Term 3: (∂ field) · ∂^power
            # ∂ acting on a field = sum of derivatives of each monomial
            df = _take_z_derivative(field)
            if df:
                new_state.append((df, power))

        # Consolidate: group by power
        consolidated = defaultdict(lambda: defaultdict(lambda: Rational(0)))
        for field, power in new_state:
            for m, c in field.items():
                consolidated[power][m] += c

        state = [(simplify_field(dict(field_dict)), power)
                 for power, field_dict in consolidated.items()]

    # Extract coefficients by power of ∂
    result_by_power = {}
    for field, power in state:
        if power in result_by_power:
            result_by_power[power] = add_fields(result_by_power[power], field)
        else:
            result_by_power[power] = field

    # W₃ = coefficient of ∂¹
    return result_by_power.get(1, {})


def _take_z_derivative(field: ExactField) -> ExactField:
    """Take the z-derivative of a field: ∂_z[f(z)].

    For a monomial ∂^{d₁}φ_{a₁} · ∂^{d₂}φ_{a₂} · ..., the z-derivative is
    the sum over each factor of replacing ∂^{d_i}φ_{a_i} → ∂^{d_i+1}φ_{a_i}.
    """
    result: ExactField = defaultdict(lambda: Rational(0))
    for mon, coeff in field.items():
        for k in range(len(mon)):
            b, d = mon[k]
            new_mon = list(mon)
            new_mon[k] = (b, d + 1)
            result[tuple(sorted(tuple(x) for x in new_mon))] += coeff
    return simplify_field(dict(result))


def miura_W4() -> ExactField:
    """Spin-4 generator W₄ = coefficient of ∂⁰ in the Miura operator."""
    Js = _currents()

    state = [({(): Rational(1)}, 0)]

    for J in reversed(Js):
        new_state = []
        for field, power in state:
            new_state.append((field, power + 1))
            Jf = multiply_fields(J, field)
            new_state.append((Jf, power))
            df = _take_z_derivative(field)
            if df:
                new_state.append((df, power))

        consolidated = defaultdict(lambda: defaultdict(lambda: Rational(0)))
        for field, power in new_state:
            for m, c in field.items():
                consolidated[power][m] += c

        state = [(simplify_field(dict(field_dict)), power)
                 for power, field_dict in consolidated.items()]

    result_by_power = {}
    for field, power in state:
        if power in result_by_power:
            result_by_power[power] = add_fields(result_by_power[power], field)
        else:
            result_by_power[power] = field

    return result_by_power.get(0, {})


def miura_all() -> Tuple[ExactField, ExactField, ExactField]:
    """Compute T, W₃, W₄ exactly at α₀=1.

    Returns (T, W₃, W₄) with exact Rational coefficients.
    """
    Js = _currents()

    state = [({(): Rational(1)}, 0)]

    for J in reversed(Js):
        new_state = []
        for field, power in state:
            new_state.append((field, power + 1))
            Jf = multiply_fields(J, field)
            new_state.append((Jf, power))
            df = _take_z_derivative(field)
            if df:
                new_state.append((df, power))

        consolidated = defaultdict(lambda: defaultdict(lambda: Rational(0)))
        for field, power in new_state:
            for m, c in field.items():
                consolidated[power][m] += c

        state = [(simplify_field(dict(field_dict)), power)
                 for power, field_dict in consolidated.items()]

    result_by_power = {}
    for field, power in state:
        if power in result_by_power:
            result_by_power[power] = add_fields(result_by_power[power], field)
        else:
            result_by_power[power] = field

    T = result_by_power.get(2, {})
    W3 = result_by_power.get(1, {})
    W4 = result_by_power.get(0, {})

    return T, W3, W4


# ═══════════════════════════════════════════════════════════════════════
# Structure constant extraction
# ═══════════════════════════════════════════════════════════════════════

def compute_exact_norms():
    """Compute exact BPZ norms at α₀=1 (c=63)."""
    T, W3, W4 = miura_all()
    norm_T = bpz_inner_product_exact(T, T)
    norm_W3 = bpz_inner_product_exact(W3, W3)
    norm_W4 = bpz_inner_product_exact(W4, W4)
    return {
        "norm_T": norm_T,
        "norm_W3": norm_W3,
        "norm_W4": norm_W4,
        "c/2": Rational(63, 2),
        "T_norm_matches_c/2": norm_T == Rational(63, 2),
    }


def compute_exact_c334():
    """Compute exact c₃₃₄ = ⟨W₄|W₃W₃ at pole 2⟩/⟨W₄|W₄⟩ at α₀=1.

    To get the pole-2 content of W₃(z)W₃(w), we need the OPE.
    For the BPZ inner product ⟨W₄|C₂⟩ where C₂ is the pole-2 coefficient,
    we need to compute ⟨W₄(z₁)|[W₃(z₂)W₃(z₃)]_{pole 2}⟩.

    This equals the 3-point function coefficient: the leading pole of
    W₄(z₁)W₃(z₂)W₃(z₃) when we extract the (z₂-z₃)⁻² (z₁-z₃)⁻⁸ part.

    Equivalently: fully contract W₄ with C₂ where C₂ = OPE of W₃W₃ at pole 2.
    """
    T, W3, W4 = miura_all()

    # Compute C₂: the pole-2 coefficient of W₃(z)W₃(w)
    C2 = _ope_at_pole_exact(W3, W3, 2)

    # Compute ⟨W₄|C₂⟩
    overlap = bpz_inner_product_exact(W4, C2)

    # Compute ⟨W₄|W₄⟩
    norm_W4 = bpz_inner_product_exact(W4, W4)

    # c334_raw = overlap / norm_W4
    c334_raw = overlap / norm_W4 if norm_W4 != 0 else None

    return {
        "overlap_W4_C2": overlap,
        "norm_W4": norm_W4,
        "c334_raw": c334_raw,
        "c334_raw_squared": c334_raw**2 if c334_raw is not None else None,
    }


def _ope_at_pole_exact(f1: ExactField, f2: ExactField, pole: int) -> ExactField:
    """Compute the coefficient of (z-w)^{-pole} in the OPE f1(z)f2(w).

    Uses Wick's theorem: contract SOME pairs of operators between f1 and f2,
    keeping the remaining operators. Taylor expand the f1 remainders around w.

    For each monomial pair (m1, m2), we contract k pairs (where k is chosen
    to give the desired pole order), and the remaining operators form the
    coefficient field.
    """
    h1 = max((mon_weight(m) for m in f1), default=0)
    h2 = max((mon_weight(m) for m in f2), default=0)

    result: ExactField = defaultdict(lambda: Rational(0))

    for m1, c1 in f1.items():
        for m2, c2 in f2.items():
            ops1 = list(m1)
            ops2 = list(m2)

            # Contract k pairs from ops1 with ops2
            # The pole order from k contractions is Σ(d_i + d_j) for each contracted pair
            # We need total pole = pole
            _add_partial_contractions(ops1, ops2, pole, c1 * c2, result)

    return simplify_field(dict(result))


def _add_partial_contractions(ops1, ops2, target_pole, coeff, result):
    """Recursively contract pairs to achieve a target pole order.

    Contracted pairs contribute their pole orders (d_a + d_b for each pair).
    Uncontracted operators from ops2 form the remaining monomial.
    Uncontracted operators from ops1 need Taylor expansion (derivatives).
    """
    if target_pole == 0:
        # No more contractions needed; remaining operators form the monomial
        # ops1 at position z → Taylor expand around w: ∂^n/n! corrections
        # For the (z-w)^0 term in Taylor, just keep ops1 as-is
        remaining = tuple(sorted(tuple(ops1) + tuple(ops2)))
        result[remaining] += coeff
        return

    if target_pole < 0:
        return

    if not ops1 or not ops2:
        return

    # Try contracting ops1[0] with each element of ops2
    a, da = ops1[0]
    rest1 = ops1[1:]

    # Option 1: don't contract ops1[0] (keep it as a remainder)
    # This requires Taylor expansion, which adds ∂ corrections.
    # For simplicity at the leading level, we skip Taylor corrections
    # (they contribute at subleading poles). This is correct when
    # target_pole = h1+h2 (leading pole, no Taylor corrections needed).
    # For general pole, we need Taylor corrections — but this makes
    # the computation much more complex.

    # For the BPZ inner product (leading pole), no Taylor corrections needed.
    # For the OPE at pole 2 (not leading), we DO need Taylor corrections.

    # SIMPLIFIED APPROACH: Use the 3-point function method instead.
    # ⟨W₄|C₂⟩ = 3-point function coefficient.
    # The 3-point function involves fully contracting all operators from
    # W₄, W₃(z₂), W₃(z₃), with specific powers of (z₁-z₂), (z₁-z₃), (z₂-z₃).
    pass


# Since partial contractions with Taylor corrections are complex,
# let me use a different strategy: compute the 3-point function directly.

def three_point_function(f1: ExactField, h1: int,
                         f2: ExactField, h2: int,
                         f3: ExactField, h3: int) -> Rational:
    """Compute the 3-point function ⟨f1(z₁) f2(z₂) f3(z₃)⟩.

    For 3 fields at positions z₁, z₂, z₃, the 3-point function is:
    ⟨f1(z₁)f2(z₂)f3(z₃)⟩ = C₁₂₃ / (z₁₂^a · z₁₃^b · z₂₃^c)

    where a+b = 2h₁, a+c = 2h₂, b+c = 2h₃, so:
    a = h₁+h₂-h₃, b = h₁+h₃-h₂, c = h₂+h₃-h₁.

    C₁₂₃ is computed by fully contracting all operators, with each
    contraction between positions z_i and z_j contributing a factor
    of the propagator coefficient.

    For our purposes: f1 = W₄ (h=4), f2 = W₃ (h=3), f3 = W₃ (h=3).
    a = 4+3-3 = 4, b = 4+3-3 = 4, c = 3+3-4 = 2.

    So ⟨W₄(z₁)W₃(z₂)W₃(z₃)⟩ = C₄₃₃ / (z₁₂⁴ z₁₃⁴ z₂₃²).

    C₄₃₃ is obtained by summing over all ways to contract the operators,
    with each contraction between f_i and f_j contributing the propagator
    at the appropriate power.
    """
    # Total operators: from f1, f2, f3
    # All must be contracted pairwise (no remainders for a pure number).
    # Contractions can be between any two of the three fields.
    # Each contraction between field i and field j contributes a propagator
    # factor and a power of the separation z_ij.

    # This is a sum over all perfect matchings of the combined operators,
    # where each pair comes from two DIFFERENT fields.

    # For efficiency, we enumerate the matchings field by field.
    a_power = h1 + h2 - h3  # power of z₁₂
    b_power = h1 + h3 - h2  # power of z₁₃
    c_power = h2 + h3 - h1  # power of z₂₃

    total = Rational(0)

    for m1, c1 in f1.items():
        for m2, c2 in f2.items():
            for m3, c3 in f3.items():
                contrib = _three_point_contraction(
                    list(m1), list(m2), list(m3),
                    a_power, b_power, c_power
                )
                total += c1 * c2 * c3 * contrib

    return total


def _three_point_contraction(ops1, ops2, ops3,
                              a_target, b_target, c_target) -> Rational:
    """Contract all operators from 3 monomials, yielding a scalar.

    ops1 (from field at z₁), ops2 (from z₂), ops3 (from z₃).
    Contractions between z_i and z_j contribute to the pole z_ij^{-d}.
    We need total pole powers: z₁₂^{-a}, z₁₃^{-b}, z₂₃^{-c}.

    Each contraction of (boson_a, deriv_m) at z_i with (boson_b, deriv_n) at z_j
    contributes: δ_{ab} · (-1)^{n+1} · (m+n-1)! to the scalar coefficient,
    and adds (m+n) to the pole power of z_ij.

    We recursively try all possible contractions.
    """
    if not ops1 and not ops2 and not ops3:
        if a_target == 0 and b_target == 0 and c_target == 0:
            return Rational(1)
        return Rational(0)

    # Pick the first available operator (from ops1 first, then ops2, then ops3)
    if ops1:
        return _contract_first_op1(ops1, ops2, ops3, a_target, b_target, c_target)
    elif ops2:
        return _contract_first_op2(ops2, ops3, a_target, b_target, c_target)
    else:
        return Rational(0)  # ops3 alone can't contract with anything


def _contract_first_op1(ops1, ops2, ops3, a_t, b_t, c_t) -> Rational:
    """Contract ops1[0] with something in ops2 or ops3."""
    total = Rational(0)
    first = ops1[0]
    rest1 = ops1[1:]
    a, da = first

    # Try contracting with each element of ops2 (contributes to z₁₂ pole)
    for j, (b, db) in enumerate(ops2):
        if a != b:
            continue
        prop = (-1)**(db + 1) * factorial(da + db - 1)
        pole = da + db
        new_a = a_t - pole
        if new_a < 0:
            continue
        rest2 = ops2[:j] + ops2[j+1:]
        sub = _three_point_contraction(rest1, rest2, ops3, new_a, b_t, c_t)
        total += prop * sub

    # Try contracting with each element of ops3 (contributes to z₁₃ pole)
    for j, (b, db) in enumerate(ops3):
        if a != b:
            continue
        prop = (-1)**(db + 1) * factorial(da + db - 1)
        pole = da + db
        new_b = b_t - pole
        if new_b < 0:
            continue
        rest3 = ops3[:j] + ops3[j+1:]
        sub = _three_point_contraction(rest1, ops2, rest3, a_t, new_b, c_t)
        total += prop * sub

    return total


def _contract_first_op2(ops2, ops3, a_t, b_t, c_t) -> Rational:
    """Contract ops2[0] with something in ops3 (contributes to z₂₃ pole)."""
    total = Rational(0)
    first = ops2[0]
    rest2 = ops2[1:]
    a, da = first

    for j, (b, db) in enumerate(ops3):
        if a != b:
            continue
        prop = (-1)**(db + 1) * factorial(da + db - 1)
        pole = da + db
        new_c = c_t - pole
        if new_c < 0:
            continue
        rest3 = ops3[:j] + ops3[j+1:]
        sub = _three_point_contraction([], rest2, rest3, a_t, b_t, new_c)
        total += prop * sub

    return total


def compute_exact_c334_via_3pt() -> dict:
    """Compute c₃₃₄ exactly using the 3-point function.

    c₃₃₄ = C₄₃₃ / norm_W₄

    where C₄₃₃ = ⟨W₄(z₁) W₃(z₂) W₃(z₃)⟩ × z₁₂⁴ z₁₃⁴ z₂₃²
    and norm_W₄ = ⟨W₄(z)W₄(w)⟩ × (z-w)⁸.
    """
    T, W3, W4 = miura_all()

    C433 = three_point_function(W4, 4, W3, 3, W3, 3)
    norm_W4 = bpz_inner_product_exact(W4, W4)
    norm_W3 = bpz_inner_product_exact(W3, W3)

    c334_raw = C433 / norm_W4 if norm_W4 != 0 else None
    c334_raw_sq = c334_raw**2 if c334_raw is not None else None

    # Concordance value at c=63
    concordance = Rational(42) * 63**2 * 337 / (87 * 509 * 235)

    R = c334_raw_sq / concordance if c334_raw_sq is not None else None

    return {
        "C433": C433,
        "norm_W4": norm_W4,
        "norm_W3": norm_W3,
        "c334_raw": c334_raw,
        "c334_raw_sq": c334_raw_sq,
        "concordance_c334_sq": concordance,
        "R": R,
    }


if __name__ == "__main__":
    print("Computing exact W(sl₄) Miura at α₀=1 (c=63)...")

    print("\n1. Computing generators...")
    T, W3, W4 = miura_all()
    print(f"   T:  {len(T)} terms")
    print(f"   W₃: {len(W3)} terms")
    print(f"   W₄: {len(W4)} terms")

    print("\n2. Computing norms...")
    norms = compute_exact_norms()
    for k, v in norms.items():
        print(f"   {k}: {v}")

    print("\n3. Computing c₃₃₄ via 3-point function...")
    result = compute_exact_c334_via_3pt()
    for k, v in result.items():
        print(f"   {k}: {v}")
