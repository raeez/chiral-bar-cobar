# Wave-15 attack-and-heal: CY_4 p_1-twisted family + K3×K3 N(X)=0 claim

Date: 2026-04-18.
Execution of the Wave-1 inscription plan (`wave1_cy4_p1_twisted_attack_heal.md`, 2026-04-18, 81 lines; marked NO COMMITS THIS RUN) plus a Phase-3(c) extension inscribing the Pontryagin-number stratification and a falsification-test pair beyond the sextic.

Mission scope (per parent brief): Vol I CLAUDE.md CY_4 row; Vol III `chapters/theory/cy_to_chiral.tex`; Vol III `chapters/theory/en_factorization.tex`; AP441–AP460 block. Path-typo in mission brief: `chapters/examples/cy_to_chiral.tex` does not exist; canonical home is `chapters/theory/cy_to_chiral.tex` (AP255-adjacent drift in the brief itself).

## 1. Phase-1 numerical verification (from first principles)

K3 surface (compact complex 2, real 4):
  c_1(T_K3) = 0; ∫_{K3} c_2(T_K3) = χ_top(K3) = 24.
  p_1(T_K3^R) = c_1^2 − 2 c_2 = −2 · c_2 (real Pontryagin sign convention).
  ∫_{K3} p_1(T_K3) = −2 · 24 = **−48**.
  (The `c_2 = 48` entry in `en_factorization.tex:308-310` uses the doubled convention χ(K3^[2]) / Kummer; both conventions agree on the Pontryagin NUMBER ∫p_1, and the engine `cy4_e2_tower.py:843-846` returns −48.)

K3 × K3 (compact complex 4, real 8):
  p_1(T_{K3×K3}) = π_1^* p_1(T_K3) + π_2^* p_1(T_K3)  (product of tangent bundles).
  p_1^2 = (π_1^* p_1)^2 + 2 π_1^* p_1 · π_2^* p_1 + (π_2^* p_1)^2.
  (π_i^* p_1)^2: π_i^* p_1 lives in H^4(K3_i) = H^top(K3_i); squared is in H^8(K3_i) = 0.
  Cross term: π_1^* p_1(K3) · π_2^* p_1(K3) ∈ H^4(K3_1) × H^4(K3_2) = H^8(K3×K3) = top.
  ∫_{K3×K3} p_1^2 = 2 · (−48) · (−48) = **4608 ≠ 0**.

**Conclusion**: N(K3×K3) = 4608. The CLAUDE.md memorial "K3×K3 N(X)=0" slogan is FALSIFIED. The actual inscribed table at `en_factorization.tex:308-310` correctly lists K3×K3 with p_1 = −96 and the Z-twisted column.

Sextic X_6 ⊂ P^5:
  Adjunction: c(T_{X_6}) = c(T_{P^5})/c(O(6)) expanded to c_2 = 15 H^2 ⇒ p_1 = −30 H^2.
  ∫ H^4 = deg(X_6) = 6.
  ∫_{X_6} p_1 = −30 · 6 = −180 (matches `cy_to_chiral.tex:4639`).
  N(X_6) = ∫ p_1^2 = 900 · 6 = **5400**.

Septic X_7 ⊂ P^6:
  Adjunction gives c_2 = 21 H^2 ⇒ p_1 = −42 H^2 (matches `cy_to_chiral.tex:4834`).
  ∫ H^4 = 7; ∫ p_1 = −42 · 7 = −294.
  N(X_7) = 1764 · 7 = **12348**.

N = 0 stratum of compact CY_4:
  (i) Abelian CY_4 C^4/Λ: flat tangent bundle, all Pontryagin classes vanish identically; N = 0.
  (ii) K3 × T^4: p_1(T^4) = 0 (flat); p_1(T_{K3×T^4}) = π_1^* p_1(K3) only; p_1^2 = 0 in H^8(K3) pulled back to H^8(K3×T^4)_{K3-direction} = 0. Hence N(K3 × T^4) = 0.

## 2. Attack ledger (extending Wave-1 F1–F10)

