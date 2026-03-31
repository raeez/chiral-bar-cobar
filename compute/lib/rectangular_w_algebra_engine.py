r"""Rectangular W-algebra engine: W^k(sl_4, f_{[2,2]}) Koszul duality data.

The first genuinely non-hook nilpotent orbit in type A.

MATHEMATICAL CONTENT:

1. Central charge: c(k) = 6(2k-1)/(k+4) via the Arakawa-Creutzig-Linshaw
   coset realization W^k(sl_4, f_{[2,2]}) = Com(V^{k+2}(sl_2), V^k(sl_4)).

2. Koszul conductor: K = c(k) + c(-k-8) = 24.

3. BV self-duality: partition [2,2] is self-transpose in type A_3,
   so W^k(sl_4, f_{[2,2]})^! = W^{-k-8}(sl_4, f_{[2,2]}).

4. Generator content: 3 generators at conformal weight 1 (residual sl_2
   at level 2k) + 4 generators at conformal weight 2 (matter).
   Total: 7 strong generators.

5. Modular characteristic kappa: computed via the structural formula
   kappa = c * rho_eff, with rho_eff determined from the conformal
   weight spectrum. See RECTIFICATION-FLAG below.

6. Shadow class analysis: class M (mixed, infinite tower) expected
   from the multi-generator structure with interacting sl_2 and matter.

ROOT DATA for [2,2] in sl_4:
  - Semisimple element: h = diag(1, -1, 1, -1)
  - Weighted Dynkin diagram: [0, 2, 0]
  - Levi g_0 = s(gl_2 x gl_2) = sl_2 x sl_2 x u(1), dim = 7
  - Nilradical n_+ = g_2 = {e_{12}, e_{14}, e_{32}, e_{34}}, dim = 4
  - Centralizer g^f: dim = 7
  - (g^e)_0: 3 generators (conformal weight 1, sl_2 currents)
  - (g^e)_2: 4 generators (conformal weight 2, matter fields)
  - All positive roots in n_+ have ad(h)-eigenvalue 2 (single grading level)

COSET REALIZATION (Arakawa-Creutzig-Linshaw 2019):
  W^k(sl_4, f_{[2,2]}) = Com(V^{k+2}(sl_2), V^k(sl_4))
  where sl_2 is the diagonal sl_2 defining the [2,2] embedding.
  The level k+2 = k + n (rectangular parameter n=2).

KOSZUL DUALITY:
  Dual: W^k(sl_4, f_{[2,2]})^! = W^{-k-8}(sl_4, f_{[2,2]})
  (self-dual orbit, level shifted by FF involution k -> -k-2h^v = -k-8)
  Koszul conductor: K = 24 (level-independent).

RECTIFICATION-FLAG: kappa formula
  The modular characteristic kappa is computed assuming kappa = c * rho_eff
  with constant anomaly ratio rho_eff = 3/4. This value is CONJECTURAL
  and is derived from the weighted generator formula
  rho_eff = (3 * 1/1 + 4 * 1/2) / (3 + 4) = 5/7... NO.

  Actually: the anomaly ratio for NON-PRINCIPAL W-algebras has not been
  established in the manuscript. The formula kappa = c * rho with constant
  rho is proved ONLY for principal W-algebras (Theorem genus-universality).
  For the [2,2] W-algebra, kappa must be computed from the explicit OPE
  data or character theory. The value reported here uses the structural
  constraint (kappa + kappa' is k-independent) together with the
  coset-additive approximation, which is flagged as unverified.

  The safest statement: kappa + kappa' = C for some constant C.
  The value of C requires independent computation.

Manuscript references:
    conj:w-orbit-duality (w_algebras.tex)
    comp:sl4-ds-hierarchy (w_algebras_deep.tex)
    rem:transport-closure-diagnostics (concordance.tex)
    thm:genus-universality (higher_genus_foundations.tex)
    def:bv-dual (w_algebras.tex)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    sqrt,
    together,
)


k = Symbol('k')


# ============================================================================
# 1.  Root data for [2,2] in sl_4
# ============================================================================

def sl2_triple_22():
    """The sl_2 triple data for the [2,2] nilpotent in sl_4.

    Returns the semisimple element h = diag(1,-1,1,-1) and
    the grading data.
    """
    h_diag = (1, -1, 1, -1)

    # ALL roots of sl_4 with ad(h) eigenvalues
    all_roots = []
    for i in range(4):
        for j in range(4):
            if i != j:
                eig = h_diag[i] - h_diag[j]
                all_roots.append({
                    'root': f'e{i+1}-e{j+1}',
                    'eigenvalue': eig,
                    'grade': eig // 2,
                })

    # Standard positive roots (i < j)
    pos_roots = [r for r in all_roots
                 if int(r['root'][1]) < int(r['root'][4])]

    # Nilradical n_+: ALL root spaces with POSITIVE ad(h) eigenvalue
    # (Kazhdan grading, not standard positive system)
    nilradical = [r for r in all_roots if r['eigenvalue'] > 0]

    # Levi g_0: root spaces with eigenvalue 0
    levi_roots = [r for r in all_roots if r['eigenvalue'] == 0]

    return {
        'h_diagonal': h_diag,
        'dynkin_diagram': (0, 2, 0),
        'positive_roots': pos_roots,
        'nilradical': nilradical,
        'levi_roots': levi_roots,
        'dim_nilradical': len(nilradical),
        'dim_levi': len(levi_roots) + 3,  # root spaces at eig 0 + Cartan of sl_4
        'dim_centralizer': 7,  # sum((lambda^t)_i^2) - 1 = 4+4-1 = 7
    }


def generator_content():
    """Generator content of W^k(sl_4, f_{[2,2]}).

    Returns conformal weights and multiplicities.
    The generators come from the centralizer g^e decomposed under
    the Kazhdan grading: x in (g^e)_{2j} contributes a generator
    of conformal weight j + 1.
    """
    return {
        'weights': {1: 3, 2: 4},
        'total_generators': 7,
        'description': {
            1: '3 spin-1 currents J^a (residual sl_2 at level 2k)',
            2: '4 spin-2 fields (matter, sl_2 representation)',
        },
        'residual_sl2_level': '2k (embedding index 2)',
    }


# ============================================================================
# 2.  Central charge
# ============================================================================

def central_charge(level=None):
    """Central charge of W^k(sl_4, f_{[2,2]}).

    c(k) = 6(2k - 1)/(k + 4)

    Derived from the Arakawa-Creutzig-Linshaw coset:
    W = Com(V^{k+2}(sl_2), V^k(sl_4))
    c = c(sl_4, k) - c(sl_2, k+2)
      = 15k/(k+4) - 3(k+2)/(k+4)
      = (12k - 6)/(k + 4)
      = 6(2k - 1)/(k + 4).

    Reference: Arakawa-Creutzig-Linshaw (2019), Theorem 1.1.
    """
    if level is None:
        level = k
    return 6 * (2 * level - 1) / (level + 4)


def c_sl4(level=None):
    """Sugawara central charge of hat{sl}_4 at level k."""
    if level is None:
        level = k
    return 15 * level / (level + 4)


def c_sl2_coset(level=None):
    """Central charge of the sl_2 at level k+2 in the coset."""
    if level is None:
        level = k
    return 3 * (level + 2) / (level + 4)


def verify_coset_central_charge(level=None):
    """Verify c(W_rect) = c(sl_4, k) - c(sl_2, k+2)."""
    if level is None:
        level = k
    diff = simplify(c_sl4(level) - c_sl2_coset(level) - central_charge(level))
    return diff == 0


# ============================================================================
# 3.  Feigin-Frenkel dual and Koszul conductor
# ============================================================================

def dual_level(level=None):
    """Feigin-Frenkel dual level: k' = -k - 2h^v = -k - 8."""
    if level is None:
        level = k
    return -level - 8


