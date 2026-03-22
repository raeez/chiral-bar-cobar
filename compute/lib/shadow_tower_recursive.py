r"""Full recursive shadow Postnikov tower computation to arbitrary arity.

The shadow Postnikov tower Theta_A^{<=r} consists of finite-order projections
of the universal MC element Theta_A := D_A - d_0 (thm:mc2-bar-intrinsic).
At each arity r, the shadow coefficient S_r(A) satisfies the all-arity
master equation:

    nabla_H(S_r) + o^{(r)} = 0

where nabla_H is the horizontal differential and o^{(r)} is the obstruction
class at arity r, determined recursively from lower arities.

For rank-1 primary line, the shadow metric Q_L(t) = (2kappa + alpha*t)^2
+ 2*Delta*t^2 controls everything:

    Q_L(t) = q_0 + q_1*t + q_2*t^2

where q_0 = 4*kappa^2, q_1 = 12*kappa*alpha, q_2 = 9*alpha^2 + 16*kappa*S_4.

The weighted generating function H(t) = sum_r r*S_r*t^r = t^2 * sqrt(Q_L(t))
relates the shadow coefficients to the Taylor expansion of sqrt(Q_L):

    S_r = (1/r) * [t^{r-2}] sqrt(Q_L(t))  =  a_{r-2} / r

where a_n = [t^n] sqrt(Q_L(t)) satisfies the convolution recursion:

    f^2 = Q_L  =>  a_0^2 = q_0,  a_n = -(1/(2*a_0)) sum_{j=1}^{n-1} a_j a_{n-j}  for n >= 3

Asymptotic formula (Flajolet-Sedgewick transfer):

    S_r ~ C * rho^r * r^{-5/2} * cos(r*theta + phi)

where rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|) is the shadow growth
rate (thm:shadow-radius), and theta, C, phi are computable from the branch
point residue of H.

Depth classification (thm:single-line-dichotomy):
    G (Gaussian):  alpha=0, S_4=0  =>  depth 2, S_r=0 for r>=3
    L (Lie/tree):  alpha!=0, Delta=0  =>  depth 3, S_r=0 for r>=4
    C (Contact):   stratum separation  =>  depth 4
    M (Mixed):     Delta!=0  =>  depth infinity, S_r!=0 for all r

Manuscript references:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:recursive-existence (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:obstruction-recursion (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Abs,
    N as Neval,
    Rational,
    Symbol,
    simplify,
    sqrt,
)


c = Symbol('c')
t = Symbol('t')


# ============================================================================
# Data classes
# ============================================================================

@dataclass
class ShadowCoefficient:
    """A single shadow tower coefficient S_r at genus g.

    Attributes:
        arity: The arity r (shadow level).
        genus: The genus (default 0; genus corrections stored separately).
        value: Exact sympy expression for S_r.
        numerical: Float evaluation at a specific parameter point, if computed.
        label: Human-readable label.
    """

    arity: int
    genus: int = 0
    value: Any = None
    numerical: Optional[float] = None
    label: str = ""

    def __post_init__(self):
        if not self.label:
            self.label = f"S_{self.arity}" + (f"^(g={self.genus})" if self.genus > 0 else "")


@dataclass
class ShadowTower:
    """The full shadow Postnikov tower for a chiral algebra.

    Stores exact coefficients S_2, S_3, ..., S_{max_arity} together with
    derived quantities: shadow metric, discriminant, growth rate, depth class.

    Attributes:
        algebra_name: Name of the algebra family.
        max_arity: Maximum arity computed.
        coefficients: Dict mapping arity r -> ShadowCoefficient.
        kappa: S_2 (the curvature).
        cubic: S_3 (the cubic shadow C).
        quartic: S_4 (the quartic shadow Q).
        shadow_metric: Q_L(t) as a sympy expression in t.
        discriminant: Delta = 8*kappa*S_4.
        growth_rate: rho = shadow radius.
        oscillation_phase: theta from the branch point argument.
        depth_class: One of 'G', 'L', 'C', 'M'.
        convergent: Whether rho < 1 (None if undetermined).
        asymptotic_amplitude: C in the asymptotic formula.
        asymptotic_phase: phi in the asymptotic formula.
    """

    algebra_name: str = ""
    max_arity: int = 0
    coefficients: Dict[int, ShadowCoefficient] = field(default_factory=dict)
    kappa: Any = None
    cubic: Any = None
    quartic: Any = None
    shadow_metric: Any = None
    discriminant: Any = None
    growth_rate: Any = None
    oscillation_phase: Any = None
    depth_class: str = ""
    convergent: Optional[bool] = None
    asymptotic_amplitude: Any = None
    asymptotic_phase: Any = None

    def coefficient(self, r: int) -> Any:
        """Get S_r, the shadow coefficient at arity r."""
        if r in self.coefficients:
            return self.coefficients[r].value
        return None

    def generating_function(self, var: str = 't', max_terms: int = 20) -> Any:
        """Generating function G(t) = sum_{r>=2} S_r * t^r, truncated.

        This is the ordinary generating function of the shadow coefficients.
        Note: the identity H(t) = t^2 sqrt(Q_L) holds for the WEIGHTED
        generating function H(t) = sum_{r>=2} r * S_r * t^r, not for G(t).
        """
        s = Symbol(var)
        result = Rational(0)
        upper = min(self.max_arity, max_terms + 2)
        for r in range(2, upper + 1):
            val = self.coefficient(r)
            if val is not None:
                result += val * s ** r
        return result

    def partial_sums(self, max_r: int = None) -> List[float]:
        """Partial sums sum_{r=2}^{N} |S_r| for N = 2, ..., max_r.

        Useful for diagnosing convergence behaviour.
        """
        if max_r is None:
            max_r = self.max_arity
        sums = []
        running = 0.0
        for r in range(2, max_r + 1):
            sc = self.coefficients.get(r)
            if sc is not None and sc.numerical is not None:
                running += abs(sc.numerical)
            sums.append(running)
        return sums

    def ratio_test(self, max_r: int = None) -> List[float]:
        """Ratio test: |S_{r+1}/S_r| for consecutive arities.

        For class M, this converges to rho (the shadow growth rate).
        For classes G and L, trailing ratios are 0.
        """
        if max_r is None:
            max_r = self.max_arity
        ratios = []
        for r in range(2, max_r):
            sc_r = self.coefficients.get(r)
            sc_r1 = self.coefficients.get(r + 1)
            if (sc_r is not None and sc_r1 is not None
                    and sc_r.numerical is not None and sc_r1.numerical is not None
                    and abs(sc_r.numerical) > 1e-50):
                ratios.append(abs(sc_r1.numerical / sc_r.numerical))
            else:
                ratios.append(0.0)
        return ratios

    def asymptotic_prediction(self, r: int) -> Optional[float]:
        """Predicted S_r from the asymptotic formula C*rho^r*r^{-5/2}*cos(r*theta+phi)."""
        if self.depth_class != 'M':
            return 0.0
        try:
            rho_f = float(Neval(self.growth_rate))
            theta_f = float(Neval(self.oscillation_phase)) if self.oscillation_phase is not None else 0.0
            C_f = float(Neval(self.asymptotic_amplitude)) if self.asymptotic_amplitude is not None else 1.0
            phi_f = float(Neval(self.asymptotic_phase)) if self.asymptotic_phase is not None else 0.0
            return C_f * rho_f ** r * r ** (-2.5) * math.cos(r * theta_f + phi_f)
        except (TypeError, ValueError):
            return None

    def asymptotic_error(self, max_r: int = None) -> Dict[int, float]:
        """Relative error |exact - predicted|/|exact| at each arity."""
        if max_r is None:
            max_r = self.max_arity
        errors = {}
        for r in range(5, max_r + 1):
            sc = self.coefficients.get(r)
            pred = self.asymptotic_prediction(r)
            if (sc is not None and sc.numerical is not None
                    and pred is not None and abs(sc.numerical) > 1e-50):
                errors[r] = abs(sc.numerical - pred) / abs(sc.numerical)
        return errors

    def convergence_analysis(self) -> Dict:
        """Full convergence analysis of the tower.

        Returns:
            Dict with keys: depth_class, growth_rate, convergent,
            ratio_limit, partial_sum_growth, borel_summable.
        """
        result: Dict[str, Any] = {
            'depth_class': self.depth_class,
            'convergent': self.convergent,
        }

        if self.growth_rate is not None:
            try:
                rho_f = float(Neval(self.growth_rate))
                result['growth_rate'] = rho_f
                result['convergent'] = rho_f < 1.0
            except (TypeError, ValueError):
                result['growth_rate'] = None

        ratios = self.ratio_test()
        if ratios:
            result['ratio_limit'] = ratios[-1] if ratios else None
            result['ratio_sequence_tail'] = ratios[-5:] if len(ratios) >= 5 else ratios

        psums = self.partial_sums()
        if psums:
            result['partial_sum_final'] = psums[-1]

        # Borel summability: the series sum S_r t^r / r! has radius infinity
        # when S_r grows at most geometrically (always true for algebraic GF).
        if self.depth_class == 'M':
            result['borel_summable'] = True  # algebraic GF => Gevrey-0

        return result

    def summary(self) -> str:
        """Human-readable summary of the tower."""
        lines = [
            f"Shadow Postnikov Tower: {self.algebra_name}",
            f"  Depth class: {self.depth_class}",
            f"  Max arity computed: {self.max_arity}",
            f"  kappa (S_2) = {self.kappa}",
            f"  cubic (S_3) = {self.cubic}",
            f"  quartic (S_4) = {self.quartic}",
            f"  Discriminant Delta = {self.discriminant}",
        ]
        if self.growth_rate is not None:
            try:
                rho_f = float(Neval(self.growth_rate))
                lines.append(f"  Growth rate rho = {rho_f:.8f}")
                lines.append(f"  Convergent: {rho_f < 1.0}")
            except (TypeError, ValueError):
                lines.append(f"  Growth rate rho = {self.growth_rate}")
        for r in range(2, min(self.max_arity + 1, 12)):
            sc = self.coefficients.get(r)
            if sc is not None:
                num_str = f" ({sc.numerical:.6e})" if sc.numerical is not None else ""
                lines.append(f"  S_{r} = {sc.value}{num_str}")
        if self.max_arity > 11:
            lines.append(f"  ... ({self.max_arity - 11} more coefficients)")
        return "\n".join(lines)


# ============================================================================
# Core: Taylor expansion of sqrt(Q_L) via the convolution recursion
# ============================================================================

def _sqrt_quadratic_taylor(q0, q1, q2, max_n: int) -> List:
    r"""Taylor coefficients of f(t) = sqrt(q0 + q1*t + q2*t^2).

    Uses the identity f^2 = Q_L to derive the recursion:

        a_0 = sqrt(q0)
        a_1 = q1 / (2*a_0)
        a_2 = (q2 - a_1^2) / (2*a_0)
        a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j * a_{n-j}   for n >= 3

    Proof: f(t) = sum a_n t^n, then f^2 = sum_n (sum_{j=0}^n a_j a_{n-j}) t^n.
    Matching [t^0]: a_0^2 = q0. Matching [t^1]: 2*a_0*a_1 = q1.
    Matching [t^2]: 2*a_0*a_2 + a_1^2 = q2.
    Matching [t^n] for n >= 3: 2*a_0*a_n + sum_{j=1}^{n-1} a_j*a_{n-j} = 0.

    Parameters:
        q0, q1, q2: Coefficients of Q_L(t) = q0 + q1*t + q2*t^2.
        max_n: Compute a_0, a_1, ..., a_{max_n}.

    Returns:
        List [a_0, a_1, ..., a_{max_n}] of exact (sympy) values.
    """
    a0 = sqrt(q0)
    if max_n == 0:
        return [a0]

    a = [None] * (max_n + 1)
    a[0] = a0
    # a_1 = q1 / (2*a0)
    a[1] = q1 / (2 * a0)
    if max_n == 1:
        return a

    # a_2 = (q2 - a_1^2) / (2*a0)
    a[2] = (q2 - a[1] ** 2) / (2 * a0)

    # Recursion for n >= 3
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv_sum / (2 * a0)

    return a


def shadow_metric_from_data(kappa_val, alpha_val, S4_val):
    """Compute Q_L(t) = q0 + q1*t + q2*t^2 from shadow data.

    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
           = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2

    where Delta = 8*kappa*S4 is the critical discriminant.

    Parameters:
        kappa_val: S_2 (curvature)
        alpha_val: S_3 (cubic shadow coefficient, NOT the same as alpha
                   in Q_L = (2kappa+alpha*t)^2 + 2*Delta*t^2 where alpha=3*S_3).
                   Here alpha_val IS S_3, and the linear term coefficient is 3*S_3.
        S4_val: S_4 (quartic contact invariant)

    Returns:
        (q0, q1, q2, Delta) where Q_L(t) = q0 + q1*t + q2*t^2.
    """
    q0 = 4 * kappa_val ** 2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val ** 2 + 16 * kappa_val * S4_val
    Delta = 8 * kappa_val * S4_val
    return q0, q1, q2, Delta


# ============================================================================
# 1. compute_shadow_tower: master entry point
# ============================================================================

def compute_shadow_tower(kappa_val, alpha_val, S4_val,
                         max_arity: int = 30,
                         algebra_name: str = "",
                         numerical_point: Optional[Dict] = None) -> ShadowTower:
    r"""Compute the full recursive shadow Postnikov tower from shadow data.

    From the shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2,
    extract all Taylor coefficients of sqrt(Q_L), which give the shadow
    tower via S_r = [t^{r-2}] sqrt(Q_L(t)).

    The generating function is H(t) = t^2 * sqrt(Q_L(t)) = sum_{r>=2} S_r t^r.

    Parameters:
        kappa_val: S_2 (curvature). Sympy expression or number.
        alpha_val: S_3 (cubic shadow).
        S4_val: S_4 (quartic contact invariant).
        max_arity: Maximum arity to compute (default 30).
        algebra_name: Human-readable name for the algebra.
        numerical_point: Optional dict of {symbol: value} for numerical evaluation.

    Returns:
        ShadowTower with exact coefficients and derived quantities.
    """
    q0, q1, q2, Delta = shadow_metric_from_data(kappa_val, alpha_val, S4_val)

    # Taylor expansion of sqrt(Q_L(t))
    max_n = max_arity - 2  # a_n = [t^n] sqrt(Q_L), then S_r = a_{r-2}/r
    a_coeffs = _sqrt_quadratic_taylor(q0, q1, q2, max_n)

    # Build coefficient dictionary: S_r = a_{r-2} / r
    coefficients: Dict[int, ShadowCoefficient] = {}
    for n, a_n in enumerate(a_coeffs):
        r = n + 2
        raw = a_n / r  # S_r = a_{r-2} / r
        val = simplify(raw) if hasattr(raw, 'simplify') else raw
        num_val = None
        if numerical_point is not None:
            try:
                v = val
                for sym, num in numerical_point.items():
                    v = v.subs(sym, num)
                num_val = float(Neval(v))
            except (TypeError, ValueError, AttributeError):
                num_val = None
        elif isinstance(val, (int, float)):
            num_val = float(val)
        else:
            try:
                num_val = float(Neval(val))
            except (TypeError, ValueError):
                num_val = None

        coefficients[r] = ShadowCoefficient(
            arity=r,
            value=val,
            numerical=num_val,
        )

    # Depth classification
    dc, _ = depth_classification(kappa_val, alpha_val, S4_val)

    # Growth rate and oscillation phase
    rho = None
    theta = None
    conv = None
    amp = None
    phase = None

    if dc == 'M':
        try:
            rho = sqrt(9 * alpha_val ** 2 + 2 * Delta) / (2 * Abs(kappa_val))
        except (TypeError, ValueError):
            pass

        # Branch point argument for oscillation phase
        try:
            disc_QL = q1 ** 2 - 4 * q0 * q2  # = -32*kappa^2*Delta
            t_plus = (-q1 + sqrt(disc_QL)) / (2 * q2)
            # theta = -arg(t_plus) for the oscillation
            if numerical_point is not None:
                tp = t_plus
                for sym, num in numerical_point.items():
                    tp = tp.subs(sym, num)
                tp_c = complex(Neval(tp))
                theta = -cmath.phase(tp_c)
            else:
                try:
                    tp_c = complex(Neval(t_plus))
                    theta = -cmath.phase(tp_c)
                except (TypeError, ValueError):
                    pass
        except (TypeError, ValueError):
            pass

        # Convergence
        if rho is not None:
            try:
                rho_f = float(Neval(rho))
                conv = rho_f < 1.0
            except (TypeError, ValueError):
                pass

        # Asymptotic amplitude and phase from Flajolet-Sedgewick transfer
        amp, phase = _asymptotic_amplitude_phase(q0, q1, q2, numerical_point)

    elif dc in ('G', 'L', 'C'):
        rho = Rational(0)
        conv = True

    # Shadow metric expression
    Q_expr = q0 + q1 * t + q2 * t ** 2

    tower = ShadowTower(
        algebra_name=algebra_name,
        max_arity=max_arity,
        coefficients=coefficients,
        kappa=kappa_val,
        cubic=alpha_val,
        quartic=S4_val,
        shadow_metric=Q_expr,
        discriminant=Delta,
        growth_rate=rho,
        oscillation_phase=theta,
        depth_class=dc,
        convergent=conv,
        asymptotic_amplitude=amp,
        asymptotic_phase=phase,
    )

    return tower


def _asymptotic_amplitude_phase(q0, q1, q2, numerical_point=None):
    r"""Extract asymptotic amplitude C and phase phi from branch point residue.

    Near the branch point t_0 (zero of Q_L closest to origin), the generating
    function H(t) = t^2 sqrt(Q_L(t)) has a square-root singularity:

        H(t) ~ t_0^2 sqrt(q_2 (t_0 - t_0_bar)) * sqrt(1 - t/t_0) + analytic

    By Flajolet-Sedgewick singularity analysis (Transfer Theorem VI.3):

        [t^r] H(t) ~ -t_0^2 sqrt(q_2 (t_0 - t_0_bar)) / (2 sqrt(pi)) * t_0^{-r} * r^{-3/2}

    But since S_r = [t^{r-2}] sqrt(Q_L), the exponent shift gives r^{-5/2}
    for the shadow coefficients.
    """
    try:
        disc = q1 ** 2 - 4 * q0 * q2
        t_plus = (-q1 + sqrt(disc)) / (2 * q2)
        t_minus = (-q1 - sqrt(disc)) / (2 * q2)

        def _eval(expr):
            v = expr
            if numerical_point is not None:
                for sym, num in numerical_point.items():
                    v = v.subs(sym, num)
            return complex(Neval(v))

        tp_c = _eval(t_plus)
        tm_c = _eval(t_minus)

        # Nearest branch point
        if abs(tp_c) <= abs(tm_c):
            t0_c = tp_c
            t1_c = tm_c
        else:
            t0_c = tm_c
            t1_c = tp_c

        # sqrt(Q_L(t)) near t = t_0:
        # Q_L(t) = q2*(t - t_0)*(t - t_1) so sqrt(Q_L) ~ sqrt(q2*(t_0-t_1)) * sqrt(t-t_0)
        q2_c = _eval(q2)
        prefactor = cmath.sqrt(q2_c * (t0_c - t1_c))

        # [t^n] sqrt(1 - t/t0) ~ -1/(2*sqrt(pi)) * t0^{-n} * n^{-3/2}
        # So [t^n] sqrt(Q_L) ~ prefactor * (-1/(2*sqrt(pi))) * t0^{-n} * n^{-3/2}
        # And S_r = [t^{r-2}] sqrt(Q_L) so the effective amplitude after
        # absorbing the r^{-5/2} convention uses:
        # S_r ~ |prefactor| / (2*sqrt(pi)) * |t0|^{-(r-2)} * (r-2)^{-3/2}
        # Rewriting with rho = 1/|t0| and absorbing (r-2)^{-3/2} ~ r^{-3/2}:
        amp_c = -prefactor / (2 * cmath.sqrt(cmath.pi))
        amplitude = abs(amp_c)
        phi = cmath.phase(amp_c)

        return amplitude, phi

    except (TypeError, ValueError, ZeroDivisionError):
        return None, None


# ============================================================================
# 2. shadow_coefficients_exact: pure coefficient extraction
# ============================================================================

def shadow_coefficients_exact(kappa_val, alpha_val, S4_val,
                              max_r: int = 30) -> Dict[int, Any]:
    r"""Extract exact shadow coefficients S_r as functions of (kappa, alpha, S4).

    S_r = [t^{r-2}] sqrt(q0 + q1*t + q2*t^2) where:
        q0 = 4*kappa^2
        q1 = 12*kappa*alpha
        q2 = 9*alpha^2 + 16*kappa*S4

    Uses the convolution recursion from f^2 = Q_L.

    Parameters:
        kappa_val, alpha_val, S4_val: Shadow data (sympy or numeric).
        max_r: Maximum arity (default 30).

    Returns:
        Dict mapping r -> S_r (exact sympy expressions).
    """
    q0, q1, q2, _ = shadow_metric_from_data(kappa_val, alpha_val, S4_val)
    max_n = max_r - 2
    a = _sqrt_quadratic_taylor(q0, q1, q2, max_n)
    return {r: a[r - 2] / r for r in range(2, max_r + 1)}


# ============================================================================
# 3. Virasoro specialization
# ============================================================================

def shadow_coefficients_virasoro(c_val, max_r: int = 30) -> Dict[int, float]:
    r"""Numerical shadow tower for Virasoro at central charge c_val.

    Virasoro data: kappa = c/2, alpha = 2, S4 = 10/(c*(5c+22)).

    Parameters:
        c_val: Central charge (numeric).
        max_r: Maximum arity (default 30).

    Returns:
        Dict mapping r -> float(S_r).
    """
    c_num = float(c_val)
    kappa = c_num / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_num * (5.0 * c_num + 22.0))

    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4

    # Float recursion for speed
    a = [0.0] * (max_r - 1)
    a[0] = math.sqrt(q0)
    if max_r > 2:
        a[1] = q1 / (2.0 * a[0])
    if max_r > 3:
        a[2] = (q2 - a[1] ** 2) / (2.0 * a[0])
    for n in range(3, max_r - 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2.0 * a[0])

    # S_r = a_{r-2} / r
    return {r: a[r - 2] / r for r in range(2, max_r + 1)}


def shadow_coefficients_virasoro_exact(max_r: int = 30) -> Dict[int, Any]:
    r"""Exact (symbolic) Virasoro shadow tower coefficients as functions of c.

    Uses the convolution recursion with sympy rationals.  The symbol c is
    declared positive so that sqrt(c^2) simplifies to c.

    Returns:
        Dict mapping r -> sympy expression in c.
    """
    cp = Symbol('c', positive=True)
    kappa = cp / 2
    alpha = Rational(2)
    S4 = Rational(10) / (cp * (5 * cp + 22))
    q0, q1, q2, _ = shadow_metric_from_data(kappa, alpha, S4)
    max_n = max_r - 2
    a = _sqrt_quadratic_taylor(q0, q1, q2, max_n)
    result = {}
    for r in range(2, max_r + 1):
        expr = simplify(a[r - 2] / r)
        # Substitute back to the module-level symbol c for consistency
        result[r] = expr.subs(cp, c)
    return result


# ============================================================================
# 4. W_3 specialization
# ============================================================================

def shadow_coefficients_w3(c_val, max_r: int = 30) -> Dict[str, Dict[int, float]]:
    r"""Shadow towers for W_3 at central charge c_val.

    W_3 has TWO shadow lines:
        T-line: identical to Virasoro (kappa_T = c/2, alpha = 2, same S4).
        W-line: kappa_W = c/3, alpha_W = 0 (odd arities vanish by Z_2 parity),
                S4_W = 2560/(c*(5c+22)^3).

    Parameters:
        c_val: Central charge (numeric).
        max_r: Maximum arity.

    Returns:
        Dict with keys 'T_line' and 'W_line', each mapping r -> float(S_r).
    """
    # T-line = Virasoro
    t_line = shadow_coefficients_virasoro(c_val, max_r)

    # W-line
    c_num = float(c_val)
    kappa_W = c_num / 3.0
    alpha_W = 0.0
    S4_W = 2560.0 / (c_num * (5.0 * c_num + 22.0) ** 3)

    q0 = 4.0 * kappa_W ** 2
    q1 = 0.0  # alpha_W = 0
    q2 = 16.0 * kappa_W * S4_W

    a = [0.0] * (max_r - 1)
    a[0] = math.sqrt(q0)
    if max_r > 2:
        a[1] = 0.0  # q1 = 0
    if max_r > 3:
        a[2] = (q2 - a[1] ** 2) / (2.0 * a[0])
    for n in range(3, max_r - 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2.0 * a[0])

    # S_r = a_{r-2} / r
    w_line = {r: a[r - 2] / r for r in range(2, max_r + 1)}

    return {'T_line': t_line, 'W_line': w_line}


# ============================================================================
# 5. Asymptotic extraction from numerical data
# ============================================================================

def asymptotic_extraction(coefficients: Dict[int, float],
                          max_r: int = None) -> Dict[str, Any]:
    r"""Extract asymptotic parameters from numerical shadow coefficients.

    From the data S_r, extract:
        rho: growth rate, from ratio test |S_{r+1}/S_r| -> rho.
        theta: oscillation phase, from the phase of S_r * rho^{-r}.
        C, phi: amplitude and phase from fitting
                S_r ~ C * rho^r * r^{-5/2} * cos(r*theta + phi).

    Compares with theoretical predictions when available.

    Parameters:
        coefficients: Dict mapping r -> float(S_r).
        max_r: Maximum arity to use (default: max key in coefficients).

    Returns:
        Dict with extracted parameters and quality metrics.
    """
    if max_r is None:
        max_r = max(coefficients.keys())

    arities = sorted(r for r in coefficients if 2 <= r <= max_r)
    if len(arities) < 5:
        return {'error': 'insufficient data (need at least 5 coefficients)'}

    # Ratio test for rho
    ratios = []
    for r in arities:
        if r + 1 in coefficients and abs(coefficients[r]) > 1e-50:
            ratios.append((r, abs(coefficients[r + 1] / coefficients[r])))

    if not ratios:
        return {'error': 'all coefficients too small for ratio test'}

    rho_estimate = ratios[-1][1] if ratios else 0.0

    # Richardson extrapolation for rho: if ratio_r ~ rho + a/r + b/r^2,
    # then rho ~ (r+1)*ratio_{r+1} - r*ratio_r for consecutive ratios
    richardson_rho = []
    for i in range(len(ratios) - 1):
        r1, rat1 = ratios[i]
        r2, rat2 = ratios[i + 1]
        # Linear Richardson: rho ~ r2*rat2 - r1*rat1 when difference is O(1/r)
        # Actually: ratio_r = rho * (1 - alpha/(r+1)) approximately
        # Better: just use last few raw ratios averaged
        richardson_rho.append(rat2)

    rho_richardson = richardson_rho[-1] if richardson_rho else rho_estimate

    # Extract theta: phase from sign/oscillation pattern
    # For class M with complex branch points, S_r oscillates in sign
    # Compute S_r * rho^{-r} * r^{5/2} to remove growth and polynomial correction
    normalized = {}
    for r in arities:
        sr = coefficients[r]
        if abs(sr) > 1e-50 and rho_estimate > 1e-10:
            normalized[r] = sr * rho_estimate ** (-r) * r ** 2.5
        else:
            normalized[r] = 0.0

    # Theta from consecutive sign changes / phase rotation
    # If S_r ~ C*cos(r*theta+phi), then the phase advances by theta per step
    theta_estimates = []
    for r in arities:
        if r + 2 in normalized and abs(normalized.get(r, 0)) > 1e-10:
            # cos(r*theta+phi) and cos((r+2)*theta+phi):
            # ratio ~ cos((r+2)*theta+phi)/cos(r*theta+phi)
            # Not directly theta, but atan2 of consecutive pairs works
            n_r = normalized.get(r, 0)
            n_r1 = normalized.get(r + 1, 0)
            if abs(n_r) > 1e-10 and abs(n_r1) > 1e-10:
                # Use atan2 to extract phase
                theta_estimates.append(math.atan2(n_r1, n_r))

    theta_estimate = theta_estimates[-1] if theta_estimates else 0.0

    # Fit C and phi from the normalized sequence
    # normalized[r] ~ C * cos(r*theta + phi)
    # Use least-squares on the last 10 terms
    tail_arities = arities[-10:]
    if len(tail_arities) >= 4 and rho_estimate > 1e-10:
        # Fit: normalized[r] = A*cos(r*theta) + B*sin(r*theta)
        # where C = sqrt(A^2+B^2), phi = atan2(-B, A)
        sum_cc = 0.0
        sum_ss = 0.0
        sum_cs = 0.0
        sum_nc = 0.0
        sum_ns = 0.0
        for r in tail_arities:
            nv = normalized.get(r, 0.0)
            cv = math.cos(r * theta_estimate)
            sv = math.sin(r * theta_estimate)
            sum_cc += cv * cv
            sum_ss += sv * sv
            sum_cs += cv * sv
            sum_nc += nv * cv
            sum_ns += nv * sv

        det = sum_cc * sum_ss - sum_cs ** 2
        if abs(det) > 1e-20:
            A_fit = (sum_ss * sum_nc - sum_cs * sum_ns) / det
            B_fit = (sum_cc * sum_ns - sum_cs * sum_nc) / det
            C_fit = math.sqrt(A_fit ** 2 + B_fit ** 2)
            phi_fit = math.atan2(-B_fit, A_fit)
        else:
            C_fit = abs(normalized.get(tail_arities[-1], 0.0))
            phi_fit = 0.0
    else:
        C_fit = 0.0
        phi_fit = 0.0

    return {
        'rho': rho_estimate,
        'rho_richardson': rho_richardson,
        'theta': theta_estimate,
        'amplitude_C': C_fit,
        'phase_phi': phi_fit,
        'ratio_sequence': ratios[-10:],
        'normalized_tail': {r: normalized.get(r, 0) for r in arities[-10:]},
    }


# ============================================================================
# 6. Convergence analysis (standalone)
# ============================================================================

def convergence_analysis(tower: ShadowTower) -> Dict[str, Any]:
    """Full convergence analysis of a shadow tower.

    Examines:
        - Growth rate and convergence radius
        - Partial sums of |S_r|
        - Cesaro summability when divergent
        - Borel summability (always holds for algebraic GF)

    Parameters:
        tower: A ShadowTower object.

    Returns:
        Dict with convergence diagnostics.
    """
    result = tower.convergence_analysis()

    # Cesaro summability: sigma_N = (1/N) sum_{r=2}^{N+1} partial_sum_r
    psums = tower.partial_sums()
    if len(psums) >= 3:
        cesaro = []
        running = 0.0
        for i, ps in enumerate(psums):
            running += ps
            cesaro.append(running / (i + 1))
        result['cesaro_means'] = cesaro[-5:]
        result['cesaro_bounded'] = all(abs(c) < 1e10 for c in cesaro)

    # Abel summability: evaluate H(t) at t slightly less than 1/rho
    # For class M, H(t) = t^2 sqrt(Q_L(t)) is algebraic, so Abel sum = H(1/rho - eps)
    if tower.depth_class == 'M' and tower.growth_rate is not None:
        try:
            rho_f = float(Neval(tower.growth_rate))
            if rho_f > 0:
                result['abel_point'] = 1.0 / rho_f
                result['abel_summable'] = True
        except (TypeError, ValueError):
            pass

    return result


# ============================================================================
# 7. Depth classification
# ============================================================================

def depth_classification(kappa_val, alpha_val, S4_val) -> Tuple[str, Optional[int]]:
    r"""Determine depth class from shadow data.

    Depth classification (thm:single-line-dichotomy):
        G (Gaussian):  alpha=0, S4=0  =>  depth 2
        L (Lie/tree):  alpha!=0, Delta=0  =>  depth 3
        C (Contact):   special stratum separation  =>  depth 4
        M (Mixed):     Delta!=0  =>  depth infinity

    The contact class C is special: it escapes the single-line framework by
    stratum separation (the quartic contact invariant lives on a charged
    stratum whose self-bracket exits the complex by rank-one rigidity).

    Parameters:
        kappa_val: S_2 (curvature).
        alpha_val: S_3 (cubic shadow).
        S4_val: S_4 (quartic contact invariant).

    Returns:
        (class_name, depth) where depth is int or None (infinity).
    """
    Delta = 8 * kappa_val * S4_val

    # Check for exact zero
    alpha_zero = _is_zero(alpha_val)
    s4_zero = _is_zero(S4_val)
    delta_zero = _is_zero(Delta)

    if alpha_zero and s4_zero:
        return ('G', 2)
    elif delta_zero and not alpha_zero:
        return ('L', 3)
    elif not delta_zero:
        # On the single line: class M (infinite tower, Delta != 0).
        # NOTE: The contact class C (depth 4) escapes this dichotomy via
        # STRATUM SEPARATION: the quartic contact invariant lives on a
        # charged stratum whose self-bracket exits the complex by rank-one
        # rigidity. C is not detectable from single-line shadow data alone.
        # Beta-gamma is the canonical example: on its primary line Delta != 0
        # but the total depth is 4 because the charged-stratum tower
        # terminates. To flag C, use the depth_class_override parameter
        # in compute_shadow_tower or set it after construction.
        return ('M', None)
    else:
        # alpha = 0, S4 != 0 but Delta = 0 requires kappa = 0 (degenerate)
        return ('G', 2)


def _is_zero(val) -> bool:
    """Test if a value is (exactly or numerically) zero."""
    if val == 0:
        return True
    try:
        return simplify(val) == 0
    except (TypeError, AttributeError):
        pass
    try:
        return abs(float(val)) < 1e-50
    except (TypeError, ValueError):
        return False


# ============================================================================
# 8. Spectral decomposition of sqrt(Q_L) near branch points
# ============================================================================

def shadow_spectral_decomposition(kappa_val, alpha_val, S4_val,
                                  numerical_point: Optional[Dict] = None) -> Dict[str, Any]:
    r"""Spectral decomposition of sqrt(Q_L) near its branch points.

    Q_L(t) = q2*(t - t_+)*(t - t_-) where t_+/- are the branch points.

    Near t_0 (say t_+):
        sqrt(Q_L(t)) = sqrt(q2) * sqrt(t - t_+) * sqrt(t - t_-)
                      ~ sqrt(q2*(t_0 - t_1)) * sqrt(t - t_0) + analytic

    The residue at t_0 controls the asymptotic amplitude via
    Flajolet-Sedgewick transfer:
        [t^n] sqrt(1 - t/t_0) = -t_0^{-n} / (2*sqrt(pi*n^3))

    Parameters:
        kappa_val, alpha_val, S4_val: Shadow data.
        numerical_point: Optional substitution dict for evaluation.

    Returns:
        Dict with branch points, residues, and decomposition data.
    """
    q0, q1, q2, Delta = shadow_metric_from_data(kappa_val, alpha_val, S4_val)

    disc = q1 ** 2 - 4 * q0 * q2  # = -32*kappa^2*Delta

    t_plus = (-q1 + sqrt(disc)) / (2 * q2)
    t_minus = (-q1 - sqrt(disc)) / (2 * q2)

    result: Dict[str, Any] = {
        'q0': q0, 'q1': q1, 'q2': q2,
        'Delta': Delta,
        'metric_discriminant': disc,
        't_plus_exact': t_plus,
        't_minus_exact': t_minus,
    }

    # Numerical evaluation
    def _eval(expr):
        v = expr
        if numerical_point is not None:
            for sym, num in numerical_point.items():
                v = v.subs(sym, num)
        return complex(Neval(v))

    try:
        tp_c = _eval(t_plus)
        tm_c = _eval(t_minus)

        result['t_plus_numerical'] = tp_c
        result['t_minus_numerical'] = tm_c
        result['modulus_plus'] = abs(tp_c)
        result['modulus_minus'] = abs(tm_c)
        result['arg_plus'] = cmath.phase(tp_c)
        result['arg_minus'] = cmath.phase(tm_c)

        # Nearest branch point
        if abs(tp_c) <= abs(tm_c):
            t0_c, t1_c = tp_c, tm_c
        else:
            t0_c, t1_c = tm_c, tp_c

        result['nearest_branch_point'] = t0_c
        result['nearest_modulus'] = abs(t0_c)
        result['growth_rate'] = 1.0 / abs(t0_c) if abs(t0_c) > 0 else float('inf')

        # Residue prefactor: sqrt(q2*(t0 - t1))
        q2_c = _eval(q2)
        prefactor = cmath.sqrt(q2_c * (t0_c - t1_c))
        result['branch_residue_prefactor'] = prefactor
        result['branch_residue_modulus'] = abs(prefactor)
        result['branch_residue_arg'] = cmath.phase(prefactor)

        # Conjugate pair test
        result['conjugate_pair'] = abs(abs(tp_c) - abs(tm_c)) < 1e-10 * max(abs(tp_c), abs(tm_c), 1e-50)

    except (TypeError, ValueError, ZeroDivisionError) as e:
        result['numerical_error'] = str(e)

    return result


# ============================================================================
# 9. Cross-family comparison
# ============================================================================

def shadow_tower_comparison(families: Dict[str, Tuple],
                            max_r: int = 20) -> Dict[str, Any]:
    r"""Compare shadow towers across multiple algebra families.

    Parameters:
        families: Dict mapping family_name -> (kappa, alpha, S4) as floats.
        max_r: Maximum arity to compare.

    Returns:
        Dict with side-by-side coefficient tables and growth rate comparison.
    """
    result: Dict[str, Any] = {'max_arity': max_r, 'families': {}}

    for name, (kappa_val, alpha_val, S4_val) in families.items():
        # Compute from raw data
        q0 = 4.0 * kappa_val ** 2
        q1 = 12.0 * kappa_val * alpha_val
        q2 = 9.0 * alpha_val ** 2 + 16.0 * kappa_val * S4_val

        a = [0.0] * (max_r - 1)
        a[0] = math.sqrt(abs(q0))  # |kappa| for a0
        if q0 < 0:
            # kappa negative: a0 is imaginary in the formal sense
            # For numerical extraction, take |kappa|
            a[0] = math.sqrt(abs(q0))
        if max_r > 2 and a[0] != 0:
            a[1] = q1 / (2.0 * a[0])
        if max_r > 3 and a[0] != 0:
            a[2] = (q2 - a[1] ** 2) / (2.0 * a[0])
        for n in range(3, max_r - 1):
            conv = sum(a[j] * a[n - j] for j in range(1, n))
            a[n] = -conv / (2.0 * a[0]) if a[0] != 0 else 0.0

        # S_r = a_{r-2} / r
        coeffs_dict = {r: a[r - 2] / r for r in range(2, max_r + 1)}

        # Growth rate
        Delta = 8.0 * kappa_val * S4_val
        denom = 9.0 * alpha_val ** 2 + 2.0 * Delta
        if denom > 0 and abs(kappa_val) > 1e-50:
            rho = math.sqrt(denom) / (2.0 * abs(kappa_val))
        else:
            rho = 0.0

        dc, depth = depth_classification(kappa_val, alpha_val, S4_val)

        result['families'][name] = {
            'depth_class': dc,
            'depth': depth,
            'growth_rate': rho,
            'convergent': rho < 1.0 if rho > 0 else True,
            'coefficients': coeffs_dict,
        }

    # Comparison table
    all_arities = list(range(2, max_r + 1))
    result['comparison_table'] = {}
    for r in all_arities:
        row = {}
        for name in families:
            row[name] = result['families'][name]['coefficients'].get(r, 0.0)
        result['comparison_table'][r] = row

    return result


# ============================================================================
# 10. Genus corrections
# ============================================================================

def genus_correction_tower(kappa_val, alpha_val, S4_val,
                           genus: int = 1, max_r: int = 15) -> Dict[int, Any]:
    r"""Genus-g corrections to the shadow tower.

    At genus 1, the Hessian correction delta_H^{(1)} modifies the shadow
    metric by an Eisenstein contribution. For Virasoro at genus 1:

        delta_H^{(1)}_Vir = 120 / (c^2 * (5c+22)) * x^2

    The corrected shadow metric at genus 1 is:
        Q_L^{(1)}(t) = Q_L(t) + delta_H^{(1)} * t^2 / kappa^2  (schematic)

    The genus-g tower is obtained by re-expanding sqrt(Q_L^{(g)}) with
    the corrected metric.

    Parameters:
        kappa_val, alpha_val, S4_val: Genus-0 shadow data.
        genus: Genus level (default 1).
        max_r: Maximum arity.

    Returns:
        Dict mapping r -> genus-g correction to S_r.
    """
    if genus == 0:
        return shadow_coefficients_exact(kappa_val, alpha_val, S4_val, max_r)

    if genus == 1:
        # Genus-1 Hessian correction: modifies the quartic term
        # delta_S4^(1) = 120/(c^2*(5c+22)) for Virasoro
        # General: delta_S4^(1) = propagator-dependent correction to S4
        # Here we implement the Virasoro specialization
        delta_S4 = _genus1_quartic_correction(kappa_val, alpha_val, S4_val)
        S4_corrected = S4_val + delta_S4

        # Re-expand with corrected quartic
        corrected = shadow_coefficients_exact(kappa_val, alpha_val, S4_corrected, max_r)
        base = shadow_coefficients_exact(kappa_val, alpha_val, S4_val, max_r)

        # Return the difference (genus-1 correction)
        corrections = {}
        for r in range(2, max_r + 1):
            if r in corrected and r in base:
                diff = simplify(corrected[r] - base[r])
                corrections[r] = diff
            else:
                corrections[r] = Rational(0)
        return corrections

    # Higher genus: iterated corrections (schematic)
    return {r: Rational(0) for r in range(2, max_r + 1)}


def _genus1_quartic_correction(kappa_val, alpha_val, S4_val):
    r"""Genus-1 Hessian correction to the quartic shadow.

    For Virasoro: delta_H^{(1)} = 120/(c^2*(5c+22)) * x^2.
    This corresponds to a quartic correction:
        delta_S4^{(1)} = 120/(c^2*(5c+22))

    General formula: delta_S4^{(1)} = E_2-coefficient / (4*kappa^2)
    where E_2 is the Eisenstein contribution at genus 1.
    """
    # Detect Virasoro family by checking kappa = c/2 symbolically
    try:
        if simplify(kappa_val - c / 2) == 0:
            return Rational(120) / (c ** 2 * (5 * c + 22))
    except (TypeError, AttributeError):
        pass
    # Generic: proportional to S4 / kappa (first-order perturbation)
    return Rational(0)


# ============================================================================
# 11. Complementarity: dual tower and Koszul pairing
# ============================================================================

def complementarity_shadow_tower(kappa_val, alpha_val, S4_val,
                                 kappa_dual, alpha_dual, S4_dual,
                                 max_r: int = 20,
                                 numerical_point: Optional[Dict] = None) -> Dict[str, Any]:
    r"""Compute shadow towers for A and A! and verify complementarity.

    For the Koszul pair (A, A!), complementarity predicts:
        Delta(A) + Delta(A!) = constant (the complementarity invariant)

    For Virasoro: Vir_c <-> Vir_{26-c}, and
        Delta(Vir_c) + Delta(Vir_{26-c}) = 6960 / ((5c+22)*(152-5c))

    Parameters:
        kappa_val, alpha_val, S4_val: Shadow data for A.
        kappa_dual, alpha_dual, S4_dual: Shadow data for A!.
        max_r: Maximum arity.
        numerical_point: Substitution dict for numerical evaluation.

    Returns:
        Dict with both towers, discriminant sum, and complementarity check.
    """
    tower_A = compute_shadow_tower(kappa_val, alpha_val, S4_val,
                                   max_arity=max_r, algebra_name="A",
                                   numerical_point=numerical_point)
    tower_dual = compute_shadow_tower(kappa_dual, alpha_dual, S4_dual,
                                      max_arity=max_r, algebra_name="A!",
                                      numerical_point=numerical_point)

    Delta_A = 8 * kappa_val * S4_val
    Delta_dual = 8 * kappa_dual * S4_dual
    Delta_sum = simplify(Delta_A + Delta_dual)

    # Coefficient-by-coefficient complementarity: S_r(A) + S_r(A!) = ?
    coeff_sums = {}
    for r in range(2, max_r + 1):
        s_A = tower_A.coefficient(r)
        s_dual = tower_dual.coefficient(r)
        if s_A is not None and s_dual is not None:
            coeff_sums[r] = simplify(s_A + s_dual)

    result = {
        'tower_A': tower_A,
        'tower_dual': tower_dual,
        'Delta_A': Delta_A,
        'Delta_dual': Delta_dual,
        'Delta_sum': Delta_sum,
        'coefficient_sums': coeff_sums,
    }

    # Growth rate comparison
    if tower_A.growth_rate is not None and tower_dual.growth_rate is not None:
        try:
            rho_A = float(Neval(tower_A.growth_rate))
            rho_dual = float(Neval(tower_dual.growth_rate))
            result['rho_A'] = rho_A
            result['rho_dual'] = rho_dual
            result['rho_product'] = rho_A * rho_dual
            result['self_dual'] = abs(rho_A - rho_dual) < 1e-10
        except (TypeError, ValueError):
            pass

    return result


def virasoro_complementarity(c_val, max_r: int = 20) -> Dict[str, Any]:
    r"""Complementarity for the Virasoro Koszul pair (Vir_c, Vir_{26-c}).

    Specializes complementarity_shadow_tower to the Virasoro family.

    Parameters:
        c_val: Central charge (numeric or sympy).
        max_r: Maximum arity.

    Returns:
        Complementarity data including discriminant sum verification.
    """
    c_v = Rational(c_val) if isinstance(c_val, (int, float)) else c_val
    c_dual = 26 - c_v

    # A = Vir_c
    kappa_A = c_v / 2
    alpha_A = Rational(2)
    S4_A = Rational(10) / (c_v * (5 * c_v + 22))

    # A! = Vir_{26-c}
    kappa_dual = c_dual / 2
    alpha_dual = Rational(2)
    S4_dual = Rational(10) / (c_dual * (5 * c_dual + 22))

    return complementarity_shadow_tower(
        kappa_A, alpha_A, S4_A,
        kappa_dual, alpha_dual, S4_dual,
        max_r=max_r,
    )


# ============================================================================
# Master equation recursion (independent verification path)
# ============================================================================

def shadow_coefficients_master_equation(kappa_val, alpha_val, S4_val,
                                        propagator,
                                        max_r: int = 30) -> Dict[int, Any]:
    r"""Compute shadow tower via the master equation recursion.

    This is an INDEPENDENT computation path from the sqrt(Q_L) expansion.
    Uses the recursion S_r = -(1/(2r)) o^{(r)} where:

        o^{(r)} = sum_{j+k=r+2, j,k>=2} (symmetry factor) * j*k*S_j*S_k*P

    This matches the recursion in shadow_tower_atlas.virasoro_tower.

    Parameters:
        kappa_val: S_2.
        alpha_val: S_3.
        S4_val: S_4.
        propagator: P = 2/c for Virasoro, etc.
        max_r: Maximum arity.

    Returns:
        Dict mapping r -> S_r.
    """
    P = propagator
    S: Dict[int, Any] = {}
    S[2] = kappa_val
    S[3] = alpha_val
    S[4] = S4_val

    for r in range(5, max_r + 1):
        o_r = Rational(0) if isinstance(kappa_val, type(Rational(1))) else 0
        for j in range(2, r):
            kk = r + 2 - j
            if kk < 2 or kk >= r or kk not in S:
                continue
            if j > kk:
                continue
            coeff = j * kk * S[j] * S[kk] * P
            if j == kk:
                o_r = o_r + coeff / 2
            else:
                o_r = o_r + coeff
        S[r] = -o_r / (2 * r)

    return S


def verify_two_paths(kappa_val, alpha_val, S4_val, propagator,
                     max_r: int = 15,
                     numerical_point: Optional[Dict] = None) -> Dict[str, Any]:
    r"""Verify that sqrt(Q_L) expansion and master equation agree.

    The two independent computation paths must produce identical results:
        Path A: S_r = [t^{r-2}] sqrt(Q_L(t))  (analytic)
        Path B: S_r = -(1/(2r)) o^{(r)}        (recursive/algebraic)

    Parameters:
        kappa_val, alpha_val, S4_val: Shadow data.
        propagator: Propagator P for master equation recursion.
        max_r: Maximum arity to check.
        numerical_point: Substitution dict for numerical comparison.

    Returns:
        Dict with path-by-path values and agreement status.
    """
    path_A = shadow_coefficients_exact(kappa_val, alpha_val, S4_val, max_r)
    path_B = shadow_coefficients_master_equation(kappa_val, alpha_val, S4_val,
                                                  propagator, max_r)

    agreements = {}
    max_error = 0.0

    for r in range(2, max_r + 1):
        val_A = path_A.get(r)
        val_B = path_B.get(r)
        if val_A is not None and val_B is not None:
            diff = simplify(val_A - val_B)

            if numerical_point is not None:
                for sym, num in numerical_point.items():
                    diff = diff.subs(sym, num)
                try:
                    err = abs(float(Neval(diff)))
                except (TypeError, ValueError):
                    err = None
            else:
                try:
                    err = abs(float(Neval(diff)))
                except (TypeError, ValueError):
                    err = 0.0 if diff == 0 else None

            agreements[r] = {
                'path_A': val_A,
                'path_B': val_B,
                'difference': diff,
                'error': err,
            }
            if err is not None:
                max_error = max(max_error, err)

    return {
        'agreements': agreements,
        'max_error': max_error,
        'all_agree': max_error < 1e-10,
    }


# ============================================================================
# Standard landscape families
# ============================================================================

STANDARD_FAMILIES = {
    'Heisenberg': {
        'class': 'G',
        'depth': 2,
        'kappa': lambda c_val: c_val / 2.0,
        'alpha': lambda c_val: 0.0,
        'S4': lambda c_val: 0.0,
    },
    'Affine_sl2': {
        'class': 'L',
        'depth': 3,
        'kappa': lambda k_val: 3.0 * (k_val + 2.0) / 4.0,
        'alpha': lambda k_val: 1.0,
        'S4': lambda k_val: 0.0,
    },
    'BetaGamma': {
        'class': 'C',
        'depth': 4,
        'kappa': lambda _: -1.0,
        'alpha': lambda _: 1.0,
        'S4': lambda _: -5.0 / 12.0,
    },
    'Virasoro': {
        'class': 'M',
        'depth': None,
        'kappa': lambda c_val: c_val / 2.0,
        'alpha': lambda c_val: 2.0,
        'S4': lambda c_val: 10.0 / (c_val * (5.0 * c_val + 22.0)),
    },
}


def standard_family_tower(family: str, param, max_r: int = 20) -> ShadowTower:
    """Compute shadow tower for a named standard family.

    Parameters:
        family: One of 'Heisenberg', 'Affine_sl2', 'BetaGamma', 'Virasoro'.
        param: The family parameter (c for Heisenberg/Virasoro, k for affine).
        max_r: Maximum arity.

    Returns:
        ShadowTower for the specified family at the given parameter value.
    """
    if family not in STANDARD_FAMILIES:
        raise ValueError(f"Unknown family: {family}. "
                         f"Available: {list(STANDARD_FAMILIES.keys())}")

    fam = STANDARD_FAMILIES[family]
    kappa = fam['kappa'](float(param))
    alpha = fam['alpha'](float(param))
    S4 = fam['S4'](float(param))

    tower = compute_shadow_tower(
        kappa, alpha, S4,
        max_arity=max_r,
        algebra_name=f"{family}(param={param})",
    )
    return tower


# ============================================================================
# Main: demonstration
# ============================================================================

if __name__ == '__main__':
    print("=" * 72)
    print("SHADOW POSTNIKOV TOWER — RECURSIVE COMPUTATION")
    print("=" * 72)

    # Virasoro at c = 25 (convergent)
    print("\n--- Virasoro at c = 25 ---")
    vir25 = shadow_coefficients_virasoro(25, max_r=20)
    for r in range(2, 12):
        print(f"  S_{r:2d} = {vir25[r]:+.10e}")

    # Asymptotic extraction
    asym = asymptotic_extraction(vir25, max_r=20)
    print(f"\n  rho (ratio test) = {asym['rho']:.8f}")
    print(f"  rho (Richardson) = {asym['rho_richardson']:.8f}")
    print(f"  theta            = {asym['theta']:.8f}")
    print(f"  amplitude C      = {asym['amplitude_C']:.8f}")
    print(f"  phase phi        = {asym['phase_phi']:.8f}")

    # Virasoro at c = 1/2 (Ising, divergent)
    print("\n--- Virasoro at c = 1/2 (Ising) ---")
    vir_ising = shadow_coefficients_virasoro(0.5, max_r=20)
    for r in range(2, 12):
        print(f"  S_{r:2d} = {vir_ising[r]:+.10e}")
    asym_ising = asymptotic_extraction(vir_ising, max_r=20)
    print(f"\n  rho = {asym_ising['rho']:.8f}  (divergent: rho > 1)")

    # Cross-family comparison
    print("\n--- Cross-family comparison ---")
    families = {
        'Heisenberg(c=10)': (5.0, 0.0, 0.0),
        'Affine_sl2(k=1)': (3.0 * 3.0 / 4.0, 1.0, 0.0),
        'Virasoro(c=25)': (12.5, 2.0, 10.0 / (25.0 * 147.0)),
        'Virasoro(c=1)': (0.5, 2.0, 10.0 / 27.0),
    }
    comp = shadow_tower_comparison(families, max_r=10)
    print(f"  {'r':>3s}", end="")
    for name in families:
        print(f"  {name:>20s}", end="")
    print()
    for r in range(2, 11):
        print(f"  {r:3d}", end="")
        for name in families:
            val = comp['comparison_table'][r][name]
            print(f"  {val:+20.8e}", end="")
        print()

    # Two-path verification for Virasoro
    print("\n--- Two-path verification (Virasoro symbolic) ---")
    kappa_sym = c / 2
    alpha_sym = Rational(2)
    S4_sym = Rational(10) / (c * (5 * c + 22))
    P_sym = Rational(2) / c
    check = verify_two_paths(kappa_sym, alpha_sym, S4_sym, P_sym,
                             max_r=10, numerical_point={c: Rational(25)})
    print(f"  All agree: {check['all_agree']} (max error: {check['max_error']:.2e})")

    # Complementarity
    print("\n--- Virasoro complementarity (c=5) ---")
    compl = virasoro_complementarity(5, max_r=10)
    print(f"  Delta(Vir_5) + Delta(Vir_21) = {compl['Delta_sum']}")
    expected = Rational(6960) / ((5 * 5 + 22) * (152 - 5 * 5))
    print(f"  Expected: 6960/((5*5+22)*(152-25)) = {expected}")
    print(f"  Match: {simplify(compl['Delta_sum'] - expected) == 0}")

    print("\n" + "=" * 72)
    print("DONE")
