# Wave 6 attack-and-heal — CY-to-chiral Φ vs AP247 (functor single-target discipline)

Date: 2026-04-18. Target: FM43 + AP247. Scope: Vol III chapters/theory/cy_to_chiral.tex, chapters/frame/preface.tex, main.tex, appendices/notation.tex + Vol I CLAUDE.md FM43.

## Attack ledger

| # | file:line | finding | severity | category |
|---|-----------|---------|----------|----------|
| F1 | `chapters/theory/cy_to_chiral.tex:1–175` | Primary Φ inscription ALREADY HEALED at source. Line 8 `\Phi\colon \CY_2\text{-}\Cat \to \Etwo\text{-}\mathrm{ChirAlg}` is the d=2 evaluation with fixed target (legitimate functor at fixed d); line 36 section title reads "The CY-to-chiral correspondence programme"; line 41 writes `\{\Phi_d\}_{d \ge 1}` and declares "the target category depends on d ... does not assemble into a functor in the standard category-theoretic sense"; rem:phi-not-unified-functor :94–103 gives the AP247 Grothendieck-style acknowledgement in three subclauses (functoriality on morphisms, CY-duality-for-families, dimensional reduction); conj:phi-d-functoriality :105–113 makes the morphism-action assertion honestly conjectural with Mukai-transform K3→K3 test case flagged. rem:phi-uniqueness :120–128 states per-d uniqueness on OBJECTS only; "property (U2) (morphism action) is not part of the uniqueness package". | SURVIVING (no heal needed) | baseline |
| F2 | `chapters/frame/preface.tex:1638–1640` (pre-heal) | Late-preface three-volumes triangle writes "the functor Φ : CY_d-Cat → E_n-ChirAlg produces chiral algebras" — AP247 single-target drift AFTER the opening preface correctly uses correspondence-programme framing (lines 25–35 box-equation `\{\Phi_d\}_{d\ge1}`, "with target category varying with d"). Reverse drift within the same preface: front half honest, back half regressed to singular functor. | MODERATE | AP247 + AP288 (session-ledger stale narrative within a single file) |
| F3 | `chapters/frame/preface.tex:1648,1661,1671` (pre-heal) | "bridging Vol I and Vol III through Φ", "supplying the chiral algebra via Φ", "mediated by Φ" — three bare-Φ citations treating the programme as a single functor. | LOW–MODERATE | AP247 prose-propagation |
| F4 | `main.tex:922–923` (pre-heal) | Six-routes CY-C enumeration item (4) reads "Φ₃: the CY-to-chiral functor at d=3" — at fixed d=3 this is technically a functor (single target E_1-ChirAlg), but "CY-to-chiral functor" phrasing propagates AP247 in a load-bearing section header. | MODERATE | AP247 |
| F5 | `appendices/notation.tex:234` (pre-heal) | Notation table declares `\Phi\colon \CY_d\text{-}\Cat \to \Etwo\text{-}\mathrm{ChirAlg}` as "CY-to-chiral functor (Theorem CY-A)" — FLAT AP247 violation: single Φ with fixed target E_2-ChirAlg is the d=2 evaluation mistakenly labelled the full programme; at d=3 the target is E_1-ChirAlg. | HIGH | AP247 + AP246-style type-swap (wrong target for d-indexed programme) |
| F6 | `appendices/notation.tex:356` (pre-heal) | CY-A label row writes "CY-to-chiral functor" with `\Phi\colon \CY_d\text{-}\Cat \to \En\text{-}\mathrm{ChirAlg}` (uses generic E_n — OK) but label itself still carries "functor" language. | MODERATE | AP247 terminological |
| F7 | `CLAUDE.md (Vol I):565` (pre-heal) | FM43 reads "E_n output scope of CY-to-chiral Φ" — singular Φ framing in the counter-rule. Operational content correct, framing incompatible with AP247. | MODERATE | AP247 + AP5 cross-volume |
| F8 | working_notes.tex (multiple sites :189, 211, 283, 354, 870, 920, 1045, 1174, 1868, 1873, 2379, 2908, 2965, 4792, 5369, 5412) | Heavy "CY-to-chiral functor" usage across working notes. NOT TYPESET INTO PDF (working_notes is the author's scratch file); AP247 discipline not violated at typeset level. | INFO | note-level residue |
| F9 | `appendices/engine_table_rows.tex:2,4,11,95` + `appendices/engine_catalogue.tex:41` | "CY-to-chiral functor" as an ENGINE CATEGORY NAME in Python engine metadata tables. Engine module names like `cy_to_chiral_functor.py` are stable Python identifiers; renaming breaks imports across ~570 engine files. ALLOWED under CLAUDE.md metadata-hygiene exception for Python module names. | ALLOWED | out of AP247 scope |
| F10 | `notes/theory_denominator_bar_euler.tex:297,423,453,712,899`, `notes/physics_mtheory_branes.tex:65,303`, `chapters/examples/*` sibling sites (fukaya_categories, quantum_group_reps, super_riccati, toric_cy3_coha, matrix_factorizations, cy_c_six_routes_convergence) | "CY-to-chiral functor Φ" / "CY-to-chiral functor $\Phi_d$" scattered across example chapters and notes. Each site uses Φ_d at fixed d or names the d=2,3 evaluation; individually AP247-compliant-at-fixed-d but collectively reinforces singular-functor framing. | LOW | note-level propagation, second-pass target |

## Surviving core (3 Drinfeld-style sentences)

The CY-to-chiral construction is not a single functor Φ: CY-Cat → ChirAlg; it is a d-indexed correspondence programme {Φ_d}_{d≥1} whose target category E_{n(d)}-ChirAlg(M_d) varies with d — E_∞ at d=1 (commutative Gerstenhaber degree 0), E_2 at d=2 (Kontsevich–Vlassopoulos S²-framing), E_1 at d≥3 with the E_2-braiding migrating to the Drinfeld centre Z(Rep^{E_1}(Φ_d(C))) via the half-braiding identification σ_{V_u}(V_v) = R(u−v). Per-d existence and uniqueness hold on objects on the smooth proper locus (H1)+(H2)+(H3), proved for d=1 (classical lattice VOAs), d=2 (Theorem CY-A₂, explicit on K3: Φ_2(D^b Coh K3) = Mukai Heisenberg of rank 24), d=3 (Theorem CY-A₃ via ∞-categorical HH^{-2}_{E_1} = 0 and Goodwillie contractibility); d≥4 is open. Functoriality on morphisms (property U2: CY-morphism f: C→C' maps to chiral-algebra morphism Φ_d(f)) is separately conj:phi-d-functoriality, tested at d=2 on the Mukai transform K3 → K3 (chain-level verification pending) and open in general — so AP247 sub-checks (a) fail (d-indexed target), (b) hold only conjecturally per-d, (c) hold only conjecturally on a single concrete morphism pair.

## Heal per finding

| # | status | action taken | tag |
|---|--------|--------------|-----|
| F1 | SURVIVING | None — source is correct. | n/a |
| F2 | HEALED | preface.tex:1638–1640 rewritten to "the $d$-indexed correspondence programme $\{\Phi_d \colon \CY_d\text{-}\Cat \to E_{n(d)}\text{-}\mathrm{ChirAlg}(\cM_d)\}_{d\ge1}$ produces chiral algebras from CY categories per-$d$ ... see Theorem~\ref{thm:phi-platonic} and Remark~\ref{rem:phi-not-unified-functor} for why $\{\Phi_d\}$ is a correspondence programme, not a single functor". Cross-link to primary-source theorem and not-unified-functor remark added. | AP247 heal — ClaimStatusProvedHere carried forward from source |
| F3 | HEALED | preface.tex:1648 "bridging Vol I and Vol III through $\Phi$" → "through the per-$d$ evaluations of $\{\Phi_d\}$"; :1661 "supplying the chiral algebra via $\Phi$" → "via the per-$d$ construction $\Phi_d$" with CY category explicitly qualified "of dimension $d$"; :1663 $\kappa_{ch}(\Phi(\cC_X))$ → $\kappa_{ch}(\Phi_d(\cC_X))$ (HZ-7 $\kappa_{ch}$ subscript preserved); :1671 "mediated by $\Phi$" → "mediated by $\{\Phi_d\}$". | AP247 heal |
| F4 | HEALED | main.tex:922 "$\Phi_3$: the CY-to-chiral functor at $d=3$" → "$\Phi_3$: the $d=3$ evaluation of the CY-to-chiral correspondence programme $\{\Phi_d\}$". Preserves the Φ_3 symbol (Φ_3 at fixed d IS functorial on objects) while explicitly naming the parent programme. | AP247 heal |
| F5 | HEALED | notation.tex:234 rewritten: single Φ entry replaced by `\{\Phi_d\colon \CY_d\text{-}\Cat \to E_{n(d)}\text{-}\mathrm{ChirAlg}(\cM_d)\}_{d \ge 1}` glossed "CY-to-chiral correspondence programme: $d$-indexed per-$d$ constructions, $n(d) = \infty, 2, 1$ at $d = 1, 2, \ge 3$; not a single functor across $d$ (Theorem~\ref{thm:phi-platonic}, Remark~\ref{rem:phi-not-unified-functor})". The $A_\cC = \Phi(\cC)$ row updated to $A_\cC = \Phi_d(\cC)$ with per-$d$ qualifier. | AP247 heal + AP246-style type correction |
| F6 | HEALED | notation.tex:356 CY-A label row: "CY-to-chiral functor" → "CY-to-chiral correspondence programme $\{\Phi_d\}$"; status cell updated "$d=2,3$ proved on objects; functoriality on morphisms conjectural all $d$ (Conjecture~\ref{conj:phi-d-functoriality})"; scope cell now reads $\Phi_d\colon \CY_d\text{-}\Cat \to \En\text{-}\mathrm{ChirAlg}(\cM_d)$ with "$d$-indexed target" appended. | AP247 heal |
| F7 | HEALED | Vol I `CLAUDE.md:565` FM43 rewritten from "E_n output scope of CY-to-chiral Φ" to "E_n output scope of the CY-to-chiral correspondence programme {Φ_d}: Φ_1 lands in E_∞-chiral (d=1), Φ_2 lands in E_2-chiral (d=2), Φ_d lands in E_1-chiral (d≥3). The target E_{n(d)}-ChirAlg(M_d) varies with d, so {Φ_d} is NOT a single functor (AP247 + AP244); it is a d-indexed family of per-d constructions. Counter: always state per-d scope ... Canonical home: Vol III chapters/theory/cy_to_chiral.tex thm:phi-platonic + rem:phi-not-unified-functor + conj:phi-d-functoriality." AP5 cross-volume alignment with Vol III CLAUDE.md:19,28,87,88,123 (already healed) achieved. | AP247 heal + AP5 propagation |
| F8 | DEFERRED | working_notes.tex is not typeset into the PDF; AP247 discipline unaffected. Flag for a future working-notes sweep; not in critical path. | info |
| F9 | ALLOWED | Python engine module names `cy_to_chiral_functor.py` are stable identifiers; renaming breaks imports across ~570 engines. Engine-catalogue typeset tables inherit module names. CLAUDE.md metadata-hygiene exception applies. | out of scope |
| F10 | DEFERRED | Eleven example-chapter / notes sites carry "CY-to-chiral functor Φ_d" usage. Individually AP247-compliant-at-fixed-d (Φ_d with d specified IS a functor to a fixed target). Second-pass propagation heal — non-blocking, defer to dedicated terminology-sweep wave. | low-priority |

## Commit plan

No commits in this session per task constraints. Heals applied in-place to four files:

1. `/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex` (lines ~1638–1640, 1648, 1661–1664, 1671 — four edits).
2. `/Users/raeez/calabi-yau-quantum-groups/appendices/notation.tex` (lines 234, 356 — two edits).
3. `/Users/raeez/calabi-yau-quantum-groups/main.tex` (line 922 — one edit).
4. `/Users/raeez/chiral-bar-cobar/CLAUDE.md` (FM43 line 565 — one edit).

Pre-commit gates (when commit lands in a future session):

- Build: `pkill -9 -f pdflatex; sleep 2; make fast` in both Vol I and Vol III (1660 edits since last build noted in hook).
- Grep gates:
  - `grep -rn 'CY-to-chiral functor \$\\Phi\$\|the functor $\\Phi \\colon' chapters/ standalone/ main.tex appendices/` in Vol III — zero hits outside engine-module-name contexts.
  - `grep -rn '\\Phi\\s*\\colon\\s*\\CY_d' chapters/ standalone/ main.tex appendices/` in Vol III — every hit must carry the $d$-index or appear inside `\{\Phi_d\}_{d \ge 1}` braces.
  - Vol I CLAUDE.md FM43 grep: `grep -n 'CY-to-chiral Φ\|CY-to-chiral correspondence programme' CLAUDE.md` — AP247-compliant formulation only.
- AP5 cross-volume check: Vol II carries no Φ inscription of its own (Vol II uses CY side only through Vol III reference); Vol I references Φ only at FM43. Scope of AP5 propagation contained.
- Metadata hygiene (CLAUDE.md Manuscript Metadata Hygiene, constitutional zero-tolerance): AP247 / AP244 / AP288 tokens are banned from typeset prose. All inscribed heals carry mathematical substance ("$d$-indexed", "target varies with $d$", "not a single functor in the standard category-theoretic sense") without catalogue labels. Clean.

## Residual frontier

- Mukai-transform K3→K3 chain-level verification: the ONLY concrete morphism pair named as the "first test case" for conj:phi-d-functoriality at d=2. Until inscribed, AP247 sub-check (c) "composition verified on a concrete morphism pair" is OPEN for Φ_2. Healing path: inscribe prop:phi2-mukai-transform with chain-level chiral-algebra morphism Φ_2(FM_E) where FM_E is the Fourier–Mukai transform associated to the universal sheaf on K3 × K3.
- A_n-McKay → A_{n'}-McKay reduction under Z/n ↪ Z/n' at d=3: second concrete test case for conj:phi-d-functoriality, flagged open in the conjecture body.
- Working-notes propagation (F8) + example-chapter propagation (F10): non-blocking, defer.
- The CY-to-chiral engine module name `cy_to_chiral_functor.py` (F9) retains the legacy "functor" label for Python-identifier stability; any future engine-catalogue rename would propagate across ~570 engine files and is intentionally deferred.

## Cross-link to programme memory

- AP247 (Vol I CLAUDE.md:852): prospective forward-check for single-target functoriality discipline.
- AP244 (Vol I CLAUDE.md:833): retrospective diagnostic for overcounted foundational terms / terminological inflation. The Φ-as-functor claim was AP244's canonical example at the programme level; AP247's heal retired it.
- AP288 (Vol I CLAUDE.md:1005): session-ledger stale narrative. The preface late-section regression to singular "functor" while the preface front section uses correspondence-programme framing is a within-single-file instance of AP288 — heal pattern applies identically (rectify the stale section to match the canonical front).
- Vol III CLAUDE.md:19,28,87,88,123: already healed (commit prior to this wave). Vol I FM43 now matches Vol III discipline — AP5 propagation closed.
