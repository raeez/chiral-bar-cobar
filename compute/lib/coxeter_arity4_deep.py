"""Deep arity-4 shadow analysis for multi-generator chiral algebras.

The shadow depth classification divides chiral algebras into four classes:
  G (Gaussian, r_max=2): Heisenberg
  L (Lie/tree, r_max=3): affine Kac-Moody V_k(g) at generic k
  C (contact/quartic, r_max=4): beta-gamma
  M (mixed, r_max=infinity): Virasoro, W_N

OPEN QUESTION (conj:operadic-complexity-detailed):
  r_max(A) = A-infinity depth of A = L-infinity formality level.

This module addresses the KEY UNRESOLVED CASE: what is r_max(W_3)?
W_3 has two strong generators T (weight 2, Virasoro) and W (weight 3).
The W-W OPE contains the composite Lambda = :TT: - (3/10) d^2 T,
making the arity-4 analysis qualitatively different from single-generator
algebras.

The multi-variable shadow tower for a rank-r algebra lives on the
deformation space H^2_cyc of dimension r. For W_3:
  - T-direction deformation: x_T (weight-2 curvature)
  - W-direction deformation: x_W (weight-3 curvature)
  - Kappa matrix: diag(c/2, c/3) (no mixing by weight)

The shadow at arity n is a degree-n polynomial in (x_T, x_W).

COMPUTATION PLAN:
  1. kappa values and the 2x2 kappa matrix for W_3
  2. Multi-variable shadow recursion through arity 4
  3. Comparison: W_3 shadow vs Virasoro shadow (the Coxeter anomaly Delta S_r)
  4. DS reduction: V_k(sl_3) -> W_3 compatibility at the kappa level
  5. Shadow depth determination for W_3

Ground truth:
  - w3_bar.py: W_3 OPE data
  - virasoro_shadow_tower.py: Virasoro tower through arity 7
  - modular_shadow_tower.py: all-arity master equation
  - nonlinear_modular_shadows.tex: thm:nms-all-arity-master-equation

References:
  - thm:shadow-archetype-classification
  - conj:operadic-complexity-detailed
  - prop:shadow-formality-low-arity
"""

from __future__ import annotations

from typing import Dict, Tuple

from sympy import (
    Symbol, Rational, simplify, factor, expand, sqrt, Matrix, symbols,
    Poly, S, diff
)


# =============================================================================
# Symbolic variables
# =============================================================================

c = Symbol('c')
k = Symbol('k')
x_T = Symbol('x_T')
x_W = Symbol('x_W')
x = Symbol('x')


# =============================================================================
# 1. Kappa values for all standard families
# =============================================================================

def kappa_heisenberg():
    """kappa(Heis) = 1. Single generator of weight 1, two-point = 1."""
    return S.One


def kappa_virasoro():
    """kappa(Vir_c) = c/2. Single generator T, two-point T_(3)T = c/2."""
    return c / 2


def kappa_betagamma():
    """kappa(beta-gamma) = 1. Two generators b (wt 1), c (wt 0), cross-pairing.

    The beta-gamma system has kappa_{bc} = 1 (off-diagonal), kappa_{bb} = kappa_{cc} = 0.
    On the 1d primary line (diagonal deformation): kappa = 1.
    """
    return S.One


def kappa_affine(g_dim, h_dual, level=None):
    """kappa(V_k(g)) = dim(g) * (k + h^v) / (2 * h^v).

    For the vacuum module of the affine Kac-Moody algebra at level k.
    The curvature is kappa = dim(g) * (k + h^v) / (2 * h^v).

    For sl_N: dim = N^2-1, h^v = N.
    """
    if level is None:
        level = k
    return Rational(g_dim) * (level + h_dual) / (2 * h_dual)


def kappa_affine_sl(N, level=None):
    """kappa(V_k(sl_N)) = (N^2-1) * (k+N) / (2N)."""
    return kappa_affine(N**2 - 1, N, level)


