#!/usr/bin/env python3
r"""MC spectral rigidity: can the Maurer-Cartan equation constrain zero positions?

This module investigates the deepest open question in the arithmetic programme:
whether the MC equation D^2 = 0 and its shadow tower constraints can force
the Ramanujan bound |alpha_p| = p^{(k-1)/2} on Satake parameters.

THEORETICAL ANALYSIS:

1. NEWTON IDENTITY REDUNDANCY.
   For a Hecke eigenform f of weight k with Satake parameters (alpha_p, beta_p)
   at prime p, the shadow-symmetric power identification gives:
     S_r ~ p_{r-1}(alpha_p, beta_p) = alpha_p^{r-1} + beta_p^{r-1}
   (up to normalization, Proposition prop:shadow-symmetric-power).

   Newton's identities:
     p_r = e_1 * p_{r-1} - e_2 * p_{r-2}
   with e_1 = alpha + beta = a_f(p), e_2 = alpha * beta = p^{k-1}.

   KEY FACT: For TWO variables, all Newton identities at r >= 3 are REDUNDANT.
   Given p_1 = e_1 and e_2, the recursion p_r = e_1 * p_{r-1} - e_2 * p_{r-2}
   determines ALL higher power sums uniquely. The MC equation at arities >= 5
   gives the SAME recursion as Newton at arities 3, 4, ...

   Therefore: at a single prime p, the MC equation provides NO additional
   constraint beyond specifying (e_1, e_2) = (a_f(p), p^{k-1}).
   The Ramanujan bound |a_f(p)| <= 2*p^{(k-1)/2} is NOT forced by Newton.

2. QUARTIC CONSTRAINT.
   Q^contact_Vir = 10/[c(5c+22)] is a SPECIFIC value. But this is a constraint
   on the SHADOW TOWER of the Virasoro algebra, not directly on Hecke eigenvalues.
   The quartic shadow constrains the fourth moment of the spectral measure rho:
     S_4 = -(1/4) sum c_j lambda_j^4
   For a two-atom measure (alpha, beta):
     S_4 = -(1/4)(alpha^4 + beta^4)
   This is determined by S_2 and S_3 via Newton: p_4 = e_1*p_3 - e_2*p_2.
   So the quartic constraint is AUTOMATIC once (e_1, e_2) are fixed. No new info.

3. GENUS-1 CORRECTIONS.
   At genus 1, the MC equation includes planted-forest corrections:
     S_r^{(g=1)} = S_r^{(g=0)} + kappa * delta_pf^{(1,r)}
   The genus-1 correction involves F_1 = kappa/24 (the first Faber-Pandharipande
   number). This modifies the SEED data (S_2 at genus 1), but does NOT add new
   independent constraints on (alpha_p, beta_p) at a single prime.

   The new information from genus 1 is the MODULARITY of the generating function
   G_rho(tau) = sum c_j log(1 - lambda_j t(q)), which forces the atoms {lambda_j}
   to be Hecke eigenvalues. This is a GLOBAL constraint (all primes simultaneously),
   not a prime-by-prime constraint.

4. THE BOOTSTRAP.
   Different VOAs at different central charges c produce different spectral
   measures rho_c. The Hecke eigenforms f appearing in the spectral decomposition
   are c-INDEPENDENT (they are intrinsic to the L-function, not the VOA).
   But different VOAs may have DIFFERENT eigenforms contributing.

   The bootstrap observation: intersecting the constraint loci from many VOAs
   shrinks the allowed region for Satake parameters. The quartic closure
   conjecture (conj:quartic-closure) asserts that:
     intersect_{c,u_0} L_{c,u_0}^Vir = {rho : Re(rho) = 1/2}
   This would force the critical-line condition from the MC data alone.

   HONEST ASSESSMENT: The bootstrap is the ONE route where MC might constrain
   beyond Newton. But it requires GLOBAL data (all c simultaneously), not
   local data (one VOA at a time). And even the bootstrap gives the critical
   strip as a constraint region, not the exact Ramanujan bound.

5. THE STRUCTURAL GAPS.
   Four gaps (A-D in the manuscript) identify where MC falls short:
   - Gap A: MC -> Li positivity is blocked (sign failure)
   - Gap B: Narain triviality (free-field leverage absent)
   - Gap C: Bar-cobar is homotopical, not spectral-positive
   - Gap D: Nyman-Beurling norm mismatch

   The root cause (rem:beilinson-four-gaps): the MC equation is an
   INTEGRABILITY constraint (D^2 = 0, flatness), while Ramanujan requires
   POSITIVITY (absolute value bounds). These are logically independent.

References:
    prop:mc-bracket-determines-atoms (arithmetic_shadows.tex)
    prop:shadow-symmetric-power (arithmetic_shadows.tex)
    conj:modular-spectral-rigidity (arithmetic_shadows.tex)
    conj:quartic-closure (arithmetic_shadows.tex)
    rem:mc-rigidity-diagnosis (arithmetic_shadows.tex)
    rem:positivity-limitation (arithmetic_shadows.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =========================================================================
# 1. Newton identity redundancy analysis
# =========================================================================

def newton_two_variable_recursion(
    e1, e2, r_max: int, use_mpmath: bool = True
):
    """Compute power sums p_1, ..., p_{r_max} for two variables with
    elementary symmetric polynomials e1 = alpha + beta, e2 = alpha * beta.

    Uses Newton's recursion: p_r = e1 * p_{r-1} - e2 * p_{r-2}
    with p_0 = 2, p_1 = e1.

    For two variables, this recursion is EXACT and determines all p_r
    from (e1, e2) alone. Higher Newton identities are REDUNDANT.

    Parameters
    ----------
    e1 : the sum alpha + beta = a_f(p)
    e2 : the product alpha * beta = p^{k-1}
    r_max : compute through p_{r_max}
    use_mpmath : if True and mpmath available, use high-precision arithmetic

    Returns
    -------
    List [p_1, p_2, ..., p_{r_max}] (1-indexed in math, 0-indexed in list).
    """
    if r_max < 1:
        return []

    # Use mpmath for high precision to avoid floating-point drift
    if use_mpmath and HAS_MPMATH:
        e1_mp = mpmath.mpc(e1)
        e2_mp = mpmath.mpc(e2)
        p = [None] * r_max
        p[0] = e1_mp
        if r_max >= 2:
            p[1] = e1_mp * e1_mp - 2 * e2_mp
        for r in range(3, r_max + 1):
            p[r - 1] = e1_mp * p[r - 2] - e2_mp * p[r - 3]
        return p

    p = [None] * r_max
    p[0] = e1  # p_1 = e_1

    if r_max >= 2:
        p[1] = e1 * e1 - 2 * e2  # p_2 = e_1^2 - 2*e_2

    for r in range(3, r_max + 1):
        p[r - 1] = e1 * p[r - 2] - e2 * p[r - 3]

    return p


def newton_redundancy_test(
    e1: complex, e2: complex, r_max: int = 20
) -> Dict[str, Any]:
    """Verify that all Newton identities at r >= 3 are redundant for two variables.

    Given (e1, e2), compute p_r via the recursion and independently via
    alpha^r + beta^r. Check that Newton's identity
      p_r - e1*p_{r-1} + e2*p_{r-2} = 0
    holds at every level r >= 3 (it must, by construction).

    The point: the MC equation at arity r+1 gives p_r = e1*p_{r-1} - e2*p_{r-2},
    which is THE SAME as Newton. So MC provides NO additional constraint.

    Returns
    -------
    Dict with redundancy analysis.
    """
    # Compute power sums from recursion
    p_rec = newton_two_variable_recursion(e1, e2, r_max)

    # Compute Satake parameters
    disc = e1 * e1 - 4 * e2
    if HAS_MPMATH:
        sqrt_disc = mpmath.sqrt(mpmath.mpc(disc))
        alpha = (mpmath.mpc(e1) + sqrt_disc) / 2
        beta = (mpmath.mpc(e1) - sqrt_disc) / 2
    else:
        import cmath
        sqrt_disc = cmath.sqrt(disc)
        alpha = (e1 + sqrt_disc) / 2
        beta = (e1 - sqrt_disc) / 2

    # Compute power sums directly
    p_direct = []
    for r in range(1, r_max + 1):
        if HAS_MPMATH:
            pr = mpmath.power(alpha, r) + mpmath.power(beta, r)
        else:
            pr = alpha ** r + beta ** r
        p_direct.append(pr)

    # Use mpmath versions of e1, e2 for residual computation
    if HAS_MPMATH:
        e1_mp = mpmath.mpc(e1)
        e2_mp = mpmath.mpc(e2)
    else:
        e1_mp = e1
        e2_mp = e2

    # Check Newton identity residuals (use RELATIVE tolerance for large values)
    newton_residuals = []
    newton_relative = []
    for r in range(3, r_max + 1):
        # p_r - e1*p_{r-1} + e2*p_{r-2} should be 0
        residual = p_rec[r - 1] - e1_mp * p_rec[r - 2] + e2_mp * p_rec[r - 3]
        abs_res = float(abs(residual))
        newton_residuals.append(abs_res)
        scale = max(float(abs(p_rec[r - 1])), 1.0)
        newton_relative.append(abs_res / scale)

    # Check direct vs recursion agreement (relative)
    agreement_residuals = []
    agreement_relative = []
    for r in range(1, r_max + 1):
        abs_res = float(abs(p_rec[r - 1] - p_direct[r - 1]))
        agreement_residuals.append(abs_res)
        scale = max(float(abs(p_rec[r - 1])), 1.0)
        agreement_relative.append(abs_res / scale)

    max_newton_residual = max(newton_residuals) if newton_residuals else 0.0
    max_newton_relative = max(newton_relative) if newton_relative else 0.0
    max_agreement_residual = max(agreement_residuals) if agreement_residuals else 0.0
    max_agreement_relative = max(agreement_relative) if agreement_relative else 0.0

    tol = 1e-20 if HAS_MPMATH else 1e-8

    return {
        'e1': e1,
        'e2': e2,
        'alpha': alpha,
        'beta': beta,
        'discriminant': disc,
        'r_max': r_max,
        'p_recursion': p_rec,
        'p_direct': p_direct,
        'newton_residuals': newton_residuals,
        'max_newton_residual': float(max_newton_residual),
        'max_newton_relative': float(max_newton_relative),
        'agreement_residuals': agreement_residuals,
        'max_agreement_residual': float(max_agreement_residual),
        'max_agreement_relative': float(max_agreement_relative),
        'all_newton_hold': max_newton_relative < tol,
        'all_agree': max_agreement_relative < tol,
        'conclusion': (
            'All Newton identities at r >= 3 are REDUNDANT for two variables. '
            'The recursion p_r = e1*p_{r-1} - e2*p_{r-2} determines all p_r '
            'from (e1, e2) alone. MC at arities >= 5 provides no additional '
            'constraint beyond Newton at arities 3-4.'
        ),
    }


def mc_constraint_count(n_atoms: int, r_max: int) -> Dict[str, Any]:
    """Count MC constraints vs parameters at each arity level.

    For n_atoms spectral atoms, we have 2*n_atoms parameters (atoms + weights).
    The MC equation at arity r+1 gives one polynomial constraint.
    Arities 2, ..., r give (r-1) constraints.

    For 2 variables (Satake type):
      Parameters: 2 (e1 = alpha + beta, e2 = alpha * beta, but e2 = p^{k-1} is known)
      So effectively: 1 unknown (e1 = a_f(p)).
      Constraints from arities 2, ..., r: (r-1), but ALL redundant beyond arity 3.
      EFFECTIVE constraint count: 1 (from arity 2: kappa = c/2 relates to p_2).
      The system is NOT overdetermined at a single prime.

    For m atoms (lattice VOA):
      Parameters: 2m (m atoms + m weights, minus constraints from known e2_j).
      Constraints: (r-1) from arities 2, ..., r.
      Overdetermined when r - 1 > 2m, i.e., r > 2m + 1.

    Returns
    -------
    Dict with constraint analysis.
    """
    results = {
        'n_atoms': n_atoms,
        'r_max': r_max,
        'total_parameters': 2 * n_atoms,
        'constraints_by_arity': {},
        'rigidity_defect_by_arity': {},
    }

    for r in range(2, r_max + 1):
        n_constraints = r - 1
        defect = n_constraints - 2 * n_atoms
        results['constraints_by_arity'][r] = n_constraints
        results['rigidity_defect_by_arity'][r] = defect

    # For two variables (Satake): effective analysis
    if n_atoms == 1:
        results['satake_analysis'] = {
            'effective_unknowns': 1,  # e1 = a_f(p); e2 = p^{k-1} is fixed
            'effective_constraints': 1,  # p_2 = e_1^2 - 2*e_2
            'higher_arity_redundancy': True,
            'conclusion': (
                'For a single Hecke eigenform at a single prime, the MC equation '
                'provides ONE constraint (kappa = c/2 determines p_2). All higher '
                'arity constraints are REDUNDANT (Newton). The system has exactly '
                '1 unknown and 1 equation: no overdetermination, no new information.'
            ),
        }
    elif n_atoms == 2:
        results['two_atom_analysis'] = {
            'effective_unknowns': 4,  # 2 atoms + 2 weights
            'rigidity_arity': 2 * n_atoms + 2,  # arity at which overdetermined
            'conclusion': (
                f'For 2 atoms (e.g., Leech lattice), the system becomes '
                f'overdetermined at arity r = {2 * n_atoms + 2}. '
                f'The rigidity defect delta(2, r) = r - 5.'
            ),
        }

    return results


# =========================================================================
# 2. Quartic constraint analysis for Virasoro
# =========================================================================

def virasoro_quartic_contact(c_val: float) -> float:
    """Compute Q^contact_Vir = 10/[c(5c+22)].

    This is the arity-4 shadow coefficient for the Virasoro algebra.
    It is UNIQUELY DETERMINED by the MC equation from S_2 = c/2 and S_3 = 2.
    """
    if abs(c_val) < 1e-30 or abs(5 * c_val + 22) < 1e-30:
        return float('inf')
    return 10.0 / (c_val * (5 * c_val + 22))


def quartic_constraint_on_satake(
    a_p: float, k: int, p: int
) -> Dict[str, Any]:
    """Analyze what the quartic MC constraint says about Satake parameters.

    The quartic shadow S_4 = -(1/4)(alpha^4 + beta^4) via the spectral
    identification. Newton gives:
      p_4 = alpha^4 + beta^4 = e1*p_3 - e2*p_2
           = (alpha+beta)(alpha^3+beta^3) - alpha*beta*(alpha^2+beta^2)

    So p_4 is DETERMINED by (e1, e2). The quartic MC constraint
    Q^contact = 10/[c(5c+22)] is a constraint on the ALGEBRA's shadow,
    not directly on Satake parameters. It constrains the relationship
    between central charge c and the shadow moments.

    For a lattice VOA, the shadows ARE the moments of the spectral measure,
    so Q^contact constrains combinations of Hecke eigenvalues. But for a
    single eigenform, p_4 = e1*p_3 - e2*p_2 is automatic.

    Returns
    -------
    Dict showing that the quartic constraint is automatic at a single prime.
    """
    e1 = a_p  # alpha + beta
    e2 = p ** (k - 1)  # alpha * beta

    # Use mpmath for precision
    if HAS_MPMATH:
        e1_mp = mpmath.mpc(a_p)
        e2_mp = mpmath.mpc(p ** (k - 1))
    else:
        e1_mp = e1
        e2_mp = e2

    # Power sums
    p1 = e1_mp
    p2 = e1_mp ** 2 - 2 * e2_mp
    p3 = e1_mp ** 3 - 3 * e1_mp * e2_mp
    p4_newton = e1_mp * p3 - e2_mp * p2

    # Direct computation
    disc = e1_mp ** 2 - 4 * e2_mp
    if HAS_MPMATH:
        sqrt_d = mpmath.sqrt(disc)
        alpha = (e1_mp + sqrt_d) / 2
        beta = (e1_mp - sqrt_d) / 2
        p4_direct = mpmath.power(alpha, 4) + mpmath.power(beta, 4)
    else:
        import cmath
        sqrt_d = cmath.sqrt(disc)
        alpha = (e1 + sqrt_d) / 2
        beta = (e1 - sqrt_d) / 2
        p4_direct = alpha ** 4 + beta ** 4

    abs_residual = float(abs(p4_newton - p4_direct))
    scale = max(float(abs(p4_newton)), 1.0)
    residual = abs_residual / scale

    # Ramanujan check
    ramanujan_bound = 2 * p ** ((k - 1) / 2)
    satisfies_ramanujan = abs(a_p) <= ramanujan_bound + 1e-10

    # Alpha^4 + beta^4 in terms of the angle theta (if Ramanujan holds)
    # alpha = p^{(k-1)/2} * e^{i*theta}, beta = conjugate
    # Then p_4 = 2 * p^{2(k-1)} * cos(4*theta)
    if satisfies_ramanujan and e2 > 0:
        cos_theta = a_p / (2 * math.sqrt(e2))
        if abs(cos_theta) <= 1:
            theta = math.acos(cos_theta)
            p4_angular = 2 * e2 ** 2 * math.cos(4 * theta)
        else:
            theta = None
            p4_angular = None
    else:
        theta = None
        p4_angular = None

    return {
        'a_p': a_p,
        'k': k,
        'p': p,
        'e1': e1,
        'e2': e2,
        'p1': p1,
        'p2': p2,
        'p3': p3,
        'p4_newton': p4_newton,
        'p4_direct': complex(p4_direct) if not isinstance(p4_direct, (int, float)) else p4_direct,
        'residual': float(abs_residual),
        'relative_residual': float(residual),
        'automatic': residual < (1e-20 if HAS_MPMATH else 1e-8),
        'satisfies_ramanujan': satisfies_ramanujan,
        'theta': theta,
        'p4_angular': p4_angular,
        'conclusion': (
            'The quartic constraint p_4 = e1*p_3 - e2*p_2 is AUTOMATIC '
            'from Newton\'s identity for two variables. The MC equation '
            'at arity 5 provides the SAME constraint. No additional info '
            'about |alpha_p| vs p^{(k-1)/2} is obtained.'
        ),
    }


# =========================================================================
# 3. Ramanujan tau function tests
# =========================================================================

@lru_cache(maxsize=1024)
def ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: coefficients of Delta = q * prod(1-q^m)^{24}.

    tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472, tau(5)=4830.
    """
    if n < 1:
        return 0
    N = n
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    for m in range(1, N + 1):
        for _ in range(24):
            for i in range(N, m - 1, -1):
                coeffs[i] -= coeffs[i - m]
    return coeffs[n - 1] if n - 1 <= N else 0


