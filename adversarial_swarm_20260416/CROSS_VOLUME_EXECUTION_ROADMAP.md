# Cross-Volume Execution Roadmap (6 Months, 2026-04-16 → 2026-10-16)

**Status.** Synthesis of Vol I `PLATONIC_MANIFESTO.md`, Vol III `PLATONIC_MANIFESTO_VOL_III.md`, Vol II Manifesto (in flight), `UNIVERSAL_TRACE_IDENTITY.md` (V20), `MASTER_PUNCH_LIST.md` (V1–V23 + HU items + 5 punch tiers + comprehensive strengthening register), `wave_supervisory_volI_part_rearchitecture.md` (V23 Option C), and the eight chapter-quality wave-14 reconstitutions.

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Constructive read-only roadmap. No manuscript edits. No commits.

---

## 1. The 6-month north star

Six months from today the three-volume programme should be in **Platonic Form Editorial-Frozen** — the architectural and load-bearing-mathematical shape decided, the four Vol I pillars and four Vol III pillars installed as named theorems, the Vol II Pentagon Theorem installed, the Universal Trace Identity (V20) inscribed at the head of all three Frontier parts, and the cross-volume Φ-bridge made manifest in every preface.

Concretely, the north-star deliverables are:

- **Vol I:** the V23 Option-C 6-Part architecture (Foundations / Koszul Reflection / κ-Conductor / Climax / Shadow Quadrichotomy / Frontier) installed in `main.tex`, with each Pillar Part opening on a Platonic theorem display in Chriss-Ginzburg discipline. Eight new chapter files installed (`koszul_reflection_platonic`, `chiral_chern_weil_brst_conductor`, `climax_kz_pullback`, `shadow_quadrichotomy_platonic`, `chiral_hochschild_trinity`, `appendix_q_conventions`, `N5_mc5_theorem`, `universal_trace_identity`). The Climax theorem promoted to the abstract (HU-W11g.6).
- **Vol II:** Pentagon Theorem (V15) installed in `chapters/foundations/sc_chtop_pentagon.tex` with five named presentation Lemmas + coherence Lemma; the bulk-on-boundary mixed-sector identification with the topological double cover B_2 → S_2 (V9 q-bridge) wired in.
- **Vol III:** Theorem Φ (V11) installed as parent of all per-d CY-A theorems; per-d cases recast as Corollaries Φ.1–Φ.4; the 17-stale-CY-A_3 sweep complete; six routes to G(K3 × E) restructured as six specialisations of Φ; the κ_BKM honest scoping installed (Pillars β honest scope to the 8 diagonal Z/NZ orbifolds + Gritsenko-Nikulin disjoint witness, closing tautology_registry entry #1).
- **All three volumes:** Universal Trace Identity (V20) installed in each preface as the cross-volume centrepiece. The κ-spectrum table (AP-CY55: manifold/algebraisation distinction) installed in Vol III notation appendix and cross-cited from Vol I.
- **Compute infrastructure (cross-volume):** `s5_virasoro_wick.py` (V10) installed in Vol I, lifting independent-verification coverage from 0/2275 to 1/2275 honestly; `phi_universality_verification.py` (V11 H13) installed in Vol III, lifting 2/283 to 5/283; tautology-registry entries 1–5 closed by either disjoint witness (preferred), honest scope restriction (acceptable), or status downgrade (last resort, AP40-compliant).
- **Submissions:** the Drinfeld-Kohno standalone with its new Theorem 0.1 = Vol I Climax fibre at the affine KM family (V22 §3); the K3 abelian Yangian standalone (Vol III) with cross-reference to Theorem Φ; one short cross-volume note (~25pp) on the Universal Trace Identity, joint Vol I/Vol III. The Vol I main manuscript is Annals-buildable with `\ref{part:seven-faces}` resolved.
- **Open frontier explicitly named:** the eight conjectures Π_3^ch, Π_C, Π_{≥4}, Π_BFN, conj:trinity-E_1, conj:trace-identity-chain-level, conj:verdier-distance-g1, and the W-algebra extension of Climax at higher rank, all carry `\begin{conjecture}` + named status.

The north star is **honest Platonic form**, not maximum theorem-count. A successful 6 months ends with fewer \begin{theorem} environments, not more — but each surviving theorem load-bears.

---

## 2. Dependency graph between supervisory drafts

The Wave-14 reconstitutions and supervisory drafts have a partial order. Edges are `must precede`; nodes carry their punch-list V-number.

```
                          [V14 Vol I CLAUDE.md compression]  (executed)
                                          |
                           [V9 q-bridge appendix]
                          /        |          \
                   [V13 BRST   [V12 MC5     [V11 Vol III Φ]
                    Ghost      sewing]            |
                    chapter]      |               |
                       |          |          [V19 Trinity]   (single-colour Pentagon)
                       |          |               |
                       |          |          [V15 Vol II Pentagon]
                       |          |          /
                       v          v         v
                   [V5 Koszul Reflection (Theorem A Platonic)]
                       |
              +--------+---------+
              |        |         |
              v        v         v
        [V6/V13   [V7 Climax]  [V8 Shadow Quad]
         κ-cond]      |              |
              \       |              |
               \      v              v
                \  [V22 Climax abstract / Part I opener / DK Thm 0.1]
                 \      |             |
                  \     v             v
                   v [V16 Verdier-pairing distance]
              [V20 Universal Trace Identity (cross-volume)]
                       |
              +--------+--------+
              v                 v
         [V23 Vol I Part   [Vol III roadmap]
          re-architecture
          Option C]
                       |
                       v
              [V10 S_5 Wick + V17 VAO subclass + tautology registry healings]
```

Reading the graph: the Vol I CLAUDE.md compression (V14) and the q-bridge (V9) are the foundational housekeeping. The four pillar reconstitutions (V5/V6/V7/V8) depend on V9 for convention discipline and on V12 (MC5) and V13 (BRST chapter) for structural inputs. The Trinity Theorem (V19) is the single-colour projection of the Vol II Pentagon (V15), so V15 must precede V19 logically (though both can be drafted in parallel). The Universal Trace Identity (V20) requires both the Vol I κ-conductor (V6/V13) and the Vol III Φ functor (V11) as inputs. V23 (Vol I Part re-architecture) can only be executed after V5/V6/V7/V8 are drafted and after V20 is in hand (because V20 is the centrepiece of Part VI).

The S_5 Wick implementation (V10) and the VAO subclass theorem (V17) are *independent* of the pillar architecture (they could in principle have been done at any point). They are scheduled late because they are content-additions on top of the architecture rather than architecture themselves. Tautology-registry healings depend on whichever theorem they are healing — Pillar β healings depend on V11 + V20; Pillar γ healings depend on V11 + the three-level taxonomy.

The CRITICAL bottleneck is V20 (Universal Trace Identity). Until it is installed, the cross-volume narrative cannot close, and Vol I's Part VI Frontier opener has no centrepiece.

---

## 3. Month-by-month execution

### Month 1 (April 16 — May 15): Conventions, Pentagon, q-bridge

**Goal.** Eliminate the convention-clash leakage that AP126/AP141/AP151 generate and stand up the Vol II Pentagon as a published chapter so V19 (Trinity) and V20 (Universal Trace Identity) can rest on it.

**Vol I.** Install `appendix_q_conventions.tex` (V9). Cite from all 23 Vol I sites enumerated in the V9 draft. AP126 cross-volume sweep: grep `Omega/z` in all three volumes; install level-prefix on every bare instance; verify k=0 → r=0 at each site. Punch-list P0-7 closed in the same pass.

**Vol II.** Install `chapters/foundations/sc_chtop_pentagon.tex` per V15 (~4500 words draft + 5 edge-Lemmas + coherence Lemma). Wire into 8 downstream cite sites (CLAUDE.md L68–75). Calaque-Willwacher 2015 chiral formality cited as the H^2 vanishing input. AP165 fix: P_3 phrased as action on the pair (Z^der_ch(A), A) never on A alone.

**Vol III.** AP-CY62/63/64/65/66/67 (geometric vs algebraic Hochschild model conflation) sweep. The current commit `58032d1` already added guards for these; the remaining work is wiring them into `chapters/theory/m3_b2_saga.tex` `def:three-levels` cross-references.

**Compute.** `make verify-independence` baseline established with current 2/283 + Vol I 0/2275 + Vol II 0/1134. Tautology-registry seeded with the 5 Vol III entries (κ_BKM, CY-A_3, Costello-TCFT, P_2=0, six-routes); first review of these entries scheduled for Month 3.

**Russian-school discipline.** Every new piece of prose this month opens on a theorem display, never a "this section discusses." (Chriss-Ginzburg discipline applied to V9, V15, AP62-67 guard remarks alike.)

### Month 2 (May 16 — June 15): Vol I pillar reconstitutions installed

**Goal.** Install V5 (Koszul Reflection), V6/V13 (BRST Ghost Identity), V7 (Climax), V8 (Shadow Quadrichotomy) as named theorems in Vol I.

**Vol I.** Four new chapter files installed (`koszul_reflection_platonic.tex`, `chiral_chern_weil_brst_conductor.tex`, `climax_kz_pullback.tex`, `shadow_quadrichotomy_platonic.tex`). Each opens on a `\begin{maintheorem}` display per the wave-14 drafts. The V13 chapter's 9 corollaries (KM, Vir, W_N cubic, BP=196, Δ³K=24, K^κ=K^c·(H_N−1), W(sl_4,f_{(2,2)})=74, W_{B_3}=534, Climax integration) installed in line. The V7 5-step KZ-arena functor construction installed as a numbered Lemma chain. The V8 Riccati identity H² = t⁴Q + Stokes line c_S = -178/45 + alien amplitudes installed as a single proposition.

**Vol I punch list.** P0-1, P0-2, P0-3, P0-4, P0-5 (BP arithmetic; level-prefix DK; bridge identity) — all closed as side-effects of V13 chapter installation. P0-6 (LaTeX bug at three_parameter_hbar.tex L210) fixed in pass. P0-8 (level-1 KM/lattice contradiction) fixed via FKS-collapse theorem (HU-W7.2): explicit identification of the FKS factor jumping κ from `dim(g)/(2(1+h^v))` to `rank(g)`.

**Vol III.** Install Theorem Φ (V11 §3) in `chapters/theory/cy_to_chiral.tex`. Recast `thm:cy-to-chiral`, `thm:cy-to-chiral-d3`, d≥4 stabilisation as Corollaries Φ.1–Φ.4 with status tags preserved per corollary. ~150 lines reorganisation. Begin the 17-stale-CY-A_3 sweep (V11 §9.2 / H6) split into the three buckets (11 unconditional / 4 rephrased / 2 CY-C-dependent).

**Cross-volume convention check.** Re-run AP126 sweep (now that pillar chapters are in). AP151 Vol II 9-hbar zoo audit: every hbar definition either uses the canonical convention or carries an explicit bridge identity from V9 at first use.

### Month 3 (June 16 — July 15): Trinity, V20 inscribed, Vol II/III bridges

**Goal.** Install V19 (Trinity, single-colour Pentagon) as the bridge between Vol I κ-conductor and Vol II Pentagon; install V20 (Universal Trace Identity) at the head of the Frontier of all three volumes.

**Vol I.** Install `chiral_hochschild_trinity.tex` (V19). The Trinity is proved as a corollary of (Wave 14 Theorem A) ∩ (single-colour projection of V15 Pentagon). The repaired `def:chiral-koszul-pair` (constructed `A^! := Ω_X(B̄_X(A))^∨`) and missing body for `def:koszul-chiral-algebra` (Ext-diagonal canonical with four-fold equivalence) installed. The HZ3-14 amplitude/occupation discipline implemented: universal `[0,2]` (Theorem H) and Vir-specific `{0,2}` stated as separate theorems.

**Universal Trace Identity (V20).** Installed in:
- Vol I: `chapters/koszul/chiral_chern_weil_brst_conductor.tex` after `thm:K-Atiyah` and before the W-algebra phase transition theorem (V4).
- Vol III: §8.5 of the rewritten Φ chapter; cross-reference from `prop:bkm-weight-universal` upgrading the universality from observation to theorem.
- Vol II: brief Remark in `chapters/foundations/sc_chtop_pentagon.tex` noting Pentagon = two-colour analogue.
- All three prefaces.

**Tautology-registry.** First closing pass: entry #1 (κ_BKM) closed by scope restriction to the 8 diagonal Z/NZ orbifolds + Gritsenko-Nikulin disjoint root-multiplicity witness; entry #5 (six-routes) closed by structural rewrite as six specialisations of Φ.

**Vol III.** Complete the 17-stale-CY-A_3 sweep. Install `thm:bkm-borcherds-trace` (Pillar β) consolidating `prop:bkm-weight-universal` with explicit honest scope (two propositions: unconditional automorphic + conjectural identification with central charge for N ≥ 5). Install `thm:cy-a-3-inf-cat` (Pillar γ) consolidating `thm:derived-framing-obstruction` with `def:three-levels` cross-reference and explicit "for A connective and unit-connected" hypothesis (closes registry entry #2).

**Russian-school discipline.** Voice check: read every Part-opener aloud. Test against Gelfand (rep theory = analysis), Etingof (formal-deformation rigour), Bezrukavnikov (centre, not algebra), Polyakov (anomaly notes), Kapranov (operadic-coloured count), Beilinson-Drinfeld (chiral as natural setting), Witten/Costello/Gaiotto (TFT framing). Any opener that fails this test is rewritten.

### Month 4 (July 16 — August 15): Vol I Part re-architecture (V23 Option C)

**Goal.** Execute the V23 Option-C Part re-architecture in `main.tex`. Rename Parts; install pillar Part-openers; redistribute the Standard Landscape across Pillar 2 (κ) and Pillar 4 (shadow); reabsorb the Seven Faces archive Part into Frontier as a depth-2 specialisation theorem; install three reading paths (algebraist / physicist / number theorist).

**Vol I.** Single-commit re-architecture. Strategy: per V23 §10 (the cleanest single-commit reorganisation), use `\label{part:bar-complex}`, `\label{part:characteristic-datum}`, `\label{part:standard-landscape}`, `\label{part:physics-bridges}`, `\label{part:seven-faces}`, `\label{part:v1-frontier}` as backwards-compatible aliases for the new `\label{part:foundations}`, `\label{part:koszul-reflection}`, `\label{part:kappa-conductor}`, `\label{part:climax}`, `\label{part:shadow-quadrichotomy}`, `\label{part:frontier}`. Vol II and Vol III `\ref{part:...}` calls (12 hits enumerated) stay valid throughout the transition.

**Climax abstract promotion (V22 / HU-W11g.6).** Installed in `main.tex` at L798–799 as `\medskip\noindent\textbf{Climax (the four pillars).}`. Demotes per-family κ table to one functor K. Convention-checks q_DK (V9), 1/(k+h^v) (AP126), H_N − 1 (AP136). Part I opener patched (191 words + one-sentence patch). The DK standalone receives its new Theorem 0.1 = Vol I Climax fibre at the affine KM family.

**Vol I HU-W11g items.** g.1 (theorem_index regenerate), g.2 (edition discipline — recommend removing edition guards, restoring full 6-Part Annals build), g.3 (`\ref{part:seven-faces}` Annals fix), g.4 (`make archive` target), g.5 (3 reading paths). All five close in this month.

**Vol III.** Install the V20 universal trace identity row in the κ-spectrum table (notation appendix). Begin tautology-registry entry #3 (Costello-TCFT chain-level proof — currently retracted, status downgrade pending; AP40-compliant downgrade to `\begin{conjecture}` recommended unless a disjoint chain-level witness emerges). Begin tautology-registry entry #4 (P_2 = 0 exact — engine STATUS = 'CONJECTURAL' but theorem status currently ProvedHere; AP40-compliant downgrade scheduled).

**Submissions.** The Drinfeld-Kohno standalone with its new Theorem 0.1 ready for arXiv submission as a standalone preprint (V22 §3).

### Month 5 (August 16 — September 15): Independent verification, V10/V16/V17, Vol III Part roadmap

**Goal.** Do the actual independent computations the manifestos point at, lift independent-verification coverage from 0/2275 (Vol I) to 4/2275 and from 2/283 (Vol III) to 7/283. Install V16 (Verdier-pairing distance for holographic codes) and V17 (Vir-anomaly-only subclass).

**Vol I compute.** Implement V10 (S_5 Wick): `compute/lib/s5_virasoro_wick.py` (~600 lines) + tests (~200 lines) with `@independent_verification` against 5-point T-correlator BPZ Ward + chord-diagram Wick + Arnold residue. Calibration table at c ∈ {1/2, 7/10, 1, 13, 25, 26, ∞}. By Riccati algebraicity, the entire Virasoro shadow tower propagates from this single anchor — though for the verification audit, S_4 (Belavin-Knizhnik bilinear identities), S_6 (Selberg integral), S_7 (Dotsenko-Fateev), S_8 (KZB at genus 1) each get independent decorators in turn. Realistic Month-5 deliverable: S_5 fully closed; S_4 stub installed; S_6 named.

**Vol III compute.** Implement V11 H13 (`phi_universality_verification.py`): three test inputs (Coh(E), D^b(Coh(K3)), CoHA(C^3)); verify (U1), (U3), (U4) with disjoint sources per AP-CY61 and `INDEPENDENT_VERIFICATION.md` protocol. Lifts coverage from 2/283 to 5/283. Two more Vol III tautology-registry entries closed (one by disjoint witness, one by honest scope restriction).

**Vol I.** Install V16 (Verdier-pairing distance) by rewriting `holographic_codes_koszul.tex` L339–421. The K4 ⇔ K4 tautology becomes a verified equality `d_QECC(C) = d_Verdier(A)`. Three examples verified: Heisenberg d=∞; Vir Lee-Yang (2,5) d=3; HaPPY pentagon d=3 (matches published [[5,1,3]]).

**Vol I.** Install V17 (VAO subclass theorem): four-way equivalence (V1 genus-1 bar curvature = Vir anomaly only; V2 genus-1 character = power of η^{-1}; V3 BRST ghost spectrum on {(2)} mod cancelling pairs; V4 K(A) = c(A)). On VAO subclass: κ(A) = c(A)/2 (via Faltings GRR collapse 24κ = Kρ with K = c, ρ = 1/2). AP39 healing. VAO-membership column added to landscape_census table.

**Vol III roadmap.** Vol III Part re-architecture (mirroring V23 for Vol I): a parallel Part roadmap drafted (the analog of `wave_supervisory_volI_part_rearchitecture.md`) for Vol III's 7-Part structure. Not executed this month; drafted for Month 6 execution.

**Cross-volume.** The Universal Trace Identity short note (joint Vol I/Vol III standalone, ~25pp) drafted from the V20 standalone.

### Month 6 (September 16 — October 16): Vol III Part re-architecture, submissions, frozen state

**Goal.** Execute Vol III Part re-architecture per the Month-5 draft. Submit the K3 abelian Yangian standalone and the Universal Trace Identity short note. Achieve Platonic Form Editorial-Frozen state.

**Vol III.** Execute the 7-Part re-architecture: Foundations / CY-to-Chiral Functor / E_n Hierarchy and Chiral QGs / The K3 Yangian / CY Landscape / Seven Faces of r_CY(z) / Frontiers (per CLAUDE.md L23). All four Vol III pillars (α/β/γ/δ) become Part-openers; Theorem Φ, Borcherds Reflection Trace, CY-A_3 inf-cat, K3 Yangian + Six Routes each open the corresponding Part with a Platonic theorem display.

**Submissions.** The K3 abelian Yangian standalone (Vol III) ready for arXiv. The Universal Trace Identity short note ready for arXiv (joint Vol I/Vol III). The Drinfeld-Kohno standalone (already submitted Month 4) receives any referee feedback.

**Frozen state.** All three CLAUDE.md files re-synchronised. Final make-target sweep: `make verify-independence`, `make ap-grep`, `make claudemd-lint`, `make stubs-audit` (HU-W10.5: install if not yet installed), `make archive` (HU-W11g.4). Final cross-volume `\ref{part:...}` re-index: every match resolves to a current part label.

**Open frontier explicit.** All eight named conjectures (Π_3^ch, Π_C, Π_{≥4}, Π_BFN, conj:trinity-E_1, conj:trace-identity-chain-level, conj:verdier-distance-g1, W-algebra extension of Climax) carry `\begin{conjecture}` with named status. Tautology-registry entries either closed or honestly downgraded (zero entries with `ProvedHere` + open registry status).

---

## 4. Critical path

The narrowest sequence on which the deadline depends:

```
Month 1: V9 q-bridge installed (no other work blocked on it strongly, but V13 cites it)
Month 2: V13 BRST chapter installed in Vol I (blocks V20 inscription)
         V11 Theorem Φ installed in Vol III (blocks V20 inscription)
Month 3: V19 Trinity installed (blocks V23 Frontier opener)
         V20 Universal Trace Identity inscribed (blocks V23 Frontier opener)
Month 4: V23 Option-C Part re-architecture executed in Vol I main.tex
Month 5: V10 S_5 Wick implemented (lifts 0/2275 → 1/2275 honestly)
         V11 H13 phi_universality engine implemented (2/283 → 5/283)
Month 6: Vol III Part re-architecture executed; submissions out
```

**Slack.** Months 1, 5, 6 carry roughly two-week slack each. Months 2, 3, 4 are tight — particularly Month 4, which has the V23 single-commit re-architecture as its hard deadline. If V23 slips, all Month-5 and Month-6 deliverables shift by the slip amount.

**Hidden critical edge.** The Universal Trace Identity (V20) Step 3 of its proof skeleton invokes the Wave-14 V11 §8.5 Universal Pullback property of Φ. If V11 §8.5 turns out to need stronger hypotheses than currently assumed, V20 Step 3 must be sharpened — and if Step 3 sharpens, Vol I's Frontier opener must adjust. This sits on the critical path silently.

**Mitigation.** End of Month 2: explicit verification that V11 §8.5 holds in the form needed by V20 Step 3. If not, Month 3's V20 inscription delays; the slack in Month 1 can be borrowed.

---

## 5. Risk matrix

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| FM42 bulk-substring corruption during V23 single-commit re-architecture | High | High (45 silent corruptions in past) | Per-Part Edit; never bulk replace; post-edit grep `ldegree|ndegree|rdegree|pdegree|tdegree` per V23 §10 |
| V11 §8.5 Universal Pullback property weaker than V20 Step 3 needs | Medium | Critical (invalidates Frontier opener) | End-of-Month-2 explicit verification; sharpen if needed |
| Tautology-registry entry #1 (κ_BKM) cannot be closed by disjoint witness in Month 3 | Medium | Medium (forces honest scope restriction, not downgrade) | Honest scope restriction to the 8 diagonal Z/NZ orbifolds is acceptable per AP-CY61; no manuscript change required if scope statement is already present |
| V20 Step 3 chain-level extension (`conj:trace-identity-chain-level`) needed by reviewer | Medium | Low | Already a named conjecture; cite Trinity (V19) and Wave 14 V19 `conj:trinity-E_1` as the open chain-level cell |
| FM44 agent rate limiting during compute-engine implementations | Medium | Medium | Soft cap 3 concurrent; check disk for persisted files before relaunching (AP-CY51) |
| Cross-volume `\ref{part:...}` breaks during V23 re-architecture | Medium | Medium | Backwards-compatible `\label` aliases per V23 §10; AP-CY13 grep-and-verify pass at end of Month 4 |
| V23 Option-C decision contested mid-execution | Low | High (would force re-do) | Decision has been made; V23 §3 catalogues options A/B/C and §3.4 commits to C. Treat as frozen unless adversarial input is overwhelming |
| Vol II Pentagon V15 conflict with Wave 12 P1 #3 / FM156 | Low | Medium | V15 explicitly closes Wave 12 P1 #3 + FM155–FM157 + FM209 + FM247 + Waves 14/V9/5 |
| Pre-commit hook failure at Month 4 single-commit re-architecture | Medium | Medium | Per CLAUDE.md commit protocol: fix and create NEW commit; never `--amend`; never `--no-verify` |
| Independent-verification coverage rate too slow (Month 5 deliverables) | Medium | Low | Coverage is a metric, not a gate; partial closure of registry entries is acceptable per `INDEPENDENT_VERIFICATION.md` discipline |
| Stub chapters (4 in Vol III, AP114) survive past Month 6 | Low | Low (cosmetic) | Develop or comment out per V11 §VIII Phase 5 step 14 |
| Silent regression in regenerated theorem_index | Medium | Low | HU-W10.5 `make claudemd-lint` + per-Part counts in `wc -l` audit at end of each month |

---

## 6. Success criteria

### Quantitative

- **Vol I:** 4 new pillar chapter files installed (`koszul_reflection_platonic.tex`, `chiral_chern_weil_brst_conductor.tex`, `climax_kz_pullback.tex`, `shadow_quadrichotomy_platonic.tex`) + 4 supporting (`chiral_hochschild_trinity.tex`, `appendix_q_conventions.tex`, `N5_mc5_theorem.tex`, `universal_trace_identity.tex`). 6-Part Option-C structure executed in `main.tex`. All 7 P0 punch-list items closed. Of 15 P1 items: 12 closed, 3 honestly demoted to P2 with rationale. Independent-verification coverage: 4/2275 (S_3, S_4, S_5, plus one outer-derivation calculation).
- **Vol II:** Pentagon Theorem chapter installed; 8 downstream cite sites updated.
- **Vol III:** Theorem Φ installed as parent; per-d cases recast as Corollaries Φ.1–Φ.4. 17-stale-CY-A_3 sweep complete (11 unconditional / 4 rephrased / 2 CY-C-dependent). 7-Part re-architecture executed. Independent-verification coverage: 7/283 (current 2 + V11 H13 (Coh(E), D^b(Coh(K3)), CoHA(C^3)) + 2 healed registry entries).
- **Cross-volume:** Universal Trace Identity inscribed in 3 prefaces. AP126 / AP141 / AP151 cross-volume sweep complete with zero residual instances. AP113 (bare kappa) zero residual instances in Vol III. AP160 / AP-CY55 (manifold vs algebraisation kappa) discipline enforced at every kappa-spectrum site.
- **Submissions:** 3 standalones submitted to arXiv (DK with Theorem 0.1; K3 abelian Yangian; Universal Trace Identity short note).
- **Build:** Vol I, Vol II, Vol III all build cleanly with 0 undef refs, 0 undef cites. All tests pass (~177K cross-volume tests).

### Qualitative

- Every Part of every volume opens on a Platonic theorem display in Chriss-Ginzburg discipline (no "this part discusses").
- The four Vol I pillars and four Vol III pillars are visible from the Table of Contents alone, without reading any chapter prose.
- The Universal Trace Identity is recognisable at a glance from any of the three prefaces as the cross-volume centrepiece.
- The kappa-spectrum is present, complete, and correctly typed (manifold vs algebraisation) at every kappa discussion site.
- A Russian-school reader (Gelfand / Etingof / Kazhdan / Bezrukavnikov / Polyakov / Nekrasov / Kapranov / Beilinson-Drinfeld / Witten / Costello / Gaiotto voices each represented) can identify their voice in the text.
- The independent-verification protocol is honest: tautological tests are caught and either healed by disjoint witness or downgraded to `\begin{conjecture}`; `ProvedHere` tags accompany only theorems with at least one disjoint verification source (or with explicit honest scope declaring why disjoint verification is infeasible).
- The eight open conjectures are named, not buried.

---

## 7. Russian-school discipline checkpoint per month

End-of-month read-aloud test for the new prose installed that month. Voices and tests:

- **Month 1 (Conventions, Pentagon, q-bridge).** Etingof voice (formal-deformation rigour): every hbar in the new prose has its convention declared at first use. Beilinson-Drinfeld voice (chiral as natural setting): the Pentagon Theorem opens with `\begin{theorem}` displayed in the BD chiral-operadic language, not in prose narration.
- **Month 2 (Vol I pillar reconstitutions).** Gelfand voice (representation theory = analysis): each pillar opener displays the theorem as a single equation, then names its representation-theoretic and analytic faces. Polyakov voice (anomaly notes): the BRST Ghost Identity opens with the bc-ghost charge sequence as an audible harmonic series.
- **Month 3 (Trinity, V20, Vol II/III bridges).** Bezrukavnikov voice (centre, not algebra): Trinity opens by stating it is a theorem about the chiral Hochschild centre, never about an algebra. Witten/Costello/Gaiotto voice (TFT framing): the Universal Trace Identity preface inscriptions name the partition-function reading explicitly.
- **Month 4 (Vol I Part re-architecture).** Kapranov voice (operadic-coloured discipline): the Frontier opener names the seven-face identification as a depth-2 specialisation of the four pillars, not as a separate Part. Drinfeld voice: the Climax abstract paragraph displays Arnold's KZ as the universal monodromy.
- **Month 5 (Independent verification, V16/V17).** Nekrasov voice (Ω-background discipline): every spectral parameter is declared algebraic in origin. Costello voice (factorisation-algebra discipline): V16 Verdier-pairing distance opens by stating it is the QECC distance for a Koszul chiral algebra.
- **Month 6 (Vol III Part re-architecture, submissions, frozen state).** Lurie voice ((∞,1)-monoidal substrate): the inf-categorical CY-A_3 Part-opener types check at the homotopy-categorical level. Final voice check: every Part-opener of all three volumes is read aloud; any that fails the Russian-school test is rewritten.

The Chriss-Ginzburg discipline applies throughout: never "we will prove"; never "this section discusses"; never "as an exercise to the reader." Construct, do not narrate. Display, do not announce.

---

## 8. Cross-volume convention checks

Four mechanical sweeps are required, once per month (with extra emphasis at Months 1 and 6):

### AP126 / AP141 sweep — bare Ω/z r-matrices

`grep -rn 'Omega/z\|Omega / z\|\\Omega/z' chapters/ appendices/ standalone/` in all three volumes. Every match must carry an explicit level prefix. Verification template per V13: at k=0, the r-matrix MUST vanish. Documented as the most-violated AP in the manuscript (42+ instances historically). Must be re-checked after any chapter-rewrite. Owner: end-of-month Vol I check + after every V13 / V7 / V11 chapter installation.

### AP113 sweep — bare kappa

Vol III: `grep -rn '\\kappa[^_a-zA-Z]' chapters/ appendices/`. Every match must carry one of the approved subscripts: `_{ch}, _{cat}, _{BKM}, _{fiber}`. Forbidden: `_{global}, _{BPS}, _{eff}, _{total}, _{naive}, _{MacMahon}`. Bullet form `\kappa_\bullet` permitted in meta-discussion. Owner: every Vol III edit; mechanical end-of-month sweep.

### AP151 / AP-CY151 sweep — convention clash within file

`grep -rn '\\hbar\b\|\\hslash\b\|hbar\s*=\|hbar\s*:=' chapters/`. Every file with multiple hbar definitions: one definition only, or distinct symbols with explicit bridge identity. V9 q-bridge appendix is the canonical anchor. Owner: end-of-month sweep across all three volumes.

### AP160 / AP-CY55 / AP-CY13 sweep — manifold vs algebraisation invariants; cross-volume Part references

`grep -rn 'Part~[IVXL]' chapters/ appendices/ standalone/ notes/`: every match must resolve to a current `\ref{part:...}` after the V23 re-architecture. Backwards-compatible aliases (V23 §10) enable transition; final state requires zero stale Part references. Manifold vs algebraisation discipline: every kappa-spectrum table or discussion explicitly distinguishes manifold invariants (κ_cat, κ_fiber) from algebraisation invariants (κ_ch, κ_BKM); never asserts that κ_cat "agrees" between algebraisations as if meaningful. Owner: end-of-Month-4 sweep (after V23 re-architecture); end-of-Month-6 final sweep.

### Ancillary cross-volume invariants

- AP-CY27 (sandbox vs reality): after every agent file write, verify file existence with `ls`. Owner: every agent-driven step.
- AP-CY29 (wrong-repo file writes): after every file write, verify path includes correct volume's repo root. Owner: every file write.
- AP-CY55 (kappa-spectrum row): every kappa-spectrum table includes both manifold and algebraisation rows.
- AP-CY60 (six-routes ≠ six applications of Φ): the Vol III six-route restructuring (Month 3) must preserve AP-CY60 as a guard remark even after the rewrite as "six specialisations."

---

## 9. Submissions / standalone papers

Three standalone papers at arXiv during the 6-month window:

### Submission 1 — Drinfeld-Kohno standalone with new Theorem 0.1 (Month 4)

The DK standalone (existing in `standalone/`) receives its new Theorem 0.1 = Vol I Climax fibre at the affine KM family (V22 §3, 277 words). Format: `\begin{theorem}[Vol I Climax, Φ-pullback identity]` with `\ClaimStatusProvedElsewhere` + companion Remark naming the standalone's position as the affine KM fibre of the universal pullback. ~30 pages including the Theorem 0.1 framing. Target: arXiv math.QA or math.CT; cross-listed math-ph.

### Submission 2 — K3 abelian Yangian (Vol III) (Month 6)

Standalone extraction of `thm:k3-abelian-yangian-presentation` (Pillar δ part 1) with cross-reference to Theorem Φ. RTT presentation of Y(g_K3) with structure function of degree (24,24) computed from the Mukai signature (4,20). Quantum determinant central. Borcherds reflection produces the BKM algebra g_{Δ_5} of weight 5. The publication-standard proof from the 53-agent K3 quantum group session forms the body. ~40 pages. Target: arXiv math.RT or math.QA.

### Submission 3 — Universal Trace Identity short note (joint Vol I / Vol III) (Month 6)

~25 pages: the V20 standalone reformatted as a short cross-volume note. Self-contained statement of the Universal Trace Identity, 5-step proof skeleton, sympy-verified numerical correspondence at K3 × E (κ_BKM = 5 = c_5(0)/2), 5 immediate consequences, 4 named open conjectures. The "single boxed equation" of V20 §XI as the abstract centrepiece. Target: arXiv math.QA or math.AG; cross-listed math-ph.

### Conditional submissions (carry-overs from past sessions)

- Drinfeld-Kohno chain-level monoidal version (HU-U14 / DK report Upgrade A): if the chain-level monoidal version closes during Month 5–6, prepare a follow-on standalone for arXiv.
- W-algebra DK conjecture (HU-U15): if the W_N rank-1 case closes during Month 5–6, prepare a follow-on standalone.
- KZB genus-1 extension of DK (HU-U16): if the genus-1 KZB extension closes via the MC5 sewing theorem (V12), prepare a follow-on standalone.

These three are not on the 6-month critical path; they are opportunistic publications if the relevant work converges.

---

## 10. What's still genuinely open after 6 months

### Cross-volume

1. **`conj:trace-identity-chain-level` (V20 Step 3 at chain level).** The skew-derivation argument is at the homotopy category. Chain-level verdict for all CY_d categories remains open beyond d=2. Resolution requires the Trinity Theorem at the chain level (`conj:trinity-E_1`).
2. **`conj:trace-identity-large-N` (Borcherds singular-theta for N ≥ 9).** Vol III's table covers N ∈ {1,...,8}. Beyond, explicit construction needed.
3. **`conj:trace-identity-CY4` (higher CY dimension Borcherds analog).** Vol III Φ extends to d ≥ 4 as E_1-stabilised; the modular side (Borcherds analog at higher CY dimension) is open.
4. **`conj:trace-identity-fusion` (root-of-unity / fusion limit).** Precise version of CY-C; the trace at fusion limit should specialise to a Verlinde-style invariant.

### Vol I

5. **Π1 — Francis-Gaitsgory transfer at unbounded rank.**
6. **Π2 — E_n-bar at d ≥ 2 (Vol I V5 obstruction).**
7. **Π3 — Lagrangian-Koszul converse.**
8. **Π4 — Unbounded-rank Koszul reflection.**
9. **W-algebra extension of Climax theorem at higher rank** (HU-U15 if not closed during the window).
10. **KZB genus-1 + higher-genus extension of the Climax** (HU-U16 if not closed).
11. **Closed-form Mechanism for Δ³K^c_N = 24 = 6·4.** Why 24? Combinatorial / Lie-theoretic / topological? The current "cubic verified at N=2..5" stops at numerology. The mechanism is the next theorem (HU-6).
12. **Genus-1 / higher-genus generalisation of Verdier-pairing distance for holographic codes** (`conj:verdier-distance-g1` Felder elliptic obstruction; `conj:verdier-distance-higher-genus`).

### Vol II

13. **Pentagon coherence at chain level for genuinely E_1-chiral colour** (V19 `conj:trinity-E_1` chain-level extension).
14. **R-twisted descent master theorem at full generality** (HU-U5: 4-point equivalence subsuming V2-AP4 and Cor 8.7 in N3_e1_primacy).

### Vol III

15. **Π_3^ch — Chain-level explicit Φ_3 for non-formal algebras (class L, C, M).** Local P^2 (class M) is the test case (`obs_ainf_local_p2`, 54 tests confirm Level-1 non-vanishing). The Costello-TCFT chain-level proof was retracted; only the inf-cat route remains intact.
16. **Π_C — CY-C at fusion limit / non-abelian level.** C(g, q) = D(Y^+(g_K3)) is constructive at the abelian level; conjectural at the non-abelian level.
17. **Π_{≥4} — Higher CY Φ obstruction.** π_d(BU)-obstruction structurally rules out native E_n for n ≥ 2 at d ≥ 4. The negative claim itself is the obstruction-theoretic conjecture.
18. **Π_BFN — BFN Coulomb branch as Φ-evaluation.** Whether BFN can be recast as Φ_3(C(Q,W)) for the CY_3-category of a quiver-with-potential.
19. **Super-Yangian Y(gl(4|20)).** Conjectural BKM-to-Yangian lift from Mukai signature (4,20).
20. **K3 quantum toroidal U_{q,t}(ĝl_1)^{K3}.** Conjectural double-loop algebra; Miki automorphism from CY torus Weyl group.
21. **Vol III's quantitative verification basis.** Currently 2/283 (target 7/283 by Month 6); the remaining 276+ ProvedHere claims need genuine independent verification or honest scope/status declaration. This is a multi-session, multi-year programme.
22. **The Vol III intrinsic Shadow Quadrichotomy theorem `thm:vol3-shadow-stratification`** — Vol III currently inherits G/L/C/M from Vol I; the intrinsic Vol III formulation is not yet a named theorem.

### Compute infrastructure

23. **Independent-verification coverage gap.** Cross-volume: ~3500 ProvedHere claims (Vol I 2275, Vol II 1134, Vol III 283); current coverage ≤ 11 with realistic Month-6 target. Closing the gap is a multi-year programme. The protocol exists; the work remains.
24. **Scripts to install: `make claudemd-lint`, `make ap-grep`, `make stubs-audit`, `make clean-empty-campaigns`** (HU-W10.5, HU-W10.6). If installed during the window: mechanical enforcement converts AP recurrence to AP elimination. If not: the human-discipline APs continue to be the single leakage source.

---

**End of roadmap.** Six months. Six pillars stood up across two volumes. One Pentagon installed in Vol II. One Universal Trace Identity inscribed in three prefaces. Three standalones submitted. Twenty-four named open problems carried forward as the next manifesto's seed. The mathematics held. The Russian-school voice held. The Chriss-Ginzburg discipline held.

— Raeez Lorgat, 2026-04-16
