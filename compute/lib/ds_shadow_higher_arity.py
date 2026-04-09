r"""DS shadow functor at higher arities and non-principal Bershadsky-Polyakov reduction.

NEW COMPUTATION. Extends the DS shadow functor from arities 2-4 (ds_shadow_functor.py)
to arities 5-8, and computes the FIRST NON-PRINCIPAL shadow obstruction tower: the Bershadsky-Polyakov
algebra W^k(sl_3, f_min).

PART 1: PRINCIPAL DS SHADOW FUNCTOR AT ARITIES 5-8.

For principal DS reduction sl_N -> W_N at level k:
  c_{W_N}(k) = (N-1)(1 - N(N+1)/(k+N))

IMPORTANT CAVEAT: Whether DS reduction commutes with the shadow obstruction tower is an
OPEN CONJECTURE, not a theorem. The computations here verify CONSISTENCY: the
W_N shadow obstruction tower, independently computed from the W_N OPE, when parametrised
by the DS level k through c = c_{W_N}(k), yields rational functions of k. This
is necessary for DS commutation but far from sufficient. The functorial statement
DS(Theta_{sl_N}) = Theta_{W_N} in MC(g^mod_{W_N}) is conjectural.

What IS computed:
  Sh_r^{W_N}(k) := S_r^{Vir}(c_{W_N}(k)) on the T-line
  = the W_N shadow obstruction tower parametrised by the DS level.

THE DEPTH-INCREASE OBSTRUCTION:
  sl_N has shadow depth 3 (class L): Sh_r = 0 for r >= 4
  W_N has shadow depth infinity (class M): Sh_r != 0 for all r
  If DS commuted naively with the shadow obstruction tower, it would preserve depth.
  It does NOT: the ghost sector creates new obstruction classes.
  This is a structural obstruction to naive functoriality, not a resolution.
  The quartic Q^contact_{W_N} is independently computed from the W_N OPE;
  whether it equals the BRST-created quartic from DS(sl_N) is open.

PART 2: BERSHADSKY-POLYAKOV W^k(sl_3, f_min).

The Bershadsky-Polyakov (BP) algebra is the DS reduction of sl_3 with MINIMAL nilpotent
f = e_{12} (not principal f = e_{12} + e_{23}). This is genuinely non-principal.

Generators: J (weight 1), G^+ (weight 3/2), G^- (weight 3/2), T (weight 2).
Central charge: c_BP(k) = 2 - 24(k+1)^2/(k+3) = (-24k^2 - 46k - 18)/(k+3).
Dual level: k' = -k - 6 (involution). Koszul conductor: K_BP = 196.
BP formula: c = 2 - 24(k+1)^2/(k+3), K=196 (FKR 2020, verified k=-3/2 -> c=-2)

Shadow structure:
  T-line: Virasoro tower at c = c_BP(k). Depth infinity (class M).
  J-line: U(1) current at level k_res = k + 1/2. Depth 2 (class G, abelian).
  Mixed J-T: The J-T coupling J_{(0)}T = partial T (derivative). This coupling
    creates off-diagonal shadow data starting at arity 4.

This is the first computation of the shadow obstruction tower for a NON-PRINCIPAL W-algebra.

References:
  ds_shadow_functor.py: arities 2-4 principal DS
  virasoro_shadow_tower.py: Virasoro recursion
  virasoro_shadow_factored.py: Delta-factored form
  nonprincipal_ds_reduction.py: BP seed data (central charge, dual level)
  w3_multivariable_shadow.py: W_3 multi-variable shadow
  shadow_tower_atlas.py: all standard shadow obstruction towers
"""

from __future__ import annotations

from sympy import (
    Rational, Symbol, cancel, expand, factor, simplify, S,
)

k = Symbol('k')
c = Symbol('c')


# =============================================================================
# 1. Virasoro shadow obstruction tower (standalone recursion to arity 10)
# =============================================================================

