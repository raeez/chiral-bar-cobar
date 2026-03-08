"""MC2 scaffold: coderivation dg-Lie + cyclic L-infinity + first MC solve.

This module provides a finite-dimensional computational template for
Conjecture ``conj:universal-theta`` (MC2), focusing on Step 1 of the
proof strategy in ``rem:mc2-status``:

1. coderivation dg-Lie control object,
2. cyclic L-infinity brackets (low arity),
3. first Maurer-Cartan solver pass in a completed-direction toy model.

The scaffold is intentionally small and symbolic; it is meant to anchor
the pipeline and tests before full geometric input is attached.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Mapping, Tuple

from sympy import Eq, Matrix, Rational, Symbol, solve, simplify

from compute.lib.bar_complex import OPEAlgebra, sl2_algebra

Vector = Dict[str, object]


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


if __name__ == "__main__":
    checks = verify_mc2_cyclic_linf_scaffold()
    print("=" * 60)
    print("MC2 CYCLIC L-INFINITY SCAFFOLD")
    print("=" * 60)
    for name, ok in checks.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
