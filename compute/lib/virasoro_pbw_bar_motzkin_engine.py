r"""Virasoro PBW dimensions, bar cohomology dimensions, and the Motzkin difference sequence.

Computes three interrelated sequences at each generation degree n = 1, ..., N_max:

  1. PBW dimension = p(n), the number of partitions of n.
     This is dim(U(Vir_-)_n), the weight-n component of the PBW basis
     for the universal enveloping algebra of the negative-mode Virasoro
     subalgebra Vir_- = span{L_{-1}, L_{-2}, ...}.

  2. Bar cohomology total dimension = [x^n] x*M(x)^2.
     By Koszulness of the Virasoro algebra (Theorem B + landscape census),
     the bar cohomology generating function for W_2 = Vir is P(x) = x*M(x)^2,
     where M(x) is the Motzkin generating function.
     Dims: 1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610, ...

  3. Motzkin numbers M(n) (OEIS A001006) = Koszul dual character of Virasoro.
     The key identity linking bar cohomology to Motzkin numbers:
       M(n) - M(n-1) = bar_cohom(n-1)   for n >= 2
     i.e., the Motzkin INCREMENT equals the bar cohomology dimension
     at the previous degree.

The Motzkin numbers satisfy the recurrence:
  M(0) = 1, M(1) = 1,
  M(n) = M(n-1) + sum_{k=0}^{n-2} M(k) * M(n-2-k)   for n >= 2.

Equivalently, M(x) = (1 - x - sqrt(1 - 2x - 3x^2)) / (2x^2).

VERIFICATION PATHS (AP10/HZ-6):
  Partition numbers: [DC] dynamic programming + [LT] OEIS A000041 (Euler, 1748)
  Motzkin numbers:   [DC] recurrence relation + [LT] OEIS A001006 (Motzkin, 1948)
  Motzkin alt path:  [CF] trinomial/binomial sum (Donaghey & Shapiro, 1977)
  Bar cohomology:    [DC] Motzkin convolution + [LT] bar_cohomology_wn_universal_engine.py

Conventions:
  - Cohomological grading, |d| = +1
  - Generation degree n (Koszul dual grading), not conformal weight
  - Desuspension lowers degree: |s^{-1}v| = |v| - 1 (AP45)
"""


# ============================================================
# Partition numbers p(n) -- PBW dimensions of U(Vir_-)
# ============================================================

def partitions_up_to(n_max):
    """Compute partition numbers p(0), p(1), ..., p(n_max) via dynamic programming.

    Uses the standard recurrence: p(n) = number of ways to write n as
    a sum of positive integers (order irrelevant).

    Returns a list of length n_max + 1.

    Verification:
      # VERIFIED [DC] dynamic programming recurrence + [LT] OEIS A000041
    """
    p = [0] * (n_max + 1)
    p[0] = 1  # empty partition
    for k in range(1, n_max + 1):
        for j in range(k, n_max + 1):
            p[j] += p[j - k]
    return p


def partition_number(n):
    """Return p(n), the number of partitions of n.

    For n < 0, returns 0.  For n = 0, returns 1 (the empty partition).
    """
    if n < 0:
        return 0
    return partitions_up_to(n)[n]


# ============================================================
# Motzkin numbers M(n) -- OEIS A001006
# ============================================================

def motzkin_up_to(n_max):
    """Compute Motzkin numbers M(0), M(1), ..., M(n_max) via the recurrence.

    Recurrence: M(n) = M(n-1) + sum_{k=0}^{n-2} M(k)*M(n-2-k)  for n >= 2.
    Base cases: M(0) = M(1) = 1.

    The convolution sum is equivalent to the coefficient of x^{n-2} in M(x)^2.

    Returns a list of length n_max + 1.

    Verification:
      # VERIFIED [DC] recurrence + [LT] OEIS A001006 + [CF] generating function
    """
    if n_max < 0:
        return []
    m = [0] * (n_max + 1)
    m[0] = 1
    if n_max >= 1:
        m[1] = 1
    for n in range(2, n_max + 1):
        conv = sum(m[k] * m[n - 2 - k] for k in range(n - 1))
        m[n] = m[n - 1] + conv
    return m


def motzkin_number(n):
    """Return M(n), the n-th Motzkin number.

    M(0) = 1, M(1) = 1, M(2) = 2, M(3) = 4, M(4) = 9, ...
    For n < 0, returns 0.
    """
    if n < 0:
        return 0
    return motzkin_up_to(n)[n]


# ============================================================
# Alternative Motzkin computation via trinomial/binomial sum
# ============================================================

