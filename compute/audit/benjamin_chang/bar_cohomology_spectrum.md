# Bar Cohomology and the Primary Spectrum

## Date: 2026-04-01
## Status: RESOLVED (definitive negative + constructive positive)
## Sources: first-principles computation, bar_cohomology_dimensions.py, virasoro_bar_explicit.py, bar_character_algebraic.py, spectral_zeta_bar.py

---

## 0. Summary

**Question**: Is d(h) = dim(quasi-primaries at weight h) computable from the bar complex B(V)?

**Answer**: d(h) is NOT any single bar cohomology group H^k(B(V))_h. It is not even the alternating sum. However, d(h) IS determined by bar cohomology through the Koszul duality character relation. The chain is:

    B(V) -> H^*(B(V)) -> chi_{A!}(q) -> chi_V(q) = 1/(1 - chi_{A!}(q)) -> d(h) = chi_V(h) - chi_V(h-1)

The spectral zeta epsilon^c_s = sum d(h)(2h)^{-s} is NOT a direct homotopy-theoretic invariant of B(V). It diverges for all s (subexponential growth of d(h)). The bar complex determines the spectral data through algebraic inversion, not through direct cohomological extraction.

---

## 1. The Central Falsification: d(h) != H^1(B(V))_h

### Bar cohomology H^1(B(Vir))_h via Chevalley-Eilenberg

The CE complex Lambda^k(Vir_-^*) of Vir_- = span{L_{-n} : n >= 2} gives:

| Weight h | H^1(B(Vir))_h | d(h) |
|----------|---------------|------|
| 2        | 1             | 1    |
| 3        | 1             | 0    |
| 4        | 1             | 1    |
| 5        | 0             | 0    |
| 6        | 0             | 2    |
| 7        | 0             | 0    |
| 8        | 0             | 3    |
| 9        | 0             | 1    |
| 10       | 0             | 4    |

H^1(B(Vir))_h is nonzero ONLY at h = 2, 3, 4. These are the three generators of the Koszul dual A!. The total is 3, finite. In contrast, d(h) grows without bound.

**Proof that H^1 vanishes for h >= 5**: The CE differential d: Lambda^1_h -> Lambda^2_h sends L_{-h}^* to sum_{2 <= a < b, a+b=h} (b-a) L_{-a}^* \wedge L_{-b}^*. For h >= 5, the pair (a,b) = (2, h-2) exists with h-2 > 2 (since h >= 5 implies h-2 >= 3 > 2). The coefficient (h-2-2) = (h-4) is nonzero for h >= 5. So d is nonzero, and since Lambda^1_h is 1-dimensional, ker(d) = 0, hence H^1_h = 0.

### Bar cohomology at higher bar degrees

From the explicit mode-level computation (bar_cohomology_dimensions.py):

| Weight h | H^1 | H^2 | Total |
|----------|------|------|-------|
| 2        | 1    | 0    | 1     |
| 3        | 1    | 0    | 1     |
| 4        | 1    | 0    | 1     |
| 5        | 0    | 0    | 0     |
| 6        | 0    | 0    | 0     |
| 7        | 0    | 1    | 1     |
| 8        | 0    | 1    | 1     |
| 9        | 0    | 1    | 1     |
| 10       | 0    | 1    | 1     |

H^2 starts at weight 7 (the first "relation" in the Koszul dual). The alternating character:

    chi_{A!}(q) = 1 - 1/chi_V(q) = q^2 + q^3 + q^4 - q^7 - q^8 - q^9 - q^10 - q^11 + ...

Positive terms correspond to H^1 (generators), negative terms to H^2 (relations).

---

## 2. The Koszul Inversion Route

### The character identity

For a Koszul chiral algebra V:

    chi_V(q) * (1 - chi_{A!}(q)) = 1

where chi_{A!}(q) = sum_h [H^1_h - H^2_h + H^3_h - ...] q^h is the alternating bar cohomology character.

This is verified computationally through order q^30 in test_spectral_zeta_bar.py.

### The chain from bar to spectrum

1. **Bar complex B(V)**: the chain complex with differential from the chiral OPE
2. **Bar cohomology H^*(B(V))**: concentrated in bar degrees 1 and 2 (for Virasoro)
3. **Alternating character chi_{A!}**: determined by H^*(B(V))
4. **Vacuum module character chi_V**: recovered by chi_V = 1/(1 - chi_{A!})
5. **Vacuum module dimensions**: dim V_h = p_{>=2}(h) (coefficient of q^h in chi_V)
6. **Quasi-primary count**: d(h) = p_{>=2}(h) - p_{>=2}(h-1) for h >= 2

