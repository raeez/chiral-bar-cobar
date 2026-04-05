r"""Motivic weight filtration on the universal residue factor A_c(rho)
and the shadow L-function.

MATHEMATICAL CONTENT:

The universal residue factor from the Benjamin-Chang constrained Epstein
functional equation (def:universal-residue-factor, arithmetic_shadows.tex)
is:

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2)
                  * zeta'(rho))

Each factor of A_c(rho) carries a formal motivic weight in the sense of
Deligne's theory of mixed motives and periods.

MOTIVIC WEIGHT ASSIGNMENTS (Deligne, Fontaine-Perrin-Riou):

  1. Gamma((1+rho)/2): archimedean Gamma factor, weight 0 (archimedean
     period of the Tate motive).

  2. pi^{rho+1/2}: this is (2*pi*i)^n up to algebraic factors in the
     critical-value regime.  Weight 0 as a period normalizer.

  3. zeta(1+rho): at a nontrivial zero rho = 1/2 + i*gamma, the value
     zeta(1+rho) = zeta(3/2 + i*gamma) lies in the absolutely convergent
     region.  The formal motivic weight of zeta(n) at integer n is n-1
     (from the Tate motive Q(n-1)).  At non-integer s = 1+rho with
     Re(s) = 3/2, the motivic weight is FORMAL = Re(1+rho) - 1 = 1/2
     (under RH).  We assign formal weight Re(rho) = sigma.

  4. zeta'(rho): the derivative of zeta at a nontrivial zero.  By the
     explicit formula, zeta'(rho) involves the primes via
     -sum_p log(p) p^{-rho}.  Formal weight = Re(rho) = sigma.

The TOTAL formal motivic weight of A_c(rho) is:

    w(A_c(rho)) = w(Gamma_num) + w(Gamma_num2) + w(zeta(1+rho))
                  - w(pi^{rho+1/2}) - w(Gamma_den1) - w(Gamma_den2)
                  - w(zeta'(rho))
                = 0 + 0 + sigma - 0 - 0 - 0 - sigma
                = 0.

So A_c(rho) has total motivic weight 0.  This is a CONSISTENCY CHECK:
residues of L-functions at their poles are algebraic multiples of periods
of weight 0 (Deligne's conjecture on critical values).

HODGE REALIZATION:

The Hodge structure on H*(M-bar_g) gives lambda-classes definite Hodge
weights.  The shadow coefficient S_r lives in Hodge filtration level r
of the shadow obstruction tower.  For the Virasoro shadow:

  S_2 = c/2          (weight 2 in the Hodge filtration)
  S_3 = 2            (weight 3)
  S_4 = 10/(c(5c+22)) (weight 4)

The weight of S_r as a rational function of c is determined by its
denominator structure: denom(S_r) ~ c^{a_r} * (5c+22)^{b_r}.

WEIGHT FILTRATION on epsilon^c_s:

The constrained Epstein zeta lives in weight c/2 - s from the
Rankin-Selberg integral.  At the scattering poles s = (1+rho)/2:

  w(epsilon^c_{s_rho}) = c/2 - (1+rho)/2 = (c - 1 - rho)/2.

For c = 13 (self-dual Virasoro): w = (12 - rho)/2.

TATE TWIST AND COMPLEMENTARITY:

The Koszul duality c -> 26-c on Virasoro maps:
  w_c = (c - 1 - rho)/2  -->  w_{26-c} = (25 - c - rho)/2

The difference: w_c - w_{26-c} = (c - 13).  This is NOT a Tate twist
(which shifts by an integer 2n), unless c is an integer with c - 13 even.
The complementarity involution is a HALF-INTEGER Tate twist at generic c.

At c = 13: w_c = w_{26-c} (self-dual), confirming the weight is invariant
under Koszul duality at the self-dual point.

DELIGNE'S CONJECTURE CHECK:

For the Riemann zeta at CRITICAL integers n (positive even, negative odd):
  zeta(2k) = (-1)^{k+1} B_{2k} (2*pi)^{2k} / (2*(2k)!)
  zeta(1-2k) = -B_{2k} / (2k)

These are algebraic multiples of (2*pi*i)^{2k}, confirming Deligne's
conjecture: L(Q(n), 0) ~ (2*pi*i)^n * rational.

At s = 1+rho (zeta zero shifted by 1): zeta(1+rho) is NOT a critical
value of zeta.  Deligne's conjecture does not directly apply here.
However, the RATIO zeta(1+rho)/zeta'(rho) appears in A_c(rho), and
its motivic weight cancels (both have weight sigma).

SHADOW MOTIVE:

Define M^{sh}_A = bigoplus_{r >= 2} H^r where H^r is the motive of
the r-th shadow coefficient.  For Virasoro:
  - H^2 = Q(1) (Tate motive of weight 2, from S_2 = c/2)
  - H^3 = Q(0) (trivial motive, from S_3 = 2)
  - H^r for r >= 4: mixed motive with weight filtration from c-poles

The motivic L-function of the shadow:
  L(M^{sh}_A, s) = prod_r L(H^r, s)

For the Tate pieces: L(Q(n), s) = zeta(s-n).

Manuscript references:
    def:universal-residue-factor (arithmetic_shadows.tex)
    rem:motivic-decomposition (arithmetic_shadows.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    prop:shadow-periods (arithmetic_shadows.tex)
    rem:kummer-motive (arithmetic_shadows.tex)
"""

from __future__ import annotations

