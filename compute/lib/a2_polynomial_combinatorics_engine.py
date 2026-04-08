r"""Combinatorial analysis of A_g(N): the cross-channel genus-g polynomial.

MATHEMATICAL FRAMEWORK
======================

The genus-g cross-channel correction to the W_N free energy decomposes as:

    delta_F_g^grav(W_N, c) = sum_{m=-(g-1)}^{g-1} C_{g,m}(N) * c^m

The LEADING 1/c COEFFICIENT is A_g(N) := C_{g,-(g-1)}(N), the coefficient
of c^{-(g-1)}.  At genus 2:

    delta_F_2^grav(W_N, c) = B_2(N) + A_2(N)/c

where:
    B_2(N) = (N-2)(N+3) / 96 = (p_1 - 2) / 48
    A_2(N) = (N-2)(3N^3 + 14N^2 + 22N + 33) / 24 = (2*p_1^2 + p_2 - 12) / 4

Here p_k = S_k = sum_{j=2}^N j^k are Newton power sums of the conformal
weights {2, 3, ..., N} of the W_N generators.

THE INNER POLYNOMIAL P_2(N) = 3N^3 + 14N^2 + 22N + 33
=======================================================

Properties:
- Irreducible over Q (discriminant -110891 < 0, one real root ~-3.47)
- In rising factorial basis: P_2(N) = 3*N(N+1)(N+2) + 5*N(N+1) + 11*N + 33
- In falling factorial basis: P_2(N) = 18*C(N,3) + 46*C(N,2) + 39*N + 33
- NOT a known OEIS sequence
- (N-2)*P_2(N) is NOT always divisible by 24

GRAPH DECOMPOSITION (the main structural theorem)
=================================================

A_2(N) decomposes as a sum over THREE genus-2 stable graphs
(the only ones with mixed-channel contributions at order 1/c):

    A_2(N) = A_2^{FE}(N) + A_2^{Th}(N) + A_2^{SR}(N)

where:
    A_2^{FE}(N) = (p_1^2 - p_2)/4 = e_2(2,...,N)/2     [FIGURE-EIGHT]
    A_2^{Th}(N) = (p_2 - 4)/2                            [THETA]
    A_2^{SR}(N) = (p_1^2 - 4)/4                          [SUNRISE]

Graph  | Topology                      | h^1 | Aut | Channel constraint
-------|-------------------------------|-----|-----|-------------------
FE     | 1 vertex g=0, 2 self-loops   |  2  |  8  | 2 distinct loops
Theta  | 2 vertices g=0, 3 bridges    |  2  | 12  | T-bridge + paired W
SR     | 2 vertices g=0, 2SL+1 bridge |  2  |  8  | 2 distinct self-loops + T-bridge

The c^0 coefficient B_2(N) comes from exactly ONE graph:

    B_2(N) = (p_1 - 2)/48              [SUNSET: g=0+g=1, SL+bridge]

SYMMETRIC FUNCTION INTERPRETATION
==================================

A_2(N) = (3*e_1^2 - 2*e_2 - 12) / 4

where e_k are elementary symmetric functions of {2,...,N}.
The constant 12 = 3*e_1({2})^2 - 2*e_2({2}) is the N=2 baseline,
so A_2(N) measures the EXCESS of the quadratic symmetric invariant
3*e_1^2 - 2*e_2 beyond the uniform-weight (Virasoro) value.

Each graph contributes a specific symmetric function:
    FE:  e_2/2           (second elementary symmetric function)
    Th:  (p_2 - 4)/2     (quadratic power sum excess)
    SR:  (e_1^2 - 4)/4   (square-of-sum excess)

DEGREE PATTERN AT HIGHER GENUS
===============================

At genus g, A_g(N) = (N-2) * Q_g(N) / D_g where:
    deg(Q_g) = 3(g-1)    (inner polynomial degree)
    deg(A_g) = 3g - 2     (total degree)

Verified: g=2 (deg 3), g=3 (deg 6).

Conjecture: A_g(N) is a polynomial in p_1, p_2, ..., p_{2(g-1)}
of total weight 2g in the power-sum grading (where p_k has weight k).

Manuscript references:
    thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex)
    prop:universal-gravitational-cross-channel (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
from typing import Dict, List, Optional, Tuple


# ============================================================================
# Power sums and elementary symmetric functions of weights {2,...,N}
# ============================================================================

@lru_cache(maxsize=256)
def power_sum(k: int, N: int) -> Fraction:
    r"""Newton power sum p_k = S_k = sum_{j=2}^N j^k."""
    if N < 2:
        return Fraction(0)
    return sum(Fraction(j) ** k for j in range(2, N + 1))


def p1(N: int) -> Fraction:
    """p_1 = S_1 = sum_{j=2}^N j = N(N+1)/2 - 1."""
    return Fraction(N * (N + 1), 2) - 1


def p2(N: int) -> Fraction:
    """p_2 = S_2 = sum_{j=2}^N j^2 = N(N+1)(2N+1)/6 - 1."""
    return Fraction(N * (N + 1) * (2 * N + 1), 6) - 1


def p3(N: int) -> Fraction:
    """p_3 = S_3 = sum_{j=2}^N j^3 = [N(N+1)/2]^2 - 1."""
    return Fraction(N * (N + 1) // 2) ** 2 - 1


def elementary_e1(N: int) -> Fraction:
    """e_1(2,...,N) = p_1 = S_1."""
    return p1(N)


def elementary_e2(N: int) -> Fraction:
    """e_2(2,...,N) = (p_1^2 - p_2)/2 = sum_{2<=i<j<=N} ij."""
    return (p1(N) ** 2 - p2(N)) / 2


# ============================================================================
# The inner polynomial P_2(N) = 3N^3 + 14N^2 + 22N + 33
# ============================================================================

def inner_polynomial_P2(N: int) -> int:
    """P_2(N) = 3N^3 + 14N^2 + 22N + 33.

    Irreducible over Q. In rising factorial basis:
        P_2(N) = 3*N(N+1)(N+2) + 5*N(N+1) + 11*N + 33

    In falling factorial basis:
        P_2(N) = 18*C(N,3) + 46*C(N,2) + 39*N + 33
    """
    return 3 * N**3 + 14 * N**2 + 22 * N + 33


def P2_rising_factorial(N: int) -> int:
    """P_2(N) via rising factorial basis: 3*N^{(3)} + 5*N^{(2)} + 11*N + 33."""
    return 3 * N * (N + 1) * (N + 2) + 5 * N * (N + 1) + 11 * N + 33


def P2_falling_factorial(N: int) -> int:
    """P_2(N) via falling factorial: 18*C(N,3) + 46*C(N,2) + 39*N + 33."""
    return 18 * comb(N, 3) + 46 * comb(N, 2) + 39 * N + 33


# ============================================================================
# A_2(N): the genus-2 cross-channel polynomial (3 representations)
# ============================================================================

def A2_polynomial(N: int) -> Fraction:
    """A_2(N) = (N-2)(3N^3+14N^2+22N+33)/24.

    Rep 1: Direct polynomial formula.
    """
    if N <= 2:
        return Fraction(0)
    return Fraction((N - 2) * inner_polynomial_P2(N), 24)


def A2_power_sums(N: int) -> Fraction:
    """A_2(N) = (2*p_1^2 + p_2 - 12)/4.

    Rep 2: Via Newton power sums of the weights {2,...,N}.
    """
    s1 = p1(N)
    s2 = p2(N)
    return (2 * s1**2 + s2 - 12) / 4


def A2_symmetric(N: int) -> Fraction:
    """A_2(N) = (3*e_1^2 - 2*e_2 - 12)/4.

    Rep 3: Via elementary symmetric functions of {2,...,N}.
    """
    e1 = elementary_e1(N)
    e2 = elementary_e2(N)
    return (3 * e1**2 - 2 * e2 - 12) / 4


# ============================================================================
# Per-graph contributions to A_2(N)
# ============================================================================

def A2_figure_eight(N: int) -> Fraction:
    """Figure-eight graph contribution: e_2(2,...,N)/2 = (p_1^2 - p_2)/4.

    Graph: 1 vertex (genus 0), 2 self-loops. Aut=8. h^1=2.

    The figure-eight counts PAIRS of distinct channels (i,j) with i != j,
    weighted by the product ij of their conformal weights, divided by 4.
    This is half the second elementary symmetric function.

    Frobenius mechanism: each self-loop carries an independent channel.
    The genus-0 vertex factor V_{0,4}(i,i,j,j) = 2c (via T-exchange).
    Propagator product: (i/c)(j/c). After dividing by Aut=8:
    amplitude = ij/(4c). Mixed sum = (p_1^2 - p_2)/(4c).
    """
    s1 = p1(N)
    s2 = p2(N)
    return (s1**2 - s2) / 4


def A2_theta(N: int) -> Fraction:
    """Theta graph contribution: (p_2 - 4)/2.

    Graph: 2 vertices (genus 0), 3 parallel bridges. Aut=12. h^1=2.

    The theta graph forces all 3 edges at each genus-0 vertex to pass
    through V_{0,3}. The only nonvanishing gravitational triples are
    (T,T,T) and (T,W_j,W_j). So one edge must be T (channel 2)
    and the other two must carry matched W_j channels.

    The mixed part sums over j=3,...,N (j=2 is diagonal):
    mixed_theta = sum_{j=3}^N j^2/(2c) = (p_2 - 4)/(2c).
    """
    s2 = p2(N)
    return (s2 - 4) / 2


def A2_sunrise(N: int) -> Fraction:
    """Sunrise/dumbbell graph contribution: (p_1^2 - 4)/4.

    Graph: 2 vertices (genus 0), 2 self-loops + 1 bridge. Aut=8. h^1=2.

    The sunrise has each vertex seeing 3 half-edges: one self-loop pair
    and one bridge half-edge. The bridge is forced to channel T (=2)
    by the gravitational structure constants. Each self-loop carries
    an independent channel.

    Amplitude(a, b) = ab/(4c) where a, b are self-loop channels.
    Mixed: all (a,b) except (2,2), giving (p_1^2 - 4)/(4c).
    """
    s1 = p1(N)
    return (s1**2 - 4) / 4


def A2_graph_decomposition(N: int) -> Dict[str, Fraction]:
    """Complete graph decomposition of A_2(N).

    Returns per-graph contributions and their sum.
    """
    fe = A2_figure_eight(N)
    th = A2_theta(N)
    sr = A2_sunrise(N)
    return {
        'figure_eight': fe,
        'theta': th,
        'sunrise': sr,
        'total': fe + th + sr,
    }


# ============================================================================
# B_2(N): the c-independent coefficient (sunset graph)
# ============================================================================

def B2_polynomial(N: int) -> Fraction:
    """B_2(N) = (N-2)(N+3)/96.

    Rep 1: Direct polynomial formula.
    """
    if N <= 2:
        return Fraction(0)
    return Fraction((N - 2) * (N + 3), 96)


def B2_power_sum(N: int) -> Fraction:
    """B_2(N) = (p_1 - 2)/48.

    Rep 2: Via the first power sum.

    Source: SUNSET graph (1 genus-0 vertex + 1 genus-1 vertex,
    1 self-loop + 1 bridge). The bridge is forced to T-channel.
    The self-loop channel a runs over {2,...,N}.
    Amplitude(a) = a/48 (independent of c!).
    Mixed: a != 2, giving (p_1 - 2)/48.
    """
    s1 = p1(N)
    return (s1 - 2) / 48


# ============================================================================
# Full genus-2 cross-channel correction
# ============================================================================

def delta_F2_grav(N: int, c: Fraction) -> Fraction:
    """delta_F_2^grav(W_N, c) = B_2(N) + A_2(N)/c.

    The universal gravitational cross-channel correction at genus 2.
    """
    if N <= 2:
        return Fraction(0)
    return B2_polynomial(N) + A2_polynomial(N) / c


# ============================================================================
# All 7 genus-2 stable graphs (n=0)
# ============================================================================

def genus2_all_graphs_mixed(N: int, c: Fraction) -> Dict[str, Fraction]:
    """Per-graph mixed contributions from all 7 genus-2 stable graphs.

    Returns dict with graph names and their mixed amplitudes.

    Graph 0: SMOOTH   (g=2 vertex, no edges) -> 0
    Graph 1: TADPOLE  (g=1 vertex, 1 self-loop, h1=1) -> 0 (single edge)
    Graph 2: FIG-EIGHT (g=0 vertex, 2 self-loops, h1=2)
    Graph 3: BARBELL  (2 g=1 vertices, 1 bridge, h1=0) -> 0 (single edge)
    Graph 4: THETA    (2 g=0 vertices, 3 bridges, h1=2)
    Graph 5: SUNSET   (g=0+g=1, SL+bridge, h1=1)
    Graph 6: SUNRISE  (2 g=0 vertices, 2SL+bridge, h1=2)
    """
    fe = A2_figure_eight(N) / c
    th = A2_theta(N) / c
    sr = A2_sunrise(N) / c
    su = B2_power_sum(N)  # c-independent

    return {
        'smooth': Fraction(0),
        'tadpole': Fraction(0),
        'figure_eight': fe,
        'barbell': Fraction(0),
        'theta': th,
        'sunset': su,
        'sunrise': sr,
        'total': fe + th + sr + su,
    }


# ============================================================================
# Genus-3 structure (for degree pattern verification)
# ============================================================================

def genus3_inner_polynomial_degrees() -> Dict[str, int]:
    """Degree pattern of inner polynomials at genus 3.

    At genus 3, delta_F_3 = D(N)*c + C(N) + B(N)/c + A(N)/c^2.
    Each coefficient has the form (N-2) * Q(N) / denom.
    Returns the degree of Q(N) for each coefficient.
    """
    return {
        'D_inner_degree': 0,   # D = (N-2)/27648
        'C_inner_degree': 2,   # C = (N-2)(35N^2+133N+234)/34560
        'B_inner_degree': 4,   # B = (N-2)(15N^4+...)/1728
        'A_inner_degree': 6,   # A = (N-2)(120N^6+...)/1080
    }


def degree_pattern_conjecture(g: int) -> Dict[str, int]:
    """Conjectured degree pattern at genus g.

    Returns:
        inner_degree_leading: degree of inner polynomial Q_g in A_g = (N-2)*Q_g/D_g
        total_degree_A_g: total degree of A_g(N)
        num_power_sums: number of power sums p_k needed
    """
    return {
        'inner_degree_leading': 3 * (g - 1),
        'total_degree_A_g': 3 * g - 2,
        'num_power_sums': 2 * (g - 1),
    }


# ============================================================================
# Representation-theoretic invariants
# ============================================================================

def weight_operator_trace(k: int, N: int) -> Fraction:
    """tr(D^k) where D = diag(2, 3, ..., N) is the weight operator.

    This equals the Newton power sum p_k of the conformal weights.
    In the representation-theoretic interpretation, D acts on the
    (N-1)-dimensional 'channel space' C^{N-1} with eigenvalues {2,...,N}.
    """
    return power_sum(k, N)


def quadratic_casimir_cross(N: int) -> Fraction:
    """The quadratic Casimir-like invariant Q = 2*(tr D)^2 + tr(D^2).

    A_2(N) = (Q - 12)/4. The invariant Q depends on the channel space
    representation through the first two traces of D.
    """
    t1 = p1(N)
    t2 = p2(N)
    return 2 * t1**2 + t2


def virasoro_baseline() -> int:
    """The N=2 (Virasoro) baseline: 2*p_1(2)^2 + p_2(2) = 2*4+4 = 12.

    This is subtracted to ensure A_2(2) = 0 (no cross-channel for
    uniform-weight algebras).
    """
    return 12


# ============================================================================
# Propagator variance connection
# ============================================================================

def propagator_variance(N: int) -> Fraction:
    r"""Propagator variance delta_mix for W_N.

    delta_mix = sum_i f_i^2/kappa_i - (sum_i f_i)^2 / sum_i kappa_i

    For the gravitational Frobenius with f_i = kappa_i = c/i:
    delta_mix = sum_i (c/i)^2/(c/i) - (sum_i c/i)^2/(sum_i c/i)
              = sum_i c/i - c * (sum_i 1/i)^2 / (sum_i 1/i)
              = c * H - c * H = 0

    The propagator variance VANISHES for the gravitational Frobenius
    (all channels have f proportional to kappa). This is the
    'enhanced symmetry' condition.

    For the FULL W_N Frobenius (with OPE structure constants),
    the variance is generically nonzero.
    """
    # For gravitational Frobenius: proportional channels, so variance = 0.
    return Fraction(0)


# ============================================================================
# The Hardy-Ramanujan correction
# ============================================================================

def hardy_ramanujan_check() -> str:
    """Check: does 1729 appear in A_2(N)?

    The task description suggested A_2(6) might give 1729/4.
    CORRECTED: A_2(6) = 439/2, not 1729/4.

    1729 = 12^3 + 1^3 = 10^3 + 9^3 (Hardy-Ramanujan taxicab number)
    does NOT appear as a numerator of A_2(N) for any N <= 100.
    """
    for N in range(2, 101):
        a2 = A2_polynomial(N)
        if a2.numerator == 1729 or (a2 * 4).numerator == 1729:
            return f"1729 found at N={N}: A_2={a2}"
    return "1729 does NOT appear as numerator of A_2(N) or 4*A_2(N) for N=2..100"


# ============================================================================
# W-only form (excluding j=2 / Virasoro singleton)
# ============================================================================

def power_sum_W_only(k: int, N: int) -> Fraction:
    r"""Newton power sum p_k' = sum_{j=3}^N j^k over the strict W-generators.

    Excludes j=2 (the Virasoro stress tensor). For N <= 2 the sum is empty.
    """
    if N < 3:
        return Fraction(0)
    return sum(Fraction(j) ** k for j in range(3, N + 1))


def A2_W_only_form(N: int) -> Fraction:
    r"""A_2(N) computed in the W-only basis (no -12 constant).

    Identity:
        4 A_2(N) = 2 (p_1')^2 + p_2' + 8 p_1'
                 = 2 p_1' (p_1' + 4) + p_2'

    where p_k' = sum_{j=3}^N j^k.

    Derivation. Substitute p_1 = p_1' + 2 and p_2 = p_2' + 4 into the
    closed form 4 A_2 = 2 p_1^2 + p_2 - 12:

        2 (p_1' + 2)^2 + (p_2' + 4) - 12
            = 2 p_1'^2 + 8 p_1' + 8 + p_2' - 8
            = 2 p_1'^2 + p_2' + 8 p_1'.

    The constant -12 is exactly the j=2 (Virasoro singleton) contribution
    to 2 p_1^2 + p_2. The cross-coupling 8 = 2 * (2 * 2) is the
    bilinear coupling between the j=2 mode and the W-generators.
    """
    s1 = power_sum_W_only(1, N)
    s2 = power_sum_W_only(2, N)
    return (2 * s1 ** 2 + s2 + 8 * s1) / 4


# ============================================================================
# Asymptotic verification: A_2(N) / N^4 -> 1/8 = 3/24
# ============================================================================

def asymptotic_ratio(N: int) -> Fraction:
    r"""Ratio A_2(N) / N^4. As N -> infinity this tends to 1/8."""
    if N < 2:
        return Fraction(0)
    return A2_polynomial(N) / Fraction(N ** 4)


def asymptotic_leading_coefficient() -> Fraction:
    r"""The leading coefficient of A_2(N): 1/8 = 3/24.

    From A_2(N) = (N-2)(3N^3 + 14 N^2 + 22 N + 33)/24, the leading
    monomial is 3 N^4 / 24 = N^4/8. The 3 in the cubic is the leading
    coefficient of the inner polynomial; the /24 is the genus-2
    automorphism / cyclic-symmetry denominator.
    """
    return Fraction(1, 8)


def asymptotic_subleading_coefficients() -> Dict[str, Fraction]:
    r"""All polynomial coefficients of A_2(N) in the monomial basis.

    A_2(N) = N^4/8 + N^3/3 - N^2/4 - 11 N/24 - 11/4.

    Sanity check on signs: the cubic 14 N^2 contributes N^3 * 14/24
    plus -2 * 3 N^3/24 = (14 - 6)/24 = 8/24 = 1/3.  Verified.
    """
    return {
        'N4': Fraction(1, 8),
        'N3': Fraction(1, 3),
        'N2': Fraction(-1, 4),
        'N1': Fraction(-11, 24),
        'N0': Fraction(-11, 4),
    }


# ============================================================================
# OEIS-negative result and integer sequences
# ============================================================================

def cubic_value_sequence(N_max: int = 16) -> List[int]:
    r"""Integer sequence {3 N^3 + 14 N^2 + 22 N + 33 : N = 0, 1, ..., N_max-1}.

    Values for N = 0..15:
        33, 72, 157, 306, 537, 868, 1317, 1902, 2641, 3552, 4653,
        5962, 7497, 9276, 11317, 13638.

    OEIS LOOKUP RESULT: this sequence is NOT present in OEIS as of
    2026-04-07. The cubic 3 N^3 + 14 N^2 + 22 N + 33 is irreducible
    over Q (one real root near -3.47, complex conjugate pair) and
    does not coincide with any catalogued combinatorial polynomial.
    Conclusion: P_2(N) is a NEW polynomial introduced by the multi-
    weight genus-2 cross-channel decomposition; it has no prior
    combinatorial interpretation.
    """
    return [inner_polynomial_P2(N) for N in range(N_max)]


def A2_times_4_integer_sequence(N_max: int = 16) -> List[int]:
    r"""Integer sequence {4 A_2(N) : N = 2, 3, ..., N_max+1}.

    Values for N = 2..15:
        0, 51, 179, 434, 878, 1585, 2641, 4144, 6204, 8943,
        12495, 17006, 22634, 29549.

    OEIS LOOKUP RESULT: NOT in OEIS. The numerators are dominated by
    large primes (e.g. 179, 439, 1317 = 3*439, 11317 prime), confirming
    that A_2(N) has no clean Stanley/Macdonald-style factorization
    and is intrinsically a new sequence.
    """
    out = []
    for N in range(2, 2 + N_max):
        a4 = 4 * A2_polynomial(N)
        # Always integer because the formula has denominator 4
        # (the /24 in (N-2)*P_2/24 reduces to /4 once times 4).
        # Verify integrality:
        assert a4.denominator == 1, f"4*A_2({N}) = {a4} is not an integer"
        out.append(a4.numerator)
    return out


# ============================================================================
# Per-element interpretation: 4 A_2 + 12 as a weighted pair count
# ============================================================================

def pair_weight_count(N: int) -> Fraction:
    r"""Count 4 A_2(N) + 12 = sum over ORDERED pairs (i,j) in {2,..,N}^2 of 2 i j
    plus sum_j j^2 over the diagonal.

    Equivalently: 2 p_1^2 + p_2 = sum over (i,j) ordered of 2 i j + sum_j j^2.

    Combinatorial reading. Let (i,j) range over ORDERED pairs of conformal
    weights from {2,..,N}. The weighted count

        sum_{(i,j)} 2 i j + sum_j j^2
            = sum_{i != j} 2 i j + sum_{i = j} (2 j^2 + j^2)
            = sum_{i != j} 2 i j + sum_j 3 j^2

    counts the number of "channel-pair contact insertions" at a genus-2
    stable graph: each off-diagonal pair (i, j) with i != j contributes
    weight 2 i j (one for each cyclic orientation of the bilinear insertion);
    each diagonal pair (j, j) contributes weight 3 j^2 (the symmetric
    diagonal multiplier from the figure-eight self-loop weight).
    """
    s1 = p1(N)
    s2 = p2(N)
    return 2 * s1 ** 2 + s2


def virasoro_singleton_subtraction() -> int:
    r"""The constant 12 = 2 * 2^2 + 2^2 = 8 + 4.

    Decomposition: the j=2 (Virasoro stress tensor) is the unique
    weight in {2,..,N} for N=2. Its contribution to 2 p_1^2 + p_2 is
    2 * (2)^2 + (2)^2 = 12. Subtracting 12 from the universal
    quadratic invariant 2 p_1^2 + p_2 zeroes the Virasoro baseline,
    so that A_2(2) = 0 (uniform-weight algebras have no genus-2
    cross-channel correction).
    """
    return 12
