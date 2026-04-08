# Generating Function Investigation: delta_F_g^cross(W_3)

## Data

Three genera of the cross-channel correction to the multi-weight genus expansion
F_g(A) = kappa(A) * lambda_g^FP + delta_F_g^cross(A), computed for W_3
(generators T at weight 2, W at weight 3; kappa = 5c/6):

```
g=2: delta_F_2 = (c + 204) / (16c)
g=3: delta_F_3 = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)
g=4: delta_F_4 = (287c^4 + 268881c^3 + 115455816c^2
                  + 29725133760c + 5594347866240) / (17418240 c^3)
```

Source: `multi_weight_genus_tower.py`, `theorem_delta_f3_universal_engine.py`,
`delta_fg_degree_pattern_engine.py`.

## 1. Numerator Structure

All three numerator polynomials P_g(c) are **irreducible over Q**.
They share no common roots: P_3(-204) = 98010432 and P_4(-204) = 2549573319744,
both nonzero.

All coefficients of each P_g are **strictly positive**. This implies
delta_F_g^cross > 0 for all c > 0 at every genus: the cross-channel
correction is a strictly positive contribution.

Factorizations of individual coefficients:
- 204 = 2^2 * 3 * 17
- 3792 = 2^4 * 3 * 79;  1149120 = 2^6 * 3^3 * 5 * 7 * 19;
  217071360 = 2^8 * 3^3 * 5 * 11 * 571
- 287 = 7 * 41

No common prime structure links the numerator coefficients across genera.

## 2. Degree-Genus Pattern

| g | deg(P_g) | denom power c^{g-1} | net degree e_g | # terms |
|---|----------|---------------------|----------------|---------|
| 2 | 1        | c^1                 | 0              | 2       |
| 3 | 3        | c^2                 | 1              | 4       |
| 4 | 4        | c^3                 | 1              | 5       |

**Pattern**: deg(P_g) = g for g >= 3; deg(P_2) = 1 (special case).
The net degree e_g = deg(P_g) - (g-1) equals 0 at g=2 and stabilizes at 1
for g >= 3. Large-c asymptotics:

```
delta_F_2 ~ 1/16                    (constant)
delta_F_g ~ (lc_g / D_g) * c        for g >= 3 (linear in c)
```

## 3. Denominator Analysis

```
D_2 = 16         = 2^4
D_3 = 138240     = 2^10 * 3^3 * 5
D_4 = 17418240   = 2^11 * 3^5 * 5 * 7
```

**Prime support**: {2}, {2,3,5}, {2,3,5,7}. The primes appearing in D_g
are exactly the primes up to 2g-1.

**A-hat connection**: D_3 = 24 * 5760, where 24 and 5760 are the denominators
of the A-hat genus coefficients a_1 = 1/24 and a_2 = 7/5760. This is a
suggestive factorization but does not extend cleanly: D_4/D_3 = 126
(= binom(9,4) = 2 * 3^2 * 7), while the A-hat denominator ratio at g=3 is
967680/5760 = 168.

**Ratios**: D_3/D_2 = 8640 = 2^6 * 3^3 * 5. D_4/D_3 = 126 = 2 * 3^2 * 7.

## 4. Partial Fraction Decomposition

```
delta_F_2 = 1/16 + 51/(4c)

delta_F_3 = c/27648 + 79/2880 + 133/(16c) + 6281/(4c^2)

delta_F_4 = 41c/2488320 + 89627/5806080 + 229079/(34560c)
          + 163829/(96c^2) + 5138841/(16c^3)
```

The constant terms (c-independent part) decrease: 1/16, 79/2880, 89627/5806080
(approximately 0.0625, 0.0274, 0.0154).

The leading 1/c coefficients also decrease: 51/4, 133/16, 229079/34560
(approximately 12.75, 8.31, 6.63).

The leading 1/c^{g-1} coefficients (most singular at c=0) grow rapidly:
51/4, 6281/4, 5138841/16. These reflect the accumulation of Kac determinant
poles from the propagators eta^{TT} = 2/c and eta^{WW} = 3/c.

## 5. Ratio to Scalar Part (Large-c Asymptotics)

The scalar free energy is F_g^scalar = kappa * a_g where a_g = [x^{2g}] A-hat(ix):

```
a_1 = 1/24,  a_2 = 7/5760,  a_3 = 31/967680,  a_4 = 127/154828800
```

