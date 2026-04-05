#!/usr/bin/env python3
r"""
critical_line_atlas.py -- Critical line atlas for the standard landscape.

THE PROGRAMME:

Each chirally Koszul algebra A has a constrained Epstein zeta function
epsilon^c_s(A) whose nontrivial zeros are organized on critical lines
Re(s) = sigma_j. The number and positions of these critical lines encode
the arithmetic complexity of the shadow tower.

LATTICE VOAs (V_Lambda, rank r, theta weight k = r/2):

The Epstein zeta factorizes via the Hecke decomposition of Theta_Lambda:

    Theta_Lambda = c_E * E_k + sum_{j=1}^{g_k} c_j * f_j

where g_k = dim S_k(SL_2(Z)) is the cusp form dimension. Critical lines:

  Line 1: Re(s) = 1/2         from zeta(s)
  Line 2: Re(s) = k - 1/2     from zeta(s - k + 1)
  Line 3,...,2+g_k: Re(s) = k/2  from L(s, f_j) (each cusp form)

Total: 2 + g_k critical lines (for k >= 4; fewer for low weight).
Depth: d(V_Lambda) = 3 + g_k.

SPECIAL CASES:
  - k < 4 (rank < 8): only 1 critical line at Re(s) = 1/2.
    E_k may not be a holomorphic modular form for SL(2,Z) when k < 4.
    For rank 2: theta in M_1(Gamma_0(N)), Epstein = Dedekind zeta.
    One critical line. Depth 2.
  - k = 4 (rank 8, E_8): 2 lines at 1/2 and 7/2. Depth 3.
  - k = 8 (rank 16): 2 lines at 1/2 and 15/2. dim S_8 = 0. Depth 3.
  - k = 12 (rank 24, Niemeier): 3 lines at 1/2, 23/2, 6. dim S_12 = 1. Depth 4.
  - k = 16 (rank 32): 3 lines at 1/2, 31/2, 8. dim S_16 = 1. Depth 4.
  - k = 24 (rank 48): 4 lines at 1/2, 47/2, 12, 12. dim S_24 = 2. Depth 5.

VIRASORO FAMILY:

At generic c: the Koszul-Epstein epsilon^KE(s) is the Epstein zeta of
the shadow metric Q_L, a binary quadratic form with discriminant
D = -320c^2/(5c+22). This has:
  - 1 critical line at Re(s) = 1/2 when h(D) = 1 (the form is alone
    in its genus, and the Epstein zeta = const * zeta_K(s))
  - Potentially more complex behavior when h(D) > 1

At self-dual c = 13: Vir_13 = Vir_{26-13}^!, so the self-dual
factorization theorem applies: epsilon factors into standard L-functions.

At c = 26: kappa = 13, kappa(Vir_0^!) = 0. The Koszul dual is c = 0
which is the uncurved case.

DAVENPORT-HEILBRONN CLASSIFICATION:

For the Virasoro shadow metric Q_L at central charge c, the discriminant
is D = -320c^2/(5c+22). For minimal models M(m, m+1) at
c = 1 - 6/(m(m+1)):
  - Compute D and the fundamental discriminant d_0
  - Compute class number h(d_0)
  - h(d_0) = 1: DH obstruction absent (Epstein = const * zeta_K)
  - h(d_0) > 1: DH mechanism potentially active

DEPTH-CRITICAL LINE FORMULA:

d(A) >= 1 + #{distinct critical lines}. The gap of 2 arises from
charged strata contributing to depth but not critical lines.

For lattice VOAs: d = 3 + g_k = 1 + (2 + g_k) => equality.
For betagamma: d = 4, critical lines = 1, gap = 2.
For Virasoro: d = infinity, d_arith finite, d_alg = infinity.

Manuscript references:
    thm:spectral-decomposition-principle (arithmetic_shadows.tex)
    thm:refined-shadow-spectral (arithmetic_shadows.tex)
    thm:depth-decomposition (arithmetic_shadows.tex)
    thm:self-dual-factorization (arithmetic_shadows.tex)
    def:koszul-epstein-function (arithmetic_shadows.tex)
    rem:davenport-heilbronn-koszul-epstein (arithmetic_shadows.tex)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple
import math


# =========================================================================
# 1. Cusp form dimensions (SL_2(Z))
# =========================================================================

def cusp_form_dim_sl2z(k: int) -> int:
    r"""Dimension of S_k(SL_2(Z)) for even integer weight k.

    Standard dimension formula:
      dim S_k = 0              for k < 12 or k odd
      dim S_k = 1              for k = 12
      dim S_k = floor(k/12) - 1  if k = 2 mod 12 and k >= 14
      dim S_k = floor(k/12)      otherwise (k >= 14)
    """
    if k < 2 or k % 2 != 0:
        return 0
    if k < 12:
        return 0
    if k == 12:
        return 1
    if k % 12 == 2:
        return k // 12 - 1
    return k // 12


def modular_form_dim_sl2z(k: int) -> int:
    r"""Dimension of M_k(SL_2(Z)) for even integer weight k >= 0.

    dim M_k = dim S_k + 1 for k >= 4 (Eisenstein series contributes 1).
    dim M_0 = 1 (constants), dim M_2 = 0.
    """
    if k < 0 or k % 2 != 0:
        return 0
    if k == 0:
        return 1
    if k == 2:
        return 0
    return cusp_form_dim_sl2z(k) + 1


# =========================================================================
# 2. Critical line computation for lattice VOAs
# =========================================================================

def lattice_critical_lines(rank: int,
                           unimodular: bool = True) -> List[Dict]:
    r"""Compute critical lines for even unimodular lattice VOA of given rank.

    For even unimodular lattice Lambda of rank r:
      Theta_Lambda in M_{r/2}(SL_2(Z))
      k = r/2 (the theta weight)

    Critical lines come from:
      (1) zeta(s):          Re(s) = 1/2
      (2) zeta(s - k + 1):  Re(s) = k - 1/2 = (r-1)/2
      (3...) L(s, f_j):     Re(s) = k/2 = r/4 (from GRH for Hecke eigenforms)

    Returns list of dicts with keys: position, source, arity.
    """
    if rank % 8 != 0 and unimodular:
        # Even unimodular lattices exist only in rank 0 mod 8
        # But we compute anyway for theoretical completeness
        pass

    k = rank // 2  # theta weight (integer for even rank)
    if rank % 2 != 0:
        # Half-integer weight: more delicate theory
        k_frac = Fraction(rank, 2)
        return _lattice_critical_lines_half_int(rank, k_frac)

    g_k = cusp_form_dim_sl2z(k)

    lines = []

    if k >= 4:
        # Full Eisenstein series E_k exists for SL_2(Z) when k >= 4
        # Line 1: from zeta(s)
        lines.append({
            'position': Fraction(1, 2),
            'source': 'zeta(s)',
            'arity': 2,
            'description': 'Riemann zeta critical line',
        })
        # Line 2: from zeta(s - k + 1), critical line at Re(s) = k - 1/2
        lines.append({
            'position': Fraction(2 * k - 1, 2),
            'source': f'zeta(s-{k-1})',
            'arity': 3,
            'description': f'Eisenstein product line (from sigma_{{{k-1}}})',
        })
        # Lines from cusp forms
        for j in range(1, g_k + 1):
            lines.append({
                'position': Fraction(k, 2),
                'source': f'L(s, f_{j})',
                'arity': 3 + j,
                'description': f'Hecke eigenform #{j} of weight {k}',
            })
    elif k == 2:
        # M_2(SL_2(Z)) = 0, but M_1(Gamma_0(N)) for rank 2 lattices
        # gives Dedekind zeta with a single critical line
        lines.append({
            'position': Fraction(1, 2),
            'source': 'zeta_K(s)',
            'arity': 2,
            'description': 'Dedekind zeta critical line (rank 2)',
        })
    elif k == 1:
        # Rank 2 with odd lattice, or rank 1
        lines.append({
            'position': Fraction(1, 2),
            'source': 'zeta(2s)',
            'arity': 2,
            'description': 'Riemann zeta critical line (rank 1)',
        })

    return lines


def _lattice_critical_lines_half_int(rank: int,
                                      k_frac: Fraction) -> List[Dict]:
    r"""Critical lines for odd-rank lattice (half-integer weight theta)."""
    # For rank 1: Theta_Z in M_{1/2}(Gamma_0(4)), no cusp forms.
    # Epstein = 2*zeta(2s), critical line at Re(s) = 1/4.
    if rank == 1:
        return [{
            'position': Fraction(1, 4),
            'source': 'zeta(2s)',
            'arity': 2,
            'description': 'Riemann zeta (doubled argument) for rank 1',
        }]
    # General odd rank: would need Gamma_0(D) theory
    return [{
        'position': Fraction(1, 2),
        'source': f'L-functions for M_{{{k_frac}}}',
        'arity': 2,
        'description': f'Half-integer weight {k_frac}',
    }]


def lattice_depth(rank: int) -> int:
    r"""Shadow depth of even unimodular lattice VOA of rank r.

    d(V_Lambda) = 3 + dim S_{r/2}(SL_2(Z)) for r >= 8.
    d = 2 for r <= 4 (class G).
    d = 3 for r = 8 (class L, E_8).
    """
    k = rank // 2
    if rank < 8:
        return 2
    g_k = cusp_form_dim_sl2z(k)
    return 3 + g_k


def lattice_critical_line_count(rank: int) -> int:
    r"""Number of distinct critical lines for lattice VOA of rank r.

    For even unimodular with rank >= 8:
      #{lines} = 2 + dim S_{r/2}
    For rank < 8: #{lines} = 1.
    """
    if rank < 8:
        return 1
    k = rank // 2
    g_k = cusp_form_dim_sl2z(k)
    # Note: cusp form lines all at Re(s) = k/2, which is distinct from
    # Re(s) = 1/2 and Re(s) = k - 1/2 when k >= 4.
    # But they all lie at the SAME position Re(s) = k/2.
    # So distinct positions: 1/2, k-1/2, and k/2 (if g_k >= 1).
    # These are 3 distinct values when k >= 4 and g_k >= 1.
    # When g_k = 0: 2 distinct positions.
    # When g_k >= 1: 3 distinct positions (even though there are g_k cusp
    # eigenforms, they all share the critical line Re(s) = k/2).
    #
    # IMPORTANT: The depth formula counts L-functions, not distinct lines.
    # d = 3 + g_k = 1 + (2 + g_k) where (2 + g_k) = # of L-functions.
    # But DISTINCT critical line POSITIONS: at most 3 (for k >= 12 with g_k >= 1).
    # The cusp form lines are all at the same position k/2.
    #
    # The manuscript says "critical lines" meaning L-function sources,
    # not distinct geometric positions. So:
    #   # critical lines = 2 + g_k for k >= 4
    #   Depth = 1 + # critical lines = 3 + g_k
    return 2 + g_k


def verify_depth_critical_line_formula(rank: int) -> Dict:
    r"""Verify d(V_Lambda) = 1 + #{critical lines} for lattice VOAs."""
    d = lattice_depth(rank)
    n_lines = lattice_critical_line_count(rank)
    lines = lattice_critical_lines(rank)
    return {
        'rank': rank,
        'depth': d,
        'critical_line_count': n_lines,
        'formula_holds': d == 1 + n_lines,
        'gap': d - 1 - n_lines,
        'lines': lines,
    }


