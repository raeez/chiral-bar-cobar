"""Exact finite checks of ordered diagonal maps and the relative bar.

These checks test the displayed formulas. The manuscript gives the
general geometric, differential-module, and homological arguments.
"""

from collections import defaultdict
from itertools import combinations, permutations, product
from math import factorial
import json
import platform
import sympy as sp


def surjections(n, m):
    return (p for p in product(range(m), repeat=n) if len(set(p)) == m)


def fibre_orders(p, m):
    return product(*(permutations(i for i, j in enumerate(p) if j == a)
                     for a in range(m)))


def expand(order, fibres):
    return tuple(i for a in order for i in fibres[a])


def disagreements(a, b):
    pa = {x: i for i, x in enumerate(a)}
    pb = {x: i for i, x in enumerate(b)}
    return {frozenset((x, y)) for x, y in combinations(a, 2)
            if (pa[x] < pa[y]) != (pb[x] < pb[y])}


def add_term(out, word, coefficient):
    out[word] += coefficient
    if not out[word]:
        del out[word]


def bar_boundary(words, parity):
    out = defaultdict(int)
    for word, coefficient in words.items():
        prefix = 0
        for i in range(len(word) - 1):
            degree = sum(parity[a] for a in word[i]) % 2
            new = word[:i] + (word[i] + word[i + 1],) + word[i + 2:]
            add_term(out, new, coefficient * (-1) ** ((prefix + degree) % 2))
            prefix += degree - 1
    return dict(out)


def relabel(words, p):
    out = defaultdict(int)
    for word, coefficient in words.items():
        new = tuple(tuple(p[a] for a in state) for state in word)
        add_term(out, new, coefficient)
    return dict(out)


def cobar_boundary(terms, parity):
    out = defaultdict(int)
    for cobar, coefficient in terms.items():
        prefix_degree = 0
        for i, block in enumerate(cobar):
            for new_block, sign in bar_boundary({block: 1}, parity).items():
                new = cobar[:i] + (new_block,) + cobar[i + 1:]
                add_term(out, new, coefficient * (-1) ** (prefix_degree % 2) * -sign)
            for j in range(1, len(block)):
                left, right = block[:j], block[j:]
                left_degree = sum(parity[a] for state in left for a in state) - len(left)
                new = cobar[:i] + (left, right) + cobar[i + 1:]
                add_term(out, new, coefficient * (-1) ** ((prefix_degree + left_degree + 1) % 2))
            prefix_degree += sum(parity[a] for state in block for a in state) - len(block) + 1
    return dict(out)


def counit(terms):
    out = defaultdict(int)
    for cobar, coefficient in terms.items():
        if all(len(block) == 1 for block in cobar):
            word = tuple(a for block in cobar for a in block[0])
            add_term(out, word, coefficient)
    return dict(out)


counts = defaultdict(int)
for n in range(1, 5):
    for m in range(1, n + 1):
        orders = list(permutations(range(m)))
        for p in surjections(n, m):
            for fibres in fibre_orders(p, m):
                for a, b in product(orders, repeat=2):
                    source = disagreements(expand(a, fibres), expand(b, fibres))
                    target = disagreements(a, b)
                    expected = {frozenset((i, j)) for i, j in combinations(range(n), 2)
                                if p[i] != p[j] and frozenset((p[i], p[j])) in target}
                    assert source == expected
                    counts['overlap_pairs_through_four_labels'] += 1
                for k in range(1, m + 1):
                    for q in surjections(m, k):
                        for outer in fibre_orders(q, k):
                            composite_fibres = tuple(expand(part, fibres) for part in outer)
                            for order in permutations(range(k)):
                                assert expand(expand(order, outer), fibres) == expand(order, composite_fibres)
                                counts['nested_order_compositions_through_four_labels'] += 1

# Independent fibre calculation: equivalent orders have the same order
# on each collision block, irrespective of their interleaving elsewhere.
for n in range(1, 6):
    for m in range(1, n + 1):
        for p in surjections(n, m):
            restrictions = {tuple(tuple(i for i in order if p[i] == j)
                                  for j in range(m))
                            for order in permutations(range(n))}
            expected = 1
            for j in range(m):
                expected *= factorial(p.count(j))
            assert len(restrictions) == expected
            counts['derived_fibre_branch_partitions_through_five_labels'] += 1

# Every homogeneous parity assignment through length seven, retaining
# free noncommutative state words so associativity is not made vacuous.
for length in range(1, 8):
    for parity in product((0, 1), repeat=length):
        initial = {tuple((i,) for i in range(length)): 1}
        first = bar_boundary(initial, parity)
        assert bar_boundary(first, parity) == {}
        counts['bar_square_parities_through_length_seven'] += 1

# All degree-zero three-label words through length seven, including
# repeated labels. This checks the actual noninjective merged-state map.
p = (0, 0, 1)
for length in range(1, 8):
    for letters in product(range(3), repeat=length):
        initial = {tuple((i,) for i in letters): 1}
        assert relabel(bar_boundary(initial, (0, 0, 0)), p) == bar_boundary(relabel(initial, p), (0, 0))
        counts['merged_state_bar_words_through_length_seven'] += 1

# Nonzero rational coefficients, with a real derivative obstruction.
z1, z2, z3, za, zb, t = sp.symbols('z1 z2 z3 za zb t')
source = 1 / (z1 - z3)
restriction = source.subs({z1: za, z2: za, z3: zb}, simultaneous=True)
assert sp.simplify(restriction - 1 / (za - zb)) == 0
assert sp.simplify(sp.diff(restriction, za) -
                   (sp.diff(source, z1) + sp.diff(source, z2)).subs({z1: za, z2: za, z3: zb}, simultaneous=True)) == 0
assert sp.diff(1 / (z1 - z2), z1) == -1 / (z1 - z2) ** 2
counts['symbolic_coefficient_and_connection_identities'] = 3

# The three gap states are: inside one state, inside one bar block,
# and between cobar factors. These enumerate every word at this weight.
for length in range(1, 6):
    for gap_types in product(range(3), repeat=length - 1):
        factors, states, state = [], [], [0]
        for a, gap in enumerate(gap_types, 1):
            if gap == 0:
                state.append(a)
            else:
                states.append(tuple(state))
                state = [a]
                if gap == 2:
                    factors.append(tuple(states))
                    states = []
        states.append(tuple(state))
        factors.append(tuple(states))
        initial = {tuple(factors): 1}
        for parity in product((0, 1), repeat=length):
            first = cobar_boundary(initial, parity)
            assert cobar_boundary(first, parity) == {}
            assert counit(first) == {}
            counts['cobar_square_and_counit_parities_through_weight_five'] += 1

print(json.dumps({
    'status': 'all exact finite checks passed',
    'python': platform.python_version(), 'sympy': sp.__version__,
    'counts': dict(counts),
    'scope': 'Finite formula checks; no claim of Ran descent or independent acceptance.'
}, indent=2))