def kappa_w3():
    """kappa(W_3) as a 2x2 matrix on the (T, W) deformation space.

    kappa_TT = c/2  (from T_(3)T = c/2)
    kappa_WW = c/3  (from W_(5)W = c/3)
    kappa_TW = 0    (T has weight 2, W has weight 3 — no two-point mixing)

    The total scalar kappa (trace) is c/2 + c/3 = 5c/6.
    """
    return Matrix([
        [c / 2, 0],
        [0, c / 3],
    ])


def kappa_w3_scalar():
    """Scalar kappa for W_3: tr(kappa) = c/2 + c/3 = 5c/6."""
    return Rational(5) * c / 6


def kappa_wN(N):
    """Scalar kappa for W_N: sum over generators of their two-point coefficients.

    W_N has generators of spins 2, 3, ..., N.
    In Zamolodchikov normalization, the spin-s generator has two-point
    coefficient c/s (the leading pole W_s_{(2s-1)}W_s = c/s).

    Ground truth:
      s=2: T_{(3)}T = c/2  (Virasoro, w3_bar.py)
      s=3: W_{(5)}W = c/3  (W_3, w3_bar.py)
      s=4: W4_{(7)}W4 = c/4  (W_4, w4_bar.py)

    So kappa(W_N) = c * sum_{s=2}^{N} 1/s = c * (H_N - 1).
      W_2 = Virasoro: c/2.
      W_3: c/2 + c/3 = 5c/6.
      W_4: c/2 + c/3 + c/4 = 13c/12.
    """
    total = S.Zero
    for s in range(2, N + 1):
        total += Rational(1, s)
    return c * total


# =============================================================================
# 2. W_3 central charge from DS reduction
# =============================================================================

def w3_central_charge(level=None):
    """c_{W_3}(k) = 2 - 24(k+2)^2 / (k+3).

    DS reduction of sl_3 at level k. Critical level: k = -3.
    """
    if level is None:
        level = k
    return 2 - 24 * (level + 2)**2 / (level + 3)


def w3_complementarity():
    """c(k) + c(-k-6) = 100. The W_3 complementarity sum.

    General formula for W_N: c + c' = 2*rank + 4*h^v*dim.
    For sl_3: rank=2, h^v=3, dim=8 -> 2*2 + 4*3*8 = 100.
    """
    return 100


def ds_kappa_check(level=None):
    """Check DS reduction compatibility: kappa(V_k(sl_3)) -> kappa(W_3).

    Under DS at principal nilpotent:
      V_k(sl_3) with kappa = 8*(k+3)/6 = 4(k+3)/3
    maps to:
      W_3 with kappa = 5*c(k)/6 where c(k) = 2 - 24(k+2)^2/(k+3)

    The DS reduction does NOT preserve kappa literally (the generators change).
    What it preserves is the BAR COMPLEX structure. The kappa of the quotient
    W_3 = DS(V_k(sl_3)) is determined by the W_3 OPE, not by the original sl_3.

    Returns (kappa_sl3, kappa_w3, ratio) for comparison.
    """
    if level is None:
        level = k
    k_sl3 = kappa_affine_sl(3, level)
    c_val = w3_central_charge(level)
    k_w3 = Rational(5) * c_val / 6
    ratio = simplify(k_w3 / k_sl3)
    return k_sl3, k_w3, ratio


# =============================================================================
# 3. Multi-variable shadow tower for W_3
# =============================================================================

def w3_propagator_matrix():
    """Inverse kappa matrix for W_3: P = kappa^{-1}.

    P = diag(2/c, 3/c).
    """
    return Matrix([
        [2 / c, 0],
        [0, 3 / c],
    ])


def w3_shadow_arity2():
    """Arity-2 shadow for W_3: Sh_2 = kappa_{TT} x_T^2 + kappa_{WW} x_W^2.

    This is the curvature as a quadratic form on the deformation space.
    """
    return (c / 2) * x_T**2 + (c / 3) * x_W**2


