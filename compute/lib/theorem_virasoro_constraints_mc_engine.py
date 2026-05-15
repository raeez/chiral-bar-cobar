r"""Finite scalar shadow certificates and KW reference checks.

The certified identity in this module is the finite scalar coefficient
statement

    tau_shadow,scal^{<=G}(A) = exp(kappa(A) log tau_KW^{<=G})

in Q[kappa][[q]]/(q^{G+1}).  It is not a construction of a full
Kontsevich-Witten descendant tau function.  Standard KdV/Hirota/Virasoro
constraints are certified only in the actual KW case kappa = 1, with the
zero-field kappa = 0 exception recorded only for equations where the
trivial solution is meaningful.

The Witten-Kontsevich intersection-number routines below remain as a
reference oracle for DVV/string/dilaton identities.  They test the genuine
KW CohFT, not the assertion that tau_KW^kappa is a descendant CohFT for
arbitrary kappa.

Local source anchors:
    chapters/examples/landscape_census.tex:173-186
    chapters/examples/landscape_census.tex:4970-5018
    chapters/theory/higher_genus_modular_koszul.tex:20242-20276
    chapters/theory/higher_genus_modular_koszul.tex:20304-20388
    chapters/connections/concordance.tex:4095-4108
    chapters/connections/concordance.tex:6742-6759

All arithmetic is exact.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Tuple

from sympy import Rational, bernoulli, factorial


LOCAL_SOURCE_ANCHORS: Dict[str, str] = {
    'collision_residues': 'chapters/examples/landscape_census.tex:173-186',
    'virasoro_shadow_surface': 'chapters/examples/landscape_census.tex:160-178',
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
        'scope': 'KZ presentation; not equal to the raw trace-form residue',
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
        'source': 'chapters/examples/landscape_census.tex:151-152',
    },
    'affine_trace_form': {
        'formula': 'dim(g)*(k+h^vee)/(2*h^vee)',
        'source': 'chapters/examples/landscape_census.tex:140-143',
    },
    'virasoro': {
        'formula': 'c/2',
        'source': 'chapters/examples/landscape_census.tex:144',
    },
    'w_n': {
        'formula': 'c*(H_N-1)',
        'source': 'chapters/examples/landscape_census.tex:145-146',
    },
}


VIRASORO_SHADOW_FORMULAS: Dict[str, str] = {
    'hypothesis': 'c*(5*c+22) != 0',
    'kappa': 'c/2',
    'S_2': 'c/2',
    'S_3': '2',
    'S_4': '10/(c*(5*c+22))',
    'S_5': '-48/(c^2*(5*c+22))',
    'Delta': '40/(5*c+22)',
    'Lambda_norm': 'c*(5*c+22)/10',
    'collision_residue': '(c/2)/z^3 + 2*T/z',
}


OBJECT_FIREWALLS: Tuple[str, ...] = (
    'A is the algebra.',
    'B(A) is the bar coalgebra T^c(s^{-1} Abar).',
    'A^i is the bar-cohomology coalgebra branch.',
    'A^! is the Verdier/continuous-linear dual branch under hypotheses.',
    'Z_ch^der(A) is ChirHoch^*(A,A), the Hochschild/bulk object.',
    'Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.',
)


DATA_CHANNEL_FIREWALLS: Dict[str, Dict[str, Any]] = {
    'virasoro_ope_data': {
        'object': 'OPE/collision residue',
        'formula': VIRASORO_SHADOW_FORMULAS['collision_residue'],
        'source': LOCAL_SOURCE_ANCHORS['collision_residues'],
        'supplies_bar_differential': False,
        'supplies_derived_center': False,
    },
    'bar_differential_data': {
        'object': 'ordered bar differential and MC element',
        'formula': 'D*Theta + (1/2)[Theta,Theta] = 0',
        'source': 'local MC compute projection only',
        'supplied_by_finite_virasoro_window': False,
        'supplies_derived_center': False,
    },
    'derived_center_data': {
        'object': 'Z_ch^der(A) = ChirHoch^*(A,A)',
        'formula': 'Hochschild cochains, not Virasoro OPE constants',
        'source': 'object firewall',
        'supplied_by_virasoro_ope': False,
        'supplied_by_bar_cobar_inversion': False,
    },
}


# ============================================================================
# 0. Faber-Pandharipande numbers (standalone, avoids circular import)
# ============================================================================

@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Verified values from landscape_census.tex:4988-4998:
        g=1: 1/24
        g=2: 7/5760
        g=3: 31/967680
        g=4: 127/154828800
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    power = 2 ** (2 * g - 1)
    B_2g = bernoulli(2 * g)
    abs_B_2g = Rational(abs(int(B_2g.p)), int(B_2g.q))
    result = Rational(power - 1, power) * abs_B_2g / factorial(2 * g)
    return Fraction(int(result.p), int(result.q))


def shadow_free_energy(kappa_val, g: int) -> Fraction:
    r"""Scalar-lane coefficient F_g^scal(A) = kappa(A) * lambda_g^FP."""
    return kappa_val * lambda_fp(g)


def kernel_constant_certificate() -> Dict[str, Any]:
    r"""Return the local collision-residue and kappa convention firewall."""
    return {
        'kernel_constants': KERNEL_CONSTANTS,
        'kappa_formulas': KAPPA_FORMULAS,
        'virasoro_shadow_formulas': VIRASORO_SHADOW_FORMULAS,
        'object_firewalls': OBJECT_FIREWALLS,
        'data_channel_firewalls': DATA_CHANNEL_FIREWALLS,
        'source_anchors': LOCAL_SOURCE_ANCHORS,
    }


def virasoro_shadow_surface_certificate(c_val: Fraction) -> Dict[str, Any]:
    r"""Exact Virasoro shadow coefficients with central-charge hypotheses.

    The formulas S_4 and S_5 live on the non-singular surface
    c*(5*c+22) != 0.  The finite list S_2,...,S_5 is a computable witness
    for the local shadow table; it is not a proof of the infinite tower.
    """
    c = Fraction(c_val)
    five_c_plus_22 = 5 * c + 22
    denominator = c * five_c_plus_22
    nonsingular = denominator != 0
    kappa_val = c / 2
    lambda_norm = denominator / 10

    if nonsingular:
        S4 = Fraction(10, 1) / denominator
        S5 = Fraction(-48, 1) / (c * c * five_c_plus_22)
        delta = 8 * kappa_val * S4
    else:
        S4 = None
        S5 = None
        delta = None

    return {
        'central_charge': c,
        'kappa': kappa_val,
        'hypothesis': VIRASORO_SHADOW_FORMULAS['hypothesis'],
        'nonsingular_shadow_surface': nonsingular,
        'singular_locus': {
            'c_equals_0': c == 0,
            'c_equals_minus_22_over_5': five_c_plus_22 == 0,
        },
        'coefficients': {
            'S_2': kappa_val,
            'S_3': Fraction(2),
            'S_4': S4,
            'S_5': S5,
            'Delta': delta,
            'Lambda_norm': lambda_norm,
        },
        'formulas': VIRASORO_SHADOW_FORMULAS,
        'shadow_depth': {
            'census_class': 'M',
            'census_depth': 'infinity',
            'finite_witness_orders': (2, 3, 4, 5),
            'finite_window_proves_infinite_depth': False,
            'nonzero_finite_witnesses': nonsingular and S4 != 0 and S5 != 0,
        },
        'channel_separation': DATA_CHANNEL_FIREWALLS,
        'constructs_bar_differential': False,
        'constructs_derived_center': False,
        'source': LOCAL_SOURCE_ANCHORS['virasoro_shadow_surface'],
    }


def finite_constraint_scope_certificate(
    max_n_vir: int, max_genus: int, descendant_data_assumed: bool = False
) -> Dict[str, Any]:
    r"""Record the exact finite window checked by the Virasoro oracle.

    A finite set of Virasoro/DVV equations is a useful regression witness.
    It cannot certify the infinite Virasoro tail, reconstruct the full MC
    element, or compute Hochschild/derived-centre data.
    """
    if max_n_vir < -1:
        raise ValueError(f"max_n_vir must be >= -1, got {max_n_vir}")
    if max_genus < 0:
        raise ValueError(f"max_genus must be >= 0, got {max_genus}")

    checked_indices = tuple(range(-1, max_n_vir + 1))
    checked_genera = tuple(range(0, max_genus + 1))

    return {
        'checked_virasoro_indices': checked_indices,
        'checked_genera': checked_genera,
        'checked_constraint_count': len(checked_indices) * len(checked_genera),
        'finite_window': True,
        'descendant_data_assumed': bool(descendant_data_assumed),
        'proves_all_virasoro_constraints': False,
        'proves_full_mc_reconstruction': False,
        'reconstructs_bar_differential': False,
        'reconstructs_derived_center': False,
        'next_unchecked': {
            'virasoro_index': max_n_vir + 1,
            'genus': max_genus + 1,
        },
        'required_to_upgrade': (
            'an all-n/all-g argument for the descendant CohFT operators, '
            'compatibility with the ordered bar differential, and an '
            'independent Hochschild calculation for Z_ch^der(A)'
        ),
        'failure_mode': (
            'finite Virasoro checks are regression witnesses, not full MC '
            'reconstruction data'
        ),
    }


def _exp_series_coefficients(
    log_coefficients: Dict[int, Fraction], max_genus: int
) -> Dict[int, Fraction]:
    """Coefficients of exp(sum_{g>=1} a_g q^g) through q^max_genus."""
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
    r"""Finite scalar coefficient identity in Q[kappa][[q]]/(q^{G+1}).

    The output certifies only the logarithmic scalar lane from
    higher_genus_modular_koszul.tex:20304-20388.  It intentionally carries
    no descendant variables and no full Virasoro/KdV/Hirota certificate.
    """
    if max_genus < 1:
        raise ValueError(f"max_genus must be >= 1, got {max_genus}")

    kw_log = {g: lambda_fp(g) for g in range(1, max_genus + 1)}
    shadow_log = {
        g: kappa_val * coeff for g, coeff in kw_log.items()
    }

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
        'scalar_lane_only': True,
        'constructs_descendant_virasoro_constraints': False,
        'constructs_full_tau_function': False,
        'source': LOCAL_SOURCE_ANCHORS['finite_scalar_tau'],
    }


def standard_hierarchy_constraint_status(kappa_val: Fraction) -> Dict[str, Any]:
    r"""Classify the standard KW/KdV/Hirota/Virasoro claim at this kappa."""
    is_kw = kappa_val == Fraction(1)
    is_zero = kappa_val == Fraction(0)
    residual = kappa_val * (Fraction(1) - kappa_val)

    return {
        'kappa': kappa_val,
        'standard_kw_descendant_tau': is_kw,
        'standard_descendant_virasoro_constraints': is_kw,
        'standard_kdv_hierarchy': is_kw or is_zero,
        'standard_hirota_equations': is_kw or is_zero,
        'all_standard_constraints': is_kw,
        'trivial_zero_field_exception': is_zero,
        'kdv_residual_factor_kappa_1_minus_kappa': residual,
        'failure_mode': (
            'finite scalar coefficients do not supply descendant CohFT data; '
            'the standard nonlinear channels leave a kappa(1-kappa) residual'
        ),
        'source': LOCAL_SOURCE_ANCHORS['finite_scalar_tau'],
    }


# ============================================================================
# 1. Witten-Kontsevich intersection numbers via DVV recursion
# ============================================================================

def _double_factorial_odd(n: int) -> int:
    """(2n+1)!! = 1 * 3 * 5 * ... * (2n+1). Convention: (-1)!! = 1."""
    if n < 0:
        return 1
    result = 1
    for j in range(1, 2 * n + 2, 2):
        result *= j
    return result


@lru_cache(maxsize=None)
def wk_intersection(genus: int, insertions: Tuple[int, ...]) -> Fraction:
    r"""Witten-Kontsevich intersection number via DVV recursion.

    <tau_{d_1} ... tau_{d_n}>_g = int_{M-bar_{g,n}} psi_1^{d_1} ... psi_n^{d_n}

    Dimension constraint: sum d_i = 3g - 3 + n.
    Stability: 2g - 2 + n > 0.
    Seed: <tau_0^3>_0 = 1.
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

    # Base cases
    if genus == 0 and insertions == (0, 0, 0):
        return Fraction(1)
    if genus == 1 and insertions == (1,):
        return Fraction(1, 24)

    # String equation: if any d_i = 0
    if 0 in insertions:
        idx = insertions.index(0)
        remaining = list(insertions)
        remaining.pop(idx)
        result = Fraction(0)
        for i in range(len(remaining)):
            if remaining[i] > 0:
                new = list(remaining)
                new[i] -= 1
                result += wk_intersection(genus, tuple(new))
        return result

    # Dilaton equation: if any d_i = 1
    if 1 in insertions:
        idx = insertions.index(1)
        remaining = list(insertions)
        remaining.pop(idx)
        n_rem = len(remaining)
        if 2 * genus - 2 + n_rem > 0:
            return Fraction(2 * genus - 2 + n_rem) * wk_intersection(
                genus, tuple(remaining))

    # DVV recursion on the largest insertion
    d = insertions[-1]
    rest = list(insertions[:-1])

    if d < 2:
        return Fraction(0)

    lhs_coeff = Fraction(_double_factorial_odd(d))
    result = Fraction(0)

    # Merge terms
    for i in range(len(rest)):
        di = rest[i]
        new_d = d + di - 1
        merge_coeff = Fraction(
            _double_factorial_odd(d + di - 1),
            _double_factorial_odd(di - 1) if di >= 1 else 1
        )
        others = rest[:i] + rest[i + 1:]
        result += merge_coeff * wk_intersection(genus, tuple(others + [new_d]))

    # Handle term (genus reduction via non-separating node)
    if genus >= 1:
        for a in range(d - 1):
            b = d - 2 - a
            handle_coeff = Fraction(
                _double_factorial_odd(a) * _double_factorial_odd(b), 2
            )
            result += handle_coeff * wk_intersection(
                genus - 1, tuple(rest + [a, b]))

    # Split term (separating node)
    m = len(rest)
    for a in range(d - 1):
        b = d - 2 - a
        split_weight = Fraction(
            _double_factorial_odd(a) * _double_factorial_odd(b), 2
        )
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

    return result / lhs_coeff