# =========================================================================
# 3. Critical line spacing for lattice VOAs
# =========================================================================

def lattice_line_spacing(rank: int) -> Dict:
    r"""Compute spacing between critical lines for lattice VOA.

    Line 1: Re(s) = 1/2 (from zeta(s))
    Line 2: Re(s) = k - 1/2 (from zeta(s-k+1))
    Cusp lines: Re(s) = k/2 (from L(s, f_j))

    Spacing between lines 1 and 2: k - 1 = r/2 - 1.
    Cusp lines are at k/2, which is between 1/2 and k - 1/2 when k >= 4.
    """
    k = rank // 2
    if k < 4:
        return {
            'rank': rank,
            'theta_weight': k,
            'line1': Fraction(1, 2),
            'line2': None,
            'cusp_line': None,
            'spacing_1_2': None,
            'cusp_between': None,
        }

    line1 = Fraction(1, 2)
    line2 = Fraction(2 * k - 1, 2)
    cusp_line = Fraction(k, 2)
    g_k = cusp_form_dim_sl2z(k)

    spacing = line2 - line1  # = k - 1

    # Verify cusp line is between line1 and line2
    cusp_between = line1 < cusp_line < line2 if g_k > 0 else None

    return {
        'rank': rank,
        'theta_weight': k,
        'line1': line1,
        'line2': line2,
        'cusp_line': cusp_line if g_k > 0 else None,
        'spacing_1_2': spacing,
        'cusp_between': cusp_between,
        'cusp_form_dim': g_k,
    }