| # | file:line | category | severity | finding |
|---|-----------|----------|----------|---------|
| F11 | Vol I CLAUDE.md CY_4 row | AP271 + AP282 | HIGH | CLAUDE.md memorial continues to carry the K3×K3 N=0 slogan despite session-note retraction and manuscript/engine consensus on p_1(K3×K3) = −96. Reverse drift: the memorial is stale relative to the chapter text. |
| F12 | `cy_to_chiral.tex:4502-4700` | AP241 + scope-inflation | MEDIUM | The N(X) Pontryagin number and the N = 0 stratum of the CY_4 landscape (abelian, K3×T^4) are NOT inscribed in the chapter, even though the four-step Φ_4 construction's degeneration behaviour is structurally controlled by N(X). The chapter's `rem:cy4-deformation-space` tabulates `p_1` per family but does not compute `N = ∫ p_1^2` or identify the N = 0 stratum. |
| F13 | `conj:cy4-p1-family-associator-sextic` | AP276 (two-point extrapolation) | MEDIUM | Closed form verified at ONE non-product (sextic) and extrapolated to K3×E×E via V104 iteration-shadow. No inscribed falsification test beyond the sextic; per AP276, closed-form conjectures on ≤ 2 data points without a third-point or structural derivation stay programme-fragile. |
| F14 | `notes/session_20260417_master_synthesis.md:143-146` | AP288 (session-ledger stale narrative) | MEDIUM | The "K3 × K3 specialisation: N(X) = 0, unobstructed E_4" line survives a pre-heal narrative; inconsistent with manuscript. Needs dated retraction in place. |

## 3. Surviving core

The Φ_4 P^1-family construction (`constr:phi-4-p1-family`) stands: four explicit steps (HKR → HC^− → BCOV twist → E_1-chiral envelope), construction-level, functorial per fibre. The conjectural closed form for the iterated-product associator stands with scope tag `\ClaimStatusConjectured` and sextic verification. The negative structural assertion "no native CY_4 Yangian at generic compact CY_4 with [p_1] ≠ 0" stands as clause (iv) of `conj:cy4-twisted-center`, newly scoped to avoid the AP185 obstruction-group-vs-positive-structure conflation.

## 4. Heals executed this wave

(H1) **Vol III `chapters/theory/en_factorization.tex` clause (iv)** (line ≈297): rewrote to scope the non-existence to "generic compact CY_4 with nonvanishing p_1(T_X) ∈ H^4(X; Z)"; added explicit degeneration to the CY_3 untwisted case at flat points (C^4, abelian CY_4, K3 × T^4); distinguished obstruction GROUP π_4(BU) = Z from obstruction CLASS [p_1(T_X)] per AP185.

(H2) **Vol III `chapters/theory/cy_to_chiral.tex`**: inscribed `rem:cy4-pontryagin-number-stratum` after `ex:sextic-cy4-associator` with:
  - Definition N(X) := ∫_X p_1(T_X)^2.
  - Landscape table across 5 CY_4s: abelian (N=0), K3×T^4 (N=0), sextic (5400), K3×K3 (4608), septic (12348).
  - Explicit Künneth computation for the K3×K3 cross-term and the dimensional-vanishing of the diagonal squares.
  - Explicit retraction of the pre-inscription N(K3×K3) = 0 programme narrative.

(H3) **Vol III `chapters/theory/cy_to_chiral.tex`**: inscribed `rem:cy4-associator-falsification` giving the Wave-15 Phase-3(c) falsification test pair:
  - (T1) Septic X_7: predicts Δ_assoc = (7/6) V(τ) M^{corr} — non-integer 7/6 numerical prediction distinguishing α = 1/6 from alternatives.
  - (T2) K3 × K3 as product-CY_4: predicts Δ_assoc = 0 via κ^(4) = 0 on Mukai-polarised product; a nonzero measured associator at K3 × K3 would force a p_1^2 / N(X) correction term refining the closed form.

(H4) **Vol III `notes/session_20260417_master_synthesis.md:143-146`**: appended dated "RETRACTED 2026-04-18" annotation with pointer to this note and the computation N(K3×K3) = 4608.

## 5. Phase-5 propagation

Vol I CLAUDE.md CY_4 row updated text (proposed; commit-authored by Raeez Lorgat, no AI attribution, after build+test verification):

