r"""Universal bar cohomology H*(B(W_N)) for all N >= 2.

Computes structural invariants of the bar complex for the principal
W-algebra W_N = W(sl_N, f_prin) at arbitrary N, with detailed analysis
of the N-dependence.

W_N has (N-1) strong generators of conformal weights 2, 3, ..., N.
W_2 = Virasoro (1 generator), W_3 (2 generators), W_4 (3 generators), etc.

VACUUM MODULE:
  PBW basis: modes (W_s)_{-n} for s = 2, ..., N and n >= s,
  applied to |0> in non-increasing order within each generator family.
  Character:
    chi_{W_N}(q) = prod_{s=2}^{N} prod_{n >= s} 1/(1-q^n)

BAR COHOMOLOGY:
  The bar cohomology H*(B(W_N)) is computed by the Chevalley-Eilenberg
  complex of the negative-mode Lie algebra (W_N)_- (from the PBW spectral
  sequence collapse for Koszul algebras).

  CRITICAL DISTINCTION: the bar cohomology depends on the FULL OPE structure,
  not just the vacuum character. There is NO universal formula for
  dim H^k(B(W_N))_h from the vacuum character alone. The vacuum character
  determines the bar CHAIN GROUP dimensions (which bound the cohomology)
  but the actual cohomology requires the OPE data.

  KNOWN RESULTS (from explicit computation + conjectured GFs):
  - W_2 (Virasoro): GF P(x) = x*M(x)^2 (Motzkin), algebraic degree 2
    Dims: 1, 2, 5, 12, 30, 76, 196, 512, 1353, ...
  - W_3: GF P(x) = x(2-3x)/((1-x)(1-3x-x^2)), rational
    Dims: 2, 5, 16, 52, 171, 565, 1868, ...
  - W_4: partial data, irrational structure constants at weight >= 6

  These generating functions are in "generation degree" (the natural grading
  for the Koszul dual character), NOT conformal weight.

WHAT THIS ENGINE COMPUTES (universally, for any N):
  1. Vacuum module character chi_{W_N}(q)
  2. Augmentation ideal dims (Vbar_h)
  3. Bar chain group dims B^n_h (from convolution of Vbar)
  4. Bar Euler characteristic chi_h (Euler bound on cohomology)
  5. Exterior algebra character prod (1+q^n) (partition upper bound)
  6. kappa(W_N) = c * (H_N - 1)
  7. Growth rate estimates and recurrence detection for known GFs
  8. N-dependence analysis at each generation degree

KAPPA (modular characteristic):
  kappa(W_N) = sum_{s=2}^{N} c/s = c * (H_N - 1)
  where H_N = 1 + 1/2 + ... + 1/N is the N-th harmonic number.
  Each generator W_s contributes c/s from its leading-pole curvature.

CENTRAL CHARGE:
  c(W_N, k) = (N-1) - N(N^2-1)/(k+N)
  Feigin-Frenkel dual level: k' = -k - 2N
  Complementarity sum: c(k) + c(k') depends on N.

Conventions:
  - Cohomological grading, |d| = +1
  - n-th product convention a_{(n)}b (AP44: divided-power for lambda-bracket)
  - Desuspension lowers degree (AP45)
  - kappa(W_N) = c*(H_N - 1), NOT c/2 for N >= 3 (AP39)

References:
  Fateev-Lukyanov (1988), "The models of 2d CFT with Z_n symmetry"
  landscape_census.tex (bar dimension tables)
  bar_complex_tables.tex (low-weight computations)
  ds_spectral_sequence.py (_wn_vacuum_dims)
  bar_gf_algebraicity.py (algebraic equations)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import factorial
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Integer,
    Matrix,
    Rational,
    Symbol,
    expand,
    simplify,
    sqrt,
)


# ============================================================================
# W_N vacuum module dimensions
# ============================================================================

def wn_vacuum_dims(N: int, max_weight: int) -> Dict[int, int]:
    """Vacuum module dimensions for W_N = W(sl_N, f_prin).

    W_N has strong generators of conformal weights 2, 3, ..., N.
    Character:
      chi_{W_N}(q) = prod_{s=2}^{N} prod_{n >= s} 1/(1-q^n)

    Returns {h: dim V_h} with dim V_0 = 1 (vacuum).
    """
    dims = [0] * (max_weight + 1)
    dims[0] = 1

    for s in range(2, N + 1):
        for n in range(s, max_weight + 1):
            for h in range(n, max_weight + 1):
                dims[h] += dims[h - n]

    return {h: dims[h] for h in range(max_weight + 1)}


def wn_augmentation_dims(N: int, max_weight: int) -> Dict[int, int]:
    """Augmentation ideal V-bar dimensions for W_N.

    V-bar = vacuum module minus vacuum state.
    V-bar_0 = 0, V-bar_1 = 0, V-bar_h = chi(q)_h for h >= 2.
    """
    vac = wn_vacuum_dims(N, max_weight)
    result = dict(vac)
    result[0] = 0
    return result


# ============================================================================
# kappa(W_N) = c * (H_N - 1)
# ============================================================================

def wn_kappa_coefficient(N: int) -> Fraction:
    """The coefficient of c in kappa(W_N) = c * (H_N - 1).

    kappa(W_N) = sum_{s=2}^{N} c/s = c * (1/2 + 1/3 + ... + 1/N).

    Returns the exact rational value H_N - 1.
    """
    result = Fraction(0)
    for s in range(2, N + 1):
        result += Fraction(1, s)
    return result


def wn_kappa_symbolic(N: int):
    """kappa(W_N) as a sympy expression in c."""
    c = Symbol('c')
    coeff = wn_kappa_coefficient(N)
    return Rational(coeff.numerator, coeff.denominator) * c


def wn_kappa_table(max_N: int = 10) -> Dict[int, Fraction]:
    """Table of kappa coefficients for W_2 through W_{max_N}."""
    return {N: wn_kappa_coefficient(N) for N in range(2, max_N + 1)}


# ============================================================================
# Central charge
# ============================================================================

def wn_central_charge(N: int, k=None):
    """Central charge of W_N = W(sl_N, f_prin) at level k.

    c(k) = (N-1) - N(N^2-1)(k+N-1)^2 / (k+N)

    For N=2 (Virasoro): c = 1 - 6(k+1)^2/(k+2).
    For N=3: c = 2 - 24(k+2)^2/(k+3).

    Feigin-Frenkel dual: k' = -k - 2N.
    Complementarity: c(k) + c(k') = 2(N-1)(2N^2 + 2N + 1).
    """
    if k is None:
        k = Symbol('k')
    return (N - 1) - N * (N**2 - 1) * (k + N - 1)**2 / (k + N)


def wn_complementarity_sum(N: int):
    """c(k) + c(-k-2N) for W(sl_N)."""
    k = Symbol('k')
    c1 = wn_central_charge(N, k)
    c2 = wn_central_charge(N, -k - 2 * N)
    return simplify(c1 + c2)


# ============================================================================
# Bar chain group dimensions
# ============================================================================

def bar_chain_dim_wn(N: int, bar_deg: int, weight: int,
                     max_weight: int = 30) -> int:
    """Dimension of the bar chain group B^{bar_deg}_{weight}(W_N).

    B^n_h = {(n+1)-tuples from V-bar with total weight h} x n!
    (The Orlik-Solomon algebra OS^n(Conf_{n+1}(C)) has dimension n!.)

    Minimum weight: 2*(n+1) (each V-bar element has weight >= 2).
    """
    n = bar_deg
    vdims = wn_augmentation_dims(N, max(max_weight, weight))
    min_wt = 2 * (n + 1)
    if weight < min_wt:
        return 0

    # Count ordered (n+1)-tuples from V-bar with total weight h
    prev = {0: 1}
    for _ in range(n + 1):
        curr: Dict[int, int] = {}
        for hp, cp in prev.items():
            for hw in range(2, weight - hp + 1):
                dw = vdims.get(hw, 0)
                if dw == 0:
                    continue
                ht = hp + hw
                if ht > weight:
                    break
                curr[ht] = curr.get(ht, 0) + cp * dw
        prev = curr

    tuple_count = prev.get(weight, 0)
    os_dim = factorial(n)
    return tuple_count * os_dim


def bar_euler_char_wn(N: int, weight: int, max_bar_deg: int = 5) -> int:
    """Alternating Euler characteristic of the bar complex at weight h.

    chi_h = sum_{n=0}^{max_bar_deg} (-1)^n dim B^n_h

    This gives a constraint on the bar cohomology: if all H^k = 0 for k >= 2,
    then chi_h = dim Vbar_h - dim H^1_h.
    """
    vbar = wn_augmentation_dims(N, weight)
    result = vbar.get(weight, 0)  # n=0 contribution (B^0 = Vbar)

    for n in range(1, max_bar_deg + 1):
        dim_Bn = bar_chain_dim_wn(N, n, weight, weight)
        result += ((-1) ** n) * dim_Bn

    return result


# ============================================================================
# Exterior algebra character (upper bound on total bar cohomology)
# ============================================================================

def exterior_algebra_character(N: int, max_weight: int) -> List[int]:
    """Character of the exterior algebra on W_N modes.

    prod_{s=2}^{N} prod_{n >= s} (1 + q^n)

    This counts partitions of h into DISTINCT parts, where each part n >= s
    appears with multiplicity at most min(n-1, N-1) across all generators.

    For Koszul algebras, this is an UPPER BOUND on the total bar cohomology
    (the actual cohomology is less because the bar differential is nontrivial).
    """
    coeffs = [0] * (max_weight + 1)
    coeffs[0] = 1

    for s in range(2, N + 1):
        for n in range(s, max_weight + 1):
            # Multiply by (1 + q^n): process from high to low
            for h in range(max_weight, n - 1, -1):
                coeffs[h] += coeffs[h - n]

    return coeffs


# ============================================================================
# Known bar cohomology data (from explicit computation + conjectured GFs)
# ============================================================================

def _motzkin_numbers(max_n: int) -> List[int]:
    """Motzkin numbers M(0), ..., M(max_n)."""
    M = [0] * (max_n + 1)
    M[0] = 1
    if max_n >= 1:
        M[1] = 1
    for n in range(2, max_n + 1):
        M[n] = M[n - 1]
        for k in range(n - 1):
            M[n] += M[k] * M[n - 2 - k]
    return M


def virasoro_known_gf_dims(max_n: int = 20) -> List[int]:
    """Virasoro (W_2) bar cohomology in generation degree.

    P(x) = x * M(x)^2 (algebraic degree 2, Motzkin based).
    Dims at generation degree n: M(n+1) - M(n) = 1, 2, 5, 12, 30, 76, ...

    Growth rate: 3 (from singularity at x = 1/3).
    """
    M = _motzkin_numbers(max_n + 2)
    return [M[n + 1] - M[n] for n in range(1, max_n + 1)]


def w3_known_gf_dims(max_n: int = 20) -> List[int]:
    """W_3 bar cohomology in generation degree.

    P(x) = x(2-3x) / ((1-x)(1-3x-x^2)), rational.
    Recurrence: a_n = 4*a_{n-1} - 2*a_{n-2} - a_{n-3} for n >= 4.
    Dims: 2, 5, 16, 52, 171, 565, 1868, 6178, ...

    Growth rate: (3 + sqrt(13))/2 ~ 3.303 (from GF singularity).
    """
    a = [0, 2, 5, 16]
    while len(a) - 1 < max_n:
        k = len(a)
        a.append(4 * a[k - 1] - 2 * a[k - 2] - a[k - 3])
    return a[1:max_n + 1]


def known_gf_dims(N: int, max_n: int = 20) -> Optional[List[int]]:
    """Known bar cohomology dims for W_N, if available.

    Returns None if no closed-form GF is known for this N.
    """
    if N == 2:
        return virasoro_known_gf_dims(max_n)
    elif N == 3:
        return w3_known_gf_dims(max_n)
    return None


# ============================================================================
# Growth rate analysis
# ============================================================================

def growth_rate_from_gf(N: int, max_n: int = 25) -> Optional[Dict[str, Any]]:
    """Growth rate of known bar cohomology GF for W_N.

    The exponential growth rate gamma is 1/r where r is the radius of
    convergence of the generating function.
    """
    dims = known_gf_dims(N, max_n)
    if dims is None:
        return None

    # Ratio estimates
    ratios = []
    for i in range(1, len(dims)):
        if dims[i - 1] > 0 and dims[i] > 0:
            ratios.append(dims[i] / dims[i - 1])

    # Root estimates
    roots = []
    for i in range(len(dims)):
        if dims[i] > 0:
            roots.append(dims[i] ** (1.0 / (i + 1)))

    return {
        "N": N,
        "gamma_ratio": ratios[-1] if ratios else None,
        "gamma_root": roots[-1] if roots else None,
        "last_ratios": ratios[-5:],
        "last_roots": roots[-5:],
    }


# ============================================================================
# Recurrence detection
# ============================================================================

def detect_linear_recurrence(seq: List[int],
                             max_order: int = 10) -> Optional[Dict[str, Any]]:
    """Detect a linear recurrence in a sequence.

    If a_n = c_1 a_{n-1} + ... + c_r a_{n-r}, then the GF is rational
    with denominator degree r.
    """
    if len(seq) < 4:
        return None

    for r in range(1, min(max_order + 1, len(seq) // 2)):
        n_eqs = len(seq) - r
        if n_eqs < r:
            continue

        # Build overdetermined system
        A_rows = []
        b_vals = []
        for i in range(r, len(seq)):
            row = [Fraction(seq[i - j - 1]) for j in range(r)]
            A_rows.append(row)
            b_vals.append(Fraction(seq[i]))

        # Solve using first r equations
        M = Matrix([[a for a in row] for row in A_rows[:r]])
        rhs = Matrix(b_vals[:r])

        if M.det() == 0:
            continue

        try:
            sol = M.solve(rhs)
        except Exception:
            continue

        coeffs = [sol[i] for i in range(r)]

        # Verify on ALL remaining equations
        ok = True
        for i in range(r, len(seq)):
            pred = sum(coeffs[j] * seq[i - j - 1] for j in range(r))
            if pred != seq[i]:
                ok = False
                break

        if ok:
            int_coeffs = []
            all_int = True
            for c in coeffs:
                if hasattr(c, 'is_integer') and c.is_integer:
                    int_coeffs.append(int(c))
                elif hasattr(c, 'q') and c.q == 1:
                    int_coeffs.append(int(c.p))
                else:
                    all_int = False
                    int_coeffs.append(c)

            return {
                "order": r,
                "coefficients": int_coeffs,
                "all_integer": all_int,
                "verified_through": len(seq),
            }

    return None


# ============================================================================
# N-dependence analysis
# ============================================================================

def generation_degree_dims_at_n(n: int, max_N: int = 8) -> Dict[int, Optional[int]]:
    """Bar cohomology at generation degree n for each W_N.

    Returns {N: dim} for N = 2, ..., max_N.
    Only available for N with known GFs.
    """
    result = {}
    for N in range(2, max_N + 1):
        dims = known_gf_dims(N, n)
        if dims is not None and n <= len(dims):
            result[N] = dims[n - 1]
        else:
            result[N] = None
    return result


def polynomial_in_N_test(n: int, max_N: int = 8) -> Dict[str, Any]:
    """Test whether dim at generation degree n is polynomial in N.

    Only uses families where the GF is known.
    """
    data = generation_degree_dims_at_n(n, max_N)
    points = [(N, d) for N, d in data.items() if d is not None]

    if len(points) < 2:
        return {"degree_n": n, "polynomial": None, "insufficient_data": True}

    # Lagrange interpolation
    N_sym = Symbol('N')
    poly = Integer(0)
    for i, (xi, yi) in enumerate(points):
        term = Integer(yi)
        for j, (xj, _) in enumerate(points):
            if i != j:
                term *= (N_sym - xj) / (xi - xj)
        poly += term

    return {
        "degree_n": n,
        "polynomial": str(expand(poly)),
        "data_points": points,
    }


# ============================================================================
# DS reduction analysis
# ============================================================================

def sl_n_vacuum_dims(N: int, max_weight: int) -> Dict[int, int]:
    """Vacuum module dimensions for affine sl_N (at generic level).

    Generators: J^a (h=1) for a = 1, ..., dim(sl_N) = N^2 - 1.
    chi(q) = prod_{n>=1} 1/(1-q^n)^{N^2-1}
    """
    rank = N * N - 1
    dims = [0] * (max_weight + 1)
    dims[0] = 1

    for _ in range(rank):
        for n in range(1, max_weight + 1):
            for h in range(n, max_weight + 1):
                dims[h] += dims[h - n]

    return {h: dims[h] for h in range(max_weight + 1)}


def ds_vacuum_ratio(N: int, max_weight: int = 12) -> Dict[int, Fraction]:
    """Ratio chi_{sl_N}(q) / chi_{W_N}(q) at each weight.

    Measures the excess vacuum states in sl_N killed by DS reduction.
    """
    sl_dims = sl_n_vacuum_dims(N, max_weight)
    wn_dims = wn_vacuum_dims(N, max_weight)

    result = {}
    for h in range(max_weight + 1):
        sd = sl_dims.get(h, 0)
        wd = wn_dims.get(h, 0)
        if wd > 0:
            result[h] = Fraction(sd, wd)
    return result


# ============================================================================
# Comparison table
# ============================================================================

def vacuum_comparison_table(max_N: int = 8, max_weight: int = 12) -> Dict[int, Dict[int, int]]:
    """Vacuum augmentation dims V-bar_h for W_N, N = 2, ..., max_N."""
    return {N: wn_augmentation_dims(N, max_weight)
            for N in range(2, max_N + 1)}


def vbar_dim_at_fixed_weight(h: int, max_N: int = 10) -> Dict[int, int]:
    """dim V-bar_h(W_N) as a function of N for fixed weight h."""
    result = {}
    for N in range(2, max_N + 1):
        vbar = wn_augmentation_dims(N, h)
        result[N] = vbar.get(h, 0)
    return result


def vbar_polynomial_in_N(h: int, max_N: int = 10) -> Dict[str, Any]:
    """Test whether dim V-bar_h is polynomial in N at fixed weight h.

    For W_N, the vacuum character has a product structure that makes
    the coefficients polynomial in N for N >= h (when all generators
    have modes that contribute at weight h).
    """
    data = vbar_dim_at_fixed_weight(h, max_N)
    points = [(N, data[N]) for N in sorted(data.keys())]

    if len(points) < 3:
        return {"weight": h, "polynomial": None}

    # Lagrange interpolation
    N_sym = Symbol('N')
    poly = Integer(0)
    for i, (xi, yi) in enumerate(points):
        term = Integer(yi)
        for j, (xj, _) in enumerate(points):
            if i != j:
                term *= (N_sym - xj) / (xi - xj)
        poly += term

    poly_exp = expand(poly)

    # Check: does the polynomial stabilize? (agree for large N)
    check_N = max_N + 1
    predicted = int(poly_exp.subs(N_sym, check_N))
    actual = wn_augmentation_dims(check_N, h).get(h, 0)

    return {
        "weight": h,
        "polynomial": str(poly_exp),
        "predicted": predicted,
        "actual": actual,
        "verified": predicted == actual,
    }


# ============================================================================
# Full analysis engine
# ============================================================================

class WNBarCohomologyEngine:
    """Universal bar cohomology engine for W_N algebras.

    Computes vacuum dims, bar chain group dims, kappa, and
    structural invariants for any N >= 2.
    """

    def __init__(self, N: int, max_weight: int = 15):
        if N < 2:
            raise ValueError(f"N must be >= 2, got {N}")
        self.N = N
        self.max_weight = max_weight
        self._vacuum = wn_vacuum_dims(N, max_weight)
        self._vbar = wn_augmentation_dims(N, max_weight)
        self._kappa_coeff = wn_kappa_coefficient(N)
        self._known_gf = known_gf_dims(N, 20)

    def vacuum_dim(self, h: int) -> int:
        return self._vacuum.get(h, 0)

    def vbar_dim(self, h: int) -> int:
        return self._vbar.get(h, 0)

    def kappa_coefficient(self) -> Fraction:
        return self._kappa_coeff

    def num_generators(self) -> int:
        return self.N - 1

    def generator_weights(self) -> List[int]:
        return list(range(2, self.N + 1))

    def has_known_gf(self) -> bool:
        return self._known_gf is not None

    def known_bar_dims(self) -> Optional[List[int]]:
        return self._known_gf

    def bar_chain_dim(self, bar_deg: int, weight: int) -> int:
        return bar_chain_dim_wn(self.N, bar_deg, weight, self.max_weight)

    def euler_char(self, weight: int, max_bar_deg: int = 4) -> int:
        return bar_euler_char_wn(self.N, weight, max_bar_deg)

    def growth_rate(self) -> Optional[Dict[str, Any]]:
        return growth_rate_from_gf(self.N)

    def recurrence(self) -> Optional[Dict[str, Any]]:
        if self._known_gf is None:
            return None
        return detect_linear_recurrence(self._known_gf)

    def full_report(self) -> Dict[str, Any]:
        rec = self.recurrence()
        gr = self.growth_rate()

        return {
            "N": self.N,
            "num_generators": self.num_generators(),
            "generator_weights": self.generator_weights(),
            "kappa_coefficient": str(self._kappa_coeff),
            "has_known_gf": self.has_known_gf(),
            "known_dims": self._known_gf[:10] if self._known_gf else None,
            "growth_rate": gr["gamma_ratio"] if gr else None,
            "is_rational": rec is not None,
            "recurrence_order": rec["order"] if rec else None,
            "vacuum_dims": {h: self._vacuum[h]
                           for h in range(min(12, self.max_weight + 1))},
        }


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("UNIVERSAL BAR COHOMOLOGY H*(B(W_N)) ENGINE")
    print("=" * 80)

    # Vacuum dims table
    max_h = 12
    print(f"\n--- Augmentation ideal dims V-bar_h ---")
    print(f"{'h':>4}", end="")
    for N in range(2, 9):
        print(f"  {'W_'+str(N):>8}", end="")
    print()
    print("-" * (4 + 9 * 7))

    vbar_tables = {}
    for N in range(2, 9):
        vbar_tables[N] = wn_augmentation_dims(N, max_h)

    for h in range(2, max_h + 1):
        print(f"{h:>4}", end="")
        for N in range(2, 9):
            d = vbar_tables[N].get(h, 0)
            print(f"  {d:>8}", end="")
        print()

    # Kappa table
    print("\n--- kappa(W_N) = c * (H_N - 1) ---")
    for N in range(2, 11):
        k = wn_kappa_coefficient(N)
        print(f"  W_{N}: kappa = {k} * c  ({float(k):.6f} c)")

    # Known GF data
    print("\n--- Known bar cohomology GFs ---")
    for N in [2, 3]:
        dims = known_gf_dims(N, 10)
        print(f"  W_{N}: {dims}")
        rec = detect_linear_recurrence(dims)
        if rec:
            print(f"    Recurrence order {rec['order']}: {rec['coefficients']}")
        gr = growth_rate_from_gf(N)
        if gr:
            print(f"    Growth rate ~ {gr['gamma_ratio']:.6f}")

    # V-bar polynomial in N
    print("\n--- V-bar_h as polynomial in N ---")
    for h in range(2, 9):
        pn = vbar_polynomial_in_N(h, 8)
        if pn.get("verified"):
            print(f"  h={h}: {pn['polynomial']} (verified)")
        else:
            print(f"  h={h}: {pn['polynomial']} "
                  f"(pred={pn.get('predicted')}, actual={pn.get('actual')})")

    # Exterior algebra comparison
    print("\n--- Exterior algebra char (upper bound on total bar coh) ---")
    for N in [2, 3, 4, 5, 6]:
        ext = exterior_algebra_character(N, 10)
        print(f"  W_{N}: {[ext[h] for h in range(11)]}")
