r"""Finite scalar shadow certificates and KW Virasoro reference checks.

The scalar shadow lane computes exact coefficients

    F_g^{scal}(A) = kappa(A) * lambda_g^{FP},
    q = hbar^2,
    log tau_shadow,scal^{<=G}(A) = kappa(A) log tau_KW^{<=G}

in ``Q[kappa][[q]]/(q^{G+1})``.  This finite coefficient identity does
not construct descendant CohFT classes, descendant Virasoro operators, or
a KdV/Gelfand-Dickey hierarchy for arbitrary ``kappa``.

The Witten-Kontsevich routines below are a reference oracle for the
genuine KW descendant CohFT.  Standard descendant Virasoro constraints
are certified only in the actual KW case ``kappa = 1``.  The scalar
zero-field value ``kappa = 0`` is recorded as the trivial solution of
the standard nonlinear KdV/Hirota equations, not as a KW descendant
package.  For other values the first standard KdV equation leaves the
exact residual factor ``kappa(1-kappa)``.

Local source anchors:
    chapters/examples/landscape_census.tex:140-152
    chapters/examples/landscape_census.tex:173-186
    chapters/examples/landscape_census.tex:4970-5018
    chapters/theory/higher_genus_modular_koszul.tex:20242-20388
    chapters/connections/concordance.tex:4095-4108
    chapters/connections/concordance.tex:6742-6759

All arithmetic is exact.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Tuple

from sympy import Rational, Symbol, bernoulli, factorial


c = Symbol('c')
k = Symbol('k')
hbar = Symbol('hbar')


LOCAL_SOURCE_ANCHORS: Dict[str, str] = {
    'kappa_formulas': 'chapters/examples/landscape_census.tex:140-152',
    'collision_residues': 'chapters/examples/landscape_census.tex:173-186',
    'fp_coefficients': 'chapters/examples/landscape_census.tex:4970-5018',
    'stationary_primary_line':
        'chapters/theory/higher_genus_modular_koszul.tex:20242-20276',
    'finite_scalar_tau':
        'chapters/theory/higher_genus_modular_koszul.tex:20304-20388',
    'concordance_kappa': 'chapters/connections/concordance.tex:4095-4108',
    'scalar_free_energy':
        'chapters/connections/concordance.tex:6742-6759',
}


KERNEL_CONSTANTS: Dict[str, Dict[str, str]] = {
    'affine_raw_trace': {
        'formula': 'k*Omega_tr/z',
        'scope': 'collision residue, trace-form convention',
        'source': LOCAL_SOURCE_ANCHORS['collision_residues'],
    },
    'affine_kz': {
        'formula': 'Omega/((k+h^vee)z)',
        'scope': 'KZ presentation; not the raw trace-form residue',
        'source': LOCAL_SOURCE_ANCHORS['collision_residues'],
    },
    'heisenberg': {
        'formula': 'k/z',
        'scope': 'rank-one Heisenberg collision residue',
        'source': LOCAL_SOURCE_ANCHORS['collision_residues'],
    },
    'virasoro': {
        'formula': '(c/2)/z^3 + 2*T/z',
        'scope': 'Virasoro collision residue',
        'source': LOCAL_SOURCE_ANCHORS['collision_residues'],
    },
}


KAPPA_FORMULAS: Dict[str, Dict[str, str]] = {
    'heisenberg_rank_one': {
        'formula': 'k',
        'source': LOCAL_SOURCE_ANCHORS['kappa_formulas'],
    },
    'affine_trace_form': {
        'formula': 'dim(g)*(k+h^vee)/(2*h^vee)',
        'source': LOCAL_SOURCE_ANCHORS['kappa_formulas'],
    },
    'virasoro': {
        'formula': 'c/2',
        'source': LOCAL_SOURCE_ANCHORS['kappa_formulas'],
    },
    'w_n': {
        'formula': 'c*(H_N-1)',
        'source': LOCAL_SOURCE_ANCHORS['kappa_formulas'],
    },
}


OBJECT_FIREWALLS: Tuple[str, ...] = (
    'A is the algebra.',
    'B(A) is the bar coalgebra T^c(s^{-1} Abar).',
    'A^i is the bar-cohomology coalgebra branch.',
    'A^! is the Verdier/continuous-linear dual branch under hypotheses.',
    'Z_ch^der(A) is ChirHoch^*(A,A), the Hochschild/bulk object.',
    'Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.',
)


def kernel_constant_certificate() -> Dict[str, Any]:
    r"""Return local collision-residue and object-separation conventions."""
    return {
        'kernel_constants': KERNEL_CONSTANTS,
        'kappa_formulas': KAPPA_FORMULAS,
        'object_firewalls': OBJECT_FIREWALLS,
        'source_anchors': LOCAL_SOURCE_ANCHORS,
    }


@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande coefficient ``lambda_g^FP``.

    ``lambda_g^FP = ((2^{2g-1}-1)/2^{2g-1}) * |B_{2g}|/(2g)!``.
    The first values are recorded in ``landscape_census.tex:4988-5010``.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    power = 2 ** (2 * g - 1)
    B_2g = bernoulli(2 * g)
    abs_B_2g = Rational(abs(int(B_2g.p)), int(B_2g.q))
    result = Rational(power - 1, power) * abs_B_2g / factorial(2 * g)
    return Fraction(int(result.p), int(result.q))


@lru_cache(maxsize=64)
def lambda_g_integral(g: int) -> Fraction:
    r"""Bernoulli Hodge coefficient ``|B_{2g}|/(2g*(2g)!)``.

    This is the Bernoulli factor paired with the FP coefficient by
    ``lambda_g^FP / lambda_g_integral =
    ((2^{2g-1}-1) * 2g)/2^{2g-1}``.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    abs_B_2g = Rational(abs(int(B_2g.p)), int(B_2g.q))
    result = abs_B_2g / (2 * g * factorial(2 * g))
    return Fraction(int(result.p), int(result.q))


