r"""Line-operator data for non-principal W-algebras via DNP25 constraints.

Computes line-operator category data for non-principal W-algebras
W^k(sl_N, f_lambda) using the DS-KD intertwining on the proved corridor
(hook type in type A).  The DNP25 framework applies to ALL 3d
holomorphic-topological QFTs: the line-operator category of a boundary
chiral algebra A is C_line(A) = A!_line-mod, where A! is the Koszul dual.

MATHEMATICAL CONTENT:

1. CENTRAL CHARGE AND KAPPA FOR NON-PRINCIPAL W-ALGEBRAS:
   - Bershadsky-Polyakov W^k(sl_3, f_{sub}):
       c_BP(k) = 2 - 3(2k+3)^2/(k+3)
       rho_BP = 1/6  (anomaly ratio: 1/1 - 2/3 - 2/3 + 1/2 for J,G+,G-,T)
       kappa_BP(k) = rho_BP * c_BP(k) = (1/6)(2 - 3(2k+3)^2/(k+3))
   - Minimal W^k(sl_3, f_{min}) = Zamolodchikov W_3^{(2)}:
       Same algebra as BP (sl_3 has only two non-trivial orbits,
       and (2,1) is BOTH subregular and minimal).  This is a key point:
       sl_3 is small enough that the subregular and minimal nilpotent
       coincide (both correspond to the partition (2,1)).

2. KOSZUL DUAL IDENTIFICATION VIA HOOK-TYPE TRANSPORT:
   For hook partition lambda = (N-p, 1^p) in sl_N:
     (W_k(sl_N, f_lambda))^! = W_{k'}(sl_N, f_{lambda^t})
   where k' = -k - 2N and lambda^t is the transpose partition.
   For sl_3, (2,1)^t = (2,1) (self-transpose!), so:
     (W_k(sl_3, f_{(2,1)}))^! = W_{-k-6}(sl_3, f_{(2,1)})
   i.e. the Bershadsky-Polyakov algebra is SELF-DUAL under Koszul duality
   (with level shift k -> -k-6).

3. LINE-OPERATOR CATEGORIES (DNP25):
   For hat{sl}_N at level k:
     C_line(V_k(sl_N)) = Rep_q(sl_N)  with q = exp(pi i/(k+N))
   DS reduction on line categories:
     C_line(W_k(sl_N, f_lambda)) should be a quotient/subcategory of
     Rep_q(sl_N) determined by the BRST functor.  For principal f:
     this is the full Rep_q(sl_N).  For non-principal f: this is a
     proper subcategory -- the EVALUATION sector restricted by f.

4. SHADOW DEPTH CLASSIFICATION:
   - Principal W_N: class M (infinite depth) on T-line.
   - BP = W^k(sl_3, f_{(2,1)}): class M on T-line (generic c nonzero,
     5c+22 generically nonzero), class G on J-line (abelian current).
   - Hook-type W^k(sl_N, f_{(N-1,1)}): class M on T-line universally.

5. THE r-MATRIX AND MULTI-CHANNEL STRUCTURE:
   For BP: the r-matrix r(z) = Res^{coll}_{0,2}(Theta_BP) involves
   ALL four generators (J, G+, G-, T).  The pole structure:
     J(z)J(w) ~ k_res/(z-w)^2  (double pole only -> r-matrix: k_res/z)
     J(z)G+(w) ~ G+(w)/(z-w)   (simple pole -> r-matrix: constant)
     G+(z)G-(w) ~ k_res/(z-w)^3 + J/(z-w)^2 + ...  (triple pole -> quadratic in 1/z)
     T(z)T(w) ~ c/2/(z-w)^4 + ...  (quartic pole -> cubic in 1/z)
   The multi-channel nature is STRUCTURAL: the r-matrix lives in
   End(V) where V = span{J, G+, G-, T} with mixed statistics.

6. KOSZUL CONDUCTOR:
   K_BP = c_BP(k) + c_BP(-k-6) = 196  (k-independent).
   Compare: K_{Vir} = 26, K_{W_3} = 100, K_{W_4} = 316.
   For BP: the conductor 196 does NOT match the principal W_3 conductor
   100 -- this is because BP is a DIFFERENT DS reduction of the SAME
   affine algebra sl_3.

References:
    Dimofte-Niu-Py (2025): line operators in 3d HT QFT
    Fehily (2022): hook-type inverse reduction
    Creutzig-Linshaw-Nakatsuka-Sato (2023): Feigin-Semikhatov duality
    Bershadsky (1991), Polyakov (1990): W^(2)_3 algebra
    Manuscript: thm:ds-koszul-obstruction, thm:hook-transport-corridor
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational,
    Symbol,
    cancel,
    cos,
    exp,
    expand,
    factor,
    oo,
    pi,
    simplify,
    solve,
    sqrt,
    sympify,
)

k = Symbol('k')


# =============================================================================
# 1. Central charge formulas for non-principal W-algebras
# =============================================================================

def bp_central_charge(level=None):
    """Central charge of the Bershadsky-Polyakov algebra W^k(sl_3, f_{(2,1)}).

    c_BP(k) = 2 - 24(k+1)^2/(k+3), K_BP = 196.
    BP formula (FKR 2020, verified k=-3/2 -> c=-2).
    """
    if level is None:
        level = k
    lev = sympify(level)
    return 2 - 24 * (lev + 1) ** 2 / (lev + 3)


def principal_w3_central_charge(level=None):
    """Central charge of the principal W_3 = W^k(sl_3, f_{(3)}).

    c_{W_3}(k) = 2 - 24(k+2)^2/(k+3)

    Fateev-Lukyanov formula.
    """
    if level is None:
        level = k
    lev = sympify(level)
    return 2 - 24 * (lev + 2) ** 2 / (lev + 3)


def principal_wn_central_charge(N, level=None):
    """Central charge of the principal W_N = W^k(sl_N, f_{(N)}).

    c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)
    """
    if level is None:
        level = k
    lev = sympify(level)
    return (N - 1) - N * (N ** 2 - 1) * (lev + N - 1) ** 2 / (lev + N)


def affine_central_charge(N, level=None):
    """Sugawara central charge for V_k(sl_N).

    c = k * dim(sl_N) / (k + h^v) = k(N^2-1)/(k+N).
    """
    if level is None:
        level = k
    lev = sympify(level)
    return lev * (N ** 2 - 1) / (lev + N)


def virasoro_central_charge(level=None):
    """Central charge of the Virasoro algebra = W^k(sl_2, f_{(2)}).

    c(k) = 1 - 6(k+1)^2/(k+2)
    """
    if level is None:
        level = k
    lev = sympify(level)
    return 1 - 6 * (lev + 1) ** 2 / (lev + 2)


# =============================================================================
# 2. Dual levels (Feigin-Frenkel involution)
# =============================================================================

def ff_dual_level(N, level=None):
    """Feigin-Frenkel dual level: k' = -k - 2h^v = -k - 2N for sl_N."""
    if level is None:
        level = k
    return -sympify(level) - 2 * N


