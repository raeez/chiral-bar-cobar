# Wave 5 attack-and-heal — CY-A_3 "PROVED in inf-cat" / Obs_Ainf = 0 universally via Costello TCFT

Date: 2026-04-18
Target: CLAUDE.md Vol III §6d hCS Session Cross-Awareness + AP-CY34 + AP278 (moduli-space boundary classification asserted without construction) + AP257 (engine-vs-manuscript) + AP272 (unstated cross-lemma via folklore citation).

Primary site: Vol III `chapters/theory/m3_b2_saga.tex:547-617` `thm:total-ainf-compat` (`\ClaimStatusProvedHere`).
Secondary sites: `thm:derived-framing-m3b2` (:697-719), `cor:no-naive-cross-degree` (:995-1016), `rem:tcft-vs-naive-b2` (:632-683), CLAUDE.md headline "CY-A_3 PROVED in inf-categorical framework", "Obs_Ainf = 0 UNIVERSALLY via Costello TCFT".

## 1. Attack ledger

F1 (AP278 moduli-space boundary classification asserted without construction, SEVERITY HIGH, category: load-bearing unproved step). At `m3_b2_saga.tex:588-598` the proof of `thm:total-ainf-compat` asserts:
  "The operators b and B^(2) correspond to *geometrically distinct* boundary strata that parametrise a specific compact 1-dimensional moduli space M̄_{b, B^(2)} whose only boundary components are b ∘ B^(2) and B^(2) ∘ b. No other Connes-hierarchy operations (B^(0), B^(1), B^(3)) appear as boundary types: the surface types producing B^(i) for i ≠ 2 involve different topological operations (rotation, interior contraction, cap product) that cannot arise as degenerations of the strip-plus-node family."
  M̄_{b, B^(2)} is NEVER constructed in the file (zero hits for "dim(M̄_{b,B^(2)})", zero hits for a strata enumeration, zero hits for a corners/orientation verification). The claim "no other Connes operations arise" is asserted by elimination without citing a primary-source theorem that gives this boundary count. A reader cannot audit the ∂² = 0 argument.

F2 (AP272 unstated cross-lemma via folklore citation, SEVERITY HIGH). The proof cites `Costello2005TCFT` "Theorem A" + `Costello2007Ainfty` arXiv:0706.1959. Two defects:
  (a) BIBKEY DRIFT. `bibliography/references.tex:79-85` shows `Costello2005TCFT` and `Costello2007Ainfty` are BOTH legacy aliases to the SAME paper (math/0412149, Adv. Math. 210). The proof's "(Costello~\cite{Costello2007Ainfty}; arXiv:0706.1959)" at `m3_b2_saga.tex:574-575` references arXiv:0706.1959 but the alias resolves to 0412149. This is AP281-class bibkey drift: the sentence's arXiv number and the bibkey's target are different papers. The correct bibkey for 0706.1959 is `Costello2007` / `Costello2007OpenClosed` (both defined at `references.tex:72-76`, aliases of each other).
  (b) "Theorem A" of Costello 2005 (math/0412149) is the equivalence between cyclic A_inf CY-d algebras and open TCFTs; it does NOT independently state M̄_{b, B^(2)} has only two boundary components. The boundary classification is an unstated corollary the proof attributes to Costello without pinning a proposition number.

F3 (AP257 engine-vs-manuscript, SEVERITY MEDIUM, partially bridged). Engine `compute/lib/chain_level_m2_b2_cancellation.py:1-80` openly states: "There is no purely algebraic proof using only the pairing and the A-infinity operations. The proof is ESSENTIALLY GEOMETRIC: it uses the compact 1-dimensional moduli space M_{b,B^{(2)}}. The algebraic content is the IDENTIFICATION of b and B^{(2)} as boundary strata, which requires the open-closed TCFT equivalence." `rem:tcft-vs-naive-b2` (:632-683) already does the reconciliation work honestly, distinguishing `B^{(2)}_TCFT` from `B^{(2)}_naive` and marking the chain-level identification CONJECTURAL for non-formal algebras. The REMARK is honest; the THEOREM header `\ClaimStatusProvedHere` and the CLAUDE.md headline "Obs_Ainf = 0 UNIVERSALLY via Costello TCFT" do not carry the scope restriction forward.

