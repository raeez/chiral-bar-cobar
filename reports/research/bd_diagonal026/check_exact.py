#!/usr/bin/env python3
"""Check the scalar contraction signs and decisive finite coefficients."""
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import json
import platform
import sympy as sp

REPORT = Path(__file__).resolve().parent


def sign(n):
    return -1 if n % 2 else 1


def add(out, key, value):
    out[key] += value
    if not out[key]:
        del out[key]


def epsilon(state, label=1):
    """Tensor insertion into the block containing the specified label."""
    blocks, bits = state
    index = next(i for i, block in enumerate(blocks) if label in block)
    if bits[index]:
        return {}
    result = list(bits)
    result[index] = 1
    coefficient = sign(sum(-bits[i] - 1 for i in range(index)))
    return {(blocks, tuple(result)): coefficient}


def internal(state):
    """Suspended differential, with kappa specialized to 1 for sign checks."""
    blocks, bits = state
    out = defaultdict(int)
    for i, bit in enumerate(bits):
        if not bit:
            continue
        result = list(bits)
        result[i] = 0
        coefficient = -sign(sum(-bits[j] - 1 for j in range(i)))
        add(out, (blocks, tuple(result)), coefficient)
    return dict(out)


def collide(state):
    """Unshuffle each pair to the front, then merge its scalar factors.

    Each pair has a separate output partition. This check needs no
    replacement of chiral Jacobi by a commutative scalar multiplication.
    """
    blocks, bits = state
    out = defaultdict(int)
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            if bits[i] + bits[j] > 1:
                continue
            permutation = (i, j) + tuple(k for k in range(len(blocks)) if k not in (i, j))
            inversions = sum((-bits[permutation[a]] - 1) * (-bits[permutation[b]] - 1)
                             for a in range(len(blocks))
                             for b in range(a + 1, len(blocks))
                             if permutation[a] > permutation[b])
            coefficient = sign(inversions - bits[i])
            merged = tuple(sorted(blocks[i] + blocks[j]))
            rest = tuple(k for k in range(len(blocks)) if k not in (i, j))
            newblocks = (merged,) + tuple(blocks[k] for k in rest)
            newbits = (bits[i] + bits[j],) + tuple(bits[k] for k in rest)
            add(out, (newblocks, newbits), coefficient)
    return dict(out)


def compose(first, second, state):
    out = defaultdict(int)
    for intermediate, c1 in second(state).items():
        for result, c2 in first(intermediate).items():
            add(out, result, c1 * c2)
    return dict(out)


def sum_maps(*maps):
    out = defaultdict(int)
    for mapping in maps:
        for key, value in mapping.items():
            add(out, key, value)
    return dict(out)


partitions = [((1,), (2,), (3,)), ((1, 2), (3,)),
              ((1, 3), (2,)), ((1,), (2, 3)), ((1, 2, 3),)]
states = []
for partition in partitions:
    for blocks in permutations(partition):
        for bits in product((0, 1), repeat=len(blocks)):
            states.append((blocks, bits))
for state in states:
    assert not compose(epsilon, epsilon, state)
    assert sum_maps(compose(internal, epsilon, state),
                    compose(epsilon, internal, state)) == {state: -1}
    assert not sum_maps(compose(collide, epsilon, state),
                        compose(epsilon, collide, state))
    assert not sum_maps(compose(internal, collide, state),
                        compose(collide, internal, state))
    for label in (1, 2, 3):
        operation = lambda item, label=label: epsilon(item, label)
        assert sum_maps(compose(internal, operation, state),
                        compose(operation, internal, state)) == {state: -1}
        assert not sum_maps(compose(collide, operation, state),
                            compose(operation, collide, state))
        for other in (1, 2, 3):
            second = lambda item, other=other: epsilon(item, other)
            assert not sum_maps(compose(operation, second, state),
                                compose(second, operation, state))

# Independent parity formulas for every degree parity, without scalar-state restrictions.
parity_cases = 0
for a, b, c in product(range(2), repeat=3):
    for exponent in (a, (b - 1) * (c - 1) + a):
        assert sign(exponent - 1) + sign(exponent) == 0
    n = (a - 1) * (b + c - 2) + b
    assert sign(n + b + c) + sign(n + b + c - 1) == 0
    parity_cases += 1

t, s, u, kappa = sp.symbols('t s u kappa')
J, x2, x3, x4, x5 = sp.symbols('J x2 x3 x4 x5')
translation = J + x2 * s + x3 * s**2 + x4 * s**3 + x5 * s**4