def ramanujan_tau_mc_test(prime_bound: int = 30, r_max: int = 12) -> Dict[str, Any]:
    """Test whether MC constraints at arities 2-r_max are automatically
    satisfied for the Ramanujan tau function once tau(p) is given.

    For Delta = sum tau(n) q^n (weight k=12), at each prime p:
      e1 = tau(p), e2 = p^11
    The MC recursion gives p_r = e1*p_{r-1} - e2*p_{r-2}.

    PREDICTION: all MC constraints are automatically satisfied, because
    Newton's identities for two variables are complete. The MC equation
    gives NO EXTRA constraint beyond tau(p) and p^11.

    Returns
    -------
    Dict with per-prime analysis.
    """
    primes = _primes_up_to(prime_bound)
    results = {
        'weight': 12,
        'primes_tested': primes,
        'r_max': r_max,
        'per_prime': {},
        'all_automatic': True,
    }

    for p in primes:
        tau_p = ramanujan_tau(p)
        e1 = tau_p
        e2 = p ** 11

        # Compute power sums via Newton recursion
        p_rec = newton_two_variable_recursion(e1, e2, r_max)

        # Verify against direct computation from Satake parameters
        disc = e1 ** 2 - 4 * e2
        if HAS_MPMATH:
            sqrt_d = mpmath.sqrt(mpmath.mpc(disc))
            alpha = (mpmath.mpc(e1) + sqrt_d) / 2
            beta = (mpmath.mpc(e1) - sqrt_d) / 2
            p_direct = [
                mpmath.power(alpha, r) + mpmath.power(beta, r)
                for r in range(1, r_max + 1)
            ]
        else:
            import cmath
            sqrt_d = cmath.sqrt(disc)
            alpha = (e1 + sqrt_d) / 2
            beta = (e1 - sqrt_d) / 2
            p_direct = [alpha ** r + beta ** r for r in range(1, r_max + 1)]

        # Check agreement (relative tolerance for large values)
        max_residual = 0.0
        max_relative = 0.0
        for r in range(1, r_max + 1):
            abs_res = float(abs(p_rec[r - 1] - p_direct[r - 1]))
            scale = max(float(abs(p_rec[r - 1])), 1.0)
            rel_res = abs_res / scale
            if abs_res > max_residual:
                max_residual = abs_res
            if rel_res > max_relative:
                max_relative = rel_res

        # Check Ramanujan bound
        ramanujan_bound = 2 * p ** (11 / 2)
        satisfies = abs(tau_p) <= ramanujan_bound + 1e-10

        tol = 1e-20 if HAS_MPMATH else 1e-6
        all_auto = max_relative < tol
        if not all_auto:
            results['all_automatic'] = False

        results['per_prime'][p] = {
            'tau_p': tau_p,
            'e1': e1,
            'e2': e2,
            'discriminant': disc,
            'ramanujan_bound': ramanujan_bound,
            'satisfies_ramanujan': satisfies,
            'max_residual_across_arities': max_residual,
            'all_newton_automatic': all_auto,
        }

    results['conclusion'] = (
        'ALL MC constraints at arities 2 through ' + str(r_max) + ' are automatically '
        'satisfied for the Ramanujan tau function. The MC equation provides '
        'NO additional constraint beyond tau(p) existing and satisfying '
        'multiplicativity (tau(mn) = tau(m)*tau(n) for (m,n)=1 and '
        'tau(p^(a+1)) = tau(p)*tau(p^a) - p^11*tau(p^(a-1))).'
    )

    return results


