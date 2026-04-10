r"""Verification engine for alpha_g = 2*rank + 4*dim*h^v across simple Lie algebras.

Computes and verifies the formula alpha_g = 2*rank + 4*dim(g)*h^v for all
simple Lie algebras in types A_1--A_8, B_2--B_8, C_3--C_8, D_4--D_8,
G_2, F_4, E_6, E_7, E_8 (31 algebras total).

LIE ALGEBRA DATA:
  For each simple Lie algebra g we record:
    rank(g)  = rank of root system
    dim(g)   = dimension of g as vector space = |Phi| + rank
    h^v      = dual Coxeter number

  Classical formulas:
    A_n: rank = n,  dim = n(n+2) = n^2+2n,  h^v = n+1
    B_n: rank = n,  dim = n(2n+1),           h^v = 2n-1
    C_n: rank = n,  dim = n(2n+1),           h^v = n+1
    D_n: rank = n,  dim = n(2n-1),           h^v = 2n-2

  Exceptional:
    G_2: rank=2, dim=14, h^v=4
    F_4: rank=4, dim=52, h^v=9
    E_6: rank=6, dim=78, h^v=12
    E_7: rank=7, dim=133, h^v=18
    E_8: rank=8, dim=248, h^v=30

  Note: B_n and C_n share dim = n(2n+1) but have DIFFERENT dual Coxeter
  numbers: h^v(B_n) = 2n-1, h^v(C_n) = n+1.

ISOMORPHISMS:
  B_2 = C_2 (so_5 = sp_4): both rank=2, dim=10, h^v=3. We include B_2
  in the B-series and start C at n=3 to avoid double-counting.
  D_3 = A_3 (so_6 = sl_4): rank=3, dim=15, h^v=4. We start D at n=4.

FORMULA:
  alpha_g = 2*rank(g) + 4*dim(g)*h^v(g)

  This is the anomaly coefficient appearing in the genus-g obstruction
  theory for the modular bar complex. It encodes the interplay between
  the rank contribution (2*rank, from the Cartan directions) and the
  curvature contribution (4*dim*h^v, from the adjoint Casimir at the
  dual Coxeter level).

Conventions:
  - All data are exact integers (no floating point).
  - Cohomological grading, |d| = +1.
"""

from typing import Dict, List, NamedTuple, Tuple


class LieAlgebraData(NamedTuple):
    """Data for a simple Lie algebra."""
    name: str
    series: str       # 'A', 'B', 'C', 'D', or 'EXC'
    rank: int
    dim: int
    dual_coxeter: int  # h^v


# ============================================================
# Lie algebra table: all 31 simple Lie algebras in the range
# ============================================================

def _build_lie_algebra_table() -> Dict[str, LieAlgebraData]:
    """Build the complete table of simple Lie algebras.

    Ranges: A_1--A_8, B_2--B_8, C_3--C_8, D_4--D_8, G_2, F_4, E_6--E_8.
    Total: 8 + 7 + 6 + 5 + 5 = 31 algebras.
    """
    table: Dict[str, LieAlgebraData] = {}

    # A_n (n = 1, ..., 8): sl_{n+1}
    # rank = n, dim = n(n+2), h^v = n+1
    for n in range(1, 9):
        name = f'A{n}'
        table[name] = LieAlgebraData(
            name=name, series='A',
            rank=n, dim=n * (n + 2), dual_coxeter=n + 1,
        )

    # B_n (n = 2, ..., 8): so_{2n+1}
    # rank = n, dim = n(2n+1), h^v = 2n-1
    for n in range(2, 9):
        name = f'B{n}'
        table[name] = LieAlgebraData(
            name=name, series='B',
            rank=n, dim=n * (2 * n + 1), dual_coxeter=2 * n - 1,
        )

    # C_n (n = 3, ..., 8): sp_{2n}
    # rank = n, dim = n(2n+1), h^v = n+1
    for n in range(3, 9):
        name = f'C{n}'
        table[name] = LieAlgebraData(
            name=name, series='C',
            rank=n, dim=n * (2 * n + 1), dual_coxeter=n + 1,
        )

    # D_n (n = 4, ..., 8): so_{2n}
    # rank = n, dim = n(2n-1), h^v = 2n-2
    for n in range(4, 9):
        name = f'D{n}'
        table[name] = LieAlgebraData(
            name=name, series='D',
            rank=n, dim=n * (2 * n - 1), dual_coxeter=2 * n - 2,
        )

    # Exceptional algebras
    table['G2'] = LieAlgebraData(name='G2', series='EXC', rank=2, dim=14, dual_coxeter=4)
    table['F4'] = LieAlgebraData(name='F4', series='EXC', rank=4, dim=52, dual_coxeter=9)
    table['E6'] = LieAlgebraData(name='E6', series='EXC', rank=6, dim=78, dual_coxeter=12)
    table['E7'] = LieAlgebraData(name='E7', series='EXC', rank=7, dim=133, dual_coxeter=18)
    table['E8'] = LieAlgebraData(name='E8', series='EXC', rank=8, dim=248, dual_coxeter=30)

    return table


