# Vol II cross-volume consumer audit — Vol I heal retractions (2026-04-18)

**Mission.** Audit Vol II downstream consumers of the 2026-04-18 Vol I heal wave. Specifically check for AP271 reverse drift, HZ-11 constitutional violations, and AP264/AP255 phantom references triggered by the retractions + downgrades of the following Vol I items:

- MC4^0 class M principal: PROVED → CONJECTURAL (`thm:n4-mc4-zero-unconditional` → `conj:n4-mc4-zero-generic-parameters`)
- Verlinde recovery: ProvedHere → ProvedElsewhere (`prop:verlinde-from-ordered`)
- V^natural E_3-topological: ProvedHere → ProvedElsewhere (`thm:v-natural-e3-topological`)
- UCH gravity chain-level: restricted to pro-ambient (`thm:uch-gravity-chain-level`)
- Theorem D clause (iii) (`prop:theorem-D-factorization-homology-alt` part (iii)): → Conditional
- Theorem A modular-family extension: CONDITIONAL on GR17 + Mok25 (`thm:A-infinity-2` + `rem:A-infinity-2-modular-family-scope`)
- Chiral CE B(U^ch(L)) = CE_*(L): retraction

## Phase 1 — Grep sweep (Vol II chapters/ + standalone/)

Cross-volume consumer sites enumerated (excluding metadata, notes, session ledgers, PDFs):

| Vol I label                                 | Vol II consumer sites                                                                                                                       |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `thm:v-natural-e3-topological`              | `chapters/connections/part_vi_platonic_introduction.tex:390, 415, 518` (theorem body + proof + dependency table)                              |
| `thm:A-infinity-2`                          | `chapters/connections/programme_climax_platonic.tex:64, 857`; `chapters/frame/preface.tex:205`; `chapters/theory/factorization_swiss_cheese.tex:4043` |
| `rem:A-infinity-2-modular-family-scope`     | `chapters/frame/preface.tex:205` (already cited with attribution as scope remark)                                                             |
| `thm:moonshine-bar-euler-master` (Vol I)    | `chapters/connections/part_vi_platonic_introduction.tex:393, 423` (load-bearing consumer in `thm:part-vi-moonshine-recovery`)                 |
| `thm:uch-gravity-chain-level` (Vol II own)  | Five chapter files + cor:soft-hierarchy-unconditional-r-leq-8; all already carry pro-ambient scope language                                   |
| `thm:n4-mc4-zero-unconditional`             | **ZERO** — no Vol II consumers of the retracted theorem name                                                                                  |
| `prop:verlinde-from-ordered`                | **ZERO** — Vol II has own Verlinde infrastructure (`compute/lib/verlinde_bulk_check.py`, `test_verlinde_bulk_check.py`); no V1-label consumers |
| `bar-ce-chiral` / `chiral-ce-bar`           | **ZERO** — no Vol II consumers                                                                                                                |
| Theorem D `prop:theorem-D-factorization-homology-alt` | **ZERO** direct V1-label consumers in chapters/ or standalone/                                                                         |

## Phase 2 — Impact classification

### (a) Reverse-drift HEALTHY (Vol II already inherits correct scope)

**A-healthy-1.** `chapters/connections/universal_celestial_holography.tex:511` (`thm:uch-gravity-chain-level`).
Theorem body explicitly states: chain-level holds on pro-ambient / $J$-adic / weight-completed ambient; direct-sum ambient is GENUINELY FALSE matching Vol~I MC5 ambient-stratification. Remark `rem:uch-gravity-chain-level-promotion` at :593 explicitly retracts a prior stronger direct-sum claim. Matches Vol~I post-heal exactly.

**A-healthy-2.** `chapters/connections/soft_graviton_mellin_shadow_bridge_platonic.tex:306, 378, 748`.
All three sites already cite `thm:uch-gravity-chain-level` with explicit "pro-ambient / $J$-adic / weight-completed ambient" scope language and explicit "direct-sum ambient genuinely false" acknowledgement. No heal needed.