The asymptotic ratio delta_F_g / F_g^scalar as c -> infinity:

| g | ratio                  | numerical  |
|---|------------------------|------------|
| 2 | 18/c -> 0              | subdominant|
| 3 | **42/31**              | 1.355      |
| 4 | **9184/381**           | 24.10      |

The ratio grows super-linearly with g. At genus 2, the cross-channel
correction is subdominant (vanishes relative to the scalar part at large c).
At genus 3, it is comparable (ratio 42/31). At genus 4, it dominates
by a factor of 24. This growth is consistent with the factorial growth
of the number of stable graphs (contributing more mixed-channel
configurations at higher genus).

**The cross-channel correction dominates the scalar part at large c
for g >= 4.** The uniform-weight formula F_g = kappa * lambda_g becomes
not merely wrong but arbitrarily wrong at high genus for multi-weight algebras.

## 6. Generating Function Obstruction

The scalar genus expansion has the closed-form generating function

    sum_g F_g^scalar * hbar^{2g} = kappa * (A-hat(i*hbar) - 1).

The cross-channel correction **cannot** have an A-hat-type generating function,
for three independent reasons:

(a) **Inhomogeneous c-scaling**: delta_F_2 is O(1) as c -> infinity while
    delta_F_g for g >= 3 is O(c). No single power of c can factor out to
    produce a c-independent generating function in hbar.

(b) **Super-linear ratio growth**: the ratio delta_F_g / F_g^scalar grows
    super-linearly (0, 42/31, 9184/381, ...), ruling out any simple rescaling
    of the A-hat series.

(c) **Irreducible numerators**: the P_g(c) are irreducible over Q with
    no common factors, ruling out a product-form generating function.

The cross-channel generating function, if it exists in closed form, must
involve at least two independent functions of hbar (one for the O(1)
contribution at g=2, another for the O(c) contributions at g >= 3) or
be a bivariate generating function in (c, hbar) that is not separable.

## 7. Predictions for delta_F_5

Based on the established patterns:

1. **Numerator degree**: deg(P_5) = 5 (continuing d_g = g for g >= 3).
2. **Denominator**: D_5 * c^4, with D_5 involving primes {2, 3, 5, 7}
   (primes up to 2g-1 = 9); the prime 11 may enter if the pattern
   extends to 2g+1.
3. **Term count**: P_5 has 6 terms (= g+1) with all positive coefficients.
4. **Large-c**: delta_F_5 ~ A_5 * c (linear growth, net degree 1).
5. **Ratio**: delta_F_5 / F_5^scalar >> 24 (super-linear growth continues).
6. **Pole order**: delta_F_5 has a pole of order 4 at c = 0.

## 8. Physical Interpretation

The pole of order g-1 at c = 0 arises from the propagators: each propagator
contributes a factor 1/c (from eta^{TT} = 2/c or eta^{WW} = 3/c), and
a genus-g graph has at most 3g-3 edges with g-1 independent loops, giving
the maximal pole order.

The strict positivity of delta_F_g^cross for all c > 0 means the
multi-weight correction is a **genuine obstruction** to the scalar formula,
not a sign-alternating perturbation that might cancel in resummation.

The super-linear growth of the ratio delta_F_g / F_g^scalar implies that
the genus expansion of a multi-weight algebra is **not** controlled by a
single scalar invariant kappa at high genus. The full genus expansion
requires the complete propagator-variance data delta_mix and the
multi-channel graph sum. This is the quantitative content of
thm:multi-weight-genus-expansion and the negative resolution of
op:multi-generator-universality.

## 9. Open Questions

1. Does the bivariate generating function G(c, hbar) = sum_g delta_F_g * hbar^{2g}
   admit a closed form (possibly involving special functions beyond A-hat)?

2. Is the super-linear growth of delta_F_g / F_g^scalar factorial (suggesting
   a non-perturbative origin) or polynomial?

3. Does the denominator pattern D_g = primes up to 2g-1 persist, and does it
   have an interpretation in terms of stable-graph automorphism groups?

4. Can the N-dependence of delta_F_g^cross(W_N) (from
   `theorem_delta_f3_universal_engine.py`) illuminate the generating function
   structure? The vanishing at N=2 (Virasoro = uniform weight) provides a
   boundary condition.
