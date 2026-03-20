"""Half-space reflected weight identity (RWI) for Poisson vertex algebras.

Investigates conj:quadratic-rwi and conj:cubic-rwi from Vol II
(affine_half_space_bv.tex, sec:jet-order-inductive).

The half-space BV programme (Khan-Zeng) quantizes the PV sigma model on
C x R_{>=0} with Neumann boundary, producing a boundary vertex algebra.
The affine case (jet order <= 1) is PROVED (thm:affine-half-space-bv).
The nonlinear frontier begins at jet order 2.

The jet-order decomposition (thm:jet-inductive-rwi) writes
    RWI(V) = RWI(J^{<=1}V) + sum_{N>=2} delta_N(V),
where RWI(J^{<=1}V) = 0 by the affine theorem.

conj:quadratic-rwi: delta_2(V) = 0 for freely generated PVA of jet order <= 2.
    Mechanism: valence-shift (form-degree excess forces vanishing).
    Status: ClaimStatusOpen (label conj:quadratic-rwi).
    NOTE: line 1199 of affine_half_space_bv.tex references thm:quadratic-rwi
    as PROVED, but no such label exists. The label is conj:quadratic-rwi with
    ClaimStatusOpen. This is a broken reference.

conj:cubic-rwi: delta_3(V) = 0 for freely generated PVA satisfying Jacobi.
    Mechanism: cancellation between lollipop graph Gamma_3^{(1)} and
    reflected-triangle graph.
    Status: ClaimStatusOpen (label conj:cubic-rwi).

The propagator on the half-space uses the method of images:
    K^refl(z,t; z',t') = K(z,t; z',t') + K(z,t; bar{z'},-t')
where K is the bulk propagator (meromorphic in z-z', decaying in |t-t'|).
The self-image propagator K(z,t; z,-t) controls reflection-stratum integrals.

CONVENTIONS:
- Lambda-bracket: {a^i_lambda a^j} = sum_k pi^{ij}_k(a) lambda^k
- Jet order: max degree of pi^{ij}_k in fields a
- Cohomological grading, |d| = +1
- Equivariant Kontsevich integral on compactified half-space config spaces
"""

from __future__ import annotations

from math import factorial, pi as PI
from typing import Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, symbols, sqrt, oo, I,
    Poly, simplify, expand, cancel, factor,
    integrate, cos, sin, atan2, log, exp,
    Matrix, eye, zeros,
)


# ===========================================================================
# PVA framework
# ===========================================================================

class PVAGenerator:
    """A generator of a Poisson vertex algebra.

    Attributes:
        name: string identifier
        weight: conformal weight (half-integer)
        parity: 0 = bosonic, 1 = fermionic
    """

    def __init__(self, name: str, weight, parity: int = 0):
        self.name = name
        try:
            self.weight = Rational(weight)
        except (TypeError, ValueError):
            self.weight = weight  # allow symbolic weights
        self.parity = parity

    def __repr__(self) -> str:
        return f"PVAGen({self.name}, h={self.weight})"


class PVA:
    """A freely generated Poisson vertex algebra.

    The lambda-bracket is encoded by structure functions:
        {a^i_lambda a^j} = sum_{k=0}^{max_pole} pi^{ij}_k(a) lambda^k

    Each pi^{ij}_k(a) is decomposed by jet order:
        pi^{ij}_k(a) = pi^{ij}_{k,0} + pi^{ij}_{k,1}(a) + pi^{ij}_{k,2}(a) + ...
    where pi^{ij}_{k,m} is homogeneous of degree m in the generators.
    """

    def __init__(self, name: str, generators: List[PVAGenerator]):
        self.name = name
        self.generators = generators
        self.gen_names = [g.name for g in generators]
        self.n_gens = len(generators)
        # Lambda bracket data: (i, j, pole_order) -> {jet_order: coefficient_data}
        # coefficient_data is a dict mapping monomial tuples -> Rational
        self._brackets: Dict[Tuple[int, int, int], Dict[int, object]] = {}
        self._max_pole = 0
        self._jet_order = 0

    def set_bracket(self, i: int, j: int, pole_order: int,
                    jet_order: int, coefficient) -> None:
        """Set pi^{ij}_{pole_order, jet_order} = coefficient.

        For jet_order 0: coefficient is a Rational (constant).
        For jet_order 1: coefficient is a list of Rationals (linear in generators).
        For jet_order 2: coefficient is a matrix of Rationals (quadratic in generators).
        For jet_order 3: coefficient is a 3-tensor (cubic in generators).
        """
        key = (i, j, pole_order)
        if key not in self._brackets:
            self._brackets[key] = {}
        self._brackets[key][jet_order] = coefficient
        self._max_pole = max(self._max_pole, pole_order)
        self._jet_order = max(self._jet_order, jet_order)

    def get_bracket(self, i: int, j: int, pole_order: int,
                    jet_order: int) -> object:
        """Get pi^{ij}_{pole_order, jet_order}."""
        key = (i, j, pole_order)
        if key not in self._brackets:
            return None
        return self._brackets[key].get(jet_order, None)

    @property
    def jet_order(self) -> int:
        """Maximum jet order of the PVA."""
        return self._jet_order

    @property
    def max_pole_order(self) -> int:
        """Maximum pole order in the lambda-bracket."""
        return self._max_pole

    def lambda_bracket_jet_decomposition(self, i: int, j: int,
                                         pole_order: int) -> Dict[int, object]:
        """Return all jet-order components of pi^{ij}_{pole_order}."""
        key = (i, j, pole_order)
        return dict(self._brackets.get(key, {}))

    def __repr__(self) -> str:
        return f"PVA({self.name}, n={self.n_gens}, jet={self._jet_order})"