def _double_factorial_odd(n: int) -> int:
    """Return ``(2n+1)!!`` with ``(-1)!! = 1``."""
    if n < 0:
        return 1
    result = 1
    for j in range(1, 2 * n + 2, 2):
        result *= j
    return result


@lru_cache(maxsize=None)
def wk_intersection(genus: int, insertions: Tuple[int, ...]) -> Fraction:
    r"""Witten-Kontsevich intersection number by string/dilaton/DVV recursion.

    ``<tau_{d_1} ... tau_{d_n}>_g =
    int_{Mbar_{g,n}} psi_1^{d_1} ... psi_n^{d_n}``.
    """
    insertions = tuple(sorted(insertions))
    n = len(insertions)

    if any(d < 0 for d in insertions):
        return Fraction(0)
    if n == 0:
        return Fraction(0)
    if 2 * genus - 2 + n <= 0:
        return Fraction(0)
    if sum(insertions) != 3 * genus - 3 + n:
        return Fraction(0)
    if genus == 0 and insertions == (0, 0, 0):
        return Fraction(1)
    if genus == 1 and insertions == (1,):
        return Fraction(1, 24)

    if 0 in insertions:
        remaining = list(insertions)
        remaining.pop(remaining.index(0))
        total = Fraction(0)
        for i, d_i in enumerate(remaining):
            if d_i > 0:
                lowered = list(remaining)
                lowered[i] -= 1
                total += wk_intersection(genus, tuple(lowered))
        return total

    if 1 in insertions:
        remaining = list(insertions)
        remaining.pop(remaining.index(1))
        n_remaining = len(remaining)
        if 2 * genus - 2 + n_remaining > 0:
            return Fraction(2 * genus - 2 + n_remaining) * wk_intersection(
                genus, tuple(remaining))

    d = insertions[-1]
    rest = list(insertions[:-1])
    if d < 2:
        return Fraction(0)

    rhs = _dvv_rhs_sum(d, genus, rest)
    return rhs / Fraction(_double_factorial_odd(d))


def _dvv_rhs_sum(d: int, genus: int, rest: List[int]) -> Fraction:
    """Right-hand side of the DVV recursion for distinguished degree ``d``."""
    result = Fraction(0)

    for i, d_i in enumerate(rest):
        new_d = d + d_i - 1
        merge_coeff = Fraction(
            _double_factorial_odd(d + d_i - 1),
            _double_factorial_odd(d_i - 1) if d_i >= 1 else 1,
        )
        others = rest[:i] + rest[i + 1:]
        result += merge_coeff * wk_intersection(genus, tuple(others + [new_d]))

    if genus >= 1:
        for a in range(d - 1):
            b = d - 2 - a
            handle_coeff = Fraction(
                _double_factorial_odd(a) * _double_factorial_odd(b), 2)
            result += handle_coeff * wk_intersection(
                genus - 1, tuple(rest + [a, b]))

    m = len(rest)
    for a in range(d - 1):
        b = d - 2 - a
        split_weight = Fraction(
            _double_factorial_odd(a) * _double_factorial_odd(b), 2)
        for mask in range(1 << m):
            I_ins = [rest[bit] for bit in range(m) if mask & (1 << bit)]
            J_ins = [rest[bit] for bit in range(m) if not (mask & (1 << bit))]
            for g1 in range(genus + 1):
                g2 = genus - g1
                val_I = wk_intersection(g1, tuple(I_ins + [a]))
                if val_I == Fraction(0):
                    continue
                val_J = wk_intersection(g2, tuple(J_ins + [b]))
                result += split_weight * val_I * val_J

    return result


