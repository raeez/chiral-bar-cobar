# Wave 1 (2026-04-18) — Super-Yangian κ + κ^! = max(m, n) attack-and-heal

**Scope.** The super-Yangian complementarity identity advertised as the
successor of the retracted B86 "sum = 0" Virasoro-analogy, inscribed at:

- Vol I `chapters/examples/yangians_foundations.tex:103` — `lem:super-trace-berezinian-bridge` (the claimed central-automorphism bridge σ_{sBer}).
- Vol I `chapters/frame/programme_overview_platonic.tex:525-540` — the programme-overview prose advertising both pairings.
- Vol II `chapters/theory/super_chiral_yangian.tex:622-747` — `thm:super-complementarity-max-mn` (the actual theorem body) + `rem:two-pairings-supertrace-berezinian`.
- Vol II `chapters/theory/super_chiral_yangian.tex:792-806` — cross-volume bridge attaching the (4,20) specialisation to `Y(\fgl(4|20))`.
- Vol II `chapters/theory/super_chiral_yangian.tex:1072-1101` — cross-volume bridge section restating Vol III upgrade under the `\fgl` name.
- Vol II `chapters/theory/unified_chiral_quantum_group.tex:653` — K3 target via `\fgl(4|20)` super-Yangian.
- Vol II `chapters/theory/grt_parametrized_seven_faces.tex:937`, `chapters/connections/dnp_identification_master.tex:889` — further Vol II consumers under `\fgl` name.
- Vol III `chapters/examples/k3_yangian_chapter.tex:1857-2025` — osp super-Yangian definition + `rem:gl-to-osp-correction`.
- Vol III `main.tex:967,1083`, `chapters/examples/quantum_group_reps.tex:1058`, `chapters/examples/super_riccati_shadow_tower_platonic.tex` (multiple) — consumers carrying max(m,n).

The CLAUDE.md brief advertised `yangians_foundations.tex` as a Vol II file;
it is a Vol I file. This location drift is itself an AP291-variant
(phantom file name at advertised volume).

---

## 1. Attack ledger

