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


def find_rational_gf(
    coeffs: List[int],
    max_q: int = 5,
    max_p: int = 5,
    verbose: bool = False,
) -> Optional[Dict]:
    """Find a rational generating function P(x) = N(x)/D(x) fitting the data.

    Given coefficients [a_1, a_2, ...] of P(x) = a_1 x + a_2 x^2 + ...,
    find polynomials D(x) = 1 + d_1 x + ... + d_q x^q (monic) and
    N(x) = n_1 x + ... + n_p x^p such that D(x)*P(x) = N(x).

    This implies a linear recurrence for k > p:
        a_k + d_1 a_{k-1} + ... + d_q a_{k-q} = 0.

    Tries (p, q) pairs in order of increasing p+q, returning the first
    that fits all data consistently.

    Returns: dict with 'den_coeffs' [d_1,...,d_q], 'num_coeffs' [n_1,...,n_p],
             'p', 'q', and 'next_predicted', or None if no rational GF found.
    """
    N = len(coeffs)

    for total in range(2, max_p + max_q + 1):
        for q in range(1, min(total, max_q + 1)):
            p = total - q
            if p < 0 or p > max_p:
                continue
            # Need enough recurrence equations: N - p >= q to solve for d's.
            # Prefer N - p > q (overdetermined with verification).
            # Accept N - p == q only if p + q < N (so numerator eqs also constrain).
            n_rec_eqs = N - p  # number of recurrence equations (k = p+1 to N)
            if n_rec_eqs < q:
                continue

            # Build the recurrence system for d_1, ..., d_q
            # For k = p+1, ..., N: a_k + d_1*a_{k-1} + ... + d_q*a_{k-q} = 0
            # where a_j = 0 for j <= 0.
            A_rows = []
            b_rows = []
            for k in range(p + 1, N + 1):  # k is 1-indexed
                row = []
                for i in range(1, q + 1):
                    idx = k - i - 1  # 0-indexed: a_{k-i}
                    if 0 <= idx < N:
                        row.append(Rational(coeffs[idx]))
                    else:
                        row.append(Rational(0))
                A_rows.append(row)
                b_rows.append(Rational(-coeffs[k - 1]))

            if n_rec_eqs > q:
                # Overdetermined: use first q equations to solve, rest to verify
                A_solve = Matrix(A_rows[:q])
                b_solve = Matrix(b_rows[:q])
                try:
                    d_sol = A_solve.solve(b_solve)
                except Exception:
                    continue

                # Verify remaining equations
                ok = True
                for j in range(q, n_rec_eqs):
                    val = sum(d_sol[i] * A_rows[j][i] for i in range(q))
                    if val != b_rows[j]:
                        ok = False
                        break
                if not ok:
                    continue
            elif n_rec_eqs == q:
                # Exact fit: solve, then validate by requiring integer prediction
                A_solve = Matrix(A_rows)
                b_solve = Matrix(b_rows)
                try:
                    d_sol = A_solve.solve(b_solve)
                except Exception:
                    continue
            else:
                continue

            d_list = [d_sol[i] for i in range(q)]

            # Compute numerator coefficients: n_k = a_k + d_1*a_{k-1} + ... for k=1..p
            n_list = []
            for k in range(1, p + 1):
                val = Rational(coeffs[k - 1])
                for i in range(1, q + 1):
                    idx = k - i - 1
                    if 0 <= idx < N:
                        val += d_list[i - 1] * Rational(coeffs[idx])
                n_list.append(val)

            # Predict next coefficient
            # a_{N+1} = -(d_1*a_N + d_2*a_{N-1} + ... + d_q*a_{N+1-q})
            next_val = Rational(0)
            for i in range(q):
                idx = N - i - 1  # 0-indexed: a_{N-i}
                if 0 <= idx < N:
                    next_val -= d_list[i] * Rational(coeffs[idx])

            next_int = int(next_val) if next_val == int(next_val) else None

            # For exact fits (n_rec_eqs == q), validate by requiring integer
            # denominator coefficients, integer numerator, and integer prediction.
            # This filters out spurious rational fits that don't correspond to
            # genuine rational generating functions.
            if n_rec_eqs == q:
                all_int = all(d == int(d) for d in d_list)
                all_int = all_int and all(n == int(n) for n in n_list)
                all_int = all_int and (next_int is not None)
                if not all_int:
                    continue

            if verbose:
                print(f"Rational GF found: p={p}, q={q}")
                print(f"  D(x) = 1 + {' + '.join(f'({d})*x^{i+1}' for i, d in enumerate(d_list))}")
                print(f"  N(x) = {' + '.join(f'({n})*x^{i+1}' for i, n in enumerate(n_list))}")
                print(f"  Predicted a_{N+1} = {next_val}")

            return {
                "den_coeffs": d_list,
                "num_coeffs": n_list,
                "p": p,
                "q": q,
                "next_predicted": next_int if next_int is not None else next_val,
            }

    if verbose:
        print("No rational GF found")
    return None