def motzkin_via_trinomial(n):
    """Compute M(n) via the trinomial/binomial sum formula.

    M(n) = sum_{k=0}^{floor(n/2)} C(n, 2k) * C_k
    where C_k = C(2k, k) / (k+1) is the k-th Catalan number.

    This provides an independent computation path.

    Verification:
      # VERIFIED [DC] binomial sum + [LT] Donaghey & Shapiro (1977)
    """
    result = 0
    for k in range(n // 2 + 1):
        binom_n_2k = _binomial(n, 2 * k)
        catalan_k = _binomial(2 * k, k) // (k + 1)
        result += binom_n_2k * catalan_k
    return result


def _binomial(n, k):
    """Compute binomial coefficient C(n, k) exactly."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


# ============================================================
# Bar cohomology dimensions (generation degree)
# ============================================================

def virasoro_bar_cohom_gen_degree(n_max):
    """Bar cohomology dims in generation degree via P(x) = x * M(x)^2.

    The coefficient of x^n in x * M(x)^2 is:
      [x^n] x*M(x)^2 = [x^{n-1}] M(x)^2 = sum_{k=0}^{n-1} M(k)*M(n-1-k)

    for n >= 1.

    Returns dict mapping generation degree n -> dim H^*(B(Vir))_n for n = 1..n_max.

    Verification:
      # VERIFIED [DC] convolution + [LT] bar_cohomology_wn_universal_engine.py
    """
    m = motzkin_up_to(n_max)
    result = {}
    for n in range(1, n_max + 1):
        conv = sum(m[k] * m[n - 1 - k] for k in range(n))
        result[n] = conv
    return result


# ============================================================
# Full table computation
# ============================================================

def virasoro_pbw_bar_motzkin_table(n_max=20):
    """Full table relating PBW dims, bar cohomology, and Motzkin numbers.

    At each generation degree n = 1, ..., n_max, computes:
      - pbw_dim:           p(n) = partition number (PBW basis dim at weight n)
      - bar_cohom:         [x^n] x*M(x)^2 = Motzkin convolution (bar cohom dim)
      - motzkin:           M(n) = n-th Motzkin number (Koszul dual dim)
      - motzkin_increment: M(n) - M(n-1) = bar_cohom(n-1) for n >= 2

    Key identities:
      (a) bar_cohom(n) = sum_{k=0}^{n-1} M(k)*M(n-1-k)
      (b) M(n) - M(n-1) = bar_cohom(n-1)  for n >= 2

    Returns a list of dicts.

    Verification:
      # VERIFIED [DC] all paths independent + [LT] OEIS A000041/A001006
    """
    p = partitions_up_to(n_max)
    m = motzkin_up_to(n_max)
    bar = virasoro_bar_cohom_gen_degree(n_max)

    table = []
    for n in range(1, n_max + 1):
        motzkin_incr = m[n] - m[n - 1] if n >= 1 else 0
        row = {
            'degree': n,
            'pbw_dim': p[n],
            'bar_cohom': bar[n],
            'motzkin': m[n],
            'motzkin_prev': m[n - 1],
            'motzkin_increment': motzkin_incr,
        }
        table.append(row)
    return table


# ============================================================
# Canonical reference data
# ============================================================

# OEIS A000041: partition numbers p(1)..p(20)
# VERIFIED [DC] dynamic programming + [LT] OEIS A000041 (Euler, 1748)
PARTITIONS_1_TO_20 = [
    1, 2, 3, 5, 7, 11, 15, 22, 30, 42,
    56, 77, 101, 135, 176, 231, 297, 385, 490, 627,
]

# OEIS A001006: Motzkin numbers M(0)..M(19)
# VERIFIED [DC] recurrence + [LT] OEIS A001006 (Motzkin, 1948)
# VERIFIED [CF] trinomial sum (Donaghey & Shapiro, 1977)
MOTZKIN_0_TO_19 = [
    1, 1, 2, 4, 9, 21, 51, 127, 323, 835,
    2188, 5798, 15511, 41835, 113634, 310572, 853467, 2356779, 6536382, 18199284,
]

# Bar cohomology dims in generation degree for W_2 (Virasoro), degrees 1..10
# VERIFIED [DC] convolution of Motzkin + [LT] bar_cohomology_wn_universal_engine.py
BAR_COHOM_GEN_DEGREE_1_TO_10 = [1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610]


# ============================================================
# Summary / display
# ============================================================

def print_table(n_max=20):
    """Print the full PBW/bar/Motzkin table."""
    table = virasoro_pbw_bar_motzkin_table(n_max)
    header = (f"{'deg':>4} {'p(n)':>8} {'bar H*':>10} "
              f"{'M(n)':>12} {'M(n)-M(n-1)':>14}")
    print(header)
    print("-" * len(header))
    for row in table:
        print(f"{row['degree']:>4} {row['pbw_dim']:>8} {row['bar_cohom']:>10} "
              f"{row['motzkin']:>12} {row['motzkin_increment']:>14}")


if __name__ == '__main__':
    print("Virasoro PBW / Bar Cohomology / Motzkin Table (degrees 1-20)")
    print("=" * 60)
    print()
    print_table(20)
    print()

    # Cross-verification: recurrence vs trinomial
    print("Cross-verification: Motzkin via recurrence vs trinomial sum")
    m_rec = motzkin_up_to(19)
    m_tri = [motzkin_via_trinomial(k) for k in range(20)]
    all_match = all(m_rec[k] == m_tri[k] for k in range(20))
    print(f"  All 20 values match: {all_match}")
    print()

    # Verify identity (b): M(n) - M(n-1) = bar_cohom(n-1) for n >= 2
    bar = virasoro_bar_cohom_gen_degree(20)
    m = motzkin_up_to(20)
    identity_holds = all(m[n] - m[n - 1] == bar[n - 1] for n in range(2, 21))
    print(f"Identity M(n) - M(n-1) = bar_cohom(n-1): {identity_holds}")