| # | file:line | severity | category | finding |
|---|-----------|----------|----------|---------|
| F1 | Vol II `super_chiral_yangian.tex:692-695` | **HIGH** | AP272 folklore citation + AP259 tautological | Step 3 asserts "Berezinian contributes max(m,n) to the super-trace formula" citing Gow 2006 Thm 5.1. Gow's Thm 5.1 gives the leading coefficient of `\sBer(T(u))` as a graded determinantal polynomial; it does NOT state a shadow-depth shift of magnitude max(m,n). The value max(m,n) is pattern-matched across the table `(2,1), (2,2), (3,2), (4,3)` to match the identity being proved. The proof is circular: the Berezinian shift is defined to be whatever closes the identity, not derived from an independent Casimir / Sugawara / reflection-equation computation. |
| F2 | Vol II `super_chiral_yangian.tex:700-701` | **HIGH** | AP155 novelty + AP244 rank-count coincidence | "ψ(2\|2) gives max(2,2) = 2 which matches Beisert's central-extension counting." Beisert 2007 §3 exhibits **three** central elements (P, K, C) in the extended ψ(2\|2) ⊕ ℂ³ relevant to AdS/CFT integrability. The match "2 = 2" is rank of the quotient Cartan centre, NOT count of Beisert's centrals; the Vol I preface (`programme_overview_platonic.tex:535-540`) records this correctly as centre-rank, but the Vol II proof cites it as supporting evidence. Coincidence at (2,2) is not independent verification (AP186 — coincidental agreement masks bugs). |
| F3 | Vol II `super_chiral_yangian.tex:799-800` | **CRITICAL** | AP279 semantic-drift under rename | Cross-volume bridge reads `κ^super(Y(\fgl(4\|20))) + κ^super(Y(\fgl(4\|20))^!) = max(4,20) = 20`. Vol III renamed to `Y_{\osp(4\|20)}` (k3_yangian_chapter.tex:1921, `rem:gl-to-osp-correction`). Under the rename, the Step 1 super-Sugawara formula used by Vol II — `(k+h^∨_s)sdim(g)/(2 h^∨_s)` with `h^∨_s = m-n` for `sl(m\|n)` — does NOT transport to `osp(m\|n)`. The orthosymplectic dual Coxeter is `h^∨_{osp} = m - n - 2` (Arnaudon-Crampe-Doikou-Frappat-Ragoucy 2003), and the osp reflection-equation Shapovalov pairing is a DIFFERENT algebraic object from the `\fgl`/`\fsl` super-trace pairing. Vol II still carries the Vol III tag under the `\fgl` name in at least 10 sites (super_chiral_yangian.tex lines 87, 104, 131, 792, 799-800, 1072-1101; unified_chiral_quantum_group.tex:653; grt_parametrized_seven_faces.tex:937; dnp_identification_master.tex:889). The value "20" has not been re-derived for osp(4\|20). |
| F4 | Vol II `super_chiral_yangian.tex:622-647` | MED | AP193 biconditional forward-only | Theorem statement bounds scope to `\fsl(m\|n)` with `m ≠ n` (or `\fpsl(2\|2)` in the degenerate case), but the proof Step 1 uses the formula `(k+m-n)(m²-n²)/(2(m-n))` which simplifies to `(k+m-n)(m+n)/2` ONLY when `m ≠ n`. At `m = n`, the Step 1 formula is `0/0`, not `(k+0)(2m)/2 = km`. The `\fpsl(2\|2)` case cannot be recovered as a "degenerate case" of Step 1; it requires a separate proof, which is not inscribed. The four cited verification points `(2,1), (2,2), (3,2), (4,3)` include `(2,2)` which belongs to the `m = n` regime not covered by the formula; the `(2,2)` check is therefore vacuous relative to the stated proof. |
| F5 | Vol I `yangians_foundations.tex:103-142` | MED | AP242 forward-reference + AP277 vacuous verification | `lem:super-trace-berezinian-bridge` clause (c) says "multiplication by `\sBer(T(u))\|_{u=0}` defines an algebra automorphism σ_{sBer}: Z(A) → Z(A) of the centre, whose action on shadow depth is the additive shift κ^{sBer} = κ^{str} + (1/2)max(m,n)". The proof body cites Nazarov 1991 for centrality of `\sBer(T(u))` and Gow 2006 Prop 4.3 for non-degeneracy off `\fpsl(2\|2)`. Neither primary source gives a shadow-depth shift formula. The (1/2)·max(m,n) value is inferred from clauses (a) and (b), so clause (c) is a consequence of the identity it is supposed to bridge, not an independent structural theorem. The HZ-IV block at lines 78-102 claims three disjoint verification paths (V1 super-PBW + super-Sugawara; V2 quantum Berezinian; V3 AdS/CFT central-extension count); V1 is Vol II Step 1-2 which gives ZERO (super-trace side), V2 is the Gow-Molev attribution that is precisely what is under attack, V3 is the coincidental (2,2) match from F2. The three paths are bibliographically disjoint but all downstream-pass through the same unverified Berezinian-shift claim. |
| F6 | Vol II `super_chiral_yangian.tex:740-747` | MED | AP241 advertised-but-open | Remark (II) scope: "Above the sub-Sugawara line (k+h^∨_s > m+n) the Berezinian shift is buried in higher-order corrections to T^s_Sug that have not been computed in closed form, and a uniform programme-level canonicalisation between the two pairings is the genuine remaining frontier (F4 addendum)." The advertised identity is thus scope-restricted to the sub-Sugawara line, and even there the Berezinian shift is the unverified step of F1. The CLAUDE.md "PROVED" / status-table phrasing does not reflect this scope. |
| F7 | Vol II `super_chiral_yangian.tex:625` (theorem header) | LOW | AP43 central object property-list | The theorem statement says "(where h^∨_s is the super-dual Coxeter number, equal to m - n for sl(m\|n) and to 0 for psl(2\|2))". For psl(2\|2), h^∨_s = 0 means super-Sugawara is singular (division by (k+0) in Step 1 formula is already critical-level); the theorem statement's degenerate-case clause does not resolve this. |

---

## 2. Surviving core (Drinfeld-style)

On the sub-Sugawara line of `sl(m|n)` with `m ≠ n`, the super-trace
shadow sum `κ^str(A) + κ^str(A^!) = 0` is **proved unconditionally** by
a direct super-Sugawara computation (Step 1-2 of Vol II
`thm:super-complementarity-max-mn`), mirroring the bosonic Feigin-Frenkel
involution `k ↦ -k - 2h^∨_s` on the super-Yangian Koszul dual. The
stronger Berezinian identity `κ^{sBer} + κ^{sBer,!} = max(m,n)` is a
structural hypothesis about the relative normalisation of the two
shadow pairings; its shift-by-max(m,n) magnitude is at present
pattern-matched, not derived. The correct programme statement is
therefore: two pairings coexist on the sub-Sugawara line, the
super-trace pairing gives 0 as a theorem, the Berezinian pairing gives
max(m,n) as a conjecture bridged by σ_{sBer}; the sub-Sugawara-line
restriction and the osp-versus-gl rename propagation are both open.

---

## 3. Heal per finding

