r"""Shadow planted-forest convergence diagnostics atlas.

MATHEMATICAL FRAMEWORK
======================

The certified analytic object in this module is the scalar Bernoulli/A-hat
genus series

    sum_{g>=1} F_g^{scalar}(A) hbar^{2g}
      = kappa(A) * ((hbar/2)/sin(hbar/2) - 1).

It has poles at hbar = 2*pi*n and scalar Taylor radius 2*pi.  This is a
theorem about the scalar lane, not a theorem about the full planted-forest
partition function of an interacting algebra.

The arity quantities below are finite-depth facts for terminating classes
and arity-radius diagnostics for class M.  The Virasoro and W-line rho values
use local shadow coefficients such as S_3, S_4, S_5 and the algebraic
radicand.  They do not certify all-genus Virasoro planted-forest corrections,
Borel summability, analytic continuation of the full shadow partition
function, nonperturbative completion, BTZ/JT recovery, or multiweight
all-genus partition data.

The comparison routines deliberately return certification metadata so tests
can prevent scalar Bernoulli facts or finite windows from being promoted to
global analytic theorems.

Manuscript references:
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    prop:genus-expansion-convergence (genus_expansions.tex)
    rem:convergence-vs-string (genus_expansions.tex)
    def:shadow-growth-rate (higher_genus_modular_koszul.tex)
    prop:virasoro-shadow-canonical (landscape_census.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from sympy import Rational, Symbol, solve

from compute.lib.utils import lambda_fp, F_g

# Constants
PI = math.pi
TWO_PI = 2 * PI
TWO_PI_SQ = TWO_PI ** 2

EXACT_SCALAR_AHAT = "exact_scalar_a_hat"
FINITE_DEPTH_EXACT = "finite_depth_exact"
SINGLE_LINE_DIAGNOSTIC = "single_line_diagnostic"
ARITY_RADIUS_DIAGNOSTIC = "arity_radius_diagnostic"
ASYMPTOTIC_ESTIMATE = "asymptotic_estimate"
ANALYTIC_HYPOTHESIS_REQUIRED = "analytic_hypothesis_required"
NOT_CERTIFIED = "not_certified"
VERDIER_DUAL_BRANCH = "A^! Verdier/continuous-linear dual branch"
BAR_COBAR_INVERSION_FIREWALL = "Omega(B(A))=A is bar-cobar inversion"
HOCHSCHILD_BULK_FIREWALL = "Z_ch^der(A) is Hochschild/bulk, not Koszul dual"


# ============================================================================
# 1. Kappa values for standard-family representatives
# ============================================================================

def kappa_heisenberg(rank: int = 1, level: float = 1.0) -> float:
    """kappa(H_level^{oplus rank}) = rank * level.

    Local source: chapters/examples/landscape_census.tex records
    kappa(H_l^{oplus d}) = d*l and the collision residue k/z.
    """
    return float(rank) * float(level)


def kappa_virasoro(c_val: float) -> float:
    """kappa(Vir_c) = c/2."""
    return c_val / 2.0


def kappa_affine_sl2(k_val: float) -> float:
    """kappa(sl_2, k) = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k+2)/4.

    dim(sl_2) = 3, h^v(sl_2) = 2.
    """
    return 3.0 * (k_val + 2.0) / 4.0


def kappa_affine_slN(N: int, k_val: float) -> float:
    """kappa(sl_N, k) = (N^2 - 1) * (k + N) / (2N).

    dim(sl_N) = N^2 - 1, h^v(sl_N) = N.
    """
    dim_g = N * N - 1
    h_dual = N
    return dim_g * (k_val + h_dual) / (2.0 * h_dual)


def kappa_affine_general(dim_g: int, k_val: float, h_dual: float) -> float:
    """kappa(g, k) = dim(g) * (k + h^v) / (2 * h^v)."""
    return dim_g * (k_val + h_dual) / (2.0 * h_dual)


def kappa_wN(N: int, c_val: float) -> float:
    """Total kappa for W_N at central charge c.

    kappa(W_N) = sum_{j=2}^{N} c/j = c * H_{N-1,shift}
    where H_{N-1,shift} = 1/2 + 1/3 + ... + 1/N.

    For N=2 (Virasoro): kappa = c/2.
    For N=3 (W_3): kappa = c/2 + c/3 = 5c/6.
    For N=4 (W_4): kappa = c/2 + c/3 + c/4 = 13c/12.
    """
    return c_val * sum(1.0 / j for j in range(2, N + 1))


# ============================================================================
# 2. Shadow radius diagnostics for standard-family representatives
# ============================================================================

def virasoro_rho_squared(c_val: float) -> float:
    r"""rho^2(Vir_c) = (180c + 872) / ((5c + 22) * c^2).

    From kappa = c/2, alpha = 2, S4 = 10/(c(5c+22)):
    9*alpha^2 + 2*Delta = 36 + 80/(5c+22) = (180c + 872)/(5c+22).
    """
    return (180.0 * c_val + 872.0) / ((5.0 * c_val + 22.0) * c_val ** 2)


def virasoro_rho(c_val: float) -> float:
    """Shadow growth rate rho(Vir_c)."""
    rho_sq = virasoro_rho_squared(c_val)
    if rho_sq < 0:
        return float('nan')
    return math.sqrt(rho_sq)


def w3_wline_rho_squared(c_val: float) -> float:
    r"""rho_W^2 for W_3 on the W-line.

    kappa_W = c/3, alpha_W = 0 (Z_2 parity), S4_W = 2560/[c(5c+22)^3].
    rho_W^2 = 30720 / (c^2 * (5c+22)^3).
    """
    return 30720.0 / (c_val ** 2 * (5.0 * c_val + 22.0) ** 3)


def w3_rho_effective(c_val: float) -> float:
    """Effective shadow radius for W_3 = max(rho_T, rho_W)."""
    rho_T = virasoro_rho(c_val)
    rho_W_sq = w3_wline_rho_squared(c_val)
    rho_W = math.sqrt(rho_W_sq) if rho_W_sq >= 0 else float('nan')
    return max(rho_T, rho_W)


def w4_wline_rho_squared(j: int, c_val: float) -> float:
    r"""rho^2 for the W_j-channel (j >= 3) of W_4.

    rho_j^2 = 40 * j * 16^{2(j-2)} / (c^2 * (5c+22)^{2j-3}).
    """
    if j == 2:
        return virasoro_rho_squared(c_val)
    power = 2 * (j - 2)
    exponent = 2 * j - 3
    return 40.0 * j * (16.0 ** power) / (c_val ** 2 * (5.0 * c_val + 22.0) ** exponent)


def wN_channel_rho(N: int, j: int, c_val: float) -> float:
    """Shadow radius for the W_j-channel of W_N.

    j = 2 (T-line): rho = Virasoro rho.
    j >= 3: rho_j = sqrt(40*j*16^{2(j-2)} / (c^2*(5c+22)^{2j-3})).
    """
    if j == 2:
        return virasoro_rho(c_val)
    rho_sq = 40.0 * j * (16.0 ** (2 * (j - 2))) / (c_val ** 2 * (5.0 * c_val + 22.0) ** (2 * j - 3))
    return math.sqrt(rho_sq) if rho_sq >= 0 else float('nan')


def wN_rho_effective(N: int, c_val: float) -> float:
    """Effective shadow radius for W_N = max over all channels."""
    return max(wN_channel_rho(N, j, c_val) for j in range(2, N + 1))


def critical_central_charge() -> float:
    r"""Critical central charge c* where rho(Vir_{c*}) = 1.

    Solves 5c^3 + 22c^2 - 180c - 872 = 0.
    Unique positive real root: c* ~ 6.1243.
    """
    c = Symbol('c')
    poly = 5 * c ** 3 + 22 * c ** 2 - 180 * c - 872
    roots = solve(poly, c)
    for r in roots:
        val = complex(r.evalf())
        if abs(val.imag) < 1e-10 and val.real > 0:
            return val.real
    return float('nan')


# ============================================================================
# 3. Scalar A-hat genus convergence radius
# ============================================================================

def genus_convergence_radius() -> float:
    r"""Scalar A-hat genus convergence radius R_genus = 2*pi.

    The generating function (hbar/2)/sin(hbar/2) has poles at
    hbar = 2*pi*n (n != 0).  Nearest pole at |hbar| = 2*pi.
    """
    return TWO_PI


def genus_series_closed_form(kappa_val: float, hbar: float) -> float:
    r"""Closed-form scalar genus series: kappa * ((hbar/2)/sin(hbar/2) - 1).

    Valid as the scalar Taylor sum for |hbar| < 2*pi.
    """
    if abs(hbar) < 1e-15:
        return 0.0
    return kappa_val * ((hbar / 2.0) / math.sin(hbar / 2.0) - 1.0)


def genus_series_partial_sum(kappa_val: float, max_genus: int,
                              hbar: float = 1.0) -> float:
    r"""Partial sum sum_{g=1}^{G} F_g * hbar^{2g}."""
    total = 0.0
    kv = Rational(kappa_val) if isinstance(kappa_val, (int, float)) else kappa_val
    for g in range(1, max_genus + 1):
        fg = float(F_g(kv, g))
        total += fg * hbar ** (2 * g)
    return total


# ============================================================================
# 4. Arity radius diagnostic (family-dependent)
# ============================================================================

def arity_convergence_radius(rho: float) -> float:
    """R_arity = 1/rho.  For rho = 0: R_arity = infinity."""
    if rho <= 0:
        return float('inf')
    return 1.0 / rho


# ============================================================================
# 5. Full shadow growth rate atlas
# ============================================================================

@dataclass
class FamilyConvergenceData:
    """Convergence and certification data for one algebra-family row."""
    name: str
    depth_class: str         # G, L, C, M
    shadow_depth: float      # 2, 3, 4, inf
    kappa: float
    rho: float               # shadow growth rate
    R_genus: float           # scalar A-hat Taylor radius = 2*pi
    R_arity: float           # arity diagnostic radius = 1/rho
    genus_convergent: bool   # scalar lane only
    arity_convergent: bool   # diagnostic True iff rho < 1
    double_convergent: bool  # scalar x arity diagnostic, not full PF
    F1: float                # genus-1 free energy = kappa/24
    genus_scope: str = EXACT_SCALAR_AHAT
    arity_scope: str = ARITY_RADIUS_DIAGNOSTIC
    double_convergence_scope: str = ANALYTIC_HYPOTHESIS_REQUIRED
    full_shadow_pf_certified: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)


def family_convergence(name: str, depth_class: str, shadow_depth: float,
                       kappa: float, rho: float,
                       **params) -> FamilyConvergenceData:
    """Construct convergence data for a single family row."""
    R_genus = TWO_PI
    R_arity = arity_convergence_radius(rho)
    genus_scope = params.pop('genus_scope', EXACT_SCALAR_AHAT)
    arity_scope = params.pop('arity_scope', None)
    double_scope = params.pop('double_convergence_scope', None)
    full_pf_certified = params.pop('full_shadow_pf_certified', None)

    if arity_scope is None:
        if depth_class in {'G', 'L'} and rho == 0.0:
            arity_scope = FINITE_DEPTH_EXACT
        elif depth_class == 'C':
            arity_scope = SINGLE_LINE_DIAGNOSTIC
        else:
            arity_scope = ARITY_RADIUS_DIAGNOSTIC

    if double_scope is None:
        if depth_class in {'G', 'L'} and rho == 0.0:
            double_scope = FINITE_DEPTH_EXACT
        else:
            double_scope = ANALYTIC_HYPOTHESIS_REQUIRED

    if full_pf_certified is None:
        full_pf_certified = depth_class in {'G', 'L'} and rho == 0.0

    return FamilyConvergenceData(
        name=name,
        depth_class=depth_class,
        shadow_depth=shadow_depth,
        kappa=kappa,
        rho=rho,
        R_genus=R_genus,
        R_arity=R_arity,
        genus_convergent=True,
        arity_convergent=(rho < 1.0),
        double_convergent=(rho < 1.0),
        F1=kappa / 24.0,
        genus_scope=genus_scope,
        arity_scope=arity_scope,
        double_convergence_scope=double_scope,
        full_shadow_pf_certified=full_pf_certified,
        parameters=params,
    )


def shadow_growth_rate_atlas() -> Dict[str, FamilyConvergenceData]:
    r"""Atlas of shadow growth rates for standard-family representatives.

    Returns a dictionary mapping family names to their FamilyConvergenceData.

    Covers all four depth classes:
      G (Gaussian, rho = 0): Heisenberg, lattice VOAs
      L (Lie/tree, rho = 0): all affine KM (A-D-E, BCFG)
      C (Contact, single-line diagnostic): beta-gamma
      M (Mixed, rho > 0): Virasoro, W_N diagnostics
    """
    atlas = {}

    # === CLASS G: Gaussian, depth 2 ===
    atlas['Heisenberg_rank1'] = family_convergence(
        'Heisenberg (rank 1)', 'G', 2, kappa_heisenberg(1), 0.0,
        rank=1)

    atlas['Heisenberg_rank8'] = family_convergence(
        'Heisenberg (rank 8)', 'G', 2, kappa_heisenberg(8), 0.0,
        rank=8)

    atlas['Heisenberg_rank24'] = family_convergence(
        'Heisenberg (rank 24)', 'G', 2, kappa_heisenberg(24), 0.0,
        rank=24)

    for rank, lattice_name in [(8, 'E_8'), (16, 'D_{16}^+'), (24, 'Leech')]:
        atlas[f'Lattice_{lattice_name}'] = family_convergence(
            f'Lattice V_{lattice_name}', 'G', 2, float(rank), 0.0,
            rank=rank, lattice=lattice_name)

    # === CLASS L: Lie/tree, depth 3 ===
    # sl_2
    for k in [1, 2, 10, 100]:
        kap = kappa_affine_sl2(k)
        atlas[f'sl2_k{k}'] = family_convergence(
            f'Affine sl_2 (k={k})', 'L', 3, kap, 0.0,
            lie_type='A1', k=k, dim_g=3, h_dual=2)

    # sl_3
    for k in [1, 2, 10]:
        kap = kappa_affine_slN(3, k)
        atlas[f'sl3_k{k}'] = family_convergence(
            f'Affine sl_3 (k={k})', 'L', 3, kap, 0.0,
            lie_type='A2', k=k, dim_g=8, h_dual=3)

    # Classical types: sl_N for N = 4, ..., 8 at k = 1
    for N in [4, 5, 6, 7, 8]:
        kap = kappa_affine_slN(N, 1)
        atlas[f'sl{N}_k1'] = family_convergence(
            f'Affine sl_{N} (k=1)', 'L', 3, kap, 0.0,
            lie_type=f'A{N-1}', k=1, dim_g=N*N-1, h_dual=N)

    # Exceptional types at k = 1
    exceptionals = [
        ('G2', 14, 4), ('F4', 52, 9), ('E6', 78, 12),
        ('E7', 133, 18), ('E8', 248, 30),
    ]
    for lie_type, dim_g, h_dual in exceptionals:
        kap = kappa_affine_general(dim_g, 1, h_dual)
        atlas[f'{lie_type}_k1'] = family_convergence(
            f'Affine {lie_type} (k=1)', 'L', 3, kap, 0.0,
            lie_type=lie_type, k=1, dim_g=dim_g, h_dual=h_dual)

    # Non-simply-laced at k = 1
    non_simply_laced = [
        ('B2', 10, 3), ('C2', 10, 2), ('B3', 21, 5),
        ('C3', 21, 4), ('B4', 36, 7), ('C4', 36, 6),
    ]
    for lie_type, dim_g, h_dual in non_simply_laced:
        kap = kappa_affine_general(dim_g, 1, h_dual)
        atlas[f'{lie_type}_k1'] = family_convergence(
            f'Affine {lie_type} (k=1)', 'L', 3, kap, 0.0,
            lie_type=lie_type, k=1, dim_g=dim_g, h_dual=h_dual)

    # === CLASS C: Contact, depth 4 ===
    # Beta-gamma: single-line rho = 0 (stratum separation)
    atlas['betagamma'] = family_convergence(
        'Beta-gamma (c=-2)', 'C', 4, -1.0, 0.0,
        c=-2, note='Single-line rho = 0; quartic on charged stratum')

    # === CLASS M: Mixed, depth infinity ===
    # Virasoro at many central charges
    c_star = critical_central_charge()
    vir_c_values = [
        ('1/2', 0.5), ('1', 1.0), ('2', 2.0), ('4', 4.0),
        ('6', 6.0), ('c*', c_star), ('7', 7.0), ('10', 10.0),
        ('13', 13.0), ('20', 20.0), ('25', 25.0), ('26', 26.0),
    ]
    for label, c_val in vir_c_values:
        rho = virasoro_rho(c_val)
        kap = kappa_virasoro(c_val)
        atlas[f'Vir_c={label}'] = family_convergence(
            f'Virasoro (c={label})', 'M', float('inf'), kap, rho,
            c=c_val, c_star=c_star, above_c_star=(c_val > c_star))

    # W_3 at selected central charges
    for label, c_val in [('50', 50.0), ('98', 98.0), ('2', 2.0)]:
        rho_eff = w3_rho_effective(c_val)
        kap = kappa_wN(3, c_val)
        atlas[f'W3_c={label}'] = family_convergence(
            f'W_3 (c={label})', 'M', float('inf'), kap, rho_eff,
            c=c_val, N=3, rho_T=virasoro_rho(c_val),
            rho_W=math.sqrt(w3_wline_rho_squared(c_val)))

    # W_4 at c = 100
    rho_eff_w4 = wN_rho_effective(4, 100.0)
    atlas['W4_c=100'] = family_convergence(
        'W_4 (c=100)', 'M', float('inf'), kappa_wN(4, 100.0), rho_eff_w4,
        c=100.0, N=4)

    return atlas


# ============================================================================
# 6. Scalar x arity diagnostic domain
# ============================================================================

@dataclass
class DoubleConvergenceDomain:
    """Diagnostic domain for scalar hbar and arity variable t."""
    R_genus: float
    R_arity: float
    rho: float
    kappa: float
    name: str = ''
    genus_scope: str = EXACT_SCALAR_AHAT
    arity_scope: str = ARITY_RADIUS_DIAGNOSTIC
    full_shadow_pf_certified: bool = False

    @property
    def is_convergent(self) -> bool:
        """Return the arity-radius diagnostic, not a full PF certificate."""
        return self.rho < 1.0

    @property
    def area(self) -> float:
        if self.R_arity == float('inf'):
            return float('inf')
        return PI * self.R_genus * self.R_arity


def double_convergence_domain(kappa_val: float, rho: float,
                               name: str = '') -> DoubleConvergenceDomain:
    """Construct the scalar x arity diagnostic domain."""
    return DoubleConvergenceDomain(
        R_genus=TWO_PI,
        R_arity=arity_convergence_radius(rho),
        rho=rho,
        kappa=kappa_val,
        name=name,
    )


def double_convergence_domains_table() -> List[Dict[str, Any]]:
    r"""Scalar x arity diagnostic domains for selected algebras.

    Virasoro at c = 1/2, 1, 6, 13, 25, 26.
    W_3 at c = 50.
    sl_2 at k = 1, 2, 10, 100.
    """
    table = []

    for label, c_val in [('Vir c=1/2', 0.5), ('Vir c=1', 1.0),
                          ('Vir c=6', 6.0), ('Vir c=13', 13.0),
                          ('Vir c=25', 25.0), ('Vir c=26', 26.0)]:
        rho = virasoro_rho(c_val)
        kap = kappa_virasoro(c_val)
        table.append({
            'name': label, 'kappa': kap, 'rho': rho,
            'R_genus': TWO_PI, 'R_arity': arity_convergence_radius(rho),
            'double_convergent': rho < 1.0,
            'genus_scope': EXACT_SCALAR_AHAT,
            'arity_scope': ARITY_RADIUS_DIAGNOSTIC,
            'full_shadow_pf_certified': False,
        })

    # W_3 at c = 50
    rho_eff = w3_rho_effective(50.0)
    table.append({
        'name': 'W_3 c=50', 'kappa': kappa_wN(3, 50.0), 'rho': rho_eff,
        'R_genus': TWO_PI, 'R_arity': arity_convergence_radius(rho_eff),
        'double_convergent': rho_eff < 1.0,
        'genus_scope': EXACT_SCALAR_AHAT,
        'arity_scope': ARITY_RADIUS_DIAGNOSTIC,
        'full_shadow_pf_certified': False,
    })

    # sl_2 at various levels
    for k in [1, 2, 10, 100]:
        kap = kappa_affine_sl2(k)
        table.append({
            'name': f'sl_2 k={k}', 'kappa': kap, 'rho': 0.0,
            'R_genus': TWO_PI, 'R_arity': float('inf'),
            'double_convergent': True,
            'genus_scope': EXACT_SCALAR_AHAT,
            'arity_scope': FINITE_DEPTH_EXACT,
            'full_shadow_pf_certified': True,
        })

    return table


# ============================================================================
# 7. Scalar Bernoulli vs toy factorial comparison
# ============================================================================

def shadow_vs_string_comparison(kappa_val: float,
                                 max_genus: int = 10) -> Dict[str, Any]:
    r"""Compare scalar shadow coefficients with a toy factorial sequence.

    Scalar shadow: F_g^{scalar} = kappa * lambda_g^FP
      ~ 2|kappa| / (2*pi)^{2g}.

    The factorial comparison uses F_g^{toy} = (2g)! only as an
    asymptotic foil.  It is not a nonperturbative completion statement and
    does not compare against a full string partition function.
    """
    data = []
    for g in range(1, max_genus + 1):
        fg_shadow = abs(float(F_g(Rational(kappa_val), g)))
        fg_string = float(math.factorial(2 * g))
        ratio = fg_shadow / fg_string if fg_string > 0 else 0
        data.append({
            'g': g,
            'F_g_shadow': fg_shadow,
            'F_g_string': fg_string,
            'ratio': ratio,
            'log10_ratio': math.log10(ratio) if ratio > 0 else float('-inf'),
        })

    # Verify the ratio drops factorially
    ratio_ratios = []
    for i in range(1, len(data)):
        if data[i - 1]['ratio'] > 0:
            ratio_ratios.append(data[i]['ratio'] / data[i - 1]['ratio'])

    return {
        'kappa': kappa_val,
        'shadow_scope': EXACT_SCALAR_AHAT,
        'comparison_scope': 'toy_factorial_sequence',
        'nonperturbative_completion_certified': False,
        'data': data,
        'ratio_of_ratios': ratio_ratios,
        'factorial_decay_confirmed': all(r < 0.1 for r in ratio_ratios[2:]) if len(ratio_ratios) > 3 else False,
    }


def borel_comparison(kappa_val: float,
                      hbar_values: Optional[List[float]] = None,
                      max_genus: int = 100) -> Dict[str, Any]:
    r"""Compute scalar A-hat values and a scalar Borel-transform diagnostic.

    The ordinary scalar series converges inside |hbar| < 2*pi.  Dividing
    its scalar coefficients by (2g)! gives an entire Borel transform, but
    this routine does not certify Borel summability of the full
    planted-forest shadow partition function.
    """
    if hbar_values is None:
        hbar_values = [0.1, 0.5, 1.0, 2.0]

    results = []
    for hbar in hbar_values:
        if abs(hbar) >= TWO_PI:
            results.append({
                'hbar': hbar, 'Z_sh_exact': float('nan'),
                'note': 'outside convergence disc',
                'scope': EXACT_SCALAR_AHAT,
                'full_shadow_borel_certified': False,
            })
            continue

        Z_exact = genus_series_closed_form(kappa_val, hbar)
        Z_partial = genus_series_partial_sum(kappa_val, max_genus, hbar)
        rel_err = abs(Z_partial - Z_exact) / abs(Z_exact) if Z_exact != 0 else 0

        # Borel transform of shadow series at zeta = hbar (for comparison)
        borel_sum = 0.0
        for g in range(1, min(max_genus, 60) + 1):
            lam = float(lambda_fp(g))
            coeff = kappa_val * lam / math.factorial(2 * g)
            borel_sum += coeff * hbar ** (2 * g)

        results.append({
            'hbar': hbar,
            'Z_sh_exact': Z_exact,
            'Z_sh_partial': Z_partial,
            'relative_error': rel_err,
            'borel_transform_value': borel_sum,
            'borel_finite': math.isfinite(borel_sum),
            'scope': EXACT_SCALAR_AHAT,
            'borel_transform_scope': 'scalar_coefficients_divided_by_factorial',
            'full_shadow_borel_certified': False,
        })

    return {
        'kappa': kappa_val,
        'scope': EXACT_SCALAR_AHAT,
        'scalar_borel_transform_entire': True,
        'full_shadow_borel_certified': False,
        'results': results,
    }


# ============================================================================
# 8. Phase transition analysis
# ============================================================================

def phase_transition_scan(c_values: Optional[List[float]] = None
                           ) -> Dict[str, Any]:
    r"""Scan the Virasoro arity-radius diagnostic across c* ~ 6.125.

    For c < c*: rho > 1, so the arity-radius diagnostic gives radius < 1.
    For c > c*: rho < 1, so the diagnostic gives radius > 1.

    The critical cubic: 5c^3 + 22c^2 - 180c - 872 = 0.

    The labels "divergent", "convergent", and "marginal" refer to this
    arity-radius diagnostic, not to a certified full planted-forest
    partition function.
    """
    c_star = critical_central_charge()

    if c_values is None:
        c_values = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 5.5, 6.0,
                    c_star, 6.5, 7.0, 8.0, 10.0, 13.0, 20.0, 26.0]

    scan = []
    for c_val in c_values:
        rho = virasoro_rho(c_val)
        kap = kappa_virasoro(c_val)

        # Branch point argument (oscillation phase)
        # t_0 = (-12*c + i*sqrt(32*c^2 * 40/(5c+22))) / (2*(180c+872)/(5c+22))
        # Simplified: argument depends on Delta / alpha^2 ratio
        denom_sq = virasoro_rho_squared(c_val) * c_val ** 2
        # 9*alpha^2 = 36, 2*Delta = 80/(5c+22)
        nine_alpha_sq = 36.0
        two_delta = 80.0 / (5.0 * c_val + 22.0)
        discriminant_sign = two_delta  # always > 0 for c > 0
        theta = math.atan2(math.sqrt(4 * c_val ** 2 * two_delta),
                           -12.0 * c_val) if nine_alpha_sq + two_delta > 0 else 0

        phase = 'divergent' if rho > 1.0 else ('convergent' if rho < 1.0 else 'marginal')

        scan.append({
            'c': c_val,
            'kappa': kap,
            'rho': rho,
            'R_arity': arity_convergence_radius(rho),
            'phase': phase,
            'phase_scope': ARITY_RADIUS_DIAGNOSTIC,
            'full_shadow_pf_certified': False,
            'theta': theta,
            'F1': kap / 24.0,
        })

    return {
        'c_star': c_star,
        'scope': ARITY_RADIUS_DIAGNOSTIC,
        'full_shadow_pf_certified': False,
        'scan': scan,
    }


# ============================================================================
# 9. Analytic continuation in complex hbar
# ============================================================================

def analytic_continuation_complex_hbar(kappa_val: float,
                                        hbar_values: Optional[List[complex]] = None,
                                        max_genus: int = 80) -> List[Dict[str, Any]]:
    r"""Evaluate the scalar A-hat closed form at complex hbar values.

    Z_scalar(hbar) = kappa * ((hbar/2)/sin(hbar/2) - 1).

    This scalar function is meromorphic with poles at hbar = 2*pi*n.
    For complex hbar with |hbar| < 2*pi, the series converges absolutely.

    Test points:
    - hbar = 1 + i: inside the disc, generic complex
    - hbar = 2i: purely imaginary (Lorentzian signature)
    - hbar = -1: negative real
    """
    if hbar_values is None:
        hbar_values = [1.0 + 1.0j, 2.0j, -1.0 + 0j, 3.0 + 2.0j,
                       0.5 - 0.5j, 4.0j]

    results = []
    for hbar in hbar_values:
        hbar_c = complex(hbar)
        inside_disc = abs(hbar_c) < TWO_PI

        # Closed form using complex sin
        if abs(hbar_c) < 1e-15:
            Z_closed = 0.0 + 0.0j
        else:
            half_h = hbar_c / 2.0
            Z_closed = kappa_val * (half_h / cmath.sin(half_h) - 1.0)

        # Partial sum for verification
        Z_partial = 0.0 + 0.0j
        if inside_disc:
            for g in range(1, max_genus + 1):
                lam = float(lambda_fp(g))
                term = kappa_val * lam * hbar_c ** (2 * g)
                Z_partial += term
                if abs(term) < 1e-20 * max(abs(Z_partial), 1e-100):
                    break

        rel_err = (abs(Z_partial - Z_closed) / abs(Z_closed)
                   if abs(Z_closed) > 1e-50 and inside_disc else float('nan'))

        results.append({
            'hbar': hbar_c,
            'modulus_hbar': abs(hbar_c),
            'inside_disc': inside_disc,
            'Z_closed': Z_closed,
            'Z_partial': Z_partial if inside_disc else None,
            'relative_error': rel_err,
            'finite': cmath.isfinite(Z_closed),
            'scope': EXACT_SCALAR_AHAT,
            'full_shadow_pf_certified': False,
        })

    return results


def lorentzian_evaluation(kappa_val: float,
                           imag_hbar_values: Optional[List[float]] = None
                           ) -> List[Dict[str, Any]]:
    r"""Evaluate the scalar A-hat series at purely imaginary hbar.

    hbar = i*beta corresponds to Euclidean inverse temperature.
    Z_scalar(i*beta) = kappa * ((beta/2)/sinh(beta/2) - 1).

    This is real and finite for all beta (no poles on the imaginary axis,
    since sin(hbar/2) = sin(i*beta/2) = i*sinh(beta/2) has no real zeros
    except beta = 0).
    """
    if imag_hbar_values is None:
        imag_hbar_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]

    results = []
    for beta in imag_hbar_values:
        # Scalar A-hat value at i*beta.
        if abs(beta) < 1e-15:
            val = 0.0
        else:
            val = kappa_val * ((beta / 2.0) / math.sinh(beta / 2.0) - 1.0)

        results.append({
            'beta': beta,
            'hbar': complex(0, beta),
            'Z_sh': val,
            'is_real': True,
            'is_finite': math.isfinite(val),
            'sign': 'negative' if val < 0 else 'positive' if val > 0 else 'zero',
            'scope': EXACT_SCALAR_AHAT,
            'full_shadow_pf_certified': False,
        })

    return results


# ============================================================================
# 10. Verdier-dual branch and convergence diagnostics
# ============================================================================

def koszul_convergence_comparison(c_val: float) -> Dict[str, Any]:
    r"""Compare convergence diagnostics for Vir_c and the A^! branch.

    The function name is kept for compatibility.  The object A^! is the
    Verdier/continuous-linear dual branch in this atlas.  Omega(B(A))=A is
    bar-cobar inversion, and Z_ch^der(A) is a Hochschild/bulk object; neither
    is identified with this branch by this routine.

    Virasoro branch: A = Vir_c, A^! = Vir_{26-c}.  At c = 13 the diagnostic
    is fixed by the involution.
    """
    c_dual = 26.0 - c_val

    rho = virasoro_rho(c_val)
    rho_dual = virasoro_rho(c_dual) if c_dual > 0 else float('inf')

    kap = kappa_virasoro(c_val)
    kap_dual = kappa_virasoro(c_dual)

    return {
        'c': c_val,
        'c_dual': c_dual,
        'kappa': kap,
        'kappa_dual': kap_dual,
        'kappa_sum': kap + kap_dual,  # should be 13 for Virasoro
        'rho': rho,
        'rho_dual': rho_dual,
        'rho_product': rho * rho_dual if math.isfinite(rho_dual) else float('inf'),
        'self_dual': abs(c_val - 13.0) < 1e-10,
        'both_convergent': (rho < 1.0 and rho_dual < 1.0),
        'duality_branch': VERDIER_DUAL_BRANCH,
        'bar_cobar_inversion': BAR_COBAR_INVERSION_FIREWALL,
        'hochschild_bulk_relation': HOCHSCHILD_BULK_FIREWALL,
        'full_shadow_pf_certified': False,
    }


# ============================================================================
# 11. Affine KM approach to free field limit
# ============================================================================

def affine_sl2_free_field_limit(k_values: Optional[List[float]] = None
                                ) -> List[Dict[str, Any]]:
    r"""sl_2 convergence data as k -> infinity (free field limit).

    kappa(sl_2, k) = 3(k+2)/4 -> 3k/4 as k -> infinity.
    F_1 = kappa/24.
    R_arity = infinity (class L, rho = 0 for every finite listed k).

    The free field limit k -> infinity does not change the depth class:
    affine KM remains class L for all finite k.
    """
    if k_values is None:
        k_values = [1, 2, 5, 10, 20, 50, 100, 1000]

    results = []
    for k in k_values:
        kap = kappa_affine_sl2(k)
        results.append({
            'k': k,
            'kappa': kap,
            'rho': 0.0,
            'R_arity': float('inf'),
            'F1': kap / 24.0,
            'depth_class': 'L',
            'kappa_over_k': kap / k if k > 0 else float('inf'),
            'arity_scope': FINITE_DEPTH_EXACT,
        })

    return results


# ============================================================================
# 12. Comprehensive summary tables
# ============================================================================

def full_convergence_table() -> List[Dict[str, Any]]:
    r"""Master table of convergence diagnostics for atlas rows.

    Columns: name, class, kappa, rho, R_genus, R_arity,
             genus_conv, arity_conv, double_conv, F_1.
    """
    atlas = shadow_growth_rate_atlas()
    table = []
    for key, data in atlas.items():
        table.append({
            'key': key,
            'name': data.name,
            'class': data.depth_class,
            'depth': data.shadow_depth,
            'kappa': data.kappa,
            'rho': data.rho,
            'R_genus': data.R_genus,
            'R_arity': data.R_arity,
            'genus_conv': data.genus_convergent,
            'arity_conv': data.arity_convergent,
            'double_conv': data.double_convergent,
            'genus_scope': data.genus_scope,
            'arity_scope': data.arity_scope,
            'double_convergence_scope': data.double_convergence_scope,
            'full_shadow_pf_certified': data.full_shadow_pf_certified,
            'F1': data.F1,
        })
    return table


def virasoro_convergence_scan(
        c_values: Optional[List[float]] = None) -> List[Dict[str, Any]]:
    r"""Detailed Virasoro arity-radius diagnostic scan."""
    if c_values is None:
        c_star = critical_central_charge()
        c_values = [0.5, 1.0, 2.0, 4.0, 6.0, c_star,
                    7.0, 10.0, 13.0, 20.0, 25.0, 26.0]
    results = []
    for c_val in c_values:
        rho = virasoro_rho(c_val)
        kap = kappa_virasoro(c_val)
        results.append({
            'c': c_val,
            'kappa': kap,
            'rho': rho,
            'R_arity': arity_convergence_radius(rho),
            'R_genus': TWO_PI,
            'arity_convergent': rho < 1.0,
            'genus_scope': EXACT_SCALAR_AHAT,
            'arity_scope': ARITY_RADIUS_DIAGNOSTIC,
            'full_shadow_pf_certified': False,
            'F1': kap / 24.0,
            'F2': float(F_g(Rational(kap), 2)) if kap != 0 else 0,
        })
    return results


# ============================================================================
# 13. Scalar x arity majorant
# ============================================================================

def polylogarithm_5_2(rho: float, max_terms: int = 500) -> float:
    r"""Li_{5/2}(rho) = sum_{k>=1} rho^k / k^{5/2}.

    Converges for |rho| <= 1.
    """
    if abs(rho) > 1.0:
        return float('inf')
    total = 0.0
    for k in range(1, max_terms + 1):
        term = rho ** k / k ** 2.5
        total += term
        if abs(term) < 1e-25:
            break
    return total


def double_convergence_bound(kappa_val: float, rho: float) -> Dict[str, Any]:
    r"""Formal scalar x arity majorant.

    Under a separate analytic hypothesis bounding full arity coefficients
    by the rho-majorant, the product majorant has the form
    |kappa| * G * (1 + L).

    where G = 2/(4*pi^2 - 1) (genus geometric sum)
    and   L = Li_{5/2}(rho)   (arity polylogarithm).
    """
    G = 1.0 / (TWO_PI_SQ - 1.0)
    L = polylogarithm_5_2(rho)

    bound = abs(kappa_val) * 2.0 * G * (1.0 + L)

    return {
        'kappa': kappa_val,
        'rho': rho,
        'G': G,
        'L': L,
        'bound': bound,
        'convergent': rho < 1.0,
        'genus_scope': EXACT_SCALAR_AHAT,
        'arity_scope': ARITY_RADIUS_DIAGNOSTIC,
        'full_shadow_pf_certified': False,
        'analytic_hypothesis': ANALYTIC_HYPOTHESIS_REQUIRED,
    }


# ============================================================================
# 14. Bernoulli decay verification
# ============================================================================

def bernoulli_decay_table(max_genus: int = 20) -> List[Dict[str, float]]:
    r"""Verify Bernoulli decay: lambda_g^FP ~ 2/(2*pi)^{2g}.

    The ratio lambda_g^FP / (2/(2*pi)^{2g}) should approach 1 as g -> inf.
    """
    data = []
    for g in range(1, max_genus + 1):
        lam = float(lambda_fp(g))
        predicted = 2.0 / TWO_PI ** (2 * g)
        ratio = lam / predicted if predicted > 0 else 0
        data.append({
            'g': g,
            'lambda_fp': lam,
            'predicted': predicted,
            'ratio': ratio,
        })
    return data


def genus_ratio_table(max_genus: int = 20) -> List[Dict[str, float]]:
    r"""Consecutive ratios lambda_{g+1}^FP / lambda_g^FP -> 1/(2*pi)^2.

    This demonstrates the geometric decay with base 1/(2*pi)^2 ~ 0.0253.
    """
    data = []
    prev = float(lambda_fp(1))
    for g in range(2, max_genus + 1):
        curr = float(lambda_fp(g))
        ratio = curr / prev if prev > 0 else 0
        data.append({
            'g': g,
            'ratio': ratio,
            'target': 1.0 / TWO_PI_SQ,
            'relative_error': abs(ratio - 1.0 / TWO_PI_SQ) / (1.0 / TWO_PI_SQ),
        })
        prev = curr
    return data