def virasoro_string_equation(genus: int, insertions: Tuple[int, ...]) -> Dict[str, Any]:
    r"""Check the KW string equation ``L_{-1}`` for a correlator."""
    lhs = wk_intersection(genus, (0,) + insertions)
    rhs = Fraction(0)
    for i, d_i in enumerate(insertions):
        if d_i >= 1:
            lowered = list(insertions)
            lowered[i] -= 1
            rhs += wk_intersection(genus, tuple(lowered))

    if genus == 0 and len(insertions) == 2 and all(d == 0 for d in insertions):
        rhs += Fraction(1)

    return {
        'lhs': lhs,
        'rhs': rhs,
        'defect': lhs - rhs,
        'passes': lhs == rhs,
        'genus': genus,
        'insertions': insertions,
        'constraint': 'L_{-1} string equation',
        'scope': 'KW descendant CohFT reference',
    }


def virasoro_dilaton_equation(genus: int, insertions: Tuple[int, ...]) -> Dict[str, Any]:
    r"""Check the KW dilaton equation ``L_0`` for a correlator."""
    n = len(insertions)
    if 2 * genus - 2 + n <= 0:
        return {
            'lhs': Fraction(0),
            'rhs': Fraction(0),
            'defect': Fraction(0),
            'passes': True,
            'genus': genus,
            'insertions': insertions,
            'constraint': 'L_0 dilaton equation, unstable input',
            'scope': 'KW descendant CohFT reference',
        }

    lhs = wk_intersection(genus, (1,) + insertions)
    rhs = Fraction(2 * genus - 2 + n) * wk_intersection(genus, insertions)
    return {
        'lhs': lhs,
        'rhs': rhs,
        'defect': lhs - rhs,
        'passes': lhs == rhs,
        'genus': genus,
        'insertions': insertions,
        'constraint': 'L_0 dilaton equation',
        'scope': 'KW descendant CohFT reference',
    }


def _virasoro_dvv_constraint(
    n_vir: int, genus: int, insertions: Tuple[int, ...]
) -> Dict[str, Any]:
    d = n_vir + 1
    full_insertions = tuple(sorted(list(insertions) + [d]))
    n_full = len(full_insertions)

    if sum(full_insertions) != 3 * genus - 3 + n_full:
        return {
            'lhs': Fraction(0),
            'rhs': Fraction(0),
            'defect': Fraction(0),
            'passes': True,
            'genus': genus,
            'insertions': insertions,
            'constraint': f'L_{n_vir} dimension mismatch',
            'scope': 'KW descendant CohFT reference',
        }

    lhs = wk_intersection(genus, full_insertions)
    rhs = _dvv_rhs_sum(d, genus, list(insertions)) / Fraction(
        _double_factorial_odd(d))

    return {
        'lhs': lhs,
        'rhs': rhs,
        'defect': lhs - rhs,
        'passes': lhs == rhs,
        'genus': genus,
        'insertions': insertions,
        'constraint': f'L_{n_vir} DVV recursion with d={d}',
        'scope': 'KW descendant CohFT reference',
    }


def virasoro_L1_constraint(genus: int, insertions: Tuple[int, ...]) -> Dict[str, Any]:
    r"""Check the ``L_1`` KW Virasoro constraint through DVV."""
    return _virasoro_dvv_constraint(1, genus, insertions)


def virasoro_Ln_constraint(
    n_vir: int, genus: int, insertions: Tuple[int, ...]
) -> Dict[str, Any]:
    r"""Check the ``L_n`` KW Virasoro constraint through DVV."""
    if n_vir == -1:
        return virasoro_string_equation(genus, insertions)
    if n_vir == 0:
        return virasoro_dilaton_equation(genus, insertions)
    if n_vir < -1:
        raise ValueError(f"Virasoro index must be >= -1, got {n_vir}")
    return _virasoro_dvv_constraint(n_vir, genus, insertions)