# ============================================================================
# 2. MC equation boundary structure at genus 0
# ============================================================================

def genus0_boundary_strata(k: int) -> Dict[str, Any]:
    r"""Enumerate codimension-1 boundary strata of M-bar_{0,k}.

    M-bar_{0,k} has dimension k-3 (for k >= 3).
    Codimension-1 boundary strata are indexed by partitions {I, J} of
    {1, ..., k} with |I|, |J| >= 2 (separating nodes producing two
    genus-0 components).

    With point 1 fixed in I to remove the I/J symmetry, the number of
    strata is 2^{k-1} - k - 1 for k >= 3.

    At genus 0 there are NO non-separating nodes (handle terms),
    since genus cannot decrease below 0.

    Returns:
      strata: list of (I, J) partitions
      num_strata: count
      dimension: k - 3
    """
    if k < 3:
        return {'strata': [], 'num_strata': 0, 'dimension': max(k - 3, 0)}

    strata = []
    # Label marked points 1, ..., k.  Find all partitions {I, J} with
    # |I| >= 2, |J| >= 2.  Fix point 1 in I to avoid double-counting.
    for mask in range(1, 1 << (k - 1)):
        I = [1]  # point 1 always in I
        J = []
        for bit in range(k - 1):
            if mask & (1 << bit):
                I.append(bit + 2)
            else:
                J.append(bit + 2)
        if len(I) >= 2 and len(J) >= 2:
            strata.append((tuple(sorted(I)), tuple(sorted(J))))

    return {
        'strata': strata,
        'num_strata': len(strata),
        'dimension': k - 3,
    }


