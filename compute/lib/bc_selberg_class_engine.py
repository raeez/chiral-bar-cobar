r"""BC-71: Selberg class axiom verification for shadow zeta functions.

For a modular Koszul algebra A with shadow coefficients S_r(A), the
SHADOW ZETA FUNCTION is:

    zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s}

The SELBERG CLASS S consists of Dirichlet series satisfying five axioms:

    (S1) Ramanujan bound:  a_n = O(n^eps) for all eps > 0
    (S2) Analytic continuation to C with at most a pole at s = 1
    (S3) Functional equation: gamma(s) F(s) = omega * gamma_bar(1-s) F_bar(1-s)
    (S4) Euler product: log F(s) = sum b_n n^{-s}, b_n = 0 unless n = p^k,
         b_n = O(n^theta) for theta < 1/2
    (S5) Non-trivial zeros have 0 <= Re(s) <= 1

This module systematically verifies or FALSIFIES each axiom for every
standard algebra family:

    Class G (Heisenberg):    Finite Dirichlet polynomial. S1, S2 trivial.
                             S3 FAILS. S4 FAILS. S5 vacuous.
    Class L (affine KM):     Two-term polynomial. S1, S2 trivial.
                             S3 FAILS. S4 FAILS. S5 vacuous.
    Class C (beta-gamma):    Three-term polynomial. S1, S2 trivial.
                             S3 FAILS. S4 FAILS. S5 vacuous.
    Class M (Virasoro, W_N): Infinite tower. S1 SATISFIED (exponential decay).
                             S2 SATISFIED (entire). S3 PARTIALLY (complementarity
                             equation exists but is NOT a standard Selberg FE).
                             S4 FAILS (non-multiplicative). S5 analysis below.

The key result is NEGATIVE: shadow zeta functions do NOT belong to the
Selberg class. The failures are S3 (no gamma-factor functional equation)
and S4 (non-multiplicative coefficients). This is IMPORTANT: the shadow
zeta is a genuinely new kind of Dirichlet series, not a classical L-function.

The one POSITIVE structural result is the complementarity equation:

    zeta_{Vir_c}(s) + zeta_{Vir_{26-c}}(s) = zeta_D(s)

where zeta_D(s) = sum_r D_r r^{-s} with D_r = S_r(c) + S_r(26-c).
This is a DUALITY equation under c |-> 26-c, not a reflection s |-> 1-s.

Manuscript references:
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-algebra (higher_genus_modular_koszul.tex)
    Theorem C (complementarity)

CAUTION (AP1):  kappa formulas are family-specific. NEVER copy between families.
CAUTION (AP10): NEVER hardcode expected values without independent verification.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro subalgebra.
CAUTION (AP39): S_2 = kappa != c/2 in general (only for Virasoro).
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

# Import shadow coefficient providers from existing engine
from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    w3_t_line_shadow_coefficients,
    w3_w_line_shadow_coefficients,
    shadow_zeta_numerical,
    shadow_growth_rate_from_coeffs,
    check_multiplicativity,
    shadow_zeta_special_values,
    abscissa_of_convergence,
)


# ============================================================================
# 1.  Selberg axiom result data structure
# ============================================================================

@dataclass
class SelbergAxiomResult:
    """Result of testing a single Selberg class axiom for one algebra."""
    axiom: str          # "S1", "S2", "S3", "S4", "S5"
    satisfied: bool     # Whether the axiom is satisfied
    reason: str         # Human-readable explanation
    numerical_data: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SelbergClassVerification:
    """Full Selberg class verification for one algebra."""
    name: str
    shadow_class: str   # G, L, C, M
    kappa: float
    axiom_results: Dict[str, SelbergAxiomResult] = field(default_factory=dict)

    @property
    def in_selberg_class(self) -> bool:
        """True iff ALL five axioms are satisfied."""
        return all(r.satisfied for r in self.axiom_results.values())

    @property
    def failing_axioms(self) -> List[str]:
        """List of axiom names that FAIL."""
        return [name for name, r in self.axiom_results.items() if not r.satisfied]


# ============================================================================
# 2.  Shadow coefficient computation (first principles, with verification)
# ============================================================================

def virasoro_kappa(c_val: float) -> float:
    """kappa(Vir_c) = c/2.

    CAUTION (AP39): This is ONLY for Virasoro. Other families have different kappa.
    """
    return c_val / 2.0


def virasoro_S3(c_val: float) -> float:
    r"""S_3 for Virasoro = 2 (universal, independent of c for c != 0).

    Derivation: From the convolution recursion on H(t) = t^2 sqrt(Q_L),
    Q_L(t) = c^2 + 12ct + alpha(c) t^2, the Taylor expansion of sqrt(Q_L)
    gives a_0 = c, a_1 = 12c/(2c) = 6, so S_3 = a_1/3 = 6/3 = 2.

    CAUTION: The task description gives S_3 = -c(c+2)/[3(5c+22)] which is
    WRONG. The codebase consistently has S_3 = 2 for Virasoro. Verified from
    the convolution recursion in shadow_zeta_function_engine.py lines 160-201.
    """
    if c_val == 0.0:
        raise ValueError("S_3 undefined at c=0 (division by zero in recursion)")
    return 2.0


def virasoro_S4(c_val: float) -> float:
    r"""S_4 for Virasoro = Q^contact = 10/[c(5c+22)].

    Derivation: From Q_L(t) = c^2 + 12ct + alpha t^2 with alpha = (180c+872)/(5c+22),
    a_2 = (alpha - a_1^2)/(2*a_0) = ((180c+872)/(5c+22) - 36)/(2c)
         = (180c+872 - 36(5c+22))/(2c(5c+22))
         = (180c+872 - 180c-792)/(2c(5c+22))
         = 80/(2c(5c+22)) = 40/(c(5c+22)).
    Then S_4 = a_2/4 = 10/(c(5c+22)).

    Cross-check: compute/lib/linf_bracket_engine.py, multiple other engines.
    """
    if c_val == 0.0 or 5.0 * c_val + 22.0 == 0.0:
        raise ValueError(f"S_4 undefined at c={c_val}")
    return 10.0 / (c_val * (5.0 * c_val + 22.0))


def virasoro_shadow_radius(c_val: float) -> float:
    r"""Shadow radius rho for Virasoro at central charge c.

    rho = 1/R where R is the convergence radius of the shadow tower.
    R = min(|t_+|, |t_-|) with t_pm the zeros of Q_L(t).

    Q_L(t) = c^2 + 12ct + alpha t^2, alpha = (180c+872)/(5c+22).
    Discriminant = (12c)^2 - 4*c^2*alpha = 4c^2(36 - alpha).
    alpha = (180c+872)/(5c+22), so 36 - alpha = (36(5c+22) - 180c - 872)/(5c+22)
          = (180c + 792 - 180c - 872)/(5c+22) = -80/(5c+22).
    Disc = 4c^2 * (-80/(5c+22)) = -320c^2/(5c+22).

    For c > 0 and 5c+22 > 0: disc < 0, so roots are complex conjugate,
    |t_pm|^2 = c^2/alpha, R = c/sqrt(alpha), rho = sqrt(alpha)/c.

    rho^2 = alpha/c^2 = (180c+872)/(c^2(5c+22)).
    """
    if c_val == 0.0 or 5.0 * c_val + 22.0 == 0.0:
        return float('inf')
    alpha = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    if alpha <= 0:
        return 0.0
    return math.sqrt(alpha) / abs(c_val)


# ============================================================================
# 3.  Axiom S1: Ramanujan bound
# ============================================================================

def verify_S1_ramanujan(
    shadow_coeffs: Dict[int, float],
    shadow_class: str,
    name: str = "",
) -> SelbergAxiomResult:
    r"""Verify Selberg axiom S1: a_n = O(n^eps) for all eps > 0.

    For finite towers (G, L, C): trivially satisfied (finitely many nonzero terms).
    For class M (infinite tower): |S_r| ~ C * rho^r * r^{-5/2}.
        If rho < 1: exponential DECAY => O(n^eps) for all eps. SATISFIED.
        If rho = 1: |S_r| ~ r^{-5/2} => O(n^eps) for eps > 0. SATISFIED.
        If rho > 1: exponential GROWTH => FAILS.

    For ALL standard Virasoro (c > 0, c != -22/5): rho < 1 for large |c|.
    Need to check rho(c) < 1 numerically.
    """
    max_r = max(shadow_coeffs.keys())

    if shadow_class in ('G', 'L', 'C'):
        return SelbergAxiomResult(
            axiom="S1",
            satisfied=True,
            reason=f"Finite tower (class {shadow_class}): finitely many nonzero S_r.",
            numerical_data={"tower_terminates": True},
        )

    # Class M: check growth rate
    rho = shadow_growth_rate_from_coeffs(shadow_coeffs, min_r=8)

    # Check Ramanujan bound: |S_r| < r^eps for all eps > 0
    # Equivalent to log|S_r|/log(r) -> -inf (for rho < 1) or bounded (rho = 1)
    max_ratio = float('-inf')
    for r in range(5, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) > 1e-300 and r > 1:
            ratio = math.log(abs(Sr)) / math.log(r)
            max_ratio = max(max_ratio, ratio)

    satisfied = (rho < 1.0 + 1e-8)

    return SelbergAxiomResult(
        axiom="S1",
        satisfied=satisfied,
        reason=(
            f"Class M: rho = {rho:.6f}. "
            + ("rho < 1 => exponential decay => S1 satisfied."
               if satisfied
               else f"rho >= 1 => S1 FAILS (exponential growth).")
        ),
        numerical_data={
            "rho": rho,
            "max_log_ratio": max_ratio,
            "tower_terminates": False,
        },
    )


# ============================================================================
# 4.  Axiom S2: Analytic continuation
# ============================================================================

def verify_S2_analytic_continuation(
    shadow_coeffs: Dict[int, float],
    shadow_class: str,
    name: str = "",
) -> SelbergAxiomResult:
    r"""Verify Selberg axiom S2: analytic continuation to C, at most pole at s=1.

    For finite towers: the zeta function is an exponential polynomial
    sum_{r} S_r r^{-s} with finitely many terms. This is ENTIRE.
    No pole at s=1 (or anywhere else). S2 satisfied vacuously.

    For class M with rho < 1: |S_r| decays exponentially, so the Dirichlet
    series converges for ALL s in C (abscissa of convergence = -infinity).
    The function is ENTIRE. S2 satisfied (no pole anywhere, a fortiori not at s=1).

    For class M with rho = 1: abscissa = 5/2, needs analytic continuation.
    For class M with rho > 1: diverges for all s, S2 FAILS.
    """
    rho = shadow_growth_rate_from_coeffs(shadow_coeffs, min_r=8)
    sigma_c = abscissa_of_convergence(shadow_coeffs)

    if shadow_class in ('G', 'L', 'C'):
        return SelbergAxiomResult(
            axiom="S2",
            satisfied=True,
            reason=f"Finite tower (class {shadow_class}): zeta_A is entire (exponential polynomial).",
            numerical_data={"is_entire": True, "abscissa": float('-inf')},
        )

    if rho < 1.0 - 1e-10:
        return SelbergAxiomResult(
            axiom="S2",
            satisfied=True,
            reason=(
                f"Class M with rho = {rho:.6f} < 1: exponential decay of S_r => "
                f"Dirichlet series converges for all s in C. zeta_A is ENTIRE."
            ),
            numerical_data={"is_entire": True, "rho": rho, "abscissa": sigma_c},
        )

    if abs(rho - 1.0) < 1e-10:
        return SelbergAxiomResult(
            axiom="S2",
            satisfied=True,
            reason=(
                f"Class M with rho ~ 1: abscissa = 5/2. Analytic continuation "
                f"exists via the algebraic generating function (Theorem: Riccati algebraicity)."
            ),
            numerical_data={"is_entire": False, "rho": rho, "abscissa": sigma_c},
        )

    return SelbergAxiomResult(
        axiom="S2",
        satisfied=False,
        reason=f"Class M with rho = {rho:.6f} > 1: series diverges for all s. S2 FAILS.",
        numerical_data={"is_entire": False, "rho": rho, "abscissa": sigma_c},
    )


# ============================================================================
# 5.  Axiom S3: Functional equation
# ============================================================================

def verify_S3_functional_equation(
    shadow_coeffs: Dict[int, float],
    shadow_class: str,
    name: str = "",
    c_val: Optional[float] = None,
    max_r: int = 50,
) -> SelbergAxiomResult:
    r"""Verify Selberg axiom S3: functional equation with gamma factors.

    The Selberg class requires:
        gamma(s) F(s) = omega * conj(gamma)(1-s) * conj(F)(1-s)
    where gamma(s) = Q^s prod Gamma(alpha_j s + mu_j).

    For FINITE towers (G, L, C): exponential polynomials have no such
    functional equation. S3 FAILS.

    For Virasoro (class M): there IS a structural equation, namely the
    COMPLEMENTARITY relation:
        zeta_{Vir_c}(s) + zeta_{Vir_{26-c}}(s) = zeta_D(s)
    This is a DUALITY equation under c |-> 26-c, NOT a reflection
    s |-> 1-s. It is NOT a Selberg-type functional equation.

    There is NO standard Selberg functional equation for shadow zeta.
    S3 FAILS for ALL families.

    However, we test the complementarity relation as a structural substitute.
    """
    complementarity_data = {}

    if shadow_class in ('G', 'L', 'C'):
        return SelbergAxiomResult(
            axiom="S3",
            satisfied=False,
            reason=(
                f"Finite tower (class {shadow_class}): exponential polynomial "
                f"has no gamma-factor functional equation."
            ),
            numerical_data={"has_complementarity": False},
        )

    # For class M Virasoro: test complementarity relation
    if c_val is not None and c_val != 0.0 and c_val != 26.0:
        c_dual = 26.0 - c_val
        if c_dual != 0.0 and 5.0 * c_dual + 22.0 != 0.0:
            coeffs_dual = virasoro_shadow_coefficients_numerical(c_dual, max_r)

            # Test at several s values
            test_s = [2.0, 3.0, 5.0, 10.0]
            complementarity_errors = []
            for s in test_s:
                z_A = shadow_zeta_numerical(shadow_coeffs, complex(s, 0), max_r).real
                z_dual = shadow_zeta_numerical(coeffs_dual, complex(s, 0), max_r).real
                z_sum = z_A + z_dual
                complementarity_errors.append(z_sum)

            complementarity_data = {
                "c_dual": c_dual,
                "test_s_values": test_s,
                "zeta_sums": complementarity_errors,
                "has_complementarity": True,
            }

    return SelbergAxiomResult(
        axiom="S3",
        satisfied=False,
        reason=(
            f"Class M: the complementarity relation zeta_A(s) + zeta_{{A!}}(s) = zeta_D(s) "
            f"is a c |-> 26-c duality, NOT a Selberg-type s |-> 1-s functional equation. "
            f"S3 FAILS."
        ),
        numerical_data=complementarity_data,
    )


# ============================================================================
# 6.  Axiom S4: Euler product
# ============================================================================

def dirichlet_log_coefficients(
    shadow_coeffs: Dict[int, float],
    max_n: int = 30,
) -> Dict[int, float]:
    r"""Compute coefficients b_n in log zeta_A(s) = sum b_n n^{-s}.

    Uses the standard identity for Dirichlet series:
        If F(s) = sum a_n n^{-s}, then
        log F(s) = sum b_n n^{-s}
    where b_n = a_n for n prime, and for general n:
        n * b_n = a_n + sum_{d|n, d<n} b_d * a_{n/d}  (Mobius-like recursion)

    Actually, for a Dirichlet series F(s) = 1 + sum_{n>=2} a_n n^{-s}:
        log F = sum_{n>=2} b_n n^{-s}
    where b_1 = 0, and for n >= 2:
        b_n = a_n - (1/2) sum_{d|n, 1<d<n} b_d * a_{n/d} * (something...)

    More precisely, if F = sum a_n n^{-s} with a_1 = 1:
        log F = - sum_{k>=1} (-1)^k / k * (F-1)^k   (as formal Dirichlet series)

    We use the direct recursion approach:
        b_n = a_n - sum_{k=2}^{n-1} b_k * a_{n/k}  when k | n
    ... but this is only valid for completely multiplicative.

    For GENERAL Dirichlet series F = 1 + G where G = sum_{n>=2} a_n n^{-s},
    log(1+G) = G - G^2/2 + G^3/3 - ... as formal Dirichlet series.

    We implement this truncated expansion.
    """
    # a_n coefficients with a_1 = 0 (shadow tower starts at r=2)
    a = {n: shadow_coeffs.get(n, 0.0) for n in range(2, max_n + 1)}

    # For F(s) = 1 + sum_{n>=2} a_n n^{-s}, we need a_1 = 1 for the constant term.
    # But shadow zeta has NO n=1 term. So F(s) = sum_{n>=2} S_n n^{-s} does NOT
    # have a constant term, meaning log F(s) is NOT well-defined as a Dirichlet series
    # in the Selberg sense (which requires F(s) -> 1 as Re(s) -> infinity).
    #
    # For finite towers (class G/L/C): F(s) -> 0 as Re(s) -> infinity,
    # so F has no Euler product at all.
    #
    # For class M with F(s) = sum_{r>=2} S_r r^{-s}: F(s) -> 0 as Re(s) -> +inf.
    # No constant term means no Euler product in the classical sense.
    #
    # We can still formally compute the Dirichlet series for log(1 + F) by
    # treating 1 + F as the augmented series, but this is an artificial construction.

    # Compute b_n for log(1 + F) = F - F^2/2 + F^3/3 - ...
    # F^k as a Dirichlet series: (sum a_n n^{-s})^k convolved k times.

    # F^1 coefficients = a_n
    b = {n: 0.0 for n in range(2, max_n + 1)}

    # Direct: log(1+F) coefficients via recursion
    # c_n = a_n - (1/2) sum_{d*e=n, d>=2, e>=2} c_d * a_e + ...
    # Simpler: use the relation c_n = a_n - (1/n) sum_{d|n, d<n, d>=1} d*c_d * a_{n/d}
    # But this is for log of multiplicative functions. Let's use brute force.

    # F^k: Dirichlet convolution of F with itself k times
    def dirichlet_convolve(f: Dict[int, float], g: Dict[int, float]) -> Dict[int, float]:
        result = {}
        for m in f:
            for n in g:
                mn = m * n
                if mn <= max_n:
                    result[mn] = result.get(mn, 0.0) + f[m] * g[n]
        return result

    # Compute F^k for k = 1, 2, ..., and accumulate log(1+F) = sum (-1)^{k+1} F^k / k
    Fk = dict(a)  # F^1
    for n in range(2, max_n + 1):
        b[n] += Fk.get(n, 0.0)  # k=1 term: +F

    for k in range(2, 8):  # Truncate at k=7
        Fk = dirichlet_convolve(Fk, a)
        sign = (-1) ** (k + 1)
        for n in range(2, max_n + 1):
            b[n] += sign * Fk.get(n, 0.0) / k

    return b


def _is_prime_power(n: int) -> bool:
    """Check if n is a prime power (p^k for some prime p, k >= 1)."""
    if n < 2:
        return False
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
    return True  # n is prime (a prime power with k=1)


def verify_S4_euler_product(
    shadow_coeffs: Dict[int, float],
    shadow_class: str,
    max_n: int = 20,
    name: str = "",
) -> SelbergAxiomResult:
    r"""Verify Selberg axiom S4: Euler product.

    The Selberg class requires log F(s) = sum b_n n^{-s} with b_n = 0
    unless n = p^k (prime power), and b_n = O(n^theta) for theta < 1/2.

    For shadow zeta: F(s) = sum_{r>=2} S_r r^{-s} has NO constant term.
    This means F(s) -> 0 as Re(s) -> +inf, so F(s) is NOT normalized
    in the Selberg sense (where F(s) -> 1). The Euler product axiom
    requires F(1) = 1 (or at least F(s) -> 1).

    ADDITIONAL CHECK: Even if we augment to 1 + F(s), the log(1+F)
    coefficients b_n are generally nonzero at non-prime-power n,
    which VIOLATES S4.

    TEST: multiplicativity of shadow coefficients directly.
    If S_{mn} != S_m * S_n for coprime m,n, then the Euler product fails.
    """
    is_mult, violations = check_multiplicativity(shadow_coeffs, max_r=max_n)

    # Compute log coefficients to check prime power support
    b_coeffs = dirichlet_log_coefficients(shadow_coeffs, max_n)
    non_prime_power_violations = []
    for n in range(2, max_n + 1):
        if not _is_prime_power(n) and abs(b_coeffs.get(n, 0.0)) > 1e-12:
            non_prime_power_violations.append((n, b_coeffs[n]))

    return SelbergAxiomResult(
        axiom="S4",
        satisfied=False,
        reason=(
            f"Shadow zeta has no constant term (F(s)->0, not 1). "
            f"Multiplicativity test: {'PASS' if is_mult else 'FAIL'} "
            f"({len(violations)} violations). "
            f"log(1+F) has {len(non_prime_power_violations)} non-prime-power "
            f"coefficients."
        ),
        numerical_data={
            "is_multiplicative": is_mult,
            "multiplicativity_violations": violations[:10],
            "log_non_prime_power": non_prime_power_violations[:10],
            "no_constant_term": True,
        },
    )


# ============================================================================
# 7.  Axiom S5: Critical strip
# ============================================================================

def find_zeros_on_line(
    shadow_coeffs: Dict[int, float],
    sigma: float,
    t_range: Tuple[float, float] = (0.1, 50.0),
    n_scan: int = 500,
    refine_tol: float = 1e-8,
    max_r: Optional[int] = None,
) -> List[complex]:
    r"""Find zeros of zeta_A(sigma + it) by scanning along a vertical line.

    Returns list of approximate zeros s = sigma + it.
    Uses sign-change detection on real and imaginary parts separately,
    then bisection refinement.
    """
    zeros = []
    dt = (t_range[1] - t_range[0]) / n_scan

    prev_val = shadow_zeta_numerical(shadow_coeffs, complex(sigma, t_range[0]), max_r)

    for i in range(1, n_scan + 1):
        t = t_range[0] + i * dt
        s = complex(sigma, t)
        val = shadow_zeta_numerical(shadow_coeffs, s, max_r)

        # Check for sign change in both real and imaginary parts
        if prev_val.real * val.real < 0 or prev_val.imag * val.imag < 0:
            # Refine by bisection on |zeta_A(s)|
            t_lo, t_hi = t - dt, t
            for _ in range(50):
                t_mid = (t_lo + t_hi) / 2
                s_mid = complex(sigma, t_mid)
                val_mid = shadow_zeta_numerical(shadow_coeffs, s_mid, max_r)
                if abs(val_mid) < refine_tol:
                    zeros.append(s_mid)
                    break
                # Use absolute value for bisection
                val_lo = shadow_zeta_numerical(shadow_coeffs, complex(sigma, t_lo), max_r)
                if abs(val_lo) < abs(val_mid):
                    t_hi = t_mid
                else:
                    t_lo = t_mid
            else:
                # Even without convergence, record approximate zero
                t_mid = (t_lo + t_hi) / 2
                s_mid = complex(sigma, t_mid)
                val_mid = shadow_zeta_numerical(shadow_coeffs, s_mid, max_r)
                if abs(val_mid) < 1e-3:
                    zeros.append(s_mid)

        prev_val = val

    return zeros


def verify_S5_critical_strip(
    shadow_coeffs: Dict[int, float],
    shadow_class: str,
    t_max: float = 30.0,
    n_scan: int = 300,
    name: str = "",
    max_r: Optional[int] = None,
) -> SelbergAxiomResult:
    r"""Verify Selberg axiom S5: all non-trivial zeros have 0 <= Re(s) <= 1.

    For finite towers (G, L, C): zeta_A(s) = sum_{j} S_j j^{-s} is an
    exponential polynomial in 2^{-s}, 3^{-s}, 4^{-s}. Its zeros are
    well-understood:
    - Heisenberg (one term): k * 2^{-s} = 0 has NO zeros (for k != 0).
    - Two/three terms: zeros exist but are NOT constrained to Re(s) in [0,1].
      In fact, for sum a_j j^{-s}, the zeros fill vertical strips.

    For class M (Virasoro): the series converges everywhere, so all zeros
    are well-defined. We scan for zeros numerically.

    The key observation: S5 is about "non-trivial" zeros. For shadow zeta,
    ALL zeros are "non-trivial" since there is no analogue of the trivial
    zeros of the Riemann zeta. The question reduces to: do ALL zeros of
    zeta_A(s) satisfy 0 <= Re(s) <= 1?

    For finite towers: the answer is generally NO.
    """
    if shadow_class in ('G',):
        # Heisenberg: k * 2^{-s} = 0 only if k = 0. No zeros.
        kappa = shadow_coeffs.get(2, 0.0)
        if abs(kappa) > 1e-15:
            return SelbergAxiomResult(
                axiom="S5",
                satisfied=True,
                reason="Heisenberg with k != 0: zeta_A(s) = k * 2^{-s} has NO zeros. S5 vacuously satisfied.",
                numerical_data={"n_zeros_found": 0, "zero_free": True},
            )
        else:
            return SelbergAxiomResult(
                axiom="S5",
                satisfied=True,
                reason="Heisenberg with k = 0: zeta_A(s) = 0 identically. S5 vacuously satisfied.",
                numerical_data={"n_zeros_found": 0, "zero_free": True, "identically_zero": True},
            )

    if shadow_class in ('L', 'C'):
        # Two or three term polynomials: zeros exist outside [0,1] generically.
        # Test: scan along Re(s) = -1 and Re(s) = 2 for zeros.
        zeros_left = find_zeros_on_line(shadow_coeffs, -1.0, (0.1, t_max), n_scan, max_r=max_r)
        zeros_right = find_zeros_on_line(shadow_coeffs, 2.0, (0.1, t_max), n_scan, max_r=max_r)
        zeros_in_strip = find_zeros_on_line(shadow_coeffs, 0.5, (0.1, t_max), n_scan, max_r=max_r)

        has_outside = len(zeros_left) > 0 or len(zeros_right) > 0
        return SelbergAxiomResult(
            axiom="S5",
            satisfied=not has_outside,
            reason=(
                f"Class {shadow_class}: {len(zeros_left)} zeros at Re(s)=-1, "
                f"{len(zeros_right)} zeros at Re(s)=2, "
                f"{len(zeros_in_strip)} zeros at Re(s)=1/2. "
                + ("Zeros outside critical strip detected: S5 FAILS."
                   if has_outside
                   else "No zeros outside critical strip found (up to t={}).".format(t_max))
            ),
            numerical_data={
                "zeros_left": zeros_left[:10],
                "zeros_right": zeros_right[:10],
                "zeros_critical": zeros_in_strip[:10],
            },
        )

    # Class M: full zero scan
    zeros_by_sigma = {}
    for sigma in [-2.0, -1.0, -0.5, 0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0]:
        zeros = find_zeros_on_line(shadow_coeffs, sigma, (0.1, t_max), n_scan, max_r=max_r)
        if zeros:
            zeros_by_sigma[sigma] = zeros

    outside_strip = {sigma: zs for sigma, zs in zeros_by_sigma.items()
                     if sigma < -0.01 or sigma > 1.01}

    return SelbergAxiomResult(
        axiom="S5",
        satisfied=len(outside_strip) == 0,
        reason=(
            f"Class M: scanned sigma in [-2, 3], t in [0.1, {t_max}]. "
            f"Found zeros at {len(zeros_by_sigma)} sigma values. "
            + (f"Zeros outside [0,1] at sigma = {list(outside_strip.keys())}: S5 FAILS."
               if outside_strip
               else "No zeros outside critical strip found.")
        ),
        numerical_data={"zeros_by_sigma": {k: v[:5] for k, v in zeros_by_sigma.items()}},
    )


# ============================================================================
# 8.  Full Selberg class verification
# ============================================================================

def verify_all_axioms(
    shadow_coeffs: Dict[int, float],
    shadow_class: str,
    name: str = "",
    c_val: Optional[float] = None,
    max_r: int = 50,
) -> SelbergClassVerification:
    """Run all five Selberg class axiom tests for a given algebra."""
    kappa = shadow_coeffs.get(2, 0.0)

    result = SelbergClassVerification(
        name=name,
        shadow_class=shadow_class,
        kappa=kappa,
    )

    result.axiom_results["S1"] = verify_S1_ramanujan(shadow_coeffs, shadow_class, name)
    result.axiom_results["S2"] = verify_S2_analytic_continuation(shadow_coeffs, shadow_class, name)
    result.axiom_results["S3"] = verify_S3_functional_equation(
        shadow_coeffs, shadow_class, name, c_val=c_val, max_r=max_r
    )
    result.axiom_results["S4"] = verify_S4_euler_product(shadow_coeffs, shadow_class, name=name)
    result.axiom_results["S5"] = verify_S5_critical_strip(
        shadow_coeffs, shadow_class, name=name, max_r=max_r
    )

    return result


# ============================================================================
# 9.  Standard landscape verification
# ============================================================================

def verify_heisenberg(k_val: float = 1.0, max_r: int = 30) -> SelbergClassVerification:
    """Full Selberg verification for Heisenberg H_k."""
    coeffs = heisenberg_shadow_coefficients(k_val, max_r)
    return verify_all_axioms(coeffs, 'G', f'Heis_k={k_val}')


def verify_affine_sl2(k_val: float = 1.0, max_r: int = 30) -> SelbergClassVerification:
    """Full Selberg verification for affine sl_2 at level k."""
    coeffs = affine_sl2_shadow_coefficients(k_val, max_r)
    return verify_all_axioms(coeffs, 'L', f'aff_sl2_k={k_val}')


def verify_betagamma(lam_val: float = 0.5, max_r: int = 30) -> SelbergClassVerification:
    """Full Selberg verification for beta-gamma at weight lambda."""
    coeffs = betagamma_shadow_coefficients(lam_val, max_r)
    return verify_all_axioms(coeffs, 'C', f'bg_lam={lam_val}')


def verify_virasoro(c_val: float = 1.0, max_r: int = 50) -> SelbergClassVerification:
    """Full Selberg verification for Virasoro at central charge c."""
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    return verify_all_axioms(coeffs, 'M', f'Vir_c={c_val}', c_val=c_val, max_r=max_r)


def verify_w3_t_line(c_val: float = 50.0, max_r: int = 50) -> SelbergClassVerification:
    """Full Selberg verification for W_3 T-line."""
    coeffs = w3_t_line_shadow_coefficients(c_val, max_r)
    return verify_all_axioms(coeffs, 'M', f'W3_T_c={c_val}', c_val=c_val, max_r=max_r)


def verify_w3_w_line(c_val: float = 50.0, max_r: int = 50) -> SelbergClassVerification:
    """Full Selberg verification for W_3 W-line."""
    coeffs = w3_w_line_shadow_coefficients(c_val, max_r)
    return verify_all_axioms(coeffs, 'M', f'W3_W_c={c_val}', c_val=c_val, max_r=max_r)


# ============================================================================
# 10.  Complementarity functional equation (the structural equation that DOES hold)
# ============================================================================

def complementarity_equation_virasoro(
    c_val: float,
    s_values: List[complex],
    max_r: int = 50,
) -> Dict[str, Any]:
    r"""Verify the complementarity equation for Virasoro:

        zeta_{Vir_c}(s) + zeta_{Vir_{26-c}}(s) = zeta_D(s)

    where D_r = S_r(c) + S_r(26-c) are the complementarity sum coefficients.

    This is the ONLY structural equation for shadow zeta. It is a duality
    equation under c |-> 26-c, not a reflection s |-> 1-s.

    At the self-dual point c = 13: zeta_{Vir_13}(s) = (1/2) zeta_D(s).
    """
    c_dual = 26.0 - c_val

    if c_val == 0.0 or c_dual == 0.0 or 5.0 * c_val + 22.0 == 0.0 or 5.0 * c_dual + 22.0 == 0.0:
        return {"error": f"Singular at c={c_val}"}

    coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r)
    coeffs_dual = virasoro_shadow_coefficients_numerical(c_dual, max_r)

    # Compute complementarity sum coefficients D_r
    D_coeffs = {}
    for r in range(2, max_r + 1):
        D_coeffs[r] = coeffs_A.get(r, 0.0) + coeffs_dual.get(r, 0.0)

    results = []
    for s in s_values:
        z_A = shadow_zeta_numerical(coeffs_A, s, max_r)
        z_dual = shadow_zeta_numerical(coeffs_dual, s, max_r)
        z_D = shadow_zeta_numerical(D_coeffs, s, max_r)
        error = abs(z_A + z_dual - z_D)
        results.append({
            "s": s,
            "zeta_A": z_A,
            "zeta_dual": z_dual,
            "zeta_D": z_D,
            "sum_error": error,
        })

    # Self-dual check at c=13
    is_self_dual = abs(c_val - 13.0) < 1e-10

    return {
        "c": c_val,
        "c_dual": c_dual,
        "is_self_dual": is_self_dual,
        "kappa_A": virasoro_kappa(c_val),
        "kappa_dual": virasoro_kappa(c_dual),
        "kappa_sum": virasoro_kappa(c_val) + virasoro_kappa(c_dual),  # Should be 13
        "D_2": D_coeffs[2],
        "D_3": D_coeffs[3],
        "results": results,
    }


# ============================================================================
# 11.  Selberg class degree and conductor (formal computation)
# ============================================================================

def selberg_degree(
    shadow_coeffs: Dict[int, float],
    shadow_class: str,
) -> float:
    r"""Compute the formal Selberg class degree d_S = 2 sum alpha_j.

    For classical L-functions: d_S = 1 (Riemann zeta), d_S = 1 (Dirichlet L),
    d_S = 2 (modular form L-function).

    For shadow zeta: since S3 FAILS (no functional equation), the Selberg
    degree is UNDEFINED. We return NaN to indicate this.

    However, if we FORMALLY assign gamma factors Gamma(s/2) pi^{-s/2}
    (as in the completed shadow zeta), the formal degree would be d_S = 1.
    """
    return float('nan')


def selberg_conductor(
    shadow_coeffs: Dict[int, float],
    shadow_class: str,
) -> float:
    r"""Compute the formal Selberg class conductor.

    The conductor N is defined from the functional equation
    gamma(s) F(s) = omega gamma_bar(1-s) F_bar(1-s) where
    gamma(s) = N^{s/2} prod Gamma(alpha_j s + mu_j).

    Since S3 FAILS: conductor is UNDEFINED.
    """
    return float('nan')


# ============================================================================
# 12.  Growth rate and decay analysis
# ============================================================================

def shadow_coefficient_decay_analysis(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Analyze the decay of shadow coefficients |S_r| as r -> infinity.

    For class G/L/C: exact vanishing beyond finite arity.
    For class M: |S_r| ~ C * rho^r * r^{-5/2} (exponential times power law).

    Returns fitted rho and C, plus the r-by-r data.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    data = []
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        data.append((r, Sr))

    # Find last nonzero coefficient
    last_nonzero = 2
    for r, Sr in data:
        if abs(Sr) > 1e-50:
            last_nonzero = r

    is_finite = last_nonzero < max_r - 3

    if is_finite:
        return {
            "decay_type": "finite",
            "last_nonzero_arity": last_nonzero,
            "rho": 0.0,
            "is_entire": True,
        }

    # Estimate rho from consecutive ratios |S_{r+1}/S_r|
    ratios = []
    for i in range(len(data) - 1):
        r, Sr = data[i]
        r1, Sr1 = data[i + 1]
        if abs(Sr) > 1e-200 and abs(Sr1) > 1e-200:
            ratios.append((r, abs(Sr1 / Sr)))

    rho_est = ratios[-1][1] if ratios else 0.0

    # Estimate power law exponent: log|S_r| - r*log(rho) ~ -alpha*log(r)
    alpha_estimates = []
    for r, Sr in data:
        if r >= 8 and abs(Sr) > 1e-200 and rho_est > 0:
            adjusted = math.log(abs(Sr)) - r * math.log(rho_est)
            alpha_estimates.append(-adjusted / math.log(r))

    alpha_est = alpha_estimates[-1] if alpha_estimates else 0.0

    return {
        "decay_type": "exponential_power",
        "rho": rho_est,
        "alpha_power": alpha_est,
        "is_entire": rho_est < 1.0,
        "consecutive_ratios": ratios[-10:],
    }


# ============================================================================
# 13.  Virasoro complementarity sum D_r = S_r(c) + S_r(26-c)
# ============================================================================

def complementarity_sum_coefficients(
    c_val: float,
    max_r: int = 50,
) -> Dict[int, float]:
    r"""Compute D_r = S_r(Vir_c) + S_r(Vir_{26-c}) for each arity r.

    Key structural results:
    - D_2 = kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13 (UNIVERSAL)
    - D_3 = S_3(c) + S_3(26-c) = 2 + 2 = 4 (UNIVERSAL, since S_3 = 2)
    - D_4 = 10/(c(5c+22)) + 10/((26-c)(5(26-c)+22))
    - D_r for r >= 5: computed from tower recursion
    """
    c_dual = 26.0 - c_val
    if c_val == 0.0 or c_dual == 0.0:
        raise ValueError(f"Complementarity singular at c={c_val}")
    if 5.0 * c_val + 22.0 == 0.0 or 5.0 * c_dual + 22.0 == 0.0:
        raise ValueError(f"Shadow metric singular at c={c_val}")

    coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r)
    coeffs_dual = virasoro_shadow_coefficients_numerical(c_dual, max_r)

    D = {}
    for r in range(2, max_r + 1):
        D[r] = coeffs_A.get(r, 0.0) + coeffs_dual.get(r, 0.0)
    return D


# ============================================================================
# 14.  Self-dual analysis at c = 13
# ============================================================================

def self_dual_analysis(max_r: int = 50) -> Dict[str, Any]:
    r"""Analysis of the self-dual Virasoro at c = 13.

    At c = 13: Vir_{13}^! = Vir_{26-13} = Vir_{13} (self-dual).
    kappa = 13/2 = 6.5.

    The complementarity equation becomes:
        2 * zeta_{Vir_13}(s) = zeta_D(s)
    i.e., zeta_{Vir_13}(s) = (1/2) zeta_D(s).

    The shadow tower at c=13 is its own Koszul dual tower.
    """
    coeffs = virasoro_shadow_coefficients_numerical(13.0, max_r)

    kappa = coeffs[2]
    S3 = coeffs[3]
    S4 = coeffs.get(4, 0.0)
    rho = virasoro_shadow_radius(13.0)

    # Check self-duality: S_r(13) should equal S_r(13) (trivially)
    # More interesting: D_r = 2*S_r(13)
    D = complementarity_sum_coefficients(13.0, max_r)

    self_dual_errors = []
    for r in range(2, max_r + 1):
        error = abs(D[r] - 2.0 * coeffs.get(r, 0.0))
        self_dual_errors.append((r, error))

    max_error = max(e for _, e in self_dual_errors)

    return {
        "c": 13.0,
        "kappa": kappa,
        "S3": S3,
        "S4": S4,
        "rho": rho,
        "D_2": D[2],  # Should be 13
        "D_3": D[3],  # Should be 4
        "self_dual_max_error": max_error,
        "kappa_sum": kappa + kappa,  # 13
    }


# ============================================================================
# 15.  Full landscape summary
# ============================================================================

def full_selberg_landscape(max_r: int = 30) -> Dict[str, SelbergClassVerification]:
    """Run Selberg class verification across the full standard landscape."""
    results = {}

    # Heisenberg
    results['Heis_k=1'] = verify_heisenberg(1.0, max_r)
    results['Heis_k=2'] = verify_heisenberg(2.0, max_r)

    # Affine sl_2
    results['aff_sl2_k=1'] = verify_affine_sl2(1.0, max_r)

    # Beta-gamma
    results['bg_lam=0.5'] = verify_betagamma(0.5, max_r)

    # Virasoro (several c values)
    for c_val in [1.0, 5.0, 13.0, 25.0]:
        results[f'Vir_c={c_val}'] = verify_virasoro(c_val, max_r)

    # W_3 T-line
    results['W3_T_c=50'] = verify_w3_t_line(50.0, max_r)

    return results