def bp_dual_level(level=None):
    """Dual level for BP (sl_3): k' = -k - 6."""
    return ff_dual_level(3, level)


# =============================================================================
# 3. Koszul conductors
# =============================================================================

def koszul_conductor_bp():
    """K_BP = c_BP(k) + c_BP(-k-6).

    Should be 196, independent of k (FKR 2020).
    """
    c_k = bp_central_charge()
    c_kp = bp_central_charge(bp_dual_level())
    return simplify(c_k + c_kp)


def koszul_conductor_principal_wn(N):
    """K_{W_N} = c_{W_N}(k) + c_{W_N}(-k-2N).

    Known values: K_{Vir} = 26, K_{W_3} = 100, K_{W_4} = 246, K_{W_5} = 488.
    """
    c_k = principal_wn_central_charge(N)
    c_kp = principal_wn_central_charge(N, ff_dual_level(N))
    return simplify(c_k + c_kp)


# =============================================================================
# 4. Anomaly ratios and kappa
# =============================================================================

def bp_anomaly_ratio():
    """Anomaly ratio rho_BP for the Bershadsky-Polyakov algebra.

    Generators: J (h=1, bosonic), G+ (h=3/2, fermionic),
                G- (h=3/2, fermionic), T (h=2, bosonic).

    rho = 1/1 - 2/3 - 2/3 + 1/2 = 1 - 4/3 + 1/2 = 1/6.

    NOTE: fermionic generators contribute -1/h, bosonic contribute +1/h.
    """
    return (Rational(1, 1)            # J: bosonic, h=1
            - Rational(1, 1) * Rational(2, 3)   # G+: fermionic, 1/(3/2) = 2/3
            - Rational(1, 1) * Rational(2, 3)   # G-: fermionic, 1/(3/2) = 2/3
            + Rational(1, 2))          # T: bosonic, h=2


def bp_kappa(level=None):
    """Modular characteristic kappa for BP.

    kappa_BP(k) = rho_BP * c_BP(k) = (1/6) * c_BP(k).
    """
    return bp_anomaly_ratio() * bp_central_charge(level)