# =========================================================================
# 4. Genus-1 correction analysis
# =========================================================================

def genus1_correction_analysis(c_val: float, r_max: int = 8) -> Dict[str, Any]:
    """Analyze the genus-1 correction to the shadow tower.

    At genus 0, the shadow tower is computed from the OPE data alone.
    At genus 1, the MC equation includes corrections from the genus-1
    surface (the elliptic curve E_tau):
      S_r^{(g=1)} = S_r^{(g=0)} + planted-forest corrections
    The leading genus-1 contribution is F_1 = kappa/24.

    The genus-1 MODULARITY is the genuinely new information:
    G_rho(tau) = sum c_j log(1 - lambda_j t(q)) being modular of weight 0
    forces the atoms {lambda_j} to be Hecke eigenvalues.

    This is a GLOBAL constraint (relating different primes through the
    modular group action), not a prime-by-prime constraint.

    Returns
    -------
    Dict with genus-1 analysis.
    """
    kappa = c_val / 2
    F1 = kappa / 24

    # Shadow tower at genus 0 (on the single-generator line)
    S = {}
    S[2] = kappa
    S[3] = 2.0
    if abs(c_val) > 1e-30 and abs(5 * c_val + 22) > 1e-30:
        S[4] = 10.0 / (c_val * (5 * c_val + 22))
    else:
        S[4] = float('inf')

    # Propagator
    P = 2.0 / c_val if abs(c_val) > 1e-30 else float('inf')

    # Recursive computation of higher arities at genus 0
    # The MC recursion on the single-generator line:
    #   nabla_H(S_r) + o^(r) = 0
    #   where nabla_H(S_r x^r) = 2*r*S_r and the obstruction o^(r) comes
    #   from the H-Poisson bracket of lower shadows.
    #   The bracket {S_j x^j, S_k x^k}_H = j*k*S_j*S_k*(2/c)*x^{j+k-2}.
    #   Obstruction at arity r: sum over j+k = r+2, j>=2, k>=2 (j<=k for symmetry).
    #   Then S_r = -o^(r) / (2*r).
    for r in range(5, r_max + 1):
        T_r = 0.0
        # j+k = r+2, j >= 2, k >= 2, both j,k < r (must use only previously computed)
        for j in range(2, r + 1):
            k = r + 2 - j
            if k < 2:
                continue
            if k >= r:
                continue  # k must be a previously computed arity (< r)
            if j > k:
                continue  # avoid double counting
            if j not in S or k not in S:
                continue
            bracket = j * k * S[j] * S[k] * P
            if j == k:
                bracket /= 2
            T_r += bracket
        if abs(c_val) > 1e-30:
            S[r] = -T_r / (2 * r)
        else:
            S[r] = float('inf')

    # The genus-1 correction delta_{pf}^{(1,r)} at arity r
    # The leading correction to S_2 at genus 1 is:
    #   delta_{pf}^{(1,0)} = genus-1 planted-forest correction at arity 0
    # At arity 2, the genus-1 correction modifies kappa:
    #   kappa^{(1)} = kappa + F_1 * (correction)
    # The exact form requires M_{1,r} intersection theory.

    # What genus 1 provides that genus 0 does not:
    genus1_new_info = {
        'modularity': (
            'The generating function G_rho(tau) = sum c_j log(1 - lambda_j t(q)) '
            'is modular of weight 0 for SL(2,Z). This GLOBAL constraint forces '
            'the atoms {lambda_j} to be Hecke eigenvalues of cusp forms. '
            'This is NOT a prime-by-prime constraint; it relates all primes '
            'through the modular group action.'
        ),
        'hecke_eigenvalue_constraint': (
            'Modularity -> Hecke invariance of atoms -> atoms are Hecke eigenvalues. '
            'This is PROVED (Proposition prop:modularity-constraint). '
            'It tells us WHICH eigenforms contribute, not their eigenvalues.'
        ),
        'petersson_orthogonality': (
            'The weights c_j satisfy Petersson orthogonality, which constrains '
            'the linear combinations of eigenforms that appear.'
        ),
        'does_NOT_constrain': (
            'The genus-1 data does NOT constrain the absolute values |alpha_p|. '
            'Knowing that atoms are Hecke eigenvalues (from modularity) plus '
            'knowing p_r = e1*p_{r-1} - e2*p_{r-2} (from Newton) does not '
            'determine whether |alpha_p| = p^{(k-1)/2} or not.'
        ),
    }

    return {
        'c': c_val,
        'kappa': kappa,
        'F1': F1,
        'shadow_tower_g0': S,
        'genus1_new_information': genus1_new_info,
        'conclusion': (
            'Genus-1 corrections provide MODULARITY (a global constraint), '
            'not prime-by-prime eigenvalue bounds. Modularity forces atoms '
            'to be Hecke eigenvalues but does not force |alpha_p| = p^{(k-1)/2}.'
        ),
    }