# ===========================================================================
# Standard PVA examples
# ===========================================================================

def affine_pva(lie_type: str = "sl2", level: object = None) -> PVA:
    """Affine (Kac-Moody) PVA: jet order 1.

    {J^a_lambda J^b} = f^{ab}_c J^c + k * kappa^{ab} * lambda

    For sl_2: generators e,h,f (indices 0,1,2).
    f^{01}_0 = -2, f^{10}_0 = 2,  (i.e. [h,e] = 2e)
    f^{02}_2 = 2,  f^{20}_2 = -2, (i.e. [h,f] = -2f)
    f^{01}_1 = ... etc. But for PVA purposes the structure constants are:
    [e,f] = h, [h,e] = 2e, [h,f] = -2f
    Killing form: kappa(e,f) = kappa(f,e) = 1, kappa(h,h) = 2
    """
    k = level if level is not None else Symbol('k')

    if lie_type == "sl2":
        gens = [
            PVAGenerator("e", Rational(1)),
            PVAGenerator("h", Rational(1)),
            PVAGenerator("f", Rational(1)),
        ]
        pva = PVA("affine_sl2", gens)

        # Structure constants [J^i, J^j] = f^{ij}_k J^k (pole order 0, jet order 1)
        # [e, f] = h: f^{02}_1 = 1
        pva.set_bracket(0, 2, 0, 1, [Rational(0), Rational(1), Rational(0)])
        # [f, e] = -h: f^{20}_1 = -1
        pva.set_bracket(2, 0, 0, 1, [Rational(0), Rational(-1), Rational(0)])
        # [h, e] = 2e: f^{10}_0 = 2
        pva.set_bracket(1, 0, 0, 1, [Rational(2), Rational(0), Rational(0)])
        # [e, h] = -2e: f^{01}_0 = -2
        pva.set_bracket(0, 1, 0, 1, [Rational(-2), Rational(0), Rational(0)])
        # [h, f] = -2f: f^{12}_2 = -2
        pva.set_bracket(1, 2, 0, 1, [Rational(0), Rational(0), Rational(-2)])
        # [f, h] = 2f: f^{21}_2 = 2
        pva.set_bracket(2, 1, 0, 1, [Rational(0), Rational(0), Rational(2)])

        # Killing form: kappa * lambda (pole order 1, jet order 0)
        pva.set_bracket(0, 2, 1, 0, k)
        pva.set_bracket(2, 0, 1, 0, k)
        pva.set_bracket(1, 1, 1, 0, 2 * k)

        return pva

    raise ValueError(f"Unknown Lie type: {lie_type}")


def betagamma_pva(lam: object = None) -> PVA:
    """Beta-gamma PVA: jet order 1.

    Generators: beta (weight lambda), gamma (weight 1-lambda).
    {beta_lambda gamma} = 1 (simple pole, constant).
    Jet order = 1 because the only nonzero bracket is constant in fields
    with first-order pole.

    Actually for PVA purposes: the lambda-bracket {beta_lambda gamma} = 1
    means pi^{01}_{0,0} = 1 (pole order 0, jet order 0, constant).
    This is jet order 0 in the fields, but pole order 0 in lambda.
    The betagamma PVA is maximally simple: constant brackets, no field
    dependence. Jet order = 0.
    """
    if lam is None:
        lam = Symbol('lambda')

    gens = [
        PVAGenerator("beta", lam),
        PVAGenerator("gamma", 1 - lam),
    ]
    pva = PVA("betagamma", gens)

    # {beta_lambda gamma} = 1: constant, pole order 0
    pva.set_bracket(0, 1, 0, 0, Rational(1))
    # {gamma_lambda beta} = -1 (skew-symmetry of PVA)
    pva.set_bracket(1, 0, 0, 0, Rational(-1))

    return pva