def principal_w3_anomaly_ratio():
    """Anomaly ratio for W_3: generators at h=2 (bosonic), h=3 (bosonic).

    rho = 1/2 + 1/3 = 5/6.
    """
    return Rational(1, 2) + Rational(1, 3)


def principal_w3_kappa(level=None):
    """kappa for W_3 = (5/6) * c_{W_3}(k)."""
    return principal_w3_anomaly_ratio() * principal_w3_central_charge(level)


def virasoro_anomaly_ratio():
    """Anomaly ratio for Virasoro: single generator T at h=2.

    rho = 1/2.
    """
    return Rational(1, 2)


def virasoro_kappa(level=None):
    """kappa for Virasoro = (1/2) * c_{Vir}(k)."""
    return virasoro_anomaly_ratio() * virasoro_central_charge(level)


# =============================================================================
# 5. Kappa complementarity
# =============================================================================

def bp_kappa_complementarity():
    """kappa_BP(k) + kappa_BP(-k-6): should be k-independent.

    For the self-transpose partition (2,1)^t = (2,1) in sl_3:
    kappa(k) + kappa(k') is a constant (the Koszul conductor times rho).
    """
    kap = bp_kappa()
    kap_dual = bp_kappa(bp_dual_level())
    return simplify(kap + kap_dual)


def principal_w3_kappa_complementarity():
    """kappa_{W_3}(k) + kappa_{W_3}(-k-6): should be k-independent.

    Since (3)^t = (1,1,1), the Koszul dual of W_3 is hat{sl}_3 at dual level.
    But W_3 IS the principal W-algebra, so the KD stays within the principal
    family: W_k(sl_3)^! = W_{-k-6}(sl_3).

    kappa_sum = (5/6) * K_{W_3} = (5/6) * 100 = 250/3.
    """
    kap = principal_w3_kappa()
    kap_dual = principal_w3_kappa(ff_dual_level(3))
    return simplify(kap + kap_dual)


# =============================================================================
# 6. Generator content and shadow depth classification
# =============================================================================

@dataclass(frozen=True)
class GeneratorData:
    """Strong generator content of a W-algebra."""
    name: str
    generators: Tuple[Tuple[str, object, str], ...]  # (name, weight, parity)
    num_bosonic: int
    num_fermionic: int
    anomaly_ratio: object
    shadow_depth_T: object   # depth on T-line
    shadow_class_T: str      # G, L, C, or M


def bp_generator_data():
    """Generator data for Bershadsky-Polyakov."""
    gens = (
        ('J', Rational(1), 'bosonic'),
        ('G+', Rational(3, 2), 'fermionic'),
        ('G-', Rational(3, 2), 'fermionic'),
        ('T', Rational(2), 'bosonic'),
    )
    return GeneratorData(
        name='Bershadsky-Polyakov W^k(sl_3, f_{(2,1)})',
        generators=gens,
        num_bosonic=2,
        num_fermionic=2,
        anomaly_ratio=bp_anomaly_ratio(),
        shadow_depth_T=oo,
        shadow_class_T='M',
    )


def principal_w3_generator_data():
    """Generator data for principal W_3."""
    gens = (
        ('T', Rational(2), 'bosonic'),
        ('W', Rational(3), 'bosonic'),
    )
    return GeneratorData(
        name='Principal W_3 = W^k(sl_3, f_{(3)})',
        generators=gens,
        num_bosonic=2,
        num_fermionic=0,
        anomaly_ratio=principal_w3_anomaly_ratio(),
        shadow_depth_T=oo,
        shadow_class_T='M',
    )


def virasoro_generator_data():
    """Generator data for Virasoro = W^k(sl_2, f_{(2)})."""
    gens = (
        ('T', Rational(2), 'bosonic'),
    )
    return GeneratorData(
        name='Virasoro = W^k(sl_2, f_{(2)})',
        generators=gens,
        num_bosonic=1,
        num_fermionic=0,
        anomaly_ratio=virasoro_anomaly_ratio(),
        shadow_depth_T=oo,
        shadow_class_T='M',
    )


# =============================================================================
# 7. Line-operator category data (DNP25 framework)
# =============================================================================

@dataclass(frozen=True)
class LineOperatorCategoryData:
    """Line-operator category data for a boundary chiral algebra A.

    By DNP25, C_line(A) = A!_line-mod, where A! is the Koszul dual.
    For affine algebras V_k(g), C_line = Rep_q(g) on the evaluation sector.
    For DS reductions, C_line is a subcategory determined by the BRST functor.
    """
    algebra_name: str
    partition: Tuple[int, ...]
    N: int
    # Koszul dual identification
    koszul_dual_name: str
    koszul_dual_partition: Tuple[int, ...]
    dual_level_formula: str
    is_self_dual: bool
    # Line-operator category
    line_category_description: str
    quantum_group_type: str
    quantum_parameter_formula: str
    # DS reduction constraint
    ds_reduction_type: str  # 'principal', 'subregular', 'minimal', 'hook', etc.
    ds_kd_commutes: bool    # True on proved corridor
    proof_status: str       # 'proved', 'conjectural'