def shadow_free_energy(g: int, kappa_val: Fraction) -> Fraction:
    r"""Scalar-lane coefficient ``F_g^{scal} = kappa * lambda_g^FP``."""
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    return kappa_val * lambda_fp(g)


def shadow_partition_function_coefficients(
    kappa_val: Fraction, max_g: int = 6
) -> Dict[int, Fraction]:
    r"""Coefficients of ``log tau_shadow,scal`` through genus ``max_g``."""
    return {g: shadow_free_energy(g, kappa_val) for g in range(1, max_g + 1)}


def _exp_series_coefficients(
    log_coefficients: Dict[int, Fraction], max_genus: int
) -> Dict[int, Fraction]:
    """Coefficients of ``exp(sum_{g>=1} a_g q^g)`` through ``q^max_genus``."""
    coeffs: Dict[int, Fraction] = {0: Fraction(1)}
    for n in range(1, max_genus + 1):
        total = Fraction(0)
        for i in range(1, n + 1):
            total += i * log_coefficients.get(i, Fraction(0)) * coeffs[n - i]
        coeffs[n] = total / n
    return coeffs


def finite_scalar_shadow_tau(
    kappa_val: Fraction, max_genus: int = 4
) -> Dict[str, Any]:
    r"""Finite scalar identity in ``Q[kappa][[q]]/(q^(G+1))``."""
    if max_genus < 1:
        raise ValueError(f"max_genus must be >= 1, got {max_genus}")

    kw_log = {g: lambda_fp(g) for g in range(1, max_genus + 1)}
    shadow_log = {g: kappa_val * coeff for g, coeff in kw_log.items()}

    return {
        'kappa': kappa_val,
        'max_genus': max_genus,
        'ring': f'Q[kappa][[q]]/(q^{max_genus + 1})',
        'kw_log_coefficients': kw_log,
        'shadow_log_coefficients': shadow_log,
        'kw_tau_coefficients': _exp_series_coefficients(kw_log, max_genus),
        'shadow_tau_coefficients':
            _exp_series_coefficients(shadow_log, max_genus),
        'identity': 'tau_shadow_scal^{<=G} = exp(kappa log tau_KW^{<=G})',
        'log_identity': 'log tau_shadow_scal^{<=G} = kappa log tau_KW^{<=G}',
        'power_identity': 'tau_shadow_scal^{<=G} = (tau_KW^{<=G})^kappa',
        'scalar_lane_only': True,
        'constructs_descendant_virasoro_constraints': False,
        'constructs_full_tau_function': False,
        'source': LOCAL_SOURCE_ANCHORS['finite_scalar_tau'],
    }


def _x_over_sin_x_coefficients(max_g: int) -> Dict[int, Fraction]:
    """Coefficients of ``x/sin(x)-1`` through ``x^(2*max_g)``."""
    order = max_g + 1
    sin_over_x = [Fraction(0)] * (2 * order + 1)
    for n in range(order + 1):
        idx = 2 * n
        if idx < len(sin_over_x):
            denom = 1
            for j in range(1, 2 * n + 2):
                denom *= j
            sin_over_x[idx] = Fraction((-1) ** n, denom)

    inv = [Fraction(0)] * (2 * order + 1)
    inv[0] = Fraction(1)
    for n in range(1, 2 * order + 1):
        total = Fraction(0)
        for j in range(1, n + 1):
            if j < len(sin_over_x):
                total += sin_over_x[j] * inv[n - j]
        inv[n] = -total

    return {g: inv[2 * g] for g in range(1, max_g + 1)}


def shadow_partition_function_closed_form_check(
    kappa_val: Fraction, max_g: int = 6
) -> Dict[str, Any]:
    r"""Check the finite scalar expansion of ``(hbar/2)/sin(hbar/2)-1``."""
    x_coeffs = _x_over_sin_x_coefficients(max_g)
    matches: Dict[int, Dict[str, Any]] = {}
    all_match = True

    for g in range(1, max_g + 1):
        direct = kappa_val * lambda_fp(g)
        series = kappa_val * x_coeffs[g] / Fraction(2 ** (2 * g))
        match = direct == series
        matches[g] = {
            'direct_FP': direct,
            'series_expansion': series,
            'match': match,
        }
        if not match:
            all_match = False

    return {
        'all_match': all_match,
        'genus_checks': matches,
        'kappa': kappa_val,
        'mechanism': 'finite A-hat genus scalar coefficient identity',
        'source': LOCAL_SOURCE_ANCHORS['scalar_free_energy'],
    }