# =========================================================================
# 4. Specific lattice families
# =========================================================================

LATTICE_DATA = {
    'Z': {
        'rank': 1,
        'name': 'Z (integer lattice)',
        'theta_weight': Fraction(1, 2),
        'epstein_formula': '2*zeta(2s)',
        'depth': 2,
        'shadow_class': 'G',
        'critical_lines': [
            {'position': Fraction(1, 4), 'source': 'zeta(2s)'},
        ],
    },
    'Z2': {
        'rank': 2,
        'name': 'Z^2 (square lattice)',
        'theta_weight': 1,
        'epstein_formula': '4*zeta(s)*L(s, chi_{-4}) = 4*zeta_{Q(i)}(s)',
        'depth': 2,
        'shadow_class': 'G',
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'zeta_{Q(i)}(s)'},
        ],
    },
    'Z_i': {
        'rank': 2,
        'name': 'Z[i] (Gaussian integers)',
        'theta_weight': 1,
        'epstein_formula': '4*zeta_{Q(i)}(s)',
        'depth': 2,
        'shadow_class': 'G',
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'zeta_{Q(i)}(s)'},
        ],
    },
    'A2': {
        'rank': 2,
        'name': 'A_2 (hexagonal lattice)',
        'theta_weight': 1,
        'epstein_formula': '6*zeta_{Q(omega)}(s)',
        'depth': 2,
        'shadow_class': 'G',
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'zeta_{Q(omega)}(s)'},
        ],
    },
    'E8': {
        'rank': 8,
        'name': 'E_8 root lattice',
        'theta_weight': 4,
        'epstein_formula': '240 * 2^{-s} * zeta(s) * zeta(s-3)',
        'depth': 3,
        'shadow_class': 'L',
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'zeta(s)'},
            {'position': Fraction(7, 2), 'source': 'zeta(s-3)'},
        ],
    },
    'E8_squared': {
        'rank': 16,
        'name': 'E_8^2',
        'theta_weight': 8,
        'epstein_formula': 'zeta(s)*zeta(s-7) (Eisenstein only, S_8=0)',
        'depth': 3,
        'shadow_class': 'L',
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'zeta(s)'},
            {'position': Fraction(15, 2), 'source': 'zeta(s-7)'},
        ],
    },
    'Leech': {
        'rank': 24,
        'name': 'Leech lattice',
        'theta_weight': 12,
        'epstein_formula': 'C_E*zeta(s)*zeta(s-11) - (65520/691)*C_Delta*L(s, Delta_12)',
        'depth': 4,
        'shadow_class': 'C',
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'zeta(s)'},
            {'position': Fraction(23, 2), 'source': 'zeta(s-11)'},
            {'position': Fraction(6, 1), 'source': 'L(s, Delta_12)'},
        ],
    },
    'rank_48': {
        'rank': 48,
        'name': 'Rank 48 even unimodular',
        'theta_weight': 24,
        'epstein_formula': 'zeta(s)*zeta(s-23) + L(s,f_1) + L(s,f_2)',
        'depth': 5,
        'shadow_class': 'F_5',
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'zeta(s)'},
            {'position': Fraction(47, 2), 'source': 'zeta(s-23)'},
            {'position': Fraction(12, 1), 'source': 'L(s, f_1)'},
            {'position': Fraction(12, 1), 'source': 'L(s, f_2)'},
        ],
    },
}


