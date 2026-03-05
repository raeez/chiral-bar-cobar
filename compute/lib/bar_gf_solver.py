"""Algebraic generating function solver for bar cohomology.

Given a finite number of bar cohomology dimensions, find algebraic
generating functions P(x) = sum a_n x^n satisfying polynomial equations
c_d(x) P^d + ... + c_1(x) P + c_0(x) = 0.

Key application: predict dim H^4(B(sl3)) from the known values 8, 36, 204.

Mathematical background (examples_summary.tex, Thm ds-bar-gf-discriminant):
- sl2: P(x) = (1+x-sqrt(1-2x-3x^2))/(2x(1+x)), algebraic degree 2
- Vir: P(x) = 4x/(1-x+sqrt(1-2x-3x^2))^2, algebraic degree 2
- betagamma: P(x) = sqrt((1+x)/(1-3x)), algebraic degree 2
All share discriminant Delta(x) = 1-2x-3x^2 = (1-3x)(1+x).
"""

from __future__ import annotations

from itertools import product as iproduct
from typing import Dict, List, Optional, Tuple

from sympy import (
    Matrix, Rational, Symbol, sqrt, simplify, solve,
    Poly, ring, ZZ, QQ, symbols, series, O, expand,
    factorial, binomial, pi, oo, nsimplify, Integer
)


# ---------------------------------------------------------------------------
# Known generating functions (verified)
# ---------------------------------------------------------------------------

def riordan_numbers(N: int) -> List[int]:
    """Riordan numbers R(0), ..., R(N-1). OEIS A005043."""
    R = [0] * N
    R[0] = 1
    if N > 1:
        R[1] = 0
    for n in range(2, N):
        R[n] = ((n - 1) * (2 * R[n-1] + 3 * R[n-2])) // (n + 1)
    return R


def motzkin_numbers(N: int) -> List[int]:
    """Motzkin numbers M(0), ..., M(N-1). OEIS A001006."""
    M = [0] * N
    M[0] = 1
    if N > 1:
        M[1] = 1
    for n in range(2, N):
        M[n] = M[n-1] + sum(M[k] * M[n-2-k] for k in range(n-1))
    return M


def bar_dims_sl2(N: int) -> List[int]:
    """Bar cohomology dims for sl2: H^n = R(n+3) for n >= 1."""
    R = riordan_numbers(N + 4)
    return [R[n + 3] for n in range(1, N + 1)]


def bar_dims_virasoro(N: int) -> List[int]:
    """Bar cohomology dims for Virasoro: H^n = M(n+1) - M(n)."""
    M = motzkin_numbers(N + 2)
    return [M[n + 1] - M[n] for n in range(1, N + 1)]


# ---------------------------------------------------------------------------
# Algebraic generating function finder
# ---------------------------------------------------------------------------