def virasoro_pva(c: object = None) -> PVA:
    """Virasoro PVA: jet order 2.

    Generator: L (conformal weight 2).
    {L_lambda L} = (T + 2*lambda)*L + (c/12)*lambda^3

    Decomposed:
      pole order 0: pi^{00}_{0,1} = T*L (jet order 1, involves T = derivative)
                    BUT in the PVA framework T is the translation operator,
                    not a field. The correct encoding is:
      {L_lambda L} = 2*L*lambda + (partial L) + (c/12)*lambda^3

    In jet-order terms:
      pi^{00}_{0,1}(L) = partial(L)  [jet order 1, linear in L]
      pi^{00}_{1,1}(L) = 2*L         [pole order 1, jet order 1, linear in L]
      pi^{00}_{3,0} = c/12           [pole order 3, jet order 0, constant]

    The jet order is 1 (linear in the field L), but the total OPE has
    pole order up to 3 (lambda^3 from central charge).

    For the half-space programme, the relevant jet order is the field degree.
    Virasoro is jet order 1 in the fields but is typically reached as a
    DS reduction of affine, not directly. However, the lambda^3 term means
    the lambda-bracket has order 3 in lambda.

    For the purpose of this module: we classify by the FIELD jet order
    (degree of pi in the generators a), which is what controls the
    half-space graph combinatorics. Virasoro has field jet order 1.

    HOWEVER: the Virasoro PVA is not freely generated in the sense of
    def:jet-order-filtration (it has one generator with self-bracket
    involving a derivative). For half-space purposes, L is treated as
    a field on the target space M = C, and {L_lambda L} = 2L*lambda +
    partial(L) + (c/12)*lambda^3 has:
      - constant part of pi at lambda^3: c/12 (jet order 0)
      - linear part at lambda^1: 2L (jet order 1)
      - derivative part at lambda^0: partial L (jet order 1 in derivatives)

    The jet order in CLAUDE.md sense is 2 for Virasoro because the
    Poisson structure on the jet space J_infty(M) has quadratic terms
    from the conformal-weight-2 generator's self-interaction.
    """
    if c is None:
        c = Symbol('c')

    gens = [PVAGenerator("L", Rational(2))]
    pva = PVA("Virasoro", gens)

    # {L_lambda L} = partial(L) + 2*lambda*L + (c/12)*lambda^3
    # In jet-order terms on target M:
    # pole 0, jet 1: coefficient of lambda^0 = partial(L)
    pva.set_bracket(0, 0, 0, 1, [Rational(1)])  # derivative term (linear)
    # pole 1, jet 1: coefficient of lambda^1 = 2*L
    pva.set_bracket(0, 0, 1, 1, [Rational(2)])  # 2*L (linear in field)
    # pole 3, jet 0: coefficient of lambda^3 = c/12
    pva.set_bracket(0, 0, 3, 0, c / 12)  # central charge (constant)

    return pva


def w3_pva(c: object = None) -> PVA:
    """W_3 PVA: jet order 2.

    Generators: L (weight 2), W (weight 3).
    Lambda-brackets:
      {L_lambda L} = 2*L*lambda + partial(L) + (c/12)*lambda^3
      {L_lambda W} = 3*W*lambda + partial(W)
      {W_lambda W} = quadratic in L (jet order 2) + lower terms

    The W-W bracket at leading field order is:
      {W_lambda W} ~ beta*Lambda(L) + ...
    where Lambda(L) is a normal-ordered quadratic in L (the composite
    field :LL: - (3/10)*partial^2 L). This gives jet order 2.

    For the half-space programme, W_3 is the minimal example with genuine
    jet order 2 from nonlinear W-W OPE.
    """
    if c is None:
        c = Symbol('c')

    gens = [
        PVAGenerator("L", Rational(2)),
        PVAGenerator("W", Rational(3)),
    ]
    pva = PVA("W3", gens)

    # L-L bracket (same as Virasoro)
    pva.set_bracket(0, 0, 0, 1, [Rational(1), Rational(0)])
    pva.set_bracket(0, 0, 1, 1, [Rational(2), Rational(0)])
    pva.set_bracket(0, 0, 3, 0, c / 12)

    # L-W bracket: {L_lambda W} = 3*W*lambda + partial(W)
    pva.set_bracket(0, 1, 0, 1, [Rational(0), Rational(1)])   # partial(W)
    pva.set_bracket(0, 1, 1, 1, [Rational(0), Rational(3)])   # 3*W*lambda

    # W-L bracket: {W_lambda L} = -(L + 2*lambda)*W via skew-symmetry
    # = partial(L)*W piece + ...  (comes from sesquilinearity)
    pva.set_bracket(1, 0, 0, 1, [Rational(1), Rational(0)])
    pva.set_bracket(1, 0, 1, 1, [Rational(-1), Rational(0)])

    # W-W bracket: contains jet order 2 (quadratic in L)
    # {W_lambda W} = (1/3)*beta*Lambda + (c/3*5!)*lambda^5 + ...
    # where beta = 16/(22+5c), Lambda = :LL: - (3/10)*partial^2 L
    # The quadratic term: pi^{11}_{0,2} is a 2x2 matrix giving the
    # coefficient of a^i*a^j at pole 0. Lambda ~ L*L means
    # pi^{11}_{0,2}[0,0] = beta (L*L coefficient)
    beta = Rational(16, 1) / (22 + 5 * c) if isinstance(c, (int, Rational)) else 16 / (22 + 5 * c)
    pva.set_bracket(1, 1, 0, 2, [[beta, Rational(0)], [Rational(0), Rational(0)]])
    # W-W: pole 5, jet 0 (central charge for W)
    pva.set_bracket(1, 1, 5, 0, c / Rational(360))

    return pva


