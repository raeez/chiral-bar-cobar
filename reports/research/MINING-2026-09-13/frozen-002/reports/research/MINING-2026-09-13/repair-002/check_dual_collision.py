"""Exact finite transposition checks after the coefficient extension.

State degrees are zero; the suspended bar and dual retain their signs.
The manuscript proves the finite-perfect-module scalar comparison.
"""

from collections import defaultdict
from itertools import product
import json
import platform


def basis(labels, weight):
    if weight == 0:
        return [()]
    result = []
    for letters in product(range(labels), repeat=weight):
        for cuts in product((0, 1), repeat=weight - 1):
            word, state = [], [letters[0]]
            for letter, cut in zip(letters[1:], cuts):
                if cut:
                    word.append(tuple(state))
                    state = []
                state.append(letter)
            result.append(tuple(word + [tuple(state)]))
    return result


def image(word, merger):
    return tuple(tuple(merger[x] for x in state) for state in word)


def clean(terms):
    return {word: coefficient for word, coefficient in terms.items() if coefficient}


def transpose(functional, source_labels, merger, weight):
    return {word: functional[image(word, merger)]
            for word in basis(source_labels, weight)
            if image(word, merger) in functional}


def differential(functional, labels, weight):
    result = defaultdict(int)
    for word in basis(labels, weight):
        for i in range(len(word) - 1):
            face = word[:i] + (word[i] + word[i + 1],) + word[i + 2:]
            if face in functional:
                # -(-1)^|F| F b, where |F| is the number of dual bar letters.
                result[word] += -(-1) ** len(face) * (-1) ** i * functional[face]
    return clean(result)


def convolution(left, right):
    result = defaultdict(int)
    for a, ca in left.items():
        for b, cb in right.items():
            result[a + b] += ca * cb * (-1) ** (len(a) * len(b))
    return clean(result)


merger = (0, 0, 1)
outer = (0, 0)
composite = tuple(outer[j] for j in merger)
counts = defaultdict(int)
for weight in range(5):
    for word in basis(2, weight):
        functional = {word: 1}
        assert transpose(differential(functional, 2, weight), 3, merger, weight) == differential(transpose(functional, 3, merger, weight), 3, weight)
        counts['dual_differential_basis_checks_through_weight_four'] += 1
    for word in basis(1, weight):
        functional = {word: 1}
        direct = transpose(functional, 3, composite, weight)
        nested = transpose(transpose(functional, 2, outer, weight), 3, merger, weight)
        assert direct == nested
        counts['nested_dual_transpose_checks_through_weight_four'] += 1
    for a in range(weight + 1):
        b = weight - a
        for left in basis(2, a):
            for right in basis(2, b):
                lhs = transpose(convolution({left: 1}, {right: 1}), 3, merger, weight)
                rhs = convolution(transpose({left: 1}, 3, merger, a), transpose({right: 1}, 3, merger, b))
                assert lhs == rhs
                counts['convolution_basis_pairs_through_weight_four'] += 1

# Coefficient B=k^2 acts on C=k by first projection. Every linear map
# C→B is determined by v=f(1). B-linearity requires e2*v=0.
for first, second in product(range(-2, 3), repeat=2):
    b_linear = second == 0
    unital = (first, second) == (1, 1)
    assert not (b_linear and unital)
    counts['binary_idempotent_samples'] += 1

# After scalar extension, E(B)=C. The weight-zero transpose preserves 1.
assert transpose({(): 1}, 3, merger, 0) == {(): 1}
counts['scalar_extended_unit'] = 1

print(json.dumps({'status': 'all exact targeted checks passed',
                  'python': platform.python_version(), 'counts': dict(counts),
                  'scope': 'Finite transpose, differential, convolution, composition and coefficient-unit checks; the all-weight and derived scalar proofs are in the manuscript.'}, indent=2))
