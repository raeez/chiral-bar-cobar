# Wave-10 Anchor A vs Anchor B Adjudication

**Date**: 2026-04-18
**Scope**: Vol III constitutional contradiction on κ_ch(CY products), specifically κ_ch(K3 × E).
**Mode**: Diagnostic + proposal only. No edits.

## 1. Per-anchor statement + scope

### Anchor A — `thm:kappa-hodge-supertrace-identification`
Location: `cy_d_kappa_stratification.tex` (referenced from :408, stated earlier in the chapter and applied at :448-452).
Content: For compact CY_d, κ_ch(A_X) = Ξ(X) := Σ_q (-1)^q h^{0,q}(X). The proof at :477-492 uses **Künneth-multiplicativity of Ξ**: "Ξ(X × Y) = Ξ(X) · Ξ(Y)". Applied to K3 × E: Ξ(K3) = 2, Ξ(E) = 0, so κ_ch(A_{K3×E}) = 2 · 0 = **0**.
Status: `\ClaimStatusProvedHere`. Scope: **compact** CY_d via the standard Φ_d correspondence.

### Anchor B — `prop:beauville-kappa-formula`
Location: `cy_to_chiral.tex:293-343`.
Content: For compact CY_3,
κ_ch(X) = χ_top(X)/24 + [h^{1,0}(X) > 0] · (h^{3,0}(X) + 2).
Product branch proof (:333-336) explicitly invokes **Theorem D (Vol I) additivity under tensor products**: "κ_ch(K3 × E) = χ(O_{K3}) + h^{1,0}(E) = 2 + 1 = **3**".
Status: `\ClaimStatusProvedHere` (product branch).
Companion `rem:cy-kappa-evidence` (:273-290): explicitly names the clash — "κ_ch additive under products … χ(O_X) multiplicative under products … clash at K3 × E".
Companion `conj:cy-kappa-identification` (:262-271): states κ_ch(K3×E) = 3, κ_ch(quintic) = −25/3, and that κ_ch ≠ χ(O_X) at d ≠ 2.

## 2. Mathematical verification

**Anchor A (Hodge supertrace Künneth).** Ξ(X) = χ(O_X) = Σ_q (-1)^q h^{0,q}(X) = Σ_q (-1)^q dim H^q(X, O_X). Künneth for coherent sheaf cohomology gives H^•(X × Y, O_{X×Y}) = H^•(X, O_X) ⊗ H^•(Y, O_Y), so χ(O_{X×Y}) = χ(O_X) · χ(O_Y). This is **textbook Hirzebruch–Riemann–Roch** / Künneth. Ξ is Künneth-**multiplicative**, unambiguously. For K3 × E: χ(O_{K3}) · χ(O_E) = 2 · 0 = 0. The identification κ_ch = Ξ at all compact CY_d is the Anchor-A claim; it is a nontrivial identification, not a definition.

**Anchor B (Beauville / Beauville–Bogomolov).** The Beauville–Bogomolov decomposition classifies compact Kähler with c_1 = 0 into irreducible factors (abelian, K3/hyperkähler, strict CY). This structural theorem is unambiguous. What is **not** universally true is the additivity `κ_ch(A_{X×Y}) = κ_ch(A_X) + κ_ch(A_Y)`: this is a chiral-algebra claim that depends on which κ_ch is meant. For the **Heisenberg-level chiral de Rham** / free-boson quantization — where Ω^ch(X × Y) ≃ Ω^ch(X) ⊗ Ω^ch(Y) as factorization algebras and κ_ch is the Heisenberg level parameter summed over free-boson factors — additivity is the correct behavior. This matches the Vol I Heisenberg identification κ_Heis(H_k) = k, for which E contributes κ = 1 and K3 contributes κ = 2 by rank counting of holomorphic (p,0)-forms.

**Conclusion.** There is no arithmetic error in either computation. The clash is a **symbol collision on two genuinely distinct invariants**: Ξ (Hodge supertrace / holomorphic Euler characteristic of the CY category) and κ_Heis-sum (sum of Heisenberg levels in the chiral de Rham / free-boson presentation). The manuscript's `rem:cy-kappa-evidence` already names this clash but does not resolve it.

## 3. Contradiction classification

**(ii) — Different objects under same symbol.** Standard AP234 pattern (same letter, two distinct invariants). This is the **same failure mode** the Wave-6 κ(K3 × E) retraction campaign previously identified and declined to patch. Anchor A's Ξ is the Hodge / CY-category invariant; Anchor B's Beauville formula computes the chiral-de-Rham / free-boson scalar. At d = 2 they happen to coincide (prop:cy-kappa-d2); at d ≠ 2 they diverge, which is precisely the content of `rem:cy-kappa-evidence`.

Not (i) (neither is wrong within its own scope). Not (iii) (the hypotheses overlap fully — both cover compact CY_3 — so scope-restriction alone will not resolve).

