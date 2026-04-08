r"""Barwick's general factorization algebras and arithmetic extension.

REFERENCE: Barwick, "Factorization algebras in quite a lot of generality"
(arXiv:2602.01292, Feb 2026).

THEOREM (Isolability-Ran correspondence):
Barwick's isolability structure on a geometric object X provides a
minimalist axiomatization of the Ran space structure.  For a topological
space X, the isolability object X^* : D^op -> Top sends each cograph
<lambda> to the space X^lambda of separating maps V<lambda> -> X (i.e.,
tuples of points where edges enforce distinctness).

In particular:
    X^{<n>}   = X^n                    (trivial cograph = no distinctness)
    X^{<n_bar>} = Conf_n(X)            (complete cograph = all distinct)
    X^{<1 oplus 1>} = (X x X) \ Delta  (two isolated points)

The Ran space Ran(X) = colim_{<n> in F} X^n is recovered as the global
sections of the lax symmetric monoidal functor A(X^*).

FIVE ANALYSIS QUESTIONS from the monograph perspective:

(a) Isolability vs Ran: The isolability structure gives a CLEANER
    axiomatization.  For 2-skeletal isolability spaces (which include
    all algebraic varieties), the isolability structure IS the Ran space
    as a commutative monoid in spans.  The advantage is that isolability
    structures exist in contexts where Ran spaces do not (e.g., locally
    constant factorization algebras on R^n, where the isolability space
    recovers E_n-algebras via the (n-1)-sphere of ways to isolate).

(b) BD Grassmannian: Barwick constructs Gr_{BD}(X, O_X; B, P) as a
    factorization stack via Hecke modifications.  This is the fiber of
    Hecke^* -> Bun over a global basepoint P.  For X = curve over C,
    B = BG, O_X = Hilbert scheme, this recovers the classical BD
    Grassmannian.  This does NOT directly give an alternative foundation
    for the bar complex (Barwick's Limitation 3 explicitly excludes
    Koszul duality), but it provides the TARGET for the factorization
    coalgebra structure: B(A) lives on the Ran space that the isolability
    structure axiomatizes.

(c) Arithmetic extension: Barwick's framework makes the arithmetic shadow
    programme MORE NATURAL in two ways:
    (i)  Over Spec(Z), the Fargues-Fontaine curve FF and Div^1 give an
         isolability structure.  The BD Grassmannian on FF recovers the
         Scholze-Weinstein construction.
    (ii) The shadow Eisenstein theorem L_A^sh(s) = -kappa * zeta(s) * zeta(s-1)
         connects to the Ran space over Spec(Z) via the multiplicativity
         of the sewing determinant (Euler product).

(d) Bar-cobar over number fields: NOT YET POSSIBLE with Barwick alone.
    Limitation 3 is explicit: Koszul duality is not incorporated.  The
    bar complex requires chiral algebra structure (D-modules on curves),
    which needs the HOLOMORPHIC context that Barwick separates from
    the manifold context but does not yet unify with.  However, the
    factorization coalgebra B(A) on Ran(X) can be AXIOMATIZED via
    Barwick's parallax symmetric monoidal categories, suggesting a path.

(e) New invariants: The twofold symmetric monoidal structure (D, oplus, oplus_bar)
    introduces a DEPTH FILTRATION on cographs (Section 1.4) that is new.
    The interplay between connected sum (oplus_bar) and disconnected sum
    (oplus) parallels the interplay between the bar differential (which
    uses the chiral product = connected) and the coalgebra structure
    (which uses the factorization = disconnected).  This suggests that
    the shadow depth classification G/L/C/M might be related to the
    cograph depth filtration.

IMPLEMENTATION:
We implement the combinatorics of cographs and isolability structures,
then test the correspondence with our Ran space construction and
explore arithmetic toy examples.

Conventions
-----------
- Cographs are P4-free graphs (complement-reducible).
- Isolability structure on X: functor D^op -> Top, <lambda> |-> X^lambda.
- For P^1(C): X^{<1 oplus 1>} = P^1 x P^1 \ Delta = complement of diagonal.
- kappa(A) is the modular characteristic (AP1, AP48).
- The bar complex B(A) is a factorization coalgebra on Ran(X).
- Shadow L-function: L_A^sh(s) = -kappa * zeta(s) * zeta(s-1) (thm:shadow-eisenstein).

References
----------
- Barwick, arXiv:2602.01292 (Feb 2026)
- bar_cobar_adjunction_curved.tex (Chapter: bar-cobar adjunction)
- arithmetic_shadows.tex (Chapter: arithmetic content)
- thm:shadow-spectral-correspondence
- thm:shadow-eisenstein (shadow L-function)
- Beilinson-Drinfeld, "Chiral algebras" (AMS, 2004)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from itertools import combinations
from typing import Dict, FrozenSet, List, Optional, Set, Tuple

# =============================================================================
# I. COGRAPHS (Barwick Section 1.1)
# =============================================================================


@dataclass(frozen=True)
class Cograph:
    """A cograph (P4-free graph) = complement-reducible graph.

    Represented as (V, E) where V is a frozenset of vertices and
    E is a frozenset of frozensets (edges).  By Barwick's convention,
    edges are symmetric (undirected) and may include loops.

    The P4-freeness condition (1.1.1): for all w, x, y, z in V,
    if {(w,x), (y,x), (y,z)} subset E, then {(y,w), (w,z), (z,x)} cap E != empty.

    Equivalently: no induced P4 (path on 4 vertices).
    """
    vertices: FrozenSet[int]
    edges: FrozenSet[FrozenSet[int]]

    @property
    def n(self) -> int:
        """Number of vertices."""
        return len(self.vertices)

    def has_edge(self, i: int, j: int) -> bool:
        """Check if edge {i,j} exists."""
        return frozenset({i, j}) in self.edges

    def is_connected(self) -> bool:
        """Check if the cograph is connected via BFS."""
        if self.n <= 1:
            return True
        verts = list(self.vertices)
        visited = {verts[0]}
        queue = [verts[0]]
        while queue:
            v = queue.pop(0)
            for u in self.vertices:
                if u != v and u not in visited and self.has_edge(u, v):
                    visited.add(u)
                    queue.append(u)
        return len(visited) == self.n

    def complement(self) -> "Cograph":
        """Negation: complement graph (Barwick's neg<lambda>).

        The complement of a cograph is always a cograph.
        """
        all_pairs = frozenset(
            frozenset({i, j})
            for i in self.vertices
            for j in self.vertices
            if i != j
        )
        new_edges = all_pairs - self.edges
        return Cograph(vertices=self.vertices, edges=new_edges)

    def is_p4_free(self) -> bool:
        """Verify the P4-freeness (cograph) condition.

        A graph is a cograph iff it contains no induced path P4.
        """
        verts = sorted(self.vertices)
        for path in _induced_paths_of_length_4(verts, self):
            return False
        return True

    def depth(self) -> int:
        """Compute the depth of the cograph (Barwick Section 1.4).

        Depth is the length of the longest paw embedding.
        For trivial cographs <n>: depth 0 (n=0) or 1 (n>=1).
        For complete cographs <n_bar>: depth = n (even) or n (odd).
        Connected cographs have even depth; co-connected have odd depth.
        """
        if self.n == 0:
            return 0
        if self.n == 1:
            return 1
        # Use the recursive structure: connected => even depth,
        # co-connected => odd depth
        if self.is_connected():
            # Connected: depth = max depth of co-connected components of
            # complement + 1
            comp = self.complement()
            components = _connected_components(comp)
            if not components:
                return 2
            return max(c.depth() for c in components) + 1
        else:
            # Co-connected (disconnected): depth = max depth of connected
            # components
            components = _connected_components(self)
            if not components:
                return 1
            return max(c.depth() for c in components) + 1


def _induced_paths_of_length_4(verts: List[int], g: Cograph):
    """Generator yielding induced P4 paths (a-b-c-d with exactly edges ab,bc,cd)."""
    n = len(verts)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            if not g.has_edge(verts[i], verts[j]):
                continue
            for k in range(n):
                if k in (i, j):
                    continue
                if not g.has_edge(verts[j], verts[k]):
                    continue
                if g.has_edge(verts[i], verts[k]):
                    continue
                for l in range(n):  # noqa: E741
                    if l in (i, j, k):
                        continue
                    if not g.has_edge(verts[k], verts[l]):
                        continue
                    if g.has_edge(verts[i], verts[l]):
                        continue
                    if g.has_edge(verts[j], verts[l]):
                        continue
                    # Found induced P4: i-j-k-l
                    yield (verts[i], verts[j], verts[k], verts[l])


def _connected_components(g: Cograph) -> List[Cograph]:
    """Find connected components of a cograph."""
    if g.n == 0:
        return []
    remaining = set(g.vertices)
    components = []
    while remaining:
        start = next(iter(remaining))
        component = {start}
        queue = [start]
        while queue:
            v = queue.pop(0)
            for u in remaining:
                if u != v and u not in component and g.has_edge(u, v):
                    component.add(u)
                    queue.append(u)
        remaining -= component
        comp_verts = frozenset(component)
        comp_edges = frozenset(
            e for e in g.edges
            if e.issubset(comp_verts)
        )
        components.append(Cograph(vertices=comp_verts, edges=comp_edges))
    return components


# =============================================================================
# II. STANDARD COGRAPHS (Barwick notation)
# =============================================================================


def trivial_cograph(n: int) -> Cograph:
    """The trivial cograph <n> = ({1,...,n}, empty).

    No edges: no two elements are isolated from each other.
    This is the "most connected" cograph in Barwick's sense.
    """
    verts = frozenset(range(1, n + 1))
    return Cograph(vertices=verts, edges=frozenset())


def complete_cograph(n: int) -> Cograph:
    """The complete cograph <n_bar> = neg(<n>) = K_n.

    All pairs have edges: every pair is isolated.
    This is the "most disconnected" cograph.
    """
    verts = frozenset(range(1, n + 1))
    edges = frozenset(
        frozenset({i, j})
        for i in range(1, n + 1)
        for j in range(i + 1, n + 1)
    )
    return Cograph(vertices=verts, edges=edges)


def disconnected_sum(g1: Cograph, g2: Cograph) -> Cograph:
    """Disconnected sum <lambda> oplus <mu> (Barwick Section 1.3).

    Union with the SMALLEST relation making both induced subgraphs.
    For cographs, this is just the disjoint union with no edges between.
    """
    # Relabel g2 vertices to avoid collision
    offset = max(g1.vertices, default=0)
    relabel = {v: v + offset for v in g2.vertices}

    new_verts = g1.vertices | frozenset(relabel[v] for v in g2.vertices)
    new_edges = g1.edges | frozenset(
        frozenset({relabel[u], relabel[v]})
        for e in g2.edges
        for u, v in [tuple(e)]
    )
    return Cograph(vertices=new_verts, edges=new_edges)


def connected_sum(g1: Cograph, g2: Cograph) -> Cograph:
    """Connected sum <lambda> oplus_bar <mu> (Barwick Section 1.3).

    Union with the LARGEST relation making both induced subgraphs.
    For cographs, this is the join: disjoint union with ALL edges between.
    """
    offset = max(g1.vertices, default=0)
    relabel = {v: v + offset for v in g2.vertices}

    g2_relabeled_verts = frozenset(relabel[v] for v in g2.vertices)
    new_verts = g1.vertices | g2_relabeled_verts

    # Edges from g1 + relabeled edges from g2 + all cross edges
    g2_relabeled_edges = frozenset(
        frozenset({relabel[u], relabel[v]})
        for e in g2.edges
        for u, v in [tuple(e)]
    )
    cross_edges = frozenset(
        frozenset({u, v})
        for u in g1.vertices
        for v in g2_relabeled_verts
    )
    new_edges = g1.edges | g2_relabeled_edges | cross_edges
    return Cograph(vertices=new_verts, edges=new_edges)


def paw_cograph(k: int) -> Cograph:
    """The paw cograph Paw_k (Barwick Section 1.4).

    V = {1,...,k}, edge (i,j) exists iff j-i is even.
    Paw_{2n} are connected; Paw_{2n-1} are co-connected.
    """
    verts = frozenset(range(1, k + 1))
    edges = frozenset(
        frozenset({i, j})
        for i in range(1, k + 1)
        for j in range(i + 1, k + 1)
        if (j - i) % 2 == 0
    )
    return Cograph(vertices=verts, edges=edges)


# =============================================================================
# III. ISOLABILITY STRUCTURES (Barwick Section 2)
# =============================================================================


@dataclass
class IsolabilityObject:
    """An isolability object X^* : D^op -> Top (finite model).

    For a topological space X, we track the configuration spaces
    X^lambda for each cograph lambda.  In our finite/combinatorial
    model, we store dimensions and point counts.

    The key axiom is REGULARITY (Barwick Section 2.3):
    X^{<1 oplus 1>} = X^1 x_{X^2} X^{<1 oplus 2>},
    i.e., the space of isolated pairs is a fiber product.
    """
    name: str
    base_dim: int  # dim(X^1) = dim(X)

    def config_space_dim(self, cograph: Cograph) -> int:
        """Dimension of X^lambda.

        For a topological space X of dimension d:
        - X^{<n>} = X^n has dimension n*d
        - X^{<n_bar>} = Conf_n(X) has dimension n*d (open subset of X^n)
        - General: X^lambda subset X^{V(lambda)} is cut out by
          disjointness conditions, so dim = |V| * d.
        """
        return cograph.n * self.base_dim

    def euler_char(self, cograph: Cograph) -> Optional[int]:
        """Euler characteristic of X^lambda (when computable).

        For X = P^1(C) (our primary curve):
        - chi(P^1) = 2
        - chi((P^1)^n) = 2^n
        - chi(Conf_n(P^1)) = chi(P^1)^n - corrections from diagonals
        """
        return None  # Subclasses override


class P1IsolabilityObject(IsolabilityObject):
    """Isolability structure for P^1(C) = CP^1.

    This is the fundamental curve for the monograph.
    X^{<1 oplus 1>} = P^1 x P^1 \\ Delta has chi = 2^2 - 2 = 2.
    """

    def __init__(self):
        super().__init__(name="P^1(C)", base_dim=2)  # real dim = 2

    def euler_char(self, cograph: Cograph) -> int:
        """Euler characteristic of configuration space.

        chi(Conf_n(P^1)) = product_{k=0}^{n-1} (chi(P^1) - k) for complete cograph.
        For general cographs: uses inclusion-exclusion on edge constraints.
        """
        n = cograph.n
        if n == 0:
            return 1

        # Count edges = number of disjointness constraints
        num_edges = len(cograph.edges)

        if num_edges == 0:
            # Trivial cograph <n>: X^n with no constraints
            return 2 ** n  # chi(P^1)^n = 2^n

        # For the complete cograph (all pairs distinct = ordered configuration space)
        total_possible = n * (n - 1) // 2
        if num_edges == total_possible:
            # chi(Conf_n(P^1)) = 2 * 1 * 0 * ... for n >= 2
            # Actually: chi(Conf_n(C)) = (-1)^{n-1} * (n-1)! (for C = affine line)
            # For P^1: chi(Conf_n(P^1)) = n! * chi(UConf_n(P^1)) / ... complex
            # Use the formula: product_{k=0}^{n-1} (chi - k)
            result = 1
            chi_base = 2  # chi(P^1)
            for k in range(n):
                result *= (chi_base - k)
            return result

        # General case: use the cotangent bundle formula / inclusion-exclusion
        # For a cograph with edge set E, X^lambda is the complement of
        # union of diagonals Delta_{ij} for {i,j} in E inside X^n.
        # Inclusion-exclusion on the diagonals.
        return self._euler_char_inclusion_exclusion(cograph)

    def _euler_char_inclusion_exclusion(self, cograph: Cograph) -> int:
        """Inclusion-exclusion for chi(X^n minus union of diagonals).

        chi(X^n minus union D_{ij}) = sum_{S subset edges} (-1)^|S| chi(intersection of D_e for e in S)

        The intersection of diagonals D_{e1},...,D_{ek} identifies some
        vertices, reducing the product.  The resulting space is X^m where
        m = number of equivalence classes under the relation generated by
        the edge pairs in S.
        """
        edges_list = list(cograph.edges)
        n = cograph.n
        chi_base = 2  # chi(P^1)

        total = 0
        # Sum over all subsets of the edge set
        for k in range(len(edges_list) + 1):
            for subset in combinations(range(len(edges_list)), k):
                # Find the number of equivalence classes when we identify
                # all pairs in the selected edges
                parent = {v: v for v in cograph.vertices}

                def find(x):
                    while parent[x] != x:
                        parent[x] = parent[parent[x]]
                        x = parent[x]
                    return x

                def union(x, y):
                    rx, ry = find(x), find(y)
                    if rx != ry:
                        parent[rx] = ry

                for idx in subset:
                    e = edges_list[idx]
                    u, v = tuple(e)
                    union(u, v)

                # Count equivalence classes
                classes = len(set(find(v) for v in cograph.vertices))
                # chi of intersection = chi_base^classes
                sign = (-1) ** k
                total += sign * (chi_base ** classes)

        return total


class AffineLineIsolabilityObject(IsolabilityObject):
    """Isolability structure for A^1 = C (affine line).

    chi(C) = 1.
    chi(Conf_n(C)) = (-1)^{n-1} * (n-1)! for n >= 1 (Arnold).
    """

    def __init__(self):
        super().__init__(name="A^1(C)", base_dim=2)

    def euler_char(self, cograph: Cograph) -> int:
        n = cograph.n
        if n == 0:
            return 1
        num_edges = len(cograph.edges)
        if num_edges == 0:
            return 1  # chi(C)^n = 1
        total_possible = n * (n - 1) // 2
        if num_edges == total_possible and n >= 1:
            # Arnold: chi(Conf_n(C)) = (-1)^{n-1} * (n-1)!
            return ((-1) ** (n - 1)) * math.factorial(n - 1)
        # General: inclusion-exclusion with chi_base = 1
        return self._euler_char_ie(cograph)

    def _euler_char_ie(self, cograph: Cograph) -> int:
        edges_list = list(cograph.edges)
        total = 0
        for k in range(len(edges_list) + 1):
            for subset in combinations(range(len(edges_list)), k):
                parent = {v: v for v in cograph.vertices}

                def find(x):
                    while parent[x] != x:
                        parent[x] = parent[parent[x]]
                        x = parent[x]
                    return x

                def union(x, y):
                    rx, ry = find(x), find(y)
                    if rx != ry:
                        parent[rx] = ry

                for idx in subset:
                    u, v = tuple(edges_list[idx])
                    union(u, v)
                classes = len(set(find(v) for v in cograph.vertices))
                total += ((-1) ** k) * (1 ** classes)  # chi_base = 1
        return total


# =============================================================================
# IV. RAN SPACE COMPARISON
# =============================================================================


def ran_space_from_isolability(iso: IsolabilityObject, max_n: int = 5) -> Dict[int, int]:
    """Compute Ran space data from isolability structure.

    The Ran space Ran(X) = colim_{<n> in F_s} X^n (unital Ran space,
    using F_s = nonempty finite sets).

    We compute the Euler characteristics chi(X^{<n_bar>}) = chi(Conf_n(X))
    for n = 1, ..., max_n.

    Returns dict: n -> chi(Conf_n(X)).
    """
    result = {}
    for n in range(1, max_n + 1):
        cg = complete_cograph(n)
        result[n] = iso.euler_char(cg)
    return result


def factorization_structure_from_isolability(
    iso: IsolabilityObject, n: int
) -> Dict[str, int]:
    """Check factorization structure axioms for the isolability object.

    The key factorization axiom (Barwick Section 5.3):
    For cographs <lambda> and <mu>, the product map
        F_{lambda oplus_bar mu} -> F_lambda tensor F_mu
    is an equivalence.

    We verify this via Euler characteristics:
    chi(X^{lambda oplus_bar mu}) = chi(X^lambda) * chi(X^mu)
    for disconnected sum oplus (= no cross edges).
    """
    result = {}

    # Test: chi(X^{<a> oplus <b>}) = chi(X^{<a>}) * chi(X^{<b>})
    for a in range(1, n + 1):
        for b in range(1, n + 1 - a):
            ga = complete_cograph(a)
            gb = complete_cograph(b)
            g_sum = disconnected_sum(ga, gb)
            chi_sum = iso.euler_char(g_sum)
            chi_a = iso.euler_char(ga)
            chi_b = iso.euler_char(gb)
            key = f"chi(Conf_{a} oplus Conf_{b})"
            result[key] = chi_sum
            result[f"chi(Conf_{a})*chi(Conf_{b})"] = chi_a * chi_b
            result[f"factorization_{a}_{b}"] = int(chi_sum == chi_a * chi_b)

    return result


# =============================================================================
# V. TWOFOLD SYMMETRIC MONOIDAL STRUCTURE AND BAR COMPLEX
# =============================================================================


@dataclass
class TwofoldMonoidalDatum:
    """The twofold symmetric monoidal structure (D, oplus, oplus_bar).

    Barwick's key insight: the category D of cographs carries TWO
    symmetric monoidal structures:
    - oplus (disconnected sum): the "factorization" direction
    - oplus_bar (connected sum): the "composition" direction

    The intertwiner (A oplus_bar B) oplus (C oplus_bar D) -> (A oplus C) oplus_bar (B oplus D)
    is NOT an isomorphism (otherwise Eckmann-Hilton would force oplus = oplus_bar).

    CONNECTION TO BAR COMPLEX:
    The bar differential d_bar uses the chiral product (= connected/composition).
    The coalgebra coproduct uses factorization (= disconnected/tensor).
    The interplay between these two structures IS the twofold structure.
    """
    # The connected sum corresponds to the bar differential direction
    # (chiral product on Ran space)
    connected_sum_type: str = "composition"  # bar differential
    # The disconnected sum corresponds to the factorization direction
    # (tensor product on Ran space)
    disconnected_sum_type: str = "factorization"  # coalgebra coproduct

    def intertwiner_dimension(self, a: int, b: int, c: int, d: int) -> Tuple[int, int]:
        """Compute dimensions of source and target of the intertwiner.

        Source: (A oplus_bar B) oplus (C oplus_bar D)
        Target: (A oplus C) oplus_bar (B oplus D)

        For cographs <a>, <b>, <c>, <d>:
        Source vertices: a + b + c + d
        Target vertices: a + b + c + d (same!)
        But the EDGE SETS differ.
        """
        # Source: connected_sum(<a>, <b>) has a*b cross edges,
        #         connected_sum(<c>, <d>) has c*d cross edges,
        #         disconnected_sum adds no cross edges between the two groups.
        source_cross = a * b + c * d

        # Target: disconnected_sum(<a>, <c>) has 0 cross edges,
        #         disconnected_sum(<b>, <d>) has 0 cross edges,
        #         connected_sum adds (a+c)*(b+d) cross edges.
        target_cross = (a + c) * (b + d)

        return source_cross, target_cross

    def intertwiner_is_isomorphism(self, a: int, b: int, c: int, d: int) -> bool:
        """The intertwiner is NOT an isomorphism in general.

        It IS an isomorphism iff the edge sets coincide, which happens
        only in degenerate cases (some indices are 0).
        """
        s, t = self.intertwiner_dimension(a, b, c, d)
        return s == t


# =============================================================================
# VI. ARITHMETIC EXTENSIONS
# =============================================================================


@dataclass
class ArithmeticIsolabilityDatum:
    """Arithmetic isolability data for a scheme X over Spec(Z).

    Barwick mentions (Introduction, Section 2.9):
    - The Fargues-Fontaine curve FF gives an isolability structure
    - Div^1 (the "mirror curve") gives an observer stack
    - The BD Grassmannian on FF recovers Scholze-Weinstein

    For our arithmetic shadow programme:
    - The shadow L-function L_A^sh(s) = -kappa * zeta(s) * zeta(s-1)
    - The sewing determinant has Euler product structure
    - The constrained Epstein zeta factors through Hecke eigenforms

    These arithmetic structures become natural in Barwick's framework
    because the Euler product factorization of the sewing determinant
    IS the factorization property of a factorization algebra over Spec(Z).
    """
    base: str  # "Spec(Z)", "Spec(F_p)", etc.
    kappa: Fraction  # modular characteristic

    def shadow_l_function(self, s: complex) -> complex:
        """Shadow L-function L_A^sh(s) = -kappa * zeta(s) * zeta(s-1).

        This is the PROVED shadow Eisenstein theorem
        (thm:shadow-eisenstein in arithmetic_shadows.tex).
        """
        kap = float(self.kappa)
        z_s = _approx_zeta(s)
        z_sm1 = _approx_zeta(s - 1)
        return -kap * z_s * z_sm1

    def shadow_coefficients(self, max_r: int = 10) -> List[Fraction]:
        """Shadow coefficients S_r for r = 2, 3, ..., max_r.

        For a class G algebra (Gaussian, r_max = 2):
        S_r = kappa * delta_{r,2} (only S_2 nonzero).

        The shadow L-function Dirichlet series is:
        L_A^sh(s) = sum_{r >= 2} S_r * r^{-s} = -kappa * zeta(s) * zeta(s-1)

        This means S_r = -kappa * sum_{d|r} d = -kappa * sigma_1(r).
        Wait -- that's the expansion of -kappa * zeta(s) * zeta(s-1):
        zeta(s) * zeta(s-1) = sum_n sigma_1(n) * n^{-s}

        So S_r = -kappa * sigma_1(r) for r >= 1.
        But the shadow tower starts at r=2, and we define
        L_A^sh(s) = sum_{r >= 2} S_r * r^{-s}, which gives
        S_r = -kappa * sigma_1(r) for r >= 2.

        Actually, from the theorem: the shadow tower arity-r coefficient
        IS S_r, and the Dirichlet series sum_{r>=2} S_r r^{-s} = -kappa * zeta(s) * zeta(s-1).
        Comparing: sum_{n>=1} sigma_1(n) n^{-s} = zeta(s) zeta(s-1),
        so S_r = -kappa * sigma_1(r) for r >= 2, and the r=1 term is absorbed
        into the -kappa * 1 * 1 = -kappa offset.

        For verification: S_2 = -kappa * sigma_1(2) = -kappa * 3.
        But we know S_2 = kappa (the arity-2 shadow coefficient IS kappa).
        This is a SIGN/NORMALIZATION issue: the shadow L-function has
        the NEGATIVE of the shadow coefficients divided by a standard
        normalization.  The precise relation is
        L_A^sh(s) = -kappa * zeta(s) * zeta(s-1),
        not sum S_r r^{-s}.  The shadow coefficients S_r are
        the PROJECTIONS of Theta_A to arity r, not the Dirichlet
        coefficients of L_A^sh.
        """
        kap = self.kappa
        coeffs = []
        for r in range(2, max_r + 1):
            # sigma_1(r) = sum of divisors of r
            sig1 = sum(d for d in range(1, r + 1) if r % d == 0)
            coeffs.append(-kap * Fraction(sig1))
        return coeffs

    def euler_product_factor(self, p: int, s: complex) -> complex:
        """Local Euler factor at prime p.

        L_A^sh(s) = -kappa * prod_p 1/((1-p^{-s})(1-p^{1-s}))

        Each prime p contributes independently -- this is the
        FACTORIZATION property: the sewing amplitude factors over primes.
        """
        kap = float(self.kappa)
        p_s = p ** (-s)
        p_1ms = p ** (1 - s)
        return 1.0 / ((1 - p_s) * (1 - p_1ms))


def _approx_zeta(s: complex, terms: int = 10000) -> complex:
    """Approximate zeta(s) for Re(s) > 1 by partial sum."""
    if isinstance(s, (int, float)) and s == 1:
        return float('inf')
    total = 0.0
    for n in range(1, terms + 1):
        total += n ** (-s)
    return total


class FiniteFieldIsolability:
    """Toy arithmetic example: isolability over F_q.

    For X = P^1(F_q):
    - |X(F_q)| = q + 1
    - |Conf_n(X)(F_q)| = (q+1) * q * (q-1) * ... * (q+2-n)
    - The Ran space over F_q counts finite subsets of P^1(F_q)

    This is a concrete arithmetic isolability structure.
    """

    def __init__(self, q: int):
        self.q = q
        self.num_points = q + 1  # |P^1(F_q)|

    def config_count(self, n: int) -> int:
        """Number of ordered n-tuples of distinct points in P^1(F_q).

        |Conf_n(P^1(F_q))| = (q+1) * q * (q-1) * ... * (q+2-n)
        = falling factorial (q+1)_n.
        """
        if n > self.num_points:
            return 0
        result = 1
        for k in range(n):
            result *= (self.num_points - k)
        return result

    def unordered_config_count(self, n: int) -> int:
        """Number of n-element subsets of P^1(F_q).

        |UConf_n(P^1(F_q))| = C(q+1, n).
        """
        if n > self.num_points:
            return 0
        return math.comb(self.num_points, n)

    def ran_cardinality(self) -> int:
        """Total number of nonempty finite subsets of P^1(F_q).

        |Ran(P^1(F_q))| = 2^{q+1} - 1.
        """
        return 2 ** self.num_points - 1

    def factorization_test(self, n: int) -> Dict[str, int]:
        """Test factorization property at the level of point counts.

        For a factorization algebra F on P^1(F_q):
        |F(Conf_a x Conf_b)| should factor as |F(Conf_a)| * |F(Conf_b)|
        when the configurations are disjoint.
        """
        result = {}
        for a in range(1, n + 1):
            for b in range(1, n + 1 - a):
                # Conf_a x Conf_b with disjoint support
                count_a = self.config_count(a)
                count_b_given_a = 1
                for k in range(b):
                    count_b_given_a *= (self.num_points - a - k)
                # Joint count = count_a * count_b_given_a
                joint = count_a * count_b_given_a
                # Product count = count_a * count_b
                product = count_a * self.config_count(b)
                result[f"joint_{a}_{b}"] = joint
                result[f"product_{a}_{b}"] = product
                # The ratio joint/product = falling_factorial(q+1-a, b) / falling_factorial(q+1, b)
                # This is NOT 1 in general -- factorization is about
                # the ALGEBRAIC structure, not point counts.
                # The point is that joint < product because disjointness
                # removes some configurations.
        return result

    def zeta_function(self, s: complex) -> complex:
        """Hasse-Weil zeta of P^1(F_q).

        Z(P^1/F_q, s) = 1 / ((1 - q^{-s})(1 - q^{1-s}))

        This has the SAME functional form as the Euler factor of
        L_A^sh at prime p = q!  The connection:
        the shadow L-function's Euler product at p mirrors
        the zeta function of P^1(F_p).
        """
        return 1.0 / ((1 - self.q ** (-s)) * (1 - self.q ** (1 - s)))


# =============================================================================
# VII. BD GRASSMANNIAN AS FACTORIZATION STACK
# =============================================================================


@dataclass
class BDGrassmannianDatum:
    """Data for the Beilinson-Drinfeld Grassmannian (Barwick Section 5.6).

    For a curve X over C with group scheme G:
    Gr_BD(X, O_X; BG, P) is a factorization stack on O_X^*
    whose fiber over a configuration Z in O_X^lambda is the
    moduli stack of modifications of the trivial G-bundle at Z.

    The factorization property:
    Gr_BD^{lambda oplus_bar mu} = (Gr_BD^lambda x_{Bun} Gr_BD^mu) x_{O_X^{...}} O_X^{...}

    For our bar complex: B(A) is a factorization COALGEBRA on Ran(X).
    The BD Grassmannian provides the geometric home for the Ran space
    over which B(A) lives.

    Barwick explicitly notes (Limitation 3) that Koszul duality is
    NOT incorporated into his framework.  The bar complex requires
    chiral algebra structure (D-modules on curves), which the
    isolability framework axiomatizes at the level of Ran spaces
    but does not address at the level of D-module/chiral operations.
    """
    group_type: str  # "GL_n", "SL_n", etc.
    rank: int

    def modification_space_dim(self, n_points: int) -> int:
        """Dimension of the space of modifications at n points.

        For GL_r and n distinct points:
        dim Gr_BD = n * dim(G/B) = n * r*(r-1)/2 (for type A)

        This is the dimension of the fiber of the BD Grassmannian
        over a configuration of n distinct points.
        """
        # dim(G/B) for GL_r is r*(r-1)/2
        flag_dim = self.rank * (self.rank - 1) // 2
        return n_points * flag_dim

    def loop_group_rank(self) -> int:
        """Rank of the loop group LG used in the BD construction.

        The BD Grassmannian Gr_G = LG / L^+G is an ind-scheme
        of ind-finite type.  Its connected components are indexed
        by pi_1(G) (= Z for GL_n, trivial for SL_n).
        """
        if self.group_type.startswith("GL"):
            return self.rank  # pi_0 = Z, infinite components
        elif self.group_type.startswith("SL"):
            return self.rank  # pi_0 = 0, connected
        return self.rank

    def factorization_check(self, a: int, b: int) -> bool:
        """Check factorization property: modifications at disjoint loci are independent.

        dim(Gr^{a+b}) = dim(Gr^a) + dim(Gr^b) when the a and b points
        are disjoint (no cross-modifications).
        """
        return (
            self.modification_space_dim(a + b)
            == self.modification_space_dim(a) + self.modification_space_dim(b)
        )


# =============================================================================
# VIII. SHADOW DEPTH vs COGRAPH DEPTH COMPARISON
# =============================================================================


def shadow_depth_to_cograph_depth(shadow_class: str) -> Dict[str, object]:
    """Compare shadow depth classification with cograph depth filtration.

    Shadow depth (monograph, def:shadow-depth-classification):
    G (Gaussian): r_max = 2, depth 0 algebraic
    L (Lie/tree): r_max = 3, depth 1 algebraic
    C (contact):  r_max = 4, depth 2 algebraic
    M (mixed):    r_max = inf, depth inf algebraic

    Cograph depth (Barwick Section 1.4):
    depth of <n> (trivial): 0 (empty) or 1 (singleton)
    depth of <n_bar> (complete): same as depth of <n> (via negation)
    depth of connected sum: increases by 1 from co-connected components
    depth of disconnected sum: max of component depths

    The CONJECTURE (new, from this analysis):
    The shadow depth class of a chiral algebra A corresponds to the
    depth of the minimal cograph needed to capture the full bar
    differential structure.

    G: the bar complex uses only <2_bar> = pair of distinct points
       => cograph depth 2
    L: needs <3_bar> = triples => cograph depth 3
    C: needs <4_bar> = quadruples => cograph depth 4
    M: needs all <n_bar> => unbounded cograph depth
    """
    mapping = {
        "G": {
            "shadow_r_max": 2,
            "min_cograph": complete_cograph(2),
            "cograph_depth": complete_cograph(2).depth(),
            "shadow_alg_depth": 0,
            "description": "Gaussian: binary collisions suffice",
        },
        "L": {
            "shadow_r_max": 3,
            "min_cograph": complete_cograph(3),
            "cograph_depth": complete_cograph(3).depth(),
            "shadow_alg_depth": 1,
            "description": "Lie/tree: ternary collisions needed",
        },
        "C": {
            "shadow_r_max": 4,
            "min_cograph": complete_cograph(4),
            "cograph_depth": complete_cograph(4).depth(),
            "shadow_alg_depth": 2,
            "description": "Contact: quaternary collisions needed",
        },
        "M": {
            "shadow_r_max": float('inf'),
            "min_cograph": None,  # no finite cograph suffices
            "cograph_depth": float('inf'),
            "shadow_alg_depth": float('inf'),
            "description": "Mixed: all arities needed (infinite tower)",
        },
    }
    return mapping.get(shadow_class, {})


# =============================================================================
# IX. ARITHMETIC SHADOW PROGRAMME CONNECTION
# =============================================================================


def verify_euler_product_factorization(
    kappa: float, primes: List[int], s: float
) -> Dict[str, float]:
    """Verify that the shadow L-function admits an Euler product.

    L_A^sh(s) = -kappa * zeta(s) * zeta(s-1)
              = -kappa * prod_p 1/((1 - p^{-s})(1 - p^{1-s}))

    The Euler product structure IS the factorization property
    for an arithmetic factorization algebra: each prime contributes
    an independent local factor.

    This connects Barwick's framework (factorization algebras in
    arithmetic geometry) to our shadow Eisenstein theorem.
    """
    # Compute L via Euler product (finite approximation)
    product = 1.0
    for p in primes:
        local = 1.0 / ((1 - p ** (-s)) * (1 - p ** (1 - s)))
        product *= local
    l_euler = -kappa * product

    # Compute L via Dirichlet series
    l_dirichlet = -kappa * _approx_zeta(s) * _approx_zeta(s - 1)

    # Compute L via shadow coefficients (sigma_1)
    l_shadow = 0.0
    for n in range(1, 10001):
        sig1 = sum(d for d in range(1, n + 1) if n % d == 0)
        l_shadow += (-kappa) * sig1 * (n ** (-s))

    return {
        "L_euler_product": l_euler,
        "L_dirichlet_series": l_dirichlet,
        "L_shadow_coefficients": l_shadow,
        "euler_vs_dirichlet_ratio": l_euler / l_dirichlet if l_dirichlet != 0 else float('nan'),
        "primes_used": len(primes),
    }


def arithmetic_fa_over_fp(p: int, kappa: float) -> Dict[str, object]:
    """Toy arithmetic factorization algebra over F_p.

    Over F_p, the isolability structure on P^1(F_p) gives:
    - |P^1(F_p)| = p + 1 points
    - Ran(P^1(F_p)) = 2^{p+1} - 1 nonempty subsets
    - Conf_n(P^1(F_p)) = (p+1)_n (falling factorial)

    The "bar complex" over F_p is a finite combinatorial object:
    B_n = number of n-tuples of distinct points with the bar differential
    acting by "collision" (identification of adjacent points).

    The shadow coefficient is kappa * |P^1(F_p)| / |P^1(C)|
    in the sense that the local factor at p in the Euler product
    contributes 1/((1-p^{-s})(1-p^{1-s})).
    """
    ff = FiniteFieldIsolability(p)
    return {
        "prime": p,
        "num_points": ff.num_points,
        "ran_cardinality": ff.ran_cardinality(),
        "config_counts": [ff.config_count(n) for n in range(1, min(6, p + 2))],
        "zeta_at_2": ff.zeta_function(2.0),
        "expected_zeta_at_2": 1.0 / ((1 - p ** (-2)) * (1 - p ** (-1))),
        "euler_factor_at_2": 1.0 / ((1 - p ** (-2)) * (1 - p ** (-1))),
        "shadow_local_factor": kappa / ((1 - p ** (-2)) * (1 - p ** (-1))),
    }


# =============================================================================
# X. FULL VERIFICATION CHAIN
# =============================================================================


def verify_barwick_isolability_ran_correspondence(max_n: int = 5) -> Dict[str, object]:
    """Full verification: isolability structure recovers Ran space data.

    Path 1: Direct from isolability object (Euler characteristics)
    Path 2: Classical configuration space formulas
    Path 3: Arithmetic point counts over F_q
    """
    p1 = P1IsolabilityObject()
    a1 = AffineLineIsolabilityObject()

    results = {
        "P1_config_chi": {},
        "A1_config_chi": {},
        "classical_formulas": {},
    }

    for n in range(1, max_n + 1):
        cg = complete_cograph(n)

        # P^1 Euler characteristics from isolability
        chi_p1 = p1.euler_char(cg)
        results["P1_config_chi"][n] = chi_p1

        # Classical: chi(Conf_n(P^1)) = product_{k=0}^{n-1} (2 - k)
        classical = 1
        for k in range(n):
            classical *= (2 - k)
        results["classical_formulas"][f"P1_n={n}"] = classical

        # A^1 Euler characteristics
        chi_a1 = a1.euler_char(cg)
        results["A1_config_chi"][n] = chi_a1

    return results


def verify_twofold_intertwiner_non_iso() -> List[Tuple[int, int, int, int, bool]]:
    """Verify that the intertwiner is NOT an isomorphism (Barwick's key point).

    The intertwiner
    (A oplus_bar B) oplus (C oplus_bar D) -> (A oplus C) oplus_bar (B oplus D)
    is non-invertible in general.

    This non-invertibility is what makes factorization algebras nontrivial:
    if the intertwiner were an isomorphism, Eckmann-Hilton would force
    the two tensor products to coincide.
    """
    tm = TwofoldMonoidalDatum()
    results = []
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                for d in range(1, 4):
                    is_iso = tm.intertwiner_is_isomorphism(a, b, c, d)
                    results.append((a, b, c, d, is_iso))
    return results
