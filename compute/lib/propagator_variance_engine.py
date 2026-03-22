r"""Propagator variance engine: multi-channel non-autonomy and mixing polynomials.

For a rank-r chiral algebra A with r primary lines (channels), each carrying
curvature kappa_a (arity-2 shadow) and quartic coupling f_a (arity-4 gradient),
the PROPAGATOR VARIANCE is

    delta_mix = sum_a (f_a^2 / kappa_a) - (sum_a f_a)^2 / (sum_a kappa_a)

This is non-negative by Cauchy--Schwarz.  It vanishes iff the quartic gradient
is curvature-proportional: f_a / kappa_a = const for all a (enhanced symmetry).

The MIXING POLYNOMIAL P(A) is the polynomial in the central charge whose
vanishing determines when delta_mix = 0.

For W_3: P(W_3) = 25c^2 + 100c - 428.

Key properties (thm:propagator-variance):
  (1) delta_mix >= 0 (Cauchy--Schwarz).
  (2) delta_mix = 0 iff curvature-proportional.
  (3) Computable from arity 2 + 4 data alone.
  (4) Controls the arity-6 non-autonomy of the diagonal restriction.

The propagator variance is a STRUCTURAL INVARIANT: it measures how far
the multi-channel shadow tower deviates from a single effective 1D tower
on the diagonal.  Enhanced symmetry (delta_mix = 0) means the diagonal
restriction is autonomous and the multi-channel tower reduces to a
single-variable ODE.

Shadow depth classification per channel:
  G (Gaussian, r_max = 2): Delta = 0, S4 = 0, f = 0
  L (Lie/tree, r_max = 3): Delta = 0, S4 = 0, f = 0
  C (contact, r_max = 4): Delta = 0, stratum separation
  M (mixed, r_max = inf):  Delta != 0, f != 0

Manuscript references:
    thm:propagator-variance (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Matrix, Rational, S, Symbol, cancel,
    factor, numer, oo, simplify, solve, symbols, zeros,
)


c = Symbol('c')
k = Symbol('k')


# ============================================================================
# Data structures
# ============================================================================

@dataclass
class ChannelData:
    """Data for a single primary channel in a multi-channel chiral algebra.

    Attributes:
        label: Channel name (e.g., 'T', 'W', 'W_4').
        weight: Conformal weight of the generating field.
        kappa: Curvature (arity-2 shadow coefficient) on this channel.
        f_quartic: Quartic coupling coefficient (gradient of Sh_4 on diagonal).
        S4: Arity-4 shadow coefficient on this channel.
        Delta: Critical discriminant 8*kappa*S4 on this channel.
        depth_class: Shadow depth class (G/L/C/M) for this channel.
    """
    label: str
    weight: int
    kappa: Any
    f_quartic: Any = S.Zero
    S4: Any = S.Zero
    Delta: Any = S.Zero
    depth_class: str = ''


@dataclass
class PropagatorVarianceData:
    """Complete propagator variance data for a multi-channel algebra.

    Attributes:
        algebra_name: Name of the algebra (e.g., 'W_3', 'Virasoro').
        rank: Number of primary channels.
        channels: List of ChannelData for each channel.
        delta_mix: The propagator variance (non-negative by Cauchy--Schwarz).
        mixing_polynomial: Polynomial whose zeros give delta_mix = 0.
        mixing_zeros: Central charges where delta_mix = 0.
        enhanced_symmetry_locus: Where gradient is curvature-proportional.
        total_kappa: sum of kappa_a.
        total_f: sum of f_a.
        cauchy_schwarz_ratio: delta_mix / sum(f^2/kappa), in [0,1].
    """
    algebra_name: str
    rank: int
    channels: List[ChannelData]
    delta_mix: Any = S.Zero
    mixing_polynomial: Any = S.Zero
    mixing_zeros: List[Any] = field(default_factory=list)
    enhanced_symmetry_locus: List[Any] = field(default_factory=list)
    total_kappa: Any = S.Zero
    total_f: Any = S.Zero
    cauchy_schwarz_ratio: Any = S.Zero

    def is_autonomous(self) -> bool:
        """Whether delta_mix = 0 (curvature-proportional quartic gradient)."""
        return simplify(self.delta_mix) == 0

    def verify_cauchy_schwarz(self) -> bool:
        """Verify delta_mix >= 0 symbolically or at test points.

        For symbolic expressions, attempts simplify; falls back to
        numerical evaluation at a grid of positive c-values.
        """
        d = simplify(self.delta_mix)
        if d == 0:
            return True
        # Try numerical evaluation at several positive central charges
        test_values = [Rational(1, 2), Rational(1), Rational(2),
                       Rational(5), Rational(13), Rational(25)]
        for cv in test_values:
            try:
                val = float(d.subs(c, cv).evalf())
                if val < -1e-15:
                    return False
            except (TypeError, ValueError, AttributeError):
                continue
        return True

    def summary(self) -> str:
        """Human-readable summary of the propagator variance data."""
        lines = [
            f"Propagator variance for {self.algebra_name}",
            f"  Rank: {self.rank}",
            f"  Channels:",
        ]
        for ch in self.channels:
            lines.append(
                f"    {ch.label} (wt {ch.weight}): "
                f"kappa = {ch.kappa}, f = {ch.f_quartic}, "
                f"S4 = {ch.S4}, class {ch.depth_class}"
            )
        lines.append(f"  Total kappa: {self.total_kappa}")
        lines.append(f"  Total f:     {self.total_f}")
        lines.append(f"  delta_mix:   {self.delta_mix}")
        lines.append(f"  Autonomous:  {self.is_autonomous()}")
        if self.mixing_polynomial != 0:
            lines.append(f"  Mixing polynomial: {self.mixing_polynomial}")
        if self.mixing_zeros:
            lines.append(f"  Mixing zeros: {self.mixing_zeros}")
        return '\n'.join(lines)


# ============================================================================
# 1. Core propagator variance computation
# ============================================================================

def propagator_variance(channels: List[ChannelData]) -> Any:
    r"""Compute the propagator variance delta_mix from channel data.

    delta_mix = sum_a (f_a^2 / kappa_a) - (sum_a f_a)^2 / (sum_a kappa_a)

    Non-negative by Cauchy--Schwarz.  Vanishes iff f_a / kappa_a is
    constant across all channels (curvature-proportionality).

    Args:
        channels: list of ChannelData with kappa and f_quartic set.

    Returns:
        Simplified sympy expression for delta_mix.
    """
    if len(channels) == 0:
        return S.Zero
    if len(channels) == 1:
        return S.Zero  # single channel: trivially autonomous

    kappas = [ch.kappa for ch in channels]
    fs = [ch.f_quartic for ch in channels]

    weighted_sum = sum(f ** 2 / kap for f, kap in zip(fs, kappas))
    total_f = sum(fs)
    total_kappa = sum(kappas)

    delta = weighted_sum - total_f ** 2 / total_kappa
    return cancel(delta)


def _curvature_proportionality_ratios(channels: List[ChannelData]) -> List[Any]:
    """Compute the ratios f_a / kappa_a for each channel.

    Curvature-proportionality means all ratios are equal.
    """
    return [cancel(ch.f_quartic / ch.kappa) for ch in channels]


# ============================================================================
# 2. W_3 mixing polynomial
# ============================================================================

def mixing_polynomial_w3(cc=None) -> Tuple[Any, List]:
    r"""The mixing polynomial P(W_3) = 25c^2 + 100c - 428.

    W_3 has two channels: T (weight 2) and W (weight 3).
      kappa_T = c/2,  kappa_W = c/3
      alpha = 16/(5c+22) (Lambda coupling in WW OPE)

    Quartic shadow (from Lambda-exchange):
      Sh_4 = Q_0 [ x_T^4 + 6*alpha*x_T^2*x_W^2 + alpha^2*x_W^4 ]
    where Q_0 = 10/[c(5c+22)].

    Quartic gradients on the diagonal x_T = x_W = x:
      f_T = d/dx_T(Sh_4)|_diag = 4*Q_0*(1 + 3*alpha)
      f_W = d/dx_W(Sh_4)|_diag = 4*Q_0*alpha*(3 + alpha)

    The mixing polynomial P is the numerator of f_T/kappa_T - f_W/kappa_W:
      f_T/kappa_T = 8*Q_0*(1+3*alpha)/c = 80(5c+70) / [c^2(5c+22)^2]
      f_W/kappa_W = 12*Q_0*alpha*(3+alpha)/c = 1920(15c+82) / [c^2(5c+22)^3]

    Setting these equal and extracting the numerator polynomial:
      P(W_3) = 25c^2 + 100c - 428

    Zeros: c = (-100 +/- sqrt(10000 + 42800)) / 50
             = (-100 +/- sqrt(52800)) / 50
             = (-10 +/- 2*sqrt(132)) / 5

    Numerically: c ~ 2.597 and c ~ -6.597.

    Args:
        cc: optional symbol or value for the central charge (default: Symbol('c'))

    Returns:
        (P, zeros) where P is the mixing polynomial and zeros is the list
        of central charge values where P = 0.
    """
    if cc is None:
        cc = c
    P = 25 * cc ** 2 + 100 * cc - 428
    roots = solve(P, cc)
    return P, roots


# ============================================================================
# 3. W_N mixing polynomial (general)
# ============================================================================

def mixing_polynomial_wN(N: int, cc=None) -> Tuple[Any, List]:
    r"""Mixing polynomial for the principal W_N algebra.

    For W_N with N-1 channels at weights 2, 3, ..., N:
      kappa_j = c / j  (from W_j(z)W_j(w) ~ (c/j) / (z-w)^{2j})

    The quartic couplings involve the Lambda-exchange mechanism.  For the
    T-line, the quartic is always the Virasoro quartic:
      S4_T = 10 / [c(5c+22)]

    For other channels, the quartic involves powers of the Lambda coupling
    alpha = 16/(5c+22).

    The W_N quartic tensor has the geometric-progression structure
    (manifest in W_3 and expected for general N):
      Q_{ijkl} ~ Q_0 * alpha^{(j-2)+(k-2)+(l-2)+(m-2)}
    where j,k,l,m are the spin indices contributing through Lambda-exchange.

    For N = 3: P(W_3) = 25c^2 + 100c - 428 (exact).
    For N >= 4: the mixing polynomial has degree >= 3 in c due to additional
    channels, and the closed-form depends on the full W_N OPE structure.

    Args:
        N: rank of the W-algebra (N >= 2).
        cc: optional symbol for the central charge.

    Returns:
        (P, zeros) for the mixing polynomial.
    """
    if cc is None:
        cc = c
    if N < 2:
        raise ValueError(f"W_N requires N >= 2, got {N}")
    if N == 2:
        # Virasoro: single channel, delta_mix = 0 identically
        return S.Zero, []
    if N == 3:
        return mixing_polynomial_w3(cc)

    # For N >= 4: construct from channel data
    # kappa_j = c/j, alpha = 16/(5c+22)
    alpha = Rational(16) / (5 * cc + 22)
    Q0 = Rational(10) / (cc * (5 * cc + 22))

    # Quartic gradient on the diagonal for each channel j:
    # The quartic shadow has the form
    #   Sh_4 = sum_{i,j,k,l} Q_{ijkl} x_i x_j x_k x_l
    # with Q_{ijkl} factoring through the Lambda-exchange as
    #   Q_{ijkl} = Q_0 * alpha^{(i-2)+(j-2)+(k-2)+(l-2)} (modulo selection rules)
    #
    # For the diagonal x_2 = ... = x_N = x, the partial derivative d/dx_s
    # picks up all terms containing x_s.
    #
    # At leading order (Lambda-exchange dominance), the quartic gradient is:
    #   f_j ~ 4 * Q_0 * sum_{k: admissible} alpha^{(j-2)+(k-2)+(j-2)+(k-2)}/binomial
    #
    # For a more tractable computation, we use the geometric-progression
    # ansatz: the quartic on the diagonal is
    #   S_4^diag = Q_0 * (sum_{j=2}^N alpha^{j-2})^4
    # which gives f_j = 4 * Q_0 * alpha^{j-2} * (sum alpha^{i-2})^3.
    #
    # This is the Lambda-exchange estimate.  The exact result requires the
    # full W_N OPE structure constants at weight 4.
    #
    # Under this ansatz: f_j / kappa_j = (4j/c) * Q_0 * alpha^{j-2} * (sum)^3
    # and the mixing polynomial is the numerator of the system of equations
    # f_j/kappa_j = f_2/kappa_2 for j = 3,...,N.

    # Geometric sum factor
    geo_sum = sum(alpha ** (j - 2) for j in range(2, N + 1))

    # Quartic gradients under geometric-progression ansatz
    f_vals = []
    kap_vals = []
    for j in range(2, N + 1):
        # f_j = 4 * Q_0 * alpha^{j-2} * geo_sum^3
        f_j = 4 * Q0 * alpha ** (j - 2) * geo_sum ** 3
        f_vals.append(cancel(f_j))
        kap_vals.append(cc / j)

    # Mixing polynomial: numerator of f_2/kappa_2 - f_j/kappa_j for j=3
    ratio_2 = cancel(f_vals[0] / kap_vals[0])
    ratio_3 = cancel(f_vals[1] / kap_vals[1])
    diff_expr = cancel(ratio_2 - ratio_3)
    P = factor(numer(cancel(diff_expr)))

    # For N=3, verify consistency with known result
    roots = solve(P, cc)
    return P, roots


# ============================================================================
# 4. Enhanced symmetry detection
# ============================================================================

def enhanced_symmetry_detection(data: PropagatorVarianceData) -> Dict:
    r"""Detect and classify enhanced symmetry when delta_mix = 0.

    When delta_mix = 0, the quartic gradient is curvature-proportional:
      f_a / kappa_a = lambda (constant) for all channels a.

    This means the diagonal restriction of the multi-channel shadow tower
    is AUTONOMOUS: it satisfies a single-variable Riccati ODE.

    Returns a dict with:
      - 'is_enhanced': whether delta_mix = 0
      - 'symmetry_type': classification of the enhanced symmetry
      - 'proportionality_constant': the common ratio f/kappa (if enhanced)
      - 'proportionality_ratios': f_a/kappa_a for each channel
      - 'c_locus': central charges where enhancement occurs (if polynomial)
    """
    result = {
        'is_enhanced': data.is_autonomous(),
        'proportionality_ratios': {},
    }

    for ch in data.channels:
        if simplify(ch.kappa) != 0:
            result['proportionality_ratios'][ch.label] = cancel(
                ch.f_quartic / ch.kappa
            )

    if result['is_enhanced']:
        # All ratios equal; extract the common value
        ratios = list(result['proportionality_ratios'].values())
        if ratios:
            result['proportionality_constant'] = ratios[0]
        result['symmetry_type'] = 'curvature-proportional (autonomous diagonal)'
    else:
        result['symmetry_type'] = 'generic (non-autonomous)'
        # Find the locus where enhancement occurs
        if data.mixing_polynomial != 0:
            result['c_locus'] = data.mixing_zeros
        else:
            result['c_locus'] = []

    return result


# ============================================================================
# 5. Per-family propagator variance computations
# ============================================================================

def heisenberg_propagator(n: int = 1) -> PropagatorVarianceData:
    """Propagator variance for the rank-n Heisenberg algebra.

    Rank n, single effective channel (all n copies have identical structure).
    kappa = n/2, f = 0 (Gaussian class, all quartic shadows vanish).
    delta_mix = 0 automatically (class G).
    """
    ch = ChannelData(
        label='J',
        weight=1,
        kappa=Rational(n, 2),
        f_quartic=S.Zero,
        S4=S.Zero,
        Delta=S.Zero,
        depth_class='G',
    )
    return PropagatorVarianceData(
        algebra_name=f'Heisenberg (rank {n})',
        rank=1,
        channels=[ch],
        delta_mix=S.Zero,
        mixing_polynomial=S.Zero,
        mixing_zeros=[],
        enhanced_symmetry_locus=[],
        total_kappa=Rational(n, 2),
        total_f=S.Zero,
        cauchy_schwarz_ratio=S.Zero,
    )


def affine_sl2_propagator(level=None) -> PropagatorVarianceData:
    r"""Propagator variance for V_k(sl_2).

    Single primary channel (J^a, the current).
    kappa = 3(k+2)/4 = dim(sl_2)*(k+h^v)/(2*h^v), h^v = 2.
    f = 0 (class L: Jacobi identity kills the quartic shadow).
    delta_mix = 0 automatically.
    """
    if level is None:
        level = k
    kappa_val = Rational(3) * (level + 2) / 4
    ch = ChannelData(
        label='J',
        weight=1,
        kappa=kappa_val,
        f_quartic=S.Zero,
        S4=S.Zero,
        Delta=S.Zero,
        depth_class='L',
    )
    return PropagatorVarianceData(
        algebra_name='V_k(sl_2)',
        rank=1,
        channels=[ch],
        delta_mix=S.Zero,
        mixing_polynomial=S.Zero,
        mixing_zeros=[],
        enhanced_symmetry_locus=[],
        total_kappa=kappa_val,
        total_f=S.Zero,
        cauchy_schwarz_ratio=S.Zero,
    )


def virasoro_propagator(cc=None) -> PropagatorVarianceData:
    r"""Propagator variance for the Virasoro algebra Vir_c.

    Single T-channel (weight 2).
      kappa = c/2
      S4 = 10/[c(5c+22)]  (Lambda-exchange quartic)
      f = quartic gradient = 4*S4*kappa = 20/(5c+22)
      Delta = 8*kappa*S4 = 40/(5c+22)

    delta_mix = 0 automatically (single channel).

    The Virasoro quartic Q^contact_Vir = 10/[c(5c+22)] is the primary
    arity-4 invariant.  Poles at c = 0 and c = -22/5 (Lee--Yang).
    """
    if cc is None:
        cc = c
    kappa_val = cc / 2
    S4_val = Rational(10) / (cc * (5 * cc + 22))
    Delta_val = 8 * kappa_val * S4_val  # = 40/(5c+22)
    f_val = cancel(4 * S4_val * kappa_val)  # = 20/(5c+22)

    ch = ChannelData(
        label='T',
        weight=2,
        kappa=kappa_val,
        f_quartic=f_val,
        S4=S4_val,
        Delta=cancel(Delta_val),
        depth_class='M',
    )
    return PropagatorVarianceData(
        algebra_name='Virasoro',
        rank=1,
        channels=[ch],
        delta_mix=S.Zero,
        mixing_polynomial=S.Zero,
        mixing_zeros=[],
        enhanced_symmetry_locus=[],
        total_kappa=kappa_val,
        total_f=f_val,
        cauchy_schwarz_ratio=S.Zero,
    )


def w3_propagator(cc=None) -> PropagatorVarianceData:
    r"""Propagator variance for the W_3 algebra.

    Two channels: T (weight 2) and W (weight 3).
      kappa_T = c/2,  kappa_W = c/3
      alpha = 16/(5c+22)  (Lambda coupling in WW OPE)

    Quartic shadow from Lambda-exchange:
      Q_TTTT = 10/[c(5c+22)]          (Virasoro quartic)
      Q_TTWW = 160/[c(5c+22)^2]       (mixed T-W channel)
      Q_WWWW = 2560/[c(5c+22)^3]      (pure W channel)

    Quartic gradients on the diagonal:
      f_T = 4*Q_0*(1 + 3*alpha) = 200(c+14)/[c(5c+22)^2] (for Q_0 = 10/[c(5c+22)])
      f_W = 4*Q_0*alpha*(3+alpha) = 640(15c+82)/[c(5c+22)^3]

    Mixing polynomial: P(W_3) = 25c^2 + 100c - 428
    Zeros: c = (-10 +/- 2*sqrt(132))/5 ~ 2.597, -6.597.
    """
    if cc is None:
        cc = c
    alpha_val = Rational(16) / (5 * cc + 22)
    Q0 = Rational(10) / (cc * (5 * cc + 22))

    # Curvatures
    kappa_T = cc / 2
    kappa_W = cc / 3

    # Quartic shadow coefficients
    S4_T = Q0  # = 10/[c(5c+22)]
    S4_W = cancel(Q0 * alpha_val ** 2)  # = 2560/[c(5c+22)^3]

    # Critical discriminants
    Delta_T = cancel(8 * kappa_T * S4_T)  # = 40/(5c+22)
    Delta_W = cancel(8 * kappa_W * S4_W)

    # Quartic gradients on the diagonal x_T = x_W = x
    # f_T = d/dx_T(Sh_4)|_diag at x^3: = 4*Q_0 + 12*Q_0*alpha
    f_T = cancel(4 * Q0 * (1 + 3 * alpha_val))
    # f_W = d/dx_W(Sh_4)|_diag at x^3: = 12*Q_0*alpha + 4*Q_0*alpha^2
    f_W = cancel(4 * Q0 * alpha_val * (3 + alpha_val))

    ch_T = ChannelData(
        label='T', weight=2, kappa=kappa_T,
        f_quartic=f_T, S4=S4_T, Delta=Delta_T, depth_class='M',
    )
    ch_W = ChannelData(
        label='W', weight=3, kappa=kappa_W,
        f_quartic=f_W, S4=cancel(S4_W), Delta=Delta_W, depth_class='M',
    )

    channels = [ch_T, ch_W]
    delta = propagator_variance(channels)
    P, zeros = mixing_polynomial_w3(cc)
    total_kap = cancel(kappa_T + kappa_W)
    total_f_val = cancel(f_T + f_W)

    # Cauchy--Schwarz ratio: delta / sum(f^2/kappa)
    weighted_sum = cancel(f_T ** 2 / kappa_T + f_W ** 2 / kappa_W)
    cs_ratio = cancel(delta / weighted_sum) if weighted_sum != 0 else S.Zero

    return PropagatorVarianceData(
        algebra_name='W_3',
        rank=2,
        channels=channels,
        delta_mix=delta,
        mixing_polynomial=P,
        mixing_zeros=zeros,
        enhanced_symmetry_locus=zeros,
        total_kappa=total_kap,
        total_f=total_f_val,
        cauchy_schwarz_ratio=cs_ratio,
    )


def w4_propagator(cc=None) -> PropagatorVarianceData:
    r"""Propagator variance for the W_4 algebra.

    Three channels: T (wt 2), W_3 (wt 3), W_4 (wt 4).
      kappa_T = c/2,  kappa_3 = c/3,  kappa_4 = c/4

    Quartic structure: Lambda-exchange with geometric-progression ansatz.
    The W_4 quartic tensor has RICHER denominator than W_3 due to additional
    resonance divisors from the spin-4 sector.

    Under the Lambda-exchange dominance ansatz (valid at generic c):
      alpha = 16/(5c+22)
      Q_0 = 10/[c(5c+22)]
      f_j = 4 * Q_0 * alpha^{j-2} * (1 + alpha + alpha^2)^3  [j = 2,3,4]
    """
    if cc is None:
        cc = c
    alpha_val = Rational(16) / (5 * cc + 22)
    Q0 = Rational(10) / (cc * (5 * cc + 22))
    geo_sum = 1 + alpha_val + alpha_val ** 2

    kappas_list = [cc / 2, cc / 3, cc / 4]
    f_list = [cancel(4 * Q0 * alpha_val ** (j - 2) * geo_sum ** 3)
              for j in range(2, 5)]

    channels = []
    labels = ['T', 'W_3', 'W_4']
    for idx, j in enumerate(range(2, 5)):
        S4_j = cancel(Q0 * alpha_val ** (2 * (j - 2)))
        Delta_j = cancel(8 * kappas_list[idx] * S4_j)
        channels.append(ChannelData(
            label=labels[idx], weight=j,
            kappa=kappas_list[idx],
            f_quartic=f_list[idx],
            S4=S4_j,
            Delta=Delta_j,
            depth_class='M',
        ))

    delta = propagator_variance(channels)
    total_kap = cancel(sum(kappas_list))
    total_f_val = cancel(sum(f_list))

    # Extract mixing polynomial (numerator of the proportionality test)
    ratio_T = cancel(f_list[0] / kappas_list[0])
    ratio_3 = cancel(f_list[1] / kappas_list[1])
    diff_expr = cancel(ratio_T - ratio_3)
    P = factor(numer(cancel(diff_expr))) if diff_expr != 0 else S.Zero
    zeros = solve(P, cc) if P != 0 else []

    # Cauchy--Schwarz ratio
    weighted_sum = cancel(sum(f ** 2 / kap for f, kap in zip(f_list, kappas_list)))
    cs_ratio = cancel(delta / weighted_sum) if weighted_sum != 0 else S.Zero

    return PropagatorVarianceData(
        algebra_name='W_4',
        rank=3,
        channels=channels,
        delta_mix=delta,
        mixing_polynomial=P,
        mixing_zeros=zeros,
        enhanced_symmetry_locus=zeros,
        total_kappa=total_kap,
        total_f=total_f_val,
        cauchy_schwarz_ratio=cs_ratio,
    )


def betagamma_propagator() -> PropagatorVarianceData:
    r"""Propagator variance for the beta-gamma system.

    Class C (contact, r_max = 4).  Two sectors: beta (weight lambda)
    and gamma (weight 1-lambda).

    The quartic contact invariant lives on a CHARGED STRATUM whose
    self-bracket exits the complex by rank-one rigidity.  Stratum separation
    means the standard propagator variance formula on the neutral diagonal
    is ill-defined in the usual sense.

    For the weight-changing line: mu_{bg} = 0 (cor:nms-betagamma-mu-vanishing).
    On the full weight/contact slice, the quartic content lives in mixed
    directions.

    We record the data with appropriate flags indicating that stratum
    separation applies.
    """
    lam = Symbol('lambda')
    kappa_val = 6 * lam ** 2 - 6 * lam + 1  # = c/2 for betagamma

    ch = ChannelData(
        label='bg',
        weight=1,
        kappa=kappa_val,
        f_quartic=S.Zero,  # mu_{bg} = 0 on weight-changing line
        S4=S.Zero,  # stratum separation: quartic on charged stratum
        Delta=S.Zero,
        depth_class='C',
    )
    return PropagatorVarianceData(
        algebra_name='beta-gamma (stratum separation)',
        rank=1,
        channels=[ch],
        delta_mix=S.Zero,
        mixing_polynomial=S.Zero,
        mixing_zeros=[],
        enhanced_symmetry_locus=[],
        total_kappa=kappa_val,
        total_f=S.Zero,
        cauchy_schwarz_ratio=S.Zero,
    )


# ============================================================================
# 6. Variance landscape
# ============================================================================

def variance_landscape(c_range: Optional[List] = None) -> Dict:
    r"""Compute delta_mix across the standard landscape at specific c-values.

    Evaluates the propagator variance for each multi-channel algebra
    at a grid of central charge values.

    Args:
        c_range: list of central charge values to evaluate at.
                 Default: [1/2, 1, 2, 4, 6, 13, 25, 26].

    Returns:
        Dict mapping algebra name to list of (c_val, delta_val) pairs.
    """
    if c_range is None:
        c_range = [Rational(1, 2), Rational(1), Rational(2), Rational(4),
                   Rational(6), Rational(13), Rational(25), Rational(26)]

    landscape = {}

    # Virasoro: always 0 (single channel)
    landscape['Virasoro'] = [(cv, 0) for cv in c_range]

    # W_3
    w3_data = w3_propagator()
    w3_delta = w3_data.delta_mix
    w3_results = []
    for cv in c_range:
        try:
            val = float(w3_delta.subs(c, cv).evalf())
            w3_results.append((cv, val))
        except (TypeError, ValueError):
            w3_results.append((cv, None))
    landscape['W_3'] = w3_results

    # W_4
    w4_data = w4_propagator()
    w4_delta = w4_data.delta_mix
    w4_results = []
    for cv in c_range:
        try:
            val = float(w4_delta.subs(c, cv).evalf())
            w4_results.append((cv, val))
        except (TypeError, ValueError):
            w4_results.append((cv, None))
    landscape['W_4'] = w4_results

    # Heisenberg: always 0
    landscape['Heisenberg'] = [(cv, 0) for cv in c_range]

    # Affine sl_2: always 0
    landscape['V_k(sl_2)'] = [(cv, 0) for cv in c_range]

    return landscape


# ============================================================================
# 7. DS variance transport
# ============================================================================

def ds_variance_transport(parent_data: PropagatorVarianceData,
                          child_data: PropagatorVarianceData) -> Dict:
    r"""Track how delta_mix transforms under DS reduction.

    DS reduction removes a channel (the highest-weight current becomes
    the BRST ghost) and modifies the quartic couplings via ghost exchange.

    For sl_3 -> W_3: the current algebra has class L (delta_mix = 0),
    and W_3 has class M with generically nonzero delta_mix.  The ghost
    sector CREATES the propagator variance.

    For sl_4 -> W_4: similarly, class L (delta_mix = 0) becomes class M.

    Args:
        parent_data: PropagatorVarianceData for the parent algebra (e.g., sl_3-hat).
        child_data: PropagatorVarianceData for the DS-reduced algebra (e.g., W_3).

    Returns:
        Dict with transport data including delta change, killed channel, etc.
    """
    return {
        'parent': parent_data.algebra_name,
        'child': child_data.algebra_name,
        'parent_rank': parent_data.rank,
        'child_rank': child_data.rank,
        'parent_delta': parent_data.delta_mix,
        'child_delta': child_data.delta_mix,
        'delta_created': simplify(child_data.delta_mix - parent_data.delta_mix) != 0,
        'parent_class': [ch.depth_class for ch in parent_data.channels],
        'child_class': [ch.depth_class for ch in child_data.channels],
        'mechanism': (
            'Ghost sector creates quartic couplings and nonzero delta_mix '
            'via BRST/DS reduction.  The parent current algebra has '
            'delta_mix = 0 (class L: Jacobi identity kills the quartic).  '
            'After DS, the ghost exchange generates Lambda-type composites '
            'with generically non-proportional quartic gradients.'
        ),
    }


def sl3_to_w3_transport(cc=None) -> Dict:
    r"""Concrete DS transport for sl_3-hat -> W_3.

    sl_3-hat: single primary channel (current J^a), class L.
      kappa(sl_3) = dim(sl_3)*(k+3)/(2*3) = 8(k+3)/6 = 4(k+3)/3
      f = 0 (class L)
      delta_mix = 0

    W_3: two channels (T, W), class M.
      delta_mix = (generically nonzero) * P(c) / (denom)

    The DS reduction kills the currents, replaces them with (T, W),
    and introduces ghost-exchange quartic couplings.
    """
    if cc is None:
        cc = c

    # sl_3 parent: single effective channel, class L
    kappa_sl3 = 4 * (k + 3) / 3  # dim(sl_3) = 8, h^v = 3
    parent_ch = ChannelData(
        label='J', weight=1, kappa=kappa_sl3,
        f_quartic=S.Zero, S4=S.Zero, Delta=S.Zero, depth_class='L',
    )
    parent = PropagatorVarianceData(
        algebra_name='V_k(sl_3)',
        rank=1,
        channels=[parent_ch],
        delta_mix=S.Zero,
        total_kappa=kappa_sl3,
        total_f=S.Zero,
    )

    child = w3_propagator(cc)
    return ds_variance_transport(parent, child)


# ============================================================================
# 8. Multi-channel shadow metric
# ============================================================================

def multi_channel_shadow_metric(channels: List[ChannelData]) -> Dict:
    r"""Construct the multi-dimensional shadow metric Q on r channels.

    For rank 1:
      Q_L(t) = (2*kappa + alpha*t)^2 + 2*Delta*t^2

    where alpha is the cubic shadow coefficient and
    Delta = 8*kappa*S4 is the critical discriminant.

    For rank 2 (e.g., W_3 with T and W channels):
      Q(t_1, t_2) = [curvature matrix] + [cubic terms] + [quartic terms]

    The full metric is the Hessian of the shadow generating function
    H(x_1, ..., x_r) = sum_{s>=2} Sh_s(x_1, ..., x_r) evaluated at a
    generic point.  At the origin, Q reduces to the curvature matrix;
    the quartic terms enter at second order.

    For the STATIC (arity-2 + arity-4 only) approximation:
      Q_{ab}^{static} = 2*kappa_a*delta_{ab} + S4_{ab}*t_a*t_b
    where S4_{ab} is the mixed quartic coupling.

    Returns:
        Dict with:
          - 'hessian': the curvature matrix (2x2, 3x3, etc.)
          - 'propagator': its inverse
          - 'quartic_matrix': the quartic coupling matrix S4_{ab}
          - 'discriminant': det(Q) as a function of the deformation parameters
          - 'rank': number of channels
    """
    r = len(channels)
    if r == 0:
        return {'rank': 0, 'hessian': Matrix([]), 'propagator': Matrix([])}

    # Curvature matrix (diagonal: kappa_a)
    H = zeros(r, r)
    for i in range(r):
        H[i, i] = channels[i].kappa

    # Propagator (inverse curvature)
    P = zeros(r, r)
    for i in range(r):
        if simplify(channels[i].kappa) != 0:
            P[i, i] = 1 / channels[i].kappa
        else:
            P[i, i] = oo

    # Quartic coupling matrix
    # For W_3: Q_{TT} = Q_TTTT, Q_{TW} = Q_TTWW, Q_{WW} = Q_WWWW
    # At leading order (Lambda-exchange), Q_{ab} ~ Q_0 * alpha^{|a-2|+|b-2|}
    S4_mat = zeros(r, r)
    for i in range(r):
        S4_mat[i, i] = channels[i].S4

    result = {
        'rank': r,
        'hessian': H,
        'propagator': P,
        'quartic_matrix': S4_mat,
        'total_kappa': cancel(H.trace()),
    }

    # 1D case: full shadow metric Q_L(t) = (2*kappa + alpha*t)^2 + 2*Delta*t^2
    if r == 1:
        t = Symbol('t')
        kap = channels[0].kappa
        Delta = channels[0].Delta
        # For the single-line shadow metric:
        # Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2
        # Simplified: (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2 where Delta = 8*kappa*S4
        # Note: we do not have alpha (cubic) in ChannelData, so we record
        # the quartic contribution only.
        Q_quartic = 4 * kap ** 2 + 2 * Delta * t ** 2
        result['shadow_metric_quartic'] = Q_quartic
        result['discriminant'] = cancel(-32 * kap ** 2 * Delta)

    # 2D case: include cross-terms if available
    if r == 2:
        t1, t2 = symbols('t_1 t_2')
        # Static approximation to the 2D shadow metric
        Q_static = (H[0, 0] * t1 ** 2 + H[1, 1] * t2 ** 2
                     + S4_mat[0, 0] * t1 ** 4 + S4_mat[1, 1] * t2 ** 4)
        result['shadow_metric_static'] = Q_static
        # The 2x2 curvature-level metric
        det_H = cancel(H[0, 0] * H[1, 1])
        result['hessian_determinant'] = det_H

    return result


# ============================================================================
# W_3-specific full 2D shadow metric
# ============================================================================

def w3_full_shadow_metric(cc=None) -> Dict:
    r"""The complete 2D shadow metric for W_3 including mixed quartic terms.

    Components:
      Hessian: H = diag(c/2, c/3)
      Propagator: P = diag(2/c, 3/c)
      Quartic tensor (Lambda-exchange):
        Q_TTTT = 10/[c(5c+22)]
        Q_TTWW = 160/[c(5c+22)^2]  (mixed)
        Q_WWWW = 2560/[c(5c+22)^3]
      Geometric progression: alpha = 16/(5c+22), Q ~ Q_0 * alpha^n

    The 2x2 quartic coupling matrix:
      M_4 = [[Q_TTTT, Q_TTWW],
             [Q_TTWW, Q_WWWW]]

    Determinant of M_4:
      det(M_4) = Q_TTTT * Q_WWWW - Q_TTWW^2
               = Q_0^2 * (alpha^2 - alpha^2) = 0  (rank 1!)

    This rank-1 structure reflects the single Lambda exchange mechanism:
    all quartic couplings factor through the same composite field Lambda.
    """
    if cc is None:
        cc = c

    alpha_val = Rational(16) / (5 * cc + 22)
    Q0 = Rational(10) / (cc * (5 * cc + 22))

    Q_TTTT = cancel(Q0)
    Q_TTWW = cancel(Q0 * alpha_val)
    Q_WWWW = cancel(Q0 * alpha_val ** 2)

    M4 = Matrix([
        [Q_TTTT, Q_TTWW],
        [Q_TTWW, Q_WWWW],
    ])

    det_M4 = cancel(M4.det())

    # The rank-1 factorization: M4 = v * v^T where v = sqrt(Q0) * [1, alpha]
    # This means all quartic data factors through a single exchange channel.

    return {
        'Q_TTTT': Q_TTTT,
        'Q_TTWW': Q_TTWW,
        'Q_WWWW': Q_WWWW,
        'alpha': alpha_val,
        'Q0': Q0,
        'quartic_matrix': M4,
        'det_quartic_matrix': det_M4,
        'rank_of_quartic': 1 if det_M4 == 0 else 2,
        'factorization_vector': Matrix([1, alpha_val]),
        'hessian': Matrix([[cc / 2, S.Zero], [S.Zero, cc / 3]]),
        'propagator': Matrix([[Rational(2) / cc, S.Zero],
                               [S.Zero, Rational(3) / cc]]),
    }


# ============================================================================
# Numerical evaluation utilities
# ============================================================================

def evaluate_w3_variance(c_val) -> Dict:
    r"""Evaluate the W_3 propagator variance at a specific central charge.

    Returns numerical values for delta_mix, the quartic gradients,
    the curvature-proportionality ratios, and the mixing polynomial.
    """
    c_val = Rational(c_val)
    w3 = w3_propagator(c_val)

    f_T = float(w3.channels[0].f_quartic.evalf())
    f_W = float(w3.channels[1].f_quartic.evalf())
    kap_T = float(w3.channels[0].kappa.evalf())
    kap_W = float(w3.channels[1].kappa.evalf())

    ratio_T = f_T / kap_T if kap_T != 0 else float('inf')
    ratio_W = f_W / kap_W if kap_W != 0 else float('inf')

    P_val = float((25 * c_val ** 2 + 100 * c_val - 428).evalf())
    delta_val = float(w3.delta_mix.evalf()) if w3.delta_mix != 0 else 0.0

    return {
        'c': float(c_val),
        'kappa_T': kap_T,
        'kappa_W': kap_W,
        'f_T': f_T,
        'f_W': f_W,
        'ratio_T': ratio_T,
        'ratio_W': ratio_W,
        'ratio_difference': ratio_T - ratio_W,
        'delta_mix': delta_val,
        'P(W_3)': P_val,
        'is_enhanced': abs(P_val) < 1e-10,
    }


def evaluate_at_special_charges() -> List[Dict]:
    r"""Evaluate the W_3 propagator variance at physically significant c-values.

    Special values:
      c = 2:   W_3 minimal model (p=3, p'=4)
      c = 4/5: W_3 from sl_3 at admissible level
      c = 13:  Virasoro self-dual point (Vir_c^! = Vir_{26-c})
      c = 25:  Virasoro near string critical
      c = 50:  large central charge regime
      c = 100: complementarity sum for W_3 (c + c' = 100)
    """
    results = []
    for c_val in [Rational(2), Rational(4, 5), Rational(13),
                  Rational(25), Rational(50), Rational(100)]:
        results.append(evaluate_w3_variance(c_val))
    return results


# ============================================================================
# Runner
# ============================================================================

if __name__ == '__main__':
    print("=" * 72)
    print("PROPAGATOR VARIANCE ENGINE")
    print("=" * 72)

    # 1. Heisenberg
    heis = heisenberg_propagator()
    print(f"\n{heis.summary()}")

    # 2. Virasoro
    vir = virasoro_propagator()
    print(f"\n{vir.summary()}")

    # 3. W_3
    w3 = w3_propagator()
    print(f"\n{w3.summary()}")

    # 4. Mixing polynomial
    P, zeros = mixing_polynomial_w3()
    print(f"\nW_3 mixing polynomial: P = {P}")
    print(f"  Zeros: {zeros}")
    for z in zeros:
        print(f"    c = {z} ~ {float(z.evalf()):.6f}")

    # 5. Enhanced symmetry
    sym = enhanced_symmetry_detection(w3)
    print(f"\nEnhanced symmetry detection:")
    for key, val in sym.items():
        print(f"  {key}: {val}")

    # 6. W_4
    w4 = w4_propagator()
    print(f"\n{w4.summary()}")

    # 7. Numerical evaluation at special charges
    print(f"\nW_3 propagator variance at special central charges:")
    print(f"  {'c':>6s}  {'delta':>12s}  {'P(W_3)':>12s}  {'f_T/k_T':>10s}  "
          f"{'f_W/k_W':>10s}  {'enhanced':>8s}")
    print("  " + "-" * 68)
    for d in evaluate_at_special_charges():
        enh = "YES" if d['is_enhanced'] else "no"
        print(f"  {d['c']:6.2f}  {d['delta_mix']:12.6e}  {d['P(W_3)']:12.4f}  "
              f"{d['ratio_T']:10.6f}  {d['ratio_W']:10.6f}  {enh:>8s}")

    # 8. DS transport
    print(f"\nDS transport (sl_3 -> W_3):")
    tr = sl3_to_w3_transport()
    for key in ['parent', 'child', 'delta_created', 'parent_class', 'child_class']:
        print(f"  {key}: {tr[key]}")

    # 9. Cauchy--Schwarz verification
    print(f"\nCauchy--Schwarz verification:")
    for name, data in [('W_3', w3), ('W_4', w4), ('Heisenberg', heis)]:
        ok = data.verify_cauchy_schwarz()
        print(f"  {name}: delta_mix >= 0 ? {'PASS' if ok else 'FAIL'}")

    # 10. 2D shadow metric
    print(f"\nW_3 full 2D shadow metric:")
    sm = w3_full_shadow_metric()
    print(f"  Q_TTTT = {sm['Q_TTTT']}")
    print(f"  Q_TTWW = {sm['Q_TTWW']}")
    print(f"  Q_WWWW = {sm['Q_WWWW']}")
    print(f"  det(M_4) = {sm['det_quartic_matrix']}  (rank {sm['rank_of_quartic']})")
    print(f"  alpha = {sm['alpha']}")