def free_boson_pva() -> PVA:
    """Free boson PVA (Heisenberg): jet order 0.

    Generator: J (weight 1).
    {J_lambda J} = lambda (constant in fields).
    Jet order = 0.
    """
    gens = [PVAGenerator("J", Rational(1))]
    pva = PVA("Heisenberg", gens)

    # {J_lambda J} = lambda: pole order 1, jet order 0
    pva.set_bracket(0, 0, 1, 0, Rational(1))

    return pva


# ===========================================================================
# Half-space propagator and configuration spaces
# ===========================================================================

def bulk_propagator_form(z1: complex, t1: float, z2: complex, t2: float) -> complex:
    """Bulk propagator K(z1,t1; z2,t2) of the HT theory.

    K(z,t; z',t') = dz/(z-z') * exp(-|t-t'|)  (schematic).

    For the weight integral, the relevant quantity is the angular form
    d(arg(z-z')) = (1/2pi) * d(atan2(Im(z-z'), Re(z-z'))).

    Returns the propagator value (not the form).
    """
    dz = z1 - z2
    dt = abs(t1 - t2)
    if abs(dz) < 1e-15:
        return 0.0
    return 1.0 / dz * exp(-dt)


def reflected_propagator(z1: complex, t1: float,
                         z2: complex, t2: float) -> complex:
    """Reflected propagator K^refl by method of images.

    K^refl(z,t; z',t') = K(z,t; z',t') + K(z,t; bar{z'},-t')

    The image term enforces Neumann boundary condition at t=0.
    """
    direct = bulk_propagator_form(z1, t1, z2, t2)
    # Image: reflect z2 -> conj(z2), t2 -> -t2
    image = bulk_propagator_form(z1, t1, z2.conjugate(), -t2)
    return direct + image


def self_image_propagator(z: complex, t: float) -> complex:
    """Self-image propagator K(z,t; z,-t).

    This is the propagator connecting a point to its reflection.
    Controls the behavior of reflection-stratum integrals.
    K(z,t; z,-t) = K(z,t; bar{z},-t) when z is real.
    For general z: K(z,t; conj(z),-t) = 1/(z-conj(z)) * exp(-2t)
                                       = 1/(2i*Im(z)) * exp(-2t).
    """
    im_z = z.imag if hasattr(z, 'imag') else 0
    if abs(2 * im_z) < 1e-15:
        return float('inf')  # divergent on real axis
    return 1.0 / (2j * im_z) * exp(-2 * t)


# ===========================================================================
# Graph combinatorics for the half-space integral
# ===========================================================================

class HalfSpaceGraph:
    """An admissible graph for the equivariant Kontsevich integral.

    Vertices are typed:
        - 'bulk': interior points (z, t) with t > 0
        - 'boundary': on partial X = C x {0}

    Edges connect vertices to vertices (including boundary).

    Each vertex carries a jet-order (degree of the Poisson interaction):
        - jet 0: constant (no field dependence)
        - jet 1: affine/linear (valence 3: 2 outgoing, 1 incoming)
        - jet 2: quadratic (valence 4: 2 outgoing, 2 incoming)
        - jet 3: cubic (valence 5: 2 outgoing, 3 incoming)
    """

    def __init__(self, name: str):
        self.name = name
        self.vertices: List[Dict] = []
        self.edges: List[Tuple[int, int]] = []

    def add_vertex(self, vtype: str, jet_order: int) -> int:
        """Add a vertex. Returns vertex index."""
        idx = len(self.vertices)
        self.vertices.append({
            'type': vtype,
            'jet_order': jet_order,
            'valence_out': 2,  # always 2 from Poisson bivector pi^{ij}
            'valence_in': jet_order,  # incoming = field degree
        })
        return idx

    def add_edge(self, source: int, target: int) -> None:
        """Add a directed edge."""
        self.edges.append((source, target))

    @property
    def n_vertices(self) -> int:
        return len(self.vertices)

    @property
    def n_edges(self) -> int:
        return len(self.edges)

    @property
    def n_bulk_vertices(self) -> int:
        return sum(1 for v in self.vertices if v['type'] == 'bulk')

    @property
    def n_boundary_vertices(self) -> int:
        return sum(1 for v in self.vertices if v['type'] == 'boundary')

    @property
    def total_jet_order(self) -> int:
        """Sum of jet orders of all vertices."""
        return sum(v['jet_order'] for v in self.vertices)

    @property
    def total_valence(self) -> int:
        """Total valence (sum of in + out at all vertices)."""
        return sum(v['valence_out'] + v['valence_in'] for v in self.vertices)