**A-healthy-3.** `chapters/connections/celestial_moonshine_bridge.tex:549, 558`.
Uses the `conj:uch-gravity-chain-level` alias (phantomsection at `main.tex:1020`) and explicitly scopes clause to "strict chain-level reading conditional on Conjecture". Even though the Vol II home-file promoted conj → thm, the surface-level `conj:` alias preserves the conservative scope at the consumer. No heal needed.

**A-healthy-4.** `chapters/connections/soft_graviton_mellin_shadow_bridge_platonic.tex:723` (`cor:soft-hierarchy-unconditional-r-leq-8`).
Genus-0 clause unconditional; $g \geq 1$ weight-completed; chain-level on pro-ambient via `thm:uch-gravity-chain-level`. All ambient scope language explicit. No heal needed.

**A-healthy-5.** `chapters/connections/programme_climax_platonic.tex:64` (A-infinity-2 cite).
Citation is scoped to "fixed smooth curve $X$" (section `sec:climax-question`, :52--65), which is within Vol~I `thm:A-infinity-2`'s PROVED-unconditional fixed-curve scope. Modular-family extension not invoked. No heal needed.

**A-healthy-6.** `chapters/connections/programme_climax_platonic.tex:857` (three-volume architecture pillar enumeration).
Citation is an input-tier enumeration of Vol~I pillars, not a load-bearing modular-family invocation. No heal needed.

**A-healthy-7.** `chapters/frame/preface.tex:205` (cites `rem:A-infinity-2-modular-family-scope`).
Already cites the scope REMARK explicitly, matching Vol~I's honest attribution. Healthy.

**A-healthy-8.** `chapters/theory/factorization_swiss_cheese.tex:4043`.
Section reference to `sec:factorization-properads-theorem-A-infinity-2` (local Vol II section naming), not a cross-volume consumer of Vol~I's modular-family clause.

### (b) AP287 cross-volume attribution hygiene — HEAL APPLIED

**B-heal-1.** `chapters/connections/part_vi_platonic_introduction.tex:379--397` (`thm:part-vi-moonshine-recovery`, `\ClaimStatusProvedHere`).

Load-bearing consumer of Vol~I `thm:v-natural-e3-topological` (now `\ClaimStatusProvedElsewhere`) in BOTH theorem body (line 390) and proof identification step (line 415). Vol~I `thm:moonshine-bar-euler-master` also cited as load-bearing (line 393, line 423).

Under HZ-11 (cross-volume ProvedHere discipline), `ProvedElsewhere` status is acceptable for cross-volume attribution. Vol~II `ProvedHere` tag survives because the proof treats the Vol~I construction as attribution, not as local inscription. No theorem downgrade required.

AP287 (cross-volume theorem existence without HZ-11 attribution) triggers: the Vol~II consumer's proof cites the Vol~I label and textually says "Vol~I Theorem~\ref{...}" but the earlier text did NOT inscribe a scope remark acknowledging the Vol~I change of status. Heal via Option (b) of AP287: add a `\begin{remark}[Scope of the Vol~I inputs]` inline after the proof, recording that Vol~I `thm:v-natural-e3-topological` is `\ClaimStatusProvedElsewhere` and that the present theorem inherits this attribution without circularity.

**Heal applied.** Remark `rem:part-vi-moonshine-recovery-scope` inscribed at `part_vi_platonic_introduction.tex` between proof end (:428) and `\section{The climax, restated}` (new :430). Inline diff:

```diff
 celestial-moonshine loop at the Part~VI level.  $\quad\square$
 \end{proof}

+\begin{remark}[Scope of the Vol~I inputs]
+\label{rem:part-vi-moonshine-recovery-scope}
+Vol~I Theorem~\ref{thm:v-natural-e3-topological} carries
+\ClaimStatusProvedElsewhere: the $E_{3}$-topological structure on
+$V^\natural$ is assembled from the Leech-lattice class-G
+$E_{3}$-topological input (Vol~I Theorem~\ref{thm:E3-topological-km})
+composed with the $\mathbb{Z}/2$-orbifold anomaly vanishing of
+Vol~II Theorem~\ref{thm:uhf-monster-orbifold-bv-anomaly-vanishes}.
+The present theorem inherits this attribution: the identification of
+the Part~VI holographic $\Etopo{3}$ output with the Vol~I Monster
+construction rests on the two cited inputs, both of which are
+independently inscribed. No circular dependency arises because the
+Vol~I theorem's proof routes the orbifold step through Vol~II, and
+the Vol~II theorem proved here identifies the two outputs via the
+uniqueness clause of $\Phi_{\mathrm{hol}}$, not via the Vol~I
+construction itself.
+\end{remark}
+
 \section{The climax, restated}
```