def _virasoro_tower_internal(max_arity=10):
    """Virasoro shadow coefficients S_r(c) using master equation recursion.

    The master equation nabla_H(Sh_r) + o^(r) = 0 gives, after separating
    the j=2 Hessian-flow term:

        S_r = -(1/(r*c)) * sum_{3<=j<=k, j+k=r+2} eps(j,k) * j*k * S_j * S_k

    where eps(j,k) = 1 if j<k, 1/2 if j=k.  S_2, S_3, S_4 are initial data.

    Implementation note: the loop below starts at j=2 but effectively skips
    the j=2, k=r term because tower[r] is not yet in the dict when the
    loop runs.  This produces the correct formula.
    """
    tower = {}
    tower[2] = c / 2
    tower[3] = Rational(2)
    tower[4] = Rational(10) / (c * (5 * c + 22))

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
        tower[r] = cancel(-total / (r * c))

    return tower


# =============================================================================
# 2. Central charge maps
# =============================================================================

def principal_ds_central_charge(n, level=None):
    """Central charge of W_N = DS_{principal}(sl_N) at level k.

    c_{W_N}(k) = (N-1)(1 - N(N+1)/(k+N))
    """
    if level is None:
        level = k
    return (n - 1) * (1 - n * (n + 1) / (level + n))


def bp_central_charge(level=None):
    """Bershadsky-Polyakov central charge: c_BP(k) = 2 - 24(k+1)^2/(k+3).

    BP formula: c = 2 - 24(k+1)^2/(k+3), K=196 (FKR 2020, verified k=-3/2 -> c=-2)
    This is the DS reduction of sl_3 with MINIMAL nilpotent f = e_{12}.
    Equivalently: c_BP(k) = (-24k^2 - 46k - 18)/(k+3).

    Special values:
      c_BP(-3/2) = -2 (FKR 2020 admissible match)
      c_BP(-1) = 2
      c_BP(0) = -6
      c_BP(1) = -22
    """
    if level is None:
        level = k
    return 2 - 24 * (level + 1) ** 2 / (level + 3)


def bp_dual_level(level=None):
    """Feigin-Frenkel dual level for BP: k' = -k - 6.

    This is an involution: (k')' = k.
    Complementarity: c_BP(k) + c_BP(-k-6) = 76 (the Koszul conductor).
    """
    if level is None:
        level = k
    return -level - 6


def bp_residual_level(level=None):
    """Residual sl_2 level in the BP reduction: k_res = k + 1/2.

    The J current in BP is a U(1) current at this level.
    J(z)J(w) ~ k_res / (z-w)^2.
    """
    if level is None:
        level = k
    return level + Rational(1, 2)


# =============================================================================
# 3. Principal DS shadow obstruction tower at higher arities
# =============================================================================

def principal_ds_shadow_tower(n, max_r=8):
    """Principal DS shadow obstruction tower for W_N on the T-line, arities 2..max_r.

    Returns dict {r: Sh_r(k)} where each entry is a rational function of k.
    These are obtained by substituting c = c_{W_N}(k) into the Virasoro tower.

    For N = 2: W_2 = Virasoro, c(k) = 1 - 6/(k+2) = (k-4)/(k+2).
    For N = 3: c(k) = 2(k-9)/(k+3).
    For general N: c(k) = (N-1)(1 - N(N+1)/(k+N)).

    The T-line of W_N carries the Virasoro subalgebra, so the shadow obstruction tower
    on this line is the Virasoro tower evaluated at the DS central charge.
    """
    c_wn = principal_ds_central_charge(n)
    vir = _virasoro_tower_internal(max_r)

    ds_tower = {}
    for r in range(2, max_r + 1):
        Sr_of_k = vir[r].subs(c, c_wn)
        ds_tower[r] = factor(cancel(Sr_of_k))

    return ds_tower


def principal_ds_verify_at_level(n, level_val, max_r=8):
    """Numerically verify principal DS shadow obstruction tower at a specific level.

    Returns dict {r: (Sh_r_value, nonzero)} for each arity.
    """
    tower = principal_ds_shadow_tower(n, max_r)
    results = {}
    for r in range(2, max_r + 1):
        val = tower[r].subs(k, level_val)
        results[r] = {
            'value': val,
            'numerical': float(val) if val.is_finite else None,
            'nonzero': val != 0,
        }
    return results


# =============================================================================
# 4. DS depth increase mechanism
# =============================================================================

