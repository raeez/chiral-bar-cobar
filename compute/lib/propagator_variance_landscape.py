r"""Propagator variance landscape: delta_mix for all multi-generator algebras.

For a rank-r chiral algebra A with primary channels carrying curvature
kappa_a and quartic gradient f_a, the propagator variance is

    delta_mix = sum_a f_a^2/kappa_a - (sum_a f_a)^2 / (sum_a kappa_a)

Non-negative by Cauchy--Schwarz.  Vanishes iff f_a/kappa_a is constant
(enhanced symmetry = curvature-proportionality).

This module computes delta_mix for the COMPLETE standard landscape:

  (1) W_3 (T, W):                2 channels  [mixing polynomial P(W_3)]
  (2) W_4 (T, W_3, W_4):        3 channels  [mixing polynomial P(W_4)]
  (3) W_5 (T, W_3, W_4, W_5):   4 channels  [mixing polynomial P(W_5)]
  (4) betagamma + bc:            2 channels  [delta = 0, independent sum]
  (5) Heisenberg + Virasoro:     2 channels  [delta > 0, non-autonomous]
  (6) sl_2-hat + sl_3-hat:       2 channels  [delta = 0, both class L]

The ENHANCED SYMMETRY POINTS (zeros of the mixing polynomial) are new
structural invariants: central charges where the multi-channel shadow
tower simplifies to a single effective 1D ODE.

Key mathematical content:
  - For W_N: per-channel kappa_j = c/j (spin-j field).
  - Quartic via Lambda-exchange: Q_0 = 10/[c(5c+22)], alpha = 16/(5c+22).
  - Geometric-progression ansatz: f_j ~ Q_0 * alpha^{j-2} * (geo_sum)^3.
  - For independent sums (A oplus B with vanishing mixed OPE):
    shadows separate (prop:independent-sum-factorization), so delta_mix
    is computed from the individual channel data.
  - For class L algebras (affine KM): f = 0 by Jacobi identity, delta = 0.

Manuscript references:
    thm:propagator-variance (higher_genus_modular_koszul.tex)
    prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, S, Symbol, cancel, denom, factor, numer, oo,
    simplify, solve, sqrt, symbols, Poly, gcd,
)


c = Symbol('c')
k = Symbol('k')
lam = Symbol('lambda')


# ============================================================================
# Core propagator variance computation (standalone, no ChannelData dependency)
# ============================================================================

def propagator_variance(kappas: List, f_values: List) -> Any:
    r"""Compute delta_mix = sum f_i^2/kappa_i - (sum f_i)^2 / (sum kappa_i).

    Non-negative by Cauchy--Schwarz.  Single channel: always 0.
    """
    if len(kappas) <= 1:
        return S.Zero
    term1 = sum(f ** 2 / kap for f, kap in zip(f_values, kappas))
    term2 = sum(f_values) ** 2 / sum(kappas)
    return cancel(term1 - term2)


def mixing_polynomial(kappas: List, f_values: List, var=None) -> Any:
    r"""Extract the mixing polynomial P whose vanishing gives delta_mix = 0.

    P is the numerator of (f_1/kappa_1 - f_2/kappa_2), cleared of common
    factors with the denominator.  For r > 2 channels, P is the gcd of
    all pairwise (f_i/kappa_i - f_j/kappa_j) numerators.
    """
    if var is None:
        var = c
    if len(kappas) <= 1:
        return S.Zero
    # Collect all pairwise ratio differences
    ratio_nums = []
    for i in range(len(kappas)):
        for j in range(i + 1, len(kappas)):
            diff = cancel(f_values[i] / kappas[i] - f_values[j] / kappas[j])
            if diff != 0:
                ratio_nums.append(numer(cancel(diff)))
    if not ratio_nums:
        return S.Zero
    # The mixing polynomial is the gcd of all pairwise numerators
    # (the common factor that must vanish for ALL ratios to agree)
    P = ratio_nums[0]
    for num in ratio_nums[1:]:
        P = gcd(P, num, var)
    return factor(P)


def enhanced_symmetry_zeros(kappas: List, f_values: List, var=None) -> List:
    """Zeros of the mixing polynomial: central charges where delta_mix = 0."""
    if var is None:
        var = c
    P = mixing_polynomial(kappas, f_values, var)
    if P == 0:
        return []  # always autonomous
    return solve(P, var)


# ============================================================================
# W_N quartic structure from Lambda-exchange
# ============================================================================

def _wN_channel_data(N: int, cc=None):
    r"""Compute per-channel (kappa_j, f_j) for the principal W_N algebra.

    Channels: spin j = 2, 3, ..., N.
      kappa_j = c/j  (from W_j(z)W_j(w) ~ (c/j)/(z-w)^{2j} after
                       bar extraction: d log absorbs one pole order,
                       the r-matrix has leading pole z^{-(2j-1)}, and
                       kappa_j = Res_{z=0} z^0 r_j(z) = c/j).

    Quartic via Lambda-exchange geometric-progression ansatz:
      Q_0 = 10/[c(5c+22)]  (Virasoro quartic shadow)
      alpha = 16/(5c+22)    (Lambda coupling in WW OPE)

      The diagonal quartic is Sh_4|_{diag} = Q_0 * (sum alpha^{j-2})^4
      and the quartic gradient for channel s is
        f_s = 4 * Q_0 * alpha^{s-2} * (sum_{j=2}^N alpha^{j-2})^3.

    Returns (kappas, f_values, alpha, Q0, geo_sum).
    """
    if cc is None:
        cc = c
    if N < 2:
        raise ValueError(f"W_N requires N >= 2, got {N}")

    alpha_val = Rational(16) / (5 * cc + 22)
    Q0 = Rational(10) / (cc * (5 * cc + 22))
    geo_sum = sum(alpha_val ** (j - 2) for j in range(2, N + 1))

    kappas = [cc / j for j in range(2, N + 1)]
    f_values = [cancel(4 * Q0 * alpha_val ** (j - 2) * geo_sum ** 3)
                for j in range(2, N + 1)]

    return kappas, f_values, alpha_val, Q0, geo_sum


# ============================================================================
# Individual family computations
# ============================================================================

@dataclass
class VarianceResult:
    """Complete propagator variance data for one algebra family."""
    name: str
    rank: int
    channel_labels: List[str]
    channel_weights: List[int]
    kappas: List[Any]
    f_values: List[Any]
    delta_mix: Any
    mixing_poly: Any
    mixing_zeros: List[Any]
    total_kappa: Any
    is_autonomous: bool
    # For parametric families, the variable
    parameter: Any = None
    parameter_name: str = ''

    def verify_cauchy_schwarz(self, test_vals=None) -> bool:
        """Verify delta_mix >= 0 at a grid of parameter values."""
        d = self.delta_mix
        if simplify(d) == 0:
            return True
        if test_vals is None:
            test_vals = [Rational(1, 2), 1, 2, 5, 10, 13, 25, 50, 100]
        var = self.parameter if self.parameter is not None else c
        for v in test_vals:
            try:
                val = float(d.subs(var, v).evalf())
                if val < -1e-15:
                    return False
            except (TypeError, ValueError, ZeroDivisionError):
                continue
        return True


def w3_variance(cc=None) -> VarianceResult:
    r"""Propagator variance for W_3.

    Two channels: T (weight 2), W (weight 3).
      kappa_T = c/2,  kappa_W = c/3
      alpha = 16/(5c+22)
      Q_0 = 10/[c(5c+22)]

    Quartic gradients on diagonal:
      f_T = 4*Q_0*(1 + 3*alpha) = 200(c+14)/[c(5c+22)^2]
      f_W = 4*Q_0*alpha*(3 + alpha) = 640(15c+82)/[c(5c+22)^3]

    EXACT mixing polynomial: P(W_3) = 25c^2 + 100c - 428.

    We use the EXACT W_3 quartic structure (not the geometric-progression
    ansatz) because the Lambda-exchange for W_3 is completely understood.
    """
    if cc is None:
        cc = c
    alpha = Rational(16) / (5 * cc + 22)
    Q0 = Rational(10) / (cc * (5 * cc + 22))

    kappas = [cc / 2, cc / 3]
    # Exact quartic gradients from the W_3 Lambda-exchange structure
    f_T = cancel(4 * Q0 * (1 + 3 * alpha))
    f_W = cancel(4 * Q0 * alpha * (3 + alpha))
    f_values = [f_T, f_W]

    delta = propagator_variance(kappas, f_values)
    P = 25 * cc ** 2 + 100 * cc - 428
    zeros = solve(P, cc)

    return VarianceResult(
        name='W_3',
        rank=2,
        channel_labels=['T', 'W'],
        channel_weights=[2, 3],
        kappas=kappas,
        f_values=f_values,
        delta_mix=delta,
        mixing_poly=P,
        mixing_zeros=zeros,
        total_kappa=cancel(cc / 2 + cc / 3),
        is_autonomous=False,
        parameter=cc,
        parameter_name='c',
    )


def w4_variance(cc=None) -> VarianceResult:
    r"""Propagator variance for W_4.

    Three channels: T (wt 2), W_3 (wt 3), W_4 (wt 4).
      kappa_T = c/2,  kappa_3 = c/3,  kappa_4 = c/4

    Under the Lambda-exchange geometric-progression ansatz:
      alpha = 16/(5c+22)
      Q_0 = 10/[c(5c+22)]
      geo_sum = 1 + alpha + alpha^2
      f_j = 4*Q_0 * alpha^{j-2} * geo_sum^3

    The mixing polynomial is extracted from the pairwise ratio differences.
    For 3 channels, the GCD of (f_2/k_2 - f_3/k_3) and (f_2/k_2 - f_4/k_4)
    determines the common zero locus.
    """
    if cc is None:
        cc = c
    kappas, f_values, alpha, Q0, geo_sum = _wN_channel_data(4, cc)

    delta = propagator_variance(kappas, f_values)

    # For 3 channels, compute mixing polynomial as GCD
    P = mixing_polynomial(kappas, f_values, cc)
    zeros = solve(P, cc) if P != 0 else []

    return VarianceResult(
        name='W_4',
        rank=3,
        channel_labels=['T', 'W_3', 'W_4'],
        channel_weights=[2, 3, 4],
        kappas=kappas,
        f_values=f_values,
        delta_mix=delta,
        mixing_poly=P,
        mixing_zeros=zeros,
        total_kappa=cancel(sum(kappas)),
        is_autonomous=simplify(delta) == 0,
        parameter=cc,
        parameter_name='c',
    )


def w5_variance(cc=None) -> VarianceResult:
    r"""Propagator variance for W_5.

    Four channels: T (wt 2), W_3 (wt 3), W_4 (wt 4), W_5 (wt 5).
      kappa_j = c/j for j = 2, 3, 4, 5.
      Total kappa = c*(1/2 + 1/3 + 1/4 + 1/5) = c*77/60.

    Under the Lambda-exchange geometric-progression ansatz:
      alpha = 16/(5c+22)
      geo_sum = 1 + alpha + alpha^2 + alpha^3
      f_j = 4*Q_0 * alpha^{j-2} * geo_sum^3
    """
    if cc is None:
        cc = c
    kappas, f_values, alpha, Q0, geo_sum = _wN_channel_data(5, cc)

    delta = propagator_variance(kappas, f_values)
    P = mixing_polynomial(kappas, f_values, cc)
    zeros = solve(P, cc) if P != 0 else []

    return VarianceResult(
        name='W_5',
        rank=4,
        channel_labels=['T', 'W_3', 'W_4', 'W_5'],
        channel_weights=[2, 3, 4, 5],
        kappas=kappas,
        f_values=f_values,
        delta_mix=delta,
        mixing_poly=P,
        mixing_zeros=zeros,
        total_kappa=cancel(sum(kappas)),
        is_autonomous=simplify(delta) == 0,
        parameter=cc,
        parameter_name='c',
    )


def wN_variance(N: int, cc=None) -> VarianceResult:
    r"""Propagator variance for the principal W_N algebra (general N >= 2).

    N-1 channels at spins 2, ..., N.
      kappa_j = c/j
      Total kappa = c*(H_N - 1) where H_N = 1 + 1/2 + ... + 1/N.

    For N = 2 (Virasoro): single channel, delta = 0.
    For N >= 3: multi-channel with generically nonzero delta.
    """
    if cc is None:
        cc = c
    if N == 2:
        # Virasoro: single channel
        Q0 = Rational(10) / (cc * (5 * cc + 22))
        f_T = cancel(4 * Q0 * (cc / 2))  # = 20/(5c+22)
        return VarianceResult(
            name='Virasoro (W_2)',
            rank=1,
            channel_labels=['T'],
            channel_weights=[2],
            kappas=[cc / 2],
            f_values=[f_T],
            delta_mix=S.Zero,
            mixing_poly=S.Zero,
            mixing_zeros=[],
            total_kappa=cc / 2,
            is_autonomous=True,
            parameter=cc,
            parameter_name='c',
        )
    if N == 3:
        return w3_variance(cc)
    if N == 4:
        return w4_variance(cc)
    if N == 5:
        return w5_variance(cc)

    # General N
    kappas, f_values, alpha, Q0, geo_sum = _wN_channel_data(N, cc)
    delta = propagator_variance(kappas, f_values)
    P = mixing_polynomial(kappas, f_values, cc)
    zeros = solve(P, cc) if P != 0 else []
    labels = ['T'] + [f'W_{j}' for j in range(3, N + 1)]
    weights = list(range(2, N + 1))

    return VarianceResult(
        name=f'W_{N}',
        rank=N - 1,
        channel_labels=labels,
        channel_weights=weights,
        kappas=kappas,
        f_values=f_values,
        delta_mix=delta,
        mixing_poly=P,
        mixing_zeros=zeros,
        total_kappa=cancel(sum(kappas)),
        is_autonomous=simplify(delta) == 0,
        parameter=cc,
        parameter_name='c',
    )


def betagamma_bc_variance(ll=None) -> VarianceResult:
    r"""Propagator variance for betagamma + bc (independent sum).

    Two independent free-field systems with vanishing mixed OPE.
    By prop:independent-sum-factorization, shadows separate completely:
      kappa additive, quartic gradients additive (with zero cross-terms).

    betagamma: weight lambda, kappa = c_bg/2 = 6*lambda^2 - 6*lambda + 1.
      Class C (contact, r_max = 4). On the weight-changing line, f_bg = 0
      (cor:nms-betagamma-mu-vanishing). The quartic content lives on
      a charged stratum (stratum separation).

    bc ghosts: weight lambda, kappa = c_bc/2 = -(6*lambda^2 - 6*lambda + 1).
      Complementary system: kappa(bg) + kappa(bc) = 0.
      Class G/L. On the weight-changing line, f_bc = 0.

    Since both f_bg = f_bc = 0 on the neutral diagonal:
      delta_mix = 0 identically.

    Physical significance: the betagamma-bc system is ALWAYS autonomous
    on the neutral diagonal, regardless of conformal weight lambda.
    The non-trivial quartic structure lives on charged strata, not
    the neutral diagonal accessible to the propagator variance.
    """
    if ll is None:
        ll = lam
    kappa_bg = 6 * ll ** 2 - 6 * ll + 1
    kappa_bc = -(6 * ll ** 2 - 6 * ll + 1)

    kappas = [kappa_bg, kappa_bc]
    f_values = [S.Zero, S.Zero]

    return VarianceResult(
        name='betagamma + bc',
        rank=2,
        channel_labels=['bg', 'bc'],
        channel_weights=[1, 1],  # both weight-1 effective
        kappas=kappas,
        f_values=f_values,
        delta_mix=S.Zero,
        mixing_poly=S.Zero,
        mixing_zeros=[],
        total_kappa=cancel(kappa_bg + kappa_bc),  # = 0
        is_autonomous=True,
        parameter=ll,
        parameter_name='lambda',
    )


def heisenberg_virasoro_variance(cc=None) -> VarianceResult:
    r"""Propagator variance for Heisenberg + Virasoro (independent sum).

    Two systems with vanishing mixed OPE.
    By prop:independent-sum-factorization, shadows separate.

    Heisenberg: weight 1, kappa_H = 1 (standard level 1, c_H = 1).
      Class G (Gaussian, r_max = 2).  f_H = 0 (no quartic shadow).

    Virasoro: weight 2, kappa_V = c/2.
      Class M (mixed, r_max = infinity).
      Quartic shadow S4 = 10/[c(5c+22)].
      Quartic gradient on diagonal: f_V = 20/(5c+22).

    Propagator variance:
      delta_mix = f_V^2/kappa_V - f_V^2/(kappa_H + kappa_V)
               = f_V^2 * (1/kappa_V - 1/(kappa_H + kappa_V))
               = f_V^2 * kappa_H / (kappa_V * (kappa_H + kappa_V))

    Since f_H = 0, the Cauchy-Schwarz form simplifies:
      delta_mix = f_V^2/kappa_V - f_V^2/(1 + c/2)
               = (400/(5c+22)^2) * (2/c - 2/(c+2))
               = 1600 / (c(c+2)(5c+22)^2)

    This is STRICTLY POSITIVE for all c > 0: the Heisenberg + Virasoro
    system is NEVER autonomous.  The Gaussian channel (f_H = 0) always
    breaks curvature-proportionality with the M-class Virasoro channel.

    Enhanced symmetry: NONE.  delta_mix > 0 for all c > 0.  The mixing
    polynomial is a nonzero constant (degree 0), so there are no finite
    enhanced symmetry points.  This reflects the structural incompatibility
    of class G (terminates at arity 2) and class M (infinite tower).
    """
    if cc is None:
        cc = c

    kappa_H = S.One
    kappa_V = cc / 2
    f_H = S.Zero
    f_V = cancel(Rational(20) / (5 * cc + 22))

    kappas = [kappa_H, kappa_V]
    f_values = [f_H, f_V]

    delta = propagator_variance(kappas, f_values)

    # The mixing polynomial: f_H/kappa_H - f_V/kappa_V
    # = 0 - 40/[c(5c+22)] = -40/[c(5c+22)]
    # This is never zero for finite c > 0.
    # The "polynomial" is just -40 (the numerator after clearing c(5c+22)).
    # No zeros -> no enhanced symmetry points.
    P = mixing_polynomial(kappas, f_values, cc)

    return VarianceResult(
        name='Heisenberg + Virasoro',
        rank=2,
        channel_labels=['J', 'T'],
        channel_weights=[1, 2],
        kappas=kappas,
        f_values=f_values,
        delta_mix=delta,
        mixing_poly=P,
        mixing_zeros=[],
        total_kappa=cancel(1 + cc / 2),
        is_autonomous=False,
        parameter=cc,
        parameter_name='c',
    )


def affine_sl2_sl3_variance(k1=None, k2=None) -> VarianceResult:
    r"""Propagator variance for V_{k_1}(sl_2) + V_{k_2}(sl_3) (independent sum).

    Two affine Kac-Moody algebras with vanishing mixed OPE.
    Both are class L (Lie/tree, r_max = 3): the Jacobi identity kills
    the quartic shadow.  f = 0 for ALL affine KM algebras.

    sl_2: dim = 3, h^v = 2. kappa = dim*(k+h^v)/(2*h^v) = 3(k_1+2)/4.
    sl_3: dim = 8, h^v = 3. kappa = 8(k_2+3)/6 = 4(k_2+3)/3.

    delta_mix = 0 identically (both f_1 = f_2 = 0).

    This illustrates the general principle: the direct sum of class L
    algebras remains autonomous.  The Jacobi identity in each factor
    independently kills the quartic shadow, and since there are no
    mixed quartic terms (vanishing mixed OPE), the full system has
    zero quartic gradient.
    """
    if k1 is None:
        k1 = Symbol('k_1')
    if k2 is None:
        k2 = Symbol('k_2')

    # kappa formulas: kappa = dim(g)*(k+h^v)/(2*h^v)
    kappa_sl2 = Rational(3) * (k1 + 2) / 4
    kappa_sl3 = Rational(4) * (k2 + 3) / 3

    kappas = [kappa_sl2, kappa_sl3]
    f_values = [S.Zero, S.Zero]

    return VarianceResult(
        name='V_{k_1}(sl_2) + V_{k_2}(sl_3)',
        rank=2,
        channel_labels=['J^{sl_2}', 'J^{sl_3}'],
        channel_weights=[1, 1],
        kappas=kappas,
        f_values=f_values,
        delta_mix=S.Zero,
        mixing_poly=S.Zero,
        mixing_zeros=[],
        total_kappa=cancel(kappa_sl2 + kappa_sl3),
        is_autonomous=True,
        parameter=None,
        parameter_name='(k_1, k_2)',
    )


# ============================================================================
# Full landscape computation
# ============================================================================

def full_landscape(cc=None) -> Dict[str, VarianceResult]:
    """Compute propagator variance for all six multi-generator families."""
    if cc is None:
        cc = c
    return {
        'W_3': w3_variance(cc),
        'W_4': w4_variance(cc),
        'W_5': w5_variance(cc),
        'bg_bc': betagamma_bc_variance(),
        'heis_vir': heisenberg_virasoro_variance(cc),
        'sl2_sl3': affine_sl2_sl3_variance(),
    }


def landscape_summary(cc=None) -> str:
    """Human-readable summary of the propagator variance landscape."""
    results = full_landscape(cc)
    lines = [
        "PROPAGATOR VARIANCE LANDSCAPE",
        "=" * 60,
    ]
    for key, res in results.items():
        lines.append(f"\n{res.name} (rank {res.rank}):")
        for i, label in enumerate(res.channel_labels):
            lines.append(f"  {label} (wt {res.channel_weights[i]}): "
                         f"kappa = {res.kappas[i]}, f = {res.f_values[i]}")
        lines.append(f"  Total kappa: {res.total_kappa}")
        lines.append(f"  delta_mix: {res.delta_mix}")
        lines.append(f"  Autonomous: {res.is_autonomous}")
        if res.mixing_poly != 0:
            lines.append(f"  Mixing polynomial: {res.mixing_poly}")
        if res.mixing_zeros:
            lines.append(f"  Enhanced symmetry zeros: {res.mixing_zeros}")
        cs_ok = res.verify_cauchy_schwarz()
        lines.append(f"  Cauchy-Schwarz: {'PASS' if cs_ok else 'FAIL'}")
    return '\n'.join(lines)


# ============================================================================
# Numerical evaluation across families
# ============================================================================

def evaluate_at(c_val, cc=None) -> Dict[str, float]:
    """Evaluate delta_mix for all multi-channel families at a given c value."""
    if cc is None:
        cc = c
    results = {}
    for key, res in [('W_3', w3_variance(cc)),
                     ('W_4', w4_variance(cc)),
                     ('W_5', w5_variance(cc)),
                     ('heis_vir', heisenberg_virasoro_variance(cc))]:
        try:
            val = float(res.delta_mix.subs(cc, c_val).evalf())
            results[key] = val
        except (TypeError, ValueError, ZeroDivisionError):
            results[key] = None
    results['bg_bc'] = 0.0
    results['sl2_sl3'] = 0.0
    return results


# ============================================================================
# W_N mixing polynomial growth analysis
# ============================================================================

def wN_mixing_poly_degree(N: int, cc=None) -> int:
    """Degree of the mixing polynomial for W_N."""
    res = wN_variance(N, cc)
    P = res.mixing_poly
    if P == 0:
        return -1
    return Poly(P, cc if cc is not None else c).degree()


def wN_enhanced_symmetry_count(N: int) -> int:
    """Number of enhanced symmetry points for W_N."""
    res = wN_variance(N)
    return len(res.mixing_zeros)


# ============================================================================
# Runner
# ============================================================================

if __name__ == '__main__':
    print(landscape_summary())