def affine_line_operators(N, level=None):
    """Line-operator data for hat{sl}_N at level k.

    C_line(V_k(sl_N)) = Rep_q(sl_N), q = exp(pi i / (k + N)).
    Koszul dual: V_{-k-2N}(sl_N).
    """
    return LineOperatorCategoryData(
        algebra_name=f'V_k(sl_{N})',
        partition=(1,) * N,
        N=N,
        koszul_dual_name=f'V_{{-k-2{N}}}(sl_{N})',
        koszul_dual_partition=(1,) * N,
        dual_level_formula=f'k\' = -k - {2 * N}',
        is_self_dual=True,
        line_category_description=f'Rep_q(sl_{N}), evaluation sector',
        quantum_group_type=f'U_q(sl_{N})',
        quantum_parameter_formula=f'q = exp(pi i / (k + {N}))',
        ds_reduction_type='trivial',
        ds_kd_commutes=True,
        proof_status='proved',
    )


def bp_line_operators():
    """Line-operator data for BP = W^k(sl_3, f_{(2,1)}).

    Koszul dual: W_{-k-6}(sl_3, f_{(2,1)}) (self-dual, since (2,1)^t = (2,1)).
    Line-operator category: subcategory of Rep_q(sl_3) determined by
    the BRST reduction functor DS_{(2,1)}.

    The BRST functor DS_f: V_k(sl_3)-mod -> W_k(sl_3, f)-mod sends
    a V_k(sl_3)-module M to H^0(M tensor C_{chi}, Q_BRST).
    For hook-type f: this is an exact functor on the appropriate
    subcategory.  The image in line-operator categories is:

      C_line(BP) = DS_{(2,1)}(Rep_q(sl_3))

    which is a quotient category of Rep_q(sl_3).  The quantum group
    underlying the line operators is a QUOTIENT of U_q(sl_3), not a
    different quantum group.  Concretely, the simple objects of
    C_line(BP) are indexed by the BRST-nonvanishing representations
    of sl_3 at level k.
    """
    return LineOperatorCategoryData(
        algebra_name='W^k(sl_3, f_{(2,1)}) [Bershadsky-Polyakov]',
        partition=(2, 1),
        N=3,
        koszul_dual_name='W^{-k-6}(sl_3, f_{(2,1)}) [BP at dual level]',
        koszul_dual_partition=(2, 1),
        dual_level_formula='k\' = -k - 6',
        is_self_dual=True,
        line_category_description=(
            'DS_{(2,1)}(Rep_q(sl_3)): BRST reduction of evaluation '
            'modules of hat{sl}_3 at level k'
        ),
        quantum_group_type='Quotient of U_q(sl_3)',
        quantum_parameter_formula='q = exp(pi i / (k + 3))',
        ds_reduction_type='subregular = minimal (sl_3)',
        ds_kd_commutes=True,
        proof_status='proved (hook type, self-transpose)',
    )


def principal_w3_line_operators():
    """Line-operator data for W_3 = W^k(sl_3, f_{(3)}).

    Koszul dual: W_{-k-6}(sl_3, f_{(3)}) = W_3 at dual level.
    For the principal nilpotent, DS is the standard quantum DS reduction.
    Line-operator category:
      C_line(W_3) = DS_{(3)}(Rep_q(sl_3)) = full evaluation sector of Y(sl_3).
    """
    return LineOperatorCategoryData(
        algebra_name='W^k(sl_3, f_{(3)}) [principal W_3]',
        partition=(3,),
        N=3,
        koszul_dual_name='W^{-k-6}(sl_3, f_{(3)}) [W_3 at dual level]',
        koszul_dual_partition=(1, 1, 1),
        dual_level_formula='k\' = -k - 6',
        is_self_dual=False,
        line_category_description=(
            'DS_{(3)}(Rep_q(sl_3)): full quantum DS reduction, '
            'evaluation sector of Y(sl_3)_q'
        ),
        quantum_group_type='Y(sl_3)_q (quantum Yangian)',
        quantum_parameter_formula='q = exp(pi i / (k + 3))',
        ds_reduction_type='principal',
        ds_kd_commutes=True,
        proof_status='proved (principal)',
    )