def ds_depth_increase_mechanism(n):
    """Explain why DS takes depth 3 (sl_N) to depth infinity (W_N).

    Returns a dict with the mechanism at each arity level.

    THE PARADOX:
      sl_N has depth 3: Sh_r = 0 for r >= 4 (Jacobi identity).
      W_N has depth infinity: Sh_r != 0 for all r >= 2.
      DS reduction INCREASES shadow depth from 3 to infinity.

    RESOLUTION AT EACH ARITY:

    Arity 4 (quartic seed): The sl_N quartic is zero (Jacobi). But DS
      introduces bc ghosts with NONZERO quartic. The BRST cohomology projects
      Q_ghosts to a nonzero Q_{W_N}. The quartic is CREATED by the ghost sector.

    Arity 5 (quintic, first propagated): Once Q_{W_N} != 0, the master equation
      generates Sh_5 = -nabla_H^{-1}({C, Q}_H) from the bracket of the cubic
      and quartic. The cubic C (which survives from sl_N) and the DS-created
      quartic Q together produce a nonzero quintic obstruction.

    Arity r >= 6 (all higher): The cascade continues. Each Sh_r is generated
      from lower shadows via the master equation. The DS-created quartic at
      arity 4 is the SEED that drives the entire infinite tower.

    QUANTITATIVE: The quartic on the T-line is
      Q = 10/[c_{W_N}(k) * (5*c_{W_N}(k) + 22)]
    which is a rational function of k with poles at k = -N (critical)
    and at the zero of 5c+22.
    """
    c_wn = principal_ds_central_charge(n)
    c_wn_factored = factor(c_wn)

    val_5c22 = factor(5 * c_wn + 22)
    Q_of_k = factor(cancel(Rational(10) / (c_wn * (5 * c_wn + 22))))

    vir = _virasoro_tower_internal(8)
    Sh5_of_k = factor(cancel(vir[5].subs(c, c_wn)))

    return {
        'N': n,
        'sl_N_depth': 3,
        'W_N_depth': 'infinity',
        'c_WN': c_wn_factored,
        '5c+22': val_5c22,
        'Q_quartic_seed': Q_of_k,
        'Sh5_from_seed': Sh5_of_k,
        'mechanism': {
            'arity_4': 'Ghost sector creates nonzero quartic via BRST cohomology',
            'arity_5': 'Bracket {C, Q}_H gives nonzero quintic obstruction',
            'arity_r': 'Cascade: quartic seed propagates through master equation',
        },
        'key_identity': 'Sh_4^{sl_N} = 0, but Sh_4^{W_N} = Q(ghost) != 0',
    }


# =============================================================================
# 5. DS depth comparison table
# =============================================================================

def ds_shadow_depth_comparison(max_N=6):
    """Table showing depth(sl_N)=3 -> depth(W_N)=infinity under DS.

    Returns a dict {N: {sl_N_depth, W_N_depth, c_WN, kappa_WN, Q_4}} for N=2..max_N.
    """
    results = {}
    for n in range(2, max_N + 1):
        c_wn = principal_ds_central_charge(n)
        # kappa for W_N on T-line = c/2
        kappa_wn = c_wn / 2
        # Quartic on T-line = Virasoro quartic at c = c_WN
        Q_4 = Rational(10) / (c_wn * (5 * c_wn + 22))

        results[n] = {
            'sl_N_depth': 3,
            'sl_N_class': 'L',
            'W_N_depth': 'infinity',
            'W_N_class': 'M',
            'c_WN': factor(c_wn),
            'kappa_WN': factor(cancel(kappa_wn)),
            'Q_4': factor(cancel(Q_4)),
            'Q_4_nonzero': simplify(Q_4) != 0,
        }

    return results


# =============================================================================
# 6. Bershadsky-Polyakov kappa values
# =============================================================================

def bershadsky_polyakov_kappa(level=None):
    """kappa_BP on the T-line: kappa = c_BP(k)/2.

    This is the Virasoro curvature for the T-component of BP.
    """
    c_bp = bp_central_charge(level)
    return cancel(c_bp / 2)


def bershadsky_polyakov_kappa_j(level=None):
    """kappa_BP on the J-line: kappa_J = k_res = k + 1/2 (AP39: kappa(H_k) = k).

    The J current is U(1) at residual level k_res = k + 1/2.
    J(z)J(w) ~ k_res/(z-w)^2, so kappa_J = k_res.
    """
    if level is None:
        level = k
    k_res = level + Rational(1, 2)
    return k_res


# =============================================================================
# 7. Bershadsky-Polyakov shadow obstruction tower on T-line
# =============================================================================