| # | finding | heal | new status |
|---|---------|------|------------|
| F1 | Berezinian shift asserted, not derived | Downgrade Step 3 Berezinian-sum identity to **Conjectured**; inscribe the super-trace identity as a **Theorem** (Steps 1-2 only, genuinely proved); add `\begin{conjecture}[Berezinian shift magnitude]` stating κ^{sBer} − κ^{str} = (1/2)·max(m,n) per side on the sub-Sugawara line, ClaimStatusConjectured, with a Remark[Scope] stating the Gow/Nazarov citations establish centrality of `\sBer(T(u))` but not the magnitude of the shadow-depth shift. | `thm:super-complementarity-max-mn` split into `thm:super-complementarity-supertrace-zero` (PROVED, κ+κ^! = 0) + `conj:super-complementarity-berezinian-max-mn` (CONJECTURED, κ^{sBer}+κ^{sBer,!} = max(m,n)) |
| F2 | Beisert (2,2) match is rank-coincidence | Restate the ψ(2\|2) clause as a rank-match observation (clarifying that Beisert 2007 has THREE centrals P, K, C but their quotient by the Lie bracket closure produces a rank-2 centre), tag it as supporting evidence, not verification. | Remark demoted; theorem unchanged by this finding |
| F3 | AP279 gl-vs-osp rename semantic drift at (4,20) | Atomic rename across Vol II of `Y(\fgl(4\|20))` → `Y_{\osp(4\|20)}` in the 10 consumer sites, AND re-state the `max(4,20) = 20` specialisation as CONJECTURAL pending a separate derivation for osp(m\|n). The osp Step 1 formula uses `h^∨_{osp} = m-n-2` (Arnaudon et al. 2003) and the reflection-equation Shapovalov pairing, both distinct from the `\fgl`/`\fsl` super-trace pairing. | Value "20" tagged CONJECTURAL at (4,20); cross-volume propagation logged as Open Frontier F26b (super-complementarity osp re-derivation) |
| F4 | Step 1 formula 0/0 at m=n; `\fpsl(2\|2)` not in stated proof | Theorem scope restricted to m ≠ n explicitly; ψ(2\|2) case downgraded to Remark with CONJECTURAL status; "(2,2)" removed from the small-rank verification table. | Theorem scope tightened to m ≠ n |
| F5 | Vol I bridge lemma clause (c) circular | Replace clause (c) "algebra automorphism whose action on shadow depth is +(1/2)max(m,n)" with "the super-trace and Berezinian pairings are related by the central element `\sBer(T(u))\|_{u=0}` acting by multiplication on Z(A) (PROVED via Nazarov); the numerical gap between their shadow-depth contributions is (1/2)max(m,n) in the Berezinian normalisation (CONJECTURED, same as F1)". The lemma becomes a Proposition + Conjecture pair, not a theorem. | Split into `prop:super-berezinian-central-automorphism` (PROVED centrality, ProvedElsewhere) + `conj:super-berezinian-shadow-shift-magnitude` (CONJECTURED shift value). HZ-IV block heal: replace V2/V3 with "V2-revised = exhaustive rank-1/rank-2 super-Sugawara shadow-depth computation; V3-revised = symbolic Berezinian expansion in the quantum-minor basis"; or add `HZ-IV-W8-B` flag acknowledging primitive-tautology scope if no genuine disjoint numerical observable exists. |
| F6 | Scope above sub-Sugawara line open | Add explicit scope tag in the Vol II theorem header and the Vol I preface prose: "on the sub-Sugawara line k+h^∨_s ≤ m+n; above the sub-Sugawara line the identity is an open frontier (F4 addendum)." | Scope tag propagated |
| F7 | ψ(2\|2) h^∨_s = 0 singular | Remark noting critical-level obstruction at ψ(2\|2); proof scope excludes this case; the Vol I preface centre-rank observation retained as orientation only. | Scope tag |

---

## 4. Commit plan (no commits this run)

Per the CLAUDE.md no-commit constraint for this session, the heals are
described as a commit-plan. Each commit is atomic (AP5 + AP149):