def find_algebraic_gf(
    coeffs: List[int],
    alg_degree: int = 2,
    coeff_degree: int = 3,
    verbose: bool = False,
) -> List[Dict]:
    """Find algebraic equations satisfied by P(x) = sum coeffs[i] x^{i+1}.

    Search for equations c_d(x) P^d + ... + c_0(x) = 0
    where each c_i is a polynomial of degree <= coeff_degree.

    Returns list of solutions, each giving predicted next coefficients.

    Args:
        coeffs: known coefficients [a_1, a_2, ...] of P(x) = a_1 x + a_2 x^2 + ...
        alg_degree: degree of algebraic equation (2 = quadratic)
        coeff_degree: max degree of polynomial coefficients c_i(x)
        verbose: print intermediate results
    """
    n_known = len(coeffs)
    n_unknowns_per_coeff = coeff_degree + 1  # c_i(x) = c_{i,0} + c_{i,1}x + ... + c_{i,d}x^d
    n_total_unknowns = (alg_degree + 1) * n_unknowns_per_coeff

    # We need enough equations from the coefficient matching.
    # Equation at x^m: coefficient of x^m in c_d(x)P(x)^d + ... + c_0(x) = 0
    # Each power m gives one linear equation in the unknowns c_{i,j}.

    # Build the system: for each power x^m, collect the coefficient.
    # P(x) = sum_{k>=1} a_k x^k where a_k = coeffs[k-1]
    # P(x)^j has coefficient at x^m equal to sum over (k1,...,kj) with k1+...+kj=m of a_{k1}...a_{kj}

    # Precompute coefficients of P^j for j = 0, ..., alg_degree
    max_power = n_known + coeff_degree + 2  # how many terms to track
    P_powers = [[Rational(0)] * max_power for _ in range(alg_degree + 1)]
    P_powers[0][0] = Rational(1)  # P^0 = 1

    # P^1 coefficients
    for i, a in enumerate(coeffs):
        P_powers[1][i + 1] = Rational(a)

    # P^j = P^{j-1} * P (convolution)
    for j in range(2, alg_degree + 1):
        for m in range(max_power):
            s = Rational(0)
            for k in range(1, min(m + 1, n_known + 1)):
                if m - k < max_power:
                    s += Rational(coeffs[k - 1]) * P_powers[j - 1][m - k]
            P_powers[j][m] = s

    # Build linear system
    # c_i(x) = sum_{j=0}^{coeff_degree} c_{i,j} x^j
    # coefficient of x^m in the equation:
    # sum_{i=0}^{alg_degree} sum_{j=0}^{coeff_degree} c_{i,j} * [x^{m-j} in P^i]

    # Variables: c_{i,j} for i = 0..alg_degree, j = 0..coeff_degree
    # Total: (alg_degree+1) * (coeff_degree+1) unknowns

    # Equations: coefficient of x^m = 0 for m = 0, 1, ..., n_eqs-1
    n_eqs = n_known + coeff_degree + 1

    A_matrix = []
    for m in range(n_eqs):
        row = []
        for i in range(alg_degree + 1):
            for j in range(coeff_degree + 1):
                # Contribution: c_{i,j} * P_powers[i][m-j]
                idx = m - j
                if 0 <= idx < max_power:
                    row.append(P_powers[i][idx])
                else:
                    row.append(Rational(0))
        A_matrix.append(row)

    A = Matrix(A_matrix)

    if verbose:
        print(f"System: {A.rows} equations, {A.cols} unknowns")
        print(f"Rank: {A.rank()}")

    # Find null space
    null = A.nullspace()

    if verbose:
        print(f"Null space dimension: {len(null)}")

    if not null:
        return []

    results = []
    for vec in null:
        # Extract the polynomial coefficients
        poly_coeffs = {}
        for i in range(alg_degree + 1):
            pc = {}
            for j in range(coeff_degree + 1):
                val = vec[i * (coeff_degree + 1) + j]
                if val != 0:
                    pc[j] = val
            if pc:
                poly_coeffs[i] = pc

        # Verify against known coefficients
        ok = True
        for m in range(n_known + coeff_degree + 1):
            s = Rational(0)
            for i, pc in poly_coeffs.items():
                for j, c in pc.items():
                    idx = m - j
                    if 0 <= idx < max_power:
                        s += c * P_powers[i][idx]
            if s != 0:
                ok = False
                break

        if not ok:
            continue

        results.append({
            "poly_coeffs": poly_coeffs,
            "null_vector": vec,
        })

    return results