def bershadsky_polyakov_shadow_tower(max_r=6):
    """BP shadow obstruction tower on the T-line, arities 2..max_r.

    Returns dict {r: Sh_r(k)} where each entry is a rational function of k.
    Obtained by substituting c = c_BP(k) into the Virasoro tower.

    The T-line of BP carries the Virasoro subalgebra (the T generator),
    so the shadow obstruction tower on this line equals the Virasoro tower at c = c_BP(k).

    The tower is infinite (class M) because c_BP is generically nonzero
    and 5c_BP + 22 is generically nonzero.
    """
    c_bp = bp_central_charge()
    vir = _virasoro_tower_internal(max_r)

    bp_tower = {}
    for r in range(2, max_r + 1):
        Sr_of_k = vir[r].subs(c, c_bp)
        bp_tower[r] = factor(cancel(Sr_of_k))

    return bp_tower


# =============================================================================
# 8. Bershadsky-Polyakov shadow obstruction tower on J-line
# =============================================================================

def bershadsky_polyakov_j_line(max_r=4):
    """BP shadow obstruction tower on the J-line, arities 2..max_r.

    Returns dict {r: Sh_r(k)} on the J-line.

    The J current is U(1) (abelian). The J-J OPE is:
      J(z)J(w) ~ k_res/(z-w)^2

    with no singular terms beyond the double pole. In particular:
      J_{(0)}J = 0 (no simple pole = no Lie bracket on J-line)

    Therefore the cubic shadow on the J-line is ZERO:
      Sh_3^J = 0

    and hence all higher shadows vanish by the master equation cascade:
      Sh_r^J = 0 for r >= 3.

    The J-line has shadow depth 2 (class G, Gaussian).

    SUBTLETY: The JG+, JG-, JT couplings create off-diagonal shadow data.
    These enter the MULTI-VARIABLE shadow obstruction tower (the full 4d deformation space
    of BP), not the pure J-line restriction.
    """
    if max_r < 2:
        return {}

    k_res = k + Rational(1, 2)
    tower = {2: k_res}  # AP39: kappa(H_{k_res}) = k_res

    for r in range(3, max_r + 1):
        tower[r] = Rational(0)

    return tower


# =============================================================================
# 9. BP shadow auxiliary data
# =============================================================================

def bp_5c_plus_22(level=None):
    """Evaluate 5c_BP + 22, the Virasoro Kac factor at c = c_BP(k).

    This controls the denominator of the quartic and all higher shadows.
    """
    c_bp = bp_central_charge(level)
    return factor(cancel(5 * c_bp + 22))


def bp_quartic_on_tline(level=None):
    """Quartic shadow Q_BP on the T-line: Q = 10/[c_BP*(5c_BP + 22)].

    This is the Virasoro quartic evaluated at c = c_BP(k).
    """
    c_bp = bp_central_charge(level)
    return factor(cancel(Rational(10) / (c_bp * (5 * c_bp + 22))))


def bp_discriminant_on_tline(level=None):
    """Critical discriminant Delta_BP on T-line: Delta = 8*kappa*Q.

    Delta = 8*(c/2)*Q = 4cQ = 40/(5c+22) evaluated at c = c_BP(k).
    """
    c_bp = bp_central_charge(level)
    return factor(cancel(Rational(40) / (5 * c_bp + 22)))


# =============================================================================
# 10. Principal vs minimal DS comparison
# =============================================================================