def w3_shadow_arity3():
    """Arity-3 shadow for W_3.

    The cubic shadow encodes the structure constants of the OPE at arity 3.

    T-T-T channel: C_TTT = 2 (from T_(1)T = 2T, same as Virasoro)
    T-T-W channel: C_TTW = 0 (weight mismatch: 2+2+3=7, need even for T-sector)
    T-W-W channel: C_TWW = 0 (weight 2+3+3=8... actually need to check)
    W-W-W channel: C_WWW = 0 (no weight-3 state from W_(2)W = dT, weight 3,
                                but this is a T-descendant, not a W-primary)

    ACTUALLY: The cubic shadow involves the three-point OPE couplings.
    For the shadow tower, the relevant coupling at arity 3 is:
      C_{ijk} = <phi_i, phi_j_(1) phi_k>  (structure constant)

    For W_3 generators phi_1 = T (wt 2), phi_2 = W (wt 3):
      C_{TTT} = <T, T_(1)T> = <T, 2T> = 2 * (c/2) = c
        Wait — the shadow cubic coefficient is C = m_j(phi_i, phi_k)/kappa_{jj},
        NOT the raw OPE coefficient.

    On the PRIMARY LINE (x_T = x, x_W = 0, pure T-sector):
      Sh_3|_{x_W=0} = 2 x_T^3  (same as Virasoro)

    On the W-primary line (x_T = 0, x_W = x):
      Sh_3|_{x_T=0} = C_W x_W^3
      where C_W encodes the cubic coupling in the W-sector.

    The W-W OPE at n=3 gives W_(3)W = 2T (a T-mode, not a W-mode).
    So the W-W collision produces a T-intermediate, giving a MIXED term
    C_TW^2 x_T x_W^2 rather than a pure C_W x_W^3 term.

    Structure: Sh_3 = C_{TTT} x_T^3 + C_{T,WW} x_T x_W^2
    (terms with odd W-count vanish by W-charge conservation, since W has
    odd spin and the shadow is a genus-0 invariant).

    C_{TTT} = 2 (Virasoro gravitational cubic)
    C_{T,WW} = coefficient from W_(3)W = 2T contracted with T-propagator

    The sewing contribution: two W-insertions collide, produce T via W_(3)W = 2T,
    and the T propagates with P_T = 2/c. The coefficient:
      C_{T,WW} = 2 * (2/c) * (c/3) * 2  ... no, let me be more careful.

    The cubic shadow on the multi-variable space:
      Sh_3(x_T, x_W) = sum_{i,j,k} C_{ijk} x_i x_j x_k / (3!)
    where C_{ijk} is the fully symmetric tensor from the OPE structure constants
    normalized by the inverse kappa.

    For the shadow tower master equation on the multi-variable space:
      Sh_3 = -nabla_H^{-1}(o^(3))
    where o^(3) is the cubic obstruction. Since kappa is diagonal and there is
    no lower-order shadow beyond kappa itself, the cubic shadow is:
      C_{ijk} = (raw coupling m_{ijk}) / (2 * 3)  ... this requires the full
    genus-0 three-point function, which is determined by the OPE.

    For the SCALAR (1d) reduction on the total primary line
    (x_T = a*t, x_W = b*t with a^2 + b^2 = 1):
      Sh_3(t) = [C_{TTT} a^3 + 3 C_{T,WW} a b^2] t^3

    Computing C_{T,WW}:
    The three-point coupling <T; W, W>_3 involves W_(3)W = 2T.
    Normalize: C_{T,WW} = <T, W_(3)W> / kappa_{TT} = 2*(c/2)/(c/2) = 2.
    Wait: <T, W_(3)W> = <T, 2T> = 2 * kappa_{TT} = 2 * c/2 = c.
    Then C_{T,WW} = c / kappa_{TT} = c / (c/2) = 2.

    Hmm, this is too simple. The shadow cubic as a symmetric 3-tensor:
    T-T-T: coefficient 2 (from T_(1)T = 2T, Virasoro)
    T-W-W: coefficient from the SEWING interpretation of the three-point
            function. The raw three-point coupling in the shadow formalism
            is: T is produced by W_(3)W = 2T. The cubic shadow coefficient is:
              (number of ways to assign) * (OPE coefficient) / normalization
            = 2 (the coefficient of T in W_(3)W)

    CORRECTION (2026-03-19): The cubic coefficient of x_T x_W^2 is d_W = 3,
    NOT 2. The correct derivation uses the n=1 product (Lie bracket):
      T_(1)W = d_W * W = 3W  (Virasoro primary condition, weight 3)
      C_{TWW} = kappa(W, T_(1)W) / kappa_{WW} = kappa(W, 3W)/(c/3) = c/(c/3) = 3
    See thm:w-universal-gravitational-cubic in w_algebras.tex.
    The coefficient 2 from W_(3)W = 2T is a different OPE product (n=3 not n=1).
    """
    # On the pure T-line: 2 x_T^3 (Virasoro cubic)
    # The T-W-W coupling from thm:w-universal-gravitational-cubic: coefficient d_W = 3
    # By W-charge conservation: terms with odd powers of x_W vanish
    return 2 * x_T**3 + 3 * x_T * x_W**2