Each step is algebraic and computable. The bar complex DOES encode d(h), but not as a single cohomology group. It encodes it through power series inversion.

---

## 3. Motzkin Differences vs Quasi-Primary Counts

The sequence h_n = M(n+1) - M(n) = 1, 2, 5, 12, 30, 76, 196, 512, ... from bar_character_algebraic.py is NOT the quasi-primary count d(h). It is the Hilbert series of the full Koszul dual ALGEBRA A! in a rescaled weight grading.

| Index n | h_n (Motzkin diff) | d(n+1) (quasi-primary) |
|---------|--------------------|------------------------|
| 1       | 1                  | 0                      |
| 2       | 2                  | 1                      |
| 3       | 5                  | 0                      |
| 4       | 12                 | 2                      |
| 5       | 30                 | 0                      |
| 6       | 76                 | 3                      |

These are completely different sequences with different growth rates:
- h_n ~ 3^n / n^{3/2} (algebraic growth, Catalan discriminant)
- d(h) ~ exp(pi*sqrt(2h/3)) / h^{3/2} (subexponential, Hardy-Ramanujan)

---

## 4. Spectral Zeta Divergence

The spectral zeta epsilon^c_s = sum_{h>=2} d(h) (2h)^{-s} diverges for ALL s in C.

**Proof**: d(h) >= 0 for h >= 2, and d(h) ~ exp(C*sqrt(h)) with C = pi*sqrt(2/3) ~ 2.565. The terms d(h) * (2h)^{-sigma} ~ exp(C*sqrt(h) - sigma*log(2h)) -> infinity for any fixed sigma, since sqrt(h) dominates log(h). Since all terms are non-negative, the series cannot converge conditionally either.

The abscissa of convergence is sigma_c = +infinity. This is FUNDAMENTALLY different from:
- Minimal models: finitely many primaries, epsilon is a finite sum
- Lattice VOAs: d(h) grows polynomially, sigma_c = dim/2
- Shadow metric Epstein: positive definite form, sigma_c = 1

---

## 5. c-Independence

d(h) = p_{>=2}(h) - p_{>=2}(h-1) is INDEPENDENT of c at generic c.

**Proof**: L_1 acts on V_h via [L_1, L_{-n}] = (1+n)L_{1-n}. For n >= 2, the mode index 1-n <= -1 is always negative, so the central term (c/12)(m^3-m)delta_{m+n,0} never contributes (since 1-n < 0). The L_1 matrix has entries that are INDEPENDENT of c. Its rank is therefore constant at generic c, so dim ker(L_1) is constant.

For MINIMAL MODELS at c = c_{p,q}: null vectors reduce V_c, changing d(h). The first null vector appears at weight pq - p - q + 1.

---

## 6. What Would Be a Direct Bar-Cohomological Spectral Invariant?

The most natural spectral invariant FROM the bar complex directly is the ALTERNATING ZETA:

    zeta_{A!}(s) = sum_h chi_{A!}(h) * h^{-s} = sum_h [H^1_h - H^2_h + ...] * h^{-s}

For Virasoro, this would be:

    zeta_{A!}(s) = 2^{-s} + 3^{-s} + 4^{-s} - 7^{-s} - 8^{-s} - 9^{-s} - 10^{-s} - 11^{-s} + ...

This series has CANCELLATIONS (alternating signs) and may converge. Its analytic properties would be a genuine homotopy-theoretic invariant of B(V). Whether it satisfies a functional equation is an open question.

---

## 7. Files Created

- `/Users/raeez/chiral-bar-cobar/compute/lib/spectral_zeta_bar.py` (11 sections, full analysis)
- `/Users/raeez/chiral-bar-cobar/compute/tests/test_spectral_zeta_bar.py` (83 tests, 17 test classes)
- This document

## 8. Cross-Validated Against

- `virasoro_constrained_epstein.py` (d(h) values match)
- `bar_character_algebraic.py` (Motzkin numbers match)
- `virasoro_bar_explicit.py` (CE H^1 dims match)
- `bar_cohomology_dimensions.py` (explicit mode-level bar cohomology confirms H^1 at 2,3,4 and H^2 at 7+)
- `theta_deformation_complex.py` (quasi-primary counts at c=1 match d(h) formula)