def dual_central_charge(level=None):
    """Dual central charge: c' = c(-k-8) = 24 - c(k)."""
    if level is None:
        level = k
    return central_charge(dual_level(level))


def koszul_conductor():
    """Koszul conductor K = c(k) + c(-k-8) = 24.

    Level-independent: verified symbolically.
    """
    return simplify(central_charge() + dual_central_charge())


def verify_koszul_conductor():
    """Verify K = 24 symbolically and numerically."""
    K_sym = koszul_conductor()
    K_is_24 = K_sym == 24

    # Numerical checks
    numerical_checks = []
    for kv in [Rational(1), Rational(2), Rational(5), Rational(10),
               Rational(-1), Rational(-3), Rational(100)]:
        c_val = central_charge(kv)
        c_dual_val = dual_central_charge(kv)
        K_val = c_val + c_dual_val
        numerical_checks.append({
            'k': kv,
            'c': c_val,
            'c_dual': c_dual_val,
            'K': K_val,
            'is_24': K_val == 24,
        })

    return {
        'symbolic': K_is_24,
        'K_symbolic': K_sym,
        'numerical': numerical_checks,
        'all_pass': K_is_24 and all(nc['is_24'] for nc in numerical_checks),
    }


# ============================================================================
# 4.  BV self-duality
# ============================================================================