def w3_shadow_arity3_coefficients():
    """Return the cubic shadow coefficients as a dict.

    Keys: (i,j,k) where i,j,k in {T, W}.
    Values: coefficient of x_i x_j x_k in Sh_3 (with symmetry).
    """
    return {
        ('T', 'T', 'T'): 2,     # Virasoro gravitational cubic
        ('T', 'W', 'W'): 3,     # from T_(1)W = 3W (thm:w-universal-gravitational-cubic)
        ('T', 'T', 'W'): 0,     # weight mismatch (odd W-count)
        ('W', 'W', 'W'): 0,     # W-charge conservation
    }


def _h_poisson_bracket_2d(f, g, kappa_inv):
    """H-Poisson bracket on the 2d deformation space (x_T, x_W).

    {f, g}_H = sum_{i,j} (df/dx_i) P_{ij} (dg/dx_j)

    For diagonal P = diag(P_TT, P_WW):
    {f, g}_H = (df/dx_T) P_TT (dg/dx_T) + (df/dx_W) P_WW (dg/dx_W)
    """
    P_TT = kappa_inv[0, 0]
    P_WW = kappa_inv[1, 1]
    result = diff(f, x_T) * P_TT * diff(g, x_T) + diff(f, x_W) * P_WW * diff(g, x_W)
    return expand(result)


def _invert_nabla_H_2d(obstruction, degree, kappa_mat):
    """Solve nabla_H(Sh) = -obstruction for a degree-d polynomial in (x_T, x_W).

    nabla_H(f) = {kappa, f}_H where kappa = Sh_2.
    For a monomial x_T^a x_W^b with a+b = degree:
      nabla_H(x_T^a x_W^b) = (a * kappa_TT * P_TT * a + b * kappa_WW * P_WW * b) x_T^a x_W^b
                             = (a^2 * 1 + b^2 * 1) x_T^a x_W^b  ... no

    Actually: nabla_H(f) = {Sh_2, f}_H
    = (d Sh_2/dx_T)(P_TT)(df/dx_T) + (d Sh_2/dx_W)(P_WW)(df/dx_W)
    = c * x_T * (2/c) * df/dx_T + (2c/3) * x_W * (3/c) * df/dx_W
    = 2 x_T df/dx_T + 2 x_W df/dx_W
    = 2 * E(f)
    where E = x_T d/dx_T + x_W d/dx_W is the Euler operator.

    For a degree-d homogeneous polynomial: E(f) = d * f.
    So nabla_H(f) = 2d * f for any degree-d homogeneous polynomial.

    Hence nabla_H^{-1}(g) = g / (2d).
    """
    return -obstruction / (2 * degree)