# =========================================================================
# 5. Bootstrap system analysis
# =========================================================================

def bootstrap_constraint_locus(
    c_values: Sequence[float],
    a_p: float,
    k: int,
    p: int,
) -> Dict[str, Any]:
    """Analyze the bootstrap: using multiple central charges simultaneously.

    At each c, the Virasoro MC equation determines a shadow tower {S_r(c)}.
    The shadow-symmetric power identification gives constraints on Satake
    parameters at each prime. Different c values give DIFFERENT constraints
    because S_r depends on c through the recursion.

    BUT: for a single eigenform at a single prime, Newton's redundancy
    means each c gives the SAME constraint (e1 = a_f(p), e2 = p^{k-1}).
    The bootstrap adds no new information at a single prime.

    Where the bootstrap IS useful: it constrains the SPECTRAL MEASURE
    (which eigenforms contribute with what weights) across the c-family.
    This is a function-space constraint, not a prime-by-prime constraint.

    Returns
    -------
    Dict with bootstrap analysis.
    """
    results_per_c = {}

    for c_val in c_values:
        kappa = c_val / 2
        Q_contact = virasoro_quartic_contact(c_val)

        # At this c, the shadow tower determines the shadow coefficients
        # S_r(c). For a single eigenform, these map to:
        # S_r ~ (some c-dependent normalization) * p_r(alpha, beta)
        # The p_r satisfy Newton regardless of c.

        results_per_c[c_val] = {
            'kappa': kappa,
            'Q_contact': Q_contact,
            'note': 'Newton redundancy applies regardless of c.',
        }

    return {
        'c_values': list(c_values),
        'a_p': a_p,
        'k': k,
        'p': p,
        'per_c_analysis': results_per_c,
        'bootstrap_structure': {
            'single_prime_single_eigenform': (
                'NO new constraint. Newton redundancy means each c gives the '
                'same recursion p_r = e1*p_{r-1} - e2*p_{r-2}.'
            ),
            'multi_prime': (
                'The bootstrap across c constrains the SPECTRAL MEASURE '
                '(which eigenforms contribute). Different c -> different '
                'linear combinations of eigenforms. Consistency of these '
                'across the c-family constrains the allowed measures. '
                'But it constrains WHICH eigenforms appear, not their '
                'eigenvalues at individual primes.'
            ),
            'quartic_closure': (
                'The quartic closure conjecture (conj:quartic-closure) asserts '
                'that intersecting constraint loci over all c, u_0 gives '
                'exactly {rho : Re(rho) = 1/2}. This would be a constraint '
                'on zero POSITIONS (not eigenvalue magnitudes). The quartic '
                'closure is about the ZEROS of the moment L-function, '
                'not about Satake parameters at individual primes.'
            ),
        },
        'conclusion': (
            'The bootstrap does NOT add prime-by-prime constraints on Satake '
            'parameters. Its power lies in constraining the global spectral '
            'measure and the zero positions of moment L-functions through '
            'intersection of constraint loci across the c-family.'
        ),
    }