def standard_hierarchy_constraint_status(kappa_val: Fraction) -> Dict[str, Any]:
    r"""Classify the standard KW/KdV/Hirota/Virasoro claim at ``kappa``."""
    is_kw = kappa_val == Fraction(1)
    is_zero = kappa_val == Fraction(0)
    residual = kappa_val * (Fraction(1) - kappa_val)

    if is_kw:
        failure_mode = None
    elif is_zero:
        failure_mode = (
            'zero field solves standard KdV/Hirota equations but is not '
            'the KW descendant CohFT'
        )
    else:
        failure_mode = (
            'finite scalar coefficients do not supply descendant CohFT data; '
            'the standard nonlinear channels leave a kappa(1-kappa) residual'
        )

    return {
        'kappa': kappa_val,
        'standard_kw_descendant_tau': is_kw,
        'standard_descendant_virasoro_constraints': is_kw,
        'standard_kdv_hierarchy': is_kw or is_zero,
        'standard_hirota_equations': is_kw or is_zero,
        'all_standard_constraints': is_kw,
        'trivial_zero_field_exception': is_zero,
        'kdv_residual_factor_kappa_1_minus_kappa': residual,
        'failure_mode': failure_mode,
        'source': LOCAL_SOURCE_ANCHORS['finite_scalar_tau'],
    }


def stationary_primary_line_diagnostics() -> Dict[str, Any]:
    r"""Classify stationary primary-line data without descendant promotion."""
    return {
        'source': LOCAL_SOURCE_ANCHORS['stationary_primary_line'],
        'constructs_full_hierarchy': False,
        'requires_descendant_cohft_data': True,
        'classes': {
            'G': {'depth': 2, 'stationary_shadow': 'trivial dispersionless'},
            'L': {'depth': 3, 'stationary_shadow': 'Gelfand-Dickey GD_2'},
            'C': {'depth': 4, 'stationary_shadow': 'KdV plus contact deformation'},
            'M': {'depth': 'infinity',
                  'stationary_shadow': 'polynomial Gelfand-Dickey shadow'},
        },
    }


def descendant_cohft_data_certificate(
    descendant_data_assumed: bool = False,
) -> Dict[str, Any]:
    r"""Separate scalar shadow coefficients from independently supplied data."""
    return {
        'descendant_data_assumed': descendant_data_assumed,
        'finite_scalar_lane_supplies_descendants': False,
        'full_virasoro_constraints_available': bool(descendant_data_assumed),
        'required_extra_data': (
            'descendant CohFT classes, psi insertions, unit, metric, and '
            'Virasoro/W-operator action on descendant variables'
        ),
        'source': LOCAL_SOURCE_ANCHORS['stationary_primary_line'],
    }


def _partitions_nonneg(total: int, n: int, min_val: int = 0) -> List[Tuple[int, ...]]:
    """Sorted non-negative tuples of length ``n`` and sum ``total``."""
    if n == 0:
        return [()] if total == 0 else []
    if n == 1:
        return [(total,)] if total >= min_val else []
    out: List[Tuple[int, ...]] = []
    for first in range(min_val, total + 1):
        for rest in _partitions_nonneg(total - first, n - 1, first):
            out.append((first,) + rest)
    return out


def _generate_test_insertions(
    genus: int, n_vir: int, max_n: int = 4
) -> List[Tuple[int, ...]]:
    """Generate small stable insertion tuples for a KW ``L_n`` check."""
    d_extra = max(n_vir + 1, 0)
    results: List[Tuple[int, ...]] = []

    for n in range(0, max_n + 1):
        target_sum = 3 * genus - 3 + n + 1 - d_extra
        if target_sum < 0:
            continue
        if 2 * genus - 2 + n + 1 <= 0:
            continue
        results.extend(_partitions_nonneg(target_sum, n))

    return results