def lattice_atlas() -> Dict[str, Dict]:
    r"""Complete critical line atlas for all standard lattice families."""
    return LATTICE_DATA


# =========================================================================
# 5. Affine Kac-Moody critical lines
# =========================================================================

def affine_km_critical_lines(lie_type: str = 'A',
                              rank: int = 1,
                              level: int = 1) -> Dict:
    r"""Critical lines for affine Kac-Moody VOA at level k.

    For sl_2 at level 1: the character is related to theta functions of Z^2.
    The partition function involves theta functions at level 2k.

    The affine KM VOA V_k(g) has shadow class L (affine, r_max = 3).
    Shadow depth d = 3. The arithmetic shadow depends on level:

    For sl_2 level 1: Z = theta_3^2/(2*eta^2), related to rank-2 lattice.
    One critical line at Re(s) = 1/2 from the underlying lattice theta.

    For general g at level k: d_arith depends on the Hecke decomposition
    of the characters, which lives in a space of modular forms for
    Gamma_0(N) with N depending on the level.
    """
    if lie_type == 'A' and rank == 1:
        # sl_2
        h_dual = 2
        dim_g = 3
        c = Fraction(3 * level, level + 2)
        kappa = c / 2

        if level == 1:
            # V_1(sl_2) ~ V_{A_1} (lattice VOA for A_1 root lattice)
            # Character: theta of A_1 lattice / eta(tau)
            # One critical line at Re(s) = 1/2
            return {
                'algebra': f'sl_2 level {level}',
                'central_charge': c,
                'kappa': kappa,
                'shadow_class': 'L',
                'shadow_depth': 3,
                'd_arith': 2,
                'd_alg': 0,
                'critical_lines': [
                    {'position': Fraction(1, 2), 'source': 'zeta_{Q(sqrt(-2))}(s)'},
                ],
                'note': 'Lattice-type: V_1(sl_2) = V_{A_1}',
            }
        else:
            return {
                'algebra': f'sl_2 level {level}',
                'central_charge': c,
                'kappa': kappa,
                'shadow_class': 'L',
                'shadow_depth': 3,
                'd_arith': 'depends on level',
                'd_alg': 0,
                'critical_lines': [
                    {'position': Fraction(1, 2), 'source': 'zeta(s) or L(s, chi)'},
                ],
                'note': f'Modular forms for Gamma_0({2 * (level + 2)})',
            }

    dim_g = rank * (rank + 2) if lie_type == 'A' else None
    h_dual = rank + 1 if lie_type == 'A' else None

    return {
        'algebra': f'{lie_type}_{rank} level {level}',
        'shadow_class': 'L',
        'shadow_depth': 3,
        'd_arith': 'depends on level and type',
        'd_alg': 0,
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'L-functions of character decomposition'},
        ],
    }


# =========================================================================
# 6. Virasoro critical lines
# =========================================================================

def virasoro_shadow_data(c) -> Dict:
    r"""Shadow data for Virasoro at central charge c.

    kappa = c/2, alpha = 2, S4 = 10/(c(5c+22)), Delta = 40/(5c+22).
    Binary form discriminant D = -320c^2/(5c+22).
    """
    if isinstance(c, Fraction):
        kappa = c / 2
        alpha = Fraction(2)
        S4 = Fraction(10) / (c * (5 * c + 22))
        Delta = Fraction(40) / (5 * c + 22)
        disc = Fraction(-320) * c ** 2 / (5 * c + 22)
    else:
        c_f = float(c)
        kappa = c_f / 2
        alpha = 2.0
        S4 = 10.0 / (c_f * (5 * c_f + 22))
        Delta = 40.0 / (5 * c_f + 22)
        disc = -320.0 * c_f ** 2 / (5 * c_f + 22)

    return {
        'c': c,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': Delta,
        'discriminant': disc,
    }


def virasoro_binary_form(c) -> Tuple:
    r"""Binary quadratic form Q(m,n) from Virasoro shadow metric at c.

    Q(m,n) = 4*kappa^2*m^2 + 12*kappa*alpha*m*n + (9*alpha^2 + 16*kappa*S4)*n^2

    Returns (a, b, c_coeff, disc) where Q = a*m^2 + b*m*n + c_coeff*n^2
    and disc = b^2 - 4*a*c_coeff.
    """
    data = virasoro_shadow_data(c)
    kappa = data['kappa']
    alpha = data['alpha']
    S4 = data['S4']

    a = 4 * kappa ** 2
    b = 12 * kappa * alpha
    c_coeff = 9 * alpha ** 2 + 16 * kappa * S4

    disc = b ** 2 - 4 * a * c_coeff

    return a, b, c_coeff, disc