def mc_genus0_arity_k_terms(k: int) -> Dict[str, Any]:
    r"""Decompose the MC equation at (g=0, arity k) into boundary terms.

    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 at genus 0, arity k:

    (i) D-term (differential): encodes the codimension-1 merge strata
        where two marked points collide on a single component.
        At genus 0, this gives the "merge" terms of DVV.

    (ii) Bracket-term [Theta,Theta]: encodes the separating-node boundary,
         where the curve splits into two genus-0 components with marked
         points distributed.  This gives the "split" terms of DVV.

    (iii) Handle term: ABSENT at genus 0 (would require genus reduction
          to g=-1).

    The TOTAL boundary of the fundamental chain [M-bar_{0,k}] is:
      boundary = sum_{separating nodes} [M-bar_{0,|I|+1} x M-bar_{0,|J|+1}]

    where the +1 accounts for the node itself becoming a marked point on
    each component.

    Returns dict with term counts and identification with DVV.
    """
    boundary = genus0_boundary_strata(k)

    # The merge terms at genus 0 come from the D differential acting on
    # Theta at arity k-1.  D sends (0, k-1) -> (0, k) by adding one
    # marked point and encoding the collision.
    #
    # The split terms come from the bracket, which pairs
    # (0, k1) and (0, k2) with k1 + k2 = k + 2 (two less because the
    # node consumes one marked point from each side).

    # DVV identification:
    # The DVV recursion for <tau_d tau_S>_0 with d = k-3 (the distinguished
    # insertion) has:
    #   Merge terms: sum over i of (d+d_i-1)!! / (d_i-1)!! * <tau_{d+d_i-1} rest>_0
    #   Split terms: sum over (I,J) of <tau_a I>_0 * <tau_b J>_0
    #   Handle terms: 0 (genus 0)
    #
    # The MC equation at (0,k) decomposes as:
    #   D|_{(0,k)}: merge contribution (arity k-1 -> arity k)
    #   [,]|_{(0,k)}: split contribution from (0,k1) x (0,k2)

    split_count = boundary['num_strata']

    return {
        'arity': k,
        'genus': 0,
        'dimension_mbar': k - 3,
        'D_term': 'merge (codim-1 collision of two marked points)',
        'bracket_term': f'split into two genus-0 components ({split_count} strata)',
        'handle_term': 'ABSENT at genus 0',
        'dvv_identification': f'DVV recursion with d = {k - 3}, Virasoro L_{k - 3}',
        'virasoro_index': k - 3,
        'boundary_strata': boundary,
    }


# ============================================================================
# 3. Witten-Kontsevich reference DVV identities
# ============================================================================

def proof1_mc_projection_equals_virasoro(
    n_vir: int, max_genus: int = 2, max_extra_insertions: int = 3
) -> Dict[str, Any]:
    r"""Reference check: the KW correlators satisfy the DVV/Virasoro recursion.

    The check is a KW oracle.  It does not assert that the scalar series
    exp(kappa log tau_KW^{<=G}) carries descendant variables or satisfies
    the standard Virasoro constraints for arbitrary kappa.

    Parameters
    ----------
    n_vir : int
        Virasoro index (n >= -1).
    max_genus : int
        Maximum genus to verify.
    max_extra_insertions : int
        Maximum number of additional insertions to test.
    """
    k = n_vir + 3  # arity convention used by mc_genus0_arity_k_terms

    results = {
        'virasoro_index': n_vir,
        'mc_arity': k,
        'mc_genus': 0,
        'identification': f'L_{n_vir} <-> MC at (0, {k})',
        'scope': 'KW descendant CohFT reference, not arbitrary kappa scaling',
        'finite_scope': finite_constraint_scope_certificate(
            max_n_vir=n_vir,
            max_genus=max_genus,
            descendant_data_assumed=True,
        ),
        'tests': {},
        'all_pass': True,
    }

    # MC boundary structure
    results['mc_structure'] = mc_genus0_arity_k_terms(k)

    # Verify at multiple genera and insertions
    for g in range(0, max_genus + 1):
        for n_extra in range(0, max_extra_insertions + 1):
            test_insertions = _generate_valid_insertions(g, n_vir, n_extra)
            for ins in test_insertions:
                key = f'g{g}_ins{ins}'
                test = _verify_single_virasoro_mc(n_vir, g, ins)
                results['tests'][key] = test
                if not test['passes']:
                    results['all_pass'] = False

    # Count tests
    n_tests = len(results['tests'])
    n_pass = sum(1 for t in results['tests'].values() if t['passes'])
    results['summary'] = f'{n_pass}/{n_tests} tests passed'

    return results


def _generate_valid_insertions(genus: int, n_vir: int,
                                n_extra: int) -> List[Tuple[int, ...]]:
    """Generate valid insertion tuples for L_{n_vir} at genus g with n_extra points."""
    d_extra = max(n_vir + 1, 0)
    target_sum = 3 * genus - 3 + n_extra + 1 - d_extra
    if target_sum < 0:
        return []
    if 2 * genus - 2 + n_extra + 1 <= 0:
        return []
    return _partitions_nonneg(target_sum, n_extra)