F4 (AP287 cross-volume + internal scope-drift: CLAUDE.md carries stronger claim than inscribed theorem, SEVERITY MEDIUM). CLAUDE.md headline "CY-A_3 PROVED in inf-categorical framework; chain-level [m_3,B^(2)]!=0 is NOT obstruction; Obs_Ainf=0 UNIVERSALLY via Costello TCFT" compresses (i) `thm:total-ainf-compat` (operadic-level only, modulo AP278 gap) and (ii) `thm:derived-framing-m3b2` (∞-cat Goodwillie tower on UNIT-CONNECTED CY_3 categories only — K3×E IS unit-connected, but the headline's "UNIVERSALLY" loses this hypothesis). `thm:derived-framing-m3b2(i)-(iv)` scopes explicitly to "smooth proper CY_3 category C with unit-connected Hochschild homology (HH^0(C) = k)"; AP-CY34 headline drops that hypothesis. AP271-style reverse-drift (CLAUDE.md stronger than source): F4 makes the retraction load-bearing.

F5 (AP272 derived-framing Goodwillie connectivity bound, SEVERITY LOW, cite-sharpening). `thm:derived-framing-m3b2` proof cites `FrancisGaitsgory2012` for the bound "HH^p_{E_1}(A, A^{⊗k}) = 0 for p < -k+1 for unit-connected A." This is the connectivity bound for E_1-Hochschild of a connective E_1-algebra; standard in Francis 2013 / Francis-Gaitsgory, but the specific theorem/proposition number is not cited. Sharpen to section-level cite (AP285 alias section-number drift discipline).

F6 (AP278 companion: `prop:cyclic-ainf-framing-compat`, SEVERITY HIGH, not yet read but flagged by the meta-prompt). Needs parallel audit to F1; inherits the same load-bearing moduli-space boundary-classification obligation if it proves a TCFT-style cancellation.

## 2. Surviving core (Drinfeld three sentences)

Two independent facts survive the audit. (i) For any cyclic A_inf CY_3 algebra, the `B^{(2)}_TCFT` operator derived from Costello's open-closed TCFT equivalence satisfies {b, B^{(2)}_TCFT} = 0 at the level of the MODULI-OPERAD CHAIN COMPLEX; the chain-level identification `B^{(2)}_TCFT ≃ B^{(2)}_naive` on the bar complex of the algebra is CONJECTURAL for non-formal A_inf algebras (Tradler strictification for formal). (ii) For any smooth proper CY_3 category with UNIT-CONNECTED Hochschild homology (HH^0 = k), the primary E_2 → E_3 lifting obstruction lives in HH^{-2}_{E_1}(HH_•(C), HH_•(C)), which vanishes by the Francis-Gaitsgory connectivity bound for connective unital E_1-algebras; the space of E_3-structures compatible with the canonical E_2 is contractible. (iii) The CLAUDE.md headline "Obs_Ainf = 0 UNIVERSALLY" is an overcompression: it loses the unit-connectedness hypothesis (F4), the non-formal chain-level conjecture (F3, already honest in `rem:tcft-vs-naive-b2`), and the unproved moduli-space boundary classification (F1).

## 3. Heals (proposed, with status tags; no edits yet per "Begin by reading" scope — deliverable is the ledger)

H-F1 (AP278 primary). Two heal options:
  (a) INSCRIBE M̄_{b, B^(2)}. Add `\begin{proposition}[Boundary classification of the strip-plus-node moduli]` after `thm:total-ainf-compat` proof, stating: M̄_{b, B^(2)} ≅ M̄_{0,n+2}^{node} (compactified moduli of genus-0 bordered surfaces with n ordered boundary punctures and one interior node) — which the ENGINE docstring at `chain_level_m2_b2_cancellation.py:47-53` already identifies — is a compact 1-manifold with corners whose codim-1 strata correspond bijectively to boundary-type-A (strip degeneration before node) and boundary-type-B (node before strip), with no other types because B^(0)/B^(1)/B^(3) involve rotation/interior contraction/cap product that are not strip-plus-node degenerations. Cite Costello 2005 (math/0412149) §2.3 (bordered-surface moduli) + Costello 2007 (0706.1959) §3 (open-closed extension) with specific equation/proposition numbers once verified. STATUS: `\ClaimStatusProvedElsewhere` with Remark[Attribution]; or
  (b) DOWNGRADE. Retag `thm:total-ainf-compat` header from `\ClaimStatusProvedHere` to `\ClaimStatusConditional`; add `\begin{remark}[Scope]` naming Costello-Segal strictification + the uninscribed boundary classification as the conditional hypothesis. Keep the chapter's three-level architecture intact; the three levels still separate the claim honestly.

H-F2 (AP272 + AP281 bibkey drift). (a) Retarget `\cite{Costello2007Ainfty}` in the proof to `\cite{Costello2007}` (the correct alias for 0706.1959); the current alias is legacy-drift (`references.tex:83-85` openly flags "LEGACY ALIAS for Costello2005; consolidate in future revision"). (b) Attach §/Thm numbers: Costello 2005 Theorem 2.0.1 + Costello 2007 §3.2 (verify on primary). (c) After the rewrite, grep all Vol III for `Costello2007Ainfty` and `Costello2005TCFT` to deduplicate to one alias per target paper.

H-F3 (AP257 bridge remark). No new edit needed: `rem:tcft-vs-naive-b2` (:632-683) already does the bridge. But `\ClaimStatusProvedHere` on the parent theorem should be softened to `\ClaimStatusConditional` if H-F1(b) is chosen, or the remark's conjectural scope must be echoed in the theorem STATEMENT (not only the remark). Current statement at :562-567 already reads "The chain-level identification of B^{(2)}_TCFT with the naive pairwise-contraction operator ... is conjectural for non-formal A_inf algebras" — this is honest; the theorem environment tag however remains ProvedHere. Reconcile: either (α) move the conjectural clause to a `\begin{remark}` and restrict the theorem to the moduli-operad level (then ProvedHere is honest but F1/H-F1 must close); (β) keep the composite statement and downgrade to Conditional.

H-F4 (CLAUDE.md headline). Rewrite Vol I CLAUDE.md §"Vol III 6d hCS Session Cross-Awareness" headline (also AP-CY34 body) to:
  "CY-A_3 operadic-level compatibility PROVED for the B^{(2)}_TCFT operator (Costello open-closed TCFT, Conditional on moduli-operad boundary classification M̄_{0,n+2}^{node}, two codim-1 types); ∞-categorical lifting obstruction HH^{-2}_{E_1} PROVED to vanish for smooth proper CY_3 categories with UNIT-CONNECTED Hochschild homology (Francis-Gaitsgory connectivity bound); the chain-level identification B^{(2)}_TCFT ≃ B^{(2)}_naive on the bar complex is CONJECTURAL for non-formal A_inf algebras (Tradler strictification for formal). Individual {b_k, B^{(2)}_naive} nonzero and cannot cancel across arities (engine `chain_level_m2_b2_cancellation.py`)."
  AP-CY34 rewrite: "total {b, B^{(2)}_TCFT}=0 at the moduli-operad level via Costello's open-closed TCFT and the boundary classification of M̄_{0,n+2}^{node}; individual {b_k, B^{(2)}_naive}≠0 for k ≥ 3 and map to distinct bar arities (no cross-arity cancellation possible on the naive operator); TCFT-vs-naive identification conjectural off the formal locus."

H-F5 (AP272 Francis-Gaitsgory section-cite). In `thm:derived-framing-m3b2` proof (:738-748), append "[Francis-Gaitsgory 2012, Prop. X.Y]" (verify primary) to the connectivity-bound invocation.

H-F6 (AP278 companion). Parallel heal on `prop:cyclic-ainf-framing-compat` once located (not yet read in this audit); same H-F1 menu applies.

## 4. Inscription plan (Chriss-Ginzburg voice, no commits)

If the user authorizes edits, the load-bearing rectification is H-F1(b) + H-F4 + H-F2, in a single atomic pass:

(i) m3_b2_saga.tex `thm:total-ainf-compat` header: `\ClaimStatusProvedHere` → `\ClaimStatusConditional`. Append `\begin{remark}[Scope]\label{rem:total-ainf-compat-scope}` naming (a) moduli-operad boundary classification of M̄_{0,n+2}^{node} as the conditional hypothesis, cited to Costello 2005 §2.3 / 2007 §3 (verify primary-source section numbers), (b) the non-formal chain-level identification conjecture already in `rem:tcft-vs-naive-b2`.
(ii) `\cite{Costello2007Ainfty}` → `\cite{Costello2007}` at :574 (and any duplicate callsites in the file).
(iii) Preamble prose at :47-57 softens "the anticommutator {b, B^{(2)}} vanishes" to "{b, B^{(2)}_TCFT} vanishes at the moduli-operad level"; strict-chain-level identification with the naive operator cited forward to `rem:tcft-vs-naive-b2`.
(iv) CLAUDE.md Vol I §"Vol III 6d hCS Session Cross-Awareness" + AP-CY34 rewrite as H-F4.
(v) `cor:no-naive-cross-degree` stays ProvedHere (it is the NEGATIVE result, honestly proved via bar-arity disjointness).
(vi) Add `prop:cyclic-ainf-framing-compat` to Wave-5 queue for parallel audit.

Commit plan: NONE in this wave per user constraint. Ledger inscribed at this file.

## 5. Engines / tests touched: none (read-only audit).

## 6. Queue for Wave-6

- `prop:cyclic-ainf-framing-compat` parallel audit (F6).
- Primary-source verification of Costello 2005 Thm 2.0.1 + Costello 2007 §3.2 exact statements of the boundary classification for M̄_{0,n+2}^{node} (or alternate: Kontsevich-Soibelman, Kajiura-Stasheff, Cieliebak-Latschev for the strip-plus-node 1-moduli).
- Vol III `notes/tautology_registry.md` entry for the ProvedHere→Conditional retag on `thm:total-ainf-compat`.
- HZ-IV decorator re-audit: `operadic_tcft_mk_b2_engine.py` (43 tests) and `derived_framing_obstruction.py` (51 tests) — verify the decorator bodies are not AP277-style tautological or AP287-style primitive-by-construction.

## 7. Beilinson one-liner

Drinfeld: "Obs_Ainf = 0 is two theorems, not one: moduli-operad ∂² = 0 (conditional on a boundary classification no one has written down) and E_1-Hochschild connectivity (unconditional on unit-connected CY_3); the chain-level identification on the bar complex connects them, and it is conjectural off the formal locus. The honest sentence is shorter and sharper."