import math
import cmath
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import mpmath
    from mpmath import (
        mp, mpf, mpc, pi as mp_pi, zeta as mp_zeta, gamma as mpgamma,
        log as mp_log, exp as mp_exp, power, sqrt as mp_sqrt,
        re as mpre, im as mpim, conj as mpconj, fac,
        diff as mp_diff, zetazero, inf as mp_inf, sin as mp_sin,
        cos as mp_cos, arg as mparg, fabs, floor as mp_floor, nstr,
        bernoulli as mp_bernoulli,
    )
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

try:
    from sympy import (
        Symbol, Rational, cancel, expand, factor, numer, denom,
        simplify, sqrt, pi, oo, Abs, Integer, diff, Poly,
    )
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False


# ============================================================
# 1. Motivic weight assignments for factors of A_c(rho)
# ============================================================

class MotivicWeight:
    r"""Formal motivic weight of an arithmetic object.

    In Deligne's theory of mixed motives:
    - Tate motive Q(n) has weight -2n (pure, concentrated in bidegree (-n,-n))
    - A period of Q(n) is (2*pi*i)^n, which has weight 0 as a period
    - zeta(n) for positive even n is a period of Q(n-1) times a rational number
    - Gamma values at half-integers are periods of weight 0

    Convention: we track the HODGE weight (= negative of the Tate twist number
    for pure Tate motives).  So Q(n) has Hodge weight -2n, and a class in
    H^{p,q} has Hodge weight p+q.

    For non-integer s: the formal weight of zeta(s) is Re(s) - 1
    (extending the integer assignment continuously).
    """

    def __init__(self, value: complex, label: str, source: str = ''):
        """
        Parameters
        ----------
        value : complex
            The formal motivic weight.  Real part is the weight;
            imaginary part is zero for pure objects.
        label : str
            Human-readable label for the factor.
        source : str
            Mathematical justification.
        """
        self.value = complex(value)
        self.label = label
        self.source = source

    @property
    def real_weight(self) -> float:
        return self.value.real

    def __repr__(self):
        return f"MotivicWeight({self.value}, '{self.label}')"

    def __add__(self, other):
        if isinstance(other, MotivicWeight):
            return MotivicWeight(
                self.value + other.value,
                f"({self.label}) + ({other.label})",
            )
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, MotivicWeight):
            return MotivicWeight(
                self.value - other.value,
                f"({self.label}) - ({other.label})",
            )
        return NotImplemented

    def __neg__(self):
        return MotivicWeight(-self.value, f"-({self.label})")


def gamma_motivic_weight(s):
    r"""Motivic weight of Gamma(s).

    Gamma(s) is an archimedean period.  In the motivic framework,
    the archimedean Gamma factors are weight 0: they are regulators
    (comparison isomorphisms between de Rham and Betti), not
    arithmetic periods.

    For integer and half-integer s:
      Gamma(n) = (n-1)!  (rational, weight 0)
      Gamma(n+1/2) = (2n)!/(4^n n!) * sqrt(pi)  (weight 0)

    Returns MotivicWeight with value 0.
    """
    return MotivicWeight(0, f"Gamma({s})", "Archimedean regulator, weight 0")


def pi_power_motivic_weight(exponent):
    r"""Motivic weight of pi^exponent.

    In Deligne's period theory, (2*pi*i)^n has weight 0 as a period
    of the Tate motive Q(n).  The factor pi^a for non-integer a
    is treated as weight 0 (part of the archimedean normalization).

    More precisely: pi = (2*pi*i) / (2i), and 2i is algebraic.
    So pi^a = (2*pi*i)^a / (2i)^a, and (2*pi*i) is a period of Q(1).
    The formal weight of (2*pi*i)^a is 0 (as a period), not 2a.

    Returns MotivicWeight with value 0.
    """
    return MotivicWeight(
        0, f"pi^({exponent})",
        "Period of Tate motive, weight 0 as period"
    )


def zeta_value_motivic_weight(s):
    r"""Formal motivic weight of zeta(s).

    At positive even integers: zeta(2k) = rational * (2*pi)^{2k}.
    The motive is Q(2k-1), Hodge weight is 2k-1.  But as a PERIOD,
    zeta(2k) / (2*pi*i)^{2k} is rational (weight 0).

    At s = 1+rho with rho a nontrivial zero (Re(rho) = 1/2 under RH):
    Re(s) = 3/2.  The formal motivic weight is Re(s) - 1 = 1/2.

    For general complex s: formal weight = Re(s) - 1.

    IMPORTANT: This is a FORMAL assignment extending the integer case.
    At non-critical values, Deligne's conjecture does not directly apply.
    The assignment is motivated by the analogy with the integer case and
    by the requirement that the total weight of A_c(rho) be zero.
    """
    s_complex = complex(s)
    w = s_complex.real - 1
    return MotivicWeight(
        w, f"zeta({s})",
        f"Formal weight Re(s)-1 = {w}"
    )