def find_holonomic_recurrence(
    coeffs: List[int],
    max_order: int = 4,
    max_poly_deg: int = 2,
    a0: Optional[int] = None,
    verbose: bool = False,
) -> Optional[Dict]:
    """Find a holonomic (polynomial-coefficient) linear recurrence for the data.

    Searches for a recurrence of the form:
        p_0(n)*a_n + p_1(n)*a_{n-1} + ... + p_r(n)*a_{n-r} = 0
    where each p_i(n) = sum_j c_{i,j} * n^j is a polynomial of degree <= max_poly_deg.

    This handles algebraic generating functions (like sl2 Riordan numbers) that satisfy
    recurrences with polynomial-in-n coefficients but NOT constant-coefficient recurrences.

    Args:
        coeffs: bar cohomology dimensions [a_1, a_2, ...]
        max_order: maximum recurrence order r
        max_poly_deg: maximum degree of polynomial coefficients p_i(n)
        a0: if provided, prepended as a_0 (e.g., a0=1 for sl2 Riordan numbers)
        verbose: print intermediate results

    Returns: dict with 'recurrence' (coefficient matrix), 'order', 'poly_deg',
             'next_predicted', or None if no recurrence found.
    """
    data = ([a0] + list(coeffs)) if a0 is not None else list(coeffs)

    for r in range(2, max_order + 1):
        for d in range(0, max_poly_deg + 1):
            n_unk = (r + 1) * (d + 1)

            rows = []
            for n in range(r, len(data)):
                row = []
                for i in range(r + 1):
                    for j in range(d + 1):
                        row.append(Rational(n**j * data[n - i]))
                rows.append(row)

            if len(rows) < n_unk - 1:
                continue

            A = Matrix(rows)
            null = A.nullspace()

            if len(null) != 1:
                continue

            v = null[0]

            # Predict next value
            n = len(data)
            p_vals = []
            for i in range(r + 1):
                pv = sum(v[i * (d + 1) + j] * Rational(n**j) for j in range(d + 1))
                p_vals.append(pv)

            if p_vals[0] == 0:
                continue

            pred = Rational(0)
            for i in range(r):
                idx = len(data) - 1 - i
                if idx >= 0:
                    pred -= p_vals[i + 1] * Rational(data[idx])
            pred = pred / p_vals[0]

            # Check it's an integer
            pred_int = int(pred) if pred == int(pred) else None

            if verbose:
                print(f"Holonomic recurrence found: order={r}, poly_deg={d}")
                for i in range(r + 1):
                    terms = []
                    for j in range(d + 1):
                        val = v[i * (d + 1) + j]
                        if val != 0:
                            terms.append(f"({val})*n^{j}" if j > 0 else f"({val})")
                    if terms:
                        print(f"  p_{i}(n) = {' + '.join(terms)}")
                print(f"  Predicted a_{len(data) if a0 is not None else len(data)+1} = {pred}")

            return {
                "null_vector": v,
                "order": r,
                "poly_deg": d,
                "next_predicted": pred_int if pred_int is not None else pred,
            }

    if verbose:
        print("No holonomic recurrence found")
    return None


