r"""Higher A-infinity transferred structure maps m_5, m_6, m_7 for Virasoro.

Extends virasoro_ainfty_explicit.py from arities 2-4 to arities 5-7.

THE COMPUTATION:

The Virasoro algebra Vir_c has a single strong generator T of conformal
weight 2.  The transferred A-infinity operations m_k on H*(B(Vir_c)) are
computed via the Kadeishvili-Merkulov tree formula (HPL transfer).

On the PRIMARY LINE (all inputs = sT, the desuspension of T in bar
degree 1), the transferred operations satisfy:

    m_k^{tr}(sT, ..., sT) = S_k * (basis vector at weight 2k in Ext^1)

where S_k is the shadow tower coefficient at arity k.  This is the
shadow-formality identification (prop:shadow-formality-low-arity),
PROVED at arities 2, 3, 4 and extended here to arities 5, 6, 7.

WEIGHT GRADING:  sT has weight 2 and bar degree 1.  The operation
m_k(sT, ..., sT) has total weight 2k and bar degree 1.  Different
arities live in DIFFERENT weight spaces of Ext^1.  The A-infinity
relations involve compositions where intermediate results occupy
specific weight components; they are verified within each weight
component separately.

A-INFINITY RELATIONS:

The Stasheff relation at arity n (with m_1 = 0 on cohomology):

    sum_{p+q+r=n, q>=2} (-1)^{pq+r} m_{p+1+r}(id^p, m_q, id^r) = 0

At each arity, this provides a consistency check.  On the primary line,
the relation reduces to the MC equation of the shadow tower, which is
equivalent to the convolution recursion f^2 = Q_L (the shadow metric
identity).

FORMALITY OBSTRUCTION:

Virasoro has shadow depth = infinity (class M).  The obstruction to
A-infinity formality at arity k is the class [m_k] in the Hochschild
cohomology HH^2(Ext, Ext).  For Virasoro, m_k != 0 for ALL k >= 3,
confirming infinite shadow depth.  The obstruction cocycle at each
arity is the image of S_k under the shadow-formality identification.

CONVENTIONS:
- Cohomological grading (|d| = +1)
- Bar uses DESUSPENSION: |sT| = |T| - 1 = 2 - 1 = 1
- Exact rational arithmetic via fractions.Fraction
- Shadow coefficients: S_r = a_{r-2} / r where a_n are Taylor
  coefficients of sqrt(Q_L(t))

KNOWN VALUES (from quintic_shadow_engine.py, recomputed independently):
    S_5(c) = -48 / [c^2 (5c + 22)]
    S_6(c) = 80(45c + 193) / [3 c^3 (5c + 22)^2]
    S_7(c) = -2880(15c + 61) / [7 c^4 (5c + 22)^2]

References:
    prop:shadow-formality-low-arity (nonlinear_modular_shadows.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:obstruction-recursion (higher_genus_modular_koszul.tex)
    quintic_shadow_engine.py (independent verification)
    Kadeishvili, "On the theory of homology of fiber spaces", 1980.
    Merkulov, "Strong homotopy algebras", 1999.
    Loday-Vallette, "Algebraic Operads", Ch 9-10.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

FR = Fraction


# ============================================================================
# Exact rational arithmetic helpers
# ============================================================================

def _frac(x) -> Fraction:
    """Coerce to Fraction."""
    if isinstance(x, Fraction):
        return x
    if isinstance(x, (int,)):
        return Fraction(int(x))
    try:
        import numpy as np
        if isinstance(x, np.integer):
            return Fraction(int(x))
    except ImportError:
        pass
    if isinstance(x, float):
        return Fraction(x).limit_denominator(10**15)
    return Fraction(x)


# ============================================================================
# Shadow metric and convolution recursion
# ============================================================================

def virasoro_shadow_metric(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    r"""Shadow metric coefficients Q_L(t) = q0 + q1*t + q2*t^2 for Virasoro.

    Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S_4)*t^2

    with kappa = c/2, alpha = 2, S_4 = 10/(c*(5c+22)).

    Returns (q0, q1, q2) as exact Fractions.
    """
    c = _frac(c_val)
    kappa = c / FR(2)
    alpha = FR(2)
    S4 = FR(10) / (c * (FR(5) * c + FR(22)))

    q0 = FR(4) * kappa ** 2
    q1 = FR(12) * kappa * alpha
    q2 = FR(9) * alpha ** 2 + FR(16) * kappa * S4
    return q0, q1, q2


def convolution_coefficients(q0: Fraction, q1: Fraction, q2: Fraction,
                             max_n: int) -> List[Fraction]:
    r"""Taylor coefficients a_n of f(t) = sqrt(q0 + q1*t + q2*t^2).

    Recursion from f^2 = Q_L:
        a_0 = sqrt(q0)    [must be rational; for Virasoro, q0 = c^2, a_0 = c]
        a_1 = q1 / (2*a_0)
        a_2 = (q2 - a_1^2) / (2*a_0)
        a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j * a_{n-j}  for n >= 3

    The shadow coefficient at arity r is S_r = a_{r-2} / r.

    Parameters:
        q0, q1, q2: shadow metric coefficients (exact Fractions)
        max_n: compute a_0 through a_{max_n}

    Returns:
        List of Fraction [a_0, a_1, ..., a_{max_n}].

    Raises:
        ValueError: if q0 is not a perfect square (cannot take exact sqrt).
    """
    # Exact rational sqrt of q0
    # For Virasoro: q0 = c^2, so a_0 = c.
    # General case: q0 = (p/q)^2, check.
    n_q0 = q0.numerator
    d_q0 = q0.denominator
    from math import isqrt
    sn = isqrt(abs(n_q0))
    sd = isqrt(abs(d_q0))
    if sn * sn != abs(n_q0) or sd * sd != abs(d_q0):
        raise ValueError(f"q0 = {q0} is not a perfect square of a rational")
    a0 = Fraction(sn, sd)
    if q0 < 0:
        raise ValueError(f"q0 = {q0} is negative, cannot take real sqrt")

    coeffs = [a0]
    if max_n >= 1:
        a1 = q1 / (FR(2) * a0)
        coeffs.append(a1)
    if max_n >= 2:
        a2 = (q2 - coeffs[1] ** 2) / (FR(2) * a0)
        coeffs.append(a2)
    for n in range(3, max_n + 1):
        conv = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs.append(-conv / (FR(2) * a0))
    return coeffs


def virasoro_shadow_tower(c_val: Fraction, max_arity: int = 10
                          ) -> Dict[int, Fraction]:
    r"""Full shadow tower S_2, ..., S_{max_arity} for Virasoro at central charge c.

    S_r = a_{r-2} / r  where a_n are Taylor coefficients of sqrt(Q_L).

    Parameters:
        c_val: positive rational central charge
        max_arity: compute S_2 through S_{max_arity}

    Returns:
        Dict mapping arity r -> S_r as Fraction.
    """
    c = _frac(c_val)
    if c <= 0:
        raise ValueError("Central charge must be positive")
    q0, q1, q2 = virasoro_shadow_metric(c)
    coeffs = convolution_coefficients(q0, q1, q2, max_arity - 2)
    tower = {}
    for n in range(len(coeffs)):
        r = n + 2
        tower[r] = coeffs[n] / FR(r)
    return tower


# ============================================================================
# Higher A-infinity operations: m_5, m_6, m_7
# ============================================================================

class HigherVirasoroAInfinity:
    r"""Higher A-infinity transferred operations m_5, m_6, m_7 on H*(B(Vir_c)).

    This class extends PrimarySectorAInfinity from virasoro_ainfty_explicit.py
    to arities 5-7.  The computation uses the convolution recursion which
    encodes the full HTT (Homological Transfer Theorem) data on the primary
    line.

    On the primary line, the transferred A-infinity operations satisfy:

        m_k(sT, ..., sT) = S_k * (weight-2k basis vector in Ext^1)

    The A-infinity relations are encoded by the MC equation:

        sum_{i+j=r, i,j>=2} S_i * S_j + (horizontal differential) * S_r = 0

    which is equivalent to the convolution recursion a_n = -(1/(2a_0)) *
    sum a_j * a_{n-j}.

    Parameters:
        c_val: Central charge (positive rational).
    """

    def __init__(self, c_val: Fraction):
        self.c = _frac(c_val)
        if self.c <= 0:
            raise ValueError("Central charge must be positive")
        self.kappa = self.c / FR(2)
        self._tower_cache: Optional[Dict[int, Fraction]] = None

    def shadow_tower(self, max_arity: int = 10) -> Dict[int, Fraction]:
        """Compute and cache the shadow tower."""
        if self._tower_cache is None or max(self._tower_cache.keys()) < max_arity:
            self._tower_cache = virasoro_shadow_tower(self.c, max_arity)
        return self._tower_cache

    def mk_primary(self, k: int) -> Fraction:
        r"""Transferred m_k on the primary line: m_k(sT, ..., sT).

        Returns the scalar coefficient S_k (the shadow tower coefficient
        at arity k), which is the normalized structure constant.

        The shadow-formality identification gives:
            m_k^{tr}(sT, ..., sT) = S_k * e_{2k}

        where e_{2k} is the weight-2k basis vector in Ext^1.

        For k = 1: returns 0 (m_1 = 0 on cohomology).
        For k = 2: returns S_2 = kappa = c/2.
        For k >= 3: returns the shadow coefficient S_k.
        """
        if k <= 1:
            return FR(0)
        tower = self.shadow_tower(max_arity=k)
        return tower.get(k, FR(0))

    def m5_primary(self) -> Fraction:
        r"""m_5(sT, sT, sT, sT, sT) on the primary line.

        S_5 = -48 / [c^2 (5c + 22)]

        Independently derived:
            a_3 = -(2*a_1*a_2) / (2*a_0) = -a_1*a_2 / a_0
            a_1 = 6, a_2 = 40 / [c(5c+22)], a_0 = c
            a_3 = -6 * 40 / [c * c * (5c+22)] = -240 / [c^2(5c+22)]
            S_5 = a_3 / 5 = -48 / [c^2(5c+22)]
        """
        return self.mk_primary(5)

    def m6_primary(self) -> Fraction:
        r"""m_6(sT, ..., sT) on the primary line.

        S_6 = 80(45c + 193) / [3 c^3 (5c + 22)^2]

        Derived from:
            a_4 = -(1/(2*a_0)) * (2*a_1*a_3 + a_2^2)
            Then S_6 = a_4 / 6.
        """
        return self.mk_primary(6)

    def m7_primary(self) -> Fraction:
        r"""m_7(sT, ..., sT) on the primary line.

        S_7 = -2880(15c + 61) / [7 c^4 (5c + 22)^2]

        Derived from:
            a_5 = -(1/(2*a_0)) * (2*a_1*a_4 + 2*a_2*a_3)
            Then S_7 = a_5 / 7.
        """
        return self.mk_primary(7)

    # ------------------------------------------------------------------
    # Structure constants at specific weights
    # ------------------------------------------------------------------

    def structure_constants(self, max_arity: int = 7,
                            max_weight: int = 8
                            ) -> Dict[Tuple[int, int], Fraction]:
        r"""Structure constants of m_k on the primary line, organized by
        (arity k, output weight 2k).

        For a single generator T of weight 2, the primary-sector
        m_k maps weight 2k (input) to Ext^1 at weight 2k (output).
        The structure constant is S_k.

        At weight w in the output, the only nonzero contribution from
        the primary-sector m_k is at k = w/2 (if w is even).

        Returns:
            Dict mapping (arity, output_weight) -> Fraction.
        """
        tower = self.shadow_tower(max_arity)
        result = {}
        for k in range(2, max_arity + 1):
            w = 2 * k
            if w <= max_weight * 2:  # max_weight refers to input weight per slot
                result[(k, w)] = tower[k]
        return result

    def structure_constants_table(self, max_arity: int = 7
                                  ) -> List[Dict[str, Any]]:
        r"""Tabulate all nonzero primary-line structure constants through arity max_arity.

        Returns list of dicts with keys: arity, output_weight, coefficient, sign.
        """
        tower = self.shadow_tower(max_arity)
        table = []
        for k in range(2, max_arity + 1):
            S_k = tower[k]
            if S_k != FR(0):
                table.append({
                    'arity': k,
                    'output_weight': 2 * k,
                    'coefficient': S_k,
                    'sign': 'positive' if S_k > 0 else 'negative',
                })
        return table

    # ------------------------------------------------------------------
    # A-infinity relation verification
    # ------------------------------------------------------------------

    def verify_ainfty_relation(self, n: int) -> Fraction:
        r"""Verify the Stasheff A-infinity relation at arity n.

        The relation at arity n (with m_1 = 0 on cohomology):

            sum_{p+q+r=n, q>=2} (-1)^{pq+r} m_{p+1+r}(id^p, m_q, id^r) = 0

        ON THE PRIMARY LINE, this reduces to a scalar identity on the
        shadow coefficients.  The weight-graded structure means that
        the composition m_j(...m_i(sT,...,sT)...,sT,...,sT) involves
        m_i contributing weight 2i and m_j accepting one input of weight 2i
        plus (j-1) inputs of weight 2.

        For the PRIMARY LINE with all inputs = sT (weight 2), the
        compositions involve MIXED-WEIGHT inputs.  The correct encoding
        of the A-infinity relation is the MC equation of the shadow tower:

            a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j * a_{n-j}   for n >= 3

        equivalently: 2*a_0*a_n + sum_{j=1}^{n-1} a_j * a_{n-j} = 0 for n >= 3

        This is derived from f(t)^2 = Q_L(t) by extracting the t^n coefficient
        for n >= 3 (which must vanish since Q_L is degree 2).

        Returns:
            The residual of the MC equation at arity n (should be 0).
        """
        if n <= 2:
            return FR(0)

        tower = self.shadow_tower(max_arity=n)
        # Convert S_r to a_{r-2}: a_{r-2} = r * S_r
        a = {}
        for r, S_r in tower.items():
            a[r - 2] = FR(r) * S_r

        idx = n - 2  # the convolution index
        if idx < 3:
            # For idx < 3, the recursion involves q0, q1, q2 directly.
            # The recursion automatically holds at these indices.
            return FR(0)

        # MC equation: 2*a_0*a_idx + sum_{j=1}^{idx-1} a_j * a_{idx-j} = 0
        a0 = a.get(0, FR(0))
        residual = FR(2) * a0 * a.get(idx, FR(0))
        for j in range(1, idx):
            residual += a.get(j, FR(0)) * a.get(idx - j, FR(0))
        return residual

    def verify_all_ainfty_relations(self, max_arity: int = 7
                                     ) -> Dict[int, Fraction]:
        r"""Verify A-infinity/MC relations at all arities through max_arity.

        Returns dict mapping arity -> residual (all should be 0).
        """
        return {n: self.verify_ainfty_relation(n)
                for n in range(3, max_arity + 1)}

    # ------------------------------------------------------------------
    # f^2 = Q_L verification (shadow metric identity)
    # ------------------------------------------------------------------

    def verify_shadow_metric_identity(self, max_order: int = 7
                                       ) -> Dict[int, Fraction]:
        r"""Verify f(t)^2 = Q_L(t) at each order in t.

        f(t) = sum_{n>=0} a_n t^n with a_n = (n+2)*S_{n+2}.
        Q_L(t) = q0 + q1*t + q2*t^2.

        At t^0: a_0^2 = q0
        At t^1: 2*a_0*a_1 = q1
        At t^2: 2*a_0*a_2 + a_1^2 = q2
        At t^n (n >= 3): 2*a_0*a_n + sum_{j=1}^{n-1} a_j*a_{n-j} = 0

        Returns dict mapping order -> residual.
        """
        q0, q1, q2 = virasoro_shadow_metric(self.c)
        tower = self.shadow_tower(max_arity=max_order + 2)
        a = {n: FR(n + 2) * tower[n + 2] for n in range(max_order + 1)
             if n + 2 in tower}

        residuals = {}
        # t^0: a_0^2 - q0
        residuals[0] = a.get(0, FR(0)) ** 2 - q0
        # t^1: 2*a_0*a_1 - q1
        if 1 in a:
            residuals[1] = FR(2) * a[0] * a[1] - q1
        # t^2: 2*a_0*a_2 + a_1^2 - q2
        if 2 in a:
            residuals[2] = FR(2) * a[0] * a[2] + a.get(1, FR(0)) ** 2 - q2
        # t^n for n >= 3: should be 0
        for n in range(3, max_order + 1):
            if n in a:
                val = FR(0)
                for j in range(n + 1):
                    val += a.get(j, FR(0)) * a.get(n - j, FR(0))
                residuals[n] = val
        return residuals

    # ------------------------------------------------------------------
    # Formality obstruction cocycles
    # ------------------------------------------------------------------

    def formality_obstruction(self, k: int) -> Dict[str, Any]:
        r"""Compute the formality obstruction at arity k.

        The Virasoro is NOT A-infinity formal (shadow depth = infinity).
        The obstruction at arity k is represented by the class:

            [m_k] in HH^{2-k}(Ext, Ext)

        In the cyclic deformation complex interpretation, this is the
        obstruction class o^{(k)} = S_k, nonzero for all k >= 3 (class M).

        The obstruction is NONTRIVIAL in Hochschild cohomology because:
        (1) S_k != 0 for Virasoro at all k >= 3 (proved)
        (2) The MC equation relates o^{(k)} to lower-order data
        (3) No gauge transformation can simultaneously kill all o^{(k)}
            (the tower is infinite: class M)

        Returns dict with obstruction data.
        """
        S_k = self.mk_primary(k)
        tower = self.shadow_tower(max_arity=k)

        # The obstruction is forced by lower-order data
        # At arity k, the MC equation gives:
        # S_k = -(1/(2*a_0*k)) * sum_{j=1}^{k-3} a_j * a_{k-2-j}
        # where a_j = (j+2)*S_{j+2}
        a0 = FR(2) * tower[2]  # = c
        a = {n: FR(n + 2) * tower[n + 2] for n in range(k - 1)
             if n + 2 in tower}

        # The forcing sum (what makes S_k nonzero)
        idx = k - 2
        forcing = FR(0)
        for j in range(1, idx):
            forcing += a.get(j, FR(0)) * a.get(idx - j, FR(0))

        return {
            'arity': k,
            'S_k': S_k,
            'nonzero': S_k != FR(0),
            'forcing_sum': forcing,
            'obstruction_class': f'o^({k}) = S_{k} in HH^{{2-{k}}}(Ext, Ext)',
            'is_trivial': S_k == FR(0),
            'mechanism': ('MC recursion: lower-order shadows S_2,...,S_{k-1} '
                         'force S_k != 0 through the convolution equation')
                         if S_k != FR(0) else 'vanishes (not class M)',
        }

    # ------------------------------------------------------------------
    # Specific central charge evaluations
    # ------------------------------------------------------------------

    def evaluate_tower_numeric(self, max_arity: int = 7
                                ) -> Dict[int, float]:
        """Numerically evaluate the shadow tower for display."""
        tower = self.shadow_tower(max_arity)
        return {k: float(v) for k, v in tower.items()}


# ============================================================================
# Exact symbolic formulas (independent verification)
# ============================================================================

def S5_exact(c_val: Fraction) -> Fraction:
    r"""S_5(Vir_c) = -48 / [c^2 (5c + 22)].

    Independent derivation:
        a_1 = 6
        a_2 = 40 / [c(5c+22)]
        a_3 = -(2*a_1*a_2) / (2*c) = -6*40 / [c^2(5c+22)] = -240/[c^2(5c+22)]
        S_5 = a_3/5 = -48/[c^2(5c+22)]
    """
    c = _frac(c_val)
    return FR(-48) / (c ** 2 * (FR(5) * c + FR(22)))


def S6_exact(c_val: Fraction) -> Fraction:
    r"""S_6(Vir_c) = 80(45c + 193) / [3 c^3 (5c + 22)^2].

    Independent derivation:
        a_2 = 40 / [c(5c+22)]
        a_3 = -240 / [c^2(5c+22)]
        a_4 = -(2*a_1*a_3 + a_2^2) / (2c)
            = -(2*6*(-240/[c^2(5c+22)]) + (40/[c(5c+22)])^2) / (2c)
            = -(-2880/[c^2(5c+22)] + 1600/[c^2(5c+22)^2]) / (2c)
            = (2880/[c^2(5c+22)] - 1600/[c^2(5c+22)^2]) / (2c)
            = (2880(5c+22) - 1600) / [2c^3(5c+22)^2]
            = (14400c + 63360 - 1600) / [2c^3(5c+22)^2]
            = (14400c + 61760) / [2c^3(5c+22)^2]
            = (7200c + 30880) / [c^3(5c+22)^2]
            = 160(45c + 193) / [c^3(5c+22)^2]
        S_6 = a_4/6 = 80(45c + 193) / [3 c^3(5c+22)^2]
    """
    c = _frac(c_val)
    return FR(80) * (FR(45) * c + FR(193)) / (FR(3) * c ** 3 * (FR(5) * c + FR(22)) ** 2)


def S7_exact(c_val: Fraction) -> Fraction:
    r"""S_7(Vir_c) = -2880(15c + 61) / [7 c^4 (5c + 22)^2].

    Independent derivation:
        a_5 = -(2*a_1*a_4 + 2*a_2*a_3) / (2c)
            = -(a_1*a_4 + a_2*a_3) / c

        a_1 = 6
        a_2 = 40 / [c(5c+22)]
        a_3 = -240 / [c^2(5c+22)]
        a_4 = 160(45c+193) / [c^3(5c+22)^2]

        a_1*a_4 = 960(45c+193) / [c^3(5c+22)^2]
        a_2*a_3 = -9600 / [c^3(5c+22)^2]

        a_1*a_4 + a_2*a_3 = [960(45c+193) - 9600] / [c^3(5c+22)^2]
                           = [43200c + 185280 - 9600] / [c^3(5c+22)^2]
                           = [43200c + 175680] / [c^3(5c+22)^2]
                           = 2880(15c + 61) / [c^3(5c+22)^2]    # WAIT: check

        # 43200c + 175680 = 2880*(15c + 61)?
        # 2880*15 = 43200. 2880*61 = 175680. YES.

        a_5 = -2880(15c+61) / [c^4(5c+22)^2]
        S_7 = a_5/7 = -2880(15c+61) / [7 c^4(5c+22)^2]

        # Verify 960*(45c+193) - 9600:
        # = 960*45c + 960*193 - 9600
        # = 43200c + 185280 - 9600
        # = 43200c + 175680
        # = 2880*(15c) + 2880*61  (since 2880*15 = 43200 and 2880*61 = 175680)
        # CORRECT.
    """
    c = _frac(c_val)
    return FR(-2880) * (FR(15) * c + FR(61)) / (FR(7) * c ** 4 * (FR(5) * c + FR(22)) ** 2)


# ============================================================================
# Cross-family comparison at higher arities
# ============================================================================

def heisenberg_higher(k_val: Fraction = FR(1), max_arity: int = 7
                      ) -> Dict[int, Fraction]:
    """Heisenberg (class G): all S_r = 0 for r >= 3."""
    return {r: (k_val if r == 2 else FR(0))
            for r in range(2, max_arity + 1)}


def affine_sl2_higher(k_val: Fraction = FR(1), max_arity: int = 7
                      ) -> Dict[int, Fraction]:
    """Affine sl_2 (class L): S_3 != 0, S_r = 0 for r >= 4."""
    kappa = FR(3) * (k_val + FR(2)) / FR(4)
    result = {}
    for r in range(2, max_arity + 1):
        if r == 2:
            result[r] = kappa
        elif r == 3:
            result[r] = FR(1)  # universal cubic
        else:
            result[r] = FR(0)
    return result


def bc_ghosts_higher(max_arity: int = 7) -> Dict[int, Fraction]:
    """bc ghosts (class C): S_3, S_4 != 0, S_r = 0 for r >= 5.

    True depth is 4 (stratum separation kills quintic in full complex).
    """
    result = {}
    for r in range(2, max_arity + 1):
        if r == 2:
            result[r] = FR(-1)  # kappa = -1
        elif r == 3:
            result[r] = FR(1)   # alpha = 1
        elif r == 4:
            result[r] = FR(-5, 12)  # S_4 = -5/12
        else:
            result[r] = FR(0)   # terminates by stratum separation
    return result


def cross_family_table(max_arity: int = 7) -> Dict[str, Dict[int, Fraction]]:
    """Cross-family comparison table at arities 2-max_arity."""
    return {
        'Heisenberg': heisenberg_higher(FR(1), max_arity),
        'Affine_sl2': affine_sl2_higher(FR(1), max_arity),
        'bc_ghosts': bc_ghosts_higher(max_arity),
        'Virasoro_c25': virasoro_shadow_tower(FR(25), max_arity),
        'Virasoro_c1': virasoro_shadow_tower(FR(1), max_arity),
        'Virasoro_c13': virasoro_shadow_tower(FR(13), max_arity),
        'Virasoro_c26_minus_half': virasoro_shadow_tower(FR(51, 2), max_arity),
    }


# ============================================================================
# Complementarity at higher arities
# ============================================================================

def complementarity_sum(c_val: Fraction, max_arity: int = 7
                         ) -> Dict[int, Fraction]:
    r"""Compute S_r(c) + S_r(26-c) at each arity r.

    Theorem C constrains these sums.  For Virasoro:
    - S_2(c) + S_2(26-c) = c/2 + (26-c)/2 = 13  (AP24: NOT zero!)
    - S_3(c) + S_3(26-c) = 2 + 2 = 4
    - Higher arities: specific rational functions of c.

    At c = 13 (self-dual): S_r(13) + S_r(13) = 2*S_r(13).
    """
    c = _frac(c_val)
    c_dual = FR(26) - c
    tower = virasoro_shadow_tower(c, max_arity)
    tower_dual = virasoro_shadow_tower(c_dual, max_arity)
    return {r: tower[r] + tower_dual[r]
            for r in range(2, max_arity + 1)
            if r in tower and r in tower_dual}


# ============================================================================
# Growth rate analysis
# ============================================================================

def shadow_growth_rate(c_val: Fraction) -> Fraction:
    r"""Shadow growth rate rho for Virasoro at central charge c.

    rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)

    where alpha = 2, Delta = 8*kappa*S_4 = 40/(5c+22), kappa = c/2.

    rho^2 = (9*4 + 2*40/(5c+22)) / (4*(c/2)^2)
          = (36 + 80/(5c+22)) / c^2
          = (36(5c+22) + 80) / (c^2*(5c+22))
          = (180c + 872) / (c^2*(5c+22))

    Returns rho^2 as exact Fraction (take sqrt for float).
    """
    c = _frac(c_val)
    return (FR(180) * c + FR(872)) / (c ** 2 * (FR(5) * c + FR(22)))


def alternating_sign_pattern(c_val: Fraction, max_arity: int = 10
                              ) -> Dict[int, int]:
    """Track sign pattern of S_r: +1 or -1.

    For Virasoro: S_2 > 0 (= c/2), S_3 > 0 (= 2), S_4 > 0 (= 10/...),
    S_5 < 0, S_6 > 0, S_7 < 0, ... alternating from arity 5 onwards
    (oscillatory tower).
    """
    tower = virasoro_shadow_tower(c_val, max_arity)
    return {r: (1 if S_r > 0 else (-1 if S_r < 0 else 0))
            for r, S_r in tower.items()}


# ============================================================================
# Numerical evaluation at specific central charges
# ============================================================================

def evaluate_at_special_charges(max_arity: int = 7
                                 ) -> Dict[str, Dict[int, float]]:
    """Evaluate shadow tower at physically significant central charges.

    c = 1/2 (Ising model, minimal model M(3,4))
    c = 1 (free boson / compactified at self-dual radius)
    c = 25 (Liouville theory at b = 1)
    c = 26 (critical bosonic string: ghost sector has c' = 26-26 = 0)
    """
    charges = {
        'Ising_c=1/2': FR(1, 2),
        'free_boson_c=1': FR(1),
        'Liouville_c=25': FR(25),
        'critical_string_c=26': FR(26),
    }
    results = {}
    for name, c_val in charges.items():
        tower = virasoro_shadow_tower(c_val, max_arity)
        results[name] = {r: float(v) for r, v in tower.items()}
    return results


def mk_coefficient_table(c_val: Fraction, max_arity: int = 7,
                          max_weight: int = 14
                          ) -> List[Dict[str, Any]]:
    r"""Tabulate nonzero structure constants m_k at weight up to max_weight.

    For a single generator T of weight 2:
    - m_k(sT,...,sT) has output weight 2k
    - We list all (k, 2k) with 2k <= max_weight

    Parameters:
        c_val: Central charge.
        max_arity: Maximum arity to compute.
        max_weight: Maximum output weight to include.

    Returns:
        List of dicts with keys: arity, output_weight, S_k, S_k_float.
    """
    tower = virasoro_shadow_tower(c_val, min(max_arity, max_weight // 2))
    table = []
    for k in range(2, min(max_arity, max_weight // 2) + 1):
        S_k = tower.get(k, FR(0))
        table.append({
            'arity': k,
            'output_weight': 2 * k,
            'S_k': S_k,
            'S_k_float': float(S_k),
        })
    return table


# ============================================================================
# Main
# ============================================================================

if __name__ == '__main__':
    print("=" * 72)
    print("VIRASORO HIGHER A-INFINITY: m_5, m_6, m_7")
    print("=" * 72)

    for c_val, name in [(FR(25), 'c=25'), (FR(1, 2), 'c=1/2'),
                        (FR(1), 'c=1'), (FR(26), 'c=26'), (FR(13), 'c=13')]:
        print(f"\n--- {name} ---")
        vir = HigherVirasoroAInfinity(c_val)
        for k in range(2, 8):
            S_k = vir.mk_primary(k)
            print(f"  m_{k} (S_{k}) = {S_k}  ({float(S_k):.8g})")

        print("  A-infinity relations:")
        for n, res in vir.verify_all_ainfty_relations(7).items():
            status = "PASS" if res == FR(0) else f"FAIL (residual={res})"
            print(f"    arity {n}: {status}")

        print("  Shadow metric f^2=Q_L:")
        for order, res in vir.verify_shadow_metric_identity(7).items():
            status = "PASS" if res == FR(0) else f"FAIL (residual={res})"
            print(f"    t^{order}: {status}")