def predict_next_coefficient(
    coeffs: List[int],
    alg_degree: int = 2,
    coeff_degree: int = 3,
    verbose: bool = False,
) -> Optional[int]:
    """Predict the next bar cohomology dimension using algebraicity.

    If P(x) = a_1 x + a_2 x^2 + ... + a_N x^N + a_{N+1} x^{N+1} + ...
    satisfies a degree-d algebraic equation with polynomial coefficients
    of degree <= coeff_degree, then the first N coefficients determine a_{N+1}
    (provided the null space of the linear system is 1-dimensional).

    Returns: the predicted a_{N+1}, or None if prediction is ambiguous.
    """
    n_known = len(coeffs)

    # We want to use the algebraic equation to predict the next coefficient.
    # Strategy: add a_{N+1} as an unknown, and find the unique value that
    # allows a consistent algebraic equation.

    # Simpler: use the algebraic equation to derive a recurrence.
    # If P satisfies c_d(x)P^d + ... + c_0(x) = 0, we can extract
    # the recurrence for the coefficients.

    # First, find the algebraic equations using the known coefficients.
    solutions = find_algebraic_gf(coeffs, alg_degree, coeff_degree, verbose)

    if not solutions:
        if verbose:
            print("No algebraic equation found")
        return None

    # For each solution, predict the next coefficient
    predictions = set()

    for sol in solutions:
        poly_coeffs = sol["poly_coeffs"]

        # The algebraic equation is:
        # sum_{i=0}^{d} c_i(x) P(x)^i = 0
        # Coefficient of x^{N+1}: sum_i sum_j c_{i,j} * [x^{N+1-j} in P^i] = 0
        # The term involving a_{N+1} comes from P^1 (linear term) with c_1(x),
        # and from P^i for i >= 2 where one factor contributes a_{N+1}.

        # Actually, let's just extend the convolution and solve.
        max_power = n_known + coeff_degree + 5
        a = Symbol('a_next')

        # Recompute P_powers with the unknown next coefficient
        extended_coeffs = list(coeffs) + [a]
        P_ext = [Rational(0)] * max_power
        for i, c in enumerate(extended_coeffs):
            P_ext[i + 1] = c

        P_powers_ext = [[Rational(0)] * max_power for _ in range(alg_degree + 1)]
        P_powers_ext[0][0] = Rational(1)
        for k in range(max_power):
            P_powers_ext[1][k] = P_ext[k]

        for j in range(2, alg_degree + 1):
            for m in range(max_power):
                s = 0  # use sympy expressions
                for k in range(1, min(m + 1, len(extended_coeffs) + 1)):
                    if m - k < max_power:
                        s += extended_coeffs[k - 1] * P_powers_ext[j - 1][m - k] if k <= len(extended_coeffs) else 0
                P_powers_ext[j][m] = expand(s) if isinstance(s, type(a)) or hasattr(s, 'free_symbols') else s

        # Evaluate the equation at x^{N+1+coeff_degree} to get an equation for a
        target_power = n_known + 1  # x^{N+1} where coeffs go a_1,...,a_N

        for m in [target_power, target_power + 1]:
            eq = Rational(0)
            for i, pc in poly_coeffs.items():
                for j, c in pc.items():
                    idx = m - j
                    if 0 <= idx < max_power:
                        val = P_powers_ext[i][idx]
                        eq = expand(eq + c * val)

            if eq == 0:
                continue

            sols = solve(eq, a)
            if len(sols) == 1:
                val = sols[0]
                if val.is_integer:
                    predictions.add(int(val))
                elif val.is_rational:
                    predictions.add(val)
                break

    if len(predictions) == 1:
        return predictions.pop()
    elif len(predictions) > 1 and verbose:
        print(f"Multiple predictions: {predictions}")
    return None


# ---------------------------------------------------------------------------
# Verification: sl2 and Virasoro
# ---------------------------------------------------------------------------

def verify_sl2_algebraicity():
    """Verify that sl2 bar cohomology satisfies degree-2 algebraic equation."""
    dims = bar_dims_sl2(7)  # 3, 6, 15, 36, 91, 232, 603
    results = {}

    # Use first 5 to predict 6th
    pred = predict_next_coefficient(dims[:5], alg_degree=2, coeff_degree=2)
    results["sl2: predict a_6 from a_1..a_5"] = (pred == dims[5], pred, dims[5])

    # Use first 4 to predict 5th
    pred = predict_next_coefficient(dims[:4], alg_degree=2, coeff_degree=2)
    results["sl2: predict a_5 from a_1..a_4"] = (pred == dims[4], pred, dims[4])

    # Use first 3 to predict 4th
    pred = predict_next_coefficient(dims[:3], alg_degree=2, coeff_degree=2)
    results["sl2: predict a_4 from a_1..a_3"] = (pred == dims[3], pred, dims[3])

    return results


def verify_virasoro_algebraicity():
    """Verify that Virasoro bar cohomology satisfies degree-2 algebraic equation."""
    dims = bar_dims_virasoro(8)  # 1, 2, 5, 12, 30, 76, 196, 512
    results = {}

    pred = predict_next_coefficient(dims[:5], alg_degree=2, coeff_degree=2)
    results["Vir: predict a_6 from a_1..a_5"] = (pred == dims[5], pred, dims[5])

    pred = predict_next_coefficient(dims[:4], alg_degree=2, coeff_degree=2)
    results["Vir: predict a_5 from a_1..a_4"] = (pred == dims[4], pred, dims[4])

    pred = predict_next_coefficient(dims[:3], alg_degree=2, coeff_degree=2)
    results["Vir: predict a_4 from a_1..a_3"] = (pred == dims[3], pred, dims[3])

    return results