def verify_conjectured_gf(
    coeffs: List[int],
    num_coeffs: List,
    den_coeffs: List,
    n_predict: int = 3,
    verbose: bool = False,
) -> Dict:
    """Verify a conjectured rational GF P(x) = N(x)/D(x) against known data.

    Here N(x) = sum_{i} num_coeffs[i] * x^{i+1} and
    D(x) = 1 + sum_{i} den_coeffs[i] * x^{i+1} (monic constant term).

    The convention matches P(x) = a_1 x + a_2 x^2 + ..., so N has no constant term.

    Returns: dict with 'matches' (bool), 'predictions' (list of predicted next terms).
    """
    q = len(den_coeffs)
    p = len(num_coeffs)

    # Verify: D(x)*P(x) should equal N(x)
    # At x^k: a_k + d_1*a_{k-1} + ... + d_q*a_{k-q} = n_k (k<=p) or 0 (k>p)
    matches = True
    for k in range(1, len(coeffs) + 1):
        lhs = Rational(coeffs[k - 1])
        for i in range(1, q + 1):
            idx = k - i - 1
            if 0 <= idx < len(coeffs):
                lhs += Rational(den_coeffs[i - 1]) * Rational(coeffs[idx])
        rhs = Rational(num_coeffs[k - 1]) if k <= p else Rational(0)
        if lhs != rhs:
            if verbose:
                print(f"Mismatch at x^{k}: D*P coeff = {lhs}, N coeff = {rhs}")
            matches = False

    # Predict next terms using the recurrence
    # a_k = -(d_1*a_{k-1} + ... + d_q*a_{k-q}) for k > p
    extended = list(coeffs)
    predictions = []
    for _ in range(n_predict):
        k = len(extended) + 1  # 1-indexed
        if k <= p:
            # Still in numerator range; read from N
            val = Rational(num_coeffs[k - 1])
            for i in range(1, q + 1):
                idx = k - i - 1
                if 0 <= idx < len(extended):
                    val -= Rational(den_coeffs[i - 1]) * Rational(extended[idx])
        else:
            val = Rational(0)
            for i in range(1, q + 1):
                idx = k - i - 1
                if 0 <= idx < len(extended):
                    val -= Rational(den_coeffs[i - 1]) * Rational(extended[idx])
        val_int = int(val) if val == int(val) else val
        predictions.append(val_int)
        extended.append(val_int)

    if verbose:
        status = "VERIFIED" if matches else "MISMATCH"
        print(f"Conjectured GF: [{status}]")
        print(f"  D(x) = 1 + {' + '.join(f'({d})*x^{i+1}' for i, d in enumerate(den_coeffs))}")
        print(f"  N(x) = {' + '.join(f'({n})*x^{i+1}' for i, n in enumerate(num_coeffs))}")
        print(f"  Known: {coeffs}")
        print(f"  Predictions: {predictions}")

    return {
        "matches": matches,
        "predictions": predictions,
    }


def predict_next_coefficient(
    coeffs: List[int],
    alg_degree: int = 2,
    coeff_degree: int = 3,
    verbose: bool = False,
) -> Optional[int]:
    """Predict the next bar cohomology dimension.

    Tries three strategies in order:
    1. Rational GF fitting (P(x) = N(x)/D(x)) -- works for rational GFs
       (sl3, W3 conjectured).  CAUTION: with limited data, may return
       spurious rational fits for algebraic sequences (e.g. Virasoro
       appears rational through degree 8 but fails at degree 9).
    2. Holonomic recurrence (polynomial-coefficient linear recurrence) --
       works for algebraic GFs like sl2 Riordan numbers and Virasoro.
    3. Falls back to the algebraic equation approach (legacy, less reliable).

    Returns: the predicted a_{N+1}, or None if prediction fails.
    """
    # Strategy 1: Rational GF
    result = find_rational_gf(coeffs, max_q=5, max_p=5, verbose=verbose)
    if result is not None:
        val = result["next_predicted"]
        if isinstance(val, int):
            return val
        elif isinstance(val, Rational) and val.q == 1:
            return int(val)

    # Strategy 2: Holonomic recurrence (with a0=1 as Riordan-type seed)
    for a0_val in [None, 1, 0]:
        result = find_holonomic_recurrence(
            coeffs, max_order=4, max_poly_deg=2, a0=a0_val, verbose=verbose
        )
        if result is not None:
            val = result["next_predicted"]
            if isinstance(val, int):
                return val
            elif isinstance(val, Rational) and val.q == 1:
                return int(val)

    if verbose:
        print("All prediction strategies failed")
    return None