def principal_vs_minimal_ds_comparison(level=None):
    """Compare principal DS (sl_3 -> W_3) vs minimal DS (sl_3 -> BP) of sl_3.

    Both reductions start from sl_3 at level k but use different nilpotent
    elements: f_principal vs f_minimal.

    Returns a dict comparing the two reductions at each shadow level.
    """
    if level is None:
        level = k

    c_w3 = principal_ds_central_charge(3, level)
    c_bp = bp_central_charge(level)

    c_w3_factored = factor(cancel(c_w3))
    c_bp_factored = factor(cancel(c_bp))

    # Ghost central charges
    c_sl3 = 8 * level / (level + 3)
    c_ghost_principal = cancel(c_sl3 - c_w3)
    c_ghost_minimal = cancel(c_sl3 - c_bp)

    # Kappa values on T-line
    kappa_w3 = cancel(c_w3 / 2)  # T-line kappa: Virasoro channel only = c/2
    kappa_bp = cancel(c_bp / 2)

    # Quartic on T-line
    Q_w3 = cancel(Rational(10) / (c_w3 * (5 * c_w3 + 22)))
    Q_bp = cancel(Rational(10) / (c_bp * (5 * c_bp + 22)))

    # Koszul conductors
    K_w3 = 100  # Known: K_{W_3} = 100
    K_bp = 196  # From complementarity c_BP(k) + c_BP(-k-6) = 196

    # Dual levels
    k_dual_w3 = cancel(-(4 * 3 + 1) * level - 2 * 3 * (2 * 3 + 1))
    k_dual_w3 = cancel(k_dual_w3 / (4 * level + (4 * 3 + 1)))
    k_dual_bp = bp_dual_level(level)

    return {
        'c_W3': c_w3_factored,
        'c_BP': c_bp_factored,
        'c_sl3_sugawara': factor(cancel(c_sl3)),
        'c_ghost_principal': factor(c_ghost_principal),
        'c_ghost_minimal': factor(c_ghost_minimal),
        'kappa_W3_T': factor(kappa_w3),
        'kappa_BP_T': factor(kappa_bp),
        'kappa_BP_J': bershadsky_polyakov_kappa_j(level),
        'Q_W3_T': factor(Q_w3),
        'Q_BP_T': factor(Q_bp),
        'K_W3': K_w3,
        'K_BP': K_bp,
        'k_dual_W3': factor(cancel(k_dual_w3)),
        'k_dual_BP': factor(cancel(k_dual_bp)),
        'W3_depth': 'infinity (class M)',
        'BP_T_depth': 'infinity (class M)',
        'BP_J_depth': '2 (class G)',
        'BP_generators': 'J (wt 1), G+ (wt 3/2), G- (wt 3/2), T (wt 2)',
        'W3_generators': 'T (wt 2), W (wt 3)',
    }


# =============================================================================
# 11. Ghost contribution analysis
# =============================================================================

def ghost_central_charge_principal(n, level=None):
    """Ghost central charge for principal DS of sl_N: c_ghosts = c_sl_N - c_W_N.

    For sl_N: c_{sl_N}(k) = (N^2-1)k/(k+N), c_{W_N}(k) = (N-1)(1-N(N+1)/(k+N)).
    """
    if level is None:
        level = k
    dim_g = n * n - 1
    h_v = n
    c_sl = dim_g * level / (level + h_v)
    c_wn = principal_ds_central_charge(n, level)
    return cancel(c_sl - c_wn)


def ghost_central_charge_level_independence(max_N=6):
    """Verify: ghost central charge is level-independent for principal DS.

    The ghost central charge c_{ghosts} = c_{sl_N} - c_{W_N} turns out to
    be a CONSTANT (independent of the level k) for the principal DS reduction.
    This is a nontrivial identity reflecting the conformal weight structure
    of the bc ghost systems.

    Returns dict {N: c_ghosts} showing the constant values.
    """
    from sympy import diff as sym_diff

    results = {}
    for n in range(2, max_N + 1):
        c_ghost = ghost_central_charge_principal(n)
        is_constant = simplify(sym_diff(c_ghost, k)) == 0
        results[n] = {
            'c_ghosts': factor(c_ghost),
            'level_independent': is_constant,
        }
    return results


def ghost_central_charge_bp(level=None):
    """Ghost central charge for BP (minimal DS of sl_3): c_{sl_3} - c_BP.

    Unlike the principal case, this is NOT level-independent.
    """
    if level is None:
        level = k
    c_sl3 = 8 * level / (level + 3)
    c_bp = bp_central_charge(level)
    return cancel(c_sl3 - c_bp)


# =============================================================================
# 12. Feigin-Frenkel dual level verification
# =============================================================================

def ff_involution_check_principal(n, level=None):
    """Verify (k')' = k for the principal FF dual level.

    For W_N: k' = -(alpha*k + beta)/(4k + alpha) where alpha = 4N+1, beta = 2N(2N+1).
    """
    if level is None:
        level = k
    alpha = 4 * n + 1
    beta = 2 * n * (2 * n + 1)
    k_dual = -(alpha * level + beta) / (4 * level + alpha)
    k_double_dual = -(alpha * k_dual + beta) / (4 * k_dual + alpha)
    return simplify(k_double_dual - level) == 0