def w3_shadow_tower(max_arity=5):
    """Compute the W_3 shadow tower on the 2d deformation space (x_T, x_W).

    Returns dict {r: Sh_r} where Sh_r is a polynomial in (x_T, x_W).

    Sh_2, Sh_3, Sh_4 are OPE INPUTS determined by the quasi-primary exchange
    mechanism (Lambda-exchange for the quartic). They are NOT generated by the
    master equation. The master equation nabla_H(Sh_r) + o^(r) = 0 generates
    Sh_r for r >= 5 only, by sewing lower-arity shadows.

    Sh_2 = kappa (curvature quadratic form).
    Sh_3 = cubic shadow from T_(1)T = 2T and W_(3)W = 2T OPE data.
    Sh_4 = quartic shadow from Lambda-exchange: Q^contact = 10/[c(5c+22)]
           on the T-line, with alpha = 16/(5c+22) controlling the W-mixing.
    """
    kappa_mat = kappa_w3()
    kappa_inv = w3_propagator_matrix()

    shadows = {}
    shadows[2] = w3_shadow_arity2()
    shadows[3] = w3_shadow_arity3()

    # Arity-4: Lambda-exchange INPUT (not from master equation)
    alpha = Rational(16) / (5 * c + 22)
    N_Lambda = c * (5 * c + 22) / 10
    Q_TTTT = Rational(10) / (c * (5 * c + 22))
    Q_TTWW = 10 * alpha / (c * (5 * c + 22))
    Q_WWWW = 10 * alpha**2 / (c * (5 * c + 22))
    shadows[4] = Q_TTTT * x_T**4 + 6 * Q_TTWW * x_T**2 * x_W**2 + Q_WWWW * x_W**4

    for r in range(5, max_arity + 1):
        obstruction = S.Zero

        for j in range(2, r + 1):
            k_val = r + 2 - j
            if k_val < 2 or k_val not in shadows:
                continue
            if j > k_val:
                continue

            bracket = _h_poisson_bracket_2d(shadows[j], shadows[k_val], kappa_inv)

            if j == k_val:
                obstruction += Rational(1, 2) * bracket
            else:
                obstruction += bracket

        obstruction = expand(obstruction)

        Sh_r = _invert_nabla_H_2d(obstruction, r, kappa_mat)
        Sh_r = expand(Sh_r)

        shadows[r] = Sh_r

    return shadows


def w3_shadow_coefficients(max_arity=5):
    """Extract shadow coefficients as polynomials in c.

    Returns dict {r: dict of {monomial_string: coefficient}}.
    """
    shadows = w3_shadow_tower(max_arity)
    result = {}

    for r, sh in shadows.items():
        p = Poly(sh, x_T, x_W)
        coeffs = {}
        for monom, coeff in p.as_dict().items():
            a, b = monom
            key = f"x_T^{a}*x_W^{b}" if b > 0 else f"x_T^{a}"
            if a == 0:
                key = f"x_W^{b}"
            coeffs[key] = factor(coeff)
        result[r] = coeffs

    return result


# =============================================================================
# 4. W_3 vs Virasoro shadow comparison (Coxeter anomaly)
# =============================================================================

def coxeter_anomaly(max_arity=5):
    """Compute Delta S_r(W_3) = S_r(W_3)|_{x_W=0} - S_r(Vir_c).

    On the pure T-line (x_W = 0), the W_3 shadow should reduce to the
    Virasoro shadow if the W-generator completely decouples. Any deviation
    is the Coxeter anomaly: the backreaction of the W-generator on the
    T-sector shadow.

    Returns dict {r: (w3_on_T_line, vir_shadow, difference)}.
    """
    w3_shadows = w3_shadow_tower(max_arity)

    # Virasoro shadows on the 1d primary line (from virasoro_shadow_tower.py)
    from virasoro_shadow_tower import compute_shadow_tower as vir_tower
    vir_shadows = vir_tower(max_arity)

    result = {}
    for r in range(2, max_arity + 1):
        # W_3 shadow restricted to x_W = 0, x_T = x
        w3_T = expand(w3_shadows[r].subs(x_W, 0).subs(x_T, x))
        vir = expand(vir_shadows[r])
        diff_val = simplify(w3_T - vir)
        result[r] = (w3_T, vir, diff_val)

    return result


def w3_shadow_on_W_line(max_arity=5):
    """W_3 shadow restricted to the pure W-line (x_T = 0).

    On this line, only the W-sector contributes.
    Returns dict {r: shadow_on_W_line}.
    """
    shadows = w3_shadow_tower(max_arity)
    result = {}
    for r, sh in shadows.items():
        restricted = expand(sh.subs(x_T, 0))
        result[r] = restricted
    return result