def partition():
    """The partition [2,2] of 4."""
    return (2, 2)


def transpose_partition():
    """Transpose of [2,2] = [2,2] (self-transpose)."""
    return (2, 2)


def is_bv_self_dual():
    """Check BV self-duality: [2,2]^t = [2,2]."""
    return partition() == transpose_partition()


def orbit_dimension():
    """Dimension of the nilpotent orbit O_{[2,2]} in sl_4.

    dim O = N^2 - sum (lambda^t_i)^2 = 16 - (4+4) = 8.
    """
    return 8


def centralizer_dimension():
    """Dimension of the centralizer g^f.

    dim g^f = sum (lambda^t_i)^2 - 1 = 4 + 4 - 1 = 7.
    """
    return 7


# ============================================================================
# 5.  Modular characteristic kappa (FLAGGED)
# ============================================================================

def kappa_sl4_km(level=None):
    """Modular characteristic of hat{sl}_4 at level k.

    kappa = dim(sl_4) * (k + h^v) / (2 * h^v) = 15(k+4)/8.
    """
    if level is None:
        level = k
    return Rational(15) * (level + 4) / 8


def kappa_sl2_km(sl2_level=None):
    """Modular characteristic of hat{sl}_2 at level ell.

    kappa = 3(ell + 2)/4.
    """
    if sl2_level is None:
        sl2_level = 2 * k  # residual sl_2 level = 2k
    return Rational(3) * (sl2_level + 2) / 4


def residual_sl2_level(level=None):
    """Level of the residual sl_2 (centralizer) inside W_rect.

    The diagonal sl_2^{centr} in sl_4 has embedding index 2,
    so its level inside hat{sl}_4_k is 2k.
    """
    if level is None:
        level = k
    return 2 * level


def residual_sl2_central_charge(level=None):
    """Central charge of the residual sl_2 at level 2k.

    c(sl_2, 2k) = 3*2k/(2k+2) = 3k/(k+1).
    """
    if level is None:
        level = k
    ell = residual_sl2_level(level)
    return 3 * ell / (ell + 2)


def matter_central_charge(level=None):
    """Central charge of the matter sector: c_matter = c_total - c_{sl_2}.

    c_matter = 6(2k-1)/(k+4) - 3k/(k+1)
             = 3(3k^2 - 2k - 2) / ((k+1)(k+4)).
    """
    if level is None:
        level = k
    return simplify(central_charge(level) - residual_sl2_central_charge(level))


# RECTIFICATION-FLAG: The following kappa computation is a STRUCTURAL ESTIMATE.
# It uses the fact that kappa + kappa' must be k-independent (from concordance)
# and assumes the simplest rational form consistent with this constraint.
# The exact value requires explicit OPE data or character computation.

def kappa_rect_estimate(level=None):
    """ESTIMATED modular characteristic of W^k(sl_4, f_{[2,2]}).

    STRUCTURAL ESTIMATE using the constraint:
    kappa(k) + kappa(-k-8) = C (constant, k-independent).

    The simplest rational form kappa = (ak + b)/(k+4) gives C = 2a.
    With the additional constraint kappa(1/2) = 0 (vanishing at c=0),
    we get b = -a/2, so kappa = a(2k-1)/(2(k+4)) = (a/12) * c.

    The constant anomaly ratio rho_eff = a/12 is estimated from the
    generator-weighted formula:
    rho_eff = (3 * (1/1) + 4 * (1/2)) / (3 * 1 + 4 * 1)...

    HOWEVER: this formula is not verified for non-principal W-algebras.
    The kappa = rho * c formula with constant rho holds only for
    principal W-algebras (Theorem genus-universality).

    For the [2,2] W-algebra, kappa may have a more complex k-dependence
    (e.g., kappa = ak + b + c_term/(k+4)) because the sl_2 sector at
    level 2k contributes kappa ~ 3k/2 at large k.

    BOTTOM LINE: kappa is reported as UNKNOWN/CONJECTURAL.
    The complementarity constant kappa + kappa' is k-independent
    (structural fact) but its VALUE is not determined here.
    """
    if level is None:
        level = k
    # Return None to signal that kappa is not reliably computed
    return None