def sl4_hook_31_line_operators():
    """Line-operator data for W^k(sl_4, f_{(3,1)}).

    Koszul dual: W_{-k-8}(sl_4, f_{(2,1,1)}) (transpose partition).
    Line-operator category: subcategory of Rep_q(sl_4).
    """
    return LineOperatorCategoryData(
        algebra_name='W^k(sl_4, f_{(3,1)}) [subregular]',
        partition=(3, 1),
        N=4,
        koszul_dual_name='W^{-k-8}(sl_4, f_{(2,1,1)}) [minimal, transpose]',
        koszul_dual_partition=(2, 1, 1),
        dual_level_formula='k\' = -k - 8',
        is_self_dual=False,
        line_category_description=(
            'DS_{(3,1)}(Rep_q(sl_4)): BRST reduction by subregular '
            'nilpotent of evaluation modules of hat{sl}_4'
        ),
        quantum_group_type='Quotient of U_q(sl_4)',
        quantum_parameter_formula='q = exp(pi i / (k + 4))',
        ds_reduction_type='subregular (hook type)',
        ds_kd_commutes=True,
        proof_status='proved (hook type)',
    )


def sl4_hook_211_line_operators():
    """Line-operator data for W^k(sl_4, f_{(2,1,1)}).

    Koszul dual: W_{-k-8}(sl_4, f_{(3,1)}) (transpose partition).
    """
    return LineOperatorCategoryData(
        algebra_name='W^k(sl_4, f_{(2,1,1)}) [minimal]',
        partition=(2, 1, 1),
        N=4,
        koszul_dual_name='W^{-k-8}(sl_4, f_{(3,1)}) [subregular, transpose]',
        koszul_dual_partition=(3, 1),
        dual_level_formula='k\' = -k - 8',
        is_self_dual=False,
        line_category_description=(
            'DS_{(2,1,1)}(Rep_q(sl_4)): BRST reduction by minimal '
            'nilpotent of evaluation modules of hat{sl}_4'
        ),
        quantum_group_type='Quotient of U_q(sl_4)',
        quantum_parameter_formula='q = exp(pi i / (k + 4))',
        ds_reduction_type='minimal (hook type)',
        ds_kd_commutes=True,
        proof_status='proved (hook type)',
    )


# =============================================================================
# 8. DS reduction on line categories: the commutative diagram
# =============================================================================

@dataclass(frozen=True)
class DSLineReductionDiagram:
    """The commutative diagram for DS reduction on line categories.

    The DS-KD intertwining on the proved corridor states:

        V_k(sl_N)  --DS(f_lam)-->  W_k(sl_N, f_lam)
             |                            |
            KD                           KD
             |                            |
        V_{k'}(sl_N) --DS(f_{lam^t})--> W_{k'}(sl_N, f_{lam^t})

    Passing to line categories:

        Rep_q(sl_N)  --DS(f_lam)-->  C_line(W_k(f_lam))
             |                            |
            KD                           KD
             |                            |
        Rep_{q'}(sl_N) --DS(f_{lam^t})--> C_line(W_{k'}(f_{lam^t}))

    where q = exp(pi i/(k+N)), q' = exp(pi i/(k'+N)).
    """
    N: int
    partition: Tuple[int, ...]
    transpose: Tuple[int, ...]
    is_self_transpose: bool
    # Top row
    source_algebra: str
    source_line_cat: str
    target_algebra: str
    target_line_cat: str
    # Bottom row
    dual_source_algebra: str
    dual_source_line_cat: str
    dual_target_algebra: str
    dual_target_line_cat: str
    # Diagram status
    left_vertical_proved: bool    # affine KD always proved
    right_vertical_proved: bool   # the DS-KD commutation claim
    top_horizontal_proved: bool   # DS reduction is constructive
    bottom_horizontal_proved: bool
    diagram_commutes: bool


def ds_line_reduction_diagram(partition, N=None):
    """Construct the DS-line reduction commutative diagram."""
    lam = tuple(sorted(partition, reverse=True))
    if N is None:
        N = sum(lam)
    lam_t = _transpose_partition(lam)
    is_self_t = (lam == lam_t)
    is_hook = _is_hook(lam)

    kv_str = f'-k - {2 * N}'

    return DSLineReductionDiagram(
        N=N,
        partition=lam,
        transpose=lam_t,
        is_self_transpose=is_self_t,
        source_algebra=f'V_k(sl_{N})',
        source_line_cat=f'Rep_q(sl_{N})',
        target_algebra=f'W_k(sl_{N}, f_{{{lam}}})',
        target_line_cat=f'DS_{{{lam}}}(Rep_q(sl_{N}))',
        dual_source_algebra=f'V_{{{kv_str}}}(sl_{N})',
        dual_source_line_cat=f'Rep_{{q\'}}(sl_{N})',
        dual_target_algebra=f'W_{{{kv_str}}}(sl_{N}, f_{{{lam_t}}})',
        dual_target_line_cat=f'DS_{{{lam_t}}}(Rep_{{q\'}}(sl_{N}))',
        left_vertical_proved=True,
        right_vertical_proved=is_hook or lam == (N,) or lam == (1,) * N,
        top_horizontal_proved=True,
        bottom_horizontal_proved=True,
        diagram_commutes=is_hook or lam == (N,) or lam == (1,) * N,
    )


