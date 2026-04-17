# Attack-heal: Z_g closed forms + Bernoulli-Kummer arithmetic duality

Date: 2026-04-18. Auditor: Raeez Lorgat. AP block: AP1021-AP1040.

## Scope

Adversarial audit of:

- `chapters/theory/z_g_kummer_bernoulli_platonic.tex` (747 lines)
- `chapters/theory/shadow_tower_higher_coefficients.tex` (4016 lines, Kummer-absent theorem at line 2435)
- `CLAUDE.md` row: "Z_g closed forms: DISCOVERED g=0..9; PROVED all g via Hurwitz-Bernoulli; arithmetic duality at leading Kummer-irregular primes {691, 3617} PROVED through r=11."

Target theorems audited:

- `thm:z-g-leading-coefficient-bernoulli` (Hurwitz-Bernoulli leading coefficient)
- `thm:z-g-kummer-congruence` (irregular-prime witnesses)
- `thm:z-g-s-r-arithmetic-duality` (presence on Z_g, absence on S_r through r=11)
- `thm:s-r-kummer-absent-through-r-11` (the Kummer-absent theorem, shadow_tower_higher_coefficients.tex)

## Verified positive findings (primary-source arithmetic, pure-Python)

1. **Bernoulli numerators confirmed.** Via Akiyama-Tanigawa computation and
   cross-checked against the Bernoulli recurrence
   $\sum_{k=0}^{n} \binom{n+1}{k} B_k = 0$:

   B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, B_8 = -1/30, B_10 = 5/66,
   **B_12 = -691/2730**, B_14 = 7/6, **B_16 = -3617/510**,
   B_18 = 43867/798, B_20 = -174611/330 = -(283 · 617)/330.

   691, 3617, 43867, 283, 617 all verified prime by trial division.

2. **Kummer witness structure confirmed.**
   - num(B_12) = -691. 691 is prime. 691 > 2m = 12 and 12 ≤ 691 - 3, so
     m = 6 is a valid Kummer witness.  Hence **691 is Kummer-irregular** via the
     B_12 witness.
   - num(B_16) = -3617. 3617 is prime. 16 ≤ 3617 - 3, so m = 8 is a valid
     Kummer witness.  Hence **3617 is Kummer-irregular** via the B_16 witness.

3. **Prefactor c_g = 2^{g-1}(g-1)! / (2g-2)! verified.**

   g=2: c = 1
   g=3: c = 1/3
   g=4: c = 1/15
   g=5: c = 1/105
   g=6: c = 1/945
   g=7: c = 1/10395 = 1/(3^3 · 5 · 7 · 11)
   g=8: c = 1/135135
   **g=9: c = 1/2027025 = 1/(3^4 · 5^2 · 7 · 11 · 13)**

   Chapter's explicit c_9 = 1/2027025 at `z_g_kummer_bernoulli_platonic.tex:386`
   is correct to machine precision.  The denominator factorisation claimed
   (3^4 · 5^2 · 7 · 11 · 13 = 2027025) is exact.

   For every g in {2,...,9}, the reduced numerator of c_g is 1; hence c_g's
   numerator is trivially coprime to 691 and 3617.  The Kummer witnesses at
   g = 7, 9 survive the boxed-form normalisation because c_g's numerator
   contributes no large primes.

4. **N_r coefficient arithmetic through r = 11 verified.** Raw coefficients:

       N_4  = 10
       N_5  = -48
       N_6  = 80 (45 c + 193) / 3
       N_7  = -2880 (15 c + 61) / 7
       N_8  = 80 (2025 c^2 + 16470 c + 33314)
       N_9  = -1280 (2025 c^2 + 15570 c + 29554) / 3
       N_10 = 256 (91125 c^3 + 1050975 c^2 + 3989790 c + 4969967)
       N_11 = -15360 (91125 c^3 + 990225 c^2 + 3500190 c + 3988097) / 11

   Direct divisibility check: 691 and 3617 divide no coefficient of these raw
   polynomials.  The main theorem `thm:s-r-kummer-absent-through-r-11` holds.