# ---------------------------------------------------------------------------
# The main computation: predict sl3 degree 4
# ---------------------------------------------------------------------------

def predict_sl3_degree4(verbose: bool = False):
    """Attempt to predict dim H^4(B(sl3)) from algebraicity.

    Known values: 8, 36, 204.
    Conjecture (conj:sl3-discriminant): P(x) is algebraic of degree <= 4.

    We try degree 2 first (like sl2), then degree 3 if needed.
    With 3 data points and a degree-2 equation with low-degree coefficients,
    the system may be underdetermined. We explore different coeff_degree values.
    """
    known = [8, 36, 204]
    results = {}

    for d in [2, 3]:
        for cd in range(1, 6):
            pred = predict_next_coefficient(known, alg_degree=d, coeff_degree=cd, verbose=verbose)
            key = f"sl3: alg_deg={d}, coeff_deg={cd}"
            results[key] = pred
            if pred is not None and verbose:
                print(f"  {key}: predicted a_4 = {pred}")

    return results


# ---------------------------------------------------------------------------
# W3 prediction
# ---------------------------------------------------------------------------

def predict_w3_degree5(verbose: bool = False):
    """Attempt to predict dim H^5(B(W3)) from algebraicity.

    Known values: 2, 5, 16, 52.
    """
    known = [2, 5, 16, 52]
    results = {}

    for d in [2, 3]:
        for cd in range(1, 6):
            pred = predict_next_coefficient(known, alg_degree=d, coeff_degree=cd, verbose=verbose)
            key = f"W3: alg_deg={d}, coeff_deg={cd}"
            results[key] = pred
            if pred is not None and verbose:
                print(f"  {key}: predicted a_5 = {pred}")

    return results


# ---------------------------------------------------------------------------
# Yangian prediction
# ---------------------------------------------------------------------------

def predict_yangian_degree4(verbose: bool = False):
    """Attempt to predict dim H^4(B(Y(sl2))) from algebraicity.

    Known values: 4, 10, 28.
    Note: Yangian GF is conjectured NOT algebraic (genus_expansions.tex).
    """
    known = [4, 10, 28]
    results = {}

    for d in [2, 3]:
        for cd in range(1, 6):
            pred = predict_next_coefficient(known, alg_degree=d, coeff_degree=cd, verbose=verbose)
            key = f"Y(sl2): alg_deg={d}, coeff_deg={cd}"
            results[key] = pred

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("BAR COHOMOLOGY ALGEBRAIC GF SOLVER")
    print("=" * 70)

    print("\n--- Verification: sl2 ---")
    for name, (ok, pred, actual) in verify_sl2_algebraicity().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: predicted={pred}, actual={actual}")

    print("\n--- Verification: Virasoro ---")
    for name, (ok, pred, actual) in verify_virasoro_algebraicity().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: predicted={pred}, actual={actual}")

    print("\n--- Prediction: sl3 degree 4 ---")
    sl3_results = predict_sl3_degree4(verbose=True)
    consistent = set(v for v in sl3_results.values() if v is not None)
    if len(consistent) == 1:
        print(f"\n  *** CONSISTENT PREDICTION: dim H^4(B(sl3)) = {consistent.pop()} ***")
    elif consistent:
        print(f"\n  Multiple predictions: {consistent}")
    else:
        print("\n  No prediction from degree-2 or degree-3 algebraic equations")

    print("\n--- Prediction: W3 degree 5 ---")
    w3_results = predict_w3_degree5(verbose=True)
    consistent_w3 = set(v for v in w3_results.values() if v is not None)
    if len(consistent_w3) == 1:
        print(f"\n  *** CONSISTENT PREDICTION: dim H^5(B(W3)) = {consistent_w3.pop()} ***")
    elif consistent_w3:
        print(f"\n  Multiple predictions: {consistent_w3}")

    print("\n--- Prediction: Yangian degree 4 ---")
    y_results = predict_yangian_degree4(verbose=True)
    consistent_y = set(v for v in y_results.values() if v is not None)
    if consistent_y:
        print(f"\n  Yangian predictions: {consistent_y}")
        print("  (Note: Yangian GF conjectured non-algebraic)")