# ---------------------------------------------------------------------------
# Verification: sl2 and Virasoro
# ---------------------------------------------------------------------------

def verify_sl2_prediction():
    """Verify sl2 bar cohomology prediction via holonomic recurrence.

    sl2 has an algebraic (not rational) GF based on Riordan numbers.
    The holonomic recurrence (order 2, polynomial degree 1 in n) requires
    7 data points (a_0=1 + 6 bar dims) for a unique null vector.
    """
    dims = bar_dims_sl2(8)  # 3, 6, 15, 36, 91, 232, 603, 1585
    results = {}

    # Use first 6 bar dims (+ a_0=1 internally) to predict 7th
    pred = predict_next_coefficient(dims[:6])
    results["sl2: predict a_7 from a_1..a_6"] = (pred == dims[6], pred, dims[6])

    # Use first 7 to predict 8th
    pred = predict_next_coefficient(dims[:7])
    results["sl2: predict a_8 from a_1..a_7"] = (pred == dims[7], pred, dims[7])

    return results


def verify_virasoro_prediction():
    """Verify Virasoro bar cohomology prediction.

    CAUTION: Virasoro bar dims are Motzkin differences M(n+1)-M(n), and the
    GF is ALGEBRAIC of degree 2 (not rational).  However, a depth-3 constant-
    coefficient recurrence a_k = 4*a_{k-1} - 2*a_{k-2} - 4*a_{k-3} fits
    through degree 8, failing only at degree 9 (predicts 1352, actual 1353).
    This near-rationality is a non-trivial numerical coincidence.  With <=8
    data points, find_rational_gf returns this spurious fit, and the predictions
    happen to be correct.  With >=9 data points, the rational fit is correctly
    rejected and the holonomic strategy takes over.
    """
    dims = bar_dims_virasoro(8)  # 1, 2, 5, 12, 30, 76, 196, 512
    results = {}

    # Use first 6 to predict 7th (rational GF with q=3)
    pred = predict_next_coefficient(dims[:6])
    results["Vir: predict a_7 from a_1..a_6"] = (pred == dims[6], pred, dims[6])

    # Use first 7 to predict 8th
    pred = predict_next_coefficient(dims[:7])
    results["Vir: predict a_8 from a_1..a_7"] = (pred == dims[7], pred, dims[7])

    return results


# ---------------------------------------------------------------------------
# The main computation: predict sl3 degree 4
# ---------------------------------------------------------------------------

def predict_sl3_degree4(verbose: bool = False):
    """Predict dim H^4(B(sl3)) using conjectured rational GF.

    Known values: 8, 36, 204.
    Conjectured GF (conj:sl3-bar-gf):
        P(x) = 4x(2 - 13x - 2x^2) / ((1-8x)(1-3x-x^2))
    Denominator: (1-8x)(1-3x-x^2) = 1 - 11x + 23x^2 + 8x^3.
    Numerator: 4x(2-13x-2x^2) = 8x - 52x^2 - 8x^3.
    """
    known = [8, 36, 204]
    results = {}

    # Approach 1: verify conjectured GF
    # D(x) = 1 - 11x + 23x^2 + 8x^3, so den_coeffs = [-11, 23, 8]
    # N(x) = 8x - 52x^2 - 8x^3, so num_coeffs = [8, -52, -8]
    ver = verify_conjectured_gf(
        known,
        num_coeffs=[8, -52, -8],
        den_coeffs=[-11, 23, 8],
        n_predict=3,
        verbose=verbose,
    )
    results["conjectured_gf_verified"] = ver["matches"]
    results["predictions"] = ver["predictions"]

    # Approach 2: direct prediction (rational GF fitting)
    # With only 3 data points, the rational approach may not find a unique fit.
    pred = predict_next_coefficient(known, verbose=verbose)
    results["auto_prediction"] = pred

    return results


# ---------------------------------------------------------------------------
# W3 prediction
# ---------------------------------------------------------------------------