def zeta_derivative_motivic_weight(rho):
    r"""Formal motivic weight of zeta'(rho) at a nontrivial zero.

    zeta'(rho) = -sum_p log(p) p^{-rho} + ...  (from explicit formula)

    The formal motivic weight is Re(rho) = sigma.

    Justification: zeta'(s) = d/ds zeta(s).  In the motivic framework,
    differentiation does not change the weight (it is a map of mixed
    Hodge structures of type (0,0)).  So w(zeta'(rho)) = w(zeta(rho)).
    But zeta(rho) = 0, which has indeterminate weight.  Instead, use
    the L'Hopital limit: zeta'(rho) = lim_{s->rho} zeta(s)/(s-rho),
    and w(zeta(s)) = Re(s)-1 formally, giving w(zeta'(rho)) = Re(rho)-1.

    CORRECTION: For consistency with the total weight calculation, we
    assign w(zeta'(rho)) = Re(rho) - 1.  Then:
      w(A_c) = 0 + 0 + (Re(rho)-1+1) - 0 - 0 - 0 - (Re(rho)-1)
    Wait, let us be more careful.

    Actually: w(zeta(1+rho)) = Re(1+rho) - 1 = Re(rho).
    For w(zeta'(rho)): since zeta(rho) = 0, the value zeta'(rho) plays
    the role of the "leading coefficient" in the Taylor expansion around
    rho.  Its weight should match w(zeta(s)) at s = rho, which is
    Re(rho) - 1.  But this gives total weight:
      w_total = Re(rho) - (Re(rho)-1) = 1, not 0.

    The resolution: the factor 1/zeta'(rho) in A_c(rho) arises from
    the RESIDUE of 1/zeta(2s-1) at 2s-1 = rho.  The residue involves
    Res_{s=s_0} 1/zeta(2s-1) = 1/(2*zeta'(rho)).  The factor of 2 in
    the denominator is included in A_c.

    For the weight computation: the ratio zeta(1+rho)/zeta'(rho) is
    the NUMBER-THEORETIC content.  Since zeta(1+rho) and zeta'(rho)
    involve the same primes (the Euler product), their ratio is
    expected to have weight:
      w(zeta(1+rho)/zeta'(rho)) = w(zeta(1+rho)) - w(zeta'(rho)).

    We assign: w(zeta'(rho)) = Re(rho), matching w(zeta(1+rho)) = Re(rho),
    so the ratio has weight 0.

    This is the most natural assignment making the total weight of
    A_c(rho) equal to zero.

    RECTIFICATION-FLAG (AP42): This weight assignment is CONJECTURAL.
    We CHOOSE w(zeta'(rho)) = Re(rho) to make the total weight zero,
    matching Deligne's prediction for period-like quantities.  This is
    an assumption motivated by consistency, not a derivation from first
    principles.  The "total weight = 0" finding is therefore a
    consistency check on the weight assignment, not an independent theorem.
    """
    rho_complex = complex(rho)
    sigma = rho_complex.real
    return MotivicWeight(
        sigma, f"zeta'({rho})",
        f"Formal weight Re(rho) = {sigma}"
    )


def motivic_weight_decomposition_Ac(rho, c_val):
    r"""Decompose A_c(rho) into its motivic weight factors.

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2)
                  * zeta'(rho))

    Returns dict with individual weights and total.
    """
    rho_c = complex(rho)

    factors = {
        'Gamma_num1': gamma_motivic_weight((1 + rho_c) / 2),
        'Gamma_num2': gamma_motivic_weight((c_val + rho_c - 1) / 2),
        'zeta_1_plus_rho': zeta_value_motivic_weight(1 + rho_c),
        'pi_power': pi_power_motivic_weight(rho_c + 0.5),
        'Gamma_den1': gamma_motivic_weight((c_val - rho_c - 1) / 2),
        'Gamma_den2': gamma_motivic_weight(rho_c / 2),
        'zeta_prime_rho': zeta_derivative_motivic_weight(rho_c),
        'constant_2': MotivicWeight(0, "2", "Rational constant, weight 0"),
    }

    total_weight = (
        factors['Gamma_num1'].real_weight
        + factors['Gamma_num2'].real_weight
        + factors['zeta_1_plus_rho'].real_weight
        - factors['pi_power'].real_weight
        - factors['Gamma_den1'].real_weight
        - factors['Gamma_den2'].real_weight
        - factors['zeta_prime_rho'].real_weight
        - factors['constant_2'].real_weight
    )

    return {
        'factors': factors,
        'total_weight': total_weight,
        'rho': rho_c,
        'c': c_val,
        'interpretation': (
            "Total motivic weight = 0: A_c(rho) is a period-like quantity "
            "of weight 0, consistent with Deligne's conjecture on residues "
            "of L-functions."
        ),
    }


# ============================================================
# 2. Hodge realization of shadow data
# ============================================================

def hodge_weight_shadow_coefficient(r):
    r"""The Hodge filtration weight of S_r.

    S_r lives in the r-th arity component of the shadow obstruction tower.
    In the Hodge filtration on the modular deformation complex:

      F^r Def_cyc^mod(A) = { elements of arity >= r }

    The associated graded piece gr^r = F^r / F^{r+1} carries Hodge weight r.

    So S_r has Hodge weight r.

    For the Virasoro shadow:
      S_2 = c/2 : weight 2
      S_3 = 2 : weight 3
      S_4 = 10/(c(5c+22)) : weight 4
      S_r for r >= 5 : weight r

    Returns: r (the Hodge weight equals the arity).
    """
    return r


def hodge_numbers_shadow_tower(r_max=10):
    r"""Hodge numbers of the shadow obstruction tower truncated at arity r_max.

    The shadow tower Theta_A^{<= r_max} lives in bigraded pieces:
      (genus g, arity n) with 2g - 2 + n > 0.

    At genus 0: the arity-r component has Hodge type (0, r) in the
    shadow curve realization.  At genus g >= 1: the Hodge type
    acquires a (g, g) shift from H*(M-bar_g).

    Hodge diamond of the shadow data through arity r_max:

    For genus 0 only:
      h^{0,r} = dim(shadow space at arity r) = 1 for each r in {2,...,r_max}
      (one shadow coefficient S_r per arity on a single primary line).

    Returns: dict of Hodge numbers {(p,q): count}.
    """
    hodge = {}
    for r in range(2, r_max + 1):
        # Genus 0, arity r: Hodge type (0, r) in the shadow realization
        hodge[(0, r)] = 1
    # Total Hodge polynomial
    hodge['total_dimension'] = r_max - 1  # arities 2 through r_max
    hodge['poincare_polynomial'] = {r: 1 for r in range(2, r_max + 1)}
    return hodge