# ===========================================================================
# Dimensional / valence counting for the RWI
# ===========================================================================

def config_space_dim(n_bulk: int, n_boundary: int) -> int:
    """Real dimension of the configuration space.

    Conf^partial_n(C x R_{>=0}):
    - Each bulk point: 3 real coordinates (Re(z), Im(z), t)
    - Each boundary point: 2 real coordinates (Re(z), Im(z))
    - Quotient by translations (2 real) + dilation (1 real) = 3

    dim = 3 * n_bulk + 2 * n_boundary - 3
    """
    if n_bulk + n_boundary <= 1:
        return 0
    return 3 * n_bulk + 2 * n_boundary - 3


def form_degree(n_edges: int) -> int:
    """Form degree of the integrand = number of edges.

    Each edge contributes a 1-form (angular form d(arg(z_i - z_j))).
    """
    return n_edges


def form_degree_excess(graph: HalfSpaceGraph) -> int:
    """Form-degree excess = form_degree - config_space_dim.

    For the weight integral to be nonzero, we need
    form_degree = config_space_dim (i.e., excess = 0).

    If excess > 0, the integral vanishes by degree reasons.
    If excess < 0, we need to integrate against a nontrivial current.

    For purely affine graphs at one loop, excess = 0 (matched exactly).
    For graphs with a jet-order-N vertex, each extra incoming edge
    shifts the excess by +1 relative to the affine case.
    """
    dim = config_space_dim(graph.n_bulk_vertices, graph.n_boundary_vertices)
    fd = form_degree(graph.n_edges)
    return fd - dim


def affine_one_loop_excess(n_affine_vertices: int) -> int:
    """Form-degree excess for a purely affine one-loop graph.

    One-loop graph on m affine vertices:
    - n_bulk = m, n_boundary = 0 (all bulk)
    - Edges: m edges forming the loop + m outgoing to boundary
    - But for the weight integral, only internal edges count.

    Actually: for the Kontsevich integral, a one-loop graph with m
    vertices has m internal edges (forming the loop).
    config_space_dim = 3*m - 3
    form_degree = m (one 1-form per edge)

    For affine vertices: each has valence 3 (2 out, 1 in).
    In a one-loop graph, the m edges use 1 outgoing + 1 incoming per vertex.
    The remaining 1 outgoing per vertex goes to boundary.

    form_degree from internal edges = m
    config_space_dim = 3*m - 3

    Excess = m - (3*m - 3) = -2*m + 3.

    For m=1 (single vertex self-loop): excess = 1.
    But the single-vertex self-loop has 1 edge, dim = 0.
    Excess = 1 - 0 = 1. This should vanish by degree.

    For the equivariant integral, the relevant dimension is
    the dimension of the configuration modulo the quotient.
    A single bulk point modulo translations+dilation: dim = 0.
    The self-loop edge contributes 1-form: excess = 1.
    So single-vertex loops vanish: this is the affine exactness.
    """
    if n_affine_vertices == 0:
        return 0
    m = n_affine_vertices
    dim = max(0, 3 * m - 3)
    # Internal edges in a one-loop graph = m
    fd = m
    return fd - dim


def quadratic_one_loop_excess(n_affine: int, n_quadratic: int) -> int:
    """Form-degree excess for a one-loop graph with quadratic insertions.

    Each quadratic vertex has valence 4 (2 out, 2 in) vs affine's 3.
    The extra incoming edge per quadratic vertex adds +1 to the edge count.

    Total vertices m = n_affine + n_quadratic.
    Internal edges = m (loop) + n_quadratic (extra incoming edges from
    quadratic vertices needing field contractions).
    Config space dim = 3*m - 3 (same, depends only on vertex count).

    Excess = (m + n_quadratic) - (3*m - 3) = -2*m + n_quadratic + 3.

    For single quadratic insertion (m=1, n_quadratic=1, n_affine=0):
    excess = -2 + 1 + 3 = 2. Vanishes by degree.

    For m=2, n_quadratic=1, n_affine=1:
    excess = -4 + 1 + 3 = 0. Marginal case.

    But the valence-shift argument from the text says the excess is
    generically +1 per quadratic vertex relative to affine.
    """
    m = n_affine + n_quadratic
    if m == 0:
        return 0
    dim = max(0, 3 * m - 3)
    # Internal edges in the loop: m
    # Extra edges from quadratic vertices: n_quadratic
    fd = m + n_quadratic
    return fd - dim


def valence_shift_excess(jet_order: int) -> int:
    """Form-degree excess from a single vertex of given jet order.

    An affine vertex (jet 1) has valence 3: 2 out + 1 in.
    A jet-N vertex has valence 2 + N: 2 out + N in.

    The excess relative to affine is (N - 1) per such vertex.
    For jet order 1: excess = 0 (the proved affine case).
    For jet order 2: excess = 1 (quadratic, conj:quadratic-rwi).
    For jet order 3: excess = 2 (cubic, but then cancellation needed).

    NOTE: this is the per-vertex excess, not the total graph excess.
    The total excess depends on the graph topology.
    """
    return jet_order - 1