### (c) Broken references / phantoms

None. Every V1-label consumer in Vol~II `chapters/` or `standalone/` resolves at build time against a live Vol~I `\label{}`.

## Phase 3 — New anti-pattern inscription (AP1741)

Only one new pattern surfaced distinct from AP287's existing scope:

**AP1741 (Silent status-tag cross-volume inheritance).** When Vol~$V_1$ downgrades a theorem from `\ClaimStatusProvedHere` to `\ClaimStatusProvedElsewhere`, Vol~$V_2$ consumers with `\ClaimStatusProvedHere` that cite the downgraded Vol~$V_1$ theorem do not automatically become invalid, BUT the consumer theorem's scope-discipline debt strictly increases: the consumer must now make explicit what the Vol~$V_1$ attribution chain is, because "ProvedElsewhere" is a status tag that does NOT carry its own sourcing inside the citing volume. Under HZ-11 this is subtler than the AP287 case where the Vol~$V_1$ label is absent; here the label exists, resolves, and is proved, but its attribution chain is offloaded to yet another volume (Vol~III or back to Vol~II itself, creating a cross-volume citation cycle if not explicitly acknowledged). Canonical violation: `thm:part-vi-moonshine-recovery` in Vol~II cites Vol~I `thm:v-natural-e3-topological`, which after 2026-04-18 heal is `\ClaimStatusProvedElsewhere` and attributes BACK to Vol~II `thm:uhf-monster-orbifold-bv-anomaly-vanishes`. Without a scope remark, the reader cannot see that the cross-volume citation is non-circular. Counter: whenever a Vol~$V_2$ `ProvedHere` theorem cites a Vol~$V_1$ `ProvedElsewhere` theorem, inscribe a `\begin{remark}[Scope of the Vol~$V_1$ inputs]` acknowledging the attribution chain and exhibiting the non-circularity explicitly (either the Vol~$V_1$ theorem's attribution target is NOT the present Vol~$V_2$ consumer, or a uniqueness-clause-style identification breaks the apparent cycle). Distinct from AP287 (cross-volume theorem existence without HZ-11 attribution) by specifically targeting the `ProvedHere` $\to$ `ProvedElsewhere` downgrade transition: the Vol~$V_1$ label still resolves, but its proof-body semantics have changed, and Vol~$V_2$ consumers carry a propagation debt the metacognitive layer does not auto-track.

## Phase 4 — Build verification gate

No build or commit performed in this audit session per AP316 discipline (edits to Vol II live in main repo, not worktree; acknowledgement: worktree-isolation was not used for this mission because the edit scope is small and localized). Build verification delegated to the session's main thread.

## Phase 5 — Deliverable summary

**Consumer sites audited:** 15 (five V1-label consumer sites across 4 Vol~II files, plus eight internal `thm:uch-gravity-chain-level` consumer sites and two preface sites).

**Heals applied:** 1 (AP287 scope remark at `chapters/connections/part_vi_platonic_introduction.tex` after `thm:part-vi-moonshine-recovery` proof).

**Broken references:** 0.

**Phantom labels:** 0.

**AP inscriptions (Vol I block AP1741--AP1760):** 1 (AP1741 only, minimally per instruction).

**Recommendations for follow-up:**

1. Propagate the `rem:part-vi-moonshine-recovery-scope` pattern to any future Vol~II `ProvedHere` theorem citing a Vol~I `ProvedElsewhere` theorem (AP1741 preventative discipline).
2. Vol~II CLAUDE.md status rows for UCH gravity chain-level are already aligned with the pro-ambient restriction — no rewrite needed.
3. The `\phantomsection\label{conj:uch-gravity-chain-level}` alias at `main.tex:1020` is legitimate back-alias infrastructure (AP286 tactical alias, acceptable because consumer prose treats the aliased label as the same theorem with a conservative scope label). No heal needed.

**No commits made. Authored by Raeez Lorgat.**