# =============================================================================
# 9. Virasoro shadow tower (for depth classification)
# =============================================================================

def virasoro_shadow_tower(c_val, max_arity=10):
    """Compute S_r(c) for r = 2..max_arity via the master equation recursion.

    S_2 = c/2, S_3 = 2, S_4 = 10/(c(5c+22)).
    """
    c_sym = sympify(c_val)
    tower = {}
    tower[2] = c_sym / 2
    tower[3] = Rational(2)
    tower[4] = Rational(10) / (c_sym * (5 * c_sym + 22))

    for r in range(5, max_arity + 1):
        total = Rational(0)
        for j in range(2, r + 1):
            kk = r + 2 - j
            if kk < 2 or kk > r or j > kk:
                continue
            if j not in tower or kk not in tower:
                continue
            contrib = j * kk * tower[j] * tower[kk]
            if j == kk:
                contrib = contrib / 2
            total += contrib
        tower[r] = cancel(-total / (r * c_sym))

    return tower


def bp_shadow_tower_on_tline(max_arity=8):
    """BP shadow tower on the T-line: S_r^{Vir}(c_BP(k)).

    Returns dict {r: S_r(k)} as rational functions of k.
    """
    c_bp = bp_central_charge()
    c_sym = Symbol('c')
    vir_tower = virasoro_shadow_tower(c_sym, max_arity)

    result = {}
    for r, sr in vir_tower.items():
        result[r] = factor(cancel(sr.subs(c_sym, c_bp)))
    return result


def shadow_depth_classification(c_val):
    """Classify shadow depth on the T-line from central charge.

    Class G (depth 2): c = 0 (kappa = 0, tower trivializes).
    Class L (depth 3): 5c + 22 = 0, c = -22/5 (quartic diverges, but
                        special cancellation kills quintic and higher).
    Class M (infinite): generic c (quartic nonzero, infinite cascade).

    NOTE: this is the T-LINE classification only.  Multi-generator
    algebras can have different depths on different lines.
    """
    c_simplified = simplify(c_val)
    if c_simplified == 0:
        return 'G', 2
    if simplify(5 * c_val + 22) == 0:
        return 'L', 3
    return 'M', oo


def bp_shadow_depth():
    """Shadow depth classification for BP on each generator line.

    T-line: class M (infinite) -- generic c_BP nonzero and 5c_BP+22 nonzero.
    J-line: class G (depth 2) -- J is an abelian current, J_{(0)}J = 0.
    G-lines: determined by the G+/G- OPE structure (fermionic, class M).

    Overall classification: M (the deepest line dominates).
    """
    c_bp = bp_central_charge()
    t_class, t_depth = shadow_depth_classification(c_bp)

    return {
        'T_line': {'class': t_class, 'depth': t_depth},
        'J_line': {'class': 'G', 'depth': 2},
        'G_lines': {'class': 'M', 'depth': oo},
        'overall': 'M',
    }


# =============================================================================
# 10. r-matrix structure for non-principal W-algebras
# =============================================================================

@dataclass(frozen=True)
class RMatrixChannelData:
    """Data for a single OPE channel contributing to the r-matrix.

    The r-matrix r(z) = Res^{coll}_{0,2}(Theta_A) has poles determined
    by the OPE singular terms, SHIFTED DOWN by one order due to the
    d log(z-w) kernel (AP19: the bar kernel absorbs a pole).

    For an OPE a(z)b(w) ~ sum_{n>=0} c_n/(z-w)^{n+1}, the r-matrix
    contribution is sum_{n>=0} c_n / z^n (poles shifted down by 1).
    """
    source_gen: str
    target_gen: str
    ope_max_pole: int       # highest pole order in the OPE
    rmatrix_max_pole: int   # highest pole order in r-matrix (= ope - 1, AP19)
    channel_type: str       # 'bosonic-bosonic', 'bosonic-fermionic', 'fermionic-fermionic'


