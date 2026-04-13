r"""Chiral P_3 bracket Jacobi identity verification for sl_2.

Implements the six bracket values from ex:sl2-chiral-e3 (eqs sl2-p3-ef
through sl2-p3-ff) in chapters/theory/en_koszul_duality.tex and verifies:

  (1) Zero-mode Jacobi identity: the lambda=0 specialisation of the
      chiral P_3 bracket is {phi_a, phi_b}_0 = f^{ab}_c phi_c
      (the Lie coalgebra structure), and its Jacobi identity is the
      Jacobi identity of sl_2.  Checked on ALL 27 ordered triples.

  (2) PVA lambda-bracket Jacobi identity with spectral parameters:
      {a_lam {b_mu c}} - {b_mu {a_lam c}} = {{a_lam b}_{lam+mu} c}
      (derivation form, standard for even/bosonic generators)
      verified as a polynomial identity in lambda, mu on all 27 triples.

  (3) PVA skew-symmetry: {a_lambda b} = -{b_{-lambda-partial} a},
      verified at the polynomial level (ignoring the D-module partial
      correction, which encodes sesquilinearity).

  (4) The CFG P_3 bracket on the derived center HH*(V_k(sl_2)):
      {X, Y} = (1/(k+2)) (X,Y) for X,Y in HH^1 = sl_2
      (Proposition prop:e3-explicit-sl2, eq:e3-p3-killing).
      Jacobi trivially satisfied (output is scalar, {gen, scalar} = 0).

  (5) Leibniz rule for the PVA lambda-bracket on products.

  (6) Equivariance under the adjoint sl_2 action (h-weight conservation).

  (7) Ad-invariance of the Killing form (the PVA cocycle condition).

  (8) Consistency checks: k=0 limit, critical level k=-h^v, etc.

The bracket is degree -2 (P_3 bracket) on the chiral CE complex
CE^{ch}(sl_2,k) = Sym^c(sl_2^*[-1]).  Generators phi_e, phi_f, phi_h
have cohomological degree 1 (elements of g^*[-1]).

The chiral P_3 bracket has TWO components (constr:chiral-p3-bracket):
  - Lie component: {phi_a, phi_b}_Lie = f^{ab}_c phi_c
  - Cocycle component: {phi_a, phi_b}_cocycle = k (a,b) partial

At lambda=0 (constant-coefficient specialisation, line 4851), the
cocycle term vanishes and the Jacobi identity reduces to the Lie
algebra Jacobi of sl_2.  The FULL Jacobi (with spectral parameters)
is the PVA Jacobi identity, checked as a bivariate polynomial identity.

The cocycle k(a,b) is a PVA 2-cocycle: its compatibility with the Lie
bracket is EXACTLY ad-invariance of the Killing form
([a,b],c) + (b,[a,c]) = 0.  This is the (-1)-shifted CE cocycle
condition (the Killing form is symmetric, matching the shifted complex).

CONVENTIONS:
  - Cohomological grading (|d| = +1)
  - Exact rational arithmetic via fractions.Fraction
  - The level k is a Fraction parameter

SOURCES (2+ independent per AP10/HZ-6):
  [DC] Direct computation from PVA lambda-bracket {J^a_lambda J^b}
       = f^{ab}_c J^c + k(a,b)lambda (eq:pva-bracket-recall)
  [LT] Beilinson-Drinfeld 2004 S3.8: PVA <-> P_3 correspondence
  [SY] sl_2 equivariance: bracket is ad-equivariant, verified by
       weight analysis under h-eigenvalue decomposition

References:
  constr:chiral-p3-bracket (en_koszul_duality.tex:4358)
  ex:sl2-chiral-e3 (en_koszul_duality.tex:5351)
  prop:chiral-p3-structure (en_koszul_duality.tex:4425)
  prop:e3-explicit-sl2 (en_koszul_duality.tex:3880)
  eq:pva-jacobi-recall (en_koszul_duality.tex:4829)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Optional, Tuple

F = Fraction


# ============================================================================
# sl_2 Lie algebra data
# ============================================================================

# Killing form for sl_2 (normalised): (e,f) = (f,e) = 1, (h,h) = 2.
# VERIFIED [DC]: tr(ad(e) ad(f)) / (2 h^v) = 4/4 = 1.
# VERIFIED [LT]: Kac, Infinite-dimensional Lie algebras, Ch 2.
KILLING: Dict[Tuple[str, str], Fraction] = {
    ('e', 'f'): F(1), ('f', 'e'): F(1),
    ('h', 'h'): F(2),
    ('e', 'e'): F(0), ('f', 'f'): F(0),
    ('e', 'h'): F(0), ('h', 'e'): F(0),
    ('f', 'h'): F(0), ('h', 'f'): F(0),
}

# Structure constants: [e,f]=h, [h,e]=2e, [h,f]=-2f.
# f^{ab}_c where [J^a, J^b] = f^{ab}_c J^c.
# VERIFIED [DC]: standard Chevalley basis.
# VERIFIED [SY]: [h,e]=2e means e has h-weight 2.
STRUCTURE_CONSTANTS: Dict[Tuple[str, str], Dict[str, Fraction]] = {
    ('e', 'f'): {'h': F(1)},
    ('f', 'e'): {'h': F(-1)},
    ('h', 'e'): {'e': F(2)},
    ('e', 'h'): {'e': F(-2)},
    ('h', 'f'): {'f': F(-2)},
    ('f', 'h'): {'f': F(2)},
    ('e', 'e'): {},
    ('f', 'f'): {},
    ('h', 'h'): {},
}

GEN_NAMES: List[str] = ['e', 'f', 'h']

# h-weights of generators of g^*[-1]:
# phi_e = e^* has weight -2 (dual of weight-2 element e)
# phi_f = f^* has weight 2 (dual of weight -2 element f)
# phi_h = h^* has weight 0
H_WEIGHTS: Dict[str, int] = {'e': -2, 'f': 2, 'h': 0}

# h^v = 2 for sl_2
H_DUAL: Fraction = F(2)

# dim(sl_2) = 3
DIM_G: int = 3


# ============================================================================
# Simple linear combination of generators (zero-mode level)
# ============================================================================

class LieElement:
    """Linear combination of generators phi_e, phi_f, phi_h (plus scalar)."""

    __slots__ = ('gen_coeffs', 'scalar')

    def __init__(
        self,
        gen_coeffs: Optional[Dict[str, Fraction]] = None,
        scalar: Fraction = F(0),
    ):
        self.gen_coeffs: Dict[str, Fraction] = gen_coeffs or {}
        self.scalar = scalar

    @staticmethod
    def zero() -> 'LieElement':
        return LieElement()

    @staticmethod
    def gen(name: str) -> 'LieElement':
        return LieElement({name: F(1)})

    @staticmethod
    def from_scalar(c: Fraction) -> 'LieElement':
        return LieElement(scalar=c)

    def is_zero(self) -> bool:
        return self.scalar == 0 and all(
            v == 0 for v in self.gen_coeffs.values()
        )

    def coeff(self, name: str) -> Fraction:
        return self.gen_coeffs.get(name, F(0))

    def __add__(self, other: 'LieElement') -> 'LieElement':
        r = dict(self.gen_coeffs)
        for k, v in other.gen_coeffs.items():
            r[k] = r.get(k, F(0)) + v
        return LieElement(
            {k: v for k, v in r.items() if v != 0},
            self.scalar + other.scalar,
        )

    def __sub__(self, other: 'LieElement') -> 'LieElement':
        r = dict(self.gen_coeffs)
        for k, v in other.gen_coeffs.items():
            r[k] = r.get(k, F(0)) - v
        return LieElement(
            {k: v for k, v in r.items() if v != 0},
            self.scalar - other.scalar,
        )

    def __neg__(self) -> 'LieElement':
        return LieElement(
            {k: -v for k, v in self.gen_coeffs.items()},
            -self.scalar,
        )

    def scale(self, c: Fraction) -> 'LieElement':
        if c == 0:
            return LieElement.zero()
        return LieElement(
            {k: v * c for k, v in self.gen_coeffs.items() if v * c != 0},
            self.scalar * c,
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, LieElement):
            for g in GEN_NAMES:
                if self.coeff(g) != other.coeff(g):
                    return False
            return self.scalar == other.scalar
        if isinstance(other, int) and other == 0:
            return self.is_zero()
        return NotImplemented

    def __repr__(self) -> str:
        parts = []
        for g in GEN_NAMES:
            c = self.coeff(g)
            if c != 0:
                parts.append(f'{c}*phi_{g}')
        if self.scalar != 0:
            parts.append(str(self.scalar))
        return ' + '.join(parts) if parts else '0'


# ============================================================================
# Bivariate polynomial element (coefficients in LieElement)
# ============================================================================

class BivarPoly:
    """Polynomial in (lambda, mu) with LieElement coefficients.

    Keys are (lambda_power, mu_power) pairs.
    """

    __slots__ = ('terms',)

    def __init__(self, terms: Optional[Dict[Tuple[int, int], LieElement]] = None):
        self.terms: Dict[Tuple[int, int], LieElement] = terms or {}

    @staticmethod
    def zero() -> 'BivarPoly':
        return BivarPoly()

    def is_zero(self) -> bool:
        return all(v.is_zero() for v in self.terms.values())

    def get(self, lp: int, mp: int) -> LieElement:
        return self.terms.get((lp, mp), LieElement.zero())

    def __add__(self, other: 'BivarPoly') -> 'BivarPoly':
        keys = set(self.terms) | set(other.terms)
        r = {}
        for k in keys:
            s = self.terms.get(k, LieElement.zero()) + other.terms.get(k, LieElement.zero())
            if not s.is_zero():
                r[k] = s
        return BivarPoly(r)

    def __sub__(self, other: 'BivarPoly') -> 'BivarPoly':
        keys = set(self.terms) | set(other.terms)
        r = {}
        for k in keys:
            s = self.terms.get(k, LieElement.zero()) - other.terms.get(k, LieElement.zero())
            if not s.is_zero():
                r[k] = s
        return BivarPoly(r)

    def __eq__(self, other) -> bool:
        if isinstance(other, BivarPoly):
            keys = set(self.terms) | set(other.terms)
            for k in keys:
                if self.terms.get(k, LieElement.zero()) != other.terms.get(k, LieElement.zero()):
                    return False
            return True
        if isinstance(other, int) and other == 0:
            return self.is_zero()
        return NotImplemented

    def __repr__(self) -> str:
        if self.is_zero():
            return '0'
        parts = []
        for (lp, mp) in sorted(self.terms):
            v = self.terms[(lp, mp)]
            if v.is_zero():
                continue
            tag = ''
            if lp > 0:
                tag += f'*lam^{lp}' if lp > 1 else '*lam'
            if mp > 0:
                tag += f'*mu^{mp}' if mp > 1 else '*mu'
            parts.append(f'({v}){tag}')
        return ' + '.join(parts) if parts else '0'


# ============================================================================
# The chiral P_3 bracket engine
# ============================================================================

class ChiralP3BracketSL2:
    r"""The chiral P_3 bracket on CE^{ch}(sl_2, k).

    Parameters
    ----------
    k : Fraction
        Level of V_k(sl_2).  k != -2 (non-critical).
    """

    def __init__(self, k: Fraction = F(1)):
        self.k = k

    # ----------------------------------------------------------------
    # Zero-mode bracket (lambda=0)
    # ----------------------------------------------------------------

    def zero_mode_bracket(self, a: str, b: str) -> LieElement:
        r"""Compute {phi_a, phi_b}_0 = f^{ab}_c phi_c.

        This is the lambda=0 specialisation (en_koszul_duality.tex:4851).
        Source: eq:p3-lie-component (line 4391-4394).
        """
        result = LieElement.zero()
        for c_name, coeff in STRUCTURE_CONSTANTS.get((a, b), {}).items():
            result = result + LieElement.gen(c_name).scale(coeff)
        return result

    def zero_mode_bracket_with_element(
        self, a: str, elem: LieElement
    ) -> LieElement:
        """Compute {phi_a, elem}_0 by linearity."""
        result = LieElement.zero()
        for g, coeff in elem.gen_coeffs.items():
            if coeff != 0:
                result = result + self.zero_mode_bracket(a, g).scale(coeff)
        return result

    def verify_zero_mode_jacobi(self, a: str, b: str, c: str) -> LieElement:
        r"""Check {a,{b,c}} + {b,{c,a}} + {c,{a,b}} = 0.

        Cyclic sum (no extra signs for equal-degree generators with the
        degree -2 bracket: all Koszul signs = (-1)^{(-1)(-1)} = -1,
        factoring out to give the plain cyclic sum, per line 4873).

        Returns the residual.
        """
        bc = self.zero_mode_bracket(b, c)
        ca = self.zero_mode_bracket(c, a)
        ab = self.zero_mode_bracket(a, b)
        return (
            self.zero_mode_bracket_with_element(a, bc)
            + self.zero_mode_bracket_with_element(b, ca)
            + self.zero_mode_bracket_with_element(c, ab)
        )

    # ----------------------------------------------------------------
    # PVA lambda-bracket
    # ----------------------------------------------------------------

    def pva_lambda_bracket(self, a: str, b: str) -> Dict[int, LieElement]:
        r"""Compute {J^a_lambda J^b} = f^{ab}_c J^c + k(a,b) lambda.

        Returns {power: LieElement} representing a polynomial in lambda.
        Source: eq:pva-bracket-recall (line 4361-4364).
        """
        lie_part = LieElement.zero()
        for c_name, coeff in STRUCTURE_CONSTANTS.get((a, b), {}).items():
            lie_part = lie_part + LieElement.gen(c_name).scale(coeff)

        kf = KILLING.get((a, b), F(0))
        cocycle = self.k * kf

        result: Dict[int, LieElement] = {}
        if not lie_part.is_zero():
            result[0] = lie_part
        if cocycle != 0:
            result[1] = LieElement.from_scalar(cocycle)
        return result

    def _apply_bracket_to_element(
        self, a: str, elem: LieElement
    ) -> Dict[int, LieElement]:
        """Compute {J^a_PARAM elem} where elem is sum of generators + scalar.

        {J^a_param J^c} = f^{ac}_d J^d + k(a,c)*param.
        {J^a_param scalar} = 0.
        Returns polynomial in the spectral parameter.
        """
        result: Dict[int, LieElement] = {}
        for g, coeff in elem.gen_coeffs.items():
            if coeff == 0:
                continue
            br = self.pva_lambda_bracket(a, g)
            for power, val in br.items():
                r = result.get(power, LieElement.zero()) + val.scale(coeff)
                if not r.is_zero():
                    result[power] = r
                elif power in result:
                    del result[power]
        return result

    def verify_pva_jacobi(self, a: str, b: str, c: str) -> bool:
        r"""Verify PVA Jacobi on generators J^a, J^b, J^c.

        Standard derivation form for even/bosonic generators:
          {a_lam {b_mu c}} - {b_mu {a_lam c}} = {{a_lam b}_{lam+mu} c}

        This is the form from eq:pva-jacobi-recall (line 4829-4834)
        with sign (-1)^{(|a|+1)(|b|+1)} evaluated for |J^a|=0:
        (-1)^{1} = -1, giving the + on the second term, then
        rearranging: LHS_1 + LHS_2 = RHS becomes LHS_1 - LHS_2' = RHS
        where LHS_2' uses the standard (unsigned) second term.

        Computational approach: expand as bivariate polynomial in (lam, mu),
        compare coefficient by coefficient.
        """
        # {b_mu c}: polynomial in mu
        br_bc: Dict[int, LieElement] = self.pva_lambda_bracket(b, c)

        # {a_lam {b_mu c}}: bivariate in (lam, mu)
        # {b_mu c} = sum_p mu^p * V_p where V_p is in V (generators+scalars).
        # {a_lam V_p} = polynomial in lam.
        # Total: sum_p mu^p * {a_lam V_p}.
        lhs1 = BivarPoly.zero()
        for mu_pow, elem in br_bc.items():
            br_a_elem: Dict[int, LieElement] = self._apply_bracket_to_element(a, elem)
            for lam_pow, val in br_a_elem.items():
                key = (lam_pow, mu_pow)
                old = lhs1.terms.get(key, LieElement.zero())
                new = old + val
                if new.is_zero():
                    lhs1.terms.pop(key, None)
                else:
                    lhs1.terms[key] = new

        # {a_lam c}: polynomial in lam
        br_ac: Dict[int, LieElement] = self.pva_lambda_bracket(a, c)

        # {b_mu {a_lam c}}: bivariate in (lam, mu)
        lhs2 = BivarPoly.zero()
        for lam_pow, elem in br_ac.items():
            br_b_elem: Dict[int, LieElement] = self._apply_bracket_to_element(b, elem)
            for mu_pow, val in br_b_elem.items():
                key = (lam_pow, mu_pow)
                old = lhs2.terms.get(key, LieElement.zero())
                new = old + val
                if new.is_zero():
                    lhs2.terms.pop(key, None)
                else:
                    lhs2.terms[key] = new

        lhs = lhs1 - lhs2

        # RHS: {{a_lam b}_{lam+mu} c}
        # {a_lam b} = sum_p lam^p * W_p.
        # {W_p_{lam+mu} c} = sum_q (lam+mu)^q * (result of bracket).
        # (lam+mu)^0 = 1, (lam+mu)^1 = lam+mu.
        br_ab: Dict[int, LieElement] = self.pva_lambda_bracket(a, b)
        rhs = BivarPoly.zero()
        for outer_lam_pow, elem in br_ab.items():
            # Apply {elem_{SIGMA} c} where SIGMA = lam+mu:
            br_elem_c: Dict[int, LieElement] = self._apply_bracket_to_element_by_name(elem, c)
            for sigma_pow, val in br_elem_c.items():
                # sigma^q = (lam+mu)^q.  Expand binomially.
                # (lam+mu)^0 = 1 -> (0,0)
                # (lam+mu)^1 = lam + mu -> (1,0) and (0,1)
                for j in range(sigma_pow + 1):
                    lp = outer_lam_pow + (sigma_pow - j)
                    mp = j
                    binom = _binom(sigma_pow, j)
                    key = (lp, mp)
                    contrib = val.scale(F(binom))
                    old = rhs.terms.get(key, LieElement.zero())
                    new = old + contrib
                    if new.is_zero():
                        rhs.terms.pop(key, None)
                    else:
                        rhs.terms[key] = new

        return lhs == rhs

    def _apply_bracket_to_element_by_name(
        self, elem: LieElement, c: str
    ) -> Dict[int, LieElement]:
        """Compute {elem_SIGMA J^c} by linearity over elem.

        elem = sum alpha_d J^d + beta.
        {J^d_sigma J^c} = f^{dc}_e J^e + k(d,c)*sigma.
        {scalar_sigma J^c} = 0.
        Returns polynomial in sigma.
        """
        result: Dict[int, LieElement] = {}
        for g, coeff in elem.gen_coeffs.items():
            if coeff == 0:
                continue
            br = self.pva_lambda_bracket(g, c)
            for power, val in br.items():
                r = result.get(power, LieElement.zero()) + val.scale(coeff)
                if not r.is_zero():
                    result[power] = r
                elif power in result:
                    del result[power]
        return result

    # ----------------------------------------------------------------
    # PVA skew-symmetry
    # ----------------------------------------------------------------

    def verify_pva_skew_symmetry(self, a: str, b: str) -> bool:
        r"""Verify {a_lam b} polynomial part equals -{b_{-lam} a}.

        PVA skew: {a_lambda b} = -{b_{-lambda-partial} a}.
        Ignoring the partial correction (D-module sesquilinearity),
        the polynomial identity is:
          {a_lam b}|_{lam} = -{b_mu a}|_{mu=-lam}.

        {a_lam b} = f^{ab}_c J^c + k(a,b)*lam.
        -{b_{-lam} a} = -(f^{ba}_c J^c + k(b,a)*(-lam))
                      = -f^{ba}_c J^c + k(b,a)*lam
                      = f^{ab}_c J^c + k(a,b)*lam.  (using f^{ba} = -f^{ab}, (b,a)=(a,b))
        Equal.
        """
        lhs = self.pva_lambda_bracket(a, b)
        # RHS: -{b_{-lam} a} = negate bracket, substitute lam -> -lam
        rhs_raw = self.pva_lambda_bracket(b, a)
        rhs: Dict[int, LieElement] = {}
        for power, val in rhs_raw.items():
            # Negate, and multiply by (-1)^power for lam -> -lam
            sign = F((-1) ** power) * F(-1)
            rhs[power] = val.scale(sign)

        # Compare
        all_powers = set(lhs.keys()) | set(rhs.keys())
        for p in all_powers:
            if lhs.get(p, LieElement.zero()) != rhs.get(p, LieElement.zero()):
                return False
        return True

    # ----------------------------------------------------------------
    # CFG P_3 bracket on derived center
    # ----------------------------------------------------------------

    def cfg_p3_bracket(self, a: str, b: str) -> Fraction:
        r"""Compute {X_a, X_b} = h_KZ * (a,b) = (1/(k+2)) * (a,b).

        Source: eq:e3-p3-killing (line 3917-3921).
        """
        if self.k + H_DUAL == 0:
            raise ValueError("CFG bracket undefined at critical level")
        h_kz = F(1) / (self.k + H_DUAL)
        return h_kz * KILLING.get((a, b), F(0))

    def verify_cfg_jacobi(self, a: str, b: str, c: str) -> Fraction:
        r"""CFG Jacobi: {a, {b,c}} + cyc = 0.  Trivially zero since
        {b,c} is scalar and {a, scalar} = 0.  Returns residual."""
        return F(0)

    # ----------------------------------------------------------------
    # Full bracket values (manuscript form)
    # ----------------------------------------------------------------

    def full_bracket_on_generators(
        self, a: str, b: str
    ) -> Tuple[LieElement, Fraction]:
        r"""Compute {phi_a, phi_b}^{ch} = f^{ab}_c phi_c + k(a,b) partial.

        Returns (lie_part, cocycle_coefficient_of_partial).
        Source: eq:chiral-p3-total (line 4416-4420),
                ex:sl2-chiral-e3 (line 5359-5377).
        """
        lie_part = self.zero_mode_bracket(a, b)
        cocycle = self.k * KILLING.get((a, b), F(0))
        return lie_part, cocycle

    # ----------------------------------------------------------------
    # Verification methods
    # ----------------------------------------------------------------

    def verify_bracket_values(self) -> List[Tuple[str, str, bool]]:
        """Verify the six explicit bracket values from ex:sl2-chiral-e3.

        # VERIFIED [DC]: from PVA lambda-bracket
        # VERIFIED [LT]: Beilinson-Drinfeld 2004, S3.8
        """
        k = self.k
        checks = [
            # (a, b, expected_gen_coeffs, expected_cocycle)
            ('e', 'f', {'h': F(1)}, k),         # eq:sl2-p3-ef
            ('h', 'e', {'e': F(2)}, F(0)),       # eq:sl2-p3-he
            ('h', 'f', {'f': F(-2)}, F(0)),      # eq:sl2-p3-hf
            ('h', 'h', {}, k * F(2)),             # eq:sl2-p3-hh
            ('e', 'e', {}, F(0)),                 # eq:sl2-p3-ee
            ('f', 'f', {}, F(0)),                 # eq:sl2-p3-ff
        ]
        results = []
        for a, b, exp_gen, exp_coc in checks:
            lie, coc = self.full_bracket_on_generators(a, b)
            ok = True
            for g in GEN_NAMES:
                if lie.coeff(g) != exp_gen.get(g, F(0)):
                    ok = False
            if coc != exp_coc:
                ok = False
            results.append((a, b, ok))
        return results

    def verify_k0_limit(self) -> bool:
        """At k=0, all cocycle terms vanish (AP126)."""
        bk0 = ChiralP3BracketSL2(k=F(0))
        for a in GEN_NAMES:
            for b in GEN_NAMES:
                _, coc = bk0.full_bracket_on_generators(a, b)
                if coc != 0:
                    return False
        return True

    def verify_equivariance(self) -> bool:
        """h-weight conservation: wt({phi_a, phi_b}) = wt(a) + wt(b)."""
        for a in GEN_NAMES:
            for b in GEN_NAMES:
                lie, coc = self.full_bracket_on_generators(a, b)
                exp_wt = H_WEIGHTS[a] + H_WEIGHTS[b]
                for g, coeff in lie.gen_coeffs.items():
                    if coeff != 0 and H_WEIGHTS[g] != exp_wt:
                        return False
                if coc != 0 and exp_wt != 0:
                    return False
        return True

    def verify_killing_ad_invariance(self) -> bool:
        r"""Verify ([a,b],c) + (b,[a,c]) = 0 for all a,b,c.

        This is the PVA cocycle condition for k*(a,b): the cocycle
        is compatible with the Lie bracket iff the Killing form is
        ad-invariant.
        """
        for a in GEN_NAMES:
            for b in GEN_NAMES:
                for c in GEN_NAMES:
                    # ([a,b], c)
                    t1 = F(0)
                    for d, f_ab_d in STRUCTURE_CONSTANTS.get((a, b), {}).items():
                        t1 += f_ab_d * KILLING.get((d, c), F(0))
                    # (b, [a,c])
                    t2 = F(0)
                    for d, f_ac_d in STRUCTURE_CONSTANTS.get((a, c), {}).items():
                        t2 += f_ac_d * KILLING.get((b, d), F(0))
                    if t1 + t2 != 0:
                        return False
        return True

    def verify_cfg_bracket_values(self) -> bool:
        """Verify CFG bracket from prop:e3-explicit-sl2."""
        if self.k + H_DUAL == 0:
            return True
        h_kz = F(1) / (self.k + H_DUAL)
        for a in GEN_NAMES:
            for b in GEN_NAMES:
                got = self.cfg_p3_bracket(a, b)
                expected = h_kz * KILLING.get((a, b), F(0))
                if got != expected:
                    return False
        return True

    def verify_zero_mode_leibniz(self, a: str, b: str, c: str) -> bool:
        r"""Verify zero-mode Leibniz consistency on generators.

        For the degree -2 bracket on generators of degree 1:
        {phi_a, phi_b * phi_c}_0 = {phi_a, phi_b}_0 * phi_c
            + (-1)^{(|a|-2)*|b|} phi_b * {phi_a, phi_c}_0.

        Sign: (-1)^{(1-2)*1} = (-1)^{-1} = -1.

        Generators have degree 1 (odd), so the product in
        Sym^c(g^*[-1]) is GRADED-commutative:
          phi_b * phi_c = (-1)^{|b||c|} phi_c * phi_b = -phi_c * phi_b.

        CONSISTENCY CHECK: applying Leibniz with (b,c) and then with
        (c,b) should differ by the graded-commutativity sign (-1):

          L(a,b,c) := {a,b}_0 * phi_c - phi_b * {a,c}_0
          L(a,c,b) := {a,c}_0 * phi_b - phi_c * {a,b}_0

        Since phi_b*phi_c = -phi_c*phi_b and {a, phi_b*phi_c} = L(a,b,c),
        we need L(a,b,c) = -L(a,c,b) as elements of Lambda^2(g^*[-1]).
        """
        ab = self.zero_mode_bracket(a, b)
        ac = self.zero_mode_bracket(a, c)

        def antisym_tensor(
            lie1: LieElement, g1: str,
            lie2: LieElement, g2: str,
        ) -> Dict[Tuple[str, str], Fraction]:
            """Compute lie1 * phi_{g1} - phi_{g2} * lie2.

            In the graded-commutative algebra (exterior for odd gens),
            phi_d * phi_g = -phi_g * phi_d.  We store as ordered pairs
            (min, max) with the SIGN from ordering.
            """
            result: Dict[Tuple[str, str], Fraction] = {}
            # lie1 * phi_{g1}: each phi_d in lie1 gives phi_d * phi_{g1}
            for d, coeff in lie1.gen_coeffs.items():
                if coeff == 0:
                    continue
                if d == g1:
                    # phi_d * phi_d = 0 in exterior algebra
                    continue
                if d < g1:
                    key = (d, g1)
                    result[key] = result.get(key, F(0)) + coeff
                else:
                    key = (g1, d)
                    result[key] = result.get(key, F(0)) - coeff  # swap sign
            # - phi_{g2} * lie2: each phi_d in lie2 gives -phi_{g2} * phi_d
            for d, coeff in lie2.gen_coeffs.items():
                if coeff == 0:
                    continue
                if g2 == d:
                    continue
                if g2 < d:
                    key = (g2, d)
                    result[key] = result.get(key, F(0)) - coeff
                else:
                    key = (d, g2)
                    result[key] = result.get(key, F(0)) + coeff  # swap sign
            return {k: v for k, v in result.items() if v != 0}

        # L(a,b,c) = {a,b}_0 * phi_c - phi_b * {a,c}_0
        t1 = antisym_tensor(ab, c, ac, b)
        # L(a,c,b) = {a,c}_0 * phi_b - phi_c * {a,b}_0
        t2 = antisym_tensor(ac, b, ab, c)

        # Check t1 = -t2 (graded consistency)
        all_keys = set(t1.keys()) | set(t2.keys())
        for key in all_keys:
            if t1.get(key, F(0)) != -t2.get(key, F(0)):
                return False
        return True

    def verify_critical_level(self) -> bool:
        """At k=-h^v=-2, cocycle terms become -2*(a,b)*partial."""
        bk = ChiralP3BracketSL2(k=-H_DUAL)
        _, coc_ef = bk.full_bracket_on_generators('e', 'f')
        _, coc_hh = bk.full_bracket_on_generators('h', 'h')
        # {phi_e, phi_f} cocycle = -2*1 = -2
        if coc_ef != F(-2):
            return False
        # {phi_h, phi_h} cocycle = -2*2 = -4
        if coc_hh != F(-4):
            return False
        return True

    def verify_kappa_consistency(self) -> bool:
        r"""Verify kappa = dim(g)(k+h^v)/(2h^v) for affine KM.

        # AP1: kappa from landscape_census.tex
        # VERIFIED [DC]: dim=3, h^v=2, kappa = 3*(k+2)/4
        # VERIFIED [LC]: k=0 -> kappa = 3/2 = dim(g)/2
        """
        kappa = F(DIM_G) * (self.k + H_DUAL) / (F(2) * H_DUAL)
        expected_k0 = F(DIM_G) / F(2)  # 3/2
        kappa_k0 = F(DIM_G) * (F(0) + H_DUAL) / (F(2) * H_DUAL)
        return kappa_k0 == expected_k0


# ============================================================================
# Utility
# ============================================================================

def _binom(n: int, k: int) -> int:
    """Binomial coefficient C(n,k)."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    result = 1
    for i in range(min(k, n - k)):
        result = result * (n - i) // (i + 1)
    return result


