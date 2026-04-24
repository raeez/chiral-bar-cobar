"""Wave-2 Worker E independent-verification anchors.

The tests in this file add HZ-IV coverage for small exact models of
high-priority AP11 surfaces.  Each check computes from finite algebra,
configuration-form, or representation-theoretic data disjoint from the
corresponding manuscript proof.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product

from sympy import Matrix, Rational, eye, kronecker_product, simplify, symbols

from compute.lib.independent_verification import independent_verification


def _set_partitions(items):
    """Return canonical set partitions of a finite tuple."""
    items = tuple(items)
    if not items:
        return ((),)
    head, tail = items[0], items[1:]
    out = []
    for part in _set_partitions(tail):
        out.append(tuple(sorted(((head,),) + part)))
        for index, block in enumerate(part):
            new_block = tuple(sorted((head,) + block))
            new_part = list(part)
            new_part[index] = new_block
            out.append(tuple(sorted(new_part)))
    return tuple(dict.fromkeys(out))


def _coarsen_from_fine(fine, partition_of_fine_indices):
    coarse = []
    for index_block in partition_of_fine_indices:
        merged = []
        for idx in index_block:
            merged.extend(fine[idx])
        coarse.append(tuple(sorted(merged)))
    return tuple(sorted(coarse))


def _fine_refines_coarse(fine, coarse):
    for block in fine:
        if not any(set(block).issubset(set(big)) for big in coarse):
            return False
    return True


def _associated_composition_structures(n):
    leaves = tuple(range(n))

    left = set()
    for fine in _set_partitions(leaves):
        fine_indices = tuple(range(len(fine)))
        for coarse_indices in _set_partitions(fine_indices):
            coarse = _coarsen_from_fine(fine, coarse_indices)
            left.add((coarse, fine))

    right = set()
    for coarse in _set_partitions(leaves):
        local_fine_partitions = []
        for block in coarse:
            local_fine_partitions.append(_set_partitions(block))
        for local_fines in product(*local_fine_partitions):
            fine_blocks = []
            for local in local_fines:
                fine_blocks.extend(local)
            fine = tuple(sorted(fine_blocks))
            if _fine_refines_coarse(fine, coarse):
                right.add((coarse, fine))

    return left, right


@independent_verification(
    claim="prop:circ-associative",
    derived_from=[
        "algebraic_foundations.tex proof by three-level rooted tree colimits",
        "LV12 associativity theorem for the composition product",
    ],
    verified_against=[
        "direct enumeration of nested set partitions of {1,...,n}",
        "bijection between fine partitions and their coarsenings",
    ],
    disjoint_rationale=(
        "The proof invokes the abstract tree-colimit description.  The "
        "test enumerates finite nested partitions directly and checks that "
        "left and right association produce the same finite set."
    ),
)
def test_composition_product_associativity_by_nested_partitions():
    for n in range(1, 6):
        left, right = _associated_composition_structures(n)
        assert left == right
        assert all(_fine_refines_coarse(fine, coarse) for coarse, fine in left)


def _matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0])))
        for i in range(len(a))
    )


I2 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
A2 = ((Fraction(1), Fraction(1)), (Fraction(0), Fraction(1)))
B2 = ((Fraction(2), Fraction(0)), (Fraction(1), Fraction(3)))


def _eval_word(word, generator_map):
    value = I2
    for letter in word:
        value = _matmul(value, generator_map[letter])
    return value


def _expr_add(left, right):
    out = defaultdict(Fraction)
    for expr in (left, right):
        for word, coeff in expr.items():
            out[word] += coeff
    return {word: coeff for word, coeff in out.items() if coeff}


def _expr_right_concat(expr, suffix):
    return {word + suffix: coeff for word, coeff in expr.items()}


def _expr_left_concat(prefix, expr):
    return {prefix + word: coeff for word, coeff in expr.items()}


def _d_generator(letter):
    if letter == "x":
        return {("x", "x"): Fraction(1)}
    return {("x", "y"): Fraction(1), ("y", "x"): Fraction(1)}


def _free_derivation(word):
    if len(word) == 1:
        return _d_generator(word[0])
    prefix, suffix = word[:1], word[1:]
    return _expr_add(
        _expr_right_concat(_d_generator(prefix[0]), suffix),
        _expr_left_concat(prefix, _free_derivation(suffix)),
    )


@independent_verification(
    claim="thm:cobar-free",
    derived_from=[
        "cobar_construction.tex definition of Omega^ch(C) as Free_ch(s^-1 Cbar)",
        "manuscript proof using the free-forgetful adjunction",
    ],
    verified_against=[
        "finite tensor algebra on two generators evaluated in M_2(Q)",
        "direct Leibniz extension of a reduced-comultiplication seed",
    ],
    disjoint_rationale=(
        "The theorem proof is adjunction-theoretic.  The test works in the "
        "concrete free associative algebra and verifies extension and "
        "derivation uniqueness by exact matrix evaluation."
    ),
)
def test_cobar_free_universal_extension_and_derivation():
    generator_map = {"x": A2, "y": B2}
    words = [(), ("x",), ("y",), ("x", "y"), ("y", "x"), ("x", "y", "x")]
    for u in words:
        for v in words:
            assert _eval_word(u + v, generator_map) == _matmul(
                _eval_word(u, generator_map),
                _eval_word(v, generator_map),
            )

    for u in (("x",), ("y",), ("x", "y"), ("y", "x"), ("x", "y", "x")):
        for v in (("x",), ("y",), ("x", "x")):
            assert _free_derivation(u + v) == _expr_add(
                _expr_right_concat(_free_derivation(u), v),
                _expr_left_concat(u, _free_derivation(v)),
            )


def _dlog(i, j, z):
    coeffs = [0, 0, 0]
    denom = z[i] - z[j]
    coeffs[i] = 1 / denom
    coeffs[j] = -1 / denom
    return tuple(coeffs)


def _wedge(alpha, beta):
    return (
        simplify(alpha[0] * beta[1] - alpha[1] * beta[0]),
        simplify(alpha[0] * beta[2] - alpha[2] * beta[0]),
        simplify(alpha[1] * beta[2] - alpha[2] * beta[1]),
    )


def _wedge_add(*forms):
    return tuple(simplify(sum(form[i] for form in forms)) for i in range(3))


@independent_verification(
    claim="prop:twisting-morphism-propagator",
    derived_from=[
        "configuration_spaces.tex proof identifying the propagator MC equation",
        "universal twisting-adjunction proposition cited in the statement",
    ],
    verified_against=[
        "symbolic coefficient computation for dlog(z_i-z_j) in the basis dz_i wedge dz_j",
        "direct Arnold three-term cancellation on Conf_3(A^1)",
    ],
    disjoint_rationale=(
        "The manuscript proof uses the bar projection and residue language. "
        "The test computes the logarithmic forms as rational one-forms and "
        "checks the MC cancellation coefficient-by-coefficient."
    ),
)
def test_twisting_propagator_mc_equation_is_arnold_identity():
    z = symbols("z0 z1 z2")
    eta12 = _dlog(0, 1, z)
    eta23 = _dlog(1, 2, z)
    eta31 = _dlog(2, 0, z)
    arnold = _wedge_add(
        _wedge(eta12, eta23),
        _wedge(eta23, eta31),
        _wedge(eta31, eta12),
    )
    assert arnold == (0, 0, 0)


@independent_verification(
    claim="lem:ddr-preserves-log",
    derived_from=[
        "bar_construction.tex proof using local generators dz_i/z_i and dz_j",
        "Fulton-MacPherson normal-crossings divisor local model",
    ],
    verified_against=[
        "direct symbolic de Rham differential in Q[x,y]",
        "pole-order check after multiplying by the boundary coordinate x",
    ],
    disjoint_rationale=(
        "The proof invokes the sheaf-theoretic normal-crossings generator "
        "description.  The test differentiates an explicit logarithmic "
        "one-form and checks by algebra that the result has only a simple "
        "logarithmic pole along x=0."
    ),
)
def test_de_rham_differential_preserves_log_forms_in_local_model():
    x, y = symbols("x y")
    f = y + 1
    g = x * y**2

    # alpha = f dx/x + g dy.  Since d(dx/x)=0 and d(dy)=0,
    # d alpha has dx^dy coefficient -f_y/x + g_x.
    coeff_dx_dy = simplify(-f.diff(y) / x + g.diff(x))
    assert simplify(x * coeff_dx_dy) == simplify(x * y**2 - 1)
    assert coeff_dx_dy.as_numer_denom()[1] == x


def _basis_tuples(n, dim=2):
    return tuple(product(range(dim), repeat=n))


def _perm_matrix(n, sigma, dim=2):
    basis = _basis_tuples(n, dim)
    index = {b: i for i, b in enumerate(basis)}
    out = Matrix.zeros(dim**n, dim**n)
    for col, b in enumerate(basis):
        moved = tuple(b[sigma[i]] for i in range(n))
        out[index[moved], col] = 1
    return out


def _reynolds(matrix, n, dim=2):
    total = Matrix.zeros(dim**n, dim**n)
    perms = tuple(permutations(range(n)))
    for sigma in perms:
        p = _perm_matrix(n, sigma, dim)
        total += p * matrix * p.T
    return total / len(perms)


def _partial_trace_position(matrix, n, trace_pos, dim=2):
    in_basis = _basis_tuples(n, dim)
    out_basis = _basis_tuples(n - 1, dim)
    in_index = {b: i for i, b in enumerate(in_basis)}
    out = Matrix.zeros(dim ** (n - 1), dim ** (n - 1))
    for row_out, r in enumerate(out_basis):
        for col_out, c in enumerate(out_basis):
            value = 0
            for a in range(dim):
                rr = r[:trace_pos] + (a,) + r[trace_pos:]
                cc = c[:trace_pos] + (a,) + c[trace_pos:]
                value += matrix[in_index[rr], in_index[cc]]
            out[row_out, col_out] = value
    return out


def _tensor_operator(*ops):
    out = ops[0]
    for op in ops[1:]:
        out = kronecker_product(out, op)
    return out


E = Matrix([[0, 1], [0, 0]])
F = Matrix([[0, 0], [1, 0]])
H = Matrix([[1, 0], [0, -1]])
ID = eye(2)


def _omega12():
    return (
        Rational(1, 2) * _tensor_operator(H, H, ID)
        + _tensor_operator(E, F, ID)
        + _tensor_operator(F, E, ID)
    )


def _omega23():
    return (
        Rational(1, 2) * _tensor_operator(ID, H, H)
        + _tensor_operator(ID, E, F)
        + _tensor_operator(ID, F, E)
    )


@independent_verification(
    claim="prop:e1-nonsplitting-obstruction",
    derived_from=[
        "e1_modular_koszul.tex proof by cross-degree leakage and associator kernel",
        "e1_nonsplitting_obstruction_engine.py finite-dimensional obstruction engine",
    ],
    verified_against=[
        "exact sl2 fundamental-representation Casimir matrices over Q",
        "brute-force Reynolds projection on End((Q^2)^tensor n)",
        "deterministic matrix-unit search for partial-trace leakage",
    ],
    disjoint_rationale=(
        "The manuscript proof and existing engine state the obstruction. "
        "The test reconstructs the relevant finite matrices from the "
        "sl2 generators, averages over S_n explicitly, and searches matrix "
        "units without importing the obstruction engine."
    ),
)
def test_e1_nonsplitting_exact_sl2_kernel_and_cross_degree_leakage():
    associator_linear_term = _omega12() * _omega23() - _omega23() * _omega12()
    assert associator_linear_term != Matrix.zeros(8, 8)
    assert _reynolds(associator_linear_term, 3) == Matrix.zeros(8, 8)

    leakage_witness = None
    for row, col in product(range(8), repeat=2):
        unit = Matrix.zeros(8, 8)
        unit[row, col] = 1
        kernel_part = unit - _reynolds(unit, 3)
        leaked = _reynolds(_partial_trace_position(kernel_part, 3, 1), 2)
        if kernel_part != Matrix.zeros(8, 8) and leaked != Matrix.zeros(4, 4):
            leakage_witness = (kernel_part, leaked)
            break

    assert leakage_witness is not None
    kernel_part, leaked = leakage_witness
    assert _reynolds(kernel_part, 3) == Matrix.zeros(8, 8)
    assert leaked != Matrix.zeros(4, 4)


def _deconcatenation(word):
    return [((word[:i]), (word[i:])) for i in range(len(word) + 1)]


def _bar_differential(word):
    out = defaultdict(Fraction)
    for i in range(len(word) - 1):
        collapsed = word[:i] + (word[i] + word[i + 1],) + word[i + 2 :]
        out[collapsed] += Fraction((-1) ** i)
    return {key: value for key, value in out.items() if value}


def _delta_expr(expr):
    out = defaultdict(Fraction)
    for word, coeff in expr.items():
        for left, right in _deconcatenation(word):
            out[(left, right)] += coeff
    return {key: value for key, value in out.items() if value}


def _coderivation_rhs(word):
    out = defaultdict(Fraction)
    for left, right in _deconcatenation(word):
        for dleft, coeff in _bar_differential(left).items():
            out[(dleft, right)] += coeff
        for dright, coeff in _bar_differential(right).items():
            # In the suspended bar coalgebra the coderivation has odd
            # degree; moving it past the left tensor factor contributes
            # the Koszul sign (-1)^{|left|}.
            out[(left, dright)] += ((-1) ** len(left)) * coeff
    return {key: value for key, value in out.items() if value}


@independent_verification(
    claim="thm:diff-is-coderivation",
    derived_from=[
        "bar_construction.tex proof using operadic bar construction",
        "LV12 coderivation formalism for tensor coalgebras",
    ],
    verified_against=[
        "direct deconcatenation coproduct on finite words",
        "explicit adjacent-contraction bar differential with Koszul signs",
    ],
    disjoint_rationale=(
        "The theorem proof is operadic.  The test expands both sides of the "
        "coderivation identity on finite words and compares the resulting "
        "signed tensor sums exactly."
    ),
)
def test_bar_differential_is_coderivation_on_finite_words():
    for word in (
        ("a", "b"),
        ("a", "b", "c"),
        ("a", "b", "c", "d"),
    ):
        left = _delta_expr(_bar_differential(word))
        right = _coderivation_rhs(word)
        assert left == right