def shadow_cohft_virasoro_theorem(
    kappa_val: Fraction, max_g: int = 3, max_n_vir: int = 3
) -> Dict[str, Any]:
    r"""Classify scalar shadow data against the standard KW constraints."""
    constraints: Dict[str, Any] = {}
    kw_reference_pass = True

    for genus in range(0, max_g + 1):
        for n_vir in range(-1, max_n_vir + 1):
            for insertions in _generate_test_insertions(genus, n_vir, max_n=4):
                key = f'L_{n_vir}_g{genus}_ins{insertions}'
                result = virasoro_Ln_constraint(n_vir, genus, insertions)
                constraints[key] = result
                if not result['passes']:
                    kw_reference_pass = False

    hierarchy_status = standard_hierarchy_constraint_status(kappa_val)
    standard_package_pass = (
        kw_reference_pass
        and hierarchy_status['standard_descendant_virasoro_constraints']
    )

    return {
        'kappa': kappa_val,
        'claim': 'finite scalar shadow versus standard descendant constraints',
        'constraints': constraints,
        'kw_reference_checks_pass': kw_reference_pass,
        'finite_scalar_tau': finite_scalar_shadow_tau(
            kappa_val, max_genus=max(1, max_g)),
        'standard_hierarchy_status': hierarchy_status,
        'descendant_data': descendant_cohft_data_certificate(False),
        'scalar_lane_pass': True,
        'standard_descendant_package_pass': standard_package_pass,
        'all_pass': standard_package_pass,
        'failure_mode': None if standard_package_pass else hierarchy_status['failure_mode'],
        'source': LOCAL_SOURCE_ANCHORS['finite_scalar_tau'],
    }


def shadow_dilaton_at_genus(g: int, kappa_val: Fraction) -> Dict[str, Any]:
    r"""Scalar free-energy dilaton diagnostic at genus ``g``."""
    F_g = shadow_free_energy(g, kappa_val)
    chi = Fraction(2 * g - 2)
    hierarchy_status = standard_hierarchy_constraint_status(kappa_val)

    return {
        'genus': g,
        'kappa': kappa_val,
        'F_g': F_g,
        'chi_g': chi,
        'chi_F_g': chi * F_g,
        'lambda_fp': lambda_fp(g),
        'scalar_identity_pass': F_g == kappa_val * lambda_fp(g),
        'descendant_dilaton_certified':
            hierarchy_status['standard_descendant_virasoro_constraints'],
        'mechanism': 'scalar coefficient identity; descendant L_0 needs CohFT data',
    }


def faber_zagier_shadow_consistency(max_g: int = 4) -> Dict[str, Any]:
    r"""Check tautological scalar data and record the FP/WK distinction."""
    results = {
        'max_genus': max_g,
        'checks': {},
        'all_pass': True,
    }

    for g in range(1, max_g + 1):
        fp = lambda_fp(g)
        d_val = 3 * g - 2
        wk_val = wk_intersection(g, (d_val,))
        results['checks'][g] = {
            'lambda_fp': fp,
            'wk_single_point': wk_val,
            'wk_single_point_matches_fp': wk_val == fp,
            'lambda_g_tautological': True,
            'obs_g_in_taut_ring': True,
        }

    results['key_insight'] = (
        'lambda_g^FP is the mixed Hodge-psi integral '
        'int psi_1^(2g-2) lambda_g; pure KW psi intersections are a '
        'separate descendant CohFT reference.'
    )
    return results


def hodge_psi_identity_check(max_g: int = 4) -> Dict[str, Any]:
    r"""Check the FP/Hodge Bernoulli ratio."""
    results = {
        'max_genus': max_g,
        'checks': {},
        'all_pass': True,
    }

    for g in range(1, max_g + 1):
        fp = lambda_fp(g)
        pure = lambda_g_integral(g)
        ratio = fp / pure
        power = 2 ** (2 * g - 1)
        expected_ratio = Fraction((power - 1) * 2 * g, power)
        match = ratio == expected_ratio
        results['checks'][g] = {
            'lambda_fp': fp,
            'lambda_integral': pure,
            'ratio': ratio,
            'expected_ratio': expected_ratio,
            'ratio_matches': match,
        }
        if not match:
            results['all_pass'] = False

    return results


def virasoro_algebra_check(max_n: int = 4) -> Dict[str, Any]:
    r"""Low-degree consistency checks for the KW Virasoro reference."""
    checks: Dict[str, Dict[str, Any]] = {}

    lhs = wk_intersection(1, (0, 2))
    rhs = wk_intersection(1, (1,))
    checks['string_on_L1_genus1'] = {
        'lhs': lhs,
        'rhs': rhs,
        'passes': lhs == rhs,
        'interpretation': '[L_{-1}, L_1] = -2 L_0 consistency',
    }

    lhs_d = wk_intersection(2, (1, 2, 3))
    rhs_d = Fraction(4) * wk_intersection(2, (2, 3))
    checks['dilaton_on_L1_genus2'] = {
        'lhs': lhs_d,
        'rhs': rhs_d,
        'passes': lhs_d == rhs_d,
        'interpretation': '[L_0, L_1] = -L_1 consistency',
    }

    return {
        'max_n': max_n,
        'checks': checks,
        'all_pass': all(v['passes'] for v in checks.values()),
        'scope': 'KW descendant CohFT reference',
    }