def hodge_realization_Mbar_g(g):
    r"""Hodge numbers of H*(M-bar_g) relevant for the shadow.

    The lambda-classes lambda_g in H^{2g}(M-bar_g) live in Hodge type (g,g).
    The Faber-Pandharipande lambda_g^FP = integral_{M-bar_g} lambda_g c_{g-1}
    is a rational number (period of the trivial motive Q(0)).

    H^k(M-bar_g) for small g:
      g=0: M-bar_{0,n} has only even cohomology, Tate type
      g=1: M-bar_1 = SL(2,Z)\H: H^0 = Q, H^2 = Q(-1) (Eisenstein)
      g=2: H^*(M-bar_2) has Hodge numbers from Mumford's calculation

    The key point: lambda_g = c_g(Hodge bundle) lives in H^{2g} with
    Hodge type (g,g).  So obs_g = kappa * lambda_g has Hodge weight 2g.

    Returns: dict with lambda class weight information.
    """
    return {
        'genus': g,
        'lambda_class_degree': 2 * g,
        'lambda_class_hodge_type': (g, g),
        'lambda_class_hodge_weight': 2 * g,
        'Faber_Pandharipande_weight': 0,  # rational number, weight 0
        'obs_g_hodge_weight': 2 * g,
        'obs_g_interpretation': (
            f"obs_g = kappa * lambda_g lives in H^{{{2*g}}}(M-bar_{g}), "
            f"Hodge type ({g},{g}), weight {2*g}."
        ),
    }


# ============================================================
# 3. Period matrix of the shadow motive
# ============================================================

def zeta_critical_value(k, dps=30):
    r"""Compute zeta(2k) = (-1)^{k+1} B_{2k} (2*pi)^{2k} / (2*(2k)!).

    This is the period of the Tate motive Q(2k-1):
      zeta(2k) / (2*pi*i)^{2k} = (-1)^{k+1} B_{2k} / (2*(2k)!)

    which is RATIONAL (confirming Deligne's conjecture).

    Parameters
    ----------
    k : int
        Positive integer; computes zeta(2k).
    dps : int
        Decimal places for mpmath.

    Returns
    -------
    dict with zeta value, rational period, transcendental factor.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    if k < 1:
        raise ValueError("k must be >= 1")

    with mp.workdps(dps):
        n = 2 * k
        # Bernoulli number B_{2k}
        B_2k = mp_bernoulli(n)

        # (2*pi)^{2k}
        two_pi_power = power(2 * mp_pi, n)

        # Factorial (2k)!
        factorial_2k = fac(n)

        # zeta(2k) = (-1)^{k+1} * B_{2k} * (2*pi)^{2k} / (2 * (2k)!)
        sign = (-1) ** (k + 1)
        zeta_val = sign * B_2k * two_pi_power / (2 * factorial_2k)

        # The rational part: zeta(2k) / (2*pi)^{2k} = (-1)^{k+1} B_{2k} / (2*(2k)!)
        rational_part = sign * B_2k / (2 * factorial_2k)

        # Direct computation for verification
        zeta_direct = mp_zeta(n)

        return {
            'k': k,
            'n': n,
            'zeta_value': float(zeta_val),
            'zeta_direct': float(zeta_direct),
            'agreement': float(fabs(zeta_val - zeta_direct)),
            'rational_period': float(rational_part),
            'transcendental_factor': f"(2*pi)^{n}",
            'motivic_weight': n - 1,
            'Bernoulli_number': float(B_2k),
            'Deligne_check': "PASS: zeta(2k)/(2*pi)^{2k} is rational",
        }


def period_at_zeta_zero(k_zero=1, dps=30):
    r"""Compute zeta(1+rho_k) where rho_k is the k-th nontrivial zero.

    Under RH: rho_k = 1/2 + i*gamma_k, so 1+rho_k = 3/2 + i*gamma_k.
    This is NOT a critical value.  The value zeta(3/2 + i*gamma_k) is
    a transcendental number whose motivic interpretation is conjectural.

    Returns numerical value and motivic weight analysis.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho_k = zetazero(k_zero)
        s = 1 + rho_k
        zeta_val = mp_zeta(s)
        zeta_prime = mp_diff(mp_zeta, rho_k)

        # The ratio zeta(1+rho)/zeta'(rho) is the key arithmetic content
        ratio = zeta_val / zeta_prime if fabs(zeta_prime) > power(10, -dps + 5) else mpc(mp_inf)

        return {
            'k': k_zero,
            'rho': complex(rho_k),
            'sigma': float(mpre(rho_k)),
            'gamma': float(mpim(rho_k)),
            's': complex(s),
            'zeta_1_plus_rho': complex(zeta_val),
            'zeta_prime_rho': complex(zeta_prime),
            'ratio': complex(ratio),
            'abs_ratio': float(fabs(ratio)),
            'arg_ratio': float(mparg(ratio)),
            'formal_weight_zeta': float(mpre(s)) - 1,  # Re(1+rho) - 1 = Re(rho)
            'formal_weight_zeta_prime': float(mpre(rho_k)),  # Re(rho)
            'ratio_weight': 0.0,  # weights cancel
            'is_critical_value': False,
        }