def virasoro_critical_lines_generic(c) -> Dict:
    r"""Critical lines for Virasoro at generic central charge c.

    The Koszul-Epstein function is the Epstein zeta of the shadow metric Q_L,
    a binary quadratic form. For a binary form with discriminant D < 0:

    If h(D) = 1: epsilon_Q = const * zeta_K(s) = const * zeta(s) * L(s, chi_D)
    Both factors have all zeros on Re(s) = 1/2 (under GRH/Dirichlet theorem).
    -> 1 critical line at Re(s) = 1/2.

    If h(D) > 1: the Epstein zeta depends on the specific ideal class,
    and the Davenport-Heilbronn mechanism can produce zeros off Re(s) = 1/2.
    -> Still 1 EXPECTED critical line, but off-line zeros possible.

    The shadow depth is infinite (class M). The depth decomposition:
    d = 1 + d_arith + d_alg, with d_alg = infinity.
    """
    data = virasoro_shadow_data(c)
    disc = data['discriminant']

    if isinstance(c, Fraction):
        # Compute fundamental discriminant
        D_num = disc.numerator
        D_den = disc.denominator
        # D = -320*c^2/(5c+22) as exact fraction
    else:
        D_num = float(disc)

    return {
        'algebra': f'Vir_c (c={c})',
        'central_charge': c,
        'kappa': data['kappa'],
        'shadow_class': 'M',
        'shadow_depth': float('inf'),
        'd_arith': 1,  # Binary form -> 1 critical line position at Re(s)=1/2
        'd_alg': float('inf'),
        'discriminant': disc,
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'Epstein zeta of Q_L'},
        ],
        'note': 'Binary form: single geometric critical line position',
    }


def virasoro_self_dual_factorization() -> Dict:
    r"""Self-dual factorization at c = 13 (Vir_13 = Vir_{26-13}^!).

    At the Koszul self-dual point c = 13:
      kappa = 13/2
      kappa' = (26-13)/2 = 13/2 = kappa (self-dual)
      alpha = 2
      S4 = 10/(13*87) = 10/1131
      Delta = 40/87

    The shadow metric Q_L has discriminant:
      D = -320*(13)^2/(5*13+22) = -320*169/87 = -54080/87

    Self-dual factorization theorem (thm:self-dual-factorization):
    When A = A^!, the Verdier involution sigma on B(A) gives a functional
    equation. The constrained Epstein decomposes into standard L-functions.

    For Virasoro at c = 13: the partition function Z_{Vir_13} does NOT
    lie in a finite-dimensional space of modular forms for SL_2(Z)
    (it involves the Virasoro character chi_0, which is quasi-modular).
    The self-dual factorization operates at the level of the shadow metric
    Q_L, not the full partition function.

    The binary form Q_L at c = 13 has discriminant D = -54080/87.
    For the Epstein zeta of this specific form, self-duality provides
    the enhanced functional equation from the Koszul involution.

    Under GRH for the associated L-function: all zeros on Re(s) = 1/2.
    """
    c = Fraction(13)
    data = virasoro_shadow_data(c)
    a, b, c_coeff, disc = virasoro_binary_form(c)

    return {
        'algebra': 'Vir_13 (self-dual)',
        'central_charge': c,
        'kappa': data['kappa'],
        'kappa_dual': data['kappa'],  # self-dual
        'shadow_class': 'M',
        'alpha': data['alpha'],
        'S4': data['S4'],
        'Delta': data['Delta'],
        'form_coefficients': (a, b, c_coeff),
        'discriminant': disc,
        'self_dual': True,
        'factorization': 'epsilon^KE = sum c_j Gamma_j(s) L(s, f_j)',
        'critical_lines': [
            {'position': Fraction(1, 2),
             'source': 'standard L-functions (self-dual factorization)'},
        ],
        'theorem': 'thm:self-dual-factorization',
        'note': ('At self-dual point, Verdier involution gives enhanced '
                 'functional equation. Zeros on Re(s) = 1/2 under GRH.'),
    }