LIE_ALGEBRA_TABLE: Dict[str, LieAlgebraData] = _build_lie_algebra_table()


# ============================================================
# Core formula
# ============================================================

def alpha_g(rank: int, dim: int, dual_coxeter: int) -> int:
    """Compute alpha_g = 2*rank + 4*dim*h^v.

    All inputs and the result are exact integers.
    """
    return 2 * rank + 4 * dim * dual_coxeter


def alpha_g_for_algebra(name: str) -> int:
    """Compute alpha_g for a named simple Lie algebra."""
    data = LIE_ALGEBRA_TABLE[name]
    return alpha_g(data.rank, data.dim, data.dual_coxeter)


# ============================================================
# Cross-checks on Lie algebra data
# ============================================================

def verify_classical_dim(data: LieAlgebraData) -> bool:
    """Verify dim(g) against the classical rank formula.

    A_n: dim = n(n+2)
    B_n: dim = n(2n+1)
    C_n: dim = n(2n+1)
    D_n: dim = n(2n-1)
    """
    n = data.rank
    expected = {
        'A': n * (n + 2),
        'B': n * (2 * n + 1),
        'C': n * (2 * n + 1),
        'D': n * (2 * n - 1),
    }
    if data.series in expected:
        return data.dim == expected[data.series]
    # Exceptionals: no parametric formula, skip
    return True


def verify_classical_dual_coxeter(data: LieAlgebraData) -> bool:
    """Verify h^v against the classical rank formula.

    A_n: h^v = n+1
    B_n: h^v = 2n-1
    C_n: h^v = n+1
    D_n: h^v = 2n-2
    """
    n = data.rank
    expected = {
        'A': n + 1,
        'B': 2 * n - 1,
        'C': n + 1,
        'D': 2 * n - 2,
    }
    if data.series in expected:
        return data.dual_coxeter == expected[data.series]
    return True


def verify_all_classical_data() -> List[str]:
    """Verify dim and h^v for all classical-type algebras. Returns list of failures."""
    failures = []
    for name, data in LIE_ALGEBRA_TABLE.items():
        if not verify_classical_dim(data):
            failures.append(f'{name}: dim mismatch (got {data.dim})')
        if not verify_classical_dual_coxeter(data):
            failures.append(f'{name}: h^v mismatch (got {data.dual_coxeter})')
    return failures


# ============================================================
# Full computation
# ============================================================

class AlphaResult(NamedTuple):
    """Result of alpha_g computation for one algebra."""
    name: str
    rank: int
    dim: int
    dual_coxeter: int
    alpha_g: int
    rank_contribution: int     # 2*rank
    curvature_contribution: int  # 4*dim*h^v


def compute_all_alpha_g() -> Dict[str, AlphaResult]:
    """Compute alpha_g for all 31 simple Lie algebras in the table."""
    results: Dict[str, AlphaResult] = {}
    for name, data in LIE_ALGEBRA_TABLE.items():
        ag = alpha_g(data.rank, data.dim, data.dual_coxeter)
        results[name] = AlphaResult(
            name=name,
            rank=data.rank,
            dim=data.dim,
            dual_coxeter=data.dual_coxeter,
            alpha_g=ag,
            rank_contribution=2 * data.rank,
            curvature_contribution=4 * data.dim * data.dual_coxeter,
        )
    return results


def verify_alpha_g_positivity() -> List[str]:
    """Verify alpha_g > 0 for all algebras. Returns list of failures."""
    failures = []
    results = compute_all_alpha_g()
    for name, r in results.items():
        if r.alpha_g <= 0:
            failures.append(f'{name}: alpha_g = {r.alpha_g} <= 0')
    return failures