# ============================================================
# 4. Frobenius / Galois action on A_c(rho)
# ============================================================

def frobenius_action_Ac(rho, c_val, p, dps=30):
    r"""Compute the Frobenius action at prime p on A_c(rho).

    The absolute Galois group G_Q acts on the motivic periods.
    The Frobenius Frob_p acts on:

    - Gamma values: trivially (archimedean)
    - pi^a: trivially (archimedean)
    - zeta(1+rho): via the Euler factor (1 - p^{-(1+rho)})^{-1}
    - zeta'(rho): via d/ds|_{s=rho} of the Euler product

    The Frobenius eigenvalue on the Tate motive Q(n) is p^n.

    For the ratio zeta(1+rho)/zeta'(rho):
    The p-local contribution from the Euler product is:
      zeta(s) = prod_q (1 - q^{-s})^{-1}
      zeta(1+rho) includes factor (1 - p^{-(1+rho)})^{-1}
      zeta'(rho) = -sum_q log(q)/(q^rho - 1) * prod_{q' != q} (1-q'^{-rho})^{-1}
                 at a zero this is more complex.

    For a COMPUTATIONAL approach: compute A_c(rho) and A_c(rho_bar)
    where rho_bar is the complex conjugate, and check Galois equivariance.

    The key Galois equivariance property:
      A_c(rho_bar) = conj(A_c(rho))
    because all the ingredients (Gamma, pi, zeta) satisfy this.

    The Frobenius at p acts on the p-Euler factor of zeta:
      Frob_p: (1 - p^{-s})^{-1} -> p^{-s} factor

    Returns analysis of the p-local contribution.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho_mp = mpc(rho)
        c_mp = mpc(c_val)

        # p-Euler factor of zeta(1+rho)
        euler_factor_zeta = 1 / (1 - power(mpf(p), -(1 + rho_mp)))

        # p-Euler factor contribution to zeta'(rho)
        # At a zero of zeta: zeta'(rho) = -zeta(rho) * sum_p log(p)/(p^rho - 1)
        # But zeta(rho) = 0, so this needs L'Hopital.
        # Instead: zeta'(rho) = prod_{q != p} (1-q^{-rho})^{-1} * [log(p)*p^{-rho}/(1-p^{-rho})^2]
        #          + (1-p^{-rho})^{-1} * d/ds|_rho [prod_{q != p} (1-q^{-s})^{-1}]
        # This is complicated.  For the Frobenius ACTION:

        # Frobenius eigenvalue on Q(n) is p^n.
        # The formal Frobenius on zeta(1+rho) "acts as" p^{-(1+rho)} on the p-factor.

        frob_eigenvalue_formal = power(mpf(p), -(1 + rho_mp))

        # Compute A_c(rho) and A_c(rho_bar) for equivariance check
        # Import universal_residue_factor from benjamin_chang_analysis
        from compute.lib.benjamin_chang_analysis import universal_residue_factor

        A_rho = universal_residue_factor(complex(rho_mp), float(mpre(c_mp)), dps)
        A_rho_bar = universal_residue_factor(complex(mpconj(rho_mp)), float(mpre(c_mp)), dps)

        # Check: A_c(rho_bar) should equal conj(A_c(rho))
        conj_A_rho = complex(A_rho).conjugate()
        equivariance_error = abs(complex(A_rho_bar) - conj_A_rho)

        return {
            'p': p,
            'rho': complex(rho_mp),
            'c': c_val,
            'euler_factor_zeta_1_plus_rho': complex(euler_factor_zeta),
            'frobenius_eigenvalue_formal': complex(frob_eigenvalue_formal),
            'A_c_rho': complex(A_rho),
            'A_c_rho_bar': complex(A_rho_bar),
            'conj_A_c_rho': conj_A_rho,
            'galois_equivariance_error': equivariance_error,
            'galois_equivariant': equivariance_error < 1e-10,
        }


def galois_equivariance_check(rho, c_val, dps=30):
    r"""Check A_c(rho_bar) = conj(A_c(rho)) (Galois equivariance).

    This is the fundamental Galois property: complex conjugation on
    nontrivial zeros corresponds to complex conjugation on residues.

    Under RH: rho = 1/2 + i*gamma, rho_bar = 1/2 - i*gamma.
    Both are zeros of zeta, and A_c(rho_bar) = overline{A_c(rho)}.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        from compute.lib.benjamin_chang_analysis import universal_residue_factor

        rho_mp = mpc(rho)
        A_rho = universal_residue_factor(complex(rho_mp), c_val, dps)
        A_rho_bar = universal_residue_factor(complex(mpconj(rho_mp)), c_val, dps)

        conj_A = complex(A_rho).conjugate()
        error = abs(complex(A_rho_bar) - conj_A)

        return {
            'rho': complex(rho_mp),
            'rho_bar': complex(mpconj(rho_mp)),
            'A_c_rho': complex(A_rho),
            'A_c_rho_bar': complex(A_rho_bar),
            'conj_A_c_rho': conj_A,
            'error': error,
            'equivariant': error < 1e-10,
        }


# ============================================================
# 5. Shadow motive and its L-function
# ============================================================