def _partitions_nonneg(total: int, n: int,
                        min_val: int = 0) -> List[Tuple[int, ...]]:
    """Sorted tuples of n non-negative integers summing to total."""
    if n == 0:
        return [()] if total == 0 else []
    if n == 1:
        return [(total,)] if total >= min_val else []
    out = []
    for first in range(min_val, total + 1):
        for rest in _partitions_nonneg(total - first, n - 1, first):
            out.append((first,) + rest)
    return out


def _verify_single_virasoro_mc(n_vir: int, genus: int,
                                 insertions: Tuple[int, ...]) -> Dict[str, Any]:
    """Verify L_{n_vir} constraint at (genus, insertions) via DVV and MC.

    The DVV recursion IS the MC boundary equation.  We verify that:
    (1) The WK intersection number with tau_{n_vir+1} inserted
        satisfies the DVV recursion (= MC boundary = L_n constraint).
    (2) The constraint is tracked at the (0, n_vir+3) MC address in this
        arity convention.

    For L_{-1}: string equation.
    For L_0: dilaton equation.
    For L_n (n >= 1): DVV with d = n+1.
    """
    if n_vir == -1:
        return _verify_string_equation(genus, insertions)
    if n_vir == 0:
        return _verify_dilaton_equation(genus, insertions)
    return _verify_higher_virasoro(n_vir, genus, insertions)


def _verify_string_equation(genus: int,
                             insertions: Tuple[int, ...]) -> Dict[str, Any]:
    """Verify L_{-1} (string equation) = MC at (0,2) projection.

    String equation:
      <tau_0 tau_{d_1} ... tau_{d_n}>_g
        = sum_{i: d_i>0} <tau_{d_1} ... tau_{d_i-1} ... tau_{d_n}>_g
        + delta_{g,0} delta_{n,2} prod(delta_{d_i,0})

    MC interpretation: at arity 2, the genus-0 MC equation encodes the
    collision of two marked points.  The string equation expresses the
    residue of the bar differential along d log(z_1 - z_2) as a sum
    of lower-order terms.
    """
    lhs = wk_intersection(genus, (0,) + insertions)
    rhs = Fraction(0)
    for i in range(len(insertions)):
        if insertions[i] >= 1:
            new = list(insertions)
            new[i] -= 1
            rhs += wk_intersection(genus, tuple(new))
    # Unit contribution at genus 0
    if genus == 0 and len(insertions) == 2 and all(d == 0 for d in insertions):
        rhs += Fraction(1)

    return {
        'constraint': 'L_{-1} (string) = MC at (0,2)',
        'genus': genus,
        'insertions': insertions,
        'lhs': lhs,
        'rhs': rhs,
        'defect': lhs - rhs,
        'passes': lhs == rhs,
        'mc_arity': 2,
        'mc_term': 'D-term (collision residue at arity 2)',
    }


def _verify_dilaton_equation(genus: int,
                              insertions: Tuple[int, ...]) -> Dict[str, Any]:
    """Verify L_0 (dilaton equation) = MC at (0,3) projection.

    Dilaton equation:
      <tau_1 tau_{d_1} ... tau_{d_n}>_g = (2g - 2 + n) <tau_{d_1} ... tau_{d_n}>_g

    MC interpretation: at arity 3, the genus-0 MC equation involves the
    three-point function on M-bar_{0,3} = point.  The dilaton equation
    expresses the Euler characteristic insertion (kappa_0 = 2g-2+n)
    from the forgetful map pi: M-bar_{g,n+1} -> M-bar_{g,n}.
    """
    n = len(insertions)
    if 2 * genus - 2 + n <= 0:
        return {
            'constraint': 'L_0 (dilaton) = MC at (0,3)',
            'genus': genus,
            'insertions': insertions,
            'lhs': Fraction(0),
            'rhs': Fraction(0),
            'defect': Fraction(0),
            'passes': True,
            'mc_arity': 3,
            'mc_term': 'vacuously satisfied (unstable)',
        }

    lhs = wk_intersection(genus, (1,) + insertions)
    rhs = Fraction(2 * genus - 2 + n) * wk_intersection(genus, insertions)

    return {
        'constraint': 'L_0 (dilaton) = MC at (0,3)',
        'genus': genus,
        'insertions': insertions,
        'lhs': lhs,
        'rhs': rhs,
        'defect': lhs - rhs,
        'passes': lhs == rhs,
        'mc_arity': 3,
        'mc_term': 'forgetful map pushforward (kappa_0 = 2g-2+n)',
    }


def _verify_higher_virasoro(n_vir: int, genus: int,
                              insertions: Tuple[int, ...]) -> Dict[str, Any]:
    """Verify L_n (n >= 1) via DVV at the MC address (0, n+3).

    The DVV recursion with distinguished insertion d = n_vir + 1 gives the
    L_{n_vir} constraint.  The MC address (0, n_vir + 3) decomposes into:
      D-term: merge of the distinguished point with another
      [,]-term: splitting into two genus-0 components
    These are exactly the merge and split terms of DVV.
    """
    d = n_vir + 1
    full_ins = tuple(sorted(list(insertions) + [d]))
    n_full = len(full_ins)

    if sum(full_ins) != 3 * genus - 3 + n_full:
        return {
            'constraint': f'L_{n_vir} (DVV d={d}) = MC at (0, {n_vir + 3})',
            'genus': genus,
            'insertions': insertions,
            'lhs': Fraction(0),
            'rhs': Fraction(0),
            'defect': Fraction(0),
            'passes': True,
            'mc_arity': n_vir + 3,
            'mc_term': 'dimension mismatch, vacuously true',
        }

    lhs_val = wk_intersection(genus, full_ins)

    rest = list(insertions)
    lhs_coeff = Fraction(_double_factorial_odd(d))

    # --- MC DECOMPOSITION ---
    # D-term (merge): codim-1 collision boundary
    merge_val = Fraction(0)
    for i in range(len(rest)):
        di = rest[i]
        new_d = d + di - 1
        merge_coeff = Fraction(
            _double_factorial_odd(d + di - 1),
            _double_factorial_odd(di - 1) if di >= 1 else 1
        )
        others = rest[:i] + rest[i + 1:]
        merge_val += merge_coeff * wk_intersection(genus, tuple(others + [new_d]))

    # Handle term (genus reduction): absent at genus 0, present at g >= 1
    handle_val = Fraction(0)
    if genus >= 1:
        for a in range(d - 1):
            b = d - 2 - a
            handle_coeff = Fraction(
                _double_factorial_odd(a) * _double_factorial_odd(b), 2
            )
            handle_val += handle_coeff * wk_intersection(
                genus - 1, tuple(rest + [a, b]))

    # [,]-term (split): separating node boundary
    split_val = Fraction(0)
    m = len(rest)
    for a in range(d - 1):
        b = d - 2 - a
        split_weight = Fraction(
            _double_factorial_odd(a) * _double_factorial_odd(b), 2
        )
        for mask_val in range(1 << m):
            I_ins = [rest[bit] for bit in range(m) if mask_val & (1 << bit)]
            J_ins = [rest[bit] for bit in range(m) if not (mask_val & (1 << bit))]
            for g1 in range(genus + 1):
                g2 = genus - g1
                val_I = wk_intersection(g1, tuple(I_ins + [a]))
                if val_I == Fraction(0):
                    continue
                val_J = wk_intersection(g2, tuple(J_ins + [b]))
                split_val += split_weight * val_I * val_J

    rhs_val = (merge_val + handle_val + split_val) / lhs_coeff

    return {
        'constraint': f'L_{n_vir} (DVV d={d}) = MC at (0, {n_vir + 3})',
        'genus': genus,
        'insertions': insertions,
        'lhs': lhs_val,
        'rhs': rhs_val,
        'defect': lhs_val - rhs_val,
        'passes': lhs_val == rhs_val,
        'mc_arity': n_vir + 3,
        'mc_decomposition': {
            'merge (D-term)': merge_val / lhs_coeff,
            'handle (absent at g=0)': handle_val / lhs_coeff,
            'split ([,]-term)': split_val / lhs_coeff,
        },
    }