1. **Commit 1 (Vol II `thm:super-complementarity-max-mn` split).** Split the Vol II theorem into `thm:super-complementarity-supertrace-zero` (PROVED, Steps 1-2 only) and `conj:super-complementarity-berezinian-max-mn` (CONJECTURED, Step 3 content). Edit `super_chiral_yangian.tex:622-702`. Scope to m ≠ n. Move the ψ(2\|2) clause to a separate `rem:psl-2-2-shadow-depth` with status Heuristic.
2. **Commit 2 (Vol II AP279 rename).** Rename `Y(\fgl(4\|20))` → `Y_{\osp(4\|20)}` in all ten Vol II consumer sites identified above. Insert `\providecommand{\osp}{\mathfrak{osp}}` guard. At the load-bearing identity (lines 799-800), tag value "20" as CONJECTURAL (depending on osp(m\|n) super-Sugawara re-derivation). Add `rem:vol-ii-osp-rename-caveat` cross-referencing Vol III `rem:gl-to-osp-correction`.
3. **Commit 3 (Vol I `lem:super-trace-berezinian-bridge` split).** Split the Vol I lemma (`yangians_foundations.tex:103-172`) into `prop:super-berezinian-central-automorphism` (centrality of `\sBer(T(u))` on Z(A) via Nazarov 1991) and `conj:super-berezinian-shadow-shift-magnitude` (the (1/2)max(m,n) shift). Revise HZ-IV block: flag as HZ-IV-W8-B (primitive-tautology) or replace V3 (AdS/CFT central-extension count) with a genuinely disjoint rank-1 super-Sugawara exhaustive verification path.
4. **Commit 4 (Vol I `programme_overview_platonic.tex` scope).** Add scope tag "on the sub-Sugawara line k+h^∨_s ≤ m+n" to lines 525-540; restate max(m,n) value as CONJECTURAL per Commit 1.
5. **Commit 5 (Vol III consumer propagation).** In `main.tex:967,1083`, `chapters/examples/quantum_group_reps.tex:1058`, `chapters/examples/super_riccati_shadow_tower_platonic.tex:26,34,86,90,96,628,640,647,696,726,729,740,747,748,753,754`: tag each max(m,n) occurrence with ClaimStatusConjectured and reference Vol II `conj:super-complementarity-berezinian-max-mn` (or the Vol I proposition-conjecture split).
6. **Commit 6 (CLAUDE.md update).** Update B86 entry across all three volumes to read: "super-trace κ+κ^! = 0 PROVED on sub-Sugawara line for sl(m\|n), m ≠ n; Berezinian κ^{sBer}+κ^{sBer,!} = max(m,n) CONJECTURED (Berezinian shift magnitude unverified at primary source)." Add AP287 cross-reference noting Vol II `thm:super-complementarity-max-mn` originally inscribed as PROVED is split. Add AP288 (stale session ledger) cross-reference noting `adversarial_swarm_20260417/wave1_cross_volume_identities_attack_heal.md` §F2 is updated by the present note.
7. **Commit 7 (Open Frontier F26b).** In Vol I `FRONTIER.md` or equivalent, open new frontier F26b: "super-complementarity osp(m\|n) re-derivation". Record Arnaudon-Crampe-Doikou-Frappat-Ragoucy 2003 as the primary-source entry point; Gow-Molev 2010 and Gow 2006 as the gl(m\|n) reference; note that the shift magnitude for osp may differ from max(m,n) and depends on the reflection-equation Shapovalov form.

Verification gates per commit: build passes (pdflatex); tests pass
(`make test`); pre-commit metadata grep zero-hit (no AP tokens in .tex
outside % comments); HZ-IV decorator check on any modified test file.

No AI attribution. Author: Raeez Lorgat.

---

## 5. PE-2 kappa template snapshot (executed for F3 (4,20) specialisation)

```
## PRE-EDIT: kappa
family:                    super-Yangian Y_hbar(sl(4|20)) on sub-Sugawara line
kappa formula written:     (k + m - n)(m+n)/2 at Sugawara, super-trace pairing
census citation:           Vol II super_chiral_yangian.tex:659-660 (Step 1)
match?                     Y (super-trace)
AP39 uniqueness: is kappa = S_2?  N (super-Sugawara, not Virasoro)
evaluation paths:
  at k=0:                  (m-n)(m+n)/2 = (m^2-n^2)/2 = sdim(sl(m|n))/2
  at k=-h^v_s (critical):  0
  at (m,n) = (4,20):       (k-16)(24)/2 = 12(k-16); at k=0 gives -192 = (4-400)/2 = -198? No: sdim(sl(4|20)) = 16-400 = -384; sdim/2 = -192 OK
  Koszul dual:             (-k - (m-n))(m+n)/2; at k=0 gives (m-n)(m+n)/2 WITH OPPOSITE SIGN
  sum:                     0 (super-trace pairing, PROVED)
AP136 boundary (W_N):      NA (super-Yangian, not W_N)
wrong variants avoided:
  NOT sum = max(m,n) WITHOUT Berezinian correction
  NOT sum = 0 under Berezinian pairing (claim is max(m,n))
Berezinian shift source:   Vol II super_chiral_yangian.tex:687-696 (Step 3, CIRCULAR — Gow 2006 Thm 5.1 cited but only gives centrality, not shift magnitude)
Open Frontier:              F26b osp(m|n) re-derivation
verdict:                   ACCEPT for super-trace identity; REJECT for Berezinian identity (downgrade to Conjecture)
```
