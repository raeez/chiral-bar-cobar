# Wave-4 Adversarial Attack / Heal: SC^{ch,top} Heptagon

Target: `~/chiral-bar-cobar-vol2/chapters/theory/sc_chtop_heptagon.tex` (1209 lines).
Claim under attack: `thm:heptagon-closed` and the seven named edges.

## Phase 1 — Attack (edge-by-edge)

### Edge (1)–(2): operadic ↔ Koszul dual, `thm:edge-12`

- Cites Vallette 2007 Thm 4.1.3, Hoefel 2009, Hoefel–Livernet 2012. The in-programme anchor is `prop:sc-koszul-dual-three-sectors`, which the theorem says is in `ch:theory-equivalence` but which in fact lives at `spectral-braiding-core.tex:3751`. **Cross-reference drift (mislocated anchor) — genuine but not load-bearing.**
- No back-reference to `thm:heptagon-closed`. Non-circular. ACCEPT content; HEAL anchor.

### Edge (2)–(3): Koszul dual ↔ factorization, `thm:edge-23`

- Depends on `thm:chiral-higher-deligne` (Vol II `chiral_higher_deligne.tex`, parallel Wave-4 agent — per prompt, not re-audited here).
- The $E_2$-chiral structure on $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is invoked; this is exactly the chiral Higher Deligne output. Non-circular given `thm:chiral-higher-deligne`.
- Φ-independence at cohomology: Willwacher 2015 is cited for uncoloured $E_2$; the "coloured analogue via coloured Kontsevich formality" is a silent extension. **Flag as scope-extension claim, not silently "proved."**

### Edge (3)–(4): factorization ↔ BV/BRST, `thm:edge-34`

- Costello–Gwilliam Vol II Thm 11.3.3 (closed sector) + Butson–Yoo 2018 (bulk–boundary extension). Genuine external anchors; non-circular.
- The QME ↔ open/closed MC identification: stated via `def:log-SC-algebra` in `bv-construction.tex`. Verified: definition exists. ACCEPT.

### Edge (4)–(5): BV/BRST ↔ convolution, `thm:edge-45`

- Semifree-model argument. Strict identity on semifree; HPL off. Standard. Non-circular.
- `prop:heptagon-edge-45` invokes **Dunn additivity to combine $E_2$-chiral with $E_1^{\mathrm{top}}$ into $E_3$-action on $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$.** This is exactly the topologisation step and is CONJECTURAL outside affine KM non-critical level. The theorem as stated elides the class-M chain-level obstruction. **Overreach: the $E_3$-action conclusion of prop:heptagon-edge-45 is generic-SC^{ch,top} at cohomology, not chain-level $E_3$.** HEAL with explicit scope qualifier.

### Edge (5)–(6): convolution ↔ Drinfeld centre, `thm:edge-56`

- Bijection MC ↔ objects of $\cZ(\Rep_{\mathrm{fact}}(\cA))$. Rests on `prop:half-braiding-construction` (in-file, line 294). ACCEPT as object-level bijection.
- **Functoriality gap**: the bijection is stated at the level of objects and gauge classes; naturality with respect to factorization morphisms of the module category (i.e. the equivalence as $E_2$-categories, not merely on underlying $\infty$-groupoids) is asserted but not proved beyond citation of Lurie HA 5.1 inside the `prop:half-braiding-construction` proof. **Scope-qualify: object-and-gauge bijection proved; full $E_2$-categorical equivalence depends on factorization-functor naturality of $\sigma_\cA(z)$, itself conditional on OPE-pole bounds stated but not witnessed.**

### Edge (6)–(7): Drinfeld centre ↔ DAG, `thm:edge-67`

- Invokes PTVV Corollary 2.6 (loop space of $k$-shifted is $(k-1)$-shifted) + "Deligne conjecture for coloured operads (coloured chiral higher Deligne)".
- **The last invocation is `thm:chiral-higher-deligne` applied to $(\SCchtop)^!$, which is a coloured dioperad, not an operad in the standard sense.** Coloured Deligne conjecture for dioperads with directional asymmetry is NOT the uncoloured or symmetric-coloured case. The `thm:chiral-higher-deligne` (Vol II) proves the statement for the pair $(C^{\bullet}_{ch}(A,A), A)$, not for arbitrary coloured dioperads. **Silent scope expansion — genuine issue.** HEAL.

### Edge (7)–(1): DAG ↔ operadic, `thm:edge-71`

- Tangent identification from `thm:convolution-lagrangian`. Global sections = CE of tangent dg-Lie = $\Omega(B(\SCchtop))$. Standard PTVV + CE. ACCEPT cohomologically; chain-level needs Kan extension hypothesis named but not proved for the coloured dioperad — FLAG scope.

### Closure (`thm:heptagon-closed`)