def virasoro_c26_analysis() -> Dict:
    r"""Analysis at c = 26 (anomaly cancellation point).

    At c = 26:
      kappa(Vir_26) = 13
      Koszul dual: Vir_0, with kappa(Vir_0) = 0
      kappa_eff = kappa(matter) + kappa(ghost) = 13 + (-13) = 0

    The Koszul-Epstein function:
      kappa = 13, alpha = 2, S4 = 10/(26*152) = 10/3952 = 5/1976
      Delta = 8*13*(5/1976) = 520/1976 = 65/247
      Q_L(t) = (26 + 6t)^2 + (130/247)*t^2
      disc(Q) = -320*676/152 = -216320/152 = -27040/19

    The form is well-defined and nondegenerate. One critical line at Re(s) = 1/2.

    The dual at c = 0:
      kappa(Vir_0) = 0 -> UNCURVED. Bar d^2 = 0 at the scalar level.
      The Koszul-Epstein is degenerate (kappa = 0 -> Q_L has no leading term).
      This is the depth-zero resonance shadow (rem:virasoro-resonance-model).

    Physical significance: at c = 26 (critical string), the effective
    anomaly kappa_eff = kappa(matter) + kappa(ghost) vanishes.
    But kappa(Vir_26) = 13 is nonzero: the shadow tower is infinite.
    The c = 26 algebra is NOT special from the shadow perspective;
    the cancellation is between matter + ghost, not within the Virasoro
    algebra itself.

    The scattering matrix poles: at c = 26, the complementarity sum
    kappa + kappa' = 13/2 + 13/2 = 13 (Virasoro: AP24, not zero).
    The scattering poles are at s = 0 and s = 1 (the Epstein pole).
    """
    c = Fraction(26)
    data = virasoro_shadow_data(c)
    a, b, c_coeff, disc = virasoro_binary_form(c)

    c_dual = Fraction(0)

    return {
        'algebra': 'Vir_26 (critical string)',
        'central_charge': c,
        'kappa': data['kappa'],
        'kappa_dual': Fraction(0),  # kappa(Vir_0)
        'complementarity_sum': data['kappa'] + Fraction(0),  # 13 (not 0, AP24)
        'kappa_eff': data['kappa'] + Fraction(-13),  # matter kappa + ghost kappa
        'alpha': data['alpha'],
        'S4': data['S4'],
        'Delta': data['Delta'],
        'form_coefficients': (a, b, c_coeff),
        'discriminant': disc,
        'shadow_class': 'M',
        'shadow_depth': float('inf'),
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'Epstein zeta of Q_L'},
        ],
        'dual_analysis': {
            'c_dual': c_dual,
            'kappa_dual': Fraction(0),
            'note': 'Vir_0 is uncurved: kappa = 0, bar d^2 = 0. '
                    'Koszul-Epstein degenerate (rank-1 form).',
            'depth_dual': 'infinity (d_alg = infinity, d_arith = 0)',
        },
        'scattering': {
            'pole_at_s_1': True,
            'residue': 'proportional to vol / sqrt(|disc|)',
            'note': 'Standard Epstein pole. No special cancellation at c=26.',
        },
        'physical': {
            'anomaly_cancellation': 'kappa_eff = 0 is matter+ghost, not intrinsic',
            'string_amplitudes': 'Virasoro shadow tower at c=26 is still infinite',
        },
    }


# =========================================================================
# 7. Davenport-Heilbronn classification for minimal models
# =========================================================================

def minimal_model_c(m: int) -> Fraction:
    r"""Central charge c = 1 - 6/(m(m+1)) for unitary minimal model M(m, m+1)."""
    return Fraction(1) - Fraction(6, m * (m + 1))


def _squarefree_part(n: int) -> int:
    r"""Squarefree part of |n|: remove all squared prime factors."""
    if n == 0:
        return 0
    n = abs(n)
    result = 1
    d = 2
    temp = n
    while d * d <= temp:
        count = 0
        while temp % d == 0:
            temp //= d
            count += 1
        if count % 2 == 1:
            result *= d
        d += 1
    if temp > 1:
        result *= temp
    return result


def _fundamental_discriminant(D_num: int, D_den: int = 1) -> Tuple[int, int, int]:
    r"""Compute the fundamental discriminant from a rational discriminant.

    For a binary quadratic form with discriminant D = D_num/D_den,
    the associated quadratic field is Q(sqrt(D)) = Q(sqrt(D_num * D_den)).
    (Since sqrt(D_num/D_den) = sqrt(D_num * D_den) / D_den, and D_den is rational.)

    The fundamental discriminant d_0 is the discriminant of the ring of
    integers of Q(sqrt(D_num * D_den)).

    Returns (d_0, conductor, squarefree_part).
    """
    product = D_num * D_den  # Negative for definite forms
    abs_prod = abs(product)
    if abs_prod == 0:
        return 0, 0, 0

    # Squarefree part: remove all squared prime factors
    sf = _squarefree_part(abs_prod)

    # The quadratic field is Q(sqrt(-sf)) for negative product
    # Fundamental discriminant:
    #   d_0 = -sf   if sf = 3 mod 4
    #   d_0 = -4*sf otherwise (sf = 1 or 2 mod 4)
    if sf % 4 == 3:
        d_0 = -sf
    else:
        d_0 = -4 * sf

    # Conductor: abs_prod = sf * f^2
    f_squared = abs_prod // sf
    f = math.isqrt(f_squared)

    return d_0, f, sf