def ff_involution_check_bp(level=None):
    """Verify (k')' = k for the BP dual level k' = -k - 6."""
    if level is None:
        level = k
    k_dual = bp_dual_level(level)
    k_double_dual = bp_dual_level(k_dual)
    return simplify(k_double_dual - level) == 0


def ff_complementarity_check_bp(level=None):
    """Verify c_BP(k) + c_BP(k') = K_BP = 196.

    BP formula: c = 2 - 24(k+1)^2/(k+3), K=196 (FKR 2020, verified k=-3/2 -> c=-2)
    """
    if level is None:
        level = k
    c1 = bp_central_charge(level)
    c2 = bp_central_charge(bp_dual_level(level))
    return {
        'c_sum': simplify(c1 + c2),
        'K_BP': 196,
        'complementary': simplify(c1 + c2 - 196) == 0,
    }


# =============================================================================
# 13. Higher-arity quintic and beyond: explicit check of nonvanishing
# =============================================================================

def verify_quintic_nonvanishing(n):
    """Verify Sh_5^{W_N}(k) != 0 at generic k, confirming depth > 4.

    The quintic is the first shadow CREATED by the quartic seed.
    It is generated by the master equation from {C, Q}_H.
    """
    tower = principal_ds_shadow_tower(n, max_r=5)
    Sh5 = tower[5]

    # Check at a specific generic level (k=7 for W_2, k=10 for W_3)
    test_level = 10 if n >= 3 else 7
    val = Sh5.subs(k, test_level)

    return {
        'Sh_5': Sh5,
        'Sh_5_at_test': val,
        'nonzero': val != 0,
        'test_level': test_level,
    }


def shadow_nonvanishing_table(n, max_r=8):
    """Table showing Sh_r^{W_N}(k) != 0 at arities 2..max_r.

    Confirms that the shadow obstruction tower is infinite (class M) for W_N.
    """
    tower = principal_ds_shadow_tower(n, max_r)
    test_level = 10 if n >= 3 else 7

    results = {}
    for r in range(2, max_r + 1):
        val = tower[r].subs(k, test_level)
        results[r] = {
            'Sh_r': tower[r],
            'value_at_test': val,
            'nonzero': val != 0,
        }
    return results


# =============================================================================
# 14. BP multi-line shadow structure
# =============================================================================

def bp_shadow_structure_summary(level=None):
    """Summary of the BP shadow structure on all generator lines.

    The BP algebra has a 4-dimensional deformation space:
      {J (wt 1), G+ (wt 3/2), G- (wt 3/2), T (wt 2)}

    By Z_2 charge conservation (G+ <-> G- symmetry), the shadow obstruction tower
    splits into sectors:
      - T-line (charge 0, bosonic): Virasoro tower at c_BP(k), depth infinity
      - J-line (charge 0, bosonic): U(1) tower, depth 2 (Gaussian)
      - G-lines (charge +/- 1, fermionic): odd-weight shadows only
      - JT-mixed (charge 0): off-diagonal corrections starting at arity 4
      - JG-mixed (charge +/- 1): from J_{(0)}G = (1/2)G coupling
      - TG-mixed (charge +/- 1): from T_{(0)}G = (3/2)G coupling

    On each pure bosonic line, the tower is computable from the OPE data.
    The fermionic lines have additional sign subtleties.
    """
    if level is None:
        level = k

    c_bp = bp_central_charge(level)
    k_res = bp_residual_level(level)

    return {
        'T_line': {
            'depth': 'infinity',
            'class': 'M',
            'kappa': cancel(c_bp / 2),
            'cubic': Rational(2),  # Virasoro cubic
            'quartic': factor(cancel(Rational(10) / (c_bp * (5 * c_bp + 22)))),
        },
        'J_line': {
            'depth': 2,
            'class': 'G',
            'kappa': k_res,  # AP39: kappa(H_{k_res}) = k_res
            'cubic': Rational(0),
            'quartic': Rational(0),
        },
        'G_lines': {
            'depth': 'needs computation',
            'note': 'Fermionic, odd-weight shadows; charge +/- 1',
        },
        'JT_mixed': {
            'coupling': 'J_{(0)}T = partial_T (derivative)',
            'note': 'Off-diagonal contribution from J-T interaction',
        },
        'generators': {
            'J': {'weight': 1, 'charge': 0, 'statistics': 'bosonic'},
            'G+': {'weight': Rational(3, 2), 'charge': 1, 'statistics': 'fermionic'},
            'G-': {'weight': Rational(3, 2), 'charge': -1, 'statistics': 'fermionic'},
            'T': {'weight': 2, 'charge': 0, 'statistics': 'bosonic'},
        },
    }