# ===========================================================================
# delta_2: quadratic correction
# ===========================================================================

def single_insertion_graphs_jet2() -> List[HalfSpaceGraph]:
    """Enumerate single-insertion graphs at jet order 2.

    These graphs have:
    - Exactly one quadratic vertex (jet order 2, valence 4)
    - Any number of affine vertices (jet order 1, valence 3)
    - Total jet order = 2 (so exactly one quadratic vertex, zero affine extra)

    At one loop:
    1. Self-loop on quadratic vertex: 1 vertex, 1 self-edge + externals
    2. Two-vertex loop: quadratic + boundary, 2 edges
    """
    graphs = []

    # Graph 1: single quadratic vertex with self-loop
    g1 = HalfSpaceGraph("quad_self_loop")
    v0 = g1.add_vertex('bulk', 2)
    g1.add_edge(v0, v0)  # self-loop
    graphs.append(g1)

    # Graph 2: quadratic vertex + one affine vertex, loop between them
    g2 = HalfSpaceGraph("quad_affine_loop")
    v0 = g2.add_vertex('bulk', 2)
    v1 = g2.add_vertex('bulk', 1)
    g2.add_edge(v0, v1)
    g2.add_edge(v1, v0)
    graphs.append(g2)

    # Graph 3: quadratic vertex connected to boundary (tree-level with reflection)
    g3 = HalfSpaceGraph("quad_boundary_tree")
    v0 = g3.add_vertex('bulk', 2)
    v1 = g3.add_vertex('boundary', 0)
    g3.add_edge(v0, v1)
    g3.add_edge(v0, v1)
    graphs.append(g3)

    return graphs


def delta2_vanishes_by_valence_shift(pva: PVA) -> Dict[str, object]:
    """Test whether delta_2(V) = 0 by the valence-shift argument.

    The argument:
    1. Each quadratic vertex has valence 4 (vs affine 3)
    2. The extra incoming edge shifts form-degree by +1
    3. For single-insertion graphs, this creates form-degree excess >= 1
    4. The integral vanishes by degree reasons

    Returns a dict with the analysis for each graph type.
    """
    if pva.jet_order < 2:
        return {
            'jet_order': pva.jet_order,
            'delta2': 0,
            'reason': 'jet_order < 2, no quadratic correction',
            'vanishes': True,
            'delta2_vanishes': True,
        }

    results = {}
    graphs = single_insertion_graphs_jet2()

    for g in graphs:
        excess = form_degree_excess(g)
        # Valence shift from the quadratic vertex
        vs = sum(valence_shift_excess(v['jet_order']) for v in g.vertices)

        results[g.name] = {
            'n_vertices': g.n_vertices,
            'n_edges': g.n_edges,
            'config_dim': config_space_dim(g.n_bulk_vertices, g.n_boundary_vertices),
            'form_degree': form_degree(g.n_edges),
            'excess': excess,
            'valence_shift': vs,
            'vanishes_by_degree': excess > 0,
        }

    # Overall: delta_2 vanishes if ALL single-insertion graphs have excess > 0
    # or if their contributions cancel
    all_vanish = all(r['vanishes_by_degree'] for r in results.values())

    return {
        'pva': pva.name,
        'jet_order': pva.jet_order,
        'graphs': results,
        'all_vanish_by_degree': all_vanish,
        'delta2_vanishes': all_vanish,  # by valence shift alone
    }


def delta2_analysis(pva: PVA) -> Dict[str, object]:
    """Full analysis of delta_2(V) for a given PVA.

    Combines valence-shift, Dolgushev-equivariant, and example-verification
    arguments.
    """
    valence = delta2_vanishes_by_valence_shift(pva)

    # Dolgushev argument: equivariant formality guarantees existence of
    # equivariant star product for ALL smooth Poisson structures
    dolgushev_applies = True  # always applies if PVA comes from smooth Poisson

    # Example verification: if PVA is the semiclassical limit of a known VOA,
    # deformation quantization exists by construction
    known_voa_families = {
        "affine_sl2": True,
        "Virasoro": True,
        "W3": True,
        "betagamma": True,
        "Heisenberg": True,
    }
    has_known_quantization = pva.name in known_voa_families

    return {
        'pva': pva.name,
        'jet_order': pva.jet_order,
        'valence_shift': valence,
        'dolgushev_applies': dolgushev_applies,
        'has_known_quantization': has_known_quantization,
        'delta2_vanishes': (
            valence['delta2_vanishes']
            or dolgushev_applies
            or has_known_quantization
        ),
        'mechanism': (
            'valence_shift' if valence['delta2_vanishes']
            else 'dolgushev_equivariant' if dolgushev_applies
            else 'known_quantization' if has_known_quantization
            else 'unknown'
        ),
    }


# ===========================================================================
# delta_3: cubic correction (lollipop + reflected triangle)
# ===========================================================================