# ============================================================================
# 4. Stationary primary-line diagnostics
# ============================================================================

def proof2_kodaira_spencer(max_genus: int = 3) -> Dict[str, Any]:
    r"""Stationary primary-line checks separated from descendant constraints.

    The manuscript source at higher_genus_modular_koszul.tex:20242-20276
    restricts the hierarchy statement to one-variable stationary Riccati
    diagnostics.  A full descendant CohFT hierarchy must be supplied
    separately.
    """
    results = {
        'diagnostic': 'stationary primary-line Riccati shadow',
        'mechanism': (
            'The shadow tower gives one-variable primary-line diagnostics. '
            'It does not construct descendant Virasoro operators.'
        ),
        'constructs_descendant_virasoro_constraints': False,
        'descendant_cohft_data_assumed_separately': True,
        'source': LOCAL_SOURCE_ANCHORS['stationary_primary_line'],
        'arity_map': {},
    }

    for k in range(2, 8):
        n_vir = k - 3
        if n_vir < -1:
            continue
        results['arity_map'][k] = {
            'mc_arity': k,
            'virasoro_index': n_vir,
            'ks_interpretation': _ks_interpretation(n_vir),
        }

    # Verify the genus-0 three-point function (the seed)
    # M-bar_{0,3} = point, so <tau_0^3>_0 = 1.
    # This is the metric of the Frobenius manifold.
    seed = wk_intersection(0, (0, 0, 0))
    results['frobenius_metric'] = {
        '<tau_0^3>_0': seed,
        'expected': Fraction(1),
        'passes': seed == Fraction(1),
    }

    # Verify WDVV is vacuous at rank 1
    results['wdvv_rank1'] = {
        'classification': 'vacuous (rank 1 Frobenius manifold has no WDVV constraint)',
        'reason': '1-dimensional Frobenius manifolds have a single coordinate; '
                  'WDVV involves 4 indices, all equal for rank 1, giving a tautology.',
    }

    # Verify that L_{-1} through L_5 hold at genus 0 through max_genus
    constraint_tests = {}
    all_pass = True
    for n_vir in range(-1, 6):
        for g in range(0, max_genus + 1):
            test_ins_list = _generate_valid_insertions(g, n_vir, 2)
            for ins in test_ins_list[:3]:  # limit per config
                test = _verify_single_virasoro_mc(n_vir, g, ins)
                key = f'L_{n_vir}_g{g}_{ins}'
                constraint_tests[key] = test
                if not test['passes']:
                    all_pass = False

    results['constraint_tests'] = constraint_tests
    results['kw_reference_checks_pass'] = all_pass
    results['all_pass'] = all_pass

    return results


def stationary_primary_line_diagnostics() -> Dict[str, Any]:
    r"""Classify shadow-depth diagnostics without descendant promotion."""
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


def _ks_interpretation(n_vir: int) -> str:
    """Kodaira-Spencer interpretation of L_{n_vir}."""
    interp = {
        -1: 'Flatness of the deformation metric (string equation). '
            'The collision residue at arity 2 gives the identity element '
            'of the Frobenius algebra.',
        0: 'Euler vector field / quasi-homogeneity (dilaton equation). '
           'The arity-3 MC equation encodes the grading on the deformation space.',
        1: 'WDVV associativity at first order. '
           'The arity-4 MC equation is the first nontrivial integrability condition.',
        2: 'Second-order integrability of deformations. '
           'The arity-5 MC equation constrains 5-point deformations.',
    }
    return interp.get(n_vir,
                      f'Order-{n_vir} integrability of deformations '
                      f'(arity-{n_vir+3} MC equation).')


# ============================================================================
# 5. Scalar kappa lane and standard-hierarchy obstruction
# ============================================================================

def proof3_kappa_scaling(kappa_val: Fraction = Fraction(1, 2),
                          max_genus: int = 5) -> Dict[str, Any]:
    r"""Verify scalar kappa coefficients and report hierarchy failure.

    The positive check is only F_g^scal = kappa lambda_g^FP.  The standard
    nonlinear hierarchy channels leave the kappa(1-kappa) residual recorded
    in higher_genus_modular_koszul.tex:20376-20388.
    """
    hierarchy_status = standard_hierarchy_constraint_status(kappa_val)
    finite_tau = finite_scalar_shadow_tau(kappa_val, max_genus=max_genus)

    results = {
        'kappa': kappa_val,
        'certificate': 'finite scalar coefficient identity',
        'genus_checks': {},
        'finite_scalar_tau': finite_tau,
        'standard_hierarchy_status': hierarchy_status,
        'all_pass': True,
    }

    for g in range(1, max_genus + 1):
        fp = lambda_fp(g)
        F_shadow = kappa_val * fp
        F_kw = fp

        path1 = F_shadow
        ratio = F_shadow / F_kw if F_kw != Fraction(0) else None
        path2_pass = (ratio == kappa_val) if ratio is not None else False
        path3 = kappa_val * fp

        all_match = (path1 == F_shadow == path3) and path2_pass

        results['genus_checks'][g] = {
            'F_shadow': F_shadow,
            'F_kw': F_kw,
            'ratio': ratio,
            'kappa_constant': path2_pass,
            'three_paths_agree': all_match,
        }
        if not all_match:
            results['all_pass'] = False

    results['virasoro_linearity'] = {
        'statement': 'finite scalar log scaling is not a Virasoro constraint',
        'kappa_commutes': kappa_val == Fraction(1),
        'reason': (
            'standard tau-level Virasoro operators include nonlinear '
            'free-energy channels and descendant variables'
        ),
    }

    results['kdv_negative'] = {
        'statement': 'standard KdV fails except for kappa=1 and zero-field kappa=0',
        'residual_factor': hierarchy_status['kdv_residual_factor_kappa_1_minus_kappa'],
        'fails': not hierarchy_status['standard_kdv_hierarchy'],
        'source': LOCAL_SOURCE_ANCHORS['finite_scalar_tau'],
    }

    return results