# =============================================================================
# 5. Shadow depth classification
# =============================================================================

# The four classes with their known members
SHADOW_DEPTH_CLASSES = {
    'G': {
        'name': 'Gaussian',
        'r_max': 2,
        'members': ['Heisenberg', 'rank-N Heisenberg', 'lattice VOA (any lattice)'],
        'mechanism': 'Abelian OPE: all n-th products with n >= 2 vanish',
    },
    'L': {
        'name': 'Lie/tree',
        'r_max': 3,
        'members': ['V_k(g) at generic k (any simple g)', 'current algebras'],
        'mechanism': 'Quadratic OPE: bar complex is quadratic Koszul, cubic = tree level',
    },
    'C': {
        'name': 'contact/quartic',
        'r_max': 4,
        'members': ['beta-gamma', 'bc system'],
        'mechanism': 'First-order system: quartic contact from weight-changing line, terminates by rank-one abelian rigidity',
    },
    'M': {
        'name': 'mixed/infinite',
        'r_max': float('inf'),
        'members': ['Virasoro', 'W_N (N >= 3)', 'non-quadratic W-algebras'],
        'mechanism': 'Composite operators in OPE force infinite tower; quintic obstruction nonvanishing',
    },
}


def classify_shadow_depth(algebra_name):
    """Return the shadow depth class for a known algebra.

    Returns (class_letter, r_max, certainty) where certainty is
    'proved', 'conjectured', or 'open'.
    """
    classifications = {
        'Heisenberg': ('G', 2, 'proved'),
        'rank-N Heisenberg': ('G', 2, 'proved'),
        'lattice VOA': ('G', 2, 'proved'),
        'V_k(sl_2)': ('L', 3, 'proved'),
        'V_k(sl_3)': ('L', 3, 'proved'),
        'V_k(g) generic': ('L', 3, 'proved'),
        'beta-gamma': ('C', 4, 'proved'),
        'bc system': ('C', 4, 'proved'),
        'Virasoro': ('M', float('inf'), 'proved'),
        'W_3': ('M', float('inf'), 'conjectured'),  # THE OPEN QUESTION
        'W_N': ('M', float('inf'), 'conjectured'),
    }
    return classifications.get(algebra_name, (None, None, 'unknown'))


def w3_shadow_depth_evidence(max_arity=6):
    """Collect evidence for the shadow depth of W_3.

    Checks whether Sh_r vanishes at each arity on both the T-line and W-line.
    If Sh_r != 0 at any arity r, then r_max >= r.

    The key test: does Sh_5(W_3) vanish?
    - If yes: W_3 is class C (like beta-gamma, r_max = 4)
    - If no: W_3 is class M (like Virasoro, r_max = infinity)
    """
    shadows = w3_shadow_tower(max_arity)
    evidence = {}

    for r in range(2, max_arity + 1):
        sh = shadows[r]
        is_zero = simplify(sh) == 0
        # Check on T-line
        sh_T = simplify(sh.subs(x_W, 0))
        # Check on W-line
        sh_W = simplify(sh.subs(x_T, 0))

        evidence[r] = {
            'shadow': sh,
            'is_zero': is_zero,
            'T_line_zero': sh_T == 0,
            'W_line_zero': sh_W == 0,
        }

    # Determine class
    last_nonzero = 0
    for r in sorted(evidence.keys()):
        if not evidence[r]['is_zero']:
            last_nonzero = r

    if last_nonzero == max_arity:
        verdict = 'M (shadow tower has not terminated through arity {})'.format(max_arity)
    elif last_nonzero < max_arity:
        class_map = {2: 'G', 3: 'L', 4: 'C'}
        cl = class_map.get(last_nonzero, '?')
        verdict = '{} (shadow terminates at arity {})'.format(cl, last_nonzero)
    else:
        verdict = 'inconclusive'

    evidence['verdict'] = verdict
    return evidence


# =============================================================================
# 6. Affine sl_3 shadow tower (for DS comparison)
# =============================================================================

def sl3_kappa(level=None):
    """kappa(V_k(sl_3)) = 8*(k+3)/6 = 4(k+3)/3.

    sl_3: dim=8, h^v=3.
    """
    if level is None:
        level = k
    return Rational(8) * (level + 3) / 6


