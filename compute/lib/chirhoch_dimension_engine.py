r"""Family-indexed dimension audit for chiral Hochschild cohomology.

The module computes Lie-theoretic arithmetic and records the two bounded
vertex-cohomology results of Bakalov--De Sole--Kac.  Curve-level chart
dimensions arise only after a family support datum ``H_H(A; S)`` or a named
bounded-to-chart quasi-isomorphism.

Bounded benchmarks:

* rank-one even superboson: ``(2, 1, 0, ...)``;
* Virasoro: support ``{0, 2, 3}``, with one-dimensional groups there.

The affine, beta-gamma, bc, principal-W, and lattice rows remain open at chart
level.  For affine algebras, ``dim(g)`` is exact zero-mode metadata.  It gives
the dimension of a known inner adjoint subspace and does not compute the full
outer-derivation quotient.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Dict, List, Mapping, Optional, Tuple


THEOREM_H_REQUIRED_COMPONENTS: Tuple[str, ...] = (
    "complete_chart_complex_Q_A",
    "chart_quasi_isomorphism_gamma_A",
    "support_model_K_A_S",
    "strong_deformation_retract_i_p_h",
    "incidence_and_bar_face_compatibility",
    "averaging_and_Mittag_Leffler_comparison",
)

BOUNDED_TO_CHART_OBLIGATION = (
    "construct the bounded-to-chart chain map and prove that it is a "
    "quasi-isomorphism on the completed curve-level cochain complex"
)


LIE_ALGEBRA_DIMS: Dict[str, int] = {
    "sl_2": 3,
    "sl_3": 8,
    "sl_4": 15,
    "sl_5": 24,
    "sl_6": 35,
    "so_3": 3,
    "so_5": 10,
    "so_6": 15,
    "so_7": 21,
    "so_8": 28,
    "so_9": 36,
    "so_10": 45,
    "so_12": 66,
    "sp_2": 3,
    "sp_4": 10,
    "sp_6": 21,
    "sp_8": 36,
    "G2": 14,
    "F4": 52,
    "E6": 78,
    "E7": 133,
    "E8": 248,
}

DUAL_COXETER_NUMBERS: Dict[str, int] = {
    "sl_2": 2,
    "sl_3": 3,
    "sl_4": 4,
    "sl_5": 5,
    "sl_6": 6,
    "so_5": 3,
    "so_7": 5,
    "so_8": 6,
    "so_9": 7,
    "so_10": 8,
    "so_12": 10,
    "sp_4": 3,
    "sp_6": 4,
    "sp_8": 5,
    "G2": 4,
    "F4": 9,
    "E6": 12,
    "E7": 18,
    "E8": 30,
}


def dim_simple_lie_algebra(name: str) -> int:
    """Return the exact dimension of a supported simple Lie algebra."""

    if name in LIE_ALGEBRA_DIMS:
        return LIE_ALGEBRA_DIMS[name]
    if name.startswith("sl_"):
        try:
            N = int(name[3:])
        except ValueError as exc:
            raise KeyError(f"unknown Lie algebra: {name}") from exc
        if N < 2:
            raise ValueError("sl_N requires N at least 2")
        return N * N - 1
    raise KeyError(f"unknown Lie algebra: {name}")


def rank_simple_lie_algebra(name: str) -> int:
    if name.startswith("sl_"):
        N = int(name[3:])
        if N < 2:
            raise ValueError("sl_N requires N at least 2")
        return N - 1
    rank_table = {
        "so_3": 1,
        "so_5": 2,
        "so_6": 3,
        "so_7": 3,
        "so_8": 4,
        "so_9": 4,
        "so_10": 5,
        "so_12": 6,
        "sp_2": 1,
        "sp_4": 2,
        "sp_6": 3,
        "sp_8": 4,
        "G2": 2,
        "F4": 4,
        "E6": 6,
        "E7": 7,
        "E8": 8,
    }
    if name in rank_table:
        return rank_table[name]
    raise KeyError(f"unknown Lie algebra for rank: {name}")


@dataclass(frozen=True)
class ChirHochData:
    """A family row separating bounded data from chart conclusions."""

    family: str
    bounded_support: Optional[Tuple[int, ...]]
    bounded_dimensions: Optional[Mapping[int, int]]
    bounded_status: str
    chart_support: Optional[Tuple[int, ...]]
    chart_dimensions: Optional[Mapping[int, int]]
    chart_status: str
    comparison_map: Optional[str]
    prequotient_dimension: Optional[int]
    known_inner_zero_mode_dimension: Optional[int]
    resolution_obligation: str
    family_parameter_status: str = "family parameter recorded separately from fixed-fibre cohomology"

    @property
    def dim0(self) -> Optional[int]:
        return None if self.chart_dimensions is None else self.chart_dimensions.get(0, 0)

    def bounded_dimension(self, degree: int) -> Optional[int]:
        if self.bounded_dimensions is None:
            return None
        return self.bounded_dimensions.get(degree, 0)

    def bounded_prefix(self, max_degree: int) -> Optional[Tuple[int, ...]]:
        if self.bounded_dimensions is None:
            return None
        if max_degree < 0:
            return ()
        return tuple(self.bounded_dimensions.get(n, 0) for n in range(max_degree + 1))

    @property
    def dim1(self) -> Optional[int]:
        return None if self.chart_dimensions is None else self.chart_dimensions.get(1, 0)

    @property
    def dim2(self) -> Optional[int]:
        return None if self.chart_dimensions is None else self.chart_dimensions.get(2, 0)

    @property
    def total(self) -> Optional[int]:
        return None if self.chart_dimensions is None else sum(self.chart_dimensions.values())

    @property
    def hilbert_triple(self) -> Optional[Tuple[int, int, int]]:
        if self.chart_dimensions is None:
            return None
        return (self.dim0, self.dim1, self.dim2)

    @property
    def poincare_poly(self) -> Optional[str]:
        if self.chart_dimensions is None:
            return None
        terms = []
        for degree in sorted(self.chart_dimensions):
            coefficient = self.chart_dimensions[degree]
            if degree == 0:
                terms.append(str(coefficient))
            elif degree == 1:
                terms.append(f"{coefficient}t")
            else:
                terms.append(f"{coefficient}t^{degree}")
        return " + ".join(terms)

    @property
    def concentrated_in_012(self) -> Optional[bool]:
        if self.chart_support is None:
            return None
        return set(self.chart_support).issubset({0, 1, 2})

    @property
    def cohomology_scope(self) -> str:
        return "completed curve-level chart" if self.chart_support else "open chart comparison"


def _row(
    family: str,
    *,
    bounded_support: Optional[Tuple[int, ...]] = None,
    bounded_dimensions: Optional[Mapping[int, int]] = None,
    bounded_status: str = "open-family-specific-bounded-complex",
    prequotient_dimension: Optional[int] = None,
    known_inner_zero_mode_dimension: Optional[int] = None,
) -> ChirHochData:
    return ChirHochData(
        family=family,
        bounded_support=bounded_support,
        bounded_dimensions=bounded_dimensions,
        bounded_status=bounded_status,
        chart_support=None,
        chart_dimensions=None,
        chart_status="open-family-support-datum",
        comparison_map=None,
        prequotient_dimension=prequotient_dimension,
        known_inner_zero_mode_dimension=known_inner_zero_mode_dimension,
        resolution_obligation=BOUNDED_TO_CHART_OBLIGATION,
    )


def chirhoch_heisenberg() -> ChirHochData:
    return _row(
        "rank-one even superboson / Heisenberg presentation",
        bounded_support=(0, 1),
        bounded_dimensions={0: 2, 1: 1},
        bounded_status="proved-bounded-BDSK-Theorem-7.4",
    )


def chirhoch_virasoro() -> ChirHochData:
    return _row(
        "Virasoro Vir_c",
        bounded_support=(0, 2, 3),
        bounded_dimensions={0: 1, 2: 1, 3: 1},
        bounded_status="proved-bounded-BDSK-Theorem-7.2",
    )


def chirhoch_affine_km(lie_algebra: str) -> ChirHochData:
    dim_g = dim_simple_lie_algebra(lie_algebra)
    return _row(
        f"Affine V_k({lie_algebra})",
        bounded_status="conjectural-BDSK-Conjecture-7.5-bound",
        prequotient_dimension=dim_g,
        known_inner_zero_mode_dimension=dim_g,
    )


def affine_bounded_upper_bound(lie_algebra: str, degree: int) -> int:
    r"""Return the numerical right side of BDSK Conjecture 7.5.

    The returned integer is
    ``dim Lambda^n(g) + dim Lambda^(n+1)(g)``.  Its role is a conjectural
    upper bound for bounded affine cohomology.
    """

    if degree < 0:
        return 0
    dim_g = dim_simple_lie_algebra(lie_algebra)
    first = comb(dim_g, degree) if degree <= dim_g else 0
    second = comb(dim_g, degree + 1) if degree + 1 <= dim_g else 0
    return first + second


def chirhoch_free_fermion_bc() -> ChirHochData:
    return _row("free fermion bc")


def chirhoch_free_betagamma() -> ChirHochData:
    return _row("free beta-gamma")


def chirhoch_w_algebra(N: int) -> ChirHochData:
    if not isinstance(N, int) or N < 2:
        raise ValueError("W_N requires integer N at least 2")
    if N == 2:
        row = chirhoch_virasoro()
        return ChirHochData(
            family="W_2 = Virasoro",
            bounded_support=row.bounded_support,
            bounded_dimensions=row.bounded_dimensions,
            bounded_status=row.bounded_status,
            chart_support=None,
            chart_dimensions=None,
            chart_status=row.chart_status,
            comparison_map=None,
            prequotient_dimension=None,
            known_inner_zero_mode_dimension=None,
            resolution_obligation=row.resolution_obligation,
        )
    return _row(f"principal W_{N}")


def chirhoch_lattice(rank: int) -> ChirHochData:
    if not isinstance(rank, int) or rank < 1:
        raise ValueError("lattice rank must be a positive integer")
    return _row(f"lattice vertex algebra of rank {rank}")


def chirhoch_dimensions(family: str, **params: object) -> ChirHochData:
    normalized = family.lower().replace("-", "_").replace(" ", "_")
    if normalized in {"heisenberg", "heis", "h_k"}:
        return chirhoch_heisenberg()
    if normalized in {"virasoro", "vir", "vir_c"}:
        return chirhoch_virasoro()
    if normalized in {"affine_km", "affine", "km", "kac_moody"}:
        lie_algebra = params.get("lie_algebra")
        if not isinstance(lie_algebra, str):
            raise ValueError("affine_km requires a lie_algebra string")
        return chirhoch_affine_km(lie_algebra)
    if normalized in {"bc", "free_fermion", "fermion", "free_fermion_bc"}:
        return chirhoch_free_fermion_bc()
    if normalized in {"betagamma", "bg", "free_betagamma", "free_boson_bg"}:
        return chirhoch_free_betagamma()
    if normalized in {"w_algebra", "w_n", "w"}:
        N = params.get("N")
        if not isinstance(N, int):
            raise ValueError("w_algebra requires integer N")
        return chirhoch_w_algebra(N)
    if normalized in {"lattice", "lattice_va"}:
        rank = params.get("rank")
        if not isinstance(rank, int):
            raise ValueError("lattice requires integer rank")
        return chirhoch_lattice(rank)
    raise KeyError(f"unknown family: {family}")


def all_standard_families() -> List[ChirHochData]:
    return [
        chirhoch_heisenberg(),
        chirhoch_virasoro(),
        chirhoch_affine_km("sl_2"),
        chirhoch_affine_km("sl_3"),
        chirhoch_free_fermion_bc(),
        chirhoch_free_betagamma(),
        chirhoch_w_algebra(3),
        chirhoch_lattice(1),
    ]


def theorem_h_scope_record(
    family: Optional[str] = None,
    applies: Optional[bool] = None,
    reason: Optional[str] = None,
) -> Dict[str, object]:
    """Return the family-indexed theorem and the supplied-data status."""

    return {
        "claim": "H_H(A;S) implies Supp ChirHoch(A) subset S",
        "type_signature": {
            "quadrant": "Open-Chain",
            "presentation": "completed curve-level chiral Hochschild cochains",
            "level": 3,
            "hypothesis_package": "family support datum H_H(A;S)",
        },
        "family": family,
        "applies": None,
        "status": "open-explicit-family-support-datum",
        "hypotheses": THEOREM_H_REQUIRED_COMPONENTS,
        "reason": reason,
        "legacy_applies_argument": applies,
    }


def old_theorem_h_bound_holds(data: ChirHochData) -> Optional[bool]:
    data.family
    return None


def theorem_h_concentration_holds(data: ChirHochData) -> Optional[bool]:
    return data.concentrated_in_012


def koszul_duality_check(
    data_a: ChirHochData, data_a_dual: ChirHochData
) -> Optional[bool]:
    data_a.family, data_a_dual.family
    return None


# ---------------------------------------------------------------------------
# First-principles finite-window checks for the rank-one Heisenberg row
# ---------------------------------------------------------------------------
#
# The bounded profile (2, 1, 0, ...) for the rank-one even superboson is
# ProvedElsewhere (BDSK Theorem 7.4); this module does not re-derive it.
# What CAN be computed here from first principles, in a finite mode window,
# are the two mechanisms that the profile rests on:
#
#   (H1 witness)  an outer derivation D: alpha_0 -> K exists -- it satisfies
#                 the derivation identity on every bracket in the window and
#                 is not of the form ad_x for any x (inner derivations kill
#                 alpha_0 because alpha_0 is central);
#
#   (H2 killer)   the level-direction 2-cocycle omega(alpha_m, alpha_n)
#                 = m delta_{m+n,0} K (deforming k -> k + eps) is EXACT:
#                 omega = d(N) for the rescaling 1-cochain N(alpha_m) =
#                 alpha_m / 2, N(K) = 0.
#
# These are mode-level Lie-algebra computations (Heisenberg algebra
# h = span{alpha_m} + CK, [alpha_m, alpha_n] = m delta_{m+n,0} K).  They are
# the mode shadow of the level-rescaling exactness argument, NOT a
# computation of the full chiral (vertex-algebra) cohomology; the full
# bounded profile remains a literature input.


# Basis labels: ("a", m) for the mode alpha_m, ("K",) for the centre.
# Elements are dicts basis-label -> integer coefficient.
_K = ("K",)


def _heis_bracket_elt(x: Dict, y: Dict) -> Dict:
    """[x, y] in the Heisenberg algebra: [alpha_m, alpha_n] = m d_{m+n,0} K."""
    out: Dict = {}
    for bx, cx in x.items():
        for by, cy in y.items():
            if bx == _K or by == _K:
                continue  # K is central
            m, n = bx[1], by[1]
            if m + n == 0:
                out[_K] = out.get(_K, 0) + cx * cy * m
    return {b: c for b, c in out.items() if c != 0}


def _add(x: Dict, y: Dict, sign: int = 1) -> Dict:
    out = dict(x)
    for b, c in y.items():
        out[b] = out.get(b, 0) + sign * c
    return {b: c for b, c in out.items() if c != 0}


def _apply_linear(phi: Mapping, x: Dict) -> Dict:
    """Apply a basis-defined linear map (basis label -> element dict)."""
    out: Dict = {}
    for b, c in x.items():
        for tb, tc in phi.get(b, {}).items():
            out[tb] = out.get(tb, 0) + c * tc
    return {b: c for b, c in out.items() if c != 0}


def heisenberg_outer_derivation_window_check(window: int = 6) -> Dict[str, bool]:
    """Finite-window verification of the outer derivation D: alpha_0 -> K.

    D(alpha_m) = delta_{m,0} K, D(K) = 0, on the Heisenberg algebra
    h = span{alpha_m : |m| <= window} + CK with [alpha_m, alpha_n] =
    m delta_{m+n,0} K.  Verifies by explicit linear algebra on the basis:

    * derivation identity D([x, y]) = [D x, y] + [x, D y] for all basis
      pairs (including pairs with K);
    * non-innerness: ad_x(alpha_0) = 0 for every basis vector x (so for
      every x by linearity), while D(alpha_0) = K != 0.

    Every boolean is computed from the representation, not asserted.
    """
    modes = list(range(-window, window + 1))
    basis = [("a", m) for m in modes] + [_K]
    D = {("a", 0): {_K: 1}}  # all other basis labels map to 0

    derivation_identity = True
    for bx in basis:
        for by in basis:
            x = {bx: 1}
            y = {by: 1}
            lhs = _apply_linear(D, _heis_bracket_elt(x, y))
            rhs = _add(
                _heis_bracket_elt(_apply_linear(D, x), y),
                _heis_bracket_elt(x, _apply_linear(D, y)),
            )
            if lhs != rhs:
                derivation_identity = False

    ad_kills_alpha0 = all(
        _heis_bracket_elt({b: 1}, {("a", 0): 1}) == {} for b in basis
    )
    d_moves_alpha0 = _apply_linear(D, {("a", 0): 1}) == {_K: 1}

    return {
        "derivation_identity_on_window": derivation_identity,
        "inner_derivations_kill_alpha0": ad_kills_alpha0,
        "D_is_outer": derivation_identity and ad_kills_alpha0 and d_moves_alpha0,
    }


def heisenberg_level_rescaling_exactness_window_check(
    window: int = 6,
) -> Dict[str, bool]:
    """Finite-window verification that the level cocycle is exact.

    The level-direction 2-cocycle (adjoint/K-line valued) is
    omega(alpha_m, alpha_n) = m delta_{m+n,0} K -- the derivative of the
    bracket under k -> k + eps.  The rescaling 1-cochain is
    N(alpha_m) = alpha_m / 2, N(K) = 0 (the infinitesimal generator of
    alpha -> (1 + eps/2) alpha, which scales the level by 1 + eps; both
    bracket slots contribute, hence the 1/2).  The coboundary

        (dN)(x, y) = [N x, y] + [x, N y] - N([x, y])

    is computed on every basis pair and compared with omega.  Exactness of
    the level cocycle is the mode-level mechanism behind H^2 = 0 in the
    bounded Heisenberg profile (BDSK Theorem 7.4); this check does NOT by
    itself compute the full chiral H^2.
    """
    modes = list(range(-window, window + 1))
    basis = [("a", m) for m in modes] + [_K]
    N = {("a", m): {("a", m): Fraction(1, 2)} for m in modes}  # N(K) = 0

    def omega(bx, by) -> Dict:
        if bx == _K or by == _K:
            return {}
        m, n = bx[1], by[1]
        return {_K: m} if (m + n == 0 and m != 0) else {}

    exact_on_all_pairs = True
    for bx in basis:
        for by in basis:
            x = {bx: 1}
            y = {by: 1}
            dN = _add(
                _add(
                    _heis_bracket_elt(_apply_linear(N, x), y),
                    _heis_bracket_elt(x, _apply_linear(N, y)),
                ),
                _apply_linear(N, _heis_bracket_elt(x, y)),
                sign=-1,
            )
            if dN != omega(bx, by):
                exact_on_all_pairs = False

    return {
        "level_cocycle_exact_on_window": exact_on_all_pairs,
    }


def heisenberg_bounded_hilbert_polynomial() -> Tuple[int, ...]:
    """Hilbert-polynomial coefficients of the bounded Heisenberg profile.

    Computed from ``chirhoch_heisenberg().bounded_dimensions`` (the BDSK
    Theorem 7.4 profile carried by this module), NOT hardcoded here:
    coefficient of t^n is dim H^n.  Expected (2, 1), i.e. 2 + t.
    """
    dims = chirhoch_heisenberg().bounded_dimensions
    if not dims:
        return ()
    top = max(dims)
    return tuple(dims.get(n, 0) for n in range(top + 1))


def generate_summary_table() -> str:
    lines = [
        "Family-indexed chiral Hochschild audit",
        "family | bounded result | chart result",
    ]
    for row in all_standard_families():
        if row.bounded_dimensions is None:
            bounded = row.bounded_status
        else:
            bounded = f"support={row.bounded_support}, dims={dict(row.bounded_dimensions)}"
        lines.append(f"{row.family} | {bounded} | {row.chart_status}")
    return "\n".join(lines)


if __name__ == "__main__":
    print(generate_summary_table())