def kappa_complementarity_sum():
    """The constant kappa + kappa' for the self-dual [2,2] orbit.

    From concordance rem:transport-closure-diagnostics item (iii):
    kappa(W^k(g, f_eta)) + kappa(W^{-k-2h^v}(g, f_{eta^t})) is
    k-independent for ALL orbits.

    For self-dual orbits (eta = eta^t), this gives:
    kappa(k) + kappa(-k-8) = C.

    The VALUE of C requires explicit computation (OPEN).
    Returns: None (value unknown).
    """
    return None


# ============================================================================
# 6.  Comparison with other orbits in sl_4
# ============================================================================

def sl4_orbit_hierarchy():
    """Complete nilpotent orbit hierarchy for sl_4.

    Returns data for all 5 orbits (partitions of 4).
    """
    return {
        (1, 1, 1, 1): {
            'name': 'trivial (sl_4 hat)',
            'orbit_dim': 0,
            'generators': 15,
            'gen_weights': {1: 15},
            'bv_dual': (4,),
            'type': 'affine KM',
        },
        (2, 1, 1): {
            'name': 'minimal',
            'orbit_dim': 8,
            'generators': 12,
            'gen_weights': {1: 8, Rational(3, 2): 4},
            'bv_dual': (3, 1),
            'type': 'hook (minimal)',
        },
        (2, 2): {
            'name': 'rectangular',
            'orbit_dim': 8,
            'generators': 7,
            'gen_weights': {1: 3, 2: 4},
            'bv_dual': (2, 2),
            'type': 'rectangular (self-dual)',
        },
        (3, 1): {
            'name': 'subregular',
            'orbit_dim': 12,
            'generators': 3,
            'gen_weights': {1: 1, 2: 1, 3: 1},
            'bv_dual': (2, 1, 1),
            'type': 'hook (subregular)',
        },
        (4,): {
            'name': 'principal (W_4)',
            'orbit_dim': 12,
            'generators': 3,
            'gen_weights': {2: 1, 3: 1, 4: 1},
            'bv_dual': (1, 1, 1, 1),
            'type': 'principal',
        },
    }


def c_principal_W4(level=None):
    """Central charge of principal W_4 = W^k(sl_4, f_{(4)}).

    c = 3 - N(N^2-1)(k+N-1)^2/(k+N) with N=4.
    = 3 - 60(k+3)^2/(k+4).
    """
    if level is None:
        level = k
    return 3 - 60 * (level + 3) ** 2 / (level + 4)


def K_principal_W4():
    """Koszul conductor for principal W_4.

    K = 2(N-1)(2N^2+2N+1) = 2*3*(32+8+1) = 246.
    """
    return 246


def bv_duality_table():
    """BV duality pairing for sl_4 orbits.

    In type A, BV duality = partition transpose.
    (1^4) <-> (4), (2,1^2) <-> (3,1), (2^2) <-> (2^2).
    """
    return {
        (1, 1, 1, 1): (4,),
        (2, 1, 1): (3, 1),
        (2, 2): (2, 2),
        (3, 1): (2, 1, 1),
        (4,): (1, 1, 1, 1),
    }


# ============================================================================
# 7.  Ghost sector data
# ============================================================================

def ghost_data():
    """Ghost sector data for the DS reduction sl_4 -> W_rect.

    The DS reduction removes the nilradical n_+ (dim 4).
    Each positive root in n_+ contributes one bc ghost pair.
    All roots have ad(h)/2 = 1 (single grading level j=1).
    Ghost weights: b at conformal weight 2, c at conformal weight -1.
    """
    return {
        'num_ghost_pairs': 4,
        'ghost_j_values': [1, 1, 1, 1],
        'b_weights': [2, 2, 2, 2],
        'c_weights': [-1, -1, -1, -1],
        'c_per_pair': -26,  # 1 - 3*(2*1+1)^2 = 1 - 27 = -26
        'c_ghost_total_bc': -104,
        'effective_ghost_c': lambda kv: 3 * (kv + 2) / (kv + 4),
        # c(sl_4) - c(W_rect) = 3(k+2)/(k+4), k-dependent!
    }


