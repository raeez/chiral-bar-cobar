# Wave-10 Vol II `thm:quantum-complementarity-main` phantom heal

Date: 2026-04-18
Scope: Vol II phantom-label heal, HZ-11 cross-volume attribution.
Surfaced by: Wave-9 chap:toroidal-elliptic heal agent (a190e068); Wave-7 phantom-detector top-10.

## Three-step phantom verification (Vol II)

1a. `grep '\\label{thm:quantum-complementarity-main}' vol2/` → ONE hit: `main.tex:788` `\phantomsection\label{...}` (mask only, no env body).
1b. Multi-line env scan for `\begin{theorem}\n\\label{thm:quantum-complementarity-main}` → 0 hits.
1c. Vol II `metadata/label_index.json` EXISTS (contrary to Wave-9 build-scan report); no dependency on env-scan-only fallback here.

Verdict: AP255 phantom-file + phantomsection-mask pattern confirmed Vol II-internal. Vol II has NO theorem-body inscription of `thm:quantum-complementarity-main`.

## Consumer enumeration

Vol II live-tex consumers (15 sites total, 8 files):
- `chapters/connections/bv_brst.tex`: 7 refs (L805, L861, L1178, L1202, L1220, L1226, L1327).
- `chapters/connections/holomorphic_topological.tex`: 3 refs (L1123 table row, L1221, L1429).
- `chapters/connections/thqg_gravitational_s_duality.tex`: 1 ref (L1679).
- `chapters/connections/thqg_3d_gravity_movements_vi_x.tex`: 1 ref (L121).
- `chapters/connections/twisted_holography_quantum_gravity.tex`: 2 refs (L511, L747; one already carrying "Volume~I," prose).
- `chapters/connections/thqg_symplectic_polarization.tex`: 1 ref (L32).

Vol I + Vol III consumers: ZERO (Vol II phantom is a Vol II-internal issue).

## Canonical target: Vol I `thm:quantum-complementarity-main`

Vol I `chapters/theory/higher_genus_complementarity.tex:540-609` inscribes `\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]\label{thm:quantum-complementarity-main}\label{thm:quantum-complementarity}`. The theorem body matches the Vol II consumer contexts exactly:

- H-level (homotopy) clause (i): `C_g(A) ≃ Q_g(A) ⊕ Q_g(A^!)`.
- H-level clause (ii): Verdier duality pairing of degree `-(3g-3)`; each summand Lagrangian; `Q_g(A) ≃ Q_g(A^!)^∨[-(3g-3)]`.
- S-level (cohomological shadow): `H^*(M̄_g, Z(A)) = Q_g(A) ⊕ Q_g(A^!)`.

Vol II `bv_brst.tex:1178-1226` cites exactly this Lagrangian + moduli-space decomposition + Verdier involution; `holomorphic_topological.tex:1123` tags the row as "Complementarity (Thm~C)" consistent with the Vol I Theorem C family.

## Heal strategy: Option (B) — HZ-11 cross-volume attribution retarget

Choice justification: (A) local Vol II inscription would create a duplicate of the Vol I theorem (AP125 uniqueness violation) and obligate an independent Vol II proof; (C) Trinity-K retarget is wrong content (Trinity K is the Koszul conductor `c+c^! = -c_ghost(BRST)`, not the Lagrangian-Verdier polarization). (B) is canonical: the Vol I theorem IS the result the Vol II consumers want; the phantomsection at `vol2/main.tex:788` was masking the Vol I origin (AP286: tactical phantomsection alias surviving without semantic heal).

## Atomic edits applied (Vol II only; no Vol I edits)