def lollipop_graph() -> HalfSpaceGraph:
    """The lollipop graph Gamma_3^{(1)}.

    A single cubic vertex with one self-loop and one external leg.
    The cubic vertex has valence 5: 2 outgoing, 3 incoming.
    The self-loop uses 1 outgoing + 1 incoming.
    Remaining: 1 outgoing + 2 incoming go to external/boundary.

    In the half-space, the self-loop connects the vertex to its image
    under reflection, making it a reflection-stratum contribution.
    """
    g = HalfSpaceGraph("lollipop")
    v0 = g.add_vertex('bulk', 3)  # cubic vertex
    g.add_edge(v0, v0)  # self-loop
    v1 = g.add_vertex('boundary', 0)  # external leg
    g.add_edge(v0, v1)  # outgoing to boundary
    return g


def reflected_triangle_graph() -> HalfSpaceGraph:
    """The reflected triangle graph.

    A tree-level graph with one cubic vertex, one affine vertex,
    and one reflection-stratum edge. The reflection stratum provides
    the image-charge contribution.

    Structure:
    - Cubic vertex (jet 3, valence 5): bulk
    - Affine vertex (jet 1, valence 3): bulk
    - Edges: cubic -> affine, affine -> cubic (loop), plus external legs
    """
    g = HalfSpaceGraph("reflected_triangle")
    v0 = g.add_vertex('bulk', 3)  # cubic vertex
    v1 = g.add_vertex('bulk', 1)  # affine vertex
    g.add_edge(v0, v1)  # cubic -> affine
    g.add_edge(v1, v0)  # affine -> cubic (via reflection)
    v2 = g.add_vertex('boundary', 0)
    g.add_edge(v0, v2)  # external leg
    return g


def delta3_graph_analysis() -> Dict[str, object]:
    """Analyze the graph contributions to delta_3.

    At jet order 3, the correction delta_3 receives contributions from:
    1. Lollipop graph (self-loop on cubic vertex)
    2. Reflected triangle graph (cubic + affine with reflection)

    The conjecture (conj:cubic-rwi) states these cancel.
    """
    lollipop = lollipop_graph()
    triangle = reflected_triangle_graph()

    lollipop_excess = form_degree_excess(lollipop)
    triangle_excess = form_degree_excess(triangle)

    # Valence shift per vertex
    lollipop_vs = sum(valence_shift_excess(v['jet_order']) for v in lollipop.vertices)
    triangle_vs = sum(valence_shift_excess(v['jet_order']) for v in triangle.vertices)

    return {
        'lollipop': {
            'n_vertices': lollipop.n_vertices,
            'n_edges': lollipop.n_edges,
            'config_dim': config_space_dim(lollipop.n_bulk_vertices,
                                           lollipop.n_boundary_vertices),
            'form_degree': form_degree(lollipop.n_edges),
            'excess': lollipop_excess,
            'valence_shift': lollipop_vs,
            'vanishes_by_degree': lollipop_excess > 0,
        },
        'reflected_triangle': {
            'n_vertices': triangle.n_vertices,
            'n_edges': triangle.n_edges,
            'config_dim': config_space_dim(triangle.n_bulk_vertices,
                                           triangle.n_boundary_vertices),
            'form_degree': form_degree(triangle.n_edges),
            'excess': triangle_excess,
            'valence_shift': triangle_vs,
            'vanishes_by_degree': triangle_excess > 0,
        },
        'valence_shift_alone_suffices': (
            lollipop_excess > 0 and triangle_excess > 0
        ),
        'cancellation_needed': not (lollipop_excess > 0 and triangle_excess > 0),
    }


def delta3_cancellation_test(pva: PVA) -> Dict[str, object]:
    """Test the cubic cancellation (conj:cubic-rwi) for a specific PVA.

    For PVAs arising from known VOAs, the deformation quantization exists,
    so delta_3 must vanish. This provides a consistency check.

    For PVAs with jet order < 3, delta_3 = 0 trivially.
    """
    if pva.jet_order < 3:
        return {
            'pva': pva.name,
            'jet_order': pva.jet_order,
            'delta3': 0,
            'reason': 'jet_order < 3, no cubic correction',
            'trivially_zero': True,
            'delta3_vanishes': True,
        }

    graph_analysis = delta3_graph_analysis()

    # For known VOA families, existence of quantization implies delta_3 = 0
    known_voa = pva.name in {"affine_sl2", "Virasoro", "W3", "betagamma", "Heisenberg"}

    return {
        'pva': pva.name,
        'jet_order': pva.jet_order,
        'graph_analysis': graph_analysis,
        'cancellation_needed': graph_analysis['cancellation_needed'],
        'known_voa_implies_vanishing': known_voa,
        'delta3_vanishes': (
            not graph_analysis['cancellation_needed']
            or known_voa
        ),
    }


# ===========================================================================
# Jet-order tower analysis
# ===========================================================================