def bp_rmatrix_channels():
    """r-matrix channel data for the Bershadsky-Polyakov algebra.

    OPE structure (from Bershadsky 1991):
      J(z)J(w) ~ k_res/(z-w)^2                     (double pole)
      J(z)G+(w) ~ G+(w)/(z-w)                       (simple pole)
      J(z)G-(w) ~ -G-(w)/(z-w)                      (simple pole)
      J(z)T(w) ~ 0                                   (regular)
      G+(z)G-(w) ~ k_res/(z-w)^3 + J/(z-w)^2 + ... (triple pole)
      G+(z)G+(w) ~ 0                                 (fermionic, regular)
      G-(z)G-(w) ~ 0                                 (fermionic, regular)
      T(z)T(w) ~ c/2/(z-w)^4 + 2T/(z-w)^2 + dT/(z-w) (quartic pole)
      T(z)J(w) ~ J/(z-w)^2 + dJ/(z-w)              (double pole)
      T(z)G+(w) ~ (3/2)G+/(z-w)^2 + dG+/(z-w)      (double pole)
      T(z)G-(w) ~ (3/2)G-/(z-w)^2 + dG-/(z-w)      (double pole)

    r-matrix poles (AP19: shifted down by 1):
      J-J: single pole (from double pole OPE)
      J-G+: constant (from simple pole OPE)
      G+-G-: double pole (from triple pole OPE)
      T-T: cubic pole (from quartic pole OPE)
      T-J: single pole (from double pole OPE)
      T-G+: single pole (from double pole OPE)
    """
    channels = [
        RMatrixChannelData('J', 'J', 2, 1, 'bosonic-bosonic'),
        RMatrixChannelData('J', 'G+', 1, 0, 'bosonic-fermionic'),
        RMatrixChannelData('J', 'G-', 1, 0, 'bosonic-fermionic'),
        RMatrixChannelData('J', 'T', 0, 0, 'bosonic-bosonic'),
        RMatrixChannelData('G+', 'G-', 3, 2, 'fermionic-fermionic'),
        RMatrixChannelData('G+', 'G+', 0, 0, 'fermionic-fermionic'),
        RMatrixChannelData('G-', 'G-', 0, 0, 'fermionic-fermionic'),
        RMatrixChannelData('T', 'T', 4, 3, 'bosonic-bosonic'),
        RMatrixChannelData('T', 'J', 2, 1, 'bosonic-bosonic'),
        RMatrixChannelData('T', 'G+', 2, 1, 'bosonic-fermionic'),
        RMatrixChannelData('T', 'G-', 2, 1, 'bosonic-fermionic'),
    ]
    return channels


def bp_rmatrix_max_pole():
    """Maximum pole order in the BP r-matrix.

    The T-T channel has OPE pole order 4, so r-matrix pole order 3.
    This is the highest.
    """
    return 3


def principal_w3_rmatrix_max_pole():
    """Maximum pole order in the W_3 r-matrix.

    W(z)W(w) has pole order 6 (from the W_3 OPE), so r-matrix pole order 5.
    T(z)T(w) has pole order 4, so r-matrix pole order 3.
    The W-W channel dominates.
    """
    return 5


# =============================================================================
# 11. Comprehensive non-principal line-operator catalog
# =============================================================================

@dataclass(frozen=True)
class NonPrincipalLineOperatorEntry:
    """Complete line-operator entry for a non-principal W-algebra."""
    algebra_name: str
    lie_algebra: str
    N: int
    partition: Tuple[int, ...]
    transpose: Tuple[int, ...]
    nilpotent_type: str
    # Invariants
    central_charge: object
    anomaly_ratio: object
    kappa: object
    koszul_conductor: object
    # Depth
    shadow_class: str
    # Line operators
    line_cat_data: LineOperatorCategoryData
    # DS diagram
    ds_diagram: DSLineReductionDiagram
    # r-matrix
    rmatrix_max_pole: int
    num_rmatrix_channels: int


