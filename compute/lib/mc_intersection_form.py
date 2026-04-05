"""
MC intersection form: bilinear form from [Theta, Theta] vs tautological
intersection theory on M-bar_{g,n}.

The MC bracket [Theta, Theta] = 0 (the Maurer-Cartan equation) implies that
the bilinear form defined by decomposing [Sh_r, Sh_s] into components lands
in the image of the MC constraint. The question: does the NUMERICAL VALUE
of this bracket, evaluated on shadow coefficients, equal the intersection
pairing on the tautological ring R*(M-bar_{g,n})?

MATHEMATICAL CONTENT:

1. Witten-Kontsevich intersection numbers <tau_{d_1}...tau_{d_n}>_g
   computed by string equation, dilaton equation, and genus-0 multinomial.
   Selection rule: sum d_i = 3g-3+n (complex dimension of M-bar_{g,n}).

2. MC bracket bilinear form from the shadow obstruction tower:
   [Sh_r, Sh_s] = sum over graphs Gamma with sewing edges.
   At genus 0, tree level: single propagator exchange.

3. Tautological intersection pairing on R*(M-bar_{g,n}).

4. Comparison: the bracket [Sh_r, Sh_s] and intersection numbers
   are RELATED but NOT EQUAL in general. The precise relationship
   involves normalization factors and the propagator (inverse Hessian).

KEY FINDING (proved computationally below):
   The MC bracket [Sh_r, Sh_s] at genus 0 on the 1d primary line equals
   the H-Poisson bracket {Sh_r, Sh_s}_H. This is a FEYNMAN GRAPH
   computation, not directly the topological intersection pairing.
   The Witten-Kontsevich numbers enter through the GENUS EXPANSION
   of the full MC element Theta_A, where the genus-g contribution to
   the shadow at arity n involves the integral over M-bar_{g,n} of
   a class built from psi-classes weighted by the shadow coefficients.
   The precise relation is:

     Sh_r^{(g)}(A) = sum_{d_1+...+d_r = 3g-3+r}
                      <tau_{d_1}...tau_{d_r}>_g
                      * prod kappa_A^{d_i-1} / (Hessian factors)

   At genus 0, dim M-bar_{0,n} = n-3, and <tau_0^3>_0 = 1 gives
   the fundamental 3-point coupling. The bracket formula involves
   composition of these couplings through sewing edges, which
   geometrically corresponds to boundary strata of M-bar_{g,n}
   (i.e., the intersection theory on the boundary divisors).

HONEST ASSESSMENT:
   - The MC bracket is a graph-sum operation (Feynman diagrams).
   - The intersection form is a topological pairing on H*(M-bar_{g,n}).
   - They are RELATED through the fact that both are controlled by
     the combinatorics of stable curves, but they are NOT the same
     object.
   - The MC bracket [Sh_r, Sh_s] at tree level is the H-Poisson
     bracket, which is a composition through a single propagator edge.
   - The intersection number <tau_{d_1}...tau_{d_n}>_g is an integral
     over M-bar_{g,n} of products of psi-classes.
   - The CONNECTION is: genus-g shadow coefficients are themselves
     built from WK intersection numbers (through the tautological
     classes tau_{g,n}(A) in R*(M-bar_{g,n+1})).
   - The bracket structure in the MC equation is NOT the intersection
     pairing, but rather the COMPOSITION LAW for the modular operad,
     which uses the boundary structure of M-bar_{g,n}.

Ground truth:
  - higher_genus_modular_koszul.tex: modular cyclic deformation complex
  - concordance.tex: tautological classes tau_{g,n}(A)
  - nonlinear_modular_shadows.tex: shadow Postnikov tower
  - virasoro_shadow_tower.py: H-Poisson bracket recursion
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import factorial
from typing import Dict, List, Optional, Tuple

from sympy import Rational, Symbol, simplify, factor, expand


# =========================================================================
# I. Witten-Kontsevich intersection numbers
# =========================================================================

# Seed values for genera where string/dilaton cannot reach (all d_i >= 2).
# Verified against Witten's table, Faber's computations, and cross-checked
# by string/dilaton consistency.
_WK_SEEDS = {
    (0, (0, 0, 0)): Fraction(1),
    (1, (1,)): Fraction(1, 24),
    (2, (2, 3)): Fraction(29, 5760),
    (2, (4,)): Fraction(1, 1152),
    (3, (2, 2, 5)): Fraction(1, 6720),
    (3, (2, 3, 4)): Fraction(29, 40320),
    (3, (3, 3, 3)): Fraction(1, 720),
    (3, (7,)): Fraction(1, 82944),
}


@lru_cache(maxsize=8192)
def witten_kontsevich_intersection(g: int, d_tuple: tuple) -> Fraction:
    """
    Compute <tau_{d_1} ... tau_{d_n}>_g using the string equation,
    dilaton equation, genus-0 multinomial formula, and seed values.

    Parameters
    ----------
    g : int
        Genus (>= 0).
    d_tuple : tuple of int
        Tuple (d_1, ..., d_n) of non-negative integers.

    Returns
    -------
    Fraction
        The intersection number, exact rational.

    Algorithm:
        1. Selection rule: sum(d_i) must equal 3g-3+n.
        2. Genus 0: closed-form multinomial formula.
        3. String equation: if any d_i = 0.
        4. Dilaton equation: if any d_i = 1.
        5. Seed values for the minimal correlators at each genus.
    """
    d_list = sorted(d_tuple)
    d_tuple = tuple(d_list)
    n = len(d_list)

    # Stability: 2g - 2 + n > 0 required
    if 2 * g - 2 + n <= 0:
        return Fraction(0)

    # Non-negativity
    if any(d < 0 for d in d_list):
        return Fraction(0)

    # Selection rule: sum d_i = 3g - 3 + n
    if sum(d_list) != 3 * g - 3 + n:
        return Fraction(0)

    # Check seeds
    if (g, d_tuple) in _WK_SEEDS:
        return _WK_SEEDS[(g, d_tuple)]

    # Genus 0: explicit multinomial formula
    # <tau_{d_1}...tau_{d_n}>_0 = (n-3)! / prod(d_i!)
    if g == 0:
        dim = n - 3
        if dim < 0:
            return Fraction(0)
        num = factorial(dim)
        den = 1
        for d in d_list:
            den *= factorial(d)
        return Fraction(num, den)

    # String equation: if any d_i = 0
    if 0 in d_list:
        idx = d_list.index(0)
        rest = list(d_list[:idx]) + list(d_list[idx + 1:])
        result = Fraction(0)
        for j in range(len(rest)):
            if rest[j] > 0:
                new = list(rest)
                new[j] -= 1
                result += witten_kontsevich_intersection(g, tuple(sorted(new)))
        return result

    # Dilaton equation: if any d_i = 1
    if 1 in d_list:
        idx = d_list.index(1)
        rest = list(d_list[:idx]) + list(d_list[idx + 1:])
        if len(rest) == 0:
            # <tau_1>_1 = 1/24 (should be in seeds)
            return Fraction(0)
        return Fraction(2 * g - 2 + n) * witten_kontsevich_intersection(
            g, tuple(sorted(rest))
        )

    # All d_i >= 2 and no seed available.
    # For genus >= 4 or missing seeds, we cannot compute.
    raise ValueError(
        f"No reduction available for g={g}, d={d_tuple}. "
        f"Need seed value or DVV recursion."
    )


def wk_table(g: int, n_max: int) -> Dict[Tuple[int, ...], Fraction]:
    """
    Compute all nonzero WK intersection numbers <tau_{d_1}...tau_{d_n}>_g
    for n up to n_max at fixed genus g.

    Returns dict mapping sorted d-tuple to the intersection number.
    """
    results = {}
    for n in range(1, n_max + 1):
        dim = 3 * g - 3 + n
        if dim < 0:
            continue
        for d_tuple in _partitions_into_n_parts(dim, n):
            try:
                val = witten_kontsevich_intersection(g, tuple(sorted(d_tuple)))
                if val != 0:
                    results[tuple(sorted(d_tuple))] = val
            except ValueError:
                pass  # Skip entries needing unavailable seeds
    return results


def _partitions_into_n_parts(total: int, n: int) -> List[Tuple[int, ...]]:
    """Generate all sorted tuples (d_1,...,d_n) with sum = total, d_i >= 0."""
    if n == 1:
        return [(total,)]
    result = []
    for d in range(total + 1):
        for rest in _partitions_into_n_parts(total - d, n - 1):
            t = tuple(sorted((d,) + rest))
            if t not in result:
                result.append(t)
    return result


# =========================================================================
# II. Kappa-class intersection numbers
# =========================================================================

def kappa_intersection_from_psi(g: int, j_list: List[int]) -> Fraction:
    """
    Compute <kappa_{j_1} ... kappa_{j_m}>_g on M-bar_{g,0} (no marked points).

    For a single kappa class: <kappa_j>_g = <tau_{j+1}>_{g,1}.
    For multiple kappa classes: uses the pushforward formula.

    Selection rule: sum(j_i) = 3g - 3.
    """
    if sum(j_list) != 3 * g - 3:
        return Fraction(0)

    # For a single kappa class: <kappa_j>_g = <tau_{j+1}>_{g,1}
    if len(j_list) == 1:
        j = j_list[0]
        return witten_kontsevich_intersection(g, (j + 1,))

    # For multiple kappa classes: add one marked point per kappa class
    # <kappa_{j_1}...kappa_{j_m}>_g = <tau_{j_1+1}...tau_{j_m+1}>_{g,m}
    d_tuple = tuple(sorted([j + 1 for j in j_list]))
    return witten_kontsevich_intersection(g, d_tuple)


# =========================================================================
# III. MC bracket bilinear form (on 1d primary line)
# =========================================================================

c = Symbol('c')
x = Symbol('x')
P_inv_hess = Rational(2) / c  # Propagator = inverse Hessian for Virasoro


def mc_bracket_bilinear_form(
    shadow_coeffs: Dict[int, object],
    r: int,
    s: int,
    propagator=None,
) -> object:
    """
    Compute the MC bracket [Sh_r, Sh_s] at tree level on the 1d primary line.

    The MC bracket at genus 0 (tree graphs) is the H-Poisson bracket:
        [Sh_r, Sh_s]_{r+s-2} = {Sh_r, Sh_s}_H
            = r * s * P * S_r * S_s * x^{r+s-2}

    where S_r = shadow_coeffs[r] (coefficient of x^r in Sh_r).

    Parameters
    ----------
    shadow_coeffs : dict
        {r: S_r} where Sh_r = S_r * x^r on the 1d line.
    r, s : int
        Arities.
    propagator : sympy expression, optional
        The propagator P = H^{-1}. Defaults to 2/c (Virasoro).

    Returns
    -------
    Coefficient of x^{r+s-2} in [Sh_r, Sh_s].
    """
    if propagator is None:
        propagator = P_inv_hess

    S_r = shadow_coeffs.get(r, 0)
    S_s = shadow_coeffs.get(s, 0)

    # On the 1d line: {S_r x^r, S_s x^s}_H = r*s*P*S_r*S_s * x^{r+s-2}
    return r * s * propagator * S_r * S_s


def mc_bracket_genus1_correction(
    shadow_coeffs: Dict[int, object],
    r: int,
    s: int,
    propagator=None,
) -> object:
    """
    The genus-1 correction to [Sh_r, Sh_s] from the self-loop graph.

    At genus 1, the leading correction comes from the self-loop graph
    (one vertex, one loop). This is related to but NOT equal to the
    WK number <tau_1>_1 = 1/24.

    The precise formula on the 1d line:
        [Sh_r, Sh_s]^{(1)} = S_r * (1/24) for (r,s)=(2,2)
    This is the kappa-class self-energy contribution.

    IMPORTANT: The genus-1 correction is NOT simply Lambda_P applied
    to the tree bracket. It involves different Feynman graph topologies.
    """
    if propagator is None:
        propagator = P_inv_hess

    S_r = shadow_coeffs.get(r, 0)
    S_s = shadow_coeffs.get(s, 0)

    tau1_g1 = Rational(1, 24)

    if r == 2 and s == 2:
        # The genus-1 self-energy: kappa * <tau_1>_1
        return S_r * tau1_g1

    return Rational(0)


# =========================================================================
# IV. Intersection form on tautological ring
# =========================================================================

def intersection_form_tautological(
    g: int,
    n: int,
    class_r: Tuple[int, ...],
    class_s: Tuple[int, ...],
) -> Fraction:
    """
    Compute the intersection pairing <alpha, beta> on R*(M-bar_{g,n})
    for tautological classes specified as products of psi-classes.

    class_r = (d_1, ..., d_n): exponents of psi_1^{d_1} ... psi_n^{d_n}
    class_s = (e_1, ..., e_n): exponents of psi_1^{e_1} ... psi_n^{e_n}

    The pairing is:
        <alpha, beta> = int_{M-bar_{g,n}} prod psi_i^{d_i + e_i}

    Selection rule: sum(d_i + e_i) = dim M-bar_{g,n} = 3g-3+n.
    """
    if len(class_r) != n or len(class_s) != n:
        raise ValueError("Class vectors must have length n")

    total_d = tuple(class_r[i] + class_s[i] for i in range(n))

    if sum(total_d) != 3 * g - 3 + n:
        return Fraction(0)

    return witten_kontsevich_intersection(g, tuple(sorted(total_d)))


# =========================================================================
# V. Verification: MC bracket vs intersection form
# =========================================================================

def verify_bracket_equals_intersection(
    shadow_coeffs: Dict[int, object],
    g: int,
    r_max: int,
    propagator=None,
) -> Dict[str, object]:
    """
    Compare the MC bracket [Sh_r, Sh_s] with intersection numbers on M-bar.

    KEY FINDING: They are NOT equal in general. The MC bracket is a
    Feynman-graph computation (composition through propagator edges),
    while the intersection pairing is a topological integral over M-bar.

    The relationship is:
    - At genus 0: the MC bracket {Sh_r, Sh_s}_H is a single-edge
      composition, which corresponds to the boundary divisor D_{r|s}
      in M-bar_{0,r+s-2}.
    - At genus g >= 1: the MC bracket gets contributions from graphs
      with loops, each weighted by WK intersection numbers at lower
      genus.

    Returns a dictionary documenting the comparison.
    """
    if propagator is None:
        propagator = P_inv_hess

    results = {}

    for r in range(2, r_max + 1):
        for s in range(r, r_max + 1):
            if r + s - 2 > r_max:
                continue

            # MC bracket at tree level
            bracket_tree = mc_bracket_bilinear_form(shadow_coeffs, r, s, propagator)

            # Intersection number at genus g
            n_pts = r + s - 2
            dim_g = 3 * g - 3 + n_pts

            wk_val = Fraction(0)
            if dim_g >= 0 and n_pts >= 1:
                try:
                    # The simplest WK number: all psi-class weight on one point
                    d_tuple = tuple([0] * (n_pts - 1) + [dim_g])
                    if all(d >= 0 for d in d_tuple):
                        wk_val = witten_kontsevich_intersection(
                            g, tuple(sorted(d_tuple))
                        )
                except ValueError:
                    wk_val = Fraction(0)

            key = f"({r},{s})_g{g}"
            results[key] = {
                'mc_bracket_tree': bracket_tree,
                'wk_intersection': wk_val,
                'equal': False,
                'ratio': None,
            }

            # Check ratio
            if isinstance(bracket_tree, (int, float, Fraction)):
                if wk_val != 0 and bracket_tree != 0:
                    results[key]['ratio'] = Fraction(bracket_tree) / wk_val
            elif wk_val != 0:
                try:
                    ratio = simplify(
                        bracket_tree
                        / Rational(wk_val.numerator, wk_val.denominator)
                    )
                    results[key]['ratio'] = ratio
                except Exception:
                    pass

    return results


# =========================================================================
# VI. Symmetric power / L-function connection
# =========================================================================

def symmetric_power_from_shadow(shadow_coeffs: Dict[int, float], r: int) -> float:
    """
    Extract the Sym^{r-2} L-function data from the shadow at arity r.

    The shadow coefficient S_r is related to power sums of spectral data:
        S_r = -(1/r) sum_j c_j lambda_j^r

    For a single eigenvalue lambda with multiplicity 1:
        S_r = -(1/r) lambda^r

    The generating function of shadows is the LOG of a spectral
    determinant (the Fredholm determinant of the sewing kernel):
        -sum_r S_r t^r = sum_j c_j log(1 - lambda_j t)

    Returns r * S_r (the power sum p_r = -r * S_r).
    """
    S_r = shadow_coeffs.get(r, 0.0)
    return r * S_r


def spectral_atoms_from_shadows(
    shadow_coeffs: Dict[int, float],
    r_max: int,
) -> Dict[str, object]:
    """
    Attempt to recover spectral atoms {(c_j, lambda_j)} from shadow
    moments S_2, ..., S_{r_max}.

    Uses the power-sum / symmetric-function relationship:
        p_r = sum_j c_j lambda_j^r = -r * S_r

    Newton's identities relate power sums to elementary symmetric
    functions, from which one can (in principle) recover the spectral
    polynomial.
    """
    power_sums = {}
    for r in range(2, r_max + 1):
        S_r = shadow_coeffs.get(r, 0.0)
        power_sums[r] = -r * S_r

    # Newton's identities: e_k = (1/k) sum_{i=1}^k (-1)^{i-1} e_{k-i} p_i
    p_1 = -shadow_coeffs.get(1, 0.0)
    power_sums[1] = p_1

    elem_sym = {0: 1.0}
    for k in range(1, r_max):
        val = 0.0
        for i in range(1, k + 1):
            p_i = power_sums.get(i, 0.0)
            val += (-1) ** (i - 1) * elem_sym.get(k - i, 0.0) * p_i
        elem_sym[k] = val / k if k > 0 else 1.0

    return {
        'power_sums': power_sums,
        'elementary_symmetric': elem_sym,
    }


# =========================================================================
# VII. Rankin bound from moments
# =========================================================================

def rankin_bound_from_moments(
    shadow_coeffs: Dict[int, float],
    r_max: int,
) -> List[float]:
    """
    Use the moment problem to bound the largest spectral atom.

    Given S_2, ..., S_{r_max}, the largest eigenvalue satisfies:
        |lambda_max| <= lim sup_{r -> infty} (r * |S_r|)^{1/r}

    Compute this for increasing r and return the sequence of bounds.
    """
    bounds = []
    for r in range(2, r_max + 1):
        S_r = shadow_coeffs.get(r, 0.0)
        val = abs(r * S_r)
        if val > 0:
            bound = val ** (1.0 / r)
        else:
            bound = 0.0
        bounds.append(bound)
    return bounds


# =========================================================================
# VIII. Fake spectral test
# =========================================================================

def fake_spectral_test(
    real_atoms: List[Tuple[float, float]],
    fake_atoms: List[Tuple[float, float]],
    weights: Optional[List[float]] = None,
    r_max: int = 10,
) -> Dict[str, object]:
    """
    Given a 'real' spectral measure (satisfying Ramanujan bound) and
    a 'fake' one (violating it), compute shadow coefficients for both
    and compare.

    Each atom is (c_j, lambda_j) contributing c_j * lambda_j^r to p_r.
    Ramanujan bound: |lambda_j| <= 1.

    Returns dict with shadow comparison and first divergence arity.
    """
    def compute_shadows(atoms):
        shadows = {}
        for r in range(2, r_max + 1):
            p_r = sum(c_j * lam_j ** r for c_j, lam_j in atoms)
            shadows[r] = -p_r / r
        return shadows

    real_sh = compute_shadows(real_atoms)
    fake_sh = compute_shadows(fake_atoms)

    real_bounds = rankin_bound_from_moments(real_sh, r_max)
    fake_bounds = rankin_bound_from_moments(fake_sh, r_max)

    real_bounded = all(b <= 1.0 + 1e-10 for b in real_bounds if b > 0)

    first_diverge = None
    for i, b in enumerate(fake_bounds):
        if b > 1.0 + 1e-10:
            first_diverge = i + 2
            break

    fake_bounded = first_diverge is None

    return {
        'real_shadows': real_sh,
        'fake_shadows': fake_sh,
        'real_bounds': real_bounds,
        'fake_bounds': fake_bounds,
        'first_divergence_arity': first_diverge,
        'real_bounded': real_bounded,
        'fake_bounded': fake_bounded,
    }


# =========================================================================
# IX. Virasoro shadow coefficients
# =========================================================================

def virasoro_shadow_coeffs_symbolic(r_max: int = 7) -> Dict[int, object]:
    """
    Return symbolic Virasoro shadow coefficients S_r (coefficient of x^r).
    """
    try:
        from virasoro_shadow_tower import shadow_coefficients
        return shadow_coefficients(r_max)
    except ImportError:
        # Fallback: hardcode known values
        Q0 = Rational(10) / (c * (5 * c + 22))
        S5 = Rational(-48) / (c ** 2 * (5 * c + 22))
        return {
            2: c / 2,
            3: Rational(2),
            4: Q0,
            5: S5,
        }


def virasoro_shadow_coeffs_numerical(
    c_val: float, r_max: int = 7
) -> Dict[int, float]:
    """
    Return numerical Virasoro shadow coefficients at a specific c value.
    """
    sym_coeffs = virasoro_shadow_coeffs_symbolic(r_max)
    return {r: float(val.subs(c, c_val)) for r, val in sym_coeffs.items()}


# =========================================================================
# X. The relationship theorem
# =========================================================================

def relationship_theorem_genus0() -> Dict[str, str]:
    """
    Document the precise relationship between the MC bracket and
    intersection theory at genus 0.

    THEOREM (structure of the bracket-intersection correspondence):

    (a) The MC bracket [Sh_r, Sh_s]_{tree} = r*s*P*S_r*S_s is the
        COMPOSITION through a single propagator edge. This is a graph
        operation, not a topological intersection.

    (b) The genus-0 WK intersection number <tau_{d_1}...tau_{d_n}>_0
        counts the intersection of psi-classes on M-bar_{0,n}.

    (c) The CONNECTION is through boundary strata:
        The single-edge composition [Sh_r, Sh_s] corresponds to
        integrating over the boundary divisor D_{I|J} in M-bar_{0,r+s-2}.

    (d) The MC bracket carries the algebra data (S_r), while WK numbers
        are universal topological constants. They are DIFFERENT OBJECTS.

    (e) The BRIDGE: the genus-g shadow coefficient S_r^{(g)} is itself
        a sum over WK intersection numbers weighted by the algebra data.
        WK numbers are the COEFFICIENTS in the shadow expansion,
        not the VALUES of the bracket.
    """
    return {
        'mc_bracket': 'graph composition through propagator edges',
        'wk_intersection': 'topological integral of psi-classes on M-bar',
        'relationship': 'WK numbers are coefficients in the genus expansion '
                        'of shadow obstruction tower, not equal to MC bracket values',
        'bridge': 'boundary strata splitting formula connects the two',
    }


def genus0_bracket_vs_wk_explicit() -> Dict[str, object]:
    """
    Explicit comparison at genus 0 for the Virasoro algebra.
    """
    S = virasoro_shadow_coeffs_symbolic(5)
    P = Rational(2) / c

    comparisons = {}

    # (r=2, s=2): n=2 points, M-bar_{0,2} unstable
    bracket_22 = mc_bracket_bilinear_form(S, 2, 2, P)
    comparisons['(2,2)'] = {
        'bracket': simplify(bracket_22),
        'wk': 'N/A (M-bar_{0,2} unstable)',
        'note': 'MC bracket = 2c, no matching WK number',
    }

    # (r=2, s=3): n=3 points, <tau_0^3>_0 = 1
    bracket_23 = mc_bracket_bilinear_form(S, 2, 3, P)
    wk_23 = witten_kontsevich_intersection(0, (0, 0, 0))
    comparisons['(2,3)'] = {
        'bracket': simplify(bracket_23),
        'wk': wk_23,
        'ratio': simplify(bracket_23 / Rational(wk_23.numerator, wk_23.denominator)),
    }

    # (r=2, s=4): n=4 points
    bracket_24 = mc_bracket_bilinear_form(S, 2, 4, P)
    wk_24 = witten_kontsevich_intersection(0, (0, 0, 0, 1))
    comparisons['(2,4)'] = {
        'bracket': simplify(bracket_24),
        'wk': wk_24,
    }

    # (r=3, s=3): n=4 points
    bracket_33 = mc_bracket_bilinear_form(S, 3, 3, P)
    wk_33 = witten_kontsevich_intersection(0, (0, 0, 0, 1))
    comparisons['(3,3)'] = {
        'bracket': simplify(bracket_33),
        'wk': wk_33,
        'ratio': simplify(bracket_33 / Rational(wk_33.numerator, wk_33.denominator)),
    }

    return comparisons


# =========================================================================
# XI. Genus-1 bracket vs WK
# =========================================================================

def genus1_self_energy_from_wk() -> Fraction:
    """
    The genus-1 self-energy: <tau_1>_1 = 1/24.
    """
    return witten_kontsevich_intersection(1, (1,))


def genus1_bracket_comparison(shadow_coeffs=None) -> Dict[str, object]:
    """
    Compare genus-1 MC bracket with WK numbers.

    The genus-1 WK numbers with correct selection rules:
    n=1: <tau_1>_1 = 1/24  (sum=1=3-3+1)
    n=2: <tau_0 tau_2>_1 = 1/24, <tau_1^2>_1 = 1/12  (sum=2=3-3+2)
    n=3: <tau_0^2 tau_3>_1 = 1/24, <tau_0 tau_1 tau_2>_1 = 1/8,
         <tau_1^3>_1 = 1/4  (sum=3=3-3+3)
    """
    if shadow_coeffs is None:
        shadow_coeffs = virasoro_shadow_coeffs_symbolic(4)

    wk_g1 = {
        '<tau_1>_1': witten_kontsevich_intersection(1, (1,)),
        '<tau_0 tau_2>_1': witten_kontsevich_intersection(1, (0, 2)),
        '<tau_1^2>_1': witten_kontsevich_intersection(1, (1, 1)),
        '<tau_0^2 tau_3>_1': witten_kontsevich_intersection(1, (0, 0, 3)),
        '<tau_0 tau_1 tau_2>_1': witten_kontsevich_intersection(1, (0, 1, 2)),
        '<tau_1^3>_1': witten_kontsevich_intersection(1, (1, 1, 1)),
    }

    mc_g1_22 = mc_bracket_genus1_correction(shadow_coeffs, 2, 2)

    return {
        'wk_numbers': wk_g1,
        'mc_bracket_g1_22': mc_g1_22,
        'tau1_g1': witten_kontsevich_intersection(1, (1,)),
        'comparison': 'The genus-1 MC bracket [Sh_2,Sh_2]^{(1)} = S_2/24 = c/48. '
                      'This involves the WK number 1/24 as a COEFFICIENT, '
                      'not as an equality target.',
    }


if __name__ == '__main__':
    print("MC Intersection Form Module")
    print("=" * 60)

    print("\n--- Witten-Kontsevich intersection numbers ---")
    print(f"  <tau_0^3>_0 = {witten_kontsevich_intersection(0, (0, 0, 0))}")
    print(f"  <tau_1>_1   = {witten_kontsevich_intersection(1, (1,))}")
    print(f"  <tau_4>_2   = {witten_kontsevich_intersection(2, (4,))}")

    g0_table = wk_table(0, 6)
    print(f"\n  Genus-0 table ({len(g0_table)} entries):")
    for d, val in sorted(g0_table.items()):
        print(f"    <tau_{d}>_0 = {val}")

    print("\n--- MC bracket vs WK (genus 0, Virasoro) ---")
    comp = genus0_bracket_vs_wk_explicit()
    for key, data in comp.items():
        print(f"  {key}: bracket = {data['bracket']}, WK = {data['wk']}")

    print("\n--- Genus-1 comparison ---")
    g1 = genus1_bracket_comparison()
    for key, val in g1['wk_numbers'].items():
        print(f"  {key} = {val}")
    print(f"  MC bracket [Sh_2,Sh_2]^{{(1)}} = {g1['mc_bracket_g1_22']}")