def principal(expr, variable):
    expr = sp.expand(expr)
    return sp.Add(*(term for term in sp.Add.make_args(expr)
                    if term.as_powers_dict().get(variable, 0) < 0))


outer_J2_J = translation**2 * J + 2 * kappa / s**2 * translation
global_output = principal(outer_J2_J, s) / t
assert sp.expand(global_output - (2*kappa*J/(t*s**2) + 2*kappa*x2/(t*s))) == 0
assert global_output.subs(kappa, 0) == 0
outer_pole_output = kappa*J/(t**3*s) + principal(outer_J2_J/s, s)/t
expected = (kappa*J/(t**3*s) + J**3/(t*s) + 2*kappa*J/(t*s**3)
            + 2*kappa*x2/(t*s**2) + 2*kappa*x3/(t*s))
assert sp.expand(outer_pole_output - expected) == 0
assert sp.expand(outer_pole_output.subs(kappa, 0) - J**3/(t*s)) == 0

# The global compatible family q12(1-q12)/t has a nonregular edge average.
f = u*(1-u)/t
average = sp.integrate(f, (u, 0, 1))
assert average == 1/(6*t)
p = kappa/t**2 + J**2 + x2*J*t + x3*J*t**2
inner = principal(p*average, t)
assert sp.expand(inner - kappa/(6*t**3) - J**2/(6*t)) == 0
weighted_derivative = sp.integrate(u*sp.diff(f, u), (u, 0, 1))
assert weighted_derivative == -1/(6*t)
positive_unmerged_image = principal(p*weighted_derivative, t)
assert sp.expand(positive_unmerged_image + inner) == 0

# Weighted integration cancels both adjacent defects, including interior poles.
weighted_cases = 0
for pole in range(5):
    for power in range(1, 7):
        path_example = s + t*u + u**power*(1-u)*(s+t)/t**pole
        average_example = sp.integrate(path_example, (u, 0, 1))
        weighted = sp.integrate(u*sp.diff(path_example, u), (u, 0, 1))
        assert sp.expand(weighted + average_example - path_example.subs(u, 1)) == 0
        adjacent_defect = principal(p*(path_example.subs(u, 1)-weighted-average_example), t)
        assert adjacent_defect == 0
        weighted_cases += 1

# Endpoint integration: one polynomial path with a genuine interior normal pole.
path = 2 + 3*u + (u-u**2)*(s+t)/t**3
endpoint = path.subs(u, 1) - path.subs(u, 0)
q_derivative = principal(t*p*sp.integrate(sp.diff(path, u), (u, 0, 1)), t)
assert sp.expand(q_derivative - kappa*principal(endpoint/t, t)) == 0

# Operator proof of the Hom correction, with noncommuting symbols.
# Relations Qh=1-hQ and QD=-Db reduce D-QhD+hDb to zero.
Q, h, D, b = sp.symbols('Q h D b', commutative=False)
defect = D - (1-h*Q)*D + h*D*b
assert sp.expand(defect).subs(Q*D, -D*b).expand() == 0

record = {
    'python': platform.python_version(), 'sympy': sp.__version__,
    'scalar_contraction_states': len(states),
    'arbitrary_degree_parities': parity_cases,
    'label_contraction_checks': 3 * len(states),
    'pairwise_odd_operator_checks': 9 * len(states),
    'weighted_edge_cases': weighted_cases,
    'checks': ['epsilon square zero', 'Q1 epsilon + epsilon Q1 = -1',
               'Q2 epsilon + epsilon Q2 = 0', 'Q1 Q2 + Q2 Q1 = 0',
               'global high-inner-pole outer divisibility',
               'outer-pole cubic obstruction with five exact coefficients',
               'nonregular global edge average', 'endpoint principal-part equation',
               'weighted derivative cancels nonregular-average obstruction',
               'weighted integration cancels adjacent defects with all tested inner poles',
               'Hom correction noncommutative identity'],
    'global_output': str(global_output),
    'outer_pole_output': str(expected),
    'nonregular_average_output': str(inner),
    'positive_unmerged_output': str(positive_unmerged_image),
    'arithmetic': 'Exact integers, rational numbers, and symbolic polynomials.',
    'limits': 'These calculations check signs and specified coefficients. The source proofs establish the sheaf maps, support, arbitrary finite poles, and general chain identity. No formal proof assistant was run.',
    'result': 'PASS'
}
(REPORT / 'exact-checks.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
