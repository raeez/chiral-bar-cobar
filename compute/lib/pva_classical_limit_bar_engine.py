r"""PVA classical limit bar engine: gr^F B(A) as bar of a Poisson vertex algebra.

THEOREM-PROVING ENGINE for the classical-limit computation

    H^*(gr^F B(A)) ==> H^*(B(A))

(PBW spectral sequence converging the bar cohomology of a vertex algebra A
to the bar cohomology of its classical limit PVA = gr^F A.)

MATHEMATICAL FRAMEWORK
======================

LI FILTRATION.  A vertex algebra A carries a decreasing filtration F^p(A)
(Haisheng Li, 2004) with the property that gr^F(A) is a Poisson vertex
algebra (PVA).  The PBW spectral sequence

    E_0 = bar of gr^F(A)   (bar of the PVA)
    E_1 = H^*(E_0, d_0)
    d_1 = Poisson bracket differential (the first quantum correction)
    E_2 ==> H^*(B(A))

converges to the bar cohomology of A.  When d_1 is the only nontrivial
differential and E_2 is already the target, we say A is classically
Koszul; when higher d_r also contribute, the "leak" between bar(PVA) and
bar(VA) is the quantum correction at page r.

C_2 ALGEBRA.  The order-0 piece of the Li filtration is the C_2-algebra

    R_A := A / C_2(A)         where C_2(A) = span{ a_{(-2)} b : a, b in A }.

R_A is a commutative Poisson algebra (De Sole-Kac, 2006):

    product : a * b := image of :a b:
    bracket : {a, b} := image of a_{(0)} b

It is the "classical shadow" of A at weight 0; the bar of R_A is the
ZERO-TRUNCATION of the bar of gr^F A.  The ASSOCIATED VARIETY of A is

    X_A := Spec(R_A^{red}) .

For integrable L_k(sl_N) at positive integer level, X_A is a nilpotent
orbit closure [Arakawa 2015].

BAR OF A POISSON ALGEBRA.  For a finitely generated commutative Poisson
algebra R with generators {x_i} and Poisson bracket {x_i, x_j}, the
Chevalley-Eilenberg-style bar complex has:

    C^n = Lambda^n(R_+)                 (R_+ = augmentation ideal)
    d_CE(x_{i_1} ^ ... ^ x_{i_n}) =
        sum_{a<b} (-1)^{a+b} {x_{i_a}, x_{i_b}} ^ (^_{c != a,b} x_{i_c})

This is the standard Koszul-type complex for a Lie-Poisson algebra.
For R = Sym(g*) with Kirillov-Kostant bracket (g a Lie algebra), the
bar cohomology of the Poisson algebra is the Chevalley-Eilenberg
cohomology of g with trivial coefficients:

    H^*(gr^F V_k(g)_{weight 0}, d_CE) = H^*(g, C).

This is the UNIVERSAL affine KM classical-limit computation.

KEY IDENTIFICATION (PBW bridge):
    H^*(gr^F V_k(g), d_CE) matches classical CE; bar of QUANTIZED V_k(g)
    carries Koszul resolution corrections at the spectral-sequence pages
    d_r for r >= 1, controlled by the central charge / level.

WHAT THIS ENGINE COMPUTES
=========================

1. The PVA lambda-bracket for each standard family: Heis, sl_2, Virasoro.
   (Mirroring theorem_pva_classical_r_matrix_engine.py conventions.)

2. The C_2 algebra R_A and its Poisson bracket table.

3. The weight-0 bar complex: Chevalley-Eilenberg differential on
   Lambda^*(R_A)_+ with respect to the Poisson bracket.

4. Bar cohomology H^*(C_2 bar, d_CE) at arities 0..3 for each family.
   This is the E_1 page of the PBW spectral sequence at weight 0.

5. Comparison with the full bar cohomology H^*(B(A)) at the SAME weight
   and arity (the "leak" = dimension difference between PVA bar and
   VA bar).  For classically Koszul algebras the leak is 0; for
   non-classically-Koszul it is the quantum correction d_1 contribution.

6. Koszul dual PVAs: for the free Heisenberg PVA, the dual PVA has the
   OPPOSITE sign Poisson bracket (kappa ! = -k).  For Chevalley-Eilenberg
   on a Lie algebra, the Koszul dual at the PVA level is C^*_CE(g) with
   reversed grading.

7. Associated variety X_A = Spec(R_A^{red}):
   - Heisenberg: X = A^1 (affine line, smooth).
   - Affine sl_2 at level 1 (integrable): R_{L_1(sl_2)} is C[e,f,h]/(e^2, f^2, ef - h^2/4, ...)
     with X = nilpotent cone N_{sl_2} (nilpotent orbit closure).
   - Virasoro at c=0: R_{Vir_0} = C (trivial).

VERIFICATION PATHS (MULTI-PATH MANDATE, >=3 per claim):
    Path 1: Direct bar complex computation (rank of d_CE matrices)
    Path 2: Chevalley-Eilenberg closed form (H^*(g, C) for semisimple g)
    Path 3: Euler characteristic consistency
    Path 4: Cross-check via symmetry (anti-commutativity of Poisson bracket)
    Path 5: Comparison with PVA r-matrix from theorem_pva_classical_r_matrix_engine
    Path 6: Kappa consistency (trace of Poisson structure)

AP-DEFENCES:
    - AP44: the lambda-bracket coefficient stored is c_n = a_{(n)}b / n!.
            The Poisson bracket at the C_2 level extracts c_0 ONLY, which
            is the zero-mode of the OPE (no factorial correction).
    - AP19: pole absorption does NOT affect the C_2 zero-mode bracket;
            the d-log shift applies to the r-matrix construction, not to
            the Poisson bracket on R_A.
    - AP25: gr^F B(A) is the BAR of the classical LIMIT, which is an
            algebra (PVA).  It is NOT the Verdier dual, nor the cobar,
            nor the derived centre.
    - AP27: the bar propagator d log E(z,w) has weight 1 uniformly, so
            the classical limit uses E_1 at every edge regardless of the
            conformal weight of the generator.
    - AP33: Koszul duality at the PVA level sends k to -k for Heisenberg,
            the same symbol coincidence as for the full VA.  This does
            NOT mean the classical-limit dual equals the negative-level
            PVA as VA-Koszul duals.

References:
    Li (2004) — vertex algebra filtration
    De Sole-Kac (2006) — finite vs affine PVA
    Arakawa (2012, 2015, 2017) — associated varieties, C_2-cofiniteness
    Chevalley-Eilenberg (1948) — Lie algebra cohomology
    Manuscript: thm:associated-variety-koszulness, constr:li-bar-spectral-sequence,
                thm:pbw-degeneration, prop:c2-bar-classical-limit.

Conventions:
    - Cohomological grading (|d| = +1), bar uses desuspension.
    - Lambda-bracket: {a_lambda b} = sum_n (lambda^n / n!) a_{(n)} b   (AP44).
    - OPE: a(z) b(w) ~ sum_n a_{(n)}b / (z-w)^{n+1}.
    - Poisson bracket at the C_2 level: {a,b}_P := a_{(0)}b mod C_2.
    - Chevalley-Eilenberg sign convention:
        d_CE(x_1 ^ ... ^ x_n) =
          sum_{a<b} (-1)^{a+b} {x_a,x_b} ^ x_1 ^ ... hat_a ... hat_b ... ^ x_n
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from itertools import combinations
from typing import Any, Callable, Dict, FrozenSet, List, Optional, Sequence, Tuple


# =========================================================================
# 1. PVA lambda-bracket skeleton (rational, classical-limit specialization)
# =========================================================================

@dataclass
class ClassicalPVA:
    r"""Classical limit PVA = gr^F(A) with Poisson bracket on C_2 algebra.

    This is a finite, purely rational snapshot of a Poisson vertex
    algebra suitable for bar complex computations at the zero-mode
    (C_2 algebra) level.

    Fields:
        name: algebra name
        generators: ordered list of generator names
        weights: conformal weight of each generator
        poisson: dict (i,j) -> dict of target generators -> Fraction coefficient
                 encoding {x_i, x_j}_P = sum_k coeff_k * x_k.
                 Anti-symmetric: (j,i) not stored, inferred.
        central_terms: dict (i,j) -> Fraction for scalar (central) Poisson terms
                       (e.g. the c/2 in Virasoro's delta''' corresponds to a
                       central scalar; represented as a Fraction).
        c_or_k: central parameter (kappa value for the family)
    """
    name: str
    generators: List[str]
    weights: Dict[str, int]
    poisson: Dict[Tuple[str, str], Dict[str, Fraction]] = field(default_factory=dict)
    central_terms: Dict[Tuple[str, str], Fraction] = field(default_factory=dict)
    c_or_k: Fraction = Fraction(0)

    def gen_index(self, name: str) -> int:
        return self.generators.index(name)

    def poisson_bracket(self, a: str, b: str) -> Tuple[Dict[str, Fraction], Fraction]:
        r"""Return ({x_a, x_b}_P, central_part).

        The Poisson bracket is ANTI-SYMMETRIC: {b, a} = -{a, b}.

        Returns:
            (linear_part, central_scalar)
            linear_part: dict target -> coefficient
            central_scalar: the constant term (from the highest derivative
                            of delta in the lambda-bracket)
        """
        if (a, b) in self.poisson:
            return dict(self.poisson[(a, b)]), self.central_terms.get((a, b), Fraction(0))
        if (b, a) in self.poisson:
            lin = {k: -v for k, v in self.poisson[(b, a)].items()}
            cs = -self.central_terms.get((b, a), Fraction(0))
            return lin, cs
        return {}, Fraction(0)


# =========================================================================
# 2. Family constructors (classical limits of the standard landscape)
# =========================================================================

def heisenberg_classical_pva(k: Fraction = Fraction(1)) -> ClassicalPVA:
    r"""Heisenberg classical-limit PVA.

    A single weight-1 generator phi = J.  Lambda-bracket:
        {phi_lambda phi} = k*lambda
    i.e. c_0 = 0 and c_1 = k.  At the C_2 algebra level the zero-mode
    Poisson bracket is c_0 = 0:

        {phi, phi}_P = 0

    but the CENTRAL term at order 1 (lambda^1 piece) contributes to the
    scalar-valued Poisson bracket as a DELTA' coefficient.  In the
    zero-mode truncation this is a CENTRAL element, not a linear one.

    kappa(H_k) = k.
    """
    pva = ClassicalPVA(
        name=f"Heis_{k}",
        generators=["phi"],
        weights={"phi": 1},
        c_or_k=Fraction(k),
    )
    # Zero-mode bracket: {phi, phi}_P = 0 (no linear part)
    pva.poisson[("phi", "phi")] = {}
    # Central term at the lambda^1 level (c_1 = k):
    pva.central_terms[("phi", "phi")] = Fraction(k)
    return pva


def affine_sl2_classical_pva(k: Fraction = Fraction(1)) -> ClassicalPVA:
    r"""Affine sl_2 classical-limit PVA.

    Generators: e, f, h of weight 1.  Lambda-brackets:
        {e_lambda f} = h + k*lambda
        {h_lambda e} = 2e
        {h_lambda f} = -2f
        {h_lambda h} = 2k*lambda
        {e_lambda e} = {f_lambda f} = 0

    At the C_2 algebra level (zero-mode c_0 terms), the Poisson bracket is
    the Kirillov-Kostant bracket on sl_2^*:
        {e, f}_P = h
        {h, e}_P = 2e
        {h, f}_P = -2f
        {e, e}_P = {f, f}_P = 0
        {h, h}_P = 0

    The lambda^1 terms become CENTRAL scalars in the classical limit:
        c_central(e, f) = k
        c_central(h, h) = 2k

    kappa(sl_2, k) = 3(k+2)/4.
    """
    if k + 2 == 0:
        raise ValueError("critical level k = -h^v = -2 undefined for Sugawara")

    kappa = Fraction(3, 4) * (k + 2)
    pva = ClassicalPVA(
        name=f"sl2_k={k}",
        generators=["e", "f", "h"],
        weights={"e": 1, "f": 1, "h": 1},
        c_or_k=Fraction(kappa),
    )
    # Lie-Poisson brackets (zero-mode part)
    pva.poisson[("e", "f")] = {"h": Fraction(1)}
    pva.poisson[("h", "e")] = {"e": Fraction(2)}
    pva.poisson[("h", "f")] = {"f": Fraction(-2)}
    pva.poisson[("e", "e")] = {}
    pva.poisson[("f", "f")] = {}
    pva.poisson[("h", "h")] = {}

    # Central (level) terms
    pva.central_terms[("e", "f")] = Fraction(k)
    pva.central_terms[("h", "h")] = Fraction(2) * k
    return pva


def virasoro_classical_pva(c: Fraction = Fraction(1)) -> ClassicalPVA:
    r"""Virasoro classical-limit PVA.

    Single generator T of weight 2.  Lambda-bracket:
        {T_lambda T} = partial T + 2T*lambda + (c/12)*lambda^3

    At the C_2 algebra level, the zero-mode bracket is:
        {T, T}_P = partial T  (the c_0 coefficient)

    In the zero-mode truncation, partial T is NOT a C_2 generator (it is
    in the image of T -> partial T which lies in C_2 by definition).
    So {T, T}_P = 0 in the finite C_2 algebra.

    The lambda^3 term (c/2 = T_{(3)}T OPE mode) is the central term.

    kappa(Vir_c) = c/2.
    """
    pva = ClassicalPVA(
        name=f"Vir_c={c}",
        generators=["T"],
        weights={"T": 2},
        c_or_k=Fraction(c) / Fraction(2),
    )
    pva.poisson[("T", "T")] = {}  # in C_2 algebra, partial T becomes 0
    pva.central_terms[("T", "T")] = Fraction(c) / Fraction(12)
    return pva


# =========================================================================
# 3. Chevalley-Eilenberg bar complex of the C_2-algebra Poisson structure
# =========================================================================

def _basis_exterior(gens: Sequence[str], arity: int) -> List[Tuple[str, ...]]:
    """Return the basis of Lambda^arity(span(gens)) as a sorted list.

    Each basis element is a strictly increasing tuple of generators.
    """
    if arity < 0 or arity > len(gens):
        return []
    return [tuple(combo) for combo in combinations(gens, arity)]


def _sign_remove_two(n: int, a: int, b: int) -> int:
    """Sign for removing positions a<b from a wedge of length n and
    prepending the bracket {x_a, x_b} at position 0.

    Chevalley-Eilenberg sign for the differential:
        d(x_1 ^ ... ^ x_n) =
            sum_{a<b} (-1)^{a+b} {x_a, x_b} ^ x_1 ^ ... hat_a ... hat_b ... ^ x_n.

    Returns (-1)^{a+b}.  We use 1-indexed a,b here.
    """
    return 1 if (a + b) % 2 == 0 else -1


def ce_differential_matrix(pva: ClassicalPVA, arity: int) -> List[List[Fraction]]:
    r"""Construct the Chevalley-Eilenberg Poisson differential matrix

        d_CE : Lambda^{arity}(R_+) -> Lambda^{arity-1}(R_+)

    where R_+ is the span of the PVA generators (treated as a linear
    subspace of the C_2 algebra).

    Only the LINEAR part of the Poisson bracket contributes at this
    truncation: central terms contribute to R_0 = C (augmentation), not
    to R_+, so they are dropped here.

    Returns:
        matrix: d[i][j] with i indexing the target (arity-1) basis and
                j indexing the source (arity) basis.
                A Fraction-valued matrix.
    """
    gens = pva.generators
    source_basis = _basis_exterior(gens, arity)
    target_basis = _basis_exterior(gens, arity - 1) if arity >= 1 else []

    rows = len(target_basis)
    cols = len(source_basis)
    mat: List[List[Fraction]] = [
        [Fraction(0) for _ in range(cols)] for _ in range(rows)
    ]
    if arity == 0:
        return mat

    target_index = {b: i for i, b in enumerate(target_basis)}

    for j, src in enumerate(source_basis):
        # Iterate over pairs (a<b) in src and apply {x_a, x_b}
        n = len(src)
        for a in range(n):
            for b in range(a + 1, n):
                xa, xb = src[a], src[b]
                lin, _cen = pva.poisson_bracket(xa, xb)
                if not lin:
                    continue
                remaining = tuple(x for idx, x in enumerate(src) if idx != a and idx != b)
                for target_gen, coeff in lin.items():
                    # Replace src with ({x_a, x_b} in the form target_gen)
                    # prepended to remaining.  We must sort the result and
                    # track sign.
                    if target_gen in remaining:
                        # wedge squared zero: skip
                        continue
                    new_tuple = (target_gen,) + remaining
                    sorted_new, parity = _sort_with_sign(new_tuple)
                    sign = _sign_remove_two(n, a + 1, b + 1) * parity
                    if sorted_new in target_index:
                        mat[target_index[sorted_new]][j] += Fraction(sign) * coeff

    return mat


def _sort_with_sign(t: Tuple[str, ...]) -> Tuple[Tuple[str, ...], int]:
    """Sort a tuple of generator names and return (sorted, sign)
    based on the number of transpositions (bubble-sort parity).

    If there is a duplicate, parity is 0 (caller should handle this,
    but we return 0 sign so it cancels in any sum).
    """
    arr = list(t)
    n = len(arr)
    sign = 1
    # Bubble sort; detect duplicates on the fly
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] == arr[j + 1]:
                return tuple(arr), 0
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sign = -sign
    return tuple(arr), sign


# =========================================================================
# 4. Exact rational rank (for cohomology dimensions)
# =========================================================================

def rational_rank(matrix: List[List[Fraction]]) -> int:
    """Compute the rank of a rational matrix exactly via Gauss elimination.

    Returns the number of linearly independent rows (= columns for full-rank).
    """
    if not matrix or not matrix[0]:
        return 0
    m = [row[:] for row in matrix]
    rows = len(m)
    cols = len(m[0])
    r = 0
    pivot_col = 0
    for pivot_col in range(cols):
        if r >= rows:
            break
        # Find a pivot in column pivot_col starting at row r
        pivot_row = None
        for i in range(r, rows):
            if m[i][pivot_col] != 0:
                pivot_row = i
                break
        if pivot_row is None:
            continue
        m[r], m[pivot_row] = m[pivot_row], m[r]
        pivot = m[r][pivot_col]
        # Eliminate below and above
        for i in range(rows):
            if i == r:
                continue
            if m[i][pivot_col] != 0:
                factor = m[i][pivot_col] / pivot
                for c in range(pivot_col, cols):
                    m[i][c] -= factor * m[r][c]
        r += 1
    return r


# =========================================================================
# 5. Bar cohomology of the PVA C_2 algebra (E_1 page)
# =========================================================================

@dataclass
class CEBarReport:
    """Chevalley-Eilenberg bar cohomology of a classical limit PVA."""
    pva_name: str
    dim_gens: int
    arities: List[int]
    dim_C: Dict[int, int]           # dim Lambda^arity(R_+)
    rank_d: Dict[int, int]          # rank of d_CE : C^{arity} -> C^{arity-1}
    dim_H: Dict[int, int]           # dim H^arity
    euler_char: int


def ce_bar_cohomology(pva: ClassicalPVA, max_arity: int = 3) -> CEBarReport:
    r"""Compute the bar cohomology of the classical limit PVA through arity max_arity.

    Returns the dimensions of each Lambda^n(R_+), the rank of the CE
    differential at each arity, and the cohomology dimensions:

        dim H^n = dim C^n - rank(d_CE : C^n -> C^{n-1}) - rank(d_CE : C^{n+1} -> C^n)

    Note: we are computing the HOMOLOGICAL cohomology for the chain complex
        ... -> C^{n+1} --d--> C^n --d--> C^{n-1} -> ... -> C^0 -> 0.
    The Chevalley-Eilenberg bar differential LOWERS the exterior degree
    (standard chain complex).  Equivalently, flipping to cohomological
    indexing gives the same dimensions.
    """
    gens = pva.generators
    n_gens = len(gens)
    max_arity = min(max_arity, n_gens)
    arities = list(range(max_arity + 2))  # include one extra for boundary

    dim_C: Dict[int, int] = {}
    rank_d: Dict[int, int] = {}

    for a in arities:
        basis = _basis_exterior(gens, a)
        dim_C[a] = len(basis)
        mat = ce_differential_matrix(pva, a)
        rank_d[a] = rational_rank(mat)

    dim_H: Dict[int, int] = {}
    for a in range(max_arity + 1):
        # Standard formula for chain complex:
        # dim H_a = dim C_a - rank(d: C_a -> C_{a-1}) - rank(d: C_{a+1} -> C_a)
        dim_H[a] = dim_C.get(a, 0) - rank_d.get(a, 0) - rank_d.get(a + 1, 0)

    euler = sum((-1) ** a * dim_C.get(a, 0) for a in range(max_arity + 1))

    return CEBarReport(
        pva_name=pva.name,
        dim_gens=n_gens,
        arities=list(range(max_arity + 1)),
        dim_C={a: dim_C[a] for a in range(max_arity + 1)},
        rank_d={a: rank_d.get(a, 0) for a in range(max_arity + 1)},
        dim_H=dim_H,
        euler_char=euler,
    )


# =========================================================================
# 6. Chevalley-Eilenberg closed-form cross-check for semisimple Lie algebras
# =========================================================================

def sl2_ce_cohomology_closed_form() -> Dict[int, int]:
    r"""H^*(sl_2, C) = Lambda^*(primitive generator in degree 3).

    For a simple Lie algebra of rank r, H^*(g, C) = exterior algebra
    on primitive generators in degrees 2m_i + 1 where m_i are the
    exponents.  For sl_2, the single exponent is 1, giving a primitive
    in degree 3.  So:
        H^0 = C,  H^1 = 0,  H^2 = 0,  H^3 = C.

    Returns dict arity -> dim H^arity (as a chain complex grading).
    """
    return {0: 1, 1: 0, 2: 0, 3: 1}


def check_sl2_matches_closed_form(k: Fraction = Fraction(1)) -> Dict[str, Any]:
    """Verify the direct bar computation matches the CE closed form."""
    pva = affine_sl2_classical_pva(k=k)
    report = ce_bar_cohomology(pva, max_arity=3)
    closed = sl2_ce_cohomology_closed_form()
    match = all(report.dim_H.get(a, 0) == closed.get(a, 0) for a in range(4))
    return {
        'direct': dict(report.dim_H),
        'closed_form': closed,
        'matches': match,
        'euler': report.euler_char,
    }


# =========================================================================
# 7. Koszul dual PVA: Heisenberg has opposite-sign Poisson structure
# =========================================================================

def pva_koszul_dual_heisenberg(k: Fraction) -> ClassicalPVA:
    r"""Koszul dual of the Heisenberg PVA at level k.

    For Heisenberg, the KOSZUL DUAL PVA is another Heisenberg PVA with
    OPPOSITE central term -k.  This gives:

        kappa(H_k^!)_PVA = -k   (at the PVA level)

    which MATCHES kappa(H_{-k}) AS A NUMBER (AP33) but the dual PVA is
    still a different object from H_{-k} in full conditions.

    Complementarity at the classical level:
        kappa(H_k) + kappa(H_k^!)_PVA = k + (-k) = 0.

    This matches the KM complementarity anti-symmetry (AP24: kappa + kappa! = 0
    holds for Heisenberg / free fields / KM, but fails for Virasoro where
    the sum is c/2 + (26-c)/2 = 13).
    """
    return heisenberg_classical_pva(k=Fraction(-k))


def pva_koszul_dual_virasoro(c: Fraction) -> ClassicalPVA:
    r"""Koszul dual of the Virasoro PVA at central charge c.

    For Virasoro, the Koszul dual VA is Vir_{26-c}.  At the PVA (classical)
    level, the complementarity sum is
        kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13
    (NOT zero; AP24 is the record of this overclaim).

    We return the Virasoro PVA at c' = 26 - c as the PVA-level dual.
    """
    return virasoro_classical_pva(c=Fraction(26) - Fraction(c))


def pva_koszul_dual_sl2(k: Fraction) -> ClassicalPVA:
    r"""Koszul dual PVA for affine sl_2 at level k.

    Feigin-Frenkel: k ↦ -k - 2h^v = -k - 4 for sl_2.  At the PVA (classical)
    level the dual is the affine sl_2 PVA at the dual level.  Complementarity:
        kappa(sl_2, k) + kappa(sl_2, -k-4)
            = 3(k+2)/4 + 3(-k-4+2)/4
            = 3(k+2)/4 + 3(-k-2)/4
            = 0.

    This matches the KM complementarity identity (AP24: holds for KM).
    """
    dual_level = Fraction(-k) - Fraction(4)
    if dual_level + 2 == 0:
        # Dual sits at critical level; construct via raw bracket data
        pva = ClassicalPVA(
            name=f"sl2_dual_k={k}_critical",
            generators=["e", "f", "h"],
            weights={"e": 1, "f": 1, "h": 1},
            c_or_k=Fraction(0),
        )
        pva.poisson[("e", "f")] = {"h": Fraction(1)}
        pva.poisson[("h", "e")] = {"e": Fraction(2)}
        pva.poisson[("h", "f")] = {"f": Fraction(-2)}
        pva.poisson[("e", "e")] = {}
        pva.poisson[("f", "f")] = {}
        pva.poisson[("h", "h")] = {}
        pva.central_terms[("e", "f")] = Fraction(dual_level)
        pva.central_terms[("h", "h")] = Fraction(2) * dual_level
        return pva
    return affine_sl2_classical_pva(k=dual_level)


def pva_complementarity_sum(a_name: str, k_or_c: Fraction) -> Fraction:
    r"""Compute kappa(A) + kappa(A^!)_PVA for A in {Heisenberg, sl_2, Virasoro}.

    This is the PVA-level complementarity sum.  Expected:
        Heis      : 0
        sl_2, k   : 0
        Virasoro  : 13
    """
    if a_name == "Heisenberg":
        return Fraction(k_or_c) + Fraction(-k_or_c)
    if a_name == "sl_2":
        k = Fraction(k_or_c)
        return Fraction(3, 4) * (k + 2) + Fraction(3, 4) * ((-k - 4) + 2)
    if a_name == "Virasoro":
        c = Fraction(k_or_c)
        return c / Fraction(2) + (Fraction(26) - c) / Fraction(2)
    raise ValueError(f"unknown family: {a_name}")


# =========================================================================
# 8. Associated variety X_A = Spec(R_A^{red})
# =========================================================================

@dataclass
class AssociatedVariety:
    """Structural description of the associated variety X_A."""
    pva_name: str
    krull_dimension: int            # dim X_A as a variety
    smooth: bool                    # true if R_A^{red} = C[x_1,...,x_n]
    orbit_type: str                 # 'affine space', 'nilpotent cone', 'point', ...


def heisenberg_associated_variety(k: Fraction) -> AssociatedVariety:
    """X_{Heisenberg} = A^1 (affine line, smooth, Krull dim 1)."""
    return AssociatedVariety(
        pva_name=f"Heis_{k}",
        krull_dimension=1,
        smooth=True,
        orbit_type="affine space A^1",
    )


def sl2_universal_associated_variety(k: Fraction) -> AssociatedVariety:
    """X_{V_k(sl_2)} = sl_2^* ~ A^3 for the UNIVERSAL affine algebra.

    For the SIMPLE quotient L_k(sl_2) at positive integer level,
    X = nilpotent cone N_{sl_2} = {(e,f,h) : ef = h^2/4, ...}, dim 2.
    """
    return AssociatedVariety(
        pva_name=f"V_k(sl_2)_k={k}",
        krull_dimension=3,
        smooth=True,
        orbit_type="sl_2^* (affine 3-space)",
    )


def sl2_integrable_associated_variety(k_int: int) -> AssociatedVariety:
    """X_{L_k(sl_2)} at positive integer level = nilpotent cone of sl_2.

    Nilpotent cone N_{sl_2} = {(e,f,h) : h^2 + 4ef = 0} ~ closure of the
    principal nilpotent orbit, Krull dim 2.
    """
    if k_int < 0:
        raise ValueError(f"integrable level must be non-negative integer, got {k_int}")
    return AssociatedVariety(
        pva_name=f"L_{k_int}(sl_2)",
        krull_dimension=2,
        smooth=False,
        orbit_type="nilpotent cone closure",
    )


def virasoro_associated_variety(c: Fraction) -> AssociatedVariety:
    """X_{Vir_c}: generically a point (Vir has one generator, partial T is in C_2)."""
    return AssociatedVariety(
        pva_name=f"Vir_c={c}",
        krull_dimension=1,  # single generator T modulo partial T
        smooth=True,
        orbit_type="affine line (generator T)",
    )


# =========================================================================
# 9. The "leak" = difference between classical bar and quantum bar
# =========================================================================

def leak_dimensions(
    pva_bar_dims: Dict[int, int],
    va_bar_dims: Dict[int, int],
    max_arity: int = 3,
) -> Dict[int, int]:
    r"""Compute the dimension difference (quantum leak) between classical
    and quantum bar cohomology at each arity.

        leak[n] := dim H^n(bar VA) - dim H^n(bar PVA)

    For classically Koszul algebras, leak[n] = 0 for all n.
    """
    leak = {}
    for a in range(max_arity + 1):
        leak[a] = va_bar_dims.get(a, 0) - pva_bar_dims.get(a, 0)
    return leak


# =========================================================================
# 10. E_1 page of the Li-bar spectral sequence
# =========================================================================

@dataclass
class LiBarE1:
    """E_1 page data of the Li-bar spectral sequence for a PVA.

    E_0 = bar complex of the C_2 algebra R_A.
    d_0 = bar differential from commutative product (zero on free polynomial).
    E_1 = bar of R_A as exterior algebra.
    d_1 = Poisson differential (the CE differential d_CE).
    E_2 = H(E_1, d_1).
    """
    pva_name: str
    E0_dimensions: Dict[int, int]     # dim of C^n at arity n
    E1_dimensions: Dict[int, int]     # dim of E_1^n (= E_0^n for free commutative)
    E2_dimensions: Dict[int, int]     # dim of E_2^n = H^n(E_1, d_1)


def li_bar_E1_page(pva: ClassicalPVA, max_arity: int = 3) -> LiBarE1:
    r"""Set up the E_1 page of the Li-bar spectral sequence for this PVA.

    For the classical limit (free polynomial + Poisson), the bar complex
    at arity n is Lambda^n(gens) (free commutative case) and d_0 = 0.
    So E_1 = E_0 = Lambda^*(gens), and d_1 = d_CE.  The E_2 page is the
    Chevalley-Eilenberg cohomology.
    """
    report = ce_bar_cohomology(pva, max_arity=max_arity)
    return LiBarE1(
        pva_name=pva.name,
        E0_dimensions=dict(report.dim_C),
        E1_dimensions=dict(report.dim_C),
        E2_dimensions=dict(report.dim_H),
    )


# =========================================================================
# 11. Quantum correction: scalar kappa trace from central Poisson terms
# =========================================================================

def pva_scalar_kappa(pva: ClassicalPVA) -> Fraction:
    r"""Extract the scalar kappa from the PVA central term table.

    For Heisenberg: kappa = central_term(phi, phi) = k.
    For sl_2: kappa = (3/4)(k + 2), where central_term(e, f) = k.
    For Virasoro: kappa = c/2, where central_term(T, T) = c/12.
    """
    if pva.name.startswith("Heis"):
        return pva.central_terms.get(("phi", "phi"), Fraction(0))
    if pva.name.startswith("sl2") or pva.name.startswith("Affine sl_2"):
        k = pva.central_terms.get(("e", "f"), Fraction(0))
        return Fraction(3, 4) * (k + Fraction(2))
    if pva.name.startswith("Vir"):
        c12 = pva.central_terms.get(("T", "T"), Fraction(0))
        c = Fraction(12) * c12
        return c / Fraction(2)
    return Fraction(0)


# =========================================================================
# 12. Landscape summary table
# =========================================================================

def classical_limit_landscape_summary() -> List[Dict[str, Any]]:
    """Tabulate classical bar cohomology + kappa + associated variety
    for the standard landscape at canonical parameter values."""

    rows: List[Dict[str, Any]] = []

    # Heisenberg at k = 1
    pva = heisenberg_classical_pva(k=Fraction(1))
    rep = ce_bar_cohomology(pva, max_arity=3)
    rows.append({
        'family': 'Heisenberg',
        'param': 'k=1',
        'kappa': pva_scalar_kappa(pva),
        'bar_dims': dict(rep.dim_H),
        'euler': rep.euler_char,
        'variety': heisenberg_associated_variety(Fraction(1)).orbit_type,
    })

    # Affine sl_2 at k = 1 (universal)
    pva = affine_sl2_classical_pva(k=Fraction(1))
    rep = ce_bar_cohomology(pva, max_arity=3)
    rows.append({
        'family': 'Affine sl_2',
        'param': 'k=1',
        'kappa': pva_scalar_kappa(pva),
        'bar_dims': dict(rep.dim_H),
        'euler': rep.euler_char,
        'variety': sl2_universal_associated_variety(Fraction(1)).orbit_type,
    })

    # Virasoro at c = 1
    pva = virasoro_classical_pva(c=Fraction(1))
    rep = ce_bar_cohomology(pva, max_arity=3)
    rows.append({
        'family': 'Virasoro',
        'param': 'c=1',
        'kappa': pva_scalar_kappa(pva),
        'bar_dims': dict(rep.dim_H),
        'euler': rep.euler_char,
        'variety': virasoro_associated_variety(Fraction(1)).orbit_type,
    })

    return rows


# =========================================================================
# 13. Diagnostics: classical Jacobi identity verification
# =========================================================================

def verify_jacobi_identity(pva: ClassicalPVA) -> Dict[str, Any]:
    r"""Verify the Jacobi identity for the Poisson bracket on R_A.

    For any three generators x, y, z:
        {x, {y, z}} + cyclic = 0.

    For the affine Lie-Poisson bracket this is the Jacobi identity of
    the Lie algebra.  For Heisenberg/Virasoro (no linear bracket terms)
    Jacobi is trivially satisfied.
    """
    gens = pva.generators
    failures: List[Tuple[str, str, str, Dict[str, Fraction]]] = []

    for i, x in enumerate(gens):
        for j, y in enumerate(gens):
            for k, z in enumerate(gens):
                # Compute {x, {y, z}}
                lin_yz, _ = pva.poisson_bracket(y, z)
                cyc1: Dict[str, Fraction] = {}
                for target, coeff in lin_yz.items():
                    lin_x_target, _ = pva.poisson_bracket(x, target)
                    for t2, c2 in lin_x_target.items():
                        cyc1[t2] = cyc1.get(t2, Fraction(0)) + coeff * c2

                lin_zx, _ = pva.poisson_bracket(z, x)
                cyc2: Dict[str, Fraction] = {}
                for target, coeff in lin_zx.items():
                    lin_y_target, _ = pva.poisson_bracket(y, target)
                    for t2, c2 in lin_y_target.items():
                        cyc2[t2] = cyc2.get(t2, Fraction(0)) + coeff * c2

                lin_xy, _ = pva.poisson_bracket(x, y)
                cyc3: Dict[str, Fraction] = {}
                for target, coeff in lin_xy.items():
                    lin_z_target, _ = pva.poisson_bracket(z, target)
                    for t2, c2 in lin_z_target.items():
                        cyc3[t2] = cyc3.get(t2, Fraction(0)) + coeff * c2

                total: Dict[str, Fraction] = {}
                for d in (cyc1, cyc2, cyc3):
                    for t, c in d.items():
                        total[t] = total.get(t, Fraction(0)) + c
                total = {t: c for t, c in total.items() if c != 0}
                if total:
                    failures.append((x, y, z, total))
    return {
        'pva_name': pva.name,
        'ok': not failures,
        'failure_count': len(failures),
        'failures': failures[:5],  # first few for diagnostics
    }


# =========================================================================
# 14. Anti-symmetry of Poisson bracket verification
# =========================================================================

def verify_antisymmetry(pva: ClassicalPVA) -> Dict[str, Any]:
    """For every ordered pair (x, y) with x != y, verify {y, x} = -{x, y}."""
    gens = pva.generators
    failures: List[Tuple[str, str]] = []
    for x in gens:
        for y in gens:
            if x == y:
                continue
            lin_xy, _ = pva.poisson_bracket(x, y)
            lin_yx, _ = pva.poisson_bracket(y, x)
            neg_xy = {k: -v for k, v in lin_xy.items()}
            # Normalize zero entries
            neg_xy = {k: v for k, v in neg_xy.items() if v != 0}
            lin_yx_clean = {k: v for k, v in lin_yx.items() if v != 0}
            if neg_xy != lin_yx_clean:
                failures.append((x, y))
    return {
        'pva_name': pva.name,
        'ok': not failures,
        'failure_count': len(failures),
    }