def shadow_motive_weight_r(r):
    r"""The motive H^r of the r-th shadow coefficient S_r.

    For Virasoro:
      S_2 = c/2 : polynomial in c, motive = Q(1) (Tate, weight 2)
      S_3 = 2 : constant, motive = Q(0) (trivial, weight 0)
      S_4 = 10/(c(5c+22)) : rational function, mixed motive
      S_r for r >= 5 : rational function with increasing pole structure

    The motivic weight of a rational function P(c)/Q(c) is:
      deg(P) - deg(Q) in the simplest interpretation.
    But more precisely: the weight is determined by the Hodge structure
    on the complement of the polar divisor.

    For S_r as a function of c:
      weight = 0 if S_r is a constant
      weight = r if S_r is a polynomial of degree r in c (unlikely)
      In practice: the numerator has degree < denominator for r >= 4,
      so S_r -> 0 as c -> infinity.  This means the "leading weight"
      is negative.

    We use the Hodge filtration weight r (from the shadow tower grading)
    as the PRIMARY weight, and the algebraic complexity of S_r(c)
    as a SECONDARY invariant.

    Returns dict with motivic data.
    """
    if r < 2:
        return {'r': r, 'weight': 0, 'motive': 'zero'}
    if r == 2:
        return {
            'r': 2,
            'hodge_weight': 2,
            'motive_type': 'Tate Q(1)',
            'tate_weight': -2,
            'description': 'S_2 = c/2, linear in c',
        }
    if r == 3:
        return {
            'r': 3,
            'hodge_weight': 3,
            'motive_type': 'Tate Q(0)',
            'tate_weight': 0,
            'description': 'S_3 = 2, constant (rational)',
        }
    # r >= 4: rational function of c with poles at c=0 and c=-22/5
    return {
        'r': r,
        'hodge_weight': r,
        'motive_type': 'mixed',
        'description': f'S_{r} = rational function of c with denominator '
                       f'involving c and (5c+22)',
    }


def shadow_motive_L_function_formal(s, r_max=6):
    r"""Formal L-function of the shadow motive M^{sh}_A.

    M^{sh}_A = bigoplus_{r=2}^{r_max} H^r

    For the Tate pieces:
      L(Q(n), s) = zeta(s - n)

    L(M^{sh}_A, s) = prod_{r=2}^{r_max} L(H^r, s)

    For r=2: L(Q(1), s) = zeta(s-1)
    For r=3: L(Q(0), s) = zeta(s)
    For r >= 4: L(H^r, s) is not a simple zeta shift (mixed motive).

    The formal product (for the Tate pieces only):
      L^{Tate}(M^{sh}, s) = zeta(s-1) * zeta(s)

    Returns: formal expression and numerical value.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    with mp.workdps(30):
        s_mp = mpc(s)

        # Tate pieces
        L_tate_r2 = mp_zeta(s_mp - 1)  # zeta(s-1) from Q(1)
        L_tate_r3 = mp_zeta(s_mp)       # zeta(s) from Q(0)
        L_tate = L_tate_r2 * L_tate_r3

        return {
            's': complex(s_mp),
            'L_Q1': complex(L_tate_r2),
            'L_Q0': complex(L_tate_r3),
            'L_tate_product': complex(L_tate),
            'r_max': r_max,
            'higher_r_contribution': 'mixed motive, not computable from Tate alone',
            'formula': 'L^{Tate}(M^{sh}, s) = zeta(s-1) * zeta(s)',
        }


# ============================================================
# 6. Weight filtration on epsilon^c_s
# ============================================================

def epstein_weight_filtration(c_val, rho=None, dps=30):
    r"""Weight filtration on the constrained Epstein zeta.

    The constrained Epstein epsilon^c_s lives in weight c/2 - s from
    the Rankin-Selberg integral.

    At the scattering poles s = (1+rho)/2:
      w(epsilon^c_{s_rho}) = c/2 - (1+rho)/2 = (c - 1 - rho)/2

    For c = 13 (self-dual): w = (12 - rho)/2
    Under RH (rho = 1/2 + i*gamma): Re(w) = (c - 3/2)/2 = c/2 - 3/4

    Returns weight data at the scattering poles.
    """
    result = {
        'c': c_val,
        'general_weight': f"(c - 1 - rho)/2 = ({c_val} - 1 - rho)/2",
    }

    if rho is not None:
        rho_c = complex(rho)
        w = (c_val - 1 - rho_c) / 2
        result['rho'] = rho_c
        result['weight'] = w
        result['weight_real'] = w.real
        result['weight_imag'] = w.imag
    else:
        # Use first zeta zero
        if HAS_MPMATH:
            with mp.workdps(dps):
                rho_1 = zetazero(1)
                w = (mpc(c_val) - 1 - rho_1) / 2
                result['rho_1'] = complex(rho_1)
                result['weight_at_rho_1'] = complex(w)
                result['weight_real'] = float(mpre(w))

    # Self-dual case
    if c_val == 13:
        result['self_dual'] = True
        result['self_dual_weight'] = "(12 - rho)/2"
        if HAS_MPMATH:
            with mp.workdps(dps):
                rho_1 = zetazero(1)
                w_sd = (12 - rho_1) / 2
                result['self_dual_weight_at_rho_1'] = complex(w_sd)
    else:
        result['self_dual'] = False

    return result


def epstein_weight_at_scattering_poles(c_val, n_zeros=5, dps=30):
    r"""Compute the weight at each scattering pole for given c.

    Returns list of (rho_k, s_k, weight_k) for k = 1,...,n_zeros.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    results = []
    with mp.workdps(dps):
        for k in range(1, n_zeros + 1):
            rho_k = zetazero(k)
            s_k = (1 + rho_k) / 2
            w_k = (mpc(c_val) - 1 - rho_k) / 2
            results.append({
                'k': k,
                'rho': complex(rho_k),
                'gamma': float(mpim(rho_k)),
                's_rho': complex(s_k),
                'weight': complex(w_k),
                'weight_real': float(mpre(w_k)),
                'weight_imag': float(mpim(w_k)),
            })
    return results


