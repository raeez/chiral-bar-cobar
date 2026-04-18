# Wave-4 attack+heal — CB_{2,2}(k) = 2k(k+1)(k+2)/3

Date: 2026-04-18
Target: CLAUDE.md "Genus-2 degree decomp" row; `prop:g2-conformal-block-degree`
  in `chapters/theory/higher_genus_modular_koszul.tex:34655-34697`.

## Attack ledger (Beilinson auditor, ten voices)

A1. **Phantom check (AP255).** `\label{prop:g2-conformal-block-degree}` at
  `higher_genus_modular_koszul.tex:34656` is inscribed as a bona fide
  `\begin{proposition}` with full `\begin{proof}` body at :34681-34697.
  `metadata/claims.jsonl:2577` registers the label as ProvedHere.
  Registered in `theorem_index.tex:992`. NOT phantom. NOT phantomsection-masked.
  No AP286 (tactical alias) either — the label binds to the real proposition.

A2. **Convention (sl_2 Dynkin).** Proof body uses Dynkin labels:
  `V ⊗ V = V_0 ⊕ V_2`, fusion `N_{1,1}^0 = N_{1,1}^2 = 1`. Consistent with
  spin-1/2 defining rep and the singlet/triplet Clebsch-Gordan decomposition
  (`V_0` antisymmetric singlet, `V_2` symmetric triplet) standard across
  Vol I compute/ layer and chapters/examples/yangians_drinfeld_kohno.tex.

A3. **Integrability at k=1 (singlet-only).** Dynkin-label integrability for
  sl_2 level k: `λ ≤ k`. At k=1: V_0 (λ=0) integrable; V_2 (λ=2) NOT
  integrable (2 > 1). Statement (ii) in the proposition asserts this
  correctly. Cross-check: Verlinde g=2, n=0 with vacuum at k=1 = 4 (computed
  `(3/2)[csc²(π/3) + csc²(2π/3)] = 4`); matches CB_{2,2}(1).

A4. **Singlet + triplet at k ≥ 2.** At k=2, both channels contribute:
  singlet gives 10 (Verlinde g=2, n=0 vacuum at k=2), triplet gives 6
  (genus-2 one-point insertion of V_2). Total 16 = CB_{2,2}(2). ✓

A5. **AP259 tautology test.** Is CB_{2,2}(k) DEFINED as the cubic, or
  DERIVED? Proof body derives via Verlinde trace
  `CB_{2,1}(j) = Σ_m (S_{jm}/S_{0m})^{-2}` followed by cotangent-squared
  reduction. Wave-7 `wave7_wN_stokes_g2_decomp_attack_heal.md:103-135`
  reproduces the derivation end-to-end: Verlinde → cot²(πℓ/(k+2)) sum →
  classical identity `Σ_{ℓ=1}^{N-1} cot²(πℓ/N) = (N-1)(N-2)/3` with N=k+2
  → 2(k+2)·k(k+1)/3. Definitional-tautology status: REJECTED.

A6. **Falsification at k=2.** CB_{2,2}(2) = 2·2·3·4/3 = 16. Independent
  Verlinde computation via the S-matrix at level 2: singlet 10 + triplet 6
  = 16. Agreement; the cubic is a GENUINE derivation, not a curve fit.

A7. **Polynomial degree 3g-3+n = 3 at g=2, n=2.** Virasoro-Verlinde
  general structure: dim of conformal-block space is polynomial in k of
  degree 3g-3+n for sl_2. g=2, n=2 gives 3. Cubic in k. ✓ Structural.

A8. **Verlinde-vs-shadow distinction (ordered vs Verlinde).** CB_{2,2}(k)
  is the Verlinde integrable-truncation at level k; `dim H^1 = 12` at
  `prop:g2-degree2` is the generic Euler-characteristic count at generic ℏ
  (Euler characteristic `4·(-3) = -12`, all in H^1). Remark `rem:h1-comparison`
  at :34622 frames the relationship. Wave-7 verlinde note flags that
  Z_2 (pure partition function) ≠ CB_{2,2}(k) — they are different objects;
  CB counts blocks with two fundamental insertions, Z_2 is vacuum. Internal
  consistency HOLDS via the "ordered generic ℏ = 12" vs "integrable k = cubic"
  remark pair.

A9. **HZ-IV decorator.** Test `compute/tests/test_genus_2_ddybe_platonic.py:305`
  carries the identity with commentary. Hilbert-level check at k=1,2,3 present.
  No HZ-IV W8-B primitive-tautology flag needed (AP287): there is genuine
  numerical content at every k.

A10. **Prose residue.** Wave-7 asked for one prose heal: rename "one-point"
  → "zero-point block count in channel j". Current proof body at
  `higher_genus_modular_koszul.tex:34687-34691` reads
  "the genus-2 zero-point conformal block count in channel j after fusion
  of the two fundamentals (the exponent -2 = -(2g-2+n) at g=2, n=0)".
  That heal HAS been inscribed. Nothing further to rename.

## Surviving core (Drinfeld voice)

Genus-2 degree-2 integrable conformal blocks for sl_2 at level k decompose
along Clebsch-Gordan: singlet V_0 (always integrable) and triplet V_2
(integrable iff k ≥ 2). The total count is a cubic `CB_{2,2}(k) =
2k(k+1)(k+2)/3`, derived by channel-sum `CB_{2,2}(k) = Σ_j N_{1,1}^j
Σ_m (S_{jm}/S_{0m})^{-2}` and reduction via the classical cotangent-squared
identity. The falsification test at k=2 — independent Verlinde gives 10+6=16,
cubic gives 16 — passes; the formula is a derivation, not a definition.

## Per-finding heal

| # | Finding | Status |
|---|---------|--------|
| A1 | Label live, proof body present | ACCEPT |
| A2 | Dynkin convention consistent | ACCEPT |
| A3 | k=1 singlet-only correctly stated | ACCEPT |
| A4 | k=2 singlet+triplet split 10+6=16 | ACCEPT |
| A5 | Derivation not definitional | ACCEPT (AP259-clear) |
| A6 | k=2 Verlinde falsification test passes | ACCEPT |
| A7 | Polynomial degree 3g-3+n=3 structural | ACCEPT |
| A8 | Verlinde-vs-shadow distinction correct | ACCEPT |
| A9 | HZ-IV test at k∈{1,2,3} inscribed | ACCEPT |
| A10 | "one-point" → "zero-point" prose heal | ALREADY INSCRIBED |

**Verdict: proposition stands. No edits required. CLAUDE.md row accurate as written.**

## Commit plan

None. The proposition and its proof body are already healed to wave-7
standard; the current session is a ratification audit confirming stability.
No code, tex, or metadata changes.

## Cache entries (reinforced)

- Pattern 223 (wave-7): cotangent-squared reduction
  `Σ_{ℓ=1}^{N-1} cot²(πℓ/N) = (N-1)(N-2)/3` is the load-bearing identity
  behind the cubic; generic structure is polynomial of degree 3g-3+n.
- Pattern 224 (wave-7): "zero-point block count in channel j" is the
  correct prose; "one-point" is the incorrect label that wave-7 healed.
- New: **Verlinde-vs-shadow internal consistency at g=2.** CB_{2,2}(k)
  (integrable, cubic) and `dim H^1 = 12` (generic ℏ, Euler-characteristic)
  count DIFFERENT objects on the same surface; the integrability truncation
  is a level-dependent cut of the ordered shadow. No contradiction between
  "CB_{2,2}(2) = 16" and "Z_2(k=2) = 10" — Z_2 is vacuum, CB has two
  fundamental insertions.