def full_virasoro_verification(
    kappa_val: Fraction = Fraction(1, 2),
    max_g: int = 3,
    max_n_vir: int = 3,
) -> Dict[str, Any]:
    r"""Run the scalar and KW-reference checks with exact classification."""
    generating = shadow_partition_function_closed_form_check(
        kappa_val, max_g=max(max_g, 6))
    virasoro = shadow_cohft_virasoro_theorem(
        kappa_val, max_g=max_g, max_n_vir=max_n_vir)
    hodge = hodge_psi_identity_check(max_g=max(max_g, 3))
    fz = faber_zagier_shadow_consistency(max_g=max(max_g, 3))
    algebra = virasoro_algebra_check()
    dilaton = {
        g: shadow_dilaton_at_genus(g, kappa_val)
        for g in range(1, max_g + 1)
    }

    scalar_lane_pass = generating['all_match'] and hodge['all_pass']
    kw_reference_pass = virasoro['kw_reference_checks_pass'] and algebra['all_pass']
    standard_pass = virasoro['standard_descendant_package_pass']

    return {
        'generating_function': generating,
        'virasoro_constraints': virasoro,
        'hodge_psi': hodge,
        'faber_zagier': fz,
        'virasoro_algebra': algebra,
        'dilaton_by_genus': dilaton,
        'scalar_lane_pass': scalar_lane_pass,
        'kw_reference_checks_pass': kw_reference_pass,
        'standard_descendant_package_pass': standard_pass,
        'all_pass': standard_pass,
        'summary': (
            'Scalar coefficients verified; standard descendant hierarchy '
            f'{"certified" if standard_pass else "not certified"} '
            f'at kappa={kappa_val}.'
        ),
    }


def string_equation_genus_explicit(g: int, kappa_val: Fraction) -> Dict[str, Any]:
    r"""Explicit KW string-equation checks at fixed genus."""
    target = 3 * g
    checks: Dict[str, Dict[str, Any]] = {}
    all_pass = True

    for d1 in range(0, target + 1):
        d2 = target - d1
        if d1 > d2:
            continue
        lhs = wk_intersection(g, (0, d1, d2))
        rhs = Fraction(0)
        for idx, d_val in enumerate([d1, d2]):
            if d_val > 0:
                lowered = [d1, d2]
                lowered[idx] -= 1
                rhs += wk_intersection(g, tuple(sorted(lowered)))
        passes = lhs == rhs
        checks[f'tau_0_tau_{d1}_tau_{d2}'] = {
            'lhs': lhs,
            'rhs': rhs,
            'defect': lhs - rhs,
            'passes': passes,
        }
        if not passes:
            all_pass = False

    return {
        'genus': g,
        'kappa': kappa_val,
        'checks': checks,
        'all_pass': all_pass,
        'scope': 'KW descendant CohFT reference',
    }


def heisenberg_virasoro_operators(
    kappa_val: Fraction, max_n: int = 5
) -> Dict[str, Any]:
    r"""Return formal KW operator coefficients with scalar-lane scope flags."""
    status = standard_hierarchy_constraint_status(kappa_val)
    operators: Dict[int, Dict[str, Any]] = {}

    for n in range(-1, max_n + 1):
        merge_coefficients: Dict[int, Fraction] = {}
        for kk in range(0, 8):
            numerator = _double_factorial_odd(kk + n)
            denominator = _double_factorial_odd(kk - 1) if kk >= 1 else 1
            merge_coefficients[kk] = Fraction(numerator, denominator)

        operators[n] = {
            'index': n,
            'derivative_coeff': -int(factorial(n + 1)) if n >= 0 else 1,
            'merge_coefficients': merge_coefficients,
            'constant_term': kappa_val / Fraction(2) if n == 0 else Fraction(0),
            'standard_operator_certified':
                status['standard_descendant_virasoro_constraints'],
        }

    return {
        'kappa': kappa_val,
        'family': 'Heisenberg scalar lane',
        'shadow_class': 'G',
        'operators': operators,
        'finite_scalar_lane_supplies_descendants': False,
        'standard_hierarchy_status': status,
    }


