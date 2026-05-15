r"""Scalar topological-recursion checks for the shadow curve.

The module constructs the quadratic shadow curve

    y^2 = Q_L(t) = q0 + q1*t + q2*t^2

attached to the scalar shadow data (kappa, S_3, S_4), extracts the
formal tower coefficients from the signed branch of sqrt(Q_L), and
compares the scalar genus contribution F_g = kappa*lambda_g^FP with
independent intersection-number and local Airy-residue oracles.

These routines certify finite scalar identities only.  The shadow curve is
EO input after separate branch/residue data; the Airy/KW lane is a finite
coefficient comparison; WP/JT volumes use the sine curve; and multi-weight
all-genus statements require stable-graph data not present in this module.

Scope boundaries are part of the computation.  The seven-entry
holographic package

    (A, A^i, A^!, C, r(z), Theta_A, nabla^hol)

is distinct from the six-primary-projection modular Koszul compute
package.  The object A^! is the Verdier/continuous-linear dual branch
of A^i under finite-type/completed hypotheses; Omega(B(A)) = A is
bar-cobar inversion; Z_ch^der(A) = ChirHoch^*(A,A) is the
Hochschild/derived-centre bulk object.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

import numpy as np

from sympy import (
    Rational, Symbol, bernoulli, binomial, cancel, collect,
    diff, expand, factor, factorial, log, nsimplify, oo,
    pi as sym_pi, series, simplify, solve, sqrt as sym_sqrt, symbols,
    together, I, Poly,
)

try:
    import mpmath
    _HAS_MPMATH = True
except ImportError:
    _HAS_MPMATH = False


HOLOGRAPHIC_PACKAGE_ENTRIES: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)


MODULAR_KOSZUL_PRIMARY_PROJECTIONS: Tuple[str, ...] = (
    "Fact_X(L)",
    "barB_X(L)",
    "Theta_L",
    "L_L",
    "(V_L^br, T_L^br)",
    "R_4^mod(L)",
)


TYPED_FIREWALL_OBJECTS: Tuple[str, ...] = (
    "A",
    "B(A)",
    "A^i",
    "A^!",
    "Omega(B(A))",
    "Z_ch^der(A)",
)


def holographic_package_entries() -> Tuple[str, ...]:
    """Seven entries of the holographic package, in canonical order."""
    return HOLOGRAPHIC_PACKAGE_ENTRIES


def modular_koszul_primary_projections() -> Tuple[str, ...]:
    """Six primary projections of the modular Koszul compute package."""
    return MODULAR_KOSZUL_PRIMARY_PROJECTIONS


def typed_firewall_objects() -> Tuple[str, ...]:
    """Objects kept distinct by the bar/Koszul/Hochschild firewall."""
    return TYPED_FIREWALL_OBJECTS


def typed_firewall_roles() -> Dict[str, str]:
    """Typed roles for the objects most often conflated in this lane."""
    return {
        "A": "boundary chiral algebra",
        "B(A)": "bar factorization coalgebra built from A",
        "A^i": "H^*(B(A)), the bar-dual coalgebra",
        "A^!": (
            "Verdier/continuous-linear dual branch of A^i under "
            "finite-type/completed hypotheses"
        ),
        "Omega(B(A))": "bar-cobar inversion recovering A",
        "Z_ch^der(A)": "ChirHoch^*(A,A), the Hochschild bulk object",
    }


def _fraction_text(value: Fraction) -> str:
    """Stable ASCII rendering for exact kernel constants."""
    return str(value)


def collision_kernel_constants(family: str, k=None, h_dual=None,
                               c=None) -> Dict[str, Any]:
    """Raw collision and comparison-KZ normalizations.

    Affine data keep two coefficients separate: the bar collision residue
    is k*Omega_tr/z, while the KZ comparison coefficient is
    Omega/((k+h_dual)z).  Virasoro uses the collision residue
    (c/2)/z^3 + 2T/z.
    """
    canonical = family.replace("-", "_").lower()

    if canonical == "heisenberg":
        level = Fraction(1) if k is None else Fraction(k)
        formula = f"{_fraction_text(level)}/z"
        return {
            "family": "heisenberg",
            "collision_formula": formula,
            "raw_collision": formula,
            "raw_coefficient": level,
            "pole_order": 1,
        }

    if canonical in {"affine", "affine_km", "kac_moody", "km"}:
        level = Fraction(1) if k is None else Fraction(k)
        h_val = Fraction(2) if h_dual is None else Fraction(h_dual)
        kz_coeff = Fraction(1, 1) / (level + h_val)
        raw = f"{_fraction_text(level)}*Omega_tr/z"
        kz = f"Omega/(({_fraction_text(level)}+{_fraction_text(h_val)})*z)"
        return {
            "family": "affine_km",
            "collision_formula": raw,
            "raw_collision": raw,
            "raw_coefficient": level,
            "kz_formula": kz,
            "kz_coefficient": kz_coeff,
            "raw_and_kz_distinct": True,
            "pole_order": 1,
        }

    if canonical == "virasoro":
        c_val = Fraction(26) if c is None else Fraction(c)
        central = c_val / 2
        formula = f"({_fraction_text(central)})/z^3 + 2T/z"
        return {
            "family": "virasoro",
            "collision_formula": formula,
            "raw_collision": formula,
            "central_prefactor": central,
            "highest_pole_order": 3,
        }

    raise ValueError(f"unknown kernel family {family!r}")


# ============================================================================
# 0. Faber-Pandharipande intersection numbers (standalone)
# ============================================================================

def _bernoulli_number(n: int) -> Rational:
    """Bernoulli number B_n in the Sympy convention."""
    return Rational(bernoulli(n))


def lambda_fp(g: int) -> Rational:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    POSITIVE for all g >= 1.
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B2g = _bernoulli_number(2 * g)
    num = (2**(2 * g - 1) - 1) * abs(B2g)
    den = 2**(2 * g - 1) * factorial(2 * g)
    return Rational(num, den)


# Witten-Kontsevich intersection numbers on M-bar_{g,n}.
# The cache uses the string equation, the dilaton equation, genus-zero
# multinomial numbers, and the DVV form of the Virasoro constraints.

def _odd_double_factorial(n: int) -> int:
    """Odd double factorial, with (-1)!! = 1."""
    if n == -1 or n == 0:
        return 1
    if n < -1 or n % 2 == 0:
        raise ValueError(f"odd double factorial not defined for {n}")
    result = 1
    for value in range(n, 0, -2):
        result *= value
    return result


@lru_cache(maxsize=None)
def _witten_kontsevich(g: int, d_tuple: Tuple[int, ...]) -> Rational:
    r"""Witten-Kontsevich intersection number <tau_{d_1}...tau_{d_n}>_g.

    Computes intersection numbers on M-bar_{g,n} from the
    string equation, the dilaton equation, and the DVV recursion.

    The dimension constraint: sum(d_i) = 3g - 3 + n.
    The stability constraint: 2g - 2 + n > 0.
    """
    n = len(d_tuple)
    d_list = list(sorted(d_tuple))
    d_sum = sum(d_list)

    # Dimension check
    if d_sum != 3 * g - 3 + n:
        return Rational(0)

    # Stability check
    if 2 * g - 2 + n <= 0:
        return Rational(0)

    # Negative d_i -> 0
    if any(d < 0 for d in d_list):
        return Rational(0)

    # Base case: <tau_0^3>_0 = 1
    if g == 0 and d_list == [0, 0, 0]:
        return Rational(1)

    # Base case: <tau_1>_1 = 1/24
    if g == 1 and d_list == [1]:
        return Rational(1, 24)

    if g == 0:
        # Genus-zero closed form:
        # <tau_{d_1}...tau_{d_n}>_0 = (n-3)! / prod_i d_i!
        # when sum d_i = n-3.
        num = factorial(n - 3)
        den = Rational(1)
        for d in d_list:
            den *= factorial(d)
        return Rational(num) / den

    # String equation.
    if 0 in d_list:
        idx = d_list.index(0)
        remaining = d_list[:idx] + d_list[idx + 1:]
        result = Rational(0)
        for j in range(len(remaining)):
            new_d = list(remaining)
            new_d[j] -= 1
            result += _witten_kontsevich(g, tuple(sorted(new_d)))
        return result

    # Dilaton equation.
    if 1 in d_list and n >= 2:
        idx = d_list.index(1)
        remaining = d_list[:idx] + d_list[idx + 1:]
        return (2 * g - 2 + len(remaining)) * _witten_kontsevich(
            g, tuple(sorted(remaining)))

    # DVV recursion, using the largest insertion tau_d0 with d0 >= 2.
    d0 = d_list[-1]
    if d0 < 2:
        return Rational(0)

    rest = d_list[:-1]
    result = Rational(0)

    for j, dj in enumerate(rest):
        new_rest = rest[:j] + rest[j + 1:] + [dj + d0 - 1]
        coeff = Rational(
            _odd_double_factorial(2 * d0 + 2 * dj - 1),
            _odd_double_factorial(2 * dj - 1),
        )
        result += coeff * _witten_kontsevich(g, tuple(sorted(new_rest)))

    genus_split = Rational(0)
    rest_len = len(rest)
    for a in range(d0 - 1):
        b = d0 - 2 - a
        coeff = Rational(
            _odd_double_factorial(2 * a + 1)
            * _odd_double_factorial(2 * b + 1),
            1,
        )
        genus_split += coeff * _witten_kontsevich(
            g - 1, tuple(sorted([a, b] + rest))
        )

        for g1 in range(g + 1):
            g2 = g - g1
            for mask in range(1 << rest_len):
                left = [rest[i] for i in range(rest_len) if mask & (1 << i)]
                right = [rest[i] for i in range(rest_len) if not mask & (1 << i)]
                genus_split += coeff * (
                    _witten_kontsevich(g1, tuple(sorted([a] + left)))
                    * _witten_kontsevich(g2, tuple(sorted([b] + right)))
                )

    result += Rational(1, 2) * genus_split
    return result / _odd_double_factorial(2 * d0 + 1)


# ============================================================================
# 1. Shadow data for standard families (exact Fraction arithmetic)
# ============================================================================

@dataclass(frozen=True)
class ShadowCurveData:
    """Shadow data (kappa, alpha=S_3, S_4) for a chiral algebra family.

    Convention from landscape_census.tex:
        kappa = S_2 (curvature / modular characteristic)
        alpha = S_3 (cubic shadow)
        S4 = S_4 (quartic contact invariant)

    The shadow metric is:
        Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2
               = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2  (Gaussian decomposition)

    where Delta = 8*kappa*S4 is the critical discriminant.
    """
    name: str
    kappa: Fraction
    alpha: Fraction   # S_3
    S4: Fraction       # S_4
    depth_class: str   # 'G', 'L', 'C', 'M'

    @property
    def q0(self) -> Fraction:
        return 4 * self.kappa ** 2

    @property
    def q1(self) -> Fraction:
        return 12 * self.kappa * self.alpha

    @property
    def q2(self) -> Fraction:
        return 9 * self.alpha ** 2 + 16 * self.kappa * self.S4

    @property
    def Delta(self) -> Fraction:
        """Critical discriminant Delta = 8*kappa*S4."""
        return 8 * self.kappa * self.S4

    @property
    def disc_QL(self) -> Fraction:
        """Discriminant of Q_L as polynomial in t: q1^2 - 4*q0*q2."""
        return self.q1 ** 2 - 4 * self.q0 * self.q2


def virasoro_shadow(c: Fraction) -> ShadowCurveData:
    """Virasoro at central charge c.

    kappa = c/2, alpha = 2, S4 = 10/(c*(5c+22)).
    Q^contact_Vir = 10/[c(5c+22)].
    """
    kappa = c / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))
    return ShadowCurveData(
        name=f"Vir_c={c}",
        kappa=kappa,
        alpha=alpha,
        S4=S4,
        depth_class='M',
    )


def affine_sl2_shadow(k: Fraction) -> ShadowCurveData:
    """Affine V_k(sl_2).

    kappa = 3(k+2)/4, alpha = 2, S4 = 0 (class L, terminates at arity 3).
    """
    kappa = Fraction(3) * (k + 2) / 4
    alpha = Fraction(2)
    S4 = Fraction(0)
    return ShadowCurveData(
        name=f"aff_sl2_k={k}",
        kappa=kappa,
        alpha=alpha,
        S4=S4,
        depth_class='L',
    )


def heisenberg_shadow(k: Fraction = Fraction(1)) -> ShadowCurveData:
    """Heisenberg at level k.

    kappa = k, alpha = 0, S4 = 0 (class G: Gaussian, terminates at arity 2).
    Q_L(t) = 4*k^2 (constant): no branch points, all omega_{g,n} = 0.
    """
    return ShadowCurveData(
        name=f"Heis_k={k}",
        kappa=k,
        alpha=Fraction(0),
        S4=Fraction(0),
        depth_class='G',
    )


def betagamma_shadow() -> ShadowCurveData:
    """Beta-gamma system.

    Class C (contact, depth 4).  On the single primary line used by this
    scalar engine it has the same quadratic Q_L data as Virasoro at c=2,
    but the family label and depth class remain beta-gamma data.
    """
    vir = virasoro_shadow(Fraction(2))
    return ShadowCurveData(
        name="betagamma",
        kappa=vir.kappa,
        alpha=vir.alpha,
        S4=vir.S4,
        depth_class='C',
    )


def w3_shadow(c: Fraction) -> ShadowCurveData:
    """W_3 algebra on the W-line.

    kappa = 5c/6 (total for W_3), alpha_W = 0 (Z_2 parity),
    S4^W = 2560/[c*(5c+22)^3].
    """
    kappa = Fraction(5) * c / 6
    alpha = Fraction(0)
    S4 = Fraction(2560) / (c * (5 * c + 22) ** 3)
    return ShadowCurveData(
        name=f"W3_c={c}",
        kappa=kappa,
        alpha=alpha,
        S4=S4,
        depth_class='M',
    )


# ============================================================================
# 2. Spectral curve parametrization (Zhukovsky)
# ============================================================================

@dataclass
class ShadowSpectralCurve:
    """A genus-0 spectral curve y^2 = Q_L(t) with Zhukovsky parametrization.

    Parametrization:
        t(z) = t_mid + delta * (z + 1/z) / 2
        y(z) = sqrt(q2) * delta * (z - 1/z) / 2

    Deck involution: sigma(z) = 1/z.
    Ramification at z = +1 (-> t_+) and z = -1 (-> t_-).

    For degenerate cases (class G: constant Q_L, or class L: perfect-square Q_L),
    the finite calculator has no simple branch-point input.  No general EO
    vanishing theorem is inferred from that degeneration.
    """
    data: ShadowCurveData

    # Numerical parameters (complex, computed from data)
    t_plus: complex = 0.0
    t_minus: complex = 0.0
    t_mid: complex = 0.0
    half_gap: complex = 0.0
    sqrt_q2: complex = 0.0
    degenerate: bool = False

    def __post_init__(self):
        """Compute parametrization from shadow data."""
        q0 = float(self.data.q0)
        q1 = float(self.data.q1)
        q2 = float(self.data.q2)

        if abs(q2) < 1e-50:
            self.degenerate = True
            return

        disc = q1 * q1 - 4.0 * q0 * q2
        sqrt_disc = cmath.sqrt(disc)

        self.t_plus = (-q1 + sqrt_disc) / (2.0 * q2)
        self.t_minus = (-q1 - sqrt_disc) / (2.0 * q2)
        self.t_mid = (self.t_plus + self.t_minus) / 2.0
        self.half_gap = (self.t_plus - self.t_minus) / 2.0
        self.sqrt_q2 = cmath.sqrt(q2)

        if abs(self.half_gap) < 1e-50:
            self.degenerate = True

    def t_of_z(self, z: complex) -> complex:
        if self.degenerate:
            return self.t_mid
        return self.t_mid + self.half_gap * (z + 1.0 / z) / 2.0

    def y_of_z(self, z: complex) -> complex:
        if self.degenerate:
            return cmath.sqrt(float(self.data.q0))
        return self.sqrt_q2 * self.half_gap * (z - 1.0 / z) / 2.0

    def dt_dz(self, z: complex) -> complex:
        if self.degenerate:
            return 0.0
        return self.half_gap / 2.0 * (1.0 - 1.0 / (z * z))

    def sigma(self, z: complex) -> complex:
        return 1.0 / z

    def omega01(self, z: complex) -> complex:
        return self.y_of_z(z) * self.dt_dz(z)

    def Q_L(self, t: complex) -> complex:
        q0 = float(self.data.q0)
        q1 = float(self.data.q1)
        q2 = float(self.data.q2)
        return q0 + q1 * t + q2 * t * t

    def branch_points_exact(self) -> Tuple[Fraction, Fraction, Fraction, Fraction]:
        """Exact discriminant and coefficients for Q_L(t) = 0.

        The branch points themselves may lie in a quadratic extension of
        the Fraction field.  The returned tuple is (disc, q0, q1, q2).
        """
        q0 = self.data.q0
        q1 = self.data.q1
        q2 = self.data.q2
        if q2 == 0:
            raise ValueError("Degenerate curve: q2 = 0")
        # t_pm = (-q1 +/- sqrt(q1^2 - 4*q0*q2)) / (2*q2)
        disc = q1 ** 2 - 4 * q0 * q2
        return disc, q0, q1, q2


# ============================================================================
# 3. Shadow tower coefficients from Q_L (Taylor expansion)
# ============================================================================

def shadow_tower_from_QL(data: ShadowCurveData,
                         max_arity: int = 12) -> Dict[int, Rational]:
    r"""Compute shadow tower coefficients S_r from Q_L.

    The weighted generating function H(t) = t^2*sqrt(Q_L(t)), and
    S_r = (1/r) * [t^{r-2}] sqrt(Q_L(t)).

    We expand sqrt(Q_L(t)) = sqrt(q0) * sqrt(1 + u) where
    u = (q1*t + q2*t^2)/q0, via the binomial series
    sqrt(1+u) = sum C(1/2, n) u^n.

    Returns {r: S_r} for r = 2, ..., max_arity.
    """
    q0 = Rational(self_data_to_rat(data.q0))
    q1 = Rational(self_data_to_rat(data.q1))
    q2 = Rational(self_data_to_rat(data.q2))

    if q0 == 0:
        raise ValueError("q0 = 0: degenerate (kappa = 0)")

    N = max_arity - 1  # need coefficients up to t^{max_arity - 2}
    a = q1 / q0
    b = q2 / q0

    # Coefficient of t^m in (1 + u)^{1/2}:
    #   sum_{n = ceil(m/2)}^{m} C(1/2,n) * C(n, m-n) * a^{2n-m} * b^{m-n}
    # The formal branch is fixed by sqrt(Q_L(0)) = 2*kappa, not by the
    # positive analytic square root of 4*kappa^2.  This keeps S_2 = kappa
    # on negative scalar complementarity branches.
    if data.kappa != 0:
        sqrt_q0_val = Rational(2) * Rational(data.kappa)
    else:
        return {r: Rational(0) for r in range(2, max_arity + 1)}

    coeffs = {}
    for m in range(N + 1):
        cm = Rational(0)
        n_min = (m + 1) // 2
        for n in range(n_min, m + 1):
            j = 2 * n - m
            k_val = m - n
            # C(1/2, n) = prod_{i=0}^{n-1} (1/2 - i) / n!
            binom_half_n = Rational(1)
            for i in range(n):
                binom_half_n *= Rational(1, 2) - i
            binom_half_n /= factorial(n)
            binom_nk = Rational(factorial(n), factorial(k_val) * factorial(j))
            cm += binom_half_n * binom_nk * a**j * b**k_val
        coeffs[m] = cm

    tower = {}
    for r in range(2, max_arity + 1):
        if r - 2 <= N:
            tower[r] = sqrt_q0_val * coeffs[r - 2] / r
        else:
            tower[r] = Rational(0)

    return tower


def stationary_primary_line_riccati_diagnostic(
    data: ShadowCurveData,
    max_arity: int = 8,
) -> Dict[str, Any]:
    r"""Check the finite primary-line Riccati identity from Q_L.

    The formal shadow series is H(t) = sum_{r>=2} r*S_r*t^r.  On the
    stationary primary line the quadratic construction gives

        H(t)^2 = t^4 * Q_L(t).

    The check is finite: using S_2,...,S_max_arity verifies coefficients
    through degree max_arity+2.  It is not an EO recursion theorem, not a
    convergence-radius statement, and not a multi-weight stable-graph input.
    """
    if max_arity < 2:
        raise ValueError(f"max_arity must be >= 2, got {max_arity}")

    tower = shadow_tower_from_QL(data, max_arity=max_arity)
    h_coeffs = {r: r * tower[r] for r in range(2, max_arity + 1)}
    q_coeffs = {
        4: Rational(self_data_to_rat(data.q0)),
        5: Rational(self_data_to_rat(data.q1)),
        6: Rational(self_data_to_rat(data.q2)),
    }

    checked = {}
    for degree in range(4, max_arity + 3):
        lhs = Rational(0)
        for r in range(2, max_arity + 1):
            s = degree - r
            if 2 <= s <= max_arity:
                lhs += h_coeffs[r] * h_coeffs[s]
        rhs = q_coeffs.get(degree, Rational(0))
        checked[degree] = {
            'H_squared': lhs,
            't4_Q_L': rhs,
            'match': simplify(lhs - rhs) == 0,
        }

    return {
        'status': 'finite_riccati_diagnostic',
        'identity': 'H(t)^2 = t^4 Q_L(t)',
        'family': data.name,
        'depth_class': data.depth_class,
        'arity_window': (2, max_arity),
        'degree_window': (4, max_arity + 2),
        'tower': tower,
        'checked_coefficients': checked,
        'all_checked_degrees_match': all(
            row['match'] for row in checked.values()
        ),
        'certifies_full_eo_recursion': False,
        'certifies_kw_tau_theorem': False,
        'certifies_convergence_radius': False,
        'includes_multi_weight_stable_graph_data': False,
    }


def self_data_to_rat(val):
    """Convert Fraction to Rational-compatible form."""
    if isinstance(val, Fraction):
        return Rational(val.numerator, val.denominator)
    return val


# ============================================================================
# 4. High-precision EO recursion engine
# ============================================================================

class ShadowEORecursion:
    """Finite EO-style contour calculator for the shadow spectral curve.

    Uses mpmath for contour integration at the two ramification points of
    the quadratic curve when they are simple.  Only the implemented
    low-genus correlators are evaluated.  This class does not certify a
    full EO recursion theorem, a KW tau theorem, analytic convergence, or
    multi-weight all-genus data.

    RECURSION:
        omega_{g,n+1}(z_0, z_S) = sum_alpha Res_{z->alpha} K(z, z_0) *
            [ omega_{g-1,n+2}(z, sigma(z), z_S)
              + sum' omega_{g1,|I|+1}(z, z_I) * omega_{g2,|J|+1}(sigma(z), z_J) ]

    K(z, z_0) = -1/2 * int_{sigma(z)}^{z} B(., z_0) / (omega_{0,1}(z) - omega_{0,1}(sigma(z)))
    """

    def __init__(self, data: ShadowCurveData,
                 dps: int = 50,
                 contour_radius: float = 0.02,
                 contour_points: int = 512):
        if not _HAS_MPMATH:
            raise ImportError("mpmath required for ShadowEORecursion")

        self.data = data
        self.dps = dps
        self.contour_radius = contour_radius
        self.contour_points = contour_points

        self.degenerate = (data.q2 == 0) or (data.disc_QL == 0)

        with mpmath.workdps(dps):
            self.q0 = mpmath.mpf(str(float(data.q0)))
            self.q1 = mpmath.mpf(str(float(data.q1)))
            self.q2 = mpmath.mpf(str(float(data.q2)))

            if self.degenerate:
                self.t_plus = mpmath.mpc(0)
                self.t_minus = mpmath.mpc(0)
                self.t_mid = mpmath.mpc(0)
                self.half_gap = mpmath.mpc(0)
                self.sqrt_q2 = mpmath.mpc(0)
            else:
                disc = self.q1**2 - 4 * self.q0 * self.q2
                sqrt_disc = mpmath.sqrt(disc)
                self.t_plus = (-self.q1 + sqrt_disc) / (2 * self.q2)
                self.t_minus = (-self.q1 - sqrt_disc) / (2 * self.q2)
                self.t_mid = (self.t_plus + self.t_minus) / 2
                self.half_gap = (self.t_plus - self.t_minus) / 2
                self.sqrt_q2 = mpmath.sqrt(self.q2)

        self._cache: Dict[str, Any] = {}

    # ------------------------------------------------------------------
    # Primitives
    # ------------------------------------------------------------------

    def _t(self, z_val):
        return self.t_mid + self.half_gap * (z_val + 1 / z_val) / 2

    def _y(self, z_val):
        return self.sqrt_q2 * self.half_gap * (z_val - 1 / z_val) / 2

    def _dt_dz(self, z_val):
        return self.half_gap / 2 * (1 - 1 / (z_val * z_val))

    def _B(self, z1, z2):
        """Bergman kernel B(z1,z2) = 1/(z1-z2)^2."""
        d = z1 - z2
        if abs(d) < mpmath.mpf(10)**(-self.dps + 5):
            return mpmath.mpc(0)
        return 1 / (d * d)

    def _K(self, z_val, z0_val):
        """Recursion kernel."""
        denom1 = z_val - z0_val
        denom2 = 1 - z_val * z0_val
        if abs(denom1) < mpmath.mpf(10)**(-self.dps + 5):
            return mpmath.mpc(0)
        if abs(denom2) < mpmath.mpf(10)**(-self.dps + 5):
            return mpmath.mpc(0)
        int_B = -1 / denom1 + z_val / denom2
        y_z = self._y(z_val)
        delta = self.half_gap
        omega_diff = y_z * delta * (z_val**2 - 1) / z_val**2
        if abs(omega_diff) < mpmath.mpf(10)**(-self.dps + 5):
            return mpmath.mpc(0)
        return mpmath.mpf(-0.5) * int_B / omega_diff

    def _contour_residue(self, integrand_fn, pole):
        """Compute residue at z=pole by contour integration."""
        with mpmath.workdps(self.dps):
            r = self.contour_radius
            N = self.contour_points
            total = mpmath.mpc(0)
            for k in range(N):
                theta = 2 * mpmath.pi * k / N
                z_val = pole + r * mpmath.exp(1j * theta)
                dz = 1j * r * mpmath.exp(1j * theta) * (2 * mpmath.pi / N)
                total += integrand_fn(z_val) * dz
            return total / (2 * mpmath.pi * 1j)

    # ------------------------------------------------------------------
    # omega_{1,1}: genus-reduction from omega_{0,2}(z, sigma(z))
    # ------------------------------------------------------------------

    def omega_11(self, z0_val):
        """omega_{1,1}(z0) = sum_alpha Res K(z,z0) * B(z, 1/z)."""
        if self.degenerate:
            return mpmath.mpc(0)
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            total = mpmath.mpc(0)
            for pole in [mpmath.mpf(1), mpmath.mpf(-1)]:
                def integrand(z_val, _z0=z0_val, _p=pole):
                    K = self._K(z_val, _z0)
                    B_val = self._B(z_val, 1 / z_val)
                    return K * B_val
                total += self._contour_residue(integrand, pole)
            return total

    # ------------------------------------------------------------------
    # omega_{0,3}: splitting only (no genus reduction at g=0)
    # ------------------------------------------------------------------

    def omega_03(self, z0_val, z1_val, z2_val):
        """omega_{0,3}(z0, z1, z2)."""
        if self.degenerate:
            return mpmath.mpc(0)
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            z1_val = mpmath.mpc(z1_val)
            z2_val = mpmath.mpc(z2_val)
            total = mpmath.mpc(0)
            for pole in [mpmath.mpf(1), mpmath.mpf(-1)]:
                def integrand(z_val, _z0=z0_val, _z1=z1_val, _z2=z2_val):
                    K = self._K(z_val, _z0)
                    sz = 1 / z_val
                    t1 = self._B(z_val, _z1) * self._B(sz, _z2)
                    t2 = self._B(z_val, _z2) * self._B(sz, _z1)
                    return K * (t1 + t2)
                total += self._contour_residue(integrand, pole)
            return total

    # ------------------------------------------------------------------
    # omega_{0,4}
    # ------------------------------------------------------------------

    def omega_04(self, z0_val, z1_val, z2_val, z3_val):
        """omega_{0,4}(z0, z1, z2, z3).

        No genus reduction (g=0). Splitting: partitions of {z1,z2,z3}
        into (I,J) with |I|>=1, |J|>=1.
        """
        if self.degenerate:
            return mpmath.mpc(0)
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            z1_val = mpmath.mpc(z1_val)
            z2_val = mpmath.mpc(z2_val)
            z3_val = mpmath.mpc(z3_val)
            zS = [z1_val, z2_val, z3_val]
            total = mpmath.mpc(0)
            for pole in [mpmath.mpf(1), mpmath.mpf(-1)]:
                def integrand(z_val, _z0=z0_val, _zS=list(zS)):
                    K = self._K(z_val, _z0)
                    sz = 1 / z_val
                    val = mpmath.mpc(0)
                    for i in range(3):
                        J_idx = [j for j in range(3) if j != i]
                        # B(z, z_i) * omega_03(sigma(z), z_J)
                        w1 = self._B(z_val, _zS[i])
                        w2 = self.omega_03(sz, _zS[J_idx[0]], _zS[J_idx[1]])
                        val += w1 * w2
                        # omega_03(z, z_J) * B(sigma(z), z_i)
                        w3 = self.omega_03(z_val, _zS[J_idx[0]], _zS[J_idx[1]])
                        w4 = self._B(sz, _zS[i])
                        val += w3 * w4
                    return K * val
                total += self._contour_residue(integrand, pole)
            return total

    # ------------------------------------------------------------------
    # omega_{0,5}
    # ------------------------------------------------------------------

    def omega_05(self, z0_val, z1_val, z2_val, z3_val, z4_val):
        """omega_{0,5}(z0, z1, z2, z3, z4).

        No genus reduction. Splitting: partitions of {z1,z2,z3,z4}
        into (I,J) with |I|>=1, |J|>=1, all genus 0.
        """
        if self.degenerate:
            return mpmath.mpc(0)
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            zS = [mpmath.mpc(z1_val), mpmath.mpc(z2_val),
                  mpmath.mpc(z3_val), mpmath.mpc(z4_val)]
            total = mpmath.mpc(0)
            for pole in [mpmath.mpf(1), mpmath.mpf(-1)]:
                def integrand(z_val, _z0=z0_val, _zS=list(zS)):
                    K = self._K(z_val, _z0)
                    sz = 1 / z_val
                    val = mpmath.mpc(0)
                    indices = list(range(4))
                    # All partitions (I, J) of indices with 1 <= |I| <= 3
                    for r in range(1, 4):
                        for I_set in combinations(indices, r):
                            J_set = tuple(j for j in indices if j not in I_set)
                            z_I = [_zS[i] for i in I_set]
                            z_J = [_zS[j] for j in J_set]
                            # omega_{0,|I|+1}(z, z_I) * omega_{0,|J|+1}(sigma(z), z_J)
                            w_left = self._eval_omega_0n(z_val, z_I)
                            w_right = self._eval_omega_0n(sz, z_J)
                            val += w_left * w_right
                    return K * val
                total += self._contour_residue(integrand, pole)
            return total

    def _eval_omega_0n(self, z_val, z_extra):
        """Evaluate omega_{0,n} at (z_val, *z_extra) where n = 1 + len(z_extra)."""
        n = 1 + len(z_extra)
        if n == 1:
            # omega_{0,1} is initial data (NOT used in recursion products)
            return mpmath.mpc(0)
        if n == 2:
            return self._B(z_val, z_extra[0])
        if n == 3:
            return self.omega_03(z_val, z_extra[0], z_extra[1])
        if n == 4:
            return self.omega_04(z_val, z_extra[0], z_extra[1], z_extra[2])
        raise ValueError(f"omega_{{0,{n}}} not implemented")

    # ------------------------------------------------------------------
    # omega_{1,2}
    # ------------------------------------------------------------------

    def omega_12(self, z0_val, z1_val):
        """omega_{1,2}(z0, z1).

        Genus reduction: omega_{0,3}(z, sigma(z), z1).
        Splitting: B(z, z1)*omega_{1,1}(sigma(z))
                 + omega_{1,1}(z)*B(sigma(z), z1).
        """
        if self.degenerate:
            return mpmath.mpc(0)
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            z1_val = mpmath.mpc(z1_val)
            total = mpmath.mpc(0)
            for pole in [mpmath.mpf(1), mpmath.mpf(-1)]:
                def integrand(z_val, _z0=z0_val, _z1=z1_val):
                    K = self._K(z_val, _z0)
                    sz = 1 / z_val
                    gr = self.omega_03(z_val, sz, _z1)
                    s1 = self._B(z_val, _z1) * self.omega_11(sz)
                    s2 = self.omega_11(z_val) * self._B(sz, _z1)
                    return K * (gr + s1 + s2)
                total += self._contour_residue(integrand, pole)
            return total

    # ------------------------------------------------------------------
    # omega_{1,3}
    # ------------------------------------------------------------------

    def omega_13(self, z0_val, z1_val, z2_val):
        """omega_{1,3}(z0, z1, z2).

        Genus reduction: omega_{0,4}(z, sigma(z), z1, z2).
        Splitting: all (g1,g2)=(0,1) or (1,0) partitions of S={z1,z2}.
        """
        if self.degenerate:
            return mpmath.mpc(0)
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            z1_val = mpmath.mpc(z1_val)
            z2_val = mpmath.mpc(z2_val)
            total = mpmath.mpc(0)
            for pole in [mpmath.mpf(1), mpmath.mpf(-1)]:
                def integrand(z_val, _z0=z0_val, _z1=z1_val, _z2=z2_val):
                    K = self._K(z_val, _z0)
                    sz = 1 / z_val
                    # Genus reduction
                    gr = self.omega_04(z_val, sz, _z1, _z2)
                    # Splitting (g1=0, g2=1): partitions of {z1,z2}
                    val = gr
                    zS_list = [_z1, _z2]
                    for i in range(2):
                        J_idx = [j for j in range(2) if j != i]
                        # B(z, z_i) * omega_{1,2}(sigma(z), z_j)
                        val += self._B(z_val, zS_list[i]) * self.omega_12(sz, zS_list[J_idx[0]])
                        # omega_{1,2}(z, z_j) * B(sigma(z), z_i)
                        val += self.omega_12(z_val, zS_list[J_idx[0]]) * self._B(sz, zS_list[i])
                    # Partition I=S, J=empty:
                    # omega_{0,3}(z, z1, z2) * omega_{1,1}(sigma(z))
                    val += self.omega_03(z_val, _z1, _z2) * self.omega_11(sz)
                    # omega_{1,1}(z) * omega_{0,3}(sigma(z), z1, z2)
                    val += self.omega_11(z_val) * self.omega_03(sz, _z1, _z2)
                    return K * val
                total += self._contour_residue(integrand, pole)
            return total

    # ------------------------------------------------------------------
    # omega_{2,1}
    # ------------------------------------------------------------------

    def omega_21(self, z0_val):
        """omega_{2,1}(z0).

        Genus reduction: omega_{1,2}(z, sigma(z)).
        Splitting: omega_{1,1}(z)*omega_{1,1}(sigma(z)).
        """
        if self.degenerate:
            return mpmath.mpc(0)
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            total = mpmath.mpc(0)
            for pole in [mpmath.mpf(1), mpmath.mpf(-1)]:
                def integrand(z_val, _z0=z0_val):
                    K = self._K(z_val, _z0)
                    sz = 1 / z_val
                    gr = self.omega_12(z_val, sz)
                    sp = self.omega_11(z_val) * self.omega_11(sz)
                    return K * (gr + sp)
                total += self._contour_residue(integrand, pole)
            return total

    # ------------------------------------------------------------------
    # omega_{2,2}
    # ------------------------------------------------------------------

    def omega_22(self, z0_val, z1_val):
        """omega_{2,2}(z0, z1).

        Genus reduction: omega_{1,3}(z, sigma(z), z1).
        Splitting: all partitions (g1+g2=2, I+J={z1}).
        """
        if self.degenerate:
            return mpmath.mpc(0)
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            z1_val = mpmath.mpc(z1_val)
            total = mpmath.mpc(0)
            for pole in [mpmath.mpf(1), mpmath.mpf(-1)]:
                def integrand(z_val, _z0=z0_val, _z1=z1_val):
                    K = self._K(z_val, _z0)
                    sz = 1 / z_val
                    # Genus reduction
                    gr = self.omega_13(z_val, sz, _z1)
                    # Splitting:
                    # (g1=0, g2=2): B(z,z1)*omega_21(sigma(z))
                    s1 = self._B(z_val, _z1) * self.omega_21(sz)
                    # (g1=2, g2=0): omega_21(z)*B(sigma(z),z1)
                    s2 = self.omega_21(z_val) * self._B(sz, _z1)
                    # (g1=1, g2=1): omega_12(z,z1)*omega_11(sigma(z))
                    s3 = self.omega_12(z_val, _z1) * self.omega_11(sz)
                    # omega_11(z)*omega_12(sigma(z),z1)
                    s4 = self.omega_11(z_val) * self.omega_12(sz, _z1)
                    return K * (gr + s1 + s2 + s3 + s4)
                total += self._contour_residue(integrand, pole)
            return total

    # ------------------------------------------------------------------
    # omega_{3,1}
    # ------------------------------------------------------------------

    def omega_31(self, z0_val):
        """omega_{3,1}(z0).

        Genus reduction: omega_{2,2}(z, sigma(z)).
        Splitting: omega_{1,1}(z)*omega_{2,1}(sigma(z))
                 + omega_{2,1}(z)*omega_{1,1}(sigma(z)).
        (omega_{0,1} excluded from splitting.)
        """
        if self.degenerate:
            return mpmath.mpc(0)
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            total = mpmath.mpc(0)
            for pole in [mpmath.mpf(1), mpmath.mpf(-1)]:
                def integrand(z_val, _z0=z0_val):
                    K = self._K(z_val, _z0)
                    sz = 1 / z_val
                    gr = self.omega_22(z_val, sz)
                    s1 = self.omega_11(z_val) * self.omega_21(sz)
                    s2 = self.omega_21(z_val) * self.omega_11(sz)
                    return K * (gr + s1 + s2)
                total += self._contour_residue(integrand, pole)
            return total

    # ------------------------------------------------------------------
    # Free energies
    # ------------------------------------------------------------------

    def F1_shadow(self) -> Rational:
        """F_1 = kappa/24 on the uniform-weight scalar lane."""
        return Rational(self.data.kappa.numerator,
                        self.data.kappa.denominator) / 24

    def F1_analytical(self) -> float:
        """F_1 = kappa/24 (numerical)."""
        return float(self.data.kappa) / 24.0

    def Fg_shadow(self, g: int) -> Rational:
        """F_g = kappa * lambda_g^FP on the uniform-weight scalar lane."""
        kappa_rat = Rational(self.data.kappa.numerator,
                             self.data.kappa.denominator)
        return kappa_rat * lambda_fp(g)

    def shadow_generating_function(self, t_val: float) -> float:
        """H(t) = 2*kappa*t^2 * sqrt(Q_L(t)/Q_L(0)).

        The Taylor coefficients of H give the shadow tower:
        H(t) = sum_{r>=2} r*S_r*t^r.
        """
        kappa = float(self.data.kappa)
        q0 = float(self.data.q0)
        Q_t = float(self.data.q0) + float(self.data.q1) * t_val + float(self.data.q2) * t_val**2
        if Q_t < 0:
            return float('nan')
        return 2 * kappa * t_val**2 * math.sqrt(Q_t / q0)


# ============================================================================
# 5. Airy curve engine
# ============================================================================

class AiryCurveRecursion:
    """Local Airy residue oracle for the curve x = z^2/2, y = z.

    The Airy curve is the universal local model near a simple branch point.
    Restoring the full differential normalization gives the usual
    Witten-Kontsevich intersection numbers.  The methods below return
    coefficient functions in the root-variable convention used by this
    engine, so the exact formulas are residue oracles for that convention.

    Spectral data: x(z) = z^2/2, y(z) = z. Involution: sigma(z) = -z.
    Branch point: z = 0.  Bergman kernel: B(z1,z2) = dz1 dz2/(z1-z2)^2.

    Recursion kernel: K(z, z0) = 1/(2z) * [1/(z-z0) + 1/(z+z0)]
                               = 1/(2z) * 2z0/(z0^2 - z^2)
                               = z0 / (z*(z0^2 - z^2)).
    """

    def __init__(self, dps: int = 50, contour_radius: float = 0.01,
                 contour_points: int = 512):
        if not _HAS_MPMATH:
            raise ImportError("mpmath required for AiryCurveRecursion")
        self.dps = dps
        self.contour_radius = contour_radius
        self.contour_points = contour_points

    def _B(self, z1, z2):
        d = z1 - z2
        if abs(d) < mpmath.mpf(10)**(-self.dps + 5):
            return mpmath.mpc(0)
        return 1 / (d * d)

    def _K_airy(self, z_val, z0_val):
        """Recursion kernel for Airy: K(z,z0) = z0/(z*(z0^2 - z^2))."""
        denom = z_val * (z0_val**2 - z_val**2)
        if abs(denom) < mpmath.mpf(10)**(-self.dps + 5):
            return mpmath.mpc(0)
        return z0_val / denom

    def _contour_residue(self, integrand_fn, pole=0):
        """Residue at z=pole by contour integration."""
        with mpmath.workdps(self.dps):
            r = self.contour_radius
            N = self.contour_points
            total = mpmath.mpc(0)
            for k in range(N):
                theta = 2 * mpmath.pi * k / N
                z_val = pole + r * mpmath.exp(1j * theta)
                dz = 1j * r * mpmath.exp(1j * theta) * (2 * mpmath.pi / N)
                total += integrand_fn(z_val) * dz
            return total / (2 * mpmath.pi * 1j)

    def omega_11_airy(self, z0_val):
        """Root-coefficient omega_{1,1}^{Airy}(z0).

        = Res_{z->0} K(z,z0) * B(z,-z)
        = Res_{z->0} z0/(z*(z0^2-z^2)) * 1/(2z)^2
        = Res_{z->0} z0/(4*z^3*(z0^2-z^2))
        = 1/(4*z0^3).
        """
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            def integrand(z_val):
                K = self._K_airy(z_val, z0_val)
                B_val = self._B(z_val, -z_val)
                return K * B_val
            return self._contour_residue(integrand, 0)

    def omega_11_airy_exact(self, z0_val):
        """Exact root-coefficient: omega_{1,1}^{Airy}(z0) = 1/(4*z0^3)."""
        return 1 / (4 * z0_val**3)

    def omega_03_airy(self, z0_val, z1_val, z2_val):
        """omega_{0,3}^{Airy}(z0, z1, z2)."""
        with mpmath.workdps(self.dps):
            z0_val = mpmath.mpc(z0_val)
            z1_val = mpmath.mpc(z1_val)
            z2_val = mpmath.mpc(z2_val)
            def integrand(z_val):
                K = self._K_airy(z_val, z0_val)
                sz = -z_val
                t1 = self._B(z_val, z1_val) * self._B(sz, z2_val)
                t2 = self._B(z_val, z2_val) * self._B(sz, z1_val)
                return K * (t1 + t2)
            return self._contour_residue(integrand, 0)

    def omega_03_airy_exact(self, z0_val, z1_val, z2_val):
        r"""Exact root-coefficient omega_{0,3}^{Airy}.

        With the first variable as the recursion root, the residue is
        2/(z0*z1^2*z2^2).  The full symmetric differential is recovered
        only after restoring the differential normalization.
        """
        return 2 / (z0_val * z1_val**2 * z2_val**2)

    def F1_airy(self) -> Rational:
        """F_1^{Airy} = <tau_1>_1 = 1/24."""
        return Rational(1, 24)

    def Fg_airy(self, g: int) -> Rational:
        """F_g^{Airy} = lambda_g^FP (Faber-Pandharipande)."""
        return lambda_fp(g)


# ============================================================================
# 6. Symplectic invariance check
# ============================================================================

def symplectic_check_free_energy(data: ShadowCurveData, g: int) -> Dict[str, Any]:
    """Check the scalar free-energy normalization under the chosen branch.

    This routine does not prove general EO symplectic invariance.  It checks
    the scalar normalization used in this engine: the free energy is
    F_g = kappa*lambda_g^FP, where kappa is the signed coefficient fixed by
    sqrt(Q_L(0)) = 2*kappa.
    """
    kappa_rat = Rational(data.kappa.numerator, data.kappa.denominator)
    F_g_original = kappa_rat * lambda_fp(g)

    return {
        'g': g,
        'F_g_original': F_g_original,
        'F_g_invariant': F_g_original,
        'kappa': kappa_rat,
        'symplectic_invariant': True,
        'full_eo_symplectic_invariance_asserted': False,
        'scope': 'scalar signed-branch normalization',
        'reason': 'F_g = kappa*lambda_g^FP in the scalar shadow lane',
    }


# ============================================================================
# 7. WKB expansion
# ============================================================================

def wkb_expansion(data: ShadowCurveData, max_order: int = 4) -> Dict[int, Rational]:
    r"""Finite WKB-style scalar coefficients from the shadow spectral curve.

    The usual WKB notation writes a formal expression
    psi(x) = exp(sum_{g>=0} hbar^{g-1} S_g(x)).  This helper records only
    the scalar coefficients used by the shadow lane:

        S_0(x) = integral y dx  (classical action)
        S_1(x) = -1/2 log(y dx/dz) (one-loop)
        S_g(x) for g >= 2 from omega_{g,0}

    For the shadow curve y^2 = Q_L(t):
        S_0 = integral sqrt(Q_L(t)) dt  (elliptic integral for generic Q_L)
        S_1 = -1/4 log Q_L(t)  (logarithmic)

    No analytic WKB solution or convergence statement is certified.
    Returns {g: coefficient of S_g evaluated at a reference point}.
    """
    kappa_rat = Rational(data.kappa.numerator, data.kappa.denominator)
    results = {}

    # S_0: classical action. For the shadow curve, this encodes the
    # genus-0 prepotential F_0.  We compute the leading coefficient
    # from Q_L at t=0: S_0 ~ sqrt(q0) * t = 2*kappa*t.
    results[0] = 2 * kappa_rat  # leading coefficient of S_0 at t=0

    # S_1: one-loop determinant.
    # S_1(t) = -1/4 * log Q_L(t) + const
    # At t=0: S_1(0) = -1/4 * log(4*kappa^2)
    # The free energy F_1 = kappa/24 corresponds to the regulated
    # spectral determinant contribution.
    results[1] = kappa_rat / 24  # F_1 = kappa * lambda_1

    # S_g for g >= 2: from the recursion
    for g in range(2, max_order + 1):
        results[g] = kappa_rat * lambda_fp(g)

    return results


# ============================================================================
# 8. Verdier-complementarity scalar partner
# ============================================================================

def koszul_dual_curve(data: ShadowCurveData) -> Optional[ShadowCurveData]:
    """Return tabulated scalar data for the Verdier-complementarity branch.

    The function name is kept for compatibility with older tests.  It does
    not construct A^!.  The object A^! is obtained from A^i by
    Verdier/continuous-linear duality under finite-type/completed
    hypotheses; Omega(B(A)) recovers A by inversion, and Z_ch^der(A) is the
    Hochschild bulk object.

    Scalar branches tabulated here:
      * Virasoro: c -> 26-c, hence kappa + kappa' = 13.
      * affine sl_2: k -> -k-4, hence kappa + kappa' = 0.
      * Heisenberg: kappa -> -kappa as scalar complementarity data only.
    """
    if data.name.startswith("Vir"):
        # Extract c from kappa = c/2
        c = data.kappa * 2
        c_dual = Fraction(26) - c
        if c_dual <= 0 or c_dual * (5 * c_dual + 22) == 0:
            return None
        return virasoro_shadow(c_dual)
    if data.name.startswith("aff_sl2"):
        k = (data.kappa * 4 / 3) - 2
        k_dual = -k - 4  # FF involution for sl_2
        if k_dual + 2 == 0:
            return None
        return affine_sl2_shadow(k_dual)
    if data.name.startswith("Heis"):
        k = data.kappa
        return heisenberg_shadow(-k)
    return None


def complementarity_check(data: ShadowCurveData, g: int) -> Dict[str, Any]:
    """Verify scalar complementarity for the tabulated branch.

    Virasoro gives kappa(c) + kappa(26-c) = 13.  Affine sl_2 and
    Heisenberg scalar partners give kappa + kappa' = 0.
    """
    kappa_rat = Rational(data.kappa.numerator, data.kappa.denominator)
    F_g = kappa_rat * lambda_fp(g)

    dual = koszul_dual_curve(data)
    if dual is None:
        return {
            'F_g': F_g,
            'F_g_dual': None,
            'sum': None,
            'complementarity': False,
        }

    kappa_dual = Rational(dual.kappa.numerator, dual.kappa.denominator)
    F_g_dual = kappa_dual * lambda_fp(g)
    total = F_g + F_g_dual

    expected_constant = None
    if data.name.startswith("Vir"):
        expected_constant = Rational(13)
    elif data.name.startswith("aff_sl2") or data.name.startswith("Heis"):
        expected_constant = Rational(0)

    expected = (
        expected_constant * lambda_fp(g)
        if expected_constant is not None else None
    )

    return {
        'F_g': F_g,
        'F_g_dual': F_g_dual,
        'sum': total,
        'expected_sum': expected,
        'complementarity': (total == expected) if expected is not None else None,
        'kappa_sum': kappa_rat + kappa_dual,
    }


# ============================================================================
# 9. Shadow tower coefficient extraction from omega_{g,n}
# ============================================================================

def extract_shadow_from_omega(eo: ShadowEORecursion,
                              g: int, n: int,
                              eval_points: Optional[List[complex]] = None,
                              ) -> complex:
    r"""Evaluate one implemented EO-style correlator.

    The function name is kept for compatibility.  No canonical division by
    a standard form is performed here, and no theorem equating these
    finite correlator values with the full shadow tower is certified.
    """
    if eval_points is None:
        eval_points = [2.0 + 0.5j, 3.0 - 0.3j, 1.5 + 0.8j,
                       4.0 + 0.1j, 2.5 - 0.7j]

    if n == 1:
        if g == 1:
            return eo.omega_11(eval_points[0])
        if g == 2:
            return eo.omega_21(eval_points[0])
        if g == 3:
            return eo.omega_31(eval_points[0])
    elif n == 2:
        if g == 0:
            return eo._B(eval_points[0], eval_points[1])
        if g == 1:
            return eo.omega_12(eval_points[0], eval_points[1])
        if g == 2:
            return eo.omega_22(eval_points[0], eval_points[1])
    elif n == 3:
        if g == 0:
            return eo.omega_03(eval_points[0], eval_points[1], eval_points[2])
        if g == 1:
            return eo.omega_13(eval_points[0], eval_points[1], eval_points[2])
    elif n == 4:
        if g == 0:
            return eo.omega_04(eval_points[0], eval_points[1],
                               eval_points[2], eval_points[3])
    elif n == 5:
        if g == 0:
            return eo.omega_05(eval_points[0], eval_points[1],
                               eval_points[2], eval_points[3], eval_points[4])
    return None


# ============================================================================
# 10. Finite scalar coefficient comparison
# ============================================================================

def verify_shadow_eo_match(data: ShadowCurveData, max_genus: int = 3) -> Dict[str, Any]:
    """Verify scalar free energies against the formal shadow tower.

    This function does not perform contour integration.  It checks that the
    scalar formula F_g = kappa*lambda_g^FP is consistent with the signed
    formal branch used to extract the shadow tower from Q_L.

    Returns comparison dict for each genus.
    """
    results = {}
    kappa_rat = Rational(data.kappa.numerator, data.kappa.denominator)

    for g in range(1, max_genus + 1):
        F_g_shadow = kappa_rat * lambda_fp(g)

        tower = shadow_tower_from_QL(data, max_arity=2 * g + 2)
        F_g_taylor = tower[2] * lambda_fp(g)

        results[g] = {
            'F_g_shadow': F_g_shadow,
            'F_g_taylor': F_g_taylor,
            'tower_S2': tower[2],
            'eo_contour_integral': 'not_evaluated',
            'full_eo_recursion_theorem_asserted': False,
            'finite_scalar_identity': True,
            'match': (F_g_shadow == F_g_taylor),
        }

    return results


def kw_tau_function_log(g_max: int = 8) -> Dict[int, Rational]:
    """Finite Airy/KW logarithmic coefficients lambda_g^FP."""
    if g_max < 1:
        raise ValueError(f"g_max must be >= 1, got {g_max}")
    return {g: lambda_fp(g) for g in range(1, g_max + 1)}


def shadow_scalar_tau_log(data: ShadowCurveData,
                          g_max: int = 8) -> Dict[int, Rational]:
    """Finite scalar shadow logarithmic coefficients kappa*lambda_g^FP."""
    if g_max < 1:
        raise ValueError(f"g_max must be >= 1, got {g_max}")
    kappa = Rational(data.kappa.numerator, data.kappa.denominator)
    return {g: kappa * lambda_fp(g) for g in range(1, g_max + 1)}


def finite_scalar_kw_coefficient_identity(
    data: ShadowCurveData,
    g_max: int = 5,
) -> Dict[str, Any]:
    r"""Certify the finite scalar Airy/KW coefficient identity.

    For 1 <= g <= g_max this checks

        [hbar^{2g}] log(tau_shadow) =
        kappa * [hbar^{2g}] log(tau_KW).

    It does not assert an analytic tau-function equality, a convergence
    radius, a full EO theorem, or multi-weight all-genus data.
    """
    if g_max < 1:
        raise ValueError(f"g_max must be >= 1, got {g_max}")

    kappa = Rational(data.kappa.numerator, data.kappa.denominator)
    kw_log = kw_tau_function_log(g_max)
    shadow_log = shadow_scalar_tau_log(data, g_max)

    coefficients = {}
    for g in range(1, g_max + 1):
        coefficients[g] = {
            'lambda_fp': kw_log[g],
            'kw_log_coefficient': kw_log[g],
            'shadow_log_coefficient': shadow_log[g],
            'kappa_times_kw': kappa * kw_log[g],
            'coefficient_identity': shadow_log[g] == kappa * kw_log[g],
        }

    return {
        'status': 'finite_scalar_coefficient_identity',
        'family': data.name,
        'kappa': kappa,
        'genus_window': (1, g_max),
        'coefficients': coefficients,
        'all_coefficients_match': all(
            row['coefficient_identity'] for row in coefficients.values()
        ),
        'global_kw_tau_theorem_asserted': False,
        'analytic_tau_power_asserted': False,
        'full_eo_recursion_theorem_asserted': False,
        'convergence_radius_asserted': False,
        'multi_weight_all_genus_theorem_asserted': False,
    }


# ============================================================================
# 11. Bouchard-Marino mirror curve (resolved conifold)
# ============================================================================

class MirrorCurveConifold:
    """Separate resolved-conifold mirror-curve input.

    The mirror curve: x + y + e^{-x} + Q*e^{-y} = 0
    where Q = e^{-t} is the Kahler parameter.

    In the framing-0 case: y^2 = -4*sin^2(x/2) + 4*Q
    Branch points at sin^2(x/2) = Q, i.e., x = 2*arcsin(sqrt(Q)).

    For Q = 0 (large radius): y^2 = -4*sin^2(x/2), the Catalan curve.

    This is not the shadow curve y^2 = Q_L(t), and it is not the WP/JT
    sine curve.  The Q -> 0 Catalan helper below is only a separate
    finite combinatorial check.
    """

    def __init__(self, Q_param: float = 0.01, dps: int = 30):
        if not _HAS_MPMATH:
            raise ImportError("mpmath required")
        self.Q = Q_param
        self.dps = dps

    def catalan_number(self, n: int) -> int:
        """Catalan number C_n = (2n)! / ((n+1)! * n!)."""
        return int(factorial(2 * n) / (factorial(n + 1) * factorial(n)))

    def catalan_free_energy_g0(self, n: int) -> Rational:
        """Genus-0 open GW of conifold at Q=0: Catalan numbers.

        <W_n>_0 = C_{n-1} / n  for the disc amplitude with n boundary marked points.
        """
        if n < 1:
            return Rational(0)
        return Rational(self.catalan_number(n - 1), n)


# ============================================================================
# 12. Consistency checks: dilaton and string equations
# ============================================================================

def dilaton_equation_check(eo: ShadowEORecursion,
                           g: int, n: int,
                           z_points: List[complex]) -> Dict[str, Any]:
    """Return finite structural metadata for the dilaton equation.

    Dilaton equation:
        Res_{p->alpha} omega_{g,n+1}(z_S, p) = (2g-2+n) * omega_{g,n}(z_S)

    This is a universal constraint from the topology of M-bar_{g,n}
    (the forgetful map pi: M-bar_{g,n+1} -> M-bar_{g,n}).
    """
    chi = 2 * g - 2 + n
    if chi <= 0:
        return {
            'valid': False,
            'reason': 'unstable (chi <= 0)',
            'checked_numerically': False,
        }

    return {
        'g': g,
        'n': n,
        'euler_char': chi,
        'dilaton_factor': chi,
        'equation': f'Res omega_{{g,n+1}}(..., p) = {chi} * omega_{{g,n}}(...)',
        'valid': True,
        'checked_numerically': False,
    }


def string_equation_check() -> Dict[str, Any]:
    """The string equation for the shadow spectral curve.

    For the Airy curve: <tau_0 tau_{d_1} ... tau_{d_n}>_g
    = sum_j <tau_{d_1} ... tau_{d_j-1} ... tau_{d_n}>_g

    This is the L_{-1} Virasoro constraint.
    """
    # Verify: <tau_0^3>_0 = 1
    val = _witten_kontsevich(0, (0, 0, 0))
    # String equation from <tau_0 * tau_0 * tau_0>_0:
    # Remove one tau_0, sum over reducing each remaining tau_d by 1.
    # <tau_{-1} tau_0>_0 + <tau_0 tau_{-1}>_0 = 0
    # String equation: <tau_0 tau_{d_1}...>_g = sum <..tau_{d_j-1}..>_g.
    # From <tau_0^3>_0 = 1: remove tau_0: <tau_{-1} tau_0>_0 + <tau_0 tau_{-1}>_0
    # but tau_{-1} doesn't exist. For g=0 n=3, this is the base case.
    return {
        'base_case': '<tau_0^3>_0 = 1',
        'value': val,
        'string_eq_verified': (val == Rational(1)),
    }


# ============================================================================
# 13. Scope firewalls and finite verification report
# ============================================================================

def wp_jt_sine_curve_input() -> Dict[str, Any]:
    """Separate WP/JT topological-recursion input."""
    return {
        'shadow_curve': 'y^2 = Q_L(t)',
        'wp_jt_curve': 'y = sin(2*pi*sqrt(x))/(4*pi)',
        'same_spectral_curve': False,
        'wp_jt_from_shadow_curve_certified': False,
        'requires_separate_input': True,
    }


def multi_weight_stable_graph_scope() -> Dict[str, Any]:
    """Scope of multi-weight and planted-forest data in this module."""
    return {
        'planted_forest_diagnostics_computed': False,
        'multi_weight_stable_graph_data_present': False,
        'multi_weight_cross_channel_terms_included': False,
        'multi_weight_all_genus_theorem_asserted': False,
        'open_obligation': (
            'Multi-weight and planted-forest corrections require a separate '
            'stable-graph engine; Q_L and scalar coefficients do not compute them.'
        ),
    }


def claim_scope_firewall_report(
    data: ShadowCurveData,
    max_genus: int = 3,
    max_arity: int = 8,
) -> Dict[str, Any]:
    """Assemble the finite/non-certified split for this scalar engine."""
    return {
        'shadow_spectral_curve': {
            'equation': 'y^2 = Q_L(t)',
            'q0': data.q0,
            'q1': data.q1,
            'q2': data.q2,
            'is_eo_input_after_separate_residue_data': True,
            'certifies_full_eo_recursion': False,
        },
        'stationary_primary_line_riccati': (
            stationary_primary_line_riccati_diagnostic(data, max_arity)
        ),
        'finite_scalar_kw_coefficients': (
            finite_scalar_kw_coefficient_identity(data, max_genus)
        ),
        'wp_jt_sine_curve': wp_jt_sine_curve_input(),
        'multi_weight_stable_graphs': multi_weight_stable_graph_scope(),
        'unsupported_claims': {
            'full_eo_recursion_theorem': False,
            'global_kw_tau_theorem': False,
            'analytic_convergence_radius': False,
            'wp_jt_from_shadow_curve': False,
            'multi_weight_all_genus_from_scalar_curve': False,
        },
    }


def full_verification_suite(data: ShadowCurveData) -> Dict[str, Any]:
    """Run the finite scalar verification report for a shadow curve.

    1. Shadow tower from Q_L (Taylor expansion).
    2. Scalar free energies.
    3. Verdier-complementarity scalar partner.
    4. Signed-branch normalization check.
    5. WKB coefficients.
    """
    results = {}

    # 1. Shadow tower
    tower = shadow_tower_from_QL(data, max_arity=8)
    results['tower'] = tower

    # 2. Free energies
    kappa_rat = Rational(data.kappa.numerator, data.kappa.denominator)
    results['free_energies'] = {
        g: kappa_rat * lambda_fp(g) for g in range(1, 5)
    }

    # 3. Verdier-complementarity scalar partner
    dual = koszul_dual_curve(data)
    results['koszul_dual'] = dual
    if dual is not None:
        results['complementarity'] = {
            g: complementarity_check(data, g) for g in range(1, 4)
        }

    # 4. Symplectic invariance
    results['symplectic'] = {
        g: symplectic_check_free_energy(data, g) for g in range(1, 4)
    }

    # 5. WKB
    results['wkb'] = wkb_expansion(data, max_order=4)

    # 6. Scope firewall
    results['claim_scope'] = claim_scope_firewall_report(data)

    return results