5. **Primality/factorisation of the P_{<=11} characteristic-prime witnesses.**
   Verified primes by trial division:

       61, 163 [not checked], 173 [not checked], 193, 2111, 16657,
       38891, 292351, 3988097.

   Explicit factorisations:

       29554 = 2 · 7 · 2111       (constant of N_9)    [verified]
       15570 = 2 · 3^2 · 5 · 173  (c^1 of N_9)         [verified]
       33314 = 2 · 16657          (constant of N_8)    [verified]
       4969967 = 17 · 292351      (constant of N_10)   [verified; 292351 prime]
       3988097 prime              (constant of N_11)   [verified: trial division through 1997]
       91125 = 3^6 · 5^3          [verified]
       1050975 = 3^5 · 5^2 · 173  [verified]
       2025 = 3^4 · 5^2           [verified]

## Discrepancies found

### F1 (AP1021, display-arithmetic slip in factor table, LOW SEVERITY).

Location: `chapters/theory/shadow_tower_higher_coefficients.tex:2530`.

Claimed: `3500190 = 2 · 3 · 5 · 7 · 79 · 211`.

Actual: `2 · 3 · 5 · 7 · 79 · 211 = 3500490` (off by 300).

The correct factorisation is `3500190 = 2 · 3^2 · 5 · 38891` with
**38891 prime** (verified by trial division; sqrt(38891) < 198, no divisor
found).  The prime 38891 is already in the chapter's stated `P_{\le 11}` list at
line 2507, so this is purely a **display-arithmetic transcription error** in the
prose factor table, not a logical failure of the theorem.

Impact: the conclusion "691, 3617 are absent from P_{\le 11}" is unaffected;
38891 was already accounted for in the prime set.

Heal recommendation (deferred for user sign-off, no commits this session):

Replace line 2530 from

    3500190 &= 2 \cdot 3 \cdot 5 \cdot 7 \cdot 79 \cdot 211
             \text{ (appears in } N_{11}).

to

    3500190 &= 2 \cdot 3^{2} \cdot 5 \cdot 38891
             \text{ (appears in } N_{11}).

The new witness 38891 is already in `P_{\le 11}` (line 2507).  The stated
positive claim of `thm:s-r-kummer-absent-through-r-11` is unaffected.

### F2 (AP1022, AP313-adjacent rhetorical slip, LOW SEVERITY).

Location: `chapters/theory/z_g_kummer_bernoulli_platonic.tex:373-376`.

The proof of `thm:z-g-kummer-congruence` states:

> "the prefactor $c_g = 2^{g-1}(g-1)!/(2g-2)!$ has
>  $c_7 = 64 \cdot 720 / 12! = 46080/479001600$, whose numerator
>  $46080 = 2^{10}\cdot 45$ is coprime to $691$"

Computed: `c_7 = 46080 / 479001600 = 1/10395` (fully reduced).  The expression
`46080/479001600` is the un-reduced form; once reduced, numerator = 1 trivially
coprime to 691.  The factorisation `46080 = 2^{10} · 45` is arithmetically
correct (1024 · 45 = 46080 and 46080 = 2^10 · 3^2 · 5), and the final
conclusion "coprime to 691" is also correct.

Impact: zero on correctness of the divisibility argument.  Rhetorical polish
only.

Heal recommendation (optional): swap the un-reduced form for the reduced form
to avoid future reader confusion: `c_7 = 1/10395 = 1/(3^3 \cdot 5 \cdot 7 \cdot 11)`,
manifestly coprime to 691.

### F3 (AP1023, AP313 structural, already self-disclosed).

Location: `chapters/theory/z_g_kummer_bernoulli_platonic.tex:289-306`.

The proof of `thm:z-g-leading-coefficient-bernoulli` self-declares the
normalisation absorption explicitly:

> "The cleanest invariant statement, independent of normalisation choice, is
>  that [boxed: [n^{2(g-2)}] R_{g-2}(n^2) = B_{2g-2}/(g-1)] in the convention
>  of (4.x) after absorbing the universal prefactor $2^{g-1}(g-1)!/(2g-2)!$
>  into the definition of $R_{g-2}$."

This is the exact AP313 structural pattern:

- RAW Hurwitz identity: `[n^{2(g-2)}] R_{g-2}(n^2)_raw = 2^{g-1}|B_{2g-2}|/(2g-2)!`
- BOXED identity: `[n^{2(g-2)}] R_{g-2}(n^2) = B_{2g-2}/(g-1)`
- Related by the universal prefactor c_g = 2^{g-1}(g-1)!/(2g-2)!
  absorbed into the definition of R_{g-2}.

The chapter honestly discloses the absorption; the Kummer witnesses survive
because c_g's reduced numerator is 1 for g in {2,...,9}, trivially coprime to
any large prime.  Hence AP313 is surfaced but **does not invalidate the
Kummer-divisibility claim** at g = 7, 9.

**Impact on theorem status.** The Z_g leading coefficient "equals B_{2g-2}/(g-1)"
identity is a NORMALISATION CHOICE, not a derived identity.  The RAW Hurwitz
asymptotic is the derived identity, and the boxed form is obtained by
definitionally absorbing c_g.  The theorem-status row in CLAUDE.md should be
qualified to this effect; currently it reads "PROVED all g via
Hurwitz-Bernoulli" without noting that the boxed form is convention-dependent.

Heal recommendation (deferred; no commits this session):

Extend the `thm:z-g-leading-coefficient-bernoulli` statement OR immediate
remark with an explicit scope note:

> "Equation (leading-coeff) is the boxed form after absorbing the universal
>  prefactor c_g = 2^{g-1}(g-1)!/(2g-2)! into the definition of R_{g-2}.  The
>  raw Hurwitz asymptotic is [n^{2(g-2)}] R_{g-2}(n^2)_raw =
>  2^{g-1}|B_{2g-2}|/(2g-2)!.  Every Kummer-divisibility witness in this chapter
>  holds in both normalisations because c_g has reduced numerator 1 for
>  g in {2,...,9}."

Propose CLAUDE.md status-row addition: "(boxed-form identity; absorbs universal
prefactor c_g = 2^{g-1}(g-1)!/(2g-2)! into R_{g-2})."

### F4 (AP1024, cross-check vs CLAUDE.md B92, NO DISCREPANCY).

CLAUDE.md B92 says 2111 is Kummer-regular through B_418 and
"full confirmation via Buhler-Harvey 2011".  Chapter at line 2450 says 2111 is
Kummer-irregular via `2111 | num(B_{1038})`.  These are consistent: 2111 is
indeed Kummer-irregular (the witness Bernoulli index is 2m = 1038, far beyond
B_418), and regular through B_418.  No discrepancy.  CLAUDE.md B92 should
perhaps be clarified:

> "2111 is Kummer-REGULAR through B_{418}; its first Kummer-irregular witness
>  is at B_{1038} per the Buhler-Harvey 2011 table."

But since CLAUDE.md B92 already says "verified regular through B_418 with
full confirmation via Buhler-Harvey 2011", and Buhler-Harvey's table lists
the first witness at 2m=1038, this is consistent by reading.

## Verdict

- `thm:z-g-kummer-congruence` (691 | Z_7 leading, 3617 | Z_9 leading):
  **STANDS** as proved in boxed normalisation.  AP313 absorption self-disclosed.

- `thm:s-r-kummer-absent-through-r-11` (absence through r=11):
  **STANDS** as proved.  One display-arithmetic slip at 3500190 factorisation
  (does not touch main conclusion).

- `thm:z-g-s-r-arithmetic-duality` (present on Z_g / absent on S_r):
  **STANDS** as proved, with the caveat that the boxed "B_{2g-2}/(g-1)"
  identification is convention-dependent (absorbs c_g into R_{g-2}).

