r"""Critical discriminant atlas: Delta = 8*kappa*S_4 for all standard families.

The critical discriminant Delta classifies shadow depth on each 1D primary
slice of the cyclic deformation complex:

    Delta = 0   <=>  Q_L(t) is a perfect square  <=>  tower terminates (G/L)
    Delta != 0  <=>  Q_L(t) is irreducible       <=>  tower infinite   (M)

The shadow metric on a primary line L is:

    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2

where kappa = modular characteristic, alpha = cubic shadow,
S_4 = quartic shadow, Delta = 8*kappa*S_4.

Discriminant complementarity (Virasoro family):

    Delta(Vir_c) + Delta(Vir_{26-c}) = 6960 / [(5c+22)(152-5c)]

with universal numerator 6960 = 2^4 * 3 * 5 * 29 = 40 * 174.

Manuscript references:
    eq:discriminant-complementarity (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, Optional, Tuple


# ============================================================================
# 1. Core formula: Delta = 8 * kappa * S_4
# ============================================================================

def critical_discriminant(kappa: Fraction, S4: Fraction) -> Fraction:
    """Critical discriminant Delta = 8*kappa*S_4.

    Parameters
    ----------
    kappa : modular characteristic (arity-2 curvature)
    S4 : quartic shadow coefficient on the primary line

    Returns
    -------
    Delta = 8*kappa*S_4
    """
    return Fraction(8) * kappa * S4


def shadow_metric_Q(kappa: Fraction, alpha: Fraction, S4: Fraction,
                    t: Fraction) -> Fraction:
    """Evaluate Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.

    Equivalently: Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t
                           + (9*alpha^2 + 16*kappa*S4)*t^2.
    """
    Delta = critical_discriminant(kappa, S4)
    return (2 * kappa + 3 * alpha * t) ** 2 + 2 * Delta * t ** 2


def shadow_metric_coefficients(kappa: Fraction, alpha: Fraction,
                               S4: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """Coefficients (q0, q1, q2) of Q_L(t) = q0 + q1*t + q2*t^2.

    q0 = 4*kappa^2
    q1 = 12*kappa*alpha
    q2 = 9*alpha^2 + 16*kappa*S4  =  9*alpha^2 + 2*Delta
    """
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4
    return q0, q1, q2


def shadow_metric_polynomial_discriminant(kappa: Fraction, alpha: Fraction,
                                          S4: Fraction) -> Fraction:
    """Polynomial discriminant of Q_L(t) as a quadratic in t.

    disc(Q_L) = q1^2 - 4*q0*q2 = -32*kappa^2 * Delta.

    Negative when Delta > 0 (complex branch points, class M generic).
    Zero when Delta = 0 (double root, class G/L).
    """
    Delta = critical_discriminant(kappa, S4)
    return Fraction(-32) * kappa ** 2 * Delta


# ============================================================================
# 2. Virasoro family: kappa = c/2, alpha = 2, S_4 = 10/[c(5c+22)]
# ============================================================================

def virasoro_kappa(c: Fraction) -> Fraction:
    """kappa(Vir_c) = c/2."""
    return Fraction(c, 2)


def virasoro_alpha() -> Fraction:
    """alpha(Vir) = 2 (cubic shadow coefficient, universal for Virasoro)."""
    return Fraction(2)


def virasoro_S4(c: Fraction) -> Fraction:
    """S_4(Vir_c) = Q^contact = 10/[c(5c+22)].

    Has poles at c = 0 and c = -22/5.
    """
    c = Fraction(c)
    return Fraction(10, 1) / (c * (5 * c + 22))


def virasoro_Delta(c: Fraction) -> Fraction:
    """Delta(Vir_c) = 8 * (c/2) * 10/[c(5c+22)] = 40/(5c+22).

    The c in the numerator of kappa cancels the c in the denominator of S_4.
    Result is independent of the sign of c.
    """
    c = Fraction(c)
    return Fraction(40, 5 * c + 22)


def virasoro_Delta_dual(c: Fraction) -> Fraction:
    """Delta(Vir_{26-c}) = 40/(5(26-c)+22) = 40/(152-5c).

    The Koszul dual Vir_c^! = Vir_{26-c}.
    """
    c = Fraction(c)
    return Fraction(40, 152 - 5 * c)


def virasoro_complementarity(c: Fraction) -> Dict[str, Fraction]:
    """Discriminant complementarity for the Virasoro family.

    Delta(c) + Delta(26-c) = 40/(5c+22) + 40/(152-5c)
                            = 40*[(152-5c) + (5c+22)] / [(5c+22)(152-5c)]
                            = 40*174 / [(5c+22)(152-5c)]
                            = 6960 / [(5c+22)(152-5c)].

    The numerator 6960 = 40 * 174 is a universal constant.
    """
    c = Fraction(c)
    Delta_A = virasoro_Delta(c)
    Delta_dual = virasoro_Delta_dual(c)
    total = Delta_A + Delta_dual

    # Predicted by the formula
    predicted = Fraction(6960) / ((5 * c + 22) * (152 - 5 * c))

    return {
        'c': c,
        'c_dual': Fraction(26) - c,
        'Delta_A': Delta_A,
        'Delta_dual': Delta_dual,
        'sum': total,
        'predicted': predicted,
        'match': total == predicted,
        'numerator': Fraction(6960),
        'denominator': (5 * c + 22) * (152 - 5 * c),
    }


def virasoro_shadow_metric_coefficients(c: Fraction
                                        ) -> Tuple[Fraction, Fraction, Fraction]:
    """Coefficients (q0, q1, q2) of Q_Vir(t) for Virasoro at central charge c.

    q0 = c^2
    q1 = 12c
    q2 = (180c + 872)/(5c + 22)
    """
    c = Fraction(c)
    kappa = virasoro_kappa(c)
    alpha = virasoro_alpha()
    S4 = virasoro_S4(c)
    return shadow_metric_coefficients(kappa, alpha, S4)


# ============================================================================
# 3. W_3 family: two primary lines (T-line and W-line)
# ============================================================================

def w3_T_line_data(c: Fraction) -> Dict[str, Fraction]:
    """Shadow data for W_3 on the T-line (x_W = 0).

    The T-line is the Virasoro subsector: identical to Virasoro.
    kappa_T = c/2, alpha_T = 2, S4_T = 10/[c(5c+22)].
    """
    c = Fraction(c)
    kappa = Fraction(c, 2)
    alpha = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))
    Delta = critical_discriminant(kappa, S4)
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4,
        'Delta': Delta, 'class': 'M',
    }


def w3_W_line_data(c: Fraction) -> Dict[str, Fraction]:
    """Shadow data for W_3 on the W-line (x_T = 0).

    kappa_W = c/3, alpha_W = 0 (Z_2 parity: W -> -W forces odd vanishing),
    S4_W = 2560/[c(5c+22)^3].

    The Z_2 parity of W forces all odd-arity shadows to vanish on this line.
    The even-arity cascade is driven by S4_W alone (no cubic seed).

    Delta_W = 8*(c/3)*2560/[c(5c+22)^3] = 20480/[3(5c+22)^3].
    """
    c = Fraction(c)
    kappa = Fraction(c, 3)
    alpha = Fraction(0)
    S4 = Fraction(2560) / (c * (5 * c + 22) ** 3)
    Delta = critical_discriminant(kappa, S4)
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4,
        'Delta': Delta, 'class': 'M',
    }


def w3_total_kappa(c: Fraction) -> Fraction:
    """Total kappa(W_3) = kappa_T + kappa_W = c/2 + c/3 = 5c/6."""
    c = Fraction(c)
    return Fraction(5) * c / 6


# ============================================================================
# 4. Affine Kac-Moody: S_4 = 0 (class L)
# ============================================================================

def affine_sl2_data(k: Fraction) -> Dict[str, Fraction]:
    """Shadow data for affine sl_2 at level k.

    kappa = 3(k+2)/4, alpha = nonzero (Lie bracket cubic), S_4 = 0.
    Delta = 0 (class L): Jacobi identity kills the quartic.
    """
    k = Fraction(k)
    kappa = Fraction(3) * (k + 2) / 4
    alpha = Fraction(1)  # normalized cubic shadow
    S4 = Fraction(0)
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4,
        'Delta': Fraction(0), 'class': 'L',
    }


def affine_slN_data(N: int, k: Fraction) -> Dict[str, Fraction]:
    """Shadow data for affine sl_N at level k.

    kappa = (N^2-1)(k+N)/(2N), alpha = nonzero (Killing 3-cocycle), S_4 = 0.
    Delta = 0 (class L) for all Kac-Moody algebras.
    """
    k = Fraction(k)
    dim_g = N ** 2 - 1
    h_dual = N
    kappa = Fraction(dim_g * (k + h_dual), 2 * h_dual)
    return {
        'kappa': kappa, 'alpha': Fraction(1), 'S4': Fraction(0),
        'Delta': Fraction(0), 'class': 'L',
    }


# ============================================================================
# 5. Heisenberg: S_4 = 0, alpha = 0 (class G)
# ============================================================================

def heisenberg_data(n: int) -> Dict[str, Fraction]:
    """Shadow data for Heisenberg of rank n.

    kappa = n/2, alpha = 0, S_4 = 0.
    Delta = 0 (class G): abelian OPE, no nonlinear shadows.
    """
    return {
        'kappa': Fraction(n, 2), 'alpha': Fraction(0), 'S4': Fraction(0),
        'Delta': Fraction(0), 'class': 'G',
    }


# ============================================================================
# 6. Beta-gamma system (class C)
# ============================================================================

def betagamma_kappa(lam: Fraction) -> Fraction:
    """kappa(betagamma, lambda) = 6*lambda^2 - 6*lambda + 1.

    Standard values: lambda=0 or 1 gives kappa=1, lambda=1/2 gives kappa=-1/2.
    Central charge: c = 2*kappa = 2(6*lambda^2 - 6*lambda + 1).
    """
    lam = Fraction(lam)
    return 6 * lam ** 2 - 6 * lam + 1


def betagamma_data(lam: Fraction) -> Dict[str, Any]:
    """Shadow data for the beta-gamma system at conformal weight lambda.

    On the weight-changing primary line:
        alpha = 0 (abelian on 1D weight-shift subspace)
        S_4 = 0 on this line (cor:nms-betagamma-mu-vanishing, rank-one rigidity)

    The quartic contact invariant lives on a CHARGED STRATUM of the full
    2D weight/contact deformation slice. It is nonzero there, giving class C.
    On the neutral primary line, Delta = 0.

    The system is class C because the OVERALL deformation complex has
    nontrivial quartic (depth 4), even though the single primary line
    has Delta = 0.
    """
    lam = Fraction(lam)
    kappa = betagamma_kappa(lam)
    return {
        'kappa': kappa,
        'alpha': Fraction(0),  # on weight-changing line
        'S4': Fraction(0),     # on weight-changing line
        'Delta': Fraction(0),  # on weight-changing line
        'class': 'C',
        'note': ('Delta = 0 on neutral primary line; '
                 'quartic contact nonzero on charged stratum'),
    }


def bc_kappa(j: Fraction) -> Fraction:
    """kappa(bc, j) = -(6j^2 - 6j + 1).

    The bc system has opposite kappa from betagamma.
    """
    j = Fraction(j)
    return -(6 * j ** 2 - 6 * j + 1)


def bc_data(j: Fraction) -> Dict[str, Any]:
    """Shadow data for bc system at spin j. Mirror of betagamma."""
    j = Fraction(j)
    kappa = bc_kappa(j)
    return {
        'kappa': kappa,
        'alpha': Fraction(0),
        'S4': Fraction(0),
        'Delta': Fraction(0),
        'class': 'C',
        'note': 'Mirror of betagamma; quartic contact on charged stratum',
    }


# ============================================================================
# 7. Complete discriminant atlas
# ============================================================================

def discriminant_atlas() -> Dict[str, Dict[str, Any]]:
    """Complete discriminant atlas for the standard landscape.

    For each family, reports kappa, alpha, S_4, Delta, shadow class,
    and whether Delta = 0 (finite tower) or Delta != 0 (infinite tower).

    Families with S_4 != 0 (class M):
        Virasoro, W_3 T-line, W_3 W-line, W_N (N >= 2)

    Families with S_4 = 0:
        Heisenberg (G), Lattice (G), Affine KM (L), betagamma/bc (C on stratum)
    """
    atlas = {}

    # Class G
    atlas['Heisenberg_1'] = heisenberg_data(1)
    atlas['Heisenberg_1']['description'] = 'rank 1 Heisenberg'

    # Class L
    atlas['Affine_sl2_k1'] = affine_sl2_data(1)
    atlas['Affine_sl2_k1']['description'] = 'sl_2 at level 1'

    atlas['Affine_sl3_k1'] = affine_slN_data(3, 1)
    atlas['Affine_sl3_k1']['description'] = 'sl_3 at level 1'

    # Class C
    atlas['BetaGamma_lam1'] = betagamma_data(1)
    atlas['BetaGamma_lam1']['description'] = 'betagamma at lambda = 1'

    atlas['bc_j1'] = bc_data(1)
    atlas['bc_j1']['description'] = 'bc at spin 1'

    # Class M: Virasoro at special c values
    for label, c_val in [('Vir_1', 1), ('Vir_2', 2), ('Vir_13', 13),
                         ('Vir_25', 25), ('Vir_26', 26)]:
        c_f = Fraction(c_val)
        atlas[label] = {
            'kappa': virasoro_kappa(c_f),
            'alpha': virasoro_alpha(),
            'S4': virasoro_S4(c_f),
            'Delta': virasoro_Delta(c_f),
            'class': 'M',
            'description': f'Virasoro at c = {c_val}',
        }

    # Class M: W_3 T-line
    for label, c_val in [('W3_T_c2', 2), ('W3_T_c13', 13)]:
        atlas[label] = w3_T_line_data(Fraction(c_val))
        atlas[label]['description'] = f'W_3 T-line at c = {c_val}'

    # Class M: W_3 W-line
    for label, c_val in [('W3_W_c2', 2), ('W3_W_c13', 13)]:
        atlas[label] = w3_W_line_data(Fraction(c_val))
        atlas[label]['description'] = f'W_3 W-line at c = {c_val}'

    return atlas


# ============================================================================
# 8. Complementarity verification
# ============================================================================

def verify_complementarity_virasoro(c_values: Optional[list] = None
                                    ) -> Dict[str, Dict[str, Any]]:
    """Verify Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)] for Virasoro.

    Tests the universal-numerator complementarity at each c value.
    """
    if c_values is None:
        c_values = [1, 2, 3, 5, 7, 10, 13, 20, 25]

    results = {}
    for cv in c_values:
        result = virasoro_complementarity(cv)
        results[f'c={cv}'] = result
    return results


def complementarity_at_self_dual() -> Dict[str, Any]:
    """Verify complementarity at the self-dual point c = 13.

    At c = 13: Vir_13^! = Vir_13, so Delta(A) = Delta(A!).
    Both equal 40/(5*13+22) = 40/87.
    Sum = 80/87 = 6960/(87*87) = 6960/7569.
    """
    c = Fraction(13)
    Delta_13 = virasoro_Delta(c)
    Delta_dual = virasoro_Delta_dual(c)

    return {
        'c': c,
        'Delta': Delta_13,
        'Delta_dual': Delta_dual,
        'self_dual': Delta_13 == Delta_dual,
        'sum': Delta_13 + Delta_dual,
        'predicted': Fraction(6960) / ((5 * c + 22) * (152 - 5 * c)),
        'match': (Delta_13 + Delta_dual ==
                  Fraction(6960) / ((5 * c + 22) * (152 - 5 * c))),
    }


def complementarity_c0_limit() -> Dict[str, Any]:
    """Analyze the c -> 0 limit of the discriminant.

    Delta(c) = 40/(5c+22): well-defined at c = 0, equals 40/22 = 20/11.
    kappa(c) = c/2 -> 0 at c = 0.
    S_4(c) = 10/[c(5c+22)] -> infinity at c = 0.

    The product Delta = 8*kappa*S_4 = 40/(5c+22) is well-defined
    because the c in kappa cancels the 1/c pole in S_4.

    The Koszul dual at c = 0 is Vir_{26}: Delta(26) = 40/(5*26+22) = 40/152 = 5/19.
    Sum: 20/11 + 5/19 = (20*19 + 5*11)/(11*19) = (380+55)/209 = 435/209.
    Predicted: 6960/(22*152) = 6960/3344 = 435/209. Match.
    """
    Delta_0 = virasoro_Delta(0)
    Delta_26 = virasoro_Delta(26)
    total = Delta_0 + Delta_26

    predicted = Fraction(6960) / (22 * 152)

    return {
        'Delta_c0': Delta_0,          # 40/22 = 20/11
        'Delta_c26': Delta_26,        # 40/152 = 5/19
        'sum': total,
        'predicted': predicted,
        'match': total == predicted,
        'note': ('Delta well-defined at c=0 because kappa*S4 = '
                 '(c/2)*10/[c(5c+22)] = 5/(5c+22) is regular'),
    }


# ============================================================================
# 9. W_3 discriminant analysis
# ============================================================================

def w3_discriminant_comparison(c: Fraction) -> Dict[str, Any]:
    """Compare T-line and W-line discriminants for W_3.

    T-line: Delta_T = 40/(5c+22)  (same as Virasoro)
    W-line: Delta_W = 20480/[3(5c+22)^3]

    Ratio: Delta_W / Delta_T = 512/[3(5c+22)^2].
    At c = 2: ratio = 512/(3*32^2) = 512/3072 = 1/6.
    At c = 13: ratio = 512/(3*87^2) = 512/22707 ~ 0.0225.
    """
    c = Fraction(c)
    T_data = w3_T_line_data(c)
    W_data = w3_W_line_data(c)

    ratio = W_data['Delta'] / T_data['Delta'] if T_data['Delta'] != 0 else None

    return {
        'c': c,
        'Delta_T': T_data['Delta'],
        'Delta_W': W_data['Delta'],
        'ratio': ratio,
        'S4_T': T_data['S4'],
        'S4_W': W_data['S4'],
        'kappa_T': T_data['kappa'],
        'kappa_W': W_data['kappa'],
    }


def w3_W_line_Delta_formula(c: Fraction) -> Fraction:
    """Closed-form Delta_W = 20480/[3(5c+22)^3].

    Derivation:
        Delta_W = 8 * kappa_W * S4_W
                = 8 * (c/3) * 2560/[c(5c+22)^3]
                = 8 * 2560 / [3(5c+22)^3]
                = 20480 / [3(5c+22)^3].
    """
    c = Fraction(c)
    return Fraction(20480, 3 * (5 * c + 22) ** 3)


# ============================================================================
# 10. Shadow class determination from Delta
# ============================================================================

def classify_shadow_depth(kappa: Fraction, alpha: Fraction,
                          S4: Fraction) -> str:
    """Classify shadow depth from the single-line data.

    G: Delta = 0 AND alpha = 0  =>  r_max = 2 (no nonlinear shadows)
    L: Delta = 0 AND alpha != 0  =>  r_max = 3 (cubic terminates)
    M: Delta != 0 AND alpha != 0  =>  r_max = inf (all-arity cascade)
    Even cascade: Delta != 0 AND alpha = 0  =>  even arities only

    Note: class C (r_max = 4) escapes via stratum separation and is
    not detectable from single-line data alone.
    """
    Delta = critical_discriminant(kappa, S4)
    if Delta == 0:
        if alpha == 0:
            return 'G'
        else:
            return 'L'
    else:
        if alpha == 0:
            return 'even_cascade'
        else:
            return 'M'


# ============================================================================
# 11. Numerical evaluation helpers
# ============================================================================

def virasoro_Delta_float(c_val: float) -> float:
    """Numerical Delta(Vir_c)."""
    return 40.0 / (5.0 * c_val + 22.0)


def virasoro_complementarity_float(c_val: float) -> Dict[str, float]:
    """Numerical complementarity check."""
    Delta_A = virasoro_Delta_float(c_val)
    Delta_dual = virasoro_Delta_float(26.0 - c_val)
    total = Delta_A + Delta_dual
    predicted = 6960.0 / ((5.0 * c_val + 22.0) * (152.0 - 5.0 * c_val))
    return {
        'Delta_A': Delta_A,
        'Delta_dual': Delta_dual,
        'sum': total,
        'predicted': predicted,
        'relative_error': abs(total - predicted) / abs(predicted)
        if predicted != 0 else float('inf'),
    }


if __name__ == '__main__':
    print("=" * 70)
    print("CRITICAL DISCRIMINANT ATLAS")
    print("=" * 70)

    # Atlas summary
    atlas = discriminant_atlas()
    print(f"\n{'Family':<20s} {'kappa':>12s} {'S4':>16s} {'Delta':>16s} {'Class':>6s}")
    print("-" * 70)
    for name, data in atlas.items():
        kap_str = str(data['kappa'])[:12]
        s4_str = str(data['S4'])[:16]
        d_str = str(data['Delta'])[:16]
        print(f"{name:<20s} {kap_str:>12s} {s4_str:>16s} {d_str:>16s} {data['class']:>6s}")

    # Complementarity
    print("\nVirasoro discriminant complementarity:")
    print(f"  {'c':>4s}  {'Delta(c)':>14s}  {'Delta(26-c)':>14s}  {'Sum':>14s}  {'Match':>6s}")
    print("  " + "-" * 60)
    for cv in [0, 1, 2, 5, 13, 20, 25]:
        comp = virasoro_complementarity(cv)
        print(f"  {cv:>4d}  {str(comp['Delta_A']):>14s}  "
              f"{str(comp['Delta_dual']):>14s}  "
              f"{str(comp['sum']):>14s}  {'YES' if comp['match'] else 'NO':>6s}")

    # W_3 comparison
    print("\nW_3 T-line vs W-line discriminant:")
    for cv in [2, 13, 25]:
        comp = w3_discriminant_comparison(cv)
        print(f"  c={cv}: Delta_T={comp['Delta_T']}, Delta_W={comp['Delta_W']}, "
              f"ratio={comp['ratio']}")

    # Self-dual verification
    sd = complementarity_at_self_dual()
    print(f"\nSelf-dual (c=13): Delta = Delta' = {sd['Delta']}, "
          f"self_dual = {sd['self_dual']}, sum = {sd['sum']}")

    # c=0 limit
    lim = complementarity_c0_limit()
    print(f"\nc=0 limit: Delta(0) = {lim['Delta_c0']}, "
          f"Delta(26) = {lim['Delta_c26']}, sum = {lim['sum']}, "
          f"match = {lim['match']}")