# =========================================================================
# 6. Rigidity test: does MC constrain beyond Newton?
# =========================================================================

def rigidity_beyond_newton(
    prime_bound: int = 20,
    r_max: int = 12,
) -> Dict[str, Any]:
    """Comprehensive test: at a single prime, does MC give any constraint
    beyond Newton's identity for two-variable power sums?

    Method:
    1. Pick a hypothetical eigenvalue a(p) that VIOLATES Ramanujan:
       |a(p)| > 2*p^{(k-1)/2}.
    2. Check whether the MC recursion at arities 2 through r_max is
       consistent with this choice.
    3. If YES: MC does not constrain beyond Newton (even Ramanujan-violating
       eigenvalues are consistent with the MC recursion).

    Returns
    -------
    Dict with rigidity analysis for violating and non-violating eigenvalues.
    """
    k = 12  # weight 12 (Ramanujan tau)
    p = 2   # smallest prime

    # The Ramanujan bound: |a(p)| <= 2*p^{5.5} = 2*2^5.5 ~ 90.51
    ram_bound = 2 * p ** ((k - 1) / 2)

    # Case 1: actual tau(2) = -24, satisfies Ramanujan
    tau_2 = ramanujan_tau(2)
    assert tau_2 == -24

    # Case 2: hypothetical violation: a(2) = 200 > 90.51
    a_violating = 200.0

    # Case 3: extreme violation: a(2) = 10000
    a_extreme = 10000.0

    cases = {
        'ramanujan_satisfying': tau_2,
        'mild_violation': a_violating,
        'extreme_violation': a_extreme,
    }

    results = {}
    for label, a_val in cases.items():
        e1 = a_val
        e2 = p ** (k - 1)  # p^11 = 2048

        # Compute power sums via Newton recursion
        p_rec = newton_two_variable_recursion(e1, e2, r_max)

        # Check Newton identities (they must hold by construction)
        # Use RELATIVE tolerance for large power sums
        if HAS_MPMATH:
            e1_mp = mpmath.mpc(e1)
            e2_mp = mpmath.mpc(e2)
        else:
            e1_mp = e1
            e2_mp = e2
        newton_holds = True
        for r in range(3, r_max + 1):
            residual = abs(p_rec[r - 1] - e1_mp * p_rec[r - 2] + e2_mp * p_rec[r - 3])
            scale = max(float(abs(p_rec[r - 1])), 1.0)
            relative = float(residual) / scale
            if relative > 1e-15:
                newton_holds = False
                break

        # Check: does any MC constraint at any arity FAIL for this choice?
        # The MC equation at arity r+1 gives: S_{r+1} determined by S_2,...,S_r.
        # For the Virasoro tower, this is the recursion with propagator 2/c.
        # For the spectral rewriting, this is Newton p_r = e1*p_{r-1} - e2*p_{r-2}.
        # Newton holds REGARDLESS of whether |a(p)| satisfies Ramanujan.
        mc_consistent = newton_holds

        satisfies_ramanujan = abs(a_val) <= ram_bound + 1e-10

        results[label] = {
            'a_p': a_val,
            'ramanujan_bound': ram_bound,
            'satisfies_ramanujan': satisfies_ramanujan,
            'newton_all_hold': newton_holds,
            'mc_consistent': mc_consistent,
            'conclusion': (
                f'MC equations at arities 2-{r_max} are '
                f'{"CONSISTENT" if mc_consistent else "INCONSISTENT"} '
                f'with a(2) = {a_val}, which '
                f'{"satisfies" if satisfies_ramanujan else "VIOLATES"} '
                f'the Ramanujan bound {ram_bound:.2f}.'
            ),
        }

    return {
        'cases': results,
        'master_conclusion': (
            'The MC equation at every finite arity is consistent with '
            'BOTH Ramanujan-satisfying and Ramanujan-violating eigenvalues. '
            'Newton\'s identity for two variables is a TAUTOLOGY (it follows '
            'from the characteristic equation x^2 - e1*x + e2 = 0), so it '
            'imposes no constraint on |alpha_p|. The MC equation, in spectral '
            'coordinates, reduces to Newton\'s identity. Therefore: MC does '
            'NOT constrain Satake parameters beyond Newton at a single prime.'
        ),
    }


