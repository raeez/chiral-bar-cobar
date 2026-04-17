# Wave-9 AP Catalog Self-Audit (2026-04-18)

Per AP314 (inscription-rate outpaces audit capacity). Diagnostic only — no edits, no merges, no renumbering. The catalog is cross-referenced across sessions; premature compaction risks breaking agent behavior.

## Inventory

- **Bold-header APs** (`^\*\*AP[0-9]+`): 89 entries; 86 unique numbers; **3 duplicate numbers** collide.
- **Inline APs** (`^AP[0-9]+:` under "Anti-Patterns by Topic"): 144 entries.
- **Total AP tokens referenced in CLAUDE.md**: 263 lines carrying AP/AAP/FM/HZ-/V2-AP/AP-CY/RS- prefixes.
- **Highest AP numbers**: 305, 306, 307, 308, 309, 310, 311, 312, 313 (x2), 314, 315, 316, 320, 326, 340, 341, 360, 361, 362, 365, 421, 501, 502, 521, 524, 541, 602, 621, 622, 623 — non-contiguous; reserved blocks (AP421 MC4-swarm; AP501-502 Koszul/MC3; AP621-623 HZ-IV) leave dense gaps.

## Duplicate AP numbers (REAL collisions)

| Number | Title-A | Title-B | Verdict |
|---|---|---|---|
| AP287 | Structural-impossibility primitive tautology — HZ-IV-W8-B (l.902) | Cross-volume theorem existence without HZ-11 attribution (l.914) | **Hard collision** — second should be AP287'→next free |
| AP288 | Decorator-label vs test-body computation disjointness — HZ-IV-W8-C (l.904) | Session-ledger stale narrative (l.916) | **Hard collision** |
| AP313 | Proof via post-hoc prefactor normalization (l.976) | Truncated Agent-result masquerading as clean completion (l.980) | **Hard collision** — distinct patterns both valuable |

Also repeated internal references: `AP287` appears 11× across the document, `AP288` 11×, `AP313` 7× — repair must disambiguate every ref site before renumbering.

## Duplicate / near-duplicate *content* (same failure mode under distinct numbers)

1. **AP255** (phantom file + phantomsection mask) ≡ **AP286** (tactical phantomsection alias vs semantic heal) ≡ part of **AP264** (phantom `\ref{rem:foo}`) — three phantom-label variants. Merge candidate `ap:phantom-reference-family` with sub-rules (a)/(b)/(c).
2. **AP241** (advertised-but-not-inscribed) ≡ **AP249** (base-change cited not inscribed) ≡ **AP272** (unstated cross-lemma via folklore) ≡ **AP278** (moduli-space boundary asserted without construction) — all "citation-level claim, no inscribed body". Merge into `ap:citation-without-inscription` with tiered severity.
3. **AP256** (aspirational-heal status drift) ≡ **AP271** (reverse drift: manuscript ahead of CLAUDE.md) ≡ **AP305** (pessimistic CLAUDE.md drift) ≡ **AP300** (ProvedHere-vs-retracted-mechanism drift) — four drift directions of the same status/manuscript coupling. Merge `ap:status-manuscript-drift` with four explicit directions.
4. **AP277** (vacuous HZ-IV body) ≡ **AP287** (structural-impossibility primitive tautology) ≡ **AP288** (label-disjoint but body-identical computation) ≡ **AP310** (three paths bibliographically disjoint but shared intermediate) ≡ **AP622** (symmetry-invariance boolean True) ≡ **AP623** (Newton-identity disambiguation). Six HZ-IV-tautology variants — merge `ap:hz-iv-decoration-vacuity`.
5. **AP238** (statement/proof internal contradiction) ≡ **AP245** (statement-proof-engine numerical agreement) ≡ **AP312** (three-way cross-file scalar contradiction) — all "same symbol takes different values across LHS/proof/engine". Merge `ap:numerical-agreement-discipline`.
6. **AP40** (environment matches tag) ≡ **AP60** (ProvedHere only genuinely new) ≡ **AP227** (ProvedHere forwarding) ≡ **AP421** (standalone-only inscription claiming chapter inscription). Four tag-discipline variants; merge `ap:claim-status-tag-discipline`.
7. **AP239** (naming after physical source) ≡ **AP244** (overcounted foundational terms) ≡ **AP246** (signature type-assignment). Three naming-fidelity patterns; merge `ap:object-name-fidelity`.
8. **AP242** (forward-reference lemma) ≡ **HZ-11** (cross-volume ProvedHere) ≡ **AP287-B** (cross-volume theorem without attribution). Merge `ap:cross-volume-proof-chain`.
9. **AP280** (three-step epistemic inflation) ≡ **AP240** (closure-by-repackaging) ≡ **AP262** (hub-and-spoke TFAE scope inflation) ≡ **AP273** (admitted-redundant item in equivalence tally). Four scope/count-inflation patterns; merge `ap:scope-count-inflation`.
10. **AP264** (phantom `\ref{rem:}`) ≡ **AP265 variant** / AP264 companion (phantom `\cite{}`) ≡ **AP281** (bibkey naming drift at scale) ≡ **AP285** (alias section-number drift). Four citation-resolution patterns; merge `ap:citation-resolution-integrity`.
11. **AP293 / AP294 / AP295** (recovery infrastructure — prerequisite guard / file-size threshold / dashboard liveness). Per AP314's own example; merge `ap:recovery-infrastructure-pragmatics`.
12. **AP301 / AP302 / AP304 / AP308** (harness-level concurrency hazards — /loop interval, replace_all collisions, shared-file numbering collision, cron interleaving). Merge `ap:concurrent-agent-hygiene`.
13. **AP257** (engine-docstring vs manuscript) ≡ **AP282** (VERIFIED vs xfail) ≡ **AP128** (engine-test synchronized on wrong value) ≡ **AP315** (engine tolerance looser than physical scale). Merge `ap:engine-source-coupling`.