def sl3_cubic_shadow():
    """The cubic shadow for V_k(sl_3) involves the cubic Casimir of sl_3.

    For an affine Kac-Moody algebra V_k(g), the cubic shadow is:
      Sh_3 = (1/(k+h^v)) * sum_{a,b,c} f^{abc} x_a x_b x_c

    where f^{abc} are the structure constants.

    For sl_3: the cubic Casimir is the totally symmetric d-tensor
    d_{abc} (which exists because sl_3 has rank 2 and a nontrivial
    center of the universal enveloping algebra at degree 3).

    On the primary line (all x_a = x): this reduces to
      Sh_3 = C * x^3
    where C = (cubic Casimir trace) / (k + h^v).

    For the AFFINE case, the class L property says Sh_4 = 0.
    """
    # The cubic shadow coefficient on the 1d primary line
    # is related to the structure constants. For class L algebras,
    # the shadow tower terminates at arity 3: Sh_4 = Sh_5 = ... = 0.
    return {
        'class': 'L',
        'r_max': 3,
        'cubic_present': True,
        'quartic_vanishes': True,
        'reason': 'quadratic OPE => Koszul => tree-level termination at arity 3',
    }


# =============================================================================
# 7. Virasoro quintic obstruction (for comparison with W_3)
# =============================================================================

def virasoro_quintic_obstruction():
    """The quintic obstruction for Virasoro: o^(5) = {C, Q}_H.

    From thm:nms-virasoro-quintic-forced:
    o^(5) = {2x^3, Q_0 x^4}_H = (6x^2)(2/c)(4 Q_0 x^3)
           = 48 Q_0 / c * x^5

    where Q_0 = 10/[c(5c+22)].

    Since o^(5) != 0 (for c != 0, -22/5), the quintic shadow is forced:
    Sh_5 = -o^(5) / (2*5) = -48 Q_0 / (10c) * x^5 = -48/(10c^2(5c+22)) * x^5

    This proves Virasoro is class M.
    """
    Q0 = Rational(10) / (c * (5 * c + 22))
    o5 = 48 * Q0 / c
    Sh5_coeff = -o5 / 10
    return {
        'obstruction_coeff': factor(o5),
        'Sh5_coeff': factor(Sh5_coeff),
        'is_zero': False,
        'proves_class_M': True,
    }


# =============================================================================
# 8. W_3 quintic obstruction (the KEY computation)
# =============================================================================

def w3_quintic_analysis():
    """Analyze the W_3 quintic shadow in detail.

    The arity-5 obstruction for W_3 comes from {Sh_3, Sh_4}_H on the 2d
    deformation space. Both Sh_3 and Sh_4 are OPE inputs: Sh_3 from the
    cubic OPE couplings, Sh_4 from Lambda-exchange (Q^contact = 10/[c(5c+22)]).

    The master equation generates Sh_5 = -o^(5)/(2*5) where o^(5) = {Sh_3, Sh_4}_H.

    If the quintic obstruction has a nonvanishing component on the W-line
    (x_T = 0), this would confirm that the W-generator forces an infinite tower.
    """
    shadows = w3_shadow_tower(5)

    # Extract the quartic
    sh4 = shadows[4]

    # Extract the quintic
    sh5 = shadows[5]

    # Analyze on T-line and W-line
    sh5_T = simplify(sh5.subs(x_W, 0))
    sh5_W = simplify(sh5.subs(x_T, 0))

    # The mixed terms
    sh5_expanded = expand(sh5)

    return {
        'Sh_4': factor(sh4),
        'Sh_5': sh5_expanded,
        'Sh_5_on_T_line': sh5_T,
        'Sh_5_on_W_line': sh5_W,
        'Sh_5_vanishes': simplify(sh5) == 0,
        'W_line_nonzero': sh5_W != 0,
        'class_M_confirmed': simplify(sh5) != 0,
    }


# =============================================================================
# 9. Two-channel structure analysis
# =============================================================================