> | CY_4 p_1-twisted | CONSTRUCTED + CONJECTURED (Vol III `chapters/theory/cy_to_chiral.tex:4502-4760`, Φ_4 P^1-family + `conj:cy4-p1-family-associator-sextic` verified at sextic, 37 tests; Pontryagin number stratification `rem:cy4-pontryagin-number-stratum` inscribed 2026-04-18 Wave-15 heal; falsification test pair (septic, K3×K3) inscribed `rem:cy4-associator-falsification`); CONJECTURAL NEGATIVE (not "PROVED NEGATIVE"): clause (iv) of `conj:cy4-twisted-center` at `chapters/theory/en_factorization.tex:297` states that at generic compact CY_4 with nonvanishing [p_1(T_X)] ∈ H^4(X; Z) no native CY_4 Yangian exists, distinguishing the obstruction group π_4(BU) = Z from the obstruction class per AP185 | Pontryagin-number landscape: abelian CY_4 N = 0; K3 × T^4 N = 0; sextic N = 5400; K3 × K3 N = 4608 (retracted pre-inscription N = 0 slogan, session-note retraction 2026-04-18); septic N = 12348. 7d hCS realization neither inscribed nor typeset-cited in Vol III chapters; advertisement retired from the status row pending attribution (AP272). |

Grep sweep for downstream consumers of `\ref{conj:cy4-p1-family-associator-sextic}`, `\ref{conj:cy4-twisted-center}`, `p_1(K3×K3)`, and "N(X) = 0" in the manuscript — completed: the sole N(X)=0 site was the session note, now annotated. Zero other Vol III `.tex` sites. No Vol II sites.

## 6. AP register (AP441–AP460 block)

**AP441 (Pontryagin-number-zero stratum conflation).** An advertised "CY_X on the N = 0 stratum" claim without explicit Künneth verification of ∫ p_1^2. Dimensional vanishing of diagonal squares (π_i^* p_1^2 in H^{top+}(factor) = 0 when factor is below complex dim 4) does NOT imply the cross term vanishes. For K3 × K3 specifically: diagonal squares vanish, cross term 2 · (−48)^2 = 4608 survives. Counter: before labelling an n-fold product of CY_k with N = 0, compute the Künneth expansion of p_1(T)^2 and verify each surviving cross-product integrates to zero; on products of CY_2 factors the cross term is 2 (∫ p_1(CY_2))^2 modulo sign and is generically nonzero. Healed 2026-04-18 via `rem:cy4-pontryagin-number-stratum`.

**AP442 (Obstruction-group vs obstruction-class conflation at d = 4).** AP185 specialisation to the π_4(BU) = Z case: the non-existence of a "native CY_4 Yangian" stated as if consequence of π_4(BU) = Z alone is a category error. The nonvanishing of the OBSTRUCTION GROUP permits a nontrivial class; the assertion requires the nontrivial EVALUATION [p_1(T_X)] ≠ 0 on the specific manifold. Counter: every "π_n(BU) nontrivial ⇒ X fails positive structure" claim must include the scope "at generic X with nonvanishing obstruction class in H^n(X; Z)". Healed 2026-04-18 via `en_factorization.tex` clause (iv) rewrite.

**AP443 (Missing falsification test on a two-point closed form).** A closed-form conjecture verified at ≤ 2 data points without an inscribed next-point falsification test remains programme-fragile (AP276 recurrence). The Wave-15 heal added T1 (septic, non-integer 7/6 prediction) and T2 (K3 × K3, κ^(4) = 0 prediction); these become the commit-gate for any claimed "closed form for all compact CY_4". Counter: for every AP276-class conjecture, inscribe a `\begin{remark}[Falsification test]` environment with at least one non-verified parameter evaluation and a specific numerical prediction.

## 7. Build / test status

Pre-commit gate: (a) build verification pending; (b) test verification pending — `test_CY4_iterated_product_assoc.py` remains untouched by this wave (content-only prose additions, no engine changes, no test expectation changes). The `rem:cy4-pontryagin-number-stratum` numerical table can be wired to `compute/lib/cy4_e2_tower.py` engine outputs in a follow-up wave (not this run).

No AI attribution on any commit. All commits authored by Raeez Lorgat.

## 8. What survives open

- Cocycle candidate `c(x, y) = ⟨x ∪ y ∪ p_1(T_X), [X]⟩ / 24`: still uninscribed. Plausible programme target; Wave-1 heal (F3) picked option (b) "retract from status row" rather than (a) "inscribe as conjectural definition". Not this wave; re-evaluate at the next CY_4 pass.
- 7d hCS realization (Costello–Gaiotto attribution): neither inscribed nor typeset-cited in Vol III CY_4 chapters; remains AP272 programme frontier.
- Goodwillie-tower second-layer HH^{-3}_{E_1} obstruction analysis for non-product CY_4: cited at `cy_to_chiral.tex:4697-4700` as pending, matches scope tag of `conj:cy4-p1-family-associator-sextic`.
- `references.bib` for Vol III: AP281 open; not this wave (mission scope limited to CY_4).