- CLAUDE.md row "Z_g closed forms PROVED all g via Hurwitz-Bernoulli":
  status correct but minor scope qualifier recommended ("boxed form; absorbs
  universal prefactor c_g = 2^{g-1}(g-1)!/(2g-2)! into R_{g-2}").

## Proposed heals (deferred; no commits this session per AP316)

Three micro-heals, all in-file or in-CLAUDE.md, none touching theorem proofs:

1. `shadow_tower_higher_coefficients.tex:2530`: fix `3500190 = 2 \cdot 3 \cdot
   5 \cdot 7 \cdot 79 \cdot 211` -> `3500190 = 2 \cdot 3^{2} \cdot 5 \cdot
   38891` (AP1021).

2. `z_g_kummer_bernoulli_platonic.tex:373-376`: optionally simplify the
   `c_7 = 46080/479001600` display to its reduced form `c_7 = 1/10395
   = 1/(3^3 \cdot 5 \cdot 7 \cdot 11)` for clarity (AP1022).

3. `z_g_kummer_bernoulli_platonic.tex:208-221` and CLAUDE.md theorem-status
   row: append explicit AP313 scope qualifier acknowledging that the boxed
   identity absorbs the universal prefactor c_g (AP1023).  The chapter's
   Step 5 already admits this at :298-306; the heal is to hoist that
   admission into the theorem statement or immediate remark rather than
   burying it at the end of the proof.

## AP inscription register

- **AP1021**: display-arithmetic factor-table slip.  `a \cdot b \cdot c \cdot
  d \cdot e` claimed equal to target N, but `product != N`.  Counter: after
  any prose factorisation `N = p_1 \cdot p_2 \cdot ... \cdot p_k`, run
  `prod(p_i) == N` numerically; any mismatch = rewrite table.  Prevention:
  mandatory arithmetic sanity check for every explicit prime-factor display,
  regardless of whether the final prime set is already validated elsewhere.
  Related: AP245 (statement-proof-engine numerical agreement), AP292
  (operator-precedence arithmetic bug).

- **AP1022**: unreduced-fraction-in-prose numerator claim.  A prose claim
  about "the numerator of c_g" refers to the un-reduced form in some display
  conventions but to the reduced form in arithmetic reality.  Counter: every
  claim about a fraction's numerator/denominator must be made on the
  canonical reduced form.  Prevention: before writing "numerator N is coprime
  to p", reduce the fraction first and verify on the reduced numerator.

- **AP1023 (primary finding)**: AP313 applied to Z_g leading coefficient.
  Boxed identity "[n^{2(g-2)}] R_{g-2}(n^2) = B_{2g-2}/(g-1)" is obtained by
  definitionally absorbing the universal prefactor c_g = 2^{g-1}(g-1)!/(2g-2)!
  into the definition of R_{g-2}.  Raw Hurwitz identity is
  [n^{2(g-2)}] R_{g-2}(n^2)_raw = 2^{g-1}|B_{2g-2}|/(2g-2)!.  Both are
  mathematically valid; the boxed form is a convention.  The Kummer
  witnesses at g = 7, 9 survive because c_g's reduced numerator is 1 for
  g in {2,...,9} (trivially coprime to 691, 3617).  Honest inscription of
  the boxed-vs-raw distinction in the theorem statement recommended.

## Summary

All three backbone theorems on Z_g / S_r arithmetic duality STAND at their
stated scope.  One display-arithmetic typo (F1 / AP1021) to correct; two
rhetorical polish items (F2 / AP1022 and F3 / AP1023) for optional heal.  No
theorem requires downgrade.  The Kummer-irregularity witnesses 691 | Z_7 and
3617 | Z_9 are verified independently from first principles (Bernoulli
recurrence + Fraction arithmetic + trial division).

No commits made in this session; delivery is report-only per AP316.