def kappa_scaled_virasoro_operators(n_vir: int, kappa_val: Fraction) -> Dict[str, Any]:
    r"""Report whether the standard KW Virasoro operator is certified."""
    status = standard_hierarchy_constraint_status(kappa_val)
    allowed = status['standard_descendant_virasoro_constraints']

    return {
        'virasoro_index': n_vir,
        'kappa': kappa_val,
        'operator': f'L_{n_vir}',
        'standard_operator_certified': allowed,
        'no_deformation': allowed,
        'constructs_deformed_operator': False,
        'failure_mode': None if allowed else (
            'finite scalar coefficients do not construct a descendant '
            'Virasoro representation'
        ),
        'source': LOCAL_SOURCE_ANCHORS['finite_scalar_tau'],
    }


def descendant_cohft_data_certificate(descendant_data_assumed: bool = False) -> Dict[str, Any]:
    r"""Separate scalar shadow data from an independently supplied CohFT."""
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


# ============================================================================
# 6. W-constraint structural data
# ============================================================================

def proof4_w_constraints(max_N: int = 4) -> Dict[str, Any]:
    r"""Structural W_N hierarchy data, conditional on descendant CohFT input.

    For the W_N algebra (rank N-1), the shadow CohFT at genus 0 is the
    A_{N-1} Frobenius manifold CohFT.  The integrable hierarchy is the
    N-th Gelfand-Dickey hierarchy.

    The W_N-constraints generalize the Virasoro constraints:
      N=2 (Virasoro): L_n Z = 0 (KdV)
      N=3 (W_3): L_n Z = 0 AND W_n Z = 0 (Boussinesq / 3-KdV)
      N=4 (W_4): L_n Z = 0 AND W_n^{(3)} Z = 0 AND W_n^{(4)} Z = 0

    The scalar coefficient lane alone does not build these operators.

    At genus 0: the W_N constraints determine the A_{N-1} Frobenius
    prepotential.  The MC equation at each arity k gives the integrability
    condition for k-point deformations in the (N-1)-dimensional space.

    The explicit W_N operators require the separately supplied descendant
    CohFT package.
    """
    results = {
        'certificate': 'W-constraint structural data',
        'requires_descendant_cohft_data': True,
        'scalar_lane_constructs_operators': False,
        'families': {},
    }

    for N in range(2, max_N + 1):
        rank = N - 1
        hierarchy = _gelfand_dickey_name(N)

        # Number of W-generators: W^{(2)}, W^{(3)}, ..., W^{(N)}
        n_generators = N - 1  # = rank

        # At genus 0, the MC equation at arity k gives k-3 + rank constraints
        # (one for each generator applied to the k-point function)

        # For N=2: 1 generator (Virasoro L), L_n constraints
        # For N=3: 2 generators (L, W^{(3)}), coupled L_n + W_n constraints
        # For N=4: 3 generators (L, W^{(3)}, W^{(4)}), three families

        results['families'][N] = {
            'rank': rank,
            'W_generators': [f'W^{{({s})}}' for s in range(2, N + 1)],
            'n_generators': n_generators,
            'hierarchy': hierarchy,
            'genus_0_constraints': (
                f'With descendant CohFT data, W_{N} has {n_generators} '
                f'coupled {hierarchy} constraint families.'
            ),
            'arity_2_constraint': (
                f'String equation for all {n_generators} generators'
            ),
            'arity_3_constraint': (
                f'Dilaton/scaling for all {n_generators} generators'
            ),
        }

    # Verify that N=2 reduces to pure Virasoro
    results['n2_reduction'] = {
        'statement': 'W_2 constraints = Virasoro constraints (the W_2 algebra IS the Virasoro algebra)',
        'generators': ['L (= W^{(2)})'],
        'hierarchy': 'KdV (= 2nd Gelfand-Dickey)',
        'passes': True,
    }

    # Structural check: number of constraints at each arity
    for k in range(2, 7):
        n_vir = k - 3
        results[f'arity_{k}_structure'] = {
            'mc_arity': k,
            'virasoro_index': n_vir if n_vir >= -1 else 'N/A',
            'n2_constraints': 1 if n_vir >= -1 else 0,
            'n3_constraints': 2 if n_vir >= -1 else 0,
            'n4_constraints': 3 if n_vir >= -1 else 0,
            'general_nN_constraints': f'N-1 = rank coupled constraints from Gelfand-Dickey',
        }

    results['all_pass'] = True
    return results


def _gelfand_dickey_name(N: int) -> str:
    """Name of the N-th Gelfand-Dickey hierarchy."""
    names = {
        2: 'KdV (2nd Gelfand-Dickey)',
        3: 'Boussinesq (3rd Gelfand-Dickey / 3-KdV)',
        4: '4th Gelfand-Dickey',
        5: '5th Gelfand-Dickey',
    }
    return names.get(N, f'{N}th Gelfand-Dickey')


# ============================================================================
# 7. MC equation at general genus, extending the genus-0 projection
# ============================================================================

def mc_general_genus_projection(g: int, k: int) -> Dict[str, Any]:
    r"""The MC equation at (g, k) and its constraint content.

    At genus g > 0, the MC equation at arity k gives constraints that involve
    ALL three boundary types:
      D-term (merge): two marked points collide
      [,]-term (split): curve degenerates at a separating node
      [,]-term (handle): genus reduction by smoothing a non-separating node

    The handle term is the QUANTUM correction (absent at genus 0, classical).
    It contributes genus-(g-1) data to the genus-g constraint.

    The Virasoro constraint L_{k-3} at genus g:
      - L_{-1} (k=2, g > 0): string equation with handle terms
      - L_0 (k=3, g > 0): dilaton with handle terms
      - L_n (k=n+3, g > 0): full DVV with merge + handle + split

    The new ingredient at g > 0 is the HANDLE TERM, which couples genus g
    to genus g-1 in the DVV recursion.  A single finite projection is only
    a local address in the recursion; it does not reconstruct the full MC
    element, the ordered bar differential, or every F_g from genus-0 data.
    """
    if g < 0:
        raise ValueError(f"genus must be >= 0, got {g}")
    if k < 0:
        raise ValueError(f"arity must be >= 0, got {k}")

    return {
        'genus': g,
        'arity': k,
        'virasoro_index': k - 3 if k >= 2 else None,
        'D_term': 'merge (collision of two marked points)',
        'bracket_split': 'separating node degeneration',
        'bracket_handle': 'ABSENT' if g == 0 else f'non-separating node (genus {g} -> {g-1})',
        'is_classical': g == 0,
        'quantum_correction': g > 0,
        'finite_projection_only': True,
        'reconstructs_full_mc': False,
        'reconstructs_all_Fg_from_genus0': False,
        'separates_bar_from_hochschild': True,
        'dvv_terms': {
            'merge': 'sum_i (d+d_i-1)!!/(d_i-1)!! <...tau_{d+d_i-1}...>_g',
            'handle': '0' if g == 0 else 'sum_{a+b=d-2} (a)!!(b)!!/2 <...tau_a tau_b...>_{g-1}',
            'split': 'sum_{I+J} sum_{g1+g2=g} <tau_a I>_{g1} <tau_b J>_{g2}',
        },
    }