## Stale / superseded entries

- **AP18** ("entire standard landscape" → enumerate): effectively subsumed under AP7 + AP139 and the HOT ZONE HZ-3 weight-tag discipline.
- **AP47** (evaluation-generated core): subsumed by MC3 Wave-4 heal already propagated throughout the Theorem Status row; the pattern is now embedded in the table itself.
- **AP67** (strong vs free strong generator — W(p)): resolution partially now lives in B91 and W(p) Massey split (Wave-1 audit B91). Consider retag as historical.
- **AP76** (Y_{1,1,1} c=0, κ=Ψ): single-family numerical correction, no longer a live failure mode — retire or fold into census.
- **AP155** (new-invariant overclaiming): now superseded by AP280 + AP251 + AP273 trio.
- **AP186** (Opus coincidental agreement masks bugs): narrower restatement of AP128 + AP292 (operator-precedence bug).
- **AP187** (Miura coefficients via elementary symmetric expansion): solved positively via `thm:miura-cross-universality`; document as resolved not active pattern.
- **AP205** (reflexivity hidden in duality) / **AP206** (object switch mid-proof): both subsumed by AP195 (five-object conflation).
- **AP189** (dead labels): now subsumed by the stronger AP291 (systemic phantom-ref via self-disabled label).

## Recommended consolidation (defer execution)

Per AP314:
1. **Do not renumber existing APs.** 263 cross-reference sites means a global renumber is itself an AP149-propagation-failure hazard at scale.
2. **Mark duplicates `[COLLISION, use AP287-B label pending reconciliation]`** in-place: safer than renaming.
3. **Introduce content-addressed aliases** (`ap:phantom-reference-family`, `ap:hz-iv-decoration-vacuity`) alongside integer numbers; new inscriptions should reference the alias; legacy integer numbers preserved.
4. **Reserved-block audit** (AP306): AP316→AP360 has ~44 vacant slots; AP362→AP420 vacant; usage is bursty not dense. Before allocating AP317+, grep the programme-wide for "AP3[1-9][0-9]" usage including in agent notes outside CLAUDE.md.

## Commit plan for a future consolidation wave

Non-binding sketch — requires explicit user instruction before execution:

- **Phase 0 (read-only)**: cross-reference inventory. For each duplicate-number and merge-candidate group, grep all three volumes + `notes/` + `adversarial_swarm_*` + `memory/` for citing sites; produce a reference-count table.
- **Phase 1 (alias layer, additive)**: introduce content-addressed aliases in a new "AP Alias Table" section; existing integer-numbered entries unchanged. Zero break risk.
- **Phase 2 (collision-only rename)**: rename AP287-B → next-free slot (e.g. AP317), AP288-B → AP318, AP313-B → AP319; update every citing site in SAME commit (AP149 discipline). Three atomic commits, one per collision.
- **Phase 3 (stale retag)**: mark stale APs `[RESOLVED YYYY-MM-DD, retained for historical reference]`; do not delete.
- **Phase 4 (content merge)**: only after Phase 1 aliases have bedded in across ≥2 sessions of live agent use; merge into family entries; individual integers retained as "see: ap:family" pointers.
- **Never**: bulk renumber; bulk delete; in-session rewrite of >3 AP entries.

## Scope disclaimer

This audit is from within-CLAUDE.md pattern matching only. It does not cross-check agent notes under `adversarial_swarm_*/`, `notes/`, or Vol II/III CLAUDE.md mirrors where the same AP indices may carry divergent definitions — AP304 (concurrent-agent AP-numbering collision in shared metacognitive file) is the operational realisation of this risk. Full reconciliation requires the cross-volume AP table promised in AP253.