def predict_w3_degree5(verbose: bool = False):
    """Predict dim H^5(B(W3)) using conjectured rational GF.

    Known values: 2, 5, 16, 52.
    Conjectured GF:
        P(x) = x(2-3x) / ((1-x)(1-3x-x^2))
    Denominator: (1-x)(1-3x-x^2) = 1 - 4x + 2x^2 + x^3.
    Numerator: x(2-3x) = 2x - 3x^2.
    """
    known = [2, 5, 16, 52]
    results = {}

    # Approach 1: verify conjectured GF
    ver = verify_conjectured_gf(
        known,
        num_coeffs=[2, -3],
        den_coeffs=[-4, 2, 1],
        n_predict=3,
        verbose=verbose,
    )
    results["conjectured_gf_verified"] = ver["matches"]
    results["predictions"] = ver["predictions"]

    # Approach 2: direct prediction (rational GF fitting)
    pred = predict_next_coefficient(known, verbose=verbose)
    results["auto_prediction"] = pred

    return results


# ---------------------------------------------------------------------------
# Yangian prediction
# ---------------------------------------------------------------------------

def predict_yangian_degree4(verbose: bool = False):
    """Predict dim H^4(B(Y(sl2))) via conjectured rational GF.

    Known values: 4, 10, 28.
    Conjectured GF: P(x) = (1-3x²)/((1-x)(1-3x))
      D(x) = (1-x)(1-3x) = 1 - 4x + 3x²
      N(x) = 1 - 3x²
    Closed form: a(n) = 3^n + 1 for n >= 1.
    """
    known = [4, 10, 28]
    results = {}

    # Auto prediction (via rational GF finder)
    pred = predict_next_coefficient(known, verbose=verbose)
    results["auto_prediction"] = pred

    # Conjectured GF verification
    # Full GF: P(x) = (1-3x²)/((1-x)(1-3x)) includes a_0 = 1.
    # Shifted: P̃(x) = P(x) - 1 = 2x(2-3x)/((1-x)(1-3x)).
    # N(x) = 4x - 6x², D(x) = 1 - 4x + 3x².
    gf_result = verify_conjectured_gf(
        known,
        num_coeffs=[4, -6],       # N(x) = 4x - 6x²
        den_coeffs=[-4, 3],       # D(x) = 1 - 4x + 3x²
        n_predict=3,
    )
    results["conjectured_gf_verified"] = gf_result["matches"]
    if gf_result["matches"]:
        results["predictions"] = gf_result["predictions"]

    if verbose:
        print(f"  Conjectured GF verified: {gf_result['matches']}")
        if gf_result["matches"]:
            print(f"  Predictions: {gf_result['predictions']}")

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("BAR COHOMOLOGY GF SOLVER")
    print("=" * 70)

    print("\n--- Verification: sl2 (holonomic recurrence) ---")
    for name, (ok, pred, actual) in verify_sl2_prediction().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: predicted={pred}, actual={actual}")

    print("\n--- Verification: Virasoro (rational GF) ---")
    for name, (ok, pred, actual) in verify_virasoro_prediction().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: predicted={pred}, actual={actual}")

    print("\n--- Prediction: sl3 degree 4 ---")
    sl3_results = predict_sl3_degree4(verbose=True)
    if sl3_results.get("conjectured_gf_verified"):
        preds = sl3_results["predictions"]
        print(f"\n  *** CONJECTURED GF VERIFIED. Predictions: a_4={preds[0]}, a_5={preds[1]}, a_6={preds[2]} ***")
    else:
        print("\n  Conjectured GF does not match data")

    print("\n--- Prediction: W3 degree 5 ---")
    w3_results = predict_w3_degree5(verbose=True)
    if w3_results.get("conjectured_gf_verified"):
        preds = w3_results["predictions"]
        print(f"\n  *** CONJECTURED GF VERIFIED. Predictions: a_5={preds[0]}, a_6={preds[1]}, a_7={preds[2]} ***")
    else:
        print("\n  Conjectured GF does not match data")

    print("\n--- Prediction: Yangian degree 4 ---")
    y_results = predict_yangian_degree4(verbose=True)
    if y_results.get("conjectured_gf_verified"):
        preds = y_results["predictions"]
        print(f"\n  *** CONJECTURED GF VERIFIED. Predictions: a_4={preds[0]}, a_5={preds[1]}, a_6={preds[2]} ***")
    elif y_results.get("auto_prediction") is not None:
        print(f"\n  Auto prediction: {y_results['auto_prediction']}")
    else:
        print("\n  No prediction")