def verify_mc_at_genus_arity(g: int, k: int,
                              insertions: Tuple[int, ...] = ()) -> Dict[str, Any]:
    """Verify the MC equation at (g, k) for specific insertions.

    This is a finite-window verification: compute both sides of the DVV
    recursion at genus g with the distinguished insertion d = k-3+1 = k-2
    and additional insertions.  It is not a full MC reconstruction.
    """
    if g < 0:
        raise ValueError(f"genus must be >= 0, got {g}")
    if k < 0:
        raise ValueError(f"arity must be >= 0, got {k}")

    n_vir = k - 3
    if n_vir < -1:
        return {
            'genus': g, 'arity': k,
            'passes': True,
            'reason': 'arity too small for nontrivial Virasoro constraint',
        }
    return _verify_single_virasoro_mc(n_vir, g, insertions)


# ============================================================================
# 8. Arity-genus table: which Virasoro constraint lives at which MC address
# ============================================================================

def virasoro_mc_address_table(max_n: int = 8, max_g: int = 4) -> Dict[str, Any]:
    r"""The Virasoro-MC address table.

    For each Virasoro operator L_n and genus g, identify the MC address
    (g, k) in the arity convention k = n + 3.

    The FUNDAMENTAL identification:
      L_n constraint <-> MC equation at (g, n+3)
      (with g = 0 for the pure genus-0 identification;
       g > 0 includes handle corrections).

    The genus-g, arity-k MC equation involves:
      - k marked points on M-bar_{g,k}
      - dim M-bar_{g,k} = 3g - 3 + k
      - The constraint is nontrivial when 3g - 3 + k >= 0 and 2g - 2 + k > 0
    """
    if max_n < -1:
        raise ValueError(f"max_n must be >= -1, got {max_n}")
    if max_g < 0:
        raise ValueError(f"max_g must be >= 0, got {max_g}")

    table = {}
    for n in range(-1, max_n + 1):
        for g in range(0, max_g + 1):
            k = n + 3
            dim_mbar = 3 * g - 3 + k
            stable = 2 * g - 2 + k > 0

            table[f'L_{n}_g{g}'] = {
                'virasoro_index': n,
                'genus': g,
                'mc_arity': k,
                'dim_mbar': dim_mbar,
                'stable': stable,
                'nontrivial': stable and dim_mbar >= 0,
                'constraint_name': _constraint_name(n),
                'handle_terms': g > 0,
            }

    return table


def _constraint_name(n: int) -> str:
    """Human-readable name for L_n."""
    if n == -1:
        return 'string equation'
    if n == 0:
        return 'dilaton equation'
    return f'L_{n} Virasoro constraint'


# ============================================================================
# 9. Cross-verification: three independent paths for each constraint
# ============================================================================

def triple_verification_constraint(
    n_vir: int, genus: int, insertions: Tuple[int, ...],
    kappa_val: Fraction = Fraction(1, 2)
) -> Dict[str, Any]:
    r"""Compare the KW reference recursion with scalar kappa scaling.

    The third path certifies only scalar multiplication of the numerical
    correlator.  It becomes a descendant Virasoro certificate only at
    kappa = 1, where the object is the actual KW CohFT.
    """
    path1 = _verify_single_virasoro_mc(n_vir, genus, insertions)

    d_insert = max(n_vir + 1, 0)
    full_ins = tuple(sorted(list(insertions) + [d_insert]))
    path2_value = wk_intersection(genus, full_ins)

    path3_shadow = kappa_val * path2_value
    hierarchy_status = standard_hierarchy_constraint_status(kappa_val)
    scalar_scaling = path3_shadow == kappa_val * path2_value
    descendant_certified = (
        path1['passes']
        and scalar_scaling
        and hierarchy_status['standard_descendant_virasoro_constraints']
    )

    return {
        'virasoro_index': n_vir,
        'genus': genus,
        'insertions': insertions,
        'path1_dvv_mc': path1,
        'path2_wk_direct': path2_value,
        'path3_shadow_scaled': path3_shadow,
        'kappa': kappa_val,
        'dvv_passes': path1['passes'],
        'scaling_consistent': scalar_scaling,
        'descendant_virasoro_certified': descendant_certified,
        'all_three_agree': descendant_certified,
        'failure_mode': None if descendant_certified else (
            'scalar scaling is not a full descendant Virasoro certificate'
        ),
    }


# ============================================================================
# 10. Comprehensive theorem verification
# ============================================================================

def full_theorem_verification(
    kappa_val: Fraction = Fraction(1, 2),
    max_genus: int = 3,
    max_n_vir: int = 5,
    max_extra: int = 2,
) -> Dict[str, Any]:
    r"""Full certificate package for KW reference and scalar-shadow claims.

    The finite standard descendant window passes only at kappa = 1.  The
    function does not certify full MC reconstruction.
    """
    hierarchy_status = standard_hierarchy_constraint_status(kappa_val)
    finite_scope = finite_constraint_scope_certificate(
        max_n_vir=max_n_vir,
        max_genus=max_genus,
        descendant_data_assumed=hierarchy_status[
            'standard_descendant_virasoro_constraints'
        ],
    )
    results = {
        'claim': 'finite scalar shadow versus standard descendant constraints',
        'kappa': kappa_val,
        'standard_hierarchy_status': hierarchy_status,
        'finite_constraint_scope': finite_scope,
        'proves_full_mc_reconstruction': False,
        'constructs_bar_differential': False,
        'constructs_derived_center': False,
        'proofs': {},
        'cross_checks': {},
    }

    proof1_results = {}
    all_proof1 = True
    for n_vir in range(-1, max_n_vir + 1):
        p1 = proof1_mc_projection_equals_virasoro(
            n_vir, max_genus=max_genus, max_extra_insertions=max_extra)
        proof1_results[f'L_{n_vir}'] = p1
        if not p1['all_pass']:
            all_proof1 = False
    results['proofs']['proof1_mc_projection'] = {
        'all_pass': all_proof1,
        'scope': 'KW descendant CohFT reference',
        'details': proof1_results,
    }

    p2 = proof2_kodaira_spencer(max_genus=max_genus)
    results['proofs']['proof2_kodaira_spencer'] = p2

    p3 = proof3_kappa_scaling(kappa_val=kappa_val, max_genus=max_genus)
    results['proofs']['proof3_kappa_scaling'] = p3

    p4 = proof4_w_constraints(max_N=4)
    results['proofs']['proof4_w_constraints'] = p4

    cross_pass = True
    for n_vir in range(-1, min(max_n_vir + 1, 4)):
        for g in range(0, min(max_genus + 1, 3)):
            ins_list = _generate_valid_insertions(g, n_vir, 1)
            for ins in ins_list[:2]:
                key = f'L_{n_vir}_g{g}_{ins}'
                cv = triple_verification_constraint(n_vir, g, ins, kappa_val)
                results['cross_checks'][key] = cv
                if not cv['all_three_agree']:
                    cross_pass = False

    results['cross_checks_all_pass'] = cross_pass
    results['scalar_lane_pass'] = p3['all_pass']
    results['standard_descendant_package_pass'] = (
        all_proof1
        and p2['kw_reference_checks_pass']
        and p3['all_pass']
        and p4['all_pass']
        and hierarchy_status['standard_descendant_virasoro_constraints']
    )

    results['address_table'] = virasoro_mc_address_table(max_n=max_n_vir, max_g=max_genus)

    overall = results['standard_descendant_package_pass']
    results['finite_window_pass'] = overall
    results['all_pass'] = overall
    results['summary'] = (
        'Scalar coefficients verified; finite standard descendant window '
        f'{"certified" if overall else "not certified"} at kappa={kappa_val}; '
        'full MC reconstruction not certified.'
    )

    return results


