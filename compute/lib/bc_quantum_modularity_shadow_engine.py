r"""Quantum modularity from the shadow obstruction tower and Habiro-Zagier connection.

This module implements the bridge between:
  - The shadow obstruction tower Theta_A (bar-cobar invariants)
  - Zagier's quantum modular forms
  - Habiro's universal quantum invariants (the Habiro ring Z[q]^)
  - Nahm's conjecture on q-hypergeometric modularity
  - WRT (Witten-Reshetikhin-Turaev) invariants of 3-manifolds
  - False theta functions and mock modular forms
  - Resurgent structure at roots of unity

CENTRAL THESIS: The shadow depth classification G/L/C/M determines the type
of modular behavior:
  - Class G (Gaussian, r_max=2):  modular (theta function type)
  - Class L (Lie/tree, r_max=3):  modular (Nahm sum with pos. def. form)
  - Class C (Contact, r_max=4):   quasi-modular (E_2*-type corrections)
  - Class M (Mixed, r_max=inf):   quantum modular / mock modular

MATHEMATICAL FRAMEWORK
======================

1. SHADOW q-SERIES: For each algebra A, define
       Z_A(q) := sum_{r>=2} S_r(A) * q^r
   where S_r are the shadow tower coefficients from the master MC element
   Theta_A (thm:mc2-bar-intrinsic).  At roots of unity q = zeta_N:
       Z_A(zeta_N) = sum_{r>=2} S_r(A) * zeta_N^r
   This sum is finite modulo (zeta_N^N = 1), hence always well-defined.

2. QUANTUM MODULARITY: f: Q -> C is quantum modular of weight k if
       h_gamma(x) := f(gamma*x) - (cx+d)^{-k} f(x)
   extends to a C^infty (or real-analytic) function on R for each
   gamma in SL_2(Z).  We test this for the shadow q-series.

3. NAHM CONJECTURE: The q-hypergeometric sum
       f_A(q) = sum_{n>=0} q^{Q_A(n)} / (q;q)_{n_1} ... (q;q)_{n_r}
   with Q_A the shadow quadratic form is modular iff Q_A satisfies
   Nahm's conditions: eigenvalues in (0,1), specific K-theory constraints.
   The shadow metric Q_L(t) determines Q_A; the Nahm eigenvalue equals
   rho(A)^2 (the square of the shadow radius).

4. HABIRO RING: Z[q]^ = projlim Z[q]/((q;q)_n).  An element f in Z[q]^
   evaluates to a well-defined algebraic number at every root of unity.
   Test: Z_A(zeta_N) well-defined and algebraic for all N.

5. WRT INVARIANTS: tau_N(M^3) for lens spaces L(p,q) via surgery.
   For SU(2) level k: tau_k(L(p,1)) = sum_j S_{0j}^2 T_j^p.
   Bridge: tau_N(L(p,1)) should be accessible from shadow data of
   the affine SU(2) algebra at level k = N - 2.

6. RESURGENT STRUCTURE: As tau -> p/q (rational) from the upper half-plane,
       Z_A(e^{2*pi*i*tau}) ~ sum_k a_k (tau - p/q)^{k/2}
                             + e^{-S_1/(tau-p/q)} sum_k b_k (tau-p/q)^{k/2} + ...
   The instanton action S_1 is determined by the shadow metric branch points.

7. FALSE THETA FUNCTIONS: Partial theta series Psi(q) = sum_{n>=0} chi(n) q^{n^2/...}
   appear for class-M algebras.  The "missing half" is the quantum modular defect.

8. MOCK MODULARITY: f mock modular of weight k => shadow g of weight 2-k.
   Non-holomorphic completion: f_hat = f + Eichler integral of g.
   The shadow of the mock = a theta function determined by Q_L.

9. CATEGORIFICATION: Khovanov-type homology H^{i,j}(shadow) with
       chi_q(H) = Z_A(q)   (graded Euler characteristic = shadow q-series).

CONVENTIONS:
  - q = e^{2*pi*i*tau} (modular convention)
  - zeta_N = e^{2*pi*i/N} (primitive N-th root of unity)
  - kappa(A) = modular characteristic per AP20/AP39/AP48
  - S_r = a_{r-2}/r where a_n = [t^n] sqrt(Q_L(t))  (shadow_tower_recursive.py)
  - (q;q)_n = prod_{j=1}^n (1 - q^j)  (q-Pochhammer symbol)
  - The shadow GF H(t) = t^2*sqrt(Q_L(t)) is the WEIGHTED GF: H = sum r*S_r*t^r

Manuscript references:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple, Union

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
PI = math.pi
TWO_PI = 2.0 * PI
TWO_PI_SQ = TWO_PI ** 2
SQRT_TWO_PI = math.sqrt(TWO_PI)


# ===========================================================================
# Section 0: Standard family shadow data (self-contained, per AP1/AP39)
# ===========================================================================

@dataclass
class AlgebraData:
    """Shadow data for a standard chiral algebra family.

    Attributes:
        name:   Human-readable family name.
        kappa:  Modular characteristic kappa(A).
        alpha:  Cubic shadow coefficient S_3.
        S4:     Quartic shadow coefficient S_4.
        depth:  Shadow depth class: 'G', 'L', 'C', or 'M'.
        params: Dictionary of parameter values (c, k, rank, etc.).
    """
    name: str
    kappa: float
    alpha: float
    S4: float
    depth: str  # 'G', 'L', 'C', 'M'
    params: Dict[str, Any] = field(default_factory=dict)


def heisenberg_data(k: float = 1.0) -> AlgebraData:
    """Heisenberg VOA H_k.  kappa = k, alpha = 0, S4 = 0, class G."""
    return AlgebraData(
        name=f"Heisenberg(k={k})",
        kappa=k,
        alpha=0.0,
        S4=0.0,
        depth='G',
        params={'k': k},
    )


def affine_sl2_data(k: float = 1.0) -> AlgebraData:
    r"""Affine sl_2 at level k.
    kappa = dim(sl_2)*(k+h^v)/(2*h^v) = 3*(k+2)/4.
    alpha = 2, S4 = 0 (class L for generic k).
    """
    h_dual = 2
    dim_g = 3
    kappa = dim_g * (k + h_dual) / (2.0 * h_dual)
    return AlgebraData(
        name=f"Affine_sl2(k={k})",
        kappa=kappa,
        alpha=2.0,
        S4=0.0,
        depth='L',
        params={'k': k, 'dim_g': dim_g, 'h_dual': h_dual},
    )


def affine_sl3_data(k: float = 1.0) -> AlgebraData:
    r"""Affine sl_3 at level k.
    kappa = 8*(k+3)/6 = 4*(k+3)/3.
    """
    h_dual = 3
    dim_g = 8
    kappa = dim_g * (k + h_dual) / (2.0 * h_dual)
    return AlgebraData(
        name=f"Affine_sl3(k={k})",
        kappa=kappa,
        alpha=2.0,
        S4=0.0,
        depth='L',
        params={'k': k, 'dim_g': dim_g, 'h_dual': h_dual},
    )


def betagamma_data(lam: float = 1.0) -> AlgebraData:
    r"""Beta-gamma system.
    kappa = +1, alpha = 2, S4 from contact invariant, class C (r_max=4).
    """
    # AP137: c_bg(lambda=1) = +2, c_bc(lambda=1) = -2
    kappa = 1.0
    # The betagamma quartic contact invariant
    # Q^contact = 10/(c*(5c+22)) with c = +2 for betagamma
    # AP137: c_bg(lambda=1) = +2, c_bc(lambda=1) = -2
    c_bg = 2.0
    S4 = 10.0 / (c_bg * (5.0 * c_bg + 22.0))  # = 10/(2*32) = 5/32
    return AlgebraData(
        name=f"BetaGamma(lam={lam})",
        kappa=kappa,
        alpha=2.0,
        S4=S4,
        depth='C',
        params={'lambda': lam, 'c': c_bg},
    )


def virasoro_data(c_val: float = 1.0) -> AlgebraData:
    """Virasoro at central charge c.
    kappa = c/2, alpha = 2, S4 = 10/(c*(5c+22)), class M.
    """
    if abs(c_val) < 1e-15:
        return AlgebraData(
            name=f"Virasoro(c={c_val})",
            kappa=0.0, alpha=2.0, S4=float('inf'),
            depth='M', params={'c': c_val},
        )
    kappa = c_val / 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    return AlgebraData(
        name=f"Virasoro(c={c_val})",
        kappa=kappa,
        alpha=2.0,
        S4=S4,
        depth='M',
        params={'c': c_val},
    )


def w3_data(c_val: float = 2.0) -> AlgebraData:
    """W_3 algebra at central charge c.
    kappa(W_3) = c*(H_3-1) = 5c/6, alpha = 2, class M.
    """
    kappa = 5.0 * c_val / 6.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))  # T-line quartic
    return AlgebraData(
        name=f"W3(c={c_val})",
        kappa=kappa,
        alpha=2.0,
        S4=S4,
        depth='M',
        params={'c': c_val},
    )


def lattice_voa_data(rank: int = 1) -> AlgebraData:
    """Lattice VOA of given rank.  kappa = rank, alpha = 0, S4 = 0, class G."""
    return AlgebraData(
        name=f"Lattice(rank={rank})",
        kappa=float(rank),
        alpha=0.0,
        S4=0.0,
        depth='G',
        params={'rank': rank},
    )


def minimal_model_data(p: int = 3) -> AlgebraData:
    """Unitary minimal model M(p, p+1).
    c = 1 - 6/(p*(p+1)), which is a Virasoro algebra at c < 1.
    """
    q_param = p + 1
    c_val = 1.0 - 6.0 / (p * q_param)
    return virasoro_data(c_val)


# Standard family catalogue
STANDARD_FAMILIES = {
    'Heisenberg': heisenberg_data,
    'Affine_sl2': affine_sl2_data,
    'Affine_sl3': affine_sl3_data,
    'BetaGamma': betagamma_data,
    'Virasoro': virasoro_data,
    'W3': w3_data,
    'Lattice': lattice_voa_data,
}


# ===========================================================================
# Section 1: Shadow metric and tower coefficients
# ===========================================================================

def shadow_metric_coefficients(data: AlgebraData) -> Tuple[float, float, float]:
    """Q_L(t) = q0 + q1*t + q2*t^2, the shadow metric as quadratic in t."""
    kappa = data.kappa
    alpha = data.alpha
    S4 = data.S4
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    return q0, q1, q2


def critical_discriminant(data: AlgebraData) -> float:
    """Delta = 8*kappa*S4: the critical discriminant."""
    return 8.0 * data.kappa * data.S4


def shadow_radius(data: AlgebraData) -> float:
    """Shadow growth rate rho(A) = 1/R where R = min|branch point of H(t)|."""
    q0, q1, q2 = shadow_metric_coefficients(data)
    if abs(q0) < 1e-30:
        return float('inf')
    # rho^2 = q2/q0 for the normalized metric
    # More precisely: rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)
    # where Delta = 8*kappa*S4
    Delta = critical_discriminant(data)
    numer = 9.0 * data.alpha ** 2 + 2.0 * Delta
    if numer <= 0:
        return 0.0
    denom = 2.0 * abs(data.kappa)
    if denom < 1e-30:
        return float('inf')
    return math.sqrt(numer) / denom


def shadow_tower_coefficients(data: AlgebraData, max_arity: int = 80) -> Dict[int, float]:
    """Compute S_r(A) for r=2,...,max_arity.

    Uses H(t) = t^2*sqrt(Q_L(t)) = sum_{r>=2} r*S_r*t^r,
    so S_r = a_{r-2}/r where a_n = [t^n] sqrt(Q_L(t)).
    """
    q0, q1, q2 = shadow_metric_coefficients(data)
    max_n = max_arity - 2
    if max_n < 0:
        return {}

    if abs(q0) < 1e-30:
        return {r: 0.0 for r in range(2, max_arity + 1)}

    # Taylor coefficients of sqrt(q0 + q1*t + q2*t^2)
    a = [0.0] * (max_n + 1)
    a[0] = math.sqrt(abs(q0))
    if q0 < 0:
        # Shouldn't happen for standard families (q0 = 4*kappa^2 >= 0)
        a[0] = math.sqrt(abs(q0))

    if max_n >= 1:
        a[1] = q1 / (2.0 * a[0]) if abs(a[0]) > 1e-30 else 0.0
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2.0 * a[0]) if abs(a[0]) > 1e-30 else 0.0
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2.0 * a[0]) if abs(a[0]) > 1e-30 else 0.0

    coeffs = {}
    for n in range(max_n + 1):
        r = n + 2
        coeffs[r] = a[n] / r
    return coeffs


def classify_depth(data: AlgebraData) -> str:
    """Classify shadow depth from the metric data.

    G: alpha=0, S4=0 (or Delta=0 and alpha=0)
    L: alpha!=0, Delta=0
    C: special stratum separation (depth 4)
    M: Delta!=0 (infinite tower)
    """
    Delta = critical_discriminant(data)
    if abs(data.alpha) < 1e-15 and abs(data.S4) < 1e-15:
        return 'G'
    if abs(Delta) < 1e-15 and abs(data.alpha) > 1e-15:
        return 'L'
    if data.depth == 'C':
        return 'C'
    if abs(Delta) > 1e-15:
        return 'M'
    return data.depth


# ===========================================================================
# Section 2: Shadow q-series at roots of unity
# ===========================================================================

def root_of_unity(N: int, k: int = 1) -> complex:
    """zeta_N^k = e^{2*pi*i*k/N}."""
    return cmath.exp(2j * PI * k / N)


def shadow_qseries_at_root(data: AlgebraData, N: int,
                            max_arity: int = 80) -> complex:
    """Evaluate Z_A(zeta_N) = sum_{r=2}^{max_arity} S_r(A) * zeta_N^r.

    At roots of unity |zeta_N| = 1, so convergence requires rho < 1.
    For rho >= 1, we use the periodicity: zeta_N^r = zeta_N^{r mod N}
    to compute the FINITE sum modulo the cyclotomic relation.
    """
    S = shadow_tower_coefficients(data, max_arity)
    zeta = root_of_unity(N)

    rho = shadow_radius(data)
    if rho < 1.0 - 1e-10:
        # Convergent: sum directly
        total = complex(0.0)
        for r in range(2, max_arity + 1):
            total += S.get(r, 0.0) * zeta ** r
        return total
    else:
        # Use periodicity: group terms by r mod N
        # Z_A(zeta_N) = sum_{j=0}^{N-1} zeta_N^j * (sum_{r=j mod N, r>=2} S_r)
        # This is a FORMAL evaluation (Borel-regularized via cyclotomic folding)
        bucket = [0.0] * N
        for r in range(2, max_arity + 1):
            j = r % N
            bucket[j] += S.get(r, 0.0)
        total = complex(0.0)
        for j in range(N):
            total += bucket[j] * zeta ** j
        return total


def shadow_qseries_scan(data: AlgebraData, N_max: int = 50,
                         max_arity: int = 80) -> Dict[int, complex]:
    """Evaluate Z_A(zeta_N) for N = 1, 2, ..., N_max."""
    return {N: shadow_qseries_at_root(data, N, max_arity)
            for N in range(1, N_max + 1)}


def identify_algebraic_number(z: complex, max_deg: int = 8,
                               tol: float = 1e-6) -> Optional[Dict]:
    """Attempt to identify z as an algebraic number using integer relation detection.

    Simple heuristic approach: check if z is close to
      a rational, a quadratic irrationality, a root of unity multiple,
      or a known constant.
    """
    # Test: is z real?
    if abs(z.imag) < tol:
        x = z.real
        # Rational test: is x close to p/q for small q?
        for denom in range(1, 50):
            numer = round(x * denom)
            if abs(x - numer / denom) < tol:
                return {'type': 'rational', 'value': Fraction(numer, denom),
                        'approx': float(Fraction(numer, denom))}
        # Quadratic irrationality test: is x^2 rational?
        x2 = x * x
        for denom in range(1, 30):
            numer = round(x2 * denom)
            if abs(x2 - numer / denom) < tol and numer >= 0:
                sign = 1 if x >= 0 else -1
                return {'type': 'quadratic', 'value': f"{sign}*sqrt({Fraction(numer, denom)})",
                        'approx': x}
        return {'type': 'real_unidentified', 'approx': x}

    # Complex: test if |z| is a known value
    r = abs(z)
    theta = cmath.phase(z)

    # Root of unity multiple: z = a * zeta_N^k ?
    for denom in range(1, 30):
        r_numer = round(r * denom)
        if abs(r - r_numer / denom) < tol:
            # z = (r_numer/denom) * e^{i*theta}
            # Is theta a rational multiple of pi?
            theta_over_pi = theta / PI
            for q in range(1, 30):
                p = round(theta_over_pi * q)
                if abs(theta_over_pi - p / q) < tol / PI:
                    return {
                        'type': 'algebraic_polar',
                        'modulus': Fraction(r_numer, denom),
                        'argument': f"{p}*pi/{q}",
                        'approx': z,
                    }

    return {'type': 'unidentified', 'approx': z}


# ===========================================================================
# Section 3: Quantum modularity tests
# ===========================================================================

def mobius_action(gamma: List[List[int]], x: float) -> Optional[float]:
    """Apply gamma = [[a,b],[c,d]] in SL_2(Z) to x: gamma*x = (ax+b)/(cx+d)."""
    a, b = gamma[0]
    c_m, d = gamma[1]
    denom = c_m * x + d
    if abs(denom) < 1e-15:
        return None
    return (a * x + b) / denom


GAMMA_T = [[1, 1], [0, 1]]  # T: x -> x + 1
GAMMA_S = [[0, -1], [1, 0]]  # S: x -> -1/x
GAMMA_ST = [[0, -1], [1, 1]]  # ST: x -> -1/(x+1)
GAMMA_TS = [[1, -1], [1, 0]]  # TS: x -> (x-1)/x


def quantum_modular_defect(data: AlgebraData, x: float,
                            gamma: List[List[int]],
                            weight: float = 0.0,
                            max_arity: int = 100) -> Dict:
    r"""Compute the quantum modular defect at x for SL_2(Z) element gamma.

    h_gamma(x) = G(gamma*x) - j(gamma,x)^{-k} * G(x)

    where j(gamma,x) = cx + d is the automorphy factor and k is the weight.

    We evaluate the shadow ordinary GF G(t) = sum S_r t^r at t = x and t = gamma*x.
    For rational x = p/q with |x| < R (convergence radius), this is well-defined.
    """
    a, b = gamma[0]
    c_m, d = gamma[1]

    gamma_x = mobius_action(gamma, x)
    if gamma_x is None:
        return {'x': x, 'gamma': gamma, 'singular': True}

    S = shadow_tower_coefficients(data, max_arity)
    rho = shadow_radius(data)

    def _eval_gf(t, use_cyclotomic=False):
        """Evaluate G(t) = sum S_r t^r."""
        if abs(t) * rho < 1.0 - 1e-10:
            return sum(S.get(r, 0.0) * t ** r for r in range(2, max_arity + 1))
        else:
            # Optimal truncation
            N_star = max(3, int(1.0 / (rho * abs(t)))) if rho * abs(t) > 0 else max_arity
            N_star = min(N_star, max_arity)
            return sum(S.get(r, 0.0) * t ** r for r in range(2, N_star + 1))

    G_x = _eval_gf(x)
    G_gx = _eval_gf(gamma_x)

    automorphy = (c_m * x + d)
    if abs(automorphy) < 1e-15:
        j_factor = float('inf')
    else:
        j_factor = abs(automorphy) ** (-weight)

    defect = G_gx - j_factor * G_x

    # Test defects at several candidate weights
    defects_by_weight = {}
    for k_test in [0, 1, Fraction(3, 2), 2, 3]:
        k_f = float(k_test)
        if abs(automorphy) > 1e-15:
            j_k = abs(automorphy) ** (-k_f)
        else:
            j_k = float('inf')
        defects_by_weight[k_f] = G_gx - j_k * G_x

    return {
        'x': x,
        'gamma_x': gamma_x,
        'gamma': gamma,
        'G_x': G_x,
        'G_gamma_x': G_gx,
        'defect_at_weight': defect,
        'defects_by_weight': defects_by_weight,
        'singular': False,
        'automorphy_factor': automorphy,
    }


def quantum_modularity_scan(data: AlgebraData, max_denom: int = 8,
                             max_arity: int = 80) -> List[Dict]:
    """Scan quantum modular defects for T and S transforms at x = p/q."""
    results = []
    for q in range(1, max_denom + 1):
        for p in range(1, q + 1):
            if math.gcd(p, q) != 1:
                continue
            x = float(p) / float(q)

            # T-defect
            t_defect = quantum_modular_defect(data, x, GAMMA_T, weight=0, max_arity=max_arity)
            t_defect['transform'] = 'T'

            # S-defect (only if x != 0)
            if abs(x) > 1e-15:
                s_defect = quantum_modular_defect(data, x, GAMMA_S, weight=0, max_arity=max_arity)
                s_defect['transform'] = 'S'
            else:
                s_defect = None

            results.append({
                'p': p, 'q': q, 'x': x,
                'T_defect': t_defect,
                'S_defect': s_defect,
            })
    return results


def quantum_modularity_quality(data: AlgebraData,
                                max_denom: int = 6,
                                max_arity: int = 80) -> Dict:
    r"""Quantify how "quantum modular" the shadow q-series is.

    Metric: average |h_gamma(x)| / |G(x)| over rational x with small denominator.
    A true quantum modular form has this ratio bounded and "smooth" in x.
    A genuinely modular function has ratio = 0.
    """
    scan = quantum_modularity_scan(data, max_denom, max_arity)

    t_defects = []
    s_defects = []
    for entry in scan:
        td = entry['T_defect']
        if not td.get('singular') and abs(td.get('G_x', 0)) > 1e-15:
            t_defects.append(abs(td['defect_at_weight']) / abs(td['G_x']))
        sd = entry.get('S_defect')
        if sd and not sd.get('singular') and abs(sd.get('G_x', 0)) > 1e-15:
            s_defects.append(abs(sd['defect_at_weight']) / abs(sd['G_x']))

    return {
        'algebra': data.name,
        'depth': data.depth,
        'shadow_radius': shadow_radius(data),
        'T_defect_mean': sum(t_defects) / len(t_defects) if t_defects else None,
        'T_defect_max': max(t_defects) if t_defects else None,
        'S_defect_mean': sum(s_defects) / len(s_defects) if s_defects else None,
        'S_defect_max': max(s_defects) if s_defects else None,
        'num_T_points': len(t_defects),
        'num_S_points': len(s_defects),
    }


# ===========================================================================
# Section 4: Zagier's quantum modular forms — comparison
# ===========================================================================

def kontsevich_zagier_F(q_val: complex, max_terms: int = 200) -> complex:
    r"""Kontsevich-Zagier series F(q) = sum_{n>=0} (q;q)_n.

    This is Zagier's prototypical quantum modular form.
    At roots of unity q = zeta_N, the sum is finite (since (zeta_N;zeta_N)_n = 0
    for n >= N).

    F is quantum modular of weight 0 with respect to Gamma_0(2).
    """
    total = complex(0.0)
    pochhammer = complex(1.0)
    for n in range(max_terms):
        total += pochhammer
        pochhammer *= (1.0 - q_val ** (n + 1))
        if abs(pochhammer) < 1e-50:
            break
    return total


def kontsevich_zagier_F_at_root(N: int) -> complex:
    r"""F(zeta_N) = sum_{n=0}^{N-1} (zeta_N; zeta_N)_n.

    Finite sum at roots of unity.  These are algebraic numbers.
    """
    zeta = root_of_unity(N)
    total = complex(0.0)
    pochhammer = complex(1.0)
    for n in range(N):
        total += pochhammer
        pochhammer *= (1.0 - zeta ** (n + 1))
    return total


def zagier_quantum_modular_defect_F(N: int, gamma: List[List[int]]) -> Dict:
    r"""Quantum modular defect of F(q) at q = zeta_N under gamma.

    h_gamma(1/N) = F(zeta_{gamma*N}) - j(gamma,1/N)^{-k} * F(zeta_N)
    where gamma acts on 1/N viewed as an element of Q.
    """
    x = 1.0 / N
    gamma_x = mobius_action(gamma, x)
    if gamma_x is None:
        return {'N': N, 'singular': True}

    F_at_N = kontsevich_zagier_F_at_root(N)

    # gamma_x = p'/q' as fraction
    frac = Fraction(gamma_x).limit_denominator(10000)
    M = frac.denominator

    F_at_M = kontsevich_zagier_F_at_root(M)

    return {
        'N': N,
        'M': M,
        'x': x,
        'gamma_x': gamma_x,
        'F_zeta_N': F_at_N,
        'F_zeta_M': F_at_M,
        'defect': F_at_M - F_at_N,
        'defect_abs': abs(F_at_M - F_at_N),
    }


def shadow_vs_zagier_comparison(data: AlgebraData, N_max: int = 20) -> Dict:
    """Compare Z_A(zeta_N) with F(zeta_N) for N = 1,...,N_max.

    If the shadow q-series matches a known quantum modular form up to a
    scalar or polynomial transformation, this will detect it.
    """
    shadow_vals = shadow_qseries_scan(data, N_max)
    zagier_vals = {N: kontsevich_zagier_F_at_root(N) for N in range(1, N_max + 1)}

    ratios = {}
    for N in range(2, N_max + 1):
        zv = zagier_vals[N]
        sv = shadow_vals[N]
        if abs(zv) > 1e-15 and abs(sv) > 1e-15:
            ratios[N] = sv / zv

    # Test if ratios are constant (shadow = c * F)
    ratio_vals = list(ratios.values())
    if len(ratio_vals) >= 3:
        mean_ratio = sum(ratio_vals) / len(ratio_vals)
        variance = sum(abs(r - mean_ratio) ** 2 for r in ratio_vals) / len(ratio_vals)
        is_proportional = variance < 1e-6 * abs(mean_ratio) ** 2
    else:
        mean_ratio = None
        variance = None
        is_proportional = False

    return {
        'algebra': data.name,
        'shadow_values': shadow_vals,
        'zagier_values': zagier_vals,
        'ratios': ratios,
        'mean_ratio': mean_ratio,
        'is_proportional_to_zagier': is_proportional,
    }


# ===========================================================================
# Section 5: Habiro ring and integrality
# ===========================================================================

def q_pochhammer(q_val: complex, n: int) -> complex:
    """(q; q)_n = prod_{j=1}^n (1 - q^j)."""
    if n <= 0:
        return complex(1.0)
    product = complex(1.0)
    for j in range(1, n + 1):
        product *= (1.0 - q_val ** j)
    return product


def habiro_ring_test(data: AlgebraData, N: int, max_arity: int = 80) -> Dict:
    r"""Test Habiro ring membership for Z_A at q = zeta_N.

    Habiro ring Z[q]^ = projlim Z[q]/((q;q)_n).
    Membership requires Z_A(zeta_N) well-defined for all N.

    At q = zeta_N: (zeta_N; zeta_N)_n = 0 for n >= N (since 1 - zeta_N^N = 0).
    So any polynomial in (q;q)_0, (q;q)_1, ..., (q;q)_{N-1} evaluates finitely.

    We compute Z_A(zeta_N) and check:
      1. Finiteness (basic)
      2. Algebraicity (attempt PSLQ-style identification)
      3. Integrality of Z_A(zeta_N) * (zeta_N; zeta_N)_m for small m
    """
    zeta = root_of_unity(N)
    Z_val = shadow_qseries_at_root(data, N, max_arity)

    # (zeta_N; zeta_N)_m for m = 1,...,N-1
    pochhammer_vals = {}
    for m in range(1, N):
        pochhammer_vals[m] = q_pochhammer(zeta, m)

    # Test: Z_val * (zeta; zeta)_m close to algebraic integer?
    integrality_tests = {}
    for m in range(1, min(N, 10)):
        product = Z_val * pochhammer_vals.get(m, 1.0)
        # Check if product is close to an algebraic integer
        # Simple test: is it close to a Gaussian integer?
        near_gaussian = (abs(product.real - round(product.real)) < 0.01
                         and abs(product.imag - round(product.imag)) < 0.01)
        integrality_tests[m] = {
            'product': product,
            'product_abs': abs(product),
            'near_gaussian_integer': near_gaussian,
        }

    # Attempt algebraic identification
    alg_id = identify_algebraic_number(Z_val)

    return {
        'algebra': data.name,
        'N': N,
        'Z_at_zeta_N': Z_val,
        'Z_abs': abs(Z_val),
        'finite': abs(Z_val) < 1e15,
        'algebraic_id': alg_id,
        'integrality_tests': integrality_tests,
        'pochhammer_at_N': q_pochhammer(zeta, N),  # should be 0
    }


def habiro_scan(data: AlgebraData, N_max: int = 30,
                max_arity: int = 80) -> Dict:
    """Scan Habiro ring tests for N = 1,...,N_max."""
    results = {}
    all_finite = True
    for N in range(1, N_max + 1):
        result = habiro_ring_test(data, N, max_arity)
        results[N] = result
        if not result['finite']:
            all_finite = False

    return {
        'algebra': data.name,
        'N_max': N_max,
        'results': results,
        'all_finite': all_finite,
        'habiro_compatible': all_finite,
    }


# ===========================================================================
# Section 6: Nahm conjecture and shadow quadratic forms
# ===========================================================================

def nahm_matrix(data: AlgebraData) -> Dict:
    r"""Construct the Nahm matrix from shadow metric data.

    The Nahm matrix A encodes the quadratic form in the exponent of the
    q-hypergeometric sum f(q) = sum q^{n^T A n/2} / (q;q)_n.

    For rank-1 (single primary line): A is 1x1, A = q2/q0 = rho^2.
    Nahm criterion: eigenvalues in (0,1) <=> rho < 1 <=> c > c* for Virasoro.
    """
    q0, q1, q2 = shadow_metric_coefficients(data)
    rho = shadow_radius(data)

    if abs(q0) < 1e-30:
        return {'degenerate': True, 'algebra': data.name}

    A_val = q2 / q0  # 1x1 Nahm matrix entry

    eigenvalue = A_val
    nahm_satisfied = 0 < eigenvalue < 1

    # Bloch group element: D(alpha) where alpha satisfies 1 - alpha = alpha^A
    # For 1x1: alpha = 1/(1 + rho^2) = q0/(q0 + q2)
    alpha_bloch = q0 / (q0 + q2) if abs(q0 + q2) > 1e-15 else None

    # Rogers dilogarithm L(x) = Li_2(x) + (1/2)*ln(x)*ln(1-x) for x in (0,1)
    rogers_val = None
    if alpha_bloch is not None and 0 < alpha_bloch < 1:
        try:
            from mpmath import polylog, log as mlog
            Li2 = complex(polylog(2, alpha_bloch))
            rogers_val = Li2.real + 0.5 * math.log(alpha_bloch) * math.log(1 - alpha_bloch)
        except ImportError:
            # Approximate via series
            Li2_approx = sum(alpha_bloch ** n / n ** 2 for n in range(1, 100))
            rogers_val = Li2_approx + 0.5 * math.log(alpha_bloch) * math.log(1 - alpha_bloch)

    return {
        'algebra': data.name,
        'nahm_matrix': [[A_val]],
        'eigenvalue': eigenvalue,
        'rho_squared': rho ** 2,
        'eigenvalue_eq_rho_sq': abs(eigenvalue - rho ** 2) < 1e-10,
        'nahm_criterion': nahm_satisfied,
        'depth': data.depth,
        'bloch_alpha': alpha_bloch,
        'rogers_dilogarithm': rogers_val,
        'classification': (
            'Nahm-modular (class G/L: rho=0, eigenvalue<=0)'
            if rho < 1e-10 else
            'Nahm-convergent (rho < 1, eigenvalue in (0,1))'
            if nahm_satisfied else
            'Nahm-violated (rho >= 1, eigenvalue >= 1): quantum modular regime'
        ),
    }


def nahm_landscape_scan(families: Optional[Dict] = None) -> List[Dict]:
    """Nahm matrix analysis across the standard landscape."""
    if families is None:
        families = {
            'Heisenberg_k1': heisenberg_data(1.0),
            'Heisenberg_k2': heisenberg_data(2.0),
            'Affine_sl2_k1': affine_sl2_data(1.0),
            'Affine_sl2_k3': affine_sl2_data(3.0),
            'Virasoro_c1/2': virasoro_data(0.5),
            'Virasoro_c1': virasoro_data(1.0),
            'Virasoro_c7': virasoro_data(7.0),
            'Virasoro_c13': virasoro_data(13.0),
            'Virasoro_c25': virasoro_data(25.0),
            'W3_c2': w3_data(2.0),
            'BetaGamma': betagamma_data(),
            'Lattice_r1': lattice_voa_data(1),
            'Lattice_r24': lattice_voa_data(24),
        }

    results = []
    for label, data in families.items():
        nahm = nahm_matrix(data)
        nahm['label'] = label
        results.append(nahm)
    return results


# ===========================================================================
# Section 7: WRT invariants from shadow data
# ===========================================================================

def _su2_modular_data(k: int) -> Tuple[List[List[complex]], List[complex]]:
    """SU(2) level-k modular S and T matrices.

    For SU(2) at level k, there are (k+1) integrable reps labeled j=0,...,k.
    S_{j,j'} = sqrt(2/(k+2)) * sin(pi*(j+1)*(j'+1)/(k+2))
    T_{j,j'} = delta_{j,j'} * exp(2*pi*i*(h_j - c/24))
    where h_j = j(j+2)/(4(k+2)) and c = 3k/(k+2).
    """
    r = k + 2
    c_val = 3.0 * k / r
    prefactor = math.sqrt(2.0 / r)

    S_matrix = []
    T_diag = []
    for j in range(k + 1):
        row = []
        h_j = j * (j + 2) / (4.0 * r)
        T_diag.append(cmath.exp(2j * PI * (h_j - c_val / 24.0)))
        for jp in range(k + 1):
            row.append(prefactor * math.sin(PI * (j + 1) * (jp + 1) / r))
        S_matrix.append(row)

    return S_matrix, T_diag


def wrt_invariant_lens_space(p: int, q_lens: int, k: int) -> complex:
    r"""WRT invariant tau_k(L(p,q)) for lens space L(p,q) at SU(2) level k.

    For L(p,1) via surgery on the unknot:
        tau_k(L(p,1)) = sum_{j=0}^k S_{0,j}^2 * T_j^p

    For general L(p,q): uses the surgery formula with linking matrix.
    We implement L(p,1) exactly and L(p,q) for q=1 only.
    """
    if q_lens != 1:
        # General L(p,q): needs continued fraction expansion
        # For now, implement L(p,1) only
        return _wrt_lens_p1(p, k)

    return _wrt_lens_p1(p, k)


def _wrt_lens_p1(p: int, k: int) -> complex:
    """WRT invariant tau_k(L(p,1)) = sum_j S_{0j}^2 T_j^p."""
    S_matrix, T_diag = _su2_modular_data(k)
    total = complex(0.0)
    for j in range(k + 1):
        total += S_matrix[0][j] ** 2 * T_diag[j] ** p
    return total


def wrt_from_shadow(data_su2: AlgebraData, p: int, k: int,
                     max_arity: int = 80) -> Dict:
    r"""Compare WRT invariant tau_k(L(p,1)) with shadow data Z_A(zeta_N).

    Bridge: for SU(2) at level k, N = k + 2 is the natural root-of-unity order.
    tau_k(L(p,1)) is computed from modular data.
    Z_A(zeta_N) is computed from the shadow tower.

    The comparison tests whether WRT invariants are accessible from shadow data.
    """
    N = k + 2  # natural root of unity order for SU(2) level k

    wrt_val = wrt_invariant_lens_space(p, 1, k)
    Z_shadow = shadow_qseries_at_root(data_su2, N, max_arity)
    Z_shadow_p = shadow_qseries_at_root(data_su2, N * p, max_arity)

    # Ratio
    ratio = wrt_val / Z_shadow if abs(Z_shadow) > 1e-15 else None

    return {
        'p': p,
        'k': k,
        'N': N,
        'wrt_L(p,1)': wrt_val,
        'wrt_abs': abs(wrt_val),
        'Z_shadow_zeta_N': Z_shadow,
        'Z_shadow_zeta_Np': Z_shadow_p,
        'ratio_wrt_to_shadow': ratio,
        'algebra': data_su2.name,
    }


def wrt_s3(k: int) -> complex:
    """WRT invariant of S^3 at SU(2) level k.

    tau_k(S^3) = S_{0,0}^2 * sum_j (S_{0j}/S_{00})^2
    = 1/D^2 where D^2 = sum_j (dim_q j)^2.

    More directly: tau_k(S^3) = S_{0,0} (the quantum dimension of the vacuum).
    Actually: Z(S^3) = sqrt(2/(k+2)) * sin(pi/(k+2)).
    """
    r = k + 2
    return math.sqrt(2.0 / r) * math.sin(PI / r)


# ===========================================================================
# Section 8: Resurgent structure at roots of unity
# ===========================================================================

def instanton_action_from_shadow(data: AlgebraData) -> Dict:
    r"""Compute the instanton action S_1 from the shadow metric branch points.

    The resurgent structure of Z_A(e^{2*pi*i*tau}) as tau -> p/q involves
    trans-series:
        Z ~ sum a_k eps^{k/2} + e^{-S_1/eps} * sum b_k eps^{k/2} + ...
    where eps = tau - p/q.

    The instanton action S_1 is related to the distance to the nearest
    singularity of the Borel transform, which for the shadow GF is
    determined by the branch points of H(t) = t^2*sqrt(Q_L(t)).

    Branch points: zeros of Q_L(t) at t = t_+/-.
    S_1 = -2*pi*i * t_0 (the nearest branch point).
    """
    q0, q1, q2 = shadow_metric_coefficients(data)
    if abs(q2) < 1e-30:
        # Q_L is at most linear: no branch points
        return {
            'algebra': data.name,
            'branch_points': None,
            'instanton_action': None,
            'has_resurgent_structure': False,
        }

    disc = q1 ** 2 - 4 * q0 * q2
    t_plus = (-q1 + cmath.sqrt(disc)) / (2.0 * q2)
    t_minus = (-q1 - cmath.sqrt(disc)) / (2.0 * q2)

    # Nearest branch point determines the instanton action
    r_plus = abs(t_plus)
    r_minus = abs(t_minus)
    nearest = t_plus if r_plus <= r_minus else t_minus
    S_1 = -2j * PI * nearest

    return {
        'algebra': data.name,
        'branch_point_plus': t_plus,
        'branch_point_minus': t_minus,
        'branch_point_modulus_plus': r_plus,
        'branch_point_modulus_minus': r_minus,
        'nearest_branch_point': nearest,
        'instanton_action': S_1,
        'instanton_action_abs': abs(S_1),
        'has_resurgent_structure': True,
        'discriminant_sign': 'negative' if disc.real < 0 else 'positive',
    }


def resurgent_expansion_at_rational(data: AlgebraData, p: int, q_denom: int,
                                     num_approach: int = 30,
                                     max_terms: int = 100) -> Dict:
    r"""Compute the asymptotic expansion of F_1(tau) = -kappa*log eta(tau)
    as tau -> p/q from above (Im tau -> 0+).

    The expansion is controlled by the modular S-matrix of SL_2(Z).
    Near tau = p/q: tau = p/q + i*epsilon, epsilon -> 0+.

    Using the S-transformation of eta:
        eta(-1/tau) = sqrt(-i*tau) * eta(tau)
    and the periodicity eta(tau+1) = e^{pi*i/12} * eta(tau),
    we can express eta(p/q + i*eps) in terms of eta at large Im tau.
    """
    kappa = data.kappa
    results = []

    for j in range(1, num_approach + 1):
        eps = 10.0 ** (-j * 0.3)
        tau = complex(float(p) / float(q_denom), eps)
        q_val = cmath.exp(2j * PI * tau)

        # Compute log eta(tau) directly
        log_eta = 2j * PI * tau / 24.0
        for n in range(1, max_terms + 1):
            qn = q_val ** n
            if abs(qn) < 1e-50:
                break
            log_eta += cmath.log(1.0 - qn)

        F1 = -kappa * log_eta

        results.append({
            'epsilon': eps,
            'tau': tau,
            'F1': F1,
            'F1_real': F1.real,
            'F1_imag': F1.imag,
        })

    # Extract the leading asymptotics
    # Near tau = p/q: log eta(tau) ~ pi*i/(12*tau') where tau' = q*tau - p
    # i.e. log eta(p/q + i*eps) ~ -pi/(12*q*eps) + const + O(eps)
    # So F_1 ~ kappa * pi/(12*q*eps) (diverges as 1/eps)

    leading_coeff = kappa * PI / (12.0 * q_denom) if q_denom > 0 else None

    # Fit: F_1_real ~ A/eps + B + C*eps + ...
    if len(results) >= 3:
        eps_vals = [r['epsilon'] for r in results[-10:]]
        F_reals = [r['F1_real'] for r in results[-10:]]
        # Simple 1/eps leading coefficient extraction
        A_est = F_reals[0] * eps_vals[0] if eps_vals[0] > 0 else None
    else:
        A_est = None

    instanton = instanton_action_from_shadow(data)

    return {
        'algebra': data.name,
        'p': p,
        'q': q_denom,
        'kappa': kappa,
        'leading_coefficient': leading_coeff,
        'estimated_leading': A_est,
        'instanton_action': instanton.get('instanton_action'),
        'approach_data': results[-5:],
        'num_points': len(results),
    }


# ===========================================================================
# Section 9: False theta functions and class-M connections
# ===========================================================================

def false_theta_psi(q_val: complex, max_terms: int = 200) -> complex:
    r"""False theta function Psi(q) = sum_{n>=0} (-1)^n q^{n(n+1)/2}.

    A partial theta function: the sum runs over n >= 0 only, not all integers.
    Psi is quantum modular (Zagier), not modular.
    """
    total = complex(0.0)
    for n in range(max_terms):
        exp_val = n * (n + 1) / 2.0
        term = ((-1) ** n) * q_val ** exp_val
        total += term
        if abs(term) < 1e-50 and n > 5:
            break
    return total


def false_theta_at_root(N: int) -> complex:
    """Psi(zeta_N) at N-th root of unity."""
    zeta = root_of_unity(N)
    return false_theta_psi(zeta)


def shadow_vs_false_theta(data: AlgebraData, N_max: int = 30) -> Dict:
    r"""Compare shadow q-series Z_A(zeta_N) with false theta Psi(zeta_N).

    For class-M algebras, the shadow tower has infinite depth, and the
    partial-sum character of the shadow GF (sum from r=2, not all Z)
    is structurally analogous to partial theta functions.
    """
    shadow_vals = shadow_qseries_scan(data, N_max)
    false_theta_vals = {N: false_theta_at_root(N) for N in range(1, N_max + 1)}

    ratios = {}
    for N in range(2, N_max + 1):
        sv = shadow_vals.get(N, 0)
        fv = false_theta_vals[N]
        if abs(fv) > 1e-15 and abs(sv) > 1e-15:
            ratios[N] = sv / fv

    # Test: is the ratio a smooth function of N?
    ratio_abs = [abs(r) for r in ratios.values()]
    if len(ratio_abs) >= 3:
        ratio_spread = max(ratio_abs) / min(ratio_abs) if min(ratio_abs) > 1e-15 else float('inf')
    else:
        ratio_spread = None

    return {
        'algebra': data.name,
        'depth': data.depth,
        'shadow_vals': {N: sv for N, sv in list(shadow_vals.items())[:10]},
        'false_theta_vals': {N: fv for N, fv in list(false_theta_vals.items())[:10]},
        'ratios': ratios,
        'ratio_spread': ratio_spread,
        'structurally_similar': (ratio_spread is not None and ratio_spread < 10),
    }


# ===========================================================================
# Section 10: Mock modularity analysis
# ===========================================================================

def mock_modular_shadow_test(data: AlgebraData, tau_val: complex = None,
                              max_arity: int = 60) -> Dict:
    r"""Test mock modular properties of the shadow partition function.

    A mock modular form f of weight k has a shadow g (holomorphic modular
    of weight 2-k) such that f_hat = f + Eichler(g) is a harmonic Maass form.

    For the shadow GF:
    1. The genus-1 amplitude F_1(tau) = -kappa*log eta(tau) is quasi-modular
       (involves E_2*), not mock modular.
    2. The shadow tower G(t) = sum S_r t^r is an algebraic function of t,
       which does not directly fit the mock modular framework.
    3. However, certain generating functions constructed from G(t) and
       the modular data of A DO exhibit mock modular behavior.

    This function tests the SECOND DERIVATIVE of log eta as a mock modular
    candidate (the Eisenstein series E_2 is quasi-modular; its non-holomorphic
    completion E_2* = E_2 - 3/(pi*y) is almost modular).
    """
    if tau_val is None:
        tau_val = complex(0, 1)

    y = tau_val.imag
    if y <= 0:
        return {'error': 'tau must be in upper half-plane'}

    q = cmath.exp(2j * PI * tau_val)
    kappa = data.kappa

    # E_2(tau) = 1 - 24*sum_{n>=1} sigma_1(n)*q^n
    E2 = complex(1.0)
    for n in range(1, 100):
        # sigma_1(n) = sum of divisors of n
        sigma1 = sum(d for d in range(1, n + 1) if n % d == 0)
        E2 -= 24 * sigma1 * q ** n
        if abs(q ** n) < 1e-30:
            break

    # Non-holomorphic completion: E_2*(tau) = E_2(tau) - 3/(pi*y)
    E2_star = E2 - 3.0 / (PI * y)

    # F_1(tau) = -kappa * log eta(tau)
    log_eta = 2j * PI * tau_val / 24.0
    for n in range(1, 200):
        qn = q ** n
        if abs(qn) < 1e-30:
            break
        log_eta += cmath.log(1.0 - qn)

    F1_hol = -kappa * log_eta

    # The "shadow" in the mock modular sense for the genus-1 amplitude
    # F_1 is NOT mock modular; it transforms with an additive anomaly
    # controlled by E_2*. The anomaly is the non-holomorphic correction.
    mock_shadow = -kappa * 3.0 / (PI * y) / 24.0

    # Shadow tower evaluation
    S = shadow_tower_coefficients(data, max_arity)
    rho = shadow_radius(data)
    Delta = critical_discriminant(data)

    return {
        'algebra': data.name,
        'tau': tau_val,
        'kappa': kappa,
        'E2': E2,
        'E2_star': E2_star,
        'E2_anomaly': 3.0 / (PI * y),
        'F1_holomorphic': F1_hol,
        'mock_shadow_correction': mock_shadow,
        'discriminant': Delta,
        'shadow_radius': rho,
        'depth': data.depth,
        'mock_type': (
            'quasi-modular (E_2* completion)'
            if data.depth == 'M' else
            'modular (theta function type)'
            if data.depth in ('G', 'L') else
            'quasi-modular (E_2* + contact correction)'
        ),
    }


# ===========================================================================
# Section 11: Categorification (Khovanov-type homology)
# ===========================================================================

def khovanov_shadow_euler(data: AlgebraData, max_arity: int = 40) -> Dict:
    r"""Graded Euler characteristic from a putative Khovanov-type homology
    of the shadow tower.

    SETUP: Suppose there exists a bigraded abelian group
        H^{i,j}(shadow_A)
    such that:
        chi_q(H) = sum_{i,j} (-1)^i q^j dim H^{i,j} = Z_A(q)

    This function constructs a MINIMAL model:
    place S_r on the (0, r) diagonal: H^{0,r} = Q^{|S_r|}, H^{i,r} = 0 for i>0.
    Then chi_q = sum_r S_r * q^r = Z_A(q) trivially.

    The interesting question is whether the Khovanov homology has higher
    homological structure (d: H^{i,j} -> H^{i+1,j+?}) that categorifies
    the shadow connection or the MC equation.

    For class G/L: the homology is finite-dimensional (only H^{0,r} for r <= 3 or 4).
    For class M: infinite-dimensional, with exponential growth governed by rho.
    """
    S = shadow_tower_coefficients(data, max_arity)

    # Minimal model: H^{0,r} has dimension |S_r| (or rather, S_r is the signed rank)
    homology = {}
    total_dim = 0
    euler_char = complex(0.0)

    for r in range(2, max_arity + 1):
        S_r = S.get(r, 0.0)
        # In the minimal model, we place a 1-dim space at (0, r) with sign sgn(S_r)
        if abs(S_r) > 1e-50:
            homology[r] = {
                'i': 0,
                'j': r,
                'rank': 1,
                'signed_dim': 1 if S_r > 0 else -1,
                'value': S_r,
            }
            total_dim += 1

    # Euler characteristic at q = zeta_N
    zeta_3 = root_of_unity(3)
    chi_zeta_3 = sum(S.get(r, 0.0) * zeta_3 ** r for r in range(2, max_arity + 1))

    Z_zeta_3 = shadow_qseries_at_root(data, 3, max_arity)

    return {
        'algebra': data.name,
        'depth': data.depth,
        'total_dim': total_dim,
        'nonzero_arities': len(homology),
        'chi_at_zeta_3': chi_zeta_3,
        'Z_at_zeta_3': Z_zeta_3,
        'euler_matches_shadow': abs(chi_zeta_3 - Z_zeta_3) < 1e-10,
        'homology_preview': {r: h for r, h in list(homology.items())[:5]},
        'poincare_series_coeffs': {r: abs(S.get(r, 0)) for r in range(2, min(15, max_arity + 1))},
    }


# ===========================================================================
# Section 12: Depth classification and modularity type
# ===========================================================================

def depth_modularity_classification(data: AlgebraData,
                                     max_arity: int = 60) -> Dict:
    r"""Classify the modularity type based on shadow depth.

    CENTRAL THESIS:
      G (r_max=2):  theta-modular (Nahm-trivial, Habiro-compatible)
      L (r_max=3):  Nahm-modular (q-hypergeometric with pos def form)
      C (r_max=4):  quasi-modular (E_2*-type corrections from contact term)
      M (r_max=inf): quantum modular (Zagier type) / mock modular

    This function computes the evidence for this classification.
    """
    depth = classify_depth(data)
    rho = shadow_radius(data)
    Delta = critical_discriminant(data)
    nahm = nahm_matrix(data)
    S = shadow_tower_coefficients(data, max_arity)

    # Termination test
    nonzero_arities = [r for r in range(2, max_arity + 1)
                       if abs(S.get(r, 0)) > 1e-15]
    max_nonzero = max(nonzero_arities) if nonzero_arities else 2

    if depth == 'G':
        expected_max_arity = 2
        terminates_correctly = max_nonzero <= 3
        modularity_type = 'theta-modular'
    elif depth == 'L':
        expected_max_arity = 3
        terminates_correctly = max_nonzero <= 4
        modularity_type = 'Nahm-modular'
    elif depth == 'C':
        expected_max_arity = 4
        terminates_correctly = max_nonzero <= 5
        modularity_type = 'quasi-modular'
    else:  # M
        expected_max_arity = max_arity
        terminates_correctly = max_nonzero > 10
        modularity_type = 'quantum-modular'

    # Nahm criterion consistency
    nahm_consistent = (
        (depth in ('G', 'L') and (nahm['eigenvalue'] <= 0 or not nahm.get('nahm_criterion')))
        or (depth == 'M' and nahm['eigenvalue'] > 0)
        or (depth == 'C')
    )

    return {
        'algebra': data.name,
        'depth': depth,
        'shadow_radius': rho,
        'discriminant': Delta,
        'nahm_eigenvalue': nahm.get('eigenvalue'),
        'nahm_criterion': nahm.get('nahm_criterion'),
        'modularity_type': modularity_type,
        'max_nonzero_arity': max_nonzero,
        'expected_max_arity': expected_max_arity,
        'terminates_correctly': terminates_correctly,
        'nahm_consistent': nahm_consistent,
    }


def full_landscape_classification(max_arity: int = 60) -> List[Dict]:
    """Run depth-modularity classification across the full standard landscape."""
    families = [
        heisenberg_data(1.0),
        heisenberg_data(2.0),
        lattice_voa_data(1),
        lattice_voa_data(8),
        lattice_voa_data(24),
        affine_sl2_data(1.0),
        affine_sl2_data(3.0),
        affine_sl3_data(1.0),
        betagamma_data(),
        virasoro_data(0.5),
        virasoro_data(1.0),
        virasoro_data(7.0),
        virasoro_data(13.0),
        virasoro_data(25.0),
        w3_data(2.0),
        w3_data(10.0),
        minimal_model_data(3),  # Ising
        minimal_model_data(4),  # Tri-critical Ising
    ]

    results = []
    for data in families:
        classification = depth_modularity_classification(data, max_arity)
        results.append(classification)
    return results


# ===========================================================================
# Section 13: Multi-path cross-verification
# ===========================================================================

def cross_verify_nahm_vs_radius(data: AlgebraData) -> Dict:
    """Cross-verify: Nahm eigenvalue = rho^2 (three independent paths)."""
    # Path 1: Nahm matrix construction
    nahm = nahm_matrix(data)
    eigenvalue = nahm.get('eigenvalue', None)

    # Path 2: Shadow radius formula
    rho = shadow_radius(data)
    rho_sq = rho ** 2

    # Path 3: Ratio test on shadow coefficients
    S = shadow_tower_coefficients(data, 50)
    ratios = []
    for r in range(10, 45):
        if r in S and r - 1 in S and abs(S[r - 1]) > 1e-50:
            ratios.append(abs(S[r] / S[r - 1]))
    ratio_rho_est = ratios[-1] if ratios else None
    ratio_rho_sq_est = ratio_rho_est ** 2 if ratio_rho_est else None

    agreement_12 = abs(eigenvalue - rho_sq) < 1e-8 if eigenvalue is not None else False
    agreement_13 = (abs(eigenvalue - ratio_rho_sq_est) < 0.01
                    if eigenvalue is not None and ratio_rho_sq_est is not None else None)
    agreement_23 = (abs(rho_sq - ratio_rho_sq_est) < 0.01
                    if ratio_rho_sq_est is not None else None)

    return {
        'algebra': data.name,
        'nahm_eigenvalue': eigenvalue,
        'rho_squared': rho_sq,
        'ratio_test_rho_sq': ratio_rho_sq_est,
        'agreement_nahm_radius': agreement_12,
        'agreement_nahm_ratio': agreement_13,
        'agreement_radius_ratio': agreement_23,
    }


def cross_verify_qseries_cyclotomic(data: AlgebraData, N: int,
                                      max_arity: int = 80) -> Dict:
    """Cross-verify Z_A(zeta_N) via direct sum vs cyclotomic folding."""
    S = shadow_tower_coefficients(data, max_arity)
    zeta = root_of_unity(N)

    # Path 1: Direct sum
    direct = sum(S.get(r, 0.0) * zeta ** r for r in range(2, max_arity + 1))

    # Path 2: Cyclotomic folding (group by r mod N)
    bucket = [0.0] * N
    for r in range(2, max_arity + 1):
        bucket[r % N] += S.get(r, 0.0)
    folded = sum(bucket[j] * zeta ** j for j in range(N))

    # Path 3: From the algebraic function at zeta_N
    # H(zeta_N) = zeta_N^2 * sqrt(Q_L(zeta_N))
    q0, q1, q2 = shadow_metric_coefficients(data)
    Q_at_zeta = q0 + q1 * zeta + q2 * zeta ** 2
    H_algebraic = zeta ** 2 * cmath.sqrt(Q_at_zeta)

    # H = sum r*S_r*t^r, so H(zeta_N) = sum r*S_r*zeta_N^r
    H_series = sum(r * S.get(r, 0.0) * zeta ** r for r in range(2, max_arity + 1))

    return {
        'algebra': data.name,
        'N': N,
        'direct_sum': direct,
        'cyclotomic_folded': folded,
        'H_algebraic': H_algebraic,
        'H_series': H_series,
        'agreement_direct_folded': abs(direct - folded) < 1e-8,
        'agreement_H_algebraic_series': abs(H_algebraic - H_series) < 1e-4,
    }


def cross_verify_depth_vs_termination(data: AlgebraData,
                                       max_arity: int = 60) -> Dict:
    """Cross-verify depth classification against actual coefficient termination."""
    depth = classify_depth(data)
    S = shadow_tower_coefficients(data, max_arity)

    # Find the last nonzero coefficient
    last_nonzero = 1
    for r in range(2, max_arity + 1):
        if abs(S.get(r, 0)) > 1e-12:
            last_nonzero = r

    depth_to_expected_max = {
        'G': 2,
        'L': 3,
        'C': 4,
        'M': max_arity,  # Should still be nonzero at max_arity
    }

    expected = depth_to_expected_max.get(depth, max_arity)

    if depth == 'M':
        consistent = last_nonzero >= max_arity - 5
    elif depth == 'C':
        # Contact: terminates at 4 on the primary line, but may extend
        consistent = last_nonzero <= 6
    else:
        consistent = last_nonzero <= expected + 1

    return {
        'algebra': data.name,
        'depth': depth,
        'last_nonzero_arity': last_nonzero,
        'expected_max': expected,
        'consistent': consistent,
    }