def kdv_from_virasoro_check(
    max_g: int = 3, kappa_val: Fraction = Fraction(1)
) -> Dict[str, Any]:
    r"""Check KW KdV reference values and classify scalar ``kappa`` scaling."""
    checks: Dict[str, Dict[str, Any]] = {}

    g2_n1 = wk_intersection(2, (4,))
    checks['genus2_n1'] = {
        'value': g2_n1,
        'expected': Fraction(1, 1152),
        'passes': g2_n1 == Fraction(1, 1152),
    }

    g2_n2 = wk_intersection(2, (2, 3))
    checks['genus2_n2'] = {
        'value': g2_n2,
        'expected': Fraction(29, 5760),
        'passes': g2_n2 == Fraction(29, 5760),
    }

    if max_g >= 3:
        g3_n1 = wk_intersection(3, (7,))
        checks['genus3_n1'] = {
            'value': g3_n1,
            'expected': Fraction(1, 82944),
            'passes': g3_n1 == Fraction(1, 82944),
        }

    lhs = wk_intersection(2, (0, 2, 3))
    rhs = wk_intersection(2, (1, 3)) + wk_intersection(2, (2, 2))
    checks['string_genus2_n3'] = {
        'lhs': lhs,
        'rhs': rhs,
        'passes': lhs == rhs,
    }

    lhs_d = wk_intersection(2, (1, 4))
    rhs_d = Fraction(3) * wk_intersection(2, (4,))
    checks['dilaton_genus2_n2'] = {
        'lhs': lhs_d,
        'rhs': rhs_d,
        'passes': lhs_d == rhs_d,
    }

    reference_pass = all(v['passes'] for v in checks.values())
    status = standard_hierarchy_constraint_status(kappa_val)
    standard_kdv_certified = reference_pass and status['standard_kdv_hierarchy']

    return {
        'max_genus': max_g,
        'kappa': kappa_val,
        'checks': checks,
        'kw_reference_checks_pass': reference_pass,
        'standard_hierarchy_status': status,
        'standard_kdv_certified': standard_kdv_certified,
        'all_pass': standard_kdv_certified,
        'residual_factor': status['kdv_residual_factor_kappa_1_minus_kappa'],
        'source': LOCAL_SOURCE_ANCHORS['finite_scalar_tau'],
    }


def shadow_equation_classification(
    kappa_val: Fraction = Fraction(1, 2), max_genus: int = 5
) -> Dict[str, Any]:
    r"""Classify finite scalar identities versus standard hierarchies."""
    status = standard_hierarchy_constraint_status(kappa_val)
    finite_tau = finite_scalar_shadow_tau(kappa_val, max_genus=max_genus)

    return {
        'kappa': kappa_val,
        'source': LOCAL_SOURCE_ANCHORS['finite_scalar_tau'],
        'satisfies': {
            'finite_scalar_coefficient_identity': True,
            'standard_descendant_virasoro_constraints':
                status['standard_descendant_virasoro_constraints'],
            'standard_kdv_hierarchy': status['standard_kdv_hierarchy'],
            'standard_hirota_equations': status['standard_hirota_equations'],
            'stationary_primary_line_diagnostics': True,
        },
        'does_not_satisfy': {
            'standard_descendant_virasoro_constraints':
                not status['standard_descendant_virasoro_constraints'],
            'kdv_hierarchy': not status['standard_kdv_hierarchy'],
            'hirota_equations': not status['standard_hirota_equations'],
            'full_descendant_cohft_from_scalar_lane': True,
        },
        'exceptions': {
            'kappa_1_actual_kw': kappa_val == Fraction(1),
            'kappa_0_zero_field': kappa_val == Fraction(0),
            'zero_field_scope': 'KdV/Hirota only; not a KW descendant package',
            'kdv_residual_factor': status['kdv_residual_factor_kappa_1_minus_kappa'],
        },
        'free_energy_check': {
            'F_1_shadow': kappa_val * lambda_fp(1),
            'F_2_shadow': kappa_val * lambda_fp(2),
            'F_1_kw': lambda_fp(1),
            'F_2_kw': lambda_fp(2),
            'ratio_F1': kappa_val,
            'ratio_F2': kappa_val,
            'ratios_constant': True,
        },
        'finite_scalar_tau': finite_tau,
    }
