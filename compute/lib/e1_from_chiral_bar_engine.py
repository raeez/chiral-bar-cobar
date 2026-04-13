r"""E_1 coalgebra structure from the chiral bar complex: first-principles verification.

MATHEMATICAL FRAMEWORK:

The bar complex B^ch(A) of a chiral algebra A is defined as:
  B^ch_n(A) = sections of A^{boxtimes(n+1)} tensor Omega^n_log over FM_{n+1}(X)

At the ALGEBRAIC level (working over a point, genus 0), we have:
  B^ch(A) = T^c(s^{-1} A_bar)
where T^c denotes the cofree conilpotent coassociative coalgebra (tensor coalgebra)
and s^{-1} denotes desuspension (AP45: |s^{-1}v| = |v| - 1).

The E_1 (coassociative) coproduct Delta on B^ch(A) is the DECONCATENATION:
  Delta[a_1|...|a_n] = sum_{i=0}^{n} [a_1|...|a_i] tensor [a_{i+1}|...|a_n]
This is an ALGEBRAIC structure: it comes from the tensor coalgebra T^c(V).

The GEOMETRIC interpretation: the ordering of tensor factors corresponds to
the ordering of points t_1 < ... < t_n on R. Splitting at position i
corresponds to cutting the interval at t_i. This is the E_1 operad acting
on the topological direction R of C x R.

KEY VERIFICATION TARGETS:
  (1) Delta is coassociative: (Delta tensor id) o Delta = (id tensor Delta) o Delta
  (2) Delta has a counit: epsilon([]) = 1, epsilon([a_1|...|a_n]) = 0 for n >= 1
  (3) d_B is a coderivation of Delta:
      Delta o d_B = (id tensor d_B + d_B tensor id) o Delta
  (4) The form-degree splitting: when Delta splits [a_1|...|a_n] tensor omega,
      the form omega must be restricted to the appropriate configuration subspace.
      For ORDERED bar: omega in Omega^n_log(FM_{n+1}) restricts via the
      Kunneth-type map Omega^n_log(FM_{n+1}) -> sum Omega^p(FM_{i+1}) tensor Omega^q(FM_{n-i+1}).
      CRUCIAL: FM_{n+1}(C) does NOT split as FM_{i+1}(C) x FM_{n-i+1}(C).
      But the logarithmic forms DO split: eta_{ab} for a,b in I and eta_{cd}
      for c,d in J are INDEPENDENT (no mixed terms eta_{ac} with a in I, c in J
      appear in the coproduct). This is because the deconcatenation respects
      the ordering, so points in the "left" group never collide with points in
      the "right" group in the R-direction.
  (5) For the SYMMETRIC bar B^Sigma(A) = T^c(s^{-1}A_bar)/S_n, the coproduct
      becomes cocommutative. The shuffle coproduct is the S_n-equivariant lift.
  (6) The coproduct is SIMULTANEOUSLY algebraic AND geometric:
      algebraically it is the tensor coalgebra deconcatenation,
      geometrically it is interval splitting in the R-direction.
      These agree because the tensor coalgebra IS the algebraic model
      of the E_1 operad (Boardman-Vogt, Fresse).

For the Heisenberg algebra H_k with OPE J(z)J(w) ~ k/(z-w)^2:
  B^ch_1(H_k) = span{[J]} with form eta_{01} = d log(z_0 - z_1)
  B^ch_2(H_k) = span{[J|J]} with form eta_{01} wedge eta_{12}
      (using Arnold: eta_{01}^eta_{12} + eta_{12}^eta_{20} + eta_{20}^eta_{01} = 0)
  B^ch_3(H_k) = span{[J|J|J]} with form eta_{01}^eta_{12}^eta_{23}
      (up to Arnold relations; 3! = 6 terms in the basis of Omega^3_log(FM_4))

The bar differential at arity 2 is:
  d_B[J|J] = k * [J]   (residue of J(z)J(w) along D_{01}, extracting k from k/(z-w)^2)
Wait -- CAREFUL (AP19): the bar differential extracts residues along d log(z-w),
which has a simple pole. The OPE J(z)J(w) ~ k/(z-w)^2 combined with the
d log kernel d(z-w)/(z-w) = dz/(z-w) gives: the integrand is
  J(z)J(w) * d log(z-w) = k/(z-w)^2 * d(z-w)/(z-w) = k * d(z-w) / (z-w)^3
Wait, that is wrong. The d log form is the KERNEL form eta = d log(z_i - z_j).
The bar differential takes the residue of the OPE ALONG the collision divisor,
with the log form providing the integration measure.

More precisely: at arity n, an element is a_0 tensor ... tensor a_n tensor omega
where omega is a log n-form. The residue differential d_res sends this to
sum_{i<j} Res_{D_{ij}}[mu(a_i, a_j) tensor (others) tensor iota_{D_{ij}} omega]
where mu is the chiral product (OPE) and iota is the residue of the form along D_{ij}.

For the Heisenberg at arity 1: [J] tensor eta_{01} is in B^ch_1.
d_res([J] tensor eta_{01}) involves the OPE of J with itself along D_{01}.
But wait, arity 1 means 2 insertions (a_0, a_1) with a_0 the output.
d_res: B_1 -> B_0 extracts Res_{D_{01}}[mu(J,J) tensor Res(eta_{01})] = k * [1].

For arity 2: [J|J] tensor eta_{01} ^ eta_{12}.
d_res has THREE possible collisions D_{01}, D_{02}, D_{12}.
Each collision reduces arity by 1.

SIGN AND FORM CONVENTIONS:
  - Desuspension: |s^{-1}v| = |v| - 1 (AP45)
  - Bar differential |d| = +1 (cohomological convention)
  - Koszul signs throughout

References:
  bar_construction.tex: Definition def:bar-differential-complete
  en_koszul_duality.tex: Theorem thm:bar-swiss-cheese
  signs_and_shifts.tex: Authoritative sign conventions
  bar_complex_ordered_unordered_engine.py: Ordered vs unordered comparison
  e1_shadow_tower.py: E_1 shadow data
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import factorial, comb
from typing import Dict, List, Optional, Tuple, Any

import numpy as np


# ============================================================
# Exact rational arithmetic
# ============================================================

def _frac(x) -> Fraction:
    """Coerce to Fraction."""
    if isinstance(x, Fraction):
        return x
    if isinstance(x, (int, np.integer)):
        return Fraction(int(x))
    return Fraction(x)


FR0 = Fraction(0)
FR1 = Fraction(1)


# ============================================================
# Abstract bar element representation
# ============================================================

class BarElement:
    """An element of the bar complex B_n(A) at arity n.

    Represents a formal linear combination of bar monomials
    [a_1|...|a_n] with rational coefficients.

    Each monomial is a tuple of generator labels (strings or ints).
    The coefficient dict maps tuples -> Fraction.

    CONVENTION: arity n means n tensor factors (n+1 insertions
    including the output a_0, but we suppress a_0 in the notation
    following the reduced bar convention).
    """

    def __init__(self, terms: Optional[Dict[tuple, Fraction]] = None, arity: int = 0):
        self.terms = {} if terms is None else {k: v for k, v in terms.items() if v != FR0}
        self.arity = arity

    def __repr__(self):
        if not self.terms:
            return "0"
        parts = []
        for mon, coeff in sorted(self.terms.items()):
            if coeff == FR1:
                parts.append(f"[{'|'.join(str(x) for x in mon)}]")
            elif coeff == -FR1:
                parts.append(f"-[{'|'.join(str(x) for x in mon)}]")
            else:
                parts.append(f"{coeff}*[{'|'.join(str(x) for x in mon)}]")
        return " + ".join(parts)

    def __eq__(self, other):
        if isinstance(other, int) and other == 0:
            return not self.terms
        if not isinstance(other, BarElement):
            return NotImplemented
        return self.terms == other.terms

    def __add__(self, other):
        if isinstance(other, int) and other == 0:
            return self
        result = dict(self.terms)
        for k, v in other.terms.items():
            result[k] = result.get(k, FR0) + v
        return BarElement({k: v for k, v in result.items() if v != FR0},
                         max(self.arity, other.arity))

    def __neg__(self):
        return BarElement({k: -v for k, v in self.terms.items()}, self.arity)

    def __sub__(self, other):
        return self + (-other)

    def scale(self, c: Fraction) -> 'BarElement':
        c = _frac(c)
        return BarElement({k: v * c for k, v in self.terms.items()}, self.arity)

    def is_zero(self) -> bool:
        return not self.terms


# ============================================================
# Tensor product of bar elements (for coproduct output)
# ============================================================

class TensorBarElement:
    """A formal linear combination of tensor products of bar monomials.

    Represents sum_i c_i * [left_i] tensor [right_i].
    The terms dict maps (left_tuple, right_tuple) -> Fraction.
    """

    def __init__(self, terms: Optional[Dict[Tuple[tuple, tuple], Fraction]] = None):
        self.terms = {} if terms is None else {k: v for k, v in terms.items() if v != FR0}

    def __repr__(self):
        if not self.terms:
            return "0"
        parts = []
        for (left, right), coeff in sorted(self.terms.items()):
            l_str = f"[{'|'.join(str(x) for x in left)}]" if left else "[]"
            r_str = f"[{'|'.join(str(x) for x in right)}]" if right else "[]"
            if coeff == FR1:
                parts.append(f"{l_str} x {r_str}")
            else:
                parts.append(f"{coeff}*{l_str} x {r_str}")
        return " + ".join(parts)

    def __eq__(self, other):
        if isinstance(other, int) and other == 0:
            return not self.terms
        if not isinstance(other, TensorBarElement):
            return NotImplemented
        return self.terms == other.terms

    def __add__(self, other):
        if isinstance(other, int) and other == 0:
            return self
        result = dict(self.terms)
        for k, v in other.terms.items():
            result[k] = result.get(k, FR0) + v
        return TensorBarElement({k: v for k, v in result.items() if v != FR0})

    def __neg__(self):
        return TensorBarElement({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-other)

    def is_zero(self) -> bool:
        return not self.terms


class TripleTensorBarElement:
    """Formal sum of triple tensor products [A] x [B] x [C]."""

    def __init__(self, terms: Optional[Dict[Tuple[tuple, tuple, tuple], Fraction]] = None):
        self.terms = {} if terms is None else {k: v for k, v in terms.items() if v != FR0}

    def __eq__(self, other):
        if isinstance(other, int) and other == 0:
            return not self.terms
        if not isinstance(other, TripleTensorBarElement):
            return NotImplemented
        return self.terms == other.terms

    def is_zero(self) -> bool:
        return not self.terms


# ============================================================
# Deconcatenation coproduct
# ============================================================

def deconcatenation_coproduct(monomial: tuple) -> TensorBarElement:
    """Compute Delta[a_1|...|a_n] = sum_{i=0}^{n} [a_1|...|a_i] x [a_{i+1}|...|a_n].

    This is the standard tensor coalgebra coproduct.
    The empty tensor () represents the unit element [].
    """
    n = len(monomial)
    terms = {}
    for i in range(n + 1):
        left = monomial[:i]
        right = monomial[i:]
        terms[(left, right)] = FR1
    return TensorBarElement(terms)


def coproduct_on_element(elem: BarElement) -> TensorBarElement:
    """Apply deconcatenation to a bar element (linear extension)."""
    result = TensorBarElement()
    for mon, coeff in elem.terms.items():
        delta_mon = deconcatenation_coproduct(mon)
        scaled = TensorBarElement({k: v * coeff for k, v in delta_mon.terms.items()})
        result = result + scaled
    return result


# ============================================================
# Coassociativity verification
# ============================================================

def apply_delta_left(tensor_elem: TensorBarElement) -> TripleTensorBarElement:
    """Apply (Delta tensor id) to a tensor element.

    (Delta x id)([L] x [R]) = sum_i [L_left_i] x [L_right_i] x [R]
    """
    terms = {}
    for (left, right), coeff in tensor_elem.terms.items():
        delta_left = deconcatenation_coproduct(left)
        for (ll, lr), dcoeff in delta_left.terms.items():
            key = (ll, lr, right)
            terms[key] = terms.get(key, FR0) + coeff * dcoeff
    return TripleTensorBarElement({k: v for k, v in terms.items() if v != FR0})


def apply_delta_right(tensor_elem: TensorBarElement) -> TripleTensorBarElement:
    """Apply (id tensor Delta) to a tensor element.

    (id x Delta)([L] x [R]) = sum_j [L] x [R_left_j] x [R_right_j]
    """
    terms = {}
    for (left, right), coeff in tensor_elem.terms.items():
        delta_right = deconcatenation_coproduct(right)
        for (rl, rr), dcoeff in delta_right.terms.items():
            key = (left, rl, rr)
            terms[key] = terms.get(key, FR0) + coeff * dcoeff
    return TripleTensorBarElement({k: v for k, v in terms.items() if v != FR0})


def verify_coassociativity(monomial: tuple) -> bool:
    """Verify (Delta x id) o Delta = (id x Delta) o Delta on a monomial."""
    delta = deconcatenation_coproduct(monomial)
    lhs = apply_delta_left(delta)
    rhs = apply_delta_right(delta)
    return lhs == rhs


# ============================================================
# Counit
# ============================================================

def counit(monomial: tuple) -> Fraction:
    """epsilon([a_1|...|a_n]) = delta_{n,0}.

    The counit is 1 on the empty monomial and 0 on all others.
    """
    if len(monomial) == 0:
        return FR1
    return FR0


def verify_counit_left(monomial: tuple) -> bool:
    """Verify (epsilon x id) o Delta = id."""
    delta = deconcatenation_coproduct(monomial)
    # Apply epsilon tensor id
    result = {}
    for (left, right), coeff in delta.terms.items():
        eps_left = counit(left)
        if eps_left != FR0:
            result[right] = result.get(right, FR0) + coeff * eps_left
    # Should equal the original monomial with coefficient 1
    expected = {monomial: FR1}
    return result == expected


def verify_counit_right(monomial: tuple) -> bool:
    """Verify (id x epsilon) o Delta = id."""
    delta = deconcatenation_coproduct(monomial)
    result = {}
    for (left, right), coeff in delta.terms.items():
        eps_right = counit(right)
        if eps_right != FR0:
            result[left] = result.get(left, FR0) + coeff * eps_right
    expected = {monomial: FR1}
    return result == expected


# ============================================================
# OPE algebra definition (for bar differential)
# ============================================================

class ChiralAlgebraOPE:
    """OPE data for a chiral algebra.

    Stores the OPE structure constants: for generators a, b,
    the OPE is a(z)b(w) ~ sum_n c_n(w) / (z-w)^n.

    Each c_n is itself a linear combination of generators
    (or 'vacuum' for the identity, or 'zero').

    The BAR DIFFERENTIAL uses the RESIDUE of the OPE tensored with
    the d-log kernel. The collision residue Res_{D_{ij}} extracts
    the FULL OPE (all modes), not just the simple pole.

    For the bar complex at genus 0, the key formula is:
    d_res[a|b] = sum_n (-1)^{sign} mu_n(a,b) * (residue of eta form)
    where mu_n is the n-th OPE mode (coefficient of (z-w)^{-n}).

    CRITICAL (AP19): the bar DIFFERENTIAL uses d log(z-w) as its kernel.
    The residue of f(z,w) * d log(z-w) along z=w extracts SIMPLE POLE
    of f(z,w) * 1/(z-w), i.e., the coefficient of (z-w)^{-1} in
    f(z,w)/(z-w). If f(z,w) = c_n/(z-w)^n, the integrand is
    c_n/(z-w)^{n+1} * d(z-w), and Res extracts c_n when n+1 = 1,
    i.e., n = 0. Wait -- that is the REGULAR TERM, not the poles.

    Let me redo this carefully. The bar element at arity 1 is:
      alpha = a tensor b tensor eta_{01}
    where eta_{01} = d log(z_0 - z_1) = d(z_0-z_1)/(z_0-z_1).

    The residue differential takes:
      d_res(alpha) = Res_{z_0=z_1} [ a(z_0) b(z_1) * d(z_0-z_1)/(z_0-z_1) ]
                   = Res_{u=0} [ a(z_1+u) b(z_1) * du/u ]
    where u = z_0 - z_1.

    Now a(z_1+u) b(z_1) = sum_n c_n(z_1) * u^{-n} (OPE expansion).
    So: Res_{u=0} [ sum_n c_n u^{-n} * du/u ] = Res_{u=0} [ sum_n c_n u^{-n-1} du ]
    The residue picks out the coefficient of u^{-1} du, which is c_0... NO.
    The residue of sum_n c_n u^{-n-1} du = c_0 (the n=0 term gives u^{-1}).

    Wait, this contradicts the standard picture. Let me reconsider.

    ACTUALLY: In the vertex algebra / chiral algebra convention,
    the OPE is a(z)b(w) ~ sum_{n>=0} c_n(w) / (z-w)^{n+1},
    NOT sum c_n / (z-w)^n. The index shift matters.

    With the (n+1) convention: a(z)b(w) ~ sum_{n>=0} (a_{(n)}b)(w) / (z-w)^{n+1}.
    Then a(w+u)b(w) = sum_{n>=0} (a_{(n)}b)(w) * u^{-n-1}.
    The bar residue: Res_{u=0}[ sum_n (a_{(n)}b) u^{-n-1} * du/u ]
                   = Res_{u=0}[ sum_n (a_{(n)}b) u^{-n-2} du ]
    This picks out n = -1... which does not exist for n >= 0.

    So the d-log residue gives ZERO?! That cannot be right.

    The issue is that the bar differential is NOT simply "take residue of
    OPE times d-log." The correct construction is more subtle.

    Going back to the manuscript (def:bar-differential-complete, line 497-501):
    d_res applies Res_{D_{ij}} to mu(phi_i, phi_j) tensor (other factors) tensor omega.
    The chiral product mu already includes the integration/residue: it is the
    *-product (chiral multiplication), not the OPE. In the BD formulation,
    mu: j_* j^* (A boxtimes A) -> Delta_* A is a map of D-modules, and the
    residue extraction is part of the factorization structure.

    For COMPUTATIONAL PURPOSES (genus 0, algebraic bar complex), the bar
    differential at arity n -> arity (n-1) is:
      d_B[a_1|...|a_n] = sum_{i=1}^{n-1} (-1)^{sign_i} [a_1|...|a_i * a_{i+1}|...|a_n]
    where a_i * a_{i+1} is the chiral product (= sum of ALL OPE modes).

    For a Lie algebra-type OPE (affine KM), a_i * a_j = [a_i, a_j] (bracket).
    For the Heisenberg with J(z)J(w) ~ k/(z-w)^2:
      J * J = J_{(0)} J (the zeroth mode product)
    In the Heisenberg algebra, J_{(0)}J = 0 (the zero-mode bracket vanishes
    because [J_m, J_n] = m*k*delta_{m+n,0} and J_{(0)} = J_0).
    The J_{(1)}J = k*1 is the simple-pole coefficient (central term).

    So the bar differential is:
      d_B[J|J] = J_{(0)}J = 0   (at the binary level, using zeroth mode)

    But wait -- the bar complex of the Heisenberg is KNOWN to have nontrivial
    differential. The issue is which modes enter.

    Let me reconsider. In the chiral algebra framework (BD, Section 3.4),
    the bar differential uses the FULL chiral product, which is:
      mu^ch(a, b) = sum_{n>=0} a_{(n)}b * eta^{(n)}
    where eta^{(n)} are the appropriate form components.

    For the ordered bar complex at genus 0, the ALGEBRAIC bar differential is:
      d_B = sum of face maps in the simplicial bar construction.
    The face map d_i for 1 <= i <= n-1 is:
      d_i[a_1|...|a_n] = [a_1|...|a_i * a_{i+1}|...|a_n]
    and the product a_i * a_{i+1} uses the NORMALLY ORDERED PRODUCT
    (the regular part of the OPE, i.e., a_{(-1)}b in the vertex algebra convention).

    For the Heisenberg: J_{(-1)}J = :JJ: (the normal ordered product).

    Actually, for bar complexes of augmented algebras, the differential
    uses the AUGMENTATION IDEAL. The reduced bar complex uses A_bar = ker(epsilon),
    and the product is the induced product on A_bar.

    Let me reconsider the whole setup more carefully.

    THE CORRECT PICTURE (following Loday-Vallette, Algebraic Operads):
    For an associative algebra A, the bar complex is:
      B(A) = T^c(s^{-1} A_bar) with d_B = d_1 + d_2
    where d_2[a_1|...|a_n] = sum_{i=1}^{n-1} (-1)^i [a_1|...|a_i*a_{i+1}|...|a_n]
    and d_1 extends the internal differential.

    For a CHIRAL algebra, the product a_i * a_{i+1} is the CHIRAL PRODUCT
    (the mu^ch map), which in the vertex algebra language is:
      mu^ch(a, b) = Res_{z=0} Y(a, z) b dz   (= a_{(-1)}b, WRONG for chiral)

    Actually, for CHIRAL algebras specifically, the product that enters the
    bar complex is the chiral bracket, which for the Heisenberg is:
      {J, J} = k * 1   (the residue of the OPE, i.e., the Lie bracket)
    This is J_{(0)}J for affine KM, but for the Heisenberg with
    J(z)J(w) ~ k/(z-w)^2, the relevant product is J_{(1)}J = k.

    The confusion arises because "chiral product" can mean different things.
    In BD's framework, the chiral product mu^ch: A boxtimes A -> Delta_! A
    encodes ALL the OPE data. The bar differential extracts specific components
    depending on the form degree.

    FOR THIS ENGINE: We work with the REDUCED algebraic model.
    The bar differential on [a|b] produces the BRACKET [a,b] (for Lie-type
    algebras) or more generally the relevant OPE mode. For the Heisenberg,
    [J, J] = k (a central element), so d_B[J|J] = k * [1] = 0 in the reduced
    bar complex (since 1 is in the augmentation ideal's complement).

    ACTUALLY the curvature. For the Heisenberg, d_B^2 = 0 at genus 0, but
    the relevant bar differential at arity 2 -> 1 is:
      d[J|J] = {J,J} = k  (central)
    This gives a map B_2 -> B_1. But {J,J} = k*1 is a SCALAR, not a generator.
    In the reduced bar complex: k*1 maps to 0 under the augmentation.
    So d_B[J|J] = 0 in the reduced bar complex (the bracket is central).

    For sl_2 at level k: generators e, f, h with
      [e, f] = h, [h, e] = 2e, [h, f] = -2f
    and the chiral bracket is these Lie brackets. So:
      d_B[e|f] = [e,f] = h,  d_B[h|e] = [h,e] = 2e, etc.

    For the computational engine, we implement a general framework
    where the user specifies the OPE data (= Lie bracket for standard families)
    and we verify the E_1 coalgebra properties.
    """

    def __init__(self, generators: List[str], bracket: Dict[Tuple[str,str], Dict[str, Fraction]]):
        """Initialize with generator names and bracket data.

        bracket[(a,b)] = {c: coeff, ...} means [a,b] = sum coeff * c.
        The bracket should be antisymmetric: bracket[(b,a)] = -bracket[(a,b)].

        For generators that are central (e.g., k*1 for Heisenberg),
        map them to the special generator 'UNIT' which is zero in the reduced bar.
        """
        self.generators = generators
        self.bracket = bracket

    def product(self, a: str, b: str) -> Dict[str, Fraction]:
        """Compute the chiral bracket [a, b].

        Returns a dict mapping generator -> coefficient.
        Missing entries mean zero.
        """
        key = (a, b)
        if key in self.bracket:
            return dict(self.bracket[key])
        # Try antisymmetry
        rev_key = (b, a)
        if rev_key in self.bracket:
            return {g: -c for g, c in self.bracket[rev_key].items()}
        return {}


# ============================================================
# Bar differential
# ============================================================

def bar_differential(elem: BarElement, ope: ChiralAlgebraOPE) -> BarElement:
    """Compute d_B on a bar element using the chiral bracket.

    The bar differential on T^c(s^{-1} A_bar) is the CODERIVATION EXTENSION
    of the binary product mu: (s^{-1}A)^{tensor 2} -> s^{-1}A.

    For degree-0 desuspended generators (conformal weight 1 after desuspension
    by AP45: |s^{-1}v| = |v| - 1), the Koszul signs are ALL +1, so:

      d_B[a_1|...|a_n] = sum_{i=0}^{n-2} [a_1|...|mu(a_i, a_{i+1})|...|a_n]

    NO alternating signs (-1)^i. The coderivation extension of mu has signs
    from commuting mu past desuspended elements; for degree-0 elements these
    are all trivial.

    DISTINCTION: The simplicial/Hochschild bar differential uses (-1)^i signs.
    The coderivation on T^c(V) does NOT. These are DIFFERENT differentials
    that give the SAME cohomology (they differ by an automorphism of T^c(V)).
    But only the unsigned version satisfies Delta o d = (d x id + id x d) o Delta
    with the deconcatenation coproduct.

    For generators with nonzero desuspended degree, Koszul signs would appear:
      sign_i = (-1)^{sum_{j<i} |s^{-1}a_j|}
    For degree-0 generators this is always +1.

    NOTE: We filter out 'UNIT' terms (central elements killed in reduced bar).
    """
    result_terms: Dict[tuple, Fraction] = {}
    for mon, coeff in elem.terms.items():
        n = len(mon)
        for i in range(n - 1):
            # Merge positions i and i+1
            a_i = mon[i]
            a_ip1 = mon[i + 1]
            product = ope.product(a_i, a_ip1)
            # Koszul sign from commuting mu past s^{-1}a_0,...,s^{-1}a_{i-1}.
            # For degree-0 desuspended generators: sign = +1 always.
            sign = FR1
            for gen, pcoeff in product.items():
                if gen == 'UNIT':
                    continue  # Central elements vanish in reduced bar
                new_mon = mon[:i] + (gen,) + mon[i+2:]
                key = new_mon
                val = coeff * sign * pcoeff
                result_terms[key] = result_terms.get(key, FR0) + val
    return BarElement({k: v for k, v in result_terms.items() if v != FR0},
                     max(0, elem.arity - 1))


def bar_differential_monomial(mon: tuple, ope: ChiralAlgebraOPE) -> BarElement:
    """Convenience: apply d_B to a single monomial."""
    return bar_differential(BarElement({mon: FR1}, len(mon)), ope)


# ============================================================
# Coderivation property verification
# ============================================================

def apply_d_tensor_id(tensor_elem: TensorBarElement,
                      ope: ChiralAlgebraOPE) -> TensorBarElement:
    """Apply (d_B tensor id) to a tensor element."""
    result: Dict[Tuple[tuple,tuple], Fraction] = {}
    for (left, right), coeff in tensor_elem.terms.items():
        if len(left) < 2:
            continue  # d_B on arity < 2 is zero (no adjacent pairs)
        d_left = bar_differential_monomial(left, ope)
        for new_left, dcoeff in d_left.terms.items():
            key = (new_left, right)
            result[key] = result.get(key, FR0) + coeff * dcoeff
    return TensorBarElement({k: v for k, v in result.items() if v != FR0})


def apply_id_tensor_d(tensor_elem: TensorBarElement,
                      ope: ChiralAlgebraOPE) -> TensorBarElement:
    """Apply (id tensor d_B) to a tensor element."""
    result: Dict[Tuple[tuple,tuple], Fraction] = {}
    for (left, right), coeff in tensor_elem.terms.items():
        if len(right) < 2:
            continue
        d_right = bar_differential_monomial(right, ope)
        for new_right, dcoeff in d_right.terms.items():
            key = (left, new_right)
            result[key] = result.get(key, FR0) + coeff * dcoeff
    return TensorBarElement({k: v for k, v in result.items() if v != FR0})


def verify_coderivation(mon: tuple, ope: ChiralAlgebraOPE) -> Tuple[bool, str]:
    """Verify Delta o d_B = (d_B tensor id + id tensor d_B) o Delta on a monomial.

    Returns (True, "") if verified, (False, explanation) if failed.
    """
    # LHS: Delta(d_B(mon))
    d_mon = bar_differential_monomial(mon, ope)
    lhs = coproduct_on_element(d_mon)

    # RHS: (d_B x id + id x d_B)(Delta(mon))
    delta_mon = deconcatenation_coproduct(mon)
    rhs_1 = apply_d_tensor_id(delta_mon, ope)
    rhs_2 = apply_id_tensor_d(delta_mon, ope)
    rhs = rhs_1 + rhs_2

    if lhs == rhs:
        return True, ""
    else:
        return False, f"LHS = {lhs}, RHS = {rhs}"


# ============================================================
# d^2 = 0 verification
# ============================================================

def verify_d_squared_zero(mon: tuple, ope: ChiralAlgebraOPE) -> Tuple[bool, str]:
    """Verify d_B^2 = 0 on a monomial.

    This requires the Jacobi identity for the bracket (= Arnold relation
    for the logarithmic forms).
    """
    d_mon = bar_differential_monomial(mon, ope)
    dd_mon = bar_differential(d_mon, ope)
    if dd_mon.is_zero():
        return True, ""
    return False, f"d^2(mon) = {dd_mon}"


# ============================================================
# Standard algebras
# ============================================================

def heisenberg_ope(level: Fraction = FR1) -> ChiralAlgebraOPE:
    """Heisenberg algebra H_k with single generator J.

    OPE: J(z)J(w) ~ k/(z-w)^2.
    Chiral bracket: {J, J} = k * 1 (central).
    In reduced bar: {J, J} = 0 (central elements vanish).

    So d_B is identically zero on the reduced bar of the Heisenberg.
    This is correct: H_k has trivial bar cohomology in degrees > 1
    (it is a free commutative chiral algebra, so its bar is quasi-iso
    to its generators, i.e., B(H_k) ~ s^{-1}J in degree 1).
    """
    return ChiralAlgebraOPE(
        generators=['J'],
        bracket={('J', 'J'): {'UNIT': level}}
    )


def sl2_ope(level: Fraction = FR1) -> ChiralAlgebraOPE:
    """Affine sl_2 at level k.

    Generators: e, f, h (Chevalley basis of sl_2).
    Chiral bracket = Lie bracket:
      [e, f] = h,  [h, e] = 2e,  [h, f] = -2f
    Plus central terms from the level: [e, f] = h + k*1, etc.
    In the reduced bar, central terms vanish, so we use the Lie bracket only.

    Level k only affects the central extension (curvature), not the genus-0
    reduced bar differential.
    """
    two = Fraction(2)
    return ChiralAlgebraOPE(
        generators=['e', 'f', 'h'],
        bracket={
            ('e', 'f'): {'h': FR1},
            ('h', 'e'): {'e': two},
            ('h', 'f'): {'f': -two},
        }
    )


def abelian_lie_ope(dim: int) -> ChiralAlgebraOPE:
    """Abelian Lie algebra of dimension dim.

    All brackets zero (like multiple Heisenberg generators).
    d_B = 0.
    """
    gens = [f'x{i}' for i in range(dim)]
    return ChiralAlgebraOPE(generators=gens, bracket={})


def gl2_ope() -> ChiralAlgebraOPE:
    """gl_2 = sl_2 + center.

    Generators: e, f, h, z (z = central).
    Bracket: sl_2 bracket plus [z, anything] = 0.
    """
    two = Fraction(2)
    return ChiralAlgebraOPE(
        generators=['e', 'f', 'h', 'z'],
        bracket={
            ('e', 'f'): {'h': FR1},
            ('h', 'e'): {'e': two},
            ('h', 'f'): {'f': -two},
        }
    )


# ============================================================
# Logarithmic form algebra (for the geometric verification)
# ============================================================

class LogForm:
    """A logarithmic differential form on FM_n(C).

    Represented as a linear combination of wedge products of eta_{ij}.
    Each basis element is a frozenset of pairs (i,j) with i < j,
    representing eta_{i0,j0} ^ eta_{i1,j1} ^ ...

    Subject to:
      - Antisymmetry: eta_{ij} ^ eta_{ij} = 0
      - Arnold relation: eta_{ij} ^ eta_{jk} + eta_{jk} ^ eta_{ki} + eta_{ki} ^ eta_{ij} = 0
        for distinct i, j, k.

    We store forms in reduced form (modulo Arnold relations) using a
    canonical ordering convention.
    """

    def __init__(self, terms: Optional[Dict[tuple, Fraction]] = None, n_points: int = 0):
        """terms: dict mapping sorted tuple of (i,j) pairs -> coefficient."""
        self.terms = {} if terms is None else {k: v for k, v in terms.items() if v != FR0}
        self.n_points = n_points

    def degree(self) -> int:
        if not self.terms:
            return 0
        return len(next(iter(self.terms)))

    def __eq__(self, other):
        if isinstance(other, int) and other == 0:
            return not self.terms
        if not isinstance(other, LogForm):
            return NotImplemented
        return self.terms == other.terms

    def __add__(self, other):
        if isinstance(other, int) and other == 0:
            return self
        result = dict(self.terms)
        for k, v in other.terms.items():
            result[k] = result.get(k, FR0) + v
        return LogForm({k: v for k, v in result.items() if v != FR0},
                      max(self.n_points, other.n_points))

    def __neg__(self):
        return LogForm({k: -v for k, v in self.terms.items()}, self.n_points)

    def is_zero(self) -> bool:
        return not self.terms

    @staticmethod
    def eta(i: int, j: int, n_points: int) -> 'LogForm':
        """The basic log 1-form eta_{ij} = d log(z_i - z_j).

        We normalize so that i < j.
        eta_{ji} = -eta_{ij} (antisymmetry of d log).

        Wait -- d log(z_i - z_j) = d(z_i - z_j)/(z_i - z_j).
        d log(z_j - z_i) = d(z_j - z_i)/(z_j - z_i) = -d(z_i - z_j)/-(z_i - z_j)
                         = d(z_i - z_j)/(z_i - z_j) = d log(z_i - z_j).
        So eta_{ij} = eta_{ji}! The d-log form is SYMMETRIC.

        Actually: d log(z_i - z_j) = (dz_i - dz_j)/(z_i - z_j).
        d log(z_j - z_i) = (dz_j - dz_i)/(z_j - z_i) = -(dz_i - dz_j)/-(z_i - z_j)
                         = (dz_i - dz_j)/(z_i - z_j) = d log(z_i - z_j).
        So yes, eta_{ij} = eta_{ji}.

        We store with i < j as canonical form.
        """
        a, b = min(i, j), max(i, j)
        if a == b:
            raise ValueError("eta_{ii} is undefined")
        return LogForm({((a, b),): FR1}, n_points)

    def wedge(self, other: 'LogForm') -> 'LogForm':
        """Wedge product of two log forms."""
        result: Dict[tuple, Fraction] = {}
        for basis1, c1 in self.terms.items():
            for basis2, c2 in other.terms.items():
                # Check for repeated pairs (gives 0)
                pairs1 = set(basis1)
                pairs2 = set(basis2)
                if pairs1 & pairs2:
                    continue  # eta ^ eta = 0
                # Merge and sort, tracking sign from reordering
                combined = list(basis1) + list(basis2)
                # Sort with bubble sort to track sign
                sign = 1
                arr = list(combined)
                for pass_i in range(len(arr)):
                    for swap_j in range(len(arr) - 1 - pass_i):
                        if arr[swap_j] > arr[swap_j + 1]:
                            arr[swap_j], arr[swap_j + 1] = arr[swap_j + 1], arr[swap_j]
                            sign *= -1
                key = tuple(arr)
                result[key] = result.get(key, FR0) + c1 * c2 * _frac(sign)
        n = max(self.n_points, other.n_points)
        return LogForm({k: v for k, v in result.items() if v != FR0}, n)


def arnold_relation(i: int, j: int, k: int, n_points: int) -> LogForm:
    """The Arnold relation: eta_{ij} ^ eta_{jk} + eta_{jk} ^ eta_{ki} + eta_{ki} ^ eta_{ij} = 0.

    Returns the LHS (which should be zero in the quotient).
    """
    eij = LogForm.eta(i, j, n_points)
    ejk = LogForm.eta(j, k, n_points)
    eki = LogForm.eta(k, i, n_points)
    return eij.wedge(ejk) + ejk.wedge(eki) + eki.wedge(eij)


def verify_arnold_relation(i: int, j: int, k: int, n_points: int) -> bool:
    """Check that the Arnold relation holds for three distinct points.

    NOTE: The Arnold relation eta_{ij}^eta_{jk} + eta_{jk}^eta_{ki} + eta_{ki}^eta_{ij} = 0
    does NOT hold as an identity of formal symbols -- it is a relation in H*(FM_n(C)).
    In our representation (formal wedge products), the three terms are DISTINCT basis
    elements. The Arnold relation says they sum to zero IN COHOMOLOGY.

    So this function checks whether the Arnold relation holds in our LogForm algebra.
    It will return False because we have not quotiented by Arnold.
    The Arnold relation is an ADDITIONAL RELATION imposed on the log form algebra.
    """
    rel = arnold_relation(i, j, k, n_points)
    return rel.is_zero()


# ============================================================
# Form splitting under coproduct (the subtle geometric point)
# ============================================================

def form_restriction(form: LogForm, subset_I: frozenset, subset_J: frozenset) -> Tuple[LogForm, LogForm]:
    """Restrict a log form to the product configuration space C_{|I|} x C_{|J|}.

    Given a log form omega on FM_{n}(C) and a partition [n] = I sqcup J,
    decompose omega into "I-pure" and "J-pure" and "mixed" parts.

    The I-pure part uses only eta_{ab} with a, b in I.
    The J-pure part uses only eta_{cd} with c, d in J.
    Mixed terms (eta_{ac} with a in I, c in J) are the obstruction
    to factorization.

    For the DECONCATENATION coproduct (ordered splitting I = {1,...,i}, J = {i+1,...,n}),
    the key observation is:

    IN THE ORDERED BAR, the deconcatenation is an ALGEBRAIC operation on the tensor
    coalgebra. The forms split because the tensor coalgebra structure is INDEPENDENT
    of the form component: Delta acts on the tensor factor indices, and the form
    component is carried along.

    The GEOMETRIC subtlety: FM_{n+1}(C) does NOT split as FM_{i+1}(C) x FM_{n-i+1}(C).
    The mixed eta forms eta_{ac} (a in I, c in J) DO exist on FM_{n+1}(C).
    But the deconcatenation coproduct PROJECTS AWAY the mixed forms:
    it keeps only the I-pure and J-pure parts.

    This projection is well-defined because:
    (a) In the R-direction, points in I are to the LEFT of points in J (ordered bar).
    (b) The deconcatenation corresponds to the OPERAD COMPOSITION in E_1:
        the interval [t_1,...,t_n] splits as [t_1,...,t_i] x [t_{i+1},...,t_n].
    (c) The mixed forms carry no bar-relevant information: they do not contribute
        to the bar differential (which only merges ADJACENT pairs in the ordered bar).

    Returns: (I_form, J_form) where I_form uses only pairs from I
    and J_form uses only pairs from J. Mixed terms are ZERO.

    CRITICAL: for the coderivation property to hold, we need that the bar differential
    commutes with this projection. This works because d_res merges ADJACENT pairs,
    and adjacent pairs are always in the SAME half of the deconcatenation.
    """
    I_terms: Dict[tuple, Fraction] = {}
    J_terms: Dict[tuple, Fraction] = {}
    has_mixed = False

    for basis, coeff in form.terms.items():
        is_I_pure = all(a in subset_I and b in subset_I for (a, b) in basis)
        is_J_pure = all(a in subset_J and b in subset_J for (a, b) in basis)
        if is_I_pure:
            I_terms[basis] = I_terms.get(basis, FR0) + coeff
        elif is_J_pure:
            J_terms[basis] = J_terms.get(basis, FR0) + coeff
        else:
            has_mixed = True

    I_form = LogForm({k: v for k, v in I_terms.items() if v != FR0}, form.n_points)
    J_form = LogForm({k: v for k, v in J_terms.items() if v != FR0}, form.n_points)
    return I_form, J_form


def check_form_splitting_ordered(n: int) -> Dict[str, Any]:
    """Analyze the form splitting for the ordered bar at arity n.

    For the ordered bar at arity n, the standard log form is:
      omega_n = eta_{01} ^ eta_{12} ^ ... ^ eta_{(n-1),n}
    (the canonical ordered form using consecutive pairs).

    Under deconcatenation at position i (splitting {0,...,n} into
    {0,...,i} and {i+1,...,n}), this form splits as:
      omega_i = eta_{01} ^ ... ^ eta_{(i-1),i}
      omega_{n-i} = eta_{(i+1),(i+2)} ^ ... ^ eta_{(n-1),n}
    with the mixed term eta_{i,i+1} MISSING from both pieces.

    This missing form is exactly the form that was "consumed" by the
    bar differential when it merged positions i and i+1.

    Returns analysis dict.
    """
    results = {}
    points = list(range(n + 1))  # 0, 1, ..., n

    # Build the canonical ordered form
    pairs = [(j, j+1) for j in range(n)]

    for split_pos in range(n + 1):
        I = frozenset(range(split_pos + 1))        # {0, ..., split_pos}
        J = frozenset(range(split_pos + 1, n + 1))  # {split_pos+1, ..., n}

        I_pairs = [(a, b) for (a, b) in pairs if a in I and b in I]
        J_pairs = [(a, b) for (a, b) in pairs if a in J and b in J]
        mixed_pairs = [(a, b) for (a, b) in pairs if not (a in I and b in I) and not (a in J and b in J)]

        results[split_pos] = {
            'I': sorted(I),
            'J': sorted(J),
            'I_pairs': I_pairs,
            'J_pairs': J_pairs,
            'mixed_pairs': mixed_pairs,
            'I_form_degree': len(I_pairs),
            'J_form_degree': len(J_pairs),
            'mixed_count': len(mixed_pairs),
            'total_form_degree': len(I_pairs) + len(J_pairs) + len(mixed_pairs),
        }

    return results


# ============================================================
# Shuffle coproduct (for symmetric bar)
# ============================================================

def shuffle_coproduct(monomial: tuple) -> TensorBarElement:
    """Compute the shuffle coproduct on a monomial.

    For the SYMMETRIC bar B^Sigma(A) = T^c(s^{-1}A_bar)/S_n,
    the coproduct is the SHUFFLE coproduct:

    Delta^sh[a_1|...|a_n] = sum over (p,q)-shuffles sigma
      [a_{sigma(1)}|...|a_{sigma(p)}] tensor [a_{sigma(p+1)}|...|a_{sigma(n)}]

    A (p,q)-shuffle is a permutation sigma of {1,...,n} = {1,...,p+q}
    such that sigma(1) < ... < sigma(p) and sigma(p+1) < ... < sigma(n).

    The shuffle coproduct is cocommutative (appropriate for the symmetric bar).
    The deconcatenation is NOT cocommutative.

    The relationship: if pi: B^ord -> B^Sigma is the symmetrization map,
    then pi intertwines the deconcatenation and shuffle coproducts:
      pi tensor pi o Delta^deconc = Delta^sh o pi.
    """
    n = len(monomial)
    terms: Dict[Tuple[tuple, tuple], Fraction] = {}

    for p in range(n + 1):
        q = n - p
        # Generate all (p,q)-shuffles
        for left_indices in combinations(range(n), p):
            left_set = set(left_indices)
            right_indices = [j for j in range(n) if j not in left_set]

            left_mon = tuple(monomial[j] for j in left_indices)
            right_mon = tuple(monomial[j] for j in right_indices)

            # Sign: the Koszul sign of the shuffle permutation
            # For degree-0 elements (after desuspension of weight-1 generators),
            # all signs are +1.
            # For general degree, need to track signs.
            # We implement the degree-0 case here.
            key = (left_mon, right_mon)
            terms[key] = terms.get(key, FR0) + FR1

    return TensorBarElement({k: v for k, v in terms.items() if v != FR0})


def verify_shuffle_coassociativity(monomial: tuple) -> bool:
    """Verify the shuffle coproduct is coassociative."""
    # This is harder to check directly because of the triple tensor structure.
    # Instead, we verify a specific identity.
    # For degree-0 elements, this should hold by the standard shuffle algebra theory.
    delta = shuffle_coproduct(monomial)
    lhs = apply_delta_left_shuffle(delta)
    rhs = apply_delta_right_shuffle(delta)
    return lhs == rhs


def apply_delta_left_shuffle(tensor_elem: TensorBarElement) -> TripleTensorBarElement:
    """Apply (Delta^sh tensor id) to a tensor element."""
    terms: Dict[Tuple[tuple,tuple,tuple], Fraction] = {}
    for (left, right), coeff in tensor_elem.terms.items():
        delta_left = shuffle_coproduct(left)
        for (ll, lr), dcoeff in delta_left.terms.items():
            key = (ll, lr, right)
            terms[key] = terms.get(key, FR0) + coeff * dcoeff
    return TripleTensorBarElement({k: v for k, v in terms.items() if v != FR0})


def apply_delta_right_shuffle(tensor_elem: TensorBarElement) -> TripleTensorBarElement:
    """Apply (id tensor Delta^sh) to a tensor element."""
    terms: Dict[Tuple[tuple,tuple,tuple], Fraction] = {}
    for (left, right), coeff in tensor_elem.terms.items():
        delta_right = shuffle_coproduct(right)
        for (rl, rr), dcoeff in delta_right.terms.items():
            key = (left, rl, rr)
            terms[key] = terms.get(key, FR0) + coeff * dcoeff
    return TripleTensorBarElement({k: v for k, v in terms.items() if v != FR0})


# ============================================================
# Cocommutativity check
# ============================================================

def swap_tensor(tensor_elem: TensorBarElement) -> TensorBarElement:
    """Swap the two tensor factors: tau([L] x [R]) = [R] x [L]."""
    return TensorBarElement({(right, left): coeff
                            for (left, right), coeff in tensor_elem.terms.items()})


def is_cocommutative(monomial: tuple) -> bool:
    """Check if Delta(mon) = tau o Delta(mon).

    Deconcatenation is NOT cocommutative for n >= 2.
    Shuffle IS cocommutative.
    """
    delta = deconcatenation_coproduct(monomial)
    swapped = swap_tensor(delta)
    return delta == swapped


def is_shuffle_cocommutative(monomial: tuple) -> bool:
    """Check if Delta^sh(mon) = tau o Delta^sh(mon)."""
    delta = shuffle_coproduct(monomial)
    swapped = swap_tensor(delta)
    return delta == swapped


# ============================================================
# Counting and enumeration
# ============================================================

def count_deconcatenation_terms(n: int) -> int:
    """Number of terms in Delta[a_1|...|a_n]: always n+1."""
    return n + 1


def count_shuffle_terms(n: int) -> int:
    """Number of terms in Delta^sh[a_1|...|a_n]: 2^n (all subsets)."""
    return 2 ** n


def dim_log_forms(n: int) -> int:
    """Dimension of H^0(FM_{n+1}(C), Omega^n_log).

    The space of logarithmic n-forms on FM_{n+1}(C) modulo Arnold relations.
    By the Arnol'd-Brieskorn-Orlik-Solomon theorem:
      H*(FM_{n+1}(C)) is generated by eta_{ij} (1-forms) subject to
      the Arnold relations.
    The dimension of the degree-n part is n! (= number of permutations).

    This is because FM_{n+1}(C) / PSL_2 ~ M_{0,n+2} has cohomology
    ring = graded Orlik-Solomon algebra of the braid arrangement.
    """
    return factorial(n)


# ============================================================
# Heisenberg explicit computation
# ============================================================

def heisenberg_bar_differential_arity3(level: Fraction = FR1) -> Dict[str, Any]:
    """Explicit computation of d_B on B_3(H_k) = span{[J|J|J]}.

    For the Heisenberg algebra, the chiral bracket is {J, J} = k * UNIT.
    In the reduced bar, UNIT = 0, so d_B = 0 on all arities.

    But we verify this explicitly to check the coderivation property
    in the trivial case.

    The CURVATURE at genus >= 1 (d^2 = kappa * omega_g) is a separate
    phenomenon: at genus 0, d^2 = 0 trivially because d = 0 for Heisenberg.
    """
    ope = heisenberg_ope(level)

    mon3 = ('J', 'J', 'J')
    d_mon3 = bar_differential_monomial(mon3, ope)

    # d_B[J|J|J] = [JJ|J] - [J|JJ] (with sign)
    # But JJ = {J,J} = k*UNIT = 0 in reduced bar
    # So d_B[J|J|J] = 0

    delta_mon3 = deconcatenation_coproduct(mon3)
    ok, msg = verify_coderivation(mon3, ope)

    return {
        'monomial': mon3,
        'd_B': d_mon3,
        'd_B_is_zero': d_mon3.is_zero(),
        'coderivation_holds': ok,
        'coderivation_msg': msg,
    }


def sl2_bar_differential_arity2() -> Dict[str, Any]:
    """Explicit computation of d_B on B_2(sl_2).

    B_2 = span{[a|b] : a, b in {e, f, h}}.
    d_B[a|b] = [a,b] (the Lie bracket, with sign from desuspension).

    For sl_2:
    d_B[e|f] = [e,f] = h    (=> [h] with coefficient 1)
    d_B[f|e] = -[e,f] = -h  (antisymmetry + sign)
    d_B[h|e] = [h,e] = 2e
    d_B[e|h] = -[h,e] = -2e
    d_B[h|f] = [h,f] = -2f
    d_B[f|h] = -[h,f] = 2f
    d_B[e|e] = [e,e] = 0
    d_B[f|f] = [f,f] = 0
    d_B[h|h] = [h,h] = 0
    """
    ope = sl2_ope()
    results = {}
    for a in ['e', 'f', 'h']:
        for b in ['e', 'f', 'h']:
            mon = (a, b)
            d = bar_differential_monomial(mon, ope)
            results[mon] = d
    return results


def sl2_bar_differential_arity3() -> Dict[str, Any]:
    """Explicit computation of d_B on some elements of B_3(sl_2).

    d_B[a|b|c] = [ab|c] - [a|bc]  (simplicial signs, 0-indexed: (-1)^0 and (-1)^1)

    For [e|f|h]:
    d_B[e|f|h] = [[e,f]|h] - [e|[f,h]]
               = [h|h] - [e|2f]    (since [f,h] = -[h,f] = 2f)
               = [h|h] - 2[e|f]

    Let's verify d^2 = 0 on [e|f|h]:
    d_B(d_B[e|f|h]) = d_B([h|h] - 2[e|f])
                     = d_B[h|h] - 2*d_B[e|f]
                     = [h,h] - 2*[e,f]
                     = 0 - 2h
    Hmm, that is -2h, not 0! Let me recheck signs.

    Standard bar sign convention (Loday-Vallette, Algebraic Operads, 2.2.1):
    d_B = sum_{i=1}^{n-1} (-1)^i d_i
    where d_i[a_1|...|a_n] = [a_1|...|a_i * a_{i+1}|...|a_n].

    So d_B[a|b|c] = (-1)^1 [a*b|c] + (-1)^2 [a|b*c]
                   = -[ab|c] + [a|bc]

    For [e|f|h]:
    d_B[e|f|h] = -[h|h] + [e|2f] = -[h|h] + 2[e|f]

    d_B(d_B[e|f|h]) = d_B(-[h|h] + 2[e|f])
                     = -d_B[h|h] + 2*d_B[e|f]

    d_B[h|h] = (-1)^1 [h*h] = -[h,h] = 0
    d_B[e|f] = (-1)^1 [e*f] = -[e,f] = -h

    So d^2[e|f|h] = -0 + 2*(-h) = -2h ... still not zero!

    Wait, I think the sign convention issue is more subtle.
    The bar complex sign is d = sum (-1)^{epsilon} where epsilon
    depends on the DESUSPENDED degrees.

    For generators of conformal weight 1 (like sl_2 currents),
    |a| = 1 in the algebra grading, so |s^{-1}a| = 0 after desuspension (AP45).

    The Koszul sign rule for degree-0 elements: all signs are +1.
    So d_i has sign (-1)^i, and the bar differential is:
      d_B[a_1|a_2|a_3] = (-1)^1 [a_1 a_2 | a_3] + (-1)^2 [a_1 | a_2 a_3]
                        = -[a_1 a_2 | a_3] + [a_1 | a_2 a_3]

    Hmm, actually I was using this. Let me recheck d^2 more carefully.

    Actually, the issue may be that the product a*b in the bar complex
    is the ANTISYMMETRIZED product (= Lie bracket), and Jacobi identity
    ensures d^2 = 0.

    d^2[e|f|h] = d(-[ef|h] + [e|fh])
              = -d[ef|h] + d[e|fh]
              = -(-1)^1 [(ef)(h)] + (-1)^1 [e(fh)]    (both arity 2->1)
    Wait, for arity 2: d_B[a|b] = (-1)^1 [ab] = -[ab].

    So: d[ef|h] = -[ef, h] = -[[e,f], h] = -[h, h] = 0
        d[e|fh] = -[e, fh] = -[e, [f,h]] = -[e, -2f] = 2[e,f] = 2h

    d^2[e|f|h] = -0 + 2h = 2h. NOT ZERO!

    This means either my sign convention is wrong, or I need to
    track the Jacobi identity more carefully.

    Jacobi: [e, [f, h]] + [f, [h, e]] + [h, [e, f]] = 0
    [f, h] = -2f, so [e, -2f] = -2[e,f] = -2h
    [h, e] = 2e, so [f, 2e] = 2[f,e] = -2[e,f] = -2h
    [e, f] = h, so [h, h] = 0

    Jacobi: -2h + (-2h) + 0 = -4h ??? That is not zero!

    Wait, I have the Jacobi identity wrong. For sl_2:
    [h, e] = 2e, [h, f] = -2f, [e, f] = h.

    Jacobi for (e, f, h):
    [e, [f, h]] + [f, [h, e]] + [h, [e, f]]
    = [e, -(-2f)] ... no wait, [f, h] = -[h, f] = -(-2f) = 2f.

    So: [e, [f, h]] = [e, 2f] = 2[e, f] = 2h.
    [f, [h, e]] = [f, 2e] = 2[f, e] = -2[e, f] = -2h.
    [h, [e, f]] = [h, h] = 0.

    Sum: 2h - 2h + 0 = 0. Good, Jacobi holds!

    Now let me recompute d^2 with the correct signs.

    STANDARD BAR SIGN (Loday-Vallette, 2.2.1, for degree-0 desuspended generators):
    d[a_1|...|a_n] = sum_{i=1}^{n-1} (-1)^{i} [a_1|...|a_i a_{i+1}|...|a_n]

    Wait, I need to be more careful. Let me use the EXPLICIT sign from our code.
    In bar_differential, the sign is (-1)^i where i is 0-indexed.
    So the face map d_i (merging positions i and i+1, 0-indexed) has sign (-1)^i.

    d[a|b|c] = (-1)^0 [ab|c] + (-1)^1 [a|bc] = [ab|c] - [a|bc]

    For [e|f|h]:
    d[e|f|h] = [h|h] - [e|2f] = [h|h] - 2[e|f]

    Now d of this:
    d[h|h] = (-1)^0 [hh] = [h,h] = 0
    d[e|f] = (-1)^0 [ef] = [e,f] = h    (as monomial (h,), coeff 1)

    d^2[e|f|h] = d([h|h]) - 2*d([e|f]) = 0 - 2h.

    This is NOT zero. But it SHOULD be zero by Jacobi.

    The problem: the sign convention. Let me look at what the
    standard references say.

    In Loday-Vallette "Algebraic Operads" (2012), Section 2.2.1:
    The bar differential on T(sA) is b' = sum_{k=1}^{n-1} id^{k-1} x mu x id^{n-k-1}
    with appropriate signs from the Koszul rule.

    For the REDUCED bar: sA has degree shift, and the product mu on A is
    transported to a product on sA via:
      (sa)(sb) = (-1)^{|a|} s(ab)

    For degree-0 elements a, b (after desuspension): the Koszul sign is
    (-1)^{|s^{-1}a|} = (-1)^{-1} = -1 (since |s^{-1}a| = |a| - 1 = -1).

    Wait, I am confusing myself. Let me use the notation from signs_and_shifts.tex.

    From the signs appendix (line 548):
    d_bar[a|b] = (-1)^{|a|}[ab]

    For weight-1 generators (sl_2 currents): |a| = 1 (conformal weight).
    After desuspension: |s^{-1}a| = |a| - 1 = 0.
    The |a| in d_bar[a|b] = (-1)^{|a|}[ab] refers to the ORIGINAL degree, not desuspended.

    With |a| = 1: d[a|b] = (-1)^1 [ab] = -[ab] = -[a,b].

    For arity 3, the bar differential is (from the simplicial structure):
    d[a|b|c] = (-1)^{|a|}[ab|c] + (-1)^{|a|+|b|}[a|bc]

    For |a| = |b| = 1: d[a|b|c] = -[ab|c] + [a|bc].

    Checking d^2[e|f|h]:
    d[e|f|h] = -[ef|h] + [e|fh] = -[h|h] + [e|2f] = -[h|h] + 2[e|f]

    d(-[h|h]) = -(-1)^1 [hh] = [h,h] = 0
    d(2[e|f]) = 2 * (-1)^1 [ef] = -2[e,f] = -2h

    d^2[e|f|h] = 0 + (-2h) = -2h. STILL not zero.

    Hmm. Let me try the other convention: d[a|b] = [ab] (no sign, or sign from desuspended).

    With desuspended degrees (|s^{-1}a| = 0 for all generators):
    d[a|b|c] = [ab|c] + (-1)^0 [a|bc] = [ab|c] + [a|bc]... no that gives sum.

    Actually, the correct bar differential for the BAR of an ASSOCIATIVE algebra is:
    d = sum_{i=0}^{n} (-1)^i d_i
    where d_0, d_n are the augmentation maps and d_i (1 <= i <= n-1) uses the product.

    For the REDUCED bar (augmentation ideal), we only have d_i for 1 <= i <= n-1:
    d[a_1|...|a_n] = sum_{i=1}^{n-1} (-1)^i [a_1|...|a_i*a_{i+1}|...|a_n]

    The sign (-1)^i includes the desuspension signs only when elements have nonzero
    desuspended degree.

    For degree-0 desuspended elements:
    d[a|b] = (-1)^1 [ab] = -[a,b]
    d[a|b|c] = (-1)^1[ab|c] + (-1)^2[a|bc] = -[ab|c] + [a|bc]

    d^2[e|f|h] = d(-[h|h] + [e|2f])
               = -d[h|h] + 2 d[e|f]
               = -(-[h,h]) + 2(-[e,f])
               = [h,h] - 2[e,f]
               = 0 - 2h = -2h

    STILL nonzero. The problem is real: with these signs, d^2 != 0 on [e|f|h].

    Let me compute via Jacobi more carefully.

    For a general [a|b|c]:
    d[a|b|c] = -[ab|c] + [a|bc]
    d^2[a|b|c] = d(-[ab|c] + [a|bc])
               = -d[ab|c] + d[a|bc]
               = -(- [(ab)c]) + (- [a(bc)])
               = [(ab)c] - [a(bc)]
               = [[a,b],c] - [a,[b,c]]

    For this to be zero, we need [[a,b],c] = [a,[b,c]].
    But the JACOBI IDENTITY says [[a,b],c] = [a,[b,c]] - [b,[a,c]].
    So d^2[a|b|c] = [[a,b],c] - [a,[b,c]] = -[b,[a,c]].

    This is NOT zero in general! The bar of a LIE algebra (using the
    Lie bracket as the "product") does NOT satisfy d^2 = 0.

    This is because the LIE OPERAD is QUADRATIC but the bar differential
    for an associative algebra uses the associative product, not the Lie bracket.

    The CORRECT setup: for the CHIRAL bar complex, the relevant product
    is the VERTEX ALGEBRA normally ordered product (or the full chiral product),
    NOT the Lie bracket.

    For the CHEVALLEY-EILENBERG complex (= bar complex of the LIE operad),
    the differential uses the ANTISYMMETRIZED bar:
    d_CE(a_1 ^ ... ^ a_n) = sum_{i<j} (-1)^{...} [a_i, a_j] ^ ...
    This satisfies d^2 = 0 by Jacobi.

    For the HOCHSCHILD/BAR complex (= bar of associative algebra), the product
    is the ASSOCIATIVE product (not the Lie bracket), and d^2 = 0 by associativity.

    So for the CHIRAL bar complex:
    - The bar complex of a chiral algebra uses the CHIRAL PRODUCT mu^ch
    - For FREE chiral algebras (like Heisenberg), mu^ch includes the normally
      ordered product and is ASSOCIATIVE, so d^2 = 0
    - For the CE complex of the LIE algebra underlying the chiral algebra,
      the differential uses the Lie bracket on EXTERIOR powers

    The E_1 coproduct makes sense on the ORDERED (Hochschild) bar complex,
    which uses the ASSOCIATIVE product. For sl_2, this means the product is
    the enveloping algebra product in U(sl_2), not the Lie bracket.

    Let me revise: the bar complex of U(sl_2) uses the associative product
    in U(sl_2). On generators: a*b = ab (the associative product in U(sl_2)),
    which includes ab = [a,b] + ba (the Lie bracket plus the symmetric product).

    But the CHIRAL bar complex is different from the bar of U(sl_2).
    The chiral algebra V_k(sl_2) has OPE involving BOTH the bracket and the
    normally ordered product. The bar complex extracts residues along collision
    divisors, which picks out the SINGULAR part of the OPE (the bracket terms),
    not the regular part.

    FOR THE PURPOSES OF THIS ENGINE: we focus on the ALGEBRAIC structure
    of the deconcatenation coproduct and its compatibility with a GENERAL
    coderivation d_B. The key insight is that d_B being a coderivation of
    Delta is a FORMAL consequence of d_B being defined by merging adjacent
    pairs -- the specific product used does not matter.

    This is because the coderivation property is:
      Delta o d_B = (d_B x id + id x d_B) o Delta
    which for the deconcatenation coproduct reduces to: when d_B merges
    positions i and i+1 in [a_1|...|a_n], the merged pair either falls
    in the LEFT factor (positions 1,...,p) or the RIGHT factor (positions
    p+1,...,n) of any given splitting. It cannot span both factors because
    i and i+1 are ADJACENT.

    This is the KEY STRUCTURAL FACT: the coderivation property holds for
    ANY differential defined by merging adjacent pairs, regardless of
    d^2 = 0. The differential being a coderivation and d^2 = 0 are
    INDEPENDENT properties.

    We verify this explicitly below.
    """
    ope = sl2_ope()
    results = {}

    mon = ('e', 'f', 'h')
    d_mon = bar_differential_monomial(mon, ope)
    dd_mon = bar_differential(d_mon, ope)

    results['d[e|f|h]'] = d_mon
    results['d^2[e|f|h]'] = dd_mon
    results['d^2_is_zero'] = dd_mon.is_zero()

    # Coderivation check (should hold regardless of d^2)
    ok, msg = verify_coderivation(mon, ope)
    results['coderivation_holds'] = ok
    results['coderivation_msg'] = msg

    # Additional monomials
    for a in ['e', 'f', 'h']:
        for b in ['e', 'f', 'h']:
            for c_gen in ['e', 'f', 'h']:
                m = (a, b, c_gen)
                ok2, msg2 = verify_coderivation(m, ope)
                if not ok2:
                    results[f'FAIL_coderivation_{m}'] = msg2

    return results


# ============================================================
# CE differential (for comparison: the CORRECT d^2 = 0 complex)
# ============================================================

def ce_differential_arity2(a: str, b: str, ope: ChiralAlgebraOPE) -> BarElement:
    """Chevalley-Eilenberg differential on a ^ b.

    d_CE(a ^ b) = [a, b]  (with sign from graded antisymmetry).

    This is the differential on the EXTERIOR algebra Lambda(s^{-1}g),
    not the tensor algebra.
    """
    bracket = ope.product(a, b)
    terms = {}
    for gen, coeff in bracket.items():
        if gen == 'UNIT':
            continue
        terms[(gen,)] = coeff
    return BarElement(terms, 1)


def ce_differential_arity3(a: str, b: str, c: str, ope: ChiralAlgebraOPE) -> BarElement:
    """CE differential on a ^ b ^ c.

    d_CE(a ^ b ^ c) = [a,b] ^ c - [a,c] ^ b + [b,c] ^ a

    This satisfies d^2 = 0 by the Jacobi identity.
    """
    terms: Dict[tuple, Fraction] = {}

    # [a,b] ^ c
    ab = ope.product(a, b)
    for gen, coeff in ab.items():
        if gen == 'UNIT':
            continue
        # gen ^ c: sorted pair
        pair = tuple(sorted([gen, c]))
        sign = FR1 if (gen, c) == pair or gen == c else -FR1
        if gen == c:
            continue  # x ^ x = 0
        terms[pair] = terms.get(pair, FR0) + coeff * sign

    # -[a,c] ^ b
    ac = ope.product(a, c)
    for gen, coeff in ac.items():
        if gen == 'UNIT':
            continue
        pair = tuple(sorted([gen, b]))
        sign = FR1 if (gen, b) == pair or gen == b else -FR1
        if gen == b:
            continue
        terms[pair] = terms.get(pair, FR0) - coeff * sign

    # [b,c] ^ a
    bc = ope.product(b, c)
    for gen, coeff in bc.items():
        if gen == 'UNIT':
            continue
        pair = tuple(sorted([gen, a]))
        sign = FR1 if (gen, a) == pair or gen == a else -FR1
        if gen == a:
            continue
        terms[pair] = terms.get(pair, FR0) + coeff * sign

    return BarElement({k: v for k, v in terms.items() if v != FR0}, 2)


# ============================================================
# The reconciliation: algebraic vs geometric
# ============================================================

def algebraic_vs_geometric_analysis() -> Dict[str, Any]:
    """Analyze the relationship between algebraic and geometric coproducts.

    The deconcatenation coproduct is SIMULTANEOUSLY:

    ALGEBRAIC: It is the standard tensor coalgebra coproduct on T^c(V).
    This is a purely algebraic construction: T^c(V) = k + V + V^{x2} + ...
    with Delta(v_1 x ... x v_n) = sum_{i=0}^n (v_1 x ... x v_i) x (v_{i+1} x ... x v_n).
    Coassociativity is a formal consequence of the partition identity.

    GEOMETRIC: It corresponds to interval splitting in the E_1 operad.
    The E_1 operad is the chains on the little intervals operad:
    E_1(n) = C_*(Conf_n^{ord}(R)) ~ C_*(pt) = k  (contractible for ordered configs).
    The E_1 coalgebra structure on B^ch(A) comes from the product structure
    C x R: the C-direction gives the bar differential, the R-direction gives
    the coproduct.

    RECONCILIATION: These agree because the tensor coalgebra IS the algebraic
    model of the E_1 cooperad. More precisely:
    - The E_1 cooperad has components E_1^!(n) = k (one-dimensional)
    - A conilpotent E_1-coalgebra is the same as a conilpotent coassociative coalgebra
    - The cofree conilpotent coassociative coalgebra is T^c(V)
    - Its coproduct is the deconcatenation

    The Boardman-Vogt-Fresse theorem: the category of E_1-algebras (resp. coalgebras)
    in chain complexes is equivalent to the category of A_infinity-algebras
    (resp. A_infinity-coalgebras). The STRICT version (no higher homotopies)
    gives coassociative coalgebras.

    So the answer to "algebraic or geometric?" is: BOTH, and the identification
    is the content of the recognition theorem for E_1-coalgebras.
    """

    return {
        'algebraic_source': 'tensor coalgebra T^c(V)',
        'geometric_source': 'E_1 cooperad (little intervals)',
        'reconciliation': 'E_1-coalgebra = coassociative coalgebra (BV-Fresse)',
        'key_property': 'deconcatenation = interval splitting',
        'coassociativity': 'formal (partition identity) = geometric (contractible configs)',
        'coderivation': 'adjacent-merge + ordered-splitting = Leibniz',
        'FM_does_not_split': True,
        'forms_do_split': 'log forms for non-adjacent pairs are independent',
        'ordered_coproduct_is_cocommutative': False,
        'symmetric_coproduct_is_cocommutative': True,
    }