def class_number(D: int) -> Optional[int]:
    r"""Class number h(D) of primitive positive definite binary quadratic forms
    of discriminant D < 0.

    A form ax^2 + bxy + cy^2 is primitive if gcd(a,b,c) = 1.
    Reduced forms satisfy 0 <= b <= a <= c, with b >= 0 if a = c.
    h(D) counts the number of SL_2(Z)-equivalence classes.

    Valid discriminants satisfy D < 0 and D = 0 or 1 mod 4.

    Uses direct enumeration of reduced forms. Practical for |D| up to ~10^6.
    Returns None for invalid discriminants or |D| > 10^6.
    """
    if D >= 0:
        return None
    if D % 4 not in (0, 1):
        return None
    abs_D = abs(D)
    if abs_D > 10**6:
        return None  # Too large for direct enumeration

    count = 0
    b_max = int(math.isqrt(abs_D // 3))

    for b in range(0, b_max + 1):
        rem = b * b + abs_D
        if rem % 4 != 0:
            continue
        four_ac = rem
        a_min = max(1, b) if b > 0 else 1
        a_max = math.isqrt(four_ac // 4)

        for a in range(a_min, a_max + 1):
            if four_ac % (4 * a) != 0:
                continue
            c_val = four_ac // (4 * a)
            if c_val < a:
                continue
            # Primitive check
            if math.gcd(math.gcd(a, b), c_val) != 1:
                continue
            # Count: boundary forms (b=0, b=a, a=c) count once,
            # interior forms count twice (for +b and -b).
            if b == 0 or b == a or a == c_val:
                count += 1
            else:
                count += 2

    return count


def virasoro_dh_discriminant(c) -> Tuple:
    r"""Compute discriminant data for Virasoro at central charge c.

    disc(Q) = -320*c^2/(5c+22)

    The Davenport-Heilbronn mechanism applies to the Epstein zeta of
    the binary quadratic form Q_L. The relevant class number is h(d_0)
    where d_0 is the fundamental discriminant of Q(sqrt(disc)).

    Returns (disc_fraction, fundamental_disc, class_number_value).
    """
    if isinstance(c, Fraction):
        disc = Fraction(-320) * c ** 2 / (5 * c + 22)
    else:
        c = Fraction(c).limit_denominator(10**6)
        disc = Fraction(-320) * c ** 2 / (5 * c + 22)

    D_num = disc.numerator
    D_den = disc.denominator

    d_0, conductor, sf = _fundamental_discriminant(D_num, D_den)

    h = class_number(d_0)

    return disc, d_0, h


def minimal_model_dh_classification(m_max: int = 20) -> List[Dict]:
    r"""Davenport-Heilbronn classification for unitary minimal models.

    For M(m, m+1) with m = 3, ..., m_max:
      c = 1 - 6/(m(m+1))
      Compute disc(Q_L), fundamental discriminant, class number.
      h = 1: DH obstruction absent.
      h > 1: DH mechanism potentially active (off-line zeros possible).
    """
    results = []
    for m in range(3, m_max + 1):
        c = minimal_model_c(m)
        disc, d_0, h = virasoro_dh_discriminant(c)

        dh_active = None
        if h is not None and h > 0:
            dh_active = h > 1
        # h = None means |d_0| too large for direct computation

        results.append({
            'm': m,
            'model': f'M({m},{m+1})',
            'c': c,
            'c_float': float(c),
            'discriminant': disc,
            'disc_float': float(disc),
            'fundamental_disc': d_0,
            'class_number': h,
            'dh_active': dh_active,
            'dh_status': ('absent' if h == 1
                          else f'ACTIVE (h={h})' if (h is not None and h > 1)
                          else 'unknown'),
        })

    return results


# =========================================================================
# 8. Betagamma critical lines
# =========================================================================

def betagamma_critical_lines() -> Dict:
    r"""Critical lines for the betagamma system.

    The betagamma system has:
      shadow_class = C (contact, r_max = 4)
      depth = 4
      d_arith = 1 (the partition function 1/eta^2 is quasi-modular)
      d_alg = 2

    The constrained Epstein via U(1) symmetry has 1 critical line.
    Depth - 1 - # critical lines = 4 - 1 - 1 = 2 (the gap from AP-invisible
    charged strata).

    Verified by thm:refined-shadow-spectral.
    """
    return {
        'algebra': 'betagamma',
        'central_charge': Fraction(2),
        'kappa': Fraction(1),
        'shadow_class': 'C',
        'shadow_depth': 4,
        'd_arith': 1,
        'd_alg': 2,
        'critical_line_count': 1,
        'critical_lines': [
            {'position': Fraction(1, 2), 'source': 'zeta(s) from 1/eta^2'},
        ],
        'gap': 2,
        'gap_origin': 'Weight-changing deformations at arities 3 and 4 '
                      'invisible to U(1) spectral decomposition',
    }


# =========================================================================
# 9. Full atlas
# =========================================================================

def full_critical_line_atlas() -> Dict[str, Any]:
    r"""Complete critical line atlas for the standard landscape.

    Returns a dictionary with entries for every standard family.
    """
    atlas = {}

    # Lattice families
    for name, data in LATTICE_DATA.items():
        atlas[f'lattice_{name}'] = data

    # Affine KM
    atlas['affine_sl2_k1'] = affine_km_critical_lines('A', 1, 1)

    # Virasoro generic
    for c_val in [Fraction(1, 2), Fraction(1), Fraction(13), Fraction(26)]:
        atlas[f'virasoro_c{c_val}'] = virasoro_critical_lines_generic(c_val)

    # Self-dual
    atlas['virasoro_self_dual'] = virasoro_self_dual_factorization()

    # c = 26
    atlas['virasoro_c26_full'] = virasoro_c26_analysis()

    # Betagamma
    atlas['betagamma'] = betagamma_critical_lines()

    return atlas


def depth_critical_line_verification() -> List[Dict]:
    r"""Verify the depth-critical line inequality for all families."""
    results = []

    # Lattice families
    for rank in [1, 2, 8, 16, 24, 32, 48, 72, 96]:
        v = verify_depth_critical_line_formula(rank)
        results.append(v)

    # Betagamma
    bg = betagamma_critical_lines()
    results.append({
        'rank': 'betagamma',
        'depth': bg['shadow_depth'],
        'critical_line_count': bg['critical_line_count'],
        'formula_holds': bg['shadow_depth'] == 1 + bg['critical_line_count'] + bg['gap'],
        'gap': bg['gap'],
    })

    return results


# =========================================================================
# 10. The rank table (depth vs rank for even unimodular lattices)
# =========================================================================

def rank_depth_table(max_rank: int = 120) -> List[Dict]:
    r"""Depth, critical line count, and cusp form dimension vs rank.

    For even unimodular lattices (rank divisible by 8).
    """
    rows = []
    for r in range(8, max_rank + 1, 8):
        k = r // 2
        g_k = cusp_form_dim_sl2z(k)
        d = 3 + g_k
        n_lines = 2 + g_k
        rows.append({
            'rank': r,
            'theta_weight': k,
            'dim_M_k': modular_form_dim_sl2z(k),
            'dim_S_k': g_k,
            'max_lines': n_lines,
            'max_depth': d,
        })
    return rows


# =========================================================================
# 11. Summary statistics
# =========================================================================

def atlas_summary() -> str:
    r"""Human-readable summary of the critical line atlas."""
    lines = []
    lines.append("=" * 72)
    lines.append("CRITICAL LINE ATLAS FOR THE STANDARD LANDSCAPE")
    lines.append("=" * 72)
    lines.append("")

    lines.append("LATTICE VOAs:")
    lines.append("-" * 60)
    for name, data in LATTICE_DATA.items():
        cl = data['critical_lines']
        positions = [str(cl_item['position']) for cl_item in cl]
        lines.append(f"  {data['name']:35s}  depth={data['depth']}  "
                      f"lines={len(cl)}  at Re(s)={', '.join(positions)}")

    lines.append("")
    lines.append("VIRASORO:")
    lines.append("-" * 60)
    sd = virasoro_self_dual_factorization()
    lines.append(f"  c = 13 (self-dual):   disc = {float(sd['discriminant']):.4f}  "
                  f"lines=1 at Re(s)=1/2 (standard L-functions)")
    c26 = virasoro_c26_analysis()
    lines.append(f"  c = 26 (critical):    kappa = {c26['kappa']}  "
                  f"kappa' = {c26['kappa_dual']}  kappa_eff = {c26['kappa_eff']}")
    lines.append(f"                        disc = {float(c26['discriminant']):.4f}  "
                  f"1 critical line at Re(s)=1/2")

    lines.append("")
    lines.append("BETAGAMMA:")
    lines.append("-" * 60)
    bg = betagamma_critical_lines()
    lines.append(f"  depth={bg['shadow_depth']}  lines={bg['critical_line_count']}  "
                  f"gap={bg['gap']}  (charged strata invisible to U(1))")

    lines.append("")
    lines.append("DEPTH-CRITICAL LINE FORMULA:")
    lines.append("-" * 60)
    lines.append("  d(A) >= 1 + #{critical lines}")
    lines.append("  Equality: lattice VOAs")
    lines.append("  Gap of 2: betagamma (charged strata)")

    lines.append("")
    lines.append("RANK-DEPTH TABLE (even unimodular lattices):")
    lines.append("-" * 60)
    lines.append(f"  {'Rank':>6s}  {'k':>4s}  {'dim M_k':>7s}  {'dim S_k':>7s}  "
                  f"{'Lines':>5s}  {'Depth':>5s}")
    for row in rank_depth_table(96):
        lines.append(f"  {row['rank']:>6d}  {row['theta_weight']:>4d}  "
                      f"{row['dim_M_k']:>7d}  {row['dim_S_k']:>7d}  "
                      f"{row['max_lines']:>5d}  {row['max_depth']:>5d}")

    lines.append("")
    lines.append("DAVENPORT-HEILBRONN CLASSIFICATION (minimal models):")
    lines.append("-" * 60)
    dh = minimal_model_dh_classification(20)
    lines.append(f"  {'m':>3s}  {'c':>10s}  {'disc':>12s}  {'d_0':>8s}  "
                  f"{'h':>4s}  {'DH status':>12s}")
    for row in dh:
        c_str = str(row['c'])
        if len(c_str) > 10:
            c_str = f"{float(row['c']):.6f}"
        h_str = str(row['class_number']) if row['class_number'] is not None else '?'
        lines.append(f"  {row['m']:>3d}  {c_str:>10s}  "
                      f"{float(row['discriminant']):>12.4f}  "
                      f"{row['fundamental_disc']:>8d}  "
                      f"{h_str:>4s}  {row['dh_status']:>12s}")

    return '\n'.join(lines)


if __name__ == '__main__':
    print(atlas_summary())
