"""MC moduli curve: critical locus of the shadow potential.

Implements the MC moduli curve M_A = {dS/dx = 0, x != 0} for the
Virasoro and W_3 shadow potentials. Computes:
- MC solutions as functions of c
- Branch locus (discriminant zeros)
- Hadamard factorization data
- Jensen counting estimates
- Rank-2 critical locus for W_3

The shadow potential S(x; c) = sum_{r=2}^{r_max} S_r(c) x^r / r!
is an entire function of x (for fixed generic c) whose critical
locus {dS/dx = 0, x != 0} parametrizes the nontrivial MC solutions
of the shadow tower.  The reduced critical equation

    P(x; c) := (dS/dx) / x = 0

is polynomial in x (at finite truncation) with rational coefficients
in c.  As c varies, the roots x_k(c) trace out a branched covering
of the c-plane: the MC moduli curve.

Branch points (discriminant zeros) correspond to collision of MC
solutions, i.e., A_k singularity enhancement of the shadow potential.
The Hadamard product formula expresses the reduced derivative as

    (dS/dx) / x = (kappa / 2) prod_k (1 - x / x_k(c))

where kappa = c/2 is the Virasoro curvature and the product runs
over the (max_arity - 2) roots of the reduced equation.

For W_3 the deformation space is 2-dimensional (x_T, x_W) and the
MC locus is the simultaneous zero set of dS/dx_T and dS/dx_W.

Ground truth:
  - thm:nms-mc-moduli-curve-structure
  - thm:nms-hadamard-mc-potential
  - cor:nms-mc-solution-counting
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from sympy import (
    Symbol, Rational, simplify, factor, expand, Poly, diff, cancel,
    N as sympy_N, S, factorial, solve, numer, denom, degree,
    sqrt, log, pi, Abs, re, im, conjugate, oo,
)

from virasoro_shadow_tower import shadow_coefficients, compute_shadow_tower
from shadow_potential_singularity import (
    shadow_potential_1d,
    critical_equation_1d,
    shadow_discriminant_1d,
    critical_points_numerical,
)
from w3_multivariable_shadow import w3_corrected_shadow_tower

c = Symbol('c')
x = Symbol('x')
x_T = Symbol('x_T')
x_W = Symbol('x_W')


# ============================================================================
# 0. Fast numpy root finder for numerical continuation
# ============================================================================

def _reduced_critical_numpy_coeffs(c_val, max_arity=7):
    """Build numpy polynomial coefficients for P(x;c) = (dS/dx)/x at given c.

    Returns coefficients in numpy convention (highest degree first):
    [a_{d}, a_{d-1}, ..., a_1, a_0] where P(x) = sum a_k x^k.
    """
    coeffs = shadow_coefficients(max_arity)
    # dS/dx = sum_{r=2}^{max_arity} S_r x^{r-1} / (r-1)!
    # P(x) = (dS/dx)/x = sum_{r=2}^{max_arity} S_r x^{r-2} / (r-1)!
    # Degree of P = max_arity - 2
    d = max_arity - 2
    np_coeffs = np.zeros(d + 1, dtype=complex)
    for r in sorted(coeffs.keys()):
        k = r - 2  # x^k term in P
        s_r = complex(sympy_N(coeffs[r].subs(c, c_val)))
        from math import factorial as mfact
        np_coeffs[d - k] = s_r / mfact(r - 1)  # numpy: highest first
    return np_coeffs


def _mc_solutions_numpy(c_val, max_arity=7):
    """Fast numpy-based MC solution finder (for numerical continuation)."""
    np_coeffs = _reduced_critical_numpy_coeffs(c_val, max_arity)
    if np.all(np_coeffs == 0):
        return np.array([], dtype=complex)
    # Remove leading zeros
    first_nonzero = 0
    for i in range(len(np_coeffs)):
        if abs(np_coeffs[i]) > 1e-30:
            first_nonzero = i
            break
    np_coeffs = np_coeffs[first_nonzero:]
    if len(np_coeffs) <= 1:
        return np.array([], dtype=complex)
    roots = np.roots(np_coeffs)
    return np.sort(roots, key=lambda z: abs(z)) if len(roots) > 0 else roots


def _mc_solutions_numpy_sorted(c_val, max_arity=7):
    """Fast numpy MC solutions, sorted by absolute value."""
    np_coeffs = _reduced_critical_numpy_coeffs(c_val, max_arity)
    if np.all(np_coeffs == 0):
        return np.array([], dtype=complex)
    first_nonzero = 0
    for i in range(len(np_coeffs)):
        if abs(np_coeffs[i]) > 1e-30:
            first_nonzero = i
            break
    np_coeffs = np_coeffs[first_nonzero:]
    if len(np_coeffs) <= 1:
        return np.array([], dtype=complex)
    roots = np.roots(np_coeffs)
    idx = np.argsort(np.abs(roots))
    return roots[idx]


# ============================================================================
# 1. MC solutions (1d Virasoro)
# ============================================================================

def mc_solutions_1d(c_val, max_arity=7):
    """Compute all MC solutions x_k(c) numerically at given c.

    Returns list of complex numbers (roots of dS/dx = 0 other than x=0).
    These are the nontrivial Maurer-Cartan solutions on the primary line
    for the Virasoro shadow potential truncated at the given arity.

    Parameters
    ----------
    c_val : numeric
        Central charge value.
    max_arity : int
        Maximum arity for shadow tower truncation.

    Returns
    -------
    list of complex
        Roots of the reduced critical equation, sorted by absolute value.
    """
    crit = critical_equation_1d(max_arity)
    crit_spec = crit.subs(c, c_val)
    crit_spec = cancel(crit_spec)

    if crit_spec == S.Zero:
        return []

    if crit_spec.has(oo) or crit_spec.has(-oo) or crit_spec.has(S.ComplexInfinity):
        return []

    roots = solve(crit_spec, x)
    result = [complex(sympy_N(r)) for r in roots]
    result.sort(key=lambda z: abs(z))
    return result


def mc_moduli_curve_1d(c_values, max_arity=7):
    """Trace the MC solutions as c varies over a list of values.

    Returns dict {c: [x_k(c)]} for each c, giving the full branched
    covering structure of the MC moduli curve over the c-plane.

    Parameters
    ----------
    c_values : list of numeric
        Central charge values to sample.
    max_arity : int
        Maximum arity for shadow tower truncation.

    Returns
    -------
    dict
        Maps c_val -> list of complex MC solutions.
    """
    result = {}
    for cv in c_values:
        result[cv] = mc_solutions_1d(cv, max_arity)
    return result


# ============================================================================
# 2. Branch locus (discriminant zeros)
# ============================================================================

def branch_locus_1d(max_arity=7):
    """Compute the branch locus: values of c where MC solutions collide.

    The branch locus is the zero set of the discriminant of the reduced
    critical polynomial P(x; c).  At these c-values, two or more MC
    solutions coincide, producing A_k singularity enhancement.

    Returns the discriminant zeros as a list of complex numbers (sorted
    by real part), together with the factored discriminant expression.

    Parameters
    ----------
    max_arity : int
        Maximum arity for shadow tower truncation.

    Returns
    -------
    dict with keys:
        'zeros': list of complex branch points
        'discriminant': factored discriminant expression
        'numerator_zeros': zeros of the numerator (branch points)
        'denominator_zeros': zeros of the denominator (singularity walls)
    """
    disc = shadow_discriminant_1d(max_arity)

    num = numer(disc)
    den = denom(disc)

    num_zeros_sym = solve(num, c)
    den_zeros_sym = solve(den, c)

    num_zeros = sorted([complex(sympy_N(z)) for z in num_zeros_sym],
                       key=lambda z: (z.real, z.imag))
    den_zeros = sorted([complex(sympy_N(z)) for z in den_zeros_sym],
                       key=lambda z: (z.real, z.imag))

    return {
        'zeros': num_zeros,
        'discriminant': disc,
        'numerator_zeros': num_zeros,
        'denominator_zeros': den_zeros,
    }


# ============================================================================
# 3. Hadamard product verification
# ============================================================================

def hadamard_product_check(c_val, x_val, max_arity=7):
    """Verify the Hadamard product formula.

    The reduced derivative (dS/dx) / x has the factorization

        P(x; c) = (kappa / 2) * prod_k (1 - x / x_k(c))

    where kappa = c/2 is the curvature and x_k(c) are the MC solutions.
    This follows from P being a polynomial of degree (max_arity - 2) with
    known roots and leading term determined by kappa.

    We verify:
        dS/dx(x_val) = x_val * (kappa/2) * prod_k (1 - x_val/x_k(c_val))

    Parameters
    ----------
    c_val : numeric
        Central charge value.
    x_val : complex
        Point at which to evaluate.
    max_arity : int
        Maximum arity for shadow tower truncation.

    Returns
    -------
    tuple of (dS_dx_exact, hadamard_approx, relative_error)
    """
    # Exact value of dS/dx
    pot = shadow_potential_1d(max_arity)
    deriv = diff(pot, x)
    dS_dx_exact = complex(sympy_N(deriv.subs(c, c_val).subs(x, x_val)))

    # Hadamard product
    roots = mc_solutions_1d(c_val, max_arity)
    kappa = c_val / 2.0

    # The reduced equation P(x) = (dS/dx)/x is a polynomial of degree max_arity - 2.
    # Its constant term is kappa (= c/2), the coefficient of x in dS/dx.
    # P(x) = kappa * prod(1 - x/x_k) when the leading coefficient is kappa / prod(-x_k).
    # Actually, P(x) has constant term S''(0)/1! = kappa and degree max_arity - 2.
    # The monic polynomial with roots x_k is prod(x - x_k), so
    # P(x) = kappa/prod(-x_k) * prod(x - x_k) = kappa * prod(1 - x/x_k)   ... NOT QUITE.
    #
    # More carefully: P(x) = a_{max_arity-2} * prod(x - x_k) where
    # a_{max_arity-2} is the leading coefficient.  The constant term is
    # P(0) = a_{max_arity-2} * prod(-x_k) = kappa.
    # So a_{max_arity-2} = kappa / prod(-x_k).
    # Then P(x) = kappa/prod(-x_k) * prod(x - x_k) = kappa * prod(1 - x/x_k).
    # This is correct when all roots are nonzero, which is generic.

    if not roots:
        hadamard_val = kappa * x_val  # P(x)*x with no roots
        return (dS_dx_exact, hadamard_val, float('inf'))

    product = 1.0
    for xk in roots:
        if abs(xk) < 1e-15:
            continue  # skip degenerate roots
        product *= (1.0 - complex(x_val) / xk)

    # dS/dx = x * P(x) = x * kappa * prod(1 - x/x_k)
    hadamard_val = complex(x_val) * kappa * product

    if abs(dS_dx_exact) < 1e-15:
        if abs(hadamard_val) < 1e-15:
            rel_error = 0.0
        else:
            rel_error = abs(hadamard_val)
    else:
        rel_error = abs(dS_dx_exact - hadamard_val) / abs(dS_dx_exact)

    return (dS_dx_exact, hadamard_val, rel_error)


# ============================================================================
# 4. Jensen counting estimate
# ============================================================================

def jensen_count(R, c_val, max_arity=7):
    """Jensen estimate for N(R; c) = number of MC solutions with |x_k| < R.

    Uses the Jensen formula from complex analysis: for a polynomial f(z)
    of degree d with roots z_1, ..., z_d,

        N(R) = #{k : |z_k| < R} <= log|f(0)|/|a_d| R^d / log R

    We use the exact count from the computed roots (at finite truncation)
    and compare with the Jensen bound.

    Parameters
    ----------
    R : float
        Radius in the x-plane.
    c_val : numeric
        Central charge value.
    max_arity : int
        Maximum arity for shadow tower truncation.

    Returns
    -------
    dict with keys:
        'exact_count': exact number of roots inside disk of radius R
        'total_roots': total number of roots
        'jensen_bound': Jensen upper bound estimate
        'roots_inside': list of roots with |x_k| < R
        'roots_outside': list of roots with |x_k| >= R
    """
    roots = mc_solutions_1d(c_val, max_arity)

    inside = [z for z in roots if abs(z) < R]
    outside = [z for z in roots if abs(z) >= R]

    # Jensen bound: for f(z) = P(z) the reduced equation,
    # N(R) <= (1/log R) * log(M(R)/|P(0)|) where M(R) = max_{|z|=R} |P(z)|
    # At finite truncation this is not sharp, but gives a comparison.
    # Use a simpler estimate: N(R) <= deg(P) = max_arity - 2 always.
    # For a tighter bound, use the Jensen formula with the polynomial values.

    # Evaluate P(z) on a circle of radius R to estimate M(R)
    kappa = c_val / 2.0

    # P(0) = kappa
    P_0 = abs(kappa)

    # Use numpy polynomial for fast evaluation on the circle
    np_coeffs = _reduced_critical_numpy_coeffs(c_val, max_arity)
    n_sample = 360
    theta_vals = np.linspace(0, 2 * np.pi, n_sample, endpoint=False)
    z_vals = R * np.exp(1j * theta_vals)
    P_vals = np.polyval(np_coeffs, z_vals)
    max_P = float(np.max(np.abs(P_vals)))

    if P_0 > 0 and R > 1.0 and max_P > P_0:
        jensen_bound = np.log(max_P / P_0) / np.log(R)
    else:
        jensen_bound = max_arity - 2  # trivial bound

    return {
        'exact_count': len(inside),
        'total_roots': len(roots),
        'jensen_bound': jensen_bound,
        'roots_inside': inside,
        'roots_outside': outside,
    }


# ============================================================================
# 5. MC solutions (2d, W_3)
# ============================================================================

def mc_solutions_2d(c_val, max_arity=5):
    """W_3 MC solutions on the 2d deformation space.

    Solves dS/dx_T = 0, dS/dx_W = 0 numerically for the W_3 shadow
    potential.  By W-charge conservation, x_W = 0 is always a factor,
    so the solutions split into:

    (a) T-line solutions: x_W = 0, dS/dx_T = 0  (1d Virasoro problem
        restricted to the T-sector of W_3)
    (b) Off-axis solutions: x_W != 0, genuine rank-2 critical points

    Parameters
    ----------
    c_val : numeric
        Central charge value.
    max_arity : int
        Maximum arity for W_3 shadow tower truncation (default 5 due to
        computational cost of the 2d system).

    Returns
    -------
    list of (x_T, x_W) pairs (complex tuples), sorted by
    |x_T|^2 + |x_W|^2.
    """
    shadows = w3_corrected_shadow_tower(max_arity)

    # Build the 2d shadow potential S = sum Sh_r / r!
    pot_2d = S.Zero
    for r, sh in sorted(shadows.items()):
        pot_2d += sh / factorial(r)
    pot_2d = expand(pot_2d)

    # Critical equations
    dS_dxT = diff(pot_2d, x_T)
    dS_dxW = diff(pot_2d, x_W)

    # Substitute c
    dS_dxT_spec = cancel(dS_dxT.subs(c, c_val))
    dS_dxW_spec = cancel(dS_dxW.subs(c, c_val))

    if dS_dxT_spec == S.Zero and dS_dxW_spec == S.Zero:
        return []

    # Solve the system
    # First, get T-line solutions (x_W = 0)
    t_line_eq = cancel(dS_dxT_spec.subs(x_W, 0))
    t_line_roots = []
    if t_line_eq != S.Zero:
        # Factor out x_T
        t_reduced = cancel(t_line_eq / x_T)
        if t_reduced != S.Zero:
            t_roots_sym = solve(t_reduced, x_T)
            for r in t_roots_sym:
                t_line_roots.append((complex(sympy_N(r)), 0.0 + 0.0j))

    # Off-axis solutions: x_W != 0
    # The W-equation dS/dx_W = 0 with x_W factored gives conditions
    # on x_T for nonzero x_W.
    # dS/dx_W = x_W * G(x_T, x_W) = 0, so either x_W = 0 or G = 0.
    # For G = 0 combined with dS/dx_T = 0: a system in (x_T, x_W^2).

    # Use sympy's solve for the full system
    off_axis_roots = []
    try:
        # dS/dx_W always has x_W as a factor (by W-charge conservation:
        # S only has even powers of x_W)
        dS_dxW_reduced = cancel(dS_dxW_spec / x_W)

        if dS_dxW_reduced != S.Zero:
            # Substitute u = x_W^2 to handle the even-power structure
            u = Symbol('u')
            # In the W_3 tower, x_W appears only in even powers in S,
            # so dS/dx_W has only odd powers of x_W.
            # After dividing by x_W, the result has only even powers of x_W.
            dS_dxW_in_u = dS_dxW_reduced.subs(x_W**2, u).subs(x_W, sqrt(u))
            dS_dxT_in_u = dS_dxT_spec.subs(x_W**2, u).subs(x_W, sqrt(u))

            # Try direct solve
            sols = solve([dS_dxT_spec, dS_dxW_reduced],
                         [x_T, x_W], dict=True)
            for sol in sols:
                xt = complex(sympy_N(sol.get(x_T, 0)))
                xw = complex(sympy_N(sol.get(x_W, 0)))
                if abs(xw) > 1e-12:
                    off_axis_roots.append((xt, xw))
                    # Also include the reflection x_W -> -x_W
                    off_axis_roots.append((xt, -xw))
    except Exception:
        pass

    # Deduplicate
    all_roots = list(t_line_roots)
    for r in off_axis_roots:
        is_dup = False
        for existing in all_roots:
            if abs(r[0] - existing[0]) < 1e-8 and abs(r[1] - existing[1]) < 1e-8:
                is_dup = True
                break
        if not is_dup:
            all_roots.append(r)

    # Sort by norm
    all_roots.sort(key=lambda p: abs(p[0])**2 + abs(p[1])**2)
    return all_roots


# ============================================================================
# 6. Order of the shadow potential (entire-function growth)
# ============================================================================

def order_of_shadow_potential(max_arity=7):
    """Estimate the order rho of the entire function S(x; c).

    For a polynomial of degree d, the order is 0 (finite).  For the
    FULL (un-truncated) shadow potential, the order rho is defined by

        rho = lim sup_{r -> infty} (r log r) / (-log |a_r|)

    where a_r = S_r / r! is the coefficient of x^r in the Taylor series.

    At finite truncation, rho = 0 (polynomial).  This function estimates
    rho from the growth rate of the available coefficients, extrapolating
    to assess whether the full series is entire of finite order.

    Parameters
    ----------
    max_arity : int
        Maximum arity for shadow tower truncation.

    Returns
    -------
    dict with keys:
        'truncated_order': 0 (polynomial at any finite truncation)
        'estimated_order': estimated rho from coefficient growth
        'coefficient_data': list of (r, |a_r(c=1)|) for growth analysis
        'log_log_data': list of (r, r*log(r) / (-log|a_r|)) estimates
    """
    coeffs = shadow_coefficients(max_arity)
    coeff_data = []
    log_log_data = []

    for r in sorted(coeffs.keys()):
        # Evaluate at c = 1 for numerical estimates
        a_r = abs(complex(sympy_N(coeffs[r].subs(c, 1) / factorial(r))))
        coeff_data.append((r, a_r))

        if a_r > 0 and r >= 3:
            log_a = -np.log(a_r)
            if log_a > 0:
                rho_est = r * np.log(r) / log_a
                log_log_data.append((r, rho_est))

    return {
        'truncated_order': 0,  # polynomial at any finite truncation
        'estimated_order': log_log_data[-1][1] if log_log_data else 0,
        'coefficient_data': coeff_data,
        'log_log_data': log_log_data,
    }


# ============================================================================
# 7. Monodromy around branch points
# ============================================================================

def monodromy_around_branch_point(c0, delta=0.01, n_points=100, max_arity=7):
    """Trace MC solutions as c follows a small circle around c0.

    Detect which solutions are exchanged by the monodromy, giving the
    permutation of MC solutions induced by analytic continuation around
    the branch point.

    Parameters
    ----------
    c0 : complex
        Center of the loop (should be near a branch point).
    delta : float
        Radius of the loop.
    n_points : int
        Number of sample points on the loop.
    max_arity : int
        Maximum arity for shadow tower truncation.

    Returns
    -------
    dict with keys:
        'center': c0
        'delta': delta
        'initial_roots': roots at c0 + delta (the starting point)
        'final_roots': roots after traversing the full loop
        'permutation': list mapping initial root index to final root index
        'is_branch_point': True if the monodromy is nontrivial
        'cycle_structure': list of cycle lengths in the permutation
    """
    c0 = complex(c0)
    theta_vals = np.linspace(0, 2 * np.pi, n_points + 1)

    # Track roots along the path using fast numpy solver
    initial_roots_np = _mc_solutions_numpy_sorted(c0 + delta, max_arity)
    if len(initial_roots_np) == 0:
        return {
            'center': c0,
            'delta': delta,
            'initial_roots': [],
            'final_roots': [],
            'permutation': [],
            'is_branch_point': False,
            'cycle_structure': [],
        }

    initial_roots = list(initial_roots_np)
    n_roots = len(initial_roots)

    # Current tracked positions
    current = np.array(initial_roots, dtype=complex)

    for i in range(1, len(theta_vals)):
        c_val = c0 + delta * np.exp(1j * theta_vals[i])
        new_roots_np = _mc_solutions_numpy_sorted(c_val, max_arity)

        if len(new_roots_np) != n_roots:
            continue

        new_arr = new_roots_np

        # Match by nearest neighbor (greedy)
        used = set()
        matched = np.zeros(n_roots, dtype=complex)
        for j in range(n_roots):
            best_k = -1
            best_dist = float('inf')
            for kk in range(n_roots):
                if kk in used:
                    continue
                d = abs(current[j] - new_arr[kk])
                if d < best_dist:
                    best_dist = d
                    best_k = kk
            used.add(best_k)
            matched[j] = new_arr[best_k]
        current = matched

    final_roots = list(current)

    # Determine permutation: match final roots to initial roots
    initial_arr = np.array(initial_roots, dtype=complex)
    permutation = []
    used = set()
    for j in range(n_roots):
        best_k = -1
        best_dist = float('inf')
        for kk in range(n_roots):
            if kk in used:
                continue
            d = abs(current[j] - initial_arr[kk])
            if d < best_dist:
                best_dist = d
                best_k = kk
        used.add(best_k)
        permutation.append(best_k)

    # Compute cycle structure
    visited = [False] * n_roots
    cycles = []
    for j in range(n_roots):
        if visited[j]:
            continue
        cycle_len = 0
        k = j
        while not visited[k]:
            visited[k] = True
            k = permutation[k]
            cycle_len += 1
        cycles.append(cycle_len)
    cycles.sort(reverse=True)

    is_branch = any(cl > 1 for cl in cycles)

    return {
        'center': c0,
        'delta': delta,
        'initial_roots': initial_roots,
        'final_roots': final_roots,
        'permutation': permutation,
        'is_branch_point': is_branch,
        'cycle_structure': cycles,
    }


# ============================================================================
# 8. Auxiliary: reduced critical polynomial data
# ============================================================================

def reduced_critical_degree(max_arity=7):
    """Degree of the reduced critical polynomial P(x; c) = (dS/dx)/x.

    This equals max_arity - 2: the shadow potential has degree max_arity
    in x, so dS/dx has degree max_arity - 1, and dividing by x gives
    degree max_arity - 2.

    Returns
    -------
    int
    """
    return max_arity - 2


def reduced_critical_leading_coefficient(max_arity=7):
    """Leading coefficient of P(x; c) = (dS/dx)/x as a function of c.

    This is the coefficient of x^{max_arity - 2} in the reduced critical
    polynomial, equal to S_{max_arity} / (max_arity - 1)!.
    """
    coeffs = shadow_coefficients(max_arity)
    s_max = coeffs[max_arity]
    return factor(s_max / factorial(max_arity - 1))


def mc_solution_count(c_val, max_arity=7):
    """Number of MC solutions (counting multiplicity) at given c.

    For generic c, this equals max_arity - 2.  At special values of c
    (e.g., the branch locus or c = 0), some roots may coincide or escape
    to infinity.
    """
    roots = mc_solutions_1d(c_val, max_arity)
    return len(roots)


def mc_real_solution_count(c_val, max_arity=7, tol=1e-10):
    """Number of real MC solutions at given c."""
    roots = mc_solutions_1d(c_val, max_arity)
    return sum(1 for z in roots if abs(z.imag) < tol)


# ============================================================================
# 9. Isomonodromic data for the rank-2 conjecture
# ============================================================================

def rank2_discriminant(c_val, max_arity=5):
    """Discriminant locus of the W_3 critical system at given c.

    For the rank-2 system, the discriminant detects when two 2d MC
    solutions collide.  This is the Jacobian determinant of the map
    (x_T, x_W) -> (dS/dx_T, dS/dx_W) evaluated at the critical locus.

    Parameters
    ----------
    c_val : numeric
        Central charge value.
    max_arity : int
        Maximum arity for W_3 shadow tower.

    Returns
    -------
    dict with keys:
        'solutions': list of (x_T, x_W) MC solutions
        'jacobian_det_at_solutions': Jacobian determinant at each solution
        'degenerate_solutions': solutions where Jacobian vanishes
    """
    sols = mc_solutions_2d(c_val, max_arity)

    shadows = w3_corrected_shadow_tower(max_arity)
    pot_2d = S.Zero
    for r, sh in sorted(shadows.items()):
        pot_2d += sh / factorial(r)
    pot_2d = expand(pot_2d)

    # Hessian of S (second-derivative matrix)
    H_TT = diff(pot_2d, x_T, 2)
    H_TW = diff(pot_2d, x_T, x_W)
    H_WW = diff(pot_2d, x_W, 2)

    jac_dets = []
    degenerate = []
    for (xt, xw) in sols:
        htt = complex(sympy_N(H_TT.subs(c, c_val).subs(x_T, xt).subs(x_W, xw)))
        htw = complex(sympy_N(H_TW.subs(c, c_val).subs(x_T, xt).subs(x_W, xw)))
        hww = complex(sympy_N(H_WW.subs(c, c_val).subs(x_T, xt).subs(x_W, xw)))
        det_val = htt * hww - htw**2
        jac_dets.append(det_val)
        if abs(det_val) < 1e-8:
            degenerate.append((xt, xw))

    return {
        'solutions': sols,
        'jacobian_det_at_solutions': jac_dets,
        'degenerate_solutions': degenerate,
    }


def rank2_t_line_comparison(c_val, max_arity=5):
    """Compare T-line MC solutions in the rank-2 (W_3) and rank-1 (Vir) settings.

    On the T-line (x_W = 0), the W_3 shadow potential restricts to a
    1d potential that should agree with the Virasoro potential through
    the Coxeter anomaly analysis.

    Returns
    -------
    dict comparing the two sets of solutions.
    """
    sols_2d = mc_solutions_2d(c_val, max_arity)
    t_line_2d = [(xt, xw) for (xt, xw) in sols_2d if abs(xw) < 1e-10]
    t_vals_2d = sorted([xt for (xt, _) in t_line_2d], key=lambda z: abs(z))

    sols_1d = mc_solutions_1d(c_val, max_arity)

    return {
        'w3_t_line_solutions': t_vals_2d,
        'vir_solutions': sols_1d,
        'count_w3': len(t_vals_2d),
        'count_vir': len(sols_1d),
    }


# ============================================================================
# 10. Summary statistics
# ============================================================================

def mc_moduli_summary(c_val, max_arity=7):
    """Summary of the MC moduli curve at given c.

    Returns a dict with solution count, real/complex decomposition,
    minimum and maximum modulus, and the Hadamard error.
    """
    roots = mc_solutions_1d(c_val, max_arity)
    if not roots:
        return {
            'c': c_val,
            'max_arity': max_arity,
            'n_solutions': 0,
            'n_real': 0,
            'n_complex_pairs': 0,
            'min_modulus': None,
            'max_modulus': None,
        }

    real_roots = [z for z in roots if abs(z.imag) < 1e-10]
    complex_roots = [z for z in roots if abs(z.imag) >= 1e-10]
    n_complex_pairs = len(complex_roots) // 2

    moduli = [abs(z) for z in roots]

    # Hadamard check at a test point
    test_x = 0.1 + 0.1j
    _, _, had_err = hadamard_product_check(c_val, test_x, max_arity)

    return {
        'c': c_val,
        'max_arity': max_arity,
        'n_solutions': len(roots),
        'n_real': len(real_roots),
        'n_complex_pairs': n_complex_pairs,
        'min_modulus': min(moduli),
        'max_modulus': max(moduli),
        'hadamard_error': had_err,
        'roots': roots,
    }


# ============================================================================
# __main__: demonstration
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("MC MODULI CURVE — CRITICAL LOCUS OF THE SHADOW POTENTIAL")
    print("=" * 70)

    # -----------------------------------------------------------------
    # 1. MC solutions at c = 1 and c = 13
    # -----------------------------------------------------------------
    print("\n--- 1. MC solutions at c = 1 and c = 13 ---")
    for cv in [1, 13]:
        roots = mc_solutions_1d(cv, max_arity=7)
        real_count = sum(1 for z in roots if abs(z.imag) < 1e-10)
        print(f"\n  c = {cv}: {len(roots)} MC solutions "
              f"({real_count} real, {(len(roots) - real_count) // 2} complex pairs)")
        for i, z in enumerate(roots):
            tag = "(real)" if abs(z.imag) < 1e-10 else "(complex)"
            print(f"    x_{i} = {z:.8f}  {tag}  |x| = {abs(z):.8f}")

    # -----------------------------------------------------------------
    # 2. Hadamard product verification at c = 1
    # -----------------------------------------------------------------
    print("\n--- 2. Hadamard product verification at c = 1 ---")
    test_points = [0.1, 0.5, 1.0, 0.3 + 0.2j]
    for xv in test_points:
        exact, approx, err = hadamard_product_check(1, xv, max_arity=7)
        print(f"  x = {xv}:")
        print(f"    dS/dx (exact)    = {exact:.10f}")
        print(f"    dS/dx (Hadamard) = {approx:.10f}")
        print(f"    relative error   = {err:.2e}")

    # -----------------------------------------------------------------
    # 3. Branch locus at arity 7
    # -----------------------------------------------------------------
    print("\n--- 3. Branch locus at arity 7 ---")
    bl = branch_locus_1d(max_arity=7)
    print(f"  Number of branch points: {len(bl['numerator_zeros'])}")
    for i, z in enumerate(bl['numerator_zeros']):
        tag = "(real)" if abs(z.imag) < 1e-10 else "(complex)"
        print(f"    c_{i} = {z:.8f}  {tag}")
    print(f"  Singularity walls (discriminant poles):")
    for z in bl['denominator_zeros']:
        print(f"    c = {z:.8f}")

    # -----------------------------------------------------------------
    # 4. Monodromy around the first branch point
    # -----------------------------------------------------------------
    print("\n--- 4. Monodromy around the first branch point ---")
    real_branch = [z for z in bl['numerator_zeros'] if abs(z.imag) < 1e-10]
    if real_branch:
        bp = real_branch[0].real
        print(f"  Branch point c0 = {bp:.8f}")
        mono = monodromy_around_branch_point(bp, delta=0.05,
                                             n_points=200, max_arity=7)
        print(f"  Permutation: {mono['permutation']}")
        print(f"  Cycle structure: {mono['cycle_structure']}")
        print(f"  Is branch point: {mono['is_branch_point']}")
    else:
        print("  No real branch points found; using first complex one")
        if bl['numerator_zeros']:
            bp = bl['numerator_zeros'][0]
            print(f"  Branch point c0 = {bp}")
            mono = monodromy_around_branch_point(bp, delta=0.05,
                                                 n_points=200, max_arity=7)
            print(f"  Permutation: {mono['permutation']}")
            print(f"  Cycle structure: {mono['cycle_structure']}")
            print(f"  Is branch point: {mono['is_branch_point']}")

    # -----------------------------------------------------------------
    # 5. Jensen counting estimate
    # -----------------------------------------------------------------
    print("\n--- 5. Jensen counting estimate ---")
    for R in [1.0, 5.0, 10.0, 50.0]:
        jc = jensen_count(R, 1, max_arity=7)
        print(f"  R = {R:5.1f}: N(R) = {jc['exact_count']}/{jc['total_roots']} "
              f"(Jensen bound: {jc['jensen_bound']:.2f})")

    # -----------------------------------------------------------------
    # 6. Order estimate
    # -----------------------------------------------------------------
    print("\n--- 6. Order of shadow potential ---")
    order_data = order_of_shadow_potential(max_arity=7)
    print(f"  Truncated order: {order_data['truncated_order']}")
    print(f"  Estimated order from coefficients: {order_data['estimated_order']:.4f}")
    print(f"  Coefficient data (r, |a_r| at c=1):")
    for r, a in order_data['coefficient_data']:
        print(f"    r = {r}: |a_r| = {a:.6e}")

    # -----------------------------------------------------------------
    # 7. MC moduli summary
    # -----------------------------------------------------------------
    print("\n--- 7. MC moduli summary ---")
    for cv in [1, 13, 26]:
        s = mc_moduli_summary(cv, max_arity=7)
        print(f"  c = {cv}: {s['n_solutions']} solutions "
              f"({s['n_real']} real), "
              f"|x| in [{s.get('min_modulus', 'N/A'):.4f}, "
              f"{s.get('max_modulus', 'N/A'):.4f}], "
              f"Hadamard err = {s.get('hadamard_error', 'N/A'):.2e}")