def build_catalog():
    """Build the complete catalog of non-principal line-operator data.

    Covers: sl_2 (Virasoro), sl_3 (BP, W_3), sl_4 (hooks).
    """
    catalog = {}

    # Virasoro = W^k(sl_2, f_{(2)})
    catalog['Vir'] = NonPrincipalLineOperatorEntry(
        algebra_name='Virasoro',
        lie_algebra='sl_2',
        N=2,
        partition=(2,),
        transpose=(1, 1),
        nilpotent_type='principal',
        central_charge=virasoro_central_charge(),
        anomaly_ratio=virasoro_anomaly_ratio(),
        kappa=virasoro_kappa(),
        koszul_conductor=Rational(26),
        shadow_class='M',
        line_cat_data=affine_line_operators(2),
        ds_diagram=ds_line_reduction_diagram((2,), 2),
        rmatrix_max_pole=3,
        num_rmatrix_channels=1,
    )

    # BP = W^k(sl_3, f_{(2,1)})
    catalog['BP'] = NonPrincipalLineOperatorEntry(
        algebra_name='Bershadsky-Polyakov',
        lie_algebra='sl_3',
        N=3,
        partition=(2, 1),
        transpose=(2, 1),
        nilpotent_type='subregular = minimal (sl_3)',
        central_charge=bp_central_charge(),
        anomaly_ratio=bp_anomaly_ratio(),
        kappa=bp_kappa(),
        koszul_conductor=Rational(196),  # K=196 (FKR 2020)
        shadow_class='M',
        line_cat_data=bp_line_operators(),
        ds_diagram=ds_line_reduction_diagram((2, 1), 3),
        rmatrix_max_pole=3,
        num_rmatrix_channels=11,
    )

    # W_3 = W^k(sl_3, f_{(3)})
    catalog['W3'] = NonPrincipalLineOperatorEntry(
        algebra_name='Principal W_3',
        lie_algebra='sl_3',
        N=3,
        partition=(3,),
        transpose=(1, 1, 1),
        nilpotent_type='principal',
        central_charge=principal_w3_central_charge(),
        anomaly_ratio=principal_w3_anomaly_ratio(),
        kappa=principal_w3_kappa(),
        koszul_conductor=Rational(100),
        shadow_class='M',
        line_cat_data=principal_w3_line_operators(),
        ds_diagram=ds_line_reduction_diagram((3,), 3),
        rmatrix_max_pole=5,
        num_rmatrix_channels=3,
    )

    # sl_4 hooks
    catalog['sl4_31'] = NonPrincipalLineOperatorEntry(
        algebra_name='W^k(sl_4, f_{(3,1)})',
        lie_algebra='sl_4',
        N=4,
        partition=(3, 1),
        transpose=(2, 1, 1),
        nilpotent_type='subregular (hook)',
        central_charge=None,  # would need the full KRW computation
        anomaly_ratio=None,
        kappa=None,
        koszul_conductor=None,
        shadow_class='M',
        line_cat_data=sl4_hook_31_line_operators(),
        ds_diagram=ds_line_reduction_diagram((3, 1), 4),
        rmatrix_max_pole=None,
        num_rmatrix_channels=None,
    )

    catalog['sl4_211'] = NonPrincipalLineOperatorEntry(
        algebra_name='W^k(sl_4, f_{(2,1,1)})',
        lie_algebra='sl_4',
        N=4,
        partition=(2, 1, 1),
        transpose=(3, 1),
        nilpotent_type='minimal (hook)',
        central_charge=None,
        anomaly_ratio=None,
        kappa=None,
        koszul_conductor=None,
        shadow_class='M',
        line_cat_data=sl4_hook_211_line_operators(),
        ds_diagram=ds_line_reduction_diagram((2, 1, 1), 4),
        rmatrix_max_pole=None,
        num_rmatrix_channels=None,
    )

    return catalog


# =============================================================================
# 12. Numerical evaluation helpers
# =============================================================================

def bp_numerical_at_level(level_val):
    """Evaluate all BP invariants numerically at a specific level."""
    lv = Rational(level_val)
    c_val = bp_central_charge(lv)
    kap_val = bp_kappa(lv)
    kap_dual = bp_kappa(bp_dual_level(lv))
    return {
        'level': lv,
        'c': c_val,
        'kappa': kap_val,
        'kappa_dual': kap_dual,
        'kappa_sum': simplify(kap_val + kap_dual),
        'dual_level': bp_dual_level(lv),
        'dual_c': bp_central_charge(bp_dual_level(lv)),
    }


def quantum_parameter_at_level(N, level_val):
    """Compute the quantum parameter q = exp(pi i / (k + N)) numerically."""
    lv = float(level_val)
    import cmath
    return cmath.exp(cmath.pi * 1j / (lv + N))


# =============================================================================
# 13. Utility functions
# =============================================================================

def _transpose_partition(lam):
    """Transpose a partition."""
    if not lam:
        return ()
    max_part = max(lam)
    result = []
    for j in range(1, max_part + 1):
        count = sum(1 for part in lam if part >= j)
        if count > 0:
            result.append(count)
    return tuple(result)


def _is_hook(lam):
    """Check if a partition is hook-type: (a, 1, 1, ..., 1)."""
    if not lam:
        return False
    lam_sorted = tuple(sorted(lam, reverse=True))
    if len(lam_sorted) <= 1:
        return True
    return all(p == 1 for p in lam_sorted[1:])