- Composition of seven $\infty$-quasi-isomorphisms. Valid IF each edge is genuinely an $\infty$-qi at the stated level. Two edges carry silent scope expansions (Edge 5–6 functoriality; Edge 6–7 coloured-dioperad Deligne). **The composed self-equivalence of Face (1) is said to be "homotopic to the identity because each edge is canonical modulo associator choice" — this is asserted, not proved. The heptagon closure at the chain level needs a coherence check (hexagon + pentagon for the associator transport along the heptagon) that is not presented.** HEAL with explicit "cohomological closure" vs "chain-level closure" distinction.

### Coloured-dioperad hygiene

- `conv:heptagon-object` line 89: "two-coloured coloured operad $\SCchtop$". **SC^{ch,top} has DIRECTIONAL restriction (closed→open, no open→closed): this is a coloured dioperad, not a symmetric coloured operad.** Dunn additivity cited in `prop:heptagon-edge-45` does not apply to dioperads of this asymmetric form outside the topologised regime. HEAL by renaming throughout as "coloured dioperad" or "two-coloured operad with directional restriction."
- Self-duality trap: text correctly denies self-duality at line 102. No silent self-duality assumption found in the edges. ACCEPT.

### Constitutional hygiene violations (typeset prose)

- Line 102: `(AP-SC-NOT-SELFDUAL)` in a `\begin{convention}` block.
- Line 1037: `(Chapter~\ref{ch:topologization}; AP-TOPOLOGIZATION)`.
- Line 1070: `(AP-TOPOLOGIZATION)`.
- Line 1096: `conjectural (AP-TOPOLOGIZATION);`.

All four are blacklist-slug leakage into typeset prose. Must be removed.

### Cross-reference drift

- Line 145, 703: `prop:sc-koszul-dual-three-sectors` said to be in `ch:theory-equivalence`; actually in `spectral-braiding-core.tex` under chapter label `ch:theory-drinfeld` (spectral braiding chapter). **HEAL** — the `\ref{prop:...}` itself resolves; only the chapter-locating prose is wrong.

### Dunn-additivity on a dioperad (load-bearing audit)

`prop:heptagon-edge-45` asserts `E_2^{\mathrm{chiral}} \otimes_{\mathrm{Dunn}} E_1^{\mathrm{top}} \simeq E_3$ acting on $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Dunn additivity (Lurie HA 5.1.2.2) is for $E_n$-operads in a symmetric monoidal $\infty$-category; it does NOT directly apply to the coloured dioperad $\SCchtop$. The correct statement is: on the topologised cohomology (affine KM non-critical, proved; general conformal case, conjectural), the cohomology of $\SCchtop$-action collapses to an $E_3$-topological action via Dunn. **The prose reads as if Dunn applies to $\SCchtop$ as a dioperad; correction: Dunn applies to the topologised $E_3$ only.**

## Phase 2 — Heal (surgical)

1. Remove four blacklist-slug hits (AP-SC-NOT-SELFDUAL, AP-TOPOLOGIZATION ×3).
2. Rename anchor-location drift: "Chapter~\ref{ch:theory-equivalence}" → `spectral-braiding-core.tex` chapter label.
3. Rewrite `conv:heptagon-object` line 89 + `subsec:face-operadic` to say "two-coloured coloured operad with directional restriction (coloured dioperad in the sense of Gan; no open-to-closed operations)."
4. Rewrite `prop:heptagon-edge-45` Dunn sentence to scope-qualify: "on topologised cohomology (proved for affine Kac–Moody at non-critical level; conjectural for general chiral with conformal vector), Dunn additivity of the $E_n$-cores passes…" — no chain-level claim for generic $\SCchtop$.
5. Insert scope remark after `thm:heptagon-closed`: cohomological closure unconditional at stated scopes; chain-level closure on the evaluation-generated Koszul locus; associator-transport coherence asserted, not proved.
6. Scope-qualify Edge 5–6 (object-and-gauge bijection proved; full $E_2$-categorical equivalence conditional on factorization-functor naturality of $\sigma_\cA$).
7. Scope-qualify Edge 6–7 "coloured Deligne conjecture": specialize to the $(\SCchtop)^!$ dioperad case with citation to `thm:chiral-higher-deligne` as the applicable chiral instance; mark the coloured-dioperad generalisation as inherited from that theorem, not invoked as independent.
8. Insert a closing convention that lists "chain-level vs cohomological" and "generic SC^{ch,top} vs topologised $E_3$" for each of the seven edges, as a tight audit table.

## Phase 3 — Closure

The honest heptagon: seven faces, seven edges, all $\infty$-quasi-isomorphic at cohomology after fixing $\Phi$; chain-level strict on the Koszul locus; the Dunn-additive upgrade to $E_3$ belongs to topologisation (proved affine KM non-critical; conjectural general); the coloured-dioperad structure is respected throughout (no silent self-duality, no silent open-to-closed).
