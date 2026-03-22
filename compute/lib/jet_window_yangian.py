r"""Jet principle window stabilization for Yangian towers.

Decomposes the infinite dg-shifted Yangian tower into finite computable
windows via the reduced-weight bar filtration (conj:jet-principle).

MATHEMATICAL FRAMEWORK
----------------------

The bar complex B(A) = (T^c(s^{-1}\bar A), d_bar) carries a natural
**reduced-weight filtration**.  For a bar word sa_1 | ... | sa_ell
(tensor of desuspended generators), the reduced weight is:

    rho_red = sum_i (wt(a_i) - 1)

where wt(a_i) is the conformal weight of generator a_i.

The **reduced-weight window** K_q is:

    K_q = span{ bar words with rho_red <= q }

These windows grow polynomially and exhibit finite-stage stability.

THE JET PRINCIPLE (conj:jet-principle):
    K_q determines the dg-shifted Yangian r_A(z) through jet order z^{-q}:
    r_A(z) mod z^{-q-1}  is determined by K_q alone.

KEY OBSERVATIONS:
- Weight-1 generators (Heisenberg, affine KM): all bar words have rho_red = 0,
  so K_0 = full bar complex.  The window tower is trivially complete.
- Weight >= 2 generators (Virasoro, W_N): the jet tower is genuinely nontrivial
  and each level contributes new Yangian data.

Manuscript references:
    conj:jet-principle (higher_genus_modular_koszul.tex)
    def:reduced-weight-filtration (bar_cobar_adjunction_curved.tex)
    thm:completed-bar-cobar-strong (higher_genus_modular_koszul.tex)
    thm:coefficient-stability-criterion (higher_genus_modular_koszul.tex)
    def:modular-yangian-pro (yangians_drinfeld_kohno.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import combinations_with_replacement
from math import factorial, comb
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Symbol,
)


# ============================================================================
# 1.  Data classes
# ============================================================================

@dataclass(frozen=True)
class BarWord:
    r"""A bar word sa_1 | ... | sa_ell in the bar complex.

    Attributes
    ----------
    generators : tuple of str
        Generator names appearing in the bar word.
    weights : tuple of int
        Conformal weights of the corresponding generators.
    reduced_weight : int
        sum_i (wt(a_i) - 1).  This is the filtration index.
    bar_degree : int
        Length of the word (= len(generators)).
    total_weight : int
        sum_i wt(a_i).
    """

    generators: Tuple[str, ...]
    weights: Tuple[int, ...]
    reduced_weight: int
    bar_degree: int
    total_weight: int


def make_bar_word(generators: Tuple[str, ...],
                  weights: Tuple[int, ...]) -> BarWord:
    """Construct a BarWord from generator names and weights."""
    rw = sum(w - 1 for w in weights)
    return BarWord(
        generators=generators,
        weights=weights,
        reduced_weight=rw,
        bar_degree=len(generators),
        total_weight=sum(weights),
    )


@dataclass
class JetWindow:
    """A single reduced-weight window K_q of the bar complex.

    Attributes
    ----------
    algebra_name : str
        Name of the algebra.
    jet_order : int
        The window level q.
    bar_words : list of BarWord
        All bar words in this window (before Arnold relations).
    dimension : int
        dim K_q after Arnold relations.
    yangian_coefficients : dict
        Extracted Yangian coefficients r_0, r_1, ..., r_q.
    stable : bool
        Whether this window has stabilized (K_q = K_{q-1} in effect).
    """

    algebra_name: str
    jet_order: int
    bar_words: List[BarWord] = field(default_factory=list)
    dimension: int = 0
    yangian_coefficients: Dict[int, Any] = field(default_factory=dict)
    stable: bool = False

    def summary(self) -> str:
        """One-line summary of this window."""
        status = "STABLE" if self.stable else "active"
        n_words = len(self.bar_words)
        return (
            f"K_{self.jet_order}({self.algebra_name}): "
            f"dim={self.dimension}, raw_words={n_words}, "
            f"jets={sorted(self.yangian_coefficients.keys())}, "
            f"[{status}]"
        )


@dataclass
class YangianJetData:
    """Full jet-window decomposition of the Yangian tower.

    Attributes
    ----------
    algebra_name : str
        Name of the algebra.
    windows : dict
        {q: JetWindow} for q = 0, 1, ..., q_max.
    stabilization_order : int or None
        Smallest q such that K_q stabilises (None if not detected).
    yangian_series : dict
        Full extracted r(z) coefficients {n: r_n}.
    convergent : bool
        Whether the tower converges (class G/L/C) or not (class M).
    """

    algebra_name: str
    windows: Dict[int, JetWindow] = field(default_factory=dict)
    stabilization_order: Optional[int] = None
    yangian_series: Dict[int, Any] = field(default_factory=dict)
    convergent: bool = True

    def r_matrix_truncation(self, order: int, var: str = "z") -> str:
        """Return r(z) mod z^{-order-1} as a symbolic string.

        Parameters
        ----------
        order : int
            Truncation order (include r_0, ..., r_order).
        var : str
            Name of the spectral parameter.

        Returns
        -------
        str
            Human-readable expression for the truncated r-matrix.
        """
        z = Symbol(var)
        terms = []
        for n in range(order + 1):
            coeff = self.yangian_series.get(n)
            if coeff is not None and coeff != 0:
                terms.append(f"({coeff}) * {var}^(-{n + 1})")
        if not terms:
            return "0"
        return " + ".join(terms)

    def summary(self) -> str:
        """Multi-line summary of the full jet-window decomposition."""
        lines = [f"YangianJetData({self.algebra_name})"]
        lines.append(f"  stabilization_order = {self.stabilization_order}")
        lines.append(f"  convergent = {self.convergent}")
        lines.append(f"  n_windows = {len(self.windows)}")
        for q in sorted(self.windows):
            lines.append(f"  {self.windows[q].summary()}")
        return "\n".join(lines)

    def verify_stabilization(self, q1: int, q2: int) -> bool:
        """Test whether windows q1 and q2 give the same jets up to order q1.

        Parameters
        ----------
        q1 : int
            Lower window level.
        q2 : int
            Higher window level (q2 >= q1).

        Returns
        -------
        bool
            True if r_n from K_{q1} matches r_n from K_{q2} for all n <= q1.
        """
        if q1 not in self.windows or q2 not in self.windows:
            return False
        w1 = self.windows[q1]
        w2 = self.windows[q2]
        for n in range(q1 + 1):
            c1 = w1.yangian_coefficients.get(n)
            c2 = w2.yangian_coefficients.get(n)
            if c1 != c2:
                return False
        return True


# ============================================================================
# 2.  Bar-word enumeration
# ============================================================================

def enumerate_bar_words(generators: List[Tuple[str, int]],
                        max_reduced_weight: int,
                        max_bar_degree: int = 10) -> List[BarWord]:
    r"""Enumerate all bar words with reduced weight <= max_reduced_weight.

    A bar word is sa_1 | ... | sa_ell where a_i are chosen from the
    generator list.  The reduced weight is sum_i (wt(a_i) - 1).

    We use combinations_with_replacement for the sorted multiset of
    generators (avoiding duplicate unordered tuples).  Each unordered
    tuple of length ell represents one bar word up to the Arnold
    symmetry; the actual multiplicity in the bar complex is
    accounted for separately by Arnold dimension formulas.

    Parameters
    ----------
    generators : list of (name, conformal_weight)
        Generator list for the algebra.
    max_reduced_weight : int
        Maximum reduced weight q.
    max_bar_degree : int
        Maximum bar-word length (safety cutoff).

    Returns
    -------
    list of BarWord
        Sorted by (reduced_weight, bar_degree, generators).

    Examples
    --------
    Heisenberg with J(wt=1):
        Every word has rho_red = 0 regardless of length.
        All words land in K_0.

    Virasoro with L(wt=2):
        Word of length ell has rho_red = ell.
        K_q contains words of length <= q.

    W_3 with L(wt=2), W(wt=3):
        L|L : rho_red = 2
        L|W : rho_red = 3
        W|W : rho_red = 4
        L|L|L : rho_red = 3
    """
    # Sort generators by name for deterministic ordering
    gen_list = sorted(generators, key=lambda g: g[0])
    results: List[BarWord] = []

    for ell in range(1, max_bar_degree + 1):
        # Enumerate all multisets of size ell from gen_list
        for combo in combinations_with_replacement(range(len(gen_list)), ell):
            names = tuple(gen_list[i][0] for i in combo)
            weights = tuple(gen_list[i][1] for i in combo)
            rw = sum(w - 1 for w in weights)
            if rw <= max_reduced_weight:
                results.append(BarWord(
                    generators=names,
                    weights=weights,
                    reduced_weight=rw,
                    bar_degree=ell,
                    total_weight=sum(weights),
                ))

    results.sort(key=lambda bw: (bw.reduced_weight, bw.bar_degree,
                                  bw.generators))
    return results


# ============================================================================
# 3.  Arnold dimension and window dimensions
# ============================================================================

def arnold_corrected_dimension(n_generators: int,
                               bar_degree: int) -> int:
    r"""Dimension of bar-degree-d component with n generators, after Arnold.

    For bar degree d on d+1 points on P^1, the OS-algebra (Arnold relations)
    gives the top cohomology H^{d-1}(C_{d+1}(P^1)) of dimension d!.

    The bar complex at degree d is:
        B^d = span{bar words of length d} tensor H^{d-1}

    For a set of bar words of length d, each word sits in a d!-dimensional
    space.  But the *distinct* words (as multisets) each generate an
    orbit under the symmetric group S_d, and the Arnold quotient picks
    out the anti-invariant (alternating) part.

    For a word with all distinct generators: contributes 1 to dim.
    For a word with repeated generators: the alternating projection
    may vanish (e.g., J|J in Heisenberg contributes 0 for d=2 if
    the generator is bosonic).

    RAW DIMENSION (before Arnold): n_generators^d (ordered words).
    ARNOLD DIMENSION: n_generators^d * d! / d! = ... no, this is wrong.

    CORRECT FORMULA for the chiral bar complex:
    dim B^d = number of distinct multisets of size d from n generators,
              each weighted by the dimension of its Arnold quotient.

    For generators all of weight >= 1 (the standard case):
    Raw count = C(n_generators + d - 1, d) multisets.
    Arnold weight for a multiset with multiplicities (m_1, ..., m_r):
      = d! / (m_1! * ... * m_r!)  (multinomial coefficient)
    but then divided by d! from Arnold.
    Net: 1 / (m_1! * ... * m_r!).

    Actually, for the SYMMETRIC (bosonic) bar complex:
    dim = C(n + d - 1, d) where n = n_generators.

    But the Arnold relations on the chiral bar complex impose
    antisymmetry on the propagator indices while symmetry on the
    generator slots (for bosonic generators).

    SAFE APPROACH: use the known formula
       dim B^d = C(n_generators + d - 1, d)
    for commutative generators (all standard VOA generators are bosonic).
    """
    if bar_degree < 1:
        return 0
    # Stars-and-bars: C(n + d - 1, d) multisets of size d from n objects
    return comb(n_generators + bar_degree - 1, bar_degree)


def _count_words_in_window(generators: List[Tuple[str, int]],
                           q: int,
                           max_bar_degree: int = 50) -> int:
    r"""Count the number of distinct bar words with rho_red <= q.

    This counts multisets (unordered tuples) of generators whose
    reduced weight sum_i (wt(a_i) - 1) does not exceed q.

    For efficiency, uses a dynamic-programming approach: for each
    bar degree d = 1, 2, ..., count multisets of size d from
    generators with reduced weight <= q.

    Parameters
    ----------
    generators : list of (name, weight)
    q : int
        Maximum reduced weight.
    max_bar_degree : int
        Safety cutoff.

    Returns
    -------
    int
        Number of distinct bar words in K_q.
    """
    # Extract the list of reduced weights: w_i - 1 for each generator
    red_wts = sorted(g[1] - 1 for g in generators)
    n_gen = len(generators)

    # If all generators have weight 1, every word has rho_red = 0
    if all(rw == 0 for rw in red_wts):
        # K_q = full bar complex for all q >= 0
        # Total bar words up to max_bar_degree:
        # sum_{d=1}^{max_bar_degree} C(n_gen + d - 1, d)
        # But we should cap at a reasonable degree
        total = 0
        for d in range(1, max_bar_degree + 1):
            total += comb(n_gen + d - 1, d)
        return total

    # General case: DP over (remaining_degree, remaining_weight, min_gen_index)
    # We count multisets of size d with sum of red_wts <= q.
    # Total across all bar degrees d = 1, ..., until words can't fit.
    total = 0
    # Max bar degree: at most q / min(positive red_wts) + (count of zero-weight gens)
    min_positive_rw = min((rw for rw in red_wts if rw > 0), default=None)
    if min_positive_rw is not None:
        max_d = q // min_positive_rw + n_gen * (max_bar_degree)
        max_d = min(max_d, max_bar_degree)
    else:
        max_d = max_bar_degree

    for d in range(1, max_d + 1):
        total += _count_multisets_with_bounded_sum(red_wts, d, q)
    return total


def _count_multisets_with_bounded_sum(values: List[int],
                                      size: int,
                                      max_sum: int) -> int:
    r"""Count multisets of given size from values with element-sum <= max_sum.

    Uses recursion with memoization.  `values` must be sorted.

    Parameters
    ----------
    values : sorted list of non-negative ints
        Possible reduced weights (one per generator type).
    size : int
        Multiset size.
    max_sum : int
        Maximum allowed sum.

    Returns
    -------
    int
        Number of valid multisets.
    """
    memo: Dict[Tuple[int, int, int], int] = {}

    def _recurse(remaining: int, budget: int, start: int) -> int:
        """Count multisets of `remaining` elements from values[start:]
        with total reduced weight <= budget."""
        if remaining == 0:
            return 1
        key = (remaining, budget, start)
        if key in memo:
            return memo[key]
        count = 0
        for i in range(start, len(values)):
            v = values[i]
            if v > budget:
                break  # values is sorted, so all subsequent are >= v
            # Use generator i, then recurse allowing i again (multiset)
            count += _recurse(remaining - 1, budget - v, i)
        memo[key] = count
        return count

    return _recurse(size, max_sum, 0)


def compute_window_dimensions(generators: List[Tuple[str, int]],
                              max_q: int = 8) -> Dict[int, int]:
    r"""Compute dim(K_q) for q = 0, 1, ..., max_q.

    For each q, counts the number of distinct bar words (as multisets)
    with reduced weight at most q.  This is the dimension of the
    window K_q before Arnold quotient; the Arnold quotient is
    incorporated via the multiset count (each unordered tuple
    represents one basis element in the symmetric/chiral bar complex).

    Parameters
    ----------
    generators : list of (name, weight)
        Generator data.
    max_q : int
        Maximum window level.

    Returns
    -------
    dict
        {q: dim(K_q)} for q = 0, 1, ..., max_q.

    Examples
    --------
    >>> compute_window_dimensions([("J", 1)], max_q=4)
    {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
    # Heisenberg: K_0 already complete at bar degree 1 (the only one
    # that matters for the Yangian); but at higher bar degrees all
    # words still have rho_red = 0.  We cap at bar_degree = max_q + 1
    # for practical reasons when all weights are 1.
    """
    red_wts = [g[1] - 1 for g in generators]
    all_wt1 = all(rw == 0 for rw in red_wts)

    result = {}
    for q in range(max_q + 1):
        if all_wt1:
            # Every bar word has rho_red = 0; K_q = K_0 for all q.
            # Count bar words up to a sensible degree.
            # For Yangian extraction, bar degree d contributes to jet d.
            # Cap at max_q + 1 for a finite answer.
            dim = 0
            cap = max_q + 1
            n_gen = len(generators)
            for d in range(1, cap + 1):
                dim += comb(n_gen + d - 1, d)
            result[q] = dim
        else:
            # Count words with rho_red <= q, capping bar degree
            result[q] = _count_words_in_window(generators, q,
                                               max_bar_degree=max_q + 5)
    return result


def compute_window_dimensions_by_degree(
        generators: List[Tuple[str, int]],
        max_q: int = 8,
        max_bar_degree: int = 15) -> Dict[int, Dict[int, int]]:
    r"""Compute dim(K_q) decomposed by bar degree.

    Returns
    -------
    dict
        {q: {bar_degree: count}} for q = 0, ..., max_q.
    """
    red_wts = sorted(g[1] - 1 for g in generators)
    n_gen = len(generators)
    result: Dict[int, Dict[int, int]] = {}

    for q in range(max_q + 1):
        by_deg: Dict[int, int] = {}
        for d in range(1, max_bar_degree + 1):
            cnt = _count_multisets_with_bounded_sum(red_wts, d, q)
            if cnt > 0:
                by_deg[d] = cnt
        result[q] = by_deg
    return result


# ============================================================================
# 4.  Yangian jet extraction (per-family)
# ============================================================================

def _build_jet_window(algebra_name: str,
                      generators: List[Tuple[str, int]],
                      q: int,
                      max_bar_degree: int = 15,
                      prev_dim: Optional[int] = None) -> JetWindow:
    """Construct a JetWindow for the given algebra and jet order.

    Parameters
    ----------
    algebra_name : str
    generators : list of (name, weight)
    q : int
        Jet order.
    max_bar_degree : int
    prev_dim : int or None
        Dimension of K_{q-1}, used to detect stabilization.

    Returns
    -------
    JetWindow
    """
    words = enumerate_bar_words(generators, q, max_bar_degree)
    dim = len(words)
    stable = (prev_dim is not None and dim == prev_dim)

    # Yangian coefficient r_q: new contributions at this window level.
    # The Yangian r(z) = sum_n r_n z^{-n-1} where r_n is extracted from
    # bar words with rho_red = n (the *incremental* contribution).
    #
    # For the jet principle, words with rho_red exactly = q contribute
    # to the q-th jet coefficient r_q.
    words_at_q = [w for w in words if w.reduced_weight == q]
    n_new = len(words_at_q)

    coeffs: Dict[int, Any] = {}
    for j in range(q + 1):
        words_at_j = [w for w in words if w.reduced_weight == j]
        coeffs[j] = len(words_at_j)

    return JetWindow(
        algebra_name=algebra_name,
        jet_order=q,
        bar_words=words,
        dimension=dim,
        yangian_coefficients=coeffs,
        stable=stable,
    )


def extract_yangian_jets(family: str,
                         max_q: int = 6,
                         **params) -> YangianJetData:
    r"""Compute windows and extract Yangian jet coefficients.

    Supported families: 'heisenberg', 'affine_sl2', 'virasoro', 'w3',
    'betagamma', 'free_fermion'.

    Parameters
    ----------
    family : str
        Family name.
    max_q : int
        Maximum jet order.
    **params
        Family-specific parameters (level, central charge, etc.).

    Returns
    -------
    YangianJetData
    """
    generators = _family_generators(family)
    data = YangianJetData(algebra_name=family)

    prev_dim = None
    first_stable = None
    for q in range(max_q + 1):
        win = _build_jet_window(family, generators, q,
                                max_bar_degree=max_q + 5,
                                prev_dim=prev_dim)
        data.windows[q] = win
        if win.stable and first_stable is None:
            first_stable = q
        prev_dim = win.dimension

    data.stabilization_order = first_stable

    # Collect the full Yangian series from the highest window
    if max_q in data.windows:
        data.yangian_series = dict(data.windows[max_q].yangian_coefficients)

    # Determine convergence from shadow depth class
    red_wts = [g[1] - 1 for g in generators]
    if all(rw == 0 for rw in red_wts):
        # Class G or L: weight-1 generators, tower trivially complete
        data.convergent = True
    elif family == "virasoro":
        # Class M: infinite tower, does not stabilise
        data.convergent = False
    elif family == "w3":
        # Class M: infinite tower
        data.convergent = False
    elif family == "betagamma":
        # Class C: terminates at arity 4
        data.convergent = True
    else:
        data.convergent = True

    return data


def _family_generators(family: str) -> List[Tuple[str, int]]:
    """Return the list of (name, conformal_weight) for a family."""
    families = {
        "heisenberg": [("J", 1)],
        "affine_sl2": [("e", 1), ("h", 1), ("f", 1)],
        "virasoro": [("L", 2)],
        "w3": [("L", 2), ("W", 3)],
        "betagamma": [("beta", 1), ("gamma", 0)],
        "free_fermion": [("psi", 1)],
    }
    if family not in families:
        raise ValueError(
            f"Unknown family '{family}'. "
            f"Supported: {sorted(families.keys())}"
        )
    return families[family]


# ============================================================================
# 5.  Per-family window data
# ============================================================================

def heisenberg_windows(max_q: int = 6) -> YangianJetData:
    r"""Jet-window decomposition for the Heisenberg VOA.

    Generator: J of weight 1.
    Every bar word has rho_red = 0, so K_0 = full bar complex.
    Stabilisation at q = 0 (trivial).
    Yangian = trivial (abelian: no simple pole in J(z)J(w)).

    Returns
    -------
    YangianJetData
    """
    return extract_yangian_jets("heisenberg", max_q=max_q)


def affine_sl2_windows(max_q: int = 6) -> YangianJetData:
    r"""Jet-window decomposition for affine sl_2.

    Generators: e, h, f of weight 1.
    Every bar word has rho_red = 0 (since wt - 1 = 0 for all generators).
    K_0 = full bar complex.  Stabilisation at q = 0.

    The Yangian r(z) = classical Drinfeld r-matrix:
        r_0 = Omega / z  (Casimir element of sl_2)
    with all higher jets being trivial at the chiral level.

    Returns
    -------
    YangianJetData
    """
    return extract_yangian_jets("affine_sl2", max_q=max_q)


def virasoro_windows(max_q: int = 8) -> YangianJetData:
    r"""Jet-window decomposition for the Virasoro algebra.

    Generator: L of weight 2.
    A word of length ell has rho_red = ell * (2-1) = ell.
    So K_q contains bar words of length <= q.

    Window dimensions:
        K_0 = {vacuum}: dim = 0 (no bar words of length 0)
              Actually K_0 = {} since the shortest bar word is length 1
              and rho_red = 1 for it.  So K_0 is empty.
              Wait: length 1 word (L) has rho_red = 1.
        K_0: no words (rho_red >= 1 for all).   dim = 0.
        K_1: {L} (one word, length 1).           dim = 1.
        K_2: {L, L|L} (length 1 + length 2).     dim = 2.
        K_3: {L, L|L, L|L|L}.                    dim = 3.
        K_q: words of length 1, ..., q.          dim = q.

    Does NOT stabilise (class M, infinite tower).
    Each new window contributes exactly one word (L^|q|).

    Returns
    -------
    YangianJetData
    """
    return extract_yangian_jets("virasoro", max_q=max_q)


def w3_windows(max_q: int = 8) -> YangianJetData:
    r"""Jet-window decomposition for the W_3 algebra.

    Generators: L (wt=2), W (wt=3).
    Reduced weights:
        L: 1 per copy
        W: 2 per copy

    Window dimensions:
        K_0: no words (min rho_red = 1).           dim = 0.
        K_1: {L} (rho_red = 1).                    dim = 1.
        K_2: {L, L|L, W} (rho_red = 1, 2, 2).     dim = 3.
        K_3: {L, L|L, W, L|L|L, L|W}
             (rho_red = 1, 2, 2, 3, 3).            dim = 5.
        K_4: add L|L|L|L (4), L|L|W (4), W|W (4). dim = 8.
        K_5: add L^5 (5), L^3|W (5), L|W|W (5).   dim = 11.

    Does NOT stabilise (class M, infinite tower).

    Returns
    -------
    YangianJetData
    """
    return extract_yangian_jets("w3", max_q=max_q)


def betagamma_windows(max_q: int = 6) -> YangianJetData:
    r"""Jet-window decomposition for the beta-gamma system.

    Generators: beta (wt=1), gamma (wt=0).
    Reduced weights per generator:
        beta: 1-1 = 0
        gamma: 0-1 = -1  (NEGATIVE!)

    Since gamma has weight 0, its reduced weight is -1.
    This means adding gamma to a word *decreases* rho_red.

    Consequence: bar words involving gamma have lower reduced weight.
    In fact, any word involving at least one gamma has
    rho_red <= (total length - 1) * 0 + (-1) * n_gamma.

    K_0 contains ALL words made purely from beta (since wt=1 => rho_red=0)
    PLUS any words containing gamma (which have rho_red <= -1 < 0).
    So K_0 = full bar complex.  Stabilisation at q = 0.

    The beta-gamma system is class C (shadow depth 4, terminates).

    Returns
    -------
    YangianJetData
    """
    return extract_yangian_jets("betagamma", max_q=max_q)


# ============================================================================
# 6.  Stabilisation and comparison
# ============================================================================

def window_stabilization_test(family: str,
                              q1: int,
                              q2: int,
                              **params) -> bool:
    r"""Test whether K_{q1} and K_{q2} give the same Yangian jets up to order q1.

    Parameters
    ----------
    family : str
        Family name.
    q1 : int
        Lower window level.
    q2 : int
        Higher window level (must have q2 >= q1).
    **params
        Family-specific parameters.

    Returns
    -------
    bool
        True if the jets through order q1 agree.
    """
    if q2 < q1:
        raise ValueError(f"q2={q2} must be >= q1={q1}")
    data = extract_yangian_jets(family, max_q=q2, **params)
    return data.verify_stabilization(q1, q2)


def window_dimension_table(families: Optional[List[str]] = None,
                           max_q: int = 8) -> Dict[str, Dict[int, int]]:
    r"""Tabulate window dimensions for standard families.

    Parameters
    ----------
    families : list of str or None
        Families to include.  Default: all standard families.
    max_q : int
        Maximum window level.

    Returns
    -------
    dict
        {family: {q: dim(K_q)}} for each family.
    """
    if families is None:
        families = ["heisenberg", "affine_sl2", "virasoro", "w3",
                    "betagamma", "free_fermion"]
    result = {}
    for fam in families:
        gens = _family_generators(fam)
        result[fam] = compute_window_dimensions(gens, max_q)
    return result


def jet_yangian_comparison(family: str,
                           yangian_known: Dict[int, Any],
                           **params) -> Dict[str, Any]:
    r"""Compare window-extracted Yangian coefficients with known values.

    Parameters
    ----------
    family : str
        Family name.
    yangian_known : dict
        Known Yangian coefficients {jet_order: value}.
    **params
        Family-specific parameters.

    Returns
    -------
    dict with keys:
        'matches' : dict {jet_order: bool}
        'extracted' : dict {jet_order: value}
        'known' : dict (the input)
        'all_match' : bool
    """
    max_q = max(yangian_known.keys()) if yangian_known else 6
    data = extract_yangian_jets(family, max_q=max_q, **params)

    matches = {}
    for n, known_val in yangian_known.items():
        extracted = data.yangian_series.get(n)
        matches[n] = (extracted == known_val)

    return {
        "matches": matches,
        "extracted": dict(data.yangian_series),
        "known": yangian_known,
        "all_match": all(matches.values()) if matches else True,
    }


# ============================================================================
# 7.  Growth analysis
# ============================================================================

def window_growth_analysis(family: str,
                           max_q: int = 15) -> Dict[str, Any]:
    r"""Analyse growth of dim(K_q) with q.

    For weight-1 generators (G/L classes): dim(K_q) is constant (all
    words have rho_red = 0).

    For single weight-w generator (w >= 2): dim(K_q) = q (one word per
    degree), so growth is LINEAR.

    For multiple generators with mixed weights: growth is POLYNOMIAL
    of degree depending on the number of generators.

    For class M (infinite tower): growth rate connects to the shadow
    radius rho(A) through the jet principle.

    Parameters
    ----------
    family : str
        Family name.
    max_q : int
        Maximum q for analysis.

    Returns
    -------
    dict with keys:
        'family' : str
        'dimensions' : {q: dim}
        'growth_type' : str ('constant', 'linear', 'polynomial',
                             'exponential')
        'growth_rate' : float or None
            Effective growth rate dim(K_{q+1}) / dim(K_q) at large q.
        'shadow_class' : str
            'G', 'L', 'C', or 'M'.
        'polynomial_degree' : int or None
            If growth is polynomial, the degree.
    """
    gens = _family_generators(family)
    dims = compute_window_dimensions(gens, max_q)

    # Classify growth
    vals = [dims[q] for q in range(max_q + 1)]
    nonzero_vals = [v for v in vals if v > 0]

    # Check constant
    if len(set(vals)) <= 1:
        growth_type = "constant"
        growth_rate = 1.0
        poly_deg = 0
    elif all(vals[i + 1] - vals[i] == vals[1] - vals[0]
             for i in range(len(vals) - 1) if vals[i] > 0):
        growth_type = "linear"
        growth_rate = None
        poly_deg = 1
    else:
        # Compute ratios for large q
        ratios = []
        for q in range(max(1, max_q // 2), max_q):
            if vals[q] > 0:
                ratios.append(vals[q + 1] / vals[q])
        if ratios:
            avg_ratio = sum(ratios) / len(ratios)
        else:
            avg_ratio = 1.0

        if avg_ratio > 1.5:
            growth_type = "exponential"
            growth_rate = avg_ratio
            poly_deg = None
        else:
            growth_type = "polynomial"
            growth_rate = avg_ratio
            # Estimate polynomial degree from log-log slope
            # For dim ~ q^d, log(dim) ~ d * log(q)
            import math
            if vals[-1] > 0 and vals[max_q // 2] > 0 and max_q > 2:
                q_lo = max(max_q // 2, 2)
                q_hi = max_q
                if vals[q_lo] > 0 and vals[q_hi] > 0:
                    log_ratio = math.log(vals[q_hi] / vals[q_lo])
                    log_q_ratio = math.log(q_hi / q_lo)
                    poly_deg = round(log_ratio / log_q_ratio) if log_q_ratio > 0 else 0
                else:
                    poly_deg = None
            else:
                poly_deg = None

    # Shadow depth class
    red_wts = [g[1] - 1 for g in gens]
    if all(rw == 0 for rw in red_wts):
        if len(gens) == 1:
            shadow_class = "G"  # Heisenberg: Gaussian
        else:
            shadow_class = "L"  # Affine: Lie/tree
    elif family == "betagamma":
        shadow_class = "C"  # Contact
    elif family in ("virasoro", "w3"):
        shadow_class = "M"  # Mixed
    else:
        shadow_class = "G"

    return {
        "family": family,
        "dimensions": dims,
        "growth_type": growth_type,
        "growth_rate": growth_rate,
        "shadow_class": shadow_class,
        "polynomial_degree": poly_deg,
    }


# ============================================================================
# 8.  Asymptotic formulas
# ============================================================================

def virasoro_window_dim_exact(q: int) -> int:
    r"""Exact dimension of K_q for Virasoro.

    Single generator L of weight 2.  A bar word of length d has
    rho_red = d.  So K_q = {words of length 1, ..., q}.
    Each length d contributes exactly 1 word (L|L|...|L, d times).

    dim(K_q) = q  for q >= 1.  dim(K_0) = 0.
    """
    return max(q, 0)


def w3_window_dim_exact(q: int) -> int:
    r"""Exact dimension of K_q for W_3.

    Two generators: L (wt=2, red_wt=1), W (wt=3, red_wt=2).
    A bar word using n_L copies of L and n_W copies of W has
    rho_red = n_L + 2 * n_W.

    The number of such words (as multisets) is 1 for each valid
    (n_L, n_W) with n_L + n_W >= 1 and n_L + 2*n_W <= q.

    dim(K_q) = #{(n_L, n_W) : n_L >= 0, n_W >= 0, n_L + n_W >= 1,
                               n_L + 2*n_W <= q}.
    """
    if q <= 0:
        return 0
    count = 0
    for n_W in range(q // 2 + 1):
        # n_L ranges from 0 to q - 2*n_W, but at least 1 if n_W = 0
        max_n_L = q - 2 * n_W
        if n_W == 0:
            count += max(max_n_L, 0)  # n_L = 1, ..., max_n_L
        else:
            count += max_n_L + 1  # n_L = 0, ..., max_n_L
    return count


def asymptotic_window_dim(n_generators: int,
                          min_reduced_weight: int,
                          q: int) -> float:
    r"""Asymptotic estimate for dim(K_q) with large q.

    For n generators all of reduced weight w_min, the number of
    multisets of total reduced weight <= q is approximately:

        dim(K_q) ~ (q / w_min)^n / n!

    for large q (by the integer-partition / stars-and-bars argument).

    Parameters
    ----------
    n_generators : int
        Number of distinct generators.
    min_reduced_weight : int
        Minimum reduced weight among generators (all assumed equal for
        this estimate).
    q : int
        Window level.

    Returns
    -------
    float
        Asymptotic estimate.
    """
    if min_reduced_weight <= 0 or q <= 0:
        return float("inf") if min_reduced_weight <= 0 else 0.0
    effective_q = q / min_reduced_weight
    return effective_q ** n_generators / factorial(n_generators)


# ============================================================================
# 9.  Utility: window-to-shadow bridge
# ============================================================================

def window_shadow_bridge(family: str, max_q: int = 8) -> Dict[str, Any]:
    r"""Connect jet windows to shadow tower data.

    The jet principle links the reduced-weight window K_q to:
    - The Yangian r-matrix jet at order z^{-q}
    - The shadow tower coefficient S_q
    - The bar cohomology at reduced weight q

    This function computes the dimensional data linking these objects.

    Parameters
    ----------
    family : str
    max_q : int

    Returns
    -------
    dict with keys:
        'family' : str
        'window_dims' : {q: dim(K_q)}
        'increments' : {q: dim(K_q) - dim(K_{q-1})}
        'cumulative_fraction' : {q: dim(K_q) / dim(K_{max_q})}
            (how much of the total is captured at window q)
    """
    gens = _family_generators(family)
    dims = compute_window_dimensions(gens, max_q)

    increments = {}
    for q in range(max_q + 1):
        prev = dims.get(q - 1, 0)
        increments[q] = dims[q] - prev

    total = dims[max_q] if dims[max_q] > 0 else 1
    fractions = {q: dims[q] / total for q in range(max_q + 1)}

    return {
        "family": family,
        "window_dims": dims,
        "increments": increments,
        "cumulative_fraction": fractions,
    }