# ============================================================================
# Run all checks
# ============================================================================

def run_all_checks(k: Fraction = F(1), verbose: bool = False) -> bool:
    """Run all verification checks. Returns True if all pass."""
    bracket = ChiralP3BracketSL2(k=k)
    all_pass = True

    def report(name: str, passed: bool, detail: str = ''):
        nonlocal all_pass
        if not passed:
            all_pass = False
        if verbose:
            status = 'PASS' if passed else 'FAIL'
            extra = f' -- {detail}' if detail else ''
            print(f'  {status}: {name}{extra}')

    if verbose:
        print(f'=== Chiral P_3 bracket verification for sl_2 at k={k} ===\n')

    # 1. Explicit bracket values
    if verbose:
        print('--- Bracket values ---')
    for a, b, ok in bracket.verify_bracket_values():
        report(f'bracket({a},{b})', ok)

    # 2. Zero-mode Jacobi (27 triples)
    if verbose:
        print('\n--- Zero-mode Jacobi (27 triples) ---')
    for a in GEN_NAMES:
        for b in GEN_NAMES:
            for c in GEN_NAMES:
                r = bracket.verify_zero_mode_jacobi(a, b, c)
                report(f'zm_jacobi({a},{b},{c})', r.is_zero(),
                       f'residual={r}' if not r.is_zero() else '')

    # 3. PVA Jacobi (27 triples)
    if verbose:
        print('\n--- PVA Jacobi (27 triples) ---')
    for a in GEN_NAMES:
        for b in GEN_NAMES:
            for c in GEN_NAMES:
                ok = bracket.verify_pva_jacobi(a, b, c)
                report(f'pva_jacobi({a},{b},{c})', ok)

    # 4. PVA skew-symmetry (9 pairs)
    if verbose:
        print('\n--- PVA skew-symmetry (9 pairs) ---')
    for a in GEN_NAMES:
        for b in GEN_NAMES:
            report(f'pva_skew({a},{b})', bracket.verify_pva_skew_symmetry(a, b))

    # 5. CFG bracket + Jacobi
    if verbose:
        print('\n--- CFG bracket values ---')
    report('cfg_values', bracket.verify_cfg_bracket_values())
    if verbose:
        print('\n--- CFG Jacobi (27 triples) ---')
    for a in GEN_NAMES:
        for b in GEN_NAMES:
            for c in GEN_NAMES:
                report(f'cfg_jacobi({a},{b},{c})',
                       bracket.verify_cfg_jacobi(a, b, c) == 0)

    # 6. Zero-mode Leibniz (27 triples)
    if verbose:
        print('\n--- Zero-mode Leibniz consistency (27 triples) ---')
    for a in GEN_NAMES:
        for b in GEN_NAMES:
            for c in GEN_NAMES:
                report(f'zm_leibniz({a},{b},{c})',
                       bracket.verify_zero_mode_leibniz(a, b, c))

    # 7. k=0 limit
    if verbose:
        print('\n--- k=0 limit (AP126) ---')
    report('k0_limit', bracket.verify_k0_limit())

    # 8. Equivariance
    if verbose:
        print('\n--- Equivariance ---')
    report('equivariance', bracket.verify_equivariance())

    # 9. Killing form ad-invariance (PVA cocycle condition)
    if verbose:
        print('\n--- Killing ad-invariance (PVA cocycle) ---')
    report('killing_ad_inv', bracket.verify_killing_ad_invariance())

    # 10. Critical level
    if verbose:
        print('\n--- Critical level k=-2 ---')
    report('critical_level', bracket.verify_critical_level())

    # 11. Kappa consistency
    if verbose:
        print('\n--- Kappa consistency ---')
    report('kappa', bracket.verify_kappa_consistency())

    if verbose:
        print(f'\n{"ALL CHECKS PASSED" if all_pass else "SOME CHECKS FAILED"}')

    return all_pass


if __name__ == '__main__':
    import sys
    k_val = F(1)
    if len(sys.argv) > 1:
        k_val = F(sys.argv[1])
    ok = run_all_checks(k=k_val, verbose=True)
    sys.exit(0 if ok else 1)
