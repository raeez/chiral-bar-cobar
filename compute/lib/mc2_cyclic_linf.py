"""MC2 scaffold: coderivation dg-Lie + cyclic L-infinity + kappa extraction.

This module provides a finite-dimensional computational template for
Conjecture ``conj:universal-theta`` (MC2), focusing on:

1. coderivation dg-Lie control object,
2. cyclic L-infinity brackets (low arity),
3. first Maurer-Cartan solver pass in a completed-direction toy model,
4. **kappa extraction**: recovery of the modular characteristic scalar
   ``kappa(A)`` from the cyclic L-infinity seed data (l_2 bracket + pairing),
5. L-infinity arity-4 homotopy Jacobi identity verification,
6. full cyclic symmetry verification for l_2 and l_3.
7. a first completed-tensor and clutching compatibility surrogate.
8. completed-series cyclicity checks and a first genus-truncated
   symbolic completed MC solver branch.
9. genus-stratified obstruction extraction and recursive
   branchwise truncated completed-MC solving.

The kappa extraction (Step 3 of the MC2 programme) shows that the scalar
shadow of the universal Maurer-Cartan class Theta_A is recoverable from
the cyclic L-infinity data alone.  For affine sl_2 at level k, the
formula kappa = dim(g) * (k + h^vee) / (2 * h^vee) = 3(k+2)/4 is
verified against the explicit two-channel genus-2 computation in
Theorem thm:sl2-genus2-curvature.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from typing import Dict, Iterable, Mapping, Tuple

import numpy as np
from sympy import Eq, Matrix, Rational, Symbol, solve, simplify

from compute.lib.bar_complex import OPEAlgebra, sl2_algebra
from compute.lib.mc2_cyclic_ce import (
    cyclic_ce_cohomology as _cyclic_ce_cohomology,
    g2_structure_constants as _g2_sc,
    g2_killing_form as _g2_kf,
    sl3_structure_constants as _sl3_sc,
    sl3_killing_form as _sl3_kf,
    sp4_structure_constants as _sp4_sc,
    sp4_killing_form as _sp4_kf,
)

Vector = Dict[str, object]
TensorVector = Dict[Tuple[str, str], object]
CompletedSeries = Dict[int, Vector]
CompletedTensorSeries = Dict[int, TensorVector]
ScalarSeries = Dict[int, object]


def _clean(vec: Mapping[str, object]) -> Vector:
    """Drop zero coefficients after simplification."""
    out: Vector = {}
    for key, value in vec.items():
        sv = simplify(value)
        if sv != 0:
            out[key] = sv
    return out


def _add(u: Mapping[str, object], v: Mapping[str, object]) -> Vector:
    keys = set(u) | set(v)
    return _clean({k: u.get(k, 0) + v.get(k, 0) for k in keys})


def _scale(c: object, v: Mapping[str, object]) -> Vector:
    return _clean({k: c * val for k, val in v.items()})


def _clean_tensor(vec: Mapping[Tuple[str, str], object]) -> TensorVector:
    """Drop zero tensor coefficients after simplification."""
    out: TensorVector = {}
    for key, value in vec.items():
        sv = simplify(value)
        if sv != 0:
            out[key] = sv
    return out


def _clean_series(series: Mapping[int, Mapping[str, object]]) -> CompletedSeries:
    """Normalize a completed-series surrogate indexed by genus."""
    out: CompletedSeries = {}
    for g, vec in series.items():
        if int(g) < 0:
            raise ValueError("genus index must be nonnegative")
        cleaned = _clean(vec)
        if cleaned:
            out[int(g)] = cleaned
    return out


def _clean_tensor_series(
    series: Mapping[int, Mapping[Tuple[str, str], object]],
) -> CompletedTensorSeries:
    """Normalize a tensor-valued completed surrogate indexed by genus."""
    out: CompletedTensorSeries = {}
    for g, vec in series.items():
        if int(g) < 0:
            raise ValueError("genus index must be nonnegative")
        cleaned = _clean_tensor(vec)
        if cleaned:
            out[int(g)] = cleaned
    return out


def _add_series(
    u: Mapping[int, Mapping[str, object]],
    v: Mapping[int, Mapping[str, object]],
    max_genus: int | None = None,
) -> CompletedSeries:
    """Add two completed surrogates with optional truncation."""
    u0 = _clean_series(u)
    v0 = _clean_series(v)
    out: CompletedSeries = {}
    for g in set(u0) | set(v0):
        if max_genus is not None and g > max_genus:
            continue
        summed = _add(u0.get(g, {}), v0.get(g, {}))
        if summed:
            out[g] = summed
    return out


def _scale_series(
    c: object,
    series: Mapping[int, Mapping[str, object]],
    max_genus: int | None = None,
) -> CompletedSeries:
    """Scale a completed surrogate with optional truncation."""
    out: CompletedSeries = {}
    for g, vec in _clean_series(series).items():
        if max_genus is not None and g > max_genus:
            continue
        scaled = _scale(c, vec)
        if scaled:
            out[g] = scaled
    return out


@dataclass(frozen=True)
class CoderivationDGLieModel:
    """Finite dg-Lie model representing a coderivation control layer."""

    basis: Tuple[str, ...]
    degrees: Mapping[str, int]
    differential_table: Mapping[str, Mapping[str, object]]
    bracket_table: Mapping[Tuple[str, str], Mapping[str, object]]

    def d_basis(self, a: str) -> Vector:
        return _clean(self.differential_table.get(a, {}))

    def bracket_basis(self, a: str, b: str) -> Vector:
        if (a, b) in self.bracket_table:
            return _clean(self.bracket_table[(a, b)])
        if (b, a) in self.bracket_table:
            sign = -((-1) ** (self.degrees[a] * self.degrees[b]))
            return _scale(sign, self.bracket_table[(b, a)])
        return {}

    def d_vector(self, v: Mapping[str, object]) -> Vector:
        out: Vector = {}
        for a, coeff in v.items():
            out = _add(out, _scale(coeff, self.d_basis(a)))
        return out

    def bracket_vectors(self, u: Mapping[str, object], v: Mapping[str, object]) -> Vector:
        out: Vector = {}
        for a, ca in u.items():
            for b, cb in v.items():
                out = _add(out, _scale(ca * cb, self.bracket_basis(a, b)))
        return out

    def verify_d_squared_zero(self) -> bool:
        for a in self.basis:
            if self.d_vector(self.d_basis(a)):
                return False
        return True

    def verify_jacobi_identity(self) -> bool:
        for a in self.basis:
            for b in self.basis:
                for c in self.basis:
                    term1 = self.bracket_vectors(
                        {a: 1},
                        self.bracket_vectors({b: 1}, {c: 1}),
                    )
                    term2 = self.bracket_vectors(
                        {b: 1},
                        self.bracket_vectors({c: 1}, {a: 1}),
                    )
                    term3 = self.bracket_vectors(
                        {c: 1},
                        self.bracket_vectors({a: 1}, {b: 1}),
                    )
                    if _add(_add(term1, term2), term3):
                        return False
        return True

    def verify_d_leibniz(self) -> bool:
        for a in self.basis:
            for b in self.basis:
                lhs = self.d_vector(self.bracket_basis(a, b))
                rhs = self.bracket_vectors(self.d_basis(a), {b: 1})
                rhs = _add(
                    rhs,
                    _scale((-1) ** self.degrees[a], self.bracket_vectors({a: 1}, self.d_basis(b))),
                )
                if _add(lhs, _scale(-1, rhs)):
                    return False
        return True


@dataclass(frozen=True)
class CyclicLInfinityModel:
    """Finite cyclic L-infinity model with brackets through arity 3."""

    basis: Tuple[str, ...]
    degrees: Mapping[str, int]
    pairing_table: Mapping[Tuple[str, str], object]
    l1_table: Mapping[str, Mapping[str, object]]
    l2_table: Mapping[Tuple[str, str], Mapping[str, object]]
    l3_table: Mapping[Tuple[str, str, str], Mapping[str, object]]

    def pairing_basis(self, a: str, b: str) -> object:
        return simplify(self.pairing_table.get((a, b), 0))

    def pairing_vectors(self, u: Mapping[str, object], v: Mapping[str, object]) -> object:
        total = 0
        for a, ca in u.items():
            for b, cb in v.items():
                total += ca * cb * self.pairing_basis(a, b)
        return simplify(total)

    def l1_basis(self, a: str) -> Vector:
        return _clean(self.l1_table.get(a, {}))

    def l2_basis(self, a: str, b: str) -> Vector:
        return _clean(self.l2_table.get((a, b), {}))

    def l3_basis(self, a: str, b: str, c: str) -> Vector:
        return _clean(self.l3_table.get((a, b, c), {}))

    def l1_vector(self, v: Mapping[str, object]) -> Vector:
        out: Vector = {}
        for a, coeff in v.items():
            out = _add(out, _scale(coeff, self.l1_basis(a)))
        return out

    def l2_vectors(self, u: Mapping[str, object], v: Mapping[str, object]) -> Vector:
        out: Vector = {}
        for a, ca in u.items():
            for b, cb in v.items():
                out = _add(out, _scale(ca * cb, self.l2_basis(a, b)))
        return out

    def l3_vectors(
        self,
        u: Mapping[str, object],
        v: Mapping[str, object],
        w: Mapping[str, object],
    ) -> Vector:
        out: Vector = {}
        for a, ca in u.items():
            for b, cb in v.items():
                for c, cc in w.items():
                    out = _add(out, _scale(ca * cb * cc, self.l3_basis(a, b, c)))
        return out


def _simple_pole_bracket_table_from_ope(algebra: OPEAlgebra) -> Dict[Tuple[str, str], Vector]:
    """Extract generator-level simple-pole brackets from an OPE algebra."""
    names = set(algebra.gen_names)
    table: Dict[Tuple[str, str], Vector] = {}
    for a in algebra.gen_names:
        for b in algebra.gen_names:
            pole = algebra.simple_pole(a, b)
            filtered = _clean({c: coeff for c, coeff in pole.items() if c in names})
            if filtered:
                table[(a, b)] = filtered
    return table


def _normalized_double_pole_pairing_from_ope(
    algebra: OPEAlgebra,
) -> Dict[Tuple[str, str], object]:
    """Extract a normalized generator pairing from double-pole coefficients."""
    level = algebra.level
    table: Dict[Tuple[str, str], object] = {}
    for a in algebra.gen_names:
        for b in algebra.gen_names:
            coeff = simplify(algebra.double_pole(a, b).get("1", 0))
            if coeff == 0:
                continue
            if level is not None:
                coeff = simplify(coeff / level)
            table[(a, b)] = coeff
    return table


def build_mc2_coderivation_dg_lie_model() -> CoderivationDGLieModel:
    """Toy coderivation dg-Lie layer used as the MC2 Step-1 compute scaffold."""
    return CoderivationDGLieModel(
        basis=("theta", "omega"),
        degrees={"theta": 1, "omega": 2},
        differential_table={
            "theta": {},
            "omega": {},
        },
        bracket_table={
            ("theta", "theta"): {"omega": Rational(2)},
        },
    )


def build_mc2_cyclic_linf_model() -> CyclicLInfinityModel:
    """Toy cyclic L-infinity layer through arity 3.

    The nontrivial brackets are:
      l_2(theta, theta) = 2*omega
      l_3(theta, theta, theta) = -6*omega

    This yields a nontrivial single-parameter MC equation with solutions
    at parameters 0 and 1.
    """
    return CyclicLInfinityModel(
        basis=("theta", "omega"),
        degrees={"theta": 1, "omega": 2},
        pairing_table={
            ("theta", "omega"): Rational(1),
            ("omega", "theta"): Rational(1),
        },
        l1_table={
            "theta": {},
            "omega": {},
        },
        l2_table={
            ("theta", "theta"): {"omega": Rational(2)},
        },
        l3_table={
            ("theta", "theta", "theta"): {"omega": Rational(-6)},
        },
    )


def build_mc2_sl2_coderivation_seed() -> CoderivationDGLieModel:
    """Bar-derived dg-Lie seed from generator simple poles of affine ``sl_2``."""
    algebra = sl2_algebra()
    basis = tuple(algebra.gen_names)
    return CoderivationDGLieModel(
        basis=basis,
        degrees={name: 0 for name in basis},
        differential_table={name: {} for name in basis},
        bracket_table=_simple_pole_bracket_table_from_ope(algebra),
    )


def build_mc2_sl2_cyclic_linf_seed() -> CyclicLInfinityModel:
    """Bar-derived cyclic ``L_\\infty`` seed from affine ``sl_2`` OPE data."""
    algebra = sl2_algebra()
    basis = tuple(algebra.gen_names)
    return CyclicLInfinityModel(
        basis=basis,
        degrees={name: 0 for name in basis},
        pairing_table=_normalized_double_pole_pairing_from_ope(algebra),
        l1_table={name: {} for name in basis},
        l2_table=_simple_pole_bracket_table_from_ope(algebra),
        l3_table={},
    )


def _sl2_killing_3cocycle_from_seed(
    bracket_table: Mapping[Tuple[str, str], Mapping[str, object]],
    pairing_table: Mapping[Tuple[str, str], object],
    basis: Tuple[str, ...],
) -> Dict[Tuple[str, str, str], object]:
    """Compute phi(a,b,c) = <[a,b],c> from seed bracket/pairing data."""
    cocycle: Dict[Tuple[str, str, str], object] = {}
    for a, b, c in product(basis, repeat=3):
        bracket = bracket_table.get((a, b), {})
        coeff = simplify(sum(bracket.get(x, 0) * pairing_table.get((x, c), 0) for x in basis))
        if coeff != 0:
            cocycle[(a, b, c)] = coeff
    return cocycle


def _to_fraction(value: object) -> Fraction:
    """Convert an exact scalar to ``fractions.Fraction``."""
    sv = simplify(value)
    if hasattr(sv, "as_numer_denom"):
        num, den = sv.as_numer_denom()
        return Fraction(int(num), int(den))
    return Fraction(sv)


def _permutation_sign_from_source_to_target(
    source: Tuple[str, ...],
    target: Tuple[str, ...],
) -> int:
    """Sign of the permutation carrying ``source`` to ``target``."""
    if len(source) != len(target):
        raise ValueError("source and target must have equal length")
    source_list = list(source)
    used = [False] * len(source_list)
    perm: list[int] = []
    for value in target:
        matched = False
        for idx, source_value in enumerate(source_list):
            if used[idx] or source_value != value:
                continue
            used[idx] = True
            perm.append(idx)
            matched = True
            break
        if not matched:
            raise ValueError("target is not a permutation of source")
    inversions = sum(
        1
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
        if perm[i] > perm[j]
    )
    return -1 if inversions % 2 else 1


def _canonicalized_antisymmetric_value(
    lookup,
    canonical_input: Tuple[str, ...],
) -> Vector:
    """Recover canonical antisymmetric value from any nonzero permutation slot."""
    for permuted in set(permutations(canonical_input)):
        vec = lookup(*permuted)
        if not vec:
            continue
        sign = _permutation_sign_from_source_to_target(canonical_input, permuted)
        normalized = _clean({key: sign * value for key, value in vec.items()})
        if normalized:
            return normalized
    return {}


def cyclic_ce_profile_from_cyclic_seed(
    model: CyclicLInfinityModel,
    generator_basis: Tuple[str, ...] | None = None,
) -> Dict[str, object]:
    """Compute cyclic CE profile from a cyclic seed's ``l_2`` and pairing data.

    This is the compute bridge between the seed-level MC2 data and the CE
    uniqueness checks for the Killing 3-cocycle deformation class.
    """
    basis = generator_basis or tuple(
        name for name in model.basis if model.degrees.get(name, 0) == 0
    )
    if not basis:
        raise ValueError("generator basis must be nonempty")

    index = {name: i for i, name in enumerate(basis)}
    dim = len(basis)
    c = np.zeros((dim, dim, dim), dtype=object)
    kap = np.zeros((dim, dim), dtype=object)

    for i, a in enumerate(basis):
        for j, b in enumerate(basis):
            kap[i, j] = _to_fraction(model.pairing_basis(a, b))
            for out_name, coeff in model.l2_basis(a, b).items():
                if out_name not in index:
                    if simplify(coeff) != 0:
                        raise ValueError(
                            "generator basis is not closed under l2 bracket; "
                            f"got output basis element '{out_name}'"
                        )
                    continue
                c[i, j, index[out_name]] += _to_fraction(coeff)

    profile = dict(_cyclic_ce_cohomology(c, kap, dim))
    profile["generator_basis"] = basis
    return profile


def build_cyclic_l3_marker_extension_from_seed(
    seed: CyclicLInfinityModel,
    marker_name: str = "eta",
    marker_degree: int = 2,
    marker_pairing: object = Rational(1),
    generator_basis: Tuple[str, ...] | None = None,
) -> CyclicLInfinityModel:
    """Lift a cyclic seed by adding the first nontrivial Killing ``l_3`` marker.

    For a generator basis ``B``, defines
    ``phi(a,b,c)=< [a,b], c >`` and inserts it as an ``eta``-valued
    ``l_3`` channel on ``B^3``.
    """
    if marker_name in seed.basis:
        raise ValueError(f"marker '{marker_name}' already present in basis")

    basis = generator_basis or tuple(
        name for name in seed.basis if seed.degrees.get(name, 0) == 0
    )
    if not basis:
        raise ValueError("generator basis must be nonempty")
    unknown = [name for name in basis if name not in seed.basis]
    if unknown:
        raise ValueError(f"generator basis contains unknown elements: {unknown}")

    cocycle = _sl2_killing_3cocycle_from_seed(
        bracket_table=seed.l2_table,
        pairing_table=seed.pairing_table,
        basis=basis,
    )

    l3_table = {
        key: dict(value)
        for key, value in seed.l3_table.items()
    }
    for key, coeff in cocycle.items():
        slot = dict(l3_table.get(key, {}))
        slot[marker_name] = simplify(slot.get(marker_name, 0) + coeff)
        cleaned = _clean(slot)
        if cleaned:
            l3_table[key] = cleaned
        elif key in l3_table:
            l3_table.pop(key)

    extended_basis = seed.basis + (marker_name,)
    degrees = dict(seed.degrees)
    degrees[marker_name] = marker_degree

    pairing = dict(seed.pairing_table)
    pairing[(marker_name, marker_name)] = simplify(marker_pairing)

    l1_table = {
        key: dict(value)
        for key, value in seed.l1_table.items()
    }
    l1_table[marker_name] = {}

    l2_table = {
        key: dict(value)
        for key, value in seed.l2_table.items()
    }

    return CyclicLInfinityModel(
        basis=extended_basis,
        degrees=degrees,
        pairing_table=pairing,
        l1_table=l1_table,
        l2_table=l2_table,
        l3_table=l3_table,
    )


def build_mc2_sl2_cyclic_linf_l3_seed() -> CyclicLInfinityModel:
    """First nontrivial higher-bracket MC2 seed from affine ``sl_2``.

    The ``l_3`` channel is populated by the Killing 3-cocycle
    ``phi(a,b,c)=< [a,b], c >`` and lands in an explicit degree-2 marker
    basis element ``eta``.
    """
    return build_cyclic_l3_marker_extension_from_seed(
        build_mc2_sl2_cyclic_linf_seed(),
        marker_name="eta",
        marker_degree=2,
        marker_pairing=Rational(1),
    )


def build_shifted_symmetric_cyclic_linf_from_seed(
    seed: CyclicLInfinityModel,
    generator_basis: Tuple[str, ...] | None = None,
    degree_shift: int = 1,
) -> CyclicLInfinityModel:
    r"""Build a suspension-shifted symmetric representative of a seed.

    For generator inputs, this removes antisymmetric orientation signs from
    ``l_2``/``l_3`` table lookups by fixing a canonical basis ordering and
    transporting coefficients to all ordered slots.
    """
    basis = generator_basis or tuple(
        name for name in seed.basis if seed.degrees.get(name, 0) == 0
    )
    if not basis:
        raise ValueError("generator basis must be nonempty")
    unknown = [name for name in basis if name not in seed.basis]
    if unknown:
        raise ValueError(f"generator basis contains unknown elements: {unknown}")

    order = {name: i for i, name in enumerate(seed.basis)}
    generator_set = set(basis)

    l2_table: Dict[Tuple[str, str], Vector] = {}
    for a in seed.basis:
        for b in seed.basis:
            if a not in generator_set or b not in generator_set:
                continue
            canonical = tuple(sorted((a, b), key=lambda name: order[name]))
            value = _canonicalized_antisymmetric_value(seed.l2_basis, canonical)
            if value:
                l2_table[(a, b)] = value

    l3_table: Dict[Tuple[str, str, str], Vector] = {}
    for a, b, c in product(seed.basis, repeat=3):
        if a not in generator_set or b not in generator_set or c not in generator_set:
            continue
        canonical = tuple(sorted((a, b, c), key=lambda name: order[name]))
        value = _canonicalized_antisymmetric_value(seed.l3_basis, canonical)
        if value:
            l3_table[(a, b, c)] = value

    return CyclicLInfinityModel(
        basis=seed.basis,
        degrees={name: degree + degree_shift for name, degree in seed.degrees.items()},
        pairing_table=dict(seed.pairing_table),
        l1_table={key: dict(value) for key, value in seed.l1_table.items()},
        l2_table=l2_table,
        l3_table=l3_table,
    )


def build_mc2_sl2_shifted_cyclic_linf_l3_seed() -> CyclicLInfinityModel:
    """Suspension-shifted symmetric ``sl_2`` seed with nontrivial MC channels."""
    return build_shifted_symmetric_cyclic_linf_from_seed(
        seed=build_mc2_sl2_cyclic_linf_l3_seed(),
        generator_basis=("e", "h", "f"),
        degree_shift=1,
    )


# ---------------------------------------------------------------------------
# General-purpose seed builders from Lie algebra data
# ---------------------------------------------------------------------------


def _bracket_table_from_structure_constants(
    c,  # np.ndarray shape (dim, dim, dim)
    basis_names: Tuple[str, ...],
) -> Dict[Tuple[str, str], Vector]:
    """Convert structure constants c[i,j,k] to a bracket table dict."""
    from fractions import Fraction as _Frac

    dim = len(basis_names)
    table: Dict[Tuple[str, str], Vector] = {}
    for i in range(dim):
        for j in range(dim):
            vec: Vector = {}
            for k in range(dim):
                val = c[i, j, k]
                if isinstance(val, _Frac):
                    val = Rational(val.numerator, val.denominator)
                if val != 0:
                    vec[basis_names[k]] = val
            if vec:
                table[(basis_names[i], basis_names[j])] = vec
    return table


def _pairing_table_from_killing_form(
    kap,  # np.ndarray shape (dim, dim)
    basis_names: Tuple[str, ...],
) -> Dict[Tuple[str, str], object]:
    """Convert a Killing form matrix to a pairing table dict."""
    from fractions import Fraction as _Frac

    dim = len(basis_names)
    table: Dict[Tuple[str, str], object] = {}
    for i in range(dim):
        for j in range(dim):
            val = kap[i, j]
            if isinstance(val, _Frac):
                val = Rational(val.numerator, val.denominator)
            if val != 0:
                table[(basis_names[i], basis_names[j])] = val
    return table


def build_mc2_sl3_coderivation_seed() -> CoderivationDGLieModel:
    """Bar-derived dg-Lie seed from ``sl_3`` structure constants."""
    basis = ("e1", "e2", "e12", "h1", "h2", "f1", "f2", "f12")
    c = _sl3_sc()
    bracket = _bracket_table_from_structure_constants(c, basis)
    return CoderivationDGLieModel(
        basis=basis,
        degrees={name: 0 for name in basis},
        differential_table={name: {} for name in basis},
        bracket_table=bracket,
    )


def build_mc2_sl3_cyclic_linf_seed() -> CyclicLInfinityModel:
    """Bar-derived cyclic ``L_\\infty`` seed from ``sl_3`` structure data."""
    basis = ("e1", "e2", "e12", "h1", "h2", "f1", "f2", "f12")
    c = _sl3_sc()
    kap = _sl3_kf()
    bracket = _bracket_table_from_structure_constants(c, basis)
    pairing = _pairing_table_from_killing_form(kap, basis)
    return CyclicLInfinityModel(
        basis=basis,
        degrees={name: 0 for name in basis},
        pairing_table=pairing,
        l1_table={name: {} for name in basis},
        l2_table=bracket,
        l3_table={},
    )


def build_mc2_sl3_cyclic_linf_l3_seed() -> CyclicLInfinityModel:
    """First nontrivial higher-bracket MC2 seed from ``sl_3``.

    The ``l_3`` channel is the Killing 3-cocycle
    ``phi(a,b,c)=< [a,b], c >`` with output in an explicit degree-2
    marker basis element ``eta``.
    """
    return build_cyclic_l3_marker_extension_from_seed(
        build_mc2_sl3_cyclic_linf_seed(),
        marker_name="eta",
        marker_degree=2,
        marker_pairing=Rational(1),
    )


def build_mc2_sl3_shifted_cyclic_linf_l3_seed() -> CyclicLInfinityModel:
    """Suspension-shifted symmetric ``sl_3`` seed with nontrivial MC channels."""
    return build_shifted_symmetric_cyclic_linf_from_seed(
        seed=build_mc2_sl3_cyclic_linf_l3_seed(),
        generator_basis=("e1", "e2", "e12", "h1", "h2", "f1", "f2", "f12"),
        degree_shift=1,
    )


def verify_mc2_sl3_seed() -> Dict[str, bool]:
    """Structural checks for the bar-derived ``sl_3`` MC2 seed."""
    dg = build_mc2_sl3_coderivation_seed()
    linf = build_mc2_sl3_cyclic_linf_seed()

    pairing_matrix = Matrix(
        [[linf.pairing_basis(a, b) for b in linf.basis] for a in linf.basis]
    )
    ad_invariance = True
    for a in linf.basis:
        for b in linf.basis:
            for c in linf.basis:
                lhs = linf.pairing_vectors(dg.bracket_basis(a, b), {c: 1})
                rhs = linf.pairing_vectors({a: 1}, dg.bracket_basis(b, c))
                if simplify(lhs - rhs) != 0:
                    ad_invariance = False
                    break
            if not ad_invariance:
                break
        if not ad_invariance:
            break

    return {
        "sl3_seed_d_squared_zero": dg.verify_d_squared_zero(),
        "sl3_seed_jacobi": dg.verify_jacobi_identity(),
        "sl3_seed_leibniz": dg.verify_d_leibniz(),
        "sl3_seed_bracket_e1_f1_h1": dg.bracket_basis("e1", "f1") == {"h1": Rational(1)},
        "sl3_seed_bracket_e1_e2_e12": dg.bracket_basis("e1", "e2") == {"e12": Rational(1)},
        "sl3_seed_bracket_h1_e1_2e1": dg.bracket_basis("h1", "e1") == {"e1": Rational(2)},
        "sl3_seed_pairing_e1_f1_1": simplify(linf.pairing_basis("e1", "f1") - 1) == 0,
        "sl3_seed_pairing_h1_h1_2": simplify(linf.pairing_basis("h1", "h1") - 2) == 0,
        "sl3_seed_pairing_h1_h2_minus1": simplify(linf.pairing_basis("h1", "h2") + 1) == 0,
        "sl3_seed_pairing_nondegenerate": simplify(pairing_matrix.det()) != 0,
        "sl3_seed_pairing_ad_invariant": ad_invariance,
    }


def verify_mc2_sl3_kappa_extraction() -> Dict[str, object]:
    """Full kappa extraction verification for the sl_3 cyclic L-infinity seed.

    Expected for sl_3: dim=8, h^vee=3, C_2 eigenvalue=6,
    kappa = 4(k+3)/3, double-pole = 4k/3, simple-pole = 4.
    """
    k = Symbol("k")
    model = build_mc2_sl3_cyclic_linf_seed()

    # Casimir computation
    c2_mat = adjoint_casimir_matrix(model)
    c2_eigen = adjoint_casimir_eigenvalue(model)
    from sympy import eye as _eye
    c2_is_scalar = simplify(c2_mat - c2_eigen * _eye(8)) == Matrix.zeros(8, 8)

    # h^vee extraction
    h_dual = dual_coxeter_from_seed(model)

    # kappa extraction
    kappa_val = kappa_from_seed(model, level=k)
    kappa_expected = Rational(4) * (k + 3) / 3

    # Two-channel decomposition
    channels = kappa_two_channel(model, level=k)

    # Complementarity: kappa(k) + kappa(-k - 2*h_dual) = 0
    k_dual = -k - 2 * h_dual
    kappa_dual = kappa_from_seed(model, level=k_dual)
    complementarity = simplify(kappa_val + kappa_dual)

    # Critical level: kappa(k = -h_dual) = 0
    kappa_critical = simplify(kappa_val.subs({k: -h_dual}))

    return {
        "casimir_eigenvalue": c2_eigen,
        "casimir_is_scalar": c2_is_scalar,
        "casimir_equals_2h_dual": simplify(c2_eigen - 2 * h_dual) == 0,
        "h_dual": h_dual,
        "h_dual_equals_3": simplify(h_dual - 3) == 0,
        "kappa": kappa_val,
        "kappa_matches_formula": simplify(kappa_val - kappa_expected) == 0,
        "double_pole_channel": channels["double_pole"],
        "double_pole_matches": simplify(channels["double_pole"] - 4 * k / 3) == 0,
        "simple_pole_channel": channels["simple_pole"],
        "simple_pole_matches": simplify(channels["simple_pole"] - 4) == 0,
        "complementarity_zero": complementarity == 0,
        "critical_level_zero": kappa_critical == 0,
    }


def mc_residual_single_parameter(
    model: CyclicLInfinityModel,
    basis_element: str = "theta",
    parameter: Symbol | None = None,
) -> Tuple[Symbol, Vector]:
    """Compute the arity-3 truncated MC residual for alpha = t * basis_element."""
    t = parameter or Symbol("t")
    alpha = {basis_element: t}
    term1 = model.l1_vector(alpha)
    term2 = _scale(Rational(1, 2), model.l2_vectors(alpha, alpha))
    term3 = _scale(Rational(1, 6), model.l3_vectors(alpha, alpha, alpha))
    residual = _add(_add(term1, term2), term3)
    return t, residual


def solve_mc_single_parameter(
    model: CyclicLInfinityModel,
    basis_element: str = "theta",
    parameter: Symbol | None = None,
) -> Dict[str, object]:
    """Solve the truncated MC equation for alpha = t * basis_element."""
    t, residual = mc_residual_single_parameter(
        model=model,
        basis_element=basis_element,
        parameter=parameter,
    )
    equations = [Eq(expr, 0) for expr in residual.values()]
    if equations:
        raw = solve([eq.lhs for eq in equations], [t], dict=True)
        solutions = sorted({simplify(sol[t]) for sol in raw})
    else:
        solutions = []
    return {
        "parameter": t,
        "residual": residual,
        "equations": equations,
        "solutions": solutions,
    }


def mc_residual_three_parameter(
    model: CyclicLInfinityModel,
    basis_elements: Tuple[str, str, str] = ("e", "h", "f"),
    parameters: Tuple[Symbol, Symbol, Symbol] | None = None,
) -> Tuple[Tuple[Symbol, Symbol, Symbol], Vector]:
    """Compute the first nontrivial mixed-cubic ``l_3`` input channel.

    For degree-0 ``sl_2`` generators, the fully diagonal expression
    ``l_3(alpha, alpha, alpha)`` vanishes by antisymmetry. To expose the
    first higher-bracket signal used in the Wave-52 MC2 frontier step, we
    evaluate the mixed channel ``l_3(x e, y h, z f)`` directly.
    """
    if parameters is None:
        params = (Symbol("x"), Symbol("y"), Symbol("z"))
    else:
        params = parameters
    u = {basis_elements[0]: params[0]}
    v = {basis_elements[1]: params[1]}
    w = {basis_elements[2]: params[2]}
    residual = model.l3_vectors(u, v, w)
    return params, residual


def completed_tensor_product_surrogate(
    left: Mapping[int, Mapping[str, object]],
    right: Mapping[int, Mapping[str, object]],
    max_genus: int | None = None,
) -> CompletedTensorSeries:
    r"""Compute the completed tensor-product surrogate ``\widehat\otimes``.

    The implementation is a genus-indexed Cauchy product:
    coefficients at genus ``g`` are finite sums over ``h+(g-h)=g``.
    """
    left0 = _clean_series(left)
    right0 = _clean_series(right)
    out: CompletedTensorSeries = {}
    for g_left, u in left0.items():
        for g_right, v in right0.items():
            genus = g_left + g_right
            if max_genus is not None and genus > max_genus:
                continue
            slot = out.setdefault(genus, {})
            for a, ca in u.items():
                for b, cb in v.items():
                    key = (a, b)
                    slot[key] = simplify(slot.get(key, 0) + ca * cb)
    return _clean_tensor_series(out)


def clutching_map_via_l2(
    model: CyclicLInfinityModel,
    tensor_coeffs: Mapping[Tuple[str, str], object],
) -> Vector:
    """Project a tensor coefficient slice to the boundary via ``l_2``."""
    out: Vector = {}
    for (a, b), coeff in tensor_coeffs.items():
        out = _add(out, _scale(coeff, model.l2_basis(a, b)))
    return out


def clutching_series_via_l2(
    model: CyclicLInfinityModel,
    tensor_series: Mapping[int, Mapping[Tuple[str, str], object]],
    max_genus: int | None = None,
) -> CompletedSeries:
    """Apply the ``l_2`` clutching map genus-by-genus."""
    out: CompletedSeries = {}
    for g, coeffs in _clean_tensor_series(tensor_series).items():
        if max_genus is not None and g > max_genus:
            continue
        glued = clutching_map_via_l2(model, coeffs)
        if glued:
            out[g] = glued
    return out


def boundary_clutching_series_via_l2(
    model: CyclicLInfinityModel,
    left: Mapping[int, Mapping[str, object]],
    right: Mapping[int, Mapping[str, object]],
    max_genus: int | None = None,
) -> CompletedSeries:
    """Boundary factorization surrogate: tensor convolution then clutching."""
    tensor_series = completed_tensor_product_surrogate(left, right, max_genus=max_genus)
    return clutching_series_via_l2(model, tensor_series, max_genus=max_genus)


def verify_boundary_clutching_compatibility(
    model: CyclicLInfinityModel,
    boundary_series: Mapping[int, Mapping[str, object]],
    left: Mapping[int, Mapping[str, object]],
    right: Mapping[int, Mapping[str, object]],
    max_genus: int | None = None,
) -> bool:
    """Check the first clutching compatibility equality on truncated input."""
    lhs = _clean_series(boundary_series)
    rhs = boundary_clutching_series_via_l2(model, left, right, max_genus=max_genus)
    checked = set(lhs) | set(rhs)
    for g in checked:
        if max_genus is not None and g > max_genus:
            continue
        if _add(lhs.get(g, {}), _scale(-1, rhs.get(g, {}))):
            return False
    return True


def completed_l2_series(
    model: CyclicLInfinityModel,
    left: Mapping[int, Mapping[str, object]],
    right: Mapping[int, Mapping[str, object]],
    max_genus: int | None = None,
) -> CompletedSeries:
    """Cauchy-convolved ``l_2`` on completed surrogates."""
    left0 = _clean_series(left)
    right0 = _clean_series(right)
    out: CompletedSeries = {}
    for g_left, u in left0.items():
        for g_right, v in right0.items():
            genus = g_left + g_right
            if max_genus is not None and genus > max_genus:
                continue
            out[genus] = _add(out.get(genus, {}), model.l2_vectors(u, v))
    return _clean_series(out)


def completed_l3_series(
    model: CyclicLInfinityModel,
    u_series: Mapping[int, Mapping[str, object]],
    v_series: Mapping[int, Mapping[str, object]],
    w_series: Mapping[int, Mapping[str, object]],
    max_genus: int | None = None,
) -> CompletedSeries:
    """Cauchy-convolved ``l_3`` on completed surrogates."""
    u0 = _clean_series(u_series)
    v0 = _clean_series(v_series)
    w0 = _clean_series(w_series)
    out: CompletedSeries = {}
    for g1, u in u0.items():
        for g2, v in v0.items():
            for g3, w in w0.items():
                genus = g1 + g2 + g3
                if max_genus is not None and genus > max_genus:
                    continue
                out[genus] = _add(out.get(genus, {}), model.l3_vectors(u, v, w))
    return _clean_series(out)


def completed_pairing_series(
    model: CyclicLInfinityModel,
    left: Mapping[int, Mapping[str, object]],
    right: Mapping[int, Mapping[str, object]],
    max_genus: int | None = None,
) -> ScalarSeries:
    """Cauchy-convolved cyclic pairing on completed surrogates."""
    left0 = _clean_series(left)
    right0 = _clean_series(right)
    out: ScalarSeries = {}
    for g_left, u in left0.items():
        for g_right, v in right0.items():
            genus = g_left + g_right
            if max_genus is not None and genus > max_genus:
                continue
            value = model.pairing_vectors(u, v)
            out[genus] = simplify(out.get(genus, 0) + value)
    cleaned: ScalarSeries = {}
    for g, value in out.items():
        sv = simplify(value)
        if sv != 0:
            cleaned[g] = sv
    return cleaned


def verify_completed_cyclic_l2(
    model: CyclicLInfinityModel,
    u_series: Mapping[int, Mapping[str, object]],
    v_series: Mapping[int, Mapping[str, object]],
    w_series: Mapping[int, Mapping[str, object]],
    max_genus: int | None = None,
) -> bool:
    """Check completed cyclicity: <l2(u,v),w> = <u,l2(v,w)> genus-by-genus."""
    lhs = completed_pairing_series(
        model=model,
        left=completed_l2_series(model, u_series, v_series, max_genus=max_genus),
        right=w_series,
        max_genus=max_genus,
    )
    rhs = completed_pairing_series(
        model=model,
        left=u_series,
        right=completed_l2_series(model, v_series, w_series, max_genus=max_genus),
        max_genus=max_genus,
    )
    for genus in set(lhs) | set(rhs):
        if max_genus is not None and genus > max_genus:
            continue
        if simplify(lhs.get(genus, 0) - rhs.get(genus, 0)) != 0:
            return False
    return True


def verify_completed_cyclic_l3(
    model: CyclicLInfinityModel,
    u_series: Mapping[int, Mapping[str, object]],
    v_series: Mapping[int, Mapping[str, object]],
    w_series: Mapping[int, Mapping[str, object]],
    x_series: Mapping[int, Mapping[str, object]],
    max_genus: int | None = None,
) -> bool:
    """Check completed cyclicity: <l3(u,v,w),x> = <u,l3(v,w,x)> by genus."""
    lhs = completed_pairing_series(
        model=model,
        left=completed_l3_series(model, u_series, v_series, w_series, max_genus=max_genus),
        right=x_series,
        max_genus=max_genus,
    )
    rhs = completed_pairing_series(
        model=model,
        left=u_series,
        right=completed_l3_series(model, v_series, w_series, x_series, max_genus=max_genus),
        max_genus=max_genus,
    )
    for genus in set(lhs) | set(rhs):
        if max_genus is not None and genus > max_genus:
            continue
        if simplify(lhs.get(genus, 0) - rhs.get(genus, 0)) != 0:
            return False
    return True


def mc_residual_completed_truncated(
    model: CyclicLInfinityModel,
    alpha_series: Mapping[int, Mapping[str, object]],
    max_genus: int,
) -> CompletedSeries:
    """Compute truncated MC residual for a completed-series MC ansatz."""
    alpha0 = _clean_series(alpha_series)

    term1: CompletedSeries = {}
    for g, vec in alpha0.items():
        if g > max_genus:
            continue
        dvec = model.l1_vector(vec)
        if dvec:
            term1[g] = dvec

    term2 = _scale_series(
        Rational(1, 2),
        completed_l2_series(model, alpha0, alpha0, max_genus=max_genus),
        max_genus=max_genus,
    )
    term3 = _scale_series(
        Rational(1, 6),
        completed_l3_series(model, alpha0, alpha0, alpha0, max_genus=max_genus),
        max_genus=max_genus,
    )
    return _add_series(_add_series(term1, term2, max_genus=max_genus), term3, max_genus=max_genus)


def _equation_lhs_from_residual(
    residual: Mapping[int, Mapping[str, object]],
    max_genus: int,
) -> list[object]:
    """Flatten residual coefficients into MC-equation left-hand sides."""
    lhs: list[object] = []
    for genus in range(max_genus + 1):
        for _, expr in sorted(residual.get(genus, {}).items()):
            lhs.append(simplify(expr))
    return lhs


def _basis_slot_symbol_name(parameter_prefix: str, genus: int, basis_element: str) -> str:
    safe_basis = "".join(ch if ch.isalnum() else "_" for ch in basis_element)
    if not safe_basis:
        safe_basis = "basis"
    return f"{parameter_prefix}{genus}_{safe_basis}"


def solve_completed_mc_single_basis_truncated(
    model: CyclicLInfinityModel,
    basis_element: str = "theta",
    max_genus: int = 2,
    parameter_prefix: str = "a",
    fixed_coefficients: Mapping[int, object] | None = None,
) -> Dict[str, object]:
    """Solve truncated completed MC equations on a single-basis ansatz.

    The ansatz is
    ``alpha(q) = sum_{g=0}^{max_genus} a_g q^g * basis_element``,
    optionally fixing selected ``a_g`` values.
    """
    if basis_element not in model.basis:
        raise ValueError(f"unknown basis element '{basis_element}'")
    if max_genus < 0:
        raise ValueError("max_genus must be nonnegative")

    fixed: Dict[int, object] = {}
    if fixed_coefficients is not None:
        for g, value in fixed_coefficients.items():
            gi = int(g)
            if gi < 0 or gi > max_genus:
                raise ValueError(
                    f"fixed coefficient genus {gi} is outside the truncation 0..{max_genus}"
                )
            fixed[gi] = simplify(value)

    parameter_by_genus: Dict[int, object] = {}
    free_parameters: list[Symbol] = []
    for genus in range(max_genus + 1):
        if genus in fixed:
            parameter_by_genus[genus] = fixed[genus]
            continue
        sym = Symbol(f"{parameter_prefix}{genus}")
        parameter_by_genus[genus] = sym
        free_parameters.append(sym)

    alpha_series: CompletedSeries = {}
    for genus in range(max_genus + 1):
        coeff = simplify(parameter_by_genus[genus])
        if coeff != 0:
            alpha_series[genus] = {basis_element: coeff}

    residual = mc_residual_completed_truncated(
        model=model,
        alpha_series=alpha_series,
        max_genus=max_genus,
    )
    equation_lhs = _equation_lhs_from_residual(residual, max_genus=max_genus)
    equations = [Eq(lhs, 0, evaluate=False) for lhs in equation_lhs]

    if not free_parameters:
        solved = all(simplify(lhs) == 0 for lhs in equation_lhs)
        solutions = [{}] if solved else []
    else:
        free_set = set(free_parameters)
        if any(lhs != 0 and lhs.free_symbols.isdisjoint(free_set) for lhs in equation_lhs):
            raw_solutions = []
        elif equation_lhs:
            raw_solutions = solve(equation_lhs, free_parameters, dict=True)
        else:
            raw_solutions = [{}]
        solutions = []
        seen: set[Tuple[Tuple[str, str], ...]] = set()
        for sol in raw_solutions:
            normalized = {sym: simplify(sol.get(sym, sym)) for sym in free_parameters}
            key = tuple((sym.name, str(normalized[sym])) for sym in free_parameters)
            if key in seen:
                continue
            seen.add(key)
            solutions.append(normalized)

    return {
        "basis_element": basis_element,
        "max_genus": max_genus,
        "parameter_by_genus": parameter_by_genus,
        "free_parameters": tuple(free_parameters),
        "alpha_series": alpha_series,
        "residual": residual,
        "equations": equations,
        "solutions": solutions,
    }


def solve_completed_mc_basis_family_truncated(
    model: CyclicLInfinityModel,
    basis_elements: Iterable[str] | None = None,
    max_genus: int = 2,
    parameter_prefix: str = "a",
    fixed_coefficients: Mapping[Tuple[int, str], object] | None = None,
) -> Dict[str, object]:
    """Solve truncated completed MC equations on a multi-basis ansatz.

    The ansatz is
    ``alpha(q) = sum_{g=0}^{max_genus} sum_{b in basis} a_{g,b} q^g * b``,
    optionally fixing selected slot coefficients ``(g, b)``.
    """
    if max_genus < 0:
        raise ValueError("max_genus must be nonnegative")

    if basis_elements is None:
        basis = tuple(model.basis)
    else:
        basis = tuple(dict.fromkeys(basis_elements))
    if not basis:
        raise ValueError("basis_elements must be nonempty")
    unknown_basis = [b for b in basis if b not in model.basis]
    if unknown_basis:
        raise ValueError(f"unknown basis elements: {unknown_basis}")

    fixed: Dict[Tuple[int, str], object] = {}
    if fixed_coefficients is not None:
        for key, value in fixed_coefficients.items():
            genus_raw, basis_element = key
            genus = int(genus_raw)
            if genus < 0 or genus > max_genus:
                raise ValueError(
                    f"fixed coefficient genus {genus} is outside the truncation 0..{max_genus}"
                )
            if basis_element not in basis:
                raise ValueError(
                    f"fixed coefficient basis '{basis_element}' is outside chosen basis set"
                )
            fixed[(genus, basis_element)] = simplify(value)

    parameter_by_slot: Dict[Tuple[int, str], object] = {}
    free_parameters: list[Symbol] = []
    for genus in range(max_genus + 1):
        for basis_element in basis:
            slot = (genus, basis_element)
            if slot in fixed:
                parameter_by_slot[slot] = fixed[slot]
                continue
            sym = Symbol(_basis_slot_symbol_name(parameter_prefix, genus, basis_element))
            parameter_by_slot[slot] = sym
            free_parameters.append(sym)

    alpha_series: CompletedSeries = {}
    for genus in range(max_genus + 1):
        genus_vector: Vector = {}
        for basis_element in basis:
            coeff = simplify(parameter_by_slot[(genus, basis_element)])
            if coeff != 0:
                genus_vector[basis_element] = coeff
        if genus_vector:
            alpha_series[genus] = genus_vector

    residual = mc_residual_completed_truncated(
        model=model,
        alpha_series=alpha_series,
        max_genus=max_genus,
    )
    equation_lhs = _equation_lhs_from_residual(residual, max_genus=max_genus)
    equations = [Eq(lhs, 0, evaluate=False) for lhs in equation_lhs]

    if not free_parameters:
        solved = all(simplify(lhs) == 0 for lhs in equation_lhs)
        solutions = [{}] if solved else []
    else:
        free_set = set(free_parameters)
        if any(lhs != 0 and lhs.free_symbols.isdisjoint(free_set) for lhs in equation_lhs):
            raw_solutions = []
        elif equation_lhs:
            raw_solutions = solve(equation_lhs, free_parameters, dict=True)
        else:
            raw_solutions = [{}]
        solutions = []
        seen: set[Tuple[Tuple[str, str], ...]] = set()
        for sol in raw_solutions:
            normalized = {sym: simplify(sol.get(sym, sym)) for sym in free_parameters}
            key = tuple((sym.name, str(normalized[sym])) for sym in free_parameters)
            if key in seen:
                continue
            seen.add(key)
            solutions.append(normalized)

    return {
        "basis_elements": basis,
        "max_genus": max_genus,
        "parameter_by_slot": parameter_by_slot,
        "free_parameters": tuple(free_parameters),
        "alpha_series": alpha_series,
        "residual": residual,
        "equations": equations,
        "solutions": solutions,
    }


def completed_mc_obstruction_term_at_genus(
    model: CyclicLInfinityModel,
    alpha_series: Mapping[int, Mapping[str, object]],
    genus: int,
    require_zero_genus: bool = True,
) -> Vector:
    r"""Compute the lower-genus obstruction term at one genus.

    This computes
    ``O_g = \sum_{n>=2} 1/n! \sum_{g_1+...+g_n=g,\ g_i<g} l_n(...)``
    for the arities implemented in the model (`l_2`, `l_3`).
    """
    if genus < 0:
        raise ValueError("genus must be nonnegative")
    if genus == 0:
        return {}

    alpha0 = _clean_series(alpha_series)
    if require_zero_genus and alpha0.get(0):
        raise ValueError("genus-0 component must vanish for the strict obstruction split")

    obstruction: Vector = {}

    for g1 in range(genus):
        g2 = genus - g1
        if g2 >= genus:
            continue
        u = alpha0.get(g1)
        v = alpha0.get(g2)
        if u is None or v is None:
            continue
        obstruction = _add(
            obstruction,
            _scale(Rational(1, 2), model.l2_vectors(u, v)),
        )

    for g1 in range(genus):
        for g2 in range(genus):
            g3 = genus - g1 - g2
            if g3 < 0 or g3 >= genus:
                continue
            u = alpha0.get(g1)
            v = alpha0.get(g2)
            w = alpha0.get(g3)
            if u is None or v is None or w is None:
                continue
            obstruction = _add(
                obstruction,
                _scale(Rational(1, 6), model.l3_vectors(u, v, w)),
            )

    return obstruction


def verify_genus_stratified_obstruction_identity(
    model: CyclicLInfinityModel,
    alpha_series: Mapping[int, Mapping[str, object]],
    max_genus: int,
) -> bool:
    """Check residual_g = l1(theta_g) + O_g for a strict genus-filtered ansatz."""
    if max_genus < 0:
        raise ValueError("max_genus must be nonnegative")
    alpha0 = _clean_series(alpha_series)
    if alpha0.get(0):
        return False

    residual = mc_residual_completed_truncated(
        model=model,
        alpha_series=alpha0,
        max_genus=max_genus,
    )
    for genus in range(1, max_genus + 1):
        theta_g = alpha0.get(genus, {})
        lhs = residual.get(genus, {})
        rhs = _add(
            model.l1_vector(theta_g),
            completed_mc_obstruction_term_at_genus(
                model=model,
                alpha_series=alpha0,
                genus=genus,
                require_zero_genus=True,
            ),
        )
        if _add(lhs, _scale(-1, rhs)):
            return False
    return True


def solve_completed_mc_single_basis_recursive(
    model: CyclicLInfinityModel,
    basis_element: str = "theta",
    max_genus: int = 2,
    parameter_prefix: str = "a",
    fixed_coefficients: Mapping[int, object] | None = None,
) -> Dict[str, object]:
    """Solve truncated completed MC equations genus-by-genus on one basis element."""
    if basis_element not in model.basis:
        raise ValueError(f"unknown basis element '{basis_element}'")
    if max_genus < 0:
        raise ValueError("max_genus must be nonnegative")

    fixed: Dict[int, object] = {}
    if fixed_coefficients is not None:
        for g, value in fixed_coefficients.items():
            gi = int(g)
            if gi < 0 or gi > max_genus:
                raise ValueError(
                    f"fixed coefficient genus {gi} is outside the truncation 0..{max_genus}"
                )
            fixed[gi] = simplify(value)

    seed_branch = {g: v for g, v in fixed.items()}
    branches: list[Dict[int, object]] = [seed_branch]
    per_genus_constraints: Dict[int, list[object]] = {}

    for genus in range(max_genus + 1):
        if genus in fixed:
            continue
        sym = Symbol(f"{parameter_prefix}{genus}")
        next_branches: list[Dict[int, object]] = []
        constraints_this_genus: list[object] = []
        for branch in branches:
            alpha_series: CompletedSeries = {}
            for g in range(genus):
                if g not in branch:
                    continue
                coeff = simplify(branch[g])
                if coeff != 0:
                    alpha_series[g] = {basis_element: coeff}
            alpha_series[genus] = {basis_element: sym}

            residual_g = mc_residual_completed_truncated(
                model=model,
                alpha_series=alpha_series,
                max_genus=genus,
            ).get(genus, {})
            equations_lhs = [simplify(expr) for _, expr in sorted(residual_g.items())]
            constraints_this_genus.extend(equations_lhs)

            if not equations_lhs:
                candidates = [sym]
            else:
                if any(lhs != 0 and lhs.free_symbols.isdisjoint({sym}) for lhs in equations_lhs):
                    candidates = []
                else:
                    raw = solve(equations_lhs, [sym], dict=True)
                    if not raw:
                        candidates = []
                    else:
                        candidates = []
                        seen_values: set[str] = set()
                        for sol in raw:
                            value = simplify(sol.get(sym, sym))
                            key = str(value)
                            if key in seen_values:
                                continue
                            seen_values.add(key)
                            candidates.append(value)

            for value in candidates:
                extended = dict(branch)
                extended[genus] = value
                next_branches.append(extended)

        per_genus_constraints[genus] = constraints_this_genus
        deduped: list[Dict[int, object]] = []
        seen: set[Tuple[Tuple[int, str], ...]] = set()
        for branch in next_branches:
            key = tuple((g, str(simplify(branch[g]))) for g in sorted(branch))
            if key in seen:
                continue
            seen.add(key)
            deduped.append(branch)
        branches = deduped
        if not branches:
            break

    completed_branches: list[Dict[int, object]] = []
    for branch in branches:
        full: Dict[int, object] = {}
        for genus in range(max_genus + 1):
            if genus in branch:
                full[genus] = simplify(branch[genus])
            elif genus in fixed:
                full[genus] = simplify(fixed[genus])
            else:
                full[genus] = Symbol(f"{parameter_prefix}{genus}")
        completed_branches.append(full)

    return {
        "basis_element": basis_element,
        "max_genus": max_genus,
        "fixed_coefficients": fixed,
        "per_genus_constraints": per_genus_constraints,
        "branches": completed_branches,
        "branch_count": len(completed_branches),
    }


def solve_completed_mc_basis_family_recursive(
    model: CyclicLInfinityModel,
    basis_elements: Iterable[str] | None = None,
    max_genus: int = 2,
    parameter_prefix: str = "a",
    fixed_coefficients: Mapping[Tuple[int, str], object] | None = None,
) -> Dict[str, object]:
    """Solve truncated completed MC equations genus-by-genus on a basis family."""
    if max_genus < 0:
        raise ValueError("max_genus must be nonnegative")

    if basis_elements is None:
        basis = tuple(model.basis)
    else:
        basis = tuple(dict.fromkeys(basis_elements))
    if not basis:
        raise ValueError("basis_elements must be nonempty")
    unknown_basis = [b for b in basis if b not in model.basis]
    if unknown_basis:
        raise ValueError(f"unknown basis elements: {unknown_basis}")

    fixed: Dict[Tuple[int, str], object] = {}
    if fixed_coefficients is not None:
        for key, value in fixed_coefficients.items():
            genus_raw, basis_element = key
            genus = int(genus_raw)
            if genus < 0 or genus > max_genus:
                raise ValueError(
                    f"fixed coefficient genus {genus} is outside the truncation 0..{max_genus}"
                )
            if basis_element not in basis:
                raise ValueError(
                    f"fixed coefficient basis '{basis_element}' is outside chosen basis set"
                )
            fixed[(genus, basis_element)] = simplify(value)

    branches: list[Dict[Tuple[int, str], object]] = [dict(fixed)]
    per_genus_constraints: Dict[int, list[object]] = {}

    for genus in range(max_genus + 1):
        genus_unknown_symbols: Dict[str, Symbol] = {}
        genus_unknown_list: list[Symbol] = []
        for basis_element in basis:
            slot = (genus, basis_element)
            if slot in fixed:
                continue
            sym = Symbol(_basis_slot_symbol_name(parameter_prefix, genus, basis_element))
            genus_unknown_symbols[basis_element] = sym
            genus_unknown_list.append(sym)

        next_branches: list[Dict[Tuple[int, str], object]] = []
        constraints_this_genus: list[object] = []
        for branch in branches:
            alpha_series: CompletedSeries = {}
            for lower_genus in range(genus):
                lower_vec: Vector = {}
                for basis_element in basis:
                    slot = (lower_genus, basis_element)
                    coeff = simplify(
                        branch.get(
                            slot,
                            fixed.get(
                                slot,
                                Symbol(
                                    _basis_slot_symbol_name(
                                        parameter_prefix,
                                        lower_genus,
                                        basis_element,
                                    )
                                ),
                            ),
                        )
                    )
                    if coeff != 0:
                        lower_vec[basis_element] = coeff
                if lower_vec:
                    alpha_series[lower_genus] = lower_vec

            current_vec: Vector = {}
            for basis_element in basis:
                slot = (genus, basis_element)
                coeff = simplify(
                    fixed.get(slot, genus_unknown_symbols.get(basis_element, 0))
                )
                if coeff != 0:
                    current_vec[basis_element] = coeff
            if current_vec:
                alpha_series[genus] = current_vec

            residual_g = mc_residual_completed_truncated(
                model=model,
                alpha_series=alpha_series,
                max_genus=genus,
            ).get(genus, {})
            equations_lhs = [simplify(expr) for _, expr in sorted(residual_g.items())]
            constraints_this_genus.extend(equations_lhs)

            if not genus_unknown_list:
                candidates = [{}] if all(simplify(lhs) == 0 for lhs in equations_lhs) else []
            elif not equations_lhs:
                candidates = [{sym: sym for sym in genus_unknown_list}]
            else:
                unknown_set = set(genus_unknown_list)
                if any(lhs != 0 and lhs.free_symbols.isdisjoint(unknown_set) for lhs in equations_lhs):
                    candidates = []
                else:
                    raw = solve(equations_lhs, genus_unknown_list, dict=True)
                    if not raw:
                        candidates = []
                    else:
                        candidates = []
                        seen_values: set[Tuple[Tuple[str, str], ...]] = set()
                        for sol in raw:
                            normalized = {
                                sym: simplify(sol.get(sym, sym)) for sym in genus_unknown_list
                            }
                            key = tuple(
                                (sym.name, str(normalized[sym])) for sym in genus_unknown_list
                            )
                            if key in seen_values:
                                continue
                            seen_values.add(key)
                            candidates.append(normalized)

            for candidate in candidates:
                extended = dict(branch)
                for basis_element in basis:
                    slot = (genus, basis_element)
                    if slot in fixed:
                        extended[slot] = simplify(fixed[slot])
                    else:
                        sym = genus_unknown_symbols[basis_element]
                        extended[slot] = simplify(candidate[sym])
                next_branches.append(extended)

        per_genus_constraints[genus] = constraints_this_genus

        deduped: list[Dict[Tuple[int, str], object]] = []
        seen: set[Tuple[Tuple[Tuple[int, str], str], ...]] = set()
        for branch in next_branches:
            key = tuple((slot, str(simplify(value))) for slot, value in sorted(branch.items()))
            if key in seen:
                continue
            seen.add(key)
            deduped.append(branch)
        branches = deduped
        if not branches:
            break

    completed_branches_by_slot: list[Dict[Tuple[int, str], object]] = []
    completed_branches_by_genus: list[CompletedSeries] = []
    for branch in branches:
        full_branch: Dict[Tuple[int, str], object] = {}
        for genus in range(max_genus + 1):
            for basis_element in basis:
                slot = (genus, basis_element)
                value = simplify(
                    branch.get(
                        slot,
                        fixed.get(
                            slot,
                            Symbol(_basis_slot_symbol_name(parameter_prefix, genus, basis_element)),
                        ),
                    )
                )
                full_branch[slot] = value
        completed_branches_by_slot.append(full_branch)

        as_series: CompletedSeries = {}
        for genus in range(max_genus + 1):
            genus_vec: Vector = {}
            for basis_element in basis:
                coeff = simplify(full_branch[(genus, basis_element)])
                if coeff != 0:
                    genus_vec[basis_element] = coeff
            if genus_vec:
                as_series[genus] = genus_vec
        completed_branches_by_genus.append(as_series)

    return {
        "basis_elements": basis,
        "max_genus": max_genus,
        "fixed_coefficients": fixed,
        "per_genus_constraints": per_genus_constraints,
        "branches_by_slot": completed_branches_by_slot,
        "branches_by_genus": completed_branches_by_genus,
        "branch_count": len(completed_branches_by_slot),
    }


def verify_mc2_completion_clutching_scaffold() -> Dict[str, bool]:
    """Wave-54 surrogate checks for completion and first clutching compatibility."""
    model = build_mc2_cyclic_linf_model()
    left = {0: {"theta": Rational(1)}, 1: {"theta": Rational(2)}}
    right = {0: {"theta": Rational(3)}, 1: {"theta": Rational(5)}}
    expected_boundary = {
        0: {"omega": Rational(6)},
        1: {"omega": Rational(22)},
        2: {"omega": Rational(20)},
    }
    clutch_ok = verify_boundary_clutching_compatibility(
        model=model,
        boundary_series=expected_boundary,
        left=left,
        right=right,
        max_genus=2,
    )

    alpha_series = {0: {"theta": Rational(1)}, 1: {"theta": Rational(1)}}
    residual = mc_residual_completed_truncated(model, alpha_series=alpha_series, max_genus=2)
    residual_expected = {
        1: {"omega": Rational(-1)},
        2: {"omega": Rational(-2)},
    }
    residual_ok = True
    for g in set(residual) | set(residual_expected):
        if _add(residual.get(g, {}), _scale(-1, residual_expected.get(g, {}))):
            residual_ok = False
            break

    u = {0: {"theta": Rational(1)}, 1: {"theta": Rational(2)}}
    v = {0: {"theta": Rational(3)}, 1: {"theta": Rational(5)}}
    w = {0: {"theta": Rational(7)}}
    x = {0: {"theta": Rational(11)}}
    cyclic_l2_ok = verify_completed_cyclic_l2(model, u, v, w, max_genus=2)
    cyclic_l3_ok = verify_completed_cyclic_l3(model, u, v, w, x, max_genus=2)

    solved = solve_completed_mc_single_basis_truncated(
        model=model,
        basis_element="theta",
        max_genus=2,
        fixed_coefficients={0: Rational(1)},
    )
    completed_solver_branch_ok = bool(solved["solutions"]) and all(
        simplify(sol[sym]) == 0
        for sym in solved["free_parameters"]
        for sol in solved["solutions"]
    )
    recursive = solve_completed_mc_single_basis_recursive(
        model=model,
        basis_element="theta",
        max_genus=4,
        fixed_coefficients={0: Rational(1)},
    )
    recursive_ok = recursive["branch_count"] == 1 and all(
        simplify(recursive["branches"][0][g]) == 0
        for g in (1, 2, 3, 4)
    )

    multi = solve_completed_mc_basis_family_truncated(
        model=model,
        basis_elements=("theta", "omega"),
        max_genus=1,
        fixed_coefficients={(0, "theta"): Rational(1)},
    )
    theta_g1 = multi["parameter_by_slot"][(1, "theta")]
    omega_g0 = multi["parameter_by_slot"][(0, "omega")]
    omega_g1 = multi["parameter_by_slot"][(1, "omega")]
    multi_branch_ok = bool(multi["solutions"]) and all(
        simplify(sol[theta_g1]) == 0
        and simplify(sol[omega_g0] - omega_g0) == 0
        and simplify(sol[omega_g1] - omega_g1) == 0
        for sol in multi["solutions"]
    )
    multi_inconsistent = solve_completed_mc_basis_family_truncated(
        model=model,
        basis_elements=("theta", "omega"),
        max_genus=1,
        fixed_coefficients={(0, "theta"): Rational(2)},
    )
    multi_inconsistent_ok = not multi_inconsistent["solutions"]

    multi_recursive = solve_completed_mc_basis_family_recursive(
        model=model,
        basis_elements=("theta", "omega"),
        max_genus=3,
        fixed_coefficients={(0, "theta"): Rational(1)},
    )
    multi_recursive_branch_ok = (
        multi_recursive["branch_count"] == 1
        and simplify(multi_recursive["branches_by_slot"][0][(0, "theta")] - 1) == 0
        and all(
            simplify(multi_recursive["branches_by_slot"][0][(g, "theta")]) == 0
            for g in (1, 2, 3)
        )
    )

    inconsistent = solve_completed_mc_single_basis_truncated(
        model=model,
        basis_element="theta",
        max_genus=2,
        fixed_coefficients={0: Rational(2)},
    )
    inconsistent_ok = not inconsistent["solutions"]

    obstruction_identity_ok = verify_genus_stratified_obstruction_identity(
        model=model,
        alpha_series={
            1: {"theta": Rational(1)},
            2: {"theta": Rational(1)},
            3: {"theta": Rational(2)},
        },
        max_genus=3,
    )
    shifted_norm_ok = all(verify_mc2_shifted_seed_one_channel_normalization().values())
    shifted_scaling_ok = all(verify_mc2_shifted_seed_eta_scaling_law().values())
    shifted_poly_ok = all(verify_mc2_shifted_seed_obstruction_polynomial_law().values())
    shifted_sl3_ok = all(verify_mc2_sl3_shifted_seed_nontrivial_mc().values())
    shifted_sp4_ok = all(verify_mc2_sp4_shifted_seed_nontrivial_mc().values())

    return {
        "completed_tensor_surrogate_nonempty": bool(
            completed_tensor_product_surrogate(left, right, max_genus=2)
        ),
        "clutching_boundary_match": clutch_ok,
        "completed_mc_residual_matches_expected": residual_ok,
        "completed_cyclic_l2_match": cyclic_l2_ok,
        "completed_cyclic_l3_match": cyclic_l3_ok,
        "completed_mc_solver_branch_a0_eq_1": completed_solver_branch_ok,
        "completed_mc_recursive_branch_a0_eq_1": recursive_ok,
        "completed_mc_multi_basis_branch_theta_forced": multi_branch_ok,
        "completed_mc_multi_basis_inconsistent_detected": multi_inconsistent_ok,
        "completed_mc_multi_basis_recursive_theta_forced": multi_recursive_branch_ok,
        "completed_mc_inconsistent_a0_eq_2_detected": inconsistent_ok,
        "genus_stratified_obstruction_identity": obstruction_identity_ok,
        "shifted_seed_one_channel_normalization": shifted_norm_ok,
        "shifted_seed_eta_scaling_law": shifted_scaling_ok,
        "shifted_seed_obstruction_polynomial_law": shifted_poly_ok,
        "shifted_sl3_seed_nontrivial_mc": shifted_sl3_ok,
        "shifted_sp4_seed_nontrivial_mc": shifted_sp4_ok,
    }


def verify_mc2_cyclic_linf_scaffold() -> Dict[str, bool]:
    """Self-consistency checks for the MC2 compute scaffold."""
    dg = build_mc2_coderivation_dg_lie_model()
    linf = build_mc2_cyclic_linf_model()

    mc = solve_mc_single_parameter(linf)
    t = mc["parameter"]
    residual = mc["residual"]

    residual_at_0 = {k: simplify(v.subs({t: 0})) for k, v in residual.items()}
    residual_at_1 = {k: simplify(v.subs({t: 1})) for k, v in residual.items()}

    cyclic_l2 = simplify(
        linf.pairing_vectors(linf.l2_basis("theta", "theta"), {"theta": 1})
        - linf.pairing_vectors({"theta": 1}, linf.l2_basis("theta", "theta"))
    ) == 0
    cyclic_l3 = simplify(
        linf.pairing_vectors(linf.l3_basis("theta", "theta", "theta"), {"theta": 1})
        - linf.pairing_vectors({"theta": 1}, linf.l3_basis("theta", "theta", "theta"))
    ) == 0

    pairing_matrix = Matrix(
        [[linf.pairing_basis(a, b) for b in linf.basis] for a in linf.basis]
    )

    return {
        "dg_lie_d_squared_zero": dg.verify_d_squared_zero(),
        "dg_lie_jacobi": dg.verify_jacobi_identity(),
        "dg_lie_leibniz": dg.verify_d_leibniz(),
        "cyclic_pairing_nondegenerate": pairing_matrix.det() != 0,
        "cyclic_l2_on_theta": cyclic_l2,
        "cyclic_l3_on_theta": cyclic_l3,
        "mc_residual_at_0": all(v == 0 for v in residual_at_0.values()),
        "mc_residual_at_1": all(v == 0 for v in residual_at_1.values()),
        "mc_solver_finds_0_1": set(mc["solutions"]) == {Rational(0), Rational(1)},
    }


def verify_mc2_sl2_seed_from_bar() -> Dict[str, bool]:
    """Consistency checks for the bar-derived ``sl_2`` MC2 seed."""
    dg = build_mc2_sl2_coderivation_seed()
    linf = build_mc2_sl2_cyclic_linf_seed()

    pairing_matrix = Matrix(
        [[linf.pairing_basis(a, b) for b in linf.basis] for a in linf.basis]
    )
    ad_invariance = True
    for a in linf.basis:
        for b in linf.basis:
            for c in linf.basis:
                lhs = linf.pairing_vectors(dg.bracket_basis(a, b), {c: 1})
                rhs = linf.pairing_vectors({a: 1}, dg.bracket_basis(b, c))
                if simplify(lhs - rhs) != 0:
                    ad_invariance = False
                    break
            if not ad_invariance:
                break
        if not ad_invariance:
            break

    return {
        "sl2_seed_d_squared_zero": dg.verify_d_squared_zero(),
        "sl2_seed_jacobi": dg.verify_jacobi_identity(),
        "sl2_seed_leibniz": dg.verify_d_leibniz(),
        "sl2_seed_bracket_ef_h": dg.bracket_basis("e", "f") == {"h": Rational(1)},
        "sl2_seed_bracket_he_2e": dg.bracket_basis("h", "e") == {"e": Rational(2)},
        "sl2_seed_bracket_hf_minus2f": dg.bracket_basis("h", "f") == {"f": Rational(-2)},
        "sl2_seed_pairing_ef_1": simplify(linf.pairing_basis("e", "f") - 1) == 0,
        "sl2_seed_pairing_hh_2": simplify(linf.pairing_basis("h", "h") - 2) == 0,
        "sl2_seed_pairing_nondegenerate": simplify(pairing_matrix.det()) != 0,
        "sl2_seed_pairing_ad_invariant": ad_invariance,
    }


def verify_mc2_sl2_l3_seed() -> Dict[str, bool]:
    """Consistency checks for the first nontrivial ``l_3`` sl2 seed."""
    model = build_mc2_sl2_cyclic_linf_l3_seed()
    params, residual = mc_residual_three_parameter(model)
    x, y, z = params

    phi = lambda a, b, c: simplify(model.l3_basis(a, b, c).get("eta", 0))
    l2 = lambda a, b: model.l2_basis(a, b)

    # Chevalley-Eilenberg 3-cocycle closure on the sl2 basis.
    sl2_basis = ("e", "h", "f")
    cocycle_closed = True
    for a, b, c, d in product(sl2_basis, repeat=4):
        delta = 0
        for x0, coeff in l2(a, b).items():
            delta += coeff * phi(x0, c, d)
        for x0, coeff in l2(a, c).items():
            delta -= coeff * phi(x0, b, d)
        for x0, coeff in l2(a, d).items():
            delta += coeff * phi(x0, b, c)
        for x0, coeff in l2(b, c).items():
            delta += coeff * phi(x0, a, d)
        for x0, coeff in l2(b, d).items():
            delta -= coeff * phi(x0, a, c)
        for x0, coeff in l2(c, d).items():
            delta += coeff * phi(x0, a, b)
        if simplify(delta) != 0:
            cocycle_closed = False
            break

    eta_residual = simplify(residual.get("eta", 0))
    return {
        "sl2_l3_seed_nontrivial_channel": phi("e", "h", "f") != 0,
        "sl2_l3_seed_antisymmetry": simplify(phi("e", "h", "f") + phi("h", "e", "f")) == 0,
        "sl2_l3_seed_ce_closed": cocycle_closed,
        "sl2_l3_mc_residual_nonzero_generic": eta_residual != 0,
        "sl2_l3_mc_residual_eta_only": set(residual.keys()) == {"eta"},
        "sl2_l3_mc_residual_axis_x0": simplify(eta_residual.subs({x: 0})) == 0,
        "sl2_l3_mc_residual_axis_y0": simplify(eta_residual.subs({y: 0})) == 0,
        "sl2_l3_mc_residual_axis_z0": simplify(eta_residual.subs({z: 0})) == 0,
        "sl2_l3_mc_residual_nonzero_at_111": simplify(eta_residual.subs({x: 1, y: 1, z: 1})) != 0,
    }


def verify_mc2_sl2_shifted_seed_nontrivial_mc() -> Dict[str, bool]:
    """Checks nontrivial completed-MC channels on shifted symmetric ``sl_2`` seed."""
    model = build_mc2_sl2_shifted_cyclic_linf_l3_seed()
    params, residual = mc_residual_three_parameter(model)
    x, y, z = params
    eta_residual = simplify(residual.get("eta", 0))

    alpha = {1: {"e": Rational(1), "h": Rational(1), "f": Rational(1)}}
    obstruction_g2 = completed_mc_obstruction_term_at_genus(
        model=model,
        alpha_series=alpha,
        genus=2,
        require_zero_genus=True,
    )
    obstruction_g3 = completed_mc_obstruction_term_at_genus(
        model=model,
        alpha_series=alpha,
        genus=3,
        require_zero_genus=True,
    )

    return {
        "shifted_seed_mc_residual_eta_only": set(residual) == {"eta"},
        "shifted_seed_mc_residual_eta_nonzero": eta_residual != 0,
        "shifted_seed_mc_residual_eta_at_111": simplify(eta_residual.subs({x: 1, y: 1, z: 1})) == -2,
        "shifted_seed_obstruction_g2_nonzero": bool(obstruction_g2),
        "shifted_seed_obstruction_g3_equals_eta_minus2": obstruction_g3 == {"eta": Rational(-2)},
        "shifted_seed_obstruction_identity": verify_genus_stratified_obstruction_identity(
            model=model,
            alpha_series=alpha,
            max_genus=3,
        ),
    }


def _verify_shifted_seed_nontrivial_mc_bundle(
    model: CyclicLInfinityModel,
    basis_elements: Tuple[str, str, str],
    alpha_series: Mapping[int, Mapping[str, object]],
    expected_eta_at_111: object,
    expected_obstruction_g3: Mapping[str, object],
    expected_obstruction_g2: Mapping[str, object] | None = None,
) -> Dict[str, bool]:
    """Shared shifted-seed nontriviality checks for rank/type variants."""
    params, residual = mc_residual_three_parameter(model, basis_elements=basis_elements)
    x, y, z = params
    eta_residual = simplify(residual.get("eta", 0))

    obstruction_g2 = completed_mc_obstruction_term_at_genus(
        model=model,
        alpha_series=alpha_series,
        genus=2,
        require_zero_genus=True,
    )
    obstruction_g3 = completed_mc_obstruction_term_at_genus(
        model=model,
        alpha_series=alpha_series,
        genus=3,
        require_zero_genus=True,
    )

    checks: Dict[str, bool] = {
        "mc_residual_eta_only": set(residual) == {"eta"},
        "mc_residual_eta_nonzero": eta_residual != 0,
        "mc_residual_eta_at_111": simplify(eta_residual.subs({x: 1, y: 1, z: 1}))
        == simplify(expected_eta_at_111),
        "mc_residual_axis_x0": simplify(eta_residual.subs({x: 0})) == 0,
        "mc_residual_axis_y0": simplify(eta_residual.subs({y: 0})) == 0,
        "mc_residual_axis_z0": simplify(eta_residual.subs({z: 0})) == 0,
        "obstruction_g2_nonzero": bool(obstruction_g2),
        "obstruction_g3_expected": obstruction_g3
        == {key: simplify(value) for key, value in expected_obstruction_g3.items()},
        "obstruction_identity": verify_genus_stratified_obstruction_identity(
            model=model,
            alpha_series=alpha_series,
            max_genus=3,
        ),
    }
    if expected_obstruction_g2 is not None:
        checks["obstruction_g2_expected"] = obstruction_g2 == {
            key: simplify(value) for key, value in expected_obstruction_g2.items()
        }
    return checks


def shifted_seed_eta_channel_normalization_profile(
    model: CyclicLInfinityModel,
    *,
    basis_elements: Tuple[str, str, str],
    alpha_series: Mapping[int, Mapping[str, object]],
    obstruction_genus: int = 3,
) -> Dict[str, object]:
    """Extract the single-channel shifted-seed normalization profile."""
    if obstruction_genus < 2:
        raise ValueError("obstruction_genus must be at least 2")

    params, residual = mc_residual_three_parameter(model, basis_elements=basis_elements)
    x, y, z = params
    eta_residual = simplify(residual.get("eta", 0))
    eta_at_111 = simplify(eta_residual.subs({x: 1, y: 1, z: 1}))

    obstruction = completed_mc_obstruction_term_at_genus(
        model=model,
        alpha_series=alpha_series,
        genus=obstruction_genus,
        require_zero_genus=True,
    )
    obstruction_eta = simplify(obstruction.get("eta", 0))

    ratio = None
    if eta_at_111 != 0:
        ratio = simplify(obstruction_eta / eta_at_111)

    return {
        "eta_residual_at_111": eta_at_111,
        "obstruction_eta": obstruction_eta,
        "normalization_ratio": ratio,
        "residual_support": tuple(sorted(residual.keys())),
        "obstruction_support": tuple(sorted(obstruction.keys())),
        "obstruction": obstruction,
    }


def shifted_seed_eta_channel_scaling_profile(
    model: CyclicLInfinityModel,
    *,
    basis_elements: Tuple[str, str, str],
    alpha_basis: Tuple[str, ...],
    parameter_name: str = "t",
) -> Dict[str, object]:
    """Extract symbolic quadratic/cubic scaling profile of shifted obstructions."""
    t = Symbol(parameter_name)
    alpha_series = {1: {name: t for name in alpha_basis}}

    params, residual = mc_residual_three_parameter(model, basis_elements=basis_elements)
    x, y, z = params
    eta_at_111 = simplify(residual.get("eta", 0).subs({x: 1, y: 1, z: 1}))

    obstruction_g2 = completed_mc_obstruction_term_at_genus(
        model=model,
        alpha_series=alpha_series,
        genus=2,
        require_zero_genus=True,
    )
    obstruction_g3 = completed_mc_obstruction_term_at_genus(
        model=model,
        alpha_series=alpha_series,
        genus=3,
        require_zero_genus=True,
    )

    g2_normalized = {name: simplify(value / (t**2)) for name, value in obstruction_g2.items()}
    g3_normalized = {name: simplify(value / (t**3)) for name, value in obstruction_g3.items()}

    return {
        "parameter": t,
        "eta_residual_at_111": eta_at_111,
        "obstruction_g2": obstruction_g2,
        "obstruction_g3": obstruction_g3,
        "obstruction_g2_normalized": g2_normalized,
        "obstruction_g3_normalized": g3_normalized,
    }


def shifted_seed_obstruction_polynomial_profile(
    model: CyclicLInfinityModel,
    *,
    basis_elements: Tuple[str, str, str],
) -> Dict[str, object]:
    """Extract symbolic polynomial identities for shifted genus-2/genus-3 obstructions."""
    (x, y, z), residual = mc_residual_three_parameter(model, basis_elements=basis_elements)
    alpha1 = {
        basis_elements[0]: x,
        basis_elements[1]: y,
        basis_elements[2]: z,
    }
    alpha_series = {1: alpha1}

    obstruction_g2 = completed_mc_obstruction_term_at_genus(
        model=model,
        alpha_series=alpha_series,
        genus=2,
        require_zero_genus=True,
    )
    obstruction_g3 = completed_mc_obstruction_term_at_genus(
        model=model,
        alpha_series=alpha_series,
        genus=3,
        require_zero_genus=True,
    )
    half_l2 = _scale(Rational(1, 2), model.l2_vectors(alpha1, alpha1))
    one_sixth_l3 = _scale(Rational(1, 6), model.l3_vectors(alpha1, alpha1, alpha1))

    return {
        "parameters": (x, y, z),
        "alpha1": alpha1,
        "eta_residual": simplify(residual.get("eta", 0)),
        "obstruction_g2": obstruction_g2,
        "obstruction_g3": obstruction_g3,
        "half_l2_alpha1_alpha1": half_l2,
        "one_sixth_l3_alpha1_alpha1_alpha1": one_sixth_l3,
    }


def mc2_shifted_seed_one_channel_normalization_profiles() -> Dict[str, Dict[str, object]]:
    """Collect shifted-seed one-channel profiles across ``sl_2``, ``sl_3``, ``sp_4``."""
    return {
        "sl2": shifted_seed_eta_channel_normalization_profile(
            build_mc2_sl2_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e", "h", "f"),
            alpha_series={1: {"e": Rational(1), "h": Rational(1), "f": Rational(1)}},
        ),
        "sl3": shifted_seed_eta_channel_normalization_profile(
            build_mc2_sl3_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e1", "e2", "f12"),
            alpha_series={1: {"e1": Rational(1), "e2": Rational(1), "f12": Rational(1)}},
        ),
        "sp4": shifted_seed_eta_channel_normalization_profile(
            build_mc2_sp4_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e1", "e2", "f12"),
            alpha_series={1: {"e1": Rational(1), "e2": Rational(1), "f12": Rational(1)}},
        ),
    }


def verify_mc2_shifted_seed_one_channel_normalization() -> Dict[str, bool]:
    """Check shifted-seed one-channel normalization consistency across types."""
    profiles = mc2_shifted_seed_one_channel_normalization_profiles()
    expected = {
        "sl2": Rational(-2),
        "sl3": Rational(1),
        "sp4": Rational(2),
    }

    checks: Dict[str, bool] = {}
    ratios = []
    for key, expected_eta in expected.items():
        profile = profiles[key]
        eta_at_111 = simplify(profile["eta_residual_at_111"])
        obstruction_eta = simplify(profile["obstruction_eta"])
        ratio = profile["normalization_ratio"]

        checks[f"{key}_residual_eta_expected"] = eta_at_111 == expected_eta
        checks[f"{key}_obstruction_eta_expected"] = obstruction_eta == expected_eta
        checks[f"{key}_residual_eta_only"] = profile["residual_support"] == ("eta",)
        checks[f"{key}_obstruction_eta_only"] = profile["obstruction_support"] == ("eta",)
        checks[f"{key}_normalization_ratio_defined"] = ratio is not None
        checks[f"{key}_normalization_ratio_one"] = ratio is not None and simplify(ratio - 1) == 0
        if ratio is not None:
            ratios.append(simplify(ratio))

    checks["normalization_ratio_uniform"] = (
        len(ratios) == len(expected) and len(set(ratios)) == 1
    )
    return checks


def verify_mc2_shifted_seed_eta_scaling_law() -> Dict[str, bool]:
    """Verify quadratic/cubic shifted-obstruction scaling across rank/type lanes."""
    expected_eta = {"sl2": Rational(-2), "sl3": Rational(1), "sp4": Rational(2)}
    profiles = {
        "sl2": shifted_seed_eta_channel_scaling_profile(
            build_mc2_sl2_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e", "h", "f"),
            alpha_basis=("e", "h", "f"),
        ),
        "sl3": shifted_seed_eta_channel_scaling_profile(
            build_mc2_sl3_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e1", "e2", "f12"),
            alpha_basis=("e1", "e2", "f12"),
        ),
        "sp4": shifted_seed_eta_channel_scaling_profile(
            build_mc2_sp4_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e1", "e2", "f12"),
            alpha_basis=("e1", "e2", "f12"),
        ),
    }

    checks: Dict[str, bool] = {}
    for key, profile in profiles.items():
        t = profile["parameter"]
        eta111 = simplify(profile["eta_residual_at_111"])
        g2 = profile["obstruction_g2"]
        g3 = profile["obstruction_g3"]
        g2_normalized = profile["obstruction_g2_normalized"]
        g3_normalized = profile["obstruction_g3_normalized"]
        g3_eta = simplify(g3.get("eta", 0))

        checks[f"{key}_eta111_expected"] = eta111 == expected_eta[key]
        checks[f"{key}_g2_nonzero"] = bool(g2)
        checks[f"{key}_g3_eta_only"] = set(g3) == {"eta"}
        checks[f"{key}_g2_quadratic_scaling"] = all(
            simplify(value - (t**2) * g2_normalized[name]) == 0
            for name, value in g2.items()
        )
        checks[f"{key}_g3_cubic_scaling"] = simplify(g3_eta - (t**3) * g3_normalized["eta"]) == 0
        checks[f"{key}_g3_eta_matches_eta111_cubic"] = simplify(g3_eta - eta111 * (t**3)) == 0
        checks[f"{key}_g3_normalized_eta_expected"] = simplify(g3_normalized.get("eta", 0) - eta111) == 0

    return checks


def verify_mc2_shifted_seed_obstruction_polynomial_law() -> Dict[str, bool]:
    """Verify symbolic polynomial obstruction identities on shifted seeds."""
    s = Symbol("s")
    profiles = {
        "sl2": shifted_seed_obstruction_polynomial_profile(
            build_mc2_sl2_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e", "h", "f"),
        ),
        "sl3": shifted_seed_obstruction_polynomial_profile(
            build_mc2_sl3_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e1", "e2", "f12"),
        ),
        "sp4": shifted_seed_obstruction_polynomial_profile(
            build_mc2_sp4_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e1", "e2", "f12"),
        ),
    }

    checks: Dict[str, bool] = {}
    for key, profile in profiles.items():
        x, y, z = profile["parameters"]
        eta_residual = simplify(profile["eta_residual"])
        obstruction_g2 = profile["obstruction_g2"]
        obstruction_g3 = profile["obstruction_g3"]
        half_l2 = profile["half_l2_alpha1_alpha1"]
        one_sixth_l3 = profile["one_sixth_l3_alpha1_alpha1_alpha1"]
        g3_eta = simplify(obstruction_g3.get("eta", 0))

        g2_match = all(
            simplify(obstruction_g2.get(name, 0) - half_l2.get(name, 0)) == 0
            for name in set(obstruction_g2) | set(half_l2)
        )
        g3_match = all(
            simplify(obstruction_g3.get(name, 0) - one_sixth_l3.get(name, 0)) == 0
            for name in set(obstruction_g3) | set(one_sixth_l3)
        )

        checks[f"{key}_g2_equals_half_l2"] = g2_match
        checks[f"{key}_g3_equals_one_sixth_l3"] = g3_match
        checks[f"{key}_g3_eta_equals_residual_eta"] = simplify(g3_eta - eta_residual) == 0
        checks[f"{key}_g3_eta_only"] = set(obstruction_g3) == {"eta"}
        checks[f"{key}_eta_residual_homogeneous_deg3"] = simplify(
            eta_residual.subs({x: s * x, y: s * y, z: s * z}) - s**3 * eta_residual
        ) == 0
        checks[f"{key}_g2_homogeneous_deg2"] = all(
            simplify(value.subs({x: s * x, y: s * y, z: s * z}) - s**2 * value) == 0
            for value in obstruction_g2.values()
        )
        checks[f"{key}_g3_homogeneous_deg3"] = all(
            simplify(value.subs({x: s * x, y: s * y, z: s * z}) - s**3 * value) == 0
            for value in obstruction_g3.values()
        )

    return checks


def verify_mc2_sl3_shifted_seed_nontrivial_mc() -> Dict[str, bool]:
    """Shifted-seed nontrivial completed-MC checks for ``sl_3``."""
    return _verify_shifted_seed_nontrivial_mc_bundle(
        model=build_mc2_sl3_shifted_cyclic_linf_l3_seed(),
        basis_elements=("e1", "e2", "f12"),
        alpha_series={1: {"e1": Rational(1), "e2": Rational(1), "f12": Rational(1)}},
        expected_eta_at_111=Rational(1),
        expected_obstruction_g3={"eta": Rational(1)},
        expected_obstruction_g2={
            "e12": Rational(1),
            "f1": Rational(1),
            "f2": Rational(-1),
        },
    )


def verify_mc2_sp4_shifted_seed_nontrivial_mc() -> Dict[str, bool]:
    """Shifted-seed nontrivial completed-MC checks for ``sp_4``."""
    return _verify_shifted_seed_nontrivial_mc_bundle(
        model=build_mc2_sp4_shifted_cyclic_linf_l3_seed(),
        basis_elements=("e1", "e2", "f12"),
        alpha_series={1: {"e1": Rational(1), "e2": Rational(1), "f12": Rational(1)}},
        expected_eta_at_111=Rational(2),
        expected_obstruction_g3={"eta": Rational(2)},
        expected_obstruction_g2={
            "e12": Rational(1),
            "f1": Rational(1),
            "f2": Rational(-2),
        },
    )


# ---------------------------------------------------------------------------
# Step 3: Kappa extraction from cyclic L-infinity seed
# ---------------------------------------------------------------------------


def _pairing_inverse_dual_basis(
    pairing_table: Mapping[Tuple[str, str], object],
    basis: Tuple[str, ...],
) -> Dict[str, Vector]:
    """Compute the dual basis {e^i} with <e^i, e_j> = delta_{ij}.

    Returns a map: basis_element -> its dual expressed in the same basis.
    """
    n = len(basis)
    gram = Matrix(n, n, lambda i, j: simplify(pairing_table.get((basis[i], basis[j]), 0)))
    gram_inv = gram.inv()
    dual: Dict[str, Vector] = {}
    for j in range(n):
        v: Vector = {}
        for i in range(n):
            coeff = simplify(gram_inv[i, j])
            if coeff != 0:
                v[basis[i]] = coeff
        dual[basis[j]] = v
    return dual


def adjoint_casimir_matrix(model: CyclicLInfinityModel) -> Matrix:
    """Compute the adjoint Casimir C_2 matrix on the model's basis.

    C_2(X) = sum_i [e_i, [e^i, X]] where {e^i} is the pairing-dual basis.
    Returns the matrix representation in the model's basis.
    """
    basis = model.basis
    n = len(basis)
    dual = _pairing_inverse_dual_basis(model.pairing_table, basis)

    mat = Matrix(n, n, lambda *_: 0)
    for col_idx, x in enumerate(basis):
        # C_2(x) = sum_i [e_i, [e^i, x]]
        c2_x: Vector = {}
        for i, ei in enumerate(basis):
            ei_dual = dual[ei]
            # [e^i, x]
            inner = model.l2_vectors(ei_dual, {x: 1})
            # [e_i, inner]
            outer = model.l2_vectors({ei: 1}, inner)
            c2_x = _add(c2_x, outer)
        for row_idx, y in enumerate(basis):
            mat[row_idx, col_idx] = simplify(c2_x.get(y, 0))
    return mat


def adjoint_casimir_eigenvalue(model: CyclicLInfinityModel) -> object:
    """Extract the Casimir eigenvalue on the adjoint representation.

    For a simple Lie algebra with the normalized Killing pairing,
    C_2 = 2*h^vee * id on the adjoint.  Returns the eigenvalue (which
    should be 2*h^vee for a simple Lie algebra seed).
    """
    mat = adjoint_casimir_matrix(model)
    n = mat.shape[0]
    # Check proportional to identity
    eigenvalue = simplify(mat[0, 0])
    return eigenvalue


def dual_coxeter_from_seed(model: CyclicLInfinityModel) -> object:
    """Extract h^vee = (Casimir eigenvalue) / 2 from the cyclic seed."""
    return simplify(adjoint_casimir_eigenvalue(model) / 2)


def kappa_from_seed(
    model: CyclicLInfinityModel,
    level: object | None = None,
) -> object:
    """Compute kappa = dim(g) * (level + h^vee) / (2 * h^vee) from seed data.

    This is the scalar shadow of the modular characteristic (Theorem D_scal):
    - dim(g) = dimension of the basis
    - h^vee = adjoint Casimir eigenvalue / 2 (from l_2 + pairing)
    - level = the OPE level parameter (from the OPE algebra)

    For sl_2 at level k, this should give 3(k+2)/4.
    """
    if level is None:
        level = Symbol("k")
    h_dual = dual_coxeter_from_seed(model)
    dim_g = len(model.basis)
    return simplify(dim_g * (level + h_dual) / (2 * h_dual))


def kappa_two_channel(
    model: CyclicLInfinityModel,
    level: object | None = None,
) -> Dict[str, object]:
    """Decompose kappa into double-pole and simple-pole channels.

    Returns: {
        "double_pole": dim(g) * level / (2 * h^vee),
        "simple_pole": dim(g) / 2,
        "total": dim(g) * (level + h^vee) / (2 * h^vee),
    }

    This mirrors the two-channel genus-2 curvature proof in
    Theorem thm:sl2-genus2-curvature.
    """
    if level is None:
        level = Symbol("k")
    h_dual = dual_coxeter_from_seed(model)
    dim_g = len(model.basis)
    double = simplify(dim_g * level / (2 * h_dual))
    simple = simplify(Rational(dim_g, 2))
    total = simplify(double + simple)
    return {
        "double_pole": double,
        "simple_pole": simple,
        "total": total,
        "h_dual": h_dual,
        "dim_g": dim_g,
    }


# ---------------------------------------------------------------------------
# L-infinity arity-4 homotopy Jacobi
# ---------------------------------------------------------------------------


def _koszul_sign_4_shuffle(sigma: Tuple[int, ...], degrees: Tuple[int, ...]) -> int:
    """Koszul sign for a permutation of 4 elements with given degrees."""
    # Count inversions weighted by degrees
    sign = 0
    for i in range(len(sigma)):
        for j in range(i + 1, len(sigma)):
            if sigma[i] > sigma[j]:
                sign += degrees[sigma[i]] * degrees[sigma[j]]
    return (-1) ** sign


def verify_linf_arity4_identity(model: CyclicLInfinityModel) -> bool:
    r"""Verify the L-infinity homotopy Jacobi identity at arity 4.

    For l_1=0, the identity at arity 4 reads:
        sum_{(2,2)-shuffles} +/- l_2(l_2(a_s1, a_s2), a_s3, a_s4)
      + sum_{(1,3)-shuffles} +/- l_2(l_3(a_s1, a_s2, a_s3), a_s4)
      + sum_{(3,1)-shuffles} +/- l_3(l_2(a_s1, a_s2), a_s3, a_s4)
      + l_4(a, b, c, d) = 0

    With l_4 = 0 and l_1 = 0, and for degree-0 generators, this reduces to:
    - The ordinary Jacobi identity for l_2 (already verified),
    - Plus l_2(l_3(...), -) + l_3(l_2(...), -, -) terms.
    """
    basis = model.basis
    for a, b, c, d in product(basis, repeat=4):
        # Term 1: sum over (2,2)-shuffles of l_2(l_2(a_i, a_j), l_2(a_k, a_l))
        # For degree-0 elements, this is:
        # l_2(l_2(a,b), l_2(c,d)) + permutations
        # But actually the arity-4 relation involves nesting, not products.
        # The correct form with l_4 = 0, l_1 = 0:
        # sum_{sigma in Sh(1,3)} eps(sigma) l_2(a_s1, l_3(a_s2, a_s3, a_s4))
        # + sum_{sigma in Sh(2,2)} eps(sigma) l_3(l_2(a_s1, a_s2), a_s3, a_s4) = 0
        #
        # For degree-0 basis, all Koszul signs are +1.

        total: Vector = {}

        # l_2(a, l_3(b, c, d)) - l_2(b, l_3(a, c, d)) + l_2(c, l_3(a, b, d)) - l_2(d, l_3(a, b, c))
        for i, x in enumerate((a, b, c, d)):
            rest = [y for j, y in enumerate((a, b, c, d)) if j != i]
            sign = (-1) ** i
            l3_val = model.l3_vectors({rest[0]: 1}, {rest[1]: 1}, {rest[2]: 1})
            term = _scale(sign, model.l2_vectors({x: 1}, l3_val))
            total = _add(total, term)

        # l_3(l_2(a,b), c, d) - l_3(l_2(a,c), b, d) + l_3(l_2(a,d), b, c)
        # + l_3(l_2(b,c), a, d) - l_3(l_2(b,d), a, c) + l_3(l_2(c,d), a, b)
        elems = (a, b, c, d)
        for i in range(4):
            for j in range(i + 1, 4):
                rest = [elems[m] for m in range(4) if m != i and m != j]
                sign = (-1) ** (i + j + 1)  # (2,2)-shuffle sign for degree 0
                l2_val = model.l2_vectors({elems[i]: 1}, {elems[j]: 1})
                term = _scale(sign, model.l3_vectors(l2_val, {rest[0]: 1}, {rest[1]: 1}))
                total = _add(total, term)

        if total:
            return False
    return True


# ---------------------------------------------------------------------------
# Full cyclic symmetry verification
# ---------------------------------------------------------------------------


def verify_cyclic_l2_full(model: CyclicLInfinityModel) -> bool:
    """Verify <l_2(a,b), c> + <b, l_2(a,c)> = 0 for all triples.

    This is the ad-invariance of the pairing: the l_2 bracket is a
    derivation of the pairing in each argument.
    """
    basis = model.basis
    for a, b, c in product(basis, repeat=3):
        lhs = model.pairing_vectors(model.l2_vectors({a: 1}, {b: 1}), {c: 1})
        rhs = model.pairing_vectors({b: 1}, model.l2_vectors({a: 1}, {c: 1}))
        if simplify(lhs + rhs) != 0:
            return False
    return True


def verify_cyclic_l3_full(model: CyclicLInfinityModel) -> bool:
    r"""Verify structural cyclic properties of l_3.

    For the generator-level l_3 seed (where l_3 output lands in a
    separate degree-2 marker ``eta``), the full 4-form cyclic sum is
    not meaningful because the model is truncated (l_3 involving eta
    as input is not defined).

    Instead we verify two structural properties that ARE meaningful:

    1. **Generator-level cyclic vanishing**: For degree-0 generators
       a, b, c, d, the 4-form <l_3(a,b,c), d> = 0 (since l_3 output
       is in eta, which pairs trivially with generators).

    2. **Total antisymmetry of the Killing cocycle**: The restriction
       phi(a,b,c) = <l_3(a,b,c), eta> is totally antisymmetric in
       (a,b,c) for degree-0 generators.

    Together with the CE cocycle closure (verified in ``verify_mc2_sl2_l3_seed``),
    these ensure that the l_3 data carries the correct algebraic structure.
    """
    basis = model.basis
    # Identify degree-0 generators vs higher-degree markers
    gen_basis = tuple(b for b in basis if model.degrees.get(b, 0) == 0)

    # Property 1: generator-level 4-form vanishes
    for a, b, c, d in product(gen_basis, repeat=4):
        val = model.pairing_vectors(model.l3_vectors({a: 1}, {b: 1}, {c: 1}), {d: 1})
        if simplify(val) != 0:
            return False

    # Property 2: total antisymmetry of phi(a,b,c) = <l_3(a,b,c), eta>
    # where eta is any degree-2 marker with self-pairing
    marker_basis = [b for b in basis if model.degrees.get(b, 0) != 0]
    for marker in marker_basis:
        for a, b, c in product(gen_basis, repeat=3):
            phi_abc = model.pairing_vectors(
                model.l3_vectors({a: 1}, {b: 1}, {c: 1}), {marker: 1}
            )
            phi_bac = model.pairing_vectors(
                model.l3_vectors({b: 1}, {a: 1}, {c: 1}), {marker: 1}
            )
            phi_acb = model.pairing_vectors(
                model.l3_vectors({a: 1}, {c: 1}, {b: 1}), {marker: 1}
            )
            # Antisymmetry in first two args
            if simplify(phi_abc + phi_bac) != 0:
                return False
            # Antisymmetry in last two args
            if simplify(phi_abc + phi_acb) != 0:
                return False

    return True


# ---------------------------------------------------------------------------
# Comprehensive MC2 Step-3 verification
# ---------------------------------------------------------------------------


def verify_mc2_kappa_extraction() -> Dict[str, object]:
    """Full kappa extraction verification for the sl_2 cyclic L-infinity seed.

    This is the core MC2 Step-3 deliverable: showing that the scalar shadow
    kappa(A) is recoverable from the cyclic L-infinity data.
    """
    k = Symbol("k")
    algebra = sl2_algebra(k)
    model = build_mc2_sl2_cyclic_linf_seed()

    # Casimir computation
    c2_mat = adjoint_casimir_matrix(model)
    c2_eigen = adjoint_casimir_eigenvalue(model)
    c2_is_scalar = simplify(c2_mat - c2_eigen * Matrix.eye(3)) == Matrix.zeros(3, 3)

    # h^vee extraction
    h_dual = dual_coxeter_from_seed(model)

    # kappa extraction
    kappa_val = kappa_from_seed(model, level=k)
    kappa_expected = Rational(3) * (k + 2) / 4

    # Two-channel decomposition
    channels = kappa_two_channel(model, level=k)

    # Verify complementarity: kappa(k) + kappa(-k - 2*h_dual) = 0
    k_dual = -k - 2 * h_dual
    kappa_dual = kappa_from_seed(model, level=k_dual)
    complementarity = simplify(kappa_val + kappa_dual)

    # Critical level: kappa(k = -h_dual) = 0
    kappa_critical = simplify(kappa_val.subs({k: -h_dual}))

    return {
        "casimir_eigenvalue": c2_eigen,
        "casimir_is_scalar": c2_is_scalar,
        "casimir_equals_2h_dual": simplify(c2_eigen - 2 * h_dual) == 0,
        "h_dual": h_dual,
        "h_dual_equals_2": simplify(h_dual - 2) == 0,
        "kappa": kappa_val,
        "kappa_matches_formula": simplify(kappa_val - kappa_expected) == 0,
        "double_pole_channel": channels["double_pole"],
        "double_pole_matches": simplify(channels["double_pole"] - 3 * k / 4) == 0,
        "simple_pole_channel": channels["simple_pole"],
        "simple_pole_matches": simplify(channels["simple_pole"] - Rational(3, 2)) == 0,
        "complementarity_zero": complementarity == 0,
        "critical_level_zero": kappa_critical == 0,
    }


def verify_mc2_linf_identities() -> Dict[str, bool]:
    """Verify all L-infinity structural identities for the l_3 seed."""
    model = build_mc2_sl2_cyclic_linf_l3_seed()

    return {
        "arity4_homotopy_jacobi": verify_linf_arity4_identity(model),
        "cyclic_l2_full": verify_cyclic_l2_full(model),
        "cyclic_l3_full": verify_cyclic_l3_full(model),
    }


# ---------------------------------------------------------------------------
# sp_4 = C_2: non-simply-laced universality test
# ---------------------------------------------------------------------------

_SP4_BASIS = ("e1", "e2", "e12", "e22", "h1", "h2", "f1", "f2", "f12", "f22")
_G2_BASIS = (
    "e1",
    "e2",
    "e12",
    "e112",
    "e1112",
    "e11122",
    "h1",
    "h2",
    "f1",
    "f2",
    "f12",
    "f112",
    "f1112",
    "f11122",
)


def build_mc2_sp4_coderivation_seed() -> CoderivationDGLieModel:
    """Bar-derived dg-Lie seed from ``sp_4`` structure constants.

    sp_4 = C_2 is the simplest non-simply-laced simple Lie algebra,
    with h^vee = 3 != h = 4.  This is the critical test case for
    the universality of the kappa extraction formula across root
    length types.
    """
    c = _sp4_sc()
    bracket = _bracket_table_from_structure_constants(c, _SP4_BASIS)
    return CoderivationDGLieModel(
        basis=_SP4_BASIS,
        degrees={name: 0 for name in _SP4_BASIS},
        differential_table={name: {} for name in _SP4_BASIS},
        bracket_table=bracket,
    )


def build_mc2_sp4_cyclic_linf_seed() -> CyclicLInfinityModel:
    """Bar-derived cyclic ``L_\\infty`` seed from ``sp_4`` structure data.

    Uses the trace form on the 4-dimensional defining representation.
    Non-simply-laced normalization: kap(e_short, f_short) = 2,
    kap(e_long, f_long) = 1.
    """
    c = _sp4_sc()
    kap = _sp4_kf()
    bracket = _bracket_table_from_structure_constants(c, _SP4_BASIS)
    pairing = _pairing_table_from_killing_form(kap, _SP4_BASIS)
    return CyclicLInfinityModel(
        basis=_SP4_BASIS,
        degrees={name: 0 for name in _SP4_BASIS},
        pairing_table=pairing,
        l1_table={name: {} for name in _SP4_BASIS},
        l2_table=bracket,
        l3_table={},
    )


def build_mc2_sp4_cyclic_linf_l3_seed() -> CyclicLInfinityModel:
    """First nontrivial higher-bracket MC2 seed from ``sp_4``.

    The ``l_3`` channel is the Killing 3-cocycle
    ``phi(a,b,c) = < [a,b], c >`` with output in an explicit degree-2
    marker basis element ``eta``.
    """
    return build_cyclic_l3_marker_extension_from_seed(
        build_mc2_sp4_cyclic_linf_seed(),
        marker_name="eta",
        marker_degree=2,
        marker_pairing=Rational(1),
    )


def build_mc2_sp4_shifted_cyclic_linf_l3_seed() -> CyclicLInfinityModel:
    """Suspension-shifted symmetric ``sp_4`` seed with nontrivial MC channels."""
    return build_shifted_symmetric_cyclic_linf_from_seed(
        seed=build_mc2_sp4_cyclic_linf_l3_seed(),
        generator_basis=_SP4_BASIS,
        degree_shift=1,
    )


def verify_mc2_sp4_seed() -> Dict[str, bool]:
    """Structural checks for the bar-derived ``sp_4`` MC2 seed."""
    dg = build_mc2_sp4_coderivation_seed()
    linf = build_mc2_sp4_cyclic_linf_seed()

    pairing_matrix = Matrix(
        [[linf.pairing_basis(a, b) for b in linf.basis] for a in linf.basis]
    )
    ad_invariance = True
    for a in linf.basis:
        for b in linf.basis:
            for c in linf.basis:
                lhs = linf.pairing_vectors(dg.bracket_basis(a, b), {c: 1})
                rhs = linf.pairing_vectors({a: 1}, dg.bracket_basis(b, c))
                if simplify(lhs - rhs) != 0:
                    ad_invariance = False
                    break
            if not ad_invariance:
                break
        if not ad_invariance:
            break

    return {
        "sp4_seed_d_squared_zero": dg.verify_d_squared_zero(),
        "sp4_seed_jacobi": dg.verify_jacobi_identity(),
        "sp4_seed_leibniz": dg.verify_d_leibniz(),
        "sp4_seed_bracket_e1_f1_h1": dg.bracket_basis("e1", "f1") == {"h1": Rational(1)},
        "sp4_seed_bracket_e1_e2_e12": dg.bracket_basis("e1", "e2") == {"e12": Rational(1)},
        "sp4_seed_bracket_e1_e12_2e22": dg.bracket_basis("e1", "e12") == {"e22": Rational(2)},
        "sp4_seed_bracket_h1_e1_2e1": dg.bracket_basis("h1", "e1") == {"e1": Rational(2)},
        "sp4_seed_bracket_h1_e2_minus2e2": dg.bracket_basis("h1", "e2") == {"e2": Rational(-2)},
        "sp4_seed_pairing_e1_f1_2": simplify(linf.pairing_basis("e1", "f1") - 2) == 0,
        "sp4_seed_pairing_e2_f2_1": simplify(linf.pairing_basis("e2", "f2") - 1) == 0,
        "sp4_seed_pairing_h1_h1_4": simplify(linf.pairing_basis("h1", "h1") - 4) == 0,
        "sp4_seed_pairing_h1_h2_minus2": simplify(linf.pairing_basis("h1", "h2") + 2) == 0,
        "sp4_seed_pairing_h2_h2_2": simplify(linf.pairing_basis("h2", "h2") - 2) == 0,
        "sp4_seed_pairing_nondegenerate": simplify(pairing_matrix.det()) != 0,
        "sp4_seed_pairing_ad_invariant": ad_invariance,
    }


def verify_mc2_sp4_kappa_extraction() -> Dict[str, object]:
    """Full kappa extraction verification for the sp_4 cyclic L-infinity seed.

    Expected for sp_4: dim=10, h^vee=3, C_2 eigenvalue=6,
    kappa = 5(k+3)/3, double-pole = 5k/3, simple-pole = 5.

    This is the key non-simply-laced universality check: the formula
    kappa = dim(g) * (k + h^vee) / (2 * h^vee) must work with h^vee
    (dual Coxeter), NOT h (Coxeter number).
    """
    k = Symbol("k")
    model = build_mc2_sp4_cyclic_linf_seed()

    # Casimir computation
    c2_mat = adjoint_casimir_matrix(model)
    c2_eigen = adjoint_casimir_eigenvalue(model)
    from sympy import eye as _eye
    c2_is_scalar = simplify(c2_mat - c2_eigen * _eye(10)) == Matrix.zeros(10, 10)

    # h^vee extraction
    h_dual = dual_coxeter_from_seed(model)

    # kappa extraction
    kappa_val = kappa_from_seed(model, level=k)
    kappa_expected = Rational(5) * (k + 3) / 3

    # Two-channel decomposition
    channels = kappa_two_channel(model, level=k)

    # Complementarity: kappa(k) + kappa(-k - 2*h_dual) = 0
    k_dual = -k - 2 * h_dual
    kappa_dual = kappa_from_seed(model, level=k_dual)
    complementarity = simplify(kappa_val + kappa_dual)

    # Critical level: kappa(k = -h_dual) = 0
    kappa_critical = simplify(kappa_val.subs({k: -h_dual}))

    return {
        "casimir_eigenvalue": c2_eigen,
        "casimir_is_scalar": c2_is_scalar,
        "casimir_equals_2h_dual": simplify(c2_eigen - 2 * h_dual) == 0,
        "h_dual": h_dual,
        "h_dual_equals_3": simplify(h_dual - 3) == 0,
        "kappa": kappa_val,
        "kappa_matches_formula": simplify(kappa_val - kappa_expected) == 0,
        "double_pole_channel": channels["double_pole"],
        "double_pole_matches": simplify(channels["double_pole"] - 5 * k / 3) == 0,
        "simple_pole_channel": channels["simple_pole"],
        "simple_pole_matches": simplify(channels["simple_pole"] - 5) == 0,
        "complementarity_zero": complementarity == 0,
        "critical_level_zero": kappa_critical == 0,
    }


def build_mc2_g2_coderivation_seed() -> CoderivationDGLieModel:
    """Bar-derived dg-Lie seed from ``G_2`` structure constants.

    ``G_2`` is the first exceptional test surface on the MC2 side, with
    ``dim = 14`` and ``h^vee = 4``.
    """
    c = _g2_sc()
    bracket = _bracket_table_from_structure_constants(c, _G2_BASIS)
    return CoderivationDGLieModel(
        basis=_G2_BASIS,
        degrees={name: 0 for name in _G2_BASIS},
        differential_table={name: {} for name in _G2_BASIS},
        bracket_table=bracket,
    )


def build_mc2_g2_cyclic_linf_seed() -> CyclicLInfinityModel:
    """Bar-derived cyclic ``L_\\infty`` seed from ``G_2`` structure data."""
    c = _g2_sc()
    kap = _g2_kf()
    bracket = _bracket_table_from_structure_constants(c, _G2_BASIS)
    pairing = _pairing_table_from_killing_form(kap, _G2_BASIS)
    return CyclicLInfinityModel(
        basis=_G2_BASIS,
        degrees={name: 0 for name in _G2_BASIS},
        pairing_table=pairing,
        l1_table={name: {} for name in _G2_BASIS},
        l2_table=bracket,
        l3_table={},
    )


def build_mc2_g2_cyclic_linf_l3_seed() -> CyclicLInfinityModel:
    """First nontrivial higher-bracket MC2 seed from ``G_2``."""
    return build_cyclic_l3_marker_extension_from_seed(
        build_mc2_g2_cyclic_linf_seed(),
        marker_name="eta",
        marker_degree=2,
        marker_pairing=Rational(1),
    )


def verify_mc2_g2_seed() -> Dict[str, bool]:
    """Structural checks for the bar-derived ``G_2`` MC2 seed."""
    dg = build_mc2_g2_coderivation_seed()
    linf = build_mc2_g2_cyclic_linf_seed()

    pairing_matrix = Matrix(
        [[linf.pairing_basis(a, b) for b in linf.basis] for a in linf.basis]
    )
    ad_invariance = True
    for a in linf.basis:
        for b in linf.basis:
            for c in linf.basis:
                lhs = linf.pairing_vectors(dg.bracket_basis(a, b), {c: 1})
                rhs = linf.pairing_vectors({a: 1}, dg.bracket_basis(b, c))
                if simplify(lhs - rhs) != 0:
                    ad_invariance = False
                    break
            if not ad_invariance:
                break
        if not ad_invariance:
            break

    return {
        "g2_seed_d_squared_zero": dg.verify_d_squared_zero(),
        "g2_seed_jacobi": dg.verify_jacobi_identity(),
        "g2_seed_leibniz": dg.verify_d_leibniz(),
        "g2_seed_bracket_e1_f1_h1": dg.bracket_basis("e1", "f1") == {"h1": Rational(1)},
        "g2_seed_bracket_e2_f2_h2": dg.bracket_basis("e2", "f2") == {"h2": Rational(1)},
        "g2_seed_bracket_e1_e2_e12": dg.bracket_basis("e1", "e2") == {"e12": Rational(1)},
        "g2_seed_bracket_e1_e12_2e112": dg.bracket_basis("e1", "e12") == {"e112": Rational(2)},
        "g2_seed_bracket_e12_e112_minus3e11122": (
            dg.bracket_basis("e12", "e112") == {"e11122": Rational(-3)}
        ),
        "g2_seed_bracket_h1_e2_minus3e2": dg.bracket_basis("h1", "e2") == {"e2": Rational(-3)},
        "g2_seed_pairing_e1_f1_3": simplify(linf.pairing_basis("e1", "f1") - 3) == 0,
        "g2_seed_pairing_e2_f2_1": simplify(linf.pairing_basis("e2", "f2") - 1) == 0,
        "g2_seed_pairing_e12_f12_3": simplify(linf.pairing_basis("e12", "f12") - 3) == 0,
        "g2_seed_pairing_h1_h1_6": simplify(linf.pairing_basis("h1", "h1") - 6) == 0,
        "g2_seed_pairing_h1_h2_minus3": simplify(linf.pairing_basis("h1", "h2") + 3) == 0,
        "g2_seed_pairing_h2_h2_2": simplify(linf.pairing_basis("h2", "h2") - 2) == 0,
        "g2_seed_pairing_nondegenerate": simplify(pairing_matrix.det()) != 0,
        "g2_seed_pairing_ad_invariant": ad_invariance,
    }


def verify_mc2_g2_kappa_extraction() -> Dict[str, object]:
    """Full kappa extraction verification for the ``G_2`` cyclic L-infinity seed."""
    k = Symbol("k")
    model = build_mc2_g2_cyclic_linf_seed()

    c2_mat = adjoint_casimir_matrix(model)
    c2_eigen = adjoint_casimir_eigenvalue(model)
    from sympy import eye as _eye

    c2_is_scalar = simplify(c2_mat - c2_eigen * _eye(14)) == Matrix.zeros(14, 14)

    h_dual = dual_coxeter_from_seed(model)

    kappa_val = kappa_from_seed(model, level=k)
    kappa_expected = Rational(7) * (k + 4) / 4

    channels = kappa_two_channel(model, level=k)

    k_dual = -k - 2 * h_dual
    kappa_dual = kappa_from_seed(model, level=k_dual)
    complementarity = simplify(kappa_val + kappa_dual)

    kappa_critical = simplify(kappa_val.subs({k: -h_dual}))

    return {
        "casimir_eigenvalue": c2_eigen,
        "casimir_is_scalar": c2_is_scalar,
        "casimir_equals_2h_dual": simplify(c2_eigen - 2 * h_dual) == 0,
        "h_dual": h_dual,
        "h_dual_equals_4": simplify(h_dual - 4) == 0,
        "kappa": kappa_val,
        "kappa_matches_formula": simplify(kappa_val - kappa_expected) == 0,
        "double_pole_channel": channels["double_pole"],
        "double_pole_matches": simplify(channels["double_pole"] - 7 * k / 4) == 0,
        "simple_pole_channel": channels["simple_pole"],
        "simple_pole_matches": simplify(channels["simple_pole"] - 7) == 0,
        "complementarity_zero": complementarity == 0,
        "critical_level_zero": kappa_critical == 0,
    }


if __name__ == "__main__":
    checks = verify_mc2_cyclic_linf_scaffold()
    print("=" * 60)
    print("MC2 CYCLIC L-INFINITY SCAFFOLD")
    print("=" * 60)
    for name, ok in checks.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")

    print()
    kappa_checks = verify_mc2_kappa_extraction()
    print("=" * 60)
    print("MC2 KAPPA EXTRACTION (Step 3)")
    print("=" * 60)
    for name, val in kappa_checks.items():
        print(f"  {name}: {val}")

    print()
    linf_checks = verify_mc2_linf_identities()
    print("=" * 60)
    print("MC2 L-INFINITY IDENTITIES")
    print("=" * 60)
    for name, ok in linf_checks.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")

    print()
    completion_checks = verify_mc2_completion_clutching_scaffold()
    print("=" * 60)
    print("MC2 COMPLETION / CLUTCHING SURROGATE")
    print("=" * 60)
    for name, ok in completion_checks.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
