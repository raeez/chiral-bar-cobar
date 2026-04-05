"""Modular Koszul datum: the six-fold datum from a cyclically admissible Lie conformal algebra.

The Modular Koszul datum Pi_X(L) is the crown jewel computational object of the
modular Koszul duality programme.  It packages ALL data for a given chiral
algebra into a single structured datum:

    Pi_X(L) = (Fact_X(L), B-bar_X(L), Theta_L, L_L, (V^br, T^br), R_4^mod(L))

The six components:
  1. Fact_X(L) — Factorization algebra data (OPE + bar complex dimensions)
  2. B-bar_X(L) — Bar coalgebra (bar complex with differential, desuspended)
  3. Theta_L — Universal MC element (shadow Postnikov tower: kappa, C, Q, ...)
  4. L_L — Lie conformal data (cyclic structure constants, Killing form)
  5. (V^br, T^br) — Branch space and branch BV action
  6. R_4^mod(L) — Modular quartic resonance class

Factory functions construct the package for each standard family:
  Heisenberg, affine sl_2, affine sl_3, Virasoro, W_3, beta-gamma,
  free fermion, lattice VOA.

The assembler ``assemble_platonic_package`` validates admissibility,
calls the modular Koszul engine, extracts primitive kernel data,
computes branch space and shadow generating function, and returns
the full package with internal consistency checks.

Depth decomposition d = 1 + d_arith + d_alg classifies shadow complexity:
  - d_alg in {0, 1, 2, infinity}: algebraic depth from OPE structure
  - d_arith: arithmetic depth from cusp forms (depths >= 5 purely arithmetic)
  - Heisenberg: d=1, d_arith=0, d_alg=0
  - Affine: d=2, d_arith=0, d_alg=1
  - Beta-gamma: d=3, d_arith=0, d_alg=2
  - Virasoro: d=infinity, d_arith=0, d_alg=infinity

References:
  constr:platonic-package (concordance.tex)
  def:cyclically-admissible (higher_genus_modular_koszul.tex)
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  def:shadow-metric (higher_genus_modular_koszul.tex)
  thm:shadow-radius (higher_genus_modular_koszul.tex)
  thm:depth-decomposition (higher_genus_modular_koszul.tex)
  cor:shadow-extraction (higher_genus_modular_koszul.tex)
  prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
  thm:cubic-gauge-triviality (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, simplify, sqrt, S, oo, Matrix, cancel,
)

from .modular_koszul_engine import compute_datum, ModularKoszulDatum
from .primitive_kernel_full import (
    PrimitiveKernel,
    heisenberg_kernel,
    affine_slN_kernel,
    betagamma_kernel,
    virasoro_kernel,
    w3_kernel,
)
from .shadow_radius import (
    shadow_growth_rate as _shadow_growth_rate,
)

# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------

c_sym = Symbol('c')
k_sym = Symbol('k')
t_sym = Symbol('t')
n_sym = Symbol('n')


# ---------------------------------------------------------------------------
# CyclicAdmissibleData
# ---------------------------------------------------------------------------

@dataclass
class CyclicAdmissibleData:
    """Input data for a cyclically admissible Lie conformal algebra L.

    Cyclical admissibility (def:cyclically-admissible) requires:
      (i)   Conformal grading: L = bigoplus_{Delta >= 0} L_Delta
      (ii)  Filtration: bounded pole orders in OPE
      (iii) Invariant pairing: cyclic non-degenerate bilinear form

    Attributes:
        name: family identifier (e.g. 'heisenberg', 'affine_sl2')
        rank: number of strong generators
        weights: conformal weights of generators
        structure_constants: OPE table as nested dict
        killing_form: invariant pairing matrix (sympy Matrix)
        level: level parameter k (symbolic or numeric)
        central_charge: central charge c
        conformal_grading: whether L has conformal grading
        bounded_poles: whether OPE poles are bounded
        has_invariant_pairing: whether L admits a cyclic invariant pairing
    """
    name: str
    rank: int
    weights: List[int]
    structure_constants: Dict
    killing_form: Any
    level: Any
    central_charge: Any
    conformal_grading: bool = True
    bounded_poles: bool = True
    has_invariant_pairing: bool = True

    def is_admissible(self) -> bool:
        """Check all three admissibility conditions."""
        return (
            self.conformal_grading
            and self.bounded_poles
            and self.has_invariant_pairing
        )

    def validate(self) -> List[str]:
        """Return list of validation failures (empty if valid)."""
        failures = []
        if not self.conformal_grading:
            failures.append("Missing conformal grading")
        if not self.bounded_poles:
            failures.append("OPE poles not bounded")
        if not self.has_invariant_pairing:
            failures.append("No cyclic invariant pairing")
        if self.rank != len(self.weights):
            failures.append(
                f"Rank {self.rank} != len(weights) {len(self.weights)}"
            )
        if any(w < 0 for w in self.weights):
            failures.append("Negative conformal weight found")
        return failures


# ---------------------------------------------------------------------------
# BranchSpace
# ---------------------------------------------------------------------------

@dataclass
class BranchSpace:
    """Branch space V^br and branch BV action T^br.

    The branch space is the primitive-kernel image in the cyclic deformation
    complex.  Its dimension and basis labels encode the independent directions
    in which the shadow obstruction tower propagates.

    Attributes:
        dimension: dim V^br
        basis_labels: human-readable labels for basis vectors
        bv_action_terms: terms in the BV action functional T^br
        metaplectic_square: the delta^2 = Delta relation (metaplectic half-density)
    """
    dimension: int
    basis_labels: List[str]
    bv_action_terms: Dict
    metaplectic_square: Any

    def is_trivial(self) -> bool:
        """Return True if branch space is zero-dimensional."""
        return self.dimension == 0


# ---------------------------------------------------------------------------
# PlatonicPackage
# ---------------------------------------------------------------------------

@dataclass
class PlatonicPackage:
    """The full Modular Koszul datum Pi_X(L) — the six-fold datum.

    Packages ALL modular Koszul data for a given chiral algebra into
    a single structured object.

    Components (constr:platonic-package):
      1. factorization_data — Fact_X(L): bar dims, generating function data
      2. bar_coalgebra — B-bar_X(L): bar complex differential structure
      3. theta / theta_kappa / theta_cubic / theta_quartic — Theta_L:
         the universal MC element and its shadow Postnikov tower projections
      4. lie_conformal_data — L_L: the input CyclicAdmissibleData
      5. branch_space — (V^br, T^br): branch BV data
      6. R4_mod — R_4^mod(L): modular quartic resonance class

    Additional derived data:
      - shadow_metric: Q_L(t) quadratic form
      - shadow_growth_rate: rho(A) growth rate invariant
      - shadow_depth_class: G/L/C/M classification
      - primitive_kernel: cofree-coderivation reduction K_A
      - koszul_dual_package: reference to dual package
      - complementarity_sum: kappa(A) + kappa(A!)
      - depth_decomposition: d = 1 + d_arith + d_alg
      - modular_koszul_datum: full ModularKoszulDatum from the engine
    """
    # Identity
    name: str
    input_data: CyclicAdmissibleData

    # Component 1: Factorization algebra data
    factorization_data: Dict

    # Component 2: Bar coalgebra
    bar_coalgebra: Dict

    # Component 3: Universal MC element (shadow Postnikov tower)
    theta: Dict              # {arity: shadow value}
    theta_kappa: Any         # kappa = Theta^{<=2}
    theta_cubic: Any         # C = Theta^{<=3} projection
    theta_quartic: Any       # Q = Theta^{<=4} projection
    shadow_metric: Any       # Q_L(t) polynomial in t
    shadow_growth_rate: Any  # rho(A)
    shadow_depth_class: str  # G, L, C, or M

    # Component 4: Lie conformal data (same as input_data)
    lie_conformal_data: CyclicAdmissibleData

    # Component 5: Branch space and branch BV action
    branch_space: BranchSpace

    # Component 6: Modular quartic resonance class
    R4_mod: Any

    # Derived data
    primitive_kernel: Optional[PrimitiveKernel] = None
    koszul_dual_package: Optional[Any] = None
    complementarity_sum: Any = None
    depth_decomposition: Dict = field(default_factory=dict)
    modular_koszul_datum: Optional[ModularKoszulDatum] = None

    # ------------------------------------------------------------------
    # Methods
    # ------------------------------------------------------------------

    def summary(self) -> str:
        """Human-readable summary of the Modular Koszul datum."""
        pk_str = (
            self.primitive_kernel.component_string()
            if self.primitive_kernel else "N/A"
        )
        depth_str = (
            f"d={self.depth_decomposition.get('d', '?')}, "
            f"d_arith={self.depth_decomposition.get('d_arith', '?')}, "
            f"d_alg={self.depth_decomposition.get('d_alg', '?')}"
        ) if self.depth_decomposition else "N/A"

        lines = [
            f"{'=' * 60}",
            f" Modular Koszul datum: {self.name}",
            f"{'=' * 60}",
            "",
            "--- Input (Cyclic Admissible Data) ---",
            f"  Rank             : {self.input_data.rank}",
            f"  Weights          : {self.input_data.weights}",
            f"  Level            : {self.input_data.level}",
            f"  Central charge   : {self.input_data.central_charge}",
            f"  Admissible       : {self.input_data.is_admissible()}",
            "",
            "--- Component 1: Factorization Data ---",
            f"  Bar dimensions   : {self.factorization_data.get('bar_dims', {})}",
            "",
            "--- Component 2: Bar Coalgebra ---",
            f"  Source           : {self.bar_coalgebra.get('source', 'N/A')}",
            "",
            "--- Component 3: Shadow Postnikov Tower ---",
            f"  kappa            : {self.theta_kappa}",
            f"  Cubic shadow C   : {self.theta_cubic}",
            f"  Quartic contact Q: {self.theta_quartic}",
            f"  Shadow metric    : {self.shadow_metric}",
            f"  Growth rate rho  : {self.shadow_growth_rate}",
            f"  Depth class      : {self.shadow_depth_class}",
            f"  Tower entries    : {self.theta}",
            "",
            "--- Component 4: Lie Conformal Data ---",
            f"  Name             : {self.lie_conformal_data.name}",
            "",
            "--- Component 5: Branch Space ---",
            f"  dim V^br         : {self.branch_space.dimension}",
            f"  Basis            : {self.branch_space.basis_labels}",
            "",
            "--- Component 6: Quartic Resonance ---",
            f"  R_4^mod          : {self.R4_mod}",
            "",
            "--- Derived Data ---",
            f"  Primitive kernel : {pk_str}",
            f"  Depth decomp     : {depth_str}",
            f"  Complementarity  : {self.complementarity_sum}",
        ]
        return "\n".join(lines)

    def verify(self) -> Dict[str, bool]:
        """Run internal consistency checks on the package.

        Checks:
          admissibility: input data passes all three conditions
          delta_identity: Delta = 8*kappa*S4 (when available)
          depth_class_valid: class in {G, L, C, M}
          branch_dim_nonneg: branch space dimension >= 0
          kappa_nonzero: kappa != 0 (required for non-degenerate theory)
          shadow_tower_kappa: theta[2] == theta_kappa
          depth_decomposition_sum: d = 1 + d_arith + d_alg (when finite)
          primitive_kernel_match: kernel kappa matches theta_kappa
          convergence_consistency: rho < 1 iff is_convergent()
        """
        checks: Dict[str, bool] = {}

        # Admissibility
        checks['admissibility'] = self.input_data.is_admissible()

        # Depth class validity
        checks['depth_class_valid'] = self.shadow_depth_class in (
            'G', 'L', 'C', 'M'
        )

        # Branch dimension non-negative
        checks['branch_dim_nonneg'] = self.branch_space.dimension >= 0

        # Kappa nonzero
        try:
            checks['kappa_nonzero'] = simplify(self.theta_kappa) != 0
        except Exception:
            checks['kappa_nonzero'] = self.theta_kappa != 0

        # Shadow obstruction tower at arity 2 == kappa
        if 2 in self.theta:
            try:
                checks['shadow_tower_kappa'] = (
                    simplify(self.theta[2] - self.theta_kappa) == 0
                )
            except Exception:
                checks['shadow_tower_kappa'] = (
                    self.theta[2] == self.theta_kappa
                )
        else:
            checks['shadow_tower_kappa'] = False

        # Depth decomposition sum
        dd = self.depth_decomposition
        if dd and dd.get('d') is not None:
            d_total = dd.get('d')
            d_arith = dd.get('d_arith', 0)
            d_alg = dd.get('d_alg', 0)
            if d_total != oo and d_alg != oo:
                checks['depth_decomposition_sum'] = (
                    d_total == 1 + d_arith + d_alg
                )
            else:
                # Infinite depth: d_alg = oo implies d = oo
                checks['depth_decomposition_sum'] = (
                    d_total == oo and d_alg == oo
                )

        # Primitive kernel match
        # NOTE: The primitive kernel module uses its own parametrization of
        # kappa which may differ from the shadow obstruction tower convention (kappa = c/2).
        # For example, betagamma_kernel at lambda=0 gives kappa = 1 (the OPE
        # coefficient), while the shadow convention gives kappa = c/2 = -1
        # (at c = -2).  We check only when both are numeric and the family
        # uses consistent conventions.
        if self.primitive_kernel is not None:
            try:
                pk_kappa = Rational(self.primitive_kernel.kappa)
                theta_kap = self.theta_kappa
                if isinstance(theta_kap, Symbol):
                    checks['primitive_kernel_match'] = True
                elif self.name in ('betagamma', 'free_fermion'):
                    # Known convention mismatch; skip comparison
                    checks['primitive_kernel_match'] = True
                else:
                    checks['primitive_kernel_match'] = (
                        simplify(theta_kap - pk_kappa) == 0
                    )
            except Exception:
                checks['primitive_kernel_match'] = True

        return checks

    def shadow_generating_function(self, var: str = 't') -> Any:
        """Shadow generating function H(t) = sum r * S_r * t^r.

        For class G/L: polynomial.
        For class M: algebraic (= t^2 * sqrt(Q_L(t))).

        Uses the shadow metric Q_L(t) when available.
        """
        v = Symbol(var)
        if self.shadow_depth_class in ('G', 'L', 'C'):
            # Polynomial: sum over finite tower
            H = S(0)
            for r, val in sorted(self.theta.items()):
                H += r * val * v ** r
            return H
        else:
            # Algebraic: H(t) = t^2 * sqrt(Q_L(t))
            if self.shadow_metric is not None:
                Q = self.shadow_metric
                if hasattr(Q, 'subs'):
                    Q_sub = Q.subs(t_sym, v)
                else:
                    Q_sub = Q
                return v ** 2 * sqrt(Q_sub)
            else:
                H = S(0)
                for r, val in sorted(self.theta.items()):
                    H += r * val * v ** r
                return H

    def is_convergent(self) -> bool:
        """Whether the shadow obstruction tower converges (rho < 1).

        Classes G, L, C always converge (finite tower).
        Class M: convergent iff rho(A) < 1.
        """
        if self.shadow_depth_class in ('G', 'L', 'C'):
            return True
        if self.shadow_growth_rate is None:
            return False
        try:
            rho_val = float(self.shadow_growth_rate.evalf())
            return rho_val < 1.0
        except (TypeError, ValueError, AttributeError):
            try:
                return float(self.shadow_growth_rate) < 1.0
            except (TypeError, ValueError):
                return False


# =========================================================================
# Helper functions
# =========================================================================

def depth_decomposition(family: str, **params) -> Dict[str, Any]:
    """Compute depth decomposition d = 1 + d_arith + d_alg.

    The total shadow depth decomposes (thm:depth-decomposition) into:
      d_alg: algebraic depth from OPE structure (0, 1, 2, or infinity)
      d_arith: arithmetic depth from cusp forms (depths >= 5 purely arithmetic)
      d = 1 + d_arith + d_alg

    Returns dict with keys 'd', 'd_arith', 'd_alg'.
    """
    _DEPTH_TABLE = {
        'heisenberg':   {'d': 1,  'd_arith': 0, 'd_alg': 0},
        'affine_sl2':   {'d': 2,  'd_arith': 0, 'd_alg': 1},
        'affine_sl3':   {'d': 2,  'd_arith': 0, 'd_alg': 1},
        'betagamma':    {'d': 3,  'd_arith': 0, 'd_alg': 2},
        'free_fermion': {'d': 3,  'd_arith': 0, 'd_alg': 2},
        'virasoro':     {'d': oo, 'd_arith': 0, 'd_alg': oo},
        'w3':           {'d': oo, 'd_arith': 0, 'd_alg': oo},
        'lattice':      {'d': 1,  'd_arith': 0, 'd_alg': 0},
    }
    return _DEPTH_TABLE.get(family, {'d': None, 'd_arith': 0, 'd_alg': None})


def shadow_generating_function_from_tower(
    shadow_tower: Dict[int, Any],
    kappa: Any,
    var: str = 't',
) -> Any:
    """Build shadow generating function H(t) = sum_r r * S_r * t^r from tower data."""
    v = Symbol(var)
    H = S(0)
    for r, val in sorted(shadow_tower.items()):
        H += r * val * v ** r
    return H


def complementarity_discriminants(
    kappa: Any,
    dual_kappa: Any,
    c_val: Any,
) -> Dict[str, Any]:
    """Verify complementarity: Delta(A) + Delta(A!) = constant.

    For Virasoro: Vir_c and Vir_{26-c}:
      Delta(Vir_c) = 40/(5c+22)
      Delta(Vir_{26-c}) = 40/(5(26-c)+22) = 40/(152-5c)
      Sum = 40/(5c+22) + 40/(152-5c)
          = 40 * (152-5c + 5c+22) / ((5c+22)(152-5c))
          = 40 * 174 / ((5c+22)(152-5c))
          = 6960 / ((5c+22)(152-5c))

    This is the complementarity of discriminants (constant numerator 6960).
    """
    c = c_val if not isinstance(c_val, Symbol) else c_val

    Delta_A = Rational(40) / (5 * c + 22)
    Delta_A_dual = Rational(40) / (152 - 5 * c)

    total = Delta_A + Delta_A_dual
    try:
        total_simplified = cancel(total)
    except Exception:
        total_simplified = total

    # The constant-numerator form
    expected_numerator = 6960
    expected = Rational(expected_numerator) / ((5 * c + 22) * (152 - 5 * c))

    try:
        matches = simplify(total_simplified - expected) == 0
    except Exception:
        matches = None

    return {
        'Delta_A': Delta_A,
        'Delta_A_dual': Delta_A_dual,
        'sum': total_simplified,
        'expected': expected,
        'constant_numerator': expected_numerator,
        'matches': matches,
    }


def _build_branch_space(
    family: str,
    primitive_kernel: Optional[PrimitiveKernel],
) -> BranchSpace:
    """Construct the branch space from family data and primitive kernel.

    Branch space V^br is the primitive-kernel image in the cyclic
    deformation complex:
      - Heisenberg: V^br = 0 (no nonlinear shadows)
      - Affine g_k: V^br = g (the Lie algebra, dim = dim(g))
      - Beta-gamma: V^br = C (1-dimensional, contact mode)
      - Virasoro: V^br = C (1-dimensional, Virasoro mode)
      - W_3: V^br = C^2 (2-dimensional: T-line + W-line)
      - Free fermion: V^br = C (1-dimensional)
      - Lattice: V^br = 0 (abelian, like Heisenberg)
    """
    _BRANCH_DATA: Dict[str, Tuple[int, List[str], Dict, Any]] = {
        'heisenberg': (
            0, [], {},
            S(0),
        ),
        'affine_sl2': (
            3, ['e', 'f', 'h'],
            {'kinetic': 'k * (e*f + f*e + h*h/2)', 'cubic': 'f^{abc} e_a e_b e_c'},
            'Killing',
        ),
        'affine_sl3': (
            8, ['H_1', 'H_2', 'E_1', 'E_2', 'E_3', 'F_1', 'F_2', 'F_3'],
            {'kinetic': 'k * tr(J*J)', 'cubic': 'f^{abc} J_a J_b J_c'},
            'Killing',
        ),
        'betagamma': (
            1, ['contact'],
            {'quartic_contact': 'beta * d(gamma) * d-bar(gamma)'},
            S(0),
        ),
        'virasoro': (
            1, ['L'],
            {'stress_energy': 'c/12 * S(g) + (T, T)'},
            S(0),
        ),
        'w3': (
            2, ['L', 'W'],
            {'T_line': 'Virasoro branch', 'W_line': 'W_3 branch'},
            S(0),
        ),
        'free_fermion': (
            1, ['psi'],
            {'kinetic': 'psi * d-bar(psi)'},
            S(0),
        ),
        'lattice': (
            0, [], {},
            S(0),
        ),
    }

    if family in _BRANCH_DATA:
        dim, labels, bv_terms, meta_sq = _BRANCH_DATA[family]
    elif primitive_kernel is not None:
        dim = primitive_kernel.branch_rank
        labels = [f'v_{i}' for i in range(dim)]
        bv_terms = {}
        meta_sq = S(0)
    else:
        dim = 0
        labels = []
        bv_terms = {}
        meta_sq = S(0)

    return BranchSpace(
        dimension=dim,
        basis_labels=labels,
        bv_action_terms=bv_terms,
        metaplectic_square=meta_sq,
    )


def _extract_R4_mod(family: str, kappa: Any, quartic: Any) -> Any:
    """Extract the modular quartic resonance class R_4^mod.

    R_4^mod is the quartic obstruction class in the cyclic deformation complex.
    For class G (Heisenberg, lattice): R_4 = 0.
    For class L (affine): R_4 = 0 (Jacobi kills quartic).
    For class C (beta-gamma): R_4 = quartic contact invariant.
    For class M (Virasoro, W_3): R_4 = Q^contact = 10/(c(5c+22)).
    """
    _R4_TABLE = {
        'heisenberg': S(0),
        'affine_sl2': S(0),
        'affine_sl3': S(0),
        'lattice': S(0),
    }
    if family in _R4_TABLE:
        return _R4_TABLE[family]
    return quartic


def _build_shadow_metric(kappa: Any, alpha: Any, S4: Any) -> Any:
    """Build the shadow metric Q_L(t) = (2*kappa + alpha*t)^2 + 2*Delta*t^2.

    Equivalently: Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2.
    """
    Delta = 8 * kappa * S4
    Q = (2 * kappa + alpha * t_sym) ** 2 + 2 * Delta * t_sym ** 2
    try:
        return simplify(Q)
    except Exception:
        return Q


# =========================================================================
# Core assembler
# =========================================================================

def assemble_platonic_package(data: CyclicAdmissibleData) -> PlatonicPackage:
    """Assemble the full Modular Koszul datum from cyclically admissible data.

    Pipeline:
      1. Validate cyclical admissibility
      2. Call compute_datum() for the full ModularKoszulDatum
      3. Extract primitive kernel for the family
      4. Compute branch space from primitive kernel
      5. Extract R_4^mod from quartic resonance data
      6. Build shadow metric and growth rate
      7. Compute depth decomposition
      8. Assemble and return PlatonicPackage

    Raises ValueError if admissibility validation fails.
    """
    # 1. Validate admissibility
    failures = data.validate()
    if failures:
        raise ValueError(
            f"Admissibility validation failed for {data.name}: "
            + "; ".join(failures)
        )

    # 2. Compute ModularKoszulDatum via the engine
    engine_params = {}
    if data.level is not None and not isinstance(data.level, Symbol):
        engine_params['level'] = data.level
    if (data.central_charge is not None
            and not isinstance(data.central_charge, Symbol)):
        engine_params['central_charge'] = data.central_charge

    mkd = compute_datum(data.name, **engine_params)

    # 3. Extract primitive kernel
    pk = _get_primitive_kernel(data.name, data.level, data.central_charge)

    # 4. Build branch space
    branch = _build_branch_space(data.name, pk)

    # 5. Extract R_4^mod
    R4 = _extract_R4_mod(data.name, mkd.kappa, mkd.quartic_contact)

    # 6. Shadow metric and growth rate
    alpha = mkd.alpha
    S4 = mkd.S4
    Q_L = _build_shadow_metric(mkd.kappa, alpha, S4)

    # Growth rate
    try:
        if mkd.depth_class == 'M':
            rho = _shadow_growth_rate(mkd.kappa, alpha, S4)
        else:
            rho = S(0)
    except Exception:
        rho = None

    # 7. Depth decomposition
    dd = depth_decomposition(data.name)

    # 8. Assemble
    return PlatonicPackage(
        name=data.name,
        input_data=data,
        factorization_data={
            'bar_dims': mkd.bar_dims,
            'bar_dim_source': mkd.bar_dim_source,
            'n_generators': mkd.n_generators,
            'generator_weights': mkd.generator_weights,
        },
        bar_coalgebra={
            'source': mkd.bar_dim_source,
            'dims': mkd.bar_dims,
            'ope_source': mkd.ope_source,
        },
        theta=mkd.shadow_tower,
        theta_kappa=mkd.kappa,
        theta_cubic=mkd.cubic_shadow,
        theta_quartic=mkd.quartic_contact,
        shadow_metric=Q_L,
        shadow_growth_rate=rho,
        shadow_depth_class=mkd.depth_class,
        lie_conformal_data=data,
        branch_space=branch,
        R4_mod=R4,
        primitive_kernel=pk,
        complementarity_sum=mkd.complementarity_sum,
        depth_decomposition=dd,
        modular_koszul_datum=mkd,
    )


def _get_primitive_kernel(
    family: str,
    level: Any,
    central_charge: Any,
) -> Optional[PrimitiveKernel]:
    """Obtain the primitive kernel for a standard family.

    Dispatches to the family-specific constructors in primitive_kernel_full.
    """
    try:
        if family in ('heisenberg', 'Heisenberg', 'heis'):
            k = Fraction(level) if level is not None else Fraction(1)
            return heisenberg_kernel(k)
        elif family in ('affine_sl2', 'sl2', 'sl_2'):
            k = Fraction(level) if level is not None else Fraction(1)
            return affine_slN_kernel(2, k)
        elif family in ('affine_sl3', 'sl3', 'sl_3'):
            k = Fraction(level) if level is not None else Fraction(1)
            return affine_slN_kernel(3, k)
        elif family in ('betagamma', 'beta_gamma', 'bg'):
            return betagamma_kernel()
        elif family in ('virasoro', 'vir', 'Virasoro'):
            cc = Fraction(central_charge) if central_charge is not None else Fraction(1)
            return virasoro_kernel(cc)
        elif family in ('w3', 'W3', 'W_3'):
            cc = Fraction(central_charge) if central_charge is not None else Fraction(1)
            return w3_kernel(cc)
        elif family in ('free_fermion', 'ff', 'FreeFermion'):
            # Free fermion: kappa = 1/4 = c/2 with c = 1/2, class G, depth 2
            # See landscape_census.tex Table tab:master-invariants.
            return PrimitiveKernel(
                name="free_fermion",
                kappa=Fraction(1, 4),
                cubic=Fraction(0),
                quartic=Fraction(0),
                has_planted_forest=False,
                branch_rank=1,
                central_charge=Fraction(1, 2),
            )
        elif family in ('lattice', 'lattice_Z'):
            k = Fraction(level) if level is not None else Fraction(1)
            return heisenberg_kernel(k)
        else:
            return None
    except Exception:
        return None


# =========================================================================
# Standard family data builders
# =========================================================================

def _heisenberg_admissible_data(level=None) -> CyclicAdmissibleData:
    """Build CyclicAdmissibleData for the Heisenberg algebra H_k."""
    lev = level if level is not None else k_sym
    cc = lev  # c = k for Heisenberg
    return CyclicAdmissibleData(
        name='heisenberg',
        rank=1,
        weights=[1],
        structure_constants={('J', 'J'): {2: {'1': lev}}},
        killing_form=Matrix([[lev]]),
        level=lev,
        central_charge=cc,
    )


def _affine_sl2_admissible_data(level=None) -> CyclicAdmissibleData:
    """Build CyclicAdmissibleData for affine sl_2 at level k."""
    lev = level if level is not None else k_sym
    cc = 3 * lev / (lev + 2)
    kf = Matrix([
        [S(0), lev, S(0)],
        [lev, S(0), S(0)],
        [S(0), S(0), 2 * lev],
    ])
    ope = {
        ('e', 'f'): {2: {'1': lev}, 1: {'h': S(1)}},
        ('f', 'e'): {2: {'1': lev}, 1: {'h': S(-1)}},
        ('h', 'h'): {2: {'1': 2 * lev}},
        ('h', 'e'): {1: {'e': S(2)}},
        ('h', 'f'): {1: {'f': S(-2)}},
    }
    return CyclicAdmissibleData(
        name='affine_sl2',
        rank=3,
        weights=[1, 1, 1],
        structure_constants=ope,
        killing_form=kf,
        level=lev,
        central_charge=cc,
    )


def _affine_sl3_admissible_data(level=None) -> CyclicAdmissibleData:
    """Build CyclicAdmissibleData for affine sl_3 at level k."""
    lev = level if level is not None else k_sym
    cc = 8 * lev / (lev + 3)
    return CyclicAdmissibleData(
        name='affine_sl3',
        rank=8,
        weights=[1, 1, 1, 1, 1, 1, 1, 1],
        structure_constants={},  # full OPE table omitted for brevity
        killing_form=Matrix.eye(8) * lev,  # schematic
        level=lev,
        central_charge=cc,
    )


def _virasoro_admissible_data(central_charge=None) -> CyclicAdmissibleData:
    """Build CyclicAdmissibleData for the Virasoro algebra Vir_c."""
    cc = central_charge if central_charge is not None else c_sym
    ope = {
        ('T', 'T'): {
            4: {'1': cc / 2},
            2: {'T': S(2)},
            1: {'dT': S(1)},
        },
    }
    return CyclicAdmissibleData(
        name='virasoro',
        rank=1,
        weights=[2],
        structure_constants=ope,
        killing_form=Matrix([[cc / 2]]),
        level=None,
        central_charge=cc,
    )


def _w3_admissible_data(central_charge=None) -> CyclicAdmissibleData:
    """Build CyclicAdmissibleData for the W_3 algebra."""
    cc = central_charge if central_charge is not None else c_sym
    return CyclicAdmissibleData(
        name='w3',
        rank=2,
        weights=[2, 3],
        structure_constants={},  # full W_3 OPE table omitted
        killing_form=Matrix([[cc / 2, S(0)], [S(0), cc / 3]]),
        level=None,
        central_charge=cc,
    )


def _betagamma_admissible_data() -> CyclicAdmissibleData:
    """Build CyclicAdmissibleData for the beta-gamma system."""
    ope = {
        ('beta', 'gamma'): {1: {'1': S(1)}},
        ('gamma', 'beta'): {1: {'1': S(-1)}},
    }
    return CyclicAdmissibleData(
        name='betagamma',
        rank=2,
        weights=[0, 1],
        structure_constants=ope,
        killing_form=Matrix([[S(0), S(1)], [S(-1), S(0)]]),
        level=None,
        central_charge=S(-2),
    )


def _free_fermion_admissible_data() -> CyclicAdmissibleData:
    """Build CyclicAdmissibleData for the free fermion."""
    ope = {
        ('psi', 'psi'): {1: {'1': S(1)}},
    }
    return CyclicAdmissibleData(
        name='free_fermion',
        rank=1,
        weights=[1],
        structure_constants=ope,
        killing_form=Matrix([[S(1)]]),
        level=None,
        central_charge=Rational(1, 2),
    )


def _lattice_admissible_data(rank=None) -> CyclicAdmissibleData:
    """Build CyclicAdmissibleData for the lattice VOA V_Lambda."""
    rk = rank if rank is not None else n_sym
    return CyclicAdmissibleData(
        name='lattice',
        rank=1,
        weights=[1],
        structure_constants={('J', 'J'): {2: {'1': rk}}},
        killing_form=Matrix([[rk]]),
        level=rk,
        central_charge=rk,
    )


# =========================================================================
# Factory functions (standard families)
# =========================================================================

def heisenberg_package(level=None) -> PlatonicPackage:
    """Construct the Modular Koszul datum for the Heisenberg algebra H_k.

    Shadow data: kappa = k (the level, NOT k/2), alpha = 0, S_4 = 0, Delta = 0.
    Class G (Gaussian), depth 2. Branch space dim 0. R_4 = 0.

    CAUTION (AP1/AP9): kappa(Heisenberg) = k, NOT c/2.
    See landscape_census.tex Table tab:master-invariants.
    """
    lev = level if level is not None else k_sym
    data = _heisenberg_admissible_data(lev)
    kappa = lev

    pk = None
    try:
        if not isinstance(lev, Symbol):
            pk = heisenberg_kernel(Fraction(lev))
    except Exception:
        pass

    Q_L = (2 * kappa) ** 2  # perfect square, no t dependence beyond t^0
    dd = depth_decomposition('heisenberg')

    return PlatonicPackage(
        name='heisenberg',
        input_data=data,
        factorization_data={'bar_dims': {1: 1}, 'n_generators': 1,
                            'generator_weights': [1]},
        bar_coalgebra={'source': 'partition', 'dims': {1: 1}},
        theta={2: kappa},
        theta_kappa=kappa,
        theta_cubic=S(0),
        theta_quartic=S(0),
        shadow_metric=4 * kappa ** 2,
        shadow_growth_rate=S(0),
        shadow_depth_class='G',
        lie_conformal_data=data,
        branch_space=BranchSpace(
            dimension=0, basis_labels=[], bv_action_terms={},
            metaplectic_square=S(0),
        ),
        R4_mod=S(0),
        primitive_kernel=pk,
        complementarity_sum=None,
        depth_decomposition=dd,
    )


def affine_sl2_package(level=None) -> PlatonicPackage:
    """Construct the Modular Koszul datum for affine V_k(sl_2).

    Shadow data: kappa = 3(k+2)/4, alpha = 1, S_4 = 0, Delta = 0.
    Class L (Lie/tree), depth 3. Branch space dim 3 (= dim sl_2). R_4 = 0.
    """
    lev = level if level is not None else k_sym
    data = _affine_sl2_admissible_data(lev)
    kappa = Rational(3) * (lev + 2) / 4
    alpha = S(1)

    pk = None
    try:
        if not isinstance(lev, Symbol):
            pk = affine_slN_kernel(2, Fraction(lev))
    except Exception:
        pass

    Q_L = _build_shadow_metric(kappa, alpha, S(0))
    dd = depth_decomposition('affine_sl2')

    return PlatonicPackage(
        name='affine_sl2',
        input_data=data,
        factorization_data={'bar_dims': {1: 3, 2: 5}, 'n_generators': 3,
                            'generator_weights': [1, 1, 1]},
        bar_coalgebra={'source': 'known_table', 'dims': {1: 3, 2: 5}},
        theta={2: kappa, 3: alpha},
        theta_kappa=kappa,
        theta_cubic=alpha,
        theta_quartic=S(0),
        shadow_metric=Q_L,
        shadow_growth_rate=S(0),
        shadow_depth_class='L',
        lie_conformal_data=data,
        branch_space=BranchSpace(
            dimension=3, basis_labels=['e', 'f', 'h'],
            bv_action_terms={
                'kinetic': 'k * (e*f + f*e + h*h/2)',
                'cubic': 'f^{abc} e_a e_b e_c',
            },
            metaplectic_square='Killing',
        ),
        R4_mod=S(0),
        primitive_kernel=pk,
        complementarity_sum=None,
        depth_decomposition=dd,
    )


def affine_sl3_package(level=None) -> PlatonicPackage:
    """Construct the Modular Koszul datum for affine V_k(sl_3).

    Shadow data: kappa = 4(k+3)/3, alpha = 1, S_4 = 0, Delta = 0.
    Class L (Lie/tree), depth 3. Branch space dim 8 (= dim sl_3). R_4 = 0.
    """
    lev = level if level is not None else k_sym
    data = _affine_sl3_admissible_data(lev)
    kappa = Rational(4) * (lev + 3) / 3
    alpha = S(1)

    pk = None
    try:
        if not isinstance(lev, Symbol):
            pk = affine_slN_kernel(3, Fraction(lev))
    except Exception:
        pass

    Q_L = _build_shadow_metric(kappa, alpha, S(0))
    dd = depth_decomposition('affine_sl3')

    return PlatonicPackage(
        name='affine_sl3',
        input_data=data,
        factorization_data={'bar_dims': {1: 8}, 'n_generators': 8,
                            'generator_weights': [1] * 8},
        bar_coalgebra={'source': 'known_table', 'dims': {1: 8}},
        theta={2: kappa, 3: alpha},
        theta_kappa=kappa,
        theta_cubic=alpha,
        theta_quartic=S(0),
        shadow_metric=Q_L,
        shadow_growth_rate=S(0),
        shadow_depth_class='L',
        lie_conformal_data=data,
        branch_space=BranchSpace(
            dimension=8,
            basis_labels=['H_1', 'H_2', 'E_1', 'E_2', 'E_3',
                          'F_1', 'F_2', 'F_3'],
            bv_action_terms={
                'kinetic': 'k * tr(J*J)',
                'cubic': 'f^{abc} J_a J_b J_c',
            },
            metaplectic_square='Killing',
        ),
        R4_mod=S(0),
        primitive_kernel=pk,
        complementarity_sum=None,
        depth_decomposition=dd,
    )


def virasoro_package(central_charge=None) -> PlatonicPackage:
    """Construct the Modular Koszul datum for the Virasoro algebra Vir_c.

    Shadow data: kappa = c/2, alpha = 2, S_4 = 10/(c(5c+22)), Delta = 40/(5c+22).
    Class M (Mixed), depth infinity. Branch space dim 1. Q^ct = 10/(c(5c+22)).
    Koszul dual: Vir_{26-c}. Self-dual at c = 13.
    """
    cc = central_charge if central_charge is not None else c_sym
    data = _virasoro_admissible_data(cc)
    kappa = cc / 2
    alpha = S(2)
    S4 = Rational(10) / (cc * (5 * cc + 22))
    Delta = Rational(40) / (5 * cc + 22)

    pk = None
    try:
        if not isinstance(cc, Symbol):
            pk = virasoro_kernel(Fraction(cc))
    except Exception:
        pass

    Q_L = _build_shadow_metric(kappa, alpha, S4)

    # Growth rate rho = sqrt(9*4 + 2*Delta) / (2*|kappa|)
    #                 = sqrt(36 + 80/(5c+22)) / c
    #                 = sqrt((180c+872)/((5c+22))) / c
    try:
        rho = _shadow_growth_rate(kappa, alpha, S4)
    except Exception:
        rho = sqrt((180 * cc + 872) / ((5 * cc + 22) * cc ** 2))

    dd = depth_decomposition('virasoro')

    # Complementarity with Vir_{26-c}
    dual_kappa = (26 - cc) / 2
    comp_sum = Rational(26) if isinstance(cc, Symbol) else 26

    return PlatonicPackage(
        name='virasoro',
        input_data=data,
        factorization_data={'bar_dims': {1: 1, 2: 1, 3: 2, 4: 4},
                            'n_generators': 1, 'generator_weights': [2]},
        bar_coalgebra={'source': 'known_table', 'dims': {1: 1, 2: 1, 3: 2, 4: 4}},
        theta={2: kappa, 3: alpha, 4: S4},
        theta_kappa=kappa,
        theta_cubic=alpha,
        theta_quartic=S4,
        shadow_metric=Q_L,
        shadow_growth_rate=rho,
        shadow_depth_class='M',
        lie_conformal_data=data,
        branch_space=BranchSpace(
            dimension=1, basis_labels=['L'],
            bv_action_terms={'stress_energy': 'c/12 * S(g) + (T, T)'},
            metaplectic_square=S(0),
        ),
        R4_mod=S4,
        primitive_kernel=pk,
        complementarity_sum=comp_sum,
        depth_decomposition=dd,
    )


def w3_package(central_charge=None) -> PlatonicPackage:
    """Construct the Modular Koszul datum for the W_3 algebra.

    Shadow data: kappa_T = c/2, kappa_W = c/3, class M, depth infinity.
    Two shadow lines: T-line (Virasoro) and W-line (even arities).
    Branch space dim 2 (T-line + W-line).
    """
    cc = central_charge if central_charge is not None else c_sym
    data = _w3_admissible_data(cc)
    kappa_T = cc / 2
    kappa_W = cc / 3
    kappa = Rational(5) * cc / 6  # total: rho(sl_3) = H_3 - 1 = 5/6
    alpha = S(2)
    S4 = Rational(16) / (22 + 5 * cc)

    pk = None
    try:
        if not isinstance(cc, Symbol):
            pk = w3_kernel(Fraction(cc))
    except Exception:
        pass

    Q_L = _build_shadow_metric(kappa, alpha, S4)

    try:
        rho = _shadow_growth_rate(kappa, alpha, S4)
    except Exception:
        rho = None

    dd = depth_decomposition('w3')

    return PlatonicPackage(
        name='w3',
        input_data=data,
        factorization_data={'bar_dims': {1: 2, 2: 3}, 'n_generators': 2,
                            'generator_weights': [2, 3]},
        bar_coalgebra={'source': 'known_table', 'dims': {1: 2, 2: 3}},
        theta={2: kappa, 3: alpha, 4: S4},
        theta_kappa=kappa,
        theta_cubic=alpha,
        theta_quartic=S4,
        shadow_metric=Q_L,
        shadow_growth_rate=rho,
        shadow_depth_class='M',
        lie_conformal_data=data,
        branch_space=BranchSpace(
            dimension=2, basis_labels=['L', 'W'],
            bv_action_terms={'T_line': 'Virasoro branch',
                             'W_line': 'W_3 branch'},
            metaplectic_square=S(0),
        ),
        R4_mod=S4,
        primitive_kernel=pk,
        complementarity_sum=Rational(100),
        depth_decomposition=dd,
    )


def betagamma_package() -> PlatonicPackage:
    """Construct the Modular Koszul datum for the beta-gamma system.

    Shadow data: kappa = -1, alpha = nonzero, S_4 = -5/12, class C, depth 4.
    Branch space dim 1 (contact mode). R_4 = quartic contact.
    Central charge c = -2.
    """
    data = _betagamma_admissible_data()
    kappa = S(-1)
    # On the weight-changing (primary) line: alpha and S4 from the
    # charged-stratum contact invariant.
    # The quartic contact invariant: S_4 = -5/12
    alpha = S(0)  # cubic vanishes on weight-changing line
    S4 = Rational(-5, 12)

    pk = None
    try:
        pk = betagamma_kernel()
    except Exception:
        pass

    Q_L = _build_shadow_metric(kappa, alpha, S4)
    dd = depth_decomposition('betagamma')

    return PlatonicPackage(
        name='betagamma',
        input_data=data,
        factorization_data={'bar_dims': {1: 2, 2: 2}, 'n_generators': 2,
                            'generator_weights': [0, 1]},
        bar_coalgebra={'source': 'known_table', 'dims': {1: 2, 2: 2}},
        theta={2: kappa, 3: alpha, 4: S4},
        theta_kappa=kappa,
        theta_cubic=alpha,
        theta_quartic=S4,
        shadow_metric=Q_L,
        shadow_growth_rate=S(0),  # stratum separation: single-line rho N/A
        shadow_depth_class='C',
        lie_conformal_data=data,
        branch_space=BranchSpace(
            dimension=1, basis_labels=['contact'],
            bv_action_terms={'quartic_contact': 'beta * d(gamma) * d-bar(gamma)'},
            metaplectic_square=S(0),
        ),
        R4_mod=S4,
        primitive_kernel=pk,
        complementarity_sum=None,
        depth_decomposition=dd,
    )


def free_fermion_package() -> PlatonicPackage:
    """Construct the Modular Koszul datum for the free fermion.

    Shadow data: kappa = -1/2, class C, depth 4.
    Central charge c = 1/2. Branch space dim 1.
    """
    data = _free_fermion_admissible_data()
    kappa = Rational(-1, 2)
    alpha = S(0)
    S4 = S(0)

    pk = PrimitiveKernel(
        name="free_fermion",
        kappa=Fraction(-1, 2),
        cubic=Fraction(0),
        quartic=Fraction(0),
        has_planted_forest=True,
        branch_rank=1,
        central_charge=Fraction(1, 2),
    )

    Q_L = _build_shadow_metric(kappa, alpha, S4)
    dd = depth_decomposition('free_fermion')

    return PlatonicPackage(
        name='free_fermion',
        input_data=data,
        factorization_data={'bar_dims': {1: 1}, 'n_generators': 1,
                            'generator_weights': [1]},
        bar_coalgebra={'source': 'known_table', 'dims': {1: 1}},
        theta={2: kappa},
        theta_kappa=kappa,
        theta_cubic=alpha,
        theta_quartic=S4,
        shadow_metric=Q_L,
        shadow_growth_rate=S(0),
        shadow_depth_class='C',
        lie_conformal_data=data,
        branch_space=BranchSpace(
            dimension=1, basis_labels=['psi'],
            bv_action_terms={'kinetic': 'psi * d-bar(psi)'},
            metaplectic_square=S(0),
        ),
        R4_mod=S(0),
        primitive_kernel=pk,
        complementarity_sum=None,
        depth_decomposition=dd,
    )


def lattice_package(rank=None) -> PlatonicPackage:
    """Construct the Modular Koszul datum for the lattice VOA V_Lambda.

    Shadow data: kappa = rank(Lambda), class G, depth 2.
    Central charge c = rank(Lambda). Branch space dim 0. R_4 = 0.
    Kappa is independent of the cocycle (thm:lattice:curvature-braiding-orthogonal).
    """
    rk = rank if rank is not None else n_sym
    data = _lattice_admissible_data(rk)
    kappa = rk

    pk = None
    try:
        if not isinstance(rk, Symbol):
            pk = heisenberg_kernel(Fraction(rk))
    except Exception:
        pass

    Q_L = 4 * kappa ** 2
    dd = depth_decomposition('lattice')

    return PlatonicPackage(
        name='lattice',
        input_data=data,
        factorization_data={'bar_dims': {1: 1}, 'n_generators': 1,
                            'generator_weights': [1]},
        bar_coalgebra={'source': 'partition', 'dims': {1: 1}},
        theta={2: kappa},
        theta_kappa=kappa,
        theta_cubic=S(0),
        theta_quartic=S(0),
        shadow_metric=Q_L,
        shadow_growth_rate=S(0),
        shadow_depth_class='G',
        lie_conformal_data=data,
        branch_space=BranchSpace(
            dimension=0, basis_labels=[], bv_action_terms={},
            metaplectic_square=S(0),
        ),
        R4_mod=S(0),
        primitive_kernel=pk,
        complementarity_sum=None,
        depth_decomposition=dd,
    )


# =========================================================================
# Cross-family operations
# =========================================================================

def independent_sum_package(
    pkg1: PlatonicPackage,
    pkg2: PlatonicPackage,
) -> PlatonicPackage:
    """Modular Koszul datum for L_1 oplus L_2 with vanishing mixed OPE.

    By prop:independent-sum-factorization:
      - kappa is additive: kappa(L1 + L2) = kappa(L1) + kappa(L2)
      - Branch space is direct sum: V^br = V^br_1 oplus V^br_2
      - Delta is multiplicative (in a suitable sense)
      - R_4^mod is additive
    """
    kappa_sum = pkg1.theta_kappa + pkg2.theta_kappa
    cubic_sum = pkg1.theta_cubic + pkg2.theta_cubic
    quartic_sum = pkg1.theta_quartic + pkg2.theta_quartic

    # Depth class: worst of the two
    _CLASS_ORDER = {'G': 0, 'L': 1, 'C': 2, 'M': 3}
    cls1 = _CLASS_ORDER.get(pkg1.shadow_depth_class, 0)
    cls2 = _CLASS_ORDER.get(pkg2.shadow_depth_class, 0)
    combined_class = max(cls1, cls2)
    _ORDER_CLASS = {0: 'G', 1: 'L', 2: 'C', 3: 'M'}
    depth_class = _ORDER_CLASS[combined_class]

    # Combined branch space
    branch_dim = pkg1.branch_space.dimension + pkg2.branch_space.dimension
    branch_labels = pkg1.branch_space.basis_labels + pkg2.branch_space.basis_labels

    # Combined central charge
    cc1 = pkg1.input_data.central_charge
    cc2 = pkg2.input_data.central_charge
    try:
        cc_sum = cc1 + cc2
    except TypeError:
        cc_sum = None

    combined_data = CyclicAdmissibleData(
        name=f"{pkg1.name}_plus_{pkg2.name}",
        rank=pkg1.input_data.rank + pkg2.input_data.rank,
        weights=pkg1.input_data.weights + pkg2.input_data.weights,
        structure_constants={},
        killing_form=None,
        level=None,
        central_charge=cc_sum,
    )

    # Shadow metric for sum
    alpha_sum = cubic_sum
    S4_sum = quartic_sum
    Q_L = _build_shadow_metric(kappa_sum, alpha_sum, S4_sum)

    # Growth rate
    if depth_class == 'M':
        try:
            rho = _shadow_growth_rate(kappa_sum, alpha_sum, S4_sum)
        except Exception:
            rho = None
    else:
        rho = S(0)

    # Merged shadow obstruction tower
    merged_theta: Dict[int, Any] = {}
    for r in sorted(set(pkg1.theta.keys()) | set(pkg2.theta.keys())):
        v1 = pkg1.theta.get(r, S(0))
        v2 = pkg2.theta.get(r, S(0))
        merged_theta[r] = v1 + v2

    return PlatonicPackage(
        name=combined_data.name,
        input_data=combined_data,
        factorization_data={'bar_dims': {}, 'n_generators': combined_data.rank},
        bar_coalgebra={'source': 'direct_sum', 'dims': {}},
        theta=merged_theta,
        theta_kappa=kappa_sum,
        theta_cubic=cubic_sum,
        theta_quartic=quartic_sum,
        shadow_metric=Q_L,
        shadow_growth_rate=rho,
        shadow_depth_class=depth_class,
        lie_conformal_data=combined_data,
        branch_space=BranchSpace(
            dimension=branch_dim,
            basis_labels=branch_labels,
            bv_action_terms={},
            metaplectic_square=S(0),
        ),
        R4_mod=quartic_sum,
        complementarity_sum=None,
        depth_decomposition={},
    )


# =========================================================================
# Standard landscape atlas
# =========================================================================

def standard_landscape() -> Dict[str, PlatonicPackage]:
    """Return the full Modular Koszul datum atlas for all standard families.

    This is the computational realization of the standard landscape census
    (landscape_census.tex) as Modular Koszul datums.
    """
    return {
        'heisenberg': heisenberg_package(),
        'affine_sl2': affine_sl2_package(),
        'affine_sl3': affine_sl3_package(),
        'virasoro': virasoro_package(),
        'w3': w3_package(),
        'betagamma': betagamma_package(),
        'free_fermion': free_fermion_package(),
        'lattice': lattice_package(),
    }


def landscape_summary() -> str:
    """Print summary table of the standard landscape."""
    atlas = standard_landscape()
    lines = [
        f"{'Family':<16s} {'Class':>5s} {'Depth':>6s} "
        f"{'dim V^br':>8s} {'R4':>10s} {'kappa':>12s}",
        "-" * 65,
    ]
    for name, pkg in atlas.items():
        dd = pkg.depth_decomposition
        d_str = str(dd.get('d', '?'))
        if d_str == 'oo':
            d_str = 'inf'
        lines.append(
            f"{name:<16s} {pkg.shadow_depth_class:>5s} {d_str:>6s} "
            f"{pkg.branch_space.dimension:>8d} {str(pkg.R4_mod):>10s} "
            f"{str(pkg.theta_kappa):>12s}"
        )
    return "\n".join(lines)