# =============================================================================
# 15. Depth classification table
# =============================================================================

def ds_depth_classification():
    """Complete depth classification: input algebras vs DS outputs.

    FINITE DEPTH inputs:
      sl_N: depth 3 (class L) for ALL N
      Heisenberg: depth 2 (class G)
      Lattice: depth 2 (class G)
      Beta-gamma: depth 4 (class C)

    INFINITE DEPTH outputs from DS:
      W_2 = Virasoro: depth infinity (class M) from sl_2
      W_3: depth infinity (class M) from sl_3
      W_N for N >= 2: depth infinity (class M) from sl_N

    NON-PRINCIPAL outputs:
      BP = W^k(sl_3, f_min): depth infinity on T-line, depth 2 on J-line

    The depth ALWAYS increases under principal DS (from 3 to infinity).
    The depth ALWAYS increases on the T-line under non-principal DS too.
    """
    return {
        'inputs': {
            'sl_2': {'depth': 3, 'class': 'L'},
            'sl_3': {'depth': 3, 'class': 'L'},
            'sl_N': {'depth': 3, 'class': 'L'},
        },
        'principal_outputs': {
            'W_2 (Vir)': {'depth': 'infinity', 'class': 'M'},
            'W_3': {'depth': 'infinity', 'class': 'M'},
            'W_N': {'depth': 'infinity', 'class': 'M'},
        },
        'nonprincipal_outputs': {
            'BP (T-line)': {'depth': 'infinity', 'class': 'M'},
            'BP (J-line)': {'depth': 2, 'class': 'G'},
        },
        'depth_increase_universal': True,
        'mechanism': 'Ghost sector creates quartic seed; master equation propagates',
    }


if __name__ == '__main__':
    print("=" * 70)
    print("DS Shadow Functor: Higher Arities and Bershadsky-Polyakov")
    print("=" * 70)

    print("\n--- Principal DS tower for Virasoro (N=2), arities 2-8 ---")
    vir_tower = principal_ds_shadow_tower(2, max_r=8)
    for r in sorted(vir_tower.keys()):
        print(f"  Sh_{r}(Vir, k) = {vir_tower[r]}")

    print("\n--- Principal DS tower for W_3 (N=3), arities 2-8 ---")
    w3_tower = principal_ds_shadow_tower(3, max_r=8)
    for r in sorted(w3_tower.keys()):
        print(f"  Sh_{r}(W_3, k) = {w3_tower[r]}")

    print("\n--- Depth increase mechanism for N=3 ---")
    mech = ds_depth_increase_mechanism(3)
    print(f"  c_W3(k) = {mech['c_WN']}")
    print(f"  Q_4 (quartic seed) = {mech['Q_quartic_seed']}")
    print(f"  Sh_5 (from seed) = {mech['Sh5_from_seed']}")

    print("\n--- BP central charge ---")
    print(f"  c_BP(k) = {factor(bp_central_charge())}")
    print(f"  c_BP(1) = {bp_central_charge(1)}")

    print("\n--- BP shadow obstruction tower on T-line ---")
    bp_tower = bershadsky_polyakov_shadow_tower(6)
    for r in sorted(bp_tower.keys()):
        print(f"  Sh_{r}(BP, T-line, k) = {bp_tower[r]}")

    print("\n--- BP shadow obstruction tower on J-line ---")
    j_tower = bershadsky_polyakov_j_line(4)
    for r in sorted(j_tower.keys()):
        print(f"  Sh_{r}(BP, J-line, k) = {j_tower[r]}")

    print("\n--- Principal vs minimal DS comparison ---")
    comp = principal_vs_minimal_ds_comparison()
    for key, val in comp.items():
        print(f"  {key}: {val}")

    print("\n--- Depth comparison table ---")
    depth_table = ds_shadow_depth_comparison(6)
    for n, data in depth_table.items():
        print(f"  N={n}: sl_{n} depth={data['sl_N_depth']}, "
              f"W_{n} depth={data['W_N_depth']}, "
              f"Q_4 nonzero={data['Q_4_nonzero']}")