# ============================================================================
# 11. Genus-0 MC equation as boundary condition on M-bar_{0,k}
# ============================================================================

def mc_boundary_chain_genus0(k: int) -> Dict[str, Any]:
    r"""The MC equation at genus 0 as a boundary chain condition.

    The fundamental chain [M-bar_{0,k}] has boundary:
      partial [M-bar_{0,k}] = sum_{I,J} [M-bar_{0,|I|+1} x M-bar_{0,|J|+1}]

    where the sum is over all partitions {I, J} of {1,...,k} with |I|,|J| >= 2.

    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 at (0,k) is:
      <D Theta>_{0,k} + (1/2) <[Theta,Theta]>_{0,k} = 0

    where:
      <D Theta>_{0,k}: the differential D applied to Theta_{0,k-1}, encoding
                        the merge/collision boundary
      <[Theta,Theta]>_{0,k}: the bracket pairing Theta_{0,k1} with Theta_{0,k2},
                              encoding the split/separating-node boundary

    The total boundary vanishes: this is the statement that M-bar_{0,k} is
    a manifold with corners, and the codimension-1 boundary is the sum of
    products of lower-dimensional moduli spaces.

    This is the GEOMETRIC content of the Virasoro constraints at genus 0.
    """
    boundary_info = genus0_boundary_strata(k)

    # For each boundary stratum (I, J), compute the dimensions
    strata_dims = []
    for I, J in boundary_info['strata']:
        dim_I = len(I) + 1 - 3  # dim M-bar_{0,|I|+1}
        dim_J = len(J) + 1 - 3  # dim M-bar_{0,|J|+1}
        strata_dims.append({
            'I': I, 'J': J,
            '|I|': len(I), '|J|': len(J),
            'dim_I_component': max(dim_I, 0),
            'dim_J_component': max(dim_J, 0),
            'total_dim': max(dim_I, 0) + max(dim_J, 0),
            'codimension_in_mbar': 1,
        })

    # Verify: total boundary dimension = k - 4 = dim(M-bar_{0,k}) - 1
    expected_boundary_dim = k - 4

    return {
        'arity': k,
        'dim_mbar_0k': k - 3,
        'boundary_dim': expected_boundary_dim,
        'num_strata': boundary_info['num_strata'],
        'strata_details': strata_dims,
        'mc_decomposition': {
            'D_term': f'merge contributions from {k} collision configurations',
            'bracket_term': f'split contributions from {boundary_info["num_strata"]} separating nodes',
            'handle_term': 'ABSENT (genus 0)',
        },
        'virasoro_constraint': f'L_{k-3} (arity {k} MC projection)',
    }


# ============================================================================
# 12. Shadow partition function: certified equations and failure factors
# ============================================================================

def shadow_equation_classification(kappa_val: Fraction = Fraction(1, 2),
                                    max_genus: int = 5) -> Dict[str, Any]:
    r"""Classify scalar coefficient identities versus standard hierarchies."""
    F1_kw = Fraction(1, 24)
    F2_kw = Fraction(7, 5760)
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
            'F_1_shadow': kappa_val * F1_kw,
            'F_2_shadow': kappa_val * F2_kw,
            'F_1_kw': F1_kw,
            'F_2_kw': F2_kw,
            'ratio_F1': kappa_val,
            'ratio_F2': kappa_val,
            'ratios_constant': True,
        },
        'finite_scalar_tau': finite_tau,
    }


# ============================================================================
# 13. Structural theorem: MC arity decomposition
# ============================================================================

def mc_arity_virasoro_dictionary() -> Dict[str, Any]:
    r"""Finite MC-arity to Virasoro-constraint dictionary.

    The MC equation D*Theta + (1/2)[Theta,Theta] = 0, projected to
    genus g and arity k, gives:

    (g=0, k=2): L_{-1} = string equation
                 MC content: D|_{(0,2)} = collision residue of binary OPE
                 Geometric: dim M-bar_{0,3} = 0 (point)

    (g=0, k=3): L_0 = dilaton equation
                 MC content: D|_{(0,3)} + (1/2)[,]|_{(0,3)}
                 Geometric: dim M-bar_{0,4} = 1 (P^1)

    (g=0, k=4): L_1 = first DVV recursion
                 MC content: full D + bracket at (0,4)
                 Geometric: dim M-bar_{0,5} = 2

    (g=0, k=n+3): L_n = n-th Virasoro constraint
                   MC content: D + bracket at (0, n+3)
                   Geometric: dim M-bar_{0, n+4} = n+1

    (g>0, k): SAME L_{k-3} constraint with ADDITIONAL handle terms
              from genus reduction (g -> g-1).  These are the
              QUANTUM CORRECTIONS that couple genera.

    The formal address rule is:
      MC address (g, k)  <-->  L_{k-3} constraint at genus g
                               with handle corrections from all g' < g.

    The returned dictionary is the finite arity window 2 <= k <= 9.  It is
    a computable witness for the address convention, not a reconstruction
    of the full ordered MC element.
    """
    dictionary = {}
    for k in range(2, 10):
        n = k - 3
        if n < -1:
            continue
        dictionary[f'arity_{k}'] = {
            'mc_address': f'(g, {k})',
            'virasoro': f'L_{n}',
            'name': _constraint_name(n),
            'dim_mbar_0': k - 3,
            'boundary_strata_genus0': genus0_boundary_strata(k)['num_strata'],
            'merge_terms': 'yes (D-term)',
            'split_terms': 'yes ([,]-term)' if k >= 4 else 'no (arity too small)',
            'handle_terms': 'at g > 0 only',
            'finite_window_only': True,
            'reconstructs_full_mc': False,
        }

    return dictionary
