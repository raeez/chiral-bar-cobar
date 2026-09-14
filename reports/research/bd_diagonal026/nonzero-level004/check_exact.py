#!/usr/bin/env python3
"""Check the finite identities that decide the native translation construction."""
from pathlib import Path
from itertools import combinations, permutations
import hashlib
import json
import math
import platform
import sympy as sp

REPORT = Path(__file__).resolve().parent
ROOT = REPORT.parents[3]
t, s, x, u, k = sp.symbols('t s x u k')
J = sp.symbols('J0:12')


def pp(expression, variable):
    expression = sp.expand(expression)
    return sp.Add(*(term for term in sp.Add.make_args(expression)
                    if term.as_powers_dict().get(variable, 0) < 0))


p = k / t**2 + sum(J[r] * J[0] * t**r / math.factorial(r) for r in range(12))
endpoint_count = 0
for degree in range(7):
    for power in range(-6, 4):
        f = u**degree * t**power
        if power < 0:
            f *= u * (1-u)
        derivative = sp.diff(f, u)
        weighted = sp.integrate(u * derivative, (u, 0, 1))
        average = sp.integrate(f, (u, 0, 1))
        assert sp.simplify(weighted + average - f.subs(u, 1)) == 0
        assert sp.expand(pp(p * weighted, t) + pp(p * average, t)
                         - pp(p * f.subs(u, 1), t)) == 0
        q_derivative = pp(t * p * sp.integrate(derivative, (u, 0, 1)), t)
        assert sp.expand(q_derivative - pp(k * (f.subs(u, 1)-f.subs(u, 0))/t, t)) == 0
        endpoint_count += 1

# The input translation product is checked with independent formal output jets.
def product(r, n):
    result = {}
    for a in range(r+1):
        for b in range(n+1):
            coefficient = (sp.binomial(r, a) * sp.binomial(n, b)
                           * (-1)**a * math.factorial(a+b) / t**(a+b+1))
            key = (r-a, n-b)
            result[key] = result.get(key, 0) + coefficient
    return result


def derivative_product(terms, slot):
    result = {}
    for indices, coefficient in terms.items():
        result[indices] = result.get(indices, 0) + (-1)**slot * sp.diff(coefficient, t)
        shifted = tuple(value + (i == slot) for i, value in enumerate(indices))
        result[shifted] = result.get(shifted, 0) + coefficient
    return result


jet_count = 0
for r in range(6):
    for n in range(6):
        for slot in range(2):
            actual = derivative_product(product(r, n), slot)
            expected = product(r+(slot == 0), n+(slot == 1))
            for key in set(actual) | set(expected):
                assert sp.simplify(actual.get(key, 0)-expected.get(key, 0)) == 0
            jet_count += 1

# A direct oscillator normal-order calculation gives the outer single contraction.
a = sp.symbols('a1:8')
creation = sum(a[r]*s**r for r in range(7))
annihilation_on_current = k/s**2
normal_square_on_current = creation**2*a[0] + 2*creation*annihilation_on_current
wick_outer = pp(normal_square_on_current, s)
assert sp.expand(wick_outer-2*k*(a[0]/s**2+a[1]/s)) == 0
q_omega = pp(t*p/t, t)
q_eta = pp(t*p/t**2, t)
assert q_omega == k/t**2
assert sp.expand(q_eta-(k/t**3+J[0]**2/t)) == 0
small_defect = -2*k*(J[0]/(t*s**2)+J[1]/(t*s))
assert pp(sp.expand(s*small_defect), s) == -2*k*J[0]/(t*s)

# The actual six connecting coefficients span the whole quadratic ideal.
positions = {1:t, 2:s, 3:sp.Integer(0)}
rows = []
coefficients = {}
for sigma in permutations((1, 2, 3)):
    i, j, l = sigma
    polynomial = sp.expand((positions[i]-positions[j])*(positions[j]-positions[l]))
    coefficients[''.join(map(str, sigma))] = str(polynomial)
    pol = sp.Poly(polynomial, t, s)
    rows.append([pol.coeff_monomial(t*t), pol.coeff_monomial(t*s), pol.coeff_monomial(s*s)])
assert sp.Matrix(rows).rank() == 3

# The isolating multiplier kills the other two pair components before Weyl descent.
multiplier = t**2 * s**2 * (t-s)
component12 = pp((k/x**2)*multiplier.subs(t, x+s), x)
component13 = pp((-k/t**2)*multiplier, t)
component23 = pp((k/s**2)*multiplier, s)
assert sp.expand(component12-k*s**4/x) == 0
assert component13 == 0 and component23 == 0
commutator_factors = [-r for r in range(4, 0, -1)]
assert math.prod(commutator_factors) == 24

# Right differentiation on Laurent representatives retains the exact two normal jets.
assert pp(t*k/t**2, t) == k/t
assert pp(t*t*k/t**2, t) == 0
assert -sp.diff(k/t, t) == k/t**2

# Independent permutation signs for the first and second four-current collisions.
four_terms = {}
totals = {}
for first in combinations(range(1, 5), 2):
    other = tuple(i for i in range(1, 5) if i not in first)
    blocks = tuple(sorted((first, other)))
    first_sign = (-1)**(sum(first)-3)
    # The second collision puts the complementary block before the first block.
    second_sign = 1 if other < first else -1
    totals[blocks] = totals.get(blocks, 0) + first_sign*second_sign
    four_terms[str(first)] = {'first_sign': first_sign, 'second_sign': second_sign,
                              'double_pair': str(blocks)}
assert set(totals.values()) == {0}
assert pp(pp(k*k/(t*t*s*s), t), s) != 0

# Preserve the exact previously frozen candidate without invoking its writer scripts.
old_manifest = ROOT/'reports/research/bd_diagonal026/nonzero-level002/manifest.json'
assert hashlib.sha256(old_manifest.read_bytes()).hexdigest() == '47e010ac2529a1121cd670950a470f276ce350d8e92e574e2bba3ebd458e202a'
old = json.loads(old_manifest.read_text())
preservation = []
for entry in old['files']:
    path = ROOT/entry['path']
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    assert actual == entry['sha256'], entry['path']
    preservation.append({'path': entry['path'], 'sha256': actual})

record = {
    'result': 'passed', 'python': platform.python_version(), 'sympy': sp.__version__,
    'endpoint_families': endpoint_count, 'jet_translation_equalities': jet_count,
    'coefficient_bounds': 'Endpoint polynomials through u-degree 8 and inner pole order 6; input jets through 5 in each slot.',
    'small_diagonal_witness': 'dq12/t12^2, with q=k/t^3+J^2/t and outer defect -2k(J/(t*s^2)+TJ/(t*s)).',
    'lower_pole_output': str(q_omega), 'quadratic_coefficients': coefficients,
    'connecting_matrix_rank': 3, 'isolated_pair_output': str(component12),
    'weyl_descent_factors': commutator_factors, 'four_current_signs': four_terms,
    'four_current_cancellation': {str(key): value for key, value in totals.items()},
    'preserved_old_frozen_files': len(preservation),
    'limits': 'Exact finite computations. General all-jet, cohomology, minimality, and differential-module claims require the written proofs. No proof assistant was used.'}
(REPORT/'exact-checks.json').write_text(json.dumps(record, indent=2)+'\n')
(REPORT/'preservation-check.json').write_text(json.dumps({'result':'passed','files':preservation}, indent=2)+'\n')
print(json.dumps(record, indent=2))