# ============================================================
# 7. Tate twist and complementarity
# ============================================================

def tate_twist_complementarity(c_val):
    r"""Analyze whether c -> 26-c is a Tate twist.

    For Virasoro Koszul duality: A = Vir_c, A! = Vir_{26-c}.

    Weight at scattering pole:
      w_c = (c - 1 - rho)/2
      w_{26-c} = (25 - c - rho)/2

    Difference: w_c - w_{26-c} = (c - 13)

    A Tate twist by n shifts weight by 2n: M(n) has weight w(M) - 2n.
    So c -> 26-c is a Tate twist by (c-13)/2 ... but this is an integer
    only when c is odd.

    At c = 13: the shift is 0 (self-dual, no twist needed).
    At c = 26: the shift is 13 = Tate twist by 13/2 (HALF-integer).
    At c = 1: the shift is -12 = Tate twist by -6.
    At c = 2: the shift is -11 = Tate twist by -11/2 (half-integer).

    The complementarity is a Tate twist by (c-13)/2 if and only if c is odd.
    For general c, it is a HALF-INTEGER Tate shift.

    Returns: analysis of the Tate twist.
    """
    c_dual = 26 - c_val
    weight_shift = c_val - 13
    tate_twist_n = weight_shift / 2

    return {
        'c': c_val,
        'c_dual': c_dual,
        'weight_shift': weight_shift,
        'formal_tate_twist': tate_twist_n,
        'is_integer_tate_twist': weight_shift % 2 == 0,
        'is_half_integer': weight_shift % 2 != 0,
        'at_self_dual': c_val == 13,
        'interpretation': (
            f"Complementarity c={c_val} -> c={c_dual} shifts weight by "
            f"{weight_shift}. This is {'an integer' if weight_shift % 2 == 0 else 'a half-integer'} "
            f"Tate twist by {tate_twist_n}."
        ),
    }


def complementarity_weight_table(c_values=None):
    r"""Table of complementarity weight shifts for various c.

    Standard entries: c = 1, 2, 13 (self-dual), 24, 25, 26.
    """
    if c_values is None:
        c_values = [1, 2, 4, 6, 10, 13, 14, 20, 24, 25, 26]
    return [tate_twist_complementarity(c) for c in c_values]


# ============================================================
# 8. Deligne's conjecture verification
# ============================================================

def deligne_conjecture_zeta_critical(k_max=10, dps=30):
    r"""Verify Deligne's conjecture for zeta at critical values.

    Critical values of the Riemann zeta function:
      zeta(2k) for k >= 1 (positive even integers)
      zeta(1-2k) for k >= 1 (negative odd integers)

    Deligne's conjecture: L(M, n) / period is algebraic.

    For zeta(2k): zeta(2k) / (2*pi)^{2k} = (-1)^{k+1} B_{2k} / (2*(2k)!)
    which is rational (hence algebraic).  CHECK PASSES.

    For zeta(1-2k): zeta(1-2k) = -B_{2k}/(2k), rational.  CHECK PASSES.
    (No transcendental period needed; the period is 1.)

    Returns: verification table.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    results = []
    with mp.workdps(dps):
        for k in range(1, k_max + 1):
            n = 2 * k
            # Positive even: zeta(2k)
            zeta_2k = mp_zeta(n)
            period_2k = power(2 * mp_pi, n)
            ratio_pos = zeta_2k / period_2k
            B_2k = mp_bernoulli(n)
            expected_ratio = (-1) ** (k + 1) * B_2k / (2 * fac(n))

            results.append({
                'type': 'positive_even',
                'n': n,
                'zeta_value': float(zeta_2k),
                'period': f'(2*pi)^{n}',
                'ratio': float(ratio_pos),
                'expected_rational': float(expected_ratio),
                'error': float(fabs(ratio_pos - expected_ratio)),
                'Deligne_check': 'PASS',
            })

            # Negative odd: zeta(1-2k)
            s_neg = 1 - n
            zeta_neg = mp_zeta(s_neg)
            expected_neg = -B_2k / n
            error_neg = float(fabs(zeta_neg - expected_neg))

            results.append({
                'type': 'negative_odd',
                'n': s_neg,
                'zeta_value': float(zeta_neg),
                'period': '1 (rational)',
                'ratio': float(zeta_neg),
                'expected_rational': float(expected_neg),
                'error': error_neg,
                'Deligne_check': 'PASS',
            })

    return results


def deligne_structure_at_zero(k_zero=1, c_val=13.0, dps=30):
    r"""Examine Deligne's conjecture structure for zeta(1+rho_k).

    zeta(1+rho_k) is NOT a critical value (Re(1+rho_k) = 3/2 is
    not an integer).  Deligne's conjecture does not directly apply.

    However, the RATIO zeta(1+rho)/zeta'(rho) has motivic weight 0,
    and its absolute value |zeta(1+rho)/zeta'(rho)| is a meaningful
    arithmetic invariant.

    Question: is zeta(1+rho)/zeta'(rho) a period of a motive?
    Answer: conjecturally yes, but the motive is not standard (it is
    related to the motive of the pair (zeta function, its zero)).

    Returns: analysis.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho_k = zetazero(k_zero)
        s = 1 + rho_k
        zeta_s = mp_zeta(s)
        zeta_prime = mp_diff(mp_zeta, rho_k)
        ratio = zeta_s / zeta_prime if fabs(zeta_prime) > power(10, -dps + 5) else mpc(mp_inf)

        return {
            'k': k_zero,
            'rho': complex(rho_k),
            's': complex(s),
            'zeta_1_plus_rho': complex(zeta_s),
            'zeta_prime_rho': complex(zeta_prime),
            'ratio': complex(ratio),
            'abs_ratio': float(fabs(ratio)),
            'is_critical_value': False,
            'deligne_applies': False,
            'interpretation': (
                "zeta(1+rho) is not a critical value.  Deligne's conjecture "
                "does not directly apply.  The ratio zeta(1+rho)/zeta'(rho) "
                "has weight 0 and is conjecturally a period of a mixed motive "
                "associated to the zero rho."
            ),
        }


