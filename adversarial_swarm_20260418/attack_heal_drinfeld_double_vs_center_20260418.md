# Attack-heal: Drinfeld double $D(\cH_k)$ vs derived chiral center $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cH_k)$

Date: 2026-04-18. Scope: Vol I `conj:v1-drinfeld-center-equals-bulk` + three obstructions; conflation audit $D$ vs $Z$ vs $\cZ^{\mathrm{der}}_{\mathrm{ch}}$ across Vols I + III. Brief-audit mandate per AP314.

## (i) Locate `conj:v1-drinfeld-center-equals-bulk`

Status-table citation: `preface.tex:4228`. Actual location: `chapters/frame/preface.tex:4267` (label at :4267; body :4267-4281).

- AP271 line-drift is ALREADY inscribed in the CLAUDE.md status row at `/Users/raeez/chiral-bar-cobar/CLAUDE.md:634` ("preface.tex:4267, AP271 line-drift 2026-04-18 from previously advertised :4228"). No new AP needed on this item.
- Legacy scaffolding files still advertise `:4228` (adversarial_swarm_20260417/wave7_*.md, fix_wave_B_20260413_171623/*.md, patch file `adversarial_swarm_20260418/patch_critical_level_20260418.patch:30`). These are session-ledger rot; no consumer ref.
- `standalone/theorem_index.tex:61,:102` advertises the conjecture at `preface.tex:3950` (stale by two revisions). Third-line-drift; fix in theorem_index at next regeneration.
- Preface body :4267-4281 statement: for general $E_1$-chiral $\cA$ with $U_\cA = \cA \bowtie \cA^!$, assuming the §10.2 topologization hypotheses, $Z(U_\cA) \simeq \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ as $E_3^{\mathrm{top}}$-algebras.

The conjecture is GENERAL-$E_1$-chiral, NOT Heisenberg-specific. The CLAUDE.md status-row label "Drinfeld double vs derived center (Heis)" is HEIS-SPECIFIC, inheriting from `prop:derived-center-explicit` ($\ChirHoch^*(\cH_k) = (\bC, \bC, \bC, 0, \ldots)$). The Heis instance is the canonical witness; the conjecture itself is broader.

## (ii) Three obstructions: prose only, never inscribed as propositions

Preface :4283-4294 enumerates three obstructions in flowing prose:

1. "pointwise reduction fails for class M algebras: the stalk-wise center at degree $\ge 3$ misses $A_\infty$ corrections"
2. "the Verdier dual $\cA^!$ does not automatically carry strict factorisation, so $U_\cA$ requires careful completion"
3. "bar-cobar inversion produces the algebra $\cA$, not its center; the compatibility with the Hochschild functor requires an independent argument"

Cross-volume grep for `\begin{proposition}` + `pointwise reduction` / `Verdier dual.*strict factorisation` / `bar-cobar inversion produces`: zero hits. The obstructions are NOT inscribed as propositions (or lemmas) anywhere in Vols I / II / III.

Partial coverage: `/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B14_stale_cross_vol_refs_v2.md:4019` (scratch note) remarks that "$d_{\mathrm{alg}} = \infty$ [implies] the pointwise reduction of step~(1) is [inadequate]" — scratch-layer, not inscribed.

Vol III `drinfeld_center.tex:812` (per `adversarial_swarm_20260417/wave11_vol_iii_part_iii_attack_heal.md:11`) states that "chain-level identification at $d=3$ for non-formal algebras remains open", and `:931-935` flags class-M pointwise reduction failure. These are Vol III remarks matching obstruction 1 in scope, but they are LOCAL disclaimers of the Vol III $\Phi_d$ functor, not inscribed obstruction propositions against `conj:v1-drinfeld-center-equals-bulk`.

Conclusion (ii): all three obstructions are PROSE-ONLY in the Vol I preface. A reader chasing the conjecture's scope via `\ref{}` finds no proposition-level obstruction machinery.

**AP1981 (Prose-obstruction-only conjecture without proposition-level obstruction inscriptions).** A closing conjecture identifies three obstructions by name in the prose immediately after the `\begin{conjecture}` block ("pointwise reduction fails...", "Verdier dual does not carry strict factorisation...", "bar-cobar inversion produces $\cA$ not its center...") but inscribes none of the three as a `\begin{proposition}` or `\begin{lemma}` with an explicit obstruction class in a named cohomology group. A reader encountering the conjecture has no machinery to verify whether a candidate resolution strategy addresses each of the three; agents writing heal attempts cannot `\ref{}` the obstruction they are resolving; subsequent audits cannot check that a resolution commute with each obstruction. The AP266 healing pattern (sharpened-obstruction-as-explicit-cocycle) is the preventative counter: every conjecture flagged as "conditional on three obstructions" should inscribe each obstruction as its own proposition with a named class in $H^\bullet_{?}$ carrying a coefficient matching a programme invariant. Canonical violation here: `conj:v1-drinfeld-center-equals-bulk` at `chapters/frame/preface.tex:4267-4294`. Counter: after any `\begin{conjecture}` whose scope admits explicit obstructions, inscribe each as `\begin{proposition}[Obstruction N to conj:X]` with a named class; downstream heals reference the proposition by label. Distinct from AP241 (advertised-but-not-inscribed characterization — that pattern catches a claimed equivalence spoke absent from the theorem statement), AP242 (forward-reference lemma labelled as inscribed — prose is honestly prose-level, not labelled). Related AP266 (sharpened obstruction healing as positive pattern): AP1981 is its retrospective-diagnostic sibling. Scale of violation: one conjecture × three uninscribed obstructions.

## (iii) Vol I: Drinfeld DOUBLE $D$ vs Drinfeld CENTER $Z$ — conflation check

The preface conjecture writes $Z(U_\cA)$ — Drinfeld CENTER of the DOUBLE $U_\cA$. Two distinct constructions overlap in the symbol:

- **$U_\cA = \cA \bowtie \cA^!$** is the Drinfeld DOUBLE (Hopf-algebraic bosonisation of the chiral algebra against its Koszul dual). `chapters/frame/heisenberg_frame.tex:2093-2121` inscribes the Heisenberg case: $U_{\cH_k} = \cH_k \otimes \cH_k^!$ with braiding $R(z) = \exp(k\hbar/z)$. `chapters/theory/ordered_associative_chiral_kd.tex:8837-9499` gives the ordered-Koszul version (Yang-Zhao bialgebra) and explicitly separates antipode non-lifting (`rem:chiral-bialgebra-not-hopf`, AP263 healed).
- **$Z(\cC)$** is the categorical Drinfeld CENTER — the braided monoidal $E_2$-structure on $\cC$-modules equivariant for the half-braiding. `preface.tex:4103, :4113, :4124, :4226` consistently uses $Z$ for the categorical center.
- **$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = H^\bullet(C^\bullet_{\mathrm{ch}}(\cA, \cA), \delta)$** is the derived chiral center (Hochschild cohomology of the chiral algebra on the curve). `chapters/theory/chiral_center_theorem.tex:1955-1994` proves dim 3 for Heisenberg; naive Drinfeld center (of $U_{\cH_k}$ or of $\cH_k$ as chiral algebra) is dim 1.

The conjecture statement $Z(U_\cA) \simeq \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is a THREE-object claim:

1. Start with $\cA$ (E_1-chiral algebra on curve).
2. Form $U_\cA = \cA \bowtie \cA^!$ (Drinfeld DOUBLE — Hopf-algebraic construction at the E_1 level).
3. Take $Z(U_\cA)$ (categorical Drinfeld CENTER of the double — E_2 structure on its module category).
4. Claim: $Z(U_\cA) \simeq \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ as $E_3^{\mathrm{top}}$-algebras after topologization.

No conflation of $D$ and $Z$ in the preface body itself — each symbol is used consistently. However:

- **CLAUDE.md status row "naive Drinfeld center dim 1 vs derived chiral center dim 3"** collapses two distinct objects under the name "naive Drinfeld center". Which object is dim 1? Candidates: (a) categorical Drinfeld center $Z(U_{\cH_k}\text{-mod})$ before topologization; (b) naive commutant / pointwise chiral center $Z(\cH_k)$ of $\cH_k$ itself (the vacuum line, $= \bC$); (c) $H^0$ part of $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cH_k)$. FM40 in CLAUDE.md reads "Z(Drin(H_k)) dim 1 vs Z^{der}_{ch}(H_k) dim 3", i.e. option (a). The status row is consistent with FM40 but the row's phrasing "naive Drinfeld center" does not pin which of (a)-(c) it means. A reader could reasonably take "naive Drinfeld center" as (b) (vacuum line of $\cH_k$), which is the trivially-dim-1 object every chiral algebra has, trivialising the non-triviality of the comparison.

**AP1982 (Status-row collapse of $D(\cA)$ / $Z(U_\cA)$ / $Z(\cA)$ under unqualified "Drinfeld center" label).** A CLAUDE.md status row compares "naive Drinfeld center dim 1" against "derived chiral center dim 3"; the "naive Drinfeld center" phrase is ambiguous across (a) $Z(U_{\cA}\text{-mod})$ (categorical center of the module category of the Drinfeld double), (b) $Z(\cA)$ (chiral commutant = vacuum line for a simple chiral algebra), (c) $H^0 \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ (degree-zero part of the derived center). All three are dim 1 for Heisenberg by coincidence, so the statement is numerically correct under every reading, but the MEANING of the comparison differs by reading. Under reading (b) the comparison is trivial (every simple chiral algebra has vacuum-line commutant); under (a) the comparison is a genuine categorical statement of `conj:v1-drinfeld-center-equals-bulk` scope; under (c) it is a Theorem-H concentration claim. Counter: before writing "naive Drinfeld center" in a status row, pin one of $Z(U_\cA\text{-mod})$ / $Z(\cA)$ / $H^0\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ and inscribe the specific object in prose. Healing: amend the status row to read "$Z(U_{\cH_k}\text{-mod})$ dim 1 (categorical Drinfeld center of the double's module category, $E_2$-braided, trivial braiding in the abelian Heisenberg case) vs $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cH_k)$ dim 3 (chain-level Hochschild cohomology)". Distinct from AP234 (two Koszul conductors under the letter $K$) and AP311 (two invariants hidden under $\varrho$): AP1982 is the categorical-vs-chain-complex conflation under "center" — three distinct mathematical objects overlap in one phrase. Related AP275 (CLAUDE.md narrative inverts the correct mathematical discipline): AP1982 is the zero-information variant where the narrative is technically consistent with all readings but distinguishes none.

Vol I elsewhere: `chapters/connections/holographic_datum_master.tex:790-956` discusses Drinfeld double as universal boundary-bulk algebra; explicitly names the double (not the center) as the six-slot projection source, consistent with the preface usage. No conflation found there.

`chapters/connections/outlook.tex:388` refers to "$E_1$-chiral Drinfeld double"; consistent usage.

## (iv) Vol III: $D$ vs $Z$ vs $\cZ^{\mathrm{der}}_{\mathrm{ch}}$ consistency

Vol III uses all three objects extensively:

- **Drinfeld double**: `working_notes.tex:216` ("CoHA = $E_1$-sector; Draft (Drinfeld double)"), `:1192` ("Drinfeld double; $g(z)g(-z) = 1$ from the CY condition" for $\bC^3$), `:1888` ("$R$-matrix requiring the full Drinfeld double"), `:2462` (CoHA Euler form discussion). Used as the Hopf-algebraic $E_1$ object carrying $R$-matrix.
- **Drinfeld center $\cZ(\Rep^{E_1}(\cdot))$**: `working_notes.tex:1040, :1097, :1100, :1105, :1212, :1216, :1694, :1696, :1737, :1767, :1923, :1924, :2462, :2505, :2976, :5026`, plus 15+ engine references in `appendices/engine_table_rows.tex`. Consistently used as the $E_2$-enhancement functor: $\cC \mapsto \cZ(\Rep^{E_1}(\cC))$. Arrow 3 of the $E_n$ circle.
- **Chiral derived center $\cZ^{\mathrm{der}}_{\mathrm{ch}}$**: `working_notes.tex:1737` explicitly bridges "the $E_1 \to E_2$ passage via Drinfeld center (Theorem~\ref{wn:thm:c3-drinfeld-center}) corresponds to the open-to-bulk passage in Vol II via the chiral derived center $\cZ^{\mathrm{der}}_{\mathrm{ch}}(A)$". This is a FUNCTORIAL CORRESPONDENCE, not an identification: the Vol II chiral derived center is the bulk algebra in the 3d HT picture; the Vol III Drinfeld center is the $E_1 \to E_2$ passage on module categories. The `:1737` bridge SENTENCE is the closest Vol III comes to `conj:v1-drinfeld-center-equals-bulk`, but Vol III does not inscribe the equivalence — it routes around the conjecture by working with $\cZ(\Rep^{E_1}(A_X))$ as its working object.
- `working_notes.tex:2505` flags a genuine obstacle: "The Drinfeld center does not commute with homotopy colimits: $\cZ(\mathrm{hocolim}\, A_\alpha) \neq \mathrm{hocolim}\, \cZ(A_\alpha)$." This is a Vol-III-specific $\Phi$-functor obstruction, NOT obstruction 1/2/3 of Vol I's conjecture. No cross-talk.

Conclusion (iv): Vol III consistently distinguishes the three. Drinfeld DOUBLE is the $E_1$ Hopf object (CoHA or its dual); Drinfeld CENTER is the $E_2$-enhancement functor on module categories; chiral derived center is the Vol II bulk object. The sole bridge statement at `:1737` is correspondence-level and does not invoke `conj:v1-drinfeld-center-equals-bulk`.

## Minimal APs inscribed

Two new APs only, per AP314 throttling:

- **AP1981**: prose-obstruction-only conjecture without proposition-level obstruction inscriptions (detection + healing via AP266 pattern);
- **AP1982**: status-row collapse of $D(\cA)$ / $Z(U_\cA)$ / $Z(\cA)$ under unqualified "Drinfeld center" label.

Neither requires immediate manuscript edit. AP1981 suggests inscribing each of the three obstructions at Vol I preface :4283-4294 as propositions with named classes; AP1982 suggests a one-line amendment to the CLAUDE.md status row "Drinfeld double vs derived center (Heis)" to pin the dim-1 object explicitly.

No AP numbering collision audit performed vs Wave 15-17 inscriptions (AP1981-AP2000 block reserved for this audit per mission brief). If AP1981/AP1982 collide with a concurrent swarm's reservation, rename under Wave 18 numbering at reconciliation.

## No new CLAUDE.md or manuscript Edit performed

Mission is brief-audit only. No Edit invocations were made on CLAUDE.md, preface.tex, chiral_center_theorem.tex, or any Vol III file. Report ends here.