def effective_ghost_central_charge(level=None):
    """Effective ghost central charge: c(sl_4, k) - c(W_rect, k).

    = 15k/(k+4) - 6(2k-1)/(k+4) = (3k+6)/(k+4) = 3(k+2)/(k+4).

    Note: this is k-DEPENDENT (unlike the principal case where c_ghost = N(N-1)).
    """
    if level is None:
        level = k
    return simplify(c_sl4(level) - central_charge(level))


# ============================================================================
# 8.  Shadow class analysis
# ============================================================================

def shadow_class_analysis():
    """Shadow class analysis for the [2,2] W-algebra.

    The shadow class (G/L/C/M) depends on the quartic shadow S_4
    and the critical discriminant Delta = 8*kappa*S_4.

    For the [2,2] W-algebra:
    - Multi-generator: T (from sl_2 Sugawara) + 4 weight-2 fields.
    - The sl_2 currents introduce cubic OPE terms (J*T mixing).
    - The matter fields at weight 2 have quartic self-coupling.
    - Expected shadow class: M (mixed, infinite tower) because the
      non-abelian OPE structure forces S_4 != 0.

    The exact shadow class requires kappa and S_4 computation.
    """
    return {
        'expected_class': 'M',
        'reason': (
            'Non-abelian sl_2 current algebra + interacting matter at weight 2. '
            'The sl_2 OPE J^a(z)J^b(0) ~ k*delta/z^2 + f^{abc}J^c/z introduces '
            'non-trivial cubic shadows (class L or higher). The matter self-coupling '
            'and J-matter interaction force quartic and higher shadows (class M). '
            'Compare: principal W_4 (class M), affine sl_4 (class L).'
        ),
        'comparison': {
            'sl_4_hat': 'L (Lie/tree, r_max = 3)',
            'W_4_principal': 'M (mixed, r_max = infinity)',
            '[2,2]_rectangular': 'M (expected, needs verification)',
        },
    }


# ============================================================================
# 9.  Comprehensive summary
# ============================================================================

def full_koszul_data(level=None):
    """Complete Koszul duality data for W^k(sl_4, f_{[2,2]}).

    Returns a dictionary with all computed quantities.
    """
    if level is None:
        level = k

    c_val = central_charge(level)
    kp = dual_level(level)
    c_dual = dual_central_charge(level)
    K = simplify(c_val + c_dual)

    return {
        'partition': (2, 2),
        'algebra': 'sl_4',
        'orbit_type': 'rectangular (even)',
        'h_vee': 4,

        # Central charge
        'c': c_val,
        'c_formula': '6(2k-1)/(k+4)',

        # Duality
        'dual_level': kp,
        'dual_level_formula': '-k-8',
        'c_dual': c_dual,
        'K': K,
        'K_value': 24,
        'bv_self_dual': True,

        # Generators
        'generators': generator_content(),

        # Residual sl_2
        'sl2_level': residual_sl2_level(level),
        'sl2_central_charge': residual_sl2_central_charge(level),
        'matter_central_charge': matter_central_charge(level),

        # Ghost sector
        'ghost_effective_c': effective_ghost_central_charge(level),
        'ghost_effective_c_formula': '3(k+2)/(k+4)',

        # Kappa (FLAGGED)
        'kappa': None,  # Not reliably computed
        'kappa_status': 'OPEN',
        'kappa_sum_rule': 'kappa + kappa_dual = const (structural, value OPEN)',

        # Shadow class
        'shadow_class': 'M (expected)',
        'shadow_class_status': 'CONJECTURAL',

        # Root data
        'root_data': sl2_triple_22(),
    }


def numerical_evaluation(k_val):
    """Evaluate all quantities at a specific level k."""
    kv = Rational(k_val) if isinstance(k_val, (int, float, str)) else k_val
    data = full_koszul_data(kv)

    # Simplify all sympy expressions
    for key in data:
        val = data[key]
        if hasattr(val, 'is_number'):
            try:
                data[key] = simplify(val)
            except Exception:
                pass

    return data