def w3_two_channel_decomposition(max_arity=5):
    """Decompose W_3 shadows into T-channel and W-channel contributions.

    For each arity r, write:
      Sh_r = sum_{a+b=r} S_{a,b} x_T^a x_W^b

    The T-channel is the pure x_T part (b=0).
    The W-channel is everything with b > 0.

    By W-charge conservation (Z_2 symmetry W -> -W), only even powers of x_W appear.
    """
    shadows = w3_shadow_tower(max_arity)
    decomposition = {}

    for r, sh in shadows.items():
        p = Poly(expand(sh), x_T, x_W)
        T_channel = S.Zero
        W_channel = S.Zero
        mixed = {}

        for monom, coeff in p.as_dict().items():
            a, b = monom
            if b == 0:
                T_channel += coeff * x_T**a
            else:
                W_channel += coeff * x_T**a * x_W**b
            mixed[(a, b)] = factor(coeff)

        decomposition[r] = {
            'T_channel': expand(T_channel),
            'W_channel': expand(W_channel),
            'monomials': mixed,
            'W_charge_even': all(b % 2 == 0 for (a, b) in mixed.keys()),
        }

    return decomposition


# =============================================================================
# 10. Summary and diagnostics
# =============================================================================

def full_diagnostic(max_arity=5):
    """Run all diagnostics and return a summary dict."""
    result = {}

    # Kappa values
    result['kappa_W3_matrix'] = kappa_w3()
    result['kappa_W3_scalar'] = kappa_w3_scalar()
    result['kappa_Vir'] = kappa_virasoro()
    result['kappa_sl3'] = sl3_kappa()

    # DS check
    k_sl3, k_w3, ratio = ds_kappa_check()
    result['ds_kappa_sl3'] = k_sl3
    result['ds_kappa_w3'] = k_w3
    result['ds_ratio'] = ratio

    # Shadow tower
    shadows = w3_shadow_tower(max_arity)
    result['shadows'] = {r: expand(sh) for r, sh in shadows.items()}

    # Depth evidence
    evidence = w3_shadow_depth_evidence(max_arity)
    result['depth_verdict'] = evidence['verdict']

    # Quintic analysis
    if max_arity >= 5:
        quintic = w3_quintic_analysis()
        result['quintic_vanishes'] = quintic['Sh_5_vanishes']
        result['class_M_confirmed'] = quintic['class_M_confirmed']

    return result


if __name__ == '__main__':
    print("=" * 70)
    print("COXETER ARITY-4 DEEP: W_3 SHADOW DEPTH ANALYSIS")
    print("=" * 70)

    diag = full_diagnostic(6)

    print("\n--- Kappa values ---")
    print(f"  W_3 matrix: {diag['kappa_W3_matrix']}")
    print(f"  W_3 scalar: {diag['kappa_W3_scalar']}")
    print(f"  Virasoro: {diag['kappa_Vir']}")
    print(f"  sl_3 affine: {diag['kappa_sl3']}")

    print("\n--- DS reduction kappa ---")
    print(f"  kappa(V_k(sl_3)): {diag['ds_kappa_sl3']}")
    print(f"  kappa(W_3): {diag['ds_kappa_w3']}")
    print(f"  ratio: {diag['ds_ratio']}")

    print("\n--- Shadow tower ---")
    for r in sorted(diag['shadows'].keys()):
        print(f"  Sh_{r}: {diag['shadows'][r]}")

    print(f"\n--- Depth verdict: {diag['depth_verdict']} ---")

    if 'quintic_vanishes' in diag:
        print(f"\n--- Quintic analysis ---")
        print(f"  Sh_5 vanishes: {diag['quintic_vanishes']}")
        print(f"  Class M confirmed: {diag['class_M_confirmed']}")

    print("\n--- Two-channel decomposition ---")
    decomp = w3_two_channel_decomposition(5)
    for r in sorted(decomp.keys()):
        d = decomp[r]
        print(f"  Arity {r}:")
        print(f"    T-channel: {d['T_channel']}")
        print(f"    W-channel: {d['W_channel']}")
        print(f"    W-charge even: {d['W_charge_even']}")