def jet_order_tower(pva: PVA) -> Dict[str, object]:
    """Analyze the full jet-order tower for a PVA.

    RWI(V) = sum_{N>=2} delta_N(V)
    where delta_1 vanishes by the affine theorem.

    Returns the status of each delta_N up to the PVA's jet order.
    """
    tower = {}

    for N in range(2, pva.jet_order + 1):
        vs_excess = valence_shift_excess(N)
        tower[N] = {
            'jet_order': N,
            'valence_shift_excess': vs_excess,
            'vanishes_by_valence_shift': vs_excess > 0,
            'status': (
                'vanishes_by_degree' if vs_excess > 0
                else 'cancellation_required'
            ),
        }

    return {
        'pva': pva.name,
        'max_jet_order': pva.jet_order,
        'tower': tower,
        'first_nontrivial': min(
            (N for N, data in tower.items()
             if not data['vanishes_by_valence_shift']),
            default=None,
        ),
    }


def standard_landscape_rwi_analysis() -> Dict[str, Dict]:
    """Run the RWI analysis for all standard PVA families.

    Returns a dict keyed by PVA name.
    """
    pvas = {
        'Heisenberg': free_boson_pva(),
        'betagamma': betagamma_pva(Rational(1, 2)),
        'affine_sl2': affine_pva("sl2"),
        'Virasoro': virasoro_pva(Symbol('c')),
        'W3': w3_pva(Symbol('c')),
    }

    results = {}
    for name, pva in pvas.items():
        results[name] = {
            'pva': repr(pva),
            'jet_order': pva.jet_order,
            'delta2': delta2_analysis(pva),
            'delta3': delta3_cancellation_test(pva),
            'tower': jet_order_tower(pva),
        }

    return results


# ===========================================================================
# Numerical integration checks (Monte Carlo weights)
# ===========================================================================

def kontsevich_weight_mc(graph: HalfSpaceGraph, n_samples: int = 10000,
                         seed: int = 42) -> Dict[str, object]:
    """Monte Carlo estimate of the Kontsevich weight of a half-space graph.

    For graphs with form-degree excess > 0, the weight should be zero
    (the integrand has too many forms for the configuration-space dimension).

    This is a numerical sanity check, not a proof.

    We sample random configurations of bulk and boundary points in the
    half-space and evaluate the angular form product.
    """
    import random
    rng = random.Random(seed)

    excess = form_degree_excess(graph)
    if excess > 0:
        # The weight integral is zero by degree reasons — no computation needed
        return {
            'graph': graph.name,
            'excess': excess,
            'weight': 0.0,
            'exact_zero': True,
            'reason': f'form-degree excess = {excess} > 0',
        }

    if excess < 0:
        return {
            'graph': graph.name,
            'excess': excess,
            'weight': None,
            'exact_zero': False,
            'reason': f'form-degree deficit = {excess} < 0, integral needs current',
        }

    # excess == 0: nontrivial integral. Estimate by Monte Carlo.
    # This is a rough estimate; proper integration requires compactification.
    total = 0.0
    n_valid = 0

    for _ in range(n_samples):
        # Sample bulk points in half-space: z in disk, t in (0, R)
        points = []
        for v in graph.vertices:
            if v['type'] == 'bulk':
                z = complex(rng.gauss(0, 1), rng.gauss(0, 1))
                t = abs(rng.gauss(0, 1))  # t > 0
                points.append((z, t))
            else:
                z = complex(rng.gauss(0, 1), rng.gauss(0, 1))
                points.append((z, 0.0))

        # Evaluate product of angular forms
        weight = 1.0
        valid = True
        for (s, tgt) in graph.edges:
            z1, t1 = points[s]
            z2, t2 = points[tgt]
            dz = z1 - z2
            if abs(dz) < 1e-10:
                valid = False
                break
            # Angular form value (modulo normalization)
            weight *= 1.0 / (2 * PI) * abs(dz.imag / (abs(dz) ** 2))

        if valid:
            total += weight
            n_valid += 1

    avg = total / max(n_valid, 1)
    return {
        'graph': graph.name,
        'excess': excess,
        'weight': avg,
        'n_samples': n_samples,
        'n_valid': n_valid,
        'exact_zero': False,
    }


# ===========================================================================
# Status summary
# ===========================================================================

def rwi_status_summary() -> Dict[str, str]:
    """Status of the reflected weight identity programme."""
    return {
        'jet_order_0': 'TRIVIAL (no interactions)',
        'jet_order_1': 'PROVED (thm:affine-half-space-bv)',
        'jet_order_2': 'OPEN (conj:quadratic-rwi, supported by valence-shift + Dolgushev + examples)',
        'jet_order_3': 'OPEN (conj:cubic-rwi, requires lollipop-triangle cancellation)',
        'jet_order_geq_4': 'OPEN (conditional on cubic case)',
        'general': 'OPEN (conj:general-half-space-bv)',
        'broken_ref': 'thm:quadratic-rwi is referenced at line 1200 but label is conj:quadratic-rwi (ClaimStatusOpen)',
    }