## 4. H1-H4 analysis

- **H1 (A wins, retract B).** Mathematically unjustified: the Heisenberg-level additive invariant is a real, inscribed Vol I quantity and the Beauville-decomposition computation of it is correct. Retracting Anchor B would delete a valid theorem.

- **H2 (B wins, retract A).** Mathematically impossible: Ξ Künneth-multiplicativity is Hirzebruch–RR Künneth, a theorem of 1950s algebraic geometry. Cannot be retracted.

- **H3 (Two-subscript split).** Rename Anchor A's invariant as κ_ch^{Hodge} or κ_cat (it IS χ(O_X) = Ξ for compact CY_d where the HKR + Mukai identification applies — this is already what `rem:cy-kappa-evidence` inline-identifies as `κ_cat`). Rename Anchor B's invariant as κ_ch^{Heis} or κ_ch^{free-boson}. Both anchors stand, operating on disjoint symbols. Matches Wave-6 Route A/B framing. **Most honest; zero mathematics retracted.**

- **H4 (Scope-restrict Anchor B to indecomposable CY).** Would force Anchor B's scope to SU(d)-holonomy strict CY_d and delete the product-branch entries (K3 × E, Enr × E, T^6). But the product-branch entries are the **most concrete** and most-tested of Anchor B's content (65 tests in `kappa_ch_universal_formula.py`), and deleting them abandons the free-boson additivity that Vol I uses. **Mathematically possible but programme-destructive.**

## 5. Recommendation — **H3**

Adopt H3: **rename one of the two invariants**. The symbol `κ_ch` in Vol III should canonically denote the Hodge supertrace Ξ = χ(O_X) (Anchor A) — this aligns with `thm:kappa-hodge-supertrace-identification`, `thm:kappa-stratification-by-d`, the HKR + Mukai + HC^-_d trace construction, and the `κ_cat` inline identification in `rem:cy-kappa-evidence` at :252. The Beauville-formula invariant should be renamed, since it is not the Hodge supertrace but the Heisenberg-level sum / chiral-de-Rham scalar.

### Draft re-statement of Anchor B (rename, not retract)

Replace `prop:beauville-kappa-formula` header and body occurrences of `κ_ch` with `κ_ch^{Heis}` (or `κ_Heis-sum`). Add opening remark:

> **Notational convention (local to this proposition).** Write κ_ch^{Heis}(X) for the Heisenberg-level sum of the chiral de Rham / free-boson presentation of Φ_d(D^b(X)), i.e., the sum of Heisenberg levels over the free-boson factors in the Beauville–Bogomolov decomposition. This is a DIFFERENT invariant from the Hodge supertrace κ_ch = Ξ of Theorem `thm:kappa-hodge-supertrace-identification`; the two agree at d = 2 for K3 but diverge on products involving d = 1 factors. The identity `rem:cy-kappa-evidence` names ("additive vs multiplicative") is precisely the discrepancy κ_ch^{Heis}(K3 × E) = 3 ≠ 0 = κ_ch(K3 × E).

### Required propagations (H3 consequences)

- ~35 Route-B sites (quoting "κ_ch(K3 × E) = 3", "additivity under products", "Beauville formula") rename `κ_ch → κ_ch^{Heis}` atomically.
- ~5 Route-A sites (quoting "κ_ch(K3 × E) = 0", "Hodge supertrace Künneth") stay as-is.
- `rem:cy-kappa-evidence` rewritten: the two invariants are *distinct*, not in tension; additivity holds for κ_ch^{Heis}, multiplicativity for κ_ch = Ξ; the label `δκ_ch := κ_ch − χ(O_X)` becomes `κ_ch^{Heis} − κ_ch` with clean closed forms per dimension.
- `conj:cy-kappa-identification` rewritten: the dimension-stratified formula is for `κ_ch^{Heis}`, not κ_ch; the `κ_ch(quintic) = −25/3` entry attaches to κ_ch^{Heis}.
- CLAUDE.md HZ-7 approved-subscript set {ch, cat, BKM, fiber} extends to include **Heis**; OR Beauville's invariant is renamed `κ_free` (if Heis subscript feels too narrow).
- New AP entry (post-AP292): **AP293 (κ_ch Hodge-vs-Heisenberg symbol collision)** — the Vol III symbol κ_ch without Hodge/Heis qualifier is ambiguous between Ξ and the Heisenberg-level sum; mandate the qualifier at every product-CY site.

### Why H3 over H4

H4 scope-restriction would delete working content (the product-branch Vol I bridge). H3 preserves every existing theorem and every existing test, at the cost of a one-pass rename of ~35 sites and a two-entry HZ-7 extension. Zero mathematical retraction; one notational clarification. Matches Wave-6's prior finding that Route-B sites are legitimate inscriptions, not drift.