# =========================================================================
# 7. Where the information gap lies
# =========================================================================

def information_source_analysis() -> Dict[str, str]:
    """Analyze where the ADDITIONAL information needed for Ramanujan must come from.

    The MC equation provides:
    - Newton recursion for power sums (redundant for 2 variables)
    - Modularity of the generating function (global, forces Hecke eigenvalues)
    - Bracket positivity (constrains weights c_j, not eigenvalues)

    The MISSING ingredients for Ramanujan:
    """
    return {
        'mc_provides': {
            'newton_recursion': 'p_r = e1*p_{r-1} - e2*p_{r-2} (REDUNDANT for 2 vars)',
            'modularity': 'G_rho(tau) modular => atoms are Hecke eigenvalues (GLOBAL)',
            'bracket_positivity': 'B(Sh_r, Sh_s) positive on cusp forms (WEIGHTS, not eigenvalues)',
            'overdetermination': 'For finite-atom measures, spectral rigidity at high arity',
        },
        'mc_does_not_provide': {
            'eigenvalue_bounds': '|alpha_p| = p^{(k-1)/2} not forced by MC at any finite arity',
            'symmetric_power_continuation': 'L(s, Sym^r f) analytic continuation for r >= 5',
            'positivity': 'Absolute value bounds on Satake parameters',
        },
        'additional_information_sources': {
            '(a)_galois_representations': (
                'Deligne\'s theorem: Hecke eigenforms of weight k >= 2 satisfy '
                'Ramanujan. Proved for lattice VOAs. Uses l-adic cohomology, '
                'NOT the MC equation.'
            ),
            '(b)_langlands_functoriality': (
                'Serre reduction: if L(s, Sym^r f) has analytic continuation for '
                'all r, then Ramanujan follows. Known for r <= 4 (Gelbart-Jacquet, '
                'Kim-Shahidi, Kim). Open for r >= 5. The MC equation provides '
                'the Sym^r DATA but not its analytic continuation.'
            ),
            '(c)_bootstrap_intersection': (
                'The quartic closure conjecture: intersecting constraint loci '
                'over all central charges gives {Re(rho) = 1/2}. This would '
                'constrain zero POSITIONS of moment L-functions, a different '
                'quantity from Satake parameter magnitudes.'
            ),
            '(d)_genus_2_and_higher': (
                'At genus 2, the period matrix Omega = [[tau_1, tau_{12}], [tau_{12}, tau_2]] '
                'is 2D, breaking the diagonal structure. The genus-2 sewing '
                'kernel couples Fock sectors, potentially providing genuinely '
                'new (non-Newton) constraints. This is the frontier.'
            ),
        },
        'honest_assessment': (
            'The MC equation CANNOT reach the Ramanujan bound through the '
            'shadow tower at a single prime. Newton\'s identity redundancy '
            'is the fundamental obstruction. The MC equation is an INTEGRABILITY '
            'constraint (D^2 = 0), while Ramanujan requires POSITIVITY '
            '(|alpha| = p^{(k-1)/2}). These are logically independent.\n\n'
            'The ONE genuinely new idea is the BOOTSTRAP: using all central '
            'charges simultaneously to constrain the moment L-function zeros. '
            'But this constrains zeros, not eigenvalue magnitudes, and the '
            'quartic closure conjecture is OPEN.\n\n'
            'For lattice VOAs, Ramanujan is PROVED (by Deligne), and the MC '
            'equation VERIFIES this independently. For non-lattice theories, '
            'MC provides no path to Ramanujan without additional input '
            '(Langlands functoriality or l-adic methods).'
        ),
    }


# =========================================================================
# Utilities
# =========================================================================

def _primes_up_to(n: int) -> List[int]:
    """Return all primes up to n via sieve."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]