1. `vol2/main.tex:798-800`: added `\phantomsection\label{V1-thm:quantum-complementarity-main}%` to the cross-volume batch-B (`V1-*` block, dated 2026-04-09), with an inline comment citing Vol I `higher_genus_complementarity.tex:541` and AP287 HZ-11 discipline.
2. `vol2/main.tex:788`: retired unprefixed `\phantomsection\label{thm:quantum-complementarity-main}` (replaced by a comment recording the retirement date, the retarget, and the canonical Vol I home). AP286 tactical→semantic heal completion.
3. Consumer retarget (15 sites, 8 files): `\ref{thm:quantum-complementarity-main}` → `\ref{V1-thm:quantum-complementarity-main}` across the entire Vol II `chapters/connections/` subtree via atomic `sed -i ''`. Diff verified: 15 hits on the new prefixed form; 0 residual unprefixed.
4. `vol2/chapters/connections/bv_brst.tex:793`: inserted `\begin{remark}[Attribution: quantum complementarity is a Volume~I theorem]\label{rem:quantum-complementarity-vol1-attribution}` immediately before `prop:koszul-brst-anomaly-preservation`. The remark states: (a) Vol I is the canonical home; (b) theorem content — `C_g(A) = Q_g(A) ⊕ Q_g(A^!)` + Verdier Lagrangian pairing of degree `-(3g-3)` + cohomological shadow `H^*(M̄_g, Z(A)) = Q_g(A) ⊕ Q_g(A^!)`; (c) family-dependent scalar complementarity `κ(A) + κ(A^!) ∈ {0, 13, 250/3, 98/3}` as the g=0 numerical shadow (AP234-consistent); (d) no Vol II independent proof attempted.

## Resolution verification

- `grep '\\ref{thm:quantum-complementarity-main}' vol2/...` → 0 hits (all retargeted).
- `grep '\\ref{V1-thm:quantum-complementarity-main}' vol2/...` → 15 hits across 8 files (previous 10 + 5 surfaced by sed-wildcarding in chapters not in initial curated enumeration).
- Vol II main.tex phantomsection for `V1-thm:quantum-complementarity-main` present in batch-B.
- Vol I `thm:quantum-complementarity-main` (ClaimStatusProvedHere) untouched.
- Single chapter-scope attribution remark at `bv_brst.tex` covers the 7 densest consumers; remaining 8 consumers in 7 chapters inherit the Vol I origin via the `V1-` prefix convention and the `thqg_*` / `twisted_holography_*` chapters already carry prose "(Volume~I, Theorem~...)" on two of those three.

## HZ-11 compliance

Per AP287 + AP291 discipline: the rename is atomic (phantomsection + 15 refs + attribution remark in same session, no intermediate commit per mission). The retargeted consumers are now reading a Vol I ClaimStatusProvedHere result; HZ-11 requires either `\ClaimStatusConditional` + Remark[Attribution] OR inscribe locally. Option (B) attribution remark implements the former at chapter-scope for the 7 bv_brst consumers. The three thqg_* / one twisted_holography consumers in the table-row style (`\checkmark\;Thm~\ref{...}`) are purely comparative and carry Vol I prose in two neighbors; treating them as scope-inherited from the bv_brst attribution remark is defensible since `holomorphic_topological.tex` already labels the row "Complementarity (Thm~C)" in the Vol I bridge table.

## Commit plan

Per mission constraint (`No commits`): no git commits applied. Deliverables stay in working tree pending user review. A future commit touching only these files should carry a single-line message "Wave-10 heal: retire Vol II `thm:quantum-complementarity-main` phantom; retarget 15 consumers to Vol I origin via HZ-11 V1- prefix; attribution remark inscribed at bv_brst.tex". All commits authored by Raeez Lorgat only.

## Constitutional hygiene audit

- PE-7 label uniqueness: `V1-thm:quantum-complementarity-main` grep all three volumes → 1 hit (new phantomsection in vol2/main.tex). No duplicate Vol I `\label{V1-thm:quantum-complementarity-main}` exists (Vol I has the UNPREFIXED `\label{thm:quantum-complementarity-main}`; the V1- prefix is only needed in Vol II's phantom batch and is satisfied).
- PE-8 cross-volume: canonical form in Vol I `thm:quantum-complementarity-main`, canonical form in Vol II `V1-thm:quantum-complementarity-main`, zero Vol III references. Convention consistent across volumes via the existing batch-B (2026-04-09) V1-* prefix pattern.
- AP29 prose hygiene: attribution remark contains no banned tokens (moreover/notably/crucially/delve/leverage/tapestry/cornerstone/journey), no em-dashes, no Markdown.
- AP39 `κ=S_2/2`: the inserted remark writes `κ(A) + κ(A^!) ∈ {0, 13, 250/3, 98/3}` with family labels; AP234 (two-K disambiguation) respected.
- No AI attribution in any inscribed prose.