def verify_alpha_g_integrality() -> List[str]:
    """Verify alpha_g is a positive integer for all algebras. Returns list of failures."""
    failures = []
    results = compute_all_alpha_g()
    for name, r in results.items():
        if not isinstance(r.alpha_g, int):
            failures.append(f'{name}: alpha_g = {r.alpha_g} is not int')
    return failures


# ============================================================
# Isomorphism checks
# ============================================================

def check_b2_c2_isomorphism() -> Tuple[bool, str]:
    """Check that B_2 and C_2 have the same Lie algebra (so_5 = sp_4).

    B_2: rank=2, dim=10, h^v=3
    C_2 would be: rank=2, dim=2*(2*2+1)=10, h^v=2+1=3

    Since dim and h^v match, alpha_g would also match.
    C_2 is not in our table (C starts at n=3) to avoid double counting,
    but we verify the data would agree.
    """
    b2 = LIE_ALGEBRA_TABLE['B2']
    # C_2 data from formulas
    c2_rank = 2
    c2_dim = 2 * (2 * 2 + 1)   # = 10
    c2_hv = 2 + 1              # = 3

    match = (b2.rank == c2_rank and b2.dim == c2_dim and b2.dual_coxeter == c2_hv)
    alpha_b2 = alpha_g(b2.rank, b2.dim, b2.dual_coxeter)
    alpha_c2 = alpha_g(c2_rank, c2_dim, c2_hv)
    msg = (f'B2: rank={b2.rank}, dim={b2.dim}, hv={b2.dual_coxeter}, alpha={alpha_b2}; '
           f'C2: rank={c2_rank}, dim={c2_dim}, hv={c2_hv}, alpha={alpha_c2}')
    return (match and alpha_b2 == alpha_c2), msg


def check_d3_a3_isomorphism() -> Tuple[bool, str]:
    """Check that D_3 and A_3 have the same Lie algebra (so_6 = sl_4).

    A_3: rank=3, dim=3*5=15, h^v=4
    D_3 would be: rank=3, dim=3*(2*3-1)=15, h^v=2*3-2=4

    D_3 is not in our table (D starts at n=4) to avoid double counting,
    but we verify the data would agree.
    """
    a3 = LIE_ALGEBRA_TABLE['A3']
    # D_3 data from formulas
    d3_rank = 3
    d3_dim = 3 * (2 * 3 - 1)   # = 15
    d3_hv = 2 * 3 - 2          # = 4

    match = (a3.rank == d3_rank and a3.dim == d3_dim and a3.dual_coxeter == d3_hv)
    alpha_a3 = alpha_g(a3.rank, a3.dim, a3.dual_coxeter)
    alpha_d3 = alpha_g(d3_rank, d3_dim, d3_hv)
    msg = (f'A3: rank={a3.rank}, dim={a3.dim}, hv={a3.dual_coxeter}, alpha={alpha_a3}; '
           f'D3: rank={d3_rank}, dim={d3_dim}, hv={d3_hv}, alpha={alpha_d3}')
    return (match and alpha_a3 == alpha_d3), msg


# ============================================================
# Summary
# ============================================================

def print_summary() -> None:
    """Print a formatted summary table of all alpha_g values."""
    results = compute_all_alpha_g()
    sorted_names = []
    for series in ['A', 'B', 'C', 'D']:
        sorted_names.extend(
            sorted([n for n, d in LIE_ALGEBRA_TABLE.items() if d.series == series],
                   key=lambda x: int(x[1:])))
    sorted_names.extend(['G2', 'F4', 'E6', 'E7', 'E8'])

    print(f"{'Name':>4s}  {'rank':>4s}  {'dim':>5s}  {'h^v':>4s}  "
          f"{'2*rank':>6s}  {'4*dim*hv':>8s}  {'alpha_g':>8s}")
    print('-' * 52)
    for name in sorted_names:
        r = results[name]
        print(f'{r.name:>4s}  {r.rank:>4d}  {r.dim:>5d}  {r.dual_coxeter:>4d}  '
              f'{r.rank_contribution:>6d}  {r.curvature_contribution:>8d}  {r.alpha_g:>8d}')
    print('-' * 52)
    print(f'Total algebras: {len(results)}')


if __name__ == '__main__':
    print_summary()
    failures = verify_all_classical_data()
    if failures:
        print(f'\nCross-check FAILURES: {failures}')
    else:
        print('\nAll classical cross-checks passed.')
    pos_failures = verify_alpha_g_positivity()
    if pos_failures:
        print(f'Positivity FAILURES: {pos_failures}')
    else:
        print('All alpha_g values positive.')