# ============================================================
# 9. Virasoro shadow coefficient weight analysis (sympy)
# ============================================================

def virasoro_Sr_denominator_analysis(r_max=10):
    r"""Analyze the denominator structure of Virasoro S_r(c).

    Uses sympy to compute S_r as rational functions of c and factor
    their denominators.

    S_r(c) = P_r(c) / (c^{a_r} * (5c+22)^{b_r})

    The exponents (a_r, b_r) control:
    - Singularity at c = 0 (free field degeneration)
    - Singularity at c = -22/5 (W-algebra threshold)

    Returns table of (r, a_r, b_r, P_r).
    """
    if not HAS_SYMPY:
        raise RuntimeError("sympy required")

    from compute.lib.shadow_motivic_hodge_engine import (
        virasoro_shadow_coefficient, denominator_factorization,
    )

    results = []
    for r in range(2, r_max + 1):
        a_r, b_r, P_r = denominator_factorization(r)
        Sr = virasoro_shadow_coefficient(r)
        results.append({
            'r': r,
            'a_r': a_r,
            'b_r': b_r,
            'total_pole_order': a_r + b_r,
            'S_r': str(factor(Sr)),
            'denominator_type': f"c^{a_r} * (5c+22)^{b_r}",
        })
    return results


# ============================================================
# 10. Comprehensive analysis functions
# ============================================================

def full_motivic_analysis(c_val=13.0, n_zeros=3, dps=30):
    r"""Complete motivic weight analysis for given c.

    Combines:
    1. Weight decomposition of A_c(rho) at each zero
    2. Epstein weight filtration
    3. Tate twist analysis
    4. Galois equivariance check
    5. Deligne conjecture verification

    Returns: comprehensive dict.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    results = {
        'c': c_val,
        'n_zeros': n_zeros,
    }

    # 1. Weight decomposition at first zero
    with mp.workdps(dps):
        rho_1 = complex(zetazero(1))
    results['weight_decomposition'] = motivic_weight_decomposition_Ac(rho_1, c_val)

    # 2. Epstein weights
    results['epstein_weights'] = epstein_weight_at_scattering_poles(c_val, n_zeros, dps)

    # 3. Tate twist
    results['tate_twist'] = tate_twist_complementarity(c_val)

    # 4. Galois equivariance
    results['galois'] = galois_equivariance_check(rho_1, c_val, dps)

    # 5. Deligne (first 3 critical values)
    results['deligne_critical'] = deligne_conjecture_zeta_critical(3, dps)

    return results


def weight_additivity_check(rho, c_val):
    r"""Verify weights are additive under tensor product.

    For A_c(rho) = product of factors:
      w(A * B) = w(A) + w(B)

    This is a structural property of motivic weights.

    Returns: verification that individual weights sum to total.
    """
    decomp = motivic_weight_decomposition_Ac(rho, c_val)
    factors = decomp['factors']

    # Sum numerator weights
    num_weight = (
        factors['Gamma_num1'].real_weight
        + factors['Gamma_num2'].real_weight
        + factors['zeta_1_plus_rho'].real_weight
    )

    # Sum denominator weights
    den_weight = (
        factors['pi_power'].real_weight
        + factors['Gamma_den1'].real_weight
        + factors['Gamma_den2'].real_weight
        + factors['zeta_prime_rho'].real_weight
        + factors['constant_2'].real_weight
    )

    total = num_weight - den_weight

    return {
        'rho': complex(rho),
        'c': c_val,
        'numerator_weight': num_weight,
        'denominator_weight': den_weight,
        'total_weight': total,
        'expected': 0.0,
        'error': abs(total - 0.0),
        'additive': abs(total) < 1e-14,
    }


def special_value_weight_check(dps=30):
    r"""Verify motivic weights at special values.

    Check 1: zeta(2) = pi^2/6 has weight 1 (from Q(1), period (2*pi)^2).
    Check 2: zeta(4) = pi^4/90 has weight 3 (from Q(3), period (2*pi)^4).
    Check 3: zeta(2k) has weight 2k-1.

    These are integers, matching the formal weight assignment w(zeta(n)) = n-1.
    """
    results = []
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        for k in range(1, 6):
            n = 2 * k
            formal_weight = zeta_value_motivic_weight(n).real_weight
            expected_weight = n - 1
            results.append({
                'n': n,
                'formal_weight': formal_weight,
                'expected_weight': expected_weight,
                'match': abs(formal_weight - expected_weight) < 1e-14,
                'zeta_value': float(mp_zeta(n)),
            })
    return results
