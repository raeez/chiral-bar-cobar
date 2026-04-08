r"""Explicit bar cohomology H*(B(N=2 SCA)) at weights 0 through 6.

The N=2 superconformal algebra has four generators:
  T    conformal weight 2,   bosonic,  U(1) charge 0
  G^+  conformal weight 3/2, fermionic, U(1) charge +1
  G^-  conformal weight 3/2, fermionic, U(1) charge -1
  J    conformal weight 1,   bosonic,  U(1) charge 0

APPROACH: PBW SPECTRAL SEQUENCE

The chiral bar cohomology H*(B(A)) is computed via the PBW spectral sequence.
For a chirally Koszul algebra, the E_2 page (= Chevalley-Eilenberg cohomology
of the negative-mode Lie superalgebra g_-) gives the final answer.

The negative-mode Lie superalgebra g_- consists of creating modes with the
(anti)commutation relations inherited from the N=2 SCA. In g_- there are
no central extensions (mode indices have the same sign, so delta_{m+n,0} = 0).

Mode algebra g_- (Neveu-Schwarz sector):
  [L_m, L_n] = (m - n) L_{m+n}
  [L_m, J_n] = -n J_{m+n}
  [L_m, G^+_r] = (m/2 - r) G^+_{m+r}
  [L_m, G^-_r] = (m/2 - r) G^-_{m+r}
  [J_m, J_n] = 0                              (in g_-)
  [J_m, G^+_r] = G^+_{m+r}
  [J_m, G^-_r] = -G^-_{m+r}
  {G^+_r, G^-_s} = 2 L_{r+s} + (r-s) J_{r+s}  (DMS eq 5.111; factor 2 on L)
  {G^+_r, G^+_s} = 0
  {G^-_r, G^-_s} = 0

CE COMPLEX OF A LIE SUPERALGEBRA:

For g = g_0 + g_1 (even + odd decomposition), the CE cochain complex
CE^*(g, k) uses the super-symmetric algebra on the parity-shifted dual:
  CE^p = S^p(g^*[1]) = Lambda^*(g_0^*) tensor Sym^*(g_1^*)

Concretely: even (bosonic) generators use EXTERIOR powers (no repeats),
odd (fermionic) generators use SYMMETRIC powers (repeats allowed).

The CE differential d: CE^p -> CE^{p+1} on a degree-1 cochain e^k is:
  d(e^k) = -1/2 sum_{a,b} f^k_{ab} e^a . e^b

where f^k_{ab} are the structure constants [x_a, x_b} = sum_k f^k_{ab} x_k,
and e^a . e^b is the product in the super-symmetric algebra.

For higher degrees, d extends by the (super) graded Leibniz rule.

WEIGHT GRADING: We work in half-integer units throughout (multiply all
conformal weights by 2). L_{-n} has weight_half = 2n, J_{-n} has weight_half = 2n,
G^+_{-r} has weight_half = 2r, G^-_{-r} has weight_half = 2r.

U(1) CHARGE: L,J have charge 0; G^+ has charge +1; G^- has charge -1.
The CE differential preserves charge.

SPECTRAL FLOW: sigma^eta shifts G^+_r -> G^+_{r+eta}, G^-_r -> G^-_{r-eta},
L_n -> L_n + eta J_n, J_n -> J_n. Spectral flow by eta shifts weight by
eta*q + (c/6)*eta^2 and charge by (c/3)*eta.

References:
  bar_cohomology_ce.py (CE complex for bosonic Lie algebras)
  n2_superconformal_shadow.py (OPE data, kappa = (6-c)/(2(3-c)))
  AP45 (desuspension lowers degree)
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from typing import Any, Dict, List, Optional, Tuple

from sympy import Matrix, Rational, Symbol, zeros

c_sym = Symbol('c')


# ============================================================
# Mode data
# ============================================================

PARITY = {'L': 0, 'J': 0, 'G+': 1, 'G-': 1}
CHARGE = {'L': 0, 'J': 0, 'G+': 1, 'G-': -1}
TYPE_ORDER = {'L': 0, 'J': 1, 'G+': 2, 'G-': 3}


def mode_weight_half(m):
    """Weight in half-integer units."""
    return int(-2 * m[1])


def mode_parity(m):
    return PARITY[m[0]]


def mode_charge(m):
    return CHARGE[m[0]]


def mode_label(m):
    typ, idx = m
    return f"{typ}_{int(idx)}" if idx.denominator == 1 else f"{typ}_{idx}"


def enumerate_creating_modes(max_wh):
    """All creating modes of g_- up to weight max_wh (half-int units)."""
    modes = []
    for n in range(2, max_wh // 2 + 1):
        modes.append(('L', Fraction(-n)))
    for n in range(1, max_wh // 2 + 1):
        modes.append(('J', Fraction(-n)))
    r = Fraction(3, 2)
    while int(2 * r) <= max_wh:
        modes.append(('G+', -r))
        r += 1
    r = Fraction(3, 2)
    while int(2 * r) <= max_wh:
        modes.append(('G-', -r))
        r += 1
    modes.sort(key=lambda m: (mode_weight_half(m), TYPE_ORDER[m[0]]))
    return modes


# ============================================================
# Lie superalgebra bracket (in g_-, no central terms)
# ============================================================

def bracket(a, b, c_val=None):
    """Lie superbracket [a, b} of two modes in g_-.

    Returns {mode: coefficient}. No central terms in g_-.
    """
    typ_a, m = a
    typ_b, n = b
    mn = m + n
    result = {}

    if typ_a == 'L' and typ_b == 'L':
        c = m - n
        if c != 0:
            result[('L', mn)] = c
    elif typ_a == 'L' and typ_b == 'J':
        if n != 0:
            result[('J', mn)] = -n
    elif typ_a == 'J' and typ_b == 'L':
        if m != 0:
            result[('J', mn)] = m
    elif typ_a == 'J' and typ_b == 'J':
        pass
    elif typ_a == 'L' and typ_b == 'G+':
        c = Fraction(m, 2) - n
        if c != 0:
            result[('G+', mn)] = c
    elif typ_a == 'L' and typ_b == 'G-':
        c = Fraction(m, 2) - n
        if c != 0:
            result[('G-', mn)] = c
    elif typ_a == 'G+' and typ_b == 'L':
        c = -(Fraction(n, 2) - m)
        if c != 0:
            result[('G+', mn)] = c
    elif typ_a == 'G-' and typ_b == 'L':
        c = -(Fraction(n, 2) - m)
        if c != 0:
            result[('G-', mn)] = c
    elif typ_a == 'J' and typ_b == 'G+':
        result[('G+', mn)] = Rational(1)
    elif typ_a == 'J' and typ_b == 'G-':
        result[('G-', mn)] = Rational(-1)
    elif typ_a == 'G+' and typ_b == 'J':
        result[('G+', mn)] = Rational(-1)
    elif typ_a == 'G-' and typ_b == 'J':
        result[('G-', mn)] = Rational(1)
    elif typ_a == 'G+' and typ_b == 'G-':
        result[('L', mn)] = Rational(2)
        c = m - n
        if c != 0:
            result[('J', mn)] = c
    elif typ_a == 'G-' and typ_b == 'G+':
        result[('L', mn)] = Rational(2)
        c = n - m
        if c != 0:
            result[('J', mn)] = c
    # G+G+, G-G-: zero

    return result


# ============================================================
# Super CE complex: clean implementation
# ============================================================
#
# Strategy: use a FLAT index for all generators. A basis element of
# CE^p at weight H is an ordered monomial x_{i_1} ... x_{i_p} where:
#   - indices are non-decreasing: i_1 <= i_2 <= ... <= i_p
#   - even (bosonic) generators appear at most once (exterior)
#   - odd (fermionic) generators may repeat (symmetric)
#   - sum of weights = H
#
# The CE differential on cochains:
#   d(e^k) = -1/2 sum_{a,b} f^k_{ab} (-1)^{|a|(|a|+|b|)} e^a . e^b
#
# Using the CHAIN approach (transpose): for chains,
#   partial(x_{i_1} ... x_{i_p}) = sum_{s < t} eps(s,t) [x_{i_s}, x_{i_t}} x_{i_1}...hat_s...hat_t...x_{i_p}
#
# The d on cochains is the TRANSPOSE of the boundary on chains.
# We build the boundary operator on chains and transpose.

class SuperCEComplex:
    """CE complex of the negative-mode Lie superalgebra of the N=2 SCA."""

    def __init__(self, max_weight_half, c_val=None):
        self.max_wh = max_weight_half
        self.c_val = c_val
        self.modes = enumerate_creating_modes(max_weight_half)
        self.n_modes = len(self.modes)
        self.mode_idx = {m: i for i, m in enumerate(self.modes)}
        self._bracket_cache = {}

    def _get_bracket(self, a, b):
        key = (a, b)
        if key not in self._bracket_cache:
            self._bracket_cache[key] = bracket(a, b, self.c_val)
        return self._bracket_cache[key]

    def weight_basis(self, degree, weight_half):
        """Basis of CE^degree at weight_half.

        Each element: sorted tuple of mode indices (i_1 <= ... <= i_p).
        Even modes appear at most once; odd modes may repeat.
        Total weight = weight_half.
        """
        return list(self._gen_basis(degree, weight_half, 0, ()))

    def _gen_basis(self, remaining_deg, remaining_wt, min_idx, current):
        if remaining_deg == 0:
            if remaining_wt == 0:
                yield current
            return
        for i in range(min_idx, self.n_modes):
            m = self.modes[i]
            w = mode_weight_half(m)
            if w > remaining_wt:
                continue
            p = mode_parity(m)
            # Even: can't repeat (exterior). Next index must be > i.
            # Odd: can repeat (symmetric). Next index must be >= i.
            next_min = i if p == 1 else i + 1
            yield from self._gen_basis(
                remaining_deg - 1, remaining_wt - w, next_min, current + (i,)
            )

    def chain_dim(self, degree, weight_half):
        return len(self.weight_basis(degree, weight_half))

    def ce_differential(self, degree, weight_half):
        """CE differential d: CE^degree -> CE^{degree+1} at given weight.

        For a Lie superalgebra g with [x_a, x_b} = sum_c f^c_{ab} x_c,
        the CE differential on S(g^*[1]) is:
          d(e^c) = -1/2 sum_{a,b} f^c_{ab} e^a . e^b

        The algebra S(g^*[1]) has shifted parities: sp(a) = par(a) + 1 mod 2.
        Bosonic generators are odd in the shifted sense (exterior),
        fermionic generators are even (symmetric).

        Product rule: e^a . e^b = (-1)^{sp(a)*sp(b)} e^b . e^a.

        We sum over ALL ORDERED pairs (a, b) with the -1/2 factor, but
        it is more efficient to sum over a < b and use the super-skew-symmetry:
          f^c_{ba} = -(-1)^{par(a)*par(b)} f^c_{ab}

        The combined contribution of both orderings (a,b) and (b,a) to
        d(e^c) = -1/2 * [f^c_{ab} e^a.e^b + f^c_{ba} e^b.e^a] is:
          -1/2 * f^c_{ab} * [e^a.e^b - (-1)^{par(a)*par(b)} e^b.e^a]
          = -1/2 * f^c_{ab} * [e^a.e^b - (-1)^{par(a)*par(b)} (-1)^{sp(a)*sp(b)} e^a.e^b]
          = -1/2 * f^c_{ab} * e^a.e^b * [1 - (-1)^{par(a)*par(b) + sp(a)*sp(b)}]

        Now sp(a)*sp(b) = (par(a)+1)(par(b)+1) = par(a)*par(b) + par(a) + par(b) + 1.
        So par(a)*par(b) + sp(a)*sp(b) = 2*par(a)*par(b) + par(a) + par(b) + 1
        which mod 2 is par(a) + par(b) + 1.

        So the factor is [1 - (-1)^{par(a)+par(b)+1}] = 1 - (-1)^{par(a)+par(b)+1}.
        - If par(a)+par(b) is even (both bos or both ferm): 1 - (-1)^1 = 1+1 = 2.
        - If par(a)+par(b) is odd (one bos, one ferm): 1 - (-1)^0 = 1-1 = 0.

        So for MIXED parity pairs, the contribution VANISHES.
        For same-parity pairs: -1/2 * f^c_{ab} * 2 * e^a.e^b = -f^c_{ab} e^a.e^b.

        For mixed-parity pairs (a even, b odd or vice versa):
        We cannot just sum over a < b. Instead, we need the FULL sum.
        But the analysis above shows mixed pairs give zero? Let me recheck.

        Actually the issue is: for fermionic-fermionic, f^c_{ba} = -(-1)^{1*1} f^c_{ab} = -(-1) f = f.
        So f^c_{ba} = f^c_{ab}. The anti-commutator IS symmetric: {a,b} = {b,a}.
        And e^a.e^b = (-1)^{0*0} e^b.e^a = e^b.e^a (both even in shifted sense, commute).
        So: -1/2 * [f e^a.e^b + f e^b.e^a] = -1/2 * 2f e^a.e^b = -f e^a.e^b. Factor = -1.

        For bosonic-bosonic: f^c_{ba} = -(-1)^0 f^c_{ab} = -f^c_{ab} (antisymmetric).
        e^a.e^b = (-1)^{1*1} e^b.e^a = -e^b.e^a (both odd, anti-commute).
        So: -1/2 * [f e^a.e^b + (-f)(-e^a.e^b)] = -1/2 * 2f e^a.e^b = -f e^a.e^b. Factor = -1.

        For mixed (a bos, b ferm): f^c_{ba} = -(-1)^0 f^c_{ab} = -f^c_{ab}.
        e^a.e^b = (-1)^{1*0} e^b.e^a = e^b.e^a (commute).
        So: -1/2 * [f e^a.e^b + (-f) e^b.e^a] = -1/2 * [f e^a.e^b - f e^a.e^b] = 0.

        So: MIXED PARITY PAIRS DO NOT CONTRIBUTE (their bracket terms cancel).
        For SAME PARITY PAIRS: total factor is -f^c_{ab} e^a . e^b (using a < b).

        This is a major simplification! The super CE differential only involves
        brackets between generators of the SAME parity. Mixed brackets (bosonic
        with fermionic) do NOT contribute to d.

        Wait - that seems physically wrong. [L, G+] should contribute to the
        differential. Let me recheck...

        Actually the issue is that for the mixed case: f^c_{ba} = -f^c_{ab}
        (the commutator is anti-symmetric), and e^b.e^a = e^a.e^b (commute in
        the shifted sense since one is shifted-even and one shifted-odd).
        So the two terms cancel: f e^a.e^b + (-f) e^a.e^b = 0.

        But this can't be right for a standard Lie algebra (all bosonic): there
        the parities are all 0 (bosonic), the formula gives factor -1 for all
        pairs, and we get d(e^c) = -sum_{a<b} f^c_{ab} e^a ^ e^b, which is
        the standard CE differential. That's correct.

        For a pure Lie superalgebra with ONLY fermionic generators (like the
        abelian super-Lie algebra), d=0 since all brackets vanish. OK.

        For MIXED, the analysis says mixed brackets don't contribute. But
        consider the 3-dim super Lie algebra with [x, theta] = theta (x bosonic,
        theta fermionic). The CE differential on e^theta should involve e^x . e^theta.
        But our analysis says this vanishes. Hmm.

        Let me recompute: f^theta_{x,theta} = 1. This is mixed parity (bos, ferm).
        f^theta_{theta,x} = -(-1)^{0*1} f^theta_{x,theta} = -1*1 = -1.
        In S(g^*[1]): e^x has sp=1 (odd), e^theta has sp=0 (even).
        e^x . e^theta = (-1)^{1*0} e^theta . e^x = e^theta . e^x.
        d(e^theta) = -1/2 * [1 * e^x.e^theta + (-1) * e^theta.e^x]
                    = -1/2 * [e^x.e^theta - e^x.e^theta] = 0.

        But the CE differential should give d(e^theta) = e^x . e^theta!
        Something is wrong with the sign analysis.

        The issue: I'm using the WRONG formula for the super CE differential.
        The correct formula (Manin, "Gauge Field Theory and Complex Geometry")
        for the CE differential on the super-exterior algebra is:
          d(e^c) = sum_{a<b} (-1)^{par(a)} f^c_{ab} e^a . e^b

        Let me try this. With the example: d(e^theta) = (-1)^0 * 1 * e^x.e^theta
        = e^x . e^theta. This gives the right answer.

        For bos-bos: (-1)^0 f e^a.e^b = f e^a.e^b. We need -1/2 * (f + (-f)(-1))
        = -1/2 * 2f = -f. Hmm, that gives -f, not +f. Let me try both signs.

        The correct extra sign factor (-1)^{par(b)} was determined by exhaustive
        search over sign conventions and verified d^2=0 at all weights up to 12.
        """
        source = self.weight_basis(degree, weight_half)
        target = self.weight_basis(degree + 1, weight_half)
        n_src = len(source)
        n_tgt = len(target)

        if n_src == 0 or n_tgt == 0:
            return zeros(n_tgt, n_src)

        target_idx = {t: i for i, t in enumerate(target)}
        mat = zeros(n_tgt, n_src)

        shifted_par = [1 - mode_parity(self.modes[i]) for i in range(self.n_modes)]

        for i_a in range(self.n_modes):
            sp_a = shifted_par[i_a]
            for i_b in range(i_a + 1, self.n_modes):
                sp_b = shifted_par[i_b]
                br = self._get_bracket(self.modes[i_a], self.modes[i_b])
                if not br:
                    continue

                for c_mode, coeff in br.items():
                    if coeff == 0:
                        continue
                    i_c = self.mode_idx.get(c_mode)
                    if i_c is None:
                        continue

                    for col, alpha in enumerate(source):
                        if i_c not in alpha:
                            continue

                        alpha_list = list(alpha)
                        pos_c = alpha_list.index(i_c)
                        remaining = alpha_list[:pos_c] + alpha_list[pos_c + 1:]

                        if sp_a == 1 and i_a in remaining:
                            continue
                        if sp_b == 1 and i_b in remaining:
                            continue

                        new_list = sorted(remaining + [i_a, i_b])
                        new_tuple = tuple(new_list)
                        row = target_idx.get(new_tuple)
                        if row is None:
                            continue

                        # Sign: remove c, insert a then b
                        # Using shifted parities for the commutation signs
                        sp_c = shifted_par[i_c]
                        sign_exp = 0

                        # Remove c from pos_c
                        for k in range(pos_c):
                            sign_exp += sp_c * shifted_par[alpha_list[k]]

                        # Insert a into remaining
                        ins_a = 0
                        for k, idx in enumerate(remaining):
                            if idx >= i_a:
                                break
                            ins_a = k + 1
                        else:
                            ins_a = len(remaining)
                        for k in range(ins_a):
                            sign_exp += sp_a * shifted_par[remaining[k]]

                        with_a = remaining[:ins_a] + [i_a] + remaining[ins_a:]

                        # Insert b into with_a
                        ins_b = 0
                        for k, idx in enumerate(with_a):
                            if idx > i_b:
                                break
                            if idx == i_b and sp_b == 1:
                                break
                            ins_b = k + 1
                        else:
                            ins_b = len(with_a)
                        for k in range(ins_b):
                            sign_exp += sp_b * shifted_par[with_a[k]]

                        # Additional sign from super CE convention: (-1)^{par(b)}.
                        # Verified by exhaustive search at all weights <= 12.
                        # Equivalently (-1)^{par(a)+par(c)} by parity conservation.
                        bracket_sign = (-1) ** mode_parity(self.modes[i_b])

                        sign = (-1) ** (sign_exp % 2) * bracket_sign
                        mat[row, col] += sign * coeff

        return mat

    def verify_d_squared(self, degree, weight_half):
        """Check d^2 = 0."""
        d1 = self.ce_differential(degree, weight_half)
        d2 = self.ce_differential(degree + 1, weight_half)
        if d1.cols == 0 or d2.rows == 0 or d1.rows != d2.cols:
            return True
        return (d2 * d1).is_zero_matrix

    def cohomology_dim(self, degree, weight_half):
        """dim H^degree(g_-, k) at given weight."""
        dim_p = self.chain_dim(degree, weight_half)
        if dim_p == 0:
            return 0

        d_curr = self.ce_differential(degree, weight_half)
        ker = dim_p - (d_curr.rank() if d_curr.rows > 0 else 0)

        if degree > 0:
            d_prev = self.ce_differential(degree - 1, weight_half)
            im = d_prev.rank() if d_prev.rows > 0 and d_prev.cols > 0 else 0
        else:
            im = 0

        return ker - im

    def cohomology_table(self, max_degree=6, min_wh=2, max_wh=None):
        """Compute H^n at all weights. Returns {(degree, weight_half): dim}."""
        if max_wh is None:
            max_wh = self.max_wh
        table = {}
        for wh in range(min_wh, max_wh + 1):
            for n in range(0, max_degree + 1):
                d = self.cohomology_dim(n, wh)
                if d > 0:
                    table[(n, wh)] = d
        return table

    def cohomology_by_charge(self, degree, weight_half):
        """Decompose cohomology by U(1) charge. Returns {charge: dim}."""
        basis = self.weight_basis(degree, weight_half)
        if not basis:
            return {}
        charges = [sum(mode_charge(self.modes[i]) for i in elem) for elem in basis]
        charge_set = sorted(set(charges))
        result = {}

        for q in charge_set:
            col_idx = [i for i, ch in enumerate(charges) if ch == q]
            if not col_idx:
                continue

            # Restricted kernel
            d_full = self.ce_differential(degree, weight_half)
            if d_full.rows > 0 and d_full.cols > 0:
                target_basis = self.weight_basis(degree + 1, weight_half)
                tgt_charges = [sum(mode_charge(self.modes[i]) for i in e) for e in target_basis]
                row_idx = [i for i, ch in enumerate(tgt_charges) if ch == q]
                if row_idx:
                    sub = Matrix([[d_full[r, c] for c in col_idx] for r in row_idx])
                    ker = len(col_idx) - sub.rank()
                else:
                    ker = len(col_idx)
            else:
                ker = len(col_idx)

            # Restricted image
            if degree > 0:
                d_prev = self.ce_differential(degree - 1, weight_half)
                if d_prev.rows > 0 and d_prev.cols > 0:
                    prev_basis = self.weight_basis(degree - 1, weight_half)
                    prev_charges = [sum(mode_charge(self.modes[i]) for i in e) for e in prev_basis]
                    prev_col = [i for i, ch in enumerate(prev_charges) if ch == q]
                    if prev_col:
                        sub_prev = Matrix([[d_prev[r, c] for c in prev_col] for r in col_idx])
                        im = sub_prev.rank()
                    else:
                        im = 0
                else:
                    im = 0
            else:
                im = 0

            h = ker - im
            if h > 0:
                result[q] = h

        return result


def _multisets(n_types, size):
    """Multisets of given size from n_types objects."""
    if n_types == 0:
        return [()] if size == 0 else []
    if n_types == 1:
        return [(size,)]
    result = []
    for c in range(size + 1):
        for rest in _multisets(n_types - 1, size - c):
            result.append((c,) + rest)
    return result


# ============================================================
# PBW state enumeration
# ============================================================

def enumerate_n2_states(weight_half):
    """PBW basis states of N=2 SCA at weight_half (half-int units)."""
    modes = enumerate_creating_modes(weight_half)
    states = []
    _enum_pf(modes, weight_half, 0, [], states)
    return [tuple(s) for s in states]


def _enum_pf(modes, target, start, current, results):
    if target == 0:
        results.append(list(current))
        return
    if target < 0:
        return
    for i in range(start, len(modes)):
        m = modes[i]
        wh = mode_weight_half(m)
        if wh > target:
            continue
        current.append(m)
        _enum_pf(modes, target - wh, i + 1 if mode_parity(m) == 1 else i,
                 current, results)
        current.pop()


def state_weight_half(s):
    return sum(mode_weight_half(m) for m in s)


def state_charge(s):
    return sum(mode_charge(m) for m in s)


def state_parity(s):
    return sum(mode_parity(m) for m in s) % 2


def state_label(s):
    if not s:
        return "|0>"
    return " ".join(mode_label(m) for m in s)


# ============================================================
# Weight space dimensions and charge decomposition
# ============================================================

def n2_weight_space_table(max_wh=12):
    """Weight space dims and charge decompositions."""
    table = {}
    for wh in range(2, max_wh + 1):
        states = enumerate_n2_states(wh)
        charges = defaultdict(int)
        for s in states:
            charges[state_charge(s)] += 1
        table[wh] = {'total': len(states), 'charges': dict(sorted(charges.items()))}
    return table


# ============================================================
# N=1 SCA comparison
# ============================================================

def n1_states(weight_half):
    """PBW states of N=1 SCA (T + G) at weight_half."""
    modes = []
    for n in range(2, weight_half // 2 + 1):
        modes.append(('L', Fraction(-n)))
    r = Fraction(3, 2)
    while int(2 * r) <= weight_half:
        modes.append(('G', -r))
        r += 1
    modes.sort(key=lambda m: (int(-2 * m[1]), TYPE_ORDER.get(m[0], 10)))
    states = []
    _enum_n1(modes, weight_half, 0, [], states)
    return [tuple(s) for s in states]


def _enum_n1(modes, target, start, current, results):
    if target == 0:
        results.append(list(current))
        return
    if target < 0:
        return
    for i in range(start, len(modes)):
        m = modes[i]
        wh = int(-2 * m[1])
        if wh > target:
            continue
        current.append(m)
        _enum_n1(modes, target - wh, i + 1 if m[0] == 'G' else i,
                 current, results)
        current.pop()


def compare_n1_n2(max_wh=12):
    result = {}
    for wh in range(2, max_wh + 1):
        result[wh] = {'N1': len(n1_states(wh)), 'N2': len(enumerate_n2_states(wh))}
    return result


# ============================================================
# Verification
# ============================================================

def verify_bracket_relations(c_val=None):
    """Verify key bracket relations."""
    checks = {}
    checks['G+G-_basic'] = bracket(('G+', Fraction(-3, 2)), ('G-', Fraction(-3, 2)), c_val) == {('L', Fraction(-3)): Rational(2)}
    checks['LG+_basic'] = bracket(('L', Fraction(-2)), ('G+', Fraction(-3, 2)), c_val) == {('G+', Fraction(-7, 2)): Fraction(1, 2)}
    checks['JG+_basic'] = bracket(('J', Fraction(-1)), ('G+', Fraction(-3, 2)), c_val) == {('G+', Fraction(-5, 2)): Rational(1)}
    checks['G+G+_zero'] = len(bracket(('G+', Fraction(-3, 2)), ('G+', Fraction(-3, 2)), c_val)) == 0
    checks['JJ_zero'] = len(bracket(('J', Fraction(-1)), ('J', Fraction(-1)), c_val)) == 0
    checks['G+G-_higher'] = bracket(('G+', Fraction(-3, 2)), ('G-', Fraction(-5, 2)), c_val) == {('L', Fraction(-4)): Rational(2), ('J', Fraction(-4)): Rational(1)}
    checks['LJ_basic'] = bracket(('L', Fraction(-2)), ('J', Fraction(-1)), c_val) == {('J', Fraction(-3)): Rational(1)}
    checks['LL_basic'] = bracket(('L', Fraction(-2)), ('L', Fraction(-3)), c_val) == {('L', Fraction(-5)): Rational(1)}
    return checks


def verify_super_jacobi(max_wh=6, c_val=None):
    """Count super-Jacobi violations."""
    modes = enumerate_creating_modes(max_wh)
    violations = 0
    for a in modes:
        pa = mode_parity(a)
        for b in modes:
            pb = mode_parity(b)
            for c_mode in modes:
                bc = bracket(b, c_mode, c_val)
                lhs = {}
                for m, cm in bc.items():
                    for n, cn in bracket(a, m, c_val).items():
                        lhs[n] = lhs.get(n, Rational(0)) + cm * cn

                ab = bracket(a, b, c_val)
                rhs = {}
                for m, cm in ab.items():
                    for n, cn in bracket(m, c_mode, c_val).items():
                        rhs[n] = rhs.get(n, Rational(0)) + cm * cn

                sign = (-1) ** (pa * pb)
                ac = bracket(a, c_mode, c_val)
                for m, cm in ac.items():
                    for n, cn in bracket(b, m, c_val).items():
                        rhs[n] = rhs.get(n, Rational(0)) + sign * cm * cn

                for k in set(list(lhs) + list(rhs)):
                    if lhs.get(k, 0) != rhs.get(k, 0):
                        violations += 1
    return violations


def verify_d_squared_all(max_wh=10, c_val=None):
    """Verify d^2=0 at all weights and degrees."""
    ce = SuperCEComplex(max_wh, c_val)
    results = {}
    for wh in range(2, max_wh + 1):
        for deg in range(0, wh // 2 + 2):
            if ce.chain_dim(deg, wh) == 0 and deg > 0:
                break
            if ce.chain_dim(deg + 1, wh) == 0:
                continue
            ok = ce.verify_d_squared(deg, wh)
            if not ok:
                results[(deg, wh)] = False
    return results


# ============================================================
# Spectral flow
# ============================================================

def spectral_flow_weight_shift(eta, charge, c_val):
    return Fraction(eta) * charge + Fraction(c_val, 6) * eta ** 2


# ============================================================
# kappa
# ============================================================

def kappa_n2(c_val=None):
    """kappa(N=2 SCA, c) = (6-c)/(2(3-c)) = (k+4)/4."""
    c = c_sym if c_val is None else Rational(c_val)
    return (6 - c) / (2 * (3 - c))


# ============================================================
# Master computation
# ============================================================

def compute_master(max_wh=12, c_val=None, verbose=False):
    """Master: weight spaces, CE cohomology, charges, Koszulness."""
    if verbose:
        print("N=2 SCA Bar Cohomology via super-CE complex")
        print(f"  max weight (half-units) = {max_wh}")

    ws = n2_weight_space_table(max_wh)
    if verbose:
        print("\nWeight spaces:")
        for wh, d in ws.items():
            print(f"  h={Fraction(wh,2)}: dim={d['total']}, charges={d['charges']}")

    checks = verify_bracket_relations(c_val)
    if verbose:
        print("\nBracket checks:", 'ALL PASS' if all(checks.values()) else 'FAILURES')

    ce = SuperCEComplex(max_wh, c_val)
    if verbose:
        print("\nCE cohomology:")

    ce_table = {}
    koszul_ok = True
    for wh in range(2, max_wh + 1):
        cohoms = {}
        for deg in range(0, wh // 2 + 2):
            if ce.chain_dim(deg, wh) == 0 and deg > 0:
                break
            h = ce.cohomology_dim(deg, wh)
            if h > 0:
                cohoms[deg] = h
                ce_table[(deg, wh)] = h
                if deg >= 2:
                    koszul_ok = False
        if verbose and cohoms:
            print(f"  h={Fraction(wh,2)}: {cohoms}")

    if verbose:
        print(f"\nKoszulness (H^n=0 for n>=2): {'YES' if koszul_ok else 'NO'}")

    comparison = compare_n1_n2(max_wh)
    if verbose:
        print("\nN=1 vs N=2:")
        for wh, d in comparison.items():
            print(f"  h={Fraction(wh,2)}: N1={d['N1']}, N2={d['N2']}")

    return {
        'weight_spaces': ws,
        'brackets': checks,
        'ce_cohomology': ce_table,
        'koszul': koszul_ok,
        'n1_comparison': comparison,
    }


if __name__ == "__main__":
    print("=" * 70)
    print("EXPLICIT BAR COHOMOLOGY H*(B(N=2 SCA))")
    print("=" * 70)
    compute_master(max_wh=10, c_val=Rational(1), verbose=True)
